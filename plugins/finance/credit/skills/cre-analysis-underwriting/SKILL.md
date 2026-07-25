---
name: CRE Analysis Underwriting
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Use when evaluating a commercial real estate property, CRE loan, or property-level cash flow. Covers market framing, tenancy and lease rollover, NOI construction, valuation, three-constraint loan sizing, and downside-oriented risk assessment across stabilized, transitional, and development situations.
category: real-estate
related_skills:
  - events-distressed
  - memo-generator
  - modeling-and-valuation
  - surveillance-monitoring
  - debt-structure-covenants
  - industry-sector-analysis
  - portfolio-investment-process
  - securitization-and-clos
  - trading-pricing-mechanics
triggers:
  - CRE underwriting
  - commercial real estate
  - commercial mortgage
  - CMBS underwriting
  - property valuation
  - NOI analysis
  - lease analysis
  - loan sizing
  - debt yield analysis
  - cap rate analysis
  - submarket analysis
  - multifamily underwriting
  - office underwriting
  - industrial underwriting
  - retail underwriting
  - hospitality underwriting
  - construction lending
  - value-add underwriting
disambiguation: |
  Prefer this skill when the context is a property, real estate asset, or CRE loan.
  For corporate leverage, coverage, and issuer-level cash flow, use modeling-and-valuation.
  For cap rate or spread discussion as a market trading input rather than a property valuation input, use trading-pricing-mechanics.
---

# CRE Analysis & Underwriting

Commercial real estate underwriting is property-first and cash-flow-first: start with the asset, market, tenancy, lease rollover, and capital needs, then size debt against durable in-place and stressed performance rather than sponsor upside alone.

## Core Workflow

1. **Frame the asset and market**: Identify property type, location, submarket, competitive position, liquidity, and where the asset sits on the stabilized-to-transitional spectrum.
2. **Build in-place cash flow**: Start from the rent roll, lease terms, occupancy, reimbursements, credit loss, operating expenses, and recurring capital needs to derive in-place NOI.
3. **Separate stabilized from pro forma**: Distinguish what exists today from what requires leasing, renovation, tenant rollover, re-tenanting, or market rent growth assumptions.
4. **Value the real estate through multiple lenses**: Use income capitalization first, then cross-check with sales comparison and cost or replacement context where useful.
5. **Size debt under simultaneous constraints**: Test LTV, DSCR, and debt yield together and identify the binding constraint rather than relying on a single ratio.
6. **Stress the major drivers**: Pressure test occupancy, renewal probability, downtime, TI/LC, operating costs, exit cap rate, and interest rate assumptions.
7. **Translate findings into a lender view**: Summarize proceeds, structure, reserve needs, key diligence items, and the risks that could impair refinanceability or repayment.

## Available References

Read the most relevant reference for the specific question rather than loading the full library.

Unless a path is explicitly rooted at project `references/` or `skills/...`, the `references/...` paths below are skill-local to `skills/cre-analysis-underwriting/`.

### Core Underwriting
- `references/market-submarket-analysis-framework.md` - Market demand, supply, competitive set, and scenario framing.
- `references/property-type-deep-dive-analysis.md` - Property-type operating models, key underwriting questions, and common failure modes.
- `references/lease-analysis-deep-dive.md` - Lease economics, rollover exposure, downtime, concessions, and tenant concentration.
- `references/tenant-credit-assessment-framework.md` - Tenant credit quality, tenant granularity, and concentration analysis.
- `references/income-capitalization-approach.md` - Primary stabilized valuation framework and cap-rate judgment.
- `references/valuation-cross-checks.md` - Cost approach and sales comparison as valuation cross-checks.
- `references/loan-sizing-three-simultaneous-constraints.md` - LTV, DSCR, and debt-yield sizing logic.
- `references/sensitivity-analysis-for-cre.md` - Scenario design, breakpoints, and downside translation to lender risk.
- `references/property-risk-assessment.md` - Physical, legal, market, and execution risk framework.

### Transitional and Development
- `references/construction-development-underwriting.md` - Transitional, value-add, construction, and stabilization-risk underwriting framework.
- `references/environmental-liability-assessment.md` - Environmental diligence, liability pathways, and lender protections.

### CRE Modeling and Metrics
- `references/cre-pro-forma-cash-flow-modeling.md` - NOI buildup, lease types, operating expenses, capex, and value-add scenario modeling.
- `references/commercial-real-estate-credit-metrics.md` - NOI, cap rate, DSCR, LTV, debt yield, and rent coverage ratio definitions and interpretation.

### Workflow and Portfolio Context
- `references/cre-underwriting-checklist.md` - Single checklist covering screening, diligence, approval conditions, and post-close monitoring.
- `references/investment-strategy-spectrum-lender-positioning.md` - Business-plan risk, lender positioning, and downside posture.

### Examples
Examples support application, not principle storage.

- `examples/worked-loan-sizing-example.md` - Simple binding-constraint illustration.
- `examples/worked-office-underwriting-case-study.md` - Full office underwriting case with rollover and refinance risk.
- `examples/worked-multifamily-underwriting-case-study.md` - Full multifamily case with valuation, sizing, and stress testing.

## Output Deliverables

When asked to analyze or underwrite a CRE property or CRE loan, produce:

1. **Source citations**: Explicitly cite every data source, market input, and qualitative fact used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Property snapshot**: Property type, location, size, occupancy, tenant mix, lease rollover profile, and major asset-specific considerations.
3. **Cash flow bridge**: In-place NOI, stabilized NOI, recurring capital needs, and the key differences between current performance and pro forma assumptions.
4. **Valuation and loan sizing**: Value range, proceeds under LTV, DSCR, and debt yield, plus the binding constraint and any reserve requirements.
5. **Stress and sensitivity view**: Downside cases for occupancy, rents, downtime, expenses, exit cap rate, and interest rate assumptions.
6. **Risk and mitigant table**: Tenant concentration, rollover, capex, market liquidity, environmental, sponsor execution, and refinance risk.
7. **Comparable transactions**: Relevant sales, financings, or market markers that help position the subject asset.
8. **Recommendation and open diligence items**: Clear lender view, key conditions, and unresolved diligence requests.

## Limitations

- Cap rate valuation is weakest for distressed, highly vacant, single-tenant, specialty, and ground-up assets.
- Pro forma underwriting often overstates lease-up pace, renewal probability, and rent growth; stress each driver independently.
- Comparable transactions are only useful when tenancy, quality, location, vintage, and transaction timing are truly comparable.
- CRE is intensely local; national benchmarks should calibrate judgment, not replace submarket-specific evidence.
- Insurance, taxes, and capital needs can reprice abruptly; do not treat recent operating conditions as permanent.

## Data Quality

- Never silently fill missing data with assumptions. If information is incomplete, use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose gaps explicitly.
- Keep in-place, stabilized, and sponsor case assumptions separate. Blending them obscures the real risk transfer from present cash flow to future execution.
- Use `references/market-benchmarks.md` and `references/typical-deal-parameters.md` to calibrate assumptions, not to substitute for property-specific facts.
- When standard CRE frameworks may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.


