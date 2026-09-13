# Research Notes — Vector Retrieval Platform

Research date: **2026-09-09**

---

## Research Goal

Determine what a **Vector Retrieval Platform** is as an Application Type: what the market's "vector retrieval" products actually are, who operates them, what their defining structure is, and — critically — run the **alias test** pre-hung by the sibling `semantic-search-platform` pass (§13, processed 2026-09-09): is "Vector Retrieval Platform" one family behind two directory names with Semantic Search Platform, or a distinct Type?

Related pre-hung expectations to discharge:

- `search-platform` (§13, processed 2026-09-09): center-of-gravity seam — general-purpose ranked retrieval with a lexical full-text core vs embedding-similarity retrieval as the product's core.
- `rag-development-platform` (§13, processed 2026-09-09): "vs Vector Retrieval Platform (no generation binding — same vendors ship both sides: DB surfaces fail the test, RAG surfaces pass)".
- `vector-database-console` (§13, processed 2026-09-09): this leaf is expected to document the infrastructure/service layer (the console documents the interactive work surface over it).

---

## Initial Boundary

Working hypothesis before research: a Vector Retrieval Platform is infrastructure that stores items as vector embeddings and serves retrieval — returning the items most similar to a query, ranked by similarity score — to other applications through APIs. Probable near neighbors: Semantic Search Platform (possible alias), Search Platform (lexical core), Vector Database Console (surface), RAG Development Platform (retrieval + generation), vector-capable general databases, FAISS-class libraries.

Unknowns at start:

1. Does a distinct "vector retrieval" product population exist that is NOT the vector-database family?
2. Does "retrieval" (as opposed to "search") carry extra defining structure — e.g., retrieval-quality tooling, orchestration without storage?
3. Where exactly does the generation binding stop?

---

## Research Questions

1. What do the products self-label? Does lexical evidence run both directions (vector-terms ↔ semantic/retrieval-terms) on the same pages?
2. What is the managed unit of record, and what comparison semantics does it carry?
3. What query forms does the retrieval loop accept, and what comes back?
4. What posture does the product have — infrastructure for other applications, or an end-user search surface?
5. Is generation (LLM answering) part of the core, or an optional extension / separate product line?
6. Where is the boundary vs Search Platform (lexical core), RAG platforms, consoles, vector-capable databases?
7. Historical check: would pre-transformer similarity-retrieval systems (LSA, word2vec, CBIR era) satisfy the definition?

---

## Representative Products

Selected for market coverage, fresh Layer-A evidence for THIS pass (independent of the sibling pass's fetches), different product philosophies and delivery models, plus one engine-lineage straddler for boundary evidence:

| Product | Posture | Why sampled |
|---|---|---|
| **Pinecone** | fully-managed serverless vector database | managed-SaaS pole; the family's flagship; dense lexical field (vector database / semantic search / retrieval) |
| **Qdrant** | open-source vector search engine (+ cloud) | OSS-engine pole; self-labels "Vector Search Engine" with "Semantic Search" as a use case |
| **Weaviate** | open-source AI-native vector database (+ cloud) | module/vectorizer pole; "vector search, RAG, and memory — all in one open-source platform" |
| **turbopuffer** | vector + full-text search database built on object storage | fresh architecture pole (object-storage-native serverless); not sampled by either sibling pass |
| **Vespa** | AI search platform / serving engine (lexical-search lineage) | boundary evidence: the expected engine-lineage straddler from the search-platform seam |
| LanceDB | "Multimodal Lakehouse for AI" | drift observation (Marqo pattern): center moving toward AI data infrastructure; vector/full-text/hybrid retrieval still a first-class use case |

Inherited evidence (Layer A from the `semantic-search-platform` pass, same research date, not re-fetched this pass): **Milvus / Zilliz Cloud** (distributed OSS family, typed-field collections, load-to-serve lifecycle) and **Chroma** (developer-simple / embedded pole, built-in embedding functions). Marqo was excluded by that pass (current center: ecommerce search & discovery).

---

## Sources

Fetched 2026-09-09 (this pass):

- Qdrant — homepage: https://qdrant.tech/
- Pinecone — homepage / about / products index: https://www.pinecone.io/
- Weaviate — homepage / platform: https://weaviate.io/
- turbopuffer — homepage + docs navigation: https://turbopuffer.com/
- Vespa — homepage / product taxonomy: https://vespa.ai/
- LanceDB — homepage / blog index (drift observation): https://lancedb.com/

Inherited from the semantic-search-platform pass (2026-09-09, Layer A there; URLs recorded in that pass's Sources):

- Pinecone docs — https://docs.pinecone.io/
- Weaviate docs — https://weaviate.io/developers/weaviate (concepts: storage, concepts: search)
- Qdrant docs — https://qdrant.tech/documentation/
- Zilliz Cloud (managed Milvus) docs — https://docs.zilliz.com/docs/quick-start
- Chroma docs — https://docs.trychroma.com/docs/overview/introduction

Known-unreachable (do not attempt further): milvus.io timed out ×2 for the sibling pass; Milvus OSS-architecture claims are not made anywhere.

---

## Product Observations

### Pinecone (Layer A — fetched 2026-09-09)

- Self-label: "Pinecone is the leading **vector database** for building accurate and performant AI applications at scale in production."
- Hero line: "Search through billions of items for similar matches to any object, in milliseconds. It's the next generation of search, an API call away."
- Positioning centers on **retrieval**: "Provides all the components and capabilities for high-quality, accurate end-to-end **retrieval** in a single place: combines cutting edge models (embedding, planning, reranking) with flexible and powerful query mechanisms (vector, keywords, filtering, namespaces…)".
- Its published agent-skill description names the audience and the vocabulary in one sentence: "Use when building **vector search applications, semantic search systems, RAG pipelines, recommendation engines**, or full-text search systems. Reach for Pinecone when you need to **store embeddings, query by similarity**, implement multitenancy with namespaces, or combine multiple search methods (semantic, lexical, full-text) in a single index."
- A Pinecone research publication is literally titled "**Foundations of Vector Retrieval**" (2024-06-15) — the leaf's exact term-of-art, used by the family's flagship for the same machinery.
- Product lines: Pinecone Vector Database (the center), Assistant, Dedicated Read Nodes, BYOC, Nexus (knowledge engine for agents). The generative products are **separate lines beside** the database.
- First-party comparison pages name the family's boundary set: vs pgvector, vs Elasticsearch, vs Vertex AI Vector Search.
- Deployment posture: "Fully-managed serverless experience… No capacity planning, infrastructure management, or tuning needed"; multitenancy via namespaces.

### Qdrant (Layer A — fetched 2026-09-09)

- Page title: "Qdrant - **Vector Search Engine**".
- Hero: "High-Performance **Vector Search** at Scale. Qdrant helps you build the **AI retrieval** you want. Ship high performance, full-feature vector search at any scale and with any deployment model."
- Explicit anti-keyword framing: "ARCHITECTURE FOR THE **AI - NOT KEYWORD** - ERA"; "Go beyond keywords with neural search that understands intent" (the Semantic Search solution page).
- Solutions list: RAG, AI Agents, **Semantic Search**, Recommendation Systems, Data Analysis & Anomaly Detection — retrieval-adjacent uses around one engine.
- Capability set on the homepage: metadata filters (nested/text/geo/has_vector), native hybrid search (dense + sparse; BM25, SPLADE++, miniCOIL), built-in multivector, one-stage filtering ("filters applied during HNSW traversal"), full-spectrum reranking (score boosting, late-interaction models, MMR), real-time indexing, quantization.
- Deployment shapes: Qdrant Cloud (managed), Hybrid Cloud (BYO Kubernetes), Private Cloud (air-gapped), Edge (beta), Serverless (announced). SDKs + REST/gRPC; built-in Web UI; Cloud Inference for platform-side embeddings.
- Observation: Qdrant sells the same engine with both the "vector" label (product/title) and the "semantic search / AI retrieval" label (use cases/positioning). Both directions on the same page.

### Weaviate (Layer A — fetched 2026-09-09)

- Page title: "The AI database developers love | Weaviate". Hero: "Design, build and ship complete AI experiences. **Vector search, RAG, and memory - all in one open-source platform**."
- Platform services: "**Vector Database** — Store, index, and search high-dimensional vectors at any scale. The foundation for search, RAG, and agents." (beside Query Agent, Embeddings, Engram).
- Documentation code sample names the three query forms exactly as the family model predicts: "Pure **vector search**" (`near_vector`), "**Semantic search**" (`near_text`), "**Hybrid search** (vector + keyword)" (`hybrid`) — all against one collection.
- Developer posture: SDKs (Python/Go/TypeScript/JavaScript), GraphQL/REST APIs; cloud console and tools; "Weaviate can take care of embeddings, ranking, and auto-scaling so you can ship features, not infrastructure."
- Customer stories are all retrieval-application stories: RAG, SEARCH, ENTERPRISE research workflows, SECURITY — the platform is the substrate, the applications are the customers' products.
- Observation: Weaviate's own homepage carries "vector database", "vector search", "semantic search" (code mode), and "RAG" in one screen — the one-family-many-names pattern at full strength.

### turbopuffer (Layer A — fetched 2026-09-09)

- Page title: "turbopuffer - fast search engine built on object storage". Hero: "search every byte — **vector and full-text search** built on object storage: fast, 10x cheaper, and extremely scalable."
- Self-description block (addressed to AI agents on its own page): "turbopuffer is a **vector and full-text search database**… ideal for AI applications, **semantic search**, recommendation systems, and any use case requiring high-performance **similarity search**."
- Docs guides: Vector Search (approximate nearest neighbor), Full-Text Search (BM25), Hybrid Search (combine strategies). API: Write / Query (filters and ranking) / Namespace metadata.
- The container unit is the **namespace**; storage substrate is object storage (S3) with a memory/SSD cache — a distinct architecture pole within the family (serverless-on-object-storage rather than cluster-based).
- Customers: AI-native companies (coding agents, note-taking, legal AI, etc.) — the application-builder posture is visible in the customer profile.
- Note: homepage performance/economics figures (p50/p99, "10x cheaper", 1T+ documents, QPS) are vendor marketing claims — recorded here, NOT asserted in the final document.

### Vespa (Layer A — fetched 2026-09-09, boundary evidence)

- Page title: "Vespa AI Search Platform | AI Search at Scale". Self-description: "a distributed serving engine that unifies **retrieval, ranking, machine learning inference, and real-time serving** for business-critical AI applications."
- Use-case Search: "Vespa is the world's leading open **text search engine** *and* the world's most capable **vector database**."
- Core technologies list: AI agents, **Vector database**, RAG, Tensors, Visual retrieval, "The RAG Blueprint".
- Observation: exactly the straddler predicted by the search-platform pass — an engine-lineage product (Yahoo lexical-search heritage) whose center is unified retrieval+ranking+inference serving, with vector-database capability as one of several retrieval techniques. Center of gravity sits on the search-platform side of the seam; the vector capability does not move the center. This is the packaging-pole pattern ("legitimately serve both"), not evidence of a merged Type.

### LanceDB (Layer A — fetched 2026-09-09, drift observation)

- Page title: "LanceDB | **Multimodal Lakehouse for AI**". Center of the positioning has moved to AI data infrastructure (curation, feature engineering, training) on the Lance format — the Marqo drift pattern.
- Its Search & Retrieval use case remains first-class and uses the family's exact vocabulary: "**Unified vector, full-text, and hybrid search with SQL filters for production-ready retrieval**."
- Also sells an embedded/local mode (agent-memory stories: "local-first long-term memory layer"). 
- Observation: a family member extending outward into AI-data-platform territory while keeping vector retrieval as a named use case. Recorded as drift context; not a counter-example to the Type (its retrieval use case still matches the core), and not sampled into the comparison matrix as a clean center.

### Inherited observations (from the semantic-search-platform pass, Layer A there)

- **Milvus / Zilliz Cloud**: distributed OSS vector database; typed-field collections; load-to-serve lifecycle; managed cloud + OSS poles.
- **Chroma**: developer-simple embedding database with built-in embedding functions; local/embedded, self-hosted, and cloud modes.

---

## Cross-product Comparison

| Dimension | Pinecone | Qdrant | Weaviate | turbopuffer | Vespa | Milvus/Zilliz* | Chroma* |
|---|---|---|---|---|---|---|---|
| Self-label(s) | vector database; end-to-end retrieval; "Foundations of Vector Retrieval" | Vector Search Engine; AI retrieval; Semantic Search (use case) | AI database; Vector Database; vector search / semantic search / hybrid (query modes) | vector and full-text search database; semantic search; similarity search | AI Search Platform; text search engine + vector database | vector database | embedding database |
| Container unit of record | index (+ namespaces) | collection | collection | namespace | (application schema; streaming/indexed modes) | collection | collection |
| Comparison semantics fixed at container creation | yes (dimension/metric per index) | yes (size + distance in vectors config) | yes (vectorizer/module + schema) | yes (per namespace: dimension + distance; embedding config) | (schema-defined fields) | yes | yes |
| Query forms | vector / text / item (semantic, lexical, full-text, hybrid in one index) | vector / text / item; hybrid dense+sparse | near_vector / near_text / hybrid / BM25 | vector / text (ANN + BM25 + hybrid) | text / vector / structured; hybrid | vector / text / hybrid | vector / text |
| Results | ranked, scored | ranked, scored | ranked, scored | ranked, scored | ranked (retrieval + ranking + inference) | ranked, scored | ranked, scored |
| Metadata filtering | yes (namespaces, filters) | yes (one-stage filterable HNSW) | yes (tenants, filters) | yes (filters with ranking) | yes | yes | yes |
| Hybrid / keyword machinery | sparse + lexical + full-text | dense+sparse native (BM25, SPLADE++) | BM25 + hybrid fusion | BM25 FTS + hybrid | full lexical engine + hybrid | hybrid | FTS + hybrid |
| Reranking | dedicated rerank models | score boosting / late-interaction / MMR | ranking layer | ranking per query | distributed ML ranking (center) | (limited) | (rerankers via integrations) |
| Platform-side embedding | yes (inference) | yes (Cloud Inference) | yes (Embeddings service, vectorizers) | yes (embedded attributes) | (model inference in-platform) | yes | yes (built-in functions) |
| Generation binding in the core retrieval product | no — Assistant/Nexus are separate product lines | no — RAG is a solution page around the engine | no — generative search is an optional module; RAG a use case | no | no — RAG a use case/blueprint beside the serving engine | no | no |
| End-user search UI | none (API/SDK; console for operators) | none (API/SDK; Web UI for devs) | none (API/SDK; console) | none (API only) | none (platform for built apps) | none | none (embedded/dev) |
| Posture | application-builder infrastructure | application-builder infrastructure | application-builder infrastructure | application-builder infrastructure | application-builder infrastructure | application-builder infrastructure | application-builder infrastructure (embedded pole) |

\* inherited evidence (sibling pass Layer A).

Reading of the matrix:

1. **One population.** Every product sampled under a "vector retrieval" reading is a member of the family the market calls vector databases / vector search engines. No product self-labels "vector retrieval platform" that falls outside this family.
2. **Lexical evidence runs both directions in every sampled product.** Each vendor uses "vector …" and "semantic/retrieval …" interchangeably for the same machinery — on the same pages.
3. **The core is uniform**: container of embeddings with fixed comparison semantics → programmatic query → nearest-neighbor → scored ranked results → consumed by other applications.
4. **No generation binding anywhere in the core.** RAG/generative features are use-case pages, optional modules, or separate product lines. The deliverable of the retrieval loop is the ranked result set.
5. **Hybrid/keyword machinery is universal in the 2026 sample** (era-current capability, absent from the pre-2020 generations of the same products — confirmed by the search-platform pass for the engine-lineage products). Standard, not definitional.
6. **Deployment shapes vary widely** (managed serverless, OSS self-host, BYOC, edge, embedded-local, object-storage-native) — variant axis, not Type structure.
7. **Vespa straddles** with lexical lineage; center of gravity remains unified search serving. Engine-lineage packaging pole, symmetric to the Elastic straddle recorded by the search-platform pass.

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

The Type is recognizable in a product iff all three hold:

1. **The vector index as the managed unit of record** — a persistent, named container (index / collection / namespace depending on the product) holding operator-supplied items as **vector embeddings**, each record pairing a vector with its identity and metadata, under **fixed comparison semantics** (dimensionality + distance metric set for the container, matching the embedding model that produced the vectors). Remove it → an application-facing service over nothing; a key-value/document store.
2. **The similarity-based retrieval loop** — a programmatic query interface where the query (text, vector, or an existing item) is matched against the index by **vector similarity** (nearest-neighbor search), returning results **ranked by similarity score**. Meaning, not keyword overlap, decides matches. Remove it → embedding storage with nothing to query; make lexical matching the center instead → Search Platform territory.
3. **The application-builder posture** — the platform is operated as infrastructure that other applications integrate through APIs/SDKs; the searching end user belongs to the embedding application, not to the platform. Remove it → an embedded library component (below the platform bar) or an end-user-facing search over an organization's estate (Enterprise Search territory).

Evidence: all three hold in all seven sampled/inherited products (Layer A ×5 fresh + ×2 inherited); the abstraction is Layer C (canonical inference) from cross-product comparison.

### L1 — Common Mature Structure (widespread in current products, not definitional)

- metadata on every record + query-time filtering (pre-/in-stage filtering)
- hybrid retrieval: dense + sparse/keyword (BM25-class) fused in one query
- reranking (cross-encoder-class, score boosting, MMR/late-interaction)
- platform-side embedding generation alongside BYO-vector ingestion
- named/multiple/multivector records; multimodal retrieval
- multitenancy (namespaces/tenants), SDKs across languages, management consoles
- operational machinery: upsert, bulk import, backups/snapshots, RBAC/keys, metering, freshness/consistency checks
- retrieval-quality engineering surfaces (benchmarks, recall tuning)

### L2 — Variant / Optional Structure

- deployment shape: managed serverless / OSS self-host / vendor cloud / BYOC / private-air-gapped / edge / embedded-local
- storage substrate: object-storage-native vs local-disk clusters vs in-process
- scale architecture: distributed sharded clusters vs single binary vs serverless-per-namespace
- schema posture: schemaless records vs typed-field schema-first
- lexical depth: none → BM25 keyword → full query DSL
- RAG/generative integration as separate product lines or optional modules (Assistant-class, generative-search modules)
- agentic query layers (natural-language-to-query agents), agent-skills/MCP surfaces
- drift pole: family members extending into AI-data-platform territory (Lance format lakehouses) or vertical discovery (Marqo)

### L3 — Vendor-specific (Research Notes only)

- Pinecone: serverless object-storage-tiered architecture, namespaces-as-multitenancy specifics, Assistant/Nexus/Dedicated Read Nodes product lines, first-party comparison pages
- Qdrant: Gridstore storage engine, quantization modes (asymmetric/scalar/binary), filterable-HNSW one-stage filtering, Web UI, Cloud Inference
- Weaviate: vectorizer modules, Query Agent (NL→query), Engram (personalization), GraphQL API, generative-search module
- turbopuffer: object-storage-first architecture (S3 + cache), pinned namespaces, embedded attributes, namespace sharding
- Vespa: tensor formalism, streaming-search mode for personal/private data, distributed ML ranking, application-package schema
- LanceDB: Lance columnar format, RaBitQ quantization, Geneva feature engineering, Multimodal Lakehouse packaging
- Milvus: load-to-serve lifecycle, Attu console, Zilliz Cloud packaging

---

## The Alias Test (the pass's core deliverable)

Pre-hung by the semantic-search-platform pass: "the sampled population (Pinecone/Weaviate/Qdrant/Milvus/Chroma) is exactly the population that pass would sample and the market uses 'vector database'/'vector search'/'semantic search' interchangeably for the same products — one family behind two directory names, ratify at that pass."

Test run from this side with fresh evidence:

1. **Population test** — a fresh sample drawn from the "vector retrieval" reading (Pinecone, Qdrant, Weaviate, turbopuffer, + Vespa/LanceDB boundary observations) lands entirely inside the vector-database family; it *adds* a family member (turbopuffer) that neither sibling pass sampled, rather than finding any product outside the family. **Pass.**
2. **Lexical test** — every sampled product self-labels with BOTH term families on the same pages: Qdrant ("Vector Search Engine" title + "Semantic Search" use case + "AI retrieval" hero); Pinecone ("vector database" + "semantic search systems" + "end-to-end retrieval" + a research paper titled "Foundations of Vector Retrieval"); Weaviate ("Vector Database" product + "Semantic search" code mode); turbopuffer ("vector and full-text search database" + "semantic search" + "similarity search"). **Pass — both directions, all products.**
3. **Structural test** — does "retrieval" carry defining structure beyond the semantic-search core (embedding index + similarity loop + builder posture)? No. "Retrieval" is the IR-discipline name for the same loop; the retrieval-quality machinery it evokes (hybrid, reranking, filtering) is already documented in both documents as standard-not-definitional. No product or structure was found that satisfies "vector retrieval" but not the semantic-search core, or vice versa. **Pass.**
4. **Counter-population test** — no reachable product population organizes around "vector retrieval" with a different unit of record, different loop, or different posture. Orchestration-only retrieval layers (retrieval without owned storage) were not found as a product population; where retrieval is orchestrated with generation, that is RAG Development Platform territory.

**Verdict: ALIAS RATIFIED — Vector Retrieval Platform ≡ Semantic Search Platform. One market family behind two directory names.** Both leaves documented as the directory defines them (each document written from its own lens, cross-referencing the other); the merge/canonical-name decision is escalated to the taxonomy maintainers, consistent with the internal-knowledge-search / research-grant-management precedents.

---

## Boundary Findings

Removal tests recorded both directions.

1. **vs Search Platform** — center of gravity: this family's center is embedding-similarity retrieval; the Search Platform's center is general-purpose ranked retrieval with a lexical full-text core. Hybrid/keyword machinery exists on both sides (era-current) and cannot separate them. Remove similarity-as-center → Search Platform; make lexical matching the center of one of these products → Search Platform. Vespa = engine-lineage straddler (packaging pole, no taxonomy change), symmetric to Elastic in the search-platform pass.
2. **vs RAG Development Platform** — no generation binding. The retrieval loop's deliverable is the ranked, scored result set; grounding, prompt composition, and answering belong to the embedding application (or to separate product lines: Pinecone Assistant/Nexus, Weaviate generative search, Qdrant RAG solution page, Vespa RAG blueprint). Remove the generation binding from a RAG platform → this Type; add a generation binding to this Type's core → RAG territory.
3. **vs Vector Database Console** — infrastructure vs interactive work surface over that infrastructure (same market population, different unit of analysis; the console pass already recorded the surface-vs-system-of-record layering with vendor evidence).
4. **vs Enterprise Search Platform / Internal Knowledge Search** — developer-built application substrate (domain-agnostic, corpus supplied by the operator) vs the organization's own content estate queried by its own members under org access rules.
5. **vs vector-capable general databases (pgvector/Redis/MongoDB-Atlas class)** — center of gravity: transactional/structured-query centers with vector capability vs embedding-similarity retrieval as the center. Expected straddlers (packaging pole); not sampled this pass — noted as expectation, consistent with the console and search passes' straddler pattern.
6. **vs Recommendation / Personalization Engine** — domain-agnostic similarity infrastructure (no campaign/business-objective machinery; "find similar" is one query form) vs merchandising/personalization systems with business goals.
7. **vs AI Model Hosting Platform** — consumes embedding models to build a similarity-searchable index vs hosting/serving models as the product. Platform-side embedding generation is a capability here, not the center.
8. **vs FAISS-class similarity-search libraries** — component below the platform bar: no operator posture, no managed service, no application-builder surface. Conceptual substrate/ancestor, not the Type.
9. **vs Knowledge Graph Platform** — different semantic substrate: entities/relations/traversals vs embedding vectors/similarity.

---

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the definition?

- The three-part core (similarity-searchable vector container + nearest-neighbor loop + programmatic serving posture) predates the LLM era: LSA/word2vec-era semantic vectors, content-based image retrieval, and dedicated ANN-serving systems satisfy all three legs conceptually (medium confidence — conceptual lineage, not freshly fetched this pass; inherited from the sibling pass's check).
- The 2026 sample's universal hybrid/keyword machinery is era-current (absent from pre-2020 generations of the same products — confirmed by the search-platform pass) and is therefore excluded from the core.
- The check passes: the definition is not overfit to the current managed-cloud, hybrid-everything generation. A pure-vector, self-hosted, schemaless product remains fully in-type.

---

## Uncertainties

1. **Orchestration-only retrieval layers** (retrieval APIs with no owned storage, no generation) were not found as a distinct product population in the reachable market. If such products emerge, they would sit between this Type and RAG Development Platform; recorded as an open question, no taxonomy action.
2. **Drift direction of family members** (LanceDB → Multimodal Lakehouse; Marqo → ecommerce discovery, excluded by the sibling pass): the family perimeter is dynamic; center-of-gravity language in both documents absorbs drift without taxonomy change.
3. **Historical check confidence is medium** (conceptual lineage for pre-transformer systems; no fresh fetch of e.g. FAISS/Annoy-era documentation this pass).
4. **turbopuffer performance/economics figures** are vendor marketing claims; no performance figures are asserted in the final document.
5. Milvus OSS documentation remained unreachable (inherited limitation); Milvus evidence is via Zilliz Cloud official docs (same vendor family) — no OSS-architecture claims made.

---

## Final Synthesis

A Vector Retrieval Platform is the vector-database family seen from its retrieval center: developer-operated infrastructure whose unit of record is a persistent container of items held as vector embeddings under fixed comparison semantics, whose defining loop is programmatic similarity retrieval — query in (text, vector, or existing item), nearest-neighbor search, scored ranked results out — and whose posture is application-builder infrastructure consumed through APIs/SDKs by other applications. Meaning, not keyword overlap, decides matches; the deliverable is the ranked result set, never a generated answer; the searching end user belongs to the embedding application. The market realizes this one Type under several names — vector database, vector search engine, semantic search platform, vector retrieval platform — and the alias with Semantic Search Platform is ratified from this side. Standard capabilities (metadata filtering, hybrid dense+sparse retrieval, reranking, platform-side embedding, multitenancy, operational machinery) make the Type practical; deployment shapes and storage substrates are variants; vendor product lines and architectures are research-notes detail.
