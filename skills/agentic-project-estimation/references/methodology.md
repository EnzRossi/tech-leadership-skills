# Estimating accepted delivery with agents

This is EnzRossi's editorial synthesis of resource-constrained scheduling, empirical calibration and agent verification practices. It is not a validated proprietary forecasting model. [Sources and research limits](sources.md) explain the inputs.

## Company and consequence

Keep two axes distinct:

- **Business importance:** experiment, useful improvement, strategic dependency, time-critical obligation. This changes prioritization, staffing availability, scope trade-offs and the value of waiting.
- **Failure consequence:** reversible inconvenience, customer disruption, lost/corrupted data, unauthorized access, financial or safety impact. This changes acceptance and recovery requirements, even at a startup.

Company labels provide hypotheses, not durations:

| Context | Investigate | Do not assume |
|---|---|---|
| Startup / small product team | Founder decisions, existing managed services, narrow initial cohort, runway, lack of specialist ownership | No security needs; everyone full-time; production equals demo |
| Growing company | Shared services, compatibility, customer commitments, on-call capacity, onboarding | Every dependency requires a committee |
| Enterprise | Platform reuse, access permissions, multiple owners, data boundaries, change windows, scale/SLOs, procurement and evidence requirements | Universal enterprise multiplier; all systems need global scale; mature platforms cannot accelerate delivery |

Translate each applicable constraint into **specific work**, **a wait with an entry condition**, or **an unresolved assumption**. “Enterprise overhead: 40%” does not explain what can change. “Security review starts only after the data-flow diagram and working integration; next slot is day 15” does. An approval date can be a lower bound without guaranteeing approval. Keep working days, elapsed calendar days, holidays and part-time schedules explicit.

Use operational targets supplied by the user (load, availability, recovery, support hours). Where absent, propose a bounded initial cohort or target for confirmation, not an invented enterprise SLA. Avoid double-counting a security review as both ordinary review effort and extra organizational overhead.

## Calibration and arithmetic

Record a comparable slice through **accepted and integrated**, not just a generated PR:

| Measure | Why it matters |
|---|---|
| Tool/model version and date, codebase familiarity, starting assets | Tool changes and new repositories can invalidate an analogy |
| Scope and acceptance, including failures and abandoned attempts | Easy successful tasks alone bias the estimate |
| Human active time: framing, steering, review, repair, manual checks | Agent waiting is not necessarily paid active work; attention remains constrained |
| Agent elapsed runtime, retries and concurrency limits | More sessions can queue behind CI, budgets, shared state or decisions |
| Ready-to-start → accepted elapsed time, with external waits | This is the delivery target; overlapping times cannot simply be added |
| Defects/rework after acceptance over the observed period | Fast acceptance with escaped faults is not equivalent quality |

Use like-for-like local measurements first. For repetitive slices, scale only the comparable work and identify shared setup and integration separately. Keep outliers visible; a few observations can ground a planning range but not a reliable percentile. Do not count token totals, lines of code, commits, or completed tool rounds as delivery value.

Without local data, state a task-level judgment and the conditions making it plausible. A small, well-scoped static page with supplied content and an existing deploy path can reasonably be estimated in hours; do not import a multi-week software lifecycle. Conversely, a polished scaffold does not calibrate an unknown production integration. If the unknown dominates, timebox a calibration slice sized to resolve it and re-estimate at its acceptance boundary. Do not invent empirical speed data to fill a table.

Two supported approaches:

1. **Component schedule:** estimate human effort, agent execution and waiting per increment; lay out dependencies and shared-resource use. If a human can work elsewhere during an agent run, show that overlap. If they must supervise synchronously, reserve that time.
2. **Measured accepted-throughput:** use comparable accepted items per elapsed period at a stated team/quality configuration. This already includes whatever review, waiting and rework occurred in the measurement. Add only identifiable work outside that boundary. Do not multiply an end-to-end baseline by an AI coding factor.

The longest dependency path is a lower bound, not automatically a feasible resource schedule. Also check each scarce role's total work against its available hours. Do not add those lower bounds together; find a schedule satisfying both. If a single engineer is both implementer and reviewer, the same hour cannot occupy both roles. If verification is included in a slice's measured duration, flag it as included rather than add it again.

Illustrative arithmetic only: two independent accepted slices take 3 and 5 working days at one owner per slice. A shared integration step takes 2 days after both. One qualified person working serially needs 10 days; two qualified people can reach integration in 5, then finish in 7. A third person does not shorten that dependency path. This assumes no additional review queue, no onboarding and no competing work. If a release window is fixed at day 12, the earlier code finish does not move production before day 12. If the review instead starts after integration and lasts 4 days, it cannot be hidden inside those earlier days.

## Capacity and scenarios

For each candidate team, identify:

- Human role mix and actual allocation: domain/technical owner, implementers, reviewer, test/acceptance owner, operations support. One person can fill several roles if the total allocation fits.
- Agent setup: useful independent streams, isolation/branch strategy, shared interface contracts, execution/CI limits and who merges and accepts.
- Work that can run concurrently and work that remains serial; account for onboarding/context transfer when adding people.
- Calendar gates: earliest start, queue/service time, approval conditions, vendor lead time, release window. Parallel approval and implementation is valid only when approvals do not depend on completed implementation.

Offer meaningful choices rather than manufacturing “lean/balanced/enterprise” bundles. A larger team may finish no earlier, incur more cost, or create review backlog. A scarce domain reviewer cannot be replaced merely by starting more agents. When a deadline is impossible under all feasible staffing, propose scope/release changes and show the remaining gate. Importance is not evidence that overtime is sustainable.

Compare fixed scope first. If showing a prototype, limited rollout or lower-load option, give it a separate acceptance definition. If estimating labor cost, distinguish active effort from reserved team capacity and specify the billing model; do not quietly charge a full team for each agent waiting hour. Include tool/CI and operational costs as unknowns if rates are missing. Business viability remains unproven without sufficient value, budget and ownership evidence.

## Verification proportional to consequences

Use agents for implementation review, static checks, test generation/execution and fix loops where tools support them. Review coverage and execution logs matter more than a clean AI summary. A different model or agent is not guaranteed independent judgment.

| Change | Targeted human acceptance examples | Additional evidence when relevant |
|---|---|---|
| Reversible internal UI | Main task, empty/error path, keyboard/mobile behavior | Automated checks; rollback or easy revert |
| Customer workflow | Domain rules and exceptions, permissions, acceptance by a user representative | Integration tests, compatibility and deployment/recovery checks |
| High-consequence data/action | Cross-tenant denial, invariant/reconciliation checks, failure/retry behavior, recovery rehearsal | Independent domain/security review, migration/load/resilience evidence tied to actual requirements |

These are selection examples, not a mandatory full test suite for every task. “A few manual tests” is a request to focus human time; identify which risks automation covers and which require human judgment. Where the project itself contains an AI feature, include evaluation dataset/acceptance work for that feature separately from the fact that agents write its code.

## Range and viability review

Use named conditions: known integration works; expected fix cycle; adverse migration finding; missed change window. Do not stack overlapping rework, contingency and risk multipliers. Round to the resolution the evidence supports. A deterministic scenario finish is not a delivery guarantee; probabilities require a separate justified model.

Finish with the decision now, not a large discovery questionnaire. Identify the most valuable next observation, such as one accepted risky slice, an access decision or a reviewer-capacity commitment. Reforecast remaining work from actual acceptance data after that observation; preserve the original forecast and explain changes instead of retrospectively redefining success.
