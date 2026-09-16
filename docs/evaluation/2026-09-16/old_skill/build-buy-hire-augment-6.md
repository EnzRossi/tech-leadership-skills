# Sourcing recommendation: independent storage-consistency review

**Recommendation: Use a specialist consultant for the one-week review, with the internal technical owner retaining the design and implementation decisions. Confidence: High on sourcing fit; scope and fee remain to be agreed.**

**FACT:** The need is short, independent expert judgment before implementation; the specialist expertise is absent internally, an internal owner can brief and act, no production data is required, and there is no hiring plan or deadline pressure. **INFERENCE:** This is a clear fit for a bounded consultant engagement. It is not a close internal-versus-external call: the required expertise and independence are not supplied by the current internal option.

## Capability and decomposition

| Component | Differentiation | Recommended model |
|---|---|---|
| Independent critique of the novel consistency design | Supporting judgment; differentiation of the underlying design is UNKNOWN | Specialist consultant for one week |
| Design decisions and implementation | Potentially differentiating; classification UNKNOWN | Existing internal technical owner acts on findings; no delivery outsourcing implied |

**INFERENCE:** Without the review, implementation would proceed with this specific expertise gap or wait. The cost of an undiscovered design flaw and any cost of delay are unknown; do not manufacture urgency to justify the engagement.

## Relevant dimensions

| Dimension | Rating | Evidence |
|---|---|---|
| Maturity | Novel | FACT: novel storage consistency design |
| Domain knowledge | Specialized industry knowledge | INFERENCE from the requested consistency review |
| Urgency | Flexible | FACT: no deadline pressure |
| Duration | Spike: one week | FACT |
| Requirement uncertainty | Partly defined | FACT: design review specified; exact questions and acceptance deliverables remain to be agreed |
| Internal skills | Absent for this specialty | FACT |
| Capacity to manage consultant | Present | FACT: internal owner can brief and act |
| Security/compliance | Controlled, subject to design confidentiality | INFERENCE: no production data access needed; intellectual-property requirements remain to confirm |
| Knowledge retention | Should be transferred | INFERENCE: the internal owner needs the reasoning to implement safely |
| Reversibility | Cheap, conditional on retained deliverables | INFERENCE: one-week advice engagement has no intended operational dependency |

**UNKNOWN:** Budget shape, internal delivery capacity, specialist availability, iteration frequency, integration detail and the underlying design's differentiation. These do not negate the review fit; the owner and procurement should settle the fee, availability, confidentiality and scope before contracting.

## Alternatives and neutrality

Hiring for this isolated one-week component is removed: the demand is a spike and there is no ongoing role defined. Internal review alone loses because the specialty is absent and independence is requested. Waiting for internal learning is possible, given no urgency, but does not deliver the same independent specialist judgment. Staff augmentation and an implementation agency provide delivery capacity where the need is a focused opinion. A product purchase does not replace a tailored review of a novel design.

The skill publisher sells engineering services. The external recommendation rests on two supported conditions: bounded duration, and absent expertise that is not established as a permanent internal role. **ASSUMPTION:** This specialist review need is genuinely one-off; revisit that assumption if the team repeatedly requires the same expertise.

## Scope, cost and transition

**Proposed scope:** The internal owner supplies the design, expected consistency guarantees, failure model, invariants and the open questions. The consultant challenges those assumptions and delivers concrete failure scenarios or counterexamples, unresolved questions, and prioritized recommendations with reasoning. Finish with a walkthrough in which the owner records disposition of every material finding. No production access is included.

**Cost drivers:** Consultant fee, internal briefing/review time and work needed to act on findings. No figures are supplied; obtain a capped one-week proposal. This is an advice decision, so a build lifecycle-cost model or hiring salary comparison would add little.

**Risk:** Advice becomes an unused report or creates false confidence outside the review scope. Mitigation: the owner agrees the review boundaries upfront and records accepted actions and residual unknowns. The review does not certify the whole implementation.

## Exit and decisions

Set the engagement's calendar end date before signature: one week after its agreed start. At six months and eighteen months there should be no recurring contract or dependency; the company retains the report, relevant supporting analysis and internal decision record. A clean exit requires confidentiality/IP terms and a handover the technical owner understands.

Change the recommendation if no credible specialist is available, the question expands into sustained delivery, no owner can act on the report, or recurring demand establishes a long-term internal expertise need. Leadership approves the capped fee and contract; the technical owner decides which findings to implement.
