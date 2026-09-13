# Research Notes — Data Lake Platform

Research date: 2026-09-07
Methodology: WORKFLOW v1.1 (10-step) + WRITING_GUIDE v1.1 (§22 abstraction hierarchy, §23 evidence rules, §24 historical check)

## Research Goal

Understand what a **Data Lake Platform** actually is as an Application Type: what structures define it, what the "platform" layer adds over raw storage, how the stored data is organized, governed, and served, and where the boundaries lie against Data Warehouse Platform, Lakehouse Platform, object storage, Data Integration Platform, and Data Catalog.

## Initial Boundary (pre-research hypothesis)

- Core use: a centralized, scalable store for an organization's analytical data in open/native formats (schema-on-read), plus a management layer (organization, governance, multi-engine access) over that store.
- Users: data engineers, data platform teams, analysts (consumption side), governance/security teams.
- Nearest neighbors: Data Warehouse Platform (schema-on-write, compute-coupled), Lakehouse Platform (transactional tables + warehouse-grade management on the lake), Object Storage (no management layer), Data Integration Platform (moves data, does not hold it), Data Catalog (describes data, does not hold it), Data Virtualization (no physical copy).
- Unknowns going in: is governance definitional or merely common? Is multi-engine serving definitional? What exactly separates "data lake" from "lakehouse" in product terms?

## Research Questions

1. What is a "data lake" as opposed to a data warehouse? (formats, schema timing, storage economics)
2. What does the *platform* add over raw storage? (catalog, governance, ingestion, serving)
3. How is the stored data organized? (containers, zones, databases/tables over files, namespaces)
4. How is access governed? (permission models, granularity, enforcement point)
5. Which engines read/write the lake, and through what mechanism?
6. What role does the metadata catalog/metastore play?
7. What ingestion/lifecycle machinery exists?
8. Where is the lake→lakehouse boundary in product terms?
9. What sharing/external-distribution machinery exists?
10. Do older / non-cloud / platform-native lakes satisfy the same core? (historical check)

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / tier | Role in sample |
|---|---|---|
| AWS Lake Formation | hyperscaler managed governance service over S3 + Glue Data Catalog | governance-first realization; the clearest "platform over a lake" |
| Azure Data Lake Storage (+ Synapse Analytics) | storage-service-first lake + multi-engine analytics service on top | store-first realization; ADLS defines the lake store, Synapse shows multi-engine serving |
| Databricks | platform-native lakehouse (Delta on cloud object storage + Unity Catalog) | boundary case: the lake platform that upgraded itself into a lakehouse |
| Apache Hive / Hive Metastore | open-source historical substrate (Hadoop era) | historical baseline for the historical/market-sample check |

Rejected / not selected:
- Cloudera Data Platform — docs.cloudera.com returned 404 on three attempted paths (public-cloud overview, private-cloud overview, SDX product page); abandoned per the source-access rule. Enterprise hybrid-lake realizations are therefore under-evidenced in this pass.
- Google BigLake — cloud.google.com/biglake timed out twice; abandoned. Multi-cloud governance-layer realizations under-evidenced.
- Snowflake, Starburst, Dremio — warehouse/lakehouse query positioning, not lake platforms; would be Product Mismatch for this leaf.
- MinIO etc. — object storage only, no platform layer.

## Sources

Evidence layer A (directly observed, official docs fetched 2026-09-07):

- AWS Lake Formation — "What is AWS Lake Formation?", "How it works", "Terminology" — https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html , https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html , https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works-terminology.html
- Databricks — "What is Databricks?", "What is Unity Catalog?" — https://docs.databricks.com/aws/en/introduction/index.html , https://docs.databricks.com/aws/en/data-governance/unity-catalog/index.html
- Microsoft — "Azure Data Lake Storage overview" — https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
- Microsoft — "What is Azure Synapse Analytics?" — https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is
- Apache Hive — project home (HMS positioning, Ranger/Atlas, multi-engine clients) — https://hive.apache.org/

Source-access limitations:
- Cloudera (docs.cloudera.com, www.cloudera.com): 404 on all attempted paths — abandoned. No Cloudera-specific claims are made anywhere.
- Google BigLake (cloud.google.com/biglake): timeout ×2 — abandoned. No BigLake-specific claims are made anywhere.
- Consequence: enterprise/hybrid on-prem lake platforms and multi-cloud governance layers are covered only indirectly (via the Hive ecosystem, which historically underpins them). All such claims are kept at weak/qualified strength.

## Product Observations

### AWS Lake Formation (evidence layer A)

- Definition of the managed object: "The *data lake* is your persistent data that is stored in Amazon S3 and managed by Lake Formation using a Data Catalog." A data lake "typically stores: structured and unstructured data; raw data and transformed data." An S3 path is in the data lake only if *registered* with Lake Formation.
- Positioning: "centrally govern, secure, and globally share data for analytics and machine learning"; "break down data silos and combine different types of structured and unstructured data into a centralized repository."
- **Data Catalog**: "your persistent metadata store… in the same way you would in an Apache Hive metastore… Metadata about data sources and targets is in the form of databases and tables. Tables store schema information, location information… Databases are collections of tables." One catalog per account per region.
- **Permissions**: "a relational database management system (RDBMS) permissions model to grant or revoke access to Data Catalog resources such as databases, tables, and columns with underlying data in Amazon S3"; replaces "complex Amazon S3 bucket policies and corresponding IAM policies". Fine-grained controls "at the column, row, and cell-levels". Two enforcement levels: metadata-level permissions on catalog resources + storage access permissions on the underlying S3 data "on behalf of integrated engines".
- **Multi-engine serving**: integrated analytical engines — Amazon Athena, AWS Glue, Amazon EMR, Amazon Redshift Spectrum — query the lake through the catalog + permission check + "credential vending" (Lake Formation grants the engine temporary access; the engine fetches from S3 and applies column/row/cell filtering). External engines can connect via the Apache Iceberg REST catalog specification.
- **Ingestion**: "blueprints" (templates per source type) generate "workflows" of AWS Glue crawlers, jobs, and triggers; run on demand or schedule; status tracked as a single entity. Bulk and incremental loading from relational databases (JDBC import).
- **Governance scale machinery**: LF-Tags (tag-based access control) to "manage hundreds or even thousands of data permissions"; ABAC via tags; hybrid access mode for incremental onboarding of LF permissions; cross-account sharing; audit logging via CloudTrail ("which users or roles have attempted to access what data, with which services, and when").
- **Roles**: "data lake administrator" — can grant any principal any permission on any catalog resource or data location; designated explicitly (IAM admins are NOT automatically lake admins).
- **Federation/catalog extension**: federated catalogs over Redshift and external sources without migrating data or metadata; S3 Tables (Iceberg) integration; connection to external metastores; licensing data through AWS Data Exchange.
- Notable: Lake Formation itself does not store the data — S3 does. The product is the management layer (catalog + permissions + ingestion + serving) over registered storage locations.

### Azure Data Lake Storage + Azure Synapse (evidence layer A)

- Definition of the lake: "A *data lake* is a single, centralized repository where you can store all your data, both structured and unstructured… you don't need to conform your data to fit an existing structure. Instead, you can store your data in its raw or native format, usually as files or as binary large objects (blobs)."
- Store properties: "engineered to store massive amounts of data in any format, and to facilitate big data analytical workloads… capture data of any type and ingestion speed in a single location for easy access and analysis by using various frameworks." Multi-petabyte design, "hundreds of gigabits of throughput", no account/file-size limits stated as design goals.
- **Multi-engine access**: "primarily designed to work with Hadoop and all frameworks that use HDFS as their data access layer" via the ABFS driver; "The Apache Spark analytics engine and the Presto SQL query engine are examples of such frameworks."
- **Organization**: hierarchical namespace — "organize all the objects and files within your storage account into a hierarchy of directories and nested subdirectories"; directory operations are atomic metadata operations.
- **Governance**: "Finer grain security model" — Azure RBAC + POSIX ACLs, permissions at directory or file level; encryption at rest.
- **Cost/lifecycle**: blob-level tiering, lifecycle policy management (storage-layer machinery).
- **Synapse (the serving layer)**: "enterprise analytics service… across data warehouses and big data systems"; engines: Synapse SQL (serverless + dedicated pools), Apache Spark pools, Data Explorer; "Tables defined on files in the data lake are seamlessly consumed by either Spark or SQL. SQL and Spark can directly explore and analyze Parquet, CSV, TSV, and JSON files stored in the data lake." Built-in ingestion (Data Factory engine, 90+ sources claimed — marketing figure, not repeated as fact). Unified workspace (Synapse Studio) with RBAC.
- Notable: Azure splits the Type across two services — ADLS is the lake store (with namespace + ACLs), Synapse is the multi-engine serving/ingestion layer. Together they realize the same core; separately, ADLS alone is storage+namespace+ACLs.

### Databricks (evidence layer A — boundary case)

- Self-positioning: "a unified, open analytics platform for building, deploying, sharing, and maintaining enterprise-grade data, analytics, and AI solutions"; "uses AI with the data lakehouse"; flagship use case "Build an enterprise data lakehouse… combines enterprise data warehouses and data lakes".
- **Store**: cloud object storage in the customer's cloud account; data in open formats (Delta Lake — an open-source transactional table format over Parquet — plus other file formats for external tables).
- **Catalog/governance**: Unity Catalog — "the unified governance layer for data and AI"; every asset is a **securable object** in a three-level namespace `catalog.schema.object`; tables/volumes are **managed** (UC handles governance AND underlying file storage lifecycle) or **external** (governance only); privileges via ACLs (UI or SQL), attribute-based policies, row/column filters; workspace bindings; lineage ("automatically track how data and AI assets flow"); audit log system table; data classification (auto-tagging sensitive data); data quality monitoring (profiling + anomaly alerts); sharing via OpenSharing (managed Delta Sharing); AI asset governance.
- **Multi-engine serving**: Spark clusters, SQL warehouses, notebooks (SQL/Python/R/Scala), ML runtimes, Genie agents — all reading the same governed objects.
- **Ingestion**: Auto Loader ("incrementally and idempotently loading data from cloud object storage and data lakes into the data lakehouse"), Lakeflow pipelines; jobs/orchestration; git integration.
- Notable: Databricks documents itself as a *lakehouse* platform, not a data lake platform. It retains the full lake substrate (open formats on object storage, catalog, governance, multi-engine) and adds the transactional/warehouse layer (Delta ACID, SQL warehouses, metric views/semantic layer). It is the clearest evidence for where the lake→lakehouse boundary sits.

### Apache Hive / Hive Metastore (evidence layer A — historical baseline)

- Positioning: "distributed, fault-tolerant data warehouse system… facilitates reading, writing, and managing petabytes of data residing in distributed storage using SQL."
- **HMS**: "The central repository of metadata for Hive tables and partitions, providing clients including Hive, Impala, and Spark access through the metastore service API. A fundamental building block for modern data lakes." Also: "Hive Metastore (HMS) provides a central repository of metadata… making it a critical component of many data lake architectures."
- **Multi-engine**: HMS API clients include Hive, Impala, Spark; "Seamlessly integrates with Spark, Presto, Impala, and hundreds of other tools."
- **Storage**: "Built on top of Apache Hadoop with support for S3, ADLS, GS and more" — storage-agnostic file store.
- **Governance**: Kerberos authentication, "fine-grained access control", integration with Apache Ranger (authorization) and Apache Atlas (lineage/governance); audit logging.
- **Table machinery**: ACID for ORC tables (insert-only for other formats), compaction, Iceberg storage-handler support, replication (repl dump/load).
- Notable: the Hadoop-era lake = files in HDFS + HMS catalog + Ranger/Atlas governance + multiple engines. No cloud, no object storage, no S3. This is the historical form the L0 must still cover.

## Cross-product Comparison

| Structure | AWS Lake Formation | Azure ADLS + Synapse | Databricks | Hive/HMS (historical) |
|---|---|---|---|---|
| Lake store | Amazon S3 (registered locations) | ADLS Gen2 (blob + hierarchical namespace) | customer cloud object storage (Delta/Parquet files) | HDFS (later S3/ADLS/GCS) |
| Raw/native formats, schema-on-read | yes — "structured and unstructured; raw and transformed" | yes — "raw or native format… no need to conform" | yes — open file formats; external tables | yes — files + SerDe |
| Catalog / metadata layer | AWS Glue Data Catalog (databases/tables; Hive-metastore-like) | metastore via engines; HMS-compatible ecosystem | Unity Catalog (`catalog.schema.object`) | Hive Metastore |
| Organization of the estate | databases/tables over registered paths; federated catalogs | hierarchical directories; containers | catalogs/schemas/tables/volumes | databases/tables/partitions |
| Governance | grant/revoke RDBMS-style; DB/table/column/row/cell; LF-Tags; ABAC; CloudTrail audit | RBAC + POSIX ACLs at directory/file level | UC privileges/ACLs, ABAC policies, row/column filters, lineage, audit, classification | Ranger + Kerberos + Atlas lineage |
| Multi-engine serving | Athena, Glue, EMR, Redshift Spectrum (+ Iceberg REST catalog) | Spark, serverless SQL, dedicated SQL pools, Data Explorer | Spark, SQL warehouses, notebooks, ML runtimes | Hive, Impala, Spark, Presto (via HMS API) |
| Ingestion machinery | blueprints → Glue workflows (crawlers/jobs/triggers) | Synapse Pipelines (Data Factory engine) | Auto Loader, Lakeflow | (external to Hive proper) |
| Sharing | cross-account grants; AWS Data Exchange | (not on fetched page) | OpenSharing / Delta Sharing | (not on fetched page) |
| Transactional tables | S3 Tables / Iceberg federation | Delta Lake support in Spark | Delta Lake (ACID) — core to product | ACID ORC; Iceberg handler |

Convergent findings (layer B, cross-product):

1. Every realization separates **the store** (files/objects in open or native formats) from **the management layer** (catalog + governance + serving). The store is frequently a generic component (S3, ADLS, HDFS, GCS); the platform's identity lives in the management layer.
2. Every realization has a **persistent metadata catalog** that organizes files into structured, addressable objects (databases/tables or catalog/schema/table hierarchies). AWS explicitly models its catalog on the Hive metastore; HMS itself is described as "a fundamental building block for modern data lakes".
3. Every realization enforces **platform-level access governance** with fine granularity (column/row/cell in LF; directory/file ACLs in ADLS; row/column filters + ABAC in UC; Ranger in the Hive stack) and **audit**.
4. Every realization serves **multiple engines** over the same stored data through a shared access path (credential vending + catalog in AWS; ABFS driver in Azure; UC-governed objects in Databricks; HMS API in Hive).
5. Every realization includes **ingestion machinery** to fill the lake (blueprints/workflows, pipelines, auto-loaders) — though in the Hive-era stack ingestion sat outside the catalog proper.
6. Raw and transformed data coexist in the same store (AWS: "raw data and transformed data"; Databricks: bronze-to-gold style layering is market convention — zone *naming* not directly evidenced in fetched pages, see Uncertainties).

Divergent findings (vendor-specific, layer A single-product):

- LF-Tags / TBAC / hybrid access mode / credential vending / blueprints (AWS-specific mechanisms and names)
- Synapse Studio, serverless vs dedicated SQL pools, Data Explorer runtime (Azure-specific)
- Unity Catalog three-level namespace, managed-vs-external table split, OpenSharing branding, AI-asset governance (Databricks-specific)
- LLAP, HMS direct-API, ORC-specific ACID (Hive-specific)

## Canonical Model — L0 / L1 / L2 / L3

### L0 — Defining Invariant (deliberately small)

Three structures. Remove any one and the product stops being a data lake platform:

1. **The lake store** — a centralized, scalable store holding the organization's analytical data as files/objects in open or native formats at original fidelity; data is stored first and interpreted at read time (schema-on-read), not conformed to a predefined schema at write.
   - Remove → data warehouse (schema-on-write, modeled at ingest) or generic file/object storage.
2. **The catalog / organization layer** — a persistent metadata layer that organizes the stored files into structured, addressable objects (databases/tables or equivalent hierarchies), so the estate is worked with as data, not as files.
   - Remove → object storage / a file dump (Storage Management territory).
3. **Governed multi-engine access** — the platform controls who can access which stored data (platform-enforced permissions, fine-grained in mature products) and serves the store to multiple processing engines/consumers through that access layer, rather than locking it to one proprietary compute.
   - Remove governance → an ungoverned swamp (not a platform); remove multi-engine openness → a single-engine appliance (warehouse-shaped).

Modeling decision recorded: governance is placed in L0 for the *platform* Type (as distinct from "a data lake" as a raw storage pattern) because every sampled platform realization makes catalog+governance its identity; a store without any access machinery is not marketed or operated as a lake platform. This is a judgment call — flagged in Uncertainties.

### L1 — Common Mature Structure

- Ingestion machinery into the lake (templates/workflows, pipelines, incremental loaders)
- Fine-grained permission granularity (column/row/cell; directory/file ACLs) and tag/attribute-based policy at scale
- Discovery/search over the catalog; data classification/tagging
- Lineage and audit logging
- Cross-team / cross-account data sharing
- Raw + transformed/curated data coexisting in one store (layered zone conventions are a widespread market pattern; naming not directly evidenced in this pass)
- Storage lifecycle/cost machinery (tiering, lifecycle policies) at the store layer

### L2 — Variant / Optional

- Transactional table formats (Delta/Iceberg; ACID) — the lakehouse upgrade path
- Managed vs external tables (who owns the storage lifecycle)
- Federation (cataloging external/warehouse sources without migration)
- External data monetization/distribution (data exchange licensing)
- Streaming ingestion; log/time-series specialized engines alongside SQL/Spark
- AI-era additions: AI-asset governance, semantic layers/metric views, natural-language exploration
- Deployment shape: hyperscaler managed service vs platform-native suite vs open-source stack vs storage-service-plus-analytics-service split

### L3 — Vendor-specific (kept out of the final document)

- AWS: LF-Tags, hybrid access mode, credential vending, blueprints, data lake administrator designation semantics, one-catalog-per-region
- Azure: ABFS driver, Synapse Studio, serverless/dedicated pool split, Data Explorer
- Databricks: Unity Catalog namespace, OpenSharing, Genie, Lakeflow, Lakebase
- Hive: LLAP, HMS API details, ORC-specific ACID, repl dump/load

## Boundary Findings

- **vs Data Warehouse Platform**: the warehouse models data at write (schema-on-write), stores it in managed/proprietary structures coupled to its own compute, and is optimized for governed SQL BI. The lake stores raw in open formats, interprets at read, and decouples storage from engines. Remove schema-on-read/open formats → warehouse. (Both leaves exist in the directory; seam noted for joint review.)
- **vs Lakehouse Platform**: the lakehouse is a lake whose files have been upgraded to transactional tables (ACID, schema enforcement, performance features) with warehouse-grade SQL and unified governance on top. Product-level test: when the platform's primary promise is "warehouse-grade tables on open storage" (Delta/Iceberg as the centerpiece), it presents as a lakehouse; when the primary promise is "raw estate + governance + any-engine access", it presents as a data lake platform. Databricks self-identifies as the former while retaining the full lake substrate — recorded as the boundary case. (Lakehouse Platform is a separate directory leaf; seam noted for joint review.)
- **vs Object Storage / Storage Management**: object storage holds bytes with no catalog, no data-level permissions, no engine serving. Remove the management layer → storage.
- **vs Data Integration Platform**: integration is custodian of *movement* between systems and holds no data at rest; the lake platform is custodian of the *estate* — the typical destination those pipelines fill.
- **vs Data Catalog**: a standalone catalog describes assets living in systems it does not own; the lake platform's catalog is internal machinery over data the platform *does* hold.
- **vs Data Virtualization Platform**: virtualization answers queries without copying; the lake physically stores copies.
- **vs Data Fabric Platform**: fabric is an estate-spanning metadata/governance layer over distributed systems; the lake is a physical store with its own governance.
- **"Remove what to become another Type" summary**: remove schema-on-read/open formats → warehouse; remove catalog+governance → object storage; remove data-at-rest (movement only) → integration platform; add ACID tables as the centerpiece → lakehouse.

## Historical / Market-Sample Check (§24)

The Hadoop-era lake (files in HDFS + Hive Metastore + Ranger/Atlas + Hive/Impala/Spark) satisfies the L0 with no cloud, no object storage, no S3, no Delta/Iceberg, no tag-based access control. Therefore L0 must not require: cloud delivery, object storage, specific file formats, a specific permission mechanism, or any AI-era capability. It passed. Conversely, "big data scale" is a purpose (cheap storage of everything) rather than a definitional threshold — older departmental lakes on small clusters still fit.

## Uncertainties

1. **Governance in L0** — judgment call (see modeling decision). If a reviewer prefers a stricter reading, governance could be demoted to L1 and L0 reduced to store + catalog + multi-engine access. The final document phrases the core as "governed multi-engine access" so the seam is visible.
2. **Zone/medallion naming** — raw+transformed coexistence is directly evidenced (AWS); the raw/curated/consumed zone *naming* is a widespread market convention but was not directly evidenced in fetched pages in this pass. Kept hedged in the final document.
3. **Cloudera / enterprise hybrid realizations** — docs inaccessible; the on-prem enterprise pole is covered only via the Hive ecosystem. No Cloudera-specific claims made.
4. **Google BigLake / multi-cloud governance layers** — inaccessible; not covered.
5. **Exact permission semantics** (grant inheritance, default-deny behaviors, per-product ACL evaluation order) — not researched to that depth; final document stays conceptual.
6. **Directory seam** — Data Warehouse Platform and Lakehouse Platform leaves are unprocessed at time of writing; boundary descriptions here are one-sided and flagged for joint review.

## Final Synthesis

A Data Lake Platform is the management layer over a centralized raw-format analytical store: it holds the organization's analytical data as files/objects in open or native formats at original fidelity (schema-on-read), organizes that store through a persistent metadata catalog into structured addressable objects, governs access to it with platform-enforced fine-grained permissions, and serves it to multiple processing engines and consumers through that governed access layer. The store is frequently a generic component; the platform's identity is the catalog + governance + serving layer. Everything else — ingestion machinery, tag-based policy, lineage, sharing, transactional tables, AI governance — is standard capability or variant. The Type's two live seams are against the Data Warehouse (schema timing + format openness + compute coupling) and the Lakehouse (transactional tables as the centerpiece).
