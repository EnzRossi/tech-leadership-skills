# Sources and attribution

Reviewed 2026-09-16. These sources inform the method; they do not validate its effectiveness or establish facts about a user's initiative.

| Source | Contribution and limit |
|---|---|
| [NIST AI RMF and Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework), NIST, 2023/2024 | Risk and lifecycle governance, including human/system interaction. Voluntary risk guidance, not a legal classification or certification. |
| [User Needs + Defining Success](https://pair.withgoogle.com/chapter/user-needs/), Google PAIR | User value and alternatives to AI; informs problem-first screening. |
| [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml), Martin Zinkevich, Google | Start with metrics and simple baselines; test surrounding infrastructure. Does not prescribe a universal preference for rules over learned systems. |
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), Anthropic, 2024 | Distinguish predefined workflows from model-directed agents; choose complexity to fit the task. |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), Anthropic, 2026 | Trials, outcome/state verification, grader types and transcript inspection. Informs evaluation of the whole workflow. |
| [Data Readiness Levels](https://inverseprobability.com/publications/data-readiness-levels.html), Neil Lawrence, 2017 | Accessibility, faithfulness and task appropriateness. A conceptual readiness framework, not evidence that historical data is usable. |
| [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html), Sculley et al., 2015 | Data dependencies, feedback loops and system maintenance beyond model code. Does not quantify this initiative's costs. |

## EnzRossi contribution

The investment-stage gates, concise evaluation-contract format, separation of readiness from missing evidence, and linking the next commitment to a discriminating experiment are this repository's synthesis. Baselines, held-out testing, human adjudication and risk governance are established practices; EnzRossi does not claim to have invented them. Production fitness still requires task-specific engineering and human review.
