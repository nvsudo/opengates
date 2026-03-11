# Gate Bundle Spec

## Document Contract
- Status: Draft v0.2
- Upstream: [PRD](../prd.md)
- Downstream: None
- Change impact: Changes here affect gate authoring, template generation, and runtime loading. Update the PRD first if product behavior changes.

## Purpose
Define the minimal user-authored files that make up a gate.

## Design Principle
The gate bundle should be small enough for a user to create with their preferred LLM in one session. User-authored files should capture intent, not internal runtime mechanics.

## Required Files
`focus.md`
- Current topics, themes, and categories the user actively cares about
- Time-bounded priorities are allowed
- Should prefer concrete interests over broad mission statements

`standards.md`
- Minimum quality bar before something is escalated
- Hard disqualifiers
- Conditions that justify a clarification request
- Hidden criteria that must not be revealed directly

`voice.md`
- Desired tone for declines, clarifications, and escalations
- Style preferences
- Relationship posture, such as warm, direct, or formal

`examples.md`
- Accepted examples
- Rejected examples
- Ambiguous examples
- Short rationale for each example

## Optional Files
`gate.yaml`
- runtime settings only
- gate id
- public title or assistant/display name
- softer public surface label for the reference UI
- public path or slug
- max clarification rounds
- thread expiry
- principal notification email
- outbound notifications or handoff transports
- threshold tuning

## Recommended Folder Layout
```text
gates/
  investor/
    focus.md
    standards.md
    voice.md
    examples.md
    gate.yaml
```

## Authoring Rules
- Keep each file short enough to review quickly.
- Prefer examples over long abstractions when edge cases matter.
- Do not include secrets in Markdown files if the repo is shared.
- Do not describe hidden criteria in terms that can be reused verbatim in replies.
- Keep operational settings in `gate.yaml`; keep judgment policy in Markdown files.

## Runtime Responsibilities
The runtime may derive or maintain additional state, but that state is not required from the user. Examples:
- sender history
- thread state
- interaction logs
- memory summaries
- model-specific prompt assembly
- resume tokens

## Validation Rules
- A gate bundle is invalid if any required Markdown file is missing.
- `examples.md` must contain at least one accepted and one rejected example.
- `gate.yaml`, if present, may configure operational behavior such as route, turn limit, and notifications.
- `gate.yaml` must not redefine semantic fit criteria owned by Markdown files.
- `max_clarification_rounds`, if present, should default to `3` and stay within a bounded range defined by the runtime.

## Non-Goals
- full policy DSL
- nested template systems
- user-authored memory internals
