---
name: Private Credit Middle Market
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  This skill applies when evaluating direct lending, unitranche, delayed-draw, sponsor-backed, or non-sponsor middle market private credit opportunities. It focuses on timeless underwriting principles: borrower quality, earnings durability, structure, documentation, lender control, amendment risk, and post-close monitoring. Use root references for current pricing and performance benchmarks, and use the local BDC reference when vehicle-specific private credit constraints matter.
category: private-credit
related_skills:
  - modeling-and-valuation
  - debt-structure-covenants
  - due-diligence-and-assessment
  - industry-sector-analysis
  - portfolio-investment-process
  - surveillance-monitoring
disambiguation: |
  Prefer this skill when the context is direct lending, unitranche, or middle market private credit underwriting.
  For broadly syndicated loan analysis or high-yield bonds, use modeling-and-valuation.
  For covenant document review applicable to both BSL and private credit, use debt-structure-covenants.
  For BDC regulatory constraints in private credit contexts, also read `references/bdc-regulatory.md`.
triggers:
  - private credit
  - direct lending
  - middle market lending
  - unitranche
  - sponsor-backed lending
  - non-sponsor lending
  - delayed draw term loan
  - amendment and waiver
  - private credit underwriting
  - BDC private credit
---

# Private Credit & Middle Market Lending

Private credit underwriting is relationship-driven, structure-sensitive, and documentation-heavy: start with the borrower's durable cash generation and ownership model, then test whether the lender's control package is strong enough to intervene before value leaks away.

## Core Workflow

1. **Frame the borrower and ownership model**: Determine whether the credit is sponsor-backed or non-sponsored, identify the business model, and isolate the underwriting path that really drives repayment.
2. **Normalize earnings and cash conversion**: Scrub EBITDA, capex, working capital, customer concentration, and recurring cash obligations before using any leverage or coverage metric.
3. **Map the capital structure and facility design**: Understand where the lender sits, whether the structure includes unitranche or delayed-draw components, and which features change downside control.
4. **Underwrite documentation and lender protections**: Focus on covenants, EBITDA definitions, baskets, amendment thresholds, information rights, and collateral leakage paths.
5. **Assess ownership behavior**: Underwrite sponsor support, governance quality, and amendment behavior for sponsor-backed deals; underwrite key-person, reporting, and governance substitution for non-sponsored deals.
6. **Stress the amendment path, not just the base case**: Ask how the credit behaves if EBITDA misses plan, rates stay high, acquisitions slip, or the borrower requests covenant relief.
7. **Translate underwriting into portfolio and monitoring terms**: Size the position, identify thesis-kill triggers, and define what must be tracked post-close.

## Reference Map

Read the most relevant reference for the specific question rather than loading the full library.

### Core Underwriting
- `references/private-credit-underwriting-foundations.md` - Private credit model, middle market borrower context, and core underwriting lens.
- `references/unitranche-mechanics.md` - FOLO structure, AAL mechanics, and unitranche-specific risks.
- `references/delayed-draw-structures.md` - DDTL, accordion, revolver, and commitment-structure analysis.

### Analytical Deep Dives
- `references/sponsor-vs-non-sponsor-underwriting.md` - Governance, diligence, covenant, and monitoring differences by ownership model.
- `references/private-credit-documentation.md` - Covenant packages, EBITDA definition risk, lender control rights, and documentation review.
- `references/amendment-waiver-framework.md` - Amendment, waiver, forbearance, and surveillance implications.
- `references/pik-mechanics-analysis.md` - PIK structure, leverage drift, coverage distortion, and return implications.
- `references/post-close-monitoring-framework.md` - Private credit monitoring bridge into surveillance and escalation.
- `references/bdc-regulatory.md` - BDC regulatory framework plus the numeric thresholds that matter when private credit is held in or compared with a BDC.

### Tools and Examples
- `references/private-credit-underwriting-checklist.md` - Compact diligence and IC checklist for new private credit investments.
- `examples/worked-unitranche-case-study.md` - Illustrative end-to-end unitranche example.

## Output Guidance

When asked about a private credit opportunity, produce:

1. **Deal framing**: Borrower, owner, facility structure, use of proceeds, and why this structure exists.
2. **Core underwriting view**: Earnings durability, cash conversion, leverage tolerance, collateral quality, and downside control.
3. **Documentation view**: Maintenance covenants, EBITDA definition quality, baskets, amendment rights, and lender information rights.
4. **Structure view**: Unitranche, DDTL, PIK, guarantee, or sponsor-support mechanics that matter to recovery.
5. **Benchmarking**: Use root references for current spreads, fees, returns, and recovery assumptions; use `references/bdc-regulatory.md` for BDC-specific thresholds when relevant.
6. **Risk summary**: Key risks, mitigants, and what would cause the credit to require amendment, heightened monitoring, or re-underwriting.
7. **Monitoring handoff**: Define the post-close metrics and triggers that should feed `surveillance-monitoring`.
8. **Source citations**: Cite the supporting sources used throughout. When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.

## Scope Guardrails

- Keep skill-level references focused on durable underwriting mechanics, not current market snapshots.
- Use `references/private-credit-performance.md` for current returns, loss rates, and portfolio metrics.
- Use `references/typical-deal-parameters.md` for current pricing, fees, leverage, and call-protection norms.
- Use `references/bdc-regulatory.md` for BDC-specific regulatory and numeric thresholds rather than restating them elsewhere.
- Use `due-diligence-and-assessment` for ESG-specific diligence and broader sponsor or management work when that becomes the primary question.
- Use `debt-structure-covenants` when the issue is primarily split-lien intercreditor design, lien subordination, or documentation leakage outside the private-credit-specific lens here.
- Use `portfolio-investment-process` when the question is mainly portfolio allocation, concentration, or mandate fit rather than single-name underwriting.

## Limitations

- Private credit marks may lag realizable secondary value; compare manager marks to public credit analogs where possible.
- Documentation strength only matters if lenders are willing to enforce it; relationship orientation can weaken theoretical protections.
- Sponsor support can improve outcomes, but sponsor behavior is path-dependent and should not be treated as hard credit enhancement.
- Non-sponsored deals may have tighter documents but weaker information systems and deeper key-person dependence.
- For broader framework limits, consult `skills/memo-generator/references/analytical-limitations.md`.

## Data Quality

- When data is incomplete or unavailable, consult `skills/memo-generator/references/incomplete-data-guidance.md` and disclose the gap explicitly.
- When quoting market data, benchmark spreads, performance, or vehicle constraints, cite the root reference used and check its freshness metadata.
- When discussing current market conditions, read `references/market-benchmarks.md` alongside the relevant private credit root references.

## Examples

- `examples/worked-unitranche-case-study.md` - Illustrative unitranche case showing EBITDA normalization, FOLO structure review, covenant analysis, and monitoring translation.
