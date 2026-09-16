Release is feasible on **working day 8 with 1, 2 or 4 engineers**. Extra engineers bring acceptance forward but do not bring release forward because access is the controlling dependency.

Human effort is `4 × 6 + 12 = 36 productive hours`, or `36 ÷ 6 = 6 engineer-days`. Unattended agent runtime totals `4 × 2 = 8 hours`; it is elapsed runtime, not additional human effort. Business acceptance adds one working day.

A feasible schedule, using overnight agent runs:

| Engineers | Independent slices | Integration, one engineer | Business acceptance | Release |
|---|---|---|---|---|
| 1 | One slice each on days 1–4; each runs afterward and is ready by the following morning | Days 5–6 | Day 7 | Day 8 |
| 2 | Two slices on day 1, two on day 2; final runs finish before day 3 | Days 3–4 | Day 5 | Day 8 |
| 4 | All four slices on day 1; runs finish before day 2 | Days 2–3 | Day 4 | Day 8 |

The two-hour runs fit overnight, and integration needs `12 ÷ 6 = 2 working days` regardless of headcount because it is assigned to one engineer. This schedule assumes release itself has no separately specified duration and can occur once access arrives. More people buy recovery time before day 8: one engineer has no full spare working day after acceptance, versus two with two engineers and three with four.
