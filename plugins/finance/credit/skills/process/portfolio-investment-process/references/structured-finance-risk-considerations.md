---
last_updated: "2026-03-21"
---

## Structured Finance Risk Considerations

Special risk management considerations for securitizations, project finance, and other structured credit investments.

### Correlation Risk in Securitized Pools

Default correlation among pool assets fundamentally determines loss distribution shape and tranche protection adequacy.

**Key Dynamic**:
- **Low Correlation** (0.10–0.20): Defaults spread evenly across portfolio; losses concentrated near expected level. Fat tails minimal; tranching highly effective. Subordination of 5–10% provides substantial protection.
- **High Correlation** (0.50–0.80): Defaults cluster; losses exhibit fat tails. Stress scenarios produce correlated defaults; subordination may be insufficient. Tranches experience concentrated loss impact.

**Sources of Correlation**:
1. **Geographic Concentration**: Regional recession → correlated defaults across borrowers in same region
2. **Industry Concentration**: Sector downturn (energy, retail) → correlated defaults by sector
3. **Macroeconomic Sensitivity**: Recession → broad credit stress across diverse asset types
4. **Vintage Concentration**: All loans originated in 2019 (peak) → all age into high-risk period simultaneously

**Practical Approach**:
- Baseline model assumes correlation matrix based on historical defaults
- Stress test: double correlation assumption; recalculate loss distributions and tranche cash flows
- Example: auto ABS with CPR 6%, CDR 0.5%, correlation 0.3 → run stress scenario with correlation 0.6
  - Impact: loss tail fattens; BBB tranche extends by 6–12 months; WAL increases 0.5–1.0 years
- Large correlation increases → potential breach of early amortization triggers

**Portfolio Hedging**:
- If overweight auto ABS and concerned about correlation risk, buy CDS protection on weakest pools or index (CDX.NA.ABS auto segment) to hedge tail risk

### Model Risk in Structured Products

Structured products are model-dependent; valuation, risk assessment, and tranche prioritization all rest on assumptions. Model risk is critical.

**Key Model Risk Sources**:
1. **Garbage-In/Garbage-Out**: Bad input assumptions → misleading output
   - Example: using historical prepayment speeds (CPR 4%) in low-rate environment (actual 12%) → massive WAL shortening; unexpected principal return
   - Mitigation: sense-check assumptions against market forward rates, borrower behavior, incentives

2. **Structural Complexity**: Waterfalls with 50+ rules, triggers, subordination switches
   - Model bug (off-by-one error, wrong trigger logic) → cash flows misallocated
   - Mitigation: independent model validation; audit code logic; stress-test edge cases

3. **Parameter Sensitivity**: Small changes in CPR/CDR have outsized impact on tranche cash flows
   - Example: auto ABS
     - Base: CPR 6%, CDR 0.5% → WAL 4.8 years
     - +100 bps CPR shock: CPR 7%, CDR 0.5% → WAL 4.2 years (0.6 year shortening)
     - Duration impact: tranche loses 5–15% value if rates rise post-shortening
   - Mitigation: sensitivity tables; WAL ranges (e.g., "WAL 4.2–5.5 years across CPR scenarios")

**Risk Management**:
- **Sensitivity Analysis**: Dashboard showing valuation/WAL/cash flows across CPR/CDR ranges
- **Scenario Testing**: Base, optimistic, pessimistic; historical CPR/CDR ranges
- **Independent Validation**: Third-party audit of model logic, code, assumptions
- **Transparent Assumption Documentation**: Document why assumptions chosen; link to market data/historical performance

### Servicer Risk

Servicer quality directly impacts ABS/RMBS/CMBS cash flows and investor recovery.

**Servicer Failure Modes**:
- Poor collections: servicer inattentive to delinquencies → defaults rise (unnecessary)
- Slow recoveries: servicer inefficient in workout/liquidation → recovery rates decline
- Fraud/mismanagement: servicer diverts escrow funds, misrepresents performance
- Financial stress: servicer under pressure; may sell servicing portfolio to undercapitalized successor

**Evaluation Framework**:
1. **Servicer Financial Health**: Audit servicer's capital, profitability, market position
   - Is servicer specialized (dedicated asset class) or diversified across 50+ asset types?
   - Does servicer have scale ($500M+ AUM) or boutique?

2. **Operational Capabilities**: Staffing, technology, historical performance
   - How many delinquent accounts per servicer employee (efficiency)?
   - Average time to resolve delinquency (velocity)?
   - Historical loss severity vs. industry benchmark (quality)?

3. **Historical Performance**: Track servicer's track record on similar deals
   - Servicer X's auto ABS: CDR 0.8% (vs. market 0.5%)?
   - RMBS performance: recovery rates 65% (vs. market 70%)?

4. **Backup Servicer Provisions**: Is backup servicer pre-identified and tested?
   - Can backup assume servicing in <10 days?

**Rating Agency View**:
- Rating agencies explicitly rate servicers (S&P: "Strong", "Average", "Weak")
- Poor servicer rating → less credit subordination considered adequate
- Example: AAA RMBS with "Weak" servicer may have 25% subordination; same pool with "Strong" servicer: 18% subordination

**Portfolio Management**:
- Avoid concentration in single servicer (operational risk)
- Monitor servicer changes (servicer sales, mergers); may downgrade to backup servicer = performance risk
- In distressed / underwater ABS: servicer quality critical (poor servicer may liquidate underwater portfolio at fire-sale prices)

### Project Finance Risk Monitoring

Project finance investments require continuous operational monitoring from development through mature operation.

**Construction Phase** (highest risk; 2–4 years typical):
- **EPC Milestone Tracking**: Monitor actual construction vs. schedule; flag delays >3 months
  - Cascade: schedule delay → IDC accumulation → cost inflation → leverage ratio deterioration
  - Triggers: if delay >20% of estimated timeline, evaluate cost overrun scenario; may need equity top-up
- **Budget Variance**: Track actual costs vs. budget; flag >5% overruns monthly
  - Early warning: >10% cumulative overrun → likely completion guarantee invoked
- **Change Orders**: Monitor EPC change orders; large orders signal scope creep or design flaw
  - Example: $5M change order on $100M contract (5%) → significant cost impact
- **Independent Engineer Reports**: Review quarterly IE reports on construction progress, safety, quality
  - Red flags: safety incidents, quality defects, schedule slippage in IE notes

**Operating Phase** (20–30 years typical):
- **DSCR Monitoring**: Quarterly, compare actual vs. projected
  - If actual DSCR < projected by >20%: investigate cause
  - Scenarios: lower revenues (availability gaps, offtake underperformance), higher OpEx
  - Trigger: if DSCR falls below covenant minimum (typically 1.20x), default imminent
  
- **LLCR/PLCR**: Annual calculation; monitor trend
  - If declining >15% YoY: recalibrate; may trigger refinancing discussions
  
- **Reserve Balances**: Track DSRA, DSA (debt service account), maintenance reserve
  - If DSRA <50% of target: flag; monitor cash flow closely
  - Draws from DSRA indicate cash squeeze; need to understand cause
  
- **Operating Performance**: Monitor key metrics
  - Infrastructure: availability percentage (target 98%+), deductions, downtime
  - Utility: volume throughput, margin per unit
  - Real estate: occupancy rate, tenant credit quality, expiry analysis
  
- **Maintenance & Capex**: Ensure adequate spending to maintain asset condition
  - Under-maintenance → deferred degradation → long-term revenue/availability risk
  
- **Regulatory/Compliance**: Monitor regulatory changes, license renewals, environmental compliance
  - Regulatory breach → penalties, remediation costs, potential concession termination risk

**Cash Flow Lock-Up / Distribution Rights**:
- Monitor when distributions to sponsor restricted (distribution lock-up triggers)
  - Typical trigger: DSCR <1.30x; if triggered, all excess cash trapped until DSCR recovers
  - Sponsor equity return deferred; may indicate project stress
- Review direct agreement terms: can lender step-in if sponsor default? Timeline?

**Refinancing Risk**:
- As debt maturity approaches (5–7 years typical for bank debt), assess refinancing capacity
- If project performance deteriorated: may not qualify for refinancing at maturity
- Example: project loan matures Year 7 at 6.5% coupon; if DSCR declined to 1.15x, new lender may require 8%+ coupon or refuse
- Advocate for extended maturity or take-out commitment early if refinancing risk identified
