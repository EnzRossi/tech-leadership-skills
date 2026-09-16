# AI initiative decision: Supplier bank-detail changes

## Recommendation

**Confidence: High that rollout is not justified by the supplied evidence.**

Do not roll out this workflow. Your test reports zero wrong changes out of 200, but every case was used during prompt development and the model judged itself. This is not independent evidence of deployment safety. The approval screen also prevents staff from checking the source, so “human approval” has not been demonstrated as an effective control. The next commitment should be process and evaluation repair, with no live bank-detail changes by the agent.

## Decisive evidence

The supplied test has two known weaknesses: contamination of the test set and uncalibrated self-judgment. These are separate from the unknown true error rate. Even zero independently verified errors in a representative small sample would not prove the absence of rare harms. Here, the sample cannot support a defensible production error bound at all.

A wrong or unauthorized bank-detail change could redirect supplier payments, cause financial loss and interrupt a supplier relationship. Reversing the database change may not recover money already paid. Correctly extracting an account number from an email also does not establish the sender's authority or the change's legitimacy.

Your described reviewers see only an agent summary. They cannot reliably detect omitted warnings, altered account numbers or a misleading source through that screen. They need source access, authority and time to stop a change, and their performance must be tested. Source visibility alone will not authenticate a fraudulent request.

The strongest alternative is a controlled supplier-change process: authenticated requests or verification through an independently established supplier contact, exact field validation, appropriate approval separation and an auditable change record. If there is residual clerical work worth addressing, evaluate read-only extraction or draft preparation within that process. Neither the business benefit nor a need for agentic bank-write access has been established.

## Good enough for the next stage

Define success as the correct, authorized final bank-detail state, with no unauthorized changes, including after retries and failures. Keep prompt-development examples as regression cases. Create a new untouched set of representative requests, separated from related supplier/email threads used in development. Separately stress-test spoofing, compromised-looking conversations, embedded instructions, conflicting attachments, duplicate requests, ambiguous beneficiaries, missing verification and tool failures.

Have qualified payment-control staff establish and adjudicate expected authorization decisions independently. Compare the existing controlled process, deterministic assistance and any proposed read-only AI workflow. Exact state checks must confirm account details, permissions and absence of duplicate writes. An LLM judge could assist only after calibration against independent judgments.

Measure unauthorized actions, wrong beneficiary/account changes, missed fraud indicators, appropriate escalation, reviewer detection and correction rates, review time, and cost per correctly completed request. Test the entire interface and operational workflow. The accountable payment-risk owner must agree tolerable residual risk and required evidence before an evaluation can pass; no universal accuracy floor or convenient sample size is defensible. Rare-harm evidence must match expected exposure, and any unauthorized mutation in testing should trigger investigation and rework.

## Next commitment

Propose one bounded control-design review, owned by the payment-operations lead with security and engineering, ending with a verified change process, redesigned review screen and independent evaluation plan. Use synthetic or otherwise permitted data and a sandbox without live payout writes. Advance only to read-only/shadow testing if the control boundary and judging are credible. Retain the controlled manual process as fallback. Do not fund broader agent autonomy without a separate demonstrated benefit and authorization decision.

## What could change the recommendation

Independent held-out evidence could support a constrained assistive tool after controls are repaired. It would not retroactively validate the 200-case result. The strongest counterargument is substantial clerical savings, but no measured volume or handling-time evidence was supplied, and savings cannot substitute for authorization controls.
