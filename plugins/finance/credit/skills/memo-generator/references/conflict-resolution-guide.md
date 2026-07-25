---
last_updated: "2026-03-21"
---

# Conflict Resolution Guide

When assembling an IC memo, analytical signals from different domains frequently point in opposing directions. This is normal — credit analysis rarely produces unanimous evidence. The analyst's job is not to resolve every conflict into false consensus, but to frame the tensions explicitly, weight them appropriately, and explain how the recommendation accounts for them.

---

## Common Conflict Patterns

### Fundamentals vs. Market Pricing

| Fundamental Signal | Market Signal | Typical Cause | Resolution Approach |
|---|---|---|---|
| Improving EBITDA and deleveraging | Spreads widening vs. peers | Market pricing in sector risk, upcoming maturity, or technical selling pressure | Assess whether market concern is well-founded. If fundamental improvement is verifiable, this may represent a relative value opportunity. If widening reflects informed flow, investigate further before dismissing. |
| Deteriorating FCF and rising leverage | Spreads stable or tightening | Strong sponsorship, expected M&A support, or index/ETF technical demand | Market complacency risk. The memo must flag the disconnect and assess the durability of the technical bid supporting current levels. |
| Stable credit metrics | CDS widening or loan price decline | Potential private information leak, sector contagion, or liquidity-driven selling | Investigate whether the market knows something fundamentals do not yet reflect. Check for pending litigation, regulatory action, or management turnover rumors. |

**Default hierarchy**: Fundamentals drive the credit thesis; market pricing drives execution timing and sizing. A credit with strong fundamentals but adverse market technicals may warrant a buy recommendation with patient entry parameters. A credit with weak fundamentals but tight spreads warrants caution — the market is unlikely to provide a cushion when fundamentals deteriorate further.

### Strong Financials vs. Weak Covenants

This pattern arises frequently in sponsor-backed credits where EBITDA is growing but the credit agreement permits aggressive add-backs, unlimited restricted payments, or uncapped incremental debt capacity.

- **Frame the tension explicitly**: "Current leverage of 4.2x is within our comfort zone; however, the credit agreement permits up to 2.0x of EBITDA add-backs and $500M of incremental first lien capacity, which could erode credit quality without lender consent."
- **Quantify the gap**: Calculate leverage under both reported and add-back-adjusted EBITDA. If reported leverage is 4.2x but adjusted leverage is 5.4x, state both figures.
- **Assess behavioral likelihood**: A well-capitalized sponsor with a track record of conservative capital allocation may not exploit aggressive documentation. A serial acquirer with a history of leveraging transactions likely will.
- **Weight by mandate**: Investment grade mandates should give heavier weight to structural protections. High yield mandates may accept weaker documentation if compensated by spread and fundamental quality.

### Attractive Spread vs. Deteriorating Sector

- **Time horizon matters**: A 75bps spread premium over comparable BB credits may not compensate for a sector entering cyclical decline if the hold period is two to three years. For a three-to-six-month trading position, the same premium may offer sufficient carry.
- **Quantify the downside**: Model a sector-specific stress case. If a 20% EBITDA decline (consistent with historical sector troughs) pushes leverage from 4.5x to 6.5x and breaches the 6.0x maintenance covenant, the spread premium is insufficient.
- **Isolate company-specific factors**: Determine whether the issuer is better or worse positioned than peers within the deteriorating sector. Market share gains, lower cost position, or superior contract structures may provide insulation.

---

## Multi-Instrument Issuers: Competing Claims

When the issuer has multiple instruments outstanding (1L Term Loan, 2L Notes, Senior Unsecured), the memo must address the capital structure holistically even when recommending a single tranche.

### Intra-Capital-Structure Conflict

| Scenario | Impact | How to Frame |
|---|---|---|
| 1L tight, 2L wide | Market pricing in recovery risk for subordinated debt; 1L recovery seen as money-good | State the implied enterprise value and recovery rate the market is assigning to each tranche. Assess whether the 2L spread adequately compensates for subordination risk. |
| All tranches tight | Market complacency or strong fundamental support | If fundamentals justify tightness, no conflict. If leverage is elevated (>5.0x) and all tranches trade inside historical medians, flag the risk of a broad repricing. |
| 1L wide relative to 2L (compressed basis) | Unusual — may reflect liquidity premium, CLO demand dynamics, or structural subordination concerns | Investigate the cause. Compressed 1L/2L basis often signals a market expecting par recovery for the entire capital structure (strong credit) or systemic mispricing. |

### Presenting Multi-Tranche Analysis

- Always present the full capital structure waterfall regardless of which tranche is recommended
- Calculate the recovery breakpoint: the enterprise value at which the recommended tranche begins to take losses
- State the implied EV/EBITDA multiple at the recovery breakpoint (e.g., "Recovery on the 2L notes falls below 50% if enterprise value drops below 5.0x LTM EBITDA, compared to a 15-year sector trough multiple of 5.5x")
- Compare the spread differential between tranches to the incremental recovery risk assumed

---

## Worked Example: Improving EBITDA with Covenant Erosion

**Issuer**: MidCo Manufacturing, BB-rated, $1.2B 1L Term Loan + $400M Senior Unsecured Notes

**Positive signals**: LTM EBITDA grew 12% YoY from $280M to $314M. Leverage declined from 5.1x to 4.6x. Management guides to further deleveraging via organic growth and $50M annual mandatory amortization.

**Negative signals**: The recent amendment (Q2 2025) loosened the credit agreement. Maintenance leverage covenant moved from 5.5x to 6.5x. EBITDA add-back definitions were expanded to include "expected synergies from future acquisitions" (uncapped). A new $200M uncommitted incremental first lien basket was added.

**How to frame in the memo**:

> **Financial trajectory is positive, but structural protections have weakened.** LTM EBITDA growth of 12% has driven leverage to 4.6x from 5.1x, and the deleveraging path toward 4.0x by YE2027 is credible given contracted revenue visibility and mandatory amortization. However, the Q2 2025 amendment materially weakened the covenant package: the leverage maintenance test now sits at 6.5x (1.9x of headroom vs. 0.4x pre-amendment), and expanded add-back definitions could mask future deterioration. The incremental capacity of $200M could re-lever the credit by approximately 0.6x if fully drawn. The recommendation reflects the fundamental improvement but sizes the position conservatively to account for reduced structural protection.

**Key elements in this framing**:
- Both signals acknowledged with specifics — no suppression of negative data
- Quantified impact of covenant loosening (headroom change, incremental capacity in leverage terms)
- Recommendation explicitly adjusted for the conflict (conservative sizing)
- Forward-looking assessment of when covenant looseness could become problematic

---

## Resolution Framework

### Weight by Time Horizon

| Signal Conflict | Short-Term (< 6 months) | Medium-Term (6-18 months) | Long-Term (> 18 months) |
|---|---|---|---|
| Strong fundamentals / weak technicals | Wait for entry point; technicals resolve faster | Fundamentals dominate; use weak technicals for entry | Fundamentals decisive |
| Weak fundamentals / strong technicals | Tradeable but risky; tight stop-loss required | Avoid — fundamentals will reassert | Avoid |
| Good credit / bad documentation | Acceptable if spread compensates | Monitor for behavioral change | Higher risk — covenants constrain future optionality |
| Attractive spread / sector headwinds | Trade with hedged exposure | Assess company-specific resilience vs. sector beta | Sector risk dominates unless issuer has structural advantages |

### Weight by Mandate

| Mandate Type | Priority Hierarchy |
|---|---|
| Investment Grade | 1. Structural protections 2. Fundamental quality 3. Spread/relative value |
| High Yield | 1. Fundamental trajectory 2. Relative value 3. Structural protections |
| Distressed / Special Situations | 1. Recovery value 2. Catalyst timeline 3. Liquidity/technicals |
| CLO / Structured Vehicle | 1. Spread carry vs. default probability 2. Recovery assumptions 3. Portfolio diversification impact |

### Weight by Data Quality

When conflicts exist between high-quality and low-quality data sources, the higher-quality source takes precedence:

1. **Audited financials** over management projections
2. **Observable market prices** over model-derived fair values
3. **Contractual terms** (credit agreement, indenture) over behavioral assumptions
4. **Verified comparable transactions** over theoretical benchmarks
5. **Rating agency public reports** over unnamed market commentary

When both conflicting signals rest on equally reliable data, the memo must present both perspectives without artificially resolving the tension. State the conflict, quantify the range of outcomes, and let the conviction level and position sizing reflect the unresolved uncertainty.
