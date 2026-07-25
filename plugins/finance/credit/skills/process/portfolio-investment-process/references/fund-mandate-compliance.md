---
last_updated: "2026-03-22"
---

# Fund Mandate Compliance by Vehicle Type

Mandate constraints vary significantly across fund structures. This reference covers the analytical framework for checking mandate compliance across CLOs, BDCs, open-end funds, and SMAs. Mandate compliance must be verified before any IC recommendation. A trade that breaches a binding mandate limit is a hard stop regardless of investment merit.

> **Current regulatory and mandate constraints:** Use the governing indenture, prospectus, IMA, side letter, or other fund documents for live vehicle limits. For BDC-backed private credit positions, use `skills/private-credit-middle-market/references/bdc-regulatory.md` for the BDC-specific regulatory thresholds that commonly bind.

---

## CLO Mandate Compliance

CLO indentures impose structural tests that, if breached, redirect cash flows from equity to debt. These are not advisory limits — they are contractual. OC/IC tests, CCC bucket limits, WAL tests, diversity scores, and concentration limits all must be checked before any reinvestment trade.

**Why CLO constraints matter for credit analysis:** Unlike fund-level guidelines that may allow temporary breaches with board approval, CLO test failures trigger automatic cash flow diversion. A manager cannot choose to waive a failed OC test. This makes pre-trade compliance modeling essential — the cost of a failed test is immediate and mechanical.

### CLO Compliance Checklist

Before any CLO reinvestment trade:
- [ ] Post-trade OC test (all tranches): Pass / Maintain / Improve
- [ ] Post-trade IC test (all tranches): Pass / Maintain / Improve
- [ ] Post-trade WAL test: Within limit
- [ ] Post-trade WAS test: Above minimum
- [ ] Post-trade diversity score: Above minimum
- [ ] Single obligor: Below maximum
- [ ] Industry concentration: Below maximum per industry
- [ ] CCC bucket: Below threshold (or calculate haircut impact)
- [ ] Second lien allocation: Below maximum
- [ ] Asset is not a defaulted security
- [ ] Asset meets definition of "collateral obligation" per indenture

---

## BDC Mandate Compliance

BDCs operate under the Investment Company Act of 1940 with specific exemptions. Regulatory compliance is audited and reported publicly. Asset coverage, qualifying asset tests, and RIC status requirements all impose binding constraints on portfolio composition and leverage.

**Why BDC constraints matter for credit analysis:** BDC regulatory limits are not just risk management tools — they directly constrain the investment opportunity set. The qualifying asset test prevents free rotation into large-cap credits. The asset coverage test means NAV declines can force deleveraging into weak markets. The income distribution requirement limits the BDC's ability to build equity cushion from retained earnings.

### BDC Compliance Checklist

Before any BDC investment:
- [ ] Post-trade asset coverage ratio: Above regulatory minimum (check election status)
- [ ] Qualifying asset test: Above required minimum post-trade
- [ ] Issuer qualifies as eligible portfolio company (private or public below market cap threshold)
- [ ] Co-investment: Compliance with exemptive order allocation procedures
- [ ] Leverage utilization: Within facility covenants and regulatory limits
- [ ] Concentration limits per credit facility covenants (industry, single-name, rating)
- [ ] PIK component: Quantified and within board-approved guidelines
- [ ] Distributable income impact: Modeled for next 4 quarters

---

## Open-End Fund Mandate Compliance

Open-end credit funds face the additional challenge of managing daily liquidity against potentially illiquid credit assets. SEC Rule 22e-4 imposes liquidity classification requirements and caps on illiquid holdings.

**Why open-end fund constraints matter for credit analysis:** The tension between daily redemptions and illiquid credit assets creates a structural vulnerability. During market stress, redemptions accelerate while bid-ask spreads widen — forcing sales of liquid positions first, which concentrates the portfolio in illiquid holdings and risks breaching the illiquid cap. Pre-trade liquidity modeling is therefore as important as credit analysis.

### Open-End Fund Compliance Checklist

Before any trade:
- [ ] Post-trade illiquid allocation: Below regulatory maximum
- [ ] Post-trade highly liquid allocation: Above board-approved minimum
- [ ] Borrowing: Within regulatory limit
- [ ] Derivatives notional: Within Rule 18f-4 framework
- [ ] Redemption stress: Portfolio can meet estimated monthly redemption from liquid buckets
- [ ] NAV impact: Single-name default impact within acceptable range
- [ ] Concentration limits per prospectus (single-name, sector, rating)

---

## SMA Mandate Compliance

SMAs are governed by the Investment Management Agreement (IMA) between the manager and the client. Constraints are client-specific and often more restrictive than pooled vehicles. Every SMA has a unique set of limits that must be verified against the IMA before trading.

**Why SMA constraints matter for credit analysis:** SMA clients frequently impose restrictions that reflect their own risk preferences, regulatory requirements (insurance companies, pension funds), or ESG mandates. A credit that passes all investment merit tests may still be ineligible for a given SMA due to rating floors, sector exclusions, or instrument restrictions. Compliance must be verified per-account, not at the strategy level.

### SMA Compliance Checklist

Before any SMA trade:
- [ ] Post-trade single-name: Within IMA limit
- [ ] Post-trade sector: Within IMA limit
- [ ] Rating: Meets minimum rating requirement
- [ ] ESG screen: Issuer not on client exclusion list
- [ ] Instrument type: Permitted under IMA
- [ ] Geographic eligibility: Within permitted regions
- [ ] Issue size: Meets minimum
- [ ] WAL: Post-trade portfolio WAL within limit
- [ ] Client-specific restrictions: All additional IMA constraints verified

---

## Pre-IC Mandate Check Process

1. **Analyst identifies the target fund(s)** for the proposed investment
2. **Pull current portfolio state** for each target fund — positions, concentrations, test levels
3. **Run post-trade compliance** against all applicable constraints for the fund type using the governing vehicle documents and, for BDC private credit positions, `skills/private-credit-middle-market/references/bdc-regulatory.md`
4. **Document results** in the mandate compliance template (see `references/mandate-compliance-template.md`)
5. **If any hard limit breached:** Trade cannot proceed; identify resolution options (reduce size, sell existing exposure, or decline)
6. **If soft limit approached:** Flag in IC memo with justification and remediation plan
7. **Attach completed checklist** to the IC memo as a mandatory appendix

---

## Cross-Fund Allocation

When allocating a single investment across multiple fund vehicles:
- Each fund must independently pass its own mandate compliance check
- Allocation methodology must be documented and consistent with regulatory requirements (BDC co-investment orders, SMA IMA provisions)
- If one fund fails compliance but others pass, the trade may proceed for passing funds only
- Fair allocation policies must be followed per the firm's compliance manual

---

## Open-End Fund Liquidity-Adjusted Position Sizing

Open-end funds must classify holdings by liquidity and size positions so that redemption risk does not force the fund into the wrong assets at the wrong time. Use the applicable prospectus and liquidity-risk framework documents for the current regulatory definitions and thresholds.

### Liquidity-Adjusted Sizing Formula

```
Available Illiquid Capacity = (Total Portfolio x Current Illiquid Limit) - Current Illiquid Holdings
Maximum New Illiquid Position = MIN(Credit-Based Limit, Available Illiquid Capacity)
```

Use the current limit from the applicable fund documents and preserve headroom for mark volatility, migration between buckets, and correlated redemption pressure.

### Practical Considerations

- Liquidity classification should be revisited periodically; a position that looked tradeable in a calm market can become effectively illiquid in stress
- Private credit positions are typically classified as illiquid by default
- Bank loans with active secondary markets may qualify as "moderately liquid" or "less liquid" depending on issue size and trading volume
- Aggregate illiquid limit applies across all illiquid asset types — a large CRE debt position may crowd out private credit capacity
