# Idea Validation revision review

2026-09-18. Baseline commit: `09d79e5`, created on `codex/improve-idea-validation` before editing. The original evaluation remains unchanged in [its own directory](../2026-09-18-idea-validation/README.md).

## Assessment and research

The original skill has a useful foundation: internal/external routing, alternatives before custom builds, buyer and geography checks, AI feasibility, evidence attribution and explicit verdicts. Its earlier evaluation honestly records weak concision and overconfident inference. The main methodological gaps were a fixed demand-evidence ladder, commercial commitment criteria applied to internal tools, binary experiment outcomes, and insufficient distinction between missing evidence and negative evidence.

The revision qualifies letters, reservations and pilots by authority, terms and follow-through; distinguishes initial use from repeat value; adds internal outcome/adoption criteria; and selects a test for the most consequential weak assumption. The experiment card specifies eligible participants, measurement denominators, observation window, resource cap and pass/fail/inconclusive actions. It also covers two-sided marketplaces, nonbuyer interviews and participant trust without turning the core skill into a generic business textbook.

Primary research and its limits are recorded in [sources](../../../skills/idea-validation/references/sources.md). In particular, Strategyzer informs hypothesis prioritization and experiment design; GOV.UK informs interviews and outcome measurement; Amplitude informs retention at natural usage intervals; Microsoft informs experiment validity. These are practitioner frameworks, not proof that the resulting skill works. [Agent Skills authoring guidance](https://agentskills.io/skill-creation/best-practices) informed conditional reference loading and focusing instructions on observed failures.

The revision also narrows routing language, shortens the memo template, makes numerical cost claims require rates and quantities, and avoids treating a market ceiling as observed demand. The worked example no longer states an imagined acquisition channel as fact.

## Evaluation design

Five development fixtures were added, bringing the skill to 12 scenarios and 24 trigger queries. Three new scenarios ran with the revised skill, the committed original skill, and no explicit skill: conditional demand/retention, a justified internal release, and invalid exposure/measurement. Each of the nine responses used a separate fresh-context Codex subagent, inherited the same parent model/settings, and received the same prompt. Assertions and expected outputs were hidden from response generators. Each prompt required supplied facts only and no web research, so these tests do not assess browsing quality.

A separate fresh-context grader received randomly lettered copies, frozen assertions and programmatic whitespace word counts. It did not receive the configuration map or skill bodies. The body-count rule includes Markdown headings and excludes an explicit appendix; none of these outputs used an appendix. Critical failures and unsupported claims are recorded separately from pass counts. The exact outputs, frozen criteria, grades, anonymization map and instruction hashes are retained alongside this README. Word limits were part of the skill contract but not the unaided prompt; this makes concision grades asymmetric. The [grader critique](grader-comparison.md) also flags the literal denominator-recall assertion as stricter than decision usefulness requires. Neither issue was corrected retroactively to change scores.

The model family was GPT-6 as identified by the parent environment. Exact model build, sampling settings, tool traces, token counts and durations were not exposed/retained; absent metrics are null, not estimated. Host skill metadata may remain visible in fresh agents, so “no explicit skill” is not a proven metadata-free baseline. One trial per case/configuration cannot establish variance or causal superiority. These prompts were authored alongside the changes and are not held-out data.

## Results

| Case | Revised / original / no explicit skill | Body words: revised / original / no explicit skill |
|---|---|---|
| Conditional commitment and repeat value | 6/6 · 5/6 · 5/6 | 335 · 513 · 554 |
| Internal bounded release | 6/6 · 6/6 · 6/6 | 297 · 307 · 245 |
| Invalid exposure and broken booking | 5/6 · 5/6 · 5/6 | 314 · 308 · 159 |

The revised arm passed 17/18 assertions; the original and unaided arms each passed 16/18. All three reached defensible headline decisions. On conditional demand, the original proposed three buyers without explaining why that threshold was enough; the unaided response omitted an explicit inconclusive branch. All arms handled internal evidence appropriately, so that case demonstrates no incremental advantage.

Both skill versions exceeded the narrow answer's 300-word ceiling. The unaided answer omitted the 400-visit count but correctly explained the invalid test; that strict assertion failure is not a wrong business recommendation. The grader recorded no critical failures. It separately noted that the original/unaided demand answers amplified “founder-assisted” into required or substantial help without evidence. See exact grades for qualifications. Counts are not equally weighted quality scores and are too small to establish superiority.

The final narrow rerun produced 278 words. Its independent, explicitly unblinded grading passed 6/6 and is retained separately from this comparison.

## Follow-up and limits

The first revised narrow answer exceeded its frozen 300-word limit. The final skill adds drafting headroom and a tool-assisted count/trim instruction. A targeted fresh-context rerun is retained separately; it does not replace the failed comparison output. Two editorial clarifications also make market-sizing units explicit and keep an empty competitor search from implying rejection. The three-arm comparison hashes identify the earlier revision; final hashes identify the delivered skill. `comparison-skill.txt` preserves the exact core instructions used in that comparison; its other skill files match the delivered revision.

Only the narrow case was rerun after those final changes. The new stop-offer and marketplace scenarios are unrun coverage fixtures, and the seven existing scenarios were not rerun in this pass. Automatic activation, actual customer research, cross-model behavior, repeated trials and human decision usefulness remain unmeasured. Human review is still needed; the generated local viewer includes full outputs and grading evidence.

## Reproduce

Run each prompt in `cases.json` in a fresh context for each configuration, with identical tool permissions and model settings; conceal its assertions until grading. Obtain the original skill from `09d79e5`. Use `skill-inputs.json` to identify comparison instruction hashes and the final hash manifest for the delivered revision. Preserve failed outputs and label targeted reruns separately. Use the repository's [contribution protocol](../../../CONTRIBUTING.md) for subsequent held-out and activation tests.
