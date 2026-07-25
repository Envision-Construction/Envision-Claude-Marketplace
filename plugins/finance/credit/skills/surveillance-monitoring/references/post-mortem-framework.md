---
last_updated: "2026-03-21"
---

# Credit Post-Mortem Analysis Framework

A structured template for analyzing credit outcomes — both losses and unexpected wins. Post-mortems are conducted after any credit event that results in a material realized loss, a recovery outcome significantly different from expectations, or a near-miss that exposes a process gap. The purpose is institutional learning, not individual blame. Every post-mortem should produce specific, actionable improvements to the investment process.

---

## When to Conduct a Post-Mortem

A formal post-mortem is mandatory when any of the following occur:
- Realized loss exceeds 5% of the original position size
- Recovery achieved differs from the underwriting estimate by more than 15 percentage points
- A credit defaults or enters restructuring while held in the portfolio
- A credit is sold at a loss exceeding the stop-loss threshold approved at IC
- A watchlist credit that was de-escalated subsequently deteriorated again within 6 months
- A credit that was declined by IC later performed significantly better than expected (missed opportunity review)
- A near-miss where the outcome was favorable but the process failed (luck should not be confused with skill)

---

## Section 1: Credit Identification

| Field | Entry |
|---|---|
| **Credit Name** | [Issuer / Borrower] |
| **Sector / Industry** | [GICS sector and sub-industry] |
| **Instrument(s) Held** | [1L TL, 2L TL, Bonds, etc.] |
| **Rating at Purchase** | [Moody's / S&P / Fitch] |
| **Rating at Event** | [Moody's / S&P / Fitch] |
| **Initial Position Date** | [YYYY-MM-DD] |
| **Event Date** | [YYYY-MM-DD — default, restructuring announcement, or sale date] |
| **Holding Period** | [X months / years] |
| **Primary Analyst** | [Name] |
| **Portfolio Manager** | [Name] |
| **IC Approval Date** | [YYYY-MM-DD] |
| **Post-Mortem Date** | [YYYY-MM-DD] |
| **Post-Mortem Author** | [Name — ideally not the original analyst, or co-authored with an independent reviewer] |

---

## Section 2: Original Investment Thesis

Reproduce the key elements of the original IC memo thesis. This section establishes the baseline against which the actual outcome will be measured.

### Thesis Summary (As Presented to IC)
1. [First pillar — e.g., "Stable recurring revenue base with 90%+ retention rates supports leverage de-leveraging from 5.5x to 4.0x within 24 months"]
2. [Second pillar — e.g., "Strong sponsor (Firm X) with proven track record in the sector and history of supporting portfolio companies through downturns"]
3. [Third pillar — e.g., "Attractive relative value at S+475 vs. B-rated cohort average of S+400, compensating for customer concentration risk"]

### Key Underwriting Assumptions

| Assumption | Underwriting Value | Trigger for Concern | Thesis Violation |
|---|---|---|---|
| Revenue growth | [X%] | [< X%] | [Negative growth] |
| EBITDA margin | [X%] | [< X%] | [< X%] |
| Leverage trajectory (exit) | [X.Xx] | [> X.Xx] | [> X.Xx] |
| Free cash flow | [$XXmm] | [< $XXmm] | [Negative] |
| Customer retention | [X%] | [< X%] | [< X%] |

### Identified Risks at Underwriting

| Risk | Probability Assessed | Severity Assessed | Mitigant Identified |
|---|---|---|---|
| [Risk 1] | [Low / Medium / High] | [Low / Medium / High] | [Mitigant] |
| [Risk 2] | [Low / Medium / High] | [Low / Medium / High] | [Mitigant] |
| [Risk 3] | [Low / Medium / High] | [Low / Medium / High] | [Mitigant] |

---

## Section 3: What Actually Happened

### Timeline of Key Events

| Date | Event | Impact | Signal Available? |
|---|---|---|---|
| [YYYY-MM-DD] | [Event — e.g., Q2 earnings miss: EBITDA $45mm vs. $60mm model] | [Leverage increased to 6.2x] | [Yes — supplier checks indicated order slowdown 6 weeks prior] |
| [YYYY-MM-DD] | [Event — e.g., CFO resignation] | [Market price dropped 3 points] | [Yes — industry contacts noted departures at peer companies] |
| [YYYY-MM-DD] | [Event — e.g., Covenant amendment requested] | [Spread widened 150 bps] | [Partially — headroom had been compressing but pace accelerated] |
| [YYYY-MM-DD] | [Event — e.g., Default / Restructuring announced] | [Position marked to $XX] | [N/A — this was the event] |

### Actual vs. Underwriting Performance

| Metric | Underwriting Case | Actual at Event | Variance | Variance (%) |
|---|---|---|---|---|
| Revenue | [$XXXmm] | [$XXXmm] | [($XXmm)] | [(X%)] |
| EBITDA | [$XXmm] | [$XXmm] | [($XXmm)] | [(X%)] |
| EBITDA Margin | [X%] | [X%] | [(X pp)] | |
| Total Leverage | [X.Xx] | [X.Xx] | [+X.Xx] | |
| Interest Coverage | [X.Xx] | [X.Xx] | [(X.Xx)] | |
| Free Cash Flow | [$XXmm] | [($XXmm)] | [($XXmm)] | |
| Liquidity | [$XXmm] | [$XXmm] | [($XXmm)] | |

---

## Section 4: Outcome

### Financial Impact

| Metric | Value |
|---|---|
| **Entry Price** | [$XX.XX / par] |
| **Exit Price / Recovery Value** | [$XX.XX / par] |
| **Coupon / Interest Received** | [$X.Xmm] |
| **Total Return (Dollar)** | [($X.Xmm) or $X.Xmm] |
| **Total Return (%)** | [(X.X%) or X.X%] |
| **Annualized Return** | [(X.X%) or X.X%] |
| **Contribution to Fund Performance** | [(X.XX%) or X.XX%] |

### Recovery Analysis (If Default / Restructuring)

| Metric | Underwriting Estimate | Actual | Variance |
|---|---|---|---|
| Enterprise Value at Resolution | [$XXXmm] | [$XXXmm] | [($XXmm)] |
| EV / EBITDA Multiple at Resolution | [X.Xx] | [X.Xx] | [(X.Xx)] |
| Recovery Rate (Our Instrument) | [XX%] | [XX%] | [(XX pp)] |
| Time to Resolution | [X months] | [X months] | [+X months] |
| Legal / Advisory Costs Borne | [$X.Xmm] | [$X.Xmm] | |

---

## Section 5: Signal Analysis

This is the most critical section. For each early warning signal, assess whether it was available, whether it was detected, and whether it was acted upon.

### Signals Present Before the Event

| Signal | Date First Detectable | Detected by Team? | Acted Upon? | Action Taken (or Why Not) |
|---|---|---|---|---|
| [e.g., Revenue deceleration in quarterly filings] | [YYYY-MM-DD] | [Yes / No] | [Yes / No] | [e.g., Detected but attributed to one-time factors; model not updated] |
| [e.g., Supplier channel checks showing order declines] | [YYYY-MM-DD] | [No] | [N/A] | [e.g., No supplier channel check process in place at the time] |
| [e.g., CDS spread widening ahead of peers] | [YYYY-MM-DD] | [Yes] | [No] | [e.g., Attributed to technical flow; no fundamental review triggered] |
| [e.g., Management selling personal shares] | [YYYY-MM-DD] | [No] | [N/A] | [e.g., Insider transaction monitoring not part of surveillance workflow] |
| [e.g., Peer company in sector announced distress] | [YYYY-MM-DD] | [Yes] | [Partially] | [e.g., Added to watchlist but did not accelerate financial review] |

### Signal Classification

| Category | Count | Examples |
|---|---|---|
| **Signals detected and acted on** | [X] | [List] |
| **Signals detected but not acted on** | [X] | [List — these represent process failures in escalation or decision-making] |
| **Signals available but not detected** | [X] | [List — these represent gaps in the monitoring framework] |
| **Signals not reasonably available** | [X] | [List — e.g., fraud, undisclosed information] |

---

## Section 6: Process Failures

Identify the specific points in the investment process where the framework broke down. Be precise — "we should have done more analysis" is not actionable.

### Underwriting Phase Failures

| Failure | Description | Impact |
|---|---|---|
| [e.g., Insufficient downside scenario] | [Downside case assumed 10% EBITDA decline; actual decline was 25%. The downside was anchored to the base case rather than stress-tested independently] | [Recovery analysis was based on an enterprise value that proved 40% too high] |
| [e.g., Customer concentration underweighted] | [Top customer was 30% of revenue; risk was noted but mitigant ("long-term contract") was not verified — contract had a 90-day termination clause] | [Customer loss was the primary driver of EBITDA decline] |

### Surveillance Phase Failures

| Failure | Description | Impact |
|---|---|---|
| [e.g., Delayed model update] | [Q3 financials were not incorporated into the model for 6 weeks after filing; by that time, Q4 preliminary results showed further deterioration] | [Watchlist escalation was delayed by one full quarter] |
| [e.g., Escalation threshold too loose] | [Yellow tier trigger required leverage increase of 0.5x; actual leverage increased 0.4x for 3 consecutive quarters without triggering escalation] | [Gradual deterioration was missed because no single quarter breached the threshold] |

### Decision-Making Failures

| Failure | Description | Impact |
|---|---|---|
| [e.g., Anchoring to entry price] | [PM declined to sell at 92 because entry was par; position eventually sold at 75] | [Incremental loss of $X.Xmm from delay in exit decision] |
| [e.g., Sunk cost fallacy] | [IC voted to maintain position because "we've already taken the mark"; no re-underwriting was conducted] | [Position continued to deteriorate an additional X points] |

---

## Section 7: Documentation Gaps

What covenant protections or structural features should have been required, or what documentation weaknesses contributed to the adverse outcome?

| Gap | Description | Recommendation |
|---|---|---|
| [e.g., Absent EBITDA add-back cap] | [Credit agreement permitted unlimited cost savings add-backs; reported "Adjusted EBITDA" was $80mm vs. actual cash EBITDA of $55mm] | [Require add-back caps (maximum 25% of EBITDA) in future underwriting standards] |
| [e.g., Weak restricted payments covenant] | [Sponsor extracted $XXmm dividend 6 months before distress using builder basket capacity] | [Add restricted payment analysis to standard covenant review checklist] |
| [e.g., No financial maintenance covenant] | [Covenant-lite structure provided no early warning of deterioration] | [Adjust pricing requirements for cov-lite to compensate for monitoring gap; require tighter spread thresholds for watchlist escalation] |

---

## Section 8: Lessons Learned

Each lesson must be specific and actionable. Generic statements like "improve our analysis" are not acceptable.

### Underwriting Process Improvements

| # | Lesson | Specific Action | Owner | Implementation Deadline |
|---|---|---|---|---|
| 1 | [e.g., Customer concentration risk was underweighted because contract verification was not part of the standard workflow] | [Add contract term verification (including termination provisions) to the due diligence checklist for any issuer with >15% single-customer concentration] | [Head of Research] | [Date] |
| 2 | [e.g., Downside scenario was insufficiently severe] | [Implement independent downside stress using sector-specific historical worst-case metrics rather than percentage haircuts from the base case] | [Analyst Team] | [Date] |

### Surveillance Process Improvements

| # | Lesson | Specific Action | Owner | Implementation Deadline |
|---|---|---|---|---|
| 1 | [e.g., Cumulative deterioration across quarters was missed because triggers were point-in-time only] | [Add trailing 3-quarter cumulative trigger: if leverage increases more than 0.5x cumulatively over any 3-quarter period, escalate to Yellow regardless of single-quarter movement] | [Risk] | [Date] |
| 2 | [e.g., Channel checks would have provided 6+ weeks advance warning] | [Establish quarterly supplier/customer channel check program for top 20 portfolio exposures] | [Head of Research] | [Date] |

### Decision-Making Improvements

| # | Lesson | Specific Action | Owner | Implementation Deadline |
|---|---|---|---|---|
| 1 | [e.g., Anchoring to entry price delayed exit decision by 3 months] | [Implement mandatory re-underwriting at current market price (not cost basis) for any credit that has declined more than 5 points from entry] | [PM / CIO] | [Date] |

---

## Section 9: Portfolio Impact

### Correlation and Concentration Effects

| Question | Assessment |
|---|---|
| Were other portfolio holdings affected by the same event or sector stress? | [Yes / No — if yes, list affected names and impact] |
| Did this loss reveal a hidden correlation (e.g., common customer, supplier, or macro factor)? | [Yes / No — describe] |
| Was the position appropriately sized given the risk? | [Yes / No — if oversized, what sizing framework would have been appropriate?] |
| Did the loss, combined with other concurrent losses, breach any portfolio-level risk limits? | [Yes / No — specify which limits and by how much] |

### Portfolio-Level Lessons

| # | Lesson | Action |
|---|---|---|
| 1 | [e.g., Three portfolio companies had the same top customer; the loss in this name was compounded by spread widening in the other two] | [Implement common-customer overlap screen for portfolio-level concentration monitoring] |
| 2 | [e.g., Sector allocation of 22% masked the fact that all three names were in the same sub-sector niche] | [Add sub-sector concentration tracking to the portfolio risk dashboard] |

---

## Distribution and Follow-Up

| Item | Detail |
|---|---|
| **Distribution** | All IC members, Risk Committee, Head of Research |
| **Presentation** | Post-mortem must be presented at the next regular IC meeting |
| **Action Item Tracking** | All action items entered into the team's action tracker with named owners and deadlines |
| **Follow-Up Review** | Implementation of lessons learned reviewed at [90 days / next quarterly risk review] |
| **Retention** | Permanent file — post-mortems are never deleted or archived |
