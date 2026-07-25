---
name: Specialized Asset Finance
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Use when evaluating asset-based lending, equipment and leasing structures, or non-recourse / limited-recourse project finance. Apply it to borrowing-base facilities, residual-value underwriting, and project structures where repayment depends primarily on collateral value, contracted asset cash flows, or both.
category: structured-finance
related_skills:
  - memo-generator
  - modeling-and-valuation
  - debt-structure-covenants
  - surveillance-monitoring
  - industry-sector-analysis
  - securitization-and-clos
triggers:
  - ABL
  - asset finance
  - asset-backed lending
  - asset-based lending
  - borrowing base
  - collateral valuation
  - debt sculpting
  - equipment finance
  - finance lease
  - infrastructure lending
  - leasing
  - non-recourse lending
  - project finance
  - reserve account
  - residual value
  - sale-leaseback
  - shipping finance
  - LLCR
  - PLCR
  - DSCR project
  - EPC contract
  - concession finance
  - offtake agreement
disambiguation: |
  Prefer this skill when the context involves project finance SPVs, ABL borrowing bases, equipment or fleet collateral, or non-recourse lending against contracted asset cash flows.
  For CLO/ABS/RMBS/CMBS structures, use securitization-and-clos.
  For corporate leverage analysis, use modeling-and-valuation.
---

# Specialized Asset Finance

Specialized asset finance begins with the true source of repayment: collateral liquidation value, contracted project cash flow, or a hybrid of the two. Underwrite legal control, cash controls, asset durability, and downside recovery before relying on sponsor upside, headline leverage, or market convention.

## Core Workflow

1. **Classify the repayment source**: Determine whether debt is supported primarily by borrowing-base collateral, lease cash flows and residual value, contracted project cash flows, or a hybrid structure.
2. **Map the legal structure and control points**: Identify the borrower or SPV, key contracts, lien package, account control, perfection steps, and any step-in or transfer rights.
3. **Underwrite asset quality and durability**: Assess useful life, maintenance burden, remarketing depth, technological obsolescence, and whether the asset is essential to the obligor or project.
4. **Test operating cash flow and coverage**: Build debt service capacity from borrowing-base availability, lease cash flows, or project CFADS, and evaluate how reserves and waterfalls protect debt service.
5. **Allocate the major risks**: Decide which party bears construction, operating, counterparty, market, regulatory, and residual-value risk, then identify where risk transfer is incomplete.
6. **Pressure test the downside path**: Stress collateral value, utilization, charter or lease coverage, contract enforceability, refinancing assumptions, and exit liquidity.
7. **Translate the analysis into a lender view**: Summarize borrowing capacity, structure, monitoring needs, covenant protections, and the triggers that would impair repayment or recovery.

## Reference Map

Read the most relevant reference for the question rather than loading the full library.

### Asset-Backed and Leasing Foundations
- `references/asset-based-lending-abl-fundamentals.md` - Borrowing-base mechanics, collateral eligibility, monitoring, and dominion concepts.
- `references/equipment-finance-leasing.md` - Lease structure, sale-leasebacks, amortization matching, and residual-value risk.
- `references/sector-specific-asset-finance.md` - Sector-specific underwriting for project finance sectors (power, renewables, infrastructure, PPP) and asset finance sectors (aircraft, shipping, rolling stock).

### Project Finance Foundations
- `references/project-finance-fundamentals.md` - When project finance fits, how non-recourse structures differ from corporate lending, SPV structure, key contracts, and lender control rights.
- `references/risk-identification-allocation.md` - Construction, operating, revenue, counterparty, and regulatory risk allocation.

### Analytical Methodologies
- `references/asset-valuation-for-lending.md` - Valuation hierarchy, recovery framing, and appraisal discipline.
- `references/credit-analysis-framework-for-asset-finance.md` - Dual-lens underwriting across collateral quality and obligor quality, plus diligence checklist, monitoring, and early-warning framework.
- `references/cash-flow-waterfall-debt-sculpting.md` - Waterfall design, reserve treatment, sweep mechanics, and sculpted debt sizing.

### Documentation and Tools
- `references/project-finance-closing-documentation.md` - Closing package, direct agreements, intercreditor, and conditions precedent.
- `references/project-finance-credit-metrics.md` - Definitions and use of DSCR, LLCR, and PLCR.

### Worked Example
- `examples/worked-project-finance-example.md` - End-to-end project finance example; use it as an illustration, not as a substitute for current market assumptions.

## Output Deliverables

When asked to analyze asset-backed or project finance structures, produce:

1. **Source citations**: Explicitly cite every legal document, company source, market input, and third-party reference used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Structure and repayment summary**: Explain the borrower or SPV, the repayment source, and the key legal or contractual control points.
3. **Collateral or project asset view**: Summarize asset type, condition, remaining useful life, maintenance needs, and exit or remarketing considerations.
4. **Debt capacity and coverage**: Show borrowing-base availability, valuation support, CFADS, reserve effects, and the relevant coverage ratios by period.
5. **Waterfall and protection package**: Map reserve accounts, sweep triggers, distribution tests, direct agreements, and enforcement or step-in rights.
6. **Stress and recovery view**: Test downside assumptions for utilization, collateral value, contract performance, residual value, refinancing, and counterparty weakness.
7. **Recommendation and open diligence items**: State the lender view, required protections, and the unresolved issues most likely to impair repayment.

## Limitations

- Residual value underwriting is only as durable as maintenance discipline, asset fungibility, and secondary-market depth.
- Project finance models are only as strong as the enforceability of the underlying contracts and the credit strength of the key counterparties.
- Borrowing-base and appraisal outputs are point-in-time tools; they do not eliminate liquidity, execution, or enforcement risk in a stressed exit.
- Cross-border projects can look structurally strong on paper while still carrying material political, currency, or transfer risk.
- For broader framework limitations, consult `skills/memo-generator/references/analytical-limitations.md`.

## Data Quality

- Never silently fill missing diligence, appraisal, or contract information with assumptions. Use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose gaps explicitly.
- Treat root references as calibration inputs, not substitutes for asset-specific facts, legal terms, or current third-party reports.
- When standard analytical frameworks may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.

## Examples

- `examples/worked-project-finance-example.md`: Utility-scale project finance example covering revenue build-up, CFADS, sculpted debt sizing, waterfall mechanics, reserves, and stress testing.
