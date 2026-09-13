# IT Problem Management

## Overview

An **IT Problem Management** application is the IT organization's system of record for the *causes behind incidents*. A recurring disruption is not treated as a series of separate failures: it is traced to an underlying cause, that cause is held as a persistent, identified **problem** record, investigated to a recorded root cause, mitigated in the meantime with a documented workaround, and eliminated through a permanent fix — after which the record is closed with its related incidents resolved.

The defining structure is small:

```text
Problem record
  (persistent, identified record of a suspected or confirmed cause —
   or potential cause — of one or more incidents)
  ↓
Root-cause investigation loop
  (link the incidents as evidence → consult configuration and operational
   context → determine and record the cause)
  ↓
Cause-directed disposition to closure
  (workaround documented as the known error to reduce ongoing impact →
   permanent resolution pursued, commonly through change management →
   closed, tying back to the incidents the problem explains)
```

Everything commonly associated with modern problem management — proactive detection from trends, AI-based problem prediction, productized RCA frameworks, dedicated known-error databases — is widespread in current products but is an implementation or extension of this core, not the core itself. Paper-era and early-ITIL practice (a problem register, linked incident references, investigation notes, a workaround circulated to the service desk, a fix request to change control) satisfies the same structure.

The word "problem" is doing precise work here. An incident is the disruption itself, worked under time pressure to restore service; a problem is the cause behind one or more such disruptions, worked deliberately toward elimination. When the center of gravity moves to restoring service from a live disruption, the product is Incident Management; when it moves to governing authorized modifications to the IT environment, it is IT Change Management.

## Users & Context

The primary users are the people accountable for making recurring failures stop:

- **Problem manager** — the process owner. Receives or identifies candidate problems, prioritizes them against business impact, coordinates each investigation to its conclusion, maintains the problem queue and stakeholder communication, and keeps the workaround/known-error knowledge current for the service desk.
- **Technical specialists and subject-matter experts** — perform the actual diagnosis: analyze logs and telemetry, inspect configuration, run RCA sessions, and record what they find on the problem record.
- **Service desk agents** — consumers of the practice's output: they link new incidents to existing problems and apply documented workarounds so callers get relief before the permanent fix lands.

Secondary participants:

- **IT operations engineers** — supply monitoring data, capacity and utilization context, and often execute the operational parts of a fix.
- **Change managers** — the receiving side: the permanent fix for a problem typically enters the environment as a change they govern.
- **Service owners and administrators** — configure problem categories, priorities, workflows, and notifications.

The working context is an IT department or managed service provider of meaningful size, operating alongside a service desk, a configuration record (CMDB), and change management — usually inside the same ITSM suite. The time profile is the opposite of incident response: incidents are worked in minutes under urgency, while problem work is deliberate, scheduled investigation over days or weeks, fighting for attention against the "in-your-face urgency" of the next outage.

## Core Model

### The Defining Core

**The problem record.** A problem is a persistent, individually identified record of a suspected or confirmed underlying cause — or a potential cause — of one or more incidents. It is an object distinct from the incident records it explains: incidents are symptoms and evidence, the problem is the diagnosis under construction. The record carries what the practice needs to work the cause: a category and description of the disruption pattern, the linked incidents, the affected configuration items, a status, a priority, and an accumulating trail of the investigation.

**The root-cause investigation loop.** A problem is not just logged; it is *worked as a diagnosis*. Related incidents are attached as evidence — the repetition pattern is the data. Configuration and operational context is consulted: which components are involved, what changed recently, what the logs and monitoring show. Specialists investigate and the determined cause is recorded on the problem record itself, including honest outcomes such as a cause that could not be reproduced. Without this loop there is only a list of complaints; the cause-finding is what makes it problem management.

**The cause-directed disposition to closure.** The record exists to drive action against the cause and to end as a recorded disposition:

- While the cause is real and the permanent fix is pending, a **workaround** is documented and attached to the problem — the problem in its **known error** state: a documented root cause plus a documented workaround. The service desk uses it to relieve ongoing impact without pretending the cause is gone.
- The **permanent resolution** is pursued and recorded on the problem — and it is commonly routed through change management, so the modification that eliminates the cause is planned, authorized, and recorded like any other change to the environment.
- **Closure** is meaningful, not administrative: a closed problem is one whose cause has been addressed and which can no longer generate those incidents. The related incidents are closed with it, and the resolution knowledge (cause, fix, workaround) is preserved — often published into the knowledge base for future use.

These three structures are jointly held. A cause record with no investigation is a rumor; investigation with no record is a conversation; a record and investigation with no disposition is analysis that never lands. And the record must stay bound to the incidents it explains — a "problem" detached from any incident population loses its evidence and its closure test.

### What Mature Products Add

A typical modern product carries most of the following. They make the practice operational; they are not what makes the product problem management.

- **Incident linkage** — multiple incident tickets attached to one parent problem, so repetition becomes visible and evidence accumulates in one place.
- **Known-error surfacing** — workarounds pushed to the service desk (in-product status, knowledge articles, or a dedicated known-error collection — implementations vary) and often to self-service portals.
- **Configuration anchoring** — affected configuration items from the CMDB, with dependency context to reason about where the cause lives.
- **Priority from impact × urgency** — how many users and components are affected, and how fast the resolution is needed.
- **Change and release association** — the problem record points at the change or release that will fix it, and later at the one that did.
- **Queue, templates, and notifications** — assignment and routing of problem records, structured templates for symptoms and impact, and stakeholder notifications during investigation.
- **Closure review and metrics** — post-resolution review, recurrence tracking, problem-volume and resolution-time reporting.

### One Structure, Many Implementations

The core is written conceptually; products realize each concept differently.

```text
Concept:      Known-error layer
Realized as:  a status on the problem record,
              knowledge-base articles generated from the problem,
              a dedicated known-error database collection

Concept:      Problem identification
Realized as:  grouping recurring incidents (manual or clustered),
              major-incident escalation into a problem,
              trend and monitoring analysis before incidents occur

Concept:      Cause determination
Realized as:  specialist investigation recorded on the record,
              RCA methods productized as guided workflows (e.g. five whys),
              AI-suggested causes from incident clusters

Concept:      Permanent resolution
Realized as:  a change record governed by change management (dominant form),
              a release deployment,
              a direct fix inside the responsible team (DevOps-style)

Concept:      Diagnosis context
Realized as:  CMDB configuration items and dependencies,
              logs, monitoring and telemetry,
              the linked incident history itself
```

A reader who has only seen one packaging — say, an AI-forward SaaS suite that clusters incidents automatically — should still recognize a service desk whose problem is a prioritized ticket investigated by a specialist team with a spreadsheet of incident references: same defining core, different implementation.

## How It Works

### Identify a problem

```text
Reactive path:
  recurring incidents observed
    → pattern recognized (by the desk, the problem manager,
       or automatic clustering)
    → incidents linked to a new problem record
    → symptoms, impact, and affected components recorded

Proactive path (common modern extension):
  trends, monitoring data, capacity signals reviewed
    → a potential cause identified before incidents occur
    → problem record opened on the potential cause
```

Reactive identification from recurring incidents is the historical core; proactive detection from trends and monitoring is the common modern layer. A major single incident can also warrant a problem record of its own.

### Investigate and determine the cause

The problem manager prioritizes the record (impact × urgency), routes it to the specialists who own the affected components, and the investigation runs against the record: linked incidents give the pattern, the configuration record shows what the affected components are and what else depends on them, logs and monitoring narrow the hypothesis. The determined cause — including a documented dead end — is recorded on the problem. While investigation proceeds, stakeholders are informed so that the organization knows the repetition is understood and being worked.

### Document the workaround

When the cause is determined but the fix is not yet in place, the workaround is documented against the problem and surfaced to the service desk: the problem moves into its known-error state. New incidents matching the pattern can be resolved quickly with the workaround instead of being re-diagnosed from scratch, and users can often reach it through self-service.

### Resolve through the permanent fix

```text
Cause recorded
  → permanent solution determined
  → fix executed
      commonly: change request raised and governed
                by IT change management, then implemented
      alternatively: fix executed directly by the responsible team
  → outcome recorded back on the problem
```

The problem record tracks the fix to completion — the associated change or release is attached, and the problem is not resolved merely because a fix was *planned*.

### Close the problem

Closure verifies the details, confirms the fix took effect and the incidents stopped recurring, closes the related incidents, and preserves the knowledge — cause, resolution, workaround — frequently as knowledge-base articles. A closed problem is one that can no longer cause those incidents; if the pattern returns, the problem is a lesson in why closure discipline matters.

### Core vs common vs optional

- **Defining core** — problem record distinct from incidents; root-cause investigation loop with a recorded cause; cause-directed disposition (workaround/known error + permanent resolution + closure tied to the incident population).
- **Standard capabilities** — incident linkage, known-error surfacing, CMDB anchoring, impact × urgency priority, change association, queue/templates/notifications, closure review and metrics.
- **Optional / variant** — proactive detection from trends and monitoring, AI prediction and clustering, productized RCA workflows, MSP/cross-customer operation, DevOps-style blending with incident response.

## Interfaces

### Problem queue / list

The problem manager's working surface.

- typical information: open problems with status, priority, linked-incident counts, age, owner
- primary actions: create a problem, prioritize, assign, link incidents, filter, search

### Problem detail

The record itself — the heart of the product.

- typical information: category and description of the disruption pattern, linked incidents, affected configuration items, status, priority, investigation notes and cause determination, attached workaround, associated changes/releases
- primary actions: link incidents, record investigation findings, set the known-error state, attach the workaround, associate a change, resolve, close

### Known-error / workaround surfaces

What the service desk consumes: workaround entries attached to problems, known-error views for agents handling matching incidents, and knowledge-base publication for self-service.

### Investigation support

Where diagnosis happens in-product: RCA or guided-workflow views (in products that productize methods), links into logs, monitoring and telemetry, and the configuration context around the affected items.

### Configuration surfaces

Problem categories and priority scales, templates for symptoms and impact, workflows and states, notification and announcement rules.

### Dashboards and reports

Management visibility: open and recurring problems, resolution times, incidents prevented or resolved via workarounds, problem volume by service and cause, recurrence after closure.

## Important Rules / Behaviors

**A problem is not an incident, and neither closes the other.** The incident closes when service is restored; the problem closes when the cause is eliminated. A rollback that ends an outage typically leaves its problem wide open. One problem commonly explains many incidents, and the linkage is what turns repetition into evidence.

**The known error is a documented state, not an admission of defeat.** Cause known + workaround documented is itself a managed, visible state — the practice's way of converting a live cause into reduced impact while the permanent fix is pursued. The workaround is temporary by definition; a problem that ends at the workaround is still open.

**Priority derives from the incident population.** Impact is measured in affected users and components; urgency in how fast the cause must go. This keeps problem work aligned with business pain rather than with whoever shouts first.

**Closure has a test.** A problem closes against evidence that the cause can no longer produce those incidents — not against elapsed time or optimism. Related incidents close with it.

**The permanent fix usually changes the environment — so it usually goes through change management.** The problem record drives and tracks the fix; the change record authorizes and governs it. In DevOps-style organizations the same team may fix directly; the problem record still holds the cause and the outcome either way.

**Investigation is deliberate work that loses urgency contests.** Mature organizations protect problem work from being deprioritized into the next outage — and use notifications and announcements so that duplicated incident reports do not bury the investigation while it runs.

**Everything is attributable.** Findings, decisions, workaround changes, and closure are recorded against the problem with timestamps and ownership, so the record can serve audits, reviews, and the next team that hits the same cause.

## Variants

- **ITSM-suite module (dominant packaging)** — problem management as one governed practice inside a service-management suite, alongside incident, request, change, and configuration management; shared queue, forms, and CMDB with the rest of the suite.
- **DevOps-blended operation** — the practice fused with incident response and blameless post-incident reviews: the team that responds also investigates the cause, and corrective actions flow straight into that team's backlog rather than a separate problem team.
- **Proactive / AI-forward operations** — emphasis shifts toward detection before incidents: trend analysis, monitoring-driven problem candidates, AI clustering of incidents into problem candidates.
- **MSP / multi-customer operation** — problems scoped per customer environment, with cross-customer separation of records and workarounds.
- **Scale tiers** — small organizations run a lightweight problem queue with a single owner; large enterprises formalize problem-manager roles, structured RCA methods, and cross-team investigation coordination.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Incident Management | the restore-service loop for live disruptions; its resolution is deliberately restoration-only. Problem management consumes incident records as evidence afterward and aims at the cause. An incident can close while its problem stays open |
| IT Change Management | the governed loop for modifying the IT environment. The problem's permanent fix is commonly executed as a change, but the problem record is the diagnosis, not the authorization |
| IT Service Management (ITSM) | the umbrella suite and discipline; problem management is one practice/module inside it, not the whole |
| Ticketing System | generic demand-processing record machinery (tickets, queues, states, dispositions) with no cause semantics; a problem is a specialization of the ticket |
| CMDB | the authoritative record of what exists (configuration items and relationships); problem investigation consumes it for cause context — a record, not a diagnosis loop |
| AIOps Platform | automated analysis over the operational signal stream (dedup, correlation, anomaly detection); its output feeds problem identification, but its unit is the correlated signal, not the managed cause record |
| Bug Tracking System | a software defect tracked to a fix in code; a problem is an IT-operational cause whose disposition may be a workaround, a configuration fix, or a change. In dev-centric organizations one investigation may produce either object |
| Error Tracking Platform | aggregates software errors as signals; error patterns can trigger problems, but the error stream is input, not the cause record |
| Knowledge Management (in-suite) | the publication surface for workarounds and resolutions; it distributes the problem practice's output but does not investigate causes |
| Vulnerability Management | security weaknesses with their own detection→remediation lifecycle; a problem may be raised when a weakness causes incidents, but the objects and rules differ |

The sharpest boundary is with **Incident Management**: the two are fused in practice and packaged as sibling modules, but they are separable — an incident record whose resolution is restoration, and a problem record whose closure is cause-elimination, are different objects with different goals. The second sharpest is with **IT Change Management**: the problem finds and frames the cause; the change governs the modification that removes it.

## Representative Products

- Atlassian Jira Service Management — dev-oriented ITSM suite; problem management with incident linkage, RCA support, and corrective-action tracking; advocates blending problem and incident practices
- ManageEngine ServiceDesk Plus — ITIL-certified mid-market suite with structured RCA workflows, known-error marking, and CMDB/problem/change association
- Freshservice (Freshworks) — SaaS ITSM suite with problem records, known-error/KEDB handling, and AI-assisted identification; strong published ITIL process documentation

The defining core was checked against the ITIL-classical service-desk tradition (problem registers, known-error databases, error control via change) so that the definition does not overfit the current AI-assisted SaaS packaging.

## Sources

Research date: **2026-09-08**

- Atlassian — "What is problem management?" (official ITSM practice hub; definitions, process, JSM capabilities): https://www.atlassian.com/itsm/problem-management
- Atlassian — "Problem management vs. incident management" (official incident-management practice page): https://www.atlassian.com/incident-management/devops/incident-vs-problem-management
- ManageEngine — ServiceDesk Plus problem management (official product page incl. ITIL FAQ and three-phase process): https://www.manageengine.com/products/service-desk/problem-management.html
- Freshworks — "ITIL problem management explained" (Freshservice official process guide): https://www.freshworks.com/freshservice/itsm/problem-management/

> Sourcing limitations: official documentation for the largest enterprise ITSM suites — including the enterprise market leader — could not be retrieved from the research environment on 2026-09-08 (timeouts; product support pages missing). Enterprise-specific mechanics are therefore not asserted anywhere in this document; cross-product claims rest on the three captured products. Open-source ITSM products with explicit problem objects were also not reachable. Precise vendor specifics (exact state labels, SLA numbers, plan-gated features) are intentionally not stated; product-by-product observations are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample breadth check are recorded in the paired Research Notes.
