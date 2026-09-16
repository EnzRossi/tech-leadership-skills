# Research and attribution

Reviewed 2026-09-16. Studies below concern different populations, tools, task boundaries and outcome measures. None supplies a universal multiplier for agentic project delivery. This skill is an editorial synthesis, not a claim that EnzRossi invented critical-path scheduling or empirically validated an estimation model.

## Productivity evidence

- [Cui et al., Effects of Generative AI on High-Skilled Work](https://doi.org/10.2139/ssrn.4945566): randomized field experiments across 4,867 developers reported a pooled 26.08% increase in completed tasks, with noisy individual experiments. This is coding-assistant evidence, not a 26% reduction in whole-project calendar time or a measurement of modern autonomous agent teams.
- [METR, early-2025 experienced open-source developer RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/): 16 developers and 246 tasks in familiar mature repositories; AI availability increased completion time by 19% in that setting. Do not generalize this into a current universal slowdown.
- [METR, February 2026 experiment update](https://metr.org/blog/2026-02-24-uplift-update/): newer raw results suggest speedup, but participant/task selection and measurement of concurrent agent work undermine a reliable magnitude estimate. Motivates recording human time and elapsed agent time separately.
- [METR, May 2026 technical-worker survey](https://metr.org/blog/2026-05-11-ai-usage-survey/): self-reported value-of-work changes among 349 technical workers. Useful context on adoption, not causal timing calibration. Self-reported counterfactuals are not observed savings.
- [DORA, State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/): emphasizes the organizational system and AI as an amplifier of existing strengths and weaknesses. Organizational findings cannot establish a causal speed factor for a specific team or justify company-size stereotypes.

## Agent workflow and assurance

- [OpenAI, Harness engineering, February 2026](https://openai.com/index/harness-engineering/): a first-party account of an agent-built internal product, describing investment in repository context, feedback and engineering constraints. Its estimated manual counterfactual is not a controlled 10× productivity benchmark. Use it to identify setup and feedback work, not to divide every estimate by ten.
- [Anthropic, Demystifying evals for AI agents, January 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): supports task-specific executable outcomes, stable environments and multiple forms of grading. Passing a generated test suite alone does not establish all acceptance requirements.
- [GitHub, About Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review): describes agentic review and limitations; asks users to validate feedback and supplement it with human review. Features, approval settings, coverage and pricing can change. Verify the actual environment rather than hard-code a product capability or price into the skill.

## Scheduling and ecosystem

- [US GAO, Schedule Assessment Guide, GAO-16-89G](https://www.gao.gov/products/gao-16-89g): source for dependency logic, resource availability, critical paths and schedule risk analysis. The skill uses those principles proportionally; it does not import a government-program planning process into a small software change.
- [ZhangHanDong/agent-estimation](https://github.com/ZhangHanDong/agent-estimation): an existing skill addresses human-time anchoring with tool-call rounds and wall-clock conversion. This is meaningful overlap. Our scope is a technology leader's accepted release across human capacity, agent execution, verification and organizational gates. We do not adopt its default minutes-per-round or risk coefficients; tool rounds vary by environment and do not measure calendar delivery on their own. No instructions were copied.

The intended contribution is the combination of direct agent-work calibration, explicit measurement boundaries, resource-constrained staffing scenarios, and consequence-based acceptance. Actual forecast accuracy needs prospective estimates compared with accepted releases; the repository's scenario checks cannot establish it.
