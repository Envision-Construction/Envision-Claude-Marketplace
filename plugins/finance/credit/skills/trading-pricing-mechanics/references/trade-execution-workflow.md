---
last_updated: "2026-03-22"
---

## Trade Execution Workflow

Use this reference to think through execution from authorization to post-settlement control. Treat the workflow as principle-based; current settlement windows, assignment fees, and deal-parameter conventions should be checked in root `references/typical-deal-parameters.md`.

## Par Trading Context

Par trading refers to performing-loan trading under the standard performing-loan documentation set. The key distinction is not the exact price level; it is that the loan is trading as a current-performing credit rather than as a defaulted or claims-style asset.

Current standard settlement targets can change over time. Use root `references/typical-deal-parameters.md` for the live convention; the timeless point is that economic transfer typically precedes cash settlement, so accrued-interest and delayed-compensation logic matters.

Par confirmations typically incorporate a standard package covering settlement procedures, assignment vs. participation election, representations, fee allocation, timing adjustments, and dispute mechanics. The exact legal text matters less than understanding that the standard terms shape the economic outcome even when the ticket looks simple.

## 1. Pre-Trade Controls

Before execution, confirm:

1. The position is authorized under the relevant IC decision or PM authority.
2. The trade fits the applicable fund documents and vehicle constraints. For BDC-held private credit positions, use `skills/private-credit-middle-market/references/bdc-regulatory.md`; otherwise use the governing indenture, prospectus, IMA, or mandate documents.
3. The intended size matches portfolio limits and any name-, sector-, or rating-based concentration caps.
4. The counterparty is approved and pre-settlement exposure is acceptable.
5. No restricted-list, MNPI, or conflict issue blocks the trade.

## 2. Choose the Correct Transfer Route

For loans, the transfer route changes the economics and legal posture:

- **Assignment** transfers lender-of-record status, direct voting rights, and direct claims under the credit agreement.
- **Participation** transfers economics but usually leaves privity, voting, and enforcement rights with the seller.
- **Distressed or post-default situations** may require different documentation, claim treatment, or true-up mechanics.

Use the assignment and participation references in this skill to determine the route. Do not assume the faster route is economically equivalent.

## 3. Capture the Trade Ticket Cleanly

The trade record should identify at minimum:

- Borrower or issuer.
- Exact facility or bond.
- Notional or par amount.
- Price and whether it is clean, dirty, or flat.
- Trade date and expected settlement route.
- Legal entities for buyer and seller.
- Security identifiers and booking instructions.
- Any fee, accrued interest, delayed-compensation, or true-up expectations.

If any of those items is ambiguous, the economics are not yet locked.

## 4. Reconcile Economic Transfer with Settlement

The main execution question is not just "when does cash move?" but "when do economics move?"

- For performing trades, confirm how accrued interest or delayed compensation is handled.
- For distressed trades, confirm whether the trade is flat and whether purchase-price reduction or true-up provisions apply.
- For bonds, reconcile clean price to invoice amount using the relevant day-count convention.
- For loans, confirm whether transfer restrictions, eligible-assignee rules, minimum holds, or consent requirements can extend settlement.

Use `references/delayed-compensation-economic-adjustment-for-timing.md` for the detailed timing adjustment logic.

## 5. Execute with Market Impact in Mind

Large or illiquid positions should be built with an execution plan, not just a target size:

- Use multiple dealers when price discovery matters.
- Pace accumulation to avoid signaling demand unnecessarily.
- Distinguish forced flow, natural supply, and event-driven opportunities.
- Reassess whether the secondary market is still the best route versus primary participation.

Execution is part of underwriting. A cheap level that only exists for trivial size may not be actionable at portfolio scale.

## 6. Post-Settlement Verification

After settlement:

- Match the final confirmation against the trade ticket.
- Confirm lender-of-record or custody records were updated correctly.
- Reconcile settlement cash, accrued interest, fees, and any timing adjustments.
- Book the position with the correct structural, rating, coupon, maturity, and identifier fields.
- Hand off monitoring requirements to `surveillance-monitoring` when the trade creates or changes an owned position.

## Trade Documentation Checklist

Use this checklist before calling a trade economically and operationally complete. Confirm current market timing and fee conventions in root `references/typical-deal-parameters.md`; this checklist focuses on the control points that should remain true even when market conventions evolve.

### Trade Terms and Economics

- [ ] Borrower or issuer and exact instrument are identified correctly.
- [ ] Notional or par amount, price convention, and settlement route are unambiguous.
- [ ] Trade date, expected settlement timing, and economic transfer logic are agreed.
- [ ] Accrued interest, delayed compensation, flat trading, or true-up mechanics are documented if relevant.
- [ ] Any fees, who pays them, and whether they affect the invoice amount are captured.

### Transfer Mechanics

- [ ] Assignment vs. participation election is explicit.
- [ ] Transfer restrictions, eligible-assignee rules, and minimum-hold requirements are checked.
- [ ] Borrower, agent, or lender consent requirements are identified.
- [ ] Any unfunded commitment transfer is documented separately from funded exposure.

### Compliance and Onboarding

- [ ] MNPI and restricted-list status are cleared under internal policy.
- [ ] Counterparty onboarding, KYC/AML, tax, and settlement instructions are complete.
- [ ] Any vehicle-specific compliance requirement has been satisfied.

### Closing Package

- [ ] Trade confirmation matches the agreed economics.
- [ ] Assignment or participation documents are fully executed where required.
- [ ] Ancillary forms, notices, and representations are complete.
- [ ] The settlement path is operationally confirmed with the relevant parties.

### Post-Settlement Checks

- [ ] Cash received or paid matches the expected settlement amount.
- [ ] Register, custody, or administrator records reflect the correct owner.
- [ ] Any post-close adjustment items are tracked to resolution.
- [ ] Position data is booked correctly for risk, accounting, and surveillance.
