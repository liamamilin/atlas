# Public Budgeting Platform

## Overview

A **Public Budgeting Platform** is the system of record a government uses to build, review, adopt, publish, and manage its budget: the structured allocation of public money for a fiscal period, organized in the government's own fiscal framework and carrying the standing of a formal public spending plan.

The defining core is small:

```text
The government's budget (the unit of record)
└── structured in the government's fiscal framework
    ├── funds · departments/agencies · account classifications · fiscal period
    └── spanning operating, personnel, capital, and revenue sides
    └── built through a multi-participant cycle
        ├── contributing units submit requests and justifications
        └── the central budget office reviews, adjusts, consolidates, versions
    └── carrying public authority
        ├── proposed for adoption by the governing body
        ├── published as the budget document
        └── governing the year's spending through tracked amendments and transfers
```

What makes this Type distinct from ordinary budgeting software is the **standing of the object**. A corporate budget is an internal management plan; a public budget is the government's formal spending plan — publicly scrutinized, adopted by a governing body, published as a document of record, and treated as the frame that governs spending during the year. Everything commonly bundled with modern products — position budgeting, capital project modules, scenario tools, public transparency portals, performance dashboards — is widespread but not what makes the product a public budgeting platform.

## Users & Context

The work is a standing annual cycle inside a government's finance function, with many hands:

**Primary users:**

- **Department and agency budget staff** — draft and submit their unit's budget requests, manage their own cost centers, track adjustments to their allocations during the year. Products deliberately serve non-finance staff here: the submission workspace is designed so program managers can enter and justify numbers without being accountants.
- **The central budget / finance office** — owns the process: sets the calendar and instructions, reviews and adjusts submissions, consolidates the whole, runs scenarios, prepares the proposed budget, and manages mid-year changes. This office is the system's power user and administrator.

**Secondary users:**

- **HR / personnel staff** — supply position and compensation data that drives salary budgeting, typically the government's largest expense.
- **Executives (city manager, ministry leadership, school superintendent)** — review scenarios and trade-offs, set priorities, and sponsor the proposed budget.
- **The governing body (council, legislature, board)** — receives the proposed budget, holds hearings, and adopts it. The adoption act itself happens in the chamber, not in the software; the platform produces and versions what the governing body acts on.
- **The public** — reads the published budget document and, in many deployments, explores an interactive public budget site.

Typical context: a municipality, county, state or provincial government, national ministry, school district, or public authority running its yearly budget preparation months ahead of the fiscal year, then living with the adopted budget — amending and monitoring it — throughout the year.

## Core Model

### The budget as the unit of record

The system's central object is **the government's budget**: a persistent, structured allocation of public money for a fiscal period. It is not a document or a spreadsheet; it is a structured dataset that everything else — submissions, reviews, scenarios, the published book, the year's amendments — hangs from.

The budget is organized in the **government's own fiscal framework**:

- **Funds** — the legally distinct pools public money is organized into (general fund, special revenue funds, capital funds, and similar), each with its own purpose and constraints. Funds are the universal public-sector realization of "which money may be spent for what."
- **Organizational units** — departments, agencies, ministries, divisions, programs: who is spending.
- **Account classifications** — the government's chart of accounts / budget classification: what the money is spent on (salaries, supplies, services, debt service...), often with a parallel program or project dimension.
- **Fiscal period** — the fiscal year the allocation belongs to, with multi-year views for capital and forecasting.

Against this framework the budget carries several **content sides**, which products commonly package as modules:

- **Operating budget** — day-to-day expenses by department, fund, and cost center.
- **Personnel budget** — salaries, benefits, and positions: tracked at the position level, rolled up to department and organization. Public-sector compensation machinery (pay grids and step scales, union agreements, layered benefits calculations, funding splits across accounts or grants) is common here because people costs dominate most governments' spending.
- **Capital budget** — multi-year capital projects and their funding sources, linked to (but distinct from) the operating budget.
- **Revenue side** — estimated revenues and other financing sources the spending must fit within.
- **Performance dimension (optional)** — goals, measures, and program structures that dollars can be aligned to.

### The build–review–consolidate cycle

The budget does not appear fully formed; the platform exists to run the cycle that produces it:

- **Contributing units draft and submit.** Each department works in its own workspace against its own cost centers, entering requests and justifications under the rules the budget office has set.
- **The budget office reviews, adjusts, and consolidates.** Submissions roll up through the organizational hierarchy; the center can accept, reduce, question, or restructure; approvals and version control keep the whole coherent.
- **Scenarios are tested.** Alternative allocations, revenue assumptions, and staffing plans are modeled as parallel versions before anything is proposed.
- **A proposed budget emerges** — the consolidated, balanced-per-local-rules package that goes to the governing body.

### The public-authority posture

The budget's standing is what separates this Type from private planning tools:

- The proposed budget is **presented for adoption** by the government's governing body or legislature.
- The adopted budget is **published** as the government's budget document (the "budget book"), commonly alongside comprehensive annual financial reports.
- The budget **governs the year**: spending during the fiscal period is framed by the adopted allocations, and changes to them — transfers between lines, amendments, supplemental requests — are made as tracked, auditable changes to the budget of record rather than as silent edits.

### Standard capabilities around the core

Mature products commonly add:

- departmental submission workspaces with roles, permissions, and approval workflows
- position control and compensation modeling (pay grids, union scales, benefits layering)
- capital project budgeting with funding-source allocation and multi-year plans
- revenue forecasting and driver-based projections
- scenario planning and what-if versioning
- budget-vs-actual monitoring and variance analysis across funds, departments, and cost centers
- mid-year amendment and transfer processing with auditable history
- budget book and financial report publication, with accessibility and award-standard alignment
- integration with the government's ERP / general ledger so budget data and actuals stay synchronized
- performance/strategic linkage as an add-on module
- a public transparency portal fed by the budget data

Which of these a given product carries varies with segment and product form; none of them alone defines the Type.

## How It Works

### The annual preparation cycle

```text
Budget office sets the calendar, instructions, and targets
→ departments draft requests in their workspaces (operating lines, positions, justifications)
→ submissions roll up; budget office reviews, questions, adjusts
→ scenarios and what-ifs tested (alternative allocations, revenue assumptions, staffing plans)
→ consolidated proposed budget assembled and balanced
→ budget document produced for the governing body
→ hearings and adoption (outside the platform)
→ adopted budget becomes the year's frame
```

The cycle is annual and recurring: each fiscal year's budget is built as a new cycle over the same fiscal framework, informed by prior-year and current-year actuals.

### The in-year loop

Once the budget is adopted, the platform's center of gravity shifts from building to governing:

```text
Monitor budget vs actuals across funds, departments, cost centers
→ variances surface
→ changes needed (shortfalls, new needs, reorganizations)
→ budget transfers / amendments / supplemental requests
→ routed through approval workflows
→ recorded against the budget of record with an auditable history
→ projections and forecasts updated
```

In deployments where the platform also touches execution, the adopted allocations feed the financial system as spending authority — appropriations and allotments that purchases and payroll are checked against — and commitments reduce available budget in real time. In preparation-focused deployments this control lives in the ERP instead, and the platform stays the planning and publication layer.

### The publication step

The budget data drives the published record: the budget book assembled from the system's own numbers (department pages, fund summaries, schedules, narrative), exported or published as an accessible digital document, and commonly mirrored on a public portal where residents can explore charts, tables, and maps of the budget. Because the publication is generated from the budget data, updates to the budget flow through to the published views.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Department submission workspace

The contributing unit's home.

- the unit's budget lines by fund and cost center, prior-year and current-year references, request entry with justifications
- primary actions: enter/adjust requests, attach narratives, submit for review, track approval status

### Budget office consolidation and review

The center's working surface over the whole budget.

- the full budget tree (funds → departments → cost centers → accounts), submission status, review notes, adjustment tools
- primary actions: review and edit submissions, consolidate, adjust targets, manage versions and approvals, run the calendar

### Scenario / what-if view

The trade-off surface.

- parallel budget versions with assumptions, comparisons of allocations and outcomes
- primary actions: create/duplicate scenarios, change assumptions, compare results, promote a scenario

### Personnel / position budgeting view

The people-cost surface.

- positions by department with pay, benefits, and funding source; roll-ups to department and organization
- primary actions: add/remove positions, model pay changes, split funding, handle mid-year hires and reclassifications

### Monitoring / variance dashboard

The in-year surface.

- budget vs actuals by fund, department, cost center; variance flags; forecasts
- primary actions: drill into variances, initiate amendments or transfers, update projections

### Budget book / publication studio

The document-production surface.

- the budget document assembled from live budget data: schedules, department pages, fund summaries, charts, narrative
- primary actions: build statements and schedules, generate sections, check accessibility and award-standard requirements, publish or export

### Public budget portal

The resident-facing surface (commonly a module).

- interactive charts, tables, and maps over the published budget, capital projects, and financial reports
- primary actions: explore by fund, department, or project; view documents

## Important Rules / Behaviors

### The fiscal framework is law-shaped, not preference-shaped

The fund structure, account classifications, and organizational hierarchy are not free design choices: they reflect the government's legal and accounting framework, and the budget must be expressed in them. Changing the structure is a governed event, not a user setting.

### Balance and legal constraints vary by regime

Many governments must adopt balanced budgets and operate under statutory limits (debt limits, tax and expenditure limits); national governments may run deficits. The platform supports the regime's rules — balance checks, constraint visibility — but the rules themselves are jurisdictional, not universal.

### Changes after adoption are tracked changes

Once the budget is adopted, edits do not silently overwrite it. Transfers, amendments, and supplemental requests are processed as discrete, approved, auditable changes against the budget of record. This audit trail is a structural expectation of public budgeting, not an optional nicety.

### Version control is structural

During preparation, multiple parallel versions (department requests, budget-office scenarios, the proposed budget, the adopted budget) coexist; which version is authoritative is explicit. Personnel budgets add their own versioning as staffing plans change during the year.

### Adoption happens outside the platform

The governing body's vote is a chamber act. The platform's role ends at producing and versioning what is adopted; the adopted budget then re-enters the system as the year's frame. Products differ in how much elected-official-facing support they provide, but the vote itself is not platform machinery.

### Role separation mirrors the process

Department staff see and edit their own units; the budget office sees and controls the whole; HR touches position data; executives and governing bodies consume reviews and documents. Access control is a first-class feature because the budget is both confidential during deliberation and public after adoption.

## Variants

- **By level of government** — municipal and county budgeting (the most common product segment), state/provincial budgeting, national ministry budgeting, federal agency and defense budgeting (with its own planning-programming-budgeting vocabulary and justification documents), school districts, and special-purpose authorities.
- **By regime** — balanced-budget jurisdictions with appropriation discipline vs national budgets with deficit capacity; executive-proposal + legislative-appropriation patterns vs parliamentary patterns.
- **By methodology** — line-item budgeting vs program, performance, or outcome-based budgeting; jurisdictions differ in how dollars are organized and justified.
- **By product form** — standalone budgeting suites; budgeting as one pillar of a whole-of-government financial management suite; budgeting modules embedded in government ERP; analytics-vendor overlays on top of existing systems.
- **By execution depth** — platforms that also carry in-system spending controls (appropriations, allotments, commitments) vs preparation-and-publication platforms that leave execution to the ERP.
- **By regional machinery** — US/Canada local-government machinery (budget books, comprehensive annual financial reports, award programs, accessibility standards) vs international public-financial-management machinery (chart-of-accounts reform, donor and standards frameworks, fiscal transparency programs).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Budgeting & Forecasting Platform (corporate) | sibling verb, different object | corporate budgets are internal management plans over a private chart of accounts — never adopted by a governing body, published as a public document, or treated as spending authority; public budgets carry that standing, plus fund-based fiscal structure |
| Public Financial Management System | broader suite | the whole-of-government fiscal architecture (budget + treasury + receipts + expenditure + civil service) of which budgeting is one cycle; budgeting platforms center on the budget cycle itself |
| Capital Improvement Planning | interlocking sibling | CIP's unit of work is the multi-year capital project register with funding-source allocation; public budgeting's unit of record is the fiscal-period budget as a whole; capital budgeting appears as a module inside budgeting suites, and CIP products lack the operating/personnel/revenue budget |
| Government Transparency Portal | output relationship | budget books and open budget sites are publication outputs of budgeting; the transparency portal is the standalone publication surface for government conduct, with no budget-building machinery |
| Government Performance Management | module relationship | performance budgeting links dollars to goals; the performance Type maintains the goal→measure→actuals loop as its own managed system; vendors sell performance as a separate module beside budget modules |
| Government Revenue Management / Tax Administration | input relationship | revenue estimation feeds budget formulation; collection and administration of revenues is a different Type |
| Government Grants Management | input relationship | grants appear as revenue sources and funding sources inside budgets; the grant lifecycle is separate machinery |
| Government Procurement Platform | execution relationship | procurement spends budgeted money; commitment control links the two; the solicitation-to-award cycle is that Type's center |
| Spreadsheet Application | the "before" state | the shared fiscal framework, workflow, consolidation, versioning, and audit history are exactly what spreadsheets cannot hold |

## Representative Products

- **Euna Budget** (Euna Solutions; Questica lineage) — purpose-built public-sector budgeting suite (US/Canada local governments, states, education, nonprofits) spanning strategic, performance, personnel, operating, capital, and transparency-publishing modules.
- **FreeBalance Accountability Suite™** — government resource planning (GRP) suite for national governments across many countries; budget formulation and execution controls (appropriations, allotments, commitments, transfers) as the center of a whole-of-government fiscal system.
- **Neubrain** — public-sector budgeting and performance analytics (US federal, state, local; defense budgeting and congressional justification work; counties, cities, authorities).

Market anchors used for structure only (official sites were not reachable during research; no product-specific claims are drawn from them): OpenGov (Budgeting & Planning), ClearGov (Budget Cycle), Tyler Technologies (ERP-embedded public-sector budgeting).

## Sources

Research date: **2026-09-09**

- Euna Solutions — Budget suite page: https://eunasolutions.com/solutions/budget/
- Euna Solutions — Operating Budgeting: https://eunasolutions.com/solutions/budget/operating-budgeting/
- Euna Solutions — Personnel Budgeting: https://eunasolutions.com/solutions/budget/personnel-budgeting/
- Euna Solutions — OpenBook Transparency Budgeting: https://eunasolutions.com/solutions/budget/transparency-budgeting/
- FreeBalance — Accountability Suite products: https://www.freebalance.com/en/products/
- FreeBalance — Public Financials Management: https://www.freebalance.com/en/products/public-financials-management/
- FreeBalance — PFM Modules: https://www.freebalance.com/en/products/public-financials-management/pfm-public-financials-management-modules/
- Neubrain — Government Budgeting Software: https://www.neubrain.com/solutions/government-budgeting-software
- NASBO — Budget Processes in the States & Territories: https://www.nasbo.org/reports-data/budget-processes-in-the-states

> Sourcing limitation: the large US vendor pole (OpenGov, ClearGov, Tyler Technologies) and all sampled vendors' operational help centers were unreachable (access denied) during research. Product evidence therefore rests on official product pages and one domain authority (NASBO). Workflow details such as submission deadlines, approval-chain depths, amendment thresholds, and fiscal-year defaults are intentionally not stated in this document; the budget cycle is described at the level the sources support. Detailed observations and evidence calibration are recorded in the paired Research Notes.
