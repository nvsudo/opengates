# Thread Model Spec

## Document Contract
- Status: Draft v0.1
- Upstream: [PRD](../prd.md)
- Downstream: [Decision Runtime Spec](decision-runtime.md), [Schemas Spec](schemas.md), [OSS Implementation Review](../implementation-review.md)
- Change impact: Changes here affect thread storage, UI flow, resume behavior, and runtime control flow. Update the PRD first if user-visible behavior changes.

## Purpose
Define how OpenGates owns a bounded conversation thread before a final outcome is reached.

## Core Model
A thread is the system of record for one inbound conversation tied to one gate.

Each thread contains:
- gate identity
- sender identity or session identity
- ordered messages
- thread state
- clarification depth state
- final outcome, if reached
- principal-facing escalation summary, if reached

## Default Channel Model
- The default ingress is a public gate page or web endpoint.
- The default return path is the same gate-owned web thread.
- Email, Slack, Telegram, and other transports are optional adapters.
- Inbox read access is not required for the default product.
- The built-in web thread is a reference client for the engine, not the only allowed frontend.
- External forms, chats, or custom UIs should be able to drive the same thread model over API.

## Thread States
- `open`
- `waiting_on_sender`
- `evaluating`
- `escalated`
- `declined`
- `expired`
- `review`

## Turn Depth
- Each gate may configure `max_clarification_rounds`.
- The recommended default is `3`.
- Clarification rounds count only when the gate asks the sender for more information.
- Once the round limit is exhausted, the runtime must:
  - choose a final action, or
  - mark the thread for human review

## Clarification Behavior
- The gate may ask follow-up questions when additional context is plausibly worth obtaining.
- Each clarification turn should ask the minimum number of targeted questions needed, ideally one and at most two.
- Clarification should not continue if the sender is clearly below the bar or if the next question would expose hidden criteria.

## Identity And Resume
- A thread may begin without requiring sender email.
- The runtime may support session-based continuation, magic-link resumption, or optional email-based resumption.
- Email should be optional for resume and handoff, not required for basic use.

## Commercial Boundary
- OpenGates thread state does not carry payment state.
- Ante may attach payment state around the thread, but the runtime should only receive the message and gate context it needs to judge.
- Payment must not guarantee escalation or access.

## Handoff
- Escalated threads may trigger optional outbound actions such as:
  - notifying the principal
  - sending an escalation email with a concise summary and `why_this_matters`
  - creating an intro email
  - posting to a review queue
- These outbound transports are separate from the default thread experience.

## Non-Goals
- inbox read access by default
- indefinite conversation depth
- full messaging platform parity at launch
