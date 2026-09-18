# Idea validation methodology

EnzRossi's editorial synthesis of the sources in [sources.md](sources.md), not a validated scoring instrument. Read the section named in the workflow step you are on; do not print these tables in the memo.

## Intake questions

Ask only what the material does not answer and only what could change the verdict. Five questions per round is a ceiling, not a target.

| Axis | Questions that change the verdict | Why it matters |
|---|---|---|
| Problem and person | Who has the problem, how often, what it costs them, what they do today, who has told you this and in what words | Demand is the most common fatal gap; second-hand or imagined pain is not evidence |
| Internal or external | Will your own organisation use it, or will others pay or adopt it? Who asked for it? | Internal ideas are judged against alternatives and ownership; external ideas against market, buyer and route |
| Geography | Which country or region first, and why? Language, currency, payment methods, regulation, local incumbents | "Global" usually means "undecided"; go-to-market, pricing and compliance are local |
| Digital, physical, hybrid | Does anything need to be manufactured, shipped, installed, certified or returned? | Physical products change cost structure, cash needs and lead times; this workflow only flags them |
| AI dependency | Does the value depend on a model doing something a rule or lookup cannot? On which real examples has it been tried? | Determines whether the AI-fit checks apply and whether a demo is being mistaken for evidence |
| Advantage and why now | What do you know, own or can reach that others cannot? What changed to make this possible or needed now? | Ideas without an insight or a timing reason face incumbents on equal terms |
| Decision at stake | What will you do with a "pursue" or "stop" answer: quit a job, fund a team, pitch a board, spend a weekend? | Calibrates how much evidence the verdict needs and how expensive the first test may be |

## Internal ideas

Check, in order: an existing licensed tool that already does it; a mature product or open-source project that does; a feature or configuration of a system already in place; a spreadsheet, form or process change; then a custom build. For each rejected alternative record the specific requirement it fails, stated by a user, not a preference for building. Establish who owns the tool after launch (on-call, upgrades, access, support) and whether intended users were consulted or only the proposer. Count the opportunity cost: the engineers who build it are not building something else. A custom internal tool is usually justified when the workflow is specific to the organisation, alternatives fail a stated requirement, usage volume is real, and an owner has accepted maintenance. Otherwise recommend the alternative, a time-boxed trial of it, or dropping the idea.

## Market and competitors

- **Beachhead first.** Name one segment in one geography that the proposer can reach and that feels the problem most acutely. A small group with an intense need is a better start than a large group with mild interest.
- **Local facts.** For the chosen geography record language, currency, dominant payment rails, tax and invoicing norms, data-protection and sector regulation, procurement habits, and the incumbents buyers already use. Do not infer legal classifications from a sector name; identify the question for a specialist.
- **Competitor set.** Include direct competitors, substitutes, "do nothing / spreadsheet / hire someone", and adjacent platforms likely to add the feature. Where tools allow, look up current offerings and pricing and cite the page and date; when relying on memory, mark it unverified and approximately dated. Do not describe a competitor's features or funding from memory as fact.
- **Reading the field.** A crowded market suggests buyers exist for something in this space, not that they will pay for this product; the question becomes the wedge (segment, price, channel, workflow, geography). An empty market requires the proposer to show either a new enabler or a demand signal; otherwise treat it as likely absence of demand.
- **Sizing.** Size bottom-up: number of target accounts or users in the beachhead × plausible price × plausible penetration, each factor supplied or cited. Present top-down "TAM" figures, if the proposer insists on them, as context and not as demand.

## Buyer and route

| Role | Question | Common error |
|---|---|---|
| User | Who touches it daily and what changes for them | Assuming the user can buy |
| Buyer / budget holder | Whose budget pays and what they are measured on | Pricing to the user's pain, not the buyer's metric |
| Decision maker | Who says yes, and what they need to see | Pitching features to a role that buys risk reduction |
| Blocker | Who can veto: IT, security, legal, procurement, a union, a regulator | Discovering procurement after the "yes" |
| Route | How the decision maker is reached: existing relationship, community, content, outbound, partner, marketplace, app store, resellers | "We'll do marketing" with no named channel |
| Motion and cycle | Self-serve, inside sales, field sales, partner-led; days, weeks or quarters | Consumer-style growth assumptions for a six-month enterprise sale |
| Price hypothesis | What is charged, per what unit, versus what the alternative costs | Deciding price after build; price below the cost to sell |

Demand evidence hierarchy, strongest first: paid or pre-paid; signed letter of intent or pilot agreement; active use of a prototype; waitlist or sign-up against known traffic; problem interviews with specific past behaviour; surveys; opinions of friends, colleagues or investors. Conversations count when they follow good practice: ask about the person's life and past behaviour, not about the idea; avoid compliments and hypotheticals; look for a commitment of time, reputation or money.

## Defensibility

Ask what stops a competent team, the incumbent or the platform vendor from copying the idea within a year, and whether it matters for the proposer's goal (a lifestyle business tolerates copying; a venture-scale bet does not). Sources of defence: distribution or a captive channel; proprietary or accumulating data; switching costs and workflow embedding; network effects; regulatory or licensing position; brand; counter-positioning that incumbents cannot adopt without hurting their business; execution speed while the window is open. A clean interface, a prompt, or a public API integration alone rarely defends. Record platform risk: dependence on an app store, marketplace, model vendor or data source that can change terms or ship the feature.

Physical and hybrid products add manufacturing, certification and safety marks, minimum order quantities, inventory and working capital, logistics, returns, warranties and unit cost at low volume. Name these as binding uncertainties and hand them to people with hardware and supply-chain experience; do not estimate them here.

## AI fit

1. **Is a model needed?** Identify the step that requires interpretation, generation or prediction. If rules, a lookup, a template or an existing product covers it, the AI framing adds cost and risk without value.
2. **Can current models do it?** Ask for results on the proposer's real examples, including messy, ambiguous and adversarial cases, and for how they were judged. A demo on chosen examples supports a hypothesis, not a claim. Propose a bounded trial on a representative sample if none exists.
3. **Error cost and catch.** Who is harmed by a wrong output, is it reversible, and does a human with the time and knowledge to catch it sit in the loop? Human review counts only when reviewers can actually detect the error.
4. **Economics.** Cost per completed task (model usage, retries, review, tooling) against the price or value per task; check the slice where volume is highest and the slice where errors are costliest.
5. **Who else can ship this?** The foundation-model vendor, the system of record that owns the data, or the incumbent with the distribution. An idea that is a thin layer over a general model needs a specific reason customers would not go to the model or the incumbent directly: workflow, data, distribution, compliance or a segment the big players ignore.
6. **Market need.** Apply the ordinary demand checks; "AI" is not a customer problem. Use `ai-initiative-evaluator` for an enterprise-internal initiative where the fuller readiness and evaluation-contract procedure applies.

## Viability and cost

Assess four risks separately, and mark each Supported, Concern or Unknown: **value** (will they buy or use it), **usability** (can they use it), **feasibility** (can it be built with the time, skills and technology available), **business viability** (does it work for pricing, cost to serve, sales, legal, support and the proposer's own constraints). Supported means evidence exists for the next step, not proof.

Unit economics only from supplied or cited figures: price per unit, cost to serve per unit, cost to acquire a customer, payback and churn where known; show arithmetic and denominators. When figures are absent, name the dominant missing driver rather than estimating it. Cost drivers to name: build and iteration effort, go-to-market (channel, content, sales time), operations and hosting, model or API usage, compliance and security work, support, and the proposer's own time or salary forgone. Give an order of magnitude only when rates or scope are supplied; route a delivery estimate to `agentic-project-estimation` and a sourcing decision to `build-buy-hire-augment`. Identify legal, tax, licensing, data-protection and regulatory questions as boundaries with a named specialist role; do not decide them.

## Verdict and tests

| Verdict | When | What it does not mean |
|---|---|---|
| Pursue | Demand evidence at "commitment" level or above, a reachable decision maker, an acceptable cost structure, and a feasible first version | A funded roadmap; the next commitment is still bounded |
| Test before building | Plausible problem and buyer but demand, route or price is untested | Permission to build the product while "testing" |
| Reshape | Real problem, wrong segment, geography, product form or business model | The original idea is validated |
| Park | Sound idea whose enabling condition (regulation, technology, the proposer's capacity, timing) is absent | The idea is bad |
| Stop | No evidence of demand after honest search, no route to the buyer, economics that cannot work, or an alternative that already solves it | The proposer is wrong about the problem existing |

Cheapest discriminating tests, choose by what is most uncertain: problem interviews following the conversation rules above (demand); a landing page or pre-order with a concrete price against measured traffic (willingness to pay); a pre-sale, deposit or signed pilot with a named account (buyer and route); a concierge or manual version delivered by hand (value and usability); a Wizard-of-Oz or fake-door test of a feature (usage); a short model trial on a representative sample with an agreed judging rule (AI feasibility). Fix the pass and kill thresholds with the proposer before the test runs, and mark them as proposed; a threshold set after seeing the result is not a test.

## Worked example (fictional)

A founder in Portugal proposes an AI assistant that drafts responses to public-procurement tender questions for small construction firms, first in Portugal, later "all of Europe". Evidence: two firms said it "sounds useful"; a demo on three past tenders produced drafts the founder liked.

**Verdict: test before building.** The weakest point is demand and route: nobody has committed money or time, and the buyer (the firm owner) is reached through accountants and sector associations rather than online channels the founder planned to use. Portuguese-first is a reasonable beachhead because tender formats, language and the national procurement portal are specific; "all of Europe" is not a market, it is a list of separate markets. Competitors include general assistants, incumbents in tender-management software that could add drafting, and consultants firms already pay. Defence would come from tender-format expertise and portal integration, not from the drafting itself, which the model vendor could match. AI fit is plausible but untested beyond three chosen examples; errors in compliance sections are costly and a firm owner may not detect them. Proposed test: five firms, one real tender each, drafts produced by hand with the model behind the scenes, at a stated price with payment on acceptance; pass if three pay and would repeat, kill if none pay. Do not build the portal integration before that result. No market size, price or cost figures are supplied in this example, so none are stated.
