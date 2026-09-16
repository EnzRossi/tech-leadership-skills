# Landscape: existing leadership and management skill collections

Research date: September 2026. Star counts are approximate GitHub API figures on that date. This document records what already exists so that this repository fills gaps instead of duplicating work. No wording, frameworks, or templates were taken from the repositories below; they were reviewed as market research only.

## What we reviewed

| Repository | Focus | Scale | License | Evals / CI | Status |
|---|---|---|---|---|---|
| [manager-dot-dev/manager-skills](https://github.com/manager-dot-dev/manager-skills) | Engineering-manager craft (1:1s, feedback, hiring, reviews, roadmaps, team health) | 25 skills | MIT | None | Idle since May 2026 |
| [stephenrogan/leadership-skills](https://github.com/stephenrogan/leadership-skills) | Founder/operator "manager OS", decision memos, premortems, agent-workforce ops | 32 skills | MIT | Structural smoke evals only | Active mid-2026 |
| [dazuck/operator-skills](https://github.com/dazuck/operator-skills) | Startup founder operations (coaching, writeups, hiring, contracts, financials) | 21 skills | MIT | None | Idle since June 2026 |
| [shwetank/bettersense](https://github.com/shwetank/bettersense) | AI PM / EM / TPM craft, engineering health, tech strategy docs, reflection utilities | 54 skills + agents | CC BY-SA 4.0 | Real routing eval + LLM rubrics | Active mid-2026 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Mega-collection; includes C-level advisor personas and project-management calculators | ~388 skills | MIT | Partial | Active |
| [wdzhwsh4067/startup-cto-skills](https://github.com/wdzhwsh4067/startup-cto-skills) | Startup CTO basics, including a short build-vs-buy skill | 8 skills | MIT | None | Single commit |
| [aapersh/strategy-skills-for-claude](https://github.com/aapersh/strategy-skills-for-claude) | Consulting-style corporate strategy (business cases, prioritization, war gaming) | 21 skills | None declared | None | Active |
| [Onemedia-Consulting/ai-prioritization-framework](https://github.com/Onemedia-Consulting/ai-prioritization-framework) | AI use-case scoring for marketing and operations teams | 1 skill | MIT | None | Active |
| [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) | Product management (the best-engineered collection we found: CI validation, trigger fixtures, judged evals, worked examples) | 68 skills | Apache-2.0 | Yes | Active |

We also checked the large "awesome agent skills" lists. None had a category for technology executives.

## Topics that are already heavily covered

If you need any of the following, existing collections already do a reasonable job and we do not plan to compete on them:

- One-on-ones, feedback conversations, performance reviews, calibration, promotion cases
- Hiring loops and candidate screening for full-time employees
- Delegation, meeting design, managing up, executive updates
- Generic decision memos and premortems
- OKRs, prioritization frameworks, org design
- Product management artifacts (PRDs, roadmaps, discovery)

## Where the gaps are

Three decision types that technology leaders face constantly were thin or absent everywhere we looked.

**Deciding whether an AI initiative deserves investment.** Existing material is either product-management craft (how to build well once you have decided) or a generic use-case scoring grid aimed at marketing teams. No skill we found starts from the business problem, asks for evidence such as data samples and baseline metrics, checks whether the outcome can even be evaluated, distinguishes "prototype" from "controlled pilot" from "production", or is willing to conclude that deterministic software is the better answer.

**Diagnosing the real health of a software project from its artifacts.** Several collections offer team-health questionnaires or calculators that need pre-shaped JSON. None reads what a leader actually has, such as a Jira or Linear export, milestone plans, meeting notes, and a risk register, and triangulates them into a diagnosis with cited evidence, explicit uncertainty, and a separation of fact from inference.

**Choosing between build, buy, hire, contractors, staff augmentation, and an engineering partner as one decision.** Build-versus-buy appears in two thin places. Hiring skills assume full-time employees. Nothing treats external engineering capacity as a first-class option with its own costs, knowledge-retention risks, and exit conditions, and nothing is written by people who deliver that capacity and are willing to say when it is the wrong choice.

## Quality problems we saw and want to avoid

- Essay-length SKILL.md files that read as knowledge dumps rather than workflows
- Persona skills ("CTO advisor") that try to cover everything and therefore trigger on everything
- Template-stamped catalogs where every skill shares one skeleton and little domain judgment
- No inputs contract: skills rarely say what artifacts to ask for or what to do when evidence is missing
- No output template or worked example
- Eval theatre: structural checks presented as behavioral evaluation, or no evals at all
- Copyleft or missing licenses that block use inside companies
- Abandonment within months of the first commit

## How this repository differentiates

1. **Decision workflows, not advice.** Each skill encodes a repeatable procedure with an intake step, an evidence discipline, a decision structure, and a concrete output artifact.
2. **Evidence-first.** Every skill separates fact, inference, assumption, and unknown, and refuses to invent numbers or status that the inputs do not support.
3. **Written by practitioners.** EnzRossi is a software engineering company. We focus on delivery, engineering organizations, AI adoption, and sourcing, where we have daily experience, and we stay out of law, finance, HR, and medicine.
4. **Deliberate neutrality where we have an incentive.** The sourcing skill declares EnzRossi's commercial interest and is built to recommend against outside help when outside help is not the best answer.
5. **Real evaluation.** Each skill ships with scenario evals, trigger tests, and recorded with-skill versus without-skill comparisons, and the repository is validated in CI against the Agent Skills specification.
6. **Permissive license.** Apache-2.0, so companies can adopt, modify, and redistribute internally without friction.
