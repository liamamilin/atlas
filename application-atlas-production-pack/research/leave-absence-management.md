# Research Notes — Leave & Absence Management

## Research Goal

Determine what a **Leave & Absence Management** application actually is as an Application Type: the core objects it maintains, the lifecycle it administers, the workflows employees / managers / HR perform, the rules that govern behavior, and — critically — its boundaries against the dense neighboring cluster (Time & Attendance System, Employee Scheduling Platform, Payroll System, HRIS/HCM, Approval Workflow Platform, Benefits Administration Platform, Employee Portal, HR Case Management, Workforce Management for Contact Centers).

Directory context: leaf sits in section 09 HR, Workforce & Talent, between Employee Time Clock and Employee Scheduling Platform. Already-processed neighbors describe it consistently as "the absence discipline": Employee Scheduling ("manages approved absence as its subject; scheduling consumes leave as an assignment constraint"), Employee Time Clock ("manages time away from work (requests, balances, accruals)"), Benefits Administration ("leave events affect eligibility, coverage, and billing, but the managed object is absence"), HR Compliance ("leave systems grant leave" — execution systems).

## Initial Boundary

Working hypothesis before research:

- Core purpose: govern employee time away from work — request, approve, track balances, record taken absence.
- Likely confusion set: Time & Attendance (actuals vs planned absence), Scheduling (plan vs constraint), Payroll (pay computation vs absence record), HRIS (module vs discipline), generic approval workflow (machinery vs entitlement accounting).
- Known market structure: most leave functionality ships inside HRIS/HCM suites, but standalone products exist at two poles — lightweight time-off trackers and dedicated leave-of-absence compliance platforms.

## Research Questions

1. What objects does the system maintain? (absence types, policies, balances, requests, calendars, certificates, cases?)
2. How does absence enter the system — request only, or also direct recording (sick call-ins, manager entries)?
3. What does "management" add beyond a shared out-of-office calendar — entitlement accounting? policy rules? approval routing?
4. How do balances work — grant vs accrual vs statutory entitlement vs unlimited? carryover? proration? negative balances?
5. What rules constrain a request — coverage caps, blackout dates, notice periods, documentation?
6. How does the absence record leave the system — payroll handoff, calendar feeds, status changes?
7. What is the long-term-leave / leave-of-absence pole (statutory leave, FMLA-class case management) and is it the same Type?
8. Where is the line to Time & Attendance, Scheduling, Payroll, and generic approval tooling?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer tiers + different geographies:

| Product | Pole | Segment / Geography | Why sampled |
|---|---|---|---|
| **Timetastic** | standalone lightweight leave planner | UK SMB | pure-play time-off tracker; excellent Tier-1 help centre |
| **Personio** | HR-suite absence module (deep policy engine) | European mid-market | statutory-leave-aware entitlement engine; Tier-1 help centre |
| **Factorial** | HR-suite absence module (global SMB) | Spain/global SMB | broad absence + deduction machinery, multi-country; Tier-1 help centre |
| **AbsenceSoft** | dedicated leave-of-absence & accommodations compliance platform | US enterprise (also TPA/PEO operators) | the compliance/case-management pole; Tier-2 product documentation |

Considered and not sampled: BambooHR (help centre JS-blocked, support page 403 — abandoned per network rule), Workday / UKG (operational docs gated behind login; recorded as market context only), Rippling (help centre JS-empty), Vacation Tracker / LeaveBoard (would duplicate the Timetastic pole).

## Sources

Research date: **2026-09-07**

- Timetastic — homepage https://www.timetastic.co.uk/ ; Help Centre https://help.timetastic.co.uk/ (collections + articles: Setting different types of leave; Set your annual allowances; Set who approves leave; Maximum absent; Sick Leave — recording and reporting; Booking time off)
- Personio — product page https://www.personio.com/product/absence-management/ ; Help Centre https://support.personio.de/hc/en-us (section "Time off, leaves, and sick days"; articles: Create time off types; Create time off policies; Set up statutory and non-statutory entitlement)
- Factorial — Help Center https://help.factorialhr.com/ (sections: Absences & approvals; Time-off settings; Time Off Deductions — article inventory observed; individual article bodies not retrieved)
- AbsenceSoft — homepage https://absencesoft.com/ ; Leave of Absence https://absencesoft.com/leave-of-absence/ ; Platform Overview https://absencesoft.com/platform-overview/

Sourcing limitations: BambooHR unreachable (2 failures — abandoned). Workday/UKG operational documentation gated; no claims in this research depend on them. Factorial evidence is article-inventory + section structure level (titles directly observed; bodies not fetched) — observations from Factorial are marked accordingly and kept at capability level, not precise-rule level.

---

## Product A — Timetastic (standalone lightweight planner, UK SMB)

### Key observations (evidence layer A unless noted)

- **Positioning**: "staff leave planner"; explicitly anti-spreadsheet/anti-form. Separate product line "Rota & Time Clock" for scheduling/time clocking — absence and scheduling are deliberately different products.
- **Leave types** are the configuration spine: preloaded types (Holiday, Unpaid Leave, Sick Leave, Maternity, Paternity, Meeting, Compassionate, Working from home); add/edit/delete. Per-type settings:
  - whether bookings **deduct from the annual allowance** (locked once bookings exist against the type)
  - whether the type **requires approval**
  - whether it counts toward the department **maximum-absent** cap
  - **visibility**: Private (coworkers see that someone is off, not why — hidden from everyone except approver/manager/admin) vs Public (visible to all)
  - icon/color for calendar rendering; how it displays in external calendar integrations (busy / available / out-of-office)
  - Pro tier: **hard caps per leave type** per leave year (distinct from the allowance; not per-user overridable)
- **Allowances**: per-employee, in days and/or hours, per **leave year** (configurable start/finish); standard model = granted up front at year start; **accrued** granting available on Pro; **carry-forward** setting; **unlimited allowance** option; **pro-rata** calculations; bulk edits; prior/next-year allowance editing.
- **Approval**: default approver = department manager; per-employee approver override (e.g., a manager's own leave approved by a director); admins can approve anyone; requests inbox sectioned by approver; email notifications to approver only.
- **Booking**: from a wallchart or personal calendar — click a day or drag a range; pre-populated form; attachments can be added to bookings; cancel and amend flows; **TOIL (time in lieu)** as a leave type pattern.
- **Coverage constraints**: **Maximum absent** per department (cap on concurrent absences; per-type inclusion toggle; employee blocked at request time with a message; manager/admin can book on behalf and **override** the warning). **Locked dates** — company/department/user blackout periods.
- **Unplanned absence**: sick leave recorded through the same booking form by the employee, a manager, or an admin; per-employee and org-wide reporting/exports (Excel).
- **Visibility & sharing**: personal holiday calendar with allowance usage and use-before dates; wallchart of the whole org; email notifications and weekly absence summaries; iCal/webcal calendar feeds; Slack/Teams integrations; mobile apps.
- **Analytics (Pro)**: "Absence Insights", "Burnout Board" (branded).
- Historical check: the model is a direct digitization of the paper vacation ledger + request form (request → signature → days taken against annual entitlement). Nothing in the core requires cloud, apps, or integrations.

## Product B — Personio (European mid-market HR suite, absence module)

### Key observations (evidence layer A)

- **Positioning**: Absence Management is a Core-HR module; marketing emphasizes request/approve in one click, automatic balance calculation ("how many days taken and left"), manager calendar overview, sick-leave reporting; connected to Attendance Tracking and People Analytics.
- **Time off types**: created under Settings > Time off; settings include name, custom ID, calendar color, **category**, **time unit (daily or hourly, immutable after creation)**, and a "reduce target hours / count tracked time as overtime during time off" switch that ties absence into working-time accounting. Two documented use families: *standard* time off (employee not expected to work — paid leave, sick days, special leave) vs *productive* time off (expected to work — work from home, business trip, training).
- **Permissions-gated visibility**: employees can only see/request a type if their role has "Propose" permission for it (own/subteam/etc.), and only if a **time off policy** is assigned to them.
- **Time off policies** — the entitlement engine. One policy per type per employee at a time; multiple policies per type for market-specific rules; country-specific templates (Germany, Netherlands flagged as containing special calculation logic). Policy sections:
  - **"When is this considered time off?"** — deduction basis: workdays Mon–Fri excl. public holidays / Mon–Sat / workdays incl. or excl. public holidays / every day — computed against the employee's work schedule.
  - **Half-day requests** (daily types); hourly types allow half days on first/last day.
  - **Substitutes**: required/optional/none; substitution does **not** transfer approval permissions — approvals must be delegated separately.
  - **Certificates**: after N days of an absence, the employee must upload a certificate; in Germany, electronic sick certificates (eAU) are retrieved automatically instead of manual upload.
  - **Entitlement**: fixed or **unlimited** (open-ended periods for sick/family/public-obligation leave). Fixed entitlement configures: amount; **accrual-year start**; **granting cadence** (yearly / half-yearly / quarterly / monthly; all-at-once or monthly instalments for hours; start- or end-of-month); **onboarding accrual limits**; **tenure-based granting** (one-off or recurring rewards on work anniversary); **carryover** (amount cap + use-by window in months); **proration** (mid-year join/leave by months or days; part-time by weekly days or hours; rounding rules).
  - **Long-term effects**: after N days of an absence — **compensation proration** (salary reduced, down to zero; with Personio Payroll this is instead handled by payroll questions), **employee status** automatically flips to "Leave" (stops notifications, hidden from people list/org chart; auto-returns to Active), and **impact on other paid time off** (other types' accrual reduced at daily / calendar-monthly / rolling-monthly rates).
- **Statutory vs non-statutory entitlement** (Netherlands example): statutory entitlement required by law plus employer's non-statutory top-up with longer carryover (up to five years); a single type can hold both, consumed **first-expiring-first**; balance summaries show expiration dates and carryover rows.
- **Approvals**: configurable approval rules ("Set up time off approval rules"); approve/reject from requests; iCal team calendar; unused-time-off reports; balance adjustments (manual corrections).
- **Long-term leaves** managed inside time off policies (transition articles document maternity protection setup and long-term leave periods).

## Product C — Factorial (global SMB HR suite, absence module)

### Key observations (evidence layer A at inventory level; capability level only — article bodies not fetched)

- Help-center structure documents the same object set: **absence types**; **request and assign** time off (including bulk assignment); **time off approver** role and **approval systems** (approve/reject; global approver role); **allowances/counters** with adjustments and manual corrections; **time off calendar**; **public holidays** (per-year setup; bank-holiday treatment settings); **company-wide closures** as absence types; **blocked periods** (requests during them are handled specially); **sick leave registration**; **modify/delete absence**; **time off report export**.
- **Allowance kinds** documented as distinct configurations: **fixed balance**, **based on time worked**, and **overtime-based** allowances — i.e., entitlement can accrue from hours worked or overtime, not only calendar grants.
- **Deduction machinery** is a first-class documented area: counters deduction; calendar days vs **working days** (contract/shifts/work variants); **half-day deduction scenarios**; **jours ouvrables vs jours ouvrés** (French working-day conventions); carryover deduction; absences spanning more than one cycle.
- **Tenure periods**, **carryover at year end**, **negative balance compensation**, **balance transfer when changing policies**, **imports** of allowances, **document uploads** configured per absence type.
- AI assistance: "Smart Recommendations to Approve Absences"; hourly allowances can be blocked in 15/30-minute increments.
- Adjacent modules in the same suite: time tracking (clock in/out, timesheet approval), shift management (absences appear in shift planning), payroll integrations (absence sync to country payroll providers; German eAU via DATEV integration).

## Product D — AbsenceSoft (dedicated leave-of-absence & accommodations platform, US enterprise)

### Key observations (evidence layer A at product-page level)

- **Positioning**: "leave and accommodations management" end to end — from initial leave request to return to work; used by employers in-house **and by TPAs/PEOs** operating leave programs for client companies. Metrics framed around case volume and caseload per case manager.
- **Compliance engine**: tracks a large library of US federal/state/territorial leave and accommodation laws (FMLA, ADA, PWFA, state PFML programs; "200+" cited on multiple pages, "250+" on one — kept qualitative here), maintained by an in-house legal/compliance team, with audit trails.
- **Eligibility determination**: the platform calculates an employee's eligibility under the applicable laws "in seconds"; **company-specific policies** can be added and managed centrally alongside statutory ones.
- **Case management**: every leave is a **case** — centralized record of requests, communications, documents, data; **continuous vs intermittent** leave tracked differently (intermittent usage tracked); **concurrent leaves stacked** correctly; automated workflows; return-to-work tracking; managers see employees' leave status and **return-to-work dates** for scheduling.
- **Employee experience**: self-service portal to request leave or accommodation from any device, review status, drag-and-drop required documents, communicate with HR in-platform; **bi-directional text messaging** stored in-platform as a communications record; **barcoded fax intake** from healthcare providers auto-attaches to cases.
- **Communications machinery**: automated notifications and reminders; form/email/letter templates auto-filled with employee and regulatory details; branded, customizable; outbound texts.
- **Payroll calculations**: a distinct platform capability for pay-during-leave computation (statutory wage replacement is part of the leave obligation in this pole).
- **Reporting/dashboards**: program data views, custom reports, prebuilt and shareable dashboards.
- **Integration spine**: HRIS/HCM/payroll/time-and-attendance integrations and SSO; employee data synced automatically.

---

## Cross-product Comparison

| Structure | Timetastic | Personio | Factorial | AbsenceSoft |
|---|---|---|---|---|
| Absence types as configured categories | ✔ leave types with per-type rules | ✔ time off types (+ productive/standard families) | ✔ absence types (+ company-closure types) | ✔ statutory policies + company policies |
| Employee absence record with state | ✔ bookings (pending/approved/taken; cancel/amend) | ✔ time off periods; status effects for long leaves | ✔ absences (modify/delete; assign in bulk) | ✔ cases with lifecycle to return-to-work |
| Governed entry & decision | ✔ request → approver (per-type approval toggle; override path) | ✔ request → configurable approval rules; permission-gated types | ✔ request → approver role / approval systems | ✔ request → eligibility determination → case workflow |
| Entitlement accounting | ✔ annual allowance (days/hours; up-front or accrued; carry-forward; unlimited option; type caps) | ✔ fixed/unlimited entitlement; cadence; tenure; carryover; proration; statutory/non-statutory | ✔ counters: fixed / time-worked / overtime-based; tenure; carryover; negative balances | ✔ statutory entitlement banks (e.g., protected-leave allowances) consumed by continuous/intermittent usage |
| Balance visibility to employee | ✔ personal calendar + summaries | ✔ balance summary with expirations | ✔ counters visible (employee vs admin views documented) | ✔ self-service status |
| Team calendar / who's out | ✔ wallchart + calendar + iCal feeds | ✔ team calendar + iCal | ✔ time off calendar | manager view of leave status & return-to-work dates |
| Holiday calendars | ✔ public holidays | ✔ custom bank-holiday calendars | ✔ public holidays per year; bank-holiday treatment | (US-market: holiday handling inside policies — not separately surfaced in sampled pages) |
| Documentation/certificates | ✔ attachments on bookings | ✔ certificate-after-N-days; German eAU retrieval | ✔ document uploads per absence type | ✔ drag-and-drop documents; fax intake; certification workflow |
| Coverage constraints | ✔ max-absent per department; locked dates | (not surfaced in sampled articles) | ✔ blocked periods | (not the framing; eligibility is the gate) |
| Payroll handoff | (exports; separate Rota & Time Clock product for timesheets) | ✔ long-term compensation proration; payroll questions | ✔ absence sync to country payroll; eAU via DATEV | ✔ dedicated payroll-calculations capability |
| Deduction-basis rules (which days count) | (working schedule per user; allowance in days/hours) | ✔ five documented deduction bases vs work schedule & holidays | ✔ calendar vs working days; ouvrable/ouvré; half-day scenarios | (statutory rules embedded in compliance engine) |
| Long-term leave effects (status, pay, accrual) | — | ✔ status flip, compensation proration, other-accrual reduction | (policy-change/balance-transfer machinery; not surfaced as status effects) | ✔ case-shaped: intermittent usage, stacking, return-to-work |
| Statutory-law layer | — (UK-style company policy) | ✔ statutory vs non-statutory entitlement; country templates; maternity protection | ✔ country conventions (FR), country payroll sync | ✔ US federal/state law library + eligibility engine |
| AI assistance | — (Pro analytics only) | (AI assistant elsewhere in suite) | ✔ smart approval recommendations | ✔ "purposeful AI" positioning |
| Operator model | employer self-serve | employer self-serve | employer self-serve | employer in-house **or TPA/PEO-operated** |

### Reading of the comparison

- The four products share a stable skeleton: **types → policy/entitlement → request/entry → decision → recorded absence → balance & calendar → reporting/handoff**.
- The poles differ in what they add around that skeleton: Timetastic adds visibility/sharing polish; Personio and Factorial add deep entitlement/deduction computation and country compliance; AbsenceSoft adds statutory-law eligibility, case management, and pay-during-leave calculation.
- "Approval" is universal but not uniformly mandatory: Timetastic lets a type skip approval; Personio makes approval configurable per workflow; the invariant is the **governed decision/record step**, not the approval form itself.

## Canonical Model (L0 → L3)

### L0 — Defining Invariant (minimal)

A Leave & Absence Management application is recognizable by exactly these four structures:

1. **Absence types as configured policy categories** — the organization defines the kinds of time away from work it recognizes (vacation, sick, parental, unpaid, …), and each type carries rules: whether it draws on an entitlement, whether it needs approval, what documentation it requires, who may see it. Remove → a generic out-of-office calendar.
2. **The employee absence record** — a dated period of absence attributed to an identified employee, held as a persistent record with a lifecycle state (requested → approved/denied → taken → cancelled/edited). Remove → an org chart or a payroll system.
3. **The governed entry-and-decision flow** — absence enters through a defined channel (employee request, or manager/HR entry on the employee's behalf, e.g., sick call-ins), is validated against the type's rules, and is decided or recorded by a designated authority, with the decision recorded. Remove → attendance actuals (Time & Attendance) or a shared who's-out calendar.
4. **Entitlement accounting** — per employee per type, the system tracks how much leave the employee is entitled to (granted up front, accrued over time, fixed by statute, or set unlimited) against what has been taken, yielding a balance. Remove → a generic approval workflow with a leave template.

Historical check (§24): the paper-era realization — a vacation request form signed by a supervisor and a ledger card tracking days taken against annual entitlement — satisfies all four structures without cloud, apps, accrual engines, or integrations. Statutory sick-leave files (certificate + episode record) satisfy 1–3 with the entitlement expressed as a legal allowance. The definition is not overfit to the modern SaaS accrual engine.

### L1 — Common Mature Structure

Present across the sample; expected in market but not definitional:

- Employee self-service: request submission, balance view, personal history/calendar.
- Approver role with a request inbox/queue; email/push notifications on request and decision.
- Team/department calendar ("who's out") plus calendar interoperability (iCal feeds, Slack/Teams display).
- Holiday calendars (public/company holidays, per location) feeding deduction logic.
- Per-employee working schedules as the deduction basis; day/hour units; half-day handling.
- Grant/accrual machinery: granting cadence, carryover caps, tenure rewards, proration for join/leave/part-time, rounding.
- Documentation handling: attachments, sick notes/certificates, certificate-after-N-days triggers.
- Reporting and exports: balances, absence trends, sick-leave statistics; payroll handoff of taken leave.
- Substitute/delegate selection during absence.
- Coverage constraints: blocked/blackout periods, concurrent-absence caps.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment:

- **Long-term leave effects**: automatic employee-status change ("on leave"), compensation proration during extended absence, reduction of other accruals (Personio-documented; case-shaped equivalents in the compliance pole).
- **Statutory-leave compliance layer**: statutory vs non-statutory entitlements with first-expiring-first consumption (NL example), country policy templates, electronic sick-certificate retrieval (DE), maternity protection, French working-day conventions — geography-dependent.
- **US regulatory case management**: law-library-driven eligibility determination, intermittent-leave usage tracking, concurrent-leave stacking, certification workflows, return-to-work management, accommodations alongside leave — the dedicated-platform pole.
- **Pay-during-leave calculation** as a platform capability (compliance pole) vs payroll handoff (suite/tracker poles).
- **Operator model**: employer self-serve vs TPA/PEO-operated leave programs.
- **TOIL banks**, negative-balance compensation, balance transfer between policies, unlimited-leave policies.
- **AI assistance** (approval recommendations, policy Q&A).
- **Engagement analytics** (burnout-style boards, absence insights).

### L3 — Vendor-specific (research notes only)

- Timetastic: "Burnout Board", wallchart metaphor, separate Rota & Time Clock product line, per-type hard caps as a Pro feature.
- Personio: "productive time off" category framing, target-hours/overtime interplay, Voyager community, country templates for DE/NL.
- Factorial: One AI assistant, a3innuva/DATEV/Silae payroll integrations, Forfait Jours handling, 15/30-minute hourly blocking.
- AbsenceSoft: Compliance Engine™ branding, barcoded fax intake, LeaveLab community, caseload metrics.

## Vendor-specific Findings

See L3. None of these were promoted into the canonical model. The AbsenceSoft payroll-calculations capability is treated as a pole-specific extension of the payroll handoff, not a core structure — the tracker and suite poles explicitly hand pay computation to payroll.

## Boundary Findings

1. **vs Time & Attendance System** — sharpest seam. T&A records *actual worked time* (punches, timesheets) and enforces attendance/labor rules; this Type governs *planned and approved absence* and entitlement. They interlock: Personio's absence types reduce target hours and count worked time during absence as overtime; Factorial computes time-tracking balances "considering time off"; Timetastic ships scheduling/time-clocking as a separate product. Test: remove entitlement/policy structure and keep actuals → T&A; keep entitlement and drop actuals → this Type.
2. **vs Employee Scheduling Platform** — scheduling decides who works when (shifts as objects); leave is an upstream constraint that appears on the schedule. Approved leave blocks or flags conflicting assignments (per the scheduling document). Test: remove shifts/assignment machinery → this Type; remove entitlement accounting → scheduling with a time-off feature.
3. **vs Payroll System** — payroll computes pay; leave records the absence that feeds it (paid leave as earnings input, unpaid leave as no pay, accruals as pay-adjacent data). Personio explicitly routes long-term compensation proration to payroll when its payroll product is used. Exception noted: the compliance pole adds pay-during-leave calculation because statutory wage replacement is part of the leave obligation — recorded as a pole extension, not a core structure.
4. **vs HRIS / HCM** — packaging, not identity: in today's market most leave functionality ships as an HRIS/HCM module, but standalone products exist at both poles (Timetastic; AbsenceSoft), and the absence discipline has its own object set and lifecycle. The leaf remains a definable Type (same reasoning as athlete-injury-availability-management inside AMS). The HRIS document already treats "time off and absence management" as one module among many; this leaf documents that module's discipline.
5. **vs Approval Workflow Platform** — generic request/approval machinery can route leave requests (the approval-workflow document lists leave as a template type), but has no absence types, no entitlement ledger, no balance arithmetic, no holiday/deduction basis. Test: remove entitlement accounting → generic approval workflow.
6. **vs Benefits Administration Platform** — leave events affect benefits eligibility/coverage/billing, but the managed object is absence, not an election (consistent with the benefits document).
7. **vs Employee Portal / Employee Service Portal** — portals present leave tasks and hand off to the owning system; this Type owns the transaction and the record.
8. **vs HR Case Management** — the compliance pole is case-shaped (intake, workflow, documents, communications), but its center is the absence entitlement lifecycle under law, not multi-topic HR case intake/triage.
9. **vs Workforce Management for Contact Centers / Agent Scheduling** — coverage-aware time-off approval exists there too, but the center is forecast-driven staffing; leave is one shrinkage input.
10. **"Remove what to become another Type" summary**: remove the absence record and entitlement → calendar/approval tooling; remove planned-absence semantics and keep actuals → Time & Attendance; remove entitlement and keep generic routing → Approval Workflow Platform; remove absence and keep elections/coverage → Benefits Administration.

## Uncertainties

- Enterprise HCM absence modules (Workday, UKG, SAP SuccessFactors) were not directly documented (gated docs). Their inclusion in the market picture is common knowledge kept at packaging level only; no structural claims depend on them. The enterprise pole is evidenced via AbsenceSoft (dedicated) and Personio (suite).
- BambooHR (US SMB suite pole) unreachable; Factorial covers the SMB-suite pole instead. US-specific SMB accrual vocabulary (e.g., PTO payout on termination) is therefore not asserted.
- Factorial observations are capability-level (article inventory); precise Factorial rule details (e.g., exact deduction scenarios) were not verified and are not asserted.
- Whether "accommodations" (ADA-style workplace adjustments) belong inside this Type or adjacent is only evidenced at the compliance pole (AbsenceSoft bundles them); the tracker/suite poles show no accommodation machinery. Treated as a pole-specific extension, not core.
- Numeric limits (carryover caps, certificate thresholds, caseload figures) are product-specific configuration or marketing metrics; none are asserted as Type-level facts.

## Final Synthesis

A Leave & Absence Management application is the employer-side system of record for **time away from work**: it maintains the organization's **absence types** (each a small policy: entitlement, approval, documentation, visibility), records each absence as a **dated, employee-attributed record with a state**, moves every absence through a **governed entry-and-decision flow** (request or report → rule check → recorded decision), and keeps **entitlement accounting** per employee per type (granted, accrued, statutory, or unlimited, against usage, yielding a balance). Around this core, mature products add self-service, approval queues and notifications, who's-out calendars and holiday calendars, deduction-basis rules tied to work schedules, documentation/certificate handling, coverage constraints, reporting, and payroll handoff. The market realizes the Type at three poles — lightweight standalone trackers, HRIS/HCM suite modules with deep entitlement engines, and dedicated statutory-leave compliance platforms — which differ in the compliance and pay layers they add, not in the core.
