# Research Notes — Data Fabric Platform

Research date: 2026-09-07 · Directory leaf: §13 Data, Analytics & AI Systems · Slug: `data-fabric-platform`

## Research Goal

Understand what a "Data Fabric Platform" actually is as a marketed product category (not as an analyst architecture concept): what objects it manages, what users do with it, how work flows through it, where its boundaries lie against the many sibling data Types in the directory (Data Catalog, Data Integration, Data Virtualization, Lakehouse, Data Exchange, CDC, governance/metadata/quality/lineage leaves), and whether it is a genuine Type or only a marketing umbrella over an integration-suite bundle.

## Initial Boundary (hypothesis before research)

- Core use: an organization-wide layer that connects scattered enterprise data in place, unifies its metadata/meaning, and integrates + governs + serves it from one system.
- Users: data engineers, data stewards/governance staff, architects; consumers via self-service.
- Nearest neighbors: Data Catalog (describe-only), Data Integration Platform (pipelines), Data Virtualization Platform (one access technique), Data Governance / Metadata / Lineage / Quality / MDM (single-function layers), Data Warehouse / Lakehouse (owns the data), Data Exchange Platform (inter-org entitlement), CDC Platform (one movement mechanism).
- Known risk: "data fabric" is a heavily marketing-loaded term; some vendors describe an *architecture* rather than sell a product. The productized forms may be bundles. Also expected: naming collisions (Microsoft Fabric = unified analytics suite; NetApp "data fabric" = storage layer).

## Research Questions

1. What is the productized core — what structures exist in every "data fabric" product?
2. Do fabrics physically move data, serve it virtually, or both? Is the technique mix definitional or variant?
3. Is the fabric's own store (warehouse/lakehouse/cache) part of the definition?
4. How does governance attach — per system or through the shared metadata layer?
5. What does the user do day to day (engineer vs steward vs consumer)?
6. Where is the line to Data Catalog (describe-only) and to Data Integration Platform (pipeline-only)?
7. Is the Type separable from "data management suite" packaging?
8. Do older suite products (pre-"fabric" era) satisfy the definition without active metadata/AI?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| IBM (data fabric solutions: watsonx.data / watsonx.data integration / watsonx.data intelligence / watsonx.governance) | Enterprise portfolio realizing a fabric architecture | IBM is the loudest "data fabric" vendor and explicitly frames fabric as architecture + product portfolio; strong docs |
| Talend Data Fabric (now Qlik Talend) | The literal namesake bundle | A product actually sold under the name "Data Fabric"; its help center exposes the bundle's official structure |
| Denodo Platform | Virtualization-first "logical data management / AI data layer" | The zero-copy pole; markets itself as the fabric factory; strong public product docs |
| SAP Datasphere (in SAP Business Data Cloud) | Ecosystem-centric "business data fabric" | Fabric positioned around business semantics/context for one application ecosystem; includes its own warehousing |
| Informatica (IDMC — Intelligent Data Management Cloud) | Pure-play data-management suite with AI metadata engine | Frequently cited as the archetypal fabric-suite vendor; note: docs portal was inaccessible this pass |

Rejected / naming-collision samples (checked, deliberately not used as evidence of this Type):

- **Microsoft Fabric** — a unified SaaS analytics suite (lakehouse/warehouse/BI/notebooks under one SKU); center of gravity is owned compute + storage for analytics, not an overlay management layer over external systems of record. Belongs to the lakehouse/analytics-platform family. The name collision is noted in Boundary Findings.
- **NetApp "data fabric"** — storage-layer abstraction across on-prem/cloud storage; infrastructure/storage management domain (§14 territory), not a data-management layer over business data sources.

## Sources

Successfully fetched (2026-09-07):

- IBM, "What is a data fabric?" — https://www.ibm.com/think/topics/data-fabric (official explainer; quotes Forrester's six-component enterprise data fabric model)
- IBM, "Data fabric solutions" — https://www.ibm.com/data-fabric (official product page; "overlays existing systems"; product portfolio mapping)
- Qlik Talend Help Center — https://help.talend.com/ (official docs hub exposing the Talend Data Fabric bundle structure and the "Talend Data Fabric Getting Started Guide" entry)
- Denodo — https://www.denodo.com/en (homepage) and https://www.denodo.com/en/denodo-platform/denodo-platform (official platform page; four pillars and critical capabilities)
- SAP, "SAP Datasphere" — https://www.sap.com/products/data-cloud/datasphere.html (official product page incl. FAQ defining "business data fabric" and listing Datasphere capabilities)
- Informatica — https://www.informatica.com/ (official site; full product navigation of IDMC captured via the platform's 404 page shell; salesforce.com acquisition branding visible)

Failed fetches (recorded per source-access limitation rules; each abandoned after the allowed retries):

- Informatica docs portal — https://docs.informatica.com/ → HTTP 403 (blocked)
- SAP Help Portal — https://help.sap.com/docs/SAP_DATASPHERE → JavaScript-rendered shell, no content
- Talend "Data Fabric Getting Started Guide" deep link → HTTP 404 (bundle structure still obtained from the help hub)
- Denodo /en/platform and /en/data-fabric → 404 (recovered via /en and the platform page)

Evidence-strength consequences: Informatica and SAP observations rest on official product-site material (Tier 2), not hands-on operational docs → claims about those two are kept moderate; no precise operational facts asserted from them.

## Product Observations

### IBM — data fabric solutions / watsonx family (Evidence: A for IBM pages; B when generalized)

- IBM's own explainer: "It is **not a piece of software, but rather a design approach** that creates a unified view of data across an organization's on-premises and multicloud environments, from data lakes, data warehouses, SQL databases and other sources. With this approach, organizations don't have to move distributed data to a single location."
- Core capabilities named by IBM: data catalogs ("active metadata" — knowledge graphs, semantics, AI; organize assets in real time), data integration (batch, real-time, CDC), data governance and security (policies "easily and automatically linked to sensitive data through metadata"), self-service data access ("acts as a self-service marketplace for data consumption"), unified lifecycle (compose, build, test, deploy, optimize, monitor).
- Three foundational components named: data virtualization, federated active metadata (continuously analyze metadata, auto-tag/profile/classify, trigger alerts/actions on metadata changes), machine learning.
- Cites Forrester's six components of an enterprise data fabric: data management (governance/security/quality), data ingestion, data processing (transform/integrate/cleanse), data orchestration, data discovery (cataloging + metadata), data access (consumption + permissions).
- Product page: "A modern data fabric platform **overlays existing systems** … without requiring a full-platform rip-and-replace effort." Connects "using batch, streaming, CDC and virtualized pipelines." "Apply policies centrally … manage access and simplify audits across every ecosystem."
- Realizing products: watsonx.data (open hybrid lakehouse), watsonx.data integration (pipelines for batch/streaming/CDC), watsonx.data intelligence (AI-powered discovery, metadata management, automation), watsonx.governance, Guardium, Confluent. → A *portfolio* of cooperating products positioned as the fabric.
- Fabric-vs-lakehouse and fabric-vs-mesh contrast given: fabric manages access/integration/governance over platforms; lakehouse is a repository; mesh is decentralized-by-domain (fabric "automates key components of a data mesh such as creating data products and enforcing global governance").

### Talend Data Fabric (Qlik Talend) (Evidence: A for bundle structure from official help hub)

- The official help hub lists "Talend Data Fabric Getting Started Guide" as a first-class entry — the bundle is sold under the fabric name.
- Bundle structure visible in official docs navigation:
  - Data integration: Talend Studio (Jobs/Routes/components), Talend Cloud Pipeline Designer, Talend Change Data Capture, Data Mapper
  - Administration & execution: Talend Management Console, execution engines (Remote Engine, Dynamic Engine, engines Gen2), Administration Center (on-prem), SDLC best practices
  - Data quality and governance: Talend Data Inventory (catalog-like inventory), Talend Data Preparation (self-service prep), Talend Data Stewardship (stewardship tasks/campaigns), Talend Data Catalog
  - Application & API integration: Talend ESB, API Designer/Tester/Services, API Portal
- Interpretation: the namesake "fabric" = integration + execution + catalog/inventory + preparation + stewardship + quality + API services sold as one subscription. No virtualization engine, no own analytical store, no knowledge graph in evidence. → technique mix and semantic layer are NOT definitional; integrated operations + shared catalog/stewardship layer are.
- Now marketed as "Qlik Talend Cloud" under Qlik; product pages still expose "Talend Data Fabric" as a product.

### Denodo Platform (Evidence: A)

- Homepage: "Denodo connects, governs, and unifies your entire data estate in real time… Zero copy. Full governance. One layer." Positioned as "The AI Data Layer / Active Context."
- Four foundational pillars (official platform page): **Universal Connectivity** ("cloud platforms, lakehouses, operational systems, SaaS applications, APIs, streaming sources, and legacy environments… one consistent way to work with distributed operational and analytical data"); **Zero-Copy Delivery** ("access and combine data where it resides, reducing reliance on replication pipelines and centralized copies"; query optimization, pushdown, selective caching); **Governed Access** ("centralize governance… enforce fine-grained access controls as data is requested and consumed. Row-level security, masking, identity-aware policies, lineage, and auditability"); **Semantic Trust** ("unify business definitions, metrics, relationships, and metadata through a shared semantic layer and enterprise knowledge graph").
- Critical capabilities: real-time delivery, semantic unification, data self-service ("self-service data marketplace… access governed, trusted data without requiring IT"), federated data governance ("centralized policy management and fine-grained access control"), GenAI assistant, RAG/agent enablement, "Universal Connectivity and Data Services" (officially "200+ data sources"; consumption via SQL, REST, GraphQL and other standard APIs), "Flexible Data Integration" ("from real-time data federation to selective materialization (caching, aggregation-aware summaries), full replication (ETL, ELT, micro batching), and streaming").
- Interpretation: the virtualization pole of the Type. Denodo explicitly spans virtual→physical (its own materialization/replication/streaming) — i.e., virtualization is its *signature* but even it treats movement as an option inside one platform. "The Ultimate Data Fabric Factory" wording: builds "reusable, governed data products."

### SAP Datasphere / Business Data Cloud (Evidence: A for the product page; moderate strength)

- Positioning: "the knowledge core that unifies semantics, data products, and modeling to preserve business context across hybrid and multi-cloud environments" inside SAP Business Data Cloud.
- Key features (official): unified data integration "across every pattern — batch, streaming, replication, or data federation"; analytical and semantic modeling; knowledge graph "for connected context"; data product creation and sharing (incl. SAP-managed data products, Data Marketplace); "governed, self-service data access" via "secure, virtualized spaces… controlled ownership and data product sharing across domains"; "zero-copy data sharing across platforms."
- FAQ defines the architecture: "A business data fabric is an architecture that connects data, semantics, and business processes into a unified layer, enabling access to context-rich data across systems without duplication."
- FAQ lists Datasphere capabilities: "data integration, data cataloging, semantic modeling, data warehousing, data product management, discovery and activation, and virtualization."
- Interpretation: ecosystem-centric pole — the fabric's distinctive emphasis is *business context/semantics* for SAP estates; unlike Denodo it includes its own warehousing; unlike Talend it includes federation/virtualization and a knowledge graph. Note: includes an owned store → own-store is not disqualifying for the Type, but also not required (Talend lacks it).

### Informatica IDMC (Evidence: A-lite — official site navigation only; docs portal 403)

- Official product-site structure (captured): "Intelligent Data Management Cloud" as one platform with services: Data Catalog; Data Integration (Ingest, integrate, cleanse); API & App Integration; Data Quality & Observability; MDM & 360 Applications; Governance, Access & Privacy; Data Marketplace. Platform features: CLAIRE AI (AI engine), Headless, Cloud Connectors, Pricing.
- Branding now "Informatica from Salesforce" (acquisition).
- Interpretation: the pure-play suite pole — one cloud platform whose services correspond one-to-one to the sibling directory Types (catalog, integration, quality, MDM, governance), unified by a shared metadata/AI engine. Because operational docs were inaccessible, do not assert workflow details; keep at structure level.
- Vendor claims "Leader in 6 Gartner Magic Quadrants" (data quality, data & analytics governance, data integration, iPaaS, MDM, metadata management) — evidence that the suite population sits across many single-function categories at once.

## Cross-product Comparison

| Dimension | IBM | Talend Data Fabric | Denodo | SAP Datasphere | Informatica IDMC |
|---|---|---|---|---|---|
| Spans external heterogeneous sources in place | Yes (overlays existing systems; no rip-and-replace) | Yes (connectors/Studio/engines) | Yes (zero-copy; universal connectivity) | Yes (SAP + third-party; zero-copy sharing) | Yes (suite over "any data") |
| Unified metadata/semantic layer across the estate | Yes (federated active metadata, knowledge graph) | Partial — Data Inventory + Data Catalog (no semantic graph in evidence) | Yes (semantic layer + enterprise knowledge graph) | Yes (semantics, knowledge graph) | Yes (catalog + CLAIRE AI engine) |
| Executes data operations (not describe-only) | Yes (ingestion/processing/orchestration) | Yes (Jobs/Pipelines/CDC/prep) | Yes (federation, pushdown, caching, ETL/ELT, streaming) | Yes (all four patterns + modeling + warehousing) | Yes (integration/quality/MDM services) |
| Multiple integration styles in one system | Yes (batch, streaming, CDC, virtualized pipelines) | Yes (batch jobs, pipelines, CDC; no federation) | Yes (federation → caching → replication → streaming) | Yes (batch, streaming, replication, federation) | Yes (batch/app integration; depth unverified) |
| Governance applied through the shared layer | Yes (policies linked via metadata, applied centrally) | Yes (stewardship + catalog governance; depth per-module) | Yes (runtime, fine-grained, centralized policy) | Yes (governed spaces; data products) | Yes (governance/access/privacy service) |
| Own analytical store included | Lakehouse product adjacent (watsonx.data) | No | Cache/materialization only | Yes (data warehousing) | Not evidenced |
| Self-service consumption surface | Yes (self-service marketplace framing) | Yes (Data Inventory/Preparation) | Yes (data marketplace) | Yes (catalog, discovery & activation) | Yes (Data Marketplace) |
| AI/ML in the metadata layer | Yes (active metadata, ML automation) | Not evidenced at this pass | Yes (GenAI assistant, RAG/MCP enablement) | Yes (knowledge graph, AI context) | Yes (CLAIRE AI) |
| Data products concept | Yes (automating data-product creation) | Not branded | Yes ("data fabric factory"; products) | Yes (first-class) | Yes (marketplace-facing) |

Reading of the matrix:

- Universally present (5/5): span over external sources; unified metadata layer of some form; integrated execution of data operations; governance applied through the shared system; consumer-facing self-service surface. → L0 material (with the caveat that Talend's metadata layer is catalog/inventory-shaped, so "semantic layer/knowledge graph" specifically is common, not definitional).
- Present in most (4/5): multiple integration styles including at least two of {batch pipelines, CDC/replication, streaming, federation}; data products; AI assistance. → L1.
- Polarizing (2–3/5): virtualization/zero-copy as signature (Denodo, SAP), own analytical store (SAP, IBM-adjacent), API/ESB services (Talend), MDM services (Informatica). → L2.
- Vendor-specific: Denodo "Active Context / AI Data Layer / Lakehouse Accelerator"; IBM's Forrester six-layer framing and watsonx product naming; SAP "Business Data Fabric / Business Data Cloud / spaces"; Talend Studio/Management Console/Remote Engine machinery; Informatica CLAIRE, Headless; Salesforce acquisition branding. → L3, research notes only.

## Canonical Model (L0–L3 abstraction)

### L0 — Defining Invariant (deliberately minimal)

A Data Fabric Platform is an organization-wide data management layer that:

1. **spans many heterogeneous, distributed data sources it does not own** — it connects to the enterprise's existing systems of record (operational databases, warehouses, lakes, SaaS, files, streams, legacy) in place; the sources remain authoritative;
2. **maintains one unified metadata layer across that span** — a single system-level inventory of what data exists, where, with what meaning (catalog entries, business/semantic definitions, classifications; knowledge-graph or simpler realizations both satisfy);
3. **executes the core data operations through that one layer** — integrating/moving the data, governing it, and delivering it to consumers happen as coordinated functions of a single platform sharing the same metadata, not as unrelated tools.

Remove the span → a tool for one system. Remove the unified metadata layer → a bag of point tools (this is precisely what the fabric claim is against). Remove integrated operations → a Data Catalog (describes, does not operate). Remove governance → an integration suite without the fabric claim. 

Historical / market-sample check (structural, not observational — no pre-fabric-era vendor docs were fetched this pass): shared-metadata integration suites of the 2000s–2010s (hub-and-spoke ETL suites with a shared repository, glossary, profiling and quality modules) satisfy this L0 without virtualization, active metadata, AI, or cloud. The modern layer — active/AI metadata, virtualization, data products, marketplaces — is common mature structure, not definition. The definition therefore does not depend on the current AI-era marketing wave.

### L1 — Common Mature Structure

- connector libraries for heterogeneous sources; automated metadata harvesting/discovery
- catalog + search + business glossary; classifications/sensitivity tagging
- semantic layer / business definitions / knowledge graph of relationships
- multiple integration styles under one design surface (batch pipelines, CDC/replication, streaming, and/or federation/virtualization)
- data quality management; lineage; profiling
- policy-based access control (masking, row/column-level rules) enforced at access time
- self-service catalog/marketplace with access requests; data products
- delivery endpoints: SQL, REST/GraphQL APIs, BI connectivity
- roles: engineer (build), steward (curate/govern), admin (operate), consumer (find/use)
- lifecycle/operations: build → deploy → monitor pipelines and health; audit
- AI assistance over metadata (auto-tagging, recommendations, NL query)

### L2 — Variant / Optional Structure

- delivery-technique posture: zero-copy/virtualization-first (Denodo, SAP's federation) vs pipeline/physical-movement-first (Talend; IBM's integration products) vs hybrid
- own analytical store: none / cache-and-materialization only / full warehousing component (SAP) / adjacent lakehouse product (IBM)
- ecosystem scope: vendor-neutral overlay (IBM, Denodo, Informatica, Talend) vs application-ecosystem-centric (SAP)
- suite breadth: MDM/360 services, API/ESB services, data marketplace, streaming platform bundled in or not
- packaging: single integrated cloud platform vs bundled multi-product subscription vs cooperating portfolio; SaaS / hosted / self-hosted / hybrid; modular trials
- AI posture depth: metadata automation → NL assistants → RAG/agent-context delivery (MCP-style), including positioning labels of the current era ("logical data management", "business data fabric", "AI data layer")
- governance topology: centralized vs federated (domain ownership with central oversight)

### L3 — Vendor-specific (research notes only)

Denodo: "Active Context", "AI Data Layer", Lakehouse Accelerator (Presto-based embedded MPP engine), "200+ data sources" count, ROI percentages. IBM: Forrester six-component citation; watsonx.* naming; "not a piece of software" framing. SAP: Business Data Cloud, spaces, SAP-managed data products, Databricks partnership. Talend: Studio/Route/Job componentry, Management Console, Remote/Dynamic Engine, Stitch/Upsolver history. Informatica: CLAIRE AI, Headless, "6 Gartner MQs" claim, Salesforce ownership.

## Vendor-specific Findings

See L3 above. None of these may define the Type. In particular: Denodo's zero-copy posture must not become the definition (Talend lacks virtualization entirely; IBM sells both movement and virtualization); SAP's owned warehouse must not become the definition (Denodo/Talend lack it); "active metadata" AI must not become the definition (Talend's bundle and historical suites satisfy the Type without it).

## Boundary Findings

| Neighbor Type | Relationship | "Remove what → becomes the neighbor" / distinction |
|---|---|---|
| Data Catalog | sibling, describe-only | Catalog harvests and describes data in systems it does not own but performs no data operations; using an asset means leaving for the source. A fabric *describes and operates* (integrates, governs, serves). Remove the fabric's execution machinery → a catalog. Catalog face is one surface of a fabric. |
| Data Integration Platform | sibling, unprocessed leaf | Integration platform's center of gravity is building/running pipelines between endpoints; it makes no claim to be the organization-wide governed metadata layer and does not integrate catalog/governance/quality as one system. A fabric includes integration as one function inside the unified layer. Cross-check recommended when that leaf is processed (the data-exchange pass already requested it). |
| Data Virtualization Platform | sibling, unprocessed leaf | Virtualization is one access technique (logical views/query federation over sources). A fabric is a management layer that may include virtualization as one of several techniques. Denodo shows the virtualization pole hardening into a fabric posture by adding semantic layer + governance + marketplace + data products. Cross-check recommended at that leaf's pass. |
| Metadata / Lineage / Quality / Governance Platforms; MDM | single-function siblings | Each is one function of the fabric's shared layer, sold standalone. Their presence inside fabrics (Informatica services, IBM portfolio) does not merge the Types. |
| Data Warehouse / Lakehouse Platform | adjacent | They hold the data of record and compute over their own store. A fabric spans stores it does not own. Complication: fabrics may ship their own acceleration/landing store (SAP Datasphere warehousing; IBM's lakehouse product in the portfolio; Denodo caching) — common, not definitional. Fabrics increasingly sit *on top of* lakehouses (Denodo lakehouse optimization). |
| Data Exchange Platform | distinct (processed pass) | Exchange = inter-org entitlement + delivery of dataset offerings. Fabric = intra-org management layer. IBM/SAP fabrics expose sharing faces, but the fabric's defining population is internal estate management. |
| Change Data Capture Platform | distinct (processed pass) | CDC is one movement mechanism; fabrics list CDC among their connection styles (IBM). Mechanism leaf vs management-layer leaf. |
| Storage "data fabric" (e.g., NetApp) | different domain | Storage-layer abstraction across storage systems — infrastructure management (§14 territory), not a data-management layer over business data sources. Rejected sample. |
| Unified analytics suites ("Fabric"-named product) | naming collision | A lakehouse+BI+engineering SaaS suite centered on owned compute/storage is a Lakehouse/analytics-platform family member, not this Type, despite the name. Recorded as taxonomy note. |

Taxonomy risk (record honestly): "data fabric" is marketing-loaded; IBM explicitly calls it an architecture, not software. The productized category nonetheless exists and is independently marketed (a namesake product bundle; virtualization-first, ecosystem, and suite poles all present). The leaf stands as a Type, but its population overlaps the data-integration-suite population; the boundary with the unprocessed Data Integration Platform leaf must be cross-checked at that pass.

## Uncertainties

- Informatica: docs portal inaccessible (403); structure-level evidence only → workflow-level claims avoided.
- SAP: Help Portal (Tier-1 docs) not fetchable; capabilities taken from the official product page FAQ → moderate strength.
- Talend: deep "Data Fabric Getting Started Guide" unreachable (404); bundle composition from the official help hub navigation → module-level workflows not asserted.
- No hands-on operational documentation (job designers, policy engines) fetched for any sample; "How It Works" in the final document is written at the conceptual level supported by vendor-official material.
- Historical check is structural inference (pre-fabric-era suites), not direct observation; flagged in the research notes and kept out of the final document's claims.
- Whether the market will keep "data fabric" as the dominant label (vs "AI data layer" / "logical data management") is a positioning trend, not a structural question; noted only.

## Final Synthesis

The Data Fabric Platform Type is real but narrow at its core: an organization-wide management layer that (1) connects the enterprise's distributed data sources in place, (2) holds one unified metadata/semantic map of the whole estate, and (3) integrates, governs, and delivers that data as coordinated functions of a single system. Everything else that vendors put in the box — virtualization, pipelines, CDC, warehouses, knowledge graphs, marketplaces, data products, AI assistants, MDM, API services — is a selectable realization of one of those three functions, not part of the definition. The Type's sharpest boundaries: against the Data Catalog (describe-only), against the Data Integration Platform (pipelines without the estate-wide governed metadata layer — cross-check pending at that pass), against the Data Virtualization Platform (one technique among several), and against lakehouses/warehouses (which own the data the fabric spans).
