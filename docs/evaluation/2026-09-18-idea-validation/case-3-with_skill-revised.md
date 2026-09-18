# Idea validation: AI contract summariser for small businesses

Founding team · Evidence as of 2026-09-18 · External · digital · AI-dependent · target "global, English first" (undecided)

## Verdict

**Reshape — Confidence: Medium (competitor and price facts are cited; demand facts are absent)**

The premise "no real competitor doing exactly this for SMBs" is wrong, and that is the weakest point. Upload-a-PDF, plain-English summary, risk flags for small businesses exists today at $0 to $39/month from at least six named products, and Adobe sells it inside Acrobat for $4.99/month. This is fixable, not fatal: a crowded field means demand is real; your question is the wedge. The strongest reason it could work is that SMB owners pay $300–$1,000 for a lawyer to review a standard agreement, so a price in between is plausible. Next step: pick a segment and run a paid concierge test before writing more code.

## The idea as a hypothesis

Small-business owners (reported) receive contracts they do not fully understand and today sign unread, ask a friend, or pay a lawyer (inferred; you have not said what your five test users do). Solution: upload PDF, get summary and risk list, $29/month. Why now: frontier models read contracts well (observed on five chosen contracts). Unfair advantage: none stated. The problem is real but infrequent; a firm that signs two contracts a year does not sustain a subscription (inferred).

## What the evidence shows

**1. Crowded market, price floor near zero.** ContractCrab: $3 per contract or $30/month. Legitt AI: free for 10 contracts/month. Legly: free for 2 reviews per 90 days, $39/user/month unlimited. Pact: $49.99/year. goHeather: from $400/month per seat. LegalZoom Doc Assist: an AI summariser offered as a free lead generator for attorney plans. Adobe Acrobat AI Assistant added Contract Intelligence in February 2025 at $4.99/month. Docusign launched an AI review assistant for its CLM customers in March 2026 (sources and dates in appendix). These pages show products exist at these prices, not that customers pay or stay. $29/month sits above most direct alternatives with no stated difference.

**2. Thin layer over the model.** Users can already drop a PDF into ChatGPT or Claude at $20/month; the Pact comparison lists both as alternatives for this use. A prompt and an upload form do not defend against the model vendor, Adobe, Docusign or LegalZoom, who all have distribution you lack. Defence must come from a segment-specific playbook, a workflow (obligations, renewals), a channel (accountants, e-signature platforms, associations) or a jurisdiction the large players ignore.

**3. AI fit plausible, untested.** Five contracts you chose, judged by you, support a hypothesis, not a claim. LegalOn's 2026 benchmark (vendor-published) finds general models find clauses but fail on numeric thresholds, cross-references and absence checks; ContractEval (arXiv, August 2025) rates most LLMs at junior-legal-assistant level on clause-level risk. The costly error is the missed clause: an owner who trusts a "no major risks" summary cannot detect it, and signing is not reversible. That shapes positioning ("prepare for the lawyer", not "replace the lawyer") and liability.

**4. Demand and route unknown.** Nobody has paid, committed, trialled or been interviewed. "Global, English first" is not a beachhead; contract norms, consumer law and buying habits differ by country. No channel to the owner-operator is named.

Four risks: value Unknown; usability Supported; feasibility Concern (accuracy on messy contracts); business viability Concern (price above the field, no channel, low frequency).

## Cheapest test that could change the verdict

Concierge pre-sale in one segment, one country, two weeks. Recruit 20 SMB owners with a contract on their desk this month; offer a summary and risk list within 24 hours for a one-off $49, paid upfront, produced with your prototype plus your own review. Measure who pays, what they would have done otherwise, and who would buy again. Proposed pass: 8 of 20 pay and 5 would pay again; proposed kill: fewer than 3 pay. No new code. Thresholds are proposed until agreed before the test. Owners paying per contract but refusing a subscription would move the verdict to "pursue with per-document pricing".

## Questions that still matter

1. Whose five contracts did you test, and what did those people do with their previous contract? (Real past behaviour raises demand confidence; "our own contracts" lowers it.)
2. Which one country and segment first, and why? (A named, reachable segment moves this toward "test before building".)
3. How often does the target SMB receive a contract, and what does review cost them today? (Decides subscription versus per-document.)
4. Has the prototype missed a clause a lawyer would flag, and how do you know? (A 30–50 contract sample with a lawyer's judgement is the AI-fit test.)
5. What decision hangs on this: weekend project, side business, or quitting jobs? (A venture bet needs a defence against Adobe, Docusign and model vendors; a lifestyle business tolerates copying.)

## Boundaries

Whether paid risk-flagging counts as legal advice or unauthorised practice of law, disclaimer wording and liability for a missed clause are questions for a lawyer in each target jurisdiction. Data protection for uploaded contracts (GDPR, UK GDPR, US state laws) is a specialist question. Delivery estimate is out of scope. The memo prepares your decision; it does not make it.

## Appendix: alternatives found (web research, 2026-09-18)

| Product | What it does | Price as listed | Source, date |
|---|---|---|---|
| ChatGPT Plus / Claude Pro | Upload PDF, ask for summary and risks | Free tier; $20/mo | Pact comparison, updated 2026-06-02 |
| Adobe Acrobat AI Assistant | Contract Intelligence: overview, key terms, cited summaries, compare up to 10 contracts | $4.99/mo add-on (US) | Adobe newsroom, 2025-02-04 |
| LegalZoom Doc Assist | AI contract summary, clause summaries; "does not provide legal advice"; funnels to attorney plans | Positioned as free; price not shown | legalzoom.com/ai/doc-assist, read 2026-09-18 |
| Legitt AI | Clause-by-clause breakdown | Free for 10/mo; $14.99/user/mo | Pact comparison, 2026-06 |
| ContractCrab | Plain-language breakdown, PDF/DOCX upload, SMB positioning | $3/contract; $30/mo | Pact comparison, 2026-06 (vendor site returned HTTP 500) |
| Legly | AI review against guidelines | Free: 2 reviews/90 days; Professional $39/user/mo | legly.io/pricing, read 2026-09-18 |
| Pact | iOS app for freelancers' contracts, leases, NDAs | Free tier; $49.99/yr | Pact comparison, 2026-06 (vendor's own page; treat as marketing) |
| goHeather | Lawyer-trained review, redlines, Word add-in, SMB and in-house | Starter $400/mo, 1 seat | goheather.io/pricing, read 2026-09-18 |
| Justee | Free AI review, paid analysis | "$50 instead of $500+ lawyer fees" (search snippet, unverified) | justee.ai, search result 2026-09-18 |
| Docusign AI contract review assistant | Risks, redlines, playbooks inside Docusign CLM/IAM | Not disclosed; enterprise | PR Newswire, 2026-03-25 |
| Spellbook | Word add-in for lawyers | Custom, reported ~$99–350/user/mo | Pact comparison, 2026-06 |

Lawyer-review comparison: flat fees of roughly $300–$1,000 for a standard agreement and hourly rates of $150–$400 are quoted by several US legal-marketplace sites (search results 2026-09-18; marketing content, US-centric, not a survey).

Accuracy references: LegalOn Contract Review Benchmark 2026 (vendor-published; general models "failed on precise language, numeric thresholds, multi-part requirements, cross-references, and absence checks"); ContractEval, arXiv 2508.03080, August 2025 (19 models on CUAD; most "performed comparably to junior legal assistants").

Sources: goheather.io/pricing; legly.io/pricing; legalzoom.com/ai/doc-assist; news.adobe.com (2025-02-04); prnewswire.com Docusign release (2026-03-25); usepact.org comparison (2026-06-02); legalontech.com benchmark 2026; arxiv.org/abs/2508.03080.
