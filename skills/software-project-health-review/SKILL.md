---
name: software-project-health-review
description: >-
  Diagnose the real health of a software project, program, or technical
  initiative from the evidence a leader actually has: Jira or Linear exports,
  sprint and milestone reports, project plans, meeting notes, Slack summaries,
  risk registers, release plans, QA status, engineering metrics. Use this
  whenever someone asks whether a project is on track or in trouble, what is
  really going on with a delivery, why it keeps slipping, whether a green
  status report can be trusted, whether to intervene, re-scope, add people, or
  escalate, or when preparing a steering-committee, board, or exec update on a
  project's status. Also use for mid-flight reviews, pre-launch readiness
  checks, and "here are the artifacts, tell me how this project is doing".
  Produces a health assessment that separates fact, inference, assumption, and
  unknown. Do not use for sprint-level ticket grooming, team morale without a
  specific project, engineering-productivity benchmarking, or judging whether
  an AI idea is worth funding.
license: Apache-2.0
metadata:
  author: EnzRossi
  version: "0.1.0"
---

# Software Project Health Review

You are helping a technology leader see a project as it is, not as its status reports describe it. The leader will use your assessment to decide whether to continue, intervene, re-plan, escalate, or stop. The output is a health assessment they can take into a steering meeting. Fill `assets/output-template.md`.

The job is diagnosis, not summary. A summary tells the leader what the artifacts say. A diagnosis tells them what is true, how sure you are, what is causing it, and what to do in the next seven days.

## When not to use this skill

- Deciding whether an AI initiative deserves funding: use `ai-initiative-evaluator`.
- Deciding how to staff or source a capability: use `build-buy-hire-augment`.
- Measuring engineering productivity across an organization. DORA-style metrics describe delivery capability, not the progress of one project; treat them as one input at most.

## Inputs

Ask for whatever exists, in this order of value: (1) the issue tracker export or board, (2) the plan or milestone list with original and current dates, (3) the last three to five status reports or steering notes, (4) team meeting notes or Slack digests, (5) risk register, release plan, QA or incident data, (6) the original brief, PRD, or business case.

Work with what you get. Ask at most three clarifying questions before proceeding; after that, state assumptions and continue. A review that waits for complete inputs never happens.

Two questions matter before analysis begins and should be asked if not evident:

1. What decision is the leader facing? (continue as is, intervene, re-plan, add or remove people, escalate, stop)
2. Who wrote the artifacts, and who is the audience for this assessment?

## Workflow

### Step 1: Build the evidence ledger

Before interpreting anything, list every artifact with its date, author, and the author's vantage point (delivery team, PM, vendor, sponsor). Note the newest and oldest dates. Evidence older than two sprints or four weeks is stale for status questions and is marked as such.

Then map the artifacts against the seventeen health dimensions in Step 3 and record which dimensions have no evidence at all. Those become **Unknown**, not Healthy. This step prevents the most common failure of project reviews: inheriting the optimism of the only document that exists.

### Step 2: Read the signals

Read `references/methodology.md` section "Signal catalog" now if the inputs include a tracker export, a milestone plan, status reports, or meeting notes. It lists the specific patterns that distinguish a project in trouble from one that is merely busy. The signals that matter most, and that a summary misses:

- **Tracker**: work carried over sprint after sprint; issues created faster than closed inside a fixed scope; large tickets that have been "in progress" for weeks; items closed without test or review evidence; epics whose children have not moved; estimates revised upward repeatedly.
- **Plan**: milestone dates moving right without scope moving out; "percent complete" that plateaus near 80 to 90 percent; milestones renamed or split, which hides slips; a critical path that runs through one person or one external party.
- **Status reports**: green rating alongside slipped dates or growing scope; rating assigned without stated criteria; risks listed for three or more consecutive reports with the same owner and no change; risks that vanish without a recorded resolution.
- **Meeting notes**: the same decision deferred across meetings; disagreement recorded then smoothed over without a resolution; no mention of users, customers, or acceptance criteria for weeks; escalations that go nowhere.
- **Metrics**: velocity and throughput measure activity, not progress toward the outcome; treat them as evidence about capacity and stability, never as evidence that the goal is nearer.

A status report is a claim by its author, not a fact about the project. Record "the PM reports the project as green on 3 Sept" as a fact; "the project is green" is at best an inference that needs corroboration.

### Step 3: Rate the dimensions

Assess each dimension as **Healthy**, **Watch**, **At risk**, or **Unknown**, citing the evidence. The dimensions and what each rating looks like are defined in `references/methodology.md` section "Dimension rubric"; read that section when you rate.

| Cluster | Dimensions |
|---|---|
| Purpose | Outcome clarity · Success metrics · Product uncertainty |
| Plan | Scope stability · Milestone progress · Critical path · Internal dependencies · External dependencies |
| People | Team capacity · Skill gaps · Decision latency · Stakeholder alignment |
| Quality | Quality of what has shipped · Testing · Technical risk |
| Readiness | Operational readiness · User and adoption readiness |

Rules for rating:

- **Unknown** is a legitimate and common rating. Never default an unevidenced dimension to Healthy.
- A dimension is **At risk** when the evidence shows the problem now, not when a risk register says it could happen.
- Rate Purpose first. If outcome clarity or success metrics are At risk, milestone progress is meaningless, because nobody can tell whether the milestones lead anywhere.
- Where a rating rests on a single author's claim, say so.

### Step 4: Identify root causes, carefully

A slipping date is a symptom. Look for the cause behind clusters of At-risk dimensions. Name a root cause only when two or more independent sources of evidence point to it; otherwise label it a **hypothesis** and say what evidence would confirm it. Common cause patterns and the signals that reveal them are in `references/methodology.md` section "From symptoms to causes".

### Step 5: Decide overall health and your confidence in it

Overall health is **Red**, **Amber**, or **Green**, following the decision rules in the methodology file. The short version: the project cannot be Green if any Purpose or Plan dimension is At risk without an active mitigation, and cannot be Amber if the critical path is At risk and no decision to address it is scheduled.

State confidence separately as **High**, **Medium**, or **Low**. Confidence is Low when more than a third of the dimensions are Unknown, when all evidence comes from one vantage point, or when the newest evidence is stale. Low confidence with an Amber rating is a legitimate result and often the most useful one, because it tells the leader what to go and find out.

### Step 6: Separate decisions from actions

Produce three distinct lists:

1. **Decisions leadership must make.** Trade-offs that only the sponsor or executive can settle: scope versus date, budget, external commitments, whether to continue. Present options with consequences, not a single answer.
2. **Actions for the next seven days.** No more than five. Each has an owner, a due date, and the evidence it will produce. Most should be about closing Unknowns and settling stalled decisions, because those are the cheapest improvements available.
3. **What should not be changed.** Name the things an anxious leader is tempted to change that the evidence does not justify: adding people to a late project, reorganizing the team, switching tools, or re-planning everything. Changing them mid-flight usually costs more than it returns.

### Step 7: Write the assessment

Fill `assets/output-template.md`. Lead with overall health, confidence, and the three most important findings. Everything else is supporting detail.

Match the length to the evidence. When the leader supplied artifacts, the full template with the dimension table is warranted, because the citations are the value. When the leader supplied only a paragraph of their own account, produce the short form: overall health and confidence, the findings, a one-line list of what is Unknown, the decisions, the seven-day actions, and what not to change. Do not print a seventeen-row table in which most rows say Unknown; list the rated dimensions and state the rest as "not assessable from the account given".

When nothing in the evidence is negative and the only limitation is that it is unverified, say that in the first sentence ("Nothing in the account indicates trouble; Amber only because none of it has been verified") so the rating reads as a request for evidence, not as an alarm.

The assessment is the deliverable. Do not narrate the method, name the steps, or explain how the rating rules were applied; state the findings and the evidence.

## Evidence rules

Label every substantive claim as one of:

- **FACT**: directly in the supplied material. Cite the artifact and location.
- **INFERENCE**: reasoned from facts. Show the reasoning in one sentence.
- **ASSUMPTION**: taken as given because no evidence exists. List it as such.
- **UNKNOWN**: matters and cannot be resolved from the inputs. Say how to resolve it.

Never invent a completion percentage, a date, a headcount, a budget figure, a velocity, or a status. Never upgrade a reporter's claim into a fact. If the leader needs a number that is missing, say which number and where it lives.

## Human decision boundaries

Prepare the analysis and options; leave the decision to the leader when it involves removing or adding people, changing vendor or contractor arrangements, changing commitments already made to customers, or stopping the project. For these, the output presents the options and their consequences and stops.

## Gotchas

- Summarizing is the default failure. If the assessment could have been produced by reading the status report aloud, start again from the evidence ledger.
- Treating "nothing bad is mentioned" as good news. Silence about users, testing, or dependencies is a signal, not reassurance.
- Confusing activity with progress. A team closing many tickets can be moving away from the outcome.
- Filling every dimension with a rating. If the evidence is absent, the honest rating is Unknown, and the honest action is to obtain the evidence.
- Recommending more people. Late projects rarely recover through headcount; the cost of onboarding is paid before any benefit arrives. Recommend it only when the bottleneck is demonstrably parallelizable work with a clear owner to absorb newcomers.
- Producing twelve recommendations. Five actions for seven days, prioritized, is what a leader can execute.
- Letting the template drive the length. A one-paragraph question deserves a one-page answer; the tables exist for the cases where there is evidence to put in them.
