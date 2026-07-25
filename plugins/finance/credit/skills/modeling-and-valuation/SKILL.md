---
name: Credit Modeling and Valuation
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  This skill applies when evaluating a corporate issuer, borrower, or sponsor-backed company through financial spreading, ratio analysis, liquidity, scenario modeling, and valuation cross-checks. Use it for EBITDA normalization, free cash flow analysis, leverage and coverage assessment, refinancing risk, downside modeling, and issuer-level cash-flow work that supports a credit view.
category: corporate-credit
related_skills:
  - events-distressed
  - memo-generator
  - debt-structure-covenants
  - due-diligence-and-assessment
  - industry-sector-analysis
  - portfolio-investment-process
  - trading-pricing-mechanics
triggers:
  - credit modeling
  - credit valuation
  - financial statement analysis
  - EBITDA adjustment
  - adjusted EBITDA
  - LTM EBITDA
  - free cash flow
  - leverage ratios
  - coverage ratios
  - liquidity analysis
  - refinancing risk
  - maturity wall
  - scenario analysis
  - downside case
  - distress probability
  - DCF
  - trading comps
  - precedent transactions
  - LBO model
  - debt schedule
  - accretion dilution
  - covenant EBITDA
  - WACC
  - enterprise value
  - issuer-level cash flow
  - CRE corporate bridge
disambiguation: |
  Prefer this skill when the context is a corporate issuer, company, borrower, or sponsor-backed operating business.
  For property-level underwriting, cap-rate valuation, DSCR/LTV/debt-yield sizing, or lease-driven NOI analysis, use cre-analysis-underwriting.
  For CLO/ABS OC-IC tests and structured-product cash-flow waterfalls, use securitization-and-clos.
  For project-finance DSCR/LLCR/PLCR and debt sculpting, use specialized-asset-finance.
---

# Credit Modeling & Valuation

Corporate credit work starts with durable cash generation, not headline adjusted EBITDA. Anchor on reported results, normalize cautiously, translate earnings into free cash flow, test liquidity and refinancing risk under stress, and use valuation as a downside cross-check rather than a standalone investment answer.

## Core Workflow

1. **Frame the borrower and question**: Identify issuer type, capital structure, ownership, reporting quality, and whether the task is underwriting, surveillance, relative value, or transaction support.
2. **Build the base financial picture**: Spread the income statement, cash flow statement, and balance sheet before making adjustments.
3. **Normalize earnings and cash flow**: Reconcile reported EBITDA to adjusted EBITDA, separate recurring from one-time items, and bridge to free cash flow.
4. **Assess leverage, coverage, liquidity, and refinancing risk**: Analyze debt tranches, maturities, fixed versus floating exposure, covenant headroom, and liquidity runway.
5. **Run scenarios and stress tests**: Pressure test revenue, margins, working capital, capex, rates, and refinancing conditions; add sector or ESG stress when relevant.
6. **Use valuation to frame downside and optionality**: Apply comps, precedent transactions, DCF, and LBO cross-checks to inform recovery, equity cushion, and sponsor behavior.
7. **Translate the work into a credit view**: Summarize key metrics, cash flow durability, major risks, mitigants, and what would change the view.

## Reference Map

Read the most relevant reference for the specific question rather than loading the full library.

### Core Credit Analysis
- `references/ebitda-calculation-the-core-metric.md` - EBITDA construction, adjustment discipline, add-back skepticism, and projection methods.
- `references/free-cash-flow-build.md` - Cash flow statement analysis, cash bridge from EBITDA to actual deleveraging capacity.
- `references/credit-ratios-and-valuation-multiples.md` - Leverage ratios, coverage ratios, rating benchmark interpretation, cash flow ratios, and enterprise value multiples.
- `references/balance-sheet-focus-areas-for-credit.md` - Balance-sheet items that distort or support the credit view.
- `references/credit-quality-and-judgment-calls.md` - Trend-based credit quality framing and analytical judgment guidance.
- `references/return-on-invested-capital.md` - ROIC and reinvestment quality as supporting context for credit durability.

### Modeling, Stress, and Risk
- `references/business-trend-analysis.md` - Revenue, margin, and operating trajectory analysis.
- `references/income-statement-analysis.md` - P&L quality and operating structure.
- `references/revenue-and-expense-modeling.md` - Revenue drivers, forecast architecture, cost structure, and margin sensitivity.
- `references/inflation-cost-pressure-modeling.md` - Margin pressure analysis when costs reprice faster than revenue.
- `references/working-capital-quality-analysis.md` - Working-capital drag, seasonality, and cash conversion.
- `references/liquidity-and-covenant-compliance.md` - Liquidity runway, near-term solvency, and covenant headroom analysis.
- `references/debt-capitalization-modeling.md` - Debt schedule framing across tranches, maturities, and capital layers.
- `references/refinancing-maturity-analysis.md` - Refinancing risk framework, maturity wall construction, and alternate funding paths.
- `references/macro-rates-sensitivity.md` - Floating-rate exposure, benchmark sensitivity, and macro second-order effects.
- `references/scenario-analysis-framework.md` - Base, downside, and upside scenario construction with probabilistic extension.
- `references/distress-probability-framework.md` - Composite distress scoring and escalation thresholds.
- `references/contingent-liability-assessment.md` - Off-balance-sheet and latent liability review.
- `references/esg-scenario-integration.md` - Translating ESG findings into scenario assumptions.

### Valuation and Transaction Context
- `references/comparable-companies-analysis-trading-comps.md` - Market multiple cross-checks.
- `references/precedent-transactions-analysis-deal-comps.md` - Control-value and deal-vintage cross-checks.
- `references/dcf-and-credit-valuation.md` - Full DCF mechanics with credit-oriented WACC, equity cushion, and EV sensitivity analysis.
- `references/lbo-analysis-the-complete-lbo-model.md` - LBO framing and sponsor-return logic.
- `references/lbo-debt-schedule-modeling.md` - Debt waterfall and paydown mechanics.
- `references/accretion-dilution-analysis.md` - Transaction impact on credit quality.

### Cross-Asset and Special Cases
- `references/cre-corporate-bridge-framework.md` - Integrating material real-estate exposure into a corporate credit model.
- `skills/cre-analysis-underwriting/references/cre-pro-forma-cash-flow-modeling.md` - Property cash flow concepts when CRE is material to issuer credit.
- `references/structured-finance-cash-flow-modeling.md` - Cash-flow logic for structured or asset-backed contexts.
- `references/accounting-for-loans.md` - Loan accounting, CECL, and lender balance-sheet context.

### Tools and Worked Examples
- `references/practical-workflow-building-a-credit-summary.md` - Detailed build sequence for a lender-style credit summary with complete analysis workflow and review checklist.
- `references/checklists-practical-tools.md` - Method-specific modeling and presentation checklists.
- `references/comparable-companies-analysis-trading-comps.md` - Trading comps methodology plus football field valuation summary, method quick reference, and common analytical pitfalls.
- `skills/cre-analysis-underwriting/references/commercial-real-estate-credit-metrics.md` - CRE metric translation when property analysis intersects issuer analysis.
- `examples/worked-corporate-bb-case-study.md` - Worked example tying normalization, leverage, liquidity, and scenario analysis together.

## Output Deliverables

When asked to analyze financials, build projections, or perform valuation, produce:

1. **Source citations**: Explicitly cite every filing, management source, data provider, and benchmark used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Financial summary table**: Revenue, EBITDA, EBITDA margin, free cash flow, capex, and other core operating lines for historical and projected periods.
3. **Credit metrics table**: Gross leverage, net leverage, coverage, FCF-to-debt, liquidity, and maturity profile.
4. **EBITDA quality assessment**: Reported versus adjusted EBITDA, add-back bridge, and commentary on durability.
5. **Scenario matrix**: Base, downside, and upside with explicit assumptions and resulting leverage, coverage, and liquidity.
6. **Valuation and downside view**: Relevant comps, DCF, precedent, and LBO outputs when valuation matters to recovery, sponsor behavior, or equity cushion.
7. **Key assumptions and breakpoints**: Identify which assumptions drive the view and which thresholds would change the recommendation.

## Limitations

- EBITDA-based frameworks are weakest for pre-revenue issuers, structurally negative-EBITDA businesses, and models where maintenance capex or working capital dominates economics.
- Leverage ratios lose meaning near zero EBITDA, during extreme seasonality, or where unrestricted cash is not truly available.
- Large EBITDA add-backs require skepticism; improvement plans, synergies, and run-rate savings should not be treated as earned cash flow.
- Valuation is a cross-check, not a substitute for liquidity, covenant, and refinancing analysis.
- DCF outputs are highly sensitive to discount-rate and terminal assumptions; use them to frame value, not to force precision.
- For broader framework limitations, consult `skills/memo-generator/references/analytical-limitations.md`.

## Data Quality

- Never silently fill missing data with assumptions. Use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose gaps explicitly.
- Keep reported, adjusted, covenant, and management-case metrics separate; blending them obscures risk.
- Use root references to calibrate market-sensitive assumptions, not to override issuer-specific facts.
- When standard analytical frameworks may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.

## Examples

- `examples/worked-corporate-bb-case-study.md` - End-to-end BB-rated corporate credit example showing EBITDA normalization, leverage and coverage analysis, liquidity review, and scenario testing.
