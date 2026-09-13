# Employee Record System

## Overview

An **Employee Record System** is an employer-operated system of record for the workforce: it holds one identified record per employee, carries the employer-defined data describing that person and their employment, moves the record through the employment lifecycle (hired → active → ended), and keeps the record — under employer-controlled access — as the authoritative source that the organization's other people-processes consume.

The defining core is deliberately small:

```text
Employer-operated system of record
└── Identified employee record (one per person)
    └── Employment data (who they are, what their job is, where they sit, on what terms)
        └── Employment-status lifecycle (hire → active → end; record retained after end)
```

Everything else commonly associated with modern HR software — employee self-service, effective-dated change history, document management, org charts, payroll and benefits integration — is standard in mature products but is not what makes the system an employee record system. Older personnel systems, ERP HR modules, and regional products also fit this definition without any of those specifics.

The center of gravity is **custody of the record**. Operating HR processes on top of the record — absence, benefits, payroll runs, recruiting pipelines — belongs to neighboring types (HRIS, HCM, Payroll). In today's market the record layer usually ships as the core of those broader products, which is why the products listed at the end are all positioned as core-HR or HRIS systems.

## Users & Context

Primary users are on the employer side:

- **HR administrators / HR operations** — create records, maintain employment data, run lifecycle transitions (hire, change, leave, termination), manage documents, configure the attribute schema and permissions.
- **Managers** — view records of their direct reports within permission limits; in some products propose or approve changes.
- **Employees** — view their own record through self-service; depending on the product, propose updates to limited fields (address, bank details, emergency contacts) for approval.

Secondary consumers do not primarily "use" the system but depend on it:

- **Payroll, benefits, and time systems** — consume pay rates, employment status, organizational assignment, and tax-relevant data from the record.
- **Reporting and analytics** — aggregate record data into workforce reports.
- **IT / identity systems** — consume record status to grant or revoke account access.

The work context is administrative and continuous: records are touched every time someone is hired, changes roles, moves, takes leave, or leaves the organization — and audited when employment data must be proven.

## Core Model

### The Employee Record

The central object is the **employee record**: one identified record per person, held for as long as the organization needs it. A record has four parts:

- **Identity data** — who the person is: legal name (and often a preferred name), date of birth, government or tax identifiers, contact details (work and personal email, phones, address). The record carries an employer-assigned identifier (employee number/ID) alongside the person's own attributes.
- **Employment data** — the terms of the relationship: hire date, employment type (full-time, part-time, contractor), working hours, probation, contract end date, compensation data, pay-related flags.
- **Organizational placement** — where the person sits: department, division, location/workplace, job title or position, supervisor (reporting line), and in multi-entity organizations the legal entity and cost centers.
- **Employment status** — the record's state in the employment lifecycle. Status is not just a label: it drives whether the person appears in the active workforce, whether they can log in, and how they are counted.

### Attributes: Standard and Custom

The data in a record is held as **attributes** organized into sections (personal information, job/employment, compensation, and so on). Mature products distinguish:

- **Standard attributes** — defined by the product, covering the near-universal fields (names, hire date, department, supervisor, employment status…). These usually cannot be renamed or removed because other features depend on them.
- **Custom attributes** — defined by the organization to fit its needs (emergency contact, visa expiration, parking spot, languages spoken). Custom attributes can typically be added, edited, and archived. Archiving — rather than deletion — preserves historical data that references them.

Attribute values are typed (text, numbers, dates, option lists) and some types create **relationships between records** — most importantly the supervisor relationship, which links one record to another and, aggregated, forms the organizational chart.

### The Record as History, Not Just Current Values

A defining behavior of mature implementations: the record is not a single overwrite-able row. Changes are **effective-dated** and **recorded**:

- A change can take effect immediately, retroactively (backdated to reflect reality), in the future (scheduled), or temporarily (auto-reverting on a set date).
- Each change is logged with what changed, the old and new values, when it takes effect, and who made (and, where applicable, who approved) it. Mature implementations keep this history append-only: corrections are made by adding new entries, not by erasing old ones.
- Job and compensation data are commonly held as **dated history** — a sequence of role/compensation/status entries over time — so that "what was true on a given date" can always be answered.

### Documents Attached to the Record

Employment generates paperwork: contracts, amendments, certificates, identity documents. The record system stores these as **documents attached to the employee record**, often organized in categories with their own visibility rules. More complete implementations add document templates (filled from record attributes), retention rules, and completeness checks on the employee file.

### Permissions

Because the record holds sensitive personal data, **access is employer-controlled and role-based**:

- Rights are typically granted per section or per attribute: view, propose, or edit.
- Employees see their own record within limits; sensitive fields (government IDs, salary) are commonly masked or restricted.
- A change proposed by an employee or manager can require approval before it takes effect.

### Concept vs Implementation

The core model is conceptual; products implement it differently:

```text
Concept:            Identified employee record
Implementations:    employee profile (profile page with tabs), employee object with fields + history tables

Concept:            Employment status
Implementations:    a status attribute (Active/Inactive) driven by hire/termination dates; a status history table

Concept:            Organizational placement
Implementations:    department/division/location/supervisor attributes; job architecture objects; org chart views

Concept:            Change history
Implementations:    an append-only history tab; dated history tables per domain (job, compensation, status)
```

## How It Works

### Create a record (hire)

```text
A person is hired
→ a record is created (manually, via import, via API, or fed from recruiting/onboarding)
→ identity and employment data are filled in
→ hire date is set
→ the record becomes active on the hire date
→ the person appears in the workforce (roster, org chart, counts)
```

### Maintain the record

```text
Something changes (address, role, department, working hours, salary)
→ an authorized user edits the attribute (or an employee proposes the change)
→ an effective date is set (today / past / future / temporary)
→ the change is recorded in the history with old and new values
→ downstream views and reports reflect the change from that date
```

Bulk maintenance is standard: select many records and apply the same change; import data in volume; update programmatically through an API.

### Move through the lifecycle

```text
Position change   → update position/department/supervisor (often together with salary and schedule changes)
Long-term leave   → record the leave period on the record
Contract end      → a fixed-term contract end date is tracked, but does not by itself end employment
Termination       → an explicit termination action records the termination date, type (resignation, dismissal, retirement…),
                    and details (voluntary or not, regretted or not, rehire eligibility, reason)
→ status flips to inactive after the termination date
→ the person loses access, leaves the active roster and org chart,
  but the record is retained for historical reporting
Rehire            → a former employee can be rehired by reusing their old record
Deletion          → permanent removal of the record is an exceptional, administrator-only, irreversible action
```

### Consume the record

```text
Reports and analytics read record data
→ payroll/benefits/time systems consume pay, status, and organizational data
→ integrations sync changes outward (change-based synchronization is a common pattern)
→ identity systems use status to grant or revoke access
```

## Interfaces

### People list / roster

The entry surface for the employer side.

- Purpose: find and act on employee records.
- Typical information: name, status, position, department, supervisor, workplace.
- Primary actions: search, open a record, create a record, bulk edit, filter by status or attribute.

### Employee profile

The record itself, one page per person.

- Purpose: view and manage everything about one employee.
- Typical information: profile header (photo, name, status, hire date, position, department, supervisor), then sections of attributes (personal info, job/employment, compensation), plus tabs or areas for history and documents.
- Primary actions: edit attributes with an effective date, propose changes, view change history, upload documents, run lifecycle actions (schedule leave, terminate employment, rehire, delete).

### Change history view

- Purpose: answer "what was changed, when, by whom, and what was true before".
- Typical information: attribute, old value, new value, effective/application date, editor, requester, approver.
- Primary actions: inspect entries, add a backdated correction entry, adjust an entry date.

### Documents area

- Purpose: hold the employee's paperwork with the record.
- Typical information: document categories, files, templates.
- Primary actions: upload, generate from template, set visibility, check completeness (in more complete implementations).

### Administration settings

- Purpose: configure the record system itself.
- Typical information: attribute/section definitions, custom attributes, permission roles, document categories, import mappings.
- Primary actions: add/archive attributes, define roles and rights, configure integrations.

### Employee self-service view

- Purpose: let the employee see (and within limits, maintain) their own record.
- Typical information: their own attributes, their documents, pending proposals.
- Primary actions: view, propose a change to an allowed field, confirm data.

## Important Rules / Behaviors

- **Status governs presence and access.** The hire date activates the record; the termination date deactivates it (in the researched products, the day after the termination date). An inactive record's holder can no longer log in, disappears from the active roster and org chart, but remains in historical reports.
- **Termination is not deletion.** Ending an employment changes the record's status and adds termination details; the record is kept for history. Permanent deletion is a separate, exceptional, irreversible action.
- **A contract end date does not, by itself, end employment.** In some products a fixed-term contract end date is tracked and can trigger reminders, but employment remains active until an explicit termination is recorded.
- **Changes are effective-dated and traceable.** Retroactive, scheduled, and temporary changes are first-class; history is append-only. Late corrections to effective dates affect which reports a person appears in.
- **Permissions gate both visibility and action.** What a user sees (down to individual attributes, sometimes down to parts of a value such as the year in a date) and what they may change (view / propose / edit) are both controlled; proposed changes may require approval.
- **The record is the source, not the consumer.** Payroll, benefits, time, and identity systems read from the record; the record system's own job is to keep the data correct, complete, and attributable.

## Variants

- **Standalone record-keeping vs core of an HRIS/HCM suite** — the same record layer is sold standalone for simple needs or as the foundation module of a broader HR platform; the suite pole adds absence, benefits, payroll, and talent modules around the record.
- **Small-business vs enterprise** — small-business products emphasize simple profiles and self-service; enterprise products add multi-entity structures, country localization, governed document management, and compliance controls.
- **Single-country vs multi-country** — multi-country deployments carry legal-entity scoping, country-specific attributes, and localized rules (termination types, tax identifiers).
- **Employee-only vs extended workforce** — some record populations include contractors and contingent workers, usually via employment-type attributes.
- **Self-service depth** — from view-only employee access to propose-with-approval to limited direct editing.
- **Regulatory overlays** — region-specific fields and behaviors (government/tax identifiers, EEO categories, works-council constraints, retention rules).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Human Resource Information System / HRIS | strongest overlap | The HRIS operates HR processes (absence, benefits, time, workflows) on top of the employee data; the record system is the record layer itself. In the market the record layer is usually the core of an HRIS product. |
| Human Capital Management / HCM | superset | HCM adds talent management (performance, learning, compensation planning) around the same record. |
| Employee Onboarding / Offboarding Platform | process vs record | Those run owner-assigned task workflows around the employment transition; the record system holds the record those processes update. |
| Payroll System | consumer | Payroll computes pay from record data (rates, status, tax identifiers); it does not own the employment record. |
| Org Chart Management | derived view vs record | Org chart tools center on editing and simulating structure; here the chart is a view derived from supervisor and department attributes. |
| Employee Portal | surface vs custody | The portal aggregates employee-facing content and services; the record system is the data custody behind it. |
| People Analytics Platform | consumer | Analytics reads and aggregates the record; it does not maintain it. |
| HR Case Management | different object | Cases and requests are the working objects there; the employee record is context. |
| CRM | different subject | CRM holds customer and commercial relationships; strip the employment lifecycle and employer custody from an employee record system and it degenerates into a contact directory. |

The boundary with HRIS is the most important one, because the two types share nearly all products. The structural difference is the center of gravity: custody and correctness of the record versus operation of HR processes on top of it.

## Representative Products

- **Personio** — European mid-market core-HR platform; employee master data ("Personnel Files") as the documented foundation.
- **BambooHR** — North-American SMB HRIS with employee data at its center; its official API documentation exposes the record schema and history tables directly.
- **SAP SuccessFactors (Core HR / Employee Central)** — global enterprise HCM suite; the record layer positioned as the "single source of truth for people data" with country localization and governed document management.

These three were chosen to span segment (SMB / mid-market / enterprise), geography (North America / Europe / global), and packaging (standalone-leaning HRIS / core-HR platform / enterprise suite).

## Sources

Research date: **2026-09-06**

- Personio Help Center — Employee Management / Personnel Files:
  - Overview of the Employee Profile and Personal Info tab — https://support.personio.de/hc/en-us/articles/28163575995933
  - Summary of attributes — https://support.personio.de/hc/en-us/articles/115002699585
  - Update employee data — https://support.personio.de/hc/en-us/articles/213331029
  - Terminate an employment — https://support.personio.de/hc/en-us/articles/4405573920285
- BambooHR API Documentation:
  - Getting Started With The API — https://documentation.bamboohr.com/docs/getting-started
  - Field Names — https://documentation.bamboohr.com/docs/list-of-field-names
  - Table Name & Fields — https://documentation.bamboohr.com/docs/table-name-fields
- SAP:
  - SAP HCM overview — https://www.sap.com/products/hcm.html
  - SAP SuccessFactors Core HR and Payroll — https://www.sap.com/products/hcm/core-hr-payroll.html

> Sourcing limitation: SAP's technical help portal could not be fetched (JS-rendered), so SAP-specific observations are limited to official positioning pages; operational detail for that product is intentionally not stated. HiBob, Factorial, and OrangeHRM documentation was unreachable from the research environment and was dropped after repeated attempts. Precise vendor-specific values (field names, scheduled-update times, plan-limit behaviors) are recorded in the paired Research Notes rather than asserted here.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
