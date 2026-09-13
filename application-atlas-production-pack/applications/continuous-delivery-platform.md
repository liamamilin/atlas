# Continuous Delivery Platform

## Overview

A **Continuous Delivery Platform** is the software team's system of record for releasing software to runtime environments. It takes a **versioned deliverable** — a build artifact such as a package or container image, or a versioned declaration of desired state — and carries it to **named target environments** (development, test, staging, production, customer instances, edge sites) through a **managed, repeatable deployment process**, recording every execution as a **deployment** bound to a version, an environment, a time, and an outcome.

The problem it solves is the gap between "a validated build exists" and "the software is running where users reach it". Build systems and CI platforms produce and validate deliverables; the delivery platform owns everything after that point: where software is deployed, how it gets there, who may deploy it, what is currently running in each environment, and what happened in every past deployment.

The defining core is deliberately small:

```text
Versioned deliverable
  → Managed, repeatable deployment process
    → Named target environment(s)
      → Recorded deployment (version × environment × outcome)
        → Per-environment delivery history: "what is deployed where"
```

Everything else commonly associated with the category — promotion lifecycles, approval gates, blue/green and canary rollouts, rollback, environment-scoped secrets, dashboards — is standard capability that mature products add, not what makes the product a delivery platform. A product that only builds and tests code is a CI platform; a product that executes deployments but keeps no record of them is a script runner; a product that distributes software to employee devices is endpoint deployment management. The delivery record — the durable answer to "what is deployed where" — is what makes this a system of record rather than an automation convenience.

## Users & Context

Primary users:

- **Developers** — trigger deployments of their own services, watch them execute, and roll back when a change misbehaves; in many teams they self-serve deployments to non-production environments.
- **DevOps / platform engineers** — define and maintain the deployment processes, environments, variables, and integrations that make self-service safe.
- **Release / deployment engineers** — manage promotion between environments, coordinate releases across services, and handle freezes and exceptions.

Secondary users:

- **Engineering managers and SREs** — observe deployment status and history, respond to failed or risky deployments, and perform rollbacks during incidents.
- **Security and compliance roles** — configure who may deploy to production, review audit trails, and enforce separation between environments (for example, keeping production credentials out of test deployments).

The work context is a software team operating one or more long-lived runtime environments. Deployments happen continuously or on a release cadence; the platform is opened to check status, to push a change out, to approve someone else's deployment, or to answer "what version is in production right now?" — often during an incident.

## Core Model

### The defining spine

Four structures carry the whole Type:

**Versioned deliverable.** The unit of delivery is always a *version*, never a loose change. In most products this is a build output — a package, archive, or container image produced by a CI system and identified by version. In declarative (GitOps-style) products it is a versioned declaration — a commit or revision of configuration that describes the desired state. Either way, the platform tracks deliverables as identifiable, immutable versions.

**Target environment.** An environment is a named, managed record of a place where software runs: a stage in the promotion path (development, test, staging, production), a cluster or account, or a customer-specific instance. Environments are first-class objects: they have identity, configuration, access rules, and a current state. Many products also support short-lived dynamic environments created per change (preview or review environments) and torn down afterwards.

**Managed deployment process.** The repeatable procedure that carries a deliverable into an environment: the steps to run, in what order, against which targets, with which configuration. The process is defined once and reused across deployments, so that successive versions of the software are delivered the same way. Processes are typically edited visually or as code, and mature products snapshot the process with each release so that later process edits do not silently change how an in-flight version deploys.

**Deployment record.** Every execution creates a record: which version went to which environment, when, by whom or by what trigger, through which process, and with what outcome. Records accumulate into per-environment history, and the most recent successful record defines the environment's current version. This history is the platform's system-of-record property — the queryable answer to "what is deployed where, and how did it get there".

```text
CI / build system
  └─ produces versioned deliverable (package / image / commit)
       ↓ registered with the platform
Release / deliverable version
       ↓ carried by
Deployment process (steps, strategy, configuration)
       ↓ executed against
Target environment (named, configured, protected)
       ↓ produces
Deployment record → environment history → "current version"
```

### Standard capabilities around the spine

Mature products commonly add:

- **Promotion rules** — constraints on how a version moves between environments (which environments must receive it first, which promotions are automatic, which require a person).
- **Manual gates and approvals** — points where the deployment pauses until an authorized person approves it.
- **Rollback** — re-executing a previous version into an environment; in the common model this is itself a new recorded deployment, not an undo.
- **Environment-scoped configuration** — variables and secrets resolved per environment, so a test deployment cannot read production credentials.
- **Deployment strategies** — rolling, blue/green, and canary patterns that control how a new version replaces the old one and how traffic shifts.
- **Upstream integration** — triggers from CI completions, artifact registries, and repository events; artifact handoff from the build side.
- **Execution visibility** — step-level logs, live status, and notifications while a deployment runs.
- **Access control and audit** — role-based permissions (especially over production), SSO, and audit trails over deployments and configuration changes.
- **API and CLI access** — programmatic parity with the user interface, so deployments can be automated from other systems.

### One spine, two delivery models

The same core structure is realized by two contrasting models, and both belong to this Type:

- **Push orchestration** — the platform actively executes the deployment process: it runs steps, calls targets, and moves the version forward. The deployment happens when the process runs.
- **Declarative reconciliation (GitOps)** — the desired state for each environment is declared in version control; a controller continuously compares the live state against the declaration, reports differences, and converges the environment to the declared state, automatically or on command. The "deployment" is the act of convergence, and the record is the sync history.

The push model asks "what should we deploy next?"; the reconciliation model asks "does reality match the declaration?". Both keep a versioned deliverable, named environments, a defined process, and a recorded history — which is why they are one Type.

## How It Works

### The core deployment loop

```text
1. A build completes (or a commit lands in the desired-state repository)
2. The deliverable is registered with the platform
      (a release is created, an artifact is picked up, or a revision is tracked)
3. A deployment is triggered
      - automatically (CI completion, registry event, schedule, declared-state change)
      - or manually (a person selects a version and an environment)
4. The managed process executes
      - steps run against the environment's targets
      - environment-scoped variables and secrets are resolved
      - the deployment strategy shapes the rollout
5. Gates apply
      - automated checks (health, policy)
      - manual approvals where configured
6. The outcome is recorded
      - success / failure bound to version × environment × time × actor
      - the environment's current version updates on success
7. The change is observed
      - health and alerts on the environment
      - rollback to a previous version if the new one misbehaves
8. The version is promoted
      - the same deliverable advances to the next environment under the promotion rules
```

Steps 2–6 repeat for every environment the version passes through. The process definition stays stable while versions change; the record accumulates.

### Promotion between environments

A version typically enters at a development or test environment and advances toward production. Promotion rules define the path: some transitions fire automatically when the previous one succeeds; others wait for a person; some require the version to have reached a minimum set of environments first. Each promotion is a new deployment with its own record, so the history shows the version's full journey.

### Rollback

When a deployment causes problems, the operator selects a previous successful version and redeploys it. The important behavior: rollback is not an undo of the failed deployment — it is a **new deployment of an older version**, executed through the same process and recorded like any other. The failed deployment remains in the history as a fact. Some products can trigger this rollback automatically when monitoring detects a critical problem with the new version.

### The reconciliation loop (declarative variant)

In GitOps-style products the loop is continuous rather than event-driven:

```text
Desired state declared in version control
  → controller compares live state vs desired state
  → differences surfaced (drift, or a new declared version)
  → converge: automatic sync, or a person approves the sync
  → sync recorded; environment health evaluated
  → repeat
```

Any out-of-band change to the environment shows up as drift against the declaration and is either reverted by the next sync or flagged. Rollback means reverting the declaration to a previous commit and re-converging.

### Failure behavior

A failed deployment stops with its steps' errors visible in the execution record. The environment's previous version remains the last known-good reference — which is what makes rollback a routine operation rather than an emergency. Whether a partially completed deployment leaves mixed versions running depends on the deployment strategy and the product; strategies like blue/green exist precisely to keep the old version serving until the new one is verified.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Dashboard / environments overview

The primary entry surface, answering "what is deployed where".

- Typical information: projects or applications × environments, current version in each, last deployment time and outcome, environment health.
- Primary actions: open an environment, start a deployment, inspect recent deployments.

### Pipeline / process editor

Where the deployment process is defined.

- Typical information: steps and their order, target scope, strategy, variables, conditions and gates.
- Primary actions: add/edit/reorder steps, configure variables and secrets, define triggers, save (often as version-controlled configuration).

### Deployment execution view

The live surface while a deployment runs.

- Typical information: step-by-step progress, per-target status, streaming logs, elapsed time, current gate.
- Primary actions: approve or reject at a gate, retry a failed step, abort the deployment.

### Environment detail

The record surface for one environment.

- Typical information: current version, deployment history (version, time, actor, outcome), configuration and variables, linked targets, URL of the running application.
- Primary actions: deploy a chosen version, roll back to a previous one, stop or retire the environment, edit its configuration.

### Release / version picker

The surface for choosing what to deploy.

- Typical information: available versions of the deliverable, their build origin, what has already been deployed where, included changes (commits or tickets).
- Primary actions: select a version, choose target environment(s), trigger the deployment.

### Approval queue

Where pending gates wait for authorized people.

- Typical information: deployment awaiting approval, requester, target environment, changes included.
- Primary actions: approve, reject with reason, view execution detail.

### Administration

- Typical information: users and roles, environment protection rules, integrations (CI, registries, monitoring, ticketing), audit log.
- Primary actions: grant/revoke deployment rights, protect environments, connect external systems.

## Important Rules / Behaviors

- **The deployment record is append-only fact.** Failed and rolled-back deployments stay in the history; rollback adds a new record rather than erasing the failed one. The history is used for auditing and for answering incident questions.
- **One current version per environment is the common default, not a law.** Many products model an environment as holding one active version, with the previous successful deployment as the rollback reference; progressive strategies deliberately run more than one version at once during the transition.
- **Production is permission-gated.** Mature products let organizations restrict who (or what pipeline) may deploy to sensitive environments, independently of who can edit code. Deployment rights to production are commonly separated from general write access.
- **Environment scope bounds secret visibility.** Variables and secrets are resolved per environment; a deployment to test does not receive production credentials. This scoping is a stated security boundary, not a convenience.
- **Promotion can be enforced, not just suggested.** Products commonly prevent a version from skipping required environments, and can prevent outdated deployments from overwriting newer ones.
- **Deployments can be frozen.** Organizations can block deployments to an environment during a change freeze or incident, with the platform refusing or queuing affected deployments.
- **The process is versioned with the release.** Because processes change over time, mature products bind the process definition (or its snapshot) to the release being deployed, so a deployment's behavior is reproducible after the process has since been edited.
- **Rollback re-executes, it does not reverse.** Rolling back runs the deployment process again for an older version; anything the process does not itself restore (for example, a separate database migration) is the operator's responsibility.
- **Every action is attributable.** Deployments, approvals, and configuration changes carry the acting user or triggering system, feeding the audit trail.

## Variants

- **Push orchestration vs declarative reconciliation.** The dominant split. Push products execute deployments on demand; GitOps products reconcile environments toward declared state continuously. Hybrid stacks are common (a push pipeline publishes a new image, a reconciliation layer rolls it out).
- **Substrate focus.** Kubernetes-native products model deployments as convergence of cluster resources; VM/traditional products model machines and services as deployment targets; multi-cloud products abstract several providers behind one resource model; edge variants push to large fleets of small sites or customer instances.
- **Suite-integrated vs dedicated.** Some products are dedicated delivery platforms that assume an external CI system; others are CI/CD suites where delivery is the deploy stage of the same pipeline model. The Type is the same; the packaging differs.
- **Tenanted and fleet deployments.** The same release deployed to many customer-specific instances or sites, with per-tenant configuration — common in SaaS and distributed-retail scenarios.
- **Ephemeral environments.** Dynamic per-change environments (preview/review apps) created for a branch and destroyed after review.
- **Progressive delivery depth.** From simple rolling updates to automated canary analysis that promotes or aborts based on measured behavior.
- **Operations runbooks.** Some products extend the same process machinery to day-2 operations (restarts, failover, maintenance) executed against environments under the same access control.
- **Hosting posture.** Self-managed (on the customer's infrastructure) vs vendor-hosted SaaS; open-source core vs commercial product.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Continuous Integration Platform | upstream sibling | CI builds and tests code on every change and produces validated artifacts; it does not own environments or deployment records. Delivery platforms consume CI output. Suite products bundle both, but the seam holds: end at a validated artifact → CI; carry it to environments and record it → CD |
| Build Automation System | upstream | defines how one project is built (project-resident build definition, dependency-ordered execution); invoked by developers or CI; no environment or deployment concept |
| Artifact Repository | upstream custodian | stores and serves built artifacts under stable coordinates; the delivery platform consumes artifacts from it rather than replacing it |
| Release Management Platform | governance neighbor | plans and governs releases (calendars, approval policy, coordination across teams); the delivery platform executes deployments. "Release orchestration" vocabulary straddles both — joint boundary check recommended |
| Feature Flag Management Platform | complementary | decouples feature release from code deployment; flags may be toggled after (or instead of) a deployment. Some delivery products bundle flag features, but the flag lifecycle is its own Type |
| Application Deployment Management (IT) | false friend | distributes software packages to managed employee devices under IT policy; targets a device fleet, not server/cloud runtime environments, and serves IT operations rather than software delivery |
| IT Change Management / ITSM | governance neighbor | approves and tracks *whether* a change may proceed; the delivery platform performs the change and records it. Integration between the two is common |
| Infrastructure-as-Code Platform | adjacent | provisions and maintains infrastructure from declarations; delivery pipelines commonly include IaC steps, but provisioning infrastructure is not delivering application versions |
| Kubernetes / Container Management | substrate neighbor | operates clusters and container platforms; a GitOps delivery product may live inside Kubernetes while remaining a delivery system of record |
| Internal Developer Platform | abstraction layer | a portal over many capabilities (services, environments, deployments); delivery is one capability it may expose |

The sharpest boundary is with the **Continuous Integration Platform**: the two are marketed together as "CI/CD" so constantly that the seam is easy to lose. The working test: a product whose center of gravity is commit-triggered build/test feedback, ending at a validated artifact, is CI; a product that owns environments, executes deployments, and keeps the record of what is deployed where is CD — even when one product ships both.

## Representative Products

- **Octopus Deploy** — dedicated continuous-delivery platform (release orchestration, deployment automation, runbooks); self-managed or vendor-hosted.
- **Argo CD** — declarative GitOps continuous delivery for Kubernetes; reconciliation-based delivery model.
- **GitLab (CI/CD)** — suite-integrated CI/CD where delivery is modeled as environments and deployments inside the pipeline product.
- **Spinnaker** — open-source multi-cloud continuous delivery platform built around pipelines and cloud resource management.

Together these cover the dedicated-specialist, GitOps, suite-integrated, and multi-cloud open-source poles of the category.

## Sources

Research date: **2026-09-07**

- Octopus Deploy — Documentation overview and Getting started (concepts: projects, environments, releases, deployment process, variables, lifecycles, runbooks, tenants) — https://octopus.com/docs , https://octopus.com/docs/getting-started
- Argo CD — Overview and Core concepts — https://argo-cd.readthedocs.io/en/stable/ , https://argo-cd.readthedocs.io/en/stable/core_concepts/
- GitLab — Environments and Deployments documentation — https://docs.gitlab.com/ci/environments/ , https://docs.gitlab.com/ci/environments/deployments/
- Spinnaker — Concepts (application management, application deployment, managed delivery) and Pipelines — https://spinnaker.io/docs/concepts/ , https://spinnaker.io/docs/concepts/pipelines/

> Sourcing limitation: two additional candidate products (a SaaS CI/CD specialist and a commercial verification-led delivery platform) could not be reached during research (documentation endpoints unavailable). The sample therefore spans four products; category-wide claims in this document are worded accordingly ("mature products commonly…"), and no numeric limits, default values, or timing figures are asserted.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
