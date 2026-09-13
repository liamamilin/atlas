# Research Notes — Graph Database Explorer

Research date: 2026-09-08

## Research Goal

Understand what a Graph Database Explorer is as an Application Type: what its world contains, who works in it, how a work session actually proceeds, and where its boundaries sit against the neighboring database-surface Types (Database Management Console, Knowledge Graph Explorer, RDF/SPARQL Workbench, SQL Client / SQL Workbench, Database IDE) and against visualization tools.

This pass also discharges two cross-check requests recorded by earlier passes:

1. **database-management-console** (processed 2026-09-07) recorded: "graph-database-explorer / vector-database-console / time-series-database-workbench / rdf-sparql-workbench are data-centric exploration Types — cross-check recommended where a sampled engine console also administers deployments."
2. **knowledge-graph-explorer** (processed 2026-09-08) drew the seam: "The DB explorer's frame is the *database instance*: repositories, security, import, query monitoring, admin. Its graph views are a capability of that frame… Test: remove the knowledge/semantic frame and what remains is a database console → the other Type."

## Initial Boundary (hypothesis before research)

A Graph Database Explorer is an interactive query-and-visualization surface over a live graph database: the user connects to a running database, issues queries in the engine's graph query language (Cypher / Gremlin / nGQL / …), inspects results in graph terms (nodes, relationships, paths, properties), and often works on the data itself (edit, import, schema). Expected confusions:

- **Database Management Console (§13, processed)** — deployment-centric (lifecycle, configuration, backups); the console pass predicted explorers are data-centric and only accrete administration as a secondary surface.
- **Knowledge Graph Explorer (§13 + §02.05, processed)** — knowledge/semantic frame (typed entities under a shared model, entity-first traversal); the DB explorer's frame is the database and its data.
- **RDF/SPARQL Workbench (§13, unprocessed sibling)** — the same data-centric query-surface shape over the RDF/triple-store engine class.
- **Database IDE (§12, processed)** — development loop over schema/objects/code; graph engines are typically schema-optional, which should weaken the IDE leg here.
- **Data Visualization Application / graph-viz tooling** — visualization of results is presentation, not the product's job.
- **The graph database itself / CLI clients** — the explorer is a surface, expected to ship as a component surface of one engine family (mirroring the console pass's component-view finding).

## Research Questions

1. What is the object of record — the deployment, the data, or the knowledge?
2. What is the working context (connection model, multi-database, authentication)?
3. What is the primary interaction — query language, point-and-click browse, or both?
4. What result forms exist, and how does the presentation preserve graph structure so exploration continues?
5. What data operations exist beyond querying (edit, import, schema/index management, export)?
6. What feedback surfaces exist (timings, plans, notifications, monitoring) and where does the console seam sit?
7. Read-only vs write?
8. Packaging: embedded console of the DBMS, standalone app, deployable web GUI, cloud companion?
9. Engine binding: single engine family vs multi-dialect?
10. How do older / leaner / text-mode surfaces fit the definition (historical check)?

## Representative Products

| Product | Why selected | Philosophy / delivery | Evidence |
|---|---|---|---|
| Neo4j Browser | The dominant graph DB's default developer surface | Query-console-first; embedded out-of-the-box (server, DBaaS, desktop) | A — official Browser manual root fetched |
| Memgraph Lab | Open-core vendor's standalone explorer; richest documented query loop | Query + visualization + in-canvas editing + optional monitoring; desktop and Docker/web delivery | A — official Lab overview + full Querying chapter fetched |
| NebulaGraph Studio | Separately deployed web GUI of a multi-component engine | Fused studio pole (schema + import + nGQL console); version-coupled to the engine | A — GitHub README + official docs page fetched |
| AWS Graph Explorer | Cloud provider's open-source exploration app; multi-dialect | Browse-first, "no query language knowledge required"; Gremlin/SPARQL/openCypher endpoints | A — official GitHub README fetched |

Sample spans: dominant DB vendor, open-core challenger, multi-component engine vendor, cloud provider. Delivery forms: embedded default tool, desktop/Docker app, deployable web GUI, open-source companion. Interaction philosophies: query-first (2), fused studio (1), browse-first (1). All four Tier A.

## Sources

Fetched 2026-09-08:

1. Neo4j Browser manual (root): https://neo4j.com/docs/browser-manual/current/
2. Memgraph Lab documentation (overview): https://memgraph.com/docs/memgraph-lab
3. Memgraph Lab documentation (Querying chapter): https://memgraph.com/docs/memgraph-lab/querying
4. NebulaGraph Studio — "What is NebulaGraph Studio": https://docs.nebula-graph.io/3.8.0/nebula-studio/about-studio/st-ug-what-is-graph-studio/
5. NebulaGraph Studio — official GitHub repository README: https://github.com/vesoft-inc/nebula-studio
6. AWS Graph Explorer — official GitHub repository README: https://github.com/aws/graph-explorer

Prior-pass context (read, not fetched this pass): research/database-management-console.md, research/knowledge-graph-explorer.md.

Attempted and abandoned per source-access rules:

- AWS Neptune user-guide pages (docs.aws.amazon.com/neptune/…) returned SPA shells without content (the same failure mode the knowledge-graph-explorer pass recorded); the official Graph Explorer GitHub README was used instead as the cloud-provider pole.
- Neo4j Browser manual subpages (guessed paths) 404'd; abandoned — Neo4j evidence rests on the manual root page only, and Neo4j-specific claims are held at that page's level.
- TigerGraph GraphStudio docs 404'd on first attempt; abandoned — the fused-studio pole is covered by NebulaGraph Studio.

## Product Observations

### Neo4j Browser (evidence layer A unless noted)

From the official Browser manual root:

- Self-description: "a developer-focused tool that allows you to execute Cypher queries and visualize the results. It is the default developer interface for both Enterprise and Community editions."
- Ships "out-of-the-box with all of Neo4j's graph database offerings" — Neo4j Server (Community and Enterprise), Neo4j AuraDB (DBaaS), Neo4j Desktop; in AuraDB and Desktop it is offered as the integrated tool **Query**.
- Main focus enumerated by the vendor: (1) writing and running graph queries with Cypher; (2) exportable, tabular results of any query result; (3) graph visualization of query results "containing nodes and relationships".
- Capabilities: "Running Cypher queries. Both read and write transactions. Some administrative and management capabilities."
- Audience per manual: developers, database administrators, quality engineers, data scientists, data architects.
- Not observed at this evidence level: specific admin capabilities, canvas interaction detail, scale guards. Held at the stated level; no precise claims drawn.

### Memgraph Lab (evidence layer A unless noted)

From the Lab overview and the full Querying chapter:

- Self-description: "a powerful visualization and management tool designed to help users interact with Memgraph database efficiently"; the querying chapter: "a visual interface that simplifies interaction with the Memgraph database… writing, executing, and visualizing Cypher queries".
- Delivery: desktop application; Docker container serving a web UI (localhost:3000); enterprise features supported in the Docker environment, some not on desktop. Quick-connect screen → connect to the running Memgraph instance.
- **Query execution surface (the vendor's named primary interface)**: Cypher editor (code suggestions with clause completion and signature info), Run query / Run selected / Cancel (cancel "terminate[s] the transaction"), parameters editor, share query (shareable link with query + style + parameters), run history, collections (saved query groupings that run embedded queries without copying them back).
- **Results**: two views — "Data results" (tabular, "displaying nodes, relationships, and their properties in a structured manner") and "Graph results" (renders "the nodes and relationships returned by the query"); copy/download results as JSON/CSV/TSV; fullscreen view.
- **Graph results interaction**: click node/relationship → property sidebar; Expand / Collapse / Hide (double-click toggles); search bar over result nodes by name; layouts — force (default, with physics preferences), tree, map (auto-activates when nodes carry numeric lat/lng properties); styling via a custom style language (Graph Style Script) with per-label/per-type display options.
- **In-canvas data management**: "Edit node … modify labels or properties. Changes are instantly written back to the database"; Remove node ("deletes the node and all connected relationships from the database"); Edit edge / Remove edge — "available only in Memgraph Lab version 3.11 or newer".
- **Scale and feedback**: rendering-limit guard ("When rendering a graph that exceeds the set rendering limits … you will be asked if you want to proceed with the graph visualization or switch to the data view"); default display cap of 5000 rows per result with truncation notice and actual total count; query status bar (success/error, execution times split Lab-roundtrip vs database execution, returned row/node/relationship counts); query summary with database-impact statistics (hops traversed, nodes/relationships created or deleted, labels added/removed, properties set), execution-plan breakdown and profile, server info (server address, protocol version, database name — "useful in multi-tenant environments"), and notifications (e.g., missing indexes, inefficient query patterns).
- **Other features** (overview page + TOC): monitoring (Enterprise — "tracks resource usage, database size, query activity, transaction flow, and active sessions"), GraphChat (natural-language input that "picks one of the available tools backed by Cypher queries"), SSO, sharing, multi-tenancy, data modeling, graph schema, CSV file import, query modules, streams, logs.
- Surrounding product family visible in docs: Memgraph Playground (online sandbox), Memgraph Cloud, MAGE algorithms — Lab is the local work surface within that family.

### NebulaGraph Studio (evidence layer A unless noted)

From the official docs page and the GitHub README:

- Self-description (docs): "a browser-based visualization tool to manage NebulaGraph. It provides you with a graphical user interface to manipulate graph schemas, import data, and run nGQL statements to retrieve data." README: "web-based visualization tool… create a graph schema, import data and edit nGQL statements for data queries."
- Deployment: RPM/DEB/Tar packages, Docker, Helm in Kubernetes — deployed separately from the database; a version-compatibility matrix couples Studio releases to engine versions ("The Studio version is released independently of the NebulaGraph core").
- Features (vendor-enumerated): **Schema page** — GUI to create the space, Tag, Edge Type, Index, and "view the statistics on the graph"; **Import page** — "batch import of vertex and edge data with clicks, and view a real-time import log"; **Console page** — "run nGQL statements and read the results in a human-friendly way".
- Stated scenarios: "explore and analyze data in a visualized way"; learning nGQL "using a GUI rather than a command-line interface (CLI)". An online playground exists for trying Studio functions.
- Authentication: sign-in uses the database's own accounts — "Users can log into Studio with the `root` account" when the database's auth is disabled; "When NebulaGraph enables authentication, users can only sign into Studio with the specified account." The explorer holds no parallel authority of its own.
- Boundary evidence within the same vendor lineup: monitoring/deployment observation is a **separate product** ("NebulaGraph Dashboard" with its own docs chapter), and a **CLI client** ("NebulaGraph Console") is listed separately among clients — the GUI explorer and the text console are different surfaces in the same family.

### AWS Graph Explorer (evidence layer A unless noted)

From the official GitHub repository README:

- Self-description: "a React-based web application that makes it easy to visualize and explore graph data, no query language knowledge required. Search for nodes, expand connections, and discover relationships across your graph database through an intuitive visual interface."
- Connectivity: "Connect to graph databases that support Apache TinkerPop Gremlin or W3C RDF/SPARQL over HTTP, or openCypher via Amazon Neptune." Multi-dialect but graph-database-only — no non-graph substrates.
- Three integrated views (vendor-named): **Graph View** — "Search, visualize, and explore connections between nodes with an interactive graph layout. Expand neighbors, filter by type, and run custom queries, all from a single view"; **Data Explorer** — "Browse all nodes for a given type in a paginated table. View every property at a glance and send nodes directly to the graph view for further exploration"; **Schema Explorer** — "See node types, their relationships, and property details rendered as an interactive schema graph."
- Deployment targets: Docker, EC2, ECS Fargate, SageMaker; open-source (Apache-2.0), deployed separately from the database.
- Not observed: write/edit capability, monitoring, connection-management depth. No claims drawn beyond the README.

## Cross-product Comparison

| Dimension | Neo4j Browser | Memgraph Lab | NebulaGraph Studio | AWS Graph Explorer |
|---|---|---|---|---|
| Working context | connects to Neo4j server / AuraDB / Desktop instance | quick-connect to running Memgraph | connects to NebulaGraph from a separately deployed web GUI | connects to Gremlin / SPARQL / openCypher endpoints |
| Primary interaction | write and run Cypher queries | Cypher editor with completion, parameters, run/cancel | Console page: run nGQL statements | browse/search-first; "run custom queries" available |
| Result forms | tabular (exportable) + graph visualization of returned nodes and relationships | table ⇄ graph; property sidebar; expand/collapse/hide; result search; JSON/CSV/TSV export | "read the results in a human-friendly way" (specific rendering not observed) | graph view + paginated type tables + schema view; send nodes table→graph |
| Element identity / continuation | results contain nodes and relationships (visualized) | click-to-inspect; expand neighbors; continue from any node | not directly observed | expand neighbors; nodes move between table and graph |
| Write capability | "both read and write transactions" | read + write; in-canvas edit/remove writes back (v3.11+) | nGQL console (engine language spans CRUD per engine docs TOC) | not observed |
| Schema/model surface | "some administrative and management capabilities" (unspecified) | graph schema + data modeling features (TOC) | Schema page: create space/Tag/Edge Type/Index, view graph statistics | Schema Explorer: types, relationships, properties |
| Import | not observed | CSV file import (TOC) | batch import of vertex/edge data with real-time log | not observed |
| Feedback / performance | not observed at this level | execution times, plan/profile, impact stats, notifications, status bar | not observed (import log yes) | not observed |
| Monitoring | not observed | Enterprise monitoring feature | separate product (NebulaGraph Dashboard) | not observed |
| Scale guards | not observed | render-limit guard + 5000-row display cap | not observed | paginated tables (implies guards) |
| NL assistance | — | GraphChat (NL → Cypher-backed tools) | — | — |
| Multi-database | Neo4j databases (plural) mentioned | multi-tenancy feature; database name in summary | "space" concept (engine-level) | per-connection |
| Auth model | not directly observed | SSO feature; "authorization and authentification to your database" | database's own accounts; no parallel authority | connection configuration |
| Packaging | embedded default tool of the DBMS (server/DBaaS/desktop) | desktop app + Docker/web | separately deployed web GUI (RPM/DEB/Tar/Docker/Helm) | open-source web app deployed by the user |
| Engine binding | single engine (Neo4j/Cypher) | single engine (Memgraph/Cypher-compatible) | single engine (NebulaGraph/nGQL) | multi-dialect, graph-only |

## Canonical Model (abstraction levels)

The Type's world, in conceptual terms:

```text
Connection (a specific running graph database, entered through the database's own authentication)
  └── Database / graph space (multi-database or space selection where supported)
        └── Stored graph data (nodes/vertices + relationships/edges, with labels/types and properties)
              └── Queries (the engine's own graph query language)
                    └── Results (returned in graph terms: elements, paths, values)
                          └── Presentation (graph rendering ⇄ tables; element inspection; continue exploring)
              └── Model surface (node/edge types, properties, indexes — view and sometimes manage)
```

### L0 — Defining Invariant

Three jointly-held structures, deliberately small:

1. **A live graph database as the working context.** The explorer operates against a specific running database of a graph engine family, entered through the database's own authentication; it is engine-bound (a single engine family, or a small set of graph query dialects — never arbitrary data substrates). Remove → a graph file viewer / visualization tool over ad-hoc edge lists.
2. **The stored graph data as the object of work.** The nodes/relationships (vertices/edges) and their properties held in the connected database are what the user's operations read and — in most products — change. Remove (object = deployment lifecycle/configuration/backups) → Database Management Console; (object = curated knowledge semantics under a shared model) → Knowledge Graph Explorer.
3. **Interactive graph-language queries with graph-native results.** The user issues queries in the engine's own query language and/or works through direct browse/expand interaction that the surface itself executes against the database; results come back in the graph's own terms with element identity preserved (which node, which relationship, what connects to it), so inspection and continued exploration are always possible. Node-link rendering is the common modern realization; tabular/text rendering that keeps element identity is the leaner form. Remove → batch reporting/BI over the database, or a static diagram.

Load-bearing: 1+2 without 3 = a data dump with no interactive surface; 2+3 without 1 = visualization over ad-hoc/in-memory graphs; 1+3 without 2 = nothing to work on (2 is the content anchor); 1+2 without query leg = a bare viewer below the Type.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- query editor with syntax assistance/completion, parameters, run/stop controls
- dual result rendering — graph canvas ⇄ table — with a detail/property view per element
- graph-canvas affordances: expand/collapse/hide, in-result search, layouts (force/tree/map appear across the sample), styling controls
- write operations: read and write transactions; some products edit/delete nodes and edges directly from the visualization, writing back to the database
- model surface: view (and in studio-shaped products, manage) node/edge types, properties, indexes; graph statistics
- query feedback: execution times, plans/profile, database-impact statistics, optimization notifications
- scale guards: rendering limits, result display caps with truncation counts, pagination in type-browse tables
- result export (tabular formats, images); run history, saved queries/collections, shareable query links
- data import (CSV-class) in studio-shaped products

### L2 — Variant / Optional Structure

- packaging: embedded default tool of the DBMS vs standalone desktop app vs separately deployed web GUI vs open-source companion app vs surfaces inside cloud-provider consoles
- breadth: pure explore/query surface vs studio (schema + import + console) vs business-user visualization companion that requires no query language
- monitoring/query-activity surfaces — carried as an optional feature (Enterprise tiers) or left to separate products (NebulaGraph Dashboard); the console seam
- natural-language → query assistance (era-current)
- multi-database / multi-tenancy support
- geospatial map rendering when nodes carry coordinates
- team features: sharing, SSO
- substrate: property-graph engines dominate the sample; multi-dialect tools may additionally speak RDF/SPARQL endpoints (the RDF-native pole belongs to the RDF/SPARQL Workbench sibling)

### L3 — Vendor-specific (research notes only)

- Neo4j: Browser offered as the "Query" tool in AuraDB/Desktop; Community/Enterprise editions; GraphAcademy course referral in docs.
- Memgraph: Graph Style Script (GSS) styling language; Orb rendering library; 5000-row default display cap; request-body-size environment variable; in-canvas editing gated to Lab v3.11+; Bolt protocol version in server info; Enterprise monitoring/SSO/sharing; GraphChat; MAGE algorithm context; Playground/Cloud/Zero(MemGQL) family surfaces.
- NebulaGraph: space/Tag/Edge Type/Index terminology; nGQL; VID; Studio released independently with a version matrix; Dashboard as a separate monitoring product; default `root` account when auth disabled; online playground; Community-vs-Enterprise split (algorithms/vector search moved to cloud); four deployment methods.
- AWS: TinkerPop Gremlin / RDF-SPARQL-over-HTTP / openCypher-via-Neptune connection matrix; the three vendor-named views; Docker/EC2/ECS-Fargate/SageMaker deployment targets; Apache-2.0.

## Vendor-specific Findings

See L3. Notable market facts: (a) the explorer ships as a component surface of one engine family in every sampled case — embedded default tool, vendor app, or vendor-adjacent companion — never a universal multi-engine SKU; (b) one vendor (Nebula) explicitly splits monitoring/deployment observation into a separate Dashboard product, evidence that the data-centric explorer and the deployment/observability console are distinct jobs; (c) one vendor (AWS) ships exploration as an open-source app decoupled from any single product UI while binding to graph endpoints only.

## Rejected Findings

- **"A graph explorer is a DBaaS/cloud console"** — rejected. Embedded server tools (Neo4j Browser), desktop apps (Memgraph Lab), and self-deployed web GUIs (NebulaGraph Studio) satisfy the core with no cloud machinery.
- **"Graph rendering is the defining structure"** — rejected. Rendering is the common presentation; the invariant is results in graph terms with preserved element identity (tabular/leaner forms satisfy; a text console that preserves element references is the thin ancestor pole).
- **"Query language authoring is the only entry"** — rejected. One sampled product (AWS Graph Explorer) leads with browse/expand and treats query authoring as optional; the invariant is interactive access to the stored graph, realized through queries and/or browse — every sampled product retains query capability somewhere in the surface.
- **"The explorer is read-only"** — rejected. Two sampled products explicitly write (Neo4j Browser read/write transactions; Memgraph Lab in-canvas writes); a studio-shaped product manages schema and import. Read-only posture is a variant, not the rule.
- **"The explorer includes monitoring"** — rejected as definitional. Monitoring appears as an Enterprise feature (Memgraph) and as a separate product (NebulaGraph Dashboard); it is the console/observability seam, common-optional at best.
- **"Schema design belongs to the explorer"** — rejected as definitional. Graph engines are commonly schema-optional; schema surfaces appear where the engine holds schema (studio pole, schema views) but the center remains data work.

## Boundary Findings

1. **vs Database Management Console (§13, processed) — cross-check DISCHARGED from this side.** The console's object is the running deployment (lifecycle, configuration, backups, accounts); the explorer's object is the stored graph data. Removal test holds: remove data exploration (administration only) → console; remove deployment administration → explorer. Sampled centers are data-centric: where adjacent administration appears it is secondary (Memgraph Lab's Enterprise monitoring) or a different product entirely (NebulaGraph Dashboard). Also confirmed the console pass's "no parallel authority" finding from this side: NebulaGraph Studio documents that sign-in uses the database's own accounts. Both leaves kept distinct; both documents cross-reference.
2. **vs Knowledge Graph Explorer (§13/§02.05, processed) — sharpest seam confirmed from this side.** The KG explorer's frame is knowledge: typed entities under a shared semantic model, entity-first traversal, curated business views, read-first. The DB explorer's frame is the database: engine query language as the working instrument, data management (write/import/schema) in scope, developer-facing. Removal test: remove the query/data-management frame (curated views over typed entities remain) → KG explorer; remove the semantic/knowledge frame (query + data work over raw graph data remains) → this Type. One sampled product straddles the packaging seam: AWS Graph Explorer is browse-first with type/schema views (KG-flavored interaction) but connects to raw graph databases without any curated knowledge layer — consistent with the KG pass recording it on the exploration side (no DB admin) and with this pass recording it on the DB side (no knowledge curation, graph-endpoint-bound). Both documents may keep it as a boundary specimen.
3. **vs RDF/SPARQL Workbench (§13, unprocessed)** — engine-class sibling: the same data-centric query-surface shape over RDF/triple-store engines with SPARQL as the language. Multi-dialect tools that can also connect to SPARQL endpoints (AWS Graph Explorer) sit between the classes. Cross-check recommended at that pass.
4. **vs SQL Client / SQL Workbench (§12/§13, unprocessed)** — the same family shape (interactive query surface over a live database) in the relational class; this leaf is the graph-engine-class member. Same center-of-gravity family; cross-check recommended at those passes.
5. **vs Database IDE (§12, processed)** — the IDE's center is the development loop (schema design, object development, code). Graph engines are typically schema-optional, so the schema-development leg is weaker here; schema surfaces in this sample (Nebula Schema page, Lab data modeling) serve the data work rather than a development artifact. Removal test holds both ways.
6. **vs Data Visualization Application / graph-viz tooling** — visualization here is the presentation of query results, bound to the connected database; products whose whole job is visualizing arbitrary graph data (or graph DBs as one more source) are a different Type.
7. **vs CLI clients / consoles** — the text-mode pole (a CLI console listed separately in the same vendor's client lineup) satisfies the query leg with element-preserving text results; it is the thin ancestor of this Type, below the "explorer" presentation leg. The GUI explorer and CLI console are different surfaces for the same engine.
8. **Component-view nature** — mirroring the Database Management Console and API Gateway Management Console precedents: the explorer is essentially never a standalone universal SKU; it ships as the exploration surface of one engine family or database service. The Type is genuine (distinct defining work: interactive work on the stored graph) but is realized as a component surface. Recorded for the directory author; no unilateral change.

## Uncertainties

1. **Neo4j Browser depth** — only the manual root page was reachable; canvas interaction, specific admin capabilities, and scale guards are not directly observed. All Neo4j-specific claims held at the root page's level.
2. **NebulaGraph Studio result rendering** — the docs page says results are readable "in a human-friendly way"; specific table/canvas forms were not directly observed (the Studio docs pages beyond the "What is" page were not fetched after initial 404s; only the README-linked page was fetched once confirmed).
3. **AWS Graph Explorer write capability** — not observed in the README; no claim made.
4. **TigerGraph GraphStudio / Dgraph Ratel / ArangoDB Web UI** — not sampled (fetch abandoned / out of budget). The fused-admin pole is covered by NebulaGraph Studio's schema/import/console shape; deeper admin-fused consoles may exist and would be boundary cases toward the Database Management Console.
5. **Older-generation explorers** (early desktop graph viewers, 2010s web consoles) were reasoned about but not fetched; the historical check rests on the CLI/console pole (directly evidenced as a separate surface in Nebula's client lineup) and on the deliberately canvas-free L0.

## Historical / Market-Sample Check

Applied before freezing the core: would older, regional, platform-native, or leaner products still fit?

- A text-mode console against a graph database (the directly evidenced CLI-client pole) satisfies legs 1–2 and the element-identity form of leg 3 — the thin ancestor. The L0 deliberately does not require web delivery, canvas rendering, import, monitoring, or any era-current feature. **Passes.**
- The sampled set includes a non-Western-origin vendor's product (NebulaGraph Studio) fully satisfying the core — no regional bias in the definition. **Passes.**
- A cloud-era-only reading (only managed-service companions) would exclude the embedded/desktop/self-deployed poles — deliberately rejected.
- Era-current capabilities (NL assistance, SSO, enterprise monitoring, sharing) are excluded from the core.

The defining core is written implementation- and era-agnostic: live graph database context + stored graph as object + interactive graph-language access with element-preserving results.

## Final Synthesis

A **Graph Database Explorer** is the interactive work surface over a live graph database, bound to one graph engine family or dialect set, whose object of work is the stored graph data itself — nodes, relationships, properties — reached interactively through the engine's own query language and/or direct browse-and-expand, with results returned in the graph's own terms so that element identity survives and exploration continues from any result. Around that core, mature explorers add dual graph/table rendering with element detail views, canvas affordances (expand/collapse, layouts, styling), write operations including in-visualization editing, model/schema surfaces, query feedback (timings, plans, impact statistics, notifications), scale guards, export, run history and sharing, and — in studio-shaped products — schema management and data import. The Type's disciplines: it administers nothing about the deployment itself (that is the Database Management Console's work; monitoring is an optional feature or a separate product), it carries no curated knowledge/semantic frame (that is the Knowledge Graph Explorer's frame), and it is always a component surface of one engine family rather than a universal product. Sibling engine-class query surfaces (RDF/SPARQL Workbench; the SQL family) share the family shape with a different substrate.
