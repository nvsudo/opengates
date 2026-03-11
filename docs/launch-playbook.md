# Launch Playbook

## Document Contract
- Status: Draft v0.2
- Upstream: [Thesis](../Thesis.md), [PRD](prd.md), [OSS Implementation Review](implementation-review.md)
- Downstream: None
- Change impact: This document is a go-to-market and launch checklist derived from the product docs. It should not redefine product behavior.

## Goal
Launch Ante to a small curated set of principals, validate that priced attention access works in the real world, and avoid overbuilding beyond the MVP.

## Positioning To Hold Constant
- Ante is the commercial product. OpenGates is the open-source runtime.
- The product is a hosted, thread-first line experience, not an inbox AI.
- Payment is a core product primitive, not an optional add-on.
- MVP payment routes directly to the principal through Stripe Connect Express.
- Charity, org-pool, and split routing are post-MVP.
- The default product does not require Gmail or Outlook read access.

## Launch Model
- Quiet curated rollout to 10 to 20 hand-picked principals.
- Primary CTA: request early access.
- Secondary CTA: invite code.
- No self-serve launch.
- No Product Hunt launch.

## What Must Be True Before Launch
- The V4 homepage is the canonical marketing page.
- The line page and thread page feel premium and coherent with the V4 brand.
- Stripe Connect onboarding works end to end.
- A sender can pay, converse, and reach a final thread outcome without manual intervention.
- Escalated threads produce a useful principal-facing summary.
- Principals receive escalation email notifications.
- The principal can review escalated threads in a simple dashboard or queue.
- Waitlist capture and invite code flows work.

## Early Principal Profiles
- investors filtering pitch inbound
- enterprise buyers filtering vendor outreach
- partnerships leads filtering brand and integration asks
- high-inbound executives or public figures needing a general contact line

## Metrics To Track
- threads started
- paid threads started
- clarification rate
- escalation rate
- decline rate
- paid-to-escalated conversion
- sender drop-off after first clarification
- false positive escalations
- false negative declines

## Trust Checklist
- no inbox-read permission requested by default
- no hidden message sent on behalf of the principal
- every decision logged
- private reasoning never appears in the public thread
- hidden criteria do not leak in clarification replies
- payment never guarantees escalation

## Do Not Ship In MVP
- charity routing
- org-pool routing
- split payments
- auctions or priority lanes
- self-serve signup
- CRM integrations
- broad analytics
- intent marketplace features
