# OpenGates

Source-available runtime for filtering inbound through conversation.

OpenGates lets you define what you care about in a few files, then handles the inbound thread for you: decline, ask a bounded follow-up, or escalate with a clean summary. It is the runtime behind [Ante](https://ante.so), the hosted product.

## What It Does

OpenGates is built for attention gating:
- define a gate with Markdown files instead of a large config surface
- run a threaded decision loop over inbound messages
- return one of three outcomes: `decline`, `clarify`, or `escalate`
- keep decision guardrails and persistence outside the model
- ship with a minimal FastAPI UI and HTTP endpoints you can build on

## Why This Exists

Outbound is getting cheaper every month. More agents will write to you, not fewer. If every inbound message can be polished, the bottleneck becomes judgment.

OpenGates is the runtime for that judgment layer:
- local-first by default
- file-based and auditable
- useful without mailbox access
- usable with heuristics today and stronger model providers later

## Status

- Source-available under Elastic License 2.0
- Python 3.10+
- Install from source today
- PyPI package name: `opengates`

## Quick Start

```bash
git clone https://github.com/nvsudo/opengates
cd opengates
uv sync
uv run opengates serve --host 127.0.0.1 --port 8000
```

Open [http://127.0.0.1:8000/demo](http://127.0.0.1:8000/demo).

The repo includes a starter gate under [`gates/demo-investor`](./gates/demo-investor). If you run from a clean working directory without a local `./gates`, OpenGates falls back to the bundled starter gate packaged with the runtime.

## Install Options

With `uv`:

```bash
uv sync
uv run opengates serve
```

With `pip`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
opengates serve
```

## How It Works

1. A sender starts a thread through the built-in UI or an external client.
2. OpenGates loads the gate bundle for that gate.
3. A decision provider evaluates the current turn.
4. The runtime enforces guardrails and returns `decline`, `clarify`, or `escalate`.
5. Thread state, messages, decisions, and sender profile data are persisted locally.
6. The built-in UI or your own frontend can render the next step.

## Gate Bundle

Each gate lives in `gates/<gate_id>/` and usually includes:

```text
gates/my-gate/
  focus.md
  standards.md
  voice.md
  examples.md
  gate.yaml
```

- `focus.md`: what the gate is for
- `standards.md`: what good looks like
- `voice.md`: how replies should sound
- `examples.md`: examples that sharpen judgment
- `gate.yaml`: optional UI and runtime settings

Common `gate.yaml` fields:

```yaml
title: Investor Gate
assistant_name: OpenGates
surface_label: gate
public_path: /investor
max_clarification_rounds: 2
principal_email: founder@example.com
```

Supported UI fields include:
- `assistant_avatar`
- `assistant_status`
- `welcome_headline`
- `welcome_body`
- `composer_placeholder`
- `invited_topics`

Create a new gate from the starter bundle:

```bash
opengates init-gate --from demo-investor --to my-gate
```

## Providers

OpenGates currently supports two decision paths:

- `heuristic`: no API key required, good for obvious spam and explicit rules
- `openai`: uses the OpenAI Responses API for more ambiguous cases

Use the OpenAI provider by creating a `.env` file in your working directory:

```bash
OPENGATES_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENGATES_OPENAI_MODEL=gpt-5-mini
OPENGATES_DEBUG_PROMPTS=1
```

Notes:
- `.env` and `.env.local` are read from the current working directory
- if `OPENGATES_CONFIG_DIR` is set, config is read from there instead
- if the OpenAI call fails, the runtime falls back to heuristics

## Escalation Email

OpenGates can send an escalation email when:
- `principal_email` is set in `gate.yaml`
- SMTP settings are configured

```bash
OPENGATES_SMTP_HOST=smtp.example.com
OPENGATES_SMTP_PORT=587
OPENGATES_SMTP_USERNAME=...
OPENGATES_SMTP_PASSWORD=...
OPENGATES_SMTP_USE_TLS=1
OPENGATES_SMTP_USE_SSL=0
OPENGATES_NOTIFICATION_FROM_EMAIL=gatekeeper@example.com
OPENGATES_NOTIFICATION_FROM_NAME=OpenGates
```

## CLI

```bash
opengates serve
opengates list-gates
opengates init-gate --from demo-investor --to my-gate
```

## Project Layout

```text
gates/
  demo-investor/
src/opengates/
  app.py
  runtime.py
  gates.py
  storage.py
  schemas.py
  providers/
  starter_gates/
  templates/
tests/
```

## Development

Run tests:

```bash
uv run python -m pytest
```

Build the package:

```bash
uv build
```

## License

OpenGates is source-available under Elastic License 2.0.

That means:
- internal use is allowed, including inside commercial companies
- modification is allowed
- redistribution is allowed subject to the license terms
- offering OpenGates itself as a hosted or managed service is not allowed
