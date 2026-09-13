# Research Notes — Building Commissioning Platform

## Research Goal

Understand what a Building Commissioning Platform actually is as an Application Type: what objects it manages, what workflow it drives, who uses it, and where its boundary lies against neighboring construction/facility Types (Construction Quality Management, Punch List Management, Construction Closeout Management, BMS/BAS, Building Energy Management, Building Condition Assessment).

## Initial Boundary

Initial hypothesis: commissioning (Cx) is the quality-assurance process that verifies a building's systems (HVAC, electrical, plumbing, controls, fire/life-safety) are planned, installed, tested, and performing per the Owner's Project Requirements (OPR). A Cx platform should systematize: equipment/system registers, checklists and functional tests, issue/deficiency logs, multi-party sign-off, and commissioning reporting. Nearest confusions: construction quality/punch-list tools (deficiency tracking overlap), closeout/handover tools (turnover overlap), and BMS (both "touch" building systems).

## Research Questions

1. What is the commissioning process the software supports (phases, artifacts, roles)?
2. What are the core objects (equipment, systems, checklists, tests, issues, documents)?
3. How do checklists vs functional tests differ in structure and execution?
4. How does the issue/deficiency loop work (origin → assignment → resolution → verification)?
5. Who uses it (Cx provider, GC, trade contractors, owner, engineers) and on what surfaces (field mobile vs office web)?
6. How do phases map (new construction vs existing-building/retro-Cx vs ongoing/monitoring-based Cx)?
7. What role do BIM/equipment schedules/BAS data play?
8. What is the deliverable (commissioning reports, final documentation, turnover)?
9. How do products speak to standards (ASHRAE Guideline 0, LEED, DGNB)?
10. Where is the boundary vs construction quality, punch list, closeout, BMS?

## Representative Products

| Product | Geography | Philosophy | Customer tier |
|---|---|---|---|
| CxAlloy | US | Asset-centric field execution platform; self-described "de facto standard in commissioning" | Cx firms of all sizes; enterprise (data centers, healthcare, life sciences) |
| CxPlanner | EU (Denmark) | Test planning + system/test oversight; AI agents (CxAI); data centers & industrial | Cx teams, hyperscale data centers, oil & gas, industrial |
| Facility Grid | US | "Lifecycle Commissioning" — construct → validate → sustain; enterprise, mission-critical | GCs, owners, Cx providers, data centers (hyperscale/colocation) |
| Bluerithm | US | Flexible checklist/form-driven platform configured around each firm's process | Small-to-mid Cx firms, owners, industrial teams |

Peer set confirmed by the products themselves: CxPlanner names CxAlloy, Bluerithm, Facility Grid as competitors; Facility Grid's FAQ compares itself to CxAlloy, Bluerithm, CxPlanner.

**Product Mismatch (drift):** BuildPulse (buildpulse.io) was a known commissioning-software name but the live site (fetched 2026-09-06) is now a CI/flaky-test/analytics product for engineering teams. Excluded from the sample; recorded as a market drift observation.

## Sources

All fetched 2026-09-06:

- CxAlloy — https://www.cxalloy.com/ (product pages: asset management, issue logging, checklists & tests, tracking & reporting, security) — Tier 1/2
- CxAlloy Support KB — https://support.cxalloy.com/ (collection structure: TQ — Assets, Checklists, Tests, Templates, Lines, Issues, Reviews, Reports, Meetings, Tasks, Files, Milestones, API, COBie, Power BI, Procore, FM Imports; TQ iOS — Equipment, Issues, Checklists, Tests, Field Observations, Syncing; CxAlloy FM) — Tier 1
- CxPlanner — https://cxplanner.com/ (product pages: system & test view, checklists for Cx and QA/QC, punch list & issue management, planning & scheduling, dashboards, template center, CxAI, 3D model viewer) — Tier 1/2
- CxPlanner Commissioning 101 — https://cxplanner.com/commissioning-101 (process vocabulary: OPR, BoD, Cx log, FPT, IST, PFC, retro-Cx, ASHRAE Guideline 0, LEED v4, DGNB, TAB, CxA, data-center Level 1–5 testing, BCxP/QCxP certificates) — Tier 2 (vendor educational)
- Facility Grid — https://www.facilitygrid.com/ (Lifecycle Commissioning; FG Construct/Validate/Sustain; FAQ defining commissioning management software and operational readiness; integrations) — Tier 1/2
- Bluerithm — https://www.bluerithm.com/ and https://bluerithm.com/building-commissioning-software/ (equipment-centered Cx: equipment lists, PFC/FPT/IST forms, issues, drawings markup, dashboards, report builder, meetings, AI tools, integrations) — Tier 1/2
- BuildPulse — https://buildpulse.io/ (pivot evidence only)

No help-center article bodies were fetched beyond the CxAlloy KB index; no numeric limits, default values, or pricing details are asserted anywhere in the final document.

## Product A — CxAlloy

### Key observations (Layer A unless noted)

- Positioning: "Cx software built for the field"; "the de facto standard in commissioning"; used in 35+ countries; multi-language.
- **Asset-centric data model**: "structures commissioning around the asset, creating a single, connected data model across equipment, systems, spaces, and buildings. Every checklist, test, issue, document, and report is directly linked… full traceability from installation through final turnover."
- Asset management: full asset hierarchy (equipment → systems → facilities), custom attributes, workflows, status tracking, bulk import/export, label/nameplate scanning via device camera, historical data retained across projects and portfolios.
- **Issue logging & resolution**: issues originate from field observations, checklists, tests, and meetings; automatically tied to assets; assigned to responsible parties with due dates and notifications; observations can be promoted into formal issues; filtering by discipline, phase, priority; lifecycle tracking from identification to closeout.
- **Checklists & tests**: template-based, reusable, push updates across active workflows; custom line types, tables, structured inputs; assignable to users, roles, or companies; executed in field or office; issues auto-generated from results; multiple test attempts with full audit history.
- Reporting: automated report generator (commissioning reports with photos, issue logs, asset data, documentation), real-time dashboards, milestones (goals computed from live project data), ad-hoc reporting, white-labeled/branded reports.
- Mobile: native iOS/Android, fully offline with automatic sync, photos/notes/files captured in the field.
- Collaboration: unlimited users, granular role-based permissions; SSO (SAML), RBAC, ISO 27001, SOC 2 Type II.
- KB object vocabulary (support.cxalloy.com): Accounts, Projects, **Assets**, Checklists, **Tests**, Templates, Lines, Issues, Reviews, Reports, Meetings, Tasks, Files, Milestones, API; iOS app adds **Equipment**, **Field Observations**, Syncing. Separate products: CxAlloy TQ (commissioning), CxAlloy Q5 (AEC quality — evidence the vendor separates Cx from construction quality), CxAlloy FM (facility management companion; FM Imports).
- Integrations: Procore, Autodesk, COBie, Power BI, API.

## Product B — CxPlanner

### Key observations

- Positioning: "the fastest commissioning software ever built"; targets "Cx teams frustrated with CxAlloy, Bluerithm, Facility Grid and Excel."
- **System & Test view**: "detailed insight and overview across all equipment and their testing process" — equipment-centric test tracking.
- **Test taxonomy**: checklists for "PFC, FPT and Cx" (pre-functional checklists, functional performance tests); IST (integrated system testing) covered in educational content; mobile/tablet/desktop execution.
- **Planning & scheduling**: Gantt-style test planning — "Never miss a functional test again… keep track of your subcontractors' work"; timeline/schedule by level; dependencies.
- Punch list & issue management: 10 to 10,000 items; issue markup on drawings; site walks with drawings as layers, observations placed on drawings.
- Template center; QR code generator; meeting module; dashboards & analytics; review & markup files; 3D model viewer.
- CxAI: checklist generator, P&ID tag extraction, "ask your specs" documentation Q&A, photo recognition, automated real-time reporting, file insights, MCP integration.
- Industries: construction projects, data centers/hyperscale (Level 1–5 testing, Uptime tiers), oil & gas/renewables onshore/offshore, industrial & mechanical manufacturers.
- Separate product line: **Completion Management Software (CCMS)** for "large scale industrial projects, data centers, power plants… with 1000+ assets and instruments" — evidence that industrial completion is treated as a distinct (adjacent) product category by the same vendor.
- Educational "Commissioning 101": OPR, BoD, Cx log, FPT ("the critical milestone… where theory meets reality"), IST, retro-commissioning, ASHRAE Guideline 0, LEED v4, DGNB, TAB, commissioning agent (CxA), certificates (ASHRAE BCxP, UW-Madison QCxP). Cost framing: "often estimated to be 0.5% to 2% of construction costs" (vendor-stated empirical range — kept out of final doc).
- Clients shown: Equinix, CBRE, BCxA, CSA, AABC, ACG.

## Product C — Facility Grid

### Key observations

- Positioning: "Lifecycle Commissioning® software… built for a building's full life, not just its turnover"; mission-critical buildings (data centers, hospitals, universities, airports); 8,000+ projects claimed.
- Three modules: **FG Construct** (commissioning, quality control, operational readiness of complex building systems; asset readiness tracking; streamlined turnover), **FG Validate** ("autonomous commissioning for building automation systems… continuous QA & Cx testing; drift & energy waste detection"; BAS integration), **FG Sustain** (energy audits, annual emissions reporting, AI document processing).
- **Vendor's own definition (FAQ)**: "Commissioning management software digitizes the entire Cx process — checklists, functional performance tests, punch lists, issue tracking, and report generation. Field teams complete work via mobile app, data syncs in real time, and all project stakeholders can view status and generate reports without manual coordination or spreadsheets."
- **Vendor's own boundary statement**: "Commissioning (Cx) is the process of verifying that building systems are installed and functioning correctly. Operational readiness is broader — it ensures that systems, documentation, O&M personnel, and Cx records are all ready for the transition to sustainable building operations. Commissioning is a component of operational readiness."
- Who it helps: building owners ("see the status of building assets, Cx processes, and QC activities against the project schedule"), commissioning providers ("run your entire Cx process in one platform"), general contractors ("track, verify, and manage building assets throughout the construction lifecycle"), trade contractors ("capture and share essential equipment and system information").
- Integrations: Procore (native bidirectional sync surfacing asset status, QA/QC, Cx activity inside Procore), Bluebeam (markup/punch), Autodesk Construction Cloud, Maximo (CMMS turnover; native mobile app), open API (REST + webhooks).
- Data-center emphasis: "verify every asset — at scale… streamline functional performance testing and eliminate reporting bottlenecks."
- Blog framing: "7 Reasons Teams Replace Commissioning Spreadsheets" — the incumbent being displaced is the spreadsheet/binder workflow.

## Product D — Bluerithm

### Key observations

- Positioning: "Commissioning Management Software — digitize and streamline your checklists, documentation, and communication"; 30k+ users; flexible/configurable ("the only platform that can truly be customized to adapt to your unique process").
- **Equipment-centered**: "Keep Equipment at the Center of the Commissioning Process" — import equipment schedules, organize thousands of equipment assets, automatically associate equipment with forms, tests, issues, documentation, and status; folders, grouping by type, customizable naming.
- **Form taxonomy**: installation checklists, pre-functional checklists (PFC), functional performance tests (FPT), integrated systems tests (IST), site observation forms, design review checklists, LEED commissioning forms; forms support "equations, validation, attachments, signatures, automatic issue creation, and real-time completion tracking."
- **Issues**: "Manage deficiencies, observations, punch items, and commissioning issues from identification through resolution"; centralized issue log; assignment, due dates, photos, comments, complete issue history; issues created directly from forms/tests; open/closed dashboards.
- Drawings: PDF markups and pins connecting issues/equipment to floor plans and schematics.
- Dashboards: project and portfolio level (campuses, portfolios, clients); progress, open issues, overdue work, testing status, equipment status, milestones; shareable dashboard links.
- **Report builder**: progress reports, issue reports, site observation reports, functional testing reports, equipment reports, final commissioning reports — generated from live project data; reusable report templates; reports "hundreds and thousands of pages long."
- Meetings: agendas, attendees, notes, decisions, action items tied to project data.
- Scope claims: "the entire commissioning process and documentation requirements from pre-design through closeout… reporting, issues logs, testing documentation, pipeline tracking."
- Template scope: new construction, existing building, retro-commissioning, monitoring-based commissioning, LEED commissioning, HVAC, electrical, BAS, IST.
- AI tools: generate installation checklists, PFCs, FPTs (from screenshots of sequences of operation), LEED checklists, equipment lists (from equipment-schedule screenshots with column mapping), user imports.
- Integrations: Procore (Observations ↔ Issues sync), Autodesk Construction Cloud (Issues sync), Revit (export to Bluerithm), Willow digital twin (equipment/property sync), API, MCP server.
- Stakeholders: commissioning providers, building owners, construction teams, trade contractors, facility teams ("receive organized equipment records, testing documentation, issue histories, and closeout information").
- Boundary quote (customer): "this platform is designed for commissioning. A lot of the other platforms that we looked at were designed for construction, which is completely different. Mechanical installations are a whole different ball game."

## Cross-product Comparison

| Dimension | CxAlloy | CxPlanner | Facility Grid | Bluerithm |
|---|---|---|---|---|
| Central object | Asset (equipment/system/space/building hierarchy) | Equipment + System & Test view | Building assets/systems ("asset readiness") | Equipment (explicitly "at the center") |
| Verification activities | Checklists + Tests (template-driven, multiple attempts, audit history) | PFC / FPT checklists + test planning | Checklists, FPTs, QC activities; continuous Cx testing (FG Validate) | Installation checklists, PFCs, FPTs, ISTs, site observations, design reviews |
| Issue loop | From observations/checklists/tests/meetings → tied to assets → assign → resolve → closeout | Punch list & issues; markup on drawings; auto follow-up | Punch lists, issue tracking; dashboards | Deficiencies/observations/punch items → assign → due dates → history → close |
| Multi-party roles | Users/roles/companies; granular permissions | Team + subcontractor tracking | Owners, Cx providers, GCs, trade contractors | Cx providers, owners, construction teams, trade contractors, facility teams |
| Field execution | Native iOS/Android, offline sync, label scanning | Mobile/tablet/desktop apps | Mobile app, real-time sync | Phones/tablets/PCs, offline-capable |
| Templates | Reusable checklist/test templates, push updates | Template center | Standardized processes | Reusable project/equipment/checklist/test/dashboard/report templates |
| Reporting | Automated report generator, white-label, milestones | Automated real-time reporting, dashboards | Reporting at scale ("eliminate reporting bottlenecks") | Report builder from live data; progress/issue/site-visit/FPT/final reports |
| Meetings | Meetings module | Meeting module | — (not surfaced on fetched pages) | Meetings module (agendas, decisions, action items) |
| Drawings/BIM | — (not surfaced on fetched pages) | Issue markup on drawings; 3D model viewer | Bluebeam markup | PDF markups & pins; Revit export |
| Construction-platform integration | Procore, Autodesk, COBie, Power BI, API | Power BI; 3D viewer | Procore native bidirectional, ACC, Maximo, API | Procore, ACC, Revit, Willow, API, MCP |
| Beyond construction phase | CxAlloy FM (FM imports) | Operational readiness product line | FG Validate (autonomous Cx, BAS), FG Sustain (energy audits, emissions) | Monitoring-based Cx templates; existing-building/retro-Cx |
| Standards/certification angle | — (not surfaced) | ASHRAE G0, LEED, DGNB educational content | — | LEED fundamental/enhanced Cx forms & AI checklists |
| AI | — (not surfaced on fetched pages) | CxAI (checklist gen, P&ID extraction, spec Q&A, photo recognition, MCP) | AI document processing (FG Sustain) | AI checklist/PFC/FPT/equipment-list/user generation; MCP server |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the software stops being a commissioning platform:

1. **Building systems/equipment as identified records** — the objects being verified exist as individually identified records (equipment, systems), organized under the building/project.
2. **Structured verification activities bound to those records** — checks and tests (installation verification, pre-functional checklists, functional performance tests) are executed and recorded against specific equipment/systems.
3. **Recorded results and a deficiency loop** — each activity produces recorded outcomes; failures/observations become tracked issues assigned to responsible parties and carried to resolution.
4. **Accumulated verification evidence and reporting** — the recorded activities, results, photos, documents, and sign-offs assemble into the commissioning deliverable (progress and final commissioning reports, turnover documentation).

Remove the equipment/system records → generic checklist app. Remove the verification/test structure → punch-list tool. Remove the issue loop → static form collector. Remove evidence/reporting → not commissioning (no deliverable proving the building works).

### L1 — Common Mature Structure

- Asset hierarchy: building → system → equipment (→ components), with spaces; bulk import from equipment schedules / Revit / spreadsheets.
- Template library: reusable checklist/test/report templates per equipment type and project type; template governance across a firm.
- Test taxonomy: pre-functional checklists (PFC), functional performance tests (FPT), integrated systems tests (IST), site/field observations, design review checklists.
- Issue lifecycle: created from tests/checklists/observations; assigned to responsible party (usually a contractor); due dates, comments, photos; verification and closure; open/closed tracking.
- Multi-party collaboration with role/company-scoped permissions (Cx provider, GC, trade contractors, owner, engineers).
- Mobile field execution with offline support, photos, and (in some products) nameplate/label scanning.
- Progress dashboards and milestones computed from live data.
- Automated report generation (progress, issue, site-visit, final commissioning reports), often white-labeled.
- Meetings module (agendas, minutes, decisions, action items tied to project data).
- Document management: drawings with markup/pins, submittals, O&M docs, attachments on every object.
- Integrations: construction management platforms (Procore, Autodesk Construction Cloud), design tools (Revit), CMMS handoff, open API.
- Audit history on records.

### L2 — Variant / Optional Structure

- **Phase scope**: new-construction Cx vs existing-building/retro-commissioning vs ongoing/monitoring-based commissioning vs operational readiness framing.
- **Autonomous/continuous commissioning**: BAS integration, continuous QA/Cx testing, drift and energy-waste detection (observed in Facility Grid FG Validate; monitoring-based Cx templates in Bluerithm). Product-specific posture — optional.
- **Certification support**: LEED fundamental/enhanced Cx forms, DGNB references, ASHRAE Guideline 0 alignment (educational + template level).
- **Industry extension**: data centers (Level 1–5 test programs), industrial/oil & gas completion, energy/BESS/solar, healthcare, government, schools.
- **Energy/sustainability modules**: energy audits, emissions reporting (Facility Grid FG Sustain).
- **Operations handover depth**: FM imports, COBie, CMMS turnover (CxAlloy FM, Facility Grid→Maximo).
- **Planning depth**: Gantt scheduling of tests, workload planning, dependencies (CxPlanner).
- **AI assistance**: checklist/PFC/FPT generation, equipment-schedule import, spec Q&A, photo recognition (CxPlanner, Bluerithm; increasingly common).
- **Deployment/security posture**: SaaS multi-tenant; SSO/SAML, RBAC, SOC 2 / ISO 27001 at enterprise tier.
- **Surface extras**: 3D model viewer, QR codes, digital-twin sync.

### L3 — Vendor-specific (kept out of final document)

- CxAlloy: TQ/Q5/FM product split, Milestones object, COBie/Power BI integrations, label scanning, "de facto standard" claim, 35+ countries claim.
- CxPlanner: CxAI brand and feature names (P&ID Tag Extraction, Ask CxAI, MCP Integration), CCMS completion product line, Level 1–5 test-plan tooling, V-model content, founder credentialing content, time-savings comparison table vs Excel.
- Facility Grid: "Lifecycle Commissioning®" trademark, FG Construct/Validate/Sustain naming, "autonomous commissioning" concept, Procore-native bidirectional sync, Maximo native app, 8,000+ projects / 25% admin-reduction claims.
- Bluerithm: Claude Cowork integration, Willow digital-twin sync, form matrix, ROI calculator, 30k+ users claim, free-template library specifics.

## Boundary Findings

- **vs Construction Quality Management**: Cx verifies that building *systems perform* per requirements (does the building work); construction QC verifies that *work complies with specs* (was it built right). Overlap: checklists, issues, punch items. Evidence of the seam: CxAlloy ships Q5 (AEC quality) as a separate product from TQ (commissioning); a Bluerithm customer states Cx platforms are "designed for commissioning" while other platforms are "designed for construction, which is completely different." Remove the equipment/system verification loop and keep generic work-compliance checklists → Construction Quality Management.
- **vs Punch List Management**: punch items are one issue type inside Cx; the Cx issue log is bound to equipment/systems and test outcomes, and the platform's center is the verification loop, not the deficiency list. Remove tests/equipment and keep the deficiency list → Punch List Management.
- **vs Construction Closeout Management**: commissioning is a component of closeout; closeout spans broader deliverables (warranties, as-builts, O&M, training). Cx platforms extend into turnover (Facility Grid "streamlined turnover", Bluerithm "closeout information") but the core is verification evidence. Remove verification and keep turnover deliverables → Closeout Management.
- **vs Building Management System / BAS**: BMS controls the building in operation; the Cx platform verifies and documents. Monitoring-based/autonomous Cx *reads* BAS data (FG Validate) but does not control. Remove verification records and add control loops → BMS.
- **vs Building Energy Management**: energy platforms optimize/monitor consumption; Cx platforms prove systems meet requirements. Energy audits/emissions (FG Sustain) are an L2 extension. Center on energy → Building Energy Management.
- **vs Building Condition Assessment**: condition assessment surveys existing condition/facility condition (FCA); retro-Cx verifies performance against requirements through tests. Center on condition survey → Building Condition Assessment.
- **vs Construction Field Management / Daily Logs / RFIs**: field management covers daily construction operations; Cx covers system verification. Bluerithm customer quote supports the separation.
- **vs Industrial completion management (CCMS)**: CxPlanner sells a separate Completion product for 1000+ asset industrial/data-center programs — industrial completion is an adjacent sibling, not this Type's center. The Building Cx Platform centers on buildings' systems.
- **"去掉什么就变成另一个 Type" 判据**: remove equipment/system records → generic forms/checklist app; remove tests → punch list; remove issue loop → static forms; remove evidence/reporting → not commissioning; add control loops → BMS; center on work-compliance → construction QC.

## Historical / Market-Sample Check

- Pre-software commissioning ran on paper checklists, spreadsheets, and binders ("more efficient than paper and binders" — Bluerithm customer; "7 Reasons Teams Replace Commissioning Spreadsheets" — Facility Grid). The L0 (equipment records + verification activities + issue loop + evidence) describes the paper-era Cx log equally well — the software digitizes it; it does not define it by modern features.
- Regional breadth: EU products (CxPlanner; DGNB, V-model vocabulary) and US products (ASHRAE/LEED vocabulary) fit the same core; data-center Level 1–5 programs fit as an industry variant.
- Ongoing/monitoring-based Cx (continuous BAS-driven testing) still satisfies L0 — the "activity" becomes continuous analysis, recorded against equipment, producing issues and evidence. Classified as a variant posture (L2), not a separate Type.

## Uncertainties

- Help-center article bodies were only partially reachable (CxAlloy KB index fetched; article bodies not). Object-level workflow details (e.g., exact test-attempt state machines, exact permission matrices) are therefore kept qualitative.
- Facility Grid's KB (facilitygrid.com/kb/) was not fetched; FG Validate's "autonomous commissioning" mechanics are known only from marketing-level description — kept as optional/variant with no operational claims.
- CxPlanner help center (help.cxplanner.com) not fetched; CxAI capabilities known from product pages only.
- No pricing, numeric limits, or default values asserted anywhere.
- Market-size/leader claims (CxAlloy "de facto standard", user/project counts) are vendor claims, recorded as claims only.

## Final Synthesis

A Building Commissioning Platform is the system of record for the building commissioning process. Its world is built around the building's systems and equipment as identified records; verification activities (installation checks, pre-functional checklists, functional performance tests, integrated systems tests) are bound to those records and executed largely in the field; recorded results surface deficiencies that are tracked through assignment and resolution; and the accumulated evidence assembles into the commissioning reports and turnover documentation that prove the building works as required. Mature products add template governance, multi-party role models, mobile/offline field execution, dashboards, automated reporting, meetings, drawings markup, and construction-platform/CMMS integrations. Variants extend the Type across phases (new construction, existing-building/retro, ongoing/monitoring-based), industries (data centers, healthcare, industrial), and adjacent missions (operational readiness, energy audits, autonomous BAS-driven testing). The sharpest boundaries: construction quality management (work compliance vs system performance), punch list management (deficiency list vs verification loop), closeout management (turnover deliverables vs verification evidence), and BMS (control vs verification).
