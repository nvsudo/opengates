from __future__ import annotations

from textwrap import shorten

from .gates import GateBundle
from .schemas import Decision, PrincipalSummary, Thread, ThreadMessage


def ensure_principal_summary(
    gate: GateBundle,
    thread: Thread,
    sender_message: ThreadMessage,
    decision: Decision,
) -> Decision:
    if decision.decision != "escalate" or decision.principal_summary is not None:
        return decision
    decision.principal_summary = build_principal_summary(gate, thread, sender_message, decision)
    return decision


def build_principal_summary(
    gate: GateBundle,
    thread: Thread,
    sender_message: ThreadMessage,
    decision: Decision,
) -> PrincipalSummary:
    sender_label = _sender_label(thread)
    message_excerpt = _message_excerpt(sender_message.content)
    headline = shorten(f"{sender_label} may be worth reviewing", width=72, placeholder="...")
    summary = f"{sender_label} reached out through {gate.title} with: {message_excerpt}"
    why_this_matters = _why_this_matters(sender_message.content, decision)
    suggested_next_step = (
        "Review manually before replying."
        if decision.needs_review
        else "Review the thread and reply directly if you want to engage."
    )
    return PrincipalSummary(
        headline=headline,
        summary=summary,
        why_this_matters=why_this_matters,
        suggested_next_step=suggested_next_step,
    )


def build_escalation_email(
    gate: GateBundle,
    thread: Thread,
    sender_message: ThreadMessage,
    decision: Decision,
) -> tuple[str, str]:
    summary = decision.principal_summary or build_principal_summary(gate, thread, sender_message, decision)
    sender_label = _sender_label(thread)
    sender_email = thread.sender_email.strip() or "not provided"
    status_label = "Needs review" if decision.needs_review else "Escalated"
    subject = shorten(f"[{gate.title}] {summary.headline}", width=120, placeholder="...")
    body = "\n".join(
        [
            f"{status_label}: {gate.title}",
            "",
            summary.summary,
            "",
            "Why this matters",
            summary.why_this_matters,
            "",
            "Sender",
            f"- Name: {sender_label}",
            f"- Email: {sender_email}",
            "",
            "Decision context",
            f"- Thread: {thread.thread_id}",
            f"- Confidence: {decision.confidence:.2f}",
            f"- Tags: {', '.join(decision.tags) if decision.tags else 'none'}",
            "",
            "Latest sender message",
            sender_message.content.strip(),
        ]
    )
    if summary.suggested_next_step:
        body = "\n".join([body, "", "Suggested next step", summary.suggested_next_step])
    return subject, body


def _sender_label(thread: Thread) -> str:
    if thread.sender_name.strip():
        return thread.sender_name.strip()
    if thread.sender_email.strip():
        return thread.sender_email.strip()
    return "A sender"


def _message_excerpt(content: str) -> str:
    compact = " ".join(content.split())
    excerpt = shorten(compact, width=220, placeholder="...")
    if excerpt.endswith((".", "!", "?")):
        return excerpt
    return f"{excerpt}."


def _why_this_matters(content: str, decision: Decision) -> str:
    signals: list[str] = []
    reason = shorten(" ".join(decision.private_reason.split()), width=180, placeholder="...")
    if reason:
        signals.append(reason)
    lowered = content.lower()
    if any(token in lowered for token in ("revenue", "mrr", "arr", "customers", "growth", "traction", "users")):
        signals.append("The thread includes concrete traction or proof points.")
    if any(token in lowered for token in ("intro", "introduction", "mutual", "referred", "network")):
        signals.append("There is a clear relationship or timing hook worth checking.")
    if decision.tags:
        signals.append(f"Matched tags: {', '.join(decision.tags[:3])}.")
    if not signals:
        signals.append("The runtime judged this thread strong enough to deserve direct attention.")
    return " ".join(dict.fromkeys(signals))
