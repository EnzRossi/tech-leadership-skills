# Idea validation: in-house feature-flag and gradual-rollout system

VP Engineering, 120-person fintech · Evidence as of 2026-09-18 · Internal · digital · not AI-dependent · geography not relevant

## Verdict

**Stop the build as proposed; reshape into a two-week alternatives trial — Confidence: Medium (no problem statement was supplied, so a real unmet requirement could move this).**

The weakest point: no problem has been stated. All three reasons are about the solution ("own it", "pipeline integration", "SaaS is expensive"); none names a requirement that LaunchDarkly, cheaper vendors or open source fail. Fixable, but until closed you would fund a solution to an unknown problem. Strongest reason it could work: a fintech may need audit, approval or residency behaviour that vendors gate behind enterprise pricing; even then, self-hosted open source is the likelier answer than a from-scratch build. Next step: have the engineer write the requirement the market fails, then trial one alternative against it.

## The idea as a hypothesis

*Reported:* one team uses LaunchDarkly on a small plan; a senior engineer proposes a company-wide flag and progressive-delivery service, two engineers, six weeks. *Inferred:* other teams lack flags, so the real need is "safe gradual rollouts for every team". *Assumed:* "pipeline integration" means flag state travels with the release; confirm. *Unknown:* current LaunchDarkly spend, who asked for this, who owns it after week six.

## What the evidence shows

**1. "Expensive" has not been compared to anything.** LaunchDarkly's public pricing (launchdarkly.com/pricing, read 2026-09-18) lists a free Developer tier, pay-as-you-go Foundation at "$10 per Service Connection / mo" and "$8.33 per 1k client-side MAU / mo" billed yearly, and custom Enterprise, which is where "Custom roles & teams" and "Workflows, scheduling, & approvals" sit. Flagsmith (flagsmith.com/pricing, same date) lists $40/month Start-Up, $250/month Scale-Up and an open-source self-hosted edition. Unleash (getunleash.io/pricing) lists $75/seat/month and a free self-hosted edition limited to 1 project and 2 environments. OpenFeature (openfeature.dev), a CNCF incubating project, gives a vendor-neutral SDK with 50+ providers including all three, which addresses most of what "we'd own it" is meant to protect against.

**2. Six weeks covers the easy part.** A flag store with percentage rollouts is small. The fintech-grade tail is not: SDKs for every runtime, fail-open/fail-closed when the service is down, audit log, approvals on production changes, environment separation, stale-flag hygiene, and change-management evidence auditors accept. Vendors charge enterprise prices for approvals and roles because regulated buyers demand them and they are hard. Treat the estimate as unverified.

**3. Ownership and demand are unassigned.** A flag service is on the critical path of every deploy; nobody has accepted on-call and upgrades, and no team other than the proposer is shown to have asked. The internal-idea rule requires an organisation-specific need, a stated requirement alternatives fail, and an accepted owner. None holds yet.

**4. Opportunity cost.** Twelve engineer-weeks at your loaded rate is the first-version price; maintaining a critical-path service is usually the larger cost.

Value Unknown · Usability Unknown · Feasibility Concern (scope) · Business viability Concern (no cost comparison, no owner).

## Cheapest test that could change the verdict

The engineer writes a one-page ranked requirements list, including the pipeline integration and any compliance needs. One engineer, two weeks: stand up self-hosted Unleash or Flagsmith (or OpenFeature against the existing LaunchDarkly account) on one non-critical service, wired into the pipeline. *Proposed pass (build not justified):* all ranked requirements met, possibly via configuration. *Proposed kill of the buy/OSS route:* a top-three requirement fails and the vendor confirms it is not planned. In parallel, obtain LaunchDarkly, Flagsmith and Unleash quotes for company-wide use and place them beside twelve engineer-weeks plus a maintenance estimate. What would flip me toward building: a tested requirement all three fail that a regulator or auditor requires.

## Questions that still matter

1. What can the team not do today with LaunchDarkly, in a user's words? A concrete failure moves toward reshape-or-build.
2. What does LaunchDarkly cost now, and what was quoted company-wide? Six figures makes the comparison worth care; low four figures ends the cost argument.
3. Who besides the proposer asked for company-wide flags or pipeline integration, and what did they say?
4. What does your compliance lead expect from a flag system (audit trail, approvals, residency, PCI DSS or SOC 2 change evidence)? This often decides enterprise SaaS versus self-hosted open source.
5. Who owns the service after launch, and have they agreed?

## Boundaries

Whether flag changes are production changes under PCI DSS, SOC 2 or your regulator's rules is for your compliance lead. If the trial leaves a genuine build-versus-buy choice, route it to `build-buy-hire-augment`; a delivery estimate belongs in `agentic-project-estimation`. This memo prepares a decision; it does not authorise spending or vendor commitments.

Sources: [LaunchDarkly pricing](https://launchdarkly.com/pricing/), [Flagsmith pricing](https://www.flagsmith.com/pricing), [Unleash pricing](https://www.getunleash.io/pricing), [OpenFeature](https://openfeature.dev/), read 2026-09-18.
