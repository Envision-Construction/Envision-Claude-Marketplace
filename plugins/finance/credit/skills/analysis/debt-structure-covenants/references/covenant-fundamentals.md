---
last_updated: "2026-03-21"
---

## Overview — Why Covenants Matter

Covenants are the rules a company must follow while debt is outstanding. In leveraged finance, they are the primary protection for creditors when equity cushion is thin.

### Key Principles

- **Complexity increases with leverage**: Investment grade covenants are simple; leveraged finance covenants are intricate and layered
- **Read with cynicism**: Focus on how the company could exploit loopholes and harm bondholders
- **Defined terms are critical**: Always cross-reference every key word with the definitions section; one misread definition can miss a major loophole
- **"And" vs "or" matters enormously**: Covenant conditions connected by "and" are harder to trigger; "or" makes it easier
- **"Notwithstanding" paragraphs override**: These paragraphs say "despite what we said above, this exception applies"—they often neutralize protections

---

## Covenant Analysis Workflow

### 1. Obtain the Documents
- Bond indenture or loan agreement (or executive summary from offering materials)
- Most recent financial statements
- Any amendments, waivers, or consent solicitations

### 2. Read Each Major Covenant
For each covenant, extract:
- **Exact formula**: Ratio test, dollar limit, definition of components
- **Trigger**: When is it tested? (at action, continuously, on event)
- **Remedy**: What happens if breached? (grace period, technical default, acceleration)

### 3. Map Defined Terms
- Pull every key definition (e.g., Total Debt, EBITDA, Fixed Charges)
- Check for add-backs/adjustments to EBITDA (stock-based comp, severance, one-time costs)
- Identify "and" vs "or" language in covenant conditions

### 4. Calculate Current Headroom
For each maintenance covenant:
- Company's latest financials (e.g., Q3 2024: Debt $2.0B, EBITDA $500M, Interest $140M)
- Covenant limits (e.g., 5.0x leverage, 3.5x coverage)
- Headroom: 5.0x - 4.0x = 1.0x (20% cushion)
- Is 20% enough? Compare to stressed scenario (recession, margin compression)

### 5. Project Headroom (4–8 Quarter Horizon)
- Use company's 3-year financial projections (or build your own)
- Assumes flat/rising EBITDA, stable debt levels
- Calculate pro forma ratios each quarter
- Identify which quarters are tightest (Q4 cash flow seasonality?)
- Step-downs: when do covenant limits tighten?

**Example Projection**:
| Quarter | Debt | EBITDA | Leverage | Limit | Headroom |
|---------|------|--------|----------|-------|----------|
| Q3 2024 | $2.0B | $500M | 4.0x | 5.0x | 1.0x |
| Q4 2024 | $2.05B | $480M | 4.27x | 5.0x | 0.73x |
| Q1 2025 | $2.08B | $490M | 4.24x | 4.75x* | 0.51x |
| Q2 2025 | $2.1B | $510M | 4.12x | 4.75x | 0.63x |

*Covenant limit steps down to 4.75x in Year 2

### 6. Assess Event Risk
Which covenant could be tested by:
- **M&A**: Would acquisition trigger debt incurrence test? Asset sale test?
- **Dividend/Buyback**: Is restricted payment basket sufficient?
- **Refinancing**: Must fixed charge coverage test be satisfied at new rates?
- **Change of Control**: Could a strategic buyer pay 101 put offer, or seek waiver?

### 7. Compare to Peers
- What leverage limits do comparable companies have? (3.5–5.5x typical in LBO)
- What basket structures? (50% NI or 50% EBITDA-based?)
- Tighter covenants = stricter credit = lower spread (or higher coupon)
- Looser covenants = more room to operate = higher spread (or lower coupon)

---

## Affirmative/Maintenance Covenants in Bank Agreements

Maintenance covenants are tested *continuously* (not just on event). Breach = technical default, with a grace period (usually 30 days) to cure.

### Leverage Ratio

**Formula**: Total Debt / EBITDA ≤ X.XXx

**Key features**:
- Tested at end of each quarter
- Covenant grid reflects company's own projections
- Step-downs: limits tighten over time (Year 1: 5.0x → Year 2: 4.5x → Year 3: 4.0x)
- Grace period: 30 days to cure before technical default

**Headroom Calculation**:
- Company's projections: Debt $2.0B, EBITDA $500M → 4.0x
- Covenant limit: 5.0x
- Headroom: 5.0x - 4.0x = 1.0x, or 20% cushion
- Target headroom: ~20–25% (tighter = higher risk)

---

### Interest Coverage Ratio

**Formula**: EBITDA / Interest Expense ≥ X.XXx (e.g., 2.5x)

- Sensitive to rates and refinancing events
- Example: $500M EBITDA, 2.5x covenant, $150M interest
  - Current: $500M / $150M = 3.33x ✓
  - If rates rise to push interest to $180M: $500M / $180M = 2.78x ✓
  - If rates rise to $210M: $500M / $210M = 2.38x ✗ (breach)

---

### Other Maintenance Covenants

- **Minimum cash/liquidity**: Often $X minimum required in operating account
- **Asset appraisals**: Real estate collateral must be reappraised annually; decline triggers action
- **Capex limits**: Sometimes capped relative to depreciation or as % of revenue
- **Minimum EBITDA**: Floor on operating performance; breach signals distress

---

### Springing Maturities

Some bank agreements include "springing maturity" language:
- If junior debt (bonds, second lien) matures within 6 months AND will not be refinanced, the bank loan springs to immediate maturity
- Forces company to refinance junior debt before bank loan comes due
- Avoids cascade of defaults

---
