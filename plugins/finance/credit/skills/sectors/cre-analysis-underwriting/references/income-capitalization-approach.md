---
last_updated: "2026-03-22"
---

# Income Capitalization Approach

Income capitalization is the primary valuation method for stabilized real estate because lenders are underwriting the durability of income, not just the asset itself.

Use `references/market-benchmarks.md` for current cap-rate context. Use this note for the valuation logic.

## 1. Build NOI Correctly

The income approach begins with a disciplined NOI build. The purpose is not to create the highest possible NOI, but the most defensible one.

```text
Gross Potential Rent
  + Other Income
  = Gross Potential Income
  - Vacancy & Credit Loss
  = Effective Gross Income
  - Operating Expenses
  = Net Operating Income
  - Recurring capital needs / reserves where relevant to debt service
  = Underwriter cash flow for sizing
```

### Keep these cases separate

- **In-place NOI**: What the property earns today
- **Stabilized NOI**: What a sustainable operating level looks like after normal vacancy and market-rent assumptions
- **Pro forma NOI**: What the sponsor expects after executing a business plan
- **Underwriter NOI**: The lender's disciplined version used for sizing

If those cases are blended together, underwriting precision is lost.

### What belongs in NOI

- Base rent and recurring reimbursements
- Recurring ancillary income
- Taxes, insurance, utilities, repairs, payroll, management, and recurring operating costs

### What does not belong in NOI

- Debt service
- Capital expenditures
- TI/LC unless intentionally shown below the line or normalized in a clearly disclosed way
- One-time income or unusual recoveries
- Sponsor-specific synergies that are not yet proven

### Illustrative math example

```text
Gross Potential Rent                     1,000,000
+ Other Income                              50,000
= Gross Potential Income                 1,050,000

- Vacancy & Credit Loss                    (52,500)
= Effective Gross Income                  997,500

- Operating Expenses                     (397,500)
= Net Operating Income                    600,000
```

This example is intentionally generic. Use property-specific facts for underwriting and root references for current market calibration.

## 2. Direct Capitalization

The basic valuation formula is:

```text
Value = NOI / Cap Rate
```

This is most useful when the subject is operating near a stable level and comparable market evidence is credible.

### Cap-rate judgment depends on

- property type and quality
- location and submarket liquidity
- lease duration and tenant quality
- rollover exposure and capital needs
- demand durability and buyer depth

Cap rate is not just a market quote. It is a risk translation of the specific asset's income durability.

### The NOI and cap rate must match

| NOI Used | Matching Cap-Rate Logic |
|---|---|
| **In-place NOI** | Use when current earnings are representative and sustainable |
| **Stabilized NOI** | Use when a credible near-term normalization is required |
| **As-is NOI for transitional assets** | Often too weak for final value; may require separate as-is and stabilized views |

Do not apply a stabilized cap rate to a clearly unstable NOI stream without explaining the bridge.

### Generic sensitivity example

Assuming NOI of 600,000:

| Cap Rate | Implied Value | Value Change |
|---|---|---|
| 4.5% | 13,333,333 | +11.1% |
| 5.0% | 12,000,000 | Baseline |
| 5.5% | 10,909,091 | -9.1% |
| 6.0% | 10,000,000 | -16.7% |

Even modest cap-rate changes can move value materially, so cap selection should be tested rather than treated as a single-point truth.

## 3. DCF as a Cross-Check

DCF is most useful when lease rollover, capex, downtime, or phased stabilization make a single stabilized NOI insufficient.

### DCF logic

1. Project annual cash flows using disciplined rollover assumptions.
2. Include concessions, downtime, TI/LC, capex, and reserves where relevant.
3. Estimate terminal value using a forward NOI and an exit cap rate.
4. Discount all cash flows at a rate consistent with the business-plan risk.

DCF is not a substitute for discipline on assumptions. It is simply a more detailed way to express the same underwriting view.

### DCF is especially useful when

- lease rollover is meaningful
- TI/LC or downtime materially affects value
- the business plan involves staged stabilization
- value depends on time and path, not just steady-state income

### Discount-rate construction

Discount rates should reflect:

- current risk-free benchmark
- real-estate risk premium
- asset-specific risk adjustments
- reliability of the stabilization path
- exit uncertainty

Use `references/market-benchmarks.md` for current market calibration. This methodology file should not be the source of current discount or cap assumptions.

## 4. Cross-Checks

No valuation method should stand alone.

- **Direct cap** is strongest for genuinely stabilized assets.
- **DCF** is stronger when timing and rollover matter.
- **Sales comparison** helps anchor whether the income methods are producing a market-consistent answer.
- **Cost approach** is useful as a reasonableness check in selected situations.

If direct cap, DCF, and sales evidence disagree materially, the underwriter should explain why rather than averaging blindly.

## 5. When Income Capitalization Is Strongest

- Stabilized multifamily
- Well-leased industrial
- Diversified retail with durable occupancy
- Office with defensible occupancy and manageable rollover

## 6. When It Is Weakest

- Ground-up development
- Highly vacant or distressed assets
- Single-tenant or highly concentrated buildings near lease cliff
- Specialty assets with uncertain alternative use
- Transitional assets whose value depends mainly on sponsor execution

In those cases, income capitalization may still be used, but it should be paired with as-is versus stabilized framing, cost context, or recovery-style downside analysis.

## 7. Practical Output

For underwriting, show:

1. **NOI bridge**: from rent roll and operating statements to underwriter NOI
2. **Selected cap rate**: with a clear rationale tied to risk, quality, and liquidity
3. **Value range**: not just one point estimate
4. **Cross-checks**: sales comparison, cost or replacement, and DCF where needed
5. **Sensitivity**: how value changes if NOI weakens or cap rate widens

## Common Mistakes

- Capitalizing sponsor upside as if it were already earned
- Using a cap rate without explaining why the subject deserves it
- Ignoring recurring capex, TI/LC, or reserves in the cash flow story
- Treating a thin comp set as authoritative
- Using DCF precision to hide weak assumptions

## Quick Links

- For current cap-rate and spread calibration: `references/market-benchmarks.md`
- For rollover-specific cash flow modeling: `skills/cre-analysis-underwriting/references/lease-analysis-deep-dive.md`
- For stress design and valuation downside: `skills/cre-analysis-underwriting/references/sensitivity-analysis-for-cre.md`
