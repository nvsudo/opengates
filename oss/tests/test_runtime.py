import shutil

from fastapi.testclient import TestClient

from opengates.app import create_app
from opengates.gates import GateLoader
from opengates.notifications import EscalationEmail, EscalationNotifier
from opengates.providers import DecisionContext, DecisionProvider
from opengates.runtime import GateRuntime
from opengates.schemas import Decision
from opengates.settings import get_settings
from opengates.storage import LocalStore


class RecordingNotifier(EscalationNotifier):
    def __init__(self) -> None:
        self.emails: list[EscalationEmail] = []

    @property
    def enabled(self) -> bool:
        return True

    def send(self, email: EscalationEmail) -> None:
        self.emails.append(email)


class StaticEscalateProvider(DecisionProvider):
    def decide(self, context: DecisionContext) -> Decision:
        return Decision(
            thread_id=context.thread.thread_id,
            message_id=context.current_message.message_id,
            gate_id=context.gate.gate_id,
            decision="escalate",
            confidence=0.91,
            tags=["high-signal", "intro"],
            private_reason="Clear fit with concrete detail and a direct ask.",
            remaining_clarification_rounds=context.thread.remaining_clarification_rounds,
        )


def build_runtime(monkeypatch, tmp_path, *, provider=None, notifier=None, principal_email: str | None = None) -> GateRuntime:
    monkeypatch.setenv("OPENGATES_DATA_DIR", str(tmp_path / "data"))
    settings = get_settings()
    gates_dir = tmp_path / "gates"
    shutil.copytree(settings.gates_dir, gates_dir)
    if principal_email:
        gate_yaml = gates_dir / "demo-investor" / "gate.yaml"
        gate_yaml.write_text(
            gate_yaml.read_text(encoding="utf-8") + f"\nprincipal_email: {principal_email}\n",
            encoding="utf-8",
        )
    return GateRuntime(
        GateLoader(gates_dir),
        LocalStore(settings.data_dir),
        provider=provider,
        notifier=notifier,
    )


def test_thread_start_creates_clarify_turn(monkeypatch, tmp_path) -> None:
    runtime = build_runtime(monkeypatch, tmp_path)
    processed = runtime.start_thread(
        "demo-investor",
        name="Founder",
        email="founder@example.com",
        content="I am building an AI startup and would love to connect about a raise.",
    )
    assert processed.decision.decision == "clarify"
    assert processed.thread.status == "waiting_on_sender"
    assert processed.thread.remaining_clarification_rounds == 2


def test_thread_reply_can_escalate(monkeypatch, tmp_path) -> None:
    runtime = build_runtime(monkeypatch, tmp_path)
    first = runtime.start_thread(
        "demo-investor",
        name="Founder",
        email="signal@example.com",
        content="We are building applied AI software for finance teams and would love to connect.",
    )
    second = runtime.reply_to_thread(
        first.thread.thread_id,
        content=(
            "We are building applied AI software for finance-team reconciliation. We are at $35k MRR, "
            "22 paying customers, 18 percent monthly growth, and a founder in your network suggested "
            "we reach out. The specific ask is an investor intro."
        ),
    )
    assert second.decision.decision == "escalate"
    assert second.thread.status == "escalated"


def test_clarification_limit_forces_review(monkeypatch, tmp_path) -> None:
    runtime = build_runtime(monkeypatch, tmp_path)
    first = runtime.start_thread(
        "demo-investor",
        name="Founder",
        email="limit@example.com",
        content="We are building AI software for finance teams.",
    )
    first.thread.remaining_clarification_rounds = 0
    runtime.store.save_thread(first.thread)

    second = runtime.reply_to_thread(
        first.thread.thread_id,
        content="Still early, no traction yet, but this could be interesting.",
    )
    assert second.decision.needs_review is True
    assert second.thread.status == "review"


def test_bait_message_declines(monkeypatch, tmp_path) -> None:
    runtime = build_runtime(monkeypatch, tmp_path)
    processed = runtime.start_thread(
        "demo-investor",
        name="Troll",
        email="troll@example.com",
        content="I want to sell to you and pitch to you. to get your money. hahahaha....",
    )
    assert processed.decision.decision == "decline"
    assert processed.thread.status == "declined"


def test_http_thread_routes_work(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("OPENGATES_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(create_app())

    response = client.get("/demo")
    assert response.status_code == 200
    assert "Investor Gate" in response.text
    assert "Submit" in response.text
    assert "starts a bounded conversation" in response.text

    create = client.post(
        "/api/gates/demo-investor/threads",
        json={"name": "Founder", "email": "api@example.com", "content": "We are building applied AI software."},
    )
    assert create.status_code == 200
    thread_id = create.json()["thread"]["thread_id"]

    view = client.get(f"/api/threads/{thread_id}")
    assert view.status_code == 200
    assert view.json()["thread"]["thread_id"] == thread_id


def test_thread_page_hides_private_reason(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("OPENGATES_DATA_DIR", str(tmp_path / "data"))
    client = TestClient(create_app())

    create = client.post(
        "/api/gates/demo-investor/threads",
        json={"name": "Founder", "email": "private@example.com", "content": "I am building an AI startup and would love to connect."},
    )
    assert create.status_code == 200
    thread_id = create.json()["thread"]["thread_id"]

    page = client.get(f"/t/{thread_id}")
    assert page.status_code == 200
    assert "Private reason" not in page.text
    assert "Investor Gate" in page.text


def test_escalation_builds_principal_summary(monkeypatch, tmp_path) -> None:
    runtime = build_runtime(monkeypatch, tmp_path, provider=StaticEscalateProvider())
    processed = runtime.start_thread(
        "demo-investor",
        name="Founder",
        email="summary@example.com",
        content="We have 30 paying customers, strong growth, and want an investor intro.",
    )
    assert processed.decision.decision == "escalate"
    assert processed.decision.principal_summary is not None
    assert processed.decision.principal_summary.headline
    assert "Clear fit with concrete detail" in processed.decision.principal_summary.why_this_matters


def test_escalation_sends_email_when_configured(monkeypatch, tmp_path) -> None:
    notifier = RecordingNotifier()
    runtime = build_runtime(
        monkeypatch,
        tmp_path,
        provider=StaticEscalateProvider(),
        notifier=notifier,
        principal_email="principal@example.com",
    )
    processed = runtime.start_thread(
        "demo-investor",
        name="Founder",
        email="notify@example.com",
        content="We have 30 paying customers, strong growth, and want an investor intro.",
    )
    assert processed.thread.status == "escalated"
    assert len(notifier.emails) == 1
    assert notifier.emails[0].to_email == "principal@example.com"
    assert "Why this matters" in notifier.emails[0].text_body
    events = runtime.store.recent_events()
    assert any(event["type"] == "escalation_email_sent" for event in events)
