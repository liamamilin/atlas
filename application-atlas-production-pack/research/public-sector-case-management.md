# Research Notes — Public Sector Case Management

Research date: 2026-09-10
Leaf: Public Sector Case Management (DIRECTORY §24 Government, Public Sector & Civic)
Slug: public-sector-case-management

## Research Goal

Understand what a generic, cross-domain public-sector case management application is: what a "case" is in government software, who works it, how it moves from intake to resolution, what machinery recurs across products, and where its boundaries sit against 311/service-request platforms, domain-specific case management Types (social services, child welfare, immigration, law enforcement, court), private-sector business case management, and help-desk/ticketing systems.

## Initial Boundary

Working hypothesis before research:

- Core use: government agencies (municipal, county, state/provincial, national) track individual constituent matters — requests, complaints, applications, investigations, service provisions — as identifiable, assignable, traceable cases from intake to closure.
- Primary users: caseworkers / case managers (frontline staff holding a caseload), supervisors, program administrators; sometimes constituents via portals.
- Nearest neighbors: 311 / Citizen Service Request Platform (front-end intake + routing), domain case management Types listed separately in the directory, Business Case Management Platform (§10 private-sector analog), Help Desk / Ticketing, Government Records Management.
- Biggest unknown: whether a domain-independent "public sector case management" exists as a real market, or whether the phrase is only an umbrella over domain-specific systems.

## Research Questions

1. What is a case in public-sector software? What objects does the system hold (case, person/constituent, program, task, document, note, communication)?
2. How does a case enter the system (intake channels)?
3. How is a case assigned and worked? What is the caseload model?
4. What lifecycle/status machinery exists (statuses, tasks, deadlines, SLA, checklists)?
5. How does the agency communicate with the constituent (portal, letters, notifications)?
6. What documents/evidence/notes/audit machinery exists?
7. What reporting and accountability structures exist (caseload, outcomes, compliance)?
8. Where are the boundaries: vs 311, vs ticketing, vs domain case management, vs records management, vs BPM?

## Representative Products

Selected for market representation, documentation availability, different product philosophies, and different customer levels:

| Product | Philosophy | Customer level | Evidence tier reached |
|---|---|---|---|
| Salesforce Public Sector Solutions (Case Management for Public Sector) | configure-your-own on a CRM platform; cross-domain | large city/state agencies, national | Tier-1 (Trailhead modules + Salesforce Help) |
| CaseWorthy (incl. ClientTrack) | purpose-built human & social services case + program management | nonprofits + local/state government human services | Tier-2 (product/platform pages) |
| GovPilot | municipal "operating system" — many department modules over one platform | small-to-large municipalities/counties | Tier-2 (product site) |
| Comcate | department-specific case tools for local government (code enforcement, animal control, CRM/311) | small-to-mid municipalities | Tier-2 (product site) |

Rejected / unreachable samples:

- Tyler Technologies (largest US pure-play government software vendor): tylertech.com returned HTTP 403 on two attempts (2026-09-10). Abandoned per source-access rules. Its absence is a sourcing limitation; no claims about Tyler are made.
- ServiceNow government pages: request timed out twice. Abandoned. The platform-vs-ticketing boundary is instead reasoned from the sampled products' own intake/queue/caseload semantics.

## Sources

- Salesforce Public Sector Solutions overview: https://www.salesforce.com/publicsector/ (fetched 2026-09-10)
- Salesforce Trailhead, "Social Program Management Data Model in Public Sector Solutions" — units: Get Started with Case Management Objects for Social Programs; Understanding Participants and Public Complaints, Referrals, and Applications; Explore Cases, Programs, and Benefits: https://trailhead.salesforce.com/content/learn/modules/social-program-management-data-model-in-public-sector-solutions/... (fetched 2026-09-10)
- Salesforce Help, Public Sector Documentation (incl. Managing Investigative Cases; Create Case from Complaint flow): https://help.salesforce.com/s/articleView?id=ind.psc_admin_concept_psc_welcom.htm... and https://help.salesforce.com/s/articleView?id=ind.prog_case_mgmt_complaints_incidents_flow_setup_case.htm... (fetched 2026-09-10)
- Salesforce Developers Data Model Gallery, Investigative Case Management: https://developer.salesforce.com/docs/platform/data-models/guide/justice-investigative-case-management.html (fetched 2026-09-10)
- CaseWorthy home + platform pages: https://caseworthy.com/ , https://caseworthy.com/platform/caseworthy-platform/ (fetched 2026-09-10)
- GovPilot home: https://www.govpilot.com/ (fetched 2026-09-10)
- Comcate home: https://www.comcate.com/ (fetched 2026-09-10)

## Product Observations

### Salesforce Public Sector Solutions — Case Management for Public Sector

Evidence layer: A (directly observed in Tier-1 official documentation).

- Positioning: "Case Management for Public Sector ... streamlines client engagement, service provider communication, and care coordination." Public Sector Solutions spans "case management, licensing and permitting, grantmaking, social programs, emergency response" (product page).
- Data model (Trailhead + Data Model Gallery), organized in five categories:
  - Participant objects: person account / business account representing constituents, organizations (other agencies, nonprofits, households); participants carry role and status on complaints and cases; party relationship groups organize households/cohorts.
  - Case management objects: Public Complaint, Complaint Participant, Complaint Case, Case, Case Participant, Case Episode, Case Proceeding, Case Proceeding Result, Referral.
  - Program management objects: Program, Program Enrollment, Benefit, Benefit Type, Benefit Assignment, Benefit Schedule, Benefit Session, Recurrence Schedule.
  - Application objects: Individual Application (constituent files via online portal; approval processes; Business Rules Engine eligibility; status-change email notifications; completed form attached as PDF to records such as cases).
  - Care plan objects: Care Plan, goals, tasks assigned to the constituent.
- Intake: "there are three ways that constituents enter the system: public complaints, referrals, and applications." Public complaints arrive "over the phone, through email, or by filling out a web form"; intake officer completes initial assessments and prescreening via guided flows and dynamic assessments; running notes capture remarks quickly. Referrals track client, case, referral source, requested provider, outcome; inbound vs outbound. Applications filed through an online portal.
- Case creation and assignment: "After intake and screening, create a case to store all of the data related to a specific problem or situation, including the people involved, the problems they experience, and the measures you put in place to resolve the problems." "Case managers create cases, prioritize them, and assign caseworkers to investigate the issue." From a case, staff "can view all related participants, complaints, referrals, applications, care plans, and programs in a single record."
- Canonical workflow (Trailhead, verbatim stages): 1. Intake and Assessment → 2. Planning (eligibility determination) → 3. Care Plan Assignment (prescribed tasks and goals, benefits, program enrollments) → 4. Monitoring (scheduled check-ins) → 5. Resolution (care plan complete, case resolved).
- Routing: Omni-Channel "routing cases based on staff capacity and case type" (product page).
- Constituent-facing: Help Center self-service site; "constituents can submit a case with a quick web form"; Constituent Snapshot unified view (product page).
- Investigative variant (Help + Data Model Gallery): complaint filing → case creation → investigation → results and outcomes; "Casework Overview" console as centralized hub; case proceedings, case proceeding results, custody chain entries and custody items (evidence), regulatory code violations, violation enforcement actions, visits.
- Complaints Agentforce template: "Quickly assess complaints, gather relevant information, create an investigation, and resolve issues" (product page).

### CaseWorthy (incl. ClientTrack)

Evidence layer: A for the product's own claims (Tier-2 official product pages).

- Positioning: "purpose-built, mission-critical software platform for case & program management to enable coordinated whole-person care and outcome reporting across the spectrum of human services." Used by "1,000+ nonprofit organizations, local and state governments."
- Who served: aging services, behavioral health, IDD, education, employment, family services, homelessness/HMIS, government/public sector, veterans, survivor services — multi-program organizations.
- Stated capabilities: intake that captures critical data and "determine[s] eligibility in real time"; care plans ("design intelligent care plans, coordinate services seamlessly, and continuously monitor progress"); case notes ("300M+ case notes recorded"); document management; client and partner portals; automated notifications/reminders; role-based access; funder-ready, audit-ready reporting; configurable workflows/forms/assessments/service plans without code (apBuilder); single client record across programs ("360° view of every client"; "reduce duplicate intakes").
- Applications: ClientTrack ("case management designed to support complex human services organizations delivering care across multiple programs and funding streams"), ServTracker (aging services), MediSked (HCBS/I-DD).
- Platform: unified client & program data; service delivery & tracking ("track services, utilization, and outcomes in real time"); analytics; centralized admin (users, permissions, configurations, workflows).

### GovPilot

Evidence layer: A for the product's own claims (Tier-2 official product site).

- Positioning: "comprehensive, cloud-based Operating System for Local Governments"; municipal and county departments; "125+ Solutions for All Departments" (module catalog).
- Citizen side: "let residents report, apply, pay, and track their service request status online"; GovAlert mobile app for citizens to "quickly report concerns"; digital forms.
- Staff side: "end-to-end digital forms, automated workflows"; GovInspect mobile app for inspectors to "take notes, reference codes, and upload photos on-site"; violations and certifications sent via email (case study).
- Cross-department unification: PropertyProfile "display[s] parcel level detail including cross departmental records"; GIS maps.
- Reporting: "Pull data and generate reports with just a click."
- Departments covered include construction/permitting, code enforcement, clerk, public works; case study blog "Rethinking Case Assignments" is Comcate's, but GovPilot case studies show request→processing→resolution flows (e.g., Report-a-Concern cited as revenue/collection driver).

### Comcate

Evidence layer: A for the product's own claims (Tier-2 official product site).

- Positioning: "Software & expertise transforming municipal service delivery"; products: Code Enforcement, Animal Control, CRM/311.
- Workflow framing: "we'll work with you to understand your processes and come up with the best way to set up your workflows from request to resolution."
- Case assignment is a named concern: blog post "Rethinking Case Assignments to Keep Code Enforcement Moving"; "Closing the Loop with Public Requests for Service."
- Help Center exists (comcate.elevio.help) but did not render article content on fetch; no Tier-1 operational detail obtained.

## Cross-product Comparison

| Structure | Salesforce PSS | CaseWorthy | GovPilot | Comcate | Layer |
|---|---|---|---|---|---|
| Case as persistent identified unit of record bound to a constituent matter | Yes (Case + intake objects) | Yes (case & program management) | Yes (service requests/concerns processed per department) | Yes (request→resolution workflows) | B |
| Responsible-worker assignment / caseload semantics | Yes (case manager assigns caseworker; Omni-Channel routing by capacity) | Yes (case managers; staff caseloads) | Yes (department staff process; inspector assignment) | Yes (case assignments in code enforcement) | B |
| Configurable lifecycle from intake to recorded resolution | Yes (5-stage canonical workflow; statuses) | Yes (configurable workflows) | Yes (automated workflows per module) | Yes (request→resolution) | B |
| Multiple intake channels (web form/portal, phone, email, referral, field/citizen app) | Yes (complaints, referrals, applications; Help Center) | Yes (intake; client/partner portals) | Yes (resident report/apply/pay/track; GovAlert) | Yes (CRM/311) | B |
| Person/constituent records with roles (participants, households) | Yes (participants, party relationship groups) | Yes (client records, 360° view) | Partial (parcel/property-centric; residents) | Partial (requester records) | B |
| Case notes, documents, attachments as case memory | Yes | Yes (case notes, document management) | Yes (digital records, photos) | Yes | B |
| Tasks / checklists / deadlines inside the case | Yes (care plan goals/tasks; benefit sessions) | Yes (care plans, monitoring) | Yes (workflow steps) | Evidenced indirectly (workflow steps) | B |
| Constituent communication & status visibility | Yes (notifications, portal) | Yes (portals, notifications) | Yes (track status online) | Yes ("closing the loop") | B |
| Program/benefit/eligibility machinery | Yes (programs, benefits, eligibility, enrollment) | Yes (eligibility, programs, funding streams) | No evidence | No evidence | A (2 products) |
| Care plans (goals/tasks for the constituent) | Yes | Yes | No evidence | No evidence | A (2 products) |
| Investigation machinery (evidence, custody, proceedings) | Yes (investigative CM objects) | No evidence | No evidence | No evidence | A (1 product) |
| GIS / property / parcel anchoring | No evidence | No evidence | Yes (GIS, PropertyProfile) | No evidence | A (1 product) |
| Inspections / violations / enforcement actions | Yes (regulatory code violations, enforcement actions) | No evidence | Yes (GovInspect, violations) | Yes (code enforcement) | B |
| Funder/audit/compliance reporting | Yes (analytics) | Yes (funder-ready, audit-ready) | Yes (council reports) | No evidence | B |
| Role-based access control | Yes (permission sets) | Yes | Not stated | Not stated | B |
| AI assistance | Yes (Agentforce templates) | Yes (Cara copilot) | No evidence | No evidence | B |

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures over one binding:

1. **The case as unit of record** — a persistent, identified record of one constituent matter opened with the agency (a request, complaint, application, report, or service provision), carrying its own lifecycle and accumulating its own history. Remove → an intake log or records archive.
2. **Responsible-worker holding (caseload semantics)** — the case is held and worked by an identified staff member (individually assigned or routed to a queue/staff group by capacity and case type); the worker's caseload is a first-class working surface. Remove → an anonymous ticket queue or a bare workflow engine.
3. **Governed lifecycle to a recorded resolution** — the case moves through configured stages/statuses from intake to a recorded outcome (resolved, denied, closed, referred), with actions, notes, documents, and communications accumulating on the case as institutional memory. Remove → a task list or a filing cabinet.

Binding: **public-sector service semantics** — the case is a constituent's matter with a government agency, processed under the agency's service obligations (program rules, statutory or policy timelines, public accountability for outcomes). Remove the binding → generic business case management or help-desk territory.

Jointly-held load-bearing analysis:

- 1 alone = intake log / case-file archive
- 2 alone = staff assignment tool
- 3 without 1+2 = generic workflow engine
- 1+2 without 3 = assignment tracker with no resolution discipline
- 1+3 without 2 = case files nobody is responsible for
- 2+3 without 1 = task management with no matter of record

### L1 — Common Mature Structure

Present across the sampled products; expected in mature implementations but not definitional:

- multiple intake channels (web forms/portals, phone, email, walk-in, referral, citizen mobile reporting)
- person/constituent records with roles on the case (participants, households)
- case notes, documents/attachments, activity history
- tasks, checklists, and deadline tracking inside the case
- per-case-type configurable workflows and statuses
- constituent communication and status visibility (notifications, letters, portal)
- reporting on caseload, outcomes, and compliance
- role-based access control and audit trail

### L2 — Variant / Optional Structure

Depends on domain, agency level, and deployment:

- program/benefit machinery: eligibility determination, program enrollment, benefit assignment (social-programs pole)
- care plans with goals/tasks assigned to the constituent (human-services pole)
- investigation machinery: evidence, custody chain, proceedings, enforcement actions (investigative/enforcement pole)
- GIS/property/parcel anchoring and inspection field apps (local-government pole)
- citizen self-service portals and mobile reporting apps
- cross-agency referrals (inbound/outbound)
- fee/payment processing
- AI assistance (summaries, classification, intake guidance)

### L3 — Vendor-specific (Research Notes only)

- Salesforce: Omni-Channel, Constituent Snapshot, Business Rules Engine, OmniStudio guided flows, Casework Overview console, party relationship groups, benefit session/schedule objects, Agentforce complaint templates.
- CaseWorthy: CORE data lakehouse, apBuilder, Cara AI copilot, ClientTrack/ServTracker/MediSked application split.
- GovPilot: PropertyProfile, GovAlert/GovInspect apps, 125+ module catalog, GIS map.
- Comcate: CRM/311 product, code enforcement manager, animal control manager.

## Vendor-specific Findings

See L3. None of these were promoted to the canonical model.

## Rejected Findings

- "Case management = CRM for government." Rejected: the sampled products center on casework lifecycle and caseload, not on commercial relationship/pipeline semantics. Constituent records exist to serve cases, not deals.
- "Case management = ticketing with different words." Rejected: the caseload/responsible-worker structure and the matter-of-record lifecycle (with program rules and accountability) are structurally distinct from queue-resolved service tickets; see Boundary Findings.
- "Portals, SLA timers, GIS, and AI are part of the definition." Rejected by the historical check: paper case files with caseworker assignment and case history satisfy the core without any of these.
- "Public sector case management is only human services." Rejected: the sampled span covers enforcement/investigative and municipal service-request poles with the same three-part core.

## Boundary Findings

- **vs 311 / Citizen Service Request Platform**: the 311 platform is the citizen-facing intake, routing, and request-tracking surface (often with field dispatch); case management is the sustained worker-held processing of individual matters to resolution. Overlap zone: 311 requests commonly become cases; some vendors sell both (Comcate CRM/311 alongside code enforcement; GovPilot Report-a-Concern feeding department processing). Removal test: remove the sustained casework/caseload layer → 311 platform; remove the citizen-facing intake/routing surface → case management.
- **vs domain case management Types** (Social Services CM, Child Welfare Management, Immigration CM, Law Enforcement CM, Court CM, Prosecutor/PD CM): these add domain-specific structures (placements and safety assessments; dockets and hearings; etc.) on top of the same generic core. This leaf is the cross-domain generic; the domain leaves are specializations. The directory lists them separately; no conflict found, but the relationship should be recorded.
- **vs Business Case Management Platform (§10)**: same case machinery, different sector binding — corporate matters (compliance investigations, audits) vs constituent matters processed under public-service obligations.
- **vs Help Desk / Ticketing System**: ticket = service item in a queue, resolved as fast as possible, customer = requester of support; case = constituent matter held by a responsible worker over time under program rules and public accountability. Ticketing systems lack caseload-of-record semantics; case management lacks queue-resolution-speed as its center.
- **vs Government Records Management**: records management governs retention/disposition of official records; case management works the matter. A closed case may become a record; the two Types meet at closure.
- **vs Permit Management / Government Licensing / Code Enforcement**: domain processing Types with their own structures (plan review, inspections, fee schedules). In local government many "case management" deployments are actually these domain systems; the generic Type is what remains when the domain structures are removed.

## Uncertainties

- Tyler Technologies' product structure could not be verified (403). The largest pure-play vendor's absence means the sample may under-represent legacy on-premise government suites; assertions are calibrated accordingly.
- ServiceNow's government case-management framing could not be fetched; the ticketing boundary is reasoned from sampled products, not from a platform vendor's own framing.
- Comcate's Help Center did not render article content; its evidence is Tier-2 only.
- The exact prevalence of "case" vs "service request" vs "ticket" terminology across the market was not measured; the boundary descriptions are structural, not statistical.
- Non-US markets (UK/AU national and local government case systems) were not sampled; the sample is US-heavy. The canonical core is written jurisdiction-neutrally, but variant emphasis (e.g., statutory timelines) may differ.

## Final Synthesis

A public-sector case management application is the agency's caseworker-facing system of record for individual constituent matters. Its defining core is three jointly-held structures: the case as a persistent unit of record bound to a constituent matter; responsible-worker holding with caseload semantics; and a governed lifecycle from intake to a recorded resolution that accumulates notes, documents, and communications as institutional memory — all bound to public-sector service semantics (program rules, timelines, accountability). Around this core, mature products add intake channels, participant records, tasks and deadlines, constituent communication, reporting, and access control; domain poles (social programs, human services, investigations, municipal enforcement) add variant machinery. The Type is the cross-domain generic of which the directory's domain-specific case management leaves are specializations, and it is distinct from 311 intake platforms, ticketing systems, and records management by the caseload-of-record structure.
