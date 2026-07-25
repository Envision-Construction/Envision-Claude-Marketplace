---
last_updated: "2026-03-22"
---

## Common Pitfalls, Adjustments & Checklists

### Common Pitfalls

#### Pitfall 1: Confusing YTM with YTW on Callable Bonds
- **Mistake:** Using YTM (8.5%) on a callable bond trading above call price
- **Reality:** YTW (7.8%) is the correct expected return if bond is called
- **Fix:** Always calculate YTW for any callable bond; use STW for comparisons

#### Pitfall 2: Ignoring Accrued Interest in Dirty Price
- **Mistake:** Comparing clean prices without accounting for settlement date
- **Reality:** Buyer pays dirty price (clean + accrued)
- **Fix:** When comparing bonds between coupon dates, add accrued interest to clean price

#### Pitfall 3: Using Nominal Spread for Callable Bonds
- **Mistake:** "Bond yields 8.5%, Treasury 4.5%, so 400 bps spread"
- **Reality:** With call risk, effective spread is lower (430 bps STW vs. 440 bps nominal)
- **Fix:** Use STW as standard comparison metric in leveraged finance

#### Pitfall 4: Forgetting SOFR Floor Impact
- **Mistake:** Assuming SOFR + 300 bps means 3.0% when SOFR = 0%
- **Reality:** With 1.5% floor, coupon = 1.5% + 3.0% = 4.5%
- **Fix:** Always identify floor rate; check if it's in-the-money

#### Pitfall 5: Mispricing PIK Bonds Due to Tax Timing
- **Mistake:** Calculating return without accounting for annual tax drag
- **Reality:** Investor pays taxes on accrued PIK annually, reducing net return
- **Fix:** Model cash tax outflows separately; net return after-tax is 1-2% lower than stated PIK rate

#### Pitfall 6: Call Schedule Assumptions in Refinancing Analysis
- **Mistake:** Assuming issuer will always call on first date possible
- **Reality:** Issuer refinances when NPV is positive (rates fall meaningfully)
- **Fix:** Model multiple scenarios (base case: stable rates, stress: rates fall, bull case: rates rise)

### Bond Analysis Checklist

- [ ] **Price & Yield:** Calculate YTM and current yield; confirm formula usage
- [ ] **Call Risk:** Identify call dates and prices; compute YTW
- [ ] **Spread Metrics:** Use STW (not nominal) for callable bonds
- [ ] **Duration:** Estimate modified duration for % price sensitivity
- [ ] **Accrued Interest:** Add to clean price to get dirty price (settlement amount)
- [ ] **Floating-Rate:** Check SOFR floor and discount margin
- [ ] **Deferred Structures:** Identify PIK/zero coupon; model tax impact
- [ ] **Refinancing:** Compare NPV of refinancing cost vs. interest savings
- [ ] **Worst Case:** Always ask "what if rates fall and bonds get called?"

---
