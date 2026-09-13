# Research Project Management

## Overview

A **Research Project Management** application is the team-side coordination system for research work. It organizes a body of research work into **projects**, breaks that work into **research work items** — experiments, studies, analyses, and tasks — and manages those items through a coordination loop: planning and assignment, execution and recording, tracking of status and schedules, progress review, and reporting.

The defining core is small:

```text
Research project (container of record)
└── Research work items (experiments / studies / tasks)
    ├── research content: procedure, results, linked samples & materials
    └── coordination state: assignees, status, due dates
└── Coordination loop (plan → assign → execute & record → track → review → report)
```

Three properties hold together. Remove the research-shaped work items — keep only projects and generic to-dos — and the product is an ordinary project management tool. Remove the coordination loop — keep only the documented record — and the product is an electronic lab notebook or documentation space. Remove the project container — and the product is a loose task list with no project memory.

Everything else commonly associated with the category — progress dashboards, cross-team request handling, protocol template libraries, inventory and sample linkage, compliance machinery — is standard equipment of mature products or a segment-dependent addition, not what makes the product a research project management tool.

## Users & Context

The primary users are the members of a research team that carries out a body of work over months or years:

- **principal investigator / lab head** — owns the project portfolio, oversees progress across projects and collaborators, intervenes on blockers
- **project lead / coordinator** — plans timelines and resources; balances assignments; keeps the project moving
- **researchers** (postdocs, PhD students, research scientists) — execute the work items, record procedure and results, update status
- **lab / operations manager** — monitors parallel workflows, capacity, and materials
- **QA / compliance personnel** (regulated organizations) — verify documentation completeness and approvals

Secondary participants include internal colleagues from other teams and external collaborators, who are typically brought in through sharing or request mechanisms rather than full membership.

Typical settings: academic laboratories, biotech and pharmaceutical R&D, contract research organizations, diagnostics and industrial research labs. The coordination structure itself is domain-neutral — the same loop organizes wet-lab studies, data analyses, and observational campaigns — although the market's center of gravity is laboratory-based research, where work items carry protocols and physical materials.

## Core Model

### The research project

The project is the container of record. It is a persistent, named entity that outlives individual experiments and holds:

- the work content of the research effort (its aims or plan, expressed through the work items it contains)
- its team — members with roles and access rights, plus collaborators with narrower sharing
- its progress over time — what has been completed, what is active, what is stalled

Projects are commonly organized into folders, carry project-level permissions that decide who can see and edit the work, and are archived rather than deleted when they end, preserving the record. In mature products the project is also the unit from which reports are generated.

### Research work items

Inside a project, work is organized as research-shaped items — most commonly a hierarchy of **experiments** (or studies) containing **tasks**. What makes these items research-shaped, rather than generic to-dos, is their content:

- **procedure** — work items are typically instantiated from protocol or procedure templates and carry ordered steps that are checked off as the work proceeds
- **results** — observations, data files, and structured records attached to the item, retained as part of the project's documentation
- **research linkages** — connections to the materials and context of the work: samples, reagents and inventory items (with usage recorded against the task), instruments, and related data

Each item carries its coordination state: one or more **assignees**, a **status** drawn from the product's task workflow (commonly including not-started, in-progress, and completed-like terminal states, with the exact labels varying by product), and usually a **due date**. Items can be commented on, tagged, moved between experiments or projects, and archived.

### The coordination loop

The management layer is the loop that keeps the work items moving. It is what distinguishes a research project management tool from a documentation space: the system continuously answers *what is moving, what is stuck, who is loaded, and what is next* — through status and due-date tracking, workload views, and progress dashboards.

### Supporting structures

- **Protocol / procedure templates** — shared, versioned templates from which work items are instantiated; keep the team's methods standardized and repeatable
- **Inventory / samples** — the materials substrate; usage is commonly recorded per task, connecting the coordination layer to the physical lab
- **Requests** — structured work requests raised by one team or person and fulfilled by another; the request becomes a tracked work item in the executing team's queue
- **Reports** — project-level summaries of what was done, when, by whom, and with which results

```text
Protocol templates ──instantiated into──▶ Work items (experiments → tasks)
                                            │  assignees · status · due dates
Inventory / samples ──consumed/linked by──▶ │
                                            ▼
                              Research project (container of record)
                                            │
                              coordination loop: plan → assign → execute
                              → track → review → report
```

## How It Works

### Set up the project

```text
Create project (often inside a folder structure)
→ add team members and set access
→ structure the work: experiments / studies, optionally from templates
```

There is no institutional award setup and no sponsor configuration here — the project is the team's working container, not a funding instrument.

### Plan and assign work

```text
Create experiments / tasks (frequently from protocol templates)
→ assign each item to one or more team members
→ set due dates and, where used, milestone targets
→ order dependent work
```

Assignment is the act that turns a documented plan into managed work: the assignee sees their items, and the project lead sees the distribution.

### Execute and record

```text
Assignee opens the work item
→ follows / checks off protocol steps
→ records results and attaches data
→ consumes linked materials (usage recorded against the task)
→ updates status as the work progresses
```

Execution and documentation happen in the same object: the coordination state (status, dates) and the research record (steps, results, materials) live on the same work item. This is why research project management products usually include notebook-like documentation rather than integrating with one — the record is the residue of the managed work.

### Track and review

```text
Project lead / PI opens the progress dashboard
→ sees status distribution across tasks and experiments
→ sees workload per person, overdue and upcoming due dates
→ sees stalled work (items not updated recently)
→ drills into a filtered list and reassigns or follows up
```

The dashboard is the characteristic management surface of this Application Type. Its typical widgets — status overview, workload distribution, due/overdue tracking, and stall detection — are the operational answer to "what needs my attention".

### Coordinate across teams

```text
Requester submits a structured work request
→ the request becomes a tracked item in the fulfilling team's queue
→ fulfillment is executed and recorded like any other work item
→ requester sees status
```

This is how core facilities, service labs, and cross-functional R&D organizations run work through the same coordination model.

### Report

```text
Generate a project report
→ what was done, when, how, by whom, which results
→ share with stakeholders (management, sponsors, collaborators, QA)
```

### Capability tiers

**Defining core** — without these, it is not research project management:

- research project as persistent container with team and access control
- research-shaped work items carrying procedure, results, and material linkages
- the coordination loop: assignment, status and schedule tracking, progress review

**Standard capabilities of mature products**:

- progress dashboard (status, workload, due dates, stalled work)
- protocol / procedure template libraries
- inventory / sample linkage with usage recording
- cross-team work requests
- project reporting and export
- comments, notifications, tags, activity history
- role differentiation (PI, project lead, researcher, lab manager)

**Optional / segment-dependent**:

- compliance machinery (electronic signatures, audit trails, regulated-environment packaging)
- automation of recurring workflows
- equipment / instrument scheduling
- mobile execution in the lab
- AI assistance (template import, data query)

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Project list / workspace home

The entry surface listing the user's projects (and project folders), with recent activity and shortcuts to create new work.

- typical information: project names, folders, activity, favorites
- primary actions: open a project, create a project, search

### Project detail

The project's interior: its experiments/studies, their tasks, and the project's team.

- typical information: work item tree or table, statuses, assignees, due dates
- primary actions: create experiment/task, assign, move or archive items, manage members and sharing

### Work item view

The experiment or task surface where execution happens.

- typical information: protocol steps, results and attachments, linked materials, comments, status, assignees, due date, activity history
- primary actions: check off steps, add results, assign materials, update status, comment

### Progress dashboard

The management surface aggregating coordination state across one or more projects.

- typical information: status distribution, workload per person, due/overdue items, stalled items
- primary actions: filter, drill into a task list, reassign, follow up

### Requests surface

Where cross-team work is requested and fulfilled.

- typical information: request forms, request status, fulfilling assignments
- primary actions: submit a request, prioritize, schedule, fulfill, update status

### Reports

Project-level document generation and export.

### Settings / permissions

Team, roles, project-level access, template and workflow configuration.

## Important Rules / Behaviors

### Work items live inside projects

Experiments and tasks belong to a project; they can be moved between containers but not left floating. Archiving a project typically requires its contents to be dealt with first — the record is preserved, not discarded.

### Status follows a workflow

Work items move through a defined set of states, and many products let an organization configure its own task workflow. Completed items reach a terminal state; terminal items are typically locked against casual editing, protecting the record while allowing controlled correction.

### Access is project-scoped

Visibility and editing rights are granted primarily at the project level; a person's access to a work item derives from their access to its project. External collaborators receive narrower, explicitly granted sharing.

### Coordination state is user-visible and actionable

Due dates, overdue items, and stalled work are surfaced to the people responsible for keeping the project moving — this visibility is the product's management function, not a reporting afterthought.

### Documentation is retained

The coordination loop never destroys the research record: results, protocol steps, material usage, and activity history persist on the work item. In regulated settings this retention is formalized with signatures and audit trails; in all settings it is what makes the project report trustworthy.

### Templates standardize execution

Work instantiated from a protocol template inherits its structure; template versioning governs how updates propagate to future work without rewriting the historical record.

## Variants

- **ELN-integrated platforms** — the dominant shape: coordination and experiment documentation in one product, so the work item is simultaneously the management object and the record
- **Enterprise process-formal platforms** — heavily schema-driven work items, formal request management, and validated environments for large, multi-team R&D organizations
- **Academic / free tiers** — the same core model offered at low or no cost for individual labs and students, usually with thinner compliance and automation
- **Regulated-segment packaging** — the core model plus GxP-style compliance machinery for pharma, CRO, and diagnostics customers
- **Service-lab flavor** — coordination centered on incoming requests from internal or external clients, with fulfillment tracked like any other work
- **Domain flavors** — wet-lab life sciences dominate the market realization (protocol steps, reagents, samples), but the defining structure applies equally to computational, observational, and social research; the wet-lab vocabulary is an implementation, not the definition

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Project Management Application | closest structural neighbor | generic PM coordinates projects and generic tasks; here the work items are research-shaped — carrying procedure, results, and material linkages — and bind to the research record |
| Electronic Lab Notebook / ELN | sibling, heavily overlapping in products | the ELN's primary job is documenting experiments; the coordination loop (assignment, workload, due dates, dashboards, requests) is the research project management layer. Documentation-first products with little coordination are ELNs even when they organize by project |
| Research Grant Management / Research Administration Platform | institutional neighbor | those systems are the institution's side of research money — proposals, awards, sponsor compliance; this Type is the team's side of research work. The funded project may be the reason a research project exists, but award administration is a different system with different actors |
| Research Information Management / CRIS | institutional record neighbor | CRIS holds the institution's attributed picture of its research activity and outputs; this Type manages the live work that produces those outputs |
| Research Data Management | adjacent | RDM stewards and publishes data (FAIR organization, repositories, identifiers); this Type coordinates the work that generates data. Mature platforms bundle both |
| Research LIMS | adjacent | LIMS is sample-centric lab operations — sample workflows, chain of custody; here the project and its work items are the unit of record, with samples as linked materials |
| Clinical Trial Management System / CTMS | regulated cousin | clinical trials coordinate subject-facing, regulator-facing study machinery with its own object model; research project management serves the broader research team |
| Professional Services Automation | structural analog | PSA runs the same coordination loop over billable client work; the economics and work content differ from research work |

The two most important boundaries: against **generic project management** (the seam is the research-shaped work item) and against the **ELN** (the seam is coordination versus documentation). Because most research platforms bundle both, the practical test is the product's primary job, not the presence of individual features.

## Representative Products

- **SciNote** — ELN-rooted platform with an explicit scientific project management layer (projects / experiments / tasks, configurable task workflows, progress dashboard); academic and industry labs
- **Labguru** — lab management platform combining ELN, LIMS, and inventory with project/task coordination and request handling; biotech and pharma
- **Benchling** — enterprise R&D cloud whose coordination layer is workflow- and request-based task management over a shared notebook and registry; large biopharma R&D organizations

The boundary poles examined to fix the Type's edges: LabArchives (documentation-first academic ELN) and RSpace (FAIR research data management platform) — both organize research but are not primarily coordination systems.

## Sources

Research date: **2026-09-09**

- SciNote — https://www.scinote.net/ · https://www.scinote.net/product/scientific-project-management/ · https://knowledgebase.scinote.net/en/knowledge/what-are-project-insights-in-scinote · https://knowledgebase.scinote.net/en/knowledge/using-scinote
- Labguru — https://www.labguru.com/ · https://www.labguru.com/eln
- Benchling — https://www.benchling.com/ · https://www.benchling.com/bioresearch · https://help.benchling.com/hc/en-us (Task Management / Workflows / Requests sections)
- LabArchives — https://www.labarchives.com/
- RSpace — https://www.researchspace.com/

> Sourcing limitations: Labguru's support center and Benchling's individual help-center article pages were not reachable from the research environment on 2026-09-09; claims resting on those surfaces are kept correspondingly weaker, and precise operational details (exact status labels, numeric thresholds, plan restrictions) are intentionally not stated. The open-source academic pole (eLabFTW) was unreachable and is under-represented. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
