# Sources

Sources that informed the method in `methodology.md`, with what each contributed. The method is EnzRossi's synthesis; named frameworks belong to their authors.

## Governance and risk frameworks

- **[AI Risk Management Framework 1.0 (NIST AI 100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)** — U.S. National Institute of Standards and Technology, 2023. The Map function as the point where a go/no-go decision is made before building; documenting intended purpose, business value, risk tolerance, and the cost of expected errors; explicitly weighing non-AI alternatives; the requirement to be able to supersede or deactivate a system. Our "wrong tool" test, cost-of-being-wrong classification, and decommissioning checklist follow this structure.
- **[Artificial Intelligence Risk Management Framework: Generative AI Profile (NIST AI 600-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)** — NIST, 2024. Generative-AI-specific risks including confabulation, human-AI configuration, information security, intellectual property, and value-chain integration; decommissioning actions. Informs the risk-and-compliance rubric.
- **[Microsoft Responsible AI Standard, v2](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf)** — Microsoft, 2022. Fit-for-purpose as a requirement with evidence, defining predictable failures including false positives and false negatives up front, human oversight requirements, and discontinuing systems that evidence shows are not fit. Informs the feasibility rubric and error-asymmetry guidance.
- **[EU Artificial Intelligence Act, high-level summary](https://artificialintelligenceact.eu/high-level-summary/)** and **[Article 14, Human oversight](https://artificialintelligenceact.eu/article/14/)** — summary by the Future of Life Institute. Risk tiers and the high-risk categories (employment, credit, education, biometrics, critical infrastructure, and others); oversight requirements including the ability to override and stop. Informs the regulated-categories rule.
- **[ISO/IEC 42001:2023](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-42001)** — International Organization for Standardization, described here via Microsoft's compliance documentation. AI management systems with impact assessment and lifecycle controls.

## When to use AI, and in what shape

- **[People + AI Guidebook: User Needs + Defining Success](https://pair.withgoogle.com/chapter/user-needs/)** and **[Errors + Graceful Failure](https://pair.withgoogle.com/chapter/errors-failing/)** — Google PAIR. The situations in which AI is not the right approach (predictability as the core value, static information, high error cost, required transparency, speed to market, users who do not want automation); automate versus augment; weighing false positives against false negatives. Our Section 1 poor-fit list and Section 2 classification draw directly on these concepts.
- **[Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml)** — Martin Zinkevich, Google. Launching without machine learning when a heuristic suffices; designing metrics before models; keeping the first model simple.
- **[Building effective agents](https://www.anthropic.com/research/building-effective-agents)** — Anthropic, 2024. Finding the simplest solution; the distinction between workflows with predefined paths and agents that direct their own process; when agents are justified. Basis for the "shape of the AI" classification.
- **[A practical guide to building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)** — OpenAI, 2025. Criteria for when an agent is warranted versus a deterministic solution; human-intervention triggers for high-risk actions.
- **[AI strategy (Cloud Adoption Framework)](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai/strategy)** and **[AI workloads on Azure (Well-Architected Framework)](https://learn.microsoft.com/en-us/azure/well-architected/ai/get-started)** — Microsoft. Starting from business problems and translating them into use cases; generative versus deterministic choice; the observation that prebuilt or managed options are usually preferable to building; cost drivers including compute, model decay, and skills.

## Evaluation readiness

- **[AI in the Enterprise](https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf)** — OpenAI, 2025. Starting with evaluations before production, illustrated by enterprise adopters.
- **[Evaluating model performance](https://developers.openai.com/api/docs/guides/evals)** — OpenAI. Evaluations defined against test inputs with ground truth.
- **[Define your success criteria](https://platform.claude.com/docs/en/docs/build-with-claude/define-success)** and **[Create strong empirical evaluations](https://platform.claude.com/docs/en/docs/build-with-claude/develop-tests)** — Anthropic. Specific, measurable, multidimensional success criteria; building evaluations before prompt engineering.
- **[Testing and evaluating AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/test)** — Microsoft. Human-validated golden datasets and metric thresholds as go/no-go gates; drift monitoring.
- **[Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)** — Hamel Husain, 2024. Failed AI products share the absence of a robust evaluation system; levels of evaluation.
- **[Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/)** — Eugene Yan, 2023. Evaluation as the first pattern; limits of automatic metrics.

## Data readiness

- **[Data Readiness Levels](https://inverseprobability.com/publications/data-readiness-levels.html)** — Neil Lawrence, 2017. The three bands of accessibility, faithfulness, and appropriateness for a specific task. Our data-readiness rubric uses this three-layer structure.
- **[DAMA-DMBOK](https://www.dama.org/cpages/body-of-knowledge)** — DAMA International. Data quality as a management discipline with standard dimensions.

## Why AI initiatives fail, and what value looks like

- **[The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf)** — Ryseff, De Bruhl, Newberry, RAND Corporation, 2024. Interview-based study identifying leadership misunderstanding of the problem, missing data, technology-first framing, inadequate infrastructure, and problems too hard for AI as the leading causes. The ordering of our workflow follows these findings.
- **[The GenAI Divide: State of AI in Business 2025](https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf)** — MIT NANDA, 2025 (mirror of the report). Most organizations report no measurable return; a small share of pilots reach production; externally partnered deployments reached production more often than internal builds; systems that do not learn or integrate stall. Findings are self-reported and the report notes confounders; used as context, not as evidence about any specific initiative.
- **[Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept by End of 2025](https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025)** — Gartner, 2024. Abandonment after proof of concept attributed to data quality, risk controls, cost, and unclear value. Motivates staged recommendations with stop rules.
- **[Where's the Value in AI?](https://www.bcg.com/publications/2024/wheres-value-in-ai)** — Boston Consulting Group, 2024. A minority of companies generate value beyond proof of concept; the emphasis on people and process over algorithms; focusing on few high-value opportunities.
- **[AI at Work 2025: Momentum Builds, but Gaps Remain](https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain)** — Boston Consulting Group, 2025. Training and visible leadership support as drivers of adoption. Informs the user-desirability and operational-readiness rubrics.
- **[Identifying and scaling AI use cases](https://cdn.openai.com/business-guides-and-resources/identifying-and-scaling-ai-use-cases.pdf)** — OpenAI, 2025. Opportunity signals; impact-versus-effort prioritization; deprioritizing custom builds where a reliable tool exists.

## Sourcing and lifecycle cost

- **[Buy, boost, or build? Choose your path to generative AI](https://mitsloan.mit.edu/ideas-made-to-matter/buy-boost-or-build-choose-your-path-to-generative-ai)** — van der Meulen and Wixom, MIT Sloan / MIT CISR. Trade-offs among buying, augmenting a vendor model with proprietary data, and building; prioritizing on strategic alignment and measurable value.
- **[Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)** — Sculley et al., NeurIPS 2015. The ongoing costs of learning systems: data dependencies, feedback loops, glue code, monitoring for a changing world.
- **[LLMflation](https://a16z.com/llmflation-llm-inference-cost/)** — Guido Appenzeller, a16z, 2024. Rapid decline in inference cost for constant capability, which is why the lifecycle checklist emphasizes evaluation, monitoring, and review costs over unit inference price.

## Human-AI interaction

- **[Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/)** — Microsoft HAX Toolkit (Amershi et al., CHI 2019). Making clear what a system can do and how well, supporting correction, scoping services when uncertain. Informs the augment-versus-automate discussion.

## EnzRossi methodology

The ordering of the workflow (problem, right-tool test, classification, eight dimensions, ordered decision rules, experiment design, approval points), the eight-dimension rubric wording, the three-level cost-of-being-wrong scale and its regulated-category override, the eight recommendation outcomes and the rules that select among them, and the experiment design table are EnzRossi's synthesis from delivery practice and the sources above.
