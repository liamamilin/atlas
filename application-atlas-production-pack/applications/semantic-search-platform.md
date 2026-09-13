# Semantic Search Platform

## Overview

A **Semantic Search Platform** is developer-operated infrastructure whose retrieval center is **search by meaning**: content is stored as vector embeddings, and queries return the items that are most *semantically similar* to the query — ranked by similarity score — rather than the items that merely contain the query's keywords.

The defining structure is small:

```text
Embedding index (persistent, named container of vector embeddings)
└── Similarity-based retrieval loop
    └── query → embed → nearest-neighbor search → similarity-scored results
        └── Application-builder posture (other apps integrate via APIs/SDKs)
```

Everything commonly associated with the current generation — platform-side embedding generation, metadata filtering, hybrid keyword+vector search, reranking, multimodal retrieval, managed serverless delivery — is widespread in today's products but is not part of the defining core. A platform that stores only operator-supplied vectors and answers vector queries with scored nearest-neighbor results is fully within the Type; a platform whose center is lexical full-text retrieval with vector search added is a Search Platform, not this Type.

When the product's center shifts to orchestrating retrieval *plus generation* (answering questions, not returning similar items), it is drifting toward a different Application Type (RAG Development Platform). When the query surface is pointed at an organization's own content estate for its own members, it is drifting toward Enterprise Search territory.

## Users & Context

The primary users are the people who build and operate the retrieval layer of an AI application:

- **AI/ML engineers** — choose embedding models, design what gets embedded (documents, chunks, products, images), and own retrieval quality.
- **Backend / application developers** — integrate the platform's API or SDK into the application that serves the end user.
- **Platform / infrastructure teams** — operate the deployment: capacity, tenancy, backups, access control, cost.

The searching end user is *not* a user of this platform. They search inside an embedding application — a RAG assistant grounding its answers, a "find similar" recommendation surface, a semantic product search, an internal knowledge lookup — and the platform is invisible to them. This is the same substrate posture that defines the sibling Search Platform Type; what differs is what sits at the center of the retrieval machinery.

Typical work: provision an index or collection, ingest and embed content, tune the retrieval loop (filters, hybrid weighting, reranking), measure result quality, and keep the index fresh as source content changes.

## Core Model

### The Defining Core

```text
Embedding index
└── Vector records (id + embedding + metadata)
    └── Similarity-based retrieval loop
        └── Scored nearest-neighbor results
```

Three properties. If any one is removed, the product is no longer recognizable as a Semantic Search Platform:

- **The embedding index as the unit of record** — a persistent, named container (called an *index* or *collection* depending on the product) holding operator-supplied items as **vector embeddings**. Each item is a record: an identifier, one or more vectors, and usually attached metadata. The container carries the comparison semantics — a distance metric (cosine similarity, dot product, Euclidean distance are the common set) and the vector dimensionality — configured when the container is created, because they must match the embedding model that produced the vectors. Without the embedding transformation and the similarity structure, the product is just a key-value or document store.
- **The similarity-based retrieval loop** — a programmatic query interface where the query is embedded and matched against the index by **vector similarity (nearest-neighbor search)**. The query can take three forms, and mature products support all three: query *text* (the platform embeds it, where embedding is integrated), a query *vector* (the operator embeds it), or an *existing item* (the item's own vector becomes the query — the "find similar" pattern). Results come back ranked by similarity score, each with a score representing its distance to the query. Meaning — not keyword overlap — decides what matches: a search for "very dark" can surface items that say "ebony" or "noir" and never contain the query words. Without this loop, the product is embedding storage with nothing to query; without similarity as the *center* (lexical match as the center instead), it is a Search Platform.
- **The application-builder posture** — the platform is operated as infrastructure that other applications integrate through APIs and SDKs. The operator is a building team; the searching end user belongs to the embedding application. Without this posture, the same machinery is either a library inside one application (a component, not a platform) or an end-user-facing search over an organization's estate (Enterprise Search territory).

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They are not what makes the product a semantic search platform, but they make it practical:

- **Metadata on every record, with query-time filtering** — each vector record carries structured metadata (category, timestamps, price, tenant identifier), and queries can narrow the candidate set with filter expressions before or during the similarity search.
- **Hybrid search** — combining vector similarity with keyword (BM25-class) scoring, either by fusing two result lists (weighted fusion, reciprocal rank fusion) or by storing dense and sparse vectors side by side. Universal in the current generation; a pure-vector core is equally within the Type.
- **Reranking** — reordering an initial result set with a more computationally expensive model (cross-encoder-class) to improve precision on the top results.
- **Embedding generation** — most products offer platform-side embedding (integrated models, vectorizer modules, hosted inference services), while equally accepting operator-supplied vectors. Both paths are first-class; which one a team uses is a choice, not a Type boundary.
- **Multiple and named vectors per record** — several vector spaces on one record (e.g., a text embedding and an image embedding), searchable individually or with weighted multi-target queries.
- **Multimodal retrieval** — indexing and searching images, audio, and other media alongside text.
- **"Find similar" retrieval** — querying with an existing item's ID to get its nearest neighbors; the substrate of recommendation-style surfaces.
- **Multitenancy** — partitioning one deployment into isolated per-customer or per-workspace units (namespaces, tenants, databases).
- **Operational machinery** — SDKs across languages, management consoles, backups/snapshots, access control (API keys, roles), usage metering on managed services, bulk import from object storage, upsert semantics.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. The Variants section below enumerates how specific implementations realize each concept.

```text
Concept:          Embedding index
Implementations:  serverless index (Pinecone-style), collection (Qdrant, Chroma),
                  class-based collection (Weaviate), typed-field collection under a database (Milvus)

Concept:          Record
Implementations:  vector + metadata record, object with properties + vectors,
                  point with payload, entity with typed fields

Concept:          Query embedding
Implementations:  platform-integrated embedding of query text, operator-supplied query vector,
                  existing item's vector as the query
```

A reader who only encounters one implementation should still be able to recognize the others from the Core Model.

## How It Works

### Provision the index

```text
Create an index / collection
→ choose the comparison semantics (distance metric, vector dimensionality)
→ optionally define the record schema and which metadata is filterable
→ the container is ready to receive records
```

The metric and dimensionality are chosen to match the embedding model the team will use; they are fixed per container in the products observed, which is why model changes are a migration (re-embedding the corpus into a new index), not a field update.

### Ingest: embed and upsert

```text
Prepare items (documents, chunks, products, images)
→ embed them — with the platform's embedding machinery, or with the operator's own model
→ upsert records (id + vector + metadata) into the index
→ the platform inserts them into its similarity-searchable structure
```

Ingestion is incremental (upsert by ID — same ID overwrites) and commonly bulk (import jobs from object storage). Newly ingested items become searchable shortly after ingestion, not necessarily instantly; managed products expose freshness checks for exactly this reason.

### Query: the retrieval loop

```text
Application sends a query — text, a vector, or an item ID
→ (text is embedded by the platform where embedding is integrated)
→ nearest-neighbor search over the index, optionally narrowed by metadata filters
→ results return ranked by similarity score, with the record's fields/metadata
→ the application presents or processes them
```

This loop is the product's center. Everything else in the workflow either feeds it (ingestion) or refines its output (the next step).

### Refine: filter, hybrid, rerank, generate

```text
Narrow with metadata filters (often applied before the similarity search)
→ optionally combine vector and keyword scores (hybrid fusion)
→ optionally rerank the top results with a heavier model
→ optionally hand the results to a generative model (RAG) — in-product where offered,
  or in the embedding application
```

These are refinement layers over the same loop, not separate products. The generative step in particular is optional: the platform's deliverable is the ranked, scored result set.

### Operate

```text
Scale the deployment (managed serverless, or self-hosted cluster operations)
→ isolate tenants, manage access keys and roles
→ back up / snapshot indexes
→ monitor usage, cost, and query performance
→ re-embed and migrate when the embedding model changes
```

### Core vs Common vs Optional

Capabilities fall into three tiers:

**Defining core** — without these, not a Semantic Search Platform:

- embedding index as persistent named unit of record
- vector records (id + embedding, metadata typical)
- similarity-based retrieval loop (embed query → nearest-neighbor → scored results)
- programmatic integration surface (API/SDK)
- application-builder posture

**Common mature structure** — present in most modern products:

- metadata + query-time filtering
- hybrid (vector + keyword) search
- reranking
- platform-side embedding generation (alongside BYO vectors)
- multiple/named vectors, multimodal retrieval, find-similar queries
- multitenancy, consoles, backups, RBAC, metering, bulk import

**Variant / optional** — depends on segment, deployment, and era:

- deployment shape: managed SaaS / self-hosted OSS / BYOC / embedded-local
- embedding source: platform-integrated vs operator-supplied
- schema posture: typed-field schema-first vs schemaless records
- scale architecture: distributed cluster vs single binary
- lexical depth: none → BM25 keyword → full query syntax
- commercial model: usage-metered vs provisioned vs self-managed OSS
- RAG/generative integration and agentic query layers

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### API / SDK (the primary surface)

The product's main interface is programmatic: a REST/gRPC (occasionally GraphQL) API plus client libraries in the major languages. Operations cluster into data-plane (upsert, query, fetch, update, delete records) and control-plane (create/configure indexes, manage namespaces/tenants, keys, backups). There is no "search page" — the embedding application *is* the search page.

### Management console

Managed services ship a web console: list and configure indexes/collections, inspect record counts and index statistics, manage API keys and members, view usage and cost, configure backups. Self-hosted poles may be console-less, operated entirely through configuration and API.

### Query playground / web UI (optional)

Some products ship a lightweight web UI for running test queries and inspecting points/collections during development. It is a developer tool, not an end-user search surface.

### No end-user search UI

Unlike consumer search products, this Type does not provide the interface the searching human touches. UI kits and widgets, where offered, are building blocks for the embedding application's own interface — the same optional layer Search Platforms offer.

## Important Rules / Behaviors

### Query and content must share one embedding space

The query embedding and the record embeddings must come from the same model (or compatible spaces) for similarity to be meaningful. This is why the metric and dimensionality are fixed per index/collection, why mixing vectors from different models in one container is a modeling error, and why changing the embedding model is a re-embed-and-migrate operation rather than a setting change.

### Results are scored, not boolean

A similarity search always returns *something* (the nearest neighbors), ranked by score — there is no natural "no match" threshold unless the application imposes one on the scores. Applications therefore work with score cutoffs and top-k limits, a fundamentally different contract from lexical match/no-match retrieval.

### Approximate, not exact

Nearest-neighbor search over large indexes is approximate (ANN): the machinery trades a small amount of recall for large gains in speed and memory. Products expose tuning over this tradeoff and treat recall measurement as a normal engineering activity. Exactness guarantees are not part of the contract.

### Filters interact with the search

Metadata filtering can be applied before the similarity search (pre-filtering) or after it, with materially different behavior for result counts and recall. Mature products document which strategy they use; application developers must reason about it when combining filters with top-k limits.

### Upsert semantics and freshness

Writing a record with an existing ID overwrites it. Ingested items become searchable after a short interval rather than instantly; managed products expose freshness/consistency checks so pipelines can verify visibility before cutting over traffic.

### The platform holds no opinion about the corpus

Unlike vertical search products, the platform is domain-agnostic: documents, product catalogs, images, code, user profiles — anything embeddable is in scope. Domain semantics (what a "product" or a "document" means) live in the embedding application, not in the platform.

## Variants

The Type is implemented in several recognizable shapes:

- **Managed serverless SaaS** — fully operated, usage-metered, opaque scaling; the team only defines indexes and queries (e.g., Pinecone).
- **Open-source engine, self-hosted or vendor-cloud** — the same engine run by the team or consumed as a managed cloud; module ecosystems for embedding models (e.g., Weaviate, Qdrant, Milvus, Chroma).
- **Distributed-scale platform** — sharded/replicated clusters for billion-scale corpora, often schema-first with typed fields and explicit load/serving lifecycle (e.g., Milvus/Zilliz Cloud).
- **Developer-simple / local-first** — minimal setup, embedded or single-binary operation for prototyping and small-to-mid workloads, with a managed cloud above (e.g., Chroma).
- **Embedded/edge mode** — the engine running in-process or on-device for offline retrieval.
- **BYOC** — the managed platform deployed inside the customer's own cloud account for data sovereignty.

A variant remains a **Variant**, not a separate Type, unless it changes the core objects, the retrieval loop, or the posture — for example, a product whose center becomes ecommerce merchandising (business-objective ranking, promotional controls) has moved toward search-and-discovery territory, and a product whose center becomes answering questions with generation has moved toward RAG-platform territory.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Search Platform | the closest sibling; same application-builder posture, different retrieval center — lexical full-text core with vector/hybrid as capabilities vs embedding-similarity as the core. Engine-lineage products legitimately serve both (packaging straddle) |
| Vector Retrieval Platform | one product family behind two names — the market uses "vector database / vector search" and "semantic search" interchangeably for the same products; this document defines the family by its retrieval center (see note below) |
| Vector Database Console | an interactive work surface *over* a vector database (inspection, query, administration) vs the operated retrieval substrate itself |
| RAG Development Platform | retrieval substrate vs retrieval+generation orchestration; RAG features inside this Type are an optional layer, not the center |
| Enterprise Search Platform / Internal Knowledge Search | operates the organization's content estate under org access rules with a member-facing query surface vs a substrate for developer-built applications |
| Database (relational/document) with vector extensions | vector search as a capability of a transactional/structured-query center vs embedding-similarity retrieval as the center |
| Recommendation / Personalization Engine | domain-agnostic similarity infrastructure vs a merchandising/personalization system with campaign and business-objective machinery; "find similar" is one query form here |
| Knowledge Graph Platform | different semantic substrate: entities/relations/traversals vs embedding vectors/similarity |
| AI Model Hosting Platform | hosts/serves models as the center vs consuming embedding models to build a similarity-searchable index |

**Note on the sibling name:** the directory also carries *Vector Retrieval Platform* as a separate leaf. The researched market population — the products the market calls vector databases or vector search engines — is one family, and this document defines it by its retrieval center; how the two directory names should be consolidated is a decision for the directory's maintainers, recorded in the Research Notes.

## Representative Products

- **Pinecone** — managed serverless vector database; integrated embedding and BYO vectors; namespaces for multitenancy
- **Weaviate** — open-source AI-native vector database with vectorizer modules; self-host, cloud, and embedded deployments
- **Qdrant** — open-source vector similarity search engine; collections of points with payloads; self-host, cloud, and edge modes
- **Milvus / Zilliz Cloud** — distributed open-source vector database with a managed cloud; typed-field collections, load-to-serve lifecycle
- **Chroma** — open-source developer-simple embedding database with built-in embedding functions; local, self-hosted, or cloud

The Core Model was checked against the boundary poles: general search platforms with vector capability (lexical-core straddlers), vector-capable databases (capability-of-another-Type), and similarity-search libraries (components below the platform bar).

## Sources

Research date: **2026-09-09**

Primary vendor documentation (Tier 1):

- Pinecone — https://docs.pinecone.io/ (docs root, guides index, semantic search guide)
- Weaviate — https://weaviate.io/developers/weaviate (overview; concepts: storage; concepts: search)
- Qdrant — https://qdrant.tech/documentation/ (documentation root; what-is-qdrant)
- Zilliz Cloud (managed Milvus) — https://docs.zilliz.com/docs/quick-start (quickstart to serving cluster)
- Chroma — https://docs.trychroma.com/docs/overview/introduction (introduction)

> Sourcing limitations: milvus.io documentation timed out repeatedly and was abandoned; Milvus evidence comes from the Zilliz Cloud official documentation (same vendor family) and no Milvus OSS-architecture claims are made. Marqo was examined and excluded as a sample — its current product center is ecommerce search and discovery, with its vector-search engine carried as a separate classic product line. No pricing, latency, or numeric-limit figures are asserted in this document; where products publish such figures they are marketing claims recorded only in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis (including the seam with Search Platform and the one-family-two-names question with Vector Retrieval Platform) are recorded in the paired Research Notes.
