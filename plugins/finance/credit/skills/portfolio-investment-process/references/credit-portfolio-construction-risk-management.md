---
last_updated: "2026-03-22"
---

# Credit Portfolio Construction & Risk Management

This reference covers enduring portfolio-construction principles. Use root files for current numeric limits, market benchmarks, or stress sizes.

## Core Construction Principle

A portfolio should be built so that no single mistake, thesis break, technical shock, or liquidity event can determine the overall outcome. Diversification is not just "many names"; it is diversification across the risks that actually matter.

## Diversification Dimensions

Evaluate diversification across:

- **issuer**: no single borrower should dominate the downside
- **sector and factor**: different labels can still hide the same economic exposure
- **rating and quality**: portfolios drift toward lower quality faster than they drift back
- **maturity and refinancing profile**: avoid bunching maturities into one market window
- **seniority and structure**: first lien, unsecured, structured, and asset-backed risk do not behave the same way
- **fixed versus floating rate**: rate exposure can unintentionally overwhelm the intended credit view
- **geography and currency**: country and FX risk can amplify credit stress
- **ownership and sponsor linkage**: common sponsor behavior can create hidden concentration

## Position Sizing Principles

Position size should reflect the intersection of:

1. **conviction**: How strong is the underwriting edge?
2. **downside**: What is the realistic loss in a stress or break case?
3. **liquidity**: How hard is it to exit if the view changes?
4. **correlation**: How much does the name overlap with existing exposures?
5. **mandate fit**: Is the vehicle even allowed to own this risk at the proposed size?

The correct size is rarely the largest size that passes a headline concentration limit. It is the size that still looks rational after combining all five tests.

## Liquidity as a Construction Input

Liquidity belongs in portfolio construction from the start, not only during redemption stress.

Use liquidity tiers to answer:

- how quickly the position can be exited in normal markets
- how much price concession would be required in stressed markets
- whether the vehicle can tolerate the position remaining stuck during a broader risk event

Illiquid exposures should consume more internal risk budget even when expected return looks attractive.

## Duration and Reinvestment Shape

Portfolio construction should reflect how capital returns and refinances over time.

Useful questions:

- Is the maturity profile clustered or staggered?
- Does the portfolio depend on one favorable refinancing window?
- Is the strategy meant to express duration, avoid it, or neutralize it?
- Are floating-rate assets being funded or hedged in a way that still leaves rate risk elsewhere in the structure?

## Hedging in Construction

Hedges should support the intended portfolio, not excuse poor construction.

Good uses of hedging:

- isolating credit from rate exposure
- reducing broad-market spread beta while keeping idiosyncratic longs
- protecting a concentrated exposure when the thesis remains intact but timing risk rises

Bad uses of hedging:

- using an index hedge to pretend correlated names are diversified
- keeping an oversized position because a hedge exists in theory
- relying on illiquid or basis-sensitive hedges as if they were certain offsets

## Governance and Review

Construction quality improves when decisions are reviewed at three levels:

- **pre-trade**: Does the new idea fit the portfolio and mandate?
- **periodic portfolio review**: Has the portfolio drifted into hidden concentration or stale theses?
- **event-driven review**: Did a price move, downgrade, amendment, or market dislocation change the risk shape?

Portfolio review should focus on what changed, what is now binding, and whether capital still belongs in the current expression.

## Performance Attribution

Attribution should decompose results into drivers that inform future sizing:

- carry
- spread change
- rate move
- defaults and recoveries
- trading decisions
- hedge effectiveness
- liquidity cost

The goal is not only to explain performance, but to identify whether returns came from skill, beta, hidden factor concentration, or simply a favorable market regime.

---

### Private Debt Allocation

Use this section to decide when private debt deserves capital in a broader credit portfolio. Keep current return, spread, and loss benchmarks in root files such as `references/private-credit-performance.md` and `references/cross-asset-relative-value.md`.

#### Core Allocation Question

Private debt belongs in the allocation only when the investor is being paid for the things that are truly different from public credit:

- lower liquidity
- deeper underwriting workload
- higher reliance on manager sourcing and monitoring skill
- slower price discovery
- stronger documentation or lender control, where real

If those differences are not being compensated, illiquidity alone is not a reason to allocate capital.

#### When Private Debt Fits Best

Private debt is usually the stronger expression when:

- capital can stay committed through the full underwriting and harvest period
- the strategy benefits from maintenance covenants, information rights, and direct lender influence
- the team has the resources to underwrite and monitor borrower-level detail
- public comparables do not offer similar downside protection at a comparable all-in return
- portfolio construction can absorb slower exits and appraisal-based marks

#### When Public Credit May Be Better

Public credit can be the better choice when:

- liquidity and price transparency matter more than documentation control
- the investor wants tradable beta, faster rebalancing, or index-hedgeability
- the public market already offers sufficient spread for the same underlying risk
- the team cannot realistically diligence and monitor the private asset to a higher standard than the market

#### How to Compare Public and Private Opportunities

Normalize the comparison across five dimensions:

1. **Loss-adjusted return**: Compare expected return after expected loss, not headline spread alone.
2. **Liquidity cost**: Estimate what is being paid for lock-up and slow exit.
3. **Documentation quality**: Test whether maintenance covenants, reporting rights, or collateral actually improve downside control.
4. **Manager dependence**: Private debt outcomes depend more heavily on sourcing, amendment discipline, and workout capability.
5. **Valuation realism**: Public marks move faster; private marks move slower. Do not confuse smoothed marks with lower risk.

Use current benchmarks from `references/private-credit-performance.md` and `references/cross-asset-relative-value.md` rather than embedding them here.

#### Manager Selection Principles

Manager selection is often the most important risk decision in private debt allocation.

Focus on:

- full-cycle underwriting discipline rather than recent benign-vintage returns
- realized loss history, not just gross IRR presentation
- workout capability and restructuring experience
- sourcing quality and adverse-selection risk
- team stability and incentive alignment
- fund size relative to genuine opportunity set
- transparency around subscription lines, fee load, and valuation policy

#### Common Allocation Mistakes

##### Mistake 1: Comparing Gross Private Returns to Net Public Returns

Compare both on a like-for-like, post-fee, post-loss basis.

##### Mistake 2: Treating Smoothed Marks as Low Volatility

Private marks can delay the recognition of deterioration. Lower reported volatility is not the same as lower economic risk.

##### Mistake 3: Ignoring Vintage Diversification

A strong strategy can still disappoint if too much capital is deployed during an overheated origination window.

##### Mistake 4: Letting Subscription-Line-Boosted IRR Drive the Decision

Time-weighted return optics can overstate true economic value creation. Look at cash-on-cash outcomes and loss history as well.

##### Mistake 5: Overcrediting Documentation

Maintenance covenants and lender control matter only if the manager uses them well and the borrower retains real enterprise value.

---

## Liquidity Risk Management

Liquidity risk is the risk that the portfolio must transact faster than its assets can be sold without unacceptable value destruction.

### Core Principle

Liquidity is path-dependent. An asset that looks tradeable in a calm market can become functionally illiquid once spreads gap, dealer balance sheets retrench, or redemptions accelerate.

### Liquidity Assessment Framework

Assess liquidity through four lenses:

1. **time to exit**: how long a realistic sale would take
2. **price impact**: what concession would be required
3. **market depth**: whether there are repeatable buyers or only episodic bids
4. **funding dependence**: whether the portfolio needs the asset to fund redemptions, margin, or liabilities

### Liquidity Tiering

Use liquidity buckets as an organizing tool, but classify positions based on stress realism rather than optimistic mark-to-market assumptions.

Questions to ask for each asset:

- can the position be sold quickly in normal markets?
- can it still be sold in a stressed market?
- would the sale happen through a continuous market or a negotiated process?
- would selling it require accepting a discount large enough to change the investment case?

### Portfolio-Level Liquidity Questions

Good liquidity management looks beyond the single asset.

Test:

- how much of the portfolio can be monetized without moving the wrong sleeve first
- whether liquid assets are being implicitly reserved for redemptions or hedges
- whether illiquid allocations have crowded out flexibility elsewhere
- whether financing lines, gates, or structural protections are reliable in stress

### Liquidity Stress Testing

Model scenarios where:

- investor withdrawals accelerate
- market depth falls
- bid-ask spreads widen
- the portfolio must raise cash while marks are falling

The right output is not just a haircut estimate. It is a decision on whether the portfolio still has optionality or would be forced into distressed selling.

### Liquidity Management Tools

Common tools include:

- cash and highly liquid reserves
- staggered maturity profiles
- repo or credit facilities
- redemption gates or lockups where the vehicle allows them
- side pockets or segregated treatment for truly impaired liquidity

These tools are helpful only if the governing vehicle documents and market conditions make them genuinely usable.

### Common Liquidity Mistakes

#### Mistake 1: Treating issue size as liquidity

Large issue size helps, but it is not the same as dependable executable depth.

#### Mistake 2: Assuming yesterday's bid is today's exit

Dealer color in a stable tape is not a stress-exit plan.

#### Mistake 3: Ignoring correlation in liquidity demand

The assets most likely to be sold first are often the same assets everyone else is trying to sell.

#### Mistake 4: Using liquidity only as a compliance check

Liquidity should shape position size, asset mix, and hedge design before the portfolio is tested by outflows.
