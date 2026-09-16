**Unlimited cloud agents are not a feasible assumption for this repository.** The company prohibits external uploads, and the approved local agent is not yet procured. Agentic production delivery next week is therefore unproven and cannot be committed from these inputs.

The feasible dependency is:

**Approved agent available → local setup/validation → representative accepted migration → remaining migrations and release checks → cutover.**

Procurement timing, migration scope and accepted throughput are unknown, so a numeric production date would be fabricated. Procurement can overlap work that does not require the unavailable agent: inventory the migration, define data invariants, prepare approved fixtures and book the domain/cutover owner. It cannot be assumed complete or hidden inside a buffer.

| Scenario | Viable basis |
|---|---|
| Cloud agents | Excluded under the stated repository policy |
| Approved local agent | Conditional on procurement and setup; estimate from a representative accepted migration once available |
| Existing permitted manual tooling | Potential fallback if authorized and technically sufficient; requires its own scope/capacity estimate |

As engineering judgment, propose a **one-working-day planning timebox** for an engineer and migration owner to bound the scope, required access, reconciliation checks and rollback/cutover plan. This does not estimate migration implementation or procurement.

Production acceptance must include data reconciliation, failure/retry behavior and recovery evidence, with human review of consequential transformation logic. Agent review and test execution help once a compliant tool exists, but do not replace that owner.

Recommend moving the production commitment or narrowing to a permitted rehearsal until access and a measured slice establish feasibility. The procurement owner should provide the earliest approved availability; the migration owner should set the acceptance and release decision. More cloud capacity cannot resolve either gate.
