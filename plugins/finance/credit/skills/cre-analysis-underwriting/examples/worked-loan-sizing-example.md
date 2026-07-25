## Worked Loan Sizing Example

**Property:**
- Appraised value: $28,500,000
- Stabilized NOI: $2,000,000
- Borrower seeks maximum leverage

**Lender Parameters:**
- LTV limit: 70%
- Minimum DSCR: 1.25x
- Minimum Debt Yield: 9%
- Interest rate: 6.5%
- Amortization: 30-year (amortization factor = 0.0664)

**Constraint 1: LTV**

```
Max Loan = 70% × $28,500,000 = $19,950,000
```

**Constraint 2: DSCR**

```
Max annual debt service = $2,000,000 / 1.25 = $1,600,000

Annual debt service = (Loan × 0.065) + (Loan × 0.0664)
                    = Loan × 0.1314

Loan × 0.1314 = $1,600,000
Max Loan = $12,177,000
```

**Constraint 3: Debt Yield**

```
Max Loan = $2,000,000 / 0.09 = $22,222,000
```

**Binding Constraint:** The DSCR constraint yields the smallest maximum loan of **$12.177M** (42.7% LTV). The lender would offer a loan of $12.177M to this borrower, not $19.95M or $22.22M.

**Summary Table:**

| Constraint | Limit/Minimum | Implied Max Loan | % LTV |
|-----------|--------------|------------------|-------|
| LTV | 70% | $19,950,000 | 70.0% |
| DSCR | 1.25x | $12,177,000 | 42.7% |
| Debt Yield | 9.0% | $22,222,000 | 78.0% |
| **Binding Constraint** | — | **$12,177,000** | **42.7%** |

This illustrates why lenders increasingly favor debt yield: it forces a more conservative loan structure and better protects against downside scenarios.

---
