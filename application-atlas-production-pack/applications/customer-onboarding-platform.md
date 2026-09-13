# Customer Onboarding Platform

## Overview

A **Customer Onboarding Platform** is vendor-side software for running one specific new customer's transition from closed deal to first value. Its unit of record is a per-customer onboarding engagement — a persistent, individually identified engagement that carries a structured plan of work, distributes that work across both the vendor's team and the customer's team, and tracks progress toward a defined completion: go-live, activation, or handoff to steady-state management.

The problem it solves is structural: onboarding a new B2B customer is a joint project. The vendor must configure, migrate, integrate, and train; the customer must supply data, make decisions, complete setup steps, and attend sessions. Neither side's work fits a private to-do list, and email-and-spreadsheet coordination loses track of who owes what. The platform holds the shared plan of work, makes each side's obligations visible and actionable, and records how the transition is progressing.

Boundary: the Type covers the managed transition engagement. It does not cover the ongoing management of the account after handoff (customer success territory), the measurement of product usage (product analytics territory), or guidance experiences deployed inside the vendor's own product UI (in-app onboarding tools, a different product family).

## Users & Context

Primary users sit on the vendor side of the customer relationship:

- **Onboarding manager / implementation manager** — owns the engagement: instantiates the plan from a template, assigns tasks to both sides, chases blockers, drives to go-live.
- **Vendor specialists** — solution architects, data-migration engineers, trainers, support engineers: complete the vendor-owned technical and enablement tasks assigned to them.
- **Customer success / account team** — receives the handoff at completion; in workspace-style products, may co-own the engagement from the sales stage onward.

Secondary but structurally essential users sit on the customer side:

- **Customer project lead / champion** — the customer-side counterpart named on the engagement; completes customer-owned tasks, approves milestones.
- **Customer task assignees** — individual people on the customer's team who receive specific tasks (provide data files, fill forms, complete configuration, attend training), often notified by email or SMS and sometimes completing tasks without ever logging in.

Typical context: B2B software and services companies with a non-trivial implementation or activation phase between signature and first value. The engagement usually starts from a sales handoff (CRM opportunity won) and ends at a go-live milestone, after which the account moves to ongoing customer success management.

## Core Model

### The Defining Core

```text
Customer
  └── Onboarding Engagement (one per customer transition)
        └── Plan of Work
              ├── Stages / Phases / Milestones
              └── Tasks (owner, status, dates, instructions)
                    ├── owned by vendor-side users
                    ├── owned by the customer (and sometimes third parties)
                    └── visibility-controlled per item
        └── Progression → defined completion (go-live / activation / handoff)
```

Four properties together make the Type recognizable. Remove any one and it becomes a different kind of software:

- **Per-customer engagement of record.** A persistent, named engagement for one specific customer, distinct from the account record itself. It exists to take that customer from signed to live. Without it, there is only account management.
- **Structured plan of work.** The engagement carries a plan organized as stages, phases, or milestones containing tasks; each task has an owner, a status, and dates. Without it, the engagement is a contact with notes.
- **Two-sided work distribution.** Tasks are owned by vendor-side users *and* by the customer — sometimes by third parties such as implementation partners. The customer is a tracked worker in the plan, not merely its subject. Without this, the software is an internal implementation project tracker.
- **Tracked progression to a defined completion.** Statuses and milestones roll up to an explicit end state — go-live, activation, first value, handoff. Without it, the plan is a checklist with no journey.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical but do not define it:

- **Customer-facing shared surface** — a portal or shared workspace view where the customer sees the plan, their tasks, progress, and resources. This is the modern realization of customer participation; older spreadsheet-era onboarding satisfied the core without one.
- **Per-item visibility control** — internal-only tasks, hidden sections, or name-only exposure, so the vendor can keep internal notes and sensitive items out of the customer's view while sharing everything else.
- **Reusable onboarding templates** — project/plan/workspace templates instantiated per customer, with dynamic personalization (customer name, dates, variables) and centrally synced content.
- **Dependencies and scheduling** — tasks blocked by predecessor tasks; durations and relative or auto-calculated dates; the plan timeline shifts as reality shifts.
- **Notifications to both sides** — task-assignment emails with instructions and status-update actions, due-date reminders, and in some products SMS for customer assignees.
- **Customer data collection** — forms, file-upload requests, and attachments, so the customer's "homework" (data files, access credentials, decisions) is captured in the engagement.
- **Shared resources and content** — documents, training material, embedded content, checklists, and links made available to the customer in context.
- **Communication threads** — comments and messages on tasks or the engagement, with internal-only and customer-visible layers.
- **Progress reporting and portfolio views** — dashboards across many concurrent onboardings; customer-engagement reporting; signals that draw attention to stalled or at-risk engagements.
- **CRM integration and sales handoff** — the engagement is created from or linked to the won opportunity; account mapping keeps engagement and CRM in sync.

### One Structure, Many Implementations

The core is written conceptually. Products realize it differently:

```text
Concept:  Per-customer engagement
Forms:    customer-bound project (project-first products) · shared client workspace
          (workspace-first products) · branded per-account hub (success-workspace products)

Concept:  Plan of work
Forms:    phased project plan with dependencies · mutual action plan (checklist /
          timeline / kanban) · journey with milestones and tasks

Concept:  Customer participation
Forms:    portal login · shared workspace access · task completion directly from
          notification email or SMS · file-upload and form requests
```

A reader who has only seen one form (say, the portal-first style) should still be able to recognize the others from the core.

## How It Works

### Start the engagement

```text
Deal won in CRM (or customer identified)
→ create the engagement for that customer
→ instantiate the onboarding template (phases, tasks, durations)
→ set the start date; the plan's timeline is computed
→ name the vendor-side owner and the customer-side champion
→ invite the customer's team (by email; portal or shared-workspace access)
```

The template encodes the vendor's repeatable onboarding methodology; the instance is adapted to the specific customer.

### Run the plan of work

```text
Tasks unlock as dependencies are met
→ assignees are notified (email / SMS / in-app) with instructions and due dates
→ vendor specialists complete vendor-owned tasks
→ customer assignees complete customer-owned tasks (portal, or directly from the notification)
→ customer submits required data (file uploads, forms, attachments)
→ statuses update; the plan's progress and timeline reflect reality
→ blocked and overdue work is surfaced for attention
```

The interaction loop is the chase: the onboarding manager watches the plan, unblocks dependencies, reassigns stalled work, and keeps both sides moving. Per-item visibility control runs throughout — internal tasks stay hidden from the customer's view while shared tasks, progress, and resources remain visible.

### Reach completion and hand off

```text
Milestones complete (configuration, data migration, training, validation)
→ go-live / activation milestone reached
→ engagement marked complete
→ account handed off to steady-state management (customer success)
→ engagement record retained as the onboarding history
```

### Core vs Common vs Optional

- **Defining core** — per-customer engagement of record; structured plan of work; two-sided work distribution; tracked progression to a defined completion.
- **Standard capabilities** — customer-facing portal or shared surface; per-item visibility control; templates; dependencies and scheduling; notifications; data collection; shared resources; communication threads; portfolio reporting; CRM handoff.
- **Variant / optional** — vendor-side resource management and staffing; time tracking and project financials; multi-workstream program management; digital-touch (automated, low-touch) onboarding; embedded or white-labeled portals; third-party partner participation; pre-sale mutual action plans (POCs); post-onboarding continuation (success plans, business reviews); AI assistance.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Engagement list / portfolio view

The vendor team's entry surface across all onboardings.

- lists engagements with customer, owner, status, progress, key dates
- primary actions: open an engagement, create one from a template, filter and bulk-update, spot stalled engagements

### Plan view (project plan / mutual action plan)

The heart of the product for vendor users.

- stages/phases/milestones with tasks; owner, status, dates, dependencies per task
- timeline and checklist representations; progress roll-up
- primary actions: add/edit tasks, assign owners on both sides, set dependencies and dates, update status, hide or expose items

### Customer portal / shared workspace view

What the customer sees.

- the shared plan with their tasks and due dates, overall progress, milestones, resources, and contacts
- primary actions: complete their tasks, upload requested files, fill forms, download resources, comment, update status (sometimes directly from a notification email or SMS)

### Task detail

- instructions, attachments, checklist, assignee, dates, dependencies, messages
- visibility state (customer-visible / name-only / internal-only) is set here
- primary actions: update status, reassign, comment, attach, log time (vendor-side, where offered)

### Reporting / dashboard

- engagement progress, on-time completion, customer engagement and participation, portfolio health across onboardings
- primary actions: build reports, monitor warnings, review completed onboardings

### Settings / templates

- template authoring (phases, tasks, forms, documents), dynamic variables, branding, roles and permissions for internal users and customers, integrations (CRM, communication tools)

## Important Rules / Behaviors

- **The customer is a worker, not an audience.** Customer-owned tasks carry the same structure as vendor tasks — owner, status, dates — and the plan cannot complete without them. Notifications, email/SMS status updates, and file-upload requests exist to make customer participation low-friction.
- **Visibility is per item, not per person.** The shared surface shows a curated subset: internal tasks, notes, and sensitive fields are hidden or name-only, while the shared plan stays honest about overall progress. This two-layer visibility is a structural behavior, not a cosmetic setting.
- **Dependencies gate the work.** A task becomes available when its predecessors complete; assignment notifications fire on unlock. The plan is a small state machine, and the onboarding manager's job is keeping it unblocked.
- **The engagement ends at a defined completion.** Go-live/activation/handoff is an explicit milestone; after it, the engagement is closed and the account continues in other systems (customer success, support). The engagement record remains as history.
- **Templates encode methodology; instances carry reality.** The template is the vendor's repeatable best practice; the per-customer instance diverges as reality demands — dates shift, tasks are added, phases are re-ordered — without breaking the link to what was planned.
- **Time tracking, where present, is primarily vendor-side effort capture.** Some products exclude customer and third-party assignees from logging time; portal-side time features vary by product.

## Variants

- **Project-management-grade** — deep plan machinery (phases, dependencies, baselines) plus vendor-side resource management, time tracking, and project financials; common where onboarding is delivered by a professional-services or implementation organization.
- **Portal-first** — the customer-facing experience is the product's center: a polished, brandable (sometimes embeddable) portal where the customer lives during onboarding.
- **Workspace-first** — a shared client workspace that spans the relationship (sales materials → onboarding plan → ongoing collaboration), with the onboarding plan as one section; the engagement may start before the deal closes.
- **Success-workspace** — a branded per-account hub covering onboarding, adoption, business reviews, and renewals; onboarding is the first program of a longer customer journey.
- **CS-suite module** — onboarding realized as a lifecycle stage and program toolkit inside a customer success platform, sharing its account model, automations, and customer portal.
- **Digital-touch / scaled onboarding** — templated, automated, low-touch journeys for high-volume segments; the engagement structure survives, with automation replacing much of the manual chase.
- **Pre-sale use** — mutual action plans for POCs and trials, reusing the same plan machinery before a deal closes.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Customer Success Platform | unit of record is the ongoing account relationship across the whole lifecycle (health, success plans, renewals, reviews); here the unit of record is the per-customer transition engagement ending at first value. Overlap: customer portal, customer-assigned tasks, success plans |
| Project Management Application | generic projects/tasks/dependencies for internal teams; lacks the customer-bound engagement, two-sided work distribution, and shared customer surface |
| Professional Services Automation | centers on billable service-delivery economics (utilization, time & billing, revenue recognition); onboarding-grade products may carry this machinery, but the defining core is the customer transition, not the billable engagement |
| Employee Onboarding Platform | same journey/checklist pattern, different subject: orchestrates a new hire's entry into employment (compliance, pay, workplace, team), not a customer's adoption of a product or service |
| In-app onboarding / guidance tools (no directory leaf) | deploy tours, checklists, and tooltips inside the vendor's own product UI for end users, targeted by segments and product signals; no per-customer engagement or two-sided plan. Complementary — a vendor may run both |
| Customer Training / Academy Platform | centers on learning content, courses, and certification; training content appears here only as one resource type inside the engagement plan |
| Customer Portal | a surface, not a managed engagement; the onboarding platform uses a portal as one of its surfaces |
| CRM | stores the account and opportunity and the handoff moment; the onboarding platform instantiates and runs the engagement that follows |

The boundary with the Customer Success Platform is the most important one, because the two overlap on portals, customer-assigned tasks, and success plans. The structural difference is the unit of record: a per-customer engagement with a defined completion (this Type) versus the ongoing account relationship (customer success).

## Representative Products

- GuideCX — portal-first pure-play
- Rocketlane — project-management-grade pure-play (onboarding, implementation, professional services delivery)
- Dock — workspace-first (sales handoff → onboarding → ongoing client collaboration)
- EverAfter — success-workspace (branded per-account hub; onboarding as first program)
- Totango — customer success platform; included as the boundary check for the CS-suite-module variant

## Sources

Research date: **2026-09-08**

- Rocketlane Support / Help Center — https://help.rocketlane.com/ (project creation, team & customer invitations, customer portal section)
- GuideCX Knowledge Base — https://help.guidecx.com/ (GUIDE 2.0 collection; "Tasks in 2.0")
- Dock Help Center — https://help.dock.us/ (Workspaces; "What are Project Plans?"; "Tasks in Project Plans")
- EverAfter — https://www.everafter.ai/ (product and solutions pages)
- Totango Support — https://support.totango.com/hc/en-us (Terminology guide)
- Userflow — https://userflow.com/ (boundary check for the in-app onboarding category)

> Sourcing limitation: EverAfter's help center was unreachable from the research environment on 2026-09-08; its observations rest on official product/solutions pages, so task-level mechanics for that product are asserted at structure level only. Totango and Userflow were used as boundary checks, not as members of the Type. Precise numeric limits, plan-tier gating, and product-specific defaults are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
