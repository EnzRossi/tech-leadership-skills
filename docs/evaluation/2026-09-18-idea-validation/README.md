# Idea Validation: development evaluation

2026-09-18. This evaluates reasoning on fictional idea scenarios, not whether the verdicts would have been right for a real business. The skill adds 7 scenarios and 20 trigger fixtures (10 positive, 10 negative); automatic activation was not tested.

## Iteration 1: paired comparison

Three prompts ran with and without explicit skill loading, as separate Claude Code subagents with fresh context and web search available. One blinded grader per case received anonymised memos, the prompt and the frozen assertions, without configuration labels, and was also asked to record word count, unsupported claims and overstated certainty.

| Case | With skill | Without skill | Words with / without | Finding |
|---|---:|---:|---:|---|
| Internal feature-flag tool versus licensed and open-source alternatives | 8/8 | 7/8 | 793 / 1,812 | Both say do not build as proposed; the baseline invents parity and maintenance timelines and asks twelve questions |
| AI contract summariser, "no competitor", global | 10/10 | 6/10 | 1,010 / 2,642 | Both find the competitor claim false; the baseline reasons about price from unsourced usage and churn figures and never states why the idea could work |
| Ambulance scheduling with six signed paid pilots | 6/8 | 5/8 | 1,017 / 2,007 | Both say pursue; both exceed the word budget; the baseline invents build-cost figures and omits the regulatory boundary |

Two further with-skill responses (vague restaurant-inventory idea, 10/10 at 864 words; CEO asking for a slanted memo, 8/8 at 1,055 words) have no baseline. Graders judged the with-skill memo more decision-useful in all three paired cases, on evidence discipline and concision. These are single trials on cases written in the same session as the skill; they do not establish a general advantage.

## What the graders found wrong with the skill outputs

- Every with-skill memo exceeded the 300–700 word target, mostly through inline citation lists.
- Listings were treated as demand: "a crowded field proves people want this" and "the market shows people do pay".
- Inferences about channels, error cost, inference cost and maintenance were stated as fact without a label.
- One memo illustrated market size with a hypothetical operator count; one placed a refusal preamble before the verdict.

Four instructions were revised in response: source lists and tables go in an appendix and the body budget is explicit; a product page shows existence and price, not demand; no hypothetical counts, and unlabelled inferences carry no numbers; a refusal to slant a memo goes inside the verdict paragraph. After iteration 2 the sentence "a crowded market means demand exists" was softened to "suggests buyers exist for something in this space" because a rerun repeated it as an overstatement.

## Iteration 2: single reruns with the revised skill

| Case | Revised skill | Iteration 1 | Words total / body | Finding |
|---|---:|---:|---:|---|
| AI contract summariser | 9/10 | 10/10 | 1,223 / 867 | Sources moved to an appendix as instructed; body still over budget; the one failure is a less explicit model-evaluation plan |
| Ambulance scheduling | 5/8 | 6/8 | 1,023 / 876 | Market ceiling now computed from a cited association member count rather than a hypothetical, which the assertion wording still counts as a market figure; sector compliance rules asserted rather than flagged for a specialist; length |

The reruns did not demonstrate improvement. The appendix instruction was followed and the "proves demand" language disappeared, but bodies remained about 870 words and grades moved within single-trial variation. The compliance-boundary miss in case 5 is a real failure the skill's methodology already forbids; it is retained rather than explained away. The market-ceiling failure exposes an ambiguity between the assertion ("no market size is invented") and the skill ("size bottom-up only from supplied or cited counts"); the assertion text was left unchanged so iteration 1 and 2 grades stay comparable.

## Run conditions and limitations

- Subagents inherited the parent session model as reported by the host (Claude Fable 5.1); sampling settings and full tool traces were not retained. Token counts and durations per run are in `benchmark.json`.
- No-skill means instructed not to read any skill files; the baseline agents could still see the repository path, and one baseline memo used the publisher's company name, which was not in the prompt.
- Web research results differ between runs, so competitor findings are not reproducible facts; graders could not verify cited pages and recorded them as cited, not confirmed.
- Cases, assertions and skill were written in the same session. There is no held-out set, no repeated trials and no human technology-leader review yet.
- Assertion 3 of case 1 was split into two after grading on the grader's critique; iteration 1 was graded against the original wording in `cases.json`.

Case outputs are `case-N-with_skill.md`, `case-N-without_skill.md` and `case-N-with_skill-revised.md`, each with a matching `-grading.json`. `blind-map.json` records the anonymisation; `skill-inputs.json` records the hashes of the final skill files.

## Reproduce

Give each response agent only a prompt from [cases.json](cases.json), plus the skill folder for the with-skill arm, in a fresh context with the same tools. Keep assertions hidden until grading and grade blind. Add held-out cases written without reading the skill, run repeated trials, and have a technology leader judge decision usefulness before claiming more than these development checks show.
