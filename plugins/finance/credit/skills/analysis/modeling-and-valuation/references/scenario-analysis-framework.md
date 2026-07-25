---
last_updated: "2026-03-21"
---

## Scenario Analysis Framework

### Base Case
**Definition:** Most likely outcome assuming management guidance or consensus holds

**Characteristics:**
- Revenue growth: mgmt guidance, analyst consensus, or conservative historical growth
- Margins: reasonable normalization to historical or peer levels
- CapEx: at company guidance levels
- Assumptions: document clearly (spreadsheet tab titled "Assumptions")

### Downside Case
**Definition:** Stress scenario; but not apocalyptic

**Typical adjustments:**
- **Revenue:** -10% to -20% from base (recession, market share loss, customer churn)
- **Margins:** compress by 100-300 bps (fixed costs not reduced, pricing pressure)
- **CapEx:** maintained or reduced by only 10-20% (critical maintenance continues)
- **Working capital:** may increase (slower collections, inventory builds)

**Key question to answer:** *Does the company remain compliant with covenants? Can it service debt?*

### Upside Case
**Definition:** Outperformance scenario

**Typical adjustments:**
- **Revenue:** +5% to +15% from base (market share gains, upsell, expansion)
- **Margins:** expand by 50-150 bps (operating leverage, pricing power)
- **CapEx:** flexible growth investment or deleveraging acceleration
- **Working capital:** may decrease (better customer relationships, faster collections)

**Key question:** *What is deleveraging trajectory? When might the company refinance or return capital?*

### Calculation Outputs for Each Scenario
For each scenario, calculate and compare:
- **EBITDA** and EBITDA Margin
- **Free Cash Flow** and FCF Margin
- **Net Debt** and Net Leverage Ratio (Net Debt / EBITDA)
- **Interest Coverage** (EBITDA / Interest Expense)
- **Debt Service Coverage** (FCF / (Interest + Mandatory Amortization))
- **Liquidity** (Cash + Available Revolver Capacity)

**Comparison Table Example:**
| Metric | Downside | Base | Upside |
|---|---|---|---|
| Revenue Growth | -15% | +3% | +12% |
| EBITDA Margin | 7.5% | 10.0% | 12.0% |
| Leverage (Net Debt/EBITDA) | 4.8x | 3.8x | 2.8x |
| Interest Coverage | 2.5x | 3.8x | 5.2x |
| Liquidity | $125M | $185M | $220M |

### Probabilistic Scenario Extension

#### Beyond Base/Upside/Downside

Standard three-scenario analysis (base/upside/downside) is necessary but insufficient for institutional credit analysis. It creates false precision around three discrete outcomes when reality is a continuous distribution. This extension adds probabilistic rigor.

#### Scenario Construction Methodology

**Step 1: Define Scenario Dimensions**
Identify the 2-4 key variables that most affect credit quality:
- Revenue growth rate
- EBITDA margin
- Capex requirements
- Working capital intensity
- Interest rate environment
- Refinancing availability

**Step 2: Assign Probability Weights**

| Scenario | Description | Typical Weight | When to Adjust |
|---|---|---|---|
| **Strong upside** | Above-plan performance; M&A upside, market share gains | 10-15% | Higher if secular tailwinds confirmed |
| **Base case** | Management guidance with modest haircut (5-10% revenue, 100-200bps margin) | 40-50% | Anchor at 45% unless strong reason to shift |
| **Moderate stress** | Cyclical downturn: -10-15% revenue, -200-400bps margin | 20-25% | Higher late-cycle or for cyclical sectors |
| **Severe stress** | Recession: -20-30% revenue, -500bps+ margin, capex deferral | 10-15% | Higher for highly leveraged or single-product risk |
| **Tail risk** | Existential: key customer loss, regulatory event, fraud, technology disruption | 3-5% | Higher if specific tail risks identified |

**Probability weight calibration:**
- Weights must sum to 100%
- No single scenario should carry >50% weight (avoids false certainty)
- The severe stress weight should increase with leverage (>6x = at least 15%)
- Sector cyclicality shifts weight toward stress scenarios late in the cycle

**Step 3: Calculate Probability-Weighted Outcomes**

For each key metric, compute the expected value:

```
E[Metric] = Σ (Probability_i × Metric_i)  for all scenarios i
```

**Key metrics to probability-weight:**
- EBITDA (and resulting leverage)
- Free cash flow
- Interest coverage
- Recovery value (enterprise value in each scenario)
- Loss given default (1 - recovery rate)

**Step 4: Expected Loss Calculation**

```
Expected Loss = Probability of Default × Loss Given Default × Exposure at Default

Where:
- P(Default) = sum of probabilities for scenarios where leverage exceeds sustainable threshold
              or liquidity is exhausted or covenant breach triggers acceleration
- LGD = (1 - Recovery Rate) in the default scenario
- EAD = par value of position + unfunded commitments likely to be drawn
```

**Example:**
| Scenario | Probability | Leverage | Default? | Recovery | Loss |
|---|---|---|---|---|---|
| Strong upside | 12% | 3.5x | No | N/A | 0% |
| Base | 45% | 4.8x | No | N/A | 0% |
| Moderate stress | 23% | 6.5x | No | N/A | 0% |
| Severe stress | 15% | 8.2x | Yes | 65% | 35% |
| Tail risk | 5% | N/M | Yes | 30% | 70% |

Expected Loss = (15% × 35%) + (5% × 70%) = 5.25% + 3.50% = **8.75%**

**Step 5: Sensitivity Analysis**

Test how probability weights affect the expected loss:
- What if the severe stress probability is 20% instead of 15%?
- What if recovery in severe stress is 50% instead of 65%?
- What is the break-even spread (the spread that exactly compensates for expected loss + required return)?

**Break-even spread formula:**
```
Required Spread = Expected Loss + Risk Premium + Funding Cost + Operating Cost
                = 8.75% + 2.00% + 0.50% + 0.25% = 11.50% (≈ 1,150bps)
```

If the offered spread is below the break-even, the deal does not compensate for the risk.

#### When Standard Scenarios Mislead

| Situation | Why 3-Scenario Fails | Better Approach |
|---|---|---|
| Bimodal outcomes (e.g., FDA approval) | Base case averages two very different worlds | Model each outcome separately with binary probability |
| Fat-tailed risk (e.g., litigation, fraud) | Severe stress is too mild; tail risk too unlikely | Increase tail risk weight; model specific tail scenarios |
| High correlation with macro | Scenarios may understate severity of synchronized downturn | Use conditional scenarios (e.g., "if recession, then also rate spike + spread widening") |
| Leverage >6x | Small EBITDA changes cause large leverage swings | Model continuous EBITDA distribution; compute P(leverage > Xx) for multiple thresholds |
| Asset-light business | EBITDA-based leverage is misleading | Model FCF directly; use FCF-to-debt service coverage as primary metric |

#### Integration with Other Frameworks

- **Covenant analysis**: For each scenario, compute covenant headroom — probability-weight the expected covenant breach
- **Recovery analysis**: Model recovery at different enterprise values (one per scenario) — probability-weight the expected recovery
- **Position sizing**: Use expected loss to inform maximum position size — position size × expected loss should not exceed loss tolerance
- **Relative value**: Compare expected loss-adjusted spread across investment alternatives

---
