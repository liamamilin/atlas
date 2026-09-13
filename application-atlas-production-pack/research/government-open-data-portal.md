# Research Notes — Government Open Data Portal

Research date: 2026-09-07
Slug: government-open-data-portal
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand, from real products, what a **Government Open Data Portal** actually is: the core objects it manages, how a government publishes data to it, how the public discovers and reuses that data, what governance and delivery mechanisms exist, and where the boundary lies with neighboring Types (Data Catalog, Data Exchange Platform, Government Transparency Portal, FOI/Public Records, Government GIS, Public Data Portal §02.12, Civic Engagement / 311).

## Initial Boundary (hypothesis before research)

- Core use: a government (or public body) publishes non-personal datasets about its jurisdiction/operations for anyone to find, download, and reuse.
- Primary users: government data publishers (agency staff, open-data program managers) on one side; citizens, developers, journalists, researchers, businesses on the other.
- Nearest neighbors: Data Catalog (internal metadata discovery), Data Exchange Platform (entitlement-based sharing), Government Transparency Portal (document publication), FOI/Public Records Request Platform (reactive per-request disclosure), Government GIS (authoring/analysis engine), Public Data Portal (§02.12) — potential duplicate leaf.
- Unknowns: what exactly makes the "government" qualifier structural; whether publisher-side management is definitional; whether API delivery / preview / analytics are core or common.

## Research Questions

1. What is the core object model (dataset, resource/distribution, organization/publisher, topic/group)?
2. What does the publisher workflow look like (create → describe → attach data → publish → keep current)?
3. How is data actually delivered (download, API, linked, harvested)?
4. What does the public discovery surface look like (search, filters, dataset page, preview)?
5. What governance exists (roles, approval, private→public states, licenses, metadata standards)?
6. What engagement/reuse features exist (feedback, follow, contact owner, usage analytics)?
7. What is the "government" specialization vs generic data portals?
8. Where do the boundaries with the 8 neighbor Types run, and what removal test discriminates each?

## Representative Products

| Product | Vendor / lineage | Philosophy | Customer layer |
|---|---|---|---|
| CKAN | Open-source (OKF trust; stewards Datopian/Link Digital) | open-source "CMS for data"; powers data.gov, Canada, Australia (800+ orgs), Singapore, Mexico, Switzerland, Berlin | national + regional + city |
| Socrata (Tyler Data & Insights) | Acquired by Tyler Technologies 2018 | commercial SaaS open-data platform; strong developer API culture (SODA); Open Data Network consumer face | US states/cities/federal |
| ArcGIS Hub | Esri | engagement-first open data built on the GIS platform; sites/initiatives/catalogs | government agencies (US + international) |
| Opendatasoft → Huwise (rebrand 2025/26) | French SaaS vendor, 14+ years | open-data portal heritage, evolved into "data product marketplace"; open-government as one use case among several | cities (Vancouver), states (Bahrain, Qatar), public bodies, energy/banking |

Rationale: market leadership (CKAN is the most deployed open-source portal; Socrata dominates US municipal; Hub rides the dominant GIS platform; Opendatasoft is the major European SaaS), different packaging philosophies (open source vs SaaS vs platform extension), different geographies, national vs city scale.

## Sources

Tier 1 (official operational documentation) — all fetched 2026-09-07:

- CKAN User Guide — https://docs.ckan.org/en/latest/user-guide.html (fetched in full; richest single source)
- CKAN product site — https://ckan.org/ (positioning, showcase, government pole)
- Socrata SODA Developers — https://dev.socrata.com/ (API docs hub), https://dev.socrata.com/publishers/ (publisher guide)
- ArcGIS Hub documentation — https://doc.arcgis.com/en/hub/ (resources hub), https://doc.arcgis.com/en/hub/content/content-basics.htm (content catalogs, preview pages)
- Huwise (Opendatasoft) Help hub — https://help.opendatasoft.com/ ; User guide — https://userguide.huwise.com/ (category structures); https://userguide.huwise.com/en/categories/480130-building-data-assets ; https://userguide.huwise.com/en/categories/1459458-building-datasets ; https://userguide.huwise.com/en/categories/480194-discovering-and-exploring-data
- Huwise product site — https://www.huwise.com/en/ (positioning, capabilities, use cases)

Source-access limitations:

- socrata.com → 404; tylertech.com/products/socrata → 403; knowledge.socrata.com → timeout. Socrata positioning evidence rests on the developer site footer/links and the publisher guide; support-KB articles about the web publishing UX were referenced by the publisher guide but NOT fetched. Keep Socrata web-UX claims general.
- doc.arcgis.com "what is ArcGIS Hub" page → empty response twice, alternate URL 404. Hub evidence = resources page + content-basics doc + prior government-gis pass (ArcGIS Hub documented there as the separate open-data/engagement product on top of the ArcGIS organization).
- CKAN harvesting/federation machinery not verified this pass (user guide does not cover it) — do not claim for CKAN.
- Exact metadata-schema standard adoption (DCAT etc.) per product not directly verified — Huwise has "harvesters" category and RDF/linked-data resource types appear in CKAN docs; do not generalize.

Prior related passes used for boundary continuity (same repo):

- research/government-gis.md — boundary vs Government Open Data Portal (authoring/analysis engine vs publication catalog; ArcGIS Hub ships as separate product)
- research/data-exchange-platform.md — "remove the entitlement → open-data publication portal"
- research/data-catalog.md — "open-data portal does contain a dataset catalog — adjacent surface, different primary job"
- applications/foi-public-records-request-platform.md — "records simply published with no per-request processing → open-data or transparency portal"
- applications/civic-engagement-platform.md — "remove resident contribution → transparency/open-data portal"
- STATUS.md lines for 311 (open-data feeds = L2 there), election-results-management (results exports flow into open-data portals)

---

## Product A — CKAN

Evidence layer: A (direct, official user guide fetched in full + product site).

### Key observations

- Self-description: "a tool for making open data websites… like a content management system like WordPress — but for data, instead of pages and blog posts. It helps you manage and publish collections of data. It is used by national and local governments, research institutions, and other organizations who collect a lot of data." Consumers: "developers, journalists, researchers, NGOs, citizens, or even your own staff."
- **Dataset** is the publication unit: search results are individual datasets. A dataset = (1) metadata (title, publisher, date, formats, license…) + (2) any number of **resources** holding the data itself. Resources can be CSV, Excel, XML, PDF, image, RDF linked data; a resource can be **stored internally or linked** ("Link to a file" / "Link to an API"). Different resources may carry different years or different formats of the same data.
- Historical note: datasets were called "packages" in early versions (name persists in API).
- **Organizations** own datasets ("Normally, each dataset is owned by an organization… if CKAN is being used as a data portal by a national government, the organizations might be different government departments, each of which publishes data"). Each organization can have its own workflow and authorizations, managing its own publishing process.
- **Roles**: organization Member (sees org's private datasets) / Editor (edit and publish datasets) / Admin (add/remove/change member roles); site-wide **sysadmin** for site administration.
- **Private → Public lifecycle**: by default a newly created dataset is private (visible only to its organization's members, invisible in others' searches) and "when it is ready for publication, it can be published at the press of a button. This may require a higher authorization level within the organization."
- Dataset creation flow: Create dataset screen → title/description/tags/license (dropdown)/organization → add data screen (upload file or link to file/API, per-resource name/description/format) → additional info (visibility, author, author e-mail, maintainer, custom fields) → finish.
- Deleting a dataset hides it (recoverable by authorized users via URL, "undeleted") rather than destroying it.
- **Public discovery**: free-text search on every page; faceted filters (tags, formats) combinable in left column; search within an organization; geospatial search by selecting an area on a map "possible with an extension"; advanced fielded search (Solr-backed).
- **Dataset page**: name/description/other info + resource links; per-resource page with **preview** (grid view for CSV/XLS, map and graph views where suitable; image/PDF/HTML previews) and download; **activity stream** (history of changes); groups tab.
- **Engagement**: Follow a dataset/organization/user → news feed of changes (new/modified datasets); requires login; user profiles.
- **License field** is emphasized ("important… so that people know how they can use the data").
- Full **API** ("machine interface") documented for extensions and integrations.
- Positioning (product site): "open-source data management system (DMS) for powering data hubs and data portals… powers hundreds of data portals worldwide"; "CKAN for Government" (EU, Americas, Asia, Oceania) and "CKAN for Enterprise" (resources, energy, pharma, finance — internal data assets); Digital Public Good (UN registry); held in trust by Open Knowledge Foundation.

## Product B — Socrata / Tyler Data & Insights

Evidence layer: A for developer/publisher docs (dev.socrata.com fetched); positioning partially limited (marketing site unreachable — see limitations).

### Key observations

- Platform framing: "The Socrata Open Data API (SODA) allows you to programmatically access a wealth of open data resources from governments, non-profits, and NGOs around the world." Socrata "acquired by Tyler Technologies in 2018… now the Data and Insights division of Tyler."
- **Consumer side**: getting-started guide, "Finding Open Data", API endpoints, SoQL query language, response formats JSON / GeoJSON / CSV / RDF-XML; typed columns including Location, Point, MultiPoint, Line, MultiLine, Polygon, MultiPolygon (geospatial is first-class at the column-datatype level), checkbox, timestamps, text, URL; system fields; app tokens; CORS.
- **Dataset as managed object**: publisher docs speak of datasets as addressable assets; **Metadata API** for "asset-level metadata"; **Discovery API** to "review assets in your data catalog and discover assets across our entire corpus of open data."
- **Publisher side**: web interface recommended for first import ("uploading your data file and creating your initial dataset through our web interface… review how our systems will import your dataset, what datatypes will be selected"); referenced support articles "How to Create and Publish a New Dataset" and the "Data Management Experience" (not fetched — keep general).
- **Automated keep-current machinery**: Socrata Gateway (on-platform agent behind the firewall connecting on-prem/cloud source systems — plugins for Esri, AWS S3, MS SQL, Excel), DataSync (cross-platform Java app for scheduled updates, "intelligent update method… even when performing what would otherwise be a full replace"), Safe FME writer, Pentaho Kettle connector, SODA Producer API (bulk replace via PUT, bulk update via POST, single-row add/update/delete), Dataset Management API; SDKs in many languages.
- **Cross-domain consumer face**: Open Data Network — "Search the Open Data Network for datasets from all our customers and partners."
- Support model includes "How do I contact a dataset's owner" article — dataset owner/contact accountability concept (referenced title only).

## Product C — ArcGIS Hub (Esri)

Evidence layer: A for content documentation (resources page + content basics fetched); "what is" page unreachable; supplemented by prior government-gis pass.

### Key observations

- Framing: "ArcGIS Hub cloud-based engagement platform"; tutorial: "Learn how to create a site, share content, and brand your design"; premium tutorial: "create an initiative and use premium functionality to manage followers and engage with your community." Training blurb: "Organizations around the world use ArcGIS Hub to promote transparency, collaborate across departments, and make critical data accessible."
- Prior pass (government-gis): Hub documented as a "cloud-based engagement platform" for creating sites that "showcase apps and data without the need for any custom coding" — the open-data/public-engagement function ships as a separate product on top of the ArcGIS organization, not as part of the base GIS.
- **Content model**: "Content refers to the items — including apps, maps, data, and documents — that you want to add to a search catalog or display on your site. Content editors can manage items in the content workspace." Role-gated ("Configure roles and privileges").
- **Catalog per site**: "Each site that you create has a catalog that contains your content. Initiatives and projects also have content catalogs. You can configure these catalogs to include the content items that you want users to discover through the search bar. Only items that you add to the content catalog appear in search results, and items are only visible to those with whom the item is shared, such as a group or members of the primary ArcGIS Online organization."
- **Sharing/access**: items visible only to those with whom the item is shared — sharing levels gate public exposure.
- **Preview pages** on selecting a search result: full details page ("about view" — summary, thumbnail, download, view metadata, create maps and stories; all items have one) and explore page ("explore view" — full-screen content display with side panel; most spatial and tabular data, apps, maps have one; opens by default with a View map button or selectable layer list for a dataset).
- **Structure beyond datasets**: sites, initiatives, projects, events (initiatives/projects/events require Hub Premium subscription); site layouts with cards (Application, Category, Gallery); event catalogs; discussion boards for community engagement; Projects for organizing/tracking work; data migration tooling documented in blog.
- Interesting: documents and apps live alongside datasets as catalog items — the catalog is content-family-agnostic, not dataset-only.

## Product D — Opendatasoft → Huwise

Evidence layer: A (user guide category structures + product site).

### Key observations

- Lineage: "After fourteen years of existence, Opendatasoft becomes Huwise" (2025/26). Positioning shifted to "data product marketplace"; open data remains a documented use case: "Open government & transparency" ("Publish public information to deliver full transparency through observatories, public information sites…") and "Open data & compliance" ("Share data to meet regulatory requirements"); sectors: Local Government, Central Government & public bodies, plus energy, transport, banking.
- Heritage claim: "Built on over 14 years of experience in making data exploration accessible to all." Customers in the government pole: City of Vancouver, Western Parkland Councils, Bahrain, Qatar, Digital Ajman; Banque de France; energy utilities (UK Power Networks "Open Data Manager", E-REDES open data with 20,000 annual unique users, 350,000 monthly API calls — figures are vendor-stated, marketing layer).
- **User guide structure** (the authoritative workflow map):
  - *Building data assets*: building datasets (configuring datasets; **creating and federating a dataset**; types of source files; forms), building pages, building visualizations, **processors** (data transformation), **connectors** (source ingestion), **harvesters** (external ingestion).
  - *Discovering and exploring data*: exploring data portals; exploring datasets; creating maps and charts; legacy: sharing, reusing and reacting.
  - *Managing data assets*: "Make your data discoverable, design your asset page, and keep track of usage."
  - *Portal management*: "Configure your workspace, manage your users, and analyze how your data is used" (10 subcategories, 63 articles).
- **Capabilities surface** (product nav): data catalog, business glossary, data quality (processing/enriching), metadata management (customizable models + smart data-entry assistance), data lineage, appearance/white-labeling, user & access management (roles in sync with governance policies), data visualization, automation, analytics & conversion (track consumption/user behavior), AI search, data products, API & export ("robust APIs and multi-channel distribution"), collaboration workflows, MCP & AI agents.
- Interpretation: same Type engine (publish datasets → public portal → explore → APIs) with the platform expanding outward into internal governance/marketplace territory. The government open data portal is its founding pole; the current flagship positioning is broader. Use with care: vendor-specific expansion is L3.

---

## Cross-product Comparison

| Dimension | CKAN | Socrata/Tyler | ArcGIS Hub | Huwise (Opendatasoft) |
|---|---|---|---|---|
| Central object | Dataset (metadata + resources) | Dataset/asset (typed columns; metadata API) | Content item (apps/maps/data/documents) in per-site catalogs | Dataset (created, configured, federated) |
| Publisher side in same system | Yes — create/edit UI, org-scoped | Yes — web "Data Management Experience" + automation APIs | Yes — content workspace | Yes — building/configuring datasets + portal management |
| Visibility model | Private (org-only) → Public at publish; may need higher role | Publishing workflow (web first, then automated) | Sharing/gating via groups & org; catalog inclusion controls search visibility | User & access management; roles synced to governance |
| Multi-publisher structure | Organizations (departments) with own workflows/authorizations | Domain/tenant per customer; Open Data Network federates customers+partners | Site/initiative structure over an ArcGIS organization; departments as content editors | Workspace/portal per organization; harvesters federate external sources |
| Delivery | Upload or link (file / API resource) | Download + SODA APIs (JSON/GeoJSON/CSV/RDF-XML) | Download from details page; explore view | Export + "robust APIs and multi-channel distribution" |
| Public discovery | Faceted search, filters, org-scoped search, (extension) map search | Dataset pages + Open Data Network cross-domain search | Site search bar over configured catalogs | Exploring portals/datasets; AI search (current) |
| Preview / exploration | Grid/map/graph resource previews | Explore via APIs + datatypes (geo first-class) | Explore page (map/data full-screen) for spatial/tabular | Maps & charts; visualizations builder |
| Keep-current | Edit/re-upload; activity stream | Gateway/DataSync/FME/Producer API scheduled updates | Item management + migration tooling | Processors/connectors/harvesters; automation |
| Governance artifacts | License dropdown; author/maintainer contacts; custom fields | Metadata API; app tokens | Roles & privileges; sharing | Metadata management, glossary, lineage, quality |
| Engagement | Follow datasets/orgs/users; news feed | Contact dataset owner (support article); Open Data Network | Followers, initiatives, events, discussion boards | Collaboration workflows; usage analytics & conversion |
| Packaging | Open source, self-hosted, extension ecosystem | SaaS (Tyler Data & Insights) | Subscription product on the ArcGIS platform (Premium tier for initiatives) | SaaS; evolved into data product marketplace |

### Cross-product commonalities (candidate L1)

1. Dataset as the named, persistent unit of publication (all four) — the unit the search results, pages, and APIs are organized around.
2. A public catalog/search/browse surface over the corpus (all four).
3. Dataset detail page exposing metadata + the actual data (download and/or API) (all four).
4. The same platform hosts both the publisher side and the public side (all four).
5. Publisher-side role/permission structure and multi-department (multi-publisher) organization (all four, differently named).
6. License / usage-terms visibility to reusers (CKAN explicit; others via metadata).
7. Metadata quality / completeness machinery (all four; Huwise most explicit).
8. Keep-current machinery (scheduled updates, connectors, gateways) (Socrata, Huwise explicit; CKAN via editing/API; Hub via item management/migration).
9. Preview/exploration of the data in place (all four; depth varies).
10. Usage/engagement signals (follow, contact owner, analytics) (all four; forms vary).
11. Cross-portal/cross-corpus discovery federation (Socrata Open Data Network; Huwise harvesters; Hub is one pole of an org's ecosystem).

## Canonical Model (abstraction)

### L0 — Defining Invariant (minimal; jointly held)

1. **The published dataset record.** A persistent, individually addressable dataset entry carrying descriptive metadata (title, description, publisher, license/usage terms, currency) and serving as the unit of discovery. The record is created and maintained through the same platform's publisher side. Remove → a generic file listing or document site.
2. **Attachable data distributions.** The data itself — downloadable files or machine-readable API endpoints — attached to the dataset record as distributions (stored or linked). Remove → a metadata-only catalog or a documents portal.
3. **The public catalog surface.** Search/browse over the whole corpus organized by publisher/topic/format, open to anyone without knowing which agency holds what. Remove → an internal publishing/records tool.
4. **Open-access posture.** The published corpus is openly accessible for reuse — access is governed by license terms, not by per-consumer entitlements or grants. Remove → Data Exchange Platform territory.

Government specialization (the §24 qualifier): the operator is a government/public body publishing its own official, non-personal data for public reuse. Remove → generic open data portal (the §02.12 Public Data Portal pole); the platform model itself is identical.

### L1 — Common Mature Structure

- Multi-publisher organization structure (departments/agencies as publishing units with their own roles and workflows)
- Publisher roles + publish/approval step (private/draft → public)
- In-place preview/exploration (tables, maps, charts)
- Machine-readable API delivery alongside file download
- Keep-current automation (connectors, scheduled updates, federation/harvesting)
- Metadata completeness/quality machinery; contactable dataset owner/maintainer
- Engagement: follow, feedback, contact-owner, usage analytics
- Cross-portal discovery networks

### L2 — Variant / Optional

- Packaging: open-source self-hosted vs SaaS vs platform-extension product
- Scale/scope: single-agency portal vs national multi-agency federation vs cross-jurisdiction networks
- Content-family breadth: dataset-only vs datasets+documents+apps (Hub-style catalogs)
- Geospatial-first portals (geo datatypes, map search/explore as primary surface)
- Engagement-forward variants (initiatives, events, discussion boards)
- Regulatory-compliance publication (structured disclosure obligations)
- Evolution poles: internal data marketplace / governance catalog expansion (Huwise, CKAN-for-Enterprise)
- AI-era extensions (AI search, MCP/agent access — current-generation only)

### L3 — Vendor-specific

- CKAN: "package" legacy naming; extension-based geospatial search; sysadmin guide specifics; organization role ladder names
- Socrata: SODA/SoQL naming; Gateway/DataSync/FME tooling names; 4x4 asset identifiers (known from ecosystem, not re-verified this pass — do not publish); Open Data Network brand
- Hub: initiatives/projects/events Premium tier; site layout cards; ArcGIS Online org coupling
- Huwise: processors/connectors/harvesters taxonomy; data product marketplace positioning; MCP server; Forrester ROI claims (marketing)

## Vendor-specific Findings

- CKAN's WordPress-for-data self-analogy and "hundreds of portals" claim (product site, marketing layer).
- Socrata's SODA is also a *producer* API — publishers can upsert rows programmatically; the same interface serves consumer queries (SoQL). This dual consumer/producer API symmetry is distinctive.
- Hub's catalog deliberately includes apps and documents beside data; engagement tools (initiatives/events/discussion boards) are Premium — open data here is a facet of community engagement.
- Huwise's rebrand to "data product marketplace" shows a vendor lineage drifting from the Type's center; its open-government use case page is the anchor for the government pole.

## Boundary Findings

1. **vs Data Catalog (§13)** — the catalog is a metadata lens over an org's own estate; it describes data that lives elsewhere and orients internal discovery/governance. The open data portal is an external publication/delivery venue: it hosts or directly exposes the data for download/API. A dataset catalog surface exists *inside* portals (adjacent surface), but the primary job (external open publication + delivery) differs. Removal test: remove delivery/open publication → catalog; remove internal-estate orientation/governance lens → portal.
2. **vs Data Exchange Platform (§13)** — the exchange binds consumers to offerings via explicit entitlements (invitation/subscription/grant, terms at acceptance). The open data portal publishes once for all comers under license terms. Removal test: remove per-consumer entitlement → open data portal; add it → data exchange. (Consistent with the data-exchange pass: "an open public tier is still an entitlement decision made once for all comers" — the two Types differ in whether per-party decisions exist at all.)
3. **vs Government Transparency Portal (§24, leaf pending)** — the transparency portal publishes accountability documents/records (budgets, expenditures, meeting records) whose job is public accountability; the open data portal publishes datasets whose job is reuse (machine-readable, licensed, API-accessible). Blur: financial datasets serve both; CKAN resources may be PDFs; Hub catalogs include documents. Discriminator: unit of publication (dataset with distributions vs published document/record set) and primary job (reuse vs accountability narrative). Joint review with Government Transparency Portal recommended.
4. **vs FOI / Public Records Request Platform (§24)** — reactive per-request processing (requester relationship, deadlines, exemptions) vs proactive bulk publication with no per-request processing and no requester relationship. Consistent with the FOI pass's own boundary row.
5. **vs Government GIS (§24)** — authoring/analysis engine over authoritative geographic base vs publication catalog for reuse. Confirmed structurally: the leading GIS vendor ships open data as a separate product (Hub) on top of the GIS organization. (Consistent with the government-gis pass.)
6. **vs Public Data Portal (§02.12, leaf pending)** — potential duplicate/alias. The researched products are generic portal engines used by governments and non-governments alike; the §24 leaf is the government-operator specialization. Recommend joint review; this pass writes the government specialization and records the seam.
7. **vs 311 / Civic Engagement (§24)** — those center resident-initiated requests/contributions processed by the government; the portal is one-way proactive publication. Open-data feeds appear as L2 export features there (consistent with the 311 pass).
8. **vs Information Portal / Directory Application (§02.11) and Data Explorer (§02.12)** — directories list entries for navigation; explorers center ad-hoc analysis. The open data portal's defining closure is the acquisition of reusable data, not navigation or analysis authoring. (Portal preview/exploration is L1; the analysis workbench is a different Type.)

### "去掉什么就变成另一个 Type" 判据 (removal tests)

- Remove the dataset record with distributions → transparency/documents portal or bare file listing.
- Remove the public catalog surface → internal publishing/records tool (or an intranet CMS).
- Remove the open-access posture (add per-party entitlement) → Data Exchange Platform.
- Remove delivery of the data itself (metadata only) → Data Catalog.
- Remove the government operator specialization → generic Open Data Portal (§02.12 Public Data Portal).
- Remove the reuse license/metadata framing but keep publication → generic download site (adjacent, not this Type's engine).

## Historical / Market-Sample Check (§24)

- Early-2010s generation (e.g., CKAN-powered national portals launched 2010): dataset records + browsable/searchable catalog + file downloads + license notes. Fits L0 without previews, APIs-as-required, analytics, or federation machinery. ✓
- Single-agency regional portals (one city/agency publishing its own datasets with a simple browse-and-download list): fits L0 — the catalog may be browse-only; multi-organization federation is L1. ✓
- Pre-portal statistical-agency publication (static FTP/HTML file pages): sits *outside* the Type as bare file publication — no managed dataset records/catalog application. The L0's dataset-record + catalog requirement is what separates the application Type from plain web publishing. (Noted as the historical "before" state vendors position against; consistent with the data-exchange pass's "before" framing.)
- Non-US / platform-native: Swiss opendata.swiss, Mexican datos.gob.mx, Singapore data.gov.sg (CKAN showcase) confirm the model is not US-vendor-shaped. ✓
- Definition therefore not over-fitted to the current SaaS/AI-era feature set: no API, preview, analytics, AI, or engagement machinery is definitional.

## Uncertainties

1. Socrata's web publisher UX specifics (import review, publish states) — support-KB articles referenced but not fetched; marketing site unreachable. Claims kept general.
2. ArcGIS Hub "what is" page unreachable; positioning partially inferred from resources page, training blurbs, and the prior government-gis pass.
3. Metadata-standard adoption (DCAT etc.) per product — not directly verified; do not generalize in final doc.
4. CKAN harvesting/federation machinery — not verified this pass; attribution of federation features made only for Huwise (harvesters) and Socrata (Open Data Network).
5. Whether the taxonomy should keep Government Open Data Portal (§24) and Public Data Portal (§02.12) as separate leaves — flagged for joint review.
6. Government Transparency Portal leaf pending; boundary written from this side only.

## Final Synthesis

A Government Open Data Portal is a government-operated publication platform whose world is organized around published dataset records: persistent, metadata-described entries to which the data itself is attached as downloadable files or API-accessible distributions. The same system carries both sides — agencies' publishing staff manage datasets through organization-scoped publisher tooling (with role-gated private→public release), while the public discovers the corpus through an open catalog (search/browse/filter), evaluates each dataset on its metadata page (license, currency, owner), previews it in place, and takes the data away as downloads or API calls for reuse. Access to the published corpus is governed by license terms rather than per-consumer entitlements — the seam against data-exchange products — and the corpus is delivered openly rather than described internally — the seam against data catalogs. Common mature structure adds multi-agency federation, preview/visualization, keep-current automation, engagement and usage analytics; packaging, scale, geospatial-first, and engagement-forward postures are variants. The defining structure fits the early-2010s national portals and single-agency regional portals without any modern machinery, and the underlying engine is generic (used by research institutions and enterprises); the government qualifier names the operator and the publication mandate, not a different mechanism.
