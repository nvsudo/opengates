# Launch Playbook

## Document Contract
- Status: Draft v0.1
- Upstream: [Thesis](../Thesis.md), [PRD](prd.md), [OSS Implementation Review](implementation-review.md)
- Downstream: None
- Change impact: This document is a go-to-market and launch checklist derived from the product docs. It should not redefine product behavior.

## Goal
Get OpenGates in front of busy, high-inbound people fast enough to learn, without overspending on polish, security scope, or broad integrations.

## Positioning To Hold Constant
- OpenGates is a thread-first gate, not an inbox AI.
- The default product does not require Gmail or Outlook read access.
- The gate can ask bounded follow-up questions before escalating.
- The value is protecting attention while preserving tone.

## What Must Be True Before Public OSS
- The repo runs from a clean machine with the README only.
- No secrets are present in tracked files or commit history.
- The demo gate works end-to-end in heuristic mode without any API key.
- The OpenAI path works when a valid key is supplied through env only.
- The thread API works for external frontends, not just the built-in UI.
- The docs match the actual product behavior.

## What Must Be True Before Showing Busy Folks
- The default gate experience feels respectful and competent.
- Clarification questions do not feel like a low-rent chatbot interview.
- The thread stops after a bounded number of turns.
- The gate can explain a bad decision in logs.
- The product can be used without corporate IT approving inbox access.
- The public story is simple enough to explain in 30 seconds.

## Launch Sequence
### 1. Clean The OSS Surface
- add a top-level project README later if this repo becomes public
- add a license before public OSS
- add one copy-paste `.env` setup path
- keep one obvious demo route
- keep one obvious API example for external forms or chats

### 2. Pick One Story
Use one sentence everywhere:

`A hosted gate that asks the next smart question before your inbox ever gets involved.`

### 3. Recruit Design Partners
Start with 5 to 10 people who:
- get real inbound
- already use LLMs
- hate inbox software friction
- can show you borderline cases

Best early profiles:
- investors
- founders with lots of inbound
- executive operators
- creators with partnership noise

### 4. Force Real Usage
Do not ask for opinions on the idea. Ask each design partner to:
- create one gate
- publish one gate link
- route real inbound through it for one week
- send you at least 5 threads that felt wrong or surprising

### 5. Measure The Right Things
Track:
- threads started
- clarification rate
- escalation rate
- decline rate
- thread completion rate
- drop-off after first clarification
- false positive escalations
- false negative declines
- average turns per thread

### 6. Launch OSS And Product Separately
OSS launch goal:
- developers and operators understand the architecture
- external frontends can hook into the thread APIs

Product launch goal:
- busy people understand the benefit in one sentence
- they do not think they need to grant inbox access

## OSS Checklist
- [ ] README matches the current thread-first architecture
- [ ] reference UI and API examples are both documented
- [ ] sample gate files are short and instructive
- [ ] tests cover multi-turn clarification flow
- [ ] tests cover clarification limit enforcement
- [ ] `.gitignore` excludes local data and env files
- [ ] license is added
- [ ] issue templates are added once public
- [ ] one "good first issue" path exists after launch

## Product Checklist
- [ ] public gate page feels premium enough for serious users
- [ ] first question is easy to answer
- [ ] clarification UI looks like a conversation, not a support ticket
- [ ] sender does not need email to start
- [ ] sender can optionally add email for handoff or later continuation
- [ ] escalation output is useful to the principal
- [ ] payment, if enabled, is clearly framed as priority or seriousness, not access

## Trust Checklist
- [ ] no inbox-read permission is requested by default
- [ ] no hidden message is sent on behalf of the user
- [ ] every decision is logged
- [ ] private reasoning never appears in the public thread
- [ ] hidden criteria do not leak in clarification questions
- [ ] model failure falls back safely

## Cheap Domain Strategy
Do not optimize for the perfect forever name right now. Optimize for:
- easy to say
- easy to spell
- cheap enough to discard
- credible enough for serious people

Use this rule:
- choose `.run` if you want cheap and product-fit
- choose `.page` if you want slightly more polished and literal
- avoid `.xyz` unless price matters more than perceived seriousness

## Recommended Naming Direction
Avoid `OpenGates` as the public product name for now. It is already in active use elsewhere and is likely to create confusion.

Recommended shortlist:
### 1. GateBrief
Why:
- sounds operator-grade
- fits the "protect attention, surface the brief" story
- does not lock you into email

Current domain snapshot checked on March 10, 2026:
- `gatebrief.run` appears available
- `gatebrief.page` appears available

### 2. AskRelay
Why:
- fits the thread engine idea
- implies back-and-forth without saying chatbot
- good if you want to emphasize the API and integration angle

Current domain snapshot checked on March 10, 2026:
- `askrelay.run` appears available
- `askrelay.page` appears available

### 3. QuietGate
Why:
- strongest semantic tie to the current thesis
- easy to explain
- slightly more consumer-feeling than GateBrief

Current domain snapshot checked on March 10, 2026:
- `quietgate.run` appears available
- `quietgate.page` appears available

## Cheapest Reasonable Buy Right Now
If you want to buy something today and move on, buy:
- `gatebrief.run`

Why this one:
- cheap enough to treat as disposable
- stronger than `.xyz` for this audience
- not tied to inbox access
- broad enough to survive product iteration

## Registrar Pricing Snapshot
Checked on March 10, 2026. Prices change often, so recheck before purchase.

Using Porkbun pricing pages:
- `.run`: about `$4.12` first year sale, `$22.14` renewal
- `.page`: about `$10.81` registration and renewal
- `.xyz`: about `$2.04` first year sale, `$12.98` renewal

## First 2 Weeks After Domain Purchase
- point the domain to one clean landing page
- keep only one CTA: create or try a gate
- include one short demo GIF or video
- include one sentence on no inbox-read permissions
- include one sentence on bounded follow-up questions
- include one sample use case for investors or founders

## First Public Launch Checklist
- [ ] domain is live
- [ ] landing page is live
- [ ] demo route works
- [ ] one public OSS repo or public branch is ready
- [ ] README is polished
- [ ] one launch post is written
- [ ] 20 direct outreach targets are prepared
- [ ] 5 design partner invites are ready

## What Not To Do Yet
- do not launch as a generic AI assistant
- do not lead with inbox integrations
- do not support too many channels
- do not add pricing complexity too early
- do not ask strangers for deep setup before they see value

## Current Recommendation
- Keep the internal repo and architecture name as `OpenGates` for now.
- Use `GateBrief` as the most practical public-facing test name.
- Buy `gatebrief.run` now if you want a cheap forward move.
- Revisit permanent naming only after real design-partner usage.
