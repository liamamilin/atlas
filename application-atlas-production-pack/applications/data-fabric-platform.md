# Data Fabric Platform

## Overview

A **Data Fabric Platform** is an organization-wide data management layer that connects an enterprise's scattered data sources in place, keeps one unified metadata map of all of them, and integrates, governs, and delivers that data as coordinated functions of a single system.

It exists for a specific, common problem: in a large organization the data that matters lives in many places at once — operational databases, data warehouses, data lakes, SaaS applications, files, message streams, legacy systems — and every new project rebuilds its own pipelines, rediscovers what the data means, and re-implements its own access rules. The fabric's answer is one layer over all of it: the sources stay where they are and remain authoritative, but the fabric knows what data exists where and what it means, moves or serves it as needed, and applies governance uniformly as the data is used.

The defining structure is deliberately small:

```text
Connected data sources (systems of record stay put)
└── Unified metadata layer spanning the whole estate
    └── Integrated data operations executed through that layer
        (integration + governance + delivery from one system)
```

Everything else commonly shipped in the box — query federation, batch pipelines, change-data-capture, semantic layers, knowledge graphs, data marketplaces, data products, AI assistants, even an included warehouse — is a way of realizing one of those three functions, not part of what makes the product a fabric. A vendor may realize the layer with a single integrated platform, a bundled subscription of cooperating products, or a portfolio; and the term itself is also used in the industry for the *architecture* such a product implements. What separates a fabric product from adjacent Types is held constant: if the platform only *describes* data it is a Data Catalog; if it only *moves* data between endpoints it is a Data Integration Platform; if it owns the data of record it is a Warehouse or Lakehouse.

## Users & Context

Primary users:

- **Data engineers** — connect sources, build and operate the pipelines, views, and models through which data is integrated and delivered.
- **Data stewards / governance leads** — curate meaning in the metadata layer, define and enforce access, masking, and quality policies, work exceptions.
- **Data architects / platform teams** — design the estate-spanning layer, decide which integration style serves which use case, run the platform.

Secondary users:

- **Analysts and business consumers** — find, understand, and get access to data through the catalog or marketplace without asking IT each time.
- **Application developers and AI builders** — consume integrated, governed data through APIs, query endpoints, or ready-made data products.
- **The data leadership office** — oversight of usage, policy compliance, and the health of the whole data estate from one place.

The context is almost always a mid-size or large organization with a hybrid or multi-cloud estate and more source systems than any team can track by hand. Increasingly, the triggering motivation is AI: models and agents need data with consistent meaning and enforced access rules, which is exactly what the fabric's shared metadata layer is designed to provide.

## Core Model

### The Defining Core

**1. Connected data sources.** The fabric's world begins with registered connections to the enterprise's data systems: databases, warehouses, lakes, SaaS applications, file stores, event streams, legacy platforms. The connections are read-and-operate relationships, not migrations — the source systems remain the systems of record, and the fabric's copies (where they exist) are derivatives. This is the structural claim that separates the fabric from platforms that ingest the world into their own store.

**2. The unified metadata layer.** One system-level map spanning all connected sources: what data exists, where it lives, what it means. Its minimal content is an inventory of assets with technical descriptions; mature products add business definitions, shared metrics, classifications of sensitive fields, ownership, and relationships between assets — sometimes realized as a semantic layer or knowledge graph, sometimes as a catalog with glossary and tags. This layer is the fabric's center of gravity: integration, governance, and delivery all operate *from* it, which is what makes them coordinated functions of one system rather than a bag of tools.

**3. Integrated data operations.** The fabric does not stop at describing data — it operates on it, and all operations run through the same metadata layer:

- **Integration machinery** — moving and combining data in whichever style a use case requires: pipelines (batch, streaming, change capture, replication), logical views that query sources in place, or both coexisting in one design surface.
- **Governance machinery** — policies defined once and attached to the metadata (this field is sensitive, this dataset has an owner, this term means X), then enforced wherever the data is accessed: discovery, query, API, export.
- **Delivery machinery** — governed consumption surfaces: query endpoints, APIs, self-service catalog or marketplace with access requests, and packaged "data products" that bundle data with its meaning and rules for reuse.

```text
External estate — systems of record stay put
  operational DBs · warehouses · lakes · SaaS · files · streams
        │  connectors
        ▼
  Connected sources ──── described in ────▶ Unified metadata layer
        │                                   (inventory · meaning ·
        ▼                                    classification · lineage)
  Integrated artifacts                             │
   (pipelines · virtual views ·                    ▼
    semantic models · data products)        Governance policies
        │                                  (access · masking · quality)
        └──────────────┬─────────────────────────┘
                       ▼
          Unified delivery surfaces
   (SQL/API endpoints · catalog & marketplace · data products)
```

### Standard Capabilities

These are what mature products add on top of the defining core. They make the fabric practical; their absence makes a product older or narrower, but not a different Type.

- **Connector libraries and automated harvesting** — broad coverage of source systems; the metadata layer is populated by automatic discovery, not manual entry.
- **Catalog and search** — asset inventory with facets, descriptions, business glossary, ownership, ratings/usage signals.
- **Semantic layer / business definitions** — shared metrics and terms so every consumer reads the same meaning.
- **Classification and lineage** — automatic tagging of sensitive data; tracked lineage from source through transformations to consumers.
- **Data quality management** — rules, profiling, and quality scoring attached to assets, with stewardship workflows for exceptions.
- **Policy-based access control** — masking, row/column-level rules, identity-aware policies enforced at access time.
- **Self-service marketplace / data products** — consumers discover and request governed data on their own; recurring needs are packaged as reusable products.
- **Multi-style integration in one design surface** — batch, streaming, change capture, replication, and/or federation chosen per use case.
- **Operational monitoring** — pipeline health, usage, freshness, and audit trails across the estate.
- **AI assistance over the metadata layer** — suggested descriptions and classifications, natural-language queries over the inventory, AI-readiness framing for models and agents.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:  Spanning sources in place
Realizations:  virtual query federation, registered connections with
               pipelines, replication, zero-copy sharing links

Concept:  Unified metadata layer
Realizations:  knowledge graph, semantic layer, catalog + glossary,
               inventory with stewardship campaigns

Concept:  Integrated delivery
Realizations:  SQL/API endpoints, data marketplace, data products,
               prepared extracts handed to BI and AI tools
```

A reader who encounters only one realization — say, a virtualization-first product with no pipelines — should still be able to recognize a pipeline-first bundle as the same Type from the core model.

## How It Works

### Onboard the estate

```text
Register sources (connections, credentials, connector selection)
→ metadata harvested automatically (schemas, tables, topics, reports)
→ classify and tag (sensitivity, domains, ownership)
→ curate meaning (descriptions, business terms, shared metrics)
```

The result is the unified metadata layer. This step is continuous: sources change, and the layer tracks them through recurring harvesting rather than one-time registration.

### Build integrated data

```text
Choose the style the use case needs
→ logical view querying sources in place (fast, no copies), or
→ pipeline moving/transforming data (batch, streaming, CDC, replication)
→ outputs registered back into the same metadata layer
→ quality rules and lineage attach automatically
→ recurring needs packaged as governed data products
```

The two styles coexist deliberately: virtual views avoid copying data but lean on source availability; pipelines trade copy storage for independence and performance. A mature fabric offers both under one design surface and one metadata layer, so a consumer usually cannot tell — and does not need to know — which style produced the data they are reading.

### Govern once, enforce everywhere

```text
Define policy against the metadata layer
  (who may see what · mask these classified fields · quality thresholds)
→ policy enforced at access time on every surface
  (catalog request, query, API, export, AI tool)
→ stewardship workflows handle exceptions and corrections
→ lineage and audit accumulate automatically
```

This is the behavior that most distinguishes the fabric from a collection of separate tools: policy is written once, against shared metadata, and travels with the data wherever it is consumed — including, in current products, into AI and agent contexts.

### Consume

```text
Find data in catalog / marketplace (search, browse, read meaning)
→ see rules and quality before requesting
→ request or receive access (self-service or steward approval)
→ consume via endpoint, API, BI connection, or data product
→ usage, lineage, and audit recorded
```

### Operate

The platform team monitors pipeline health, source freshness, policy compliance, and cost, and iterates: new sources onboarded, new products published, policies adjusted. The fabric is a standing operational system, not a one-time project — its value compounds as more of the estate is connected to the same layer.

## Interfaces

Surfaces described conceptually; exact layouts and names vary by product.

### Catalog / marketplace

The consumer's front door.

- purpose: find and understand data without IT mediation
- typical information: assets, descriptions, owners, sensitivity, quality, lineage, related terms
- primary actions: search, browse, request access, open in a downstream tool

### Integration design surface

The engineer's workbench.

- purpose: build the fabric's integrated artifacts
- typical information: sources, mappings, transformations, schedules, run status
- primary actions: create pipelines or views, model semantics, test, deploy, schedule

### Governance and stewardship console

The steward's control room.

- purpose: define and enforce policy, work exceptions
- typical information: policies, classifications, quality scores, stewardship tasks, audit
- primary actions: author policy, classify assets, resolve stewardship tasks, review audit

### Administration console

- purpose: operate the platform itself
- typical information: connections and credentials, engines/runtimes, monitoring, users and roles
- primary actions: manage connections, tune execution, manage users, review platform health

### Delivery endpoints

- purpose: machine and tool consumption of integrated data
- typical forms: SQL endpoints, REST/GraphQL APIs, BI-tool connectivity, AI/agent context interfaces

## Important Rules / Behaviors

### Sources remain authoritative

The fabric connects, moves, and serves; it does not silently become the system of record. Local copies exist as caches, materializations, or delivered products — and mature products treat the difference between a derivative copy and the source as visible, manageable state. Drift between copy and source is a real operational hazard the platform is designed to expose, not hide.

### The metadata layer is the shared substrate

Every function — discovery, integration, governance, delivery — reads and writes the same metadata. This is the load-bearing rule: change a classification and access policy follows; register a new dataset and it becomes discoverable, governable, and consumable through the same layer. Products that bolt separate tools together without this shared substrate are selling the functions without the fabric.

### Policy travels with the data

Access decisions are made by the platform's own policy layer, tied to enterprise identity, and enforced at consumption time — not re-implemented per downstream tool. Because policies attach to metadata (classifications, domains), broadening access does not mean re-negotiating every dataset individually.

### Integration style is a per-use-case decision

Latency, cost, and source-impact trade-offs decide between querying in place, caching, and full movement. The same estate typically runs several styles side by side. federated access fails when a source is down; pipelines can lag their sources — mature products surface both failure modes rather than promising one uniform behavior.

### Access to the layer is role-separated

Building, governing, and consuming are distinct responsibilities with distinct rights. Engineers generally cannot rewrite policy; consumers see only what policy allows; stewards work through recorded, auditable actions. Exact role models vary by product; the separation itself is consistent across the category.

## Variants

- **Delivery-technique posture** — zero-copy/virtualization-first products (query sources in place, minimal replication) versus pipeline-first products (move and transform, minimal federation) versus hybrids offering the full range. This is the most visible philosophical split in the category.
- **Own-store inclusion** — some fabrics include a warehouse/lakehouse component or acceleration caches; others own no analytical store at all. Inclusion is a packaging decision, not a Type requirement.
- **Ecosystem scope** — vendor-neutral fabrics that span any estate versus ecosystem-centric fabrics built to preserve business context for one application family (an ERP vendor's estate, for example).
- **Suite breadth** — master-data services, API/application-integration services, streaming platforms, and data marketplaces are variously bundled in or left to specialists.
- **Packaging and deployment** — single integrated cloud platform, bundled multi-product subscription, or cooperating product portfolio; SaaS, hosted, or self-hosted; modular editions for trial and scale.
- **AI posture** — from metadata automation (suggested tags, classifications) through natural-language inventory query, to serving as the governed context layer for AI agents — the current era's dominant positioning theme across all poles.
- **Governance topology** — centralized policy-making versus federated models where domains own their data products under central oversight.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Catalog | closest sibling | A catalog describes data in systems it does not own and stops there — using an asset means leaving for the source. The fabric describes **and operates**: integrates, governs, serves. The catalog face is one surface of a fabric. |
| Data Integration Platform | sibling | Integration platforms center on building and running pipelines between endpoints, without an estate-wide governed metadata layer as the organizing structure. In a fabric, integration is one function inside the unified layer. |
| Data Virtualization Platform | sibling, technique-specialist | Virtualization is one access technique — logical views over sources. A fabric is a management layer that may include virtualization among several techniques; a virtualization-only product lacks the integrated governance/quality/management machinery. |
| Metadata / Lineage / Quality / Governance Platforms; MDM | single-function siblings | Each is one function of the fabric's shared layer, sold standalone. Their inclusion inside fabric suites does not collapse the Types. |
| Data Warehouse / Lakehouse Platform | adjacent | Warehouses and lakehouses hold the data of record and compute over their own store; the fabric spans stores it does not own. Fabrics may ship acceleration stores, and increasingly sit on top of lakehouses to manage access beyond them. |
| Data Exchange Platform | adjacent, different scope | Exchange handles inter-organization entitlement and delivery of dataset offerings; the fabric manages an organization's internal estate. Sharing faces inside fabrics serve internal reuse. |
| Change Data Capture Platform | mechanism vs layer | CDC is one movement mechanism; fabrics list change capture among their integration styles rather than being defined by it. |
| Database Management Console / SQL Client | different altitude | Those operate one database system at a time; the fabric's unit is the whole estate. |

The most consequential boundary — and the one to watch as the market moves — is with the Data Integration Platform: the categories share population members historically, and the structural test is whether an estate-wide governed metadata layer organizes the product, or whether pipelines are the product.

## Representative Products

- **IBM** — data fabric solutions realized through its watsonx.data family (lakehouse, integration pipelines, intelligence/metadata, governance): the enterprise-portfolio pole, and the vendor most explicitly articulating fabric as an architecture overlaid on existing systems.
- **Informatica (IDMC — Intelligent Data Management Cloud)** — the pure-play suite pole: catalog, integration, application integration, quality, master data, governance, and marketplace services on one platform driven by a shared AI metadata engine.
- **Talend Data Fabric (Qlik Talend)** — the namesake bundle pole: integration, change capture, execution infrastructure, inventory/catalog, preparation, stewardship, and API services sold as one subscription.
- **Denodo Platform** — the virtualization-first pole: universal connectivity, zero-copy delivery, runtime governance, and a shared semantic layer with a knowledge graph, marketed as logical data management.
- **SAP Datasphere** — the ecosystem-context pole: integration across movement patterns, semantic modeling, knowledge graph, data products, and warehousing, positioned as the "knowledge core" of an application ecosystem's business data fabric.

The sample deliberately spans all four product philosophies and different customer contexts; a unified analytics suite that carries "Fabric" in its name belongs to the lakehouse/analytics-platform family and was excluded on structural grounds.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces:

- IBM — "What is a data fabric?" https://www.ibm.com/think/topics/data-fabric · "Data fabric solutions" https://www.ibm.com/data-fabric
- Qlik Talend Help Center (Talend Data Fabric bundle documentation) — https://help.talend.com/
- Denodo — https://www.denodo.com/en · https://www.denodo.com/en/denodo-platform/denodo-platform
- SAP — "SAP Datasphere" https://www.sap.com/products/data-cloud/datasphere.html
- Informatica — https://www.informatica.com/ (product/platform structure)

> Sourcing limitations: vendor documentation portals for Informatica and SAP's help portal were not retrievable from the research environment on this date, and one deep Talend guide link was unreachable. Claims about those products rest on official product-site material, and operational details (connector counts, limits, default settings, plan-gated capabilities) are intentionally not asserted here. Detailed product-by-product evidence and the cross-product comparison matrix are recorded in the paired Research Notes.
