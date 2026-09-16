# Project health decision: Customer Portal Rebuild

CTO · Historical assessment: August 2026 evidence; steering through 7 August, engineering digest through 8 August, Jira entries through 11 August. Export timestamp and filtering are unspecified.

## Recommendation

**Health: Amber for the reported 30 November commitment · Confidence: Medium.** Thursday’s steering committee should replace Green with an explicit recovery decision: agree launch acceptance, secure the SSO dependency or a viable alternative, and resolve the payment design. The revised date remains plausible, but current evidence does not substantiate it. The original 15 October target has slipped; this does not prove November is unachievable. Sponsor approval of the rebaseline is unverified. Sales’ reported 1 December commitments leave little room for release or adoption problems.

## Findings that change the decision

| Evidence and source | Implication for the commitment | Confidence / competing explanation |
|---|---|---|
| Helen W’s 7 August steering report moves launch from 15 October to 30 November for vendor dependency and additional scope, while live chat remains undecided. The 30 July–8 August engineering digest questions live chat inclusion and whether launch means all epics or invoices/support. | Without accepted release boundaries, remaining work cannot be assessed against November or the two customer promises. This is an acceptance and decision problem. | High confidence in inconsistent accounts; actual approved scope may exist outside these artifacts. Obtain sponsor-approved acceptance and customer commitments. The repeated PMO reports are one reporting lineage. |
| CP-101/102 record SSO vendor blockage; Priya’s 28 July and 8 August reports describe no committed sandbox date and continued nonavailability. CP-122 is To Do; Diego’s 23 July–6 August reports describe the unresolved webhook decision involving Raj. | If authentication and payments are required, sandbox-dependent integration and unresolved retry behavior are candidate release blockers. Mock integration may advance development but cannot establish real-provider readiness. | Medium confidence in delivery exposure: scope and dependency durations are missing. Sandbox work may be parallelizable, and the webhook choice may affect less work than implied. Demonstrate affected acceptance paths before claiming a critical path. |
| CP-152–154 record production provisioning, monitoring and load testing as unassigned/To Do. CP-160 is reopened; Marcus reports invoice totals differing from billing on 4 August. CP-164 records payment-session expiry. | Operational acceptance and financial correctness require explicit ownership and evidence. Completed screens do not establish a usable launch; unresolved defects could prevent acceptance. | Medium confidence: a separate release plan or test evidence may exist, and defect discovery may reflect effective QA. Capacity and severity are not established by assignments alone. |

Sprint associations and Updated dates establish neither continuous blockage nor velocity. Missing PR links do not prove absent testing.

## This week

All assignments and deadlines below are proposed unless already recorded.

| Action or leadership decision | Proposed owner / needed by | Evidence or outcome produced |
|---|---|---|
| Approve launch scope, acceptance and rebaseline; reconcile the two account promises. | Product lead, Sales and sponsor / Thursday | Signed release boundary. Decide full-scope date exposure versus a phased launch with reduced customer capability; verify customer acceptability before changing promises. |
| Escalate SSO for a dated sandbox commitment and integration window; assess mock/fallback feasibility. | Priya, with CTO escalation / before Thursday | Vendor commitment or explicit alternative decision, including remaining real-provider validation and acceptance implications. |
| Decide webhook retry ownership and session behavior. | Raj with Diego / within two working days | Recorded design decision and demonstrated path to payment acceptance; expose any remaining dependency. |
| Build the remaining release plan against accepted scope. | Engineering lead with QA/operations / within seven days | Owners, realistic allocation and dependencies; production, load, monitoring, rollback/support readiness and defect acceptance evidence. Establish whether November is credible. |

Do not add engineers or replace the supplier yet: neither intervention has a demonstrated route to removing these decision and dependency constraints within the available time.

## What could change the recommendation

An approved narrow release, committed integration dates and a feasible readiness plan could support Green. Conversely, required acceptance work that cannot fit November without changing scope, date or resources warrants Red. No delivery forecast is justified from this snapshot.
