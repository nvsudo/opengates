# Ante

Your attention has a price.

Ante is a product for filtering inbound through conversation — with payment as a first-class primitive. You define what you care about, set a price, and Ante handles the rest. Senders ante up, make their case, and only the signal gets through.

Powered by [OpenGates](oss/), the open-source judgment runtime. OpenGates handles thread decisions, principal-facing summaries, and escalation email. Ante handles payment, payout, and the hosted commercial surface.

## How it works

1. **You open a line** — a public address like `pitch@you` or `vendor@company`. You define topics, criteria, voice, and an optional ante amount.
2. **Senders make their case** — they land on your line, pay the ante if there is one, and write their pitch. The AI asks sharp follow-ups. Bounded and direct.
3. **You see only what survives** — declined warmly, clarified efficiently, escalated with a clean summary and the sender's ante attached.

## Repo Structure
```text
├── ante-homepage.html     # Canonical V4 homepage HTML
├── Thesis.md              # Why this exists
├── brand-guidelines.md    # Brand, voice, naming, visual identity
├── docs/                  # Product docs, specs, plans
├── archive/               # Legacy artifacts kept temporarily during cleanup
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

## Terminology

| Concept | Name |
|---|---|
| The brand | **Ante** |
| A single filter | **a line** |
| The sender-facing address | `type@principal` (e.g. `pitch@a16z`) |
| The conversation | **a thread** |
| The payment | **the ante** |
| The OSS package | `opengates` (PyPI legacy) |

## Links

- [Thesis](Thesis.md) — why this exists
- [Brand Guidelines](brand-guidelines.md) — voice, naming, visual identity
- [V3→V4 Handoff](archive/handoffs/v3-to-v4.md) — archived transition record
