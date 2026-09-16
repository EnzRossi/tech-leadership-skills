# Methodology: Software Project Health Review

This file holds the detailed method behind `SKILL.md`. Read the section the workflow points you to; you rarely need all of it at once.

Contents:
1. Signal catalog (by artifact type)
2. Dimension rubric (seventeen dimensions, four ratings)
3. From symptoms to causes
4. Overall health and confidence rules
5. Worked example
6. Why the method is shaped this way

The method is EnzRossi's synthesis. The concepts it draws on are attributed in `sources.md`.

---

## 1. Signal catalog

A signal is a pattern in an artifact that changes the probability of a problem. Signals are not verdicts. Record each one as FACT with a citation, then decide what it implies.

### 1.1 Issue tracker exports (Jira, Linear, Azure Boards, GitHub Projects)

Read the export as a dataset, not as a list. Where it has dates, compute rather than skim.

| Signal | How to detect it | What it usually means |
|---|---|---|
| Carry-over | Same issues appear in three or more consecutive sprints or cycles | Estimates are not trusted, work is blocked, or the team is overcommitted |
| Scope inflow inside a fixed target | Issues created in the epic or milestone after the plan was set, at a rate close to or above the closure rate | Scope is not stable; the end date is drifting whether or not anyone has said so |
| Aging work in progress | Issues in an active state for more than two to three times the team's typical cycle time | Hidden blockers, unclear acceptance criteria, or one person carrying too much |
| Silent tickets | No comments, status changes, or links for two weeks or more while nominally in progress | Work has stopped, or is happening outside the tracker |
| Estimate creep | Story points or estimates revised upward more than once on the same item | The problem is less understood than the plan assumes |
| Closed without evidence | Issues moved to Done with no linked pull request, test reference, or reviewer | "Done" means "coded", not "verified"; expect a QA or integration bulge later |
| Frozen epics | Parent items whose children have not changed state in a sprint | The area is deprioritized, blocked, or nobody owns it |
| Unassigned critical items | High-priority or blocking issues with no assignee for more than a few days | Ownership gap or capacity gap |
| Bug ratio rising | Share of new issues that are defects rising over consecutive periods | Quality debt is arriving; velocity numbers will overstate progress |
| Reopened issues | Items closed then reopened | Acceptance criteria are unclear or testing is late |

What a tracker cannot tell you: whether the outcome is still the right one, whether users want it, whether the architecture will hold, or how the team feels. Do not rate Purpose or People dimensions from tracker data alone.

### 1.2 Plans, roadmaps, and milestone lists

| Signal | How to detect it | What it usually means |
|---|---|---|
| Right-shift without scope-out | Dates move later while the deliverable list stays the same | The slip is being absorbed rather than managed |
| Plateau near completion | Percent-complete reports of 80 to 95 percent for several periods | Remaining work is the hard, uncertain part; the metric is measuring tasks, not risk |
| Milestone renaming or splitting | A milestone becomes two, or is renamed with a later date | A slip is being hidden in plain sight |
| Single-threaded critical path | The path to the release runs through one engineer, one team, or one external party | Any absence or delay there moves the release one for one |
| No float anywhere | Every task is described as critical | The plan was not sequenced, or padding was removed under pressure |
| Missing integration and hardening time | The plan goes from "feature complete" to "release" in days | The plan assumes the first integration works |
| Original dates unavailable | Only current dates are shown | You cannot see drift; ask for the baseline |

### 1.3 Status reports and steering notes

| Signal | How to detect it | What it usually means |
|---|---|---|
| Green with slipped dates or grown scope | Compare the rating with the plan signals above | Watermelon reporting: green outside, red inside |
| Ratings without criteria | No definition of what earns Green, Amber, or Red | The rating reflects the author's comfort, not the project's state |
| Persistent risk | The same risk appears in three or more reports with the same owner and same mitigation text | The risk is not being worked, or the mitigation is not working |
| Vanishing risk | A risk disappears without a recorded resolution | Either quietly resolved or quietly dropped; ask which |
| Escalations without outcome | "Raised with X" recorded, no decision recorded later | Decision latency |
| Uniform positivity | Every section positive, no trade-offs mentioned | Bad news is not travelling upward; this is a reporting-culture signal, not evidence of health |

Reports from a vendor or partner about their own delivery deserve the same treatment as internal reports, plus one extra question: what does the contract reward them for reporting?

### 1.4 Meeting notes, standups, retrospectives, Slack digests

| Signal | How to detect it | What it usually means |
|---|---|---|
| Deferred decision | "To be discussed next week" for the same item across meetings | Decision latency; the team is working around an open question |
| Smoothed disagreement | Disagreement recorded, then the topic disappears without a decision | Stakeholder misalignment that will resurface at release |
| Absent users | No mention of users, customers, acceptance, or feedback for several weeks | The team is building to a spec, not to an outcome |
| Repeated firefighting | Incidents, hotfixes, or support requests dominate standups | Capacity is being consumed by operations; plan velocity is fictional |
| Same blocker, different day | A blocker named in more than two standups | Nobody has authority or time to remove it |
| Retrospective items never actioned | The same improvement appears in successive retrospectives | Team has stopped believing change is possible |

Meeting notes are the best available evidence for decision latency and stakeholder alignment. They are weak evidence for progress.

### 1.5 Engineering and delivery metrics

Delivery-performance metrics (deployment frequency, lead time, change failure rate, recovery time) describe how well the team can ship. They say nothing about whether what is shipping leads to the project outcome. Use them for:

- Team capacity and quality (stable or degrading?)
- Operational readiness (can this team deploy and recover quickly?)

Do not use velocity, story points completed, or lines of code as evidence of progress toward the goal. Rising velocity with a static remaining scope is a good sign; rising velocity with growing scope tells you nothing.

### 1.6 Risk registers

A risk register is evidence of what the team is worried about, not of what will happen. Useful reads:

- Risks with no owner, no trigger, and no dated mitigation are decoration.
- Risks that have already materialized but are still listed as risks indicate the register is not maintained.
- The absence of the obvious risks (key-person dependency, external dependency, integration) is itself a signal.

### 1.7 QA, release, and incident data

- Test coverage numbers without a statement of what is covered are weak evidence. A rising defect count late in the schedule is strong evidence.
- A release plan without rollback, monitoring, and support ownership indicates operational readiness is Unknown at best.
- Production incidents on adjacent systems during the project consume the team's capacity; count them.

---

## 2. Dimension rubric

Rate each dimension **Healthy**, **Watch**, **At risk**, or **Unknown**. The rubric describes what the evidence looks like at each level. If none of the artifacts speaks to the dimension, the rating is Unknown, and the assessment names the artifact that would resolve it.

### Purpose

**Outcome clarity**
- Healthy: a one-sentence statement of the change the project should cause for users or the business exists, is recent, and appears in the team's own artifacts, not just the sponsor's.
- Watch: the outcome is stated but the team's tracker and notes only ever mention features.
- At risk: different artifacts state different outcomes, or the outcome is a deliverable ("launch the new portal") rather than a result.
- Resolve Unknown with: the original brief or the sponsor's one-pager.

**Success metrics**
- Healthy: one to three measures with a baseline and a target, and a way to measure them after release.
- Watch: measures exist but no baseline, or the measurement method is undefined.
- At risk: no measures, or measures that only count delivery (on time, on budget).
- Resolve Unknown with: ask the sponsor how they will know in six months whether the project worked.

**Product uncertainty**
- Healthy: the riskiest assumptions about users have been tested (prototype, pilot, research) and the results are recorded.
- Watch: assumptions are listed but untested; testing is planned late.
- At risk: the plan builds the full scope before any user contact, or research contradicts the plan.
- Resolve Unknown with: any user research, prototype feedback, or pilot data.

### Plan

**Scope stability**
- Healthy: scope changes are recorded, each traded against date or budget, and the net change over the last month is small.
- Watch: scope is growing slowly with informal approval.
- At risk: inflow near or above closure rate; features added without anything removed.

**Milestone progress**
- Healthy: milestones are hit or slips are small, recorded, and explained; the baseline is visible.
- Watch: one slip, absorbed, with a credible recovery.
- At risk: repeated right-shift, plateau near completion, or renamed milestones.

**Critical path**
- Healthy: the path to release is identified, has float, and has no single point of failure.
- Watch: identified but runs through one person or team.
- At risk: not identified, or runs through an external party with no commitment.

**Internal dependencies**
- Healthy: other teams' deliverables are listed with dates and named owners who have agreed.
- Watch: listed but not agreed by the delivering team.
- At risk: discovered dependencies appearing in notes; a dependency already late.

**External dependencies**
- Healthy: vendors, partners, and regulators are listed with contractual or written dates and a fallback.
- Watch: dates exist, no fallback.
- At risk: dependency on an external party's roadmap, procurement, or approval without a date.

### People

**Team capacity**
- Healthy: the team is stable, allocation is known, and operational load is measured and leaves room for planned work.
- Watch: partial allocations, one recent departure, or operational load rising.
- At risk: key people at low allocation, planned hires not started, or firefighting dominating standups.

**Skill gaps**
- Healthy: the skills the architecture needs exist in the team or are contracted with knowledge transfer planned.
- Watch: one critical skill in one person.
- At risk: a required skill is absent and the plan assumes learning on the critical path.

**Decision latency**
- Healthy: open decisions have a named decider and a date; notes show decisions being made.
- Watch: decisions take more than two weeks; escalations are needed to move them.
- At risk: the same decision deferred three or more times; the team is building around the gap.

**Stakeholder alignment**
- Healthy: the sponsor, product, engineering, and affected business owners state the same priorities in their own artifacts.
- Watch: differences in emphasis; one stakeholder rarely present.
- At risk: recorded disagreement without resolution, or a stakeholder discovered late.

### Quality

**Quality of what has shipped**
- Healthy: defect trend flat or falling; incidents on the new work are rare and resolved.
- Watch: defect trend rising but understood.
- At risk: reopened issues, rising bug ratio, or incidents that consume the team.

**Testing**
- Healthy: automated tests exist for the delivered work; acceptance criteria are written before build; test evidence is linked to Done.
- Watch: testing is manual but planned and staffed.
- At risk: testing is a phase at the end, or "Done" has no test evidence.

**Technical risk**
- Healthy: the hardest technical questions (scale, integration, data migration, security) were proven early with a spike or prototype.
- Watch: known unknowns scheduled for later.
- At risk: the plan assumes an unproven integration or migration works on first attempt; architecture debates ongoing while build continues.

### Readiness

**Operational readiness**
- Healthy: monitoring, alerting, runbooks, rollback, on-call ownership, and support handover are planned with owners and dates, and the team can already deploy the system to a production-like environment.
- Watch: planned but unstaffed.
- At risk: no mention of operations, or the first production deployment is the launch.

**User and adoption readiness**
- Healthy: the people who will use or be affected by the system know when it arrives, have been trained or involved, and there is a rollout plan with a feedback loop.
- Watch: a communication plan exists; no involvement yet.
- At risk: users unaware, or a "big bang" cutover with no fallback.

---

## 3. From symptoms to causes

A cause explains several At-risk ratings at once. Name it as a **root cause** only when at least two independent kinds of evidence support it (for example, tracker data and meeting notes). Otherwise write it as a **hypothesis** with the evidence that would confirm it.

| Pattern of symptoms | Candidate cause | Confirming evidence |
|---|---|---|
| Scope inflow + deferred decisions + smoothed disagreement | No single accountable owner, or owner without authority | Who approves scope changes? Who can say no? |
| Carry-over + estimate creep + silent tickets | The problem is less understood than the plan assumes; discovery is happening inside delivery | Spikes or prototypes were skipped; architecture debates in notes |
| Green reports + slipped dates + persistent risks | Reporting culture penalizes bad news | Compare team-level notes with upward reports |
| Firefighting + aging WIP + rising bugs | Capacity is consumed by operations or by another project | Allocation data; incident counts |
| Frozen epics + unassigned criticals + skill in one person | Key-person dependency | Who touched the frozen area last? |
| Absent users + deliverable-shaped outcome + delivery-only metrics | Project framed as output; nobody owns the result | The sponsor's success criteria |
| Late integration + no operational plan + first deploy at launch | Plan optimized for feature completion, not for release | Release plan; environment availability |

Do not present a cause the leader cannot act on. "The team is not good enough" is not a diagnosis; "the architecture requires a skill the team does not have, and the plan gave no time to acquire it" is.

---

## 4. Overall health and confidence rules

**Overall health**

- **Red**: a Purpose or Plan dimension is At risk with no mitigation in motion, or the critical path is At risk and no decision to address it is scheduled, or two or more clusters contain At-risk dimensions.
- **Amber**: any dimension At risk with an active mitigation, or two or more dimensions on Watch in the same cluster, or Purpose dimensions Unknown.
- **Green**: no dimension At risk, at most two on Watch, and fewer than a third of dimensions Unknown.

An assessment that would be Green except for many Unknowns is **Amber with Low confidence**, not Green.

**Confidence in the assessment**

- **High**: evidence from at least three vantage points (for example, tracker, team notes, sponsor reports), newest evidence within two weeks, fewer than a quarter of dimensions Unknown.
- **Medium**: two vantage points, or evidence two to four weeks old, or up to a third Unknown.
- **Low**: a single vantage point, or evidence older than four weeks, or more than a third Unknown.

State what would raise confidence. Usually it is one artifact and one conversation.

---

## 5. Worked example

**Inputs supplied.** A Jira export for a customer-portal rebuild (two teams, nine sprints), three monthly steering decks, the last four weeks of standup notes.

**Evidence ledger.** Jira: current to yesterday. Steering decks: written by the PMO, latest three weeks old, all rated Green. Standup notes: engineering-authored, current. No PRD, no risk register, no release plan, no metrics baseline.

**Signals.** Jira: 14 issues carried over three or more sprints (FACT, filter on sprint history); issue inflow to the release epic 31 created versus 26 closed over the last four sprints (FACT); two epics "Payments" and "SSO" with no child state change in three sprints (FACT). Steering decks: Green in all three; release date moved from 15 Oct to 30 Nov between deck one and deck three with an unchanged scope list (FACT); risk "SSO vendor sandbox unavailable" present in all three decks, same owner, same mitigation text (FACT). Standups: SSO blocker named in eleven of twenty standups (FACT); no mention of users, pilots, or acceptance in any note (FACT).

**Ratings.** Scope stability: At risk. Milestone progress: At risk. External dependencies: At risk (SSO vendor). Decision latency: At risk (SSO risk unworked for three months). Outcome clarity, success metrics, product uncertainty: Unknown (no PRD, no user mentions). Testing: Unknown (no test evidence in Done issues, but no QA data either). Operational readiness: Unknown (no release plan). Team capacity: Watch (carry-over suggests overcommitment; no allocation data). Others: Unknown or Watch.

**Root cause (hypothesis).** The SSO dependency is blocking the Payments and SSO epics and nobody with authority over the vendor relationship owns it; the PMO reports Green because the date was reset and the risk is "tracked". Confirming evidence: the vendor contract owner; whether anyone has escalated to the vendor.

**Overall.** Red. Confidence Medium: three vantage points and current data, but more than a third of dimensions Unknown.

**Decisions for leadership.** (1) Who owns the SSO vendor relationship and by what date will sandbox access be confirmed or an alternative chosen? (2) Given 31-in versus 26-out, does the 30 Nov date hold with reduced scope, or does the date move again?

**Seven-day actions.** Obtain the original brief and success metrics from the sponsor; get the SSO vendor commitment in writing or start a fallback spike; extract test evidence for Done issues from the last two sprints; produce a scope-change log since the 15 Oct baseline; add operational readiness to the next steering agenda.

**Do not change.** Team composition; the two-team structure; the tracker or workflow; the sprint length. Nothing in the evidence points at them, and changing them now would consume the capacity the project lacks.

---

## 6. Why the method is shaped this way

- **Ledger before interpretation** because reviews inherit the bias of whatever document they read first. Research on IT project reporting finds status reports on troubled projects are biased a majority of the time, and optimistic far more often than pessimistic; the people closest to the problem are often the last to tell senior management.
- **Unknown as a first-class rating** because the alternative, silently rating unevidenced dimensions as fine, is exactly how watermelon projects stay green.
- **Purpose before Plan** because a project can be perfectly on schedule toward the wrong result, and no amount of tracker analysis reveals that.
- **Two sources for a root cause** because a single artifact reflects a single vantage point, and confident causal claims from one vantage point are the fastest way to lose the trust of the team being reviewed.
- **Decision latency as a dimension** because large-sample project research identifies slow decisions as a leading cause of failure, and it is the cheapest problem to fix once named.
- **A "do not change" list** because leaders under pressure reach for headcount, reorganization, and re-planning, all of which have a well-documented cost that arrives before any benefit.
