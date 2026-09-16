# Contributing

Improve a real technology decision workflow. Read [principles](docs/principles.md) and [landscape](docs/landscape.md) first. A specific failure case is more valuable than another generic leadership framework.

## Scope and structure

We accept software delivery, AI adoption, project health, sourcing and adjacent technology leadership decisions. Generic executive personas and legal, financial, HR-policy, marketing or medical advisory skills are out of scope.

Copy `templates/skill-template/` for a new skill. Each skill needs:

- `SKILL.md`: standard frontmatter, narrow trigger description, focused procedure and reference-loading instructions.
- `references/methodology.md` and `references/sources.md`: decision criteria, limitations, worked example and attribution.
- `assets/output-template.md`: concise decision artifact with optional depth.
- `evals/evals.json`: realistic scenarios and behavioral assertions.
- `evals/trigger-evals.json`: positive requests and nearby requests that should not activate it.

The validator checks minimum fixture structure, not whether the tests are good. Keep frontmatter within the [format specification](https://agentskills.io/specification). Descriptions should identify decision intent and nearby exclusions, not just keywords. Keep SKILL.md below 500 lines; shorter is usually better.

## Evaluate the change

Use [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills) or a recorded version of [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md). Our fixtures use `assertions`; adapt to `expectations` if your runner requires it.

1. Add cases for normal, messy, missing and contradictory evidence, preferred-answer pressure, a legitimate proceed decision, and a stop/wait decision. Include no-AI and no-external-provider outcomes where relevant, plus a positive outside-help case for sourcing neutrality.
2. Freeze prompts and grading criteria before running. Use separate fresh contexts for revised, previous and no-skill arms, with the same model/settings/tools and input data. Hide expected outputs and grades from response generators. Give all arms the same user task; do not make only one arm see the needed artifacts.
3. Grade behavior against evidence. A defensible alternative recommendation can pass; do not force the author's preferred option. Record serious invented facts, unsupported certainty and consequential boundary failures separately from counts of passing assertions. Check calculations and output length programmatically.
4. Inspect outputs with a technology leader. Where possible blind labels and randomize order. Repeated paired trials are needed to quantify variability. Keep a fresh held-out set; do not tune the description or workflow on it and still call it held-out.
5. Commit sanitized prompts, exact outputs, evidence-backed grades, revision/model/harness settings and limitations. Record missing token/time data as missing, not estimated. Update [eval-results.md](docs/eval-results.md); do not claim deployment readiness from a few development cases.

For activation tests, install the skill in the target client and observe the actual load/invocation trace. Validate instrumentation with an explicit-invocation positive control. Zero observed activations can be a harness failure **or** a real routing failure; investigate before assigning cause. Fixture validation and description-only classification do not measure triggering.

## Validate locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements-validation.txt
.venv/bin/python scripts/validate_skills.py --require-reference
.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
```

The official validator revision is pinned in `scripts/requirements-validation.txt`. Update deliberately after reviewing its changes. Local checks validate YAML, file references, fixture types and trigger coverage; CI uses the same commands. Neither invokes models. Remote source links require a separate review; local Markdown file destinations are checked automatically (heading anchors are not).

## Pull requests

Explain the decision failure, the changed behavior and validation. Include relevant results and remaining uncertainty, not just a pass-rate headline. Keep the change focused. Do not submit confidential client data or unsanitized transcripts. By contributing, you agree your contribution uses the repository's [Apache-2.0 license](LICENSE).
