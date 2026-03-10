# InboundAI Agent Access

## Recommendation
Use an API as the source of truth. Add MCP on top later.

## Why API First
- search, auth, billing, rate limits, and usage policy belong in an application API
- threads, replies, and handoffs are stable app concepts
- web, mobile, and automation clients can all share the same contract
- the commercial product will likely charge per routed thread or per token band, which is easier to manage in an API

## Why MCP Later
MCP is useful as an adoption layer for agent-native clients.

Use it later for tools like:
- `search_people`
- `list_desks`
- `start_thread`
- `reply_to_thread`
- `get_thread_status`

But those tools should call the same InboundAI API underneath.

## Product Model
Human users:
- open a public intake page
- send a message
- continue the thread in the web UI

Agent users:
- search for a person or desk
- open a thread through API or an MCP tool that wraps the API
- receive the same reply types as humans

## Search
Longer term, "search the human you want to reach" should be an application feature, not just a prompt trick.

Likely model:
- directory of public desks
- searchable by person, topic, company, or route
- each result resolves to a desk slug and thread endpoint

## Cost
Cost can attach to:
- premium routed threads
- paid priority lanes
- agent-originated usage bands
- enterprise or managed routing plans

If cost exists, it should be explicit before thread creation.
