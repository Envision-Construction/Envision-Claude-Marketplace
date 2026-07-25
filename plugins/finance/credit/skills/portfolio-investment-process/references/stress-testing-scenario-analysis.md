---
last_updated: "2026-03-22"
---

# Stress Testing & Scenario Analysis

Use this reference for the process of building and applying stress tests. Pull the current scenario sizes and benchmark assumptions from the root files `references/stress-scenario-framework.md`, `references/market-benchmarks.md`, and `references/default-recovery-rates.md`.

## Purpose

Stress testing answers two questions:

1. What happens to the position or portfolio if the world is worse than the base case?
2. Which assumption actually breaks the thesis or the portfolio limit?

The point is not to predict the exact future path. The point is to expose fragility before capital is committed.

## Scenario Types

### Historical Replay

Use a prior market regime as a template for how multiple variables can move together. Historical replay is useful for showing how liquidity, spreads, defaults, and technicals can interact rather than move one at a time.

### Hypothetical Downside

Design a forward-looking scenario around the risk that matters most to the current portfolio, such as:

- refinancing shock
- recessionary margin compression
- liquidity freeze
- sector-specific drawdown
- rate shock with weaker coverage

### Reverse Stress

Start from the bad outcome and work backward:

- what spread move would break the position?
- what EBITDA decline would violate the thesis?
- what combination of downgrades, defaults, or liquidity loss would breach portfolio limits?

Reverse stress is often the fastest way to identify the true binding constraint.

## Scenario Design Principles

Good stress tests:

- move the variables that are economically linked
- distinguish mark-to-market pain from realized loss
- separate issuer-level stress from portfolio-level contagion
- include liquidity and financing effects where relevant
- use current root inputs rather than stale historical numbers copied into local files

Bad stress tests:

- move one variable in isolation when the real risk is multi-factor
- reuse old magnitudes without checking the current market regime
- assume orderly exit in a disorderly scenario
- present a scenario table without explaining what would force action

## Position-Level Stress Process

For a proposed or existing position:

1. Define the key break variables: revenue, margin, rates, spread, recovery, exit liquidity, or structural test cushion.
2. Build at least a moderate downside and a severe downside.
3. Translate the operating stress into price impact, loss severity, or refinance risk.
4. Identify the breakpoint where the thesis changes from "under pressure" to "no longer acceptable."

## Portfolio-Level Stress Process

For a portfolio:

1. Apply the scenario to all relevant names, not just the candidate investment.
2. Layer in concentration and correlation effects where losses can cluster.
3. Test the impact on:
   - portfolio P&L
   - drawdown
   - concentration limits
   - liquidity coverage
   - vehicle-specific tests
4. Identify which holdings or risk buckets drive the damage.
5. Decide whether to reduce exposure, hedge, or reject the new trade.

## Mechanics

Stress mechanics can combine:

- **mark-to-market impact**: spread, price, or rate move applied to current exposure
- **default loss impact**: stressed default and recovery assumptions
- **liquidity impact**: additional exit discount or inability to monetize
- **correlation impact**: simultaneous loss across linked names or sleeves

Use metric definitions from `references/credit-risk-metrics.md` when translating scenarios into CS01, DV01, or expected-loss terms.

## Reporting Standard

A useful stress output should state:

- the scenario definition
- the variables shocked
- the position-level effect
- the portfolio-level effect
- the names or sleeves most affected
- whether any current limit or mandate test would be breached
- the recommended action if the scenario is judged plausible

## Interpretation

A position is not acceptable simply because it survives a stress mechanically. The harder question is whether surviving still leaves the portfolio in a shape the investor would willingly own.

Stress testing is therefore a decision tool, not a presentation exercise.
