---
name: Bankruptcy Legal Framework
description: |
  U.S. bankruptcy fundamentals: Chapter 7 vs. Chapter 11 mechanics, claim definitions and allowed amounts,
  class formation, voting, blocking positions, cramdown, and subordination rules.
last_updated: "2026-03-22"
---

## Bankruptcy Basics (U.S. Focus)

### Chapter 7 vs. Chapter 11

**Chapter 7: Liquidation**
- Company ceases operations
- Trustee appointed to sell assets
- Proceeds distributed by priority (secured lenders → trade creditors → shareholders)
- Quick process (6-12 months typically)
- Creditors rarely recover pennies on dollar
- Equity holders recover: essentially zero

**Chapter 11: Reorganization**
- Company continues operating (often under court protection)
- Management or trustee runs the business
- Debt is restructured: principal haircuts, maturity extensions, interest rate reductions
- Creditors may receive equity in reorganized company (ownership stake)
- Bankruptcy plan voted on by creditors
- Judge confirms plan if legally valid
- Process slower: 1-3 years or more
- Allows for business recovery and creditors to recover substantially

### The Bankruptcy Filing Trigger

**When must a company file?**
- When it cannot meet financial obligations as they come due
- Most bankruptcies triggered by missed debt payments (bond interest, bank loan payment)
- Missed trade payables alone rarely trigger bankruptcy (though they signal distress)
- Technical defaults on covenants don't force bankruptcy: creditors choose to accelerate

**Cure Period & Negotiations**
- Typical bond indenture: 30-day grace period after missed interest payment
- During grace period, company can cure (pay accrued interest + any fees) without triggering acceleration
- This grace period is a negotiation window: advisors often contact bondholders to discuss restructuring options
- If not cured by day 30 → default accelerated → company has 10 days to file bankruptcy voluntarily or face involuntary petition

**Automatic Stay**
- Filing bankruptcy triggers automatic stay: all collection actions cease immediately
- Creditors cannot:
  - Foreclose on collateral
  - Accelerate debt (already accelerated, but foreclosure blocked)
  - Garnish wages
  - Pursue litigation
  - Cut off utilities (with exceptions for priority of payment order)
- This stay gives company breathing room to negotiate restructuring plan

---

## Claims in Bankruptcy

### Definition: What Is a "Claim"?

**Claim = Principal Owed + Accrued Unpaid Interest (as of filing date)**

The claim is the creditor's legal entitlement in the bankruptcy estate. It's not what they'll recover — it's what they can vote on and receive distribution from.

### Accrued Interest & OID/Zero-Coupon Treatment

**Regular Coupon Bonds**:
- $100M face, 8% coupon, semi-annual payment
- Claim includes all accrued but unpaid interest
- If 3 months of interest accrued (45 days into 6-month period) → claim = $100M + $4M accrued interest = $104M

**Zero-Coupon Bonds (Critical Example)**:
- Issued at discount: $100M face, issued at 61% of face value = $61M cash proceeds
- At filing, 2 years later, accreted to 83.3% = $83.3M
- **Claim in bankruptcy = $83.3M (not $100M face)**
- Why? Because the $83.3M represents the full principal + accreted interest up to filing date
- Comparison: If this were an annual coupon bond at 8%, claim would be approximately the same due to accreted OID

**OID (Original Issue Discount) Bonds**:
- $500M face bond issued at 97% of face = $485M proceeds
- OID = $15M over bond life (spread over 5 years = $3M per year)
- At filing in year 3 → claim based on accreted value, not $500M face
- Accreted 3 years → claim = ~$500M (OID has been built in)
- At filing in year 1 → claim = ~$491M (only 1 year of OID accreted)

**PIK Bonds (Paid-in-Kind)**:
- Principal grows each period as interest paid in additional bonds
- Example: $100M face, 12% PIK
- Year 1: $100M → $112M (12% accreted in additional bonds)
- Year 2: $112M → $125.4M (12% on $112M)
- Filing in year 2 → claim = $125.4M (this is the principal size at filing, including all PIK accreted)

### Post-Petition Interest (Generally NOT Paid)

**Key Rule**:
- Interest that accrues AFTER bankruptcy filing is NOT paid on unsecured claims (with one exception)
- Only exception: **oversecured claims**

**Oversecured Claim**: Collateral value > Claim amount + applicable interest
- Example: $50M secured loan, collateral worth $80M, $15M of interest accrues post-petition
- This claim is oversecured: $80M collateral covers $50M + $15M interest with $15M cushion
- Lender receives full claim + post-petition interest

**Undersecured Claims**: Collateral value < Claim amount
- Example: $50M secured loan, collateral worth $40M
- Secured portion = $40M (secured claim)
- Deficiency = $10M (unsecured claim)
- Post-petition interest: NOT paid on either portion
- Total recovery depends on estate value distribution

---

## Classes of Claims & Voting

### Priority Structure

**Secured claims**: Backed by specific collateral (mortgages, UCC liens)
**Senior unsecured claims**: No collateral, first in line of unsecured creditors (bank revolvers, senior notes)
**Subordinated claims**: Junior to senior unsecured (subordinated notes, mezzanine debt)
**Equity**: Ownership interests

Each class treated equally within the class (pro rata, dollar-for-dollar), but classes get priority over each other by legal right.

### Impaired vs. Unimpaired Classes

**Impaired class**: Not receiving 100% of claim value under the plan
- Example: Senior notes owed $300M, receiving $250M (new debt + equity) = impaired
- Gets to vote: yes or no on the plan
- Voting threshold: **two-thirds of dollar amount AND 50% of number of holders**
- If either threshold missed → class rejects plan

**Unimpaired class**: Receiving full claim value under the plan
- Example: Bank debt owed $100M, receiving $100M in new senior debt = unimpaired
- Deemed to accept the plan (no vote required)
- Cannot block the plan

**Class receiving nothing**: Impaired but has zero recovery
- Deemed to reject (no vote required)
- Cannot block: already getting nothing, can't make it worse
- Exception: if plan would give something to junior class → rejecting class can argue unfairness

### Blocking Position & Cram-Down

**Blocking Threshold**: 33.4% of dollar amount in an impaired class
- Hold 33.4%+ of a claim class → can block the plan
- Forces compromise or cram-down
- Example: Class has $300M of claims, you hold $100.2M → blocking position

**Cram-down**: Court forces plan on dissenting impaired class
- Requires: (1) plan satisfies absolute priority rule, (2) is fair and equitable, (3) doesn't discriminate unfairly
- Rarely used: judges strongly prefer consensus plans
- Threat of cram-down is negotiation leverage: "Accept this better offer or I'll cram it down"

### Second Lien Placement: Same vs. Separate Class

**Same Security Agreement**:
- First lien and second lien have same collateral and security agreement
- Court treats them as same class in bankruptcy
- First lien gets paid in full, second lien gets remainder
- First lien controls the class (dominates voting)

**Separate Security Agreements**:
- First lien: specific assets (A, B, C)
- Second lien: different assets (D, E, F) or blanket on all assets but subordinated
- Creates separate classes with separate voting
- Second lien has more say in restructuring if its collateral is valuable
- Post-petition interest analysis: first lien oversecured? Second lien may be too
- Example: $100M first lien with $150M collateral (oversecured), $50M second lien with $30M incremental collateral (undersecured)

---

## Subordination in Bankruptcy

### How Subordination Works

**Subordination clause**: "This debt is subordinated in right of payment to Senior Debt"
- Holder agrees that in bankruptcy, Senior Debt gets paid before Subordinated Debt
- In bankruptcy waterfall, Senior Debt classes are paid in full before any funds go to Subordinated classes
- Pre-bankruptcy: both lenders may have equal claim on assets, but subordination agreement controls bankruptcy distribution

### Critical Detail: How "Senior Debt" Is Defined

**Tightly Defined Subordination**:
- "Subordinated to the existing senior bank debt and specifically identified senior note obligations"
- Only those specific obligations rank senior
- Other creditors (trade claims, other bond issues) rank pari passu (equal) with subordinated bonds
- Example: If subordination is only to bank loans, trade claims are NOT senior
  - Waterfall: Bank loans paid first, then trade claims and sub bonds equally

**Loosely Defined Subordination**:
- "Subordinated to all Senior Debt" (defined broadly in credit agreement)
- Includes all senior bank debt, senior notes, any future senior obligations
- Subordinated bonds are junior to everything that could be called "senior"
- Example: Even trade claims might rank pari passu or senior if they have payment priority
  - Waterfall: All senior debt paid first, then subordinated bonds absorb all remaining shortfall

### BlowUp Co Example

**Enterprise Value**: $250M
**Capital Structure**:
- Senior bank notes: $100M
- Trade payables: $50M
- Subordinated notes: $250M

**Without Subordination (Pro Rata Distribution)**:
- Total claims = $400M
- Recovery rate = $250M / $400M = 62.5%
- Senior notes: 62.5% x $100M = $62.5M (recovery of 62.5%)
- Trade claims: 62.5% x $50M = $31.25M
- Sub notes: 62.5% x $250M = $156.25M

**With Subordination (if trade claims rank pari passu with bank debt)**:
- Pari passu claims (senior): $100M + $50M = $150M
- Subordinated: $250M
- Pro rata on senior: $250M x ($150M / $250M) = $150M available
- Senior creditors recover 100%: bank notes $100M, trade $50M
- Subordinated gets: $250M - $150M = $100M
- Sub notes: $100M / $250M = 40% recovery

**Key Insight**: Subordinated debt gives up its pro rata share to make senior debt whole. The waterfall explicitly prioritizes by class.

---
