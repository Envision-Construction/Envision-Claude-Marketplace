---
last_updated: "2026-03-22"
---

## CRE Loan Covenants & Cash Management

CRE covenants are asset-level and cash-control-focused. The lender is underwriting a property, its rents, and its refinanceability, so the covenant package is designed to protect collateral value and control cash leakage earlier than a typical corporate loan agreement.

For property-level underwriting, sizing, valuation, and current market norms, use `cre-analysis-underwriting` plus root references such as `references/typical-deal-parameters.md`. This document is the narrow bridge for document mechanics.

### Core Covenant Families

**Performance tests**
- DSCR, debt yield, occupancy, and related triggers test whether property cash flow still supports the loan
- These covenants matter because a decline in NOI can quickly become a cash-control or default issue rather than just a reporting issue

**Value and structure tests**
- LTV retesting, appraisal rights, subordinate-debt restrictions, and transfer limits protect collateral value and seniority
- The key question is not just whether the loan starts at a conservative leverage point, but whether the document lets the lender react if value falls or new debt is introduced

**Single-asset and separateness protections**
- SPE covenants, separateness requirements, independent directors, and anti-commingling rules are designed to keep the asset isolated from sponsor-level distress
- In CMBS and similar structures, these provisions are part of the bankruptcy-remoteness package, not just administrative formalities

### Cash Management Structures

CRE documents often protect lenders by controlling where rents go and how they are applied.

| Structure | Core Mechanic | Why It Matters |
|---|---|---|
| Hard lockbox | Rents flow directly into a lender- or servicer-controlled account | Gives the lender immediate control of operating cash |
| Springing lockbox | Borrower has more flexibility until a trigger event occurs | Converts operational underperformance into tighter lender control |
| Cash trap | Excess cash is retained rather than distributed | Preserves cash inside the structure without fully taking over operations |
| Cash sweep | Excess cash is applied to debt paydown | Forces deleveraging rather than allowing distributions |

### Waterfall Review

When reviewing CRE cash management, confirm the order of cash application:
1. Property operating expenses and required carry costs
2. Debt service
3. Reserves and escrows
4. Excess cash to borrower, trapped cash account, or mandatory sweep

This order determines how quickly equity can be cut off and how much operating flexibility remains after a trigger event.

### Trigger Analysis

The analytical question is not only whether a trigger exists, but what it does once tripped.

Check:
- Which performance or appraisal events activate lockbox, trap, or sweep features
- Whether distributions are automatically blocked upon trigger
- What cure paths exist: paydown, waiver, operational improvement, additional reserve funding, or rebalancing
- Whether a cured trigger automatically resets, or whether lender consent is required to restore flexibility

### Lease and Property Control Rights

CRE covenant packages often give lenders control over actions that would be routine in corporate loans.

Review:
- Approval rights for large leases, lease modifications, and tenant concessions
- Notice requirements around major-tenant defaults or occupancy deterioration
- Reserve mechanics for TI/LC, replacement capex, taxes, and insurance
- Insurance, casualty, condemnation, and environmental provisions that can redirect proceeds away from equity

### CMBS and Securitized Variants

CMBS and related securitized CRE structures often add:
- Servicing transfer mechanics and special-servicing triggers
- Defeasance or strict prepayment restrictions
- Tighter SPE and transfer restrictions
- Limits on subordinate debt and mezzanine flexibility unless expressly permitted

### Comparison to Corporate Covenant Analysis

| Feature | CRE Loan Documents | Corporate Loan Documents |
|---|---|---|
| Testing basis | Property cash flow and collateral value | Consolidated issuer performance |
| Cash control | Lockbox, trap, and sweep structures | Distribution and debt baskets |
| Enforcement path | Receivership, servicing transfer, reserve control, collateral remedies | Covenant breach, amendment, acceleration, intercreditor remedies |
| Cure path | Paydown, reserve funding, waiver, operational repair | Equity cure, amendment, refinancing, basket management |

**Key insight:** CRE documents are more intrusive because the lender is relying on the property and its rents as the repayment source. The document review should focus on control of cash, collateral isolation, trigger consequences, and refinanceability rather than only on the opening DSCR or LTV.

---
