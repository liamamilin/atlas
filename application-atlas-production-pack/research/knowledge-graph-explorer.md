# Research Notes — Knowledge Graph Explorer

Research date: 2026-09-08

## Research Goal

Understand what a Knowledge Graph Explorer is as an Application Type: what exists inside it, what users do with it, how exploration actually proceeds, and how it differs from the neighboring graph-related Types in the directory (Knowledge Graph Platform, Graph Database Explorer, RDF/SPARQL Workbench, Semantic Search Platform, Data Catalog, and the 02.05 reference-family Types).

## Initial Boundary (hypothesis before research)

A Knowledge Graph Explorer is an application for interactively navigating an existing knowledge graph: locating entities, inspecting their types/attributes/connections, and following relationships across the graph to understand structure. Expected confusions:

- Graph Database Explorer (§13) — developer/DBA console over a graph database.
- RDF/SPARQL Workbench (§13) — query-language-first interface.
- Knowledge Graph Platform (§13) — build/integrate/govern the graph.
- Data Catalog (§13) — metadata about datasets, not instances.
- General Reference Database / Online Encyclopedia (§02.05) — curated human-readable reference records.

Directory anomaly noticed immediately: the leaf "Knowledge Graph Explorer" appears **twice** in DIRECTORY.md — under §02.05 Reference & General Knowledge and under §13 Data, Analytics & AI Systems. Same name, same slug. Recorded as a Boundary Issue; this research covers the concept once, with the §13 (data/analytics) reading as the market's center of gravity and the 02.05 reading discussed under Boundary Findings.

## Research Questions

1. What is the unit of exploration, and what does an entity view contain?
2. How is the semantic layer (classes/types, ontology, vocabularies) surfaced during exploration?
3. What entry points exist into the graph (search, browse-by-class, saved views, queries)?
4. How does traversal work (expand, filter, path finding, scale guards)?
5. What presentation forms exist (node-link canvas, tables, schema diagrams, maps)?
6. Where do queries fit (visual builders, text queries, natural language)?
7. Read-only vs write: is exploration read-first? Where do corrections happen?
8. Packaging: standalone app, platform module, DB workbench surface, cloud companion?
9. Substrates: RDF triples vs property graph vs virtualized sources?

## Representative Products

| Product | Why selected | Tier/philosophy | Evidence quality |
|---|---|---|---|
| Stardog Explorer | Named "Explorer"; pure-play enterprise KG platform's exploration app | Enterprise, RDF/semantic, no-code audience | A — full official docs fetched |
| Neo4j Bloom | Graph-DB vendor's exploration app for business users | Property graph, business-view, perspectives | A− — overview + Perspectives TOC fetched; fine-grained feature pages not fetched |
| AWS Graph Explorer | Open-source, cloud-provider exploration app; multi-dialect | Developer-deployed viz app; property graph + RDF | A — official GitHub README/docs fetched |
| GraphDB (Workbench) Visual Graph | Triple-store workbench with embedded exploration views — boundary case toward Graph Database Explorer | RDF database console | A — full official docs fetched |
| metaphacts Platform | Semantic-suite exploration/app-building; would cover suite-embedded explorers | Semantic web suite | ✗ — docs unreachable (2 transport errors); not directly observed |
| Wikidata Query Service | Public/free knowledge graph exploration; consumer-adjacent pole | Public KG | ✗ — user manual timed out twice; not directly observed (conceptual knowledge only, no precise claims drawn) |

Sample spans: enterprise pure-play (Stardog), graph-DB vendor (Neo4j), cloud provider (AWS), RDF DB workbench (Ontotext/Graphwise), with two unreachable sources noted. Three data substrates covered (RDF, property graph, both).

## Sources

Fetched 2026-09-08:

1. Neo4j Bloom user guide (overview + Perspectives section): https://neo4j.com/docs/bloom-user-guide/current/ , https://neo4j.com/docs/bloom-user-guide/current/bloom-perspectives/
2. AWS Graph Explorer (official repo README/docs): https://github.com/aws/graph-explorer
3. Stardog documentation home + Stardog Explorer chapter: https://docs.stardog.com/ , https://docs.stardog.com/stardog-applications/explorer/
4. GraphDB 11.5 documentation (What is GraphDB + Visualize and explore): https://graphdb.ontotext.com/documentation/ , https://graphdb.ontotext.com/documentation/11.5/visualize-and-explore.html

Attempted and abandoned (per source-access rules):

5. metaphacts — https://documentation.metaphacts.com/ and https://dev.metaphacts.com/ — transport errors ×2 each host.
6. Wikidata Query Service User Manual — https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual — timeout ×2.
7. AWS Neptune user-guide page (https://docs.aws.amazon.com/neptune/latest/userguide/graph-explorer.html) — returned SPA shell without content; replaced by the official GitHub source (4).

## Product Observations

### Product 1 — Stardog Explorer (Evidence layer A)

Official framing: "the search and visualization tool for anyone to explore complex data fabrics easily, without code or queries." Web application. One of three Stardog applications: Designer (create KG), Explorer (browse/analyze), Studio (SPARQL IDE). Getting-Started flow literally goes: Introduction to KGs → "Browse a demo Knowledge Kit in Explorer" → "Creating a Knowledge Graph in Designer" → "Learn SPARQL in Studio".

Key observations:

- **Entry by search**: text search (full-text or starts/ends/contains patterns; searches restricted to `rdfs:label`, `rdfs:comment`, `skos:prefLabel`, `skos:definition` properties); class filter beside the search bar; "Visualize" button renders the model directly.
- **Query Builder**: visually define queries along relationship paths of the data model ("Explorer leverages your model to show the relevant relationships and attributes for each class"); aggregation filters (Group By, Sum/Avg/Count/Min/Max → SPARQL HAVING); AND NOT exclusions; save queries (stored queries, Private flag, tags; "Voicebox Query Prompt" saved queries with associated questions guide natural-language answering).
- **Entity detail**: "detailed views of each class"; instance views show connected properties (up to 10 instances per connected property), and properties are linked "so you can continue exploring".
- **Graph canvas**: select/drag-select nodes and edges; legend of class types with click-to-filter; auto-grouping of same-class nodes with same in/out relationships (drag out to ungroup, double-click to break); "Expand by" menu listing all incoming/outgoing relationships of selection; double-click expands all; warning when expansion exceeds 500 nodes; force-directed or tree layout; toggles for relationship labels/full node text.
- **Path queries**: shortest path between two classes or two instances (limit 20 hops); model-targeted for classes, instance-targeted otherwise.
- **Maps**: auto-detects geospatial attributes (GeoSPARQL / wgs lat-long) and renders nodes on an interactive map.
- **Settings/scope**: named-graph scope (all/virtual), reasoning schema choice, reasoning toggle, case-insensitive search. Virtual graphs (data virtualization) can be explored when "virtual transparency" is enabled.
- **Share/export**: share links (viewer sees the graph "from their permission set, not the original sharer's"); download tabular data.
- **Model criteria**: the UI is driven by the semantic model — classes must be OWL/RDFS classes or SKOS Concepts; relationships are ObjectProperties with declared domain/range; attributes are DatatypeProperties with domains. Models >1000 classes/relationships/attributes have restricted behavior (unbound relationships/attributes omitted from Expand-by, detail views, path expansion).
- **Scale constants (vendor-specific)**: top 50 text-search results; 100 instances per class variable in Query Builder results; ~5000 objects in visualization; 500-node expansion warning; 20-hop path limit.

### Product 2 — Neo4j Bloom (Evidence layer A−)

Official framing: "a graph exploration application for visually interacting with graph data… Bloom wraps that power into an interactive graph visualization environment, presenting a business view of the graph." Powered by the Neo4j graph database (property graph).

Key observations:

- Audience named by vendor: graph analyst (creates Perspectives, explores the "business graph"), graph evangelist, graph administrator (enables business users). Explicit business-user positioning.
- **Perspectives**: "a business view of the graph" — curated subsets/configurations of the database presented for exploration; creation, refresh (database scans), storage/sharing, and **role-based access control for Perspectives and Scenes** documented as first-class chapters.
- Components and installation, visual tour, "features in detail" chapters exist; the deeper feature pages (search phrases, scenes, parameterized searches) were not individually fetched in this pass — claims here are kept to the overview level.
- Terminology distinguishes exploration artifacts (Perspectives, Scenes) from the underlying database — same separation as Stardog Designer vs Explorer, but named differently.

### Product 3 — AWS Graph Explorer (Evidence layer A)

Official framing (repo description): "a React-based web application that enables users to visualize both property graph and RDF data and explore connections between data without having to write graph queries." "Search for nodes, expand connections, and discover relationships across your graph database through an intuitive visual interface."

Key observations:

- **No query language required** — the defining pitch; connects to Gremlin (TinkerPop), RDF/SPARQL over HTTP, or openCypher (via Amazon Neptune).
- **Three integrated views in one app**:
  - *Graph View* — "Search, visualize, and explore connections between nodes with an interactive graph layout. Expand neighbors, filter by type, and run custom queries."
  - *Data Explorer* — "Browse all nodes for a given type in a paginated table. View every property at a glance and send nodes directly to the graph view for further exploration." (table ⇄ canvas bridge)
  - *Schema Explorer* — "Understand your data model at a glance. See node types, their relationships, and property details rendered as an interactive schema graph."
- Deployment: self-hosted web app (Docker, EC2, ECS Fargate, SageMaker) connecting to your graph database — exploration is decoupled from the database product itself; open-source (Apache-2.0).

### Product 4 — GraphDB Workbench, "Visualize and explore" (Evidence layer A)

Context: GraphDB is an RDF triple store (database) with SPARQL, reasoning, connectors, clustering, admin tooling; the **Workbench** is its web UI. The Workbench also contains repository management, security, query monitoring, import/export — i.e., a database console that *embeds* exploration views. Boundary-relevant.

Key observations (from the "Visualize and explore" chapter):

- **Class hierarchy view**: nested-circle diagram of imported RDF classes sized by instance count; click a class → side panel (local name, IRI, instance count, first 1,000 instances, button to run auto-generated SPARQL listing all instances); slider to control classes shown; filter by named graph; export diagram as SVG.
- **Domain-range graph**: per-class view of properties with their domain and range (schema-level connectedness).
- **Class relationships view**: bundles of links between classes computed from *real statements* (not the schema); thickness = link count; per-pair top predicates; class list ordered by links; graph-scoped.
- **Resource exploration ("Easy graph")**: autocomplete IRI search as starting point ("explore the graph of your data without using SPARQL"); node colors by type; node size by RDF rank; hover shows types; default shows first 20 links sorted by RDF rank; expand (menu or double-click) / collapse / hide / focus; side panel with labels/description/rank.
- **Graph settings**: maximum links per expansion, label-language preference ordering, include schema statements, include inferred statements, expand over `owl:sameAs`, show/hide predicate labels, preferred and ignored types and predicates.
- **Custom visual graphs**: user-defined graph configurations composed of five SPARQL queries (starting point / graph expansion CONSTRUCT / node basics / edge basics / node extra) — power-user customization of what exploration means.
- **Save/share/embed**: saved graph state + config; shared graphs (editable only by owner; free-access users see shared only); embeddable via `&embedded` URL parameter that hides Workbench chrome — exploration surface as embeddable widget.
- **View/edit resources**: inspect all triples where an IRI is subject/predicate/object; add/edit triples in place; inferred statements cannot be edited. (Write capability inside the workbench — differs from dedicated explorers.)
- Companion chapters: "Exploring your data", "Graph path search", "Talk to Your Graph" (LLM), geospatial visualization — exploration is one cluster of the console's surfaces.

## Cross-product Comparison

| Dimension | Stardog Explorer | Neo4j Bloom | AWS Graph Explorer | GraphDB Workbench (Visual graph) |
|---|---|---|---|---|
| Entry point | text search (label/description properties) + class filter + Query Builder + saved queries | search over business graph via Perspective (details not fetched) | node search; table browse by type; schema view | autocomplete IRI search; class hierarchy browse; saved graphs |
| Entity view | class/instance detail with connected properties (linked to continue exploring) | node inspection on canvas | node details panel; Data Explorer table with all properties | side panel: labels, description, RDF rank; View-resource triples (S/P/O) |
| Traversal | Expand-by relationship menu; expand all; auto-grouping; shortest path (classes or instances) | interactive graph visualization; expansion per perspective | expand neighbors; filter by type | expand/collapse/hide/focus; default links per expansion; expand over owl:sameAs |
| Semantic layer visible | model-driven UI (OWL/RDFS/SKOS criteria); Visualize model button | Perspective as curated business view (ontology depth not observed) | Schema Explorer (types, relationships, properties) | class hierarchy, domain-range graph, class-relationship bundles, schema/inferred toggles |
| Query access | visual Query Builder → SPARQL; saved/shared queries | not directly observed (search-phrase mechanism not fetched) | "run custom queries" within Graph View | custom graph configs (5 SPARQL queries); SPARQL view nearby |
| Scale guards | 500-node expansion warning; 50/100/5000/20-hop caps | not observed | pagination in Data Explorer | max-links setting; 1000-instance lists; 20-link default |
| Sharing | share links render under viewer's permissions; download tabular | Perspectives/Scenes sharing + RBAC (TOC-observed) | (open-source app; collaboration not observed) | saved/shared graphs; embeddable iframe |
| Write capability | none in Explorer (build happens in Designer) | not observed | none observed (exploration app) | yes — edit/add triples on resources (inferred excluded) |
| Substrate | RDF (+ virtual graphs) | property graph | property graph (Gremlin/openCypher) + RDF (SPARQL) | RDF |
| Packaging | platform module (web app) of KG platform | module of graph DB platform | standalone open-source web app | embedded views of a DB console |
| Presentation extras | geospatial map; force/tree layouts | visualization environment | graph + table + schema views | hierarchy circles, bundle diagrams, SVG export, map (geo chapter) |

## Canonical Model (abstraction)

The Type's world, in conceptual terms:

```text
Knowledge Graph (persisted, typed: entities + typed relationships + attributes, under a shared model)
  └── Entity (identified, typed, labeled; carries attributes and connections)
        ├── Relationship (typed, directed connection to another entity)
        └── Type / class membership (the semantic frame: vocabulary, hierarchy, domain/range)
  └── Exploration state (the accumulating subgraph a user has assembled: entry entity + expansions + filters)
```

Three jointly-held structures:

1. **The existing typed graph as the subject of exploration.** The application consumes a graph that already exists — entities carry types/classes, relationships carry names/types, both may carry attributes, and a shared model (schema, ontology, vocabulary — however light) governs what can appear. The explorer is read-first; building, loading and governing the graph is another application's job (KG platform / DB tooling). Remove → network/graph visualization over ad-hoc edge lists (no semantics), or a plain DB tool.
2. **Entity-first inspection.** The user reaches an *identified entity* through a knowledge-aware entry surface (label/keyword search with autocomplete, browse-by-class, saved/shared views) and sees it as a meaningful object — its type, human-readable label, attributes, and its connections. Remove → a raw query console returning tables.
3. **Relationship traversal as the primary interaction.** From any inspected entity the user follows its typed relationships to connected entities and continues outward; the accumulation of visited entities and links is presented so the structure stays visible (node-link canvas in most current products; traversable property lists are an older/leaner realization). Remove → a single-record reference viewer (encyclopedia-card behavior).

L0 = 1+2+3 jointly held. Historical check (§24): Linked Data browsers of the mid-2000s (e.g., resource-rendering browsers over RDF, Tabulator-style) satisfy 1–3 — typed resources, typed followable properties, entity pages — with no canvas visualization, no query builder, no AI. The core therefore must not require canvas visualization, visual query building, or any current-era feature. Passed.

### L1 — Common Mature Structure (not definitional)

- node-link graph canvas: layouts, zoom, selection, node grouping/collapse, legends, expand menus
- entity search over label/description properties with autocomplete; class/type filters
- browse-by-class and schema-level overviews (class hierarchy, class relationships, domain-range, schema graph)
- scale guards: expansion limits, warnings, paginated tables, per-expansion link caps
- filtering by class/type, predicate, direction; language preferences for labels
- visual query building along model paths; saved and shared queries/views
- shortest-path/path finding between entities
- share links (rendered under the viewer's own permissions), saved states, export (image/tabular)
- permission-gated visibility / RBAC in enterprise deployments
- read-first posture (dedicated explorers); table ⇄ canvas bridges; detail side panels

### L2 — Variant / Optional Structure

- substrate: RDF/SPARQL, property graph (labels/relationship types), or virtual graphs over external sources; multi-dialect support
- packaging: standalone open-source app; platform module of a KG suite; embedded views inside a DB workbench (straddling Graph Database Explorer); embeddable no-chrome widget; cloud-provider companion
- semantic depth: full ontology + reasoning (inference toggles change what is visible) vs light label/type model
- geospatial map rendering of located entities
- natural-language / LLM question answering over the graph (era-current; present in several vendors' stacks but not part of the exploration core)
- custom graph configurations (define expansion/labeling semantics via queries) — power-user feature
- in-place statement editing (workbench-style) vs strictly read-only exploration
- audience posture: business-user no-code vs data-engineer-flavored

### L3 — Vendor-specific (kept out of the final document)

Stardog: Knowledge Kits, Voicebox Query Prompts, named-graph/virtual-transparency scope settings, exact caps (50 search results, 100 per class variable, ~5000 objects, 500-node warning, 20 hops), the exact rdfs:/skos: search-property set, model-size restriction (>1000 classes). Neo4j: Perspectives/Scenes as named artifacts, role-based access control for them. AWS: Gremlin/openCypher/SPARQL connection matrix, deployment targets (Docker/EC2/ECS/SageMaker), three-view naming. GraphDB: RDF rank sizing, default 20-link expansion, five-query custom graph configs, `&embedded` parameter, free-access mode behavior, autocomplete-index prerequisite, SVG export.

## Vendor-specific Findings

See L3 above. Notable vendor-market facts: Stardog ships exploration as a *separate application* from graph building (Designer) and querying (Studio) — market evidence that build/query/explore are distinct jobs. GraphDB embeds exploration inside a database console — evidence for the Graph-Database-Explorer boundary being porous in packaging but distinct in center of gravity. AWS ships exploration as a standalone open-source app decoupled from any single product UI.

## Boundary Findings

- **vs Knowledge Graph Platform (§13)**: the platform builds/integrates/governs the graph (mapping, ingestion, entity resolution, ontology management, virtualization); the explorer consumes it. Same vendor splits them (Stardog Designer vs Explorer). If the product's primary job is producing/curation of the graph, it is the platform; if it is navigating/understanding the resulting graph, it is this Type.
- **vs Graph Database Explorer (§13)**: sharpest seam. The DB explorer's frame is the *database instance*: repositories, security, import, query monitoring, admin. Its graph views are a capability of that frame. This Type's frame is the *knowledge*: entities, classes, meanings, traversal. GraphDB Workbench straddles (admin console + explore views); AWS Graph Explorer and Bloom sit cleanly on the exploration side (no DB admin); Stardog Explorer cleanly (no admin, no build). Test: remove the knowledge/semantic frame and what remains is a database console → the other Type; keep the knowledge frame and the DBA surfaces become irrelevant → this Type.
- **vs RDF/SPARQL Workbench (§13)**: query-first (write SPARQL, tabular results) vs navigation-first (start from an entity, follow links; queries optional/translated). Coexistence in the same products (GraphDB SPARQL view next to Visual graph; Stardog Studio next to Explorer) shows they are different surfaces for different jobs, not the same Type.
- **vs Semantic Search Platform (§13)**: search returns ranked results; exploration *continues* from an entry point into traversal. Search is one entry surface here, not the whole job.
- **vs Data Catalog (§13)**: catalogs describe datasets (metadata about collections); this Type traverses instances inside one graph. A vendor "knowledge catalog" module (Stardog's) is platform-side metadata, not the explorer.
- **vs Online Encyclopedia / General Reference Database (§02.05)**: encyclopedias present curated human-readable articles; this Type exposes the traversable statement graph. A public knowledge graph like Wikidata sits at the seam (both a reference resource and a graph), which is likely why the leaf name appears in both sections of the directory. The 02.05 reading ("explore general knowledge as a graph") is a domain/audience variant of the same interaction core, not a different structure — the structures (entity, typed relationship, traversal) are identical; only the content domain and audience differ.
- **vs Data Visualization Application**: ad-hoc charting/visualization of arbitrary data vs live traversal over a governed typed graph. Visualization is a *presentation* here, not the product.
- **Remove-what test**: remove the typed/semantic layer → network analysis / graph visualization tool (different Type); remove entity-first inspection → query workbench; remove traversal → record viewer/reference card.

## Uncertainties

1. metaphacts not directly observed (docs unreachable ×2) — the "suite-embedded explorable-app builder" segment is inferred from Stardog/GraphDB packaging patterns only. No claims about metaphacts specifics are made anywhere.
2. Wikidata Query Service not directly observed (manual timeout ×2) — the public/free pole and the 02.05 adjacency rest on conceptual reasoning, marked as such. No precise claims drawn from memory.
3. Bloom's fine-grained mechanics (its search-phrase language, scenes) were not fetched; Bloom observations kept to overview + Perspectives structure level.
4. Whether standalone "Knowledge Graph Explorer" products (independent of any platform/DB) form a large market: evidence suggests the common packaging is module/surface/embedded-app; standalone open-source exists (AWS). Treated as packaging variant, not a taxonomy problem.
5. Write-capability spread: observed read-only in dedicated explorers (Stardog explicitly, AWS implied by description) and in-place editing in a DB workbench (GraphDB). Medium-confidence generalization: dedicated explorers are read-first; corrections flow through build/edit surfaces — stated moderately in the final doc.

## Final Synthesis

A Knowledge Graph Explorer is the navigation-and-understanding surface over an existing knowledge graph. Its defining core is small: a persisted typed graph (entities + typed relationships + attributes under a shared model) as the subject; entity-first inspection (reach an identified entity, see its type/label/attributes/connections); and relationship traversal as the primary interaction, with the accumulated structure kept visible. Everything else — canvas layouts, schema diagrams, visual query building, path finding, maps, sharing/RBAC, reasoning toggles, natural-language answering — is common mature or optional structure, and the exact interaction limits are vendor detail. Its nearest neighbors are separated by center of gravity: the platform *builds* the graph, the DB explorer *operates* the database, the SPARQL workbench *queries* it, and this Type *traverses and understands* it.
