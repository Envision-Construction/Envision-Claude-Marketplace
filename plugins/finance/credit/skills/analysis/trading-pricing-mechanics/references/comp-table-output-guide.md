## Comp Table Output Guide

Use this guide whenever producing peer comparisons, basis analyses, or tiering exercises. The goal is not to maximize the number of rows; it is to compare the target against a cohort that is economically relevant and normalized for the main structural differences.

### 1. Build the Right Cohort First

Choose peers in this order:

1. Same sector or sub-sector.
2. Similar place in the capital structure.
3. Similar rating or risk bucket.
4. Similar rate format and optionality.
5. Similar maturity window and liquidity.

Do not mix secured and unsecured debt, fixed and floating instruments, or performing and distressed names without explicitly adjusting for the structural gap.

### 2. Default Table Shape

Use 4-6 comps for a standard analysis. Expand only when the extra names are truly informative.

```text
Peer Comparable Analysis: [Target Issuer] [Instrument Type]
As of: [Date]
────────────────────────────────────────────────────────────────────────────────────────────
                              Gross    Net     Int                              Dollar
Issuer          Rating (M/S)  Lev      Lev     Cov    FCF/Debt   OAS/DM  YTW    Price   Mat
────────────────────────────────────────────────────────────────────────────────────────────
TARGET ISSUER   B2/B          5.2x     4.8x    2.5x   8%         +425    8.75%  96.50   2030
Comp A          B1/B+         4.5x     4.0x    3.0x   10%        +350    8.00%  98.00   2031
Comp B          B2/B          5.5x     5.0x    2.3x   6%         +475    9.25%  94.00   2029
Comp C          B2/B          5.0x     4.5x    2.7x   9%         +400    8.50%  97.00   2030
Comp D          B3/B-         6.0x     5.5x    2.0x   5%         +525    9.75%  92.00   2029
────────────────────────────────────────────────────────────────────────────────────────────
Cohort Median   B2/B          5.1x     4.6x    2.6x   8.5%       +413    8.63%  96.75   2030
Target vs Med   In-line       +0.1x    +0.2x   -0.1x  -0.5%      +12     +12bp  -0.25   --
────────────────────────────────────────────────────────────────────────────────────────────
Δ Since Last Review: Target +25 wider, Cohort +15 wider → Target underperformed by 10 bps
```

### 3. Required Columns

| Column | What it captures |
|---|---|
| Issuer | Target first, clearly labeled |
| Rating (M/S) | Rating anchor or risk bucket |
| Gross Leverage | Total debt burden |
| Net Leverage | Balance-sheet flexibility |
| Interest Coverage | Cushion against earnings volatility |
| FCF/Debt | Cash conversion and deleveraging capacity |
| OAS/DM | Main spread metric for value comparison |
| YTW | Realized yield under the relevant downside path |
| Dollar Price | Price context and distance from par |
| Maturity | Tenor and refinancing horizon |

Add columns only when they explain a likely pricing difference. Common additions are issue size, next call date, duration, covenant type, ownership, and a short structural note.

### 4. Cohort Summary Rules

- Use the median as the default summary statistic.
- Report the mean only when the set is tight and free of major outliers.
- If one name is distressed, either exclude it or clearly separate it from the performing cohort.
- If the cohort is too small to be robust, say so rather than pretending the table is statistically strong.

### 5. Interpreting the Table

The target is only "cheap" when it trades wide after adjusting for:

- Leverage and coverage quality.
- Sector or business-model risk.
- Security package and recovery expectations.
- Rate format and optionality.
- Liquidity and issue size.
- Near-term event risk such as a call, repricing, downgrade, or refinancing wall.

If spread rank and fundamental rank diverge, that is where the relative-value discussion starts.

### 6. Cross-Market Basis Format

Use this when comparing two instruments of the same issuer.

```text
Cross-Market Basis Analysis: [Issuer Name]
As of: [Date]
──────────────────────────────────────────────────────────────────────────────
                                                        Dollar
Instrument      Coupon/Spread    DM/OAS    YTW    Price    Maturity    WAL
──────────────────────────────────────────────────────────────────────────────
TL B (1L)       S+350            +365      8.15%  99.25    2031        4.2y
Sr Unsec Notes  7.500% fixed     +425      8.75%  96.50    2030        3.8y
──────────────────────────────────────────────────────────────────────────────
Observed Basis:                  -60 bps

Structural Adjustments:
  Security premium (1L vs unsec):     -100 to -150 bps
  Fixed vs floating adjustment:       +30 to +50 bps
  Liquidity premium:                  +20 to +30 bps
  Optionality adjustment:             +10 to +20 bps
  ─────────────────────────────────────────────────────
  Warranted basis:                    -40 to -50 bps
  Conclusion: Loan trades 10-20 bps rich vs bond
```

State the observed basis, the warranted basis, and the reason for any residual gap.

### 7. Tiering Exercise Format

Use tiering when the question is "does spread rank match quality rank?"

```text
Fundamental Ranking vs Market Pricing: [Sector / Cohort Name]
As of: [Date]
──────────────────────────────────────────────────────────────────────
Rank  Issuer          Quality Score    OAS/DM    Spread Rank   Verdict
──────────────────────────────────────────────────────────────────────
1     Comp E          Strong           +375      2nd tightest  Fair
2     Comp A          Above Avg        +350      Tightest      Fair
3     TARGET          Average          +425      4th           Wide by ~25 bps
4     Comp C          Average          +400      3rd           Fair
5     Comp B          Below Avg        +475      5th           Fair
6     Comp D          Weak             +525      Widest        Fair
──────────────────────────────────────────────────────────────────────
Misalignment: Target ranked 3rd by quality but 4th by spread
```

Quality rank should reflect the full underwriting view, not just one metric.

### 8. Basis Analysis Format

Use this when quantifying whether the target deserves its spread differential.

```text
Basis Analysis: [Target Issuer] vs [Cohort Name]
As of: [Date]
──────────────────────────────────────────────────────────
Target OAS/DM:                        +425 bps
Cohort median OAS/DM:                 +413 bps
Observed differential:                +12 bps wide

Warranted Premium / (Discount):
  Higher leverage:                    +5 to +10 bps
  Lower coverage:                     +5 bps
  Stronger sponsor support:           -10 bps
  Better sector positioning:          -5 bps
  ──────────────────────────────────
  Net warranted differential:         -5 to 0 bps

Mispricing estimate:                  +12 to +17 bps wide of fair value
Catalyst:                             [What closes the gap]
Timeline:                             [Expected path]
Conviction:                           [High / Medium / Low]
```

Bound the adjustments rather than forcing false precision. The point is disciplined judgment, not pseudo-accuracy.
