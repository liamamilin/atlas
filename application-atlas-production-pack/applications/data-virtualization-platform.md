# Data Virtualization Platform

## Overview

A **Data Virtualization Platform** is a server-side data-access layer that connects to an organization's heterogeneous data sources in place, defines a persistent logical data model over them, and executes queries against that model on demand — reaching into the sources at query time and combining the results, without ever holding the data of record in a store of its own.

The defining core is small:

```text
Connections to data sources the platform does not own
└── Persistent logical data model over those sources (virtual views)
    └── On-demand query execution reaching into the sources at query time
```

Everything commonly associated with the category — connector catalogs, query optimization, caching and materialized acceleration, data APIs, catalogs, governance and lineage tooling — is widespread in mature products but is not what makes the platform a data virtualization platform. A product that copies data into a store it owns and queries that copy is a data warehouse, lakehouse, or replication platform; a product that only describes data without serving queries is a data catalog. The virtualization platform is the layer in between: it serves queries over data it never takes custody of.

## Users & Context

Primary users:

- **data engineers / data architects** — connect sources, build and maintain the logical model (views that join, union, filter, and reshape source data), expose it to consumers
- **analysts, data scientists, and BI tools** — consume the model through SQL clients and BI applications, querying virtual views as if they were ordinary tables

Secondary users:

- **data stewards / governance owners** — apply security policies, descriptions, and standards at the logical layer
- **platform administrators** — operate the server: authentication, credentials, workload limits, monitoring, environment promotion

The typical context is an enterprise with data spread across operational databases, warehouses, data lakes, files, and SaaS applications, where consumers need unified access without waiting for every source to be piped and consolidated into one store. The platform sits between the sources and the consumers; it is infrastructure that most end consumers touch only through a SQL connection or an API.

## Core Model

### The Defining Core

```text
Data source connections
└── Base views (source-shaped logical tables)
    └── Derived views (joined / unioned / filtered / transformed)
        └── The virtual model (persistent, named, reusable)
            └── Query execution at request time
                └── Results returned to the consumer
```

- **Data source connections** — configured access to external systems the platform does not own: relational databases, warehouses, data lakes and object stores, files, SaaS applications, web services. Each connection carries the connector type, address, and credentials. The platform is a custodian of access, never the system of record.
- **Base views** — for each connected source, the platform introspects its structure and represents it as logical tables shaped like the source. A base view is a standing definition of "what this source looks like here," not a copy of its data.
- **Derived views** — the heart of the model. Users compose base views and other derived views into new logical tables using relational operations: joins across sources, unions of similar tables, selections, projections, aggregations, and reshaping of nested or semi-structured data. A derived view is defined once, kept as a named object, and can itself be used to build further views — layer by layer, until a consumer-facing view exists.
- **The virtual model** — the whole collection of base and derived views, organized (by databases/schemas, folders, or spaces depending on the product) and persistently stored as the platform's managed metadata. This model is what users edit, version, promote between environments, and govern.
- **Query execution** — when a consumer queries any view, the platform decomposes the request into sub-queries sent to the involved sources in real time, combines the returned data, and streams the result back. The view's definition — not a stored copy of its data — determines what is computed.

### One Structure, Many Implementations

The core model is conceptual. Products realize each piece differently:

```text
Concept:  Data source connections
Realizations:  JDBC/ODBC connections, native adapters, connector plugins,
               API/SaaS connectors, file and object-store readers

Concept:  The virtual model
Realizations:  SQL-defined views in a platform language, visual view editors,
               properties-file catalogs, spaces/folders hierarchies

Concept:  Query-time execution
Realizations:  single-server engines, distributed clusters with a planner
               and parallel workers, pushdown into source SQL
```

A reader who has only seen one realization (for example, a visual view designer over cloud warehouses) should still be able to recognize a code-defined federated query engine as the same Type from the core model.

### Standard Capabilities

Mature products commonly add these capabilities. They make the platform practical but do not define it:

- **Connector catalogs** — broad libraries of prebuilt connectors, with SDKs or frameworks for custom ones.
- **Query optimization with pushdown** — the planner pushes filters, projections, and where possible joins down into the sources so that only needed data crosses the wire; some products ship partial operations into capable sources ("data ship" style).
- **Optional acceleration** — caching of query results or whole views (partial, full, or incremental modes), materialized summary tables, or transparently managed precomputed copies that the optimizer substitutes automatically when beneficial. Acceleration never changes the system of record: invalidate the cache and the sources remain authoritative.
- **Logical-layer security** — authentication against enterprise identity (LDAP, Kerberos, SAML, OAuth/SSO), fine-grained privileges on views, row- and column-level policies, data masking, and credential vaults or delegated ("pass-through") credentials so source access happens under governed identities.
- **Data services** — publication of views beyond SQL: REST, OData, or GraphQL endpoints, and sometimes message-listener surfaces, so applications can consume the same governed model.
- **Discovery and lineage** — a catalog-style face over the virtual model (search, descriptions, usage) and lineage derived from view composition, since every view's derivation is recorded in the model itself.
- **Monitoring and workload control** — query monitors, execution traces showing how a query was decomposed, statistics, health checks, and resource rules that cap or prioritize concurrent queries.
- **Lifecycle machinery** — export/import of the model between environments, version-control integration, and promotion from development to production.

## How It Works

### Build the model

```text
Connect a source
→ the platform introspects its structure
→ base views appear, shaped like the source
→ compose derived views: join, union, filter, transform
→ repeat, layer by layer, until consumer-facing views exist
→ describe, secure, and organize the views
```

There is no data loading step in this loop. Building the model changes metadata, not data.

### Serve a query

```text
Consumer submits SQL (or calls a published API) against a view
→ platform parses and plans the query against the view's definition
→ planner pushes down what the sources can handle
→ sub-queries execute against the sources in real time
→ platform combines the partial results (joins, unions, aggregations)
→ result streams back to the consumer
```

Every query repeats this loop. Two queries against the same view can hit different sources or different plans; the view's definition stays stable while the execution adapts.

### Accelerate (optional)

```text
Identify slow, repeated queries or heavy views
→ configure a cache / materialized copy / precomputed summary
→ queries are served from the accelerated copy where possible
→ refresh or invalidate on a schedule or on demand
→ the source remains the system of record throughout
```

### Govern and operate

```text
Apply privileges and row/column policies at the logical layer
→ monitor queries, traces, and source health
→ control concurrency and workload priority
→ export/import and version the model across environments
```

### Defining core vs standard capabilities vs variants

**Defining core** — without these, not a data virtualization platform:

- connections to data sources the platform does not own
- a persistent logical model (base + derived views) over those sources
- on-demand query execution reaching into the sources at query time

**Standard capabilities** — present in most mature products:

- connector catalogs and custom-connector extension
- optimization with pushdown
- optional acceleration (caching, materialization, transparent rewrite)
- logical-layer security (SSO, privileges, row/column policies, credential vaults)
- data services (REST/OData/GraphQL publication)
- discovery, lineage, monitoring, workload control
- lifecycle machinery (export/import, version control, promotion)

**Common variants** — depend on positioning, deployment, and customer:

- acceleration depth (none → cache → bundled replication/ETL features)
- deployment (self-hosted server, cloud service, open-source cluster)
- semantic-layer depth, self-service web surfaces, streaming listeners
- write-back to transaction-capable sources (product-dependent)

## Interfaces

Described conceptually; exact names and layouts vary by product.

### Design studio / view editor

The builder's primary surface.

- tree or catalog of sources and views, a view editor (visual or SQL-based), schema previews of each view
- primary actions: connect a source, create/derive a view, edit a definition, inspect lineage, test-run a query

### Query / VQL shell

A SQL console against the virtual model.

- primary actions: run queries against any view, inspect execution traces showing how the query was decomposed and pushed down

### Catalog / discovery face

The consumer's entry surface in products that ship one.

- search and browse over published views, descriptions, ownership, lineage
- primary actions: find a view, understand it, connect to it

### Administration and monitoring console

The operator's surface.

- server configuration, authentication and credential settings, concurrency and resource rules
- query monitor, execution statistics, health and cache management

### Client connectivity

The consumer-facing endpoints: SQL drivers (JDBC/ODBC-class) that any BI tool or client can use, plus published REST/OData/GraphQL data services where offered.

## Important Rules / Behaviors

### The platform never holds the data of record

Sources remain authoritative. Caches and materialized copies are acceleration: they can be invalidated or dropped without breaking the model, and a query can always fall back to the sources. If a product's store becomes the system of record, the product has stopped being a virtualization platform.

### Security applies at the logical layer

Policies (privileges, row/column rules, masking) attach to views, so they hold no matter which source serves the data and no matter which interface (SQL, API) the consumer uses. Conversely, source-side credentials are typically held by the platform — via vaults or delegated/pass-through login — so consumers never touch sources directly.

### Query performance depends on the sources

Because execution happens at query time across the network, latency and load characteristics follow the slowest involved source. This is the structural trade the Type makes against copying: no pipeline to build and keep fresh, but every query pays the federation cost unless acceleration is configured.

### Pushdown has limits

Sources differ in query capability. The planner pushes down what each source can handle and performs the remaining operations itself; some sources only accept restricted queries. Execution traces exist precisely because plans vary.

### The model is metadata, and it is versionable

Views are definitions, so the whole model can be exported, imported, version-controlled, and promoted between environments like code. Lineage is derivable from the definitions themselves.

### Write-back is conditional

Some products can update sources through the virtual layer, but only where the underlying source supports transactions. Read-mostly is the typical posture; write-back is a product-dependent capability, not a defining property.

## Variants

- **Pure-play virtualization platform** — the logical access layer as the whole product; acceleration and governance layered on top.
- **Lakehouse-native platform** — virtualization semantics (views over external sources, transparent acceleration) inside a product centered on an organization's own lake storage; the strongest current straddle with the Lakehouse Type.
- **Open-source federated query engine** — a distributed SQL engine over connectors, configured as code; typically lacks the built-in governance and catalog layers, which are added around it.
- **Enterprise suite module** — virtualization embedded in a broader data-management suite alongside integration, catalog, and quality products.
- **DBMS federation capability** — the same technique (linked servers, heterogeneous gateways) embedded inside a database product rather than sold as a standalone platform; adjacent realization of the technique, not the platform Type.
- **Acceleration-depth spectrum** — from no acceleration at all, through caching and materialized summaries, to products that bundle replication/ETL features for heavy views.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Data Integration Platform | builds and runs persistent pipelines that move data between endpoints; virtualization moves nothing and serves queries at request time |
| ETL / ELT Platform | transformation happens in flight or in the destination and results are stored; virtualization computes at query time over sources left in place |
| Data Replication Platform | maintains a synchronized physical copy in a target store; virtualization has no target store |
| Change Data Capture Platform | delivers an ordered stream of row-level changes; virtualization serves query results over current logical views |
| Data Warehouse / Lakehouse Platform | holds the data of record and computes over its own store; virtualization owns no store of record (caching is acceleration, not custody) |
| Data Catalog | describes data in systems it does not own but performs no data operations; using an asset means leaving for the source — virtualization executes the query itself |
| Data Fabric Platform | an estate-wide management layer that may include virtualization as one technique among several; virtualization is the single access technique as the center |
| Data Exchange Platform | entitles and delivers dataset offerings between organizations; virtualization is intra-organization logical access |
| SQL Client / Database IDE | user-facing query tools that connect to one system at a time; a virtualization platform is the server-side layer such tools connect to |
| API Management Platform | manages API lifecycle and traffic as its center; virtualization merely publishes data APIs as one delivery surface |

The most important boundary is the movement/copy line shared with integration, ETL/ELT, and replication: those Types establish persistent copies or flows of data; virtualization's defining promise is that no copy is required — the query reaches the source. The second most important is custody: warehouses and lakehouses own their data; a virtualization platform never does.

## Representative Products

- Denodo Platform
- TIBCO Data Virtualization (rebranding as Spotfire Data Virtualization)
- Dremio
- Trino

The core model was checked against the open-source engine pole (which ships none of the governance/catalog/acceleration layers in its core) and against lakehouse-positioned products, to avoid defining the Type by any single era or packaging pattern.

## Sources

Research date: **2026-09-07**

- Trino — official concepts documentation: https://trino.io/docs/current/overview/concepts.html
- Denodo — Virtual DataPort Administration Guide (General Architecture and manual structure): https://community.denodo.com/docs/html/accessible/8.0/vdp/administration/general_architecture/general_architecture.html
- Denodo — Data Virtualization product page: https://www.denodo.com/en/data-virtualization
- TIBCO / Spotfire Data Virtualization — product documentation hub and 8.9 release notes: https://docs.tibco.com/products/tibco-data-virtualization
- Dremio — "What is Dremio?" and Key Concepts documentation: https://docs.dremio.com/current/what-is-dremio/key-concepts/

> Sourcing limitation: TIBCO workflow-level detail (design-studio procedures) and Dremio security/acceleration chapters were read at documentation-structure level only; claims that depend on them are stated at moderate strength. Precise numeric limits, default settings, and version-specific behaviors are intentionally not stated. Detailed evidence and product-by-product observations are recorded in the paired Research Notes.
