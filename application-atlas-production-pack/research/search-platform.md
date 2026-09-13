# Research Notes — Search Platform

Research date: 2026-09-09
Leaf: Search Platform (DIRECTORY.md §13 Data, Analytics & AI Systems)
Slug: search-platform

---

## Research Goal

Understand what a "Search Platform" is as an Application Type in the §13 (Data, Analytics & AI Systems) sense: the search-engine substrate that development teams operate and that other applications build search upon. Produce a vendor-neutral Application Document that explains the Type's core structure, workflow, interfaces, rules, variants, and boundaries — without over-fitting to any one product, era, or deployment shape.

## Initial Boundary

Working hypothesis before research:

1. **Core use**: provide a search engine — indexing + ranked retrieval — as an operable platform that developers embed into their own applications (site search, app search, ecommerce search, RAG grounding, log search).
2. **Primary users**: developers / engineering / platform teams who configure, populate, tune, and operate the engine; the searching end user belongs to the embedding application, not to the platform.
3. **Nearest neighbors**: Enterprise Search Platform (§10, processed — pre-hung boundary note), Web Search Engine (§02.02), Vector Retrieval Platform / Semantic Search Platform (§13 siblings, unprocessed), Code Search Platform (§12, processed), RAG Development Platform (§13 sibling, unprocessed), databases with full-text capabilities, Log Management (§14).
4. **Likely boundary with Enterprise Search Platform** (from the ESP pass, recorded in STATUS.md): operating target — ESP operates the organization's content estate under org access rules with a member-facing query surface; Search Platform operates as a substrate for arbitrary developer-built applications. Engine-lineage products (Elastic) legitimately serve both; the ESP pass held this as a packaging-pole variant, no taxonomy change.
5. **Unknowns**: whether the "developer/application-builder posture" is definitional or merely dominant; whether vector/semantic search (now ubiquitous in the sample) has become definitional; whether hosted site-search SaaS is inside or adjacent to the Type.

## Research Questions

1. What are the core objects? (documents/records, indices, schemas/mappings/settings, queries, results)
2. What does the platform provide vs. what does the embedding application build?
3. How does ingestion work (push/pull), and what happens between ingest and searchability?
4. How does the query loop work, and what exactly is "relevance" in these products?
5. How is relevance tuned (analysis, ranking rules, custom ranking, synonyms, rules)?
6. What deployment shapes exist (self-hosted engine, managed cloud, SaaS API, hyperscaler service)?
7. What is the developer integration surface (APIs, clients, UI libraries)?
8. Where are the boundaries vs. the neighboring Types listed above?
9. Would older / non-cloud / library-era products still fit the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer levels and deployment shapes:

| Product | Philosophy / posture | Customer level | Evidence quality |
|---|---|---|---|
| **Elasticsearch** (Elastic) | engine-lineage distributed platform; self-hosted + cloud + serverless; extends into observability/security | enterprise + startup | Tier-1 docs (search use case, data store, site-or-app) + Tier-2 product page |
| **Algolia** | API-first SaaS search platform; developer-experience-first; ecommerce/media focus | startup → enterprise | Tier-1 docs (prepare data, relevance overview, manage indices, docs index) |
| **Apache Solr** | classic open-source engine on Lucene; schema-first; self-managed | OSS community → enterprise | Tier-1 Reference Guide index (full TOC + intro text); deep pages 404 — see Sources |
| **Meilisearch** | lightweight open-source engine; single binary, REST API, no schema; Cloud or self-host | indie/SMB → mid-market | Tier-1 docs (overview, indexes/core concepts) |
| **Azure AI Search** | hyperscaler fully-managed service; classic search + agentic retrieval; AI enrichment | enterprise | Tier-1 Microsoft Learn overview |

This sample spans: engine-lineage commercial (Elastic), SaaS API-first (Algolia), classic OSS (Solr), lightweight OSS (Meilisearch), hyperscaler managed (Azure). Deliberately excluded: single-vendor suites' embedded search modules; web search engines; vector-database-only products (different §13 sibling).

## Sources

Fetched 2026-09-09:

- Elasticsearch product page — https://www.elastic.co/elasticsearch/ (Tier 2)
- Elasticsearch docs: Search use case — https://www.elastic.co/docs/solutions/search (Tier 1)
- Elasticsearch docs: The Elasticsearch data store — https://www.elastic.co/docs/manage-data/data-store (Tier 1)
- Elasticsearch docs: Add search to your site or app — https://www.elastic.co/docs/solutions/search/site-or-app (Tier 1)
- Algolia docs index — https://www.algolia.com/doc/ (Tier 1)
- Algolia docs: Prepare your records for indexing — https://www.algolia.com/doc/guides/sending-and-managing-data/prepare-your-data/ (Tier 1)
- Algolia docs: Relevance overview — https://www.algolia.com/doc/guides/managing-results/relevance-overview/ (Tier 1)
- Algolia docs: Manage indices — https://www.algolia.com/doc/guides/sending-and-managing-data/manage-indices-and-apps/manage-indices/ (Tier 1)
- Apache Solr Reference Guide (10.0) — https://solr.apache.org/guide/ (Tier 1 index page)
- Meilisearch docs overview — https://www.meilisearch.com/docs (Tier 1)
- Meilisearch docs: Indexes — https://www.meilisearch.com/docs/learn/core_concepts/indexes (Tier 1)
- Azure AI Search: Introduction — https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search (Tier 1)

**Source-access limitations**:
- Solr deep guide pages (introduction, documents-fields-schema-design) returned 404 twice each — abandoned per network rules. Solr evidence is the Reference Guide index page (official, committer-written intro text + complete TOC), which is Tier-1 structural evidence but not page-level operational detail. No numeric Solr claims made anywhere.
- No pricing, no latency numbers, no version-specific defaults asserted in the final document. Meilisearch's "<50ms" and Algolia's speed claims are marketing figures — recorded here, excluded from the final document.

---

## Product A — Elasticsearch (Elastic)

### Key observations (Evidence Layer A unless noted)

- Self-description: "open source, distributed search and analytics engine built for speed, scale, and AI applications… As a retrieval platform, it stores structured, unstructured, and vector data in real time." (product page, Tier 2)
- Data model: stores data as **JSON documents organized into indices**; each index holds a dataset with its own **schema defined by a mapping** (fields + types); many independent datasets side by side, searched individually or together; **aliases** as logical references; **data streams** for timestamped append-only data. (data store docs, Tier 1)
- **Text analysis**: "how unstructured text is converted into a structured format optimized for full-text search, including tokenization, normalization, and custom analyzers." (Tier 1)
- **Near real-time search**: newly indexed data becomes searchable "within seconds of indexing" — not instantly. (Tier 1)
- Search approaches: full-text, vector, semantic, hybrid; ranking and reranking to "control result ordering and relevance"; query languages (Query DSL, ES|QL piped language). (Tier 1)
- Distributed architecture: nodes, shards, primaries, replicas; cross-cluster search for federation. (Tier 1 references)
- Ingestion: Index API for documents; "pipelines, agents, and Logstash" for production ingestion; built-in connectors; 350+ integrations claim (marketing figure — not asserted). (Tier 1/Tier 2)
- Application-builder posture: "Add search to your site or app" — language clients (Java, Python, Go, Ruby, Rust, .NET, PHP…) + **Search UI library** to build the search interface of the embedding application. Use cases listed: website and documentation search, ecommerce product catalogs, recommendation, RAG, geospatial, QA, dashboards, "custom observability or cybersecurity search tools". (Tier 1)
- Deployment: Elastic Cloud Serverless / Elastic Cloud Hosted (AWS/GCP/Azure) / self-managed download. (Tier 2)
- Vendor drift (L3): the same engine powers solution families — Observability (log analytics, APM) and Security (SIEM, XDR). Kibana as the visualization/management UI. Jina AI models, Agent Builder. (Tier 2)

## Product B — Algolia

### Key observations

- Self-description: "Build search, discovery, and AI-powered retrieval experiences with Algolia." Docs organized around: send and manage data; build search and AI experiences; tune and personalize ranking; measure and optimize. (docs index, Tier 1)
- Data model: **record** = collection of named attributes (key-value); each record has a unique **objectID** (set by the developer or generated); records live in **indices**; attributes need no fixed schema ("don't have to follow a specific schema — they can differ for each record"). (prepare-your-data, Tier 1)
- Record design doctrine: include only what serves search — attributes for **searching** (searchableAttributes), for **display**, for **filtering** (attributesForFaceting), and numeric/boolean **custom ranking** attributes ("custom ranking makes results more relevant by including your business metrics"). Explicitly: "Don't worry about relational database principles." (Tier 1)
- Relevance model: "Relevance is finding results that match a search query and ranking them so the best-matched results appear at the top." Finding = text-based comparisons (typos, stop words) + non-textual factors (filters, geolocation); ranking = tie-breaking algorithm. Tuning levers: searchable attributes, custom ranking, **rules** (override relevance, e.g. promotions), **synonyms**, facets, natural-language settings, personalization. (relevance overview, Tier 1)
- Measurement: search analytics, click and conversion events, A/B testing. (docs index, Tier 1)
- SaaS posture: index names "appear in network requests, so consider them publicly available"; multiple **applications** for testing/staging/production environments; dashboard + API as peer surfaces. (manage indices, Tier 1)
- AI era: NeuralSearch (hybrid), Dynamic Re-Ranking, Agent Studio, MCP server, Recommend. (docs index, Tier 1)
- UI building: "Build search UIs" guides + UI libraries. (docs index, Tier 1)

## Product C — Apache Solr

### Key observations (guide index page, Tier 1 structural evidence)

- Self-description: "Solr is the open source solution for search and analytics. A fast open source search platform built on Apache Lucene, Solr provides scalable indexing and search, as well as faceting, hit highlighting and advanced analysis/tokenization capabilities."
- Concept set (from guide structure): **Documents, Fields, and Schema Design**; **Solr Indexing**; **Searching**; **Relevance** — the same four pillars as the commercial products.
- Schema-first posture: Schema Elements, Schema API, Schemaless Mode, Field Types, Copy Fields, Dynamic Fields, DocValues.
- Analysis pipeline: Analyzers, Tokenizers, Filters, CharFilters, Language Analysis, Phonetic Matching, Analysis Screen (a debugging UI for the analysis chain).
- Query machinery: Standard/DisMax/eDisMax query parsers, JSON Request API + JSON Query DSL, function queries, SQL query language, spatial search, **dense vector search**.
- Result control: Faceting, JSON Facet API, grouping, clustering, highlighting, pagination, query elevation (curated top results), response writers.
- Relevance tooling: Spell Checking, Suggester, MoreLikeThis, Query Re-Ranking, Learning To Rank.
- Operations: SolrCloud (shards, replicas, ZooKeeper ensemble), user-managed replication, monitoring (metrics, thread dump, circuit breakers, rate limiters), security (authentication/authorization plugins, audit logging, SSL), Admin UI, client APIs (SolrJ, JavaScript, Python, Ruby).

## Product D — Meilisearch

### Key observations

- Self-description: "Meilisearch indexes your content and makes it accessible to both humans and AI… stores your documents and embeddings, then exposes them through fast full-text search, semantic search, and conversational interfaces, all from a single API." (docs overview, Tier 1)
- Posture: "a single binary with a REST API. There is no cluster to configure, no schema to define, and no separate vector store to manage." Cloud or self-host. (Tier 1)
- Data model: **index** = group of documents with associated settings, defined by a `uid`, containing one **primary key** (required attribute, unique per document; same value ⇒ overwrite), customizable settings, arbitrary number of documents. Implicit index creation on first write; explicit creation "considered safer for production". (indexes doc, Tier 1)
- Settings = the per-index search behavior: displayed/searchable attributes, distinct attribute, filterable attributes (faceting), pagination limits, **ranking rules** (ordered chain: words, typo, proximity, attributeRank, sort, wordPosition, exactness — order matters), sortable attributes, stop words, synonyms, typo tolerance (configurable per word/attribute). (Tier 1)
- Isolation rule: "One index's settings do not impact other indexes" — e.g. different synonyms per index on the same server. (Tier 1)
- Operations: **index swapping** — atomic exchange of two indexes' documents/settings/task history without downtime for search clients. (Tier 1)
- AI era: auto-embeddings (embedder configuration generates vectors at index time), hybrid search merging keyword + semantic, RAG/conversational search grounded in indexed data. (Tier 1)
- Marketing figures ("<50ms", "under 50 milliseconds") — recorded here only, excluded from final document.

## Product E — Azure AI Search

### Key observations

- Self-description: "a fully managed, cloud-hosted service that connects your data to AI… unifies access to enterprise and web content so agents and LLMs can use context… to produce reliable, grounded answers." (Microsoft Learn, Tier 1)
- **Classic search** architecture: "an index-first retrieval model for predictable, low-latency queries. Each query targets a single, predefined search index and returns ranked documents in one request–response cycle." The service "sits between the data stores that contain your unprocessed content and your client app. The app is responsible for sending query requests… and handling the response." (Tier 1)
- Two workloads: **Indexing** (loads content into an index and makes it searchable; inbound text tokenized and stored in **inverted indexes**, vectors in vector indexes; only JSON documents; **push** method = upload JSON, **pull** method = indexer workflow from supported data sources) and **Querying** (client app sends query requests: full-text, vector, hybrid, multimodal, fuzzy, autocomplete, geo). (Tier 1)
- **AI enrichment**: skills that chunk, vectorize, and transform raw content at indexing time. (Tier 1)
- Relevance tuning: "relevance tuning to improve intent matching and result quality"; faceted navigation, filters (incl. geo), synonym mapping, autocomplete. (Tier 1)
- **Agentic retrieval** (newer layer): knowledge bases over knowledge sources; LLM-assisted query planning, decomposition, parallel retrieval, semantic reranking, merged results "optimized for agent consumption". Builds on the classic architecture. (Tier 1)
- Security: Microsoft Entra ID, Private Link, **document-level access control**, role-based access; security-filter trimming pattern for other sources. (Tier 1)
- Pricing models: dedicated provisioned capacity (Search Units) vs serverless preview. (Tier 1)

---

## Cross-product Comparison

| Structure | Elasticsearch | Algolia | Solr | Meilisearch | Azure AI Search | Strength |
|---|---|---|---|---|---|---|
| Document/record as indexed unit | JSON document | record (attributes + objectID) | document (fields) | document (primary key) | JSON document | **Universal (5/5)** |
| Named index container with per-index config | index + mapping + settings | index + settings | core/collection + schema | index + uid + settings | index + schema | **Universal (5/5)** |
| Field-role configuration (searchable / filterable / sortable / displayed) | mapping + analysis | searchableAttributes, attributesForFaceting, custom ranking | schema field types + index flags | settings (searchable/displayed/filterable/sortable) | schema + analyzers | **Universal (5/5)** |
| Text analysis pipeline (tokenize/normalize; synonyms, stopwords) | analyzers | typo/stop-word handling + NLP settings | analyzers/tokenizers/filters | typo tolerance + synonyms + stop words | analyzers + synonym maps | **Universal (5/5)** |
| Query interface returning **ranked** results | Query DSL / ES|QL | Search API (query + parameters) | query parsers / JSON DSL / SQL | search endpoint (query + parameters) | query request per index | **Universal (5/5)** |
| Relevance tuning as operator work | ranking/reranking, scoring | custom ranking, rules, synonyms | function queries, LTR, elevation | ranking rules chain | scoring profiles, semantic ranking | **Universal (5/5)** |
| Push ingestion API | Index API | send/update data API | update handlers | add documents endpoint | push JSON | **Universal (5/5)** |
| Pull ingestion (connectors/indexers/crawlers) | connectors + pipelines | connectors (docs index) | Tika extraction (guide TOC) | not observed | indexers (pull method) | Common (4/5 observed) |
| Filters & facets | filters, aggregations | filters, facets | faceting | filterableAttributes + facets | filters, faceted navigation | **Universal (5/5)** |
| Typo tolerance / fuzzy / spell-check | fuzzy queries | typo tolerance | spell checking, suggester | typo tolerance (built-in) | fuzzy search | **Universal (5/5)** |
| Autocomplete / suggestions | — (not fetched at this depth) | Query Suggestions (docs index) | Suggester | — (not fetched at this depth) | autocomplete | Common (3/5 directly observed) |
| Highlighting | — (not fetched at this depth) | — (not fetched at this depth) | hit highlighting (guide intro) | — (not fetched at this depth) | — (not fetched at this depth) | Common (1/5 direct + product-page knowledge; treated as common-mature, not asserted per product) |
| Language clients / SDKs | 8+ named clients | SDKs + API clients | SolrJ/JS/Python/Ruby | SDKs 10+ languages (vendor claim) | .NET/Java/JS/Python SDKs | **Universal (5/5)** |
| UI-building layer for the embedding app | Search UI library | build-search-UI guides | — | — | — | Optional (2/5) |
| Search analytics / measurement | via Kibana (L3) | analytics, events, A/B testing | metrics (ops-level) | — | monitoring/diagnostics | Common (3/5) |
| Vector / semantic / hybrid search | dense/sparse vectors, hybrid, rerank | NeuralSearch | dense vector search | auto-embeddings + hybrid | vector + hybrid + semantic rerank | **Universal in current sample (5/5) — era-current, see anti-overfit** |
| Distributed cluster architecture | shards/replicas, cross-cluster | managed (opaque) | SolrCloud + ZooKeeper | single binary (sharding on roadmap-class claims — not asserted) | partitions/replicas (dedicated model) | Variant |
| Schema posture | dynamic or explicit mapping | schemaless records | schema-first (+ schemaless mode) | no schema | schema-first (JSON only) | Variant |
| Managed SaaS / hosted offering | Cloud serverless/hosted | SaaS-native | self-managed (3rd-party hosting exists — not asserted) | Meilisearch Cloud | fully managed service | Variant |
| Document-level security trimming | — (not fetched at this depth) | — | — | — | document-level access control + security filters | Product-supported pattern (1/5 direct) |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

**The developer-operated search-engine substrate.** Three jointly-held structures:

1. **The searchable index as the managed unit of record** — a persistent, named container of operator-supplied documents that the platform transforms into a searchable structure (inverted index and friends) under per-index configuration of how fields are treated (searchable, filterable, sortable, displayed) and how text is analyzed.
   - Remove → a document database or file store; the search-specific transformation and configuration are gone.
2. **The query→ranked-results loop** — a programmatic query interface that accepts a query (text and/or structured conditions) and returns matching documents ordered by computed relevance, with the relevance machinery (analysis, scoring, ranking rules, custom ranking) as the operator's tunable center.
   - Remove the ranking → key-value lookup / unranked filtering = database territory. Remove the loop → a static archive.
3. **The application-builder posture** — the platform is operated as infrastructure that *other* applications integrate through programmatic interfaces (APIs, SDKs, clients); the platform's own operator is a building team, and the searching end user belongs to the embedding application.
   - Remove → the query surface pointed at an organization's own content estate under org access rules = **Enterprise Search Platform**; or a self-crawled public-web corpus served directly to end users = **Web Search Engine**; or an embedded library inside one application = a component, not a platform.

Jointly-held load-bearing tests:
- 1 alone = document database with a text index
- 2 without 1 = stateless ranking service over nothing
- 3 without 1+2 = SDK with no engine
- 1+2 without 3 = a search engine box/library operated for a single direct audience (web-search-engine or embedded-component territory, not the §13 platform Type)
- 2+3 without 1 = query API with no corpus

### L1 — Common Mature Structure

Present across the sample (or across most of it) but not required to recognize the Type:

- text analysis pipeline (tokenization, normalization, stemming, stopwords, synonyms)
- typo tolerance / fuzzy matching / spell-correction
- filters and facets (refinement of result sets)
- pagination and sorting
- custom ranking / boost / scoring profiles / ordered ranking rules
- push ingestion API (universal); pull connectors/indexers (common)
- REST API + language clients/SDKs
- autocomplete / query suggestions
- highlighting of matched terms
- search analytics / usage measurement
- API-key and role-based access control
- vector/semantic/hybrid search and reranking (**era-current**: universal in the 2026 sample, absent in the pre-2020 generation — see anti-overfit)
- aggregations/analytics over indexed data (the "analytics engine" extension)

### L2 — Variant / Optional Structure

- **Deployment shape**: self-hosted open-source engine / vendor-managed cloud / fully-managed SaaS API / hyperscaler managed service
- **Schema posture**: schema-first (declared field types) vs schemaless/dynamic/inferred
- **Query style**: query DSL vs query parsers vs parameter-based request
- **Scale-out architecture**: distributed cluster (shards/replicas/coordination service) vs single binary
- **Corpus/use-case domain**: ecommerce/product search, site search, app search, documentation search, RAG grounding, log/metrics search (engine reuse)
- **Tenancy & commercial model**: multi-tenant SaaS vs single-tenant deployment; usage-based vs provisioned capacity
- **AI depth**: lexical-only → hybrid → semantic rerank → agentic retrieval / conversational layers
- **Document-level security trimming**: present in some products, absent/not-observed in others

### L3 — Vendor-specific Structure (research notes only)

- **Elastic**: ES|QL piped query language; Kibana; data streams; searchable snapshots; data tiers; Jina AI models; Agent Builder; the Observability and Security solution families built on the same engine; cross-cluster search.
- **Algolia**: NeuralSearch; Dynamic Re-Ranking; Query Suggestions; personalization (classic/advanced); click/conversion events; A/B testing; Agent Studio; MCP server; applications as environment containers (testing/staging/production); "index names are publicly visible" SaaS guidance.
- **Solr**: Streaming Expressions + math expressions; SQL interface + JDBC; SolrCloud + ZooKeeper; Solr Cell/Tika extraction; Learning To Rank; Query Elevation; configsets; phonetic matching; circuit breakers/rate limiters.
- **Meilisearch**: the seven default ranking rules chain (words, typo, proximity, attributeRank, sort, wordPosition, exactness); atomic index swapping; auto-embedders; implicit index creation; distinct attribute; "<50ms" marketing claim.
- **Azure**: agentic retrieval (knowledge bases / knowledge sources / query planning); AI enrichment skillsets; integrated vectorization; semantic ranking; Search Units pricing; serverless preview model; Entra ID / Private Link integration; Foundry IQ underpinning.

## Anti-overfit Analysis

- **Inverted index / BM25 / Lucene lineage NOT definitional.** 5/5 samples use inverted indexes under the hood (Azure documents inverted indexes explicitly; Elastic/Solr via Lucene), but the invariant is the *searchable transformed corpus + ranked retrieval*, not the data structure. A platform could rank by other means. Historical check: pre-inverted-index-era and non-Lucene engines (Sphinx, Xapian) satisfy the core.
- **Vector/semantic/hybrid search NOT definitional.** Universal in the 2026 sample (5/5) but absent from the pre-2020 generation of the same products (Solr 8-era, Elasticsearch pre-8, early Algolia, early Meilisearch, pre-AI Azure Search). Era-current capability → L1, not L0. Also protects the boundary vs the §13 siblings Vector Retrieval Platform / Semantic Search Platform.
- **Cloud/SaaS delivery NOT definitional.** Self-hosted OSS poles (Solr, Meilisearch self-host, Elastic self-managed) satisfy the core fully.
- **Distributed cluster NOT definitional.** Meilisearch's single-binary pole satisfies the core.
- **Schema-first NOT definitional.** Schemaless poles (Algolia records, Meilisearch, Elastic dynamic mapping) and schema-first poles (Solr, Azure) both satisfy.
- **Facets/autocomplete/highlighting NOT definitional.** Standard capabilities; a minimal engine without them is still recognizably a search platform.
- **Connectors/indexers NOT definitional.** Push-only ingestion (Meilisearch observed; Algolia push documented as the primary path) satisfies the core.
- **"Analytics engine" extension NOT definitional.** Aggregations are common but the analytics use (log analytics, metrics) is the engine reused by adjacent Types (see boundaries).

## Historical / Market-Sample Check

- **Older generation (2000s–2010s)**: Solr (Lucene lineage), Sphinx Search, Xapian, dtSearch (desktop + SDK) — operator-supplied corpus → index → query API → ranked results → embedded into applications. All satisfy the three-leg core with no cloud, no vectors, no SaaS. ✓
- **Library pole**: Apache Lucene itself is an engine *library* embedded in one application — it fails the application-builder posture (nothing is operated as a platform for other applications; it is a component). The Type requires the operated-service posture. Lucene is the conceptual substrate/ancestor, documented as such. ✓ (definition survives by excluding the library pole)
- **Platform-native / database-embedded**: PostgreSQL full-text search, MySQL FULLTEXT — capabilities of a database Type, not a standalone operated platform. Excluded by the platform posture + center-of-gravity (the product's center is the database, not search). ✓
- **Regional/vertical engines**: ecommerce search appliances, regional enterprise engines — all satisfy the core; vertical tuning is corpus-domain variant (L2). ✓
- **Hosted site-search SaaS** (crawler + widget for one website): satisfies the three legs if its center is the engine/API substrate; if its center is a finished widget with no programmatic substrate, it drifts toward a packaged application. Treated as a packaging variant of this Type where the API substrate exists; flagged as an uncertainty (not directly sampled).

## Vendor-specific Findings

See L3 above. None promoted to the canonical model.

## Rejected Findings

- "Search Platform = Elasticsearch-style distributed cluster" — rejected (single-binary pole in-sample).
- "Search Platform = SaaS API product" — rejected (self-hosted poles in-sample).
- "Search Platform = vector database with text search added" — rejected (lexical full-text is the historical core; vector is the era-current addition; the §13 taxonomy also carries separate vector-retrieval siblings).
- "Relevance = BM25 scoring" — rejected (ranking machinery varies: tie-breaking chains, ranking-rule lists, scoring profiles, LTR; the invariant is *tunable computed relevance*, not any specific algorithm).
- "Search Platform includes its own dashboards/UI" — rejected as definitional (Kibana/Algolia dashboard/Azure portal/Solr Admin UI are management surfaces; the Search UI library layer is optional; the embedding application owns the end-user search UI).

## Boundary Findings

1. **vs Enterprise Search Platform (§10, processed)** — pre-hung seam from the ESP pass, RATIFIED here: the operating target. ESP = the organization's distributed internal content estate, ingested under the organization's access rules, surfaced to members through one query surface. Search Platform = a substrate a building team operates so that *arbitrary applications* (theirs or their customers') can embed search over corpora the team supplies. Removal tests: strip the application-builder posture and point one query surface at the org estate with org access rules → ESP; give the ESP an API/SDK substrate for developers to build custom search apps → it grows a Search Platform facet (engine-lineage packaging pole). Elastic legitimately serves both — packaging variant, no taxonomy change (consistent with the ESP pass).
2. **vs Web Search Engine (§02.02)** — corpus ownership + audience. Web search engine crawls and operates its own public-web corpus and serves end users directly. Search Platform's corpus is supplied by the operating team; end users belong to embedding applications. Remove operator-supplied corpus → web search engine.
3. **vs Vector Retrieval Platform / Semantic Search Platform (§13 siblings, unprocessed)** — center of gravity. Those Types (expected) center embedding-similarity retrieval as the product's core; Search Platform centers general-purpose ranked retrieval with a lexical full-text core (vector/hybrid as era-current capabilities). All five sampled products now ship vector/hybrid — convergence watch; joint-review flag raised for the sibling passes.
4. **vs RAG Development Platform (§13 sibling, unprocessed)** — substrate vs orchestration. Search Platform provides the retrieval substrate; RAG platforms orchestrate retrieval + generation pipelines. Azure's agentic retrieval and Meilisearch's conversational search drift toward the RAG side — recorded as L2 AI-depth variant, not a Type change. Flag for the sibling pass.
5. **vs Code Search Platform (§12, processed)** — corpus + query semantics. Code search centers a managed source-code corpus with code-aware queries (repo/path/language scoping, symbol search). Search Platform is domain-agnostic documents. A search platform *can* host a code corpus (and code-search products can be built on search engines) — the code-aware query semantics and VCS-bound corpus are the seam.
6. **vs Database / SQL workbench Types** — center of gravity. Databases center transactional/structured query over tables; Search Platform centers relevance-ranked retrieval over documents. Database FTS is an embedded capability of another Type. Removal test: remove relevance ranking + the document/index model → database.
7. **vs Log Management / Observability (§14)** — engine reuse. Engine-lineage products are widely reused as log stores (Elastic ships whole Observability/Security families on the same engine). That is an adjacent *use* of the engine by other Types, not this Type's center; the Search Platform document should not absorb observability.
8. **vs Data Catalog (§13)** — object of search. Data catalog searches *metadata about datasets*; Search Platform searches *the operator's content corpus*. Clean seam.
9. **vs Site-search SaaS / hosted website search** — packaging. A hosted search widget for one website is a packaged application; where the product's center is the API/engine substrate (developer-integrable), it is this Type in a managed-packaging variant. Not directly sampled — uncertainty recorded.

## Uncertainties

- Solr evidence is the Reference Guide index (official, Tier-1 structural) — deep operational pages unreachable (404 ×2). No Solr-specific numeric or workflow claims made; Solr's role in the sample is the classic-OSS/schema-first pole, which its guide index evidences adequately.
- Highlighting/autocomplete presence per product was not uniformly fetched at depth; treated as common-mature capabilities without per-product assertions.
- Whether hosted site-search SaaS products (crawler+widget, no API substrate) constitute a variant of this Type or a separate packaged-application Type — not sampled; left as an open question for any future site-search leaf.
- The exact state of Meilisearch distributed/sharded deployment (marketing-adjacent claims only) — not asserted.
- Elastic's document-level security (DLS) was not fetched at depth; document-level security trimming is asserted only for Azure (direct evidence) and phrased as a product-supported pattern in the final document.
- Boundary vs the unprocessed §13 siblings (Vector Retrieval Platform, Semantic Search Platform, RAG Development Platform) is reasoned from this sample's evidence + the directory structure; joint review recommended when those passes run.

## Final Synthesis

A Search Platform (§13) is the developer-operated search-engine substrate: a platform whose unit of record is the **searchable index** — a persistent named container of operator-supplied documents transformed into a searchable structure under per-index field/relevance configuration — whose defining loop is **query → ranked results** through a programmatic interface with tunable relevance machinery, and whose defining posture is the **application-builder substrate**: the platform is operated by a building team and integrated into other applications through APIs/SDKs, with the searching end user belonging to the embedding application.

Everything else — analysis pipelines, typo tolerance, facets, autocomplete, connectors, analytics, vector/hybrid search, distributed clusters, managed clouds, dashboards — is standard mature capability or variant structure, not definition. The definition survives the historical check (2000s-era engines satisfy it; the Lucene library pole and database-embedded FTS are excluded by the platform posture; vector-free generations satisfy it).

The sharpest boundary is vs Enterprise Search Platform (operating target: arbitrary applications vs the organization's content estate — Elastic-class products legitimately straddle as a packaging pole) and vs Web Search Engine (operator-supplied corpus vs self-crawled public corpus). Convergence watch vs the §13 vector/semantic/RAG siblings.
