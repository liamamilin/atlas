# Research Notes — Academic Search Engine

Research date: 2026-09-06

## Research Goal

Understand what an Academic Search Engine is as an Application Type: what the searchable unit is, how a scholarly corpus is built and bounded, what a query→results loop looks like, how citation navigation and full-text access routing work, how author/venue entity views fit in, and how this Type is bounded against Vertical Search Engine, Library Discovery Platform, Digital Library Platform, Reference Manager, Bibliometrics Platform, and AI Research Assistant.

## Initial Boundary

Initial hypothesis (pre-research): the Type centers on searching a corpus of scholarly documents (journal articles, conference papers, preprints, theses) and returning bibliographic records — not web pages, not answers, not hosted content. The closest confusions:

- **Vertical Search Engine (§02.02)** — an academic search engine is structurally a vertical search; the directory places it under §23 because the scholarly corpus carries its own record structure (bibliographic identity, citation graph, access rights) and its own user population. This overlap must be recorded, not hidden.
- **Library Discovery Platform (§23 sibling)** — both find scholarly literature; discovery is institution-bound (catalog + subscribed holdings), academic search is corpus-bound and institution-independent.
- **Digital Library Platform** — hosts full content; search is a capability of the host.
- **Reference Manager** — manages the user's personal library and citations; the search engine finds and exports.
- **Bibliometrics Platform** — analyzes research output for evaluation; the search engine retrieves documents.
- **AI Research Assistant / Answer Engine (§02.03)** — returns synthesized answers; the search engine returns document records. AI features inside search engines are augmentation layers that cite back to records.

## Research Questions

1. What is the searchable unit, and what metadata does a record carry?
2. How is the corpus built and bounded (web indexing, curated source lists, OA harvest, publisher partnerships)?
3. What does the query flow look like (single box, fielded forms, operators, filters, spellcheck, suggestions)?
4. How are results ranked, sorted, and refined?
5. How does citation navigation work (counts, cited-by, references, cited-reference search, citation contexts)?
6. How is full-text access routed (OA links, publisher links, institutional entitlement)?
7. How do author/venue entity views work (profiles, disambiguation, claiming)?
8. What is the save/export/alert loop (reference managers, saved searches, email alerts)?
9. Where does AI augmentation fit, and does it change the core model?
10. What are the business models and customer layers (free public, institutional subscription, freemium)?
11. Would older / regional / domain-specific products (PubMed, ADS, CiteSeerX, national databases) still fit the definition?

## Representative Products

Selection logic: market representation + documentation quality + different product philosophies + different customer layers.

| Product | Philosophy | Customer layer | Evidence level reached |
|---|---|---|---|
| **Semantic Scholar** (Ai2, nonprofit) | Free, AI/NLP-driven search over a web-indexed + partnership corpus; open API | Individual researchers/students; free public platform | A — homepage, FAQ (full), API overview fetched |
| **Scopus** (Elsevier) | Curated abstract & citation database with independent content-selection board; subscription | Institutions (universities, corporate R&D); subscription + free Preview | A — product page + LibGuide (home, searching, content) fetched |
| **Web of Science** (Clarivate) | Citation-index pioneer; curated multi-collection platform (incl. regional collections); subscription | Institutions; subscription | A− — Help Center structure + fielded-search article + cited-reference-search page fetched |
| **Dimensions** (Digital Science) | Linked research data (publications + grants + patents + trials + policy); freemium | Institutions, funders, government, industry; free personal tier | B− — homepage positioning only; docs site 404; no operational detail verified |
| **Google Scholar** | Free web-scale scholarly search | Individuals; free | C — degraded; all official surfaces (about page, support center, homepage) timed out across 3 attempts; abandoned per source-retry rule. Listed as representative; no operational claims made |

BASE (open-access aggregator) was planned as a sixth sample (open-harvest philosophy); both fetch attempts timed out and it was abandoned. It is referenced below only as unverified boundary context, never as evidence.

## Sources

- Semantic Scholar — homepage: https://www.semanticscholar.org/ (fetched 2026-09-06)
- Semantic Scholar — FAQ: https://www.semanticscholar.org/faq (fetched 2026-09-06; full text incl. Search, Library, Citations, Content, Alerts sections)
- Semantic Scholar — API overview: https://www.semanticscholar.org/product/api (fetched 2026-09-06)
- Scopus — product page: https://www.elsevier.com/products/scopus (fetched 2026-09-06)
- Scopus — LibGuide Home: https://elsevier.libguides.com/Scopus (fetched 2026-09-06; updated Sep 1, 2026)
- Scopus — LibGuide Searching Scopus: https://elsevier.libguides.com/Scopus/topical-search (fetched 2026-09-06)
- Scopus — LibGuide Content: https://elsevier.libguides.com/Scopus/content (fetched 2026-09-06)
- Web of Science — Help Center "Using Web of Science": https://webofscience.zendesk.com/hc/en-us/categories/29975435578641-Using-Web-of-Science (fetched 2026-09-06)
- Web of Science — Advanced Search - Fielded Search: https://webofscience.zendesk.com/hc/en-us/articles/20129792747921-Advanced-Search-Fielded-Search (fetched 2026-09-06; updated Jul 20, 2026)
- Web of Science — Cited Reference Search - videos: https://webofscience.zendesk.com/hc/en-us/articles/23290426868625-Cited-Reference-Search-videos (fetched 2026-09-06)
- Dimensions — homepage: https://www.dimensions.ai/ (fetched 2026-09-06)
- Google Scholar — https://scholar.google.com/intl/en-US/scholar/about.html, https://support.google.com/scholar/, https://scholar.google.com/ (all timed out 2026-09-06; abandoned)

## Product Observations

### Semantic Scholar — key observations (Evidence: A, official docs)

- **Self-identification**: "Semantic Scholar is a free, AI-powered research tool for scientific literature"; FAQ states "Semantic Scholar is an academic search engine and we are unable to provide the proper permissions on behalf of the authors and publishers whose content is discoverable on our site." Also: "As an academic search engine and discovery tool, Semantic Scholar is not engaged in any editorial decisions in the publishing process." (Direct vendor use of the Type name.)
- **Corpus**: homepage search box advertises "237,814,958 papers from all fields of science" (live counter); API page cites 214M papers / 2.49B citations / 79M authors (different snapshot). FAQ: content sourced "via web indexing and from partnerships with scientific journals, indexes, and content providers" (PubMed, arXiv, Springer Nature named). Corpus focus: "published academic articles and preprints"; book coverage "very limited", patents not included; primarily English.
- **Search mechanics**: single search box; FAQ — no Boolean operators or wildcards supported, quoted text supported, not case-sensitive, limited query expansion (author names only); search filters exist (video tutorials referenced); ranking via "a relevance function … that takes into account different aspects of the query and the paper details"; sort options: relevance, citation count, most influential papers, recency; venue pages reachable by clicking journal/conference names, with filters.
- **Record enrichment (AI layer)**: TLDR (AI-generated one-sentence summary; "limited to the computer science and biomedical domains"); Field of Study via ML classification from title/abstract (up to 3 fields, English only); citation intent classification (Background / Method / Result; "limited to papers for which we have access to the full text"); Highly Influential Citations (ML model over full text); Citation Velocity / Acceleration; topic pages (CS only, LLM-generated definitions); "Ask This Paper" (LLM QA with supporting statements from the paper; explicit caution that generated text "will not be free of errors").
- **Citation navigation**: citation counts on records; "over two billion citations"; cited-by browsing via the citation graph.
- **Access routing**: paper page shows "View PDF / View Paper / View via Publisher" below the abstract, or "No Paper Link Available"; non-OA papers route to publisher (possibly paywall/purchase); institutional access via GetFTR and LibKey partnerships with OpenAthens/eduGAIN/InCommon sign-in ("Access PDF via Institution" / "Access PDF via LibKey" buttons).
- **Personal layer (account)**: Library (save papers, folders, bulk export citations, AI Research Feeds built from a folder, personalized insights on search results); alerts (author / paper / topic / research-feed; daily or weekly email); Research Dashboard (recommended papers + alert digest + author-page citations); thumbprint icon marks personalized insights; account optional for search/read.
- **Author entity**: author pages auto-created via disambiguation model (S2AND); claim/moderate workflow (add/remove papers, edit name/affiliation/ORCID); Semantic Scholar ID used by conference systems for reviewer assignment.
- **Export/cite**: Cite button offers BibTeX, MLA, APA, Chicago; EndNote .enw download; Zotero Connector / Mendeley Web Importer integration (paper page + bulk save on results page).
- **Programmatic access**: S2AG REST API (papers, authors, citations, venues, SPECTER2 embeddings), Recommendations API, Datasets (monthly downloads); public endpoints rate-limited, API key for higher limits.
- **Corrections**: remove-paper requests; author-page correction tools; "removing papers from your author page does not remove them from the Semantic Scholar site."

### Scopus — key observations (Evidence: A, official docs)

- **Self-identification**: "Scopus: A comprehensive abstract and citation database"; LibGuide: "Scopus is an abstract and citation database. Abstracts are brief synopses of articles. A citation gives credit to a source … Most Scopus citations link to the full-text version of the publication hosted on various publishers' platforms."
- **Corpus curation**: content curated by the Content Selection and Advisory Board (CSAB), "an international group of scientists and researchers with journal editor experience"; board "constantly review[s] all new titles suggested to Scopus, as well as existing titles"; product page: "source-neutral", 100M+ records, 25.2M+ open-access documents, journals + books + conference proceedings + preprints; "updated daily".
- **Search mechanics (LibGuide)**: search by Documents, Authors, or Organization; document search defaults to Article title + Abstract + Keywords; drop-down to change search field; "+Add search field" rows combined with Boolean AND/OR/NOT; date range (publication date or "added to Scopus" date); advanced field codes; search tips (double quotes = loose phrase, braces = exact phrase, asterisk wildcard); Search History with save and combine-queries.
- **Results page**: default sort by date, "Sort by" dropdown; refine panel filters: search-within, author name, Open Access type, year, subject area, publication stage, keyword, affiliation, funding sponsor; registered users can save searches and set email alerts on a query.
- **Citation navigation**: "Cited reference search — Scopus provides the ability to search the list of cited references in articles, books, etc."; "secondary documents" = non-indexed references retrieved from the citations of covered documents.
- **OA filters**: All open access / Gold / Hybrid Gold / Bronze / Green.
- **Export**: to Mendeley, RefWorks, SciVal, RIS (EndNote), CSV, BibTeX, Plain Text; "Analyze Search Results" button.
- **Entity views**: Author Profiles (19.5M+ searchable; "research output, impact and collaborators"; auto-populated; Author Profile Wizard for corrections); Affiliation profiles.
- **Metrics**: CiteScore (journal-level), PlumX tags; product page: "Journal, article, author and institutional metrics".
- **AI layer**: "Scopus with AI" — natural-language search, responses "grounded in trusted, clearly cited content and data"; Scopus AI LibGuide exists.
- **Access model**: institutional subscription; "Scopus Preview" free tier (title list access); APIs via Elsevier developer portal; Scopus Academy training.

### Web of Science — key observations (Evidence: A−, official help center)

- **Platform structure**: Help Center sections: My Account; Content and Analysis (Citation Reporting, Open Access, Journal Title Abbreviations, Find All Records for an Author, Collection Development Tools, Usage Counts); Web of Science Search (Alerting, Smart Search, Search Rules, Search Operators, All Databases Search, Advanced Search - Fielded Search, Advanced Search Query Builder, Cited Reference Search, Search Results, Search History, Web of Science Research Assistant); Researcher Profiles (ORCID Search & Link Wizard, sync, add/remove publications); Admin Portal (Organization Settings, COUNTER Reports); APIs and XML; Web of Science Collections.
- **Multi-collection corpus**: Core Collection plus named collections — Arabic Citation Index, Biological Abstracts, BIOSIS Citation Index/Previews, CABI, Chinese Science Citation Database, Current Contents Connect, Data Citation Index, Derwent Innovations Index, FSTA, Grants Index, Inspec, KCI (Korean Journal Database), MEDLINE, Policy Citation Index, Preprint Citation Index, ProQuest Dissertations & Theses Citation Index, SciELO Citation Index, Zoological Record. (Regional/national literature is a first-class structure: Arabic, Chinese, Korean, Latin American collections.)
- **Fielded search (article)**: "Search for records from product indexes"; select field + term, Add Row for more criteria, Boolean AND/OR/NOT between rows; "Your settings are applied to all product databases in your subscription package; administrators may set one to three search fields to display as the default search fields for their institution" (institutional admin configuration of the search surface); searches land in Search History.
- **AI layer**: "AI Enabled Search" — topic and keyword suggestions, quick-add keywords, simplified Boolean (OR / INCLUDE / EXCLUDE); "Web of Science Research Assistant" exists as a separate help section; "Did You Mean" spellcheck with alternative-query suggestion; implicit AND between adjacent terms.
- **Cited reference search**: first-class search mode (dedicated article + training videos: "What is a Cited Reference Search", "How to do a Cited Reference Search"); related-records finding (training video "Find articles using related records"); controlled search terms (training video).
- **Researcher profiles**: ORCID connection wizard; profile add/remove publications.
- **Institutional admin**: Admin Portal with organization settings, COUNTER usage reports, single-product reports — the subscription customer manages the platform.

### Dimensions — key observations (Evidence: B−, positioning only)

- Self-description: "Intelligent discovery. Faster insight."; "the world's largest collection of linked research data, accessible via our web platform"; "over 70% of publications with full-text indexing"; linked objects: 164M publications, 8.1M grants, 170M patents, 938k clinical trials, 2.5M policy documents, 42M datasets.
- Product suite: Dimensions Analytics ("Find the information you need in millions of publications, patents, datasets, grants, and more"), Landscape & Discovery, Perspectives & Insights, Reviewer Finder, Research Security, GBQ (BigQuery), API, Industry Partnerships.
- Audience: academic institutions, government, nonprofits, industry/pharma, publishers — heavier institutional/analytics framing than the other samples.
- **Boundary tension**: Dimensions' homepage framing is research analysis and linked-data insight as much as literature search; the search/discovery app exists (app.dimensions.ai login) but operational search behavior could not be verified (docs.dimensions.ai returned 404). Treated as a straddling sample: satisfies the search core per positioning, but leans toward Bibliometrics/Research Information territory.

### Google Scholar — observations (Evidence: C, degraded; fetch failures)

- All three official surfaces (about page, support center, homepage) timed out on 2026-09-06 across separate attempts; abandoned per the source-retry rule.
- Google Scholar is retained as a representative product because it is the most widely used free scholarly search surface and the sample would be unrepresentative without a free web-scale engine. However, **no operational details are asserted from memory**: no claims about its ranking, filters, profiles, alerts, or library features appear in the evidence-based sections of this research or the final document. Its role in the sample is coverage/philosophy representation only.

## Cross-product Comparison

| Dimension | Semantic Scholar | Scopus | Web of Science | Dimensions | Google Scholar |
|---|---|---|---|---|---|
| Searchable unit | paper record (articles + preprints; books limited, no patents) | document record (articles, books, conference papers, preprints, data papers) | record from product indexes (multi-collection) | publication record within linked research objects | scholarly documents (unverified) |
| Corpus construction | web indexing + publisher/index partnerships | curated source list, independent board (CSAB), updated daily | curated collections incl. regional/national indexes | linked data aggregation (positioning) | web-scale scholarly indexing (unverified) |
| Query surface | single box; quotes; no boolean/wildcards; filters | documents/authors/organizations; fielded rows + boolean; field codes; phrases/wildcards | fielded rows + boolean; query builder; smart search; spellcheck; AI keyword suggestions | search app (unverified) | single box (unverified) |
| Ranking/sort | relevance function; sort by relevance/citations/influential/recency | default date sort; sort dropdown | search rules; history | unverified | unverified |
| Refinement filters | search filters (video-documented) | year, author, OA type, subject area, publication stage, keyword, affiliation, funding sponsor | refine panels (help section implied) | unverified | unverified |
| Citation navigation | counts, cited-by, influential citations, citation intent | cited reference search; secondary documents | cited reference search mode; related records | citations between linked objects | unverified |
| Author/venue entities | author pages (auto + claim), venue pages | author profiles (19.5M+), affiliation profiles | researcher profiles + ORCID wizard | people/org/network profiles (positioning) | unverified |
| Access routing | View PDF/Paper/Publisher; GetFTR + LibKey institutional | links to publisher-hosted full text; OA filters | full-text links (help structure) | unverified | unverified |
| Save/export/alerts | library + folders; BibTeX/APA/MLA/Chicago/EndNote; 4 alert types | save searches; email alerts; export to Mendeley/RefWorks/RIS/BibTeX/CSV | alerting section; search history | unverified | unverified |
| AI augmentation | TLDR, field-of-study, citation intent, topic pages, Ask This Paper, feeds | Scopus AI (NL search, cited answers) | AI keyword suggestions, Research Assistant | AI technology layer (positioning) | unverified |
| Business model | free public + open API | institutional subscription + free Preview | institutional subscription | freemium (free personal tier per positioning) | free (unverified) |
| Programmatic access | S2AG API + datasets | Elsevier APIs | APIs and XML section | Dimensions API + GBQ | unverified |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

The smallest structure without which the product stops being an academic search engine:

1. **Scholarly document records** — the searchable unit is a record representing a scholarly document (journal article, conference paper, preprint, thesis, book chapter), carrying bibliographic identity: title, authors, year, venue/source, and related metadata.
2. **Corpus-bounded scholarly query** — queries run against a corpus restricted to scholarly documents, not the open web at large; the engine returns corpus matches ranked by relevance to the query.
3. **Result as scannable record list** — results are presented as a list of records the user can scan, refine, and act on (open the record, follow to the document or its access point), not as generated answers and not as a personal-library structure.

Historical check: field databases and early engines (PubMed/MEDLINE-era services, 1990s subject databases, CiteSeerX-era citation indexers, national/regional databases) all satisfy these three properties without AI features, citation counts, web-scale indexing, or access entitlements. The L0 holds across eras.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required for the definition:

- structured refinement: filter panels (year, author, venue/source, subject area, document type, OA status) and fielded/advanced search forms with Boolean operators, phrases, wildcards
- citation navigation: citation counts, cited-by lists, reference lists, cited-reference search as a distinct mode
- author and venue entity views: author profiles with disambiguation and claiming; affiliation pages; venue pages
- full-text access routing: OA links, publisher links, institutional entitlement (resolver-style services), PDF links — routing, not hosting
- abstracts displayed on records
- save/export loop: saved records, citation export (BibTeX/RIS/EndNote formats), reference-manager integration
- alerts: saved queries with email notification of new matches
- search history and query combination
- related-work / recommendation surfaces
- programmatic access (APIs, datasets) in the major products

### L2 — Variant / Optional Structure

- **Corpus curation posture**: open web-scale indexing vs curated source list with independent quality board vs publisher-partnership indexing vs open-access harvesting (unverified context: BASE/CORE-style aggregators)
- **Coverage scope**: multidisciplinary vs domain-specific (biomedical, education, astronomy, psychology) vs regional/national literature (Arabic, Chinese, Korean, SciELO collections inside a global platform)
- **Business model**: free public vs institutional subscription vs freemium
- **AI augmentation depth**: ML ranking and enrichment (summaries, field classification, citation intent, QA, topic pages, keyword suggestions) — a modern layer, corpus-dependent, with explicit accuracy caveats from vendors
- **Analytics depth**: embedded metrics (journal metrics, h-index, citation velocity) vs standalone analysis products fed by the same data
- **Object scope**: publications only vs linked grants/patents/datasets/policy documents
- **Access surface**: web app, browser extension, mobile web, API

### L3 — Vendor-specific Structure (research notes only)

- Semantic Scholar: TLDR, citation intent taxonomy (Background/Method/Result), Highly Influential Citations, Citation Velocity/Acceleration, SPECTER2 embeddings, Research Feeds rating loop (More/Less Like This), thumbprint personalization, S2AND disambiguation, Semantic Reader, "Ask This Paper" on gpt-based QA, Semantic Scholar ID for reviewer assignment
- Scopus: CSAB, CiteScore, PlumX, secondary documents, "added to Scopus" date filter, Author Profile Wizard, Scopus Preview, SciVal export target, Scopus Academy
- Web of Science: Core Collection as anchor product, cited-reference search as separate mode, Researcher Profiles + ORCID wizard, Admin Portal with COUNTER reports, institution-set default search fields, Derwent/Grants/Policy collections, Research Assistant
- Dimensions: grants-patents-trials-policy linkage, Reviewer Finder, Research Security, GBQ, Industry Partnerships
- Google Scholar: unverified at research date — no vendor-specific claims recorded

## Vendor-specific Findings

See L3. None of these are promoted to the canonical model. The most tempting over-generalizations and why they were rejected:

- **"Citation counts are the defining feature"** — rejected: citation navigation is near-universal in the sampled majors but absent in real scholarly search products without citation graphs (OA aggregators; early PubMed). It is L1.
- **"Fielded Boolean search is the defining feature"** — rejected: Semantic Scholar explicitly does not support Boolean operators in its main box; the canonical concept is structured refinement, implemented variously (filters vs field codes vs neither).
- **"Institutional entitlement is the defining feature"** — rejected: free public products route to OA/publisher links without entitlements; entitlement is an access-routing variant.
- **"AI summaries are the defining feature"** — rejected: AI layers are corpus-dependent (S2 TLDR limited to CS/biomed; topic pages CS-only) and vendor-caveated; older products satisfy the Type without any AI.

## Boundary Findings

1. **vs Vertical Search Engine (§02.02)** — an academic search engine is structurally a vertical search engine over the scholarly vertical. The directory separates them because the scholarly corpus carries a record structure the generic vertical concept does not require (bibliographic identity, citation graph, access rights) and a distinct user population and tool ecosystem. Test: remove the scholarly-corpus restriction and the bibliographic record structure → a generic vertical search remains; remove the vertical generality (i.e., restrict to scholarly records) → it is this Type. **Recorded as a taxonomy overlap for joint review** — the leaf is defensible but sits in tension with §02.02.
2. **vs Library Discovery Platform (§23 sibling)** — both surface scholarly literature. Discovery is institution-bound: its organizing container is the library's catalog + subscribed holdings, and its success condition is "get this item from my library". Academic search is corpus-bound and institution-independent; institutional entitlement appears only as an access aid. Test: remove the institution's holdings/catalog → the academic search engine still stands; remove the global corpus → it collapses into a library catalog/discovery.
3. **vs Digital Library Platform** — the platform hosts full content (its primary job); search is a capability of the host. The search engine indexes/points; hosting is incidental (some products hold OA copies). Gradient: repository aggregators that hold harvested copies blur the line; the primary presented job (find vs hold) is the test.
4. **vs Reference Manager** — the manager owns the user's personal library and the citing workflow; the search engine owns corpus discovery. The export loop (BibTeX/RIS, browser connectors) is the designed hand-off. Lightweight in-product libraries (S2 Library) are saving conveniences, not reference management (no cite-while-you-write).
5. **vs Bibliometrics Platform** — the search engine's primary job is retrieving documents; bibliometrics evaluates entities (authors, journals, institutions). Gradient: Scopus/Dimensions embed analytics; SciVal/InCites-style products are the pure analysis side. Test: remove document retrieval → bibliometrics remains; remove entity evaluation → the search engine remains.
6. **vs AI Research Assistant / Answer Engine (§02.03)** — the search engine returns document records; the assistant returns synthesized answers. The sampled AI layers (Scopus AI, S2 Ask This Paper, WoS Research Assistant) are augmentation over the record corpus and cite back to records. Products whose primary surface becomes answer-first are drifting toward the AI Research Assistant Type.
7. **vs General Web Search Engine** — corpus restriction plus scholarly record structure is the wall. A general web engine that offers a scholarly-restricted surface with bibliographic records implements this Type (which is exactly the Google Scholar pattern).

## Uncertainties

- **Google Scholar operational behavior unverified** (all official surfaces unreachable at research date). The final document describes the free web-scale philosophy generically and makes no Scholar-specific operational claims.
- **Dimensions operational search behavior unverified** (docs 404). Dimensions is treated as a straddling sample; its inclusion leans on positioning evidence only.
- **BASE/CORE-style OA aggregators unverified** — used only as boundary context for the "citation navigation is L1" decision; no claims made about their internals.
- **Whether citation navigation should be L0**: the sampled majors all have it, but the historical check (citation-graph-free field databases) and the existence of citation-less scholarly search products argue L1. Decision: L1, with the reasoning recorded.
- **WoS cited-reference search mechanics**: the mode's existence is confirmed (dedicated article + training videos), but the fetched page was video-only; mechanics not detailed from memory.
- **Ranking internals**: vendors describe ranking only at the level of "relevance function" (S2) or default sort (Scopus); no cross-product claim about ranking signals is made beyond what vendors state.

## Final Synthesis

An Academic Search Engine is a search application whose corpus is restricted to scholarly documents and whose results are bibliographic records of those documents. The defining core is small: scholarly document records with bibliographic identity, a corpus-bounded query, and a scannable, refinable record list. Everything else the market associates with the category — fielded Boolean search, citation counts and cited-by navigation, author profiles, institutional access routing, alerts, exports, AI summaries — is common mature structure layered on that core, and varies by product philosophy: open web-scale free engines, curated subscription databases with independent content boards, AI-driven open platforms with public APIs, and linked-data research platforms. The Type's edges are real but gradient-shaped: toward Vertical Search (structural overlap, flagged), toward Library Discovery (institution-bound vs corpus-bound), toward Bibliometrics (retrieval vs evaluation), and toward AI Research Assistants (records vs answers).
