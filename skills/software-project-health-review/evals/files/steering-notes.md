# Customer Portal Rebuild — Steering Committee Notes

## 12 June 2026 (PMO: Helen W)
Status: GREEN
- Launch date: 15 October 2026.
- Invoices epic on track; dashboard delivered early.
- Risk: SSO vendor sandbox not yet provisioned. Owner: Priya N. Mitigation: chasing vendor account manager.
- Ask: none.

## 10 July 2026 (PMO: Helen W)
Status: GREEN
- Launch date: 15 October 2026 (under review pending vendor).
- Invoices epic complete except export. Support epic progressing.
- Payments epic started; card payment flow to begin Sprint 7.
- Risk: SSO vendor sandbox not yet provisioned. Owner: Priya N. Mitigation: chasing vendor account manager.
- Product asked whether live chat can be included; to be discussed.

## 7 August 2026 (PMO: Helen W)
Status: GREEN
- Launch date revised to 30 November 2026 to accommodate vendor dependency and additional scope requested by Sales (live chat, knowledge base, bulk download).
- Payments epic in progress.
- Risk: SSO vendor sandbox not yet provisioned. Owner: Priya N. Mitigation: chasing vendor account manager.
- Risk: Sales has committed portal availability to two accounts for 1 December. Owner: Sales.
- Live chat inclusion: to be discussed with Product next meeting.

# Engineering standup digest (Slack #portal-team), 21 July – 8 August 2026
- 21 Jul: Priya — still no SSO sandbox, vendor says "next week" again. Marcus — invoice export done, picking up notification center. Diego — payment methods UI mostly done, waiting on webhook design decision.
- 23 Jul: Priya — no sandbox. Diego — webhook design: do we handle retries ourselves or use provider's? Need decision from architecture, asked Raj. Sofia — attachments finishing.
- 28 Jul: Priya — sandbox: vendor escalated internally, no date. Diego — still waiting on webhook decision. Marcus — multi-currency bug reopened, rounding differs from billing system.
- 30 Jul: Diego — webhook decision still open; started card payment UI without it. Sofia — picking up live chat spike since it's now in scope?
- 4 Aug: Priya — no sandbox. Marcus — multi-currency: billing team says their totals are correct, ours differ. Sofia — live chat vendor options, unclear if it's in scope.
- 6 Aug: Diego — webhook: Raj said he'd look this week. Marcus — notification center in progress. Priya — asked Helen whether we should build against a mock IdP instead; Helen to raise at steering.
- 8 Aug: Priya — no sandbox. Diego — session expiry bug found in payment flow, could be a problem for card payments. Team asked: what is the definition of "launch" — all epics or just invoices and support?
