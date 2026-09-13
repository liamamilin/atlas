# Research Notes — Continuous Delivery Platform

Research date: 2026-09-07
Leaf: Continuous Delivery Platform (DIRECTORY.md §12 Software Development & Product Engineering)
Slug: continuous-delivery-platform

---

## Research Goal

Understand what a Continuous Delivery (CD) Platform actually is as an Application Type — its core object model, its defining workflow, its users, its interfaces, its rules — from real products' official operational documentation, and separate the defining structure from what is merely common in the current market.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: a CD platform takes versioned build outputs and delivers them to target environments through managed, repeatable deployment processes, recording what is deployed where.
- Nearest neighbors: Continuous Integration Platform (unprocessed sibling), Build Automation System (processed), Artifact Repository (processed), Release Management Platform (unprocessed), Feature Flag Management Platform (unprocessed), Application Deployment Management (§14, processed — endpoint/device side), IaC Platform, Kubernetes/Container Management, Internal Developer Platform, Software Delivery Governance Platform.
- Main confusion risks: (1) "CI/CD" products blur CI and CD; (2) "release management" vocabulary is used both for governance/planning and for deployment execution; (3) GitOps reframes deployment as reconciliation, which may or may not fit a push-centric definition.

## Research Questions

1. What is the unit of delivery? (artifact? image? commit? release bundle? desired-state declaration?)
2. What is an "environment" in each product, and how is it modeled?
3. What is the deployment process object, and how is it defined (UI-built steps vs YAML vs declarative manifests)?
4. What is recorded per deployment, and what does the platform know about "what is deployed where"?
5. How do promotion, approvals, gates, freezes, and rollback work?
6. How do CD platforms relate to CI systems and artifact repositories (integration seam)?
7. How does the GitOps pull model differ from the push model, and does it still fit one Type?
8. Who uses the product, and what surfaces do they operate?
9. Where is the boundary vs CI, release management, feature flags, ITSM change management, and endpoint deployment management?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy | Segment | Evidence |
|---|---|---|---|
| Octopus Deploy | Dedicated CD specialist ("CI is not CD"; release & deploy focus) | Commercial, self-managed + SaaS (Octopus Cloud), SMB→Fortune 100 | Tier-1 docs (docs root + getting-started), full fetch |
| Argo CD | Declarative GitOps CD for Kubernetes (pull/reconcile model) | Open source (CNCF), K8s-native teams | Tier-1 docs (overview + core concepts), full fetch |
| GitLab (CI/CD) | Suite-integrated CI/CD — CD as environments/deployments inside one application | Commercial SaaS + self-managed, all tiers | Tier-1 docs (environments + deployments), full fetch |
| Spinnaker | Open-source multi-cloud CD platform (pipeline + cloud-resource model) | Open source, large enterprises, Netflix heritage | Tier-1 docs (concepts + pipelines), full fetch |

Rejected/abandoned samples:
- Harness — docs paths 404 twice (developer.harness.io); abandoned per network rules; no claims made.
- CircleCI — docs paths 404 twice (circleci.com/docs/deploy-overview/, /docs/deployments/); abandoned; no claims made.

## Sources

All fetched 2026-09-07:

- Octopus Deploy — https://octopus.com/docs (product overview) and https://octopus.com/docs/getting-started (concepts: projects, environments, releases, deployment process, variables, infrastructure, lifecycles, runbooks, tenants, spaces)
- Argo CD — https://argo-cd.readthedocs.io/en/stable/ (overview: what/why/how it works, features) and https://argo-cd.readthedocs.io/en/stable/core_concepts/ (Application, target/live state, sync, refresh, health)
- GitLab — https://docs.gitlab.com/ci/environments/ (environments: static/dynamic, tiers, states, variables scoping, protected environments, auto rollback) and https://docs.gitlab.com/ci/environments/deployments/ (deployment records, history, rollback semantics, manual deployments)
- Spinnaker — https://spinnaker.io/docs/concepts/ (application management + application deployment + managed delivery) and https://spinnaker.io/docs/concepts/pipelines/ (pipeline/stage/task, templates, execution history)

Evidence layers used below: A = directly observed on the cited official page of that product; B = cross-product commonality across the sample; C = canonical inference from comparison + boundary reasoning.

---

## Product A — Octopus Deploy

### Key observations (Layer A unless noted)

Positioning (docs root):
- Self-describes as "a sophisticated, best-of-breed continuous delivery (CD) platform"; offers "release orchestration, deployment automation, and runbook automation".
- Explicit scope claim: "Octopus takes over where your CI server ends, modelling the entire release orchestration process of software." Lists: release versioning, environment promotion, deployment automation, progressive software delivery (rolling, blue/green, canary), configuration management, approvals & ITSM integration, deployment freezes, coordinating deployments across projects and dependencies.
- Explicit principle: "CI is not CD"; "Build your binaries/containers once"; consistency across processes/teams/environments; pragmatic GitOps.
- Targets: Kubernetes, Linux/Windows VMs, AWS/Azure/GCP — via Tentacle agent, SSH, CLI, or web service.
- Governance: RBAC ("only the right people can deploy to production"), all changes audited; self-managed or Octopus Cloud.
- Tenanted deployments: coordinated rollouts across geographically distributed clusters / thousands of end-customers / edge locations (retail stores, hospitals, hotels).

Concepts (getting-started):
- **Projects** = the applications deployed; a project holds "all the information needed to deploy an application".
- **Environments** = where applications are deployed (Dev, Test, Production); deployment targets (machines and services) are organized into environments.
- **Releases** = "a bundle of all the things needed to deploy a specific version of an application": container images/packages (CI-produced artifacts), configuration and variables per environment, a snapshot of the deployment process (so later process changes don't affect in-flight releases), and details of Jira tickets and Git commits that went into the release. Releases are usually created automatically at the end of a CI process.
- **Deployment** = a release deployed to an environment. Docs note teams use "release" and "deployment" interchangeably but they are distinct.
- **Deployment Process** = "the recipe for deploying the project — the steps that will be run"; steps contain actions; built-in step templates + custom steps; process stays stable across deployments while software changes; can be stored in Git (Config as Code).
- **Variables** = environment-scoped configuration ("your test environment shouldn't have access to your production database").
- **Lifecycles** = promotion rules: phases, each with one or more environments, automatic vs manual deployment environments, required number of environments before the next phase unlocks.
- **Runbooks** = day-2 operations automation inside a project (infrastructure provisioning, database management, failover); grant developers safe operations ability without production access.
- **Tenants** = customer-specific deployment pipelines without duplicating project configuration (SaaS instances, edge fleets); deploy a release to all/some/tagged tenants.
- **Spaces** = team isolation of projects/environments/infrastructure in large organizations.
- Packaging: CI output = packages/containers; packages can be pushed to Octopus's built-in package repository or an external one (e.g. Artifactory).
- Dashboard: first page; shows projects × environments × releases grid (what's deployed where).
- Approvals: "Approvals with manual interventions" is part of the first-deployment tutorial; Approvals is a top-level docs section; deployment freezes listed as a capability.

## Product B — Argo CD

### Key observations (Layer A)

Positioning (overview):
- "A declarative, GitOps continuous delivery tool for Kubernetes."
- Principle: "Application definitions, configurations, and environments should be declarative and version controlled. Application deployment and lifecycle management should be automated, auditable, and easy to understand."
- GitOps pattern: Git repositories as the source of truth for the **desired application state**; manifests via Kustomize/Helm/Jsonnet/plain YAML/config-management plugins.
- "Argo CD automates the deployment of the desired application states in the specified target environments." Deployments can track branches, tags, or pinned commits (tracking strategies).
- Implemented as a Kubernetes controller continuously comparing **live state** vs **target state**; deviation = `OutOfSync`; reports/visualizes differences; syncs automatically or manually back to desired state.
- Feature list: automated deployment to target environments; multiple config tools; multi-cluster; SSO; multi-tenancy + RBAC; rollback/"roll anywhere" to any committed configuration; health status analysis; drift detection/visualization; automated or manual sync; web UI with real-time activity; CLI; webhooks; access tokens; PreSync/Sync/PostSync hooks (e.g. blue/green & canary rollouts); audit trails for app events and API calls; Prometheus metrics; parameter overrides.

Core concepts (core_concepts page):
- **Application** — a group of Kubernetes resources as defined by a manifest (a CRD).
- **Target state** — desired state as files in Git. **Live state** — what is actually deployed.
- **Sync status** — whether live matches target. **Sync** — the process of moving the application to target state. **Sync operation status** — whether a sync succeeded.
- **Refresh** — compare latest Git with live state; figure out differences.
- **Health** — is the application running correctly / can it serve requests?
- **Tool / config management plugin** — builds manifests from a directory of files.

## Product C — GitLab (CI/CD)

### Key observations (Layer A)

Environments (docs/ci/environments/):
- "A GitLab environment represents a specific deployment target for your application, like development, staging, or production."
- With environments you: keep deployment process consistent/repeatable; **track what code is deployed where**; roll back to previous versions; protect sensitive environments from unauthorized changes; control deployment variables per environment ("maintain security boundaries"); monitor environment health with alerts.
- Environments are **static** (reused, fixed names like staging/production) or **dynamic** (created per pipeline, e.g. review apps per merge request, then stopped/deleted).
- Environment states: `available` / `stopping` / `stopped` (driven by stop jobs).
- **Deployment tiers**: development / testing / staging / production / other; guessed from name patterns (regex table shown in docs) or set explicitly via `deployment_tier`.
- Environments created in UI or via `.gitlab-ci.yml` `environment:` keyword on a deploy job; environment URL surfaced in MRs and views.
- **Environment-scoped CI/CD variables**: limit sensitive variables to specific environments (default scope `*`); supply-chain mitigation rationale stated in docs.
- **Protected environments**: "Allowed to deploy" lists; deployment-only access patterns; stopping/deleting protected environments restricted.
- Stopping: on_stop jobs, auto-stop after time period (`auto_stop_in`), stale-environment cleanup, branch-deletion auto-stop.
- **Auto Rollback** (Ultimate): automatically triggers a rollback when a critical alert is detected; redeploys the most recent successful deployment; skipped if a deployment is running; rate-limited (once per three minutes — precise figure kept in notes only); off by default.
- Environment permissions by role (Reporter/Developer/Maintainer/Owner).

Deployments (docs/ci/environments/deployments/):
- "When you deploy a version of your code to an environment, you create a deployment. There is usually only one active deployment per environment."
- "Provides a full history of deployments to each environment. Tracks your deployments, so you always know what is deployed on your servers."
- Manual deployments via `when: manual` (Run button: "Can be manually deployed to <environment>").
- Per-deployment MR tracking: commit-diffs between latest and previous deployment → which merge requests are newly included.
- Deployment Git-refs (`refs/environments/*`) let you check out deployed state locally; old refs archived (up to 50,000 kept — precise figure in notes only); deployed commits preserved via keep-around refs.
- **Rollback**: rolling back creates a **new deployment** with its own job ID pointing at the target commit; only deployment jobs run; artifacts from earlier jobs may need manual regeneration (Terraform plan/apply example).
- Retry or roll back from the environment's deployment list ("Re-deploy to environment" / "Rollback environment").
- Related pages exist for: deployment approvals, deployment safety (incl. "prevent outdated deployment jobs"), incremental rollouts, review apps, external deployment tools (track deployments made by external tools), releases, feature flags.

## Product D — Spinnaker

### Key observations (Layer A)

Concepts (docs/concepts/):
- "An open-source, multi-cloud continuous delivery platform that helps you release software changes with high velocity and confidence."
- Two core feature sets: **Application management** (view/manage cloud resources) and **Application deployment** (construct/manage CD workflows), plus **Managed delivery** on top.
- Application management model: **Application** (represents the service + its configuration + the infrastructure it runs on) → **Cluster** (logical grouping of server groups; explicitly NOT a K8s cluster) → **Server Group** (the base resource: identifies the deployable artifact — VM image, Docker image, source location — plus instance count, autoscaling, metadata; when deployed, a collection of running instances) + **Load Balancer** + **Firewall**.
- Application deployment model: **Pipeline** ("the key deployment management construct"; sequence of stages; parameters passed stage to stage; started manually or triggered by events — Jenkins job completing, new Docker image in registry, CRON schedule, stage in another pipeline; notifications on start/complete/fail) → **Stage** (collection of sequential tasks and composed stages; e.g. Deploy, Resize, Disable, **Manual Judgment**) → **Task** (automatic function).
- **Deployment strategies as first-class constructs**: Spinnaker handles orchestration (verify health checks, disable old server groups, enable new); blue/green supported; rolling blue/green and canary in active development (docs wording).
- **Managed Delivery**: declare **desired state** of the application in terms of logical **environments** (test, prod) where infrastructure resources exist and where **software artifacts** (Debian package, Docker image) are deployed; Spinnaker detects new artifact versions, satisfies deployment **constraints**, detects divergence from desired state, and reconciles. User guide adds: delivery configs, environment constraints, pinning an environment, marking an artifact as bad, resource status.

Pipelines (docs/concepts/pipelines/):
- Pipelines = "managing deployments in a consistent, repeatable and safe way"; stages range from infrastructure manipulation (deploy, resize, disable) to scaffolding (manual judgment, wait, run Jenkins job) — "precisely define your runbook for managing your deployments".
- Parallel stage paths; concurrency control (whether multiple instances of a pipeline can run at once).
- Execution history = introspection of each deployment operation + "an effective audit log of enforced processes/policies".
- Blue/Green deploy stage expands into a sequence of steps → tasks → cloud API calls with polling and failure remediation.
- **Pipeline templates**: parameterized templates + configurations (inherit/override triggers, notifications, parameters) for scalable cross-team standardization.
- Artifacts reference (nav): Docker image, Debian package, Maven artifact, Git repo, S3/GCS objects, etc.; triggers from Artifactory/GitHub/GCS/pub-sub/webhooks; CI integrations (Jenkins, Travis, CodeBuild, Cloud Build).
- Canary analysis support (setup + user guide sections); automated rollbacks (Kubernetes provider guide); RBAC (Fiat), SSO/OAuth/SAML/LDAP.

---

## Cross-product Comparison

| Dimension | Octopus Deploy | Argo CD | GitLab CI/CD | Spinnaker |
|---|---|---|---|---|
| Unit of delivery | Release (bundle: packages + variables + process snapshot + build info) | Git revision of desired-state manifests (branch/tag/pinned commit) | Deployment of a code version (commit) to an environment | Artifact (Docker image, Debian, Maven…) carried by pipeline; or declared artifact in Managed Delivery |
| Environment concept | Environments grouping deployment targets; lifecycles define promotion | Target environment = cluster/namespace where desired state applies | Environment = named deployment target (static/dynamic) with tiers | Logical environments (Managed Delivery); cloud accounts/regions/clusters in classic model |
| Process object | Deployment Process (steps, snapshot per release; config-as-code) | Sync policy + hooks + sync waves (declarative) | Pipeline deploy jobs with `environment:` keyword | Pipeline of stages (visual; templates) |
| Deployment record | Deployment (release × environment); dashboard grid | Sync history; sync status; OutOfSync diff | Deployment record + full history + per-deployment MRs | Pipeline execution history as audit log; server-group state |
| "What's deployed where" | Dashboard (projects × environments × releases) | Live state vs target state per Application | Environments list + deployments list | Clusters view; application infrastructure view |
| Promotion | Lifecycles (phases, auto/manual, required environments) | Tracking strategies; ApplicationSet progressive syncs | Manual deploy jobs; rules; (approvals page) | Manual Judgment stage; environment constraints (Managed Delivery) |
| Rollback | Re-deploy previous release (docs sections) | Rollback to any committed config | Rollback creates a NEW deployment of previous commit | Automated rollbacks (K8s provider); re-deploy |
| Strategies | Rolling, blue/green, canary (progressive delivery) | Hooks for blue/green & canary rollouts | Incremental rollouts (separate page) | Blue/green first-class; rolling; canary analysis |
| Config per environment | Environment-scoped variables | Parameter overrides; per-app values | Environment-scoped CI/CD variables | Pipeline variables; per-environment config (Managed Delivery) |
| Governance | RBAC, audit, approvals & ITSM, freezes | RBAC, SSO, audit trails, sync windows | Protected environments, deployment approvals, deployment safety | RBAC (Fiat), SSO, execution history as audit |
| CI relationship | Explicit: integrates with CI; CI produces packages; Octopus "takes over where CI ends" | CI automation page: CI triggers/updates; Argo syncs | CI and CD in one product (deploy stage of pipeline) | Triggers from Jenkins/Travis/CodeBuild/CloudBuild; artifact triggers |
| Delivery model | Push (orchestrated execution) | Pull (controller reconciles desired state) | Push (pipeline jobs) | Push; Managed Delivery adds declarative reconcile |
| Substrate | K8s, VMs, clouds, edge (agent/SSH/CLI/API) | Kubernetes only | Any target reachable by runner scripts + deployment services | Multi-cloud (AWS/GCP/Azure/K8s/CF/AppEngine/Cloud Run/Oracle) |
| Ops extras | Runbooks (day-2), tenants, spaces | Drift detection, health, orphaned resources | Review apps, auto rollback on alerts, incident alerts on env page | Managed delivery (pin, mark-as-bad), canary analysis |

### Layer B findings (cross-product commonality)

1. All four model **named target environments** as first-class records (B).
2. All four keep a **recorded history of deployments/syncs** binding version × environment × outcome (B).
3. All four expose **"what is currently deployed where"** as a primary surface (dashboard/environments/clusters/applications) (B).
4. All four define a **repeatable deployment process** distinct from any single execution (B).
5. All four integrate **upstream** with CI systems and/or artifact sources; none claims to replace CI (B; Octopus states it explicitly, GitLab is the counter-pole that bundles CI).
6. All four provide **rollback/re-deploy to a previous version** (B).
7. All four provide **environment-scoped configuration/variables** with security rationale (B).
8. All four provide **RBAC + audit**; production deploys are permission-gated (B).
9. All four support **manual gates** somewhere in the flow (manual interventions, manual sync, when:manual, Manual Judgment) (B).
10. All four support **progressive/strategy-based rollouts** in some form (B).

### Layer C canonical inference

The Type is best understood as the **system of record for releasing software to runtime environments**: versioned deliverable → managed deployment process → named environment → recorded deployment state, with promotion, gating, rollback, and audit built around that spine. The GitOps pull model is the same spine with the trigger inverted (reconcile-to-declared-state instead of execute-declared-process), so it stays inside the Type.

---

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant (minimal)

A Continuous Delivery Platform is recognizable by exactly this structure:

```text
Versioned deliverable (build artifact or versioned desired-state declaration)
  → Managed, repeatable deployment process
    → Named target environment(s)
      → Recorded deployment (version × environment × time × outcome)
        → Per-environment delivery history ("what is deployed where")
```

Four properties; remove any one and the product stops being this Type:

1. **Versioned deliverable** — the unit of delivery is a version of build output (package/image) or a versioned declaration (commit/revision). Without it, the product is a generic workflow/runner.
2. **Named target environments** — managed records of the places software runs (dev/test/staging/prod, clusters, tenants). Without it, the product is CI (build/test feedback only).
3. **Managed deployment process** — a defined, repeatable, automated procedure that carries a version to an environment. Without it, the product is ad-hoc scripts or a manual ops checklist.
4. **Recorded deployments / delivery history** — each execution is recorded and accumulates into per-environment state and history. Without it, the product is a script runner, not a delivery system of record.

Deliberately NOT in L0 (tested against the sample and against older practice): promotion lifecycles, approvals, rollback, deployment strategies, environment-scoped variables, CI integration, RBAC, dashboards, GitOps, Kubernetes, multi-cloud, tenanted fleets. A single-environment, single-artifact CD with a plain process and a deployment log still satisfies L0.

### L1 — Common Mature Structure (very common, not definitional)

- Pipeline/process visualization and stage orchestration (parallel paths, concurrency control)
- Manual approvals / gates (manual interventions, deployment approvals, Manual Judgment)
- Promotion rules between environments (phases/lifecycles; required environments)
- Rollback / re-deploy to a previous version (rollback recorded as a new deployment)
- Environment-scoped configuration variables and secrets
- Deployment strategies: rolling, blue/green, canary (progressive delivery)
- CI integration (trigger on build completion; artifact handoff) and artifact-repository integration
- Execution logs / step-level task detail / streaming output
- Notifications (email/Slack/SMS/webhooks)
- RBAC, SSO, audit trails
- API/CLI parity with the UI
- Health/status of deployments and environments
- Config-as-code storage of process definitions (Git-backed)

### L2 — Variant / Optional Structure

- Delivery model: push orchestration vs GitOps pull/reconcile (drift detection, sync policies, sync windows)
- Substrate: Kubernetes-native vs VM/traditional vs multi-cloud vs PaaS vs edge fleets
- Tenanted / customer-instance deployments (SaaS multi-tenant, store/restaurant edge fleets)
- Runbooks / day-2 operations automation
- Ephemeral preview environments (review apps / dynamic environments)
- Automated verification & auto-rollback on alerts; canary analysis
- Deployment freezes / sync windows / outdated-deployment prevention
- Release traceability (commits, tickets/MRs included per deployment; build info)
- Feature-flag integration (adjacent capability, separate Type)
- Platform packaging: dedicated CD product vs CI/CD suite module vs open-source platform; self-hosted vs SaaS
- Platform-level multi-tenancy (spaces/projects isolation)

### L3 — Vendor-specific (research notes only)

- Octopus: Lifecycles/phases, Tenants, Spaces, Runbooks, Tentacle agent, built-in package repository, "CI is not CD" positioning, release = process snapshot bundle.
- Argo CD: Application CRD, AppProject, target/live state vocabulary, OutOfSync status, refresh vs sync, sync waves/hooks, ApplicationSet, tracking strategies, config-management plugins.
- GitLab: `environment:` keyword in `.gitlab-ci.yml`, deployment tiers guessed by name regex, review/$CI_COMMIT_REF_SLUG dynamic environments, auto_stop_in, dotenv URL capture, protected environments "allowed to deploy", deployment Git-refs (refs/environments/*) with keep-around commits, auto-rollback rate limit (once per 3 minutes, off by default), 50,000 deployment-ref archive threshold.
- Spinnaker: Application/Cluster/Server Group/Load Balancer/Firewall resource model, Orca/Clouddriver/Front50 microservice architecture, Bakery (VM image baking), Manual Judgment stage, pipeline templates, Managed Delivery (delivery configs, environment constraints, pinning, mark-artifact-as-bad), Fiat RBAC, canary config objects.

## Rejected Findings (considered, not promoted)

- "CD platforms deploy to Kubernetes" — rejected as definitional; only Argo CD is K8s-only; Octopus/Spinnaker/GitLab span VMs and multiple substrates.
- "CD platforms include CI" — rejected; Octopus explicitly positions against it; Spinnaker/Argo CD integrate with external CI. GitLab bundles CI but that is suite packaging, not the Type's definition.
- "CD platforms manage infrastructure/cloud resources" — rejected as definitional; Spinnaker's server-group model is product-specific; GitLab/Octopus treat targets as endpoints. IaC steps appear inside pipelines but infrastructure provisioning is a neighboring Type.
- "Deployment = one active version per environment" — GitLab states "usually only one active deployment per environment"; canary/blue-green keep multiple versions serving simultaneously, so this is a common default, not an invariant. Written as common behavior, not a rule.
- "Rollback is an undo" — rejected; GitLab explicitly creates a NEW deployment on rollback; Argo CD rolls forward to a committed config. Rollback is forward execution of an older version.
- "Tenanted deployments" — Octopus-specific emphasis (L3); Spinnaker Managed Delivery environments and Argo ApplicationSets are related but differently shaped; kept as L2 variant.
- "Release orchestration across projects/dependencies" — Octopus claims it; not evidenced across the sample at the same depth; kept as L2/optional.

## Boundary Findings

- **vs Continuous Integration Platform** (§12 sibling, unprocessed): sharpest seam. CI = commit-triggered build/test orchestration producing validated artifacts and fast feedback; CD = carrying versioned deliverables to named environments and recording what is deployed where. Octopus's own docs draw the line ("CI is not CD"; "takes over where your CI server ends"; CI's job is "to take source code and turn it into an artifact"). GitLab bundles both — suite packaging, not Type fusion. Test: does the product's center of gravity end at producing a validated artifact (CI) or extend to environment delivery + deployment records (CD)? Joint review recommended when continuous-integration-platform is processed (build-automation-system pass already recorded a related flag).
- **vs Build Automation System** (processed): build tool = how one project builds (project-resident definition, artifact production); CD = delivery of built outputs to environments. Consistent with that pass's recorded seam.
- **vs Artifact Repository** (processed): custody/serve of artifacts vs delivery of artifacts to environments. CD platforms consume repositories (Octopus built-in repo is an convenience, not the Type).
- **vs Release Management Platform** (§12 sibling, unprocessed): release governance/planning (calendars, approvals policy, release notes, coordination across teams) vs deployment execution machinery. Overlap zone: "release orchestration" vocabulary (Octopus). Test: does the product execute deployments against environments (CD) or coordinate/plan/govern releases as management objects (Release Management)? Flag for joint review.
- **vs Feature Flag Management Platform** (§12 sibling, unprocessed): flags decouple feature release from code deployment; CD platforms integrate flags (Octopus/GitLab ship flag features) but the flag lifecycle is its own Type. Test: object of record = deployment vs flag.
- **vs Application Deployment Management** (§14, processed): that Type distributes software packages to managed endpoint devices (UEM-flavored); this Type delivers server/cloud software to runtime environments. Different target population and different record model.
- **vs IT Change Management / ITSM**: change tickets/approvals govern *whether* a change may proceed; CD executes the change and records it. Octopus lists "approvals & ITSM integration" — integration seam, not fusion.
- **vs IaC Platform** (§14): provisioning infrastructure vs delivering application deliverables; CD pipelines commonly include IaC steps (GitLab rollback caveat mentions Terraform jobs) — composition, not identity.
- **vs Kubernetes/Container Management** (§14): cluster operations vs application delivery to clusters; Argo CD is CD-shaped even though it lives inside K8s.
- **vs Internal Developer Platform / IDP** (§12, unprocessed): portal/abstraction layer; CD is one capability an IDP may expose. Not settled here.
- **"去掉什么就变成另一个 Type" 判据**: remove environments + deployment records → CI platform; remove versioned deliverable (deploy arbitrary change tasks) → IT change/automation tooling; remove the managed process (manual execution) → ops runbook practice, not a CD platform; remove runtime environments (deploy to employee devices) → Application Deployment Management.

## Historical / Market-Sample Check (§24)

- Would older products fit L0? Pre-"CD"-branding deployment automation (2000s-era release/deploy tools organized around application → environment → deployment process → deployment record) satisfies the L0 spine; the L0 is essentially the digitization of classical release-engineering practice (versioned build → documented procedure → named environment → recorded result). No modern-market-only concept (GitOps, K8s, canary analysis, SaaS) is required by L0. Check passed.
- Regional/platform-native check: the sample spans US-commercial (Octopus), CNCF open source (Argo CD, Spinnaker), and suite-integrated (GitLab) origins; no region-specific structure entered L0.
- The one era-sensitive risk — "environment = cloud/cluster" — was abstracted to "named target environment record", which covers VM fleets and edge devices equally.

## Uncertainties

- CircleCI and Harness could not be fetched (404s); the SaaS CI/CD-specialist pole and the commercial verification-led CD pole are under-sampled. Claims about "all CD platforms" are limited to the four-product sample; wording in the final document uses "mature products commonly…" rather than universal claims.
- Spinnaker's "Managed Delivery" is documented at overview level only; its current adoption depth is unclear; treated as L2 variant (declarative/reconcile posture inside a push-centric platform).
- Argo CD's relationship to the broader Argo family (Workflows, Rollouts, Kargo) was not researched; progressive-delivery depth in the GitOps pole may be understated.
- Release Management Platform boundary is provisional because that leaf is unprocessed; joint review flag recorded.
- No numeric limits, default values, or timing figures from any product were promoted to the final document (e.g., GitLab's 3-minute auto-rollback rate limit and 50,000-ref archive threshold stay here in notes).

## Final Synthesis

A Continuous Delivery Platform is the software-delivery system of record between "validated build output exists" and "software is running in an environment". Its defining spine: a **versioned deliverable** is carried by a **managed, repeatable deployment process** to **named target environments**, and every execution is **recorded**, accumulating into per-environment delivery history — the answer to "what is deployed where, since when, by whom, and did it work". Around that spine, mature products add promotion rules, gates and approvals, rollback, environment-scoped configuration, progressive rollout strategies, CI/artifact-repository integration, RBAC/audit, and observability hooks. Two delivery models realize the same spine: push orchestration (pipeline executes the deployment) and GitOps reconciliation (controller converges live state to a declared desired state). The Type ends where CI ends (build/test feedback), where release governance begins (planning/approval policy), where feature release begins (flags), and where endpoint software distribution begins (device fleets).
