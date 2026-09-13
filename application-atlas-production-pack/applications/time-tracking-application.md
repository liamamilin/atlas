# Time Tracking Application

## Overview

A **Time Tracking Application** is the record-keeper of time spent on work: it captures how long work took as individual, persistent time entries, attributes each entry to a piece of work structure — a project, task, client, or matter — and turns the accumulated record into timesheets, reports, and billable hours.

The defining core is small:

```text
Time entry (a persistent, addressable record of a duration)
└── attributed to a work structure (project / task / client / matter)
    └── formed by a user act (timer, manual input, timesheet cell, or confirmed suggestion)
```

Everything else commonly associated with the category — billable rates, invoicing, approval workflows, budgets, automatic background capture, calendar integration, capacity planning — is widespread in current products but is not what makes a product a time tracker. A paper timesheet — a professional writing durations against client matters and totaling them for billing — satisfies the core with no software at all.

When the record stops being formed by the user's hand and instead accumulates automatically as usage observation, the product is drifting toward a different Application Type (Productivity Activity Tracker). When the record's unit of truth becomes attendance hours for payroll rather than task time for billing and analysis, it drifts toward the Employee Time Clock / Time & Attendance family.

## Users & Context

The primary user is anyone who needs to account for their working time against the work it belonged to:

- **Freelancers and solo professionals** track time per client and project so they can bill accurately and see what is profitable.
- **Members of billable teams** (agencies, consultancies, law firms, design and software teams) log their hours against shared projects; the record feeds client invoices, project budgets, and internal visibility.
- **Individuals tracking for themselves** use the same entries for self-awareness — where the day actually went — without any billing downstream.

Secondary roles appear once a team is involved:

- **Managers/approvers** review submitted timesheets, request changes, and approve periods so downstream numbers are stable.
- **Administrators** set up the work structure (clients, projects, tasks), rates, permissions, and — where offered — approval schedules and lock rules.

The work context is the working day itself: time is captured as work happens (a running timer) or reconstructed shortly after (manual entry, a timesheet grid filled at day's or week's end). Desktop apps, mobile apps, browser extensions, and the web app are peer surfaces over the same record.

## Core Model

### The Defining Core

Three properties, held together. Remove any one and the product stops being recognizable as a time tracker:

- **The time entry as the unit of record.** A persistent, individually addressable record of a duration of time — carrying its date, its recorder, and typically a short description. The entry survives sessions and accumulates into the user's (or team's) history. Without it there is only a stopwatch with no memory.
- **Attribution to a work structure.** Each entry is attributed to a target in a user-maintained work hierarchy — most commonly project, with task and client as finer and coarser grains. This is what the record is *about*: work performed, not applications used, and not attendance kept. The hierarchy's depth and how strictly it is enforced vary by product (some require the full client→project→task chain, some require only a project, some leave attribution optional in the quick-timer surface) — but the existence of a user-chosen work-structure target is constant.
- **User-driven formation of the record.** The entry comes into being through a user act: starting and stopping a timer, typing a duration or start/end times, filling a cell in a timesheet grid, or confirming a suggestion produced by automatic capture. The record is declarative — the user says what the time was for. Where records form without the user's hand, the product has crossed into ambient usage observation.

### Capabilities Mature Products Commonly Add

These make the record useful; they are not what makes the product a time tracker.

- **Timesheet views** — day and week grids over the entry population, with totals per day, per week, and per attribution group.
- **Reports and analysis** — filter, group, and break down time by project, client, task, team member, and date range; detailed (entry-level) and summary forms; export to spreadsheets and accounting tools.
- **Billable semantics** — a billable/non-billable flag on entries and configurable billable rates (set per project, per person, or per task), with cost rates alongside in team products.
- **Budgets and estimates** — project budgets in hours or fees, estimated-vs-actual comparisons, and profitability/utilization reporting built on the same entries.
- **Capture aids** — reminders to track and to submit, idle detection, favorite and recent entries, resume/continue, copy last week's structure.
- **Multi-surface clients** — web, desktop (timer plus capture aids), mobile, and browser extension, synchronized.
- **Team layer** — a workspace with members, roles and permissions, per-person rates, and project assignment.
- **Integrations** — timers embedded in project-management and issue tools via extensions, calendar connections, and exports into invoicing and accounting.
- **Expenses** — cost entries alongside time entries in the billing-oriented segment.

### One Structure, Many Implementations

The core is written conceptually; realizations vary:

```text
Concept:   Attribution target
Realized as:  client → project → task hierarchies of differing depth and strictness;
              matter/job labels in professional-services flavors

Concept:   User-driven capture
Realized as:  running timer, manual duration or start/end entry,
              timesheet-grid cell entry, calendar-block entry,
              confirmation of automatically captured suggestions

Concept:   The record's destination
Realized as:  client invoices, payroll handoff, project budgets,
              internal productivity analysis, personal self-awareness
```

## How It Works

### Capture: forming entries

```text
Start a timer (with description + attribution target) and stop it when done
— or —
Enter time after the fact (duration, or start and end times)
— or —
Fill a cell in the day/week timesheet grid
— or —
Confirm a suggestion produced by automatic background capture
→ a time entry exists, attributed and dated
```

Timer and manual entry are both first-class in mature products; forgetting to start the timer is an expected event, so manual reconstruction is a supported path, not an apology. Where a product captures activity automatically in the background, the captured material is presented as suggestions or raw blocks that the user reviews and converts into entries — the entry still owes its existence to the user's confirmation.

### Attribute: the work structure

Entries are made against the work hierarchy the account maintains: clients group projects, projects carry tasks, rates, and budgets. Changing structure is an administrative act; entries keep their attribution once made (products differ on whether an entry's attribution can be edited inline or must be deleted and re-created).

### Accumulate: the timesheet and its discipline

```text
Entries accumulate through the period (day/week)
→ the timesheet view totals them per day, per attribution group
→ (team tier) the member submits the timesheet
→ an approver reviews against expected hours
   → approve  → the period locks
   → request changes / send back → the member edits and resubmits
→ locked periods keep billing, payroll, and reporting numbers stable
```

Submission and approval are an **optional organizational discipline**, not part of the core: products gate it behind plans or modules, and a person tracking time only for themselves has no submission step at all. Where it exists, its purpose is stated plainly by vendors: catching missing or misattributed time before it becomes an invoice, and freezing the numbers that payroll and clients depend on.

### Consume: reports and money

```text
Entry population
→ filter/group by project, client, task, person, date
→ timesheet and summary reports
→ billable hours × rates
→ invoices (built in, or exported to invoicing/accounting tools)
→ payroll handoff (in workforce-oriented use)
```

The same record serves non-money destinations too: project budgets and estimated-vs-actual comparisons, utilization views, and personal self-awareness.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Timer / time-tracker surface

The daily driver. A description field ("what are you working on?"), an attribution picker, a start/stop control, and the list of recent entries with resume actions. Primary actions: start/stop timer, switch to manual mode, continue a previous entry, edit the running entry's start time.

### Timesheet (day/week grid)

The period surface. Rows are tasks or project/task combinations, columns are days; cells hold durations. Grouping by client or project with group totals is common. Primary actions: enter/edit durations, expand a row to see its entries, copy last week, submit for approval (where enabled).

### Calendar view

A timeline of the day onto which entries are placed as blocks — clicked into empty slots or dragged and resized. Useful for reconstructing a day visually.

### Reports

The analysis surface over the entry population: dimension pickers (project, client, task, member), date ranges, detailed and summary modes, charts, and export. Approval-status views (unsubmitted / submitted / approved) live nearby in team products.

### Approvals surface (team tier)

The reviewer's queue: submitted timesheets with logged hours against expected hours, approve / request-changes / decline actions, and the locked-period list.

### Project / client / task administration

Where the work hierarchy is maintained: create and archive projects, set project type and billable method, define tasks, assign people, set rates and budgets.

### Settings

Capture preferences (duration vs start/end display, decimal vs clock format), rounding rules, required fields, reminders, integrations.

## Important Rules / Behaviors

### The entry is declarative and user-owned

An entry exists because a user formed it. Automatic capture, where present, only proposes — its output becomes an entry through user confirmation, and in some products the unconfirmed material stays private to the user, never visible to administrators.

### Attribution strictness is a product choice, not a law

Some products require the full client→project→task chain on every entry; others require only a project; the quick-timer surface of some products allows entries with no attribution at all. The work-structure target is the center; how hard it is enforced varies.

### Submitted and approved periods lock

Once a timesheet is submitted it becomes read-only to its author; once approved, the whole period locks (including days with no time). Only administrators — or roles with approval permission — can edit locked entries, usually with an explicit warning, and approval can be withdrawn to reopen a period. This locking is what makes the record trustworthy enough to invoice and pay against.

### Approval is optional and organizational

Products are explicit that a personal tracker needs no approval workflow. It exists for the cases where someone downstream depends on the numbers — client billing, payroll, audits.

### The record fences off surveillance

Mainstream time trackers keep the record at the granularity of work attribution. Capturing screenshots, keystrokes, or content crosses into employee monitoring, and leading products either refuse it outright or fence it into a separate module. The presence of deep surveillance capture is a reliable sign that a product has left this Type.

### Money semantics ride on the entry, not inside it

The billable flag and rate resolution turn entries into invoice lines; the entry itself stays a neutral duration record. Non-billable and internal work is tracked through the same entries with the flag unset or the project marked non-billable.

## Variants

- **Solo billing tracker** — freelancer-oriented: timer, clients and projects, billable rates, invoice generation from entries.
- **Team timesheet tracker** — workspace with members, roles, submission/approval discipline, locking, utilization and profitability reporting.
- **Automatic-capture tracker** — background observation of computer work feeding suggestion-based entry formation; privacy posture (local storage, private-by-default) is part of the pitch.
- **Embedded tracker** — lives inside project-management/issue tools via extensions and integrations; the tracker's own surface is thin, the record is shared.
- **Workforce-flavored tracker** — adds kiosk clock-in, GPS, breaks, time off, and scheduling; drifts toward the time-clock/T&A family while keeping task attribution at the center.
- **Industry flavors** — law firms (time increments suited to legal billing, matter attribution), agencies (retainers, estimates, profitability), consultants and accountants (client reporting). These change the vocabulary and the billing rules, not the core.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Productivity Activity Tracker | records form automatically from ambient usage observation and serve productivity interpretation; here records are user-formed and attributed to work structures. Market products blur the two deliberately — usually by bundling both faces under one roof — but the seam (who forms the record, what it is about) holds. |
| Employee Time Clock | records identified employees' in/out punches assembled into approved payable hours; the unit of truth is attendance, not task time. Some trackers add kiosk clock-in as a surface — bundling, not identity. |
| Time & Attendance System | organization-side workforce-time system (attendance state, time policies, absence); task-attributed self-logged time is not its center. |
| Focus Timer | times deliberate, bounded attention sessions for motivation; its records are a motivational byproduct, not a billing-grade ledger. A Pomodoro mode inside a tracker is a borrowed capability. |
| Time Blocking Application | plans future time (work→time allocation); the tracker records past time. Planning products bundle tracking stats as furniture. |
| Professional Services Automation (PSA) | binds recorded hours into the full resource-billing loop — rate cards, approval gates, invoice generation, utilization and margin economics. Time tracking is the hours-capture component of that loop, not the loop itself. |
| Invoicing Application | turns billed items into invoices and payments; the tracker produces the hours that feed it. Built-in invoicing in a tracker is a downstream convenience. |
| Task Mining Platform | derives task structure and work patterns from observed system interaction; the tracker holds user-declared time. Declared vs derived is the seam. |
| Project Management Application | plans and coordinates work (tasks, schedules, boards); the tracker records the time the work took. Trackers integrate into PM tools rather than replacing them. |
| Employee Monitoring Software | serves organizational oversight with capture depth (screenshots, keystrokes, content) beyond work attribution; crossing that depth leaves this Type. |

## Representative Products

- **Toggl Track** — timer-first independent benchmark spanning freelancers to enterprises; explicit no-surveillance stance; timesheet approvals and billable machinery at team tiers.
- **Harvest** — professional-services lineage: timer + timesheets + invoicing + budgets; the client→project→task chain stated as the product's spine.
- **Clockify** — freemium team pole; the widest capture-surface set (timer, manual, timesheet, calendar, kiosk, auto tracker) and the clearest example of neighboring capabilities bundled beside the tracking core.
- **RescueTime (Timesheets)** — the vendor-drawn seam made visible: one app carrying a productivity-activity face (Focus) and a time-tracking face (Timesheets) with automatic, suggestion-reviewed project/client/task logging.

The definition was checked against the paper-timesheet lineage (no software) to avoid over-fitting to the modern timer-and-cloud pattern.

## Sources

Research date: **2026-09-09**

- Toggl — product page https://toggl.com/track/ ; Toggl 2.0 Knowledge Base https://docs.toggl.com/ (incl. Using the Timesheet view, Timesheet Approvals, Features index)
- Harvest — product page https://www.getharvest.com/ ; Help Center https://support.getharvest.com/hc/en-us (incl. Quick start guide, Understanding the three project types, Submitting and approving timesheets)
- Clockify — Help Center https://clockify.me/help/ (incl. Track time & expenses, Track time, Auto tracker)
- RescueTime — product page https://www.rescuetime.com/

> Sourcing limitation: Timely (timely.app / memory.ai), intended as the strongest automatic-capture sample, was unreachable this pass (empty response; 404) and was dropped after two attempts. The automatic-capture pole is therefore evidenced by Clockify's Auto tracker (help-center level) and RescueTime's Timesheets (product-page level); claims about how the most automatic products form entries are calibrated accordingly and kept at "suggestion/confirmation" strength rather than asserting exact mechanics.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical market-sample check are recorded in the paired Research Notes.
