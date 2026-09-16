# Sources

Sources that informed the method in `methodology.md`, with what each contributed. The method, including the sixteen-dimension structure, the knockout rules, the neutrality rule, and the option profiles, is EnzRossi's synthesis. Named frameworks belong to their authors.

## Differentiation, core versus commodity

- **[In Defense of Not-Invented-Here Syndrome](https://www.joelonsoftware.com/2001/10/14/in-defense-of-not-invented-here-syndrome/)** — Joel Spolsky, 2001. Core business functions should be done in-house regardless of cost; the argument for building where differentiation lives.
- **[Utility vs Strategic Dichotomy](https://martinfowler.com/bliki/UtilityVsStrategicDichotomy.html)** — Ross Pettit, on martinfowler.com, 2010. Treat utility systems and strategic systems differently: buy and standardize the former, build and optimize for speed on the latter; only a small share of most portfolios is strategic.
- **Dealing with Darwin** (2005) and the **[core versus context talk](https://thebln.com/2011/09/context-core-geoffrey-moore-at-business-of-software-video-transcript/)** — Geoffrey Moore. Core is what amplifies differentiation; mission-critical is not the same as core. Our decomposition test uses this distinction.
- **[IT Doesn't Matter](https://hbr.org/2003/05/it-doesnt-matter)** — Nicholas Carr, Harvard Business Review, 2003. Infrastructural technology becomes commodity; spend less and follow rather than lead on commodity.
- **[Wardley Mapping](https://learnwardleymapping.com/introduction/)** and **[Pioneers, Settlers, Town Planners](https://blog.gardeviance.org/2015/03/on-pioneers-settlers-town-planners-and.html)** — Simon Wardley (mapping released under Creative Commons). The evolution of components from genesis to commodity, and the idea that the right way to source and staff a component depends on its stage. Our "maturity of the problem" dimension follows this idea.

## Build-versus-buy frameworks (attributed, not copied)

- **[Build vs. buy: a strategic framework for evaluating third-party solutions](https://www.thoughtworks.com/insights/e-books/build-versus-buy-strategic-framework-for-evaluating-third-party-solutions)** — Thoughtworks, 2022. Scoping buy decisions at a finer grain than the whole system; consistent evaluation criteria; usage breakpoints that trigger a revisit. Our decomposition step and "revisit at usage breakpoints" guidance draw on these concepts.
- **[Build vs. buy strategy: top principles for enterprise applications](https://www.gartner.com/en/doc/build-vs-buy-strategy-top-principles-for-enterprise-applications)** — Gartner. Buy where possible, build where it differentiates, integrate everything.
- **[Buy, boost, or build? Choose your path to generative AI](https://mitsloan.mit.edu/ideas-made-to-matter/buy-boost-or-build-choose-your-path-to-generative-ai)** — MIT Sloan / MIT CISR. The trade-offs among buying, augmenting a vendor's offering with proprietary data, and building.

## Lock-in, reversibility, and options

- **[Don't get locked up into avoiding lock-in](https://martinfowler.com/articles/oss-lockin.html)** — Gregor Hohpe, 2019. Lock-in has many forms, including in things you build; the trade-off is switching cost against unique utility; reducing lock-in is an option with a price. Basis for rating the exit of every option rather than treating lock-in as a vendor property.
- **[Managing technical lock-in in the cloud](https://www.gov.uk/guidance/managing-technical-lock-in-in-the-cloud)** — UK Government Digital Service. Some lock-in is worth accepting; estimate switching cost in business cases; test portability periodically.
- **[Amazon 2015 shareholder letter](https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm)** — Jeff Bezos. One-way versus two-way door decisions; the speed a decision deserves depends on its reversibility.
- **[Real Options Underlie Agile Practices](https://www.infoq.com/articles/real-options-enhance-agility/)** — Chris Matts and Olav Maassen, 2007. Options have value and expire; do not commit early without a reason. Basis for the "wait or validate" option and for expiry conditions on recommendations.
- **Bezos on undifferentiated heavy lifting** — as [reported from a 2006 MIT talk](https://www.artima.com/weblogs/viewpost.jsp?thread=178569). Most engineering effort in a company goes to work that does not differentiate it; the opportunity-cost argument for buying commodity.

## Total cost and hidden costs of building

- **[Total cost of ownership (TCO)](https://www.gartner.com/en/information-technology/glossary/total-cost-of-ownership-tco)** — Gartner glossary. Cost assessed over the full life, including support, downtime, and training.
- **[Frequently Forgotten Fundamental Facts about Software Engineering](https://dl.acm.org/doi/10.1109/MS.2001.922739)** — Robert L. Glass, IEEE Software, 2001. Maintenance consumes the majority of a software system's lifetime cost. Basis for the statement that maintenance, not build, dominates the cost of building.

## External providers, outsourcing, and knowledge

- **[Global Outsourcing Survey 2024](https://www.deloitte.com/global/en/issues/work/global-outsourcing-survey.html)** — Deloitte. Cost has declined as the primary reason for outsourcing; a majority of organizations have selectively brought previously outsourced work back in-house; vendor-management capability is often immature. Informs the "cost is the only argument" warning and the capacity-to-manage dimension.
- **[A review of the IT outsourcing empirical literature and future research directions](https://eprints.lse.ac.uk/26386/)** — Lacity, Khan, Willcocks, Journal of Strategic Information Systems, 2009. Relationship management and the capabilities of both client and supplier are persistent success factors.
- **[How Do Committees Invent?](http://www.melconway.com/Home/Committees_Paper.html)** — Melvin Conway, 1968, and **[Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html)** — Martin Fowler, 2022. System structure mirrors communication structure; an isolated external team produces an isolated component. Basis for the management notes on partners.
- **[Team Topologies: key concepts](https://teamtopologies.com/key-concepts)** — Matthew Skelton and Manuel Pais, 2019. Team cognitive load as a design constraint; team types and interaction modes. Informs the internal-capacity and management-capacity dimensions.

## Hiring realities

- **[SHRM 2025 benchmarking reports](https://www.shrm.org/about/press-room/shrm-releases-2025-benchmarking-reports--how-does-your-organizat)** — Society for Human Resource Management, 2025. Cost per hire and time to fill benchmarks; few organizations measure quality of hire. Cited as context only; the organization's own hiring data overrides it.
- **[Time to hire by industry](https://resources.workable.com/stories-and-insights/time-to-hire-industry)** — Workable, 2023. Engineering roles take longer to fill than most.
- **The Mythical Man-Month** — Frederick P. Brooks Jr., 1975. Ramp-up and communication overhead mean added people do not add capacity immediately.
- **[Do Things that Don't Scale](https://paulgraham.com/ds.html)** — Paul Graham, 2013. Doing a capability manually while learning what is needed is a legitimate path; basis for the "wait or validate" option.

## EnzRossi methodology

The decomposition test, the sixteen-dimension rubric in four groups, the eight option profiles, the knockout rules, the two bias lists and the neutrality rule, the cost-driver table, and the exit and transition patterns are EnzRossi's synthesis from delivery and staffing practice and the sources above. EnzRossi sells engineering and staff-augmentation services; the neutrality rule exists because of that.
