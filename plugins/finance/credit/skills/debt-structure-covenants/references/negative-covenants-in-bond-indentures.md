---
last_updated: "2026-03-21"
---

## Negative Covenants in Bond Indentures

Negative covenants restrict what the company can do. They are tested only when the company takes an action (e.g., issuing debt, paying dividends). The company is not in technical default for *failing* a negative covenant—it's in default for *violating* it by taking a prohibited action.

### 1. Debt Incurrence Covenant

**Purpose**: Limit additional debt issuance to preserve leverage ratios.

**Structure**:
- Ratio test must be satisfied *pro forma* after the new debt is issued
- If it's not satisfied, the debt cannot be issued without an amendment/waiver

**Leverage Ratio Test**:
- Formula: Total Debt / EBITDA ≤ X.XXx
- Example: $500M EBITDA, 4x leverage limit, $2B existing debt
  - Current: $2,000M / $500M = 4.0x (at limit)
  - Can issue $500M more to reach 5x before hitting the 5x limit? No—the limit is 4x
  - Can issue up to $500M only if pro forma leverage stays at 4.0x: ($2,000M + $500M) / $500M = 5.0x—*violated*
  - Actually can issue $0 while maintaining exactly the 4.0x ratio

- Example 2: If the limit is 5.0x instead:
  - Can issue debt so long as pro forma leverage ≤ 5.0x
  - ($2,000M + X) / $500M ≤ 5.0x → X ≤ $500M → can issue $500M

**Fixed Charge Coverage Test**:
- Formula: EBITDA / Fixed Charges ≥ X.XXx (e.g., 2.0x)
- Fixed Charges = interest expense + principal repayments
- *Highly sensitive to interest rates*

Example:
- $500M EBITDA, fixed charge coverage limit 2.0x, $100M existing annual fixed charges
- Current: $500M / $100M = 5.0x (comfortable)
- Want to issue $500M new debt at *10% rate*:
  - New fixed charges: $100M + (5% × $500M) = $125M
  - Pro forma: $500M / $125M = 4.0x ✓ (passes 2.0x minimum)

But at *13% rate*:
  - New fixed charges: $100M + (13% × $500M) = $165M
  - Pro forma: $500M / $165M = 3.0x ✓ (still passes)

But at *20% rate* (rising rate environment):
  - New fixed charges: $100M + (20% × $500M) = $200M
  - Pro forma: $500M / $200M = 2.5x ✓ (still passes, but much tighter)

At *25% rate*:
  - New fixed charges: $100M + (25% × $500M) = $225M
  - Pro forma: $500M / $225M = 2.2x ✓ (passes barely)

At *30% rate*:
  - New fixed charges: $100M + (30% × $500M) = $250M
  - Pro forma: $500M / $250M = 2.0x ✓ (at exactly the minimum—no room for error)

At *31% rate*:
  - New fixed charges: $100M + (31% × $500M) = $255M
  - Pro forma: $500M / $255M = 1.96x ✗ (below 2.0x—cannot issue)

**Key insight**: Fixed charge coverage tests constrain debt issuance in high-rate environments.

**Common Carve-Outs** (exceptions that don't need to satisfy the ratio test):
- Existing bank facility and revolving credit commitments (be careful: is it reduced by prepayments or refinancings?)
- Liens/mortgages on acquired property (asset-level debt)
- Tax liens below a specified amount
- Debt incurred to finance acquisitions (purchase price financing)
- Equity-linked debt (e.g., convertible bonds with a 0.5x debt cap per 1.0x equity raised)
- Refinancing debt to replace maturing debt (common refinancing carve-out)

---

### 2. Restricted Payments Covenant

**Purpose**: Control cash outflows that weaken the balance sheet (dividends, buybacks, optional repayments of subordinated debt).

**Structure**: Two-part test—both must be satisfied:
1. **Ratio test**: Same as debt incurrence (leverage or coverage)
2. **Basket test**: Dollar amount accumulated and available to spend

**How the Basket Works**:
- Starts from an effective date; accumulates each quarter
- Typically builds at 50% of net income (or alternate basis: 50% of EBITDA over 1.4x interest coverage)
- Restricted payments made in a quarter reduce the balance
- Example:
  - Effective date: Jan 1, 2024; Q1 net income $100M → basket = $50M
  - Q2 net income $80M → basket = $50M + $40M = $90M
  - Company pays $40M dividend in Q2 → basket = $90M - $40M = $50M
  - Q3 net income -$20M → basket = $50M - $10M = $40M (negative NI deducted or just excluded?)

**Critical detail**: Does negative net income get deducted from the basket, or is it ignored?
- Some indentures: negative NI is deducted (bleeds the basket in downturns)
- Others: negative NI is excluded (basket only grows in profitable quarters)
- Read the exact language carefully

**Common Carve-Outs**:
- Employee stock repurchases (capped, e.g., $5–10M annually for ESPP)
- One-time payments (annual amounts, e.g., $10M)
- Equity-funded restricted payments (e.g., if company raises $100M equity, can pay $100M in dividends)
- Refinancing of junior debt (paying off old preferred stock or subordinated notes)

---

### 3. Change of Control Covenant

**Purpose**: Protect against a leveraged buyout or hostile takeover that harms existing creditors.

**Trigger**: A change of control event occurs (typically defined as):
- A single person/entity acquires >35% or >50% of voting power, OR
- Majority of board is replaced within a 12-month window

**Remedy**: Company must make a "101 put offer" within 90 days of closing:
- Offer to repurchase bonds at 101% of principal (or specified price)
- Bondholders can tender their bonds for cash at this price
- If enough tender, the bonds are retired

**Permitted Holders Exception**:
- Takeover by "permitted holders" (usually defined term) does NOT trigger the covenant
- Common examples: controlling family members, existing PE sponsor re-upping, qualified long-term holders
- Read the definition—it's a major loophole

**When It Doesn't Matter**:
- If bonds trade below 101 (e.g., at 95), rational bondholders won't tender; they'll hold the bonds
- If leverage ratio post-acquisition is lower or ratings unchanged, some indentures allow waiver of the put offer

**Acquirer Strategy**:
- If bonds trade above 101, acquirer wants to avoid the put offer cost
- Typical solution: seek a waiver from bondholders (10% or 25% holder consent)
- Cost of waiver: pay additional fees, increase coupon, tighten covenants on acquirer's new debt

---

### 4. Asset Sale Covenant

**Purpose**: Prevent the company from liquidating value and returning cash to equity without bondholders sharing.

**Key Definitions**:
- What counts as a "covered asset sale"? Usually: asset > 10% of total assets or > $X threshold
- Must proceeds be cash? Usually 85% must be cash; 15% can be notes/assumption of liabilities

**Use of Proceeds**:
- (1) Repurchase bank debt at par (lenders get priority)
- (2) Offer to repurchase outstanding bonds at par
- (3) Reinvest in permitted assets within 180 days (e.g., acquire replacement equipment)
- If not reinvested or used as above, proceeds are held and reduce debt

**Carve-Outs** (sales that don't trigger the covenant):
- Sales of ordinary course inventory
- Real estate and nonstrategic subsidiaries (often capped)
- Casualty/insurance proceeds
- Disposition of assets acquired in an M&A (if non-core to the acquisition)

---

### 5. Reporting Requirements

**Purpose**: Ensure bondholders have information to monitor the company.

**Key Requirements**:
- Delivery of annual/quarterly financial statements (audited for annual, reviewed for quarterly)
- Within 90 days of year-end for annual; within 45 days for quarterly
- Investor calls (quarterly, semiannual, or annual)
- SEC filings if public; restricted distribution (IntraLinks) if private

**Why It Matters**:
- Private companies with poor reporting = wide bid-ask spreads, illiquid bonds
- Public companies with regular SEC filings + calls = tighter spreads, more trading
- If a company loses SEC reporting status (goes private), bonds are harder to sell

---
