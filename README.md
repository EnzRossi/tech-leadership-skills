# EnzRossi Tech Leadership Skills

**Better AI workflows for the people leading software.**

Open-source Agent Skills for technology leaders making software, delivery, resourcing, and AI decisions.

[![Validate skills](https://github.com/EnzRossi/tech-leadership-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/EnzRossi/tech-leadership-skills/actions/workflows/validate-skills.yml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-spec%20compliant-green.svg)](https://agentskills.io/specification)

## What this is

A set of [Agent Skills](https://agentskills.io) that give AI coding agents and assistants a repeatable way to work through the decisions technology leaders face: whether an AI initiative deserves money, whether a project is really on track, and how to source an engineering capability.

Each skill is a decision workflow, not a prompt. It tells the agent what evidence to ask for, how to read it, what to do when it is missing, how to structure the analysis, and what artifact to produce. The result is a memo or assessment a CTO, VP of Engineering, product leader, or founder can take into a meeting.

## Why it exists

Most AI leadership content is either generic advice or a scoring template. Neither survives contact with a real decision, where the inputs are incomplete, the status report is optimistic, and the person asking already has an answer in mind.

We wanted skills that behave like a good advisor: start from the business problem, insist on evidence, separate what is known from what is inferred, say "do not proceed" when that is the answer, and leave the decision with the human. We also wanted to measure whether the skill actually changes the output compared with the same model working alone.

EnzRossi is a software engineering company. We built these skills for the conversations we have with clients and for our own leadership team. They are useful whether or not you ever work with us; that independence is the point.

## Who it is for

- CTOs, VPs of Engineering, Engineering Directors, and Heads of Platform
- Product leaders working with engineering on investment and delivery decisions
- Founders and CEOs of software companies making sourcing and AI bets
- Engineering managers preparing steering, board, or executive updates
- Practitioners who build agents and want examples of evidence-disciplined, evaluated skills

## What Agent Skills are

An Agent Skill is a folder with a `SKILL.md` file: YAML frontmatter that tells the agent what the skill does and when to use it, followed by instructions the agent loads only when the skill is relevant. Supporting material lives in `references/`, `assets/`, and `scripts/`. The format is an open standard published at [agentskills.io](https://agentskills.io/specification) and supported by Claude Code, Codex, GitHub Copilot, Cursor, Gemini CLI, and a growing list of other tools.

Skills load progressively: the agent sees only the name and description until it decides the skill applies, then reads `SKILL.md`, then loads reference files only when the workflow tells it to. That keeps context small and lets a skill carry deep methodology without paying for it on every turn.

## What makes these skills different

- **Decision-first.** Each skill begins with the decision at stake and the business problem, not with the technology or the option the requester arrived with.
- **Evidence discipline.** Every output labels claims as fact, inference, assumption, or unknown. Numbers, dates, and statuses are never invented. "Unknown" is a legitimate rating.
- **Willing to say no.** Each skill has a path to "do not use AI", "do not intervene", or "do not hire the outside firm", and the evals check that it takes those paths when the evidence points there.
- **Neutral where we have an interest.** The sourcing skill declares EnzRossi's commercial interest and contains an explicit rule that counteracts it.
- **Measured.** Every skill ships with scenario evals, trigger tests, and a recorded comparison against the same model without the skill, including where the skill made things worse. See [docs/eval-results.md](docs/eval-results.md).
- **Attributed.** Each skill has a `references/sources.md` naming the research and frameworks behind it. Our own synthesis is labeled as ours.

## Available skills

| Skill | Decision it supports | Output |
|---|---|---|
| [ai-initiative-evaluator](skills/ai-initiative-evaluator/) | Does this AI initiative deserve investment, and what should happen next? Starts from the business problem and tests whether deterministic software would do. Recommends one of: do not use AI, research, prototype, controlled pilot, production, buy, build, or external partner. | Evaluation memo with recommendation, eight-dimension assessment, risks, unknowns, next experiment with stop rule, success criteria, approval points |
| [software-project-health-review](skills/software-project-health-review/) | Is this project really on track? Reads tracker exports, plans, status reports, and meeting notes; diagnoses rather than summarizes. | Health assessment with overall rating and confidence, seventeen-dimension ratings with cited evidence, root causes versus hypotheses, leadership decisions, seven-day actions, and what not to change |
| [build-buy-hire-augment](skills/build-buy-hire-augment/) | How should we obtain this capability: build, buy, hire, contractors, staff augmentation, engineering partner, consultant, hybrid, or wait? | Sourcing memo per component with knockouts, alternatives, trade-offs, cost drivers, transition and exit strategy, and conditions that would change the recommendation |

## Examples

**Project health.** A CTO pastes a Jira export, three months of green steering decks, and a Slack digest and asks how healthy the portal rebuild really is. The skill builds an evidence ledger, finds the same vendor risk carried through three reports with an unchanged owner, scope added by Sales while the status stayed green, a design decision stalled for weeks, and operational tasks nobody owns. It rates the project Red with Medium confidence, lists the unknowns, and gives five actions for the week, plus the things an anxious leader should not change.

**AI initiative.** Finance wants generative AI to reconcile 40,000 daily settlement transactions against the ledger after seeing a demo. The skill restates the problem, notes that structured matching has exact answers and that the task's value is auditability, sets the cost of being wrong as high, and recommends a rules-based or off-the-shelf reconciliation approach with AI confined, if at all, to suggesting resolutions for ambiguous exceptions under review.

**Sourcing.** A fintech's CTO built the pricing engine that customers buy the company for, has no time to rebuild it, and has a fixed-price offer from a familiar services firm. The skill identifies the engine as core, ongoing, and knowledge-critical, rules out a fixed-scope partner as the sole option, and recommends hiring and building internally with the CTO's knowledge transferred, allowing a bounded role for the firm only with an end date and a receiving owner.

The scenario prompts and expected behavior for each skill are in its `evals/evals.json`.

## Installation

Skills are plain folders. Copy the ones you want into the directory your agent scans, or clone the whole repository and symlink.

**Claude Code**

```bash
git clone https://github.com/EnzRossi/tech-leadership-skills.git && cp -r tech-leadership-skills/skills/* ~/.claude/skills/
```

For a single project, copy into `.claude/skills/` inside the repository instead.

**Codex, Cursor, Gemini CLI, and other clients that scan `.agents/skills`**

```bash
git clone https://github.com/EnzRossi/tech-leadership-skills.git && mkdir -p ~/.agents/skills && cp -r tech-leadership-skills/skills/* ~/.agents/skills/
```

**GitHub Copilot**

Copy into `.github/skills/` in a repository, or `~/.copilot/skills/` for personal use.

Each client's official documentation is linked in [docs/compatibility.md](docs/compatibility.md), along with what we have actually tested.

## Compatibility

The skills follow the Agent Skills specification and use only the standard frontmatter fields, so they should load in any compliant client. We only claim compatibility where we have tested it. See [docs/compatibility.md](docs/compatibility.md) for the current list and how to report results from other tools.

## Evaluation philosophy

A skill has to earn its place by changing what the agent does. For each skill we:

1. Write scenario evals that sound like real requests, including an incomplete-information case and a case where the right answer is not to proceed.
2. Run each scenario with the skill and without it, in clean contexts, and grade both against the same assertions.
3. Run trigger tests: prompts that should activate the skill and near-miss prompts that should not.
4. Record the results in [docs/eval-results.md](docs/eval-results.md) and change the skill only in ways that generalize beyond the eval set.

We do not optimize skills to pass their own tests. Where the model without the skill already does well on an assertion, that assertion tells us to remove instructions rather than add them.

## Contributing

We welcome new skills and improvements inside our area of competence: software delivery, engineering organizations, AI adoption, project health, technical initiatives, resourcing, vendors, product and engineering collaboration, and executive technology decisions. We do not accept skills that attempt legal, financial, HR-policy, marketing, or medical expertise.

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/principles.md](docs/principles.md) first. Start from `templates/skill-template/`. Validate with:

```bash
python scripts/validate_skills.py
```

## Repository layout

```
skills/                      the skills (one folder each, spec-compliant)
templates/skill-template/    annotated starting point for a new skill
docs/principles.md           the rules every skill is reviewed against
docs/landscape.md            what other collections cover and how this one differs
docs/compatibility.md        tested clients and how to report others
docs/eval-results.md         recorded with-skill versus without-skill comparisons
scripts/validate_skills.py   repository conventions check; wraps the official skills-ref validator
.github/workflows/           CI running the same validation on every pull request
```

## License

Apache License 2.0. See [LICENSE](LICENSE). We chose Apache-2.0 so that companies can adopt and adapt these skills internally without legal friction, and because its explicit patent grant matters to corporate counsel.

## About EnzRossi

[EnzRossi](https://enzrossi.com) is a software engineering company. We build software and provide engineering teams for organizations that need to deliver. These skills encode how we think about the decisions our clients bring us. If they are useful to you and you never call us, they have done their job.
