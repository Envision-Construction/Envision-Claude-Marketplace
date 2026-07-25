---
last_updated: "2026-03-22"
---

# Pre-Trade Mandate Compliance Check Template

A standardized template for verifying that a proposed trade complies with all investment mandate limits before execution. Populate numeric limits from the governing documents and current references such as `references/portfolio-risk-parameters.md` and, for BDC private credit use cases, `skills/private-credit-middle-market/references/bdc-regulatory.md` rather than copying "typical" values from memory. A failed compliance check is a hard stop unless the mandate explicitly allows an exception path.

---

## Trade Identification

| Field | Entry |
|---|---|
| **Trade Date** | [YYYY-MM-DD] |
| **Credit Name** | [Issuer / Borrower] |
| **Instrument** | [1L TL / 2L TL / Sr. Unsecured / Sub Notes / etc.] |
| **CUSIP / ISIN** | [Identifier] |
| **Trade Direction** | [ ] Buy / [ ] Sell / [ ] Increase / [ ] Decrease |
| **Proposed Notional** | [$XXmm par amount] |
| **Proposed Market Value** | [$XXmm at current price] |
| **Fund(s) Affected** | [Fund name(s) and allocation split] |
| **Analyst** | [Name] |
| **Portfolio Manager** | [Name] |

---

## 1. Concentration Limits

### Single-Name Exposure

| Metric | Current | Post-Trade | Mandate Limit | Headroom | Pass/Fail |
|---|---|---|---|---|---|
| Par Exposure (% of NAV) | [X.X%] | [X.X%] | [X.X%] | [X.X%] | [ ] |
| Market Value Exposure (% of NAV) | [X.X%] | [X.X%] | [X.X%] | [X.X%] | [ ] |
| CS01 Contribution (% of Total) | [X.X%] | [X.X%] | [X.X%] | [X.X%] | [ ] |

### Industry / Sector Concentration

| GICS Sector | Current (% NAV) | Post-Trade (% NAV) | Mandate Limit | Headroom | Pass/Fail |
|---|---|---|---|---|---|
| [Issuer's sector] | [X.X%] | [X.X%] | [X.X%] | [X.X%] | [ ] |
| [Second largest sector] | [X.X%] | [X.X%] | [X.X%] | [X.X%] | [ ] |
| [Third largest sector] | [X.X%] | [X.X%] | [X.X%] | [X.X%] | [ ] |

### Issuer Group / Related Entity Exposure

| Metric | Current | Post-Trade | Mandate Limit | Pass/Fail |
|---|---|---|---|---|
| Combined exposure to issuer corporate family (% NAV) | [X.X%] | [X.X%] | [X.X%] | [ ] |
| Number of distinct instruments in same capital structure | [X] | [X] | [X max] | [ ] |

---

## 2. Credit Quality Distribution

### Rating Distribution vs. Mandate Bands

| Rating Bucket | Current (% NAV) | Post-Trade (% NAV) | Mandate Minimum | Mandate Maximum | Pass/Fail |
|---|---|---|---|---|---|
| Investment Grade (BBB- and above) | [X.X%] | [X.X%] | [X%] | [100%] | [ ] |
| BB+ to BB- | [X.X%] | [X.X%] | [X%] | [X%] | [ ] |
| B+ to B- | [X.X%] | [X.X%] | [X%] | [X%] | [ ] |
| CCC+ and below | [X.X%] | [X.X%] | [0%] | [X%] | [ ] |
| Not Rated | [X.X%] | [X.X%] | [0%] | [X%] | [ ] |

**Notes on split ratings:** Use the lower of Moody's and S&P for mandate compliance purposes unless the fund documents specify otherwise.

### Weighted Average Rating

| Metric | Current | Post-Trade | Mandate Requirement | Pass/Fail |
|---|---|---|---|---|
| Weighted Average Rating Factor (WARF) | [XXXX] | [XXXX] | [Max XXXX] | [ ] |
| Weighted Average Rating (letter) | [B+] | [B+] | [Min B+] | [ ] |

---

## 3. Geographic and Currency Exposure

### Geographic Distribution

| Region | Current (% NAV) | Post-Trade (% NAV) | Mandate Limit | Pass/Fail |
|---|---|---|---|---|
| United States | [X.X%] | [X.X%] | [X%] | [ ] |
| Western Europe | [X.X%] | [X.X%] | [X%] | [ ] |
| Emerging Markets | [X.X%] | [X.X%] | [X%] | [ ] |
| Other Developed Markets | [X.X%] | [X.X%] | [X%] | [ ] |

### Currency Exposure

| Currency | Current Unhedged (% NAV) | Post-Trade Unhedged (% NAV) | Mandate Limit (Unhedged) | Pass/Fail |
|---|---|---|---|---|
| USD | [X.X%] | [X.X%] | [N/A — base] | [ ] |
| EUR | [X.X%] | [X.X%] | [X%] | [ ] |
| GBP | [X.X%] | [X.X%] | [X%] | [ ] |
| Other | [X.X%] | [X.X%] | [X%] | [ ] |

**Note:** If the instrument is non-USD, confirm whether an FX hedge is in place or planned. Unhedged non-base currency exposure is typically limited to 5-15% of NAV.

---

## 4. Maturity and Duration Profile

### Maturity Distribution

| Maturity Bucket | Current (% NAV) | Post-Trade (% NAV) | Mandate Limit | Pass/Fail |
|---|---|---|---|---|
| Less than 1 year | [X.X%] | [X.X%] | [Min X%] | [ ] |
| 1-3 years | [X.X%] | [X.X%] | [X%] | [ ] |
| 3-5 years | [X.X%] | [X.X%] | [X%] | [ ] |
| 5-7 years | [X.X%] | [X.X%] | [X%] | [ ] |
| Greater than 7 years | [X.X%] | [X.X%] | [Max X%] | [ ] |

### Duration Metrics

| Metric | Current | Post-Trade | Mandate Limit | Pass/Fail |
|---|---|---|---|---|
| Weighted Average Life (years) | [X.X] | [X.X] | [Max X.X] | [ ] |
| Spread Duration (years) | [X.X] | [X.X] | [Max X.X] | [ ] |
| Effective Duration (years) | [X.X] | [X.X] | [Max X.X] | [ ] |

---

## 5. Liquidity Profile

### Liquidity Bucket Distribution

| Liquidity Tier | Definition | Current (% NAV) | Post-Trade (% NAV) | Mandate Minimum/Maximum | Pass/Fail |
|---|---|---|---|---|---|
| **Tier 1 — Daily** | Can be sold within 1 business day at or near mid-market (e.g., on-the-run IG bonds, liquid CDX) | [X.X%] | [X.X%] | [Min X%] | [ ] |
| **Tier 2 — Weekly** | Can be sold within 5 business days with less than 50 bps market impact (e.g., liquid HY bonds, broadly syndicated loans) | [X.X%] | [X.X%] | [N/A] | [ ] |
| **Tier 3 — Monthly** | Can be sold within 30 days; may require price concession of 50-200 bps (e.g., smaller loan tranches, off-the-run bonds) | [X.X%] | [X.X%] | [N/A] | [ ] |
| **Tier 4 — Illiquid** | Liquidation timeline exceeds 30 days or requires structured process (e.g., private placements, distressed loans, bespoke structured products) | [X.X%] | [X.X%] | [Max X%] | [ ] |

### Liquidity Coverage

| Metric | Current | Post-Trade | Mandate Requirement | Pass/Fail |
|---|---|---|---|---|
| Tier 1 + Tier 2 coverage of 30-day redemption estimate | [X.Xx] | [X.Xx] | [Per mandate / root reference] | [ ] |
| Cash and cash equivalents (% NAV) | [X.X%] | [X.X%] | [Min X%] | [ ] |
| Undrawn credit facility | [$XXmm] | [$XXmm] | [N/A] | [ ] |

---

## 6. Instrument-Specific Limits

| Instrument Category | Current (% NAV) | Post-Trade (% NAV) | Mandate Limit | Pass/Fail |
|---|---|---|---|---|
| Senior Secured Loans | [X.X%] | [X.X%] | [X%] | [ ] |
| Senior Unsecured Bonds | [X.X%] | [X.X%] | [X%] | [ ] |
| Second Lien / Subordinated | [X.X%] | [X.X%] | [Max X%] | [ ] |
| Structured Products (CLO, ABS) | [X.X%] | [X.X%] | [Max X%] | [ ] |
| Equity or Equity-Linked | [X.X%] | [X.X%] | [Max X%] | [ ] |
| CDS / Derivatives (notional as % NAV) | [X.X%] | [X.X%] | [Max X%] | [ ] |
| PIK or Deferred Interest | [X.X%] | [X.X%] | [Max X%] | [ ] |
| Covenant-Lite Loans | [X.X%] | [X.X%] | [Max X%] | [ ] |

---

## 7. Risk Metrics Impact

| Risk Metric | Current | Post-Trade | Mandate Limit | Pass/Fail |
|---|---|---|---|---|
| Total Portfolio CS01 ($) | [$XXX,XXX] | [$XXX,XXX] | [Max $XXX,XXX] | [ ] |
| Portfolio DV01 ($) | [$XXX,XXX] | [$XXX,XXX] | [Max $XXX,XXX] | [ ] |
| Gross Leverage (Long + Short / NAV) | [X.Xx] | [X.Xx] | [Max X.Xx] | [ ] |
| Net Leverage (Long - Short / NAV) | [X.Xx] | [X.Xx] | [Max X.Xx] | [ ] |
| Expected Shortfall (95%, 1-month) | [$X.Xmm] | [$X.Xmm] | [Max $X.Xmm] | [ ] |
| VaR (95%, 1-day) | [$X.Xmm] | [$X.Xmm] | [Max $X.Xmm] | [ ] |

---

## Compliance Determination

### Summary

| Category | Result |
|---|---|
| Concentration Limits | [ ] Pass / [ ] Fail |
| Credit Quality Distribution | [ ] Pass / [ ] Fail |
| Geographic / Currency Exposure | [ ] Pass / [ ] Fail |
| Maturity / Duration Profile | [ ] Pass / [ ] Fail |
| Liquidity Profile | [ ] Pass / [ ] Fail |
| Instrument-Specific Limits | [ ] Pass / [ ] Fail |
| Risk Metrics | [ ] Pass / [ ] Fail |

### Overall Determination

- [ ] **PASS** — Trade complies with all mandate limits. Approved for execution.
- [ ] **FAIL** — Trade breaches one or more mandate limits. Trade cannot proceed without resolution.

### Binding Constraint (If Fail)

| Constraint | Current Utilization | Post-Trade Utilization | Limit | Overage |
|---|---|---|---|---|
| [Identify the specific limit that is breached] | [X.X%] | [X.X%] | [X.X%] | [+X.X%] |

### Resolution Options (If Fail)
1. **Reduce proposed trade size** to [$XXmm] to stay within [specific] limit
2. **Sell existing exposure** to [issuer/sector] to create headroom
3. **Request formal exception** from IC / CIO with documented rationale (exceptions are time-limited and must specify a remediation plan)
4. **Decline the trade** — mandate limits are hard constraints

---

## Sign-Off

| Role | Name | Date | Signature |
|---|---|---|---|
| Analyst (Preparer) | | | |
| Portfolio Manager | | | |
| Compliance Officer | | | |

**Compliance Note:** Retain the completed template in the trade file for the period required by the governing regulation, fund documents, and internal retention policy. Any exception granted should be documented separately with approval authority and a remediation timeline.
