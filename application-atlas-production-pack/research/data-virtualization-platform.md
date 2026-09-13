# Research Notes — Data Virtualization Platform

## Research Goal

Understand what a Data Virtualization Platform really is as an Application Type: what objects exist inside it, what users do with them, how a query actually flows, what rules govern the system, and where the boundary lies against the neighboring §13 data-platform Types (integration, replication, CDC, warehouse/lakehouse, catalog, fabric, exchange).

## Prior-Pass Cross-Check Obligations

Three processed leaves left binding cross-checks for this pass:

- **data-replication-platform pass**: "remove the target store → data-virtualization-platform" — replication holds a synchronized physical copy; virtualization has no target store.
- **data-integration-platform pass**: "remove the movement → data virtualization" — integration moves data through persistent pipelines; virtualization does not move data.
- **data-fabric-platform pass**: ratified split — "virtualization platform = logical access technique as the center"; fabric = estate-spanning unified metadata layer with integration/governance/delivery as functions of one system. Joint review recommended when either leaf is processed.
- **data-exchange-platform pass**: boundary held on intra-org movement vs inter-org entitlement; cross-check at this pass recommended.

All four are discharged in Boundary Findings below.

## Initial Boundary

Initial hypothesis before research:

- Core use: give consumers unified, governed, query-time access to data that lives in many heterogeneous systems, without copying it into a store the platform owns.
- Users: data engineers / architects build the logical model; analysts, data scientists, BI tools consume; stewards and admins govern and operate.
- Nearest neighbors: ETL/ELT & Data Integration (movement vs no movement), Replication (copy vs no copy), Data Warehouse/Lakehouse (owned store vs none), Data Catalog (describes vs serves queries), Data Fabric (one technique vs estate-wide management layer), SQL clients (query tool vs server-side access layer).
- Unknowns: whether caching/materialization is definitional (products increasingly ship it); whether API publication is definitional; where the Dremio lakehouse pole lands; historical check (federated-database era).

## Research Questions

1. What is the platform's managed object — what does a user create, keep, and edit over time?
2. How does a query actually execute — what happens between a client's SQL and the returned rows?
3. What does the platform hold — does it ever become the system of record?
4. How is security applied — at the source, at the logical layer, or both?
5. What acceleration exists, and is it optional?
6. What surfaces do builders vs consumers vs operators use?
7. How does the model move through environments (lifecycle)?
8. Where does this Type end and integration/replication/warehouse begin?

## Representative Products

Selected for market representativeness, documentation quality, and philosophical spread:

| Product | Pole | Why sampled |
|---|---|---|
| Denodo Platform | pure-play data virtualization leader | the category's reference implementation; full Tier-1 admin guide reachable |
| TIBCO Data Virtualization (rebranding to Spotfire Data Virtualization) | classic enterprise-suite DV | Composite Software heritage; enterprise deployment machinery; release notes + docs hub reachable |
| Dremio | lakehouse-native pole | virtualization semantics (views over external sources, transparent acceleration) inside a lakehouse-positioned product |
| Trino | open-source federated query engine | engine-only pole; proves by omission which capabilities are NOT definitional |

## Sources

Fetched 2026-09-07:

- Trino — official concepts documentation (Tier 1): https://trino.io/docs/current/overview/concepts.html
- Denodo — product page (Tier 2): https://www.denodo.com/en/data-virtualization
- Denodo — User Manuals index + Expert Trails list (Tier 1): https://help.denodo.com/docs/html/9.2/index (redirects to community.denodo.com/docs)
- Denodo — Virtual DataPort Administration Guide 8.0, General Architecture + full TOC (Tier 1): https://community.denodo.com/docs/html/accessible/8.0/vdp/administration/general_architecture/general_architecture.html
- TIBCO — Spotfire/TIBCO Data Virtualization product docs hub + 8.9 release notes (Tier 1 release notes, Tier 2 hub): https://docs.tibco.com/products/tibco-data-virtualization
- Dremio — Enterprise documentation root, "What is Dremio?", "Key Concepts" (Tier 1): https://docs.dremio.com/current/what-is-dremio/key-concepts/

Access limitations:

- Denodo: the accessible 8.0 manual index and the General Architecture page were fetched in full; deeper chapters (cache modes detail, resource manager detail) were read at TOC level only. Concept-level claims are safe; numeric defaults not asserted.
- TIBCO: full user-guide chapters (Studio workflows) not fetched; evidence is release-notes + docs-hub level → workflow-level claims kept moderate.
- Dremio: key-concepts and what-is pages fetched; acceleration/security chapters read at TOC level.
- Trino: concepts page fetched in full; connector/security chapters read at TOC level.
- Historical check (federated-database era, DBMS federation features) is structural inference from the sampled products' own positioning; no legacy documentation directly fetched — flagged in Uncertainties.

## Product Observations

### Denodo Platform (pure-play pole)

Evidence layer: A (direct, Tier-1 admin guide + Tier-2 product page).

Key observations:

- Official architecture statement: Virtual DataPort "enables business applications to process a series of distributed and heterogeneous data sources … as though the data were contained in a large 'Virtual' Database"; it "acts as a mediator that provides a structured and unified view of the data contained in all the data sources."
- Three-layer model: **physical layer (wrappers)** → **logical layer** (with a "Data Module: Cache") → **user layer**.
- **Data sources + base views**: connect via JDBC, ODBC, SOAP web services, XML, JSON, delimited files, Excel, web sources, LDAP, SAP BAPI, Salesforce, object storage (Parquet), HDFS/S3 paths, custom wrappers. Each source is introspected into **base views** shaped like the source.
- **Derived views** composed from base/other views: union, join, selection, flatten, intersection, minus, interface views; tree view of the composition; **data lineage** derived from view composition.
- **VQL (Virtual Query Language)** — SQL-like language used to create views combining sources with "selections, projections, unions, joins, groups."
- **Query execution**: "When the system receives a VQL query on a previously defined view, it can generate an execution plan … a list of subqueries that are sent in real-time to the various sources involved and a series of operations combining the data obtained from each source."
- **Cache module** optional: "The system can access the source data in real time … Caches can be created and configured for the sources or views as required." Cache modes: partial / full / incremental; cache maintenance task; cache stored in an external database.
- **Write-back**: "Virtual DataPort also allows the updating of data sources, provided that these are capable of supporting transactions."
- **Publication**: SOAP/REST web services, OData 4.0 service, GraphQL service, RESTful architecture with associations; JMS and Kafka listeners; remote tables (pushdown into sources).
- **Security**: privileges system; server authentication via LDAP, Kerberos, SAML, OAuth, Denodo Security Token; credentials vault (AWS Secrets Manager, Azure Key Vault, CyberArk, HashiCorp Vault).
- **Operations**: Resource Manager (plans and rules — query workload control), concurrent-request limits, memory management, query monitor, execution trace viewer, health monitoring, audit trail.
- **Lifecycle**: metadata export/import across environments (environment-dependent vs independent elements), version control systems integration (Git/TFS/SVN), storing metadata on an external database.
- **Surrounding modules**: Design Studio (web), Administration Tool + VQL Shell, Data Catalog, Solution Manager (ops/monitoring), Scheduler, Diagnostic & Monitoring Tool.
- Product page (Tier 2) capability framing: logical data abstraction; smart query acceleration (optimizer + MPP engine + AI-powered acceleration); advanced semantics (catalog); universal connectivity + data services (SQL, JSON, REST, GraphQL APIs); flexible data integration "from real-time federation to selective materialization (caching, aggregation-aware summaries), full replication (ETL, ELT, micro batching), and streaming"; unified security and governance.
- Users named on the product page: data architects, data engineers, data scientists/analysts, analytics leaders, CIOs/CTOs, data stewards.

### TIBCO Data Virtualization / Spotfire Data Virtualization (enterprise-suite pole)

Evidence layer: A for release-notes-level facts (Tier 1), B for general DV framing.

Key observations:

- Design/admin/self-service surfaces: **Studio** (design tool), **Web Manager** (administration), **Web UI** (self-service flows with a Flow editor and "Staging Operator").
- **Adapters** for data sources; **introspection** with "Detect New Resources During Re-Introspection" (source re-scan); Data Source Toolkit for building adapters.
- **Query engine** with SQL script support (incl. geospatial types), **Data Ship Join** and **bulk loading** frameworks (pushdown/load optimization per adapter), top-N query optimization.
- **Caching**: multi-table caching with proactive capability detection; cache refresh with cancellation rights tied to permissions ("Modify All Status").
- **Client delivery**: JDBC, ODBC, ADO.NET drivers; OData with SQL-mapping optimizations; IPv6 support.
- **Security**: pass-through login (delegated credentials to the underlying database), Kerberos SSO with credential delegation, service accounts, OAuth proxy login with fetch access tokens, dynamic-security custom functions for row-level security (TestUserIdentity, CurrentUserName, CurrentUserDomain).
- **Operations**: system tables (SYS_CONFIG, SYS_SESSIONS), deployment metrics via procedures, monitoring tab with drill-down dashboards, deployment report (snapshot of sources, caches, clusters), client-application identification.
- **Data Staging** (new in 8.9): redefines "data source" as "data store" usable as both source and destination — staged copies with retention periods; monitoring dashboard. This is an explicit drift toward integration capability inside a DV product.
- Rebranding: TIBCO Data Virtualization → Spotfire Data Virtualization (SDV) — label drift, structure unchanged.

### Dremio (lakehouse-native pole)

Evidence layer: A (Tier-1 docs).

Key observations:

- Positioning: "open lakehouse platform" for self-service analytics; "analysts can join data in the lake with data in external databases, so they don't have to move data into object storage to derive value from that data" — federation across sources without movement.
- **Sources**: object stores (Amazon S3, Azure Storage) and external databases; files/folders formatted as tables.
- **Tables and views**: views are "logical representations of data … always reflect the current state of the parent tables or views they are derived from" — the virtual-view concept, lakehouse-flavored.
- **Reflections**: "precomputed, optimized copy of source data or query results that accelerates query performance"; optimizer transparently rewrites queries to use reflections when beneficial — acceleration is transparent and optional, direct table access remains the baseline.
- **Spaces and folders** organize views (project/purpose/department); per-user **home space**.
- **Consumption**: BI client connectivity (Power BI, Tableau), SQL reference, REST API; "Build Data Products" (discover, develop, accelerate).
- Based on Apache Iceberg / Apache Arrow; DML directly in the lake.

### Trino (open-source engine pole)

Evidence layer: A (Tier-1 docs).

Key observations:

- "Trino is a distributed query engine that processes data in parallel across multiple servers" — coordinator (parse, plan, manage) + workers (execute tasks).
- **Data sources**: "data lakes and lakehouses, numerous relational database management systems, key-value stores, and many other data stores" — accessed via **connectors** (SPI plugins): Delta Lake, Hive, Hudi, Iceberg, MySQL, PostgreSQL, Oracle, SQL Server, Cassandra, ClickHouse, OpenSearch, Pinot, Prometheus, SingleStore, Snowflake, utility connectors.
- **Catalog** = configuration properties (connector + credentials + URL) naming a data source; many catalogs per cluster; cross-catalog queries "even within the same SQL query." Catalog → schema → table naming.
- **Query execution model**: statement → query → distributed plan → stages → tasks → splits → drivers → operators; exchanges transfer data between nodes.
- **Clients**: any SQL client/driver (CLI, desktop, web, SaaS BI tools); ANSI-compatible SQL.
- Notably absent from the OSS core (by omission evidence): no built-in governed catalog of business semantics, no security-masking layer beyond connector/cluster authn-z, no materialized cache in core — confirming these are common-but-not-definitional.

## Cross-product Comparison

| Dimension | Denodo | TIBCO/Spotfire DV | Dremio | Trino |
|---|---|---|---|---|
| External sources, not owned | yes (JDBC/ODBC/SOAP/files/SaaS/SAP/LDAP…) | yes (adapters, introspection) | yes (object stores + external DBs) | yes (connectors, catalogs) |
| Persistent logical model as managed object | yes — base views + derived views (join/union/selection/flatten/intersection/minus/interface), VQL definitions | yes — views/flows in Studio; data stores | yes — views derived from tables/views, organized in spaces | yes — catalogs/schemas/views; views via SQL |
| Query-time execution into sources | yes — plan → real-time subqueries to sources + combination | yes — query engine with data ship join | yes — query over sources; views always current | yes — distributed plan over connectors |
| Owns data of record | no (cache is acceleration) | no (staging is explicit, optional) | no (lake store is the org's; reflections are acceleration) | no |
| Pushdown/optimization | yes (optimizer, remote tables) | yes (data ship join, top-N) | yes (optimizer, reflection rewriting) | yes (stages/splits, connector pushdown) |
| Optional acceleration | cache module (partial/full/incremental), materialized tables | multi-table caching, bulk loading | reflections (transparent) | not in OSS core |
| Publication surfaces | JDBC/ODBC + SOAP/REST/OData/GraphQL + JMS/Kafka listeners | JDBC/ODBC/ADO.NET + OData | JDBC/ODBC + BI tools + REST API | any SQL client via JDBC etc. |
| Security at logical layer | privileges, row/col policies, masking-class machinery, vaults, SSO | pass-through/delegated credentials, row-level dynamic functions | security & compliance layer (TOC-level) | cluster/connector authn-z (OSS core) |
| Catalog/discovery face | Data Catalog module | monitoring + system tables; (suite) | spaces + data products discovery | none in core |
| Lifecycle machinery | metadata export/import, VCS integration | deployment report, version control system info | (TOC-level) | config-as-code properties files |
| Write-back to sources | yes (transaction-capable sources) | staging destinations | DML in lake (Iceberg) | limited (connector-dependent) |
| Workload control | resource manager plans/rules, concurrency limits | deployment metrics, monitoring dashboards | (admin TOC-level) | cluster resource groups (TOC-level) |

## Canonical Abstraction

### L0 — Defining Invariant

Three properties. Remove any one and the product stops being a data virtualization platform:

1. **Connections to data sources the platform does not own.** Heterogeneous external systems — databases, warehouses, lakes, files, SaaS/APIs — connected in place; the platform is a mediator/access layer and never the system of record. (Remove → the platform becomes a data warehouse/lakehouse.)
2. **A persistent logical data model defined over those sources.** Virtual views/tables that combine and reshape sources (joins, unions, selections, transformations), kept as named, reusable, editable definitions — the platform's managed object. (Remove → an ad-hoc query tool / SQL client.)
3. **On-demand query execution reaching into the sources at query time.** A query against the virtual model is decomposed into sub-queries executed against the sources in real time and combined into a result — without first establishing a persistent copy of the data. (Remove → ETL/ELT or replication platform.)

### L1 — Common Mature Structure

Very common in mature products, not required to define the Type:

- connector/adapter catalog with custom-connector extension
- cost-based optimization with pushdown (predicate/projection pushdown, join strategies, data-ship)
- optional acceleration: caching (partial/full/incremental), materialized tables/summaries, transparent rewrite (reflections-class)
- logical-layer security: SSO/LDAP/Kerberos/SAML/OAuth, fine-grained privileges, row/column-level policies, credential vaults, delegated/pass-through credentials
- publication beyond SQL: REST/SOAP/OData/GraphQL data services
- discovery/catalog face over the virtual model (search, descriptions, lineage)
- monitoring: query monitor, execution traces, statistics, health
- lifecycle: metadata export/import, version-control integration, environment promotion
- workload control: resource plans/rules, concurrency limits
- lineage derived from view composition

### L2 — Variant / Optional Structure

- acceleration depth: none → cache → materialized summaries → bundled replication/ETL features (Denodo's "flexible data integration" spectrum)
- deployment: self-hosted server, cloud SaaS, OSS cluster, embedded engine
- positioning: standalone pure-play vs lakehouse-native vs suite module vs DBMS federation capability
- semantic-layer depth (business terms/metrics over the logical model)
- self-service web surfaces for non-engineers
- streaming listeners (Kafka/JMS)
- write-back to transactional sources
- data staging (explicit optional copies with retention — TIBCO)

### L3 — Vendor-specific (research notes only)

- Denodo: VQL language; Virtual DataPort / ITPilot / Scheduler / Solution Manager module names; Denodo Security Token; Materialization expert trail.
- TIBCO: Studio / Web Manager / Web UI triad; Data Ship Join; SYS_* system tables; Spotfire rebrand; Data Staging operator.
- Dremio: Reflections; Spaces; home space; data-products framing; Iceberg/Arrow positioning.
- Trino: coordinator/worker/stage/split/driver/operator/exchange execution model; catalog properties files; SPI connector architecture.

## Vendor-specific Findings

- Denodo's "flexible data integration" spectrum (real-time federation → selective materialization → full replication/ETL/ELT/micro-batching → streaming) shows the pure-play pole absorbing integration capabilities — a capability overlap with the Data Integration Platform Type, not a boundary dissolution: the center remains the logical access layer.
- TIBCO's Data Staging explicitly redefines sources as stores usable as destinations — the same drift, from the suite pole.
- Dremio's reflections are the clearest "transparent acceleration" realization: optimizer compares reflection-based vs direct plans and rewrites automatically.
- Trino's OSS core ships none of the governance/catalog/acceleration layers — the strongest evidence that L1 items are common, not definitional.

## Rejected Findings

- "Data virtualization = no caching/materialization at all" — rejected: every mature pole ships optional acceleration; the invariant is that the source remains the system of record and acceleration is optional, not that copies never exist.
- "Data virtualization = semantic layer" — rejected: business semantics are a common layer on top (Denodo catalog, Dremio spaces/data products), not the defining structure; a DV platform without a semantic layer (Trino core) still qualifies.
- "Data virtualization = API gateway for data" — rejected: API publication is a common delivery surface; the defining act is query-time logical access, not API management.
- "Data virtualization requires a GUI design studio" — rejected: Trino is configured via properties files and SQL; the model can be code-defined.
- "Data virtualization is read-only" — rejected: Denodo documents write-back to transaction-capable sources; Dremio supports DML in the lake. Read-mostly is typical, not definitional.

## Boundary Findings

| Neighbor Type | Relationship | "Remove what → becomes the neighbor" / distinction |
|---|---|---|
| Data Integration Platform (processed) | sibling | Integration's center is persistent configured pipelines that move data between endpoints; virtualization's center is query-time logical access with no movement. Cross-check DISCHARGED from this side: "remove the movement → data virtualization" holds. Overlap is real (DV platforms bundle optional replication/ETL; integration platforms add pushdown) but the centers differ. |
| Data Replication Platform (processed) | sibling | Replication's defining promise is a synchronized physical copy in a target store; virtualization has no target store. Cross-check DISCHARGED: "remove the target store → data-virtualization-platform" holds. |
| Change Data Capture Platform (processed) | distinct | CDC delivers an ordered change-event stream; virtualization serves query results over current logical views. CDC may feed a DV source; mechanism vs access layer. |
| Data Warehouse / Lakehouse Platform | adjacent, straddle | Warehouse/lakehouse hold the data of record and compute over their own store; virtualization owns no store of record. Dremio straddles: lakehouse-positioned, but its views-over-external-sources + transparent-acceleration semantics are the DV core; recorded as straddle, not a merge. |
| Data Catalog (processed) | sibling, describe-only | Catalog describes data in systems it does not own but performs no data operations; using an asset means leaving for the source. DV executes queries. DV platforms ship catalog faces (Denodo Data Catalog) — packaging, not merge. |
| Data Fabric Platform (processed) | sibling | Fabric = estate-wide management layer (unified metadata + integration + governance + delivery as functions of one system); virtualization = one access technique as the center. Denodo shows the virtualization pole hardening into a fabric posture. Cross-check DISCHARGED from this side: split held. |
| Data Exchange Platform (processed) | distinct | Exchange = inter-org entitlement + delivery of dataset offerings; virtualization = intra-org logical access. Cross-check DISCHARGED: held. |
| SQL Client / Database IDE / Ad-hoc Query Application | adjacent | Those are user-facing query tools over one connection at a time; DV is a server-side access layer with a managed, governed model. A DV platform is what such tools connect to. |
| Semantic Layer (no directory leaf) | capability overlap | Business-meaningful views/metrics are one common layer of a DV platform; not a separate Type in the directory. |
| API Management Platform | adjacent | DV publishes data APIs as one delivery surface; it does not manage API lifecycle/rate-limiting/partner portals as its center. |
| DBMS federation features (linked servers, heterogeneous gateways) | capability form | Same technique embedded in a DBMS rather than a standalone platform; the directory leaf is the platform form. Recorded as adjacent realization, not a merge. |

## Historical / Market-Sample Check

Structural inference (flagged — no legacy docs directly fetched): the federated-database-era products of the 2000s (enterprise federation servers; DBMS federation features) satisfy the three L0 properties — connect heterogeneous sources, define logical views, execute at query time — while lacking catalogs, API publication, caching, and modern governance. Therefore none of those L1 items may enter the definition. Conversely, modern lakehouse-era products (Dremio) still satisfy L0 despite the different substrate. The definition is era-stable.

## Uncertainties

- TIBCO: workflow-level detail (Studio view-building steps) not directly observed; claims kept at release-notes/docs-hub level.
- Dremio: security/acceleration chapters read at TOC level; reflection mechanics quoted from key-concepts page only.
- Trino: governance/caching absence asserted from the OSS core docs structure; enterprise distributions may add such layers (not researched).
- Historical check is structural inference, not direct observation of legacy documentation.
- Whether "data virtualization" remains the dominant market label (vs "logical data management", "data fabric", "semantic layer") is positioning drift, not structure; noted only.

## Final Synthesis

The Data Virtualization Platform Type is real and has a small, era-stable core: **connect to data sources the platform does not own → define a persistent logical model over them → execute queries on demand by reaching into the sources at query time, without holding the data of record.** Everything else vendors ship — connectors, optimizers, caching, reflections, catalogs, API publication, governance, lifecycle tooling, workload control, even bundled replication — is common mature structure or optional capability layered on that core. The Type's sharpest boundaries: against integration/replication/CDC (movement/copy contracts vs no-movement logical access), against warehouse/lakehouse (owned store vs none), against the catalog (describes vs serves), and against the fabric (one technique vs estate-wide management layer). The Dremio straddle and the Denodo/TIBCO capability absorption are recorded as packaging drift, not boundary dissolution.
