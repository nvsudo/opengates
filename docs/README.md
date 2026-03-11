# Document Tree

## Purpose
This repository uses a simple dependency tree so product decisions can be traced from idea to implementation detail.

Canonical V4 brand and product narrative now live in:
- [README](../README.md)
- [Thesis](../Thesis.md)
- [Brand Guidelines](../brand-guidelines.md)

Legacy design artifacts and the V3→V4 handoff have been moved under `archive/`.

## Tree
- [Thesis](../Thesis.md)
  - source of truth for why this exists and what kind of product it is
- [MVP Plan](mvp-plan.md)
  - the first build and launch plan derived from the thesis
- [PRD](prd.md)
  - the product definition derived from the thesis and MVP plan
- Specs
  - [Gate Bundle Spec](specs/gate-bundle.md)
  - [Thread Model Spec](specs/thread-model.md)
  - [Decision Runtime Spec](specs/decision-runtime.md)
  - [Schemas Spec](specs/schemas.md)
- Derived Review
  - [OSS Implementation Review](implementation-review.md)
- Launch
  - [Launch Playbook](launch-playbook.md)

## Dependency Rules
- If the thesis changes, review every downstream document.
- If the MVP plan changes, review the PRD and any affected specs.
- If the PRD changes, review all linked specs and derived reviews.
- If a spec changes without changing product behavior, upstream documents do not need edits.
- If a spec change implies a product change, update the PRD first.
- Derived reviews should never become the place where product decisions are invented.

## Change Workflow
1. Update the highest-level document where the decision belongs.
2. Propagate that change only to linked downstream documents.
3. Record new assumptions in the nearest document that owns them.
4. Do not solve product ambiguity inside a low-level spec or implementation review.

## Current Scope
This tree is intentionally small. The current product spine is:
- Thesis
- MVP plan
- PRD
- four implementation-facing specs
- one OSS implementation review
- one launch playbook
