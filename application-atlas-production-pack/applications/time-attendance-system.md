# Time & Attendance System

## Overview

A **Time & Attendance System** is an organization-side system of record for workforce time. It captures when employees work — at shared clocking terminals, on personal devices, or as entered time — assembles that time into approved per-employee hours, maintains a standing picture of the workforce's attendance in which working, late, absent, and on-approved-leave are distinguishable states, and applies the organization's time policies (overtime, breaks, rounding, absence kinds and balances) to that record so the hours it produces are payroll-ready and defensible under audit.

The defining structure is small:

```text
Worked-time record of record
└── Standing attendance state (worked time + time away held together)
    └── Time-policy administration (rules applied to the record)
        └── Payroll-ready, auditable hours
```

Everything commonly associated with modern products — biometric terminals, GPS and geofencing, live attendance dashboards, overtime time banks, statutory compliance engines — is widespread in current products but is implementation depth, not the defining core. A factory punch clock beside a timekeeper's ledger, with a daily attendance register and the works rulebook, satisfies the same structure: worked time recorded, attendance state maintained with time away distinguished, rules applied under supervision.

The Type is a system level above the Employee Time Clock: the clock's whole world is punches, timesheets, approval, and payroll handoff, and the Time & Attendance System contains that layer — but additionally makes attendance and absence administration and time-policy administration primary objects. When a product's documented world is only punches and timesheets, it is the clock; when attendance state and time policy are administered in their own right, it is this Type.

## Users & Context

Primary users:

- **Employee (hourly or shift worker)** — clocks in and out at a shared terminal or personal device, records breaks, sees accumulated hours, and requests time off. The largest user population; interaction is frequent but brief.
- **Supervisor / shift manager** — watches the live attendance picture (who is on, late, absent, on leave), resolves exceptions such as missed punches, approves timesheets, and decides leave requests.

Secondary users:

- **HR / time administrator** — owns the framework rather than individual records: time policies, absence kinds and accrual rules, work-schedule settings, clocking surfaces, multi-location configuration, and compliance reporting.
- **Payroll processor** — consumes the closed, approved hours each pay period.
- **HR / operations leadership** — consumes attendance, lateness, and overtime reporting for workforce decisions.

The typical context is organizations where time worked is the basis of pay and compliance: retail, hospitality, healthcare, manufacturing, logistics, construction, education, government, and field services. A second context is statutory: in jurisdictions where recording working time is a legal employer obligation, office-based organizations use the same systems for compliant time records. Multi-site operation is common; the system is usually administered centrally with per-location or per-group policy variation.

## Core Model

### The Defining Core

**The worked-time record.** The foundation is a per-employee record of time worked: timestamped boundary events (clock in, break start and end, clock out) captured at a clocking surface, or time entered directly. Entries assemble into hours for defined periods — the timesheet — which is reviewed, corrected, and approved under manager authority, and then handed to payroll. The organization's answer to "when did this person work, and how much" lives here.

**The standing attendance state.** Worked time alone does not make attendance manageable, so the system holds worked time and time away from work together in one picture. For each day and each employee, the state is distinguishable: worked (with hours), late (relative to planned or expected work), absent without recorded cause, or on approved leave. Absence kinds — vacation, sick leave, public holiday, unpaid leave — are recorded, requested, and approved inside or immediately beside the time system, so a supervisor looking at a day sees "on approved vacation", not an unexplained gap. This combined state is monitored as a management discipline: live views of who is currently present, named exception classes (missed punch, late arrival, long shift, absence), and attendance reports over time.

**Time-policy administration.** The organization's time rules exist as governed configuration, not ad-hoc settings: overtime thresholds and rates, break requirements (paid and unpaid), rounding, absence kinds with accrual or balance semantics, and the mapping of hours to pay-relevant classes. The system applies these rules to the record — computing overtime, flagging rule violations such as missed or short breaks, deducting breaks, rounding, maintaining balances — and keeps the result defensible: approval states, recorded corrections, and an audit trail of who changed what and when. Rules are commonly scoped per group, location, or employment terms, because pay and attendance rules differ across sites, roles, collective agreements, and jurisdictions.

```text
Employee
└── Time entry / punch (boundary events at a clocking surface)
    └── Worked-time record → assembled hours per period
        ├── judged against: planned/expected work → late, absent, exceptions
        ├── judged against: time policies → overtime, breaks, rounding, premiums
        ├── combined with: recorded absence → working / late / absent / on leave
        └── approved → closed period → payroll-ready hours
```

If the worked-time record is removed, nothing remains. If the attendance state is removed, the product collapses to the Employee Time Clock — punches and timesheets with no managed picture of presence and absence. If policy administration is removed, the product collapses to a manual attendance register. All three must hold for the Type.

### Standard Capabilities

Mature products commonly carry most of the following. They make the system practical at organizational scale but do not define it.

- **Clocking surfaces** — a shared terminal or kiosk at the workplace (dedicated device, tablet app, browser, wall-mounted device), personal mobile/web/desktop apps, purpose-built hardware terminals with badge or keypad entry, and offline capture that syncs when connectivity returns. Many products offer several at once, "mix and match" per workforce segment.
- **Identity verification at the surface** — PIN, QR code, badge/RFID, photo capture, or facial recognition, aimed at preventing one employee clocking for another.
- **Schedule anchoring** — punches and entries are compared against planned shifts or expected hours: clock-ins outside windows may be restricted or flagged, and no-shows surface as named exceptions. Where scheduling is a separate product or module, the schedule flows in as the reference; where it is configuration, fixed and flexible work schedules are defined in the system (in some products, flexible schedules are themselves submitted for approval).
- **Exception machinery** — missed punches, late arrivals, long shifts, and absences surfaced as alerts or queues, with mitigations such as reminders and automatic clock-out at shift end.
- **Approval workflow** — timesheets move from pending to approved under manager review; periods close and freeze; approved records must be explicitly reopened to change, and rule-derived values recalculate on reopen. Some products compare clocked time against approved time, allow auto-approval, or restrict approval to exception cases only.
- **Overtime machinery** — hours classified against configured thresholds and rates; in many products overtime is also a balance (a time bank with earned or deficit hours).
- **Break handling** — paid and unpaid break recording, automatic deduction, and alerts or approvals when recorded time violates break requirements.
- **Rounding** — punch timestamps adjusted to configured intervals for payroll consistency, with actual times preserved.
- **Absence and balance machinery** — leave policies with accrual methods (per period worked, fixed annual grants, pro-rata), carryover, public holidays, balances with history, request-and-approve flows, and entering absence on an employee's behalf.
- **Attendance reporting** — live dashboards of current attendance status, plus reports on attendance, lateness, overtime, and hours by location or group.
- **Audit trail** — a recorded history of edits, on-behalf entries, approvals, and reopenings.
- **Payroll handoff** — export files or formats, integrations with payroll/HR/ERP systems, or built-in payroll in some products.
- **Administration at scale** — multi-location and multi-group structures, role-based permissions, and policy scoping per group or site.
- **Job or project attribution** — hours attributed to jobs, projects, departments, or cost centers for labor costing; common but secondary to attendance.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:   Capture surface
Implementations:  shared kiosk/terminal, personal mobile/web app, hardware badge or
                  biometric terminal, wall-mounted shared device with QR clocking,
                  calendar/timesheet entry for non-shift staff

Concept:   The expectation frame for attendance
Implementations:  published shift schedules (from a bundled or sibling scheduling
                  product), configured work schedules (fixed or flexible), expected
                  weekly hours

Concept:   Time policy
Implementations:  pay-rule engines scoped to locations/groups/unions/laws, break and
                  meal rules with alerts, rounding settings, overtime rate tables,
                  time banks, accrual policies

Concept:   Payroll destination
Implementations:  export files (CSV/Excel), provider-formatted reports, direct
                  integrations with payroll/HR/ERP systems, built-in payroll
```

A reader who has only seen one implementation — a phone app with facial recognition, or a badge terminal in a factory — should still recognize the other as the same Type.

## How It Works

### Configure (administrator, at setup and on change)

```text
Set up the workforce (employees, groups, locations, employment terms)
→ configure the expectation frame (work schedules, or expected hours per employee)
→ configure time policies (overtime, breaks, rounding, absence kinds, accrual rules)
→ set up clocking surfaces (shared terminals, personal apps, hardware)
→ connect or prepare the payroll destination
```

### The daily loop (capture → compare → act)

```text
Employees clock in / take breaks / clock out (or record absence requests)
→ entries assemble into the day's worked time
→ the system compares entries against the expectation frame and the rules:
   late arrival, early departure, missed punch, long shift, short break,
   unplanned absence, overtime accrued
→ exceptions surface to supervisors on a live attendance view
→ supervisors investigate and act: message the employee, correct the record,
   approve an exception, or record the missed work as leave
```

This loop is the attendance discipline: every day, the state of every employee becomes visible and actionable, rather than accumulating silently until payday.

### The absence loop (request → decision → state change)

```text
Employee requests time off (or manager/HR records it on their behalf)
→ checked against policy (balance, notice, coverage limits)
→ approved or declined by the designated approver
→ the absence appears in the attendance state for those days
→ balances adjust according to the absence kind's accrual rules
```

Because absence lives in the same system, the boundary between "absent without cause" and "on approved leave" is always explicit — and some products let a supervisor reclassify a worked-time record as leave during approval (for example, when a reported sick day turns out to be half worked, half leave).

### The period loop (review → approve → hand off)

```text
Pay period ends
→ managers review pending timesheets (individually or in bulk)
→ corrections are made before approval; every change is attributed
→ timesheets are approved and the period closes
→ approved hours (with overtime, breaks, leave, and pay-class detail) are
   exported or integrated to payroll
```

Approval is the gate between recorded time and payable time. After closure, records are frozen; changes require reopening the period, and rule-derived values (overtime, rounding, break deductions) are recalculated under the administrator's rules.

### The compliance loop (rules → flags → resolution → evidence)

```text
Rules from internal policy, collective agreements, and law are configured
→ the system evaluates recorded time against them continuously
→ violations surface as alerts or approval triggers (missed breaks, overtime
   thresholds, rest requirements, entry anomalies)
→ resolutions are recorded; the corrected record and its history are retained
→ reports provide the audit-ready view for payroll, HR, and inspectors
```

In compliance-oriented deployments this loop is the product's reason to exist: the record must not only be accurate but demonstrably governed.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Clocking surface (shared terminal / kiosk / personal app)

- shows the current time, the employee's schedule where present, and current clock state
- primary actions: identify (PIN/QR/badge/face), clock in, start/end break, clock out
- may capture location, photo, or prompt for a job/project or reason

### Live attendance view (supervisor)

- shows who is currently on the clock, late, absent, or on leave, typically for the day
- surfaces exceptions as a queue: missed punches, long shifts, unplanned absences
- primary actions: investigate an exception, message the employee, jump to the timesheet, record absence

### Timesheet review & approval console (manager, web)

- lists timesheets by period, employee, group, and status
- typical information: entry times, computed hours, breaks, overtime, exceptions, leave taken, comments, change history
- primary actions: edit entries, add entries on behalf, convert to leave, approve (single or bulk), unapprove/reopen, export

### Leave / time-off management

- request forms, a team or organization calendar of upcoming absences, balance views
- primary actions: request, approve/decline, enter on behalf, adjust balances, configure leave kinds and accruals

### Policy and rule configuration (admin)

- work schedules, overtime rules, break rules, rounding, absence kinds, accrual policies, clocking surfaces and their verification methods, payroll export setup — scoped per location, group, or employment terms

### Reporting

- attendance, lateness, overtime, hours by group/location/project, and payroll-preparation reports; scheduled or on demand

### Employee self-service

- own hours and current period state, own schedule, absence requests and balances

## Important Rules / Behaviors

### Worked time and time away must be distinguishable

The attendance state only works because the system separates "worked", "absent unexplained", and "on approved leave". An unexplained gap is an exception demanding action; an approved absence is an expected state with its own record. Products commonly let managers reclassify between these during approval, attributed and audited.

### Approval gates payroll

Unapproved timesheets are working records; approved timesheets are payable records. Editing is normally allowed only before approval; afterwards a timesheet must be reopened, and rule-derived values are recalculated under the governing rules. Closed periods freeze records.

### Attendance is judged against an expectation

Whether the expectation is a published shift, a configured work schedule, or expected weekly hours, the system needs a reference to name lateness or absence. The expectation is plan-side data — owned by scheduling where scheduling exists — but the judgment against it happens here.

### Rules are configuration, and their scope matters

Overtime, break, and absence rules are held as policy objects scoped per group, location, or employment terms. Changing a rule changes how past-style entries evaluate on recalculation, which is why recalculation typically happens only on explicit reopen.

### The record is a compliance artifact

Because hours feed pay and, in many jurisdictions, legal record-keeping obligations, the system preserves actual times alongside adjusted values, attributes every correction, and retains history. Products frame this as passing audits and inspections without a scramble; the underlying behavior is an audit trail plus approval states.

### Identity and location evidence is sensitive by design

Verification methods (PIN, badge, photo, facial recognition) and location capture exist to make each record attributable to a person and a place. They are enforcement surfaces for workplace policy and fraud prevention, and their configuration varies by workforce segment and privacy posture.

## Variants

- **Compliance-first pure-play** — time & attendance sold as the whole product, with deep pay-rule administration (union/collective-agreement/local-law rule sets), clock hardware estates, and exception reporting; typical of mid-market/enterprise and public-sector buyers.
- **Scheduling-led suite** — attendance embedded in a workforce suite whose center is shift scheduling; punches are tightly coupled to published shifts and leave to coverage.
- **HR-suite module** — time tracking and absence as modules of an HR platform; the statutory-recording pole (European market) lives here, where compliant time records are a legal employer obligation and time data sits beside core HR records for audit.
- **Freemium attendance tracker** — accessible, app-first capture with live dashboards, anti-buddy-punching verification, and payroll exports; the small-business pole, sometimes straddling into personal time tracking.
- **Enterprise HCM module** — time & attendance inside large human-capital suites, typically with terminal hardware, union/aggregate rule engines, and heavy integration; not directly researched for this document (see Sources).
- **Industry-shaped deployments** — education (attendance tracking with substitute and extra-duty management), public safety (rotation and overtime-heavy rules), healthcare (shift and compliance intensity), manufacturing and logistics (multi-site, job costing).

A variant remains a variant unless it changes the defining core: a product whose whole world is punches and timesheets is the Employee Time Clock even if marketed as "time and attendance"; a product that administers only absence is Leave & Absence Management.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Employee Time Clock | nested layer | the clock's whole world is punch → timesheet → approval → payroll handoff; the Time & Attendance System contains that layer and adds attendance-state and time-policy administration as primary objects |
| Employee Scheduling Platform | plan-side sibling | scheduling owns future work (the plan); this system records and judges actual work against the plan; scheduling products commonly bundle attendance |
| Leave & Absence Management | adjacent sibling | governs planned and approved absence as its subject (types, entitlements, decisions); this system holds absence inside the attendance picture but centers worked time; deep leave policy may be embedded or delegated |
| Payroll System | downstream | consumes approved hours to compute wages, taxes, and payslips; this system produces payroll-ready hours and does not run the pay computation |
| Workforce Management Platform | broader suite | scheduling + time & attendance + forecasting + engagement on one platform; this Type is one major module of it |
| Time Tracking Application | adjacent, easily confused | time is self-logged, task/project-attributed, and voluntary, serving billing and productivity analysis; here time is organization-authorized, attendance-oriented, and payroll-bound |
| Workforce Management for Contact Centers / Agent Scheduling | adjacent, different demand model | staffing derived from queue forecasts and service-level targets at fine interval granularity, not from a worked-time record |
| HRIS / HCM | record master (upstream) | maintains the employment record; the time system consumes employee/employment data and is either a sibling module or integrated |

The most important boundary is with the Employee Time Clock, because the two are nested and the market brands products at both poles "time and attendance". The structural test: if attendance state and time-policy administration are primary documented objects, the product is this Type; if punches and timesheets are the whole world, it is the clock.

## Representative Products

- TCP TimeClock Plus (TCP Software) — compliance-first pure-play time & attendance with pay-rule depth and clock hardware; government, education, healthcare, enterprise
- Deputy — scheduling-led workforce suite with timesheets, leave, and kiosk time capture; mid-market, AU/UK/US
- Personio — HR suite whose time tracking and absence modules carry the European statutory-recording pole; mid-market
- Jibble — freemium attendance-led tracker with live dashboards, facial recognition, and payroll exports; global SMB

Enterprise HCM suites (UKG/Kronos, ADP, Workday) are well-known market examples of the enterprise pole; their documentation was not reachable from the research environment and they were not directly researched for this document.

## Sources

Research date: **2026-09-08**

Primary official documentation:

- TCP Software — TimeClock Plus product and timekeeping pages — https://www.tcpsoftware.com/ , https://tcpsoftware.com/products/timeclock-plus/ , https://tcpsoftware.com/products/timeclock-plus/timekeeping-software/
- Deputy Help Center — Timesheets and Manage leave categories — https://help.deputy.com/hc/en-au/categories/4614232027023-Timesheets , https://help.deputy.com/hc/en-au/categories/17243648734095-Manage-leave
- Personio — Time Tracking product page (with FAQ) and Help Center (Employee Management: "Attendance, work schedules, and overtime"; "Time off, leaves, and sick days") — https://www.personio.com/product/attendance-tracking/ , https://support.personio.de/hc/en-us/categories/200849035-Employee-Management
- Jibble — Time & Attendance product page (with category FAQ) and Help Center — https://www.jibble.io/time-and-attendance-software , https://www.jibble.io/help

> Sourcing limitations: enterprise HCM time-and-attendance documentation (UKG/Kronos, ADP, Workday) was not reachable from the research environment, consistent with prior research in this domain; enterprise-tier claims are kept general. Rippling's help center was unreachable (application-rendered portal) and was dropped from the sample. Evidence for the market-leading pure-play vendor is product-page level (official but marketing-adjacent), so its operational detail is kept general. Precise rule values, thresholds, and configuration menus seen in research are product-specific settings, not industry standards, and are not stated as such in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/regional sample check are recorded in the paired Research Notes.
