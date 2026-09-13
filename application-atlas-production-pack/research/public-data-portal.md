# Research Notes — Public Data Portal

Research date: 2026-09-08
Slug: public-data-portal
Leaf: Public Data Portal — DIRECTORY.md §02.12 Data Exploration (sibling leaf: Data Explorer, processed 2026-09-07)
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand, from real products, what a **Public Data Portal** is as an Application Type when the *government operator context is stripped away*: what its unit of record is, how discovery works, how data is actually delivered, what governance rides on the records, and where the boundary runs against the sibling §02.12 leaf (Data Explorer), the §24 government specialization (Government Open Data Portal), and the neighboring publication/search/data Types.

This pass also carries a **joint review obligation**: the government-open-data-portal pass (§24, 2026-09-07) flagged this leaf as a potential duplicate/alias and recommended joint review when it was processed (STATUS.md Boundary Issues line: "candidate outcomes: keep-both with operator-specialization seam, or merge under one leaf"). This pass must sample predominantly **non-government operators** to test whether a generic core exists and discharge that flag.

## Initial Boundary (hypothesis before research)

- Core use: an organization publishes collections of data as datasets that anyone can find and take away (download / API).
- Primary users: the operator's publishing staff on one side; the general public — researchers, journalists, developers, analysts, citizens — on the other.
- Nearest neighbors: Data Explorer (sibling §02.12 — query/render vs find/download), Government Open Data Portal (§24 — potential alias), Data Catalog (§13), Data Exchange Platform (§13), Vertical Search Engine (§02.02), Information Portal / Directory (§02.11), Government Transparency Portal (§24), Digital Collection Portal / Institutional Repository (§23), General Reference Database (§02.05).
- Unknowns going in: whether "government" is the only real operator class (alias question); whether publisher-side tooling is definitional for a generic portal (aggregators may only harvest); whether in-portal visualization, APIs, or open licensing belong in the core; whether the "public" qualifier means open licensing or merely open access.

## Research Questions

1. What is the unit of record, and what does a record carry?
2. How is data attached to records — hosted, linked, queryable?
3. What does the public discovery surface look like (search, browse, facets, listings)?
4. What access posture applies (free? account? license/terms granularity)?
5. What publisher-side machinery exists, and is it definitional or implementation?
6. How do portals express currency/freshness, provenance, and multi-publisher structure?
7. Which capabilities are era machinery vs structural (preview, charts, APIs, analytics, harvesting)?
8. Does the generic core survive when the operator is not a government?
9. Where exactly is the seam vs Data Explorer, Data Catalog, Data Exchange, search engines, and document-publication Types — with removal tests?

## Representative Products

Selected to span **operator classes** (open-source engine / international financial institution publisher / UN statistics aggregator), **philosophies** (catalog engine vs publisher-curated statistical service vs single-entry-point aggregation), and **audience tiers**. Government-operated portals are deliberately NOT the sample (they are the sibling pass's specialization); engine products (Socrata, ArcGIS Hub, Huwise) enter only as Layer-B continuity from the sibling pass.

| Product | Operator class | Philosophy | Evidence |
|---|---|---|---|
| CKAN (docs + product site) | open-source portal engine — used by "national and local governments, research institutions, and other organizations" | "CMS for data" — self-serve publication with wiki-like possible modes | A (user guide fetched in full) |
| World Bank Open Data (data.worldbank.org + Data Catalog + Microdata Library) | international financial institution publishing its own compiled statistics | publisher-curated statistical service with companion query tool (DataBank) | A (about + get-started pages) |
| UNdata (data.un.org) | UN Statistics Division (UN DESA) — aggregation of many UN/international databases | single-entry-point statistical data service ("Statistics as a Public Good", launched 2005) | A (home + about pages) |

## Sources

Tier 1 (official operational documentation), all fetched 2026-09-08:

- CKAN — User Guide: https://docs.ckan.org/en/latest/user-guide.html (fetched in full — richest single source)
- World Bank Open Data — About us: https://data.worldbank.org/about ; Get started: https://data.worldbank.org/about/get-started
- UNdata — Home: https://data.un.org/ ; About UNdata: https://data.un.org/Host.aspx?Content=About

Same-repo continuity (prior passes, Layer B for cross-product claims):

- research/government-open-data-portal.md — engine-side Layer-A evidence (CKAN, Socrata, ArcGIS Hub, Huwise) reused as cross-product continuity; its joint-review flag is discharged by this pass
- research/data-explorer.md + applications/data-explorer.md — sibling §02.12 seam held from the explorer side
- research/data-catalog.md — "open-data portal does contain a dataset catalog — adjacent surface, different primary job"
- research/data-exchange-platform.md — "remove the entitlement → open-data publication portal"
- research/general-reference-database.md, research/digital-collection-portal.md, research/institutional-repository.md, research/government-gis.md, research/government-transparency-portal.md — publication-Type seams held from their sides

Source-access limitations (all 2026-09-08):

- data.europa.eu — /en/how-to-use → 404, /en/about → 404 (2 attempts). **Abandoned per network rule.** The EU-federated-aggregator pole is therefore NOT directly verified; UNdata carries the aggregator pole instead. No EU-portal-specific claims made.
- Kaggle — /docs/datasets returned an empty JavaScript shell (title only). Abandoned. The community-published pole is NOT directly verified; CKAN's documented no-organization "wiki-like datahub" mode (Layer A) is the only direct evidence that non-institutional publishing fits the Type.
- HDX (data.humdata.org/about) — empty response. Abandoned. Humanitarian portals NOT directly characterized.
- World Bank DataBank and Data Catalog interiors not fetched (their public surfaces only, via the get-started page); no claims about their internals beyond what those pages state.
- UNdata publisher-side machinery (how datamarts are ingested/updated) not documented on reachable pages — publisher-side claims for UNdata not made.

## Product A — CKAN

Evidence layer: A (official user guide fetched in full).

### Key observations

- Self-description: "a tool for making open data websites. (Think of a content management system like WordPress — but for data, instead of pages and blog posts.) It helps you manage and publish collections of data. It is used by national and local governments, research institutions, and other organizations who collect a lot of data." Consumers named: "developers, journalists, researchers, NGOs, citizens, or even your own staff." — **direct evidence that the engine is operator-generic.**
- **Dataset = the publication unit.** "A dataset is a parcel of data — for example… the crime statistics for a region, the spending figures for a government department, or temperature readings from various weather stations." Search results are individual datasets. A dataset = metadata (title, publisher, date, formats, license) + any number of **resources** holding the data itself (CSV, Excel, XML, PDF, image, RDF). Resources may be **stored internally or linked** ("Link to a file" / "Link to an API"). Different resources may carry different years or different formats of the same data. Early versions called datasets "packages" (name persists in API).
- **Publishing side in the same system.** Login "is not needed to search for and find data, but is needed for all publishing functions." Dataset creation flow: title/description/tags/license (dropdown)/organization → add resources (upload or link) → additional info (visibility, author, author e-mail, maintainer, custom fields) → finish. Organizations own datasets; org roles Member/Editor/Admin; site-wide sysadmin. "It is possible, however, to set up CKAN to allow datasets not owned by any organization. Such datasets can be edited by any logged-in user, creating the possibility of a wiki-like datahub." — **direct evidence that organization structure is NOT definitional.**
- **Private → public lifecycle**: default new dataset is private (visible only to the owning organization, invisible in others' searches); "when it is ready for publication, it can be published at the press of a button. This may require a higher authorization level."
- **License emphasized**: "it is important to include license information so that people know how they can use the data."
- **Public discovery**: free-text search on every page; faceted filters (tags, formats) combinable; search within an organization; Solr-backed advanced fielded search; map-area search "possible with an extension."
- **Dataset/resource pages**: name/description/info + resource links; per-resource page with **preview** (grid for CSV/XLS, map and graph views where suitable, image/PDF/HTML previews) and download; **activity stream** (history of changes).
- **Deletion is hiding**: deleted datasets "are not completely deleted… hidden" and recoverable by authorized users.
- **Engagement**: Follow datasets/organizations/users → news feed of changes (login required).
- **Full API** ("machine interface") documented.
- Product site (Layer A, marketing layer): "open-source data management system (DMS) for powering data hubs and data portals… powers hundreds of data portals worldwide"; "CKAN for Enterprise" — internal data assets (drift pole).

## Product B — World Bank Open Data

Evidence layer: A (official about + get-started pages).

### Key observations

- **Operator and mission**: the Development Data Group "coordinates statistical and data work and maintains a number of macro, financial and sector databases"; data compiled "from the statistical systems of member countries" under professional standards. Open-data framing: "transparency and accountability are essential to the development process… share its knowledge freely and openly… free and open access to a comprehensive set of data about development."
- **Access posture**: "All of the data found here can be used free of charge with minimal restrictions" + Terms of Use page. (Terms recorded at site level; the Microdata Library records terms **per dataset** — "Many of these datasets are available as open data; check the terms of use associated with each dataset.")
- **Consumer loop** (Get started): search box with type-ahead over "indicator names, countries, and topics"; browse lists of countries/topics/indicators; data pages render charts; **Download** button on any data page ("Country pages provide all data for all years for a single country… indicator pages provide data for all countries for all years") for desktop tools like Excel.
- **Companion query tool**: "Data displayed on this site are a subset of those available in the World Bank's DataBank, which contains extensive collections of time series data. The DataBank has advanced functions for selecting and slicing the datasets, performing customized queries and data downloads, and creating charts and other visualizations." — **the explorer coexists as a separate named product.**
- **Embeddable widgets**: "Widgets are small snippets of code that let you embed a data chart or map on another website… when new data are available, widgets update automatically."
- **Web API**: "The Data API is a way for web sites and other tools to access data directly. This is the interface of choice for creating custom data visualizations, live combinations with other data sources (mashups), and more. data.worldbank.org is built using data through the Data API." Developer section in the help desk.
- **Data Catalog**: "A comprehensive listing of data and datasets published by the World Bank… The Catalog contains all the datasets in DataBank, plus many other useful datasets, including some sub-national and raw data from surveys. Datasets can be easily downloaded, or accessed through the DataBank query tool or custom tools specific to the dataset." — **the catalog is the find→download surface; per-dataset delivery varies (download, query tool, custom tools).**
- **Microdata Library**: "facilitates access to microdata collected through sample surveys of households, business establishments or other facilities… Many of these datasets are available as open data."
- **Audiences named**: policymakers, advocacy groups, journalists, academia, researchers.
- **Portal family structure**: data.worldbank.org (flagship indicator site) + DataBank (query tool) + Data Catalog (comprehensive listing) + Microdata Library (survey microdata) — one publisher operating several complementary surfaces.

## Product C — UNdata

Evidence layer: A (official home + about pages).

### Key observations

- **Self-description**: "UNdata is a web-based data service for the global user community. It brings international statistical databases within easy reach of users through a single-entry point. Users can search and download a variety of statistical resources compiled by the United Nations (UN) statistical system and other international agencies."
- **Unit structure**: "The numerous databases or tables collectively known as 'datamarts' contain over 60 million data points and cover a wide range of statistical themes including agriculture, crime, communication, development assistance, education, energy, environment, finance, gender, health, labour market, manufacturing, national accounts, population and migration, science and technology, tourism, transport and trade." Home page banner: "32 databases – 60 million records."
- **Aggregation posture**: content compiled from "more than 20 international statistical sources"; a Partners page; specialized external databases (UNComtrade, SDG indicators, MBS Online) surfaced as **links out** — the portal both hosts datamarts and indexes external ones.
- **Discovery surfaces**: search; **Advanced search**; **Explorer** over datamarts; popular statistical tables by theme with **per-table "Updated:" dates** and **PDF | CSV downloads**; country/area profiles (web adaptation of the World Statistics Pocketbook); **Update Calendar** page; Glossary.
- **API**: SDMX **Browse** and **Web Service** with documentation — machine access to the same data.
- **Provenance/curation**: every popular table names its statistical sources; glossary; site-usage guidance; feedback channel ("Please send us your feedback").
- **History (documented)**: "UNdata was launched as part of a project in 2005, called 'Statistics as a Public Good', whose objectives was to provide free access to global statistics…" — maintained by the Development Data Section, UN Statistics Division (UN DESA). **A 2005-era portal already exhibiting the full generic core: single-entry-point catalog, search/download, terms of use, API.**
- **Governance**: Conditions of Use page; UN DESA accountability; contact e-mail.

## Cross-product Comparison

| Dimension | CKAN (engine) | World Bank Open Data | UNdata |
|---|---|---|---|
| Unit of record | Dataset (metadata + resources; "package" legacy name) | Dataset (in Data Catalog); data pages per indicator/country | Datamart/database + tables; popular statistical tables; country profiles |
| Metadata carried | title, description, tags, license, org, author/maintainer, custom fields | description, source attributions, coverage, terms of use | theme organization, source compilation (20+ sources), update dates, glossary |
| Data delivery | upload/link file or API resource; download; previews | bulk download per country/indicator page; Web API; DataBank query tool; widgets | PDF/CSV per table; SDMX web service + browser |
| Discovery | faceted search (tags/formats), org-scoped search, advanced fielded search | type-ahead search; browse countries/topics/indicators | search, advanced search, Explorer over datamarts, theme/country listings |
| Currency signals | activity stream | data updates & errata page | per-table "Updated:" dates + Update Calendar |
| Terms/access | license dropdown on record; login not needed to search/find | free with minimal restrictions; site terms; per-dataset terms in Microdata | free access; Conditions of Use; "Statistics as a Public Good" |
| Publisher side in same system | Yes — org-scoped create/edit/publish (documented) | publisher machinery not documented on reachable pages (public surfaces only) | not documented on reachable pages (aggregated datamarts; update calendar implies feed management) |
| Multi-publisher structure | Organizations (departments/bodies) with own workflows | one publisher, multi-database family (Catalog/Microdata/DataBank) | 20+ international sources; partners; external-database links |
| In-place exploration | resource previews (grid/map/graph) | charts on data pages; DataBank visualizations; widgets | Explorer; (popular tables are table-first) |
| Engagement | follow + news feed; author/maintainer contact | "welcome suggestions"; feedback/help desk | feedback link; contact e-mail; site-usage page |

### Cross-product commonalities (candidate L1)

1. Dataset-level records with descriptive metadata as the discovery unit — all three (different unit vocabularies).
2. Search + browse over the whole corpus, usable without an account — all three; CKAN states it explicitly.
3. The portal leads the user to the **data itself** — files and/or APIs, hosted or linked — all three; per-dataset delivery mixes download/query/custom tools (World Bank explicit).
4. Usage terms/licenses recorded on or alongside the data — all three (granularity varies: per-record CKAN vs site-level + per-dataset World Bank vs site-level UNdata).
5. Publisher/source attribution and contactability — CKAN author/maintainer; UNdata source compilation + contact; World Bank Development Data Group contact.
6. Currency/freshness signals — all three, differently realized.
7. API delivery alongside files — all three.
8. Feedback/engagement channels — all three.
9. Companion exploration/visualization surfaces — CKAN previews; World Bank charts/DataBank; UNdata Explorer — present but not the portal's defining closure.

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal; jointly held)

1. **The maintained dataset record.** A persistent, individually addressable entry for one dataset — a named parcel of data — carrying descriptive metadata (what it contains, who publishes/sources it, what it covers, when it was updated, how it may be used). The portal maintains these records as its own catalog content — authored in place, ingested, or harvested — rather than merely crawling third-party pages. Remove → a bare file listing or a search engine's results page.
2. **Data distributions attached to the record.** The data itself, reachable through the record as downloadable files and/or queryable API endpoints — hosted by the portal or linked to stable locations, commonly several per record (formats, years, granularities). Remove → a metadata-only index or a link directory.
3. **The public discovery surface.** Search and browse over the whole corpus, open to anyone, with no prior knowledge of which organization holds what and, in the typical case, no account. Remove → an internal publishing/records tool or a private data service.
4. **The public-access posture.** The corpus is published once, for all comers: acquisition is governed by the usage terms/licenses recorded on or alongside the data, not by per-consumer grants, subscriptions, or entitlement decisions. Remove → Data Exchange Platform / subscription data service territory.

Jointly-held load-bearing tests: (1) alone = file listing; (2) alone = download mirror; (3) alone = vertical search engine; (1+2) without (3) = unorganized file repository; (1+3) without (2) = metadata index; (2+3) without (1) = anonymous bulk-download site; (1+2+3) without (4) = gated data service (drifts out of "public").

Evidence note: leg 1 is deliberately phrased "maintained… (authored, ingested, or harvested)" — broader than the government sibling's "created through the same platform's publisher side" — because aggregation via harvested/ingested records is a real generic-portal posture (UNdata's datamarts aggregate 20+ sources; EU-style federation not directly verified but the UNdata pattern is documented). The direct-publishing realization (CKAN's org-scoped create/edit/publish) is the documented Layer-A case; publisher-side tooling in the same system is **L1 common**, not definitional.

### L1 — Common Mature Structure

- Publisher-side tooling in the same system (create/edit records, attach distributions, publish) with roles
- Multi-publisher organization structure (departments/agencies/units as publishing units; or many aggregated sources under partnerships)
- Faceted/advanced search; browse listings by theme, publisher, geography, format
- In-place preview/exploration (grids, charts, maps) where data suits
- API delivery alongside file download, with developer documentation
- Freshness machinery: update dates on records, update calendars, activity/change history
- Contactable owners/sources; feedback channels; provenance/glossary material
- Engagement features (follow datasets/organizations, change notifications)
- Cross-portal links and specialized-database link-outs; harvesting/federation for aggregators
- Embeddable widgets / share links

### L2 — Variant / Optional Structure

- Operator class: government (→ sibling §24 Type), international organization, statistical agency, research institution, NGO/humanitarian network, enterprise (internal-gated drift), open community hub (CKAN's no-organization wiki-like mode)
- Corpus composition: heterogeneous file catalogs vs statistical time-series collections ("datamarts") vs microdata libraries; documents/apps sometimes catalogued alongside datasets
- Posture: direct publisher vs single-entry-point aggregator over many sources vs harvesting federation
- Terms granularity: per-record licenses vs site-level conditions vs per-dataset terms within one portal family
- Delivery emphasis: bulk-file-first vs API-first vs visualization-forward
- Portal families: one publisher operating complementary surfaces (flagship site + query tool + catalog + microdata library)
- Era machinery (not definitional): AI-era search, usage analytics, MCP/agent access (sibling-engine evidence)

### L3 — Vendor-specific

- CKAN: "package" legacy naming; Solr DisMax advanced-search syntax; sysadmin guide; organization role ladder (Member/Editor/Admin); demo instance
- World Bank: DataBank / Data Catalog / Microdata Library / WDI product names; widget mechanics; Development Data Group organization
- UNdata: "datamarts" vocabulary; SDMX Browse/Web Service; Update Calendar; Gapminder/SIDA/Statistics Sweden founding partnership; UN21 Award; Pocketbook/Yearbook lineage
- (From sibling pass, for continuity only: Socrata SODA/SoQL; ArcGIS Hub sites/initiatives; Huwise processors/connectors/harvesters)

## Vendor-specific Findings

- CKAN's "WordPress for data" analogy and no-organization "wiki-like datahub" mode — the mode shows the Type does not require institutional structure.
- World Bank operates the Type as a **family of complementary surfaces** (portal + query tool + catalog + microdata library), with the Data API explicitly the substrate of the flagship site — a publisher-side integration depth not seen in the CKAN docs.
- UNdata documents its own founding mission ("Statistics as a Public Good", 2005) — the oldest directly-observed instance, proving the core predates the modern SaaS feature set.
- Sibling engines (Socrata, Hub, Huwise) monetize the same engine as SaaS/platform-extension; Hub deliberately catalogs apps/documents beside data (content-family-agnostic catalog).

## Rejected Findings (checked and rejected as generalizations)

- **"A public data portal must be government-operated"** — rejected. CKAN names "research institutions, and other organizations"; Socrata SODA covers "governments, non-profits, and NGOs" (sibling Layer A); World Bank and UNdata are non-government operators with the same structure. The government case is a specialization (see Boundary Findings #1).
- **"A public data portal must render charts/maps in-browser"** — rejected. UNdata's core surface is table-first (PDF/CSV); CKAN previews are per-resource and optional ("if the data is suitable"). Visualization is L1.
- **"A public data portal is an API-first data service"** — rejected. File download is the floor everywhere observed; APIs are L1 delivery alongside files.
- **"Dataset records must be owned by organizations"** — rejected. CKAN explicitly supports organization-free datasets editable by any logged-in user.
- **"The portal is the system of record for the data"** — rejected. Portals publish copies/exports/views of data owned in source systems (World Bank compiles from member-country statistical systems; consistent with the sibling pass and the government-gis seam).
- **"Open licensing (CC-class) is definitional"** — rejected. What is common to all samples is that **usage terms are recorded and visible**; the specific openness of the license varies (World Bank "minimal restrictions"; Microdata per-dataset terms; UNdata conditions of use). Per-record open-license dropdowns are one implementation (CKAN).
- **"In-portal accounts/personalization are definitional"** — rejected. All three samples serve anonymous discovery/download; accounts unlock engagement features only (CKAN follow).

## Boundary Findings

1. **vs Government Open Data Portal (§24) — JOINT REVIEW DISCHARGED: keep-both (operator-specialization seam).** The government sibling's own research established that the engines are generic ("sold to governments and non-governments alike"; CKAN "used by national and local governments, research institutions, and other organizations"). This pass independently derives the same four-leg core from three non-government operators (engine, international financial institution, UN statistics division) — the government qualifier names the operator and its publication mandate (official non-personal public-sector data, proactive bulk publication, accountability attribution), not a different mechanism. Precedent: greenhouse-gas-accounting / carbon-accounting-platform keep-both. Both leaves stay documented and cross-referenced; the government sibling's L0 leg 1 ("created and maintained through the same platform's publisher side") is retained there as the direct-publishing realization; this leaf's leg 1 is phrased one level higher ("maintained… authored, ingested, or harvested") so aggregation postures fit. Consolidation recommended only at a future taxonomy pass.
2. **vs Data Explorer (§02.12 sibling, processed)** — seam RATIFIED from the portal side. Portal = catalog of dataset records whose closure is **acquisition**: find → evaluate (metadata/license/currency) → take the data away (download/API) for use elsewhere. Explorer = pre-structured published observations **re-cut and rendered live in-app** (compose selection → computed re-render). World Bank provides a documented coexistence proof: the Data Catalog ("comprehensive listing… easily downloaded, or accessed through the DataBank query tool") vs DataBank (slicing, custom queries, visualizations) are separate named products with different closures. Removal tests: remove live view composition/rendering from an explorer → it becomes a portal; add a file catalog to an explorer → still an explorer with a catalog; remove acquisition/delivery from a portal → it becomes a metadata index.
3. **vs Data Catalog (§13)** — consistent with the data-catalog pass: a catalog describes an organization's internal data estate and points to where data lives; the portal is an external publication/delivery venue (hosts or directly exposes the data). A catalog surface exists inside portals as an adjacent surface. Remove delivery/open publication → catalog.
4. **vs Data Exchange Platform (§13)** — consistent with the data-exchange pass: exchanges bind each consuming party via explicit entitlements; the portal publishes once for all comers under terms. Add per-consumer entitlement → exchange.
5. **vs Vertical / General Search Engine (§02.02)** — a search engine discovers and links; it does not maintain dataset records or deliver the data as its own content (metadata-only index fails L0 leg 2). Dataset-discovery crawlers are search engines, not portals.
6. **vs Information Portal / Directory Application / Listings Platform (§02.11)** — directories aggregate entries for navigation with content held elsewhere; the portal's unit of record is a dataset with distributions, and its defining closure is data acquisition. Consistent with the general-reference-database pass ("datasets/files vs editorial prose entries").
7. **vs Government Transparency Portal (§24, processed)** — consistent with its pass: the transparency portal's organizing unit is the accountability strand of the publishing government's own conduct (documents/records for scrutiny); this Type's organizing unit is the dataset record for reuse, under any operator. The transparency pass's joint-review note with §02.12 is addressed here: keep-both on the unit-of-publication + operator-identity line.
8. **vs Digital Collection Portal / Institutional Repository / Digital Library Platform (§23)** — those publish collection items / research outputs / bibliographic holdings for viewing or whole-item delivery; the data portal publishes datasets for programmatic and analytical reuse. Consistent with those passes' boundary rows.
9. **vs Product/Developer Documentation Portal (§02.07 / §12)** — documentation portals publish prose about a product/API; the data portal's content is the data itself. API documentation pages inside a data portal serve the distributions (L1), not a different Type.

### "去掉什么就变成另一个 Type" removal tests

- Remove the maintained dataset records → file listing / search engine.
- Remove the distributions (metadata only) → vertical search engine / Data Catalog.
- Remove the public discovery surface → internal publishing tool / bare download mirror.
- Remove the public-access posture (per-party entitlements) → Data Exchange Platform / subscription data service.
- Remove acquisition closure (data re-cut and rendered live in-app) → Data Explorer.
- Remove dataset semantics (prose entries/documents) → Information Portal / Transparency Portal / Reference Database.
- Remove generic operators (government-only) → Government Open Data Portal (§24 specialization).

## Historical / Market-Sample Check

- **UNdata (2005)** — documented on its own About page: launched 2005 under "Statistics as a Public Good" with single-entry-point search/download over UN databases. Fits the four-leg core with no in-portal visualization, no modern analytics, no harvesting machinery. ✓
- **Early CKAN instances** — CKAN's own user guide retains the 2006–08-era "packages" vocabulary; the documented feature floor (dataset + resources + license + faceted search) is the full L0 without previews/APIs-required. ✓
- **Table-first statistical publication** — UNdata's popular statistical tables (PDF|CSV with update dates) show the Type works with a minimal, download-oriented surface. ✓
- **Pre-portal static publication** (FTP directories / statistical-yearbook pages) — sits *outside* the Type: no managed dataset records/catalog application (consistent with the sibling pass's historical finding). ✓
- **Non-US / platform-native / regional** — UNdata and the World Bank are global South-facing institutions; the sibling pass confirmed Swiss/Mexican/Singapore portals. The model is not one geography's shape. ✓
- Definition therefore not over-fitted to the current SaaS/AI-era feature set: no API, preview, charts, organizations, analytics, harvesting, or AI is definitional.

## Uncertainties

1. data.europa.eu unreachable (404 ×2 URLs) — the EU federated-aggregation pole not directly verified; aggregation claims rest on UNdata only. No harvesting-federation generalization made beyond sibling-engine evidence (Huwise harvesters; Socrata Open Data Network).
2. Kaggle and HDX unreachable — community-published and humanitarian poles not directly verified; kept as weakly-phrased variants (CKAN's wiki-like mode is the only direct non-institutional evidence).
3. World Bank / UNdata publisher-side internals not documented on reachable pages — publisher-side-in-same-system held L1 on CKAN Layer A + sibling-engine Layer B, not generalized as definitional.
4. Metadata-standard adoption (DCAT etc.) — not verified for any sample; not claimed.
5. Subscription statistics platforms (Statista-class) not sampled — the entitlement seam (L0 leg 4) is argued structurally and from the data-exchange pass's continuity, not from a sampled negative case.
6. Whether taxonomy should merge §02.12 Public Data Portal with §24 Government Open Data Portal — resolved keep-both at joint review (see Boundary #1); final consolidation is a taxonomy-pass decision.

## Final Synthesis

A Public Data Portal is a publication platform, operated by any body, whose world is organized around maintained dataset records: persistent, individually addressable, metadata-described entries to which the data itself is attached as downloadable files and/or queryable APIs. The public discovers the corpus through an open search/browse surface — no account, no prior knowledge of who holds what — evaluates each dataset on its record (content, sources, coverage, currency, usage terms), and takes the data away for reuse elsewhere. The corpus is published once for all comers under recorded terms, not entitlements; records are maintained by the portal whether authored in place, ingested, or harvested. Publisher-side tooling, multi-publisher structures, previews and charts, APIs, freshness machinery, and engagement features are the common mature layer; operator class, corpus composition, aggregation posture, and terms granularity are variants. The core predates the modern feature set (UNdata 2005, early CKAN) and survives in table-first and single-agency forms; the government-operated case is the operator specialization already documented as Government Open Data Portal (§24), and the live-analysis sibling is Data Explorer (§02.12) — separated by the acquisition-vs-rendering closure.
