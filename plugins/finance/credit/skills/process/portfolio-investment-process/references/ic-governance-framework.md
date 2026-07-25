---
last_updated: "2026-03-22"
---

# Investment Committee Governance Framework

**Last Updated:** March 2026
**Update Cadence:** Annual
**Next Review:** March 2027

This file codifies the governance processes surrounding Investment Committee operations, from pipeline origination through post-close surveillance handoff. It serves as the single source of truth for IC scheduling, decision taxonomy, escalation protocols, and approval-to-close timelines. For numeric risk parameters referenced in IC decisions, see `references/portfolio-risk-parameters.md`. For escalation thresholds that trigger ad-hoc IC sessions, see `references/escalation-trigger-thresholds.md`.

---

## 1. IC Calendar & Pipeline Management

### 1.1 Session Cadence

The IC operates on a structured calendar with two session types:

| Session Type | Frequency | Trigger | Notice Period |
|---|---|---|---|
| Standing IC | Weekly (same day/time) | Scheduled calendar | Agenda circulated T-2 business days |
| Ad-Hoc IC | As needed | Tier 3+ escalation, time-sensitive opportunity, or CIO request | Minimum 4 hours notice; materials may follow |

Standing IC sessions are held weekly regardless of pipeline volume. When no new credits are scheduled, the session is shortened to cover portfolio updates, surveillance escalations, and follow-up items only. Cancellation of a standing IC requires CIO approval and must not occur more than twice per quarter.

### 1.2 Pipeline Tracking

All credits under consideration are tracked in a centralized pipeline with the following fields:

```yaml
pipeline_record:
  credit_name: ""                    # Issuer or borrower name
  asset_class: ""                    # Corporate loan, bond, private credit, CRE, structured
  analyst: ""                        # Lead analyst
  co_analyst: ""                     # Supporting analyst (if applicable)
  origination_date: ""               # Date credit entered pipeline
  target_ic_date: ""                 # Planned IC presentation date
  status: ""                         # See status definitions below
  priority: ""                       # High / Medium / Low
  estimated_size_mm: ""              # Target position size ($MM)
  time_sensitivity: ""               # Standard / Elevated / Urgent
  memo_draft_status: ""              # Not started / In progress / Under review / Final
  ic_conditions: []                  # Conditions imposed at IC (if applicable)
  conditions_verified: false         # Boolean — all conditions confirmed
```

### 1.3 Pipeline Status Definitions

| Status | Definition | Owner |
|---|---|---|
| In Pipeline | Credit identified, preliminary analysis underway | Analyst |
| Scheduled | IC date confirmed, memo in final preparation | Analyst |
| Presented | Memo presented to IC, decision pending or rendered | IC Chair |
| Approved | IC approval granted (unconditional or conditional) | PM / Analyst |
| Conditional Pass | Approved subject to specified conditions | Analyst (condition verification) |
| Declined | IC rejected the investment | Analyst (may resubmit) |
| Tabled | IC requires additional information before deciding | Analyst |
| Withdrawn | Analyst removed credit before IC decision | Analyst |

### 1.4 Pipeline Capacity Management

To ensure adequate discussion quality, each standing IC session is limited to a maximum of 3-4 new credit presentations. When pipeline volume exceeds session capacity, the IC Chair prioritizes based on time sensitivity, portfolio need, and analyst readiness. Credits that are deferred receive priority scheduling at the next available session.

### 1.5 Agenda Structure

A standard standing IC session follows this structure:

| Segment | Duration | Content |
|---|---|---|
| New Credit Presentations | 30-45 min each | Full memo walkthrough, Q&A, challenge, decision |
| Follow-Up Reviews | 15-20 min each | Condition verification, resubmissions, material updates |
| Portfolio Update | 15 min | NAV, performance attribution, risk metric summary |
| Surveillance Escalations | As needed | Tier 2+ items requiring IC awareness or action |
| Administrative Items | 5-10 min | Threshold review status, process items, upcoming calendar |

Materials for new credit presentations must be distributed to all IC members no later than 2 business days before the session. Late submissions may be deferred to the following session at the IC Chair's discretion.

---

## 2. IC Decision Types

Every credit presented to the IC receives one of the following formal outcomes. The IC Chair is responsible for documenting the decision, any conditions, and the vote record.

| Decision | Definition | Next Steps |
|---|---|---|
| Approve | Full approval at the recommended size and terms | Proceed to execution within the approval-to-close timeline |
| Conditional Pass | Approval subject to specified conditions | Analyst verifies each condition; execution proceeds only after all conditions are met or escalated |
| Decline | Investment rejected on its merits | Analyst may resubmit only with material new information; minimum 30-day cooling period unless market circumstances change materially |
| Table | Insufficient information to render a decision | Analyst addresses identified gaps and re-presents at next available IC session; no cooling period |
| Withdraw | Analyst withdraws credit before IC decision | No formal IC record; credit may re-enter the pipeline at any time |

**Conditional Pass governance:** Each condition must have a clearly defined verification method, a responsible party, and a deadline. Conditions that remain unverified at trade date trigger a Tier 3 escalation (see `references/escalation-trigger-thresholds.md`). The PM may not override unverified conditions without CIO approval.

**Resubmission protocol:** A declined credit may be resubmitted a maximum of 2 times. Each resubmission must include a cover memo identifying what has materially changed since the prior presentation. If the IC declines a credit after 2 resubmissions, the analyst may escalate to the CIO (see Section 4).

---

## 3. Periodic Threshold Review

The IC conducts an annual review of all governance thresholds and risk parameters to ensure calibration remains appropriate for prevailing market conditions and fund mandates. The review covers three reference files:

- `references/escalation-trigger-thresholds.md` — Surveillance escalation triggers (Tier 1-4)
- `references/portfolio-risk-parameters.md` — Concentration limits, position sizing, risk targets
- `skills/private-credit-middle-market/references/bdc-regulatory.md` — BDC-specific compliance requirements for private credit use cases

### 3.1 Review Checklist

The threshold review must address each of the following questions with documented findings:

**Escalation Calibration**
- Are current thresholds producing an appropriate volume of escalations? Benchmark: 5-15% of positions should trigger Tier 1+ activity in a normal credit environment; fewer than 5% suggests thresholds are too loose, more than 25% suggests thresholds are too tight.
- Are escalations identifying genuine credit deterioration, or are they generating excessive false positives from market noise?
- Were any material credit events in the past 12 months missed by the current threshold framework?

**Market Condition Alignment**
- Has the credit spread regime shifted enough to warrant threshold recalibration? A sustained move of more than 100 bps in the broad market index warrants review of spread-based triggers.
- Has the default cycle phase changed? Early-cycle, mid-cycle, and late-cycle environments may require different sensitivity levels.
- Have interest rate or liquidity conditions changed materially since the last calibration?

**Fund Vehicle Compliance**
- Are fund vehicle constraints still aligned with LP expectations as documented in the most recent annual meeting, side letters, and investment guidelines?
- Have regulatory requirements changed? This includes BDC asset coverage ratios, CLO reinvestment criteria, risk retention rules, and SEC reporting obligations.
- Do any new fund vehicles or mandates require additional constraint parameters?

### 3.2 Threshold Change Governance

Any proposed change to escalation thresholds, risk parameters, or fund vehicle constraints requires:

1. Written proposal documenting the current threshold, proposed threshold, and rationale for change
2. Back-testing analysis of how the proposed threshold would have performed over the trailing 12 months
3. Impact assessment quantifying how many current positions would change escalation classification
4. CIO sign-off before implementation
5. Distribution of updated reference files to all IC members and analysts within 5 business days of approval

Threshold changes take effect at the start of the next calendar month following approval, unless an emergency override is warranted by market conditions.

---

## 4. CIO Escalation Workflow

The CIO escalation process exists as a safety valve for situations where an analyst believes an IC decision is incorrect after exhausting the standard resubmission process. It is designed to be used infrequently and with appropriate gravity.

### 4.1 Escalation Trigger

An analyst may request CIO review when: the IC has declined the same credit after 2 resubmissions, and the analyst maintains that the investment merits approval based on analytical grounds.

### 4.2 CIO Review Package

The CIO receives the following materials for review:

- Original IC memo (first submission)
- IC feedback memoranda from both rounds, including specific objections raised
- Analyst's resubmission cover memos documenting responses to IC concerns
- Dissent records (if any IC members supported approval)
- Updated market data and any new information since the last presentation

### 4.3 CIO Decision Options

| Decision | Definition | Documentation Required |
|---|---|---|
| Override IC — Approve | CIO approves the investment over IC objection | Written rationale, specific risk acknowledgment, any additional conditions |
| Side with IC — Decline | CIO upholds the IC's decline decision | Brief confirmation memo; no further resubmission permitted |
| Mandate Third Submission | CIO identifies specific conditions under which a third IC presentation is warranted | Written conditions that must be satisfied before re-presentation |

### 4.4 Guardrails

- **Timeline:** CIO must render a decision within 5 business days of receiving the escalation package.
- **Frequency limit:** Each analyst is limited to a maximum of 2 CIO escalations per quarter. Exceeding this threshold triggers a review of analyst-IC alignment with the CIO and IC Chair.
- **Transparency:** All CIO escalation decisions are documented and shared with the full IC. Override decisions are flagged in quarterly governance reporting.
- **Post-override monitoring:** Credits approved via CIO override receive enhanced surveillance with a dedicated quarterly review for the first 12 months post-close.

---

## 5. Dissent Tracking Protocol

When an IC decision is not unanimous, the dissenting view must be formally recorded. Dissent tracking serves calibration and decision-quality purposes; it carries no punitive implications for the dissenter.

### 5.1 Dissent Record Requirements

Each dissent record must include:

- Credit name and IC decision date
- Identity of dissenting member(s)
- Summary of the dissenting view (specific risks or opportunities the dissenter believes the majority decision underweights)
- Majority rationale for the prevailing decision
- Measurable indicators that would validate or invalidate the dissenting view within 6-12 months

### 5.2 Review Cadence

Dissent records are reviewed at 6-month intervals by the IC Chair and CIO. The review assesses:

- **Outcome tracking:** Was the dissenter's concern validated by subsequent credit performance? (e.g., dissent against an approval where the credit later deteriorated, or dissent against a decline where the credit performed well)
- **Pattern identification:** Are certain risk categories systematically underweighted or overweighted in IC deliberations?
- **Calibration feedback:** Should dissent outcomes inform adjustments to the IC's analytical framework or threshold parameters?

### 5.3 Governance Principle

Dissent is a protected and valued component of the IC process. Analysts and IC members must be able to register dissenting views without concern for professional consequences. The dissent tracking mechanism exists solely to improve collective decision quality over time.

---

## 6. Approval-to-Close Timeline

Once the IC renders an approval (unconditional or conditional), execution must proceed within defined timeline benchmarks. Delays beyond the benchmarks below require an explanation to the IC Chair and may trigger a re-confirmation vote if the delay exceeds 2x the standard timeline.

### 6.1 Timeline Benchmarks by Asset Class

| Asset Class | Standard Timeline | Key Dependencies |
|---|---|---|
| Corporate Loan (Secondary) | 5-10 business days | Agent bank transfer, T+7 standard settlement |
| Corporate Loan (Primary) | 10-15 business days | Allocation confirmation, credit agreement execution, funding |
| Private Credit (Direct Lending) | 10-20 business days | Documentation negotiation, legal review, funding mechanics |
| CRE Debt | 20-40 business days | Environmental assessment, title insurance, appraisal, structural review |
| Structured Finance (Secondary) | 3-5 business days | T+3 standard settlement, custody transfer |
| CLO Equity / Primary Structured | 15-30 business days | Warehouse period, ramp, closing mechanics |

### 6.2 Pre-Close Condition Verification

Before trade date, the executing analyst must confirm that all IC conditions have been satisfied. The verification checkpoint follows this protocol:

1. **Condition audit:** Each condition from the IC decision record is reviewed against evidence of fulfillment.
2. **Verification sign-off:** The analyst documents how each condition was met and obtains PM acknowledgment.
3. **Unmet condition escalation:** If any condition cannot be verified before trade date, the analyst must escalate to the IC Chair. The IC Chair may (a) grant a time extension with revised deadline, (b) convene an ad-hoc IC to reassess, or (c) revoke the approval pending re-presentation.

### 6.3 Post-Close Procedures

Upon trade execution, the following steps must be completed within 2 business days:

- **Trade confirmation:** Analyst confirms execution details (price, size, settlement date) and circulates to PM and operations.
- **Surveillance handoff:** Analyst maps thesis-kill triggers to the monitoring framework defined in `references/escalation-trigger-thresholds.md` and confirms setup in the surveillance system. Every approved position must have a surveillance handoff completed before T+5.
- **Risk system entry:** Position is entered into the portfolio risk system with correct sector, rating, and facility coding.
- **Documentation filing:** Final credit memo, IC decision record, trade ticket, and any condition verification documents are filed in the credit archive.

### 6.4 Stale Approval Policy

An IC approval expires if trade execution has not occurred within 60 calendar days of the approval date, or 30 calendar days for time-sensitive opportunities flagged as such at IC. Expired approvals require re-presentation to the IC with updated market data, refreshed financial analysis, and confirmation that the original investment thesis remains intact.

---

## 7. Secondary Market Fast-Track Protocol

When a secondary market opportunity requires rapid execution (settlement T+7 or sooner), the standard IC process may be compressed for credits where the fund already has an existing analytical foundation.

### 7.1 Eligibility Criteria

Fast-track IC is available only when ALL of the following are met:

| Requirement | Standard |
|---|---|
| Existing coverage | Credit is already in the portfolio or has been presented to IC within the past 12 months |
| Analyst familiarity | Lead analyst has active coverage and current model |
| Size threshold | Position addition ≤50% of existing position or ≤1.0% of AUM (whichever is smaller) |
| Rating stability | No rating downgrade or outlook change since last IC review |
| Surveillance status | Green or Yellow only (Orange/Red credits require full IC) |

### 7.2 Fast-Track Process

| Step | Timeline | Requirements |
|---|---|---|
| Analyst notification to PM + IC Chair | T+0 (trade identification) | 1-page trade rationale memo: updated spread, relative value, model confirmation |
| PM + IC Chair review | Within 4 hours | Verbal or written approval; if either objects, full IC required |
| Trade execution | Upon approval | Standard execution and settlement process |
| IC ratification | Next standing IC session | Full summary presented for formal record; IC may impose conditions retroactively |

### 7.3 Restrictions

Fast-track approvals are limited to 3 per analyst per quarter. Exceeding this limit requires CIO pre-approval. Fast-track is never available for: new names (no prior IC coverage), distressed credits (price <80), or credits on the watchlist (Orange/Red).

---

## 8. Weekend, Holiday & After-Hours Escalation Protocol

Credit events do not respect business hours. This section defines escalation procedures when material events occur outside the standard IC schedule.

### 8.1 Tier-Based Response

| Escalation Tier | After-Hours Response | Timeline |
|---|---|---|
| Tier 1 (Analyst Watch) | No immediate action required. Analyst documents and reviews at next business day. | Next business day |
| Tier 2 (Team Review) | Analyst notifies PM via secure messaging. PM assesses whether waiting until next business day is acceptable. | Within 12 hours |
| Tier 3 (IC Notification) | Analyst notifies PM and IC Chair immediately. Ad-hoc IC convened within 24 hours (video conference acceptable). | Within 24 hours |
| Tier 4 (Emergency) | Analyst notifies PM, IC Chair, and CIO immediately. Emergency IC within 4 hours. Hedging or position reduction may proceed pre-IC with PM approval and retroactive IC ratification. | Within 4 hours |

### 8.2 Pre-IC Protective Actions

In Tier 4 emergencies occurring outside business hours, the PM may authorize the following protective actions before IC convenes:

- **CDS hedging**: Purchase CDS protection up to the full position notional
- **Position reduction**: Sell up to 50% of the position at market
- **Revolver draw block**: Notify agent bank to block further draws (if applicable and permitted under documentation)

All pre-IC actions require PM written authorization (email or secure message with timestamp) and must be ratified at the emergency IC session.

---

## 9. Post-Investment Action Materiality Thresholds

Not all post-investment events require full IC review. This section defines materiality thresholds that determine the governance level for post-investment actions.

### 9.1 Materiality Framework

| Action Type | PM Authority (No IC Required) | IC Notification (Next Standing IC) | Full IC Required |
|---|---|---|---|
| Covenant amendment — administrative (e.g., reporting deadline extension) | ✓ | — | — |
| Covenant amendment — financial (e.g., leverage step-up, EBITDA definition change) | — | If headroom impact <200bps | If headroom impact ≥200bps or affects maintenance test |
| Add-on acquisition by borrower | — | If add-on <15% of existing EBITDA | If add-on ≥15% of existing EBITDA |
| Position increase (existing approval) | Up to 25% of current position | 25-50% increase | >50% increase or exceeds original IC-approved size |
| Dividend recap or distribution | — | — | Always requires full IC |
| Collateral release | — | If <10% of collateral value | If ≥10% of collateral value |
| Sponsor equity cure | — | ✓ (notification with cure details) | — |
| Rating downgrade (1 notch) | — | ✓ | — |
| Rating downgrade (2+ notches or to CCC) | — | — | ✓ |

---

## 10. Subsequent Action Governance

This section covers IC governance for actions on existing portfolio positions that are not new investments.

### 10.1 Scope

Covers IC governance for actions on existing portfolio positions that are not new investments:
- **Position increase**: Adding to an existing approved position
- **Refinancing/reprice**: Rolling into a new facility that replaces the existing one
- **Add-on participation**: Participating in incremental debt issued by an existing borrower
- **Amendment/waiver consent**: Voting on borrower-requested documentation changes

### 10.2 Governance Tiers

| Action | IC Requirement | Documentation | Approval Authority |
|---|---|---|---|
| Position increase ≤25% of original | Notification only | Updated position summary | PM |
| Position increase >25% of original | Abbreviated IC review | Abbreviated memo (2-3 pages) | IC majority |
| Refinancing at same/tighter terms | Notification only | Term comparison sheet | PM |
| Refinancing at wider terms or weaker docs | Abbreviated IC review | Updated credit view + term comparison | IC majority |
| Add-on with incremental leverage ≤0.5x | Abbreviated IC review | Leverage impact memo | PM + Head of Research |
| Add-on with incremental leverage >0.5x | Full IC review | Updated full IC memo | Full IC |
| Amendment/waiver (immaterial) | PM discretion | Waiver summary | PM |
| Amendment/waiver (material — covenant reset, collateral release) | Full IC review | Amendment analysis memo | Full IC |

### 10.3 Abbreviated IC Memo Template (2-3 Pages)

#### For Position Increases

```
POSITION INCREASE REQUEST

Credit: [Name]
Current Position: $[X]mm ([Y]% of portfolio)
Proposed Addition: $[X]mm (new total: $[Y]mm, [Z]% of portfolio)

ORIGINAL APPROVAL:
- IC Date: [Date]
- Original Thesis: [1-2 sentences]
- Approval Conditions: [Any unresolved conditions]

THESIS UPDATE:
- Thesis still intact? [Yes/No with explanation]
- Key developments since original approval: [3-5 bullets]
- Current surveillance status: [Tier 1-4]

FINANCIAL UPDATE:
| Metric | At Approval | Current | Change |
|---|---|---|---|
| Leverage | X.Xx | X.Xx | +/-X.Xx |
| Coverage | X.Xx | X.Xx | +/-X.Xx |
| Spread | Xbps | Xbps | +/-Xbps |
| Price | XX.X | XX.X | +/-X.X |

CONCENTRATION IMPACT:
- Single-name: [X]% of [Y]% limit (post-increase)
- Sector: [X]% of [Y]% limit
- Rating bucket: [X]% of [Y]% limit

RATIONALE:
[Why increasing now — improved conviction, better price, portfolio rebalance]

RISKS:
[Any new risks or changed risks since original approval]
```

#### For Refinancing/Repricing

```
REFINANCING REVIEW

Credit: [Name]
Current Facility: [Describe — term, rate, maturity, covenants]
Proposed Facility: [Describe new terms]

TERM COMPARISON:
| Feature | Current | Proposed | Assessment |
|---|---|---|---|
| Spread | | | Better/Worse/Same |
| Maturity | | | Extended/Same/Shorter |
| Covenants | | | Tighter/Same/Looser |
| Amortization | | | More/Same/Less |
| Call protection | | | Better/Worse/Same |
| Incremental capacity | | | More/Same/Less |

NET ASSESSMENT:
[Is the refinancing credit-positive, neutral, or credit-negative? Would you participate in the new facility on the same terms as the old?]

RECOMMENDATION:
[Roll into new facility / Exit at par / Reduce position]
```

#### For Amendment/Waiver Consent

```
AMENDMENT/WAIVER ANALYSIS

Credit: [Name]
Request: [What the borrower is requesting]
Consent Deadline: [Date]

AMENDMENT DETAILS:
[Specific changes requested — covenant level, basket size, definition change]

CREDIT IMPACT:
[How does this change affect credit quality? Quantify if possible — e.g., "increases incremental debt capacity by $Xmm"]

FEE/COMPENSATION:
[What is being offered in exchange — consent fee, spread increase, additional reporting]

PRECEDENT:
[Have we seen similar amendments from this borrower or in this sector?]

RECOMMENDATION:
[Consent / Reject / Consent with conditions]
[If consent: document rationale for why terms remain acceptable]
[If reject: document specific objections and counter-proposal]
```

### 10.4 Decision Rules

#### Automatic Escalation to Full IC
Any subsequent action that would result in:
- Single-name exposure exceeding limit
- Position in a Tier 3+ credit
- Amendment that materially weakens credit protections (covenant holiday, collateral release, lien subordination)
- Refinancing with materially weaker documentation

#### De Minimis Threshold
Actions below $[X]mm or [Y]% of portfolio may be handled at PM discretion with notification to IC within 5 business days. Threshold should be defined per fund/mandate.

---

## 11. Cross-References

This governance framework integrates with the following reference files and skills:

| Reference / Skill | Integration Point |
|---|---|
| `references/escalation-trigger-thresholds.md` | Defines numeric triggers for Tier 3+ ad-hoc IC sessions |
| `references/portfolio-risk-parameters.md` | Supplies risk limits validated during IC approval |
| `skills/private-credit-middle-market/references/bdc-regulatory.md` | Ensures BDC private credit approvals comply with vehicle-specific mandates |
| `credit-committee` agent | Executes the structured IC challenge process and produces dissent records |
| `memo-generator` skill | Assembles the memo package presented at IC |
| `surveillance-monitoring` skill | Receives the post-close surveillance handoff |
| `portfolio-investment-process` skill | Validates position sizing and mandate compliance pre-IC |
