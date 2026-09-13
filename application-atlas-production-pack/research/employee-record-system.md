# Research Notes — Employee Record System

Research date: 2026-09-06

## Research Goal

Understand what an "Employee Record System" is as an Application Type: what the employee record actually consists of in real products, how records enter / change / end, who may see and change what, how the record connects to the organization and to downstream consumers, and where the boundary lies against HRIS, HCM, onboarding/offboarding, payroll, and directory-type products.

## Initial Boundary

Initial hypothesis before research:

- An Employee Record System is the employer-operated **system of record for employee master data**: one identified record per employee, carrying personal/employment attributes, organizational placement, employment status lifecycle, and attached documents, maintained under employer-controlled access.
- Nearest neighbors: HRIS (broader process system), HCM (broader still), Employee Onboarding/Offboarding (transition workflows), Payroll (consumes record data), Org Chart Management (derived structure), Employee Portal (employee-facing surface), People Analytics (consumes record data).
- Open risk: in the market, "employee record system" is rarely a separately sold category — the employee-record layer is usually marketed as the core of an HRIS. This was flagged as a possible Alias/overlap problem to verify during research.

## Research Questions

1. What is an employee record made of? (attributes, sections, history, documents)
2. How does a record enter the system (hire) and how do changes get made (direct edit, propose/approve, bulk, import, API)?
3. How does the record end or pause (termination, leave, rehire, deletion) and what happens to data afterwards?
4. Who can see and change which parts? (permission model, sensitivity, self-service)
5. How is the record linked to the organization (department, location, supervisor, legal entity)?
6. How is the record consumed downstream (payroll, benefits, reporting, integrations)?
7. What does the record system itself NOT do (boundary against process-running neighbors)?
8. Historical check: would older personnel systems, ERP HR modules, and regional products still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophy, and different customer tiers:

| Product | Segment / philosophy | Why selected |
|---|---|---|
| Personio | European mid-market "Core HR" platform; employee master data ("Personnel Files" / Personalverwaltung) as the foundation | Deep, accessible help-center documentation of the record model |
| BambooHR | North-American SMB HRIS; employee data as the product's center of gravity | Official API documentation exposes the record schema and history tables directly |
| SAP SuccessFactors (Core HR / Employee Central) | Global enterprise HCM suite; "single source of truth for people data" positioning | Enterprise/suite pole; localization and document-management depth |

Rejected / unreachable samples (see Source-access Limitation):

- HiBob — help center gated behind login (two attempts, different locales)
- Factorial — support site 404
- OrangeHRM — docs path 404
- BambooHR marketing site — 403; help center JS-rendered (API documentation site used instead)

## Sources

Tier 1 (official operational documentation):

- Personio Help Center — https://support.personio.de/hc/en-us
  - Employee Management category: https://support.personio.de/hc/en-us/categories/200849035-Employee-Management
  - Overview of the Employee Profile and Personal Info tab: https://support.personio.de/hc/en-us/articles/28163575995933
  - Summary of attributes: https://support.personio.de/hc/en-us/articles/115002699585
  - Update employee data: https://support.personio.de/hc/en-us/articles/213331029
  - Terminate an employment: https://support.personio.de/hc/en-us/articles/4405573920285
- BambooHR API Documentation — https://documentation.bamboohr.com/docs
  - Getting Started With The API: https://documentation.bamboohr.com/docs/getting-started
  - Field Names: https://documentation.bamboohr.com/docs/list-of-field-names
  - Table Name & Fields: https://documentation.bamboohr.com/docs/table-name-fields
  - Get Changed Employee IDs: https://documentation.bamboohr.com/reference/get-changed-employee-ids

Tier 2 (official product/positioning pages):

- SAP HCM: https://www.sap.com/products/hcm.html
- SAP SuccessFactors Core HR and Payroll: https://www.sap.com/products/hcm/core-hr-payroll.html

## Product A — Personio (evidence layer A: directly observed)

Observations from the official Help Center:

**Record container**

- The **employee profile** "stores all employee information in one place" with different tabs for managing employee data. Profile header shows picture, name, status, hire date, and employment details (position, department, team, supervisor, workplace).
- The **Personal Info tab** organizes employee data into **sections and attributes**; each attribute shows its current value; each section shows the viewer's permissions for that section.
- Attributes have types: single-line/multi-line text, link, single-selection and multi-selection lists, number, number with decimals, date, and **relationship attributes** (Person, Additional supervisor) that link to other employee records.
- **Core attributes** are vendor-managed and locked (cannot be edited/deleted by the customer); **custom attributes** are customer-defined, editable, archivable, and can be scoped to specific legal entities. Archived attributes can be shown again with permission.
- Core attributes include: first/last/preferred name, birthday, citizenship, children, employee ID, contract end date, cost centers, department, email, employment type, full-time weekly working hours, gender, hire date, job name (with job architecture: job family/track/level), last day of work, legal entity, marital status, workplace, personal email, mobile phone, position, probation length/end, **status**, supervisor, team, notice pronounced, termination date, regretted/voluntary termination, termination reason, position should be backfilled, termination type, weekly working hours.
- Integration-specific attributes are system-managed when a payroll integration is active.

**Record lifecycle**

- **Hire date** "marks a person's start of employment and turns their status to **Active** on that day."
- **Termination date** "marks a person's end of employment. It turns their status to **Inactive** the day after, which prevents them from logging in."
- Termination is an explicit feature: enter termination date and type, add details, optionally adjust absence entitlement. Termination attributes: termination date, notice announced, last day of work, type of termination (resignation, retirement, collective layoff agreement, contract expired, court settlement, death, dismissal, mutual termination, settlement agreement, switch of legal entity, valid cancellation), voluntary (yes/no), regretted (yes/no), position to be backfilled, termination reason.
- **Contract end date ≠ termination date**: a fixed-term contract end does not end employment; status stays Active unless terminated.
- **Rehire**: "Rehire this person" transfers a former employee's data to a new profile.
- **Delete profile** permanently removes the record (administrators only, irreversible); termination is the recommended alternative because it "keeps employee data for historical reporting."
- Inactive profiles: visible only in search/People list to users with view rights on Status; removed from the org chart; do not count toward the plan's employee limit; remain visible in historical reports.

**Change mechanics**

- Attribute updates are **effective-dated**: immediate (today), retroactive (past date), future (scheduled; applied at a fixed nightly time), or **temporary** (reverts on a set date).
- A **History tab** records every attribute/salary change with attribute, application date, editor, old value, new value, requester, approver, creation date. History entries **cannot be deleted**; corrections are made by adding new entries or modifying dates.
- Bulk editing via the People list (Actions → Edit profile) including backdating to each employee's hire date.
- Data can also enter/update via import, public API, onboarding tasks, and the Recruiting module when hiring a candidate.

**Access & permissions**

- Role-based permissions with per-section rights: **View / Propose / Edit**. Employees with Propose rights can submit changes for approval; View-only users see current values only (scheduled future changes hidden from them).
- Date attributes can restrict year visibility for view-only users.
- Administrators can "log in as this employee" to verify permission setup.

**Organization linkage & surfaces**

- Supervisor attribute (plus additional-supervisor relationship attributes for dotted lines); **Org chart** view derived from the record; People list as the searchable roster.
- Documents Hub: document management with templates and placeholders fed by attributes.
- Reminders can be attached to the profile; long-term leave can be scheduled on the profile.

## Product B — BambooHR (evidence layer A: directly observed, via official API documentation)

Observations from the official API documentation (the API is permissioned "as if a real user were using the software"):

**Record schema (fields)**

- Identity/personal: firstName, lastName, middleName, preferredName, displayName, dateOfBirth, gender, ssn, sin, nin, nationalId, passportNumber, nationality, ethnicity, maritalStatus, eeo (US EEO job category).
- Contact: workEmail, homeEmail, bestEmail, workPhone/homePhone/mobilePhone (+extension), address1/2, city, state, country.
- Employment: hireDate, originalHireDate, terminationDate, employmentStatus (list: "Contractor", "Full-Time", "Furloughed", "Part-Time", "Terminated", or custom), status ("Active"/"Inactive"), exempt (FLSA overtime status), standardHoursPerWeek, includeInPayroll, employeeNumber ("assigned by your company"), payGroup, timeTrackingEnabled.
- Organization: department, division, location, jobTitle, reportsTo/supervisor (employee-reference fields).
- Compensation: payRate, payType, paidPer, payFrequency, paySchedule, payChangeReason, overtimeRate.
- System fields: id (auto-assigned), lastChanged timestamp, createdByUserId.

**Record = profile fields + dated history tables**

- Tabular tables attached to the employee: **jobInfo** ("the history of an employee's role within a company": date, location, department, division, jobTitle, reportsTo), **compensation** (rate history with startDate/endDate, type, reason), **employmentStatus** (status history with termination reason/type/rehire/regrettable fields), plus side tables: dependents, contacts/emergencyContacts, employeeEducation, employeeCertifications, employeeVisas, employeePassports, employeeAssets, bonus, commission, earnings, employeeStockOptions, employeeEquityGrants.
- Termination details recorded on the status change: terminationTypeId ("Death", "Resignation (Voluntary)", "Termination (Involuntary)"), terminationStatusId (reason list), terminationRegrettable, terminationRehireId (rehire eligibility: "Yes"/"No"/"Upon review").

**Schema extensibility & integrity**

- Custom fields: create/edit/archive; archived fields remain listable. List-field options are soft-deleted ("archived") and "included so that historical data can reference the value."
- Change tracking: "Get Changed Employee IDs" returns employees changed since a timestamp — "a change in ANY individual field in the employee record, as well as any change to the employment status, job info, or compensation tables" — with change type Inserted/Updated/Deleted. This confirms the record is a synchronized system-of-record object consumed by other systems.
- Files: company files organized in categories with per-user visibility; employee documents handled through file sections with view permissions.
- Sensitive data: SSN/SIN of dependents returned masked; stored encrypted.

## Product C — SAP SuccessFactors Core HR / Employee Central (evidence layer A for positioning statements, layer B otherwise)

Observations from official product pages (Tier 2):

- Core HR is positioned as the "localized foundation for cloud HR": "Establish a **single source of truth for people data** and drive compliance with a solution localized in more than 100 countries and territories."
- AI-enabled self-services and "personalized profiles" for employees.
- **Centralized document management**: "Store and manage employee documents from one place"; full-text search and self-service; "retention rules and employee file completeness checks"; document templates for personalized employee communications.
- SAP's own HRIS definition (FAQ): software that manages core HR processes and "store[s] employee data, such as personal, demographic, and compensation information."
- The suite separates Core HR (Employee Central) from time tracking, payroll, benefits, and service delivery — i.e., the record layer is one module of a broader HCM suite.

Note: SAP Help Portal (help.sap.com) is a JS-rendered SPA and could not be fetched; operational detail for Employee Central is therefore NOT directly observed. All SAP-specific claims above are kept at positioning level.

## Cross-product Comparison

| Dimension | Personio | BambooHR | SAP SuccessFactors |
|---|---|---|---|
| Record container | Employee profile with tabs; Personal Info tab of sections/attributes | Employee record with fields + tabular history tables | "Single source of truth for people data" (positioning) |
| Identity | Employee ID; email as login | Auto-assigned id + company-assigned employeeNumber | (not directly observed) |
| Personal data | Names, birthday, citizenship, marital status, children, contact data | Names, DOB, gender, government IDs (ssn/sin/nin/nationalId), contact data | personal, demographic data (per SAP's HRIS definition) |
| Employment data | Employment type, weekly hours, probation, contract end, cost centers, legal entity | employmentStatus, exempt/FLSA, standardHoursPerWeek, includeInPayroll | compensation information (per SAP's HRIS definition) |
| Org placement | Department, team, position/job architecture, supervisor + additional supervisors, workplace, legal entity | department, division, location, jobTitle, reportsTo | (not directly observed) |
| Status lifecycle | Status attribute: Active on hire date → Inactive day after termination date; prevents login | status Active/Inactive; employmentStatus history table | (not directly observed) |
| Termination | Dedicated feature with date/type/voluntary/regretted/backfill/reason | employmentStatus table row with termination type/reason/rehire-eligibility/regrettable | (not directly observed) |
| History | Append-only History tab (old/new value, editor, requester, approver); effective-dated changes (immediate/retro/future/temporary) | Dated history tables (jobInfo, compensation, employmentStatus); lastChanged; changed-IDs sync | (not directly observed) |
| Documents | Documents Hub with templates/placeholders | Files with categories and visibility permissions | Centralized document management with retention rules and completeness checks |
| Permissions | Role-based per-section View/Propose/Edit; year-visibility restriction; admin "log in as employee" | API permissioned per user; masked sensitive fields | (not directly observed) |
| Self-service | Employees can propose changes with approval | (implied by permissioned user model; not directly observed) | AI-enabled self-services (positioning) |
| Extensibility | Custom attributes (archivable, legal-entity scoped) | Custom fields (archivable); soft-deleted list options for historical integrity | (not directly observed) |
| Downstream | Payroll integration attributes; reports; org chart | Changed-employee sync; payroll flags; reports | Predelivered integrations with SAP payroll (positioning) |
| Entry points | Import, API, onboarding tasks, recruiting module | API (add employee endpoints in reference) | (not directly observed) |

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the Type stops being recognizable:

```text
Employer-operated system of record
└── Identified employee record (one per person, employer-assigned identity)
    └── Employment data (employer-defined attributes about the person and their employment)
        └── Employment-status lifecycle (hire → active → end; status governs presence/access; record retained after end)
```

Four properties:

1. **Identified employee record** — each person in the workforce is held as an individually identified record (one record per person). Without this, it is not a record system.
2. **Employment data** — the record carries the employer-defined data describing the person and their employment (who they are, what their job is, where they sit in the organization, on what terms). Without this, it is just a user directory.
3. **Employment-status lifecycle** — the record's status follows the employment relationship (not yet started → active → ended), status changes are recorded events (hire, termination), and the record persists after the employment ends. Without this, it is a contact list, not a record of employment.
4. **Employer custody / system-of-record role** — the organization (not the employee) owns and maintains the record as the authoritative version that other processes and systems consume. Without this, it is a self-authored profile surface.

### L1 — Common Mature Structure

Present across the researched sample (and expected in any mature product), but not required to recognize the Type:

- **Profile surface** — per-employee page organizing the record into sections/tabs (personal info, job/employment, compensation, documents).
- **Attribute schema with core + custom split** — vendor-managed standard attributes plus customer-defined attributes; archiving instead of hard deletion to preserve historical integrity.
- **Effective-dated changes** — immediate, retroactive, future-scheduled, and temporary (auto-reverting) changes.
- **Change history / audit trail** — who changed what, when, old value → new value; append-only in mature implementations.
- **Permission model** — role-based, section/field-level rights (view / propose / edit); sensitive-field handling (masking, restricted visibility).
- **Employee self-service** — employees view their own record and, in some products, propose or directly update limited fields.
- **People list / directory** — searchable roster of all records; bulk edit.
- **Organizational linkage** — department, location, supervisor/reporting line; org chart derived from record data.
- **Documents attached to the record** — contracts, IDs, certificates; templates; in enterprise products, retention rules and completeness checks.
- **Lifecycle operations** — hire (record creation, often fed from recruiting/onboarding), position change, long-term leave, termination (with termination details), rehire (reusing the old record), deletion (irreversible, exceptional).
- **Bulk operations & import/API** — mass update, data import, programmatic access.
- **Downstream consumption** — reports/analytics, payroll/benefits/time systems consuming record data, change-based sync.

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, regulatory posture:

- **Population scope** — employees only vs employees + contractors/contingent workers (employment-type attributes exist for this in both Personio and BambooHR).
- **Multi-entity / multi-country** — legal-entity-scoped attributes, country-specific fields, localization (SAP: 100+ countries).
- **Packaging** — standalone record-keeping product vs core module of an HRIS vs module of an ERP/HCM suite.
- **Self-service depth** — view-only vs propose-with-approval vs direct edit of limited fields.
- **Document-management depth** — simple attachments vs governed document management (retention, completeness checks).
- **Sensitive-data posture** — encryption, masking, field-level privacy, regional privacy regimes.
- **Identity integration** — SSO, directory sync, record-driven account provisioning (status change disables login).
- **Regulatory overlays** — EEO/FLSA fields (US), works-council involvement (EU), country-specific termination types.

### L3 — Vendor-specific Structure

Stays in Research Notes:

- Personio: "Personal Info tab" naming; locked core attributes; scheduled future changes applied at a fixed nightly time; inactive profiles not counted toward plan employee limits; admin "log in as this employee"; UK-law-specific termination types; celebration widget fed by birthday attribute.
- BambooHR: specific API field names (acaStatus, flsaCode, bestEmail); named tabular tables (jobInfo, employeeStockOptions, employeeEquityGrants); rehire-eligibility option list; Get Changed Employee IDs sync endpoint; 20MB file limit.
- SAP: Employee Central / Work Zone / Joule assistant naming; "localized in more than 100 countries" claim; Gartner MQ positioning.

## Vendor-specific Findings

See L3. Additionally:

- Personio's plan-limit behavior (inactive profiles don't count) is a commercial mechanic, not a structural property of the Type.
- BambooHR's "bestEmail" (work email if set, otherwise home email) is an implementation convenience.

## Boundary Findings

| Neighbor | Relationship | Distinction |
|---|---|---|
| HRIS | strongest overlap | HRIS operates HR processes (absence, benefits, time, payroll, workflows) on top of the employee data; the Employee Record System is the record layer itself. In the market the record layer is usually sold as the core of an HRIS, so the two Types share most products. |
| HCM | superset | HCM adds talent management (performance, learning, compensation planning) around the same record. |
| Employee Onboarding / Offboarding Platform | process vs record | Those run owner-assigned task workflows around the employment transition; the record system holds the record those processes update (consistent with the already-published offboarding document). |
| Payroll System | consumer | Payroll computes pay from record data (pay rates, status, tax data); it does not own the employment record. |
| Org Chart Management | derived view vs record | Org chart tools center on structure editing/scenarios; here the chart is a view derived from supervisor/department attributes. |
| Employee Portal | surface vs custody | The portal aggregates employee-facing content/services; the record system is the data custody behind it. |
| People Analytics | consumer | Analytics reads the record; it does not maintain it. |
| HR Case Management | different object | Cases/requests are the object there; the employee record is static context. |
| CRM | different subject | CRM holds customer/commercial relationships; remove the employment-status lifecycle and employer custody and an employee record system degenerates into a contact directory. |

**"Remove what to become another Type" tests:**

- Remove employment-status lifecycle + employer custody → contact directory / CRM.
- Remove record custody, keep only transition task workflows → onboarding/offboarding platform.
- Remove the employee subject, keep org structure editing → org chart management.
- Add process operation (absence, benefits, payroll runs) on top → HRIS/HCM territory.

**Alias/overlap problem (to record in STATUS.md):** no sampled product sells itself as a standalone "employee record system"; the record layer is marketed as the core of Core-HR/HRIS products (Personio "Core HR", SAP "Core HR", BambooHR HRIS). The leaf is best understood as the **record-centric view** of the core-HR layer. It remains documentable as a distinct Type (different center of gravity: custody of the record vs operation of HR processes), but a joint review with the HRIS leaf is recommended when HRIS is processed.

## Historical / Market-Sample Check

- **Older personnel systems** (1980s–90s personnel information systems, government personnel files): identified employee record + employment data + status + organizational assignment — fits L0. They lack self-service, effective-dating UIs, and fine-grained permissions, which confirms those belong in L1/L2, not L0.
- **ERP HR modules** (SAP ERP HCM, PeopleSoft HCM): the "worker/master data" record is the core — fits L0.
- **Regional products** (Personio in Europe, BambooHR in North America): both fit L0 despite different terminology (Personnel Files vs employee fields).
- Conclusion: L0 as defined survives the historical check. Nothing era-specific (self-service, cloud, effective-dating UI, document hub) is required by the definition.

## Uncertainties

- SAP SuccessFactors operational detail (record model, permission model, lifecycle mechanics) could not be directly observed (JS-rendered help portal); SAP claims are kept at positioning level.
- HiBob, Factorial, OrangeHRM unreachable; the sample is three products. Cross-product claims rest on Personio + BambooHR direct observation with SAP positioning support.
- Employee self-service depth in BambooHR (what employees can edit about themselves) was not directly observed.
- Whether any market product exists that is *only* an employee record system (no HR processes at all) was not confirmed; the researched products all bundle at least some HR processes. This supports the alias/overlap flag rather than refuting the Type.

## Final Synthesis

An Employee Record System is the employer-operated system of record for the workforce: one identified record per employee, carrying employer-defined employment data, moving through an employment-status lifecycle (hire → active → end) with the record retained after the employment ends, maintained under employer-controlled access, and consumed by the organization's other people-processes. Mature products wrap this core in a profile surface, an extensible attribute schema, effective-dated changes with an audit trail, role-based permissions with employee self-service, a searchable roster, organizational linkage, attached documents, and integration surfaces for payroll/benefits/reporting. The Type's center of gravity is **custody of the record**; operating HR processes on top of the record is the territory of the neighboring HRIS/HCM Types — which is why, in today's market, the record layer usually ships as the core of those products.
