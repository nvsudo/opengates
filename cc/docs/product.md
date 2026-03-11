# Ante Product

## Positioning
Ante is priced access to attention.

It gives a principal:
- a public line page for each kind of inbound they want to receive
- a bounded conversation with judgment before access is granted
- hidden criteria that senders can't game
- direct Stripe payout when a paid line is used
- a clean escalation path when something is worth real attention

## Core Principles
- The thread lives in Ante, not in the principal's inbox.
- Inbox read access is not the default product.
- Different kinds of inbound route through different lines.
- The goal is not blocking more. It's letting the right inbound get through.
- The sender never sees the criteria. They experience a fair conversation.
- Payment is core, but payment never guarantees escalation.
- MVP payment routes directly to the principal. Charity and split routing are post-MVP.

## Web Identity Rule
Email is mandatory for the web product.

Why:
- it anchors sender identity
- it enables OTP or other lightweight verification later
- it allows the thread to be resumed cleanly
- it gives the system a reliable handoff path for intros or CC flows

This is app-level product behavior, not a per-line option.

## Handoff Model
The default path is:
1. Sender starts on the web thread.
2. Ante asks follow-up questions when needed.
3. If the thread is worth surfacing, the principal gets notified.
4. If approved, Ante can send an intro, a CC, or a structured forward.

Email is an edge channel for notification and action, not the source of truth for the conversation.

## Economics
The principal controls the economics of their lines:
- Free — just a smart filter, tokens absorbed
- Priced — direct payment to the principal, used to cover cost or prove seriousness
- Timing — payment can happen before the thread starts or after AI qualification

Payment is a seriousness filter, not a pass. Paying doesn't guarantee access. Quality still has to clear the line.

## Non-Goals For V1
- full inbox integration by default
- unbounded autonomous research
- public agent directory with open write access
- MCP as the primary product interface
- charity, org-pool, or split payment routing
- auctions and priority-lane pricing
