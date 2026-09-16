# Sourcing decision: Feature flags and experimentation

Platform and product leaders · Evidence: your description

## Recommendation

**Confidence: Medium; a buy-first assessment is justified, but product fit and migration economics are unknown.**

Pause discretionary expansion of the internal system and evaluate buying an established product, configured and integrated by your platform team. Keep essential maintenance running. Feature flags and experimentation appear to be utility capabilities here, and you report two engineers spending nearly all their time sustaining them. Nine months already spent is not a reason to keep building; compare future cost and value from today.

## Why this choice

Buying may release platform capacity and deliver the experimentation features product needs, but no candidate has yet demonstrated your must-haves. Inventory flag semantics, SDK coverage, latency and availability needs, data requirements, experimentation analysis and integration points. Mission-critical use does not itself make the implementation a competitive differentiator.

The strongest competing option is retaining the existing system with a deliberately limited roadmap. It already works and avoids immediate migration risk. This can win if requirements are unusual, available products cannot meet them, or the maintenance burden is lower than migration and licenses over your relevant horizon. Continuing unconstrained internal expansion commits ongoing engineering capacity and is the least justified option without a differentiating need.

The team's lock-in concern is valid but incomplete. An internal system also creates dependence on its maintainers, custom SDKs and undocumented behavior. Evaluate actual switching costs symmetrically. Buying the solution still requires an internal technical owner to manage integration, reliability, access and vendor changes.

## Cost, transition and exit

Use the same feature requirements, traffic and decision horizon for both routes. Internal costs include the reported two-engineer commitment, additional feature work, support and foregone platform work. Do not label all released effort cash savings. Buying adds licenses at actual usage tiers, integration, training, dual operation, migration, administration and eventual replacement. No reliable monetary comparison is possible from supplied figures.

Proposed receiver: the platform team, with a named service owner and allocated migration time. Pilot a representative low-risk flag path, validate semantics and failure behavior, then cut over incrementally with rollback. Product should accept experiment interpretation, not just dashboard availability. Before a long-term product commitment, test configuration/data exports and replacement interfaces. Retire the internal system only when dependents are migrated and operational parity is demonstrated.

## Next action

Proposed owner: platform lead with the product experimentation owner. Run a bounded fit-and-migration assessment against a small set of must-haves and a representative integration. Produce forward costs, migration risks and the platform work freed. Seek a buy decision only if fit and benefits exceed continuing with a constrained internal roadmap.

## What could change the recommendation

The strongest argument for retention is a genuinely unusual requirement whose product workaround is costly or unsafe. Demonstrate it with the requirements inventory and integration trial. The other decisive unknowns are product cost at your workload and the realistic migration effort. Pride and sunk effort alone do not alter the recommendation.
