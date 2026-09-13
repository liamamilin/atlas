# Research Notes — Construction Safety Management

Research date: 2026-09-07
Leaf: Construction Safety Management (§17 Construction, Real Estate & Facilities)
Slug: construction-safety-management

## Research Goal

Understand what a Construction Safety Management application actually is as a software Type: what objects it manages, who uses it, how safety work flows through it, what rules and states matter, and where its boundaries sit against Construction Field Management, Construction Quality Management, EHS/HSE Platforms, Daily Log Application, and Construction Project Management. Produce a vendor-neutral canonical model.

## Initial Boundary (working hypothesis before research)

- Core use: managing worker safety on construction projects — recording incidents/hazards, driving corrective actions, running safety program activities (inspections, meetings, inductions), and retaining compliance evidence.
- Likely users: safety managers/coordinators, site supervisors, field workers (including subcontractor crews), corporate EHS leaders.
- Nearest neighbors: Construction Field Management (umbrella site-execution layer that includes safety records), Construction Quality Management (same inspection machinery, different object), EHS/HSE Platform (§21, enterprise-wide), Daily Log Application, Construction Project Management (module realization), Construction Equipment Management (equipment inspections).
- Unknowns: whether the incident register or the hazard/corrective loop is the center; whether program activities (toolbox talks, JHA, permits, orientations) are definitional or common; how strong the regulatory-reporting layer is as a structural element; whether this leaf can stand as a point Type given two prior passes flagged it as module-realized.

## Research Questions

1. What record families exist (incidents, injuries, near misses, hazards, observations, inspections, meetings, permits, JHAs, orientations, training)?
2. What is the state/lifecycle of each record (report → classify → investigate → action → verify → close)?
3. Who creates records (field workers without accounts? subcontractors?) and who works them (safety managers)?
4. How does the regulatory layer appear (OSHA logs, recordable rates, audit evidence, retention)?
5. How do records anchor (project, location tier, worker, subcontractor organization)?
6. What is common vs product-specific: toolbox talks, JHA/pre-task plans, permits, SDS, orientation/access control, equipment inspections, training tracking, analytics (leading indicators, TRIR/LTI)?
7. Boundary tests vs Field Management, Quality Management, EHS Platform, Daily Log, PM platform.

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Procore | Construction-suite module (project-level Incidents/Inspections/Observations tools) | Market-leading PM suite; safety realized as project tools; deep official docs |
| HammerTech | Construction-safety specialist platform (enterprise GCs/EPCs) | Full safety-program scope (orientations, JHA, permits, meetings, inspections, observations, incidents) |
| Safesite | Modern SMB-first standalone safety app | Field safety features + compliance reporting + OSHA recordkeeping + insurance tie-in |
| SafetyCulture (Mitti) | General inspection-led platform used across industries incl. construction | Inspection-first philosophy (template → inspection → report + actions); different product philosophy |

Coverage: suite-embedded vs standalone specialist vs SMB vs general inspection-led; enterprise vs SMB tier; US-centric vs regional (HammerTech AU/UK/US sites).

## Sources

All fetched 2026-09-07 (WebFetch, official sources):

- Procore — Support Home (tool taxonomy: project tools incl. Incidents, Inspections, Observations, Daily Log, Punch List; company tools incl. Action Plans, Inspections, Prequalifications) — https://support.procore.com/
- Procore — Incidents user guide landing (overview, tutorial list, FAQ list, permissions matrix, recent changes incl. Root Cause Analysis Form 07/2026, conditional custom fields 07/2026, equipment linkage 11/2025) — https://support.procore.com/products/online/user-guide/project-level/incidents
- HammerTech — Construction Safety Software home (platform grouping Mobilize/Coordinate/Report; FAQ; no-per-seat-fee positioning; customer stats) — https://www.hammertech.com/
- HammerTech — Incidents & Injuries product page (lifecycle: field reporting → investigation/RCA → corrective actions; linked records; LTI/MTI tracking; Power BI trends; FAQ) — https://www.hammertech.com/en-us/platform/incidents-injuries
- HammerTech — Site Observations product page (proactive observation model; positive/neutral/negative classification; numbered + owned + photo-verified closeout; no-login crew participation; AI photo recognition) — https://www.hammertech.com/en-us/platform/site-observations
- Safesite — Home (feature taxonomy: Inspections & Audits, Incident Reporting, Safety Meetings, Hazard Management, Safety Observations, To-Do List, Offline, Multilingual, Leading Indicator Analytics, Safesite Score, Compliance Reporting, Campaign Scheduler, Team & Trade Management, OSHA Recordkeeping, Training & Certification Tracker, Document Management; industries incl. construction; templates library incl. trenching & excavation) — https://www.safesitehq.com/
- Safesite — Hazard Management feature page (record/notify/resolve hazards; automated follow-up & close-out workflow; trends by personnel/team/project/organization) — https://safesitehq.com/features/hazard-management-app/
- Safesite — Help Center (reachable; Intercom; collections: Desktop Portal admin, Mobile App field, Notifications, FAQs) — https://help.safesitehq.com/
- SafetyCulture/Mitti — Help Center home (featured articles: "What are templates, inspections, and reports?"; "What are actions?"; "What is Training in Mitti?"; "What are Heads Ups?"; seat types) — https://help.safetyculture.com/ (redirects to mitti.com help center)

Unreachable / not used: procore.com marketing product pages (404 on /en-us/products/safety, /products/safety, /products/incident-management — support site used instead); deep Safesite/Mitti article bodies (nav-level only for Mitti).

## Product Observations

### Procore (evidence layer A — direct official docs)

- Incidents is a **project-level tool**; company-level tools include Inspections, Action Plans, Prequalifications; project tools include Incidents, Inspections, Observations, Daily Log, Punch List. Safety capability is realized as several project tools inside the suite, not one "safety" module.
- Incidents tool self-description: "keeps track of safety-related issues so your team can manage risk, identify trends, and harness valuable data… Track hazards, contributing conditions and behavior, person(s) involved, and the paper history associated with each incident throughout the lifecycle of your project. Report on trends… Capture incident data in real-time and update as more information becomes available. Customize severity levels and which team members get alerted."
- **Incident as aggregation record**: an incident carries child record types — Injury/Illness Record, Near Miss Record, Property Damage Record, Environmental Record, Witness Statement, Action, Related Item. Tutorials: "Add an Injury/Illness Record to an Incident", "Add a Near Miss Record to an Incident", "Add a Witness Statement to an Incident", "Add an Action to an Incident", "Close an Incident".
- Lifecycle: create incident → add records (witness statements, injuries) → assignees/contacts → close. Recycle-bin deletion; CSV/PDF export; email incidents.
- Investigation: dedicated Root Cause Analysis form introduced 07/2026 with granular permissions and configurable fieldsets; conditional custom fields on the incident form (07/2026); equipment records linkable from the project Equipment tool (11/2025).
- Permissions: full matrix with None/Read Only/Standard/Admin + granular permissions; private incidents visible to Creator/Assignee/Alert Recipient/Distribution List; field-worker mobile creation ("Create an Incident (Mobile) - Field Worker"); configurable fieldsets (required/optional/hidden).
- Regulatory: FAQ titles present — "Can I use the Incidents tool to help comply with OSHA reporting requirements?", "Will Procore integrate with OSHA's Injury Tracking Application for electronic submission of injury and illness records?" (FAQ titles only; article bodies not fetched — no field-level OSHA claims).
- Locations: multi-tiered location tagging on incident items; map view for photo attachments.
- Observation boundary note: Observations is a *separate* project tool from Incidents (unified observation-type selection in incidents noted 09/2025 release note).

### HammerTech (evidence layer A — product + platform pages)

- Self-positioning: "Construction Safety Software… Every Safety Workflow Connected in One Platform. Safety isn't a single task — it's a workflow. From inductions and pre-starts to incident tracking and reporting."
- Platform taxonomy (vendor's own grouping): **Mobilize** (Subcontractor Management, Orientations & Worker Info, JHAs, SDS, Safety Plans) / **Coordinate** (Pre Task Plans, Permits, Safety Meetings, Notifications, Logistics, Equipment Compliance) / **Report** (Inspections, Site Observations, Incidents & Injuries, Daily Report, Site Access) + Reporting & Insights + HammerTech Intelligence (AI).
- Incidents & Injuries: lifecycle = report from anywhere on site (tailored forms per project/company/regulatory requirements; photo/document attachments; linked records: injuries → incidents → affected workers → corrective actions) → investigate (structured root cause analysis; version-controlled timestamped records "to support audit and legal review"; automatic Lost Time Injury tracking and recordable incident rates by project) → corrective actions (raise/assign from any incident record; live dashboards; project-wide open-action tracking). Types: "injuries, incidents, near misses, property damage, and other project-specific occurrence types — all configurable".
- Cross-module interlocks (vendor-documented): Site Observations "convert field hazard observations directly into official incident records"; Inspections "generate incident reviews directly from failed checklist items"; Daily Report "log critical incident timelines and injury details automatically into your daily site records"; Power BI trend integration.
- Site Observations: definition FAQ — "A safety observation is a recorded note about a hazard, unsafe behavior, near miss, or quality issue spotted on a job site. Unlike incident reports, observations are proactive, so crews are capturing risk before anyone gets hurt." Classification: Positive/Negative/Neutral; configurable priority (suggested or locked); numbered records with instant ownership assignment + automated reminders; photo-evidence closeout verification; "workers can log observations without an account"; AI photo recognition auto-populates type/classification/description; voice-to-text; bulk logging.
- Program breadth: subcontractor prequalification, orientations/worker info (site access), JHAs, SDS, safety plans, pre-task plans, permits, safety meetings, equipment compliance.
- Business model: "No Per-Seat Fees… Every worker and subcontractor gets in with no extra fees" — participation-breadth philosophy.
- Customers: ENR Top 400 GCs/EPCs/owners; multi-region (US/AU/GB).

### Safesite (evidence layer A — product + feature pages)

- Self-positioning: "Best-in-Class Safety Management System & Safety App… Go Beyond Safety Compliance… Just safer worksites." Industries: agriculture, construction, manufacturing; construction a headline vertical.
- Feature taxonomy (vendor's own grouping): **Field Safety** (Inspections & Audits, Incident Reporting, Safety Meetings/toolbox talks, Hazard Management, Safety Observations, To-Do List, Offline Mode, Multilingual EN/ES/FR/PT) / **Management Dashboard** (Leading Indicator Analytics, Safesite Score, Compliance Reporting, Safety Campaign Scheduler, Team & Trade Management, OSHA Recordkeeping incl. "OSHA 300 form integration", Training & Certification Tracker, Document Management) / **Safety Success** (support services, template library, safety program review, tailored compliance plan).
- Incident Reporting: "Capture critical info, instantly notify stakeholders, or add to OSHA Log… Record serious injuries, near misses, theft, property damage, and equipment failure… Use data to analyze root cause and reduce TRIR."
- Hazard Management: "Record, communicate and resolve hazards on-the-go… notifying and automatically following up on hazards with responsible parties… Create corrective actions on the spot… Assign priority and instantly notify the responsible party… automated close-out workflow." Analytics "view trends by personnel, team, project, or organization."
- Safety Meetings: "Track attendance and topics covered; identify training needs with our powerful analytics; choose from 100s of templates, forms, and topics."
- Inspections: schedule/track inspections; create safety tasks and raise hazards; library of compliance checklists; offline mode.
- Business model: free core app + plans; insurance tie-in (Foresight workers' comp "powered by Safesite"). Marketing outcome claims (57% incident reduction, 62% faster hazard resolution, 21,000+ hazards closed yearly, 8 hrs/week saved) — vendor marketing numbers, recorded here only, not promoted.

### SafetyCulture / Mitti (evidence layer A — help center landing; layer B for model shape)

- Help center now operates under "Mitti by SafetyCulture" brand (SafetyCulture product rebrand observed 2026-09-07; app login still app.safetyculture.com).
- Core model visible from featured-article descriptions: **templates → inspections → reports** ("Learn about templates, inspections, and reports… how they relate to each other to help you create templates, conduct inspections, and share inspection reports"); **Actions** ("identify, track, collaborate, and complete tasks together"); **Training**; **Heads Ups** (broadcast messages); seat types (full/lite/guest).
- Construction presence: templates library includes construction; historically iAuditor widely used for construction safety walks. Construction-specific safety-program machinery (OSHA logs, inductions, permits) not evidenced at help-center level in this pass → assertions about this pole kept modest (inspection-led core + actions; used in construction).

## Cross-product Comparison

| Dimension | Procore | HammerTech | Safesite | SafetyCulture/Mitti |
|---|---|---|---|---|
| Incident/event records | Incidents tool w/ child records: injury/illness, near miss, property damage, environmental, witness statements, actions, related items | Incidents & Injuries: injuries, near misses, property damage, configurable occurrence types; linked records | Incident Reporting: injuries, near misses, theft, property damage, equipment failure; OSHA Log | (not surfaced at help-center level; actions model present) |
| Proactive findings | Observations (separate tool) | Site Observations (hazard/unsafe behavior/near miss/quality issue; positive/neutral/negative) | Hazards + Safety Observations | Inspections surface findings; actions |
| Corrective loop | Actions on incidents; Action Plans (company tool) | Corrective/preventive actions from incidents & observations; ownership; project-wide open tracking | Corrective actions on the spot; priority; responsible party; automated close-out | Actions as first-class object |
| Investigation/RCA | RCA form (2026), versioned records | Structured RCA, version-controlled timestamped records | root cause analysis via data | — |
| Inspections/audits | Inspections project tool | Inspections module (failed items → incident reviews) | Inspections & Audits w/ checklist library | Inspection-led core (template → inspection → report) |
| Meetings/toolbox talks | (not a dedicated safety tool) | Safety Meetings module | Safety Meetings (attendance, topics, templates) | — |
| Program documents | — | Safety Plans, SDS, JHAs, orientations | Document Management | — |
| Regulatory layer | OSHA compliance FAQs, ITA integration question | regulatory-requirement form tailoring; LTI/MTI rates | OSHA Recordkeeping / OSHA 300 integration | — |
| People anchoring | assignees/contacts, private visibility | workers, subcontractors, affected workers; no-login capture | personnel/team/project analytics; team & trade management | seat types, guest seats |
| Analytics | trends reporting, insights (granular permission) | live dashboards, leading indicators, Power BI | leading-indicator analytics, Safesite Score | — |
| Packaging | suite project tools | standalone specialist platform | standalone app + insurance bundle | general platform (all industries) |
| Participation model | Standard/Admin users; field-worker mobile | every worker + subcontractor, no per-seat fees, no-login observations | free app for field, admins on desktop portal | seat types incl. lite/guest |

### Convergent findings (cross-product, layer B)

1. **Two-sided record posture**: reactive event records (incidents: injury, near miss, property damage, environmental) AND proactive finding records (hazards/observations) — present in every construction-scoped product sampled.
2. **Corrective-action loop as the management engine**: findings and investigation outcomes convert into assigned, owned, tracked actions to verified closure (Procore actions; HammerTech CAPA with ownership + reminders + photo-verified closeout; Safesite on-the-spot actions with automated close-out; Mitti actions).
3. **Project/site anchoring with multi-tier locations + people/organization anchoring** (affected worker, subcontractor org, crew).
4. **Investigation of significant events** (root cause analysis, witness statements, evidence attachments, versioned/auditable records).
5. **Safety program activities around the register**: inspections/audits with checklists; toolbox talks/safety meetings (Procore absent as dedicated tool → common, not definitional).
6. **Regulatory recordkeeping alignment** (OSHA 300-class logs, recordable rates, audit/legal-defensible records) — US-centric in sample; present in all three construction-scoped products, absent in general pole's surfaced docs.
7. **Broad field participation**: mobile capture, offline, multilingual, no-login/no-account or low-barrier worker reporting; subcontractors included.
8. **Analytics over leading + lagging indicators** and roll-up across projects.
9. **Configurable forms/taxonomies** (incident types, severity/priority levels, fieldsets, templates).
10. **Cross-register interlocks**: observations → incidents; failed inspection items → reviews/actions; incident timelines → daily logs; equipment records → incidents.

### Divergences (layer A/L3)

- Procore: safety as multiple project tools inside PM suite; recycle bin; configurable fieldsets/granular permissions machinery; no dedicated toolbox-talk tool.
- HammerTech: full safety-program breadth (orientations/site access, permits, PTP, SDS, safety plans, equipment compliance); no-per-seat pricing; HammerTech Intelligence AI photo recognition; Power BI.
- Safesite: free-app + insurance (Foresight workers' comp) bundling; safety campaign scheduler; Safesite Score; multilingual (EN/ES/FR/PT).
- Mitti: inspection-led generic platform; Heads Ups broadcasts; seat-type model; rebrand from SafetyCulture.

## Canonical Model (synthesis)

### L0 — Defining Invariant (deliberately minimal)

A Construction Safety Management application is the project-side system of record for managing worker safety on construction work. Removing any element below stops the product being recognizable as this Type:

1. **Safety records anchored to projects and people** — a standing register of safety-relevant occurrences and findings on the work: injuries/illnesses, near misses, property/environmental damage events, and proactive hazard/observation findings. Records attach to projects/sites (locations) and to the workers and organizations involved. Remove project/people anchoring → generic enterprise EHS; remove the safety register → not this Type.
2. **The corrective-action loop** — findings and investigation outcomes become assigned, owned corrective/preventive actions tracked to (evidence-verified) closure. Remove → an incident/hazard log with statistics, not safety *management*.
3. **Investigation + retained auditable record of significant events** — significant events carry an investigation (witness statements, evidence, root cause) and the register is retained as a durable, attributable record (compliance/legal posture). Remove → ephemeral hazard reporting, not a managed safety program.

Framing sentence (canonical, layer C): *the managed loop from recorded safety events and hazards to accountable corrective actions, kept as a durable project-anchored safety record.*

### L1 — Common Mature Structure

- Incident record families (injury/illness, near miss, property damage, environmental) with configurable types and severity levels
- Hazard/observation register with classification (positive/negative/neutral; type; priority) and unique numbering
- Inspections & audits with checklist libraries/templates, scheduled and ad hoc
- Toolbox talks / safety meetings with attendance and topics (common; absent as a dedicated tool in one sampled suite → common-not-universal)
- Investigation machinery: witness statements, photo/document evidence, root cause analysis, versioned records
- Notifications/alerts to responsible parties; automated reminders and follow-up
- Mobile field capture (offline; multilingual; low-barrier/no-login participation; subcontractor inclusion)
- Dashboards/analytics: leading indicators (inspections, observations, meetings), lagging indicators (incident rates, days-since), trends by project/team/personnel, export/reporting
- Regulatory recordkeeping support (OSHA 300-class logs in US market; recordable-rate tracking)
- Configurable forms/fieldsets, severity/priority taxonomies, template libraries
- Cross-module interlocks: observation→incident conversion, failed-inspection-item→action/review, incident→daily-log summary, equipment linkage
- Document management for safety program documents (plans, SDS) and training/certification tracking (common; depth varies)

### L2 — Variant / Optional Structure

- Regional regulatory regimes: US OSHA recordkeeping/electronic submission vs UK/ANZ/other regimes (form tailoring "per regulatory requirements")
- Safety-program workflow add-ons: JHA/job hazard analysis libraries, pre-task plans, permit-to-work (hot work/confined space), orientations/inductions with site access control, SDS management, equipment compliance inspections
- Scope posture: construction-specialist platform vs suite module (PM platform or field-management platform) vs general inspection-led platform used in construction vs enterprise EHS-suite construction module
- Customer tier: ENR-class enterprise GC/EPC vs SMB contractor crews
- Business model: per-seat vs no-per-seat participation pricing; free core + paid plans; insurance bundling (workers' comp) tie-ins
- AI posture: AI photo recognition of hazards, auto-populated observation fields, AI risk surfacing (era-typical; not definitional)
- Multi-language field experience; campaign scheduling; scoring systems (branded "safety score" metrics)

### L3 — Vendor-specific (kept in notes only)

- Procore: recycle bin for incidents; configurable fieldsets implementation; granular-permission mechanics; distribution groups; "Project Incident Insights" granular permission; conditional custom fields (07/2026); unified observation-type selection in incidents (09/2025); equipment linkage (11/2025); RCA form (07/2026).
- HammerTech: Mobilize/Coordinate/Report grouping; HammerTech Intelligence (AI photo recognition); HammerTechGO; Power BI integration; no-per-seat-fee policy; 5M workers / 1,000+ customers / 50,000+ projects marketing stats; customer quotes (Holder, Axiom).
- Safesite: Safesite Score; Foresight Insurance bundling ("powered by Safesite", 18% claims-reduction claim); 57%/62%/8-hrs/21,000+ marketing claims; safety campaign scheduler; EN/ES/FR/PT app.
- Mitti/SafetyCulture: rebrand to Mitti; Heads Ups broadcast feature; full/lite/guest seat types; template-upload digitization service.

## Boundary Findings

1. **vs Construction Field Management (§17, processed)** — Field Management is the integrating site-execution layer (day record + field work items); its pass flagged this leaf for cross-reference. Held: the safety register + safety program loop is a distinct center. A field issue (punch/deficiency) closes when the work is redone and verified; a safety finding closes when the hazard is remediated/behavior corrected and evidence recorded — same *discipline*, different object semantics, different regulatory frame, different program context (incidents, investigations, OSHA logs, toolbox talks have no punch-list analogue). Products embed one register inside the other (HammerTech daily report; Procore field tools) — packaging, not type identity. Cross-reference recorded for the field-management pass's umbrella flag.
2. **vs Construction Quality Management (§17 sibling, unprocessed)** — same inspection/checklist/CAPA machinery, different object of record: specification conformance/defects (rework cost) vs harm to people (regulatory/legal exposure). Vocabulary test: "nonconforming installation" vs "unsafe condition". Environmental incident records appear inside incident registers (Procore) — quality systems don't carry injury/near-miss families. Joint review recommended when that leaf is processed.
3. **vs EHS / HSE Platform (§21)** — enterprise EHS spans all operations (facilities, chemical management, emissions, ISO 14001/45001 programs, corporate audits) with the organization as anchor; this Type anchors to construction projects/sites, carries construction workforce structure (subcontractors, crews, inductions), and construction hazard workflows. General EHS vendors serve construction customers; seam = primary anchor + workforce model. Note: sampled construction-scoped products center the project register, not org-wide EHS program management.
4. **vs Daily Log Application (§17, processed as sibling of field management)** — incident timelines/injury details flow into daily site records (HammerTech-documented); the daily log centers the day's work record, the safety system centers the safety register across days. One-directional summary flow, not merge.
5. **vs Construction Project Management (§17, processed)** — safety realized as modules inside PM platforms (prior pass recorded this); PM centers schedule/cost/contracts/coordination. This leaf stands as the safety program's system of record; suite-module realization is a packaging variant (same treatment as RFI/Submittal/Quality leaves).
6. **vs Construction Equipment Management / CMMS (§16/§17)** — equipment compliance inspections (HammerTech Equipment Compliance; Safesite "monthly equipment inspection forms") overlap pre-operational equipment checks; equipment systems center the fleet/assets, safety centers hazards/people/events. Equipment inspection forms are a shared surface.
7. **vs Permit Management (§24) / government permits** — construction permit-to-work (hot work, confined space, excavation) is an authorization workflow inside the safety program; no evidence it constitutes a separate product class here; recorded as variant/extension, not a boundary conflict with government permit management (different domain).
8. **vs Incident Management (§14 IT)** — false friend: IT incident response shares the incident→action lifecycle but no injury/hazard model, no regulatory safety recordkeeping, no site anchoring.
9. **Anti-overfitting note** — OSHA specifics (300/300A logs, ITA submission, TRIR vocabulary) are the dominant US realization, not the definition: the register + loop model survives under UK/ANZ regimes and under pre-OSHA paper practice (see historical check). Toolbox talks, JHAs, permits, orientations are program realizations, not invariants.

### Historical / market-sample check (§24 discipline)

Pre-digital construction safety practice: paper OSHA 300 logs (US, 1971→), job hazard analysis forms, toolbox-talk sign-in sheets, permit-to-work books, safety-walk checklists, incident report forms retained in project files. All satisfy the L0 core (project-anchored safety records + corrective loop + investigation/retention) without mobile apps, cloud, AI, checklists engines, or OSHA electronic submission. The definition therefore does not encode the modern mobile/AI implementation. Older/regional products (paper-based programs, ANZ/UK regimes without OSHA) fit.

## Uncertainties

- Mitti/SafetyCulture construction-specific depth: help-center landing evidences the inspection/actions model but not construction safety specifics (OSHA logs, inductions); treated as the general inspection-led pole with modest-strength assertions.
- Procore FAQ article bodies not fetched (titles only): OSHA compliance support asserted at FAQ-title strength; no field-level OSHA claims made anywhere.
- Procore marketing pages unreachable (404 ×3); support docs used instead — no product-positioning claims made beyond support-site evidence.
- No numeric limits (retention periods, user counts, file sizes) asserted anywhere — none were evidenced.
- Subcontractor prequalification machinery (HammerTech Subcontractor Management; Procore Prequalifications) borders Subcontractor Management/prequalification Types; recorded as adjacent program breadth, not core.

## Final Synthesis

Construction Safety Management is the project-side system of record for the safety of people doing construction work. Its defining structure is small: a standing register of safety events (injuries, near misses, property/environmental damage) and proactive findings (hazards/observations) anchored to projects, locations, and the workers/organizations involved; a corrective-action loop that turns every finding and investigation outcome into an owned, tracked action carried to evidence-verified closure; and investigation/retention machinery that keeps significant events as durable, attributable records usable for compliance and legal defense. Around that core, mature products add inspection/audit engines, toolbox talks, configurable taxonomies, mobile low-barrier capture for the whole site population (including subcontractors), analytics over leading and lagging indicators, and regional regulatory recordkeeping (OSHA-class in the US). The Type is realized as standalone specialist platforms (HammerTech, Safesite), as project tools inside construction PM suites (Procore), and as construction deployments of general inspection-led platforms (SafetyCulture/Mitti). Packaging varies; the safety register + corrective loop + investigation/retention center is stable.
