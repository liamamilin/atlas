# Capital Improvement Planning

## Overview

A **Capital Improvement Planning** application is a public-sector planning and funding system used to build, adopt, and maintain a **multi-year plan of capital projects** — proposed long-lived physical improvements such as roads, buildings, water and sewer systems, parks, facilities, fleets, and major equipment. Each project carries an estimated cost, a place on a multi-year schedule, and a share of the jurisdiction's constrained capital funding sources (bonds, grants, impact fees, utility rates, reserves). Because capital needs reliably exceed capital funding, the system's central job is to help staff **evaluate, prioritize, and select** projects, and to carry the resulting plan through the jurisdiction's formal adoption process.

The system is the *planning-and-funding* layer. It ends where construction delivery begins and where the annual operating budget begins: it decides which improvements to build, in which years, funded from which sources — not how a single project is built, and not how day-to-day services are budgeted.

## Users & Context

The software is used inside a government organization — cities, counties, towns, special districts and utilities, school districts, and state or regional agencies — by several roles whose relationship to the plan differs:

- **Departments that own needs** (public works/engineering, planning, parks and recreation, utilities, facilities): propose projects, describe justification and scope, provide planning-level cost estimates, and track the status of projects they will eventually execute.
- **Finance / budget office**: consolidates department requests, maintains the funding-source picture, allocates funds across projects and years, analyzes gaps and long-term financial impact, and integrates the plan with the budget process.
- **City manager / executive budget office**: runs the evaluation cycle, weighs priorities, and prepares the recommended plan.
- **Governing body** (council, board, commission): reviews, adopts, and amends the plan — typically through the same public process that adopts the budget.
- **The public** (optional surface): views the plan through published reports, interactive maps, or transparency portals; in some jurisdictions, residents directly express preferences on candidate projects.

The work context is an annual cycle inside a multi-year frame: each budget season, the plan is rolled forward, re-prioritized, refined, and its first year is funded through the adopted capital budget.

## Core Model

The defining core is small and can be read as one structure:

```text
Capital project (proposed improvement — explicitly not routine maintenance)
  ├── cost estimate (planning-level, refined over time)
  ├── scheduled fiscal years (multi-year forward horizon)
  ├── funding allocation (project × funding source × year, often split across sources)
  └── priority (score / rank from evaluation criteria)

Multi-year plan (draft → recommended → adopted → amended)
  └── year 1 funded through the annual capital budget
```

### Capital project

The central record. A project is an identified, discrete improvement to a long-lived physical asset — a street reconstruction, a facility, a utility line, a park, a building system replacement. It typically carries: a name and description, the proposing department, a category and (often) a location or related asset, a justification or need statement, a planning-level cost estimate, phasing or dependencies, and a status. The capital/operating boundary is part of the definition: routine maintenance and operating expenses belong to the operating budget, not here. What qualifies as "capital" (thresholds, asset classes) is defined by each jurisdiction.

### Cost estimate

Every project carries an estimated cost, usually at planning-level precision in early years and refined as a project approaches funding. Estimates are what make comparison, ranking, and funding analysis possible.

### Funding sources and allocations

Capital funding is categorized and finite. Sources commonly include bond proceeds, grants, impact or development fees, utility rates, dedicated capital funds, and reserves; exact categories are jurisdiction-specific. A project's funding is an **allocation**: the link between a project, a funding source, and a year — frequently split across multiple sources and multiple years. Allocations are constrained: planned funding cannot exceed what each source can provide, and projects may sit in an unfunded or partially funded state. This constraint is what makes prioritization the type's central activity.

### Multi-year schedule

Projects are placed in fiscal years across a forward horizon that extends beyond the current adopted budget year. The horizon length varies by jurisdiction; the plan is characteristically longer than a single budget cycle. As each cycle completes, the plan typically rolls forward: a new year is added at the horizon end, and project timing and costs are revised.

### Priority

Projects are evaluated and ranked. Evaluation uses criteria the jurisdiction configures — for example need, safety, asset condition, or community benefit — commonly weighted and combined into a ranked list. The output is a defensible, attributable ranking that supports funding recommendations.

### The plan as a governed artifact

The plan itself is a managed object: assembled as a draft, refined through review, published, formally adopted by the governing body, and subsequently amendable (projects added, deferred, rescoped, re-funded). The adopted plan is the shared reference that the annual capital budget draws from.

### Standard capabilities around the core

Mature products commonly add structure that is not required to recognize the type but makes it work in practice:

- **Request intake** — department-facing forms and workflow for submitting and reviewing project proposals.
- **Scenario planning** — alternative funding strategies and phasing options, long-term financial impact including debt obligations and future maintenance costs of new assets.
- **Capital–operating linkage** — visibility into how the first funded year connects to the annual budget and how new capital assets affect future operating costs.
- **Post-adoption tracking** (in products that span beyond adoption) — monitoring approved projects' status, timelines, and expenditures against allocations across years, with re-prioritization as projects evolve.
- **Publication and transparency** — printable and digital plan documents, interactive charts, and public access to the plan.
- **Reporting and role-based collaboration** — dashboards for executives, elected bodies, and auditors; department/finance/executive roles with different permissions.
- **Integration** — synchronization of projects, funding streams, and budget data with ERP/financial systems.

Some products add **GIS-based mapping**: project locations drawn from spatial data, linked to project and budget details, sometimes published as an interactive public map. Others add **resident engagement surfaces** where the public selects and ranks candidate projects (see Variants).

## How It Works

The canonical workflow runs annually inside the multi-year frame:

```text
1. Collect requests
   departments submit project proposals (need, scope, cost estimate, timing)
2. Evaluate & prioritize
   staff score proposals against weighted criteria → ranked list
3. Build the multi-year plan
   projects scheduled across plan years; phased; dependencies considered;
   scenarios compared (funding strategies, timing, long-term impact)
4. Match funding
   sources allocated to projects by year; splits across sources;
   gaps identified; unfunded projects documented or deferred
5. Publish & adopt
   plan document produced; governing body reviews and adopts
   (amendments recorded thereafter)
6. Fund year 1
   the first scheduled year is appropriated through the annual capital budget;
   operating impacts of new assets feed the operating budget
7. Track & roll forward
   approved projects monitored (status, spend vs allocation);
   each new cycle revises estimates and timing and adds a new horizon year
```

Two of these steps deserve emphasis. **Prioritization under constraint** is the loop that gives the type its purpose: every other capability exists to make the selection defensible — criteria, scores, funding analysis, scenarios, and publication all serve decisions that elected bodies must stand behind. **The roll-forward** is what makes this planning rather than a one-time list: the plan is continuously revised, projects move between funded and unfunded states, and the multi-year frame persists across budget cycles.

Capabilities fall into three natural tiers:

- **Defining core** — project register with cost estimates, funding-source allocation, multi-year scheduling, prioritized selection, governed adoption.
- **Common in mature products** — request intake workflow, weighted scoring, scenario planning, capital–operating linkage, publication, dashboards, ERP integration, and often post-adoption tracking.
- **Optional / variant** — GIS mapping, public engagement and participatory prioritization, grant-seeking depth, asset-condition-driven needs analysis, delivery-stage tracking.

## Interfaces

The main surfaces, described conceptually; exact layouts vary by product.

### Plan workspace

The coordinator's home view.

- Purpose: see and shape the whole multi-year plan.
- Typical information: projects grouped by year, department, category, fund, or status; cost totals per year; funding-source totals vs allocations.
- Primary actions: add/edit projects, move projects between years, adjust allocations, filter and group, compare scenarios.

### Project detail

The working record for one project.

- Purpose: hold everything known about a proposed or adopted improvement.
- Typical information: description, department, category/asset/location, justification, cost estimate and revisions, phasing and dependencies, funding lines by source and year, schedule, status, attached documents, priority score.
- Primary actions: edit details, update estimate or timing, adjust funding lines, change status, view history.

### Request intake

The department-facing submission surface.

- Purpose: gather proposals in a structured, comparable form.
- Typical information: need statement, scope, requested timing, cost estimate, supporting documents.
- Primary actions: submit a request, revise, respond to review comments.

### Evaluation / scoring view

The prioritization surface.

- Purpose: compare candidate projects on consistent criteria.
- Typical information: criteria and weights, per-project scores, computed rankings, reviewer attributions.
- Primary actions: configure criteria, record scores, generate ranked recommendations.

### Funding & scenario view

The financial-analysis surface.

- Purpose: show whether the plan is financially sustainable.
- Typical information: funding sources and capacities, allocations by project and year, gaps and unfunded items, projected long-term impacts (debt service, future maintenance).
- Primary actions: reallocate, split funding across sources, create and compare scenarios.

### Publication / public view

The outward-facing surface.

- Purpose: communicate the plan to elected bodies and the community.
- Typical information: plan document or digital book, summary charts, project summaries, sometimes an interactive map of project locations.
- Primary actions: generate/export the plan, publish updates, browse (public).

### Tracking dashboard

The oversight surface for adopted projects.

- Typical information: project status, timeline progress, expenditures vs allocated funding across years.
- Primary actions: review progress, flag exceptions, adjust funding or priorities.

## Important Rules / Behaviors

- **Capital excludes routine operations.** The register holds long-lived improvements; recurring maintenance and operating costs are deliberately out of scope and belong to the operating budget. Jurisdiction-specific rules define the threshold.
- **Funding is constrained and categorized.** Planned allocations cannot exceed source capacity; projects can be documented as unfunded or partially funded rather than silently over-allocated. Splits across sources and years are normal.
- **The plan is governed.** A draft is not the plan; adoption by the governing authority is the gate that turns it into the working reference. Subsequent changes are amendments, not silent edits.
- **Estimates degrade gracefully.** Cost figures for later years are planning-level and are expected to change; the system tracks revisions rather than treating early estimates as commitments.
- **Projects persist across cycles.** A project is a durable record that moves through proposals, prioritization, funding, and execution — not a line item recreated each year.
- **Attribution matters.** Proposals, scores, recommendations, and amendments are attributable to roles (department, finance, executive, governing body), because the plan must survive public scrutiny and audit.
- **Public-record context.** The plan and its process are public-sector artifacts; transparency and defensibility (documented criteria, decisions, and audit trails) are structural expectations, not add-ons.

## Variants

- **By packaging** — a standalone capital-planning tool; a module inside a broader public budgeting suite; or a planning module that also spans delivery-stage tracking of approved projects.
- **By jurisdiction type** — municipal and county general-government CIPs; special districts and utilities (rate-funded capital programs); school-district facilities plans; state/regional agency programs. Domain changes the project mix and funding sources, not the machinery.
- **By planning driver** — request-driven (departments propose); asset-condition-driven (needs derived from condition assessments of existing infrastructure); or policy/master-plan-driven.
- **Engagement-led variant** — a public-facing surface where residents or stakeholders select and rank candidate projects within a stated budget, producing preference and consensus input. This surface intentionally lacks the funding accounting and adoption machinery of the staff-side plan; it informs the process rather than executing it.
- **Regional vocabulary** — "capital improvement plan" and "capital improvement program" (and equivalents elsewhere) denote the same artifact; downstream budget cadence (annual vs biennial) and source categories differ by jurisdiction.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Public Budgeting Platform | closest sibling; centers on the **annual operating budget** (expense authority by fund and line item, legally adopted each cycle). Capital improvement planning centers on **multi-year projects and their capital funding**; it frequently ships as a module inside budgeting suites. The removal test: take away the multi-year project/funding-source structure and only annual budgeting remains. |
| Construction Project Management / Project Controls | manages **delivery of an individual approved project** (schedule, procurement, change orders, field operations). Capital improvement planning selects, prioritizes, and funds the **portfolio**; its execution visibility normally stops at status and spend. |
| Public Asset Management / EAM | holds the condition and maintenance of **existing** assets. Its condition data feeds capital needs, but maintenance operations are operating activity, not capital investment decisions. |
| Government Grants Management | grants appear inside capital planning as **funding sources**; the grant lifecycle (discovery, application, compliance, reporting) is a separate type. |
| Public Works Management | operational management of work orders and routine maintenance — outside the capital boundary by definition. |
| Government GIS | spatial infrastructure and mapping; in capital planning it is a presentation/data layer (project locations), not the plan machinery. |
| Government Performance Management | measures service performance against goals; capital improvement planning allocates investment under funding constraints. Scoring overlaps in form, purpose differs. |

The boundary with the operating budget is the sharpest one to hold in practice, because capital and operating planning share the budget calendar, the finance office, and often the same software suite. The structural difference is durable: operating budgeting authorizes spending by fund and category for one cycle; capital improvement planning commits long-lived improvements across multiple years and ties each to named funding sources.

## Representative Products

- **Euna Budget — Capital Budgeting** (Euna Solutions; successor to Questica's budgeting line) — CIP as a module of a public-sector budgeting suite: weighted-criteria prioritization, multi-year plan building, funding allocation, scenario planning, capital–operating linkage, GIS mapping, digital CIP publication, and post-adoption spending oversight.
- **Balancing Act — Prioritize** (Engaged Public) — the public-engagement surface: residents and stakeholders select and rank budgeted projects within a fixed budget, producing weighted preference and consensus data that feeds staff-side decisions.

Other widely used capital-planning and budgeting vendors exist in the local-government market (e.g., OpenGov, ClearGov); their product documentation could not be verified during this research (see Sources) and no claims about them are made here.

## Sources

Research date: **2026-09-06**

- Euna Solutions — Budget (suite overview): https://eunasolutions.com/solutions/budget/
- Euna Solutions — Capital Budgeting (module page, including PLAN/BUILD/MANAGE workflow and FAQ): https://eunasolutions.com/solutions/budget/capital-budgeting/
- Balancing Act — homepage: https://www.abalancingact.com/
- Balancing Act — Prioritize: https://abalancingact.com/solutions/prioritize
- MRSC (Municipal Research and Services Center of Washington) — Finance & Budgeting topic pages (budget as legal authority to expend funds; annual/biennial adoption cadence): https://mrsc.org/explore-topics/finance , https://mrsc.org/explore-topics/finance/budgets/budgeting-contents

> Sourcing limitation: vendor help centers and several reference sources (including OpenGov and ClearGov product sites, GFOA best-practice material, and general-reference articles) were not reachable from the research environment on 2026-09-06 (access denied or timeouts). Product observations therefore rest on official product pages, and this document deliberately states no precise operational figures (plan-horizon lengths, cost thresholds, scoring scales, or default settings); such specifics vary by jurisdiction and product.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
