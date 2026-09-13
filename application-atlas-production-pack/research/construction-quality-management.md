# Research Notes — Construction Quality Management

## Research Goal

Understand what "construction quality management" software actually is as an Application Type: what objects it holds, who performs and accepts quality work, how the quality process runs from planned inspection through non-conformance correction to verified acceptance, and where it begins and ends relative to the neighboring construction leaves (Field Management, Punch List, Safety, RFI, Project Management, Property Inspection, Manufacturing QMS).

## Initial Boundary

Working hypothesis at start:

- Construction Quality Management is the **conformance-process layer** of construction software: verifying that construction work conforms to the project's requirements (contract documents, specifications, drawings, codes) and managing correction of what doesn't.
- Expected core objects: inspection/checklist records, non-conformance / deficiency records (NCRs, defects, observations), acceptance/sign-off acts, planned inspection regimes (ITPs, hold points), and quality analytics.
- Nearest neighbors: Construction Field Management (already processed — owns the day record + general field work items), Punch List Management (unprocessed sibling), Construction Safety Management, Construction Project Management, RFI Management, Property Inspection Application, Manufacturing QMS / CAPA Management, Audit-style generic inspection platforms.
- Main risk: **overlap with Construction Field Management's "field work item tracked to verified completion"** — the deficiency register is shared machinery; the L0 must be drawn so quality owns the *conformance loop* (inspection against requirements + managed correction), not general site execution.

## Research Questions

1. What objects exist in a construction quality product: templates, inspections, checklists, observations, NCRs/defects, quality plans, sign-offs, test data?
2. What is the core loop: plan → inspect → record → raise non-conformance → assign/fix → reinspect → verify/accept → close → analyze?
3. Who performs inspections and who accepts (QC staff, superintendent, subcontractor, owner, third-party inspector)? How does the two-sided verification work?
4. How is the process anchored to requirements (specs, contract documents) and to the project (locations, drawings, work stages)?
5. What quality-specific machinery exists beyond generic issue tracking: ITPs, hold/witness points, blocking, verification methods, disposition?
6. How much of the machinery is shared with safety/environmental checklists (one engine, two regimes)?
7. What did construction quality management look like before software (historical/market-sample check)?
8. How do vendors position "quality" vs "punch" vs "safety"?

## Representative Products

Selected for market representativeness, documentation depth, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence depth |
|---|---|---|---|
| Procore | Enterprise platform; Quality & Safety as one tool group (Inspections, Observations, Action Plans, Punch List) inside the project suite | Enterprise GC / owner | Tier-1 support docs, deep (tool landing pages + permissions) |
| FTQ360 | Quality-specialist standalone ("First Time Quality"); QAQC program platform: QAQC plans, hold points, defect prevention analytics | Mid/large GCs, homebuilders, factory-built housing, oil & gas, renewables/power delivery | Tier-2 product pages, rich (vendor-positioned) |
| PlanRadar | Defect-documentation-first platform (plans + tickets + templates), multi-industry (construction, real estate, FM, fire safety), European | SMB–mid-market contractors, developers, inspectors | Tier-2 product pages (platform level) |

Market anchors acknowledged but **not directly documented this run**: Autodesk Construction Cloud (autodesk.com 403 — consistent with two sibling runs the same week; abandoned after one attempt per network rules), SafetyCulture (generic inspection platform, out of construction scope), residential builders' quality tools (Buildertrend etc.), and dedicated ITP tools. No claims are made from these.

## Sources

Research date: **2026-09-07**

- Procore — https://support.procore.com/products/online/user-guide/project-level/inspections (Inspections tool: templates, schedules, mobile performance, signers, close, reinspect, observations-from-inspection, related items, locations, photos, exports, permissions)
- Procore — https://support.procore.com/products/online/user-guide/project-level/observations (Observations tool: scopes "quality, safety, commissioning, warranty, and work to complete"; create/respond/resolve/close/reject; templates; types; quality vs safety categories)
- Procore — https://support.procore.com/products/online/user-guide/project-level/action-plans (Action Plans tool: ITPs/quality plans, verification methods, blocking functionality, signatures, Plan Manager/Assignee/Approver/Receiver roles, approve-before-perform, create-by-location/asset)
- FTQ360 — https://www.ftq360.com/ and https://www.ftq360.com/construction-quality-management-software/ (six essential QAQC functions: deficiency/NCR/punchlist reports, daily progress reports, checklist inspections 750+ templates, field data collection incl. measurements/OCR/GPS, project-specific QAQC plans with hold points and progress tracking, proactive defect prevention / vendor first-time-quality analytics)
- PlanRadar — https://www.planradar.com/us/ (construction quality positioning: defect management & punch lists, inspections/checklists/safety audits, handovers, evidence collection; templates; plan pinning; free subcontractor/watcher participation; multi-industry scope)

Source-access limitations: autodesk.com / Autodesk Construction Cloud documentation returned 403 (consistent with the construction-document-management and construction-field-management runs of the same week); abandoned after one attempt. planradar.com quality-specific landing page 404 (platform root fetched instead — PlanRadar evidence is platform-level, not a dedicated quality-module page). FTQ360 evidence is Tier-2 vendor positioning (rich but marketing-shaped); no Tier-1 help center fetched this run. Findings relying on weaker evidence are qualified below.

## Product A — Procore

### Key observations (Layer A — support-site content unless noted)

- **Inspections tool**: "comprehensive set of boilerplate inspection checklists that can be reused and customized on individual construction projects." Template levels: **company** and **project**. Templates divide into **sections + line items** capturing "every specialized requirement associated with each inspection type"; **conditional logic** on items (Dec 2024 release); templates that **require photos and observations**; alphanumeric numbering; bulk creation (open beta, 2025).
- **Inspection schedules**: create/edit/delete/search schedules (including **by equipment**, Jan 2025 release); view schedules.
- **Performing**: create an inspection from a template, perform on **web and mobile** (per-item responses, comments, attachments, photos that populate the project Photos tool), **add signers to an inspection**, **sign a completed inspection**, **close an inspection**, **create reinspections** of closed inspections (Aug 2025 release), create an **Observation from an inspection**, add a **related item**, create **inspections on a drawing** (iOS), create from a **location** (Android), maps support.
- **Template library spans regimes**: quality checklists (pre-pour, pre-drywall, pre-roofing, pre-backfill — from third-party contributors OAC Management Inc. / NextWave), safety (OSHA trenching, lockout/tagout, materials handling), site safety inspection, environmental (SWPPP stormwater), equipment pre-operation, jobsite cleanliness — **one checklist engine serves quality, safety, and environmental regimes**.
- **Observations tool**: "Observations can encompass scopes of work including **quality, safety, commissioning, warranty, and work to complete**. This tool is used to assign tasks to other project team members at any phase in the project lifecycle." Create (also from photos/models/inspections/locations, Quick Capture), set due date, distribute with email notifications, assignees **view/respond/complete** from mobile, monitor by status and type, real-time history/activity feeds, **reject an observation**, **close an observation** (superintendent), **create a Change Event from an observation** (cost linkage), observation **types** and **templates**, **separate observations into quality and safety categories** (Nov 2025 release), drawings/models/locations linkage, granular permissions.
- **Action Plans tool** (the planned-quality machinery): "plans outlining critical milestones that represent **the standards of quality** for their defined scopes of work... maintaining a high degree of accountability by preserving records of work completed and **documenting the approval from responsible parties** for that completed work." Explicitly positioned to "streamline processes such as **Inspections & Test Plans (ITPs), quality assurance plans, concrete pour plans, project startup plans, safety plans**." Mechanics: company/project templates; create by location or by **asset**; **approve an action plan before it can be performed** (Approver role; approve on behalf of another user within same company); **verification methods** per item (default set documented); **blocking functionality** (item must be completed before the plan can progress); **required signatures**; item status updates by assignee; roles: **Plan Manager, Assignee, Approver, Receiver**; sign items and sign the completed plan as Receiver; request records (documents/tests) on items; link Assets; PDF export; custom reports.
- Cross-object machinery: related items across tools; photos → project Photos tool; multi-tiered locations shared across tools; granular per-tool permissions (None/Read Only/Standard/Admin + granular); collaborator model gives subcontractors scoped mobile participation.

## Product B — FTQ360

### Key observations (Layer B — vendor product pages; Tier-2, vendor-positioned)

- Self-positioning: "Inspection and QAQC Software for Quality Project Delivery"; brand = "First Time Quality" (defect prevention over detection). Segments: construction, homebuilding, factory-built housing, oil & gas, renewable energy / power delivery. Adjacent safety app offered separately.
- **Six essential QAQC functions** (vendor's own taxonomy):
  1. **Deficiency and work-to-complete punchlist reports** — "document issues found at all stages of project delivery, communicate them to responsible parties, and ensure issues are corrected." Documented issue kinds include design issues found in pre-construction reviews, construction deficiencies, equipment/system performance issues during startup and commissioning, customer/quality issues at turnover, **RFIs, Change Orders, Non-conformance Reports (NCR)**, and **importing Excel punch lists from any source**. Accountability framing: "consistent process for tracking and assigning accountability for correcting deficiencies"; identify recurring issues.
  2. **Daily progress reports** — day-anchored record with photos/videos, manpower/subcontractor/equipment/material receipts, weather, delays (overlaps Construction Field Management; present here as a quality-support function).
  3. **Checklist inspections** — "proof positive that inspected work meets project requirements"; **library of over 750 customizable checklist templates** covering pre-construction document review of specifications/drawings, vendor/subcontractor qualification, completion of work tasks, QC review of phases/milestones, systems startup; "documented compliance with project requirements... enhanced supplier and subcontractor accountability."
  4. **Field data collection** — digital forms for technical inspection data: concrete delivery sample measurements, material delivery quality/condition, HVAC startup measurements, equipment serial numbers, key dimensions of formwork/foundation/framing, GPS location, **OCR capture of measurement-device screens**, **capture and acceptance of third-party inspection test reports**, commissioning performance testing.
  5. **Project-specific QAQC plans** — "itemize required inspections, tests, and **hold points**... automated progress tracking shows which tests and inspections have been completed and which ones are still to come." Plan contents listed by the vendor: drawing/spec review, vendor and subcontractor qualification reviews, personnel qualification, factory acceptance tests, checklist inspections, milestone inspections, **surveillance inspections by independent inspectors**, **hold points for customer approval to proceed**, periodic quality and safety audits, **independent inspections by code officials and other third parties**, handover/closeout. "Schedule inspections and assign them to inspectors"; look-ahead dashboards; exception alerts; "meet customer requirements for project-specific construction quality control plan submittals."
  6. **Proactive quality assurance and risk management** — identify potential problems from **historical deficiency data**, apply lessons learned, **review vendor first-time-quality performance** ("disqualify subpar vendors"), add checkpoints/initial inspections to prevent known risks, monitor deficiencies in real time; supports six-sigma/lean/zero-defect programs.
- Platform claims: operates across hundreds of projects / thousands of inspections; **online and offline with automatic syncing**; integrations synchronizing projects/vendors/users; direct database connections for Excel/Power BI; cybersecurity compliance.

## Product C — PlanRadar

### Key observations (Layer B — platform root page; platform-level, not a dedicated quality-module page)

- Positioning: "Construction & Building Condition Assessment Platform — field management, simplified"; multi-industry: construction, real estate, facility management, fire & life safety. For general contractors: "**Build it right, first time** — ensure construction quality and reduce rework to deliver projects on time and on budget," with capability tiles: **defect management & punch lists**, daily logs, **inspections, checklists & safety audits**, handovers, evidence collection & claims management.
- Structure visible on the platform: projects with **plans/BIM** and **document management**; site users record **defects/tickets pinned to plans** (the product's heritage is defect documentation — its Android package is literally named "defectradar"); **customizable templates** adapting to existing processes; **reporting & insights**; schedules with real-time site updates.
- Collaboration model: "**unlimited free subcontractors and watchers** — pay for your core team but easily collaborate with all project stakeholders"; mobile apps (iOS/Android); offline site documentation; 360° reality capture (SiteView) as an add-on; evidence-collection/claims framing ("documented history" positioning in testimonials).
- Quality-specific planned-inspection machinery (ITPs, hold points) is **not surfaced** on the pages fetched — consistent with a defect-first rather than QA-plan-first philosophy.

## Cross-product Comparison

| Dimension | Procore | FTQ360 | PlanRadar | Reading |
|---|---|---|---|---|
| Template-driven inspection records | company+project templates; sections; line items; conditional logic; photo-required templates | 750+ template library spanning lifecycle (pre-con review → startup) | customizable templates for recurring documentation | **Common**; the itemized inspection record is the shared object |
| Planned quality regime (ITP-like) | Action Plans explicitly positioned for ITPs/quality plans; inspection schedules | project-specific QAQC plans itemizing inspections/tests/hold points with progress tracking | not surfaced | **Common at mature pole**, absent in defect-first pole → standard capability, NOT definitional |
| Non-conformance / deficiency records | Observations (quality/safety/commissioning/warranty/work-to-complete); punch list sibling tool; NCR linkage at FTQ360 | NCRs + deficiency/work-to-complete reports; recurring-issue identification | defect tickets on plans (core heritage) | **Common**; naming varies (observation/NCR/defect/snag/punch) |
| Two-sided verification / acceptance | inspection signers; action plan Approver/Receiver signatures; reject/close on observations; collaborator respond→resolve | customer hold points; surveillance by independent inspectors; code-official inspections; accountability loop | "project manager takes over for the final review" (testimonial); watchers | **Common**; signature/approval machinery depth varies |
| Reinspection after correction | create reinspections of closed inspections | implied by prevention/correction loop; progress tracking | defect tickets reopen/recheck (implied) | Common; strongest direct evidence Procore |
| Requirements anchoring | templates encode specialized requirements per inspection type; ITP framing | "assure completed work meets specifications"; pre-construction spec review | plans/specs on platform | **Common**; quality records justify against project requirements |
| Measurement/test data capture | attachments/records on items | concrete samples, HVAC startup, dimensions, OCR of gauge screens, GPS, third-party test reports | attachments/photos | Common; specialist depth at FTQ360 |
| Location/plan anchoring | multi-tiered locations; create inspections on drawings/models | GPS; location framing | plan-pinned tickets (signature strength) | **Common** (building side) |
| Quality analytics | reports/exports; (dashboards at suite level) | first-time-quality per vendor; deficiency trends; lessons learned; risk management | reporting & insights | Common; specialist depth at FTQ360 |
| Shared engine with safety/environmental | same templates serve OSHA/SWPPP/site-safety; observations split quality vs safety | safety app separate; audits named in plans | safety audits same platform | **Common** — regime (quality vs safety) is the differentiator, not the checklist machinery |
| Mobile + offline field performance | perform on web/iOS/Android | online/offline with sync | mobile apps, offline documentation | **Common** |
| Multi-party participation | subcontractor collaborators respond/resolve; owner templates/videos; third-party contributors to template library | subcontractor/vendor accountability; independent inspectors; code officials | free subcontractors + watchers | **Common** |
| Reports outward (PDF/email) | inspection/observation reports, exports, custom reports | professional-grade reports; database access | reports/insights | **Common** |
| Handover/punch orientation | punch list sibling tool; project-shutdown template | work-to-complete + turnover issues; handover in plan | handovers; punch lists | Common at the edges; Punch List is its own sibling Type |

## Canonical Model (Layer C synthesis)

The Type is the **conformance-process system of record for construction delivery**. One loop carried by two visible primitives:

1. **The conformance (inspection) record** — a structured, template-driven examination of construction work against the project's defined requirements (specifications, contract documents, drawings, codes, project quality plans), performed by an identified party at a defined location/stage, with per-item responses, evidence (photos, measurements, test reports), and a signed/closed result that is retained as the project's quality record. Historically: the paper Inspection & Test Plan sheet, the pre-pour card, the QC inspector's signed checklist.
2. **The non-conformance (deficiency) record** — a recorded failure of work to meet requirements, raised from an inspection or ad-hoc observation, attributed (location, responsible party, severity/type), assigned for correction, and closed only on **verified acceptance** (reinspection, signature, owner/customer approval). Historically: the Non-Conformance Report form and the punch-driven correct-then-reinspect loop.

Around the loop: planned inspection regimes (ITPs / quality plans / hold points / inspection schedules — the "quality assurance" half), acceptance machinery (signers, approvers, receivers, witness roles), evidence capture (photos, measurements, third-party test reports), requirements-anchored checklists, multi-party participation (subcontractor respond/resolve, owner/third-party inspector witness/accept), quality analytics (deficiency trends, first-time-quality, vendor performance), and the quality record as a handover/closeout artifact. The same template engine commonly serves safety and environmental checklists — the **regime object** (work conformance vs hazard control) is what separates quality from safety, not the machinery.

## L0 — Defining Invariant (minimal)

A Construction Quality Management application is recognizable when it provides, for a construction project:

1. **Recorded conformance verification of construction work against defined requirements** — structured inspection records (itemized checklist/template responses) performed by an identified party on project work, with results retained as the project's quality record.
2. **Managed correction of detected non-conformance** — findings of failed conformance become attributed deficiency records assigned to a responsible party, tracked through correction to verified acceptance (reinspection/sign-off/acceptance).

Remove #1 → a defect/issue tracker (Punch List Management / field work items). Remove #2 → a checklist/form tool with no quality loop. Remove the construction anchoring (project work checked against contract/specification requirements, trades, locations) → a generic audit/inspection platform. Historically, the paper ITP + NCR form + signed checklist satisfy both invariants — the Type predates its software and is not defined by photos, mobile apps, cloud, analytics, templates libraries, or plan pinning.

Deliberately NOT definitional: planned inspection regimes (ITPs/hold points/quality plans), template libraries and conditional logic, signature/approval-role machinery, measurement/OCR/GPS capture, plan/model pinning, photo evidence, analytics (FTQ scores, vendor quality), mobile/offline, integrations, cloud delivery, any status-label set.

## L1 — Common Mature Structure

- **Template libraries** — reusable checklists organized in sections + line items, often per inspection type (pre-pour, pre-drywall, waterproofing, milestone, startup), customizable per project; conditional logic and evidence-requirements on items at the mature pole.
- **Planned inspection regimes** — inspection schedules; project quality plans / ITPs itemizing required inspections and tests with **hold points** (work may not proceed without approval) and assigned inspectors; look-ahead/progress tracking of plan completion.
- **Acceptance machinery** — named signers/approvers/receivers; per-item and whole-record signatures; reject/close actions; verification methods per item; customer/owner hold points; witness/surveillance by independent or code officials.
- **Deficiency register with accountability** — observations/NCRs/defects with type, severity, location, due dates, responsible-party assignment, respond→resolve→close flow, rejection of unsatisfactory responses, recurring-issue identification.
- **Evidence capture** — photos/attachments/videos; measurement and test data (some products capture instrument readings, third-party test reports); records linked to items.
- **Location/plan anchoring** — multi-tiered location taxonomies; pinning records to drawings/models (building side); GPS (civil/energy side).
- **Reinspection** — closed/failed inspections can be reinspected; correction loop is explicit.
- **Multi-party model** — subcontractors respond/resolve in scoped roles (often free/light seats); owners and third-party inspectors witness and accept; distribution/notification.
- **Reporting outward** — inspection reports, deficiency/punch reports, quality-plan progress; PDF/email/CSV export; the quality record as a closeout/handover artifact.
- **Analytics** — deficiency trends, first-time-quality/first-pass rates, vendor/subcontractor quality performance, lessons-learned reuse (specialist depth).
- **Mobile + offline** field performance of inspections and deficiency updates.
- **Cross-register linkage** — related items to RFIs, drawings, change events; photos to a project photo library; punch list machinery at handover.

## L2 — Variant / Optional Structure

- **Product pole**: suite-embedded quality tools inside a construction platform (financials/PM alongside) vs quality-specialist QAQC platform (plans + prevention analytics) vs defect-documentation-first platform (plan-pinned tickets, multi-industry).
- **Segment flavor**: commercial building GC (stage-gate checklists, punch orientation) vs residential/homebuilding (stage quality gates, customer walk orientation) vs industrial/energy (ITP-heavy, hold/witness points, factory acceptance tests, commissioning/turnover, third-party surveillance) vs infrastructure/civil.
- **Regime scope**: quality-only vs shared checklist engine with safety/environmental vs bundled safety app.
- **Formality of the quality regime**: informal deficiency-driven quality (small residential) ↔ formal QA/QC programs (documented project quality plans submitted to customers, independent surveillance, qualification of vendors/personnel).
- **Regional vocabulary**: punch list vs snag list (UK/AU) vs defect; QA/QC naming; NCR vs observation vs issue.
- **Integration posture**: standalone vs integrated with project management/cost/document management; ERP/database hand-off for analytics.

## L3 — Vendor-specific Structure (research notes only)

- Procore: company-vs-project template levels; Action Plan roles (Plan Manager, Assignee, Approver, Receiver) and approve-on-behalf; default verification methods; blocking functionality; "Completed Action Plan Receiver"; create-by-location/asset; related items; Change Event from Observation (cost linkage); quality-vs-safety observation categories (Nov 2025); inspection schedules by equipment; bulk creation beta; recycle bin; granular permission matrix per tool; third-party template contributors (OAC Management, NextWave, OSHA, GH Phipps punch types).
- FTQ360: 750+ template library; OCR of measurement-device screens; precision GPS; Excel punch list import; direct database connections (Excel/Power BI); Intelligent Inspection Review service; maturity assessment; firsttimequality.com plan services; segments incl. factory-built housing and energy-rebate programs.
- PlanRadar: unlimited free subcontractors/watchers; plan-pinned defect tickets (Android package "defectradar"); SiteView 360° reality capture; fire-safety/NFPA verticals; PlanRadar Connect (200+ integrations); ISO/GDPR security posture.
- Marketing anecdotes (Trans-Ash quote, CBRE, Five Guys testimonials) — not evidence for canonical claims.

## Boundary Findings

- **vs Construction Field Management** (processed sibling): field management owns the **day record + general field work items** (site-execution layer); quality owns the **conformance loop** (inspection against requirements + non-conformance correction with acceptance). The deficiency register is shared machinery — the discriminator is the product's center of gravity: site execution (day-anchored, any-issue) vs conformance (requirements-anchored, inspection-driven). **Keep only the day record + general work items → Field Management; keep only the inspection/conformance loop → Quality Management.** Flagged for joint review (see Boundary Issues).
- **vs Punch List Management** (unprocessed sibling): punch list is the **end-of-project / handover defect register**; quality spans the whole delivery with planned inspections, non-conformance disposition, and acceptance. Quality tools commonly host punch-like registers (Procore ships both; FTQ360 calls its register "deficiency/work-to-complete punchlist"). **Keep only the handover defect register → Punch List Management.** Joint review recommended when that leaf is processed.
- **vs Construction Safety Management**: same checklist machinery, different **regime object** — hazards, incidents, and regulatory safety compliance vs work conformance to contract requirements. Procore's template library and observation categories show vendors deliberately splitting quality vs safety observations on one engine; FTQ360 ships a separate safety app. **Keep the machinery and change the regime object → Safety Management.**
- **vs Construction Project Management** (processed sibling): the umbrella owns schedule/cost/contracts/document registers; quality is one register family inside it. **Add schedule/cost/contract objects → Project Management.**
- **vs RFI Management**: an RFI asks the design team a question; a non-conformance record asserts work doesn't meet requirements. Deficiencies may spawn RFIs (related-item linkage), but the objects and workflows differ.
- **vs Property Inspection Application**: construction-phase conformance of work in progress vs post-occupancy condition assessment of a finished building (PlanRadar serves both poles — same ticket machinery, different regime).
- **vs Manufacturing QMS / CAPA Management**: different unit of production — one-off contracted work anchored to project specifications vs repeatable production lots; no batch/lot structure here; construction quality anchors to locations, stages, and contract documents.
- **vs generic audit/inspection platforms** (e.g., general-purpose checklist apps): no construction requirement model (specs/trades/locations/ITPs), no project delivery lifecycle. **Remove construction anchoring → generic inspection app.**
- **去掉什么就变成另一个 Type 判据**: remove inspection/conformance records → defect tracker (Punch/Field); remove non-conformance correction loop → checklist/form tool; remove construction anchoring → generic audit platform; add the day record → Field Management; change the regime object to hazards → Safety Management.

## Uncertainties

- **Autodesk Construction Cloud** could not be documented (403 across three same-week runs). It is a known market anchor for the suite-embedded pole; the "suite module" pole therefore rests on Procore alone this run.
- **FTQ360 evidence is Tier-2 vendor positioning** (rich but marketing-shaped). Its NCR/hold-point/FTQ-analytics capabilities are vendor-stated, not verified in a help center. Structural claims from FTQ360 are marked Layer B and used only for cross-product commonality, not for precise mechanics.
- **PlanRadar evidence is platform-level** (root page); its quality-specific machinery beyond defect tickets was not surfaced. Claims about PlanRadar are kept generic.
- **Whether the planned-inspection regime (ITP/quality plans) is universal** is unresolved: strong at Procore (Action Plans) and FTQ360 (QAQC plans); absent in the PlanRadar sample → kept OUT of L0 (correct per single-product discipline), recorded as a standard capability with pole variance.
- **Deficiency-register overlap with Field Management**: the two L0s (field work item; non-conformance record) describe overlapping market machinery with different centers of gravity. The subtraction judgment is inference from directory structure + vendor nav splits; joint review flagged.
- **Historical check is reasoning-based** (paper ITPs, NCR forms, pre-pour cards, signed QC checklists); no pre-digital product was researched directly.
- Precise status names, permission tiers, and numeric template counts vary by product and are kept out of the canonical document.

## Final Synthesis

Construction Quality Management is the **conformance-process system of record for construction projects**: it turns a project's requirements (specifications, contract documents, codes, quality plans) into itemized, template-driven inspection records performed by named parties at defined locations and stages, and it converts failed findings into attributed non-conformance/deficiency records that are assigned to responsible parties, corrected, reinspected, and closed only on verified acceptance — with the whole loop retained as the project's quality record for handover, disputes, and improvement. Mature products add planned inspection regimes (ITPs, hold points, schedules), acceptance machinery (signers, approvers, customer hold points), evidence capture (photos, measurements, third-party test reports), multi-party participation (subcontractor respond/resolve, owner/third-party witness), quality analytics (deficiency trends, first-time-quality, vendor performance), and mobile/offline field performance — sharing one checklist engine with safety and environmental regimes while remaining distinct by regime object. The market realizes the Type in three poles — suite-embedded quality tools, quality-specialist QAQC platforms, and defect-documentation-first platforms — and the boundary logic is subtraction: keep only the day record and general work items → Construction Field Management; keep only the handover defect register → Punch List Management; change the regime object to hazards → Construction Safety Management; add schedule/cost/contracts → Construction Project Management; remove construction anchoring → a generic inspection/audit tool.
