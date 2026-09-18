# Idea validation: AI contract summariser for small businesses

Founding team · Evidence as of 2026-09-18 · External · digital · AI-dependent · target geography stated as "global, English first" (treated here as undecided)

## Verdict

**Reshape, then test before building — Confidence: Medium (market facts are verifiable; demand facts are absent)**

The weakest point is the premise "no real competitor". A short search found the exact product, at or below your price, from incumbents with distribution: Adobe sells contract summaries inside Acrobat for $4.99/month; Rocket Lawyer includes unlimited AI red-flag review in every plan from about $12/month; and at least eight free or freemium upload-and-flag tools exist. Fixable only with a wedge the incumbents will not serve. Strongest reason it could work: a crowded market means the job is real. Next step: pick one segment and one geography and get five businesses to pay before writing more code.

## The idea as a hypothesis

Small-business owners (segment unspecified) sign contracts they do not understand and cannot afford a lawyer for each one (assumed; frequency and cost unstated). Today they read it themselves, paste it into ChatGPT or Claude, or sign blind (inferred). Proposed: PDF in, plain-English summary and risky-clause list out, $29/month (reported). Why now: frontier models make this cheap to build (true for everyone). Unfair advantage: none stated. Evidence: a weekend prototype on five self-chosen contracts that "look great" to the builders, not to a lawyer or buyer.

## What the evidence shows

**1. Market: crowded, and the incumbents own the channel.** Adobe's Acrobat AI Assistant (announced 4 Feb 2025) automatically recognises contracts, generates an overview and key terms with clickable citations, compares up to 10 contracts, and sells as a $4.99/month add-on to free Reader, in English worldwide ([Adobe news release](https://news.adobe.com/news/2025/02/acrobat-ai-assistant-contracts), read 2026-09-18). Rocket Lawyer's pricing page lists Standard, Plus and Pro plans at $12.41, $20.75 and $29.08/month, all with "Unlimited Rocket Copilot AI" that will "point out key terms and red flags" on uploaded contracts ([rocketlawyer.com/pricing](https://www.rocketlawyer.com/pricing), read 2026-09-18; likely annual-billed equivalents). A roundup dated April 2026 lists Legitt AI ($14.99–24.99/mo, free tier), ContractCrab ($3/contract), Pact ($49.99/yr), goHeather ($99/mo), and ChatGPT Plus or Claude Pro at $20/mo ([Pact blog](https://www.usepact.org/blog/post/best-ai-contract-review-tools-freelancers-small-business)); Justee, Lexitize, Clause AI and ContractReview.legal also advertise free upload-and-flag review (landing pages seen 2026-09-18, not verified). PDF-in, summary-out is the category's free tier; $29/month sits above Rocket Lawyer's top plan, which also bundles templates and lawyer access.

**2. AI fit: the thin-layer problem.** The prototype is Claude with a prompt; the customer can open claude.ai or Acrobat and get the same output, so you need a reason they would not. Five chosen contracts is a demo, not evidence: untested on scanned PDFs, long MSAs, non-US governing law, or contracts whose risk is a missing clause. A missed indemnity or auto-renewal costs the buyer real money, and the owner is exactly the reviewer who cannot catch the miss. Nobody qualified has graded accuracy.

**3. Buyer and route: unnamed.** "SMB, global" is not a segment. The owner being user, buyer and decision maker helps, but no channel is named and no reason given why they find you before Adobe or Rocket Lawyer, who already sit in their workflow. No one has paid, trialled or joined a waitlist; demand evidence is at the "we think" level.

**4. Regulatory boundary.** Whether a consumer tool that flags "risky clauses" is unauthorised practice of law is unsettled in the US and varies by state; an NCSC white paper (Aug 2025) proposes reforms and Feb 2026 commentary notes no uniform definition exists ([Thomson Reuters Institute](https://www.thomsonreuters.com/en-us/posts/government/ai-impacts-unauthorized-practice-of-law/)). A question for a lawyer, not a reason to stop, but it argues for one jurisdiction first.

**5. Viability.** Value: Unknown. Usability: Supported. Feasibility: Supported for the demo, Unknown at production accuracy. Business viability: Concern — priced above incumbents with weaker distribution; the dominant cost driver will be customer acquisition, not model usage. No unit economics computed: no acquisition cost, volume or churn supplied.

## Reshape options worth testing

The job is real; the generic form is taken. Wedges incumbents are unlikely to serve: one vertical's recurring contract type (retail leases, construction subcontracts, agency or influencer deals) where "what is normal in this market" beats a general summariser; a non-US English jurisdiction (UK, Australia, Ireland, Singapore) where Rocket Lawyer's US data helps less; or an embed in an accountant's or broker's workflow rather than a destination site.

## Cheapest test that could change the verdict

Concierge pre-sale, four weeks, no new code. One vertical, one country. Reach 30 owners through a channel you can actually use (trade association, co-working community, accountant partner). Offer a paid review of one real contract within 24 hours at $29/month or a one-off $49, produced with the prototype and checked by you. Pass (proposed): 5 of 30 pay and 3 would send the next contract. Kill (proposed): fewer than 2 pay, or a lawyer spot-checking 10 outputs finds a material missed risk in more than one. Ask each payer why they did not use Acrobat or ChatGPT.

## Questions that still matter

1. Which specific type of business and which country first, and why that one? A concrete answer turns "reshape" into "test"; "global SMB" keeps it at reshape.
2. Who outside the team has seen an output, what was their reaction, and has anyone offered to pay? Any payment or repeat request moves confidence up sharply.
3. How did you judge the five summaries as "great"? If a lawyer graded them for missed risks, say what they found; if not, the feasibility claim is unsupported.
4. What can you reach that Adobe and Rocket Lawyer cannot: a community, a vertical's data, a partner channel? No answer means no defence against copying.
5. What decision hangs on this: a side project, or leaving jobs and raising money? The bar for evidence differs by an order of magnitude.

## Boundaries

Unauthorised-practice-of-law exposure by jurisdiction, liability disclaimers and data-protection duties for uploaded contracts (GDPR if any EU customers) need a lawyer before launch. This memo prepares your decision; it does not replace legal or financing advice.
