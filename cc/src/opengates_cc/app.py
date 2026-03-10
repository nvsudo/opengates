from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Form, HTTPException, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from opengates.gates import GateLoader
from opengates.providers import build_provider
from opengates.runtime import GateRuntime
from opengates.schemas import ApiThreadCreateRequest, ApiThreadReplyRequest
from opengates.storage import LocalStore

from .settings import get_settings
from .ui import load_presentation


def create_app() -> FastAPI:
    settings = get_settings()
    gate_loader = GateLoader(settings.gates_dir)
    store = LocalStore(settings.data_dir)
    runtime = GateRuntime(gate_loader=gate_loader, store=store, provider=build_provider(settings))

    app = FastAPI(title="OpenGates CC")
    templates = Jinja2Templates(directory=str(Path(__file__).with_name("templates")))

    @app.get("/", response_class=HTMLResponse)
    def index(request: Request) -> HTMLResponse:
        desks = []
        for gate_id in gate_loader.list_gates():
            bundle = gate_loader.load(gate_id)
            desks.append(
                {
                    "gate_id": gate_id,
                    "title": bundle.title,
                    "assistant_name": bundle.assistant_name,
                    "public_path": bundle.public_path,
                    "preview": " · ".join(bundle.focus_items[:3]),
                }
            )
        return templates.TemplateResponse(request, "index.html", {"desks": desks})

    @app.get("/demo", response_class=HTMLResponse)
    def demo_desk(request: Request) -> HTMLResponse:
        return desk_intake(request, "demo-investor")

    @app.get("/g/{gate_id}", response_class=HTMLResponse)
    def desk_intake(request: Request, gate_id: str) -> HTMLResponse:
        try:
            gate = gate_loader.load(gate_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        presentation = load_presentation(gate)
        return templates.TemplateResponse(
            request,
            "intake.html",
            {"gate": gate, "presentation": presentation},
        )

    @app.post("/g/{gate_id}/threads")
    def create_thread_form(
        gate_id: str,
        name: str = Form(""),
        email: str = Form(""),
        topic: str = Form(""),
        content: str = Form(...),
        priority_paid: str | None = Form(None),
    ) -> RedirectResponse:
        try:
            processed = runtime.start_thread(
                gate_id,
                name=name,
                email=email,
                content=_compose_intake_content(topic=topic, content=content),
                payment_status="paid" if priority_paid else "none",
                source="web_thread",
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return RedirectResponse(url=f"/t/{processed.thread.thread_id}", status_code=303)

    @app.get("/t/{thread_id}", response_class=HTMLResponse)
    def thread_view(request: Request, thread_id: str) -> HTMLResponse:
        try:
            view = runtime.get_thread_view(thread_id)
            gate = gate_loader.load(view.thread.gate_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        presentation = load_presentation(gate)
        closed = view.thread.status in {"declined", "escalated", "expired", "review"}
        return templates.TemplateResponse(
            request,
            "thread.html",
            {
                "gate": gate,
                "presentation": presentation,
                "thread_view": view,
                "thread_closed": closed,
                "thread_status_label": _thread_status_label(view.thread.status),
            },
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

    @app.get("/favicon.ico")
    def favicon() -> Response:
        return Response(status_code=204)

    @app.post("/api/gates/{gate_id}/threads")
    def api_create_thread(gate_id: str, payload: ApiThreadCreateRequest) -> dict:
        try:
            processed = runtime.start_thread(
                gate_id,
                name=payload.name,
                email=payload.email,
                content=payload.content,
                payment_status=payload.payment_status,
                source="api",
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return processed.model_dump(mode="json")

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
                payment_status=payload.payment_status,
                source="api",
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return processed.model_dump(mode="json")

    return app


def _compose_intake_content(*, topic: str, content: str) -> str:
    if topic.strip():
        return f"Topic: {topic.strip()}\n\n{content.strip()}"
    return content.strip()


def _thread_status_label(status: str) -> str:
    labels = {
        "waiting_on_sender": "awaiting reply",
        "declined": "closed",
        "escalated": "escalated",
        "review": "needs review",
        "evaluating": "reviewing",
        "open": "open",
        "expired": "expired",
    }
    return labels.get(status, status.replace("_", " "))


app = create_app()
