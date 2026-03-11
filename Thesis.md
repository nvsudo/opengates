# Ante / OpenGates Thesis

## Document Contract
- Status: Draft v0.4
- Upstream: None
- Downstream: [Document Tree](docs/README.md), [MVP Plan](docs/mvp-plan.md), [PRD](docs/prd.md), [Brand Guidelines](brand-guidelines.md)
- Change impact: Changes here can invalidate every downstream product and technical document.
- Naming: **Ante** is the commercial product brand. **OpenGates** is the open-source runtime. This document uses "OpenGates" for the runtime and "Ante" for the commercial product. A single filter unit is called a **line** in the commercial product.

## Problem
People with asymmetric attention are increasingly shielded by proxy gatekeepers, not because they are closed, but because their time is scarce and easy to waste. That problem becomes more urgent as agents generate more polished inbound across email, forms, messaging, and social channels. Good signal gets buried with spam, generic asks, and agent-generated noise.

Traditional executive assistants solved this with judgment, context, tone, and bounded back-and-forth. They did not just filter one message. They asked the next sensible question, then the next one, and only surfaced something once it was worth attention.

Most software does not replicate that. It either acts like a dumb filter, a generic AI autoresponder, or a risky mailbox integration that requires inbox read access.

Critically, smarter inboxes alone will not solve this. Every email client will ship AI triage — Claude with Gmail MCP, Superhuman with built-in filtering, Google with priority sorting. The filtering capability is commoditizing. What does not exist is a price mechanism for attention itself.

## Thesis
OpenGates should be an agent-native, local-first runtime that helps a person or team protect attention without becoming rude or inaccessible.

Each line represents a specific surface for inbound, such as investor outreach, vendor pitches, partnership requests, or general contact. The user should be able to chat with their preferred LLM, generate a small line bundle, and then let OpenGates execute that line reliably.

The default commercial product (Ante) should be a hosted, thread-first conversation with payment as a core primitive:
- inbound starts on a public line page or webhook
- the line owns the conversation thread
- the line can ask bounded follow-up questions before escalating
- the line does not require inbox read access by default
- payment is configurable per line: amount, timing (before or after AI qualification), and destination

The boundary should stay clean:
- **OpenGates** owns AI judgment, bounded thread control, principal-facing escalation summaries, and escalation email delivery
- **Ante** owns payment collection, payout routing, hosted dashboards, and the commercial line surface

## Why Payment Is the Core Differentiator

Without payment, Ante is a nicer front-end for AI triage that any LLM connected to an inbox can replicate. The AI conversation, the criteria matching, the tone enforcement — all of that is capability, not moat. It will be commoditized.

With payment, Ante is a new primitive: sender-funded attention access. This does not exist in email. LinkedIn InMail is the closest, and that money goes to LinkedIn, not to the principal. No one has put a toll in front of attention itself.

London's congestion charge proved the mechanism works for traffic. Polymarket proved it works for information. Ante brings it to inbound communication.

Payment serves multiple functions depending on configuration:
- **Token cost offset** ($5): covers the cost of AI processing
- **Noise floor** ($50): eliminates unserious senders
- **Conviction signal** ($5K-$25K): proves the sender believes in what they're pitching
- **Sales access fee** ($2K-$5K): sellers pay to reach enterprise buyers
- **Future routing extensions**: charity, org-pool, and split-routing paths are post-MVP

These are all the same mechanic with different configuration. The plumbing is simple (Stripe Connect). The power is in the economics.

## Product Principles
- Local-first by default: user context, preferences, and history should work on the user's machine first.
- Agent-native: line behavior should be authored in simple files that good models can read and improve over time.
- Minimal authoring surface: the user should define only what matters, not maintain a giant configuration system.
- Structured execution: the runtime should enforce schemas, guardrails, routing, turn limits, and logs outside the model.
- Thread-first by default: the line should own a bounded conversation thread instead of forcing mailbox integrations.
- No inbox read access by default: the product should be usable without Gmail or Outlook read permissions.
- Anti-gaming by design: follow-up questions and replies should not reveal the true criteria.
- Warmth without access inflation: the system should preserve tone while still protecting time.
- Payment-native: every line can have a price. Payment timing (before or after qualification) is configurable. Payment is not a paywall — it's a signal.
- Better models, better outcomes: the system architecture should improve as models improve, without changing core infrastructure.
- Everything is config: payment amount, payment timing, payment routing, number of lines, clarification depth, tone — all configurable per line. Templates get you started.

## Core Insight
The product is not "AI replies." The product is not even "AI triage." The product is **priced attention access with AI judgment**.

That means the step function is the combination of:
- a price mechanism that filters noise at source
- a compact line definition
- a reliable threaded decision loop
- anti-gaming controls
- bounded clarification depth
- payment handling and routing in the commercial layer

The durable moat is not any of these individually. It is the network effects that emerge from usage (see Moat Thesis below).

## Moat Thesis

Payment + AI triage is the step function, not the moat. Someone will clone the mechanic. The moat builds over time through:

### Phase 1: Sender reputation (network effect)
As multiple principals use Ante, the same senders appear across lines. A founder who pitched 10 lines and got escalated 8 times has a reputation score. A vendor who got declined everywhere is flagged. This is cross-principal intelligence that no individual principal has, and no email client can build. The more principals on Ante, the better every principal's judgment gets.

### Phase 2: Intent marketplace (with principal consent)
Every sender who comes through a line is declaring explicit, high-quality intent with money behind it. "I want to sell agent orchestration tools to enterprise CIOs." "I want to pitch a Series A to a16z." Every principal is also declaring what they want. With the principal's opt-in permission, Ante can match — not just filter. The CIO who set up a line looking for agent orchestration audit platforms can be told "three vendors match what you described, and they've already been qualified."

V1 is a tool. V2 adds sender reputation. V3 is a marketplace. Every V1 user generates the data that makes V3 possible.

**The intent marketplace thesis belongs in the investor pitch deck, not in launch messaging.**

## Primary User
Ante is for anyone whose inbound is worth more than their time to read it. The product is not persona-specific — it's infrastructure for attention economics, like Linktree is infrastructure for link management.

Templates make the product concrete for specific use cases. The four launch templates are:

1. **Investor inbound** — VCs, angels, fund managers filtering deal flow
2. **Sales / vendor to buyers** — enterprise buyers filtering seller outreach
3. **Partnership / collab** — creators, companies filtering brand and integration requests
4. **General contact** — public figures, executives, anyone with high inbound volume

The initial curated launch targets 10-20 high-value principals across these categories.

## Product Shape
The first version is a judgment runtime plus a hosted commercial layer. OpenGates evaluates inbound against a line policy and chooses one of three actions on each turn:
- decline
- clarify
- escalate

The line should be easy to create by chatting with an LLM and producing a small set of files:
- `focus.md`
- `standards.md`
- `voice.md`
- `examples.md`
- optional `gate.yaml` for runtime settings in OpenGates
- optional `line.yaml` for commercial settings in Ante, including payment config

Every thread should be bounded. The default recommendation is `3` clarification rounds, but the line owner can configure that depth.

Payment is configurable per line in Ante:
- Amount: $0 (free) to any amount
- Timing: before conversation starts, or after AI qualifies the sender
- Destination (MVP): principal's Stripe account via Connect Express
- Destination (post-MVP): charity, org pool, or split routing

OpenGates should also produce a principal-facing summary for escalations and be able to send the initial escalation email when configured. Everything else should be runtime-managed.

## Distribution And Business Thesis
Open source is useful because trust, inspectability, and portability matter. Users should be able to self-host, run locally, and inspect the line logic. Open source also helps define a recognizable line bundle format that other tools can adopt.

The commercial path (Ante) is convenience, not lock-in:
- hosted line pages and thread UX
- Stripe Connect payment handling
- premium connectors
- analytics and audit UX
- managed setup for non-technical users
- teams, delegation, and workflow controls

The principal controls the economics of their lines. Payment is a first-class primitive, not an add-on. This is the Linktree model: the product is a configurable surface. Payment, criteria, tone, follow-up depth — all config that can be stitched together for what's right for you.

## Launch Strategy

### Curated first wave
Launch with 10-20 hand-picked principals. High-value attention problems where the ante amount and AI quality matter most. This buys time to:
- Get judgment and tone right before scaling
- Learn what the moat actually is from real usage
- Build sender reputation data from real interactions
- Avoid broadcasting a roadmap for competitors

The homepage is polished but the launch is quiet. Request early access + invite codes. Not a Product Hunt launch.

### Why not self-serve at launch
Self-serve risks a principal creating a line that embarrasses them — wrong tone, leaked criteria, bad decline. Trust is destroyed. Curated launch solves this. Self-serve opens when templates and guardrails are proven.

## What Must Be True For This To Work
- the user can create a working line in minutes, not days
- the system does not embarrass the user with bad tone
- the system does not reveal how to game the line
- the system can hold a short thread before surfacing something
- the system can generate a clean principal-facing summary with a credible explanation of why the thread matters
- escalation email works reliably when configured
- payment works reliably and the UX is clean
- the system logs enough context to build trust
- the runtime remains stable as model quality changes
- the default product does not require inbox read permissions

## Non-Goals For The First Version
- replacing email clients
- requiring inbox read access
- building a full CRM
- supporting every channel at launch
- payment routing beyond simple principal payout
- allowing indefinite open-ended conversations
- making the user author large prompt libraries
- self-serve signup (curated launch first)
- the intent marketplace (V3 aspiration, not MVP)

## Decisions Carried Downstream
- The user-authored line bundle is intentionally small.
- Markdown is the main authoring format; structured config is thin and operational.
- Runtime behavior is centered on `decline`, `clarify`, and `escalate` per turn.
- The default product is a hosted thread-first web conversation.
- Payment is a core primitive in Ante, configurable per line (amount, timing, destination).
- OpenGates does not own payment state; it owns judgment, summaries, and escalation notifications.
- Inbox read access is optional and explicitly non-default.
- Clarification depth is configurable per line and recommended at `3`.
- Launch is curated (10-20 principals), not self-serve.
- "Line" is the commercial term for a single filter unit. "Gate" is deprecated in commercial contexts.
- The homepage is the commercial product page. Developer docs are separate.

## Next Documents
- [Document Tree](docs/README.md)
- [MVP Plan](docs/mvp-plan.md)
- [PRD](docs/prd.md)
- [Investor Pitch Deck](docs/pitch-deck.md) — includes moat thesis and intent marketplace vision
