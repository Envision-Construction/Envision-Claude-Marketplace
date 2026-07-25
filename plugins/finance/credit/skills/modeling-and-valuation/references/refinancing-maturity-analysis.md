---
last_updated: "2026-03-21"
---

## Refinancing & Maturity Risk Analysis

### Refinancing Risk Assessment Framework

Refinancing risk is the risk that a borrower cannot replace maturing debt on acceptable terms. It is distinct from credit risk (ability to service debt) and liquidity risk (ability to meet near-term obligations), though all three are deeply interconnected. A fundamentally sound credit can default if it cannot refinance a large maturity into a hostile market.

**Core Questions for Every Maturity:**
1. Can the company access capital markets at or near current terms?
2. If markets are shut, does the company have alternative funding sources?
3. What is the cost differential between current debt and likely refinancing terms?
4. Does the company have sufficient runway (time + liquidity) to wait for better conditions?

### Current Terms vs Market Analysis

Compare the borrower's existing debt cost to prevailing market conditions. Reference `references/market-benchmarks.md` for current benchmark levels.

**Assessment Template:**
```
Existing Debt Terms vs Current Market:
────────────────────────────────────────────────────────
Instrument       Existing Cost   Current Market   Delta
────────────────────────────────────────────────────────
1L secured debt  existing        current          wider/tighter
Unsecured notes  existing        current          wider/tighter
Junior capital   existing        current          wider/tighter
────────────────────────────────────────────────────────
Implication: Refinancing today would increase annual interest expense by $X-$Ymm
```

**Key Factors Driving Refinancing Cost:**
- Rating migration since original issuance (upgrade = tighter, downgrade = wider)
- Sector sentiment shifts (e.g., healthcare regulatory risk, retail secular decline)
- Leverage trajectory (deleveraging = favorable, re-leveraging = unfavorable)
- General market conditions: risk-on vs risk-off, new issue calendar congestion
- Benchmark rate changes: SOFR level vs original pricing date

### Runway Analysis

Runway measures how much time and financial flexibility a company has before it must refinance.

**Runway Components:**
- **Time to maturity**: months/quarters until each tranche matures
- **Available liquidity**: undrawn revolver + cash on hand (net of minimum operating cash)
- **FCF generation**: cumulative projected free cash flow between now and maturity
- **Mandatory amortization**: scheduled principal payments reducing outstanding balance
- **Springing maturities**: provisions that accelerate bank debt maturities (typically 91 days before a bond maturity)

**Runway Calculation:**
```
Available Resources to Address Maturity:
  Cash on hand (net of operating minimum)         $50M
  Projected cumulative FCF to maturity             $120M
  Undrawn revolver capacity                        $75M
  Less: other maturities before target             ($30M)
  Less: mandatory amortization payments            ($20M)
  ─────────────────────────────────────────────
  Net resources available                          $195M
  Maturity amount                                  $300M
  Funding gap requiring market access              $105M
```

### Alternative Capital Sources

When primary market access is constrained, evaluate alternative funding avenues:

| Source | Typical Use Case | Advantages | Disadvantages |
|--------|-----------------|------------|---------------|
| Bank market (TL/RCF) | Senior secured refinancing | Flexible terms, relationship-driven | Secured only, size limits, financial covenants |
| Bond market | Unsecured or secured notes | Large size, covenant-lite available | Market sentiment dependent, longer execution |
| Private credit / direct lending | Middle market or stressed credits | Speed, certainty of execution | Often higher cost, smaller size, tighter covenants |
| Asset sales | Non-core divestitures | Reduces debt without new borrowing | Execution risk, may sell at distressed values |
| Equity raise / rights issue | Highly leveraged situations | Reduces leverage directly | Dilutive, signals distress if unplanned |
| Sale-leaseback | Real estate / equipment-heavy | Unlocks asset value | Creates operating lease obligation, reduces asset base |
| Sponsor equity injection | PE-backed companies | Demonstrates sponsor commitment | Rare unless recovery value is compelling |

### Refinancing Scenario Modeling

Model three refinancing scenarios to bracket outcomes:

**Best Case (Current Market Access):**
- Refinance at current market spreads
- Full amount placed, bullet maturity extended 5-7 years
- Modest increase in interest expense
- Assumes no market disruption between now and execution

**Base Case (Wider Spreads):**
- Market spreads widen from current levels
- Full amount refinanced but at higher cost
- Possible need for additional secured capacity or tighter covenants
- Quantify impact on interest coverage and FCF

**Stress Case (Market Shut / Distressed Access):**
- Public markets inaccessible for an extended period
- Refinancing only available through private credit, banks, or bilateral lenders at meaningfully higher cost
- Reduced size available, requiring partial paydown from cash/asset sales
- Potential need for amend-and-extend with existing lender group
- Quantify: can the company survive on internal resources until markets reopen?

### Cost of Carry Analysis

Quantify the P&L and cash flow impact of refinancing at higher rates:

```
Cost of Carry Impact:
  Outstanding principal                    $400M
  Current all-in cost                      Existing cost
  Projected refinancing cost               New cost
  Incremental annual interest expense      Recalculate
  Impact on interest coverage ratio        Recalculate
  Impact on annual FCF                     Recalculate
  Impact on leverage (via lower FCF)       Recalculate
```

### Maturity Wall Analysis at Portfolio Level

For portfolio managers, aggregate maturity exposure across holdings:

**Portfolio Maturity Profile:**
- Plot all portfolio holdings by maturity year
- Identify concentration: >15% of portfolio maturing in any single year is elevated risk
- Flag names where refinancing risk is highest (low-rated, leveraged, cyclical)
- Monitor "watch list" maturities 18-24 months ahead

**Key Portfolio Metrics:**
- Weighted average maturity of portfolio
- Percentage of holdings maturing within 12 months / 24 months
- Concentration in any single maturity year
- Average credit quality of near-term maturities vs portfolio average

### Amend-and-Extend Mechanics

When full refinancing is impractical, sponsors and borrowers may pursue amend-and-extend (A&E):

**When A&E is Preferred Over Full Refi:**
- Market conditions are unfavorable for new issuance
- Company needs time for operational improvement before accessing public markets
- Sponsor wants to avoid repricing the full capital structure wider
- Existing lender group is supportive and concentrated (easier to negotiate)

**Typical A&E Terms:**
- Maturity extended for a shorter period than a full refinancing cycle
- Spread increase or fee package offered as compensation to extending lenders
- May include additional amortization or cash sweep provisions
- Non-extending lenders remain on original terms (creates split tranches)
- Often accompanied by a modest paydown

### Rating Agency Considerations

Rating agencies evaluate refinancing risk as part of their overall credit assessment:

**Factors Agencies Monitor:**
- **Maturity profile**: concentration of maturities, weighted average life
- **Revolver dependency**: reliance on revolver drawings to fund operations (viewed negatively)
- **Market access track record**: has the issuer successfully accessed markets recently?
- **Liquidity adequacy**: cash + revolver vs near-term maturities and uses
- **Covenant headroom**: tight cushion raises refinancing risk (lenders less willing to extend)

**Rating Impact:**
- Upcoming large maturity (within 12-18 months) with uncertain refinancing can trigger negative outlook
- Successful refinancing that extends maturity and reduces cost can support stable/positive outlook
- Serial A&E activity without deleveraging may signal structural refinancing challenges

### Key Metrics Summary

| Metric | Definition | Watch Level |
|--------|-----------|-------------|
| Weighted avg maturity | Principal-weighted average years to maturity | < 3 years = elevated |
| Nearest maturity date | First significant debt maturity | < 12 months without clear plan = red flag |
| % debt maturing < 12 months | Share of total debt due within one year | > 20% = high urgency |
| % debt maturing < 24 months | Share of total debt due within two years | > 35% = needs attention |
| Liquidity / near-term maturities | Cash + revolver vs debt due < 24 months | < 1.0x = significant risk |
| Refi spread gap | Current cost vs estimated new issue cost | Large enough to impair coverage or FCF materially |
| FCF coverage of maturities | Cumulative FCF vs total maturities due | < 0.5x = market access critical |

### Maturity Wall Construction

#### Maturity Schedule Build
**Plot all debt maturities by year:**

```
Maturity Wall Summary:
2027: $4M (term loan amortization)
2028: $4M (term loan amortization)
2029: $50M (revolver) + $4M (TL amort) = $54M due
2030: $4M (term loan amortization)
2031: $150M (First Lien Bond) + $4M (TL amort) = $154M due
2032: $400M (Term Loan B maturity) + $4M (TL amort) = $404M due
2033: $100M (Second Lien Bond) maturity

Peak: $404M in 2032 (all term loan)
```

#### Refinancing Risk Assessment
**Key questions for each maturity:**

1. **Covenant compliance:** Will company be in compliance at maturity date?
2. **Market access:** Will debt markets be receptive to refinance? (If 2032 is a down market, refinancing risk is high.)
3. **Asset value:** If asset-backed lending, is collateral value sufficient to refinance?
4. **Debt reduction:** Will company have prepaid enough to reduce maturity amount?

**Example:**
- $400M term loan due in 2032
- Base case projects $150M prepayment by 2032
- Remaining: $250M needs refinancing
- Can company refinance $250M at acceptable rates? → Yes in upside, risky in downside

#### Springing Maturities
Some bank agreements include **springing maturity provisions:**

- Bank debt may "spring" 6 months before a publicly traded bond matures
- Forces refinancing earlier than stated maturity
- Common in high-leverage LBOs where management must address maturity wall

#### Basket Capacity & Incremental Debt
Can company **increase debt** to refinance existing maturity?

- Incurrence test: new debt allowed if pro forma leverage < 4.0x (example)
- Cash flow sweep: prepayments reduce flexibility to refinance higher amounts

---
