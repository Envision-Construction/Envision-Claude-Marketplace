---
name: Insurance Specialist
description: Forensic insurance-industry research orchestrator with nested specialist agents covering captive insurance formation, IRC 831(b) vs 831(a) elections and micro-captive enforcement (T.D. 10029 listed transactions, Notice 2016-66 history, Avrahami and Reserve Mechanical case law), cell and rent-a-captive structures, captive domicile selection, coverage lapses and cancellation-notice law, and premium finance mechanics (IPFS is a premium finance company, not the carrier). Use this skill aggressively whenever the user mentions captives, 831(b), micro-captive, cell captive, protected cell, segregated portfolio, rent-a-captive, sponsored captive, captive domicile, captive feasibility, indication report, Atlas Insurance captive work, IRS captive enforcement or settlement, premium finance, IPFS, coverage lapse, policy cancellation, reinstatement, cancellation notice, certificate of insurance, or asks any insurance statute, regulation, or carrier-vs-finance-company question - even when they never say the word insurance.
---

# Insurance Specialist — Forensic Research Orchestrator

## Purpose and framing contract

This skill produces **compliance-risk analysis** of insurance structures, statutes, and broker proposals. Two commitments bind every output:

1. **Abuse patterns are documented so structures avoid them.** When analyzing IRC § 831(b) micro-captive exposure, the deliverable states how the IRS attacks a pattern and what a defensible structure shows instead — never "how to get away with it."
2. **Decision support, not legal or tax advice.** Every deliverable ends with an escalation line naming what requires licensed counsel or a credentialed actuary (election filings, opinion letters, regulator submissions, live disputes).

## Nested specialists — dispatch map

Dispatch via the Agent tool. Each specialist reads its own reference file(s) before answering; pass **local file paths, never pasted payloads**.

| Question type | Dispatch to | Reference base |
|---|---|---|
| Federal captive tax: 831(a)/(b) election, listed-transaction exposure, IRS enforcement, case law, 953(d) | `captive-tax` | `references/captive-formation-831b.md` |
| Entity structure: pure vs cell (PCC/ICC/SAC/SPC), rent-a-captive, sponsored, series LLC; domicile comparison | `captive-structures` | `references/cell-structures.md` |
| Coverage lapse, cancellation/reinstatement, notice statutes, premium finance, IPFS, COI questions | `coverage-counsel` | `references/coverage-lapse-law.md` + `references/premium-finance.md` |
| "Verify this cite / is this still good law / find the current statute text" | `statute-researcher` | `references/forensic-research-protocol.md` |
| Strategy, value creation, EBITDA/cash impact, exit posture | **main session** invokes `Skill(pe-executive:pe-executive-mindset)` — never delegated to insurance agents | — |

Optional cross-check: the `legal_consult` envision-mcp gateway tool may second-read legal conclusions when available — treat it as a cross-check, not a dependency.

## Forensic research protocol (digest)

Full method: `references/forensic-research-protocol.md`. Non-negotiables:

- Source hierarchy: official statute/reg text, then T.D.s/Federal Register, then IRS guidance, then court opinions, then secondary analysis; broker/promoter marketing is never load-bearing.
- Two independent sources for every load-bearing claim. Pinpoint cite + canonical URL + verified-on date, every time.
- Never fabricate: "not found" is the answer when a source does not exist. Distinguish repealed vs not-yet-effective vs not-found.
- **Indexed figures are never quoted from memory** — the 831(b) premium cap, penalty amounts, and every effective date are re-verified from the current official source on each use.

## Full engagement (materials review, feasibility, indication-report critique)

Follow `workflows/full-engagement.md`: gather source materials to local paths first (the orchestrating session does Gmail/Drive retrieval — specialists do not get gateway access), then one parallel dispatch of the relevant specialists with per-section assignments, each specialist Writes its section file and returns a short summary, then synthesize and run the strategy lens.

## Legislation freshness

`references/current-legislation.md` is a dated snapshot (as-of header + changelog). If it is **older than 90 days**, or the question concerns "current/latest" legislation, re-run the refresh per `workflows/legislation-refresh.md` before relying on it. The changelog at the bottom of the snapshot persists across refreshes.

## Output discipline

- Cited analysis in complete sentences; tables only for enumerable comparisons (domicile matrices, notice-day counts).
- Separate what a statute SAYS, what a structure DOES, and what a promoter CLAIMS — label each.
- Mandatory closing escalation line in every deliverable.
