from __future__ import annotations

import smtplib
from abc import ABC, abstractmethod
from dataclasses import dataclass
from email.message import EmailMessage

from .settings import Settings


@dataclass(frozen=True)
class EscalationEmail:
    to_email: str
    subject: str
    text_body: str
    reply_to: str | None = None


class EscalationNotifier(ABC):
    @property
    @abstractmethod
    def enabled(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def send(self, email: EscalationEmail) -> None:
        raise NotImplementedError


class NoopEscalationNotifier(EscalationNotifier):
    @property
    def enabled(self) -> bool:
        return False

    def send(self, email: EscalationEmail) -> None:
        return None


class SmtpEscalationNotifier(EscalationNotifier):
    def __init__(
        self,
        *,
        host: str,
        port: int,
        from_email: str,
        from_name: str = "OpenGates",
        username: str | None = None,
        password: str | None = None,
        use_tls: bool = True,
        use_ssl: bool = False,
    ):
        self.host = host
        self.port = port
        self.from_email = from_email
        self.from_name = from_name
        self.username = username
        self.password = password
        self.use_tls = use_tls
        self.use_ssl = use_ssl

    @property
    def enabled(self) -> bool:
        return True

    def send(self, email: EscalationEmail) -> None:
        message = EmailMessage()
        message["From"] = f"{self.from_name} <{self.from_email}>"
        message["To"] = email.to_email
        message["Subject"] = email.subject
        if email.reply_to:
            message["Reply-To"] = email.reply_to
        message.set_content(email.text_body)

        smtp_cls = smtplib.SMTP_SSL if self.use_ssl else smtplib.SMTP
        with smtp_cls(self.host, self.port, timeout=15) as server:
            if not self.use_ssl and self.use_tls:
                server.starttls()
            if self.username:
                server.login(self.username, self.password or "")
            server.send_message(message)


def build_notifier(settings: Settings) -> EscalationNotifier:
    if not settings.smtp_host or not settings.notification_from_email:
        return NoopEscalationNotifier()
    return SmtpEscalationNotifier(
        host=settings.smtp_host,
        port=settings.smtp_port,
        from_email=settings.notification_from_email,
        from_name=settings.notification_from_name,
        username=settings.smtp_username,
        password=settings.smtp_password,
        use_tls=settings.smtp_use_tls,
        use_ssl=settings.smtp_use_ssl,
    )
