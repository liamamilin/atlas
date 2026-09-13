# Daily Log Application

## Overview

A **Daily Log Application** is a construction project's day-record system: it lets the people running the work on site record, day by day, what happened on the project — who worked, what was done, what conditions affected the work, what arrived, and what went wrong — and turns each day's record into a distributable report for the project's parties.

The defining structure is small:

```text
Project day record
└── a dated, per-day record of one project's site activity,
    composed of attributed entries,
    accumulated as a chronological series over the project's life
    └── written by the people running the work,
        as the project's contemporaneous account for its parties
```

Everything commonly associated with modern daily-log products — automatic weather capture, signatures, PDF distribution, time cards, photos, reminders — is standard capability built around this core, not what makes the product a daily log. The pattern predates software: the superintendent's paper daily report book and the site diary satisfy the same structure, which is why the definition does not depend on any digital mechanism.

When the application adds field work items (deficiencies, issues, tasks) tracked to verified completion, it has drifted into Construction Field Management; when it centers schedules, budgets, or contracts, it has drifted into Construction Project Management.

## Users & Context

The primary users work on or direct the site work:

- **Superintendent / site manager (general contractor)** — owns the day: completes the daily log, records conditions and events, closes and distributes the day's report.
- **Foreman / crew supervisor** — records what the crew did, crew time in some products, and the conditions that affected production; in several products work is logged per company so subcontractor activity is visible to the general contractor.
- **Field engineer / assistant project manager** — logs conditions, back-fills entries, assembles reports for the office and owner.

Secondary participants sit around the record rather than in it:

- **Project manager / office staff** — read the log for progress and cost context, configure sections and recipients, monitor that reports are being filed.
- **Subcontractor collaborators** — in some products submit their own log entries, which pend until the contractor approves them.
- **Owner / owner's representative / inspectors** — receive the daily report as evidence of progress and conditions; in some products owners keep their own daily logs on the same machinery.

The work environment is the jobsite: phones and tablets used while walking the work, connection unreliable, entries made in minutes between tasks. Mobile capture is the dominant interaction; the web console is the companion surface for review, configuration, and distribution.

## Core Model

### The defining core

**The project day record.** Every day on a construction site produces an account of what happened, and this Type holds it. The record is anchored to a project and a date, is composed of individual entries — each attributed to an author, a time, and commonly a company and a location — and accumulates as a chronological series across the project's duration. Together the days become the project's contemporaneous memory: the place to answer later questions about who was on site, what work was performed, what the weather did, what arrived, what was delayed, and why production moved the way it did. That memory is relied upon for progress questions, delay and claim support, and project closeout, which is why entries are dated, attributed, and tracked through edits rather than silently rewritten.

**Site-work authorship with an accountability purpose.** The record is written by the people running the work — superintendents, foremen, field engineers, crews — not by office staff, and it is written for others: the office, the owner, inspectors, and the parties who may one day dispute what happened. This is what separates a daily log from a personal journal (no project, no parties) and from an office progress report (not field-made, not contemporaneous).

### What a day holds

The content of a day is broadly stable while the vocabulary is configurable and varies by product:

- **Work performed** — work logs describing the day's activities, in several products organized by company so headcount and activity per subcontractor are visible.
- **Labor** — manpower on site; in some products this is the time-card section itself.
- **Conditions** — weather (automatic capture from a weather service or the project address in modern products; manual entries otherwise), working conditions notes.
- **Materials and equipment** — deliveries received, equipment in use, in some traditions production quantities installed.
- **Events** — delays, visitors, phone calls, safety events, accidents, notable incidents.
- **Notes** — free-text observations, often with photos and files attached.

### Standard capabilities around the core

Mature products consistently add:

- **A day lifecycle** — the day's log is open while work happens, then closed by a deliberate completion act (a signature or a mark-complete); completed days can be re-opened or unsigned, prior days can be back-entered, and change history tracks edits.
- **Reporting outward** — the day record renders as a formatted report (PDF) that is emailed or automatically distributed to configured recipients when the day is completed.
- **Report-compliance machinery** — daily reminders and missed-report identification in daily-report-led products, and approval queues for collaborator-submitted entries in multi-party products.
- **Photo and attachment evidence** — attached to entries and flowing into a project-wide photo store.
- **Day navigation** — calendar and list views, date-range browsing, search and filters, copy-previous-day.
- **Role-scoped participation** — field authors, collaborators who submit pending approval, readers and recipients.

### One structure, several realizations

The same day record is realized differently across the market, and none of the realizations is the definition:

```text
Concept:    The project day record
Realizations:
  - a structured log tool with typed entry sections
    (one entry type per domain: manpower, delivery, weather, …)
  - a daily report with toggleable sections filled on mobile
  - a field diary joined to the day's time card, with tags and notes
  - a configurable form ("Daily Site Log") whose filled instances
    become dated records and render as report documents
```

A reader who has only seen one realization should be able to recognize the others from the core structure.

## How It Works

### The daily loop

```text
During the day (from the site, often offline)
→ record entries as things happen: work done, manpower per company,
  deliveries, conditions, events, delays
→ weather lands in the record (automatically or by entry)
→ end of day: review, preview the report
→ complete the day (sign or mark complete)
→ report is distributed to the office, the owner, and other recipients
```

This loop repeats every working day and the results accumulate — the series of days is the product's output as much as any single report.

### Completing and correcting a day

A day is not finished until someone deliberately closes it. Products differ in the mechanics — some use a signature, some a mark-complete state — and in how strictly the closure holds: some allow continued editing after signing (with an explicit un-sign), others keep a change history over mark-complete/re-open cycles. Back-entry is supported: a previous day can be opened and its entries added or corrected, and one product's calendar deliberately allows only past dates. When no work occurred, at least one product records a "no work done" day so the series stays unbroken.

### Multi-party recording

Where subcontractors participate, they typically submit entries that pend until the contractor approves or rejects them; work-log entries are organized per company so the general contractor can see each trade's headcount and activity. Reports themselves can be assigned to a responsible person who is notified on submission.

### Distribution

The completed day renders as a branded PDF report and reaches its audience by email — sent manually from the log, or automatically to a configured recipient list the moment the day is completed. Owner-facing variants add a sign-off step (inspector or owner representative signs the daily field report).

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Day view / log calendar

The project's series of days.

- Purpose: navigate to a day and see its state at a glance.
- Typical information: date, completion state, section summaries (weather, headcount, notable entries).
- Primary actions: open a day, add entries, copy from a previous day, mark the day complete or re-open it, email or export the day's report.

### Entry forms / log sections

The editing surface for one day's content.

- Purpose: capture the day's activity in structured sections.
- Typical information: section-specific fields (people and hours, quantities, weather values, delay reasons), free-text descriptions, photos and files.
- Primary actions: add/edit/delete an entry, attach evidence, submit an entry for approval (collaborators), approve or reject pending entries (contractor).

### Report preview and distribution

- Purpose: review the day as the recipients will see it, then send it.
- Typical information: the assembled PDF report — sections, photos, weather, signature block.
- Primary actions: preview, sign or sign off, distribute to recipients, download.

### Report-compliance surface

- Purpose: keep the one-record-per-day cadence honest.
- Typical information: which days have no completed report, reminder schedules, pending collaborator entries awaiting approval.
- Primary actions: set reminders, find missed reports, approve/reject submissions.

### Web console vs mobile capture

Mobile is where entries are born (offline-capable, camera-first, sometimes voice-dictated); the web console is where configuration (sections, recipients, templates), review, and distribution happen.

## Important Rules / Behaviors

- **The record is contemporaneous and durable.** Entries belong to the day they describe; back-entry for past days is supported, edits are visible in change history, and a completed day is deliberately marked complete (or signed) rather than silently rewritten — the record's value for progress and dispute support depends on this.
- **A completion act closes the day — but its strictness varies.** Some products let users keep editing after signing and un-sign deliberately; others cycle mark-complete and re-open. No product surveyed makes the day immutable in an absolute sense.
- **Attribution is structural.** Entries carry author, time, and commonly company and location; per-company organization of work logs and per-form assignments drive notifications, approvals, and reporting.
- **Collaborator submissions are gated.** Subcontractor entries pend until approved; the approval queue is part of the multi-party recording model.
- **The cadence expects a record for every working day.** Reminders and missed-report tracking in daily-report-led products, and no-work-day entries, keep the series continuous.
- **Some captured data is read-only.** Weather filled automatically by a service may not be editable on the day's record; manual weather entries coexist with it.
- **The log documents, it does not direct.** The daily log records what happened; the machinery that assigns follow-up work (punch items, corrective actions) lives in other registers, even when those registers ship in the same product.

## Variants

- **Pure-play daily-report application** — the day record is the product's heart; SMB general contractors and subcontractors are the audience; time tracking, safety, and RFIs appear as adjacent modules.
- **Platform module** — the daily log is one tool in an enterprise construction platform's project container, beside punch lists, inspections, RFIs, timesheets, and financials.
- **Time-and-quantity-led field suite (heavy civil)** — the day record is a field diary joined to the day's time card and production quantities, feeding job costing; delays and conditions are tagged so reports can be run against them.
- **Form-based realization** — the site diary is a configurable form whose filled instances become dated records and render as report documents, on platforms whose primary objects are tickets and inspections.
- **Naming variance** — the same object is sold as daily log, daily report, daily field report, site diary, and construction diary across regions and segments.
- **Depth dials** — automatic vs manual weather; payroll-grade time cards vs lightweight entries vs none; production quantities and cost linkage (strongest in heavy civil); segments splitting a day by area or phase; voice dictation and geotagged entry creation.
- **Owner-side logs** — owner organizations keeping their own daily logs on the same machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Construction Field Management | superset | adds field work items (punch/issue/task) tracked through assignment to verified completion, plus inspection machinery; the daily log is one of its two primitives — keep only the day record and this Type remains |
| Construction Project Management | container, umbrella | owns schedules, budgets, contracts, and change; hosts the daily log as a module inside the project container |
| Construction Safety Management | adjacent register | safety events appear as daily-log entries, but the incident register, investigation, and corrective-action lifecycle belong to the safety Type |
| Construction Labor Management | adjacent resource view | centers the workforce population and crew administration; time-card sections inside a daily log are one recording, not a workforce system |
| Employee Time Clock / Time & Attendance | adjacent | centers clock-in/out and attendance for payroll; a daily-log timecard section is evidence in the day's account |
| Construction Equipment Management | adjacent resource view | equipment entries in a day record are the seam; the machine population (maintenance, availability) is that Type's center |
| Construction Reality Capture Platform | adjacent | photos inside log entries are evidence; capture-first, spatially anchored visual progress documentation is that Type |
| Construction Quality Management | adjacent register | an "inspection" log entry records that an inspection happened; the checklist/NCR machinery belongs to the quality Type |
| Construction Document Management | adjacent | the distributed daily report is a document output; the controlled document and drawing register is that Type |
| Note-taking Application | different domain | a generic notes/journal app shares the "write about the day" surface but has no project anchoring, no attributed multi-party entries, no project parties, and no reporting/accountability machinery |

The load-bearing boundary is with Construction Field Management: the day record and the field work item are different objects, and every product surveyed keeps them separate even when it ships both. Add work items tracked to verified completion and the product is field management; keep only the day record and it is this Type.

## Representative Products

- Procore — enterprise construction platform; the structured Daily Log tool with typed entry sections beside the full field and financial tool set
- Raken — pure-play daily-report application built around the signed, auto-distributed daily report
- HCSS HeavyJob — heavy-civil field suite where the field diary is joined to time cards, quantities, and job costing
- PlanRadar — European field-documentation platform; site diaries realized as configurable forms and report templates
- Fieldwire by Hilti — field-first standalone; the daily report is a form template among field forms

## Sources

Research date: **2026-09-07**

- Procore — Daily Log tool guide: https://support.procore.com/products/online/user-guide/project-level/daily-log
- Raken — How to Create Your First Daily Report: https://help.rakenapp.com/en/articles/14463911-how-to-create-your-first-daily-report-in-raken ; Daily Reports collection: https://help.rakenapp.com/en/collections/19725844-daily-reports
- HCSS HeavyJob — product page: https://www.hcss.com/products/heavyjob/ ; Daily Log page: https://www.hcss.com/products/daily-log-reporting-software/
- PlanRadar — product page: https://www.planradar.com/ ; Help Center (forms): https://help.planradar.com/hc/en-gb/articles/13920866832541-Manage-Forms-of-a-Project
- Fieldwire by Hilti — Help Center: https://help.fieldwire.com/hc/en-us (Daily Report forms)

> Sourcing limitations: the Raken marketing site, NoteVault, Buildertrend, and Autodesk Construction Cloud were not reachable from the research environment during this pass (or the same-week sibling passes) and are not cited as evidence; the voice-first and residential-builder variants of this Type are therefore unverified. HCSS and PlanRadar product pages are marketing-tier sources, corroborated where possible by their own help-center and video content. Precise operational details (exact entry-type catalogs, exact lock/edit rules, plan-level restrictions) vary by product and are deliberately not stated as general facts in this document; product-level detail is retained in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample breadth check are recorded in the paired Research Notes.
