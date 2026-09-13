# Research Notes — Feature Store

## Research Goal

Understand what a Feature Store actually is as an Application Type: the objects it manages, the workflows it supports (definition → storage → training retrieval → serving retrieval → operation), how products differ, and where its boundaries sit against neighboring data/ML Types. Produce the evidence basis for a vendor-neutral Application Document.

## Initial Boundary

Working hypothesis at start:

- A Feature Store is the data layer of ML systems: it manages *features* (named model inputs) as shared, reusable assets — cataloging their definitions, persisting their values keyed by entity over time, and retrieving them consistently for model training and model inference.
- Likely users: data scientists, ML engineers, data engineers, platform teams.
- Nearest neighbor Types in the directory (§13 Data, Analytics & AI Systems and adjacent):
  - Machine Learning Platform (broader lifecycle — could absorb this as a module)
  - Model Registry (registry of models, not features)
  - MLOps Platform (lifecycle automation)
  - Data Warehouse / Data Lake / Lakehouse Platform (general data of record)
  - Data Catalog (processed 2026-09-07 — metadata lens over all data assets)
  - Data Science Workbench (processed 2026-09-07 — interactive sessions; that pass pre-hung a cross-check request against this leaf)
  - Vector Retrieval Platform / Vector Database Console (embeddings)
  - Customer Data Platform (§06 — entity-keyed profiles for marketing)
- Known straddle risk: cloud ML suites (SageMaker, Vertex AI) and lakehouse platforms (Databricks) embed feature stores as modules rather than selling them standalone.

## Research Questions

1. What is a "feature" in these systems, and what objects exist around it (entity, feature view/group, data source, feature service)?
2. How are features defined and registered? What does the registry/catalog hold?
3. How do feature values get into the system (ingest, materialization, streaming/push, managed computation)? Is computation part of the Type?
4. What are the offline/historical and online stores, and is the online store definitional or optional?
5. How does training-data retrieval work? What is point-in-time correctness and is it universal?
6. How does serving retrieval work (online lookup, feature vectors, serving endpoints)?
7. What surrounds the core: discovery/sharing, quality/statistics, monitoring, governance, lineage?
8. What product philosophies exist (open-source library vs managed platform vs suite module; ingest-only vs pipeline-managed)?
9. What are the boundaries against neighboring Types, and what removal tests separate them?

## Representative Products

Selected for market representativeness, documentation quality, and spread of product philosophy / customer tier:

| Product | Form | Why sampled |
|---|---|---|
| **Feast** | open-source feature store (BYO storage/compute) | De-facto open-source standard; minimal philosophy; explicitly documents what it is NOT |
| **Tecton** | commercial managed feature platform | Pure-play category leader born from Uber's ML platform; managed-pipeline philosophy |
| **Hopsworks** | open-source platform (own storage engine) + commercial cloud | Feature store with in-platform storage (RonDB) and its own governance model; standalone-FS or full-MLOps packaging |
| **Amazon SageMaker Feature Store** | cloud-suite module | Hyperscaler ML suite embedding; ingest-centric (no managed feature computation) — important counter-shape to Tecton |
| **Databricks Feature Store** (Feature Engineering in Unity Catalog) | lakehouse-embedded module | Features realized as governed lakehouse tables; strongest governance/lineage integration; shows the warehouse-adjacent pole |

## Sources

Research date: **2026-09-08**. All Tier-1 (official product documentation), fetched live.

- Feast — Introduction: https://docs.feast.dev/ ; Concepts overview: https://docs.feast.dev/getting-started/concepts/overview ; Point-in-time joins: https://docs.feast.dev/getting-started/concepts/point-in-time-joins
- Tecton — Introduction: https://docs.tecton.ai/docs/introduction (docs root + doc nav also reviewed)
- Hopsworks — Documentation home: https://docs.hopsworks.ai/latest/ ; Feature View overview: https://docs.hopsworks.ai/latest/concepts/fs/feature_view/fv_overview/
- Amazon SageMaker — Feature Store developer guide: https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html
- Databricks — Feature Store docs: https://docs.databricks.com/aws/en/machine-learning/feature-store/index.html

Not sampled (coverage note): Google Vertex AI Feature Store, Firebase-managed feature store, chunked/rising open-source alternatives (e.g. Chronon, Feathr) — five-product cap; the GCP pole is under-represented. No vendor claims below draw on those products.

## Product Observations

Evidence layer marking: **[A]** = directly observed in this product's official docs; **[B]** = recurring across multiple sampled products (noted in cross-product section).

### Feast (docs.feast.dev)

- [A] Self-definition: "an open-source feature store that helps teams operate production ML systems at scale by allowing them to define, manage, validate, and serve features for production AI/ML."
- [A] Composition: "two foundational components: (1) an offline store for historical feature extraction used in model training and (2) an online store for serving features at low-latency in production systems and applications."
- [A] Explicit non-goals: "not an ETL/ELT system", "not a data orchestration tool", "not a data warehouse", "not a database" — instead "a lightweight downstream layer that can serve data from an existing data warehouse … to models in production", re-using existing infrastructure.
- [A] Concept model: Project → Feature Views → Features; features relate to Entities; every feature view has a Data Source; training datasets generated from sources; features "stored in a registry, which can be accessed across users and services"; retrieval via Python SDK or a deployed feature server (HTTP); UI (alpha) and CLI for exploring/updating feature information.
- [A] Retrieval pattern table: training data generation (`get_historical_features`), offline retrieval for batch predictions (same API), online retrieval for real-time predictions (`get_online_features`).
- [A] Point-in-time joins: "Feature values in Feast are modeled as time-series records"; historical retrieval joins feature views onto an "entity dataframe" "in a point-in-time correct way … able to reproduce the state of features at a specific point in the past"; scanning backward from each entity-row timestamp bounded by a TTL; explicit anti-leakage framing ("Avoid data leakage by generating point-in-time correct feature sets … ensures that future feature values do not leak to models during training").
- [A] Availability-time subtlety: by default only the feature's event timestamp constrains the join; an optional `filter_by_created_timestamp` flag restricts to values already available at each entity timestamp ("useful to keep backfilled values from leaking into training data").
- [A] Ingestion: offline batch use cases can query existing data without ingestion; online use cases use materialization (batch→online) and push (streaming features pushed to offline/online). Push-model serving architecture.
- [A] Scope note: "Feast today primarily addresses *timestamped structured data*."
- [A] Surrounding machinery: feature quality monitoring (null rates, distributions, drift across batch data and serving logs); permissions concept; tags; partial lineage via third-party catalogs (DataHub/Amundsen plugins).

### Tecton (docs.tecton.ai)

- [A] Self-definition: "The feature store for real-time machine learning at scale"; positions itself as "the feature layer of your ML stack" with three jobs: transform raw data into features/embeddings, serve features quickly and reliably for real-time predictions, "guarantee consistency between training and serving."
- [A] Category definition given by the vendor: "A **feature** is a measurable property or characteristic of a phenomenon being observed… the inputs that models use to learn patterns from data and to make inferences"; "A **feature store** is infrastructure which configures, deploys and manages **data pipelines** that transform data into features and serve those features to ML models."
- [A] Concept model: **feature view** "defines a set of features that will be computed and stored" (batch / stream / real-time feature views; per-view flags `online=True, offline=True`); **feature service** "collects feature views together and provides an API endpoint that models can use to access individual features" so "models don't need to know which feature views implement the features they require."
- [A] Two consumption modes: "offline, typically when a large dataset is created at a specific point in time in order to train that model; and online, in an ongoing process where a set of features about a specific entity is provided to a model for it to make an inference."
- [A] Training-side guarantees: "Generate historically accurate training data sets"; "automatically handles point-in-time correct backfills"; "eliminating the common problem of training-serving skew."
- [A] Time-window aggregations as a first-class capability ("average transaction amount over the last 7 days" at scale); real-time/streaming computation with "write feature logic once and Tecton executes it consistently both in real-time for predictions and offline for training."
- [A] Product surfaces: Web App UI; documented lifecycle: define → deploy → read (training/inference) → test → change → materialize → share → publish; monitoring & alerting; drift detection; cost management; admin/security sections.
- [A] Marketing-grade performance claims (<5 ms at 100K req/s) — treated as vendor claims, not canonical facts.

### Hopsworks (docs.hopsworks.ai)

- [A] Self-definition: "a data platform for ML with a Python-centric Feature Store and MLOps capabilities… modular platform. You can use it as a standalone Feature Store" or for full model governance/serving.
- [A] Concept model: **feature groups** (the write API — where feature pipelines write data; stored as Hudi tables on object storage, or as **external feature groups** where offline data stays in an external lakehouse: Snowflake, Databricks, Redshift, BigQuery, JDBC); **feature views** (the read API — "a logical view over (or interface to) a set of features that may come from different feature groups", created by joining features across feature groups).
- [A] Feature view semantics (fetched page): features inherit type, primary key and **event_time** from feature groups; a feature view can include the label for the supervised problem, transformation functions "applied to specified features consistently between training and serving", the ability to create training data, and the ability to "retrieve a feature vector with the most recent feature values"; "the feature view is a representation for a model in the feature store"; feature views enable reuse of features across models (and untransformed storage in groups makes features more reusable).
- [A] Online serving by a dedicated engine (RonDB) positioned as the low-latency store; online and offline APIs are distinct surfaces.
- [A] Surrounding machinery in-doc: statistics, data validation (Great Expectations integration), feature monitoring, versioning, deprecation, TTL, tags/mandatory tags, provenance & lineage, search, project-based multi-tenancy with sharing across projects; embeddings + vector similarity search shipped as a sibling capability (OpenSearch-based); FTI (feature/training/inference) pipeline architecture with Airflow orchestration.

### Amazon SageMaker Feature Store (docs.aws.amazon.com)

- [A] Self-definition: "simplifies how you create, store, share, and manage features… by providing feature store options and reducing repetitive data processing and curation work"; explicitly framed against training-serving skew ("a common issue in ML where the difference between performance during training and serving can impact the accuracy of your ML model").
- [A] Concept model: features stored in **feature groups** ("visualize a feature group as a table in which each column is a feature, with a unique identifier for each row"); a **Record** is the values for one **RecordIdentifier**; feature-group metadata includes description, storage configuration, record identifier, **event time**, tags.
- [A] Store topology is per-feature-group configuration: groups "can be configured to include an online or offline store, or both". Online store "retains only the latest records… designed for supporting real-time predictions that need low millisecond latency reads and high throughput writes"; offline store "keeps all records… as a historical database… intended for data exploration, model training, and batch predictions" (append-only, event-time-prefix scheme, Parquet, queryable via Athena).
- [A] Ingestion: streaming (synchronous `PutRecord` — "streaming features") or batch (e.g. Processing jobs; Data Wrangler export). No managed feature-computation engine — the product ingests and stores; transformation happens upstream.
- [A] Retrieval: online mode for low-latency/high-throughput prediction; offline mode for training and batch inference with the ability to "extract data at different points in time"; joins across feature groups performed by the client application at inference time.
- [A] Discovery/share: "other authorized users… can share and discover it"; browse/search by feature-group name, description, record identifier, creation date, tags.

### Databricks Feature Store / Feature Engineering (docs.databricks.com)

- [A] Self-definition: "a central registry for the features used in your AI and ML models. When you register features and models in Unity Catalog, you get built-in governance, lineage, point-in-time joins, and cross-workspace feature sharing and discovery."
- [A] Two authoring strategies: **Feature Views** ("define features declaratively and let Databricks compute and manage the feature pipelines for you"; time-windowed aggregations; streaming feature views with sub-second freshness; public preview) vs **feature tables** ("you populate yourself by writing feature values to a Delta table" with a primary key — you own the pipeline). Both publish to the **Online Feature Store**.
- [A] Training side: "point-in-time correctness to create a training dataset that reflects feature values as of the time a label observation was recorded"; when models are trained on registered features, "the model automatically tracks lineage to the features that were used in training."
- [A] Serving side: Online Feature Store ("serve feature data to online applications and real-time machine learning models"); Model Serving with "automatic feature lookup" ("at inference time, the model automatically looks up the latest feature values"); standalone feature-serving endpoints; on-demand feature computation at inference time; elimination of training/serving skew is a stated goal ("the feature computations used at inference are the same as those used during model training").
- [A] Materialization: feature views are "materialized … for offline training or online serving" — the two destinations are the organizing distinction.
- [A] Governance: Unity Catalog access control over feature tables, lineage of feature table ↔ model ↔ function; tags; catalog explorer / Features UI.
- [A] Naming/packaging note: docs URL and product naming drift ("Feature Store" page; "Feature Engineering Python API"; legacy "Workspace Feature Store (deprecated)"); Feature Views in public preview at research date.

## Cross-product Comparison

| Dimension | Feast | Tecton | Hopsworks | SageMaker FS | Databricks FS |
|---|---|---|---|---|---|
| Feature-definition container | Feature view [A] | Feature view [A] | Feature group (write) + feature view (read) [A] | Feature group [A] | Feature view / feature table [A] |
| Entity semantics | Entity + join keys [A] | Entities [A] | Primary/serving keys [A] | RecordIdentifier [A] | Primary key [A] |
| Event-time versioning | Time-series records, TTL [A] | timestamp_field, window aggregates [A] | event_time inherited [A] | event time field [A] | point-in-time joins [A] |
| Historical/offline store | Yes, core [A] | Yes [A] | Yes (Hudi / external) [A] | Yes (append-only S3/Parquet) [A] | Yes (Delta) [A] |
| Online store | Yes, core component [A]; offline-only use documented [A] | Yes; per-view flag [A] | Yes (RonDB) [A] | Per-feature-group option [A] | Publish target; per-feature choice [A] |
| Point-in-time training retrieval | Explicit, detailed [A] | Explicit [A] | Training-data generation documented; PIT wording not directly fetched [A/B] | "extract data at different points in time" [A] | Explicit "point-in-time correctness" [A] |
| Serving retrieval | get_online_features / feature server [A] | Feature service endpoints [A] | Feature vector retrieval [A] | Online mode for real-time predictions [A] | Automatic feature lookup + serving endpoints [A] |
| Registry/catalog of record | Registry [A] | Feature definitions applied/managed [A] | Catalog + search + sharing [A] | Discoverable feature groups [A] | "Central registry" in Unity Catalog [A] |
| Feature computation | Minimal: on-demand/streaming transforms; explicitly not ETL [A] | Core philosophy: managed pipelines [A] | External/own pipelines; on-demand transforms [A] | None — ingest-only [A] | Managed (Feature Views) or owner-built (feature tables) [A] |
| Sharing/reuse | Cross-user registry access [A] | Share/publish workflows [A] | Cross-project sharing [A] | Authorized discovery/search [A] | Cross-workspace sharing/discovery [A] |
| Quality/monitoring | Feature quality monitoring, drift [A] | Monitoring, alerting, drift [A] | Statistics, validation, feature monitoring [A] | Not prominent in fetched docs | Monitoring (platform-level) [A] |
| Governance/lineage | Permissions, tags; partial via plugins [A] | Access controls, lineage (in-product) [A] | Provenance, projects, governance [A] | Tags; metadata warnings [A] | Unity Catalog governance + model↔feature lineage [A] |
| Embeddings/vector search | AI-engineering framing only | Serves embeddings/prompts as features | Separate vector-DB capability [A] | — | RAG tutorial usage [A] |

Cross-product reading:

- **[B]** Every sampled product organizes features into named, registered containers (feature view / feature group) bound to entities and event time, and exposes two retrieval contexts: historical (training/batch) and online (scoring).
- **[B]** The online store is present in all five as a product component, but is *per-container optional* in every one (Feast offline-only usage; Tecton per-view flag; SageMaker per-group choice; Databricks materialize-to-offline-or-online; Hopsworks per-group online config). It is the standard modern realization, not the definition.
- **[B]** Feature computation ranges from none (SageMaker) through optional transforms (Feast) to the core philosophy (Tecton). The Type does not require a computation engine.
- **[B]** Point-in-time-correct training retrieval is explicit in 4/5 fetched samples with near-identical language (reproduce feature state as of the label's event time; prevent leakage / training-serving skew). Hopsworks' training-data generation was observed; its PIT wording was not directly fetched this pass.

## Canonical Model — Four Abstraction Layers

### L0 — Defining Invariant (deliberately minimal)

A Feature Store is recognizable by exactly three jointly-held structures:

1. **The feature registry of record** — features held as named, individually identified, managed definitions (typed model inputs bound to entities and sources), grouped into registered containers (feature views / feature groups) in a shared catalog that persists across users, models, and time. *Remove → plain tables/databases with no feature-level identity; a data catalog without data.*
2. **Entity-keyed, event-time-versioned feature values in a persisted historical store** — feature values stored as records keyed by the entity they describe and versioned by the event time they describe, retaining history. *Remove → a current-state lookup/cache; no ML history, no training data.*
3. **Model-context retrieval purpose-built for ML workflows** — two retrieval legs off the same registered features: (a) training-dataset assembly that joins feature values onto labeled entity rows **as of each row's event time** (point-in-time correctness — future values must not leak into training data), and (b) feature-vector retrieval that feeds model scoring, in batch (from the historical store) or real-time (from the online store, the standard modern realization). *Remove (a) → an online cache with no training story; remove (b) → a training-dataset utility; remove both → a generic data platform.*

Joint test: 1 alone = a data catalog (or plain schema registry); 2 alone = a versioned table store; 3 without 1+2 = bespoke notebook code; 2+3 without 1 = ad-hoc data prep; 1+3 without 2 = a definition list with nothing to retrieve. All three legs together are what makes the Type.

Note on the online store: deliberately **not** in L0. The scoring leg of (3) exists in both batch and real-time form; the low-latency online store is the standard implementation of the real-time form (see L1), and offline-only deployments satisfy the core (documented at Feast, SageMaker, Databricks).

### L1 — Common Mature Structure

Present in essentially all mature modern products; expected by the market but not definitional:

- **Online store** for low-latency feature serving, with per-feature-container enablement (the standard implementation of the scoring leg)
- **Materialization / ingestion machinery**: backfills, scheduled batch materialization, streaming ingestion, pushed records
- **Discovery, sharing, reuse**: searchable catalog UI over the registry; cross-team / cross-project / cross-workspace sharing of feature containers
- **Serving bundles**: a model's feature set packaged as one retrievable unit (feature services / the model's feature view) so models don't bind to individual feature containers
- **Time-window aggregation features** and declared transformations (managed or on-demand, where the product computes)
- **Freshness controls**: TTL / staleness windows on feature values
- **Statistics** over feature values; feature servers (HTTP) and SDKs (Python-first, some Java/Go) as standard surfaces

### L2 — Variant / Optional Structure

Depends on segment, deployment, security posture, or era:

- Data validation (expectation suites) and feature-quality/drift monitoring programs
- Governance depth: access control models, lineage/provenance to models, mandatory tags, audit — strongest in lakehouse-embedded and platform-suite forms
- On-demand (request-time) feature computation; model-dependent transformations applied consistently across training and inference
- External feature groups (offline values stay in the external lakehouse) vs in-platform storage
- Embeddings as first-class feature values; vector similarity search as an adjacent capability; RAG-oriented retrieval extensions (era-current)
- Deployment form: OSS library + BYO infrastructure vs managed SaaS platform vs suite module
- Project/workspace/tenancy models (multi-tenant sandboxes, dev/staging/prod structuring)

### L3 — Vendor-specific Structure (Research Notes only)

- Feast: projects; entity-dataframe retrieval input; `filter_by_created_timestamp` availability filtering; push-model serving architecture; explicit "what Feast is not" list; alpha Web UI
- Tecton: `FeatureService.online_serving_enabled`; aggregation intervals; interactive tour; vendor performance numbers (<5 ms, 100K req/s — marketing claims); cost-management tooling
- Hopsworks: RonDB online engine; hsfs/hsml Python API split; spine groups; feature logging to Kafka; FTI pipeline architecture; Great Expectations integration
- SageMaker: `PutRecord`/`DeleteRecord` record APIs; AZ-distributed service posture; guidance against PII in feature-group metadata; Data Wrangler authoring integration; Athena/S3 offline access pattern
- Databricks: Unity Catalog as governance substrate; Lakebase-powered online store; automatic feature lookup inside Model Serving; legacy workspace-level Feature Store deprecation path; Feature Views public-preview status

## Rejected Findings

- **"A feature store manages feature pipelines" (Tecton's category definition)** — rejected as definitional: SageMaker Feature Store operates with no managed computation (ingest-only), and Feast explicitly disclaims pipeline management. Held as a product-philosophy variant, not the Type.
- **"The online store defines the Type"** — rejected: per-container optionality observed in all five samples; offline-only deployments satisfy the core.
- **"Features are always computed by the store"** — rejected on the same ingest-only counter-shape.
- **"A feature store is a kind of database/warehouse"** — rejected: Feast's explicit non-goal statement; the Type's identity is the feature-level registry + ML retrieval semantics, whatever storage re-used underneath.
- **"Point-in-time joins are an optional quality feature"** — rejected: the leakage-prevention semantics is the stated reason for the training-retrieval leg in every sample that documents it; without it the system does not produce valid training data.

## Boundary Findings

1. **vs Machine Learning Platform (§13 sibling, unprocessed) — sharpest seam.** Suite/lakehouse products embed the feature store as a named module inside a broader ML lifecycle platform (SageMaker Feature Store inside SageMaker; Databricks Feature Engineering inside the lakehouse platform; Hopsworks pairing FS with registry/serving/monitoring). Removal tests: strip the feature-data layer (registry + entity/time-versioned values + ML retrieval) from the suite → an ML platform without its feature layer remains; strip training/deployment/monitoring machinery from a feature store → the feature store remains (Feast and SageMaker FS both operate without any training/deployment machinery). Feature store = the feature-data layer; ML platform = the lifecycle platform around models. Cross-check requested at that pass.
2. **vs Model Registry (§13 sibling, unprocessed).** Object of record: feature definitions/values vs model artifacts/versions/stages. Hopsworks ships both side-by-side in one platform (feature groups/views vs model registry/serving) — a clean in-product demonstration that they are distinct registries. Feature lineage can connect the two (Databricks tracks model→feature lineage) without merging them.
3. **vs MLOps Platform (§13 sibling, unprocessed).** MLOps machinery automates the model lifecycle (CI/CD, pipelines, deployment, monitoring); the feature store is a data layer those workflows consume. Feast explicitly disclaims orchestration ("relies on upstream data pipelines… and integrations with tools like Airflow").
4. **vs Data Warehouse / Lakehouse / Data Lake (§13).** The warehouse/lakehouse is the organization's general data of record; the feature store is an ML-specialized downstream layer that frequently *re-uses* warehouse/lakehouse storage (Feast plugins over BigQuery/Snowflake/etc.; Hopsworks external feature groups; Databricks features as Delta tables). Feast's non-goal list states the distinction directly ("not a data warehouse… not a database"). Removal test: remove entity/event-time semantics, the registry, and ML retrieval semantics → a governed table store (the lakehouse pole); add them → the feature store.
5. **vs Data Catalog (§13, processed 2026-09-07).** The data catalog is a metadata/discovery lens over all data assets and does not hold or serve feature values; the feature store's registry is ML-purpose, carries entity/time semantics and value stores, and serves models. Discovery UX overlaps (search/tags/browse) — the seams recorded by that pass remain consistent from this side.
6. **vs Data Science Workbench (§13, processed 2026-09-07) — discharges that pass's cross-check request.** The workbench is the interactive code session (data scientists' surface); the feature store is managed feature-data machinery consumed *by* workbench sessions (features authored from notebooks, training datasets pulled into them). No overlap of centers: the workbench pass's removal tests (remove lifecycle machinery → workbench remains) hold from this side.
7. **vs Customer Data Platform / Audience Management (§06).** CDPs hold entity-keyed profiles for marketing activation; a feature store holds entity-keyed feature values for ML models. Shape is similar (entity-keyed attribute records), the semantics differ: CDPs have no event-time-versioned training retrieval, no point-in-time joins, no model-scoring serving contract, and their consumers are campaigns, not models.
8. **vs Vector Retrieval Platform / Vector Database Console (§13).** Feature retrieval is key-based lookup of entity attributes; vector retrieval is similarity search over embeddings. Products keep them as separate capabilities (Hopsworks ships a vector DB beside its feature store; Databricks treats RAG retrieval as a feature-store use case, not the core). Embeddings may be stored *as* feature values without the Type becoming vector retrieval.

**Remove-what test (Type identity):** remove the registry leg → a feature-value database; remove the historical/time-versioned store → a feature-definition catalog plus serving cache; remove ML-context retrieval → a data platform. What remains of the *name* only after all three legs hold is "Feature Store".

**Historical / market-sample check:** the Type is young (market crystallized ~2017 with internal systems at large ML operators), but the check still applies: pre-"feature-store"-era internal systems — a shared feature registry plus a training-dataset builder performing point-in-time joins, with no online store, streaming, or managed pipelines — satisfy the L0 core. Open-source minimal deployments configured offline-only satisfy it today. Therefore the core as drawn (registry + entity/time-versioned values + dual-context retrieval) does not over-fit the current managed-platform pattern. Era-current machinery (streaming, managed pipelines, monitoring programs, embedding extensions) is held at L1/L2.

## Uncertainties

- Hopsworks: point-in-time-correctness wording was not directly fetched (training-data page unfetched this pass); its training-data generation was observed, and PIT is asserted for the other four samples. Assertions involving Hopsworks are worded accordingly.
- Tecton's performance figures are vendor marketing claims and are not carried into the Application Document.
- Databricks Feature Views were in public preview at research date; packaging and naming are actively drifting ("Feature Store" page name vs "Feature Engineering" API naming vs deprecated workspace-level store). Observations restricted to fetched pages.
- SageMaker offline-store access patterns (Athena, event-time prefix scheme) are product-specific; excluded from the canonical document.
- Google Vertex AI Feature Store and other open-source entrants (Chronon, Feathr) not sampled; the cloud-GCP pole and some OSS diversity are unverified this pass.

## Final Synthesis

A Feature Store is the ML feature-data layer: it treats features as named, shared, entity-bound definitions held in a registry of record; persists their values as entity-keyed, event-time-versioned records in a historical store; and retrieves them for the two contexts models need — point-in-time-correct training datasets and feature-vector lookup for scoring (realized at low latency through an online store in modern products). Everything else — computation engines, streaming, validation/monitoring programs, governance/lineage depth, embeddings — is a capability layer that varies by product philosophy (OSS library vs managed platform vs suite module) and sits on top of that three-part core.
