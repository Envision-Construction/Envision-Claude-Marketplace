---
last_updated: "2026-03-22"
---

# Litigation Risk in Bankruptcy

Framework for assessing litigation risks that can affect recovery outcomes in bankruptcy proceedings, including avoidance actions, preference claims, fraudulent conveyance, and adversary proceedings.

## Avoidance Actions Overview

The Bankruptcy Code grants the trustee or debtor-in-possession power to recover certain pre-petition transfers that disadvantaged creditors:

| Action Type | Code Section | Lookback Period | Standard |
|---|---|---|---|
| Preferential Transfers | Section 547 | 90 days (1 year for insiders) | Transfer to creditor on account of antecedent debt while insolvent |
| Fraudulent Transfers | Section 548 | 2 years pre-petition | Transfer for less than reasonably equivalent value while insolvent |
| State Fraudulent Transfer | Section 544(b) | Varies by state (4-6 years common) | Applies state fraudulent transfer law with federal standing |
| Post-Petition Transfers | Section 549 | After petition date | Unauthorized post-petition transfers |

## Preference Claims (Section 547)

### Elements Required

All five elements must be present for a preference:
1. Transfer of the debtor's property
2. To or for the benefit of a creditor
3. On account of an antecedent debt
4. Made while the debtor was insolvent
5. Made within 90 days before filing (1 year for insiders)

**Presumption of Insolvency**: The debtor is presumed insolvent during the 90 days before filing. The creditor bears the burden of rebutting this presumption.

### Common Defenses

| Defense | Section | Description | Practical Application |
|---|---|---|---|
| Ordinary Course | 547(c)(2) | Payment made in ordinary course of business | Regular trade payments consistent with historical pattern |
| Contemporaneous Exchange | 547(c)(1) | New value given at substantially the same time | COD deliveries, same-day settlements |
| New Value | 547(c)(4) | Creditor provided new value after preferential payment | Ongoing trade credit replenishes preference exposure |
| Security Interest | 547(c)(3) | Perfected security interest within 30 days | Properly perfected purchase-money security interests |
| Small Preference | 547(c)(9) | Aggregate transfers <$7,575 (adjusted periodically) | De minimis exception for small vendors |

### Impact on Recovery Analysis

| Creditor Type | Preference Exposure | Typical Outcome |
|---|---|---|
| Trade creditors | Payments received in 90-day lookback | Often settle at 50-70% of preference amount |
| Lenders (revolver draws) | Payments or setoffs in lookback period | Ordinary course defense usually applies |
| Insiders (officers, directors, affiliates) | 1-year lookback — significantly broader exposure | Higher litigation risk; less favorable settlement |
| PE sponsor (if insider) | 1-year lookback for management fees, dividends | Dividend recap within 1 year is high risk |

## Fraudulent Conveyance (Section 548)

### Two Types of Fraud

| Type | Standard | Common Examples |
|---|---|---|
| Actual Fraud (548(a)(1)(A)) | Intent to hinder, delay, or defraud creditors | Transfers to family members, asset concealment |
| Constructive Fraud (548(a)(1)(B)) | Less than reasonably equivalent value received while insolvent | LBO debt, intercompany transfers, below-market transactions |

### LBO Fraudulent Conveyance Risk

The most significant fraudulent conveyance risk in leveraged finance:

| Element | Analysis |
|---|---|
| Transfer | Target company incurs acquisition debt; proceeds go to selling shareholders |
| Reasonably Equivalent Value | Target received no value — consideration went to sellers |
| Insolvency | If acquisition debt renders target insolvent (liabilities > assets at FMV) |
| Result | Acquisition debt potentially voidable as fraudulent transfer |

**Practical Factors Affecting LBO Risk**:
- Leverage level at closing (higher = greater risk)
- Solvency opinion obtained at closing (provides defense but not conclusive)
- Business performance post-acquisition (subsequent decline may support insolvency argument)
- Time between LBO and filing (longer gap weakens causal link)

### Dividend Recap Exposure

Sponsor-funded dividend recapitalizations face heightened fraudulent conveyance scrutiny:
- Company takes on additional debt; proceeds distributed to sponsor
- If company subsequently becomes insolvent, distribution may be clawed back
- 2-year federal lookback (Section 548); state laws may extend to 4-6 years under Section 544(b)
- Settlement range: 30-80% of distribution amount

## Substantive Consolidation

### Definition

Court order pooling assets and liabilities of multiple affiliated entities, treating them as a single estate. This can dramatically change recovery outcomes:

| Without Consolidation | With Consolidation |
|---|---|
| Each entity's assets apply to that entity's creditors | All assets pooled for all creditors |
| Higher recovery for creditors of asset-rich entities | Blended recovery across all entities |
| Separate waterfall analysis required per entity | Single waterfall for consolidated estate |

### Factors Courts Consider

| Factor | Favoring Consolidation | Opposing Consolidation |
|---|---|---|
| Corporate formalities | Entities share officers, board, offices | Separate governance, records, meetings |
| Financial records | Commingled accounts, consolidated books | Separate bank accounts, books |
| Asset segregation | Intercompany loans without documentation | Clear asset ownership, arm's-length transfers |
| Third-party perception | Creditors relied on consolidated credit | Creditors contracted with specific entity |
| Intercompany transactions | Extensive, undocumented intercompany activity | Limited, documented at arm's length |

### Credit Analysis Impact

- **Multi-entity borrowers**: Map legal entity structure and identify which entity holds key assets
- **Structural priority**: Senior secured debt at the operating company level has better structural position than holding company debt — unless consolidation eliminates this distinction
- **Recovery sensitivity**: Model recovery both with and without consolidation to establish range

## Equitable Subordination (Section 510(c))

### When Claims Are Subordinated

Courts may subordinate claims of creditors who engaged in inequitable conduct:

| Element | Description |
|---|---|
| Inequitable Conduct | Creditor used its position to gain unfair advantage |
| Harm to Other Creditors | Conduct resulted in injury to other creditors or conferred unfair advantage |
| Subordination Consistent with Bankruptcy Code | Remedy is appropriate under the circumstances |

### High-Risk Parties

| Party | Risk Level | Typical Exposure |
|---|---|---|
| PE sponsor as lender | HIGH | Management fees, intercompany loans, secured claims |
| Insider lenders | HIGH | Loans from officers, directors, or affiliates |
| Controlling shareholders | MEDIUM-HIGH | Dominant shareholder with lending relationship |
| Arm's-length lenders | LOW | Rarely subordinated absent extreme conduct |

## Adversary Proceedings

### Types and Timeline Impact

| Proceeding Type | Purpose | Typical Duration | Recovery Impact |
|---|---|---|---|
| Lien validity challenge | Disputes perfection or priority of security interest | 6-18 months | Can eliminate secured status |
| Claim objection | Disputes amount or validity of filed claim | 3-12 months | May reduce or disallow claims |
| Avoidance action | Preference or fraudulent transfer recovery | 12-36 months | Increases estate value |
| Asset ownership dispute | Determines who owns contested assets | 6-24 months | Directly affects distributable estate |

**Cost Impact**: Adversary proceedings generate significant legal fees — $5-50M+ for complex cases. These fees are administrative claims with priority over all pre-petition creditors, reducing available recovery.

## Impact on Recovery Analysis

### Modeling Litigation Risk

| Factor | Conservative Case | Base Case | Optimistic Case |
|---|---|---|---|
| Preference recoveries | 20% of identified preferences | 50% recovery | 70% recovery |
| Fraudulent conveyance claims | Full claim amount recovered | 50% settlement | 20% settlement |
| Professional fees (litigation) | +$20-50M admin costs | +$10-25M | +$5-10M |
| Timeline extension | +12 months from litigation | +6 months | +3 months |
| Time value discount | Additional PV discount for delay | Moderate discount | Minimal discount |

### Checklist for Litigation Risk Assessment

- [ ] Identify all payments to insiders within 1-year lookback period
- [ ] Identify all payments to non-insider creditors within 90-day lookback period
- [ ] Assess LBO leverage and solvency opinion adequacy
- [ ] Identify any dividend recapitalizations within state fraudulent transfer lookback period
- [ ] Map corporate entity structure for substantive consolidation risk
- [ ] Identify any insider lending or sponsor-related claims subject to equitable subordination
- [ ] Estimate professional fee budget for anticipated litigation
- [ ] Assess whether litigation will delay plan confirmation and reduce present value of recovery
- [ ] Evaluate insurance coverage (D&O, fiduciary) that may fund settlements
- [ ] Review committee formation — creditors' committee pursuit of avoidance actions signals magnitude of exposure
