# Project health decision: payments reconciliation replacement

Decision maker: inherited programme sponsor. Evidence: your current account; absolute dates and original baseline were not supplied. Commitment assessed: cutover in five weeks.

## Recommendation

**Health: Amber · Confidence: medium.** Material correctness and release threats require intervention now. A five-week recovery remains possible, but ticket closure does not establish it. Keep the date conditional on demonstrated ingestion, classified reconciliation exceptions, recovery and finance acceptance. This week, seek approval to exercise the $25,000 extension within its ten-day deadline unless those gates and a credible remaining plan are established first. The extension buys an operating fallback; it does not repair data.

## Findings that change the decision

| Evidence and source | Implication for the commitment | Confidence / competing explanation |
|---|---|---|
| Your dashboard reports 92/100 tickets closed; 12/18 recent closures were documentation or UI. Remaining work includes production ingestion, partial-posting recovery and finance sign-off. | Closure percentage is not release completion. These are candidate release blockers; ticket count without sizes, dependencies or acceptance evidence cannot forecast completion. | High on the metric limitation; medium on remaining effort. Documentation/UI may be necessary release work rather than distraction. Inspect the acceptance path. |
| Your rehearsal reconciled 99.7% by count: 600/200,000 remain unmatched, representing $4.8m/$60m = **8% of processed value**. | A small count masks material monetary exposure. This is unmatched value, not proven loss. Unknown causes prevent a defensible correctness decision. | High on arithmetic; low on causes. Expected timing differences might be acceptable exceptions; mapping or posting defects could block release. Classify and trace the full $4.8m. |
| Platform engineer reports recovery locally; no recorded drill. Finance has only two testing days next week before its lead's absence. | Local recovery is not demonstrated production recovery. Acceptance has a real availability constraint; unresolved findings could have no empowered retester before cutover. | Medium. Recovery may work and a finance delegate may be available, but neither is established. Rehearse and allocate acceptance authority. |

## This week

| Action or leadership decision | Proposed owner / needed by | Evidence or outcome produced |
|---|---|---|
| Approve the extension decision and confirm how to exercise it. Default to purchasing fallback if readiness remains unresolved. | Sponsor and commercial owner; decide this week, request within ten days. | Recorded decision weighing $25,000 against losing a month of fallback. Do not assume the option can be recovered after expiry. |
| Classify all 600 exceptions by cause and dollar amount, prioritising high-value items; distinguish expected timing from missing, duplicate or incorrect postings. | Reconciliation lead with finance; initial analysis before next week's tests. | Dollar-balanced exception register, remediation owners, and finance-approved treatment of legitimate exceptions. |
| Replace percent-complete reporting with remaining acceptance work, dependencies, owners and estimates, including production bank-file ingestion. | Engineering lead; within seven days. | Credible route to cutover or evidence requiring a rebaseline. No extrapolation from nine closures per week. |
| Run and record production-like ingestion and partial-posting recovery, including interruption, safe replay, duplicate prevention and rollback. | Platform and application leads; prepare this week for finance testing. | Logs and reconciled balances demonstrating recovery; failures become release blockers with owners. |
| Reserve finance's two days for the highest-risk cases; name an empowered delegate for fixes and retesting after the lead leaves. Agree go/no-go authority and gates. | Finance lead and sponsor; this week. | Signed acceptance criteria, scheduled tests and available acceptance ownership through cutover. |

Adding engineers is not yet justified: the binding constraints may be classification, acceptance and integration rather than parallel coding capacity.

## What could change the recommendation

Documented benign exceptions, successful recovery and an owned acceptance plan could support the date. If required work cannot fit, or finance acceptance has no available owner, rate Red and change the commitment. Engineering is right that delay alone may not fix the data; any extension must carry these specific remediation and verification obligations.
