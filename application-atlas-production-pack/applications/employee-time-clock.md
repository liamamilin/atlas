# Employee Time Clock

## Overview

An **Employee Time Clock** is the application employees use to record when their work starts and stops. Employees "punch" in and out — on a shared terminal or kiosk at the workplace, or from their own phone or computer — and the system accumulates those timestamped events into a per-employee timesheet for each pay period. Supervisors review, correct, and approve the timesheets, and the approved hours are handed off to payroll.

The defining structure is small:

```text
Identified employee
└── Work-time boundary events (clock in / break / clock out) recorded at a clocking surface
    └── Accumulation into a per-employee, per-pay-period timesheet
        └── Organizational review & approval
            └── Handoff to payroll / attendance processing
```

Everything else commonly associated with modern time clocks — GPS and geofencing, facial recognition, rounding rules, overtime engines, schedule enforcement, tips, job costing — is widespread in current products but is implementation depth, not the defining core. A mechanical punch clock with paper timecards satisfies the same structure: identified worker, in/out punches, a timecard per pay period, and payroll use.

When the primary surface shifts to self-logged, task-attributed time for billing or productivity analysis, the product is drifting toward a different Application Type (Time Tracking Application). When scheduling, absence, and labor-rule compliance become the primary objects, it becomes a Time & Attendance or Workforce Management system, of which the time clock is one layer.

## Users & Context

Primary users:

- **Hourly employee**: punches in and out for shifts, records breaks, sees their own accumulated hours.
- **Supervisor / shift manager**: monitors who is on the clock, handles missed punches and lateness, reviews and approves timesheets; in some products may clock employees in or out on their behalf.

Secondary users:

- **Administrator**: configures employees, clocking surfaces, and the rules that govern punching and pay (windows, locations, rounding, breaks, overtime).
- **Payroll processor**: consumes the closed, approved hours at the end of each pay period.

The typical context is shift-based, hourly work: retail, restaurants, healthcare, manufacturing, warehouses, call centers, and field services. The clocking surface is usually a shared device placed at a workplace entrance or break room, while field and remote workers punch from their own mobile phones. Office salaried staff, where included, typically appear only as exceptions (duration entry rather than punches).

## Core Model

### The Defining Core

```text
Identified employee
└── Punch (work-time boundary event)
    └── Timesheet (per employee, per pay period)
        └── Approval under organizational authority
            └── Payroll / attendance handoff
```

Four properties. If any one is removed, the product is no longer recognizable as an employee time clock:

- **Identified employee** — every punch belongs to a specific, identified member of the organization. Without this, the product is an anonymous timer.
- **Punch** — a timestamped boundary event (clock in, break start/end, clock out) recorded at a clocking surface by the employee or by an authorized manager on their behalf. Without punches, there is no recorded work time.
- **Timesheet** — the accumulated, per-employee record of punches and computed hours for a pay period. It is the organization's authoritative record of worked time, not a personal log.
- **Organizational oversight and downstream use** — the timesheet is reviewed and approved under manager authority and exists to feed payroll and attendance processing. Without this, the product is a personal time tracker.

### Standard Capabilities

A typical modern time clock carries most of these capabilities. They are not what makes the product a time clock, but they make it practical at workplace scale.

- **Clocking surfaces** — a shared terminal or kiosk (a dedicated computer or tablet at the workplace, identified by employee ID, PIN, badge, QR code, or face) and/or a personal mobile or web app. Many products offer both.
- **Schedule anchoring** — punches are compared against the employee's scheduled shift: clock-in may be restricted to the shift start or a defined window around it, blocked entirely when the employee is not scheduled, and flagged as late or absent when it deviates.
- **Location enforcement** — punches may be restricted to a physical address, an IP address, or a geofenced area; mobile punches may capture GPS location as evidence.
- **Break tracking** — paid and unpaid breaks recorded between clock in and clock out, sometimes with employee attestation at clock-out and automatic deduction of unpaid breaks.
- **Rounding** — punch timestamps adjusted to configured intervals (up, down, or nearest) for payroll consistency, with the actual time preserved alongside the rounded time.
- **Overtime rules** — hours beyond configured daily or weekly thresholds (and rest-day or holiday classes) identified automatically, often with multiplier rates and alerts as employees approach overtime.
- **Exception machinery** — missed clock-out, late arrival, wrong location, forgotten clock-in: surfaced as notices or alerts, with mitigations such as punch reminders and automatic clock-out at shift end.
- **Approval workflow** — timesheets move from pending to approved under manager review; edits are made before approval, and approved timesheets must be explicitly reopened (unapproved) to change.
- **On-behalf correction** — managers can add or edit timesheets for employees who forgot to punch, typically with the change attributed and audited.
- **Audit trail** — a history of who created or changed each entry, when, and how; punch-location evidence where location capture is enabled.
- **Payroll handoff** — closing the pay period and exporting hours (files, formats, or integrations) to a payroll processor.
- **Identity verification at the surface** — PIN, photo capture, facial recognition, or badge/QR to reduce "buddy punching" (one employee punching for another).

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:   Clocking surface
Implementations:  shared kiosk/terminal (tablet app, browser), personal mobile app,
                  web app, desktop app, hardware badge terminal

Concept:   Employee identity at the surface
Implementations:  employee ID, email, PIN, badge/RFID/NFC, QR code, photo, facial recognition

Concept:   Location enforcement
Implementations:  fixed workplace address, IP/network restriction, GPS geofence, kiosk presence

Concept:   Payroll handoff
Implementations:  export file (CSV/Excel), provider-formatted report, direct integration,
                  built-in payroll service
```

A reader who has only seen one implementation (e.g., a phone app with GPS) should still be able to recognize a factory badge terminal or a browser kiosk as the same Type.

## How It Works

### Configure (administrator, once per workplace)

```text
Add employees (with clock credentials: ID, PIN, badge, face enrollment)
→ set up clocking surfaces (shared terminal/kiosk and/or personal apps)
→ configure rules: clock-in windows, location restrictions, breaks,
   rounding, overtime thresholds, tips, job attribution
→ connect or prepare the payroll destination
```

### The punch loop (employee, every shift)

```text
Identify at the surface (ID / PIN / badge / QR / face)
→ clock in (subject to window and location checks; select position or job if prompted)
→ take breaks (clock break start/end, if break tracking is enabled)
→ clock out (confirm breaks taken if attestation is enabled; report tips if applicable)
```

Each event is stored as a timestamp against the employee and, where configured, against a position, job, or location. If the employee punches too early, from the wrong place, or while not scheduled, the punch may be blocked or flagged. If the employee forgets to punch out, the system flags the exception — some products remind the employee or automatically clock them out at shift end.

### Exceptions and corrections (supervisor, continuously)

```text
Exception appears (late in / missed out / wrong location / absent)
→ supervisor investigates (history, punch map, employee message)
→ corrects: edit the timesheet, or add one on the employee's behalf
→ change is attributed and recorded in the audit trail
```

In some products, a scheduled employee who never punched in appears as an absent record pre-filled from the schedule; the supervisor can then approve it (if the shift was actually worked), convert it to leave, discard it, or ask the employee about it.

### Approve and hand off (manager → payroll, every pay period)

```text
Pay period ends
→ manager reviews pending timesheets (individually or in bulk)
→ edits where needed, then approves
→ closes the pay period (further changes blocked unless reopened)
→ exports approved hours to payroll (file, report, or integration)
```

Approval is the gate between "recorded time" and "payable time". After closure, the record is effectively frozen; corrections require reopening the period, and some products recalculate rule-derived values (rounding, overtime) when a closed timesheet is reopened.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Clocking surface (shared terminal / kiosk)

The workplace device used solely for clocking in and out.

- shows the current time and, often, the employee's upcoming shift
- primary actions: identify (ID/PIN/badge/QR/face), clock in, start/end break, clock out
- may prompt for position, job site, notes, tips, or break confirmation
- may capture a photo or verify identity biometrically

### Personal punch app (mobile / web)

The employee's own device, used where mobile or remote punching is allowed.

- shows schedule and current punch state
- primary actions: clock in/out, take break, view own hours
- may enforce location (GPS/geofence) and capture location evidence

### Timesheet review & approval console (manager, web)

The manager's primary working surface.

- lists timesheets by pay period, employee, and location, grouped by status (pending / approved / absent / paid)
- typical information: punch times, computed hours, breaks, overtime, exceptions, notes, comments
- primary actions: review detail, edit entries, add timesheet on behalf, approve (single or bulk), unapprove, view change history, export

### Employee self-service timesheet

- shows the employee's own hours for the pay period
- primary actions: view hours; edit own entries only where the employer allows it and only while the period is open

### Attendance / exception dashboard

- surfaces who is currently on the clock, late arrivals, missed punches, absences, and wrong-location events, usually for a recent window
- primary actions: investigate, message employee, jump to the affected timesheet

### Rule configuration (admin)

- clock-in windows, location/IP restrictions, break policies, rounding rules, overtime thresholds and rates, tips, job/position attribution, approval and auto-approval settings, payroll export setup

## Important Rules / Behaviors

### Punches are gated, not just recorded

Clocking is frequently conditional: an employee may be unable to punch in too early, from the wrong location, or while not scheduled. The time clock is therefore both a recording device and an enforcement point for workplace policy.

### Approval is the gate to payroll

Unapproved timesheets are working records; approved timesheets are payable records. Editing is normally allowed only before approval; after approval, a timesheet must be explicitly unapproved (and, in some products, un-marked as paid) before it can change. Pay periods can be closed, freezing all records until reopened by a manager.

### The actual time is preserved

When rounding is applied, products keep the actual punch time alongside the rounded time, and rounding applies to timestamps rather than to computed durations. Approved timesheets are generally not silently recalculated; recalculation happens on explicit reopen, under rules the administrator controls.

### Rules are computed on the timesheet, not at the punch

Overtime classification, break deductions, and rounding are applied when the timesheet is assembled and recalculated as entries change. This is why approval is recommended in chronological order in some products: approving later entries can change overtime computed on earlier ones in the same week.

### Every correction is attributed

Timesheet edits, on-behalf punches, and approvals are recorded in a history (who, when, how); in some products, manager comments on a timesheet are hidden from the employee. The audit trail exists because the timesheet is a payroll-legal record, not a scratchpad.

### The schedule is the reference point

Where scheduling is present, the punch is judged against the plan: late, early, absent, or unscheduled punches are named exceptions. The timesheet records actuals; the schedule remains the plan.

## Variants

- **Kiosk-centric (on-site hourly work)** — shared tablet/browser terminal at the workplace with PIN, badge, QR, or face identification; retail, restaurants, healthcare, manufacturing.
- **Mobile GPS-centric (field work)** — personal-phone punching with GPS capture, geofencing, and job attribution; construction, landscaping, logistics, cleaning services.
- **Scheduling-led suites** — the time clock is a module attached to an employee scheduling product; punches are tightly coupled to published shifts (window enforcement, absent detection).
- **Tracker-led freemium products** — a time-tracking product that also serves as a time clock; attendance features (kiosk, geofence, overtime) layered on a timesheet engine.
- **Suite / HCM module** — the time clock as the recording layer of a broader Time & Attendance or workforce management system, alongside absence, accruals, and labor compliance; large employers often pair it with dedicated hardware terminals.
- **Payroll-bundled** — the time clock and payroll in one product, removing the export boundary.

A variant remains a variant unless it changes the defining core; for example, a product whose primary truth is self-logged task time for client billing has become a Time Tracking Application, not a variant of the time clock.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Time & Attendance System | parent/system level | adds schedule compliance, absence and accrual management, and labor-rule administration as primary objects; the time clock is its punch-recording and timesheet layer |
| Time Tracking Application | adjacent, easily confused | time is self-logged, task/project-attributed, and voluntary, serving billing and productivity analysis rather than organizational attendance and payroll |
| Payroll System | downstream | computes wages, taxes, and payslips from approved time; the time clock produces the approved time and does not compute pay |
| Employee Scheduling Platform | plan-side sibling | owns the planned shift; the time clock records actuals and is judged against the plan; scheduling products often bundle a time clock |
| Workforce Management Platform | broader suite | combines scheduling, time & attendance, forecasting, and engagement; the time clock is one capability inside it |
| Leave & Absence Management | adjacent | manages time away from work (requests, balances, accruals); a time clock may carry leave timesheets as records but does not own leave policy |

The most important boundary is with Time & Attendance: the two are nested, not competing. If a product's whole world is punches and timesheets, it is a time clock; if punches are one input to a larger attendance-compliance system, the system is the Time & Attendance type.

## Representative Products

- When I Work — scheduling-led SMB suite with a Time Clock & Attendance module
- Jibble — freemium time tracking / attendance product with kiosk, geofencing, and rule engines
- Deputy — mid-market workforce management with dedicated kiosk/time-clock apps and a mature timesheet approval workflow
- Buddy Punch — SMB time-clock-first product for US hourly workforces (kiosk, GPS, anti-buddy-punching features)

Other well-known market examples include QuickBooks Time and Homebase (SMB), and the time-and-attendance modules of enterprise HCM suites; these were not directly researched for this document (see Sources).

## Sources

Research date: **2026-09-06**

Primary official documentation:

- When I Work Help Center — "Time Clock & Attendance" category; "Clocking In and Out"; "Working with Timesheets" category — https://help.wheniwork.com/
- Jibble Help Center — "How time rounding works"; "How does overtime work?" — https://www.jibble.io/help
- Deputy Help Center — "Deputy Kiosk and Time Clock" category; "What are the Deputy Kiosk/Time Clock apps?"; "Timesheets" category; "Adding, editing and approving Timesheets" — https://help.deputy.com/
- Buddy Punch — official product and feature pages — https://buddypunch.com/

> Sourcing limitation: enterprise HCM time-and-attendance documentation (Workday, UKG/Kronos, ADP) was not reachable from the research environment (gated or script-rendered portals), and Homebase / QuickBooks Time fetches failed. Claims about the enterprise tier and about specific hardware terminals are therefore kept general. Precise configuration values quoted in research (clock-in window options, rounding intervals, overtime thresholds) are product-specific settings, not industry standards, and are not stated as such in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical-sample check are recorded in the paired Research Notes.
