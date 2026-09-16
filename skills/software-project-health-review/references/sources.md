# Sources

The sources that informed the method in `methodology.md`. One line each on what concept was taken. Nothing is reproduced at length; the method is EnzRossi's synthesis unless stated otherwise.

## Team and project health frameworks

- **[Team Health Monitor](https://www.atlassian.com/team-playbook/health-monitor)** — Atlassian Team Playbook. The idea of rating a fixed set of health attributes with a coarse scale and discussing the weakest ones; the legacy project-team variant's attributes (full-time owner, shared understanding, value and metrics, managed dependencies) informed our Purpose and Plan clusters. Atlassian's attribute names and play mechanics are theirs; ours differ deliberately.
- **[Project Poster](https://www.atlassian.com/team-playbook/plays/project-poster)**, **[Trade-offs](https://www.atlassian.com/team-playbook/plays/trade-offs)**, **[Pre-mortem](https://www.atlassian.com/team-playbook/plays/pre-mortem)**, **[DACI](https://www.atlassian.com/team-playbook/plays/daci)** — Atlassian Team Playbook. Separating what is known from what must be found out; making constraint flexibility explicit; naming a single approver for decisions.
- **[Understand team effectiveness (Project Aristotle)](https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness)** — Google re:Work. Psychological safety, dependability, and structure and clarity as the team dynamics that predict effectiveness; the finding that candor about problems is a health attribute in its own right.

## Delivery metrics and their limits

- **[DORA's four keys](https://dora.dev/guides/dora-metrics-four-keys/)** and the **[2024](https://dora.dev/research/2024/dora-report/)** and **[2025](https://dora.dev/research/2025/dora-report/)** DORA reports — DORA, Google Cloud. Delivery performance measures capability, not project progress; the 2024 finding that unstable organizational priorities predict burnout; the 2025 framing of AI as an amplifier of existing team strengths and dysfunctions.
- **[The SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124)** — Forsgren, Storey, Maddila, Zimmermann, Houck, Butler, ACM Queue, 2021. Productivity cannot be captured by a single activity metric, which is why this skill refuses to read velocity as progress.
- **[DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/)** — DX, 2024. Further support for multi-dimensional measurement.

## Project risk, estimation, and reporting bias

- **[Why Your IT Project May Be Riskier Than You Think](https://hbr.org/2011/09/why-your-it-project-may-be-riskier-than-you-think)** — Flyvbjerg and Budzier, Harvard Business Review, 2011 ([working paper](https://arxiv.org/abs/1304.0265)). In 1,471 IT projects the average overrun was moderate but one in six was a black swan; project risk lives in the tail, which is why the method looks for early tail signals rather than averages.
- **[From Nobel Prize to Project Management: Getting Risks Right](https://arxiv.org/abs/1302.3642)** — Flyvbjerg, Project Management Journal, 2006. Reference class forecasting as a corrective for optimism bias and strategic misrepresentation.
- **[The Cone of Uncertainty](https://www.construx.com/wp-content/uploads/2019/02/CxWhitePaper_ConeOfUncertainty.pdf)** — Steve McConnell, Construx (from *Software Estimation*, 2006, building on Boehm). Estimates narrow only when decisions remove variability, which is why deferred decisions matter for schedule.
- **[CHAOS Report: Beyond Infinity](https://www.standishgroup.com/products/copy-of-chaos-report-beyond-infinity-digital-version)** — The Standish Group, 2020. Decision latency identified as a leading cause of project failure. Standish's methodology is proprietary and its success rates are contested; we use only the qualitative finding.
- **["Why didn't somebody tell me?": climate, information asymmetry, and bad news about troubled projects](https://dl.acm.org/doi/10.1145/1007965.1007971)** — Keil, Smith, Pawlowski, Jin, ACM SIGMIS Database, 2004. The reluctance to pass bad news upward and the information asymmetry it creates.
- **[The effects of optimistic and pessimistic biasing on software project status reporting](https://www.sciencedirect.com/science/article/abs/pii/S0378720606001145)** — Snow, Keil, Wallace, Information & Management, 2007. Status reports on high-risk projects are frequently biased, and far more often optimistic than pessimistic. This is the empirical basis for treating a status rating as a claim rather than a fact.
- **[Ten Troublesome PM Ideas](https://www.pmi.org/learning/library/ten-troublesome-pm-ideas-combat-6715)** — Project Management Institute. The "watermelon project" pattern: green outside, red inside.
- **[Performing a Project Premortem](https://hbr.org/2007/09/performing-a-project-premortem)** — Gary Klein, Harvard Business Review, 2007, drawing on Mitchell, Russo and Pennington (1989). Prospective hindsight as a way to surface risks the team already senses.
- **The Mythical Man-Month** — Frederick P. Brooks Jr., 1975. Adding people to a late project makes it later, because of ramp-up and communication cost. The basis for the "do not change" guidance on headcount.

## Dependencies and critical path

- **[Critical Path Method calculations](https://www.pmi.org/learning/library/critical-path-method-calculations-scheduling-8040)** — Project Management Institute. Critical path and float.
- **[Critical Chain Project Management](https://www.pmi.org/learning/library/critical-chain-project-management-theory-7118)** — Project Management Institute, on Goldratt's *Critical Chain* (1997). Resource constraints and buffers instead of per-task padding.

## Outcomes, definition of done, readiness

- **[The Scrum Guide](https://scrumguides.org/scrum-guide.html)** — Schwaber and Sutherland, 2020. Definition of Done as a formal statement, which underlies the "closed without evidence" signal.
- **[Product vs. Feature Teams](https://www.svpg.com/product-vs-feature-teams/)** — Marty Cagan, SVPG, 2019, and **Outcomes Over Output** — Josh Seiden, 2019. Outcome as a change in behavior rather than a delivered thing; the basis for the outcome-clarity rubric.
- **[Working Backwards: the PR/FAQ process](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)** — Bryar and Carr. Writing the result before the plan.
- **[Reliable Product Launches at Scale](https://sre.google/sre-book/reliable-product-launches/)** and **[Evolving the SRE Engagement Model](https://sre.google/sre-book/evolving-sre-engagement-model/)** — Google, *Site Reliability Engineering*. Launch checklists and production readiness reviews; the operational-readiness rubric.

## Decision rights and latency

- **[RAPID decision making](https://www.bain.com/insights/rapid-decision-making/)** — Bain & Company. A single decider per decision.
- **[Amazon 2015 shareholder letter](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm)** and **[2016 letter](https://www.sec.gov/Archives/edgar/data/1018724/000119312517120198/d373368dex991.htm)** — Jeff Bezos. One-way versus two-way door decisions; deciding with roughly seventy percent of the information. Used to separate decisions leadership must make from actions the team can take.

## EnzRossi methodology

The seventeen-dimension structure in five clusters, the signal catalog, the Unknown rating and its rules, the two-source rule for root causes, the overall-health and confidence decision rules, and the "what should not change" list are EnzRossi's synthesis from delivery practice and the sources above.
