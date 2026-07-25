---
last_updated: "2026-03-22"
---

# Equity Cure Mechanics

Framework for analyzing equity cure provisions in credit agreements, including mechanics, limitations, and credit implications for leveraged credits.

## Definition and Purpose

An **equity cure** is a contractual right — typically reserved for the private equity sponsor — to contribute equity capital to the borrower to cure a financial covenant breach. The contributed capital is treated as if it were earned EBITDA or used to repay debt for purposes of the covenant compliance calculation.

**Purpose**: Provides the sponsor a mechanism to avoid a technical default when the portfolio company temporarily underperforms financial covenant thresholds, buying time for operational improvement or strategic alternatives.

## Mechanics

### Cure Process Timeline

| Step | Timing | Action |
|---|---|---|
| 1. Quarter End | Day 0 | Financial results show covenant breach |
| 2. Compliance Certificate | Day 45-60 | Borrower delivers quarterly financials showing breach |
| 3. Cure Notice | Within 10-15 business days of certificate delivery | Sponsor notifies agent of intent to cure |
| 4. Cure Contribution | Within cure period (typically same as notice) | Sponsor contributes cash equity to borrower |
| 5. Recalculation | Upon contribution | Covenant compliance recalculated including cure amount |

### Two Cure Methods

| Method | Mechanics | Prevalence | Borrower Friendliness |
|---|---|---|---|
| Deemed EBITDA | Cure amount added to EBITDA for covenant calculation purposes only | More common | MORE borrower-friendly |
| Debt Paydown | Cure proceeds used to repay debt, reducing leverage numerator | Less common | LESS borrower-friendly |

**Deemed EBITDA Example**:
- Covenant: Total Leverage ≤ 5.0x
- Actual EBITDA: $90M, Total Debt: $500M → Actual Leverage: 5.56x (breach)
- Sponsor contributes $25M equity cure
- Adjusted EBITDA: $90M + $25M = $115M → Adjusted Leverage: 4.35x (compliant)
- Note: Actual EBITDA does not change — only the covenant calculation changes

**Debt Paydown Example**:
- Same starting point: $500M debt / $90M EBITDA = 5.56x
- Sponsor contributes $50M, used to repay debt
- Adjusted: $450M / $90M = 5.0x (compliant)
- Note: More expensive for sponsor — requires larger contribution for same result

## Limitations

### Standard Limitations on Equity Cure Rights

| Limitation | Typical Terms | Purpose |
|---|---|---|
| Maximum Total Cures | 2-3 over the life of the credit agreement | Prevents indefinite reliance on sponsor support |
| Consecutive Quarter Restriction | No cure in two consecutive quarters | Forces operational improvement between cures |
| Rolling Period Cap | Maximum 2 cures in any 4 consecutive quarters | Prevents clustering of cures |
| Minimum Cure Amount | Must cure to exactly the required level (no excess) | In some agreements; prevents gaming |
| Maximum Cure Amount | Cure amount limited to shortfall amount | Prevents over-curing to create artificial headroom |
| Cure Form | Cash equity contribution only (not PIK or subordinated debt) | Ensures real capital infusion |

### Variation in Market Practice

More borrower-friendly agreements may include:
- Higher total cure caps (4-5 cures)
- No consecutive quarter restriction
- Cure amount can exceed shortfall (creating forward headroom)
- Broader permitted cure instruments (subordinated shareholder loans)

More lender-friendly agreements may include:
- Lower total cure caps (1-2 cures)
- No consecutive quarter cures AND no more than 2 in any 5-quarter period
- Cure amount must be contributed as common equity (not shareholder loans)
- Cure triggers enhanced reporting requirements

## Exhaustion Scenarios

### What Happens When Cure Rights Are Used Up?

Once all available cure rights have been exercised, the borrower must:

| Scenario | Likely Outcome | Credit Implication |
|---|---|---|
| Business recovers | Covenant compliance restored organically | Positive, but cure history remains a yellow flag |
| Business flat | Must negotiate waiver or amendment | Amendment costs, covenant tightening, spread increase |
| Business deteriorates further | Default risk without cure safety net | Accelerated path to restructuring |

### Modeling Cure Exhaustion

For each credit with equity cure provisions, build a scenario matrix:

1. **Identify the EBITDA level** at which the leverage covenant is breached
2. **Calculate cure amount required** at each downside EBITDA scenario
3. **Track remaining cure rights** — how many have been used?
4. **Assess sponsor willingness** — Will the sponsor fund another cure? (See valuation analysis below)

## Valuation and Sponsor Willingness

### When Will Sponsors Cure?

Sponsors cure when the cost of curing (equity contribution) is less than the value of avoiding default:

| Factor | Cure Likely | Cure Unlikely |
|---|---|---|
| Equity value | Positive — sponsor has value to protect | Negative — equity is underwater |
| Cure cost vs. equity value | Cure < 10% of remaining equity value | Cure > 50% of remaining equity value |
| Turnaround timeline | Clear path to recovery within 2-3 quarters | No visibility to operational improvement |
| Fund vintage | Early in fund life, ample reserves | Late in fund life, limited reserves |
| Portfolio priority | Core holding, high ownership | Small holding, other portfolio priorities |
| Strategic alternatives | Sale process or refinancing in progress | No alternatives, business declining |

### Cure as a Signal

| Situation | Signal | Severity |
|---|---|---|
| First cure in Year 3+ | Temporary setback; generally manageable | LOW |
| First cure within 12 months of closing | Original investment thesis was wrong | HIGH |
| Second cure within 24 months | Fundamental business or structure mismatch | HIGH |
| Cure used to avoid reporting breach | Cosmetic fix, not operational improvement | MEDIUM-HIGH |
| Cure structured as PIK/sub debt (not cash) | Sponsor unwilling to commit real capital | HIGH |

## Analysis Framework

For each credit with equity cure provisions, document the following:

### Cure Rights Inventory

| Item | Current Status |
|---|---|
| Total cure rights granted | [e.g., 3] |
| Cure rights exercised to date | [e.g., 1] |
| Cure rights remaining | [e.g., 2] |
| Consecutive quarter restriction | [Yes/No] |
| Rolling period restriction | [e.g., 2 in any 4 quarters] |
| Cure method | [Deemed EBITDA / Debt Paydown] |

### Cure Trigger Analysis

| EBITDA Scenario | Leverage | Covenant Level | Breach? | Cure Amount Required |
|---|---|---|---|---|
| Base Case | 4.5x | 5.0x | No | N/A |
| Downside (-10%) | 5.0x | 5.0x | Borderline | $0-5M |
| Stress (-20%) | 5.6x | 5.0x | Yes | $25M |
| Severe Stress (-30%) | 6.4x | 5.0x | Yes | $55M |

### Sponsor Assessment Integration

Cross-reference with the due-diligence-and-assessment skill's sponsor evaluation:
- **Fund dry powder**: Does the sponsor have capital available for cure contributions?
- **Fund vintage**: Is the fund approaching end of investment period (limiting new contributions)?
- **Sponsor track record**: Has this sponsor historically supported portfolio companies through stress, or written off investments quickly?
- **Other portfolio demands**: Is the sponsor facing cure/support needs across multiple portfolio companies simultaneously?

## Red Flags

- [ ] Cure exercised in first 12 months post-closing (investment thesis was wrong from inception)
- [ ] Cure structured as PIK note or subordinated loan rather than cash equity
- [ ] Multiple cures used within 24 months (serial underperformance)
- [ ] Cure used to avoid breach reporting rather than to support the business operationally
- [ ] Sponsor fund is late vintage with limited remaining capital for follow-on support
- [ ] Remaining cure rights insufficient to cover projected covenant breach scenarios
- [ ] No consecutive quarter restriction in cure provision (allows indefinite kicking the can)
