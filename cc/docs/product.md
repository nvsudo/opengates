# InboundAI Product

## Positioning
InboundAI is the inbound router for scarce attention.

It gives a person:
- a mobile-first public intake surface
- invited topics or desks
- a bounded AI conversation before access is granted
- a clean handoff path when something is worth real attention

## Core Principles
- The thread lives in InboundAI, not in the principal's inbox.
- Inbox read access is not the default product.
- Different kinds of inbound should route through different desks.
- The best outcome is not blocking more. It is letting the right inbound get through.

## Web Identity Rule
Email is mandatory for the web product.

Why:
- it anchors sender identity
- it enables OTP or other lightweight verification later
- it allows the thread to be resumed cleanly
- it gives the system a reliable handoff path for intros or CC flows

This is app-level product behavior, not a per-desk option.

## Handoff Model
The default path is:
1. Sender starts on the web thread.
2. InboundAI asks follow-up questions when needed.
3. If the thread is worth surfacing, the principal gets notified.
4. If approved, InboundAI can send an intro, a CC, or a structured forward.

Email is an edge channel for notification and action, not the source of truth for the conversation.

## Non-Goals For V1
- full inbox integration by default
- unbounded autonomous research
- public agent directory with open write access
- MCP as the primary product interface
