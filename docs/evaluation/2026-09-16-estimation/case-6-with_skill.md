**Reviewer capacity is the demonstrated bottleneck; two more implementers do not improve the current acceptance bound.**

Each PR needs **45 minutes = 0.75 reviewer hours**. The reviewer can accept at most **3 ÷ 0.75 = 4 PRs/day**. For 24 PRs, review alone requires **24 × 0.75 = 18 hours**, or **18 ÷ 3 = 6 working days** at current availability. Generation capacity is 12 PRs/day, so its aggregate floor is **24 ÷ 12 = 2 days**. These bounds overlap; do not add them as eight days automatically.

| Change | Review throughput | Review-only duration floor |
|---|---|---|
| Add two implementers; reviewer unchanged | 4 PRs/day | 6 days |
| Increase reviewer to 6 hours/day | 8 PRs/day | 3 days |
| Supply 9 qualified reviewer-hours/day | 12 PRs/day | 2 days, matching generation capacity |

The last option likely requires another qualified reviewer; it is a capacity scenario, not an overtime recommendation. Extra reviewers need domain context and consistent acceptance criteria.

These are **lower bounds, not feasible finish promises**: first-PR arrival, review findings and schema approval timing are unspecified. Two PRs cannot start until the schema is approved. Prioritize that approval and work on the other 22 in parallel. If schema approval consumes the same scarce reviewer and is outside the 24 × 45-minute allowance, add that effort to her capacity schedule. Late approval can extend every scenario.

Throttle work in progress around acceptance capacity. Agent review can triage issues but does not replace the required domain review. Confirm whether 45 minutes includes fixes/reruns and final acceptance; otherwise estimate them explicitly. With no escaped-defect history, throughput says nothing reliable about production quality. Observe the first accepted batch, fixes and schema timing before committing a delivery date.
