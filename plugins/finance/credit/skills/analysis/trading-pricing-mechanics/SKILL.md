---
name: Trading Pricing Mechanics
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  This skill applies when evaluating how a loan or bond should trade, how to compare spread and yield across instruments, or how trade mechanics and documentation affect execution, settlement, and realized return.
category: markets
related_skills:
  - memo-generator
  - modeling-and-valuation
  - debt-structure-covenants
  - portfolio-investment-process
  - securitization-and-clos
triggers:
  - OAS
  - Z-spread
  - asset swap spread
  - assignment agreement
  - basis trade
  - bond pricing
  - callable bond analysis
  - carry analysis
  - comp table
  - credit curve
  - delayed compensation
  - distressed trading
  - duration
  - floating-rate pricing
  - loan settlement
  - loan trading
  - mark to market
  - new issue concession
  - participation agreement
  - relative value
  - secondary loan market
  - spread analysis
  - trade confirmation
  - yield calculations
disambiguation: |
  Prefer this skill when the context involves loan/bond pricing, spread levels, secondary trading, or relative value comparison.
  For CRE cap rates as property valuation, use cre-analysis-underwriting.
  For CLO tranche pricing and new issue spreads, use securitization-and-clos.
---

# Trading & Pricing Mechanics

Trading and pricing work is about translating instrument structure into comparable economics. Start by identifying the instrument and settlement conventions, normalize price and spread into the right measure for that instrument, then judge relative value only after adjusting for seniority, optionality, duration, liquidity, and execution friction.

## Core Workflow

1. **Classify the instrument correctly**: Loan vs. bond, fixed vs. floating, performing vs. distressed, secured vs. unsecured, callable vs. non-callable.
2. **Translate quoted terms into comparable economics**: Price, accrued interest, yield, spread, discount margin, duration, convexity, and settlement adjustments should reconcile to the actual cash economics.
3. **Normalize for structure before judging value**: Seniority, collateral, optionality, liquidity, tenor, and rate format can make two equal-looking spreads economically very different.
4. **Separate market level from issuer view**: Distinguish beta moves, technicals, and benchmark shifts from issuer-specific deterioration or improvement.
5. **Incorporate execution reality**: Documentation route, consent mechanics, settlement timing, delayed compensation, and position-building friction all affect realized return.
6. **Frame upside and downside explicitly**: Carry, pull-to-par, roll-down, spread tightening, spread widening, and default/loss outcomes should all be visible in the return discussion.
7. **Express the conclusion in investor terms**: State whether the instrument is rich, fair, or cheap, why, what could close the gap, and what could invalidate the view.

## Reference Map

Read the most relevant reference for the question rather than loading the full library. Skill-local references should stay focused on durable analytical principles; current market levels and live conventions belong in root references.

### Pricing Mathematics
- `references/core-pricing-accrued-interest.md` - Clean vs. dirty price, accrued interest, and invoice amount.
- `references/yield-calculations.md` - YTM, YTC, YTW, and the logic for choosing the relevant yield.
- `references/floating-rate-pricing.md` - Discount margin, floor behavior, and reference-rate fallback issues.
- `references/call-schedule-analysis.md` - Call structure, clawbacks, and make-whole framing.
- `references/advanced-duration-return-analytics.md` - Duration, convexity, carry, roll-down, and scenario return framing.
- `references/duration-price-sensitivity.md` - Duration formulas, price sensitivity, convexity, and quick estimation rules of thumb.
- `references/practical-calculation-workflows.md` - Worked calculation sequences for common pricing tasks.
- `references/common-pitfalls-and-checklists.md` - Frequent analytical mistakes, adjustments, and bond analysis checklist.

### Relative Value and Comparables
- `references/relative-value-analysis-for-credit.md` - Spread hierarchy (nominal, STW, Z-spread, OAS, ASW), tight/wide framing, curve work, and cross-market comparison logic.
- `references/comp-table-output-guide.md` - Comparable set construction and standard output format for comp tables and basis analyses.
- `references/quick-refinancing-check-framework.md` - Simple refinancing economics and repricing pressure checks.

### Trading Mechanics and Documentation
- `references/the-assignment-agreement-rights-consents-and-mechanics.md` - Assignment path, consent logic, and lender-of-record implications.
- `references/participation-agreements-rights-limitations-and-use-cases.md` - Participation structure, limitations, and fallback use cases.
- `references/distressed-trading-mechanics.md` - Flat trading, true-up, breakage, and distressed-specific mechanics.
- `references/delayed-compensation-economic-adjustment-for-timing.md` - Economic transfer vs. settlement timing adjustments.
- `references/trade-execution-workflow.md` - Pre-trade controls, par trading logic, settlement workflow, trade documentation checklist, and post-settlement checks.

### Instrument Context
- `references/loan-market-pricing-and-analytics.md` - Secondary loan market structure, fair-value and dealer-mark framing, and core loan-market metrics.
- `references/loans-are-not-securities-the-regulatory-framework.md` - Why syndicated loans trade under a different legal and regulatory regime than securities.
- `references/deferred-payment-structures.md` - Zero-coupon, PIK, and toggle-style cash flow structures.

## Output Deliverables

When asked to analyze pricing, trading mechanics, or relative value, produce:

1. **Source citations**: Explicitly cite every market input, pricing source, and qualitative fact used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Instrument snapshot**: Security type, seniority, rate format, callability, maturity, settlement route, and any structural features that matter to pricing.
3. **Pricing bridge**: Clean price, dirty price, accrued interest, yield, spread, duration, convexity, and the specific metric used to judge value.
4. **Comparable or basis analysis**: Peer set, cohort median, target vs. cohort differential, and any structural adjustments needed to normalize the comparison.
5. **Return framing**: Carry, pull-to-par, roll-down, spread move sensitivity, and stressed downside including loss or recovery assumptions when relevant.
6. **Execution considerations**: Documentation route, consent requirements, settlement friction, liquidity, and any delayed-compensation or true-up risk.
7. **Recommendation and catalyst view**: Rich/fair/cheap assessment, what could close the gap, and what would prove the view wrong.

## Limitations

- Relative value is only as good as the normalization. Raw spread comparisons across different structures, tenors, or rate formats are frequently misleading.
- Dealer marks and screened prices can lag fundamental deterioration, especially in loans, private markets, and thinly traded issues.
- Optionality and floors can make headline yield or spread look attractive while hiding call risk, negative convexity, or fixed-rate behavior.
- Execution friction matters. A trade that looks optically cheap may not be economically attractive once liquidity, settlement delay, or documentation complexity are included.
- Current market conventions can change. Use root references for live settlement norms, benchmark spreads, and reference-rate levels rather than treating historical examples as permanent.

## Data Quality

- Never silently fill missing market, documentation, or structural data with assumptions. Use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose gaps explicitly.
- Separate live market inputs from timeless analytical logic. Pull current spreads, rates, and trading conventions from root references and keep local references focused on enduring principles.
- When comparing across instruments or asset classes, state the normalization choice explicitly: spread basis, duration basis, recovery basis, or liquidity basis.
- When standard analytical frameworks may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and disclose the limitation directly.

## Examples
- `examples/worked-corporate-bb-case-study.md`: Comparable spread analysis, target vs. cohort framing, warranted spread adjustment, and recommendation.
