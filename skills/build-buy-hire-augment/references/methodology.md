# Methodology: Build, Buy, Hire, Augment

The detailed method behind `SKILL.md`. Read the section the workflow points to.

Contents:
1. Decomposition
2. Dimension rubric (sixteen dimensions)
3. The eight options and their profiles
4. Knockout rules
5. Signs the internal option is wrong, and signs the external option is wrong
6. Cost drivers by option
7. Exit and transition patterns
8. Worked example
9. Why the method is shaped this way

The method is EnzRossi's synthesis. Concepts drawn from others are attributed in `sources.md`.

---

## 1. Decomposition

Split the capability into components small enough that each has one sourcing answer. For each component ask:

- **Would a customer or the market notice if ours were better than a competitor's?** If yes, it is *differentiating*. If a competitor could buy the same thing tomorrow and nobody would notice, it is *commodity*.
- **Is this something we must do well but that does not win us business?** Then it is *mission-critical commodity*, which is still commodity for sourcing purposes. Mission-critical is not the same as core.
- **How mature is the problem?** Novel problems with no established solution behave differently from problems with many vendors. Novel plus differentiating is the strongest case for building; mature plus commodity is the strongest case for buying.

A typical result: the data model, the workflow logic, and the customer-facing experience are differentiating; authentication, payments, notifications, hosting, and analytics plumbing are commodity. The recommendation then reads as a hybrid ("buy the platform, build the differentiating layer, hire for the components you will iterate on for years"), which is the honest answer far more often than a single option is.

Where a component is small and commodity, note that the decision is itself not worth much analysis: default to buy and move on.

---

## 2. Dimension rubric

Rate each dimension for each component. Ratings are descriptive labels, not numbers.

### Nature of the capability

**Differentiation** — Core (how the organization wins; owning it compounds) · Supporting (important, but a competitor could have the same) · Commodity (identical for everyone).

**Maturity of the problem** — Novel (no established solution; requirements discovered by doing) · Emerging (solutions exist but vary; practice unsettled) · Mature (multiple vendors; well-understood; standardized).

**Domain knowledge required** — Deep proprietary (only people inside the organization understand the rules and data) · Industry (people with sector experience can learn it in weeks) · Generic (any competent engineer).

**Integration depth** — Standalone · Integrated through stable interfaces · Entangled with core systems, data models, or workflows.

### Shape of the demand

**Urgency** — Weeks · Months · Flexible. Record what happens if the date is missed; urgency without a consequence is preference.

**Duration** — Spike (under six months) · Bounded (six to eighteen months) · Ongoing (indefinite; the capability must be maintained and evolved).

**Iteration frequency** — Build once and run · Periodic change · Continuous change (weekly or faster; the capability is a product).

**Requirement uncertainty** — Defined (acceptance criteria could be written today) · Partly defined (the outcome is clear; the path is not) · Undefined (the organization is still learning what it needs).

### Internal position

**Internal skills** — Present · Adjacent (learnable in the urgency window) · Absent.

**Internal capacity** — Available · Available if something is deprioritized (name it) · Fully committed.

**Talent availability** — Rate from the organization's own recent hiring data where available: Readily hireable in the urgency window · Hireable but slow · Scarce or unaffordable in this market. Unknown if no data.

**Capacity to manage the option** — Every option needs a different kind of management: people management for hires, day-to-day direction for augmented staff, outcome and acceptance management for partners, vendor management for products. Rate whether that management capacity exists: Present · Stretched · Absent.

### Constraints

**Security and compliance** — Open · Controlled (external access possible with agreements and controls) · Restricted (data or systems cannot be accessed by external parties, or residency or clearance requirements apply).

**Knowledge retention requirement** — Must stay in-house (the knowledge is an asset or a risk) · Should be transferred (external help acceptable if knowledge is handed over) · Not required (the organization does not need to understand how it works).

**Reversibility and lock-in** — Rate the exit: Cheap (weeks, low cost, standard formats) · Moderate (months; migration work) · Expensive (years or infeasible; proprietary formats or entangled dependencies). Every option, including building, has lock-in; rate each option's exit rather than treating lock-in as a property of vendors alone.

**Budget shape** — A fact about the organization, not an analysis: Capital available for upfront investment · Operating budget only · Constrained (any option must fit a stated envelope). Record as given; do not model finances.

---

## 3. The eight options and their profiles

Each profile lists the conditions under which the option fits, the conditions under which it hurts, and the management it requires.

### Build internally
- **Fits**: Core differentiation; novel or emerging problem; continuous iteration; deep proprietary domain knowledge; entangled integration; ongoing duration; skills present or adjacent; capacity available.
- **Hurts**: Commodity components; mature problems with good products; teams already fully committed; build-once-and-run demands where the maintenance burden is out of proportion to the differentiation.
- **Management**: Product ownership and engineering management for the life of the system, not just the build.

### Buy a SaaS or platform
- **Fits**: Commodity or supporting components; mature problem; defined requirement; standalone or interface-level integration; build-once-and-run or periodic change; exit moderate or cheap.
- **Hurts**: Core differentiation (the organization's advantage becomes available to everyone); entangled integration; continuous change at a pace the vendor's roadmap will not follow; restricted data; per-unit pricing that scales badly with the organization's growth.
- **Management**: Vendor management, integration ownership, and periodic re-evaluation against usage breakpoints where pricing or fit changes.

### Hire full-time employees
- **Fits**: Ongoing duration; core or supporting differentiation; knowledge must stay in-house; talent hireable in the urgency window; management capacity for people present.
- **Hurts**: Spike or bounded duration; skills needed only for a migration or a launch; urgency the hiring market cannot meet; no manager with time to onboard and grow the hire.
- **Management**: People management, onboarding, career development. First-year cost is dominated by time to fill and ramp time, not salary.

### Staff augmentation or contractors
- **Fits**: Bounded duration or a capacity gap while hiring; work directed day-to-day by an internal lead; an existing team to absorb knowledge; urgency higher than hiring allows; skills adjacent to the team's own so the work is reviewable.
- **Hurts**: Ongoing core work with no plan to internalize (the knowledge leaves with the contractor); no internal lead with time to direct; restricted security regimes without clearances; engagements that quietly become permanent, which is a hire without the retention.
- **Management**: Daily direction and code review by an internal lead; a written end date and knowledge-transfer plan from day one.

### Project-based engineering partner or agency
- **Fits**: Defined or partly defined requirement with a clear acceptance test; internal capacity absent; bounded duration; the organization needs the outcome more than the know-how, or knowledge transfer is contracted; supporting rather than core differentiation.
- **Hurts**: Undefined requirements (fixed scope on an uncertain need builds the wrong thing); core capabilities with no internal owner to receive them; entangled integration with systems the partner cannot access; organizations without someone to manage acceptance.
- **Management**: Outcome definition, acceptance testing, and a receiving owner. Architecture will follow the communication structure between partner and organization; if the partner is isolated, the result will be too.

### Specialist consultant
- **Fits**: A narrow, short need for judgment rather than hands: architecture review, security assessment, migration planning, a second opinion on a decision. Highest value when the organization's own people will do the work afterward.
- **Hurts**: Anything that requires sustained delivery; situations where the consultant's recommendation has no internal owner to act on it.
- **Management**: A sharply written question and an internal owner for the answer.

### Hybrid
- **Fits**: Almost every decomposed capability. Common shapes: buy the platform and build the differentiating layer; hire the long-term core and augment to hit a date; partner for a bounded launch with contracted knowledge transfer to hires who start during the engagement.
- **Hurts**: When "hybrid" is used to avoid deciding. Every component still needs one answer and one owner.
- **Management**: The union of the components' management needs, plus the seams between them.

### Wait or validate first
- **Fits**: Undefined requirement; unknown duration; business consequence of delay is small; the capability can be done manually or with a spreadsheet long enough to learn what is really needed.
- **Hurts**: When waiting has a real, stated cost that the requester has quantified.
- **Management**: A dated decision to revisit, with the evidence that will be gathered in the meantime.

---

## 4. Knockout rules

Apply per component. Record each knockout and its reason in the memo.

| Condition | Options removed |
|---|---|
| Security and compliance Restricted for this component | Staff augmentation, project partner, and SaaS unless the provider meets the regime; consultant only under agreement |
| Requirement Undefined | Project partner on fixed scope; buy (nothing to evaluate a product against); hire for this component specifically until the role is definable |
| Duration Spike | Hire for this component alone |
| Duration Ongoing and Differentiation Core and Knowledge retention Must stay in-house | Project partner as the sole option; staff augmentation without a parallel internalization plan |
| Capacity to manage the option Absent | The option that needs that management (no lead to direct augmented staff; no owner to accept partner deliverables; no people manager for hires) |
| Talent availability Scarce and Urgency Weeks | Hire as the sole route to the date |
| Internal capacity Fully committed and nothing will be deprioritized | Build internally as the sole option |
| Differentiation Commodity and a mature product exists | Build internally, unless integration depth is Entangled and no product integrates |

Knockouts are conservative: they remove an option as the *sole* answer for the component; it may still appear inside a hybrid where the condition is addressed (for example, augmentation with a written internalization plan).

---

## 5. Signs the internal option is wrong, and signs the external option is wrong

Leaders arrive with a bias in one direction or the other. Check both lists.

**Signs that building or hiring internally is the wrong answer even though the leader prefers it**
- The component is commodity and the preference is pride or distrust of vendors rather than differentiation.
- The team is fully committed and the plan depends on people doing this "on the side".
- The organization's own hiring data shows time to fill exceeds the urgency window.
- The requirement is a one-time migration or launch and the hire would be underused afterward.
- The skill is absent and the plan is to learn it on the critical path of a dated commitment.

**Signs that an outside firm is the wrong answer even though a vendor or the leader proposes it**
- The capability is core and ongoing, and nobody internal is designated to receive it.
- The requirement is undefined; the partner will build the wrong thing on time and on budget.
- The motive is to avoid an internal conversation about priorities or performance.
- The organization has no one with time to direct augmented staff or accept partner deliverables.
- The proposal has no end date, no knowledge-transfer plan, or no exit terms.
- Cost is the only argument. Cost has fallen as the primary reason organizations use external providers; where it is the sole reason offered, look for the hidden management and knowledge costs.

**The neutrality rule, restated.** Recommend an external firm only when at least two of the following hold for the component: urgency the hiring market cannot meet; bounded duration; skill absent internally and not core long term; internal capacity blocked by commitments that will not move. Where the external and internal options are close, prefer internal. Where an external option is recommended, the memo must include the end date, the receiving owner, and the knowledge-transfer plan.

---

## 6. Cost drivers by option

List drivers, not figures. Mark which the leader has numbers for.

| Option | Upfront drivers | Ongoing drivers | Often forgotten |
|---|---|---|---|
| Build | Design and build effort; opportunity cost of the team's alternative work | Maintenance and operation (commonly the majority of lifetime cost); dependencies and upgrades; on-call | The cost of the product not built while the team built this |
| Buy | Licensing; integration; data migration; training | Subscription growth with seats or usage; integration upkeep on vendor changes; vendor management | Exit cost; pricing breakpoints as usage grows |
| Hire | Recruiting cost; time to fill; ramp time at reduced productivity | Compensation and benefits; management time; development | The months between deciding to hire and having productive capacity |
| Staff augmentation | Onboarding; access provisioning | Rates typically above internal cost per hour; internal direction and review time | Knowledge that leaves at the end; dependency creep if the end date slips |
| Project partner | Scoping and contracting; acceptance criteria | Engagement fees; internal acceptance and review time; knowledge transfer | Post-handover maintenance if no internal owner exists; rework when scope was wrong |
| Consultant | Fees; internal time to brief | Usually none | Cost of not acting on the recommendation |
| Wait | Manual effort in the interim | The stated cost of delay | Learning value gained, which is a benefit not a cost |

Two facts from published research shape this table and belong in the memo when relevant: maintenance and evolution account for the majority of a built system's lifetime cost, and time to fill an engineering role in recent benchmarks is measured in months, before ramp time. Cite them as context; the organization's own figures override them.

---

## 7. Exit and transition patterns

For each recommended option, describe the exit at six and eighteen months and the transition from today.

**Exit patterns**
- *Build*: exit means decommissioning or replacing; cost depends on how entangled the system became. Design for replaceable modules where uncertainty is high.
- *Buy*: exit means migration; cost depends on data portability, standard formats, and how much workflow was customized inside the product. Test export early. Some lock-in is worth accepting for unique value; the memo should say which lock-in is being accepted and why.
- *Hire*: exit is a people decision and belongs to the leader; the sourcing memo notes only whether the role remains needed.
- *Staff augmentation*: exit is the contract end; clean only if knowledge transfer was planned and an internal person paired throughout.
- *Partner*: exit is handover; clean only if acceptance criteria included documentation, tests, and a receiving owner who worked alongside the partner.

**Transition patterns**
- *Augment while hiring*: augmentation covers the gap; hires start during the engagement and pair with augmented staff; the engagement ends on a date, not on "when the hires are ready".
- *Partner to internal*: partner delivers a bounded first version; internal owner is named before the engagement starts and reviews every increment; knowledge transfer is a deliverable with acceptance criteria.
- *Buy then build the edge*: adopt the product for the commodity core; build the differentiating layer against the product's interfaces; revisit the buy at usage breakpoints.
- *Wait then decide*: run the manual process with a named owner for a fixed period; collect the volume, variation, and pain data; make the sourcing decision on a date.

---

## 8. Worked example

**Request.** A VP of Engineering at a 60-person B2B SaaS company: "We need to add SOC 2 compliance tooling and a customer-facing audit-log feature by Q2. I want to hire two senior engineers. Thoughts?"

**Step 1.** Capability: (a) achieve and maintain SOC 2 evidence collection and controls monitoring; (b) give customers a queryable audit log of actions in the product. If missed: two enterprise deals conditional on SOC 2 (FACT, per VP) slip; audit log is a roadmap item with no dated deal (FACT).

**Step 2.** Decompose. (a) Compliance tooling: commodity, mature (many products), generic domain, standalone integration. (b) Audit log: supporting differentiation (enterprise buyers expect it; competitors have it), mature pattern, deep proprietary knowledge of the product's data model, entangled integration, continuous change as the product grows.

**Step 3, selected ratings.** Urgency: months (Q2). Duration: (a) ongoing but low-touch; (b) ongoing. Internal skills: (a) absent; (b) present. Internal capacity: fully committed; VP says the roadmap could shed one item (FACT). Talent availability: the company's last two senior hires took 3.5 and 5 months (FACT). Capacity to manage: people management present; vendor management stretched. Security: controlled. Knowledge retention: (a) not required; (b) must stay in-house. Budget shape: operating budget only (FACT).

**Step 4, knockouts.** (a) Build internally removed: commodity with mature products. (b) Project partner removed as sole option: core-adjacent, ongoing, must stay in-house. (b) Hire as the sole route to Q2 removed: last hires took 3.5 to 5 months, then ramp.

**Step 5.** (a) Buy a compliance-automation product; assign an internal owner from engineering or operations for vendor management. No external engineering needed. (b) Build internally with the existing team after shedding the named roadmap item; if Q2 is firm and the shed item does not free enough capacity, add one augmented engineer paired with an internal owner for a maximum of six months, ending on a date. Neutrality check for (b): urgency real, duration bounded for the gap, skill present internally (so "skill absent" does not hold), capacity blocked (holds). Two conditions hold only if the deprioritization is insufficient; otherwise the internal option wins. Hire: one senior engineer for the ongoing audit and platform work, started now, expected productive after Q2; not two, because (a) needs no engineer.

**Step 6, cost drivers.** Buy (a): subscription, integration time, evidence-collection setup; exit moderate (evidence exported; controls re-mapped). Build (b): the shed roadmap item is the cost; maintenance ongoing. Augmentation, if used: rate for six months; internal review time; exit at contract end with pairing throughout. Hire: time to fill three to five months on own data; ramp thereafter.

**Step 7.** Recommendation: buy (a); build (b) internally with one deprioritization; hire one senior engineer now for the ongoing work; hold augmentation in reserve with a trigger. Alternatives considered: two hires (loses on urgency and on (a) needing none); partner for (b) (loses on knowledge retention and entanglement). Changes the recommendation: if the shed item cannot be shed by a set date, trigger six-month augmentation; if the enterprise deals lapse, urgency falls and the hire alone suffices.

---

## 9. Why the method is shaped this way

- **Decomposition first**, because the strategic-versus-utility split is real but rarely applies to a whole capability; applying a single answer to a mixed request is the most common sourcing error, and the literature on scoping buy decisions at a finer grain than "the system" supports it.
- **Sixteen dimensions in four groups**, because the published build-versus-buy frameworks cover the nature of the capability well but say little about the shape of demand (duration, iteration, uncertainty) or the organization's ability to manage each option, and those are where hire-versus-augment-versus-partner decisions are actually made.
- **Knockouts before comparison**, because a weighted comparison can let a strong score on cost hide an option the organization cannot legally or practically use.
- **An explicit neutrality rule**, because the publisher has a commercial interest and the reader should be able to see the mechanism that counteracts it.
- **Both bias lists**, because leaders who distrust vendors overbuild and overhire as reliably as vendors oversell.
- **Cost drivers, not figures**, because the honest state of most sourcing decisions is that the numbers are not yet known, and inventing them destroys the memo's credibility.
- **Exit and revisit conditions**, because sourcing decisions are options with expiry dates, not permanent choices; decisions that are cheap to reverse can be made quickly and revisited, and decisions that are expensive to reverse deserve the evidence first.
