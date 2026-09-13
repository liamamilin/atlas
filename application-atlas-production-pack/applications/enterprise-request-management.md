# Enterprise Request Management

## Overview

An **Enterprise Request Management** application is the internal request-fulfillment orchestration system of an organization: it publishes a defined catalog of requestable services, captures internal requesters' submissions against those offerings, routes each request through a defined fulfillment path — approval gates where required, fulfillment tasks and/or automated actions executed by the responsible internal provider — and advances it through a tracked lifecycle to a completed outcome, with status visible to the requester throughout.

The defining structure is small:

```text
Published catalog of defined service offerings
└── Submitted request (internal requester × offering × submitted data)
    └── Routing into fulfillment (approval gates, tasks, automation)
        └── Tracked lifecycle to an outcome, requester-visible
```

Everything else commonly associated with the category — self-service portals, multi-step approval chains, SLA clocks, dynamic forms, cross-system provisioning automation, multi-department workspaces, analytics — is widespread in mature products but is not what makes the product this Type. The literal "Enterprise Request Management" label has largely receded in market language; the same structure is overwhelmingly sold as "service request management", "service catalog", or "enterprise service management" inside ITSM/ESM suites, with a smaller standalone-orchestration segment. The Type is defined by structure, not by the label.

## Users & Context

The requester population is **internal** — employees and teams of the operating organization. This is part of the Type's frame: the same machinery deployed for external customers is the customer-support Type's frame, and deployed for residents is the public-sector twin.

Primary users:

- **Requester (employee)** — browses the catalog of services the organization offers, submits a request against a specific offering, and tracks its progress to completion.
- **Approver (manager, cost-center owner, data owner, security team)** — authorizes requests that require it, typically by acting on a notification without opening the fulfillment system.
- **Fulfiller (service team member or agent)** — receives routed requests, works the fulfillment tasks, and moves the request through its lifecycle.

Secondary users:

- **Service owner / administrator** — defines catalog offerings: request forms, visibility, approval paths, fulfillment routing, delivery expectations.
- **Service-management lead** — monitors volumes, fulfillment times, and service-level compliance across offerings and departments.

Typical context: an organization where employees previously requested things (equipment, access, accounts, onboarding, facilities work, travel) through email and hallway conversations, and the organization wants every request to arrive through one front door, be routed by rule rather than by memory, and be trackable by both the requester and the provider.

## Core Model

### The Defining Core

Four structures. Remove any one and the product stops being recognizable as this Type:

- **Published catalog of defined service offerings** — the organization pre-defines what can be requested. Each offering carries a request form and, implicitly, a fulfillment path. This is the discriminator against free-form ticketing: the request is bound to a defined offering, not merely typed after the fact.
- **Submitted request as a tracked record** — an internal requester's submission bound to a specific offering, holding the submitted data and a tracked lifecycle state. The request is persistent and individually identifiable, not a one-off form response.
- **Routing into fulfillment** — the request is directed to a responsible internal provider (team, individual, or automation) along a defined path. Approval gates sit inside this path where the offering requires them; fulfillment may be decomposed into tasks.
- **Tracked lifecycle to an outcome with requester-visible state** — the request advances through states (received → approved/assigned → fulfilled → closed, or rejected/cancelled) and the requester can see where it stands.

The requester population being internal is part of the frame: "enterprise" is not decoration.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the Type practical; they do not define it.

- **Requester portal** — the catalog front door: browse, search, submit, and a "my requests" tracker showing live status.
- **Approval machinery** — multi-step chains, approver groups, approval by email/chat/mobile, delegation. Approvals appear in essentially all sampled products, always as a gate inside the fulfillment flow, never as the organizing purpose.
- **Fulfillment task decomposition** — a request broken into tasks assigned to teams or individuals, with task-level targets (OLA-style) distinct from the requester-facing SLA.
- **Service-level targets per offering** — delivery expectations held on the catalog item, measured from submission, with escalation before breach.
- **Dynamic request forms** — conditional fields adapting to the requester's role, department, or answers; pre-population from organizational data (manager, cost center, entitlements).
- **Catalog item metadata** — owner, description, category, cost, estimated delivery, visibility restrictions (who may request).
- **Notifications and status updates** — to requester and fulfillers at lifecycle transitions.
- **Fulfillment automation** — provisioning or record-creation across connected systems as part of fulfillment; depth varies widely (see Variants).
- **Reporting and analytics** — request volumes, fulfillment times, bottlenecks, SLA compliance.
- **Knowledge base deflection and satisfaction measurement** — common in suite products.
- **Multi-department operation** — department workspaces or segregated desks so HR, facilities, finance, and IT each run their own service operation on shared machinery.
- **Audit trail** — who requested, approved, fulfilled, and when; retained as the compliance record.

### One Structure, Many Implementations

The Core Model is written in conceptual terms. Implementations differ on every layer:

```text
Concept:        Catalog of offerings
Implementations:  formal service-catalog items in categories, request types
                backed by work types, forms grouped in portal containers

Concept:        Submitted request
Implementations:  ticket bound to a service item, form submission instance,
                request/work-item duality (external vs internal view)

Concept:        Routing into fulfillment
Implementations:  rule-evaluated business rules, workflow stages, queues with
                assignment, orchestrated automation across backend systems

Concept:        Requester-visible state
Implementations:  portal status list, progress activities exposed to the
                submitter, notification stream
```

A reader who has only seen one implementation — say, a request catalog inside an ITSM suite — should still be able to recognize a standalone orchestration product or an older Remedy-generation request system from the Core Model.

## How It Works

### Define the offering

The service owner configures a catalog item: what it is, who may request it, the request form (fields, conditions), the approval path (if any), the fulfillment routing (which team, which tasks, which automation), and the delivery expectation. The item is published to the catalog — or held as a draft until ready.

### Submit the request

```text
Requester opens the portal
→ browses or searches the catalog
→ selects an offering
→ completes its request form (often pre-populated from their profile)
→ submits
```

The submission creates the tracked request record. From this point the requester's role changes from actor to observer: the system, not the requester, drives the flow.

### Route and approve

Business rules evaluate the request — by offering, cost, security classification, department, or submitted data — and determine the path. Where approval is required, the request pauses at an approval gate: the designated approver is notified and can approve or reject from email, chat, mobile, or the portal, with delegation supported in mature products. A rejection returns or closes the request with the reason recorded.

### Fulfill

The approved request reaches the responsible provider. Fulfillment takes one of two shapes depending on the product philosophy:

- **Ticket-and-human**: the request lands in a team's queue, is assigned, and is worked as tasks by people.
- **Orchestrated automation**: the request triggers a defined workflow that executes across the involved backend systems — creating accounts, provisioning access, placing orders — with parallel and sequential steps, dependency management, and exception routing when a step fails.

Most products sit between these poles; the suite products fulfill natively or via integration apps, while the standalone-orchestration products make cross-system execution their differentiator.

### Track and close

The request advances through its lifecycle. The requester sees status and progress throughout — including intermediate states such as awaiting approval or assigned to a team. On completion, fulfillment is confirmed, the requester is notified, and the full trail (submission, approvals, tasks, timestamps) is retained as the audit record.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- published catalog of defined service offerings
- submitted request as tracked record (internal requester)
- routing into fulfillment along a defined path
- tracked lifecycle to an outcome with requester-visible state

**Common mature structure** — present in most modern products:

- requester portal; approval machinery; task decomposition; per-offering SLA targets; dynamic forms; catalog metadata; notifications; reporting; audit trail; multi-department operation

**Variant / optional** — depends on segment, scale, and product philosophy:

- cross-system fulfillment automation depth
- external-customer or citizen deployment of the same machinery
- knowledge-base deflection, CSAT, virtual agents / AI assistance
- deployment model (SaaS vs on-premises/air-gapped), workspace architecture

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Service catalog / requester portal

The requester's primary entry surface.

- lists the organization's requestable services, organized in categories
- typical information: service name, description, delivery expectation, cost where relevant
- primary actions: browse, search, submit a request, view "my requests"

### Request detail (requester view)

The tracker for one submitted request.

- typical information: current state, approval status, progress activities, expected completion
- primary actions: add information, cancel, approve (when the requester is also an approver), view history

### Request detail (fulfiller view)

The working view of the same record — in several products literally the same object presented differently to help seekers and agents.

- typical information: submitted data, requester and offering, priority/SLA state, tasks, internal notes, full trail
- primary actions: assign, work tasks, request more information, approve/reject, advance state, close

### Approval surface

A lightweight surface (often email/chat-embedded) where an approver sees the request's essentials and records a decision.

### Catalog administration

The service owner's configuration surface for offerings: forms, visibility, approval paths, fulfillment routing, delivery expectations, publish/draft states.

### Queues and reporting

Agent-side triage views over incoming requests; management views over volumes, fulfillment times, and service-level compliance.

## Important Rules / Behaviors

### The catalog binding is structural

A request is submitted *against* a defined offering, and the offering carries the form, the approval path, and the fulfillment path. This is what separates the Type from free-form ticketing, where categorization happens after intake and no pre-defined fulfillment path exists.

### Approval is a gate, not the purpose

Approvals appear throughout the category, but always as one stage inside the fulfillment flow. The object being managed is the requested service fulfilled by a team — not the authorization decision itself. Remove the fulfillment machinery and keep only the gate, and an approval-workflow platform remains.

### Dual view of one record

The requester-facing presentation and the fulfiller-facing working view are two views of the same tracked record. What the requester sees is deliberately curated (progress, status, expected completion); the fulfiller sees the operational detail.

### The requester is an observer after submission

Once submitted, the flow is driven by rules, approvers, and fulfillers. The requester contributes information and receives status; they do not steer the fulfillment path.

### Time governance attaches to the offering

Delivery expectations and service-level targets are configured per offering and measured from submission, with escalation before breach. Task-level targets (between fulfiller teams) are commonly layered beneath the requester-facing target.

### Fulfillment may span systems

In the orchestration-heavy implementations, fulfillment means executing across multiple backend systems, with failed steps routed to the right team while unaffected branches continue. In ticket-and-human implementations, fulfillment is human work inside the product. Both satisfy the core; the depth is a variant.

## Variants

- **Request-management slice of an ITSM/ESM suite** — the dominant market form: the request function sits inside a wider service-management discipline (incidents, problems, changes, knowledge, CMDB). The request machinery is the same; the surrounding discipline is the suite's.
- **Standalone catalog + orchestration layer** — a unified catalog and fulfillment-orchestration layer sitting on top of existing backend systems of record; strongest in enterprise/government deployments with many fulfillment systems.
- **Team-scale service desk** — lighter products where a team stands up a service space with request types and a help center; the same core at smaller scale.
- **Department scope** — IT-only catalogs vs all-department operation (HR, facilities, finance) with per-department workspaces or segregated desks.
- **Population extensions** — the same machinery deployed for external customers or, in public-sector deployments, for citizens; the core is unchanged, the frame is a different Type.
- **Deployment** — SaaS vs on-premises/air-gapped; single-tenant vs multi-workspace architectures.

## Related Application Types

| Application Type | Distinction |
|---|---|
| IT Service Management (ITSM) | centers the IT function's full service discipline (incident/problem/change/configuration practices); request fulfillment is one practice among many. Strip incidents/problems/changes → this Type remains; strip the catalog + fulfillment flow → ITSM remains |
| Enterprise Service Management | wraps the request flow in the full service-management discipline across departments (service levels, knowledge, measurement, governance); this Type is the request-orchestration subset. A scope gradient, not a structure wall |
| Approval Workflow Platform | its object is the authorization decision; this Type's object is the requested service fulfilled by a team. Approval appears here only as a gate inside fulfillment |
| Ticketing System / Help Desk | free-form ticket intake vs catalog-bound requests with pre-defined fulfillment paths. Remove the catalog/offering definitions → generic ticketing remains |
| 311 Citizen Service Request Platform | the public-sector twin with the same skeleton; differs in requester population (residents), routing basis (jurisdiction/location), and accountability framing (public transparency) |
| Employee Service Portal | the front-door surface (browse/submit/track); this Type is the orchestration behind it. Portals ship as components of request/ESM products |
| Workflow Management Platform | generic engines route work between people/systems but hold no requester-facing catalog or request lifecycle as first-class objects. Remove the request object + catalog → workflow engine remains |
| HR Case Management | HR cases are sensitive case types with structured findings/outcomes under confidentiality discipline; requests here are general service fulfillment. HR service requests route through this machinery; investigations do not |
| Customer Service Platform | audience identity: internal requesters vs external customers. The machinery is shared and deployable for both; the boundary is the deployment frame |
| Purchase Order Management | procurement requests may be catalog items here; the PO system remains the system of record for purchase orders. This Type routes and tracks; downstream systems execute |

The most consequential boundary is with ITSM/ESM: the most common implementation of this Type is the request-management slice of those suites. The boundary is scope-based, not structural — the same products realize both, and the Type stands on the request-fulfillment flow as its center.

## Representative Products

- Kinetic Platform (Kinetic Data) — standalone catalog + orchestration lineage
- Freshservice (Freshworks) — SaaS ITSM suite with ESM extension
- Jira Service Management (Atlassian) — team-scale service desks
- SolarWinds Service Desk — mid-market ITSM with ESM feature set

The Core Model was checked against the Remedy-generation request-management lineage (evidenced through the standalone vendor's own documented lineage) and against manual email/verbal request handling as the outside-the-Type baseline, to avoid over-fitting to the current SaaS pattern.

## Sources

Research date: **2026-09-06**

- Kinetic Data — https://kineticdata.com/ (home; service-request-management and it-service-catalog use-case pages), https://docs.kineticdata.com/ (Key Terms)
- Freshworks Freshservice — https://support.freshservice.com/ (Service Catalog configuration article; Approvals and Task management KB structure)
- Atlassian Jira Service Management — https://support.atlassian.com/jira-service-management-cloud/ ("About requests and work items"; request types; approvals)
- SolarWinds Service Desk — https://www.solarwinds.com/service-desk (product page; IT Service Catalog use-case page)

> Sourcing limitation: ServiceNow, TeamDynamix, and BMC Helix could not be reached from the research environment (JS-only docs, 403s, timeouts). The enterprise-incumbent tier is therefore characterized only indirectly; no claims are made about those products' current mechanics, and no precise numeric limits or default settings are asserted anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
