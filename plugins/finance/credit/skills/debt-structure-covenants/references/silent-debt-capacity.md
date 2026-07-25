---
last_updated: "2026-03-22"
---

## Silent Debt Capacity

### Definition

Silent debt capacity is the additional debt an issuer can incur under its existing documents **without obtaining creditor consent**. It is the gap between reported leverage and the leverage the borrower could reach after using available baskets, ratio debt, incremental capacity, and related carve-outs. Analysts who focus only on drawn debt miss how much structural risk is still available inside the agreement.

---

### Components of Silent Debt Capacity

#### 1. Builder Basket (Retained Excess Cash Flow Accumulation)

The builder basket accumulates over time based on a formula tied to retained earnings, consolidated net income, or excess cash flow since the agreement's closing date.

- **How it grows**: Each quarter of positive net income adds to capacity; negative quarters may or may not reduce it (check "no claw-back" language)
- **Usage**: Funds restricted payments (dividends, buybacks) OR additional debt incurrence, depending on agreement structure
- **Risk**: After several years of profitability, accumulated capacity can become large enough to change the creditor position materially

#### 2. General Debt Basket (Fixed-Dollar Free-and-Clear Amount)

A fixed-dollar amount of additional debt permitted without any financial test. Often expressed as the greater of a dollar amount and a percentage of EBITDA or total assets.

- **Formula examples**: A fixed dollar amount, or the greater of a dollar amount and a percentage of EBITDA or assets
- **Risk**: The EBITDA-linked formulation grows with the business, creating ever-larger capacity

#### 3. Ratio Debt Basket (Leverage-Based Incurrence Test)

Permits unlimited additional debt so long as the issuer meets a leverage test at the time of incurrence (typically a pro forma first lien or total leverage ratio). This is the single largest source of silent capacity.

- **Critical flaw**: The test is only run at the moment of incurrence; if EBITDA subsequently declines, the debt remains outstanding
- **Risk**: A borrower can look conservatively levered today while still having large uncapped capacity under a ratio test

#### 4. Incremental Facility Capacity

Specific provisions governing additional term loan or revolver commitments under the existing credit agreement, often with Most Favored Nation (MFN) protections and inside-maturity restrictions.

- **MFN protection**: New incremental debt may be constrained if pricing or economics move too far above the existing debt
- **Inside maturity**: Incremental debt must mature no earlier than existing debt (prevents new debt from jumping the repayment queue)
- **Capacity**: Often combines fixed-dollar and ratio-based capacity in the same provision
- **MFN sunset**: Time limits can weaken protection later in the life of the deal

#### 5. Contribution Debt

Equity contributions to the borrower can create additional debt capacity under contribution-debt or cure-related language.

- **Mechanism**: Sponsor injects equity → company designates it as a "Cure Amount" or "Specified Equity Contribution" → unlocks additional debt basket
- **Risk**: Creates circularity where equity raises fund debt issuance, potentially increasing total leverage rather than reducing it
- **Analyst question**: Does sponsor support reduce leverage in substance, or does it simply create room for more debt?

---

### Calculating Total Silent Capacity: Worked Example

**Issuer Profile:**
- LTM EBITDA: $400M
- Total Debt Outstanding: $1,600M (4.0x leverage)
- First Lien Debt: $1,200M (3.0x first lien leverage)

**Credit Agreement Provisions:**
- Ratio debt basket: First Lien Net Leverage ≤ 4.25x
- General debt basket: Greater of $150M or 37.5% of LTM EBITDA
- Builder basket: 50% of cumulative CNI since closing ($180M accumulated over 3 years)
- Incremental facility: $100M fixed plus ratio-based amounts
- Contribution debt: None outstanding

| Component | Calculation | Available Capacity |
|---|---|---|
| **Ratio debt basket** | (4.25x − 3.0x) × $400M EBITDA | $500M |
| **General debt basket** | Greater of $150M or 37.5% × $400M | $150M |
| **Builder basket** | 50% of cumulative CNI (3 years of earnings) | $180M |
| **Incremental facility (fixed)** | Fixed amount under credit agreement | $100M |
| **Less: existing usage** | Prior incremental draws against fixed basket | ($50M) |
| **Total Silent Capacity** | | **$880M** |

**Impact on True Leverage:**
- **Reported leverage**: $1,600M / $400M = **4.0x**
- **Maximum potential leverage**: ($1,600M + $880M) / $400M = **6.2x**
- **Leverage gap**: 2.2x — this is the hidden risk that headline metrics do not capture

**Important caveats:**
- Not all baskets are additive — some agreements contain "nesting" provisions where usage of one basket reduces availability under another
- Ratio debt capacity is dynamic: if EBITDA deteriorates, ratio-based capacity can shrink quickly even if fixed-dollar baskets remain available
- Builder basket may have restricted payment usage that reduces debt incurrence capacity

---

### Why Silent Capacity Matters

**For credit analysis:**
- Headline leverage ratios understate true risk if large silent capacity exists
- Two issuers with identical drawn leverage can have very different risk depending on unused capacity and leakage pathways
- Peer comparisons must account for documentation quality, not just drawn leverage

**For recovery analysis:**
- Higher actual leverage at default (because borrower drew on silent capacity during stress) translates directly to lower recovery rates
- Enterprise value / total claims is the core recovery driver — silent capacity inflates the denominator
- See the `modeling-and-valuation` skill for how leverage projections should incorporate total capacity, not just currently drawn debt

**For pricing and relative value:**
- Two credits at identical spreads but different silent capacities offer asymmetric risk-reward
- Documentation-adjusted spread analysis should widen the effective spread for credits with large silent capacity
- See the `trading-pricing-mechanics` skill for relative value frameworks that incorporate documentation risk

---

### Silent Capacity Screening Framework

Use the quantified result to answer three questions:

1. **How much additional debt could be incurred without consent?**
2. **Which pathways are easiest to access in practice: ratio debt, free-and-clear baskets, incremental facilities, or contribution mechanics?**
3. **How would recovery, refinancing flexibility, and position sizing change if the borrower actually used that capacity?**

Map the answer into current root-level portfolio and documentation-risk standards rather than relying on a static local threshold table.

---
