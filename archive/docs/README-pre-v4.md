# Ante

Your attention has a front door.

Ante is a product for filtering inbound through conversation. You define what you care about — topics, standards, tone — and Ante handles the rest. Senders make their case. The gate asks follow-ups. Only the signal gets through.

Powered by [OpenGates](oss/), an open-source runtime.

## Repo Structure
```text
├── Thesis.md              # Why this exists
├── brand-guidelines.md    # Brand, voice, naming, visual identity
├── docs/                  # Product docs, specs, plans
├── oss/                   # OpenGates — open-source runtime
└── cc/                    # Ante — commercial product surface
```

## Quick Start

**OSS runtime:**
```bash
cd oss
uv sync
uv run opengates serve
```

**Commercial product:**
```bash
cd cc
uv sync --extra dev
uv run opengates-cc serve --port 8100
```
