**A working demo does not establish pilot readiness.** The pilot needs agreed answer-quality criteria, a current-policy source process and an accountable support/escalation owner. Without those, there is no defensible full delivery date for either staffing option.

As a proposed engineering-judgment allocation, timebox **two working days** with a technical lead and available policy/support decision-maker to define a bounded pilot: permitted topics/users, authoritative policy versions, independently specified evaluation cases, an accepted error threshold and escalation destination. This is discovery, not a promise to make the pilot ready. If no owner is available, that decision remains a release gate.

| Staffing | Useful work division | Pilot schedule implication |
|---|---|---|
| 1 senior | Sequentially develops evaluation harness, retrieval/citation behavior, escalation and operational evidence while steering agents | Longer human critical path; duration unknown until acceptance and a measured slice exist |
| 2 seniors | One owns current-policy retrieval/citations; one owns independently specified evaluations, unsupported-question escalation and instrumentation | Can overlap independent implementation, but shared acceptance decisions and final integration remain serial |

Agents writing code are separate from the LLM feature being evaluated. Agentic code review, fix/rerun cycles and browser checks do not measure answer correctness. Evaluate supported questions for faithful quotations and correct sources, outdated/conflicting policies, unsupported questions that must escalate, retrieval failures and misleading source content. Include human-reviewed cases and execution evidence; tests invented solely by the implementation agent may repeat its mistakes.

Calibrate one end-to-end slice that answers from a current policy and escalates an unsupported question to the named owner. Measure active steering/review/fix time separately from agent runtime, then estimate remaining coverage, policy-update handling, escalation operation and limited rollout. Do not halve the duration for two engineers or infer reliability from the generated demo.

Recommend a narrowly scoped pilot only after its threshold is met and support ownership exists. The sponsor should appoint that owner and approve the error tolerance; those decisions, plus the accepted slice, trigger the readiness forecast. Staffing and agent usage create costs, but rates and operating volume are absent.
