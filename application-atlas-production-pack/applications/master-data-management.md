# Master Data Management

## Overview

A **Master Data Management (MDM)** application is an organization's system of record for the identity of its shared core business entities — customers, products, suppliers, locations, employees, materials and similar entities that many systems touch. It holds one authoritative record per real-world entity, builds that record by consolidating the entity's records from multiple source systems, and keeps it current through a governed stewardship process so that every consuming system works from the same identity.

The problem it solves is structural: the same customer exists in the CRM, the billing system, the web store and the support desk — spelled differently, keyed differently, partially filled in each. Transaction systems cannot fix this because each owns only its own slice. An MDM application is the standing authority that answers, per entity: *is this the same customer as that one, what do we actually know about them, and which value is correct when systems disagree?*

The defining core is deliberately small:

```text
Designated entity domains (customer, product, supplier, …)
└── Master record of record — one authoritative record per real-world entity
    └── Built by cross-system consolidation
        └── (match the entity's records across source systems
             → merge → decide which attribute value survives)
    └── Governed maintenance
        └── (steward review, approval-gated changes, attributable history)
    └── Served back to the consuming systems
        └── (publish / sync / API / events)
```

Everything else the market associates with MDM — graph-style hierarchies, embedded data quality, reference data lists, AI-assisted matching, real-time APIs — is common capability layered on that spine, not what makes the product an MDM.

## Users & Context

MDM is used by a small specialist population on behalf of the whole organization.

Primary users:

- **Data stewards** — the operational center of the product. They review suspected duplicate matches, resolve conflicting values, merge and split records, author and correct master data, and work through task queues. In some organizations stewardship is a full-time role; in others it is part of an analyst's or governance manager's responsibilities (one sampled vendor defines the role in exactly these terms).
- **MDM administrators / solution architects** — configure the data model (entity types, attributes, lifecycles), the matching rules, survivorship policies, and the connections to source and consuming systems.
- **Data governance / data management leaders** — own the program: which entity domains are mastered, which systems are authoritative for what, who stewards which domain.

Secondary consumers:

- **Operational and analytical systems** (CRM, ERP, e-commerce, data warehouses) — they receive master records through integrations and are the reason the product exists, though people operating them rarely open the MDM application itself.
- **Business users** — in some products, role-specific data-entry and lookup experiences are exposed over the master data for non-specialists.

The work context is enterprise data management: multi-system estates, mergers and system consolidations, regulatory reporting, and increasingly the need for trustworthy entity data feeding AI systems — the framing current vendors emphasize, though not part of what defines the Type.

## Core Model

### The defining core

Three structures, held together. If one is removed, the product stops being an MDM.

**1. The master record of record.** For each entity type the organization designates as master data (a *domain*), the system holds persistent, individually identified authoritative records — commonly called **golden records** — one per real-world entity. The record is the reference point: the answer to "what do we actually know about this customer/product/supplier?" A master record typically carries:

- its own identifiers, plus a profile of attributes (name, addresses, classifications, status)
- the **source records** contributed by each source system, retained on or alongside the golden record — one sampled platform models each source contribution explicitly as a *crosswalk* holding the source system's name and that system's unique key, so nothing about where a value came from is lost
- derived state: whether the record is active, whether it is part of a merge group, its place in any hierarchy

**2. Cross-system identity consolidation.** The golden record is not entered once; it is *built* from the entity's records across multiple source systems. This is the mechanical heart of MDM:

```text
Source system A record ─┐
Source system B record ─┼─→ match (same real entity?) ─→ merge ─→ survivorship
Source system C record ─┘         (rules / fuzzy / ML)              (per attribute:
                                                                    which value wins?)
```

- **Matching** compares records — exactly, fuzzily, or with ML assistance — and groups those likely to denote the same entity. Matching is configurable; mature products maintain separate matching configuration for incoming source records and for the master records themselves.
- **Merging** combines a match group into one master record. The merge is usually *logical*: the source records remain distinguishable beneath the golden record.
- **Survivorship** decides, attribute by attribute, which value is authoritative when sources disagree — by source trust ranking, recency, or explicit rule. One sampled platform computes this per attribute at read time; another populates the golden record from "the best information available across source systems."

This leg is what separates MDM from a single-system master file (an ERP's internal item master is a master file, not MDM) and from a deduplication tool (matching without holding the authoritative record).

**3. Governed maintenance serving the estate.** The golden record population is kept current and *used*:

- **Governed change loop** — changes pass through review and approval. Automatically constructed records and machine-proposed matches are surfaced to stewards for confirmation; manual edits go through publish workflows; every change is attributable. One vendor states the gate directly: no record reaches the master store without passing defined validation and approval steps, whether triggered by a human steward or an automated agent.
- **Serving the estate** — authoritative records flow out to the systems that need them: batch exports, ongoing synchronization back to source systems, REST APIs, and event streams. Without this leg the product is a one-off consolidation project rather than management.

### Standard capabilities of mature products

Present across the researched sample and expected in the market, but not part of the definition:

- **Configurable data model** — every sampled product describes itself as metadata- or model-driven: entity types, attributes, relationships, and record lifecycles are configured, not hard-coded.
- **Hierarchies and relationships** — typed parent-child and network relationships among master records (customer/account hierarchies, product hierarchies); some products model the whole estate as a graph in which each entity exists once and participates in multiple hierarchies simultaneously.
- **Embedded data quality** — validation, standardization (e.g. address verification), enrichment, and duplicate prevention at the point of entry. Several MDM platforms ship data quality as a first-class, natively integrated capability; the boundary with dedicated Data Quality Platforms is covered below.
- **Stewardship work surfaces** — dashboards and task queues, side-by-side record comparison, draft states, publish workflows, audit trails.
- **Reference data** — code lists and value sets (countries, statuses, categories) managed beside entity master data; bundled in some products, shipped as a sibling product in others.
- **Integration machinery** — connectors to ERP/CRM/enrichment providers, initial and incremental loads, streaming publication, role-based permissions, APIs.
- **AI-era additions** — ML/AI-assisted matching, AI assistants for stewardship tasks, and protocol servers letting AI agents query governed master data. Era-current, optional.

### One structure, many implementations

The Core Model is conceptual; products realize it differently:

```text
Concept:   Authoritative record
Realized as:   golden record populated by survivorship at merge time, or
               a master record whose authoritative attribute values are
               computed from retained source contributions at read time

Concept:   Source contribution
Realized as:   explicit crosswalk objects (source + source-system key),
               source-record layers beneath the master layer, or
               match groups of candidate records

Concept:   Serving the estate
Realized as:   batch export, ongoing sync back to sources, REST services,
               streaming/event publication
```

## How It Works

The lifecycle of master data through the system:

### 1. Establish the model and connections

Administrators configure the entity domains to be mastered, their attributes and relationships, the matching rules, the survivorship policies, and the connections to source and consuming systems. Source systems are connected for load — initial bulk loads and ongoing incremental loads.

### 2. Load and match

Records arrive from source systems. The platform cleanses and standardizes them, then matches them against each other and against existing master records to find which records denote the same real entity. Matches above a confidence threshold may merge automatically; borderline matches become **match proposals** for human review.

### 3. Survive and publish the golden record

For each match group, survivorship rules combine the best available values into the golden record. Publication of changes is typically approval-gated: stewards confirm merges, review automatically constructed records, and resolve tasks before changes take effect.

### 4. Steward on an ongoing basis

The steady-state loop of the product:

```text
review match proposals → confirm / reject / merge / split
resolve conflict and quality tasks → correct or enrich values
author new master records where none exists
→ every change recorded and attributable
```

Stewards search and browse the master data, compare records side by side, and work their queues. Quality problems detected by embedded rules or anomaly detection become tasks routed to the responsible steward.

### 5. Serve consumers

Golden records flow to consuming systems — as full/incremental batch exports, as on-demand API reads, as event streams, and (in the coexistence style, below) as synchronization *back into the source systems themselves*, so the same merge that happened in the hub happens in the sources.

### Where authoring lives — the implementation styles

Mature products support more than one posture for where master data is created and edited; one sampled vendor documents these styles verbatim:

- **Consolidation** — sources feed the hub; consolidated golden records are provided downstream. Authoring remains in the sources.
- **Coexistence** — as consolidation, plus propagation of golden records *back* to the source systems, while authoring stays in the sources.
- **Centralized** — the hub is the only place master data is read and written.
- **Mixed** — read/write in both hub and sources.

The style is a deployment decision, not a different Type.

## Interfaces

Described conceptually; names and layouts vary by product.

### Stewardship workbench

The primary surface for data stewards.

- Purpose: keep the master data population clean, complete and current.
- Typical information: task queues (match proposals, quality issues, authoring requests), record lists with completeness/quality indicators, side-by-side record comparison.
- Primary actions: merge, split, unmerge, edit values, approve or reject proposals, create records, assign and resolve tasks.

### Master record detail page

The "360 view" of one entity.

- Purpose: show everything known about one real-world entity.
- Typical information: the golden profile, the contributing source records with their source-system identifiers, relationship/hierarchy context, quality indicators, change history.
- Primary actions: edit, merge/split into or out of this record, view lineage of a value, navigate to related entities.

### Search and browse

- Purpose: find entities and navigate the population, including hierarchical navigation.
- Typical information: filtered entity lists, saved searches, hierarchy trees.
- Primary actions: open a record, export, bulk operations.

### Model and configuration environment

- Purpose: define entity types, attributes, lifecycles, match rules, survivorship policies, validations and integrations.
- Primary actions: model entities, configure matching, wire loads/exports/APIs, manage roles and permissions. Distinctly an administrator surface; in several products it is a separate design environment from the stewardship application.

### Integration surfaces

APIs, batch load/export definitions, and event/stream publication — the programmatic face through which consuming systems and pipelines read and receive master data.

## Important Rules / Behaviors

- **The system is the identity authority, not a bystander.** What distinguishes MDM behavior from reporting or integration middleware: it prevents duplicates and low-quality records from entering *itself and connected source systems*, and it enforces its survivorship decisions on downstream consumers.
- **Match decisions are consequential and reviewable.** Merging is usually logical (source records remain distinguishable), and undoing a wrong merge — split/unmerge — is a first-class operation in mature products. Automatic merges happen only above configured confidence; borderline cases go to human review.
- **Nothing authoritative changes without governance.** Proposals, drafts, approval gates, publish workflows, attributable audit history. The approval gate applies regardless of whether the trigger was human or automated.
- **Records have lifecycles.** Master records are activated, deactivated, merged and split as governed events — not silently overwritten. History is retained.
- **Source contributions are preserved.** The golden record is not a replacement for source records; it sits above them. Where a value came from, and which rule chose it, remain answerable.
- **Conflicting values are resolved by policy, not by silence.** Survivorship rules make "which value is correct" a configured, inspectable decision rather than an accident of which system wrote last.

## Variants

- **Single-domain MDM** — mastering one entity domain: customer (historically called Customer Data Integration), address, supplier, vehicle. Explicitly a supported product scope, not a lesser form.
- **Multi-domain MDM suites** — several related domains mastered in one platform with relationships preserved between them; the dominant enterprise posture.
- **Domain-packaged MDM** — the same platform sold as product-experience, customer-experience, business-partner, supplier or location packages.
- **Implementation style** — consolidation / coexistence / centralized / mixed (see How It Works).
- **Deployment** — SaaS, self-hosted, hybrid, on-premises; several products offer the full spectrum.
- **Suite position** — standalone MDM product vs one product line inside a broader data-management platform that also ships data quality, catalog and reference data products (common among sampled vendors).
- **Model richness** — golden-record store vs graph/semantic data model with typed relationships and attribute inheritance.
- **Industry shapes** — healthcare party mastering (organizations and professionals as distinct party types), regulatory-compliance consolidation, CRM support programs.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Data Quality Platform | adjacent, tightly interlocked | DQ authors rules and *evaluates* data it does not own as system of record, recording pass/fail results; MDM *is* the system of record for master data. MDM products embed DQ machinery; DQ platforms treat MDM as just another source. Boundary: evaluator vs record-holder. |
| Data Governance Platform | adjacent, program layer | Governance defines policies, accountability and governed processes over the data estate; MDM manages the master records themselves. A governed definition of "Customer ID" belongs to governance; the consolidated customer record giving it substance belongs to MDM. |
| Data Catalog | adjacent | A catalog holds metadata *about* data assets (inventory + discovery); MDM holds the master data records themselves. Frequently shipped as sibling products in one suite. |
| Product Information Management / PIM | domain-relative | PIM centers on product records structured for selling/marketing channels with outbound channel renditions; MDM centers on cross-system entity identity and is domain-general. Product mastering can live in either; the center of gravity differs. |
| CRM / ERP / HRIS | complement | Operational systems own transactions and their own domain records; MDM consolidates identity *across* them. A single-system master file is not MDM. |
| Customer Data Platform | adjacent, different center | CDP collects behavior/event data and builds marketing-oriented profiles for activation; MDM builds governed operational master records for enterprise-wide use. |
| Data Warehouse / Lakehouse | different purpose | Analytical copies for querying vs operational authoritative records served back to source systems; coexistence-style MDM propagates data *upstream* into sources, which an analytical store never does. |
| ETL / ELT Platform | capability seam | Movement pipelines feed and receive MDM, but hold no authoritative record and make no identity decisions. |
| Reference Data Management | bundled capability | Code lists vs entity instances; commonly bundled in MDM platforms or shipped as a sibling product. |

The most consequential boundary is with the Data Quality Platform, because the two are sold together and interlock deeply; the durable discriminator is that MDM holds and decides the authoritative record, while DQ evaluates and reports on data held elsewhere.

## Representative Products

- Reltio — cloud-native, real-time unification and MDM
- Ataccama ONE MDM — standalone MDM engine within a unified data-quality/catalog/MDM family
- Profisee — Microsoft-native MDM across SaaS to on-premises deployment
- Stibo Systems STEP — enterprise multi-domain MDM platform
- Semarchy — model-driven, declaratively designed data platform with MDM at its core

Informatica, the category's long-standing enterprise anchor, could not be documented directly (see Sources) and is therefore listed without claims.

## Sources

Research date: **2026-09-08**

Primary vendor sources:

- Reltio Documentation Portal — https://docs.reltio.com/ (Data unification and MDM at a glance; Reltio configuration data types: The Source Type, The Graph Type) — fetched 2026-09-08
- Ataccama Documentation — https://docs.ataccama.com/ (ONE MDM: Welcome to MDM; Introduction to MDM; user-guide and configuration navigation) — fetched 2026-09-08
- Profisee — https://www.profisee.com/platform/ , /platform/golden-record-management/ , /platform/stewardship/ — fetched 2026-09-08
- Stibo Systems — https://www.stibosystems.com/platform — fetched 2026-09-08
- Semarchy Documentation Hub — https://docs.semarchy.com/ (incl. Concepts and terminology) — fetched 2026-09-08

> Sourcing limitations: Informatica's documentation domain was unreachable (HTTP 403; consistent with prior research passes), so no Informatica-specific claims are made anywhere in this document. Profisee's dedicated documentation subdomain was unreachable (connection failures), so its evidence rests on official product-site pages. Semarchy's legacy MDM product documentation redirects were stale at research date; its evidence is held at the platform level. All operational specifics that these limitations touch (numeric limits, thresholds, retention behavior, product-specific defaults) are deliberately not asserted.

Detailed product-by-product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
