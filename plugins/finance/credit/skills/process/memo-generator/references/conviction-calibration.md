---
last_updated: "2026-03-21"
---

# Conviction Calibration

Conviction reflects the analyst's confidence that the investment thesis will play out as expected. It is distinct from the attractiveness of the opportunity — a highly attractive credit with significant information gaps should carry lower conviction than a moderately attractive credit with comprehensive data. This guide provides frameworks for calibrating conviction levels consistently and translating them into actionable recommendations.

---

## Evidence Quality and Conviction Mapping

### Information Completeness Scale

| Level | Description | Typical Situations |
|---|---|---|
| **Comprehensive** | Audited financials, management access, site visits, full credit agreement, observable market pricing, rating agency reports | Public investment-grade issuers, large-cap HY with active analyst coverage |
| **Adequate** | Public financials (potentially unaudited), limited management interaction, credit agreement available, peer-based relative value analysis | Mid-cap HY, larger private credit deals with disclosure packages |
| **Partial** | Limited financial history (< 3 years), no direct management access, incomplete credit documentation, limited comparable data | Smaller private credit, emerging market credits, first-time issuers |
| **Sparse** | Minimal verified financial data, no management access, documentation not yet finalized, no direct comps | Pre-marketing new issues, small private placements, highly bespoke structures |

### Conviction Decision Matrix

| | **Strong Thesis** (clear catalyst, quantifiable edge, supported by multiple data points) | **Moderate Thesis** (reasonable case, some execution dependency, partial data alignment) | **Weak Thesis** (directional view, significant assumptions, limited supporting data) |
|---|---|---|---|
| **Comprehensive Data** | **High Conviction** — Full-size position. Clear entry and exit parameters. | **Medium Conviction** — Standard position. Tighter monitoring triggers. | **Low Conviction** — Small or avoid. Data contradicts thesis; reassess whether thesis is valid. |
| **Adequate Data** | **High Conviction** — Standard-to-full position. Flag specific data gaps in memo. | **Medium Conviction** — Standard position. Identify what additional information would raise conviction. | **Low Conviction** — Small position only if spread compensates for uncertainty. |
| **Partial Data** | **Medium Conviction** — Reduced position. Thesis is compelling but unverifiable on key dimensions. | **Low Conviction** — Small position or conditional pass. Identify critical data needed. | **Decline** — Insufficient basis for investment. |
| **Sparse Data** | **Low Conviction** — Small position only for high-conviction mandates with relevant expertise. | **Decline** — Cannot underwrite responsibly. | **Decline** — Do not invest. |

## Quantitative Conviction Scoring

The qualitative conviction matrix above provides directional guidance. This section adds numeric calibration to enable consistent scoring across analysts and credits.

### Information Quality Score (IQ)

| Score | Range | Criteria |
|---|---|---|
| IQ-1 (High) | >90% data available | Audited financials (3+ years), management access, full credit agreement, observable market pricing, rating agency coverage, site visit or equivalent |
| IQ-2 (Medium) | 60-90% data available | Public financials (may be unaudited for recent periods), limited management interaction, credit agreement available, peer-based analysis possible |
| IQ-3 (Low) | <60% data available | Limited financial history (<3 years), no management access, incomplete documentation, limited or no comparable data |

### Analytical Uncertainty Score (AU)

Analytical uncertainty measures how sensitive the recommendation is to key assumptions.

| Score | Model Sensitivity | Description |
|---|---|---|
| AU-1 (Low) | <5% IRR swing from key assumptions | Core thesis robust across reasonable assumption ranges. Base case outcome achievable under multiple scenarios. |
| AU-2 (Medium) | 5-15% IRR swing | Thesis depends on 1-2 key assumptions that could reasonably go either way. Spread between bull and bear cases is material. |
| AU-3 (High) | >15% IRR swing | Thesis highly dependent on unverifiable assumptions. Small changes in inputs produce large changes in outputs. |

### Composite Conviction Score

| | AU-1 (Low Uncertainty) | AU-2 (Medium Uncertainty) | AU-3 (High Uncertainty) |
|---|---|---|---|
| **IQ-1 (High Data)** | **Strong** (score 9) | **Moderate-High** (score 7) | **Moderate** (score 5) |
| **IQ-2 (Medium Data)** | **Moderate-High** (score 7) | **Moderate** (score 5) | **Weak** (score 3) |
| **IQ-3 (Low Data)** | **Moderate** (score 5) | **Weak** (score 3) | **Insufficient** (score 1) |

### Conflicting Signal Rules

When upstream skills produce conflicting analytical signals:

- **2 skills conflict** (e.g., strong sector outlook from `industry-sector-analysis` but weak financial profile from `modeling-and-valuation`): No automatic downgrade. Frame the tension explicitly in the memo.
- **3+ skills conflict**: Automatic conviction downgrade by one level (e.g., Strong to Moderate). The memo must include a dedicated "Conflicting Signals" subsection explaining each conflict and why the recommended conviction level is still appropriate.
- **Thesis-kill trigger conflicts with base case**: If any thesis-kill trigger is within 10% of current levels, conviction cannot exceed Moderate regardless of other scores.

### Score-to-Action Mapping

| Composite Score | Maximum Conviction | Maximum Position Size |
|---|---|---|
| 7-9 | High | Full allocation per mandate |
| 5-6 | Medium | Standard allocation (50-75% of max) |
| 3-4 | Low | Reduced allocation (25-50% of max) |
| 1-2 | Insufficient | Decline or Conditional Pass only |

---

## Recommendation Actions

### Action Definitions

| Action | When to Use | Conviction Requirement |
|---|---|---|
| **Buy** | Positive thesis, acceptable risk/reward, adequate information | Medium or High |
| **Increase** | Existing position, thesis strengthened or spread widened attractively | Medium or High |
| **Hold** | Existing position, thesis intact, no change in risk/reward | Any (reflects prior conviction) |
| **Reduce** | Existing position, thesis weakened but not invalidated | Any |
| **Sell** | Thesis violated, risk/reward deteriorated, or stop-loss triggered | Any |
| **Avoid** | Thesis is negative — the credit is likely to deteriorate or is overvalued. Active recommendation against investment. | Medium or High (negative conviction) |
| **Decline** | Insufficient information to form a view. Not a negative credit opinion — an acknowledgment that responsible underwriting is not possible with available data. | N/A |
| **Conditional Pass** | Thesis has merit but requires specific additional information or conditions to proceed. The memo identifies exactly what is needed. | Low to Medium |

### Distinguishing Avoid, Decline, and Conditional Pass

- **Avoid**: "We have analyzed this credit thoroughly and believe it will underperform. Do not invest." Requires an analytical basis.
- **Decline**: "We cannot form a responsible credit opinion with available information. Revisit if data improves." Does not imply negative view.
- **Conditional Pass**: "This could be an attractive investment if [specific condition]. Proceed to the next stage once [specific data point] is obtained." Implies willingness to re-engage.

---

## Conviction and Position Sizing

Conviction levels translate directly into position sizing ranges. The final size within each range depends on portfolio concentration limits, sector exposure, and liquidity considerations (see `portfolio-investment-process` for detailed sizing frameworks).

| Conviction Level | Typical Size Range (% of AUM) | Maximum Single-Name Exposure | Notes |
|---|---|---|---|
| **High** | 1.0% – 3.0% | Per mandate limits | Full allocation. Entry parameters can be slightly aggressive. |
| **Medium** | 0.5% – 1.5% | 50-75% of maximum | Standard allocation. Entry at or below target levels only. |
| **Low** | 0.1% – 0.5% | 25-50% of maximum | Toe-hold or monitoring position. Entry only at attractive levels with wide stop-loss. |

**Conviction-size consistency check**: Before finalizing the memo, verify that the recommended position size is consistent with the stated conviction level. A high-conviction buy recommendation at a 0.25% position size signals internal inconsistency. A low-conviction recommendation at a 2.0% position size signals misaligned risk-taking.

---

## Common Conviction Errors

### 1. Anchoring to Sunk Analysis Time

**Error**: Recommending a buy at medium or high conviction because the analyst spent three weeks on the analysis, not because the evidence warrants it.

**Correction**: The appropriate response to extensive analysis that reveals an unattractive or unclear opportunity is Avoid or Decline — not a reluctant buy to justify the effort. Time spent is a sunk cost that should not influence the recommendation.

### 2. False Precision

**Error**: Stating high conviction based on a detailed model that relies on unverifiable assumptions (e.g., "Our model shows 8.2% IRR under the base case" when the revenue growth assumption is management guidance with no independent verification).

**Correction**: Precision in model output does not equal precision in the thesis. If the key assumption driving the model is uncertain, conviction should reflect the input uncertainty, not the output precision. State the sensitivity: "A 200bps change in revenue growth assumptions swings the IRR from 5.1% to 11.3%, underscoring the dependence on unverified management guidance."

### 3. Herd Following

**Error**: High conviction because "the market consensus is bullish" or "three other CLO managers are buying this name."

**Correction**: Market consensus is an input to relative value analysis, not a substitute for independent credit work. Consensus can be wrong, particularly at cycle inflection points. The memo must document the analyst's independent basis for conviction.

### 4. Recency Bias

**Error**: Upgrading conviction because the most recent quarter was strong, without assessing whether it represents a sustainable trend or a one-time event.

**Correction**: A single strong quarter does not change the structural credit profile. Assess whether the improvement is driven by sustainable factors (market share gains, completed restructuring, contractual repricing) or transitory ones (inventory restocking, one-time contract, favorable weather for CRE assets). Conviction should reflect the durability of the trend, not the magnitude of the latest data point.

### 5. Overweighting Qualitative Positives

**Error**: High conviction based on "strong management team" and "good sponsor" without quantifying what these qualitative assessments mean for credit outcomes.

**Correction**: Qualitative factors support conviction only when linked to measurable outcomes. "Strong management" means: track record of deleveraging post-acquisition (achieved 1.5x leverage reduction in prior deal over 18 months), disciplined M&A (passed on three acquisitions in the last two years that would have re-levered the credit), and transparent communication with lenders (proactive covenant amendment in advance of anticipated breach).

---

## Calibration Checklist

Before assigning a conviction level, verify the following:

- [ ] Conviction reflects information quality, not just thesis attractiveness
- [ ] Position size is consistent with stated conviction level
- [ ] At least one scenario has been modeled where the thesis fails — and the downside is acceptable at the recommended size
- [ ] The analyst can articulate what specific evidence would raise or lower conviction by one level
- [ ] Conviction is based on the analyst's independent work, not consensus views or management representations alone
- [ ] Qualitative conviction drivers are linked to measurable outcomes
- [ ] Time spent on analysis has not biased the recommendation toward action
