# Sourcing decision: Storage consistency design review

## Recommendation

**Confidence: High in using a specialist consultant; individual suitability remains to be verified.**

Yes. A one-week independent specialist review fits the reported need: a specific expertise gap, a bounded decision before implementation and an internal technical owner who can brief the reviewer and act on findings. No production data is needed. Deadline pressure and a hiring plan are not prerequisites for outside expertise. Commission a focused review once the candidate's relevant expertise, independence and deliverable are clear.

## Why this choice

| Capability | Solution + delivery route + long-term owner | Decisive evidence |
|---|---|---|
| Independent assessment of the storage consistency design | Obtain specialist advice; retain design and implementation internally. The existing technical owner owns the decision and follow-through. | Your report establishes a one-week review need and no internal specialist reviewer. A recipient able to act is already available. |

This is a choice about obtaining judgment, not whether to buy or build the storage system. A project agency or staff augmentation arrangement would introduce unnecessary delivery scope unless the review exposes a separate implementation need.

The strongest competing option is internal study followed by internal review. With no deadline pressure, that may build valuable knowledge, but it does not yet supply the specialist expertise or independence requested. Prefer it if the owner can demonstrate equivalent expertise and an appropriately independent reviewer at acceptable effort. There is no reason to apply an automatic internal tie-break.

Hiring is not justified for this isolated one-week need without evidence of a durable role. Proceeding without a specialist review saves the fee but leaves the stated expertise gap unresolved before an implementation decision. Postponing preserves flexibility but contributes no evidence unless the team uses the time for a defined learning or validation activity.

## Cost, transition and exit

Compare the consultant and internal-learning alternatives against the same outcome: a useful independent assessment before implementation, not merely a week of labor. Consultant fees are unknown; include briefing, preparation, internal discussion, findings triage and any agreed clarification. For the internal alternative, include study time and the opportunity cost of taking the technical owner away from other work. Existing salary does not make that effort free, and no rates or cost advantage have been established.

Scope the deliverable to the design's consistency claims, assumptions, concrete failure scenarios, trade-offs and a reproducible test plan. Require evidence and uncertainty for each finding, plus a walkthrough with the owner. Novel designs may require experiments beyond a one-week review; the reviewer should identify those limits rather than promise proof of correctness.

No production data access is needed, which removes one access dependency, but design materials still need an appropriate sharing arrangement. Keep implementation authority with the internal owner. The review ends when findings have been explained, challenged and accepted for disposition, and the owner can run or commission the proposed tests. Documents alone are insufficient if the findings cannot be acted on. Further consulting should depend on an explicit unresolved question, not automatic renewal.

## Next action

Have the internal technical owner prepare a short review brief containing the design, claimed guarantees, failure model and key unanswered questions, then assess a specialist's closely relevant work and independence. The human decision is a bounded one-week engagement with the above acceptance criteria; no vendor contact or spending has been executed here.

## What could change the recommendation

The strongest objection is that a short external review may miss implicit system context. A good briefing and walkthrough reduce that risk. If the design cannot yet be explained well enough to review, first improve the design artifact; if no suitably qualified independent specialist is available, reconsider the review route. Neither uncertainty justifies defaulting to internal review without the expertise it requires.
