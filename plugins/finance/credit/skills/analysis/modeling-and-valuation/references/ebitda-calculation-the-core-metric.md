---
last_updated: "2026-03-21"
---

## EBITDA Calculation: The Core Metric

EBITDA is the starting point for all leveraged finance analysis. It represents operating earnings before financing decisions and accounting choices.

### Basic EBITDA Formula

```
Net Income (from Income Statement)
  + Interest Expense
  + Income Taxes
  + Depreciation
  + Amortization
  _______________
  = EBITDA
```

### Adjusted EBITDA

Adjusted EBITDA adds back one-time or non-recurring items to normalize earnings for analytical purposes.

**Common adjustments:**
- Restructuring charges and severance
- Litigation settlements
- Impairments and write-downs
- Stock-based compensation
- Management fees and equity grants
- Deferred revenue adjustments
- Sponsor management fees (in LBO context)
- Realized and unrealized gains/losses on asset sales
- Cost savings from synergies (implemented and credibly projected)
- Non-recurring professional fees (M&A, IPO, refinancing)

**Critical rule: Be skeptical of every adjustment.** Each must be justified:
- Is it truly non-recurring?
- Is it clearly additive to recurring cash generation?
- Are competitors including similar adjustments?
- What would covenant EBITDA look like without it?

### Pro Forma EBITDA

Pro forma EBITDA reflects what EBITDA would have been if acquisitions or divestitures had occurred at the beginning of the period.

**Approach:**
1. Identify acquisition date and divested date
2. Extract full-year EBITDA contribution for acquired business
3. Remove contribution period for divested business
4. Add/subtract to reported EBITDA

**Example:** Company acquired ABC Corp on August 1. ABC contributed $3M EBITDA from August-December. Annualized ABC = $3M ÷ 5 months × 12 = $7.2M. Pro forma EBITDA = Reported + $7.2M × 7 months / 12 = Reported + $4.2M.

### Covenant EBITDA vs. Analyst EBITDA

**Covenant EBITDA** is defined in the credit agreement (indenture or loan agreement) and is what lenders use to assess covenant compliance.

**Key differences from analyst EBITDA:**
- Credit agreements specify exactly which items are additive
- Timing of add-backs may differ (e.g., only add-backs in effect during period)
- Baskets and caps apply (e.g., "up to $5M of management fees")
- Force leverage calculations with specific definitions
- Often conservative relative to analyst adjustments

**Action:** Always review the credit agreement definition when evaluating leverage ratios.

### EBITDA Projections

#### Quick Method
```
EBITDA = Revenue × EBITDA Margin %
```
**Use for**: quick screening, high-level reviews
**Risk**: assumes margin remains stable; may mask operating changes

#### Bottom-Up Method (More Rigorous)
```
EBITDA = Revenue - COGS - SG&A + Add-backs
```

Where add-backs typically include:
- D&A (add back to get to cash flow)
- Stock-based compensation (non-cash)
- Other non-cash charges (asset write-downs, etc.)

This method is preferred because it forces you to think through each expense line.

#### Sensitivity Analysis
Show EBITDA sensitivity to revenue changes:
```
Base Case EBITDA (at Mgmt guidance)
Upside: Revenue +5% to +10% → EBITDA often +10% to +20% (positive operating leverage)
Downside: Revenue -10% to -20% → EBITDA often -15% to -30% (negative operating leverage)
```

**Example sensitivity table:**
| Revenue Change | EBITDA Change | EBITDA Margin |
|---|---|---|
| -20% | -30% | 8.0% |
| -10% | -17% | 9.0% |
| Base | Base | 10.0% |
| +10% | +20% | 11.0% |
| +20% | +35% | 12.0% |

#### Pro Forma EBITDA Adjustments
Add normalized/pro forma items when analyzing acquisitions or troubled companies:
- **Synergies**: revenue synergies (full weight), cost synergies (50-75% credit given — unachieved synergies are a risk)
- **Baseline margin normalization**: if the company is below peer margins, assume some improvement over time
- **One-time charges**: add-back actual or expected charges
- **Conservative approach**: give partial credit to expected synergies; assume some are never realized

---
