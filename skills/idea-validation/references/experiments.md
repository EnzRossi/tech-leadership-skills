# Designing and interpreting validation experiments

Use this when the next decision depends on a test. This card extends Strategyzer's Test Card with operating details and uncertainty handling; it is this repository's synthesis, not a statistical validation instrument.

## Select the test

Start with the assumption most likely to change the next commitment, considering importance and evidence. A landing-page click cannot establish repeat value; a polished prototype cannot establish a buyer's budget. If a hard feasibility or data-access constraint blocks delivery, resolve it before collecting demand for an undeliverable offer.

| Uncertainty | Smallest useful test | What remains unknown |
|---|---|---|
| Problem and current workaround | Interview eligible users about recent events and inspect workflow artifacts | Willingness to buy the proposed solution |
| Buyer, price and procurement | Offer a scoped paid pilot to an authorized buyer | Renewal, scalable delivery and repeatable sales |
| Reach and initial interest | Present a clear offer through the intended channel; measure eligible exposures and responses | Clicks or emails do not establish willingness to pay |
| Usability and delivered value | Concierge or prototype task compared with the current workflow | Manual assistance can hide delivery costs and usability failures |
| Recurring value | Observe the same eligible cohort completing the value-producing action or renewing over its natural cycle | Short windows cannot establish long-term retention |
| Internal benefit | Compare task outcomes, rework and adoption against the existing workflow | Time saved is not automatically cash saved |
| Marketplace liquidity | Attempt real matches in one constrained market with both sides available | Listings and one-sided waitlists do not establish successful transactions |
| AI feasibility | Evaluate representative, messy cases with independent outcome checks and error/effort costs | A successful demo does not establish reliable operation |

## Compact experiment card

Include only decision-relevant details in the memo; use an appendix if needed.

- **Hypothesis and commitment:** what must be true, and what decision the result changes.
- **Participants:** eligibility, geography where relevant, recruitment channel, exclusions and likely selection bias. Include nonbuyers or failed users when investigating contradictory evidence.
- **Procedure and baseline:** what participants actually do, offer and price if applicable, current alternative, and any founder assistance or incentives.
- **Measure:** numerator, denominator and meaningful outcome. Keep invited, reached, eligible, activated, paid and retained counts separate. Record cancellations, refunds, failures and nonresponse.
- **Window and cap:** natural usage or buying cycle, planned exposure/sample rationale, duration and maximum effort or spend. A tiny discovery sample can reveal failure mechanisms but cannot estimate population conversion precisely.
- **Rules fixed before execution:** proposed pass, fail and inconclusive criteria, why they are sufficient for this next commitment, and what follows each. Use a defensible qualitative criterion if numerical cutoffs lack a basis. Criteria are proposals until agreed; do not invent universal conversion or interview-count benchmarks.
- **Accountability:** proposed owner, review date or relative deadline, and unresolved permissions. Do not imply these are assigned or approved.

## Interpret before changing the verdict

Check recruitment and instrumentation first. Too few eligible observations, a broken checkout, insufficient exposure or no opportunity for repeat use make the result inconclusive. Fix the specific defect or extend observation within an agreed cap; do not keep extending until a desired result appears. Preserve the original rule when revising a hypothesis, and label the next test as new.

A failed offer can reject a segment/price/channel combination without rejecting the underlying problem. Repeated credible negative evidence or a binding constraint may justify stopping. A pass supports only the tested assumption and the next bounded commitment; it is not product-market fit. For recurring products measure meaningful repeat activity at the natural frequency, not logins or a universal day-7/day-30 threshold. For A/B tests that need population-level inference, define sample size and analysis with appropriate statistical expertise; do not apply significance language to a handful of interviews.

## Participant trust

Design experiments transparently. Label unavailable features or prototypes and explain what happens after a click or reservation. For concierge or Wizard-of-Oz tests, disclose material human access and use consented or synthetic data where appropriate. Do not recommend collecting sensitive material or payment details just to gauge interest. Pre-orders require clear availability, delivery and refund terms and an authorized way to fulfill or refund them. Drafting a test does not authorize launching it or contacting participants.

## Worked interpretation (fictional)

A prototype has 100 sign-ups, but only 12 people were eligible for its intended workflow and only 3 tried it. No one has reached the next monthly task. Report the separate counts. This supports some initial interest; neither 3/100 nor 3/12 is a retention rate. The next step is to understand activation and observe the next task, not to declare recurring demand or kill it for lack of weekly use.
