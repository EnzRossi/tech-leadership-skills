# Idea validation: scheduling and compliance tool for private ambulance operators in Germany

Founder (decision: commit two engineers for one quarter) · Evidence as of 2026-09-18 · External · digital · not AI-dependent · Germany only

## Verdict

**Pursue, with a bounded first commitment — Confidence: Medium.**

Your demand evidence is at the second-strongest level: six signed paid pilot agreements at 400 EUR/month, plus two proposal requests, from 14 interviews, in a sector where you have eight years of contacts and a route through the regional associations. That justifies a quarter of two engineers. The weakest point is the competitor set: it is not two general SaaS tools. At least five German vendors sell scheduling specifically to Rettungsdienst and Krankentransport with qualification-based crew staffing and working-time checks. Fixable, not fatal, but it changes what the first version must be; check it with your six signatories before writing code. Second weak point: at 400 EUR/month this is a niche business unless price or scope grows.

## The idea as a hypothesis

Private ambulance and patient-transport operators in Germany (14 interviewed) schedule crews in Excel or a 15-year-old desktop tool whose vendor stopped updates (reported). They must staff vehicles with required qualification mixes, respect Arbeitszeitgesetz and collective-agreement limits, and track mandatory annual training, under 16 state rescue-service laws (inferred from research). Solution: a scheduling tool that encodes these rules. Why now: the incumbent tool is dying. Advantage: sector experience and the associations' trust. Assumed: "compliance" means one rule set across your six pilots' states.

## What the evidence shows

**Demand: supported.** Six signed paid pilots plus two proposal requests from 14 interviews is strong B2B conversion. Caveat: payment starts "when we deliver a first version", so the money is conditional on scope you have not fixed. 6 × 400 EUR = 2,400 EUR/month, 28,800 EUR/year: it proves buyers exist, it does not pay two engineers.

**Competitors: concern, and your list is incomplete.** Web research on 2026-09-18 found sector-specific German products: SIEDA OC:Planner (Rettungsdienst scheduling with qualification-based vehicle staffing, TVöD/DRK tariff rules, SaaS or on-premise, marketed to DRK/ASB/JUH and "independent rescue services"), timecount (crew qualifications, rest-period monitoring, billing for private providers, names private rescue services as clients), Nostradamus (working-time and qualification checks, says pricing starts at single-digit euros per employee per month), Geocon/Cairful and CareMan-Office. A crowded field means demand is real; the question is your wedge: small private operators the aid-organisation-focused vendors under-serve, state-specific rules, migration off the dead desktop tool, or price. Show which one your six pilots actually bought.

**Buyer and route: supported.** In a private operator the owner or Geschäftsführer is buyer and decision maker, so the cycle is short, and you have closed six. The associations are a credible channel (BKS states it represents over 150 member companies; unverified beyond its own claim). Bottom-up ceiling: if the addressable pool is a few hundred private operators, 300 × 400 EUR × 12 = 1.44M EUR/year at full penetration. Realistic penetration makes this a niche product unless per-seat pricing, billing (§ 302 SGB V data exchange, which incumbents bundle) or public operators are added later.

**Defensibility: fixable.** Rule encoding and a clean UI are copyable. Defence would come from association endorsement, embedding in daily dispatch, and being the migration path off the legacy tool. Rules differ by state and change (e.g. TVöD weekly-hour reductions in 2026–27), so compliance content is an ongoing cost, not a one-off.

**Viability and cost.** Value: supported. Usability: unknown. Feasibility: supported for scheduling; the dominant cost driver is compliance content across states plus data migration from the legacy tool, not the build itself. Business viability: concern on scale, not on unit economics. Cost stated as two engineers with no external spend; the real cost is what those engineers would otherwise ship.

## Cheapest test that could change the verdict

Two weeks, before the quarter starts, run by you. Take the six signatories through (a) a one-page first-version scope with acceptance criteria and a go-live date, and (b) a 30-minute look at two named incumbents (OC:Planner, timecount) with the question "why would this not do?" Ask for a first-month prepayment or deposit against the scope. Proposed pass: at least 4 of 6 confirm the scope and date, at least 2 prepay, and rejections of the incumbents cite a specific missing rule or workflow. Proposed kill: fewer than 3 confirm, or a majority say an incumbent would do at a comparable price. Thresholds are proposed until you agree them.

## Questions that still matter

1. What exactly does each pilot agreement bind the operator to, who signed (owner?), what counts as "first version", and what are the exit terms? Weak terms move this toward "test before building".
2. Which compliance rules, in which states, do the six pilots need on day one? Six states with divergent rules changes scope and the quarter estimate.
3. Did the interviews surface OC:Planner, timecount, Nostradamus or similar, and why were they rejected? "Never heard of them" is different from "tried, too expensive, built for the DRK".
4. Does the legacy desktop tool also do dispatch or insurer billing? If so, scheduling alone may not let operators switch off the old tool.
5. What is the goal: a profitable line of business or a venture-scale product? The niche size is fine for the first and a concern for the second.

## Boundaries

Whether your product's checks satisfy each Landesrettungsdienstgesetz, the Arbeitszeitgesetz and applicable collective agreements is a question for a labour-law specialist and the operators' own compliance owners; the tool can assist, not certify. Data protection for staff data (GDPR, works-council rights on scheduling systems) needs a named reviewer. This memo does not authorise the engineering commitment; that decision remains yours after the two-week test.

## Sources consulted (2026-09-18)

- [SIEDA OC:Planner for Rettungsdienst](https://www.sieda.com/dienstplan-software-rettungsdienst/)
- [timecount Rettungsdienst software](https://www.timecount.com/rettungsdienst-software/)
- [Nostradamus: Dienstplan Rettungsdienst](https://nostradamus-software.de/dienstplan-rettungsdienst/)
- [softguide: software for Krankentransport and Rettungsdienst](https://www.softguide.de/software/krankentransporte)
- [Wikipedia: Private Rettungsdienstunternehmen in Deutschland](https://de.wikipedia.org/wiki/Private_Rettungsdienstunternehmen_in_Deutschland) (16 state laws; 2010 BKS revenue figure, dated)
- [BKS Bundesverband, Zahlen Daten Fakten](https://www.bks-rettungsdienst.de/zahlen-daten-fakten/) (page did not load; "over 150 member companies" taken from the search snippet, unverified)
- [FragDenStaat: 30-hour annual training requirement, Baden-Württemberg](https://fragdenstaat.de/en/request/fortbildungspflicht-rettungsdienst-bw-30h-pro-aufgabe/)
