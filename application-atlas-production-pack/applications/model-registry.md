# Model Registry

## Overview

A **Model Registry** is the shared record system an organization uses to manage its machine learning models: each model is held as a named, persistent entry; every registered model is retained as an identified version carrying its evaluation metrics, input/output schema, descriptions, and references to the code and data that produced it; and the registry is the recorded point where models pass from building to use — versions are marked as approved or production-ready, and deployment pipelines, serving endpoints, and CI/CD workflows resolve what to run *through* the registry.

The defining structure is small:

```text
Registered model entry        ("the model that solves problem X" — persistent, named, shared)
        │  accumulates
Model versions                (numbered records of the model artifact + metadata + lineage)
        │  marked & consumed through
Selection / consumption       (approval states, stages, or aliases → deployment, CI/CD)
```

Everything else commonly present — search and comparison surfaces, lineage graphs, access control, webhooks, model documentation cards — makes the registry workable but does not define it. Equally important is what the registry does not do: it trains nothing, tracks no experiments, serves no predictions, and watches no production traffic. It is the layer of record around which training, deployment, and monitoring machinery flows.

Remove the named model entries and only a versioned file store remains; remove the versioned records and only a mutable current-model folder remains; remove the selection-and-consumption layer and only an archive of experiment outputs with no recorded answer to "which version is in production?" remains.

## Users & Context

The registry serves the same data organization that builds models, with each role touching a different layer:

- **Data scientists** register the outputs of their training work: at the end of a training run or pipeline, they publish the resulting model into the registry, where it gains a version number and picks up its metrics and lineage. Registration is usually done from code rather than through the UI.
- **ML engineers** manage the model estate day to day: comparing candidate versions, updating metadata and descriptions, marking versions as approved or production-ready, and wiring the registry into deployment pipelines.
- **Reviewers and approvers** (in governed teams) inspect a version's metrics, evaluation records, and lineage before it can be marked for production; the mark itself is a permissioned act.
- **Platform / MLOps engineers** own the registry as infrastructure: its access model, its integration with CI/CD and serving, and its sharing configuration across teams, workspaces, or accounts.
- **Downstream consumers** — deployment pipelines, serving endpoints, batch-scoring jobs, and the teams that run them — are mostly indirect users: they reference a model version (or its "current"/"production" alias) through the registry rather than copying model files around.
- **Governance and audit roles** read the registry's lineage and history to answer where a production model came from and what changed over time.

The work context is the organization's **model estate**: the shared answer to which models exist, which versions are candidates, which version currently serves each use case, and how each of those versions traces back to its training data and code.

## Core Model

### The defining core

Three structures, held together.

**The registered model of record.** A registered model is a persistent, named entry that stands for "the model that solves this problem" — a fraud-detection model, a demand-forecasting model — as a shared object of the organization rather than a private file. It outlives individual experiments, jobs, and team changes, and it is the container under which versions accumulate. Products name this container differently (model group, registered model, registry collection), but the concept is constant: one entry per model, discoverable by the whole organization.

**The model version as the unit of record.** Each time a model is registered, it becomes a numbered version under its entry — a retained record of the model artifact together with what the organization knows about it:

- the **artifact** itself, stored by the registry or referenced in external storage
- **evaluation metrics** recorded alongside it (for example, performance on test data)
- an **input/output schema** (signature) describing what the model expects and returns
- **descriptions, tags, and documentation** — including, in some products, evaluation images and model cards
- **provenance** — references to the run, job, code, and data that produced it

Versions are retained and comparable rather than overwritten: version 7 does not replace version 6; both remain inspectable. This is what makes the registry a *record* system rather than a storage folder — the model's history and its evidence travel with it.

```text
REGISTERED MODEL  "fraud-detection"
├── v5   metrics · schema · lineage → run #812, dataset A   (archived)
├── v6   metrics · schema · lineage → run #903, dataset B   (approved → serving)
└── v7   metrics · schema · lineage → run #974, dataset C   (candidate)
```

**The selection-and-consumption junction.** The registry is where the organization's decision about *which version is in use* is recorded and acted on. A version is marked as qualified — through a lifecycle stage, an approval status, or a named alias (such as a "production" or "champion" alias) — and downstream machinery resolves what to run by pointing at the registry rather than at raw files: a serving endpoint references the production alias; a batch-scoring job loads the version an alias currently denotes; a CI/CD pipeline reacts when a version is approved or an alias moves. Updating production then means moving the mark to a different registered version, and rollback is the same operation in reverse. Where a product does not provide in-record marks, the same junction is realized through environment-scoped registries (separate development/staging/production registries with promotion between them) and version-addressable consumption.

### Standard capabilities mature products add

Expected in current products but not what makes the registry a registry:

- **Search and comparison** — finding models and versions across the organization, comparing metrics across versions side by side.
- **Lineage graphs** — browsable references from a version back to its producing run, code, and training data; captured automatically where the registry is paired with an experiment tracker or data catalog.
- **Access control and sharing** — per-model or per-registry roles; sharing across teams, workspaces, accounts, or regions; restricting who may mark versions or download artifacts.
- **Documentation surfaces** — descriptions, model cards, input examples, evaluation images.
- **Automation and events** — webhooks or notifications when a version is approved or an alias changes; deployment history views.
- **Programmatic parity** — an SDK/API surface (register, describe, transition, alias, search) that training code and pipelines call directly; registration from code is the dominant path.

### One structure, many implementations

The core is written conceptually; products realize each part differently:

```text
Concept:   Registered model of record
Realized as: Model Group, registered model, registry collection

Concept:   Model version record
Realized as: numbered model package/version; artifact held in-registry
             or linked by pointer into external storage

Concept:   Selection marking
Realized as: named lifecycle stages, approval statuses, mutable
             aliases, or separate environment-scoped registries
```

A reader who has only seen one shape — say, aliases in a hosted catalog — should still recognize a stage-based registry or an approval-workflow registry as the same kind of system.

## How It Works

### Register a version

```text
Training run / pipeline produces a model
→ the producer (or a pipeline step) registers it into a named model entry
→ the registry assigns the next version number
→ the version record captures metrics, schema, description, tags
   and references to the producing run/job/code/data
```

Registration usually happens from training code or a pipeline step, not from the UI. If the entry does not exist yet, it is created on first registration. External models can also be imported into a registry in some products.

### Evaluate and compare

```text
Open the model entry's version list
→ compare candidate versions' metrics side by side
→ inspect a version's lineage: which run, which data, which code
→ read evaluation records and documentation
```

Comparison is the everyday reading loop of the registry: the retained, metadata-carrying versions are what make a decision from last quarter reproducible today.

### Mark for use

```text
A candidate version is reviewed (in governed teams: explicit approval)
→ it is marked as qualified: approval status set, stage advanced,
   or a production/staging alias assigned to it
→ the act is permissioned and recorded
```

The mark is a state on the version record — never an overwrite of the artifact. Products differ in the machinery (stages, statuses, aliases, or environment-scoped registries); the pattern — evaluate, approve, mark — is consistent.

### Consume

```text
Deployment pipeline / serving endpoint / batch job
→ resolves the version to run through the registry:
   by alias ("the current production version"), by stage/approval
   state, or by direct version reference
→ the workload binds to that version
```

Updating production means re-pointing the mark at a different registered version; consumers that reference the alias pick up the new version on their next execution, and rollback is moving the mark back. The deployment never drifts from the record, because it is the record the deployment machinery reads.

### Govern over time

```text
Who approved version 6? → the registry records it
Which dataset trained the model now in production? → lineage lookup
Which versions are safe from deletion? → protected marks
A model is retired → its versions are explicitly deleted (destructive)
```

The record system is also the audit surface: lineage, history of changes, and permissioned marks are how governance questions become lookups rather than investigations.

### Capability tiers

**Defining core** — without these, not this Type:

- named, persistent model entries shared across the organization
- versioned model records retaining the artifact with ML-typed metadata and lineage
- the selection-and-consumption junction: marks that qualify versions, and consumption of versions by reference

**Standard structure** — present in most mature products:

- search, comparison, lineage graphs, access control and sharing, documentation surfaces, automation/webhooks, SDK/API parity, audit history

**Variant / optional** — depends on packaging and philosophy:

- stage-based vs alias-based vs approval-status vs environment-scoped promotion
- registry-held vs externally referenced artifacts
- standalone machinery vs suite-embedded service vs catalog-integrated governance vs artifact-generic registry
- cross-account/cross-region sharing; external model import; marketplace-adjacent packaging

## Interfaces

### Registry browser (models list)

The primary entry surface.

- typical information: registered models/groups, their owners, version counts, recent activity, organizational grouping
- primary actions: open a model entry, search/filter, create an entry

### Model entry page

- typical information: the entry's description and tags, its version list with numbers and marks (stages/approvals/aliases), latest activity
- primary actions: open a version, compare versions, add tags/description, manage aliases or approval states where provided

### Version detail page

- typical information: the version's metrics, input/output schema, description, tags, artifact location, lineage references (run/job/code/data), evaluation records
- primary actions: edit metadata, set/advance marks, download or reference the artifact, delete (destructive, permissioned)

### Comparison view

- typical information: candidate versions' metrics side by side
- primary actions: select versions to compare, promote the comparison into an approval decision

### Lineage view

- typical information: the graph connecting the version to its producing run, code, and training data (and, where integrated, to feature data)
- primary actions: traverse the graph, open linked records

### Administration / access settings

- typical information: who can view, register, mark, or delete; cross-team/workspace/account sharing configuration
- primary actions: assign roles, configure sharing, manage protected marks

### SDK / API

The dominant registration and consumption surface: training code and pipelines call the registry programmatically to register versions, set marks, resolve the current production version, and search records.

## Important Rules / Behaviors

- **Versions are promoted, not overwritten.** A registered version is an identified record; qualification changes (approval, stage, alias) are state changes on it. Production updates and rollbacks are re-pointings of a mark, which is what makes iteration safe.
- **The version's artifact is fixed at registration; its metadata is not.** Descriptions, tags, schema additions, and documentation can be updated after registration; the artifact itself is not replaced. Deletion of a model or version is an explicit, destructive act that removes the artifact and its record.
- **One mark, one version.** Where aliases are the marking mechanism, an alias denotes a single version at a time — moving the mark moves production. Tags, by contrast, can be shared by many versions.
- **Environment placement is not deployment status.** A version registered in a "production" container is not thereby in production: its location reflects governance rules; its deployment status is what the mark (alias/approval) says. Products separate these two concepts explicitly.
- **Marking is permissioned.** Who may approve, promote, or assign a production mark is an access-control decision; protected marks can make designated versions un-modifiable and un-deletable by non-administrators.
- **Registration and lineage are producer-dependent.** A version can be registered from a tracked run, a pipeline, or independently; lineage exists for what was linked at registration time, and is captured automatically only where the registry is integrated with the tracker or catalog.
- **Signatures gate consumption where present.** When a version carries an input/output schema, consumers can have their inputs validated against it at inference time; versions without a schema accept whatever they are given.
- **The registry serves nothing and trains nothing.** Deployments, batch scoring, and training all happen elsewhere; the registry's role is the recorded reference point between them. Exact state vocabularies, numbering conventions, and limits are product-specific and are not stated here as universal.

## Variants

Common shapes the Type takes in the market:

- **Standalone open-source record machinery** — the registry as an embeddable component paired with experiment tracking; the de-facto standard layer many platforms integrate with; promotion through named stages plus review/approval workflows.
- **Suite-embedded registry service** — the registry as a governed component of a cloud ML platform, with model groups and collections, deployment and CI/CD integration, and cross-account sharing.
- **Catalog-integrated registry** — models held as governed objects inside the organization's data catalog: enterprise privileges, audit, and lineage machinery shared with tables and other data assets; promotion realized through mutable aliases rather than stages.
- **Org-level artifact registry** — a curated central registry of versioned artifacts whose flagship type is models: registry → collection curation, role-gated protected marks, org-wide sharing across teams, event automation on marks.
- **Environment-scoped registries** — promotion realized by separate development/staging/production registries with CI/CD moving versions between them, rather than by in-record states.
- **Artifact-generic extension** — the same registry holding datasets, prompts, and other artifact types beside models.

A variant remains a variant while the defining core — named entries, versioned records, and the selection-and-consumption junction — still applies.

## Related Application Types

| Type | Distinction |
|---|---|
| Machine Learning Platform | the build-and-operate lifecycle around models: platform-executed training, a model artifact of record, and a deployment bridge. The registry is the record machinery inside that lifecycle — and also exists standalone outside any platform. Suites embed a registry; the registry does not embed a platform. |
| MLOps Platform | the record-and-loop machinery: tracked run records + versioned model records with promotion + the operationalization bridge. The registry alone has no run-tracking spine and no operationalization loop; it is the model-record system that loop flows through. |
| AI Model Hosting Platform | operates serving infrastructure that applications invoke. The registry serves nothing — it records and hands off; train → register → deploy passes through it with hosting downstream. |
| Feature Store | the feature-data layer: feature definitions and entity/time-versioned feature values. Distinct object of record from model artifacts; the two often ship side by side and connect through lineage without merging. |
| ML Model Monitoring Platform | the deployed-model watch loop (drift, performance, integrity). Not a registry capability — monitoring reads the registry's records (which version is deployed) and operates elsewhere; bundling happens at platform level, not in the record system. |
| Artifact Repository | format-generic custody of built software artifacts keyed by package coordinates, serving package-manager resolution. The registry's records are ML-typed governed objects (metrics, signatures, training lineage) consumed by deployment decisions about which model version is in use. |
| Data Science Workbench | the interactive code session where analysis and model building happen. Sessions and runs produce the artifacts that get registered; the registry sits downstream as the record layer. |
| AI Governance Platform | the business/risk/legal registry for AI systems: policies, review state, compliance context. The model registry holds technical artifact records; governance consumes them. |
| Model API Platform | provides inference access to a vendor's own first-party model line. The registry holds an organization's own models and serves nothing. |
| Public model hubs | distribution and discovery of pretrained models to the public. A different contract from organizational governance of self-built models; hubs appear in this Type as ingestion sources, not variants. |

The boundary with the MLOps Platform and the Machine Learning Platform is the most important one, because every sampled platform embeds a registry and market labels overlap. The structural test is the center of gravity: the platforms center the lifecycle (executing training; running the record-promote-deploy loop), while the registry centers the model record — and exists, in open-source form, with no lifecycle machinery around it at all.

## Representative Products

- **MLflow Model Registry** — open-source, vendor-neutral record machinery: centralized model versioning, stage management, lineage tracking, and team review workflows; the classic archetype and the integration pole for many platforms.
- **Amazon SageMaker AI Model Registry** — suite-embedded registry service: Model Groups and versioned model packages, staging construct and approval statuses, deploy-from-registry and CI/CD automation, cross-account discoverability.
- **Databricks Models in Unity Catalog** — catalog-integrated registry: models as governed securable objects with enterprise privileges, audit, and lineage; alias-based promotion; a documented evolution from stages to aliases.
- **Weights & Biases Registry** — SaaS org-level curated registry: registries and collections of versioned artifacts with models as the flagship type; role-gated protected marks; event automation.
- **Hopsworks Model Registry** — open platform registry beside a feature store, feeding KServe serving; versioned model packages with schema, sample data, and provenance; environment-scoped registries for promotion.

The defining core was checked against open-source machinery, hyperscaler suites, a data-catalog-integrated registry, a SaaS artifact registry, and a feature-store-paired platform, so that no single packaging philosophy is baked into the definition.

## Sources

Research date: **2026-09-08**

- Amazon SageMaker AI — *Model Registration Deployment with Model Registry* and *Model Registry Models, Model Versions, and Model Groups* — https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html
- Weights & Biases — *W&B Registry overview* and *Reference an artifact version with aliases* — https://docs.wandb.ai/models/registry.md , https://docs.wandb.ai/models/registry/aliases.md
- Hopsworks — *Model Registry* (concepts) and documentation home — https://docs.hopsworks.ai/latest/concepts/mlops/registry/
- Databricks — *Manage model lifecycle in Unity Catalog* — https://docs.databricks.com/en/machine-learning/manage-model-lifecycle/index.html
- MLflow — *Model Registry* documentation (fetched via the paired research effort; this document's registry concepts corroborated through the Databricks-hosted MLflow documentation above)

> Sourcing limitations: one vendor's documentation site was unreachable from the research environment during this pass (its registry evidence carried from a prior direct fetch of the same official documentation); one cloud vendor's documentation repeatedly timed out and was excluded without claims. Product-specific state vocabularies, numbering conventions, version thresholds, and limits are intentionally not stated as universal in this document. Detailed product-by-product observations, the cross-product comparison, and boundary removal tests are recorded in the paired Research Notes.
