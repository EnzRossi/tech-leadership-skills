# Project health methodology

EnzRossi's synthesis; [sources](sources.md) attribute the underlying concepts. This is a diagnosis aid, not a validated risk score or delivery-date predictor.

## Artifact limits

Before computing, establish the export's scope, timestamp, field meaning, duplicates, parent/child rows and filters. Preserve source IDs. Count with a parser when tools are available; otherwise omit uncertain totals. Label counts as counts, not completion percentages.

| Available data | Supports | Does not establish |
|---|---|---|
| Current status and Created/Updated dates | Current recorded state and time since last recorded update | Start date, time-in-status, cycle time, or whether work stopped |
| Semicolon-separated sprint field | Recorded association with several sprints | Actual commitment/carry-over each sprint without board history |
| Linked PR field | Links included in this export | Absence of testing, reviews, or implementation elsewhere |
| Created and Resolved dates | Counts in an explicitly chosen window, subject to reopen/filter semantics | Scope inflow to a milestone unless milestone membership history is known |
| Story points | Estimates in this team's convention | Percent of business value delivered, hours or cross-team productivity |
| Priority/assignee | Recorded priority and assignment | Critical-path membership or actual individual load |

Compare original and approved current dates. Do not treat a renamed milestone as deception without checking scope equivalence and approval. Freshness is relative to the question: yesterday's snapshot matters for tomorrow's cutover; old decisions can still explain a slip. When no newer evidence exists, label the review historical.

## Signals

Each signal has an alternative explanation and a discriminating check. Keep those distinct from the observed fact.

| Area | Signal and possible mechanism | Check before concluding |
|---|---|---|
| Outcome/acceptance | Stakeholders describe different launch scope; acceptance repeatedly changes | Ask the accountable product/sponsor owner for the accepted release boundary. A migration can have a valid technical acceptance outcome; it need not invent a revenue metric. |
| Scope/milestones | Dates shift while required work grows; remaining hard work not demonstrated | Compare change approvals, baseline scope and remaining acceptance work. Planned discovery and approved scope trade-offs are not necessarily dysfunction. |
| Dependencies/decisions | Same blocker persists; work starts around an unsettled design; supplier has no commitment | Identify the affected acceptance path, decider and needed-by point. Confirm mitigation actually removes exposure; "chasing vendor" is not a dated delivery commitment. |
| Capacity/ownership | Necessary tasks unowned; incidents consume the team; one expert gates reviews | Check allocation and work queues. An assignee list is not a capacity model; identify review/onboarding load before adding staff. |
| Quality/release/adoption | Reopened correctness defects, late integration, untested migration, no demonstrated rollback/support readiness | Inspect defect severity, test coverage by failure mode, production-like rehearsal, operational acceptance and affected-user readiness. More defects may reflect better discovery rather than worsening quality. |

For technical debt, require a delivery mechanism: e.g., schema coupling prevents parallel migrations, flaky tests delay releases, or recurring incidents displace planned work. Recommend a bounded repair tied to that mechanism; do not default to a rewrite.

## From symptoms to action

Write: **evidence → candidate mechanism → threatened commitment → discriminating check → intervention**.

Example: repeated deferred webhook decision → integration work may be blocked → payment acceptance date exposed → verify dependency and decision owner → obtain decision or remove payments from this release. This does not prove the whole project lacks architectural leadership.

Treat independently collected observations differently from reports quoting each other. Confidence may be high in a missed milestone and low in its cause. A known breach can justify Red even when other areas are unknown. Conversely, an evidence gap cannot by itself justify Red or Amber. Use the health definitions in SKILL.md rather than a second set of scoring rules.

Before recommending extra engineers, show separable work, a lead with review capacity, access/onboarding time, and why the contribution arrives before the constraint binds. If the bottleneck is a decision or external commitment, adding engineers does not remove it. State what should continue when the current response is working.

## Worked example using the repository fixture

The fixture is fictional; observations are as of the supplied August 2026 records, not today's status.

- Steering notes, 7 August: target changed from 15 October to 30 November while status remained Green; additional scope requested by Sales. This is a reported rebaseline, not proof the new date is impossible.
- The CSV contains five `scope-added` rows: CP-115, CP-123, CP-133, CP-134, CP-143. Their combined estimates are 34 points; this is neither velocity nor progress.
- CP-101 and CP-102 list Sprint 3 through Sprint 9. The notes independently report an unresolved sandbox; sprint association alone would not prove continuous blockage.
- Standup entries from 23 July through 6 August record the unsettled webhook design. The 8 August note asks what launch includes. These support a decision/acceptance threat, not a diagnosis of individual incompetence.
- CP-152–154 record unassigned, not-started production provisioning, monitoring and load testing. The export does not establish whether a separate release plan exists.

A defensible assessment is Amber for the revised commitment, or Red if the required launch path cannot credibly recover, with that inference explained. Ask for accepted launch scope, a vendor date/fallback and the remaining release path. Do not assert a new launch forecast, fourteen carried-over issues, or an inflow rate: this snapshot cannot establish those histories.
