# Principles

These principles govern every skill in this repository. Pull requests are reviewed against them.

## 1. A skill must earn its place

A skill exists to add knowledge, process, judgment, or structure that a strong model would not reliably produce on its own. For every instruction, ask: would a capable model already do this without being told? If yes, delete the instruction or make it specific enough that it changes behavior. Lines such as "communicate clearly" or "consider risks" fail this test and do not belong in a SKILL.md.

## 2. Start from the decision, not the technology

Technology leaders come to these skills with a decision to make: fund or stop, ship or hold, hire or contract. Every skill begins by naming the business problem and the decision at stake before any analysis of tools, models, or vendors. If a simpler solution than the one the user has in mind would serve the problem, the skill says so.

## 3. Evidence discipline

Skills work from what the user actually provides. Each output labels its claims as one of four kinds:

- **Fact**: directly supported by the supplied material, with a pointer to where.
- **Inference**: a reasoned conclusion from facts, with the reasoning shown.
- **Assumption**: something the analysis had to take as given because no evidence was available.
- **Unknown**: something that matters and cannot be resolved from the inputs.

Skills never invent numbers, dates, statuses, or costs. When a number would help and the inputs do not supply one, the skill names the number that is needed and how to get it.

## 4. Honest uncertainty over false precision

Scores and ratings appear only when they change a decision, and always with the assumptions that produced them. A skill states its confidence in its own conclusion and what would raise or lower it. A three-level rating with visible reasoning beats a two-decimal score with hidden reasoning.

## 5. Recommendations are specific and falsifiable

Every recommendation names a next action, who owns it, what evidence it will produce, and what result would change the recommendation. "Investigate further" is not a recommendation; "run a two-week labeling exercise on 200 historical tickets to measure whether agreement between reviewers exceeds 85 percent" is.

## 6. Human decision boundaries

These skills prepare decisions; humans make them. For employment, compensation, large financial commitments, legal matters, security and compliance, external commitments, customer promises, and irreversible actions, the skill produces analysis and options and stops. Boundaries are stated once, where they change the workflow, not sprinkled as disclaimers.

## 7. Neutrality where the author has an interest

EnzRossi sells software engineering and staff-augmentation services. Any skill that touches sourcing must recommend against external engineering help whenever that is the better answer, and must say so in plain language. The value of the repository depends on readers trusting that the recommendation was not written to win business.

## 8. Progressive disclosure

SKILL.md is the workflow and routing layer, kept well under 500 lines. Methodology, research, worked examples, and long checklists live in `references/`, loaded only when the workflow says to. Output templates live in `assets/`. Nothing is duplicated between layers.

## 9. Attribute what is not ours

When a skill uses a named framework, research finding, or model belonging to another organization or author, the skill and its `references/sources.md` say whose it is. EnzRossi's own methodology is labeled as such. Synthesis is encouraged; presenting others' work as our invention is not.

## 10. Measured, not assumed, value

Every skill ships with realistic scenario evals, trigger tests, and a recorded comparison of the same task performed with and without the skill. Changes to a skill should generalize beyond the eval set; a change that improves the evals but narrows the skill is a regression.

## 11. Stay inside our competence

The repository covers software delivery, engineering organizations, AI adoption, project health, technical initiatives, resourcing, vendors, product and engineering collaboration, and executive technology decisions. It does not attempt legal, financial, tax, HR-policy, marketing, or medical expertise. Where a decision crosses into those domains, the skill says so and hands off.
