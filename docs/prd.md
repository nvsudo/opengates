# Product Requirements Document

## Document Contract
- Status: Draft v0.2
- Upstream: [Thesis](../Thesis.md), [MVP Plan](mvp-plan.md)
- Downstream: [Gate Bundle Spec](specs/gate-bundle.md), [Thread Model Spec](specs/thread-model.md), [Decision Runtime Spec](specs/decision-runtime.md), [Schemas Spec](specs/schemas.md), [OSS Implementation Review](implementation-review.md)
- Change impact: Changes here may require updates across all specs and the implementation review. Thesis and MVP plan changes are only needed if the product intent or launch scope changes.

## Product Summary
OpenGates is a local-first, agent-native runtime that evaluates inbound through a hosted conversation thread and chooses one of three actions on each turn: decline, clarify, or escalate.

The first product experience is a hosted gate page backed by a local runtime. The sender starts a thread with the gate, the gate may ask bounded follow-up questions, and only the best items reach the principal. Inbox read access is explicitly non-default.

The built-in web experience is a reference UI. The product core is the thread engine and decision runtime, which should also be usable from external forms, chats, or custom frontends over API.

## Target User
Primary user:
- someone with high opportunity-cost attention and too much inbound

Initial profiles:
- investor
- founder
- executive
- operator
- creator with high-value inbound

## Core Job To Be Done
When inbound reaches me, help me avoid wasting time while still catching valuable signal, preserving my tone, and gathering enough context before something reaches me.

## User Inputs
The user should only need to define:
- what they care about right now
- what standards must be met before something reaches them
- how they want replies to sound
- a few examples of good, bad, and ambiguous inbound

The user may also configure operational settings in `gate.yaml`:
- public route or path
- max clarification rounds
- optional charging or priority settings
- optional outbound notifications or handoff transports

## Primary User Flow
1. User creates a new gate from a starter template.
2. User edits a small number of Markdown files directly or via an LLM.
3. User publishes a hosted gate page or local endpoint for that gate.
4. A sender starts a thread with the gate.
5. The runtime evaluates the current message against the gate bundle and thread context.
6. The runtime validates the model output and applies hard guardrails.
7. The system declines, asks a clarifying question, or escalates.
8. If clarification is chosen and rounds remain, the thread continues in the same gate-owned conversation.
9. If escalation or handoff is chosen, the system may notify the principal or create an intro using an outbound transport if configured.
10. The user reviews logs and adjusts the gate bundle if needed.

## Functional Requirements
### Gate Authoring
- The system must support a gate bundle made of Markdown-first files.
- The system must provide starter templates for at least one user profile.
- The runtime must be able to load one gate bundle from disk and execute it.
- `gate.yaml` must support operational settings without becoming the main policy surface.

### Intake And Threads
- The system must accept inbound from a hosted gate page.
- The system must normalize inbound into one internal schema.
- The system must create and persist a thread for each conversation.
- The system must support a web-first conversation without requiring inbox read permissions.
- The system may collect sender email for resume or handoff, but it must not depend on mailbox access.
- The system should support webhook ingestion into the same thread model.
- The system should expose thread APIs so external form or chat frontends can create threads, append replies, and fetch thread state.

### Decisioning
- The runtime must output exactly one of `decline`, `clarify`, or `escalate` on each turn.
- The runtime must produce a structured decision object.
- The runtime must support private reasoning and user-visible reply text separately.
- `clarify` may repeat across multiple turns, but only up to `max_clarification_rounds` for that gate.
- When the turn limit is exhausted, the runtime must force a final action or mark the thread for review.

### Channel Behavior
- The default return path must be the gate-owned web thread.
- The system may optionally send outbound email, notifications, or intros after a decision.
- Inbox read access is optional and explicitly non-default.

### Charging
- The system may support optional charging or priority lanes on a per-gate basis.
- Charging may offset token costs or deter unserious inbound.
- Charging must not force escalation by itself.

### Guardrails
- The runtime must support rules that are enforced outside the model.
- The system must prevent follow-up questions from leaking hidden criteria.
- The system must enforce max clarification rounds.
- The system must not require inbox read permission to function.

### Logging And Review
- Every thread message must be logged with the input, decision, and resulting action.
- The user must be able to inspect why a thread was escalated, declined, or kept open.
- The system must persist sender history, thread state, and prior interaction context.

## Non-Functional Requirements
- Local-first storage for gate bundle and logs
- Simple setup for non-technical but LLM-literate users
- Model-provider abstraction so improved models can be swapped in later
- Fast enough response time for a conversational web thread
- Secure enough thread resumption for practical use

## Non-Goals
- inbox replacement
- inbox read access by default
- CRM functionality
- broad analytics suite
- full workflow automation for teams
- automatic memory mutation without review
- indefinite open-ended conversations

## Acceptance Criteria
- A user can create a gate from templates and process real inbound the same day.
- A sender can complete a multi-turn gate conversation without mailbox integration.
- The runtime produces valid structured decisions for all test submissions and thread turns.
- Rejection tone matches the voice instructions closely enough to avoid obvious brand damage.
- Clarification requests remain neutral and non-leaky across adversarial samples.
- Clarification depth is enforced per gate.
- Logs are sufficient to debug a bad decision after the fact.

## Open Questions
- Should resume links be anonymous tokens, email-based, or both?
- What should the default thread expiry be?
- Should the first outbound notification path be email, Telegram, or a plain review queue?

## Spec Links
- [Gate Bundle Spec](specs/gate-bundle.md)
- [Thread Model Spec](specs/thread-model.md)
- [Decision Runtime Spec](specs/decision-runtime.md)
- [Schemas Spec](specs/schemas.md)
- [OSS Implementation Review](implementation-review.md)
