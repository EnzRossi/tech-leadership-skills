**Earliest delivery is 9 elapsed working days from today**, assuming both activities succeed as stated.

Implementation and security review start together:

| Activity | Elapsed working-day interval |
|---|---|
| Implementation, including review/testing | Start through completion at day 5 |
| Security review from accepted design | Start through completion at day 8 |
| Cutover by available owner | After both complete, from day 8 to day 9 |

The calculation is **max(5, 8) + 1 = 9 working days**. If today is the start of working day 1, cutover completes at the end of working day 9.

The security review is the binding path. It can begin from the already accepted design, so it does not wait for implementation, and the two durations must not be summed as 5 + 8 + 1. The cutover cannot overlap the preceding work because it explicitly requires both to finish.

Implementation's review and testing are already included; no extra allowance is warranted. There are no stated resource conflicts or additional release tasks. More implementation staffing would not advance delivery while security still completes at day 8.

This is a deterministic earliest schedule, not a percentile estimate or guarantee of review approval. Under the supplied assumptions, no further discovery or contingency calculation is needed.
