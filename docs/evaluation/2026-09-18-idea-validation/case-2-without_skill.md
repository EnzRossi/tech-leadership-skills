# Memo: Should we build our own feature-flag and gradual-rollout system?

**To:** VP Engineering
**Re:** Proposal to build an internal feature-flag / progressive-delivery system (2 engineers, 6 weeks) instead of expanding LaunchDarkly

## Short answer

Probably not as proposed. The three stated reasons are all real concerns, but none of them actually requires building a flag platform, and the 6-week estimate describes a prototype, not the system a 120-person fintech will end up depending on for years. My recommendation is to treat this as a *sourcing* decision with four options, not a build-vs-LaunchDarkly binary, and to run a short, time-boxed evaluation before committing anyone's quarter.

I would not say a flat "no" to the engineer. The instinct to integrate flags tightly with the deploy pipeline is good and worth funding. The instinct to write the flag engine, targeting rules, UI, audit log and SDKs from scratch is where the proposal goes wrong.

## What the proposal gets right

- **Cost pressure is legitimate.** LaunchDarkly's paid tiers are usage-priced. As of mid-2026 the Foundation plan is quoted at roughly $12/month per service connection plus about $10 per 1,000 client-side monthly active users, with Enterprise and Guardian on custom quotes (see [GrowthBook's pricing breakdown](https://www.growthbook.io/insights/launchdarkly-pricing) and [costbench](https://costbench.com/software/developer-tools/launchdarkly/)). For a fintech with a consumer app, the client-side MAU meter is the one that grows with the business, not with engineering headcount. "Expensive" is plausible once you expand from one team to all of them; you should get the actual quote before anyone argues about it.
- **Tight pipeline integration is valuable.** Flags that are created, referenced and cleaned up as part of the deploy flow, with rollout stages driven by deployment health, are a real productivity and safety win. That is a thin integration layer, though, not a flag engine.
- **Ownership matters in a regulated business.** Auditors will ask who changed which flag, when, with whose approval, and whether production behaviour can be reconstructed for a given date. You do need to own that *evidence*, whichever tool produces it.

## Where it goes wrong

### 1. The estimate covers the fun 20 percent

Six weeks for two engineers is credible for: a flag store, boolean and percentage rollouts, a server SDK for your main language, and a basic admin page. It is not credible for the parts that make a flag system safe to bet the company on:

- Deterministic bucketing that is stable across services and SDK versions (so a user is not in the 5 percent cohort in one service and the 95 percent in another).
- Multi-language SDKs with local evaluation, caching, streaming or polling updates, and correct fail-open/fail-closed behaviour when the flag service is down. In fintech, "the flag service is down so every payment route fell back to default" is an incident, not an edge case.
- Client-side (web and mobile) evaluation without leaking targeting rules or PII.
- Segment and attribute targeting, prerequisites, scheduled changes, and flag lifecycle (stale-flag detection and removal), which is what actually keeps a codebase from rotting.
- Audit log, approvals and role-based access good enough to hand to SOC 2 / PCI auditors as change-control evidence.
- Metrics-linked automatic rollback, which is the thing "gradual rollout" is really for. This is what LaunchDarkly sells at the Guardian tier and it is not a six-week feature.
- Operations: this becomes a tier-0 dependency on the hot path of every request. It needs an on-call owner, SLOs, capacity planning and a runbook forever.

Realistically, a mature internal system is 12 to 18 months of one to two engineers' attention, front-loaded, and then a permanent tax of roughly half an engineer. The build cost is not $X for six weeks; it is the opportunity cost of what those two senior engineers would otherwise have shipped, plus the maintenance tail.

### 2. "We'd own it" cuts both ways

Owning it means owning the outages, the SDK upgrades every time a language runtime moves, the security reviews, and the recruiting story ("you'll maintain our home-grown flag system"). Feature flagging is not a differentiator for a fintech. Your customers do not pay you for a better flag UI. Undifferentiated infrastructure is exactly the category where buy or adopt-open-source normally wins.

### 3. It is a false binary

The choice is not "LaunchDarkly at full price" versus "write it ourselves". The open-source and open-standard landscape in 2026 is mature enough that the middle options are strong:

- **OpenFeature** is a CNCF standard SDK that decouples your application code from any particular flag backend. LaunchDarkly, Flagsmith, Unleash, flagd and others all ship providers for it ([OpenFeature mid-2026 update](https://openfeature.dev/blog/openfeature-mid-2026-update/), [1xAPI guide](https://1xapi.com/blog/feature-flags-nodejs-openfeature-2026-guide)). Adopting it now is the single cheapest way to get the "ownership" the engineer wants: you own the integration surface, and you can swap the backend later without touching application code.
- **Self-hostable open-source backends** (Unleash, Flagsmith, GrowthBook, Flipt, flagd) give you the admin UI, SDKs, targeting and audit trail already written, with the data on your own infrastructure ([FlagShark comparison](https://flagshark.com/blog/open-source-feature-flag-tools-compared-2026/), [GO Feature Flag roundup](https://gofeatureflag.org/blog/best-opensource-feature-flag-tools)). Several are explicitly positioned for regulated, self-hosted environments ([Flagsmith OpenFeature docs](https://docs.flagsmith.com/integrating-with-flagsmith/openfeature)). Note the caveat one commentator makes: OpenFeature ports your *code*, not your flag *data*, so backend migration is still a project, just a much smaller one ([stribog.com](https://stribog.com/blog/openfeature-flagsmith-unleash-self-hosted-feature-flags-runtime-control)).

## The four real options

| Option | Upfront engineering | Ongoing cost | Fit for the stated reasons |
|---|---|---|---|
| **A. Expand LaunchDarkly company-wide** | Low (weeks of rollout) | Highest cash cost, scales with MAU; negotiate | Fails the "expensive" test unless negotiated; strong on audit, rollback, SDK maturity |
| **B. OpenFeature + self-hosted OSS backend (Unleash / Flagsmith / GrowthBook / flagd)** | Medium (4 to 8 weeks: deploy, harden, migrate one team, pipeline glue) | Infra plus roughly 0.25 to 0.5 engineer for ops and upgrades; optional paid support | Meets ownership and pipeline integration; largely meets cost; audit features vary by product, verify |
| **C. Build from scratch (the proposal)** | High and underestimated (6 weeks to a demo, 12 to 18 months to parity) | 0.5 engineer forever, plus on-call for a tier-0 service | Meets ownership and pipeline integration at the highest total cost; weakest on rollback and audit for a long time |
| **D. Hybrid: OpenFeature now, keep LaunchDarkly for the one team, defer the backend decision** | Lowest (2 to 3 weeks) | Current spend | Buys a reversible position; does not solve company-wide rollout yet |

My default recommendation is **B, entered via D**: standardise on OpenFeature in the deploy pipeline and the shared libraries first, then run a 2 to 3 week evaluation of two self-hosted backends against a written requirements list, in parallel with getting a real LaunchDarkly quote for all-company usage. Give the senior engineer the OpenFeature integration and the pipeline glue. That is the part of his proposal that is genuinely valuable, it uses his enthusiasm, and it is where tight deploy-pipeline integration actually lives.

Choose A over B if the negotiated LaunchDarkly number comes in under roughly the loaded cost of half an engineer per year and your compliance team strongly prefers a vendor-attested audit trail. Choose C over B only if the evaluation shows that every OSS backend fails a hard requirement (for example, a data-residency or evaluation-latency constraint none of them can meet). I would be surprised.

## Questions I would ask before deciding

**About the pain**
1. What specifically is broken today? Is the problem that the other teams have no flags at all, that they have ad hoc config flags with no rollout control, or that LaunchDarkly's price for expanding is the blocker? The answer changes which option wins.
2. Has anyone actually obtained a company-wide LaunchDarkly quote, or is "expensive" extrapolated from list price? Ask for the quote and the negotiated number. Vendors move a lot at renewal when there is a credible open-source alternative on the table.

**About requirements**
3. What does compliance and security need from flag changes: approval workflows, immutable audit log, SSO and RBAC, retention? Who signs off that a self-hosted tool meets it?
4. Do we need client-side flags in web and mobile, and at what MAU? That is both the cost driver for SaaS and the hardest part to build well.
5. Do we need metrics-driven automatic rollback in the next 12 months, or is manual staged rollout with good observability enough for now?
6. What is the acceptable failure mode when the flag service is unavailable? Who has defined default behaviour for the payment and ledger paths?

**About the build proposal itself**
7. Ask the engineer for the six-week scope written as a list of what is explicitly *out*: client SDKs, segments, approvals, audit export, scheduled changes, stale-flag tooling, HA deployment. If most of that is out, the estimate is for a prototype and should be labelled that way.
8. Who owns it in year two, including on-call? Is that person him, and what happens if he leaves?
9. What is he not going to build during those six weeks, and does the product side agree that trade is worth it?
10. Has he evaluated Unleash, Flagsmith, GrowthBook or flagd and rejected them for a concrete reason, or has he not looked? "We could build it" and "we should build it" are different claims.

**About the organisation**
11. Is there a platform or developer-experience team that would naturally own this? If not, a home-grown tier-0 service with no team home is a known failure pattern.
12. Is there a hidden motive worth surfacing kindly: a senior engineer wanting a greenfield project? That is a legitimate retention concern, but it should be solved with a project the company needs, and the OpenFeature and pipeline-integration work may satisfy it.

## Suggested next steps

1. This week: request the all-company LaunchDarkly quote; ask the engineer to write the one-page requirements list and the explicit out-of-scope list for his proposal.
2. Next 2 to 3 weeks: he leads an evaluation of two self-hosted OSS backends behind OpenFeature, using one real service and one real rollout, with compliance in the room for the audit and access-control requirements.
3. Decision meeting with a simple scorecard: total three-year cost (cash plus loaded engineering time), audit and compliance fit, failure-mode behaviour, and migration effort in and out.
4. Whatever backend wins, standardise flag access on OpenFeature so the decision stays reversible.

## Sources

- [GrowthBook: LaunchDarkly pricing 2026](https://www.growthbook.io/insights/launchdarkly-pricing)
- [costbench: LaunchDarkly pricing](https://costbench.com/software/developer-tools/launchdarkly/)
- [LaunchFlag: LaunchDarkly's two pricing meters](https://launchflag.dev/blog/launchdarkly-pricing)
- [OpenFeature mid-2026 update](https://openfeature.dev/blog/openfeature-mid-2026-update/)
- [1xAPI: Feature flags in Node.js with OpenFeature 2026](https://1xapi.com/blog/feature-flags-nodejs-openfeature-2026-guide)
- [Flagsmith docs: OpenFeature](https://docs.flagsmith.com/integrating-with-flagsmith/openfeature)
- [FlagShark: open-source feature flag tools compared 2026](https://flagshark.com/blog/open-source-feature-flag-tools-compared-2026/)
- [GO Feature Flag: best open-source feature flagging tools 2026](https://gofeatureflag.org/blog/best-opensource-feature-flag-tools)
- [stribog.com: OpenFeature ports your code, not your flag data](https://stribog.com/blog/openfeature-flagsmith-unleash-self-hosted-feature-flags-runtime-control)

Pricing figures are as quoted by third-party summaries in 2026 and should be confirmed against LaunchDarkly's own quote before use in a decision.
