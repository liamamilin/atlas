# Continuous Integration Platform

## Overview

A **Continuous Integration Platform** is the development team's automated validation infrastructure. It watches a version-control system for changes to the code, and each time a change arrives it automatically runs that change through a defined sequence of build and test jobs on execution capacity the platform provides, records the result of every run, and reports the verdict back to the place where the team develops the software.

The problem it solves is continuity of integration: when many people change a shared codebase, waiting days or weeks between integrations makes failures large and hard to localize. A CI platform inverts that — every change is built and tested immediately and automatically, so a defect is discovered by the machine within minutes of the commit that caused it, attributed to a specific change, and surfaced to the person who made it.

Its boundary: a CI platform ends at a **validated, recorded verdict on a change** — a green or red run, plus any outputs (artifacts, reports) the jobs produce. It does not own what happens after: carrying the software to servers, recording what is deployed where, or holding a long-term ledger of code-quality problems. It also does not decide *how* a project builds — that lives in the project's build tool, which CI invokes.

## Users & Context

**Primary users** are software developers, in two roles:

- **Authors of changes** — they push commits and open pull requests; the platform runs automatically in response, and they consume the verdict (a status on their commit, a failed-log link) without operating the platform itself. For most developers the CI platform is infrastructure they read, not software they configure.
- **Pipeline authors** — developers or platform engineers who write the run definitions: which jobs a pipeline contains, what commands run, on what environment, under which conditions.

**Secondary users**:

- **Release/build engineers and platform teams** — operate the execution capacity (agent fleets, queues, shared secrets), tune reliability and speed, and often provide reusable pipeline components for the rest of the organization.
- **Administrators** — manage permissions, integrations, and organization-level policy.

The context is the development workflow of a team or organization using version control. The platform sits beside the version-control system (or inside the same product), constantly converting change events into runs and runs into verdicts. Its "customers" are other tools and humans: pull-request pages, chat channels, dashboards, badge images, downstream deployment tooling.

## Core Model

### The defining structure

```text
Version-control change event (push / pull request / merge request)
  ↓ triggers automatically
Run of a Pipeline  (the unit of work, defined as reusable configuration)
  → decomposes into Jobs
    → each Job is a sequence of Steps (commands)
  ↓ executes on
Runners / Agents  (execution capacity the platform coordinates)
  ↓ produces
Recorded Run: status + logs (+ artifacts, reports)  — kept as history
  ↓ surfaces as
Feedback: verdict on the commit / pull request, dashboards, notifications
```

Five properties. Remove any one and the product stops being a CI platform:

- **Change-bound automated runs.** Runs start on their own, in response to changes pushed to version control — a commit, a pull request, a merge request. This binding is what makes the integration *continuous*. Schedules, manual runs, API calls, and pipeline-triggering-pipeline are widely available across mature products, but they are extensions; a platform that only executes scheduled jobs without watching source changes is a job scheduler.
- **A managed run definition.** The work is not typed by hand each time — it is held by the platform as named, reusable configuration: a *pipeline* (or *workflow*) decomposing into *jobs*, each job a sequence of *steps*. In current products this definition is almost always a configuration file versioned alongside the code, so pipelines are reviewed and changed like code; older products held the definition in forms filled in through a web UI. Both satisfy the definition — what matters is that the definition is managed, reusable, and belongs to the project.
- **Platform-coordinated execution capacity.** Jobs do not run on the developer's machine. They run on *runners* or *agents* — machines or containers that register with the platform, wait for work, execute jobs, and report back. The platform schedules waiting work onto this capacity (queues, agent pools), whether the capacity is operated by the vendor or by the customer. This is what lets one shared "build farm" serve a whole organization.
- **Recorded runs with outcomes.** Every execution — whether it passed or failed — becomes a durable record: a status, the complete log output, and any published artifacts or reports. Runs accumulate into per-project history, which is what makes the platform the *system of record* for the question "what happened to this change?" A verdict that isn't recorded can't be integrated into.
- **Feedback into the development workflow.** The verdict travels back to where development happens: the commit or pull request shows green or red, dashboards list runs, chat channels and email receive failure notices, badge images show project health. The feedback loop — change → run → verdict → developer → fix → change — is the entire point of the Type.

The canonical workload inside those jobs is **building and testing the software**, which is what gives each change its validation verdict. Structurally, though, a job can run any command; the platform orchestrates *defined jobs*, and build/test is what teams conventionally put in them.

### What mature products add

Products in this category commonly carry most of the following. They make the platform practical at team scale but do not define it:

- **Parallel jobs and ordering** — independent jobs run simultaneously; dependencies make jobs wait for others; stages or wait points group work into phases for readability.
- **Matrix expansion** — one job definition multiplied across configuration combinations (operating systems, language versions), each combination a separate job in the same run.
- **Reusable building blocks** — packaged steps or configuration fragments (shared libraries, reusable components, action libraries) that teams publish and reuse across projects.
- **Variables and credential injection** — configuration values and secrets passed into jobs, with scoping rules (per project, group, or organization) and protections such as hiding secret values in logs or restricting variables to trusted branches.
- **Artifacts** — files produced by a run (binaries, packages, reports), stored by the platform or in connected storage, retrievable later and passable between jobs in the same run.
- **Test-report handling** — jobs can publish test results that shape the run's status; several products distinguish "the build compiled but tests failed" from outright build failure, and can surface failures as summaries attached to the run.
- **Manual gates** — a run can pause and wait for a person to approve or provide input before continuing, commonly before sensitive operations such as production deployment.
- **Pipeline chaining** — one pipeline triggering another (build pipeline → deployment pipeline), passing data along.
- **Notifications and badges** — outbound messages on run events (started, passed, failed) to email, chat, or webhooks; embeddable status images.
- **Scheduled runs** — recurring runs on a time trigger (nightly builds).
- **Containerized job environments** — jobs run inside a chosen container image, or on fresh ephemeral machines per run in hosted offerings.
- **Concurrency control and retries** — limits on how many jobs sharing a resource run at once; automatic or manual re-execution of failed jobs.
- **Administration surfaces** — permissions, integration settings, audit logs, API and CLI access.

### One structure, many implementations

```text
Concept:            change-bound trigger
Implementations:    push/commit events, pull/merge-request events,
                    plus schedule, manual, API, pipeline-to-pipeline triggers

Concept:            run definition
Implementations:    YAML file in the repository (dominant today),
                    Groovy-style DSL file, web-UI-configured jobs (legacy model)

Concept:            execution capacity
Implementations:    vendor-hosted ephemeral machines, customer-operated
                    agent fleets, dynamic cloud-provisioned agents

Concept:            run record
Implementations:    "build" with statuses including intermediate states
                    (e.g. built-but-tests-failed), "pipeline" / "workflow run"
```

A reader who has only seen a modern SaaS product should still recognize an older self-hosted server from the 2000s as the same Type: it watched source control, ran builds on its agents, and kept a history of every build.

## How It Works

### Configure: define the pipeline

A pipeline author defines, for a project, what should happen when changes arrive: which jobs exist, what commands each runs, what environment each needs, which jobs depend on which, and under which branch/tag conditions each applies. The definition is saved as configuration belonging to the project — in current practice a file committed to the repository, so it evolves under the same review as the code it validates. Mature products supplement this with reusable shared components and, in some, the option to compute steps at runtime.

### Trigger: a change starts a run

When a change reaches version control — a pushed commit, an opened pull request, a proposed merge — the platform creates a **run** (called a *build* or *pipeline* depending on the product). The run is created automatically; nobody presses a button. The same is true for pull requests: each proposal gets its own run, so review can proceed against a real validation rather than hope. Schedules, manual clicks, API calls, and upstream pipelines can also start runs.

### Schedule and execute: jobs land on capacity

The platform places the run's jobs onto its execution capacity. An agent or runner that is idle accepts (or is handed) a job; the job's steps execute in order — checking out the code at the exact change being validated, preparing the environment (often a specified container image), then running the defined commands: invoke the project's build tool, run its test suites, run whatever checks are configured. Independent jobs proceed in parallel; dependent jobs wait. Output streams back to the platform as it is produced.

### Record: the run becomes history

When the jobs finish, the run gets its verdict — success, failure, or an intermediate state some products maintain (built fine, tests failed). The complete log is attached and kept. Anything jobs published — binaries, packages, test reports — is stored as artifacts. The run joins the project's history: every change the platform ever saw, and what happened to it, remains queryable.

### Feed back: the verdict returns to development

The run's status appears on the commit and pull request that caused it; dashboards list recent runs per project with trends; notifications push failures to chat or email. The author of a broken change reads the log, fixes the code, pushes — and the loop runs again. This loop, repeated many times a day, is the "continuous integration" the Type is named for.

### Hand off: what continues downstream

A green run's artifacts (the built outputs) are available to whatever comes next: a triggered downstream pipeline — often deployment — an artifact repository, or a human retrieving a package. Several products also gate the handoff on a person: a run pauses until someone approves continuation before anything sensitive, such as a production deployment, may proceed.

## Interfaces

Conceptual surfaces; names and layouts vary by product.

### Configuration surface

Where run definitions live.

- the pipeline definition itself (a versioned configuration file in practice; a form-driven editor in the legacy model)
- primary actions: define jobs/steps/conditions, commit the definition, preview or validate it

### Run list (dashboard)

The project's history of runs — the platform's front door for consumers.

- lists runs per project with status, branch, triggering change, duration, and trend
- primary actions: inspect a run, re-run, cancel, filter, trigger manually

### Run detail

One recorded run, examined.

- the job graph with per-job status, each job's complete log output, artifacts and published reports, timing
- primary actions: follow live output, open a failed step's log, download artifacts, retry a failed job, approve a paused gate

### Commit / pull-request status (integrated view)

The verdict where the change lives — often rendered inside the version-control or code-review surface.

- per-change status with links to the runs that produced it

### Runner / agent management

The operator's view of execution capacity.

- registered agents, their labels and health, queues and pools, what is running where
- primary actions: register or remove agents, group them by capability, manage concurrency

### Administration / settings

Organization-level surfaces.

- permissions and roles, variable/secret management, integrations (version control, chat, storage), notifications, API tokens

## Important Rules / Behaviors

- **Runs are automatic and change-attributed.** A run always belongs to a specific change and is triggered by it without human action; this attribution is what turns a red run into "your commit broke it" rather than "something is broken".
- **The definition is part of the project.** Because run definitions are (in current practice) versioned with the code, a change can alter its own validation rules, and the pipeline a run executes is the one defined at that change — definitions evolve under review like the software they validate.
- **The build itself is delegated.** The platform invokes the project's build tool and test runners; it orchestrates and records, it does not embody the project's build logic. The same project builds identically whether invoked by a developer or by a CI agent.
- **Status is finer than pass/fail in mature products.** Runs can carry intermediate verdicts — compiled successfully but tests failed — surfaced distinctly so authors know whether the *code* or the *tests* misbehaved.
- **Secrets are scoped and shielded.** Credentials are injected into jobs under scoping rules (project, group, organization; sometimes restricted to trusted branches), and products commonly mask secret values in logs. Execution capacity is effectively a credentials bastion, which is why agent fleets are operated carefully.
- **Capacity is finite and shared.** Jobs queue when capacity is busy; products provide concurrency limits, and some add locks that serialize access to a shared resource (for example, allowing only one deployment job at a time) or agent labeling so jobs land on capable machines; in some products, superseded runs — those overtaken by newer commits on the same branch — are skipped or canceled automatically.
- **Artifacts are outputs, not inventory.** Run artifacts are kept as attached evidence of a specific run; long-term custody and serving of software packages belong to registry/repository tooling.
- **Feedback is the contract.** The platform's social function depends on the verdict being trustworthy and fast; teams tune pipelines for reliability and speed (caching, splitting, parallelism) because a flaky or slow verdict erodes the whole loop.

## Variants

- **Standalone automation server (self-hosted)** — an open or commercial server the team operates itself, with agent fleets it provisions; the oldest and still widespread shape.
- **Hosted SaaS platform** — vendor-operated orchestration with vendor-provided ephemeral build machines; the dominant shape for new teams.
- **Hybrid orchestration** — control plane hosted by the vendor, execution on the customer's own machines or cloud, combining SaaS convenience with on-premises code and credential control.
- **Suite-integrated CI/CD** — CI as one module of a single-application DevOps product, sharing one object model with planning, hosting, and delivery; or a CI feature area inside a source-code hosting platform, where runs are just another kind of activity on a repository.
- **Specialist SaaS** — products differentiated on speed, scale, or developer experience of the run loop itself.
- **Era variants** — the 2000s-generation server (plugins for each source-control and build system, web dashboard of past builds) and the modern config-as-code platform realize the same loop with different technology; the legacy UI-configured job model survives alongside config files in some products.

A variant remains a variant unless it changes the core loop: a product whose center of gravity moves to environments and deployment records has crossed into a different Type (see below).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Build Automation System | upstream collaborator | the build tool defines *how one project builds* (project-resident definition, dependency-ordered execution, artifacts) and is invoked *by* CI jobs; CI decides *when and where builds run, for whom, with what history* |
| Continuous Delivery Platform | downstream sibling | CD takes validated artifacts to named environments, executes deployments, and records what is deployed where; CI ends at the validated verdict. A CI pipeline may contain deploy steps, but "which version is in which environment" is not its record |
| Code Quality Platform | consumer/producer seam | CI runs checks as jobs and records job outcomes; the code-quality platform holds long-term quality state — issues, metrics, ratings — and judges code health across changes |
| Test Runner / E2E Testing Platform | delegated tool | test tooling defines and executes the tests; CI provides the triggered execution shell, collects reports, and reflects results in run status |
| Artifact Repository / Package Registry | custody neighbor | registries store and *serve* published packages to consumers; CI merely *produces* run outputs and hands them over |
| Source Code Hosting Platform | event source and host | hosting platforms store the code and reviews that trigger runs, and frequently bundle CI as a feature; the CI machinery (trigger → run → record → feedback) remains a distinct Type either way |
| Job Scheduler / Workflow Orchestrator | structural relative | similar graph execution, but no binding to source changes, no build/test semantics, no commit-attributed verdicts |
| Internal Developer Platform | umbrella consumer | an IDP may expose pipelines as one self-service capability among many; CI is the capability, not the portal |

The two seams that matter most: **Build Automation** (how vs when/where — a CI job typically *contains* a build-tool invocation) and **Continuous Delivery** (verdict vs environment record — vendor "CI/CD platform" branding spans the seam by packaging two Types into one product, not by fusing them).

## Representative Products

- **Jenkins** — self-hosted open-source automation server; the long-dominant self-managed pole, spanning the legacy UI-configured job model and modern pipeline-as-code
- **GitHub Actions** — CI integrated into a source-code hosting platform; the dominant hosted realization
- **GitLab CI/CD** — pipelines bundled inside a single-application DevOps suite
- **Buildkite** — hosted orchestration with self-hosted or vendor-hosted agents; the explicit hybrid pole

The defining structure was additionally checked against older-generation products (a 2001-era open-source CI server and the hosted-CI pioneer generation) to ensure the definition does not over-fit to the modern hosted, YAML-based pattern.

## Sources

Research date: **2026-09-07**

- Jenkins User Documentation — https://www.jenkins.io/doc/ , https://www.jenkins.io/doc/book/pipeline/ , https://www.jenkins.io/doc/book/glossary/
- GitHub Actions — Understanding GitHub Actions — https://docs.github.com/en/actions/about-github-actions/understanding-github-actions
- GitLab Docs — Get started with GitLab CI/CD — https://docs.gitlab.com/ci/
- Buildkite Docs — https://buildkite.com/docs , https://buildkite.com/docs/pipelines/glossary , https://buildkite.com/docs/agent
- CruiseControl — https://cruisecontrol.sourceforge.net/ (historical anchor)
- Travis CI — https://docs.travis-ci.com/ (documentation surface; historical anchor)

> Sourcing limitation: one widely used SaaS specialist (CircleCI) could not be reliably fetched in this pass or the prior sibling pass; category-level statements are drawn from the four sampled products plus historical anchors. Precise numeric limits (concurrency caps, usage quotas, timeouts) are intentionally not stated — none were directly observed.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/era check are recorded in the paired Research Notes.
