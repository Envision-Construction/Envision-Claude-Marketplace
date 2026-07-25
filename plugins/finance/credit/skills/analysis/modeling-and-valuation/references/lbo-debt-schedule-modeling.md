---
last_updated: "2026-03-21"
---

## LBO Debt Schedule Modeling

When modeling credit for a PE-backed company, you must build the debt schedule that drives interest expense, leverage trajectory, and covenant compliance. For the complete LBO framework including sources & uses construction, operating model, and returns analysis, see `references/lbo-analysis-the-complete-lbo-model.md`.

### Debt Schedule — Tranche-by-Tranche Tracking

For each debt tranche, model year-by-year:

```
TERM LOAN B SCHEDULE         Year 0    Year 1    Year 2    Year 3    Year 4    Year 5
═══════════════════════════  ═══════   ═══════   ═══════   ═══════   ═══════   ═══════
Beginning Balance             $600      $600      $594      $540      $488      $430
  + New Borrowings               0         0         0         0         0         0
  - Mandatory Amortization      (0)       (6)       (6)       (6)       (6)       (6)
  - Cash Flow Sweep              0       (0)      (48)      (46)      (52)      (55)
  - Optional Prepayment          0        0         0         0         0         0
Ending Balance                $600      $594      $540      $488      $430      $369
Interest Rate               S+400     S+400     S+400     S+400     S+400     S+400
Cash Interest Expense         $36       $36       $34       $31       $28       $24
```

### Debt Paydown Waterfall (Priority)

```
Available Cash for Debt Service:
  EBITDA
  - Cash Interest Expense (all tranches)
  - Cash Taxes
  - CapEx
  - Working Capital Changes
  = Free Cash Flow Before Debt Paydown

Mandatory Payments (Non-Discretionary):
  1. Revolver interest + commitment fees
  2. Term Loan mandatory amortization (typically 1% of original balance annually)
  3. Senior Note interest (fixed coupon, cash-pay)
  4. Sub Note interest (cash-pay portion; PIK accrues separately)

Remaining FCF → Cash Flow Sweep:
  Applied in order of seniority:
  1. Term Loan (most senior, gets swept first)
  2. Senior Notes (if TL fully repaid or sweep allocation allows)
  3. Sub Notes (last in priority)

Sweep Percentage Grid:
  Leverage > 4.5x: 75% of excess FCF swept
  Leverage 3.5x-4.5x: 50% swept
  Leverage < 3.5x: 25% swept (or 0% with step-down)
```

### PIK Debt Accretion in the Model

For PIK or toggle tranches:
```
PIK NOTE SCHEDULE            Year 0    Year 1    Year 2    Year 3
═════════════════            ═══════   ═══════   ═══════   ═══════
Beginning Balance             $100      $100      $112      $125
  + PIK Interest Accrual        0        12        13        15
  - Cash Pay                    0         0         0         0
Ending Balance                $100      $112      $125      $140
PIK Rate                      12%       12%       12%       12%
```

**Key insight**: PIK debt GROWS the debt burden. Total leverage increases each year even if operating performance is flat. The "silent leverage" from PIK can push a company past covenant thresholds.

### Interest Expense Build

Sum interest across ALL tranches:
```
CONSOLIDATED INTEREST EXPENSE    Year 1    Year 2    Year 3
══════════════════════════════   ═══════   ═══════   ═══════
Revolver (commitment fee)          $0.4      $0.4      $0.4
Term Loan B (SOFR+400)           $36.0     $34.0     $31.0
Senior Notes (8.0% fixed)        $32.0     $32.0     $32.0
Sub Notes PIK (12% PIK)           $0.0      $0.0      $0.0
Total Cash Interest              $68.4     $66.4     $63.4
Total PIK Interest               $12.0     $13.4     $15.0
Total Interest (Cash + PIK)      $80.4     $79.8     $78.4
```

**For credit analysis**: Use CASH interest for coverage ratios. Use TOTAL interest (cash + PIK) for full leverage picture. PIK interest doesn't hit cash flow but does increase debt.

### Leverage Trajectory Modeling

```
                              Entry    Year 1    Year 2    Year 3    Year 4    Year 5
══════════════════════════════════════════════════════════════════════════════════════
Total Debt                   $1,100   $1,106    $1,055    $1,015     $965      $909
  - Cash                        $0      $20       $25       $30       $35       $40
Net Debt                     $1,100   $1,086    $1,030     $985      $930      $869
EBITDA                         $200     $215      $230      $248      $265      $280
Net Leverage                   5.5x     5.1x      4.5x      4.0x      3.5x      3.1x
Cash Interest Coverage          —       3.1x      3.5x      3.9x      4.2x      4.4x
```

**Deleveraging trajectory is the central credit thesis for any PE-backed name.** If the model shows leverage INCREASING or flat over 3 years, the credit story is broken.

### Exit Assumptions and Equity Returns

```
Exit Enterprise Value = Exit EBITDA × Exit Multiple
  Example: $280M EBITDA × 9.0x = $2,520M

Exit Equity Value = Exit EV - Remaining Net Debt
  = $2,520M - $869M = $1,651M

Sponsor Returns:
  Entry Equity: $455M
  Exit Equity:  $1,651M
  MOIC: $1,651M / $455M = 3.6x
  IRR:  (3.6)^(1/5) - 1 = 29.2%
```

### Refinancing Scenario in the Model

Model what happens if the company refinances its capital structure mid-hold:
```
Year 3 Refinancing:
  Retire: TLB at par ($488M remaining) + Senior Notes at 103 ($412M)
  New Issuance: $900M TLB at SOFR+350 (50bp tighter — credit has improved)
  Cash Interest Savings: ~$5M annually (lower spread)
  Impact on Coverage: Interest coverage improves from 3.9x to 4.2x
  Impact on Leverage: Neutral (same debt amount, just repriced)
```

---
