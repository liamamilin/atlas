# Research Notes — Bibliometrics Platform

## Research Goal

Understand what a Bibliometrics Platform actually is as an Application Type: the data substrate it builds on, the entities it aggregates to, the quantitative indicators it computes, the analytical workflows users perform, the surfaces they use, and the boundaries against adjacent Types (academic search engine, citation database, CRIS, BI tools).

## Initial Boundary

Working hypothesis before research:

- Core use: quantitative analysis of scholarly publication and citation data for research evaluation, benchmarking, and strategy.
- Primary users: research office / institutional analysts, librarians, institutional leadership, funders, publishers; secondarily individual researchers.
- Nearest neighbors: Academic Search Engine (document discovery), citation databases (Scopus / Web of Science — data substrate, not analytics), Reference Manager (personal library), Research Information Management / CRIS (institution's own current record), BI / data visualization platforms (generic analytics).
- Likely boundary trap: the same vendors sell the citation database and the analytics platform built on it; the analytics layer is the Type, the database is the substrate.

## Research Questions

1. What data does a bibliometrics platform operate on, and is the corpus hosted by the vendor or user-supplied?
2. What entities does it aggregate publications into, and via what attribution machinery?
3. What indicators/metrics does it compute (raw and normalized)?
4. What is the typical analytical workflow from question to answer?
5. What does the entity-comparison (benchmarking) loop look like?
6. What interfaces exist (profiles, comparisons, maps, reports, API)?
7. What rules matter: data refresh, disambiguation, comparability across platforms, access/entitlement?
8. Where is the boundary to the academic search engine and to CRIS?

## Representative Products

Selected for market position + different philosophies + different customer tiers:

| Product | Vendor | Position | Philosophy / tier |
|---|---|---|---|
| SciVal | Elsevier | institutional research analytics/benchmarking | enterprise strategic analytics over the vendor's curated citation index (Scopus) |
| InCites | Clarivate | institutional benchmarking analysis | same philosophy over a different curated index (Web of Science) — direct competitor pole |
| Dimensions (Analytics suite) | Digital Science | linked research database + analytics | broad linked-data philosophy: publications linked to grants, patents, datasets, policy, trials; free web app tier + modules + API |
| Lens.org | Lens (Cambia-affiliated) | scholarly + patent search & analytics | merged scholarly-works + patents corpus; individual-friendly, metric-innovation posture (In4M) |
| VOSviewer | Leiden University (CWTS) | bibliometric mapping tool | free desktop/web tool; bring-your-own-data (import bibliographic exports), network map construction and visualization; individual analyst tier |

This spans: enterprise subscription platforms (SciVal, InCites), broad linked-data platform (Dimensions), scholarly+patent freemium platform (Lens), free byo-data mapping tool (VOSviewer).

## Sources

Research date: 2026-09-06.

Fetched (evidence Layer A unless noted):

1. Elsevier — SciVal product page: https://www.elsevier.com/products/scival — rich: positioning, data substrate, modules, metrics, FAQ (Scopus vs SciVal), users. ✅
2. Digital Science — Dimensions main site: https://www.dimensions.ai/ — rich: data counts, product modules, sectors, use cases. ✅
3. Lens — Support Center & Knowledge Base hub: https://support.lens.org/ — moderate: content categories (Scholarly Works, Patents, Biological, In4M Metric, Accounts & Work Area). ✅
4. Clarivate — https://incites.clarivate.com/ — returned page title "InCites - Clarivate" only (JS-rendered body not retrievable). https://help.incites.clarivate.com/ — transport error. ⚠️ Degraded: no operational evidence. Additional guessed URL (clarivate.com/products/...incites-benchmarking-analysis) returned 404. Per source-access rules, Clarivate source abandoned; InCites claims kept weak and general.
5. VOSviewer — https://www.vosviewer.com/ (reachable, but body was a security notice, no product content); https://www.vosviewer.com/about (404); https://app.vosviewer.com/ (title only, JS app). ⚠️ Degraded: no operational evidence. VOSviewer claims kept weak and general.
6. Elsevier support hub root (https://service.elsevier.com/app/home/supporthub/scival/) — directory only; no SciVal article content. (Incidental observation: Pure, Elsevier's CRIS, is listed as a separate support hub — supports the CRIS-vs-bibliometrics boundary.)

Not fetched / abandoned per network rules: support.dimensions.ai (timeout ×1 → abandoned after main-site success), harzing.com Publish or Perish (timeout → abandoned), lens.org main site (405).

## Product Observations

### SciVal (Elsevier) — evidence layer A

From the official product page (2026-09-06):

- Positioning: "connected research analytics" to help institutions "evaluate research performance, understand broader research impact and explore funding activity"; aimed at university leadership, liaison librarians, deans, administrators, research support offices.
- Explicit FAQ distinguishes **Scopus** (curated abstract & citation database) from **SciVal** ("an advanced research analytics tool built on Scopus data") — direct vendor confirmation of the database-substrate vs analytics-platform layering.
- Data substrate: built on Scopus; "covers over 75 million records dating back to 1996"; "updated weekly across most data sources".
- Aggregated entities: "24,800+ institutions, 21M+ researchers and 236+ nations"; analysis "across institutions, researchers and disciplines"; Scopus Author Profiles give "full publication history" per researcher.
- Adjacent data beyond publications: policy data (Overton), patent data (LexisNexis IP DirectData), mass media data, awarded grants data.
- Modules: Research Analytics (foundation), Impact Analytics (societal impact, policy, innovation, SDGs), Funding Analytics (funding landscape).
- Metric families listed: Collaboration, Published, Viewed, Cited, Policy impact, Patent impact, Media impact, Awarded grants, University rankings; plus "transparent ranking bibliometrics" (the bibliometrics used by THE, QS, U.S. News rankings); a "Research Metrics Guidebook" for responsible metric use.
- Use cases: benchmark against peers, rankings analysis, identify collaboration partners, monitor emerging research areas ("Topics"), research evaluation ("best metrics to assess performance by researcher, department, faculty and institution"), talent identification, SDG benchmarking.
- Outputs: "tailored reports… to inform decisions, track progress and update stakeholders".
- Vendor-specific names: Topics, Research Analytics/Impact Analytics/Funding Analytics, SDG benchmarking, ranking bibliometrics access.

### InCites (Clarivate) — evidence layer B, degraded

- Official site reachable but body not retrievable; only the product identity "InCites — Clarivate" was observed.
- Known market position (general knowledge, not fetch-verified): benchmarking/evaluation analytics over the Web of Science citation index for institutions, funders, publishers.
- Per source-access rules: no operational details (modules, metric names, workflows) are asserted from this product. Its role in this research is to confirm that the SciVal-style institutional-benchmarking philosophy exists in at least one more major product, at market-position level only.

### Dimensions (Digital Science) — evidence layer A

From the official main site (2026-09-06):

- Positioning: "largest collection of interconnected global research data… web platform and time-saving, workflow-based applications"; "linked data" is the explicit philosophy.
- Data scope (stated counts): publications 164M+, online citations 280M, grants 8.1M, patents 170M, datasets 42M, policy documents 2.5M, clinical trials 938k; ">70% of publications with full-text indexing".
- Products/modules: Dimensions Analytics ("find the information you need… get an overview of topics, organizations, people, or network profiles"), Landscape & Discovery (customized landscape-analysis dashboards, horizon scanning), Perspectives & Insights ("research strategy, impact assessment and collaboration analysis; benchmark against others"), Reviewer Finder, Research Security, GBQ (combine Dimensions data with own datasets on Google BigQuery), API, Industry Partnerships.
- Use cases: horizon scanning/landscape analysis, reviewer identification, research security risk screening, research evaluation ("research evaluation and analysis" per user quote), agreement negotiation data (publisher quote).
- Sectors: academic institutions, government, nonprofits, industry/pharma, publishers.
- Access: web app with login (app.dimensions.ai); commercial engagement via demo/quote; a "Scientometric access" program exists; free version widely known but not evidenced on the fetched page → keep weak.
- Entity model confirmed: topics, organizations, people, network profiles.

### Lens.org — evidence layer A (moderate, support-hub structure)

From the official support hub (2026-09-06):

- Content categories observed: **Patents**, **Scholarly Works**, **Biological** (biological sequences disclosed in patents), **In4M Metric** ("Influence on Industry and Innovation Metric"), **Accounts & Work Area** ("user settings, personal details, work area product").
- Confirms: a merged scholarly-works + patents corpus (plus biological sequence content), a first-party influence metric aimed at industry/innovation influence, and a user work-area concept (saved/user-owned analysis space) with account management.
- Operational detail of search/analytics flows not retrieved (category pages not fetched) → moderate evidence only.

### VOSviewer (Leiden University CWTS) — evidence layer B, degraded

- Official site reachable but body was a security notice; app subdomain returned title only.
- Known positioning (general knowledge, not fetch-verified): free tool for constructing and visualizing bibliometric maps (co-authorship, co-citation, bibliographic coupling, term co-occurrence) from user-supplied bibliographic export files (Web of Science, Scopus exports) or APIs; runs as desktop application and web app (VOSviewer Online).
- Used in this research as the "bring-your-own-data, free, individual" pole to test whether the Type definition depends on hosted subscription corpora. No operational claims asserted from it in the final document.

## Cross-product Comparison

| Dimension | SciVal | InCites | Dimensions | Lens.org | VOSviewer |
|---|---|---|---|---|---|
| Publication corpus | hosted (Scopus) | hosted (Web of Science, unverified) | hosted (own linked database) | hosted (scholarly works) | user-supplied (export files) |
| Citation-linked records | yes (A) | presumed (unverified) | yes (A: "online citations") | yes (A) | yes (co-citation/coupling inputs) |
| Entity aggregation | institutions, researchers, nations, disciplines, Topics (A) | institutions, researchers (unverified) | organizations, people, topics, network profiles (A) | works/patents, scholars implied (A-moderate) | authors, journals, terms, documents (unverified) |
| Citation-based indicators | yes, multiple families incl. rankings bibliometrics (A) | yes (unverified) | yes (A) | yes, first-party metric In4M (A) | network structure rather than impact metrics (unverified) |
| Benchmarking/peer comparison | yes (A) | core positioning (unverified) | yes: "benchmark against others" (A) | not evidenced | not core |
| Adjacent datasets (grants/patents/policy/media) | grants, patents, policy, media (A) | — | grants, patents, datasets, policy, trials (A) | patents, biological sequences (A) | no |
| Visualization/maps | dashboards/reports (A) | — | landscape dashboards, network profiles (A) | — | mapping is the core (unverified) |
| Export/reporting | tailored reports (A) | — | dashboards; GBQ/API for data egress (A) | work area (A-moderate) | export maps/images (unverified) |
| API / programmatic access | not evidenced | — | yes (A) | not evidenced (widely known, weak) | no |
| Customer tier | institutional enterprise | institutional enterprise | institutional + government + industry; login app | individual + institutional | individual, free |
| Access model | subscription (contact-to-buy, A) | subscription (unverified) | demo/quote + free tier (weak) | freemium (weak) | free (weak) |

Stable cross-product commonalities (Layer B, ≥2 products with A evidence): citation-linked publication corpus as substrate; aggregation of publications into named entities via attribution; citation-derived quantitative indicators; comparative/benchmarking use; extension beyond publications into adjacent datasets (2 of 3 hosted-corpus platforms, plus Lens patents); visual/dashboard surfaces; report/export outputs.

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

```text
Bibliometrics Platform
→ bibliographic corpus of scholarly outputs carrying citation links
   (vendor-hosted index OR user-supplied data)
→ attribution-based aggregation of publications into analyzable entities
   (researcher, institution, journal, country, subject field/topic)
→ quantitative indicators computed from the corpus (citation-derived measures)
→ comparative / evaluative analysis as the purpose
   (benchmark, rank, trend, map research activity and impact)
```

Four properties. Remove any one and the Type dissolves:

- remove the citation-linked corpus → nothing to measure; becomes generic statistics
- remove entity aggregation → it is a citation database / academic search engine (document-level surface)
- remove computed indicators → it is a database, not an analytics platform
- remove the comparative/evaluative purpose → raw data portal without analytical framing

L0 deliberately does NOT include: hosted subscription index, specific metric names (h-index, FWCI, JIF), field normalization, web delivery, dashboards, adjacent datasets (grants/patents/policy), API, disambiguation quality guarantees, weekly refresh. §24 historical check: 1990s–2000s desktop citation analyzers reading export files, national bibliometric datasets, regional evaluation systems, and Google-Scholar-derived free tools all satisfy this L0 — they operate on citation-linked bibliographic data, aggregate to entities, compute indicators, and serve evaluation. Conversely the definition excludes the citation databases themselves (Scopus/WoS as search surfaces) because those center document discovery, not entity-level measurement.

### L1 — Common Mature Structure

Present in most modern products (Layer B cross-product commonality):

- entity profile pages (researcher / institution / journal / topic) with attributed publication sets
- peer comparison / benchmarking sets (define a set of entities, compare indicators)
- time-trend analysis over years
- subject/topic classification and field breakdowns
- visual surfaces: dashboards, charts, network/landscape maps
- export and report generation for evaluation exercises, funding bids, rankings
- entity disambiguation machinery (author profiles, institution profiling) as a quality layer
- data-vintage management: indicators recomputed as the index updates (SciVal A: weekly)
- access/entitlement layer (accounts; institutional licensing)

### L2 — Variant / Optional Structure

- corpus scope: publications only ↔ publications + grants + patents + policy + media + datasets + trials
- corpus provenance: vendor-curated subscription index ↔ open/linked data ↔ user-imported exports
- normalization posture: raw counts ↔ field/collection-normalized impact indicators (concept common; exact definitions are vendor-specific)
- delivery: hosted web platform ↔ desktop tool ↔ API/warehouse (BigQuery-style)
- customer tier: enterprise institution ↔ government/funder ↔ industry/pharma ↔ individual researcher/free
- use-case extensions: societal impact analytics, funding-landscape analytics, reviewer finding, research-security screening, SDG benchmarking
- regional evaluation regimes (national assessment exercises, ranking bibliometrics) shape what indicators are exposed

### L3 — Vendor-specific Structure (research notes only)

- SciVal: Research/Impact/Funding Analytics module split; "Topics"; THE/QS/U.S. News ranking bibliometrics; SDG benchmarking; Overton/LexisNexis/Elsevier media data feeds; Scopus author profiles
- Dimensions: Landscape & Discovery; Perspectives & Insights; Reviewer Finder; Research Security; GBQ (BigQuery); Industry Partnerships; Altmetric-lineage online citations; scientometric access program
- Lens: In4M (Influence on Industry and Innovation) metric; biological sequence search over patents; work-area product
- InCites / VOSviewer: operational specifics not verified in this pass (access degraded)

## Vendor-specific / Rejected Findings

Rejected as definitional (with reasons):

- "A bibliometrics platform is a subscription product over a curated vendor index" — REJECTED: free byo-data tools (VOSviewer) and open/linked-data platforms (Dimensions' broader posture, Lens' freemium) exist; hosted-vs-supplied corpus must stay out of L0.
- "A bibliometrics platform must include grants/patents/policy data" — REJECTED: only some products extend beyond publications (L2 scope variant).
- "Bibliometrics = h-index / FWCI / JIF" — REJECTED at definitional level: specific metric names are vendor corpora decisions; the L0 concept is "citation-derived indicators" (Lens' In4M shows first-party metric invention is normal).
- "Must be a web platform" — REJECTED: desktop mapping tools are part of the same family (L2 delivery variant).
- "Must expose ranking bibliometrics" — SciVal-specific marketing differentiator (L3).
- "Institutional benchmarking is the definition" — too narrow: reviewer finding, research security, horizon scanning (Dimensions A) and individual mapping (VOSviewer) are real uses; benchmarking is the dominant enterprise pattern (L1/L2), not the invariant.

## Boundary Findings

- **vs Academic Search Engine** (processed sibling): search engine's deliverable = ranked, refinable document list for discovery/reading; bibliometrics platform's deliverable = indicators/mappings over aggregated entities for evaluation. A citation database has a document-record query surface; a bibliometrics platform has an entity-metric surface. *Remove entity-level aggregation and indicators, keep document discovery → Academic Search Engine.* SciVal's own FAQ draws exactly this line (Scopus = database, SciVal = analytics on top).
- **vs Citation database (Scopus / Web of Science as products)**: the database is the data substrate (a search surface over records); the platform is the analytics layer. Same vendors sell both; the Type boundary is the analytics layer, not the data.
- **vs Research Information Management / CRIS**: CRIS = the institution's self-managed current record of its own outputs/people (curated, authoritative for reporting); bibliometrics platform = external analytic view over an index (or exported into CRIS). *Remove the index-derived measurement and make the institution curate its own records → CRIS.* (Elsevier lists Pure as a separate product line; metrics commonly flow from the analytics platform into CRIS.)
- **vs Data Explorer / BI / Dashboard platforms**: generic form similarity (query → aggregate → chart) but the scholarly domain supplies the essence: citation linkage, author/institution disambiguation, field normalization, evaluation semantics. *Remove the scholarly citation domain → generic BI.*
- **vs Public Data Portal**: portals publish data for reuse; bibliometrics platforms compute evaluative indicators over linked corpora. Some platforms expose API/warehouse egress (Dimensions GBQ/API) — that is an L2 access variant, not a Type shift.
- **vs Reference Manager / Academic Paper Reader**: personal reading/writing library vs analytic corpus for evaluation. No overlap in core objects.

## Uncertainties

1. InCites operational structure unverified (JS-rendered help site inaccessible): modules, metric names, workflows unknown here. Market-position claim only. Degraded on purpose.
2. VOSviewer operational structure unverified this pass; used only as a boundary test (byo-data/free pole). Its map-type list is general knowledge, not fetch-verified.
3. Free-tier details for Dimensions and Lens not evidenced on fetched pages (widely known but not confirmed here) → access-model claims kept weak.
4. Whether "publication-count-only" tools (no citation data) should count as bibliometrics platforms: none sampled; L0 keeps citation linkage as invariant; risk noted.
5. Exact normalization methodology across products not verified; treated as conceptual (L2) only.
6. National/regional bibliometric evaluation systems were not sampled; their fit to L0 is inferred, not observed.

## Final Synthesis

A Bibliometrics Platform is the analytics layer over scholarly publication-and-citation data. Its defining structure: a citation-linked bibliographic corpus (hosted or imported), attribution-based aggregation of publications into analyzable entities, quantitative indicators computed over those entities, and a comparative/evaluative purpose. Mature products add entity profiles, benchmarking sets, trends, topic breakdowns, visualizations, reports, and disambiguation machinery; scope beyond publications (grants, patents, policy, media), delivery form (web/desktop/API/warehouse), corpus provenance (curated/open/imported), and customer tier (enterprise/individual/free) are variants. The Type sits between the citation database below it (document discovery = Academic Search Engine territory) and evaluation regimes above it (whose indicator demands shape the product but do not define it).
