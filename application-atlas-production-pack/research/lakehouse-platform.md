# Research Notes — Lakehouse Platform

## Research Goal

Understand the Lakehouse Platform as an Application Type: what objects exist inside it, what users do with them, how data and work flow through it, what rules govern it, and — most critically this pass — where its boundary sits against the two neighboring data-platform Types that share its substrate (Data Lake Platform, Data Warehouse Platform) and the other §13 siblings that embed inside it (virtualization, catalog, feature store, workbench, ML platform, exchange, fabric).

This pass carries **discharge obligations** from four sibling passes:

1. **data-lake-platform (2026-09-07)**: three-way lake/warehouse/lakehouse seam flagged for joint review; suggested discriminator = "transactional tables as the product's centerpiece"; also asked whether a joint re-draw is needed since the same products claim both leaves.
2. **data-warehouse-platform (2026-09-07)**: ratifies the seam; recommends adopting "what is the store of record" as the discriminator and cross-referencing all three documents.
3. **data-virtualization-platform (2026-09-07)**: straddle recorded — Dremio is lakehouse-positioned but its views-over-external-sources + transparent-acceleration semantics are the virtualization core; "packaging-pole note, not a merge candidate".
4. **data-fabric-platform (2026-09-07)**: naming collision — Microsoft's Fabric product is a unified SaaS analytics suite (lakehouse/warehouse/BI over owned compute+storage) → belongs to the lakehouse/analytics-platform family, NOT the fabric Type.
5. **feature-store (2026-09-08)** + **data-science-workbench (2026-09-07)**: lakehouse platforms embed feature engineering and notebooks as modules; removal tests recorded both directions; cross-check expected from this side.

## Initial Boundary (hypothesis before research)

- A lakehouse is an analytical data platform that merges the data lake's open storage substrate with the warehouse's table semantics (ACID, schema, SQL performance) and serves one governed store to multiple workload classes (SQL analytics, data engineering, data science/ML).
- Closest neighbors: Data Lake Platform (same substrate, no transactional-table centerpiece), Data Warehouse Platform (same table semantics, closed-format store of record).
- Likely non-definitional: ML/AI tooling, notebooks, streaming, BI dashboards, semantic layers, agentic AI — all present in the flagship product but absent in other lakehouse-positioned products.
- Biggest risk: the category is young and marketing-saturated; vendors self-apply "lakehouse" loosely (query engines, catalogs, and suites all claim it). The Type must be anchored on documented product structure, not positioning labels.

## Research Questions

1. What is the lakehouse's **store of record** — where does the data of record physically live, and in what form?
2. What makes its tables "transactional"? What table-format machinery is common (snapshots, schema evolution, time travel, maintenance)?
3. What is the role of the **catalog**? Is it table-registration machinery, a governance layer, or both?
4. Is **multi-workload serving** (SQL + data engineering + ML) definitional, or a positioning claim?
5. Is **openness** (open formats, open catalogs, external engines) definitional or a positioning axis? Does the platform need to run on the customer's own storage?
6. What separates a lakehouse **platform** from a lakehouse **query engine** or lakehouse **catalog** (market uses all three labels)?
7. Where exactly do the lake, warehouse, and virtualization boundaries run — can the sibling-suggested discriminators be ratified with direct evidence?
8. What do users actually face: interfaces, daily loops, lifecycle of a table?
9. Historical check: does the structure hold for pre-term (pre-"lakehouse") products and non-cloud deployments?

## Representative Products

Selection logic: market representation + documentation completeness + genuinely different product philosophies + different positions on the lake/warehouse/lakehouse continuum.

| Product | Role in sample | Position |
|---|---|---|
| **Databricks** | the platform that formalized the category; full multi-workload suite | platform-native suite; Delta Lake substrate; customer cloud account |
| **Microsoft Fabric (lakehouse item)** | SaaS suite with lakehouse at its center; OneLake substrate | unified SaaS analytics platform; the data-fabric pass's excluded namesake, routed here |
| **Dremio** | query-engine lineage grown into an open lakehouse; no owned storage | open-standard pole (Iceberg/Polaris/Arrow); managed cloud + self-managed on-prem poles |
| **Snowflake** | warehouse platform adopting open-format tables | boundary-drift pole: warehouse store of record + Iceberg/Open Catalog interop surface |
| **Apache Iceberg (open standard)** | the substrate itself; not a product | evidence for the table-format/catalog contract shared across all products |

Also reviewed structurally (not fetched): AWS Lake Formation/S3 Tables family and Apache Hive — used by the sibling lake pass and for the historical check respectively; no vendor-specific claims made from memory.

## Sources

All fetched 2026-09-08, official documentation (Tier 1/2):

- Databricks documentation — "What is Databricks?" — https://docs.databricks.com/aws/en/introduction/index.html (Tier 1)
- Microsoft Learn — "What is a lakehouse? - Microsoft Fabric" — https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview (Tier 1)
- Dremio documentation — "What is Dremio?" — https://docs.dremio.com/current/what-is-dremio/ (Tier 1); Dremio docs home — https://docs.dremio.com/current/ (Tier 1)
- Dremio platform page — https://www.dremio.com/platform/ (Tier 2)
- Snowflake documentation — "Apache Iceberg™ tables" — https://docs.snowflake.com/en/user-guide/tables-iceberg (Tier 1)
- Apache Iceberg — "Terms" — https://iceberg.apache.org/terms/ (Tier 1, open standard)

Sibling research consulted (same production run): research/data-lake-platform.md, research/data-warehouse-platform.md, research/data-virtualization-platform.md, applications/data-lake-platform.md, applications/data-warehouse-platform.md, STATUS.md flags from data-fabric / data-exchange / feature-store / data-science-workbench passes.

> Source-access note: no fetch failures this pass; all five fetched sources returned full content. A first attempt at docs.dremio.com/current/concepts/lakehouse/ returned 404 and was immediately rerouted to the docs root + "What is Dremio?" page (no repeat retries). Cloudera was deliberately excluded (the lake pass already recorded it unreachable ×3).

## Product Observations

### Databricks (platform-native suite pole) — Evidence A

- Self-positioning: "a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions at scale"; "uses AI with the data lakehouse".
- Flagship use case: "Build an enterprise data lakehouse — combines enterprise data warehouses and data lakes"; "Data engineers, data scientists, analysts, and production systems can all use the data lakehouse as their **single source of truth**, providing access to consistent data" — multi-workload unity as the stated center.
- **Delta Lake** — open table format (open-source, originated by the vendor) as the table substrate; paired with **Spark** and **Structured Streaming** for processing.
- **Unity Catalog** — "a unified data governance model for the data lakehouse": ACL privileges via UI or SQL, admin/user division of responsibility; also hosts the **managed OpenSharing** protocol for sharing outside the environment ("sharing within your organization as simple as granting query access to a table or view").
- Workload surfaces: SQL warehouses (admin-configured compute for end-user SQL), SQL query editor, notebooks (SQL/Python/R/Scala with embedded visualizations), Lakeflow pipelines (declarative ETL "managing dependencies between datasets"), **Auto Loader** ("incrementally and idempotently loading data from cloud object storage and data lakes into the data lakehouse"), Jobs orchestration, git folders, bundles (CI/CD).
- ML/AI machinery: MLflow, ML runtime, LLM tooling, AI functions in SQL, AI/BI dashboards, metric views ("define business KPIs once… query them across any dimension"), Genie natural-language exploration — plus even an OLTP Postgres service (Lakebase) beyond the lakehouse proper.
- Integration posture: "integrates with cloud storage and security **in your cloud account**" — the storage substrate sits in the customer's cloud account.

### Microsoft Fabric lakehouse (SaaS suite pole) — Evidence A

- Definition: "A lakehouse in Fabric combines the scalability of a data lake with the querying capabilities of a warehouse. You store structured and unstructured data in a single location, manage it with **Delta Lake**, and analyze it with both **Apache Spark and SQL** — all without moving data between systems."
- Stated benefits: "One copy of data for both data engineering and analytics workloads; Delta Lake format for **ACID transactions, schema enforcement, and time travel**; Spark and SQL access; built-in integration with Power BI, pipelines, dataflows."
- **Lakehouse vs warehouse table** (the sharpest documented fork in any sampled doc): both share the same SQL engine and both store data in Delta on OneLake; lakehouse = Spark-first dev tool, structured + unstructured data, no multi-table transactions, "best for data engineering, data science, medallion architectures"; warehouse = T-SQL-first, structured only, multi-table transactions, "BI reporting, dimensional modeling". Both usable in the same workspace.
- **Tables/Files split**: lakehouse organizes data into a **Tables** folder (managed Delta tables) and **Files** folder (unstructured or non-Delta data). Placing a file in Tables triggers automatic validation (Delta only), metadata extraction, and **registration in the metastore** — "managed file-to-table experience".
- **SQL analytics endpoint** auto-generated at creation: read-only T-SQL over Delta tables; "Only Delta tables appear in the SQL analytics endpoint… Parquet, CSV, and other formats can't be queried through this endpoint. If you don't see your table, convert it to Delta format."
- **Shortcuts in OneLake**: "live, read-only references" to external sources without copying; cross-tenant data sharing supported.
- **Analyze data with** dropdown: SQL analytics endpoint / Eventhouse endpoint (KQL, real-time) / notebook — multiple engines over the same lakehouse item.
- Ingestion: notebooks, pipelines (copy activity), dataflows Gen 2 (low-code visual), Spark job definitions.

### Dremio (open-standard, no-owned-storage pole) — Evidence A

- Self-positioning: "Dremio's **open lakehouse platform**, based on community-driven standards like **Apache Iceberg and Apache Arrow**, enables organizations to use best-in-class processing engines and eliminates vendor lock-in" (docs, Tier 1). Platform page brands it "The Agentic Lakehouse Platform".
- Serving loop: "Data analysts can explore and visualize data with sub-second query response times, and **data engineers can ingest and transform data directly in the data lake with full support for DML operations**" — writes directly to lake tables; "analysts can join data in the lake with data in external databases, so they don't have to move data into object storage" (federation — virtualization semantics inside the lakehouse, matching the sibling straddle note).
- **Open Catalog (Apache Polaris)**: "Manages metadata for **Iceberg tables in the lakehouse**, including schemas, table definitions, and query metadata; enables unified governance and fine-grained access control across data assets."
- Query engine built on Apache Arrow; **Reflections** (autonomous acceleration: materialized summaries, transparent query rewrite) + background maintenance ("compaction, metadata cleanup, and other automated maintenance tasks").
- Sources are external object storage (docs list Amazon S3, Azure Storage under "Manage Sources") — Dremio owns **no store of record**; the Iceberg tables in object storage are the data of record.
- Deployment poles: Dremio Cloud (fully managed) / Dremio Enterprise ("Self managed software that runs on Kubernetes, on-premise, or in the cloud") / Community Edition — the self-managed, non-cloud realization of the Type.
- Ecosystem stance: co-created/maintains Apache Arrow, Iceberg ("the open table format for reliable and scalable lakehouse data"), Polaris ("open metadata catalog designed for modern lakehouse architectures").

### Snowflake (warehouse-side boundary-drift pole) — Evidence A

- Iceberg tables: "combine the performance and query semantics of typical Snowflake tables with **external cloud storage that you manage**. They are ideal for existing data lakes that you cannot, or choose not to, store in Snowflake."
- The open table format provides "**ACID transactions, schema evolution, hidden partitioning, table snapshots**"; Parquet data files.
- **External volume** (customer-managed cloud storage) holds data + metadata; "The external storage is not part of Snowflake" — the data of record can live outside the platform entirely.
- **Catalog options**: Snowflake as Iceberg catalog (Snowflake-managed tables, full platform support, lifecycle maintenance incl. compaction) OR external Iceberg catalogs via **catalog integration** (AWS Glue, Snowflake Open Catalog, Databricks Unity Catalog REST); **catalog-linked databases** auto-discover and stay in sync with remote catalogs ("preserving full interoperability with your existing Iceberg ecosystem").
- **Delta Direct**: create Iceberg tables over **Delta table files in object storage** — reading a rival format's tables in place.
- **External query engines through Snowflake Horizon Catalog**: external engines (e.g., Spark) can read Snowflake-managed Iceberg tables through the catalog's REST API with vended credentials and enforced policies (masking, row-access policies) — governed multi-engine access in the lakehouse sense, from the warehouse side.
- Native Snowflake tables remain internally-optimized (closed-format) — the Iceberg surface is a table *type* within the warehouse, not a replacement of the warehouse store of record. This is precisely the convergence the warehouse pass documented.

### Apache Iceberg (open standard) — Evidence A

- Catalog: "Tasks like creating, dropping, and renaming tables are the responsibility of a catalog… The most important responsibility of a catalog is tracking a table's **current metadata**… **Multiple types of compute engines using a shared Iceberg catalog allows them to share a common data layer.**"
- REST catalog: decouples engines from catalog implementations ("a single client to talk to any catalog backend") — the protocol that makes cross-platform multi-engine interop real (Snowflake↔Glue↔Open Catalog↔Unity Catalog).
- Snapshot: "the state of a table at some time" — versioned table states; snapshot log tracks how the current snapshot changed over time.
- The integration list of engines reading Iceberg (Spark, Flink, Trino, Presto, Athena, Redshift, BigQuery, Snowflake, ClickHouse, DuckDB, …) empirically documents the multi-engine market around one open table format.

## Cross-product Comparison

| Dimension | Databricks | Fabric lakehouse | Dremio | Snowflake (Iceberg surface) | Iceberg standard |
|---|---|---|---|---|---|
| Store of record | Delta tables, customer cloud account | Delta tables on OneLake (vendor-operated) | Iceberg tables in external object storage | Iceberg tables in external volume (customer-managed) or Snowflake-managed storage | open formats on external storage |
| Table semantics | ACID, schema enforcement, time travel (via Delta) | ACID, schema enforcement, time travel (Delta) | Iceberg table semantics | ACID, schema evolution, snapshots (spec) | snapshots, atomic metadata pointer, schema evolution |
| Catalog | Unity Catalog (governance + sharing) | metastore (auto-registration) + OneLake | Open Catalog (Polaris) | Snowflake catalog OR external REST catalogs; catalog-linked DBs | catalog = name→current metadata pointer, atomic update |
| Multi-engine | Spark + SQL + (ML) own engines; OpenSharing for external engines | Spark + T-SQL endpoint + KQL endpoint | own engine + external engines via REST catalog | own engine + external engines via Horizon REST catalog | any Iceberg-compatible engine |
| Multi-workload claim | "single source of truth" for engineers/scientists/analysts | "one copy of data" for engineering + analytics | analysts + data engineers (+ BI tools) | warehouse + lake interop (converging) | shared data layer across engines |
| Ingestion | Auto Loader, Lakeflow pipelines | pipelines, dataflows, notebooks, Spark jobs | ingest/transform "directly in the data lake" (DML) | COPY INTO / writes to Iceberg; catalog-linked sync | (out of scope) |
| Table maintenance | (platform-managed; not detailed in fetched pages) | (implicit via Delta) | autonomous: compaction, metadata cleanup | compaction (Snowflake-managed); customer-side for external | maintenance docs (branching, expiry) |
| Sharing | managed OpenSharing | shortcuts + cross-tenant sharing | catalog-level governance | direct sharing, listings, Native Apps | REST catalog vended credentials |
| Storage ownership | customer account | vendor-operated (OneLake) | external (S3/Azure) | external volume (customer) or Snowflake-managed | external |
| ML/AI machinery | MLflow, AI functions, dashboards, Genie | Spark ML (via notebooks), Power BI | AI Agent, semantic layer (no notebooks) | (not fetched; not claimed) | — |
| Deployment | managed SaaS over customer cloud | SaaS | managed cloud / self-managed K8s/on-prem / community | managed SaaS | standard, engine-neutral |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **Open-format transactional table store as the store of record.** The platform's data of record lives as tables carrying transactional semantics — ACID/snapshot-based consistency, schema enforcement/evolution, versioned states — implemented over **open file formats** (Delta/Iceberg-class: data files plus a metadata/snapshot layer) on scalable storage, typically object storage. Remove → the substrate degenerates to a data lake's schema-on-read files (no transactional centerpiece) or a warehouse's closed-format internal store.
2. **The catalog as the table layer of record.** A persistent catalog tracks the tables by name — table → current metadata/snapshot pointer with atomic updates — so users and engines address data as tables (query, insert, alter, time-travel), and the same tables are registered/discoverable across the platform and (in mature products) to external engines through open catalog protocols. Remove → files in storage with no table semantics; the catalog alone is a metadata service, not a platform.
3. **One governed store serving multiple workload classes.** The same cataloged tables are served — under one permission authority — to more than one workload class: SQL analytics for analysts/BI and data engineering/transformation as the constant pair, with data science/ML commonly added; the serving engines may be the platform's own (SQL warehouses, Spark runtimes, auto-generated SQL endpoints) or external engines connecting through open catalog/table protocols. Remove → a single-workload appliance: a query engine over tables, or a lake store, not a lakehouse platform.

Jointly-held is load-bearing:

- 1 alone = data lake platform (the sibling Type; the lake pass's "lakehouse upgrade path" line).
- 2 alone = an open table-format catalog service (Polaris/Glue-class infrastructure), not a platform.
- 3 without 1 = multi-engine access over raw schema-on-read files = data lake platform again.
- 1+2 without 3 = an open-format table store with one engine — the market realizes these as query engines/components (the lakehouse *engine* label), not lakehouse platforms.
- 2+3 without 1 = virtualization/federation territory (no owned transactional store).
- 1+3 without 2 = tables no one can address — incoherent as a product.

Evidence: all four sampled products document all three legs (A). The multi-workload leg is the *platform* claim — every sampled platform leads with unity language ("single source of truth", "one copy of data", "without moving data between systems") and documents at least two workload classes served from one cataloged store; the open standard encodes it as "multiple types of compute engines using a shared catalog share a common data layer".

### L1 — Common Mature Structure (present across the sample, not definitional)

- Ingestion machinery: incremental/idempotent loading from object storage (Auto Loader), declarative pipelines, copy activity, low-code dataflows (Databricks, Fabric; Dremio via DML; Snowflake via writes/sync).
- Platform compute layer: managed SQL warehouses / Spark clusters / auto-generated SQL analytics endpoints (Databricks, Fabric; Dremio engine; Snowflake warehouses).
- Table maintenance: compaction, orphan/metadata cleanup, snapshot expiry — autonomous in Dremio and Snowflake-managed tables; part of Delta/Iceberg lifecycle.
- Fine-grained governance: row/column-level controls, masking, tag policies (Unity Catalog ACLs, Polaris fine-grained access control, Horizon policy enforcement for external engines).
- Data sharing without copy: managed open sharing protocols (OpenSharing), live references/shortcuts, cross-tenant sharing, listings, REST-catalog vended credentials.
- Semantic layer / metric views; BI dashboard serving; discovery/search over the catalog.
- Time travel / snapshots as a user-facing table capability.
- Streaming ingestion and incremental processing.

### L2 — Variant / Optional

- Data-science/ML machinery (notebooks, experiment tracking, feature engineering, model serving, AI functions) — deep in Databricks/Fabric, absent from Dremio's core; the workbench/feature-store passes' removal tests confirm non-definitional.
- External-source federation (query external databases in place — Dremio's explicit strength; virtualization semantics inside the lakehouse).
- Event/real-time analytics endpoints (Fabric's KQL Eventhouse endpoint).
- OLTP components (Databricks Lakebase).
- Agentic-AI interfaces (natural-language exploration, MCP connectivity).
- Deployment posture: fully managed SaaS vs self-managed on Kubernetes/on-premises (Dremio Enterprise) vs open-source community editions; storage operated by vendor (OneLake) vs customer account (Databricks, Snowflake external volumes, Dremio sources).
- Data marketplace/monetization surfaces.
- Format breadth: single-format native (Delta for Databricks/Fabric; Iceberg for Dremio) vs multi-format interop (Snowflake Delta Direct; Iceberg REST catalogs spanning platforms).

### L3 — Vendor-specific (Research Notes only)

Unity Catalog; OneLake and shortcuts; Polaris Open Catalog; Delta Sharing/OpenSharing; Delta Direct; Horizon Catalog; Snowflake external volumes & catalog-linked databases; Auto Loader; Lakeflow; Reflections; Genie; AI/BI dashboards; Eventhouse; medallion architecture; Lakebase; Metric views; Dataflows Gen 2; Sap's acquisition of Dremio (context only).

### Rejected Findings (considered and rejected as definitional)

- **"Open-source/open-standards commitment"** — a positioning axis, not structure: Databricks and Dremio lead with it, Fabric does not, yet all satisfy the core. What is structural is the *open file format substrate* (leg 1), not the vendor's OSS posture.
- **"Customer-owned storage"** — rejected as definitional: Fabric operates OneLake (vendor-run) while Databricks/Snowflake/Dremio put files in customer-managed storage. The invariant is the open format + table semantics, not who owns the bucket.
- **"Schema-on-read raw layer always present"** — rejected: the lakehouse's centerpiece is tables; raw files remain an adjacent surface (Fabric's Files folder, Databricks' unmanaged paths) but the defining promise is the transactional table layer. (This is exactly the sibling discriminator, now ratified with direct evidence: Fabric documents that only Delta tables appear in the SQL endpoint; files must be converted.)
- **"AI-native/agentic"** — era-current marketing on every platform page; zero structural support (no sampled product requires it; Dremio/Fabric/Databricks ship it as L2 features).
- **"Unified governance across the whole enterprise"** — fabric-territory claim; lakehouse governance covers its own estate.

## Historical / Market-Sample Check (§24 reasoning, recorded here as required)

- **Term recency**: the category is young — the term was formalized by the Delta Lake–originating vendor around 2020–2021 (public research-paper lineage; not fetched this pass, recorded as context only). Any definition must therefore be checked against **pre-term structures**, not against the term's marketing.
- **Conceptual pre-term check** (structural inference — no legacy documentation fetched): the Hive-era analytical estate — distributed file system (open formats, e.g. ORC/Parquet) + shared metastore (name→table metadata) + table-level transactional support (Hive ACID, maturing through the 2010s) + multiple engines (Hive, Spark, Presto) reading the same tables — satisfies all three L0 legs at analog level, while lacking every L1 modern addition (managed cloud compute, autonomous maintenance, sharing protocols, semantic layers). The modern category's contribution is the *maturity* of the transactional table layer (snapshot-model table formats) and its productization, not a new structure. → The definition must not name cloud, object storage, snapshot-file layouts, specific formats (Delta/Iceberg/Hudi), or modern governance machinery.
- **Non-cloud realization check**: Dremio Enterprise self-managed on-premises/Kubernetes satisfies the core (A-documented deployment pole).
- **Era-stability conclusion**: the definition holds for the pre-term pattern, the self-managed pole, and the managed-cloud suite pole. Storage ownership, format choice (Delta vs Iceberg), and deployment model are all variant axes.

## Boundary Findings

**vs Data Warehouse Platform** (the sharpest seam; discharge of the three-way joint review):
- The warehouse's store of record is its own modeled, internally-optimized store; the lakehouse's store of record is open-format transactional tables on lake-style storage.
- Ratified discriminator (both sibling passes' suggestions confirmed with direct evidence): **what is the store of record** — and operationally, "are transactional open-format tables the product's centerpiece?"
- Direct evidence of convergence-from-both-sides: Snowflake (warehouse) documents Iceberg tables on external storage with REST-catalog interop and external-engine reads; Fabric documents warehouse and lakehouse sharing the *same* SQL engine and *same* Delta-on-OneLake substrate, differing on dev tool/data types/transaction scope — i.e., the two leaves converge to near-identity at the substrate level while remaining distinct at the workload-center level. **Keep-both ratified**: the discriminator is workload/substrate posture (warehouse = modeled analytical store + SQL platform as the center; lakehouse = open-format transactional tables + multi-workload platform as the center), not feature presence. Cross-references recorded both directions.
- Remove test: remove the open-format substrate (store everything in the platform's internal format) → warehouse. Remove the modeled-store center (make open tables the point) → lakehouse.

**vs Data Lake Platform** (discharge):
- The lake platform's store is raw, schema-on-read, original-fidelity; the transactional table layer is its documented "upgrade path" (the lake doc's own words), i.e., optional.
- Remove test: remove the transactional-table centerpiece → data lake platform. The lake pass's suggested discriminator ("transactional tables as the product's centerpiece") is adopted and confirmed: Fabric documents that only Delta tables are queryable through the SQL endpoint and that non-Delta files must be converted — the table layer is the point, files are the pre-table state.
- Databricks is confirmed as the boundary case (lake pass already used it that way): it retains the full lake substrate but self-identifies as a lakehouse. **No joint re-draw needed**: each product's self-positioning matches the discriminator (Databricks/Fabric → lakehouse; AWS Lake Formation-class → lake platform). The "same products claim both leaves" worry is resolved: the overlap product (Databricks) claims lakehouse and is documented by both passes as the boundary case.

**vs Data Virtualization Platform** (discharge):
- Virtualization owns no store of record and establishes no persistent copy; the lakehouse's defining leg 1 is precisely an owned store of record. Dremio's federation/views-over-external-sources are DV semantics shipped *inside* a lakehouse-positioned product — straddle recorded, matching the sibling note exactly; not a merge candidate.

**vs Data Catalog**: standalone catalogs describe estates they don't own; the lakehouse catalog is internal machinery over the platform's own tables (though mature lakehouse catalogs now *also* serve external engines — the service direction, not the description direction, distinguishes them).

**vs Machine Learning Platform / Data Science Workbench / Feature Store** (discharge of the feature-store and workbench flags):
- Notebooks, MLflow-class tracking, and feature engineering are modules inside the lakehouse; the model-lifecycle machinery is absent from one sampled lakehouse (Dremio) entirely. Removal tests hold both directions (strip ML machinery → lakehouse remains; strip the table store/catalog/serving → ML platform remains). The lakehouse hosts; it does not define itself by the model lifecycle.

**vs Data Exchange Platform** (discharge of the exchange pass's realization-pole note): sharing (open sharing protocols, shortcuts, listings) is a standard capability here and the delivery mechanism there; the entitlement-centered exchange Type remains distinct.

**vs Data Fabric Platform** (discharge of the naming-collision flag): Microsoft Fabric the *product* is routed to this leaf (lakehouse/analytics-platform family) as the fabric pass recorded; the fabric *Type* spans stores it does not own, while the lakehouse holds its own store of record. No directory change; cross-reference recorded.

**vs Business Intelligence Platform**: dashboards/metric views are served from lakehouse tables (Databricks AI/BI, Power BI on Fabric); the BI Type's center is governed analytics content for business consumers. Fabric bundles both — recorded as suite bundling, not boundary dissolution.

**vs OLAP / SQL query engines**: a SQL engine over lake tables (Trino-class) realizes only leg 1 (+ a catalog) — the market labels these lakehouse *engines*/query platforms, not lakehouse platforms; leg 3 (multi-workload platform) is what the "platform" in the leaf name carries.

## Uncertainties

- **Databricks table-maintenance and storage details** were not fetched this pass (intro page only); Dremio/Snowflake/Fabric document maintenance autonomously, so the L1 claim stands on 3/4 products — wording kept cross-product rather than universal.
- **Snowflake's non-Iceberg surfaces** (Snowpark, dynamic tables, native governance depth) not fetched; Snowflake is treated strictly as the boundary-drift pole and no claims are made about its warehouse-internal architecture beyond what the Iceberg page states.
- **Historical check is structural inference** (no legacy Hive-era documentation fetched); the pre-term pattern's fit is reasoned from the sibling lake pass's documented Hive substrate plus the open standard's own catalog/snapshot concepts.
- **BigQuery/AWS S3 Tables** were not sampled; the hyperscaler-native lakehouse services are covered only via the Iceberg standard's integration list (which documents their Iceberg surfaces) — noted as sample breadth limitation, not evidence.
- **Fabric multi-table transaction boundary** (lakehouse = no, warehouse = yes) is a single-product documentation detail (A, Fabric only); used as *illustrative* of the table-semantics gradient, not as a Type-wide rule.

## Final Synthesis

The Lakehouse Platform is real and distinct from both siblings, with a small era-stable core: **the store of record is open-format transactional tables; a catalog makes those tables the addressable, governed layer of record; one governed store serves multiple workload classes (SQL analytics + data engineering as the constant, data science/ML common)**. Everything else the vendors ship — managed compute, ingestion, autonomous maintenance, fine-grained policy, sharing protocols, semantic layers, notebooks, ML tooling, agentic interfaces, OLTP sidecars — is common mature structure or optional machinery around that core. The three-way lake/warehouse/lakehouse seam resolves on the store-of-record/centerpiece discriminator, ratified with direct evidence from both sides of the convergence; the embedded-module seams (workbench, feature store, ML platform, exchange, catalog, virtualization, fabric) all hold on removal tests, with the Dremio virtualization straddle and the Microsoft Fabric naming collision recorded as packaging/posture notes, not boundary dissolutions. The market is converging from both sides (warehouses adopting open tables; lakehouses adding warehouse-grade SQL), so the store-of-record discriminator — not feature presence — is what keeps the three Types separately describable.
