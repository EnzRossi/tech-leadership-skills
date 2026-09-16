# Sourcing recommendation: international seller payouts

Prepared 16 September 2026 for the CTO. Decision horizon: the supplied approximately five-month deadline; confirm its exact calendar date rather than reconciling it against today's date.

## Recommendation

**Confidence: Medium on the sourcing direction; Low on deadline feasibility until the banking-data restriction and delivery ownership are resolved.**

| Component | Differentiation | Recommended model and reason |
|---|---|---|
| Country payout rails and standardized payment execution | Commodity, mission-critical — INFERENCE | Evaluate buying a provider only if Compliance confirms the data flow satisfies the restriction and the exact countries/capabilities are supported. |
| Seller experience, internal banking-data handling, reconciliation and platform integration | Supporting or potentially core — INFERENCE; differentiation to confirm | Internally owned implementation, with a bounded payments-experienced partner for defined launch work if an internal receiving owner can be freed. |
| Ongoing operating capability and architecture accountability | Supporting, retained internally — INFERENCE | Establish an internal owner immediately; assess hiring for the continuing need, without making the launch depend on recruitment. |

Do not make hiring a new payments team the sole launch plan. **FACT:** Your last senior hires took four and six months before any ramp, while six platform engineers are fully committed. The first step is a short feasibility and ownership decision: Compliance validates permitted data flows while the CTO frees time for an accountable technical owner and validates a country-by-country release boundary.

## Capability and consequence

**FACT:** Two enterprise sellers signed conditional on payouts in 14 countries by end of Q1, approximately five months away. Current capability is US-only with one processor. **INFERENCE:** Missing the commitment puts those commercial relationships at risk; revenue and contractual consequences are unknown. **ASSUMPTION:** Operating payouts is ongoing, while initial country expansion is bounded launch work.

## Dimension assessment

| Dimension | Payout rails | Internal integration and launch | Evidence |
|---|---|---|---|
| Differentiation | Commodity | Supporting, possibly core seller logic | INFERENCE: standard movement of money versus marketplace-specific behavior |
| Maturity | Established pattern; suitable product unverified | Partly known implementation | INFERENCE; no vendor capability claims verified |
| Domain knowledge | Industry | Industry plus proprietary marketplace context | INFERENCE from payments and existing integration |
| Integration depth | Interface integration to validate | Entangled with internal banking data and operations | INFERENCE |
| Urgency | Months | Months | FACT: roughly five months and conditional sellers |
| Duration | Ongoing | Launch spike, then ongoing maintenance | ASSUMPTION |
| Requirement uncertainty | Partly defined | Partly defined | FACT: countries/count and constraint, but acceptance criteria missing |
| Internal skills | Payments specialist absent | Domain expertise absent; general engineering present | FACT: no payments specialist hired; team of six |
| Internal capacity | Fully committed | Fully committed | FACT: board reliability program |
| Talent availability | Hireable but slow | Hireable but slow | FACT: four- and six-month senior hires; payment-specific market remains unknown |
| Security/compliance | Restricted until a compliant flow is proven | Restricted banking-data component | FACT: banking data must stay in own systems |
| Knowledge retention | Provider mechanisms need not be owned | Must retain operating knowledge | INFERENCE: ongoing accountability and integration maintenance |

**Information still needed:** iteration frequency, management capacity, budget shape, option-specific exit costs, exact country list and provider coverage, data-access interpretation, technical owner, ongoing operating workload and actual commercial downside. CTO, Compliance, Finance and Sales should supply these before commitments.

## Options removed or conditional

| Option | Treatment and reason |
|---|---|
| Internal build alone | Removed under current allocation: the fully loaded team cannot also absorb this launch without an explicit priority change. |
| Hire alone to hit date | Rejected as an executable date plan: historical hiring consumes most or all of five months, before ramp. Hiring remains available for ongoing work. |
| Provider handling prohibited banking data | Removed unless Compliance confirms that its actual data flow satisfies the regime. Do not assume tokenization, encryption or contractual promises create permission. |
| External implementer with prohibited data/system access | Removed for that component unless an approved access model exists. Work on synthetic data or constrained interfaces is a possibility to validate. |
| Agency as sole permanent owner | Rejected: it leaves ongoing operations without an internal receiving owner. |
| Fixed-scope full launch now | Conditional: country and compliance acceptance criteria are insufficiently defined to contract the entire outcome responsibly. |

## Alternatives considered

**Hiring a payments team** is attractive for retained expertise. It loses as the immediate delivery route on your own hiring history and absent specialist experience. Reconsider a narrowly scoped ongoing hire once you know which capabilities remain after a provider is adopted.

**Building with the existing platform team** protects knowledge and control. It becomes viable only if leadership explicitly reduces reliability work and confirms the freed skills/capacity can deliver. Treat that board-level trade-off seriously; do not assume spare evenings or cost-free internal time.

**Staff augmentation** can add hands but requires daily technical direction; it is less attractive than bounded outcome delivery while payments expertise is missing. A **consultant** can clarify architecture and country feasibility but cannot deliver the rollout. **Wait** is suitable for the short validation gate, not an indefinite response to a dated commitment.

## Trade-offs and external-firm neutrality

**INFERENCE:** For a bounded launch package, two external-use conditions hold: duration is limited and internal capacity is blocked by another commitment. Hiring speed also threatens the deadline, though payment-specific recruitment remains unknown. This supports external launch help only if an internal owner has time to accept the work. It does not justify outsourcing the permanent capability.

Proposed partner end: completion of the Q1 launch package plus a separately bounded handover period, with the exact calendar end date fixed before signature. Receiving owner: a CTO-designated internal technical lead, named before engagement. Require paired design reviews, repository ownership, executable tests, operational runbooks, incident drills and a handover acceptance test.

## Cost drivers

| Option | Costs to obtain | Figures available / owner |
|---|---|---|
| Buy | Setup, transaction/FX fees, volume tiers, reconciliation, integration, compliance and migration | None; Finance/procurement and provider quotes |
| Internal build | Freed reliability capacity, implementation, security, continuing maintenance and operations | Team size only; engineering and Finance |
| Hire | Search, compensation, management, time to fill and ramp | Four/six months historical fill; recruiting supplies remainder |
| Partner | Discovery, delivery, acceptance effort, change requests, access setup, knowledge transfer and maintenance after handover | None; procurement and technical owner |
| Augment | Rates, onboarding, daily supervision, paired knowledge transfer | None; engineering/procurement |
| Consultant / short validation | Specialist fee, internal briefing and acting on findings | None; CTO |
| Wait | Delay exposure and interim manual/US-only operation | None; Sales and Finance |

For planning, maintenance and operations dominate the lifetime cost of built systems; ramp and time-to-fill dominate the first-year delivery economics of hiring. These are qualitative planning considerations, not a quantified forecast for this company.

## Transition and risk controls

1. Within a proposed week, Compliance documents exactly what may leave company systems and who may access it. CTO names and allocates an internal owner. Sales supplies country-level requirements and acceptance criteria.
2. Within a proposed second week, validate a representative payout/reconciliation path and provider coverage against those requirements. Produce an achievable dependency plan, with country restrictions and banking-data flows explicit.
3. If feasible, buy the commodity rails and scope the partner's bounded integration package. Internal staff retain authorization, data and operational ownership; acceptance includes duplicate prevention, failure recovery, reconciliation, observability and handover.
4. If no compliant route or available owner exists, escalate scope/date versus reliability priorities immediately. Leadership must change a constraint; an agency does not remove it.

## Exit strategy

| Option | At six months | At eighteen months | Clean-exit condition |
|---|---|---|---|
| Provider | Migration/switching likely requires integration and reconciliation work | Re-evaluate usage economics and coverage; switch if justified | Tested data export, mapping and replaceable adapter; no unexamined proprietary workflow dependence |
| Partner | Engagement ends with accepted handover | No standing dependency; new work separately justified | Owned code, tests, runbooks and internal ability to operate |
| Internal build | Stop or replace launch modules; absorb sunk effort | Ongoing replacement/decommissioning cost depends on entanglement | Clear module boundaries and retained knowledge |
| Hire | Role likely only recently productive; leadership reviews ongoing need | Retained operating owner if workload supports it | Documented responsibilities; people decisions reserved for leadership |
| Augmentation, if substituted | Fixed contract end with pairing complete | No automatic renewal | Internal lead can run and modify delivered work |
| Consultant / validation | Already complete | Reuse retained findings, reassess changed assumptions | Deliverables retained and decisions acted on |

## Conditions that change the recommendation

If a compliant provider cannot serve the exact countries, reopen sourcing and commitment scope; do not substitute an unsupported product claim. If leadership frees enough capable internal capacity, internal implementation can replace partner work. If no receiving owner can be made available, do not engage delivery help. If ongoing custom work is substantial, strengthen internal hiring; if it is small, do not hire a whole team.

Leadership retains budget, vendor contracting, hiring and changes to enterprise commitments. Approve those only with the country acceptance matrix, compliant data-flow decision, named owner and costed feasible delivery plan.
