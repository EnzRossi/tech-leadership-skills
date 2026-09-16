# Compatibility

These are instruction-only skills using standard `name`, `description`, `license` and `metadata` fields. References and templates are local Markdown. Reading supplied CSVs may benefit from the host's normal data tools; no connector or external service is required by the skills.

## What has actually been checked

| Check | Status |
|---|---|
| Packaging/frontmatter | Local convention checks and pinned official `skills-ref`; see CI and review report for executed results |
| Explicit workflow use | Revised skills exercised through Codex desktop subagents in this review; saved outputs in [evaluation results](eval-results.md) |
| Installation, automatic discovery and activation | Not measured for the revised skills |
| Cross-client output parity | Not measured |

The initial version reported Claude Code runs without retained transcripts or exact model/client versions. Those claims are historical reports, not verified compatibility evidence. A subagent explicitly reading SKILL.md is not an installation/discovery test.

## Documented installation paths

These are supported client locations according to the linked official documentation; they are not claims of successful tests of this repository.

| Client | Project / personal | Official documentation |
|---|---|---|
| Codex | `.agents/skills/` / `~/.agents/skills/` | [Codex skills](https://developers.openai.com/codex/skills/) |
| Claude Code | `.claude/skills/` / `~/.claude/skills/` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| GitHub Copilot | `.github/skills/` / `~/.copilot/skills/` (host-dependent) | [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |

Other clients may implement the [Agent Skills specification](https://agentskills.io/specification). Check their current documentation rather than assuming identical loading, file access, permissions or invocation behavior.

## Report a compatibility test

Record client/version, model, installation path, skill revision, exact prompt and observed skill-file load or invocation trace. Include one positive and one near-miss negative request. Note whether reference files were read and whether the output followed the decision procedure. Do not include private user data.

Scenario fixtures use `assertions`, following Agent Skills evaluation guidance. Some versions of Anthropic skill-creator expect `expectations`; adapt at the runner boundary and record the version. Neither fixture parsing nor predicting which description matches a query measures actual activation.
