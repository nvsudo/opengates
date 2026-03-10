# Schemas Spec

## Document Contract
- Status: Draft v0.2
- Upstream: [PRD](../prd.md), [Thread Model Spec](thread-model.md), [Decision Runtime Spec](decision-runtime.md)
- Downstream: [OSS Implementation Review](../implementation-review.md)
- Change impact: Changes here affect storage, validation, and connector contracts. Update the PRD first if the schema change alters product behavior.

## Purpose
Define the minimum internal schemas needed for the MVP.

## Submission
```json
{
  "submission_id": "sub_123",
  "gate_id": "investor",
  "thread_id": "thr_123",
  "source": "web_thread",
  "sender": {
    "name": "Jane Founder",
    "email": ""
  },
  "content": "Short pitch or request text",
  "metadata": {
    "payment_status": "none",
    "submitted_at": "2026-03-10T08:00:00Z"
  }
}
```

## Thread
```json
{
  "thread_id": "thr_123",
  "gate_id": "investor",
  "source": "web_thread",
  "sender_key": "session_abc",
  "status": "waiting_on_sender",
  "turn_count": 1,
  "max_clarification_rounds": 3,
  "remaining_clarification_rounds": 2,
  "created_at": "2026-03-10T08:00:00Z",
  "updated_at": "2026-03-10T08:00:03Z"
}
```

## Thread Message
```json
{
  "message_id": "msg_123",
  "thread_id": "thr_123",
  "role": "sender",
  "channel": "web",
  "content": "We are building AI tooling for finance teams.",
  "created_at": "2026-03-10T08:00:00Z"
}
```

## Decision
```json
{
  "decision_id": "dec_123",
  "thread_id": "thr_123",
  "message_id": "msg_123",
  "gate_id": "investor",
  "decision": "clarify",
  "confidence": 0.81,
  "tags": ["founder", "b2b"],
  "private_reason": "Potential fit but lacks traction details",
  "user_visible_reply": "Thanks for reaching out. Could you share current traction and the specific ask?",
  "needs_review": false,
  "remaining_clarification_rounds": 2
}
```

## Interaction Event
```json
{
  "event_id": "evt_123",
  "thread_id": "thr_123",
  "type": "decision_logged",
  "timestamp": "2026-03-10T08:00:03Z",
  "payload": {}
}
```

## Sender Profile
```json
{
  "sender_key": "session_abc",
  "first_seen_at": "2026-03-10T08:00:00Z",
  "last_seen_at": "2026-03-10T08:00:03Z",
  "interaction_count": 1,
  "notes": []
}
```

## Schema Rules
- `submission_id`, `gate_id`, and `thread_id` are required where they apply.
- `decision` must be one of `decline`, `clarify`, or `escalate`.
- `user_visible_reply` is required for `decline` and `clarify`.
- `confidence` is required for all decisions.
- `remaining_clarification_rounds` must never be negative.
- `private_reason` is never sent to end users.

## Storage Guidance
- store thread records separately from thread messages
- store raw submissions separately from decisions
- store sender profiles by stable sender key
- prefer append-only event logs for auditability

## Non-Goals
- analytics warehouse schema
- billing schema
- team workflow schema
