---
name: build-buy-hire-augment
description: >-
  Decide how to source a technology or engineering capability: build it
  in-house, buy a SaaS or platform, hire full-time engineers, use contractors or
  staff augmentation, engage a project-based engineering partner or agency, use
  a specialist consultant, combine approaches, or wait and validate first. Use
  this whenever a CTO, CEO, VP of Engineering, or founder asks "should we build
  or buy this", "should we hire or outsource", whether to use an agency, dev
  shop, nearshore or offshore team, freelancers, or contractors, how to staff a
  new initiative or fill a skills gap, whether to replace a vendor with an
  internal build, or how to add engineering capacity fast. Produces a sourcing
  recommendation with alternatives, trade-offs, cost drivers, transition and
  exit strategy, and the conditions under which it would change. Deliberately
  neutral: recommends against outside firms when they are not the best answer.
  Not for comparing two named vendors, writing job descriptions, running
  hiring, or negotiating contracts.
license: Apache-2.0
metadata:
  author: EnzRossi
  version: "0.1.0"
---

# Build, Buy, Hire, Augment

You are helping a technology leader decide how to obtain an engineering or technology capability. The output is a sourcing recommendation built from `assets/output-template.md` that they can defend in a leadership meeting and revisit when conditions change.

**Declared interest.** This skill is published by EnzRossi, a company that sells software engineering and staff-augmentation services. The skill is designed to counteract that interest: when the analysis is close between an external option and an internal one, prefer the internal one, and recommend an outside firm only when the evidence in Step 5 supports it. A leader who follows this skill should end up not hiring an outside company at least as often as hiring one.

## When not to use this skill

- Whether an AI initiative deserves investment at all: use `ai-initiative-evaluator` first. This skill assumes the capability is wanted.
- A project already underway that is struggling: use `software-project-health-review`. Adding or changing suppliers to a troubled project is a different decision from sourcing a new capability.
- Choosing between two named products or two named vendors, drafting job descriptions, or negotiating rates and contracts. Hand those to procurement, recruiting, or legal.

## Inputs

Ask for, in order of value: (1) the capability needed and the business reason it is needed now, (2) the timeline and what happens if it is missed, (3) how long the need is expected to last, (4) who in the organization would own it, (5) the current team's skills and load, (6) constraints: budget shape, security or compliance requirements, data residency, existing vendor relationships, (7) anything already tried.

Ask at most four questions before proceeding on stated assumptions. If the requester has already chosen an option and wants validation, evaluate the alternatives anyway; the comparison is the value.

## Workflow

### Step 1: Define the capability and the decision

Write the capability as an outcome the business needs, not as a role or a product ("process 50,000 invoices a month with under one percent exceptions", not "hire two backend engineers" or "buy an invoicing tool"). Then write what the organization would stop doing, or fail to do, if it does not obtain the capability. If the answer is "nothing much", the recommendation is probably **wait**.

### Step 2: Decompose before deciding

A capability is rarely one thing. Split it into components and mark each as **differentiating** (part of how the organization wins) or **commodity** (necessary, but the same for everyone). Most requests contain both. The differentiating components and the commodity components usually have different right answers, and the most common sourcing mistake is applying one answer to the whole. Read `references/methodology.md` section "Decomposition" for the test.

### Step 3: Assess the sixteen dimensions

Rate each dimension using the rubric in `references/methodology.md` section "Dimension rubric". Read that section now.

| Group | Dimensions |
|---|---|
| Nature of the capability | Differentiation · Maturity of the problem · Domain knowledge required · Integration depth |
| Shape of the demand | Urgency · Duration · Iteration frequency · Requirement uncertainty |
| Internal position | Internal skills · Internal capacity · Talent availability · Capacity to manage the option |
| Constraints | Security and compliance · Knowledge retention requirement · Reversibility and lock-in · Budget shape |

Where the inputs are silent, the rating is **Unknown**, and it appears in the memo as information still needed. Do not rate talent availability, budget shape, or urgency from general knowledge; these are facts about this organization and this market.

### Step 4: Screen out options

Apply the knockout rules in `references/methodology.md` section "Knockout rules" to the eight options. A knockout removes an option regardless of its other merits: for example, a compliance regime that forbids external access to the data removes staff augmentation and partners for that component; a requirement that is still undefined removes a fixed-scope partner engagement; a duration under a year removes hiring for that component alone. Record every knockout with its reason, so the leader sees why an option they favored is absent.

### Step 5: Compare the survivors

For each surviving option, use the fit table in `references/methodology.md` section "Option profiles" to judge fit against the dimension ratings. Then apply the neutrality rule:

> Recommend an external firm (staff augmentation, project partner, or consultant) only when at least two of the following are true for the component: the urgency cannot be met by the hiring market; the duration is bounded; the skill is absent internally and is not core long term; internal capacity is blocked by other commitments that will not move. Otherwise prefer hire, build, buy, or wait.

Also check the mirror conditions, which are listed in the methodology under "Signs the internal option is wrong": a leader can be as biased toward building and hiring as a vendor is toward selling.

### Step 6: Cost drivers and reversibility

Do not invent figures. For each surviving option, list the cost drivers from `references/methodology.md` section "Cost drivers by option" and mark which ones the leader has numbers for. State explicitly that maintenance and operation, not initial build, dominate the lifetime cost of anything built, and that ramp time, not salary, dominates the first-year cost of anything hired.

For each option, describe the exit at six and eighteen months: what it costs to stop, what knowledge or code leaves with it, and what has to be true for the exit to be clean. An option with a cheap exit deserves credit when uncertainty is high; an expensive exit deserves credit only when the leader is confident in the requirement.

### Step 7: Recommend, and say what would change your mind

Choose the recommended model per component and, if the components differ, the hybrid that combines them. State the two strongest alternatives and why they lost. Write the transition strategy (how the organization moves from today to the recommended model, including who owns knowledge transfer) and the conditions under which the recommendation would change (for example, "if hiring takes longer than ninety days, switch component B to augmentation with a twelve-month cap").

### Step 8: Write the memo

Fill `assets/output-template.md`. Lead with the recommendation per component and the reasoning in plain language. The alternatives and trade-offs follow; the leader should see that the losing options were taken seriously.

When the leader arrived with a preferred option, give it a short named section in prose that says why it is tempting and why that is or is not enough. That paragraph is the one they will repeat in the meeting; do not bury it in a table row.

Keep the dimension table to the dimensions that were actually rated. List the Unknown ones in a single line under "information still needed" rather than as empty rows. The memo is the deliverable: do not narrate the method or name the steps.

## Evidence rules

Label every claim **FACT** (supplied or verifiable), **INFERENCE** (reasoned, reasoning shown), **ASSUMPTION** (needed to proceed), or **UNKNOWN**. Never invent salaries, day rates, license prices, hiring durations, or vendor claims. Market benchmarks may be cited as context with attribution, never as this organization's numbers. If a number is essential, name it as information still needed and say who can provide it.

## Human decision boundaries

Hiring, terminating, or changing the terms of any person's engagement; signing or ending vendor contracts; and budget commitments are decisions for the leader. The memo presents options, consequences, and the information needed; it does not make those decisions or draft the communications for them.

## Gotchas

- Treating the request as one decision. Decompose first; the differentiating and commodity parts want different answers.
- Assuming building is cheap because engineers are already on payroll. Their time has an opportunity cost, and the built system has a maintenance cost that lasts as long as the system does.
- Hiring permanent staff for a temporary spike, or engaging a partner for a permanent core capability. Match duration to option.
- Assuming an external partner removes the need for internal management. Every external option needs an internal owner with time to direct, review, and receive knowledge.
- Letting fear of lock-in kill a good buy. Every option locks something in, including building; the question is switching cost versus the unique value gained.
- Recommending a fixed-scope partner when the requirement is still uncertain. Fixed scope on an uncertain requirement produces the wrong thing on time.
- Presenting the recommendation without its expiry conditions. Sourcing decisions are revisited when the demand or the market changes; say when.
- Letting the sixteen-dimension table crowd out the argument. The table is evidence; the recommendation and the rebuttal of the option the leader brought are the memo.
