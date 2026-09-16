# Project health decision: Customer portal rebuild

CTO · Historical review of August 2026 evidence; latest recorded Jira update 11 August, steering 7 August, engineering digest through 8 August

## Recommendation

**Health: Amber for the reported 30 November commitment · Confidence: Medium.**

The project has material unresolved release threats, so Green is unsupported. The original 15 October plan has already slipped; that does not prove the revised date is impossible. Take Thursday's steering meeting toward explicit launch scope, a dated SSO resolution or fallback, and accountable payment/release decisions. Red would be justified if that exercise shows the required release cannot fit without changing the commitment. The supplied artifacts do not establish such a forecast yet.

## Findings that change the decision

| Evidence and source | Implication for the commitment | Confidence / competing explanation |
|---|---|---|
| Helen W's 7 August steering notes move launch from 15 October to 30 November and cite vendor dependency plus Sales requests, while live chat remains “to be discussed.” On 8 August engineers ask whether launch includes all epics or invoices/support. Parsed Jira has five `scope-added` rows: CP-115, 123, 133, 134, 143, totaling 34 estimated points. | An unsettled acceptance boundary prevents a credible remaining-work plan and may consume capacity on optional work. Sales' reported 1 December promises leave very little separation from launch. | High confidence in the recorded inconsistency; medium in its delivery effect. Product may have an approved release boundary absent from these records. Obtain that decision before attributing causality. |
| Sandbox absence recurs in June–August PMO notes and Priya's July–August digest. CP-101/102 remain In Progress; CP-103 role mapping is To Do and unassigned. | If SSO is required, login and integrated access testing are candidate release blockers. “Chasing vendor” supplies neither a usable date nor a tested fallback. | Strong corroboration of an unresolved dependency, without proving how much schedule it caused. A mock identity provider may unblock development, but does not demonstrate real-vendor integration or production acceptance. |
| Diego reports unresolved webhook design on 23 July through 6 August; CP-121/122 are To Do. CP-164 records session expiry during payment. CP-160 is Reopened for invoice totals. CP-152–154 record unassigned production provisioning, monitoring and load testing. | Payment correctness, invoice correctness and operational readiness need demonstrable acceptance before launch. UI progress alone cannot establish completion. | Medium: records identify concrete concerns, but dependencies, durations, severity decisions and any separate release plan are missing. Additional defect discovery can reflect effective testing, not worsening engineering quality. |

The CSV contains 32 unique issues: 13 Done, four In Progress, 14 To Do and one Reopened. These are recorded counts, not an outcome completion percentage. Export timestamp, filters and completeness are unspecified. Sprint associations do not establish carry-over history; Created/Updated fields do not establish time-in-status or velocity. Missing PR links do not prove missing review or tests. The PMO notes are successive reports from one author, not three independent confirmations.

## This week

| Action or leadership decision | Proposed owner / needed by | Evidence or outcome produced |
|---|---|---|
| Decide launch scope and acceptance, including each Sales addition; confirm rebaseline authority and customer promises. | Product sponsor with Sales and CTO / Thursday | One accepted release boundary and recorded scope/date trade-offs. |
| Escalate sandbox to obtain a committed usable date; assess fallback against actual launch requirements. | Priya with CTO/vendor owner / before Thursday | Explicit SSO dependency owner, needed-by point and viable fallback or leadership decision. |
| Resolve webhook retries and ownership; demonstrate consequences for payment acceptance. | Proposed decider Raj with payment lead / before Thursday | Architecture decision and remaining integration/test work, including session expiry. |
| Assemble remaining acceptance-to-release dependency plan and allocate release owners. | Engineering lead with QA/operations / within seven days | Dated, capacity-backed work and evidence for correctness, provisioning, monitoring, load testing and rollback; revised-date feasibility decision. |
| Replace unconditional Green reporting with this evidence and triggers. | Helen W with CTO / Thursday | Amber report distinguishing original slip from current risk; escalate to Red if the accepted release path cannot fit. |

Adding engineers is not yet justified: external commitments and design decisions may be binding, and the export does not establish a staffing shortage.

## What could change the recommendation

An already-approved narrower launch, committed vendor path and credible release plan could support Green. Conversely, an indispensable dependency arriving too late would support Red. Those three checks matter more than inferring causes from activity counts. No new launch date can be calculated from this snapshot.
