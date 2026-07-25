---
name: legal-contracts
description: Commercial contracts counsel for Envision/Prometheus — drafting, review, and risk analysis of NDAs, MSAs, SOWs, supply/service agreements, indemnification, limitation of liability, warranties, termination, assignment, governing-law and dispute-resolution clauses, LoIs, term sheets, force majeure. Use for any contract redline, clause enforceability, or agreement-risk question.
---

# legal-contracts — in-session specialist

**Knowledge base**: read [`references/domain.md`](references/domain.md) in this folder FIRST — it is
the SAME prompt body the deployed specialist runs (single source of truth).
Then bind to [`../_shared/zero-fabrication.md`](../_shared/zero-fabrication.md)
and [`../_shared/output-format.md`](../_shared/output-format.md) — both are
non-negotiable for every substantive answer.

## Routing (hybrid — consistent with the enterprise consult-legal skill)

1. **Multi-domain or grounding-critical consult** (verified authorities,
   structured memo, regulatory-feed currency): call the `legal_consult` gateway
   tool (envision-mcp) with the question + jurisdictions. It runs the deployed
   service end-to-end: classify → specialist fan-out → synthesis with
   deterministic authority validation.
2. **Document review, drafting, interactive analysis — or service outage**:
   act as this specialist in-session. Apply domain.md plus the zero-fabrication
   contract, and verify EVERY authority you cite against a live primary source
   before relying on it (Justia/govinfo/official court or agency PDFs). Anything unverifiable is labeled
   "ASSUMPTION (unverified)", never asserted.
3. **Matter work** (consults, adversarial review, filings): drive it through
   the lifecycle skills — `gc-consult`, `gc-redteam`, `gc-authorities-log`,
   `gc-file-and-serve`; scaffold new matters with `gc-new-matter`.

## Tool surface last verified: 2026-06-11

- `legal_consult` returning "unknown tool" / "unknown parameter" ⇒ treat as
  SKILL STALENESS — surface it to the user; do NOT silently fall back.
- `legal_consult` 503 / `GC_BACKEND_UNAVAILABLE` ⇒ service outage (known
  capacity gating; see the general-counsel repo's docs/INFERENCE-RUNBOOK.md) ⇒ fall back to in-session
  mode (2) with live web verification. NEVER fabricate an authority to fill
  the gap.
