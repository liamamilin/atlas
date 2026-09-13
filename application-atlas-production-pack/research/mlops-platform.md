# Research Notes — MLOps Platform

Research date: 2026-09-08
Directory leaf: MLOps Platform (§13 Data, Analytics & AI Systems)
Slug: mlops-platform

## Research Goal

Understand what a "MLOps Platform" actually is as an Application Type — separate from the already-processed Machine Learning Platform, whose pass left a forward flag: "every sampled product uses 'MLOps' as the practice/capability framing... the ML platform is the concrete build-and-operate system; MLOps names the lifecycle-automation discipline/machinery implemented on it... the leaves overlap heavily in market labels — recommend joint review... possible gradient resolution analogous to hosting." This pass must answer: is MLOps Platform a distinct Type, an alias, or a gradient sibling? What is its own center, removal-tested? Also discharge the ml-model-monitoring-platform pass's forward flag ("expect monitoring named as a bundled capability there too") and pre-check the unprocessed model-registry seam.

## Initial Boundary

- Hypothesis: "MLOps Platform" names the **record-and-operationalization machinery** of the model lifecycle — the loop that records runs, versions and promotes models, and moves them into production — as opposed to the ML platform's **execution center** (platform-operated model-building compute). If the market contains products labeled MLOps that execute no training on their own compute, the two leaves cannot be aliases; the resolution is a gradient (analogous to AI Model Hosting vs Machine Learning Platform).
- Likely confusions: Machine Learning Platform (execution center), Model Registry (record machinery alone), ML Model Monitoring Platform (the watch loop), Data Science Workbench (interactive session), DataOps Platform (data-pipeline lifecycle), CI/CD platforms (software-artifact delivery), Feature Store (feature-data layer), AI Governance Platform (business/risk registry).
- Prior flags to discharge: machine-learning-platform forward flag (b) — vs mlops-platform; ml-model-monitoring-platform forward flag — "expect monitoring named as a bundled capability there too".

## Research Questions

1. What structures are jointly held by products the market labels "MLOps platform"?
2. Is managed/owned model-training execution required, optional, or absent across that population? (the alias test)
3. What is the record spine (runs? models? both?) and what does promotion look like?
4. How is operationalization realized — built-in serving, deployment targets, or registry-triggered handoff?
5. What automation machinery exists, and is it definitional or common?
6. Where do monitoring, HPO/sweeps, tenancy, and LLM/GenAI surfaces sit (core vs standard vs variant)?
7. Removal tests both directions against each §13 sibling; label-overlap evidence.
8. Would older / non-cloud / differently positioned products still fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| MLflow | open-source, vendor-neutral record machinery (tracking + registry + deployment clients); the de-facto standard; docs explicitly frame the ML tooling as "MLOps" | the archetype of the machinery-without-owned-compute pole; huge market presence |
| Weights & Biases (W&B) | SaaS record-first platform (tracking, artifacts, registry, sweeps) with Launch automation over the customer's own compute infrastructure | tracking-first commercial pole; free-to-enterprise customer span |
| Comet | SaaS "ML platform... track, compare, explain, and optimize... from managing experiments to monitoring models in production" | tracking + registry + webhooks + production monitoring SaaS pole; VPC/on-prem enterprise posture |
| Valohai | execution-orchestration commercial platform; reproducibility-first philosophy; YAML-defined jobs/pipelines; hybrid/on-prem/SLURM deployment | the gradient straddler that orchestrates training execution on customer infra |
| ClearML | OSS + commercial full stack: agents/queues execution, experiment tracking, pipelines, serving/GenAI engine, GPUaaS control plane | self-managed full-stack pole; documents the machinery/execution gradient inside one product |

Cross-check suite evidence (already recorded [A] in research/machine-learning-platform.md): SageMaker (Projects CI/CD, Pipelines, Model Registry, Model Monitor as the MLOps module group), Azure ML ("train and deploy models and manage MLOps"; "auditable if not reproducible"), Databricks ("MLOps workflows"; 8-stage lifecycle), Hopsworks ("MLOps capabilities": Experiments → Registry → Serving → Monitoring). Dropped in the sibling pass and not re-attempted per the recorded source-access limitation: Google Vertex AI (timeouts), DataRobot (403).

## Sources

All fetched 2026-09-08. Tier-1 operational documentation throughout.

- MLflow — Documentation home + ML section: https://mlflow.org/docs/latest/index.html ; https://mlflow.org/docs/latest/ml/ (tracking, model registry, deployment, evaluation descriptions)
- Weights & Biases — Documentation index: https://docs.wandb.ai/ ; llms.txt doc map: https://docs.wandb.ai/llms.txt (product cards; W&B Launch pages: platform/launch.md and concept pages)
- Comet — Docs home: https://www.comet.com/docs/v2/ (guides index: experiment management, artifacts, model registry, production monitoring, self-hosted)
- Valohai — Docs index/llms.txt: https://docs.valohai.com/llms.txt ; Philosophy: https://docs.valohai.com/readme/philosophy/reproducibility-by-default.md
- ClearML — Documentation overview: https://clear.ml/docs/latest/docs/ (three-layer platform overview)
- Sibling-pass Tier-1 sources (SageMaker/Azure ML/Databricks/Kubeflow/Hopsworks) recorded in research/machine-learning-platform.md, consulted for the suite-side framing.

No Tier-3 sources needed. Source-access limitations: ClearML evidence held at overview-layer depth (deeper pages not fetched); MLflow OSS automation machinery not observed in fetched pages; W&B production model monitoring not observed in fetched pages. Claims calibrated accordingly below.

## Product Observations

### MLflow [A: directly observed]

- Self-definition: "the largest open source **AI engineering platform** for agents, LLMs, and ML models"; teams use it to "debug, evaluate, monitor, and optimize production-quality AI applications"; explicit Type framing: "If this is your first time exploring **MLflow for MLOps**, the tutorials and guides here are a great place to start."
- ML capabilities as documented: **MLflow Tracking** ("comprehensive experiment logging, parameter tracking, metrics visualization, and artifact management"; experiment organization/comparison; artifact storage with each run; share experiments across teams); **Model Registry** ("centralized model versioning, stage management, and model lineage tracking"; "Version Control: Track model versions with automatic lineage"; "**Stage Management: Promote models through staging, production, and archived stages**"; "**Team-based model review and approval workflows**"; model discovery/search across the organization); **Deployment** ("supports multiple deployment targets including REST APIs, cloud platforms, and edge devices"; built-in REST serving with input validation; batch inference); **Evaluation** (automated metrics, custom evaluators, model comparison, tracked validation datasets).
- Runs anywhere: local, on-prem, cloud, managed services; "vendor-neutral"; self-hosting section; collaboration layer for teams.
- **No managed training execution**: training runs wherever the user runs code; MLflow records and registers. **No trigger/schedule machinery observed** in OSS docs (the Databricks-hosted variant adds jobs — sibling-pass evidence).

### Weights & Biases [A]

- Self-definition: "Develop AI models and ship LLM applications with the **W&B platform for experiment tracking, evaluation, and observability**."
- W&B Models product card: "Manage AI model development with **experiment tracking**, fine-tuning, reporting, hyperparameter **sweeps**, and a **model registry for versioning and reproducibility**."
- W&B Launch: "Scale and manage ML workloads with W&B Launch by configuring **jobs, queues, and agents on your compute infrastructure**." Concepts: jobs, queues, target resources, agents, agent environments. Targets documented: Docker/local machine, Kubernetes (Helm, Kaniko image building), **SageMaker** (training jobs), **Vertex AI** (CustomJob) — Launch drives execution ON the customer's infrastructure; jobs created "from Git repositories, code artifacts, or Docker images"; queues control who can push; queue observability dashboard; sweeps-on-launch.
- Support tag surface (documented product objects): experiments, runs, artifacts, sweeps, workspaces, teams, alerts, resuming, reports, run crashes.
- Modern overlay: W&B Weave (LLM tracing/evaluation), Serverless Inference / Serverless Training (public preview, CoreWeave-powered), Sandboxes (private preview).

### Comet [A]

- Self-definition: "Data science and machine learning teams use **Comet's ML platform** to **track, compare, explain, and optimize their models across the complete ML lifecycle – from managing experiments to monitoring models in production**."
- Two-line SDK start; experiments log parameters, metrics, models, code, images, point clouds, tables, text, audio, video, curves, HTML, assets, remote data; resume; distributed training; notebook runs; search & export; migration tooling ("Load data from Neptune").
- **Model Registry**: register/manage models, **model approval**, **webhooks — "Integrating with CI/CD pipelines"**; landing copy: "Save model versions and **deploy registered models using your computing environment**."
- **Production Monitoring (MPM)**: send production data, dashboards, custom metrics — the watch loop as a module.
- **Artifacts**: dataset versions, remote artifacts, **data lineage**. **Optimizer**: HPO. Comet UI: project pages, single-experiment page, visualizations/panels, admin dashboard, service accounts.
- Enterprise posture: "we treat virtual private cloud (VPC) and on-premises environments as first-class citizens"; self-hosted section.
- **No managed training execution**: tracking hooks onto the user's own compute via SDK/framework integrations (SageMaker, Vertex, Kubeflow, Metaflow, Ray, TensorBoard...).

### Valohai [A]

- Philosophy (documented product stance): "**Reproducibility by Default**" — "Every execution becomes an **immutable, reproducible unit by default**"; automatic capture of **Git commit hash, Docker image digest, input file hashes, parameter values, execution command**; "Find the original execution in your history → click 'Create execution from this' → get identical results"; audit trail extends across chained pipelines. Companion pages: "YAML Over SDK", "Unifying Your ML Infra", "Let Data Scientists Be Scientists" (infra abstraction for data scientists).
- Documented machinery: **Executions** (steps: parameters, inputs, outputs, env vars; queue priority; spot instances; time limits; dynamic GPU allocation; custom execution status); **Pipelines** (chain jobs; per-node environments; data passing; execution reuse/caching; error handling; dynamic conditions; parallel runs); **Tasks** (grid search, Bayesian optimization, manual sweeps, early stopping); **Data** (S3/Azure/GCP/OVH/Oracle data stores; data versioning; datasets; tags/aliases/custom properties); **Models** ("Create and Manage Models"; "Model Artifacts & Versioning"); **Experiment Tracking** (collect metrics from PyTorch Lightning/TensorFlow/output files; visualize; compare executions); **Inference & Serving** (real-time endpoints: deploy/test/monitor/debug; batch inference); **Automation** (**triggers: scheduled and webhook; "Launch Pipelines with Webhooks"; notification triggers including model-version trigger and dataset-version trigger**; REST API; auto-fetch repository on push; launch executions on new S3 data); **Observability** (productivity dashboard, audit log, resource monitoring/hardware statistics); **Git integration** (executions bound to commits; manage commit visibility); **Notebooks** as executions (push to git; convert to production script); distributed training.
- Deployment shape: orchestrates execution **on the customer's own cloud/on-prem machines** — AWS/Azure/GCP/OCI, Kubernetes, on-premises Linux workers (with a Valohai agent), OpenShift, **SLURM**; hybrid deployments; self-hosted options.

### ClearML [A — overview layer]

- Self-definition: "the end-to-end platform for streamlining AI development and deployment", built of three layers:
  1. **Infrastructure Control Plane** (cloud/on-prem agnostic): "compute resource provisioning and management... GPUaaS"; resource management, workload autoscaling, monitoring/logging, cost optimization, cloud+on-prem compute (DevOps/IT-facing; agents & queues model).
  2. **AI Development Center**: integrated IDE; "scalable and distributed model training and hyperparameter optimization"; data management/versioning; "**Experiment Tracking: Track metrics, artifacts, and logs. Manage versions, and compare results**"; "**Workflow Automation: Build pipelines to formalize your workflow**".
  3. **GenAI App Engine**: "deploy large language models (LLM) into GPU clusters"; RAG workloads; networking/authentication/RBAC.
- **Platform Management Center**: administrative dashboard across tenants — activity, usage, costs.
- Gradient visible inside one product: agent/queue execution on user machines AND an optional compute control plane (GPUaaS) — machinery plus execution.

## Cross-product Comparison

| Structure | MLflow | W&B | Comet | Valohai | ClearML | Suites (sibling pass) | Evidence |
|---|---|---|---|---|---|---|---|
| Tracked run/experiment records (params, metrics, artifacts, code/data/environment refs) | Tracking (experiments, params, metrics, artifacts) | tracking/experiments, runs, artifacts | experiment management (log metrics/params/models/code/assets) | executions with automatic capture (commit, image digest, inputs, params, command) | "track metrics, artifacts, and logs" | Experiments (SageMaker), job artifacts (Azure), MLflow tracking (Databricks), experiments (Hopsworks) | 5/5 A + suites A |
| Versioned model records with lineage | Model Registry (versioning, automatic lineage) | "model registry for versioning and reproducibility" | Model Registry (versions, approval) | Models ("Model Artifacts & Versioning") | "manage versions" | Model Registry / Models in Unity Catalog / Hopsworks Model Registry | 5/5 A + suites A |
| Lifecycle promotion of model versions (stages/approval) | "staging, production, and archived stages"; review/approval workflows | registry versioning + aliases (docs-card level) | model approval + webhooks | model versioning; model-version triggers | (not fetched in depth) | SageMaker approval workflow; Databricks stage/test/promote | 4/5 A + suites A |
| Operationalization of registered versions | Deployment: "multiple deployment targets... REST APIs, cloud platforms, edge"; built-in REST serving; batch | Launch jobs to compute targets; Serverless Inference (preview) | "deploy registered models using your computing environment"; CI/CD webhooks | real-time endpoints + batch inference | GenAI App Engine deployment | endpoints/serving in all suites | 5/5 A |
| Automation machinery (triggers/schedules/queues/CI-CD) | not observed in OSS docs (weak) | Launch queues/agents; sweeps-on-launch | webhooks (CI/CD), service accounts for automated jobs | triggers (scheduled/webhook/model-version/dataset-version), REST API | workflow automation/pipelines; agents & queues | Projects CI/CD (SageMaker); Event Grid triggers (Azure); MLOps workflows (Databricks) | 4/5 A + 1 weak + suites A |
| Comparison/visualization surface | metric visualization, run comparison | workspace/reports/panels | project panels, single-experiment page, visualizations | visualize metrics; compare executions | compare results | run comparison everywhere | 5/5 A |
| Tenancy/org (projects/teams/RBAC) | collaboration/self-hosting, teams | teams, org management, workspaces | workspaces, admin dashboard, service accounts | organizations/teams/environments & access control, SSO | tenants, Platform Management Center | workspaces/projects/domains | 5/5 A |
| HPO / sweeps | not observed (evaluation yes, sweeps no) | sweeps (core card) | Optimizer | Tasks (grid/Bayesian/early stopping) | HPO | Autopilot/AutoML/Katib (suite-side) | 4/5 A — common |
| Production model monitoring module | not observed as OSS module | not observed in fetched pages | Production Monitoring (MPM) | endpoint monitoring | (monitoring/logging at infra layer) | Model Monitor (SageMaker), monitor-and-retrain (Databricks), Model Monitoring (Hopsworks) | 2/5 A in sample + suites A — optional/bundled |
| Git/code binding | (not fetched) | jobs from Git repos | log code | Git integration (commit-hash capture) | code captured via SDK (overview only) | Git integration (Azure) | 3/5 A — common |
| LLM/GenAI overlay | LLMs & Agents section (tracing, eval, prompts, AI gateway) | Weave | Opik | GenAI workflows docs | GenAI App Engine | model catalogs, prompt flow, FM APIs | 5/5 A — modern overlay |
| Own managed training compute | none | none (Launch drives customer infra; serverless preview) | none | orchestrates on customer cloud/on-prem (customer's machines) | agents on user machines + optional GPUaaS control plane | owned managed compute (SageMaker/Azure/Databricks/Hopsworks) | the gradient axis |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (jointly-held; removal-tested)

1. **The tracked run record.** Model-building and processing work is captured as recorded, comparable runs in a persistent, organization-shared record system — parameters, metrics, artifacts, and references to the code, data, and environment that produced them. The record is the lifecycle's memory: comparison, reproducibility, and audit all hang off it. Remove → deployment automation over invisible work (CI/CD/hosting territory); nothing ML-specific remains.
2. **The versioned model record with promotion.** Trained models are held as identified, versioned records — traceable to the run and data that produced them — advanced through defined lifecycle states (staging → production → archived, or approval gates) rather than overwritten. It is the object to which deployment and governance attach. Remove → a metrics tracker or a file store; the lifecycle object is gone.
3. **The operationalization bridge.** Machinery that moves registered model versions into production serving — built-in endpoints, deployment targets, or registry-triggered handoff (webhooks/CI-CD) into the organization's serving environment — with the deployed instance bound to the model version. Remove → an experimentation record system whose models never operationalize; the "Ops" is gone.

Jointly-held is load-bearing: 1 alone = experiment tracker / metadata store (below the Type); 2 alone = Model Registry (the sibling Type: record machinery alone); 3 alone = deployment tooling; 1+2 without 3 = the build-side record layer of an ML platform without the Ops; 1+3 without 2 = automation with no governed model object; 2+3 without 1 = manually operated registry+deployment with no reproducibility spine.

**Training execution is deliberately NOT in the core.** The clean poles (MLflow, Comet) run no training on their own compute and remain fully recognizable members of the Type; execution-orchestration poles (Valohai, ClearML agents, W&B Launch) drive training jobs on the **customer's** infrastructure; only the suite pole (SageMaker/Azure/Databricks/Hopsworks) owns managed training compute, and there the MLOps machinery is a named module group. This is the gradient axis separating MLOps Platform from Machine Learning Platform (whose L0 leg 1 is platform-executed training).

### L1 — Common Mature Structure (very common; not definitional)

- comparison/visualization surfaces over runs (charts, run diffing, reports)
- automation machinery: triggers (schedules, webhooks, data/model-version events), job queues/agents, CI/CD integration
- approval/review workflows around promotion (gates before production)
- tenancy containers (workspace/project/org/team) with RBAC and SSO at the enterprise pole
- HPO/sweeps machinery
- Git/code binding on runs and jobs
- SDK/CLI/API parity with the UI; offline/local logging modes (observed in two products' SDK docs)
- audit logs and resource/usage observability
- environment/Docker machinery (image digests, environment capture)
- production model monitoring as a module (bundled in suites; standalone module in Comet; absent from the OSS record-machinery pole)

### L2 — Variant / Optional Structure

- packaging pole: standalone SaaS machinery vs OSS embeddable record machinery vs execution-orchestration commercial platform vs suite-embedded module group
- execution substrate: none vs customer-infra orchestration (agents/workers) vs owned managed compute (suite pole)
- operationalization substrate: built-in serving vs deployment targets vs registry-triggered handoff into the org's own serving/CI-CD
- deployment posture: SaaS, self-hosted/VPC/on-prem, hybrid, on-prem workers/SLURM
- LLM/GenAI-ops extensions (tracing, evaluation, prompt management, AI gateways) as a modern overlay across all five sampled products
- migration tooling (cross-platform metadata import), service accounts for machine users

### L3 — Vendor-specific (research notes only)

- MLflow: flavors/autologging, stage vocabulary, self-hosting packaging, Databricks-hosted variant with jobs; "30M monthly downloads" marketing stat
- W&B: Launch queue/agent/Kaniko machinery, sweeps semantics, Weave, CoreWeave-powered serverless products, MCP server/skills
- Comet: Optimizer, Python panels/visualization library, MPM SDK, "Load data from Neptune" migration, service accounts
- Valohai: valohai.yaml (YAML-over-SDK philosophy), execution immutability guarantee, service buttons, reusable step libraries, SLURM support, dynamic GPU allocation
- ClearML: GPUaaS control plane, GenAI App Engine, Platform Management Center, agents & queues model

## Rejected Findings

- "MLOps Platform = Machine Learning Platform under another name" — rejected: MLflow and Comet fail the ML platform's defining leg (platform-executed model training) yet are central members of the MLOps-labeled population; the resolution is a gradient (machinery center vs execution center), not an alias.
- "MLOps Platform = the practice/discipline, not a product" — rejected: the market ships concrete products under the label; the discipline (record, version, promote, automate) is implemented BY the machinery. The ML-platform pass's framing ("MLOps names the lifecycle-automation discipline implemented on the platform") is refined here: the discipline has its own product population whose center is exactly that machinery.
- "MLOps Platform = CI/CD for models" (automation-only definition) — rejected: the OSS archetype (MLflow) ships no trigger machinery in its core docs; automation is common structure, not the invariant.
- "MLOps Platform = model monitoring" — rejected: monitoring appears as a module (Comet MPM, suite Model Monitor) or is absent (MLflow OSS, W&B fetched pages); the watch loop is the sibling Type's center.
- "MLOps Platform = experiment tracking" — rejected: tracking alone is below the Type; every full member adds versioned model records + operationalization.
- "MLOps requires built-in serving" — rejected: operationalization is realized through deployment targets (MLflow), customer-environment deployment (Comet), launch jobs (W&B) as well as built-in serving (Valohai); the bridge is the invariant, the substrate is variant.

## Boundary Findings

1. **vs Machine Learning Platform (processed) — DISCHARGES that pass's forward flag (b), the sharpest seam.** Resolution: **keep-both as gradient siblings**, analogous to the hosting resolution. Machine Learning Platform's defining core = platform-executed training + model artifact of record + deployment bridge (execution center). MLOps Platform's defining core = tracked run records + versioned/promoted model records + operationalization bridge (machinery center) — training execution neither required nor excluded, and when present it runs on the customer's infrastructure (Valohai/ClearML/W&B Launch) rather than owned managed compute. Removal tests both directions: strip the MLOps machinery from a suite → a managed training/serving service remains (ML platform); strip managed training execution from an MLOps platform → the record-and-operationalization loop remains intact (MLflow/Comet prove it). Suites straddle (SageMaker/Azure/Databricks/Hopsworks bundle the machinery as named "MLOps" module groups); the machinery-only pole does not straddle. Label evidence: MLflow docs frame the tooling as "MLOps" (A, this pass); suite vendors use MLOps as the automation/practice framing of their platforms (A, sibling pass).
2. **vs ML Model Monitoring Platform (processed) — DISCHARGES that pass's forward flag** ("expect monitoring named as a bundled capability there too"): confirmed. Monitoring appears as a bundled module (Comet Production Monitoring; suite Model Monitor/monitor-and-retrain; Valohai endpoint monitoring) and is absent from the OSS record-machinery pole's core. The dedicated watch-loop Type keeps its own leaf; keep-both holds.
3. **vs Model Registry (unprocessed) — forward flag.** The registry is the record machinery alone (model versions, stages, approvals as the object-of-record system); in every sampled MLOps platform it appears as an embedded component (MLflow Model Registry, W&B model registry, Comet Model Registry, Valohai Models, suite registries). Recommended: keep-both with the object-of-record split (registry machinery vs the record-and-operationalization loop around it); joint review when that leaf is processed.
4. **vs Data Science Workbench (processed) — consistent, no flag.** The workbench's center is the interactive session; workbench sessions and notebooks feed runs INTO the MLOps record system (notebooks-as-executions in Valohai; notebook logging in Comet; jobs from Git/W&B). The workbench pass's framing ("downstream operationalization/governance machinery") is confirmed from this side.
5. **vs DataOps Platform (processed) — consistent, no flag.** DataOps centers data pipelines as the managed object; MLOps centers the model lifecycle records/loop. Same pass's own boundary entry already recorded this seam from the other side.
6. **vs AI Model Hosting Platform (processed) — consistent, no flag.** Hosting centers platform-operated serving for consumption; MLOps operationalization may be realized through deployment targets and registry-triggered handoff without the platform operating the serving substrate. Gradient noted in that pass already ("ML/MLOps platforms span data/training/pipelines/deployment/monitoring").
7. **vs Continuous Integration / Continuous Delivery platforms (§12) — consistent, no flag.** CI/CD manages software code artifacts (build/test/release of the codebase); MLOps platforms integrate WITH CI/CD (webhooks, pipeline triggers) while their own center is the model record loop. No sampled MLOps product manages general code CI.
8. **vs Feature Store (processed) — consistent, no flag.** Feature-data layer vs lifecycle loop machinery; the feature-store pass recorded this seam from its side ("automation-of-lifecycle vs feature-data layer consumed by it"). Dataset-version artifacts and dataset-version triggers in sampled products are record/automation objects, not feature-value stores.
9. **vs AI Governance Platform (processed) — consistent, no flag.** Governance registries hold business/risk/legal context and review state; MLOps registries hold technical artifact records with lineage. The governance pass recorded the seam ("technical artifact store in MLOps vs governance registry").

Boundary test (the "remove → becomes another Type" checks): remove the run-record spine → CI/CD/deployment tooling; remove the versioned model record → an experiment tracker (below the Type); remove operationalization → the build-side record layer (registry+tracking slice); add platform-executed training on owned compute → Machine Learning Platform territory.

## Historical / Market-Sample Check (§24)

- The "MLOps" name is era machinery (coined ~2018-2019 in the sample's own framing); the structure is not. Treating models like software releases — record what ran, version the artifact, promote through stages, deploy the version, keep the loop running — is the classical model-management lineage: recorded training runs in shared logs, versioned artifact stores with staged promotion, scheduled deployment/retraining pipelines. A pre-cloud, pre-label setup with a metrics log + versioned artifact store + staged promotion + scheduled deploy pipeline satisfies all three legs (held at conceptual strength — the lineage products predate the label and were not directly fetched).
- The definition names no cloud, Kubernetes, Git, Python, SDK, Docker, SaaS, or dashboard. A Git-free, Python-free realization of the same three legs would still satisfy them.
- MLflow's own "vendor-neutral, runs anywhere" framing and Valohai's on-prem/SLURM support document that the Type is not bound to a deployment shape.
- Check passed.

## Uncertainties

- ClearML evidence held at overview-layer depth; its registry depth and model-repository specifics not fetched — claims about ClearML limited to its overview statements.
- MLflow OSS automation machinery (schedules/triggers) not observed in fetched pages — automation held common (4/5 A + suites), not definitional.
- W&B production model monitoring not observed in fetched pages — not claimed for W&B.
- Neptune, ZenML, cnvrg, Domino, Iguazio not sampled — the five-product sample already repeats the same three-leg core with clean poles on the gradient; stop condition reached.
- Vertex AI and DataRobot were unreachable in the sibling pass (recorded limitation) and were not re-attempted here per the network-restricted rule; no claims made about them.
- Valohai's marketing self-label ("MLOps platform") not verified from the docs layer — label claims held general rather than vendor-verbatim.

## Final Synthesis

The MLOps Platform is the organization's record-and-loop machinery for its models: it captures model-building and processing work as recorded, comparable runs; holds the resulting models as versioned records promoted through lifecycle states; and bridges chosen versions into production serving — with the whole path kept reproducible and auditable by the record spine, and the loop kept running by automation machinery. It is defined against the Machine Learning Platform not by scope but by center of gravity: the ML platform's center is executing model-building on managed compute; the MLOps platform's center is the record, promotion, and operationalization machinery, which runs with or without any owned compute (MLflow and Comet prove the pole; Valohai/ClearML/W&B Launch drive execution on the customer's infrastructure; suites bundle the machinery as their "MLOps" module group). Everything else the market associates with the label — comparison dashboards, triggers and queues, approvals, tenancy, sweeps, monitoring modules, GenAI surfaces — is standard or variant structure around that three-part core.
