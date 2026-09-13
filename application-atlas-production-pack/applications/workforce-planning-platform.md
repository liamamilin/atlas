# Workforce Planning Platform

## Overview

A **Workforce Planning Platform** enables an organization to plan its future workforce as a managed, time-phased object: it takes the current workforce as a baseline, expresses future demand from business goals, projects how today's workforce will evolve on its own, quantifies the gaps between demand and supply, and models scenarios and actions — hiring, contracting, automation, upskilling, restructuring, retention — to close those gaps, then tracks the chosen plan against actuals as reality unfolds.

The defining structure is small:

```text
Current-workforce baseline (from HR/payroll records)
└── Workforce plan across a future horizon (people by segment, per period)
    ├── Demand — workforce required by business goals and drivers
    ├── Supply — how the present workforce projects forward (attrition, movement, retirement)
    ├── Gap — demand vs supply, per segment and period
    ├── Scenarios / actions — modeled ways to close the gap
    └── Tracking — the selected plan continuously reconciled against actuals
```

Everything else commonly associated with the category — compensation and cost modeling, skills and competency layers, predictive forecasting, approval workflows, AI assistance, write-back into HR or finance systems — is widely supported by mature products but is not what makes the product a workforce planning platform. A maintained spreadsheet of headcount by department, projected needs by year, attrition assumptions, gaps, and alternative staffing options — the way workforce planning was done for decades before this software existed — satisfies the same structure.

When the dominant surface shifts to describing and measuring the workforce as it is or was, the product is drifting toward People Analytics; when it shifts to authoring and comparing alternative organizational structures, toward Organization Design; when it shifts to scheduling shifts and capturing worked time, toward Workforce Management.

## Users & Context

Primary users:

- **HR / workforce planning leads and analysts** — own the planning process, build and maintain plans, run scenarios, and report on gaps
- **Finance / FP&A partners** — consume the cost side of plans and reconcile them with budgets; in some organizations they co-own headcount planning
- **Business and line leaders** — own the demand side for their units, contribute to plans delegated to them, and approve headcount targets

Secondary users:

- **Executives** — review scenarios and trade-offs, and set the strategic direction the plans must serve
- **HR business partners and recruiting/talent leaders** — receive approved plans as targets for hiring and talent actions

Typical contexts: annual budgeting cycles with periodic re-forecasts; multi-year strategic planning exercises; and event-driven replans triggered by growth targets, restructurings, cost-reduction programs, M&A, digitalization or automation initiatives, and anticipated retirements or talent shortages. The work is inherently cross-functional — HR, Finance, and business units plan against a shared workforce picture, which is why collaboration and delegation are structural features rather than conveniences.

## Core Model

### The Workforce Plan

The center of the system is the **plan**: a persistent, structured, editable model of the organization's future workforce across a defined time horizon (one or more years, or rolling quarters). A plan is segmented — by organizational unit, role or job family, location, grade, or skill — and carried period by period. Plans are versioned and revisable; they accumulate an authoring history and remain distinct from one-off analyses. The plan is the system's object of record: what it means for the platform to exist is that the organization's intended future workforce is held here, not in scattered spreadsheets.

### The Baseline (Supply Anchor)

Every plan starts from the **current workforce**: actual headcount, positions, roles, and — in mature products — compensation and cost, drawn from HR, payroll, ERP, or finance systems through integration or structured import. The baseline is not a one-time snapshot; mature products keep reconciling the plan against actuals as hires, exits, and moves accumulate. This anchor is what makes the plan about a real workforce rather than an abstract scenario.

### Demand

**Demand** is the workforce the business will need: expressed as targets or as driver-based assumptions — revenue growth, expansion into new locations or markets, new capabilities required by strategy, efficiency or automation goals. Demand is stated in the plan's own units: people of particular kinds, in particular places, at particular times. The same business driver can be translated into different demand profiles, which is precisely what scenarios explore.

### Supply Projection

**Supply** is how the present workforce evolves if the organization does nothing new: attrition and turnover rates, retirements, internal transfers and promotions, retention programs. Supply projection answers the question "what will my workforce look like in one, three, or five years by itself?" — the counterfactual against which demand is compared.

### Gap

The **gap** is the computed difference between demand and projected supply, per segment and per period — for example, surpluses and shortages by role cluster across quarters. The gap view is the planning conversation's focal point: it turns strategy statements into concrete workforce quantities that must be sourced, built, reduced, or redirected.

### Scenarios and Actions

To close gaps, the platform models **scenarios**: alternative futures and action sets applied to the baseline and compared against each other. The action vocabulary recurs across products — recruit externally, engage contractors, automate or redesign work, upskill and retrain existing employees, reduce or transition roles, retain critical talent — combined in different proportions per scenario. A scenario isolates its changes from the live baseline until it is selected; comparing scenarios side by side, with their headcount, cost, and capability consequences, is how the organization chooses its plan.

### Workforce Economics

Plans are expressed in two currencies: **people** (headcount, FTE, positions) and **cost** (compensation, position budgets). The cost view is the bridge to Finance — it lets headcount plans and financial budgets be negotiated on one picture. Cost modeling is near-universal in current products, but a plan expressed purely in headcount still satisfies the Type; the subject of the plan is people, with cost as its economic shadow.

### Actuals and Tracking

The selected plan is continuously compared with **actuals** as they accumulate from the same HR systems that fed the baseline: planned versus actual headcount and cost by unit, off-plan departments, hiring progress against plan. Divergence triggers re-forecasting and re-planning — which is why mature products treat planning as a continuous cycle rather than an annual event.

### One Structure, Many Implementations

```text
Concept:      Baseline        Implementations:  HRIS/payroll/ERP integration, structured import, manual load
Concept:      Segmentation    Implementations:  org units, job families, roles, locations, grades, skills
Concept:      Demand          Implementations:  driver-based assumptions, target-setting, finance-goal linkage
Concept:      Supply dynamics Implementations:  attrition-rate assumptions, retirement models, movement flows
Concept:      Scenario        Implementations:  sandboxed plan copies, what-if adjustments, AI-generated options
Concept:      Handoff         Implementations:  approved hiring plans into HCM, cost plans into finance systems,
                                                 structure changes into org-design or org-chart systems
```

A reader who has only seen one implementation (for example, driver-based headcount planning inside a finance suite) should be able to recognize the others — multi-year strategic planning on an analytics platform, or drag-and-drop position modeling on an org-transformation platform — as the same Type.

## How It Works

The defining workflow is a loop:

```text
Establish the baseline
→ express demand (business goals, drivers, targets)
→ project supply (attrition, retirement, movement)
→ see the gap (demand vs supply per segment, per period)
→ model scenarios and actions to close it
→ compare, select, and approve a plan
→ track the plan against actuals
→ re-plan as conditions change
```

**Establish the baseline.** Workforce data is brought in from HR, payroll, and finance systems and organized into the plan's segmentation — roles or job families, units, locations. Open positions, vacancies, and costs are part of this picture: the baseline includes positions that exist but are not yet filled.

**Express demand.** Leaders translate business direction into required workforce: growth targets become new roles in expanding units; efficiency goals become reductions or automation; new capabilities become skill requirements. Demand may be entered as targets, generated from driver assumptions, or imported from financial plans.

**Project supply.** Assumptions about attrition, retirement, movement, and retention are applied to the baseline across the horizon, producing the "do nothing" future for each segment.

**See the gap.** The platform computes and displays where demand exceeds supply (shortages to source or build) and where supply exceeds demand (surpluses to redeploy or reduce), period by period.

**Model scenarios.** Users construct alternatives — combinations of hiring, contracting, automation, upskilling, restructuring, and retention — and the platform computes each one's consequences on headcount, cost, and capability across the horizon. Scenarios are worked in isolation from the live plan, then compared.

**Select and hand off.** A scenario is chosen (often through review and approval), becoming the plan of record. Approved plans then move outward: hiring targets toward recruiting and HCM systems, cost plans toward finance, structural changes toward org-design or org-chart processes.

**Track and re-plan.** Actuals flow in continuously; the plan is marked up against them; and when the business or the labor market shifts, the cycle runs again from the refreshed baseline.

### Core vs Standard vs Optional

**Defining core** — without these, not a workforce planning platform:

- a persistent, time-phased workforce plan as the object of record
- a current-workforce baseline from real workforce records, reconciled against actuals
- the demand → supply → gap → action loop over the horizon

**Standard capabilities** — present in most mature products:

- cost and compensation modeling alongside headcount (the HR–Finance bridge)
- HRIS/payroll/ERP/finance integrations feeding baseline and actuals
- skills and competency dimensions on supply and demand
- approval workflows, delegation of plan portions, role-based access
- dashboards and reports: gap views, plan-vs-actual views
- multi-cycle plan management (annual plan, re-forecasts)

**Optional / variant** — depends on product philosophy and customer:

- predictive or AI-assisted forecasting of attrition and future workforce state
- skills-ontology-based strategic planning (skills as the primary planning unit)
- org-structure authoring inside planning scenarios (the org-design overlap)
- write-back into HCM/ERP/finance systems rather than export-based handoff
- consulting-led transformation delivery versus self-serve operation

## Interfaces

Surfaces described conceptually; exact layouts and names vary by product.

### Plan workspace

The primary authoring surface — a sheet- or table-like model of the workforce by segment and period, with driver assumptions and editable targets.

- typical information: segments (roles/units/locations) as rows, periods as columns, headcount/FTE/cost values, driver assumptions
- primary actions: set targets, adjust drivers, enter assumptions, copy a cycle, create a plan version

### Gap view

The demand-versus-supply comparison surface.

- typical information: supply, demand, and gap per segment per period, often as bar or bridge charts; largest gaps highlighted
- primary actions: filter to segments, drill into a gap, launch a scenario or action to address it

### Scenario comparison

The surface where alternative futures are compared.

- typical information: side-by-side scenario totals (headcount, cost, capability mix), differences from the baseline
- primary actions: create/duplicate a scenario, apply actions, compare, submit for review, select

### Current-state dashboard

The baseline assessment surface over today's workforce.

- typical information: headcount, FTE, cost, composition, and structure distributions; trends
- primary actions: segment, filter, export, use as planning starting point

### Plan-vs-actual tracking

The monitoring surface for the selected plan.

- typical information: planned versus actual headcount and cost by unit; hiring progress; off-plan flags
- primary actions: review variances, adjust the plan or forecast, trigger re-plan

### Collaboration and administration

Sharing, delegation, and governance surfaces: assign plan portions to contributing teams, review and approve submissions, configure drivers, data integrations, and permissions.

## Important Rules / Behaviors

### The plan is anchored to reality and reconciled continuously

A plan detached from actuals is not a workforce plan. The platform keeps the baseline synchronized with workforce records, and plan-versus-actual divergence is a standing, visible quantity. Some products warn explicitly that changes merged into systems of record can be overwritten by the next HR-system sync unless both sides are updated together — the anchoring is bidirectional and sensitive.

### Scenarios are isolated until selected

Scenario changes do not affect the live baseline or plan of record until the scenario is chosen and (in most products) approved. This isolation is what makes speculative modeling safe.

### Approval gates make a plan official

In mature products, a plan or scenario passes through review and approval — by finance, leadership, or the owning executive — before it becomes the plan of record or is handed off to execution systems. Delegation assigns accountability for portions of a plan, not just edit rights.

### Handoffs are directional

The planning platform decides and records; it does not execute hiring, payroll, or reorganization. Approved hiring plans flow to recruiting/HCM, cost plans to finance processes, and structural changes to org-design machinery. When a product does include execution machinery (for example, requisition approval inside an HCM suite), that is bundling across Types, not part of the planning core.

### The subject is the workforce, not money

Cost is modeled as the workforce's economic shadow, but the objects being planned are people — roles, positions, skills, capacities. This is the rule that keeps the Type distinct from financial planning, where headcount is merely a cost line.

## Variants

- **Horizon gradient** — multi-year strategic workforce planning (initiative-driven, scenario-heavy), medium-term tactical planning, and short-term annual/quarterly headcount planning with approval workflows are poles of the same Type; many products serve several, and vendors commonly sell "strategic workforce planning" and "headcount planning" as use cases or modules of one platform.
- **Granularity variants** — position-level planning (individual seats), role/job-family cluster planning, and skills-based planning (skills as the planning unit) — often mixed in one deployment.
- **Packaging variants** — a companion module of a people-analytics platform; a product inside an enterprise FP&A/planning suite; one suite in a workforce-planning portfolio alongside org-chart and org-design products; the planning solution of a workforce-transformation platform; a planning module of a mid-market people-ops platform.
- **Delivery variants** — self-serve SaaS operation versus consulting-led deployment for large transformation programs; public-sector workforce planning with longer horizons and establishment controls.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| People Analytics Platform | adjacent, frequently bundled | analytics describes and measures the workforce as it is or was (question → answer); workforce planning holds normative plan objects across a future horizon and runs the demand–supply–gap–action loop |
| Organization Design Platform | adjacent sibling, frequently bundled | org design asks how the organization should be structured (reporting lines, positions, spans) and compares structures; workforce planning asks how many people of what kind will be needed over time; structure changes are a handoff between them |
| Workforce Management Platform | adjacent, layered below | workforce management runs the operational shift/day loop (demand → schedules → worked time → labor governance); workforce planning is the multi-period strategic/tactical layer above it and hands targets down |
| Budgeting & Forecasting Platform (FP&A) | neighboring domain | FP&A plans money (revenue/expense lines, headcount as a cost line); workforce planning plans people, with cost as the shared currency bridging to finance — workforce planning can be packaged inside an FP&A suite without being the same Type |
| Succession Planning Platform | adjacent sibling | succession centers named individuals and their readiness for specific key roles; workforce planning centers aggregate workforce quantities by segment — readiness signals may feed planning, but pipelines of people are not plans of populations |
| HRIS / HCM | data substrate and execution side | HRIS is the record master for the current workforce and HR operations; workforce planning consumes it as baseline and actuals and hands approved targets back for execution |
| Demand Planning (supply chain) | same word, different subject | demand planning forecasts goods and services; workforce planning forecasts the workforce needed to serve business demand — they may consume the same drivers from opposite sides |

The sharpest boundary in practice is with People Analytics: the same vendors bundle both, the same data feeds both, and the interfaces look similar. The structural test is whether the system holds a plan of record for the future and computes gaps and actions against it — or answers questions about the present and past.

## Representative Products

- Visier — Workforce Planning (people-analytics-native companion solution)
- Nakisa — Strategic Workforce Planning Suite (enterprise suite with a documented planning methodology and a headcount planning module)
- OrgVue (workforce-transformation platform combining workforce planning with organization modeling)
- Workday Adaptive Planning — Workforce Planning (workforce planning inside an enterprise FP&A planning suite)
- ChartHop — Planning (scenarios and headcount planning on an org-chart-native mid-market platform)

The defining structure was checked against the pre-software practice of the same job — maintained manpower-planning files: current establishment by department and grade, forecast requirements by year, attrition and retirement assumptions, gaps, alternative staffing options, periodic reconciliation — to avoid over-fitting the definition to the current SaaS market.

## Sources

Research date: **2026-09-08**

- Visier — Workforce Planning solution page: https://www.visier.com/solutions/workforce-planning/
- Nakisa — Strategic Workforce Planning Suite product page (including documented six-step planning workflow and headcount planning module): https://nakisa.com/products/strategic-workforce-planning-software/
- OrgVue — Workforce Planning solution page (including documented five-step workflow): https://www.orgvue.com/solutions/strategic-workforce-planning/
- Workday — Adaptive Planning, Workforce Planning product page: https://www.workday.com/en-us/products/adaptive-planning/workforce-planning/overview.html
- ChartHop — Planning documentation index: https://docs.charthop.com/planning ; scenario mechanics cross-referenced from research/organization-design-platform.md (first-hand capture of https://docs.charthop.com/scenarios)

> Sourcing limitation: vendor help-center / operational documentation was not reachable for Visier (docs site returned empty), Workday, Nakisa, or OrgVue during this pass; these products are evidenced at official product-page level. ChartHop's headcount-planning documentation body was client-rendered and empty at fetch time, so its headcount-planning mechanics rest on the documentation index and the scenario documentation captured during the earlier organization-design research pass. Interface-level mechanics are therefore described conceptually, and no precise numeric limits, defaults, or time windows are asserted anywhere in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against the neighboring sibling Types are recorded in the paired Research Notes.
