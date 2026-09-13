# Feature Store

## Overview

A **Feature Store** is the data-management layer that treats machine-learning features — the named input values models learn from — as managed, shared assets. It registers their definitions in a catalog, stores their values as records keyed by the object they describe and versioned by the time they describe, and retrieves them for the two contexts models need: **training datasets** assembled with point-in-time correctness, and **feature lookup** at scoring time.

The defining core is small:

```text
Feature (named, typed model input bound to an entity)
└── Feature registry / catalog of record
    └── Entity-keyed, event-time-versioned feature values (historical store)
        ├── Training leg: point-in-time-correct training-dataset assembly
        └── Scoring leg: feature-vector retrieval for model scoring
            (real-time form served by a low-latency online store)
```

The problems it exists to solve are the ones teams hit when features are produced ad hoc in notebook code: the same inputs re-implemented differently per model, training data that silently leaks information the model will not have at prediction time (training–serving skew), and no operational way to get fresh feature values to running models. Mature products add discovery/sharing, materialization machinery, statistics and monitoring, and governance — these are standard capabilities, not what makes a feature store.

A feature store is not a general data platform. It is a downstream layer that typically re-uses existing warehouse/lakehouse/operational storage, and products in this space are explicit about what they are not: not an ETL system, not a workflow orchestrator, not a data warehouse, not a database.

## Users & Context

- **Data scientists** — define features for their models, discover and reuse features defined by others, and generate training datasets from registered features.
- **ML engineers** — productionize the feature layer: wire sources, run or schedule materialization, integrate feature retrieval into inference services, manage freshness and versions.
- **Data engineers** — own the upstream pipelines whose outputs feed feature containers; in products without managed computation, they effectively author the feature pipelines.
- **Platform administrators** — govern access, sharing across teams/projects, tags, lineage, and audit.

The context is an organization building and operating ML models — recommendations, fraud and risk scoring, churn prediction, credit scoring, forecasting, personalization. Usage splits into batch work (large training sets, scheduled batch scoring) and real-time work (low-latency feature lookup inside live prediction services). The primary working surfaces are code (SDKs, CLIs) plus a catalog UI; this is a developer-facing data system, not an end-user product.

## Core Model

### The defining core

**Feature.** A named, typed model input — a measurable property of some real-world object: an attribute (a user's location), or more often a computed value such as an aggregate over a time window (transactions in the last 30 days, average account balance). A feature carries its name, data type, the entity it describes, and its source.

**Entity.** The real-world object features describe — a user, driver, item, card, merchant. Entities are identified by join keys; every feature value is meaningful only in reference to an entity, and retrieval is keyed by entity. Entity-keying is what makes features combinable across tables and models.

**Feature registry / catalog of record.** Features are registered as managed records, grouped into named containers — *feature views* or *feature groups*, depending on the product — each binding a set of features to its entities, schema, data source, and event-time field. The registry persists across users, services, and models; it is the shared source of truth that makes a feature reusable instead of re-implemented. Mature products expose the registry through search/browse UI, tags, descriptions, and lineage.

**Stored feature values.** The values themselves are held as records keyed by entity and versioned by **event time** (the time the value describes), distinct from ingestion time. The historical store retains this history — it is the raw material for training and batch scoring.

**Retrieval for model contexts.** The same registered features are retrieved in two modes:

- **Historical retrieval** — joins feature values onto a set of labeled entity rows *as of each row's event time*, reproducing the state of the world at the moment each training example occurred. This point-in-time correctness is the semantic that keeps future or unavailable values from leaking into training data.
- **Scoring retrieval** — returns the feature vector for one or more entities so a model can score. In real-time serving this is a low-latency lookup of the latest values from an **online store** (the standard modern component); in batch scoring it is a large retrieval from the historical store. Products commonly bundle a model's required features into one retrievable unit (a feature service, or the model's feature view) so the model does not bind to individual feature containers.

### Where the values come from — the variable part

How feature values are produced varies by product philosophy and is deliberately not part of the core:

- **Ingest-only** — the store receives already-computed records (push/stream/batch writes); computation lives upstream.
- **Managed computation** — the product builds and runs feature pipelines from declared logic (declarative feature views with aggregations, streaming features).
- **Bring-your-own** — feature pipelines run externally (Spark, Flink, SQL, dbt-style), and the store registers and stores their outputs; some products keep even the historical data in the external lakehouse ("external" feature containers).

### Concept vs implementation

```text
Concept:   named feature container registered in a catalog
Forms:     feature view (Feast/Tecton/Databricks), feature group (Hopsworks/SageMaker)

Concept:   entity the feature describes
Forms:     entity + join keys, primary/serving keys, record identifier

Concept:   scoring retrieval
Forms:     online-store lookup via SDK/HTTP endpoint, client-side joins across
           containers, automatic lookup wired into model-serving endpoints
```

## How It Works

### 1. Define and register

```text
Declare features (name, type, entity, source, event-time field)
→ group them into a feature view / feature group
→ register in the feature store's catalog
→ discoverable by other teams and models
```

Definitions live as code or catalog objects and persist independently of any one model.

### 2. Load feature values

```text
Backfill historical values from the source
→ schedule or trigger materialization (batch → historical and/or online store)
→ keep values fresh (streaming ingestion or pushed record updates)
```

In ingest-only products this step is simply writing records; in pipeline-managed products the store computes the features from declared logic. The historical store accumulates the full event-time-versioned history; the online store (when enabled) holds the latest value per entity.

### 3. Generate a training dataset

```text
Collect labeled entity rows (entity keys + the event time of each label)
→ the store joins registered features onto those rows
   as of each row's event time, within freshness windows
→ result: a training dataset whose features reflect
   only what was knowable at each moment
```

Rows older than available feature history, or outside the permitted staleness window, come back without feature values rather than with leaked ones.

### 4. Retrieve features for scoring

```text
At inference time, look up the feature vector for the request's entity key(s)
→ online store returns the latest values (low latency)
→ the model scores
```

In batch scoring, the same retrieval runs over large entity sets from the historical store. The feature definitions serving inference are the ones the model trained on — the consistency between the two legs is the point of the Type.

### 5. Operate

```text
Monitor freshness, statistics, and drift of feature values
→ manage schema evolution, versions, deprecation
→ share containers across teams/projects; control access; trace lineage to models
```

### Capability tiers

**Defining core** — feature registry of record; entity-keyed, event-time-versioned historical store; point-in-time-correct training retrieval; feature-vector retrieval for scoring.

**Standard capabilities in mature products** — online store for low-latency serving (per-feature-container optionality); materialization/backfill/streaming machinery; discovery, search, sharing and reuse; serving bundles (feature services); time-window aggregations and declared transformations; freshness windows (TTL); statistics; SDKs plus HTTP feature servers and a catalog UI.

**Optional / variant** — data validation and feature-quality/drift monitoring; on-demand (request-time) computation; governance depth (access control, lineage to models, mandatory tags, audit); external feature containers backed by external lakehouses; embeddings as feature values; multi-project tenancy and environment separation.

## Interfaces

### SDK / API (primary surface)

The main way features are defined and consumed. A Python SDK is the norm for definition, historical retrieval, and online lookup; some products add Java/Go clients and HTTP feature servers so non-Python services can fetch feature vectors.

### CLI

Definition deployment and registry inspection (plan/apply-style commands, listing and describing feature containers) in library-form products.

### Catalog UI

Search/browse over registered feature containers: names, owners, descriptions, tags, schemas, statistics, materialization status, lineage to sources and models. This is the discovery-and-reuse surface — the registry made visible to a team rather than to one notebook.

### Retrieval endpoints

The model-facing surface: online lookup endpoints (by entity key(s), returning the feature vector) and training-dataset queries (labeled entity rows in, training dataset out). In suite products, model-serving endpoints can perform the lookup automatically so inference code never touches the store directly.

## Important Rules / Behaviors

- **Point-in-time correctness governs training retrieval.** The historical join reproduces feature state as of each labeled row's event time. Values that entered the store after that moment do not appear in that row (products differ in how strictly ingestion-time availability is enforced — some offer an explicit availability filter).
- **Freshness is bounded by declared windows.** A feature value carries an event time, and retrieval within a maximum staleness window means rows older than available data return empty rather than stale-beyond-limit values.
- **Online stores hold the latest value.** Real-time lookup returns the most recent value per entity; the historical accumulation is kept separately from it. Updates arrive by materialization, streaming, or pushed writes (retention and update mechanics vary by product).
- **Retrieval is entity-keyed.** Features are fetched by join key(s); there is nothing to return for an entity with no stored values. Combining features across containers is the retrieval layer's join work, not the model's.
- **Definitions are shared contracts, not code inside one model.** Registered features persist beyond any model's lifecycle; products provide versioning, schema evolution, and deprecation paths rather than silent edits (mechanics vary by product).
- **Transformations, where the product manages them, apply identically in both contexts.** Consistency between training-time and inference-time computation is a stated goal of transformation features; in ingest-only products, consistency is the data engineer's responsibility upstream.
- **Governance wraps the registry.** Access control, tags, and lineage from features to models are the mature layer; depth varies from light metadata to lakehouse-integrated governance.

## Variants

- **Open-source library + own infrastructure** — definitions as code, storage and compute brought from existing infrastructure (warehouse, KV store, stream processor); the minimal, composable pole.
- **Managed feature platform** — the vendor operates computation, stores, and serving; feature pipelines declared and run as a service; monitoring and drift tooling built in.
- **Cloud-suite module** — a named feature-store service inside a hyperscaler ML suite, tightly integrated with that suite's ingestion, notebooks, and model hosting.
- **Lakehouse-embedded** — features realized as governed tables in the lakehouse catalog, with registry, point-in-time joins, lineage, and serving layered on the platform's governance substrate.
- **Full ML platform with feature store at the center** — feature store sold alongside model registry, serving, and monitoring as one platform.
- **Offline-only deployments** — training and batch scoring without an online store; satisfies the core for batch-model estates.
- **Embedding-era extensions** — embeddings stored and served as feature values, and retrieval-augmented-generation applications consuming feature/serving endpoints; an active drift zone, not a separate core.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Machine Learning Platform | broader; frequent embedder | spans the model lifecycle (training, deployment, monitoring); the feature store is its feature-data layer — suite products ship this Type as a named module inside it |
| Model Registry | sibling registry | object of record is the model artifact and its versions, not feature definitions and values; lineage connects them without merging them |
| MLOps Platform | consumer machinery | automates lifecycle workflows (pipelines, CI/CD, deployment); the feature store is a data layer those workflows consume, not an orchestrator itself |
| Data Warehouse / Lakehouse Platform | substrate | organization-wide data of record; the feature store re-uses its storage and adds entity/event-time semantics, the feature registry, and ML retrieval semantics |
| Data Catalog | adjacent metadata layer | discovery lens over all data assets; holds metadata, not feature values, and serves analysts rather than models |
| Data Science Workbench | consumer surface | interactive code sessions in which data scientists author and consume features; the workbench is the session, the feature store is the managed data layer behind it |
| Customer Data Platform | shape-similar, different semantics | entity-keyed profiles for marketing activation; no event-time-versioned training retrieval, no point-in-time joins, no model-scoring contract |
| Vector Retrieval Platform | adjacent retrieval Type | similarity search over embeddings vs key-based feature lookup; embeddings can be stored as feature values without the Types merging |

The closest seam is with the Machine Learning Platform: the market realizes feature stores mostly *inside* ML suites and lakehouse platforms. The separation is structural — strip the feature-data layer (registry, entity/time-versioned values, ML retrieval) and a lifecycle platform remains; strip training/deployment/monitoring machinery and a feature store remains.

## Representative Products

- Feast — open-source feature store (bring-your-own infrastructure)
- Tecton — managed feature platform for real-time ML
- Hopsworks — open-source feature store / ML platform with its own storage engine
- Amazon SageMaker Feature Store — feature store service in a cloud ML suite
- Databricks Feature Store (Feature Engineering in Unity Catalog) — lakehouse-embedded feature registry

The core model was checked across all five to avoid over-fitting to any one packaging pattern (managed pipelines vs ingest-only vs library-form), and the definition was tested against minimal and pre-name-era implementations (offline-only deployments; shared feature registry + point-in-time training-dataset tooling without online serving) to keep the core era-neutral.

## Sources

Research date: **2026-09-08**

- Feast — Introduction, Concepts, Point-in-time joins — https://docs.feast.dev/ , https://docs.feast.dev/getting-started/concepts/overview , https://docs.feast.dev/getting-started/concepts/point-in-time-joins
- Tecton — Introduction — https://docs.tecton.ai/docs/introduction
- Hopsworks — Documentation home; Feature View overview — https://docs.hopsworks.ai/latest/ , https://docs.hopsworks.ai/latest/concepts/fs/feature_view/fv_overview/
- Amazon SageMaker AI — Feature Store developer guide — https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html
- Databricks — Feature Store documentation — https://docs.databricks.com/aws/en/machine-learning/feature-store/index.html

> Sourcing limitations: all evidence is from official product documentation fetched on 2026-09-08. Google Vertex AI Feature Store and several open-source entrants were not sampled (five-product cap). Vendor performance figures were treated as marketing claims and excluded. One sampled product's point-in-time terminology was verified for four of five products directly and inferred for the fifth from its training-data documentation.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
