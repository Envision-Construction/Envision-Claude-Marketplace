# Buildr Public API Docs — Captured Reference

Captured 2026-05-23 via `claude-in-chrome` from the login-gated docs at https://docs.buildr.com (the user's authenticated session). The docs themselves declare the API as a **Beta Service**. Public docs and our Envision-MCP integration disagree on one important detail (base URL) — flagged below.

## ⚠ Base URL discrepancy (verify before assuming the integration is right)

| Source | Base URL |
|---|---|
| Public docs (https://docs.buildr.com/api-guide/getting-started) | `https://api.buildr.com/api/beta/` |
| Envision-MCP integration (`config/buildr_settings.py`) | `https://api.buildr.com/v1` |

Both URLs are plausibly live (Buildr may keep `/v1` as an internal/legacy path or both may resolve via a router). If you ever see `404 Not Found` on a resource that the public docs list as available — e.g. `/financials/billing_periods`, `/projects/{id}/documents`, `/workforce` — the first thing to check is whether `BUILDR_BASE_URL` should be flipped to `/api/beta/`. Don't change it speculatively; coordinate with whoever owns the gateway.

## Auth

- OAuth2, two grant flows supported: **Authorization Code** and **Client Credentials**.
- Envision-MCP uses Client Credentials (`POST https://api.buildr.com/oauth/token`, `grant_type=client_credentials`). Access token ~2h, gateway refreshes ~5min early.
- Request header on every call: `Authorization: Bearer <access_token>`.
- There is **no separate `/api-guide/authentication` page** in the public docs (it returns 404) — auth details live only on `/api-guide/getting-started`.

## Rate limits (per Buildr account)

| Bucket | Limit | Window |
|---|---|---|
| Burst | 20 requests | 10 seconds |
| Hourly | 2,000 requests | 1 hour |
| Daily | 48,000 requests | 24 hours |

When a bucket overflows the API returns `429 Too Many Requests` with body:

```json
{
  "error": "rate_limit_exceeded",
  "message": "Burst rate limit exceeded",
  "bucket": "burst",
  "limit": <int>
}
```

The Envision-MCP `requests.Session` retries 3× with backoff on 429/5xx automatically. Multi-tenant note: these limits are per Buildr account, not per OAuth client — heavy concurrent operations from other Buildr integrations on the same account share the budget.

## Response envelopes

Consistent across all endpoints:

| Operation | Envelope |
|---|---|
| Create (`POST /<resource>`) → 201 | `{ "item": {...} }` |
| Get (`GET /<resource>/{id}`) → 200 | `{ "item": {...} }` |
| List (`GET /<resource>`) → 200 | `{ "items": [...] }` plus pagination metadata |
| Update (`PATCH`) → 200 | `{ "item": {...} }` |
| Delete (`DELETE`) → 204 | empty |

Resources always have `id` (string), `created_at`, `updated_at`. Nested associations are returned as embedded objects (e.g. `created_by: { id, first_name, last_name, email, ... }`), not as id-only references. Field naming is `snake_case` throughout.

The Envision-MCP integration unwraps these envelopes internally — `b.get_companies()` returns the array, not the wrapper object — so session-side code rarely sees the raw envelope.

## Pagination

The docs page renders but most of its content is filtered by the claude-in-chrome safety layer (cursor strings trip the filter). Captured section structure:

- Using pagination in the REST API
- About pagination
- Using link headers
- Changing the number of items per page

Translation by inspection of the integration code: Buildr uses **page-number pagination** (`?page=N&per_page=100`). The integration walks pages until `meta.total_pages` is reached. Cursor-based pagination via `Link` headers is also documented but not used by the current integration.

For very large reads, narrow with filter params (e.g. `?company_id=...`) rather than walking the full table.

## Webhooks

Captured section structure (content filter blocked the body):

- Introduction
- Creating a webhook
- Example Payload
- Supported Webhooks
- Securing your webhook

Confirmed from the getting-started page: webhooks are POST callbacks to an endpoint URL you configure in your Buildr account; payloads include the changed entity's `id` and `url` for fetching the full resource. The Envision-MCP integration has the receiving end wired in `gateway/webhooks/buildr.py` — sessions don't typically need to think about webhooks unless they're debugging missed events.

If you need the actual signing scheme or the supported event list, read it directly in your browser at https://docs.buildr.com/api-guide/webhooks (the docs site is login-gated).

## Full resource surface (52 categories)

Buildr's public API is **much wider than the Envision-MCP integration exposes** (12 resources via `buildr_read` / `buildr_write`). Anything in the list below that the integration doesn't cover is reachable only by extending the gateway — sessions cannot call it directly.

```
bidding-package         call                    call-outcome
comment                 company                 company-role
contact                 contract-type           custom-field
custom-field-group      delivery-method         division
document-categories     email                   financials-billing-periods
financials-change-orders financials-closed-periods financials-forecast-periods
financials-prime-contracts forecast-periods     gng-feature
gng-lead-answer         gng-lead-survey         gng-project-answer
gng-project-survey      gng-survey-template     gng-survey-template-question
industry                lead                    lead-source
loss-reason             market-sector          meeting
project                 project-changeset       project-directory-contacts
project-directory-memberships project-document-folders project-documents
project-event           project-event-type      project-photos
project-stages          project-team-membership project-team-role
task                    task-list               tender-type
trade                   user                    webhook
webhook-message         work-scope              workforce
```

Resources currently exposed via Envision-MCP (per `gateway/strap/buildr.py`): `deals` (Buildr's `leads`?), `pipeline`, `companies`, `contacts`, `projects`, `activities` (Buildr's `call` / `meeting` / `comment`?), `tasks`, `tags`, `users`, `custom_fields`, `reports`, `connection`.

Resources visible in public docs but NOT in Envision-MCP that look high-value for Envision workflows:
- `financials-billing-periods`, `financials-change-orders`, `financials-prime-contracts` — money flow tied to a project
- `project-documents`, `project-document-folders`, `project-photos` — operational artifacts
- `project-directory-contacts`, `project-directory-memberships`, `project-team-membership` — who's working on what
- `workforce`, `division`, `market-sector` — org context
- `lead-source`, `loss-reason`, `market-sector` — win/loss analysis dimensions

The integration also exposes a `deals` resource that doesn't directly appear in the public docs. The integration code (`integrations/buildr.py`) routes `get_deals()` to `/leads`, suggesting Envision named the abstraction "deals" but Buildr calls them "leads." Worth keeping in mind when reading the public docs alongside the integration.

## Example API reference page (Create bidding package)

Canonical shape of one endpoint page from https://docs.buildr.com/api-reference/bidding-package/create-bidding-package:

```
POST /api/beta/bidding_packages
Authorization: Bearer <token>
Content-Type: application/json

{
  "bidding_package": {
    "project_id": "769",
    "name": "Earthwork",
    "cost_code_id": "456",
    "description": "Core scope package",
    "due_date": "2026-04-18"
  }
}

→ 201
{
  "item": {
    "id": "483",
    "created_at": "...",
    "updated_at": "...",
    "name": "Earthwork",
    "description": "Core scope package",
    "bidder_reminder_frequency": "weekly",
    "portal_submission_deadline_rule": "due_date",
    "due_date": "2026-04-18",
    "due_date_includes_time": false,
    "account_id": "123",
    "project_id": "769",
    "cost_code_id": "456",
    "cost_code_number": "03-3000"
  }
}
```

Key patterns visible from this and the list-companies endpoint:
- Request body is namespaced under the resource singular: `{ "bidding_package": { ... } }` for create, NOT `{ ... }` directly. Each resource has its own wrapper key.
- All ids are strings even when numeric (`"id": "483"`).
- Timestamps are ISO 8601 UTC with `Z` suffix.
- Resources can carry derived fields the server populates (e.g. `cost_code_number` from the related cost_code).

## Source links (require Buildr login)

- API Guide index: https://docs.buildr.com/api-guide/getting-started
- Rate limiting: https://docs.buildr.com/api-guide/rate-limiting
- Pagination: https://docs.buildr.com/api-guide/pagination
- Webhooks: https://docs.buildr.com/api-guide/webhooks
- API Reference (any endpoint, e.g.): https://docs.buildr.com/api-reference/company/list-companies
- `https://docs.buildr.com/llms.txt` is referenced by the docs but returns 404 in practice (don't waste time on it).
