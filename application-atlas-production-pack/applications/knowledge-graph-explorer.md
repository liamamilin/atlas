# Knowledge Graph Explorer

## Overview

A **Knowledge Graph Explorer** is an application for interactively navigating an existing knowledge graph — a persisted graph of typed entities (people, products, organizations, events, concepts, and so on) connected by named, typed relationships. The user locates an entity, sees what it is and how it connects, follows relationships to neighboring entities, and gradually assembles a visible picture of the structure connecting them.

Its purpose is understanding connected data without having to write graph queries. Where a graph database console answers "how do I operate this database" and a query workbench answers "how do I express this question in a query language," the explorer answers "what is this thing connected to, and what does that structure look like."

The defining structure is small:

```text
Knowledge graph (typed entities + typed relationships + attributes, under a shared model)
  └── Entity — identified, typed, labeled, inspectable
        └── Relationship traversal — follow named connections entity by entity
              └── Visible accumulation — the explored subgraph stays on screen as structure
```

Everything commonly associated with modern graph exploration — node-link canvases with force-directed layouts, visual query builders, schema diagrams, shortest-path finding, maps, saved shared views — makes the exploration practical, but the Type remains recognizable without them. Older linked-data browsers, which rendered an entity's typed properties as a page of followable links, satisfy the same core with none of the modern apparatus.

When the primary job shifts to building, loading, or governing the graph, the product is a Knowledge Graph Platform; when it shifts to operating the database instance, it is a Graph Database Explorer; when it shifts to writing queries against a query language, it is a query workbench. The explorer's job is traversal and comprehension.

## Users & Context

The primary users are people who need to understand connected data but are not necessarily query-language authors:

- **analysts and domain experts** — following connections among customers, transactions, products, or equipment to answer questions like "who else is connected to this entity?" or "how are these two things related?"
- **knowledge engineers and data engineers** — inspecting how an integrated graph actually materialized: whether entities resolved correctly, which relationships exist, how classes connect
- **business users** — in enterprise deployments, exploring a curated "business view" of the graph prepared for them, with no query language involved

Typical context: a browser-based application connected to a knowledge graph maintained by a platform or a graph database. Someone else — a data engineering or knowledge engineering team — produced the graph; the explorer is where consumers meet it. In database-console packaging, the same person may both administer and explore; in dedicated packaging, exploration is deliberately separated from building and administration.

## Core Model

### The defining core

Three structures, held together:

**1. The knowledge graph as the subject of exploration.** The application consumes a graph that already exists. Its contents are:

- **Entities** — identified things, each with an identity, one or more types or classes, a human-readable label, and attributes (properties with values)
- **Relationships** — typed, usually directed connections between entities, carrying meaningful names ("works for", "located in", "purchased", "part of"), sometimes with attributes of their own
- **A shared model** — the vocabulary that names and organizes all of the above: entity types and their hierarchy, which relationship types may connect which types, which attributes belong to which types. The model may be a light label-and-relationship scheme or a formal ontology; either way, it is what makes the graph *knowledge* rather than an anonymous edge list.

The explorer is read-first: building, loading, and governing this graph is the job of adjacent applications (graph platform, database tooling), not of the explorer itself.

**2. Entity-first inspection.** The user reaches an *identified entity* through a knowledge-aware entry surface — searching by label or keyword, browsing by entity type, or opening a saved view — and can see it as a meaningful object: what type it is, what it is called, what attributes it carries, and what it is connected to.

**3. Relationship traversal as the primary interaction.** From any inspected entity, the user follows its typed relationships to connected entities and continues outward. Traversal is usually selective (choose which relationship types or directions to follow) and always accumulative: the entities and links visited so far remain visible together, so the *structure* — not just the current record — is the object of attention.

Remove the typed model and the product becomes a generic network-visualization tool over ad-hoc edge lists. Remove entity-first inspection and it becomes a raw query console. Remove traversal and it becomes a single-record reference viewer. The three together are the Type.

### What mature products add

Current products typically carry most of the following. They make exploration effective but do not define the Type:

- **Graph canvas** — a node-link view of the explored subgraph with layouts, zoom, selection, node grouping or collapsing, legends keyed to entity types, and per-node expand menus listing the available relationship types
- **Entity search** — label/keyword search with autocomplete, often restricted to meaningful name and description properties, with filters by entity type
- **Browse-by-class and schema views** — overviews of the model itself: class hierarchies, diagrams of which types relate to which and by what relationship types, instance lists per class. These orient the user before instance-level traversal.
- **Table views** — paginated listings of entities by type with their attributes, bridging into the canvas for further exploration
- **Visual query building** — composing questions along the model's relationship paths (and simple aggregations) without writing a query language; results land in the same list/canvas views
- **Path finding** — shortest or constrained paths between two chosen entities
- **Saved and shared views** — a state of exploration (entry entity, expansions, filters) persisted, bookmarked, or shared by link
- **Export** — images of the canvas, tabular extracts of the explored subgraph
- **Scale guards** — limits, warnings, and pagination that keep runaway expansions of large graphs manageable
- **Access control** — permission-gated visibility of entities and views in enterprise deployments

### One structure, many implementations

The core is conceptual; products realize it differently:

```text
Concept:            Shared model over the graph
Implementations:    formal ontology (OWL/RDFS/SKOS vocabularies), light type/label model,
                    curated "business view" configurations over a property graph

Concept:            Entity identity and entry
Implementations:    IRIs / resource identifiers with label search, node IDs with keyword search,
                    autocomplete over name/description properties

Concept:            Visible accumulation of traversal
Implementations:    interactive node-link canvas, paginated property tables,
                    traversable property lists on entity pages (older linked-data style)
```

A reader who has only seen one realization — say, a modern canvas-based explorer — should still recognize an entity page of followable typed links as the same Type of application.

## How It Works

Exploration is a loop, not a pipeline:

```text
1. Enter the graph
     search by name/keyword · browse by entity type · open a saved or shared view
2. Inspect the entity
     type, label, attributes, list of connections
3. Traverse
     expand along chosen relationship types (or all of them)
4. Shape the accumulating view
     filter by type or relationship, group/collapse nodes, adjust layout
5. Orient in the model
     consult class/schema views when the instance level is disorienting
6. Ask structured questions (optional)
     visual query builder, path finding between two entities
7. Persist and share
     save the view or query, share a link, export data or images
→ the result becomes the entry point for the next loop
```

In prose: the user starts from something they can name — a customer, a molecule, a machine, a concept — found through search or a class listing. The entity view shows what the graph knows about it and lists its connections by relationship type. The user expands one or more of those connections; new entities enter the view, each itself inspectable and expandable. Because graphs grow quickly, products guard this step: expansion may be limited per step, warned when large, or paginated in table form. The user prunes and filters the accumulating picture — hiding irrelevant types, grouping same-type nodes — until the structure they care about is legible. When instance-level navigation loses the thread, schema-level views (which classes exist, how they relate) restore orientation. Findings leave the tool as a shared link, a saved view, an exported image, or a data extract — and in team settings, someone else's next exploration often starts from that shared state.

Two capabilities sit alongside this loop rather than inside it:

- **Query access.** Most products keep a door to the underlying query language or a visual builder that generates queries — but the defining posture is that a user who never opens that door can still explore.
- **Correction.** Dedicated explorers are read-first: when the graph is wrong, the fix happens in the platform's build/edit surfaces, not in the exploration canvas. Some database-console-packaged tools blur this by letting users edit statements on a resource directly.

## Interfaces

The main surfaces, described conceptually; exact names and layouts vary by product.

### Search / entry surface

The door into the graph.

- typical information: search box with autocomplete over entity labels and descriptions; entity-type filter; recent or saved views
- primary actions: search for an entity, filter by type, open a saved or shared view

### Entity detail

The inspection surface for one entity — usually a side panel on the canvas or a dedicated page.

- typical information: type(s), human-readable label, identifiers, attribute values, connections grouped by relationship type (and direction)
- primary actions: expand a connection into the view, open a connected entity, edit attributes (where editing exists at all)

### Graph canvas

The traversal surface where the explored subgraph accumulates.

- typical information: nodes colored/shaped by entity type, labeled edges, legend, selected node's details
- primary actions: expand or collapse nodes, filter, group/ungroup, rearrange layout, clear or reset the view

### Schema / class views

The model-level surfaces that orient exploration.

- typical information: entity-type hierarchy, which types connect to which and by which relationship types, instance counts per type
- primary actions: jump from a class to its instances, open a type-pair relationship view

### Query surfaces

The structured-questioning surfaces.

- typical information: visual builder over the model's classes and relationship paths; saved queries; in some products a direct query-language editor or natural-language prompt
- primary actions: compose a question along model paths, run it, send results to the list or canvas view

### Settings / scope

Configuration of what exploration covers.

- typical information: which named graphs or data sources are in scope, label-language preferences, whether inferred (derived) statements are included
- primary actions: change scope, toggle inference, adjust display

## Important Rules / Behaviors

**The model shapes the interface.** What can be searched, expanded, filtered, or asked depends on the graph's shared model: the classes it declares, the domains and ranges of its relationship types, the attributes attached to types. A relationship type with no declared endpoints may not appear in expand menus; search may cover only name and description properties. The explorer therefore reads two things — the graph *and* its model — and changes to the model change the exploration surface.

**Traversal is guarded.** Graphs explode combinatorially, so products impose scale discipline: per-expansion limits, warnings before large expansions, paginated tables, collapsed grouping of same-shaped nodes. Specific caps are product decisions; the guarding behavior itself is general.

**Visibility follows permissions.** In enterprise deployments, what a user can see while exploring is bounded by their access rights. Shared views render under each viewer's own permissions — sharing shows the *view*, not the sharer's access.

**Exploration is read-first.** The defining posture is non-destructive: exploring does not change the graph. Products vary at the edge — some database consoles allow editing the statements of a resource in place, with derived statements kept read-only — but the explorer as a Type exists to comprehend, not to mutate.

**Inference changes what is visible.** Where the platform derives additional facts (class hierarchy reasoning, equivalence), products expose a choice about whether derived statements participate in search, expansion, and display. The same graph can therefore present differently to the same user depending on this setting.

**One graph, several presentations.** The same subgraph may appear as a canvas, a table, a schema diagram, or (where entities carry location attributes) a map. These are views over one structure, switchable rather than separate datasets.

## Variants

Common forms in the market:

- **Semantic-web / ontology-aware explorer** — RDF-native; the model is a formal vocabulary; reasoning and named-graph scoping may be first-class; often part of an enterprise knowledge-graph platform
- **Property-graph business-view explorer** — exploration over a labeled property graph, framed by curated views that translate the database into business terms for non-technical users
- **Standalone open-source exploration app** — deployed separately, connecting to one or more graph stores and query dialects; exploration decoupled from any single product's console
- **Database-console exploration views** — visualize-and-explore surfaces embedded in a graph database's web console, sometimes with editing capabilities and schema statistics alongside administrative functions
- **Embedded explorer** — an exploration view exposed as an embeddable, chrome-less widget inside another application
- **Public knowledge-graph exploration** — free, open graphs of general knowledge explored via query and graph views; here the same interaction core serves a general-reference audience rather than an enterprise one

The variant axis does not change the core: entity-first inspection and typed-relationship traversal over a modeled graph remain the job in every form.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Knowledge Graph Platform | upstream | builds, integrates, and governs the graph (mapping, ingestion, entity resolution, ontology management); the explorer consumes the result |
| Graph Database Explorer | sibling, often confused | frame is the database instance — repositories, security, import, query monitoring; its graph views are a capability of that frame, while the explorer's frame is the knowledge itself |
| RDF / SPARQL Workbench | sibling, complementary | query-first: the user writes a query language and reads tabular results; the explorer is navigation-first and treats queries as an optional door |
| Semantic Search Platform | adjacent | search returns ranked results and ends there; the explorer begins at an entry point and continues into traversal |
| Data Catalog | adjacent | catalogs describe datasets (metadata about collections); the explorer traverses instances within one graph |
| Data Visualization Application | adjacent | renders arbitrary data for presentation; the explorer's visualization is a means to traverse live, governed graph data |
| General Reference Database / Online Encyclopedia | consumer-side cousin | presents curated human-readable records about entities; the explorer exposes the traversable statement graph behind entity-level knowledge |

The sharpest boundary is with the Graph Database Explorer, because both render subgraphs. The test is the center of gravity: if the product stops working when the graph database's administrative frame is removed, it is a database tool with exploration views; if it works for a domain expert who has no database-administration role at all, it is a Knowledge Graph Explorer.

## Representative Products

- **Stardog Explorer** — exploration application of an enterprise knowledge-graph platform; search and visual query building over a semantic model, deliberately separated from the platform's graph-building and query-authoring applications
- **Neo4j Bloom** — graph exploration application over a property graph, presenting curated business views ("perspectives") of the database to business users
- **AWS Graph Explorer** — open-source web application for visually exploring property-graph and RDF data across query dialects without writing graph queries
- **GraphDB Workbench (visual graph views)** — exploration views embedded in an RDF database console; included as the boundary case where database console and knowledge explorer meet

Older linked-data browsers — applications that rendered an RDF resource's typed properties as a page of followable links — are historical realizations of the same core, useful for checking that the definition does not overfit the modern canvas era.

## Sources

Research date: **2026-09-08**

- Neo4j — Neo4j Bloom user guide (overview; Perspectives): https://neo4j.com/docs/bloom-user-guide/current/ , https://neo4j.com/docs/bloom-user-guide/current/bloom-perspectives/
- AWS — Graph Explorer (official repository and documentation): https://github.com/aws/graph-explorer
- Stardog — Stardog documentation; Stardog Explorer chapter: https://docs.stardog.com/ , https://docs.stardog.com/stardog-applications/explorer/
- Ontotext / Graphwise — GraphDB 11.5 documentation; "Visualize and explore": https://graphdb.ontotext.com/documentation/ , https://graphdb.ontotext.com/documentation/11.5/visualize-and-explore.html

> Sourcing limitations: documentation for a semantic-suite exploration product (metaphacts) was unreachable from the research environment on 2026-09-08, and the user manual of a major public knowledge graph's query interface (Wikidata Query Service) timed out; neither could be directly observed, so no product-specific claims about them are made. Claims in this document are calibrated accordingly: behaviors stated generally are supported by the directly observed sample; the public-knowledge-graph variant is described conceptually. Precise product limits and defaults observed in the sample are deliberately not asserted here.
