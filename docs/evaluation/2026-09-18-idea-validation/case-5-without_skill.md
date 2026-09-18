# Validation memo: scheduling and compliance tool for private ambulance operators in Germany

**Decision requested:** commit two engineers for one quarter to build a first version.

**My recommendation:** conditional go. The demand signal is unusually strong for this stage and you have a real founder-market advantage. But two of your stated facts do not hold up on a 20-minute check, and one of them (the competitor picture) changes what you should build in the quarter. Spend one to two weeks closing the gaps below before the engineers start, and start them with a narrower scope than "scheduling and compliance tool."

---

## 1. What your evidence actually proves

| Claim | Strength | Comment |
|---|---|---|
| 14 problem interviews, notes exist | Good | Enough for a niche B2B segment, provided the 14 are not all from one region or one association. |
| 6 signed paid pilots at 400 EUR/month, contingent on delivery | Strong, with a caveat | A signature on a conditional agreement is the best pre-product signal you can get short of cash. The caveat: nothing has been paid, and "starting when we deliver a first version" puts the definition of "first version" entirely on your side. If that definition is vague, the six can walk without breaking anything. |
| 2 more asked for a proposal | Weak-to-moderate | Interest, not commitment. Count them as pipeline, not evidence. |
| Incumbent is Excel plus an abandoned 15-year-old desktop tool | Strong | A dead vendor is the cleanest replacement trigger there is. Verify the tool's name and whether anyone has quietly picked up its customers. |
| 8 years in the sector, know the associations | Strong | This is your distribution channel. It is also a bias risk: you may be interviewing people who already like you. |
| Competitors: two generic workforce-scheduling SaaS | **Does not hold** | See section 2. |
| Cost: two internal engineers, hosting only | Understated | See section 4. |

Net: the demand side is validated well beyond what most founders bring to this decision. The supply side (who else is selling to these operators) and the cost side are not.

## 2. The competitor picture is wrong, and that matters

A short search surfaces at least six German vendors that already sell scheduling, personnel or fleet software specifically to Krankentransport and Rettungsdienst operators, not generic workforce tools:

- Caladis (RC 4.0 GmbH): cloud platform for Krankentransport and Rettungsdienst covering Dienstplan, Personal, Fuhrpark and administration in one system ([caladis.de](https://caladis.de/), [rc4-0.com](https://rc4-0.com/caladis))
- DMRZ: Krankentransport software with Fahrten, Mitarbeiter, Fahrzeuge and Arbeitszeitkonto, plus billing to Krankenkassen ([dmrz.de](https://www.dmrz.de/software/krankentransport-und-taxisoftware))
- OC:Planner (SIEDA): Dienstplan software for Rettungsdienst, positioned at the Hilfsorganisationen (DRK, ASB, JUH, MHD) ([sieda.com](https://www.sieda.com/dienstplan-software-rettungsdienst/))
- CareMan (opta data): Dienstplan and office software for Fahrdienste and Rettungsdienste ([softguide.de](https://www.softguide.de/programm/careman-office-fuer-fahrdienst-krankentransport-rettungsdienst), [optadata.de](https://www.optadata.de/transport-und-rettungsdienste/rettungsdienste/))
- Nostradamus: Dienstplan software marketing directly to Rettungsdienst, with content on Arbeitszeitgrenzen and qualification mix per vehicle ([nostradamus-software.de](https://nostradamus-software.de/dienstplan-rettungsdienst/))
- A longer list of Krankentransport and Rettungsdienst tools is catalogued at [softguide.de](https://www.softguide.de/software/krankentransporte)

I have not evaluated any of these in depth and cannot tell you how well they cover the compliance rules your operators care about. But their existence changes two things:

1. **Your positioning claim ("nobody covers German ambulance compliance rules") is unproven.** It may still be true for the specific rules your operators struggle with. Right now it is an assumption.
2. **Your six pilots have alternatives they could buy today.** Why haven't they? The honest answers are the most valuable data you have not collected yet: too expensive for a small operator, built for the large Hilfsorganisationen rather than private operators, no billing integration, bad UX, or simply that nobody has sold to them. Each of those answers points to a different product.

This is the single most important thing to fix before committing the quarter. It does not kill the idea. Fragmented, vertical German SMB software markets with an abandoned incumbent are exactly where a focused, well-distributed entrant wins. But you need to know what you are entering.

## 3. Market size sanity check

The BKS Bundesverband, the main association of private Rettungsdienst operators, represents more than 150 member companies with around 6,500 employees, organised in eight regional associations ([bks-rettungsdienst.de](https://www.bks-rettungsdienst.de/zahlen-daten-fakten/), [Wikipedia](https://de.wikipedia.org/wiki/Bundesverband_eigenst%C3%A4ndiger_Rettungsdienste_und_Katastrophenschutz)). Private Krankentransport-only operators (no Notfallrettung) add to that number but are also smaller and lower-margin.

Rough arithmetic at your price point: if the addressable set is a few hundred private operators and you win a third of them at 400 EUR/month, you are at roughly 50k EUR MRR. That is a healthy, self-funding niche product for a services company. It is not a venture-scale outcome unless you expand to the Hilfsorganisationen (who already have vendors and long procurement cycles), to adjacent verticals (Fahrdienste, Pflege) or to adjacent functions (billing, fleet, MPBetreibV device tracking). Decide now which of those you are fine with, because the quarter's architecture decisions depend on it.

Also check whether 400 EUR/month is flat per operator or scales with vehicles or headcount. Flat pricing caps revenue at the number of operators; per-vehicle pricing tracks the value you deliver.

## 4. The cost is understated

"Two engineers, hosting only" ignores:

- **Your own time.** For a first version in a compliance domain, the domain expert (you) is the bottleneck, not the engineers. Budget at least 30 to 50 percent of your time for the quarter.
- **Opportunity cost.** Two engineers for a quarter at EnzRossi is billable capacity you are not selling. Put a number on it. That is the real budget, and 6 x 400 EUR = 2,400 EUR/month of pilot revenue does not come close to covering it. You are making an investment, not a cost-neutral experiment. That is fine; name it.
- **Regulatory and data protection cost.** You will hold employee working-time records, qualifications, and likely health-adjacent data (Impfstatus, G-Untersuchungen). That is GDPR with employee data, Auftragsverarbeitungsvertrag (AVV) with every customer, German or EU hosting expectations, and probably a Betriebsrat question at larger operators. A few thousand EUR of legal templates and some engineering time for audit logging and deletion is realistic.
- **Compliance-rule maintenance.** Rettungsdienst is regulated at Land level; there are 16 Landesrettungsdienstgesetze and they differ on crew qualification requirements, plus federal Arbeitszeitgesetz and Tarifvertrag-specific hour limits ([nostradamus-software.de](https://nostradamus-software.de/dienstplan-rettungsdienst/)). Encoding these rules is not a one-time task. Someone owns keeping them current, forever.

## 5. Risks, ranked by how likely they are to kill this

1. **Building "scheduling" instead of the specific compliance pain.** Generic scheduling is a solved, crowded problem; two engineers will not out-build Caladis or SIEDA on scheduling UX in a quarter. Your defensible wedge is whatever compliance rule the incumbents get wrong or ignore, plus your distribution through the associations. If the interviews do not clearly name that rule, you do not have a wedge yet.
2. **Pilot conversion.** Six conditional signatures becoming six paying customers depends on a shared, written definition of "first version" and a fixed start date. Without both, expect two or three to convert.
3. **Regional concentration.** If the 14 operators cluster in one or two Länder, your rule engine and your channel both validate for those Länder only. National expansion becomes a second product.
4. **Data migration.** Operators on Excel and a dead desktop tool need their staff, qualifications, vehicles and historic shift data moved. If migration is manual, you will spend the second quarter onboarding six customers instead of selling. If migration is not in scope for the first version, say so to the pilots now.
5. **Sales bandwidth.** You are the domain expert, the product owner and the only seller. This is the standard founder bottleneck; the quarter plan should not assume you can do all three well at once.

## 6. What I would do before the engineers start (one to two weeks)

1. **Re-read the 14 interview notes with one question:** which specific compliance failure has cost these operators money, an inspection finding, or a lost tender? Write the top three as one sentence each. If you cannot, run five follow-up calls that ask only that question.
2. **Ask all 8 committed or interested operators:** "Have you looked at Caladis, DMRZ, CareMan, OC:Planner or Nostradamus? Why did you not buy?" Record verbatim. This costs you eight phone calls and is worth more than any further desk research.
3. **Do a two-hour teardown of Caladis and Nostradamus** (demo request or public material). Confirm or refute your "nobody covers the compliance rules" claim per rule, not in general.
4. **Turn the pilot agreements into a one-page scope:** what the first version does, what it does not do (migration? billing? mobile app?), the delivery date, and what happens if you miss it. Get the six to initial it. This converts vague signatures into a real commitment and gives the engineers a fixed target.
5. **Cost the quarter honestly** (loaded engineer cost plus your time plus legal) and set the kill or continue criterion now: for example, at least four of six pilots paying by end of the quarter after delivery, and at least two new signed operators from association channels.

## 7. If you proceed: shape of the quarter

- Weeks 1 to 2: the validation above, in parallel with engineers setting up infrastructure, auth, tenancy, audit logging, and the data model for staff, qualifications, vehicles and shifts.
- Weeks 3 to 8: the compliance wedge first, scheduling second. Concretely: import or enter shifts, then flag violations of the two or three rules your operators named (rest time, weekly hour limits, crew qualification mix per vehicle, expiring qualifications or Fortbildung hours). A tool that only checks and reports on a plan built elsewhere is a legitimate first version and is far smaller than a full scheduler.
- Weeks 9 to 12: onboard two of the six pilots with real data, not all six. Fix what breaks. Start billing the two.
- Do not build: mobile apps, billing to Krankenkassen, fleet management, or an automatic shift optimiser. Each is a quarter on its own and each has established vendors.

## 8. Questions I would ask you

1. What are the top three compliance rules your interviewees actually named, in their words? Can you point to them in the notes?
2. Which Länder are the 14 operators in? How many vehicles and staff does the median one have?
3. What is the 15-year-old desktop tool called, and who inherited its customers, if anyone?
4. Why did none of the six buy Caladis or a comparable vertical tool? Have you asked?
5. Is the 400 EUR flat, or does it scale with vehicles or staff? How did you arrive at it?
6. What exactly did the six sign: a Letter of Intent, an order form with cancellation rights, or a contract with a delivery date? What does "first version" mean in that document?
7. What is the loaded cost of two engineers for a quarter at EnzRossi, and what billable work are they not doing?
8. Is data migration from Excel and the old tool in scope for the pilots' expectations?
9. Do you want a self-funding niche product or a venture-scale company? The answer changes how you architect for multi-Land rules and adjacent segments.
10. Who owns keeping 16 Landesgesetze and tariff rules current after launch?

## Bottom line

You have done more validation than most founders do before spending a quarter. The demand signal (six conditional paid pilots from a segment you know, replacing an abandoned tool) is real. What is missing is a truthful competitor map and a sharp definition of the compliance wedge. Spend two weeks on those, narrow the first version to compliance checking rather than full scheduling, and then commit the engineers with written pilot scope and an explicit kill criterion.

Sources consulted:
- [BKS Bundesverband, Zahlen Daten Fakten](https://www.bks-rettungsdienst.de/zahlen-daten-fakten/)
- [Wikipedia: Bundesverband eigenständiger Rettungsdienste und Katastrophenschutz](https://de.wikipedia.org/wiki/Bundesverband_eigenst%C3%A4ndiger_Rettungsdienste_und_Katastrophenschutz)
- [Wikipedia: Private Rettungsdienstunternehmen in Deutschland](https://de.wikipedia.org/wiki/Private_Rettungsdienstunternehmen_in_Deutschland)
- [Caladis](https://caladis.de/) and [RC 4.0 GmbH](https://rc4-0.com/caladis)
- [DMRZ Krankentransport-Software](https://www.dmrz.de/software/krankentransport-und-taxisoftware)
- [SIEDA OC:Planner for Rettungsdienst](https://www.sieda.com/dienstplan-software-rettungsdienst/)
- [opta data Rettungsdienste](https://www.optadata.de/transport-und-rettungsdienste/rettungsdienste/) and [CareMan-Office on softguide](https://www.softguide.de/programm/careman-office-fuer-fahrdienst-krankentransport-rettungsdienst)
- [Nostradamus: Dienstplan Rettungsdienst](https://nostradamus-software.de/dienstplan-rettungsdienst/)
- [softguide.de: Software für Krankentransporte und Rettungsdienste](https://www.softguide.de/software/krankentransporte)
