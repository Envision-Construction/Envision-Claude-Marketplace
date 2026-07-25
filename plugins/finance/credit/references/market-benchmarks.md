---
last_updated: "2026-03-21"
update_cadence: quarterly
next_review: "2026-06-21"
data_vintage: "Q1 2026"
sources:
  - "LCD/PitchBook"
  - "Bloomberg"
  - "S&P Global Ratings"
  - "Federal Reserve"
---

# Market Benchmarks Reference

**Last Updated:** March 2026
**Update Cadence:** Quarterly
**Next Review:** June 2026

---

## 1. Base Rate Environment

| Metric | Current Level | Range (2025-2026) |
|--------|---------------|------------------|
| SOFR (Overnight) | 4.25-4.35% | 4.20-4.75% |
| SOFR 1-Month | 4.30% | 4.25-4.80% |
| SOFR 3-Month | 4.35% | 4.28-4.85% |
| SOFR 6-Month | 4.40% | 4.30-4.90% |
| SOFR 12-Month | 4.45% | 4.32-4.95% |
| Fed Funds Rate | 4.25-4.50% | 4.00-5.25% |
| 2-Year Treasury | 3.85-4.00% | 3.75-4.35% |
| 10-Year Treasury | 4.10-4.25% | 3.95-4.50% |

**Context:** Expect gradual rate moderation through H2 2026 given moderate inflation trends. Fed policy remains data-dependent.

---

## 2. Leveraged Loan Spreads

### First Lien Term Loan B (TLB)

| Rating | Bid-Ask Spread | OID Range | New-Issue Coupon |
|--------|---|---|---|
| BB | 325-375 bps | 2.0-3.5% | SOFR+350-400 |
| B | 400-475 bps | 3.5-5.0% | SOFR+425-500 |
| B- | 475-550 bps | 4.5-6.0% | SOFR+500-575 |
| CCC | 600-725 bps | 6.5-8.5% | SOFR+625-750 |

### Second Lien / Unitranche Pricing

| Product | Spread Range | Typical Coupon |
|---------|---|---|
| Second Lien | SOFR+550-700 | SOFR+575-675 |
| Unitranche (BB) | SOFR+425-525 | SOFR+450-500 |
| Unitranche (B) | SOFR+525-650 | SOFR+575-625 |

**Clearing Spreads:** 350-400 bps (TLB), 575-650 bps (2L)
**Market Size:** ~$1.3T leveraged loan market; annual issuance running 200-250B

---

## 3. High Yield Bond Spreads

### Option-Adjusted Spread (OAS) by Rating

| Rating | Current OAS | 52-Week Range |
|--------|---|---|
| BB | 285-335 bps | 270-380 bps |
| B | 420-480 bps | 390-525 bps |
| CCC | 650-800 bps | 600-950 bps |

### New-Issue Coupon Ranges

| Rating | Coupon Range | Pricing Convention |
|--------|---|---|
| BB | 5.50-6.75% | Par to 101 |
| B | 7.00-8.50% | Par to 102 |
| CCC | 10.00-12.50% | 98-102 |

**Market Size:** ~$2.0T HY bonds outstanding; annual issuance 120-180B depending on cycle

---

## 4. CLO Market Data

### Issuance & AUM
- **2025 CLO Issuance:** ~$175-190B (normalized pace post-2024 reset)
- **Total CLO AUM:** ~$825B globally; ~$600B in US
- **Annual New Issuance (2026E):** 180-210B

### Tranche Pricing (New-Issue Spreads)

| Tranche | Rating | Spread to SOFR | Expected Return |
|---------|--------|---|---|
| AAA | AAA | SOFR+90-120 | 5.15-5.45% |
| AA | AA | SOFR+150-200 | 5.75-6.35% |
| A | A | SOFR+220-280 | 6.45-7.15% |
| BBB | BBB | SOFR+350-425 | 7.75-8.70% |
| BB | BB | SOFR+550-675 | 10.00-11.10% |
| B | B | SOFR+900-1150 | 13.25-15.85% |
| Equity | Unrated | 12-16% expected return | 12.00-16.00% |

**Typical Arbitrage:** 200-280 bps on AAA through BBB weighted average

---

## 5. Private Credit Spreads

### Direct Lending (Unitranche Equivalent)

| Borrower Quality | SOFR Spread | Total Yield |
|---|---|---|
| Sponsor-backed, EBITDA >$20M | +425-525 | 8.65-9.60% |
| Mid-market, EBITDA $10-20M | +525-650 | 9.60-10.85% |
| Lower mid-market, <$10M EBITDA | +675-850 | 11.15-12.85% |

### Secondary/Mezzanine
- **Mezz Pricing:** SOFR+750-1000 (8.75-12.00% total)
- **Sub Debt:** SOFR+1000-1500+ (9.25-13.50%+)

**Market Size:** ~$1.8T private credit AUM; annual deployment 250-320B

---

## 6. Market Size & Volume Summary

| Segment | Total Outstanding | Annual Issuance (2026E) |
|---------|---|---|
| Leveraged Loans | $1.3T | 200-250B |
| High Yield Bonds | $2.0T | 120-180B |
| CLOs | $825B ($600B US) | 180-210B |
| Private Credit | $1.8T | 250-320B |
| **Total Credit Market** | **~$7.0T** | **~$750-960B** |

---

## 7. SOFR Floor Conventions

**SOFR Floor Conventions:** See `references/typical-deal-parameters.md` for SOFR floor conventions by loan type and market segment.

---

## 8. Pricing Grid Conventions

### Typical Leverage-Based Step-Downs (Loan Pricing)

| Leverage Metric | Spread Adjustment |
|---|---|
| Total Debt/EBITDA > 5.0x | SOFR + Base Spread |
| Total Debt/EBITDA 4.0-5.0x | SOFR + Base - 25 bps |
| Total Debt/EBITDA 3.0-4.0x | SOFR + Base - 50 bps |
| Total Debt/EBITDA < 3.0x | SOFR + Base - 75 bps |

### Interest Coverage Step-Ups

| EBITDA/Interest | Spread Adjustment |
|---|---|
| < 2.0x | +25 bps step-up |
| 2.0-2.5x | No adjustment |
| > 2.5x | -25 bps step-down |

---

## Notes for Analysts

- **Regional Variation:** European direct lending spreads typically 50-100 bps tighter than US equivalents
- **Covenant Trends:** Continued loosening; most sponsor-backed deals now "cov-lite" in SOFR+400 range
- **Rating Inflation:** Credit quality trends mix; watch for increased B-rated issuance
- **Liquidity Premium:** Wider spreads on smaller $<50M facilities; tighter on institutional scale
- **Cross-Border:** SOFR-based deals now 95%+ of new US issuance; sterling SONIA alternatives declining

---

## 9. Commercial Real Estate Market Benchmarks

### Cap Rate Ranges by Property Type

| Property Type | Cap Rate Range | Notes |
|---|---|---|
| Multifamily | 4.5–6.5% | Most competitive; cap rates tighten for stabilized assets |
| Industrial | 5.0–7.0% | Benefited by e-commerce logistics demand |
| Office — CBD | 6.5–8.5% | Elevated due to remote work headwinds |
| Office — Suburban | 7.0–9.5% | Higher caps reflect greater uncertainty |
| Retail — Anchored | 6.0–8.0% | Stable cash flows; lower caps for grocery-anchored |
| Retail — Unanchored | 7.5–10.0% | Wider range; tenant credit dependent |
| Hospitality — Select Service | 7.5–9.5% | Operational risk premium factored in |
| Self-Storage | 5.5–7.5% | Resilient asset class; steady occupancy |
| Medical Office | 5.5–7.0% | Steady demand from healthcare users |
| Data Center | 5.0–6.5% | Low-cap due to long-term lease stability |

### CRE Mortgage Spreads by Lender Type

| Lender Type | Spread Range | Typical Coupon | LTV | DSCR |
|---|---|---|---|---|
| Agency (GSE-eligible) | T+140–200 bps | 5.40–6.00% | 60–75% | ≥1.25x |
| CMBS Conduit | T+160–250 bps | 5.50–6.50% | 65–80% | ≥1.20x |
| Life Company | T+130–180 bps | 5.30–5.80% | 60–75% | ≥1.30x |
| Bank Portfolio | SOFR+175–300 bps | 5.75–6.65% | 65–80% | ≥1.15x |
| Bridge/Debt Fund | SOFR+300–550 bps | 7.25–9.75% | 70–85% | ≥1.10x (interest-only) |

**Context:** Agency spreads tightest; bridge lending provides maximum flexibility but at highest cost. Life company lending favors longer hold periods and lower leverage.

### CMBS Market Snapshot

| Metric | 2025 | 2026E | Notes |
|--------|------|-------|-------|
| Annual Issuance Volume | $85–95B | $80–100B | Normalized post-rate volatility |
| SASB vs. Conduit Mix | 35% SASB / 65% Conduit | Similar | SASB (single-asset/properties) gaining share |

**CRE Delinquency Rates:** See `references/default-recovery-rates.md` (CRE Default & Recovery section) for current delinquency rates by property type.

**Update Cadence:** Quarterly (track rate environment, delinquency trends, property-type performance)

---

## Structured Finance Market Benchmarks

Current market conditions for asset-backed securities, project finance, and securitized credit markets (March 2026).

### ABS Spreads by Sector (New-Issue)

| Sector | AAA Spread | Tranche Spread Range | Notes |
|--------|-----------|---------------------|-------|
| Auto Prime | T+40–60 bps | AAA to BBB: T+40 to T+350 | Tightest spreads; strongest underwriting |
| Auto Subprime | T+80–120 bps | AAA to B: T+80 to T+800 | Wider spreads reflect credit risk |
| Credit Card | T+35–55 bps | AAA to A: T+35 to T+200 | Low-risk, stable vintages |
| Student Loan | T+50–80 bps | AAA to BBB: T+50 to T+300 | Government-backed; low default |
| Equipment | T+50–75 bps | AAA to A: T+50 to T+250 | Lease-backed; collateral-strong |
| RV Loans | T+75–110 bps | AAA to BBB: T+75 to T+400 | Volatile collateral; wider spreads |

**Context**: Auto prime tightest due to strong collateral values and underwriting. Subprime wider reflecting 5–7% default rates. Credit card resilient (0.5–1% default).

### RMBS Spreads

| Product | AAA Spread | Notes |
|---------|-----------|-------|
| Agency MBS (Current Coupon) | T+80–140 bps | Implicit government backing; liquid |
| Non-Agency Prime Jumbo AAA | T+100–160 bps | Higher default risk vs. agency |
| Non-Agency Alt-A AAA | T+150–220 bps | Legacy; lower credit quality |

**Market Snapshot**: Agency MBS ~$12T outstanding; non-agency smaller and distressed. Pre-2009 vintage experiencing high defaults (70+ months delinquent).

### CMBS Spreads

| Product | AAA Spread | Notes |
|---------|-----------|-------|
| Conduit AAA | T+90–140 bps | Diversified property pools; liquid |
| SASB AAA | T+80–130 bps | Single-asset; concentrated; less liquid |

**Delinquency Context**: See `references/default-recovery-rates.md` (CRE Default & Recovery section) for current CMBS delinquency rates by property type.

### ABS Issuance Volume (Annual)

| Metric | 2025 Actual | 2026 Estimate |
|--------|-------------|---------------|
| Total ABS Issuance | ~$300–320B | ~$310–350B |
| Auto ABS | ~$120B | ~$130B |
| Credit Card ABS | ~$50B | ~$55B |
| Equipment ABS | ~$30B | ~$32B |

### RMBS & CMBS Issuance

| Product | 2025 | 2026E |
|---------|------|-------|
| Agency RMBS | ~$2.0–2.2T | ~$2.1–2.4T |
| Non-Agency RMBS | ~$80–100B | ~$90–110B |
| CMBS | ~$85–95B | ~$80–100B |

**Context**: RMBS dominated by agency (~95% of market); non-agency small, specialist market. CMBS normalized post-rate volatility.

### Project Finance Spreads (Infrastructure Debt)

| Rating | BBB Project Bond Spread | BB Project Bond Spread |
|--------|--------------------------|----------------------|
| Investment-Grade Infrastructure | T+150–220 bps | N/A (IG category) |
| BB-Rated Infrastructure | T+250–350 bps | N/A (below BBB) |
| Typical Senior Leverage | 70–75% | Range for projects |

**Examples**:
- Motorway concession (toll revenue, 25-year): BBB, T+180 bps
- Wind farm (PPA-backed, strong offtake): BBB, T+150 bps
- Water treatment (municipal revenue-backed): BBB, T+200 bps
- Port expansion (traffic-dependent): BB, T+300 bps

**Market Size**: Global infrastructure debt market ~$200–250B annual issuance; US/Europe dominant. Asian/EM infrastructure growing 15–20% annually.

