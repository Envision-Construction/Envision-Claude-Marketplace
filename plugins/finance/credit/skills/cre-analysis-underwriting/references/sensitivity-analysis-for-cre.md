---
last_updated: "2026-03-21"
---

## Sensitivity Analysis for CRE

Sensitivity analysis should answer a practical underwriting question:

**How much deterioration can this asset absorb before value, proceeds, or debt service no longer support the loan?**

Use `references/stress-scenario-framework.md` for current mild, moderate, and severe CRE shock magnitudes. This file explains how to apply those shocks to a property-level underwrite.

### 6A: Build the Right Baseline

Run sensitivities from the correct starting point:

- **In-place case**: Current rents, occupancy, and expense run rate
- **Underwriter case**: Haircut assumptions used for sizing
- **Sponsor case**: Business-plan case used to explain upside

Never stress only the sponsor case. A lender needs to know what happens to current and underwriter cash flow, not just the best-version projection.

### 6B: Stress the Main Variable Families

| Variable Family | Typical Drivers | Why It Matters |
|---|---|---|
| **Occupancy / vacancy** | Move-outs, slower lease-up, rollover downtime | Direct hit to EGI and often to refinanceability |
| **Rent** | Lower mark-to-market, concessions, renewal weakness | Erodes value and debt yield quickly |
| **Expenses** | Insurance, taxes, payroll, repairs, utilities | Margin compression can offset otherwise stable revenue |
| **Capital needs / TI / LC** | Deferred maintenance, tenanting costs, re-leasing spend | Reduces true cash flow available to debt service |
| **Rates and refinance terms** | Higher coupon, tighter sizing, lower proceeds | Creates maturity default risk even if operations hold |
| **Cap rate / exit value** | Wider market pricing, lower liquidity | Reduces collateral value and equity cushion |
| **Timing** | Slower absorption, longer downtime, delayed stabilization | Burns reserves and pushes out take-out timing |
| **Tenant event** | Major tenant default or non-renewal | Concentrated properties fail on single-credit events |

### 6C: Use One-Way and Two-Way Tests

#### One-way tests

Change one variable at a time to identify the primary value driver.

Examples:
- Occupancy only
- Rent only
- Expense inflation only
- Exit cap only
- Refinance rate only

#### Two-way tests

Use two-way matrices for variables that interact directly.

Common pairs:
- Occupancy x rent
- NOI x refinance rate
- Stabilized NOI x exit cap rate
- Lease-up pace x TI/LC burden

### 6D: Generic Matrix Templates

#### Occupancy x rent matrix

| Occupancy | Rent Downside 1 | Rent Downside 2 | Rent Downside 3 |
|---|---|---|---|
| Base occupancy | NOI / DSCR / debt yield | NOI / DSCR / debt yield | NOI / DSCR / debt yield |
| Mild occupancy downside | NOI / DSCR / debt yield | NOI / DSCR / debt yield | NOI / DSCR / debt yield |
| Moderate occupancy downside | NOI / DSCR / debt yield | NOI / DSCR / debt yield | NOI / DSCR / debt yield |
| Severe occupancy downside | NOI / DSCR / debt yield | NOI / DSCR / debt yield | NOI / DSCR / debt yield |

#### Refinance matrix

| Refinance Rate | Refi DSCR | Max Loan at Minimum DSCR | Proceeds Gap vs Current Balance |
|---|---|---|---|
| Base |  |  |  |
| Mild rate shock |  |  |  |
| Moderate rate shock |  |  |  |
| Severe rate shock |  |  |  |

### 6E: Refinance and Maturity Risk

CRE defaults often occur because refinance proceeds fall short, not because current-period cash flow instantly goes to zero.

At maturity, test:

1. **New debt service** at stressed rates
2. **Maximum proceeds** under stressed DSCR and debt yield
3. **Collateral value** under stressed cap rate
4. **Proceeds gap** against the current or projected loan balance
5. **Equity check requirement** if the loan cannot refinance in full

If the refinance only works under optimistic rent, occupancy, or cap-rate assumptions, maturity risk is the real underwriting issue.

### 6F: Tenant and Rollover Stress

For concentrated assets, run single-event stresses:

- Loss of largest tenant
- Non-renewal of major rollover cluster
- Delayed release of vacant anchor or large block
- Re-tenanting at lower rent and higher TI/LC burden

These tests are often more informative than portfolio-style percentage shocks.

### 6G: Scenario Design

Build three scenario levels using the root stress framework:

| Scenario | Purpose | What To Show |
|---|---|---|
| **Mild** | Normal downside / underwrite discipline | Cushion to covenants and refinance |
| **Moderate** | Credit committee stress case | Whether the asset still supports the proposed structure |
| **Severe** | Breakpoint / survival case | Equity shortfall, reserve burn, or workout trigger |

Apply the property-type adjustments from `references/stress-scenario-framework.md` rather than inventing new global shock levels in each asset memo.

### 6H: Minimum Output Set

Every useful CRE sensitivity exercise should show:

1. **NOI change**
2. **Value change**
3. **DSCR**
4. **Debt yield**
5. **Refinance proceeds**
6. **Any covenant or underwriting threshold breach**
7. **Sponsor equity or reserve need**

### 6I: Common Mistakes

- Stressing only one variable when the risk is clearly multi-factor
- Applying current market stress magnitudes from memory rather than root references
- Stressing stabilized NOI but ignoring the path and timing to reach stabilization
- Treating refinance rate stress separately from tighter debt-yield or LTV sizing
- Ignoring TI/LC, concessions, and downtime in rollover-heavy assets
- Reporting value sensitivity without showing loan proceeds and debt-service consequences

---
