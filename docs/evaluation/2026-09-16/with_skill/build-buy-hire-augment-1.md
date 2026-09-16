# Sourcing decision: International seller payouts

CTO · Planning horizon: supplied five months to end of Q1

## Recommendation

**Confidence: Medium in the sourcing direction; low in deadline feasibility until data flow and country fit are verified.**

Pursue a conditional hybrid: buy suitable payout infrastructure and use an experienced payments partner for bounded integration, with an internal technical owner allocated now. Do not make hiring a full payments team the Q1 dependency. Your reported four- and six-month senior hiring cycles consume most or all of the five-month window before ramp-up. The immediate gates are what Compliance permits and who can own acceptance while the six platform engineers are committed to reliability.

## Why this choice

| Component | Solution + delivery route + long-term owner | Decisive evidence |
|---|---|---|
| Country payout execution | Conditionally buy provider capability; partner can assist integration. Proposed internal payments owner remains accountable for service/vendor operation. | Fourteen-country expansion is materially beyond the reported US-only setup. Provider coverage, onboarding time and data handling remain unverified; no named platform is endorsed. |
| Marketplace payout control, bank-data boundary and reconciliation | Retain/build integration in your systems with a payments-experienced partner; internal technical owner owns interfaces and acceptance. | Banking-data constraint and durable operational accountability require an explicit boundary. Outside delivery may be possible through approved access, but this is not established. |

The banking requirement is **reported by Compliance**, not yet a verified architecture rule. Clarify whether “stay within our systems” prohibits storage elsewhere, transmission, third-party processing, or only unnecessary retention, and what payment execution is permitted. A provider needing prohibited data access is ineligible in that form. It does not follow that every provider or agency is excluded, nor that tokenization or controlled access automatically complies. Building internally would still need a permissible way to execute payments through financial institutions.

The strongest competitor is reprioritizing existing engineers and buying infrastructure directly. It avoids partner coordination, but the team lacks reported payments expertise and already has a board-backed reliability commitment. It becomes preferable if you can free capable ownership and delivery capacity without unacceptable reliability impact. A partner adds specialist capacity but also procurement, onboarding, review and handover load; it cannot replace internal accountability.

Hiring could support durable operations later, once the ongoing role is established. It has weak timing evidence for this launch. Status quo preserves reliability capacity but fails the stated expansion commitment to the two enterprise sellers. Renegotiating scope or timing remains a leadership option if no compliant, credible route fits; it is not costless waiting.

## Cost, transition and exit

Compare all options over the same 14-country scope, five-month delivery window and agreed operating horizon, using the same payout volumes and service requirements. No defensible cash total is possible without country mix, volumes, fees and staffing costs. Include provider transaction/FX and support costs, integration and reconciliation, partner fees, internal review, operations, maintenance, hiring/ramp where applicable, migration and replacement. Report reliability opportunity cost separately from payroll to avoid double-counting.

Free a named internal receiver by explicitly deciding which current work moves. That owner controls API/data interfaces and accepts incremental country and failure-mode tests: correct payouts, duplicate prevention, reconciliation, recovery and monitoring. Transition is complete when the receiving team can independently modify, deploy and recover the integration. Test provider data exports and replacement interfaces before expansion; review or end partner delivery at accepted handover, not an arbitrary duration.

## Next action

Propose a one-week feasibility decision led by the CTO, Compliance and an allocated technical owner. Produce a permitted data-flow boundary, country-by-country must-haves, provider/partner evidence requirements and a capacity-backed integration/acceptance plan. Approve only a bounded discovery commitment until these gates pass; no supplier selection or contract is implied here.

## What could change the recommendation

The hybrid's strongest weakness is scarce internal management capacity. If nobody can be freed, reduce another commitment or revisit Q1 rather than assuming an agency solves ownership. A verified data prohibition may rule out the proposed provider form. Conversely, a proven existing-processor expansion path plus available internal expertise could make direct internal integration simpler and preferable.
