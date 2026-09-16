**Production in 10 working days is not viable for 1, 2 or 4 developers under the stated dependencies.** Reset the commitment and calibrate the risky integration. Coding agents do not remove certification or establish payment correctness.

Using elapsed working days from project start, access takes 7 days. Let **I > 0** be time from access to complete sandbox integration. Certification then takes a quoted 5 days:

**Production duration ≥ 7 + I + 5 = 12 + I working days.**

That already exceeds 10, even if every other requirement is ready. Certification cannot overlap incomplete sandbox integration. Rejections, queue delays and remaining release work could extend this bound; the vendor quote is not a guarantee.

Keep the production acceptance bar constant. Assume the requested 1/2/4 scenarios mean full-time engineers and instant hiring, while domain transfer and coordination still take attention.

| Staffing | Maximum 10-day capacity | Useful allocation | Delivery bound |
|---|---|---|---|
| 1 full-time | 10 engineer-days | Senior owns design, integration, review, acceptance and operations; agents limited by owner capacity | ≥12 + I₁ days |
| 2 full-time | 20 engineer-days | Senior owns ledger/provider decisions; second owns independently specified failure tests and delivery tooling | ≥12 + I₂ days |
| 4 full-time | 40 engineer-days | Domain/integration, payouts, verification, release/operations owners; up to four independent agent streams | ≥12 + I₄ days |
| Actual: 1 full-time + 1 half-time | 15 engineer-days | Senior remains bottleneck; half-time engineer supplies verification/integration support | ≥12 + I_actual days |

These are capacity bounds before coordination, not project effort estimates. The actual team is **1.5 human FTE**. If added developers also work part-time, recalculate availability. More engineers may shorten implementation and verification, but the unknown integration duration cannot be divided by headcount, and four agents are not four additional human FTE.

There is insufficient scope or measured throughput for a defensible total effort range. Production acceptance must cover balanced ledger postings, auditable corrections and reconciliation; duplicate requests/webhooks and idempotency; out-of-order events; timeouts after provider success; retries and partial failure; rejected/returned payouts; authorization and recovery. Independently specify expected outcomes, automate repeatable checks and require accountable human review of money-moving logic and execution evidence. Include agent review, finding triage, fixes and reruns. Three manual happy paths can supplement this evidence, but cannot replace it. Startup status does not reduce the impact of incorrect balances or duplicate payments.

As an explicitly proposed **discovery timebox**, spend 1–2 senior engineer-days before access defining provider contracts, acceptance rules and a representative ledger-to-payout slice; prepare fixtures and tests during the access wait. This is an engineering-judgment allocation, not an estimate for finishing integration. After access, complete that slice through reconciliation and failure handling, record human steering/review/fix time and agent runtime, and reforecast at its acceptance boundary.

A separately scoped mocked demonstration might fit day 10; it must not move real money or be described as certified production. Production technical feasibility remains conditional on integration, certification and acceptance, with a named reconciliation/support and incident owner. Business viability is unproven without value, budget and operational assumptions. Human effort, agent/CI use, review and ongoing support are cost drivers; rates are absent, so no money estimate is justified.

The CEO should reset the promise, and the senior engineer should own calibration and release evidence. Confirm the production ledger/payout scope and the provider's precise gate timing before issuing a new date.
