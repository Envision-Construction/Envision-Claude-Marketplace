---
name: Debt Structure Covenants
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Use when analyzing a credit agreement, bond indenture, intercreditor agreement, amendment package, or capital structure. This skill covers debt ranking, covenant mechanics, documentation leakage, silent debt capacity, LME vulnerability, refinancing structure, and amendment risk for corporate and private-credit borrowers, with a narrow CRE bridge for loan terms and cash-management structures.
category: corporate-credit
related_skills:
  - cre-analysis-underwriting
  - events-distressed
  - memo-generator
  - modeling-and-valuation
  - surveillance-monitoring
  - portfolio-investment-process
  - private-credit-middle-market
  - trading-pricing-mechanics
triggers:
  - amendment
  - anti-LME provisions
  - bond indenture analysis
  - capital structure
  - capital structure analysis
  - change of control covenant
  - covenant analysis
  - covenant headroom
  - covenant-lite
  - credit agreement
  - debt hierarchy
  - debt incurrence
  - debt ranking
  - debt structure
  - documentation risk
  - equity cure
  - events of default
  - intercreditor
  - liability management protection
  - loan agreement review
  - material adverse change
  - ranking of debt
  - restricted payments
  - sacred rights
  - senior secured
  - senior unsecured
  - structural subordination
  - subordinated debt
  - unitranche
  - waiver
disambiguation: |
  Prefer this skill when the core task is reading debt documents, mapping creditor protections, or assessing covenant flexibility.
  For issuer operating performance, leverage, coverage, and downside modeling, use modeling-and-valuation.
  For property underwriting, property-level DSCR/LTV, or CRE market analysis, use cre-analysis-underwriting.
  For CLO/ABS structural tests such as OC/IC coverage, use securitization-and-clos.
---

# Debt Structure & Covenant Analysis

Debt document analysis is about legal capacity and creditor position, not just headline leverage. Start by mapping where each claim sits, what actions the borrower can take without consent, and which protections still matter after definitions, baskets, intercreditor provisions, and amendment history are applied.

## Core Workflow

1. **Map the stack**: Identify each tranche, ranking, security package, guarantee package, maturity, and governing document.
2. **Read the governing documents and amendments together**: The current credit profile is the original agreement plus every amendment, waiver, extension, and side agreement.
3. **Pull the key definitions before judging the covenant**: EBITDA, debt, restricted payments, investments, unrestricted subsidiaries, and collateral release language usually drive the real economics.
4. **Quantify flexibility, not just restrictions**: Measure maintenance headroom, incurrence capacity, silent debt capacity, unrestricted-subsidiary leakage, and amendment optionality.
5. **Test structural protections**: Review sacred rights, pro rata sharing, collateral release mechanics, guarantee release, anti-LME blockers, and intercreditor remedy limits.
6. **Assess refinancing and amendment path**: Determine whether near-term maturities can be refinanced, amended, or extended without materially worsening the creditor position.
7. **Translate the document set into risk**: Summarize how documentation changes recovery, monitoring, pricing, position sizing, or escalation.

## Reference Map

Read the most relevant reference for the question rather than loading the full library.

### Core Structure and Document Reading
- `references/covenant-fundamentals.md` - Why covenants matter, analysis workflow and headroom calculation, maintenance covenant mechanics and enforcement posture.
- `references/credit-agreement-deep-dive.md` - Credit agreement anatomy, core sections, and where risks usually sit.
- `references/documentation-risk-checklist.md` - Systematic checklist for reviewing a new agreement or indenture.
- `references/debt-priority-and-structural-subordination.md` - Formal ranking, recovery order, lien versus seniority distinctions, HoldCo/OpCo issues, guarantee gaps, and practical recovery implications.

### Documentation Leakage and Capacity
- `references/silent-debt-capacity.md` - How to quantify hidden debt capacity across baskets and ratio tests.
- `references/covenant-lite-analysis.md` - How to analyze credits without maintenance covenants.
- `references/lme-covenant-analysis.md` - How to assess LME vulnerability from document language.
- `references/amendment-waiver-dynamics.md` - Amendment mechanics, consent structure, and cumulative documentation erosion.
- `references/refinancing-risk-framework.md` - Refinancing path analysis, maturity pressure, and extension risk.
- `references/lease-accounting-covenant-impact.md` - Lease-adjusted covenant interpretation and comparability issues.
- `references/equity-cure-mechanics.md` - Equity cure mechanics and sponsor-support interpretation.

### Instruments and Structure Types
- `references/advanced-loan-structures.md` - Incrementals, second lien, unitranche, split collateral, and bridge structures.
- `references/negative-covenants-in-bond-indentures.md` - Bond-style incurrence covenants and indenture mechanics.
- `references/coupon-structures.md` - Cash-pay, PIK, toggle, and deferred-pay debt implications.
- `references/maturities-calls-and-puts.md` - Call protection, maturity design, and optionality.

### CRE Bridge
- `references/cre-loan-covenants-cash-management.md` - CRE loan terms, lockbox and trap mechanics, and lender control features.

### Tools
- `references/covenant-comparison-template.md` - Side-by-side comparison template for tranches, amendments, or peer documents.

## Output Deliverables

When asked to analyze debt structure or documentation, produce:

1. **Source citations**: Explicitly cite every filing, agreement, amendment, and market input used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Capital structure map**: Tranches, amounts, maturities, pricing, ranking, security, and guarantee package.
3. **Covenant and capacity summary**: Key maintenance tests, incurrence tests, headroom, silent debt capacity, and major leakage vectors.
4. **Documentation risk flags**: Material weaknesses such as aggressive addbacks, loose baskets, unrestricted-subsidiary leakage, anti-LME gaps, or weak sacred rights.
5. **Intercreditor and recovery view**: Subordination mechanics, release provisions, standstills, purchase options, and recovery implications.
6. **Refinancing and amendment view**: Near-term maturities, springing triggers, amendment history, and likely refinancing or extension path.
7. **Monitoring implications**: What should be watched going forward, what would trigger escalation, and how documentation changes the risk posture.

## Limitations

- Documentation as drafted is not the same as documentation as enforced; lender incentives and collective-action dynamics still matter.
- EBITDA addbacks, pro forma adjustments, and cure mechanics can make formal covenant compliance look better than true creditor protection.
- Intercreditor provisions and anti-LME protections may be untested or fact-specific in litigation; do not treat legal language as certainty of recovery.
- Silent debt capacity and refinancing flexibility are path-dependent; they can shrink or expand materially as EBITDA, asset values, and market access change.

## Data Quality

- Never silently fill missing terms with assumptions. If the agreement, amendment set, or cap table is incomplete, use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose the gap explicitly.
- Separate contractual capacity from practical capacity. A borrower may be allowed to incur debt on paper but unable to access the market on acceptable terms.
- Use `references/credit-agreement-trends-documentation-risk.md` and `references/typical-deal-parameters.md` to calibrate market context, not to override the actual document language.
- When framework outputs may be misleading, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.

## Examples

- `examples/worked-corporate-bb-case-study.md`: Capital structure mapping, covenant analysis, silent debt capacity assessment, and documentation risk framing for a leveraged corporate borrower.
