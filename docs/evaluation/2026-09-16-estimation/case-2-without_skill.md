**A production commitment in 10 working days is not credible with 1, 2 or 4 developers.** Seven working days for sandbox access plus five working days for certification already means at least 12 working days, even pretending sandbox integration takes no time. Certification actually follows a completed integration, so the real dependency chain is longer. Coding agents cannot shorten those external waits.

For an initial planning estimate, assume a narrow single-provider ledger and payout service, an existing deployment platform, and experienced developers. The ranges below are judgment estimates, not measured delivery rates; the unfamiliar API and missing reconciliation tests make confidence low.

| Work | Productive developer-days |
|---|---:|
| Before sandbox: ledger design, invariants, implementation and provider adapter against mocks | 8–12 |
| After sandbox: integration, reconciliation, failure/retry handling, verification and operational readiness | 10–18 |
| Total implementation and verification | **18–30** |

Allow another five working days for certification and one to two for production activation and verification. Some work can move across the sandbox boundary once requirements are known.

To avoid assuming perfect headcount scaling, use effective throughput of 1, 1.6 and 2.4 developer-days per day for teams of 1, 2 and 4 full-time humans. These are explicit planning assumptions reflecting shared design, review and integration dependencies—not claims about AI productivity.

The schedule model is `max(7, ceil(before-sandbox effort / throughput)) + ceil(after-sandbox effort / throughput) + 5 + (1 to 2)`:

| Full-time humans | Illustrative working-day range | Ten-day production commitment |
|---|---:|---|
| 1 | `8 + 10 + 6` to `12 + 18 + 7` = **24–37** | No |
| 2 | `7 + 7 + 6` to `8 + 12 + 7` = **20–27** | No |
| 4 | `7 + 5 + 6` to `7 + 8 + 7` = **18–22** | No |

Your current staffing is **1.5 nominal full-time equivalents**, not two full-time developers. Using a provisional effective throughput of 1.3 gives about **21–31 working days**. Availability windows and who owns integration could stretch this further. Certification findings or a provider delay are outside these ranges.

Three manual happy-path tests cannot establish that money remains correct after duplicate requests, concurrent payouts, timeouts, partial failures or replayed webhooks. The minimum release scope should include automated ledger balance and reconciliation checks, idempotency, retry and failure tests, authorization checks, traceable transactions, and a tested procedure to stop payouts and recover safely. Agents can help implement these; agent review does not establish their correctness independently.

Reset the CEO commitment now: day 10 can target a demonstrable, limited sandbox milestone, conditional on access and initial integration results. Spend the first one to two days validating the provider contract, certification prerequisites and ledger invariants, then replace these provisional effort ranges with task-level estimates. More developers can shorten implementation; none make the external gate fit ten days.
