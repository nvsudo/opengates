from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from .gates import GateBundle, GateLoader
from .notifications import build_notifier
from .providers import build_provider
from .runtime import GateRuntime
from .schemas import ApiSubmissionRequest, ApiThreadCreateRequest, ApiThreadReplyRequest
from .settings import get_settings
from .storage import LocalStore


def create_app() -> FastAPI:
    settings = get_settings()
    gate_loader = GateLoader(settings.gates_dir)
    store = LocalStore(settings.data_dir)
    runtime = GateRuntime(
        gate_loader=gate_loader,
        store=store,
        provider=build_provider(settings),
        notifier=build_notifier(settings),
    )

    app = FastAPI(title="OpenGates")
    templates = Jinja2Templates(directory=str(Path(__file__).with_name("templates")))

    def load_gate(gate_id: str) -> GateBundle:
        try:
            return gate_loader.load(gate_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    def render_gate_intake(request: Request, gate_id: str) -> HTMLResponse:
        gate = load_gate(gate_id)
        return templates.TemplateResponse(request, "intake.html", {"gate": gate})

    def create_thread(
        gate_id: str,
        *,
        name: str,
        email: str,
        content: str,
    ) -> RedirectResponse:
        try:
            processed = runtime.start_thread(
                gate_id,
                name=name,
                email=email,
                content=content,
                source="web_thread",
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return RedirectResponse(url=f"/t/{processed.thread.thread_id}", status_code=303)

    @app.get("/", response_class=HTMLResponse)
    def index(request: Request) -> HTMLResponse:
        gates = []
        for gate_id in gate_loader.list_gates():
            bundle = gate_loader.load(gate_id)
            gates.append({"gate_id": gate_id, "title": bundle.title, "public_path": bundle.public_path})
        return templates.TemplateResponse(request, "index.html", {"gates": gates})

    @app.get("/g/{gate_id}", response_class=HTMLResponse)
    def gate_intake(request: Request, gate_id: str) -> HTMLResponse:
        return render_gate_intake(request, gate_id)

    @app.post("/g/{gate_id}/threads")
    def create_thread_form(
        gate_id: str,
        name: str = Form(""),
        email: str = Form(""),
        content: str = Form(...),
    ) -> RedirectResponse:
        return create_thread(gate_id, name=name, email=email, content=content)

    @app.post("/g/{gate_id}/submit")
    def submit_form_alias(
        gate_id: str,
        name: str = Form(""),
        email: str = Form(""),
        content: str = Form(...),
    ) -> RedirectResponse:
        return create_thread_form(
            gate_id=gate_id,
            name=name,
            email=email,
            content=content,
        )

    @app.get("/t/{thread_id}", response_class=HTMLResponse)
    def thread_view(request: Request, thread_id: str) -> HTMLResponse:
        try:
            view = runtime.get_thread_view(thread_id)
            gate = gate_loader.load(view.thread.gate_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        closed = view.thread.status in {"declined", "escalated", "expired", "review"}
        return templates.TemplateResponse(
            request,
            "thread.html",
            {"gate": gate, "thread_view": view, "thread_closed": closed},
        )

    @app.post("/t/{thread_id}/reply")
    def reply_to_thread_form(thread_id: str, content: str = Form(...)) -> RedirectResponse:
        try:
            runtime.reply_to_thread(thread_id, content=content, source="web_thread")
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return RedirectResponse(url=f"/t/{thread_id}", status_code=303)

    @app.get("/healthz")
    def healthz() -> dict:
        return {"ok": True}

    @app.get("/api/gates")
    def list_gates() -> dict:
        return {"gates": gate_loader.list_gates()}

    @app.post("/api/gates/{gate_id}/threads")
    def api_create_thread(gate_id: str, payload: ApiThreadCreateRequest) -> dict:
        try:
            processed = runtime.start_thread(
                gate_id,
                name=payload.name,
                email=payload.email,
                content=payload.content,
                source="api",
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return processed.model_dump(mode="json")

    @app.post("/api/gates/{gate_id}/submit")
    def api_submit_alias(gate_id: str, payload: ApiSubmissionRequest) -> dict:
        return api_create_thread(gate_id, payload)

    @app.get("/api/threads/{thread_id}")
    def api_get_thread(thread_id: str) -> dict:
        try:
            view = runtime.get_thread_view(thread_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return view.model_dump(mode="json")

    @app.post("/api/threads/{thread_id}/reply")
    def api_reply_to_thread(thread_id: str, payload: ApiThreadReplyRequest) -> dict:
        try:
            processed = runtime.reply_to_thread(
                thread_id,
                content=payload.content,
                source="api",
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return processed.model_dump(mode="json")

    @app.get("/api/logs/recent")
    def recent_logs(limit: int = 20) -> dict:
        return {"events": store.recent_events(limit=limit)}

    register_public_gate_routes(app, gate_loader, render_gate_intake, create_thread)

    return app

def register_public_gate_routes(app: FastAPI, gate_loader: GateLoader, render_gate_intake, create_thread) -> None:
    gate_ids = gate_loader.list_gates()
    public_paths: dict[str, str] = {}

    for gate_id in gate_ids:
        bundle = gate_loader.load(gate_id)
        if bundle.public_path.startswith("/api") or bundle.public_path.startswith("/t/"):
            raise RuntimeError(f"gate '{gate_id}' uses reserved public_path '{bundle.public_path}'")
        owner = public_paths.setdefault(bundle.public_path, gate_id)
        if owner != gate_id:
            raise RuntimeError(
                f"gates '{owner}' and '{gate_id}' share public_path '{bundle.public_path}'"
            )

    for gate_id in gate_ids:
        bundle = gate_loader.load(gate_id)
        if bundle.public_path == f"/g/{gate_id}":
            continue
        app.add_api_route(
            bundle.public_path,
            build_gate_public_endpoint(render_gate_intake, gate_id),
            methods=["GET"],
            response_class=HTMLResponse,
            include_in_schema=False,
            name=f"gate-public-{gate_id}",
        )
        app.add_api_route(
            bundle.thread_create_path,
            build_gate_create_endpoint(create_thread, gate_id),
            methods=["POST"],
            include_in_schema=False,
            name=f"gate-public-create-{gate_id}",
        )
        app.add_api_route(
            bundle.submit_path,
            build_gate_create_endpoint(create_thread, gate_id),
            methods=["POST"],
            include_in_schema=False,
            name=f"gate-public-submit-{gate_id}",
        )


def build_gate_public_endpoint(render_gate_intake, gate_id: str):
    def endpoint(request: Request) -> HTMLResponse:
        return render_gate_intake(request, gate_id)

    return endpoint


def build_gate_create_endpoint(create_thread, gate_id: str):
    def endpoint(
        name: str = Form(""),
        email: str = Form(""),
        content: str = Form(...),
    ) -> RedirectResponse:
        return create_thread(gate_id, name=name, email=email, content=content)

    return endpoint


app = create_app()
