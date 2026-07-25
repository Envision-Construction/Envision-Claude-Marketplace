## Description: <br>
Forensic insurance-industry research orchestrator with nested specialist agents covering captive insurance formation, IRC 831(b) vs 831(a) elections and micro-captive enforcement, cell and rent-a-captive structures, captive domicile selection, coverage lapses and cancellation-notice law, and premium finance mechanics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Third-Party Community Consideration
This skill is not owned or developed by NVIDIA. This skill has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Envision Construction Agent Card](https://github.com/Envision-Construction/claude-code-memory). <br>

### License/Terms of Use: <br>
## Use Case: <br>
Employees (Envision / Prometheus Ventures insurance and finance staff) use this skill for compliance-risk analysis of captive insurance structures, statutes, and broker proposals — cited decision support that ends with an escalation line naming what requires licensed counsel or a credentialed actuary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Yes] <br>
**Credential Type(s):** [OAuth Token] <br>  

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. See skill body for more details. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Captive Formation and the 831(b) Election](references/captive-formation-831b.md) <br>
- [Cell Structures](references/cell-structures.md) <br>
- [Coverage Lapse Law](references/coverage-lapse-law.md) <br>
- [Current Legislation (dated snapshot)](references/current-legislation.md) <br>
- [Forensic Research Protocol](references/forensic-research-protocol.md) <br>
- [Premium Finance](references/premium-finance.md) <br>
- [Full Engagement Playbook](workflows/full-engagement.md) <br>
- [Legislation Refresh Workflow](workflows/legislation-refresh.md) <br>
- [26 U.S.C. § 831 (Cornell LII)](https://www.law.cornell.edu/uscode/text/26/831) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis] <br>
**Output Format:** [Markdown — cited analysis in complete sentences with tables for enumerable comparisons; mandatory closing escalation line] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Every load-bearing figure re-verified from current official sources; two independent sources per load-bearing claim] <br>

## Evaluation Agents Used: <br>
- Claude Code <br>



## Evaluation Tasks: <br>
12 keyed prompts (3 fabricated-authority traps, 3 stale-figure/currency traps, 3 domain-depth, 3 judgment) x 2 configs (with skill / without) x 3 repeat runs = 72 runs; 210 keyed-fact checks graded by independent scorer agents against an adversarially verified answer sheet, plus 24 blind order-swapped A/B judgments (EVAL.md, 2026-07-04). <br>

## Evaluation Metrics Used: <br>
Reported benchmark dimensions: <br>
- Keyed-fact pass rate: Fraction of keyed factual checks answered correctly against the verified answer sheet. <br>
- Trap pass rate: Resistance to fabricated-authority and stale-figure/currency trap prompts. <br>
- Fabrication rate: Rate of invented legal authority in responses (lower is better). <br>
- Citation validity: Fraction of extracted citations verified as valid against live web sources. <br>
- Blind A/B wins: Blind order-swapped pairwise preference judgments between with-skill and without-skill answers. <br>

Underlying evaluation signals used in this run: <br>
- `keyed_fact_checks`: 210 keyed-fact checks graded by independent scorer agents against an adversarially verified corpus. <br>
- `web_verified_citations`: 350 extracted citations verified against live web sources. <br>
- `blind_ab_judgments`: 24 blind order-swapped A/B judgments; judges not told which config produced which answer and instructed not to reward length. <br>



## Evaluation Results: <br>
| Metric | With skill (36 runs) | Without skill (36 runs) |
|---|---|---|
| Keyed-fact pass rate | **100%** (105/105) | 92.4% (97/105) |
| Trap pass rate | **100%** (18/18) | 83.3% (15/18) |
| Fabrication rate (invented authority) | 0% | 0% |
| Citation validity (web-verified) | **100%** (180/180) | 98.8% (168/170) |
| Blind A/B wins | **20** | 4 (0 ties) |

## Skill Version(s): <br>
9549265 (source: git SHA, committed 2026-07-25) <br>


