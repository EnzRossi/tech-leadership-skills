# Agentic Project Estimation: development evaluation

2026-09-16. This evaluates the reasoning in fictional planning scenarios, not the accuracy of real delivery forecasts. No real software project was built or timed. The new skill adds 12 scenarios and 20 trigger fixtures (10 positive, 10 negative); automatic activation was not tested.

## Paired comparison

Three prompts were executed with and without explicit skill loading. A separate grader received anonymized outputs, prompts and frozen assertions, without the skill or configuration labels. Both configurations got the same prompts and no grading criteria.

| Case | With skill | Without skill | Finding |
|---|---:|---:|---|
| Accepted slices and fixed access gate | 5/5 | 5/5 | Both derive day 8 for all team sizes and avoid double-counted verification |
| Startup payments deadline | 5/5 | 4/5 | Both reject day 10; skill output makes agent/human ownership explicit and avoids unsupported full-project durations |
| Small enterprise page | 5/5 | 5/5 | Both reject two weeks; skill uses 75–105 minutes from the supplied analogue and additional brand review |

The one failed baseline assertion combines agent/human separation with review ownership. Its threshold is debatable; the grader explicitly noted that a looser reading could pass it. The baseline's illustrative schedule inputs were labeled as judgment, so they were not graded as fabricated measurements. The enterprise scenario leaves some ambiguity about whether historical browser checks cover the requested mobile/keyboard checks; both stated interpretations were accepted. Do not interpret 15/15 versus 14/15 as a measured general advantage.

See [blind review](blind-review.md), [configuration mapping](blind-map.json), [paired benchmark](benchmark.json), and [frozen cases/rubric](cases.json). Case outputs and grading files are named `case-N-with_skill.md`, `case-N-without_skill.md` and corresponding `-grading.json` files in this directory. [Instruction snapshots and hashes](skill-inputs.json) identify what was tested.

## Additional coverage

Nine further with-skill responses cover vague scope, unsupported speedup claims, review bottlenecks, sparse historical data, urgency versus consequence, reuse, restricted tool access, parallel gates and AI-product acceptance. They passed 26/27 assertions. The remaining assertion requires execution traces to verify no upload occurred; it is unverified, not an observed violation. All text-assessable checks passed. There is no baseline comparison for these nine cases. See [additional grading review](additional-review.md) and retained `case-4` through `case-12` outputs and grades.

Across both sets, 15 responses were retained: 12 with skill and three without. These are development checks, not evidence of forecast accuracy. Keep the trace-dependent check visible and add tool traces in a future run rather than redefining it after seeing results.

## Run conditions and limitations

- One separate Codex subagent per response configuration, each starting without parent conversation history; cases within an arm share that agent's context. The additional coverage uses the same with-skill agent.
- No-skill means instructed not to load skill bodies. Host skill metadata may still have been visible. It is not a proven instruction-free baseline.
- Exact model build, sampling controls, per-case timing, tokens and full execution traces were not exposed. The standard skill-creator aggregator's default zero metrics were removed from the retained benchmark rather than presented as measured data. Pass-rate variation across different cases is not repeated-trial uncertainty.
- A workspace relocation raced with the first three with-skill output writes. That agent recreated its responses at the corrected location without reading the baseline or rubric. This storage recovery is not counted as a fresh independent trial; the discarded file contents were not retained.
- Cases and skill were designed in the same development session. There is no held-out comparison or repeated-run estimate of reliability. The grader's qualitative preferences are judgments, not independent project outcomes.

The skill was not revised to chase the one-point comparison difference. Before claiming forecast accuracy, collect prospective estimates and accepted-release dates with scope, team allocation, review/fix effort, tool versions and changed constraints preserved. Separate overruns caused by scope changes from estimation error. Test automatic activation and run independent cases across models before making broader performance claims.

## Reproduce

Give each response agent only a prompt from [cases.json](cases.json), plus the skill and linked methodology for the with-skill arm. Keep assertions hidden until grading. Use a fresh session per case where possible and record client/model settings. Use the same scope and quality bar in both arms. Grade final decisions and calculations, preserve failures, and distinguish behavioral checks from real-world forecast accuracy.
