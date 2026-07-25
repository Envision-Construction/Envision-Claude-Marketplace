---
name: gc-consult
description: Run a grounded GC consult — jurisdiction/posture first, 3+ specialist lenses, every load-bearing authority verified against a live primary source, conclusion-first memo with verdict, fallback ladder, and authority index. Use before any hearing, deadline, filing decision, or strategy call. Triggers on "run a consult", "GC consult on X", "what's our strategy for the hearing", "what are our options before <deadline>", "analyze our position in <matter>", "forensic consult".
---

# gc-consult — the deterministic consult pathway

Binding contracts: [`../_shared/zero-fabrication.md`](../_shared/zero-fabrication.md)
and [`../_shared/output-format.md`](../_shared/output-format.md). Never fabricate
an authority; an unverifiable claim is labeled "ASSUMPTION (unverified)".

Execute the steps below IN ORDER. Each step's outcome dictates the next —
no judgment calls about sequencing.

## STEP 1 — Jurisdiction & posture

Establish forum, governing law, procedural posture, and controlling dates
BEFORE any substantive work. No silent defaults. In a matter repo, read the
matter's `00-*` anchor doc first. Carry these four facts into every later step.

## STEP 2 — Call the deployed service (`/consult-legal` path)

Call the `legal_consult` gateway tool (envision-mcp) with: the question
verbatim + the jurisdictions from STEP 1. This is the deployed General Counsel
service — the productionized descendant of the org `/consult-legal` skill
(prompts ported 2026-06-10) — running classify → 9-specialist fan-out → Opus
synthesis with deterministic authority validation.

Outcome table (exactly one row applies):

| Gateway result | Next action |
|---|---|
| Structured answer (200) | Go to STEP 4 with the returned `{answer, authorities, jurisdictions, assumptions, limitations}` |
| "unknown tool" / "unknown parameter" | SKILL STALENESS — surface to the user verbatim; STOP. Do not silently fall back. |
| 503 / `GC_BACKEND_UNAVAILABLE` | Service outage (capacity gating; general-counsel repo `docs/INFERENCE-RUNBOOK.md`). Go to STEP 3. |
| Tool call denied/blocked before reaching the service (local permission mode, MCP server not connected) | Record "gateway unreachable in this environment" in LIMITATIONS. Go to STEP 3. |
| User explicitly asked for in-session / interactive / document-review work | Skip the gateway; go to STEP 3. |

**Tool surface last verified: 2026-07-04.**

## STEP 3 — Dispatch the general-counsel orchestrator

Dispatch ONE agent: `general-counsel:general-counsel` (this plugin's
supervisor). Its prompt must contain, in order: (a) the question verbatim,
(b) jurisdictions, (c) posture + controlling dates from STEP 1, (d) any
matter-file facts the specialists need. The orchestrator deterministically
selects 3–5 specialist lenses from the supervisor routing table, taps this
plugin's bundled insurance-specialist agents when captive/coverage/premium-finance
issues are present, fans out in parallel, synthesizes, and returns the full
memo (VERDICT / per-lens analysis / fallback ladder / LIMITATIONS / AUTHORITY
INDEX) with the mandatory method line. Do not re-run its work; verify its
method-line counts are real numbers before delivering.

For single-lens document review or interactive drafting, dispatch the one
matching `general-counsel:legal-<area>` agent directly instead of the
orchestrator.

## STEP 4 — Deliver

- **In a matter repo** (a repo with a `matters/` tree): write the memo as
  `CONSULT-<YYYY-MM-DD>.md` in the matter folder with the matter's privilege
  header, then surface the VERDICT in the response.
- **Anywhere else**: deliver the memo in the response (or to a path the user
  names).

Every delivery opens with the method line — real counts, or it is not done:

> Method: multi-specialist consult (GC service pattern: grounding →
> N specialists → adversarial verification). **N findings verified against live
> primary sources** (name the source classes); **N load-bearing claims
> adversarially checked; N corrected.** Not legal advice; for review by
> retained counsel.

## Matter lifecycle (general-counsel repo only)

The matter-lifecycle skills are repo-local to the general-counsel repo (where
privileged `matters/` work product lives): scaffold via `gc-new-matter`; after
the consult, run `gc-redteam` before anyone acts on it; any resulting filing
goes through `gc-authorities-log` then `gc-file-and-serve`.
