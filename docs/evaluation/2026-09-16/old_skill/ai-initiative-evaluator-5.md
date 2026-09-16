# AI Initiative Evaluation: supplier bank-detail changes

Prepared 16 September 2026 for the rollout decision.

## Executive recommendation

**Recommendation: Do not use AI in the proposed autonomous form. Confidence: High.**

**FACT:** All 200 cases were used in prompt development, and the model judged its own answers. **INFERENCE:** Zero reported errors on that set does not establish unseen-case accuracy, much less safe operation for high-impact payout changes. Keep changes in the existing verified process; redesign the authorization control and independent evaluation before reconsidering an advisory tool.

## Problem and strongest alternative

**ASSUMPTION:** The business wants to reduce manual effort in processing legitimate supplier banking changes. **UNKNOWN:** Volume, handling cost, fraud history and expected benefit; the user supplied no quantified business baseline.

**INFERENCE:** Bank-detail changes require exact, auditable authorization. The strongest alternative is a structured change request with authenticated supplier confirmation through a previously trusted channel, deterministic account/identity validation, and appropriately authorized human approval. AI may help extract a proposed change; it cannot establish that the sender is entitled to make it. An email alone should not serve as that authorization.

## Classification

| Item | Finding |
|---|---|
| Automate or augment | Effective automation: a glance at a summary without source access cannot independently verify the proposed action. |
| Cost of being wrong | High: a false approval can divert funds and may be hard to reverse. False rejection or delay is generally the safer failure, subject to the business's obligations. Regulatory category requires compliance review. |
| Shape | Agent unjustified; a fixed extraction-and-validation workflow would suffice for an advisory alternative. |

## Assessment

| Dimension | Rating | Evidence |
|---|---|---|
| Business value | Unknown | No volume, cost or delay baseline. |
| Strategic fit | Unknown | No strategic case supplied; likely supporting operations is only an inference. |
| User desirability | Unknown | No user evidence beyond the proposed glance-review workflow. |
| Technical feasibility | Weak | FACT: development examples and self-judgment are the only evidence. |
| Data readiness | Unknown | Representativeness, rights and coverage of fraudulent or ambiguous requests are unexamined. |
| Evaluation readiness | Weak | No independent held-out cases or independent ground truth. |
| Operational readiness | Weak | FACT: reviewers cannot see the original; effective oversight is absent. Monitoring and rollback are unknown. |
| Risk and compliance | Weak | Proposed high-impact action lacks a credible preventive control in the information supplied. |

## Risks and next step

**INFERENCE:** Evaluation leakage and correlated judging errors can hide failures; even a genuinely independent small test with no errors would not prove zero risk. High-impact, rare failures require explicit tolerance and an evaluation design that can support it. Do not infer a rollout error rate from this result.

**Proposed next step:** Over two weeks, the payments-control owner and security lead document the current authorization process and rebuild the verification screen to show the original request, existing trusted supplier details, exact before/after values and independently obtained authorization evidence. No tool gets bank-detail write permission in this exercise. Budget is unknown and must be capped by the sponsor.

If there is still a business case for AI assistance, build an independently labeled held-out evaluation first, separated from prompt development. Include impersonation, compromised-email scenarios, conflicting instructions, malformed attachments, ambiguous account numbers and instructions embedded in documents. Domain reviewers, rather than the generating model alone, determine correctness. Compare against the verified manual and deterministic processes on both accuracy and full review time.

**Proposed acceptance criteria:** Every proposed change requires verifiable authorization through the trusted process; unauthorized or ambiguous requests produce no change; reviewers can detect seeded summary/source mismatches before approval. Any unauthorized mutation, inaccessible source evidence, or bypass of verification stops the exercise. The risk owner must specify the tolerable harmful-error rate and evaluation size before considering operational exposure; a blanket 100% score on a small set is insufficient.

## Information and approvals needed

**UNKNOWN:** Who owns bank-change controls, acceptable residual risk, case volume and fraud exposure, reviewer staffing, and incident/reversal capability. The finance/payments owner and security lead must answer these before any revised pilot.

Leadership approves spend; finance's authorized control owner approves any bank-change workflow; security/compliance approves data processing and access; any production write access or removal of review returns for explicit authorization with independent evidence. Lifecycle costing can wait until the business case and safe workflow exist.
