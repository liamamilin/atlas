# Research Notes — Data Science Workbench

## Research Goal

Understand what a Data Science Workbench actually is as an Application Type: what its defining structure is, what mature products add on top, where it ends and neighboring Types (Machine Learning Platform, BI Platform, SQL Workbench, Cloud IDE) begin, and how the category is realized across very different packaging philosophies (open-source tool, platform-embedded module, hyperscaler suite, enterprise governance platform, modern collaborative SaaS).

## Initial Boundary

Working hypothesis before research:

- A Data Science Workbench is an interactive, code-first environment where data scientists explore data, build analyses and models, and produce shareable analytical artifacts — the notebook being the dominant surface form.
- Nearest neighbors: Machine Learning Platform (lifecycle system), MLOps Platform (operationalization), Business Intelligence Platform (governed analytics content for business consumers — the BI pass left an explicit light flag on this leaf), SQL Workbench / Analytical Query Editor (query-centric), Cloud IDE / Code Editor (general software development), Data Explorer (§02.12, published-data consumption).
- Known unknowns: whether the notebook artifact is definitional or merely the dominant realization; whether "managed compute" is definitional (Jupyter runs locally); how deep the governance/deployment machinery of enterprise products (Domino) reaches into the definition.

## Research Questions

1. What is the unit of work — the notebook, the session, the project?
2. What is the kernel/session model, and how do products attach compute to it?
3. How does data enter the session?
4. What languages and execution semantics exist (linear kernel vs reactive graph)?
5. What collaboration, sharing, and permission machinery is standard?
6. What publishing/export paths exist (reports, apps, dashboards, jobs)?
7. Where does reproducibility/governance machinery appear, and is it definitional?
8. How do AI assistants/agents enter the surface, and do they change the Type?
9. What separates this Type from BI, ML Platform, SQL tooling, and IDEs?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy | Tier |
|---|---|---|
| JupyterLab (Project Jupyter) | open-source archetype; the notebook standard itself | individual / community |
| Databricks Notebooks | platform-embedded, lakehouse-native, multi-language, enterprise | enterprise |
| Amazon SageMaker Studio | hyperscaler ML suite hosting a suite of IDEs (JupyterLab, Code Editor, RStudio) | enterprise / cloud |
| Domino Data Lab | enterprise governance-first data science platform (workspaces + reproducibility engine) | regulated enterprise |
| Hex | modern collaborative notebook SaaS, repositioned 2026 as "AI analytics platform" | team / mid-market |

## Sources

All fetched 2026-09-07. Zero fetch failures across 14 pages.

- JupyterLab docs (readthedocs): index, Notebooks user guide, Documents and Kernels — https://jupyterlab.readthedocs.io/en/latest/ , /user/notebook.html , /user/documents_kernels.html
- Databricks docs (AWS): Notebooks index, Develop code in notebooks, Notebook compute resources, Collaborate using notebooks — https://docs.databricks.com/aws/en/notebooks/index , /notebooks-code , /notebook-compute , /notebooks-collaborate
- Amazon SageMaker AI docs: Studio overview, Studio spaces, SageMaker JupyterLab — https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated.html , /studio-updated-spaces.html , /studio-updated-jl.html
- Domino Data Lab docs: Domino overview, Use Workspaces, Manage Compute Environments, Reproducibility Engine — https://docs.domino.ai/ , /cloud/platform-capabilities/core-concepts/workspaces , .../compute-environments , .../reproducibility
- Hex Learn docs: What is Hex, Notebook agent, Execution model, App builder — https://learn.hex.tech/ , /docs/explore-data/notebook-view/notebook-agent , /docs/explore-data/projects/project-execution/execution-model , /docs/share-insights/apps/app-builder

## Product Observations

### JupyterLab (evidence layer A — direct observation)

- Self-definition: "a highly extensible, feature-rich notebook authoring application and editing environment… providing tools (and standards) for interactive computing with computational notebooks."
- Canonical notebook definition (quoted from Project Jupyter docs): "A computational notebook is a shareable document that combines computer code, plain language descriptions, data, rich visualizations like 3D models, charts, graphs and figures, and interactive controls. A notebook… provides a fast interactive environment for prototyping and explaining code, exploring and visualizing data, and sharing ideas with others."
- Kernel architecture: "kernels are separate processes started by the server that run your code in different programming languages and environments." Any open text file can be connected to a code console and kernel; code consoles give "a log of computations done in the kernel, in the order in which they were done" and "a place to interactively inspect kernel state without changing the notebook."
- Notebook mechanics: Edit Mode vs Command Mode; cells (code/Markdown); drag-drop rearrangement; synchronized views; collapsible code/output; output scrolling; tab completion and tooltips.
- Subshell consoles (ipykernel 7+): run code concurrently with the main notebook execution.
- Trust model: JavaScript/HTML in notebooks from other machines are untrusted; outputs sanitized until the notebook is explicitly trusted; re-running a cell marks it trusted.
- Visualization: matplotlib/plotly/bokeh/altair/ggplot2; ipywidgets for interactive widgets; Mermaid diagrams built in.
- Also ships: terminals, debugger, file editor, extensions ecosystem, workspaces (UI layout), real-time collaboration, LSP support, notebook export, JupyterHub for multi-user hosting.

### Databricks Notebooks (evidence layer A)

- Self-definition: "Notebooks are the primary tool for creating data science and machine learning workflows on Databricks. Databricks notebooks provide real-time coauthoring in multiple languages, automatic versioning, and built-in data visualizations for developing code and presenting results."
- Languages: Python, SQL, Scala, R; per-cell language override via magic commands (%python/%r/%scala/%sql/%md); auxiliary magics (%pip, %run, %fs, %sh, %tensorboard, %skip, %%profile).
- Language REPL isolation: "Variables defined in one language… are not available in the REPL of another language. REPLs can share state only through external resources."
- SQL results as data: SQL cell results automatically available as implicit DataFrame `_sqldf` in subsequent Python/SQL cells; SQL cells can run in parallel in a new session; notebooks can attach to SQL warehouses (SQL-only mode with SQL warehouse sessions).
- Compute attachment: notebook attaches to all-purpose compute, serverless compute (default in Unity Catalog workspaces), or SQL warehouse; "The notebook must be attached to an active compute session for code assistance features"; attaching requires CAN ATTACH TO permission on compute; "any user with the CAN RUN permission on the notebook has implicit permission to access the compute resource"; predefined Spark variables (sc, spark, sqlContext).
- Session restoration (serverless): idle termination snapshots memory state (Python variables via pickle/cloudpickle, Spark DataFrames/temp views, Spark session state via Spark Connect migration); restore on reconnect; ~1-month TTL; explicit limitations (no file handles, locks, network connections).
- Collaboration: five permission levels (NO PERMISSIONS / CAN READ / CAN RUN / CAN EDIT / CAN MANAGE); real-time co-editing of the same cell; comments with @mentions; folder permission inheritance; Premium-plan gating for access control.
- AI: Genie Code assistant (generate/explain/debug); Data Science Agent ("orchestrate multi-step workflows from a single prompt… build an entire notebook for tasks like EDA, forecasting, and machine learning from scratch"); Genie in comment threads.
- Also: dashboards built from notebook results; widgets (interactive input parameters); notebook workflows/orchestration; import/export; debugger; unit testing; results tables with filters and download.

### Amazon SageMaker Studio (evidence layer A)

- Self-definition: "the latest web-based experience for running ML workflows. Studio offers a suite of integrated development environments (IDEs). These include Code Editor, based on Code-OSS… a new JupyterLab application, RStudio, and Amazon SageMaker Studio Classic."
- Role framing: "A data scientist can use JupyterLab to explore data and tune models. In addition, a machine learning operations (MLOps) engineer can use Code Editor with the pipelines tool in Studio to deploy and monitor models in production."
- Spaces: "used to manage the storage and resource needs of some… Studio applications"; 1:1 with an application instance; private or shared; each application gets its own EBS volume; image-based.
- SageMaker JupyterLab: ships the SageMaker Distribution image (PyTorch, TensorFlow, Keras, NumPy, Pandas, scikit-learn); shared spaces for real-time collaboration; Amazon Q Developer code companion; built-in Git integration; runs on a single EC2 instance with an EBS volume; instance switching; "Run interactive Spark jobs on Amazon EMR and AWS Glue serverless infrastructure, right from your notebook… schedule the notebook as a job."
- Suite machinery around the workbench: access to all SageMaker resources (training jobs, endpoints) in one interface; simplified model deployment; JumpStart model discovery; idle shutdown; BYOI; lifecycle configurations.

### Domino Data Lab (evidence layer A)

- Self-definition: "a platform for building, delivering, and governing AI solutions for mission-critical use cases… built on a flexible orchestration engine that makes it easy to run arbitrary computational workloads in secured sandboxes, while automatically capturing reproducible results of those workloads and audit trails."
- Workspaces: "an interactive session where you can conduct research, analyze data, train models, and more. Use workspaces to work in the development environment of your choice, like Jupyter notebooks, RStudio, VS Code, and many other customizable environments." Settings: hardware tier, environment, volume size; package persistence across sessions; SSH from local tools; sync /mnt to project; stop/resume with persistence; create workspace from a checkpoint (any commit); App Preview + Publish App from a workspace.
- Compute Environments: "defined by Docker images that create isolated containers for each execution unit including Workspaces, Runs, Apps, and Models"; versioned revisions with build status and inheritance/dependency tree; DSE (full) vs DME (light); global/project/org visibility.
- Reproducibility Engine: automatically tracks tuples of code / data / software / command / results; tracks environment revision, dataset snapshots, project file snapshots; jobs dashboard with reproducible materials; MLflow-based experiment tracking; rationale: collaboration/reuse, auditability/compliance, good science.
- Platform frame: Projects (DFS-backed or Git-backed), templates, search, collaboration, Governance Center (policies, FinOps, audit trail), App & Agent Hub, APIs ("increasingly, agents use the platform even more than humans").

### Hex (evidence layer A)

- 2026 positioning: "Hex is an AI analytics platform that makes it easy for anyone to explore data, with answers you can trust" — a deliberate repositioning away from pure notebook-tooling vocabulary (drift observation; the notebook remains the core surface: "Explore data deeply — Investigate questions with AI-generated SQL + Python").
- Notebook cells: Python, SQL, Markdown/text, Pivot, Input parameters, Single value, Chart cells.
- Execution model: "Hex notebooks improve upon Jupyter notebooks by using a reactive execution model" — a graph (DAG) built automatically from variable references links cells; Graph View visualizes it; "reproducible by default, in that a given change will trigger a predictable, consistent set of re-computes"; parallel SQL execution (up to 4–8 concurrent queries depending on connection type); published-app runs skip cells not needed downstream.
- Notebook agent: natural-language assistance with full project context and warehouse schema; generate/edit/move/delete cells with per-cell Confirm/Undo pending changes; subagents for parallel workstreams; web search; model & effort picker; credits metering; can arrange and publish apps.
- Published apps: compose notebook cells into shareable apps (rows/columns/tabs, themes, embedding, scheduled runs); app runs execute the full project in notebook order.
- Context/governance layer: data connections + semantic models + workspace rules as grounding context; Context Studio observability; permissions (workspace roles Admin/Manager/Editor; project permissions Can Edit / Can Explore); MCP/CLI/Slack surfaces into the same governed context.

## Cross-product Comparison

| Dimension | JupyterLab | Databricks | SageMaker Studio | Domino | Hex |
|---|---|---|---|---|---|
| Unit of work | notebook document + kernel | notebook + attached compute session | JupyterLab space (app instance) | workspace session on compute environment | project (notebook + environment) |
| Session model | kernel process (local or server) | compute session (all-purpose/serverless/SQL warehouse) | EC2 instance + EBS per space | Docker container per execution unit | managed environment, reactive DAG over cells |
| Notebook artifact | .ipynb (nbformat standard) | Databricks notebook (workspace object, auto-versioned) | notebooks inside JupyterLab/Code Editor | notebooks inside project files | Hex project cells |
| Languages | any kernel (Python/R/etc.) | Python/SQL/Scala/R + magics | Python (distribution image), R (RStudio app) | any (Jupyter/RStudio/VS Code pluggable) | Python + SQL + no-code cells |
| Data access | files + libraries | Unity Catalog tables, DBFS, SQL warehouses | S3/EMR/Glue from notebook | data sources + datasets + project files | data connections + semantic models |
| Environment management | user-managed (pip/conda) | cluster libraries, %pip, serverless | SageMaker Distribution image, BYOI | Docker environments with revisions | managed environment |
| Collaboration | RTC (recent), JupyterHub multi-user | real-time co-editing, 5 permission levels, comments | shared spaces, real-time | project collaborators, orgs | real-time, roles + project permissions |
| Reproducibility | not built-in (files + Git) | automatic notebook versioning | Git integration | Reproducibility Engine (tuples) | reactive DAG "reproducible by default" |
| Publishing | export HTML/PDF/etc. | dashboards from notebooks | schedule notebook as job | publish Apps from workspace | published apps (tabs/themes/embed) |
| AI assistance | (ecosystem extensions) | Genie Code + Data Science Agent | Amazon Q Developer | (agents as platform users) | Notebook agent (confirm/undo changes) |
| Governance | none native | workspace ACLs, Premium | IAM/domain | Governance Center, audit trail, FinOps | workspace settings, context governance |

Cross-product commonalities (evidence layer B):

1. Every product centers an **interactive code session** (kernel / compute session / workspace / project environment) as the unit of work.
2. Every product brings **data into the session** (files, tables, connections, datasets).
3. Every product frames the purpose as **exploring data / building analyses and models** (verbatim in all five self-descriptions).
4. The **notebook** (code cells + inline outputs + narrative) is the dominant artifact in all five — but Jupyter's own architecture separates document from kernel, and Domino's workspace concept is IDE-agnostic, showing the notebook is a realization, not the invariant.
5. **Environment management** (packages/images) is universal; who manages it (user vs platform) varies.
6. **Collaboration/sharing** is universal in the modern sample (RTC, permissions, comments).
7. **Publishing/export** paths exist in all five (export, dashboards, jobs, apps).
8. **AI assistance** is era-typical across the sample (Genie, Q Developer, Hex agent; Jupyter via ecosystem).

## Canonical Abstraction

### L0 — Defining Invariant (deliberately small)

Three properties. Remove any one and the product stops being recognizable as a Data Science Workbench:

1. **Interactive stateful code session** — the unit of work is a live execution session (kernel/workspace) attached to the workbench surface; the user runs code incrementally, results return inline, and session state (variables, loaded data) persists across steps within the session. Remove → a script editor plus a batch job runner (an IDE, not a workbench).
2. **Data as working material** — the workbench connects to data sources and loads/queries data into the working environment; the session exists to work ON data. Remove → a generic IDE or REPL.
3. **Exploratory analysis/modeling purpose** — the code is written to explore data, build analyses and models, and produce quantitative/analytical artifacts (the data-science orientation that separates it from general software development). Remove → a generic terminal/shell.

### L1 — Common Mature Structure

- **The notebook artifact** — code cells + inline rich outputs + narrative text; persistent, shareable, exportable (the dominant modern realization of the session; Jupyter's own document/kernel separation and Domino's IDE-agnostic workspaces show it is not the invariant).
- **Multi-language support** — Python/R/SQL/Scala kernels or language-switching cells.
- **Environment management** — package installation, images/distributions; platform-managed in hosted products, user-managed locally.
- **Compute attachment/scaling** — attach/detach sessions to compute (clusters, GPUs, serverless); compute sizing tiers.
- **Inline visualization** — plots, tables, rich output rendered in the session surface.
- **File/data access machinery** — upload, dataset browsing, data-source connections.
- **Container above the notebook** — project/workspace/space organizing notebooks + environments + data + results.
- **Version control** — Git integration and/or automatic versioning.
- **Collaboration** — sharing, permission ladders, comments, real-time co-editing.
- **Scheduling/jobs** — run the notebook as a scheduled or triggered job.
- **Publishing/export** — HTML/PDF export; publish as app/dashboard/report.
- **Debugger/terminals** — standard dev-tool affordances inside the session.
- **AI assistance** — code generation/explanation; agentic notebook building (era-typical).

### L2 — Variant / Optional Structure

- **Governance/reproducibility machinery** — environment revisions, audit trails, lineage, FinOps (Domino-class; absent in the open-source pole).
- **Deployment handoff** — model endpoints, app hosting, MLOps integration (present in platform-embedded products; not definitional).
- **Execution philosophy** — linear user-driven kernel session (Jupyter/Databricks) vs reactive dependency-graph execution (Hex).
- **Packaging posture** — standalone open-source tool vs platform-embedded module vs enterprise platform vs collaborative SaaS.
- **Deployment locus** — local desktop vs hosted multi-user server (JupyterHub) vs cloud SaaS vs customer VPC/on-prem.
- **Audience breadth** — individual data scientist → team → enterprise/regulated (pharma SCE, model risk management per Domino's own use-case list).
- **SQL-first vs Python-first orientation**; no-code cell types (Hex pivot/input/chart cells).
- **Semantic/context layers** — semantic models, workspace rules grounding AI answers (Hex).
- **Community/marketplace surfaces** (Kaggle-class; not directly sampled).

### L3 — Vendor-specific (research notes only)

- Databricks: magic-command catalog (%sql/_sqldf, %run, %fs, %sh, %tensorboard, %skip, %%profile), per-language REPL isolation, serverless session restoration mechanics (pickle/cloudpickle, Spark Connect migration, ~1-month TTL, 50 MB Spark-state limit), CAN ATTACH TO / implicit compute access rule, Premium-plan ACL gating, Unity Catalog/DBFS, Genie Code/Data Science Agent naming.
- SageMaker: spaces (1:1 app instance, private/shared, EBS per app), SageMaker Distribution image contents, Studio Classic legacy split, Amazon Q Developer, idle shutdown, BYOI, lifecycle configurations, trusted identity propagation.
- Domino: DRE tuple model (code/data/software/command/results), DSE/DME environment families, hardware tiers, /mnt sync + package persistence, checkpoints-from-commit, App Preview/Publish App, Governance Center/FinOps/Audit Trail, "agents use the platform even more than humans" framing.
- Hex: reactive DAG + Graph View, app-run cell-skipping rules, parallel-SQL concurrency numbers (4/8), pending-changes Confirm/Undo per cell, model & effort picker, credits metering, semantic models/workspace rules, MCP/CLI/Slack surfaces.
- Jupyter: nbformat, trust model, subshell consoles, Edit/Command modes, extension ecosystem, JupyterHub.

## Vendor-specific / Rejected Findings

- **Rejected as definitional: the notebook artifact.** Jupyter's own architecture (document vs kernel), Domino's IDE-agnostic workspaces (Jupyter/RStudio/VS Code), and the pre-notebook interactive-statistics era (R console, SAS, MATLAB) show the notebook is the dominant realization, not the invariant. Kept in L1.
- **Rejected as definitional: platform-managed compute.** JupyterLab runs fine on a laptop with user-managed environments; "managed" is a hosted-product property, not a Type property. The invariant is that the session executes in a runtime the workbench attaches to.
- **Rejected as definitional: reactive/DAG execution.** Hex-specific philosophy (its own docs frame it as an improvement "upon Jupyter notebooks"); the linear kernel session remains the dominant model.
- **Rejected as definitional: governance/audit machinery.** Present only at the enterprise pole (Domino); the open-source and SaaS poles satisfy the Type without it.
- **Rejected as definitional: AI agents.** Era-typical capability across the sample; agents operate inside the workbench surface (Databricks Data Science Agent, Hex Notebook agent) without changing the session+data+analysis core.
- **Rejected as definitional: publishing apps/dashboards.** A capability drifting toward BI/dashboard territory; the workbench core stands without it (Jupyter export is the minimal form).

## Boundary Findings

- **vs Machine Learning Platform (§13 sibling, unprocessed):** the sharpest seam. ML platforms span the full lifecycle (training pipelines, registries, deployment, monitoring); the workbench is the interactive development surface. Products straddle deliberately: SageMaker Studio is "the web-based experience for running ML workflows" hosting IDEs; Databricks notebooks are "the primary tool for creating data science and machine learning workflows" inside a lakehouse platform. Removal tests: remove the interactive session → the ML platform remains (pipelines/jobs/registry/deployment); remove lifecycle machinery → the workbench remains. Both leaves stand; the workbench leaf documents the interactive surface, and the ML-platform pass should treat the embedded workbench as a module. Joint review recommended.
- **vs Business Intelligence Platform (§13, processed — discharges that pass's light flag):** BI centers a governed analytics-content lifecycle (authored dashboards/reports in a hosted repository, consumed by a business audience under content-and-data access control); the workbench centers the code session for the data scientist. The drift zone is real: workbenches publish apps/dashboards (Hex apps, Databricks dashboards-in-notebooks) and BI platforms add notebook/AI surfaces. Removal tests: remove code execution → BI remains; remove the governed content repository + consumer audience → the workbench remains. Flag discharged from this side.
- **vs SQL Workbench / Analytical Query Editor (§13 siblings):** query-centric single-language tooling bound to a database/analytical platform vs a multi-language stateful code session. The workbench can contain SQL cells (Databricks %sql, Hex SQL cells) but its center is the code session. Gradient, not a wall; consistent with the analytical-query-editor pass's own sibling notes.
- **vs Cloud IDE / Code Editor (§12, both processed):** general software development (build/run/debug apps) vs data-science work (explore data, build models). Straddle: notebooks inside IDEs (VS Code), SageMaker's Code Editor (Code-OSS) inside Studio. Test: remove data-science semantics (kernels with inline outputs, data access, analysis purpose) → IDE remains. The two Types share editor machinery; the session+data+purpose core separates them.
- **vs Data Explorer (§02.12, processed):** explorer = published observation data consumed by selection (no code, no user data); workbench = code-first analysis over connected data. Clean split.
- **vs Ad-hoc Query Application (§13, processed):** ad-hoc = governed question loop for business users (compose query → run → refine); workbench = stateful code session for data scientists. The ad-hoc loop can live inside a workbench as SQL cells; the reverse is not true.
- **vs AI Coding Agent / AI Coding Assistant (§12, both processed):** agents/assistants operate inside workbench surfaces (Databricks Data Science Agent, Hex Notebook agent, SageMaker Q Developer) as capabilities; the workbench remains the environment. Consistent with the ai-coding-agent pass's autonomy-gradient framing.
- **vs MLOps Platform / Model Registry / Feature Store (§13 siblings, unprocessed):** operationalization and governance-of-models machinery sit downstream of the workbench; Domino packages them around its workspaces but its own workspace concept is the interactive session. Cross-check recommended when those leaves are processed.
- **Naming observation:** the market label has drifted — "data science workbench/platform" (Domino heritage) → "AI analytics platform" (Hex 2026) → "ML workflows experience" (SageMaker). The referent (interactive code session over data for analysis/modeling) is stable; the leaf name remains valid as the historical market name.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0?

- **Pre-notebook interactive statistics:** R console sessions, SAS interactive sessions, MATLAB — interactive stateful sessions over data for analysis, no notebook artifact, no cloud, no collaboration. Satisfy the L0 triple. The notebook is therefore NOT definitional.
- **Classic Jupyter Notebook (2014) / IPython (2001):** notebook + kernel, no collaboration, no governance, no publishing. Satisfies the L0 triple.
- **Apache Zeppelin:** multi-language notebooks, platform-native form. Satisfies.
- **Kaggle Notebooks:** community-hosted notebooks with datasets/GPUs. Satisfies (not directly sampled; structural).
- Check passed: the L0 triple survives all historical poles; nothing modern (cloud, RTC, AI, governance) is required.

## Uncertainties

- **Kaggle/community pole** not directly fetched — community/marketplace surfaces documented structurally only.
- **Deepnote / CoCalc / Saturn Cloud / Vertex AI Workbench / Azure ML notebooks** not fetched — the collaborative-SaaS and other-hyperscaler poles are covered by Hex + SageMaker evidence; no claims made about the unfetched products.
- **JupyterHub operational detail** not fetched — multi-user hosting documented from the JupyterLab TOC reference only.
- **Domino's model-deployment/MLOps depth** (endpoints, monitoring) not fetched — recorded as platform-frame context only, not asserted as workbench machinery.
- **Hex semantic-model authoring** ("Modeling workbench") not fetched — semantic layer recorded as context-supply capability at wording strength.
- No numeric limits asserted anywhere in the final document except where directly documented (Hex parallel-SQL concurrency 4/8; Databricks session-restoration TTL/limits — kept in research notes, not the final doc).

## Final Synthesis

The Data Science Workbench is the interactive development surface of data work. Its defining core is small: a stateful code session attached to the workbench, data brought into that session as working material, and an exploratory analysis/modeling purpose. Everything else — the notebook artifact, multi-language kernels, environment management, compute scaling, collaboration, versioning, scheduling, publishing, governance, AI agents — is mature structure layered on that core, varying by packaging philosophy (open-source tool, platform module, hyperscaler suite, governance platform, collaborative SaaS). The Type's center of gravity is the session; the notebook is its dominant document form; the project/workspace is its container; and its edges blur deliberately into ML platforms (lifecycle), BI (published analytics), and IDEs (general code) — seams the market itself polices with role framing ("data scientist uses JupyterLab to explore data and tune models; MLOps engineer uses Code Editor with pipelines").
