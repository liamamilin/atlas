# Research Notes — Knowledge Graph Platform

Research date: 2026-09-08

## Research Goal

Understand what a Knowledge Graph Platform is as an Application Type in §13 Data, Analytics & AI Systems: what its world contains, what its defining work is, who builds and consumes the graph, how construction → governance → serving actually proceeds, and where its boundaries sit against the neighboring graph Types the directory already documents (Knowledge Graph Explorer, Graph Database Explorer, RDF/SPARQL Workbench) and the adjacent data Types (Data Catalog, Data Fabric, Metadata Management, Enterprise Search, RAG/assistant Types).

This pass also discharges an explicit delegation recorded by the knowledge-graph-explorer pass (processed 2026-09-08): "read-first by construction (build/govern → Knowledge Graph Platform, database operation → Graph Database Explorer, query authoring → RDF/SPARQL Workbench)". The build/govern side of that seam is defined here.

## Initial Boundary (hypothesis before research)

A Knowledge Graph Platform is the platform on which an organization builds, governs, and serves a knowledge graph: it models a domain (ontology/schema/vocabulary), turns heterogeneous sources into graph content mapped to that model (ingestion, virtualization, mapping, entity resolution, curation), governs the resulting asset (security, versioning, quality, provenance), and serves it to consumers (query, APIs, search, applications, AI). Hypothesized confusions:

- Graph databases (product class, not a directory leaf; nearest leaves are Graph Database Explorer / Database Management Console) — the storage engine vs the platform above it.
- Knowledge Graph Explorer (§13, processed) — consumption/traversal surface; this Type builds and governs.
- RDF/SPARQL Workbench (§13) — query-authoring surface; often included in the platform as one module.
- Data Catalog (§13) — metadata about datasets; some KG platforms ship catalog modules, and at least one catalog product runs on a graph substrate.
- Data Fabric / Metadata Management (§13) — estate-wide data layers whose metadata layer may itself be a knowledge graph.
- MDM (§13) — golden-record management; overlaps on entity resolution.

## Research Questions

1. What is the platform's asset of record, and what does the vendor's own "knowledge graph" definition contain?
2. How is the graph constructed: modeling (what standards), mapping (source → model), ingestion vs virtualization, entity resolution, curation?
3. How is it governed: security model, versioning/lifecycle, quality constraints, provenance?
4. How is it served: query languages, SQL/BI, APIs, search, inference, application/explorer surfaces, AI answering?
5. Who works in the platform (engineers, ontology/knowledge engineers, domain experts, stewards, admins, developers)?
6. What is the relationship to underlying storage: own engine, storage-agnostic middleware, hosted SaaS?
7. Where is the line between "platform" and "graph database" — does the sampled market draw it, and where?
8. Does the platform Type remain recognizable without the era-current features (visual no-code modeling, virtualization, GenAI/RAG layers)?

## Representative Products

| Product | Why selected | Philosophy/tier | Evidence |
|---|---|---|---|
| Stardog | Enterprise KG platform pure-play; docs document the entire build/govern/serve estate | Engine-included enterprise platform (RDF) | A — docs home, KG intro, Designer chapter fetched in full |
| metaphactory (metaphacts) | Storage-agnostic KG platform over SPARQL stores; modeling/curation/app-building suite | Middleware platform, RDF/open-standards, domain-expert audience | A− — official product page with full feature tabs fetched (help docs remain unreachable, as in the explorer pass) |
| Neo4j | Property-graph market leader; KG positioned as a design pattern on its platform; GenAI tooling | Database-centered platform, developer-first | A — official knowledge-graph use-case page fetched |
| data.world | Cloud platform whose catalog runs on a knowledge-graph substrate; governance/catalog posture | SaaS catalog-first packaging of a graph substrate | A− — docs home + developer API reference fetched; KG architecture visible via API semantics (IRI resources, relationships, layered model, SPARQL endpoints) |
| Ontotext GraphDB (cross-reference only) | RDF database whose workbench embeds exploration/admin — used by the sibling pass as the DB-console pole | Not re-fetched this pass; cited from sibling research notes for the DB-vs-platform seam |

Sample spans: engine-included enterprise (Stardog), storage-agnostic suite (metaphactory), database-centric developer platform (Neo4j), SaaS governance/catalog packaging (data.world). Two substrates (RDF, property graph) plus one hosted graph substrate. PoolParty (semantic middleware, taxonomy-first) was targeted as a fifth sample but its docs host was unreachable (2 transport errors); abandoned per source-access rules and recorded under Uncertainties.

## Sources

Fetched 2026-09-08:

1. Stardog documentation home: https://docs.stardog.com/
2. Stardog — Getting Started Part 1: Introduction to Knowledge Graphs: https://docs.stardog.com/getting-started-series/getting-started-1
3. Stardog — Stardog Designer chapter: https://docs.stardog.com/stardog-applications/designer/
4. metaphacts — metaphactory product page (feature tabs): https://www.metaphacts.com/product
5. Neo4j — Knowledge graph use case: https://neo4j.com/use-cases/knowledge-graph/
6. data.world — docs home: https://docs.data.world/en/ ; developer docs: https://developer.data.world/ ; API reference index: https://developer.data.world/llms.txt

Attempted and abandoned (per source-access rules):

7. PoolParty — https://docs.poolparty.biz/ and https://docs.poolparty.biz/en/ — transport errors ×2.
8. metaphacts help/documentation (https://documentation.metaphacts.com, https://help.metaphacts.com) — unreachable in the sibling pass (×2 transport errors); not retried; the vendor's product page (4) was reachable and is used instead.

Cross-referenced (not re-fetched): Ontotext GraphDB documentation and Stardog Explorer observations from research/knowledge-graph-explorer.md (2026-09-08); graph-database-explorer pass notes (2026-09-08).

## Product Observations

### Product 1 — Stardog (Evidence layer A)

Vendor's own definition of the Type's asset: "We define knowledge graph as a representation of data that is enriched with real-world context, is based on the graph data structure, and has a flexible schema that allows for multiple definitions of the same data." And: "a graph database is still only designed to support one point of view, whereas the knowledge graph's schema supports multiple points of view."

Platform scope observed in the docs tree:

- **Applications split by job**: Stardog Designer ("no-code, visual tool for creating and maintaining your Knowledge Graph"), Stardog Explorer (browse/analyze), Stardog Studio (SPARQL IDE). Build / explore / query are deliberately separate applications — market evidence that construction and consumption are distinct jobs.
- **Construction machinery**: Designer projects organize "data modeling and mapping efforts"; data models use "OWL and RDFS standards to ensure data models are compatible with open source semantic tools"; multiple data models per project (each with its own namespace); inference rules defined in If…Then form "to capture business and domain logic"; mapping view maps project resources (CSV files, relational sources via virtual graphs) to model concepts, with a machine-generated "mapping suggestions" service, and "a primary identifier... used to identify unique class instances" as the requirement for a completed mapping; publishing to the platform endpoint is permission-gated. AI assistance ("AI Hints") documents domain terminology for the NL layer; Voicebox can drive "guided ontology creation and mapping".
- **Integration machinery**: Virtual Graphs chapter — connectors to SQL/NoSQL data sources, mapping data sources, "Virtual Transparency" (query virtualized sources through the graph), import JSON/CSV, optimization; external compute (Databricks/EMR/Spark) for materialization and entity resolution at scale.
- **Entity Resolution**: dedicated capability with its own security chapter and CLI; also executable on external compute.
- **Governance machinery**: Security model with named-graph security, virtual-graph security, fine-grained security, Kerberos/LDAP/OAuth; entity-resolution security; Data Quality Constraints (ICV — SHACL-class) "help ensure data is correct by finding, flagging, and/or preventing conflicting data"; Knowledge Catalog module (external catalogs, secrets); database administration (backup/restore, checkpoints, transaction logs, optimization).
- **Serving machinery**: SPARQL (+ path queries, full-text, geospatial, GraphQL, SQL via a BI server), stored queries/functions, label service; Inference Engine ("displays all logic for each result" — explainable derivation); graph analytics (algorithms, Spark); machine learning; BI-tools-over-SQL; programmatic access (Java/Python/JS/.NET/HTTP API); Voicebox ("conversational AI interface... Translates questions into SPARQL queries and returns grounded, hallucination-free answers"; processes unstructured documents).
- **Operations**: server install (Docker/AWS/Azure/K8s), HA cluster (cache/standby/replica nodes), monitoring/capacity planning; cloud (Stardog Cloud) and self-managed editions; Launchpad for login-provider integration.

### Product 2 — metaphactory / metaphacts (Evidence layer A−: official product page, full feature tabs)

Self-positioning: "Enterprise knowledge graph platform turning complex data into trusted AI-powered insights", "Knowledge graph platform based on open standards", "an enterprise knowledge graph-based platform that leverages semantic knowledge modeling and knowledge discovery capabilities". Explicitly vendor-independent over storage: "Repository Management — Vendor-independent proxy over multiple SPARQL 1.1 compliant data repositories including access control"; federation engines federate "multiple SPARQL endpoints under a single virtual endpoint".

- **Semantic knowledge modeling**: visual modeling interface for "creating, importing, extending & editing, exploring, visualizating and documenting semantic models" for technical and non-technical users; "the visual language translates to core elements of OWL and SHACL"; vocabulary & taxonomy management (SKOS, hierarchies, multilingual synonyms, tree visualization, import/export); data catalog integration (DCAT, Dublin Core — dataset metadata becomes part of the graph); import of public ontologies (MeSH, FIBO, schema.org, ISO15926, IDMP…); publishing of semantic models via API and web app.
- **Collaboration & asset governance**: multi-role collaboration (knowledge graph engineers, taxonomists, domain experts/SMEs, business users); "Cataloging, import/export, versioning and metadata management for semantic models, vocabularies and datasets"; lifecycle and change management ("from 'In development' to 'In review'" status model, lock/unlock for review, notifications); Git integration for versioning; "Detailed provenance documentation of an asset's creation, owner, history and changes"; roles & permissions.
- **Serving**: search (semantic search, facets, synonym search via controlled vocabularies, pathfinding); visualization & interactive exploration; authoring via "model-driven semantic forms" with provenance capture; personal/collaborative knowledge organization; **model-driven application building** (no-code wizards selecting classes/relations/attributes from the model; declarative Web Components; templating; role-based access; SSO via OIDC/OAuth/SAML/JWT).
- **Knowledge graph management (middleware)**: data access services (SPARQL 1.1 Protocol, Graph Store HTTP Protocol, Linked Data Platform, content negotiation); hybrid + transparent federation; **Query as a Service** ("template queries and expose them during runtime as dynamic and parameterisable REST APIs" with "controlled access to published query results using access permissions, data hiding, and encapsulation"); label/description/lookup services; data & query engineering (ingestion, connectors, profiling, namespace management, SPARQL editor, query catalog); data quality (SHACL-based rule engine, validation reports, quality dashboards).
- **AI layer**: conversational interface (NL2SPARQL generation/refinement/execution; RAG for unstructured queries); AI-assisted semantic modeling (suggestions for mapping concepts to physical data); "neuro-symbolic integration" — LLM agents grounded in the semantic model.
- **Deployment**: on-premise or cloud (AWS Marketplace); Docker microservice packaging; works with a list of compatible graph databases (storage engine NOT included).

### Product 3 — Neo4j (Evidence layer A)

Positioning: "A knowledge graph is a design pattern for storing, organizing, and accessing interrelated data entities, including their semantic relationships." "You can quickly design, implement, and evolve your knowledge graph with Neo4j."

- Capabilities advertised for knowledge graphs: property graph model (nodes/relationships/properties), flexible schema ("Introduce new data, properties, and relationships without rebuilding the database"), Cypher query language, Graph Data Science ("65+ production-ready algorithms — including node embeddings, similarity metrics, and community detection"), native performance architecture, "Extensive Data Integrations — native drivers, connectors, and no-code import tools".
- Construction-side story: "Constructing knowledge graphs with LLMs" (GraphAcademy course), LLM Graph Builder (labs project), "Entity resolution for knowledge graphs" tutorials/blog ("Entity resolved knowledge graphs"), full-graph migration from triple stores, ontology learning from graph data (webinar series).
- Use cases: fraud detection ("Connect disparate data across your business... Analyze billions of data connections"), customer 360/recommendation, semantic search/GenAI ("GenAI-powered semantic search"), GraphRAG ("knowledge graph... vastly improves the retrieval portion of RAG... capturing evidence provenance" — quoted from Gartner-attributed material).
- Scale claim: "1,700+ organizations build with Neo4j-powered knowledge graphs."
- Interpretation for the Type boundary: the product is a graph DBMS platform; its knowledge-graph posture is delivered by (a) the flexible-schema data model, (b) a construction tooling layer (LLM Graph Builder, import tools, entity-resolution guidance), and (c) serving tooling (GDS, search/GenAI integration, explorer). The same company markets the DBMS alone to graph-database buyers — the straddling pole between "database" and "knowledge graph platform".

### Product 4 — data.world (Evidence layer A−: docs home + developer/API reference)

User-facing docs are catalog-first (Catalog Toolkit, metadata collectors for dozens of sources, glossary, lineage, organization/user-group administration, SSO/SCIM). The knowledge-graph architecture is visible in the developer API semantics:

- Resources of any type are **addressed by IRI** ("Get a resource... Return details about a resource of any type in the organization"; "Get resources that are related to a resource identified by IRI").
- **Directed relationships** between resources are first-class API objects ("Creates a relationship between two catalog resources identified by IRI... with one being the source and the other the target"; delete-equivalent).
- The substrate is described by the vendor as a **catalog graph with a layered model**: "The data.world catalog graph relies on a layered model that keeps the content from collected source systems separate from edits made by end users on the platform. This allows the collected source system data to update regularly without overwriting enrichment and curation efforts that are authored on data.world."
- **SPARQL endpoints per organization** (SELECT/CONSTRUCT/DESCRIBE/ASK with RDF result formats; named-graph semantics — a ":current" default graph per org) alongside SQL; saved queries; datasets/projects; metadata collectors; quality checks/badges; automation triggers; AI Context Engine starter kits; natural-language answer endpoints over structured data.
- Interpretation for the Type boundary: the knowledge graph here is the platform substrate; the product's center of gravity is data cataloging/governance. This is the seam specimen for the Data Catalog boundary — graph substrate, catalog surface.

## Cross-product Comparison

| Dimension | Stardog | metaphactory | Neo4j | data.world |
|---|---|---|---|---|
| Asset of record | knowledge graph ("flexible schema... multiple definitions") | knowledge graph over open standards (OWL/SHACL/SKOS) | knowledge graph as design pattern over property graph | catalog graph (IRI-addressed resources + directed relationships) |
| Own storage engine | yes (RDF databases; db lifecycle, backup, HA) | no — vendor-independent proxy over SPARQL 1.1 repositories | yes (property graph DBMS; DBMS is the core product) | hosted substrate (opaque); org-scoped SPARQL |
| Modeling standards | OWL/RDFS data models; multiple models per project; inference rules If…Then | OWL/SHACL visual language; SKOS vocabularies; public ontology import | property graph model; flexible schema; ontology tooling via ecosystem | org metadata model (catalog toolkit); IRIs + typed resources |
| Source → graph machinery | virtual graphs (SQL/NoSQL connectors), CSV/JSON import, mapping UI with suggestions + primary identifiers, publish gated by permissions | data ingestion + connectors; federation (hybrid + transparent) over endpoints; mapping suggestions via AI | drivers/connectors + no-code import tools; LLM Graph Builder; entity-resolution tutorials | collectors (catalog metadata from dozens of sources); datasets/files/streams; virtual connections |
| Entity resolution | first-class capability (dedicated chapter, security, external compute) | not on the observed page as a named module (curation/forms with provenance instead) | tutorial/methodology level (entity-resolved KGs) | implicit in layered identity/collection (not named ER) |
| Quality machinery | Data Quality Constraints (ICV; find/flag/prevent conflicting data) | SHACL rule engine, validation reports, quality dashboards | (not observed on the fetched page) | quality checks/badges (API) |
| Governance | named-graph/virtual-graph security, fine-grained security, users/roles, Kerberos/LDAP/OAuth | roles & permissions, lifecycle statuses (in development → in review), Git versioning, provenance, notifications | (admin exists; not the fetched page's focus) | org/user groups, SSO/SCIM, admin tokens, approval statuses |
| Serving surfaces | SPARQL (+path/full-text/geo/GraphQL), SQL/BI server, stored queries, apps (Designer/Explorer/Studio), Voicebox NL | search, exploration, visualization, model-driven app building, Query-as-a-Service REST APIs, conversational interface | Cypher, GDS algorithms, GenAI/GraphRAG integration, drivers | SQL + SPARQL APIs, search, NL answer endpoints, AI Context Engine |
| AI layer | Voicebox (NL→SPARQL, grounded answers, unstructured docs), AI Hints | NL2SPARQL + RAG conversational interface; neuro-symbolic agents | GenAI/GraphRAG positioning; LLM Graph Builder | AI Context Engine; NL answer API |
| Audience emphasis | enterprise data teams + no-code graph builders | domain experts/SMEs + business users + engineers | developers | data governance/catalog organizations |
| Deployment | self-managed (Docker/K8s/marketplaces) or managed cloud | on-prem or cloud (AWS Marketplace), Docker microservices | self-managed or cloud DBMS | SaaS |

## Canonical Model (abstraction)

### L0 — Defining Invariant (three jointly-held structures)

1. **The knowledge graph as the platform's asset of record.** A persisted — or virtually unified — graph whose members are individually identified entities and named, typed relationships, governed by a shared semantic model (schema, ontology, controlled vocabulary — however formal or light) that the organization maintains and evolves. The graph is a lasting shared asset, not one application's transient data. Remove → a graph database's contents, an ontology file, or an ad-hoc graph project; the Type's "knowledge" frame collapses.

2. **Construction machinery: the platform turns sources into the graph and keeps it current.** The platform itself provides the means by which heterogeneous source content is connected, mapped into the shared model, and maintained: ingestion or virtualization of sources, mapping source fields/tables to model concepts, resolving/identifying entities, curated correction (by engineers and/or domain experts), and — in mature products — constraint-based quality checking. Construction may be code-first, visual/no-code, or AI-assisted; what is definitional is that the platform owns the source→model pipeline, not merely the storage of whatever a user already built. Remove → a graph DBMS or a visualization tool; the platform's defining work disappears.

3. **Governed serving of the graph to consumers beyond its builders.** The platform operates the graph as a shared resource: query surfaces (graph query language, and commonly SQL/BI/REST/GraphQL), search, permission-gated access for multiple users and applications, and typically derivation features (inference/rules) and derived-view protection. The consumers are downstream surfaces — explorers, BI, applications, AI assistants — built on top. Remove → a modeling/mapping studio whose output is files, not an operating platform.

Jointly-held is load-bearing:

- 1 alone → a graph database or a shared ontology document.
- 2 without 1+3 → an ETL/mapping project with no semantic asset and no consumption surface.
- 3 without 2 → a query engine/DBMS serving whatever graph exists (the graph-database pole).
- 1+3 without 2 → still a graph database with security (the classic DBMS shape); the market draws exactly this line — the same vendors sell the DBMS alone and the KG platform as different things (Neo4j straddles visibly; Stardog names its DB and its platform separately).
- 2+3 without 1 → integration pipelines with no knowledge frame; nothing distinguishes the result from ordinary data integration.

**Historical / market-sample check (passed).** The mid-2000s semantic-web stack satisfies all three legs with none of the modern apparatus: an RDF triple-store server (Sesame/Jena-class) + an ontology authored in RDFS/OWL (leg 1) + RDB-to-RDF mapping (D2RQ-class) and/or direct RDF authoring with batch load (leg 2) + a SPARQL endpoint with repository-level access control and OWL reasoning (leg 3). No visual modeling, no virtualization marketing, no cloud, no AI. An analog-level reading (shared controlled vocabulary/thesaurus + curated records linked by it + retrieval service, as in library authority-file systems) also fits the frame conceptually. Therefore the definition must not require: visual/no-code modeling, virtualization, entity resolution as a named module, GenAI layers, or cloud delivery. All of those are L1/L2.

### L1 — Common Mature Structure (not definitional)

- **Data virtualization / federation** — querying sources in place under the model (virtual graphs; transparent federation of endpoints) as an alternative or complement to materialization. Common, not definitional (early platforms were batch-load only).
- **Entity resolution / linking** — named module in some products (Stardog), methodology in others (Neo4j ecosystem), implicit in others (data.world).
- **Inference / rules** — OWL/RDFS reasoning, user-defined If…Then rules, SHACL rule engines; explainability of derived facts (Stardog "displays all logic for each result").
- **Data quality constraints** — SHACL-class validation: find, flag, or prevent conflicting/nonconforming data; violation reports.
- **Visual / no-code modeling and mapping UIs** — for non-engineering participants (Designer; metaphactory visual modeling); code-first remains a valid alternative posture.
- **Rich query surface set** — SPARQL/Cypher + SQL-over-graph for BI + GraphQL + full-text/geospatial search + stored/parameterized queries; Query-as-a-Service REST templating.
- **Asset governance** — catalogs of models/vocabularies/datasets, versioning (incl. Git), lifecycle/status workflows, provenance documentation.
- **Application/explorer surfaces** — the platform family's own consumption apps (Designer/Explorer/Studio; model-driven app building; the Knowledge Graph Explorer sibling Type).
- **AI answering layer** — NL question translation to graph queries, RAG grounded in the graph, unstructured-document ingestion into the graph (era-current; present across the sample but young).
- **Enterprise security depth** — named-graph/element-level security, Kerberos/LDAP/OAuth/SSO/SCIM; fine-grained access as an enterprise-tier depth, not a Type requirement.
- **Operations machinery** — clustering/HA, backup/restore, monitoring, cloud-vs-self-managed packaging.

### L2 — Variant / Optional Structure

- **Storage posture** — engine-included platform (Stardog; Neo4j-as-database) vs storage-agnostic middleware over third-party stores (metaphactory) vs hosted SaaS substrate under another product's surface (data.world).
- **Model formality** — formal RDF/OWL ontologies + SKOS vocabularies + SHACL constraints vs light property-graph schema vs org-defined catalog models.
- **Data strategy** — materialize vs virtualize vs federate vs layered (collected-source layer separated from human curation layer, data.world).
- **Audience posture** — engineer-first (Neo4j), domain-expert/business-user participation (metaphactory, Designer), governance-organization-first (data.world).
- **Industry packaging** — pharma/life sciences, manufacturing, finance, cultural heritage verticals (metaphactory industries; Stardog federal/data-fabric positioning).
- **GenAI posture** — KG as RAG/GraphRAG grounding substrate; agent platforms; era-current emphasis, not definitional.

### L3 — Vendor-specific (kept out of the final document)

Stardog: Designer/Explorer/Studio/Knowledge Kits/Voicebox/Launchpad/ICV/BARQ naming; AI Hints; named-graph security vocabulary; specific permission strings and namespace conventions (urn:…:data:). metaphactory: Ephedra/Fedx federation engines, Semantic Clipboard, metis and Dimensions Knowledge Graph product lines, specific W3C component/templating mechanics, SAP HANA Cloud integration. Neo4j: AuraDB/Bloom/GDS product names, "index-free adjacency"/"65+ algorithms"/"1000x" marketing claims, LLM Graph Builder specifics. data.world: Eureka Explorer, dwSQL dialect, collectors catalog, AI Context Engine, ":current" default-graph convention, 25-resource bulk limits.

## Vendor-specific Findings

- The same vendor splits build/query/explore into separate applications (Stardog Designer vs Explorer vs Studio) — strong market evidence that "platform" is the build/govern layer and consumption surfaces are distinct applications.
- The same vendor sells the DBMS alone AND the KG platform story (Neo4j) — the market itself draws the database-vs-platform seam and straddles it commercially.
- A KG platform can own no storage at all (metaphactory proxies "multiple SPARQL 1.1 compliant data repositories") — platform is about the asset lifecycle, not the engine.
- A catalog product can run on a graph substrate without being a KG platform in center of gravity (data.world) — packaging overlap, different job.
- Stardog's own definition frames KG-vs-DB as "one point of view vs multiple points of view" (schema flexibility) — vendor framing, useful as evidence for leg 1's flexible-shared-model requirement, quoted only in research notes.

## Boundary Findings

- **vs Knowledge Graph Explorer (§13, processed sibling)**: the explorer consumes and traverses an existing graph; this platform builds, integrates, governs, and serves it. The sibling pass explicitly delegated build/govern to this pass. Test: if the primary job is producing/curating/governing the graph, platform; if navigating/understanding the resulting graph, explorer. Same vendors split them (Stardog Designer vs Explorer).
- **vs Graph Database / Graph Database Explorer / Database Management Console (§13)**: the database's object is the stored graph and its deployment (engine, repositories, backup); the platform's object is the knowledge asset's lifecycle — model → mapped sources → governed graph → consumers. The DB-explorer pass established the console's frame as "the running deployment"; this pass's frame is the knowledge asset. Test: remove the semantic model + construction machinery → what remains is a DBMS with admin/query tooling (the other Type); add them → platform. Neo4j is the recorded straddling pole (database product, KG posture via tooling).
- **vs RDF/SPARQL Workbench (§13)**: query-authoring surface for a dialect vs platform owning the asset lifecycle. The workbench appears *inside* platforms (Stardog Studio) as one serving surface — module-of, not peer-of.
- **vs Data Catalog (§13)**: catalog describes datasets/collections for discovery and governance; the KG platform's asset is the instance-level entity/relationship graph serving consumption. Overlaps are real and packaged both ways: a KG platform ships a catalog module (Stardog Knowledge Catalog); a catalog runs on a graph substrate (data.world). Center-of-gravity test: whose asset of record is the data estate's metadata vs the semantically integrated knowledge graph itself.
- **vs Data Fabric / Metadata Management (§13)**: the fabric pass recorded that a "knowledge-graph/semantic-layer" can *be* the fabric's metadata layer — i.e., the fabric consumes the KG frame for estate-wide data operations. The KG platform's center is the knowledge asset serving knowledge applications, not managing the data estate. Adjacent, sometimes co-located in one suite.
- **vs Master Data Management (§13)**: MDM governs golden records for master data domains; overlap at entity resolution. A KG platform's graph is a semantic integration asset for many consumers, not the system of record for master data stewardship workflows. (Moderate-confidence distinction; no MDM product was sampled this pass.)
- **vs Enterprise Knowledge Assistant / RAG Development Platform (§13)**: the KG is the grounding substrate these consume; NL-answering layers exist *inside* KG platforms as L1 capabilities, but the assistant product's center is the conversation/agent, not the graph asset.
- **Remove-what test**: remove the shared semantic model → graph database/tooling; remove construction machinery → DBMS or visualization tool; remove governed serving → a modeling/authoring studio that produces files. All three removed together → nothing recognizable.

## Taxonomy notes

- No directory change requested. The leaf is well-formed and distinct from all processed siblings. The delegation seam from knowledge-graph-explorer is honored and refined: build/govern = this Type; database operation = Graph Database Explorer; query authoring = RDF/SPARQL Workbench; traversal/consumption = Knowledge Graph Explorer.
- One naming caution for future passes: "platform" here follows the vendor usage (asset lifecycle platform), not "platform" in the infrastructure sense. No alias problem observed.

## Uncertainties

1. PoolParty (taxonomy/ontology-first semantic middleware) not directly observed — docs host unreachable ×2. The model-first middle of the market is therefore evidenced through metaphactory (A−) and Stardog's Designer instead; no PoolParty-specific claims are made anywhere.
2. metaphactory evidence is the vendor product page (feature tabs), not the deep help docs (unreachable in the sibling pass ×2, not retried). Feature claims are calibrated to page level; no precise mechanics asserted.
3. Neo4j evidence is the marketing/use-case page, not operations docs; its construction tooling (LLM Graph Builder, import tools) is recorded at positioning level. Its inclusion as the straddling pole is a documented interpretation, not a claim that Neo4j "is" a KG platform in the sampled-products sense.
4. data.world's KG architecture is observed through API semantics (IRIs, relationships, layered model, SPARQL); the user-facing docs never use "knowledge graph" — the graph-substrate reading is an inference from primary API documentation, marked as such.
5. MDM and Data Fabric distinctions rest on one direction of evidence (this pass only; both siblings already processed with their own records). The seams as stated are center-of-gravity tests, confirmed not by joint product sampling.
6. Whether "platform without any serving surface" exists as a real product shape (pure build/curate tooling sold as KG platform) — not observed; all sampled platforms serve. The L0's joint-hold of serving is calibrated to the observed market; a pure curation tool would fall below the Type.

## Final Synthesis

A Knowledge Graph Platform is the platform on which an organization turns heterogeneous data sources into a governed, shared knowledge graph and serves it to consumers. Its defining core is three jointly-held structures: (1) the knowledge graph itself as the asset of record — identified entities and typed relationships under a shared, evolvable semantic model; (2) construction machinery — the platform's own means of connecting and mapping sources into that model, resolving entities, curating and quality-checking the result, kept current as sources change; (3) governed serving — the graph operated as a shared, permission-controlled resource for many consumers through query languages, APIs, search, and the applications built on it. The storage engine may or may not be included; the modeling standard may be formal ontology or light schema; construction may be code, visual, or AI-assisted; none of that defines the Type. What defines it is the asset lifecycle: model the knowledge, build the graph from sources, govern it, serve it. The explorer traverses the result; the database stores the substrate; the workbench queries it; the platform is what makes the graph an organizational asset in the first place.
