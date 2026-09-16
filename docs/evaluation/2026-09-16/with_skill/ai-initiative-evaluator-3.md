# AI initiative decision: Payment reconciliation

Finance operations sponsor · Evidence: your workflow description

## Recommendation

**Confidence: High on deterministic reconciliation as the first investment; medium on implementation effort.**

Fund discovery and implementation of deterministic reconciliation, conditional on validating the file schemas and ledger rules. Do not fund generative AI as the matching or sign-off authority. Matching structured settlement records against a ledger requires exact, reproducible rules and a complete exception trail. An LLM demo does not establish that it can safely account for every transaction or improve on conventional automation.

## Decisive evidence

You report approximately 40,000 transactions daily from three CSV providers, three people reconciling in Excel, and a requirement to resolve every unmatched transaction before close. Volume supports investigating automation, but it does not establish recoverable payroll savings or a need for language generation.

The strongest simpler option is provider-specific parsing, schema validation, normalization, rule-based matching and an exception queue. Evaluate an existing reconciliation product against a modest internal implementation; delivery effort, integration and operating cost are unknown. Keeping Excel preserves continuity while the replacement is validated, but retains the reported manual workload.

Exact steps should include identifiers, amounts, currencies, settlement periods, fees, duplicates and completeness controls. Missing or ambiguous matches must remain visible exceptions. Do not allow the system to invent a match simply to reach a balanced total. Unstructured descriptions could later justify assisted extraction, with deterministic validation and human resolution, if they prove to be the bottleneck.

## Good enough for the next stage

Compare the candidate against current reconciliation on the same historical files, preserving an untouched period for acceptance. Include each provider, high-volume days, split settlements, refunds, chargebacks, missing files, duplicate imports, currency differences and period boundaries. Confirm which cases actually occur rather than assuming all do.

Finance staff should adjudicate disputed historical matches using raw records; spreadsheet decisions are not automatically correct labels. Use executable control totals and record-level traces. Measure false matches separately from missed matches, exception age, manual resolution time, total close time and effort per day. A proposed essential gate is that every input is accounted for as a justified match or explicit exception, with no silent loss; this follows directly from your close requirement. Finance must define tolerable false-match risk and close deadlines before acceptance.

Run in parallel with the established process, prevent automatic ledger writes initially, test reprocessing and rollback, and retain finance authority to stop release. A human review claim is useful only if reviewers can inspect supporting evidence and handle the actual exception volume.

## Next commitment

Proposed owner: finance operations, with an engineering counterpart. Bound initial work to mapping the three inputs, documenting reconciliation rules and testing the hardest exceptions. Advance when a deterministic approach passes agreed controls and reduces end-to-end effort; rework if source completeness or ledger mapping is unresolved. Do not require an AI experiment.

## What could change the recommendation

A large residual workload requiring genuine interpretation could justify an assistive model around the exception workflow. Establish its share, whether source inputs are permitted, and whether assistance reduces total review time without introducing false matches. That would change the exception-handling approach, not the need for exact accounting controls.
