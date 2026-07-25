## Distressed Trading Mechanics

### Definition of Distressed Loans
Distressed loans are those where the borrower is:
- **In default** on interest or principal payments (payment default)
- **In material breach** of financial covenants (covenant default)
- **Approaching maturity** with limited refinancing options (maturity default)
- **In bankruptcy** (claims trading)
- **Exhibiting credit deterioration** with high probability of future default

Distressed loans trade at significant discounts to par (often 20-80 cents on the dollar) reflecting the probability of principal loss.

### Settlement Timeline — T+20
Distressed trades typically use longer and more bespoke settlement mechanics than performing trades because the transfer package often must address defaults, uncertain balances, claims treatment, or non-standard economics. Use root `references/typical-deal-parameters.md` for the current market convention; the enduring principle is that distressed settlement is slower and more conditional than performing-loan settlement.

### Pricing and the "Flat" Market
Distressed loans trade using different conventions than par loans:

**Par Trading (Performing Loans)**
- Price: 98.50 (percentage of par)
- Buyer receives: Accrued interest from last coupon date to settlement date (called "accrued" or "dirty" price)
- The sale price (98.50) is the "clean" price; actual payment is 98.50 + accrued interest

**Flat Trading (Distressed Loans)**
- Price: 45.00 (percentage of par)
- Buyer receives: ONLY the price paid (45.00); no separate accrued interest
- Why: Borrower is typically in payment default; there is no accrued interest to transfer
- "Flat" price includes all economics — principal recovery expectation only

**Semi-Annual Reset Example**
- Assume 6% coupon on $100M loan, coupon paid Jan 1 and July 1
- Par trade on March 1: Price 99.00 + accrued interest of 1% (~3 months of accrual) = 100.00 all-in payment
- Distressed trade on March 1: Price 50.00 flat (no accrued interest); buyer pays only 50.00

### LSTA Standard Terms for Distressed Trades
Distressed confirmations usually address flat trading conventions, extended settlement, true-up, breakage, bankruptcy or claims-specific language, and the treatment of uncertain balances or post-trade credit events.

### True-Up Mechanics
In distressed trades, particularly post-default, the outstanding loan balance may be uncertain:
- Borrower may have made partial prepayments
- Default interest may accrue, increasing the balance
- Facilities may be partially charged off by lender

**True-up process**:
- Trade confirmation references an estimated outstanding balance (e.g., $98.5M)
- At settlement, agent provides actual outstanding balance (e.g., $98.1M)
- If difference is material, seller either:
  - Adjusts purchase price to reflect actual balance, or
  - Buyer accepts the balance and settlement proceeds as-is

### Breakage Costs
When a floating-rate loan is transferred during an interest accrual period:

**Breakage scenario**:
- 3-month benchmark period: June 1 - September 1
- Assignment effective: July 15
- Seller's interest period broken mid-period
- Buyer is responsible for buyer's portion of interest; seller continues to bear seller's portion

**Breakage cost**:
- Calculated as the cost of breaking the benchmark fixing early
- Typically 5-10 basis points (paid by buyer to seller or absorbed in pricing)
- LSTA standard: Breakage costs are buyer's responsibility unless otherwise negotiated

### Unfunded Commitments in Distressed Trades
If the loan includes an unfunded revolver component:
- **Par market practice**: Buyer assumes unfunded commitment upon assignment
- **Distressed practice**: Often negotiated separately
  - Buyer may refuse to assume unfunded commitment
  - Trade documentation specifies whether unfunded revolver is "funded" (buyer responsible) or "unfunded" (seller retains)
  - If buyer refuses, buyer pays a discount for funded amount only

### Bankruptcy Claim Trading
Post-bankruptcy-filing, loans may become **claims** subject to bankruptcy-specific treatment:
- Claims trade under Claims trading conventions (not loan trading conventions)
- Effective date may be delayed pending claim allowance by court
- Principal recovery determined by plan of reorganization
- Settlement can extend materially while claim status and transfer requirements are clarified
