# AI initiative methodology

EnzRossi's editorial synthesis of the sources in [sources.md](sources.md), not a validated scoring instrument. Read "Readiness" and "Evaluation contract" for investment decisions; use the remaining sections as relevant.

## Readiness

Use Supported / Concern / Unknown if labels help. Supported means evidence sufficient for the proposed next stage, not proof of production suitability. Do not print a full rubric by default.

| Area | Evidence that changes the decision | Common false positive |
|---|---|---|
| Business and user value | Current pain, task volume, avoidable effort/error, user workflow, adoption incentives, benefit owner | Sponsor enthusiasm; hours saved assumed to equal payroll savings |
| Strategic relevance | Connection to a stated priority; consequence of delay; advantage worth owning | Commodity confused with low value; board demand confused with customer need |
| Data readiness | Accessible inputs linked to outcomes; permission for this use; representative coverage; signal available at decision time | "Four years of history" without raw inputs; final outcomes used as input features; rejected cases missing |
| Feasibility | Candidate compared with current process and simplest credible alternative on this task | Vendor benchmark or curated demo treated as task evidence |
| Evaluation readiness | Agreed judging rubric, cases and denominators, threshold rationale, trusted adjudication | An average accuracy percentage with no costly-error breakdown |
| Integration and operation | Access to source of truth; latency budget; retries/fallback; owner, review capacity, observability, incident response, model-change re-evaluation | Low token cost treated as low total cost; no production owner |
| Risk containment | Data minimization and access boundaries; tested handling of mistakes, misuse and adversarial inputs; ownership of remaining risk | Human-in-the-loop asserted without testing reviewer detection or workload |

Check maintenance of prompts, models, data pipelines, connectors and evaluation cases. Include vendor dependence, training, support, log retention, and decommissioning only where material. Quantify whole-workflow costs from supplied estimates; otherwise identify the dominant missing driver.

## Evaluation contract

A contract here is an acceptance plan agreed by the decision maker, not a legal document. Keep its decisive parts in the memo.

1. **Unit and baseline.** Define the unit of success (claim routed correctly, question resolved, tool task completed). Compare the current workflow, strongest simple alternative, and candidate on equivalent cases and permissions. For copilots compare human-plus-tool with human alone, including correction time. For forecasts use an appropriate naive or statistical baseline.
2. **Cases and leakage.** Sample real workload across normal, ambiguous, missing-input, out-of-scope, rare costly errors and adversarial cases. Keep representative prevalence evaluation separate from stress testing. Reserve untouched cases before tuning. Split by time, customer, document family or entity when random splits would leak related examples. Historical decisions may reflect old policy, bias, or incomplete information; inspect raw input availability and label validity.
3. **Judging.** Use executable checks for exact fields or state, qualified reviewers for domain judgment, and adjudication of disagreement. Give reviewers the same rubric; inspect disagreements before declaring labels reliable. An LLM judge can help after calibration against human decisions; it is not its own ground truth. Evaluate retrieval evidence and grounded answers separately when retrieval can fail.
4. **Measures and gates.** Use task success and error severity, not a universal accuracy target. For classification, separate false positives and negatives, per-class recall/precision and abstention coverage. For generative outputs, assess factual support and task completion. For agents, verify final state, permission compliance, repeated actions, retries, tool failures and escalation, across multiple trials where behavior varies. Report end-to-end latency (including tail latency), availability, review burden and cost per successful task when they constrain value. Averages must not hide an unacceptable slice.
5. **Threshold justification.** Start from the consequence of error, incumbent performance and sponsor tolerance. Mark thresholds as supplied, measured or proposed; explain proposed trade-offs. Report numerator/denominator and uncertainty. Zero observed catastrophic errors in a small sample is not proof of safety. Do not prescribe a universal 50–200 case sample or acceptance rate; size the evidence to the decision and rare-event exposure. A small discovery set can expose failure modes but cannot certify low risk.
6. **Exposure and regression.** Specify shadow, review-only or bounded live operation; accountable owner; human approval boundary; fallback; stop/rework conditions; and evidence needed to expand. Define logs sufficient to investigate failures while protecting sensitive data. Re-evaluate on model, prompt, tool, source-data or policy changes. Feed production failures into regression cases without treating the tuned suite as a fresh test.

## Stage gates

| Next commitment | Minimum rationale | What it does not authorize |
|---|---|---|
| No AI / process repair / postpone | Simpler option is sufficient; benefit not worth effort; or no feasible containment/access path | An obligatory AI experiment |
| Investigate | A specific missing problem, adoption, data or ownership fact can change the decision | Treating the proposal as funded |
| Prototype | Plausible value; permitted usable inputs; bounded technical question and way to judge progress | Live consequential actions |
| Controlled pilot | Relevant offline evidence; credible evaluation contract; bounded exposure and staffed fallback | Broad deployment or assumed savings |
| Staged production | Pilot evidence supports this population and workflow; residual risk accepted; operating ownership, monitoring and rollback ready | Expansion to materially different users or autonomy without re-evaluation |

Stages can overlap for separate components. A blocker in one proposed data use does not prohibit safe discovery elsewhere. A pilot with positive signals but no control may justify conditional expansion; describe the attribution gap rather than saying criteria were met when none were supplied.

## Worked example (fictional)

A support leader reports 600 daily shipment-status emails and estimates four minutes each. The tracking API already has authoritative status. A vendor proposes an autonomous reply agent.

**Recommendation:** test a tracking link and deterministic reply for identifiable orders first. Reported volume and estimated handling time suggest potential effort to recover, not proven savings. The remaining uncertainty is how many emails require interpretation or a service decision. Sample those exceptions; if they justify it, test extraction or drafting with verification against the tracking API. Wrong-recipient disclosure and incorrect status are different failures; evaluate both. Set any reduction target after measuring baseline and acceptance with the service owner. Do not fabricate savings or a target from this example.
