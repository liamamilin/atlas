# Data Catalog

## Overview

A **Data Catalog** is a discovery application that maintains a searchable, browsable inventory of an organization's data assets — tables, columns, files, reports, dashboards, pipelines, topics, ML models — where the assets themselves live in other systems. Each inventory entry carries the structural and descriptive context a person needs to answer three questions before using the data: *What is this? What does it mean? Can I trust it?*

The defining core is deliberately small:

```text
Data assets living in external systems
└── Catalog entry standing for each asset
    └── Structural metadata (what the asset looks like)
        + descriptive context (what it means, who owns it)
    └── Search & browse discovery over the whole inventory
```

The catalog describes data; it does not hold it. When a user decides to use an asset, the work continues in the system that actually stores it. Everything else commonly associated with modern catalogs — automated metadata harvesting through connectors, lineage graphs, business glossaries, domains, certification badges, sensitive-data classification, quality scores, popularity ranking, access-request flows, AI copilots — is widespread in current products but is not what makes the product a catalog. Older data dictionaries and manually maintained metadata repositories, where every entry was typed in by hand, satisfy the same defining core.

## Users & Context

A catalog sits between the people who produce data and the people who need to use it. Typical users:

- **Data analysts, data scientists, business analysts** — the primary consumers. They search for data on a topic, evaluate candidates, and need to understand meaning and trustworthiness before writing a query or building a report.
- **Data engineers** — use the catalog to understand schemas and dependencies, trace where data comes from, run impact analysis before changing a pipeline, and document assets they build.
- **Data stewards and data owners** — curators. They assign meaning: write descriptions, attach business terms, tag and classify, certify trustworthy assets, and keep context current as data changes.
- **Governance, compliance, and privacy teams** — use the inventory to find sensitive data, check classification and policy attachment, and produce audit evidence.
- **Business users and executives** — lighter consumers who rely on search, plain-language descriptions, and trust signals to find certified data without knowing technical names.
- Increasingly, **applications and AI agents** — many catalogs expose their inventory programmatically so other tools can retrieve governed context about the data.

The context is organizational: most deployments aggregate metadata from many systems (warehouses, databases, BI platforms, pipelines, files) because the problem being solved is cross-silo — nobody knows what data exists, where it lives, or what it means.

## Core Model

### The defining core

**1. The catalog entry.** The central object is a record that stands for a data asset living elsewhere — a table in a warehouse, a column, a file, a BI dashboard, a pipeline job, a message topic, an ML model. Entries are referential: the catalog is a lens over an estate it does not own. This is what separates a catalog from a data platform: remove the "stands for something external" property and you are holding data, not describing it.

**2. Structural metadata plus descriptive context on each entry.** An entry carries at least two kinds of information:

- *Structural metadata* — what the asset looks like: schema, columns and their types, or the equivalent structure for non-tabular assets. This is usually harvested from the source system.
- *Descriptive context* — what the asset means and how it may be used: descriptions, business terms, tags, owner. Some of this is authored by people; some is machine-generated and confirmed by people.

Without the descriptive layer, a catalog degrades into a name index; the reason entries exist is to let a user understand an asset without opening the source system.

**3. A discovery surface over the inventory.** Search and browse are the entry points. A user who knows neither the system nor the technical name can find candidates by topic, business term, owner, tag, or plain keyword, then filter and compare. The inventory plus the discovery surface is what makes the application a *catalog* rather than a metadata repository.

### What mature products add

These capabilities are standard in mature products. They deepen the find → understand → trust loop but do not define the Type:

- **Automated harvesting** — connectors/crawlers extract metadata from many kinds of sources (databases, warehouses, BI tools, transformation and pipeline tools, messaging, file stores, SaaS apps) and keep entries current on schedules. Modern catalogs treat this as the default population mechanism.
- **Lineage** — a graph view of where an asset's data comes from and what consumes it, enabling impact analysis. Depth varies (asset-level vs. column-level; BI and pipeline lineage).
- **Business glossary and terms** — defined business vocabulary linked to assets, so a search for a business concept surfaces the data behind it.
- **Organizing containers** — domains, folders, or collections that group assets by business area or subject rather than by source system.
- **Trust machinery** — owners and stewards named on entries; certification states; endorsements; comments or Q&A between users on an entry.
- **Usage signals** — popularity, query-log-derived statistics, view counts; many products rank or annotate results by how much an asset is actually used.
- **Classification and tags** — labels on entries, including detection of sensitive categories (e.g., personal data) for compliance use.
- **Quality signals** — profiling statistics, freshness, test results or quality scores surfaced on the entry, whether measured natively or aggregated from external quality tools.
- **Access flows** — visibility rules over entries and, commonly, a request-access path from the entry page into the source system's grant process.
- **Programmatic surfaces** — APIs/SDKs so other tools can read (and sometimes write) the inventory, plus embedded search in chat or BI tools.

### One structure, many implementations

```text
Concept:              Catalog entry for an external asset
Realizations:         table/column records, dashboard records, file records,
                      topic records, pipeline records, model records

Concept:              Descriptive context
Realizations:         human-written descriptions, machine-suggested descriptions
                      confirmed by stewards, glossary terms, tags, classifications

Concept:              Discovery surface
Realizations:         keyword search with facets/filters, browse trees by source
                      or domain, conversational question-answering over the inventory

Concept:              Keeping the inventory current
Realizations:         scheduled crawls, incremental scans, event-driven ingestion,
                      manual registration
```

A reader who has only seen one modern cloud catalog should be able to recognize a manually populated enterprise data dictionary from the 2000s as the same Type, and vice versa.

## How It Works

A catalog runs three loops.

### Population loop — building the inventory

```text
Register a source (warehouse, database, BI server, pipeline tool, file store…)
→ harvest metadata from the source (schemas, tables, columns, reports, jobs)
→ create/update catalog entries
→ enrich entries (descriptions, terms, tags, owners — machine-suggested,
   human-confirmed, or hand-written)
→ repeat on a schedule so entries track the source
```

Before connectors existed, and still today in smaller setups, this loop runs manually: a steward types the structure and description of each table. The loop is what keeps the catalog an *inventory of what actually exists* rather than a wish list.

### Discovery loop — the reason users open the product

```text
Search by keyword / business term / filter, or browse by source or domain
→ scan result cards (name, description, owner, certification, usage)
→ open an entry
→ read the schema, description, lineage, quality and usage signals
→ decide: is this the right data, and can I trust it?
→ use the data in the source system, or request access from the entry
```

The catalog's product value concentrates in this loop: it compresses "asking around to find the right table" into a search experience. Entry pages are the unit of understanding — most time in a mature catalog is spent on an entry, not on the result list.

### Curation loop — keeping context trustworthy

```text
Steward/owner reviews entries in their domain
→ improves descriptions, attaches terms, tags, classifications
→ certifies assets that meet the bar; flags or deprecates stale ones
→ answers questions from users on the entry
→ usage patterns and gaps feed the next round of curation
```

Trust states matter here: entries commonly carry a state such as verified, draft, or deprecated, and both search ranking and user guidance lean on those states. Curation is continuous because sources change; an uncurated catalog decays into a stale phone book.

## Interfaces

Exact layouts and names vary by product. The following surfaces recur.

### Search / browse (catalog home)

The primary entry surface.

- a search bar over all inventory (keyword; in current products often natural-language or conversational as well)
- browse structures by source, asset type, or business domain
- result cards showing name, description snippet, owner, certification state, usage
- primary actions: search, apply filters/facets (source, type, domain, owner, tag, certification), open an entry

### Asset detail page (entry page)

The unit of understanding, one per data asset.

- typical information: qualified name and alias, description, schema/columns with types, owner and stewards, tags and classifications, glossary terms, lineage, quality/profiling signals, usage/popularity, related assets, the source system it lives in
- primary actions: read and evaluate, ask a question or comment, edit context (if curator), request access, follow/star, open or query the source

### Lineage view

A graph surface reachable from an entry.

- upstream and downstream assets, sometimes down to column level; pipeline and BI hops
- primary actions: trace origin, assess downstream impact of a change, navigate to neighboring entries

### Glossary / term pages

The business-vocabulary surface.

- term definitions, related terms, the assets mapped to each term
- primary actions: browse from business concept to data, link terms to assets (curators)

### Stewardship surfaces

Curator-facing worklists.

- entries awaiting documentation or review, suggested descriptions to confirm, classification tasks, certification queues
- primary actions: approve/edit suggestions, bulk-edit metadata, assign owners

### Admin console

- source registration and connection settings, harvest schedules, user/group management, roles, catalog customization (custom fields/templates in some products)
- primary actions: connect/disconnect sources, run or schedule harvesting, manage users and permissions

### Programmatic interfaces

- APIs/SDKs to search and read entries (and often write metadata), used to embed catalog knowledge into other tools, pipelines, and increasingly AI agents

## Important Rules / Behaviors

- **The catalog describes; it does not serve data.** Using an asset means leaving the catalog for the source system (or a query tool the product hosts). This boundary is structural, not incidental — it is what keeps the catalog applicable across an entire estate.
- **Inventory currency is a maintained property, not a given.** Entries reflect the last successful harvest. When sources change (tables added, renamed, dropped), the catalog is reconciled on the next crawl; how promptly and how visibly this happens varies by product.
- **Entry visibility can be restricted.** Sources or entries can be public to all catalog users or limited to explicitly granted users; role determines who can view, who can curate, and who can administer. Permissions on catalog visibility are a separate question from permissions on the underlying data.
- **Trust states shape guidance.** Certification/deprecation states attached to entries are commonly used to rank results and to warn users away from deprecated assets at the moment of use.
- **Business vocabulary steers retrieval.** Linking a glossary term to assets, and writing descriptions, typically improves how assets rank in search — curation directly changes discoverability.
- **One business concept, many entries.** The same real-world entity (e.g., "customer") usually appears in many systems under different names; catalogs commonly provide a way to map those variants to one logical concept, and governance-heavy products make that mapping a first-class object.
- **Roles separate consumption from curation.** Reading and searching is broadly available; editing descriptions, certifying, and administering sources is reserved for steward/admin roles. Licensing models sometimes encode this split explicitly.

## Variants

- **Standalone discovery-led catalogs** — the catalog is the product; positioning emphasizes search quality, usage analytics, and adoption by analysts.
- **Governance-suite modules** — the catalog is the inventory layer of a wider governance platform; positioned around stewardship programs, policy management, compliance, and health scoring, with governance domains as the main organizing frame.
- **Hyperscaler-bundled catalogs** — shipped as part of a cloud vendor's platform (often alongside security/compliance offerings), with a metadata storage/scanning foundation plus a user-facing catalog experience.
- **Open-source, self-hosted catalogs** — deployable on the customer's own infrastructure, often standards-driven, with a commercial distribution behind them.
- **Data-product / marketplace extension** — a growing layer in which curated bundles of assets ("data products") are published to a marketplace-style consumption surface on top of the catalog inventory.
- **AI-context pole** — catalogs repositioned as the context/knowledge layer that AI applications and agents query for governed, business-ready metadata; mechanically the same inventory, consumed programmatically.

A variant remains a variant as long as the defining core — external-asset inventory with descriptive context and a discovery surface — is intact. If the product's primary object becomes the data itself, or the policy/attestation workflow rather than the inventory, it has become a neighboring Type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Metadata Management Platform | broader discipline: manages metadata itself as governed enterprise content (standards, models, exchange) across its lifecycle; the catalog is the discovery-facing instantiation over that metadata |
| Data Governance Platform | organizes policies, stewardship programs, and compliance workflows over the estate; the catalog supplies the inventory those processes act on. Governance suites usually embed catalogs |
| Data Lineage Platform | centers on capturing and tracing data flows at pipeline depth; lineage is one view inside a catalog |
| Data Quality Platform | measures and tests data; the catalog surfaces quality signals but its job is discovery and understanding |
| Data Warehouse / Lakehouse Platform | holds the data; the catalog describes data across systems. A warehouse's built-in schema browser serves one system natively and is not a cross-silo catalog |
| Enterprise Search / Internal Knowledge Search | indexes documents and knowledge content for member-facing search/Q&A; the catalog indexes structured data assets with schema-level metadata |
| Data Exchange Platform / Government Open Data Portal | publishes and shares datasets to external or cross-org consumers; the catalog orients internal discovery and governance of the organization's own estate |
| Master Data Management | manages the master data records themselves (golden records); the catalog manages metadata about data assets. Mapping one business concept across systems is the seam |
| Database Management Console / SQL Client | operates a single database engine; the catalog aggregates across engines and adds business context. Some catalogs embed a query tool for convenience |

The two seams most often blurred in the market are with **Metadata Management Platform** (suites collapse inventory + metadata lifecycle into one product) and with **Data Governance Platform** (governance-first vendors lead with the catalog as the visible surface). The working distinction is the primary object of work: the asset inventory and its discovery loop, versus metadata as governed content, versus policy and compliance workflows.

## Representative Products

- Alation
- Collibra
- Microsoft Purview (Data Map + Unified Catalog)
- Atlan
- OpenMetadata

The definition was checked against older, manually populated data dictionaries and metadata repositories, and against single-system schema browsers, to avoid defining the Type by today's connector-driven, cloud, AI-assisted implementations.

## Sources

Research date: **2026-09-07**

- Alation — product page: https://alation.com/product/data-catalog/ ; documentation: https://docs.alation.com/ (About Alation; Roles and License Types)
- Collibra — product page and FAQ: https://www.collibra.com/us/en/products/data-catalog
- Microsoft — Microsoft Learn: https://learn.microsoft.com/en-us/purview/data-map ; https://learn.microsoft.com/en-us/purview/unified-catalog ; https://learn.microsoft.com/en-us/purview/purview
- Atlan — documentation: https://docs.atlan.com/get-started/what-is-atlan ; https://docs.atlan.com/product/capabilities/discovery/how-tos/search-and-discover-assets
- OpenMetadata — documentation: https://docs.open-metadata.org/ ; https://docs.open-metadata.org/v2.0.x/how-to-guides/data-discovery

> Sourcing limitations: Alation's current help center (help.alation.com) could not be fetched from the research environment (JS-rendered); its customer-managed documentation site was used instead. Collibra was researched at product-page/FAQ strength; detailed operational documentation was not fetched, so Collibra-specific workflow details are stated only at that strength. Precise vendor figures (connector counts, capacity limits, license tiers) are recorded in the Research Notes and intentionally not asserted as Type-level facts here.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
