# MVP Plan

## Document Contract
- Status: Draft v0.2
- Upstream: [Thesis](../Thesis.md)
- Downstream: [PRD](prd.md)
- Change impact: Changes here may require PRD and spec updates. Thesis changes only if the product direction changes.

## MVP Goal
Prove that a user can define a gate in a few minutes, run a public thread-first gate conversation, and trust the system to decline, clarify, or escalate without leaking private criteria or requiring inbox read access.

## MVP Success Criteria
- A user creates one working gate bundle in under 15 minutes.
- Real inbound can start through a hosted gate page.
- The runtime can hold a short thread with bounded clarification depth.
- The system can ask useful follow-up questions before escalating.
- The user can inspect logs and understand why a thread was declined, clarified, or escalated.
- The product works without Gmail or Outlook read permissions.

## MVP Scope
Include:
- one hosted gate page
- one threaded web conversation flow
- one local runtime
- one gate bundle format
- one model provider integration
- one escalation or notification path
- audit logging
- optional payment or priority metadata support

Exclude:
- multi-user workspaces
- inbox read integrations
- many connectors
- adaptive autonomous memory writing
- a broad dashboard product

## 7-Day Build Sequence
### Day 1
- create the gate bundle format
- build a public gate page
- build the thread and message model
- support `decline`, `clarify`, and `escalate` per turn

### Day 2
- add runtime guardrails
- add turn limits and thread states
- add audit logs and sender history
- test adversarial and gameable inputs

### Day 3
- add a chat-like web thread UI
- add resumable thread links or session recovery
- generate starter gate files from user answers

### Day 4
- add optional payment metadata or priority lane support
- ensure payment never bypasses quality thresholds
- support configurable clarification depth, with `3` as the recommended default

### Day 5
- run a private beta with a few high-inbound users
- collect real examples of false positives, false negatives, and thread drop-off
- refine examples, follow-up questions, and reply templates

### Day 6
- tighten positioning and onboarding copy
- publish repository docs
- record a short thread-based demo

### Day 7
- launch publicly
- onboard early design partners
- collect requests for connectors, hosting, pricing, and managed setup

## Deliverables
- a runnable local MVP
- a hosted threaded gate page
- a starter gate bundle
- one end-to-end multi-turn demo flow
- private beta feedback notes

## Risks To Watch
- runaway thread depth and token costs
- tone failures in follow-up questions
- follow-up questions that leak criteria
- sender drop-off without a good resume path
- overscoping connectors before proving the thread loop

## Decisions Carried Downstream
- The MVP is one gate, one public web thread, one model provider, one escalation path.
- Inbox read access is not required.
- Clarification depth is configurable in `gate.yaml` and recommended at `3`.
- The payment flow is optional and non-default.
- The runtime must log structured thread decisions from day one.
- The user-authoring experience must be template-driven, not config-heavy.

## Next Documents
- [PRD](prd.md)
