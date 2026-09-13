# Knowledge Graph Platform

## Overview

A **Knowledge Graph Platform** is the platform on which an organization turns heterogeneous data sources into a governed, shared knowledge graph — a persisted graph of identified entities (people, products, organizations, machines, concepts) connected by named, typed relationships under a shared semantic model — and then serves that graph to the applications and people who consume it.

Its defining work spans the whole life of the graph: modeling the domain's vocabulary, building the graph from sources (by ingestion, mapping, virtualization, and curation), governing it as an organizational asset (security, versions, quality, provenance), and operating it as a shared, permission-controlled resource for many consumers. Where a graph database stores and serves whatever graph it is given, a knowledge graph platform is what makes the graph an *asset*: it owns the pipeline from messy sources to a semantically modeled, quality-checked, access-controlled knowledge resource that outlives any single project.

The defining structure is small:

```text
Shared semantic model (schema / ontology / vocabulary)
  └── Knowledge graph (identified entities + typed relationships + attributes)
        └── Construction machinery (sources → mapped → resolved → curated → kept current)
              └── Governed serving (query, search, APIs, access control → downstream consumers)
```

Everything commonly associated with current products — visual no-code modeling, data virtualization, formal reasoning, entity-resolution engines, graph algorithms, GenAI question answering — makes the platform effective but does not define it. The mid-2000s semantic-web stack (an RDF store + an ontology + database-to-RDF mapping + a SPARQL endpoint with access control) satisfies the same core with none of the modern apparatus.

When the primary job shifts to navigating the finished graph, the product is a Knowledge Graph Explorer; when it shifts to operating the database itself, a Graph Database Explorer or management console; when it shifts to authoring queries, a query workbench. The platform's job is producing and operating the graph as an asset.

## Users & Context

Several distinct roles work in the same platform, typically in sequence:

- **Knowledge / data engineers** — connect data sources, configure mappings, load or virtualize content, and operate the running platform. They are the platform's primary operators.
- **Knowledge engineers, taxonomists, and domain experts** — design and evolve the semantic model: the classes, relationship types, attributes, and controlled vocabularies that give the graph its meaning. In mature products this work is deliberately open to non-programmers, because the people who understand the business domain rarely write code.
- **Data stewards / governance owners** — define quality constraints, manage access rights and lifecycle status, and review provenance and validation reports.
- **Application developers** — consume the graph through query languages, APIs, and SDKs to build downstream products.
- **Analysts and business users** — consume the graph through the platform's own or companion surfaces: search, exploration views, BI, and natural-language question answering.

The organizational context is an enterprise with more data than shared understanding: sources live in many systems, the same real-world thing is recorded differently in each, and no single application owns the connections between them. The platform exists so that one governed graph can answer questions no single source can.

## Core Model

### The defining core

Three structures, held together. Remove any one and the product stops being a knowledge graph platform.

**1. The knowledge graph as the asset of record.** A persisted — or virtually unified — graph whose members are individually identified entities and named, typed relationships, each carrying attributes, all governed by a shared semantic model: the schema, ontology, or controlled vocabulary that declares which entity types exist, which relationships may connect which types, and which attributes belong where. The model may be a formal open-world ontology or a light type-and-label scheme; either way it is what makes the graph *knowledge* rather than an anonymous edge list, and it is something the organization maintains and evolves deliberately. The graph is a lasting shared asset, not one application's transient data.

**2. Construction machinery: sources become the graph, and stay current.** The platform provides the means by which heterogeneous source content is turned into graph content: connecting to sources (files, relational databases, APIs, other data platforms), mapping source fields and tables onto model concepts, establishing which records describe the same real-world entity, curating and correcting content (by engineers, domain experts, or AI assistance), and validating the result against quality constraints. Construction may be code-first, visual/no-code, or AI-assisted — what is definitional is that the platform owns this source-to-model pipeline. A database accepts whatever a user loads; a platform is judged by what it does to transform sources into the modeled, trustworthy graph.

**3. Governed serving of the graph to consumers beyond its builders.** The platform operates the graph as a shared resource: query surfaces (a graph query language, and commonly SQL-for-BI, REST, or GraphQL as well), search over entities and their connections, and permission-gated access for many users and applications — including access control that follows the graph's own structure. Consumers are downstream surfaces: exploration applications, dashboards, operational applications, AI assistants. If nothing consumes the graph, the product is a modeling tool, not a platform.

The three are load-bearing jointly:

```text
model alone            → a graph database's contents or an ontology document
construction alone     → an ETL project with no semantic asset
serving alone          → a query engine over whatever graph exists
model + serving,
without construction   → a graph database with security — a different product class
construction + serving,
without model          → ordinary data integration with no knowledge frame
```

### What mature products add

Current platforms typically carry most of the following. They make the platform practical but do not define the Type:

- **Data virtualization and federation** — querying sources in place through the model instead of (or alongside) materializing them, sometimes federating several stores behind one endpoint
- **Entity resolution** — identifying which source records describe the same real-world entity, as a named capability in some products and a methodology in others
- **Reasoning and rules** — deriving additional facts from the model (class hierarchies, equivalences, user-defined If–Then rules), with the derivation logic inspectable
- **Data quality constraints** — declaring rules the graph must satisfy; violations can be flagged, reported, or blocked
- **Visual / no-code modeling and mapping** — canvas-style editors that let domain experts and business users participate in modeling and mapping without writing code
- **Rich query surfaces** — the graph query language plus SQL over the graph for BI tools, GraphQL endpoints, full-text and geospatial search, stored and parameterized queries
- **Asset governance** — catalogs of models, vocabularies, and datasets; versioning (including developer-workflow integration); lifecycle statuses; provenance records of who created and changed what
- **Companion consumption applications** — exploration and search surfaces built on the platform's own graph
- **AI answering** — natural-language questions translated into graph queries, answers grounded in the graph, and unstructured documents absorbed into it (era-current; present across the market but young)
- **Enterprise security and operations** — fine-grained access control down to graph elements, enterprise authentication integration, clustering, backup, monitoring

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:            Shared semantic model
Implementations:    formal RDF/OWL ontology + SKOS vocabularies + SHACL constraints,
                    light property-graph schema, organization-defined catalog models

Concept:            Source integration
Implementations:    batch ingestion, continuous collectors, live virtual graphs over
                    relational systems, federation across query endpoints

Concept:            Entity identity
Implementations:    persistent global identifiers (IRIs), node IDs with matching rules,
                    layered identity kept separate per source

Concept:            Governed serving
Implementations:    query endpoints (SPARQL / Cypher / SQL / GraphQL), query templates
                    exposed as REST APIs, per-element access control, org-scoped graphs
```

A reader who has only seen one realization — say, a cloud platform with a visual mapping tool — should still recognize a code-first platform that loads RDF files and exposes a secured SPARQL endpoint as the same Type of product.

## How It Works

The platform's work is a lifecycle, not a single transaction. A typical arc:

```text
1. Model the domain
     create or import the semantic model: classes, relationship types,
     attributes, vocabularies — authored, imported from standards,
     or drafted with AI assistance and then reviewed
2. Connect and map sources
     register data sources; map source fields/tables to model concepts;
     mark which fields identify unique entities; let the platform suggest
     mappings where it can
3. Construct the graph
     load mapped content or expose sources as virtual graphs;
     resolve entity identity; apply rules and inference;
     validate against quality constraints
4. Govern
     grant access by role and by graph structure; version and review
     model changes; keep provenance of what came from where and who
     edited what
5. Serve
     query (graph language, SQL/BI, APIs), search, explore, feed
     applications and AI assistants — every consumer sees the graph
     through its own permissions
6. Evolve
     sources change and the model matures → mappings are revised,
     content re-synced, quality re-checked — the graph is kept current,
     not rebuilt
```

In prose: a team first decides what the organization's graph will talk about — customer, product, site, machine, concept — and expresses that in a shared model, often reusing public vocabularies where they fit. Each source system is then connected and mapped: a column becomes an attribute, a foreign key becomes a relationship, a row becomes an entity instance — identified by a designated key so that two sources describing the same warehouse end up as one entity, not two. Content either lands in the platform's own store or stays in place behind a virtual mapping; either way, queries see one graph. Rules and constraints run against the result: class membership derived from shared properties, business logic captured as If–Then rules, conflicting or nonconforming data flagged before it misleads anyone. Access is granted by role and often by graph region, so a regional analyst sees regional entities. From there the graph serves: analysts explore it, BI tools query it through SQL, applications call it through APIs, and AI interfaces answer questions by translating them into graph queries — each surface consuming the same governed asset. When a source schema changes or the domain grows, the model and mappings are revised and content re-synced; the asset persists through the change.

### Core vs standard vs optional

**Defining core** — without these, not this Type:

- the knowledge graph as a shared asset under a maintained semantic model
- construction machinery: sources → mapped → identified → curated → kept current
- governed serving: query/search access, permission-controlled, for consumers beyond the builders

**Standard capabilities** — present in most mature products:

- virtualization or federation alongside materialization
- entity resolution, reasoning/rules, quality constraints
- visual modeling and mapping for non-engineers
- SQL/BI and API serving in addition to the graph query language
- asset catalogs, versioning, lifecycle workflow, provenance
- companion exploration/search applications
- fine-grained security and enterprise authentication
- AI question-answering over the graph

**Optional / variant** — depends on segment and posture:

- formal-ontology depth vs light schema
- own storage engine vs storage-agnostic middleware vs hosted substrate
- industry-specific packages and pre-built models
- GenAI agent integration as a product surface

## Interfaces

The main surfaces, described conceptually; exact names and layouts vary by product.

### Modeling canvas

The semantic model's home.

- typical information: classes, relationships, attributes, vocabularies; list and graph views of the model; namespaces and identifiers
- primary actions: create/edit/import model concepts, define rules, manage multiple model versions or variants

### Mapping / integration console

Where sources meet the model.

- typical information: registered data sources and their connection state; source fields/tables beside target model concepts; mapping completeness indicators; platform-suggested mappings awaiting approval
- primary actions: register a source, create/adjust a mapping, designate entity-identifying fields, publish mappings to the endpoint

### Query surfaces

The structured access layer.

- typical information: query editors for the graph language (and often SQL), saved/query catalogs, result tables or graphs, query performance feedback
- primary actions: write/run/save queries, expose parameterized queries as service endpoints

### Administration & security

The operating console for the platform and its graph.

- typical information: users, roles, permissions (including graph-region and source-scoped rights), databases/repositories and their lifecycle, backups, monitoring
- primary actions: manage users/roles, grant/revoke access, manage storage, configure authentication integration

### Governance surfaces

The asset-management layer.

- typical information: catalogs of models/vocabularies/datasets, lifecycle status, version history, provenance records, validation and quality reports
- primary actions: change lifecycle status, review/approve changes, inspect provenance, triage violations

### Curation forms

Where domain experts correct and enrich graph content.

- typical information: model-driven entry forms for entity instances, validation against the model as the user types, provenance of each value
- primary actions: create/edit instances, connect entities, capture provenance

### Consumption surfaces

What consumers meet.

- typical information: entity search with autocomplete, exploration views of entities and their connections, dashboards or applications generated from the model, conversational answer interfaces
- primary actions: search, navigate connections, ask questions, consume results

## Important Rules / Behaviors

**The model gates everything.** What can be mapped, queried, validated, or surfaced depends on the declared semantic model: a relationship type with undeclared endpoints cannot be mapped, an attribute outside the model cannot be searched, a constraint references a model concept. Changing the model changes the platform's entire behavior surface — which is why model changes are versioned and reviewed.

**Instance identity must be established.** Mapping source content to a model concept is not complete until the platform knows what makes an instance unique — a designated identifier or matching rule. Without it, sources produce duplicates rather than entities. Mature platforms make this explicit in the mapping workflow.

**Source-derived content and human curation stay separate.** Content collected from source systems is kept in a different layer than edits made by people on the platform, so that re-collecting a source refreshes its content without destroying human enrichment. This layering is the standard way platforms reconcile "always current from the source" with "curated by us".

**Access control follows the graph's structure.** Permissions attach not only to the platform as a whole but to regions of the graph — named subgraphs, entity types, individual entities, virtualized sources — so different audiences see different projections of the same asset. Derived and virtualized content is covered by the same controls as stored content.

**Multiple models can frame the same graph.** A single graph can be read through more than one model or business view — the flexibility the "knowledge" frame exists for. Which model a consumer sees is a governed choice, not an accident.

**Constraints are enforced, not decorative.** Quality rules can find, flag, or outright prevent nonconforming content; validation reports are part of operating the platform, and violations are visible and inspectable down to the offending entities.

**Virtualized content is served through the model.** When a source is mapped rather than loaded, the platform still answers queries, applies security, and enforces the model against it — the consumer cannot tell loaded and virtualized content apart except through metadata the platform chooses to expose.

## Variants

Common forms in the market:

- **Engine-included enterprise platform** — the vendor ships its own graph store plus the full construction/governance/serving estate; deployment from Docker/Kubernetes to managed cloud
- **Storage-agnostic platform** — the platform operates over third-party graph stores through standard query protocols; its value is the asset lifecycle, not the engine (a form directly observed in the researched sample; how much of the market shares it was not directly verified)
- **Database-centered platform with KG tooling** — a graph DBMS vendor whose knowledge-graph story is delivered through a construction tooling layer (importers, LLM-assisted graph building, entity-resolution methodology) on top of the database; the same vendor sells the database alone to other buyers
- **Hosted governance substrate** — a SaaS product whose underlying architecture is a graph (identified resources, directed relationships, layered provenance) surfaced through a catalog/governance product rather than a graph-facing console
- **Model-first middleware** — taxonomy/ontology-centric platforms emphasizing controlled vocabularies, content intelligence, and semantic application building
- **Industry-tuned packages** — pharma, manufacturing, finance, cultural-heritage editions with pre-built models and connectors

The variant axis does not change the core: every form still models, constructs, governs, and serves a shared knowledge graph.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Knowledge Graph Explorer | downstream | the explorer navigates and helps people understand the finished graph; the platform builds, governs, and serves it. Same vendors ship them as separate applications |
| Graph Database Explorer / Database Management Console | sibling at the storage layer | their object is the running database and its stored graph; the platform's object is the knowledge asset's lifecycle — model, sources, curation, consumption |
| Graph databases (product class) | substrate | a DBMS stores and serves whatever graph it is given; the platform owns the source-to-model pipeline and the asset's governance. A DBMS plus construction and governance tooling becomes this Type |
| RDF / SPARQL Workbench | included module | query authoring over one dialect is one serving surface inside the platform, not the platform |
| Data Catalog | adjacent, often co-packaged | a catalog's asset of record is metadata about datasets for discovery and governance; the platform's asset is the instance-level entity/relationship graph. A platform may ship a catalog module; a catalog may run on a graph substrate |
| Data Fabric / Metadata Management Platform | adjacent estate layer | the fabric manages the whole data estate through a metadata layer, which may itself be a knowledge graph; the platform's center is the knowledge asset serving knowledge applications |
| Master Data Management | overlapping capability | MDM governs golden records for master data domains; the platform's graph is a semantic integration asset for many consumers, not the stewardship system of record |
| Enterprise Knowledge Assistant / RAG Development Platform | consumer | assistants and RAG pipelines ground their answers in the graph the platform provides; answering layers inside the platform are a capability, not the Type |
| Search Platform / Semantic Search Platform | adjacent capability | search over the graph is one serving surface; a search platform's center is retrieval, not the graph asset |

The sharpest boundary is with the graph database. The market itself polices this seam: the same vendor sells the database to graph-database buyers and the knowledge-graph platform (database plus modeling, mapping, resolution, governance, and serving tooling) to knowledge-asset buyers. The test is the source-to-model pipeline: remove it and what remains is a DBMS with security; add it and the product becomes a platform.

## Representative Products

- **Stardog** — enterprise knowledge-graph platform including its own RDF store, virtual-graph integration, entity resolution, reasoning, quality constraints, and separate applications for modeling (Designer), querying (Studio), and exploration (Explorer)
- **metaphactory (metaphacts)** — storage-agnostic knowledge-graph platform operating over third-party SPARQL stores: visual OWL/SHACL modeling, SKOS vocabulary management, governance with versioning and lifecycle, model-driven application building
- **Neo4j** — property-graph platform whose knowledge-graph posture combines a flexible-schema graph database with a construction tooling layer (importers, LLM-assisted graph building, entity-resolution methodology) and serving tooling (algorithms, GenAI integration); included as the boundary case where database and platform meet in one vendor
- **data.world** — hosted platform whose catalog and governance product runs on a knowledge-graph substrate (IRI-addressed resources, directed relationships, layered provenance, organization-scoped SPARQL); included as the boundary case where a graph substrate surfaces as a catalog

Older realizations — the mid-2000s semantic-web stack of RDF store, ontology, database-to-RDF mapping, and secured SPARQL endpoint — satisfy the same core and were used to check that the definition does not overfit the current visual/cloud/AI era.

## Sources

Research date: **2026-09-08**

- Stardog — documentation home; Getting Started Part 1: Introduction to Knowledge Graphs; Stardog Designer chapter: https://docs.stardog.com/ , https://docs.stardog.com/getting-started-series/getting-started-1 , https://docs.stardog.com/stardog-applications/designer/
- metaphacts — metaphactory product page (feature overview): https://www.metaphacts.com/product
- Neo4j — Knowledge graph use case: https://neo4j.com/use-cases/knowledge-graph/
- data.world — documentation home, developer docs, and API reference: https://docs.data.world/en/ , https://developer.data.world/ , https://developer.data.world/llms.txt

> Sourcing limitations: the documentation site of a taxonomy-first semantic-suite vendor was unreachable (transport errors on two attempts), so the model-first middle of the market is evidenced through the two sampled platforms above; no claims about that vendor are made. For the storage-agnostic platform sampled here, evidence comes from the vendor's official product page rather than its deep help documentation (unreachable in a same-day sibling pass); feature claims are calibrated to page level. One sampled product's knowledge-graph architecture is observed through its developer/API documentation rather than its user-facing docs; that reading is stated as an inference. Precise product limits, defaults, and branded module names observed in the sample are deliberately not asserted in this document; they remain in the Research Notes.
