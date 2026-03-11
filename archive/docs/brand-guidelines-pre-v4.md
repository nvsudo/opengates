# Ante — Brand Guidelines

**Version 0.3 · March 2026**

---

## 1. Brand Narrative

### The world changed

Outbound used to cost something — time, thought, a stamp. That cost was a natural filter. If someone wrote you a letter, they probably meant it.

That era is ending fast. GTM is automated. Agents draft outreach at zero marginal cost. A million polished emails can hit your inbox before lunch. The economics flipped: sending is free, but reading is expensive.

Calendar slots are infinite until Calendly adds a price — then they're commitments. The pattern is the same: when access is free, noise wins. When access costs something — money, effort, specificity — signal wins.

But price alone is a blunt filter. A great cold email from an unknown founder is worth more than a paid message from a PR firm. The real filter isn't a paywall. It's judgment. Judgment that asks the right follow-up question, reads between the lines, and knows when something is worth interrupting you for.

The best executive assistants always did this. They weren't spam filters. They were judgment layers with taste, tone, and a short memory for what you actually care about this month.

Now that capability can scale.

### What Ante is

Ante is the boundary between you and everyone trying to reach you.

It sits outside your inbox. It doesn't read your email. It doesn't replace your EA. It's a new surface — a front door with its own judgment, its own tone, and its own rules that stay hidden.

You define what you care about. What quality looks like. How decline should sound. Ante enforces all of it in a short, bounded conversation — then surfaces only what earned your attention.

The sender never sees your criteria. They experience a conversation that's direct, fair, and fast. If they have something worth hearing, they get through. If they don't, they're declined warmly. They never know why.

Optionally, you can charge. Five bucks to cover tokens. Fifty to signal seriousness. An auction if you want. Or nothing at all — just a hiring page that happens to have judgment behind it. You decide the economics. Ante provides the intelligence.

---

## 2. Naming

### Kill "InboundAI"

"InboundAI" sounds like a feature inside HubSpot. It's descriptive, generic, and forgettable. It doesn't carry the thesis. It dies today.

### The name: **Ante**

In poker, the ante is what you put on the table before you see any cards. You commit something — money, effort, specificity — before you know the outcome. The bad players fold. The serious ones play.

In Latin, "ante" means "before." Anteroom. Antechamber. The space you pass through before you reach the person.

Both meanings map perfectly to the product. The sender doesn't know your criteria. They can't see your cards. But they have to put something on the table — a clear pitch, real context, maybe a payment — and the gate decides if it's worth passing through.

**Ante** is the brand name for everything — the commercial product, the open-source core, and the overall identity. One name, one energy, one story. The OSS repo can keep the `opengates` Python package name for backward compatibility, but in all public-facing language (README, website, social), the brand is simply Ante.

| Surface | Name | Usage |
|---|---|---|
| The brand | **Ante** | Marketing, website, product UI, social |
| The hosted product | **Ante** | ante.so, the app, the service |
| The OSS runtime | **Ante** (open-source) | GitHub, README, developer docs |
| Python package | `opengates` | PyPI, imports (technical legacy) |
| A single filter | **a gate** | "Create a gate for investor inbound" |
| The sender-facing address | **an @-handle** | `pitch@a16z`, `mentor@emusk` |
| The sender-facing page | **a gate page** | "Share your gate page" |
| The conversation | **a thread** | "The thread is still open" |
| The payment | **the ante** | "The ante is $25,000" |
| The person behind the gate | **the principal** | Internal/docs only |
| The person trying to get through | **the sender** | Internal/docs only |

### The @-handle system

Every Ante has an address: `type@principal`. The left side is the gate type (pitch, mentor, collab, hire, etc.), the right side is the principal's identity. This maps to the email mental model but with intention: the sender knows what kind of access they're requesting and the price of requesting it.

Examples: `pitch@a16z` · `mentor@emusk` · `collab@mkbhd` · `hire@stripe`

### Payment as proof of intent

Payment is not a paywall. It's a signal. When someone pays $25,000 to pitch a16z, they're not buying access — they're proving conviction. The ante filters noise at the source. The principal keeps the ante whether they respond or not. Free gates are still available — effort alone can be the filter. But for high-demand principals, the ante is the market's way of sorting serious from speculative.

How it sounds in practice: "I set up an Ante for investor inbound." "A founder anted $25k this morning — looks strong." "Check your Ante, there's a new escalation." "What's your pitch@ link?"

---

## 3. Voice & Tone

### Brand personality

**Confident, direct, warm, and a little opinionated.**

Not a bouncer. Not a chatbot. Think of the best EA you've ever met — the one who's friendly but doesn't waste words, who asks exactly the right follow-up question, who tells you "this one's worth your time" and is usually right.

That's the voice. It has a point of view. It respects your intelligence. It doesn't try to impress you.

### The four registers

**1. Marketing voice** (website, README, social)

Thesis-driven. Slightly provocative. The kind of writing where every sentence earns the next one.

- "Your attention has a front door."
- "When anyone can send anything to anyone for free, noise wins."
- "The best filter isn't a paywall. It's judgment."
- "Stop triaging. Start deciding."

Never: hype, superlatives, "revolutionary," "game-changing," anything that sounds like it was written by a growth marketer at 2am.

**2. Product voice** (UI copy, buttons, status messages)

Calm. Precise. Every word earns its place. The interface should feel like it was designed by someone who respects your time.

- "Thread escalated" not "Great news! This thread has been escalated!"
- "Declined" not "Unfortunately, this submission did not meet our criteria"
- "3 follow-ups remaining" not "You have 3 chances left to clarify"

Never: exclamation marks, emoji, "awesome," "oops," passive voice.

**3. Gate voice** (the AI conversation with senders)

Warm but not soft. Direct but not cold. The gate is having a real conversation — it's not a form and it's not a chatbot.

- Asks one question at a time
- Never reveals criteria
- Declines without false hope or apology
- Follows up with the question that actually matters, not a generic "tell me more"

Never: "great question!", filler praise, defensive tone, anything that sounds like a customer support bot.

**4. Developer voice** (OSS docs, API reference)

Technical. Opinionated where it matters. Silent where it doesn't. Show the code, explain the why, skip the fluff.

Never: "simply," "just," "easy," "seamlessly," or any word that makes the developer feel dumb when something goes wrong.

### Words we use

gate, thread, sender, principal (the person behind the gate), decline, clarify, escalate, signal, noise, attention, judgment, criteria, standards, focus, surface (as a verb), bounded

### Words we don't

AI-powered, intelligent, smart, revolutionary, game-changing, leverage, utilize, unlock, supercharge, seamless, frictionless, robot, bot, chatbot, spam filter

---

## 4. Visual Identity

### Design philosophy

**Architecture, not decoration. But with soul.**

The product controls access. The design should feel like a well-designed building — every detail is considered, but the building doesn't need you to notice. It just works, and you feel it.

At the same time, the brand has personality. Think Linktree's boldness mixed with Stripe's precision. Full-bleed sections, dark bands, accent blocks, subtle hover interactions, and confident typography. The homepage should feel like someone with taste and conviction built it — not a SaaS template.

### Color system

The dark-navy-with-green palette felt like a fintech dashboard. The new direction is quieter and warmer.

**Light mode (primary)**

| Role | Color | Hex |
|---|---|---|
| Background | Warm white | `#FAFAF8` |
| Surface | Light stone | `#F0EFEB` |
| Text primary | Near-black | `#1A1A18` |
| Text secondary | Warm gray | `#6B6B66` |
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

### Why this palette

Warm white feels editorial. Premium without trying. The teal accent is distinctive but composed — it reads as "a decision was made here" without being loud. The overall effect is: someone thoughtful built this.

### Typography

**Inter** for everything. One typeface, used well.

| Element | Weight | Size | Tracking |
|---|---|---|---|
| Hero headline | 800 | clamp(2.8rem, 6vw, 4.2rem) | -0.035em |
| Section head | 750 | clamp(1.8rem, 3.5vw, 2.4rem) | -0.03em |
| Body | 400 | 1rem | normal |
| Small / meta | 450 | 0.85rem | 0.01em |
| Buttons | 600 | 0.9rem | 0.01em |
| Code | JetBrains Mono 400 | 0.9rem | normal |

### Layout

- Base grid: 4px
- Card radius: 12px (composed, not bubbly)
- Max prose width: 680px
- Max marketing width: 1080px
- Body line-height: 1.6, headlines: 1.15

### Kill the device shell

The phone mockup goes. It was a fun 12:30am experiment. It constrains everything.

- **Homepage** is a full-bleed marketing page with dark bands, accent sections, persona grids, product demo mockups, asset placeholders for real imagery, and a strong thesis sell. Not a SaaS landing page — a story.
- **Gate pages** become clean card layouts with a "gate" badge, topic chips, and a tight form. The form IS the product.
- **Threads** keep chat bubbles for messages (that's a real conversation) with colored status banners, living on a proper web page, not inside a fake phone.

### Logo

Wordmark for now. The product name in Inter 700 with tight tracking. No icon. A wordmark in the right typeface at the right weight is a logo.

---

## 5. Copy — Applied

### Homepage hero

**Before:**
> Kicker: "Inbound router"
> Headline: "Let the right inbound get through."
> Body: "InboundAI gives every person a mobile-first intake surface..."

**After:**

> **Your attention has a front door.**
>
> AI made outbound free. Now everyone's in your inbox — agents, bots, cold pitches, noise. Ante puts judgment between you and the flood. Hidden criteria. Your tone. A conversation that filters before you ever see it.

### How it works

> **Define what you care about.**
> A few files. What topics matter, what quality looks like, how you sound when you say no. That's it. No complex setup. Chat with an LLM, drop the files, you're live.
>
> **Senders make their case.**
> They find your gate page, pick a topic, and write. The gate reads it, decides if it needs more, and asks exactly one follow-up at a time. Bounded. Direct. No endless back-and-forth.
>
> **You see only what's worth your time.**
> Declined warmly. Clarified efficiently. Escalated with a clean summary. You decide. The gate did the work.

### Gate page (sender-facing)

**Before:**
> "Hi, I'm Investor Desk. I screen investor inbound for focused, high-signal opportunities."

**After:**
> **Investor Gate**
>
> This gate filters inbound for a specific investor. If your ask fits what they're looking for, you'll be heard. Pick the topic that matches and make your case clearly — relevant detail beats length.

### Decline

> Thanks for reaching out. This doesn't match what this gate is focused on right now.

Two sentences. No false hope. No apology. Warm and final.

### OSS README opener

**Before:**
> "OpenGates OSS MVP — Local-first, agent-native inbound gate runtime."

**After:**
> **OpenGates** is an open-source runtime for filtering inbound through conversation. You define what you care about in a few Markdown files. The runtime handles the rest — decline, clarify, or escalate — so only the best signal reaches you.
>
> Outbound is getting cheaper every month. This is the other side of that trade.
>
> OpenGates powers [Ante](https://ante.so), the hosted product.

---

## 6. Terminology Migration

Everything changes at once. No half-measures.

| Old | New |
|---|---|
| InboundAI | Ante |
| OpenGates (in commercial context) | Ante |
| desk | gate |
| Investor Desk | Investor Gate |
| surface_label: desk | surface_label: gate |
| intake surface / intake | gate page |
| inbound router | *(remove — describe the value, not the category)* |
| mobile-first intake surface | *(kill entirely)* |

---

## 7. Brand Architecture Summary

| Layer | Name | Voice |
|---|---|---|
| Commercial product + website | **Ante** | Marketing voice — thesis-driven, opinionated |
| Hosted product UI | **Ante** | Product voice — calm, precise |
| Gate conversations | *(gate name, e.g. "Investor Gate")* | Gate voice — warm, direct |
| Open-source core | **Ante** (open-source) | Developer voice — technical, no marketing |
| GitHub / PyPI / dev docs | **Ante** | Developer voice |

---

## 8. Not Covered Yet

Logo mark, motion guidelines, email templates, social templates, pricing page, onboarding copy, error states. Foundation first.
