# Research Notes — Legal Research Platform

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal; not referenced in the final document)
Joint-review context: this pass resolves the coupling flag recorded by the case-law-research-platform pass (2026-09-07), which recommended joint review of the two leaves when this one was processed.

## Research Goal

Understand what a Legal Research Platform actually is as an Application Type: what exists inside it, who uses it, how research work flows, which states and rules matter, and where its boundary lies — above all against the Case Law Research Platform (the sibling leaf whose pass flagged a coupling), and against eDiscovery, docket management, drafting, and regulatory-change neighbors.

## Initial Boundary

Working hypothesis before research:

- Core use: legal professionals research the whole body of law — not only judicial decisions but also legislation, regulations, court rules, and secondary/analytical sources — as first-class content.
- Likely users: attorneys (litigation and transactional), paralegals, law librarians/KM, in-house counsel, government lawyers, law students.
- Nearest neighbors: Case Law Research Platform (case-law core of the same market), eDiscovery (party documents), Legal Docket Management (procedural records), Legal Drafting Platform / Legal Document Automation (work-product production), Regulatory Change Management (obligation monitoring), Academic Search Engine (scholarly corpus), Legal Matter Management (matter files).
- Open questions: Is "multi-family breadth" the defining invariant, or is the citator? Does the free pole fit? Is this leaf a distinct Type or a variant/facet of Case Law Research Platform (the fold candidate from the prior pass)?

## Research Questions

1. What content families exist inside these products, and which are first-class?
2. What does retrieval look like across families (citation, topic, question, browse)?
3. How does authority validation work when the authority is a statute or regulation, not a case?
4. What editorial layers exist (headnotes, annotated statutes, practice notes, standard documents, encyclopedias)?
5. How do users organize ongoing research (folders, notes, history, alerts, trackers)?
6. What interfaces exist (search, results, document viewers per family, citator, guidance surfaces)?
7. Which rules matter (currency/point-in-time law, jurisdiction scoping, access, citation conventions)?
8. How do variants differ (jurisdiction scope, access model, AI depth, audience packaging, practice verticals)?
9. Where exactly is the boundary vs Case Law Research Platform — and is the fold candidate (case-law as a facet of LRP) or keep-both the right outcome?

## Representative Products

Selected for market representation + documentation quality + different philosophies + different customer tiers. Four commercial products carry over from the case-law pass (fetched 2026-09-07 from official pages; observations reused with that provenance); two new fetches on 2026-09-08 add the secondary-content layer and the free multi-family pole.

| Product | Vendor | Pole | Evidence tier reached |
|---|---|---|---|
| Westlaw (Edge / Advantage) | Thomson Reuters | dominant commercial, editorial-suite philosophy, tiered editions | Tier 2 product pages (overview, KeyCite — 2026-09-07; Practical Law — 2026-09-08) |
| Lexis+ | LexisNexis | dominant commercial, modular suite | Tier 2 product pages (overview, Shepard's — 2026-09-07; Practical Guidance — 2026-09-08) |
| Bloomberg Law | Bloomberg Industry Group | all-in-one flat-price platform, dockets/news depth | Tier 2 product pages (home, legal research — 2026-09-07) |
| vLex (part of Clio) | vLex | global/multi-jurisdiction + AI | Tier 2 product pages (home, vLex Library — 2026-09-07) |
| LII (Legal Information Institute) | Cornell Law School (non-profit) | free public multi-family pole | Tier 1 homepage (2026-09-08) |

Rejected candidates: Jus Mundi (global arbitration research specialist) — 403 on both attempts (jusmundi.com and www.jusmundi.com/en/home), abandoned per network rules; CanLII — 403 ×2 in the prior pass. The global-specialist and free-international poles are therefore under-sampled (see Uncertainties).

## Sources

Fetched 2026-09-07 (prior case-law pass, reused with provenance):

- Westlaw overview — https://legal.thomsonreuters.com/en/products/westlaw
- KeyCite — https://legal.thomsonreuters.com/en/products/westlaw/keycite
- Lexis+ overview — https://www.lexisnexis.com/en-us/products/lexis-plus.page
- Shepard's Citations Service — https://www.lexisnexis.com/en-us/products/shepards.page
- Bloomberg Law home — https://pro.bloomberglaw.com/
- Bloomberg Law Legal Research — https://pro.bloomberglaw.com/products/legal-research-and-software/legal-research/
- vLex home — https://vlex.com/
- vLex Library — https://vlex.com/vlex-library
- CourtListener home + case-law coverage wiki (free pole for the sibling Type) — https://www.courtlistener.com/ , https://wiki.free.law/c/courtlistener/help/data-coverage/case-law

Fetched 2026-09-08 (this pass):

- Practical Law — https://legal.thomsonreuters.com/en/products/practical-law
- LexisNexis Practical Guidance — https://www.lexisnexis.com/en-us/products/practical-guidance.page
- LII (Legal Information Institute) — https://www.law.cornell.edu/

Abandoned after failures:

- Jus Mundi — https://jusmundi.com/ and https://www.jusmundi.com/en/home — 403 ×2
- CanLII — 403 ×2 (prior pass)

Source-access limitation: no vendor's in-product help center / user guide was reachable at operational depth (Westlaw help lives behind sign-in; Lexis+ subpages are hero pages; the Practical Law page is navigation-heavy). All evidence is from official product/marketing pages and the LII public site. Consequently: no precise numeric limits, no exact state names, no pricing figures are asserted in the final document; vendor figures (e.g., "1B+ documents", "100+ countries", "650+ attorney-editors") are recorded here as vendor claims only.

## Product Observations

### Westlaw (Thomson Reuters) — evidence layer A (direct, official pages; 2026-09-07 + 2026-09-08)

- Self-description: "legal research service" / "legal research software"; tiered editions (Westlaw Edge, Edge with AI-Assisted Research, Westlaw Advantage).
- KeyCite: "verify whether a case, statute, regulation, or administrative decision is still good law… and find citing references to support your legal argument" — authority validation explicitly spans content families (decisions AND statutes AND regulations).
- KeyCite Alerts: "monitor the status of your case, statute, administrative decision, regulation, patent or trademark" — monitoring spans families.
- Quick Check: upload legal documents → report of authority missed or contrary.
- Litigation analytics: judges, courts, attorneys, law firms, damages, case types.
- Search: WestSearch Plus; AI-Assisted Research; Deep Research (agentic); Claims Explorer; Litigation Document Analyzer.
- Editorial claim: "100 years of editorial enhancements"; Practical Law sold alongside (separate product).
- **Practical Law (2026-09-08 fetch)**: "Legal Resources & Know-How for Professionals"; "Draft faster with standard documents and clauses"; "practice notes that provide plain-language explanations of complex legal issues and help you get up to speed on a new or existing matter"; "resources are written and maintained by over 650 dedicated, full-time attorney-editors globally"; "guides, templates, and checklists". Site taxonomy separates "Legal research & guidance" from "Drafting software, service & guidance" — the vendor itself polices the research-vs-drafting seam.
- Audience segmentation: law firms under/over 10 attorneys, businesses, government.

### Lexis+ (LexisNexis) — evidence layer A (2026-09-07 + 2026-09-08)

- Self-description: "advanced legal research platform"; modules: Legal Research, Practical Guidance, Litigation Analytics, Document Analysis, Legal News Hub; AI layer "Lexis+ with Protégé".
- Shepard's: "Is it good law?" — "the most comprehensive editorial analysis of case law, statutes, regulations, administrative decisions and more" — validation spans families; headnote-level signals; "Reason for Shepard's Signal"; "Analysis by Court" grid.
- Lexis Answers (NL Q&A); Search Term Maps; Document Analysis (upload → validate research, missing authorities).
- Folders: shareable with team; FAQ confirms folders and alerts carry over.
- Content breadth claim: "more case law, more unreported case law, more verdicts and settlements, more briefs, pleadings, motions" per jurisdiction.
- **Practical Guidance (2026-09-08 fetch)**: features — Intuitive Navigation; Resource Kits ("all the relevant practical guidance for a specific task"); State Law Comparison Tool ("compare laws across multiple jurisdictions including state and federal"); Automated Templates ("build your document based on answers you supply to an interactive questionnaire"); Legal Developments ("impact analysis and end-to-end coverage of emerging legal developments in your practice area"); Trackers ("monitor statutory, case law and regulatory developments"). ~30 practice areas listed (AI & Technology … Trusts and Estates). Sold inside Lexis+ ("Try Practical Guidance on Lexis+ with Protégé").
- Audience: small/medium/large firms, corporate legal, law schools, government; online store for 1–3 attorney firms.

### Bloomberg Law — evidence layer A (2026-09-07)

- Self-description: "all-in-one legal platform"; components: Legal Research, Workflow Tools, Practical Guidance, News and Analysis; separate Dashboard Legal.
- Research page: "brings together primary and secondary sources, trusted legal news, expert analysis, and purpose-built AI"; "AI-assisted search and powerful filtering"; flat-price posture ("one platform, one price", "without paying upcharges").
- Practice organization: 13 practice centers (Antitrust … Trademarks & Copyrights); "In Focus" emerging-topic resources, trackers, chart builders.
- Dockets: AI-powered docket search and analysis; customer quotes emphasize docket depth as differentiator.
- News: 40+ news channels; Bloomberg Terminal integration.
- Litigation/business intelligence: track cases, judges, law firms; competitor and litigation-trend analytics.
- Audience: law firms, in-house counsel, government, law schools.

### vLex (part of Clio) — evidence layer A (2026-09-07)

- Self-description: "AI engineered for lawyers" (Vincent) backed by "the world's most comprehensive legal database"; products: Vincent AI, vLex Library, Docket Alarm, vLex Labs, Fastcase Library.
- vLex Library: "over one billion legal documents from 100+ countries"; "350K+ daily updates"; "2,500+ data sources" (vendor claims).
- Precedent Map: citation analysis visualization — "positively cited, criticized, or overruled"; filter by treatment type, legal concepts, jurisdiction.
- Key Passages: most-cited paragraphs of opinions.
- Cited Authorities: "the complete citation landscape of any case at a glance, distinguishing between case law and legislation"; **amendment alerts when relied-on statutes change**; **point-in-time legislation views ("legislation as it existed at any point in time")** — statute currency as a first-class behavior.
- Search modes: Smart Searchbar (typeahead), Browsing the Law (jurisdictions, courts, practice areas), Advanced Search (Boolean + precision filters), Comparative Research (multi-jurisdiction simultaneous).
- Vincent AI: NL Q&A "with proper citations", 50-state surveys, contract analysis, judge/opposing-counsel profiling.
- Docket Alarm: "850+ million court records with real-time alerts, litigation analytics, and powerful APIs" (vendor claim).
- Fastcase Library: "U.S. primary law database providing coverage of cases, statutes, regulations, court rules, and constitutions with powerful visualization tools".
- Audience: large/small firms, legal departments, bar associations, law schools, law librarians, government; Word/Outlook/iManage integrations; SOC2/ISO 27001 claims.

### LII (Legal Information Institute, Cornell Law School) — evidence layer A (2026-09-08)

- Self-description: "We believe that everyone should be able to read and understand the laws that govern them, without cost." Activities: "Publishing law online, for free. Creating materials that help people understand law. Exploring new technologies that make it easier for people to find the law."
- **Multi-family primary law as first-class navigation**: Constitution; U.S. Code; C.F.R.; Supreme Court; Executive Orders; Federal Rules (appellate, civil, criminal, evidence, bankruptcy); State law and State regulations ("LII now publishes state regulations for all 50 U.S. states"); U.C.C.; locators for Uniform law, State statutes by topic, World law.
- **Secondary/analytical layer**: Wex Legal Dictionary & Encyclopedia (original content, new entries listed); Congressional Research Service's U.S. Constitution Annotated (with updates referencing recent Supreme Court decisions — an annotated-statute layer linking legislation to cases); LII Supreme Court Bulletin; Introduction to Basic Legal Citation; Parallel Table of Authorities; RiO Citation Resolver; Table of Popular Names; Gender Justice Collection.
- Currency claims: "The U.S. Code is up to date through the most recent version published by the Office of the Law Revision Counsel. The CFR is up to date."
- Browse surfaces: "Learn About" (Administrative Law, Civics, Constitutional Law, …), Legal Topics (Business Law, Criminal Law, …).
- Free access posture: donation/sponsor-supported; lawyer directory and advertising as support.
- No citator/treatment-evaluation layer observed; citation machinery is lookup/resolver-level (RiO Citation Resolver, citation guide).

## Cross-product Comparison

| Structure | Westlaw | Lexis+ | Bloomberg Law | vLex | LII | Reading |
|---|---|---|---|---|---|---|
| Judicial decisions as first-class family | yes | yes | yes | yes (global) | yes (Supreme Court) | universal → core family |
| Legislation as first-class family | yes (KeyCite covers statutes) | yes (Shepard's covers statutes; folders for statutes) | yes (primary sources) | yes (point-in-time views, amendment alerts) | yes (U.S. Code, state statutes) | universal → core family |
| Regulations / court rules as first-class family | yes (KeyCite covers regulations) | yes (Shepard's covers regulations) | yes | yes (Fastcase: regulations, court rules) | yes (C.F.R., Federal Rules, state regulations) | universal → core family |
| Secondary / analytical sources as first-class family | Practical Law (practice notes, standard documents, checklists) | Practical Guidance (resource kits, practice areas) | practice centers, news & analysis | secondary sources in library | Wex encyclopedia, Constitution Annotated, Bulletin | universal → core family |
| Retrieval: citation / party / topic / question | WestSearch Plus, AI-Assisted | Lexis Answers, Search Term Maps | AI-assisted search + filters | 4 named modes incl. comparative | search + browse + citation resolver | universal → defining |
| Authority validation spanning families (citator) | KeyCite (cases, statutes, regulations, admin decisions) | Shepard's (cases, statutes, regulations, admin decisions) | not directly observed | Precedent Map + statute amendment alerts | **absent** (lookup only) | common commercial → standard capability, not defining |
| Editorial aids on primary law | "editorial enhancements" | headnotes, most-cited headnote | practice centers | Key Passages | Constitution Annotated, Wex | common → standard capability |
| Practice guidance / know-how layer | Practical Law | Practical Guidance | Practical Guidance component | (secondary sources) | (encyclopedia-level only) | common commercial → standard capability |
| Research organization (folders, alerts, trackers) | KeyCite Alerts; folders | folders (shareable) + alerts | trackers | alerts (incl. statute amendment) | (not observed) | common → standard capability |
| Document/brief analysis | Quick Check | Document Analysis | (AI tools) | Vincent document analysis | none | common commercial → standard capability |
| Multi-jurisdiction / comparative | US-centric | US-centric (state depth) | US federal+state | 100+ countries claim, comparative research | US + world-law locators | variant |
| Dockets layer | (not emphasized) | (not emphasized) | deep differentiator | Docket Alarm | RECAP is sibling-pole (CourtListener) | variant layer |
| Analytics (judge/court/firm) | yes | module | yes | yes (Docket Alarm) | none | variant layer |
| News layer | (separate offerings) | Legal News Hub | 40+ channels | (news in library) | none | variant layer |
| AI assistant | CoCounsel / Deep Research | Protégé | purpose-built AI | Vincent | none | era-common → variant layer |
| Access model | subscription tiers | subscription + store | flat all-inclusive | subscription + trial | free / donation-supported | variant |

Key comparative insights:

1. **Multi-family breadth is universal.** Every sampled product — including the free pole — carries at least three of the four families (decisions, legislation, regulations/rules, secondary/analytical) as first-class, independently navigable content. No sampled product is single-family. This is the property that distinguishes the Type from the case-law core.
2. **Retrieval is universal** across citation, party, topic, and question modes, scoped by jurisdiction/court/content type.
3. **Authority validation spanning families** (citator covering statutes and regulations, not just cases) is universal in commercial products but absent in the free pole → commercial maturity layer, not defining. The free pole still shows the *concept* (citation resolver, annotated statutes linking cases to code sections) without the treatment-evaluation layer.
4. **The secondary/analytical layer is universal** but takes different shapes: attorney-maintained know-how (practice notes, standard documents, checklists) in commercial products; encyclopedia/annotation-level content in the free pole.
5. **Statute currency is a first-class behavior**: amendment alerts (vLex), trackers monitoring "statutory, case law and regulatory developments" (Lexis), currency claims (LII), KeyCite Alerts covering statutes (Westlaw). Law changes through legislation as well as through later courts.
6. **Market realization**: commercial products are the case-law core (a Case Law Research Platform) plus breadth — the two Types are nested in market realization, not identical.

## Canonical Abstraction

### L0 — Defining Invariant

```text
Curated corpus of authoritative legal materials
  spanning MULTIPLE first-class content families
  (judicial decisions; legislation; regulations & court rules;
   secondary/analytical sources — at least two families present)
+ Professional retrieval over the corpus
  (by citation, party, topic/keyword, or question;
   scoped by jurisdiction, court, and content type)
```

Two properties. Remove the multi-family breadth (keep decisions + citation network only) → Case Law Research Platform. Reduce to a single family (legislation only) → a statute archive / public data source, not a research platform. Remove retrieval → a static archive or publisher, not a platform.

Historical check (reasoning-based, no fetched primary evidence for the print era): the multi-family structure predates software — the print law library organized reporters (decisions), annotated codes (legislation), regulations, digests, encyclopedias, treatises, and citators as one research environment with finding aids linking across families; electronic services inherited the library's structure rather than inventing it. Early electronic services began case-law-centric and absorbed further families over time; the free pole today (LII) still realizes the multi-family structure without any commercial layer. L0 holds across eras and access models.

### L1 — Common Mature Structure

- **Authority validation spanning content families** (the citator): for decisions, statutes, regulations, administrative decisions — citing references, direct history, treatment signals (positive/negative/caution), increasingly AI-derived warnings. Commercial-common; absent in the free pole.
- **Editorial aids**: headnotes and topic classification on opinions; annotated legislation (statutes annotated with case summaries); most-cited passages; legal encyclopedias.
- **Multiple retrieval modes**: natural-language Q&A, Boolean/fielded advanced search, browse by jurisdiction/court/practice area, typeahead.
- **Research organization**: folders/workspaces (shareable), notes/highlights, search history.
- **Alerts and trackers**: citation-status alerts, search/topic alerts, statute-amendment alerts, practice-area development trackers.
- **Citation output**: formatted citations for briefs/memos; citation resolvers.
- **Document/brief analysis**: upload work product → report of supporting, contrary, or missed authority.
- **Practice guidance / know-how layer**: attorney-maintained practice notes, standard documents and clauses, checklists, resource kits; state/multi-jurisdiction comparison tools.

### L2 — Variant / Optional Structure

- Jurisdiction scope: single-country depth (US federal + state is the largest market) vs multi-country/comparative platforms vs world-law locators.
- Access model: tiered/segmented commercial subscription vs flat all-inclusive vs free public/donation-supported.
- AI assistant layer: conversational research, agentic deep research, drafting support (era-current; absent in the free pole).
- Analytics layer: judge/court/law-firm/litigation analytics.
- Dockets layer: court-filings search and tracking.
- News layer: legal news channels and current-awareness.
- Audience packaging: firms by size, corporate legal, government, law schools, bar associations, librarians, public.
- Practice-area verticalization: research services tuned to a single practice domain (e.g., tax research services) — reasoning-based, not directly sampled.

### L3 — Vendor-specific (research notes only)

- Westlaw/Thomson Reuters: KeyCite flag system, KeyCite Overruling Risk, WestSearch Plus, Quick Check, Claims Explorer, Litigation Document Analyzer, Deep Research, CoCounsel, Practical Law (650+ attorney-editors claim), edition ladder (Edge/Advantage), "100 years of editorial enhancements" claim.
- LexisNexis: Shepard's Signal vocabulary, Reason for Shepard's Signal, headnote-level signals, Analysis by Court grid, 29-step editorial process claim, Lexis Answers, Search Term Maps, Protégé, Practical Guidance (Resource Kits, State Law Comparison Tool, Automated Templates, Trackers, ~30 practice areas), Legal News Hub, module list.
- Bloomberg Law: 13 practice centers, In Focus trackers, Chart Builder, dockets depth, flat pricing posture, Dashboard Legal, 40+ news channels, Terminal integration.
- vLex: Precedent Map, Key Passages, Cited Authorities, Vincent, Docket Alarm, Fastcase Library, vLex Labs, coverage claims (1B+ documents / 100+ countries / 2,500+ sources / 350K+ daily updates), point-in-time legislation views.
- LII: Wex, U.S. Constitution Annotated (CRS), Supreme Court Bulletin, Introduction to Basic Legal Citation, Parallel Table of Authorities, RiO Citation Resolver, Table of Popular Names, Gender Justice Collection, state-regulations publishing (all 50 states), lawyer directory, donation posture.

## Rejected Findings

- "The citator is the defining invariant of the Legal Research Platform" — rejected: the free multi-family pole (LII) has citation lookup but no treatment-evaluation layer and is still recognizably in the Type; the citator is the commercial maturity layer inherited from the case-law core. (Consistent with the sibling pass, where treatment evaluation was also found non-defining.)
- "AI assistance defines the modern legal research platform" — rejected: the free pole has none; all commercial AI layers are recent add-ons; era-common capability.
- "Practical guidance/know-how is definitional" — rejected: absent at encyclopedia-only depth in the free pole; commercial-common.
- "Flat all-inclusive pricing is the access model" — Bloomberg-specific posture; others use tiered/segmented subscriptions; the free pole is donation-supported.
- "Dockets or analytics are part of the core" — rejected: variant layers, absent in several products.
- "Coverage percentages / document counts / editor counts" — vendor claims only; never promoted to the final document.
- "Fold candidate: Legal Research Platform is just a bigger Case Law Research Platform" — rejected (see Boundary Findings 1).

## Boundary Findings

1. **vs Case Law Research Platform — the sharpest seam; the joint-review flag is DISCHARGED from this side. Outcome: keep-both, with a content-scope seam.**
   - The two Types overlap heavily in market realization: every commercial product sampled at either node is both — a case-law core (opinion corpus + precedent graph + citator) delivered inside a multi-family research platform. This is the same embedded-core pattern documented elsewhere (e.g., a membership roll inside a church-management system).
   - But the defining cores are genuinely different, and each Type has realizations the other cannot cover:
     - Case Law Research Platform's L0 is content-scoped to judicial decisions + the precedent citation graph; its free pole (CourtListener) is decisions-only and still in-type. A multi-family platform with no opinion corpus (e.g., legislation + guidance) would not fit it.
     - Legal Research Platform's L0 is multi-family breadth + retrieval; its free pole (LII) is multi-family with no citator and still in-type. A decisions-only service with a citator fits the sibling, not this Type's discriminator.
   - Removal tests, both directions: strip a commercial platform to decisions + citation network → Case Law Research Platform; add statutes/regulations/secondary as first-class research content → Legal Research Platform. Strip LII to Supreme Court opinions only → it leaves this Type and joins the sibling's free pole.
   - Fold candidate (case-law as a facet of LRP) rejected because: (a) the free poles demonstrate two distinct minimal forms; (b) the print-era antecedents were distinct structures (reporters+citator shelf vs the whole law library); (c) the organizing centers differ (precedent graph vs authority-family breadth); (d) the sibling pass independently kept the leaf and requested exactly this joint review.
   - Residual watch-item: the market sells both labels for the same products; future consolidation of the two leaves into one Type with two named facets remains a defensible alternative. Recorded, not acted on.
2. **vs eDiscovery Platform**: eDiscovery manages parties' documents produced in a matter; this Type manages published law. Replace the authority corpus with party-produced files → eDiscovery.
3. **vs Legal Docket Management**: dockets track procedural events in live cases; this Type's objects are published authorities. A docket layer inside these platforms is an adjacent module.
4. **vs Legal Drafting Platform / Legal Document Automation** (the "draft vs law as object" seam recorded by the drafting pass): this Type's object is the law (authority) being researched; drafting's object is the work product being produced. Guidance content inside research platforms (standard documents, automated templates) is a research aid — the drafting engine with its own template/data/assembly structure is a different Type. Corroborating evidence: Thomson Reuters' own site taxonomy separates "Legal research & guidance" from "Drafting software, service & guidance".
5. **vs Regulatory Change Management**: RCM turns regulatory change into an organization's compliance obligations (requirement register, tracked remediation); this Type's trackers/alerts surface legal developments as research content. Seam: obligation register vs authority corpus.
6. **vs Academic Search Engine**: a scholarly search engine that indexes some opinions has corpus+search but no authority apparatus, no editorial legal layer, no professional validation workflow.
7. **vs Legal Matter Management**: the matter file (documents, tasks, dates for one piece of legal work) vs the law itself. Research output may be filed to a matter; the systems are different Types.
8. **vs Knowledge Base Application / Information Portal**: consumer-facing legal-information portals (plain-language advice sites) drift away from the Type — their content is not authoritative law and their users are not legal professionals. LII stays in-type because its core is primary-law publishing + retrieval, but its "Learn About" layer shows the drift direction.
9. **vs Investment Research Platform**: name similarity only; financial-market research vs legal authority research. Different corpora, users, and validation apparatus.

## Uncertainties

- Jus Mundi (global arbitration research) unreachable (403 ×2); CanLII unreachable (403 ×2, prior pass). The global-specialist and free-international poles are unverified; global claims rest on vLex's marketing pages.
- No vendor help center reachable at operational depth → no precise operational rules (search-syntax specifics, folder limits, alert mechanics, pricing) asserted anywhere.
- Bloomberg Law's citator was not directly observed on fetched pages (inherited uncertainty from the sibling pass); no citator claims for Bloomberg appear in the final document.
- Whether regional/national platforms outside the US (UK, Canada, Australia, civil-law jurisdictions) realize the same multi-family structure — assumed structurally similar (the print antecedent is global), unverified by fetch.
- Whether practice-area vertical research services (e.g., tax research platforms) are best read as LRP variants — reasoning-based, not directly sampled.
- LII's advanced-search depth (fielded/Boolean) not verified; only basic search + browse + citation resolver observed.
- The exact boundary behavior of unofficial/non-precedential content across families observed only as content-breadth claims (Lexis), not as workflow rules.

## Final Synthesis

A Legal Research Platform is the legal profession's research system over the whole body of law. Its defining core is a curated corpus of authoritative legal materials spanning multiple first-class content families — judicial decisions, legislation, regulations and court rules, secondary and analytical sources — together with professional retrieval over that corpus. Everything else layers onto that spine: authority validation spanning families (the citator, the commercial maturity layer), editorial aids (headnotes, annotated statutes, encyclopedias), multiple retrieval modes, research organization (folders, alerts, trackers), citation output, document analysis, and the practice-guidance layer. Commercial products realize the Type as a case-law core plus breadth — the case-law structure is inside them, not identical to them; the free pole realizes the multi-family structure minimally, without any commercial layer. The Type's sharpest boundary is with the Case Law Research Platform (resolved: keep-both, content-scope seam), and its other boundaries separate published law from party documents (eDiscovery), procedural records (dockets), work-product production (drafting), compliance obligations (regulatory change), and scholarly literature (academic search).
