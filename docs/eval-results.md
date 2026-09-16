# Evaluation results

This file records what we measured when building the first three skills. It exists so that readers can judge for themselves whether the skills add value over a strong model working alone, and so that contributors have a baseline to beat.

Method summary. For each skill we took two scenarios from `evals/evals.json` (the normal case and the "do not proceed" case), ran each in a clean context twice, once with the skill loaded and once with no skill, using the same model (Claude, September 2026, via Claude Code subagents). An independent grader agent then scored both outputs against the same assertions, with the burden of proof on the assertion, and wrote a qualitative comparison. Trigger tests were run separately with `claude -p` against the skill descriptions. Eval workspaces are not committed; the summary below is what we kept.

## Iteration 1: with skill versus without skill

| Skill | Scenario | With skill | Without skill | Output size (with / without) |
|---|---|---|---|---|
| ai-initiative-evaluator | Claims triage (normal case) | 12/12 | 9/12 | 32k / 13k chars |
| ai-initiative-evaluator | Settlement reconciliation (do not use AI) | 7/7 | 5/7 | 24k / 13k chars |
| software-project-health-review | Portal rebuild with Jira export and notes | 12/12 | 9/12 | 29k / 15k chars |
| software-project-health-review | Two-week slip, CEO wants contractors | 6/6 | 5/6 | 19k / 10k chars |
| build-buy-hire-augment | Multi-country payouts in five months | 10/10 | 7/10 | 29k / 13k chars |
| build-buy-hire-augment | Core pricing engine, fixed-price offer | 7/7 | 6/7 | 27k / 13k chars |

Token use with the skill was roughly 1.3 to 1.5 times the baseline, and wall-clock time roughly 1.5 to 2.8 times, driven mostly by the longer output.

### What the skills changed

The graders' comparisons converged on the same findings across all six pairs.

**Where the skill added value**

- **No invented numbers.** In five of six pairs the baseline fabricated figures a leader could repeat in a meeting and be wrong about: team cost ranges, licence prices, auto-match percentages, contractor and salary ranges, FX spreads, "20 to 50 percent change orders", "three to five months to hire". The with-skill outputs contained none, and labeled their own estimates as assumptions.
- **Correct arithmetic against the artifacts.** On the portal review, every count and story-point total in the with-skill output re-derived correctly from the CSV. The baseline miscounted twice and placed an unsupported judgment inside its evidence table.
- **Unknowns the baseline missed.** On the claims-triage case the skill asked whether the raw inbound emails and attachments are actually retained and linked to claim records, without which four years of "labeled history" is unusable. The baseline assumed the data existed. It also grounded accuracy targets in an inter-rater agreement test rather than asserted percentages.
- **Neutrality applied mechanically.** On both sourcing cases the skill checked its four conditions for recommending external help, set an end date, named the receiving owner, specified knowledge transfer, and on the payments case barred external engineers from production banking data. The baseline recommended contractors with "time-box it to the program" and never constrained data access.
- **Structure a leader can execute.** The skill produced a stated confidence level, at most five owned actions for the week, and a "do not change" list. The baseline produced nine actions plus five asks with implicit ownership and no confidence statement, and its "what not to do" list was mostly further demands for change.
- **Decisions reserved for the leader.** The baseline issued directives ("open the search this month"); the skill presented hiring and contract decisions as the leader's.

**Where the skill made things worse**

- **Length and template rigidity.** Every with-skill output was roughly twice as long. Dimension tables were printed in full even when most rows were Unknown; on the one-paragraph slip question, nine of seventeen rows said Unknown and carried no information. A CTO would skim these.
- **Buried arguments.** On the pricing-engine case the decisive rebuttal ("an attractive price and codebase familiarity are not sufficient reasons") sat in a table row; the baseline gave it a crisp section a leader would quote.
- **Deferred decisiveness.** The with-skill memos sometimes left thresholds as open questions for the sponsor where the baseline proposed a concrete target. Not inventing numbers is right; refusing to propose any is a different failure.
- **Meta-commentary.** One memo explained which decision rules had fired. That belongs in the transcript, not the deliverable.

**Non-discriminating assertions.** Between five and nine assertions per scenario passed in both configurations: a strong model reaches the right headline recommendation on all six scenarios unaided. The skills' value is in the evidence discipline, the unknowns surfaced, the neutrality mechanism, and the executable structure, not in reaching a different conclusion. We kept those assertions because they guard against regression, but they do not measure the skill.

### Changes made after iteration 1

Applied to all three skills, as generalizable rules rather than fixes for the specific scenarios:

1. A proportionality rule in the output step: match length to the evidence supplied; collapse Unknown or not-applicable sections to a single line; produce a short form when the leader supplied only their own account.
2. A prohibition on narrating the method or naming decision rules in the deliverable.
3. An instruction to propose concrete thresholds and targets as recommendations for confirmation rather than leaving them as open questions.
4. For the sourcing skill, a named prose section on the option the leader arrived with.
5. For the project-health skill, a phrasing rule for the "nothing negative, but unverified" case so an Amber rating reads as a request for evidence rather than an alarm.
6. Three assertions were reworded to be less ambiguous or to check the thing that actually separated the runs (counts matching the CSV).

## Iteration 2: spot check of the proportionality change

We reran the one-paragraph slip scenario with the revised project-health skill. The output fell from 19.4k to 9.7k characters, opened with "Nothing in your account indicates trouble; Amber only because none of it has been verified", rated only the six dimensions the account supports and listed the rest as not assessable, kept the five owned actions and the "do not change" list, and still recommended against the consultant and contractors. The change generalizes: it is a rule about matching output to evidence, not about this scenario.

## Trigger tests

Each skill ships eighteen trigger queries (eight that should activate it, ten near misses that should not) in `evals/trigger-evals.json`. We attempted to run them with the `skill-creator` trigger harness through `claude -p`. The results were inconclusive: the harness detected zero activations on every query, positive and negative alike, across two runs and two model configurations, which indicates the detection mechanism did not work in the installed CLI version rather than that the descriptions failed. We are recording this as **not measured** rather than reporting the numbers. The descriptions were written to the agentskills.io guidance (intent-focused, explicit near-miss exclusions, under 1024 characters) and were reviewed by hand against every trigger query; measured trigger rates are the first thing we want from contributors running a current Claude Code, Codex, or Copilot.

## How to reproduce

Anthropic's `skill-creator` skill in Claude Code automates the loop: it runs each eval prompt with and without the skill in subagents, grades against the assertions, and aggregates a benchmark. The agentskills.io [evaluation guide](https://agentskills.io/skill-creation/evaluating-skills) describes the same workflow for other agents. Trigger tests use the [description optimization guide](https://agentskills.io/skill-creation/optimizing-descriptions) format, which is what `evals/trigger-evals.json` follows.

Note for anyone rerunning the trigger tests through `claude -p`: check that the CLI version supports the model you pass and that the harness actually observes a `Skill` tool call on at least one positive query before trusting a full run. A run that reports zero activations everywhere is a broken harness, not a result.
