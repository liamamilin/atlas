# Research Notes — Machine Learning Platform

Research date: 2026-09-08
Directory leaf: Machine Learning Platform (§13 Data, Analytics & AI Systems)
Slug: machine-learning-platform

## Research Goal

Understand what a "Machine Learning Platform" actually is as an Application Type: what the central objects are (training runs? models? endpoints?), what the platform itself does versus what it merely hosts or connects, who operates it, how the model lifecycle flows, and where the boundary lies against the densely packed §13 sibling space (Data Science Workbench, Feature Store, Model Registry, MLOps Platform, AI Model Hosting Platform, Data Labeling Platform, AI Model Evaluation Platform).

## Initial Boundary

- Hypothesis: an ML platform is the end-to-end environment for an organization's own models — build (train) and operate (deploy/monitor) joined by a model record.
- Likely confusions: the workbench leaf (interactive session), the feature-store leaf (feature-data layer), the hosting leaf (serving-only center), the registry leaf (record machinery), the MLOps leaf (lifecycle automation), AutoML tools, general pipeline orchestration.
- Pending sibling flags to discharge from prior passes: data-science-workbench (embedded session = module, keep-both), feature-store (module boundary, keep-both), ai-model-hosting (lifecycle-breadth gradient), data-labeling (no overlap of centers).

## Research Questions

1. What are the core objects the platform manages (workspace/project, data, training runs, models, endpoints, pipelines)?
2. What exactly does the platform execute, and what does it only record or connect?
3. How does a model move from training to operational serving? What states does it pass through?
4. What is tracked and what is the record (runs, metrics, artifacts, lineage)?
5. Who uses it and on which surfaces (studio UI, notebooks, SDK/CLI, pipeline DSL, admin consoles)?
6. Which capabilities are definitional vs module/optional (feature store, workbench, labeling, AutoML, monitoring, LLM surfaces)?
7. Where is the seam against each §13 sibling, with removal tests both directions?
8. Would older / non-cloud / differently positioned products still fit the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Amazon SageMaker AI | hyperscaler managed suite; code-first + no-code (Canvas/Autopilot) | market-defining managed platform; deep docs |
| Azure Machine Learning | hyperscaler managed service; workspace/assets/jobs/endpoints object model | explicit role model and lifecycle documentation |
| Databricks (ML) | lakehouse-embedded platform; notebooks + MLflow center | documents a market-side definition of "What is an ML platform?" |
| Kubeflow | self-managed, open-source, Kubernetes-native composable stack | the no-cloud / not-SaaS pole; modules usable independently |
| Hopsworks | feature-store-first modular data platform for ML | in-product demonstration of module boundaries (standalone FS vs full platform) |

Dropped: DataRobot (AutoML SaaS pole) — docs.datarobot.com returned HTTP 403; excluded without claims (see Uncertainties). Google Vertex AI — cloud.google.com timed out twice; excluded without claims.

## Sources

- AWS — What is Amazon SageMaker AI: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
- AWS — Overview of machine learning with SageMaker AI: https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html
- AWS — SageMaker AI Features: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis-features.html
- Microsoft — What is Azure Machine Learning: https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning
- Databricks — Machine learning on Databricks: https://docs.databricks.com/aws/en/machine-learning/index.html
- Databricks — Concepts: DS and ML on Databricks (incl. "What is an ML platform?"): https://docs.databricks.com/aws/en/machine-learning/concepts/
- Kubeflow — Introduction: https://www.kubeflow.org/docs/started/introduction/
- Kubeflow — Trainer Overview: https://www.kubeflow.org/docs/components/trainer/overview/
- Hopsworks — Documentation home (platform, MLOps, projects): https://docs.hopsworks.ai/latest/

All fetched 2026-09-08. Tier-1 operational documentation throughout (developer guides / docs portals). No Tier-3 sources needed. Google Vertex AI and DataRobot unreachable — recorded as source-access limitations.

## Product Observations

### Amazon SageMaker AI [A: directly observed]

- Self-definition: "a fully managed machine learning (ML) service" for data scientists and developers to "build, train, and deploy ML models into a production-ready hosted environment"; "store and share your data without having to build and manage your own servers"; "managed ML algorithms"; "bring-your-own-algorithms and frameworks"; "flexible distributed training options".
- Canonical workflow (docs' own three stages, circular): Generate example data → Train a model → Deploy the model; after deployment: monitor inferences, collect more data, evaluate drift, retrain. Data prep via SDK/Processing jobs; evaluation via SDK; deployment via "hosting services... deploy your model independently, which decouples it from your application code".
- Training: built-in algorithms or user containers; compute "ranging from a single general-purpose instance to a distributed cluster of GPU instances"; training jobs are the unit (HyperPod recipes run "as SageMaker training jobs"; training plans reserve compute "for... training jobs and HyperPod clusters").
- Component list (features page, verbatim fragments): Studio ("the web-based experience for running ML workflows... suite of IDEs": Code Editor/Code-OSS, JupyterLab, RStudio), Canvas ("an auto ML service... no coding experience"), Autopilot (AutoML), Experiments ("experiment management and tracking... reconstruct an experiment... trace model lineage for compliance and audit"), Feature Store (online/offline), Ground Truth (labeling), Data Wrangler, Model Building Pipelines ("integrated directly with SageMaker AI jobs"), Model Registry ("versioning, artifact and lineage tracking, approval workflow, and cross account support for deployment"), Model Monitor ("monitor and analyze models in production (endpoints) to detect data drift and deviations in model quality"), Model Cards / Model Dashboard / Clarify (governance), Batch Transform (batch inference), Serverless Endpoints, Inference Recommender, shadow tests, Processing (preprocess/feature engineering/evaluate), Notebook-based Workflows ("run your Studio notebook as a non-interactive, scheduled job"), Projects (CI/CD), Role Manager ("least-privilege permissions for common ML activities... persona-based"), JumpStart (pretrained models; fine-tune and deploy), Edge Manager/Neo (edge), Augmented AI (human review).
- 2024 rename: SageMaker → SageMaker AI; next-generation "Amazon SageMaker" = unified data/analytics/AI platform umbrella (Lakehouse, Catalog, SQL analytics, Data Processing, Unified Studio, Bedrock).

### Azure Machine Learning [A]

- Self-definition: "a cloud service for accelerating and managing the machine learning (ML) project lifecycle. ML professionals, data scientists, and engineers use it in their daily workflows to train and deploy models and manage machine learning operations (MLOps)."
- Audience framing: "individuals and teams implementing MLOps within their organization to bring ML models into production in a secure and auditable production environment". Roles: data scientists/ML engineers (accelerate daily workflows), application developers (integrate models into apps), platform developers (build ML tooling on ARM APIs), enterprises (RBAC, deny access to protected data).
- Studio authoring: managed Jupyter notebooks; run-metrics visualization; Designer ("drag and drop datasets and components to create ML pipelines... train and deploy ML models without writing any code"); AutoML UI; data labeling (image/text projects).
- Workspace: "a workspace organizes a project and allows for collaboration"; shared notebooks/compute/serverless compute/data/environments; "versioned assets for jobs like environments and storage references"; operationalization via "an ML pipeline... triggered on a schedule or HTTPS request"; "managed inferencing solution, for both real-time and batch deployments, abstracting away the infrastructure management".
- Train: "run your training script in the cloud or build a model from scratch"; open frameworks (PyTorch, TensorFlow, scikit-learn, XGBoost, LightGBM, R, .NET); AutoML = "automated featurization and algorithm selection"; HPO; multinode distributed training on clusters/serverless GPU; embarrassingly parallel patterns.
- Deploy: managed endpoints for real-time (HTTPS, "traffic can be split across multiple deployments, allowing for testing new model versions") and batch (asynchronous jobs on compute clusters).
- MLOps framing: "A model's lifecycle from training to deployment must be auditable if not reproducible"; Git integration; MLflow integration; pipeline scheduling; Event Grid triggers; CI/CD (GitHub Actions/Azure DevOps); "job artifacts, such as code snapshots, logs, and other outputs"; "lineage between jobs and assets, such as containers, data, and compute resources".
- LLM/GenAI bundle: model catalog (Azure OpenAI, Mistral, Meta, Cohere, NVIDIA, HF...), prompt flow; note: "Both Azure Machine Learning studio and Microsoft Foundry allow you to work with LLMs".

### Databricks (ML) [A]

- Self-definition: "The integrated platform unifies the entire ML lifecycle from data preparation to production monitoring."
- The docs' own 8-stage ML lifecycle: scope use case → EDA → prepare data and features (managed within a feature store) → train models and track experiments (logging experiment metadata "for analysis and for deployment") → evaluate → "register, stage and test models before promoting to production" → "deploy to production in real-time endpoints or batch inference jobs" → "monitor and retrain".
- In-doc definition of the Type itself: "An ML platform is the combined infrastructure, tooling, and governance layer that supports the full ML lifecycle, from raw data to production models. A well-designed ML platform connects data engineering, interactive data science and production ML in a single governed system." Key components listed: data assets (files, tables, processing pipelines, feature stores); experimentation tools (notebooks, visualizations, AI assistance); training infrastructure (customizable environments, flexible compute); deployment and monitoring infrastructure (batch and real-time serving, production dashboards and alerts); MLOps and governance tools (orchestration, CI/CD, lineage, access management, audit logging).
- Modules observed: Feature Store (in Unity Catalog), Databricks Runtime for ML, AI Runtime (serverless GPU), distributed training examples, Ray, MLflow tracking ("track experiments, compare model performance, and manage the complete model development lifecycle"), Model Serving ("deploy custom models and LLMs as REST endpoints with automatic scaling and GPU support"), AI Gateway (govern endpoints), Batch inference, Foundation Model APIs ("hosted by Databricks"), Models in Unity Catalog ("model registry in Unity Catalog for centralized governance and to manage the model lifecycle, including deployments"), Lakeflow Jobs (automated workflows for ML pipelines), MLOps workflows (automated training, testing, deployment), Unity Catalog governance (data, features, models, functions; lineage), data profiling/anomaly detection.
- AI assistance: Genie Code across notebooks/workspace (development, debugging, operations, endpoint analysis).

### Kubeflow [A]

- Self-definition: "the Cloud Native AI platform... modular, open source projects that form the Kubernetes-native stack for data & AI workloads"; mission: "deliver more models, agents, and AI applications into production with well-lit paths across the AI lifecycle"; principles: Simple / Portable ("local laptop, on-premises, or any cloud") / Scalable / Composable ("mix and match tools across the AI lifecycle").
- Subprojects "designed to be usable both independently and as part of the Kubeflow Distribution": Notebooks (Jupyter), Workspaces, Trainer, Katib, Pipelines, Dashboard (profiles/namespaces), Hub (Model Registry + Model Catalog), Spark Operator, SDK, MCP server.
- Trainer: "Kubernetes-native distributed AI platform for scalable large language model (LLM) fine-tuning and training of AI models across a wide range of frameworks" (PyTorch, MLX, HuggingFace, DeepSpeed, JAX, XGBoost); APIs = "TrainJob and Runtimes"; personas: AI Practitioners (ML engineers/data scientists "develop AI models using the Kubeflow Python SDK and TrainJob") and Platform Administrators ("managing Kubernetes clusters and Kubeflow Training Runtimes").
- Pipelines concepts: Pipeline, Component, Graph, Experiment, Run and Recurring Run, Step, Output Artifact, IR YAML, ML Metadata (run/artifact tracking).
- Serving and features are ecosystem: KServe ("ecosystem" — model serving), Feast ("ecosystem" — feature store). Model Registry is a Hub subproject (with its own UI REST API, Python client, Model Catalog REST API).
- History: "started as an open sourcing of the way Google ran TensorFlow internally, based on a pipeline called TensorFlow Extended. It began as just a simpler way to run TensorFlow jobs on Kubernetes."

### Hopsworks [A]

- Self-definition: "a data platform for ML with a Python-centric Feature Store and MLOps capabilities. Hopsworks is a modular platform. You can use it as a standalone Feature Store, you can use it to manage, govern, and serve your models, and you can even use it to develop and operate feature, training and inference pipelines."
- MLOps chain (docs' own diagram flow): Experiments & Model Training → Model Registry → Model Serving; Prediction services (operational ML / analytical ML); Model Monitoring; Vector DB (OpenSearch); BI tools.
- Execution machinery: Jobs = "a Jupyter notebook, a python script or a jar" (Python/PySpark/Spark/Ray jobs, schedulable); FTI (feature/training/inference) pipeline architecture orchestrated with bundled Airflow; JupyterLab bundled; "train models on as many GPUs as are installed in a Hopsworks cluster"; Python environments per pipeline stage.
- Registry/serving detail: Model Registry frameworks (TensorFlow/Torch/scikit-learn/LLM/Python), import from HuggingFace, model schema; Model Serving via KServe: deployment creation, deployment state, predictor/transformer, inference logger/batcher, autoscaling, REST API.
- Tenancy: "projects as a secure sandbox in which teams can collaborate and share ML assets"; multi-tenant project model; dev/staging/prod via projects; "All ML assets support versioning, lineage, and provenance... complete view of the MLOps life cycle, from feature engineering through model serving."
- Deployment: k8s in AWS/Azure/GCP, on-prem, air-gapped; serverless option.

## Cross-product Comparison

| Structure | SageMaker | Azure ML | Databricks | Kubeflow | Hopsworks | Evidence |
|---|---|---|---|---|---|---|
| Managed training execution on platform compute | training jobs; built-in algo or own container; distributed GPU | jobs ("run your training script in the cloud"); clusters/serverless | Runtime for ML clusters; AI Runtime serverless GPU | Trainer TrainJob + Runtimes; KFP steps | Jobs (notebook/python/spark/ray) on cluster GPUs | 5/5 A |
| Build runs recorded (params/metrics/artifacts) | Experiments; lineage tracking | job artifacts (code snapshots, logs); lineage jobs↔assets | MLflow tracking | KFP Experiments/Runs + ML Metadata | experiments/training records; provenance | 5/5 A |
| Persisted model artifact, commonly versioned/registered | Model Registry (versioning, artifact+lineage, approval workflow) | MLflow; lineage to producing jobs | Models in Unity Catalog ("model registry... manage the model lifecycle, including deployments") | pipeline artifacts in object store; Model Registry subproject (optional) | Model Registry (versions, frameworks, schema) | 5/5 A ("commonly registered": Kubeflow registry optional) |
| Deployment bridge: real-time endpoints and/or batch | endpoints/serverless/batch transform | managed endpoints (online+batch) | Model Serving REST endpoints + batch inference | KServe (ecosystem) | KServe deployments + batch | 5/5 A (Kubeflow via ecosystem project) |
| Deployment bound to model record (version updates/rollback, traffic split) | shadow tests; dashboard integrates endpoints+monitor | "traffic can be split across multiple deployments... testing new model versions" | registry manages "the model lifecycle, including deployments" | KServe revisions (not fetched in detail — held weak) | deployment state machine on model | 4/5 A + 1 weak |
| Pipelines/orchestration of the ML workflow | Model Building Pipelines | ML pipelines, scheduled/event-triggered | Lakeflow Jobs; MLOps workflows | Pipelines (center) | Airflow/FTI | 5/5 A |
| Embedded interactive dev surface (notebooks/IDE) | Studio suite of IDEs; notebook jobs | studio notebooks | notebooks (primary DS/ML tool) | Notebooks subproject | JupyterLab | 5/5 A (module everywhere) |
| Feature/data layer attached | Feature Store module | data assets + labeling | Feature Engineering in Unity Catalog | Feast (ecosystem) | Feature Store (center) | 5/5 A (definitionally optional) |
| Production model monitoring | Model Monitor (drift, quality) | monitor/retrain/redeploy framing | monitor and retrain stage; data profiling | not a core subproject | Model Monitoring | 4/5 A |
| Tenancy container | domain/shared spaces | workspace | workspace + Unity Catalog | profiles/namespaces | projects | 5/5 A |
| AutoML / no-code build | Autopilot, Canvas | AutoML + Designer | not verified in fetched pages | Katib (HP tuning/NAS only) | not observed | 2/5 A — common-to-optional |
| Governance extras | Model Cards, Clarify, Role Manager, Model Dashboard | RBAC, secure workspace, Purview integration | AI Gateway, Unity Catalog, audit | multi-user isolation | governance page, audit logs | 5/5 A (module depth varies) |
| LLM/foundation-model surfaces | JumpStart, HyperPod | model catalog, prompt flow | Foundation Model APIs, AI Runtime | Trainer LLM fine-tuning | LLM framework, HF import | 5/5 A (modern overlay) |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (jointly-held; removal-tested)

1. **Platform-executed model training.** The platform provisions and operates the compute on which model-building runs execute — from user-authored training code, automated model search, or pipeline steps — over data the organization connects to it. The build run is a platform-managed, recorded unit (job/run/experiment), not merely an ad-hoc script in a personal session. Remove → serving/hosting of models built elsewhere (AI Model Hosting / Model Registry territory), or a bare data/experiment layer.
2. **The trained model as the held unit of record.** The output of a build run is persisted by the platform as an identified model artifact — commonly versioned and registered — that outlives the run, is traceable to the run/data that produced it, and is the object to which registration, promotion, deployment, and governance attach. Remove → a run farm / experiment tracker with no held model object; also separates from Feature Store (feature-data records) and Data Science Workbench (session with no lifecycle object).
3. **The deployment bridge into prediction service.** The platform moves held models into serving surfaces — real-time prediction endpoints and/or batch scoring jobs — that applications consume, with the deployed instance bound to the model record (updates/rollbacks reference artifact versions). Remove → a build/experimentation environment whose models never reach operations.

Jointly-held is load-bearing: 1 without 2 = a job runner; 2 without 1 = a model registry; 3 without 1+2 = hosting; 1+2 without 3 = experimentation platform; 2+3 without 1 = manually stitched registry+hosting.

Supporting span evidence: every product's self-definition covers build AND deploy (SageMaker "build, train, and deploy"; Azure "train and deploy models and manage MLOps"; Databricks "from data preparation to production monitoring"; Kubeflow "deliver more models... into production"; Hopsworks "develop and operate feature, training and inference pipelines").

### L1 — Common Mature Structure (very common; not definitional)

- experiments/run tracking with parameters, metrics, artifacts; comparisons
- model registry machinery: versions, stages/approval workflows, lineage
- ML pipelines/orchestration (scheduled/event-triggered; train→register→deploy→retrain)
- embedded interactive development surfaces (notebooks/IDEs) as modules
- tenancy containers (workspace/project/domain/profile) with sharing and RBAC
- real-time + batch serving options; traffic splitting; autoscaling
- production model monitoring (drift, quality) feeding retrain
- environments (dependency/containers) and compute elasticity (distributed training, GPU)
- lineage/audit/reproducibility machinery; CI/CD integration
- SDK/CLI/API parity with the UI

### L2 — Variant / Optional Structure

- build philosophy: code-first vs AutoML/no-code (Canvas/Designer-class) — poles coexist in one market
- feature/data layer: embedded feature store vs external (Feast/KServe as integrations) vs none
- data labeling embedded (Ground Truth/Azure labeling) vs external
- deployment substrate: vendor-managed cloud vs self-managed Kubernetes/on-prem (even air-gapped)
- LLM/foundation-model surfaces: model catalogs, hosted FM APIs, fine-tuning scale-out (HyperPod-class), prompt tooling
- edge deployment, human-review loops, model cards/governance depth, AI assistants
- open-source community governance vs commercial SaaS; serverless vs cluster provisioning

### L3 — Vendor-specific (research notes only)

- SageMaker: HyperPod, training plans, Partner AI Apps, JumpStart, Inference Recommender, shadow tests, Batch Transform, Data Wrangler, Studio domains/shared spaces, neo/Edge Manager
- Azure ML: Designer drag-drop canvas specifics, prompt flow, model catalog providers, ARM/Event Grid integration, Microsoft Foundry overlap note
- Databricks: Unity Catalog as unified governance spine, AI Gateway for endpoints, Genie Code, Lakeflow Jobs, Foundation Model APIs
- Kubeflow: KFP component/IR YAML/ML Metadata specifics, Katib NAS, Kueue/JobSet/LWS integrations, Profiles, CNCF graduation (2026)
- Hopsworks: FTI pipeline naming, RonDB online store, OpenSearch vector DB, bundled Airflow/Superset, project multi-tenancy model

## Rejected Findings

- "ML platform = feature store + registry + serving" — rejected as definition: Kubeflow runs training with serving only via an ecosystem project, and Hopsworks can operate as a standalone feature store; the components are packaging, not the Type.
- "ML platform = notebook environment" — rejected: notebooks are an embedded module; SageMaker/Azure/Databricks/Kubeflow all execute managed runs without any session.
- "ML platform = managed endpoints" — rejected: that is the hosting slice; every sampled platform's center includes building the models.
- "ML platform = AutoML" — rejected: only 2/5 sampled products lead with AutoML; code-first is equally primary.
- "ML platform = MLOps discipline" — rejected as definition: MLOps is the vendors' name for lifecycle practices implemented on the platform; the platform is the concrete system, the discipline a framing (forward flag vs the MLOps leaf).
- "A pipeline orchestrator is an ML platform" — rejected: pipelines are one structure inside the lifecycle; KFP alone is usable independently as tooling.

## Boundary Findings

1. **vs Data Science Workbench (processed) — DISCHARGES that pass's flag.** Removal tests both directions recorded there and reconfirmed here: strip the interactive session → SageMaker/Azure/Databricks remain (training jobs, pipelines, registry, endpoints); strip lifecycle machinery → the workbench remains. SageMaker Studio self-describes as "the web-based experience for running ML workflows" hosting IDEs, and Databricks notebooks are "the primary tool" — in both, the session is a surface INTO the platform's managed machinery. Embedded workbench = standard module; keep-both ratified from this side.
2. **vs Feature Store (processed) — DISCHARGES that pass's flag.** Feature store = the feature-data layer; ML platform = the lifecycle platform around models. Hopsworks self-documents the seam in one product ("standalone Feature Store... or... manage, govern, and serve your models"). Strip the feature layer → an ML platform remains (Kubeflow + Trainer without Feast; SageMaker without Feature Store); strip training/deployment → the feature store remains. Keep-both ratified.
3. **vs AI Model Hosting Platform (processed) — DISCHARGES that pass's flag.** Hosting centers on operating serving for consumption (often of models it did not build); the ML platform centers the build lifecycle joined to serving. Hosting without any training still satisfies hosting (recorded in that pass); an ML platform without the deployment bridge fails this Type. Bundling runs both directions (hosting platforms bundle training; platforms bundle hosting) — gradient, keep-both.
4. **vs Model Registry (unprocessed) — forward flag.** The registry is the record-keeping machinery (versions, stages, approvals) as its own object-of-record system; in every sampled platform it appears as an embedded component (SageMaker Model Registry, Models in Unity Catalog, Hopsworks Model Registry, Kubeflow Hub Model Registry). Recommended: keep-both with the object-of-record split (registry machinery vs the lifecycle platform around it); joint review when that leaf is processed.
5. **vs MLOps Platform (unprocessed) — forward flag.** Every sampled product uses "MLOps" as the practice/capability framing (Azure: "train and deploy models and manage MLOps"; Databricks: "MLOps workflows"; Hopsworks: MLOps section covering registry/serving/monitoring). From this side: the ML platform is the concrete build-and-operate system; MLOps names the lifecycle-automation discipline/machinery implemented on it. The leaves overlap heavily in market labels — recommend joint review when the MLOps leaf is processed; possible gradient resolution analogous to hosting.
6. **vs Data Labeling Platform (processed) — DISCHARGES that pass's flag.** Labeling platforms manage the annotation production workflow; embedded labeling (SageMaker Ground Truth, Azure data labeling) is a module feeding training data into the platform. No overlap of centers; removal test passes.
7. **vs AI Model Evaluation Platform (processed) — consistent, no flag.** Evaluation evaluates MARKET AI models with standardized instruments; the ML platform tracks and evaluates the organization's OWN models through build runs. In-platform evaluation machinery is a capability, not the evaluation Type's center.
8. **vs ETL / orchestration platforms (§13):** ML-platform pipelines are ML-lifecycle-scoped (train→register→deploy→retrain); general data pipeline orchestration is a sibling's center. Kubeflow Pipelines is usable independently — gradient noted; no flag.
9. **vs LLM Application Development Platform (§13):** dev platforms build applications over consumed foundation models; ML platforms build the organization's own models (fine-tuning is training). Model catalogs/hosted FM APIs inside ML platforms are the hosting slice. Consistent with the hosting pass's framing; no new flag.

Boundary test (the "remove → becomes another Type" checks): remove training+artifacts → Data Science Workbench; remove lifecycle, keep feature-data layer → Feature Store; remove build side → AI Model Hosting; remove build+operate, keep record machinery → Model Registry.

## Historical / Market-Sample Check (§24)

- The definition names no cloud, notebook, container, Kubernetes, Python, GPU, AutoML, feature store, or LLM. A pre-cloud, server-based model-building environment — one that executed recorded model-building runs over connected data on centrally managed compute, held the resulting models as registered artifacts, and deployed them for scoring into operational applications — satisfies all three legs. The classical enterprise data-mining/model-management lineage (build → register → deploy for scoring) matches this shape; not directly fetched, held at canonical-inference strength.
- Kubeflow's own history note ("began as just a simpler way to run TensorFlow jobs on Kubernetes") documents the minimal-pole end: managed training + artifact flow + serving, no registry UI, no feature store, no monitoring — still recognizably the Type.
- AutoML is era- and philosophy machinery (2/5 sampled poles); notebooks are module machinery; both fail the historical test as definitional claims.
- Check passed.

## Uncertainties

- Google Vertex AI unreachable (cloud.google.com timeouts ×2) — the third-hyperscaler pole is unsampled; no GCP-specific claims made anywhere; "hyperscaler" breadth rests on AWS + Azure evidence only.
- DataRobot unreachable (docs 403) — the pure-AutoML SaaS pole is unsampled; AutoML evidence is from SageMaker/Azure docs only; no claims about AutoML-led vendors' registries/serving depth.
- Databricks AutoML not verified in fetched pages — not claimed for Databricks.
- Kubeflow serving internals (KServe revision semantics) not fetched — traffic-split/rollback claim held weak for Kubeflow, asserted from Azure (A) and Hopsworks deployment states (A) plus SageMaker shadow tests (A).
- Per-product numeric limits, instance types, pricing, state-name taxonomies deliberately not asserted.
- Third-party/community ML platforms (Domino, Iguazio, Algorithmia-lineage) not sampled — the five-product sample already repeats the same three-leg core; stop condition reached.

## Final Synthesis

The Machine Learning Platform is the organization's system for its own models: it executes model-building on compute it manages, holds the resulting models as governed, versioned artifacts traceable to their runs, and bridges them into prediction serving that applications consume — then keeps them current through monitoring and retraining. Everything else the market bundles — notebooks and IDEs, feature stores, labeling, AutoML, pipelines, registries, monitoring, governance, foundation-model surfaces — is mature structure arranged as modules, and the packaging philosophy (hyperscaler suite, lakehouse-embedded, self-managed composable stack, feature-store-first) is variant, not identity. The seams are real and removal-tested: the interactive session is the Workbench's center; the feature-data layer is the Feature Store's; serving-for-consumption alone is Hosting; record machinery alone is Registry. The platform is what remains when all of those are stripped away and training, model record, and deployment bridge still stand.
