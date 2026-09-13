# Research Notes — Data Catalog

Research date: 2026-09-07
Leaf: Data Catalog (DIRECTORY.md §13 Data, Analytics & AI Systems, line 994)

## Research Goal

Understand what a Data Catalog actually is as an Application Type: what its world is made of (the central objects), how its inventory is populated and kept current, how users discover and evaluate data, which structures are definitional vs. merely common in the current market, and where its boundaries lie against neighboring data-platform Types (Metadata Management, Data Governance, Data Lineage, Data Warehouse/Lakehouse, Enterprise Search).

## Initial Boundary

Working hypothesis before research:

- Core purpose: help people in an organization discover, understand, and evaluate data that lives in many separate systems — without the catalog holding the data itself.
- Likely central object: a catalog entry (asset record) standing for an external data asset, carrying technical + business metadata.
- Likely core loop: populate inventory (manually or automatically) → search/browse → land on an entry → evaluate understanding/trust → use the data or request access → curation keeps context accurate.
- Nearest Types: Metadata Management Platform, Data Governance Platform, Data Lineage Platform, Data Quality Platform, Data Warehouse / Lakehouse Platform, Enterprise Search / Internal Knowledge Search, Government Open Data Portal, Master Data Management.
- Likely confusions: catalogs vs. governance platforms (suites blur them); catalogs vs. a warehouse's own schema browser; catalogs vs. document search.

## Research Questions

1. What does a catalog entry contain? What is the minimum structure of an entry?
2. How do entries get created and kept current — automated harvesting vs. manual registration?
3. How do users find data (search mechanics, browse organization, filters/facets)?
4. How is "understanding" conveyed on an entry (schema, descriptions, terms, profiles, samples)?
5. How is trust signaled (ownership, certification, popularity/usage, quality, lineage)?
6. What stewardship/governance machinery exists (owners, workflows, tags/policies, access requests)?
7. Which roles use the catalog and how do their surfaces differ?
8. What are the main interfaces (search page, entry page, lineage view, admin console, APIs)?
9. Which capabilities are definitional, and which are common-but-not-definitional or optional?
10. What breaks the boundary toward neighboring Types?

## Representative Products

Selected for market representation, documentation quality, distinct product philosophies, and distinct customer tiers:

| Product | Philosophy / position | Tier |
|---|---|---|
| Alation | commercial enterprise leader; behavior/usage-driven catalog ("people-first governance") | large enterprise |
| Collibra | governance-first data intelligence suite; catalog inside a governance platform | large enterprise |
| Microsoft Purview (Data Map + Unified Catalog) | hyperscaler-bundled cloud governance/catalog; sold inside a security+compliance platform | enterprise / Microsoft estates |
| Atlan | modern cloud-native "active metadata / context layer for AI" startup pole | mid-market to enterprise |
| OpenMetadata | open-source unified metadata platform (self-hosted OSS pole) | OSS / teams to enterprise |

## Sources

Tier 1/2 official surfaces fetched 2026-09-07:

- Alation
  - Product page: https://alation.com/product/data-catalog/ (Tier 2; includes vendor's own definition of "data catalog" and FAQ distinguishing catalog vs. dictionary vs. glossary)
  - Operational docs: https://docs.alation.com/ index; https://docs.alation.com/en/latest/welcome/About/index.html ; https://docs.alation.com/en/latest/welcome/CatalogBasics/RolesOverview.html (Tier 1)
  - Limitation: https://help.alation.com/s/ is a JS-rendered Salesforce site; fetch returned a CSS error after one attempt. docs.alation.com (Customer Managed docs) was used instead. Note on docs.alation.com: from Aug 18 2026 cloud docs move to the help center; this site remains for customer-managed deployments.
- Collibra
  - Product page + FAQ: https://www.collibra.com/us/en/products/data-catalog (Tier 2; includes vendor definition and "who uses a data catalog" list)
  - Limitation: detailed product documentation (docs.collibra.com) not fetched; governance-depth claims kept moderate.
- Microsoft Purview
  - https://learn.microsoft.com/en-us/purview/purview (platform overview, Tier 1)
  - https://learn.microsoft.com/en-us/purview/data-map (Tier 1)
  - https://learn.microsoft.com/en-us/purview/unified-catalog (Tier 1)
- Atlan
  - https://docs.atlan.com/ (docs root, Tier 1)
  - https://docs.atlan.com/get-started/what-is-atlan (Tier 1)
  - https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets (Tier 1)
- OpenMetadata
  - https://docs.open-metadata.org/ (docs root, Tier 1)
  - https://docs.open-metadata.org/v2.0.x/how-to-guides/data-discovery (Tier 1)

Evidence layers: A = directly observed on the cited official page; B = cross-product commonality; C = canonical inference.

## Product A — Alation

### Key observations (Layer A unless noted)

- Vendor definition (product-page FAQ): "A data catalog is a collection of metadata, combined with data management and search tools, that helps analysts and other data users to find the data that they need, serves as an inventory of available data, and provides information to evaluate fitness of data for intended uses."
- Catalog = "comprehensive inventory of all your enterprise data from multiple data storage sources, including databases, file systems, business intelligence or data visualization tools… together with curated content generated by machine learning … and manually by your data stewards."
- Population is documented as an iterative five-step cycle: (1) metadata extraction (MDE) builds the basic structure from the database's own metadata (schemas, tables, columns, types); (2) query log ingestion (QLI) derives usage, popularity, queries/joins/filters; (3) human-guided ML (Lexicon) suggests business-friendly titles and glossary terms, confirmed by curators; (4) stewards add descriptions, custom metadata, domain documentation; (5) usage completes the flywheel ("the better it gets, the more it is used…").
- Each data object has a **catalog page**: descriptions, popularity, health, overall trustworthiness; users ask questions via Conversations.
- Search: keyword search; catalog "surfaces your company's most popular data assets"; ML interprets natural language (product page).
- Metadata taxonomy stated by vendor: technical (schemas/tables/columns), business (definitions, KPIs, glossaries), operational (usage, popularity, performance), social (ratings, comments, endorsements).
- Trust surface: lineage, tags, quality, trust flags, endorsements, comments; "trust check flags … display warnings about data issues visible to the analyst at the moment the data is being used."
- Roles (docs): Server Admin, Catalog Admin, Source Admin, Steward, Composer, Explorer, Viewer — roles map to license levels (Creator / Explorer / Viewer). Viewers are read-only (search/browse/conversations/stars); stewards create documents, edit fields, upload data dictionaries; admins install connectors, register sources, schedule extraction.
- Data sources are **Public** (visible to all users) or **Private** (explicit access only); Data Source Admins control settings/extraction/access.
- Governance App: Policy Center, Workflow Center, Stewardship Workbench, Governance Dashboard; Document Hubs (custom documentation types; built-in Glossary Hub); Critical Data Elements (CDE) Manager maps critical fields across systems; Data Quality App (completeness/validity/accuracy/freshness monitoring); Data Products App + Marketplace ("data assets (tables, files, APIs, streams) vs. data products (reusable, governed listings of data assets)").
- Compose: full SQL editor inside the catalog with suggestions toward trusted sources and away from deprecated ones; query forms, scheduling, snippets, history.
- Lineage: "compiled from data source metadata, query logs, Compose queries, and data posted over Alation's public APIs … visually represented as a diagram on the Lineage tab of a data source's catalog page"; can be created manually.
- Alation Analytics: usage information about the catalog itself (how users interact) to prioritize curation.
- Integration surfaces: Alation Anywhere (Slack, Teams, Tableau, Chrome extension); REST APIs; Open Connector Framework (120+ connectors incl. BI and file systems).

## Product B — Collibra

### Key observations

- Vendor definition (product-page FAQ): "A data catalog is a single place to discover and view information to understand your data. It automatically collects metadata from systems across your organization and organizes it with business context including definitions, owners, classifications, relationships and policies."
- FAQ on users (Tier 2, cross-checks role model): data stewards (metadata, definitions, classifications), data owners (domains, policy adherence), data engineers (schemas, dependencies, troubleshooting), data product managers, GRC teams, platform/architecture teams, security & privacy teams.
- Capabilities: 100+ native integrations connecting cloud platforms, databases, enterprise apps, BI tools, legacy systems; profiling statistics and samples; automated classification (incl. PII/PHI labeling); automated curation/description generation; "embedded semantic layer" connecting technical data to business concepts (glossary terms, policies); certification of trustworthy data; data products ("reusable assets packaged with relevant context, controls and access methods"); data contracts and sharing agreements; Data Marketplace for publishing/consumption; interactive lineage diagrams; AI Copilot ("find data and business term definitions … simply ask a question").
- FAQ distinguishes data catalog (metadata repository/management for owners and stewards) vs. data marketplace (consumer-facing find/assess/access layer).
- Governance-first framing throughout: catalog is positioned as part of a "Data Intelligence Platform"; trust signals ("Data Confidence") are the brand frame.

## Product C — Microsoft Purview (Data Map + Unified Catalog)

### Key observations

- Purview is a broad platform (data security + governance + compliance). The catalog-relevant components are the **Data Map** and the **Unified Catalog** under "Data governance."
- Data Map: "provides the foundation for data discovery and data governance. It captures metadata about data present in analytics, software-as-a-service (SaaS), and operational systems in hybrid, on-premises, and multicloud environments. The data map stays up to date with its built-in scanning and classification system."
- Data Map stores technical metadata (schema, data type, columns — discovered by scanning), business metadata (descriptions, glossary terms, manual tagging, metadata promoted from Power BI), semantic metadata (collection mappings, classifications), operational metadata (pipeline run statuses/times).
- Metadata operations enumerated by the vendor include: create an asset; add a relationship such as owner, steward, parent, lineage; edit an asset to add business metadata (description, glossary term); keyword search returning results. (Capacity-unit billing detail = vendor-specific; research notes only.)
- Unified Catalog: experiences for "data consumers, data stewards, and data owners." Organizing structures:
  - **Governance domains** — "a boundary that aligns your data estate to your organization. Think of it as a mini catalog inside Unified Catalog"; organize by business concepts (Marketing, Finance).
  - **Data products** — "a kit of data assets (tables, files, Power BI reports, and more) that provides assets with a use case for ease of discovery and understanding."
  - **Glossary terms** — business vocabulary attached to assets; in the new experience "active objects" that can carry policies.
  - **Critical data elements** — logical grouping of important fields mapped across tables (e.g., "Customer ID" mapping CustID and CID); quality rules and access policies attach to CDEs.
  - **Access policies / self-service access requests** — users request access "to all the data you need with a single request from inside Unified Catalog."
  - **Data quality** — rules set through domains/products/assets; quality scores at asset, data product, and domain levels.
  - **Health management** — health controls, health actions, scores; **OKRs** linking data products to business objectives.
- Discovery: "Search by governance domain, by data product, by keyword, or use the AI powered copilot to find what you need"; browse the catalog; inventory of "all your data assets, their metadata, and their lineage so you can understand the topography of your data estate."
- Audience framing: organization-wide data consumers (discovery, secure access, understanding), data owners/stewards (curation, responsible use, impact analysis), data officers/CxO (value creation, standardization).

## Product D — Atlan

### Key observations

- Positioning (docs): "the context layer for AI — the platform where metadata, semantics, lineage, and business knowledge come together so data teams and AI agents can find, understand, and act on data with confidence."
- "Atlan crawls metadata from the tools your team already uses — data warehouses, BI platforms, transformation tools, observability systems, and more. Metadata flows into Atlan automatically… Together, this connected metadata forms your **Enterprise Data Graph**."
- Discovery (structured search doc): search bar available everywhere (Cmd/Ctrl+K); search covers "tables, columns, databases, SQL queries, BI dashboards, and more."
  - Keyword matching over asset name (technical name + alias), description, linked glossary terms; glossary-term/description matches boost results; handles incomplete and misspelled queries.
  - Filters/facets: source (connector/connection), domains, **certificate** (Verified / Draft / Deprecated / No certificate), owners (users or groups), tags, terms, properties (technical name/alias, description, last updated).
  - Sorting: relevance, name, updated, star count, popularity (for supported sources).
  - Exact-match quoting; search by `database.schema.table` qualified name or GUID; result counts grouped by asset type; save/bookmark and share filtered search URLs.
  - Search-quality guidance: certify assets, link terms, enrich descriptions, star assets.
- Governance: tags for sensitive data, granular access control ("Purposes"), data contracts, playbooks automating metadata enrichment; domains as organizational structure.
- AI: conversational search ("ask a question"), MCP server exposing governed context to AI tools, Context Agents Studio for metadata enrichment agents.
- Certificates as trust states attached to assets (Verified/Draft/Deprecated) are a first-class filter and workflow.

## Product E — OpenMetadata

### Key observations

- Positioning: "Unified platform for data discovery, lineage, and governance… learn how to document, discover, and govern your data assets end-to-end."
- Discovery guide: "Discovering data among thousands of datasets is hard without rich metadata and faceted search. OpenMetadata with a single catalog aggregates metadata about all data assets, and presents the right information to users depending on their needs." Serves **data producers** (evolve data, prioritize bug fixes) and **data consumers** (timely decisions with the right data).
- Discovery strategies: keyword search, data associations (frequently joined tables, lineage), complex/advanced queries. Search spans "tables, topics, dashboards, pipelines, ML models, containers, glossaries, and tags"; detailed metadata for assets and components (columns, charts), including complex types (arrays, structs). "Data evolution tracked using lineage and metadata versioning."
- Guides: asset discovery, quick preview/glance, asset details, advanced search — the canonical user path is search → preview → details.
- Connectors across classes: Database (50+), Messaging (Kafka etc.), Dashboard (Looker, Tableau, Power BI…), Pipeline (Airflow, dbt…), ML Model (MLflow, SageMaker), Search (Elasticsearch), Storage (S3/GCS), Drive, and Metadata (other catalogs: Alation, Atlas, Amundsen as sources).
- 2.0 release structures: Explore page with **Browse Estate** panel + query bar + result cards; **Context Center** as "the single home for reference content in your catalog" (articles, documents, knowledge pills for MCP assistants); first-class **Tasks** (replacing suggestions/threads); custom intake forms for governance workflows; 3D Knowledge Graph for glossary exploration; profiler with dynamic sampling.
- Also ships: data quality/observability, data contracts, data insights (usage), governance, MCP server + AI SDK, REST APIs. Deployment: quick-start container to production K8s; OSS core with commercial distribution.

## Cross-product Comparison

| Dimension | Alation | Collibra | Microsoft Purview | Atlan | OpenMetadata | Strength |
|---|---|---|---|---|---|---|
| Inventory of entries standing for external data assets | A | A | A (Data Map) | A | A ("single catalog aggregates metadata about all data assets") | B — universal |
| Entries carry structural + descriptive metadata | A (schemas; descriptions; custom metadata) | A (profiles, definitions) | A (technical + business metadata enumerated) | A (name/alias, description, terms) | A (schema + columns; docs) | B — universal |
| Search + browse discovery surface | A | A | A ("search & browse", copilot) | A (structured search doc) | A (faceted search) | B — universal |
| Automated harvesting via connectors/crawlers | A (MDE, 120+ connectors) | A (100+ integrations) | A ("built-in scanning") | A (crawls; 80+ sources) | A (ingestion connectors) | B — universal in modern products |
| Usage/popularity signals | A (QLI, popularity ranking) | (not emphasized on fetched page) | A (operational metadata; run statuses) | A (popularity sort) | A (data insights; usage) | B — common, depth varies |
| Lineage | A (catalog-page lineage tab) | A (interactive diagrams) | A (asset relationships/lineage) | A (lineage capability) | A (lineage guide; versioned evolution) | B — common; treated as major capability everywhere, not uniform in depth |
| Business glossary / terms linked to assets | A (Glossary Hub; Lexicon) | A (semantic layer) | A (glossary terms; CDEs) | A (terms filter; linking) | A (glossaries searchable; Knowledge Graph) | B — universal |
| Trust/certification states on entries | A (trust flags, endorsements) | A (certification) | (implicit via curation/health) | A (Verified/Draft/Deprecated certificates) | (tasks/certification features) | B — common, naming varies |
| Ownership/stewardship (owners, stewards assigned to entries/domains) | A (roles; stewards) | A (owners, stewards) | A (owner/steward relationships; domains) | A (owner filter) | A (owner; teams) | B — universal |
| Domains / folders / business-area organization | A (Domains docs) | (implied via governance structures) | A (governance domains) | A (domains filter) | A (Browse Estate; domains) | B — common |
| Sensitive-data classification | A (PII/PHI/PCI framing) | A (automated classification) | A (classification system) | A (tag sensitive data) | (tags; PII via classification) | B — common |
| Quality signals surfaced on entries | A (Data Quality App) | A (DQ&O certification) | A (quality rules/scores) | (via observability sources) | A (profiler, quality tests) | B — common, depth varies |
| Request-access / self-service access | (private sources; not fetched in detail) | A (access methods in products) | A (self-service access requests + policies) | A (access control/Purposes) | (intake forms; API tokens) | B — common, mechanism varies |
| Catalog-internal SQL/query surface | A (Compose; query forms) | (via Marketplace querying) | (not on fetched pages) | A (visual query builder) | A (query features) | B — common-optional |
| AI assistance (descriptions, NL Q&A, copilots, MCP) | A (ALLIE, Agent Studio) | A (AI Copilot) | A (AI-powered copilot) | A (conversational AI, MCP, context agents) | A (AI SDK, MCP, knowledge pills) | B — universal in 2026 samples; recent-era |
| Data products / marketplace layer | A (Data Products App + Marketplace) | A (Data Marketplace) | A (data products; subscription) | A (data products capability) | (not on fetched pages) | B — emerging common layer |
| Programmatic APIs | A (REST APIs; APIs by role) | A (developer portal) | (Data Map ops; APIs implied) | A (API docs) | A (REST, SDKs, MCP) | B — universal |
| Roles/license tiers | A (7 roles, 3 licenses) | (persona FAQ only) | (consumer/steward/owner experiences) | (users/groups) | (teams/roles) | vendor-specific depth |
| Multi-source aggregation as deployment shape | A | A | A | A | A | B — universal in practice |

## Canonical Abstraction (for synthesis only — not for final doc)

### L0 — Defining Invariant (deliberately minimal)

1. **A metadata inventory of data assets that live in systems the catalog does not own** — entries (asset records) stand for tables, files, reports, topics, pipelines, models, etc. that exist outside the catalog; the catalog is a lens/description layer, not the store of the data.
2. **Per-entry descriptive content** — each entry carries at minimum structural metadata (what the asset looks like — e.g., its schema/columns or equivalent) plus explanatory context (what it means/contains — description-level human or machine context), so a user can evaluate the asset without opening the source.
3. **A search/browse discovery surface over the inventory** — users can find entries without knowing beforehand which system holds the data.

Drop (1) and the data itself is inside → warehouse/lake, not a catalog. Drop (2) → a bare name index, not a catalog. Drop (3) → a metadata repository/documentation store without discovery, drifting to Metadata Management Platform. An entry that merely lists names without structure or meaning does not let a user "understand before use," which is the catalog's reason to exist.

### Historical / market-sample check

- Pre-cloud, pre-crawler era: enterprise data dictionaries and metadata repositories (technical registries of tables/columns with descriptions, browsable/searchable) satisfy L0 with fully manual population. A curated wiki page or spreadsheet of tables with schemas and definitions satisfies L0.
- Therefore: automated crawling/connectors, cloud delivery, lineage graphs, glossary linking, classification, quality integration, popularity ranking, AI copilots, and data products are all **NOT definitional** — they are L1/L2. The historical check passes.
- Conversely, a warehouse's own schema browser fails L0's spirit (entries are native to the system, not referential across systems) and the market does not call it a data catalog — supports keeping the referential-inventory clause in L0.

### L1 — Common Mature Structure

- Automated metadata harvesting: connectors/crawlers over databases, warehouses, BI tools, pipelines, message systems, file stores; scheduled/incremental syncs keep the inventory current.
- Broad asset-type coverage: tables, columns, dashboards/reports/charts, pipelines/jobs, topics/streams, ML models, containers/files, plus glossary terms as first-class searchable objects.
- Usage/popularity signals (query logs, view counts) and behavioral ranking of results.
- Lineage graphs (asset- and often column-level; BI/pipeline lineage) with impact analysis.
- Business glossary/terms linked to assets; domains/folders/collections as organizing containers.
- Trust machinery: owners/stewards, certification states, trust flags/endorsements, comments/conversations on entries.
- Tags and sensitive-data classification (incl. PII-style detection) on entries.
- Quality signal integration (scores, tests, freshness, profiling statistics, sample data/preview).
- Ownership + stewardship workflows: assignment, suggestions/tasks, review queues, curation automation.
- Self-service access requests / permission-aware visibility of entries.
- Roles: consumer/reader, curator/steward, admin; role-scoped abilities.
- APIs/SDKs for programmatic metadata read/write; embedded surfaces in chat/BI tools; admin console for sources, schedules, users.
- AI assistance over the catalog (suggested descriptions, natural-language Q&A, copilots, agent/MCP exposure of governed context) — universal in the 2026 sample but recent-era; not definitional.

### L2 — Variant / Optional Structure

- Packaging: standalone catalog vs. governance-suite module vs. hyperscaler platform component vs. OSS self-hosted.
- Governance depth: light curation vs. full governance programs (domains, policies, OKRs, health scores, CDE management).
- Data products & marketplace layer (publish/consume governed bundles) — present in 3/5 sampled products as a distinct app.
- Data contracts (2/5 sampled explicitly; growing).
- Catalog-internal SQL query tooling.
- Deployment/tenancy: SaaS vs. self-hosted; private-network agents for on-prem sources.
- Audience poles: analyst-first discovery vs. steward-first governance.
- Consumption by AI agents as a primary client (2024–2026 positioning pole).

### L3 — Vendor-specific (research notes only)

- Alation: MDE/QLI/Lexicon terminology; the five-step population cycle framing; Compose; Alation Anywhere; Agent Studio; Creator/Explorer/Viewer license tiers; seven-role model; trust-check flags at point of use.
- Collibra: "Data Confidence" branding; "embedded semantic layer"; Data Marketplace; AI Copilot; data contracts/sharing agreements framing.
- Microsoft Purview: Data Map capacity-unit/ops-per-second billing model; governance domains + OKRs + health controls/actions framing; "Unified Catalog" naming; free vs. enterprise editions; regional rollout gating; Power BI metadata promotion.
- Atlan: "context layer for AI" / Enterprise Data Graph naming; Context Agents Studio; Context Engineering Studio; Purposes; Playbooks; star count as a social signal.
- OpenMetadata: JSON-schema-based metadata standard; Browse Estate/Context Center/3D Knowledge Graph naming (v2.0); ability to ingest other catalogs (Alation/Atlas/Amundsen) as metadata sources; Collate commercial distribution.

## Rejected Findings

Considered and rejected as definitional (with reasons):

- **Automated crawling/connectors** — manual data dictionaries satisfy the Type; rejected from L0 (→ L1).
- **Lineage** — valuable and common, but dedicated Lineage Platforms exist and older catalogs lacked it; a catalog without lineage remains a catalog (→ L1).
- **Business glossary** — catalogs without glossaries exist; glossary linking is standard but not defining (→ L1).
- **Usage/popularity ranking** — behavior-led pole (Alation) is one philosophy, not the Type (→ L1, depth varies).
- **Sensitive-data classification** — common; classification engines are also their own tooling (→ L1/L2).
- **Quality integration** — Data Quality Platforms exist separately; surfacing signals is common-optional (→ L1).
- **Access-request workflows** — depend on governance depth (→ L1/L2).
- **AI copilots / MCP / agent consumption** — 2023+; historical check excludes from definition (→ L1/L2 pole).
- **Data products/marketplace** — emerging packaging layer, present in most sampled suites but not universal and recent (→ L2).
- **Cloud delivery** — on-prem/self-hosted catalogs are first-class (→ L2).
- **Enterprise scale/multi-team governance programs** — small-team catalogs satisfy the Type (→ L2).

## Boundary Findings

- **vs. Metadata Management Platform** — the widest seam. Metadata management is the broader discipline/platform (collect, store, standardize, govern, publish metadata across its lifecycle; standards, APIs, interoperability). The catalog is the discovery-oriented, user-facing instantiation over that metadata. Suites collapse the two. Operational seam: if the primary object of work is the *asset inventory + its discovery/understanding surface*, it is a catalog; if the primary object is *metadata itself as governed enterprise content* (models, standards, exchange), it is metadata management. Recommend joint review when the Metadata Management Platform leaf is processed.
- **vs. Data Governance Platform** — governance organizes policy, stewardship organization, compliance workflows over the estate; the catalog supplies the inventory and discovery those processes act on. Governance-first suites (Collibra, Purview Unified Catalog) embed catalogs; standalone catalogs add governance features. Seam test: remove the discovery inventory → policy/attestation workflow tool (governance); remove policy workflows → pure catalog. Both leaves exist in DIRECTORY.md; overlap acknowledged, boundary held on the primary object of work.
- **vs. Data Lineage Platform** — lineage is one relationship structure inside a catalog; a dedicated lineage platform centers on capture/tracing/debugging of data flows at pipeline depth. A catalog without lineage is still a catalog; a lineage platform without a discovery inventory is not a catalog.
- **vs. Data Warehouse / Data Lake / Lakehouse Platform** — they hold the data; the catalog describes data across systems. A warehouse's built-in schema browser serves one system natively and is not a cross-silo catalog (though lakehouse platforms increasingly ship catalog-like features on top — a real convergence trend worth noting, not a merge).
- **vs. Enterprise Search / Internal Knowledge Search** — those index documents/knowledge content for member-facing Q&A/search; the catalog indexes structured data assets with schema-level metadata and technical provenance. (Consistent with the internal-knowledge-search pass: its corpus is docs/wikis/KB, not data assets.)
- **vs. Data Exchange Platform / Government Open Data Portal** — those publish/share datasets to external or cross-org consumers (the publishing/sharing act is primary); the catalog orients internal discovery and governance of the org's own estate. An open-data portal does contain a dataset catalog — adjacent surface, different primary job.
- **vs. Master Data Management** — MDM manages the master data records themselves (golden records); the catalog manages metadata about data assets. CDE features (mapping "Customer ID" across systems) sit at the seam.
- **vs. Database Management Console / SQL Client** — operate one engine; the catalog aggregates across engines and adds business context. Catalog-internal SQL tools (Compose etc.) are a convenience seam, not a merge.
- **"去掉什么就变成另一个 Type" tests**:
  - Hold the data itself instead of describing it → Data Warehouse/Lakehouse.
  - Keep the metadata store but remove search/browse discovery → Metadata Management Platform content store.
  - Remove per-entry descriptive context → bare asset index (falls toward generic search).
  - Center the product on policy/attestation workflows → Data Governance Platform.
  - Center on public/cross-org dataset sharing → Data Exchange / Open Data Portal.

## Uncertainties

- The exact edge between this leaf and Metadata Management Platform is genuinely soft in the market; flagged for joint review in STATUS.md.
- Data products/marketplace may be hardening into a distinct Application Type (3/5 sampled products ship it as a separate app); flagged.
- Collibra's operational documentation was not fetched; its deeper governance-machinery details (workflow specifics, certification mechanics) are asserted only at product-page strength.
- Alation's new help center was unreachable (JS-rendered); older docs site used — the five-step cycle and role model come from the customer-managed docs and may differ in minor detail from the current cloud experience.
- Access-request mechanics vary substantially across products (catalog-scoped vs. source-system-scoped grants); the final document deliberately stays conceptual here.
- OpenMetadata data-product/marketplace evidence was not on fetched pages; that cell is left unstated rather than guessed.

## Final Synthesis

A Data Catalog is an application that maintains a searchable, browsable inventory of an organization's data assets — entries standing for data that lives in other systems — where each entry carries the structural and descriptive context a person needs to judge what the data is, what it means, and whether it can be trusted, and where the inventory is kept current against its sources. Everything else that modern products pile on — crawlers, lineage, glossaries, domains, certification, classification, quality scores, popularity ranking, access requests, AI copilots, marketplaces — enriches the discovery-and-understanding loop but does not define it. The catalog's reason to exist is the moment before use: a person (or, increasingly, an agent) who does not know what data exists can find candidates, understand them, and establish enough trust to proceed.
