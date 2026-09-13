# Research Notes — DataOps Platform

Research date: 2026-09-07
Slug: `dataops-platform` (DIRECTORY §13 Data, Analytics & AI Systems)

## Research Goal

Understand what the market means by "DataOps Platform" as an Application Type: what the platform's primary managed objects are, what work users do around them, how the development→production loop actually runs, and how the Type is bounded against the dense cluster of neighboring data-platform Types (ETL/ELT, data quality, data observability, data lineage, CI/CD for software, MLOps).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a DataOps Platform manages the engineering lifecycle of data pipelines — pipelines as versioned objects, developed/tested in environments isolated from production, promoted into production, and operated there — i.e., the DevOps loop applied to data work.
- Likely nearest neighbors: ETL/ELT Platform (data movement is the center), Data Quality Platform (rules + results), Data Observability Platform (estate health + incidents), Continuous Integration / Continuous Delivery Platform (§12, software artifacts), MLOps Platform (model lifecycle), and the unlisted market category of "data orchestrators" (Airflow/Prefect/Dagster-class).
- Known open obligation: the data-observability-platform pass flagged "CI/CD shift-left impact previews ship inside observability products — capability relationship, cross-check recommended" against this leaf. This pass discharges it.

## Research Questions

1. What is the primary managed object — pipeline, asset, DAG, flow, recipe? Is it code, configuration, or both?
2. What does the development experience look like, and where does version control live (external Git, platform-native branching, or both)?
3. How do changes travel from development to production? What isolates development from running production pipelines?
4. What role do tests play, and are they gates on promotion or parallel quality tooling?
5. What does "operations" mean here: scheduling/triggers, run records, monitoring, alerting?
6. Does the platform execute the data work itself (connectors, transformations) or orchestrate external engines/tools? Who holds the data of record?
7. Who uses the platform (engineers, analysts, mixed teams), and how does that shape the product?
8. What do vendors themselves say "DataOps" means, and how much of that is methodology marketing vs. product structure?
9. Boundary questions above (ETL/ELT, CI/CD, DQ, observability, orchestrator, MLOps).

## Representative Products

Selection principles applied: market representativeness, documentation completeness, different product philosophies, different customer tiers.

| Product | Philosophy / pole | Tier of evidence |
|---|---|---|
| **Dagster** | Orchestration-first engineering tool (OSS + commercial Dagster+); asset-centric; "best-in-class testability" | A (full official docs) |
| **Keboola** | End-to-end governed data platform, long self-branded as DataOps; platform-hosted storage; UI + code + CLI + AI | A (marketing site + full user docs) |
| **DataKitchen (DataOps Automation)** | DataOps pure-play "meta-orchestrator / data factory"; tool-agnostic; methodology-led vendor | A (product pages + full product docs) |
| **Prophecy** | Low-code/AI-native pipeline IDE with Git-native CI/CD; runs on customer's cloud engines | A (docs incl. CI/CD pages) |

Sample change: **Orchest** (open-source "data-ops IDE") was planned as the fifth sample but its domain now serves unrelated content (defunct product). Recorded as sample loss; not replaced — stop conditions were already met with four products spanning the intended philosophy spread (engineer-first code, governed end-to-end platform, pure-play process platform, analyst-facing low-code IDE).

## Sources

Fetched 2026-09-07 (all successful on first attempt unless noted):

- Dagster — https://docs.dagster.io/ (overview, concepts nav: build/automate/operate/observe/test guides) ; https://docs.dagster.io/deployment/dagster-plus (Dagster+ capabilities)
- Keboola — https://www.keboola.com/product (product overview) ; https://help.keboola.com/ (user documentation index) ; https://help.keboola.com/components/branches/ (Development Branches, Tier 1)
- DataKitchen — https://www.datakitchen.io/ (homepage/FAQ) ; https://www.datakitchen.io/products/dataops-automation/ (product page + FAQ) ; https://docs.datakitchen.io/automation/what-is-automation/ (Tier-1 product docs incl. full docs nav for Kitchens/Recipes/Orders/Vaults/Tests/Alerts/Versioning)
- Prophecy — https://docs.prophecy.io/ → redirected https://docs.prophecy.ai/ (introduction) ; https://docs.prophecy.ai/data-engineering/getting-started (quickstart, Tier 1) ; https://docs.prophecy.ai/data-engineering/ci-cd/reliable-ci-cd.md (CI/CD strategies, Tier 1) ; https://docs.prophecy.ai/_llms/data-engineering.md (documentation index, fetched via curl)
- Orchest — https://www.orchest.io/ fetched: domain now serves unrelated gambling-affiliate content. Product defunct or rebranded out of the category. No data available.

Access limitations: none material beyond the Orchest loss. DataKitchen's enterprise-only doc pages are marked in their docs (shield icon) but the public "What is Automation?" page is complete. Prophecy marks CI/CD features as Enterprise Edition — noted where relevant.

## Product Observations

### Dagster (evidence layer A)

- Self-description (docs root): "Dagster is a data orchestrator built for data engineers, with integrated lineage, observability, a declarative programming model, and best-in-class testability."
- Primary objects: **assets** (data assets declared in Python code), asset **dependencies** (lineage graph), **jobs/ops**, **schedules**, **sensors** (event triggers), **declarative automation** (assets request their own materialization), **partitions and backfills**, **resources** (external systems), **projects/workspaces** (code repositories).
- Docs are organized into Build / Automate / Operate / Log & debug / Observe / Test — the guide taxonomy itself mirrors a lifecycle.
- Test section is first-class: testing assets, **asset checks** (data quality assertions attached to assets), unit testing assets and ops, testing partitioned config, **data contracts with asset checks**.
- Observe section (mostly Dagster+): asset catalog (search + lineage), alerts (Slack/PagerDuty/email) for failed runs, data quality issues, violated SLAs; asset health status; freshness policies; insights (cost/trend analytics).
- Dagster+ (docs): "managed orchestration platform built on top of Dagster's open source engine"; serverless (fully managed) and hybrid (customer-run execution, Dagster+ control plane); adds Insights, Alerts, RBAC, audit logs, Asset Catalog, and **Branch Deployments** — "create staging environments of your Dagster code, right in Dagster+."
- OSS pole: the orchestration core (define + run + monitor) is free/self-managed; the dev→promote machinery is productized in the commercial tier.
- Positioning contrast noted in DataKitchen's docs (see below): Dagster/Airflow/Prefect are framed as "pipeline orchestrators" that "schedule and run DAGs within a single tool context."

### Keboola (evidence layer A)

- Current marketing positions an "AI & Data Platform" (pivot from earlier explicit "DataOps Platform" branding); capabilities: ingestion (large connector library — marketing number, not definitional), transformations (SQL/Python/dbt workspaces), orchestration ("flows"), version control & branching, safe experimentation in workspaces, cost/usage monitoring, job telemetry, multiproject environments.
- User docs (Tier 1) structure: Projects/Organizations → Storage (buckets/tables/files — platform **is** a data store) → Components (extractors, writers, applications, transformations) → **Flows** (orchestrated pipelines of components) → **Development Branches** → Jobs/notifications/telemetry → Workspaces (SQL editor sandboxes) → CLI/API/MCP.
- **Development Branches (Tier 1, key page)**:
  - Creating a branch yields "an exact copy of the project and all its current configurations"; modify without touching production; production flows keep running.
  - Storage isolation: branch runs **read** production tables transparently; **writes** land in the branch's isolated storage layer (copy-on-write "Branched Storage" on Snowflake; prefix-based model on other backends) — production data is never touched, no full data duplication.
  - Closing a branch: **delete** (discard) or **merge into production** — all changes applied at once after approval, producing new **configuration versions**; "Branches 2.0" merge requests add diff review and **approvals** before changes reach production.
  - Guardrails: components writing to external destinations are marked *unsafe* in a branch and cannot run until reviewed/redirected; OAuth-authorized components cannot be re-authorized in a branch (shared tokens could break production); branch is "for development and testing only."
- Multi-project organization and a data catalog exist as governance layers above projects.

### DataKitchen — DataOps Automation (evidence layer A)

- Vendor's definition of the methodology (site FAQ): "DataOps is a set of technical practices, workflows, and cultural norms that let a data team innovate quickly while keeping error rates low. It combines Agile development, DevOps automation, and statistical process control from lean manufacturing."
- Product framing: "Orchestrate, Deploy, and Monitor Data Pipelines"; "Meta-orchestrate your data operation from a single platform: pipelines, tools, teams, and environments. Automate deployment, embed testing at every step."
- Docs (Tier 1): "Automation facilitates the control of **two data pipelines — the production pipeline and the development pipeline — at the same time**."
- DataOps features listed in docs: meta-orchestration (orchestrate pipelines, then orchestrate the orchestration across teams/tools/locations/environments); automated testing and monitoring (tests at every step + alerts); environment creation and management ("infrastructure as code" — kitchen workspaces pre-configured with tools, datasets, tests, created in minutes, merged when ready, torn down at project end); tool-agnostic integration (connectors + container nodes wrapping any tool); DataOps process analytics (test coverage growth, error reduction, deployment cycle times, collaboration); storage and revision control (**version control using Git and Docker Hub**); history/metadata logs; authorization (identity provider); secrets management (HashiCorp Vault-class); collaboration/sharing (**ingredients**); automated deployment ("continuous deployment for testing and releasing new analytics on demand and safely migrating analytics to production. Solutions such as Jenkins or CircleCI move the code/configuration from one environment… to a production environment").
- Core concepts (docs nav + product page): **Kitchens** (isolated workspace environments — "like Git branches for your whole data stack"; create/merge/revert/delete; kitchen users, roles, security; kitchen history), **Recipes** (collections of related pipelines; recipe graphs of nodes; variations = per-use-case configurations), **Nodes** (action, conditional, container, ingredient nodes; node tests), **Ingredients** (reusable shared pipeline components with variable validation), **Orders** (recipe executions with full monitoring, logging, test-result tracking; order runs), **Vaults/Secrets** (global/kitchen/custom), versioning & deployments docs section.
- Explicit competitive framing (product FAQ): "Airflow, Dagster, Prefect… are pipeline orchestrators. They schedule and run DAGs within a single tool context. Automation is a meta-orchestrator that sits above your existing tools and coordinates work across them. It manages environments, deployment, version control, testing, collaboration, and process metrics alongside orchestration."
- "A DataOps Factory, Not Another DAG Tool": runs the production pipeline and the development pipeline simultaneously.
- Deployment models: SaaS (vendor-hosted), self-hosted, hybrid. Enterprise product; its TestGen (data quality tests) and Observability (data journeys) siblings are open source and integrate with it.

### Prophecy (evidence layer A)

- Self-description: "Build, run, and manage AI-native data pipelines"; generate pipelines with AI, refine visually or in SQL, run recurring data flows on your data platform; audiences split into analysts (SQL pipelines) and engineers (Spark-native).
- Primary objects: **Project** (bound to a **Git repository**), **Pipeline** (graph of visual "gems" backed by generated code), **Job** (scheduled/triggered execution of pipelines), **Fabric** (execution environment — customer's Spark engine e.g. Databricks/EMR/Dataproc, or SQL warehouse e.g. Snowflake; Prophecy-managed trial fabric exists), **Datasets**, **parameters** (environment-adaptable values), secrets providers.
- Quickstart (Tier 1): create project → connect Git account → **create a development branch** ("your pipeline will not appear in the main branch until you merge your changes") → build pipeline on canvas → attach cluster (fabric) → run interactively with data previews → **Commit Changes** (Git workflow dialog with commit history, changed entities, generated commit message) → merge to main.
- CI/CD strategies (Tier 1, Enterprise): recommended multi-fabric environment setup — Development / QA-Staging / Production fabrics with separate data (synthetic → production-like → real), access, and cluster sizing. Workflow: develop on `dev` branch → validate in QA fabric (merge to `main`, deploy, verify scheduled runs) → deploy to production (small platform team; jobs should run as a **service principal**, unattended).
- Two deployment routes: (1) **Prophecy-native CI/CD** — a release marks a project version with a Git **tag**; deployment builds and pushes that version to the chosen fabric; the release process "automatically builds the code, **runs unit tests**, and packages everything needed (JARs/wheels)"; (2) **External CI/CD via Prophecy Build Tool (PBT)** — CLI that builds/deploys from Git inside GitHub Actions or Jenkins, with `--fabric-ids` targeting environments.
- Validation tooling: unit tests for pipelines, **data diff** (compare actual vs expected datasets), execution metrics, lineage extractor.
- Pipelines can be orchestrated by Prophecy's own scheduling ("Automate") or external schedulers; API supports deploying projects and triggering runs for external CI/CD integration.

## Cross-product Comparison

| Dimension | Dagster | Keboola | DataKitchen Automation | Prophecy |
|---|---|---|---|---|
| Primary managed object | Asset / job, declared in Python code | Component configurations + Flows (platform-stored config) | Recipe (graph of nodes) inside a Kitchen | Pipeline (visual gem graph) inside a Project |
| Where definitions live | Code repository (Git) | Platform configuration store, versioned internally | Platform (JSON artifacts) versioned via Git + Docker Hub | Git repository (project = repo) |
| Version control experience | External Git; branch deployments in Dagster+ | **Platform-native branches + merge requests** (Git-like, no external Git needed) | Kitchens as environments; artifact version control via Git/Docker Hub | Full Git workflow in-editor (branch/commit/merge/PR/tag) |
| Dev/production isolation | Branch deployments (Dagster+); self-managed otherwise | Development branch = full config copy + write-isolated storage; prod flows keep running | Kitchen = isolated, production-like workspace ("like Git branches for the whole data stack") | Branch + dev/QA/prod **fabrics** (separate engines, data, access) |
| Promotion mechanism | Deploy code; branch deployments for staging | Merge request with diff + approvals → new config versions applied at once | Merge kitchens; automated deployment orchestrations migrate dev→test→prod (Jenkins/CircleCI integrable) | Release (Git tag) → deploy to fabric; or external CI/CD (PBT) |
| Testing | Asset checks (data), unit tests, data contracts — first-class docs pillar | Testing by safe execution in branches; unsafe external writes blocked | Tests at every node; integrates TestGen (DQ) | Unit tests run at release; data diff; interactive validation |
| Execution model | Runs jobs/materializes assets on external compute via resources (self-hosted or Dagster+ serverless/hybrid) | Platform runs components incl. connectors/transformations; platform-hosted storage | Agents execute nodes across external tools (meta-orchestration; tool-agnostic) | Jobs run pipelines on customer's engines (fabrics) |
| Data of record | External systems | **Platform Storage** (buckets/tables) | External tools/warehouses | External engines/warehouses |
| Monitoring | Run UI, logs, lineage, asset health/freshness, alerts, insights (Dagster+) | Job queue, notifications, telemetry dashboards | Order run monitoring, alerts, process analytics (cycle time, test coverage) | Execution metrics, monitoring surfaces, lineage extractor |
| Who builds | Data engineers (Python) | Mixed: analysts (UI/SQL) + engineers | Data engineering teams (enterprise) | Analysts + engineers (low-code + code) |
| Delivery model | OSS + commercial SaaS/hybrid/serverless | SaaS multi-cloud/private | SaaS / self-hosted / hybrid (enterprise) | SaaS (Enterprise for CI/CD) + free tier |
| AI authoring | (Labs features) | AI assistant + MCP server; natural-language pipeline building | (not central) | AI agent/Copilot generate pipelines + commit messages |

**Stable commonalities (evidence layer B, cross-product):**

1. All four center on **data pipeline definitions as durable, versioned, iterated objects** (code, config, or graph).
2. All four maintain a **separation between a development context and production**, and all four provide a **controlled promotion operation** (merge/release/deploy with visibility into what changes).
3. All four **execute or orchestrate pipeline runs** in production on schedules/triggers and provide **run records, logs/status, and failure visibility** (alerts).
4. All four treat **environments** as a first-class structure with environment-specific values (connections, credentials, parameters) and per-environment secrets handling.
5. All four support **testing in the loop** (data tests, code tests, or safe trial runs), though its formality varies.
6. All four expose **collaboration structures**: shared projects/workspaces, reusable components (ingredients/shared code/gems), roles.
7. All four integrate with or expose **CI/CD machinery** (native or external).

**Key variation axes (evidence layer B/C):** data of record (platform-hosted vs external); execution (native runtime vs meta-orchestration of external tools); authoring (code-first vs low-code vs config); how productized the dev→prod loop is (managed feature vs self-managed practice); process metrics as a sellable (DataKitchen only, explicit); AI-native authoring (current-generation, uneven).

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

A DataOps Platform is recognizable as such when **all three** of these hold jointly:

1. **Data pipeline definitions as the platform's primary managed objects of record** — pipeline logic (as code, configuration, or graph) exists as durable, named, **versioned** objects inside the platform's world, iterated over time. Remove → the product is a generic IDE/CI tool or an unversioned job runner; the Type collapses.
2. **A managed develop→promote loop over environments separated from production** — the platform provides (or structures) an isolated development context in which pipeline changes are made and tried **without touching running production pipelines**, and a controlled, reviewable, versioned operation that carries accepted changes into production. Remove → the product is a pipeline runtime/scheduler (orchestrator pole) or an ETL tool; the "Ops" loop is gone.
3. **Operational execution and monitoring of pipelines as ongoing production work** — production pipelines run on schedules/triggers as unattended work; each run is a recorded event with status/logs, and failures are visible (alerting). Remove → the product is development tooling, not operations.

Jointly-held is essential: property 1+3 without 2 describes an orchestrator; 1+2 without 3 describes development tooling; 2+3 without 1 describes generic deployment tooling.

### L1 — Common Mature Structure (very common, not definitional)

- Automated testing as part of the loop: data-quality checks attached to pipelines/assets, unit tests of pipeline code, data diffs; tests run at release or as pipeline steps; occasionally as hard gates (product-dependent).
- Git integration in both directions (external Git as the store, or Git-like native branching with merge requests, diffs, approvals).
- Run history with logs, lineage visualization of pipeline graphs, asset/table-level metadata views.
- Alerting into chat/pager channels (Slack/PagerDuty/email-class).
- Scheduling + event/sensor triggers + backfills/retries.
- Reusable component libraries (shared code, ingredients, gems, templates) and project/team collaboration with roles.
- Secrets/credential management scoped per environment.
- API/CLI for operating the platform itself (infra-as-code posture).
- Catalog/glossary/lineage adjacency and cost/usage insights at the commercial tiers.

### L2 — Variant / Optional Structure

- Data of record: platform-hosted storage (end-to-end pole) vs. external-only (orchestration/IDE poles).
- Execution stance: platform-native runtime vs. meta-orchestration over the customer's existing tools.
- Authoring philosophy: code-first (engineer), low-code visual canvas (analyst-friendly), form/config editors; AI-assisted generation as a current-generation overlay.
- How the dev→prod loop is productized: managed branch/deploy features (commercial tiers) vs. self-managed deployments (OSS pole).
- Delivery model: OSS self-hosted, SaaS, hybrid, private-cloud; enterprise governance depth (RBAC, audit logs, process analytics) varies by segment.
- Methodology packaging: maturity models, consulting, process metrics (pure-play pole).

### L3 — Vendor-specific (Research Notes only)

- Dagster: assets/ops/sensors/declarative automation terminology; Dagster+ branch deployments, insights, asset catalog; data contracts via asset checks.
- Keboola: components/extractors/writers; branch storage copy-on-write mechanics (Snowflake-only "Branched Storage", prefix model elsewhere); "Branches 2.0" merge requests; Storage buckets; Kai assistant/MCP server; connector-count marketing.
- DataKitchen: Kitchens/Recipes/Variations/Ingredients/Orders terminology; "two pipelines" (production + development) framing; DKCloudCommand CLI; Jenkins/CircleCI as migration executors; TestGen/Observability sibling products; maturity model/certifications.
- Prophecy: gems/fabrics terminology; Prophecy Build Tool (PBT); release=Git-tag semantics; service-principal guidance for production jobs; Alteryx import tool; Copilot-generated commit messages.

## Vendor-specific Findings

- The term "DataOps" is vendor-defined as a **methodology** (Agile + DevOps + lean SPC for data; DataKitchen is the category's origin story and still sells the methodology alongside software). Products labeled "DataOps" sit at very different poles. The Type must be defined by product structure (the lifecycle loop), not by label adherence.
- Marketing-layer claims (connector counts, speed-to-production figures, pricing comparisons) were not carried into the canonical model.
- Current-generation pivot pressure: Keboola now leads with "AI & Data Platform"; Prophecy leads with "AI-native"; the underlying pipeline-lifecycle structure is stable beneath the messaging.

## Boundary Findings

**vs ETL/ELT Platform & Data Integration Platform (§13, processed):** ETL/integration's defining core = connections to external source/destination systems and the movement/transformation of data as the managed unit. A DataOps platform's defining core is the engineering **lifecycle loop** around pipelines. Overlap is real (end-to-end poles move data themselves: Keboola hosts storage + connectors; Prophecy builds ingestion/transformation pipelines). Discriminator (center-of-gravity test): in an ETL platform the lifecycle features (if any) serve data movement; in a DataOps platform the pipeline exists as the artifact of a managed development process, and the platform need not move data at all (DataKitchen moves nothing; Dagster orchestrates external compute). An ETL product lacking the dev→promote loop is not this Type; a DataOps platform with weak native movement capability is still this Type. Legacy enterprise ETL suites with versioned repositories and dev/test/prod environment promotion satisfy the L0 *structures* but their center of gravity remains data movement tooling — recorded as a soft edge, not a hard boundary failure.

**vs Continuous Integration Platform / Continuous Delivery Platform (§12):** CI/CD manages software source → build artifacts → running software; tests verify code behavior; the deliverable is software. DataOps manages data pipelines: the deployment unit includes pipeline configuration and environment-specific values; tests must validate **data** as well as code (data tests, data diffs); production work is unattended recurring execution against data systems rather than user-facing service delivery. The relationship is integrative, not duplicative: Prophecy documents external CI/CD (GitHub Actions/Jenkins via its build tool) as a first-class route; DataKitchen names Jenkins/CircleCI as the migration executors. CI/CD platforms lack pipeline runtime, data tests, and data-run monitoring. Boundary held.

**vs Data Quality Platform (§13, processed):** DQ's core = the defined rule/expectation as primary managed object + recorded pass/fail results attributed to data. DataOps embeds tests as one leg of the lifecycle loop (gates or steps) but does not center the rule/result record, and lacks pipeline development/promotion as its concern is quality measurement. Consistent with the keep-both outcome recorded in the data-quality-platform pass. Interlock direction: DQ tests are embedded *into* DataOps loops (DataKitchen "tests at every node" / TestGen integration; Dagster asset checks run alongside materializations).

**vs Data Observability Platform (§13, processed) — DISCHARGES this pass's pending flag:** the observability pass flagged "CI/CD shift-left impact previews ship inside observability products — capability relationship, cross-check recommended." Cross-check result: **capability relationship confirmed; Types distinct.** Observability's center is ambient health evaluation over the whole estate plus the incident loop; DataOps' center is the pipeline engineering lifecycle (develop→promote→operate). Observability products add preview/gating *features* at the promotion edge; DataOps platforms add monitoring *features* at the operations edge (Dagster+ alerts/health; Keboola telemetry; DataKitchen ships Observability as a sibling product). Primary objects do not coincide; keep-both.

**vs data orchestrators (Airflow/Dagster/Prefect market category — no dedicated §13 leaf):** pure orchestration = run DAGs/pipelines on schedules with run monitoring. That maps to L0 property 1+3 but not 2 as a *productized* feature. The commercial DataOps layer of these products (Dagster+ branch deployments) is what completes the loop; OSS orchestration cores lack the managed promotion leg. DataKitchen's own docs make this the explicit competitive contrast ("pipeline orchestrators… single tool context" vs meta-orchestrator managing "environments, deployment, version control, testing, collaboration, and process metrics"). Taxonomy note recorded in STATUS: the directory has no leaf for the pure data-orchestrator category; this leaf is the nearest home, with the orchestration-first pole as a variant.

**vs MLOps Platform (§13):** MLOps centers the model lifecycle (train/register/deploy/monitor models); DataOps centers data pipelines. They interlock (feature/training pipelines are DataOps artifacts feeding ML systems) but primary objects, test semantics (data quality vs model quality) and production artifacts (pipelines vs model endpoints) differ. Adjacent, not overlapping.

**vs Data Governance Platform / Data Catalog / Data Lineage (§13, processed):** governance = governed program rules; catalog = discovery entries for assets; lineage = flow graph of record. DataOps platforms consume/produce these as capabilities (lineage views of pipeline graphs; catalog entries of produced assets) without centering them. Held, consistent with sibling passes.

**Historical / market-sample check:** the category is young (methodology term mid-2010s; pure-play vendor founded 2013), so the check must ask whether older/leaner realizations still fit rather than whether the Type predates software. (a) A data team practicing DataOps with assembled tools (Git + CI + orchestrator + test framework) is a *practice*, not a platform — the Type requires the integrated product; no conflict. (b) Legacy enterprise ETL suites with versioned repos + dev/test/prod promotion + schedulers satisfy the L0 structures — they are admitted as an older realization of the same lifecycle, with the center-of-gravity caveat above; this prevents overfitting the definition to 2020s SaaS branching features. (c) The definition does not require Git specifically (Keboola's branching is platform-native), cloud delivery (self-hosted pole exists), or AI authoring.

## Uncertainties

- The exact strength of the testing leg in L0 was deliberately resolved as L1: DataKitchen treats embedded testing as definitional marketing; Keboola's branches enable but do not mandate tests; Dagster supports fully check-free operation. Testing as a *hard promotion gate* is variant, not invariant.
- Keboola's current marketing has de-emphasized the "DataOps Platform" label (now "AI & Data Platform"); the structural evidence (branches, flows, telemetry) is Tier-1 and current, but the *label's* future stability is not guaranteed. No action needed for the Type definition, which is label-independent.
- Prophecy's CI/CD features are Enterprise-Edition-gated; the free tier's loop depth could not be verified. Claims about Prophecy are therefore anchored to its documented Enterprise posture.
- Orchest sample lost (defunct domain); the open-source-IDE pole is covered only indirectly via Prophecy's low-code pole. Does not affect L0.
- DataKitchen's enterprise doc pages were not fetched (marked restricted); the public docs were sufficient. The "two pipelines" framing is vendor-terminology and was abstracted, not imported.
- Pure-play "DataOps" vendors other than DataKitchen (e.g., Ascend, Nexla) were not fetched; the four-sample spread satisfied stop conditions. If the taxonomy later needs a finer split of the end-to-end pole, additional sampling would be required.

## Final Synthesis

The market label "DataOps Platform" covers heterogeneous product poles (pure-play process platform, end-to-end governed platform, low-code IDE, orchestrator-plus) that all realize the same defining structure: **the engineering lifecycle of data pipelines as the product** — pipelines as versioned objects of record, a managed develop→promote loop over environments isolated from running production, and operational execution with monitoring of pipelines as ongoing work. Testing gates, Git/CI-CD machinery, lineage/observability surfaces, reuse libraries, secrets, and AI authoring are the standard capability package around that core, not the core itself. The Type is bounded from ETL/integration (movement-centered), CI/CD (code-artifact-centered), DQ (rule/result-centered), observability (estate-health-centered), and MLOps (model-centered) by primary-object and center-of-gravity tests; the relationships with all of them are integrative (each embeds into the DataOps loop or vice versa).
