---
last_updated: "2026-03-22"
---

# Loan Sizing: Three Simultaneous Constraints

CRE debt should be sized by testing **LTV, DSCR, and debt yield at the same time**. The binding constraint is the most restrictive one, not the average of the three.

Use `references/typical-deal-parameters.md` for current lender thresholds and market conventions. This note explains the logic.

## 1. LTV

```text
Maximum Loan = Value x LTV Limit
```

### What LTV measures

LTV is a collateral-value test. It answers: **how much value cushion exists if the asset must be refinanced or sold?**

### Best use

- stabilized collateral
- assets with credible valuation evidence
- situations where sale or refinanceability drives recovery

### Weakness

LTV can overstate safety if value depends on optimistic cap rates, lease-up, or sponsor execution.

## 2. DSCR

```text
DSCR = NOI / Annual Debt Service
```

### What DSCR measures

DSCR is a periodic cash-flow test. It answers: **can current or underwritten NOI service the proposed debt payments?**

### Best use

- amortizing or term loans where periodic payment burden matters
- assets with relatively stable operating income
- loans where current debt service capacity is the main control

### Weakness

DSCR depends on rate and amortization structure. It can make loans appear safer or weaker simply because terms differ.

## 3. Debt Yield

```text
Debt Yield = NOI / Loan Amount
```

### What debt yield measures

Debt yield is a capital-efficiency test. It answers: **how much current income supports each dollar of debt, independent of coupon and amortization?**

### Best use

- comparing structures across different rates
- assets where lenders want a pure income-to-loan buffer
- refinance and downside analysis

### Weakness

Debt yield does not directly capture payment timing burden and should not replace DSCR where debt service structure matters.

## 4. Why the Binding Constraint Changes

| Situation | Constraint More Likely To Matter |
|---|---|
| **Strong collateral value but tighter payment burden** | DSCR |
| **Current cash flow is healthy but valuation is weak** | LTV |
| **Lender wants protection independent of rate structure** | Debt yield |
| **Transitional or bridge execution risk** | Often LTV and debt yield, with future-funding controls layered on |

The point is not to predict the binding ratio in advance. It is to show which one actually limits proceeds.

## 5. Underwriting Sequence

1. Determine the correct NOI for sizing.
2. Establish value through the appropriate valuation methods.
3. Apply market or lender thresholds from root references.
4. Calculate maximum proceeds under each constraint.
5. Identify the binding constraint.
6. Re-test under downside NOI, higher rates, and wider cap rates.

## 6. Refinance Discipline

Loan sizing should not stop at origination.

At maturity, re-test:

- DSCR under stressed refinance rate
- debt yield under stressed NOI
- LTV under stressed value

Many CRE problems emerge because refinance proceeds fail before current-period operations fail.

## 7. Transitional Assets

For business-plan assets, keep the sizing cases separate:

- **as-is sizing**
- **future-funding or holdback logic**
- **stabilized take-out sizing**

Do not present stabilized proceeds as if they are immediately available against an unstabilized asset.

## 8. Worked Logic Example

```text
Max Loan by LTV        = underwritten value x lender LTV limit
Max Loan by DSCR       = underwritten NOI / minimum DSCR / debt constant
Max Loan by Debt Yield = underwritten NOI / minimum debt yield

Recommended Loan = lowest of the three
```

The recommended loan may be further reduced for reserves, future funding, rounding discipline, or additional structural risk.

## 9. Output Template

Show:

1. **NOI used for sizing**
2. **Value used for LTV**
3. **Thresholds used**, sourced from root references or lender guidance
4. **Maximum loan under each constraint**
5. **Binding constraint**
6. **Resulting actual LTV, DSCR, and debt yield at the recommended loan**

## Common Mistakes

- Averaging the three constraints instead of sizing to the tightest
- Using sponsor NOI instead of underwriter NOI
- Treating stabilized proceeds as current proceeds on a transitional asset
- Reporting origination ratios without refinance stress
- Forgetting that reserves and future funding can reduce effective proceeds even after the ratio test is done
