# Ante — Brand Guidelines

**Version 0.4 · March 2026**

---

## 1. Brand Narrative

### The world changed

Outbound used to cost something — time, thought, a stamp. That cost was a natural filter. If someone wrote you a letter, they probably meant it.

That era is ending fast. GTM is automated. Agents draft outreach at zero marginal cost. A million polished emails can hit your inbox before lunch. The economics flipped: sending is free, but reading is expensive.

Smarter inboxes won't fix this. Every email client will ship AI triage — Claude with Gmail MCP, Superhuman with built-in filtering, Google with priority sorting. But no one has put a toll in front of attention itself. London's congestion charge proved it. Polymarket proved it. Money doesn't lie.

The best executive assistants always understood this. They weren't spam filters. They were judgment layers with taste, tone, and a short memory for what you actually care about this month.

Now that capability can scale — and it can charge.

### What Ante is

Ante is the boundary between you and everyone trying to reach you.

It sits outside your inbox. It doesn't read your email. It doesn't replace your EA. It's a new surface — a front door with its own judgment, its own tone, and its own rules that stay hidden.

You define what you care about. What quality looks like. How decline should sound. What it costs to reach you. Ante enforces all of it in a short, bounded conversation — then surfaces only what earned your attention.

The sender never sees your criteria. They experience a conversation that's direct, fair, and fast. If they have something worth hearing, they get through. If they don't, they're declined warmly. They never know why.

Payment is the core differentiator. Without it, Ante is just a nicer front-end for AI triage that any LLM can replicate. With it, Ante is a new primitive: sender-funded attention access. Five bucks to cover tokens. Fifty to signal seriousness. Five thousand to get in front of an enterprise buyer. Twenty-five thousand to pitch a16z — proving conviction. Or nothing at all — just judgment as the filter. The principal controls the economics. Ante provides the intelligence.

---

## 2. Naming

### The name: **Ante**

In poker, the ante is what you put on the table before you see any cards. You commit something — money, effort, specificity — before you know the outcome. The bad players fold. The serious ones play.

In Latin, "ante" means "before." Anteroom. Antechamber. The space you pass through before you reach the person.

Both meanings map perfectly to the product. The sender doesn't know your criteria. They can't see your cards. But they have to put something on the table — a clear pitch, real context, maybe a payment — and the line decides if it's worth passing through.

**Ante** is the brand name for everything — the commercial product, the open-source core, and the overall identity. One name, one energy, one story. The OSS repo keeps the `opengates` Python package name for backward compatibility, but in all public-facing language (README, website, social), the brand is simply Ante.

### Terminology

| Surface | Name | Usage |
|---|---|---|
| The brand | **Ante** | Marketing, website, product UI, social |
| The hosted product | **Ante** | ante.so, the app, the service |
| The OSS runtime | **Ante** (open-source) | GitHub, README, developer docs |
| Python package | `opengates` | PyPI, imports (technical legacy) |
| A single filter | **a line** | "Open a line for investor inbound" |
| The sender-facing address | **an @-handle** | `pitch@a16z`, `vendor@stripe` |
| The sender-facing page | **(no special name)** | Senders just see the principal's name and open topics |
| The conversation | **a thread** | "The thread is still open" |
| The payment | **the ante** | "The ante is $25,000" |
| The person behind the line | **the principal** | Internal/docs only |
| The person trying to get through | **the sender** | Internal/docs only |

### The "line" concept

A line is the unit of Ante. Each line represents a specific surface for inbound — investor outreach, vendor pitches, partnerships, general contact. Principals can have one line or many.

The word "line" is internal product vocabulary. Senders don't need to learn it. When a sender visits a principal's Ante, they see the principal's name, what topics are open, and what it costs. Just like X doesn't make you think about "handles" and Linktree doesn't make you think about "links." The naming is architecture. The experience is just a conversation.

How it sounds in practice: "I opened a line for investor inbound." "A founder anted $25k on the pitch line — looks strong." "Check your lines, there's a new escalation." "What's your pitch@ link?"

### The @-handle system

Every line has an address: `type@principal`. The left side is the line type (pitch, vendor, collab, contact, etc.), the right side is the principal's identity. This maps to the email mental model but with intention: the sender knows what kind of access they're requesting and the price of requesting it.

Examples: `pitch@a16z` · `vendor@stripe` · `collab@mkbhd` · `contact@you`

### Payment as proof of intent

Payment is not a paywall. It's a signal — and it's the core differentiator. When someone pays $25,000 to pitch a16z, they're not buying access — they're proving conviction. In the MVP, the ante routes directly to the principal's Stripe account. Charity, org-pool, and split routing come later. Free lines are available — effort alone can be the filter. But for high-demand principals, the ante is the market's way of sorting serious from speculative.

Payment is configurable: before the conversation (upfront filter) or after the AI qualifies the sender (earned access). The principal chooses.

---

## 3. Voice & Tone

### Brand personality

**Confident, direct, warm, and a little opinionated.**

Not a bouncer. Not a chatbot. Think of the best EA you've ever met — the one who's friendly but doesn't waste words, who asks exactly the right follow-up question, who tells you "this one's worth your time" and is usually right.

That's the voice. It has a point of view. It respects your intelligence. It doesn't try to impress you.

### The four registers

**1. Marketing voice** (website, README, social)

Thesis-driven. Slightly provocative. The kind of writing where every sentence earns the next one.

- "Your attention has a price."
- "When sending is free, noise wins."
- "The best filter isn't a paywall. It's judgment."
- "Stop triaging. Start charging."

Never: hype, superlatives, "revolutionary," "game-changing," anything that sounds like it was written by a growth marketer at 2am.

**2. Product voice** (UI copy, buttons, status messages)

Calm. Precise. Every word earns its place. The interface should feel like it was designed by someone who respects your time.

- "Thread escalated" not "Great news! This thread has been escalated!"
- "Declined" not "Unfortunately, this submission did not meet our criteria"
- "3 follow-ups remaining" not "You have 3 chances left to clarify"

Never: exclamation marks, emoji, "awesome," "oops," passive voice.

**3. Line voice** (the AI conversation with senders)

Warm but not soft. Direct but not cold. The line is having a real conversation — it's not a form and it's not a chatbot.

- Asks one question at a time
- Never reveals criteria
- Declines without false hope or apology
- Follows up with the question that actually matters, not a generic "tell me more"

Never: "great question!", filler praise, defensive tone, anything that sounds like a customer support bot.

**4. Developer voice** (OSS docs, API reference)

Technical. Opinionated where it matters. Silent where it doesn't. Show the code, explain the why, skip the fluff.

Never: "simply," "just," "easy," "seamlessly," or any word that makes the developer feel dumb when something goes wrong.

### Words we use

line, thread, sender, principal (the person behind the line), decline, clarify, escalate, signal, noise, attention, judgment, criteria, standards, focus, surface (as a verb), bounded, ante (as payment)

### Words we don't

AI-powered, intelligent, smart, revolutionary, game-changing, leverage, utilize, unlock, supercharge, seamless, frictionless, robot, bot, chatbot, spam filter, gate (in commercial/public contexts)

---

## 4. Visual Identity

### Design philosophy

**Architecture, not decoration. But with soul.**

The product controls access. The design should feel like a well-designed building — every detail is considered, but the building doesn't need you to notice. It just works, and you feel it.

At the same time, the brand has personality. Think Linktree's boldness mixed with Stripe's precision. Full-bleed sections, dark bands, accent blocks, subtle hover interactions, and confident typography. The homepage should feel like someone with taste and conviction built it — not a SaaS template.

### Color system

**Light mode (primary)**

| Role | Color | Hex |
|---|---|---|
| Background | Warm white | `#FAFAF8` |
| Surface | Light stone | `#F0EFEB` |
| Text primary | Near-black | `#1A1A18` |
| Text secondary | Warm gray | `#5A5A55` |
| Text tertiary | Muted | `#9C9C96` |
| Border | Faint warm | `#E2E1DC` |
| Accent | Deep teal | `#0D7C66` |
| Accent hover | Darker teal | `#095C4B` |
| Accent soft | Teal wash | `#0D7C660F` |

**Status**

| State | Color | Hex |
|---|---|---|
| Escalated | Forest | `#1A7A3A` |
| Clarifying | Amber | `#A67C00` |
| Declined | Warm red | `#B5432A` |

**Dark mode (secondary)**

| Role | Color | Hex |
|---|---|---|
| Background | Charcoal | `#141413` |
| Surface | Dark stone | `#1E1E1C` |
| Text primary | Off-white | `#EBEBEA` |
| Text secondary | Muted | `#8A8A85` |
| Accent | Lighter teal | `#12A383` |

### Typography

**Inter** for all UI and body text. **JetBrains Mono** for @-handles and code.

| Element | Family | Weight | Size | Tracking |
|---|---|---|---|---|
| Hero headline | Inter | 800 | clamp(2.8rem, 6vw, 4.2rem) | -0.035em |
| Section head | Inter | 750 | clamp(1.8rem, 3.5vw, 2.4rem) | -0.03em |
| Body | Inter | 400 | 1rem | normal |
| Small / meta | Inter | 450 | 0.85rem | 0.01em |
| Buttons | Inter | 600-650 | 0.9rem | 0.01em |
| @-handles | JetBrains Mono | 700-800 | varies | -0.01em |
| Code | JetBrains Mono | 400 | 0.9rem | normal |

### Layout

- Base grid: 4px
- Card radius: 12px (composed, not bubbly)
- Large card radius: 20px
- Max prose width: 680px
- Max marketing width: 1080px
- Body line-height: 1.6, headlines: 1.05-1.15

### Page architecture

- **Homepage** (ante.so) is the commercial product page. Full-bleed marketing with dark bands, accent sections, persona grids, conceptual illustrations, and a strong thesis sell. CTA is "Request early access" with invite code option. Not a SaaS landing page — a story.
- **Line pages** (sender-facing) are clean surfaces showing the principal's name, open topics, and the ante amount. The form IS the product. No jargon — senders don't need to learn "line" or any other internal term.
- **Threads** keep chat bubbles for messages with colored status banners, living on a proper web page.
- **Developer docs** live at docs.ante.so or ante.so/docs. Separate audience, separate voice.

### Logo

Wordmark for now. The product name in Inter 700 with tight tracking. No icon.

---

## 5. Copy — Applied

### Homepage hero

> **Your attention has a price.**
>
> AI made outbound free. A million agents will pitch you before breakfast. Ante puts a price and judgment between you and the flood. Senders ante up. Only the signal gets through.

### How it works

> **One address. Real judgment. A price that filters.**
>
> You open a line — a public address with AI judgment behind it. Senders see what you're open to, pay the ante if there is one, and make their case. The AI runs a real conversation. Only what survives reaches you.

### Sender-facing page

Senders see: the principal's name, what topics are open, the ante amount (if any), and a form to make their case. No product jargon. No explanation of "lines" or "gates." Just a clean surface that says: here's what this person is open to, here's what it costs, make your case.

### Decline

> Thanks for reaching out. This doesn't match what this line is focused on right now.

Two sentences. No false hope. No apology. Warm and final.

### OSS README opener

> **OpenGates** is an open-source runtime for filtering inbound through conversation. You define what you care about in a few Markdown files. The runtime handles the rest — decline, clarify, or escalate — so only the best signal reaches you.
>
> Outbound is getting cheaper every month. This is the other side of that trade.
>
> OpenGates powers [Ante](https://ante.so), the hosted product.

---

## 6. Terminology Migration (V3 → V4)

| Old (V3) | New (V4) |
|---|---|
| gate | line |
| gate page | *(no special name — it's just the sender-facing surface)* |
| gate voice | line voice |
| gate bundle | line bundle (OSS internal only) |
| "Create a gate" | "Open a line" |
| "Investor Gate" | "Investor Line" (or just "Investor Inbound" sender-facing) |
| "Create your Ante" (CTA) | "Request early access" |
| InboundAI | Ante |
| desk | line |
| surface_label: gate | surface_label: line |
| inbound router | *(remove — describe the value, not the category)* |

---

## 7. Brand Architecture Summary

| Layer | Name | Voice |
|---|---|---|
| Commercial product + website | **Ante** | Marketing voice — thesis-driven, opinionated |
| Hosted product UI | **Ante** | Product voice — calm, precise |
| Line conversations | *(line name, e.g. "Investor Line")* | Line voice — warm, direct |
| Open-source core | **Ante** (open-source) | Developer voice — technical, no marketing |
| GitHub / PyPI / dev docs | **Ante** | Developer voice |

---

## 8. Launch Strategy

### Model: Curated first wave

Ante launches with 10-20 hand-picked principals. High-value attention problems — the kind where the ante amount and AI quality matter most. This buys time to get judgment, tone, and economics right before opening up.

The homepage exists and is polished, but it's not a Product Hunt launch. It's a quiet front door for people we send there. CTA is "Request early access" with an invite code path.

### Starter templates (4)

1. **Investor inbound** — deal flow filtering by thesis fit, stage, traction
2. **Sales / vendor to buyers** — sellers pay to get in front of enterprise buyers
3. **Partnership / collab** — brand deals, co-marketing, integrations
4. **General contact** — front door for everything else, free or priced

### Payment in MVP

Ships day one. Simple Stripe Connect Express. Principal sets a price per line (including $0). Sender pays via Stripe Checkout. Money goes to principal. Configurable: before conversation or after AI qualification.

Payment routing (charity, org pool, splits) is V2.

---

## 9. Not Covered Yet

Logo mark, motion guidelines, email templates, social templates, pricing page, onboarding copy, error states, investor pitch deck. Foundation first.
