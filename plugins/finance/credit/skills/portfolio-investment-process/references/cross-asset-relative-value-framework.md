---
last_updated: "2026-03-22"
---

# Cross-Asset Relative Value Framework

Compare risk-adjusted returns across corporate credit, private credit, CRE debt, and structured finance to decide where the next unit of risk budget belongs. Use `references/cross-asset-relative-value.md` for current benchmark inputs and live market snapshots.

## Core Principle

Cross-asset relative value is not a spread comparison. It is a normalization exercise. The question is not "which asset yields more?" but "which asset offers the best compensated downside after adjusting for loss risk, liquidity, structure, and execution realism?"

## Return Decomposition

Break the offered return into:

- **credit risk premium**: compensation for expected default and loss severity
- **liquidity premium**: compensation for limited exit flexibility
- **complexity premium**: compensation for analytical and operational burden
- **structural premium**: compensation for documentation quality, subordination, collateral, or control rights
- **technical premium**: supply-demand distortions that may reverse faster than fundamentals

## Normalization Steps

### 1. Normalize for Expected Loss

Start with loss-adjusted spread or yield:

```text
Loss-Adjusted Return = Gross Return - Expected Loss
Expected Loss = Probability of Default x Loss Given Default
```

Use current default and recovery inputs from `references/default-recovery-rates.md` when a live comparison is required.

### 2. Normalize for Liquidity

Estimate how much of the quoted return is compensation for holding-period rigidity or slow exit.

Ask:

- how quickly can the asset be sold in normal conditions?
- what happens to that exit path in a stressed market?
- is the investor structurally able to hold through the illiquidity?

Use `references/cross-asset-relative-value.md` and `references/market-benchmarks.md` for current liquidity and spread context rather than hard-coding bands here.

### 3. Normalize for Duration and Rate Exposure

Compare fixed-rate and floating-rate assets on a rate-aware basis.

Questions to answer:

- is the asset carrying rate risk, spread risk, or both?
- does the strategy want that rate exposure?
- would a hedged comparison change the ranking?

### 4. Normalize for Structural Quality

Structure can improve or worsen the real return.

Evaluate:

- maintenance versus incurrence covenants
- collateral quality and enforceability
- subordination and credit enhancement
- amortization and cash-trapping mechanics
- control rights in amendments, defaults, or restructurings

### 5. Normalize for Operational Complexity

An asset that requires intensive monitoring, specialized modeling, or bespoke servicing should clear a higher bar than a liquid plain-vanilla bond with comparable downside.

## Decision Questions

After normalization, ask:

1. Which asset offers the best compensated downside?
2. Which asset preserves optionality if the thesis changes?
3. Which structure gives the strongest downside control for the same economic risk?
4. Which asset best fits the vehicle that will own it?
5. Is the apparent premium structural and durable, or just a temporary technical dislocation?

## Common Trade-Offs

Typical trade-offs include:

- **private credit versus public loans**: control and covenants versus liquidity and mark-to-market transparency
- **CLO tranches versus single-name loans**: diversification and structural subordination versus reduced direct underwriting control
- **CRE debt versus corporate credit**: collateral and asset-level covenants versus asset-specific execution and valuation risk
- **asset-backed paper versus corporate bonds**: structural protection and amortization versus model dependence and servicing risk

## Rotation Principle

Capital should rotate across asset classes when the normalized return ranking changes, not just when raw spread leadership changes.

Useful prompts:

- Has liquidity become unusually cheap or unusually expensive?
- Are technicals making one asset class look optically attractive without improving downside?
- Has structure become more valuable because cycle risk is rising?
- Is the portfolio being overpaid or underpaid for lock-up and complexity?

## Output Standard

A cross-asset recommendation should always state:

- the alternative asset classes considered
- the normalization adjustments applied
- the structural reason for the final preference
- the key condition that would cause capital to rotate elsewhere

---

### Comparable Analysis Methodology

#### Purpose and Framework

Relative value analysis answers: **Which credit offers the best risk-adjusted value?**

By comparing similar companies' bonds and loans across dimensions like leverage, valuation, and cash generation, you identify:
- Credits offering excess yield for their risk level
- Structural or covenant differences justifying (or not) spread differences
- Trading anomalies suggesting mispricing

#### Building a Basic Relative Value Sheet

**Minimum columns:**

| Company | Security | STW (bp) | Bond Debt/EBITDA | Total Debt/EBITDA | FCF/Debt | TEV/EBITDA | STW/Leverage |
|---------|----------|----------|------------------|-------------------|----------|-----------|--------------|
| Alpha Co | Sr Notes | 275 | 2.8x | 3.2x | 18% | 5.5x | 98 |
| Beta Inc | Sr Notes | 310 | 3.1x | 3.5x | 16% | 5.8x | 100 |
| Gamma Ltd | Sub Notes | 420 | 3.8x | 4.2x | 12% | 6.2x | 111 |

**Key metrics explained:**

- **STW (Spread-to-Worst)**: The yield spread of the bond over a risk-free benchmark, accounting for call features
- **Bond Debt/EBITDA**: The leverage of the specific debt tranche
- **Total Debt/EBITDA**: The company's total leverage
- **FCF/Debt**: Cash generation relative to debt—higher is better for repayment ability
- **TEV/EBITDA**: Enterprise value multiple reflecting market's view of the company
- **STW/Leverage**: Spread compensation per unit of leverage—shows if you're being paid enough per turn of risk

#### Intracapital Comparison: Senior vs. Subordinated Within One Company

Compare the yield spread between a company's senior notes and subordinated notes. The additional yield should compensate for:
- Loss of payment priority (junior has to wait)
- Additional leverage before junior notes are in the waterfall
- Weaker covenants (often with junior debt)

**Example:**
- Senior notes: 275 bp at 3.2x net debt
- Subordinated notes: 420 bp at 3.2x net debt
- Spread pickup: 145 bp

Is 145 bp enough premium for the structural subordination risk? Depends on:
- Company stability (stable business = less subordination risk)
- Size of subordinated tranche (larger = more potential equity cushion)
- Covenant comparison (can senior notes be prepaid from operations?)

#### When Senior Bonds Trade Rich

Sometimes a company's senior notes trade at tighter spreads (lower yields) than subordinated notes would suggest. Causes include:

1. **Call features**: Senior notes may be protected from calls, making them "safer" than the subordination structure alone suggests
2. **Covenant strength**: Senior notes might have stronger financial covenants than subordinated notes
3. **Market positioning**: Senior notes may be more liquid or on index (attracts institutional demand)
4. **Overvaluation**: Pure mispricing—someone is willing to buy senior cheap

**How to exploit:** If senior notes are genuinely overvalued and subordinated notes appropriately priced, prefer subordinated (get more spread for similar risk).

#### Extended Relative Value Sheet

Add these columns for deeper comparison:

| Company | Issue Size ($M) | Rating | Next Call | Duration | CDS (bp) | Comment |
|---------|-----------------|--------|-----------|----------|----------|---------|
| Alpha Co | 400 | B | 2027 | 4.2 | 285 | Smaller issue, less liquid |
| Beta Inc | 750 | B | 2028 | 4.5 | 310 | Index component, more demand |
| Gamma Ltd | 300 | B- | 2026 | 4.0 | 425 | Upcoming maturity pressure |

**Additional considerations:**

- **Issue size**: Larger issues tend to trade tighter (more liquid)
- **Rating**: Rating agencies' view of credit; downgrades can hurt valuations
- **Call date**: Earlier call = bond can be refinanced; matters more in declining rate environment
- **Duration**: How much will bond price change with interest rate move
- **CDS levels**: Credit default swap spreads; should roughly align with bond spreads (arbitrage if they diverge)

#### Operational Comparison Sheet

Build a second sheet comparing the underlying businesses on operating metrics:

| Company | Revenue Growth (YoY) | EBITDA Margin | Subscriber Growth | ARPU | EBITDA Growth |
|---------|---------------------|---------------|-------------------|------|---------------|
| Alpha Co | 4% | 32% | 2% | $89 | 6% |
| Beta Inc | 6% | 29% | 4% | $92 | 8% |
| Gamma Ltd | 2% | 27% | 0% | $78 | 1% |

**Key insights:**

- **Revenue and EBITDA growth**: Higher growth supports higher leverage multiples
- **Margin trends**: Expanding margins are positive; contracting margins signal competitive pressure or cost headwinds
- **Industry-specific metrics**: Subscriber/ARPU growth for telecom; same-store sales for retail; etc.

Compare operational metrics vs. financial metrics. A company with strong EBITDA growth but poor leverage ratios might be in an investment phase. A company with declining margins but stable debt metrics might be at risk.

#### Covenant Comparison

For each credit, document:

1. **Maintenance covenants**: Interest coverage test, leverage ceiling, etc.
   - How much headroom does each company have?
   - Which company has most financial flexibility?

2. **Incurrence covenants**: Restrictions on additional borrowing, dividends, asset sales
   - Can the company easily refinance?
   - Can it pay a dividend?

3. **Affinity between covenants**: Bank maintenance covenants vs bond incurrence covenants
   - Bank covenants are usually tighter (covenant-lite loans are looser)
   - See which company can go longer without breaching

#### Subjective Factors and Event Analysis

Supplement quantitative relative value with forward-looking analysis:

1. **Upcoming events**: Maturity approaching, covenant step-down, management change
2. **Probability-weighted impact**: If 60% chance of refinancing within 12 months, how does that affect relative value?
3. **Competitive position changes**: New competitor entering? Market consolidation?
4. **Leverage trajectory**: Is management committed to deleveraging, or will leverage drift higher?
