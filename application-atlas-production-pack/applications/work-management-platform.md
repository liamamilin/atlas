# Work Management Platform

## Overview

A **Work Management Platform** is a team's operational work system: it holds a team's whole ongoing work as a shared, structured population of work records, moves that work through configured process machinery, and gives the team and the organization a coordination surface that reads across all of it.

The defining structure is small:

```text
Shared work population (structured records in an organizational container hierarchy)
└── Configured process governing how work moves (status workflows, rules, approvals, intake)
    └── Cross-container coordination surface (personal work views, dashboards, rollups)
```

Three properties. If any one is removed, the product is no longer recognizable as a work management platform:

- **The shared work population as the system of record** — persistent, structured, individually addressable work records (an item, task, or row) carrying typed attributes such as status, assignee, dates, and custom fields, held in an organizational container hierarchy. The hierarchy holds the team's whole ongoing operational work; the project is one container type among several, not the unit of record.
- **Configured process governing how work moves** — the team's recurring work patterns are held in the system itself: defined status workflows, rules that act on record events, approvals that gate transitions, and intake forms that turn requests into records. Work moves by the system's machinery, not only by hand.
- **The cross-container coordination surface** — the population is worked and read above the single container: personal across-work views, dashboards and reports that aggregate many containers, and commonly portfolio or goal rollups. This is the layer that lets a team or organization see and steer all of its work.

Everything else commonly associated with these products — Gantt and timeline views, templates, integrations, workload charts, bundled docs and chat, AI assistance — is widespread in current products but is not part of the defining core.

## Users & Context

The primary user is a **team member** who does operational work inside the platform: picking up assigned records, advancing them through their states, commenting, and updating fields. Work arrives for this user both from colleagues and, in mature deployments, through intake forms and automations.

Around the member sit three further roles:

- **Team lead / manager** — organizes containers, defines statuses and rules, watches dashboards and workload, rebalances assignments.
- **Process or operations owner** — builds the machinery: intake forms, automation rules, approval chains, templates that standardize how recurring work runs.
- **Administrator** — governs the account: members and guests, permissions, security, integrations.

External participants (clients, contractors, other departments) commonly appear as restricted roles or as submitters of request forms.

The typical context is a team or department whose work is continuous — marketing operations, IT and HR requests, creative production, client deliverables, internal programs — rather than a single bounded undertaking. The platform is the place where that work is requested, tracked, executed, and reported.

## Core Model

### The Defining Core

```text
Account / Workspace
└── Container hierarchy (spaces, folders)
    └── Work containers (boards, lists, projects, sheets)
        └── Work record (item / task / row)
            ├── Typed attributes: status, assignee, dates, custom fields
            └── Process machinery attached: workflows, rules, approvals, intake
    └── Coordination surface (personal work views, dashboards, reports, rollups)
```

**The work record.** The atom of the system is a structured record of one piece of work. It carries typed attributes — a status drawn from a defined set, one or more assignees, dates, and custom fields the team defines (priority, stage, client, cost, anything). Records are individually addressable: they can be linked, filtered, grouped, and reported on by their attributes.

**The container hierarchy.** Records live in containers, and containers live in an organizational hierarchy: an account or workspace holds spaces or folders, which hold the work containers themselves. Container names differ by product — boards, lists, projects, sheets — but the structure is shared: a container is a persistent, shared, named collection of records with its own access settings. Crucially, **several container types coexist**: a bounded project, an ongoing request queue, a recurring operations board, a client list. The project is one container among several; the system of record is the whole population.

**The process layer.** Attached to the records is the machinery that moves them:

- **Status workflows** — named states (with groups such as not-started / in-progress / done) that define how a record may move; teams define their own.
- **Rules / automations** — trigger-condition-action machinery bound to record events: when a date arrives, when a status changes, when a record is created — then notify someone, assign someone, change a value, move or copy the record to another container.
- **Approvals** — gates where designated people must approve before work proceeds; in mature products these can form ordered chains and can attach to files as well as records.
- **Intake forms** — published forms whose submissions create records automatically: fields map into record attributes, the record lands in a chosen container, assignees and even an approval process can be attached by the form's configuration. Forms may be internal or open to external submitters through a public link.

**The coordination surface.** Above the containers, the platform serves views of the whole population:

- **Personal work views** — each member sees everything assigned to or involving them across all containers (My Work / My Tasks / My To-Do), plus an inbox of updates.
- **Dashboards and reports** — aggregations across many containers: counts, status breakdowns, timelines, workloads. Reports typically read live data from multiple containers in one view.
- **Rollups** — commonly, portfolios that group related containers and goals that connect work to objectives, so leadership can read progress above the team level.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Work record
Realized as:  item on a board (board-native products), task in a list (list-native),
              row in a sheet (grid-native)

Concept:   Container hierarchy
Realized as:  workspaces → folders → boards;  spaces → folders → lists;
              spaces → folders → projects;  workspaces holding sheets

Concept:   Process machinery
Realized as:  per-board automation recipes;  workflow builders with trigger/condition/action
              blocks;  request-form builders;  approval chains
```

A reader who has only seen one product should still be able to recognize the others from the core model.

## How It Works

### Set up the work system

```text
Create the workspace/account structure
→ add spaces or folders for teams, departments, or programs
→ create containers for each kind of work (a project, a request queue, an operations board)
→ define the record shape: statuses, custom fields, who can access what
```

Teams usually start from templates that pre-configure containers, statuses, and fields for a known kind of work.

### Capture work

Work enters the population in three ways:

```text
A member creates a record by hand
→ or a colleague submits an intake form, and the system creates the record
  (fields mapped, container chosen, assignee and approval attached by the form)
→ or an automation creates records on a schedule or from another system
```

### Move the work

```text
Record is created with a status and an assignee
→ assignee works it, comments, attaches files, updates fields
→ status advances through the defined workflow
→ rules fire on the way: notifications, assignments, value changes,
  moves to other containers when conditions are met
→ where approvals apply, designated approvers gate the transition
→ record reaches a terminal state (done, approved, closed)
```

The recurring version of this loop — the same request type arriving again and again — is what the process machinery exists for: the form, the statuses, the rules, and the approval chain together make the pattern run in-system.

### See and steer the whole

```text
Members read their personal work view and inbox
→ leads read dashboards and reports across containers
→ status, workload, and overdue work surface at team or organization level
→ where portfolios/goals exist, progress rolls up above the team
→ the reading drives replanning: reassign, reprioritize, re-date
```

### Defining core vs standard vs optional

**Defining core** — without these, not a work management platform:

- shared structured work records with typed attributes
- organizational container hierarchy holding several container types
- configured process machinery (status workflows; rules; commonly approvals and intake forms)
- cross-container coordination surface (personal work views + cross-container reporting)

**Standard capabilities** — present in most mature products:

- multiple switchable views over the same records (list/board/table, timeline/Gantt, calendar, workload)
- comments, mentions, attachments, activity history on records
- sharing and permission ladders (members, guests, viewers; per-container access)
- templates of recurring work; notifications; search; integrations; mobile/desktop apps; admin console

**Optional / variant** — depends on segment, plan, and product philosophy:

- goals/OKR and portfolio rollups; resource and capacity planning; time tracking
- bundled docs, whiteboards, chat
- vertical packaging (sales, development, service) on the same engine
- external request forms with submission analytics; ordered approval chains; file proofing
- AI assistance

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Work container view (board / list / sheet)

The primary working surface for a team.

- the container's records as rows or cards, grouped and colored by the team's scheme
- typed attribute columns; inline editing; sub-records beneath records
- primary actions: create record, edit attributes, assign, change status, filter/group/sort, switch view

### Record detail

The full surface of one piece of work.

- description, attributes, sub-records, attachments, comments, activity history
- primary actions: update fields, comment/mention, attach, advance status, link related records

### Personal work view

The member's across-work entry point.

- everything assigned to or involving the member, across all containers; an inbox of updates
- primary actions: open record, update, prioritize, mark done

### Dashboard / report

The coordination surface for leads and the organization.

- widgets or report blocks aggregating records across containers: status breakdowns, counts, timelines, workload
- primary actions: configure data source and widget, read, drill into underlying records, share

### Form builder / intake form

The request machinery.

- builder: question types, field mapping, destination container, visibility (internal or public link)
- submitter surface: the published form; submission creates a record
- primary actions: build form, share/deactivate, read submissions and analytics

### Automation / workflow builder

The process machinery.

- trigger → condition → action recipes, from templates or from scratch; bound to a container or broader
- primary actions: create rule, enable/disable, manage rule list

### Admin / settings

- members and guests, roles and permissions, security, integrations, plan management

## Important Rules / Behaviors

### Access is hierarchical and graded

Permissions attach at multiple levels — account, space/folder, container, record — with roles such as member, guest, and viewer. Containers can be private or open. External participants see only what is shared with them; public request forms let outsiders create records without accounts. This layered access model is structural: the same population serves internal teams and external submitters.

### Status is governed, not free

A record's status moves within the workflow the team defined; states are grouped (commonly not-started / in-progress / done) and downstream machinery keys on them. Approvals, where present, pause movement until designated people act — in some products as ordered chains.

### Rules act on records automatically

Automations fire on record events (status change, date arrival, creation) and perform actions (notify, assign, change values, move or copy records across containers). They run without manual effort once configured; products meter or cap automation usage on some plans.

### Views are projections, not copies

List, board, table, timeline, calendar, and workload are different readings of the same records; editing in one view updates the record everywhere. Reports and dashboards read live data across containers rather than snapshotting it.

### The project is a container, not the record

Progress can be read per container, but the system of record is the population: records can outlive containers, live in more than one container in some products, and be reported on across containers. Nothing in the core requires a plan-of-record for a bounded undertaking — that is the neighboring project-management Type's structure.

### Templates make patterns repeatable

Containers, records, and process machinery can be saved as templates and re-instantiated, so a proven workflow (statuses, rules, forms, approval chain) reproduces with each new instance of the same kind of work.

## Variants

- **Substrate philosophy** — grid-native products (spreadsheet-like sheets whose rows become managed work), board-native products (visual boards with typed columns), list-native products (hierarchical lists of tasks). One Type, different center surfaces.
- **Scale packaging** — SMB-friendly visual products vs enterprise products with admin consoles, audit, and governance layers.
- **Vertical packaging** — the same engine sold as sales/CRM, software development, or service-desk variants; creative/proofing-oriented variants.
- **Converged-workspace packaging** — products that bundle docs, chat, and whiteboards beside the work records so the platform is also the team's content and communication home.
- **Platform-embedded realization** — work management delivered as a surface inside a broader productivity platform (structured lists, views, and rules inside an office suite) rather than as a standalone product.
- **Intake posture** — internal-only request forms vs public external intake with submission analytics.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Project Management Application | closest sibling; market vocabulary overlaps | PM's unit of record is one bounded undertaking with a plan of record tracked to its end; here the unit of record is the whole ongoing work population and the project is one container among several. Products are attributed by center of gravity, not feature lists — the same product can be marketed in both vocabularies. |
| Task Management Application | sibling below | task management centers discrete completable task records for people (personal-first, two-state grammar); remove the request/approval/process machinery and the coordination surface and a task manager remains. |
| Project Portfolio Management Application | sibling above | PPM centers the governed investment collection above projects (selection, funding, benefits); here a portfolio is one optional rollup view over operational work, and the record is the work item, not the investment. |
| Workflow Management Platform | process-first neighbor | there the record is the configured recurring process pattern and its executed instances; here the record is the work item and process machinery is attached to it. Products' "workflow" features (automations, status workflows) are machinery over records, not process instances as the record. |
| Collaborative Spreadsheet / Structured Table | drift origin | rows as cells in a calculation grid = spreadsheet; rows become scheduled, dependent, approvable work items and the grid becomes the surface = work management. |
| Collaborative Workspace / Team Workspace Platform | content-first neighbor | workspaces center persistent shared content (pages/docs) with membership; tasks are one content type inside. Here work records with status machinery are the center; docs are one bundled surface. |
| Kanban Task Board | view/container sibling | the board is one view or container inside a work management platform; a standalone board tool is its own Type. |
| Business Management Suite | broader suite | work management lacks the customer-and-money transaction spine; it manages work for teams, not business transactions for a company. |
| Professional Services Automation | commercial-layer neighbor | PSA adds the billable-commercial layer (client projects, time-to-billing, utilization economics) over work-management-like machinery; work here carries no settlement semantics. |

## Representative Products

- Asana
- monday work management
- Smartsheet
- Wrike
- ClickUp

These five self-label the category ("work management", "Work OS", "collaborative work management") and span the substrate philosophies (list-native, board-native, grid-native) and customer tiers. The core model was checked against platform-embedded realizations (office-suite work surfaces) to avoid over-fitting to any one product family.

## Sources

Research date: **2026-09-09**

- monday.com Support Center — structural hierarchy; automations; WorkForms — https://support.monday.com/hc/en-us
- Smartsheet Help Center — creating and organizing items; sheets and rows; automated workflows — https://help.smartsheet.com/
- Wrike Help Center — projects; request forms; automation; custom statuses and workflows; approvals — https://help.wrike.com/hc/en-us
- ClickUp Help Center — intro to the hierarchy; task statuses; views — https://help.clickup.com/hc/en-us
- Asana — features overview (product pages) — https://asana.com/features

> Sourcing limitation: Asana's help center is a JavaScript application that could not be fetched from the research environment (two attempts); Asana evidence is limited to its product/feature pages, so no Asana-specific operational details (limits, defaults, plan gating) are stated in this document. Precise numeric limits and plan-specific details for all products are intentionally omitted; they belong to product documentation, not to this Type-level description.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
