# Research Notes — Construction Labor Management

Research date: 2026-09-07
Slug: construction-labor-management
Directory leaf: Construction Labor Management (§17 Construction, Real Estate & Facilities)

## Research Goal

Understand what "Construction Labor Management" is as an Application Type, from real products: what objects exist, who uses them, how labor is planned/allocated/recorded against construction work, what rules matter (qualifications, certifications, wage/compliance), and where the boundary lies with neighboring Types (Construction Field Management, Employee Scheduling, Time & Attendance, Workforce Management Platform, Subcontractor Management, HRIS/Payroll).

## Initial Boundary (hypothesis before research)

- Hypothesis: software that manages construction workers as a resource — worker rosters, certifications, crew assignments to projects, timesheets, labor compliance.
- Likely confusions:
  - Construction Field Management (daily logs, punch lists — processed separately; overlaps on timesheets)
  - Employee Scheduling Platform / Time & Attendance System (generic HR-family)
  - Workforce Management Platform (generic §09)
  - Subcontractor Management (contract-side vs worker-side)
  - Construction Project Management / Construction Scheduling (project activity schedules vs labor resource)
- Unknowns going in:
  1. Is this a real standalone product category or only a module of construction PM suites?
  2. Is time capture definitional, or do planning-only products (no timesheets) still belong?
  3. Is certification/compliance tracking definitional?
  4. Does the Type include site-presence/access-control products (badging, turnstiles)?

## Research Questions

1. What is the core "thing" being managed — worker, crew, role, project, shift, timesheet?
2. How does allocation work (who decides, on what surface, matched by what)?
3. How are qualifications/certifications stored and used — advisory or enforced?
4. How is time/presence captured and where does it go (payroll, job cost)?
5. What reporting/compliance outputs exist (headcount, utilization, wage rules, fatigue)?
6. What are the product poles (planning vs field ops vs site tracking vs time tracking)?
7. Who is the worker population — contractor-internal staff, craft labor, or multi-employer site workforce?
8. Where is the boundary vs generic scheduling/T&A and vs field management?

## Representative Products

Selected for market representativeness + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Self-positioning (observed) |
|---|---|---|---|
| Assignar | field operations: crew scheduling + time + forms + compliance + T&M/job costing | mid-market subcontractors (civil, crane, rail, concrete…) | "construction platform that connects Field to Finance" |
| Bridgit Bench | workforce planning: people/roles/projects allocation + forecasting | large general contractors | "AI workforce planning for construction" |
| Eyrus | site workforce tracking: registration, credentials, presence, time, access | large sites; GC/owner-driven programs | "Construction Worksite Intelligence Platform" |
| ClockShark (boundary probe) | construction time tracking (GPS, crew punch) | SMB contractors | "time tracking" platform (help guide) |

LaborChart (a prominent "workforce management for construction" product) was intended as a sample but could not be reached (see Sources / limitations).

## Sources

Fetched 2026-09-07:

- Assignar homepage — https://assignar.com/ (A)
- Assignar scheduling product page — https://assignar.com/scheduling-assigning/ (A)
- Assignar time-tracking product page — https://assignar.com/time-tracking-field-data/ (A)
- Bridgit homepage — https://gobridgit.com/ (A)
- Bridgit Knowledge Base index — https://support.gobridgit.com/hc/en-us (A)
- Bridgit KB article "Certifications" — https://support.gobridgit.com/articles/2628106903-certifications (A)
- Bridgit KB article "Crew Management" — https://support.gobridgit.com/articles/5833024303-crew-management (A)
- Eyrus homepage — https://eyrus.com/ (A)
- Eyrus Workforce page — https://eyrus.com/workforce-management (A)
- ClockShark Help Guide — https://help.clockshark.com/ (A)

Failed / abandoned sources (per network-limitation rule, 1–2 failures then drop):

- https://www.laborchart.com/ (404), https://laborchart.com/ (transport error), https://help.laborchart.com/ (404) — LaborChart not sampled; no claims in this research rely on it.
- https://support.assignar.com/hc/en-au (timeout, then transport error) — Assignar help-center articles not reached; Assignar evidence limited to its main-site product pages.
- https://www.clockshark.com/ (403) — ClockShark main site blocked; evidence limited to its public help-guide index.

Evidence layers used below: **A** = directly observed on a fetched official page of a specific product; **B** = observed across multiple products in the sample; **C** = canonical inference from cross-product comparison and boundary reasoning.

## Product Observations

### Assignar (A)

From homepage + scheduling + time-tracking pages:

- Self-positioning: "construction platform that connects Field to Finance"; "Built by Contractors, for Contractors"; target industries: civil infrastructure contractors (crane, excavation, rail, concrete, asphalt, demolition, traffic, scaffolding).
- Feature spine (marketing nav): Pay Rates, Job Costing, Schedule of Rates (T&M), Scheduling, Time Tracking, Forms & Field Data, Safety and Compliance, Reporting & Analytics, Progress Tracking, Integrations; separate products: Assignar Operations, Assignar Pay, AI assistant ("Milo").
- Scheduling model (A):
  - "Work orders" are created and "automatically populate into the Scheduler, ready to be filled with the resources that can do the job."
  - Drag-and-drop resources onto the calendar to schedule them; immediate notifications.
  - "Smart Allocations": resources carry "availability and certifications" so schedulers "find and schedule them in seconds."
  - Recommendation engine: "recommends qualified and available workers for a job."
  - Jobsite app: assignments upload into the worker app; schedulers can "text workers directly from the Scheduler"; supervisors can "add or remove workers to shifts using the app, and push shifts to the next day."
  - Reporting from scheduling data: utilization, overtime frequency.
  - Equipment is scheduled alongside workers ("Schedule Crews & Equipment", "people and equipment… at a glance").
- Time model (A):
  - Workers "confirm shifts, clock in and out, and fill out their timesheets" in the mobile app.
  - "Supervisors can do this for an entire crew in under a minute, with our bulk timesheet capability."
  - "Activity Breakdown": shifts broken up by activity; time tracked against activity "with equipment, too"; break times tracked.
  - "Timesheet Review page" in the office shows "the status of each worker's time sheets"; notes from the jobsite arrive with submission.
  - Timesheet data syncs "directly into your ERP and accounting systems automatically at your chosen interval."
- Crews exist as an operational unit (crew timesheets; crew scheduling) (A).

### Bridgit Bench (A)

From homepage + KB (Certifications, Crew Management) + KB index:

- Self-positioning: "Workforce planning software for contractors" / "AI workforce planning for construction"; customers: GCs, self-perform GCs, specialty contractors; "trusted by nearly 40% of top contractors" (marketing claim, not operational evidence).
- Platform pillars (A): Project Planning ("plan projects, roles, and staffing in one place"), Forecasting ("match your project pipeline to your people… where gaps are forming, when to hire, whether you can take on the next bid"), Internal Resumes ("job history, skills, certifications, location, and availability" per person), Communication ("assignment alerts via SMS or email, project-wide announcements, notes on profiles"), Integrations ("sync project, pursuit and people data" from CRM, HRIS, project systems), Bridgit AI (agents that "propose a full team" for open project roles; custom reports).
- Core planning objects (A, KB): People; Projects; Roles (project demand that people fill); Assignments (people placed into roles); Crews.
- Crews (A, KB "Crew Management"):
  - A crew = "a team responsible for a specific scope of work — with a defined composition and often a reporting hierarchy."
  - Two forms: **preset crews** (saved, named groups of people, optional trade attribute, used for "fast bulk assignment across projects… crews who travel from job to job together") and **project crews** (labels organizing roles on one project).
  - Assigning a preset crew to a project is a single drag-and-drop action; "Crew assignment places people into unfilled roles" — it does NOT override existing role assignments (explicit).
  - A person can belong to multiple preset crews but only one crew on a project at a time.
  - Permission-gated: "Manage People", "Manage Roles & Assignments", "Manage Roles".
- Certifications (A, KB "Certifications"):
  - Organization-defined master certification list; certifications assigned to people with expiration dates and per-type warning ranges; documents attached (public or private).
  - Status color coding: gray valid / orange approaching expiry (days shown) / red expired; people list shows certification abbreviations with color coding; filter workforce by certification status; Snapshot dashboard shows an "Expiring Certifications" metric.
  - **Enforcement posture (explicit): "Bridgit does not automatically prevent you from assigning someone with an expired certification to a project—it's a visual alert system to help you maintain compliance."**
  - Certifications may be non-expiring (degrees, one-time trainings).
- People domain also includes: Time Off, Experience Tracking, Profiles (KB related-articles and collection names) (A).
- Notably ABSENT from all fetched Bridgit surfaces: clock in/out, timesheets, payroll handoff. Bridgit is a planning/allocation pole; time capture is not part of its offering (A — absence observed on homepage + KB index + 2 articles).

### Eyrus (A)

From homepage + Workforce page:

- Self-positioning: "The Worksite Intelligence Platform" / "Construction Worksite Intelligence Platform"; "Construction worker registration, time tracking, access control, video surveillance and more."; audience: GCs, owners/developers, subcontractors, safety managers, security personnel, field engineers.
- Workforce solution scope (A): "Registration, onboarding, communication, time tracking, payroll, and reporting."
- Worker registration & onboarding (A):
  - "Collect worker name, cell phone, trade, company"; collect certifications; orientation videos with multilingual support and engagement tracking; signatures; background checks; custom fields.
  - "Your workforce database will have alerts and reporting, so you maintain compliant worksites."
- Time tracking & payroll (A):
  - Multiple capture methods: worker app self check-in; worker app/digital badge + foreman app (worker taps badge against a separate foreman device); kiosks; hand scanners; BLE beacons/badges + readers at entry/exit points and in zones; access control via turnstiles ("total time spent on site"), vehicle gates/guards, doors/gates/trailers with zone tracking.
  - "Leverage zones for tracking work in certain areas or tracking various wage rates."
  - "Eyrus automatically creates timesheets for each worker." Timesheets go to "common payroll systems."
  - Access control described as "the most accurate and objective time tracking for construction"; "Objective Comparisons: have one source of truth with other contractors" (GC vs subcontractor headcount/hours disputes).
- Communication (A): SMS to all workers with saved communication groups (site updates, safety updates, urgent messages, weather/emergencies, news/events).
- Reporting (A): Headcounts and Workhours, Project Dashboard, Portfolio Dashboard, Worksite Zones, Certifications Tracking, Local Wage & Regulations, Worker Fatigue Reports, Custom Reports.
- Adjacent bundles (A, same vendor): access control hardware (turnstiles), video surveillance, site security, safety system, conditions monitoring, AI assistant ("Lens"), evacuation/mustering, zone management. These are separate solution lines around the workforce core.
- Multi-employer dimension: worker records carry "company"; headcounts "separated out by subcontractor" (customer quote); subcontractors given "authority to manage their workforce and work zones within Eyrus."

### ClockShark (A — boundary probe)

From public help-guide index only (main site returned 403):

- Self-identity: time tracking for construction/field service; "All-in-one platform" includes: Set Up Employees, Track Time (incl. "CrewClock to punch your crew in via mobile"), GPS requirements, GPS location sharing & privacy, mobile app, integrations (QuickBooks Online), reports, quotes & invoices.
- The center of gravity is time capture (GPS-verified punch, crew punch, reports, payroll sync); scheduling/quotes exist as surrounding features.
- Interpretation: a construction-specialized Time & Attendance product. Useful to test whether pure time tracking is in-family for Construction Labor Management.

## Cross-product Comparison

| Structure / capability | Assignar | Bridgit Bench | Eyrus | ClockShark | Layer |
|---|---|---|---|---|---|
| Identified worker records (person-level, not anonymous labor) | ✔ (workers as schedulable resources) | ✔ (People, profiles/"internal resumes") | ✔ (worker registration database) | ✔ (employees) | B |
| Construction-work attributes on workers (trade/skills/qualifications) | ✔ (certifications + qualifications feed matching) | ✔ (skills, experience, certifications, trade on crews) | ✔ (trade collected at registration) | (trade not observed) | B (3/4) |
| Construction work as allocation anchor: projects / jobs / work orders / sites | ✔ (work orders, scheduler) | ✔ (projects + roles) | ✔ (sites, project & portfolio dashboards) | ✔ (jobsites w/ GPS) | B |
| Planned allocation of labor to work (assignment/scheduling of people & crews) | ✔ (scheduler, drag-drop, recommendation engine, shifts) | ✔ (role assignment, crew bulk assignment, forecasting) | — (records actual presence, not planned allocation) | (limited; not the focus) | B (2/4 strong) |
| Recorded labor against work (time/presence: clock in/out, badge, GPS, turnstile) | ✔ | — (absent from offering) | ✔ (app/badge/BLE/turnstile; auto timesheets) | ✔ (core) | B (3/4) |
| Crew as a managed unit | ✔ (crew timesheets; crew scheduling) | ✔ (preset + project crews, bulk assign) | partial (foreman app; groups) | ✔ (CrewClock crew punch) | B |
| Certification tracking with expiry alerts | ✔ (certs feed qualified-matching) | ✔ (master list, warning ranges, color status, dashboard metric) | ✔ (collected at onboarding; certification reports) | not observed | B (3/4) |
| Enforcement of expired credentials | recommendation-shaped ("qualified & available" matching); no blocking observed | explicitly advisory only (does not block assignment) | gate-adjacent: certifications collected before site entry (access control pole) | — | varies by product |
| Worker notification / mass communication | ✔ (text from scheduler) | ✔ (assignment alerts SMS/email, announcements) | ✔ (SMS groups incl. emergency mustering texts) | not observed | B (3/4) |
| Time → payroll / ERP / accounting handoff | ✔ (ERP/accounting sync; Assignar Pay) | — (HRIS/CRM/project-data sync instead) | ✔ (payroll systems) | ✔ (QuickBooks) | B (3/4; planning pole replaces with HRIS sync) |
| Reporting on labor (headcount, hours, utilization, overtime) | ✔ (utilization, overtime) | ✔ (workforce dashboards, forecasting reports) | ✔ (headcounts & workhours, zones, fatigue, wage regs) | ✔ (reports) | B |
| Availability / time off | ✔ (availability in smart allocations) | ✔ (availability; Time Off) | — | — | B (2/4) |
| Multi-employer site workforce (workers from many subcontractors on one project) | (contractor-internal focus) | (contractor-internal staff + craft) | ✔ (company field, headcount by sub, GC/sub dispute resolution) | — | product-specific emphasis |
| Demand forecasting vs opportunity pipeline / hiring gaps | — | ✔ (forecasting pillar) | — | — | product-specific |
| Mobile field capture for workers | ✔ | — (mobile app is planner-side) | ✔ | ✔ | B (3/4) |
| Equipment co-scheduling with labor | ✔ | — | — | — | product-specific |
| Compliance-shaped reports (local wage & regulations, fatigue) | ✔ (compliance forms; CA-compliance content) | (cert compliance only) | ✔ (wage & regulations, fatigue) | — | B (2/4) |
| AI assistance | ✔ (Milo) | ✔ (agents proposing teams) | ✔ (Lens) | — | B (3/4) |
| Hardware-adjacent (turnstiles, BLE, badges) | — | — | ✔ | (GPS only) | product-specific |

### Evidence synthesis

- Layer B findings (cross-product): worker-level records; construction-work attributes; project/job/site as anchor; planned allocation and/or recorded time as the two complementary forms; crews; certification tracking with expiry signaling; worker notification; reporting on headcount/hours/utilization; payroll/accounting or HRIS handoff.
- Key asymmetries: planning products (Bridgit) lack time capture; time products (ClockShark) lack allocation depth; site-tracking products (Eyrus) record presence instead of planned assignments; field-ops products (Assignar) span both.
- Enforcement of credentials is NOT uniform: at least one product is explicitly advisory-only; others shape recommendations around qualification; none of the sampled products was observed hard-blocking assignments based on expired credentials (absence of evidence, not evidence of absence — assertion kept weak).

## Canonical Abstraction

### L0 — Defining Invariant

The Type answers one question for a construction organization: **who (identified workers, each carrying construction-work attributes) works on what (construction work: projects/jobs/sites), when — and the answer is tracked.**

Minimal structures:

1. **Worker population as managed records** — identified individual workers (not anonymous headcount), each carrying work-relevant attributes (at minimum trade/skill and availability or placement; certifications/pay attributes are common but not required).
2. **Tracked placement of labor against construction work over time** — in *planned* form (workers/crews assigned to projects, roles, work orders, shifts) and/or in *recorded* form (presence/hours on the work). Either form alone satisfies the Type; mature products typically offer at least one and many offer both.

Removal tests:

- Remove worker-level records → the system manages tasks/assets, not labor (falls into project mgmt / equipment mgmt).
- Remove tracked placement (no assignments, no time/presence) → an HR roster/HRIS, not labor management.
- Remove the construction-work context (projects/jobs/sites + craft attributes) → generic workforce management / employee scheduling.

### L1 — Common Mature Structure

- Worker profile with trade, skills, certifications, experience, availability, contact channel.
- Crew as a named, reusable team unit (preset/saved crews and project-scoped crews; bulk assignment).
- Project/job role demand (roles/positions to fill), with matching of qualified + available workers (recommendation-shaped assistance is common).
- Time capture & timesheets with review (mobile clock in/out; supervisor bulk crew entry; activity/break/equipment breakdown in field-ops products) and review queue before approval.
- Certification/credential tracking with expiry warnings and compliance dashboards.
- Worker notification (SMS/email of assignments and site-wide messages).
- Reporting: headcounts, hours, utilization, overtime; certification-expiry metrics.
- Handoff: time → payroll/ERP/accounting; people data ↔ HRIS; project data ↔ project systems.
- Mobile capture surfaces for workers and supervisors.

### L2 — Variant / Optional Structure

- Product pole (the dominant variant axis):
  - *workforce planning* (GC-side allocation of staff + craft against projects and pipeline; forecasting; no time capture),
  - *field operations* (subcontractor scheduling + time + forms + T&M/job costing),
  - *site workforce tracking* (registration, credentials, presence, access, mustering for large multi-employer sites),
  - *construction time tracking* (SMB GPS time capture — boundary case toward Time & Attendance).
- Workforce scope: contractor-internal staff and craft (planning pole) vs site-wide multi-employer workforce across subcontractors (tracking pole).
- Compliance depth: prevailing-wage / certified-payroll and union-reporting regimes (regional, e.g. US public works), fatigue rules, local wage & regulation reporting.
- Demand forecasting against opportunity pipeline; hiring-gap modeling.
- Hardware-coupled capture: turnstiles, BLE readers/badges, kiosks, hand scanners; zone-based wage-rate tracking.
- Equipment co-management alongside labor.
- Emergency mustering / evacuation headcount.
- AI assistance (team-proposal agents, site assistants).
- Deployment: SaaS; hardware-bundled vs pure software.

### L3 — Vendor-specific (kept out of final document)

- Assignar: work orders as scheduling primitive; Schedule of Rates (T&M); job costing; Assignar Pay; Milo AI; forms engine; CraneOps/InfraOps/TrafficOps industry packages; "60% more efficient"-class marketing metrics.
- Bridgit Bench: Bridgit AI agents ("propose a team"), Bridgit MCP, Snapshot dashboard metric names, Strategic-Account-Manager-mediated CSV import, module licensing (Crews module enablement).
- Eyrus: Lens AI assistant, Perry Weather integration, BLE hardware specifics, visibility app, portfolio dashboards.
- ClockShark: CrewClock, geofence specifics, quotes & invoices module, 2024 app migration.

## Boundary Findings

- **vs Construction Field Management** (separate directory leaf, processed 2026-09-07): Field Management's defining core is the *day record* (site activity log) + *field work items* (punch/deficiency items). Labor Management's defining core is the *worker population + placement*. Overlap: both may carry crew timesheets. Discriminator: remove the day-record/work-item machinery and a field-management product collapses; remove worker-allocation and a labor-management product collapses. Timesheets in field management feed the day record; in labor management the worker/time record IS the product. Joint review recommended.
- **vs Time & Attendance System (§09)**: pure construction time tracking (probe product) is a Time & Attendance realization specialized to construction (GPS jobsites, crew punch). It satisfies L0 (recorded placement) but sits at the family edge; the canonical center includes allocation. Products that are *only* time capture are better filed as T&A variants.
- **vs Employee Scheduling Platform (§09)**: generic scheduling manages shifts against demand; construction labor management anchors allocation to projects/jobs with craft-qualification matching and crew semantics. Shift mechanics (Assignar shifts) are one realization inside a project-anchored world.
- **vs Workforce Management Platform (§09, generic)**: the generic Type spans forecasting→scheduling→compliance for any industry; Construction Labor Management is the construction-industry specialization with projects/jobsites/crews/craft credentials as its world. Taxonomy keeps both; the relationship is industry-specialization, not duplication.
- **vs Subcontractor Management**: manages contracted firms and their contracts/compliance; labor management tracks workers (including subcontractors' workers as records on a site) but not the contract relationship. Eyrus's "headcount by subcontractor" is the seam: worker-level tracking vs firm-level management.
- **vs Construction Equipment Management**: parallel resource Type (equipment as managed asset). One sampled product schedules crews and equipment in one scheduler — co-management is a variant, not a definitional structure.
- **vs Construction Project Management / Construction Scheduling**: PM owns project plan/activities/cost; labor management owns the labor resource. A project schedule may drive labor demand, but the labor record and allocation live here.
- **vs HRIS / Payroll System**: HRIS owns employment master data and payroll owns pay execution; labor management consumes worker records and hands off time. Worker onboarding at the site (orientation, credentials-before-entry) is operational, not HR-administrative.
- **vs Construction Safety Management**: certification tracking and orientation overlap; safety management's core is the safety program (incidents, observations, inspections). Labor management uses credentials for *allocation eligibility*, safety management for *safety outcomes*.

### "Remove what, and it becomes another Type" summary

- Remove worker-level allocation & placement → Construction Project Management / Field Management.
- Remove projects/jobsites/crews/craft context → Employee Scheduling / generic Workforce Management / Time & Attendance.
- Remove labor and keep firms/contracts → Subcontractor Management.
- Remove labor and keep machines/assets → Construction Equipment Management.

## Historical / Market-Sample Check

- Pre-digital practice: craft qualification cards/rosters (worker records with trades), the superintendent's crew board (planned placement), foreman time cards (recorded time). All satisfy L0 → the definition does not depend on cloud, mobile apps, GPS, or AI.
- Regional breadth: union-hall dispatch (worker availability + assignment to jobs), European/Australian civil subcontracting (Assignar's AU heritage), US prevailing-wage regimes — all fit worker-records + placement.
- Naming breadth: the market calls this family "labor management", "workforce management", "workforce planning", "field operations", "workforce tracking" — the L0 abstraction (workers + tracked placement against construction work) covers all naming variants.
- Anti-overfitting check: "certification expiry dashboards" and "AI" are current-market patterns, not invariants (older products and the probe product lack them). "Time capture" is extremely common but NOT definitional (planning pole lacks it while remaining squarely in-family).

## Uncertainties

1. LaborChart could not be fetched (site unreachable); it is commonly cited as a flagship of this category. Its absence is a coverage gap, mitigated by having both the planning pole (Bridgit) and field-ops pole (Assignar); no claim depends on it.
2. Assignar help-center unreachable; Assignar evidence rests on main-site product pages (marketing-operational hybrid). Detailed mechanics (e.g., exact timesheet approval flows) not verified.
3. ClockShark evidence limited to its help-guide index (main site 403); used only as a boundary probe.
4. Whether any product in the wider market *hard-blocks* assignments on expired credentials is unverified; sampled evidence shows advisory/recommendation postures only. Assertion kept weak ("varies; commonly advisory").
5. Extent of certified-payroll (Davis-Bacon-type) machinery inside this Type vs inside payroll products is not fully resolved; treated as a regional compliance variant with payroll handoff as the seam.
6. Boundary with Construction Field Management on timesheets requires the joint review noted above.

## Final Synthesis

Construction Labor Management is the application Type that manages construction labor as an allocatable, trackable resource. Its defining structure is small: identified workers carrying construction-work attributes, plus tracked placement of that labor against construction work over time — planned (assignments to projects/roles/crews/shifts) and/or recorded (presence and hours on the work). Around this core, mature products add crews, role demand and qualified-matching, time capture with review and payroll handoff, certification tracking with expiry signaling, worker notification, and labor reporting. The market realizes the Type through four recognizable poles — workforce planning, field operations, site workforce tracking, and construction time tracking — distinguished by whether placement is planned, recorded, or both, and by whether the workforce is contractor-internal or site-wide multi-employer. The Type ends where labor stops being the managed object: project schedules and costs (PM), day records and work items (field management), firms and contracts (subcontractor management), machines (equipment management), employment and pay (HRIS/payroll).
