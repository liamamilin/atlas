# Research Notes — Continuous Integration Platform

## Research Goal

Understand what a Continuous Integration Platform is as an Application Type: the core objects of its world model (pipeline, job, step, trigger, runner/agent, run record), who operates it and who consumes its output, how a change flows from commit to recorded verdict, which rules govern execution, and where it separates from neighboring developer-tooling Types (Build Automation System, Continuous Delivery Platform, Code Quality Platform, test tooling, artifact/package custody).

Two joint-review flags from previously processed siblings must be resolved or confirmed from this side:

1. **build-automation-system pass** (research/build-automation-system.md §Boundary Findings): "build tool = how one project builds; CI = when/where builds run for whom (triggers, hosted shared execution, orchestration across jobs, run history)."
2. **continuous-delivery-platform pass** (research/continuous-delivery-platform.md §Boundary Findings): "CI = commit-triggered build/test orchestration producing validated artifacts and fast feedback; CD = carrying versioned deliverables to named environments and recording what is deployed where. Octopus docs: 'CI is not CD'."

Also relevant: the code-quality-platform pass recorded "vs CI (triggered-by/reports-into, not orchestrates)".

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the Type is the execution-and-orchestration layer for validating source changes — a platform that watches version control, runs defined build/test jobs on shared infrastructure, records each run, and reports the verdict back to developers.
- Nearest neighbors to separate from: Build Automation System (what a build *is*, project-resident definitions + artifact production), Continuous Delivery Platform (what happens *after* a validated artifact — environments + deployment records), Code Quality Platform (long-term quality state + verdicts), Test Runner / E2E tooling (the tests themselves), Artifact Repository / Package Registry (custody/serving of outputs), Source Code Hosting Platform (often bundles CI as a feature area).
- Known risks: (a) over-fitting to the modern YAML-in-repo / SaaS-hosted pattern (Jenkins-era UI-configured jobs and 2001-era servers must still fit); (b) CI products that also model deploy steps blurring the CD seam; (c) the "CI/CD platform" marketing label fusing two Types.

## Research Questions

1. What are the core objects? (pipeline/workflow, job, step, stage, trigger/event, runner/agent/node, run/build record, artifact)
2. What triggers a run, and is change-binding definitional?
3. Where does execution happen, and who provides the compute? (hosted runners, self-hosted agents, queues)
4. How is work organized inside a run? (jobs, parallelism, dependencies, stages, matrix)
5. What is the unit of record, and what does it contain? (status taxonomy, logs, history)
6. How does feedback reach the development workflow?
7. What rules matter? (secrets/variables, concurrency, superseded builds, retries, manual gates, report-driven status)
8. What flows onward — artifacts, reports, downstream pipelines?
9. Where exactly are the seams vs Build Automation, CD, Code Quality, and custody Types?
10. Historical check: do 2001-era servers and the pre-YAML UI-configured model fit the same core?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Jenkins | self-hosted open-source automation server; legacy UI-configured model + modern pipeline-as-code in one product; historical continuity (Hudson heritage era) | market anchor, deepest documentation of agent/executor machinery |
| GitHub Actions | hosted, integrated into a source-code hosting platform | dominant modern realization; event/workflow/runner model documented at Tier 1 |
| GitLab CI/CD | CI/CD bundled inside a single-application DevOps suite | suite-module pole; YAML config, runners, variables at Tier 1 |
| Buildkite | hybrid: hosted orchestration + self-hosted (or vendor-hosted) agents | articulates the orchestration/execution split most explicitly; step-type taxonomy at Tier 1 |

Historical anchors (boundary/historical evidence only, not shaping the modern model): **CruiseControl** (2001-era open-source CI tool, still-hosted docs) and **Travis CI** (hosted-CI-for-open-source pioneer, documentation structure observable).

CircleCI (SaaS specialist pole) was attempted: docs landing returned a content stub this pass, and it was unreachable (404×2) during the continuous-delivery pass. Dropped per the network limitation rule; recorded under Uncertainties.

## Sources

All fetched 2026-09-07:

- Jenkins — https://www.jenkins.io/doc/ , https://www.jenkins.io/doc/book/pipeline/ , https://www.jenkins.io/doc/book/glossary/
- GitHub Actions — https://docs.github.com/en/actions/about-github-actions/understanding-github-actions
- GitLab — https://docs.gitlab.com/ci/
- Buildkite — https://buildkite.com/docs , https://buildkite.com/docs/pipelines/glossary , https://buildkite.com/docs/agent
- CruiseControl — https://cruisecontrol.sourceforge.net/
- Travis CI — https://docs.travis-ci.com/ (documentation surface/TOC; individual articles not fetched)
- CircleCI — https://circleci.com/docs/ (stub only — unusable)

## Product Observations

### Jenkins

Evidence layer: A (direct observation, official docs ×3 pages).

- Self-description: "a self-contained, open source automation server which can be used to automate all sorts of tasks related to building, testing, and delivering or deploying software"; functionality extended through plugins; also characterized as "fundamentally, an automation engine which supports a number of automation patterns… from simple continuous integration to comprehensive CD pipelines".
- Pipeline: "a user-defined model of a CD pipeline"; defined in a text file (Jenkinsfile) committed to the project's source control — "Pipeline-as-code… treating the CD pipeline as a part of the application to be versioned and reviewed like any other code". Benefits listed: automatic pipeline build process for all branches and pull requests, code review of the pipeline, audit trail, single source of truth.
- **Legacy model documented in-product**: "Jenkins has always allowed rudimentary forms of chaining Freestyle Jobs together to perform sequential tasks… Pipeline makes this concept a first-class citizen." Freestyle jobs are user-configured (UI) descriptions of work. Pipeline definition is also possible "through the classic UI" — the Jenkinsfile is best practice, not the only surface.
- Core concepts: **Pipeline** (user-defined model; entire build process incl. stages for building, testing, delivering); **Node** ("a machine which is part of the Jenkins environment and is capable of executing a Pipeline"; both controller and agents are nodes); **Stage** ("a conceptually distinct subset of tasks… e.g. 'Build', 'Test' and 'Deploy'… used by many plugins to visualize or present status/progress"); **Step** ("a single task… tells Jenkins *what* to do at a particular point"; e.g. `sh 'make'`).
- Glossary machinery: **Agent** ("a machine, or container, which connects to a Jenkins controller and executes tasks when directed by the controller"); **Controller** ("central, coordinating process which stores configuration, loads plugins, and renders the various user interfaces"); **Executor** ("a slot for execution of work… A Node may have zero or more Executors… how many concurrent Jobs or Pipelines are able to execute on that Node"); **Queue** behavior (node block "adds an item to the Jenkins queue. As soon as an executor is free on a node, the steps will run"); **Workspace** ("a disposable directory on the file system of a Node where work can be done"); **Label** (user-defined text for grouping agents, e.g. `linux`, `docker`); **Cloud** (system configuration providing dynamic agent provisioning, e.g. Azure VM Agents / Amazon EC2 plugins).
- **Build** = "result of a single execution of a job". Status taxonomy: Successful ("no compilation errors"), Failed ("fatal error"), **Unstable** ("built successfully and one or more publishers report it unstable — e.g. JUnit test fails"), Stable ("successful and no publisher reports it unstable"), Aborted (interrupted). **Publisher** = "part of a Build after the completion of all configured Steps which publishes reports, sends notifications, etc." The `junit` step aggregates test reports.
- **Artifact** = "an immutable file generated during a Build or Pipeline run which is **archived** onto the Jenkins Controller for later retrieval by users". Fingerprint = hash to track artifact usage across pipelines.
- **Trigger** = "a criteria for triggering a new Pipeline run or job" (glossary). **Upstream/Downstream** = configured pipelines that trigger / are triggered as part of another's execution.
- Pipeline properties: **Durable** ("survive both planned and unplanned restarts of the Jenkins controller"), **Pausable** ("can optionally stop and wait for human input or approval before continuing"), fork/join, parallel, extensible DSL, shared libraries.

### GitHub Actions

Evidence layer: A (direct observation, official docs ×1 page).

- Self-description: "a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production." Goes beyond CI/CD: workflows can run on other repository events (e.g. label issues).
- **Workflow** = "a configurable automated process that will run one or more jobs… defined by a YAML file checked in to your repository" (`.github/workflows`); triggered by an event in the repository, manually, or on a defined schedule; a repository can have multiple workflows; workflows can reference other workflows (reuse).
- **Event** = "a specific activity in a repository that triggers a workflow run. For example… someone creates a pull request, opens an issue, or pushes a commit"; also schedule, "posting to a REST API" (repository dispatch), manual.
- **Job** = "a set of steps in a workflow that is executed on the same runner"; steps are "a shell script… or an action"; steps run in order and share data; steps can run concurrently in selected cases. Jobs: "by default, jobs have no dependencies and run in parallel"; dependencies make a job wait. **Matrix** = "run the same job multiple times, each with a different combination of variables—like operating systems or language versions."
- **Action** = "a pre-defined, reusable set of jobs or code" (checkout, toolchain setup, cloud authentication); own or from GitHub Marketplace.
- **Runner** = "a server that runs your workflows when they're triggered. Each runner can run a single job at a time." GitHub provides hosted Ubuntu/Windows/macOS VMs; "each workflow run executes in a fresh, newly-provisioned virtual machine"; larger runners available; self-hosted runners for different OS/hardware.
- Advanced features named: concurrency, test matrices; new direction: agentic workflows authored in natural language (Copilot) — noted as an era signal, not structural.

### GitLab CI/CD

Evidence layer: A (direct observation, official docs ×1 page).

- Framing: "CI/CD is a continuous method of software development, where you continuously build, test, deploy, and monitor iterative code changes… GitLab CI/CD can catch bugs early in the development cycle." Part of the DevSecOps lifecycle (Plan/Create/Verify/Secure/Release/Monitor) — suite context.
- **`.gitlab-ci.yml`** at project root (custom filename allowed) "defines the stages, jobs, and scripts that make up your CI/CD pipeline, including variables, job dependencies, and when and how each job runs."
- "Pipelines are made up of stages and jobs: **Stages** define the order of execution. Typical stages might be `build`, `test`, and `deploy`. **Jobs** specify the tasks to be performed in each stage… a job can compile or test code."
- **Triggering**: "GitLab creates a pipeline each time it's triggered, for example, by a commit, a merge request, on a schedule, or when you manually run one. **A runner then executes the pipeline's jobs.**"
- **Runners**: "the agents that run your jobs… can run on physical machines or virtual instances"; a container image can be specified per job in YAML; "the runner loads the image, clones your project, and runs the job either locally or in the container." GitLab.com provides shared runners (Linux/Windows/macOS); own runners can be registered (self-managed instances or local machine).
- **CI/CD variables**: key-value pairs storing configuration and "sensitive information, like passwords or API keys"; hard-coded, set in project settings, or dynamically generated; scopes: project, group, instance; custom + predefined (context about current job/pipeline/environment); **protected** variables ("restrict access to jobs running on protected branches or tags") and **masked** variables ("hide variable values in job logs").
- Expressions (`$[[ ]]`) validated at pipeline creation; inputs context; matrix context for 1:1 mappings between matrix jobs.
- **CI/CD components**: "a reusable pipeline configuration unit… publish… to the CI/CD Catalog"; component templates for common tasks. Also documented areas: pipeline security, secrets manager, external secrets, testing, Auto DevOps, migration guides.

### Buildkite

Evidence layer: A (direct observation, official docs ×3 pages).

- Positioning: Pipelines = "Powerful CI/CD built to scale on **your choice of infrastructure**" — the explicit hybrid pitch; separate product areas on the same platform: Pipelines, Test Engine, Package Registries (boundary evidence for custody Types).
- **Agent**: "a small, reliable, and cross-platform build runner that connects your infrastructure to Buildkite. It polls Buildkite for work, runs jobs, and reports results… You need at least one agent to run builds." Responsibilities: "polling buildkite.com for work, running a build's jobs, reporting back the status code and output log of the job, and uploading the job's artifacts."
- Mechanics: agent polls the agent API over HTTPS ("no need to forward ports or provide incoming firewall access"), registers into the organization's agent pool, polls for work, accepts a job, executes the command, streams output back, posts the final exit status. Meta-data and artifact commands let "completely isolated build jobs… have access to shared state and data storage across any number of machines and networks."
- **Self-hosted vs hosted agents**: self-hosted = "you provision, scale, and maintain your own servers" (full control, on-prem/own-cloud for strict security, persistent or ephemeral); hosted = fully managed (Linux/macOS/Windows, "always ephemeral, destroyed after each job", auto-scaling, NVMe-backed cache volumes). **Ephemeral agent**: operates only for the duration of one job.
- **Pipeline** = "a container for modeling and defining workflows… a series of steps to achieve goals like building, testing, and deploying software." **Build** = "a single run of a pipeline. You can trigger a build in various ways, including through the dashboard, API, as the result of a webhook, on a schedule, or even from another pipeline using a trigger step." **Job** = "the execution of a command step during a build"; job states: pending, scheduled, running, finished, failed, canceled, etc.
- **Step types**: command (shell commands on one or more agents), wait (pauses build until previous jobs complete), **block** ("pauses a build until it is manually unblocked… often used as a manual approval gate before a sensitive step, such as a production deployment"), input (collects information from a user), **trigger** ("creates a build on another pipeline… the standard way to chain pipelines together, such as a build pipeline triggering a separate deployment pipeline"), group. Step outcomes: passed / soft_failed ("surface… but does not block downstream steps") / hard_failed / errored.
- **Build matrix** ("expands a single command step into multiple jobs, one for each combination of values… operating system and language version"); **parallelism** (same step across N jobs; with test splitting shards long test suites); **concurrency group** (named limit across builds/pipelines; "commonly used to serialize access to a shared resource, such as a deployment target"); **retry** (automatic by exit status / agent lost; manual); **skip and cancel intermediate builds** ("when several commits arrive on the same branch in quick succession… only the latest commit is built").
- **Agent targeting**: steps select agents via `key=value` tags (`queue=ios`, `os=linux`); **queues** isolate agent pools; **clusters** group queues + pipelines (team self-management).
- **Artifacts**: "file generated during a build… Buildkite-managed storage service or a third-party cloud storage service like Amazon S3, Google Cloud Storage, or Artifactory… storing assets like logs and reports, or passing files between steps." **Annotations**: rich content attached to the build page (test failure summaries, deployment links). **Build metadata**: key/value pairs passed between steps (commit reference, approval decision).
- **Notifications**: outbound messages on build events (starting, passing, failing) to email, Slack, webhooks. **Scheduled builds**: cron-defined recurring builds with branch/commit/message/environment. **Dynamic pipelines**: steps defined at runtime via pipeline upload. **Signed pipelines**: cryptographic signing of step definitions ("an agent only runs steps signed by a trusted key"). **OIDC**: short-lived tokens for job→cloud authentication without long-lived secrets. **Pipeline templates**: org-level reusable configuration ("platform teams provide a consistent, governed starting point"). **Merge queue** integration. **Hooks**: scripts at named lifecycle points (environment, checkout, pre-command, command, post-command, pre-exit).

### CruiseControl (historical anchor, 2001-era)

Evidence layer: A (direct observation of still-hosted project docs).

- "Both a continuous integration tool and an extensible framework for creating a custom continuous build process"; "dozens of plugins for a variety of source controls, build technologies, and notifications schemes including email and instant messaging"; "A web interface provides details of the current and previous builds"; builders for Ant/NAnt/Maven/Phing/Rake/Xcode plus a catch-all exec builder; XFDs (eXtreme Feedback Devices) driving physical displays from build results.
- Reading against the candidate core: change-binding (source-control plugins), delegated builds (builders invoke build tools), notification schemes (feedback), current + previous build details (run records) — all present in 2001. No YAML, no cloud, no containers.

### Travis CI (historical hosted pioneer)

Evidence layer: A-lite (documentation surface/TOC observed; individual articles not fetched).

- Documentation structure directly observable: onboarding, "Core Concepts", "Customizing the Build", "Building Pull Requests", "Cron Jobs", "Job Lifecycle", "Build Matrix", "Build Stages", "Conditional Builds, Stages, and Jobs", caching dependencies, deployment providers, "Configuring Notifications", "Showing Build Status Images" (badges), API-triggered builds, hosted environment references (Ubuntu/Windows/FreeBSD images), Enterprise (self-hosted) offering.
- Confirms the hosted-CI shape: repository-provider integration, config-driven builds, matrix/stages, badges, notifications.

## Cross-product Comparison

| Concept | Jenkins | GitHub Actions | GitLab CI/CD | Buildkite |
|---|---|---|---|---|
| Run definition | Pipeline (Jenkinsfile in SCM **or** classic-UI config); legacy: Freestyle job (UI) | Workflow (YAML in `.github/workflows`, checked in) | Pipeline (`.gitlab-ci.yml` at project root) | Pipeline of steps; dynamic pipelines can generate steps at runtime |
| Decomposition | Pipeline → Stage → Step | Workflow → Job → Step | Pipeline → Stage → Job → script | Pipeline → Step (command/wait/block/input/trigger/group) → Job |
| Trigger | "criteria for triggering" runs/jobs; multibranch auto-creates builds for branches & PRs | repository events (push, PR, issue), schedule, REST dispatch, manual | commit, merge request, schedule, manual | webhook, dashboard, API, schedule, trigger step |
| Execution capacity | Agent (machine/container) directed by controller; Executor slots per Node; queue; labels; cloud-provisioned agents | Runner (hosted VM per job; self-hosted option); one job at a time | Runner ("the agents that run your jobs"); shared on GitLab.com or registered | Agent polls for work; self-hosted or Buildkite-hosted; tags/queues/clusters |
| Run record | Build (Successful/Failed/Unstable/Stable/Aborted) | Workflow run (fresh VM per run) | Pipeline (created per trigger) | Build (states) + job states + annotations |
| Logs/output | console output per build (implied by status/UI; not fetched in detail) | (not fetched in detail) | job logs; masked variables hide values in job logs | agent "reporting back the status code and output log of the job" |
| Artifacts | immutable files archived on controller, retrievable by users; fingerprints | (not fetched in detail) | (not fetched in detail) | Buildkite-managed or S3/GCS/Artifactory storage; passing files between steps |
| Reuse units | plugins, shared libraries, pipelines-as-upstream/downstream | actions + Marketplace; reusable workflows | components + CI/CD Catalog; templates | plugins, pipeline templates, dynamic pipelines |
| Variables/credentials | (not fetched in detail) | (not fetched in detail) | CI/CD variables: custom/predefined, project/group/instance scopes, protected + masked | hooks-managed secrets; OIDC short-lived tokens; build metadata |
| Matrix | (not fetched in detail) | documented (OS/language combos) | matrix context in expressions | build matrix; parallelism |
| Parallel / order | fork/join, parallel stages | jobs parallel by default, dependencies for order | stages define order | parallelism attribute; wait steps; concurrency groups |
| Manual gate | "Pausable… wait for human input or approval" | (not fetched) | (manual run only observed) | block step (approval gate), input step |
| Notifications | publishers "send notifications" | (not fetched) | (not fetched) | build events → email/Slack/webhooks |
| Superseded-run handling | (not observed) | (not observed) | (not observed) | skip queued / cancel running intermediate builds |

Cross-product commonalities (layer B): all four sampled products expose (1) change-bound triggering including pull/merge-request flows, (2) a hierarchical run definition (pipeline/workflow → jobs/steps) held as configuration, (3) a named runner/agent concept executing jobs on capacity the platform coordinates, (4) recorded runs with status and accumulated history, (5) feedback into the development workflow (PR/branch status, dashboards, notifications). Three of four document matrix expansion and scheduled runs; two document artifacts and manual gates directly.

## Canonical Abstraction Hierarchy

### Level 0 — Defining Invariant

The smallest structure without which the product stops being a CI platform:

1. **Change-bound automated runs** — runs start automatically in response to version-control change events (push/commit, pull request, merge request). Schedule, manual, API, and pipeline-to-pipeline triggers are universal extensions, but binding to source changes is what makes the loop "continuous integration"; a platform that only schedules work without change-binding is a job scheduler.
2. **Managed run definition** — the work is expressed as named, reusable platform-held configuration: a pipeline/workflow decomposing into jobs, jobs into steps. Modern products version this file with the project; the legacy model holds it in platform UI. (Jenkins documents both surfaces — therefore the *file-in-repo* implementation cannot be definitional.)
3. **Platform-coordinated execution capacity** — jobs execute on runners/agents/nodes the platform registers, schedules onto (queue/pool), and monitors — capacity distinct from each developer's own machine, hosted by the vendor or self-managed via agents.
4. **Recorded runs with outcomes** — every run is a durable record: status (success/failure plus intermediate states) and log output, accumulating into per-pipeline history; the platform is the system of record for what happened to each change.
5. **Feedback into the development workflow** — outcomes surface where development happens: commit/PR status, run dashboards, notifications, badges.

Canonical purpose (framing, not a sixth invariant): the jobs canonically build and test the software, so each change receives a validation verdict — "continuous integration" as practiced since the 2001-era servers. The Type structurally orchestrates *defined jobs*; build/test is the canonical content, not a mechanism requirement.

### Level 1 — Common Mature Structure

Present across the sample, expected by the market, not definitional:

- job-level parallelism with dependency ordering; stage/phase grouping for visualization
- matrix expansion (one definition × configuration combinations)
- reusable units (actions/components/shared libraries/plugins) with shared catalogs
- variables and credential injection with scoping and log masking (protected/masked variables, OIDC tokens)
- artifacts: immutable run outputs, stored platform-side or in external storage, retrievable and passable between steps
- test-report ingestion with status semantics beyond binary (Unstable publishers; soft fail; annotations)
- manual gates / input steps inside runs
- pipeline chaining (upstream/downstream, trigger steps)
- notifications (email/chat/webhook) and status badges
- scheduled (cron) builds
- container images per job / ephemeral environments (hosted runners; ephemeral agents)
- retry policies; concurrency groups; superseded-build skipping/canceling (2 products documented)
- API/CLI access; permission/administration surfaces; audit

### Level 2 — Variant / Optional Structure

- where execution capacity lives: vendor-hosted only ↔ self-hosted only ↔ hybrid (orchestration hosted, agents anywhere)
- packaging: standalone automation server ↔ suite module (single-application DevOps platform) ↔ capability of a code-hosting platform ↔ SaaS specialist
- deployment steps inside pipelines (CD-flavored usage) — possible everywhere, structural nowhere in the sample
- dynamic pipelines (steps computed at runtime); signed pipelines; merge-queue integration
- ephemeral vs persistent agents; agent pools/queues/clusters self-management
- test-analytics/flaky-test management layers; package registries as sibling products
- enterprise governance (org-level templates, audit logs, clusters); self-hosted enterprise editions; billing by usage
- AI/agentic assistance (era signal, single product observed)

### Level 3 — Vendor-specific Structure (research notes only)

- Jenkins: controller/agent split, executor slots, Stable-vs-Unstable publisher semantics, freestyle jobs, Jenkinsfile DSL (declarative/scripted), Update Center, LTS line, Blue Ocean, fingerprints, multibranch
- GitHub Actions: `.github/workflows` location, Marketplace, larger runners, agentic (Copilot) workflows, "repository dispatch" REST trigger
- GitLab: instance/group/project variable scopes, protected branches/tags coupling, CI/CD Catalog, Auto DevOps, Duo, secrets manager, DevSecOps stage framing
- Buildkite: clusters/queues terminology, Test Engine (bktec, quarantine/mute/skip states), signed pipelines, Elastic CI Stack for AWS, NVMe cache volumes, annotations, no-inbound-firewall polling model
- Travis CI: per-language build-image references, status images, deployment provider catalog

## Rejected Findings (deliberately NOT definitional)

- **YAML / pipeline-as-code in the repository**: Jenkins explicitly supports classic-UI pipeline configuration and documents freestyle jobs as its long-standing model — the Type predates and survives without in-repo config files. The definitional concept is *platform-held, reusable run definition*; versioned config files are the dominant modern implementation.
- **YAML specifically**: Jenkins Pipeline DSL is Groovy-based; "declarative configuration language" is the concept, YAML is today's common serialization.
- **Fresh-environment-per-run**: GitHub (fresh VM always) and Buildkite-hosted (ephemeral always) vs persistent Jenkins agents with disposable workspaces — common for hosted SaaS, not invariant.
- **Containers**: Jenkins agents are machines or containers; CruiseControl predates both. Container images per job = common, not defining.
- **Test execution as a mechanism requirement**: no sampled product structurally requires test jobs; a CI platform runs defined jobs, canonically including build and test. Rejected as an invariant, kept as purpose framing.
- **Cloud/SaaS delivery**: self-hosted open-source (Jenkins) and hybrid (Buildkite) poles refute.
- **Deploy capability**: deploy stages appear in examples across products, but no sampled CI product keeps environments/deployment records as first-class objects — that is the CD Type's record model.
- **Public marketplace/ecosystem as defining**: reuse units are common; marketplace mechanics (GitHub Marketplace, GitLab Catalog, Update Center) are vendor-shaped.

## Boundary Findings

- **vs Build Automation System** (sibling pass recorded the seam from the build-tool side — confirmed from the CI side): the build tool answers "how does this project build" (project-resident definition, dependency-ordered execution, artifact production, invoked by a developer or by a CI agent); the CI platform answers "when/where do builds run, for whom, with what history" (triggers, shared execution capacity, orchestration across jobs, run records). CI-side evidence: Jenkins jobs invoke build tools as steps (`sh 'make'` — "Using Build Tools" tutorial area); CruiseControl ships "builders" for Ant/Maven/Rake while remaining a CI tool — the build engine is delegated, not embodied. Removal test: remove triggers + shared capacity + run records → build tool; remove the project-resident build definition → CI platform. Both products coexist in one pipeline without fusion.
- **vs Continuous Delivery Platform** (sibling pass recorded the seam from the CD side — confirmed from the CI side): CI ends at producing validated build/test verdicts and artifacts; CD owns named environments, executes deployments, keeps "what is deployed where" records. CI-side evidence: every sampled CI product *can model* deploy steps in pipelines (GitLab's example stages include `deploy`; Buildkite's block step "manual approval gate before a sensitive step, such as a production deployment"; Buildkite trigger step "build pipeline triggering a separate deployment pipeline"; Jenkins pipeline examples include Deploy stages) — but deployment *records/environments* are absent from every sampled CI object model; Buildkite chains to a *separate deployment pipeline* rather than owning environment state; Jenkins artifacts are "archived… for later retrieval by users", not delivered to environments. Working test (both sides now agree): center of gravity ends at validated artifact + feedback → CI; extends to environment delivery + deployment records → CD. "CI/CD platform" branding (GitHub's, GitLab's) is suite packaging, not Type fusion — consistent with the CD pass's GitLab observation.
- **vs Code Quality Platform** (sibling pass recorded "CI triggered-by/reports-into, not orchestrates" — consistent): CI platforms run checks as jobs and ingest their outputs (Jenkins junit publisher marks builds Unstable; Buildkite annotations surface test failures), but long-term quality state (issues, metrics, ratings, verdict standards) lives in the code-quality Type. A quality scanner runs *inside* a CI job; the CI platform records the job, not the quality ledger.
- **vs test tooling (Unit/Integration Test Runner, E2E Testing)**: the test tool defines and runs tests; the CI platform provides the triggered execution shell and the record. Jenkins' `junit` step and Buildkite's test-splitting consume test output produced by the project's own test runner.
- **vs Artifact Repository / Package Registry**: custody-and-serving of published artifacts vs producing run outputs. CI-side evidence: Buildkite ships Package Registries as a *separate product* on the same platform; Jenkins archives build artifacts on the controller for retrieval by users (run outputs), with fingerprints to track usage — a record-keeping convenience, not a registry service.
- **vs Source Code Hosting Platform**: hosting platforms integrate CI as a feature area (GitHub Actions lives inside a hosting platform; GitLab pipelines inside a single-application suite; multibranch CI binds to branches/PRs). The CI capability remains a distinct Type — trigger/run/record machinery — whether standalone, bundled, or integrated; the hosting platform's defining objects (repositories, reviews) are the CI's *event sources*, not its core model.
- **vs generic job schedulers / workflow orchestrators**: scheduled and API triggers exist in every product, and pipeline structure resembles DAG orchestration — but change-binding to version control, the PR/commit feedback loop, and build/test workload semantics distinguish the Type. Remove change-binding → scheduler/orchestrator, not CI.
- **"去掉什么就变成另一个 Type" 判据**: remove recorded runs/history → ad-hoc remote build execution, not CI; remove change-trigger → job scheduler; remove platform-provided execution capacity (definitions run on developer machines) → build tool + scripts; remove the jobs/pipeline decomposition (one monolithic command) → a build script; add named environments + deployment records → Continuous Delivery Platform; add long-term issue/metric state + quality verdicts → Code Quality Platform.

## Historical / Market-Sample Check

- **2001-era CruiseControl** fits the candidate core fully: source-control-bound triggering (source-control plugins), build delegation (builders for Ant/Maven/Rake/exec), notification schemes (email/IM), recorded runs ("details of the current and previous builds"). It has none of the modern L1 (YAML, cloud runners, containers, matrices, marketplace) and is unmistakably a CI tool → the definition is not over-fit to the modern era.
- **Pre-YAML in-product legacy model**: Jenkins documents freestyle jobs ("Jenkins has always allowed…") and classic-UI pipeline configuration as first-class alternatives — the definitional core deliberately does not require config-files-in-repo, so the 2005–2015 UI-configured era satisfies it.
- **Hosted pioneer (Travis CI)**: documentation surface shows the hosted-CI shape (repo-provider binding, matrix/stages, cron, badges, enterprise) consistent with the core; no structural deviation observed.
- Regional/platform-native check: self-hosted (Jenkins — globally deployed, region-neutral), hosted SaaS (GitHub/Buildkite/GitLab.com), and Berlin-headquartered hosted pioneer (Travis) span the deployment spectrum; no region-specific structure entered the core. Check passed.

## Uncertainties

- **CircleCI under-sampled**: docs landing returned a content stub this pass and 404×2 in the prior CD pass; the SaaS-specialist pole (orbs, executors, performance-focused workflows) is unverified. Category claims are worded "across the sampled products".
- GitHub Actions secrets, environments, caching, and approvals were not directly observed this pass (only named features: concurrency, matrix, runners); no claims made about them for GitHub specifically.
- GitLab's deployment/environment machinery (its CD half) was not fetched; nothing asserted about GitLab keeping deployment records.
- Travis CI observed at documentation-structure level only; no operational details claimed.
- Jenkins console-log surfaces, JCasC, and the multibranch article body were not fetched; multibranch behavior cited from the Pipeline overview page only.
- No numeric limits (concurrency caps, minutes, timeouts, queue sizes) asserted anywhere — none were observed in fetched pages.

## Final Synthesis

A Continuous Integration Platform is the development team's automated validation infrastructure: it watches version control for changes, automatically runs each change through a platform-defined pipeline of jobs on coordinated execution capacity, records every run (status + logs) as the durable verdict on that change, and surfaces the verdict where development happens. The defining core is five-fold — change-bound automated runs, managed run definitions, platform-coordinated execution capacity, recorded run outcomes, development-workflow feedback — with build-and-test as the canonical workload. Everything else (matrix, artifacts, secrets, gates, chaining, notifications, where the compute lives) is mature-market structure layered on that loop. The Type sits between the Build Automation System (which defines what a build *is* and gets invoked as a step) and the Continuous Delivery Platform (which takes validated artifacts to environments and keeps deployment records); "CI/CD platform" product branding spans the seam by packaging, not by fusion.
