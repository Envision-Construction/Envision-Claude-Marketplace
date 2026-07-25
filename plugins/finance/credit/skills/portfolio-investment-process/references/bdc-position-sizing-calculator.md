---
last_updated: "2026-03-22"
---

# BDC Position Sizing Calculator

This tool provides the regulatory constraint framework for sizing positions within a Business Development Company (BDC). All BDC investments must pass three binding regulatory tests before credit-based position sizing applies.

---

## BDC Regulatory Constraints Summary

| Constraint | Requirement | Source |
|---|---|---|
| Asset Coverage Ratio | ≥150% (Total Assets / Total Borrowings) | Investment Company Act of 1940, as modified by SBCAA 2018 |
| Qualifying Assets | ≥70% of total assets must be qualifying assets | Investment Company Act of 1940 |
| Maximum Leverage | ≤2.0x debt-to-equity | SBCAA 2018 (post-shareholder/board approval) |

---

## Asset Coverage Calculation

```
Asset Coverage Ratio = Total Assets / Total Borrowings
Minimum: 150% (post-SBCAA 2018)
Available Debt Capacity = (Total Assets / 1.50) - Current Borrowings
```

The asset coverage ratio is calculated on a consolidated basis and includes all outstanding indebtedness (credit facilities, unsecured notes, CLO leverage, SBA debentures). Unfunded commitments are generally excluded unless drawn.

---

## Qualifying Asset Test

```
Qualifying Assets = Securities of eligible portfolio companies
  - Private US companies (not publicly traded), OR
  - Public US companies with market cap < $250M
Required: ≥70% of total assets at time of investment
Available Non-Qualifying Capacity = (Total Assets x 30%) - Current Non-Qualifying Assets
```

The qualifying asset test is measured at the time of each new investment. If a portfolio company subsequently goes public or exceeds the market cap threshold, the position is grandfathered — but no new non-qualifying investments may be made while the ratio is below 70%.

---

## Position Sizing Worked Example

**Starting Portfolio:**
- Total Assets: $1,500M
- Total Borrowings: $750M
- Equity (Net Assets): $750M
- Qualifying Assets: $1,100M (73.3% of total assets)
- Current Leverage: $750M / $750M = 1.00x debt-to-equity

**Proposed Investment:** $30M first lien term loan to a private US company (qualifying asset), funded via credit facility draw.

### Test 1: Asset Coverage

```
Post-Trade Total Assets = $1,500M + $30M = $1,530M
Post-Trade Total Borrowings = $750M + $30M = $780M
Asset Coverage = $1,530M / $780M = 196.2% >= 150%  PASS
```

### Test 2: Qualifying Asset Test

```
Post-Trade Qualifying Assets = $1,100M + $30M = $1,130M
Qualifying Ratio = $1,130M / $1,530M = 73.9% >= 70%  PASS
```

### Test 3: Leverage Test

```
Post-Trade Debt-to-Equity = $780M / $750M = 1.04x <= 2.0x  PASS
```

**Result:** Position fits within all BDC regulatory constraints.

---

## Sensitivity Table: Maximum Additional Investment Capacity

Given the starting portfolio above ($1,500M assets, $750M borrowings, $1,100M qualifying):

| Scenario | Binding Constraint | Max New Investment |
|---|---|---|
| Qualifying asset, debt-funded | Asset coverage (150%) | $750M |
| Qualifying asset, equity-funded | No binding constraint (all tests improve) | Limited by available equity |
| Non-qualifying asset, debt-funded | Qualifying asset test (70%) AND asset coverage | ~$78M (qualifying ratio floor) |
| Non-qualifying asset, equity-funded | Qualifying asset test (70%) | ~$121M (qualifying ratio floor) |

Note: These maximums assume no other portfolio changes. In practice, marks on existing positions, repayments, and drawdowns continuously shift available capacity.

---

## Practical Considerations

- **BDC Valuation:** Portfolio holdings are marked to fair value quarterly by the board of directors. NAV declines reduce equity and can push leverage toward the 2.0x limit, potentially forcing asset sales or equity raises to restore compliance.
- **Distribution Requirements:** BDCs electing RIC status must distribute at least 90% of taxable income annually to avoid entity-level taxation. This limits retained earnings as an equity cushion and makes the BDC reliant on external capital for growth.
- **Co-Investment Limitations:** BDCs affiliated with an investment adviser must obtain an SEC exemptive order to co-invest alongside affiliated funds. The order specifies allocation procedures, eligible transaction types, and board oversight requirements. Verify exemptive order terms before allocating to a co-invested deal.
- **Cross-Trade Restrictions:** BDCs generally cannot engage in principal transactions with affiliates. Cross-trades between affiliated funds require compliance with specific regulatory conditions or no-action letter guidance.

---

## Integration with Position Sizing

The final BDC position size is determined by the most restrictive of three independent constraints:

```
BDC Position Size = MIN(
  Credit-Based Limit per portfolio-risk-parameters.md,
  BDC Regulatory Capacity (asset coverage, qualifying asset, leverage),
  Liquidity Availability (undrawn credit facility capacity, cash on hand)
)
```

Always run all three tests before presenting a position sizing recommendation. A position that passes credit analysis but breaches a BDC regulatory constraint is a hard stop — regulatory limits cannot be waived or exceeded with IC approval.
