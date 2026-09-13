# Lakehouse Platform

## Overview

A **Lakehouse Platform** is an analytical data platform whose store of record is a set of **transactional tables built on open data file formats** — tables that carry warehouse-grade semantics (ACID-style consistency, schema enforcement and evolution, versioned table states) but live as files in open formats on scalable storage — together with a **catalog** that makes those tables the addressable, governed layer of record, and a serving layer through which **one governed store serves multiple kinds of analytical work**: SQL analytics for analysts and BI consumers, data engineering and transformation for builders, and commonly data science and machine learning.

The category exists because the two classic analytical stores each paid a tax. The data warehouse modeled everything at write and kept data in a proprietary, compute-coupled format — excellent for governed SQL, poor for scale economics, raw formats, and non-SQL workloads. The data lake kept everything cheaply in open files — excellent for scale and flexibility, but its tables were not truly transactional, so concurrent updates, reliable pipelines, and warehouse-grade management were hard to build on it. The lakehouse is the merger: the lake's open storage substrate, upgraded with a transactional table layer, served like a warehouse — with the explicit promise that one copy of the data serves every analytical workload, so the estate does not fragment into a lake, a warehouse, and copies in between.

The defining structure is small:

```text
Open-format transactional table store
  (the data of record: ACID/snapshot-consistent tables over open file
   formats — Delta/Iceberg-class — on scalable storage)
  └── The catalog
      (tracks tables by name → current table metadata; makes tables
       addressable, discoverable, and permission-checked)
      └── One governed store, multiple workloads
          (SQL analytics + data engineering on the same tables,
           through the platform's own engines and/or external
           engines connecting through open catalog protocols)
```

Everything else the category is known for — managed compute, ingestion pipelines, autonomous table maintenance, fine-grained security policy, data sharing, semantic layers, notebooks, machine-learning tooling, AI assistants — is widespread in current products but is not what makes the platform a lakehouse. Self-managed, on-premises deployments satisfy the same core, and the structure predates the category's name.

The boundary sentence: **the lakehouse holds the data of record as transactional open-format tables; it does not merely store raw files (that is a data lake), does not hold the data of record in its own closed internal format (that is a data warehouse), and does not answer queries over data it never holds (that is data virtualization).**

## Users & Context

Primary users are the technical staff of an organization's data platform, and — unlike most data-platform Types — the *same* store serves them all:

- **Data engineers** build the pipelines that land and transform data: they ingest from operational sources, write tables in the platform's table format, build derived datasets, and keep data flowing on schedule. Their work product is the table layer itself.
- **Analytics engineers** shape the shared, curated tables (business-ready models, metric definitions) that the rest of the organization consumes.
- **Analysts and BI consumers** query the same tables through SQL editors and dashboard tools — usually through a managed SQL surface, without touching storage or pipelines.
- **Data scientists and ML engineers** (where the platform carries them) explore the same tables in notebook environments and build features and models from them.
- **Platform administrators** configure compute (SQL warehouses, processing clusters), manage permissions in the catalog, govern sharing, and watch cost and performance.

Typical scenarios: consolidating a fragmented estate (a legacy warehouse plus scattered lake storage plus team-local extracts) into one governed store; giving analysts warehouse-grade SQL over data that stays in open formats; feeding AI/ML workloads from the same governed tables the reports run on; sharing selected tables with other teams or organizations without copying them.

The work rhythm: engineers and administrators work in build-and-operate cycles (onboard a source, register tables, tune maintenance); analysts work in query-and-explore cycles; and both meet in the catalog — the shared map of what tables exist and who may use them.

## Core Model

### The defining core

Three structures. Remove any one and the product stops being a lakehouse platform:

- **The open-format transactional table store.** The platform's data of record is held as tables with transactional semantics — changes are atomic and consistent, schemas are enforced and can evolve, and the table has versioned states — implemented as an open file format: data files (typically columnar) plus a metadata layer that describes which files make up the table and when. The storage underneath is scalable, typically object storage. Two properties are load-bearing at once: the tables are *transactional* (this is what separates the lakehouse from the data lake, where files are raw and interpreted at read time), and the format is *open* (this is what separates it from the data warehouse, where the store of record is the platform's own internal, compute-coupled format). An open format means other engines — including engines not made by the platform's vendor — can read the same tables.

- **The catalog.** A persistent catalog tracks the tables by name — a table name resolves to that table's current metadata — and is how users and engines address data as *tables* ("query this table", "insert into that table") rather than as file paths. The catalog is also where the platform's governance attaches: permissions are granted on catalog objects, and the catalog is the discovery surface for finding what data exists. In mature products the catalog reaches outward too: external engines connect through open catalog protocols and are granted short-lived, permission-checked access to the same tables. Without the catalog there are only files; a catalog alone, without the table store, is just metadata infrastructure.

- **One governed store, multiple workloads.** The same cataloged tables are served to more than one workload class under a single permission authority: SQL analytics for analysts and BI tools, and data engineering — ingestion and transformation with full read/write table operations — as the constant pair; data science and ML commonly join them. The serving engines may be the platform's own (managed SQL warehouses, distributed processing runtimes, auto-generated SQL endpoints) or external engines connecting over open protocols; either way, permissions and table identity travel across engines, and the workloads do not each get a private copy of the data. Without this leg the product is a single-workload appliance — a query engine over tables, or a table-format storage service — not a lakehouse platform.

### Standard capabilities around the core

Mature products add a consistent layer of machinery that makes the core operable:

- **Managed compute.** The platform operates the processing resources — SQL warehouses for analytics, distributed processing runtimes for engineering — scaled and tuned by the platform rather than by users.
- **Ingestion machinery.** Incremental, repeatable loading from operational databases, files, and streams into lakehouse tables — declarative pipelines, low-code ingestion flows, stream-to-table paths.
- **Table maintenance.** Background optimization of the physical table layer: compacting small files, cleaning up expired snapshots and orphaned files, keeping query performance stable as tables churn. In mature products this is increasingly autonomous.
- **Fine-grained governance.** Row- and column-level restrictions, masking, and tag- or attribute-based policy on top of basic grants — administered in the catalog, enforced wherever a table is read, including by external engines.
- **Data sharing without copy.** Granting other teams, accounts, or external parties access to selected tables through managed sharing protocols or live references — the recipient reads the platform's tables directly rather than receiving a copy.
- **Time travel / table versioning as a user capability.** Because tables are snapshot-versioned, users can query a table as it was, audit what changed, and recover from bad writes.
- **Semantic and BI surfaces.** Shared metric definitions over lakehouse tables, dashboard serving, and catalog-wide search and discovery.

### One structure, many implementations

The core model is written conceptually. Realizations differ on every axis except the core:

```text
Concept:   Open-format transactional table store
Realized as:  one open table format as the platform's native layer ·
              the open Iceberg format as an interop surface on a
              closed-format warehouse · tables in the customer's cloud
              storage account · tables in the vendor-operated lake storage

Concept:   The catalog
Realized as:  a full governance catalog (permissions, lineage, sharing) ·
              an automatic registration/metastore service ·
              an open catalog product implementing a REST protocol ·
              platform-as-catalog with external-catalog integrations

Concept:   One store, multiple workloads
Realized as:  own-engine serving (SQL warehouse + processing runtime) ·
              auto-generated SQL endpoints over the same tables ·
              external engines reading through open catalog protocols ·
              all of the above at once
```

A reader who has only seen one style — say, a managed suite where the platform's own engines do everything — should still recognize a self-managed open-standard deployment (external engines, an open catalog, tables in the customer's own storage) as the same Type from the core model.

## How It Works

A lakehouse platform has one establishment phase and three permanently ongoing loops: bringing data in, serving workloads out, and keeping the table layer healthy.

### Establish the estate

```text
Connect or designate the storage (cloud storage account / managed lake storage)
→ the catalog becomes the table layer of record
→ administrators configure compute (SQL warehouses, processing runtimes)
→ grant initial permissions
```

From this point, tables registered in the catalog are the governed estate — wherever their files physically live.

### Bring data in and make it tables

```text
Configure ingestion from a source (database, files, stream)
→ data lands as lakehouse tables in the open table format
→ (in some products: files land first, and placing/declaring them
   in the tables area triggers validation, metadata extraction,
   and registration in the catalog)
→ derived tables are built by transformation jobs reading and
   writing other tables — full read/write table operations
```

The characteristic act is **writing tables, not landing files**: ingestion and transformation produce governed, transactional tables from the start. Raw, non-table files can live alongside (and many estates keep a raw zone), but they sit outside the SQL surface until converted into the table format.

### Serve the workloads

```text
An analyst submits SQL / opens a dashboard
→ the platform's SQL layer resolves the tables through the catalog
→ permissions are checked on the catalog objects
→ the engine reads the table (its current snapshot) and returns results

An engineer runs a transformation job
→ same catalog resolution, same permission check
→ the job reads and writes tables transactionally
→ downstream tables update atomically
```

This loop — **many workloads, one catalog, one permission authority** — is the defining interaction of the Type. The same table can be the source of a transformation job, a dashboard, an ML training set, and an externally connected engine's read, all under the same identity and permissions.

### Share and federate

```text
Grant a team/account/external party access to selected tables
→ recipients read the platform's tables through the sharing protocol
  or a live reference — no copy changes hands
→ where sources outside the store matter, the platform may query
  external databases in place without ingesting them (product-dependent)
```

### Maintain

```text
Tables accumulate new versions and small files as they churn
→ the platform compacts, expires old snapshots, cleans orphaned files
→ schemas evolve as sources change (add/reshape columns without rewrites)
→ bad writes are recovered by restoring a prior table state
→ cost and usage are reviewed through the platform's monitoring
```

### Defining core, standard, and optional, at a glance

**Defining core** — without these, not this Type:

- open-format transactional table store as the data of record
- the catalog making those tables addressable and governed
- one governed store serving multiple workload classes

**Standard capabilities** — present in most mature products:

- managed compute (SQL warehouses, processing runtimes)
- ingestion machinery (incremental pipelines, stream-to-table)
- autonomous table maintenance (compaction, snapshot expiry)
- fine-grained governance (row/column policy, masking, tags)
- no-copy sharing of selected tables
- time travel / versioned table states as a user capability
- semantic layers and dashboard serving over the tables

**Optional / variant** — depends on product philosophy and customer scale:

- notebook workbenches and data-science/ML machinery
- federation of external databases queried in place
- real-time/event analytics endpoints alongside SQL
- transactional (operational) database components
- agentic/natural-language interfaces
- deployment posture: fully managed SaaS vs self-managed software; vendor-operated vs customer-owned storage; single-format native vs multi-format interop

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Catalog explorer

The estate's map, and the anchor surface for both governance and discovery.

- browsable hierarchy of catalogs/schemas/tables with schema details and table properties
- search and discovery across tables; classification and documentation on objects
- primary actions: browse, search, inspect a table's schema and history, register or convert tables, tag and document

### Notebook workspace

Where engineers and data scientists work when the platform carries them (product-dependent).

- code cells (SQL and general-purpose languages) attached to the estate's tables; embedded visualizations
- primary actions: explore data, develop transformation logic, promote it to scheduled jobs

### SQL editor

The analysts' surface.

- query authoring against cataloged tables, result grids, saved queries
- primary actions: run queries, explore results, build visualizations, share query assets

### Ingestion and pipeline configuration

Where data enters.

- source connections; pipeline definitions with schedules and dependencies; ingestion status
- primary actions: create/edit pipelines, run now, schedule, inspect what landed and what failed

### Permission and sharing administration

Where governance happens.

- principals and their grants on catalog objects; policy rules (row/column, tags); sharing grants to other accounts
- primary actions: grant/revoke, define policies, set up sharing recipients, review audit trails

### Compute administration

- SQL warehouses and processing runtimes: sizes, scaling, auto-stop
- primary actions: create/resize/stop compute, review usage and cost

### Monitoring and maintenance

- table health (file counts, snapshot growth), maintenance runs, query performance, lineage
- primary actions: review anomalies, trigger or verify maintenance, trace lineage

## Important Rules / Behaviors

### The open format is a contract, not a detail

Because the store of record is open-format, the platform's own engines are not the only readers of its data. Mature platforms treat this as a feature: external engines connect through open catalog protocols and read (in some cases write) the same tables, under the catalog's permissions. The corollary is also structural: a platform that required its own proprietary runtime to read its own tables would contradict the Type.

### Tables, not files, are the governed surface

Files live in storage; tables live in the catalog. A file that is not part of a registered table is invisible to the SQL surface and outside the permission model's table-level rules — in one sampled platform, only tables in the platform's open table format appear through the SQL endpoint, and other formats must be converted first. Registration (and keeping registration truthful as files change) is standing work.

### Table state is versioned

Every change to a table produces a new versioned state; readers see a consistent snapshot, and concurrent readers and writers do not corrupt each other. This is what makes the store safely shared by multiple workload classes, and it is also the basis of time travel and recovery. Versioning has a cost: snapshots and superseded files accumulate, which is why maintenance (compaction, expiry, cleanup) is a standing operational duty rather than an optional extra.

### One permission authority over all engines

Permissions attach to catalog objects and are enforced wherever a table is read — the platform's own engines and external engines alike. In mature deployments an external engine is issued short-lived, scoped access at request time rather than holding standing credentials. This is what allows the "many workloads, one store" promise to coexist with governance.

### The store of record is held, not merely referenced

The platform holds the data of record: its tables are the authoritative copies organizations operate on. This distinguishes it from layers that only describe or only borrow data. Where the platform does reference outside data (live references to external sources, federation of external databases), those are additions to the core, not the store of record itself.

### Storage location is a variant axis, not a constant

In some products the table files sit in the customer's own cloud storage account (the platform manages table state there); in others the platform operates the lake storage itself. Both satisfy the core; what is invariant is the open format and the table semantics, not who owns the bucket.

## Variants

Common realizations of the Type:

- **Platform-native multi-workload suite** — the platform's own engines serve every workload class over its native open table format; governance, sharing, ML tooling, and BI surfaces all bundled. The fullest expression of the Type.
- **SaaS analytics suite with the lakehouse at its center** — the lakehouse is one item in a broader suite (alongside warehouses, pipelines, dashboards) sharing one lake substrate and one governance model.
- **Open-standard, engine-led platform** — a query engine plus an open catalog over tables in the customer's own storage, built on community-driven table formats; the deployment spans fully managed cloud service, self-managed software on Kubernetes or on-premises, and free editions.
- **Warehouse with an open-format interop surface** — a closed-format warehouse that also operates on open-format tables in external storage and serves them to external engines through open catalog protocols; the boundary-drift realization, converging on the lakehouse core from the warehouse side.
- **Self-managed / open-source stacks** — open table formats plus an open catalog plus attached engines, operated by the organization; the non-cloud and pre-term lineage of the same structure.

A variant remains a variant unless it changes the core: a product whose tables are not transactional presents as a data lake platform; a product whose store of record is its own closed format presents as a data warehouse; a product that holds no store of record presents as data virtualization; a product that serves only one workload class over its tables is a query engine or table service, not a platform.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Data Warehouse Platform | the warehouse's store of record is its own modeled, internally-optimized format and its center is governed SQL analytics; the lakehouse's store of record is open-format transactional tables and its center is multi-workload unity. Converging market: warehouses adopt open-format tables, lakehouses add warehouse-grade SQL — the store-of-record/centerpiece discriminator, not feature presence, keeps them distinct |
| Data Lake Platform | the lake holds raw, schema-on-read data at original fidelity with governance and multi-engine access; the transactional table layer is its optional upgrade. The lakehouse is that upgrade made the centerpiece |
| Data Virtualization Platform | answers queries over data it never holds, with no persistent copy; the lakehouse holds the data of record. Some lakehouse products ship federation (query external databases in place) — an addition, not the core |
| Data Catalog | describes assets living in systems it does not own; the lakehouse catalog is internal machinery over the platform's own tables — though mature lakehouse catalogs also serve external engines, the service direction distinguishes them |
| Data Science Workbench | interactive code sessions for data scientists; the lakehouse *hosts* such sessions as an optional module, and a lakehouse remains one without any workbench |
| Machine Learning Platform / Feature Store / Model Registry | lifecycle machinery around models and features; the lakehouse may carry these as modules, but the model lifecycle is not what makes it a lakehouse |
| Data Exchange Platform | entitlement-centered distribution of datasets between organizations; lakehouse sharing is a capability that delivers tables to recipients, not a marketplace of record |
| Data Fabric Platform | an estate-spanning management layer over many systems the fabric does not own; the lakehouse holds its own store of record. A suite product carrying the fabric name in the market belongs to this leaf, not the fabric Type |
| Business Intelligence Platform | governed analytics content for business consumers; lakehouse dashboards and metric views serve BI from the tables but the BI content lifecycle is downstream |

The two most important boundaries: against the **data warehouse** (what is the store of record — closed modeled store vs open-format transactional tables) and against the **data lake** (are transactional tables the centerpiece or an optional layer). Both seams run through a market that is actively converging from both sides, and both are documented from the neighboring passes as well as this one.

## Representative Products

- Databricks — platform-native multi-workload suite; the vendor behind one of the open table formats and the popularizer of the category
- Microsoft Fabric — SaaS analytics suite whose lakehouse item is the suite's data-engineering center, on a shared lake substrate with its warehouse
- Dremio — open-standard lakehouse platform (query engine + open catalog over open table formats in customer storage), spanning managed-cloud and self-managed deployments
- Snowflake — included as the boundary-drift pole: a warehouse platform operating open-format tables in external storage and serving them to external engines through open catalog protocols

The definition was checked against the pre-term lineage (shared-metastore, open-file-format analytical estates with table-level transactions and multiple engines) and against self-managed/non-cloud deployments, to avoid defining the Type by the current managed-cloud pattern.

## Sources

Research date: **2026-09-08**

- Databricks — "What is Databricks?" (documentation) — https://docs.databricks.com/aws/en/introduction/index.html
- Microsoft — "What is a lakehouse? - Microsoft Fabric" (Microsoft Learn) — https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview
- Dremio — "What is Dremio?" and documentation home — https://docs.dremio.com/current/what-is-dremio/ , https://docs.dremio.com/current/
- Dremio — platform overview (product page) — https://www.dremio.com/platform/
- Snowflake — "Apache Iceberg™ tables" (documentation) — https://docs.snowflake.com/en/user-guide/tables-iceberg
- Apache Iceberg — "Terms" (project documentation) — https://iceberg.apache.org/terms/

Paired sibling documents consulted for boundary alignment: Data Lake Platform and Data Warehouse Platform application documents and research notes; boundary flags recorded in the production status from the data-virtualization, data-fabric, data-exchange, data-science-workbench, and feature-store passes.

> Sourcing note: all primary sources were fetched successfully on the research date. Precise operational parameters (service limits, file-size targets, retention defaults, region availability) documented in those sources are intentionally not restated here; they remain in the paired Research Notes. The historical check is structural inference from the documented open-standard concepts and the neighboring lake-platform research, not from fetched legacy documentation.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, the abstraction-level analysis, and the full boundary analysis against the neighboring data-platform Types are recorded in the paired Research Notes.
