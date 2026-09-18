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

Check, in order: an existing licensed tool that already does it; a mature product or open-source project that does; a feature or configuration of a system already in place; a spreadsheet, form or process change; then a custom build. For each rejected alternative record the specific requirement it fails, stated by a user, not a preference for building. Establish who owns the tool after launch (on-call, upgrades, access, support) and whether intended users were consulted or only the proposer. Count the opportunity cost: the engineers who build it are not building something else. A custom internal tool can be justified by a specific unmet requirement or a substantiated total-cost advantage, real usage and accepted maintenance ownership. Test completion time, error/rework rate and repeat adoption against the current workflow; attendance at a mandated demo is not adoption. Separate capacity released from cash savings unless a realizable spending reduction is identified. Otherwise recommend the alternative, a time-boxed trial of it, or dropping the idea.

## Market and competitors

- **Beachhead first.** Name one segment in one geography that the proposer can reach and that feels the problem most acutely. A small group with an intense need is a better start than a large group with mild interest.
- **Local facts.** For the chosen geography record language, currency, dominant payment rails, tax and invoicing norms, data-protection and sector regulation, procurement habits, and the incumbents buyers already use. Do not infer legal classifications from a sector name; identify the question for a specialist.
- **Competitor set.** Include direct competitors, substitutes, "do nothing / spreadsheet / hire someone", and adjacent platforms likely to add the feature. Where tools allow, look up current offerings and pricing and cite the page and date; when relying on memory, mark it unverified and approximately dated. Do not describe a competitor's features or funding from memory as fact.
- **Reading the field.** A crowded market suggests buyers exist for something in this space, not that they will pay for this product; the question becomes the wedge (segment, price, channel, workflow, geography). An empty market requires the proposer to show either a new enabler or a demand signal; otherwise retain demand as unknown; a web search alone cannot establish absence of demand.
- **Sizing.** Only size if decision-relevant. Addressable accounts × price is a ceiling, not a forecast. An association membership count may include ineligible accounts and exclude eligible ones. A reachable-market scenario additionally needs a credible acquisition route and adoption assumptions, clearly separated from observed demand. Each number needs a supplied or cited basis; do not invent penetration to complete a formula. Present top-down "TAM" figures, if the proposer insists on them, as context and not as demand.

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

Match evidence to the claim instead of treating a fixed hierarchy as a score:

| Claim | Useful evidence | What it cannot establish |
|---|---|---|
| The problem matters | Recent concrete episodes, existing workarounds, cost or effort observed | That this solution is wanted or worth its price |
| A buyer will commit | A purchase or a pilot with a named authorized buyer, price, scope and start conditions | Broad demand or repeat revenue |
| The solution creates value | Task completion and outcomes against the current alternative | Sustainable acquisition or retention |
| Value persists | Repeat use, renewals or repeat purchase over the natural usage cycle | Profitable scale outside the tested cohort |
| A route is repeatable | Eligible leads reached and converted with measured effort and cost | That another geography or segment behaves the same |

Record who participated, how recruited, when, the denominator, and material counterevidence. Friends, incentives, founder-assisted pilots and early enthusiasts can distort results. Inspect LOIs for authority, price, procurement conditions and whether the buyer can walk away; do not infer legal enforceability. Distinguish refundable deposits, one-off payments and renewal. For marketplaces test both sides in the same narrow place/time/category, including completed matches and repeat transactions; one side's waitlist does not validate liquidity. For free products identify who sustains the service and test that party's value separately.

In interviews, ask for the last occurrence, what they did, its consequences, who approved spending and what they already tried. Request artifacts when appropriate, ask about reasons not to switch, and seek nonbuyers or churned users as well as enthusiasts. Avoid pitching until after problem exploration. Useful interviews establish problems and constraints; behavioural tests establish different claims. Do not dismiss interviews merely because money has not changed hands.

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

Unit economics only from supplied or cited figures: price per unit, cost to serve per unit, cost to acquire a customer, payback and churn where known; show arithmetic and denominators. When figures are absent, name the dominant missing driver rather than estimating it. Cost drivers to name: build and iteration effort, go-to-market (channel, content, sales time), operations and hosting, model or API usage, compliance and security work, support, and the proposer's own time or salary forgone. Give numerical cost ranges only when supplied or cited rates, quantities and scope support them; route a delivery estimate to `agentic-project-estimation` and a sourcing decision to `build-buy-hire-augment`. Identify legal, tax, licensing, data-protection and regulatory questions as boundaries with a named specialist role; do not decide them.

## Verdict and tests

| Verdict | When | What it does not mean |
|---|---|---|
| Pursue | Evidence adequate for the specified next commitment: credible buyer commitment or internal outcome/adoption evidence, a reachable accountable decision maker, viable cost structure and feasible next version | A funded roadmap; the next commitment is still bounded |
| Test before building | Plausible problem and buyer but demand, route or price is untested | Permission to build the product while "testing" |
| Reshape | Real problem, wrong segment, geography, product form or business model | The original idea is validated |
| Park | Sound idea whose enabling condition (regulation, technology, the proposer's capacity, timing) is absent | The idea is bad |
| Stop | Credible negative evidence from an adequately targeted test, a binding constraint or economics that cannot work, or an adequate alternative with no demonstrated reason to replace it | The proposer is wrong about the problem existing |

Read [experiment design](experiments.md) when selecting a test or interpreting results. Prioritize important assumptions with weak evidence, including hard feasibility or permission constraints that could make demand testing pointless. Pass, fail and inconclusive outcomes all need next actions. Stop the current hypothesis only when the evidence supports doing so; no interviews yet, sparse traffic or no competitors found means unknown, not disproven.

## Worked example (fictional)

A founder in Portugal proposes an AI assistant that drafts responses to public-procurement tender questions for small construction firms, first in Portugal, later "all of Europe". Evidence: two firms said it "sounds useful"; a demo on three past tenders produced drafts the founder liked.

**Verdict: test before building.** The weakest point is demand and route: nobody has committed money or time, and the buyer and route remain unverified. A proposed hypothesis is that firm owners can be reached through accountants or sector associations; no supplied evidence establishes that channel. Portuguese-first is a reasonable beachhead because tender formats, language and the national procurement portal are specific; "all of Europe" is not a market, it is a list of separate markets. Competitors include general assistants, incumbents in tender-management software that could add drafting, and consultants firms already pay. Defence would come from tender-format expertise and portal integration, not from the drafting itself, which the model vendor could match. AI fit is plausible but untested beyond three chosen examples; errors in compliance sections are costly and a firm owner may not detect them. Proposed test: recruit eligible firms outside the founder’s friends for a bounded manual pilot at an explicit price, with a qualified reviewer checking drafts before use. Confirm the effort cap, cohort, price and outcome criteria with the proposer before running it. Payment tests initial willingness to pay; repeat purchase at the next relevant tender tests recurring value. Too few eligible firms or no new tender during the window is inconclusive, not rejection. Do not build the portal integration before that result. No market size, price or cost figures are supplied in this example, so none are stated.
