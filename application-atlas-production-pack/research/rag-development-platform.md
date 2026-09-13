# Research Notes — RAG Development Platform

Research date: 2026-09-09
Methodology: WORKFLOW v1.1 / WRITING GUIDE v1.1

## Research Goal

Understand what a **RAG Development Platform** actually is as an Application Type: what objects it holds, what the developer builds and operates on it, how the retrieve-then-generate loop is realized across real products, and where its boundaries lie against vector databases, search platforms, LLM application development platforms, and end-user knowledge assistants.

## Initial Boundary

Working hypothesis before research:

- A RAG (Retrieval-Augmented Generation) Development Platform is a developer-facing platform for building applications in which an LLM's answers are **grounded in an external/private knowledge corpus retrieved at query time**.
- Expected core objects: corpus/index, documents, chunks, embeddings, retrieval, prompt composition, generated answers with citations.
- Likely confusions:
  - **Vector Retrieval Platform / Vector Database** — retrieval infrastructure without the generation binding.
  - **Search Platform / Semantic Search Platform** — returns ranked results, not generated grounded answers.
  - **LLM Application Development Platform** — broader; RAG is one pattern among several (agents, extraction, workflows).
  - **Enterprise Knowledge Assistant** — end-user product; the RAG platform is the machinery such products are built on.
  - **AI Gateway / Model Routing** — model access without corpus or retrieval.

## Research Questions

1. What is the platform's unit of record for knowledge (corpus / collection / index / knowledge base / context), and what does it hold?
2. What does the ingestion path look like (connectors, parsing, chunking, embedding, indexing, incremental updates)?
3. What does the query path look like (query processing → retrieval → rerank → prompt composition → generation → citations)?
4. What is the developer build surface (APIs, SDKs, pipelines, consoles, query languages)?
5. How is the LLM coupled (platform-hosted vs BYO vs per-query choice)? Is the LLM part of the platform or external?
6. How do grounding, citations, evaluation, and observability appear as platform capabilities?
7. Where exactly is the seam to the vector database / search platform on one side and the LLM application platform / end-user assistant on the other?
8. Does the defining core survive without vectors (keyword/lexical retrieval), without chunking-as-config, without a specific deployment model?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Tier / shape |
|---|---|---|
| **Pinecone** (Database + Assistant + Nexus) | Managed infrastructure vendor that grew a full managed-RAG surface on top of a vector database | Commercial SaaS; startup→enterprise |
| **Weaviate** | Open-source vector database with RAG built in as database-level "generative search" modules | OSS self-host + managed cloud; developer-first |
| **Vectara** | API-first end-to-end RAG/grounded-generation platform (now self-labeled "agentic platform"), retrieval engine + hallucination grading | Commercial SaaS/VPC/on-prem/air-gapped; enterprise |
| **AWS Bedrock Knowledge Bases** | Hyperscaler-managed RAG pipeline inside a broader AI platform; managed vs customer-managed split | Cloud-vendor-native; enterprise |

Boundary check product (not a representative sample member): **LlamaIndex** — framework/library pole, used to test the seam against LLM Application Development Platform.

## Sources

All fetched 2026-09-09 (Layer A — directly observed official documentation):

- Pinecone — https://docs.pinecone.io/ (documentation home); https://docs.pinecone.io/llms.txt (doc index); https://docs.pinecone.io/guides/nexus/concepts.md (Nexus key concepts); https://docs.pinecone.io/guides/assistant/overview.md (Assistant overview)
- Weaviate — https://weaviate.io/developers/weaviate (database intro); https://weaviate.io/developers/weaviate/search/generative (RAG / generative search)
- Vectara — https://docs.vectara.com/docs (about); https://docs.vectara.com/docs/platform-architecture/platform-stack (platform stack)
- AWS — https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html (Knowledge Bases); https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html (how KBs work)
- LlamaIndex (boundary check) — https://docs.llamaindex.ai/en/stable/understanding/ ("Building an LLM application")

No source-access limitations encountered; all official documentation pages fetched successfully.

## Product Observations

### Pinecone (evidence layer A)

Official self-description: "the vector database for AI agents and applications, built for semantic search, knowledge retrieval, and long-term memory at scale." Three product surfaces:

1. **Database** — managed vector indexes; semantic search and knowledge retrieval; embedding and rerank models offered through an inference API (large catalog of third-party embedding/reranking models documented per-model).
2. **Assistant** — "a managed service for building production-grade RAG chat and agent applications grounded in your data." Documented workflow: create assistant → upload documents ("Your assistant manages chunking, embedding, and storage for you") → chat ("your assistant queries a large language model (LLM) with context from your documents to ensure the LLM provides grounded responses") → evaluate answers (metrics: correctness, completeness, alignment, with fact-level entailment reasoning) → optimize (custom instructions, metadata filtering) → retrieve context snippets (snippets usable "with your own LLM, RAG application, or agentic workflow"). Chat responses carry **citations** with file name, page numbers, file metadata, and signed URLs. Model selectable per chat call (example uses gpt-4o).
3. **Nexus** — "the knowledge engine for agents. It compiles your data into queryable knowledge once, then serves grounded, cited answers to agents on every call." Core concepts: **sources** (uploaded files, repo URLs, connectors such as Box/Google Drive with OAuth), **workspace** (tenancy boundary backed by a project), **context** ("the unit of knowledge: Sources → Manifest → Knowledge"; one context per dataset; a query reads one or more), **manifest** (JSON plan defining "what to chunk, embed, and distill into artifacts"), **tasks/workflows** (Import ingests and cleans sources; Curate builds artifacts per the manifest; Explore proposes a manifest; Optimize self-tunes the manifest from real query traffic; Search answers a query), **artifacts** (condensed knowledge with type/kind/scope/provenance, linked by typed edges into a knowledge graph), **query** ("a question asked against one or more curated contexts... Nexus plans its own retrieval and answers with citations"), **KnowQL** (declarative query language: `scope` of contexts + `ask` + optional typed `shape`), **sessions** (multi-turn conversation state). Query tracing exposes reasoning steps, retrieval tool calls, token usage, latency, cost. Curation is explicit: a context is "not queryable until you import sources and curate them — curate is explicit." BYOC deployment option.

### Weaviate (evidence layer A)

Official self-description: "an open-source, AI vector database... designed to store and index both data objects and their vector embeddings." Key capabilities listed: semantic and hybrid search; **retrieval augmented generation (RAG)** ("Weaviate can serve as a robust backend for RAG workflows, where vector search is used to retrieve context that enhances the output of generative models"); agent-driven workflows.

RAG as a database feature ("generative search"): "a RAG query consists of two parts: *a search query*, and *a prompt for the model*. Weaviate first performs the search, then passes both the search results and your prompt to a generative AI model before returning the generated response."

- Generative model provider configured per collection (default) and/or per query; integrations with third-party providers (examples show OpenAI, Anthropic).
- Two generation shapes: **single prompt** (a generated response per retrieved object, with `{prop-name}` interpolation of retrieved content into the prompt) and **grouped task** (one response over all retrieved objects, with optional property selection to limit prompt length).
- Images can be supplied as generation input.
- Search strategies available to the RAG query: vector similarity (near_text), keyword (BM25), hybrid, image/multimedia, multi-target vectors; plus filters, reranking, boost.
- Named vectors: collections can carry multiple named vectors; queries must target one.
- Deployment: Weaviate Cloud (managed), Docker, Kubernetes, Embedded (in-process from Python/JS).
- Adjacent services: Query Agent (agentic search over cloud collections, translates natural-language questions into optimized queries), Weaviate Embeddings (managed embedding inference), Engram (managed memory for agents).

### Vectara (evidence layer A)

Official self-description: "an **API-first Agentic Platform** for building production-grade AI agents and assistants that retrieve knowledge, reason over context, use tools, and deliver grounded answers with step-level audit trails, fine-grained access controls, real-time policy and factual-consistency enforcement." Historically known as a RAG-as-a-service platform; the RAG machinery is explicit in the stack.

Seven documented layers:

1. **Interfaces** — REST API (primary), coding-agent skills, Admin Console (inspect sessions, replay retrieval traces, tune HHEM thresholds, manage corpora/agents/pipelines).
2. **Agent runtime** — stepped state machines, sub-agent delegation, structured-output gating, cross-session approvals.
3. **Tools** — 35+ built-in tools, Python Lambda tools, MCP servers.
4. **LLM gateway** — hosted models (Anthropic, OpenAI, Gemini, on-prem specialized) + BYO LLM ("bring your own deployment. The platform calls it the same way it calls the hosted models").
5. **Retrieval engine** — "a six-stage pipeline, tunable at every stage. Not a one-shot vector lookup": `Documents → Chunking → Boomerang (embedding) → Hybrid (BM25 + dense + filters) → Slingshot reranker → Citations → Generation-ready context`. Chunking: "sentence or max-chars chunking; never crosses section boundaries." Citations: "every retrieved chunk travels with its source. The generated answer cites the documents it grounded on."
6. **Corpora & ingestion** — "A corpus is more than a vector store: it is writable, filterable, multilingual semantic storage." One primitive serves knowledge, memory, and scratchpad. Filter attributes (user_id, session_id, doc_type, tier) turn a corpus into structured storage; multi-corpus search at query time; "RBAC is enforced at retrieval: a user only ever sees chunks their identity is entitled to see." Ingestion runs as **pipelines**: "pulls records from a source (S3, SharePoint, web, Salesforce, Slack, Notion, Google Drive, GitHub, custom) on a schedule (cron, interval, manual, webhook)."
7. **Foundation** — tenant isolation, IdP/SSO, RBAC by corpus, audit and traces ("Every query, retrieval source, prompt, LLM call, citation, and HHEM score is logged"), encryption, no training on customer data.

Quality machinery: **HHEM** grades every answer for hallucination (documented as under 50ms per answer); **Hallucination Corrector** "rewrites ungrounded spans rather than fabricating"; query observability; Open Eval Framework. Deployment: SaaS, VPC, on-premises, air-gapped.

### AWS Bedrock Knowledge Bases (evidence layer A)

Official description: "With Amazon Bedrock Knowledge Bases, you can integrate proprietary information into your generative-AI applications. When a query is made, a knowledge base searches your data to find relevant information to answer the query. The retrieved information can then be used to improve generated responses."

Canonical RAG mechanics documented in two phases:

- **Pre-processing**: "convert the data into text and split it into manageable pieces. The pieces or chunks are then converted to embeddings and written to a vector index, while maintaining a mapping to the original document."
- **Runtime**: "an embedding model is used to convert the user's query to a vector. The vector index is then queried to find chunks that are semantically similar... the user prompt is augmented with the additional context from the chunks... The prompt alongside the additional context is then sent to the model to generate a response."

Two knowledge-base types:

- **Managed Knowledge Base** — "Amazon Bedrock manages the underlying data ingestion, indexing, storage, and retrieval infrastructure"; connectors for S3, SharePoint, Confluence, Google Drive, OneDrive, Web Crawler; document-level permission filtering with ACLs at retrieval time; Smart Parsing (auto-selects parsing strategy per document type incl. PDFs, PPTX, DOCX, audio, video, scanned docs); agentic retrieval (multi-hop reasoning, query decomposition into sub-queries, iterative retrieval across multiple KBs, sufficiency evaluation); native AgentCore Gateway integration (MCP-compatible agents invoke the KB as a tool); observability with retrieval traces and per-KB metrics.
- **Customer-managed Knowledge Base** — "you set up and manage your own RAG pipeline, including the vector store (such as Amazon OpenSearch Serverless, Amazon Aurora, and Amazon Neptune), and have full control over data ingestion, parsing, indexing and storage configurations."

Capabilities: answer queries "either with direct quotations from sources or with natural responses generated from the query results"; augment your own prompts with retrieved information; citations ("so the original data source can be referenced and accuracy can be checked"); multimodal (images extracted from documents and retrievable; image queries); reranking models. Also: zero-setup "chat with your document"; structured data stores; Kendra GenAI index; Neptune Analytics graphs.

### LlamaIndex (boundary check, evidence layer A)

Official framing: "Building an LLM application" — a code framework with three main parts: **Building a RAG pipeline**, **Building an agent**, **Building Workflows**. RAG pipeline stages documented as Loading & Ingestion (connectors via LlamaHub), Indexing and Embedding, Storing (vector stores), Querying. RAG described as "a key technique for getting your data to an LLM, and a component of more sophisticated agentic systems." The developer assembles components in their own code; there is no hosted corpus of record in the open-source framework itself (LlamaCloud exists as a separate managed service: LlamaCloudIndex + LlamaCloudRetriever, LlamaParse). Dozens of LLM and embedding integrations; hundreds of vector-store integrations.

**Classification**: framework/library, not a platform with a managed corpus — belongs to the LLM Application Development Platform neighborhood; used here as boundary evidence only.

## Cross-product Comparison

| Dimension | Pinecone | Weaviate | Vectara | AWS Bedrock KB |
|---|---|---|---|---|
| Knowledge unit of record | Assistant: assistant holding uploaded files; Nexus: **context** (Sources → Manifest → Knowledge) | **collection** (objects + embeddings) | **corpus** (writable, filterable semantic storage) | **knowledge base** (data sources → embedded chunks mapped to originals) |
| Ingestion | file upload; connectors (Box, Google Drive, OAuth); curation tasks (import/curate/explore/optimize) | developer inserts objects via API; embeddings via model-provider integrations | ingestion **pipelines** from S3/SharePoint/web/Salesforce/Slack/Notion/GDrive/GitHub on schedules | connectors (S3, SharePoint, Confluence, GDrive, OneDrive, web crawler); managed or customer-managed pipeline |
| Chunking | managed by Assistant; manifest-driven in Nexus | developer-side (objects are what you insert) | platform chunking (sentence/max-chars, section boundaries) | managed (Smart Parsing) or customer-configured |
| Embedding | platform-managed or via inference API | via model-provider integrations; named vectors | platform model (Boomerang) | service-managed or choose-your-own |
| Retrieval | Nexus "plans its own retrieval"; Assistant retrieves context snippets | vector / keyword (BM25) / hybrid + filters + rerank | hybrid BM25 + dense + filters, reranker chain, per-query metadata filters | semantic search, multimodal, agentic multi-hop, reranking |
| Generation binding | Assistant chat (LLM + document context, citations); Nexus KnowQL (grounded, cited answers) | generative modules: single prompt / grouped task, provider per collection or query | generation-ready context → LLM gateway (hosted or BYO) | prompt augmented with chunks → model generates; direct quotations or natural responses |
| Citations | yes (file, pages, metadata, signed URLs) | not a first-class part of the generative-search feature (retrieved objects are the references) | yes ("every retrieved chunk travels with its source") | yes (original data source referenced) |
| Grounding / quality machinery | evaluation metrics (correctness / completeness / alignment) | — | HHEM hallucination grading + Hallucination Corrector + query observability + eval framework | accuracy checking via citations |
| Build surface | APIs, Python/Node SDKs, console, MCP server | client libraries (Python/JS/Go/Java/C#), GraphQL/REST/gRPC | REST API, SDKs, console, coding-agent skills, pipelines | AWS console/API/SDK; AgentCore Gateway (MCP) |
| Deployment | SaaS (+ BYOC for Nexus) | OSS self-host (Docker/K8s/embedded) + managed cloud | SaaS / VPC / on-prem / air-gapped | AWS-managed service |
| LLM coupling | model selectable per chat call; Nexus model guidance | BYO provider integration (per collection/query) | hosted + BYO endpoint | service-managed or choose-your-own models |
| Multi-turn state | sessions (Nexus) | — (developer-side) | sessions, cross-session approvals | — (application-side) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A RAG Development Platform is a **developer-facing platform whose defining core is the managed retrieve-then-generate loop over a maintained knowledge corpus**. Four jointly-held structures:

1. **The knowledge corpus as a managed unit of record** — external documents/data brought into the platform and held in processed, retrievable form (retrievable units carrying provenance back to their sources). Remove → raw LLM API / prompt tooling with no knowledge of record.
2. **The retrieval stage** — query-time selection of relevant corpus units (implementation may be vector, keyword, or hybrid; with filtering/reranking). Remove → generation without grounding = plain LLM application.
3. **The generation binding** — retrieved units + the user query are composed into a prompt for an LLM, producing a grounded response that references its sources. Remove → vector database / search platform territory.
4. **The developer build surface** — APIs/SDKs/pipelines/consoles through which developers construct, configure, and operate the loop as parts of their own applications. Remove → an end-user assistant product (Enterprise Knowledge Assistant territory).

Jointly-held load-bearing checks:
- 1 alone = vector database / semantic storage (Pinecone Database, Weaviate-as-database).
- 2 without 1 = retrieval over nothing.
- 3 without 1+2 = plain LLM application.
- 4 without 1–3 = build surface over nothing (framework with no corpus).
- 1+2 without 3 = search/retrieval platform.
- 1+3 without 2 = LLM with a document dump, no relevance machinery.

### L1 — Common Mature Structure

Present across the sample, not required for the definition:

- **Chunking/parsing** of source documents into retrievable units (platform-managed in Pinecone Assistant/Vectara/AWS Managed KB; developer-side in Weaviate; manifest-configured in Nexus).
- **Embedding model management** — platform-provided models or BYO provider integrations; named/multiple vectors per object (Weaviate).
- **Hybrid retrieval** — vector + keyword (BM25) with metadata filters (Vectara, Weaviate, AWS; Pinecone via sparse+dense models).
- **Reranking** (Vectara Slingshot chain, AWS reranking models, Pinecone rerank models, Weaviate rerank module).
- **Citations / source references** in generated answers (Pinecone, Vectara, AWS; Weaviate's generative search returns the retrieved objects alongside generated text instead).
- **Connectors** to enterprise sources (S3, SharePoint, Confluence, Google Drive, OneDrive, web, Salesforce, Slack, Notion, GitHub, Box).
- **Evaluation / quality tooling** — answer metrics (Pinecone correctness/completeness/alignment), hallucination grading (Vectara HHEM), eval frameworks.
- **Observability / tracing** — retrieval traces, reasoning steps, token usage, cost (Pinecone Nexus tracing, Vectara query observability, AWS retrieval traces).
- **Multi-turn sessions** with conversation state (Pinecone Nexus sessions, Vectara sessions).
- **Retrieval-time access control** — document-level ACL/RBAC filtering (AWS ACLs, Vectara RBAC at retrieval).
- **MCP / agent integration surfaces** (Pinecone MCP server, AWS AgentCore Gateway, Vectara MCP tools, Weaviate MCP server).

### L2 — Variant / Optional Structure

- **Product shape**: retrieval-infrastructure-first (vector DB; developer builds the rest) ↔ full-stack managed RAG API (upload → query) ↔ customer-managed pipeline (AWS customer-managed KB) ↔ framework/library (LlamaIndex — boundary, see below).
- **Deployment**: SaaS ↔ OSS self-hosted ↔ VPC/on-prem/air-gapped ↔ cloud-vendor-native.
- **LLM coupling**: platform-hosted models ↔ BYO endpoint ↔ per-call model selection.
- **Agentic extension**: agentic retrieval (multi-hop, query decomposition, sufficiency evaluation — AWS), agent runtimes (Vectara stepped state machines), agent-facing query languages (KnowQL). Increasingly common; not definitional.
- **Multimodal**: image extraction and retrieval, image queries, multimodal embeddings (AWS, Weaviate, Pinecone).
- **Corpus reuse semantics**: corpus as knowledge only vs corpus also serving agent memory/scratchpad (Vectara documents this explicitly).
- **Governance depth**: tenant isolation, audit streaming to SIEM, compliance certifications (Vectara, AWS) — enterprise-tier variant.

### L3 — Vendor-specific Structure (Research Notes only)

- Pinecone: Nexus manifest/curation ledger/artifacts/KnowQL; Assistant evaluation metrics API; serverless indexes; BYOC.
- Weaviate: generative modules' single_prompt/grouped_task shapes; named vectors; Query Agent; Engram; embedded deployment mode.
- Vectara: HHEM + Hallucination Corrector; Boomerang embeddings; Slingshot reranker chain; stepped state-machine agent runtime; UserFn expression language.
- AWS: Managed vs Customer-managed KB split; Smart Parsing; AgentCore Gateway; Kendra GenAI index; Neptune Analytics graphs; binary vs float32 vector trade-off documentation.

## Vendor-specific Findings

- Vectara's self-positioning has drifted from "RAG-as-a-service" toward "agentic platform" (its own docs now lead with agents); the RAG machinery (corpora, retrieval engine, grounded generation, HHEM) remains the documented substrate. Market-label noise: vendors converge on "agents" branding while the RAG loop stays central.
- Pinecone now ships three surfaces (Database / Assistant / Nexus) — the same vendor spans the vector-database Type and the RAG-platform Type; the seam inside one vendor confirms the boundary rather than dissolving it.
- Weaviate implements RAG as a database query feature (generative search) rather than a separate service — the generation binding can live at the database layer.
- AWS splits the Type internally: managed KB (platform runs the pipeline) vs customer-managed KB (developer runs the pipeline on AWS infrastructure) — both marketed under one feature name.

## Boundary Findings

- **vs Vector Retrieval Platform / Vector Database**: retrieval infrastructure without the generation binding. Test: does the platform bind retrieval results into LLM generation as a first-class capability? Pinecone Database alone fails the test; Pinecone Assistant/Nexus pass. Weaviate passes only through its generative modules.
- **vs Search Platform / Semantic Search Platform**: search's terminal object is a ranked result list consumed by the application; the RAG platform's terminal object is a generated, grounded, source-referenced answer.
- **vs LLM Application Development Platform**: broader Type — builds any LLM application (agents, workflows, structured extraction); RAG is one pattern. Frameworks (LlamaIndex, LangChain, Haystack) sit here: code libraries with no hosted corpus of record. LlamaIndex's own docs frame RAG as one of three parts of "building an LLM application." The RAG platform holds the corpus and operates the loop; the framework lets the developer assemble it.
- **vs Enterprise Knowledge Assistant**: end-user product (chat over company knowledge for non-developers). The RAG platform's user is a developer building such products. Pinecone Assistant straddles deliberately: an API for developers to build assistants — the developer remains the user.
- **vs AI Gateway / Model Routing**: model access without corpus, retrieval, or grounding.
- **vs Knowledge Graph Platform**: different representation (entities/relations vs retrievable passages); note Pinecone Nexus artifacts form "a knowledge graph" via typed edges — a vendor-specific convergence, not a Type merger.
- **Remove-what test**: remove the generation binding → vector database/search platform; remove the corpus of record → LLM application framework; remove the build surface → end-user assistant; remove retrieval → prompt/LLM tooling.

## Historical / Market-Sample Check

RAG as a named technique is young (term popularized ~2020; product category ~2023+). Checks applied:

- **Vector-free fit**: the defining core does not require vector embeddings — keyword/BM25-first retrieval bound to generation satisfies it (Vectara hybrid, Weaviate BM25, AWS keyword paths). The invariant is the retrieval stage, not the vector representation.
- **Chunking-free fit**: chunking is the common implementation of "retrievable units," not the invariant; Weaviate's developer-defined objects and Nexus's artifact distillation show the unit granularity varies.
- **Chat-free fit**: the loop does not require a conversational surface — single-shot query→grounded-answer (AWS "direct quotations or natural responses") and multi-turn sessions (Nexus) both fit.
- **Pre-LLM lineage**: classic enterprise search + summarization systems do NOT satisfy the definition (no LLM-class generation binding) — the Type is intrinsically LLM-era; the definition should say so honestly rather than stretch to include IR history.
- **Anti-overfit against the 2023–2024 default implementation** (vector DB + chunk-500-tokens + LangChain glue): guarded by keeping vectors, chunk sizes, and frameworks out of the core.

## Uncertainties

- The market boundary between RAG Development Platform and LLM Application Development Platform is actively blurring (Vectara → "agentic platform"; Pinecone Assistant → agent features; LlamaIndex → LlamaCloud managed service). Recorded as a convergence trend; not resolved here.
- Weaviate's generative search does not document citations as a first-class feature of that API (the retrieved objects serve as references); assertion kept product-specific.
- Pinecone Nexus is new (2026 docs); its concept vocabulary (manifest, artifacts, KnowQL) may not stabilize; treated as L3.
- Sample depth: 4 representative products + 1 boundary check. Additional candidates (Qdrant, Elasticsearch, Azure AI Search, Vertex AI Search, NVIDIA NeMo Retriever) not fetched; stop conditions met (stable commonalities emerged; further products would repeat evidence).
- Whether "RAG Development Platform" products must expose evaluation tooling to qualify: only 3 of 4 sampled do (Weaviate does not, at the database layer). Kept in L1, not L0.

## Final Synthesis

The RAG Development Platform is the developer-facing system of record and operation for the retrieve-then-generate loop: it holds an external knowledge corpus in processed retrievable form, executes query-time retrieval against it, binds the retrieved units into LLM generation, and exposes the whole loop to developers as buildable, configurable, observable machinery. Its four load-bearing structures — corpus of record, retrieval stage, generation binding, developer build surface — jointly distinguish it from the vector database (no generation binding), the search platform (no generation), the LLM application platform (no corpus of record), and the end-user knowledge assistant (no build surface). Everything else — chunking strategies, embedding models, hybrid search, rerankers, citations, connectors, evaluation, tracing, agentic retrieval, deployment topology — is mature common structure or variant machinery, documented as such.
