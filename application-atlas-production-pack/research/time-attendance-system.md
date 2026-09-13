# Research Notes — Time & Attendance System

## Research Goal

Understand what a Time & Attendance System actually is at the system level (as distinct from the already-documented Employee Time Clock): what objects exist beyond punches and timesheets, how attendance and absence are managed as disciplines, what time-policy machinery exists, how the schedule and payroll interact with the time record, which roles operate the system, and where the boundary sits against Employee Time Clock, Employee Scheduling, Leave & Absence Management, Payroll, Workforce Management, and Time Tracking.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: an organization-side system that records worked time (the time-clock layer), but additionally manages attendance as an ongoing organizational picture (who is present/late/absent/on leave) and administers time policies (overtime, breaks, absence kinds, accruals) as configurable rules applied to the record — the "system" level the Employee Time Clock research identified as its parent Type.
- Likely users: hourly/shift employees (clock in/out, request leave), supervisors (attendance monitoring, exceptions, approvals), HR/time administrators (policy configuration, multi-site administration, compliance reporting), payroll (consumes approved hours).
- Nearest types: Employee Time Clock (nested recording layer), Employee Scheduling Platform (plan side), Leave & Absence Management (absence depth), Payroll System (downstream computation), Workforce Management Platform (broader suite), Time Tracking Application (self-logged task time).
- Unknowns: whether attendance state and absence integration are truly definitional vs merely common; how deep the rules machinery goes in different market poles; regional (statutory) variants; enterprise HCM behavior.

## Research Questions

1. What exists in a T&A system beyond punch→timesheet→approval→payroll (the time clock's whole world)?
2. Is there a standing attendance state/picture (who is in, late, absent, on leave) and how is it surfaced?
3. How is time away from work (leave/PTO) integrated — records, balances, accruals — and where is the seam with worked time?
4. What time rules exist as configurable policy (overtime, breaks, rounding, premiums), and how are they expressed per group/location/union/jurisdiction?
5. How does the schedule/planned work interact with the time record (adherence, late/absent detection)?
6. What compliance machinery exists (labor-law rules, attestation, audit trails, record defensibility)?
7. What clocking surfaces and identity verification exist at system level (hardware, kiosk, mobile, biometrics)?
8. What reaches payroll, and how (export, integration, built-in)?
9. Who uses the system and in which surfaces?
10. Where is the boundary vs Employee Time Clock / Scheduling / Leave / Payroll / WFM / Time Tracking?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, different customer tiers, and different geographies:

| Product | Philosophy / tier | Why selected |
|---|---|---|
| TCP TimeClock Plus (TCP Software) | compliance-first pure-play time & attendance vendor; mid-market/enterprise; US government, education, healthcare, manufacturing | the Type's center of gravity: T&A sold as the whole product with pay-rule/compliance depth and clock hardware |
| Deputy | scheduling-led workforce suite with time & attendance and leave; mid-market; AU/UK/US | plan-side suite where timesheets, leave, and scheduling interlock; strong help-center documentation |
| Personio | European HR suite where time tracking is a Core HR module with statutory compliance orientation; mid-market | regional/regulatory pole (European working-time recording); shows T&A inside an HRIS with absence as a sibling module |
| Jibble | freemium attendance-led time tracker; global SMB; 100k+ teams | market's own articulation of the "time and attendance" category; attendance dashboards and anti-fraud emphasis at the accessible end |

Enterprise HCM suites (UKG/Kronos, ADP, Workday) were not directly reachable (gated/JS-rendered; consistent with the Employee Time Clock research limitation) — enterprise claims are kept general. Rippling's help center was unreachable (SPA); dropped from the sample after two attempts.

## Sources

Fetched 2026-09-08 (official vendor surfaces):

- TCP Software — https://www.tcpsoftware.com/ (root), https://tcpsoftware.com/products/timeclock-plus/ (product), https://tcpsoftware.com/products/timeclock-plus/timekeeping-software/ (timekeeping capability page)
- Deputy Help Center — https://help.deputy.com/ (root), https://help.deputy.com/hc/en-au/categories/4614232027023-Timesheets (Timesheets category), https://help.deputy.com/hc/en-au/categories/17243648734795 / .../17243648734095-Manage-leave (Manage leave category)
- Personio — https://www.personio.com/product/attendance-tracking/ (Time Tracking product page + FAQ), https://support.personio.de/hc/en-us (Help Center root), https://support.personio.de/hc/en-us/categories/200849035-Employee-Management (Employee Management category incl. "Attendance, work schedules, and overtime" and "Time off, leaves, and sick days" sections)
- Jibble — https://www.jibble.io/help (Help Center root), https://www.jibble.io/time-and-attendance-software (Time & Attendance product page + FAQ)

Unreachable / abandoned:

- Rippling help center — help.rippling.com/hc/en-us (404) and help.rippling.com (JS-rendered, empty content) — abandoned after 2 attempts
- UKG — https://www.ukg.com/products/ukg-dimensions (404); enterprise HCM docs known gated (prior sibling research) — abandoned
- TCP support portal (community.tcpsoftware.com, Salesforce-based) — not fetched; TCP operational detail kept general
- Deputy individual leave/timesheet articles — category listings fetched; article-level fetch skipped (sufficient structure evidence)

Cross-reference (processed sibling leaves, read for boundary calibration): applications/employee-time-clock.md, applications/leave-absence-management.md, applications/payroll-system.md, applications/employee-scheduling-platform.md, plus their research notes.

## Product Observations

### TCP TimeClock Plus (TCP Software)

Evidence tier: A for existence of capabilities (official product pages); B for operational depth (marketing pages, support portal not fetched).

Key observations:

- Positioning: "automated time and attendance software for organizations where accuracy and compliance are non-negotiable"; vendor's own demo-configurator capability menu is exactly: Time & Attendance / Employee Scheduling / Absence Management / Labor & Demand Planning — the market splits the domain into these named capabilities.
- Pay-rule administration as the product's depth claim: "From multiple pay rates and overtime rules to union rules and multiple locations"; "Match payroll rules to internal policies, unions, CBAs, and local, state, and federal laws."
- Compliance alerting on time data: "Set alerts for missed breaks, CA meal rules, rest periods, leave accruals, and more."
- Attendance exceptions as named classes: "Catch exceptions, like missed punches, long shifts, tardies, and absences" — tardy and absence are system-recognized states, not just punch gaps.
- Leave & accruals inside the same product: "PTO. FMLA. Holiday and sick time… employees to request time off and for managers to review"; accrual tracking named in the visibility list ("hours worked, breaks, leave requests, exceptions, accruals, overtime, job codes, pay rates").
- Industry-shaped variant: K-12 resource management bundles "time clock attendance tracking, absence management, and extra duty tracking" plus substitute management — attendance + absence + assignment in one public-sector shape.
- Capture: "flexible time clocks or electronic time sheets"; hardware line ("on-site, mobile time tracking, or web clocks… 'mix and match' devices"), biometric options.
- Labor distribution: job codes, "multi-level job costing", allocation to budgets or grants.
- Reporting: "Complete payroll reporting; 30+ exceptions reports; overtime trends and forecasts; auto-send reports to stakeholders."
- Integration spine: "Secure, flexible integrations for your ERP, HCM, and payroll systems."
- Customer story frames FLSA compliance as the driver (Pasco County School District).

### Deputy

Evidence tier: A for product structure (official help-center category listings); B for article-level mechanics.

Key observations:

- Help-center areas confirm the interlocking: Timesheets, Manage leave, Scheduling, Deputy Kiosk and Time Clock, Payroll (AU/US), Deputy HR — time recording, absence, and scheduling are separate documented areas of one suite.
- Timesheets area (recording + approval machinery): filtering/reviewing, adding/editing/approving, unapproving "time and/or pay", auto-approval settings, "Comparing clocked time against approved time", "Recalculating approved timesheets", rounding settings, "Mark a timesheet as paid", timesheet attestation (Beta), export codes, CSV/Excel export.
- Worked-time ↔ leave seam is explicit: "How to convert a timesheet to a leave timesheet in Timesheet Approval" — a punch-derived record can be reclassified as leave inside the approval flow; leave and worked time live in one record system.
- Leave management area: leave policies + accrual setup (accrue "based on regular working hours", "average working hours", pro-rata for mid-year joiners, automatic recalculation when regular hours change); request and approve leave (manager awareness, approve/decline, "Enter leave on behalf of a team member"); balances (bulk import, bulk entitlements, "leave accrual and leave balance history tracking"); public holidays; employee availability/unavailability; "Block future time off requests"; maximum-people-on-leave limits; TOIL (time off in lieu) with rules attached to pay rates.
- Regional structure: leave-setup documentation is split by market (US/UK vs Australia with/without Deputy Payroll) — statutory regimes shape the policy machinery.
- Timesheet bound to "employment agreement" (error message referenced) — in AU/NZ markets the time record attaches to employment-agreement terms.
- (From sibling research, corroborated here by category structure: locked shifts in the Schedule produce timesheets; kiosk/time-clock apps record punches; Deputy Payroll AU/US consumes approved time.)

### Personio

Evidence tier: A for module structure (official help center categories); A/B for capabilities (official product page FAQ — marketing-adjacent but product-specific and detailed).

Key observations:

- Product structure: "Time Tracking" and "Absence Management" are two separate Core HR modules; the help center functional area is titled "Attendance, work schedules, and overtime" (13 articles: create work schedules, create/submit flexible work schedules, …) — attendance, schedules, and overtime form one documented functional area; absence/time off is a neighboring area ("Time off, leaves, and sick days", 19 articles; time-off approval rules in "Approvals").
- Tracking methods: digital timesheet, clock-in/out in web and mobile app, and the "Personio Entrance App" — "a shared time tracking device for deskless employees" (turn a tablet/laptop into a time-tracking device; employees clock in/out via QR code).
- Location-bound time tracking: geotracking captures location at clock in/out; geofencing checks workplace presence and "react with warnings/approvals if needed".
- Work schedules as the expectation frame: "Fixed or flexible work schedules"; flexible schedules go through a submission/approval flow — planned work shapes the record.
- Smart Compliance Check: "Stay compliant with labour laws and protect employee wellbeing"; UI example shows a required 45-minute break and "comparing original tracking with applied changes" — the system compares recorded time against break/law rules and applies/flags adjustments transparently.
- Exception-based governance: "Set workflows to trigger approvals of time entries that violate company policies"; FAQ: approvals are flexible — "run time tracking with or without approvals, and you can set up exception approval workflows… most time entries flow through automatically—while the 'edge cases' still get reviewed."
- Overtime as a balance object: time bank with "8h available balance", daily calculation option, deficit-hours handling ("Don't track" option exists) — overtime can be a tracked balance, not just a pay multiplier.
- Premiums: "Compensate employees fairly for special or off hours work with custom rules" (announced feature).
- Payroll linkage: "Reliable attendance data for Payroll"; hourly salary calculation "using recorded working hours and hourly rates"; project tracking for billing/analysis; time data "sits next to core HR data—making processes smoother and records easier to audit."
- HR oversight: FAQ — "gives HR and managers a reliable overview of attendance and overtime."

### Jibble

Evidence tier: A for product structure (help center) and A/B for category framing (official T&A product page; vendor articulates the category definition itself).

Key observations:

- The vendor's own category definition (T&A product page FAQ): "Time and attendance software help businesses track employee work hours, attendance, breaks, overtime, and leave from one platform. It replaces manual timesheets with automated records, making payroll, reporting, and compliance more accurate." — the market's unit set is exactly hours + attendance + breaks + overtime + leave → payroll/reporting/compliance.
- Workflow sections on the T&A page: Track employee time → Stop buddy punching (AI facial recognition) → Verify every clock-in location (GPS/geofencing, offline sync) → Prepare payroll faster (overtime, paid/unpaid break deductions, pay periods, exceptions, approvals, CSV/XLS export) → Keep project hours organized → Simplify leave management (custom leave policies, automated accruals and carryovers, rules assigned per team) → Turn attendance into insights → Integrations.
- Attendance as a standing picture: "real-time overview of attendance with a live dashboard that shows employee hours, attendance status, and workforce activity at a glance"; reports include "detailed attendance reports, overtime summaries, lateness reports, and employee hours by project or location."
- Help-center structure confirms the same machinery at feature level: Time Tracking Settings (custom time tracking rules, time tracking policy, reminders & automatic clock out), Work Schedule Settings (manage work schedules, overtime rates, end-of-workday timesheet splitting), Location Settings (geofences, restricting locations), Leave Management (time off calendar, multi-level approvals, leave balances export), Timesheets & Approvals, Shared Kiosks (QR kiosk, kiosk mode, app pinning/guided access), Organization Settings (time rounding, holidays), fraud-prevention onboarding checklist.
- Identity verification at the surface: AI facial recognition, selfie capture per entry, RFID/NFC, QR kiosks — explicitly framed against buddy punching.
- Audit posture: "Timestamped records for complete attendance history. Edit history records track who changed what and when" — framed as "Pass compliance inspections without a scramble."
- Scale/administration: multi-location support, role-based permissions, groups with per-group settings and assigned managers; free-forever/unlimited-users packaging pole.

## Cross-product Comparison

| Structure | TCP TimeClock Plus | Deputy | Personio | Jibble | Strength |
|---|---|---|---|---|---|
| Worked-time capture at clocking surfaces (punch/entry) | Y (clocks, e-timesheets) | Y (timesheets, kiosk) | Y (timesheet, clock-in, Entrance App) | Y (mobile/web/kiosk/Slack/Teams) | 4/4, A |
| Assembly into approved, payroll-bound hours | Y (payroll reporting, integrations) | Y (approve/unapprove/mark-paid, export) | Y (approvals flexible, hourly salary) | Y (pay-period reviews, approvals, CSV/XLS) | 4/4, A |
| Standing attendance picture (present/late/absent/on-leave; live view or exception classes) | Y (tardies/absences exceptions; OT/exception reports) | partial evidence today (timesheet/leave areas; attendance monitoring corroborated by sibling research) | Y (attendance overview for HR/managers; work-schedule adherence) | Y (live attendance dashboard, attendance status, lateness reports) | 3.5/4, A/B |
| Time away (leave) integrated in the same system | Y (leave & accrual module; leave accrual alerts) | Y (Manage leave; convert timesheet→leave timesheet) | Y (Absence Management module; time off balances) | Y (leave management; policies/accruals/carryover) | 4/4, A |
| Accrual/balance machinery | Y (accruals in visibility list; leave accrual alerts) | Y (accrual methods, balance history) | Y (time-off balances; overtime time bank) | Y (accruals, carryover, balance export) | 4/4, A |
| Time-policy configuration (OT/breaks/rounding/rules per group/location) | Y (pay rules; unions/CBAs/laws; meal-break alerts) | Y (rounding, auto-approval, TOIL rules, employment agreements) | Y (compliance check, break rules, overtime settings, workflow automations) | Y (custom rules, rounding, OT rates, auto clock-out) | 4/4, A |
| Schedule/planned-work anchoring of the time record | Y (scheduling sibling product; schedule repetition) | Y (scheduling suite; locked shifts → timesheets) | Y (fixed & flexible work schedules; submission/approval) | Y (work schedules; end-of-workday splitting) | 4/4, A/B |
| Exception machinery on time data | Y (missed punches, long shifts, tardies, absences) | Y (forgotten clock on/off; auto-approval exceptions) | Y (rule-violation workflows; warnings/approvals on geofence) | Y (missed clock-in alerts; automatic clock-out) | 4/4, A |
| Audit/defensibility posture | Y (reporting/export; compliance framing) | Y (history, recalculation of approved, unapprove) | Y ("records easier to audit") | Y (edit history; "compliance inspections" framing) | 4/4, A/B |
| Payroll destination (export/integration/built-in) | Y (ERP/HCM/payroll integrations) | Y (export codes; Deputy Payroll AU/US built-in) | Y (hourly salary; payroll modules) | Y (CSV/XLS; QuickBooks/Xero/Deel) | 4/4, A |
| Identity verification / anti-buddy-punching at surfaces | Y (hardware, biometric options) | Y (kiosk permissions; sibling research) | Y (Entrance App QR) | Y (face recognition, selfie, RFID/NFC) | 4/4, A/B |
| Job/project/cost attribution | Y (job codes, multi-level job costing) | Y (custom timesheet fields/shift questions) | Y (project tracking) | Y (projects/activities) | 4/4, A/B |
| Multi-location / group-structured administration | Y ("multiple locations") | Y (Locations area) | Y (location-bound tracking) | Y (multi-location, groups, role permissions) | 4/4, A/B |
| Attestation on time records | — | Y (Beta) | — | — | 1/4, product-specific |
| Region-specific statutory depth in-product | Y (CA meal rules, FLSA framing) | Y (AU employment agreements, market-split docs) | Y (labour-law compliance check; flexible-schedule submission) | Y (labor-laws resource hub) | 4/4 as capability; specifics regional |
| Pay computation inside the product | payroll-calculation claims (loosely worded) | Y (Deputy Payroll as separate product) | Y (hourly salary calc; separate payroll modules) | — (exports only) | mixed; treated as adjacent/bundled |

Reading of the comparison:

- The punch→timesheet→approval→payroll spine (the Employee Time Clock's whole world) appears in all four products but as one layer, never the whole product: every product also carries the attendance picture and the policy/absence machinery as first-class documented areas.
- The attendance picture (who is present/late/absent/on leave, surfaced live or as named exception classes and reports) is evidenced directly in three products and structurally in the fourth.
- Leave integration is universal in the sample: in every product, time away is administered inside (or immediately beside) the time system, and the worked-time↔leave seam is product-visible (Deputy's timesheet→leave conversion; TCP's leave accruals inside time data).
- Policy configuration (overtime, breaks, rounding, accrual policies) exists in all four as managed configuration — not ad-hoc settings — and is framed against internal policy/union/CBA/law compliance in the compliance-first pole and against labour-law/statutory compliance in the European pole.
- Schedule anchoring is universal in sample (all four products tie the time record to planned work in some form), but its depth varies (scheduling-suite pole vs schedule-as-configuration pole); held as common mature structure, not the invariant — a T&A system can judge attendance against expected hours without owning shift planning.

## Canonical Model

### L0 — Defining Invariant

The Time & Attendance System is the organization's system of record for workforce time, and its defining core is exactly three jointly-held structures:

1. **The worked-time record of record** — per-employee worked time captured at clocking surfaces or entered, assembled into hours for defined periods, and moved under organizational approval to a payroll/compliance destination. (The time-clock layer, inherited: remove → no workforce time system at all.)
2. **The standing attendance state of the workforce** — worked time and time away maintained together as an ongoing organizational picture in which each employee's state is distinguishable as working / late / absent / on approved leave, monitored and acted on as a management discipline (live views, named exception classes, attendance reporting). (Remove → a punch-clock timesheet layer = Employee Time Clock.)
3. **Time-policy administration** — the organization's time rules (overtime, breaks, rounding; absence kinds with accrual/balance semantics) held as governed configuration applied to the record to classify, flag, and make hours payroll- and compliance-ready, with the record kept defensible (approval states, audit trail). (Remove → a manual attendance register/spreadsheet; the "management" disappears.)

Jointly-held is load-bearing: 1 alone = Employee Time Clock; 1+2 without 3 = an attendance register; 1+3 without 2 = a rules-bearing timesheet engine (the honest market edge where "time & attendance"-branded clocks sit); 2+3 without 1 = Leave & Absence Management with no worked-time capture.

### L1 — Common Mature Structure

- Clocking-surface variety: shared kiosk/terminal, personal mobile/web/desktop, hardware badge/biometric terminals, offline capture with later sync
- Identity verification at surfaces (PIN/QR/badge/face/selfie) framed against buddy punching
- Schedule anchoring: punches/entries judged against planned shifts or expected hours; late/absent detection; end-of-workday splitting
- Exception machinery: missed punch, late arrival, long shift, absence; alerts, reminders, automatic clock-out
- Approval workflow with period closure; unapprove/reopen; recalculation of rule-derived values on reopen; clocked-vs-approved comparison
- Rounding and break handling (paid/unpaid, deductions, attestation in some products)
- Overtime machinery: thresholds, rates, time banks/balances, trend reporting
- Leave/absence policy machinery: policies, accrual methods, carryover, balances, public holidays
- Live attendance dashboards and attendance/lateness/overtime reports
- Audit trail / edit history (who changed what and when)
- Payroll handoff: export files/formats, integrations, or built-in payroll
- Multi-location/multi-group administration with role-based permissions
- Job/project/cost attribution of hours

### L2 — Variant / Optional Structure

- Hardware badge/biometric terminal estates vs software-only capture
- Compliance-regime depth as market shape: US (FLSA, state meal/rest rules, CBAs/unions) vs European statutory working-time recording vs AU/NZ employment-agreement-bound timesheets
- Approval posture: mandatory approvals vs exception-only approvals vs no approvals
- Attestation at approval time (single product in sample)
- Built-in payroll vs export/integration boundary
- Scheduling bundled (suite pole) vs scheduling as a sibling product
- Productivity/monitoring extensions (screenshots, activity tracking, live location) at the tracker pole
- Industry-shaped variants (K-12 substitute/extra-duty management; public-safety rotation patterns)
- Packaging: free-forever/unlimited users vs enterprise contracts

### L3 — Vendor-specific (kept out of the final document)

- TCP: K-12 "resource management" (substitute search/request, extra duty tracking); "30+ exceptions reports"; value calculator; CA-meal-rule alert naming
- Deputy: TOIL rules attached to pay rates; "mark a timesheet as paid"; employment-agreement binding error; market-split leave documentation (AU without Deputy Payroll vs US/UK)
- Personio: Entrance App (QR shared-device clocking); deficit-hours handling option; premiums (announced); flexible-work-schedule submission flow
- Jibble: Slack/Teams clocking; MCP/AI-assistant integrations; live location tracker; guided-access/app-pinning kiosk lockdown

## Boundary Findings

- **vs Employee Time Clock (processed sibling)**: nested, not competing — the market boundary is a gradient. The time clock's whole world is punches→timesheet→approval→payroll handoff; the T&A system additionally holds the attendance state and time-policy administration as primary objects. Market evidence: products at the clock pole brand themselves "time & attendance" (Jibble's T&A page describes essentially a clock-plus-attendance product), while system-level products (TCP, Deputy, Personio) document attendance/absence/policy as separate functional areas. Test: if the product's documented world is punches and timesheets, it is the clock; if attendance state, absence/accrual management, and policy administration are primary documented objects, it is the system. The directory keeps both leaves; the clock is the recording layer the system contains.
- **vs Employee Scheduling Platform (processed sibling)**: plan vs actual. Scheduling owns future work; T&A records and judges actual work against that plan ("the locked-shift handoff marks the boundary" per the scheduling document). Scheduling-led suites bundle T&A; T&A products anchor on schedules without owning shift planning. Expected-hours-based organizations satisfy T&A without scheduling ownership — anchoring, not scheduling, is in the core.
- **vs Leave & Absence Management (processed sibling)**: leave governs planned and approved absence (types, entitlements, balances, decisions) and "does not record actual worked time (Time & Attendance)" per its document. In T&A, absence appears as part of the attendance state (on-leave vs absent) and worked-time↔leave reclassification is possible (Deputy); deep accrual-policy machinery is either embedded (common in the sample) or delegated to the leave sibling. Remove worked-time capture from T&A → leave/absence management.
- **vs Payroll System (processed sibling)**: T&A is the upstream input provider ("payroll consumes that data to compute and issue pay"). The T&A core stops at payroll-ready approved hours; wage/tax computation and pay runs belong to payroll. Boundary softens where vendors bundle (Deputy Payroll; Personio hourly-salary calc; TCP's loosely-worded "payroll calculations" claims) — held as adjacent/bundled capability, not core.
- **vs Workforce Management Platform (unprocessed sibling)**: per the scheduling document, WFM = scheduling + T&A + forecasting + engagement + analytics as one platform; T&A is one major module. The leaf's future pass should confirm; from this side, T&A-licensed standalone products (TCP TimeClock Plus, Jibble) exist without forecasting/engagement.
- **vs Time Tracking Application**: self-logged, task/project-attributed time for billing and productivity analysis vs organization-authorized attendance time for payroll/compliance. The tracker pole (Jibble) carries both faces; the unit of truth distinguishes them.
- **vs Workforce Management for Contact Centers / Agent Scheduling Platform**: derives staffing from queue forecasts/service levels at fine interval granularity — a different demand model from T&A's worked-time record.
- **vs Shop-floor/production time capture (MES/Shop Floor Management)**: production systems capture time against jobs/operations for output accounting; T&A's subject is the person's attendance and worked time for pay/compliance. Job costing exists in T&A as attribution of hours, not production accounting.
- **"去掉什么就变成另一个 Type" 判据**: remove worked-time capture → Leave & Absence Management; remove attendance-state and policy primacy → Employee Time Clock; add wage computation/pay run as primary → Payroll System; add ownership of future shift planning → Employee Scheduling; add forecasting/engagement/analytics umbrella → Workforce Management Platform; make time self-logged and task-attributed → Time Tracking Application.

## Historical / Market-Sample Check

- Paper-era factory timekeeping satisfies the core: punch clock + timekeeper's ledger (worked-time record of record), a daily attendance register distinguishing present/late/absent plus a vacation ledger (attendance state with time away), and the factory rulebook (overtime authorization, break requirements) applied by the timekeeper under supervisor sign-off (policy administration, audit by signature). No cloud, biometrics, or scheduling software involved.
- Regional check: European statutory working-time recording (Personio's home market, where time records are an employer legal obligation) satisfies via the same three legs — the statutory driver changes the compliance depth, not the core. AU/NZ employment-agreement-bound timesheets satisfy likewise.
- Platform-native/embedded variants: POS-embedded time clocks and HRIS-embedded attendance modules satisfy as embedding postures of the same core.
- The modern implementation layer (biometrics, GPS/geofencing, AI face recognition, live dashboards, time banks, exception-approval workflows) is era-current capability, none of it definitional.

## Uncertainties

- Enterprise HCM time & attendance (UKG/Kronos, ADP, Workday, Paycom) not directly reachable; enterprise-tier mechanics (hardware estates, union/CBA rule engines at scale) asserted only in general terms, consistent with the sibling Employee Time Clock research limitation.
- Rippling help center unreachable (SPA); Rippling dropped from the sample rather than filled from memory.
- TCP evidence is product-page level (Tier 2); its support community portal was not fetched, so TCP operational detail (e.g., exact rule configuration) is kept general.
- Deputy's attendance-monitoring depth (live views, attendance reports) is corroborated structurally today (category structure) and from sibling research, not from a fetched attendance-specific article — attendance leg rests mainly on TCP/Personio/Jibble.
- Personio compliance-check mechanics come from its product page/FAQ (official but marketing-adjacent); precise behavior kept general.
- Exact statutory references (e.g., specific national working-time statutes) were not verified on fetched pages and are not asserted anywhere.
- Single-product findings kept product-specific: attestation (Deputy, Beta), TOIL-with-pay-rates (Deputy), Entrance App QR clocking (Personio), deficit-hours handling (Personio), Slack/Teams clocking (Jibble), K-12 substitute management (TCP).
- TCP's "automate complex payroll calculations" wording is ambiguous between rule-derived hours/premiums and pay computation; treated conservatively as payroll-readiness, not a pay run.

## Final Synthesis

The Time & Attendance System is the organization-side system of record for workforce time: it captures worked time at clocking surfaces and assembles it into approved hours (the layer the Employee Time Clock exposes as its whole world), maintains the standing attendance state of the workforce by holding worked time and time away together (working / late / absent / on-leave distinguishable, monitored live and through named exception classes), and administers the organization's time policies — overtime, breaks, rounding, absence kinds with accrual/balance semantics — as governed configuration applied to the record, kept defensible through approval states and audit trails, and handed to payroll as payroll-ready hours. Attendance and absence administration and policy administration are what make it a system rather than a clock; capture without them is the sibling clock Type; capture-free absence administration is the leave sibling; wage computation is payroll's territory. The market implements the core across a gradient of poles — compliance-first pure-plays, scheduling-led suites, HR-suite modules under statutory drivers, and freemium attendance trackers — all recognizable as one Type by the three jointly-held structures.
