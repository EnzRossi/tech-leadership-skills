# Customer portal health assessment

For the CTO and Thursday steering committee; assessed as of the supplied August 2026 evidence, through 11 August. Decision: intervene and re-plan commitments.

## Overall

**Red · Low confidence in the full assessment.** **INFERENCE:** Active scope growth, an undated vendor dependency and unresolved payment design decisions make the green report unreliable. The intervention is justified by corroborated delivery evidence; overall confidence is low because eight dimensions remain unknown. A release/dependency plan and a conversation with the technical lead and sponsor would materially improve the picture.

## Three findings that matter most

1. **The date moved without a credible release recovery. FACT:** Steering changed 15 October to 30 November, a 46-day slip, while retaining Green and adding scope (steering, 12 June and 7 August). Two accounts were promised availability on 1 December. **INFERENCE:** One day between planned launch and customer commitment leaves little room for failure.
2. **The critical dependencies are unresolved. FACT:** The same SSO sandbox risk and mitigation appear in all three steering reports; engineering still has no vendor date on 28 July or sandbox on 8 August. Payment webhook design remains unresolved across 23, 28 and 30 July and 6 August digest entries; CP-120–122 remain open. **INFERENCE:** Additional calendar time alone does not unblock the release.
3. **Reported activity is not verified readiness. FACT:** The 32-row export has 13 Done records, five without a linked PR; CP-160 is reopened. Six records span at least three listed sprints. Between 6 July and 11 August inclusive, 11 issues were created and four resolved. **INFERENCE:** Scope/defect inflow is outpacing closure within this export; neither ticket totals nor story points establish business completion.

## Evidence base

| Artifact | Date | Author / vantage | Freshness at August assessment |
|---|---|---|---|
| jira-export.csv | Export time unspecified; latest update 11 August, earliest creation 4 May | Author unknown; tracker snapshot | Current snapshot inferred; older unchanged rows are aging signals, not status histories. |
| steering-notes.md, steering sections | 12 June, 10 July, 7 August | Helen W, PMO upward report | August current; June/July historical baseline, stale for current status. |
| steering-notes.md, engineering digest | 21 July–8 August | Attributed engineers; digest compiler unknown | Current team view; completeness unknown. |

No direct evidence for business outcome, success measures, product validation, team allocation, skill coverage, internal delivery commitments, or customer adoption preparation. These remain Unknown.

## Dimension ratings

| Cluster | Dimension | Rating | Evidence |
|---|---|---|---|
| Purpose | Outcome clarity | Unknown | UNKNOWN: no business brief; 8 August asks what launch includes, establishing release ambiguity rather than the business objective. |
| Purpose | Success metrics | Unknown | UNKNOWN: no baseline/target supplied. |
| Purpose | Product uncertainty | Unknown | UNKNOWN: no research or prototype feedback supplied. |
| Plan | Scope stability | At risk | FACT: five scope-added records; steering 7 August adds features; digest 4 August still questions live-chat inclusion. |
| Plan | Milestone progress | At risk | FACT: launch shifts 46 days, steering 12 June versus 7 August. |
| Plan | Critical path | At risk | INFERENCE: launch delay explicitly tied to vendor; no committed sandbox date, digest 28 July. Full path is unknown. |
| Plan | Internal dependencies | Unknown | UNKNOWN: billing discrepancy and architecture decision exist, but agreed team deliverables/dates are absent. Decision issue rated separately. |
| Plan | External dependencies | At risk | FACT: SSO vendor uncommitted, CP-101–103 and repeated digest entries. |
| People | Team capacity | Unknown | UNKNOWN: aging and carry-over show problems, but cannot establish actual allocation or overload. |
| People | Skill gaps | Unknown | UNKNOWN: no skills inventory; do not equate unresolved design with missing expertise. |
| People | Decision latency | At risk | FACT: webhook decision repeatedly requested 23 July–6 August, while card UI began 30 July. |
| People | Stakeholder alignment | At risk | FACT: steering 7 August names live chat added and still to be discussed; digest 4 and 8 August questions scope and launch. |
| Quality | Shipped quality | At risk | FACT: CP-160 reopened multi-currency bug; digest 4 August records divergence from billing. No production incident evidence supplied. |
| Quality | Testing | Unknown | UNKNOWN: no test evidence field or QA artifact; five Done records lack PR links, which is a verification gap, not proof tests do not exist. |
| Quality | Technical risk | At risk | INFERENCE: payment integration decision remains open during build, digest 23–30 July; load test CP-154 unscheduled. |
| Readiness | Operational readiness | Watch | FACT: staging/CI Done (CP-150–151), but production and monitoring tasks CP-152–153 unassigned, monitoring unscheduled. Runbooks/rollback unknown. |
| Readiness | User/adoption readiness | Unknown | UNKNOWN: Sales commitments do not establish training, pilot, support or rollout readiness. |

Eight dimensions are Unknown in this table; this further limits confidence.

## Changes and top risks

**FACT:** Date moved 46 days; five scope-added items now appear; a Sales commitment risk appeared in August. SSO mitigation is unchanged across three reports. CP-120 was last updated 20 June, 52 days before 11 August; this is record staleness, not a measured in-progress duration. CP-103 and CP-121–122 have unchanged May dates and no assignees.

| Risk | Evidence | Mitigation state | Proposed owner |
|---|---|---|---|
| Vendor blocks release again | Three steering reports; repeated team blocker | Chasing has produced no dated commitment | CTO-designated vendor relationship owner; Priya technical lead |
| Payment flow incomplete or unsafe | CP-120–122, CP-164; webhook digest | Architecture review mentioned, no recorded decision | Raj and payments lead |
| Scope consumes revised schedule | Five scope-added items, live-chat ambiguity | No explicit scope-out documented | Product and sponsor |
| Unverified release quality | CP-160 reopened; missing QA/readiness evidence | Unknown | QA/release owner to be named |

## Causes and hypotheses

**INFERENCE — supported cause:** Unresolved external access is delaying SSO: tracker blocked-vendor labels and independent team/PMO accounts agree. **INFERENCE — supported cause:** Scope approval is not being translated into a shared release boundary: scope-added records and the team's live-chat/launch questions corroborate that gap.

**Hypothesis:** Upward reporting rewards optimism or treats reset dates as recovery. Repeated Green reports despite slips support investigation but do not prove motive; ask Helen what Green criteria were applied. **Hypothesis:** Payment ownership lacks decision authority; confirm with Raj and Diego before changing staffing.

**ASSUMPTION:** Thursday refers to the next steering meeting in the supplied evidence context. The exact meeting date is not supplied; due dates below are relative to it, not September dates.

## Missing information

Obtain the sponsor's outcome/metrics brief, integrated dependency/release plan, actual allocation and skill coverage, QA/test/acceptance evidence, and rollout/support plan. These distinguish a delivery blockage from broader capability or product problems.

## Leadership decisions for Thursday

| Decision | Options and consequences |
|---|---|
| Release scope and promise | Reduce the first release to an explicitly accepted subset, preserving more time for quality; or retain scope and renegotiate the customer date. Neither option currently has a validated delivery forecast. |
| Vendor dependency | Secure a dated commitment plus fallback trigger; or authorize a bounded alternative feasibility check. A mock IdP can enable development but does not prove production integration. |
| Payment design authority | Give a named decider authority and a decision deadline; continued deferral preserves rework risk. |

## Next seven days

| Action | Proposed owner | Due | Evidence produced |
|---|---|---|---|
| Agree first-release outcome, acceptance and explicit exclusions with Product and Sales | CTO/sponsor | Before Thursday | Signed release boundary, success measures and commitment options |
| Obtain vendor date or document fallback decision | Vendor owner with Priya | Thursday | Written commitment, fallback trigger and dependency plan |
| Resolve webhook design and remaining payment dependencies | Raj with Diego | Before Thursday | Decision record and testable payment completion sequence |
| Verify Done work, reopened defect and highest-risk payment paths; inventory release controls | QA/release lead | Within seven days | Test evidence, defect disposition, production/rollback/monitoring gaps |
| Reforecast bounded scope using actual allocation and dependency dates | Helen with engineering lead | Within seven days | Integrated release plan with owners, contingencies and evidence-based status criteria |

Do not add engineers, reorganize, or replace tooling on this evidence. The demonstrated bottlenecks are dependency and decision resolution; parallelizable capacity shortage has not been established. Customer commitment changes remain leadership decisions.
