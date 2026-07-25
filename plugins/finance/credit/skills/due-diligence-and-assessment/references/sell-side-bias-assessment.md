last_updated: "2026-03-22"
---

# Sell-Side Bias Assessment

Framework for identifying and adjusting for systematic biases in sell-side materials (CIMs, management presentations, and projections) during credit due diligence.

## CIM Bias Patterns

### Common Bias Categories

The Confidential Information Memorandum (CIM) is prepared by the sell-side advisor and is inherently an advocacy document. Recognize the following systematic biases:

| Bias Category | How It Manifests | What to Look For |
|---|---|---|
| Metric Cherry-Picking | Only favorable metrics highlighted; unfavorable metrics omitted or buried | Compare CIM metrics to 10-K/10-Q; identify what is NOT shown |
| Non-Standard EBITDA | Aggressive addbacks inflate adjusted EBITDA | Compare CIM adjusted EBITDA to reported; calculate addback % |
| Favorable Peer Selection | Peer group selected to make subject look favorable | Verify peers are truly comparable by size, business mix, geography |
| Optimistic Projections | Revenue/EBITDA growth exceeds historical trend without clear catalyst | Compare projected growth to historical actual growth rates |
| Risk Minimization | Risks mentioned briefly or buried in appendix; no quantification | Look for what is NOT disclosed rather than what is |
| Historical Period Selection | Only strong recent quarters shown; weak periods excluded | Request full 5-year historical data; reconstruct trends |
| Customer Concentration | Top customers listed without concentration % or revenue dependency | Calculate Herfindahl index from full customer data |

### CIM vs. Audited Financials Reconciliation

| CIM Element | Verification Source | Common Discrepancy |
|---|---|---|
| Revenue | 10-K / audited financials | CIM may use pro forma revenue including uncommenced contracts |
| EBITDA | Income statement + addback schedule | CIM addbacks may exceed audited adjustments |
| Growth Rates | Historical 10-K trend | CIM may calculate growth from trough year (flattering) |
| Margin Trends | Income statement trend | CIM may exclude low-margin periods or segments |
| Customer Metrics | Revenue by customer (if available in filings) | CIM may present gross customer count without addressing churn |
| Capex | Cash flow statement | CIM may classify growth capex as one-time, understating maintenance |

## Management Presentation Red Flags

### Presentation Quality Assessment

| Signal | What It Suggests | Severity |
|---|---|---|
| No discussion of risks or challenges | Management lacks self-awareness or is deliberately omitting | MEDIUM-HIGH |
| Projections show hockey-stick growth | Inflection point assumed without demonstrated catalyst | HIGH — demand evidence |
| EBITDA adjustments >30% of reported | Reported earnings poorly reflect cash generation | HIGH — scrutinize each addback |
| "Run-rate" based on single strong quarter | Extrapolating temporary performance | HIGH — request trailing 12-month data |
| Extensive use of "pro forma" without clearly stated basis | Obscuring actual performance | MEDIUM-HIGH |
| No bridge from historical to projected performance | Projections disconnected from demonstrated capability | MEDIUM |
| Competitor analysis showing only subject company strengths | Biased competitive assessment | MEDIUM |
| TAM/SAM analysis implying large market opportunity | Often irrelevant to near-term credit performance | LOW-MEDIUM |

### Questions to Ask Management

| Question | Purpose | Red Flag Response |
|---|---|---|
| What was the biggest operational challenge in the last 12 months? | Test candor and self-awareness | Denial that any challenges existed |
| How do actual results compare to projections made 2-3 years ago? | Track record of projection accuracy | Refuse to share or significant misses without explanation |
| Which customers have been lost in the last 24 months and why? | Customer retention quality | Claim of zero customer losses in competitive market |
| What would cause EBITDA to decline 20%? | Risk awareness | Cannot articulate realistic downside scenarios |
| How are your projections different from what you showed in the last fundraise? | Consistency of narrative | Projections change to suit the audience |

## Projection Assessment Framework

### Benchmarking Projections

| Benchmark | Projection Comparison | Interpretation |
|---|---|---|
| Company's Own History | Projected growth vs. actual multi-year track record | If the forecast requires a step-change versus history, demand specific catalysts and execution evidence |
| Industry Growth Rate | Projected growth vs. industry forecast | Projected share gains must be substantiated |
| Peer Performance | Projected margins vs. best-in-class peers | Achieving best-in-class margins requires demonstrated competitive advantage |
| Management Track Record | Prior projections vs. actual outcomes | Serial over-projectors should face higher haircuts |
| Economic Cycle | Projections assume expansion throughout | No recession modeled = incomplete analysis |

### Projection Haircut Framework

Apply analytical adjustments to sell-side projections to develop a credit base case:

| Projection Element | Base-Case Adjustment Principle | When to Lean More Conservative |
|---|---|---|
| Revenue Growth | Pull growth toward demonstrated historical run rate unless a near-term catalyst is already visible | Management has a miss history; demand softening; share gains unsupported |
| EBITDA Margin Expansion | Require evidence of mix shift, pricing power, or cost actions already underway | Margin bridge is vague; competitive pressure is rising; savings remain unimplemented |
| Capex | Stress capex above management's estimate when maintenance needs are unclear | History of overruns; visible deferred maintenance; integration or compliance spend not fully budgeted |
| Working Capital | Assume some incremental cash use where growth, seasonality, or customer mix implies it | Business is working-capital-intensive; collections have been volatile; inventory risk is elevated |
| Synergy Realization | Delay and discount synergies unless they are contract-backed or already being executed | First-time acquirer; integration complexity high; revenue synergies drive the thesis |
| Cost Savings | Credit only savings with ownership, timing, and implementation evidence | Savings depend on difficult restructuring actions, vendor renegotiation, or optimistic timeline assumptions |

### Logical Consistency Tests

| Test | What to Check | Red Flag |
|---|---|---|
| Revenue vs. Capex | Is revenue growth supported by adequate capex investment? | Revenue doubles but capex flat = unrealistic |
| Revenue vs. Headcount | Does revenue growth require proportional hiring? | Revenue +30% with flat headcount in people-dependent business |
| Revenue vs. Working Capital | Does growth require working capital investment? | No WC build modeled despite significant revenue growth |
| Margin vs. Mix | Does margin expansion assume mix shift toward higher-margin products? | Mix shift without evidence of customer demand change |
| Growth vs. Market | Does the company grow faster than its addressable market? | Implies share gains — verify competitive dynamics support this |

## EBITDA Addback Scrutiny

### Addback Assessment Framework

For each addback in the CIM or QoE report, apply the following tests:

| Test | Question | If "No" → Challenge the Addback |
|---|---|---|
| Non-Recurring | Is this truly a one-time event? | Has this "one-time" cost occurred in 2+ of last 4 years? |
| Quantifiable | Is the amount objectively measurable? | Is the estimate based on management judgment rather than invoices/contracts? |
| Supportable | Can the amount be verified by third-party data? | Does the auditor or QoE provider independently validate? |
| Achievable | Has the company demonstrated ability to realize this savings? | Has management achieved similar savings in prior periods? |
| Reasonable | Is the amount proportionate to the underlying business event? | Does the addback seem disproportionately large? |

### Common Addback Categories and Scrutiny Level

| Addback Category | Scrutiny Level | Common Issues |
|---|---|---|
| Restructuring / Severance | MEDIUM | May recur if the business is structurally declining or serially reorganized |
| Acquisition / Transaction Costs | LOW | Usually more supportable, but verify that scope is truly one-time |
| Sponsor Management Fees | LOW | Legitimate only if the cost truly disappears rather than being replaced by another sponsor charge |
| Litigation / Settlement | MEDIUM-HIGH | May signal continuing legal exposure rather than a completed event |
| Run-Rate Cost Savings | HIGH | Benefits may not be implemented or may take longer than forecast |
| Run-Rate Revenue / EBITDA | VERY HIGH | Often extrapolates incomplete periods or assumes unproven demand |
| Stock-Based Compensation | MEDIUM | Non-cash does not mean non-economic; often recurring |
| Public Company Costs | LOW-MEDIUM | Some savings are real, but some are replaced by private-company or sponsor costs |

### Addback Quality Score

Calculate the total addback as a percentage of reported EBITDA:

| Addback / Reported EBITDA | Quality Assessment | Credit Action |
|---|---|---|
| <10% | HIGH quality — minimal adjustments | Standard analysis |
| 10-20% | MODERATE quality — adjustments material but common | Scrutinize each addback; apply 80-90% realization |
| 20-30% | LOW quality — adjustments significant | Apply 70-80% realization; model pre-addback EBITDA as stress case |
| >30% | VERY LOW quality — reported earnings poorly reflect economics | Apply 60-70% realization; question whether adjusted EBITDA is meaningful |

## Advisor Incentive Assessment

### Sell-Side Advisor Fee Structure

| Fee Component | Incentive Created |
|---|---|
| Retainer | Some incentive to stay engaged, but less tied to valuation outcome |
| Success Fee | Strong incentive to close the deal and maximize headline value |
| Escalator | Direct incentive to push optimistic positioning above a target valuation |
| Fairness Opinion | Incentive to support the transaction narrative, moderated by reputational risk |

**Implication**: The CIM is an advocacy document. The advisor earns more when the deal closes at a higher price. This creates systematic upward bias in how the business is presented. Adjust for this known bias systematically.

## Independent Verification Protocol

### Authoritative Data Sources

| Data Point | Authoritative Source | Why CIM May Differ |
|---|---|---|
| Revenue | 10-K / audited financials | CIM may use pro forma or run-rate |
| EBITDA | Income statement + documented addbacks | CIM addbacks may be more aggressive |
| Customer Metrics | Customer-level data in data room | CIM may present selectively |
| Market Size | Independent industry reports (IBISWorld, Gartner, etc.) | CIM may cite favorable estimates |
| Competitive Position | SEC filings of public competitors | CIM may overstate relative position |
| Employee Metrics | ADP data, W-2 counts, HR records | CIM headcount may differ from actual |

### Verification Priorities

| Priority | Action | Purpose |
|---|---|---|
| 1 | Reconcile CIM EBITDA to audited financials line-by-line | Quantify all adjustments |
| 2 | Compare CIM projections to company's prior internal budgets | Assess projection credibility |
| 3 | Request Quality of Earnings (QoE) report from independent provider | Third-party validation of addbacks |
| 4 | Verify customer concentration from actual revenue data, not CIM summary | True concentration may differ |
| 5 | Cross-check CIM market claims with independent industry research | Validate TAM, growth rates, competitive position |

## Summary: Analytical Posture

The credit analyst's role is to convert advocacy into analysis. The CIM tells you how the sell-side wants you to see the business. Your job is to determine how the business actually performs under realistic assumptions.

**Default approach**: Start from audited financials, not the CIM. Build projections independently using historical trends and industry benchmarks. Then compare to CIM/management projections to identify where and why they differ. The gap between independent and sell-side projections is the "bias adjustment" — this should be transparently disclosed in credit analysis and the investment memo.
