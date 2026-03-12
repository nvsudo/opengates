from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    package_root: Path
    config_root: Path
    bundled_gates_dir: Path
    user_gates_dir: Path
    gates_dir: Path
    data_dir: Path
    provider_name: str
    openai_api_key: str | None
    openai_model: str
    debug_prompts: bool
    smtp_host: str | None
    smtp_port: int
    smtp_username: str | None
    smtp_password: str | None
    smtp_use_tls: bool
    smtp_use_ssl: bool
    notification_from_email: str | None
    notification_from_name: str


def get_settings() -> Settings:
    package_root = Path(__file__).resolve().parent
    config_root = Path(os.getenv("OPENGATES_CONFIG_DIR", Path.cwd())).resolve()
    file_env = _read_env_file(config_root / ".env")
    file_env.update(_read_env_file(config_root / ".env.local"))

    bundled_gates_dir = package_root / "starter_gates"
    user_gates_dir = config_root / "gates"
    configured_gates_dir = _get_path_env("OPENGATES_GATES_DIR", file_env)
    if configured_gates_dir is not None:
        gates_dir = configured_gates_dir
    elif user_gates_dir.exists():
        gates_dir = user_gates_dir
    else:
        gates_dir = bundled_gates_dir

    data_dir = _get_path_env("OPENGATES_DATA_DIR", file_env) or (config_root / "data")
    provider_name = os.getenv("OPENGATES_PROVIDER", file_env.get("OPENGATES_PROVIDER", "heuristic"))
    openai_api_key = os.getenv("OPENAI_API_KEY", file_env.get("OPENAI_API_KEY"))
    openai_model = os.getenv("OPENGATES_OPENAI_MODEL", file_env.get("OPENGATES_OPENAI_MODEL", "gpt-5-mini"))
    debug_prompts = _as_bool(os.getenv("OPENGATES_DEBUG_PROMPTS", file_env.get("OPENGATES_DEBUG_PROMPTS", "0")))
    smtp_host = os.getenv("OPENGATES_SMTP_HOST", file_env.get("OPENGATES_SMTP_HOST"))
    smtp_port = int(os.getenv("OPENGATES_SMTP_PORT", file_env.get("OPENGATES_SMTP_PORT", "587")))
    smtp_username = os.getenv("OPENGATES_SMTP_USERNAME", file_env.get("OPENGATES_SMTP_USERNAME"))
    smtp_password = os.getenv("OPENGATES_SMTP_PASSWORD", file_env.get("OPENGATES_SMTP_PASSWORD"))
    smtp_use_tls = _as_bool(os.getenv("OPENGATES_SMTP_USE_TLS", file_env.get("OPENGATES_SMTP_USE_TLS", "1")))
    smtp_use_ssl = _as_bool(os.getenv("OPENGATES_SMTP_USE_SSL", file_env.get("OPENGATES_SMTP_USE_SSL", "0")))
    notification_from_email = os.getenv(
        "OPENGATES_NOTIFICATION_FROM_EMAIL",
        file_env.get("OPENGATES_NOTIFICATION_FROM_EMAIL"),
    )
    notification_from_name = os.getenv(
        "OPENGATES_NOTIFICATION_FROM_NAME",
        file_env.get("OPENGATES_NOTIFICATION_FROM_NAME", "OpenGates"),
    )
    return Settings(
        package_root=package_root,
        config_root=config_root,
        bundled_gates_dir=bundled_gates_dir,
        user_gates_dir=user_gates_dir,
        gates_dir=gates_dir,
        data_dir=data_dir,
        provider_name=provider_name,
        openai_api_key=openai_api_key,
        openai_model=openai_model,
        debug_prompts=debug_prompts,
        smtp_host=smtp_host,
        smtp_port=smtp_port,
        smtp_username=smtp_username,
        smtp_password=smtp_password,
        smtp_use_tls=smtp_use_tls,
        smtp_use_ssl=smtp_use_ssl,
        notification_from_email=notification_from_email,
        notification_from_name=notification_from_name,
    )


def _get_path_env(name: str, file_env: dict[str, str]) -> Path | None:
    raw = os.getenv(name, file_env.get(name))
    if raw is None or not raw.strip():
        return None
    return Path(raw).expanduser().resolve()


def _read_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}

    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip().strip("'").strip('"')
    return values


def _as_bool(raw: str) -> bool:
    return raw.strip().lower() in {"1", "true", "yes", "on"}
