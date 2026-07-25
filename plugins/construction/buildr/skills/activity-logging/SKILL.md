---
name: Activity Logging
description: Log calls, meetings, and notes into Buildr against the right entity (contact, deal, or company). Use this skill whenever the user mentions they just had a conversation, meeting, or call with someone and wants it recorded, asks to add a note to a deal/contact/company, or wants to capture CRM activity. Triggers on "log this call", "I just met with [Name]", "record a meeting in Buildr", "add a note about [Deal] / [Contact]", "log the conversation with [Company]", "put this in the CRM", "we should log that", "capture this in Buildr".
---

# Buildr — Activity Logging

## Two paths for calls and meetings

The generic dispatcher (post-PR #722) exposes `calls` and `meetings` as full resources alongside the typed `activities` helpers. They are NOT equivalent:

| Path | Action | Minimum required fields |
|------|--------|------------------------|
| Typed adapter (quick log) | `activities.log_call` | `contact_id` only |
| Typed adapter (quick log) | `activities.log_meeting` | `contact_id` only |
| Generic dispatcher (full record) | `calls.create` | `call_outcome_id`, `company_id`, `contact_id`, `recorded_at` |
| Generic dispatcher (full record) | `meetings.create` | `title`, `meeting_at`, `recorded_at`, `company_id` |

Use the **typed adapters** for fast activity logging during a session. Use the **generic dispatcher** when you need a complete CRM record with outcome tracking, duration metadata, or full meeting scheduling details.

---

Record BD activity in Buildr with proper entity linking. Three dedicated helpers exist (`log_call`, `log_meeting`, `add_note`) — prefer them over the generic `activities.create` because they encode the right type and field shape.

## Pick the right action

| User said | Action | Required fields |
|-----------|--------|----------------|
| "log a call" / "I called X" | `activities.log_call` | `contact_id`; optional `notes`, `duration` (int, minutes) |
| "log a meeting" / "I met with X" | `activities.log_meeting` | `contact_id`; optional `notes`, `date` (YYYY-MM-DD or ISO) |
| "add a note about X" | `activities.add_note` | `entity_id`, `entity_type` ("deal" / "contact" / "company"), `note` |
| Email, custom type, or other | `activities.create` | `type`, `description`, `entity_id` |

## Standard sequence

1. **Resolve the target entity.** Users name people, companies, or deals — not IDs. Resolve once before writing:
   - Person → `mcp__envision-mcp__buildr_read(resource="contacts", action="list")`, match by name
   - Company → `buildr_read(resource="companies", action="list")`, match by name
   - Deal → `buildr_read(resource="deals", action="list")`, match by deal name
   - If ambiguous (multiple matches), list them and ask which.

2. **Confirm with the user before writing.** Echo back:
   - The contact / deal / company you matched (name + a disambiguator like company or stage)
   - The activity type, notes/subject, and any date/duration you'll send

3. **Write:**
```
mcp__envision-mcp__buildr_write(
  resource="activities", action="log_call",
  params={"contact_id": "...", "notes": "...", "duration": 30}
)
```

4. **Surface the returned activity id** so the user can reference it.

## Linking rules

One conversation often touches multiple entities (a deal, the buyer's contact record, the buyer's company). Buildr links activities to one primary entity at a time via the action's required field. If the conversation cleanly maps to a contact who is associated with a deal, log it against the contact — Buildr surfaces it on the deal record too via the contact↔deal relationship.

When the user says "log this against the [Company] account" but mentions a specific person, default to the contact-level link (more granular, still rolls up). When the user says "log against the deal", use `activities.add_note` with `entity_type="deal"`.

## Gotchas

- `duration` is minutes, not seconds. "30 minute call" → `duration: 30`.
- `date` for `log_meeting` defaults to "now" if omitted — pass an explicit date when logging after the fact.
- `add_note` is for free-text annotations on any entity — use it when the user says "add a note" rather than "log a call/meeting", and surface where the note lands.
- Don't fabricate `contact_id`s. If you can't resolve one cleanly, either ask the user to disambiguate or offer to create the contact first via `contacts.create`.
- `activities.create` accepts arbitrary `type` (string) for cases the three helpers don't cover (email, demo, site_visit, etc.). Pass `description` for the note body.

## Related

- `buildr:crm` — surface map
- `buildr:account-360` — pull existing activity history before logging the new one
- `buildr:deal-lifecycle` — when logging a stage change, not a touchpoint
