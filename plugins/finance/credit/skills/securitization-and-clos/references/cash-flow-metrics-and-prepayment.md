last_updated: "2026-03-22"
---

## Cash Flow Metrics And Prepayment

Cash flow analysis in securitization starts with one question: how quickly does principal come back, and what happens to losses or optionality while you wait? The same pool can look safe or risky depending on prepayment, default timing, and where a tranche sits in the waterfall.

### Core Metrics

| Metric | What it measures | Why it matters |
|---|---|---|
| **WAL** | Average time to principal return | Drives extension risk, carry profile, and sensitivity to faster or slower amortization |
| **CPR / SMM** | Voluntary prepayment speed | Critical for RMBS and some ABS; changes both timing and option cost |
| **CDR** | Default rate | Determines how fast collateral deterioration reaches the structure |
| **Loss Severity / LGD** | Loss per default | Controls how much enhancement is truly available after recoveries |
| **CNL** | Cumulative realized losses | Tracks whether structural protection is being consumed faster than expected |
| **DM / Spread / OAS** | Compensation over benchmark | Helps separate carry from embedded option or liquidity risk |

### WAL Discipline

- WAL is only useful when tied to a clear cash flow path. A short stated maturity can still hide long WAL if principal is back-ended.
- Faster principal return generally helps junior tranches and hurts premium-priced, reinvestment-sensitive paper.
- Slower principal return generally increases extension risk and keeps the investor exposed to collateral deterioration for longer.
- When comparing securities, ask whether WAL is driven by scheduled amortization, prepayments, calls, or structural assumptions that may not hold in stress.

### Prepayment Framework

Use prepayment modeling as a framework, not a single point estimate.

**1. Start with the right driver**
- RMBS is driven mainly by refinancing incentive, seasoning, and housing turnover.
- Consumer ABS is usually more sensitive to borrower behavior and asset turnover than to rates.
- CLO prepayments come from refinancing, repricing, M&A, and opportunistic liability management at the borrower level.

**2. Use PSA as a common language, not a forecast**
- PSA is a standard benchmark for mortgage speed assumptions.
- It is useful for scenario comparison, but real pools will diverge because borrower mix, seasoning, geography, documentation quality, and frictions all matter.

**3. Build an S-curve mentally even when the model is simple**
- Prepayments usually stay at a floor when refinancing is uneconomic.
- They accelerate sharply once the borrower has a clear economic incentive to refinance.
- They eventually plateau because not every borrower can or will refinance.

**4. Adjust for burnout**
- Seasoned pools often prepay more slowly than incentive alone would suggest because the easiest borrowers have already exited.
- Burnout is especially important in seasoned mortgage pools and in legacy collateral where the remaining borrower base is less refinance-responsive.

**5. Separate turnover from refinancing**
- Some prepayments happen because assets are sold, collateral is replaced, or borrowers move, regardless of rate incentive.
- A good model keeps turnover as a floor and refinancing as the cyclical overlay.

**6. Apply seasonality only when timing matters**
- Seasonality can matter a lot for short-WAL assets or premium and discount tranches where a few months of cash flow timing move returns.
- It matters less when the investment case is dominated by cumulative loss behavior rather than cash flow timing.

### Default And Loss Discipline

- CDR tells you how quickly problems are entering the pool.
- Loss severity tells you how much enhancement each default actually consumes.
- CNL tells you how much of the original structure has already been spent.
- Delinquency buckets, cure rates, and roll rates matter because losses usually emerge through a pipeline rather than appearing all at once.

When underwriting a tranche, always ask:
- Is the deal more exposed to faster defaults or to worse severity?
- Are losses front-loaded or back-loaded relative to the tranche's protection?
- Does the structure depend on recoveries arriving quickly to repair tests?

### Spread Metrics

- **Nominal spread** is quick but weak whenever expected life is unstable.
- **Discount margin** is useful for floating-rate paper where carry relative to index matters.
- **OAS** is most valuable when embedded optionality materially changes realized cash flows.
- Never compare OAS across sectors without checking whether the prepayment or volatility assumptions are consistent.

### Asset-Class Pattern Recognition

| Asset class | Primary behavior to underwrite | Main trap |
|---|---|---|
| **Agency RMBS** | Prepayment and extension | Treating a single PSA speed as reliable through the cycle |
| **Non-agency RMBS** | Delinquency migration, severity, and slower prepay | Underestimating servicing and foreclosure timelines |
| **Consumer ABS** | Payment rate, charge-off behavior, and seasoning | Assuming prepayment behaves like mortgages |
| **CMBS** | Balloon refinance risk, workout timing, and special servicing | Focusing only on current DSCR instead of maturity risk |
| **CLO** | Repricing, refinancing, and reinvestment optionality | Using bond-style prepayment intuition for loan collateral |

### Modeling Checklist

1. Start with the structural cash flow path before you layer on market assumptions.
2. Stress prepayment separately from default and recovery; they do not move together.
3. Use ranges and scenarios rather than a single "best" speed assumption.
4. Reconcile projected WAL to the actual waterfall. A prepayment assumption that contradicts the structure is useless.
5. Re-underwrite the first-loss and last-money tranches separately; the same collateral path affects them very differently.
6. For current spread or yield levels, use `references/market-benchmarks.md` rather than embedding live numbers here.

---

### Cash Flow Waterfall Analysis

#### Waterfall Purpose & Structure
Waterfall determines the order and priority of cash distribution. Protects senior tranches by ensuring interest on senior notes is paid before mezzanine, and principal directed to senior before junior. Waterfalls can be complex, with multiple triggers and payment tests.

#### Sequential Pay (Most Common in ABS)

**Monthly cash flow priority**:
1. Collections from obligors (principal + interest)
2. Less: Servicing fees
3. Senior tranche interest payment
4. Mezzanine tranche interest payment
5. Junior tranche interest payment
6. Senior tranche principal paydown (ongoing amortization)
7. Mezzanine tranche principal paydown
8. Junior tranche principal paydown
9. Excess cash to reserve account or residual investor

**Result**: Senior tranche paid down first, achieves shortest weighted average life (WAL). Junior has longest WAL.

**Example waterfall — 3-tranche auto ABS**:
- Pool: 50,000 auto loans, $500M original balance, ~4% monthly payment rate
- Monthly collections: ~$20M principal + $2M interest = $22M
- Waterfall (simplified):
  - Servicing fee (0.50% of outstanding): −$2M
  - Remaining: $20M
  - Senior interest (70M @ 2.5%): −$0.15M → Senior pays in full
  - Mezzanine interest (20M @ 4.5%): −$0.075M → Mezzanine pays in full
  - Junior interest (10M @ 7%): −$0.07M → Junior pays in full
  - Senior principal: −$10M → Senior balance: $60M (10% paid off this month)
  - Mezzanine principal: −$7M → Mezzanine balance: $13M
  - Junior principal: −$2.75M → Junior balance: $7.25M
  - Residual/reserve: +$0.025M excess

#### Pro-Rata Pay

Alternative waterfall structure:
- Principal distributions split proportionally among all tranches simultaneously
- All tranches have identical WAL
- Interest still paid pari passu to all tranches
- Used in some CMBS deals, WBS structures, managed funds

**Example — same 3-tranche ABS, pro-rata principal**:
- After interest/fees: $20M principal available
- Senior gets: $20M x (70/100) = $14M
- Mezzanine gets: $20M x (20/100) = $4M
- Junior gets: $20M x (10/100) = $2M
- All tranches paydown together, all have similar WAL

**Trigger to Switch**: Many pro-rata structures revert to sequential pay upon performance deterioration (see Triggers below)

#### Triggers & Performance Tests

**Early Amortization Triggers** (convert pro-rata to sequential, or accelerate principal paydown):
- **Cumulative loss trigger**: If cumulative net losses exceed threshold (e.g., 3% of original pool), rapid amortization begins
- **Delinquency trigger**: If aggregate delinquency rate (30+ DPD) exceeds threshold (e.g., 3-5%), triggers activate
- **Excess spread trigger**: If monthly excess spread falls below minimum (e.g., 1.0%), indicates pool weakening
- **Default rate trigger**: If monthly CDR exceeds threshold (e.g., 2%), trigger fires
- **Servicer replacement trigger**: If servicer fails, backup servicer takes over

**Consequences of trigger**:
- Pro-rata pay → Sequential pay (senior gets all principal, junior gets none, until seniors fully paid)
- Extended amortization period (vs. original average life)
- Potential for negative carry if rates have declined and notes refinanced at lower rates
- Extension risk for senior holders if they expected 3-year WAL but deal extends to 5-7 years due to trigger

**Performance tests (ongoing covenants)**:
- Overcollateralization test: OC ratio must stay above minimum (e.g., 105%). If test fails, can trigger reserve account funding
- Coverage ratio: Interest coverage must exceed threshold
- Failure to pass tests → restrictions on distributions to residual, may require excess spread to rebuild reserves

#### Loss Distribution & Waterfall Impact

When defaults occur and losses are realized:
- Losses flow bottom-up: Junior tranche absorbs first, then mezzanine, then senior
- Example: $2M loss on $500M pool
  - Applied to outstanding junior tranche ($7.25M): Junior balance → $5.25M
  - If loss exceeded junior ($15M cumulative loss): Mezzanine absorbs excess
  - Senior untouched until mezzanine depleted
