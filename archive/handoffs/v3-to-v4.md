# Ante — V3 → V4 Handoff

**Date:** March 11, 2026
**Status:** V4 complete. Ready for implementation.

---

## What this document is

This captures every product, brand, and design decision made in the V3→V4 sprint. It serves as the single source of truth for anyone building, designing, or writing for Ante going forward.

---

## 1. Naming Decisions

### Brand name: Ante (unchanged)
Ante is the brand for the commercial product, the open-source project (in public-facing contexts), and all marketing.

### Unit name: "gate" → "line"
The word "gate" is retired from all commercial contexts. A single filter is now called a **line**.

- "Gate" felt cold, security-flavored, and carried negative "gatekeeper" energy
- "Line" is direct, conversational, and resonates naturally: "open a line," "your pitch line," "drop a line," "hold the line"
- "Line" is internal product vocabulary. Senders never need to learn it — they just see the principal's name and what topics are open (same way X doesn't teach you "handles" and Linktree doesn't teach you "links")

### Terminology table (final)

| Concept | Name | Context |
|---|---|---|
| The brand | **Ante** | Everywhere |
| A single filter | **a line** | Commercial product |
| Sender-facing address | **@-handle** (`pitch@a16z`) | Product + marketing |
| Sender-facing page | *(no special name)* | Senders just see it |
| The conversation | **a thread** | Product |
| The payment | **the ante** | Product + marketing |
| Person behind the line | **the principal** | Internal/docs only |
| Person trying to get through | **the sender** | Internal/docs only |
| OSS Python package | `opengates` | PyPI, imports only |

### Migration checklist
- [ ] All UI copy: gate → line
- [ ] Homepage: done (V4 file delivered)
- [ ] Brand guidelines: done (V4 file delivered)
- [ ] Thesis: done (V4 file delivered)
- [ ] README: done (V4 file delivered)
- [ ] OSS code: `gate` references stay in `opengates` internals for now; public-facing docs use "line"
- [ ] Config files: `gate.yaml` → `line.yaml` in commercial product

---

## 2. Product Decisions

### Core differentiator: Payment
Without payment, Ante is a nicer front-end for AI triage that any LLM + inbox MCP can replicate. With payment, Ante is a new primitive: **sender-funded attention access**. This does not exist in email today.

Payment ships on day one. It is not a feature — it is the product.

### Payment mechanics (MVP)
- **Integration:** Stripe Connect Express
- **Flow:** Principal sets a price per line (including $0). Sender pays via Stripe Checkout. Money goes to principal.
- **Timing:** Configurable per line — before the conversation starts, or after the AI qualifies the sender. Principal chooses.
- **Routing (MVP):** Money goes to principal's connected Stripe account. That's it.
- **Routing (V2+):** Charity routing, org cloud pool routing, split payments. Not in MVP.

### Line templates (4 starters)
1. **Investor inbound** — `pitch@` — deal flow filtering by thesis fit, stage, traction
2. **Sales / vendor to buyers** — `vendor@` — sellers pay to reach enterprise buyers
3. **Partnership / collab** — `collab@` — brand deals, co-marketing, integrations
4. **General contact** — `contact@` — front door for everything else, free or priced

### What ships in MVP
- Public URL / line page per principal
- AI conversation (clarify / decline / escalate)
- Principal dashboard with escalated threads
- Payment per line (configurable amount and timing)
- Email notifications to principal on escalation
- Sender email capture
- 4 starter templates

### What does NOT ship in MVP
- Payment routing to charity / org / splits
- Analytics beyond basic thread counts
- Team / delegation features
- CRM integrations
- Self-serve signup (curated launch only)
- Intent marketplace / sender matching

---

## 3. Launch Strategy

### Model: Curated first wave
- 10-20 hand-picked principals
- High-value attention problems where ante amount and AI quality matter most
- Request early access + invite codes on homepage
- NOT a Product Hunt launch — quiet rollout to avoid broadcasting roadmap to competitors

### Why curated, not self-serve
Self-serve risks a principal creating a line that embarrasses them — wrong tone, leaked criteria, bad decline. Trust is destroyed in one interaction. Curated launch lets us get judgment, tone, and economics right before opening up.

### CTA on homepage
- Primary: "Request early access" (email capture)
- Secondary: "Have an invite code? Enter it here"

---

## 4. Moat Thesis

### Step function (what we ship)
Payment + AI triage. This is defensible for ~6 months. Someone will clone it.

### Moat (what we build over time)

**Phase 1 — Sender reputation (network effect):**
Same senders appear across multiple principals. A founder who got escalated by 8 of 10 lines has a reputation score. A vendor who got declined everywhere is flagged. Cross-principal intelligence that no individual principal and no email client can build.

**Phase 2 — Intent marketplace (with principal consent):**
Every sender declares explicit, paid intent. Every principal declares what they want. With opt-in, Ante can match — not just filter. "Three vendors match your open requirement for agent orchestration auditing, and they've already been qualified."

**Where this lives:** Investor pitch deck. NOT in launch messaging. NOT on the homepage.

---

## 5. Homepage Decisions

### Audience
ante.so is the commercial product page. Developers get docs (docs.ante.so or ante.so/docs).

### Hero
- **Headline:** "Your attention has a price."
- **Energy:** Payment thesis — validates the principal, makes them feel seen
- **Illustration:** 3-slide auto-rotating carousel showing the full product loop (sender chats → AI asks follow-ups → escalation email to principal with context on why it matters)

### Carousel slides
1. **Investor** — `pitch@a16z`, $20 ante. AI compliance startup. Escalation tells VC it aligns with their agent-context thesis.
2. **Enterprise Buyer** — `vendor@scb-uk`, $3,000 ante routed to IT cloud pool. Agent orchestration auditor. Escalation tells CIO it matches their open requirement.
3. **Authority Figure** — `contact@obama`, $17,500 ante routed to Obama Foundation. Code2040 keynote request. Escalation tells team it aligns with equity-in-tech priorities.

### Sections killed (V3 → V4)
- **"How it works" (1-2-3 steps)** — redundant, carousel shows it
- **"Conversation, not a form" (accent band)** — redundant, carousel shows it
- **"Bring your LLM key / BYOK"** — wrong audience for launch, too much infrastructure detail

### Sections kept / added
- **Proof bar** — "Payment proves intent · Criteria stay hidden · Your voice, your rules · Open-source core"
- **The problem** (dark band) — "When sending is free, noise wins." + Polymarket/congestion charge framing
- **Before / After comparison** — inbox today vs. with Ante
- **Who it's for** — 4 persona cards (Investors, Enterprise Buyers, Partnerships, General)
- **Economics** — 3 tiers: $0 (free line), $5-$500 (noise floor), $5K+ (conviction ante)
- **CTA** — Request early access + invite code

---

## 6. Brand & Voice Updates

### Hero copy changed
- V3: "Your attention has a front door."
- V4: "Your attention has a price."

### Problem section sharpened
Added the key insight: "Smarter inboxes won't fix this. Every email client will ship AI triage. But no one has put a toll in front of attention itself."

### Voice registers updated
- "Gate voice" → "Line voice"
- No other register changes

### Words we don't use (added)
- "gate" (in commercial/public contexts)

---

## 7. Files Delivered

| File | Description |
|---|---|
| `ante-homepage-v4.html` | Complete homepage with carousel, all sections, responsive |
| `brand-guidelines-v4.md` | Full brand doc with line terminology, payment-as-core, launch strategy |
| `Thesis-v4.md` | Updated thesis with moat thesis, payment differentiator, curated launch |
| `README-v4.md` | Updated repo README |
| `v4-handoff.md` | This document |

---

## 8. Open Items for Implementation

- [ ] Stripe Connect Express integration
- [ ] Line page template system (4 starters)
- [ ] AI conversation engine (clarify/decline/escalate loop)
- [ ] Principal dashboard (escalated threads, summaries)
- [ ] Escalation email design and delivery
- [ ] Invite code system for early access
- [ ] Email capture for waitlist
- [ ] line.yaml config schema (amount, timing, criteria, voice)
- [ ] Sender-facing page design (V4 line page — not yet updated from V3)
- [ ] Thread page design (V4 thread page — not yet updated from V3)
- [ ] Investor pitch deck (includes moat thesis + intent marketplace)
