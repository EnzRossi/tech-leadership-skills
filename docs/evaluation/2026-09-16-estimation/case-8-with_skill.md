**Give the demo priority where urgency matters, but retain human verification for the permission refactor.** Business importance and failure consequence are separate: an investor demo may be urgent while a tenant-permission mistake can disclose another customer's data.

There is insufficient scope or accepted-throughput evidence to assign credible delivery durations. As a proposed allocation, spend **half a working day** agreeing the demo's supported paths and the refactor's access rules, then estimate accepted increments from those boundaries.

| Work | Acceptance and staffing |
|---|---|
| Synthetic-data investor demo | One engineer can own a narrowly scripted flow, agent review/fixes and targeted human checks of the main path, unsupported inputs and presentation failures. Confirm synthetic data stays synthetic and label demo limitations. |
| Tenant-permission refactor | The second engineer can define and execute permission tests and implementation; reserve qualified human review of authorization logic, cross-tenant denial, role boundaries and regression evidence before release. |

Both engineers may pair briefly for domain review; schedule that time rather than counting the same hour in both streams. Agents can implement and run tests concurrently, but generated tests need independently specified access expectations. A clean automated review is not sufficient evidence of tenant isolation.

If the demo consumes both engineers, explicitly defer the refactor release and its remaining work. Do not ship the refactor by reallocating all of its human verification time to the demo. That is the useful scope/date trade-off.

The product owner should define the demo deadline and minimum supported scenario. The permission owner should approve the access matrix and release evidence. Re-estimate after one representative accepted change for each; additional urgency can change allocation, not eliminate necessary verification.
