---
last_updated: "2026-03-22"
update_cadence: semi-annually
next_review: "2026-09-22"
data_vintage: "Q1 2026"
sources:
  - "Internal credit surveillance frameworks"
  - "LSTA market practice guidelines"
  - "Rating agency monitoring methodologies (S&P, Moody's, Fitch)"
  - "Bloomberg terminal data feeds"
  - "LCD/PitchBook leveraged loan data"
---

# Data Pipeline Specification

**Last Updated:** March 2026
**Update Cadence:** Semi-Annually
**Next Review:** September 2026

This file now contains the current monitoring parameters, cadence targets, escalation cutoffs, and tolerance bands used by the surveillance process. For sourcing logic, calculation methodology, lineage standards, stale-data handling method, and quality-control process guidance, see `skills/surveillance-monitoring/references/data-pipeline-methodology.md`.

---

## 1. Monitoring Parameter Matrix

See `references/escalation-trigger-thresholds.md` for current threshold values by tier.

| Metric | Standard Cadence | Heightened / Watchlist Cadence | Distressed / Severe Cadence |
|---|---|---|---|
| EBITDA variance vs. model | Quarterly, within 5 business days of earnings release or compliance certificate | Quarterly with interim monthly management updates where available | Monthly with real-time news monitoring support |
| Covenant headroom | Quarterly, aligned with compliance certificate delivery | Quarterly with pro forma monthly estimates where management data is available | Monthly pro forma calculations |
| Liquidity runway | Quarterly | Monthly | Weekly or bi-weekly where information rights permit |
| CDS spread / loan price | Daily for liquid positions; weekly dealer marks or monthly NAV for illiquid positions | Daily regardless of liquidity | Daily regardless of liquidity |
| Rating changes | Real-time alerts plus quarterly review | Real-time alerts plus quarterly review | Real-time alerts plus quarterly review |

---

## 2. Escalation Response Parameters

See `references/escalation-trigger-thresholds.md` for current threshold values by tier.

The tables below define the required actions at each escalation tier. Match the tier using the thresholds in the authoritative source above.

### EBITDA Variance

| Escalation Tier | Required Action |
|---|---|
| Tier 1 (Heightened Monitoring) | Add to watchlist, increase monitoring frequency, update model with actuals |
| Tier 2 (Active Review) | Prepare updated credit analysis, notify PM, assess covenant cushion impact |
| Tier 3 (IC Notification) | Invoke events-distressed for recovery analysis, prepare IC memo, assess portfolio concentration impact |

### Covenant Headroom

| Escalation Tier | Required Action |
|---|---|
| Tier 1 (Heightened Monitoring) | Flag in surveillance report, model forward covenant trajectory under base and stress |
| Tier 2 (Active Review) | Prepare covenant waiver/amendment analysis, assess cure right availability, notify PM |
| Tier 3 (IC Notification) | Invoke events-distressed, assess remedies (cure, waiver, forbearance), prepare IC briefing |

### Liquidity Runway

| Escalation Tier | Required Action |
|---|---|
| Tier 1 (Heightened Monitoring) | Model forward liquidity under base and stress, identify refinancing options |
| Tier 2 (Active Review) | Prepare detailed liquidity analysis, assess refinancing feasibility, notify PM and IC |
| Tier 3 (IC Notification) | Invoke events-distressed, prepare recovery analysis, assess DIP financing scenarios |

### CDS Spread / Loan Price

| Escalation Tier | Required Action |
|---|---|
| Tier 1 (Heightened Monitoring) | Review for fundamental catalyst, check news flow, add to watchlist if not already |
| Tier 2 (Active Review) | Prepare updated credit analysis, reassess fair value, evaluate hedging |
| Tier 3 (IC Notification) | Full credit review, invoke events-distressed if warranted, assess portfolio impact |

### Rating Changes

| Escalation Tier | Required Action |
|---|---|
| Tier 1 (Heightened Monitoring) | Review rating rationale, assess if thesis intact, model downgrade scenario |
| Tier 2 (Active Review) | Update credit analysis, reassess relative value, check fund mandate compliance |
| Tier 3 (IC Notification) | Full IC review, invoke events-distressed, assess forced selling risk |

---

## 3. Stale-Data Adjustment Parameters

| Parameter | Current Setting |
|---|---|
| Approaching stale window | Within 30 days of `next_review` |
| Spread and pricing confidence band when stale | +/-20% |
| Default and recovery confidence band when stale | +/-10% |
| Materially stale trigger | `next_review` + 90 days |

### Application Rules
- **Spread and pricing data:** Apply +/-20% confidence band around stale figures
- **Default and recovery rates:** Apply +/-10% confidence band
- **Deal parameters and conventions:** Flag but do not adjust unless market regime change is known
- **Rating thresholds:** Do not adjust unless methodology change is announced

---

## 4. Quality-Control Tolerance Bands

| Checkpoint | Frequency | Tolerance / Control |
|---|---|---|
| Financial statement spreading | Every quarterly update | Dual-analyst review for Top 20 exposures; single analyst with checklist for remainder |
| Covenant compliance | Every compliance certificate | Variance >2% between certificate and independent calculation triggers review |
| Market pricing | Daily | Variance >2 points between dealer marks and composite pricing triggers dealer inquiry |
| Recovery estimates | Quarterly or upon material event | Benchmark against rating agency LGD estimates and historical recovery comps |
| Portfolio risk metrics | Monthly | Reconcile position-level data to accounting and custody records |

### Verification Controls
- Material metrics that could trigger escalation require verification from at least two independent sources before escalation
- Rating actions from a single agency remain sufficient for escalation because the agency is the authoritative source
- When sources conflict, use the more conservative figure for risk purposes and document the discrepancy
