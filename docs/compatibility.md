# Compatibility

The skills in this repository follow the [Agent Skills specification](https://agentskills.io/specification) and use only the standard frontmatter fields (`name`, `description`, `license`, `metadata`). They contain no client-specific extensions, no scripts that require a particular runtime, and no tools beyond reading files. Any client that implements the specification should load them.

We distinguish between *specification compliance*, which we verify automatically, and *tested compatibility*, which means someone has actually installed the skill in a client and confirmed it activates and follows its workflow.

## Specification compliance

Verified on every commit by CI using the official reference validator, [`skills-ref`](https://github.com/agentskills/agentskills/tree/main/skills-ref), plus this repository's own convention checks. See [.github/workflows/validate-skills.yml](../.github/workflows/validate-skills.yml).

## Tested clients

| Client | Status | What was tested | Install location |
|---|---|---|---|
| Claude Code | Tested (September 2026) | Scenario evals executed by Claude Code subagents loading and following each skill, graded against the baseline; see [eval-results.md](eval-results.md). Trigger rates were not successfully measured in the CLI version available to us. | `~/.claude/skills/` or `.claude/skills/` ([docs](https://code.claude.com/docs/en/skills)) |

## Format-compatible, not yet tested by us

These clients document support for the Agent Skills standard. The skills should work, but we have not run them there. If you do, please open an issue or pull request with the client, version, and what you observed, and we will move it to the table above.

| Client | Install location | Documentation |
|---|---|---|
| OpenAI Codex | `.agents/skills/` in the project or repo root, or `~/.agents/skills/` | [Codex skills](https://developers.openai.com/codex/skills/) |
| GitHub Copilot (CLI, coding agent) | `.github/skills/`, `.claude/skills/`, `.agents/skills/`; personal: `~/.copilot/skills/`, `~/.agents/skills/` | [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| VS Code (Copilot) | Same as Copilot, plus `~/.claude/skills/` | [Agent skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills) |
| Cursor | `.agents/skills/`, `.cursor/skills/`, `~/.agents/skills/`, `~/.cursor/skills/` | [Cursor skills](https://cursor.com/docs/context/skills) |
| Gemini CLI | `.gemini/skills/`, `.agents/skills/`, `~/.gemini/skills/`, `~/.agents/skills/` | [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) |
| Claude.ai and the Claude API | Upload as a skill | [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) |

The full list of clients that declare support is maintained at [agentskills.io/clients](https://agentskills.io/clients). The `.agents/skills/` directory is scanned by most of them, which makes it the most portable install location.

## Known differences between clients

- Clients differ in how aggressively they activate skills from the description alone. Our trigger tests were run in Claude Code; other clients may activate more or less readily.
- Some clients render or truncate long responses differently. The output templates are plain markdown with no client-specific formatting.
- The evals in `evals/evals.json` follow the agentskills.io format. Anthropic's `skill-creator` uses the field name `expectations` where the specification uses `assertions`; the content is otherwise identical.

## Reporting results

Open an issue titled "Compatibility: <client> <version>" with the skill name, the prompt you used, whether the skill activated, and whether the output followed the template. Transcripts help.
