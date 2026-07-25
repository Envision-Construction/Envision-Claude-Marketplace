---
last_updated: "2026-03-21"
---

## Part 1: Comparable Companies Analysis ("Trading Comps")

The most widely used valuation methodology in investment banking. Provides a market-based range by analyzing how similar publicly traded companies are currently valued in the market.

### Core Concept

Trading comps answer: "What is the market currently willing to pay for similar businesses?" By identifying comparable companies and measuring their trading multiples, you establish a reference frame for what your target company should be worth.

### Step 1: Select the Comparable Universe

**Screening Criteria:**
- **Business description**: Same product/service focus; similar revenue models (subscription vs. transactional, B2B vs. B2C)
- **Sector/Sub-sector**: Direct competitors preferred; adjacent businesses acceptable if similar economics
- **Size**: Revenue within 0.5x to 3.0x of target (to match financial/operational maturity)
- **Growth profile**: Similar growth rates (both mature, both hyper-growth, etc.); high-growth and stable companies trade at different multiples
- **Margin profile**: EBITDA/Operating margins should be comparable
- **Geographic mix**: Geographic mix and exposure to same macro risks
- **Customer base**: Concentrated vs. diversified; large customers vs. SMB exposure

**Universe Size:**
- Narrow "core comps" (3–5 closest): tightest valuation range but limited sample size
- Broader universe (10–15 total): better diversification but wider dispersion

**Sources:**
- SEC filings (10-K annual, 10-Q quarterly, proxy statements)
- Equity research reports and consensus estimates
- Bloomberg terminal, CapitalIQ, Refinitiv Eikon
- Industry reports and trade publications
- Press releases and investor presentations

### Step 2: Locate Necessary Financial Information

For each comparable company, gather:

**Stock Market Data:**
- Current stock price (use most recent close)
- Shares outstanding (basic shares per latest 10-Q)
- Dilutive securities (in-the-money options, warrants, RSUs, convertibles)

**Debt & Other Obligations:**
- Total debt (current + long-term)
- Cash and cash equivalents
- Preferred stock outstanding
- Minority interest (non-controlling interests in subsidiaries)
- Operating lease obligations (if applicable, may be capitalized under ASC 842)

**Financial Data:**
- Last Twelve Months (LTM): Revenue, EBITDA, EBIT (operating income), Net Income
- Next Twelve Months (NTM): Consensus estimates from I/B/E/S, FactSet, or Bloomberg
- Capital expenditures (annual and as % of revenue)
- Depreciation & amortization (D&A)
- Effective tax rate
- Working capital metrics (if material)

**Calendarization Note:** If comps have staggered fiscal year-ends, adjust to a common period using weighted averages of partial periods.

### Step 3: Calculate Enterprise Value and Multiples

**Fully Diluted Shares Outstanding (Treasury Stock Method):**
```
Basic Shares Outstanding
  + In-the-Money Options/RSUs/Warrants
    (# Options × % exercised, using treasury stock method)
    Treasury Stock Method = Options - (Options × Strike Price / Current Price)
  + Convertible Securities (if any)
  = Fully Diluted Shares Outstanding
```

**Enterprise Value Calculation:**
```
Equity Value = Current Stock Price × Fully Diluted Shares Outstanding

Enterprise Value (TEV) = Equity Value
                      + Total Debt
                      + Preferred Stock
                      + Minority Interest
                      - Cash & Cash Equivalents
                      - Other Non-Operating Assets
```

**Key Trading Multiples:**

| Multiple | Formula | When to Use | Strengths | Limitations |
|----------|---------|-------------|-----------|-------------|
| **EV / Revenue** | TEV / Revenue | Pre-profit, high-growth, or SaaS companies | Less subject to D&A or tax manipulation | Ignores profitability entirely; wide ranges common |
| **EV / EBITDA** | TEV / EBITDA | **Primary in leveraged finance**; mature companies | Compares operations regardless of capital structure or tax rate; capital-structure neutral | EBITDA can be adjusted; hides CapEx requirements |
| **EV / EBIT** | TEV / EBIT | Comparing companies with different D&A impact | Accounts for depreciation differences | Less commonly used; EBIT can be volatile |
| **EV / (EBITDA - CapEx)** | TEV / (EBITDA - CapEx) | Capital-intensive industries (industrials, utilities) | Captures true cash-generative ability | Requires normalization of CapEx |
| **P / E** | Stock Price / EPS | Mature, stable-earnings companies | Equity perspective; reflects leverage impact | Distorted by capital structure, tax rate, D&A |
| **P / BV** | Stock Price / Book Value | Financial institutions, asset-heavy businesses | Accounts for balance sheet; useful for banks | Requires high ROE to be meaningful |

**Example Calculation:**

```
Company ABC:
  Stock Price: $50.00
  Shares Outstanding (basic): 100M
  Options (in-the-money): 5M shares at $40 strike
  Total Debt: $500M
  Cash: $100M
  Minority Interest: $20M

Treasury Stock Calculation:
  Options Proceeds = 5M × $40 = $200M
  Shares Repurchased = $200M / $50 = 4M shares
  Net Dilution = 5M - 4M = 1M shares

Fully Diluted Shares = 100M + 1M = 101M

Equity Value = $50 × 101M = $5,050M
Enterprise Value = $5,050M + $500M + $20M - $100M = $5,470M

If EBITDA = $640M:
  EV / EBITDA = $5,470M / $640M = 8.5x
```

### Step 4: Analyze and Benchmark

**Create Summary Statistics:**
- Mean, median, high, low for each multiple
- Standard deviation (if dispersion is high, investigate outliers)
- Quartiles (Q1, Q3) to identify outlier comps

**Identify "Closest Comps":**
- 3–5 most similar companies by business model, size, growth
- Narrow range from this subset for tighter valuation

**Apply to Target Company:**
```
Target EBITDA = $200M
EV / EBITDA Range (from comps) = 8.0x – 9.0x (median 8.5x)
Implied Enterprise Value = $1,600M – $1,800M (midpoint $1,700M)
```

**Reconcile Across Multiples:**
- If EV/EBITDA and EV/Revenue imply very different valuations, investigate
- Check historical multiples for each comp (are they anomalously high/low today?)
- Assess market sentiment (bull vs. bear markets drive multiple compression/expansion)

---

## Valuation Integration: Football Field Summary

### Quick Reference: Valuation Methods

| Methodology | Entry Point | Output | Best For | Key Assumption |
|---|---|---|---|---|
| **Trading Comps** | Public-market peer set | Market value range | Relative value and sentiment cross-check | Peer set is truly comparable |
| **Precedent Transactions** | Relevant deal set | Control-value range | Acquisition context and control premium framing | Deal vintage is comparable to the current environment |
| **DCF** | Historical plus projected cash flows | Intrinsic value range | Long-duration value framing | Discount rate and terminal assumptions are credible |
| **LBO Analysis** | Debt capacity plus sponsor case | Financial-buyer range | Sponsor behavior and downside support | Leverage, exit, and return hurdles fit the deal environment |

Use `references/market-benchmarks.md` and `references/typical-deal-parameters.md` to calibrate market-sensitive inputs rather than treating any single range as permanent.

Present all valuation methodologies side by side as horizontal bars to show the "fair value range."

### Visual Summary

```
Valuation Methodology     Low ($M)    Mid ($M)   High ($M)
------------------------------------------------------------
Trading Comps (EV/EBITDA) 8.0x-9.5x
                          ================|
                          $1,600M          $1,900M

Precedent Transactions    9.0x-10.0x  [includes control premium]
                              |-----------------|
                              $1,800M           $2,000M

DCF (10% WACC)           PV of cash flows + Terminal Value
                            |------------------|
                            $2,100M            $2,450M

LBO Analysis (Max Price)   Sponsor returns 20%+ IRR
                          |-------------|
                          $1,700M       $2,100M

52-Week Trading Range     $45 - $53 per share
                          |----------------------|
                          $1,350M               $1,590M

Wall Street Consensus     Sell $42, Hold $50, Buy $58
                          |------------------------|
                          $1,260M                 $1,740M

------------------------------------------------------------
Implied Valuation Range                   $1,600M - $2,400M
Suggested Offer Price (Control Premium)   $1,800M - $2,100M
```

### Interpretation

- **Trading Comps**: Market's current view (minority interest premium implicit)
- **Precedent Transactions**: What acquirers typically pay (includes control premium)
- **DCF**: "Intrinsic value" based on fundamentals
- **LBO**: Maximum price a financial buyer can pay and achieve target returns
- **Consensus**: Blended view from all methodologies

A well-executed valuation uses all four methods to triangulate "fair value."

---

### Key Takeaways & Best Practices

**1. No Single Method is Sufficient**

Always use **multiple approaches** and triangulate:
- If all four methods cluster around $2.0B, high confidence
- If DCF says $2.5B but comps say $1.8B, investigate the gap
  - Is terminal growth assumption too high?
  - Are comps trading at an anomalous multiple?
  - Are synergies significant but not captured in DCF?

**2. Understand What Each Method Values**

```
Trading Comps           -> Minority interest (market view); capital-structure neutral
Precedent Transactions  -> Control interest; includes strategic buyer premiums
DCF                     -> Intrinsic value; independent of market sentiment
LBO                     -> Financial buyer's maximum willingness to pay
```

**3. Trading Comps vs. Precedent Transactions**

- Precedent multiples typically 15-40% *higher* than trading comps due to control premium
- Control Premium = (Deal Multiple - Trading Multiple) / Trading Multiple
- When comparing, adjust for this structural difference

**4. Terminal Value Dominates DCF**

- TV typically 60-80% of total DCF value
- Small changes in exit multiple or terminal growth rate swing valuation significantly
- Always stress-test: vary exit multiple +/-0.5-1.0x, vary terminal growth +/-0.5-1.0%
- Use both exit multiple *and* perpetuity growth methods; cross-check results

**5. LBO Sets the "Floor" Price**

- PE firm will not pay above price that doesn't deliver 20%+ IRR
- If LBO IRR is 18% at $2.0B entry price, sponsor won't bid above (unless forced into competitive auction)
- Strategic buyers can pay more than PE firms due to synergies

**6. Sources Must Equal Uses in LBO**

- If you can't balance sources and uses, adjust:
  - Increase debt (higher leverage -> higher returns but more risk)
  - Decrease entry price
  - Increase equity sponsor check
  - Reallocate transaction fees or other uses

Sponsor equity is typically the "plug" that balances the model.

**7. IRR and MOIC Both Matter**

- High IRR on small equity check may be less attractive than lower IRR on larger check
- A $100M sponsor equity investment with 30% IRR = $3.4x MOIC (5 years)
- A $200M sponsor equity investment with 25% IRR = $2.7x MOIC (5 years)
- Investors typically target BOTH minimum IRR (e.g., 20%) AND minimum MOIC (e.g., 2.0x)

**8. Value Creation Sources in LBO**

Sponsor returns come from:
1. **EBITDA Growth** (operational improvement, market growth, synergies)
2. **Multiple Expansion** (exit at higher multiple than entry, if market conditions permit)
3. **Debt Paydown** (FCF reduces debt, amplifying equity returns on smaller equity base)
4. **Dividend Recaps** (refinancing to extract cash during hold; adds to returns but increases leverage/risk)

Most value typically comes from debt paydown and EBITDA growth; multiple expansion is opportunistic.

**9. Key Formulas to Memorize**

```
EV = Equity Value + Debt - Cash

Unlevered FCF = EBIT(1-T) + D&A - CapEx - Change in NWC

WACC = E/V x Cost of Equity + D/V x Cost of Debt x (1-T)

Cost of Equity = Rf + Beta x ERP + Size Premium

Terminal Value (Exit Multiple) = Terminal Year EBITDA x Multiple

Terminal Value (Perpetuity) = Terminal Year UFCF x (1+g) / (WACC - g)

MOIC = Exit Equity Value / Entry Equity Value

IRR = Solve for discount rate where PV(Inflows) = PV(Outflows)
```

**10. Common Valuation Pitfalls to Avoid**

- **Over-reliance on DCF alone**: If all other methods suggest $1.8B but DCF says $2.5B, don't ignore the gap
- **Not normalizing EBITDA**: Add back one-time charges, management perks, non-recurring items
- **Using effective tax rate instead of marginal**: Distorts WACC and DCF calculations
- **Forgetting working capital**: Negative working capital swings can eliminate year's FCF
- **Not stress-testing terminal assumptions**: Terminal value is 60-80% of DCF; small changes = big impact
- **Applying precedent multiples to minority stake context**: Control premium makes them too high
- **Under-estimating deal costs**: Transaction and financing fees can be 3-5% of deal size
- **Ignoring debt covenants**: High leverage may trigger financial covenants, constraining operations
- **Assuming linear debt paydown**: Paydown accelerates as cash flow improves; manually model each tranche

---
