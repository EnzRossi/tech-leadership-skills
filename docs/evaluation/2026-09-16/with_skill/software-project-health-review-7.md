# Project health decision: tracker snapshot interpretation

PM · CSV export date and project commitment not supplied

## Recommendation

**Health: Not assessable · Confidence: High that the requested conclusions are unsupported by these fields.** Do not calculate delivery cycle time from Created and Updated dates, and do not declare QA Red because a PR column was omitted. The supplied description supports a reported count of 18 issues recorded Done. It does not establish when work started or finished, whether testing happened, or whether the project's release commitment is achievable.

## Findings that change the decision

| Evidence and source | Implication for the commitment | Confidence / competing explanation |
|---|---|---|
| User describes 18 issues marked Done. | This reports a current recorded state, not 18 independently accepted outcomes or overall completion. | No CSV was supplied for independent counting or checking filters and duplicate rows. |
| Created and Updated exist; status history does not. | Created-to-Updated is an elapsed interval between two record timestamps, not cycle time or time-in-status. | Updated could reflect comments, metadata changes or reopening after completion. Created is not necessarily work start. |
| PR-link column was not exported. | PR evidence is unavailable in this artifact. | The omission says nothing about actual review, implementation or testing. |

Cycle time requires explicit start and end definitions plus events that capture those boundaries. For example, a team could choose first entry into active work through completion, with a stated policy for reopened issues. These are choices to establish before calculating, not meanings to assign retroactively to Created and Updated. Even a Resolved field would require checking completion and reopening semantics.

Likewise, QA health concerns the acceptance and release work required for the commitment. A PR link can help locate implementation evidence, but its presence would not by itself prove adequate testing. Its absence from an export cannot prove inadequate testing. There is no observed quality failure here and no basis to invent one from a missing column.

## This week

| Action or leadership decision | Proposed owner / needed by | Evidence or outcome produced |
|---|---|---|
| Replace the proposed metric/status with a statement of artifact limits. | PM / next update | “18 issues reported Done; cycle time and QA health not established by this export.” |
| Obtain status-transition history and agree cycle-time boundaries. | Tracker administrator and delivery lead / within three working days | Timestamped start/end events, reopen policy and export scope suitable for calculation. |
| Obtain acceptance criteria, test results and release checks for the work that matters to the current commitment. | QA or engineering owner / this week | Direct evidence of quality coverage and any actual release threat. |

A broader QA intervention or demand to retroactively populate links is not justified by this snapshot. First obtain the evidence needed for the question rather than changing the workflow to fit an export.

## What could change the recommendation

Three facts would materially help: the agreed project outcome and current target; reliable workflow history; and direct acceptance/test evidence for the remaining release path. History would enable a defined cycle-time calculation. Quality evidence could support a health rating independently of the tracker. Until then, report the known artifact limitation without converting uncertainty into a red project status.
