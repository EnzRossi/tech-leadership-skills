# Contributing

Thank you for helping technology leaders make better decisions. This guide explains what we accept, how a skill is structured, and how we check quality.

## What we are looking for

Skills that encode a repeatable decision workflow for people who lead software, delivery, engineering organizations, or AI initiatives. Good candidates share three traits:

1. A technology leader faces the decision repeatedly and it has real stakes.
2. A strong model would not reliably handle it well without structure, evidence discipline, or domain judgment.
3. The output is an artifact someone can take into a meeting.

Read [docs/principles.md](docs/principles.md) before you start. Check [docs/landscape.md](docs/landscape.md) so you do not rebuild something another collection already does well.

Out of scope: legal, financial, tax, HR-policy, marketing, and medical expertise; generic prompt collections; skills that only restate common knowledge.

## Skill structure

Every skill follows the [Agent Skills specification](https://agentskills.io/specification):

```
skills/<skill-name>/
  SKILL.md                    # required: frontmatter + workflow (under 500 lines)
  references/
    methodology.md            # the detailed method, loaded when the workflow says so
    sources.md                # required: attributed research behind the method
  assets/
    output-template.md        # the artifact the skill produces
  evals/
    evals.json                # required: >= 3 scenario evals with assertions
    trigger-evals.json        # required: >= 5 should-trigger and >= 5 should-not-trigger prompts
```

Start from `templates/skill-template/`, which contains annotated versions of each file.

### Frontmatter

Only the fields defined by the specification are allowed: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. The `name` must match the directory name, be lowercase, and use hyphens. The `description` is the routing mechanism: write it from the user's point of view, list the situations that should activate the skill, include near-miss situations that should not, and keep it under 1024 characters. See the [description guidance](https://agentskills.io/skill-creation/optimizing-descriptions).

### SKILL.md body

SKILL.md is the workflow and routing layer. Put the intake questions, the ordered steps, the evidence rules, the decision structure, and pointers to reference files there. Put the long methodology, research, and examples in `references/`. Tell the agent when to load each reference file.

Every instruction must change behavior. Before submitting, go through the file line by line and remove anything a capable model would do anyway.

### Sources

`references/sources.md` lists the primary and authoritative sources that informed the method, each with a link, the author or publisher, and one or two lines on what concept it contributed. Attribute named frameworks to their owners. Label EnzRossi's own synthesis as such. Do not paste long passages from sources.

## Evaluation

We do not merge skills on the strength of their prose. Each skill needs:

**Scenario evals** in `evals/evals.json` following the [agentskills.io eval format](https://agentskills.io/skill-creation/evaluating-skills): at least a normal case, an ambiguous or incomplete-information case, and a case where the right answer is to not proceed. Prompts should read like something a real CTO, VP of Engineering, product leader, or founder would type. Assertions describe expected behavior, not exact wording.

**Trigger evals** in `evals/trigger-evals.json`: an array of `{"query": "...", "should_trigger": true|false}`. Negative cases should be near misses that share vocabulary with the skill but need something else.

**With-skill versus without-skill comparison**: run the scenario evals both ways in clean contexts, and record what the skill changed in `docs/eval-results.md`. If the skill does not measurably improve the output, it is not ready.

Anthropic's `skill-creator` skill automates much of this loop in Claude Code, and the agentskills.io evaluation guide describes the same process for other agents.

## Validation

Run before opening a pull request:

```bash
pip install "git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref"
```

```bash
python scripts/validate_skills.py
```

The first command installs the official reference validator. The script runs it on every skill and then checks the repository's own conventions: required files, reference paths, eval JSON validity, and trigger-test coverage. CI runs the same checks on every pull request.

## Pull requests

- One skill or one focused improvement per pull request.
- Explain what decision the skill supports and why a model needs it.
- Include the eval results you observed.
- Keep the tone practical. No marketing language about EnzRossi or anyone else.

## License

By contributing you agree that your contribution is licensed under the Apache License 2.0, the same license as the repository. We chose Apache-2.0 because it is permissive enough for companies to adopt, adapt, and redistribute skills internally, and it carries an explicit patent grant, which matters to corporate legal teams more than the difference between MIT and Apache does to individuals.
