---
name: Account 360
description: Build a complete picture of a single account/company in Buildr — the company record, all contacts there, every open and closed deal, recent activities (calls, meetings, notes), and open tasks. Use this skill whenever the user asks for a full snapshot of one account, wants to see history with a customer or prospect, or is preparing for a meeting. Triggers on "tell me about [Company]", "what's our history with X", "account snapshot for Y", "who do we know at [Company]", "before my meeting with X pull everything we have", "open deals for [Company]", "Buildr profile of [Company]".
---

# Buildr — Account 360

Assemble everything Buildr knows about one company into a single brief.

## Standard sequence

1. **Resolve company_id.** If the user gave a name:
   - `mcp__envision-mcp__buildr_read(resource="companies", action="list")`
   - Match on `name` (case-insensitive, substring). If multiple match, surface them and ask.
   - If the user gave an ID, use it directly.

2. **Parallel fetch** — these 5 reads have no dependencies, batch them in one tool-call block:
   - `buildr_read(resource="companies", action="get", item_id=company_id)`
   - `buildr_read(resource="contacts", action="list", params={"company_id": company_id})`
   - `buildr_read(resource="deals", action="list", params={"company_id": company_id})`
   - `buildr_read(resource="activities", action="list", params={"company_id": company_id})`
   - `buildr_read(resource="tasks", action="list", params={"company_id": company_id})`

3. **Synthesize a brief.** Default layout:

```
# [Company Name] — Buildr Snapshot
Type: prospect/client/subcontractor · Status: active · Owner: [user.name]
Website: … · Industry: …

## Open Deals (n)
| Deal | Stage | Value | Probability | Expected close | Owner |
|------|-------|-------|-------------|----------------|-------|

## Recent Activity (last 30 days)
- 2026-05-21 | call | "..." with [Contact] (15 min)
- ...

## Contacts (n)
| Name | Title | Email | Phone |
|------|-------|-------|-------|

## Open Tasks (n)
- [ ] due 2026-05-30 | "..." (assigned [user])

## Closed Deals (n won, m lost)
[brief list with year and value]
```

## When to use this vs. buildr:crm

Use `buildr:account-360` when the user wants a single-page brief on ONE account. For multi-account analysis, pipeline rollups, or generic CRM questions, fall through to `buildr:crm` (the broader entrypoint).

## Gotchas

- Activities don't always carry `company_id` — some are linked only to a contact or deal. To get full coverage: filter activities by every `contact_id` at the company AND every `deal_id` for the company, then dedupe by activity id.
- Stale companies often have inactive contacts. If the user asks "who should we reach out to", filter to `status="active"` contacts only.
- For meeting prep specifically, surface the most recent activity per contact at the top — that's usually the freshest signal.
- If `contacts.list` doesn't expose a `company_id` filter for some reason, fall back to listing all contacts and filtering in memory by `contact.company_id`.

## Related

- `buildr:crm` — full MCP surface
- `buildr:activity-logging` — log a note right after using this skill to prep a meeting
- `buildr:deal-lifecycle` — when the user wants to act on one of the deals you surfaced
