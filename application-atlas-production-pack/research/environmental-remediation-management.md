# Research Notes — Environmental Remediation Management

## Research Goal

Understand the Application Type "Environmental Remediation Management" (§21 leaf) from real products: what a remediation-management application is, what exists inside it, who uses it, how remediation work is managed through it, and how it differs from its closest siblings — especially Contaminated Site Management (processed 2026-09-07, which flagged this leaf for cross-reference: "project execution vs lifecycle phase + data streams; one sampled product spans remediation projects + O&M — overlap specimen") and Environmental Site Assessment (processed 2026-09-08).

## Initial Boundary

Working hypothesis before research:

- Core use: managing the **execution of environmental remediation (cleanup) projects** — the work that removes, contains, or monitors contamination after assessment identifies it.
- Users: remediation project/program managers, environmental consultants, remediation contractors, finance functions, data managers.
- Nearest neighbors: Contaminated Site Management (site record + evidence across lifecycle), Environmental Site Assessment (bounded engagement → deliverable), Environmental Monitoring Platform (ongoing observation), Waste/Hazardous Waste Management (materials logistics), Construction Project Management (generic PM machinery), Environmental Data Platform (data corpus).
- Unknowns: does this Type have its own distinct product population, or is remediation always just a module/phase inside contaminated-site or data platforms? What is the center of gravity — data, money, field execution, or compliance?

## Research Questions

1. What is the unit of managed work — the site, the project, the obligation, the field job?
2. What does the system hold about the remedy itself: scope, strategy, phasing, cleanup criteria/targets, schedule?
3. How is execution managed: work authorization, tasks, field records, contractors, change?
4. How is progress toward "clean"/closure measured and evidenced (monitoring data, treatment-system performance, verification)?
5. How do money (budgets, forecasts, POs, change orders, invoices) and vendors figure in — core or common?
6. How does regulation figure in: frameworks, deadlines, reports, submissions, audit?
7. Who are the users and how do owner-side, consultant-side, and contractor-side products differ?
8. Where is the seam vs Contaminated Site Management, Construction PM, and EHS/compliance platforms — what would have to be removed to cross each seam?

## Representative Products

Selected for different product philosophies and customer tiers:

| Product | Pole | Customer tier | Evidence |
|---|---|---|---|
| **ENFOS** | finance-led remediation obligation & project portfolio management (system of record for remediation operations + accounting) | enterprise owner/operators (energy, industrial) | official product page fetched (A); case studies via search snippets (A-) |
| **Locus EIM — Remediation & Environmental Liability Management** | data & operations-led (remediation project data + O&M of treatment systems) | enterprise owners, consultancies | official product page fetched (A) |
| **EnFlection (Trihydro)** | remediation + post-closure + active-operations system of record (data-led; the overlap specimen named by the contaminated-site pass) | consultancies, owners across 38 US states (vendor figure) | official product page fetched (A) |
| **FieldFlō** | contractor-side field-execution management (scheduling, T&M, safety, job costing) | remediation/abatement contractors (SMB) | official product page fetched (A) |

Secondary specimens (official pages seen via search snippets, not deep-fetched — evidence marked A-): **PIR-a RemMS** (GIS-based remediation project execution: field tickets, daily site documentation, soil data for remediation/disposal decisions), **EVX Software** (consulting PM: phases, remediation tasks, compliance deliverables, budgets), **Matidor** (map-centric consulting PM: remediation zones, real-time budgets, offline field capture), **SiteCrest** (asset-owner portfolio tracking from assessment through remediation completion, divestment framing), **BEM PMDB** (project dashboard for site assessment/investigation/remediation with regulatory-stakeholder access, EDD sync), **EnviroCommand** (consulting firm platform: projects/phases/tasks, state compliance deadlines).

Deliberately not sampled again as primary: ESdat / EQuIS (already the environmental-data/contaminated-site substrate in two prior passes; both can serve remediation programs but center the data spine, not project execution).

## Sources

Fetched 2026-09-10 (layer A):

- ENFOS — Environmental Remediation Software (ASC 410-30) — https://enfos.com/environmental-remediation-obligation
- Locus Technologies — EIM Remediation & Environmental Liability Management — https://www.locustec.com/applications/environmental-information-management/remediation/
- Trihydro — EnFlection Environmental Software — https://www.trihydro.com/digital-services/enflection/
- FieldFlō — Environmental Remediation Management Software — https://fieldflo.com/environmental-remediation

Search-snippet official pages (layer A-):

- PIR-a Corp — RemMS — https://www.pir-a.com/remms
- EVX Software — Site assessment and remediation — https://www.evxsoftware.com/industries-site-assesment-and-remediation
- Matidor — Environmental services — https://matidor.com/solutions/environmental-services
- SiteCrest — https://www.sitecrest.io/
- BEM Systems — PMDB — https://bemsys.com/pmdb/ ; ETrak fact sheet — https://bemsys.com/wp-content/uploads/2025/11/BEM-ETrak-Fact-Sheet-2025_11.pdf
- EnviroCommand — https://envirocommand.com/
- ENFOS case studies (Hobson & Company ROI white paper; Casestudies.com customer cases: Kinder Morgan, Sunoco, ConocoPhillips) — https://enfos.com/white-papers/enfos-roi-environmental-remediation-obligations , https://www.casestudies.com/company/enfos/case-study/sunoco-customer-case-study , https://www.casestudies.com/company/enfos/case-study/conocophillips-customer-case-study , https://www.casestudies.com/company/enfos/case-study/kinder-morgan-customer-case-study

Sibling documents consulted: applications/contaminated-site-management.md (+ its research notes' boundary flags), applications/environmental-site-assessment.md.

Sourcing limitations: no deep help-center/user-guide documentation was reached for any sampled product (product pages and case studies only). All workflow detail in this pass is therefore at conceptual grain; no precise operational parameters (numeric limits, default values, exact status vocabularies) are asserted from vendor material. Case-study quotes are vendor-published marketing material, used only for structure confirmation, not for numbers.

## Product Observations

### ENFOS (finance-led; enterprise owner/operator)

Key observations (layer A unless noted):

- Positions as a **"purpose-built ERO system of record for the dual domains of remediation operations and accounting"** — Environmental Remediation Obligation = legal obligation to investigate, remediate, monitor, or restore contaminated soil/groundwater/surface water (ASC 410-30 framing).
- Platform structure: **Inventory** (identify & centralize all obligations), **Plan** (forecast, prioritize, budget), **Settlement** (manage, track, control project expenditures), **Assurance** (validate, audit, report).
- The obligation/project record centralizes **sites, vendors, documents, financial plans, costs, regulatory info** in one auditable platform.
- Spend drivers enumerated on the ERO page: chemicals of concern, geology/hydrogeology, site conditions, historical site use, regulatory standards and limits, regulatory pathway, planned future land use, institutional controls, **remediation strategy**, **cleanup phasing and work breakdown structure**, legal mandates (consent decrees), property value.
- Recognition drivers: contaminant concentrations exceed regulatory thresholds; liability reasonably estimable.
- Execution machinery (from case studies, A-): contractor **proposals → work authorizations → purchase orders → change orders → invoices**; "Procure to Pay" platform with real-time SAP interface and configured **work breakdown structure elements**; "eliminates unauthorized work"; spend tracked **by vendor, by project, by business** ("how much spend is authorized, how much committed through POs, how much spent out of those POs").
- Remeasurement loop: obligation remeasured each reporting period as new information emerges — updated sampling results, regulatory actions, changes in remediation plans, cost inputs, timing.
- Progress-to-closure language: obligations "managed toward site closure"; **closure criteria evolve over time** and must be integrated with the accounting framework.
- Audit trail: assumption history, roll-forwards, journal entries, supporting documentation; SOX/ASC reporting; ERP/GL integration.
- Scale: case studies describe portfolios of ~1,000+ remediation projects (Sunoco) and >30,000 sites (ConocoPhillips engagement scope) — vendor-published figures, structure only.
- Modules named in Sunoco case (A-): Technical Data Management, Document Management, Financial Management, Compliance Assurance, GIS.

### Locus EIM — Remediation (data & operations-led)

- "Manage multiple data streams **throughout your environmental remediation projects** and during subsequent **operation and maintenance (O&M) of remediation treatment systems**."
- **Task Management**: "Schedule specific tasks and track maintenance on all equipment."
- **Calculation Engine**: automate calculations "to measure and visualize performance."
- **Dashboards**: "instantly identify performance issues."
- **Data Upload**: analytical data uploads "with validation, error checking, multiple EDD formats, customized valid values."
- **Formatted Reports**: integration with TCEQ TRRP Commander for regulatory reporting (product-specific).
- Sampling optimization: "uses historical data and a statistical approach, optimizes wells being sampled, reduces frequency of sampling, and provides strong scientific evidence to support your remediation efforts."
- Framed as "Remediation & **Environmental Liability Management**" — same liability-management vocabulary as ENFOS, realized through data rather than accounting.
- Broader platform: GIS mapping, sample planning, mobile field data collection, permit tracking, cloud security/user management.

### EnFlection (Trihydro) (data-led; remediation + post-closure + operations)

- "Centralizes data into a **secure system of record**… supporting transparency across stakeholders… project needs including **site remediation, post-closure monitoring, active site operations**, carbon capture initiatives, and tracking of emerging contaminants."
- Regulatory frameworks named: **RCRA, CERCLA, State Programs, NPDES, UIC Class VI**.
- Data streams: groundwater, surface water, stormwater, leachate, soil sampling, air, field parameters, fluid levels, site characterization.
- Site decisions: interactive maps of sampling data by location; "monitor project activities, datasets, and key performance indicators in real time"; simultaneous team access.
- Data consistency: sampling planning ("avoid over-sampling"), defined standards and analytical criteria per sample event, metadata organization, synonym-based loading, **data validation flagging discrepancies**, notifications for significant data events.
- Analysis/reporting: query/filter/compare **against regulatory standards or customized thresholds**; saved queries shared team-wide; "reproducible, formatted tables and charts ready for reporting"; "consistent record of data, analyses, and reports to support team transitions".
- AI-powered natural-language queries restricted to the site's data (era-current).
- Security/governance: role-based access by site administrators, single-tenant Azure, MFA/SSO, full data ownership.
- Scale: single sites to corporate-wide portfolios.

### FieldFlō (contractor-side field execution)

- "Built by contractors for contractors… equips **environmental remediation professionals**" — one of several industry packs (demolition, asbestos abatement, masonry, concrete).
- Feature set: **Project Management** (day in the field, documentation, certificates), **Safety Management System**, **Dashboard/Reports**, **Time & Material tracking** ("automate your T&M tracking… automate change orders"), **CRM**, **Time Tracking & Payroll**, **Inventory/Equipment warehouse tracking**, **Online Training & Certificate tracking**, **Employee HR & skill tracking**, **Scheduling System** (interactive, SMS deployment populating timesheets), **Job Costing** ("upload estimates and see how your bids and actuals line up in real-time"), **Form Builder**, **Document Management**.
- Free Job Hazard Analysis (JHA) form for "site safety requirements before starting work on your environmental remediation projects."
- Framing: "environmental remediation projects are complex, often involving hazardous materials, strict regulations, and dispersed teams."
- Note: no chemistry/lab-data machinery, no monitoring-well analytics — the center is field operations and job economics.

### Secondary specimens (A-)

- **RemMS (PIR-a)**: "GIS based data management solution for remediation projects": soil quality data "for informed remediation and disposal decision-making"; AI correlation of field data "for real time decision making"; **field tickets, safety forms, daily site documentation**; "project management planning, justifications and decisions for planning transparency." Built by remediation project managers for remedial work "on behalf of the energy and industrial sectors."
- **EVX**: "manage every stage of site assessment and remediation in one platform… multiple investigations, contractors, and regulatory agencies… sampling data, remediation tasks, compliance deadlines, and budgets"; "connects tasks, time entries, and costs"; compliance deliverables tied to project phases.
- **Matidor**: map-centric consulting PM; "assessment sites, remediation zones, and reclamation properties plot automatically on interactive maps"; standardized remediation/ESA templates; offline mobile field capture with chain-of-custody; real-time budgets with threshold alerts; parent projects per site with subprojects per phase (Phase I → II → III remediation).
- **SiteCrest**: asset-owner portfolio oversight "from Phase 1 assessments through remediation completion"; "track all steps and stages of site environmental work"; "track environmental activity status and prioritize remediation investments… on divestment activities."
- **BEM PMDB**: web project dashboard for site assessment/investigation/remediation; central repository for project data; EDD auto-sync; query with regulatory or client-specific criteria; schedule tracking; work planning; tiered secure access "for client and regulatory stakeholders"; CSM deliverables.
- **EnviroCommand**: firm-level platform — projects, phases & tasks; compliance "tracked automatically… deadlines and filings… by state and project type"; remediation monitoring as a project type; client & regulator portals.

## Cross-product Comparison

| Structure | ENFOS | Locus EIM | EnFlection | FieldFlō | Secondary (A-) |
|---|---|---|---|---|---|
| Remediation project of record (bounded cleanup effort, persistent, identified) | ✔ (obligation/project + site + vendor + documents) | ✔ (remediation projects as data context) | ✔ (site/project system of record) | ✔ (per-project field ops) | ✔ all |
| Regulatory cleanup driver framing | ✔ ("regulatory action", standards, consent decrees) | ✔ (liability mgmt, TCEQ reporting) | ✔ (CERCLA/RCRA/state/NPDES/UIC) | ✔ ("hazardous materials, strict regulations") | ✔ (EVX, BEM, EnviroCommand) |
| Defined scope/completion: strategy, phasing, criteria, "done" | ✔ (strategy, WBS phasing, closure criteria) | ✔ (performance measures; sampling optimization toward goals) | ✔ (criteria/threshold comparison; project progress tracking) | ✔ (estimates→actuals; project completion docs) | ✔ (EVX phases, Matidor phase progression, SiteCrest stages) |
| Managed execution: tasks/phases/field work tracked | ✔ (work authorization→PO→change order→invoice; WBS) | ✔ (task management, equipment maintenance) | ✔ (project activities, workflows) | ✔ (scheduling, timesheets, T&M, safety forms) | ✔ (RemMS field tickets/daily docs; EVX tasks; BEM work planning) |
| Money: budgets, forecasts, actuals, POs, change orders | ✔ core | — (not featured) | — (not featured) | ✔ (job costing, T&M, change orders) | ✔ (EVX, Matidor) |
| Vendors/contractors | ✔ core (proposals, POs, vendor controls) | — | — | ✔ (crews, employees; CRM) | ✔ (EVX contractor coordination) |
| Monitoring/lab data (EDDs, wells, sampling events) | partial (technical data mgmt; sampling results as remeasurement inputs) | ✔ core | ✔ core | — | ✔ (BEM, QNOPY) |
| Treatment-system O&M / equipment maintenance | — | ✔ core | ✔ (active site operations) | partial (equipment/inventory tracking) | — |
| Progress vs criteria / performance evidence | ✔ (closure criteria, remeasurement) | ✔ (calculation engine, dashboards, performance issues) | ✔ (criteria comparison, KPIs) | ✔ (completion documentation) | ✔ |
| Regulatory reporting/deadlines | ✔ (compliance assurance, audit) | ✔ (TCEQ integration) | ✔ (formatted reports, frameworks) | partial (regulatory framing; safety compliance) | ✔ (EVX, EnviroCommand, BEM) |
| Documents & audit trail | ✔ core | ✔ | ✔ (system of record, data history) | ✔ (document management) | ✔ |
| Portfolio/multi-project scale | ✔ core (enterprise portfolios) | ✔ (multi-site) | ✔ (single site→corporate) | — (per-contractor) | ✔ (SiteCrest portfolio) |
| GIS/maps | ✔ (GIS module) | ✔ | ✔ (interactive maps) | — | ✔ (RemMS, Matidor, BEM) |
| Field safety machinery | — | — | — | ✔ core | ✔ (RemMS safety forms) |
| Financial-accounting integration (ERP/GL, reserves) | ✔ core | — | — | partial (payroll) | — |
| Mobile/offline field capture | — | ✔ (platform) | — | ✔ (field-oriented) | ✔ (Matidor, QNOPY) |

Reading: every product holds (1) a remediation project/obligation of record, (2) a defined scope/completion meaning, and (3) managed execution with recorded, attributed progress. Everything else is distribution-dependent: money and vendors are core at the owner/finance and contractor poles, absent at the data poles; monitoring data and O&M are core at the data poles, absent at the field pole; safety is core only at the contractor pole.

## Canonical Model (Abstraction Hierarchy)

### L0 — Defining Invariant (jointly held; each leg load-bearing)

1. **The remediation project of record** — an identified, bounded effort to remediate contamination at a specific site/medium, carried under a regulatory or legal cleanup driver, persistent across the project's multi-year (often decade-scale) life; holds scope, status, and history. Remove → task lists, spend ledgers, or data tables with no managed cleanup effort (generic PM / generic data tool).
2. **The defined end state** — the project carries what completion means: the remediation strategy/plan and its phasing, and the criteria that define "clean"/done against which progress and closure are judged. Remove → work management with no defined "done" (generic construction/professional PM).
3. **Managed execution with recorded progress** — the work advances through recorded, attributed actions: authorized work (proposals/work authorizations/POs/change orders where the pole carries them), planned phases and milestones, executed field work and tasks, completed actions — tracked as managed progress against the plan and reported to stakeholders/regulators. Remove → plan documents and invoices with no managed state (a file, not an application).

Binding: environmental remediation semantics — the object of work is contamination cleanup (media, contaminants, regulatory cleanup obligations), not structures or generic engagements. Remove the binding → generic construction PM (FieldFlō serves demolition/masonry/concrete with the same machinery) or generic professional-services PM.

Jointly-held test: 1 alone = a site file/obligation ledger; 2 alone = a plan document; 3 alone = generic task/field management; 1+2 without 3 = a bound plan nobody executes in-system; 1+3 without 2 = busywork with no closure test; 2+3 without 1 = template workflow not attached to any actual cleanup effort.

### L1 — Common Mature Structure

- **Money machinery** — budgets/estimates, forecasts, actuals, commitments, invoices; change orders as the standard response to scope evolution (core at owner/finance and contractor poles).
- **Vendor/contractor management** — proposals/bids, work authorization, vendor performance and spend control.
- **Monitoring & field data** — sampling events, wells/locations, lab EDD ingestion with validation, field logs/photos/mobile capture.
- **Performance & progress analysis** — trends, criteria/threshold comparison, KPIs/dashboards, sampling optimization.
- **Regulatory compliance & reporting** — framework tracking (CERCLA/RCRA/state programs or regional equivalents), deadlines/deliverables, formatted reports/submissions.
- **Documents & audit trail** — work plans, permits, reports, correspondence; attributed, defensible history.
- **Portfolio/program view** — many projects/sites with status, spend vs budget, stage; roll-up for owners.
- **GIS/maps** — sites, remediation zones, sample locations, progress in space.
- **Stakeholder surfaces** — client/regulator portals, transparency views, role-based access.

### L2 — Variant / Optional Structure

- Treatment-system O&M & equipment maintenance (remedy-type dependent: active systems vs MNA/monitoring-only)
- Waste/disposal streams (characterization, disposal decisions, manifests) — thin in this sample; belongs to waste-management Types
- Field safety machinery (JHA, safety forms, training/certificates) — contractor-side common
- Financial-accounting integration depth (reserves/roll-forwards/journal entries, ERP/GL, SOX-style audit posture) — owner-enterprise variant
- Public/agency program systems (register-side tracking of cleanup cases) — overlaps Contaminated Site Management's agency pole
- Mobile/offline-first field capture; AI-assisted querying/analysis (era-current)
- Consulting-firm operations integration (time/expense/invoicing, firm-level dashboards)

### L3 — Vendor-specific (Research Notes only)

- ENFOS's ASC 410-30/ARO accounting framing and "ERO flywheel" positioning; named modules (Inventory/Plan/Settlement/Assurance)
- Locus's TCEQ TRRP Commander integration; SOC-posture marketing
- EnFlection's AI smart queries; Class VI CCS data streams; vendor counters (500+ users, 38 states)
- FieldFlō's abatement/demolition industry family (CRM, payroll, HR/certificates)
- Case-study customer figures (portfolio sizes, ROI percentages) — marketing material, excluded from the final document

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit? Pre-software remediation projects were managed with: a work-plan binder (project of record + defined scope/criteria), field logbooks and daily reports (execution records), contractor invoices and approvals (execution/money), correspondence and progress reports to the agency (recorded progress + reporting). All three L0 legs are satisfiable without GIS, lab EDDs, ERP integration, or telemetry. Conversely, a modern SaaS feature such as AI querying or automated change-order generation is clearly era-current, not definitional. The definition does not overfit the current market.

## Vendor-specific Findings

- ENFOS is alone in making the accounting/obligation frame the spine (liability remeasurement, reserves, ERP/GL). Do not generalize "remediation management = liability accounting".
- Locus and EnFlection alone (of the primary sample) carry the treatment-system O&M emphasis; FieldFlō and ENFOS do not. O&M is remedy-type dependent.
- FieldFlō is alone in centering field safety and payroll; its remediation pack is one of several trades — evidence that the generic-PM machinery is not what defines this Type, the remediation binding is.
- Regulatory-framework vocabularies are regime-specific (CERCLA/RCRA/NPDES/UIC/US state programs named by EnFlection and BEM's ETrak NJ/LSRP extension); regional regimes shape vocabulary, not structure.

## Boundary Findings

**vs Contaminated Site Management** (the flagged seam): Contaminated Site Management centers the *site record and its cumulative evidence across the whole lifecycle* (investigation → remediation → monitoring → closure, retained register) — remediation appears there as a lifecycle phase plus data streams and tasks. This Type centers the *project as managed work*: authorizing, planning, executing, operating, and completing the remedy, with the execution machinery (work authorization, tasks/field ops, spend control, change management) and the money as first-class structures. Tests: remove the execution/money machinery and keep the site-evidence spine → Contaminated Site Management; remove the site-evidence spine and keep execution → this Type still stands (the ENFOS and FieldFlō poles carry no contamination-profile/evidence machinery). Overlap zone: products spanning remediation projects + O&M + site data (EnFlection, Locus EIM — the specimens named by the contaminated-site pass). Keep-both confirmed on the execution-vs-record seam.

**vs Construction Project Management**: remediation projects use construction-style machinery (schedule, budget, change orders, field crews, safety), but the object of work is contamination cleanup under regulatory cleanup drivers with completion defined by cleanup criteria/verification. A trade-tool like FieldFlō shows the machinery is generic; the remediation binding (media, contaminants, regulator-facing scope and closure) is what makes this a distinct Type.

**vs Environmental Site Assessment**: assessment is a bounded engagement producing a formal deliverable on existing conditions; remediation management executes the cleanup that assessment findings may trigger. Designed handoff: classified findings → remediation project of record (also visible in Matidor's Phase I→II→III phase progression framing).

**vs Environmental Monitoring Platform**: monitoring centers ongoing observation of facilities/parameters; here monitoring events are one evidence stream inside the project's progress-to-closure loop.

**vs Environmental Data Platform**: data-platform centers a cross-program data corpus without a project-execution lifecycle; here data exists to drive the managed project.

**vs Waste / Hazardous Waste Management**: disposal of remediation waste is a logistics concern inside a project; the waste Types center materials/waste logistics themselves. (RemMS mentions disposal decisions as a project output — supports keeping the seam.)

**vs Environmental Compliance Management / EHS platforms**: those center an organization's standing obligations and incidents; here the managed unit is the individual cleanup project moving to closure.

**vs ERP / Professional Services Automation / Spend platforms**: spend machinery appears here (owner pole), but attached to remedy scope, cleanup criteria, and site work with regulatory-facing closure — not generic engagements.

## Uncertainties

- The agency/register side (state/federal cleanup-program systems tracking remediation cases) was not directly examined this pass; it is claimed by the contaminated-site pass as its agency pole. If a distinct "remediation program/case" agency product class exists, it may straddle both Types — recorded as a possible future joint-review item, not resolved here.
- No deep help-center documentation was reached; workflow states (exact project/obligation status vocabularies, approval-chain depths, change-order mechanics) are documented at conceptual grain only.
- Non-US/regional markets (UK contaminated-land remediation, EU PPP framing) were not sampled; regional vocabulary differences are asserted only at framework-name level via vendor material (EnFlection's "State Programs", BEM's NJ/LSRP).
- Whether "environmental liability management" (Locus/ENFOS vocabulary) constitutes a separate buyer-centered Type vs this leaf's owner pole — treated here as a variant emphasis (finance-led pole), not a separate Type; flagged for the taxonomy owners if a future pass disagrees.

## Final Synthesis

Environmental Remediation Management is the remediation-program system of record: it holds each cleanup effort as a bounded, persistent project of record under a regulatory driver, carries that project's defined end state (strategy, phasing, completion/cleanup criteria), and manages execution toward it through recorded, attributed progress — authorized work, planned phases and tasks, executed field work and operations, evidence of performance, and the money and vendors that perform the work — reporting that progress to the regulators and stakeholders the project answers to. The market realizes this center from four poles — finance-led (owner obligation portfolios), data/operations-led (project data + O&M), contractor field-execution-led, and consulting-PM-led — and the Type is distinct from Contaminated Site Management (site-evidence record vs project execution) and from generic construction PM (remediation binding + regulatory closure semantics).
