# AI initiative decision: Claims triage

CTO · Evidence: supplied CTO account

## Recommendation

**Confidence: Medium in investigating; low in production value until workflow and data are checked.**

This warrants a bounded investigation, with an offline prototype conditional on usable, permitted data. Do not approve a live pilot yet. The reported workload makes triage a credible opportunity, but historical assignments, sponsor enthusiasm and the board deadline do not establish accuracy, adoption or savings. Start with claims staff and adjusters, a data-access check and a baseline; take that investment hypothesis and its gates to the board next month.

## Decisive evidence

- Your figures imply 3,000 claims/week × 6 minutes = 18,000 minutes, or **300 staff-hours/week** of reported triage effort. That is potential capacity to recover, before review, exceptions and operating effort; it does not establish cash savings or that 14 roles can disappear.
- Four years of final assignments and outcomes are candidate labels. It is unknown whether the original emails and attachments remain accessible and linked, whether assignments reflect current routing policy, or whether severity was knowable at intake. Later outcomes must not become intake features. Claims experts should adjudicate ambiguous and outdated labels.
- On-premises health information makes permitted access, processing, logs and retention binding design questions. On-premises storage alone establishes neither permission nor a requirement to run every component locally. Adjuster participation and a production owner remain unknown; the head of claims' support is useful but insufficient.

The strongest simpler option is structured intake plus deterministic extraction, field validation and routing rules, with manual exceptions. Compare that with the current process before assuming an LLM is needed. Interpretation of varied narrative and attachments may justify generative extraction; severity classification could use rules or predictive ML. Keep identifiers, queue permissions and routing validation exact. A fixed assistive workflow is the initial candidate; nothing supplied requires an autonomous agent.

## Good enough for the next stage

Use a claim with its intake materials as the evaluation unit. Compare human-only triage, the simpler workflow and human-plus-candidate on equivalent cases, including correction time. Reserve untouched cases before tuning; split by time and related claim/customer groups to avoid leakage. Cover routine volume, document types, missing attachments, ambiguous severity, unusual claims and misleading document instructions. Keep rare-error stress tests distinct from prevalence estimates.

Qualified adjusters should independently label and adjudicate disputed cases; use exact checks for extracted fields. Measure routing correctness, critical-field errors, severe-claim false negatives and false positives, abstention coverage, review workload, end-to-end latency and cost per successfully triaged claim. Under-triage can delay urgent handling; wrong routing can delay service or expose information to an inappropriate queue. Reviewers need original evidence, time and authority to reject suggestions.

Acceptance thresholds remain **unagreed**. Claims leadership should set them from measured incumbent errors, consequences and operational capacity; an overall accuracy number cannot compensate for unacceptable severe-claim misses. Size the held-out evaluation around those tolerances, especially rare harms.

## Next commitment

Propose a two-week discovery led by the head of claims with an engineering lead, adjuster representatives and the data/privacy owner. Produce the baseline, adjudicated label sample, permitted data path and agreed evaluation contract. Advance to an offline prototype only if these support a testable advantage over simpler automation. Rework or stop if permissions, labels, reviewer capacity or incremental value are inadequate. Later live exposure should begin in shadow mode, retain manual fallback and stop for material privacy or severity failures; expansion requires measured evidence and operating ownership.

## What could change the recommendation

Structured intake may capture most of the benefit more cheaply. A representative workflow sample would settle that. The other decisive unknowns are availability of original intake data and adjusters' actual review burden; resolve both during discovery. Compare available products and internal implementation only after these boundaries are clear.
