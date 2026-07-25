---
last_updated: "2026-03-21"
---

## Part 2: Precedent Transactions Analysis ("Deal Comps")

Values a company based on what acquirers actually paid for comparable businesses in M&A transactions. More relevant for establishing acquisition value (includes control premium) versus market value.

### Core Concept

While trading comps show what public markets pay for *minority stakes*, precedent transactions show what *acquirers* paid to gain *control*. The difference is the **control premium**.

### Step 1: Select Comparable Transactions

**Screening Criteria:**
- **Timeframe**: Last 3–5 years (older deals less relevant to current market)
- **Target size**: Enterprise value within 0.5x to 3.0x of target's size
- **Sector**: Same or adjacent industry; similar business model
- **Geography**: Same market or similar macro conditions
- **Deal type**: Pure strategic vs. financial buyer; auction vs. bilateral negotiation (auctions yield higher prices)
- **Completion status**: Focus on *closed* transactions (signed multiples can drop between announcement and close)

**Sources:**
- Merger proxies (DEFM14A or S-4 filings with acquisition data)
- Form 8-K filings (acquisition announcements)
- Press releases from acquirer/target
- Merger data providers: Bloomberg, Dealogic, Refinitiv, CapitalIQ
- Investment bank pitchbooks and research reports

### Step 2: Locate Transaction Data

For each transaction, extract:

**Deal Economics:**
- **Announcement date** and close date
- **Form of consideration**: Cash, stock, or mixed (can affect tax and valuation)
- **Target Enterprise Value**: Total cash paid (TEV), less target's net debt at close
- **Target financials at announcement**: Use LTM or NTM consensus if available (pre-synergy basis)
- **Deal premium**: Offer price vs. stock price 1 day before, 1 week before, 1 month before announcement (standard benchmarks: 30% typical for public companies)

**Transaction Structure:**
- Debt assumed (if any)
- Earnouts, deferred payments (must be included in TEV)
- Seller financing (if any)
- Non-cash payments

### Step 3: Calculate Transaction Multiples

**Standard Multiples:**
```
TEV / LTM EBITDA    — Most important (primary leverage metric at close)
TEV / LTM Revenue   — Revenue-based
TEV / NTM EBITDA    — Forward-looking (if consensus available at announcement)
Deal Premium        — Offer price vs. unaffected stock price (1-day standard)
```

**Example:**
```
Target acquisition by Buyer Inc.
  Announcement: 100M shares at $50/share = $5,000M equity consideration
  Assume target debt = $500M, cash = $100M
  TEV = $5,000M + $500M - $100M = $5,400M

  Target LTM EBITDA at announcement = $600M
  TEV / LTM EBITDA = $5,400M / $600M = 9.0x

  Unaffected stock price (1 day prior) = $42.50
  Deal Premium = ($50 - $42.50) / $42.50 = 17.6%
```

### Step 4: Apply to Target and Adjust for Context

**Determine Valuation Range:**
```
Calculate mean/median TEV/EBITDA from transaction set
Apply to target's EBITDA
Example: Median Deal Multiple = 9.0x; Target EBITDA = $200M
Implied TEV = $1,800M
```

**Key Adjustments:**

1. **Control Premium**: Precedent transactions *include* control premium (15–40% for public targets, higher in competitive auctions). If comparing to trading comps, reconcile the difference.
   ```
   Control Premium = (Deal Multiple - Trading Comp Multiple) / Trading Comp Multiple
   Typical: 20–30% control premium for strategic deals; up to 50%+ in auction situations
   ```

2. **Buyer Type**: Strategic buyers can pay higher multiples than financial buyers (PE firms) due to synergies.
   - Strategic-to-Strategic deals: highest multiples
   - Strategic-to-Financial: mid-range
   - Financial-to-Any: lowest multiples (must make economic sense on a standalone basis)

3. **Market Conditions**: Adjust if market environment significantly different (low rates enabled higher leverage in 2015–2020; high rates compress valuations today).

4. **Competitive vs. Bilateral**: Auction/competitive situations drive multiples 10–20% higher than bilateral negotiations.

---
