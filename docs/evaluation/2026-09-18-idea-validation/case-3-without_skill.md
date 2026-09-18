# Validation memo: AI contract summariser for SMBs ($29/month)

**Date:** 18 September 2026
**Prepared for:** Founding team
**Status:** Not validated. What you have is a working demo and a hypothesis. Below is what I can confirm, what I cannot, and what it would take to actually validate it.

---

## 1. Bottom line

I would not launch on the current evidence, and I would not spend money on marketing yet. The idea is plausible and the timing is fine, but three of your four core assumptions are either wrong or untested:

| Assumption | My read | Confidence |
|---|---|---|
| "The summaries look great" (product works) | Untested. 5 contracts, judged by you, is not evidence of quality. | High that this is untested |
| "No real competitor doing exactly this for SMBs" | Wrong. The space is crowded at every price point, including free. | High |
| "$29/month is the right price" | Untested, and the pricing model (subscription) may be mismatched to usage patterns. | Medium |
| "SMBs want this and will pay" | Untested. No customer conversations reported. | High that this is untested |

The good news: none of this kills the idea. It changes what you should do in the next 4 to 6 weeks, which is customer discovery and a real evaluation set, not a launch.

---

## 2. The competition claim does not survive a 20-minute search

You said there is no real competitor doing this for SMBs. I found the opposite. The market is dense and includes a free tier from the largest incumbent your users already have installed.

**Incumbent with distribution:** Adobe added "Contract Intelligence" to Acrobat AI Assistant in February 2025. It auto-detects that a PDF is a contract, generates an overview, extracts key terms, and its legal positioning explicitly says it highlights unusual language, missing clauses, and potential risk areas. It also compares up to 10 contracts, including scanned ones. This is your exact feature list, inside the PDF reader SMBs already use. ([Adobe news release](https://news.adobe.com/news/2025/02/acrobat-ai-assistant-contracts), [Adobe legal landing page](https://business.adobe.com/products/acrobat-business/legal.html), [Forbes coverage](https://www.forbes.com/sites/marksparrow/2025/02/04/adobe-acrobat-ai-assistant-can-now-read-and-summarise-complex-contracts/))

**SMB-priced direct competitors:** Buyer's guides for 2026 list free options (Justee, goHeather free tier, LegalChatAI), $19.99 to $89.99/month tiers (TheLawGPT), and $29 to $99/user/month entry tiers (Loio, Spellbook basic). ([LegalOn buyer's guide](https://www.legalontech.com/post/best-ai-contract-review-tools), [TheLawGPT SMB guide](https://www.thelawgpt.com/blog/ai-contract-review-small-business-guide), [aiflowreview SMB roundup](https://aiflowreview.com/ai-contract-review-tools/), [Spellbook pricing article](https://spellbook.com/learn/ai-contract-review-software-pricing))

**Generic LLMs:** Anyone with a ChatGPT, Claude, or Gemini subscription can upload a PDF and ask "summarise this and list the risky clauses." Adobe itself publishes a how-to for doing exactly this with Acrobat inside ChatGPT. ([Adobe UK guide](https://www.adobe.com/uk/acrobat/resources/how-to-summarise-contracts-with-chatgpt-and-acrobat-ai.html)) This is your real competitor for the "I have one contract to check" user, and it is priced at zero marginal cost.

**Cautionary tale on the upmarket side:** Robin AI, one of the best-funded UK legal AI startups, stopped operating independently between late 2025 and early 2026; its managed-services business was acquired and Microsoft hired its engineers. Well-funded, well-built, and still could not make the unit economics work in contract review. ([Spellbook on Robin AI](https://spellbook.com/learn/robin-ai-pricing), [Layer3 Labs guide](https://www.layer3labs.io/guides/robin-ai-explained))

**What this means for you:** "Upload PDF, get summary and risky clauses" is a feature, not a product, and it is already a feature of Acrobat and every frontier chatbot. If you want to build a company here, the wedge has to be something the generic tools do not do. Candidates:

- A specific vertical (e.g. commercial leases for independent retailers, SaaS vendor agreements for agencies, freelance/contractor agreements) where you can encode what "risky" actually means for that contract type and that user.
- A workflow, not a summary: track renewals and notice periods, alert before auto-renewal, store the obligations, integrate with where SMBs already are (Gmail, Xero/QuickBooks, Slack).
- A "compare to market" angle: "this indemnity clause is broader than 90% of the agency contracts we've seen," which requires a corpus you do not yet have.
- A pathway to a human: flag, then hand off to a lawyer for a fixed fee. This is also your main defence against the regulatory problem in section 4.

I cannot tell you which of these is right. Only customers can.

---

## 3. "Looks great on 5 contracts" is not evidence

This is the most important technical point. You are proposing to tell people which clauses in a binding document are risky. The cost of a wrong answer is asymmetric: a false negative (missing an unlimited liability clause, a non-compete, a personal guarantee) can cost the user far more than $29. Five contracts judged informally by the builders tells you nothing about the miss rate.

What "validated" would look like on the product side:

1. **An evaluation set of at least 50 to 100 real contracts** across the types you intend to support, with risky clauses labelled by someone qualified (a contracts lawyer, paralegal, or experienced commercial manager), not by you.
2. **Measured recall on risky clauses**, per clause category. Recall matters more than precision here. Decide what miss rate you can live with and whether you will disclose it.
3. **Hallucination and fabrication rate**: how often does the summary state a term that is not in the document (a payment period, a jurisdiction, a cap)? Every claim in the summary should link back to the source text; Adobe already does clickable citations, so this is table stakes.
4. **Robustness to input quality**: scanned PDFs, multi-column layouts, exhibits and schedules, tracked-changes exports, 80-page documents where the operative clause is on page 61 and overridden by an amendment on page 78.
5. **Jurisdiction sensitivity**: "risky" is not universal. A non-compete is largely unenforceable in California and routine in England. A liquidated damages clause reads differently under civil law. "Global, English first" means you will get contracts governed by US state law, English law, Australian, Indian, Singaporean, and EU-member law from day one. Does your prototype know which framework it is applying? If it applies a generic "risky" heuristic, it will be confidently wrong in a predictable share of cases.

A weekend prototype on Claude is a perfectly good way to learn whether the thing is technically feasible. It is. That question is answered. The open question is whether it is reliable enough to put a paid promise behind, and the only way to find out is to measure.

---

## 4. Regulatory and liability exposure is real and shapes the product

**Unauthorised practice of law (UPL).** In every US state, only a licensed attorney may advise on the legal effect of a contract; AI review tools position themselves as software providing general information, not legal advice, and rely on disclaimers to stay on the right side of the line. The rules are described as vague and inconsistent across jurisdictions, which is exactly the kind of uncertainty a two-person startup does not want to test. ([Thomson Reuters Institute](https://www.thomsonreuters.com/en-us/posts/government/ai-impacts-unauthorized-practice-of-law/), [Richmond JOLT](https://jolt.richmond.edu/is-your-artificial-intelligence-guilty-of-the-unauthorized-practice-of-law/), [Bloomberg Law](https://news.bloomberglaw.com/us-law-week/human-contract-review-behind-ai-might-jeopardize-your-license))

Practical consequences:

- "Here is a list of risky clauses" is closer to the advice line than "here is a summary." The phrasing, the UI, and the terms of service need to be designed with this in mind, and you need a lawyer to review them before launch, not after.
- Disclaimers reduce but do not eliminate exposure. If a user relies on your tool, signs, and gets hurt by a clause you missed, you will at minimum face a chargeback and a public complaint, and possibly worse.
- "Global" multiplies this. UK, Australia, and most EU states have their own reserved-activity or legal-services regulation. You do not need to solve all of it to start, but you need to pick where you launch and know the rules there.

**Data handling.** Contracts are among the most sensitive documents an SMB has: pricing, customer names, salaries, IP. Users will ask, before they pay, whether their contracts are used for training, where they are stored, who at your company can see them, and whether you will sign a DPA. You need real answers, including what your model provider's data terms are and how you would honour a GDPR deletion request. This is a launch blocker, not a later feature.

---

## 5. The $29/month question

I cannot validate the price without customers, but I can flag the structural problems.

**Usage pattern mismatch.** Most small businesses do not sign contracts every month. A typical 5-person agency or shop might see 3 to 10 meaningful contracts a year, clustered around a new lease, a new supplier, a new large client. That is an episodic need. A monthly subscription for an episodic need has two likely outcomes: they subscribe, use it once, and churn; or they do not subscribe at all because they would rather paste the PDF into ChatGPT for free. Alternatives worth testing:

- Per-document pricing ($15 to $49 per contract) or credit packs.
- Annual plan positioned as "insurance," bundled with renewal tracking so there is a reason to keep it running.
- A higher price point ($99 to $199/month) for a narrow segment that does sign contracts weekly (recruiters, agencies, property managers, procurement at 50-person companies), which is a different business.

**Willingness to pay is unknown.** Who is the buyer? "Small business" spans a sole-trader plumber and a 200-person logistics firm. Their contract volume, sophistication, and budget differ by two orders of magnitude. Until you can say "our user is X, who signs Y contracts a year, and currently handles them by Z," you cannot price.

**Unit economics.** At $29/month, your fully loaded cost per user has to stay well under $10 to make this work with SMB churn rates (typically 3 to 7% monthly). Long contracts with frontier models, multiple passes, and retries are not free. Model the cost of an 80-page lease with exhibits before you commit to a flat price.

---

## 6. What I would do in the next 4 to 6 weeks

Do not build more features. Do these three things in parallel.

**A. Twenty customer conversations (weeks 1 to 3).**
Pick one segment you can reach easily (through your own network, a trade association, a Reddit or Facebook group for that trade). Talk to 20 owners or ops managers. Do not demo first. Ask:

- When did you last sign a contract you did not fully understand? What did you do?
- Have you ever been burned by a clause you did not notice? What happened, what did it cost?
- Have you ever paid a lawyer to review a contract? How much? How did that feel?
- Have you tried ChatGPT or Acrobat for this? What happened?
- (Only at the end) show the prototype on one of *their* contracts. Watch what they do with the output. Ask what they would pay, then ask them to pay it.

You are looking for evidence of a painful, recurring, budgeted problem. If people say "nice, but I'd just ask my accountant / ChatGPT," that is your answer. If three of twenty pull out a card, you have something.

**B. A real evaluation set (weeks 1 to 4).**
Collect 50 to 100 real contracts (anonymised, from the customer conversations, from your own network, from public filings such as SEC EDGAR exhibits for US commercial agreements). Have a qualified person mark the genuinely risky clauses. Run the prototype. Publish the recall and hallucination numbers to yourselves. Decide if you would put your name behind them.

**C. Regulatory and data groundwork (weeks 2 to 6).**
One conversation with a lawyer who knows UPL and legal-tech in your first launch jurisdiction. Terms of service, disclaimers, data-retention policy, provider data terms, DPA template. This is a few thousand dollars and one afternoon, and it is cheaper than finding out later.

**Kill / continue criteria at the end of six weeks:**

- Continue if: a clearly defined segment describes the problem unprompted, at least 3 to 5 of 20 pay something (even $20 one-off) before launch, recall on your labelled risky clauses is above whatever bar you set (I would want 90%+ for the top 10 clause categories), and you can articulate why a user would pick you over Acrobat or ChatGPT in one sentence.
- Pivot if: the pain is real but the wedge is elsewhere (renewal tracking, obligation management, lawyer hand-off).
- Stop if: users are happy with generic tools, or the miss rate is one you would not accept for your own contracts.

---

## 7. Questions I need answered before I can go further

1. **Who exactly is the user?** Give me a person: industry, headcount, role, how many contracts a year, who reviews them today.
2. **What were the 5 contracts?** Types, length, governing law, where you got them. Were any of them scanned, amended, or over 30 pages?
3. **Who judged the summaries as "great"?** You, or someone who reviews contracts professionally?
4. **Which jurisdiction do you launch in first?** "Global" is not a launch plan. US (which state?), UK, Australia, something else?
5. **What is your data story?** Where are contracts stored, for how long, who can see them, what are your model provider's training and retention terms?
6. **What does the user do after reading the risky-clause list?** Negotiate? Walk away? Call a lawyer? Sign anyway? The answer determines whether the product is a summariser, a negotiation aid, or a lawyer-referral funnel.
7. **Why would someone use this instead of Acrobat's built-in feature or ChatGPT?** One sentence. If you cannot write it yet, that is the thing to discover.
8. **How much runway and time are you putting into this?** The plan above assumes a few weeks of founder time and low four figures in spend. If you are considering quitting jobs or raising, the bar for evidence is higher.
9. **Have you tried to sell it yet?** Not launch, sell. Has anyone been asked for money and said yes?
10. **Is there anything about the 5 contracts the prototype got wrong that you have not mentioned?** Founders tend to remember the wins.

---

## 8. Summary

- Technical feasibility: confirmed. A weekend on Claude proves the model can do it.
- Product reliability: unknown. 5 self-judged samples is not a measurement.
- Competition: the "no competitor" claim is incorrect. Adobe Acrobat ships this feature; a dozen SMB-priced tools exist; every frontier chatbot does it for free. A wedge is required.
- Demand and pricing: unknown. No customer evidence. Subscription pricing is likely mismatched to episodic usage.
- Regulatory and data: real, jurisdiction-dependent, and must be designed in before launch.

Recommendation: six weeks of customer discovery, a labelled evaluation set, and a lawyer conversation. Then decide. Do not launch or spend on acquisition until you can answer the ten questions above.

---

### Sources

- [Adobe: Acrobat AI Assistant contract intelligence announcement (Feb 2025)](https://news.adobe.com/news/2025/02/acrobat-ai-assistant-contracts)
- [Adobe: Acrobat Studio for Legal](https://business.adobe.com/products/acrobat-business/legal.html)
- [Adobe UK: How to summarise contracts with ChatGPT and Acrobat AI](https://www.adobe.com/uk/acrobat/resources/how-to-summarise-contracts-with-chatgpt-and-acrobat-ai.html)
- [Forbes: Adobe Acrobat AI Assistant can compare and summarise complex contracts](https://www.forbes.com/sites/marksparrow/2025/02/04/adobe-acrobat-ai-assistant-can-now-read-and-summarise-complex-contracts/)
- [Computerworld: Adobe enhances Acrobat AI with contract intelligence](https://www.computerworld.com/article/3816432/adobe-enhances-acrobat-ai-with-contract-intelligence-to-streamline-enterprise-workflows.html)
- [LegalOn: Best automated contract review software tools of 2026](https://www.legalontech.com/post/best-ai-contract-review-tools)
- [TheLawGPT: AI contract review for small businesses, 2026 guide](https://www.thelawgpt.com/blog/ai-contract-review-small-business-guide)
- [aiflowreview: AI contract review tools for small businesses (2026)](https://aiflowreview.com/ai-contract-review-tools/)
- [Spellbook: AI contract review software pricing in 2026](https://spellbook.com/learn/ai-contract-review-software-pricing)
- [Spellbook: Robin AI pricing and what happened to the company](https://spellbook.com/learn/robin-ai-pricing)
- [Layer3 Labs: What is Robin AI (2026)](https://www.layer3labs.io/guides/robin-ai-explained)
- [HyperStart: Spellbook pricing](https://www.hyperstart.com/blog/spellbook-pricing/)
- [Thomson Reuters Institute: AI and unauthorized practice of law regulations](https://www.thomsonreuters.com/en-us/posts/government/ai-impacts-unauthorized-practice-of-law/)
- [Richmond Journal of Law and Technology: Is your AI guilty of the unauthorized practice of law?](https://jolt.richmond.edu/is-your-artificial-intelligence-guilty-of-the-unauthorized-practice-of-law/)
- [Bloomberg Law: Human contract review behind AI might jeopardize your license](https://news.bloomberglaw.com/us-law-week/human-contract-review-behind-ai-might-jeopardize-your-license)
- [Spellbook: State bar rules on AI use](https://spellbook.com/learn/state-bar-rules-ai-use)

Note: several of these sources are vendor-published (Spellbook, LegalOn, TheLawGPT) and have an interest in how the market is described. I have used them for factual claims about pricing tiers and feature lists, which are easy to verify on the vendors' own sites, not for market-size or quality judgements.
