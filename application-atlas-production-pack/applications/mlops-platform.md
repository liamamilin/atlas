# MLOps Platform

## Overview

An **MLOps Platform** is the shared record-and-loop system an organization uses to operate its machine learning models like governed software: every model-building and processing run is captured as a recorded, comparable unit; the resulting models are held as versioned records that are promoted through lifecycle states; and chosen versions are moved into production serving — with the record trail making the whole path reproducible and auditable, and automation keeping new versions flowing as data and code change.

The defining core is small:

```text
Tracked run record            (what ran: params, metrics, artifacts, code/data/environment)
        │  produces
Versioned model record        (registered versions, traceable, promoted through states)
        │  operationalized through
Deployment / serving binding  (endpoints, deployment targets, or trigger-handoff)
        │  watched & re-run
New data / new code → new run  (the loop continues)
```

The name comes from treating model delivery as an operations discipline ("MLOps" — machine learning operations), and the market uses the label in two ways: it names this machinery as standalone products, and it names the machinery sections inside broader machine-learning suites. This document covers the machinery itself. What it does not require is training compute of its own: the machinery runs whether training happens on the organization's own machines, on a vendor's managed cloud, or anywhere else — that is the line separating this Type from the Machine Learning Platform, which is defined by running model-building on compute it manages.

Remove the run records and only deployment automation over invisible work remains; remove the versioned model records and only a metrics tracker remains; remove the operationalization bridge and only an experimentation archive whose models never ship remains. All three structures, held together, are what makes the product this Type.

## Users & Context

The platform serves the same data team that builds models, with each role touching a different part of the loop:

- **Data scientists** are the heaviest daily users: their training scripts, notebooks, and pipelines write runs into the record system, and they live in the comparison surfaces — comparing this week's runs against last month's, checking which data and parameters produced the winning model.
- **ML engineers** productionize what data scientists prove: they register models, manage versions and promotion states, wire deployments, and build the automated pipelines that retrain and redeploy.
- **Platform / MLOps engineers** own the machinery itself: connecting the platform to the organization's compute (queues, agents, deployment targets), configuring triggers and automation, managing environments and secrets.
- **Reviewers and approvers** (in governed teams) inspect registered versions — their metrics, lineage, and evaluation records — and promote or reject them through approval gates.
- **Application developers** are mostly indirect consumers: they receive prediction endpoints or models handed off through the deployment machinery, and rarely touch the record system.
- **Administrators** manage the tenancy containers — projects, teams, access control — and read audit trails.

The work context is a team's model estate: a shared record of what has been tried, which models exist, which versions serve production, and how each production model traces back to the code and data that produced it. Regulated teams use the same machinery with heavier emphasis on reproducibility and audit; the platform's own record system is the evidence they rely on.

## Core Model

### The defining core

Three structures, held together. Each is load-bearing; remove any one and the product stops being recognizable.

**The tracked run record.** Work on models — training, fine-tuning, data processing, evaluation — is captured as a run: a recorded unit holding its parameters, metrics, outputs, and artifacts, together with references to the code, the data, and the environment that produced it. Some products capture this automatically ("reproducibility by default" — the execution records its own code version, image, inputs, and configuration whether or not the user remembers); others rely on instrumentation through an SDK or framework hooks. Either way, the run record is the platform's memory: without it there is no comparison, no reproducibility, no audit — just scripts that ran once and left no trace. Runs are organized under shared containers (projects, experiments, workspaces) so the whole team sees one record base rather than scattered private notes.

**The versioned model record with promotion.** The output of a run — the model — is held as an identified, versioned record, traceable to the run and data that produced it. Versions are promoted through defined lifecycle states (commonly named staging, production, archived, or expressed as approval states) rather than overwritten: a model "goes to production" as a state change on its record, not as a file copy. This record is the object to which everything operational attaches — deployments, approvals, downstream monitoring — and it is what makes rollback a matter of pointing back at the prior version.

**The operationalization bridge.** Registered versions move into production serving through the platform's machinery. The realization varies widely — built-in real-time endpoints and batch inference, deployment jobs sent to compute targets the organization owns, or registry-triggered handoff (webhooks into the organization's own CI/CD and serving environment) — but the bridge itself is constant: the deployed instance stays bound to the model record, so updating production means promoting/deploying a different registered version. This is the "Ops" in MLOps: the machinery that turns experiment outputs into operated services.

```text
Code + data + environment
        │  executed (on any compute)
        ▼
RUN RECORD ──── params · metrics · artifacts · lineage
        │  model registered
        ▼
MODEL RECORD ── versions · stages/approvals · lineage to run & data
        │  promoted & operationalized
        ▼
PRODUCTION SERVING ── bound to a version (rollback = prior version)
        │
        ▼
monitor / collect / retrain → new run …
```

### Standard capabilities mature products add

Expected in current products but not what makes the product this Type:

- **Comparison surfaces** — dashboards over runs: metric curves, run diffing, parallel-coordinate charts, reports; the everyday reading surface of the record system.
- **Lineage** — links connecting a model version to its producing run, its training data, and its environment, browsable in both directions.
- **Automation machinery** — triggers (schedules, webhooks, new-data events, model-version events), job queues and agents, and CI/CD integration that re-runs the loop without manual re-execution.
- **Approval workflows** — review and sign-off gates before a version can be promoted to production.
- **Tenancy and access control** — projects/teams/workspaces scoping records and actions, with role-based permissions and enterprise SSO.
- **Hyperparameter sweeps** — automated search over training configurations, with results landing in the same record system.
- **SDK / CLI / API parity** — everything visible in the UI operable from code; offline logging modes for restricted environments.
- **Audit logs and usage observability** — who changed what, and resource/usage accounting.
- **Environment capture** — container images and dependency references so a run can be rebuilt elsewhere.
- **Production monitoring** — drift and quality watching on deployed models, present in some products as a module and bundled in suites; absent from the record-machinery pole's core.
- **GenAI extensions** — tracing, evaluation, and prompt layers for LLM applications, a rapidly common modern overlay on the same record spine.

### One structure, many implementations

The core is written conceptually; products realize each part differently:

```text
Concept:   Tracked run record
Realized as: SDK-instrumented experiment logging, automatic execution
            capture (code commit + image digest + inputs + command),
            notebook-run recording

Concept:   Versioned model record with promotion
Realized as: registries with named stages, versioned artifacts with
            aliases, approval-state workflows, deployment-bound versions

Concept:   Operationalization bridge
Realized as: built-in real-time endpoints and batch inference,
            deployment jobs to customer compute targets, registry
            webhooks handing off to the organization's CI/CD
```

A reader who has only seen one shape — say, a hosted dashboard fed by SDK logging — should still recognize the platform that instead orchestrates executions on the team's own servers: same three structures, different substrate.

## How It Works

### Record a run

```text
Author training/processing logic (script, notebook, or pipeline step)
→ attach instrumentation (SDK calls, framework hooks, or automatic capture)
→ execute on whatever compute the team uses
→ the platform records the run: parameters, metrics, outputs,
  code reference, data reference, environment reference
```

The run record exists whether the work ran on a laptop, a company cluster, or a managed cloud — the platform's contract is with the record, not the compute. This is why the same platform can sit above a data science team's heterogeneous infrastructure.

### Compare and select

```text
Open the project's run history
→ filter and group runs
→ compare metrics and outputs side by side
→ inspect a candidate run's parameters, data, and environment
→ identify the version worth promoting
```

Comparison is the everyday loop of model development; the record system makes it possible months later, not just today.

### Register and promote

```text
Register the chosen output as a model version
→ the version carries lineage back to its run and data
→ evaluation/approval gate (in governed teams: explicit review)
→ promote through lifecycle states (e.g. staging → production)
→ the state change is recorded on the model record
```

Promotion is a state change on a versioned record, never an overwrite. Exact state names vary by product; the pattern — register, evaluate, approve, promote — is consistent across the researched sample.

### Operationalize

```text
Deploy a registered version to a serving surface:
  - the platform's own real-time endpoint / batch inference, or
  - a deployment job sent to the organization's compute target, or
  - a registry-triggered handoff (webhook) into the org's CI/CD
→ applications consume the served model
→ the deployment stays bound to the model version
```

Updating production means deploying a different registered version; rollback is the same operation in reverse. The deployment never drifts from the record, because it is the record that the deployment machinery acts on.

### Automate the loop

```text
Configure triggers: schedule, new-data event, webhook, code change
→ trigger fires a pipeline: train → evaluate → register → promote → deploy
→ each stage records its run and artifacts
→ new model versions flow to production without manual re-execution
```

Automation is what turns the record-and-promote machinery into an operations loop. Mature products express it as pipelines whose every stage is itself a recorded run, so automated work is as auditable as manual work.

### Reproduce and audit

```text
Find any historical run in the record
→ read its captured code, data, environment, and parameters
→ re-execute it ("create execution from this") and get the same result
→ or read forward: which production model came from which run and data
```

The record spine exists precisely so that a production question ("which dataset trained this model?") or a reproduction ("rebuild last quarter's model") is a lookup, not an investigation.

### Capability tiers

**Defining core** — without these, not this Type:

- tracked run records as the shared, comparable memory of model work
- versioned model records with promotion through lifecycle states
- the operationalization bridge binding deployments to model versions

**Standard structure** — present in most mature products:

- comparison/visualization surfaces; lineage; automation (triggers, queues, CI/CD); approval workflows; tenancy and access control; sweeps; SDK/CLI/API parity; audit and environment capture

**Variant / optional** — depends on packaging and segment:

- built-in serving vs deployment targets vs trigger-handoff (substrate choice)
- execution orchestration on customer infrastructure vs no execution at all
- production monitoring modules; GenAI/LLM-ops extensions; self-hosted/VPC/on-prem/hybrid deployment; cross-platform migration tooling

## Interfaces

### Run / experiment dashboard

The primary reading surface.

- typical information: run lists grouped by project/experiment, metric charts, run status, owners, timestamps
- primary actions: compare runs, filter/group, open a run detail, launch a new run

### Run detail

- typical information: the run's parameters, metrics, logged artifacts, code and data references, environment, logs
- primary actions: inspect lineage, download/reproduce the run, tag, comment, resume (for interrupted work)

### Model registry view

- typical information: registered models, their versions, lifecycle states, approvals, lineage to runs
- primary actions: register a version, request/perform approval, promote or roll back a stage, deploy a version

### Deployment / serving view

- typical information: live deployments, their bound model versions, endpoint health and traffic where the platform operates serving
- primary actions: create/update a deployment, split or shift traffic (where supported), test, tear down

### Automation / pipeline configuration

- typical information: pipelines, triggers (schedules, webhooks, events), queues and agents, run history of automated work
- primary actions: define or edit a pipeline, configure triggers, manage queues/targets, re-trigger

### Administration

- typical information: projects/teams/orgs, members and roles, audit logs, usage
- primary actions: manage members and permissions, configure integrations, review audit trail

### SDK / CLI / API

Programmatic parity with the surfaces above: start and log runs from training code, register and promote models, configure deployments and triggers, query records — the dominant way data scientists interact with the record system, since instrumentation lives in their code.

## Important Rules / Behaviors

- **Work must flow through the record.** A model built outside the platform's instrumentation does not exist to it: no comparison, no lineage, no promotable version. The instrumentation step is therefore structural, not optional polish.
- **Versions are promoted, not overwritten.** A model version is an identified record; lifecycle changes are state changes on it. Production updates and rollbacks are version re-pointings, which is what makes iteration safe.
- **Deployments bind to versions.** Whatever the serving substrate, the running instance is traceable to a registered model version and, through lineage, to the run and data that produced it.
- **Promotion can be gated.** Governed products make approval an explicit step between evaluation and production; the gate's existence is common, its strictness varies by team configuration.
- **Automation acts on recorded events.** Triggers fire on schedules, webhooks, and record events (a new model version registered, a dataset version updated) — the record system is also the automation bus.
- **Reproducibility depends on what the record captured.** Products differ in whether capture is automatic or instrumentation-dependent; either way, only captured references can be replayed. Strongest guarantees come from infrastructure-level capture (code commit, image, inputs, parameters frozen per execution).
- **Tenancy scopes everything.** Records, models, deployments, and automation live inside project/team containers; who can promote, deploy, or trigger is a permissioned decision, and enterprise deployments put access control and audit around all of it.
- **The platform is compute-agnostic.** Nothing in the core requires the vendor to own training compute; runs may execute on the user's laptop, the company's cluster, a managed cloud, or a compute queue the platform orchestrates on the customer's own machines.
- **Exact limits, state names, and defaults vary.** Stage vocabularies, retention, and numeric limits are product-specific; this document states none as universal.

## Variants

Common shapes the Type takes in the market:

- **Record-first SaaS machinery** — tracking, registry, comparison, and automation delivered as hosted products; runs execute on the customer's own infrastructure via SDK instrumentation; automation extends to deployment jobs on customer compute targets. The most common entry point for teams.
- **Open-source embeddable machinery** — the record system as vendor-neutral open source, self-hosted or embedded in other tools; the de-facto standard layer many other products integrate with.
- **Execution-orchestration platforms** — the platform drives the execution itself: it provisions or queues work on the organization's cloud accounts, on-premises workers, or schedulers, wrapping every execution in automatic reproducibility capture; strongest in hybrid and regulated deployments.
- **Full-stack self-managed platforms** — open-source cores plus commercial layers spanning tracking, orchestration, serving, and (optionally) a compute control plane; the machinery/execution gradient inside a single product.
- **Suite-embedded module groups** — the same machinery packaged inside broader machine-learning platforms, sold under the "MLOps" banner as the CI/CD, registry, and automation section of the suite.
- **GenAI-ops extensions** — the same record spine pointed at LLM applications (traces, evaluations, prompts), increasingly bundled into products of every pole.

A variant remains a variant while the defining core — run records, versioned model records with promotion, and the operationalization bridge — still applies.

## Related Application Types

| Type | Distinction |
|---|---|
| Machine Learning Platform | the execution-center sibling: it runs model-building on compute it manages, holding models and deploying them. The MLOps platform's center is the record-and-operationalization machinery, which runs with or without owned compute. Suites straddle both; the machinery-only pole (no managed training) exists only on this side. |
| Model Registry | the record machinery alone — versions, stages, approvals as its own object-of-record system. Inside an MLOps platform the registry is one component of the loop; the platform adds the run-record spine and the operationalization bridge. |
| ML Model Monitoring Platform | the deployed-model watch loop: ongoing evaluation of production behavior against baselines. Appears here as a bundled module; the dedicated Type owns no records, promotion, or deployment machinery. |
| Data Science Workbench | the interactive code session where analysis and prototyping happen. Workbench sessions feed runs into the MLOps record system; the session itself holds no lifecycle. |
| AI Model Hosting Platform | centers on operating serving infrastructure for consumption (often of models built elsewhere). The MLOps platform's bridge may hand models off to such infrastructure rather than operate serving itself. |
| Feature Store | the feature-data layer (definitions, time-versioned values, training/serving retrieval) consumed by the model lifecycle; dataset-version artifacts here are record/automation objects, not feature stores. |
| DataOps Platform | the same discipline applied to data pipelines (versioned pipelines, develop→promote loop) rather than models; the two interlock but center different objects. |
| Continuous Integration / Continuous Delivery platforms | manage software code artifacts (build/test/release of the codebase). MLOps platforms integrate with them (webhooks, triggers) but center model records, not code builds. |
| AI Governance Platform | holds business/risk/legal context and review state for AI systems; the MLOps registry holds technical artifact records. Governance consumes MLOps records; the centers do not overlap. |

The boundary with the Machine Learning Platform is the most important one, because the market's labels overlap heavily: suites sell their machinery sections as "MLOps," and machinery products are marketed as platforms. The structural difference is the center of gravity — executing model-building on managed compute versus the record-promotion-operationalization loop — and the population proves the seam: products with no managed training compute at all are unambiguously this Type and unambiguously not that one.

## Representative Products

- **MLflow** — open-source, vendor-neutral record machinery: tracking, model registry with stage promotion, deployment targets; the archetype of the machinery-without-owned-compute pole.
- **Weights & Biases** — record-first SaaS platform (experiment tracking, artifacts, registry, sweeps) whose Launch machinery drives jobs on the customer's own compute infrastructure.
- **Comet** — SaaS platform spanning experiment management, model registry with approvals and CI/CD webhooks, and production monitoring; VPC/on-prem enterprise posture.
- **Valohai** — execution-orchestration platform with reproducibility-by-default capture, YAML-defined pipelines, serving, and trigger automation over hybrid/on-prem/cloud infrastructure.
- **ClearML** — open-source-plus-commercial full stack: agents/queues execution, experiment tracking, pipelines, serving, and an optional compute control plane.

The defining core was checked against the machinery-only pole (no managed training compute) and against the suite pole (the machinery packaged inside broader platforms), so that no single packaging philosophy is baked into the definition.

## Sources

Research date: **2026-09-08**

- MLflow — *MLflow Documentation* (home and ML section: tracking, model registry, deployment, evaluation) — https://mlflow.org/docs/latest/ 
- Weights & Biases — *Documentation* (product overview; W&B Launch: jobs, queues, agents) — https://docs.wandb.ai/
- Comet — *Comet Docs* (experiment management, artifacts, model registry, production monitoring, self-hosted) — https://www.comet.com/docs/v2/
- Valohai — *Documentation* (executions, pipelines, models, automation triggers, serving) and *Reproducibility by Default* — https://docs.valohai.com/
- ClearML — *ClearML Documentation* (platform overview: control plane, development center, GenAI engine) — https://clear.ml/docs/latest/docs/

> Sourcing limitations: ClearML evidence is held at overview-layer depth; MLflow's open-source automation machinery was not observed in the fetched documentation; production-monitoring claims are made only where directly observed. Two vendor sites previously unreachable from the research environment were not sampled and no claims are made about them. Product-specific numeric limits, state-name taxonomies, and defaults are intentionally not stated in this document.

Detailed product-by-product observations, the cross-product comparison, and boundary removal tests are recorded in the paired Research Notes.
