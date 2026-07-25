---
name: Portfolio Investment Process
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  This skill applies when deciding how a credit idea fits into a portfolio after underwriting: position sizing, mandate compliance, cross-asset relative value, hedging, portfolio construction, stress testing, and IC governance. Use it when the question is no longer "is this credit good?" but "how should it be owned, sized, constrained, compared, and monitored in the portfolio?"
category: portfolio-management
related_skills:
  - credit-committee
  - events-distressed
  - memo-generator
  - modeling-and-valuation
  - surveillance-monitoring
  - debt-structure-covenants
  - industry-sector-analysis
  - trading-pricing-mechanics
triggers:
  - allocation decision
  - capital allocation
  - CLO position sizing
  - concentration risk
  - correlation risk
  - credit committee
  - credit hedging
  - credit portfolio construction
  - credit risk budgeting
  - credit risk metrics
  - cross-asset relative value
  - fund mandate compliance
  - hedging strategy
  - IC governance
  - liquidity risk
  - mandate compliance
  - new issue analysis
  - portfolio construction
  - portfolio review
  - position sizing
  - risk appetite
  - relative value analysis
  - risk limits
  - stress testing credit
  - surveillance handoff
disambiguation: |
  Prefer this skill when the user is allocating capital, setting exposure, checking limits, comparing portfolio expressions, or deciding what governance and monitoring a position requires after underwriting.
  For issuer-level underwriting, use the domain skill first.
  For ongoing monitoring after trade date, hand off to `surveillance-monitoring`.
---

# Portfolio Investment Process

Portfolio construction is where a good credit idea becomes a portfolio decision: size the exposure against downside, liquidity, correlation, vehicle constraints, and alternative uses of capital rather than treating underwriting conviction alone as the answer.

## Core Workflow

1. **Start with the portfolio context**: Identify the target vehicle, available risk budget, current concentrations, liquidity profile, and any hard mandate constraints before discussing sizing.
2. **Translate underwriting into portfolio downside**: Convert the credit view into position-level loss, stress behavior, recovery uncertainty, and what could force an early exit.
3. **Size against the binding constraint**: Let conviction, liquidity, correlation, and hard limits compete; the smallest permissible size should win.
4. **Check mandate and structure explicitly**: Vehicle constraints, concentration rules, instrument eligibility, and governance requirements are hard gates, not memo footnotes.
5. **Compare alternative expressions of the view**: Test whether the best expression is this specific bond, loan, hedge, structure, or even a different asset class.
6. **Document the decision and monitoring handoff**: State the action, sizing rationale, breached or near-breached limits, required conditions, and the few triggers that would change the recommendation.

## Reference Map

Read the most relevant local reference for the question rather than loading the full library.

### Core Portfolio Construction
- `references/credit-portfolio-construction-risk-management.md` - Timeless portfolio construction principles, sizing logic, diversification lenses, portfolio review discipline, and liquidity risk management (tiering, stress testing, liquidity management tools).
- `references/risk-appetite-and-limit-framework.md` - Risk appetite statement template and limit design principles: how to turn strategy into formal portfolio limits, organize breach handling, and connect governance to IC decision-making.
- `references/hedging-strategies.md` - Hedge-selection framework across single-name, index, rates, and basis trades.
- `references/investment-traps-to-avoid.md` - Common portfolio-level judgment errors and how to avoid them.
- `references/structured-finance-risk-considerations.md` - Portfolio-specific risk lenses for structured products and project-style exposures.

### Analytical Methodologies
- `references/fund-mandate-compliance.md` - Vehicle-specific compliance logic for CLOs, BDCs, open-end funds, and SMAs.
- `references/stress-testing-scenario-analysis.md` - Timeless stress-design process and how to translate scenarios into portfolio decisions.
- `references/cross-asset-relative-value-framework.md` - Cross-asset normalization and comparable analysis framework; use root benchmarks for current inputs.
- `references/correlation-adjusted-position-sizing.md` - Factor overlap, contagion channels, hidden concentration risk, and sizing adjustments.
- `references/new-issuance-analysis.md` - New-issue diligence and pricing framework.
- `references/the-investment-decision-process.md` - Full investment decision workflow from context to action.
- `references/ic-governance-framework.md` - IC process, dissent handling, conditions, escalation, portfolio-level governance, and subsequent action governance (Section 10) for position increases, refinancings, amendments, and other post-approval actions.

### Supporting Workflow References
- `references/preparing-a-credit-snapshot.md` - Fast first-pass triage before deeper portfolio work.
- `references/equity-analysis-for-debt-investors.md` - Equity-cushion framing and when equity signals matter to debt sizing or risk.

### Tools and Examples
- `references/credit-risk-metrics.md` - Definitions and formulas for core portfolio risk metrics.
- `references/mandate-compliance-template.md` - Fill-in template for documenting pre-trade mandate checks.
- `references/bdc-position-sizing-calculator.md` - BDC-specific capacity checks that bind before discretionary sizing.
- `examples/worked-position-sizing-example.md` - End-to-end example combining mandate checks, correlation adjustment, stress testing, and final sizing.

## Output Deliverables

When asked to size, compare, or approve an investment for a portfolio, produce:

1. **Source citations**: Explicitly cite every market input, structural fact, policy limit, and regulatory constraint used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Portfolio context**: Target vehicle, current relevant concentrations, liquidity profile, and the specific limits that matter to this decision.
3. **Sizing recommendation**: Recommended notional and percentage of portfolio, plus the binding constraint and why larger size would be unjustified.
4. **Limit consumption and mandate check**: Post-trade single-name, sector, rating, liquidity, and vehicle compliance view with pass/fail logic.
5. **Stress and downside view**: Position-level and portfolio-level stress effect using current calibration from `references/stress-scenario-framework.md`.
6. **Relative value and expression choice**: Why this asset, tranche, hedge, or asset class is the best expression of the view versus alternatives considered.
7. **Decision and conditions**: Buy, sell, hold, increase, reduce, hedge, or decline; include any IC conditions, execution parameters, or required follow-up.
8. **Monitoring handoff**: A short list of thesis-kill triggers or review points for `surveillance-monitoring`.

## Limitations

- Portfolio limits improve discipline but do not eliminate correlated tail risk.
- Position sizing frameworks can understate exit risk when liquidity disappears faster than expected.
- Relative value analysis is only as good as the comparables, structural adjustments, and loss assumptions behind it.
- Governance frameworks create consistency but do not replace judgment when the facts change quickly.

## Data Quality

- Use local references for methodology and root references for mutable inputs. Do not restate current limits, market spreads, or stress sizes from memory.
- Never silently fill missing data with assumptions. If information is incomplete, use `skills/memo-generator/references/incomplete-data-guidance.md` and state the gap explicitly.
- Keep underwriting facts, current portfolio state, and stress assumptions separate; blending them hides the true driver of the sizing decision.
- When a standard framework may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and disclose the limitation directly.

## Examples

- `examples/worked-position-sizing-example.md`: Position sizing workflow for a CLO investment decision showing mandate checks, concentration review, correlation adjustment, stress testing, and monitoring handoff.
