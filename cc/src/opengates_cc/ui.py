from __future__ import annotations

from dataclasses import dataclass

import yaml

from opengates.gates import GateBundle


@dataclass(frozen=True)
class DeskPresentation:
    headline: str
    body: str
    assistant_status: str
    assistant_avatar: str
    composer_placeholder: str
    invited_topics: list[str]
    principal_handle: str
    payment_enabled: bool
    ante_amount: str | None


def load_presentation(gate: GateBundle) -> DeskPresentation:
    config_path = gate.path / "gate.yaml"
    config = {}
    if config_path.exists():
        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}

    default_body = (
        "Pick the track that fits best, then send the clearest version of your ask. "
        "This desk may ask a few follow-up questions before it decides."
    )
    invited_topics = config.get("invited_topics") or gate.focus_items[:6]
    return DeskPresentation(
        headline=config.get("welcome_headline") or f"Hi, I'm {gate.assistant_name}.",
        body=config.get("welcome_body") or default_body,
        assistant_status=config.get("assistant_status") or "Reviewing inbound now",
        assistant_avatar=config.get("assistant_avatar") or "IA",
        composer_placeholder=config.get("composer_placeholder") or "Share the context, links, ask, and what makes this timely.",
        invited_topics=[str(item).strip() for item in invited_topics if str(item).strip()],
        principal_handle=str(config.get("principal_handle") or "ante").strip() or "ante",
        payment_enabled=bool(config.get("payment_enabled")),
        ante_amount=str(config.get("ante_amount")).strip() if config.get("ante_amount") is not None else None,
    )
