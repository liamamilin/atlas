# Construction Field Management

## Overview

A **Construction Field Management** application is the site-execution system of record for a construction project: the place where the people running the work on site — superintendents, foremen, field engineers, safety and quality staff, and subcontractor crews — record what happened on the project each day, raise and assign the issues and deficiencies that come out of the work, and carry those items through to verified completion.

Two structures define the Type:

```text
Project day record
└── a day-anchored record of site activity, kept by the field
    (work performed, labor and time, weather, equipment, deliveries, events)

Field work item
└── a deficiency / issue / task raised from the workface
    (location, responsible party, due date, evidence)
    tracked to verified completion
```

Everything else commonly associated with the category — plan viewing and markups, photo evidence, inspection checklists, safety observations, timesheets, notifications, offline mobile capture — is standard capability that mature products add around this core, not what makes the product field management. The pattern also predates software: a paper daily report book and a clipboard punch list satisfy the same defining structure, which is why the definition does not depend on any digital mechanism.

When the application stops recording the day's site work and field-raised items and centers instead on schedules, budgets, or contracts, it has drifted into Construction Project Management territory; when it keeps only one register (the log, the punch list, the RFIs, safety), it has become one of the focused Types described at the end of this document.

## Users & Context

The primary users work at the workface or direct it:

- **Superintendent / site manager (general contractor)** — owns the day: completes the daily log, walks the site raising deficiencies, verifies that trade work is complete, runs inspections.
- **Foreman / crew supervisor (subcontractor)** — records crew time, receives assigned punch items and tasks, reports completion from the field, keeps the crew's compliance and safety records current.
- **Field engineer / assistant PM** — logs conditions, creates and tracks issues, assembles reports for the office and the owner.
- **Safety and quality staff** — perform inspections from checklists, record incidents and unsafe-condition observations, track corrective items to closure.

Secondary users sit in the office or in other organizations:

- **Project manager / office staff** — consume field records for progress, claims protection, and closeout; configure templates and permissions.
- **Subcontractor collaborators** — scoped participants who view assigned items, respond, and submit log entries or completed work for approval.
- **Owner / architect / owner's representative** — typically readers and verifiers: they receive reports, walk the punch with the contractor, and verify completion of items.

The work environment is the jobsite: phones and tablets used while walking the work, hands dirty, connection unreliable. Mobile capture — turning a photo into an assigned item in one step, filling a form at the scaffold — is the dominant interaction; the web console is the companion surface for configuration, review, and reporting.

## Core Model

### The defining core

**The project day record.** Every day on a construction site produces a record of what happened, and this Type holds it. The record is anchored to a project and a date, is produced by field personnel (sometimes contributed by subcontractors and approved by the contractor), and answers, for any later reader: who was on site, what work was performed, what conditions affected the work, what arrived, and what went wrong. Mature products structure the day into domain sections — weather, manpower per company, equipment in use, deliveries, visitors, phone calls, delays, safety events, notes, and in some traditions production quantities — but the exact sections are configurable and vary; the day-anchored record itself is the constant. The record is cumulative and durable: it becomes the project's contemporaneous memory, used for progress questions, delay and claim support, and closeout.

**The field work item.** Walking the site produces things that need doing: a deficiency found during a walkthrough, a hazard, an incomplete installation, a coordination problem. The field work item is the object that carries one of these from discovery to done. It is always attributed — pinned to a location on the project (a building level, a room, or a position on a drawing), assigned to a responsible party (usually a subcontractor or trade), given a due date, categorized, and backed by evidence (photos, notes, drawings). It moves through a lifecycle: raised → assigned/notified → worked and responded to → completed by the responsible party → **verified by a second party** → closed. The verification step is the discipline that separates field management from a generic task list: the party doing the work and the party accepting it are different, and the item is not done until both have acted. Items keep a change history, support comments, and reassign when responsibility changes.

Together these two structures are the Type: the day record answers "what happened", the work item answers "what must change and who owns it". A product with only the day record is a daily log application; a product with only work-item registers is punch-list or task management; the field-management Type is the integration of both, in the hands of site personnel.

### The supporting cast

Mature products consistently add these capabilities around the core:

- **Locations and plans** — a location taxonomy for the project (building → level → area → room) and the current drawing set, so any record can be anchored to a place; deficiencies are commonly pinned onto plan sheets, and the plans are viewable and markable in the field.
- **Photo evidence** — photos attached to log entries, work items, and inspections, flowing into a project-wide photo library; in some products photos are the fastest way to create an item (capture → item in one step).
- **Inspections and checklists** — reusable checklist templates (sections and line items, sometimes with conditional logic) instantiated as scheduled or ad-hoc inspections of the work: quality hold points, safety walks, equipment checks, environmental requirements. An inspection is performed on site, may require photos, and is closed with signatures; failed items typically generate work items.
- **Safety records** — incidents, unsafe-condition observations, and violations recorded with the same attribution machinery as any field item; in many products safety walkthroughs are simply inspections run from safety checklists.
- **Time capture** — worker and crew timesheets entered from the field (by the worker or by a supervisor for a whole crew), feeding payroll and job costing.
- **Parties and permissions** — the general contractor, its subcontractors, the owner, and the designer participate with distinct scopes: subcontractors typically see and act on what is assigned or exposed to them, and submissions (log entries, completions) can require approval before becoming official.
- **Outward reporting** — the day record, punch list, and inspection results are exportable and emailable as formatted reports (PDF), often on a schedule, because the office, the owner, and the architect must be kept informed without touching the tool.

## How It Works

### The daily loop

```text
Start of day
→ site walk: record conditions, manpower, deliveries, events (day record)
→ issues found become work items (photo, location, assignee, due date)
→ responsible parties notified; work proceeds
→ crew time recorded (timesheets)
→ end of day: day record completed, submitted, or approved
→ report distributed to office / owner
```

The daily loop is the heartbeat of the Type: record what happened, direct what must change, close the day.

### The work-item loop

```text
Discovery (walkthrough, inspection, observation, photo)
→ create item with location + evidence + responsible party + due date
→ notification to assignee
→ assignee responds / completes work in the field
→ verifier (contractor, architect, owner's rep) inspects
→ verified and closed — or rejected and reworked
```

Statuses and labels vary by product, but the two-sided complete-then-verify discipline recurs across the sampled market. Overdue items surface through reminders, overdue notifications, and aging views; a punch walkthrough near project end is the same loop executed at volume, often against item templates.

### The inspection loop

```text
Pick template (quality / safety / environmental / equipment)
→ schedule or raise ad-hoc inspection for a location
→ perform on mobile: answer line items, add photos, note failures
→ sign / collect signatures
→ failed items become corrective work items
→ failed inspections may be reinspected after correction
```

### The time loop

```text
Crew works → worker clocks in/out or supervisor completes crew timesheet
→ time approved → flows to payroll / job costing
```

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Day record view

The project calendar/list of days. Typical information: date, status (open / submitted / complete), section summaries (weather, manpower, notable events). Primary actions: open a day, add entries to sections, copy from a previous day, mark the day complete, email/export the day's report.

### Work-item list and detail

The project's open items by status, location, assignee, or trade. Typical information: item number, title, location (often with a plan thumbnail or pin), assignee, due date, status, photos. Primary actions: create item (frequently from a photo or a tapped point on a plan), assign, comment, respond, mark complete, verify/accept and close, reassign, export.

### Plan viewer

The current drawing set, with markups and item pins. Typical information: sheet revisions, pinned items per location. Primary actions: view latest revision, mark up, pin an item to a spot, filter items by sheet. (The controlled drawing register behind this surface belongs to Construction Document Management.)

### Inspection runner

A checklist executed for one location and date. Typical information: template sections, per-item pass/fail/NA responses, required photos, signatures. Primary actions: perform items, raise items from failures, sign, close, reinspect.

### Timesheet surface

Crew time by day. Typical information: workers, hours, activities, cost codes. Primary actions: clock in/out, fill or approve crew time, submit for approval.

### Reports and dashboards

Formatted output of the records above — daily reports, punch logs with aging, inspection summaries — plus progress overviews for management.

## Important Rules / Behaviors

- **Completion is not closure.** A work item is closed only after a party other than the doer verifies the work. This two-sided rule is the behavioral signature of the Type.
- **The day record is contemporaneous and durable.** Entries are dated to the day they describe; back-entry for a previous day is possible in mature products, and edits are tracked in a change history. A completed day is typically marked complete rather than silently rewritten, and may be reopened deliberately. The record's value for progress questions, delay support, and disputes depends on this durability.
- **Attribution is mandatory-ish.** A field item without a location and a responsible party is considered incomplete; notifications, aging, and reporting all hang off those attributes.
- **Multi-party visibility is scoped.** Subcontractor collaborators see their own assignments and shared records; submissions from them may pend until approved; owner/designer access is commonly read-and-verify. Permission models are per-role and per-tool.
- **Inspections gate work.** A failed inspection item generates corrective work; a closed inspection that required correction is typically reinspected rather than edited.
- **Photos flow to one library.** Evidence attached in one surface (item, log entry, inspection) becomes part of the project photo record rather than being trapped per-record.
- **Mobile capture assumes imperfect connectivity.** Field records are designed to be created on site — often offline — and synchronized later.

## Variants

- **Field-first standalone** — the product is built around tasks pinned to plans, punch, and inspections; project-management functions (RFIs, submittals, budget) are present but secondary. Typical for mid-market general contractors and specialty contractors.
- **Suite-embedded field module** — field tools (daily log, punch, inspections, safety, timesheets) are one group in a construction platform that also owns financials, contracts, and the document register. Typical for enterprise contractors and owners.
- **Subcontractor field-operations platform** — the spine is crews, equipment, time, and compliance forms for self-perform trades (civil, concrete, crane, rail); the day record is time- and form-based rather than a structured weather/manpower diary.
- **Segment flavors** — building projects anchor everything to drawings and building locations; civil and heavy work anchors to jobs, crews, and equipment instead.
- **Day-record realization** — structured log object with fixed sections vs digitized paper forms vs timesheet-plus-photos.
- **Regional vocabulary** — the same deficiency walkthrough is called punch list (US), snag list (UK/AU), réserves (FR), Mängelliste (DE), opleverlijst (NL); the structure is identical.
- **Optional depth** — reality capture (360° photos, progress capture), QR/label linking of physical site objects to records, payroll and accounting integration, plan-gated module mixes.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Project Management | umbrella, adjacent | owns schedules, budgets, contracts, change; field management owns the day record and field work items — vendors sell both as one platform |
| Daily Log Application | subset | keeps only the day-anchored site record, without the integrated work-item/inspection machinery |
| Punch List Management | subset | keeps only the deficiency register and its completion workflow |
| RFI Management | subset, sibling register | keeps only the question-to-answer workflow; field management hosts it as one module |
| Submittal Management | subset, sibling register | keeps only the shop-drawing/approval workflow |
| Construction Quality Management | overlapping sibling | quality programs, NCRs, and audit depth; inspections inside field management are the operational checklist layer |
| Construction Safety Management | overlapping sibling | safety programs and compliance management; incident/observation capture appears in both |
| Construction Labor Management | adjacent resource view | centers the workforce population; field management centers the day's work the workforce performs |
| Construction Equipment Management | adjacent resource view | centers the machine population; equipment entries in a field day record are the seam |
| Construction Reality Capture Platform | adjacent | capture-first progress documentation; photos inside field records are evidence, not the object |
| Construction Document Management | adjacent | owns the controlled drawing/document register that the field viewer consumes |
| Property Inspection Application | different industry phase | inspects occupied/completed buildings, not work in progress on a construction project |

The load-bearing boundary is with Construction Project Management: the same vendors sell both, but the objects differ. If the day record and field work items are removed and schedules, cost, and contracts remain, the product is project management, not field management.

## Representative Products

- Procore — enterprise construction platform; field tools (Daily Log, Punch List, Inspections, Timesheets, Incidents, Observations) beside financial and project-management tools
- Fieldwire by Hilti — field-first standalone; tasks, plans, punch, inspections, forms; explicitly markets field management separately from project management
- Assignar — subcontractor field-operations platform; crews, equipment, time, and compliance forms

## Sources

Research date: **2026-09-07**

- Fieldwire by Hilti — product site: https://www.fieldwire.com/ ; punch list: https://www.fieldwire.com/punch-list-app/ ; help center: https://help.fieldwire.com/hc/en-us ; task model article: https://help.fieldwire.com/hc/en-us/articles/360003458332-Introduction-to-Tasks
- Procore — support home and tool grid: https://support.procore.com/ ; Daily Log guide: https://support.procore.com/products/online/user-guide/project-level/daily-log ; Punch List guide: https://support.procore.com/products/online/user-guide/project-level/punch-list ; Inspections guide: https://support.procore.com/products/online/user-guide/project-level/inspections
- Assignar — product site: https://www.assignar.com/

> Sourcing limitation: Autodesk Construction Cloud, Raken, and NoteVault were not reachable from the research environment during this pass and are not cited as evidence; the suite-embedded pole therefore rests primarily on one directly documented product, and claims about the daily-report-led small-business pole are stated at reduced strength. Vendor-specific limits and defaults are intentionally omitted from this document and retained in the paired Research Notes.
