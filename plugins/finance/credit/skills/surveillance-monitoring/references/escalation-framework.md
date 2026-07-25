---
name: Escalation Framework
description: |
  Combined escalation reference covering surveillance color tiers, governance chain, required documentation by stage, thesis-kill trigger linkage, conditional approval tracking, de-escalation principles, and post-mortem linkage.
last_updated: "2026-03-22"
---

# Escalation Framework

This file consolidates the escalation tier definitions and IC escalation governance into a single reference covering the full escalation lifecycle: classification, ownership, documentation, decision rights, condition tracking, de-escalation, and post-mortem.

> Use `references/escalation-trigger-thresholds.md` for current numeric trigger and de-escalation levels.

## Tier Overview

The escalation framework exists to convert deterioration into consistent action. It combines a surveillance color, a governance tier, a named owner, and a required document so that stressed names are handled predictably rather than informally.

| Status | Surveillance Meaning | Primary Owner | Core Deliverable |
|---|---|---|---|
| Green | Performing in line with thesis | Analyst | Routine surveillance update |
| Yellow | Early thesis drift | Analyst with PM visibility | Watch memo |
| Orange | Material deterioration or action framing required | Analyst + PM + broader governance visibility | Concern report |
| Red | Imminent or actual stress requiring binding decision | Full governance engagement | Situation report |

## Tier Definitions

### Green

- The credit is performing broadly as expected.
- Monitoring remains routine and thesis-based.
- The analyst still needs to document material developments, but there is no formal escalation.

### Yellow

- One or more warning signals suggest the thesis is drifting.
- The right response is to raise visibility, tighten monitoring, and document what changed.
- A Yellow credit belongs on a formal watchlist even if no position action is yet required.

### Orange

- Deterioration is now material enough that monitoring alone is not sufficient.
- Downside, hedgeability, structural risk, and action alternatives should all be explicitly assessed.
- The main mistake at this stage is producing updates that describe weakness without forcing a decision discussion.

### Red

- The credit is near or in an event-driven state: breach, default risk, liquidity crisis, LME, or similarly acute deterioration.
- Decision rights, execution feasibility, legal analysis, and recovery framing all become active.
- The position should be treated as a live risk-management problem, not a normal surveillance item.

## Escalation Chain

```
Analyst Identification -> PM / Team Review -> IC Notification -> Binding IC Decision -> Post-Decision Monitoring or Distressed Handoff
```

The specific tier matters less than the discipline behind it:
- identify the trigger clearly
- name the owner
- produce the required document
- record the decision and follow-up action

## Governance Tiers

### Analyst Watch

- Used when early thesis drift is present but the position is still manageable within normal surveillance.
- The analyst owns the situation, documents the trigger, and informs the PM.
- The key deliverable is a concise watch memo: what changed, why it matters, and how monitoring will intensify.

### Team Review

- Used when deterioration becomes material enough to require coordinated review rather than analyst-only judgment.
- This is where downside work, hedging feasibility, documentation risk, and sponsor or management engagement should become explicit.
- The key deliverable is a concern report that frames action alternatives rather than simply restating weak metrics.

### IC Notification

- Used when the deterioration, event, or governance issue requires formal committee visibility and a binding decision path.
- At this point, the question is no longer only "what happened?" but "what are we going to do?"
- The key deliverable is a situation report covering facts, downside, structure, and recommended action set.

### Emergency IC

- Used for payment default, bankruptcy, fraud, severe liquidity failure, or similarly acute events.
- Protective action can be taken quickly, but the rationale and follow-up must still be documented and ratified.
- The key deliverable is an emergency situation report focused on immediate facts, remedies, and executable actions.

## Required Actions by Tier

### Watch Memo
- identify the breached or approaching trigger
- explain whether the issue is temporary, cyclical, structural, or governance-related
- state what additional monitoring will occur
- state what would force further escalation

### Concern Report
- update the base and downside view
- identify structural, covenant, documentation, and liquidity implications
- assess action alternatives such as maintain, reduce, hedge, or engage
- clarify what decision the PM or committee must now make

### Situation Report
- summarize the event and immediate facts
- frame current financial position and structural rights
- present downside and recovery logic
- recommend executable actions and owners

### Emergency Situation Report
- immediate facts, legal or structural implications, executable options, required approvals

## Documentation by Escalation Stage

| Stage | Purpose | Core Contents |
|---|---|---|
| Watch Memo | Frame early deterioration | Trigger, current thesis view, expected trajectory, monitoring changes |
| Concern Report | Evaluate action alternatives | Updated projections, downside scenario, structural issues, proposed actions |
| Situation Report | Support binding decision | Event summary, financial position, capital structure, recovery framing, action recommendation |
| Emergency Situation Report | Support urgent protective action | Immediate facts, legal or structural implications, executable options, required approvals |

## Notification Chain

```
Analyst -> PM -> IC Chair / Governance Forum -> Full Decision Makers
```

Escalation should be auditable:
- who identified the issue
- when it was identified
- what document was produced
- what action was taken
- what follow-up remains open

## Thesis-Kill Trigger Linkage

Surveillance works best when escalation tiers are set at approval, not invented during stress. Each thesis-kill trigger should be mapped to:
- the measurable breach condition
- the surveillance color and governance tier it implies
- the owner who must respond
- the required document and decision forum

This mapping should be established when the investment is approved and revisited when the thesis changes.

## Conditional Approval Tracking

When IC grants a conditional approval:
- every condition must have a verification method, owner, and deadline
- open conditions must be revisited in each monitoring cycle until verified or failed
- unmet conditions are governance events, not administrative footnotes
- if a failed condition changes the risk profile materially, the investment must return to the appropriate decision forum

Suggested condition register:

| Condition | Verification Method | Responsible Party | Deadline | Status |
|---|---|---|---|---|
| [IC condition] | [Document review / data confirmation / legal sign-off] | [Owner] | [Date] | Open / Verified / Failed |

## De-Escalation Principles

De-escalation should be slower than escalation and should not be based on a single favorable data point.

General rules:
- de-escalate only when the original trigger is resolved or clearly reversing
- require evidence that stabilization is durable, not just headline-positive
- document de-escalation with the same discipline used for escalation
- move one stage at a time rather than skipping directly from severe stress to normal status
- if a credit re-escalates soon after de-escalation, treat that as a process-learning event

## Re-Review Standard

A position should be re-reviewed when:
- a condition cannot be met as originally approved
- the trigger was not technically breached, but the economics now look meaningfully different
- the recommended action set has changed from hold to reduce, hedge, exit, or engage
- portfolio concentration, vehicle constraints, or structural risk has changed the decision context

## Post-Mortem Linkage

Credits that escalate through severe deterioration, distressed exit, or governance failure should feed directly into `references/post-mortem-framework.md`.

Governance-specific post-mortem questions include:
- were the original escalation triggers appropriately designed
- was the escalation path followed in time
- did the committee decision framework help or delay action
- were conditional approvals or monitoring obligations strong enough for the realized downside
