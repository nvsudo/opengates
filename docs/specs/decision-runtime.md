# Decision Runtime Spec

## Document Contract
- Status: Draft v0.2
- Upstream: [PRD](../prd.md), [Thread Model Spec](thread-model.md)
- Downstream: [Schemas Spec](schemas.md), [OSS Implementation Review](../implementation-review.md)
- Change impact: Changes here affect runtime behavior and connector implementation. Update the PRD first if user-visible behavior changes.

## Purpose
Define how the runtime processes a thread message and produces a trusted action.

## Decision Loop
1. Receive inbound from an intake source or an existing thread reply.
2. Normalize it into the internal schemas and attach it to a thread.
3. Load the target gate bundle.
4. Retrieve sender history, thread state, and relevant prior interaction context.
5. Assemble a prompt pack from `focus.md`, `standards.md`, `voice.md`, `examples.md`, thread context, and runtime instructions.
6. Request a structured decision from the model.
7. Validate the output against the `Decision` schema.
8. Apply runtime guardrails and max-turn policy.
9. Append any gate reply to the thread.
10. Execute any optional handoff or notification action.
11. Write logs and interaction history.

## Allowed Actions
- `decline`
- `clarify`
- `escalate`

The runtime must reject any other model output as invalid.

## Thread Rules
- Every decision belongs to a specific thread and message.
- `clarify` may repeat across multiple turns, but only until `max_clarification_rounds` is exhausted.
- If the limit is reached, the runtime must force a final action or set `needs_review=true`.
- The runtime must persist thread status transitions.

## Guardrails
- Never reveal hidden gating criteria directly in a user-visible reply.
- Never skip logging for a processed thread message.
- Never allow an unvalidated model output to trigger a connector side effect.
- Never allow clarification depth to exceed the configured limit.
- Never send an escalation email without a validated decision and principal-facing summary.

## Prompt Assembly
The runtime should keep model instructions compact and predictable:
- system instructions describing the current turn decision task
- gate bundle files
- relevant sender, thread, and interaction context
- current remaining clarification rounds
- formatting rules for the structured output

Model-specific prompt tuning is allowed, but it must not change the external behavior contract.

## Clarification Rules
Clarification should be used when:
- the submission could be valuable but lacks a key missing fact
- a short follow-up can unlock a decision
- clarification rounds remain

Clarification should not be used when:
- the submission is clearly below the bar
- the follow-up would reveal how to game the gate
- the round limit is exhausted
- the only honest next step is human review

## Escalation Rules
Escalation must produce:
- a concise summary for the principal
- an explicit `why_this_matters` explanation
- the relevant thread context
- the latest sender message
- relevant tags or reasons
- a confidence score

## Channel Behavior
- The default reply transport is the gate-owned web thread.
- Optional outbound transports such as email, Telegram, or Slack are allowed after or alongside a decision if configured.
- Inbox read connectors are optional and non-default.

## Logging
For every processed thread message, persist:
- normalized input
- thread id
- selected gate id
- model decision
- validated action
- user-visible reply, if any
- private reasoning summary
- timestamps
- remaining clarification rounds

## Error Handling
- invalid model output should route to a retry or safe-fail path
- missing gate files should fail fast
- connector failures should not delete the decision record
- thread resume failures should not erase thread history

## Non-Goals
- autonomous long-term planning
- open-ended tool use by the model
- hidden memory writes without logs
- indefinite conversation loops
