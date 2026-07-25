---
last_updated: "2026-03-21"
update_cadence: semi-annually
next_review: "2026-09-21"
data_vintage: "H1 2026"
sources:
  - "Internal risk management framework"
  - "Industry standard risk parameters"
  - "Regulatory requirements (SEC, Investment Company Act)"
---

# Portfolio Risk Parameters Reference

**Last Updated:** March 2026
**Update Cadence:** Semi-annually
**Next Review:** September 2026

This file contains all numeric risk appetite parameters used in portfolio construction and mandate compliance. Values are calibrated for a broadly syndicated leveraged credit portfolio and should be customized per fund type (see Fund-Type Customization below). For the framework explaining how these parameters govern investment decisions, see `skills/portfolio-investment-process/references/risk-appetite-and-limit-framework.md`.

---

## 1. Overall Portfolio Parameters

Return and risk targets for the portfolio as a whole. These set the performance envelope within which the PM operates.

```yaml
portfolio_parameters:
  target_gross_return: "8-10%"          # Annualized gross return target
  target_net_return: "6-8%"             # Annualized net return (after fees, expenses)
  maximum_drawdown: "-8%"               # Maximum peak-to-trough NAV decline before mandatory review
  volatility_target: "3-5%"             # Annualized NAV volatility (monthly, rolling 12-month)
  tracking_error: "N/A"                 # vs. benchmark (if applicable)
  information_ratio_target: ">1.0"      # Excess return per unit of tracking error
  sharpe_ratio_floor: "0.8"             # Minimum acceptable risk-adjusted return
```

**When to update:** Revisit when base rates shift materially (>100 bps), fund strategy changes, or investor expectations are reset at annual meetings.

---

## 2. Concentration Limits

Position, sector, rating, and geography concentration limits. Each parameter has a target (optimal), soft limit (triggers PM review), and hard limit (triggers mandatory IC action).

```yaml
concentration_limits:
  single_name:
    target: "1.5-2.0%"                 # Optimal position size
    soft_limit: "3.0%"                  # Triggers PM review
    hard_limit: "5.0%"                  # Maximum; requires IC exception above this
  sector:
    target: "10-15%"                    # Per GICS sector
    soft_limit: "20%"
    hard_limit: "25%"
  sub_sector:
    target: "5-8%"                      # Per GICS sub-industry
    soft_limit: "12%"
    hard_limit: "15%"
  rating_bucket:
    ccc_and_below:
      target: "0-5%"
      soft_limit: "7.5%"
      hard_limit: "10%"
  geography:
    non_us_developed:
      target: "10-20%"
      soft_limit: "25%"
      hard_limit: "30%"
    emerging_markets:
      target: "0-5%"
      soft_limit: "7.5%"
      hard_limit: "10%"
  sponsor:
    single_sponsor: "5%"               # Maximum exposure to credits controlled by one PE sponsor
```

**When to update:** Revisit when portfolio AUM changes significantly, new asset classes are added, or after stress events that reveal hidden correlations.

---

## 3. Instrument Limits

Minimum and maximum allocations by instrument type. These ensure the portfolio maintains the desired risk profile and structural seniority.

```yaml
instrument_limits:
  senior_secured_loans:
    minimum: "40%"
    maximum: "100%"
  senior_unsecured_bonds:
    maximum: "40%"
  second_lien:
    maximum: "15%"
  mezzanine_subordinated:
    maximum: "10%"
  structured_products:                  # CLO tranches, ABS
    maximum: "15%"
  equity_equity_linked:
    maximum: "5%"
  cds_derivatives:
    gross_notional_max: "20%"           # As % of NAV
  pik_deferred_interest:
    maximum: "10%"
  covenant_lite:
    maximum: "80%"                      # Market reality; tighter for conservative mandates
```

**When to update:** Revisit when new instrument types are added to the investable universe or when market structure shifts (e.g., cov-lite share changes materially).

---

## 4. Liquidity Parameters

Cash, liquidity reserve, and redemption coverage requirements. Critical for open-end structures and any fund with redemption features.

```yaml
liquidity_parameters:
  minimum_cash:
    target: "3-5%"
    hard_minimum: "2%"
  liquidity_reserve:                    # Tier 1 + Tier 2 assets
    minimum: "25%"                      # Sufficient to cover 30-day redemption stress
  redemption_buffer:
    coverage_ratio: "1.5x"             # Liquid assets / estimated 30-day redemption
  maximum_illiquid:
    tier_4: "15%"                       # Assets requiring >30 days to liquidate
  bid_ask_monitoring:
    average_spread_alert: "200 bps"     # Portfolio-weighted average bid-ask; triggers liquidity review
```

**When to update:** Revisit when fund structure changes, redemption terms are modified, or after periods of market stress that test liquidity assumptions.

---

## 5. Rating Distribution Targets

Target credit quality mix. Ensures the portfolio stays within the intended risk band and does not drift into unintended credit quality buckets.

```yaml
rating_distribution:
  investment_grade:                     # BBB- and above
    target: "0-5%"
    maximum: "15%"
  bb:
    target: "30-40%"
    minimum: "20%"
    maximum: "50%"
  b:
    target: "40-50%"
    minimum: "30%"
    maximum: "60%"
  ccc:
    target: "0-5%"
    maximum: "10%"
  not_rated:
    maximum: "10%"
  weighted_average_rating:
    target: "B+"
    minimum: "B"                        # Below this triggers IC review
```

**When to update:** Revisit when the credit cycle shifts (e.g., wave of downgrades), fund strategy pivots, or rating agency methodology changes.

---

## 6. Duration and WAL Constraints

Weighted average life, spread duration, and maturity concentration limits. These manage reinvestment risk and maturity wall exposure.

```yaml
duration_constraints:
  weighted_average_life:
    target: "3.0-4.5 years"
    maximum: "5.5 years"
  spread_duration:
    target: "3.0-4.0 years"
    maximum: "5.0 years"
  effective_duration:
    target: "0.2-0.5 years"            # Low for floating-rate portfolios
    maximum: "1.0 year"
  maturity_concentration:
    single_year: "20%"                  # Maximum maturing in any single calendar year
    two_year_wall: "35%"                # Maximum maturing within 24 months
```

**When to update:** Revisit when interest rate outlook changes significantly or when portfolio repositioning shifts the maturity profile.

---

## Fund-Type Customization

The parameters above are calibrated for a broadly syndicated leveraged credit portfolio. The tables below show how specific fund structures typically adjust these base parameters to reflect their regulatory, structural, and investor requirements.

### CLO

| Parameter | Typical CLO Adjustment |
|---|---|
| CCC bucket | Hard limit 7.5% (par haircut above this per indenture) |
| WAL test | Maximum 5.0-7.0 years (declining over reinvestment period) |
| Single-name | 2.0% hard limit |
| Industry diversity | Minimum 15-20 Moody's industries; maximum 8-12% per industry |
| Second lien | Maximum 5-10% |
| Caa concentration | Separate tracking; excess Caa treated at market value not par |
| Reinvestment criteria | Must meet all OC/IC tests post-trade; no defaulted assets purchased |

### BDC

| Parameter | Typical BDC Adjustment |
|---|---|
| Asset coverage | Minimum 150% (regulatory requirement; 200% pre-2018 election) |
| Qualifying assets | Minimum 70% of total assets (eligible portfolio company investments) |
| Single-name | 5-10% (higher due to concentrated strategy) |
| Income distribution | Minimum 90% of investment company taxable income |
| Leverage cap | 2.0x debt-to-equity (regulatory maximum) |
| Non-qualifying | Maximum 30% of total assets (public securities, foreign companies) |
| PIK income | Track separately; maximum 15-20% of total investment income |

### Open-End Fund

| Parameter | Typical Open-End Adjustment |
|---|---|
| Liquidity buckets | Minimum 15% in Tier 1 (daily liquid); maximum 15% illiquid (SEC Rule 22e-4) |
| Redemption management | Model 10% monthly redemption stress; maintain 1.5x coverage |
| NAV impact | Maximum 25 bps NAV impact from single-name default |
| Cash buffer | Higher minimum (5%) to absorb daily flows |
| Leverage | Limited; typically 0-33% borrowing capacity |

### SMA (Separately Managed Account)

| Parameter | Typical SMA Adjustment |
|---|---|
| Concentration | Client-specific; typically 3-5% single-name |
| ESG exclusions | Per client IPS (investment policy statement) |
| Sector restrictions | Per client guidelines (e.g., no tobacco, no firearms) |
| Rating floor | Often B- or B; some clients require BB- minimum |
| Instrument restrictions | May exclude CDS, structured products, or second lien |
| Reporting | Monthly or quarterly per IMA (investment management agreement) |
