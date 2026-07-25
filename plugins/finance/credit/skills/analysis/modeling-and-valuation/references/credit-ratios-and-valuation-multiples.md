---
last_updated: "2026-03-22"
---

## Credit Ratios and Valuation Multiples

## Leverage Ratios

Leverage ratios measure how much debt a company carries relative to its cash flow and capital structure. Higher leverage indicates greater financial risk.

### Total Debt / EBITDA

**Definition:** The primary leverage measure in leveraged finance.

**Formula:**
```
Total Debt / EBITDA
```

**Interpretation:**
- Represents how many years of EBITDA it would take to pay off all debt
- Higher ratios = more leveraged = greater financial risk
- This is the foundational leverage metric used across all credit analyses

**Practical Example:**
```
Company: Manufacturing LLC
Total Debt: $500M (includes all debt tranches)
LTM EBITDA: $125M

Total Debt / EBITDA = $500M / $125M = 4.0x

Interpretation: It would take 4 years of full EBITDA to repay all debt.
```

### Net Debt / EBITDA

**Definition:** Adjusts total debt by subtracting cash to reflect net leverage position. Better for cash-rich companies.

**Formula:**
```
Net Debt / EBITDA = (Total Debt - Cash) / EBITDA
```

**Key Decision: Cash Adjustment**
- **Subtract all cash?** Conservative approach; assumes company needs zero cash reserves
- **Subtract only excess cash?** More realistic; keeps operating/safety cash on balance sheet
- **Typical treatment:** Subtract all cash for leverage analysis, but note the distinction in commentary

**Practical Example:**
```
Company: Tech Services Inc
Total Debt: $300M
Cash: $80M
LTM EBITDA: $100M

Method 1 (All Cash):
Net Debt / EBITDA = ($300M - $80M) / $100M = 2.2x

Method 2 (Operating Cash Only: $20M):
Net Debt / EBITDA = ($300M - $20M) / $100M = 2.8x

The difference matters for highly liquid companies.
```

### Secured Debt / EBITDA

**Definition:** Measures leverage at the secured/senior debt level only.

**Formula:**
```
Secured Debt / EBITDA
```

**Why it matters:**
- Shows how much debt is backed by collateral
- Determines what unsecured creditors can access in bankruptcy
- Important for waterfall and loss-severity analysis

**Practical Example:**
```
Company: Retail Chain
Secured Debt: $200M (revolving credit + term loan)
Unsecured Debt: $150M (senior notes + subordinated debt)
Total Debt: $350M
LTM EBITDA: $70M

Total Debt / EBITDA = 5.0x
Secured Debt / EBITDA = 2.9x (more manageable at secured level)

This shows that $150M of unsecured debt is below the secured base.
```

### Bank Debt / EBITDA

**Definition:** Isolates exposure to bank lenders (revolving credit + term loans).

**Formula:**
```
Bank Debt / EBITDA
```

**Why it matters:**
- Banks typically require tighter leverage covenants
- Shows reliance on bank financing vs capital markets
- Indicates refinancing risk (banks can tighten terms)

**Practical Example:**
```
Company: Distribution Services
Revolving Credit: $50M (undrawn)
Term Loan: $150M
Senior Notes: $200M
Subordinated Notes: $100M
Total Debt: $450M
LTM EBITDA: $90M

Bank Debt / EBITDA = $150M / $90M = 1.7x
Total Debt / EBITDA = $450M / $90M = 5.0x

The company has modest bank leverage but high total leverage.
Bank covenant typical: Bank Debt / EBITDA < 2.5x
```

### Total Debt / Total Capitalization

**Definition:** Shows debt as a percentage of total capital (debt + equity).

**Formula:**
```
Total Debt / Total Capitalization = Total Debt / (Total Debt + Equity Value)
```

**Interpretation:**
- Equity value = market cap (for public companies) or investor valuation (private)
- Lower % = more equity cushion
- Higher % = more financial risk, less flexibility

**Practical Example:**
```
Company: Private Manufacturing Firm
Total Debt: $400M
Equity Value (per investor): $600M
Total Capitalization: $1,000M

Total Debt / Total Cap = $400M / $1,000M = 40%

This represents a moderate leverage structure with reasonable equity cushion.
```

### Debt / Equity Ratio

**Definition:** Simple measure of debt relative to equity value.

**Formula:**
```
Debt / Equity = Total Debt / Equity Value
```

**Interpretation:**
- For every $1 of equity, how much debt?
- Intuitive but less useful in leveraged finance (ratios like Debt/EBITDA preferred)

**Practical Example:**
```
Company: Software Reseller
Total Debt: $200M
Equity Value: $400M

Debt / Equity = $200M / $400M = 0.5x or 50%

For every dollar of equity, there's $0.50 of debt.
```

---

## Coverage Ratios

Coverage ratios measure how much cash flow is available to pay debt service. They answer: "Can the company pay its interest and debt obligations from operating cash flow?"

### EBITDA / Interest Expense

**Definition:** The primary coverage ratio. Shows how many times EBITDA covers annual interest.

**Formula:**
```
Interest Coverage = EBITDA / Interest Expense
```

**Interpretation:**
- For current benchmark ranges by rating, see `references/rating-agency-thresholds.md`
- <1.5x = distress risk (can't cover interest from operations)

**Practical Example:**
```
Company: Hospitality Group
LTM EBITDA: $150M
LTM Interest Expense:
  - Term Loan at 4%: $60M × 4% = $2.4M
  - Senior Notes at 5%: $100M × 5% = $5.0M
  - Sub Notes at 7%: $40M × 7% = $2.8M
Total Interest: $10.2M

EBITDA / Interest = $150M / $10.2M = 14.7x

This is very strong coverage. The company could cut EBITDA by 93%
and still cover interest from remaining operations.
```

### (EBITDA - CapEx) / Interest

**Definition:** More conservative; accounts for required capital spending.

**Formula:**
```
(EBITDA - CapEx) / Interest Expense
```

**Why it matters:**
- EBITDA includes all cash but doesn't account for capital investments
- Companies must reinvest to maintain operations and growth
- This ratio better reflects cash available for debt service

**Practical Example:**
```
Company: Manufacturing Business
LTM EBITDA: $100M
LTM Maintenance CapEx: $20M
LTM Interest Expense: $8M

Standard EBITDA / Interest = $100M / $8M = 12.5x (looks great)
(EBITDA - CapEx) / Interest = ($100M - $20M) / $8M = 10.0x (still strong)

The adjusted ratio better reflects sustainable coverage.
```

### EBITDA / (Interest + Required Debt Amortization)

**Definition:** Captures total debt service, not just interest.

**Formula:**
```
Total Debt Service Coverage = EBITDA / (Interest + Principal Repayment)
```

**Why it matters:**
- Must pay both interest AND principal
- Amortization schedules matter: steep amortization = high debt service
- This is the strictest coverage test for management flexibility

**Practical Example:**
```
Company: Business Services
LTM EBITDA: $80M
LTM Interest: $5M
Scheduled Amortization (Year 1): $12M
Total Debt Service: $5M + $12M = $17M

EBITDA / Interest = $80M / $5M = 16.0x (very loose)
EBITDA / Debt Service = $80M / $17M = 4.7x (tighter)

The debt service coverage shows meaningful annual amortization pressure.
```

### Fixed Charge Coverage Ratio

**Definition:** The strictest test. Includes interest, amortization, CapEx, taxes, and other fixed charges.

**Formula:**
```
Fixed Charge Coverage = EBITDA / (Interest + Principal + CapEx + Taxes + Other Fixed Charges)
```

**Interpretation:**
- Most conservative coverage test
- Gives clear picture of residual cash flow
- If this ratio is weak, company has limited flexibility

**Practical Example:**
```
Company: Specialty Chemicals
LTM EBITDA: $120M

Fixed Charges:
  Interest: $6M
  Debt Amortization: $15M
  Maintenance CapEx: $18M
  Cash Taxes: $12M
  Mandatory Pension Contributions: $3M
  Total Fixed Charges: $54M

Fixed Charge Coverage = $120M / $54M = 2.2x

After covering all fixed obligations, ~44% of EBITDA available for
growth investments, dividends, or additional debt repayment.
```

### Cash Interest vs Total Interest (PIK Consideration)

**Definition:** Distinguishes between cash interest (paid annually) and PIK interest (added to principal).

**Formula:**
```
Cash Interest Coverage = EBITDA / Cash Interest Expense
Total Interest Coverage = EBITDA / (Cash Interest + PIK Interest)
```

**Why it matters:**
- PIK (Payment-in-Kind) notes accrue interest that compounds on the principal
- PIK interest is NOT paid in cash but increases leverage
- Lenders focus on cash interest; equity holders should worry about total interest

**Practical Example:**
```
Company: Growth Technology Platform
LTM EBITDA: $60M

Interest Expense:
  Term Loan (cash): $3.0M
  Senior Notes (cash): $4.0M
  Subordinated Notes (50% PIK / 50% cash): $2.0M PIK + $2.0M cash
  Total Interest: $11M (of which $9M is cash)

Cash Interest Coverage = $60M / $9M = 6.7x (strong)
Total Interest Coverage = $60M / $11M = 5.5x (good)

PIK notes add $2M annual leverage growth beyond cash interest.
```

---

## Ratio Interpretation Framework: Rating Benchmarks

### Typical BB-Rated Companies (Investment Grade Risk)

**Leverage Ratios:**
- For current benchmark ranges by rating, see `references/rating-agency-thresholds.md`

**Credit Profile:** Adequate leverage, strong coverage, manageable debt service. Reasonable cushion for economic headwinds.

**Practical Example:**
```
Company: Large Telecom
Total Debt / EBITDA:     3.2x
Interest Coverage:       4.5x
FCF / Total Debt:        18%
Trends:                  Stable
Rating: BB / Stable Outlook
```

---

### Typical B-Rated Companies (Speculative Grade)

**Leverage Ratios:**
- For current benchmark ranges by rating, see `references/rating-agency-thresholds.md`

**Credit Profile:** Higher leverage, tighter coverage. Limited cushion. Vulnerable to revenue decline. Refinancing risk if market deteriorates.

**Practical Example:**
```
Company: Mid-Market Services
Total Debt / EBITDA:     4.8x
Interest Coverage:       3.0x
FCF / Total Debt:        10%
Trends:                  Stable (not improving)
Rating: B / Stable Outlook

Limited deleveraging. Dependent on stable/growing EBITDA.
```

---

### Typical CCC-Rated Companies (Distress Risk)

**Leverage Ratios:**
- For current benchmark ranges by rating, see `references/rating-agency-thresholds.md`

**Credit Profile:** High leverage, weak coverage. Significant distress risk. Limited margin for error. High default probability if business deteriorates. Refinancing dependent.

**Practical Example:**
```
Company: Struggling Retail
Total Debt / EBITDA:     6.5x
Interest Coverage:       1.8x
FCF / Total Debt:        5%
Trends:                  Deteriorating (revenue down, margins squeezed)
Rating: CCC / Negative Outlook

High distress risk. Limited deleveraging. Vulnerable to further decline.
Covenant violations likely if business continues to deteriorate.
```

---

## Cash Flow Ratios

Cash flow ratios measure how quickly the company can reduce debt from operating cash generation.

### FCF / Total Debt (Deleveraging Capacity)

**Definition:** Shows what percentage of debt can be repaid annually from free cash flow.

**Formula:**
```
FCF / Total Debt = Free Cash Flow / Total Debt
```

**Interpretation:**
- >20% = strong deleveraging (rapid paydown)
- 10-20% = solid deleveraging
- 5-10% = modest deleveraging
- <5% = slow deleveraging / refinancing dependent

**Practical Example:**
```
Company: Industrial Services
LTM Free Cash Flow: $50M
Total Debt: $400M

FCF / Total Debt = $50M / $400M = 12.5%

This means the company can pay down 12.5% of debt annually from FCF
(assuming no growth investments, dividends, or acquisitions).
At this rate, debt would be eliminated in ~8 years.
```

### Retained Cash Flow / Total Debt

**Definition:** FCF after dividends. Shows deleveraging capacity after shareholder distributions.

**Formula:**
```
Retained Cash Flow / Total Debt = (FCF - Dividends) / Total Debt
```

**Why it matters:**
- Equity sponsors often take dividends, reducing deleveraging capacity
- Shows true debt repayment after sponsor distributions
- Often much lower than FCF / Total Debt for dividend-paying sponsors

**Practical Example:**
```
Company: Telecom Platform (Sponsor-owned)
LTM FCF: $80M
Annual Dividend to Sponsor: $40M
Retained Cash Flow: $40M
Total Debt: $500M

FCF / Total Debt = $80M / $500M = 16% (looks okay)
Retained FCF / Total Debt = $40M / $500M = 8% (slower deleveraging)

Sponsor distributions cut deleveraging by half. This is typical
in sponsor-owned deals where sponsors prioritize returns.
```

### (EBITDA - CapEx) / Total Debt

**Definition:** Another version of cash flow leverage; uses normalized sustainable cash flow.

**Formula:**
```
(EBITDA - CapEx) / Total Debt
```

**Practical Example:**
```
Company: Infrastructure Provider
LTM EBITDA: $200M
Normalized CapEx (% of revenue maintenance): $40M
Total Debt: $600M

(EBITDA - CapEx) / Debt = ($200M - $40M) / $600M = 26.7%

Annual sustainable cash available for debt service and other uses.
```

### FCF Yield on Debt

**Definition:** What return does the credit investor earn from cash flow perspective?

**Formula:**
```
FCF Yield = FCF / Total Debt
```

**Interpretation:**
- Similar to FCF / Total Debt but phrased as a yield perspective
- Tells debt investor how much cash is being generated per dollar of debt
- Higher yield = more attractive from credit perspective

**Practical Example:**
```
Company: Logistics Network
LTM FCF: $120M
Total Debt: $800M
FCF Yield = $120M / $800M = 15%

From a debt perspective, the company generates 15% annual cash return
on the debt principal. This is attractive for credit investors.
```

---

## Enterprise Value Ratios

Enterprise value (EV) ratios measure total firm value relative to cash flow and compare debt across companies with different equity values.

### Enterprise Value Definition

**Formula:**
```
Enterprise Value (EV) = Market Cap + Total Debt - Cash
```

**Components:**
- **Market Cap** = stock price × shares outstanding (or investor valuation for private companies)
- **Total Debt** = all interest-bearing obligations
- **Cash** = cash and equivalents (sometimes less restricted cash)

**Why it matters:**
- Normalizes firm value by removing capital structure
- Enables comparison across companies with different leverage
- Foundation for valuation multiples (EV/EBITDA, EV/Revenue)

### EV / EBITDA (Valuation Multiple)

**Definition:** Total firm value relative to cash flow generation.

**Formula:**
```
EV / EBITDA = Enterprise Value / EBITDA
```

**Interpretation:**
- Valuation multiple: how much the market pays for each dollar of EBITDA
- Industry-dependent: industrials typically 8-12x; software typically 15-25x
- Lower multiples = cheaper / more value; higher = premium/growth
- Used to value companies and as benchmark for M&A pricing

**Practical Example:**
```
Company: Industrial Distribution
Market Cap: $1,200M
Total Debt: $800M
Cash: $150M
Enterprise Value: $1,200M + $800M - $150M = $1,850M
LTM EBITDA: $250M

EV / EBITDA = $1,850M / $250M = 7.4x

If comparable companies trade at 8-9x EV/EBITDA, this target
appears undervalued (good investment opportunity).
```

### Market-Adjusted Debt (MAD)

**Definition:** Weights each debt tranche by its market trading price for more conservative analysis.

**Formula:**
```
Market-Adjusted Debt = Σ(Face Value × Market Trading Price %)
```

**Why it matters:**
- Face value assumes 100% recovery; unrealistic in distress
- Trading prices reflect market's true valuation of each tranche
- Subordinated debt trading at 60¢ should be counted as $60M, not $100M
- More conservative than face-value analysis

**Practical Example:**
```
Company: Struggling Retail Chain
Debt tranches and market prices:

Term Loan: $200M face, trading at 95¢ → $190M MAD
Senior Notes: $150M face, trading at 85¢ → $127.5M MAD
Sub Notes: $100M face, trading at 50¢ → $50M MAD
Total Face Value: $450M
Market-Adjusted Debt: $367.5M

LTM EBITDA: $75M

Face Value Leverage: $450M / $75M = 6.0x
Market-Adjusted Leverage: $367.5M / $75M = 4.9x

The market-adjusted approach gives a more realistic picture
of what debt is truly worth if repaid.
```

### TEV Cushion (Equity Cushion)

**Definition:** Measures equity value as a cushion protecting debt from losses.

**Formula:**
```
TEV Cushion = (TEV/EBITDA - Net Debt/EBITDA) / (TEV/EBITDA)
           = (Equity Value / Enterprise Value)
```

**Interpretation:**
- Shows what % of enterprise value belongs to equity holders
- Higher = more equity cushion = safer credit
- Lower = less cushion = equity is thin

**Practical Example:**
```
Company: Software Services
EV / EBITDA: 10.0x
Net Debt / EBITDA: 3.5x
TEV Cushion: (10.0 - 3.5) / 10.0 = 65%

Or alternatively:
Enterprise Value: $500M
Equity Value: $325M
TEV Cushion: $325M / $500M = 65%

Equity holders have 65% of the pie; debt holders have 35%.
Strong cushion. Debt can absorb 65% loss of EV before writing down.
```

---
