---
last_updated: "2026-03-21"
---

## Part 4: Preparing a Credit Snapshot

### Purpose: Rapid Triage Framework

A credit snapshot is a structured analysis designed to quickly assess a credit's health. It answers:
- **Can this company service its debt?**
- **Are there imminent liquidity issues?**
- **What could go wrong, and how soon?**

Use this framework as your first pass. Deeper dives are guided by what you find.

### Step-by-Step Credit Snapshot

#### Step 1: Context — Why Are You Looking at This?

Before diving into financials, understand your goal:
- **New issuance**: Is this a new investment opportunity?
- **Price drop**: Did the bond drop 5 points overnight? Something happened.
- **Portfolio review**: Routine review of a holding.
- **Event analysis**: Maturity coming, covenant step-down, or rumored M&A.

Your purpose drives which analyses matter most.

#### Step 2: The Business — Elevator Pitch

Document in one paragraph:
- **Industry**: What sector?
- **Business model**: How does it make money? (Subscription, transactional, asset-based?)
- **Competitive position**: #1, fragmented, consolidating?
- **Key drivers**: What makes revenue grow or contract?

**Example:**
"ABC Telecom is the 3rd-largest wireless carrier in region. Subscription model with 8M subscribers. Growing through fixed-line broadband expansion. Competes with two larger incumbents and faces pressure from MVNO (virtual operators). Key metrics: subscriber growth, ARPU (average revenue per user), churn."

#### Step 3: Debt Capitalization Table

List every debt instrument:

| Tranche | Type | Amount ($M) | Coupon | Maturity | Status |
|---------|------|----------|--------|----------|--------|
| Term Loan | Secured | 200 | L+3.5% | 2027 | 1st lien |
| Sr Notes | Unsecured | 300 | 7.5% | 2029 | Sr unsec |
| Sr Sub Notes | Unsecured | 150 | 9.0% | 2032 | Sr sub |
| Revolver | Secured | 75 | L+2.5% | 2026 | Undrawn |

**Also document:**
- **Cash balance**: Amount on balance sheet
- **Revolver availability**: Can this liquidity be tapped?
- **Maturities by year**: Is there a maturity wall?

#### Step 4: Statement of Cash Flows

Analyze the last 4 quarters (LTM) or full year:

| Line Item | Amount ($M) | % of Revenue |
|-----------|----------|----------|
| Operating Cash Flow (CFO) | 85 | 12.0% |
| Less: CapEx | (45) | (6.4%) |
| **Free Cash Flow** | **40** | **5.6%** |
| Debt Service (Principal + Interest) | (35) | (4.9%) |
| **FCF after Debt Service** | **5** | **0.7%** |

**Key questions:**
- Is CFO positive? (Negative CFO = company is burning cash operationally)
- What's CapEx as % of revenue? (Asset-intensive businesses need high CapEx)
- After debt service, is there excess cash to reduce debt, pay dividends, or cover contingencies?

#### Step 5: LTM Adjusted EBITDA and Key Ratios

Build a simple table:

| Metric | LTM | Prior Year | Change |
|--------|-----|-----------|--------|
| Revenue | 710 | 680 | +4.4% |
| EBITDA (reported) | 145 | 138 | +5.1% |
| Adjustments | 12 | 10 | — |
| **Adjusted EBITDA** | **157** | **148** | **+6.1%** |
| Total Debt | 500 | 480 | +4.2% |
| Cash | (20) | (15) | — |
| **Net Debt** | **480** | **465** | +3.2% |
| **Net Debt / EBITDA** | **3.1x** | **3.1x** | Flat |

**Calculate immediately:**
- **Debt/EBITDA** (total and net): Leverage metric
- **EBITDA-CapEx / Interest**: Cash available to pay interest
- **FCF / Total Debt**: Debt repayment capacity

**Rules of thumb:**
- Net Debt > 5.0x: High leverage; tight covenants or company must deleverage
- Net Debt 3.0x-5.0x: Moderate leverage; manageable if business is stable
- Net Debt < 3.0x: Conservative; company has refinancing flexibility
- EBITDA-CapEx / Interest < 1.5x: Interest coverage is tight; risk if EBITDA declines

#### Step 6: Enterprise Value Analysis (If Public)

If the company has a public stock:

```
Market Cap = Share Price × Shares Outstanding = $40 × 50M = $2,000M
Plus: Total Debt = 500M
Less: Cash = (20M)
Enterprise Value = $2,480M

TEV / EBITDA = $2,480M / $157M = 15.8x
```

**Sanity check:**
- Is 15.8x reasonable for this industry? (Telecom average might be 7-8x)
- Is this company's multiple higher or lower than peers? Why?
- Does the equity value make sense relative to the business quality?

If the TEV multiple is very high, equity holds a lot of value and bonds are safer (equity cushion is large).
If the TEV multiple is very low, equity is cheap/distressed and bonds may be at risk (equity cushion is small).

#### Step 7: Initial Assessment Checklist

- [ ] Is cash flow positive or negative?
- [ ] Are there maturities due in the next 24 months?
- [ ] Is leverage stable, rising, or falling?
- [ ] Is the business growing, flat, or declining?
- [ ] Are there obvious liquidity issues?
- [ ] Does the capital structure make sense? (Or are there structural issues?)

**Based on findings, proceed with deeper analysis:**

### When to Deepen Your Analysis

#### **If: Cash flow is negative OR maturities are looming → Detailed Liquidity Analysis**

Build a liquidity waterfall:

```
Cash on hand: $20M
Plus: Revolver availability: $75M
Plus: Operating CFO (next 12M forecast): $85M
Less: CapEx: $(45M)
Less: Interest and debt service: $(35M)
Less: Other uses (dividends, M&A): $(10M)
Cumulative: $90M available

Upcoming maturities (next 24M): $65M
Refinancing need coverage: 1.4x
```

If liquidity coverage is less than 1.2x, refinancing risk is material.

#### **If: Business appears stable → Operating Trend Analysis**

Compare revenue, EBITDA, and margin trends:

| Quarter | Revenue | YoY Growth | EBITDA Margin | Trend |
|---------|---------|-----------|---------------|-------|
| Q1 2024 | 165 | +2% | 21% | Stable |
| Q2 2024 | 168 | +3% | 21% | Stable |
| Q3 2024 | 172 | +4% | 22% | Improving |
| Q4 2024 | 175 | +5% | 22% | Improving |

**What changed?** Did margins improve due to operational discipline, or just leverage from existing scale? Is the business normalizing after a downturn?

#### **If: Examining a specific debt instrument → Structural and Covenant Analysis**

1. **Seniority**: Is this debt 1st lien (has priority claim on assets) or unsecured?
2. **Covenants**: What are the financial maintenance tests?
3. **Baskets**: What exceptions exist? Can the company still pay dividends? Issue more debt?
4. **Call features**: When can this debt be refinanced?
5. **Cross-default**: If one debt tranche defaults, do all tranches default?

#### **If: Margins or costs are volatile → Margin and Cost Trend Analysis**

Break EBITDA into its components:

| Year | Revenue | COGS | Gross Margin % | OpEx | EBITDA | EBITDA Margin % |
|------|---------|------|----------------|------|--------|-----------------|
| 2022 | 650 | 455 | 30% | 95 | 100 | 15.4% |
| 2023 | 680 | 478 | 29.7% | 100 | 102 | 15.0% |
| 2024 LTM | 710 | 497 | 30.0% | 108 | 105 | 14.8% |

**Observations:**
- COGS as % of revenue has stabilized (good)
- OpEx is growing faster than revenue (negative)
- EBITDA margin is declining despite revenue growth (margin compression)

Why is OpEx growing? Are headcount, rent, or other fixed costs rising? Can management control this?

#### **If: Ownership has changed or incentives matter → Ownership Assessment**

1. **Sponsor ownership**: If owned by a PE firm, what's the fund timeline? Exit pressure?
2. **Management incentives**: Do managers have equity stakes? (Aligns interests)
3. **Dividend policy**: Is the company paying out cash? To whom?
4. **Insider trading**: Are executives buying or selling stock?

#### **If: Maturity approaching or covenant step-down imminent → Upcoming Events**

1. **Maturity**: Can the company refinance? Is there a refinancing market for this credit?
2. **Covenant step-downs**: Are leverage tests becoming tighter? Will the company breach?
3. **Peer performance**: How are comparable companies performing? (Affects refinancing ability)
4. **Market conditions**: Is the HY market open or closed? Does that matter for this refinancing?

---
