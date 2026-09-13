# Metadata Management Platform

## Overview

A **Metadata Management Platform** is the system of record for an organization's metadata: it holds descriptions of the organization's data assets in one central store, collects those descriptions from the systems where the data actually lives, and serves them back out — to people who need to find and understand data, and to machines (other tools, automation, AI agents) that need the same context programmatically.

The problem it solves is scattering. A mid-sized or large organization's data estate spans warehouses, lakes, databases, BI tools, transformation pipelines, and SaaS applications. Every one of those systems knows something about its own piece — schemas, tables, dashboards, jobs — but nothing knows how the pieces connect. A metadata management platform is where the descriptions of all of those pieces are brought together into one maintained, cross-system picture.

The defining core is small:

```text
Central metadata store of record (descriptions ABOUT data — not the data)
└── Collection machinery bound to the sources (keeps the store current)
    └── Served metadata layer (to people AND to machines)
```

Everything else that modern products pile on — catalog search experiences, business glossaries, lineage views, classification, governance workflows, data quality, data marketplaces, AI assistants — enriches this core or ships as an application on top of it. The platform itself never holds or moves the data it describes; it holds the knowledge about the data.

## Users & Context

Primary users:

- **data engineers and platform teams** — connect sources, operate collection (scans, agents, ingestion), keep the estate mapped as pipelines and warehouses change
- **data stewards and governance leads** — enrich records with business meaning: descriptions, glossary terms, classifications, ownership; maintain the vocabulary the organization uses for its data
- **analysts and data scientists (consumers)** — search the estate, read an asset's meaning and lineage, judge whether a table or dashboard can be trusted before using it

Secondary users:

- **administrators** — manage connections, collection scheduling, permissions, and the metadata model itself
- **integration developers and, increasingly, automated agents** — consume metadata through APIs and interchange interfaces to power other tools and AI applications

The work environment is the enterprise data platform: the application runs as a service (cloud, self-hosted, or on-premises components) that sits across the whole estate rather than inside any one system. Most interaction happens in bursts — connecting a new source, cataloging a new domain, resolving what a column means, answering "where does this number come from" — rather than in long continuous sessions.

## Core Model

### The metadata record (asset)

The central object is the **metadata record** — commonly called an asset. One record stands for one thing in the estate: a database or warehouse, a schema, a table, a column, a BI dashboard, a report, an ETL job, an ML model, a glossary term. The record is individually addressable, persists over time, and accumulates:

- **technical metadata** — what the source system reports: schema, data types, columns, row counts, the definition of a job or dashboard
- **business metadata** — what people and policies add: descriptions, glossary terms, business names, tags
- **operational metadata** — what happens to the data: run statuses, execution times, freshness signals
- **relationship metadata** — how the record connects to others: ownership, stewardship, parent/child structure, lineage, glossary bindings

A mature product carries records across many asset classes and keeps them in a typed structure: each record has a type (table, dashboard, pipeline…), defined attributes for that type, and defined kinds of relationships it can hold. Some products make this model deeply configurable — organizations define their own asset types, attributes, and relationship kinds as part of setting the platform up — while others ship a fixed system model with limited extension. Both realizations are this Type; the configurability is a maturity and packaging variable, not the definition.

### The store of record

The records live in one repository that the platform owns and operates — the authoritative place where the organization's cross-system metadata accumulates. Two properties matter:

- **Descriptive only.** The platform never holds the data itself. A table record describes the table; the rows stay in the warehouse. This is the load-bearing "about, not is" property.
- **Cross-source by design.** The store exists precisely because the estate spans many systems. A single engine's schema browser or a lakehouse's internal catalog serves one platform; the metadata store exists to unify across all of them.

Mature products commonly hold this store as a graph — records as nodes, relationships as edges — because most questions users ask ("what feeds this table?", "who owns everything downstream of this dashboard?") are graph questions.

### Collection machinery

The store is fed by machinery bound to the sources, and this is what separates *management* from a hand-built register:

- **connectors / crawlers / scanners** — scheduled jobs that connect to a warehouse, BI tool, or pipeline system and extract its metadata (schemas, datasets, dashboards, jobs)
- **on-site agents** — for sources that cannot be reached from the cloud, a small deployable component runs inside the organization's network, processes source information locally, and sends only the extracted metadata to the platform (this is also how data-residency requirements are met)
- **embedded hooks** — capture components installed in the systems themselves that report metadata (especially lineage) as work happens
- **API ingestion** — external tools and pipelines push metadata in directly, including, in some products, metadata from *other* metadata platforms

Collection runs repeatedly. Sources change constantly — tables are added, dashboards rebuilt, jobs rewritten — so the machinery re-harvests on a schedule to keep the store synchronized with reality.

### The served metadata layer

The store's content is put to use on two fronts:

- **To people** — search and discovery over the estate: find assets by name, term, owner, tag, or certification; read an asset's full context (structure, meaning, lineage, quality signals, who owns it). This is the surface most people think of as "the catalog."
- **To machines** — APIs, exports, and event streams that let other systems consume the same metadata: governance tools reading classifications, BI tools embedding context next to a chart, data platforms building automation on top, and AI agents retrieving governed context about the estate.

The second front is what makes this a *platform* rather than a documentation site: the same records power many applications, which is why vendors ship catalogs, governance programs, quality modules, and marketplaces as applications over one shared store.

### Concept vs implementation

```text
Concept:                          Common implementations:
metadata record (asset)           typed entity, JSON-schema model, graph node
collection machinery              crawlers/scanners, on-site agents, embedded hooks, API push
relationship structure            graph edges, typed relations, lineage events
machine serving                   REST APIs, SDKs, event streams, agent/interchange protocols
human serving                     catalog search UI, asset pages, embedded context in BI tools
```

A reader who has only seen one packaging (say, a cloud governance suite) should still be able to recognize the others — an open-source framework with hooks and a REST store, or a separately-licensed metadata foundation beneath a catalog product — as the same Type.

## How It Works

Three loops run continuously, plus the synchronization behavior that holds them together.

### Loop 1 — Connect and collect

```text
Register a source system
→ provide credentials / deploy an on-site agent where needed
→ configure what to extract (schemas, dashboards, pipelines, usage)
→ run collection (on schedule or on demand)
→ platform creates/updates metadata records for what it found
```

This is the operational entry point for administrators and data engineers. The first full collection over a new source is usually the moment the platform becomes useful: the estate suddenly has a map.

### Loop 2 — Enrich and organize

```text
Open a record (or a batch of records)
→ add descriptions, glossary terms, ownership, tags
→ classify sensitivity where policy requires it
→ certify or endorse records that can be trusted
→ organize records into domains, projects, or terms
```

Stewards and domain experts do this work. Enrichment is the difference between a machine-readable inventory and an actually usable one: harvested metadata says what a table *is*; human enrichment says what it *means* and whether it can be trusted. Mature products also automate part of this — rules that apply tags or terms to matching records, and promotion of descriptions written in source systems up into the platform.

### Loop 3 — Consume

People:

```text
Search or browse the estate
→ open an asset's record
→ read structure, meaning, lineage, quality, ownership
→ decide: use it, request access, or keep looking
```

Machines:

```text
Call the API / subscribe to events
→ query records, relationships, classifications
→ feed the result into another tool, workflow, or AI agent
```

Consumption is the platform's reason to exist: the loops above are only worth running because the records get used — by analysts before they query, by engineers before they change a pipeline, by governance processes, and by automated systems that need the same context.

### The synchronization behavior underneath

Collection and enrichment must coexist, and mature products keep them from colliding: metadata harvested from sources is distinguished from metadata added by people, so that re-running a scan updates technical facts without erasing descriptions, tags, and ownership that humans contributed. How each product reconciles a conflict (source value vs platform value) varies; the separation itself is structural. Identity resolution — recognizing that a re-harvested table is the same table as yesterday — is what makes records persistent objects rather than a stream of snapshots.

### Core vs standard vs optional capabilities

**Defining core** — without these, not this Type:

- central metadata store of record for cross-system data assets
- collection machinery keeping the store current from its sources
- serving to people (discovery/understanding) and to machines (APIs/interchange)

**Standard capabilities** — present in essentially all mature products:

- typed metadata model with asset classes and relationship kinds
- lineage as a first-class relationship with a visual traversal surface
- business glossary / terms as a first-class record class
- classification and tags (including sensitivity labeling)
- ownership and stewardship attributes on records
- search-and-discovery experience over the estate
- admin surface for connections, collection scheduling, and permissions
- enrichment automation (rules, playbooks, promotion from sources)

**Optional / advanced** — depends on packaging, segment, and era:

- governance-program machinery (policy objects, workflows, certification processes, issue tracking)
- data quality and observability modules
- data contracts; data products and marketplace surfaces
- AI assistants and agent endpoints over the metadata
- deeply configurable metamodels; metadata-to-metadata ingestion; federated deployment with on-site processing

## Interfaces

Conceptual surfaces; exact names and layouts vary by product.

### Catalog / search experience

The primary human entry point.

- Purpose: find and understand data across the estate.
- Typical information: result list with asset type, name, owner, certification and classification signals; filters by type, domain, tag, owner.
- Primary actions: search, filter, open a record, save views.

### Asset detail page

The record's full context surface.

- Purpose: answer "what is this, what does it mean, can I trust it" for one asset.
- Typical information: schema or structure, description, glossary terms, tags/classifications, owner and stewards, lineage, quality or freshness signals, related assets.
- Primary actions: edit descriptions/terms, attach tags, assign ownership, view lineage, start an access or issue request (where offered).

### Lineage view

The graph traversal surface for the flow relationship.

- Purpose: see where an asset's data comes from and where it goes; assess impact before changes.
- Typical information: upstream/downstream graph across systems, down to column depth in mature products.
- Primary actions: navigate hops, filter, drill into a node's record.

### Glossary / terms workspace

The semantic layer surface.

- Purpose: build the shared business vocabulary and bind it to technical assets.
- Typical information: term hierarchy, definitions, linked assets, stewards.
- Primary actions: create/edit terms, link assets, assign stewards.

### Administration console

The operator surface.

- Purpose: run the platform.
- Typical information: connected sources and their collection status, scan schedules, agent health, users and roles, model/type configuration.
- Primary actions: add/edit connections, schedule collection, manage permissions, configure the metadata model (where configurable).

### Programmatic interface

The machine surface.

- Purpose: serve the same records to other systems and agents.
- Typical shape: REST APIs over records and relationships, SDKs, event streams for metadata changes, and increasingly agent-oriented endpoints that expose governed context to AI tools.

## Important Rules / Behaviors

- **The platform describes; it does not hold.** No data rows, no query results as data — only metadata. Everything in the store is about assets that live elsewhere. This is the wall against warehouses, lakes, and fabrics.
- **Records persist and accumulate.** A record is an object with a history, not a snapshot; re-collection updates it rather than replacing it, and platform-side additions survive re-collection (see synchronization above).
- **Source systems remain the origin of technical truth.** Harvested technical metadata reflects what the source reports; the platform is the authority for the *combined, enriched* picture, not for the source's internals.
- **Permissions shape visibility.** Access to the platform is role-based (and in some products attribute-based): who can connect sources, who can edit which records, who sees which classifications. Governance-heavy deployments extend this to visibility rules on the records themselves.
- **Collection is an operated subsystem.** Connections need credentials, schedules, and often in-network agents; collection failures are operational events that stewards and admins monitor, because a stale store silently loses trust.
- **The store is only as good as its coverage.** A warehouse never connected is invisible to the platform — "the estate" means the connected estate, and maturity is measured by how much of the real estate is actually mapped.

## Variants

- **API-first / active-metadata platforms** — cloud-native products whose center is the live, continuously synchronized metadata graph, sold to data teams, with the catalog experience as one face and machine endpoints as the other.
- **Governance-first enterprise suites** — platforms where the metadata store is the foundation beneath a governance operating model; stewardship, policies, and workflows are the visible applications; often serve highly regulated industries and offer self-hosted deployment.
- **Hyperscaler foundation products** — cloud suites that sell the metadata store itself as a separately-metered foundation, with discovery/catalog surfaces and other solutions layered above it.
- **Open-source frameworks** — self-hosted platforms built around a schema-driven store and REST/SDK access; deploy and operate it yourself, with connector breadth as the community contribution.
- **Framework-shaped lineage/estate tools** — thin-UI, hook-based collectors feeding a common store for machine consumers; the historical shape of the Type.
- **Deployment poles** — SaaS-only; self-hosted; hybrid with on-site agents for sources that cannot leave the network (data-residency driven).

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Data Catalog | closest sibling — the discovery-facing instantiation of the same layer | the catalog's product identity is the asset inventory + find-and-trust loop; the metadata platform's identity is the layer itself (store + collection + exchange) that powers catalogs, governance, quality, and agents; suites ship both in one product |
| Data Governance Platform | adjacent — an application riding on the layer | governance centers rules, accountability, and processes over the estate; metadata platform centers the descriptive content; governance machinery appears here as modules |
| Data Lineage Platform | capability seam | lineage is one relationship inside the metadata content; a dedicated lineage platform centers capture/tracing/impact operations on the flow graph at pipeline depth |
| Data Quality Platform / Data Observability Platform | module seam | quality/health machinery (tests, monitors, incidents) executes and alerts; this platform holds descriptive and operational records about the same assets |
| Master Data Management | different object | MDM manages the master data records themselves (golden customer/product records); this platform manages metadata *about* data assets |
| Data Fabric Platform | boundary at data movement | a fabric actively integrates and delivers data through an estate-spanning metadata layer; this platform stops at describing — it never holds or moves the data |
| Lakehouse / Warehouse Platform | holds vs describes | platform-native catalogs describe their own estate's tables and increasingly serve external engines; this Type exists to unify across systems it does not operate |
| Enterprise Asset Registry / IT Asset Management | different asset class | those record IT assets (hardware, software, licenses) with financial/lifecycle semantics; this Type records data-and-analytics assets with technical/business semantics |
| Data Exchange Platform | different primary act | exchange centers publishing/sharing data outward to consumers; this platform centers the internal record layer |

The boundary with **Data Catalog** is the most important one, and the market deliberately blurs it: most products ship both. The structural test is what the product *is* when the discovery experience is taken away — a metadata layer still stands (several products sell exactly that) — and what the product *is* without the collection-and-exchange machinery — a per-asset discovery page is not this Type.

## Representative Products

- Atlan — API-first active-metadata platform
- Collibra — governance-first enterprise data intelligence platform
- Microsoft Purview (Data Map + Unified Catalog) — hyperscaler suite productizing the metadata store as a foundation
- OpenMetadata — open-source unified metadata platform
- Apache Atlas — open-source metadata management and governance framework (Hadoop era)

The definition was checked against the framework-era shape (thin UI, hooks, common store) to avoid over-fitting it to the modern catalog-style implementation.

## Sources

Research date: **2026-09-08**

- Atlan — What is Atlan (official documentation): https://docs.atlan.com/get-started/what-is-atlan
- OpenMetadata — Documentation root (official): https://docs.open-metadata.org/latest
- Microsoft Purview — Learn about Microsoft Purview: https://learn.microsoft.com/en-us/purview/purview ; Learn about Microsoft Purview Data Map: https://learn.microsoft.com/en-us/purview/data-map
- Collibra — Collibra Platform (product page): https://www.collibra.com/us/en/products/data-intelligence-platform ; Documentation center: https://productresources.collibra.com/docs/collibra/latest/Content/Home.htm ; About Edge: https://productresources.collibra.com/docs/collibra/latest/Content/Edge/co_edge.htm
- Apache Atlas — GitHub README (official project): https://github.com/apache/atlas ; https://atlas.apache.org

> Sourcing limitations: Informatica's documentation portal (403) and product page (404) were unreachable after two attempts and Informatica is therefore not used as an evidence product; Apache Atlas's deeper documentation pages were unreachable (SPA), so Atlas observations rest on the official README at reduced strength; OpenMetadata's dedicated overview page 404'd and observations come from its documentation root. Precise operational details (connector counts, billing/metering, model internals) are deliberately not stated in this document; where cross-product behavior varies (re-collection vs human edits, conflict resolution, permission depth), the document describes the conceptual structure rather than any product's specific mechanics.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
