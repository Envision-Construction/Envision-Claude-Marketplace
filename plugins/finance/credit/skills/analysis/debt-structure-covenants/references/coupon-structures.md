---
last_updated: "2026-03-21"
---

## Coupon Structures

Coupon mechanics determine how and when interest is paid—critical for understanding a borrower's cash flow strain and investor return profile.

### Fixed Rate Coupon
- **Definition**: Standard cash-pay coupon with a fixed rate for the bond's life
- **Prevalence**: Most common coupon type in high-yield bonds
- **Mechanics**: Interest paid semi-annually (typically), rate fixed at issuance
- **Borrower benefit**: Predictable, fixed obligation
- **Investor benefit**: Consistent, known cash returns; no interest-rate risk on coupon (though price risk remains)
- **Example**: 8.5% fixed-rate bond due 2032

### Floating Rate Coupon
- **Definition**: Coupon that resets periodically, typically SOFR + spread
- **Standard in**: Bank loans and floating-rate notes
- **Mechanics**: Reset to SOFR (or similar index) + predetermined spread, usually quarterly or semi-annually
- **SOFR Floor**: Typical structure includes a floor (e.g., "SOFR floored at 2%"). If SOFR < 2%, borrower pays 2% + spread anyway
- **Borrower view**: Benefits when rates decline (because of floor); hurts when rates rise
- **Investor view**: Protected downside if rates fall (floor ensures minimum return); benefits if rates rise
- **Example**: "SOFR + 350bp, floored at 2%" → if SOFR = 1.5%, borrower pays 2.0% + 3.5% = 5.5%

### Zero Coupon Bonds
- **Definition**: Bonds issued at deep discount, no periodic cash interest, accretes to par at maturity
- **Pricing formula**: Accreted Value = Issue Price × (1 + r)^t
- **Cash interest**: 0 throughout the life of the bond
- **Tax benefit (issuer)**: Despite no cash payments, issuer gets OID (original issue discount) tax deduction annually. Total deduction = accreted gain from issue price to par.
- **Recovery at maturity**: Investor receives par at maturity, realizing full gain as bullet payment
- **Use case**: Ultra-highly leveraged deals where issuer cannot sustain cash interest in early years
- **Example**: $100M par bond issued at $60M. Over 7 years, accretes at implicit rate of ~8% per annum. Investor receives $100M at maturity. Issuer deducts $40M of accretion over time for tax purposes.

### Zero-Step Coupon
- **Definition**: Zero coupon period (typically 2–4 years) followed by cash-pay step-up
- **Mechanics**: First period: no cash payments (accretion only). Second period: starts paying fixed cash coupon.
- **Benefit to issuer**: Defers cash outlays until business has deleveraged and can sustain higher payments
- **Benefit to investor**: Delayed but increasing returns; deferred-pay feature (like zero) but eventual cash generation (like step coupon)
- **Example**: Years 1–3 zero coupon at 10% implicit rate, accretion to par. Years 4–10 step to 9% cash pay.

### PIK (Payment-in-Kind)
- **Definition**: Interest paid by issuing additional bonds (or adding to principal), not cash
- **Mechanics**: At each coupon date, issuer issues new bonds to investors in lieu of cash
  - Example: $100M outstanding at 10% PIK → after year 1, $110M outstanding (original $100M + $10M of new PIK bonds)
- **Leverage impact**: Outstanding debt amount grows mechanically with each PIK coupon; debt/EBITDA increases over time
- **Investor perspective**: Return is embedded in the accreting principal; investor's money is not spent but added to debt burden
- **Issuer perspective**: Preserves cash in near term but increases leverage; common in heavily leveraged buyouts
- **Example**: LBO with 6x leverage. Senior bank debt at SOFR+350. Mezzanine at 12% PIK. After 3 years of PIK, mezzanine balance grows from $100M to ~$140M, pushing overall debt/EBITDA higher.
- **Default risk**: As leverage rises with each PIK coupon, default probability increases; PIK bonds are riskier than equivalent cash-pay

### Toggle Bonds
- **Definition**: Issuer can choose each coupon period to pay in cash OR PIK
- **Mechanics**: Two rates offered: lower cash-pay rate and higher PIK rate
  - Example: "8.0% cash or 8.75% PIK, at issuer's option"
- **Issuer incentive**: Choose PIK when cash is tight; revert to cash when leverage allows
- **Investor risk**: Uncertainty about payment form; if issuer chooses PIK, principal balloons
- **Market perception**: Toggle bonds trade between cash and PIK bond yields, depending on issuer credit strength and cash flow outlook
- **Covenant pressure**: Heavy PIK election can trigger leverage maintenance tests or acceleration clauses

### Cash Pay Step Coupon
- **Definition**: Cash coupon that steps up over time
- **Mechanics**: Year 1–3 coupon = 6.5%, Year 4–7 coupon = 8.0%, Year 8–10 coupon = 9.5%
- **Issuer benefit**: Lower initial cash outlay; company deleverages, can absorb higher coupon later
- **Investor benefit**: Known escalation schedule; increasing yield to compensate for extension risk
- **Example**: Many senior secured bonds have step structure aligned with expected deleveraging path

### Purpose of Deferred-Payment Bonds
**Why use zero coupon, zero-step, PIK, or toggle?**
- Heavily leveraged companies (5x+) cannot sustain significant cash interest in years 1–3
- During high-leverage period, business generates just enough FCF to service senior debt and fund capex
- Deferred-pay bonds push interest expense into future periods when leverage is lower
- Allows sponsors to complete add-on acquisitions and operations improvements before requiring full cash coupon
- Trade-off: Interest cost is higher (embedded in accretion or step-up) and default risk is elevated

---
