# Evaluation results

Development review, 2026-09-16. These results are evidence about the recorded cases, not a claim that the skills consistently outperform a strong model or are validated in real organizations.

The later [Agentic Project Estimation evaluation](evaluation/2026-09-16-estimation/README.md) and [Idea Validation evaluation](evaluation/2026-09-18-idea-validation/README.md) are recorded separately. The three-skill results below remain unchanged.

## What ran

The initial suite contained 28 scenarios (AI 9, health 9, sourcing 10) and 60 trigger queries (20 per skill). All 28 scenarios were executed with the revised workflows. Six were also executed with the original skills and without explicitly loading a skill. Response generators did not receive assertions or expected outputs. A fresh grader saw randomly named copies of the 18 comparison outputs, their prompts and their assertions, without configuration labels.

Each configuration used a separate Codex desktop subagent with no parent conversation history. Cases within each configuration shared that agent's context; they were not six independently reset sessions. Agents inherited the same parent model setting. The interface did not expose an exact model build, sampling parameters, per-run tokens or timings. Host skill descriptions may still have been visible to the baseline; “without skill” means instructed not to load skill bodies, not a proven metadata-free environment. Full tool traces are not retained. These limitations prevent exact replication and strong causal claims.

The main comparison is a development set: the revised methodology contains worked examples related to some cases. The original skill baseline is commit `8b2cdfe`; instruction contents and hashes for the revised run are retained in [revision inputs](evaluation/2026-09-16/revision-inputs.json). Later independent held-out cases are recorded separately; they were not used to tune the skills.

## Six-case comparison

Raw grades from the frozen comparison contract, including a 700-word check:

| Case | Revised | Original | No explicit skill | Words: revised / original / baseline |
|---|---:|---:|---:|---:|
| AI: claims triage | 12/13 | 11/13 | 9/13 | 626 / 1015 / 562 |
| AI: contaminated bank-change test | 6/6 | 3/6 | 4/6 | 623 / 731 / 376 |
| Health: portal artifacts | 11/14 | 11/14 | 11/14 | 761 / 1428 / 850 |
| Health: thin but positive evidence | 4/4 | 3/4 | 4/4 | 476 / 323 / 142 |
| Sourcing: payouts | 10/11 | 9/11 | 9/11 | 678 / 1593 / 655 |
| Sourcing: specialist review | 4/4 | 2/4 | 4/4 | 629 / 776 / 211 |

[Exact outputs](evaluation/2026-09-16/README.md), [raw grades](evaluation/2026-09-16/comparison-grading.json), [frozen assertions](evaluation/2026-09-16/comparison-rubric.json) and [rubric corrections](evaluation/2026-09-16/rubric-review.md) are retained. Counts are not equally weighted measures of decision usefulness. No significance test or variance estimate is justified by these single trials.

### What changed and what failed

- The old health output explicitly said “Amber only because none of it has been independently verified.” The revised output separates provisional Green from low confidence. The no-skill baseline already avoided that mistake.
- The revised AI bank-change answer covers final-state and permission verification, evaluation leakage, independent judging and ineffective review. All arms reject rollout; the difference is the completeness of the evidence plan, not the headline recommendation.
- The old portal answer inferred historical scope inflow from snapshot fields. The revised answer names those limits and computes the five scope-added rows correctly. This remains development evidence because the method includes the fixture example.
- The old sourcing answers explicitly use the arbitrary two-condition external-help rule. Revised and baseline answers both recommend a specialist where appropriate. The baseline is considerably more concise on that simple question.
- Revised output totals were lower than original totals, but higher than the baseline. The first revised portal memo was 761 words and failed the length check. A focused trim instruction produced a 694-word rerun without losing the decisive findings. A grader still noted that calling the revised date “plausible” is weakly supported; the memo does not establish a forecast.
- A further proportionality change removed the implicit 400-word minimum. Narrow-question reruns are retained in `rerun/`; they reduce padding without changing the recommendation. These are targeted development reruns, not a fresh full-suite benchmark.
- Some raw failures reflect weak assertions: demanding literal labels, several do-not-change items, or boilerplate reserving decisions to humans. Current fixtures check the substantive safeguard instead. Old grades remain unchanged; revised wording was not used to inflate the comparison scores.

## Additional development coverage

The remaining 22 cases test deterministic reconciliation, vague executive pressure, pilot expansion, time leakage, denied data use, net review burden, contradictory status, historical evidence, injected vendor instructions, technical debt, sourcing bias, common-horizon costs, short projects with durable demand, no-op choices and outside expertise on core systems.

[AI and health grades](evaluation/2026-09-16/additional-grading.json) record 64/66 assertions passed across 14 outputs. Two failures were narrow: the reconciliation memo did not explicitly rate error cost as high, and the mobile-project memo requested integrated demos without explicitly prioritizing the riskiest features. Grading ambiguity is recorded; neither was silently converted into a pass. See [sourcing and portal rerun grades](evaluation/2026-09-16/sourcing-additional-grading.json) for the remaining cases and the partner exit-condition gap. That file records 49/50 checks across eight sourcing outputs plus the portal rerun (35/36 for sourcing and 14/14 for the rerun).

## Independent held-out check

After the skills were frozen, a separate fresh agent wrote three new cases without reading the skills, existing fixtures or outputs. Fresh response agents ran the same prompts with and without explicitly loaded skills; a separate blinded grader applied the four prewritten assertions per case. No skill was tuned afterward. Exact prompts, outputs, grades and instruction hashes are in the [artifact index](evaluation/2026-09-16/README.md).

| Held-out decision | Revised | No explicit skill | Words: revised / baseline |
|---|---:|---:|---:|
| Warranty assistant economics and biased demo | 3/4 | 4/4 | 560 / 635 |
| Reconciliation cutover with count/value mismatch | 4/4 | 4/4 | 659 / 599 |
| Sample routing with capacity and handover constraints | 4/4 | 4/4 | 654 / 729 |

**No held-out advantage was demonstrated.** The revised AI answer omitted the explicit $4,800 monthly recurring net value, although its correct payback and annual calculations imply it; this narrow failure is retained with the grader's ambiguity note. The baseline AI answer separately blurred capacity redeployment with cash savings; this concern is recorded even though its assertions passed. Both configurations handled the project and sourcing decisions well. Three single trials cannot establish parity, superiority or reliability.

Across all batches there are 49 retained responses: 40 development/comparison responses, three targeted reruns and six held-out responses. Narrow reruns reduced the health answer from 476 to 242 words and the specialist answer from 629 to 264 words, preserving the recommendation. These length reductions do not themselves prove better decision usefulness.

## What is not measured

Automatic triggering, full installation compatibility, repeated-run stability, cross-model performance, and usefulness in real leadership decisions remain unmeasured. The 60 trigger queries were checked as fixtures and reviewed for routing intent; no observed activation rate is claimed. Previous zero-activation reports cannot distinguish broken detection from actual routing failure without a positive control.

The first implementation reported strong Claude comparison results but kept no raw outputs or exact model identity in the repository. Those numbers have been retired as unverifiable historical claims; the original document remains in Git history. No new evaluation inherits its performance or compatibility claims.

## Reproduce and extend

Use the recorded prompts and matching fixtures from the repository root. Start fresh contexts for each case/configuration, pin the model/settings and skill revision, and conceal grading criteria from response generators. Compare the same inputs with the skill, previous revision and no skill; retain actual outputs and traces. Grade independently with evidence and a human reader, including arithmetic and concision. Repeat before reporting variability. [CONTRIBUTING.md](../CONTRIBUTING.md) describes the protocol and actual activation testing.

Structural verification is separate: `scripts/validate_skills.py --require-reference` plus validator regression tests. CI does not call an AI model or claim that parsed fixture JSON means the skill passed its scenarios.
