---
last_updated: "2026-03-21"
---

## Maturities, Calls, and Puts

The call schedule and maturity structure define when debt can be retired, refinanced, or forced repayment, and at what cost.

### Typical Maturities

**Bank Loans**
- Maturity: 5–7 years from closing, typically shorter than bonds
- Amortization: Usually 0–2% annually before final balloon
- Refinancing: Often refinanced before maturity when company has deleveraged

**High-Yield Bonds**
- Maturity: 7–10 years from issuance, with some 12-year bonds (rare)
- Bullet maturity: Most HY bonds are bullets (full repayment at maturity), not amortizing
- Refinancing risk: If company hasn't deleveraged sufficiently, may face expensive or impossible refinancing near maturity

### Call Schedules and Protections

**Noncall Period (Most Common)**
- Typical structure: Noncall for 2–5 years (e.g., "NC3" = noncall for 3 years)
- Benefit: Investor has "call protection"—issuer cannot force early repayment during this period
- After NC period: Call schedule with declining call premiums
- Example:
  - Years 0–3: Noncall (NC3)
  - Year 3: Callable at 105 (par + 5%)
  - Year 4: Callable at 102.5
  - Year 5: Callable at 101
  - Year 6+: Callable at par (100)

**Call Premium**
- Definition: Premium over par paid by issuer to call a bond early
- Typical structure: Call premium ≈ half the coupon in year 1, declining annually
- Example: 9% coupon → Year 3 call premium ≈ 4.5%–5%, declining to par by year 6–7
- Purpose: Protects investors from call risk in early years; issuer can call cheaper when refinancing environment improves

**Noncall-for-Life (NCL)**
- Definition: Bond cannot be called for any reason over its entire life
- More common in: Investment-grade bonds, higher-quality HY
- Cost to issuer: Higher coupon (50–100bp premium) to compensate investor for lack of call risk
- Investor benefit: Keeps upside if spreads compress; cannot be forced out of investment at inopportune time

**Make-Whole Call**
- Definition: Issuer can call bond anytime, but must pay Treasury yield + fixed spread (usually 50bp)
- Pricing: Call price = (PV of all remaining coupons discounted at Treasury yield + spread) + (PV of par discounted at Treasury yield + spread)
- Mechanics: Available on nearly all high-yield bonds; most expensive form of call for issuer
- Example: 8% bond due 2032. Treasury yield on 2032 curve = 3.5%. Make-whole call price = PV of all future coupons at 4.0% + PV of par at 4.0%. If bond is trading well above par, call price is steep.
- Benefit to issuer: Can refinance anytime without waiting for scheduled call date (if refinancing environment improves dramatically)
- Benefit to investor: Provides "upside" scenario—if refinancing is attractive to issuer, investor gets called at a favorable price

**10% Annual Call**
- Definition: Issuer can call up to 10% of original issue amount per year at 103 (3% premium to par)
- Common in: Senior secured bonds, bonds structured to replace bank debt
- Purpose: Allows sponsor-driven deleveraging (reducing debt) without full refinancing
- Mechanics: Company uses excess cash flow or asset sales to pay down top of debt structure
- Covenant requirement: May require "no more than 2% of original issue outstanding" tests or "maintain minimum leverage ratio"
- Example: $500M original issuance. Each year, company can call up to $50M at 103. Over 10 years, $500M can be paid down incrementally.

**Equity Clawback**
- Definition: Issuer can call up to 35% (sometimes 30%) of original issue amount using proceeds from equity offerings
- Call price: Typically ~110% of par, available only in first 3 years
- Mechanics: When equity raises capital (IPO, secondary offering), proceeds can be deployed to buy bonds at clawback price
- Constraint: At least 65% of original issue must remain outstanding after clawback
- Benefit to issuer: Allows equity raise to strengthen balance sheet; can "reprice" debt earlier
- Benefit to investor: Equity clawback usually priced at meaningful premium (110% vs. make-whole ~105%), incentivizing participation
- Example: $200M original issue. Sponsor sponsors secondary at IPO, raises $100M. Uses $35M (clawback cap = 35% × $200M = $70M, but only $35M raised) to call bonds at 110%.

### Mandatory Prepayments and Sweeps

**Cash Flow Sweep**
- Definition: When company generates excess free cash flow, percentage (typically 50%) must be used to prepay debt
- Mechanics: Calculated annually post-refinancing or post-add-on. If FCF > certain threshold, 50% of excess prepays debt (usually pro rata across tiers, often "last out" structure)
- More common in: Bank loans and covenant-heavy deals
- Less common in: Senior unsecured bonds (investor-friendly)
- Benefit to lenders: Reduces leverage mechanically as company deleverages
- Downside to bondholders: Reduces upside if company outperforms; prepayment is pro rata (pro rata = all bonds prepaid equally, not "first out")
- Example: Company projects EBITDA = $400M, interest = $100M, capex = $50M, working capital change = $20M. FCF = $230M. If threshold is $50M, excess = $180M. 50% sweep = $90M prepayment.

### Refinancing and Repayment Mechanics

**Open-Market Repurchases**
- Definition: Company buys bonds in secondary market at current market price (typically at discount if spreads have widened)
- Covenant requirement: Usually allowed if company maintains leverage ratio (e.g., Net Leverage < 4.0x) OR in "Excess Cash Flow" basket
- Pricing: If bonds trading at 85 cents on dollar, company buys at 85 and realizes gain
- Restriction: Cannot typically apply to bank loans (pro rata requirement—bank group must approve prepayment)
- Tax impact: Issuer may realize gain if bought below original issue price; bondholder realizes realized loss if bought at discount
- Strategic use: Buyback when bonds are trading cheap; refinancing risk is high; strong FCF generation
- Example: $100M bond trading at 85. Company buys $50M in open market for $42.5M. Realizes $7.5M gain. Reduces outstanding to $50M.

**Tender Offer**
- Definition: Company makes formal offer to all bondholders to sell bonds at specified price and deadline
- Mechanics: Typically combined with "consent solicitation" (asking bondholders to amend covenants)
- Incentive: "Call premium" or "tender premium" (e.g., offering 102 for bonds trading at par)
- Use case: Refinancing at lower coupon; removing covenants; changing maturity
- Consent mechanics: Holders who tender often receive additional consideration for consenting to amendments
- Example: Offer to tender 2028 bond at 103 in exchange for new 2035 bond at 6% coupon (vs. original 9%). Combined with consent to strip certain financial maintenance covenants.

**Refinancing Analysis (Callable Bonds)**
- General principle: Issuer will call a bond if refinancing cost < benefit of retirement
- Calculation: Compare after-tax cost of new debt (coupon × (1 - tax rate) + original issue discount amortization) to coupon of existing bond
- If new coupon is 200bp lower, and call price is par, issuer has strong economic incentive to refinance
- NPV analysis: PV of interest savings (call price - coupon differential) vs. refinancing fees and new debt issuance costs
- Example:
  - Existing bond: 9% coupon, due 2032 (10 years left). Call price = par.
  - Refinancing environment: New 10-year bond at 7% coupon.
  - Annual savings = 2% × $100M = $2M per year × 10 years = $20M (undiscounted).
  - Refinancing cost: 2–3% of issue size = $2–3M.
  - If cost < savings, issuer calls.

### AHYDO (Applicable High-Yield Discount Obligation)

**Tax Rule Definition**
- AHYDO is a tax classification for bonds with high OID (original issue discount) and long maturity
- Triggers: Bond must have OID > 500bp over applicable federal rate (AFR) AND maturity > 5 years
- Example: 10% coupon bond issued at $70M par (30% discount = 30% OID). If AFR = 3%, OID spread = 7% - AFR, triggering AHYDO rules

**Issuer Impact**
- "Catch-up" payment requirement at year 5 (or earlier): Issuer must make deemed principal payment equal to accrued deferred interest
- If not paid, interest deduction is suspended until catch-up paid
- Cash flow implication: Heavily leveraged issuers with zero coupon or deep-discount bonds may face unplanned cash requirements at year 5 refinancing
- Covenant impact: Some HY bond documents contain AHYDO carve-outs allowing temporary leverage covenant relief if catch-up payment is made

**Bondholder Impact**
- Generally does not affect bondholder economics, but limits issuer's ability to defer refinancing
- May force refinancing earlier than expected

### Tenders, Exchange Offers, and Amend-and-Extend

#### Tender Offer

**Structure**:
- Company offers to buy bonds at premium (e.g., 110% of principal)
- Must have cash or financing to fund the tender
- Consent fee often added (e.g., 1-2%) for holders who tender

**Economics**:
- Company issues new bonds at higher coupon/lower price to finance tender
- Incentive: reduces covenant complexity, extends maturity, lowers coupon (if new debt is junior)
- Investor decision: take $110 cash or hold the bonds?

**Minimum Acceptance Condition**:
- Usually 50.1% of outstanding must tender for the offer to close
- Strips covenant protections for non-tendering minority (new notes are less restrictive)
- Holdouts risk being left with orphaned bonds

#### Exchange Offer

**Structure**:
- Bondholders receive new notes in exchange for old bonds (no cash)
- New notes may be senior, have higher coupon, shorter maturity, or more principal

**Incentive for Exchange**:
- New notes more attractive (higher coupon, senior status)
- Old notes' covenants are eliminated or relaxed
- Reduces company's near-term refinancing pressure

**Holdout Risk**:
- If 50.1%+ accept, old bonds lose covenant protection
- Remaining 49.9% hold orphaned bonds with fewer covenants but same credit profile
- Often trades at discount post-exchange

#### Amend and Extend (Bank Market)

- Lender and borrower agree to modify terms and extend maturity
- Common example: 5x leverage covenant reset to 5.5x in exchange for 2-year maturity extension
- Avoids refinancing pressure; improves lender documentation

---
