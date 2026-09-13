# Research Notes — Time Tracking Application

Research date: 2026-09-09
Slug: time-tracking-application (DIRECTORY §03.14 Time & Focus)

## Research Goal

Understand the Time Tracking Application as an Application Type from real products: what the unit of record is, how time is captured and attributed, what the timesheet/report/billing machinery looks like, which roles act on the record, and where the boundaries run against the already-processed §03.14 siblings (Productivity Activity Tracker, Focus Timer, Time Blocking Application) and the §09 workforce-time Types (Employee Time Clock, Time & Attendance System), plus PSA and Invoicing.

## Initial Boundary

Working hypothesis at start: a Time Tracking Application records how much time was spent on what — attributed to projects/tasks/clients — for reporting, billing, and productivity analysis. Nearest confusions:

- Productivity Activity Tracker (2026-09-08): ambient capture + productivity interpretation; forward flag says test the who-starts-the-clock + record-purpose seam and expect bundling-not-identity (RescueTime sells Focus and Timesheets as two named tools on one app).
- Focus Timer (2026-09-07): deliberate bounded sessions for motivation vs continuous record for reporting/billing.
- Time Blocking Application (2026-09-09): plan-future vs record-past.
- Employee Time Clock / Time & Attendance (2026-09-06/08): organization-authorized attendance time for payroll vs self-logged task time for billing/analysis; unit of truth distinguishes.
- PSA (processed): time tracking captures hours; PSA binds hours to billable projects, resolves rates, gates approval, converts to invoices — time tracking is a component of PSA, not the Type.
- Task Mining: declared/timer-based vs derived-from-observation.
- Engineering Productivity Analytics: self-declared/active time vs tool-derived process signals.

## Research Questions

1. What is a time entry? What fields does it carry (duration, attribution target, description, billable flag, date, user)?
2. How is time captured — running timer, manual entry, timesheet grid, calendar, automatic capture? Which modes are first-class?
3. What is the attribution structure (client → project → task)? How deep, and how strictly required?
4. Where do billable/non-billable and rates appear? Are they definitional or common?
5. What is the timesheet (period view) and its lifecycle (submit/approve/lock)?
6. What reports exist and what dimensions do they break down?
7. What integrations matter (PM tools, invoicing, accounting, calendars)?
8. Who uses it (freelancer, agency, team, individual) and what roles exist?
9. Where exactly do the seams run vs PAT (automatic capture), T&A (attendance), focus timer, time blocking, PSA?
10. Historical check: does the paper timesheet lineage satisfy the definition?

## Representative Products

| Product | Why selected | Positioning observed |
|---|---|---|
| Toggl Track | Independent timer-first market benchmark; freelancer→enterprise span; new 2.0 KB rich | "The time tracker millions trust… time data for better capacity, profitability, and project planning" |
| Harvest | Timer + timesheet + invoicing lineage; professional-services philosophy; excellent Tier-1 help center | "Turn hours into profit… track time, bill clients, optimize team time" |
| Clockify | Freemium timesheet-first team pole; bundles kiosk/auto-tracker/activity monitoring — the market-blur pole | "Time and cost tracking… time tracker and timesheet software for teams" |
| RescueTime | Vendor-drawn seam: one app, two named tools (Focus = PAT; Timesheets = Time Tracking); automatic-capture pole | "Two tools with one powerful app… Focus… and Timesheets, to automate tracking time by client, project, or task" |

Timely (timely.app) was attempted as the AI-automatic pole: root fetch returned no content and memory.ai returned 404 — dropped after two attempts per the network-limitation rule. The automatic-capture pole is instead evidenced by Clockify Auto tracker (Tier 1) and RescueTime Timesheets (Tier 2).

## Sources

Tier 1 (official operational documentation):

- Toggl 2.0 Knowledge Base — https://docs.toggl.com/ (root), https://docs.toggl.com/features, https://docs.toggl.com/using-the-timesheet-view, https://docs.toggl.com/timesheet-approvals-in-toggl-2.0
- Harvest Help Center — https://support.getharvest.com/hc/en-us (root), Quick start guide, Understanding the three project types, Submitting and approving timesheets
- Clockify Help Center — https://clockify.me/help/ (root), https://clockify.me/help/track-time-and-expenses, https://clockify.me/help/track-time-and-expenses/creating-a-time-entry, https://clockify.me/help/track-time-and-expenses/auto-tracker

Tier 2 (official product pages):

- Toggl Track — https://toggl.com/track/
- Harvest — https://www.getharvest.com/
- Clockify — https://clockify.me/ (via help-center footer product framing)
- RescueTime — https://www.rescuetime.com/

Source-access limitations:

- Timely (timely.app / memory.ai) unreachable this pass (empty response; 404) — dropped from sample; automatic-capture pole covered by Clockify Auto tracker + RescueTime Timesheets instead.
- RescueTime evidence is product-page level (Tier 2); its help center was not fetched. Claims about RescueTime kept at positioning level.
- Toggl is mid-transition to "Toggl 2.0" (focus.toggl.com); KB terminology uses "Time Log"/"time entry" interchangeably. Legacy Track help center not separately fetched.

## Product Observations

### Toggl Track (Tier 2 product page + Tier 1 2.0 KB)

Key observations (evidence layer A unless noted):

- Positioning: "Toggl gives teams the time data they need for better capacity, profitability, and project planning." Features nav: Automated time tracking, Online work timer, Timesheet reports, Integrations, Invoicing, Time off management, Time reporting and analytics.
- Use cases: Employee time tracking, Time billing, Project time tracking, Payroll. Industries: consultants, agencies, design, finance, lawyers, software.
- Trust boundary vs employee monitoring, vendor-stated: "Maintain employee trust with a tool that never monitors screens, keystrokes, or webcams" (also "No screenshots, no keystroke logging, just accurate, respectful records" for law firms).
- Billable machinery: "Set custom hourly rates, track billable hours, and generate detailed invoices directly from your team's time entries"; law firms: "Billable rates with 6-minute increments."
- Reports: "Filter, group, and break down time data exactly how you need it — by project, client, team, or any dimension."
- Automated time tracking framing: "Track time in the background or with a single click — so your team never has to rely on memory."
- 2.0 KB features list: Timesheet Approvals, Billable Rates, Rounding, Time Tracking Reminders and Project Alerts, Required Fields for Tasks and Time Logs, custom fields (project/task/member level), Labor cost, Project Fixed Fees, Recurring Projects, Time Off Pro, Audit Log, Utilization and Workload Reports, Profitability Reports, Time Logs Report, Summary Report, Forecasting in reports.
- Timesheet view (A): "structured, grid-style way to log and review your time across the week… tasks laid out in rows with day columns." Group by Task / Project / Client / Client & Project. Duration typed as `1 h`, `0.5`, `60 m`, `90 m`. **"Taskless entries: You can log time against a project without assigning a task"** — project required, task optional in this surface. Billable status per entry. Copy from previous week (prefill rows vs copy rows+hours). Submitted/approved timesheets read-only.
- Timesheet Approvals (A): "adds a formal submit-and-review workflow… Once submitted or approved, the period locks to keep billing, payroll, and reporting numbers stable." Premium plan, webapp only. Use cases: bill clients by the hour (approval catches missing/misattributed time before invoice), time data feeds payroll, compliance/client audits, people forget to log time. **"If you're mainly using Toggl for personal time awareness and nobody downstream depends on the data being locked down, you probably don't need this."** Roles: Admins (setups), Approvers (review/approve/request changes/decline/withdraw), Members (submit). Weekly cadence (monthly "coming soon"). Locking: members cannot edit submitted/approved periods; admins can with warning.

### Harvest (Tier 2 product page + Tier 1 help center)

Key observations (A):

- Positioning: "Turn hours into profit. Harvest helps professional teams track time, bill clients, optimize team time, and measure performance." Workflow: Track → Review → Bill → Organize → Manage.
- **Core attribution chain, vendor-stated: "In Harvest, all time is tracked to a task that's assigned to a project for a client."** Organize section: "Your clients, projects, and tasks — all structured and connected. Set up your work hierarchy so every hour your team tracks has a clear home and purpose." Clients → Projects → Tasks → Tags.
- Capture: "One-click timers, weekly and daily timesheets, or track directly from your connected calendar — on desktop, mobile, or browser." Quick start: Day view "+ Track time" → "either start a timer or enter your time after the fact"; Week view "best for adding a lot of time at once."
- Account preferences: **Timer mode** — Duration (e.g. 5 hours) vs Start and end times (9:00am–2:00pm); **Time display** — decimal (2.25) vs HH:MM (2:15).
- Three project types (A): **Time & Materials** (bill by the hour at billable rates; rate basis: project rate / person rate / task rate), **Fixed Fee** (set price regardless of hours; project fees; milestone or recurring monthly billing), **Non-Billable** (track time, no invoices — internal projects). Budgets: hourly (total project hours / per person / per task) or fee-based (total fees / fees per task); optional monthly reset. Retainers draw down.
- Team: permission levels (Members / Some Managers / All Managers / Administrators), capacity, roles, default billable rates and cost rates per person, project assignment.
- Timesheet approval (A): "allows Administrators and Managers to review, approve, and lock your team's weekly submitted time and expense entries." **"Timesheet approval is an optional module in your account."** Submit daily/weekly/custom range; time and expenses always submitted together. "After submission, timesheets can still be edited until they're approved." "Approving a timesheet locks the entries for the entire week" (including days with no time). "Timesheets cannot be rejected" — request changes via email or edit directly (differs from Toggl's request-changes state). Withdraw approval (admins only). Auto-submit / auto-lock on schedule (recurring lock modes). Reminders: recurring weekly, manual one-time, personal daily.
- Reports: Time report, Detailed time/expense, Uninvoiced report, Project profitability, Team utilization, custom exports to accounting tools.
- Invoicing: "Build invoices from tracked time and expenses"; online payments; retainer billing.
- Integrations: 40+ (PM tools, accounting, payments); Harvest Forecast is a separate scheduling product.

### Clockify (Tier 1 help center)

Key observations (A):

- Positioning: "Time and cost tracking"; "The world's leading time tracker and timesheet software for teams." Part of CAKE.com suite (with Plaky PM, Pumble chat).
- Help-center categories: Getting started / Administration / **Track time & expenses** / Reports / Projects / **Activity Monitoring** / Integrations / Apps.
- Track time (A): four first-class capture modes — **Time Tracker** (timer: description "What are you working on?", "Select a Project to associate the time with (optional)", Start/Stop), **Manual mode** (start+end times or just duration), **Timesheet** (week grid; "Task/@Project link (required when Timesheet is enabled)"), **Calendar view** (click a time slot, drag/resize blocks). Continue an existing entry (resume with same description/project/tags — creates a new entry). Change start time of running timer. Keyboard shortcuts (n/m/c/s, favorites 1–5).
- Time-entry machinery: custom fields, split entry, favorite entries, duration format (decimal/hh:mm), GPS tracking, **Pomodoro, idle detection, reminders**, edit entries, **add time for others**, required fields, **time rounding**, **time audit**, **billing tracked time (billable)**, time categorization & tags.
- Timesheets: **Lock timesheets**. Approvals: submit time & expenses for approval, manage member's time, approve time & expenses. Time off: balance, request, policy, accrual, approve, non-working days. Kiosk: shared clock-in surface with PIN authentication, breaks on kiosk, clock in/out via kiosk (T&A-shaped surface inside a time tracker).
- **Auto tracker (A) — the seam evidence**: "lets you automatically monitor programs that are active while you're tracking time. This feature helps you generate accurate timesheets." Records programs/window titles/URLs/idle percentage. **"Recorded activities only appear in the auto tracker window and aren't automatically added to your timesheet. You must manually convert them into time entries"** (+ project + description). Privacy: data stored locally, only the user sees it, auto-deleted after 45 days; "If a regular user didn't add activities as time entries, admins won't be able to see them."
- Activity Monitoring (separate help category): "Smart productivity tracking, utilization reports, and custom activity controls" — PAT/employee-monitoring-shaped capability bundled alongside.
- Features roll: Timer, Timesheet, Kiosk, Calendar, Auto tracker, Rates, Projects, Activity, Location, Scheduling, Time off, Approval, Team, Expenses, Invoicing. Use cases: Timekeeping, Planning, Attendance, Reporting, Budgeting, Payroll.

### RescueTime (Tier 2 product page)

Key observations (A at positioning level; B for mechanics):

- Vendor-drawn two-tool framing: "RescueTime delivers two tools with one powerful app: RescueTime **Focus**, to improve concentration and automatically track time spent on apps and websites, and RescueTime **Timesheets**, to automate tracking time by client, project, or task."
- Focus = the Productivity Activity Tracker face (automatic activity tracking, goals & alerts, focus sessions, blocking, productivity reports).
- Timesheets = the Time Tracking face: "automatically logs your time by project, client, and task, generating accurate timesheets without manual entry"; "No timers, spreadsheets, or guesswork required." Solo features: Timeline, **Smart Fill Hints**, **Suggestion Review**, Flexible Reporting. Team features: Shared Clients/Projects/Tasks, Role-based Access Control, Team Weekly Calendar View, **Billable Rates**. "Filter reports to create invoices for clients."
- Privacy FAQ: "We collect data about which apps and websites you use to generate your reports… We do not collect keystrokes, form input, screenshots, or webpage content."
- The two tools share one app and one automatic-capture substrate; the seam between them is drawn by the vendor itself — Focus serves productivity interpretation, Timesheets serves project/client/task attribution with billable rates and client reports.

## Cross-product Comparison

| Dimension | Toggl Track | Harvest | Clockify | RescueTime (Timesheets face) |
|---|---|---|---|---|
| Unit of record | time entry / "Time Log" | time entry (task+project+client) | time entry | auto-attributed project/client/task time |
| Attribution chain | project required, task optional (timesheet surface); client grouping | client → project → task, all required | project optional in tracker; required in timesheet surface | project/client/task via automatic suggestion |
| Capture modes | timer, manual, timesheet grid, calendar, background/automated | timer, manual (duration or start/end), timesheet day/week, calendar | timer, manual, timesheet grid, calendar, kiosk, auto tracker | automatic capture + suggestion review |
| Billable/rates | billable per entry; billable rates; 6-min increments (law) | billable per project type; rates by project/person/task; cost rates | billable flag; rates feature | billable rates for invoicing |
| Timesheet lifecycle | submit → approve/request changes/decline; period locks | submit → approve (lock whole week); withdraw; auto-lock | submit → approve; lock timesheets | (not observed at this level) |
| Approval optional? | yes — Premium feature; "personal time awareness… you probably don't need this" | yes — "optional module" | yes — feature-gated | n/a |
| Reports | summary, time logs, profitability, utilization, forecasting | time, detailed, uninvoiced, profitability, utilization | reports suite with rates | client reports, flexible reporting |
| Downstream money | built-in invoicing | built-in invoicing + payments | built-in invoicing | "filter reports to create invoices" |
| Bundled neighbors | capacity planning, time off, AI reports | expenses, Forecast (separate scheduling product) | kiosk, activity monitoring, scheduling, time off, GPS, Pomodoro | Focus (PAT) on same app |
| Anti-monitoring stance | explicit ("never monitors screens, keystrokes, or webcams") | not stated on fetched pages | activity monitoring offered as separate category | explicit ("no keystrokes, screenshots") |

Cross-product commonalities (B layer):

1. Every sampled product centers on a persistent, individually addressable **time entry** carrying duration + attribution + description + date + (usually) billable flag + user.
2. Every sampled product attributes time to a **work structure** (client/project/task hierarchy); strictness varies (Harvest full chain; Toggl project-required/task-optional; Clockify project-optional in tracker mode) — the *existence* of a user-chosen attribution target is constant, its depth/enforcement is variant.
3. Every sampled product offers **multiple capture modes** with timer and manual entry both first-class; the timesheet grid and calendar are common secondary surfaces.
4. Automatic capture appears only as a **capture aid** whose output must pass user confirmation before becoming entries (Clockify: "you must manually convert them"; RescueTime: "Suggestion Review") — or is marketed as suggestion-driven ("Smart Fill Hints"). No sampled product turns ambient capture directly into authoritative billable entries without a user confirmation step.
5. **Reports** over the entry population (by project/client/team/person, filterable, exportable) are universal.
6. **Billable semantics** (billable flag + rates) appear in all sampled products; depth varies.
7. **Timesheet approval + locking** appears in the team/organization tier of all three Tier-1 products, always as an optional/gated module, always ending in a locked period that protects downstream billing/payroll/reporting numbers.
8. **Invoicing** appears as built-in or tightly-coupled downstream in all sampled products.
9. Reminders to track/submit are universal furniture.
10. All sampled products either reject or fence off employee-monitoring depth (screenshots/keystrokes) — Toggl and RescueTime state it explicitly; Clockify splits "Activity Monitoring" into its own category.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (three jointly-held structures)

1. **The time entry as the unit of record** — a persistent, individually addressable record of a duration of time, carrying its date, its recorder, and (typically) a description. Remove → a stopwatch/timer utility with no memory, or a live meter.
2. **Attribution of time to a work structure** — each entry is attributed by the user to a work-structure target (project, task, client, matter, job — a user-maintained hierarchy whose depth and enforcement vary). This is what the record is *about*: work performed, not applications used (PAT) and not attendance kept (T&A). Remove → an unattributed duration log; the Type's center collapses and the record becomes indistinguishable from usage telemetry.
3. **User-driven formation of the record** — the entry comes into being through a user act: starting/stopping a timer, typing a duration or start/end times, filling a timesheet cell, or confirming an automatically captured suggestion. Remove → ambient automatic attribution = Productivity Activity Tracker.

Jointly-held is load-bearing:

- 1 alone = a stopwatch log (no attribution, no work semantics).
- 2 without 1+3 = a work breakdown structure with no time record (project management).
- 3 without 2 = usage telemetry (PAT) or attendance punches (T&A).
- 1+2 without 3 = ambient auto-attributed timesheets — the RescueTime-Timesheets pole, held as a straddle (see Boundary Findings), not as L0 evidence.
- 1+3 without 2 = a personal duration diary — edge case; the market's center of gravity always attributes.

### L1 — Common Mature Structure

- Timesheet period views (day/week grid) over the entry population.
- Reports/analytics: filter/group/break down by project, client, task, team member; detailed and summary forms; export (CSV/Excel, accounting tools).
- Billable flag on entries + billable rates (at project/person/task grain) + cost rates; rounding rules.
- Project budgets and estimates vs actuals; project profitability/utilization reporting.
- Reminders (to track, to submit); idle detection; favorite/recent entries; copy last week; continue/resume timer.
- Multi-surface clients: web, desktop (with timer + capture aids), mobile, browser extension; cross-device sync.
- Team/workspace layer: members, roles/permissions, per-person rates, assignment to projects.
- Integrations: embed timers in PM/issue tools (browser extensions), export to invoicing/accounting, calendar connections.
- Expenses alongside time (common in the billing-oriented segment).

### L2 — Variant / Optional Structure

- **Timesheet approval + locking** — optional module (Harvest: "optional module"; Toggl: Premium plan), organization-tier only; lifecycle submit → review → approve/request-changes/decline → locked period; auto-lock/auto-submit schedules; withdrawal by admins.
- **Automatic capture** (auto tracker / memory / suggestions) — capture-aid philosophy; local-storage privacy postures; confirmation step before entries form.
- **Kiosk clocking surface** (Clockify) — shared-device clock-in with PIN; drifts toward Employee Time Clock.
- **Time off / breaks / holidays** inside the tracker (Clockify time-off policies; Toggl Time Off Pro; Harvest PTO in Forecast) — drifts toward T&A/Leave.
- **GPS/location** (Clockify) — field-work variant.
- **Built-in invoicing depth** (Harvest: invoices, payments, retainers; Toggl: invoicing from entries; Clockify: invoicing feature) — depth is a variant axis; the PSA seam.
- **Scheduling/capacity planning** (Toggl capacity planning; Harvest Forecast as separate product) — plan-side neighbor bundled or split.
- **Pomodoro timer mode** (Clockify) — focus-timer neighbor bundled.
- **Activity monitoring** (Clockify, separate category) — PAT/employee-monitoring neighbor bundled.
- Rounding rules, required fields, custom fields, audit log, SSO — governance furniture, depth varies by tier.

### L3 — Vendor-specific (research notes only)

- Toggl 2.0: timesheet rows default new entries to 8:00 AM; unsaved rows shown pink; group-by preference saved per workspace; "Time Log" terminology; weekly-only approval cadence (monthly "coming soon"); single approver per setup; 6-minute increment billing marketed for law firms.
- Harvest: three project types named Time & Materials / Fixed Fee / Non-Billable; "Timesheets cannot be rejected" (request-changes via email or direct edit instead); time and expenses always submitted/approved together; Harvest Forecast shipped as a separate product; auto-lock modes (deadline / previous week/month / older-than-N-days).
- Clockify: auto-tracker thresholds (10 s minimum, 60 s default, 10 s switching tolerance), 45-day local auto-deletion, kiosk PIN authentication, CAKE.com suite packaging.
- RescueTime: two-tools-one-app packaging (Focus + Timesheets); "Smart Fill Hints"/"Suggestion Review" naming.

## Vendor-specific Findings

See L3. Additionally: Toggl's anti-monitoring stance ("never monitors screens, keystrokes, or webcams") is vendor positioning but evidences the Type's structural fence against employee monitoring; Clockify's Activity Monitoring category shows the same fence drawn as a separate module rather than a stance.

## Boundary Findings

1. **vs Productivity Activity Tracker** (forward flag DISCHARGED, ratified from this side). Seam = who forms the record + what the record is about. PAT: ambient automatic capture of app/website usage, interpreted through a productivity frame; nothing for the user to start or stop. Time Tracking: user-driven entries attributed to work structures for reporting/billing. Market blurs deliberately and the blur is *bundling, not identity*: RescueTime ships Focus (PAT) and Timesheets (Time Tracking) as two named tools on one app — the vendor itself draws the seam; Clockify's Auto tracker captures ambient activity but "you must manually convert them into time entries" — the entry's user-driven formation survives; Clockify's Activity Monitoring sits in its own help category beside the tracking core. Test: remove user-driven formation (records form without the user's hand) → PAT; remove the work-structure attribution center → PAT remains.
2. **vs Employee Time Clock / Time & Attendance System** (§09, both processed). Seam = unit of truth. Time tracking: self-logged task/project-attributed durations for billing/analysis; the time clock: identified employee's in/out punches assembled into approved payable hours; T&A: adds attendance state and time-policy administration. Clockify's kiosk is a T&A-shaped surface inside a time tracker — bundling, not identity. Test: make the record attendance hours for payroll, organization-authorized → time clock/T&A; make it task-attributed and self-driven → this Type.
3. **vs Focus Timer** (processed). Seam = bounded motivational session vs continuous attributable record. Focus timer's records are a byproduct motivational surface, not a billing-grade ledger. Clockify bundles a Pomodoro mode — capability, not the Type. Test: remove attribution/reporting center, add session bounding + motivation framing → focus timer.
4. **vs Time Blocking Application** (processed). Seam = record-past vs plan-future. Time-blocking products bundle time-tracking stats as furniture (Sunsama actual time, Reclaim Time Tracking, Akiflow Stats). Test: remove the forward plan → tracker.
5. **vs PSA** (processed). Seam = hours capture vs the resource-billing loop. PSA binds hours to billable projects, resolves rate cards, gates approval, converts to invoices, and measures utilization/margin per project; time tracking is the hours-capture component. Test: make rate resolution + invoice generation + resource economics the center → PSA.
6. **vs Invoicing Application** (processed). Invoicing turns billed items into documents and payments; time tracking produces the hours that feed it. Built-in invoicing in time trackers is a downstream convenience; remove invoicing and the tracker stands; remove entries and the invoicing tool stands.
7. **vs Task Mining / Engineering Productivity Analytics** (both processed). Declared/user-entered time vs derived-from-observation process signals. Test: derive the task structure from system observation → task mining/EPA.
8. **vs employee monitoring (no directory leaf)**. Adding screenshots/keystroke/content capture to serve organizational oversight crosses out of this Type; Toggl and RescueTime explicitly fence it off; the taxonomy gap is already flagged by the productivity-activity-tracker pass — no change from this side.
9. **"去掉什么就变成另一个 Type" 判据**: remove user-driven formation → PAT; remove work-structure attribution → PAT or a bare stopwatch log; re-point the record at attendance/payroll → time clock/T&A; re-point the record at the future → time blocking; bound the record into motivational sessions → focus timer; add rate-card/invoice/resource economics as the center → PSA.

## Historical / Market-Sample Check (§24)

Passed. The paper timesheet lineage — a professional (lawyer, consultant, contractor) hand-writing durations against matters/clients/jobs in a notebook or paper sheet, totaling them per period, and handing them to billing — satisfies all three L0 structures with no software, no timer, no cloud, no rates engine: the entry is the written line, attribution is the matter/client heading, formation is the hand that writes it. The mechanical punch clock belongs to the *other* lineage (attendance → T&A/time clock), confirming the attribution seam is old, not new. The definition names no timer, no cloud, no billable rates, no approvals, no AI — the paper pole proves none of them definitional. Modern automatic-capture products (RescueTime Timesheets) satisfy the core only through their user-confirmation layer (Suggestion Review); their fully-automatic marketing pole is held as a straddle, not as the definition.

## Uncertainties

- **Attribution strictness at the edges**: Clockify's tracker mode makes project optional ("Select a Project… (optional)"); whether any mainstream product ships a durable entry with *no* attribution target at all (pure duration diary) was not confirmed. Held: attribution target existence is L0, per-entry enforcement is variant.
- **Automatic-capture pole depth**: Timely (memory.ai) unreachable; the strongest automatic products (Timely, Memory) may form entries with lighter confirmation than Clockify's explicit convert step. RescueTime's "without manual entry" marketing vs its "Suggestion Review" feature leaves the confirmation depth ambiguous at Tier 2. The L0 wording ("user-driven formation… or confirming an automatically captured suggestion") is calibrated to the observable evidence; a future pass with Timely access should re-test.
- **Approval universality**: approval/locking observed in all three Tier-1 products but always plan-gated/optional; whether any product makes approval non-optional was not tested. Held optional.
- **Legacy Toggl Track KB** not separately fetched; 2.0 KB terminology ("Time Log") may differ from legacy docs. No claims rest on legacy-only behavior.
- **RescueTime mechanics** rest on Tier 2 product pages; no Tier-1 operational detail (how suggestions are accepted, whether unreviewed suggestions persist as entries).

## Final Synthesis

The Time Tracking Application is the record-keeper of time spent on work: its defining core is the time entry — a persistent, addressable duration record — attributed by the user to a work structure (project/task/client/matter), formed through a user act (timer, manual input, timesheet cell, or confirmed suggestion). Around this core, mature products add the timesheet's period views, reports that break the population down by every attribution dimension, billable flags and rates, budgets and estimates-vs-actuals, reminders and capture aids, multi-surface clients, team/permission layers, and integrations into PM and accounting tools. Organization-tier products add the optional approval-and-locking discipline that stabilizes the numbers for billing, payroll, and compliance. The Type's edges are exact: where records form without the user's hand and serve usage interpretation, it is a Productivity Activity Tracker; where the record is attendance for payroll, it is the time clock/T&A family; where the record plans the future, time blocking; where it bounds motivational sessions, the focus timer; where rate cards, invoice generation, and resource economics become the center, PSA. The paper timesheet satisfies the core with no software — the Type is older than its tools.
