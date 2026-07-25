## Floating-Rate Pricing

Floating-rate instruments should not be treated as "always near par" without checking the reset mechanism, spread basis, embedded floors or caps, and whether the reference-rate regime itself has changed since issuance.

### Discount Margin

Discount margin is the spread over the projected reference-rate path that equates expected cash flows to the current price. It is the closest floating-rate analogue to a spread measure for fixed-rate bonds.

Use discount margin when:

- The instrument reprices periodically off a floating benchmark.
- The market quotes the instrument on spread over the benchmark rather than as a standalone yield.
- You need to compare a floating-rate instrument with another floating-rate instrument on a normalized basis.

### Why Floating-Rate Instruments Usually Trade Near Par

Frequent coupon resets dampen interest-rate sensitivity because the coupon periodically re-aligns with the prevailing benchmark. That said, price can still move materially when:

- Credit spread changes.
- The benchmark floor becomes valuable.
- Liquidity deteriorates.
- The market expects refinancing, repricing, or default risk.

### Floor Mechanics

A benchmark floor creates a minimum coupon base and introduces fixed-rate behavior whenever the observed benchmark falls below the floor.

Practical implications:

- When the benchmark is above the floor, the floor is out-of-the-money and has little immediate economic effect.
- When the benchmark is below the floor, the lender effectively owns a floor option.
- The deeper the floor is in-the-money and the longer it is expected to remain so, the more duration-like the instrument becomes.

Do not compare two floating-rate loans on spread alone if one has a meaningful floor and the other does not.

### Reference-Rate Fallbacks and Legacy Contracts

Some legacy instruments were originated under a prior reference-rate regime and later transitioned through hardwired fallback language or amendment. When analyzing those instruments:

- Confirm the current benchmark named in the documents.
- Identify whether any spread adjustment was added to preserve economics during the transition.
- Avoid comparing pre-transition and post-transition spreads without normalizing for that adjustment.
- Distinguish legacy fallback mechanics from new-issue pricing conventions.

Use root `references/market-benchmarks.md` for the live benchmark curve and `references/typical-deal-parameters.md` for current convention ranges rather than embedding those values here.

### Common Mistakes

- Using current coupon as a proxy for required return.
- Ignoring the value of an in-the-money benchmark floor.
- Treating repricing frequency as a substitute for credit analysis.
- Comparing floating-rate and fixed-rate instruments without an asset-swap or equivalent normalization step.
- Mixing legacy fallback-adjusted spread with newly originated spread as if they were directly comparable.
