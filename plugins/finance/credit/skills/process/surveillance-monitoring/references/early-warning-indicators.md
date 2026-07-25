---
last_updated: "2026-03-22"
---

# Early Warning Indicator System

Early warning indicators are useful only when they are tied back to the original thesis and interpreted in context. The goal is not to react mechanically to every data point, but to identify whether a credit is drifting away from the assumptions that justified the investment.

> For current numeric thresholds, response windows, and operating cadence, use `references/escalation-trigger-thresholds.md` and `references/data-pipeline-specification.md` at the project root.

## Core Principles

- Early warning signals matter most when they cluster across multiple dimensions rather than appearing in isolation.
- Direction and velocity matter as much as level; rapid deterioration is usually more important than a weak but stable metric.
- Denominator-driven deterioration is often more concerning than changes caused by a deliberate, value-accretive use of debt.
- Market signals can lead fundamentals, but they can also be noisy; always separate idiosyncratic pressure from market-wide moves.
- Qualitative developments matter most when they impair reporting credibility, access to capital, management stability, or sponsor alignment.

## Status Logic

### Green
- The credit is performing broadly in line with the underwriting case.
- Variances are explainable and do not materially impair the thesis.
- No escalation is required beyond routine surveillance.

### Yellow
- The first meaningful signs of thesis drift are visible.
- The credit remains fundamentally financeable, but the analyst should increase attention and refresh assumptions.
- The right action is usually enhanced monitoring rather than immediate position change.

### Orange
- Multiple indicators point to meaningful thesis pressure, or one severe indicator suggests the downside case is starting to dominate.
- At this stage, surveillance should move from observation to action evaluation: update the model, reassess recovery downside, and frame likely portfolio responses.

### Red
- The credit is approaching or has entered a state where default, restructuring, forced action, or emergency governance review becomes realistic.
- Monitoring becomes event-driven and decision-oriented rather than routine.

## Indicator Families

### Financial Signals

Watch for deterioration in:
- EBITDA, revenue, and margins relative to the underwriting case
- leverage, especially when driven by weaker earnings rather than purposeful debt-funded growth
- free cash flow conversion and working-capital consumption
- liquidity runway, revolver reliance, and near-term funding demands
- interest or fixed-charge coverage and the ability to absorb additional pressure

Interpretation guidance:
- A modest miss in a cyclical business may be less meaningful than the same miss in a stable recurring-revenue business.
- A weak quarter matters less than a pattern of repeated underperformance.
- A company that still has cash today may already be in trouble if its burn rate, maturities, or covenant path are worsening quickly.

### Market Signals

Watch for:
- secondary price weakness
- spread widening
- CDS deterioration where available
- dealer quote dispersion
- peer-group underperformance that is either issuer-specific or part of a sector-wide stress pattern

Interpretation guidance:
- Technical widening without fundamental change should not be treated the same as issuer-specific underperformance.
- Price and spread moves are more powerful when confirmed by earnings misses, weak liquidity, or ratings pressure.
- A market move that is worse than peers often deserves investigation even before internal metrics breach formal thresholds.

### Qualitative Signals

Watch for:
- unplanned CEO or CFO turnover
- auditor changes, delayed filings, or control weaknesses
- management credibility erosion
- sponsor behavior that prioritizes value extraction over balance-sheet support
- litigation, regulation, customer loss, or supplier disruption that could alter the thesis

Interpretation guidance:
- Reporting quality problems often precede financial transparency problems.
- Multiple leadership changes in a short period are more important than a single orderly succession.
- A sponsor's willingness or unwillingness to support the borrower can change the practical downside more than the reported quarter alone.

### Structural Signals

Watch for:
- covenant cushion erosion
- amendment or waiver requests
- maturity walls without a credible refinancing path
- incremental debt raised on more punitive terms
- asset transfers, dropdown risk, or LME precursor behavior

Interpretation guidance:
- A covenant amendment requested before a formal breach can still be a serious signal if it reflects deteriorating economics rather than ordinary flexibility.
- Refinancing risk should be assessed against market access, lender appetite, and free-cash-flow trajectory, not maturity date alone.
- Structural deterioration can be thesis-breaking even when reported earnings have not yet fully collapsed.

## Asset-Class-Specific Signals

### Corporate Credit
- EBITDA trajectory versus model
- covenant cushion and leverage path
- liquidity access and refinancing risk
- sponsor or management behavior

### Private Credit
- maintenance covenant performance
- information-rights quality and reporting timeliness
- sponsor support, amendment cadence, and fair value drift
- rising PIK dependence or repeated equity cures

### CRE
- occupancy, collections, and NOI trend
- tenant rollover and major tenant concentration
- DSCR, reserve adequacy, and refinanceability
- property-level market pressure such as cap-rate expansion or weakening submarket demand

### Structured Finance
- collateral quality migration
- trigger-test cushion and structural protections
- servicer or manager performance
- pool delinquency, defaults, extension risk, or special servicing trends

## Using Early Warning Indicators Well

- Tie each signal back to a specific thesis pillar or thesis-kill trigger.
- Escalate faster when signals cluster across fundamentals, market data, and qualitative developments.
- Avoid false comfort from a single green metric when several other dimensions are deteriorating.
- Avoid false alarms from a single noisy market print when operating performance remains intact.
- Always convert a warning signal into an action question: what changed, what could happen next, and what decision might follow?
