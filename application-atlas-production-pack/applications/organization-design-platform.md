# Organization Design Platform

## Overview

An **Organization Design Platform** is a workspace in which an organization is held as structured data — units, positions, people, and reporting relationships — so that designers of the organization can study the structure as it is today, build alternative future structures against it, compare those alternatives through measurable impact, and hand the chosen structure off toward implementation.

The defining core is small:

```text
Organization structure as structured data
└── current-state baseline
    └── alternative future-state structures (scenarios) derived from it
        └── comparison of states through measurable impact
            └── handoff of the chosen structure toward implementation
```

What makes this a distinct type of application rather than a drawing tool is that the chart is *data*: every box is a record with attributes, cost, and occupancy, and every proposed change is a modification of records that can be measured. What makes it distinct from ordinary org-chart software is the scenario loop: the ability to propose a reorganization in an isolated copy of the structure, evaluate it, and only then apply it.

## Users & Context

Primary users are the people whose job is to shape the organization:

- **HR / organization-design practitioners** — build and analyze structure models, run reorganization scenarios, prepare decision materials
- **HR business partners** — collaborate inside scenarios for their part of the organization
- **Transformation / restructuring teams** — run large structural programs (cost reduction, post-merger integration, operating-model change)

Secondary users:

- **Executives** — review and compare proposed structures, approve changes
- **Finance partners** — align structural scenarios with budgets and cost targets
- **Line managers** — in some products, propose adjustments to their own team structures

Typical occasions for use: restructures and reorganizations, workforce expansion or reduction, mergers and acquisitions, annual planning cycles, a new executive reshaping their organization, and continuous monitoring of structural health (spans, layers, vacancies). The work is episodic but recurring: a redesign may run for weeks as a project, then the platform returns to monitoring until the next change.

## Core Model

### The defining core

**Organization structure as data.** The platform's world is a model of the organization: organizational units (company, departments, teams, groups), positions (jobs), people (employees), and the reporting relationships between them. The model is queryable — headcount, cost, and attributes can be aggregated over any subtree — which is what separates it from a static diagram.

**Current state and future states.** The model is instantiated as the *current* organization — the baseline that reflects today's structure, usually kept in step with the HR system of record. From that baseline, users derive *scenarios*: isolated copies of the structure in which proposed changes live — new positions, moves, promotions, backfills, terminations, re-parenting of teams. A scenario is a sandbox: its changes are visible only to its owners and invited collaborators and have no effect on the baseline until explicitly applied.

**Impact comparison.** Because both the baseline and every scenario are data, the platform can compute what each proposed structure would mean: total headcount, open positions, compensation cost (often shown as annualized run-rate or prorated over fiscal periods), and structural-health measures such as span of control and number of layers. Comparing scenarios side by side against these measures — and often against a budget — is the act of "designing" the organization in this software.

**Handoff toward implementation.** A scenario that survives review is applied in some form: merged into the platform's primary structure, written back to the HR/HCM system of record, or exported as a change plan (new-hire requests, position changes) for execution in other systems.

### Objects inside the model

- **Position** — a job slot in the structure. Positions exist independently of people: a position can be vacant (an open job to be hired), occupied by one person, or — flagged as a defect — associated with multiple people or left unassigned. This position/person separation is what lets a scenario add a role before anyone is hired.
- **Person** — an employee record, usually synchronized from the HR system, with attributes (department, location, level, compensation) that feed both the chart and the metrics.
- **Reporting line** — the primary manager relationship that gives the structure its shape. Some products also support secondary relationships (dotted-line / matrix reporting) and groupings that sit outside the reporting tree (functions, cohorts).
- **Scenario** — the future-state container described above, with its own access control and lifecycle.
- **Change items** — the individual differences between a scenario and the baseline (a hire, a move, a termination), which can be listed, delegated, and tracked as a change plan.
- **Metrics** — computed aggregates over any part of the structure: headcount, FTE, vacancies, compensation cost, span of control, layers, gaps and overlaps.

### Concept vs implementation

The core is conceptual, and products implement it differently:

```text
Concept:   structure baseline kept current
Implementations:  live HRIS sync, scheduled integration, periodic file import

Concept:   applying an approved scenario
Implementations:  merge into the platform's primary chart,
                  write-back into the HCM/ERP system of record,
                  export of change plans and hiring requests

Concept:   structural-health measurement
Implementations:  built-in span/layers/vacancy indicators,
                  configurable dashboards, custom formulas
```

## How It Works

The typical lifecycle of organization design work in such a platform:

```text
Connect workforce data (HRIS integration or import)
→ build / verify the current-state structure
→ create a scenario (isolated copy of the structure)
→ edit the future structure (move teams, add or remove positions,
   change reporting lines, mark terminations, plan backfills)
→ observe impact (headcount, cost, spans, layers, budget fit)
→ compare scenarios and iterate
→ share for review / approval
→ apply: merge, write back, or export a change plan
→ track the transition (vacancies filled, position changes executed)
→ monitor the new baseline; repeat when the next change comes
```

Two loops run in parallel. The **design loop** (scenario → impact → compare → approve → apply) is the defining activity. The **monitoring loop** (current structure → health metrics → identify spans/layers/vacancy problems → new scenario) is what turns the platform from a project tool into a standing system of structural insight.

Scenario isolation is the pivotal mechanic: while a reorganization is being explored, the live organization keeps running; the proposed one exists only inside its scenario. Only after review — and, where configured, formal approval — do the changes become official, at which point the platform's baseline and (in integration-coupled products) the HR system of record are updated together.

## Interfaces

### Org chart canvas

The primary surface. An interactive rendering of the reporting hierarchy with people and position cards.

- typical information: names, titles, departments, locations, open jobs, aggregate headcount/cost per subtree
- primary actions: navigate and zoom, search people/jobs/groups, filter or color-code by attribute, inspect a person or position, view the structure at a past or future date
- in a scenario, the same canvas becomes the editing surface: drag a subtree to a new manager, add or delete positions, change attributes

### Scenario list

The entry point to the design loop.

- typical information: scenario name, owner, review status, cost summary
- primary actions: create a scenario, open a shared one, filter by owner or status

### Data sheet / forecast sheet

A tabular view over the same records the chart shows.

- typical information: people and positions as rows, attributes and cost as columns; forecast views add budget lines and period-based cost
- primary actions: bulk edit, filter, compare cost between scenarios, export

### Dashboards and reports

- typical information: span-of-control and layer distributions, vacancy and gap summaries, cost by department or region, scenario-vs-baseline comparisons
- primary actions: configure views, share or export for decision meetings

### Review and approval surfaces

- typical information: what changed in the scenario, who proposed it, approval state
- primary actions: comment, request changes, approve or reject, apply the scenario

### Administration / integration settings

- data-source connections, field mapping, permission configuration, sensitive-data controls (compensation visibility)

## Important Rules / Behaviors

- **Scenario isolation.** Changes inside a scenario do not affect the primary structure and are invisible to the wider organization until the scenario is applied. This is the rule that makes exploratory reorganization safe.
- **Approval gates.** Depending on configuration, a scenario must pass review and approval before its changes can become official. Scenario records carry a visible lifecycle (being edited → in review → approved/rejected → applied).
- **System-of-record precedence.** Where the platform syncs with an HR system, the sync can overwrite platform-side changes; applying a scenario and updating the source system need to be coordinated, and at least one product warns users about this conflict explicitly.
- **Sensitive-data control.** Compensation is treated as sensitive: visibility is permission-controlled, and some products exclude it from shared links and exports by default.
- **Position integrity.** The model distinguishes positions from the people in them; unassigned people, vacant positions, and positions with multiple occupants are structural defects, and some products surface them explicitly for resolution during design.
- **Cost semantics.** Scenario cost is typically shown as an annualized run-rate, with prorated fiscal-period views; products treat these as planning figures, not full forecasts of future payroll.
- **Permission-scoped visibility.** What a user sees on the chart and in metrics depends on their role and scope (for example, an HR partner may see only their part of the organization).

## Variants

- **Strategic vs operational design.** Some products split the experience: a strategic tier for central HR/finance teams running organization-wide redesigns, and an operational tier letting line managers propose and get approval for team-level changes.
- **Position-level vs aggregate modeling.** Position-level modeling captures every reporting line and cost; high-level modeling works over functions, job families, or grades when full position data is unavailable or speed matters more than granularity.
- **Implementation coupling.** Deeply coupled products write approved structures back into the HCM/ERP system of record; loosely coupled products merge internally or export change plans for execution elsewhere.
- **Bundled breadth.** Some platforms are focused design tools; others bundle headcount planning, compensation, job architecture, skills analysis, or broader workforce-transformation analytics around the same structural model.
- **Delivery posture.** Self-serve SaaS for people-ops teams and consultants versus enterprise deployments accompanied by professional services and transformation programs.
- **AI assistance.** An emerging layer: scenario drafting, role clustering, and question-answering over the structure. Present in current products but not required by the type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Org Chart Management | closest sibling | maintains and publishes the *current* structure as a record; lacks the scenario/impact loop that defines design. Vendors in this market ship the two as separate products, though some platforms bundle both |
| Workforce Planning Platform | overlapping sibling | centers on demand/supply of headcount over a time horizon; org design centers on structure and compares proposed structures. Metrics (headcount, cost) overlap; the scenario-of-structure loop does not |
| HRIS / HCM | upstream system | system of record for employee data; the design platform consumes it and may write approved structures back. An HRIS has no scenario sandbox for structure |
| People Analytics Platform | adjacent | answers analytical questions about the workforce; shares metrics (spans, layers, cost) but does not model and apply alternative structures |
| Diagramming Application | superficially similar | draws org charts as shapes; holds no position records, no occupancy, no cost, no scenario lifecycle |
| Succession Planning Platform | adjacent talent process | works on coverage of critical roles by candidates; org design works on the shape of the structure itself |

The most important boundary is with **Org Chart Management**: both hold the same structural model, and modern products increasingly bundle both. The working test is the scenario loop — remove the ability to propose, measure, and apply alternative structures, and what remains is chart management, not organization design.

## Representative Products

- **ChartHop** — people-ops platform with the org chart at its center; scenarios with merge-to-primary and headcount planning (mid-market)
- **Nakisa Org Design Suite** — enterprise org design with strategic and operational tiers and write-back into major HCM/ERP systems
- **OrgVue** — workforce-transformation platform for large structural programs; position-level and high-level modeling
- **Functionly** — self-serve interactive org design with scenarios, forecasts, and change plans for operational leaders and consultants

## Sources

Research date: **2026-09-06**

- ChartHop Help Center — Scenarios; Org Chart; Planning; Getting around in ChartHop — https://docs.charthop.com/scenarios , https://docs.charthop.com/org-chart , https://docs.charthop.com/planning , https://docs.charthop.com/getting-around-in-charthop
- ChartHop product site — https://www.charthop.com/
- Nakisa Org Design Suite product page — https://nakisa.com/products/org-design-software/
- OrgVue — Organization modeling; Platform overview — https://www.orgvue.com/solutions/organization-modeling/ , https://www.orgvue.com/
- Functionly — Scenarios, Forecasts, Change Planning; product site — https://www.functionly.com/features/scenarios-forecasts-change-planning , https://www.functionly.com/

> Sourcing limitation: one vendor's in-product documentation portal (Nakisa docs) was not reachable in depth during research; that vendor's workflow details come from its official product page and are stated with reduced precision. Precise numeric limits, pricing-tier gating, and permission specifics were not systematically researched and are intentionally not asserted in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
