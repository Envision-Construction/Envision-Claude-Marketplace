---
last_updated: "2026-03-22"
---

# Hedging Strategies

Use hedges to reshape portfolio risk when the underlying thesis still matters but the current expression carries unwanted beta, rate risk, event risk, or liquidity timing risk.

## Core Principle

The best hedge is the one that offsets the risk you actually have, not the risk that is easiest to trade.

Before hedging, identify whether the exposure is primarily:

- issuer-specific default risk
- broad spread beta
- interest-rate duration
- basis dislocation
- currency risk
- tail-event convexity need

## Main Hedge Types

### Single-Name Credit Hedges

Use single-name CDS or similar issuer-specific protection when the goal is to hedge deterioration in one credit without selling the cash instrument.

Best use cases:

- concentrated positions
- temporary event risk
- delayed exit from the cash instrument
- situations where the thesis is intact but timing risk increased

Main drawbacks:

- basis risk between CDS and cash
- counterparty and collateral considerations
- liquidity can worsen when the hedge is needed most

### Index Hedges

Use index protection when the portfolio needs less market spread beta but the investor wants to keep idiosyncratic names.

Best use cases:

- macro risk-off concern
- temporary protection around market events
- fast beta reduction while individual positions are being reviewed

Main drawbacks:

- portfolio composition may not match the index
- sector or quality mismatches can make the hedge look better in theory than in realized P&L
- index hedges do not solve issuer-specific or documentation-driven downside

### Rate Hedges

Use Treasury futures, swaps, or other rate instruments when the portfolio's intended view is credit, not duration.

Best use cases:

- fixed-rate credit portfolios with unwanted rate exposure
- relative-value trades that should isolate spread from rates
- liability-matching or carry strategies where rate moves would dominate results

Main drawback:

- removing duration does not remove credit risk, and can sometimes expose how much of the return was really a rate view

### Basis Trades

Use basis trades when the dislocation is between economically related instruments rather than in the issuer view itself.

Typical expressions:

- cash bond versus CDS
- hedged asset-swap style structures
- relative-value trades between tranches or similar instruments

These trades require discipline because financing, carry, and liquidity can dominate the outcome before convergence occurs.

### FX Hedges

Use currency forwards or swaps when the investor wants the credit but not the currency.

Questions to ask:

- is the currency move likely to swamp the expected credit return?
- is the investor being paid to hold the unhedged FX exposure?
- does the mandate allow unhedged non-base-currency risk?

## Hedge Sizing Principles

Hedge sizing should be tied to the metric being reduced:

- spread risk: CS01 or spread duration
- rate risk: DV01 or duration
- tail risk: scenario loss or breakpoint analysis
- basis exposure: relative spread or carry decomposition

Avoid the shortcut of matching notional if the sensitivities are not actually comparable.

## When Not to Hedge

Do not hedge just because the position feels large. Hedge only when:

- the underlying thesis remains attractive
- the risk being hedged is separable from the main thesis
- the hedge is liquid and measurable enough to manage
- the expected cost of protection is justified by the risk being removed

If the position no longer belongs in the portfolio, reduction or exit is often cleaner than adding a hedge.

## Monitoring Hedge Effectiveness

Review hedges for:

- basis drift
- changing portfolio composition
- time decay or carry bleed
- counterparty or collateral changes
- whether the original reason for the hedge still exists

A hedge that no longer maps to the portfolio can quietly create a second risk book rather than reducing the first one.
