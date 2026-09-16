# Sourcing methodology

EnzRossi's synthesis of [attributed concepts](sources.md). No validated scoring model, universal staffing ratio, or preference for a delivery provider is claimed.

## Decomposition and ownership

Split where different sourcing choices can coexist behind a maintainable boundary, not at every feature. Ask whether better performance changes customer choice, whether the component is a mature utility, how entangled its data/workflow is, and who must retain the know-how. Mission-critical infrastructure can be commodity; a commodity component may still be cheaper or simpler to retain internally.

Separate **solution** (retain/build/buy/stop) from **delivery and ownership** (existing team/hire/contractor/augmentation/partner/consultant). A hybrid adds coordination costs; show interface ownership and integration acceptance before recommending it. Do not equate owning IP with employing every contributor.

| Delivery option | Useful when | Evidence needed / main failure mode |
|---|---|---|
| Existing team | Capability and capacity exist, or a named priority can move | Which work stops; who operates it; critical-path opportunity cost |
| Hire internally | Durable work and institutional knowledge need a stable owner | Recruiting and ramp evidence, manager capacity, future role beyond initial delivery |
| Contractor / staff augmentation | Internal lead can direct bounded or transitional work | Access, review time, scope, knowledge transfer, end/review trigger; added people do not resolve missing decisions |
| Project partner | Outcome can be accepted incrementally; supplier can own delivery | Acceptance authority, interfaces, uncertainty allocation, receiving owner; fixed price does not remove discovery risk |
| Specialist consultant | Bounded expertise/judgment unlocks work others will own | Question, deliverable, recipient who can act; one compelling expertise gap can justify this option |
| Buy product/platform | Available product meets must-haves with acceptable integration and exit cost | Verify fit/access/pricing at workload; retain an operating and vendor owner |
| Do nothing / wait / reprioritize | Benefit, urgency or capability need is unproven, or another commitment matters more | Consequence of waiting and trigger to revisit; not a permanent escape from deciding |

## Constraints and trade-offs

Use the same standard for all options. Mark a constraint as **verified**, **reported**, or **unresolved** and show the source.

- **Access/security/compliance:** disqualify only a delivery form that cannot meet the actual requirement. On-premises, de-identified inputs, controlled access or separate interfaces may change eligibility. Do not assume they are approved. Escalate ambiguous interpretation to the accountable owner.
- **Time to value:** compare procurement/startup/ramp/integration and acceptance against the actual needed-by date. An existing employee moving teams may ramp faster than a contractor; a proven specialist may beat recruiting. Use this organization's evidence.
- **Uncertainty:** fixed scope without agreed acceptance is a poor fit. A paid discovery phase, time-and-materials work or iterative partner engagement can still be appropriate. Product trials can clarify requirements before a long contract.
- **Duration and knowledge:** a short project can lead to a durable platform role. An ongoing core can use outside specialists with capable internal ownership. Check the receiving team's ability to operate and change it; do not prohibit all outside help by label.
- **Management capacity:** every choice requires it, including buy and wait. If no one can direct work or accept an outcome, first free or establish an owner. External delivery does not outsource accountability.
- **Reversibility:** quantify or describe the cost of replacing each option, including an internal build. Prefer a reversible learning step when options are close only if it resolves uncertainty cheaply enough.

A weighted score is optional only if requested. Show weights, evidence, sensitivity to uncertain inputs and hard constraints separately. A tiny lead is not a decision rule.

## Cost and transition

Compare the same scope, service level, demand scenario and horizon. Distinguish one-time, recurring and transition costs; do not turn accounting categories into legal or financial advice.

| Option | Include when material |
|---|---|
| Build/retain | Build changes, dependencies, run/support, upgrades, foregone roadmap, later replacement |
| Buy | License/usage tiers, integration, migration, data egress/export, training, vendor management, replacement |
| Hire | Recruiting, compensation/benefits, ramp, manager time, durable role needs |
| Augment/partner | Fees, provisioning, internal direction/review, acceptance, rework, overlap with receiving team, exit |
| Wait | Manual work, cost of delay, option to learn before committing |

Where figures are supplied, calculate transparently. Example (fictional, same six-month scope): a partner quote of 120k plus 30k internal acceptance and 20k transition is 170k before unknown run costs. Comparing only 120k with 150k internal delivery would reverse the ranking by omitting costs. Check which costs are incremental versus already committed; do not count salaried effort twice as cash and opportunity cost without explaining the distinction.

Transition should have evidence of readiness, not just a promised date: named receiver with allocated time; incremental code/data access; review and rehearsal; receiving team independently deploys, modifies, and recovers; exit artifacts and remaining dependencies. End/review dates can be proposed, but cannot be presented as agreed. Ongoing arrangements may need periodic review rather than a fictitious terminal date.

## Symmetric challenge

- If the publisher sold the opposite option, would the recommendation change? If yes, remove the sales-driven premise.
- What is the strongest reason to retain internal ownership, and the strongest reason to bring in outside capability? Do not require two arbitrary conditions for one side.
- What fact would reverse the recommendation? If none, this may be preference dressed as analysis.

## Worked example (fictional)

An internal team understands its product but needs a one-week review of a novel storage consistency design. It has a technical owner with time to brief and act, no internal reviewer with the required expertise, and no production data access is needed.

A specialist consultant can be justified by the expertise gap alone. Scope the review to failure modes and a reproducible test plan, with the internal owner receiving it. Hiring for this review is not warranted unless a durable role is independently demonstrated. This is neutral even though the publisher sells services; an automatic internal preference would make the decision worse.
