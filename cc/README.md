# OpenGates CC

Commercial app surface for OpenGates.

This project reuses the OSS runtime as a dependency, but keeps its own:
- public UI
- gate presentation
- copy and styling
- commercial product experiments

## Run
```bash
cd cc
uv sync --extra dev
uv run opengates-cc serve --host 127.0.0.1 --port 8100
```

Open [http://127.0.0.1:8100/demo](http://127.0.0.1:8100/demo).

## Environment
Copy `.env.example` to `.env` or `.env.local`.

Useful vars:
- `OPENGATES_CC_PROVIDER=heuristic|openai`
- `OPENAI_API_KEY=...`
- `OPENGATES_CC_OPENAI_MODEL=gpt-5-mini`
- `OPENGATES_CC_DEBUG_PROMPTS=1`

## Structure
```text
cc/
  gates/
  src/opengates_cc/
  tests/
```
