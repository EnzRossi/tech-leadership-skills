# Methodology: AI Initiative Evaluator

The detailed method behind `SKILL.md`. Read the section the workflow points to.

Contents:
1. Is AI the right tool?
2. Classification (automate or augment; cost of being wrong; AI shape)
3. Dimension rubric (eight dimensions, four ratings)
4. Decision rules (from dimension pattern to recommendation)
5. Designing the next experiment
6. Lifecycle cost checklist
7. Worked example
8. Why the method is shaped this way

The method is EnzRossi's synthesis. Concepts drawn from others are attributed in `sources.md`.

---

## 1. Is AI the right tool?

Run this test before evaluating the AI proposal. Answer each question from the problem statement, not from the proposed solution.

**Alternatives test.** For the problem as restated, could most of the value be captured by:

- A rule set or decision table written by the people who do the task today?
- A lookup, search, or database query over data the organization already has?
- A workflow or forms change that removes the step rather than automating it?
- An existing non-AI product (ticketing, scheduling, OCR with templates, reporting tool)?
- Doing the task manually for now, because the volume does not justify any automation?

If any of these captures most of the value, the AI proposal has to beat that alternative on cost and risk, not on novelty. Record the strongest alternative in the memo. Many teams find that a heuristic captures a large share of the benefit they hoped to get from a model, at a fraction of the cost and with none of the evaluation burden.

**Shape test.** AI is plausibly the right tool when several of these hold:

- Inputs are unstructured (free text, images, speech, documents with variable layouts).
- The rules are hard to write down, change often, or would be brittle.
- Humans do the task by judgment and would disagree at the margins.
- Variation or imperfection in output is acceptable, or a human reviews the output anyway.
- Volume is high enough that per-item human effort is the constraint.

AI is a poor fit when:

- The task's value is its predictability: the same input must always produce the same output.
- Information is static and limited, so a table or rule already covers it.
- Every error is expensive and there is no cheap way to catch errors before they matter.
- The decision must be transparent or auditable by law or contract, and a probabilistic explanation will not satisfy the auditor.
- Users have said they do not want automation of this task, or their trust in it is the product.
- Speed to market matters more than the marginal quality AI adds, and a simpler solution ships sooner.

**Verdict.** One of: *AI is the wrong tool* (recommend the alternative), *AI is the right shape but the alternative should be the baseline* (build the heuristic first, measure, then decide), or *AI is the right tool* (continue). This verdict appears in the memo as its own finding.

---

## 2. Classification

### 2.1 Automate or augment

- **Augment**: the system drafts, suggests, ranks, summarizes, or flags; a human decides and acts. Tolerates lower accuracy because the human is the safeguard. Requires that the human can actually check the output in the time available; otherwise it is automation with a rubber stamp.
- **Automate**: the system acts (sends, approves, rejects, files, routes) without a human on each item. Requires accuracy matched to the cost of being wrong, a defined escalation path for low-confidence or out-of-scope cases, and a way to detect and reverse mistakes at scale.

Ask explicitly whether the requester expects a human to review every output. If yes, and the volume is large, check whether that review is realistic; review fatigue turns augmentation into unsupervised automation.

### 2.2 Cost of being wrong

| Level | Definition | Consequence for the initiative |
|---|---|---|
| Low | An error is an inconvenience, obvious to the user, and reversed in seconds | Augmentation with light oversight is fine; accuracy target set by user tolerance |
| Medium | An error costs money or time, irritates a customer, or requires a correction process; reversible with effort | Needs measured accuracy on representative data before exposure; escalation path for uncertain cases; sampling-based review |
| High | An error causes financial loss, legal exposure, safety harm, discrimination, or reputational damage; hard or impossible to reverse | Automation is rarely acceptable; human decision with the system as advisor; formal evaluation, monitoring, and the ability to disable; likely regulatory obligations |

Two refinements:

- **Error asymmetry.** Ask which is worse, a false positive or a false negative, and by how much. A fraud filter and a medical screen have opposite asymmetries. The answer sets the operating point and belongs in the success criteria.
- **Regulated categories.** If the use touches employment decisions, credit, insurance, education access, biometrics, law enforcement, critical infrastructure, or medical decisions, treat the cost of being wrong as High regardless of the requester's view, and add regulatory assessment to the next stage.

### 2.3 Shape of the AI

Recommend the simplest shape that could solve the problem.

1. **Single call with context**: one model invocation, possibly with retrieval of relevant documents. Covers a large share of real use cases: classification, extraction, summarization, drafting, question answering over known material.
2. **Fixed workflow**: a predefined sequence of steps, some of which are model calls, with deterministic checks between them. Use when the task decomposes into known stages.
3. **Agent**: the model decides which steps to take and when to stop. Use only when the path cannot be predicted in advance, the environment gives feedback the model can use, and the cost of a wrong path is contained. Agents multiply cost, latency, and failure modes.

Also distinguish **generative** (produces text, images, code; variation acceptable) from **discriminative or predictive** (classifies, scores, forecasts; accuracy is the point). Predictive tasks with tabular data often belong to established machine learning, not large language models, and are cheaper to evaluate.

---

## 3. Dimension rubric

Rate each dimension **Strong**, **Adequate**, **Weak**, or **Unknown**. Unknown means the inputs do not allow a rating; say what would resolve it.

### Business value
- Strong: the outcome is quantified with the requester's own numbers (volume, time per item, error cost, revenue at stake), the baseline is measured, and the value exceeds a rough lifecycle cost by a wide margin.
- Adequate: the outcome is quantified but the baseline or the volume is estimated.
- Weak: the value is described in adjectives, or the volume is too low to justify any automation, or the value depends on adoption that nothing supports.
- Resolve Unknown with: how the task is done today, by how many people, how often, and what a mistake costs.

### Strategic fit
- Strong: the capability is part of how the organization wins customers or is clearly on the path there; owning it compounds.
- Adequate: it improves an important internal process but competitors could buy the same thing.
- Weak: it is a commodity function available as a product, or it is disconnected from stated strategy ("the board wants AI").
- Resolve Unknown with: the strategy document or the executive's own words on what the organization competes on.

### User desirability
- Strong: the intended users asked for it, or observed behavior shows them working around the problem today, and the proposed workflow was designed with them.
- Adequate: users agree the problem is real; the solution has not been shown to them.
- Weak: the initiative comes from outside the user group, users have rejected similar tools, or the solution requires users to change how they work with no benefit to them personally.
- Resolve Unknown with: three conversations with the people who would use it.

### Technical feasibility
- Strong: a comparable task on comparable data has been shown to work at the required accuracy, in this organization or publicly, and a prototype on the organization's own data confirms it.
- Adequate: comparable public results exist; nothing has been tried on this data.
- Weak: the task requires accuracy that nothing comparable achieves, or the demo shown was on hand-picked inputs, or the task is one that current systems are known to do badly (long-horizon reasoning, exact arithmetic on large tables, novel expert judgment with no reference data).
- Resolve Unknown with: a one-to-two week spike on fifty to two hundred real examples.

### Data readiness
Assess three layers, borrowing the structure of data readiness levels: can the data be **accessed** (exists, machine-readable, legally usable for this purpose), is it **faithful** (representative, not missing the hard cases, labels or outcomes recorded reliably), and is it **appropriate** for this specific task (contains the signal needed; not merely adjacent)?
- Strong: all three confirmed on a sample you or the team has inspected.
- Adequate: accessible and faithful; appropriateness untested.
- Weak: data exists only in descriptions, lives in systems nobody has extracted from, lacks rights for this use, or lacks the outcome labels the task needs.
- Resolve Unknown with: a sample of real records and the answer to "who can approve using this data for this purpose?"

### Evaluation readiness
- Strong: a set of real inputs with agreed correct or acceptable outputs exists, or experts have agreed how to judge outputs and a labeling exercise is scoped; success thresholds are defined including error asymmetry.
- Adequate: experts can describe what good looks like; no labeled set yet; building one is feasible in weeks.
- Weak: experts disagree about what correct means, or correctness is only knowable long after the fact with no proxy, or nobody has proposed how to measure.
- Resolve Unknown with: ask two experts to judge the same twenty outputs and measure their agreement.

### Operational readiness
- Strong: a named owner for production; monitoring for quality drift and cost; a process for model or vendor changes; an incident path; capacity for the human review the design assumes; a decommissioning plan.
- Adequate: an owner is identified; the rest is planned for the pilot.
- Weak: nobody owns it after launch; the team that builds it will not run it; the design assumes human review that no one is staffed to do.
- Resolve Unknown with: who is on call for this in twelve months, and who pays the inference bill?

### Risk and compliance
Consider: personal or sensitive data; security of the system and of any vendor; intellectual property in training data and outputs; fairness and disparate impact; confabulation exposed to users or customers; regulatory tier; reputational exposure if outputs are wrong in public; dependence on a single vendor's model.
- Strong: risks identified with mitigations and owners; regulatory tier known; a way to disable the system exists.
- Adequate: risks identified; mitigations planned for the pilot.
- Weak: personal data or regulated decisions involved with no assessment; outputs to customers with no review; no way to turn it off.
- Resolve Unknown with: data classification of the inputs and the regulatory category of the decision.

---

## 4. Decision rules

Apply in order. Stop at the first rule that fires.

1. **Section 1 verdict is "wrong tool"** → **Do not use AI.** The memo names the alternative and the next step for it.
2. **Cost of being wrong is High and the design automates** → **Do not use AI** in that form. Offer the augment variant as an alternative recommendation if the other dimensions support it.
3. **Business value is Weak** → **Do not use AI.** Nothing downstream fixes a problem not worth solving.
4. **Business value Unknown, or the problem or users are Unknown** → **Research further.** Specify the research: who to talk to, what to count, for how long.
5. **Value and desirability at least Adequate; feasibility or data readiness Weak or Unknown** → **Prototype** on real data, scoped to answer the feasibility or data question, with a stopping rule.
6. **Feasibility shown; evaluation readiness Weak** → **Prototype** the evaluation set first. No pilot until outputs can be judged.
7. **Feasibility and evaluation at least Adequate; operational, desirability, or cost questions open** → **Run a controlled pilot** with real users, a control or baseline, and predefined success and stop criteria.
8. **Pilot met its criteria; operational readiness and risk at least Adequate** → **Proceed toward production**, staged.
9. **Sourcing lean, applied alongside rules 5 to 8:**
   - Strategic fit Weak or Adequate and a mature product exists → **Buy**. Evaluate the product with the same eight dimensions; a vendor's data readiness and evaluation readiness claims need the same evidence.
   - Strategic fit Strong and internal skills present or acquirable in time → **Build internally.**
   - Strategic fit Strong, urgency real, internal capacity or skill missing → **External engineering partner**, with knowledge transfer and exit written into the engagement. Hand the detailed sourcing decision to `build-buy-hire-augment` when it is contested.

Rules 1 to 3 are deliberately placed first. The evaluation must be able to stop an initiative for reasons that no amount of technical strength can overcome.

---

## 5. Designing the next experiment

Every recommendation except "Do not use AI" comes with an experiment. Define:

| Element | Requirement |
|---|---|
| Question | The single Weak or Unknown dimension this experiment resolves |
| Method | What is built, bought, or studied; on which real data or users; the simplest shape that answers the question |
| Baseline | What the result is compared against: the current process, a heuristic, or human performance on the same items |
| Measures | The metric, the threshold, and the error asymmetry (which errors count more) |
| Duration and budget | Weeks, not quarters; a spend the sponsor can lose |
| Stop rule | The result that ends the initiative or sends it back to research |
| Owner and approver | Who runs it; who decides on the result |

For a **research** step, the method is interviews, counts, and data inspection, and the measures are agreement rates and quantified volumes. For a **prototype**, the method is a build on fifty to two hundred real examples and the measure is accuracy against a baseline. For a **pilot**, the method is real users in the real workflow for a bounded period with a control, and the measures include adoption, time saved, error rate, and review burden.

---

## 6. Lifecycle cost checklist

Do not estimate costs the user has not provided figures for. Do list the cost drivers so the sponsor can estimate them:

- Inference or API cost per item at expected volume, and how it changes with the shape (agents multiply calls)
- Model or vendor change management: re-evaluation each time the model is updated
- Monitoring for quality drift, cost drift, and abuse
- Human review time the design assumes, at volume
- Data pipeline, access, and rights maintenance
- Security and compliance review, initial and recurring
- Integration into the workflow and the systems that surround it
- Training and change management for users
- Decommissioning: what happens to data, dependent processes, and users when the system is turned off

Unit inference prices have fallen steeply year over year; the durable costs are evaluation, monitoring, review, and integration. A memo that budgets only for inference and build is underestimating.

---

## 7. Worked example

**Request.** A COO of a mid-size logistics company asks: "Our customer service team spends hours a day answering shipment-status emails. A vendor showed us an AI agent that replies automatically. Should we buy it?"

**Step 1, problem.** Customer service agents (12 people) answer roughly 600 status emails a day (FACT, from the COO); each takes about four minutes (ASSUMPTION, the COO's estimate); the information comes from the tracking system (FACT). Outcome: reduce agent time on status emails by half without increasing customer complaints.

**Step 2, right tool.** The status is a deterministic lookup on a tracking number. The unstructured part is finding the tracking number or order reference in the email. Alternatives: a self-service tracking page and an email template with a link (workflow change); a rules-based parser for tracking numbers plus a templated reply (deterministic). Verdict: AI is the wrong tool for the reply and at most a small helper for extracting references from messy emails. Most of the value is capturable without AI.

**Step 3 to 5.** Business value Adequate (quantified, baseline estimated); Strategic fit Weak (commodity); Desirability Unknown (agents not consulted; customers' preference for self-service unknown); Cost of being wrong Medium (wrong status to a customer). Decision rule 1 fires.

**Recommendation.** Do not buy the AI agent. Ship a tracking link in the auto-reply and a self-service page; measure the drop in status emails over four weeks. If residual emails are dominated by messy references, prototype extraction only, with agents reviewing drafts. Approval point: any automated reply to customers.

**Success criteria.** Status emails down by at least forty percent in four weeks; complaint rate unchanged; the experiment is owned by the customer-service lead.

---

## 8. Why the method is shaped this way

- **Problem before technology**, because interview-based research on failed AI projects places leadership misunderstanding of the problem and technology-first framing among the top causes, ahead of technical difficulty.
- **The "wrong tool" test comes first**, because machine-learning practitioners' own guidance is to launch without a model where a heuristic captures most of the value, and because a probabilistic system can never be the right choice for a task whose value is its determinism.
- **Cost of being wrong before accuracy**, because required accuracy has no meaning until the consequence of error is known, and because regulated categories change the work regardless of technical merit.
- **Evaluation readiness as a gate**, because enterprise programs that succeeded describe starting with evaluations, and because a pilot that cannot be judged produces confidence rather than evidence.
- **No composite score by default**, because a single Weak dimension in cost of being wrong, data, or evaluation should stop an initiative, and weighted averages exist to prevent exactly that.
- **Stage recommendations (research, prototype, pilot, production) rather than a single yes or no**, because the evidence available at evaluation time is rarely sufficient for a production decision, and because a large share of generative AI projects are abandoned after proof of concept for reasons a staged plan surfaces early.
- **Lifecycle cost and decommissioning**, because pilots are the cheapest stage, hidden technical debt in learning systems is well documented, and governance frameworks explicitly require a plan for superseding or deactivating a system that stops performing.
