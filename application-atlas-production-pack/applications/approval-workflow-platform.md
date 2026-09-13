# Approval Workflow Platform

## Overview

An **Approval Workflow Platform** is an organization-facing application that turns authorization requests into tracked decision workflows: a submitted request is captured as a structured record, routed by the system — following configured rules — to one or more designated approvers, each records an explicit approve / reject / return decision, the request's state advances accordingly until an outcome is reached, and the full, attributable decision history is retained as the authorization record.

The defining core is small:

```text
Submitted request (what is being asked, from whom, with supporting data)
  → routed to designated approver(s) in a defined path
    → recorded decisions (approve / reject / return, with comments)
      → request state advances to an outcome
        → outcome + attributable decision history retained
```

The platform replaces the ad-hoc baseline it is usually bought to replace — approval requests living in email threads, chat messages, and spreadsheets, with no shared status, no enforced order of sign-off, and an audit trail that has to be reconstructed after the fact. What mature products add on top of the core — form builders, SLA timers, escalation, dashboards, mobile approvals, document handling, AI-assisted triage — makes the loop faster and more governable, but the loop itself is the Type.

When the center of gravity shifts away from routing a request to a recorded human authorization decision — toward arbitrary task automation, whole-process modeling, or fulfilling service work — the product has drifted into a neighboring Application Type.

## Users & Context

Three recurring roles, plus the organization that owns the process:

- **Requester** (any employee): submits a request — an expense claim, leave, purchase, capital expenditure, vendor addition, system access, discount, document sign-off — then watches its status instead of chasing approvers by email.
- **Approver** (typically a manager, finance, department head, or functional owner such as IT or HR): receives pending requests assigned to them, reviews the submitted details and attachments, asks for clarification, and records a decision. Most approvers act on requests only occasionally, so products put heavy weight on making this surface fast and interruptible.
- **Process / workflow administrator** (business operations or IT): builds and maintains each approval process — the request form, the sequence of approval steps, the routing rules, reminder and escalation behavior, and who may see or act on what.

The typical environment is internal operations across finance, HR, IT, procurement, and general management. The platform acts as the **system of record for the authorization decision itself**: the decision and its evidence live here even when the work the decision authorizes (payment, provisioning, purchase) happens in another system.

## Core Model

### The defining structure

**Request.** The central object: one submitted instance of something awaiting an authorization decision. A request carries the requester's identity, the submitted data captured on a structured form (amounts, dates, line items, justifications), and usually attachments (receipts, quotes, contracts). Everything else in the system exists in relation to a request.

**Approval path (workflow).** The configured route a request must travel: an ordered set of approval stages, each expecting a decision from a designated approver. Paths support both **sequential** stages (manager, then finance, then controller) and **parallel** stages (HR and IT review simultaneously). A path is defined once by an administrator and then applied to every request of that type.

**Approver designation.** Who must decide at each stage. Products designate approvers in several ways — a named person, a role or group (any member of Finance can decide), a dynamic rule such as "the requester's manager," or an external participant outside the normal user population. Routing between stages is commonly **conditional on request data**: amounts above a threshold add a stage, certain departments route differently, low-risk routine requests skip stages or auto-approve.

**Decision.** The action an approver takes on a request: **approve**, **reject**, or **send back for revision**, normally with a comment explaining the choice. Decisions are the only thing that moves a request forward. Each decision is attributed — who decided, when, on what, with what comment.

**State.** The request's visible position in its lifecycle: not yet submitted, awaiting a specific approver, returned for revision, approved, rejected, withdrawn, cancelled. Both requester and approvers can see where a request stands and who it is waiting on.

**Decision history (audit trail).** The retained, append-style record of everything that happened to a request: submissions, edits, comments, each decision with its actor and timestamp, escalations, and the final outcome. This history is what makes the platform the system of record — audit and finance read it instead of reconstructing events from email.

### One structure, many implementations

The core is written in conceptual terms; products realize each piece differently:

```text
Concept:                Request capture
Implementations:        purpose-built request forms, records created in
                        another system and sent for approval, document
                        packages attached to a request

Concept:                Approval path definition
Implementations:        no-code visual designers, stage lists configured
                        in a form builder, approval steps inserted into a
                        general automation flow

Concept:                Approver designation
Implementations:        named users, roles/groups, requester's manager
                        (dynamic), external or guest participants,
                        no-login signed links

Concept:                Decision response channel
Implementations:        in-app task list, email response, chat
                        notification, mobile app, secure approval link
```

A reader who has only seen one implementation — for example, a no-code SaaS designer — should still be able to recognize an approval step embedded in an ERP or automation platform as the same underlying structure.

### Standard capabilities of mature products

Dedicated products in this category nearly always include:

- form builder with validation, conditional fields, and reusable field logic
- conditional routing rules on request data (amount, department, type, risk)
- return-for-revision loop back to the requester, with resubmission
- reminders and escalation when a request sits too long with one approver
- notification across email, chat, and mobile push
- requester-visible status ("where is my request right now")
- dashboards for pending load, cycle times, bottlenecks, and missed deadlines
- exportable audit logs and audit-ready reporting
- templates for common approval types (expense, leave, CapEx, access, vendor, contract)
- handoff of approved requests into systems of record (ERP, HR, identity, document storage)
- mobile approval surface

Some products extend further into capabilities that depend on segment and regulatory posture — a policy layer governing who may approve what (including segregation-of-duties constraints), document-centric features (embedded viewing, generation, e-signature), accounting enrichment such as account/cost-center coding, no-login or license-free approver participation for occasional approvers, and AI-assisted decisioning that auto-approves routine in-policy requests and escalates genuine exceptions with recorded rationale.

## How It Works

### Configure the process (administrator)

```text
Define the approval type
→ build the request form (fields, validation, conditional sections)
→ lay out the approval path (stages; sequential and/or parallel)
→ set approver designation per stage (person / role / dynamic rule)
→ add routing conditions on request data (amounts, department, type)
→ configure reminders, escalation, and notifications
→ publish; govern who may create, view, approve, administer
```

Many products shorten this with prebuilt templates for common approval types.

### Submit and route (requester + system)

```text
Requester fills the form, attaches supporting documents
→ request is created and becomes visible in their request list
→ system validates the submission (completeness, policy pre-checks
   such as budget, duplicates, or master-data presence, where offered)
→ routing rules select the path and the first approver(s)
→ approvers are notified (in-app, email, chat, or mobile)
```

### Decide (approver)

```text
Approver opens the pending request
→ reviews submitted data, attachments, and prior comments
→ optionally asks the requester for clarification
→ records a decision:
     approve            → request advances to the next stage
     reject             → request ends with a negative outcome
     send back          → request returns to the requester for revision
→ comment is attached; decision is logged with actor and timestamp
```

Parallel stages advance only when all their approvers (or the configured quorum) have decided; sequential stages wait for each in turn.

### Close and hand off

```text
Final approval reached
→ outcome recorded; request state becomes approved
→ downstream action triggered: purchase order raised, payment queued,
   access provisioned, document released, notification to requester
→ request and its decision history remain findable for audit
```

### Exceptions that shape real usage

- **Stalled requests** — no decision within the expected time. Products send reminders, then escalate to a higher approver or an exception queue; some track explicit service-level deadlines per stage.
- **Returned requests** — the requester revises and resubmits; the cycle repeats, with prior rounds still visible in the history.
- **Withdrawal / cancellation** — the requester (or the sender, in automation-embedded implementations) can cancel a pending request that was submitted in error or is no longer relevant; the cancellation is itself recorded.
- **Approval is not execution** — an approved request authorizes the work; it does not perform it. The handoff to the executing system is a distinct, often automated, step.

## Interfaces

### Request form / submission surface

What the requester uses to start.

- typical information: typed form fields, conditional sections, file attachments
- primary actions: submit, save draft, attach documents

### My requests / status tracker

The requester's view of everything they have submitted.

- typical information: request type, submitted date, current state, current stage and pending approver, outcome
- primary actions: view detail, revise a returned request, withdraw a pending one

### Approver inbox / pending approvals

The approver's working surface, also reachable via email, chat, and mobile.

- typical information: queue of pending requests with submitted details, attachments, prior decisions and comments, deadline indicators
- primary actions: approve, reject, send back with comment, comment / ask for clarification, reassign (where supported)

### Workflow designer / admin console

The administrator's configuration surface.

- typical information: list of approval workflows, each with its form, stages, routing rules, notification and escalation settings, roles and permissions
- primary actions: create/edit workflow, publish versions, manage users/roles, configure reminders and integrations

### Dashboards and reports

The process-owner view across many requests.

- typical information: pending volume, cycle times, bottlenecks per stage or approver, overdue items, outcome statistics
- primary actions: filter, drill into individual requests, export audit-ready logs

## Important Rules / Behaviors

- **Decisions are attributable and logged.** Every approve / reject / return is recorded with who, when, and what was said. This is the substrate of the audit trail and is treated by buyers as non-negotiable.
- **State advances only through recorded decisions** (plus configured system actions such as auto-approval or escalation). A request never silently moves between stages; where it stands and why is always visible.
- **Routing is rule-driven on request content.** The path is not chosen ad hoc per request; the administrator's conditions (amount thresholds, department, request type, risk) decide who must sign. Changing the rules is an administrative act, not a per-request workaround.
- **Only designated approvers decide.** Deciding is a permission bound to the stage's designation; requesters and bystanders can see status but cannot act on requests assigned to others.
- **Rejection and return loop back rather than dead-end.** A returned request goes to the requester for revision and resubmission; the prior rounds remain in the history.
- **Inactivity is managed, not ignored.** Reminders and escalation are standard machinery because approver silence is the most common failure mode of the process.
- **The policy layer sits above the workflow layer.** Mature deployments also govern who may approve what, and may enforce constraints such as segregation of duties; the exact enforcement varies by product.
- **Outcome is evidence, and usually a trigger.** The retained history serves audit; the approved outcome commonly triggers action in the system of record where the real work happens.

## Variants

- **Horizontal approval suites** — general-purpose platforms where any department builds approval processes on shared designer, forms, and reporting machinery; the dominant SaaS pattern.
- **Document-heavy enterprise approval** — deployments centered on contracts, invoices, and compliance evidence, with embedded document viewing/generation/signing and on-premises or hybrid deployment options for regulated industries.
- **Forms-first approval workflows** — implementations that grew out of online form builders, where a form submission kicks off a multi-step approval route; common in education and mid-market back offices.
- **Approval management at enterprise scale** — emphasis on the policy layer above the workflows: who-can-approve-what catalogs, segregation of duties, uniform governance across many departmental workflows.
- **Approvals embedded in another platform** — the same loop implemented as a capability inside an automation, ERP, HR, or service-management product rather than as a standalone purchase. The structure is identical; the Type boundary is whether the authorization loop is the product's organizing purpose.
- **AI-assisted decisioning** — an emerging layer in which routine in-policy requests are auto-approved and exceptions escalated with recorded rationale, layered on the same human decision chain.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Workflow Management Platform | shares the engine family (designer, forms, routing); its organizing purpose is arbitrary task/automation sequences, not authorization decisions — an approval here is one step among many |
| Business Process Management Platform | adds explicit process modeling, cross-system orchestration, and process discovery/mining; the request-decision loop is a narrow special case |
| Enterprise Request Management | centers on service requests fulfilled by a team (intake → assignment → fulfillment); approval appears as one gate inside that lifecycle, not the purpose |
| Online Form Builder | ends at collecting structured data; it does not route submissions through designated decision chains with tracked state |
| Deal Desk / Commercial Approval Platform | owns a domain object (the deal) whose lifecycle includes approval gates with commercial logic; the approval workflow platform owns the generic request itself |
| Purchase Order Management / IT Change Management | likewise own domain objects (PO, change record) with embedded approval steps; the approval loop recurs inside them but is not their center |
| IT Service Management | approval tasks exist inside tickets and change records; the ticket's fulfillment lifecycle, not the authorization chain, is the primary object |

The closest and most consequential boundary is with the **Workflow Management Platform**: the market mostly sells approval workflows as a use case of horizontal workflow engines, and the two share designers, forms, and routing. The structural test is the organizing object — a request awaiting an authorization decision versus a task in an arbitrary process.

## Representative Products

- Kissflow
- Cflow
- Nutrient Workflow (Integrify lineage)
- onPhase Forms (frevvo lineage)

The core loop was additionally checked against a platform-native implementation of the same structure (approvals embedded in a general automation platform) to avoid over-fitting the definition to standalone no-code products.

## Sources

Research date: **2026-09-06**

- Kissflow — Workflow Management and Automation Platform: https://kissflow.com/workflow/ ; Approval Workflow Software: https://kissflow.com/workflow/approval-workflow-software/
- Cflow — Approval Workflow Software: https://www.cflowapps.com/platform/approval-software/ ; Help Center / Knowledge Base: https://www.cflowapps.com/help/
- Nutrient Workflow (Integrify) — homepage: https://www.integrify.com/ ; overview: https://www.nutrient.io/workflow-automation/overview/
- onPhase Forms (frevvo) — homepage: https://www.frevvo.com/ ; Forms & Workflow: https://www.onphase.com/forms-workflow-automation ; documentation portal: https://docs.frevvo.com/
- Microsoft Learn — Create and test an approval workflow with Power Automate (platform-native contrast sample): https://learn.microsoft.com/en-us/power-automate/modern-approvals

> Sourcing limitations: all evidence is from official product/support surfaces retrieved on 2026-09-06; the frevvo/onPhase documentation has migrated and deep operational pages were not reachable, so that product's evidence is product-page level and claims leaning on it are stated more cautiously. Numeric limits, exact default settings, and per-product state names are intentionally not asserted in this document; detailed vendor observations are retained in the paired Research Notes. Delegation/coverage behavior of pending approvals was not directly evidenced in the accessible sources and is therefore not claimed here.
