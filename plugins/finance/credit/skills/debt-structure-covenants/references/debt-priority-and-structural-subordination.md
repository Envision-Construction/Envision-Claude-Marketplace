---
last_updated: "2026-03-22"
---

## Debt Priority and Structural Subordination

Formal seniority (priority ranking) determines recovery in a default or liquidation. But practical recovery depends on collateral coverage, guarantee structure, and structural subordination.

## Priority Hierarchy (Highest to Lowest Recovery)

```
1. Senior Secured (Bank Loans)
   ↓
2. Senior Unsecured (Traditional HY Bonds)
   ↓
3. Senior Subordinated
   ↓
4. Subordinated ("Mezzanine")
   ↓
5. Preferred Stock
   ↓
6. Common Equity
```

## Senior Secured vs. Senior Unsecured

**Senior Secured**
- Definition: Debt with first lien position on specified collateral (assets of the company)
- Collateral: Typically first-lien on all assets—property, plant, equipment, inventory, receivables, IP, etc.
- Lien priority: If company has multiple layers of debt, senior secured creditors get "first claim" on asset sale proceeds
- Typical vehicle: Bank loans (term loans, revolvers)
- Recovery profile: Unsecured subordinated creditors only recover if senior secured lenders are 100% repaid first
- Example: Company with $500M assets, $300M senior secured bank debt, $200M senior unsecured bonds. In a $400M asset sale, senior secured gets up to $300M (fully paid); senior unsecured splits remaining $100M.

**Senior Unsecured**
- Definition: Unsecured debt with formal seniority over subordinated and junior layers
- No collateral: No specific lien; claim is on residual value after senior secured liens are satisfied
- Covenant protection: Usually has financial maintenance covenants (leverage tests, interest coverage)
- Typical vehicle: Most high-yield bonds
- Recovery profile: Recovers after senior secured; recovers before subordinated
- Ranking note: "Senior" refers to unsecured ranking, not to secured status. Can be structurally subordinated if issued at HoldCo level.

**Key Distinction: Secured vs. Seniority**
- A bond can be "senior unsecured" (no lien, but high unsecured priority)
- A bond can be "senior secured" (first lien, highest priority)
- A bond can be "subordinated" (formal junior ranking, even if secured)
- **Read carefully**: Labels can be misleading. "Senior" ≠ "has security." Must review security agreement and lien position.

## Security and Collateral

**What is Collateral?**
- Specific lien on company assets: property, equipment, inventory, accounts receivable, IP, cash, subsidiary stock
- Defined in: Security agreement (for personal property), mortgage (for real property), collateral agreement (summary)
- Exclusions: Foreign subsidiaries typically NOT pledged (regulatory/treaty reasons); excludes certain assets (e.g., licensed IP, regulated operations)

**Secured vs. Unsecured Recovery**
- Secured creditors get first lien proceeds; unsecured creditors (senior or subordinated) share remaining asset sale value
- Example:
  - Company: $600M in assets, $400M senior secured debt, $200M senior unsecured debt, $100M subordinated debt
  - Liquidation: Assets sell for $450M
  - Senior secured: Gets full $400M; $50M shortfall (note: this shortfall is unsecured claim, sharing with other unsecured)
  - Senior unsecured: $50M × ($200M / $300M) = $33.3M (50% recovery)
  - Subordinated: $50M × ($100M / $300M) = $16.7M (16.7% recovery)

## Pari Passu ("Equal Ranking")

**Definition**: Creditors at the same seniority level rank equally and share pro rata on collateral or liquidation proceeds.

**Pro Rata Mechanics**:
- If two bonds are pari passu and $100M is available for repayment:
  - Bond A: $200M outstanding
  - Bond B: $300M outstanding
  - Bond A receives: $100M × ($200M / $500M) = $40M
  - Bond B receives: $100M × ($300M / $500M) = $60M

**Subtleties in Pari Passu**:
- Pari passu does NOT always mean identical treatment
- Example: Revolver (pari passu in ranking) may have "first out" mechanics on asset sales, getting paid before other pari passu creditors
- Example: Guarantee structure can override pari passu. New debt with subsidiary guarantee can be paid ahead of unguaranteed pari passu bonds (see Structural Subordination below)
- **Read definitions carefully**: Pari passu bond document ≠ pari passu in practice if cross-collateralization or guarantee mechanics exist

---

## Structural Subordination

Structural subordination occurs when debt issued at a higher level in the corporate structure (holding company) is effectively junior to debt at lower levels (operating company), even if labeled "senior."

### HoldCo vs. OpCo Structure

**Typical Setup**:
```
                   HoldCo (Sponsor-owned parent)
                        |
                   [Senior Notes]
                        |
                    OpCo (Operating subsidiary)
                    /    |    \
        [Bank Loan] [Sr Sub] [Revolving Credit]
                    |
            Asset/Cash Flow
```

- **HoldCo debt**: Issued by parent holding company; unsecured claim on OpCo equity and dividends
- **OpCo debt**: Issued by operating subsidiary; direct claim on operating assets and cash flow
- **Structural subordination**: HoldCo noteholders can only recover from OpCo *after* OpCo debt is satisfied; OpCo is "bankruptcy-remote" and can be shielded from HoldCo obligations

### Why Use HoldCo Structure?

1. **Bank leverage limits**: Senior lenders (bank) cap leverage at OpCo level (e.g., 3.5x). Additional debt issued at HoldCo to avoid triggering lender consent
2. **Covenant restrictions**: OpCo debt may restrict additional OpCo-level borrowing. New debt issued at HoldCo to bypass restrictions.
3. **Expansion financing**: Sponsor acquires new subsidiary and wants to limit guarantees from existing OpCo. New acquisition debt sits at HoldCo or new sub.
4. **Preferred equity structures**: Preferred stock issued at HoldCo avoids OpCo subsidiary guarantee restrictions.

### Structural Subordination in Practice

**Example Structure**:
- OpCo: Bank loan $300M, Senior Subordinated Notes $150M
- HoldCo: Senior Notes $100M
- Formal ranking: Bank loan (Secured), Sr Sub Notes & Senior Notes (Unsecured, pari passu)
- Practical ranking:
  - Bank loan gets first claim on OpCo assets
  - Sr Sub Notes (OpCo-issued) get second claim on OpCo assets
  - **HoldCo Senior Notes get claim ONLY on residual after Sr Sub Notes paid** ← Structurally subordinated
  - If OpCo liquidates and assets sell for $400M:
    - Bank loan: full recovery ($300M)
    - Sr Sub Notes: $100M (full recovery)
    - HoldCo Senior Notes: $0 (no recovery, even though "Senior" in name)

### Cross-Default Provisions

**Definition**: Default at one entity in the structure triggers default at all other entities.

**Example**:
- OpCo defaults on bank loan
- Cross-default clause: Triggers default on OpCo Sr Sub Notes and HoldCo Senior Notes simultaneously
- Effect: Creditors at all levels can accelerate and seek repayment

**Benefit to lenders**: Prevents OpCo from selectively defaulting on OpCo bonds while trying to pay HoldCo obligations (or vice versa).

**Risk to HoldCo noteholders**: Default can cascade unexpectedly; HoldCo structure does not insulate them from OpCo operational issues.

### Subsidiary Guarantees: Override to Structural Subordination

**Guarantee Definition**: Subsidiary pledges its assets and credit to support parent-level (HoldCo) debt.

**Guarantee Mechanics**:
- HoldCo issues Senior Notes $100M
- OpCo **guarantees** repayment of HoldCo notes
- HoldCo notes are now an obligation of OpCo's assets (in addition to OpCo's own debt)
- Recovery: HoldCo noteholders can file claim directly on OpCo assets; no longer limited to residual after OpCo debt

**Senior Guarantee vs. Subordinated Guarantee**:
- **Senior Guarantee**: HoldCo notes are guaranteed by OpCo. Guarantee is not subordinated; HoldCo notes rank *pari passu* with or *senior to* OpCo's own unsecured debt
  - Example: OpCo guarantees HoldCo Senior Notes as **Senior Guarantee**. HoldCo notes rank pari passu with OpCo Sr Sub Notes on OpCo assets.
- **Subordinated Guarantee**: HoldCo notes are guaranteed, but guarantee is subordinated to OpCo's own debt
  - Example: OpCo guarantees HoldCo notes as **Subordinated Guarantee**. HoldCo notes rank junior to OpCo Sr Sub Notes, but senior to OpCo's subordinated debt.

**Effect of Guarantee on Structural Subordination**:
- **Without guarantee**: HoldCo notes are structurally subordinated to all OpCo debt
- **With senior guarantee**: HoldCo notes "prime" or equal OpCo unsecured debt
- **With subordinated guarantee**: HoldCo notes are junior to OpCo's senior debt but senior to OpCo's junior debt

### "Priming" and Negative Pledge

**"Primed" Defined**: Existing bondholders find their position weakened when new, structurally senior debt is issued.

**Example**:
- HoldCo has Senior Unsecured Notes (unguaranteed by OpCo)
- New debt: HoldCo issues new Senior Notes with OpCo **Senior Guarantee**
- Effect: New Senior Notes "prime" the old Senior Notes. Old notes are now effectively subordinated to new notes' guarantee.
- Bondholder reaction: Old notes decline in value; issuer was able to weaken existing bondholders' position without their consent.

**Negative Pledge Covenant**:
- Old bond covenants: "If HoldCo grants security or guarantee to any creditor, HoldCo grants equal security/guarantee to these notes"
- Purpose: Prevent issuer from "priming" existing bonds with new secured debt
- Mechanics: If issuer grants guarantee to new debt, automatically must grant same guarantee to old bonds
- Effect: Prevents selective guarantee issuance; new bonds cannot leapfrog old bonds

**Example of Negative Pledge in Action**:
- HoldCo Senior Notes 2028 have negative pledge clause
- Issuer wants to issue HoldCo Senior Notes 2035 with OpCo guarantee
- Negative pledge requires 2028 notes also get OpCo guarantee
- Result: Both 2028 and 2035 notes share OpCo guarantee *pari passu*; no priming

### Visual Structure Examples

#### Basic HoldCo / OpCo with Structural Subordination

```
                        Sponsor/Equity
                             |
                        ┌────HoldCo────┐
                        |               |
                    [Sr Notes]      [Preferred]
                        |
                    ┌───OpCo───┐
                    |          |
            [Bank Loan]   [Sr Sub Notes]
                    |
            Operating Assets
            & Cash Flow
```

**Recovery Waterfall in Distress**:
1. Bank Loan -> Direct claim on OpCo assets
2. Sr Sub Notes -> Direct claim on OpCo residual after Bank Loan
3. HoldCo Sr Notes -> Claim on OpCo residual after Sr Sub Notes (structural subordination!)
4. Preferred -> Claim on OpCo residual or HoldCo equity value

#### HoldCo / OpCo with Subsidiary Guarantee (Removes Structural Subordination)

```
                        HoldCo
                        |
                   [Sr Notes +
                    OpCo Guarantee]
                        |
                    ┌───OpCo───┐
                    |          |
            [Bank Loan]   [Sr Sub Notes]
                    |
            Operating Assets
            & Cash Flow
```

**Recovery Waterfall in Distress**:
1. Bank Loan -> Senior Secured lien on OpCo assets
2. Sr Sub Notes -> Unsecured claim on OpCo residual (ranking below bank loan)
3. HoldCo Sr Notes (with OpCo guarantee) -> Unsecured claim on OpCo residual, **pari passu with Sr Sub Notes** (guarantee removes structural subordination!)

---
