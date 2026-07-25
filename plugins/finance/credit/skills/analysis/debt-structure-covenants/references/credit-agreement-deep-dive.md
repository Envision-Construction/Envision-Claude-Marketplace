---
last_updated: "2026-03-21"
---

## Credit Agreement Deep Dive

### Anatomy of a Credit Agreement
The credit agreement is the governing document for syndicated loans. Unlike bond indentures (which are relatively standardized), credit agreements are heavily negotiated and can run 200-400+ pages.

**Core Sections:**
1. **Definitions**: 50-100+ pages of defined terms. CRITICAL to understanding — every key term (Consolidated EBITDA, Permitted Debt, Restricted Payments) has a bespoke definition that can dramatically affect economics
2. **Facility Terms**: Commitment amounts, interest rates, maturity dates, amortization schedules, prepayment mechanics
3. **Conditions Precedent**: Requirements that must be satisfied before initial and subsequent borrowings (legal opinions, no default, accuracy of representations)
4. **Representations & Warranties**: Borrower's statements about its legal status, financial condition, compliance with laws, no litigation. If materially incorrect, can trigger Event of Default
5. **Affirmative Covenants**: Things borrower MUST do — deliver financial statements, maintain insurance, permit inspections, comply with laws, pay taxes
6. **Negative Covenants**: Restrictions on what borrower CANNOT do — incur debt, grant liens, make investments, pay dividends, sell assets, merge, change business
7. **Financial Covenants**: Quantitative tests (leverage, coverage, capex limits) — may be maintenance (tested quarterly) or incurrence (tested only when specific action taken)
8. **Events of Default**: Triggers that allow lenders to accelerate debt — payment default, covenant breach, cross-default, bankruptcy, judgment, change of control, ERISA events
9. **Remedies**: Lender rights upon Event of Default — acceleration, enforcement of security interests, application of proceeds

### Material Adverse Change (MAC) Clause
- **Definition**: Condition precedent allowing lenders to refuse funding if borrower has experienced a "Material Adverse Change" or "Material Adverse Effect" since a specified date
- **Scope**: Covers changes in business, assets, financial condition, or results of operations
- **Carve-outs**: Typically excludes: general economic conditions, industry-wide changes, changes in accounting standards, changes in law — UNLESS they disproportionately affect the borrower
- **Controversy**: Rarely invoked — banks fear reputational damage of pulling committed financing. But threat of MAC keeps borrowers honest.
- **Acquisition financing**: "SunGard MAC" / "Certain Funds" provisions limit the conditions under which lenders can refuse to fund acquisition financing — essentially remove MAC condition for initial draw

### Pro Rata Sharing Provisions
- **Principle**: All lenders within a tranche share payments pro rata based on their commitment percentages
- **Mechanics**: If any lender receives a disproportionate payment (e.g., through setoff against borrower's deposits), that lender must share excess with other lenders
- **Purpose**: Prevents individual lenders from "jumping the queue" by exercising setoff rights
- **Waterfall**: Payments applied first to fees, then interest, then principal (unless otherwise specified)
- **Exception**: DIP financing in bankruptcy may have different priority; "first out" structures in unitranche

### Covenant-Lite (Cov-Lite) Loans
- **Definition**: Term loans that lack financial maintenance covenants — tested only on incurrence basis (like bond covenants)
- **Evolution**: Pre-2007: most loans had maintenance covenants. 2007 first wave of cov-lite. Post-2020: cov-lite is approximately 85-90% of the institutional (TLB) market as of early 2025
- **What's missing**: No quarterly leverage or coverage ratio tests. Borrower only tested when taking affirmative action (incurring debt, making acquisitions, paying dividends)
- **What remains**: Negative covenants still present (debt incurrence limits, restricted payments, lien restrictions) — but tested on incurrence, not maintenance
- **Revolver carve-out**: Even in cov-lite deals, revolvers often retain a springing financial covenant (e.g., leverage test that "springs" only if revolver is drawn past 35% threshold)
- **Investor concern**: Delayed default recognition — borrower can deteriorate significantly before triggering any covenant. By the time default occurs, recovery value may be substantially impaired
- **Borrower benefit**: Operational flexibility — management can focus on running business without worrying about quarterly covenant compliance during temporary downturns

### Standard Credit Agreement Provisions
- **Industry practice**: Standard provisions establish market expectations — significant deviations require explanation
- **Key provisions**: EBITDA definition, excess cash flow definition, available amount basket, incremental facility provisions, pro rata sharing, assignment and participation mechanics
- **"Borrower-friendly" vs "lender-friendly"**: Each provision exists on a spectrum. Current market (strong demand, low defaults) tends toward borrower-friendly; stressed markets shift toward lender-friendly

### Events of Default — Detailed Cascade
1. **Payment default**: Failure to pay principal when due (usually immediate default) or interest within grace period (typically 3-5 business days)
2. **Covenant default**: Breach of financial covenant (usually 30-day cure period for maintenance covenants) or negative covenant (often no cure period)
3. **Representation default**: Material misrepresentation discovered — typically no cure
4. **Cross-default**: Default on other debt exceeding specified threshold (e.g., $25M)
5. **Bankruptcy/insolvency**: Filing for bankruptcy, appointment of receiver — immediate Event of Default
6. **Judgment default**: Unstayed judgment exceeding threshold amount
7. **ERISA event**: Certain pension-related liabilities exceeding threshold
8. **Change of control**: Defined change in ownership triggers put right or acceleration
9. **Invalidity of guarantees/security**: If any guarantee or security interest is found invalid

### Equity Cure Rights
- **Definition**: Sponsor can inject equity into borrower to "cure" a financial covenant breach
- **Mechanics**: Equity contribution treated as EBITDA addback (or debt reduction) for purposes of the tested ratio
- **Limitations**: Typically limited to 2-3 cures in any 4-quarter period, and 5-7 cures over life of facility
- **No "over-cure"**: Cure amount limited to the exact shortfall needed to achieve compliance (prevents gaming)
- **Timing**: Must be made within specified period after covenant test date (typically 10-15 business days after delivery of financials)
- **Significance**: Gives PE sponsors a "put option" to avoid technical default during temporary operational dips

---
