# Research Notes — Construction Field Management

## Research Goal

Understand what "construction field management" software actually is as an Application Type: what objects it holds, who uses it, how daily site work is recorded and directed, how field-raised items reach verified completion, and where it begins and ends relative to the many single-function construction leaves around it (Daily Log, Punch List, RFI, Submittal, Quality, Safety, Labor, Equipment).

## Initial Boundary

Working hypothesis at start:

- Construction Field Management is the **site-execution layer** of construction software — what superintendents, foremen, field engineers, and subcontractor crews use on site day to day — as opposed to the office-side layer (scheduling, cost, contracts, document control).
- Expected core objects: the daily log (weather / manpower / equipment / deliveries / events), field-raised work items (issues / punch / tasks), inspections and checklists, safety records, photos, and time capture.
- Nearest neighbors: Construction Project Management (umbrella), Daily Log Application, Punch List Management, RFI Management, Submittal Management, Construction Quality Management, Construction Safety Management, Construction Labor Management, Construction Equipment Management, Construction Reality Capture, Construction Document Management, Property Inspection Application.
- Main risk: this may be an **umbrella / suite-level Type** whose "features" are themselves separate directory leaves — the defining core must be drawn so the umbrella does not swallow its children.

## Research Questions

1. What objects exist in a field-management product (day record, work item, inspection, safety record, time, photo, plan)?
2. What is the core loop: record site conditions → raise/assign items → resolve → verify → report?
3. Who are the users and how do GC, subcontractor, owner roles differ?
4. What is mobile-first about it (offline, photos, quick capture, notifications)?
5. Is the daily log definitional or common? Are plan/location anchoring, photos, timesheets definitional or common?
6. How do the single-function leaves (punch, RFI, quality, safety) relate — integrated modules or separate Types?
7. What did field management look like before software (historical/market-sample check)?
8. Does the market itself use "field management" as a product category, and how do vendors draw the field vs project line?

## Representative Products

Selected for market representativeness, documentation depth, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier | Evidence depth |
|---|---|---|---|
| Procore | Enterprise construction platform; field tools as one tool grid among financials/PM | Enterprise GC / owner | Tier-1 support docs, deep (tool landing pages) |
| Fieldwire by Hilti | Field-first standalone; explicitly markets "field management" vs "project management" | Mid-market GC + specialty contractors | Tier-1 help center + Tier-2 product pages |
| Assignar | Subcontractor field-operations platform ("field to finance"); labor/crew-scheduling spine | Self-perform subcontractors (civil, concrete, crane, rail) | Tier-2 product pages (marketing-descriptive) |

Market anchors acknowledged but **not directly documented this run** (fetch failures — see Sources / Uncertainties): Autodesk Construction Cloud (Autodesk Build), Raken (daily-report-led SMB), NoteVault (voice daily reporting), PlanGrid heritage. No claims are made from these.

## Sources

Research date: **2026-09-07**

- Fieldwire by Hilti — https://www.fieldwire.com/ (product nav: Field management / Project management / Plans and BIM / Reporting)
- Fieldwire by Hilti — https://www.fieldwire.com/punch-list-app/ (punch process, two-step verification, regional naming)
- Fieldwire by Hilti — https://help.fieldwire.com/hc/en-us (help center category map)
- Fieldwire by Hilti — https://help.fieldwire.com/hc/en-us/articles/360003458332-Introduction-to-Tasks (task model)
- Procore — https://support.procore.com/ (project tool grid incl. Daily Log, Punch List, Inspections, Incidents, Observations, Action Plans, Coordination Issues, Tasks, Crews, Timesheets, Photos, Forms, T&M Tickets)
- Procore — https://support.procore.com/products/online/user-guide/project-level/daily-log (Daily Log tool)
- Procore — https://support.procore.com/products/online/user-guide/project-level/punch-list (Punch List tool)
- Procore — https://support.procore.com/products/online/user-guide/project-level/inspections (Inspections tool)
- Assignar — https://www.assignar.com/ (operations platform: scheduling, time tracking, forms & field data, safety & compliance, reporting, integrations)

Source-access limitations: support.fieldwireapp.com (transport error), rakeapp.com ×2 (403), autodesk.com ×2 + help.autodesk.com (403/empty; consistent with an earlier same-week sibling run), notevault.com ×2 (transport error). Per network rules these were abandoned after retries; findings relying on them are not asserted. Assignar evidence is marketing-descriptive (Tier 2), so Assignar-specific structural claims are kept qualified.

## Product A — Procore

### Key observations (Layer A — support-site content unless noted)

- The support tool grid names the field-side project tools explicitly: **Daily Log, Punch List, Inspections, Incidents, Observations, Action Plans, Coordination Issues, Tasks, Crews, Timesheets, Photos, Forms, T&M Tickets, Drawings** — alongside office-side tools (Budget, Commitments, Prime Contracts, Progress Billings, Change Events, Submittals, RFIs, Schedule, Specifications).
- **Daily Log**: "central location for viewing, tracking, and emailing updates about daily project activities". Entry types evidenced by tutorial list: Accident, Daily Construction Report, Delay, Delivery, Dumpster, Equipment, Inspection, Manpower, Notes, Observed Weather, Phone Call, Plan Revision, Productivity, Quantity, Safety Violation, Scheduled Work, Timecard, Visitor, Waste, Work Log. Weather auto-populated from a weather service or an on-site station (vendor detail). Day-anchored mechanics: log for a day or date range, calendar view, "Mark a Daily Log as Complete", "Re-Open", "Copy a Daily Log", enter logs for a previous day, segments (multiple logs per day), change history, email/export PDF/canned reports, approve/reject pending entries submitted by collaborators (subcontractors), custom fields, granular permissions.
- **Punch List**: "used at the end of a project to keep track of remaining items to complete, assign responsibility, and maintain due dates". Create (manual, from drawing, Quick Capture on mobile, templates, import), assign, due dates, overdue email notifications, respond, resolve (subcontractor as collaborator), close / accept-and-close (superintendent/admin), statuses (open / closed / pending), comments, photos (populating the Photos tool), attachments, change history, recycle bin, dashboards, CSV/PDF export, multi-tiered locations, item templates and categories, distribution groups, private-by-default items, punch-item color codes on drawings, permissions matrix (None / Read Only / Standard / Admin).
- **Inspections**: reusable checklist templates (company level → project level), sections + line items, conditional logic, templates that require photos/observations, inspection schedules (incl. by equipment), perform on mobile (per-item responses, comments, photos, attachments, contacts), signers/signatures, close, reinspect closed inspections, create an Observation from an inspection, related items, location filtering, exports/reports, map view. Template library examples span quality (pre-pour, pre-drywall, pre-backfill), safety (OSHA trenching, lockout/tagout), site safety inspections, environmental (SWPPP stormwater), equipment pre-operation — one checklist engine serves quality/safety/environmental.
- Cross-object machinery: "related items" link records across tools; photos populate a project-wide Photos tool; locations are a shared multi-tiered taxonomy; granular permissions per tool; collaborator model gives subcontractors scoped mobile participation (view / respond / resolve / submit entries for approval).

## Product B — Fieldwire by Hilti

### Key observations (Layer A — help center + Layer A/B for product pages)

- The product's own navigation splits: **Field management** (Task management, Scheduling, Punch list, Inspection) vs **Project management** (RFIs, Submittals, Change orders, Budget, Document management, Specifications) vs **Plans and BIM** (Plan viewing, As-built drawings, BIM viewer) vs **Reporting** (Reports, Forms). Self-labeled "the field-first tool for the jobsite" / "jobsite management". This is direct vendor evidence of the field-vs-project split used in this research.
- **Tasks** (help article, Layer A): a catch-all field object covering "QA/QC issues, inspection observations, punch items or deficiencies, safety issues, RFIs and change orders, work progress, delays, design and pre-con coordination, variations, general communication". Created by pinning to a plan sheet. Attributes: unique task number, title, status (default or custom), category, assignee, plan link, nested location, start/end dates with due-date reminders, cost, tags, watchers, custom attributes (plan-gated). Content: timestamped comments/messaging, checklists (from templates, initials + date per item), attachments (photos → Photos tab, files, forms with status, RFIs, crop plans, 360° photos, links), related tasks, history. Export/email as PDF; QR codes for tasks/punch (print & scan on site); task importer; trash/recovery; create-task permissions for member/follower roles.
- **Punch** (product page): walkthrough-driven deficiencies; each item carries plan location + photos, checklists, categories, hashtags, due dates; assign to trades; **two-step verification** — a party can mark complete while only a verifying role (e.g. the architect/GC) can verify true completion; PDF reports auto-generated and distributed; templates for common deficiencies duplicated across locations; closeout orientation. Regional naming on the same page family: snag list (UK/AU/IE), réserves (FR), Mängelliste (DE), opleverlijst (NL), anmärkningslista (SV).
- **Forms / daily reports**: forms digitize "daily reports, timesheets, inspection requests, and RFIs" — i.e., the day record is form-realized rather than a structured log object. Plans tab with versioning, offline markups, as-builts; mobile apps (iOS/Android) + web; real-time task messaging; reports incl. scheduled PDF reports.

## Product C — Assignar

### Key observations (Tier-2 marketing-descriptive; treat structure claims as qualified)

- Self-positioned as "the construction platform that connects Field to Finance" for **self-perform subcontractors** (asphalt, concrete, piling, excavation, rail, crane, scaffolding, traffic, demolition…).
- Feature spine: **crew & equipment scheduling** (drag-and-drop calendar, qualification/availability, notify, extend orders, remove workers), **time tracking** (mobile clock in/out, worker timesheets, supervisor completes timesheets for a whole crew, activities and breaks), **digital forms** filled from the field for regulation/compliance, **safety and compliance**, **job costing**, **schedule of rates / T&M**, **pay rates**, **reporting & analytics**, **integrations** to ERP/accounting ("without double-entry"), and progress tracking (LPS-based).
- Day-record form: labor time per day via timesheets; field evidence via photos and forms; no structured weather/manpower diary surfaced on the sampled pages — consistent with the labor-operations pole rather than the building-superintendent pole.

## Cross-product Comparison

| Dimension | Procore | Fieldwire | Assignar | Reading |
|---|---|---|---|---|
| Day-anchored record of site activity | structured Daily Log tool (weather/manpower/equipment/deliveries/…) | daily reports via Forms + task activity + reports | timesheets + forms (labor-centric) | Common; structural form varies |
| Field work item tracked to verified closure | Punch List + Tasks + Coordination Issues (respond→resolve→close/accept) | Tasks as catch-all incl. punch; two-step verify | forms-based (weaker as first-class) | Common; strongest in building-side products |
| Inspections / checklists from templates | Inspections tool (schedules, signers, reinspection) | Inspection app + task checklists + forms | compliance forms | Common |
| Safety records | Incidents, Observations, Action Plans, safety-violation log entries | safety issues as tasks; safety forms | safety & compliance module | Common |
| Time capture | Timesheets tool + daily-log timecard entries | timesheets via forms | core capability (crew timesheets) | Common; depth varies by pole |
| Plans / drawings in the field | Drawings tool (mobile) | Plans tab is the product's backbone | not surfaced | Common in building projects; not universal |
| Location anchoring | multi-tiered locations across tools; drawings; maps | plan pinning + nested locations | jobs/crews rather than building locations | Common; realization varies by segment |
| Photos as evidence | photos across tools → Photos tool, quick capture | photos on tasks/plans, 360° support | photographic evidence | Common |
| Multi-party participation | collaborator (subcontractor) submissions + approvals | assignees/trades, watchers, verify roles | crews + supervisors + office | Common |
| Reporting outward (PDF/email) | daily-log/punch/inspection reports, exports | PDF reports, scheduled reports, QR/print | shareable reports | Common |
| Notifications / mobile-first | mobile apps, quick capture, push | mobile apps, offline markups, reminders | mobile app for crews | Common |
| Crew & equipment scheduling | Crews tool; not the center | task-level scheduling (lean) | core capability (drag-drop calendar) | Variant (pole-defining for Assignar) |
| RFI / submittal registers in-product | yes (own tools) | yes (project-management group) | not surfaced | Common in suites; their workflows are separate Types |
| Structured daily-log object vs form-based day record | structured object | form-based | timesheet/form-based | Variant |

## Canonical Model (Layer C synthesis)

The Type is the **site-execution layer of construction delivery**. Two primitive structures carry it:

1. **The field day record** — a project-scoped, day-anchored record of what happened on site (work performed, labor/time, weather, equipment, deliveries, visitors, calls, notable events, quantities in some traditions), produced by field personnel and reportable outward. Historically: the superintendent's daily report book.
2. **The field work item** — a deficiency / issue / task raised from the field, attributed (location on the work, responsible party, due date, category, evidence photos), tracked through assignment and response to **verified completion** (two-sided: doer completes, a verifying party accepts), and reportable. Historically: the punch list on a clipboard and the foreman's issue list.

Around these: inspections/checklists (recurring structured record sets with sign-off), safety records, time capture feeding payroll, plan/location anchoring for building work, photos as evidence, and outward reporting (PDF/email) that keeps the office, owner, and architect informed. The unifying property is that records are made **at the workface, by the people running the work**, tied to the project and its locations, and flow **outward** to the office/parties — the reverse of office systems that push work orders down.

## L0 — Defining Invariant (minimal)

A Construction Field Management application is recognizable when it provides, for a construction project:

1. **A project-scoped, day-anchored record of site activity**, created and maintained by/for the people running the work on site (the daily log/diary; a day-anchored time record satisfies the minimal form).
2. **Field-raised work items** (deficiency/issue/task) attributed to the project's work, assigned to a responsible party, and tracked to verified completion.

Remove the day record → only work-item registers remain (Punch List Management / Task Management). Remove the work items → only a Daily Log Application remains. Remove the site/field framing (field personnel recording site work on a construction project) → generic task management or project management. Historically, the paper daily report + clipboard punch list + foreman's issue list satisfy both invariants — the Type predates its software and is not defined by photos, plan pinning, mobile apps, notifications, or cloud sync.

Deliberately NOT definitional: structured daily-log sections (weather/manpower/…), plan/drawing anchoring, multi-tiered building locations, photo evidence, mobile/offline, notifications, inspections machinery, safety modules, timesheet→payroll, integrations, cloud delivery, any approval depth.

## L1 — Common Mature Structure

- Day record with **domain sections** (weather, manpower, equipment, deliveries, visitors, calls, delays, safety events, notes; production quantities in some products), entry approval for collaborator-submitted records, mark-complete/reopen, copy-previous-day, change history.
- Work items with **status lifecycle and verification** (open → respond/resolve → verify/close; two-step verification where the verifier ≠ doer), due dates, overdue notifications, reassignment, templates/categories, watch/subscribe.
- **Location anchoring** — pinning to plan sheets and/or a multi-tiered location taxonomy; punch color-coding on drawings.
- **Photos/attachments as evidence**, flowing into a project-wide photo store.
- **Inspections/checklists** from reusable templates with sections, conditional logic, schedules, signers/signatures, reinspection; one engine serving quality, safety, and environmental checklists.
- **Safety records** — incidents, observations/unsafe-condition reports, safety violations, toolbox/safety-meeting records.
- **Time capture** — worker/crew timesheets from the field feeding payroll.
- **RFI/submittal registers** present in the same product (workflows documented under their own Types).
- **Reporting outward** — PDF/email of daily reports, punch logs, inspection results; scheduled reports; export.
- **Mobile-first capture** — phone/tablet apps, quick capture from photos, offline work, push notifications.
- Multi-party participation model (GC ↔ subcontractor collaborators ↔ owner/architect readers) with scoped permissions and audit history.

## L2 — Variant / Optional Structure

- Product pole: field-first standalone (tasks+plans center) vs suite-embedded field module vs subcontractor field-operations platform (crew/equipment scheduling + time + forms spine).
- Segment: building/GC projects (plan-anchored, punch-centric) vs civil/self-perform trades (crew/job-anchored, labor- and compliance-centric).
- Day-record realization: structured log object vs digitized forms vs timesheet-only.
- Crew & equipment scheduling as a first-class capability (some products center it; others offer light scheduling of tasks).
- Regional vocabulary: punch list vs snag list (UK/AU) vs réserves vs Mängelliste vs opleverlijst.
- Reality-capture depth (360° photos, progress capture), QR/label attachment of physical site items to records.
- Plan gating (which modules ship at which tier), ERP/payroll/accounting integration depth, deployment (cloud SaaS dominant; mobile offline posture varies).

## L3 — Vendor-specific Structure (research notes only)

- Procore: weather auto-fill from a named weather service or on-site station; Daily Log segments (multiple logs per day, beta); punch-item color codes on drawings; "related items" machinery; Quick Capture; collaborator approve/reject queue; granular per-tool permission templates; recycle bin; distribution groups/lists; T&M Tickets and Direct Costs tools.
- Fieldwire: tasks-as-catch-all philosophy (RFIs, variations, delays all representable as tasks); crop-plan attachments; Hilti pre-printed QR label integration; 50 task-emails/day outbound limit; 255-character title cap; 30-day trash recovery; ≤20 custom task attributes; plan tiers (Basic/Pro/Business/Business Plus); "Field Intelligence" AI branding.
- Assignar: pay rates, schedule of rates (T&M), job costing, LPS progress tracking, Milo AI assistant, industry-specific products (CraneOps, TrafficOps, InfraOps).
- Marketing/customer anecdotes (EllisDon, Graham, Webcor quotes) — not evidence for canonical claims.

## Boundary Findings

- **vs Construction Project Management** (umbrella): PM owns schedule, cost, contracts, and the document register; field management owns the day record, field work items, inspections, safety, and time capture. Fieldwire's own nav ("Field management" vs "Project management") and Procore's tool grid (field tools beside financial tools) show vendors drawing the same line. **Keep schedule/cost/contract objects and drop the day record + field work items → Construction Project Management.**
- **vs Daily Log Application**: the daily log is one object of this Type. **Keep only the day record → Daily Log Application.** (Sibling-leaf boundary; recommend cross-reference when that leaf is processed.)
- **vs Punch List Management / RFI Management / Submittal Management / Construction Quality Management / Construction Safety Management**: each owns one register/workflow; field management is the integrating site-execution layer that commonly hosts them. **Keep only one register and its workflow → that leaf.**
- **vs Construction Labor Management / Construction Equipment Management**: those Types center the populations (people, machines); field management centers the day's work and its record. Assignar demonstrates the seam — its spine is crews/equipment/time; the day-record/work-item pair is thinner. **Primary object becomes the machine or workforce population → those leaves.**
- **vs Construction Reality Capture Platform**: photos inside field records vs capture-first progress documentation. **Capture becomes the primary object → Reality Capture.**
- **vs Construction Document Management** (sibling pass): plans are consumed/annotated in the field; the controlled register/revisions live in document management.
- **vs Property Inspection Application**: construction-phase inspections of work in progress vs post-occupancy building condition inspections.
- **vs generic Task Management / Project Management**: no construction objects (day record, punch verification, trades, building locations) → generic task tool.
- **Umbrella risk (taxonomy note)**: this leaf is a suite-level Type (like Work Management Platform). Its standard capabilities overlap the single-function leaves by design. "去掉什么就变成另一个 Type" 判据: remove the day record → Punch List/Task registers; remove work items → Daily Log Application; remove the site-execution objects while keeping schedule/cost → Construction Project Management; keep only inspections → Construction Quality Management; keep only safety → Construction Safety Management.

## Uncertainties

- **Autodesk Construction Cloud / Autodesk Build** could not be documented (403/empty across attempts, consistent with the same-week document-management run). Its field module is a known market anchor; no claims made. This also means the "suite-embedded field module" pole rests on Procore alone.
- **Raken / NoteVault** (daily-report-led SMB pole) unreachable; the SMB daily-report pole is evidenced only indirectly (Procore's structured Daily Log; Fieldwire's form-based daily reports). No SMB-market-specific claims made.
- **Assignar evidence is Tier-2 marketing-descriptive**; absence of a structured daily-diary object in Assignar is an absence-of-evidence observation, not a claim that the product lacks one. Its help center was not fetched.
- **Daily-log-as-L0-halves**: in the sampled products the two L0 invariants always co-occur; whether a market-viable product carries only the work-item half without any day-anchored record is untested. The boundary judgment (work-item-only → Punch List Management) is inference from the directory structure, flagged for joint review.
- **Precise status names** vary (open/pending/closed; complete/verify; approve/reject); canonical claim is the verification-to-closure discipline, not any label set.
- Historical check is reasoning-based (paper daily reports, clipboard punch lists, paper inspection checklists, toolbox-talk sign-in sheets satisfy the L0 pair); no pre-digital product sample was researched directly.

## Final Synthesis

Construction Field Management is the **site-execution system of record for construction projects**: a project-scoped, day-anchored record of what happened on site (the daily log — work performed, labor and time, weather, equipment, deliveries, events, commonly with sections, entry approval, and report export) plus the field work items raised from the workface (deficiencies, issues, tasks) that are attributed (location, responsible party, due date, evidence), assigned across the project's parties, and tracked to verified completion through a two-sided complete-then-verify loop. Mature products wrap these invariants with plan/location anchoring, photo evidence, template-driven inspections serving quality/safety/environmental checklists, safety incident/observation records, crew timesheets feeding payroll, RFI/submittal registers, mobile-first capture with offline and quick-capture, notifications, and outward PDF/email reporting that keeps office, owner, and architect informed. The market realizes the Type in three poles — field-first standalone (tasks+plans), suite-embedded field module, and subcontractor field-operations (crews/equipment/time spine) — and the boundary logic is subtraction: keep only the day record and it is a Daily Log Application; keep only one register and it is that leaf; keep schedule/cost/contracts and it is Construction Project Management.
