# Research Notes — Construction Scheduling

Research date: 2026-09-07

## Research Goal

Understand what a Construction Scheduling application actually is as an Application Type: the core objects it manages, the work its users perform, how the schedule is built / calculated / maintained, which structures are defining vs merely common in today's market, and where the boundary lies against Construction Project Management, Lean Construction Planning, and other neighbors.

## Initial Boundary

- Hypothesis: software whose object of record is the **construction project schedule** — a structured, dated work plan of the project's activities — computed from activity logic (CPM tradition), baselined, and updated as the project progresses.
- Users: planners/schedulers, project managers, superintendents, trade partners, owners' representatives, project-controls teams.
- Closest neighbors: Construction Project Management (§17 sibling, processed — that pass explicitly declared the schedule dimension NOT definitional there), Lean Construction Planning (§17 sibling, unprocessed), Project Controls Platform (§17 sibling, unprocessed), generic Project Management Application (§03.07), Production Scheduling / Call Sheet (§27, different domain), APS (§16, manufacturing).
- Unknowns going in: whether the directory leaf collapses into Construction Project Management; how much the lean/Last Planner pole overlaps; whether the AI-generation products are still this Type; whether light residential schedulers force a weaker definition.

## Research Questions

1. What is the core object model? (activities, relationships, calendars, milestones, WBS/codes, resources, cost)
2. What does the calculation engine do, and is calculation definitional? (forward/backward pass, float, critical path)
3. How is the schedule built? (from scratch, templates/task pools, import from other schedule formats)
4. How does the update cycle work? (progress capture, recalculation, data/status date, variance)
5. What is the baseline machinery and why does it exist?
6. What planning surfaces exist beyond the master schedule? (lookaheads, pull plans, 4D, what-if scenarios)
7. Who uses it and with what permissions? (planner vs field vs partner vs owner)
8. What integrations/interchange formats are canonical? (P6 XER, MS Project MPP/MPX)
9. Where do lean/commitment workflows and AI optimization sit relative to the definition?

## Representative Products

| Product | Pole | Customer tier / philosophy |
|---|---|---|
| Oracle Primavera P6 EPPM | enterprise CPM engine | owner/GC/infrastructure; "the standard for planning and scheduling" |
| Asta Powerproject (Elecosoft) | construction-specialist desktop/enterprise CPM | UK/Europe strong, mid-market to megaproject; Gantt-first editing |
| Procore Scheduling / Project Schedule tool | PM-suite-embedded scheduling, field-connected | GC platform; schedule shared with whole project community |
| ALICE Technologies | AI generative scheduling / optioneering | large GCs/owners; scenario generation on top of P6/MSP schedules |
| Touchplan (MOCA Systems) | lean collaborative planning (Last Planner) | GC + specialty contractor collaboration; lookahead-centric |

Microsoft Project noted as the widely used general-purpose tool in the space; **not directly verified** in this pass (support site blocked/redirected) — no product-specific claims made for it.

## Sources

- Oracle Primavera P6 EPPM product page — oracle.com/construction-engineering/primavera-p6/ (fetched 2026-09-07)
- P6 EPPM v26 documentation library — docs.oracle.com/cd/G48897_01/ (index, guides node, user-guides node)
- P6 EPPM v26 help — "P6 Overview" + "Working with P6" (docs.oracle.com/cd/G48897_01/p6help/en/)
- P6→Oracle Primavera Cloud migration guide "About this Content" — docs.oracle.com/cd/E80480_01/English/admin/p6_eppm_migration_guide/213347.htm
- Elecosoft — Asta Powerproduct page (eleco.com/products/asta/asta-powerproject/), Asta Enterprise page (eleco.com/products/asta/asta-enterprise/)
- Procore — Support home (support.procore.com/), Project Schedule tool user guide (support.procore.com/products/online/user-guide/project-level/schedule), FAQ "What is a construction project's schedule?", construction scheduling software product page (procore.com/project-management/schedule)
- ALICE Technologies — alicetechnologies.com homepage (products/FAQ), DCMA schedule-check whitepaper landing (blog.alicetechnologies.com/whitepapers/overview-of-dcma-schedule-check)
- Touchplan — touchplan.io homepage
- Fetch failures / blocks: docs.oracle.com construction-engineering index path (404), procore.com/en-us/scheduling & /en-us/products/scheduling & /en-us/project-management (404 — correct paths found later), support.procore.com v2 scheduling manual (timeout ×2 — abandoned), support.microsoft.com/project (redirected to Planner), microsoft.com product page (bot-blocked), buildertrend.com (403), openproject.org docs path (404), duckduckgo search (timeouts).

---

## Product Observations

### Oracle Primavera P6 EPPM (evidence layer A unless noted)

- Positioned as "the standard for planning and scheduling"; manages "projects, programs, and portfolios", on-premises or cloud.
- Marketing headline capability: **"Primavera P6 CPM Schedule"** — "Plan, schedule, and control large-scale programs and individual projects; secure multiuser access to schedules; open and schedule multiple projects simultaneously; adaptable views; team member interfaces for gathering status updates."
- Help structure ("Working with P6"): main sections — Dashboards (portlets), Portfolios, **Projects** ("the working core": WBS, activities, risks, issues, Gantt charts, calendars, expenses, resource assignments), Resources (roles/teams), Approvals (timesheet and **status-update approvals**), Reports, Administration (enterprise data: codes, UDFs, **calendars**, roles, units of measure shared across the application).
- Roles named in help: project managers, activity owners, resources, executives, financial executives (earned value).
- Import/Export guides exist as a first-class doc family (interchange of schedule data is a formal product surface; XER/XML formats referenced from the migration guide).
- P6→Oracle Primavera Cloud migration guide: OPC "combines CPM contract scheduling and task management in a single cloud environment"; migration moves projects, WBS, activities, relationships, calendars, baselines, resources etc.; P6 concepts carry over with terminology differences.
- Integrated cost & schedule marketing: cost codes in Unifier tied to cost/work breakdown structures in P6; **time-phased baseline** fed by P6 drives forecast comparison; activity sheet lets PMs/team members track schedule progress "without having to access Primavera P6 directly or wait for updates from schedulers".
- Resource management pole: role/resource optimization, demand & capacity planning, what-if scenarios, graphical utilization analysis.

### Asta Powerproject / Asta family (evidence layer A)

- "Planning and project management software... used on projects of all sizes", "purpose built for construction"; 100,000+ professionals claim; UK/EU heritage, 12 language versions.
- Build workflow described explicitly: "Task pools and code libraries make it easy to build and visualise your plan in minutes. **Drawing and linking tasks for critical path analysis** and assigning codes, calendars, resources, and costs can all be done intuitively from within the Gantt chart."
- Family structure: Powerproject (planning + risk analysis), **Asta Enterprise** (multiple users working in the same programme simultaneously, central shared resources across projects), **Asta Siteprogress** (iOS/Android companion for site staff to update project progress "at any time from any location"), **Asta Vision** (web portal for managing Powerproject plans / stakeholder reporting), **Asta 4D** (4D BIM planning), **ProjectViewer** (free viewer for stakeholders without a licence).
- Regional depth: training course "Satisfying NEC Requirements using Powerproject" (NEC contract programme practice), customer stories from UK contractors (Kier, HG, Bouygues, Skanska) plus mining (Peru), Australia (Kapitol).
- Licensing: single, concurrent server, SaaS cloud subscription; Windows desktop base with Mac via SaaS; mobile via separate Siteprogress licence.

### Procore Scheduling (evidence layer A)

**Legacy "Project Schedule" tool** (support docs):
- "The Schedule tool enables you to keep your team up-to-date by giving them a real-time view of the current project schedule. You can create, edit, and share schedules, along with integrating your Primavera P6 or MS Project schedules."
- Import existing schedules created in Microsoft Project, Primavera P6, MPX (also Asta Powerproject / Phoenix via Procore Drive desktop integration); create editable schedules; calendar items (public/private) assignable to users and contacts; view by day/week/month or Gantt; track progress by resource group or individual.
- **Lookahead plans** are a first-class artifact: create lookahead from the schedule, add/manage subtasks, activity feed, change history, follow-up lookaheads; FAQ exists for whether master schedule updates when a lookahead changes.
- **Schedule change requests**: collaborators request changes; schedule owners review them (two-tier edit governance).
- Percent-complete updates by users with a specific permission (field progress input into the schedule record).
- Granular permissions matrix (None / Read Only / Standard / Admin) per action; mobile apps with offline caching; notification emails (weekly project/resource schedule emails).
- FAQ definition: "a construction project's schedule outlines each step that should be completed by a specific date before the next step can be taken... a project manager maintains the schedule, and a superintendent verifies if the subcontractors and all responsible parties show up for work at the time they are assigned."

**Native "Procore Scheduling" (modernized experience)** (product page):
- "Build schedules that connect planning to execution"; import from P6/MS Project "or build new schedules from scratch"; automatic sync from P6/MSP "with automatic updates"; "collaborate in real time from the desk to the dirt with lookaheads and tasks".
- "Designate specific team members and trade partners to activities"; "track accountability across every activity"; "coordinate trades using **live dependencies**"; "monitor the **critical path** and manage task links".
- Filters/columns panel; Gantt ↔ list views; digital lookaheads where field staff/trades break down upcoming work into short-term tasks; schedule delays traceable to project activities like RFIs and observations; Procore Analytics portfolio roll-up; multilingual.
- v2 support manual for the scheduling product exists but was unreachable (timeouts) — deeper CPM semantics of the native engine not directly verified.

### ALICE Technologies (evidence layer A for positioning/flows; B for market claims)

- "AI-powered generative construction scheduling"; automates what-if scenario exploration; FAQ: "ALICE differs from traditional or legacy CPM scheduling software by automating the creation of optimal resource-loaded schedules".
- Three products: **ALICE Plan** (upload schedule + drawings → 2D visualization on drawings, Gantt sorted by WBS or custom properties, canvas to adjust sequences/relationships/filters, timelapse playback, review/share/export); **ALICE Optimize** (import P6/MSP schedule → define optimization goal → "ALICE rapidly simulates scenarios" → solutions on a time-vs-cost graph → select/export); **ALICE Model** (import BIM model → add "recipes" = means & methods → generate baseline schedule → run what-ifs under constraints).
- Import surfaces named: Oracle Primavera P6, Microsoft Project, Oracle Primavera Cloud — evidence that the P6/MSP schedule file is the industry's interchange artifact.
- Schedule Quality Score based on the **DCMA 14-Point Assessment** ("evaluates your schedule for logic, realism, and reliability"); Schedule Insights Agent ("chat" with your schedule); construction optioneering; risk modeling; recovery/acceleration planning; bid-phase use by GCs/owners/consultants; project types: industrial/infrastructure/commercial.

### Touchplan (evidence layer A)

- "Collaborative construction planning and scheduling software" — "cloud-based, real-time platform for general contractor and specialty contractor collaboration"; owner analytics.
- Lean machinery front and center: "Implement the **Last Planner System**, **Pull Plans**, and **Lookahead Plans**"; "Sync Plans to the **Master Schedule** and transition from long-range pull plans to short-term lookaheads"; patented pull planning (US patent cited).
- Master Schedule Synchronization as a named capability — the product deliberately operates downstream of a master schedule.
- Variance reports / analytics ("schedule performance risk... variance reports showed all the data we needed"); commitment tracking, crew planning; BoardScan (digitizing hand-drawn pull-plan boards).
- Serves GCs, specialty contractors, owners, architects/engineers; mission-critical segments (data centers, healthcare, life sciences, infrastructure).

---

## Cross-product Comparison

| Structure | P6 | Asta | Procore | ALICE | Touchplan | Layer |
|---|---|---|---|---|---|---|
| Project schedule as managed object (activities + dates) | ✔ | ✔ | ✔ | ✔ (generated/imported) | ✔ (master schedule + lookaheads) | universal |
| Dependency logic between activities | ✔ | ✔ ("linking tasks") | ✔ ("live dependencies", task links) | ✔ (adjust relationships) | ✔ (pull-plan logic → schedule) | universal |
| Calculation engine deriving dates / critical path | ✔ (CPM) | ✔ (CPM "critical path analysis") | ✔ ("monitor the critical path") | ✔ (simulates + CPM baseline) | derived via master sync | universal in the sampled dedicated schedulers |
| Calendars / working-time handling | ✔ (enterprise calendars) | ✔ (assign calendars in Gantt) | implied (dates/views) | ✔ (constraints) | implied | strong-common |
| Baseline / plan-of-record vs current | ✔ (time-phased baseline feeds forecasts) | ✔ (implied by scenario/comparison practice; not directly quoted) | ✔ (imported schedules tracked; lookahead change history) | ✔ ("generate baseline schedule"; compare scenarios) | ✔ (master schedule as reference) | strong-common |
| Progress update loop (field in → schedule out) | ✔ (team member interfaces, status-update approvals) | ✔ (Siteprogress mobile) | ✔ (percent-complete permission, change requests) | ✖ (analysis-time, not progress ledger) | ✔ (commitment/crew updates) | strong-common |
| Lookahead planning surface | ✔ (filters/views; lean done via partners) | ✔ (Siteprogress/shorter horizons; not directly quoted) | ✔ (first-class lookaheads + subtasks) | partial (scenario views) | ✔ (core purpose) | strong-common |
| Resource loading / roles | ✔ deep | ✔ (in-Gantt resource assignment; Enterprise shared resources) | ✔ (assign to crews/trade partners) | ✔ (resource optimization) | ✔ (crew planning) | strong-common |
| Cost loading / schedule-cost integration | ✔ (Unifier tie-in) | ✔ (costs & cash flow) | ✔ (analytics) | ✔ (time-cost trade-off) | partial | common, depth varies |
| Schedule quality checks | ✔ (DCMA-class checks via ecosystem; ALICE productizes) | ✔ (risk analysis; checks not directly quoted) | ✖ observed | ✔ (DCMA 14-point score) | ✔ (variance reports) | common (mechanism varies) |
| Interchange with P6/MSP formats | native | Asta↔Procore integration documented by Procore | ✔ (import P6/MSP/Asta/Phoenix/MPX) | ✔ (import P6/MSP/OPC) | ✔ (master sync) | strong-common — the file formats are the ecosystem glue |
| Multi-user / community access | ✔ secure multiuser | ✔ Enterprise same-programme editing | ✔ whole-project community incl. subs | ✔ (owners/GCs/consultants) | ✔ GC + subs + owners | strong-common |
| AI scenario generation | ✖ | ✖ | ✖ | ✔ core | ✖ | single-product (pole) |
| Lean Last Planner workflow | ✖ | ✖ | partial (lookaheads) | ✖ | ✔ core | single-product (pole) |

Stop condition: a sixth product would mostly re-evidence this table.

---

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant

1. **The project schedule as the object of record** — a structured, dated work plan of one construction project's activities (work items/phases/tasks with durations and/or fixed dates, milestones, organized by outline/WBS and/or dependency network), persisting across the project's life. Remove → not a scheduling application at all.
2. **Timing machinery** — the application, not the user's hand, keeps the schedule's timing internally consistent: durations, dependencies, and working-time rules are evaluated to derive and re-derive dates and to show which work drives completion (critical path / float being the canonical outputs). Remove → a task list or calendar, not a scheduler.
3. **The living-plan discipline** — the schedule is maintained through an explicit update cycle (progress and change in → dates recalculated) against a retained plan-of-record (baseline / master schedule), so plan-vs-current variance is always expressible. Remove → a one-shot planning chart / drawing.

Minimal, project-anchored, era-safe: nothing about 4D, AI, resource curves, cost, mobile, or lean.

### L1 — Common Mature Structure (evidence layer B)

- **Gantt chart as the primary editing/reporting surface** (all five; P6 "adaptable views", Asta "intuitively from within the Gantt chart", Procore Gantt, ALICE Gantt sorted by WBS, Touchplan master views) — with calendar and list views common (Procore day/week/month + list; ALICE drawing-canvas overlay as an emerging surface).
- **Dependency model** — finish-to-start as the default relationship, with lead/lag and additional relationship types; constraints (fixed dates) coexisting with logic; out-of-sequence/negative-float situations handled (generic to the CPM tradition; specific semantics kept unverified).
- **Working-time calendars** (P6 enterprise calendars; Asta per-task calendars; industry practice for weather/holiday/shift handling).
- **Milestones** and **outline/WBS grouping + activity codes** (P6 codes; Asta code libraries/task pools; Procore filters by trade/task type; ALICE WBS sorting).
- **Baseline machinery** — retain a plan-of-record, compare current dates against it; multiple baselines common in the CPM pole (P6 time-phased baseline explicitly).
- **Update cycle** — progress captured (percent complete, actual start/finish, sometimes via approval workflows — P6 status-update approvals, Procore percent-complete permission + change requests, Asta Siteprogress) then recalculation against an as-of date; variance vs baseline exposed (Touchplan variance reports named).
- **Lookahead planning** — a derived short-horizon working view for field coordination (Procore lookaheads with subtasks/history; Touchplan lookahead plans; P6/ASTA via filters and mobile updates).
- **Resource and role loading** on activities (all five at varying depth).
- **Schedule-cost linkage** — cost loading of activities or integration with cost systems (P6↔Unifier; Asta costs/cash flow; ALICE time-cost graphs).
- **Schedule quality checks** — logic/float/constraint hygiene checks; DCMA 14-point is the canon ALICE productizes (mature-pole safeguard; absence in one sampled product is the reason it is not higher).
- **Interchange of schedule files** (P6 XER, MS Project MPP/MPX, XML) as the ecosystem glue — evidenced from four of five products' import/export surfaces.
- **Shared/community access with tiered permissions** (P6 secure multiuser; Procore granular permission matrix + read-only partners; Asta Enterprise concurrent editing + free ProjectViewer).
- **Mobile / field update surfaces** (Siteprogress; Procore mobile with offline; P6 team-member interfaces).
- **Reporting/printing** and stakeholder views (P6 reports; Asta Vision/ProjectViewer; Procore emails/PDF).

### L2 — Variant / Optional Structure

- **Engine pole vs collaboration pole**: full CPM desktop/enterprise engines (P6, Asta) vs cloud-collaborative scheduling embedded in a PM platform (Procore) — different philosophies of who touches the schedule.
- **Lean/Last Planner overlay**: pull planning, weekly work plans, commitment tracking, PPC-style variance (Touchplan core; Procore lookaheads partial) — a workflow philosophy layered on the same schedule object.
- **AI generative scheduling / optioneering**: scenario simulation, optimization goals, generated baselines from BIM (ALICE) — positions itself explicitly against "traditional or legacy CPM scheduling software".
- **4D BIM linkage** (Asta 4D; ALICE Model path).
- **Schedule risk analysis** (Asta advertises risk analysis; CPM-pole Monte-Carlo risk products exist in the ecosystem) — optional, often adjacent product.
- **Portfolio/program level** operation (P6 portfolios/EPS; Procore Analytics cross-project).
- **Owner-side schedule review/oversight** (owners as analytics consumers in Touchplan/ALICE; owner review workflows common in the market).
- **Regional conventions** — UK/NEC programme practice (Asta training), US subcontractor-coordination practice (Procore/Touchplan).
- **Residential/SMB template scheduling** — widely present in the market (builder software suites) but **not directly researched this pass**; recorded as a low-confidence pole.
- **Deployment**: desktop (Asta, MSP heritage), on-prem/cloud enterprise (P6), cloud SaaS (Procore, Touchplan, ALICE).

### L3 — Vendor-specific (research notes only)

- P6: EPS/OBS security model, Activity Codes/UDFs enterprise libraries, XER format, Team Member interfaces, Unifier/OPC integrations, status-update approval flow, time-phased baseline feeding Unifier forecasts.
- Asta: ProjectViewer free viewer, Siteprogress separate licence, Vision portal, Enterprise same-programme co-editing, NEC-requirements training track, concurrent licensing.
- Procore: Schedule change requests + review flow, granular permission matrix, Procore Drive desktop integrations (Asta/Phoenix/MS Project), lookahead change-history/activity feed, ACC-based pricing.
- ALICE: Plan/Optimize/Model product split, "recipes" (means & methods parameterization), Schedule Insights Agent (chat), DCMA-based Schedule Quality Score, time-vs-cost solution graphs.
- Touchplan: patented pull planning, BoardScan (whiteboard digitization), master-schedule synchronization as a product pillar.

---

## Boundary Findings

- **vs Construction Project Management (§17 sibling, processed)** — clean and mutually reinforcing. The processed PM pass declares the schedule dimension deliberately NOT definitional for PM ("a flagship category product ships no native CPM"). This pass flips the discriminator: what makes Construction Scheduling its own Type is that the **schedule itself (activity network + computed dates + baseline/update discipline) is the object of record the application owns**. Procore's legacy Schedule tool (import-mostly, change-request governed) illustrates the PM-side implementation; the native Procore Scheduling product crossing into native dependencies/critical path is the same company converging on this Type from the PM side. Remove the calculation engine and schedule ownership → it is a PM tool with a schedule viewer.
- **vs Lean Construction Planning (§17 sibling, unprocessed)** — the softest seam. The schedule object is shared; the workflow differs: Lean/Last Planner centers on collaborative commitment planning (pull plans, weekly work plans, constraint logs, PPC measurement), while this Type centers on the calculated network and baseline discipline. Touchplan sits in the overlap zone (lean workflow + master-schedule synchronization). Discriminator for the lean leaf: if the object of record is the commitment/lookahead workflow and the master schedule is consumed via synchronization, it is Lean; if the calculated master schedule is the record, it is this Type. Joint review recommended when the lean leaf is processed.
- **vs Project Controls Platform (§17 sibling, unprocessed)** — controls = governance across cost + schedule + risk + change at program level; scheduling feeds one discipline. P6 itself stretches toward controls (portfolio, earned-value dashboards) — recorded as suite drift. Joint review recommended.
- **vs generic Project Management Application (§03.07)** — generic PM tools share Gantt/dependency structures; the construction-specific Type is distinguished by the construction schedule practice around it: contractual baselines, master-schedule ↔ lookahead discipline, trade/crew assignment, P6/MSP interchange conventions, integration with construction field records. This is an industry-tuned-instantiation seam (similar to manufacturing ERP vs ERP). Microsoft Project — the archetypal general-purpose tool used in construction — could not be verified directly this pass (see Uncertainties).
- **vs Construction Field Management (§17, processed)** — field = daily records/punch/safety; this Type's field-facing surface is only progress reporting into the schedule (and lookaheads outward). Complementary; consistent with the field pass's day-record core.
- **vs Production Scheduling / Call Sheet (§27)** — different domain (film); no shared record model beyond a timeline surface.
- **vs Advanced Planning & Scheduling (§16)** — manufacturing finite-capacity sequencing vs project network logic; different objects (orders/work centers vs project activities).

**Historical / market-sample check (§24 discipline):** Would pre-digital and older products still fit? The type as *software* began by automating network scheduling: hand-calculated CPM networks (1950s–60s) and bar-chart programmes were the practice; early software (Artemis-era mainframe, Primavera P3 1983, MS Project 1984) and today's cloud tools all satisfy L0 — a dated activity plan, machine-derived timing, maintained against a plan-of-record. A pure hand-drawn bar chart without logic has no timing machinery and is pre-software practice (or charting), not this Type. Regional check: UK (Asta/NEC), US (Procore/Touchplan), global enterprise (P6) all fit. The definition does not depend on any single vendor pattern (e.g., P6's EPS or XER are L3).

---

## Uncertainties

1. **Microsoft Project specifics unverified** (support site redirects; product page bot-blocked). No product-specific claims made for MSP in either file; it is acknowledged only as a widely used general-purpose tool whose schedule files (MPP) are an interchange standard — supported indirectly by Procore/ALICE import surfaces (layer A, cross-product).
2. **Procore's native scheduling engine depth unverified** (v2 manual timeouts): "monitor the critical path" and "live dependencies" are direct product-page claims, but exact float/constraint/recalculation semantics were not confirmable. Final document phrases these carefully.
3. **Residential/SMB template-scheduling pole not directly researched** (Buildertrend 403). The final document does not assert specifics for it; the pole is recorded as a market presence with low confidence.
4. **Asta baseline/update details** inferred from product-family structure rather than help-center pages (help docs behind download/support package); assertions kept at product-page strength.
5. **Touchplan/P6/ALICE numeric claims** (dollar volumes, ROI percentages, user counts) are marketing figures — recorded here only, excluded from the final document.
6. **Exact relationship-type semantics** (FS/SS/FF/SF, lag signs, constraint lists) are standard CPM canon but were not re-verified per-product this pass; the final document describes them generically without per-vendor specifics.

## Final Synthesis

A Construction Scheduling application is the scheduling discipline's system of record: it holds the project schedule as a structured, dated plan of activities; it derives timing from the plan's own logic (durations + dependencies + working-time rules) rather than freehand dates, making the critical path and float computable; and it maintains that schedule as a living document — progress flows in, dates are recalculated, and the current plan stays comparable to a retained baseline. Around this minimal core, mature products add the Gantt-first editing surface, calendars, codes/WBS, resource and cost loading, lookaheads, quality checks, file interchange, and tiered community access. Product philosophies diverge by pole: enterprise CPM engines, construction-specialist desktops, PM-suite-embedded cloud scheduling, lean collaborative planning overlays, and AI scenario optimizers — all operating on the same object of record. The schedule-ownership + calculation seam separates it from Construction Project Management; the commitment-workflow seam separates it from Lean Construction Planning.
