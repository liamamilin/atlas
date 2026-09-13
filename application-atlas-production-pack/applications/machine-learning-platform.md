# Machine Learning Platform

## Overview

A **Machine Learning Platform** is the system an organization uses to build, deploy, and operate its own predictive models. It runs model training on compute it manages, holds the trained models as governed, versioned artifacts, and moves them into prediction services that applications consume — then keeps those models current through monitoring and retraining.

The defining core is small:

```text
Managed training run          (the platform executes model-building)
        │  produces
Model artifact of record      (versioned, traceable, survives the run)
        │  promoted
Deployment into serving       (real-time endpoint / batch scoring)
        │  consumed by
Applications                  (feedback → monitor → retrain)
```

Everything else the market associates with these products — notebooks, feature stores, data labeling, automated model search, pipeline orchestration, registries, monitoring dashboards, foundation-model catalogs — is mature structure arranged as modules around that core. Remove the build side and only serving for externally built models remains (model hosting); remove the lifecycle and only an interactive development session remains (data science workbench); remove the models themselves and only a feature-data layer or a record catalog remains.

## Users & Context

The platform serves a data team spread across roles, each touching the model lifecycle at a different stage:

- **Data scientists** explore connected data, engineer features, and build and evaluate models — interactively at first, then as repeatable training runs.
- **ML engineers** productionize what data scientists prove: they turn training code into pipelines, promote registered models, operate deployments, and tune serving.
- **Platform administrators** own the container layer: they create workspaces or projects, manage compute and environments, and control who can see and do what.
- **Application developers** are consumers: they call prediction endpoints from their own services and rarely touch the build side.
- In governed deployments, **reviewers or stewards** approve models for production and read lineage and audit records.

The work context is an organization's data estate: the platform connects to data the organization already holds (warehouses, lakes, databases, streams) and exists to turn it into models that serve predictions inside products and operations. Regulated industries use the same platform with heavier emphasis on reproducibility, lineage, and approval.

## Core Model

### The defining core

Three structures, held together. Each one is load-bearing; remove any and the product stops being this Type.

**Managed model-building runs.** The platform provisions and operates the compute on which model-building actually executes. The user brings training logic (custom code, an automated build, or a pipeline step) and connected data; the platform runs it as a managed, recorded unit — a job or run with its inputs, logs, metrics, and outputs captured. This is what separates a platform from a personal analysis environment: the work survives the session in the platform's own records, and it scales from a single machine to distributed compute without the user operating servers.

**The model as the held unit of record.** The output of a build run is a model artifact that the platform persists as an identified object — commonly versioned and registered — that outlives the run. The artifact is traceable to the run and data that produced it, and it is the object to which everything downstream attaches: evaluation records, approvals, deployments, monitoring. Without a held model record there is no lifecycle — only runs and files.

**The deployment bridge into prediction service.** The platform moves held models into serving surfaces that applications consume: real-time prediction endpoints that respond to requests over the network, and batch scoring jobs that score datasets on schedule or on demand. The deployed instance remains bound to the model record — an update or rollback is performed by pointing the deployment at a different model version, not by rebuilding.

```text
Data the organization connects
        │
        ▼
Managed training run  ──  recorded (inputs, metrics, artifacts)
        │
        ▼
Model artifact of record  ──  versioned, registered, traceable
        │
        ▼
Deployment  ──  real-time endpoint / batch scoring
        │
        ▼
Applications & consumers
        │
        ▼
Monitor → retrain loop  (back to a new training run)
```

### Standard capabilities mature products add

These are expected in current products but do not define the Type:

- **Experiment tracking** — each build run records its parameters, metrics, and artifacts so runs can be compared and the best one identified.
- **Registry machinery** — versions, lifecycle stages, approval workflows, and lineage connecting a model version to its producing run, training data, and environment.
- **ML pipelines** — the build–register–deploy–retrain sequence expressed as an orchestrated, scheduled or event-triggered workflow.
- **Embedded development surfaces** — notebooks and IDEs inside the platform, from which managed runs are launched. (The interactive session itself is the neighboring Data Science Workbench Type; inside an ML platform it is a module.)
- **Tenancy containers** — a workspace, project, or domain that organizes people, assets, and permissions; sharing within and sometimes across containers.
- **Serving options** — autoscaling endpoints, traffic splitting between model versions for safe rollout, and batch inference.
- **Production monitoring** — drift and quality detection on live predictions feeding the retrain loop.
- **Environment management** — captured dependencies and container images so a run is repeatable elsewhere.
- **Compute elasticity** — distributed training across many machines and GPUs when the work demands it.
- **Governance machinery** — audit logs, access control, model documentation, CI/CD integration.

### One structure, many implementations

The core is written conceptually. Products realize each concept differently:

```text
Concept:   Managed training run
Realized as: custom-code training jobs, automated model builds,
             pipeline steps, scheduled notebook jobs

Concept:   Model artifact of record
Realized as: registered model versions with approval stages,
             lineage-tracked artifacts in a governance catalog,
             versioned artifacts in object storage

Concept:   Deployment bridge
Realized as: managed prediction endpoints, self-managed serving
             components, batch/scoring jobs, serverless options

Concept:   Tenancy container
Realized as: workspace, project, domain, namespace
```

## How It Works

### The lifecycle loop

The platform's work is a continuous cycle, which the products themselves describe in matching stages:

```text
Connect data
→ build and evaluate models (tracked runs)
→ register and promote the chosen model
→ deploy to serving
→ applications consume predictions
→ monitor live behavior
→ collect new data / retrain
→ back to build
```

### A build run

```text
Attach or reference data
→ author or select training logic (own code, automated build, or pipeline step)
→ choose compute (from small to distributed)
→ submit the run
→ the platform executes it and records parameters, metrics, logs, artifacts
→ compare runs; keep the winning model
```

The run is the reproducibility unit: because its inputs and outputs are recorded, the same model can be rebuilt and audited later.

### Promotion and deployment

```text
Model version registered
→ evaluated against held-out data and acceptance criteria
→ approved (stage promoted) — the gate most products make explicit
→ deployed: the version is bound to a real-time endpoint or batch job
→ traffic may be split between old and new versions while confidence builds
→ rollback = re-point the deployment at the prior version
```

Exact stage labels vary by product; the pattern — register, test, approve, deploy, with the deployment bound to versions — is consistent across the researched sample.

### Operating side

Once serving, the model is a live asset: the platform exposes its request load and health, watches input data and prediction quality for drift, and turns detected degradation into a new training run. Applications integrate by calling the endpoint or writing data for batch scoring; they are decoupled from how the model was built.

### Capability tiers

**Defining core** — without these, not this Type:

- platform-executed model-building runs
- the model artifact as held, versioned record
- the deployment bridge into real-time or batch prediction serving

**Standard structure** — present in most mature products:

- experiment tracking; registry with approval; pipelines; embedded notebooks; tenancy and permissions; serving options incl. traffic splitting; production monitoring; lineage/audit

**Variant / optional** — depends on segment and philosophy:

- automated model building / no-code builders
- embedded feature store or external feature layer
- embedded data labeling
- foundation-model catalogs, hosted third-party model APIs, large-scale fine-tuning
- edge deployment, human review of predictions, model documentation cards
- self-managed open-source packaging vs vendor-managed cloud service

## Interfaces

### Studio / web console

The primary operations surface.

- typical information: lists of training runs, models and versions, endpoints, pipelines, jobs, with status and owners
- primary actions: launch a run, compare experiments, register/promote a model, create or update a deployment, inspect monitoring

### Embedded development environment

Notebooks and code editors inside the platform, attached to its data and compute.

- purpose: interactive exploration and authoring of training logic
- primary actions: browse data, prototype, launch the prototype as a managed run, schedule a notebook as a job

### SDK / CLI / API

Programmatic parity with the console; most mature products let everything done in the UI be done from code.

- primary actions: submit runs, build pipelines, register and deploy models, query status and metrics

### Pipeline editor

Where the lifecycle is expressed as a workflow — visually or in code.

- typical information: pipeline graph, steps, triggers, run history
- primary actions: compose steps (data prep → train → evaluate → register → deploy), schedule, retrigger on new data

### Monitoring / governance views

- typical information: endpoint traffic and health, drift and quality signals, lineage graphs, approval state, audit events
- primary actions: acknowledge alerts, compare current vs baseline, trigger retraining, review lineage

## Important Rules / Behaviors

- **The model record outlives everything.** Runs finish and sessions close; the registered model version persists and is what deployments, approvals, and audits reference.
- **Deployments are bound to versions.** Updating a live model means deploying a different registered version; rollback is the same operation in reverse. This is what makes production iteration safe.
- **Promotion is gated.** In governed products a model version typically must pass evaluation and an explicit approval before it can serve production traffic; "register → stage → test → promote" is the documented pattern.
- **Runs are the audit trail.** Build runs capture code, data references, parameters, and outputs; lifecycle auditability — "auditable if not reproducible" in one vendor's own framing — is a first-class requirement, not an add-on.
- **Compute is the platform's problem.** Users describe what to run and at what scale; the platform provisions, schedules, and tears down compute. Idle-session compute and run compute are billed or capacity-managed differently across products.
- **Tenancy controls reach.** Data, features, models, and endpoints all live inside the tenancy container, and access control on the container governs who can build, deploy, or call. Calling a prediction endpoint is a permissioned act, not a public one.
- **Models degrade.** Live prediction quality depends on the world staying like the training data; monitoring for drift is the standard mechanism that closes the loop back to retraining.
- **Exact limits, state names, and defaults vary.** Numbers (instance sizes, version counts, retention) and stage labels are product-specific; this document states none as universal.

## Variants

Common shapes the Type takes in the market:

- **Hyperscaler managed suites** — the platform as a fully managed cloud service with per-use compute; code-first and no-code build paths side by side.
- **Lakehouse-embedded platforms** — the lifecycle layered directly on the organization's data platform, with governance catalogs spanning data, features, and models in one system.
- **Self-managed composable stacks** — open-source components (notebooks, training, pipelines, serving) assembled by the organization on its own infrastructure; the strongest "no vendor cloud" pole.
- **Feature-store-first platforms** — platforms that grew from the feature-data layer outward, sellable as a standalone feature store or as a full lifecycle platform.
- **AutoML-led / code-optional** — build experience centered on automated model search and visual builders, aimed at analysts as much as engineers.
- **Scale-out fine-tuning variants** — the same core pointed at large-model training, with cluster reservations and distributed-training machinery as the differentiator.

A variant remains a variant while the defining core — managed runs, model record, deployment bridge — still applies.

## Related Application Types

| Type | Distinction |
|---|---|
| Data Science Workbench | the interactive code session is the center; it has no lifecycle of its own. Embedded in an ML platform it is a module. Strip the platform's managed runs/registry/endpoints and the session remains. |
| Feature Store | manages the feature-data layer (definitions, entity/time-versioned values, training/serving retrieval) — a data layer the ML platform consumes. Present as an embedded module, an external service, or not at all. |
| Model Registry | the record-keeping machinery itself (versions, stages, approvals) as a standalone object-of-record system; inside ML platforms it is a component. |
| AI Model Hosting Platform | centers on operating serving for consumption, often for models it did not build; training is at most a bundled adjacent capability. The ML platform's center includes building the models. |
| MLOps Platform | names the lifecycle-automation discipline (CI/CD for models, reproducibility, monitoring practice) — in market labels the two Types overlap heavily and a joint boundary pass is warranted. |
| Data Labeling Platform | manages the annotation production workflow; embedded labeling here is a module feeding training data. |
| AI Model Evaluation Platform | evaluates the market's AI models with standardized instruments; the ML platform evaluates the organization's own models through its tracked runs. |
| ETL / orchestration platforms | general data-pipeline machinery; ML-platform pipelines are scoped to the model lifecycle. |
| LLM Application Development Platform | builds applications over consumed foundation models; the ML platform builds the organization's own models (fine-tuning is training). |

## Representative Products

- **Amazon SageMaker AI** — hyperscaler managed suite; the documented build → train → deploy loop with a broad module catalog (registry, monitoring, AutoML, labeling, feature store).
- **Azure Machine Learning** — hyperscaler managed service built around workspaces, versioned assets, jobs, and managed endpoints, with an explicit role and MLOps framing.
- **Databricks (machine learning)** — lakehouse-embedded platform whose notebooks, MLflow tracking, and Unity Catalog governance carry the lifecycle from data to served models.
- **Kubeflow** — open-source, Kubernetes-native composable stack (training, pipelines, serving, optional registry); the self-managed pole.
- **Hopsworks** — feature-store-first modular platform sellable as a standalone feature store or a full registry/serving/pipeline platform.

The defining core was checked against the minimal, non-cloud pole (a composable stack that is "just a simpler way to run training jobs" plus artifact flow and serving) and against the pre-cloud build→register→deploy scoring lineage, so that no modern packaging (cloud, notebooks, AutoML, feature stores, Kubernetes) is baked into the definition.

## Sources

Research date: **2026-09-08**

- AWS — *What is Amazon SageMaker AI*, *Overview of machine learning with Amazon SageMaker AI*, *SageMaker AI Features* — https://docs.aws.amazon.com/sagemaker/latest/dg/
- Microsoft — *What is Azure Machine Learning?* — https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning
- Databricks — *Machine learning on Databricks*, *Concepts: Data science and machine learning on Databricks* — https://docs.databricks.com/aws/en/machine-learning/
- Kubeflow — *Introduction*, *Trainer Overview* — https://www.kubeflow.org/docs/
- Hopsworks — Documentation home and MLOps/project concepts — https://docs.hopsworks.ai/latest/

> Sourcing limitation: Google Vertex AI documentation could not be reached from the research environment (repeated timeouts), and DataRobot documentation returned an access error; neither product was sampled and no claims are made about them. All statements above are calibrated to the five documented products; product-specific numeric limits, state names, and defaults are intentionally omitted.

Detailed product-by-product observations, the cross-product comparison, and boundary removal tests are recorded in the paired Research Notes.
