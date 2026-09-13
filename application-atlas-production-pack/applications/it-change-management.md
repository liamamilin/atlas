# IT Change Management

## Overview

An **IT Change Management** application is the IT organization's system of record for governing modifications to its own IT environment. Every addition, modification, or removal that could affect IT services — infrastructure, systems, configurations, applications, documentation — is captured as a managed change record, assessed for risk and impact, authorized by a designated change authority before implementation, scheduled, implemented, and then reviewed and closed with its outcome recorded.

Its purpose is to balance progress against risk: the organization wants changes to happen (and often to happen fast), while avoiding change-caused outages, collisions between simultaneous changes, and untraceable modifications. The defining core is deliberately small — the change record, risk-gated pre-implementation authorization, and a governed lifecycle carried to a reviewed outcome. Everything else the market associates with the category — change advisory boards, change calendars, freeze windows, configuration-item linkage, automated risk scoring, pipeline integration — is widespread, mature capability that makes the practice operational, not what makes the product a change-management product. Older, paper-era change control (a change request form, a review board, an authorized schedule of changes, sign-offs and review minutes) satisfies the same structure.

When the governed modification loop disappears — leaving only ticket queues, deployment execution, or generic request approval — the product has drifted into a neighboring type (IT Service Management, Application Deployment Management, Approval Workflow Platform).

## Users & Context

The primary users form an authority structure, because the application's job is deciding who may change what and when:

- **Change requester / implementer** — an engineer, administrator, or support technician who proposes a change: describes what will change and why, identifies affected systems, documents the implementation and rollback approach, and later executes the implementation tasks and records results.
- **Change manager** — the process owner and gatekeeper. Reviews incoming change requests for validity and completeness, drives risk assessment, coordinates the approval path, maintains the change schedule, and closes changes after reviewing their outcome.
- **Approvers / change authority** — the people or boards empowered to authorize changes. In mature products this is tiered: low-risk changes may be approved by a line manager or automatically under a pre-approved policy, while higher-risk changes go to a review board (commonly called a change advisory board, CAB), and the riskiest or largest changes escalate to senior management.
- **CAB members / stakeholders** — representatives from IT operations, development, support, and the business who assess significant changes from technical, business, and financial angles.
- **Secondary users** — service desk staff linking incidents to changes, problem managers using changes as remediation, and administrators configuring change types, workflows, and authority rules.

The work context is an IT department or managed service provider of any meaningful size, typically alongside a service desk, an asset/CMDB record, and operational monitoring. In DevOps-oriented organizations, the requester is often a developer and the "change" may be a deployment flowing through a delivery pipeline, with the change record providing the governance and audit layer around it.

## Core Model

The application's world is organized around one central object and the structures that govern it.

### The Change Request

The **change request** (in many products historically called an RFC, request for change) is the central record: a persistent, individually identified record of one proposed modification to the IT environment. It carries:

- **what** will change — the scope: systems, services, configuration items, or components affected
- **why** — the reason and expected benefit, often referencing the incident, problem, project, or request that motivated it
- **how** — the implementation plan, commonly including a **rollout plan** and a **backout (rollback) plan** describing how to reverse the change if it fails
- **risk and impact** — the assessed likelihood and consequences of the change, recorded through classification fields or structured assessment
- **who and when** — requester, implementers, approvers, and the planned implementation window

The change request is the object that moves through the lifecycle, accumulates the audit trail, and outlives the change itself as the organization's record of what was modified, by whom, under whose authority, and with what result.

### Risk and Impact Assessment

Before a change may proceed, its risk and impact are assessed. Mature products support this at several depths: simple classification fields, structured questionnaires whose weighted answers compute a risk level, business rules that auto-classify, and — in current-generation products — predictive scoring based on historical change data. Assessment is informed by context pulled from associated records: configuration items or assets show which services depend on what is being changed, and linked incidents or problems show why the change is needed. The assessment result drives everything downstream: how deep the process goes, who must authorize, and how carefully the change is scheduled.

### Authorization

Authorization is the control point that distinguishes change management from change tracking: a change record may not move to implementation until a designated change authority approves it. The concept is constant across products; its realizations vary:

```text
Concept:          designated change authority
Implementations:  a named approver or manager
                  a review board (change advisory board) for significant changes
                  a small standing group for urgent situations (emergency board)
                  a pre-approval policy that authorizes predefined low-risk changes automatically
                  peer review in decentralized, DevOps-style organizations
```

Authorization level scales with assessed risk — a tiered authority structure is the common mature pattern, so that trivial changes are not burdened by executive approval and dangerous changes cannot slip through a single opinion.

### The Governed Lifecycle

The change record moves through defined states. Exact labels vary by product, but the conceptual progression is stable:

```text
Requested / Submitted
  → Reviewed & Classified (type assigned, validity checked)
  → Assessed (risk, impact, plans)
  → Authorized (by the appropriate authority)
  → Scheduled (placed on the change calendar)
  → Implemented (tasks executed, results recorded)
  → Reviewed (post-implementation review)
  → Closed (outcome classified: successful / failed / rolled back)
```

Closure is not administrative only: the outcome is classified, the review captures lessons, and the results feed back — a change that repeatedly succeeds may be reclassified into a faster pre-approved path next time; a failure feeds process improvement and, when needed, a rollback or an incident record.

### Scheduling and the Change Calendar

Changes that modify live services need coordination in time. A common scheduling surface in mature products is a **change calendar**: an aggregate view of planned changes over which implementers and stakeholders plan windows, avoid collisions, and respect **maintenance windows** (times when changes are expected) and **change-freeze periods** (times when changes are prohibited, e.g. holidays, audits, peak business). Some products detect conflicts — a change scheduled against another change on the same system, or against a freeze window — before implementation is attempted. The accumulated authorized schedule doubles as the organization's forward-looking statement of what will change and when.

### Context and Associations

The change record is an association hub. Mature products commonly attach:

- **configuration items / assets** — for impact analysis and for keeping the infrastructure record current
- **incidents** — both as trigger (an outage prompting an emergency change) and as consequence (incidents caused by a change)
- **problems** — a change frequently being the chosen remediation for a known root cause
- **service requests and releases** — situating the change among the organization's other work records
- **tasks** — the decomposed implementation work assigned to different technical teams

An audit trail of every action on the record — edits, decisions, approvals, status changes — accumulates automatically and serves both operational learning and formal audit obligations.

## How It Works

### The normal change flow

The most complete path through the application:

```text
Requester raises the change
  → describes what/why, affected systems, implementation and rollback plan
→ Change manager reviews the request
  → valid? complete? classify the change type
→ Risk and impact assessed
  → assessment fields or questionnaire; context from CIs/assets and linked records
→ Authorization
  → routed to the authority the risk level calls for; decisions recorded
→ Scheduled on the change calendar
  → window chosen; conflicts with other changes, maintenance, and freeze periods checked
→ Implementation coordinated
  → tasks assigned and executed; results and evidence recorded on the change
→ Post-implementation review
  → did it achieve the objective? side effects? costs and downtime as planned?
→ Closed with an outcome classification
  → successful / failed / rolled back; lessons feed the next change
```

### The emergency path

When service is actively disrupted, urgency inverts the order: an emergency change is authorized quickly by a small, standing emergency authority, implemented immediately with reduced (but not zero) assessment, and the documentation, testing depth, and review are completed retrospectively. Products provide a distinct fast-track type or workflow for this path precisely because the normal path is too slow — and because emergency changes are both the highest-risk and highest-benefit changes the organization makes.

### The pre-approved path

Low-risk, frequently repeated changes (the "standard" type in most products) follow a defined, pre-approved procedure. They either skip the assessment-and-authorization loop entirely or ride an automated workflow that implements them on request. Making this path the default for routine work is a common maturity goal: it concentrates human review on the changes that need it.

### Core vs common vs optional

- **Defining core** — change request as managed record; risk-gated authorization before implementation; governed lifecycle to a reviewed, closed outcome with retained history.
- **Standard capabilities in mature products** — change type models (standard/normal/emergency at the core, with finer gradations in some), review boards and tiered authority, change calendar with maintenance/freeze windows, task decomposition, rollout/backout plans, configuration-item and incident/problem associations, templates, workflow automation, audit trails, outcome reporting.
- **Optional / advanced** — structured risk-scoring machinery and predictive risk scoring, automated conflict detection, pre-approved change catalogs, pipeline-linked change records for DevOps delivery, SLA timers on changes, deep analytics on change success and change-caused incidents.

## Interfaces

### Change queue / list

The working surface for the change manager and implementers.

- lists change records filterable by state, type, risk, requester, or approver
- surfaces what is pending assessment, pending authorization, scheduled, in implementation, overdue review
- primary actions: open a change, update state, assign, filter, search

### Change form / detail

The record itself.

- structured fields for scope, reason, risk, affected items; sections for implementation, rollout, and backout plans; stage-specific content in template-driven products
- associations panel (CIs/assets, incidents, problems, tasks); activity and approval history
- primary actions: edit, submit for assessment/approval, record a decision, attach evidence, move stage, close with outcome

### Change calendar

The time coordination surface.

- aggregate view of scheduled changes, maintenance windows, and freeze periods; weekly or monthly views
- primary actions: schedule a change into a window, declare freeze/maintenance windows, inspect collisions

### Approval surface

What authorities and board members interact with.

- the changes awaiting their decision, with assessment summaries and recommendations
- primary actions: approve, reject, return for more information; in board-style processes, review agendas of multiple changes

### Requester intake

Where changes enter — a portal or form (in suite products, shared with the service desk's request intake), often template-driven so requesters answer the questions the organization's change policy requires.

### Administration and configuration

Where the practice is encoded: change types and their workflows, stages and statuses, assessment questions, authority and approval rules, templates, calendar windows.

### Dashboards and reports

Management visibility: successful vs failed changes, rolled-back changes, change-caused incidents, emergency-change volume, unauthorized changes detected, schedule adherence, backlog.

## Important Rules / Behaviors

### No unauthorized changes

The foundational policy the application enforces: modifications to the IT environment flow through the change process, and the record of authorization exists before implementation, not after. Detecting changes that bypassed the process is itself a tracked metric in mature products.

### Change type determines depth and authority

The classification assigned at review decides how much process applies: pre-approved types run automated fast paths; moderate types go to the change manager; significant types convene a board; the largest escalate to senior authority. Classification errors are handled cautiously — unknown-risk changes are mapped to the more thorough path until proven otherwise.

### Authorization gates implementation

A change record cannot legitimately reach implementation state without the required decision recorded. Emergency types are the deliberate exception, and they carry a compensating rule: retrospective documentation and review are mandatory, and the emergency path itself is monitored (frequent emergency changes are a process-failure signal).

### Reversibility is planned, not improvised

Mature implementations expect a backout plan before implementation proceeds, and high-risk changes are tested where possible in non-production environments. When a change fails, rollback is executed and the failure classified — the failed change remains a record, contributing to success-rate measurement and process learning.

### The calendar is a governance surface, not decoration

Freeze periods and maintenance windows constrain when changes may run; scheduling against them is blocked or flagged. Conflicts between concurrent changes on shared systems are checked before they become outages.

### The infrastructure record and the change record interlock

Impact analysis draws on the configuration/asset record; after implementation, the outcome feeds back so the infrastructure record reflects reality. Change management needs a view of the environment; the environment's record needs changes to be recorded. Neither side of the interlock is the other type: the record of what exists is configuration management data, the governed loop that modifies it is this type.

### Everything is attributable

Every decision, edit, and state transition on a change is attributed and timestamped. This is what makes the closed change record usable in audits, post-incident analysis, and organizational learning.

## Variants

- **ITIL-classical control-first organizations** — tiered change authority, formal review boards meeting on cadence, published change schedules, formal post-implementation review; the practice is explicitly control-oriented and audit-driven.
- **High-velocity / DevOps organizations** — authority decentralized toward teams and peers; change records link to delivery pipelines and deployment evidence; automated checks replace meetings where possible; review boards are reserved for the riskiest changes or reframed as advisory.
- **Suite-module vs dedicated packaging** — the most common packaging is as a module of an IT service management suite alongside incident, problem, request, and asset management; the practice also exists as a distinguishable module inside broader platforms.
- **Scale and tier** — small organizations run lightweight flows (a single approver, a simple calendar); large enterprises configure multiple type models, scoped calendars, regionally scoped freeze windows, and separation-of-duties rules.
- **Deployment model** — SaaS and on-premises products both exist; on-premises heritage is strong in this category.
- **Risk machinery depth** — from a manual risk field to weighted questionnaires to predictive scoring learned from historical change outcomes.
- **Change-model granularity** — the standard/normal/emergency triad is the common core; some organizations add intermediate levels (minor/major) as their scale demands.

## Related Application Types

| Application Type | Distinction |
|---|---|
| IT Service Management / ITSM | the surrounding suite (service desk, incident, request, asset practices); change management is one governed practice inside it, not the whole |
| CMDB | the authoritative record of what exists (configuration items and their relationships); change management governs modifications to that environment and consumes the CMDB for impact — a record, not a governance loop |
| Approval Workflow Platform | generic request → route → decide machinery for any domain; change management binds authorization to an IT change record with risk scaling, scheduling, implementation tracking, and outcome review |
| Application Deployment Management | executes software changes onto endpoint populations; change management authorizes and records changes regardless of who or what executes them |
| Configuration Management (infrastructure tooling) | declares and enforces desired state on infrastructure — it performs changes; change management governs them at process level |
| Release Management Platform | coordinates groups of changes/deployments into releases; change management governs each modification individually |
| Incident Management | the restore-service loop for unplanned disruptions; incident-triggered emergency changes are the bridge, but records, loops, and goals differ |
| IT Problem Management | the root-cause elimination loop; a change is often the remediation a problem record produces, not the problem record itself |
| Patch Management | executes a recurring class of software updates at scale; in governance terms these commonly ride the pre-approved change path |
| Engineering Change Management | the same governance grammar applied to product/BOM engineering data; the record base and context (IT environment, service impact) are what define this type |

## Representative Products

- ManageEngine ServiceDesk Plus (change management module)
- Jira Service Management
- SolarWinds Service Desk

These were the products whose official documentation grounded this description; they span the ITIL-classical and DevOps-oriented philosophy poles and different customer tiers.

## Sources

Research date: **2026-09-08**

- ManageEngine — ServiceDesk Plus change management (feature page) — https://www.manageengine.com/products/service-desk/change-management.html
- ManageEngine — ServiceDesk Plus: how to set up change risk assessment — https://www.manageengine.com/products/service-desk/it-change-management/change-risk-assessment.html
- ManageEngine — ServiceDesk Plus: ITIL change management process guide — https://www.manageengine.com/products/service-desk/it-change-management/
- Atlassian — What is IT change management (ITSM practices) — https://www.atlassian.com/itsm/change-management
- SolarWinds — Service Desk product page (change management section) — https://www.solarwinds.com/service-desk

> Sourcing limitation: official documentation for several major ITSM suites (including the enterprise market leader and a mid-market SaaS suite) could not be retrieved from the research environment on 2026-09-08 (timeouts, JavaScript-only doc portals, or missing pages). Enterprise-specific mechanics are therefore not asserted anywhere in this document; cross-product claims rest on the three captured products, and claims that rest on a single product's documentation (notably the change-calendar and conflict-detection detail) are stated with calibrated caution. Detailed observations and the comparison matrix are in the paired Research Notes.
