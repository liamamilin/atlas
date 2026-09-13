# Research Notes — Case Law Research Platform

Research date: 2026-09-07
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal; not referenced in the final document)

## Research Goal

Understand what a Case Law Research Platform actually is as an Application Type: what exists inside it, who uses it, how the research work flows, which states and rules matter, and where its boundary lies against the neighboring Legal Research Platform and other legal-adjacent Types.

## Initial Boundary

Working hypothesis before research:

- Core use: legal professionals find, read, validate ("is this still good law?"), and organize judicial decisions (case law / opinions).
- Likely users: attorneys, paralegals, law librarians, judges/clerks, law students.
- Nearest neighbors: Legal Research Platform (broader — statutes, regulations, secondary sources), eDiscovery (party documents, not published law), Legal Docket Management (procedural case tracking), Court Case Management System (court operations), Academic Search Engine (scholarly corpus that includes some case law).
- Open questions: Is the citator definitional or merely common? How does the free/public pole fit? Is this leaf a distinct Type or a variant of Legal Research Platform?

## Research Questions

1. What is the central content object, and what metadata does it carry?
2. How is retrieval done (citation, party, topic, Boolean, natural language, browse)?
3. What is the citator, and how do treatment signals work across products?
4. What editorial layers exist on top of raw opinions (headnotes, topic classification, key passages)?
5. How do users organize ongoing research (folders, notes, history, alerts)?
6. What interfaces exist (search, results, opinion viewer, citator report)?
7. Which rules matter (coverage, publication status, editorial control, access)?
8. How do variants differ (case-law-only vs bundled; commercial vs free; single-jurisdiction vs global; AI depth)?
9. Where exactly is the boundary vs Legal Research Platform, and vs general document search?

## Representative Products

Selected for market representation + documentation quality + different philosophies + different customer tiers:

| Product | Vendor | Pole | Evidence tier reached |
|---|---|---|---|
| Westlaw (Edge / Advantage) | Thomson Reuters | dominant US commercial, citator-first (KeyCite) | Tier 2 product pages (westlaw overview + KeyCite page) |
| Lexis+ | LexisNexis | dominant US commercial, citator-first (Shepard's), suite modules | Tier 2 product pages (Lexis+ overview + Shepard's page) |
| Bloomberg Law | Bloomberg Industry Group | all-in-one flat-price platform, dockets/news depth | Tier 2 product pages (home + legal research) |
| vLex (part of Clio) | vLex | global/multi-jurisdiction + AI (Vincent) | Tier 1/2 product pages (home + vLex Library) |
| CourtListener | Free Law Project (non-profit) | free/public case-law-centric pole | Tier 1 (homepage + case-law data coverage wiki) |

CanLII was intended as a second free/international sample but returned 403 on both attempts (see Source-access Limitation).

## Sources

All fetched 2026-09-07:

- Westlaw overview — https://legal.thomsonreuters.com/en/products/westlaw
- KeyCite — https://legal.thomsonreuters.com/en/products/westlaw/keycite
- Lexis+ overview — https://www.lexisnexis.com/en-us/products/lexis-plus.page
- Shepard's Citations Service — https://www.lexisnexis.com/en-us/products/shepards.page
- Lexis+ Legal Research subpage — https://www.lexisnexis.com/en-us/products/lexis-plus/legal-research.page (thin)
- Lexis state case law page — https://www.lexisnexis.com/en-us/case-law-research/default.page (thin, marketing)
- Bloomberg Law home — https://pro.bloomberglaw.com/
- Bloomberg Law Legal Research — https://pro.bloomberglaw.com/products/legal-research-and-software/legal-research/
- vLex home — https://vlex.com/
- vLex Library — https://vlex.com/vlex-library
- CourtListener home — https://www.courtlistener.com/
- CourtListener case-law coverage (FLP wiki) — https://wiki.free.law/c/courtlistener/help/data-coverage/case-law
- CanLII — https://www.canlii.org/en/info/about.html and /en/index.php — **403 both, abandoned after 2 attempts**

Source-access limitation: no vendor's in-product help center / user guide was reachable at operational depth (Lexis+ legal-research subpage was a hero page; Westlaw help lives behind sign-in). All evidence below is from official product/marketing pages and the CourtListener public wiki. Consequently: no precise numeric limits, no exact state-machine names, no pricing figures are asserted in the final document; vendor figures (e.g., "1B+ documents", "9M decisions") are recorded here as vendor claims only.

## Product Observations

### Westlaw (Thomson Reuters) — evidence layer A (direct, official pages)

- Self-description: "legal research service" / "legal research software"; tiered editions (Westlaw Edge, Edge with AI-Assisted Research, Westlaw Advantage) "built on the same trusted foundation… versions… to meet your needs — and your budget".
- KeyCite (dedicated product page): "verify whether a case, statute, regulation, or administrative decision is still good law… and find citing references to support your legal argument."
  - Citing References: "show how other authorities have interpreted a document, as well as the depth of the discussion and the topics discussed".
  - History tab: "the history of a document—including a visual representation".
  - KeyCite Alerts: "monitor the status of your case, statute, administrative decision, regulation, patent or trademark".
  - Flag system: red flag, yellow flag, blue-striped flag, plus an "Overruling Risk alert" icon; "the most negative treatment is displayed next to the flag".
  - KeyCite Overruling Risk: "warns you when a point of law has been implicitly undermined based on its reliance on an overruled or otherwise invalid prior decision. Artificial intelligence identifies bad law that has no direct citations pointing to its invalidity."
- Quick Check: "Upload legal documents to create a report indicating authority that may have been missed or is contrary to your opponent's position."
- Litigation analytics: "data-driven insights on judges, courts, attorneys, law firms, damages, and case types".
- Search: WestSearch Plus; AI-Assisted Research ("fast, accurate, and trusted answers"); Deep Research (agentic); Claims Explorer; Litigation Document Analyzer.
- Editorial claim: "100 years of editorial enhancements"; related products Practical Law (650+ attorney editors) and CoCounsel (AI assistant) are separate offerings.
- Audience segmentation: law firms under/over 10 attorneys, businesses, government.

### Lexis+ (LexisNexis) — evidence layer A

- Self-description: "advanced legal research platform"; modules: Legal Research, Practical Guidance, Litigation Analytics, Document Analysis, Legal News Hub; AI layer "Lexis+ with Protégé" (generative/agentic, conversational search, drafting).
- Shepard's Citations Service (dedicated page): "Is it good law? *Shepardize* and be sure."
  - "count on the most comprehensive editorial analysis of case law, statutes, regulations, administrative decisions and more".
  - Treatment nuance: "Courts rarely overrule a case on every point of law… Only *Shepard's* can show you these 'followed' points of law because only *Shepard's* shows you both negative treatments plus true positive treatment from subsequent citing cases" — split-of-authority visibility.
  - Shepard's Signal indicators attached to headnotes; clicking a signal opens the Shepard's report filtered to that headnote and treatment.
  - "Reason for *Shepard's* Signal" — shows the citing reference with the strongest influence on the signal, without leaving the case.
  - Case cards in search results: circular graphic of treatment counts; "most cited headnote" surfaced.
  - Graphical "Analysis by Court": grid view of citing trends across courts and time periods.
  - Editorial claim: attorney-editors, "strict 29-step editorial process" (linked PDF).
  - Cultural claim: "Judges will ask you, 'Did you *Shepardize*?'"
- Lexis Answers: natural-language question → answer within results; Search Term Maps: visualize where terms appear in documents.
- Document Analysis: "upload or drag and drop your document to validate your legal research" — key citations, arguments, risks, missing authorities.
- Folders: "Folders can be created to quickly and easily find up-to-date statutes and you can share them with your team" (customer testimonial); FAQ confirms folders and alerts carry over from the prior platform.
- Content breadth claim: "more case law, more unreported case law, more verdicts and settlements, more briefs, pleadings, motions" per jurisdiction.
- Audience: small/medium/large firms, corporate legal, law schools, government; online store for 1–3 attorney firms.

### Bloomberg Law — evidence layer A

- Self-description: "all-in-one legal platform"; components: Legal Research, Workflow Tools, Practical Guidance, News and Analysis; separate Dashboard Legal (project management/collaboration).
- Research page: "brings together primary and secondary sources, trusted legal news, expert analysis, and purpose-built AI"; "AI-assisted search and powerful filtering options"; "complete, unlimited access to all content and AI-powered workflow tools" (flat-price posture: "one platform, one price", "without paying upcharges").
- Practice organization: 13 practice centers (Antitrust … Trademarks & Copyrights); "In Focus" emerging-topic resources, trackers, and chart builders.
- Dockets: AI-powered docket search and analysis; customer quotes emphasize granular docket scanning as the differentiator ("Dockets are probably the reason we got the product firmwide").
- News: 40+ news channels; Bloomberg Terminal integration.
- Litigation/business intelligence: track cases, judges, law firms; competitor and litigation-trend analytics.
- Audience: law firms, in-house counsel, government, law schools.

### vLex (part of Clio) — evidence layer A

- Self-description: "AI engineered for lawyers" (Vincent) backed by "the world's most comprehensive legal database"; products: Vincent AI, vLex Library, Docket Alarm, vLex Labs, Fastcase Library.
- vLex Library: "over one billion legal documents from 100+ countries"; "350K+ daily updates"; "2,500+ data sources" (vendor claims).
  - **Precedent Map**: "transforms complex citation analysis into immediate visual clarity" — "color-coded visual indicators" showing whether precedents have been "positively cited, criticized, or overruled"; filter by treatment type, legal concepts, jurisdiction.
  - **Key Passages**: "the exact paragraphs that other courts cite most frequently from judicial opinions"; "citation frequency analysis"; "chronological citation tracking".
  - **Cited Authorities**: "the complete citation landscape of any case at a glance, distinguishing between case law and legislation"; amendment alerts when relied-on statutes change; point-in-time legislation views ("legislation as it existed at any point in time").
  - Search modes: Smart Searchbar (typeahead suggestions), Browsing the Law (filter by jurisdictions, courts, practice areas), Advanced Search (Boolean operators + precision filters), Comparative Research (multi-jurisdiction simultaneous).
- Vincent AI: natural-language Q&A "with proper citations", 50-state surveys, contract analysis, judge/opposing-counsel profiling from court records.
- Docket Alarm: "850+ million court records with real-time alerts, litigation analytics, and powerful APIs".
- Fastcase Library: "U.S. primary law database providing coverage of cases, statutes, regulations, court rules, and constitutions with powerful visualization tools".
- Audience: large/small firms, legal departments, bar associations, law schools, law librarians, government; integrations with Word, Outlook, iManage; SOC2/ISO 27001 claims.

### CourtListener (Free Law Project) — evidence layer A

- Self-description: "free legal research website containing millions of legal opinions from federal and state courts"; "Search millions of legal decisions by case name, topic, or citation"; "472 Jurisdictions".
- Users: "lawyers, journalists, academics, and the public".
- Surfaces: Case Law search (+ advanced search), citation lookup (/c/), RECAP Archive (PACER dockets/filings), oral argument audio, judges database, financial disclosures.
- Alerts: search alerts for case law and filings; docket alerts.
- Data posture (wiki): 9M+ decisions from 2,000+ courts; claims >99.9% of US precedential case law; continuous scraper-based updates; direct publishing partnerships with courts incl. neutral citations at issuance; machine+human data corrections; API and bulk data for all.
- No editorial treatment-evaluation layer (headnotes/signals) is offered — citation lookup and citing references exist, but "good law" evaluation is not part of the free pole's observed offering.

## Cross-product Comparison

| Structure | Westlaw | Lexis+ | Bloomberg Law | vLex | CourtListener | Reading |
|---|---|---|---|---|---|---|
| Corpus of judicial decisions w/ court/jurisdiction/date attribution | yes | yes | yes | yes (global) | yes (US) | universal → defining |
| Retrieval: citation / party / topic / question | yes | yes | yes | yes | yes (case name, topic, citation) | universal → defining |
| Citation relationships between decisions (citing/cited) | KeyCite citing references | Shepard's citing decisions | (citator not directly observed) | Precedent Map / Cited Authorities | citation lookup + citing refs | universal in sample → defining |
| Treatment evaluation (good law / negative treatment signals) | KeyCite flags + Overruling Risk | Shepard's signals + Reason | not directly observed | Precedent Map colors | **absent** | common commercial; NOT in free pole → standard capability, not defining |
| Editorial enhancements (headnotes, key passages, topic links) | "editorial enhancements", topics in citing refs | headnotes + most-cited headnote | practice centers | Key Passages | none | common commercial → standard capability |
| Multiple retrieval modes (NL Q&A, Boolean, browse) | WestSearch Plus, AI-Assisted | Lexis Answers, Search Term Maps | AI-assisted search + filters | 4 named modes | basic + advanced search | common → standard capability |
| Research organization (folders, alerts) | KeyCite Alerts; folders (icon evidence only) | folders (shareable) + alerts | trackers | alerts (statute amendment, dockets) | search + docket alerts | common → standard capability |
| Document/brief analysis (upload → missed/contrary authority) | Quick Check | Document Analysis | (AI tools) | Vincent document analysis | none | common commercial → standard capability |
| Statutes/regulations/secondary sources bundled | yes | yes | yes | yes | no (opinions + dockets + oral args) | common commercial → scope variant |
| Dockets layer | (not emphasized on fetched pages) | (not emphasized) | deep differentiator | Docket Alarm product | RECAP Archive | variant layer |
| Analytics (judge/court/firm) | yes | module | yes | yes (Docket Alarm) | judges DB (reference, not analytics) | variant layer |
| News/practical guidance modules | Practical Law (separate) | modules | modules | (secondary sources) | none | variant layer |
| AI assistant | CoCounsel / Deep Research | Protégé | purpose-built AI | Vincent | none | era-common → variant layer |
| Access model | subscription tiers | subscription + store | flat all-inclusive | subscription + trial | free/non-profit | variant |
| Jurisdiction scope | US-centric | US-centric (state depth) | US federal+state | 100+ countries | US (472 jurisdictions) | variant |

Key comparative insights:

1. The **decision corpus + retrieval + citation network** triad is present in every sampled product including the free pole — it survives the historical check (citation analysis of precedent predates software; early full-text services coexisted with separate print citators, and the modern products integrated what was always one practice).
2. **Treatment evaluation** (the "good law" signal layer) is universal in commercial products but absent in the free pole → it is the standard commercial maturity layer, not the defining invariant.
3. Every commercial product has drifted into a **multi-content platform** (statutes, regulations, secondary sources, guidance, news, dockets, analytics). None of the commercial samples is case-law-only. The case-law-specific structure is nonetheless what they are organized around (citator-first marketing on both dominant vendors).
4. The free pole (CourtListener) demonstrates the minimal Type: corpus + search + citation lookup + alerts, no editorial layer, no paywall.

## Canonical Abstraction

### L0 — Defining Invariant

```text
Corpus of judicial decisions
  (published opinions attributed to courts / jurisdictions / dates)
+ Retrieval over the corpus
  (by citation, party, topic, or question)
+ Citation relationships between decisions
  (the precedent graph: which decisions cite which, navigable)
```

Three properties. Remove the corpus → not about case law. Remove retrieval → a static archive, not a research platform. Remove the citation network → generic full-text document search over opinions; the precedent-based research practice (tracing and validating authority) disappears, and with it the Type's reason to exist.

Historical check: the citation-relationship concept predates software (print citators); early full-text services delivered corpus+search while citation work was done in a companion product — the *concept* was always intrinsic to the practice, only its integration is modern. The free pole today still exposes citation lookup. L0 holds.

### L1 — Common Mature Structure

- Citator with treatment evaluation: user-visible status signals (positive / negative / caution), citing references with discussion depth, case history, overruling-risk detection (editorial and/or AI-derived).
- Editorial enhancements on opinions: headnotes, issue/topic classification, most-cited passages, topic-taxonomy navigation.
- Multiple retrieval modes: natural-language Q&A, Boolean/fielded advanced search, browse by jurisdiction/court/practice area, typeahead.
- Research organization: folders/workspaces, notes/highlights, search history, shareable collections.
- Alerts: citation-status alerts (a relied-on case changes status), search/topic alerts, statute-amendment alerts.
- Citation output: formatted citation copy/export for briefs and memos.
- Document/brief analysis: upload work product → report of supporting, contrary, or missed authority.

### L2 — Variant / Optional Structure

- Content scope beyond decisions: statutes, regulations, court rules, constitutions, secondary sources (treatises, journals), practical guidance, legal news, dockets/filings, verdicts/settlements, briefs/pleadings. (Full bundle = drift toward Legal Research Platform.)
- Jurisdiction scope: single-country vs multi-country/comparative research; global coverage claims.
- Access model: commercial subscription (tiered/segmented/flat) vs free/public/non-profit.
- AI assistant layer: conversational research, agentic deep research, drafting support.
- Analytics layer: judge/court/law-firm/litigation analytics.
- Audience packaging: firms by size, corporate legal, government, law schools, bar associations, librarians.

### L3 — Vendor-specific (research notes only)

- Westlaw: KeyCite flag color system, KeyCite Overruling Risk, WestSearch Plus, Quick Check, Claims Explorer, Litigation Document Analyzer, Deep Research, CoCounsel, Practical Law, edition ladder (Edge/Advantage).
- LexisNexis: Shepard's Signal vocabulary, Reason for Shepard's Signal, headnote-level signals, Analysis by Court grid, 29-step editorial process claim, Lexis Answers, Search Term Maps, Protégé, Experience Dock, module list.
- Bloomberg Law: 13 practice centers, In Focus trackers, Chart Builder, dockets depth, flat pricing posture, Dashboard Legal, 40+ news channels, Terminal integration.
- vLex: Precedent Map, Key Passages, Cited Authorities, Vincent, Vincent Studio, Docket Alarm, Fastcase Library, vLex Labs, coverage figures (1B+/100+ countries/2,500+ sources).
- CourtListener: RECAP, oral-argument audio, judges DB, financial disclosures, API/bulk data, coverage figures (9M+ decisions/2,000+ courts/472 jurisdictions/99.9% claim).

## Rejected Findings

- "AI assistance defines the modern case law research platform" — rejected: the free pole has none and the commercial AI layers are all recent add-ons; era-common capability, not definitional.
- "Flat all-inclusive pricing is the access model" — Bloomberg-specific posture; others use tiered/segmented subscriptions.
- "Dockets are part of the defining core" — rejected: strong at Bloomberg/vLex/CourtListener, not central to the fetched Westlaw/Lexis research surfaces; a variant layer.
- "Treatment signal vocabularies are standardized across products" — rejected: each vendor's signal/flag vocabulary is proprietary; only the concept (positive/negative/caution treatment) is shared.
- "Westlaw's Key Number topic taxonomy is a Type-level structure" — not directly observed in fetched pages; excluded from all layers rather than guessed.
- "Coverage percentages / document counts" — vendor claims only; never promoted to the final document.

## Boundary Findings

- **vs Legal Research Platform** (the sharpest seam): the sampled commercial products all bundle statutes, regulations, and secondary sources — i.e., the market realization of this leaf is mostly *as the case-law core of broader legal research platforms*. The case-law-specific structure (precedent graph + citator + opinion-centric workflow) is nonetheless real, distinct, and the organizing center of these products. Judgment: the leaf is defensible as a Type (its defining core is content-scoped to judicial decisions and their authority relationships), but it is closely coupled to Legal Research Platform; a joint review of the two leaves is recommended. Test: remove the citation/authority layer and the statute/regulation/secondary bundle → what remains is a legal document archive, not either Type; add first-class non-decision research workflows → Legal Research Platform.
- **vs eDiscovery**: eDiscovery manages parties' documents in a matter; this Type manages *published law*. Replace the opinion corpus with party-produced files → eDiscovery.
- **vs Legal Docket Management**: dockets track procedural events in live cases; this Type's object is the published opinion. A docket layer inside these platforms is an adjacent module, not the core.
- **vs Court Case Management System**: court-side operations vs published law; different operator (court vs practitioner).
- **vs Academic Search Engine**: a general scholarly search engine that indexes some opinions has corpus+search but no citator, no editorial layer, no professional validation workflow → stays outside the Type.
- **vs Reference Manager**: organizes citations to sources; does not host or validate the law itself.
- **vs plain archive/publisher**: corpus without retrieval+citation tooling is a data source, not a research platform.

## Uncertainties

- Bloomberg Law's citator was not directly observed on fetched pages (its research page emphasizes search/dockets/analytics); citator presence is inferred from category membership, not evidenced. No citator claims for Bloomberg appear in the final document.
- Westlaw's editorial topic taxonomy (Key Number) was not directly observed; excluded.
- CanLII (free international pole) unreachable (403 ×2); the free-pole analysis rests on CourtListener alone. Regional free services (CanLII, national court sites) are assumed structurally similar but unverified.
- Exact editorial workflows (how treatments are assigned, update cadence) are vendor-claimed (e.g., "29-step process") and not independently verifiable.
- Pricing/access details observed only at surface level (tier existence, flat-price posture, free pole); no figures asserted.
- The exact boundary behavior of "unreported"/non-precedential decisions (how products treat them) was observed only as a content-breadth claim (Lexis), not as a workflow rule.

## Final Synthesis

A Case Law Research Platform is a professional research application whose world is built from judicial decisions. Its defining core is a corpus of published opinions attributed to courts and jurisdictions, retrieval over that corpus, and the citation network that links decisions to each other. Everything else layers onto that spine: the citator's treatment evaluation (the commercial maturity layer that answers "is this still good law?"), editorial aids (headnotes, key passages, topic classification), multiple retrieval modes, research organization (folders, alerts), document analysis, and — variably — statutes, regulations, secondary sources, dockets, analytics, news, and AI assistants. Commercial products realize the Type as the case-law core of broader legal research platforms; the free pole realizes it minimally. The Type's sharpest boundary is with Legal Research Platform (scope of first-class content) and with eDiscovery/docket management (published law vs party documents vs procedural records).
