# RAG Development Platform

## Overview

A **RAG Development Platform** is a developer-facing platform for building applications in which an LLM's answers are grounded in a maintained body of knowledge: the platform holds an external corpus in retrievable form, retrieves the passages relevant to a query at run time, and binds those passages into the LLM's prompt so the generated answer reflects — and cites — the corpus rather than the model's general training alone.

The technique the platform operationalizes is Retrieval-Augmented Generation (RAG): instead of fine-tuning a model on private data, the application retrieves relevant material at query time and lets the model compose its answer from it. A RAG Development Platform turns that technique into managed, buildable machinery: ingestion pipelines, a queryable knowledge corpus, retrieval engines, generation bindings, and the APIs and consoles through which developers assemble, evaluate, and operate all of it inside their own applications.

The defining core is deliberately small:

```text
Knowledge corpus (unit of record)
└── Retrieval stage (query → relevant corpus units)
    └── Generation binding (retrieved units + query → LLM → grounded, source-referenced answer)
        └── Developer build surface (APIs / pipelines / consoles to construct and operate the loop)
```

Everything commonly associated with modern products — vector embeddings, chunking strategies, hybrid search, rerankers, connectors, evaluation dashboards, agentic retrieval — is widespread in current implementations but is not what makes the platform a RAG platform. Remove the generation binding and the product is a vector database or search platform; remove the corpus of record and it is an LLM application framework; remove the build surface and it is an end-user assistant product.

## Users & Context

The primary user is a **developer building an application that answers questions or generates content over a body of knowledge the base LLM does not know**: AI engineers, backend engineers, and platform teams assembling question-answering services, search-and-summarize features, support assistants, research and analysis tools, and agent back-ends over proprietary documents, wikis, tickets, manuals, or code.

Typical work modes:

- **Build**: connect data sources, configure how documents become retrievable content, wire the query path into their application's API or chat surface.
- **Tune**: adjust retrieval behavior (search strategy, filters, reranking) and generation behavior (instructions, model choice, citation requirements) against real queries.
- **Evaluate and operate**: check answer quality, inspect what was retrieved and cited for a given answer, monitor cost and latency, and manage the corpus as source data changes.

Secondary users include platform/ops engineers who run the deployment (especially in self-hosted or private deployments) and data owners who govern what may be retrieved. The end users who ultimately see the answers are users of the developer's application, not users of the platform itself — the platform's console and APIs face the builder, not the consumer.

## Core Model

### The Defining Core

Four structures, held jointly. Each alone is a different kind of software; together they are the RAG Development Platform.

**1. The knowledge corpus as a managed unit of record.** The platform holds external documents and data as a persistent, addressable body of knowledge: sources are brought in (uploaded or pulled through connectors), processed into retrievable units, and kept — with provenance back to their original documents — as the corpus the application will answer from. The corpus is a living record: sources can be added, updated, and removed, and the retrievable form follows. Products name this unit differently (index, collection, corpus, knowledge base, context); the structure is the same. Without it, there is nothing of the organization's own knowledge in the system — just a model API.

**2. The retrieval stage.** At query time, the platform selects the corpus units relevant to the query. This is genuine machinery, not a lookup: mature platforms rank by meaning and by terms, apply metadata filters, and re-score candidates. The implementation varies — vector similarity, keyword search, or a hybrid of both — but the stage itself is invariant: some mechanism must decide, per query, which parts of the corpus matter. Without it, an LLM sees either nothing or everything, and neither is grounded retrieval.

**3. The generation binding.** The platform composes the retrieved units and the user's query into a prompt for an LLM and returns the model's response as the application's answer. The answer is produced *from* the retrieval: mature platforms make the linkage explicit by carrying source references (citations) from the retrieved units into the generated answer. Without this binding — if the platform stops at ranked results — the product is a search or retrieval platform; if it composes prompts without a corpus, it is plain LLM application machinery.

**4. The developer build surface.** The corpus, retrieval, and generation loop is exposed as construction material: APIs and SDKs to call from application code, configuration for ingestion and retrieval behavior, consoles to manage corpora and inspect queries, and hooks (evaluation, tracing) to operate the result. The platform's user is the builder; the loop is a component of the builder's application, not a finished consumer product.

### Standard Capabilities of Mature Products

These appear across the researched sample and make the loop practical, but they are implementations and extensions, not the definition:

- **Chunking and parsing** — splitting source documents into retrievable units (platform-managed, developer-defined, or configurable per pipeline).
- **Embedding management** — vector representations of units and queries, with platform-provided or third-party embedding models, sometimes several per corpus.
- **Hybrid search and filtering** — combining meaning-based and term-based retrieval, narrowed by metadata filters before generation.
- **Reranking** — re-scoring retrieved candidates for relevance before they reach the prompt.
- **Connectors** — scheduled pulls from enterprise sources (object storage, wikis, drives, ticketing, web crawls).
- **Citations and grounding enforcement** — every answer carrying references to the documents it drew from; some products additionally grade answers for factual consistency with the retrieved material.
- **Evaluation tooling** — scoring answers for correctness and completeness against expected results.
- **Tracing and observability** — recording what was retrieved, what was sent to the model, token usage, latency, and cost, per query.
- **Multi-turn sessions** — conversation state so follow-up questions resolve against prior turns.
- **Retrieval-time access control** — filtering which units a given user's query may reach, enforced at retrieval rather than only at the application layer.
- **Agent integration surfaces** — exposing the corpus and the query loop as tools that AI agents can call.

### One Structure, Many Implementations

The core is written conceptually; implementations vary along stable axes:

```text
Concept:   Knowledge corpus of record
Names:     index, collection, corpus, knowledge base, context

Concept:   Retrievable unit
Forms:     embedding-backed chunks, developer-defined objects,
           distilled artifacts; unit granularity is a configuration, not a constant

Concept:   Retrieval stage
Forms:     vector similarity, keyword (BM25), hybrid of both,
           plus filters and reranking at varying depths

Concept:   Generation binding
Forms:     platform-hosted LLM, bring-your-own endpoint,
           per-call model selection; citation handling from explicit
           citation objects to retrieved-records-as-references

Concept:   Developer build surface
Forms:     REST APIs + SDKs, declarative query languages,
           managed consoles, infrastructure-level pipelines the
           developer runs themselves
```

A reader who has only seen one implementation — say, a managed "upload your PDFs and chat" API — should still be able to recognize a self-hosted database with built-in generative modules, or a cloud-vendor pipeline the developer assembles themselves, as the same Application Type.

## How It Works

The platform runs two loops, plus the builder's own iteration loop around them.

### The ingestion loop (documents → retrievable knowledge)

```text
Connect a source (upload, connector, or pipeline)
→ extract content from documents
→ split into retrievable units (chunking or equivalent)
→ compute representations (embeddings / index structures)
→ write to the corpus, keeping the mapping to the original source
→ repeat as sources change (incremental updates, scheduled pipelines)
```

In managed products this loop is largely operated for the developer — "upload documents; the platform manages chunking, embedding, and storage." In infrastructure-first and customer-managed products, the developer configures or operates each step themselves. Either way, the corpus ends up holding retrievable units bound to their sources, and a corpus that has not been built out from its sources is explicitly not yet queryable in products that separate staging from curation.

### The query loop (query → grounded answer)

```text
Application sends a query (and, for chat, conversation state)
→ platform processes the query (embedding / term matching / decomposition)
→ retrieves candidate units from the corpus
  (hybrid search, metadata filters, reranking)
→ composes the prompt: query + retrieved units (+ instructions)
→ calls the LLM (platform-hosted or developer-supplied)
→ returns the generated answer with references to its sources
→ records the trace (retrieved units, prompt, usage, latency, cost)
```

This is the loop the platform exists to run. Its visible outputs are the grounded answer and its citations; its invisible outputs are the traces that make the answer auditable.

### The builder's loop (build → evaluate → tune)

```text
Configure ingestion and retrieval for the target use case
→ run real (or golden) queries against the corpus
→ inspect answers, citations, and traces
→ evaluate correctness / completeness / grounding
→ adjust: chunking, retrieval strategy, filters, rerankers,
  instructions, model choice
→ redeploy and monitor in production
```

Mature platforms treat evaluation as part of the product rather than an afterthought: answer metrics scored against expected answers, grading of whether an answer is consistent with the material it cites, and observability views for triaging regressions.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Management console

The builder's control surface.

- lists corpora (and their ingestion state), connectors, and deployments
- typical information: source health, document/unit counts, query volume, cost
- primary actions: connect sources, trigger ingestion/curation, create and delete corpora, inspect configuration

### Ingestion / data source views

Where sources become corpus content.

- connected sources, import and pipeline status, per-source file trees
- primary actions: upload files, link a connector, run or schedule a pipeline, review processing errors

### Query playground / interactive query

Where the builder exercises the loop directly.

- a query input against a chosen corpus; the generated answer with inline citations; the retrieved units behind the answer
- primary actions: run a query, inspect retrieved passages and scores, iterate on instructions or retrieval settings

### APIs and SDKs

The primary integration point — the loop called from the developer's own application code.

- endpoints for corpus management, ingestion, and query/generation
- SDKs in common languages; some products add a declarative query language or MCP surfaces so agents can call the corpus as a tool

### Evaluation and observability views

Where answer quality is judged and regressions are triaged.

- evaluation runs and metrics (correctness, completeness, grounding scores), per-query traces with retrieved units and model calls, usage and cost rollups
- primary actions: run an evaluation set, replay a trace, adjust thresholds or configuration

## Important Rules / Behaviors

### The grounding contract

The platform's core promise is that answers come from the corpus. Mature products enforce this visibly — citations attached to generated answers, references resolvable to original documents — and some additionally grade the answer against the retrieved material before it is trusted. Where the corpus cannot support an answer, some products offer a decline-or-answer policy rather than letting the model improvise.

### Corpus state gates querying

A corpus built from sources is not instantly queryable everywhere: products that separate ingestion from curation require the build step to complete first, and updating sources requires re-processing before the changes are retrievable. Ingestion and retrieval are asynchronous by nature.

### Retrieval-time access control

Because one corpus often serves many users, access rules are enforced where retrieval happens: a query issued under a given identity reaches only the units that identity is entitled to see. This is a structural rule in enterprise-oriented products, not a UI feature.

### Model coupling is a configuration, not an identity

The LLM that performs generation is typically swappable — hosted models chosen per call or per configuration, or a developer-supplied endpoint called by the platform like any hosted model. The corpus, the retrieval machinery, and the citation structure persist across model changes; the platform's value does not depend on one specific model.

### Provenance survives processing

Units in the corpus carry their origin: which document, where in the document, under what metadata. Every downstream behavior — citations, permission filtering, source updates and deletions — depends on this mapping holding.

## Variants

Common shapes of the same Type:

- **Managed full-stack RAG API** — upload documents, get a grounded-answer endpoint; the platform runs the entire loop (managed assistants, RAG-as-a-service).
- **Retrieval-infrastructure-first** — a vector database or search engine the developer builds around; RAG appears as built-in generative modules or as code the developer writes on top.
- **Cloud-vendor pipeline** — RAG machinery embedded in a broader AI platform, offered both fully managed and as a customer-operated pipeline over the vendor's storage and search infrastructure.
- **Self-hosted open-source** — the same corpus/retrieval/generation structures deployed in the developer's own environment, from local evaluation to Kubernetes clusters.
- **Private / regulated deployment** — VPC, on-premises, or air-gapped operation for compliance-bound customers; the loop is unchanged, the trust boundary moves.
- **Agentic extension** — the loop exposed to AI agents as a callable tool, with agentic retrieval (query decomposition, multi-hop retrieval across corpora) as an increasingly common retrieval mode.

A variant stays a variant while the four core structures hold. When a product drops the build surface and ships a finished chat product to end users, it has crossed into the Enterprise Knowledge Assistant Type; when it drops the corpus and generalizes to arbitrary LLM application construction, it has crossed into the LLM Application Development Platform Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Vector Retrieval Platform / Vector Database | upstream sibling | holds embeddings and serves similarity search; no generation binding — ranked results, not grounded answers. Vector databases frequently add a RAG layer on top, which is precisely the seam between the Types |
| Search Platform / Semantic Search Platform | adjacent | terminal object is a ranked result list consumed by an application; no LLM generation step |
| LLM Application Development Platform | broader | builds LLM applications of any shape (agents, workflows, extraction); RAG is one pattern. Frameworks and libraries live here — code to assemble a pipeline, with no hosted corpus of record |
| Enterprise Knowledge Assistant | downstream product | the finished end-user application (chat over company knowledge) that developers build on a RAG platform; no build surface for other applications |
| AI Gateway / Model Routing Platform | adjacent | model access, routing, and metering; no corpus, no retrieval, no grounding |
| Knowledge Graph Platform | adjacent | organizes knowledge as entities and relations rather than retrievable passages; some RAG products borrow graph structures internally without becoming this Type |
| LLM Evaluation Platform | complementary | evaluates LLM applications generally; RAG platforms embed evaluation scoped to their own retrieve-then-generate loop |
| LLM Observability Platform | complementary | general tracing/monitoring for LLM apps; RAG platforms ship loop-specific tracing (retrieval, prompts, citations) built in |

The two most consequential seams: **generation binding** separates this Type from retrieval-only infrastructure, and **corpus of record + build surface** separates it both from stateless LLM tooling below and from finished assistant products above.

## Representative Products

- **Pinecone** — managed vector database with managed RAG surfaces on top (an assistant API where the platform manages chunking, embedding, and storage; a "knowledge engine" that compiles sources into curated, queryable knowledge with grounded, cited answers).
- **Weaviate** — open-source AI vector database with RAG built in as generative search (a RAG query = search query + prompt; the database retrieves, then passes results and prompt to a configurable generative model), deployable self-hosted or as managed cloud.
- **Vectara** — API-first grounded-generation platform: managed corpora, a multi-stage retrieval engine (chunking → embeddings → hybrid search → reranking → citations), an LLM gateway with bring-your-own-model support, and answer-level hallucination grading.
- **Amazon Bedrock Knowledge Bases** — cloud-vendor RAG pipeline inside a broader AI platform: managed knowledge bases (connectors, managed parsing/indexing/retrieval, agentic retrieval) alongside customer-managed knowledge bases over the developer's own vector stores.

The Type was additionally checked against the framework pole (LlamaIndex — RAG pipeline components as a code library with no hosted corpus of record) to sharpen the boundary with LLM Application Development Platforms; it is recorded as a neighboring Type, not a variant of this one.

## Sources

Research date: **2026-09-09**. All sources are official product documentation, fetched directly.

- Pinecone — Documentation home & index: https://docs.pinecone.io/ ; Nexus key concepts: https://docs.pinecone.io/guides/nexus/concepts ; Assistant overview: https://docs.pinecone.io/guides/assistant/overview
- Weaviate — Database introduction: https://weaviate.io/developers/weaviate ; Retrieval Augmented Generation (generative search): https://weaviate.io/developers/weaviate/search/generative
- Vectara — About: https://docs.vectara.com/docs ; The platform stack: https://docs.vectara.com/docs/platform-architecture/platform-stack
- AWS — Amazon Bedrock Knowledge Bases: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html ; How knowledge bases work: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-it-works.html
- LlamaIndex (boundary check) — Building an LLM application: https://docs.llamaindex.ai/en/stable/understanding/

> Sourcing note: all quoted behaviors above come from the fetched official documentation of the sampled products as of the research date. Vendor positioning shifts quickly in this category (several sampled vendors now lead with "agents" branding); precise plan-, limit-, and model-catalog details were deliberately left to the vendor pages and the paired Research Notes rather than asserted here.

Detailed evidence, per-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
