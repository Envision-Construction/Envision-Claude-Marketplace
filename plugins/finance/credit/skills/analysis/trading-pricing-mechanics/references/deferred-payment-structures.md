---
last_updated: "2026-03-21"
---

## Deferred Payment Structures

### Zero-Coupon Bonds
No cash interest paid; instead, issued at deep discount and accrete to par at maturity.

**Formula:**
```
Price = Par / (1 + r)^n

where:
  r = yield per period
  n = number of periods
```

**Example:**
- Par: $100,000
- Maturity: 10 years
- Yield: 7%

```
Price = $100,000 / (1.07)^10
       = $100,000 / 1.9672
       ≈ $50,835

Investor pays $50,835 today, receives $100,000 in 10 years
Implicit annual return: 7%
```

**Tax treatment (AHYDO rules):**
- "Applicable High-Yield Discount Obligation"
- IRS requires accrual of discount annually for tax purposes
- Investor reports income each year even though no cash received
- Can create negative carry for tax-exempt investors

**In leveraged finance:**
- Used in restructurings, PIK toggles, or distressed situations
- Allows issuer to defer cash outflow
- Higher promised yield to compensate for deferred payments and risk

### Zero-Step Coupon
Zero coupon for an initial period, then steps up to regular coupon payment.

**Example (Typical LBO structure):**
```
Years 1-3:  0% (no payment)
Years 4-7:  6% semi-annual coupon
Year 8:     Principal repayment

Price calculation:
  PV = 3×0 + Σ[3/(1+y)^t for t=7-14] + 100/(1+y)^16

If y = 8% annual (4% per period):
  PV = 0 + 3×[1-(1.04)^-8]/0.04 × (1.04)^-6 + 100/(1.04)^16
     = 3×7.435 × 0.7903 + 100×0.5339
     ≈ 17.65 + 53.39
     ≈ 71.04 per $100 par
```

**Use case:** Allows issuer to build EBITDA cushion before debt service kicks in (typical in sponsors' models).

### PIK (Payment-in-Kind) Bonds
Interest paid in additional bonds rather than cash. Principal compounds over time.

**Formula:**
```
Accreted Value = Par × (1 + PIK Rate)^n

where:
  n = number of accrual periods
```

**Example:**
```
Par: $100,000
PIK Rate: 12% annual (6% per period)
Accrual periods: 20 (10 years, semi-annual)

Accreted Value = $100,000 × (1.06)^20
               = $100,000 × 3.2071
               = $320,710

Bondholder receives $320,710 at maturity instead of $100,000
All compounding is reinvested interest (no cash received)
```

**Price impact:**
- PIK bonds trade at discounts because investor doesn't receive cash
- Must pay income taxes on accrued PIK even without cash receipt
- Creates significant negative carry

**Example pricing:**
```
PIK bond with 12% PIK rate
Investor's required yield: 10%

Price = Accreted Value / (1 + investor yield)^n
      = $320,710 / (1.10)^10
      ≈ $123.30 per $100 par

(Investor gets 10% return, but reinvestment boost from PIK helps offset)
```

### Toggle Bonds
Issuer can choose each period to pay cash coupon OR add PIK coupon to principal.

**Example structure:**
```
Toggle Option: 10% cash OR 12% PIK each period

Year 1: Issuer chooses 10% CASH (pays $10M on $100M)
Year 2: Issuer chooses 12% PIK (principal grows to $112M)
Year 3: Issuer chooses 10% CASH (pays $11.2M on $112M)
Year 4: Issuer chooses 12% PIK (principal grows to $125.44M)
...continues to maturity
```

**Pricing challenge:**
- Must model issuer's likely choices (usually: cash when able, PIK when stressed)
- Requires scenario analysis and management discretion assessment

**Typical model:**
```
Scenario 1 (Base case - issuer stays healthy):
  Mostly CASH payments → behaves like regular bond

Scenario 2 (Stress - EBITDA dips):
  Switch to PIK periodically → higher principal at maturity

Weighted Price = Prob(Scenario 1) × Price_1 + Prob(Scenario 2) × Price_2
```

---
