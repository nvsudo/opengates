# Ante — Asset Brief

**What's needed to bring the V2 homepage to life.**

The copy and layout are done. These are the visual assets that will replace the placeholder slots on the homepage. None are blocking — the page works without them — but each one significantly raises the quality and personality.

---

## 1. Flow Diagram

**Where:** How It Works section, below the 3 steps
**What:** A clean horizontal flow showing the sender's journey:

```
Sender → Gate page → Conversation (clarify loop) → Decision (decline / escalate) → Principal sees summary
```

**Style:** Minimal, on-brand (warm white bg, teal accents for arrows/decision nodes). Not a wireframe — more like an editorial infographic. Think Stripe Atlas diagrams.
**Format:** SVG or PNG, ~1080px wide
**Priority:** High — this anchors the "how it works" section

---

## 2. Product Walkthrough (Video/GIF)

**Where:** The teal accent band section ("It's a conversation, not a form")
**What:** A 20–30 second screen recording showing a real gate interaction:
1. Someone lands on a gate page
2. Picks a topic, writes their pitch
3. Gate responds with a follow-up question
4. They respond
5. "Escalated" result

**Style:** Clean browser chrome (or no chrome). Could be a GIF loop or a short video. Real gate, real data — not a mockup.
**Format:** MP4 or GIF, 480–600px wide
**Priority:** Highest — this is the "aha" moment. People need to SEE the conversation.

---

## 3. Gate Bundle Screenshot

**Where:** "Under the hood" dark section, next to the file list
**What:** A screenshot of a gate directory in VS Code or a terminal `ls -la`:

```
demo-investor/
├── focus.md
├── standards.md
├── voice.md
└── gate.yaml
```

Bonus: show 3–4 lines of `focus.md` content visible in the editor — something specific and real (e.g., "Looking for: applied AI with real user pull, B2B vertical SaaS with >$500k ARR...").

**Style:** Dark editor theme. Cropped tight. Not a full-screen screenshot — just the relevant panel.
**Format:** PNG, ~500px wide
**Priority:** Medium — the file list in the HTML already communicates this, but a real screenshot adds credibility

---

## 4. Hero Visual (Optional Enhancement)

**Where:** Hero section, right side (currently showing the demo chat mockup)
**What:** The HTML demo mockup already works well here. But if you want to replace it with something higher-fidelity:
- A short video of a live gate conversation
- An animated illustration of messages flowing through a gate
- A stylized screenshot of the actual product

**Priority:** Low — the current chat mockup is doing its job

---

## 5. OG / Social Image

**Where:** `<meta property="og:image">` — what shows when the URL is shared on Twitter/LinkedIn
**What:** Landscape card (1200×630):
- "Ante" wordmark (Inter 800, tight tracking)
- "Your attention has a front door." tagline
- Warm white background, deep teal accent
- Clean, editorial, not crowded

**Format:** PNG, 1200×630
**Priority:** High — this is the first visual impression for anyone seeing a shared link

---

## Notes

- Every asset should feel like it belongs on the same page as the copy — warm, confident, specific.
- Avoid stock photography. Avoid generic SaaS illustrations. If it looks like it could be on any product page, it's wrong.
- Teal accent: `#0D7C66`. Warm white bg: `#FAFAF8`. Dark sections: `#111110`.
