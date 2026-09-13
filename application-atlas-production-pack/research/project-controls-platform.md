# Research Notes — Project Controls Platform

Research date: 2026-09-09

## Research Goal

Understand what a "Project Controls Platform" actually is as an Application Type: what objects it holds, who uses it, what its control loop is, and — critically — whether it is a distinct Type or merely an umbrella over Construction Cost Management + Construction Scheduling + Change Order Management + risk tooling.

## Initial Boundary

The leaf sits in DIRECTORY §17 (Construction, Real Estate & Facilities). Prior sibling passes left explicit forward notes:

- **construction-cost-management** (processed 2026-09-07): records Project Controls Platform as "superset pillar — combines cost with schedule, risk, and progress measurement; this Type is the cost pillar alone."
- **construction-scheduling** (processed 2026-09-07): records Project Controls Platform as "adjacent sibling — controls govern cost + schedule + risk + change at program level; scheduling is the schedule discipline feeding it."
- **preconstruction-management** (processed 2026-09-09): "schedule/risk appear inside precon only as optional workstreams at the enterprise pole — not definitional here"; forward note for this leaf.
- **construction-contract-administration** (processed 2026-09-07): describes "standalone project-controls module" as one packaging of contract administration — a bundling seam.

Initial hypothesis: project controls = the measurement-and-governance discipline over capital projects (baseline vs actual across cost AND schedule, variance, forecast, change, risk, reporting), operated by a distinct profession (project controllers / cost engineers / planners). Risk to test: umbrella-alias collapse into the sibling Types.

## Research Questions

1. What is the unit of record — project, program, portfolio?
2. What is the "baseline" concretely, and is cost+schedule integration definitional or incidental?
3. Where do actuals and progress come from, and how do they enter the system?
4. What does the recurring control loop look like (cadence, artifacts, decisions)?
5. Who is the user — is there a distinct "project controls" profession in evidence?
6. Which capabilities are common mature structure vs definitional (EVM, risk, change, portfolio roll-up, field capture, document management, estimating)?
7. Where are the seams to Construction Cost Management, Construction Scheduling, Construction Project Management, PPM, Estimating, Change Order Management?
8. Historical check: would spreadsheet-era / pre-platform project controls still satisfy the definition?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| InEight | Modern integrated project-controls suite for capital construction (contractor + owner) | Self-brands "project controls platform"; modular suite; explicit project-controller user |
| Cleopatra Enterprise | Cost-engineering-heritage project controls (EPC/owner, process & energy industries) | Dedicated "Project Controls" solution page; AACE/cost-engineering culture; STO/turnaround scope |
| Octave Sequence Enterprise (formerly Hexagon EcoSys) | Enterprise project performance platform (owner/operators, EPC) | "Project controls and project management" feature framing; enterprise/portfolio scale; no-code configurability |
| Oracle Primavera Cloud | Schedule-heritage project controls (CPM standard pedigree; owners + delivery teams) | The CPM/planning standard extended with risk, resources, portfolio, capital planning |
| Contruent (formerly ARES PRISM) | Lifecycle cost management / out-of-the-box project controls (owner/EPC, government-adjacent) | WBS/CBS control-account machinery; EVMS-heritage vocabulary; explicit cost-engineer role |

Deliberate spread: integrated suite vs cost-engineering vs enterprise-configurable vs schedule-heritage vs out-of-box lifecycle cost; contractor/owner/EPC seats; building/infrastructure/process-energy industries; US/EU/global.

## Sources

All fetched 2026-09-09 (Layer A unless noted):

- InEight — Platform overview: https://ineight.com/products/platform/
- InEight — Project Controls solution: https://ineight.com/products/ineight-project-controls/
- InEight — Earned Value Management solution: https://ineight.com/process-solutions/earned-value-management/
- Cleopatra Enterprise — home: https://cleopatraenterprise.com/
- Cleopatra Enterprise — Project Controls software: https://cleopatraenterprise.com/project-controls-software/
- Octave (formerly Hexagon) — Sequence Enterprise (formerly EcoSys): https://hexagon.com/products/ecosys (serves Octave-branded page)
- Oracle — Primavera Cloud: https://www.oracle.com/construction-engineering/primavera-cloud-project-management/
- Contruent (formerly ARES PRISM) — home: https://www.aresprism.com/ (serves contruent.com)
- Contruent — Budget Management (WBS/CBS): https://www.contruent.com/product/contruent-cost/budget-management/

Failed/blocked sources: Deltek Cobra/Acumen (deltek.com 404 ×2 — abandoned per network rule). Deep help-center documentation (InEight learn.ineight.com, Oracle docs library, Octave docs.hexagonali.com) not fetched this pass — product/solution pages are the reachable layer. EcoSys/Contruent rebrands discovered during fetch (EcoSys → Octave Sequence Enterprise; ARES PRISM → Contruent).

## Product Observations

### InEight (Layer A)

- Self-description: "construction project controls platform… multiple purpose-built applications for managing capital projects, spanning from pre-planning to predictable, on-time completion and commissioning"; "unify your scope, cost, and schedule in one connected platform to replace disconnected systems with real-time insight."
- Project Controls bundle = Control (budgets, forecasts, actuals, ERP integration) + Contract + Change + Plan & Progress (work packaging, mobile field capture); beside Estimate, Schedule (full CPM, AI planning, risk analysis), Document, Model, Report & Explore (portfolio dashboards).
- Project Controls page: five core capabilities — seamless data integration; advanced budgeting and forecasting ("time-phased budgets… supported by detailed work breakdown structures"); superior change order management ("approved change orders integrate directly into your budget, so budgets and forecasts are always synced"); built-in EVM; detailed work packaging ("work packages are integrated with project budgets").
- EVM page: EVM connects "planned value, earned value, actual cost, schedule progress, percent complete, and forecasting data"; percent complete tied to "recorded field progress" to remove opinion; owner-contractor alignment ("owners validate the project story, contractors manage performance"); review "at both the detailed work breakdown level and the project level"; forecasting from "performance-to-date."
- Users named: Project Controllers, Field Teams, Executives. Customer titles in evidence: "Director of Project Controls," "VP Global Program Controls," "Senior Project Controls."
- Audit posture: "Undeletable records support audit-proof review"; FedRAMP for regulated industries/government capital projects.
- Industries: transportation, power & renewables, nuclear, water, oil/gas/chemical, mining.

### Cleopatra Enterprise (Layer A)

- Home: "integrated software solution for Capital Projects and STO (Shutdowns, Turnarounds and Outages) Projects… support the complete lifecycle, from planning to execution"; "in control of scope, cost, and time all at once."
- Project Controls page defines the practice: "many organizations are adopting project controls software to support cost control, change management, and earned value management (EVM). These practices assist companies to stay within budget and time by monitoring project performance against the baseline, identifying areas of concern, and implementing corrective measures."
- "Consolidated baseline by combining cost and schedule — establish a single, unified project baseline that integrates both cost and schedule for complete project performance visibility… track every deviation against this consolidated baseline."
- Baseline mechanics (FAQ): "A cost estimate and schedule can be used to set up the baseline… budget items… imported from Excel or another system, but also taken from an estimate… a basic schedule can be set up in cost management, and more complex schedules can be imported from dedicated scheduling software such as Primavera and MS Projects. All these interfaces are bi-directional and enable you to set up multiple baselines."
- Actuals from ERP: "import information such as commitments (contracts, POs) and actuals (hours, invoices, expenses, accruals) directly from ERP systems such as SAP."
- EVM: CPI/SPI, S-curves, "customizable metrics and forecasting methods"; forecasting from "current progress, trends, risk factors, and performance history"; scenario analyses (best/worst case).
- Change: "structured change management workflows establish clear thresholds, approval paths, and stakeholder notifications… transparent audit trail."
- Field: "connected field workers report real-time progress directly into the system."
- Risk: "identify, analyze, and mitigate risks… evaluate contingencies… what-if analysis."
- Contract types: "reimbursable, lump sum and hybrid… visualize and manage your cashflow and revenue."
- Configurable dashboards/KPIs; ISO 27001; AACE Certified Education Provider (cost-engineering culture).

### Octave Sequence Enterprise, formerly Hexagon EcoSys (Layer A)

- Category: "Enterprise Project Performance" (EPP); "an enterprise-wide perspective into what drives project success."
- Feature pillars: project portfolio management; "project controls and project management — take control of the full project lifecycle… deliver projects on schedule and within budget"; project planning, scheduling and estimating; "earned value and performance management — streamline EVM and ensure accurate outcome predictions"; budgeting and forecasting; capital budgeting and funding ("connecting budgeting and fund management… at the strategic portfolio level with tactical project progress and performance data").
- Integration breadth: "connects seamlessly with virtually any business-critical system, including finance, accounting, procurement, scheduling, design, construction management and contractor time tracking."
- Form: no-code/low-code configurable platform ("tailor screens, workflows, reports, dashboards, KPIs"); role-based dashboards "from project professionals analyzing details to executives seeking high-level insights"; mobile apps; multi-tenant cloud; "millions of transactions… multi-year capital programs."
- Evidence of the user profession: "25% increase in project controller productivity" (Forrester TEI study cited on page).
- Clients: EPC firms, Turner & Townsend, Technip Energies, Ball Aerospace, Burns & McDonnell.

### Oracle Primavera Cloud (Layer A)

- Positioning: "Connect owners and delivery teams to shared planning, scheduling, resources, and risk management"; "the industry standard in CPM planning and scheduling… built from the same pedigree as Primavera P6."
- Scope: contract schedule (CPM) + field schedule (lean/Last Planner-aligned task management) "structurally connected… into one unified plan"; resource management (centralized labor/equipment/material pool, "future period capacity planning of quantities and costs"); risk management (all six PMI-framework steps: register, qualitative scoring, quantitative Monte Carlo simulation, response plans, monitoring, dashboards; "easily tie risks to the schedule"); portfolio management and capital planning for owners; configurable dashboards at "project, workspace, and portfolio-level."
- Cost linkage: resource/cost loading of the plan; "manage cash flow"; capital planning; contingency budgets with risk ("Manage risk and contingency budgets in one solution").
- Interchange: XER import/export with P6; MPP import; "operate as a current and historical hub to manage and control all your project plans."
- FedRAMP "In Process" designation (2026 press release linked).
- Note: cost management here is schedule-anchored (cost loading, cash flow, capital planning) rather than a full commitment/invoice ledger — the schedule-heavy pole of the Type. Oracle's own related-product framing separates "project delivery and controls" (Aconex) and "capital program management" (Unifier).

### Contruent, formerly ARES PRISM (Layer A)

- Positioning: "LIFECYCLE COST MANAGEMENT… Deliver capital projects and programs with precision, speed and cost efficiency by integrating cost and schedule"; "Project Controls Software, Ready Out-of-the-Box."
- Product family: Procurement (ProcureWare: vendor/RFP/contract award), Estimate (QTO 2D/3D/BIM, estimating), Engineering (design-phase controls), Cost Controls (Budget Management WBS/CBS, EVM, Field Management, Cost Forecasting, Integrated Schedules), Contracts (contracts & commitments, POs & invoices, pay requests & progress claims, change orders), Change Management (trends & change orders, approvals & certified audit trail), Data Insights (dashboards, reports, BI), Integrations.
- Budget Management page: WBS "connects scope to schedule and cost… logical work packages"; CBS "mirror[s] the WBS with detailed cost code structures… by funding source, cost type, or contract structure"; "link project scope directly to cost control accounts"; "Establish time-phased budgets using WBS/CBS-aligned control accounts"; "Every dollar, hour and quantity is tied to a control point"; roll-up/drill-down "across programs, contracts and work packages"; "Integrated Scheduling: sync cost and schedule by linking WBS and CBS to activities in Primavera P6 or Microsoft Project"; "Change Management: automatically reflect scope changes in your budget structures"; "EVM: use WBS/CBS-based control accounts to drive performance metrics, forecast final costs, and detect trends early"; "centralized, version-controlled cost data."
- Roles served: Executives & Owners, Cost Engineers, Project Managers, Field Engineers, Procurement Managers, Estimators.
- Customer titles in evidence: "Project Controls Manager," "Lead Controller"; customer self-describes goal as "excellence in PC."
- Anti-spreadsheet framing: "Megaprojects are too complex for spreadsheets and manual processes… can't scale to manage the vast scope of cost, schedule and change data involved."
- Forecast accuracy claim in customer quote ("+/- 15% to +/- 4%") — vendor-published testimonial, not independently verified.
- ISO 9001/27001; UK G-Cloud supplier.

## Cross-product Comparison

| Structure | InEight | Cleopatra | EcoSys/Octave | Primavera Cloud | Contruent | Strength |
|---|---|---|---|---|---|---|
| Project/program of record tracked over life | ✓ | ✓ | ✓ (enterprise/program scale) | ✓ (project/workspace/portfolio) | ✓ (programs, contracts, work packages) | Universal (A) |
| Integrated cost+schedule baseline ("consolidated baseline", WBS/CBS control accounts, time-phased budget) | ✓ time-phased budget + WBS + schedule | ✓ explicit "consolidated baseline by combining cost and schedule", multiple baselines | ✓ EVM + budgeting + scheduling integrated | ✓ cost/resource-loaded CPM schedule + capital planning | ✓ WBS/CBS control accounts + integrated schedules | Universal (A) — the Type's signature |
| Progress/actuals ingestion from execution sources | ✓ field capture + ERP + scheduling tools | ✓ field progress + ERP (SAP) + Primavera/MSP | ✓ finance/accounting/procurement/scheduling/time tracking | ✓ field task updates + resource loading | ✓ field management + ERP/accounting integrations | Universal (A); sources vary |
| Variance + performance metrics + forecast-to-complete | ✓ EVM, forecasting from performance-to-date | ✓ CPI/SPI, S-curves, forecasting, scenarios | ✓ EVM, outcome predictions | ✓ schedule health indicators, cash flow, risk-adjusted outcomes | ✓ EVM, cost forecasting, trend detection | Universal (A); EVM is the mature form |
| Change machinery updating the baseline | ✓ change orders integrate into budget | ✓ structured change workflows, thresholds, audit trail | ✓ (within project controls pillar) | ✓ (contingency/risk response; lighter change emphasis on page) | ✓ trends & change orders → budget structures, certified audit trail | Strong (A, 4/5 explicit) |
| Recurring performance reporting / governance dashboards | ✓ dashboards, Report & Explore | ✓ dashboards, KPIs, cost reports | ✓ role-based dashboards | ✓ dashboards at all levels | ✓ executive dashboards, 200+ prebuilt | Universal (A) |
| EVM metrics (CPI/SPI/S-curves) | ✓ | ✓ | ✓ | ✓ (risk-adjusted; EVM heritage) | ✓ | Common mature (4/5 explicit) |
| Risk management (register, qualitative/quantitative) | ✓ (solution) | ✓ | ✓ (implied in pillar) | ✓ full PMI 6-step, Monte Carlo | — (not prominent on fetched pages) | Common, NOT definitional (Contruent pole) |
| Portfolio/program roll-up | ✓ | ✓ (PPM solution) | ✓ (EPP pillar) | ✓ (portfolio + capital planning) | ✓ (programs) | Common mature |
| Field/mobile progress capture | ✓ | ✓ | ✓ (mobile apps) | ✓ (task management mobile) | ✓ (field management) | Common mature |
| Schedule-tool interchange (P6/MSP) | ✓ (integrations) | ✓ (bi-directional Primavera/MSP) | ✓ (scheduling integration) | ✓ (XER/MPP native) | ✓ (P6/MSP linking) | Common mature |
| ERP/financial integration for actuals | ✓ | ✓ (SAP) | ✓ | ✓ (Oracle stack) | ✓ | Common mature |
| Estimating inside the platform | ✓ (Estimate) | ✓ (heritage core) | ✓ (pillar) | — | ✓ (Estimate + QTO) | Common, NOT definitional (Primavera pole) |
| Document/model management inside | ✓ (Document, Model) | — | — | — | — | Optional (1/5) |
| Contracts/commitments inside | ✓ (Contract) | ✓ (tendering & contracting) | — | — | ✓ (Contracts family) | Common, NOT definitional |
| STO/turnaround scope | — | ✓ (OPEX suite) | — | — | — | Variant (1/5) |
| No-code configurability | ✓ (configurable) | ✓ (configurable dashboards) | ✓ (signature) | — | ✓ (templates) | Variant emphasis |
| Compliance posture (FedRAMP/G-Cloud, audit) | ✓ FedRAMP | ✓ ISO 27001 | — | ✓ FedRAMP in-process | ✓ G-Cloud, ISO, certified audit trail | Variant (regulated/government pole) |

## Canonical Model (Layer C synthesis)

```text
Controlled project/program of record
└── Integrated performance baseline (the plan-of-record)
    ├── scope structured over breakdown hierarchies
    │   (WBS / CBS — work packages, control accounts, cost codes)
    ├── time-phased budget (cost dimension)
    └── linked schedule (time dimension)
        ↓ measured against
Progress + actuals (from field capture, ERP/finance, scheduling tools)
        ↓
Variance · performance metrics (EVM at the mature pole) · forecast-to-complete
        ↓
Controlled change (trends/change orders → baseline updates, audit trail)
        ↓
Recurring performance reporting → governance decisions (project → program → portfolio)
```

### L0 — Defining Invariant (three jointly-held structures)

1. **The controlled project/program of record** — a persistent, identified capital project (or program of projects) whose performance is tracked over its life in the system. Remove → disconnected reports/spreadsheets with no project memory.
2. **The integrated performance baseline** — the plan-of-record binding scope, cost, and schedule into one measurable reference: a time-phased budget structured over breakdown hierarchies (work/cost breakdown structures, control accounts) linked to the schedule, held as a managed, versioned baseline. Remove → a scheduling tool (schedule baseline only) or a cost ledger (budget only); the control reference dies.
3. **The control loop** — progress and actuals flow in from execution sources; the system measures them against the baseline, producing variances, performance metrics, and forecasts of the final outcome; changes are recorded as controlled adjustments that update the baseline; the comparison is surfaced as recurring performance reporting for governance. Remove → a static plan, or raw status reporting with no plan-of-record.

Jointly-held load-bearing:
- 1 alone = project registry / portfolio list
- 2 without 1 = a plan file or template
- 3 without 1+2 = raw progress reporting
- 1+2 without 3 = a static planning artifact (planning, not control)
- 1+3 without 2 = status tracking with no plan-of-record
- 2+3 without 1 = a measurement engine with no project memory

### L1 — Common Mature Structure

- EVM metrics (planned/earned value, CPI/SPI, S-curves) as the mature measurement form
- Change/trend machinery feeding controlled baseline updates with audit trail
- ERP/financial integration (commitments, invoices, hours, accruals as actuals)
- Schedule-tool interchange (Primavera P6 XER / Microsoft Project MPP, bi-directional)
- Field/mobile progress capture (quantities, hours, percent complete)
- Portfolio/program roll-up and executive dashboards
- Configurable dashboards/KPIs per role
- Risk management (register, qualitative scoring, quantitative simulation)
- Work packaging (work packages tied to budget lines)
- Contract/commitment visibility feeding cost measurement
- Version control / audit trail on baseline and cost data

### L2 — Variant / Optional Structure

- Operating seat: owner (validate contractor progress, funding oversight) vs contractor/EPC (manage performance, margin) vs both in one environment
- Industry weight: building construction vs infrastructure/transportation vs process/energy (oil & gas, power, nuclear, mining) vs water
- Compliance posture: EVMS/compliance-driven measurement (government/regulated) vs commercial performance management; FedRAMP/G-Cloud/ISO postures
- STO/turnaround (shutdown/turnaround/outage) scope measured with the same machinery
- Estimating inside the platform vs integrated from external estimating tools (baseline seeded either way)
- Document control / 3D model management inside vs outside
- Contracts/procurement inside vs outside
- Deployment: cloud SaaS vs configurable no-code platform vs out-of-the-box templates
- What-if/scenario analysis depth; AI planning/forecasting assistance (era-current)

### L3 — Vendor-specific (research notes only)

- InEight module names (Control, Contract, Change, Plan & Progress, Estimate, Schedule, Document, Model, Report & Explore); InEight NOW per-user tier; "undeletable records" phrasing
- Octave/EcoSys rebrand history; Forrester TEI statistics; EcoSys Connect data integration product
- Cleopatra CESK cost dataset; STO Control sister product; Cost Engineering Academy; Dutch "Projectbeheersing" site
- Contruent ProcureWare; Contruent Drive; G-Cloud 14 listing; Dodge SmartMarket report
- Oracle Primavera P6 XER interchange specifics; Last Planner System® alignment in Primavera Cloud task management; Oracle Integration Cloud bundling (2M messages/month allotment); Aconex/Unifier sibling positioning

## Umbrella Question (the central taxonomy risk)

Is "Project Controls Platform" merely an umbrella over Construction Cost Management + Construction Scheduling + Change Order Management + risk tooling?

**Resolution: distinct Type.** Evidence:

1. **Own unit of record.** The integrated performance baseline (consolidated cost+schedule plan-of-record over WBS/CBS control accounts) is not owned by any sibling Type. Construction Cost Management owns the cost budget alone (its own doc: "this Type is the cost pillar alone"); Construction Scheduling owns the calculated schedule network alone. The *consolidation* is this Type's signature — Cleopatra names it explicitly ("consolidated baseline by combining cost and schedule"), Contruent structures it (WBS/CBS control accounts + integrated schedules), InEight time-phases budget against schedule with EVM.
2. **Own terminal discipline.** The control loop (measure → variance → forecast → report → decide) is a governance rhythm with its own artifacts (the recurring performance/cost report, EVM metrics, forecast revisions), not just the sum of the sibling loops.
3. **Own user profession.** All five products name the project controls profession in their own materials: "project controllers" (InEight user segment; EcoSys "project controller productivity"; Contruent "Project Controls Manager"/"Lead Controller" testimonials; Cleopatra cost-engineering culture; Primavera's scheduler/controls heritage). The sibling Types' primary users differ (cost managers, schedulers, PMs coordinating parties).
4. **Precedent.** Matches the preconstruction-management resolution pattern: an umbrella suspicion dissolves when the sampled products organize around their own unit of record and terminal event rather than around a toolbox.

The sibling Types remain real Types as single disciplines; this Type is defined by their integration under one measurement baseline and one governance loop. Bundling (a controls platform containing estimating, contracts, documents) goes outward from the core and does not dissolve it.

## Boundary Findings

| Neighbor | Seam | Removal test |
|---|---|---|
| Construction Cost Management | cost pillar alone vs integrated control | strip the schedule dimension + EVM/cross-dimensional loop → cost management remains |
| Construction Scheduling | schedule discipline vs integrated control | strip the cost dimension + measurement loop → scheduling remains |
| Construction Project Management | coordination record (RFIs/submittals/community/documents) vs measurement record (baseline/variance/forecast) | strip the coordination record and community → controls remains; strip baseline+loop → PM remains |
| Project Portfolio Management Application | selection/funding/prioritization above projects vs execution measurement of projects | strip the execution baseline+loop, keep selection/funding → PPM remains (EcoSys/Primavera bundle both — bundling seam, not alias) |
| Construction Estimating | pre-award pricing vs post-award control; estimate seeds the baseline (designed seam) | strip execution measurement, keep pricing → estimating remains |
| Change Order Management | change machinery vs baseline ownership | strip the baseline the changes update → change tooling remains |
| Progress Billing | revenue mirror (owner billing) vs cost/performance control | strip measurement, keep billing → Progress Billing remains |
| Business Intelligence / Dashboard Platform | computes from its own project performance record vs visualizing external data | strip the project record + baseline → generic BI remains |
| Generic Project Management Application | task-level coordination vs baseline-disciplined measurement with breakdown structures | strip WBS/CBS control accounts + baseline discipline → generic PM remains |

## Historical / Market-Sample Check (§24)

- **Spreadsheet-era project controls**: a cost engineer maintaining budget-vs-committed-vs-actual-vs-forecast spreadsheets beside a planner's schedule, merged in a monthly report, satisfies the L0 (baseline reference + measurement loop + project of record) with no platform at all. Therefore "platform" packaging, cloud delivery, dashboards, and mobile capture are NOT definitional.
- **Schedule-only heritage tools** (e.g., classic CPM engines): a schedule baseline with progress and dates variance but no cost dimension fails the integrated-baseline leg — correctly classified as Construction Scheduling, not project controls. The sampled schedule-heritage product (Primavera Cloud) reaches toward the Type through cost loading, capital planning, and risk, and Oracle itself frames cost-light scheduling and "capital program management" as siblings.
- **EVMS compliance tooling** (government/defense earned-value systems): satisfies the L0 with the compliance posture as variant; the EVMS pole was not directly sampled (Deltek unreachable) but the in-sample EVM evidence (4/5 products) covers the measurement machinery.
- **Regional practice**: Cleopatra's Dutch "projectbeheersing" site and UK G-Cloud listing (Contruent) indicate the Type exists under regional labels and procurement regimes; nothing in the core is US-specific.

## Uncertainties

1. Deep operational documentation (help centers, admin guides) was not fetched; workflow details (exact status vocabularies, cadence defaults, permission models) are described structurally, not per-product.
2. Deltek Cobra/Acumen (the classic EVMS compliance pole) unreachable — the compliance-pole variant is inferred from in-sample EVM evidence, not from that vendor's own materials.
3. EcoSys and ARES PRISM rebrands (Octave Sequence Enterprise; Contruent) discovered mid-research; market materials under old names may describe older versions.
4. Vendor-published statistics (EcoSys Forrester TEI figures, Contruent customer quotes, Cleopatra survey percentages) are marketing claims, not verified outcomes; not used in the final document.
5. Primavera Cloud's cost depth (full ledger vs cost loading) could not be confirmed from the fetched page; treated as the schedule-anchored pole with cost linkage rather than asserting ledger parity.
6. The exact boundary between "project controls" and "capital program management" (e.g., Oracle Unifier, owner-side capital program suites) deserves its own pass if that leaf is processed; this pass treats owner-side program roll-up as a variant of controls, not a separate Type.

## Final Synthesis

A Project Controls Platform is the measurement-and-governance system of record for capital projects and programs. Its defining core is three jointly-held structures: the controlled project/program of record; the integrated performance baseline (scope structured over work/cost breakdown hierarchies into control accounts, time-phased budget linked to schedule, held as a managed versioned plan-of-record); and the control loop (progress and actuals measured against the baseline → variance, performance metrics, forecast-to-complete → controlled change updating the baseline → recurring performance reporting for governance). EVM, risk, portfolio roll-up, field capture, ERP integration, estimating, contracts, and document management are common mature or optional structures, not the definition. The Type is distinct from its single-discipline siblings (cost management, scheduling) precisely by the integration those siblings lack, and distinct from project management by measuring rather than coordinating.
