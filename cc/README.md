# Ante

Commercial product surface powered by the OpenGates runtime.

This project reuses the OSS runtime as a dependency, but keeps its own:
- public UI and line presentation
- copy, styling, and brand
- commercial product experiments

Docs:
- `docs/product.md`
- `docs/website-copy.md`
- `docs/agent-access.md`

## Run
```bash
cd cc
uv sync --extra dev
uv run opengates-cc serve --host 127.0.0.1 --port 8100
```

Open [http://127.0.0.1:8100/demo](http://127.0.0.1:8100/demo).

## Product Rules
- web intake requires sender email
- the thread lives in the product, not in the user's inbox
- inbox read access is not the default commercial product
- API is the planned system of record for agent access; MCP can wrap it later

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
