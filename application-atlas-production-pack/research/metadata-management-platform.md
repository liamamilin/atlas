# Research Notes — Metadata Management Platform

## Research Goal

Understand what a Metadata Management Platform actually is as an Application Type — not as a discipline buzzword. Four sibling leaves in §13 (data-catalog, data-governance-platform, data-lineage-platform, lakehouse-platform) were already processed and all four hung joint-review flags on this leaf, each holding the seam on "primary object of work" and predicting suite collapse. This pass must:

1. derive the defining core from real products, not from the sibling definitions;
2. discharge the four flags from this side;
3. verify the definition survives the historical check (the "metadata management" label is older than the modern data catalog; the definition must not be fitted to the 2020s catalog-style implementation).

## Initial Boundary

Hypothesis before research:

- Core use: an organization's data estate is scattered across warehouses, lakes, BI tools, pipelines, and SaaS; nobody can answer "what data do we have, what does it mean, where does it come from." A metadata management platform is the central system that collects, holds, models, and serves the *descriptions* of that estate.
- Users: data engineers, data stewards/governance teams, analysts/scientists, platform admins; increasingly machine consumers (APIs, AI agents).
- Nearest neighbors: Data Catalog (softest seam), Data Governance Platform, Data Lineage Platform, Data Quality Platform, Master Data Management, Data Fabric Platform, Lakehouse Platform (platform-native catalogs), Data Warehouse/Lake (hold the data itself), Enterprise Asset Registry (§10, different asset class).
- Known unknowns: is the metadata *model* (customizable metamodel) definitional or common? Is the human catalog UI definitional or one serving surface? Is machine-exchange (API-first serving) definitional? How old does the Type actually run?

## Research Questions

1. What are the core objects? (asset/metadata record, source connection, relationship, glossary term, tag/classification…)
2. Where does metadata come from — what collection machinery exists, and is it load-bearing?
3. What is the store of record — is the platform the authoritative holder of metadata, or just an index/cache?
4. How is metadata served out — to people (discovery UX) and to machines (APIs/interchange/notifications)?
5. What metadata *kinds* are held (technical / business / operational / semantic)?
6. What rules govern the record lifecycle — re-harvest vs human enrichment, identity resolution, permissions?
7. Where is the seam vs Data Catalog (the flagged softest seam), and do the sampled products support the sibling passes' "primary object of work" discriminator?
8. Would older / non-catalog-style realizations (frameworks, foundation layers, repositories) still satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Why sampled |
|---|---|---|
| Atlan | modern API-first "active metadata" SaaS; control-plane / context-layer positioning | strongest current-market formulation of the metadata-layer concept |
| Collibra | governance-first enterprise suite; operating-model/metamodel-centric | enterprise governance pole; operating model = explicit metamodel machinery |
| Microsoft Purview (Data Map + Unified Catalog) | hyperscaler suite; productizes the metadata store as a separately-billed foundation | cleanest evidence that the metadata layer is itself the product, distinct from the discovery surface |
| OpenMetadata | open-source, schema-driven unified metadata platform | OSS pole; connector catalog + metadata-to-metadata ingestion visible end-to-end |
| Apache Atlas | open-source framework (Hadoop era) | historical/structural counterweight: type system + hooks + common store + REST, thin UI — pre-modern-catalog shape |

Targeted but abandoned: Informatica (CDGC) — docs.informatica.com returned 403 and the product URL 404; abandoned after two attempts per the network rule; no Informatica-specific claims are made anywhere.

## Sources

Research date: 2026-09-08. All fetched live.

- Atlan — docs.atlan.com/get-started/what-is-atlan (official docs root page)
- OpenMetadata — docs.open-metadata.org/latest (official docs root; llms.txt index note)
- Microsoft Purview — learn.microsoft.com/en-us/purview/purview (suite overview); learn.microsoft.com/en-us/purview/data-map (Data Map concept article)
- Collibra — collibra.com/us/en/products/data-intelligence-platform (product page); productresources.collibra.com/docs/collibra/latest/Content/Home.htm (docs center); productresources.collibra.com/docs/collibra/latest/Content/Edge/co_edge.htm (About Edge)
- Apache Atlas — github.com/apache/atlas (official README); atlas.apache.org (site title only)

Access limitations recorded in Uncertainties.

---

## Product A — Atlan

(Evidence layer: A — official docs, directly observed)

### Key observations

- Positioning: "the context layer for AI — the platform where metadata, semantics, lineage, and business knowledge come together so data teams and AI agents can find, understand, and act on data."
- **Collection machinery is the first listed capability**: "Atlan crawls metadata from the tools your team already uses — data warehouses, BI platforms, transformation tools, observability systems, and more. Metadata flows into Atlan automatically, so your catalog stays current without manual upkeep."
- The accumulated result is named: "**Enterprise Data Graph**: a living graph of your data estate that the rest of Atlan, and your AI agents, build on." — the store is a graph over the estate; everything else builds on it.
- Human serving: "Search across all connected sources, filter by certification, owner, or lineage" — discovery-and-search is a capability on top of the graph, not the definition of the product.
- Governance machinery (tags, access control "purposes", data contracts, playbooks) — modules on the layer.
- **Machine serving is first-class**: "Expose governed, business-ready context to any AI tool via MCP"; API authentication reference in the get-started path ("Explore the API").
- Enrichment automation: playbooks and AI "automate metadata enrichment at scale."

Reading: a modern MMP = connected graph of harvested metadata + human discovery + governance modules + machine exchange. The catalog UX is one consumption surface among several.

## Product B — Collibra

(Evidence layer: A for Edge/docs-index pages; A/B for product page — marketing-flavored, used only for stack/foundation confirmation)

### Key observations

- Docs center (Tier 1) shows the structural inventory: "Understanding and working with **assets**" (asset pages), "**Out-of-the-box asset types**", "Start building your Collibra environment", "Collibra operating model", "Overview of Catalog connectors", "Create a technical lineage via Edge", Workflow Designer, Data Marketplace, Stewardship, Usage Analytics. The platform's unit of work is the typed **asset**; asset types are a managed configuration layer (OOTB types + operating model).
- **Edge (About Edge, Tier 1)** — the harvest layer in operational detail:
  - "Edge provides seamless native integrations and on-site data processing solutions that prioritize security and proximity to the data… Edge securely connects to your data sources either hosted in an on-premises or cloud environment. Edge capabilities process the data source information and send the results to Collibra."
  - "you create a connection to Databricks Unity Catalog and add a capability that allows you to **integrate the metadata** from Databricks Unity Catalog in Collibra."
  - "The results can be **assets, such as Schema or Table assets**, or extra information about the assets."
  - Site types (self-managed Kubernetes "Standard" vs vendor-managed "Collibra Cloud"), Edge CLI, global permissions (Manage Edge sites / Install Edge sites) — harvest is an operated, permissioned subsystem.
- Product page (Tier 2): stack = AI Command Center, Data Catalog, Data Privacy, Data Governance, Data Quality & Observability, Data Lineage, Data Marketplace. **Platform foundations include "Semantic graph": "Bridge raw data and business meaning to empower both people and AI with trusted context."**
- Integration/exchange: "100+ native integrations", "Collibra-supported integrations, partner-built integrations and **APIs**" (developer.collibra.com/rest); "Collibra Everywhere" browser extension surfaces "business context from Collibra within popular enterprise web applications and BI tools" — the layer is pushed out to where work happens.
- Self-hosted variant exists (Collibra Platform Self-Hosted docs publication).

Reading: enterprise pole. The metamodel (asset types, operating model) is explicit and configurable; harvest is an agent-based subsystem; the semantic graph is the foundation; catalog/governance/marketplace are applications on it.

## Product C — Microsoft Purview (Data Map + Unified Catalog)

(Evidence layer: A — Microsoft Learn conceptual articles)

### Key observations

- Suite overview: data governance solutions = "**Microsoft Purview Data Map**" + "Microsoft Purview Unified Catalog" — the metadata store and the discovery surface are *listed as two separate solutions*.
- **Data Map concept article is the cleanest definition-of-the-layer evidence found in the whole sample**:
  - "The Microsoft Purview Data Map **provides the foundation for data discovery and data governance**. It **captures metadata about data present in analytics, software-as-a-service (SaaS), and operational systems in hybrid, on-premises, and multicloud environments**. The data map **stays up to date with its built-in scanning and classification system**."
  - The store is billable on its own: capacity units = "metadata storage and operation throughput"; operations = "any Create, Read, Write, Update, and Delete operations on metadata stored in the Data Map," e.g. "Create an asset in Data Map", "**Add a relationship to an asset such as owner, steward, parent, lineage**, and so on", "Edit an asset to add business metadata such as description, glossary term", "Keyword search returning results".
  - Storage holds "technical, business, operational, and semantic metadata": technical = "schema, data type, columns" discovered by scanning; business = "automated metadata, such as metadata promoted from Microsoft Power BI datasets or descriptions from SQL tables, and **manual tagging of descriptions, glossary terms**"; semantic = "collection mapping to data sources or classifications"; operational = "data factory copy and data flow activity run statuses, and run times."
  - Sourcing nuance: some business metadata is itself harvested ("promoted from Power BI datasets", "descriptions from SQL tables") — the harvest/eñrichment distinction is explicit in one product.
- Unified Catalog = the human discovery/governance surface on top (not fetched in depth this pass; the data-catalog pass already covered Purview's catalog side).

Reading: Microsoft sells the metadata store itself as a foundation product with an operations model (CRUD + search over metadata records). This is the strongest market proof that "the metadata layer" is the Type's product, with discovery as a sibling application on it.

## Product D — OpenMetadata

(Evidence layer: A — official docs root)

### Key observations

- Self-description: "Unified platform for data discovery, lineage, and governance"; "Start with OpenMetadata and learn how to **document, discover, and govern your data assets** end-to-end."
- **Connector catalog is the dominant structural fact of the docs**: categories Database (50+ engines: Snowflake, BigQuery, Redshift, Databricks, Postgres, Oracle, SAP HANA…), Messaging (Kafka, Kinesis, Pub/Sub, Redpanda), Dashboard (Tableau, Power BI, Looker, Superset, Qlik, QuickSight…), Pipeline (Airflow, dbt Cloud, Airbyte, Fivetran, Dagster, NiFi, OpenLineage, Spline…), ML Model (MLflow, SageMaker), Search (Elasticsearch, OpenSearch), Storage (S3, GCS), Drive (SFTP, Google Drive), REST (API service).
- **Metadata-category connectors exist**: "Metadata: AlationSink, Atlas, Amundsen" — the platform ingests metadata *from other metadata platforms*. Metadata is treated as ingestable content from arbitrary sources, the defining mental model of the Type.
- Serving surfaces: Explore page ("Browse Estate"), search, lineage, quality/observability, insights, governance, data contracts, Context Center (reference content/knowledge pills), Tasks, 3D Knowledge Graph for glossary exploration.
- Machine serving: REST APIs; SDKs; "AI SDK — programmatic access to OpenMetadata through MCP tools across Python, TypeScript, Java, and CLI"; MCP server; real-time metadata ingestion (APIs vs Kafka, per its own blog index).
- Deployment: Docker quick-start, Kubernetes/cloud/bare-metal production — self-hosted OSS pole.

Reading: OSS pole. The entity model is schema-driven; the connector grid IS the harvest layer; serving spans UI + REST + SDK + MCP. A "metadata" source category makes the layer-on-layer structure explicit.

## Product E — Apache Atlas

(Evidence layer: A — official GitHub README + site title; docs site is an SPA and deeper pages 404'd, so claims are held to README strength)

### Key observations

- Self-description: "Apache Atlas — Open **Metadata Management** and Governance capabilities across the Hadoop platform and beyond"; site title: "Data Governance and Metadata framework for Hadoop." The Type's own name is used by an OSS framework — the label is not a 2020s marketing invention.
- "an **extensible set of core foundational governance services** — enabling enterprises to… meet their compliance requirements within Hadoop and allows integration with the whole enterprise data ecosystem."
- "**enables any metadata consumer to work inter-operably without discrete interfaces to each other — the metadata store is common.**" — the common store serving arbitrary consumers is stated as the framework's purpose.
- Capture machinery: build artifacts are hooks (hive-hook, kafka-hook, sqoop-hook, storm-hook, falcon-hook, impala-hook, couchbase-hook) — embedded capture from the systems where data lives, plus a graph repository (graphdb/, repository/ modules) and REST + notification (Kafka) interfaces.
- Security: "metadata veracity is maintained by leveraging Apache Ranger to prevent non-authorized access paths… Security is both role based (RBAC) and attribute based (ABAC)."
- UI: a dashboard module exists but is clearly secondary — no discovery-first UX in evidence.

Reading: the 2015–Hadoop-era structural pole: common metadata store + hooks (collection) + REST/notifications (exchange) + thin UI. Fits the Type with none of the modern catalog/AI machinery — the historical check passes against over-fitting to the catalog-style implementation.

---

## Cross-product Comparison

| Structure | Atlan | Collibra | Purview | OpenMetadata | Atlas |
|---|---|---|---|---|---|
| Central metadata store of record | Enterprise Data Graph ("living graph of your data estate") | semantic-graph foundation; typed asset store | Data Map: billable metadata storage, CRUD operations model | unified repository behind Explore/API | common metadata store (graph repository) |
| Collection machinery keeping it current | crawlers; "metadata flows in automatically, so your catalog stays current" | Edge sites → connections → capabilities → "assets, such as Schema or Table assets" | "built-in scanning and classification system" | connector grid across 9 source categories incl. metadata platforms | hooks embedded in ecosystem components |
| Human serving (discovery/understanding) | search + filters (certification, owner, lineage) | Data Catalog product; asset pages | Unified Catalog (separate solution) | Explore/Browse Estate, search | dashboard (thin; secondary) |
| Machine serving / exchange | APIs; MCP "expose governed context to any AI tool" | REST APIs + developer portal; 100+ integrations; browser extension pushes context into BI tools | operations throughput (CRUD + search) sold as capacity; consumed by catalog & other solutions | REST, SDKs, MCP, AI SDK, Kafka-class ingestion | REST + Kafka notifications; "any metadata consumer… inter-operably" |
| Metadata kinds held | metadata, semantics, lineage, business knowledge | technical + business assets per asset types | technical / business / semantic / operational (explicit) | schemas, dashboards, pipelines, ML models, glossary terms | technical + operational + business taxonomical metadata |
| Relationship structure | graph (lineage key capability) | asset relations per metamodel; technical lineage via Edge | relationships as operations (owner, steward, parent, lineage) | entity relations; lineage as first-class module | typed relations in the graph store |
| Typed metadata model | asset model | explicit operating model + OOTB asset types | system model + custom attributes (extent not fetched) | schema-driven entity model | extensible type system ("extensible set of core… services") |
| Governance modules on the layer | tags, purposes/access control, contracts, playbooks | governance/privacy/stewardship/workflows | classification + governance solutions above | governance, contracts, tasks | Ranger-backed RBAC/ABAC |
| Deployment poles | SaaS | SaaS + self-hosted | cloud (Azure service) | OSS self-hosted (Docker/K8s) | OSS self-hosted |

Reading of the table: every sampled product realizes the same triple — a central store of metadata records about data that lives elsewhere, collection machinery keeping it current, and a served layer consumed by humans and machines. The differences are packaging (which applications ship on the layer) and depth, not structure.

## Canonical Model (abstraction ladder)

### Level 0 — Defining Invariant

The smallest structure without which the product is no longer this Type:

1. **The central metadata store of record** — persistent, individually addressable records *about* the organization's data assets (what they are, what they mean, where they come from, how they relate), held in one repository the platform owns and operates. The platform describes data; it does not hold the data. Remove → there is no enterprise metadata layer at all (each tool keeps its own scattered descriptions).
2. **Source-bound collection keeping it current** — machinery that pulls/pushes metadata from the external systems where the data lives (connectors, scanners, on-site agents, embedded hooks, API ingestion), so records track their sources and the store stays synchronized. Remove → a static, hand-built register: a modeling/documentation tool, and the "management" is gone.
3. **The served metadata layer** — the content is put to use beyond the store: exposed to people for discovery and understanding (a catalog/search surface, native or in the sibling products the layer powers) and to machines (APIs, exports, interchange, notifications) so other tools and processes build on the same metadata. Remove → a private metadata database that nothing consumes.

Jointly load-bearing:

- 1+2 without 3 → a dark archive; collected metadata nothing can use.
- 1+3 without 2 → a hand-curated register that decays.
- 2+3 without 1 → a connector toolkit / transient index with no record of record.

Named-nothing check: the L0 names no UI style, no AI, no cloud, no glossary, no lineage depth, no governance program, no specific connector count. Atlas (hooks + common store + REST + thin dashboard) satisfies all three legs; so does Purview's store-only pole.

### Level 1 — Common Mature Structure

Present across the mature sample, expected in market, not definitional:

- typed metadata model: assets/entities with system types (tables, columns, schemas, dashboards, pipelines, ML models, glossary terms) and configurable extension (Collibra operating model/asset types; OpenMetadata schema; Atlas extensible types)
- cross-asset relationship structure, with **lineage as the flagship relationship** (a module or capability in every sampled product)
- business glossary / semantic layer (terms, definitions) as a first-class record class
- classification / tags / sensitivity labels (Purview's built-in classification; Atlan tags; Collibra classification)
- ownership & stewardship as record attributes (Purview: owner/steward relationship operations; Atlan filter by owner; Collibra stewardship)
- search-and-discovery experience (the catalog surface) as the primary human interface
- enrichment machinery: manual editing + automated promotion/playbooks (Purview: automated vs manual business metadata; Atlan playbooks + AI)
- usage/health overlays (Collibra Usage Analytics; OpenMetadata Insights) — common but visibly optional
- admin surface for connections/scan scheduling/permissions (Collibra Edge sites + global permissions; Purview scanning; OpenMetadata ingestion pipelines)

### Level 2 — Variant / Optional Structure

Depends on segment, deployment, packaging, era:

- the applications shipped on the layer: catalog-led vs governance-led suites vs store-only foundation products
- governance-program machinery (policy objects, workflows, certification, issue management) — governance-suite packaging, not the metadata core
- data quality / observability modules; data contracts; data products & marketplace surfaces (Collibra Data Marketplace/Data Products GA 2026; Atlan data products; evidence for OpenMetadata data products not on fetched pages — left unstated)
- AI machinery: copilots, context agents, MCP endpoints (all five sampled ship some; era machinery, not definitional)
- deployment: SaaS-only vs self-hosted vs on-site agent processing for data-residency (Collibra Edge standard vs Collibra Cloud; OpenMetadata/Atlas self-hosted)
- metamodel customization depth: fully configurable operating model vs fixed system model + custom attributes
- metadata-to-metadata ingestion (OpenMetadata's Atlas/Amundsen/AlationSink connectors) — a modern interop pole
- scope extension to AI assets (models/agents as governed records) — documented in sibling passes as scope variant

### Level 3 — Vendor-specific (Research Notes only)

- Collibra: Edge site types (Standard/Collibra Cloud), Edge CLI, "operating model" terminology, Data Citizens branding, Control Tower, IDC-based ROI claims
- Microsoft Purview: capacity-unit billing (25 ops/sec + 10 GB per CU; quota escalation via support ticket), Azure portal metrics, DSPM/Compliance suite adjacency
- Atlan: playbooks, Purposes, Context Agents Studio / Context Engineering Studio, customer-named stats (FOX, Unilever)
- OpenMetadata: Context Center/knowledge pills, Tasks, 3D Knowledge Graph view, release-versioned breaking changes
- Atlas: Hadoop hooks inventory, Ranger integration, Kafka notifications

## Vendor-specific Findings

See Level 3. None promoted to the canonical model. The only near-miss was Collibra's explicit "operating model" (metamodel-as-product): attractive as an L0 candidate, but Purview/OpenMetadata/Atlan do not center a configurable metamodel the same way, so it stays L1/L2.

## Rejected Findings

- "A metadata management platform = a data catalog" — rejected as a Type merge: suites collapse them, but the store-and-exchange layer is realizable without any discovery UX (Atlas dashboard; Purview Data Map as a separately-billed store), and the catalog's identity (asset inventory + discovery loop) does not require an exchange layer.
- "Machine-serving (API-first) is the defining difference from a catalog" — rejected as the *single* discriminator: too clean, and catalogs also expose APIs. Held instead on primary object of work (see Boundary Findings); machine-exchange remains part of the served-layer leg without being the seam itself.
- "Customizable metamodel is definitional" — rejected: fixed-model products are still recognizably this Type (Purview's system model; Atlan's fixed asset model).
- "The platform must hold business glossary/semantics" as definitional — rejected; glossary is a record class that most products carry (L1), but a technical-metadata-only store (Atlas-style) is still the Type.
- Precise connector counts, billing numbers, capacity-unit tables — kept in Research Notes (L3/billing), not in the canonical document.

## Boundary Findings

- **vs. Data Catalog (§13 sibling; the flagged softest seam — joint review DISCHARGED from this side)** — the market collapses the two into suites, but the primary object of work still separates them, as the catalog pass held: the catalog's product identity is the *asset inventory + its discovery/understanding loop* (a person finds and trusts data); the MMP's product identity is the *metadata layer itself* — the store, its collection machinery, and its exchange — of which discovery is one consumption surface. Evidence for a layer-without-discovery-shape: Atlas (thin dashboard), Purview Data Map (separately-billed store whose human surface is the sibling Unified Catalog product), OpenMetadata's server/API-first architecture. Evidence for catalog-as-one-surface: every suite brands catalog as one application on the platform (Collibra stack list). Removal tests hold both directions: strip the discovery experience → still an MMP content store; strip the collection+store and keep only per-asset discovery pages served from elsewhere → not this Type. Boundary held; both leaves stand; cross-references recorded in the final document.
- **vs. Data Governance Platform (flag DISCHARGED from this side)** — governance centers rules/accountability/processes over the estate (policy objects, stewardship workflows, certification); the MMP centers the metadata content and its lifecycle. Governance machinery rides on the metadata layer (tags, policies-as-records, stewards-as-attributes); MMPs ship governance modules without making the governance program the primary object. Consistent with the governance pass's own framing; keep-both.
- **vs. Data Lineage Platform (flag DISCHARGED from this side)** — lineage is the flagship relationship structure *inside* the metadata content; a dedicated lineage platform centers capture/tracing/impact operations on the flow graph at pipeline depth. In-suite, lineage renders as a view on the metadata graph. Consistent with the lineage pass's "expect suite collapse" note.
- **vs. Lakehouse Platform (flag DISCHARGED from this side)** — lakehouse-native catalogs are internal-machinery-first (serving their own engines' tables) and have extended outward to external engines (the lakehouse pass's own observation). The MMP is external-first by design: its store exists to describe a *cross-system* estate it does not operate. Suite collapse expected where lakehouse vendors sell estate-wide governance; the leaves stand on the primary object.
- **vs. Data Quality Platform / Data Observability Platform** — quality/health machinery (tests, monitors, incidents) is a module riding on the layer; the MMP holds descriptive records and health *metadata* (Purview's operational metadata: run statuses) without centering test/monitor execution.
- **vs. Master Data Management** — MDM manages the master *data* records themselves (golden customer/product records); the MMP manages metadata *about* data assets. Critical-data-element mapping machinery sits at the seam (consistent with catalog and governance passes).
- **vs. Data Fabric Platform** — the fabric pass defined fabric as an estate-spanning unified metadata layer *with integration, governance, and delivery as functions of one system* (it actively moves/serves data). The MMP stops at describing: it never holds or moves the data. A fabric includes an MMP-shaped layer; an MMP is not a fabric.
- **vs. Data Warehouse / Data Lake** — they hold the data; the MMP describes data across systems. A warehouse's schema browser serves one engine; the MMP's store exists because the estate spans many.
- **vs. Enterprise Asset Registry / IT Asset Management (§10/§14)** — those hold records about IT assets (hardware, software, licenses) with financial/lifecycle semantics; the MMP's record class is data-and-analytics assets with technical/business semantics. Different asset class, different consumers. (Conceptual distinction; not deep-researched this pass.)
- **vs. Data Exchange Platform** — exchange centers the publishing/sharing act toward consumers (the data moves outward); the MMP centers the descriptive record layer. A marketplace surface on top of an MMP can drift toward the exchange/catalog-family surface — a capability seam, not a merge.
- **"去掉什么就变成另一个 Type" tests**:
  - Hold the data instead of describing it → Warehouse/Lake/Lakehouse.
  - Remove the central store, keep connectors → connector toolkit / integration platform machinery.
  - Remove collection, keep the store → static hand-built register (modeling/documentation tool).
  - Remove the served layer entirely → private metadata database (not a product).
  - Keep the layer but center the *discovery loop* as the product → Data Catalog.
  - Center policy/stewardship/certification processes → Data Governance Platform.
  - Center the flow graph + trace operations → Data Lineage Platform.
  - Move/serve the data itself through the layer → Data Fabric territory.

## Market-structure observation

The sampled market realizes the Type as: (a) API-first active-metadata platforms (Atlan, OpenMetadata), (b) governance-first suites whose foundation is a semantic graph/metadata store (Collibra), (c) hyperscaler suites that productize the store as a billable foundation (Purview Data Map), (d) OSS frameworks (Atlas). All four shapes ship the same triple. The layer-without-discovery shape persists commercially (Purview bills the store separately), which supports holding catalog and metadata-management as distinct leaves even under suite collapse.

## Historical / Market-Sample Check (§24 discipline)

- Atlas (Hadoop era, OSS, framework-shaped, thin UI) satisfies all three L0 legs — the definition does not depend on the modern catalog-style implementation, AI, or cloud.
- The Type's own label predates the current sample: Atlas's README (2015-era project, actively maintained) self-describes as "Metadata Management"; the enterprise-metadata-repository category the Type grew out of is older still (context-level inference from the discipline's standards/repo lineage; no specific legacy-vendor claims asserted — those vendors were not fetched this pass).
- Older regional/platform-native realizations: platform-native catalogs (lakehouse engines) realize the same triple internally (store + collection + serving for their own estate) — they fit the structure but center their own platform, which is why the lakehouse seam was held on primary object.
- Definition names no software surface, no cloud, no AI, no connector count, no glossary, no specific metadata-kinds taxonomy beyond "about data assets."

## Uncertainties

- Informatica CDGC unreachable (docs 403, product page 404 after 2 attempts) — the classic enterprise-suite pole rests on Collibra/Purview evidence only; no Informatica claims made.
- Atlas deeper docs (Type System pages) 404'd behind its SPA; Atlas observations held to README/site-title strength — no specific type-system internals asserted.
- OpenMetadata's dedicated "what is" page 404'd; observations come from the docs root (still Tier 1) — fine at the strength used.
- Purview Unified Catalog not fetched this pass (covered by the data-catalog pass); this pass leans on Data Map + suite overview, which is exactly the layer-side evidence needed.
- Collibra's operating-model internals (metamodel object details) came from the docs *index* and product page, not the operating-model article itself; assertions about Collibra held accordingly (asset types/operating model exist and are configurable = index-level evidence).
- Whether the data-products/marketplace layer hardens into a distinct leaf — watch-flag reaffirmed from this side (Collibra Data Marketplace + Data Products application shipping as separate apps, 2026; Atlan data products a listed capability); not resolved here.
- The exact strength of "machine exchange" as a seam criterion vs catalogs (catalogs also have APIs) — held as part of the served-layer leg, not as the seam itself; the seam stays on primary object of work.

## Final Synthesis

A Metadata Management Platform is the system of record for an organization's metadata. Its defining structure is a triple: a central store of metadata records about data assets that live elsewhere (the platform describes, never holds, the data); collection machinery bound to those sources that keeps the store current (connectors, scanners, on-site agents, hooks, API ingestion); and a served layer that puts the content to use — to people through discovery and understanding surfaces, and to machines through APIs, interchange, and notifications, so that catalogs, governance programs, quality tooling, and now AI agents all build on the same metadata. The typed metadata model, relationships (lineage above all), glossaries, classification, ownership, and search are the mature-market furniture on this triple; governance programs, quality machinery, data products, and marketplaces are applications that ship on top. The Type is old enough to predate its current catalog-shaped packaging — a framework with hooks and a common store satisfies it as fully as a SaaS suite — and the seam against the Data Catalog leaf holds on the primary object of work: the catalog is the discovery-facing instantiation of the metadata layer; the metadata management platform is the layer itself.
