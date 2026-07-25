---
last_updated: "2026-03-22"
---

## LME Covenant Analysis

### What Are Liability Management Exercises?

A Liability Management Exercise (LME) is any transaction by which a borrower restructures its existing debt obligations outside of a traditional consensual refinancing — often to the detriment of some or all existing creditors. LMEs exploit permissive covenant language to achieve outcomes that creditors did not anticipate when they underwrote the deal.

For full LME taxonomy, execution mechanics, and distressed investing implications, see the `events-distressed` skill. This document focuses on **identifying and assessing LME vulnerability from within the credit agreement itself**.

For market-wide documentation erosion trends that have enabled LME proliferation, see `references/credit-agreement-trends-documentation-risk.md` (root reference). For broader agreement review outside the LME lens, use `references/documentation-risk-checklist.md` within this skill.

---

### Covenant Provisions That Enable or Block LMEs

#### Open Market Purchase Provisions (Serta-Style Uptier)

Uptier exchanges allow a subset of lenders to exchange into new super-priority debt, subordinating non-participating lenders. The enabling language is typically found in the "open market purchase" or "Dutch auction" provision of the credit agreement.

- **Enabling language**: "The Borrower may purchase or prepay Term Loans on a non-pro-rata basis through open market purchases, Dutch auctions, or privately negotiated transactions"
- **Why it matters**: If the agreement permits non-pro-rata repayment without requiring the same terms be offered to all lenders, a narrow coalition (often 50.1%) can exchange into new senior debt while leaving minority lenders subordinated
- **Protective language**: "Any open market purchase, exchange, or similar transaction must be offered to all Lenders on identical terms and on a pro-rata basis"

#### Unrestricted Subsidiary Designations (J.Crew-Style Dropdown)

Dropdown transactions move valuable assets (IP, real estate, key contracts) from the restricted group to an unrestricted subsidiary, placing them beyond lender reach. The borrower then pledges those assets to secure new debt at the unrestricted sub level.

- **Enabling language**: "The Borrower may designate any Restricted Subsidiary as an Unrestricted Subsidiary, provided that the aggregate fair market value of assets so transferred does not exceed the greater of $X million or Y% of Total Assets"
- **Why it matters**: Thresholds of 10-15% of total assets — common in aggressive documentation — can allow transfer of hundreds of millions in collateral value
- **Protective language**: "Material Intellectual Property, real property, and assets generating more than 5% of consolidated revenue shall not be transferred to any Unrestricted Subsidiary"

#### Non-Pro-Rata Repayment Permissions

Beyond open market purchases, some agreements permit selective repayment or exchange of debt to specific lender groups without offering the same terms to all.

- **Enabling language**: "Prepayments may be applied to any tranche or sub-tranche as determined by the Borrower"
- **Why it matters**: Permits selective paydowns that create de facto subordination among originally pari passu lenders
- **Protective language**: "All voluntary prepayments shall be offered to Lenders on a pro-rata basis across all Term Loan tranches"

#### Sacred Rights and Voting Thresholds

Sacred rights define which amendments require unanimous (or supermajority) consent versus simple majority. Narrow sacred rights lists leave more room for majority coalitions to impose adverse changes on dissenters.

- **Enabling language**: "Required Lenders (>50%) may amend any provision of this Agreement other than those requiring consent of each affected Lender"
- **Why it matters**: If lien subordination, collateral release, or pro-rata sharing modifications are NOT on the sacred rights list, a 50.1% coalition can authorize them
- **Protective language**: Sacred rights should explicitly include: lien subordination, guarantee release, collateral release, pro-rata sharing changes, and any amendment that would permit priming of existing debt

#### Anti-Subordination Protections

Explicit provisions that prevent any transaction resulting in structural or contractual subordination of existing debt without unanimous consent.

- **Enabling language** (weak): Agreement is silent on whether amendments can effect subordination
- **Why it matters**: Silence is the borrower's friend — absent explicit prohibition, courts have generally upheld majority-approved transactions that subordinate dissenters
- **Protective language**: "No amendment, waiver, or modification shall, without the consent of 100% of Lenders, subordinate the Obligations in right of payment or lien priority to any other Indebtedness"

---

### LME Vulnerability Assessment Checklist

When reviewing a credit agreement, check each of the following provisions. A score of 6+ red flags indicates high LME vulnerability.

| # | Provision to Check | Red Flag | Protective Standard |
|---|---|---|---|
| 1 | Open market purchase clause | Permits non-pro-rata purchases without offering to all lenders | Must offer to all lenders on same terms |
| 2 | Sacred rights list | Lien subordination and pro-rata sharing NOT listed | Explicit inclusion of subordination, collateral release, pro-rata changes |
| 3 | Required Lender threshold | Simple majority (>50%) for material amendments | Supermajority (66.67%–75%) for material amendments |
| 4 | Unrestricted subsidiary cap | >10% of total assets or no cap on IP/revenue-generating transfers | Cap at 5%; carve-out for material IP and key assets |
| 5 | Non-pro-rata prepayment | Borrower discretion on prepayment allocation across tranches | Mandatory pro-rata across all term loan tranches |
| 6 | Anti-subordination clause | Absent or limited to maturity/rate/principal only | Explicit prohibition on lien and payment subordination |
| 7 | Collateral release mechanics | Majority lenders can release material collateral | Unanimous consent for release of collateral >5% of total |
| 8 | Exchange offer provisions | No requirement to offer exchanges to all lenders equally | Blocker requiring identical terms offered pro-rata |
| 9 | Guarantee release | Majority can release guarantees from material subsidiaries | Unanimous consent for release of any material guarantor |
| 10 | Defined term manipulation | Broad "Permitted Indebtedness" or "Permitted Liens" definitions without LME-specific carve-outs | Definitions explicitly exclude priming transactions |

---

### LME Type Matrix

| LME Type | Key Enabling Provision | Historical Example | Protective Language to Seek |
|---|---|---|---|
| **Uptier exchange** | Open market purchase + low sacred rights threshold | Serta Simmons (2020): 50.1% lender coalition exchanged into super-priority TL | "Any exchange must be offered pro-rata to all Lenders on identical terms" |
| **Dropdown / asset transfer** | Broad unrestricted subsidiary designation | J.Crew (2017): transferred IP to unrestricted sub, pledged to new lenders | "Material IP and assets >5% of total must remain in Restricted Group" |
| **Double-dip / collateral stripping** | Weak collateral release + loose investment basket | Envision Healthcare (2023): new debt secured by assets stripped from existing collateral pool | "Collateral release requires 100% Lender consent" |
| **Pari-plus / super-priority** | Permitted debt basket + weak lien restrictions | Boardriders (2019): new money at super-priority diluted existing first lien | "No Indebtedness shall have priority over existing Obligations in lien ranking" |
| **Non-pro-rata paydown** | Selective prepayment discretion | TriMark (2020): selective repayment of cooperative lenders at par while others traded at discount | "All prepayments applied pro-rata across all Term Loans" |

---

### Assessing Overall LME Exposure

**Low vulnerability (0-2 red flags):** Post-2023 documentation with explicit anti-Serta and anti-J.Crew provisions. Sacred rights cover subordination. Pro-rata sharing enforced.

**Moderate vulnerability (3-5 red flags):** Typical 2018-2022 vintage documentation. Some protective provisions but gaps remain. Monitor for amendment activity.

**High vulnerability (6+ red flags):** Pre-2020 or aggressively documented credits. Multiple LME vectors available. Discount trading price should reflect documentation risk. Consider hedging or exiting if credit deteriorates.

---
