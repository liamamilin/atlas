# Research Notes — Daily Log Application

## Research Goal

Understand what a "Daily Log Application" actually is as an Application Type in the construction family: what objects it holds, who writes into it, how a day is recorded, completed, and distributed, how it relates to the daily-report/site-diary paper tradition, and where it begins and ends relative to Construction Field Management (whose own research pass defined this leaf as the subtraction result "keep only the day record"), Construction Project Management, and the other construction leaves.

## Initial Boundary

Working hypothesis at start:

- A Daily Log Application is the construction project's **day-record system**: per-day, project-anchored records of site activity and conditions (work performed, labor, equipment, deliveries, weather, delays, events), written by field personnel, completed through a deliberate completion act, and distributed outward as daily reports.
- It sits inside the Construction family (directory §17, between Construction Field Management and RFI Management). The name "daily log" collides with consumer journaling apps; the directory placement scopes this Type to construction.
- Nearest neighbors: Construction Field Management (day record + work items), Construction Project Management (container/umbrella), Construction Safety Management (safety register), Construction Labor Management / Time & Attendance (time capture), Construction Equipment Management, Construction Reality Capture (photos), Note-taking Application (generic).
- Main risk: defining the Type by the modern structured-log implementation (Procore-style typed entry sections) when form-based and diary-style realizations are equally valid; also the risk of swallowing work-item machinery that belongs to Construction Field Management.

## Research Questions

1. What is the central object — is it a "day" container, a stream of entries, a report document, or all three?
2. What entry types/sections does a day record hold across products? Which are definitional vs configurable?
3. Who authors entries (superintendent, foreman, subcontractor collaborators, owners) and what approval machinery exists?
4. What is the day's lifecycle: open → complete/signed → distributed? Can signed/completed days be edited? Back-entry for past days?
5. How does the record get out of the system (PDF, email, automatic distribution) and who receives it?
6. Is there compliance machinery (reminders, missed-report tracking)?
7. How does the log relate to time cards, quantities, photos, safety records, inspections — inside or beside the Type?
8. What did the daily log look like before software (paper daily report / site diary tradition) — historical/market-sample check?
9. What naming does the market use (daily log / daily report / daily field report / site diary / construction diary)?
10. Boundary: what addition makes this Type become Construction Field Management, and what subtraction dissolves it?

## Representative Products

Selected for market representativeness, documentation depth, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence depth |
|---|---|---|---|
| Procore | Structured Daily Log tool as one module of the enterprise construction platform | Enterprise GC / owner | Tier-1 support site (tool guide, tutorial catalog, FAQ titles) |
| Raken | Pure-play daily-report-led application ("the daily report is the heart of Raken") | SMB GC / subcontractor | Tier-1 help center (detailed how-to + collection map) |
| HCSS HeavyJob | Heavy-civil field suite where the daily log is tied to time cards, quantities, job costing | Self-performing civil/infrastructure contractors | Tier-2 product pages + vendor video transcript (operational) |
| PlanRadar | European field-documentation platform; site diary realized as a form/report template | Mid-market GC / consultancy / owner (Europe-led) | Tier-1 help center (forms mechanics) + Tier-2 product page |
| Fieldwire by Hilti | Field-first standalone; the day record is a form template (Daily Report) | Mid-market GC + specialty contractors | Tier-1 help center search results (this pass) + sibling-run help-center evidence (same week) |

Market anchors acknowledged but **not directly documented** (unreachable — see Sources / Uncertainties): NoteVault (voice-first daily reporting), Buildertrend (residential builder pole), Autodesk Construction Cloud / Build (suite module), Raken marketing site. No claims are made from these.

## Sources

Research date: **2026-09-07**

- Procore — Daily Log tool guide: https://support.procore.com/products/online/user-guide/project-level/daily-log (tool description, tutorial catalog incl. entry-type tutorials, FAQ titles, workflow, recent changes)
- Raken — How to Create Your First Daily Report: https://help.rakenapp.com/en/articles/14463911-how-to-create-your-first-daily-report-in-raken
- Raken — Daily Reports collection: https://help.rakenapp.com/en/collections/19725844-daily-reports (article map incl. segments, reminders, missed reports, weather capture)
- HCSS HeavyJob — product page: https://www.hcss.com/products/heavyjob/ ; Daily Log product page: https://www.hcss.com/products/daily-log-reporting-software/ (FAQ definitions + Field Diary video transcript)
- PlanRadar — product page: https://www.planradar.com/ ; HelpCenter search "site diary": https://help.planradar.com/hc/en-gb/search?query=site+diary ; Manage Forms of a Project: https://help.planradar.com/hc/en-gb/articles/13920866832541-Manage-Forms-of-a-Project ("Daily Site Log" form example)
- Fieldwire by Hilti — help center search "daily report": https://help.fieldwire.com/hc/en-us/search?query=daily+report ("Introduction to 'Daily Report' Forms" snippet, custom form builder, forms tab list)
- Fieldwire by Hilti — additional Layer-A observations recorded in the sibling pass `research/construction-field-management.md` (fetch 2026-09-07: help center + product pages)
- Boundary counterparts (prior passes, same repo): `research/construction-field-management.md` (defines Daily Log Application as the day-record-only subtraction result; L0 removal test), `research/construction-project-management.md` (flags Daily Log as PM-platform module / legitimate point Type), `research/construction-safety-management.md` (incident→daily-log summary interlock)

Source-access limitations: rakenapp.com marketing site (403), notevault.com (transport error ×2 in the same-week sibling run — not retried), buildertrend.com (403) + help.buildertrend.com (timeout), autodesk.com help (403 in sibling runs same week). Per network rules these were abandoned; findings relying on them are not asserted. HCSS and PlanRadar product pages are Tier-2 marketing; their operational claims are corroborated where possible by help-center/video content.

## Product A — Procore

### Key observations (Layer A — support-site content, fetched 2026-09-07)

- Tool description: "The Daily Log tool is designed to provide members of your project team with a central location for viewing, tracking, and emailing updates about daily project activities." View the daily log for a specific day or a date range; review current weather from a weather service or from a compatible on-site weather station; arrange the page layout; add log entries or create entries based on the previous day; forward logs to contacts named in the Project Directory.
- **Entry types** (evidenced by the tutorial catalog — one tutorial per type): Accident, Daily Construction Report, Delay, Delivery, Dumpster, Equipment, Inspection, Manpower, Notes, Observed Weather, Phone Call, Plan Revision, Productivity, Quantity, Safety Violation, Scheduled Work, Timecard, Visitor, Waste, Work Log. Customizable log names and configurable/custom fields are documented in recent-changes entries; company and location fields were recently extended to all daily log types.
- **Day mechanics**: Mark a Daily Log as Complete; Re-Open a Daily Log; Copy a Daily Log; Enter Logs for a Previous Day; Edit Previously Entered Daily Log Entries; View Daily Log Change History; Calendar view and List view; Search/Filter; Segments (multiple logs per day — recently added); Quick Create; Bulk Delete.
- **Multi-party authorship**: Create Daily Log Entries as a Collaborator (subcontractor); Resubmit as Collaborator; Approve or Reject Daily Log Entries; View Pending Daily Log Entries; Create Pending Entries for Missing Companies. Role-scoped tutorial tracks exist for Superintendent, Field Worker, Subcontractor-as-Collaborator, Specialty-Contractor-as-Client, and Owner (Owner - Add/Configure/View Daily Log Entries).
- **Evidence & attachments**: Add a Photo to a Daily Log Entry so that it Populates in the Photos Tool; Upload Photos from the Photos Tool; Attach Files; Related Items linking across tools.
- **Output**: Email a Daily Log; Export a Daily Log as PDF; View a Daily Log Canned Report; Create a Custom Report from the Daily Log; Action-Oriented Emails for Daily Logs (FAQ).
- **Weather**: Observed Weather Condition entries (manual) coexist with service-provided weather; FAQs cover weather-delay alerts, weather not showing, and why the weather-delay row cannot be changed (service-filled row is read-only).
- **Rules/limits signaled by FAQ titles**: "Why does the Daily Log's calendar only let me select dates in the past?" (day selection is past-oriented — back-entry supported); production quantities connect to the project budget; timecard entries relate to the separate Timesheets tool.

## Product B — Raken

### Key observations (Layer A — help center, fetched 2026-09-07)

- Framing (article opening): "The daily report is the heart of Raken. It's how field crews document what happened on the jobsite each day — who worked, what was done, weather conditions, photos, safety notes, and more. Once signed and completed, the report is automatically distributed to stakeholders as a PDF."
- **Mobile-first day flow**: open the app → Project Tools → select project → "today's daily log opens automatically"; a date strip navigates between days. Web app: Projects → [Project] → Daily Logs with date navigation.
- **Sections of the day**: Work logs (organized **by company** — a GC tracks subcontractor headcount and activity; free-text name alternative), Notes (rich text, appear in the PDF, can carry photos/files), Attachments (photos from camera, files), Time cards (individual employee hours for payroll), Survey (admin-configured daily questions; **delays are logged as survey questions**, e.g. weather/material delay), Safety & QC (toolbox talks, checklists, observations).
- **Completion & integrity**: Preview report → Sign & complete (drawn signature) → **automatic distribution** to configured recipients; signing does NOT lock editing — entries can be added/updated after signing, and Unsign removes the signature; "No work done" toggle (moon icon) marks a no-work day and **still generates a report entry**.
- **Back-entry**: log or edit entries for any previous date via date navigation.
- **Weather**: captured automatically from the project's street address (dedicated article: Raken Automatic Weather Capture).
- **Configurability**: report sections toggled per project (Project Settings > Daily report settings); Segmented Daily Reports (segments per area/phase, with setup/view/download articles); logo and cover-photo branding; hours-to-date tracking; transfer daily reports between projects.
- **Compliance machinery**: "Set Up Daily Reminders" and "Find Missed Daily Reports" articles under a collection literally named **Managing Report Compliance** — the product actively polices that a report exists for each day.
- **Platform breadth** (collection map): Time Tracking (44 articles), Production (11), Safety & Quality (16), RFIs & Submittals (4), Tasks & Messaging (3), Scheduling & Certs, Directory, Photos & Attachments, Forms & Documents (2), Integrations (37). Daily reporting has **no plan restriction**; role required: Project Member and above.

## Product C — HCSS HeavyJob

### Key observations (Layer A product-page FAQ + vendor video transcript; Tier-2 pages)

- Positioning: "Construction Daily Report Software — Know what's happening on every jobsite"; "The field-friendly interface allows your foremen to easily log daily events and helps project managers get a better idea of what's going on at the jobsite."
- **FAQ definitions** (vendor's own category definition): "Construction daily log reporting software creates a digital record of everything that happens on the jobsite each day" — capturing labor, equipment, materials, weather, progress, issues; a daily report includes who worked and for how long, equipment and materials used, weather conditions, delays, safety issues, photos, and notes; daily logs "reduce disputes and risk by creating a time-stamped record of jobsite activity… providing clear evidence to support decisions, resolve disputes, and protect against claims"; logs feed job costing and productivity tracking; digital logs improve on paper by real-time entry, photos, and searchable standardized reports.
- **Field Diary video transcript** (operational detail): the field app presents Diary, Photos, and Time card together; a diary entry starts with **working conditions** free text (talk-to-text supported) and can pull geo-tagged location information; **customizable tags** (material delay, equipment breakdown, subcontractor issue) classify entries so reports can be run against them ("how many times I've had a subcontractor issue on the job site"); general **notes** form a "daily digest" management reads "the same way you would a newspaper"; the diary is **submitted together with the time card**.
- **Feature list on the HeavyJob page** (named capabilities): Project management, Time cards, Job costing, Budget & forecasting, Material tracking, Map view, Field productivity, T&M billing, **Daily field reporting (DFR)** — "customizable templates to easily document work completed, report to owners on work progress, and get sign-off from inspectors or owner representatives" — and **Daily log** — "easy management review of all daily activities, photos, and progress"; plus Construction forms and accounting/payroll integrations.
- Segment: self-performing civil, infrastructure, and utility contractors; crews/foremen enter time cards, quantities, and daily logs from mobile devices, working offline ("with or without an internet connection… sync it later"). Marketing metrics (user counts, ROI claims) are not evidence for canonical structure.

## Product D — PlanRadar

### Key observations (Layer A help center + Tier-2 product page)

- **Product page** (marketing): "Site diaries" is a named capability in every customer-pole pitch (general contractors: "digitally documenting all construction processes"; consultancies; owners: "secure storage & archiving of project information"; specialty contractors), listed beside defect management & snagging, inspections/checklists/safety audits, handovers, and "evidence collection & claims management".
- **Help center** (form mechanics): forms are assigned to projects and "enable the creation of tickets"; the docs use **"Daily Site Log"** as their example form name; per-project form configuration includes mandatory fields and **assigned lists** (e.g. a **Weather** list with values such as "Snow"; a "Submittal type" list), multi-selection options, and per-form **approval workflows**; a form cannot be removed from a project while tickets created from it exist.
- Sample ticket-report template library includes **"Site diaries"** as a report family — the diary renders as a formatted report from recorded tickets/entries.
- Structural reading: PlanRadar's primary object is the ticket (defect/inspection/observation); the site diary is realized **as a form-driven, dated record + report template** rather than a dedicated structured-log tool — a different realization of the same day-record concept. Search-result snippets show the platform's use cases as "defect tracking (snagging) on a construction site; site reports; managing recurring tasks".

## Product E — Fieldwire by Hilti

### Key observations (Layer A help-center search results this pass + sibling-run Layer A notes, 2026-09-07)

- "Introduction to 'Daily Report' Forms": "Daily Reports are designed to document your daily work activity in a convenient and straightforward [way]" — the day record exists as a **form template** instantiated per day.
- The Forms tab hosts Daily Reports alongside Inspection Requests, Timesheets, Safety Audits, and Time & Material Tag forms; the Custom Form Builder can edit Fieldwire's daily reports, timesheets, inspection requests, and safety audits.
- Form mechanics surfaced in search snippets: reports carry **sequential numbers** (Q&A on resetting form numbers when "Daily Report #3" is deleted); a daily report can be **reassigned** to another person, who receives a notification when the report is submitted.
- Sibling-run evidence (same week): Fieldwire digitizes "daily reports, timesheets, inspection requests, and RFIs" as forms; its own navigation splits Field management (tasks, punch, inspections) from Project management (RFIs, submittals, budget); daily reports export as PDF (summary/detailed), with scheduled reports.

## Cross-product Comparison

| Dimension | Procore | Raken | HCSS HeavyJob | PlanRadar | Fieldwire | Reading |
|---|---|---|---|---|---|---|
| Day-record realization | structured log tool with ~20 typed entry sections | daily report with toggleable sections | diary entries + tags + notes, tied to time cards | "Daily Site Log" form → tickets + report template | "Daily Report" form template | Common object; realization varies (typed log / sections / diary / form) |
| Day anchoring | calendar/list of days; day or date range; segments per day | today's log opens automatically; date strip; no-work day still yields an entry | diary submitted per day with the time card | tickets dated; diary renders per period via report templates | sequentially numbered daily report forms | Common; day-anchoring is constant |
| Content sections | work log, manpower, equipment, deliveries, visitors, calls, delays, notes, quantities, productivity, safety, accidents, waste, dumpsters | work logs **by company**, notes, attachments, time cards, survey questions (delays), safety & QC | working conditions, tags, notes, photos; labor/equipment/materials via time cards & quantities | form fields with lists (weather list etc.) | form-defined fields | Work performed + labor + conditions + events constant; exact vocabulary varies |
| Authorship | superintendent/field worker; subcontractor collaborator entries pending approval; owner tutorials exist | field crews; work logs organized per company; Project Member+ | foremen; talk-to-text; geo-tagged location pull | form assignees; approval workflows | form assignee, reassignment with notification | Field-made, attributed; multi-party participation common |
| Weather | service/on-site-station auto + manual observed-weather entries; service row read-only | automatic from project address | FAQ lists weather among captured items | weather list field (manual) | form field | Auto-capture common in modern products, not universal |
| Completion act | Mark as Complete / Re-Open; change history | Sign & complete; Unsign; editable after signing | submit with time card | approval workflow on tickets/forms | submit; assignee notified | Common: a deliberate completion act; lock semantics vary |
| Distribution | Email Daily Log; PDF export; canned/custom reports | automatic PDF distribution to configured recipients on completion | DFR reports to owners with inspector/owner-rep sign-off | ticket report templates (site diaries) | PDF summary/detailed reports | Common; the report is the output artifact |
| Compliance machinery | pending-entry approval queue; action-oriented emails | daily reminders; missed-report finder ("Managing Report Compliance") | not surfaced on sampled pages | approval workflows | not surfaced | Common in daily-report-led products |
| Photos/attachments | photos populate project Photos tool | attachments per section; cover photos | photos in diary; map view | photos in tickets | photos on forms | Common |
| Time capture | timecard entries beside Timesheets tool | time cards section | time cards are the spine (diary submitted with time card) | not surfaced | timesheets forms | Common but depth varies; not definitional |
| Quantities/production | quantity + productivity entries; quantities → budget | Production collection | core spine (quantities, job costing, T&M) | not surfaced | not surfaced | Variant (heavy-civil/progress tradition) |
| Adjacent registers in-product | inspections, safety violations, accidents as entry types; related items across tools | safety & quality, RFIs & submittals, tasks modules | construction forms; HCSS Safety sibling | defect/snagging tickets, inspections, approvals | punch, inspections, RFIs, submittals | The log sits beside work-item registers; adding them → field management |
| Segment | enterprise GC/owner | SMB GC/subs | heavy-civil self-perform | European mid-market/consultancy | mid-market GC/specialty | Distinct tiers/geographies, one structure |

## Canonical Model (Layer C synthesis)

The Type holds one object: **the project day record** — a dated, per-day account of one construction project's site activity and conditions, composed of attributed entries, accumulated as a chronological series across the project's life. What a day holds is broadly stable (work performed, labor and by whom, equipment, materials/deliveries, weather, delays, notable events, notes) while the section vocabulary is configurable and varies. The record is written by the people running the work (superintendents, foremen, field engineers, crews, sometimes subcontractor collaborators pending approval), not by office staff, and it exists as the project's contemporaneous account **for its parties** — the office, the owner, inspectors, and, when disputes arise, the record that supports or defeats claims. A deliberate completion act (mark complete / sign & submit) closes the day; mature products then render and distribute a formatted daily report (PDF/email, often automatically to configured recipients), and daily-report-led products police completeness with reminders and missed-report tracking.

Around this core, products add: photo/attachment evidence flowing to a project photo store, automatic weather capture, time cards and production quantities (depth varies by segment — payroll-grade in the heavy-civil pole), per-company labor attribution, segments (splitting a day by area/phase), change history, calendar/list/date-range browsing, and role-scoped participation. The Type is deliberately the day record only: the field work items (punch/issue/task registers), inspection checklists, and safety case machinery that typically appear in the same products belong to Construction Field Management and its sibling Types.

## L0 — Defining Invariant (minimal)

A Daily Log Application is recognizable when it provides, for a construction project/site:

1. **The project day record** — a dated, per-day record of that project's site activity and conditions, composed of attributed entries (who recorded, about what, when; commonly company/location), accumulated as a chronological series over the project's duration.
2. **Site-work authorship with an accountability purpose** — entries are made by/for the people running the work on site, as the project's contemporaneous account for the project's parties (the office, the owner, inspectors), not as private reflection and not as office-authored reporting.

Removal tests: remove the per-day anchoring → a notes app or photo library; remove the project/site-work anchoring → a personal journal/diary app; remove the accumulation → a status-update feed; remove the field authorship/accountability → an office progress report. Addition test: add field work items tracked to verified completion → Construction Field Management; add schedule/cost/contract machinery → Construction Project Management. Historical check: the superintendent's paper daily report book / site diary / foreman's hard book (HCSS testimonial: "a lot of people are still old school… they have a hard book, and they put everybody's time down") satisfies both properties without any software; HCSS's own FAQ frames the digital product explicitly against "paper logs". The Type predates its software and is not defined by weather auto-capture, signatures, PDF distribution, mobile apps, or cloud sync.

Deliberately NOT definitional: typed entry-section catalogs, weather automation, signatures/lock semantics, PDF/report formatting, time cards, quantities, photos, segments, reminders/missed-report tracking, per-project configurability, mobile/offline, cloud, integrations.

## L1 — Common Mature Structure

- **Domain sections/entry types for the day**: work performed (work logs), labor/manpower organized per company, equipment, materials/deliveries, weather, delays, safety events, notes; visitors, calls, waste, dumpsters in some catalogs; production quantities and time cards in some traditions. Section sets are configurable (toggleable sections, custom fields, survey questions).
- **Day lifecycle**: open during the day → deliberate completion act (Mark Complete / Sign & complete / submit) → distribution; re-open/unsign and post-completion edits with change history; copy-previous-day; back-entry for past days; calendar/list/date-range views.
- **Reporting outward**: formatted daily report (PDF), email to configured recipients, automatic distribution on completion in daily-report-led products; branding (logo/cover).
- **Compliance machinery**: daily reminders, missed-report identification, approval queues for collaborator-submitted entries, pending-entry states.
- **Attribution machinery**: author, company, location, timestamp on entries; per-company organization of labor.
- **Photo/attachment evidence** flowing into a project-wide photo store.
- **Role-scoped participation**: field authors, collaborators who submit pending approval, office/owner readers and recipients.

## L2 — Variant / Optional Structure

- Product pole: pure-play daily-report application (Raken) vs platform module (Procore Daily Log) vs time-and-quantity-led field-suite feature (HCSS HeavyJob) vs form/ticket realization on a documentation platform (PlanRadar) vs form-template layer in a field-first tool (Fieldwire).
- Realization of the day record: structured typed-entry log vs report sections vs configurable form.
- Weather: automatic capture (by address / weather service / on-site station) vs manual fields.
- Time capture depth: payroll-grade crew time cards inside the log (heavy-civil pole) vs lightweight timecard entries vs none.
- Quantities/production tracking and job-costing linkage (heavy-civil/progress-billing tradition).
- Segments (splitting a day by area/phase/company), survey/custom questions, custom fields.
- Adjacent registers hosted in the same product (safety, quality, RFI/submittal, punch) — depth of hosting varies; full work-item machinery → Construction Field Management.
- Voice capture/talk-to-text, geotagged entry creation, offline capture with sync.
- Owner-side daily logs (owner representatives keeping their own logs).
- Regional/naming variance: daily log / daily report / daily field report (DFR) / site diary / construction diary.

## L3 — Vendor-specific Structure (research notes only)

- Procore: ~20-entry-type catalog (incl. Dumpster, Waste, Plan Revision); Dark Sky-class weather service or on-site station with read-only service-filled weather rows; segments (recent addition); customizable log names; Quick Create; bulk delete; related-items machinery; action-oriented emails; owner-facing configuration tutorials; calendar limited to past dates; custom fields; granular per-tool permissions.
- Raken: moon-icon no-work toggle; automatic weather from project street address; cover photos/logo branding; rich-text formatting plan-gated; transfer daily reports between projects; hours-to-date tracking; segments; "Managing Report Compliance" collection (reminders + missed reports); sign/unsign semantics.
- HCSS HeavyJob: Field Diary + Photos + Time card triad; customizable job tags with reportable categories (material delay, equipment breakdown, subcontractor issue); "daily digest" notes metaphor; talk-to-text; geotagged location pull; Daily Field Reporting with inspector/owner-representative sign-off; diary submitted with the time card; job costing/T&M/payroll integration spine; marketing metrics (140,000 daily time cards claim, 7–9 minutes average in-app) — not evidence.
- PlanRadar: site diary as a form assigned per project with mandatory fields, list fields (Weather with values like Snow; Submittal type), multi-selection, per-form approval workflows, tickets as records, site-diary report templates in a sample library; removal of a form blocked while tickets exist.
- Fieldwire: Daily Report form template with sequential numbering (and Q&A on renumbering after deletion); reassignment of a report with submission notifications; custom form builder editing the daily report; forms tab grouping daily reports with timesheets, inspection requests, safety audits, T&M tags.

## Boundary Findings

- **vs Construction Field Management** (the load-bearing boundary): the sibling pass's L0 states "Remove the work items → only a Daily Log Application remains", and its related-types table lists this Type as "subset: keeps only the day-anchored site record, without the integrated work-item/inspection machinery". This pass confirms from the log side: every sampled product's daily-log center contains no work-item lifecycle (raise → assign → respond → verify → close); where such registers exist in the same product they are separate objects/tools. **Add field work items tracked to verified completion → Construction Field Management; keep only the day record → this Type.** Both documents cross-reference.
- **vs Construction Project Management**: the PM pass flagged Daily Log (with RFI, Submittal, Punch, Quality, Safety) as "realized as modules inside PM platforms (each remains a legitimate point Type)". Discharged from this side: the daily log has no schedule, cost, contract, or change objects of its own; Procore/PlanRadar evidence shows it living as a tool inside the project container. **Remove the day record and keep schedule/cost/contracts → Construction Project Management.**
- **vs Construction Safety Management**: safety events appear as daily-log entry types (Procore Safety Violation/Accident entries; Raken Safety & QC section; HCSS FAQ lists safety issues), and the safety pass recorded incident→daily-log summary interlocks. But the daily log carries no incident register, investigation, or corrective-action lifecycle — **keep only safety records with their machinery → Construction Safety Management.**
- **vs Construction Labor Management / Employee Time Clock / Time & Attendance**: time cards live inside the daily log in several products (Procore timecard entries; Raken time cards; HCSS diary-with-time-card), but the log's center is the day's account, not the workforce or payroll. **Center the crew population/time/payroll → those Types.** HCSS demonstrates the time-led pole where the log is one feature of a time-card-and-quantities spine.
- **vs Construction Equipment Management**: equipment entries in a day record are the seam; centering the machine population (maintenance, availability, telematics) → that leaf.
- **vs Construction Reality Capture Platform**: photos inside entries are evidence; capture-first, spatially anchored visual accumulation → Reality Capture.
- **vs Construction Quality Management / Property Inspection Application**: an "Inspection" entry type records that an inspection happened; the checklist/NCR/inspection-run machinery belongs to the quality/inspection Types.
- **vs Note-taking Application / consumer journaling**: name collision ("daily log"). A generic notes or journal app lacks the project/site-work anchoring, entry attribution, project parties, and reporting/accountability machinery. The directory scopes this leaf to the Construction family; the Type is construction-scoped by placement and by the researched population.
- **vs Construction Document Management**: the distributed daily report is a document output; the controlled register/drawing revisions live in document management. The log is the living day record, not a controlled-document system.

## Uncertainties

- **Raken marketing site 403** — product positioning rested on its help center (Tier-1) alone; acceptable because the help center is explicit and detailed.
- **NoteVault (voice-first daily reporting pole) and Buildertrend (residential-builder pole) unreachable** (NoteVault transport errors ×2 in the same-week sibling run; Buildertrend 403 + help timeout). The voice-capture and residential traditions are therefore not directly documented; no claims made about them.
- **Autodesk Construction Cloud / Build daily logs unreachable** (consistent with sibling runs) — the "suite-embedded module" pole beyond Procore is not independently evidenced; the module-vs-standalone variant claim rests on Procore plus PlanRadar/Fieldwire/HCSS as non-Procore realizations.
- **Completion/lock semantics vary** (Procore mark-complete/re-open with change history vs Raken sign/unsign with post-signature editing): the canonical claim is only that a deliberate completion act exists; no claim about immutability.
- **"A report entry for every day" cadence**: evidenced directly in Raken (no-work day still generates a report entry; reminders; missed-report finder) and suggested by Procore's approve/pending machinery; not asserted as universal.
- **Historical check is reasoning-based**: paper daily report/site diary traditions satisfy the L0 pair, supported by HCSS's explicit paper-vs-digital framing and testimonials referencing paper "hard books"; no pre-digital product sample was researched directly.
- HCSS and PlanRadar product pages are Tier-2 marketing; their operational details were corroborated where possible by the vendor's own video transcript (HCSS) and help center (PlanRadar).

## Final Synthesis

A Daily Log Application is the construction project's day-record system of record: a dated, per-day, attributed account of site activity and conditions — work performed, labor organized by company, equipment, materials and deliveries, weather, delays, safety events, notes — written by the people running the work and accumulated as the project's contemporaneous memory. The day is held open while work happens, closed by a deliberate completion act (mark complete or sign), and rendered into a formatted daily report distributed to the project's parties, with daily-report-led products adding reminders and missed-report tracking to enforce the one-record-per-day cadence. Realizations range from structured typed-entry log tools (Procore) through sectioned mobile daily reports (Raken), time-card-joined field diaries (HCSS HeavyJob), form-driven site diaries on documentation platforms (PlanRadar), and daily-report form templates (Fieldwire) — the section vocabulary is always configurable and never definitional. The defining core is exactly two properties — the project day record and field-made authorship with an accountability purpose — and the boundary logic is subtraction: add field work items tracked to verified completion and it becomes Construction Field Management; add schedule/cost/contract machinery and it is Construction Project Management; keep only safety, labor, equipment, or capture and it is those Types. The paper daily report book and site diary satisfy the core unchanged, which is why the definition does not depend on weather automation, signatures, PDF distribution, or mobile capture.
