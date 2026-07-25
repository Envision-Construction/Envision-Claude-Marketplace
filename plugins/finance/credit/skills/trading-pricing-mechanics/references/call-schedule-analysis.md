---
last_updated: "2026-03-21"
---

## Call Schedule Analysis

### Typical High-Yield Call Schedule

**Structure:**
```
NC (Noncall) Period:  Years 0-3  (cannot call)
Then declining premium calls:
  Year 4:  103 (bond issuer can call entire deal at 103)
  Year 5:  102.5
  Year 6:  102
  Year 7+: 100 (par)
```

**Purpose:**
- NC period protects bondholder from immediate refinancing risk
- Declining schedule reflects declining risk as time passes
- At par (100), issuer has no incentive to call (no savings vs. maturity)

### "10% Call Feature"
Common in senior secured bonds; allows issuer to call up to 10% of original principal amount annually at specified price (usually 103).

**Example:**
```
Original issuance: $500M
10% call feature at 103 per $100 par

Year 1: Can call $50M (10% × $500M) at 103
Year 2: Can call $50M (additional, not cumulative) at 103
...continuing

Cumulative amount callable after N years: N × 10% × original amount
(Capped at 100% of original after 10 years)
```

**Impact on bondholder:**
- Limited refinancing risk in early years
- Cannot refinance entire deal at once
- Useful for operational flexibility or asset sales

### Equity Clawback (Equity Proceeds Call)
Allows issuer to call a portion of debt using proceeds from equity issuance (IPO or secondary).

**Typical structure:**
```
35% call feature:
  Issuer can call up to 35% of original principal at ~110
  Triggered by IPO or equity proceeds
  Only available if 65% of original debt outstanding

Example: $500M original issue
  - Issuer IPOs, raises equity proceeds
  - Can call $175M (35%) at 110
  - Only if $325M+ (65%) remains outstanding
  - Protects control and deleveraging optionality
```

**Bondholder implications:**
- Good sign for credit (successful IPO)
- But refinancing at 110 vs. original price = investor loss
- Often limited to specific windows (1-2 years post-close)

### Make-Whole Call (Treasury+50bp)
Allows issuer to call bonds early at a price based on Treasury yield plus spread, rather than fixed call price.

**Formula:**
```
Make-Whole Call Price = Par + Accrued + Make-Whole Premium

Make-Whole Premium = Σ[Cash Flows discounted at (Treasury + Spread)]
```

**Example:**
```
Bond: $100M, 10% coupon, 5 years to maturity
Remaining cash flows: 5% coupons + $100 par in 5 years
Treasury yield (5-year): 4%
Make-whole spread: 50 bps
Make-whole discount rate: 4.5%

Make-Whole Premium = PV of remaining cash at 4.5% - Current Price
                   ≈ $120 per $100 par (illustrative)

Issuer can call at 120 anytime (vs. standard 103 call price)
```

**Why issuers use make-whole:**
- Demonstrates confidence in credit quality
- Makes bond more attractive (lower fixed call price risk)
- No date restriction—can refinance anytime if rates fall enough

**Bondholder advantage:**
- Captures value of make-whole premium if rates drop
- Less downside from call risk
- Common in investment-grade; rarer in high-yield

---
