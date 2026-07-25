---
last_updated: "2026-03-22"
---

# Risk Appetite & Limit Framework

This file combines the Risk Appetite Statement (RAS) template with the principles for designing and operating portfolio limits. The RAS translates investment strategy into quantitative limits, connecting IC decision-making to portfolio construction and mandate compliance. The limit framework defines how to structure, calibrate, and enforce those limits in practice.

> **Current parameter values:** See `references/portfolio-risk-parameters.md` for all current numeric targets, limits, and fund-type customizations. That file is updated semi-annually and includes the latest risk parameters.

---

# Part 1 — Risk Appetite Statement (RAS) Template

A configurable template for defining portfolio-level risk parameters. The RAS is the foundational governance document that translates investment strategy into quantitative limits, connecting IC decision-making to portfolio construction and mandate compliance.

---

## Template Structure

The RAS is organized into six parameter groups. Each parameter specifies a **target** (optimal allocation), a **soft limit** (triggers review), and a **hard limit** (triggers mandatory action). Customize values for the specific fund type.

---

## 1. Overall Portfolio Parameters

Defines the portfolio's return objectives and risk tolerances at the highest level: gross and net return targets, maximum drawdown, volatility targets, and risk-adjusted return floors (Sharpe ratio, information ratio).

- **Target:** The return and risk profile the PM is optimizing toward under normal conditions.
- **Soft limit:** A drawdown or volatility level that triggers PM-level review and potential position adjustments.
- **Hard limit:** A threshold (e.g., maximum drawdown) that triggers mandatory IC involvement and remediation.

**Governance link:** If drawdown exceeds the maximum threshold, the PM must present a remediation plan to IC within 5 business days. Positions may not be added until the plan is approved.

> For current numeric values, see `references/portfolio-risk-parameters.md`, Section 1.

---

## 2. Concentration Limits

Controls exposure at the single-name, sector, sub-sector, rating bucket, geography, and sponsor levels. Prevents over-concentration that could cause outsized losses from a single default or correlated event.

- **Target:** The optimal position size or allocation percentage for each dimension.
- **Soft limit:** The level at which the PM must review the position and assess whether the concentration is intentional and justified.
- **Hard limit:** The maximum beyond which an IC exception is required before the position can be maintained or increased.

> For current numeric values, see `references/portfolio-risk-parameters.md`, Section 2.

---

## 3. Instrument Limits

Sets minimum and maximum allocations by instrument type (senior secured loans, unsecured bonds, second lien, mezzanine, structured products, equity, CDS/derivatives, PIK, and covenant-lite). Ensures the portfolio maintains the desired structural seniority and risk profile.

- **Minimum:** The floor allocation to maintain sufficient exposure to core instruments (e.g., senior secured loans).
- **Maximum:** The ceiling to prevent overallocation to riskier or less liquid instrument types.

> For current numeric values, see `references/portfolio-risk-parameters.md`, Section 3.

---

## 4. Liquidity Parameters

Governs cash reserves, liquidity tiers, redemption coverage, illiquid asset limits, and bid-ask spread monitoring. Critical for any fund with redemption features or NAV-based pricing.

- **Target:** The optimal cash and liquidity reserve level to meet redemptions without forced selling.
- **Hard minimum:** The floor below which the fund cannot operate without triggering mandatory action.
- **Alert thresholds:** Bid-ask spread levels or liquidity metrics that trigger enhanced monitoring.

> For current numeric values, see `references/portfolio-risk-parameters.md`, Section 4.

---

## 5. Rating Distribution Targets

Defines the target credit quality mix across rating buckets (investment grade, BB, B, CCC, not rated) and the weighted average rating floor. Prevents unintended credit quality drift.

- **Target:** The optimal allocation to each rating bucket given the fund's strategy and return objectives.
- **Minimum/Maximum:** Bands that keep the portfolio within the intended credit quality range.
- **Weighted average rating floor:** The minimum portfolio-level rating that, if breached, triggers IC review.

> For current numeric values, see `references/portfolio-risk-parameters.md`, Section 5.

---

## 6. Duration and WAL Constraints

Controls weighted average life, spread duration, effective duration, and maturity concentration. Manages reinvestment risk, interest rate sensitivity, and maturity wall exposure.

- **Target:** The optimal duration and WAL profile for the current rate environment and fund strategy.
- **Maximum:** Ceilings that prevent excessive extension risk or maturity concentration.
- **Maturity concentration limits:** Caps on the percentage of the portfolio maturing in any single year or within a rolling 24-month window.

> For current numeric values, see `references/portfolio-risk-parameters.md`, Section 6.

---

## Fund-Type Customization

The base parameters above are calibrated for a broadly syndicated leveraged credit portfolio. Different fund structures (CLO, BDC, Open-End, SMA) require specific adjustments driven by their regulatory requirements, structural features, and investor expectations.

> For current fund-type customization tables covering CLO, BDC, Open-End Fund, and SMA adjustments, see `references/portfolio-risk-parameters.md`, Fund-Type Customization section.

---

## RAS Connection to IC Decision-Making

The RAS directly governs IC recommendations:

1. **Pre-IC Check:** Before any investment is presented to IC, the analyst must verify that the proposed position fits within RAS parameters using the mandate compliance checklist (see `references/mandate-compliance-template.md`)
2. **Soft Limit Breach:** If the trade would breach a soft limit, the IC memo must include explicit justification and a remediation timeline
3. **Hard Limit Breach:** If the trade would breach a hard limit, the trade cannot proceed without a formal IC exception — exceptions must specify: rationale, maximum duration, remediation plan, and the specific risk being accepted
4. **Ongoing Compliance:** RAS parameters are monitored continuously; passive breaches (from rating migration, NAV changes, or market moves) trigger review at the next monitoring cycle, with mandatory remediation within 30 days

---

# Part 2 — Risk Limit Framework

This section defines how to design and operate portfolio limits. It is intentionally principle-based. Current numeric settings belong in the root `references/portfolio-risk-parameters.md`, which is the shared source for live limits, sizing bands, and fund-type customizations.

## What a Good Limit Does

A useful risk limit should:

- constrain a real failure mode rather than create reporting noise
- be measurable from available data
- have a clear owner and escalation path
- distinguish monitoring thresholds from true hard stops
- trigger an action, not just a red flag on a dashboard

Bad limits are vague, duplicative, or impossible to remediate. Good limits connect directly to capital preservation, liquidity, mandate compliance, or governance.

## Core Limit Categories

### 1. Concentration Limits

Use concentration limits to prevent a single name, sector, sponsor, geography, or rating bucket from dominating portfolio outcomes.

Key principles:

- single-name limits protect against unrecoverable idiosyncratic mistakes
- sector and factor limits protect against cyclical or correlated drawdowns
- sponsor and issuer-group limits matter when documentation behavior or ownership incentives can be correlated across names
- rating-bucket limits prevent hidden risk drift from gradual migration into lower-quality exposures

Use the current thresholds from `references/portfolio-risk-parameters.md` rather than embedding them here.

### 2. Market Sensitivity Limits

Set portfolio-level limits for the risk measures that matter to the strategy, such as spread sensitivity, rate sensitivity, loss budget, or scenario loss.

Key principles:

- use CS01 when spread widening is the primary portfolio risk
- use DV01 when interest-rate exposure can obscure the intended credit view
- use drawdown and scenario-loss limits to keep model outputs tied to capital at risk
- treat VaR or expected shortfall as tools, not complete descriptions of downside

If a sensitivity metric becomes the binding constraint, the correct response is usually to reduce exposure, hedge, or change the expression of the view rather than simply approve an exception.

### 3. Liquidity Limits

Liquidity limits should reflect the fund's liability structure, expected redemption profile, financing flexibility, and the true liquidation timeline of the assets held.

Key principles:

- classify liquidity by expected exit ability under stress, not by optimistic dealer color
- separate liquid reserves, moderate-liquidity assets, and assets that would require forced-sale discounts
- size illiquid positions based on both downside conviction and exit realism
- include financing availability and redemption coverage in the framework when the vehicle has external liquidity demands

For live liquidity targets and thresholds, use `references/portfolio-risk-parameters.md`. If the position is intended for a BDC private credit vehicle, also use `skills/private-credit-middle-market/references/bdc-regulatory.md`.

### 4. Governance Limits

Some limits are governance limits rather than economic limits. These include:

- approvals required above certain size or concentration levels
- notification thresholds for soft-limit approaches
- mandatory IC review for certain amendments, exceptions, or vehicle-specific constraints
- stale-approval and condition-verification rules

Governance limits matter because the same exposure can be acceptable or unacceptable depending on who reviewed it, what changed, and whether the portfolio can still tolerate it.

## Limit Architecture

For each limit, define:

1. **Metric**: What is being measured.
2. **Threshold type**: Target, alert, soft limit, or hard limit.
3. **Data source**: Where the metric comes from.
4. **Owner**: PM, analyst, risk, IC, or compliance.
5. **Required action**: What happens if the threshold is approached or breached.
6. **Review cadence**: How often the limit should be refreshed or recalibrated.

Without this structure, "limits" become static reference points rather than operating controls.

## Breach Handling Principles

Differentiate passive breaches from active breaches:

- **Passive breach**: Market movement, migration, or NAV change pushed the portfolio through a threshold.
- **Active breach**: A new trade, add-on, or approved action created the breach.

Handle them differently:

- passive breaches require diagnosis, remediation timing, and evidence that the position still fits the portfolio
- active breaches require immediate accountability because the portfolio knowingly moved outside policy

Every breach memo should answer:

1. What limit was approached or breached?
2. Was the cause active or passive?
3. What is the remediation path?
4. By when will the portfolio return to policy?
5. Does the situation require a hedge, trim, exception, or full re-underwrite?

## Reporting Expectations

Limit reporting should show trend and consumption, not just snapshots.

Minimum reporting logic:

- current utilization versus limit
- change since prior period
- top contributors
- headroom remaining
- whether the portfolio is becoming more or less correlated
- whether current breaches are temporary, structural, or evidence of thesis drift

The most important reports are the ones that explain what the team should do next.
