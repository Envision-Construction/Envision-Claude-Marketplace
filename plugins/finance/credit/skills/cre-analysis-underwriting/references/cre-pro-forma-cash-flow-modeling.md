---
last_updated: "2026-03-21"
---

## CRE Pro Forma Cash Flow Modeling

### NOI Build from Rent Roll

Net Operating Income (NOI) is the heart of CRE underwriting. Build it systematically from the rent roll:

**Step 1: Gross Potential Rent (GPR)**
```
GPR = Σ(each unit/space × contract rent × 12 months)
```
- Unit-by-unit: multiply each leased unit's monthly rent by 12
- Unleased units: apply market rent (underwriting assumption)
- Multi-tenant: sum across all leases
- Example: 10 units at $2,000/month = $240,000 GPR annually

**Step 2: Other Income**
- Parking fees, late charges, subletting income, utility reimbursements
- Typically 5-10% of GPR
- Example: $240,000 GPR + $15,000 other income = $255,000 total income

**Step 3: Vacancy & Credit Loss**
```
Vacancy & Credit Loss = (GPR + Other Income) × Vacancy Rate %
```
- Vacancy assumptions: 5-10% typical for stabilized properties (class A lower, class C higher)
- Credit loss: 1-3% for tenant bankruptcy risk (use historical or local market data)
- Example: $255,000 × 7% vacancy = $17,850 loss

**Step 4: Effective Gross Income (EGI)**
```
EGI = GPR + Other Income - Vacancy & Credit Loss
```
- Example: $255,000 - $17,850 = $237,150 EGI

**Step 5: Operating Expenses**
Deduct all operating costs related to property maintenance and administration:
- Property taxes (largest single item for most properties)
- Insurance (property, liability, workers compensation)
- Utilities (if landlord pays)
- Repairs & Maintenance (R&M): routine upkeep, HVAC, roof repairs
- Management fees: typically 3-6% of EGI
- Administrative: accounting, legal, miscellaneous
- Landscaping, snow removal, common area maintenance
- Example: $237,150 EGI - $95,000 operating expenses = $142,150 NOI

**NOI Calculation:**
```
NOI = EGI - Operating Expenses
```

### Lease Type Impact on Expenses

**Triple-Net (NNN) Leases**
- Tenant pays: property taxes, insurance, CAM (Common Area Maintenance)
- Landlord pays: only building structure maintenance + debt service
- Landlord NOI: cleaner, lower operating expenses
- Landlord responsibility: ensure tenant solvency (bad tenant credit = bad rent collection)
- Example: Restaurant in shopping center on NNN → landlord gets rent but tenant bears expense volatility

**Gross Leases**
- Landlord pays: ALL operating expenses
- Tenant pays: base rent only
- Landlord exposed to: rising property taxes, insurance, utilities
- Landlord profit: highly dependent on expense control
- Example: Class A office building — landlord bills tenants for above-base expense increases

**Modified Gross**
- Hybrid: landlord pays base expenses, tenant reimburses excess above base year
- Base year stop: "Tenant pays excess property taxes above Year 1 level"
- Caps: "Landlord liable for insurance increases above 5% annually"
- Landlord protection: limits expense volatility exposure
- Example: 2,000 SF office at $25/SF base + expense stop → tenant covers tax increases over base

### Operating Expense Detail

**Property Taxes** (typically 15-25% of NOI in high-tax jurisdictions)
- Varies by location: Texas/Arizona lower (~0.5-0.8% of value), NY/NJ higher (~1.5-2.0%)
- Assessed value may change annually
- Tax appeals possible (if market value declines)
- For stabilized proforma: use current year or assume modest growth (2-3% annually)

**Insurance** (typically 1-3% of revenue)
- Property insurance: covers building replacement
- Liability: covers slip-and-fall and third-party injuries
- Environmental: required in some markets (Phase I concern)
- Workers compensation: if any employees on-site
- Amount: increases with property value, loss history, risk profile

**Utilities** (if landlord paid)
- Electricity, natural gas, water/sewer, trash
- Efficiency matters: LED lighting, HVAC tuning, smart controls reduce expenses
- Typically 2-5% of NOI for typical properties
- Can be 5-10% for data centers or refrigerated warehouses (high energy)

**Repairs & Maintenance** (typically 3-8% of NOI)
- Routine: HVAC filter changes, plumbing repairs, roof patching, parking lot resealing
- Aging buildings: higher R&M burden
- Capital reserves: separate from R&M (see CapEx section)
- Expense reimbursement opportunity: landlord can often bill tenants for major repairs (lease-dependent)

**Management Fees** (typically 3-6% of EGI)
- Third-party property manager: 5-6% of EGI (includes leasing, tenant relations, vendor management)
- In-house management: imputed at 3-4%
- Larger portfolios: lower %, smaller assets: higher %
- Discounted for newer/smaller properties

**Administrative & Other** (typically 1-2% of NOI)
- Accounting, legal, reserves for contingencies
- Leasing commissions at lease renewals (see below under tenant rollover)

### Tenant Rollover Modeling

**The Roll Problem**: As leases expire, rent may reset to current market rates — opportunity or risk.

**Lease Expiration Schedule**
Build a timeline showing when each tenant's lease expires:
```
Tenant A: 2,000 SF, current rent $20/SF = $40,000/yr, lease expires Year 2
Tenant B: 3,000 SF, current rent $18/SF = $54,000/yr, lease expires Year 4
Tenant C: 1,500 SF, current rent $22/SF = $33,000/yr, lease expires Year 5
```

**Renewal Probability**
- Conservative assumption: 60-80% of tenants renew (20-40% depart)
- By tenant quality: A-credit tenants (95%+ renewal), C-credit tenants (40-50%)
- Market-dependent: strong market = higher renewal, weak market = lower

**Downtime (Vacancy) Between Tenants**
- Market-dependent: 3-6 months typical
- New tenant: 4-6 months to lease, construct TI, move in
- Loss of rent during downtime: major P&L impact
- Pro forma: if 1,000 SF rolls in Q3 at $20/SF, model 4 months loss = $6,667

**Market vs. In-Place Rent Analysis**
- **In-place rent**: current rent paid by occupant (may be above or below market)
- **Market rent**: rent achievable for newly leased space today
- Example:
  - Tenant paying: $18/SF (in-place, favorable lease from prior owner)
  - Market rent today: $22/SF (market has improved)
  - At renewal: tenant likely loses lease or accepts mark-to-market

**Below-Market Lease (Upside Scenario)**
- In-place: $18/SF, Market: $22/SF
- At rollover: uplift of $4/SF on 1,000 SF space = $4,000 additional annual NOI
- Probability: depends on tenant credit, market tightness
- Pro forma: apply 70% probability of achieving market rent (conservative)

**Above-Market Lease (Downside Risk)**
- In-place: $25/SF, Market: $20/SF
- At rollover: rent decline of $5/SF on 1,000 SF = $5,000 lost NOI
- Tenant may depart rather than accept 20% rent cut
- Pro forma: assume 100% loss if tenant leaves (pessimistic but prudent)

> **Note:** Dollar amounts and percentage ranges below are illustrative benchmarks. Consult `references/market-benchmarks.md` for current market data.

**Leasing Costs at Tenant Turnover**

Tenant Improvements (TI):
```
Renewal TI: $5-15/SF typical (paint, carpet, minor upgrades)
New Tenant TI: $15-60/SF typical (type varies widely)
  - Industrial: $10-15/SF (minimal)
  - Office: $40-60/SF (demising walls, electrical, IT infrastructure)
  - Retail: $30-50/SF (storefront upgrades, systems)
```
- TI paid by landlord (cost borne in year of renewal/lease-up)
- Amortized over lease term for accounting, but cash impact upfront

Leasing Commissions:
```
LC = % of aggregate lease value (total rent over lease term)
Typical: 4-6% of total lease payments
Example: 1,000 SF at $20/SF × 5-year lease = $100,000 rent
Leasing commission = $100,000 × 5% = $5,000 (typically split 2.5% each to tenant rep and landlord rep broker)
```
- Paid at lease signing
- Tenant representation commission: 2.5-3%
- Landlord representation commission: 2.5-3%
- Pro forma: include as cash outflow in year lease executed

**Pro Forma Example: 5,000 SF Apartment Building**
```
Year 1: 5 units × $1,000/month × 12 = $60,000 GPR
Year 2: 1 unit (tenant A) renews at market ($1,100/month instead of $1,000)
  - Downtime: 2 months = $2,200 lost
  - TI cost: 500 SF × $8/SF = $4,000
  - Leasing commission: ($1,100 × 12) × 5% = $660
  - Net impact: +$1,200 rent - $2,200 downtime - $4,000 TI - $660 commission = -$5,660 (upfront cost)
  - Year 2+ recurring benefit: +$1,200 annual rent
```

### Below/Above Market Lease Analysis

**Mark-to-Market Summary Table**
Build a table showing each lease and mark-to-market opportunity/risk:
```
Tenant     | Sq Ft | Current Rent | Market Rent | Mark-to-Market | Expiry | Action
Unit A     | 1,000 | $18/SF       | $22/SF      | +$4/SF upside  | Yr 3   | Re-lease
Unit B     | 1,500 | $25/SF       | $20/SF      | -$5/SF risk    | Yr 5   | Likely depart
Unit C     | 1,200 | $20/SF       | $20/SF      | Neutral        | Yr 4   | Renewal likely
```

**Calculate NOI Impact at Each Rollover**
- If mark-to-market positive: show additional NOI in proforma upon rollover
- If mark-to-market negative: show reduced NOI or assume tenant departure

**Probability Weighting**
- Conservative: assume 50-70% chance of achieving positive mark-to-market (holdout risk)
- Assume 80-100% probability of losing above-market space (tenants will leave or force negotiation)

### CapEx and Reserves

**Routine Maintenance CapEx**
- Annual budget for non-recurring repairs: roof section replacement, HVAC replacement on schedule, parking lot resealing
- Typically $250-500/unit (multifamily) or $0.15-0.30/SF annually (by property type)
- Separates from R&M (which is smaller repairs and maintenance)

**Replacement Reserve**
- "Reserves for replacement" or "FF&E reserve" for major component failures
- Example: multifamily property with 100 units, $400/unit annual reserve = $40,000/year
- Used to fund: roof (25-30 year life), HVAC (15-20 year), parking surface (15-20 year), windows (20+ year)

**Deferred Maintenance Assessment**
- Phase I property condition report (PCR) identifies deferred maintenance
- Quantifies cost to bring property to market standard
- Example: $200,000 deferred maintenance (roof, parking lot, HVAC) → should be capitalized upfront in acquisition analysis
- Reduces stabilized NOI impact (already spent at acquisition)

**Impact on Debt Service**
- CapEx reduces FCF available for debt service (and leverage calculations)
- Lenders often require reserve accounts: impound CapEx annually
- Example: Debt agreement requires $50,000 annual CapEx reserve → borrower must deposit $50K/year into restricted account

### Value-Add Scenario Modeling

Value-add properties: purchased below stabilized value, improved through repositioning, then sold.

**Current NOI vs. Projected NOI**
```
Current (Day 1):
  Occupancy: 85% at $18/SF = $18,000 NOI (simplified)

Projected (Stabilized, Post-Renovation):
  Occupancy: 95% at $22/SF = $22,000 NOI

Value Creation:
  NOI uplift: $22,000 - $18,000 = $4,000 (22% improvement)
```

**Renovation Budget**
- Hard costs: structural, systems, cosmetic work
- Soft costs: architecture, permits, project management (typically 15-25% of hard costs)
- Contingency: 10-15% of total hard + soft (unknown risks)
- Interest carry: financing cost during renovation period
- Example:
  ```
  Hard costs:        $1,000,000
  Soft costs (20%):    $200,000
  Contingency (10%):   $120,000
  Interest carry (6m): $36,000
  Total:             $1,356,000
  ```

**Rent Premium Achievable**
- Based on renovated comps in market
- Class C building renovated to Class B: support $20-22/SF
- Class B building renovated to Class A: support $25-28/SF
- Market-dependent: must support assumptions with comp analysis

**Lease-Up Timeline**
- Phased lease-up (if can lease during construction): 3-4 months
- Post-completion lease-up: 4-6 months for full stabilization
- During lease-up: carry costs (utilities, taxes, insurance) with no rent income
- Pro forma: show month-by-month lease-up trajectory

**Stabilization Period**
- Time required to achieve target occupancy + market rent
- Typical: 12-18 months post-renovation start
- Pro forma: show ramp from acquisition baseline → stabilized NOI

**Development Yield Analysis**
```
Development Yield = Stabilized NOI / Total Project Cost

Project Cost = Acquisition price + Renovation cost + Soft costs + Interest carry + CapEx reserve

Example:
  Acquisition:       $3,000,000
  Renovation:        $1,500,000
  Total Cost:        $4,500,000

  Stabilized NOI:    $450,000

  Development Yield: $450,000 / $4,500,000 = 10.0%
```

**Comparison to Market Cap Rate**
- Market cap rate: 6-8% for Class A, 8-10% for Class B
- If development yield > market cap rate: positive value creation
- If development yield < market cap rate: paying too much upfront
- Example: 10% dev yield vs. 7% market cap rate → 300 bps upside

### Construction/Development Pro Forma

Building a new property from ground up involves extended pre-income phase.

**Total Cost Build**
```
Land:                    $1,000,000
Hard Costs (construction):
  - Structural          $ 600,000
  - MEP (mechanical)    $ 400,000
  - Finishes            $ 500,000
  Total Hard:           $1,500,000

Soft Costs (15-20% of hard):
  - Architects          $  200,000
  - Engineering        $   75,000
  - Permits/Fees       $   75,000
  - Project mgmt       $  150,000
  Total Soft:          $  500,000

Contingency (5-10%):     $  200,000

Interest Carry:
  - During construction (18 months at 5% on average balance): $60,000

Developer Fee (if applicable): $100,000

Total Project Cost:      $3,360,000
```

**Draw Schedule**
- Lender funds on construction schedule (monthly or periodic draws)
- Builder invoice submitted, third-party inspector verifies, lender funds
- Interest accrues on drawn amounts only (not full commitment)

**Pre-Leasing Requirements**
- Many lenders require pre-leasing: 70-80% pre-leased before funding beyond certain % of construction
- De-risks lease-up phase
- Example: Shopping center must be 75% pre-leased (anchor tenants signed) before construction begins

**Absorption / Lease-Up Velocity**
- How many months to lease available space post-completion
- Multifamily: 4-6 months typical
- Office: 6-12 months (longer negotiation cycles)
- Retail: 6-12 months (more selective tenant approval)
- Pro forma: show month-by-month lease-up; avoid revenue until lease executed and tenant occupancy

**Stabilized NOI Projection**
- Upon full lease-up: apply market rent assumptions + controllable operating expenses
- Example: 150-unit multifamily at $1,500/month average = $2,700,000 GPR
- Less 5% vacancy + $900,000 operating expenses = $1,620,000 NOI

**Development Yield vs. Market Cap Rate**
- Compare stabilized property yield to market exit cap rate
- If dev yield (stabilized NOI / total project cost) > market cap rate: justify development
- If dev yield ≤ market cap rate: negative spread → development may not be economic
- Example: $1,620,000 NOI / $3,360,000 cost = 48.2% yield (this would be annually on stabilized basis, typically expressed as cap rate)
- Correct phrasing: Stabilized cap rate = $1,620,000 / implied property value at market cap rate
  - If market cap rate = 6.5%: implied value = $1,620,000 / 0.065 = $24.9M
  - Development yield compared to market exit cap rate

---
