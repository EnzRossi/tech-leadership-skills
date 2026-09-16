# AI Initiative Evaluation: claims intake and triage

Prepared 16 September 2026 for the CTO and board strategy discussion. Origin: claims team proposal.

## Executive recommendation

**Recommendation: Research further for a human-assisted workflow; do not approve autonomous severity classification and routing in the proposed form. Confidence: Medium.**

**FACT:** The team handles roughly 3,000 claims weekly at six minutes each. **INFERENCE:** That represents about 300 hours of intake effort a week, a material opportunity, but neither net savings nor safety has been established. Recommend two weeks of user discovery, data inspection, and evaluation design before authorizing a prototype; the sponsor must supply the budget cap.

## The problem, stated without the technology

**FACT:** Fourteen people manually read claims emails and attachments, extract fields, determine severity and assign queues. Four years of historical assignments and outcomes exist on-premises and include personal health information. **UNKNOWN:** Baseline error rates, delays, actual labor cost, and the share of those 300 hours that can be removed rather than shifted into review.

**Proposed success outcome, for sponsor confirmation:** reduce total intake-and-correction time by at least 30% while preserving or improving urgent-claim identification and routing accuracy. This is a suggested target, not a measured result or a headcount commitment.

## Is AI the right tool?

**INFERENCE:** Unstructured correspondence makes extraction and classification plausible AI tasks. Start with a deterministic baseline: structured intake where feasible, OCR/template extraction, required-field checks, and a claims-owned routing decision table. AI must outperform that baseline on net time and quality. Retain deterministic routing controls and human severity decisions until evidence supports anything further; no agent is needed.

## Classification

| Item | Finding |
|---|---|
| Automate or augment | Proposed routing is automation. Recommended variant augments intake staff and adjusters, with source-visible review before action. |
| Cost of being wrong | High: insurance and health-related information; under-triaging urgent cases can be more harmful than over-escalating. Compliance must assess applicable obligations. |
| Shape | Fixed workflow for document handling, extraction and suggestions, with deterministic checks. Primarily predictive/classification, not open-ended generation. |

## Assessment

| Dimension | Rating | Evidence and remaining need |
|---|---|---|
| Business value | Adequate | FACT: volume and time quantified approximately; UNKNOWN: total lifecycle cost and recoverable capacity. |
| Strategic fit | Adequate | INFERENCE: improves important claims operations; competitive differentiation is unproven. |
| User desirability | Unknown | FACT: claims head enthusiastic, adjusters unconsulted. Interview intake users and adjusters. |
| Technical feasibility | Unknown | No representative performance evidence supplied. Test extraction, severity and routing separately. |
| Data readiness | Unknown | FACT: historical records exist; no inspected sample, access approval or assessment of label fidelity. Final assignments may differ legitimately from initial routing. |
| Evaluation readiness | Unknown | Historical outcomes are candidates for labels, not agreed triage ground truth. Have two adjusters independently judge the same cases. |
| Operational readiness | Unknown | No production owner, review capacity, monitoring or incident plan supplied. |
| Risk and compliance | Weak | FACT: PHI and insurance workflow; no assessment or approved processing design supplied. |

## Risk assessment

| Risk | Likelihood / impact | Proposed mitigation and owner |
|---|---|---|
| Urgent cases under-triaged | Unknown / high | Claims lead defines severity errors and escalation; reviewer sees source evidence and can override. |
| PHI leakage | Unknown / high | Security/privacy owner approves data access, runtime boundary, logs, retention and any vendor use before real-data work. |
| Historical-label mismatch | Unknown / high | Adjusters construct intake-time labels without later information; data lead inspects hard and recent cases. |
| Review erases savings | Unknown / material | Operations measures reading, checking, correction and rework time, not model latency alone. |

## Biggest unknowns and questions before a prototype

1. Do intake staff and adjusters agree on the problem, desired workflow and acceptable errors? Claims head arranges at least three user conversations within week one.
2. Can historical inputs be joined reliably to valid intake labels and used for this purpose? Data lead and privacy owner inspect a permitted sample and approve access within two weeks.
3. What constitutes a correct severity and route, and who owns review and production operations? Claims experts and CTO agree definitions, owners and review capacity before funding a prototype.

## Recommended next experiment

**Proposal:** A two-week discovery and judging-set exercise led jointly by a claims operations lead and technical lead. Inspect 50–200 authorized historical examples covering document types, recent changes and difficult cases. Have two adjusters independently label an initial 20 cases, reconcile disagreements, and separate evaluation cases from development cases. Compare the current manual process and deterministic baseline on the same material.

**Proposed gate:** At least 90% initial expert agreement on severity and routing, followed by adjudicated labels and documented policies for the remainder; confirmation from users that source-visible review fits their work; approved access and feasible cost envelope. Stop or return to process redesign if labels cannot be agreed, access is refused, or the simpler workflow captures most value.

A subsequent prototype could target at least 30% lower net handling time, at least 95% routing agreement, and at least 99% recall for urgent claims, with no observed critical misses in the sampled evaluation. These are sponsor-review proposals, not proof of safety: the rare urgent cohort needs a separately justified evaluation size before live exposure. Do not start a live pilot until evaluation readiness is adequate.

## Lifecycle costs and approvals

Estimate secure hosting/inference, extraction pipelines, integration, expert labeling, full reviewer time, monitoring and drift, re-evaluation on model changes, privacy review, training and decommissioning. Finance and engineering supply the cost envelope; no monetary savings are established.

Privacy/security approves regulated-data use; CTO and claims sponsor approve each stage's capped budget and thresholds; claims leadership approves any customer-impacting exposure or reduction in review. Leadership retains staffing and vendor-contract decisions. Present the board with this gated evidence plan next month, rather than a production promise.

**ASSUMPTION:** An advisory workflow can be piloted without modifying claims decisions or the system of record; confirm with the claims owner.
