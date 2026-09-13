# Data Lake Platform

## Overview

A **Data Lake Platform** is the management layer over a centralized store of raw analytical data. It holds an organization's analytical data as files or objects in open or native formats at original fidelity — data is stored first and interpreted when read, not conformed to a predefined schema when written — and it wraps that store in the machinery that makes it usable as a shared organizational resource: a persistent metadata catalog that organizes the files into structured, addressable objects, platform-enforced access governance, and a serving layer through which multiple processing engines and consumers read and process the same stored data.

The problem it exists to solve is the economics and the risk of analytical data at scale. Organizations accumulate far more data than they can model up front — logs, event streams, sensor output, application exports, documents, third-party files — and modeling all of it at ingest (the data-warehouse discipline) is expensive and premature. The data lake inverts this: keep everything, cheaply, in its original form, and decide later what it means. What turns that inversion from a liability ("a swamp of unfindable files") into an asset is the platform layer: without a catalog the store is unfindable, without governance it is unsafe, and without a serving layer it is inert.

The defining structure is small:

```text
The lake store
  (centralized files/objects in open or native formats, original fidelity, schema-on-read)
  └── The catalog / organization layer
      (persistent metadata: databases, tables, hierarchies over the files)
      └── Governed multi-engine access
          (platform-enforced permissions; many engines, one store)
```

Everything else commonly associated with the category — ingestion pipelines, tag-based policy at scale, lineage, data sharing, transactional table formats, AI-era governance — is standard capability or variant, not what makes the product a data lake platform. Older, non-cloud, self-managed lake stacks satisfy the same core with none of the modern additions.

The boundary sentence: **the platform holds the data at rest and governs it; it does not model the data at write, and it does not own the engines that process it.** A product that models data into a predefined schema in its own managed store is a data warehouse; a product that only moves data between systems is a data integration platform; a product that only describes data living elsewhere is a data catalog.

## Users & Context

Primary users are technical, spanning both sides of the store:

- **Data engineers** fill and organize the lake: they build ingestion from sources, register schemas into the catalog, lay out the estate (which data lands where, in what structure), and keep raw and processed data coherently arranged.
- **Data platform administrators / stewards** govern the estate: they manage the catalog, grant and revoke permissions, classify sensitive data, review audit trails, and manage storage locations and lifecycle.
- **Analysts, data scientists, and ML engineers** are the consumption side: they rarely administer the lake; they query and process it through whatever engines the organization has attached to it.
- **Governance / security stakeholders** (in larger organizations) set policy that the platform's permission and audit machinery must express.

Typical scenarios: consolidating scattered data sources into one analytical store; keeping raw history at low cost while curated views are built on top; giving many teams access to the same data without each team holding its own copy; feeding analytics, machine learning, and AI workloads from one governed source.

The work rhythm differs by role. Engineers and administrators work in build-and-maintain cycles — onboarding a source, restructuring a zone, reviewing permissions. Consumers work in query-and-explore cycles through engines, usually without touching the lake's own interfaces at all: for them the lake is simply where the data lives.

## Core Model

### The defining core

Three structures. Remove any one and the product stops being a data lake platform:

- **The lake store.** A centralized, scalable store holding the organization's analytical data as files or objects in open or native formats, at original fidelity. The store's defining property is *schema-on-read*: data lands in whatever form it arrives, and structure is applied when the data is read, not when it is written. The store typically holds both raw and transformed data side by side — the original landing of a source and the processed derivatives built from it. Storage is deliberately cheap and built to scale well beyond modeled warehouse estates, because the lake's contract is "keep everything first, decide later". Without this property — if data must be conformed to a schema before it can be stored — the product is a data warehouse, not a lake.

- **The catalog / organization layer.** A persistent metadata layer that organizes the stored files into structured, addressable objects — databases, tables, schemas, partitions, or equivalent hierarchies — each carrying schema information and location information pointing into the store. The catalog is what makes a pile of files into an estate: it is how engines and users address data as *data* ("this table in this database") rather than as paths. It is also the anchor for discovery: users search and browse the catalog to find what exists. Without this layer the product is object storage with a console.

- **Governed multi-engine access.** The platform controls who can access which stored data, and it serves the store to multiple processing engines and consumers through that access layer. Permissions are enforced at the platform level — in mature products with fine granularity (down to columns, rows, or individual files/directories) and with policy mechanisms that scale across thousands of objects — and access is auditable. The same stored data is readable by several different engines and tools; no single engine owns the store. Without governance the store is an ungoverned swamp; without engine openness it is a single-engine appliance — either way, no longer this Type.

### Standard capabilities around the core

Mature products add a consistent set of machinery that makes the core operable:

- **Ingestion machinery.** Template-driven or pipeline-driven loading of data into the lake — bulk import from databases and files, incremental loading, scheduled workflows that land, crawl, and register data. Ingestion ends at the lake's edge: the platform fills the store and catalog; deeper transformation is typically done by engines working on the lake.
- **Fine-grained, scalable permission policy.** Beyond basic grants: column-, row-, and cell-level restrictions; tag- or attribute-based policies that replace thousands of per-object rules with a few labels; directory/file-level access lists where governance reaches into the store itself.
- **Discovery and classification.** Search and browse over the catalog; automatic or manual tagging of sensitive data so policy can reference it.
- **Lineage and audit.** Records of who accessed what, when, and through which engine; tracking of how data assets derive from one another.
- **Data sharing.** Granting other teams, accounts, or external parties access to parts of the estate without copying it — cross-account grants, managed sharing protocols, or licensed distribution.
- **Storage lifecycle and cost machinery.** Tiering, lifecycle rules, and retention management at the store layer, where the underlying storage service exposes them — the lake's economics are part of its value.
- **Schema evolution handling.** Sources change; the catalog's descriptions must be refreshed (re-crawled, re-registered) or updated to stay truthful about what is in the store.

### One structure, many implementations

The core model is written conceptually; the Variants section below enumerates how realizations differ.

```text
Concept:   The lake store
Realized as:  commodity object storage with a namespace · a managed storage service ·
              a distributed file system · cloud object storage in the customer's account

Concept:   The catalog
Realized as:  a shared metastore service · a managed metadata service ·
              a governance catalog with catalog/schema/table hierarchy

Concept:   Governed access
Realized as:  grant/revoke permission models · directory/file ACLs ·
              tag/attribute-based policy · policy engines bolted onto the store
```

A reader who has only seen one style — say, a managed governance service over commodity buckets — should still recognize a self-managed open-source stack, or a storage service plus a separate analytics service, as the same Type from the core model.

## How It Works

A data lake platform has one establishment phase and a permanently ongoing operate phase.

### Establish the lake

```text
Provision or designate the store (buckets / file system / storage account)
→ register the storage locations with the platform
→ create the catalog (or connect to the organization's existing metastore)
→ designate administrators who may grant access
```

From this point, the registered locations are the lake: data written there is under the platform's governance, and data addressed through the catalog resolves to those locations.

### Ingest and organize

```text
Configure ingestion from a source (database, files, stream)
→ data lands in the store in its native form
→ schema is extracted and registered in the catalog (crawl / register)
→ the estate is arranged: databases, tables, zones for raw vs processed data
→ sensitive content is classified and tagged
```

The characteristic act of lake ingestion is *landing without modeling*: the source's shape is preserved, and the catalog records what landed and where. Processed derivatives are written back into the same store as new data, alongside — never instead of — the raw original.

### Govern

```text
Define permission policy (who may read which databases/tables/columns/rows)
→ grant to users, groups, or engine service identities
→ policy scales via tags/attributes where object counts are large
→ access attempts are checked at the platform layer and logged for audit
```

Governance is continuous, not a setup step: as the estate grows, permissions, classifications, and reviews accumulate alongside the data.

### Serve

```text
A user submits a query or job to an engine
→ the engine resolves the referenced tables through the catalog
→ the platform checks the user's permissions on those catalog objects
→ if authorized, the engine obtains access to the underlying files —
   commonly as short-lived, scoped access issued for the request
→ the engine reads the store directly and applies any row/column filtering
→ results return to the user; the access is recorded
```

This is the interaction loop that defines the Type: **many engines, one store, one permission authority.** The engines do the computation; the platform does the addressing and the gating. Different engines — SQL query engines, distributed data-processing engines, machine learning tooling, specialized analytics runtimes — can be attached to the same lake, and a user's permissions travel with them across engines.

### Maintain

```text
Watch audit and access patterns
→ absorb source changes (re-crawl, re-register, update schemas)
→ onboard new sources; restructure zones as needs mature
→ review and adjust permissions; manage lifecycle and storage cost
→ (optionally) upgrade parts of the estate to transactional tables
```

### Defining core, standard, and optional, at a glance

**Defining core** — without these, not this Type:

- centralized raw-format store (schema-on-read, original fidelity)
- persistent catalog organizing the store into addressable data objects
- governed multi-engine access (platform-enforced permissions; many engines, one store)

**Standard capabilities** — present in most mature products:

- ingestion machinery (templates/workflows/pipelines, bulk + incremental)
- fine-grained and scalable permission policy (column/row granularity, tag/attribute policy)
- discovery/search over the catalog; classification/tagging
- lineage and audit
- data sharing across teams/accounts
- storage lifecycle and cost management
- schema evolution handling

**Optional / variant** — depends on segment, era, deployment:

- transactional table formats with ACID semantics (the lakehouse upgrade path)
- managed vs external tables (whether the platform also owns the files' lifecycle)
- federation of external sources into the catalog without migration
- external data distribution/monetization
- specialized engines (log/time-series) attached alongside SQL and general-purpose processing
- AI-era additions: AI-asset governance, semantic/metric layers, natural-language exploration

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Catalog explorer

The estate's map, and the primary surface for understanding what the lake contains.

- browsable hierarchy of databases, tables, schemas, and their locations; schema details per table
- search across the catalog; tags and classifications on objects
- primary actions: browse, search, inspect schema and location, create/alter catalog objects, tag

### Permission administration

Where governance happens.

- list of principals and their grants on catalog objects (and storage locations)
- policy definition: per-object grants, tag/attribute-based rules, row/column filters
- primary actions: grant, revoke, define policy, review effective access, inspect audit history

### Ingestion configuration

Where data enters.

- source connection setup; ingestion templates or pipeline definitions; schedules
- crawl/registration results: what was discovered, what schemas were recorded
- primary actions: create/edit ingestion, run now, schedule, review what landed

### Engine workspaces

The consumers' surfaces — technically part of attached engines rather than the lake itself, but operationally inseparable from the Type, since most daily interaction with lake data happens here.

- SQL editors, notebook environments, job consoles pointed at the lake
- primary actions: query, explore, build pipelines and models against cataloged data

### Monitoring and audit

- access history (who accessed what, when, via which engine); lineage views; storage metrics
- primary actions: filter, investigate access, trace lineage, review anomalies

### Storage administration

- registered locations, lifecycle and tiering rules, capacity and cost views
- primary actions: register location, set lifecycle policy, review usage

## Important Rules / Behaviors

### The catalog describes; the files remain

The catalog's table definitions are descriptions of data that lives independently in the store. If files change underneath — new layouts, new partitions, removed objects — the catalog's description drifts out of truth until it is refreshed. Registration and re-crawling are therefore standing maintenance, not one-time setup.

### Permissions attach to catalog objects, and reach the store

The permission model's power comes from its position: users are granted (or denied) *data objects*, and the platform translates that into access to the underlying files only at the moment an authorized engine needs them — typically by issuing short-lived, scoped access rather than permanent credentials. This is why the platform, not the storage layer's native policy, is the authority: in mature deployments the storage-level permission machinery is subordinated to (or replaced by) the platform's model.

### Raw fidelity is preserved

The lake keeps the original landing of ingested data. Cleaning, joining, and reshaping produce *new* data in the same store; they do not overwrite the source of record. Re-processing from raw is always possible, which is precisely the lake's value proposition — and the reason its storage bill is the price of that option.

### The platform is a system of rest, not of movement

Data lives here. Unlike integration platforms — custodians of data in transit — the lake platform is the custodian of the estate itself: deleting the platform or a registered location deletes (or orphans) the data. Conversely, the lake is the typical *destination* of integration pipelines and the typical *source* for warehouses, marts, and ML systems.

### No engine owns the store

The store's openness is structural: formats are open or native, and access paths are shared. An engine that could only read the lake through its own proprietary runtime would contradict the Type. In practice this is what allows engines to be added, replaced, and run side by side as the organization's tooling evolves.

### Governance scales by abstraction

Fine-grained per-object permissions do not survive thousands of tables. Mature products therefore add a second, coarser policy mechanism — tags or attributes attached to objects, with rules expressed against the tags — so that policy can be written once and applied across the estate. The two mechanisms coexist: explicit grants for exceptions, attribute policy for breadth.

## Variants

Common realizations of the Type:

- **Managed governance service over commodity storage** — the store is a generic cloud object storage service; the platform product contributes the catalog, the permission model, ingestion templates, and engine integration. The purest expression of "the platform is the management layer".
- **Storage-service-first split** — the lake store ships as a storage capability (hierarchical namespace, file-level access control, access designed for distributed analytics frameworks) and the serving/ingestion layer ships as a separate analytics service; together they realize the core, separately each is only half of it.
- **Platform-native suite** — one vendor platform spans the store (in the customer's cloud account, in open formats), the catalog/governance layer, and the engines. These products have largely evolved into **lakehouse** positioning by making transactional tables their centerpiece; they remain instructive boundary cases for this Type.
- **Open-source self-managed stack** — a distributed file system plus a shared metastore plus policy/lineage engines plus whatever processing engines the organization attaches; the historical baseline of the Type and still the substrate under several commercial products.
- **Enterprise / hybrid deployments** — the same core realized on-premises or across cloud and on-prem storage, typically by the same open-source lineage; documentation evidence for this pole is thinner (see Sources).

A variant remains a variant unless it changes the core: a product whose store enforces schema-at-write is a warehouse; a product whose centerpiece is transactional warehouse-grade tables presents as a lakehouse; a product with no catalog or no governance is storage, not a platform.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Data Warehouse Platform | models data at write into its own managed, compute-coupled structures, optimized for governed SQL analytics; the lake stores raw in open formats and leaves modeling to read time |
| Lakehouse Platform | a lake whose files have been upgraded to transactional (ACID) tables with warehouse-grade SQL and management on top; the closest sibling — the seam is whether transactional tables are the centerpiece or an optional layer |
| Object Storage / Storage Management | holds bytes with namespaces and access control but no data catalog, no data-level permission model, no engine serving; the lake platform is precisely the management layer added above it |
| Data Integration Platform | custodian of data *movement* between systems, holds no data at rest; its pipelines typically *fill* the lake |
| Data Catalog | describes assets living in systems it does not own; the lake platform's catalog is internal machinery over data the platform itself holds |
| Data Virtualization Platform | answers queries without physically copying data; the lake is defined by physically holding the copies |
| Data Fabric Platform | estate-spanning metadata/governance layer over distributed systems; the lake is one physical store with its own governance |
| Business Intelligence Platform | downstream consumer; reads what the lake (via engines) supplies and holds no part of the estate |
| Data Quality / Data Governance Platforms | provide quality and policy machinery as standalone products; the lake platform embeds a working subset of both for its own estate |

The two most important boundaries: against the **data warehouse** (schema timing, format openness, compute coupling — the fork that created the lake in the first place) and against the **lakehouse** (whether transactional tables are the point of the product or an optional upgrade). Both seams involve directory leaves that are documented separately; the descriptions here are one-sided and flagged for joint review.

## Representative Products

- AWS Lake Formation — managed governance service over Amazon S3 and a shared metadata catalog
- Microsoft Azure Data Lake Storage (with Azure Synapse Analytics) — lake storage capability plus multi-engine analytics service
- Databricks — platform-native suite; self-identifies as a lakehouse platform and is included as the boundary case showing where the lake platform's evolution points
- Apache Hive / Hive Metastore — the open-source historical substrate; included as the historical baseline

The definition was checked against the Hadoop-era lake pattern (distributed file system + shared metastore + policy engines + multiple engines) to avoid over-fitting to the modern cloud-object-storage pattern: it satisfies the same core with no cloud, no object storage, and no modern table formats.

## Sources

Research date: **2026-09-07**

- AWS — Lake Formation Developer Guide: "What is AWS Lake Formation?", "How it works", "Lake Formation terminology" — https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html , https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html , https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works-terminology.html
- Databricks — Documentation: "What is Databricks?", "What is Unity Catalog?" — https://docs.databricks.com/aws/en/introduction/index.html , https://docs.databricks.com/aws/en/data-governance/unity-catalog/index.html
- Microsoft — "Azure Data Lake Storage overview" — https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction
- Microsoft — "What is Azure Synapse Analytics?" — https://learn.microsoft.com/en-us/azure/synapse-analytics/overview-what-is
- Apache Hive — project documentation home (metastore positioning, security integrations, storage support) — https://hive.apache.org/

> Sourcing limitation: official documentation for Cloudera's data platform (docs.cloudera.com) was not reachable (repeated 404s), and Google's BigLake documentation timed out repeatedly; both were abandoned rather than retried. The enterprise/hybrid on-premises pole and multi-cloud governance layers are therefore covered only indirectly, via the open-source substrate that historically underpins them, and no claims specific to those vendors are made in this document. Precise operational details (permission-evaluation semantics, service limits, regional availability) are intentionally not stated; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against the neighboring data-platform Types are recorded in the paired Research Notes.
