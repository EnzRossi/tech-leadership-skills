All three teams can release at the **start of working day 8**, assuming release has no additional duration. Extra engineers finish acceptance earlier but cannot move the access gate.

Human effort is **4 × 6 + 12 = 36 active hours**. The **4 × 2 = 8 aggregate unattended agent hours** overlap overnight with human downtime; they are not extra human hours. Steering, review, fixes and manual slice acceptance are already included.

| Engineers | Slice work | Integration, one engineer | Business acceptance | Release |
|---|---|---|---|---|
| 1 full-time | One slice/day on days 1–4; two-hour run after each | Days 5–6 | Day 7 | Start day 8 |
| 2 full-time | Two slices/day on days 1–2; runs after each | Days 3–4 | Day 5 | Start day 8 |
| 4 full-time | Four slices on day 1; runs that evening | Days 2–3 | Day 4 | Start day 8 |

Each engineer spends at most six productive hours/day. Integration begins after the final agent runs complete and takes **12 ÷ 6 = 2 working days**. Business acceptance then takes one working day, with its owner assumed available. One engineer can cover every engineering role; no time is double-booked.

Access is obtained independently and ready at the start of day 8. Release is the later of access readiness and acceptance completion. These are deterministic schedules using supplied durations, not confidence ranges. Two and four engineers provide two and three spare working days before release, respectively; one engineer has no spare working day. Additional staffing helps absorb implementation overruns but cannot shorten serial integration or the fixed access gate. An access delay shifts every release; failed acceptance requires reforecasting. No budget figures are included.
