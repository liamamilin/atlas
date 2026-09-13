# Case Law Research Platform

## Overview

A **Case Law Research Platform** is a professional research application built around judicial decisions. Its subject matter is the published opinion of a court; its job is to help a legal professional find decisions, read them with the aid of editorial and computational layers, validate whether an authority can still safely be relied on, trace how later courts have treated it, and organize that work into briefs-ready research.

The defining core is deliberately small:

```text
Corpus of judicial decisions
  (published opinions attributed to courts, jurisdictions, and dates)
+ Retrieval over that corpus
  (by citation, party name, topic, or question)
+ Citation relationships between decisions
  (the precedent graph: which decisions cite which, navigable in both directions)
```

Everything else commonly associated with these products — treatment signals ("good law" indicators), headnotes and key passages, folders and alerts, brief analysis, statutes and secondary sources, dockets, analytics, AI assistants — is a capability layered on top of that spine, not part of what makes the product a case law research platform. A free public database of opinions with search and citation lookup still belongs to this Type; a bundle of statutes and treatises with no opinion corpus does not.

The most important boundary is with the **Legal Research Platform**: in today's market, commercial products at this node are almost always delivered as the case-law core of a broader research platform that also carries statutes, regulations, and secondary sources. This document describes the case-law structure that such products are organized around.

## Users & Context

Primary users are legal professionals whose work product depends on precedent:

- **Attorneys** (litigators above all, but also transactional and advisory lawyers) — find supporting authority, verify that the cases they cite are still good law, and distinguish adverse authority before it is used against them.
- **Paralegals and legal assistants** — run citation checks, pull cases, and assemble research folders under attorney direction.
- **Law librarians and knowledge-management staff** — often the most expert users; they design research strategies, maintain alerts, and evaluate coverage across platforms.
- **Judges, clerks, and court staff** — verify authority in drafts and opinions.
- **Law students** — learn and perform the same research loop in academic settings.

Secondary users include compliance and in-house teams monitoring legal developments, journalists and academics (especially via the free public pole), and litigation-analytics consumers.

The typical context is deadline-driven document production: a brief, a memo, an opinion, a client advice letter. Research is rarely "done" — an authority that is good today can be overruled next month, which is why monitoring (alerts) is a structural part of the workflow rather than an afterthought.

## Core Model

### The defining core

Three structures. If any one is removed, the product stops being a case law research platform:

- **Judicial decision (opinion).** The central object: a court's written decision, attributed to a court, jurisdiction, date, docket, parties, and (usually) judges, with a publication status (precedential / reported vs unpublished / non-precedential). Everything else in the system hangs off decisions.
- **Retrieval over the decision corpus.** The corpus is organized by jurisdiction, court, and time, and the platform can find decisions by citation, party name, topic or issue, or a natural-language question. Without retrieval the corpus is an archive, not a research platform.
- **Citation relationships between decisions.** The precedent graph: which decisions cite which, captured as navigable links. Case law is authority-based — a decision's meaning in practice is inseparable from how later courts have received it. This graph is what turns "document search over opinions" into case law research. It is also the oldest layer of the practice: citation analysis of precedent long predates software.

### What mature products add

These capabilities are standard in commercial products and expected by professional users, but they are layers on the core rather than the definition:

- **Citator with treatment evaluation.** The commercial maturity layer. For any decision, the platform shows the citing references (with the depth of discussion and the topics discussed), the decision's direct history, and user-visible status signals — positive treatment, negative treatment, caution — typically as colored flags or icons, increasingly supplemented by AI-derived warnings when a point of law has been undermined without any direct citation saying so. The underlying judgment is editorial (specialized attorney-editors) and/or algorithmic; the signal is advisory, not the law itself.
- **Editorial enhancements on opinions.** Headnotes summarizing legal points, issue or topic classification that links a passage to related authority, and passage-level analysis showing which paragraphs of an opinion other courts actually cite.
- **Multiple retrieval modes.** Natural-language question answering alongside Boolean/fielded advanced search, browse-by-jurisdiction/court/practice-area navigation, and typeahead suggestion.
- **Research organization.** Folders/workspaces for collected authority, notes and highlights, search history, and shareable collections for teams.
- **Alerts.** Notification when a relied-on decision's status changes, when new decisions match a saved query, or when a relied-on statute is amended.
- **Citation output.** Copying or exporting decisions in the citation formats legal writing requires.
- **Document/brief analysis.** Uploading a draft or an opponent's filing and receiving a report of authority it missed, relied on wrongly, or failed to address.

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:   Decision corpus        Implementations:  vendor-edited collections; scraped court output;
                                                    direct-publishing partnerships with courts

Concept:   Retrieval              Implementations:  citation/party lookup, Boolean and fielded search,
                                                    natural-language Q&A, browse by court/topic

Concept:   Citation network       Implementations:  editorial citators with signal vocabularies;
                                                    computed citing-reference graphs; visual maps
```

A reader who has only seen one commercial platform should still be able to recognize a free public opinion database as the same Type from the core alone.

## How It Works

The defining loop is a research cycle, not a transaction:

```text
1. FIND      enter a citation, party name, question, or issue
             → results list with status indicators per decision
2. READ      open the opinion
             → headnotes / key passages orient the reader inside the text
3. VALIDATE  check the citator
             → citing references, direct history, treatment signals
             → is this still good law, on the point I need?
4. EXPAND    follow citing references and topic links outward
             → more on-point authority, adverse authority, deeper history
5. ORGANIZE  save to folders, annotate, copy citations
6. MONITOR   set alerts on key authorities and queries
             → the loop re-opens when the law changes
```

Two properties make this loop distinctive:

- **Validation is not optional.** In professional practice, citing an overruled case is a serious error. The citator step is culturally enforced — practitioners speak of "checking treatment" before filing — and the platforms treat it as the anchor feature, surfacing status indicators directly in search results rather than hiding them behind a separate tool.
- **The loop never terminates.** Because authority status changes over time, alerts keep the research alive after the brief is filed. A case relied on in a filed brief can be negatively treated later; citation alerts exist precisely for this.

A second, newer loop runs alongside it: **document analysis**. The user uploads a draft brief, a contract, or an opponent's filing; the platform extracts the authorities cited, reports authority that was missed or is contrary, and links each finding back into the same corpus and citator.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Search bar / home

The entry surface. Accepts citations, party names, natural-language questions, and terms; offers scope selection (jurisdiction, content type) and typeahead suggestions. Primary actions: run a search, look up a citation, open saved research.

### Results list

A ranked list of decisions with per-item status indicators (treatment flags), court/date metadata, and — in mature products — treatment summaries (counts of positive/negative citing references) visible without opening the document. Primary actions: open a decision, filter by court/jurisdiction/date/topic/treatment, save to folder.

### Opinion viewer

The document surface for a single decision: full text with headnotes or key-passage highlights, cited-authority links inline, and panels for the citator (history, citing references, treatment detail). Primary actions: jump to a cited authority, open the citator report, highlight/note, copy citation, save, alert.

### Citator report

The validation surface: the decision's direct history, its citing references grouped by treatment, and filters by court, date, or treatment type. In some products this is a visual map or grid rather than a list. Primary actions: inspect a citing reference, filter to negative treatment, trace history.

### Folders / research workspace

Collected authority organized per matter or project, with notes and sharing. Primary actions: add/remove items, annotate, share, export.

### Alerts management

Saved queries and watched authorities with notification configuration.

### Analytics / dockets / AI panels (where present)

Optional surfaces: judge and court statistics, docket search and tracking, and conversational AI assistants that answer questions with citations back into the same corpus.

## Important Rules / Behaviors

- **Authority status is time-varying.** A decision's usability is a state that changes as later courts act. The platform's treatment signals and alerts exist to keep that state visible; research artifacts (folders, briefs) can silently go stale.
- **Treatment signals are judgments, not law.** Signals are produced by editorial staff and/or algorithms. They direct attention (investigate this citing reference) rather than conclusively determine outcomes; the citing references themselves remain the ground truth.
- **Partial treatment is normal.** A court rarely overrules a case on every point. Mature citators evaluate at the level of the point of law, so one decision can be negatively treated on one headnote and followed on another. This is why headnote-level signals exist.
- **Publication status matters.** Reported/precedential and unpublished/non-precedential decisions carry different weight, and coverage of the latter varies by product and jurisdiction.
- **Coverage is scoped.** Every product covers a defined set of courts, jurisdictions, and date ranges; depth varies substantially between commercial and free products, and between jurisdictions. Cross-jurisdiction work may cross platform boundaries.
- **Access is gated in commercial products.** Subscription and seat models control who can search, open, and export; the free public pole is open but narrower in tooling.
- **Citation conventions are load-bearing.** Decisions carry official, parallel, and neutral citations; platforms must resolve all of them, and citation output follows jurisdiction-specific conventions.

## Variants

- **Case-law-centric vs full research platform.** The minimal Type (opinions + search + citation lookup) exists mainly in free/public products. Commercial products bundle statutes, regulations, secondary sources, practical guidance, news, dockets, and analytics — the case-law core delivered inside a Legal Research Platform.
- **Jurisdiction scope.** Single-country depth (US federal + state is the largest market) vs multi-country/comparative platforms covering dozens of jurisdictions and languages.
- **Access model.** Tiered or segmented commercial subscriptions; flat all-inclusive pricing in some products; free non-profit services funded by donations and court partnerships.
- **AI depth.** From none (free pole) to conversational research assistants and agentic deep research built on the same corpus and citator.
- **Adjacent layers.** Dockets and court-filings search, litigation analytics (judges, courts, firms), legal news, and practical guidance appear as modules in some products and are absent in others.
- **Audience packaging.** Large firms, small firms and solos, corporate legal departments, government, law schools, bar associations — same core, different packaging and pricing.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Legal Research Platform | broader sibling | adds statutes, regulations, and secondary sources as first-class research content with their own workflows; commercial products at this node are usually delivered inside one |
| eDiscovery Platform | adjacent | manages parties' documents produced in a matter, not published law |
| Legal Docket Management | adjacent | tracks procedural events in live cases; the docket layer here is a module, not the core |
| Court Case Management System | different operator | court-side operations on its own cases, not practitioner research over published law |
| Academic Search Engine | adjacent | may index opinions, but has no citator, editorial layer, or professional validation workflow |
| Reference Manager | adjacent | organizes citations to sources; does not host or validate the law |
| Legal Document Automation / Drafting | downstream | consumes research output; does not maintain the authority corpus |

The sharpest seam is with the Legal Research Platform. Test: if statutes, regulations, and secondary sources are first-class research subjects alongside decisions, the product is a Legal Research Platform; if the opinion corpus, the precedent graph, and authority validation are the organizing center, the case-law structure described here is what the product is built on.

## Representative Products

- **Westlaw** (Thomson Reuters) — dominant commercial platform; KeyCite citator with treatment flags and AI-derived overruling risk; tiered editions.
- **Lexis+** (LexisNexis) — dominant commercial platform; Shepard's citator with headnote-level signals; modular suite (research, practical guidance, analytics, document analysis, news).
- **Bloomberg Law** (Bloomberg Industry Group) — all-in-one flat-price platform; strong dockets, news, and practice-center organization.
- **vLex** (part of Clio) — global multi-jurisdiction platform (100+ countries claimed); Precedent Map citation visualization; Vincent AI.
- **CourtListener** (Free Law Project) — free non-profit pole: millions of US opinions, search, citation lookup, alerts, API; demonstrates the minimal Type without the commercial editorial layer.

## Sources

Research date: **2026-09-07**

- Westlaw overview — https://legal.thomsonreuters.com/en/products/westlaw
- KeyCite — https://legal.thomsonreuters.com/en/products/westlaw/keycite
- Lexis+ overview — https://www.lexisnexis.com/en-us/products/lexis-plus.page
- Shepard's Citations Service — https://www.lexisnexis.com/en-us/products/shepards.page
- Bloomberg Law — https://pro.bloomberglaw.com/ and https://pro.bloomberglaw.com/products/legal-research-and-software/legal-research/
- vLex — https://vlex.com/ and https://vlex.com/vlex-library
- CourtListener — https://www.courtlistener.com/ and https://wiki.free.law/c/courtlistener/help/data-coverage/case-law

> Sourcing limitation: vendor in-product help centers and user guides were not reachable at operational depth from the research environment; evidence comes from official product pages and the CourtListener public wiki. Precise operational details (numeric coverage figures, exact signal vocabularies, pricing, editorial process specifics) are therefore not asserted in this document; vendor-stated figures are recorded only in the Research Notes. CanLII (a free international service) was unreachable (403) and is not sampled.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
