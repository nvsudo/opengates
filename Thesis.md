# OpenGates Thesis

## Document Contract
- Status: Draft v0.2
- Upstream: None
- Downstream: [Document Tree](docs/README.md), [MVP Plan](docs/mvp-plan.md), [PRD](docs/prd.md)
- Change impact: Changes here can invalidate every downstream product and technical document.

## Problem
People with asymmetric attention are increasingly shielded by proxy gatekeepers, not because they are closed, but because their time is scarce and easy to waste. That problem becomes more urgent as agents generate more polished inbound across email, forms, messaging, and social channels. Good signal gets buried with spam, generic asks, and agent-generated noise.

Traditional executive assistants solved this with judgment, context, tone, and bounded back-and-forth. They did not just filter one message. They asked the next sensible question, then the next one, and only surfaced something once it was worth attention.

Most software does not replicate that. It either acts like a dumb filter, a generic AI autoresponder, or a risky mailbox integration that requires inbox read access.

## Thesis
OpenGates should be an agent-native, local-first gate runtime that helps a person or team protect attention without becoming rude or inaccessible.

Each gate represents a specific surface for inbound, such as investor outreach, partnership requests, podcast requests, or founder intros. The user should be able to chat with their preferred LLM, generate a small gate bundle, and then let OpenGates execute that gate reliably.

The default product should be a hosted, thread-first gate conversation:
- inbound starts on a public gate page or webhook
- the gate owns the conversation thread
- the gate can ask bounded follow-up questions before escalating
- the gate does not require inbox read access by default

The system should:
- accept inbound content from a public gate page, form, or webhook
- evaluate it against a private policy for that gate
- respond in the user's tone
- ask neutral 2nd-order and 3rd-order questions when more information is needed
- continue the thread until it reaches a final outcome
- surface only the best items to the principal
- avoid leaking the real criteria that determine access

## Product Principles
- Local-first by default: user context, preferences, and history should work on the user's machine first.
- Agent-native: gate behavior should be authored in simple files that good models can read and improve over time.
- Minimal authoring surface: the user should define only what matters, not maintain a giant configuration system.
- Structured execution: the runtime should enforce schemas, guardrails, routing, turn limits, and logs outside the model.
- Thread-first by default: the gate should own a bounded conversation thread instead of forcing mailbox integrations.
- No inbox read access by default: the product should be usable without Gmail or Outlook read permissions.
- Anti-gaming by design: follow-up questions and replies should not reveal the true gating criteria.
- Warmth without access inflation: the system should preserve tone while still protecting time.
- Better models, better outcomes: the system architecture should improve as models improve, without changing core infrastructure.

## Core Insight
The product is not "AI replies." The product is trusted judgment at the point of inbound.

That means the durable value is not a prompt. It is the combination of:
- a compact gate definition
- a reliable threaded decision loop
- memory and sender context
- auditability
- channel integrations
- anti-gaming controls
- bounded clarification depth

## Primary User
OpenGates is initially for people with large amounts of inbound and high opportunity cost:
- investors
- founders
- operators
- executives
- creators with high-quality but noisy inbound

These users already use LLMs. They do not need another full software platform to author their preferences. They need a system that converts their intent into a gate they can trust.

## Product Shape
The first version should not be a broad inbox AI. It should be a narrow gate runtime with one job: evaluate inbound against a gate policy and choose one of three actions on each turn:
- decline
- clarify
- escalate

The gate should be easy to create by chatting with an LLM and producing a small set of files:
- `focus.md`
- `standards.md`
- `voice.md`
- `examples.md`
- optional `gate.yaml` for operational settings

Every thread should be bounded. The default recommendation is `3` clarification rounds, but the gate owner can configure that depth. More depth means more diligence and more token cost, which the gate owner may choose to absorb or offset with an optional charge.

Everything else should be runtime-managed.

## Distribution And Business Thesis
Open source is useful here because trust, inspectability, and portability matter. Users should be able to self-host, run locally, and inspect the gate logic. Open source also helps define a recognizable gate bundle format that other tools can adopt.

The commercial path is convenience, not lock-in:
- hosted gate pages and thread UX
- premium connectors
- analytics and audit UX
- managed setup for non-technical users
- teams, delegation, and workflow controls
- optional outbound email or intro flows

An optional payment or paywall integration can act as a seriousness filter and token-cost offset, but it should never become the core value proposition. Payment is a signal, not a pass. Charging may also be used to fund deeper multi-turn diligence, but the gate should never equate payment with quality.

## What Must Be True For This To Work
- the user can create a working gate in minutes, not days
- the system does not embarrass the user with bad tone
- the system does not reveal how to game the gate
- the system can hold a short thread before surfacing something
- the system logs enough context to build trust
- the runtime remains stable as model quality changes
- the default product does not require inbox read permissions

## Non-Goals For The First Version
- replacing email clients
- requiring inbox read access
- building a full CRM
- supporting every channel at launch
- turning payment into required access
- allowing indefinite open-ended conversations
- making the user author large prompt libraries

## Decisions Carried Downstream
- The user-authored gate bundle is intentionally small.
- Markdown is the main authoring format; structured config is thin and operational.
- Runtime behavior is centered on `decline`, `clarify`, and `escalate` per turn.
- The default product is a hosted thread-first web conversation.
- Inbox read access is optional and explicitly non-default.
- Clarification depth is configurable per gate and recommended at `3`.
- Payment is an optional seriousness filter or cost offset, not the core product.

## Next Documents
- [Document Tree](docs/README.md)
- [MVP Plan](docs/mvp-plan.md)
- [PRD](docs/prd.md)
