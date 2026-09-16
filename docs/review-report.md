# Repository review — 2026-09-16

The three use cases and project name remain worth keeping. The first version was not ready to support its credibility claims: several rules encoded false certainty or bias, and the published evaluation results could not be audited. The revised repository is ready for final human review, with explicit limits on what its tests demonstrate.

## What was good

- Relevant decisions with realistic artifacts, a limited three-skill scope and an appropriate technology-leadership audience.
- Problem-first AI screening, separate supporting references, explicit uncertainty and willingness to recommend against the proposed investment.
- Sourcing decomposition, attention to retained knowledge and declared commercial interest.
- Scenario and trigger fixtures, a fictional tracker dataset, permissive license and simple CI.

## Main problems found

1. **Unsupported certainty:** AI was said to weaken auditability universally; human review supposedly tolerated lower accuracy; small fixed sample sizes stood in for an evaluation design. Permission failures could still lead to a real-data prototype.
2. **False project alarms and causes:** missing evidence forced Amber, document counts controlled confidence, and two sources could supposedly establish a root cause. Tracker snapshots were read as history. The worked example invented counts inconsistent with the fixture; the eval said four scope additions where five exist.
3. **Biased sourcing logic:** an internal tie-break and two-condition rule replaced commercial bias with a different bias. Short duration and core IP became automatic exclusions. Ramp time and maintenance were asserted to dominate costs without context.
4. **Output burden:** large dimension tables crowded out the recommendation. Repeated requirements across skill, methodology and template amplified length.
5. **Evidence claims:** old evaluation scores lacked retained outputs, exact model details and traces. Attempted trigger tests were described inconsistently, and zero activations were assumed to prove a harness problem. Landscape claims overstated novelty.
6. **Validation gaps:** a hand-written parser was not real YAML parsing; malformed JSON could crash checks; string booleans passed as trigger labels; referenced fixture paths could escape a skill; official validation could be silently skipped.

## Changes made

- Kept all three names and folder contracts; revised their methods to add decision-changing checks and remove unsupported rules.
- AI now separates technology, interaction and orchestration; defines held-out evaluation, label validity, costly-error slices, reviewer capacity, tool-state verification and stage-specific approval evidence.
- Project health now distinguishes a breached original plan from the current commitment, supports Not assessable, separates confidence from health, and checks what each artifact can actually establish. Seventeen printed dimensions became five diagnostic areas.
- Sourcing separates solution from delivery and ownership, applies symmetric evidence standards, compares costs on a common basis, and makes handover capability testable. Sixteen dimensions remain considerations only where they affect the decision.
- Shortened templates, descriptions, README, attribution and compatibility claims. Removed mirrored survey claims, forecasts, redundant sources and categorical legal/commercial assertions. Retained sources each support a specific methodological choice; synthesis is not presented as original research.
- Expanded behavioral and near-miss fixtures, retained generated comparison outputs, added validation regression tests, pinned the official validator revision and made CI fail if it is unavailable.

## Skills removed or significantly changed

None removed or renamed. All three were substantially revised because their use cases are useful but the decision rules needed correction. No future skills were implemented.

## Evaluation results

See [evaluation results](eval-results.md) for the authoritative run record, retained outputs, grading evidence and limitations. The old published scores are not reused as verified evidence. Structural checks and model behavior are reported separately; actual automatic triggering remains unmeasured. The pinned official validator, repository link/fixture checks, eight validator regression tests and `git diff --check` passed locally. CI configuration was updated but no remote CI run is claimed.

The central development finding is already clear: the old health rule creates an Amber warning solely from unverified evidence; the revised procedure avoids that error. Revised outputs are shorter than the originals, but the no-skill baseline performs well on several cases. A revised portal memo exceeded its length target, prompting a focused trim rule and rerun. These are development findings, not a general superiority claim. Across 28 scenarios, three targeted reruns and three independent held-out cases, 49 responses are retained. The held-out comparison scored 11/12 for the revised skills and 12/12 for the baseline, with a narrow subtotal omission and a separate baseline cash-savings concern. It demonstrates no overall incremental advantage; the repository now says so.

## Remaining concerns

- Human CTO/engineering review of the memos and thresholds is still needed. Synthetic cases cannot establish whether the artifacts improve real meetings or decisions.
- Explicitly loading skills in agents is not an installation/discovery test. Run actual positive and near-miss activation traces in each claimed client before marking it tested.
- Comparisons used one inherited model configuration, small samples and shared context within each arm. Exact runtime model build, timing/tokens and complete traces were not supplied by the subagent interface. Repeated fresh-context trials and untouched cases are needed for stronger claims.
- Publisher identity, repository URL, copyright ownership and any claim of EnzRossi field experience need maintainer confirmation. The README no longer claims these workflows were field-validated with clients.
- Remote source pages were reviewed selectively for the retained concepts; the local link validator does not validate remote availability or heading anchors. External content and client behavior can change.

## Recommended next steps

Before publishing: review the retained outputs and failures; have at least two technology leaders use each workflow on permitted real artifacts; verify installation/activation in one named client; rerun important cases in fresh contexts with a recorded exact model; confirm ownership and repository metadata. Publish as an initial reviewed release with its evaluation limitations, not as a proven advisory system.

After launch: collect cases where the recommendation was wrong or unusable, record the missing evidence and outcome, and use those failures for regression tests. Add skills only when these three show repeat use.

## Ranked future skills

Ranking is editorial judgment, not market validation. It balances recurring usefulness, distinctiveness, EnzRossi's delivery credibility, likely adoption, ability to demonstrate AI expertise and educational value.

| Rank | Candidate | Why consider it / boundary |
|---|---|---|
| 1 | AI pilot evidence audit | Turn actual pilot logs, rubrics and results into an expansion/hold decision. Strong AI demonstration and teachable failure cases; narrower than the investment evaluator, with deeper artifact inspection. |
| 2 | Delivery recovery option planner | Take a diagnosed constraint and compare scope/date/sequence options with dependencies and capacity. Useful follow-through on health review; must not invent recovery forecasts. |
| 3 | Vendor handover readiness | Test whether the receiving team can change, deploy and recover what a supplier delivered. Distinctive and credible for a services firm; stay neutral about whether to retain the vendor. |
| 4 | Engineering capacity constraint review | Distinguish demand, review bottlenecks, incident load and skills from a presumed headcount deficit. High recurrence and educational value; avoid individual productivity scoring. |
| 5 | AI workflow autonomy boundary review | Use task traces and tool permissions to decide where automation can act, must verify or must escalate. Strong AI engineering signal; requires adversarial execution evidence. |
| 6 | Technical decision reversal review | Revisit an ADR using changed constraints, switching costs and evidence that would justify migration. More differentiated than a generic architecture decision template. |
| 7 | Product/engineering commitment reconciliation | Reconcile sales promises, product acceptance and engineering dependencies into explicit trade-offs and owners. Broad adoption potential; distinguish from meeting summaries. |
| 8 | Executive decision memo audit | Check a technical memo for unsupported claims, absent alternatives and unclear asks, then test it with a fresh reader. Useful and educational but crowded; implement only with technology-specific failure cases. |
