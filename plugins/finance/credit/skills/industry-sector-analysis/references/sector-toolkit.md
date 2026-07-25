---
last_updated: "2026-03-22"
---

# Sector Analysis Toolkit

Concise companion to the canonical default sector framework (`references/cross-asset-sector-framework.md`). Use for quick framing before deep dives.

**Path resolution**: Paths shown as `references/...` are skill-local unless marked **(root)**. Skill-local files live under `skills/industry-sector-analysis/references/`. **(root)** means the shared project file at `references/<same path>` (repo root).

## Cyclical and Secular Framing

- **Spectrum**: Highly cyclical (commodity, autos, building, transport) -> moderately cyclical (diversified industrials, specialty chem, some media/hardware) -> defensive (regulated utilities, waste, staples, parts of healthcare).
- **Cyclical traits**: demand tied to capex/housing/commodities; high fixed cost amplifies revenue moves; WC release helps briefly but does not fix earnings.
- **Defensive traits**: essential/recurring/regulated demand; lower volume volatility; risk often reimbursement, regulation, labor inflation, or policy--not macro demand alone.
- **Secular vs cyclical test**: If macro returned to a prior peak, would economics recover? If no, the issue is at least partly secular (misidentifying secular decline as a trough is a common error).
- **Leverage / liquidity**: cyclical names need trough-capable leverage and liquidity through recovery, not just the first shock; long-cycle capex sectors need extra runway.
- **Stress sequence**: (1) pick relevant historical or model downturn, (2) label cyclical vs secular vs both, (3) map revenue, margin, WC, capex, (4) test liquidity and covenants on a multi-quarter path, (5) re-check leverage on trough earnings.

## Pricing Power and Pass-Through

**Definition knobs**: differentiation, switching costs, market structure, demand elasticity, buyer concentration, regulatory pricing.

| Revenue pattern (3-5y) | Signal |
| --- | --- |
| Steady price contribution (>~2% real) | Strong |
| Price volatile / sometimes negative | Moderate |
| Price consistently negative | Weak / price taker |
| Price up, volume down | Short-term OK, longer-term demand risk |

**Gross margin vs inputs**: stable GM with rising costs = pass-through; compress then recover in 1-2Q = lagged pass-through; no recovery = weak pass-through.

**Pass-through lag (typical)**:

| Mechanism | Lag |
| --- | --- |
| Surcharge / index | Days to 90d |
| Spot / competitive repricing | 1-3 mo |
| Menu / list price | 3-6 mo |
| Annual renewal | 6-12 mo |
| Multi-year fixed | Until renewal |

**Margin outlook cheat sheet**: strong + rising costs -> stable/expand; weak + rising costs -> model 200-400bps multi-quarter squeeze; weak pricing power -> cut max sustainable leverage ~0.5-1.0x vs sector avg and widen scenarios.

**Checklist (high level)**: decompose revenue (price/volume/mix); GM vs input costs; escalators/surcharges/index; structure and switching costs; customer concentration; peer pricing behavior; fixed-price contract %.

## Cross-Sector Comparison Shortcuts

**Archetype lenses** (what to stress first):

| Archetype | Focus |
| --- | --- |
| Defensive essentials | Regulation, reimbursement, pass-through vs topline cyclicality |
| Asset-light recurring | Retention, pricing, concentration, addback quality |
| Lease-heavy consumer / service | Rent-adjusted leverage, units, location/route quality |
| Commodity / price-taking | Normalized earnings, liquidity, cost position |
| Cyclical manufacturers | Utilization, backlog, WC swings |
| Backlog / project-led | Program conversion, milestones, contract risk |

**Peer selection prompts**:

1. Sub-sector vs headline sector label?
2. Dominant risk: cyclical, regulatory, recurring revenue, or balance sheet?
3. Right metric: EBITDA, EBITDAR, FFO, tangible equity, or capital ratios?
4. Are margins/volumes above through-cycle?
5. Customer/program/geo concentration vs sector average?

**Practical output**: name archetype; top 2-3 comparison dimensions; why tighter/looser than sector median. Sector-specific comps and traps: `references/industry/`.

## Sector Leverage Calibration Prompts

**Apply in order**: (1) shared benchmark from `references/rating-agency-thresholds.md` **(root)**, (2) earnings volatility, (3) revenue visibility, (4) capex / maintenance / WC intensity, (5) accounting distortions (leases, SBC, reserves, backlog), (6) concentration, (7) financial policy.

**Archetype calibration**:

| Archetype | Lean |
| --- | --- |
| Regulated / essential | More leverage if visibility real; watch political/reg shock |
| Recurring / asset-light | More than generic industrial if retention + FCF durable |
| Lease-heavy consumer / service | Debt/EBITDA understates; rent-adjust |
| Commodity / price-taking | Tightest; normalize earnings |
| Cyclical manufacturing | Through-cycle / trough basis |
| Contracted / backlog | Backlog only if conversion quality strong |
| Financial / BS-led | EBITDA often wrong lens; use capital/funding metrics |

**Named sectors**: Use the relevant file under `references/industry/` for sector-specific leverage hooks and KPIs instead of duplicating a sector index here.

**Common mistakes**: sector average as verdict; peak earnings in cyclicals; ignoring lease/SBC/reserve/WC; defensive demand confused with strong FCF; comparing banks to corporates on Debt/EBITDA alone.

## Sector Documentation Watchpoints

Read after you understand the business model. For current covenant and LME cycle terms, use `references/credit-agreement-trends-documentation-risk.md` **(root)**.

**By business model**:

| Model | Watch |
| --- | --- |
| Roll-up / M&A-heavy | Recurring addbacks, run-rate synergies, large acquisition baskets, earnouts |
| Lease-heavy | Rent in covenants, economic debt, exit friction, FF&E/fleet reality |
| Commodity / resource | Favorable price decks, hedging optics, RBL/collateral tests, reclamation |
| Backlog / program-led | Backlog as cash, POC/milestone EBITDA, bonding/LDs, incremental debt on unconverted backlog |
| Regulated / licensed | Change-of-control vs licenses, compliance reps, ring-fence, min capital/liquidity |

**Sector clusters** (doc theme -> first look): **Healthcare / TMT** addbacks and definitions (EBITDA/ARR, SBC); **Energy / Chemicals / Metals** price and collateral normalization; **Retail / Gaming / Transport / Auto** lease and WC; **Industrials / Aero / Building / Packaging** cycle, backlog, execution; **Financials** capital and funding triggers; **Utilities / Environmental** ring-fence and environmental reserves. Detail by name: `references/industry/`.

**Red flags**: same addback yearly; EBITDA excludes spend needed to sustain the model; capacity assumes optimistic backlog/ARR/synergies; ignores rent/reserves/reclamation; large RP/M&A capacity into weakness.

## Supply-Chain Vulnerability

**Four dimensions**:

| Dimension | Low risk | High risk |
| --- | --- | --- |
| Geography | Diversified stable sourcing | Critical inputs in one region/corridor |
| Supplier concentration | Many substitutes | Sole-source or few vendors |
| Substitutability | Commodity / swappable | Qualified/regulated/slow switch |
| Inventory buffer | Can hold safety stock | JIT or perishable, little buffer |

**Archetypes**: JIT assembly (stops on one part); qualified inputs (aerospace, pharma); commodity inputs (price/timing volatility); route/logistics dependent (ports, freight); asset-light digital (lower direct chain risk; still vendor concentration).

**High-risk signals**: production stops on single component; long requalification; model needs minimal inventory; fragile geography; customer penalties for late delivery.

**Credit channels**: revenue stop; margin hit (alternate source, expedite); WC strain (inventory, prepay); capex (dual-source, nearshore); customer concentration amplifies.

**Management**: positive = multi-sourcing, tier-2+ mapping, safety stock where needed, flexible logistics; negative = single-source, blind past tier-1, JIT where cost of failure is extreme.

**Stress framing**: duration until break; recoverable vs lost demand; margin from alternates/freight/under-absorption; liquidity to stabilize.

**Mistakes**: treat structural concentration as temporary; only watch commodity price not availability; ignore inventory liquidity cost; ignore shelf space/program loss from delays.

---

**Navigation**: `references/cross-asset-sector-framework.md` (default framework); `references/technology-disruption-timeline.md` (horizon framing); sector files in `references/industry/`. Root: `references/rating-agency-thresholds.md`, `references/market-benchmarks.md`, `references/stress-scenario-framework.md`, `references/credit-agreement-trends-documentation-risk.md`.
