---
last_updated: "2026-03-22"
---

## Asset Class Deep Dives

### Auto Loan & Lease ABS

**Collateral characteristics**:
- Prime auto loans (credit score 650+), near-prime (550-650), subprime (below 550)
- Lease receivables (off-balance-sheet for auto manufacturers; residual value risk)
- Loan term: 36-84 months (typical); leases 24-48 months
- Originator: captive finance (GM Financial, Ford Credit), bank (Ally, Chase), non-bank originator

**ABS structure**:
- Senior/mezzanine/junior tranches, sequential pay
- Typically fixed-rate notes issued even if collateral mixes fixed + floating
- WAL: 1.5-3.5 years (auto loans amortize relatively fast)
- Size: Typically $200M-$1B deals

**Credit enhancement**:
- Subordination: 1-10% for AAA (depends on prime vs. subprime; subprime deals need more OC)
- Excess spread: 3-10% (3% for prime, 8-10% for subprime)
- Reserve account: 2-3% of original balance

**Key risks**:
- **Prepayment**: Trade-in, refinance, payoff. Prime auto CPR 20-30%, subprime lower (10-20%). Limited negative convexity vs. mortgages
- **Default risk**: Subprime more volatile; historically 3-5% CDR for prime, 8-12% for subprime. COVID drove defaults up significantly
- **Loss severity**: 20-30% typical (repossession + auction recovery); varies by market value of vehicle
- **Residual value risk (leases)**: Actual residual vs. predicted — if cars worth less than residual, lease originator absorbs loss (affects excess spread)
- **Used car prices**: Inflation/deflation impacts residual value and recovery

**Performance analytics**:
- Monthly delinquency rates (30+/60+/90+ DPD)
- Cumulative net losses (should stay low for prime deals)
- Prepayment rate (track vs. expectations)
- Roll rate (% of 30-DPD that cure vs. progress to 60+)
- Dealer concentration (if originators are concentrated at few dealers, higher default correlation)

### Credit Card ABS

**Collateral characteristics**:
- Revolving credit card receivables (no fixed maturity on individual accounts)
- Monthly payment rate 4-15% of balance (depends on issuer, economic cycle)
- Yield (spread on receivables): 12-18% typical
- Originator: Card issuer (Chase, Bank of America, Citi, American Express)

**Unique structure**:
- **Revolving period**: Buyers receive interest only. New receivables continuously added (originator originates new card loans, added to pool). Excess spread retained in reserve
- **Controlled amortization period**: At specified date (e.g., month 72), transition to principal paydown. Investors receive scheduled principal reduction monthly + interest
- **Rapid amortization trigger**: If early amortization trigger fires (see below), transitions immediately to controlled amortization
- **Master trust**: Single trust entity issues multiple series (Series 2024-1, 2024-2, etc.), each series backed by different pool/vintage
- **Expected life**: 5-7 years from issuance to full payoff

**Credit enhancement**:
- Subordination: Junior tranches 3-8% of deal
- Excess spread: 8-15% very common (gross yield 14% − funding 4% − fee 0.5% = high excess spread). Much larger than auto/equipment ABS
- Reserve account: 1-2% initially, maintained from excess spread

**Key risks**:
- **Payment rate decline (MPR/payment rate drop)**: If unemployment rises or consumers stressed, payment rate declines. Collections fall → excess spread shrinks → rapid amortization trigger fires
- **Charge-off spike**: Economic downturn → charge-off rate (credit losses) increases sharply
- **Yield compression**: If spread on receivables declines (less profitable origination) → excess spread shrinks
- **Early amortization trigger**: Fires if:
  - Payment rate falls below threshold (e.g., 5%)
  - Cumulative loss rate exceeds threshold (e.g., 4%)
  - Average consumer balance-to-limit ratio (utilization) exceeds threshold
  - Servicer replacement
  - Reserve account depleted
- **Extension risk**: If rapid amortization fires, remaining life shortens dramatically (e.g., 3-month payout vs. 5-year), opportunity cost if rates have risen
- **Counterparty risk**: Receivables originated by issuer; if issuer fails, new receivables stop being added → base shrinks

**Performance analytics**:
- Monthly payment rate (MPR) — % of balance paid
- Charge-off rate (new losses as % of balance)
- Delinquency rate (30+/60+/90+ DPD)
- Utilization ratio (average balance / average limit) — high utilization = higher default risk
- Yield and excess spread
- Trigger status (e.g., how far from rapid amortization?)

### Student Loan ABS

**Collateral types**:

**Federal (FFELP — Federal Family Education Loan Program)**:
- Government guarantees 97-100% of principal + accrued interest
- Default of borrower → government pays guarantee claim to servicer
- Credit risk minimal (government backstop)
- Declining population (FFELP originated until 2010; now Direct Loans dominate)

**Private Student Loans**:
- No government guarantee; borrower credit-dependent
- Issued by banks, non-bank originators
- Interest rates fixed or floating (some tied to Prime)
- Deferment/forbearance: Borrower can pause payments if in school, economic hardship, etc. (reduces cash flow)

**ABS structure**:
- Sequential pay, amortizing (unlike credit card revolving structure)
- WAL: 7-15 years (long payment terms, many loans 10-year life)
- Floating rate notes common (match floating-rate collateral)
- Larger deals $500M-$2B+

**Credit enhancement**:
- FFELP: Government guarantee + some OC (super-senior). Minimal additional credit enhancement needed
- Private: Subordination 5-15%, excess spread 2-5%, reserve account

**Key risks**:
- **FFELP**: Regulatory risk (government may modify guarantee, change terms). Low credit risk
- **Private**: Borrower credit quality critical. High unemployment/recession → default spikes
- **Deferment/forbearance**: Economic stress pushes borrowers into forbearance → collections stop → WAL extends. Student loan forgiveness programs (income-based repayment, public service forgiveness) create policy risk
- **Servicer concentration**: Few large servicers (Mohela, Navient, etc.); servicer quality & compliance critical
- **Wage garnishment/offset**: Recovery mechanism somewhat limited vs. other loans
- **Income-based repayment risk**: Borrowers on income-based repayment may be making smaller payments than interest accrual → negative amortization on some loans

**Analytics**:
- Payment rate (% of balance paid monthly)
- Delinquency rates (very important — student loans deferment can mask default risk)
- In-school/grace period deferment rates
- Forbearance rates
- Default and loss rates (varies 2-6% annually)
- School/program concentration (graduate vs. undergraduate)

### Equipment ABS

**Collateral types**:
- Aircraft leases (most common, most transparent)
- Railcar leases
- Shipping containers
- Technology equipment (servers, telecom)
- Medical equipment
- Commercial kitchen equipment

**ABS structure**:
- Equipment lease receivables (lessee obligation to pay rent per lease agreement)
- Sequential pay, amortizing
- WAL matched to lease term (aircraft: 7-12 years, railcars: 10-15 years)
- Smaller deal sizes typically (niche originator base)

**Credit enhancement**:
- Subordination: 5-15% depending on equipment type and lessee credit
- Excess spread: 2-6%
- Residual value insurance: Insures equipment residual value at lease end (addresses technological obsolescence or physical deterioration)
- Reserve account: 2-5%

**Key risks**:
- **Lessee credit**: Fewer, larger lessees → concentration risk. Single lessee default could impact multiple leases
- **Residual value**: If actual residual less than estimated, loss absorbed by sponsor/equity; no impact to noteholders IF securitized as residual retained
- **Technology obsolescence**: Faster in telecom/tech equipment; slower in aircraft
- **Equipment condition at lease end**: Return condition lower than expected → lower recovery on residual
- **Lessee concentration**: If equipment portfolio concentrated with few large lessees, default of one is material
- **Specialty equipment**: Illiquid residual markets (railcars hard to sell, limited secondary market)

**Analytics**:
- Lessee credit quality (percentage investment-grade lessees)
- Concentration (top-10 lessee % of portfolio)
- Equipment type breakdown and vintage
- CPR (equipment off-lease early, or lease extended)
- Recovery assumptions (residual values)
- Excess spread

---

### RMBS (Residential Mortgage-Backed Securities)

#### Agency RMBS

**Issuers**: Ginnie Mae (government-owned), Fannie Mae, Freddie Mac (government-sponsored enterprises / GSEs)

**Credit profile**:
- Agency issues guarantee — government or GSE backs bonds
- Credit risk borne entirely by agency, NOT by investor
- Investor bears **prepayment risk** and **interest rate risk** only
- Agency guarantees timely payment of principal + interest regardless of borrower default/delinquency
- Implicit government backing (especially Fannie/Freddie) — market confidence very high

**Pass-through structure**:
- Most common: Pass-through MBS where investor receives pro-rata share of mortgage payments
- Monthly: Principal + interest from borrowers → trustee → pass to noteholders pro-rata
- Weighted average coupon (WAC) on mortgage pool vs. MBS coupon to investor = basis (mortgage originator keeps spread)

**CMO (Collateralized Mortgage Obligation)**:
- Restructuring of MBS cash flows into tranches
- **Sequential tranches**: A, B, C, Z. All principal to A until paid, then B, then C, then Z. Interest to all
- **PAC (Planned Amortization Class)**: Guaranteed principal paydown schedule within prepayment range. PACs protected from prepayment risk within band (100-400% PSA, e.g.)
- **TAC (Targeted Amortization Class)**: Similar to PAC but one-sided; protects against extensions, not contractions
- **IO/PO Splits**: Interest-only vs. principal-only strips. PO benefits from fast prepay; IO benefits from slow prepay
- **Floating-rate CMOs**: Notes with coupon tied to SOFR/Prime + spread; inverse floaters exist

**Prepayment modeling**:
- PSA is the standard market language for baseline mortgage speed assumptions.
- Realized speeds depend on rates, borrower incentive, seasoning, burnout, mobility, and refinancing frictions.
- Agency RMBS should be treated primarily as an optionality problem rather than a credit-loss problem.

**RMBS duration/convexity**:
- **Negative convexity**: In rate-down environment, prepayment rises, WAL shortens, price upside capped. In rate-up environment, prepayment falls, WAL extends, duration extends (price downside amplified)
- **Trading strategy**: Rate-sensitive; requires prepayment forecasting
- **Current coupon**: The most actively traded coupon stack moves with the market. Use `references/market-benchmarks.md` for live context rather than embedding point-in-time levels here.

#### Non-Agency RMBS

**Definition**: Private-label MBS with NO government guarantee. Credit risk borne by investor.

**Collateral types**:
- **Prime jumbo**: Larger-balance prime borrowers with strong documentation and lower expected loss content
- **Alt-A**: "Alternative documentation"; lower documentation standards, stated income, FICO 600-700, reduced verification
- **Subprime** (legacy, pre-GFC): FICO <620, higher LTV, stated income, piggyback loans (first + second mortgages). Heavily securitized pre-2007; now virtually absent in new issuance
- **Non-QM**: Non-qualified mortgage; borrower doesn't fit standard criteria (self-employed, no W-2s, etc.); post-GFC issuance, smaller market

**Structure**:
- Subordinated tranches; sequential pay typical
- % subordination varies: Prime jumbo 5-10% AAA subordination, subprime 30-50% (much higher losses expected)
- Excess spread often present
- Reserve account

**Credit analysis — loan-level data essential**:
- **LTV (Loan-to-Value)**: Lower LTV = lower loss severity if default
- **FICO score**: Higher FICO = lower default probability
- **DTI (Debt-to-Income)**: Lower DTI = higher payment capacity, lower default
- **Loan purpose**: Cash-out refi = higher default risk vs. rate-and-term refi or purchase
- **Occupancy**: Owner-occupied safest, investment property higher risk, second home intermediate
- **Documentation**: Full-doc safest, stated income / no-doc = higher risk
- **Prepay penalty**: Yield premium for shorter WAL (prepay penalties reduce voluntary prepayment)
- **Geographic concentration**: Avoid concentration in declining markets
- **Property type**: Single-family detached safest, condo/multi-family higher risk

**Prepayment modeling**:
- Non-agency usually SLOWER prepayment than agency (prepay penalties, lower incentive to refi)
- CPR models: Custom models for subprime, seasoning effects critical
- Burnout: Subprime pools seasoned, fast prepayers gone, remaining borrowers less mobile
- Voluntary vs. involuntary prepayment: Refinance voluntary (rates down), default + foreclosure involuntary

**Representations & Warranties (R&W)**:
- Originator represents loan quality (credit, documentation, appraisal, property condition)
- If representation breached → originator obligated to repurchase loan at par
- R&W strength depends on originator stability (some originators defunct, repurchase demands not collectible)
- Investor should review loan-level data to assess R&W compliance likelihood

#### Credit Analysis Framework for Non-Agency RMBS

1. **Pool composition**: FICO/LTV/DTI/occupancy/documentation distribution
2. **Vintage analysis**: Origination standards, home-price backdrop, and servicing quality at issuance matter as much as current borrower metrics
3. **Current delinquency**: Leading indicator of losses
4. **Cumulative loss**: Historical performance track record
5. **Servicer quality**: Managing delinquencies, foreclosure timelines, loss mitigation
6. **Economic environment**: Local unemployment, home price trends in pool geographies
7. **Ratings**: Rating agency stress assumptions; compare to actual pool characteristics

#### Loan-Level Data Analysis for Non-Agency RMBS

**Key Distribution Metrics**

When analyzing a non-agency RMBS pool, assess these distributions:

| Metric | What to Assess | Concern Threshold |
|---|---|---|
| **FICO Distribution** | Weighted average and tail (<620 bucket) | WA FICO <680; >15% below 640 |
| **LTV Distribution** | Weighted average and tail (>80% bucket) | WA LTV >75%; >20% above 80% |
| **DTI Distribution** | Weighted average and tail (>43% bucket) | WA DTI >40%; >25% above 43% |
| **Geographic Concentration** | Top 3 states/MSAs | Any single state >25%; top 3 >50% |
| **Loan Purpose** | Purchase vs. refi vs. cash-out refi | Cash-out refi >40% (higher default rates) |
| **Documentation Type** | Full doc vs. alt-doc vs. no-doc | Alt/no-doc >30% (higher risk; less common post-GFC) |
| **Occupancy** | Owner-occupied vs. investor vs. second home | Investor >25% (higher default, lower loss severity) |

**Vintage Ramp Profiles**

Default timing varies by origination vintage and economic conditions:

| Phase | Timeline | Typical CDR Behavior |
|---|---|---|
| **Ramp-Up** | Months 1-18 | CDR increases from near-zero to peak; early payment defaults (EPDs) signal origination quality issues |
| **Peak Default** | Months 18-36 | Highest CDR; rate resets (if ARM), payment shock, life events |
| **Seasoning** | Months 36-60 | CDR declines as weaker borrowers have already defaulted; survivors are stronger |
| **Stable Tail** | Months 60+ | Low, stable CDR; remaining pool is highly seasoned; burnout effect |

**Key Insight:** Pools that show rapid CDR ramp in months 6-12 (vs. the typical 18-month ramp) signal origination quality problems — underwriting standards were likely weak.

#### Non-Agency Credit Metrics

**Default and Loss Analysis**

| Metric | Formula | Typical Pattern | Use |
|---|---|---|---|
| **CDR (Conditional Default Rate)** | Monthly default rate annualized | Lower for cleaner prime collateral and higher for weaker or more levered borrowers | Pool-level credit quality |
| **CPR (Conditional Prepayment Rate)** | Monthly prepayment rate annualized | Higher when refinancing incentive is strong and frictions are low | WAL and cash flow projection |
| **Loss Severity** | (Loss on liquidation) / (Defaulted UPB) | Higher when LTV, timelines, or housing-market weakness are worse | Recovery estimation |
| **CNL (Cumulative Net Loss)** | Total losses / Original pool balance | Builds gradually and shows how much enhancement has been consumed | Subordination adequacy |
| **60+ Day Delinquency** | UPB 60+ days past due / Current pool balance | Early warning before realized loss | Pipeline to default |

**Delinquency Pipeline Analysis**

Track the progression from early delinquency through liquidation:

```
Current → 30-Day → 60-Day → 90-Day → Foreclosure → REO → Liquidation
         ↑                                                    |
         └── Cure Rate (borrowers returning to current) ──────┘
```

| Stage | Typical Duration | Cure Rate | Severity Impact |
|---|---|---|---|
| 30-Day DQ | 1 month | 60-70% cure | Minimal if cured |
| 60-Day DQ | 2 months | 30-40% cure | Advancing costs begin |
| 90-Day DQ | 3+ months | 15-25% cure | Foreclosure likely |
| Foreclosure | 6-24 months (state-dependent) | <5% cure | Legal costs, property deterioration |
| REO | 3-12 months | N/A | Holding costs, disposition discount |
| Liquidation | Final | N/A | Full loss realization |

**Judicial vs. Non-Judicial States:** Foreclosure timelines vary dramatically. Non-judicial states (e.g., TX, GA) average 6-9 months. Judicial states (e.g., NY, NJ, FL) can take 18-36 months, increasing loss severity by 10-20% due to carrying costs.

#### Agency vs. Non-Agency Risk Comparison

| Dimension | Agency (Ginnie/Fannie/Freddie) | Non-Agency |
|---|---|---|
| **Credit Risk** | Government/GSE guarantee — no credit risk to bondholder | Full credit risk to bondholder; subordination required |
| **Prepayment Risk** | Primary risk — no call protection | Present but secondary to credit risk |
| **Liquidity** | Extremely liquid (TBA market) | Less liquid; dealer-dependent |
| **Subordination** | None needed | 5-30% depending on collateral quality |
| **Yield** | Treasury + 50-150 bps | Treasury + 150-500 bps (risk-dependent) |
| **Key Risk** | Prepayment timing, extension, negative convexity | Default, loss severity, recovery timing |
| **Regulatory Treatment** | 0-20% risk weight (banks) | 20-100%+ risk weight |
| **GSE Reform Risk** | Political risk of privatization or guarantee reduction | Not affected by GSE reform |

#### Non-QM / Non-Agency New Issuance (Post-GFC)

The post-GFC non-agency market has evolved significantly from pre-crisis subprime:

**Current Non-Agency Loan Types**

| Loan Type | Borrower Profile | Common Feature | Risk Level |
|---|---|---|---|
| **Non-QM (Bank Statement)** | Self-employed or irregular-income borrowers | Alternative income verification | Moderate |
| **DSCR Rental Loans** | Real estate investors | Qualification based on property cash flow | Moderate |
| **Jumbo Prime** | Higher-income prime borrowers | Full-documentation larger-balance loans | Low |
| **Fix-and-Flip** | Property investors with short business plans | Short duration and execution-driven exits | High |
| **Reperforming/Non-Performing** | Seasoned distressed collateral | Discount purchase and workout dependence | Moderate-High |

**Credit Enhancement Sizing**

Enhancement should be derived from:

- expected default frequency
- severity under foreclosure or liquidation timelines
- prepayment behavior and resulting WAL
- geographic and servicer concentration
- borrower documentation quality and representation risk

Use `references/market-benchmarks.md`, `references/default-recovery-rates.md`, and `references/typical-deal-parameters.md` for current enhancement ranges by product type.

---

### CMBS (Commercial Mortgage-Backed Securities)

For property-level NOI, lease rollover, submarket analysis, and valuation, use `cre-analysis-underwriting`. This note focuses on what is specific to securitized CRE exposure: tranche structure, balloon risk, servicing dynamics, and how loan-level weakness migrates into CMBS subordination.

#### CMBS Conduit

**Definition**: Pooled securitization of 30-100+ diverse commercial mortgages (office, retail, multifamily, hospitality, industrial, mixed-use)

**Mortgage characteristics**:
- Multi-loan pool backed by income-producing commercial real estate.
- Balloon maturity risk is usually central because legal final maturity is shorter than economic amortization.
- Property, tenant, lease, and sponsor quality still drive loss behavior even though the investor owns securities rather than loans.

**CMBS structure**:
- **Senior tranches (AAA)**: 60-70% of structure, first loss protection, floating or fixed coupons. May have call protection / step-down provisions
- **Mezzanine (AA to BB)**: 15-30%
- **Junior/B-piece (BB to unrated)**: 5-15%; traditionally held by "B-piece buyer" (dedicated investor in junior CMBS tranches, provides discipline)
- **Sequential or pro-rata pay** depending on deal (most sequential)

**Subordination sizing**:
- CMBS relies on subordination to absorb property-specific and refinance-related losses.
- The exact enhancement required is market-specific; use `references/market-benchmarks.md` and `references/typical-deal-parameters.md` for current levels instead of hard-coding them here.

**Triggers & Covenants**:
- Loan documents and servicing standards determine how quickly trouble transfers from routine administration to workout mode.
- Prepayment protection, reserve triggers, cash management, and extension tests matter as much as headline DSCR and LTV.

#### Single Asset / Single Borrower (SASB)

- Single large loan (often $500M+) on iconic trophy asset (Park Avenue office tower, flagship retail on 5th Ave, large multifamily complex, major hospitality)
- Simpler structure than conduit (no granularity benefit of diversification)
- More transparent due diligence (focus entirely on single property/borrower quality)
- Larger loan size → borrower credit quality more important
- Direct correlation: property performance = deal performance (no diversification benefit)

#### CRE CLO

- Pool of 30-100+ transitional/bridge CRE loans (shorter term, floating rate, often 3-5 year maturity)
- **Bridge loans**: Short-term, used for stabilization or repositioning; intended to be refinanced or paid via sale
- **Managed CLO structure**: Manager actively trades loans, harvests gains, reinvests proceeds (similar to corporate CLO management)
- **Reinvestment period**: First 2-3 years, manager can reinvest prepayments/payoffs into new loans
- **Amortization period**: Later years, cash directed to paydown

Refer back to this `securitization-and-clos` skill for CLO-style reinvestment mechanics and to `cre-analysis-underwriting` for transitional property underwriting.

#### CMBS Analysis Framework

1. **Collateral quality**: Refer to CRE skills for property-level analysis
   - Property type, location, market fundamentals
   - Tenant quality (investment-grade vs. non-IG)
   - Lease structure (remaining lease term, rent rollover risk, tenant credit)
   - Physical condition (capital expenditure needs)

2. **Loan-level metrics**:
   - DSCR (debt service coverage ratio): NOI / Debt Service
   - LTV (loan balance / property value): Lower = safer
   - Yield (coupon on loan): Compensation for subordination risk
   - Amortization: Shorter amort = higher balloon risk

3. **Portfolio-level metrics**:
   - Geographic diversification (% in top 5 metros, state concentration)
   - Sector diversification (% office, retail, multifamily, hospitality, industrial)
   - Tenant industry diversification (retail = tenant sector concentration risk)
   - Weighted average DSCR (portfolio average)
   - Weighted average LTV

4. **Stress testing**:
   - What if DSCR falls 15-20% (cap rate rises, NOI declines)?
   - What if 10-15% of loans go into special servicing?
   - Recovery rate assumptions on workout loans

5. **Special servicer quality**:
   - Track record handling distressed loans
   - Network for workouts, asset sales
   - Communication / transparency with noteholders

#### Property-Type Risk Framing

Property-type risk should be treated as structural input, not as a fixed ranking table:

- **Multifamily and industrial** often show lower loss volatility, but local supply and sponsor behavior still matter.
- **Retail and hospitality** are more operationally sensitive and require closer review of tenant quality, franchise obligations, and cash burn.
- **Office** often carries the longest tail risk because lease rollover and capex needs can delay recovery even when current debt service looks acceptable.

Use `references/default-recovery-rates.md` and `references/market-benchmarks.md` for current delinquency and recovery context by property type.

#### Servicer Analysis Framework

**Role Distinction**

| Role | Function | Compensation | Conflict Potential |
|---|---|---|---|
| **Master Servicer** | Day-to-day administration and reporting | Routine fee stream | Low under normal conditions |
| **Special Servicer** | Workout, foreclosure, modification, REO, and liquidation | Workout- and liquidation-linked economics | Moderate to high; incentives can diverge from bondholder interests |
| **Operating Advisor** | Oversight and review where required | Mostly fixed economics | Lower direct conflict but limited direct control |

**Servicer Quality Assessment**

| Dimension | Strong Servicer | Weak Servicer |
|---|---|---|
| **Workout Speed** | Acts quickly but not recklessly | Allows problems to age without a clear strategy |
| **Recovery Discipline** | Maximizes net proceeds, not just gross sale price | Accepts delays, weak auctions, or excessive capex leakage |
| **Conflict Management** | Transparent on incentives and decision authority | Opaque alignment with junior holders or affiliated parties |
| **Modification Quality** | Uses modifications to preserve value rationally | Extends problems without improving recovery odds |
| **Reporting Quality** | Clear path, milestones, and disclosure | Sparse reporting and weak rationale |

**Transfer Triggers**

A loan transfers from master to special servicer when:
- Payment default occurs
- Imminent default becomes credible
- Maturity refinance fails
- Borrower distress or bankruptcy removes normal servicing assumptions

**Analyst Focus:** Monitor the percentage of pool balance in special servicing. Rising special servicing rate is a leading indicator of subordination erosion.

#### Loan-Level Data Interpretation

**Key CREFC Reporting Fields**

| Field | What It Tells You | Red Flag |
|---|---|---|
| **DSCR (NCF)** | Debt service coverage using net cash flow | DSCR <1.15x declining for 2+ quarters |
| **Occupancy** | Physical or economic occupancy | Occupancy declining >5% from securitization |
| **Debt Yield** | NOI / Loan Balance | Debt yield declining below 8% |
| **LTV (Updated)** | Current appraised value vs. loan balance | LTV >80% (indicates negative equity risk) |
| **Lease Expiration Schedule** | Upcoming rollover risk | >30% of NRA expiring within 12 months |
| **Reserve Balances** | TI/LC, replacement, debt service reserves | Reserves being depleted without replenishment |

**Early Warning: Pre-Special-Servicing Signals**
1. DSCR declining for 3+ consecutive quarters
2. Occupancy dropping >10% from securitization levels
3. Major tenant non-renewal or downsizing
4. Borrower requesting reserve draws for operating shortfalls
5. Property tax delinquency
6. Insurance lapses or coverage reductions

#### Yield Maintenance vs. Defeasance

| Mechanism | How It Works | Borrower Incentive | Investor Impact |
|---|---|---|---|
| **Yield Maintenance** | Borrower compensates lender for lost coupon economics | More flexible when rates move favorably for the borrower | Provides some call protection but can weaken when reinvestment economics change |
| **Defeasance** | Borrower substitutes Treasury securities matching remaining cash flows; original loan effectively becomes risk-free | Prepay when property value has appreciated enough to justify defeasance cost | High WAL stability; cash flows guaranteed by Treasuries |

**Key Insight:** Defeasance provides stronger call protection than yield maintenance because the substituted Treasuries continue generating the same cash flows regardless of rate movements. Yield maintenance penalties can compress when rates rise, enabling prepayment.

#### SASB vs. Conduit vs. CRE CLO

| Feature | SASB | Conduit | CRE CLO |
|---|---|---|---|
| **Collateral** | Single asset / single borrower | 30-100+ diverse loans | 20-50+ transitional loans |
| **Loan Type** | Fixed-rate, stabilized | Fixed-rate, stabilized | Floating-rate, transitional |
| **Concentration Risk** | Very high (single property) | Low (diversified pool) | Moderate (fewer loans, value-add) |
| **Credit Enhancement** | Lower (10-20% sub) | Higher (20-30% sub) | Moderate (15-25% sub) |
| **Transparency** | Maximum (single asset) | Moderate (pool-level) | Moderate (active management) |
| **Manager Role** | None (static) | None (static) | Active management (reinvestment) |
| **Prepayment** | Defeasance/yield maintenance | Defeasance/yield maintenance | Flexible (floating-rate) |
| **Best For** | Trophy asset exposure | Diversified commercial mortgage | Transitional/value-add exposure |
| **Key Risk** | Binary — single asset default = total loss for junior | Tail risk — worst loans in pool drive subordination erosion | Manager quality — portfolio decisions affect all tranches |

---

### Loan Fund Vehicle Structures

Loan funds matter in securitization analysis because investor vehicle design affects liquidity, valuation pressure, and forced-selling risk in the underlying loan market. The goal here is not to underwrite a specific fund manager, but to understand how the vehicle itself can amplify or dampen market stress.

#### Why Vehicle Structure Matters

- Loans often settle more slowly than public bonds.
- Many investor vehicles promise liquidity that is faster than the assets they hold.
- In stressed markets, the interaction between redemption terms, valuation policy, leverage, and financing lines can drive technical price moves that have little to do with borrower fundamentals.

#### Common Vehicle Types

##### Open-End Funds
- Offer frequent investor liquidity.
- Must manage the mismatch between investor redemptions and slower loan settlement.
- Tend to hold cash, short-duration instruments, or highly liquid loans as a buffer.
- Can become forced sellers when redemptions accelerate.

##### ETFs
- Add an exchange-traded wrapper on top of a less liquid loan market.
- Secondary-market trading can keep the fund liquid for the investor even when the underlying market is less liquid.
- Creation and redemption mechanics, fair-value marks, and dealer balance-sheet capacity become important during stress.

##### Closed-End And Interval Structures
- Reduce daily redemption pressure.
- Allow the manager to hold less liquid positions with less risk of forced selling.
- Introduce discount or premium-to-NAV behavior that can diverge from underlying credit fundamentals.

##### Separately Managed And Long-Lockup Capital
- Usually have the least structural liquidity pressure.
- Can hold through temporary dislocations more easily.
- Still require strong valuation discipline and concentration controls.

#### Underwriting Framework

When analyzing a loan vehicle or using it as a reference point for CLO or loan-market behavior, focus on:

1. **Liquidity promise versus asset liquidity**: How often can investors redeem relative to how fast loans can be sold or settled?
2. **Valuation policy**: How are stale or infrequently traded loans marked, and who controls overrides?
3. **Use of leverage or financing**: Does the vehicle rely on credit lines, repo, or other financing that can tighten when spreads widen?
4. **Portfolio construction discipline**: Are concentrations, lower-liquidity positions, or weaker credits constrained?
5. **Reinvestment behavior**: Does the manager need to stay fully invested, or can it let cash build when market conditions are unattractive?

#### Risk Translation

Vehicle design influences how market stress shows up:

- **Redemption pressure** can force sales of the most liquid loans first, worsening the quality of what remains.
- **Stale marks** can understate risk until the first real trades reset valuations.
- **Leverage or financing lines** can turn a mark-to-market problem into a forced deleveraging event.
- **Discount-to-NAV behavior** in closed-end structures can create technical opportunity without improving underlying credit.

#### Practical Use

- Use this framework when comparing CLO equity to loan funds or other floating-rate credit vehicles.
- Use the governing CLO indenture, fund documents, or mandate materials for current numeric constraints, regulatory limits, and vehicle-specific thresholds.
- Use `trading-pricing-mechanics` when the question is primarily about execution, liquidity, or relative value in the secondary loan market.
