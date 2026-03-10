# OSS Implementation Review

## Document Contract
- Status: Draft v0.1
- Upstream: [PRD](prd.md), [Thread Model Spec](specs/thread-model.md), [Decision Runtime Spec](specs/decision-runtime.md), [Schemas Spec](specs/schemas.md)
- Downstream: None
- Change impact: This document is derived from the product and technical specs. It should not introduce new product behavior by itself.

## Purpose
Identify what must change in the current `oss/` implementation before it matches the updated thread-first architecture.

## Current OSS Assumptions That No Longer Fit
- The runtime is submission-first, not thread-first.
- The UI is a single send-and-result flow, not a persistent conversation.
- `Decision` objects are keyed to submissions, not thread messages.
- `gate.yaml` does not yet express public path, turn depth, or thread behavior.
- The provider prompt sees the latest submission but not a structured thread history.
- The app treats email as an optional sender field, but there is no first-class thread resume model.

## Most Impacted Files In The Current OSS Repo
- `oss/src/opengates/app.py`
- `oss/src/opengates/runtime.py`
- `oss/src/opengates/schemas.py`
- `oss/src/opengates/storage.py`
- `oss/src/opengates/gates.py`
- `oss/src/opengates/providers/base.py`
- `oss/src/opengates/providers/heuristic.py`
- `oss/src/opengates/providers/openai_responses.py`
- `oss/src/opengates/templates/intake.html`
- `oss/src/opengates/templates/result.html`
- `oss/tests/test_runtime.py`

## Required Changes In `oss/`
### Gate Config And Templates
- Extend `GateConfig` to support `public_path`, `max_clarification_rounds`, optional `thread_expiry`, optional outbound notification settings, and optional charging fields.
- Update starter gates to include thread-first defaults.

### Schemas And Storage
- Add first-class `Thread` and `ThreadMessage` models.
- Add thread persistence alongside submissions, decisions, events, and sender profiles.
- Track thread status, turn count, and remaining clarification rounds.
- Add a thread resume mechanism, likely with session tokens or magic links.

### Runtime
- Change the runtime from one-shot processing to thread-aware processing.
- Pass thread history and remaining turns into the provider context.
- Enforce clarification depth and force a final action or review when the limit is reached.
- Separate current-message evaluation from final escalation or handoff execution.

### Web App
- Replace the current result page with a chat-like thread page.
- Introduce routes such as:
  - `GET /g/{gate_id}` for new thread creation
  - `GET /t/{thread_id}` for thread continuation
  - `POST /t/{thread_id}/reply` for sender responses
- Keep `/demo` as a convenience alias, but point it into the thread model.
- Treat the built-in web UI as a reference client and add API routes that third-party forms or chats can use directly.

### Provider Layer
- Expand the provider context to include thread history, thread state, and remaining clarification rounds.
- Ensure prompt-debug logging captures the exact thread context sent to the model.
- Keep heuristics as prefilter and fallback logic.

### Tests
- Add tests for multi-turn clarification flows.
- Add tests for limit enforcement at `max_clarification_rounds`.
- Add tests for resume behavior.
- Add tests confirming the product still works without any mailbox integration.

## Non-Blocking Later Work
- email ingress adapters
- outbound intro email generation
- Slack or Telegram notifications
- pricing and payment processor integration
- managed hosted deployment layers

## Recommendation
Do not patch the current single-turn flow incrementally. Replace the current submission-first web flow with a thread-first model, then reattach existing provider, storage, and gate-loading pieces where they still fit.
