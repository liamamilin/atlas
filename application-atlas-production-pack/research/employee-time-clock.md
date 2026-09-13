# Research Notes — Employee Time Clock

Research date: 2026-09-06

## Research Goal

Understand what an Employee Time Clock application actually is and how it works in real products: what gets recorded, on what surfaces, how raw punches become approved payable hours, which roles act on the data, which rules govern the process, and where the Type's boundary sits against Time & Attendance, Time Tracking, Scheduling, and Payroll.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: employees record when work starts and stops ("punch in/out"); the system accumulates these events into per-employee time records used for manager approval and payroll.
- Likely users: hourly employees (punch), supervisors/managers (review, edit, approve), administrators (configure rules), payroll (consume).
- Nearest types: Time & Attendance System (broader system), Time Tracking Application (self-logged task time), Payroll System (downstream wage computation), Employee Scheduling Platform (plan vs actual), Workforce Management Platform (suite).
- Unknowns: exact punch mechanics per product; shared-terminal vs personal-device balance; rounding/overtime rule depth; approval workflow shape; payroll handoff mechanics; enterprise-tier behavior.

## Research Questions

1. What is a punch/time entry and what does it record (timestamp, direction, attribution, note, break)?
2. What clocking surfaces exist (shared terminal/kiosk, personal mobile/web, hardware, biometrics)?
3. How do raw punches become approved hours (timesheet assembly, rounding, overtime, exceptions, approval)?
4. What roles act on what, and what are the permission boundaries?
5. What rules/constraints govern punching (time windows, location restrictions, missed punches, buddy-punching prevention)?
6. How is the schedule related to punches (planned vs actual, late/absent detection)?
7. How does data reach payroll (export/integration/close period)?
8. Where is the boundary vs Time & Attendance / Time Tracking / Scheduling / Payroll?

## Representative Products

Selected for market representativeness, documentation quality, and different product philosophies:

| Product | Philosophy / tier | Why selected |
|---|---|---|
| When I Work | SMB, scheduling-led suite with Time Clock & Attendance module | deep public help center; shows schedule↔clock coupling |
| Jibble | Freemium, tracker-led, cross-tier (SMB→enterprise marketing) | deep public help center; strongest rule-engine documentation (rounding, overtime) |
| Deputy | Mid-market workforce management (AU/US), scheduling + timesheets + payroll | deep public help center; strongest timesheet-approval lifecycle documentation |
| Buddy Punch | SMB US hourly, time-clock-first product | official product/feature pages; anti-buddy-punching posture; kiosk + mobile + GPS |

Also attempted: Homebase (fetch failed twice — abandoned), QuickBooks Time (fetch timed out twice — abandoned), Rippling (JS-rendered help center — unusable), UKG/Kronos Community (JS-rendered — unusable), ADP (403). Enterprise HCM tier therefore not directly researched; see Source-access Limitation.

## Sources

Tier 1 (official operational documentation):

- When I Work Help Center — https://help.wheniwork.com/ ; category "Time Clock & Attendance" (https://help.wheniwork.com/article-categories/time-clock-and-attendance/); article "Clocking In and Out" (https://help.wheniwork.com/articles/clock-in-and-out/); category "Working with Timesheets" (https://help.wheniwork.com/article-categories/working-with-timesheets/)
- Jibble Help Center — https://www.jibble.io/help ; "How time rounding works" (https://www.jibble.io/help/how-time-rounding-works); "How does overtime work?" (https://www.jibble.io/help/how-does-overtime-work)
- Deputy Help Center — https://help.deputy.com/ ; category "Deputy Kiosk and Time Clock" (https://help.deputy.com/hc/en-au/categories/4614233183503-Deputy-Kiosk-and-Time-Clock); "What are the Deputy Kiosk/Time Clock apps?" (https://help.deputy.com/hc/en-au/articles/4877100522895-What-are-the-Deputy-Kiosk-Time-Clock-apps); category "Timesheets" (https://help.deputy.com/hc/en-au/categories/4614232027023-Timesheets); "Adding, editing and approving Timesheets" (https://help.deputy.com/hc/en-au/articles/6997348381327-Adding-editing-and-approving-Timesheets)

Tier 2 (official product pages):

- Buddy Punch — https://buddypunch.com/ (feature descriptions: kiosk PIN/facial recognition/QR, GPS, geofencing, IP locks, punch limiting, automatic clock-outs, photos on punch, timesheet approvals, automatic breaks, overtime policies, payroll integrations)

## Product Observations

### When I Work (evidence layer A — official help articles)

- Clocking surfaces: personal account on web/iOS/Android app; shared **Time Clock Terminal** = "a dedicated computer or mobile device at your workplace that is used solely for clocking in and out" (entrance, break room, central location); iOS **Photo clock in/out** (photo taken at clock in and clock out).
- Terminal identity: employee enters **employee ID or email** on the terminal.
- Employer-controlled punch restrictions: clock-in allowed only at assigned shift start time or within a configured window (5/15/30 minutes offered); "if you're too early, you may be unable to clock in"; clock-in may be restricted to a **specific physical address or IP address** ("if you're at the wrong location, you may be unable to clock in"); employer can **prevent clocking in when not scheduled**.
- Punch content: timestamp; if qualified for multiple positions → select **position** worked; may select **job site**; optional **clock-in/out note** for employer; **tips** entry at clock out (if enabled); **break attestation** at clock out (confirm breaks taken; provide reason if not).
- Breaks: employer enables break clocking between in and out.
- On-behalf clocking: supervisors/managers/admins can clock employees in/out (supervisors limited to employees on their own schedule).
- **Attendance notices** on dashboard: late clock in, forgot to clock out, clock in at wrong location, forgot to clock in; generated from attendance settings; last 7 days displayed.
- Timesheets: organized by **pay period**; employees can view own timesheet and edit only if employer allows and only in **open** pay periods; managers/supervisors/admins review and edit user timesheets.
- **Timesheet approval**: tracks which timesheets were checked for accuracy before closing the pay period.
- **Pay period close & export**: when a pay period ends, review and close it to prepare for export to payroll processor; open pay period = changes allowed (employees too, if allowed); closed = no changes unless reopened by admin/manager.
- Hours calculation: clock in/out recorded to hour and minute; seconds not recorded.
- Rounding: entries rounded to nearest 5/6/15 minutes; both rounded and actual entries can be exported; rounded entries can be sent to supported payroll integration.
- Timesheet history: when/how entry created, edits, who made changes; **map of clock in/out locations** when location restrictions enabled.
- Roles: Admins, Managers, Supervisors, Employees with distinct scopes.

### Jibble (evidence layer A — official help articles)

- Product family spans time clock software, attendance, kiosk, GPS, project time tracking; the time clock is one deployment of a timesheet engine.
- Clocking surfaces: mobile app, web, desktop app, Chrome extension, **shared kiosk** (QR code kiosk; kiosk mode on desktop app; Android app pinning; iOS Guided Access), **RFID/NFC**, **facial recognition** verification, offline attendance.
- **Time rounding**: adjust clock-ins, clock-outs, break times to pre-defined increments; methods to-nearest/up/down; configurable intervals (5/6/15/30 min offered); multiple rules per entry type with **effective date ranges**; rounding applied to **timestamps, not durations**; manual duration-only entries not rounded; timesheets show **Actual Time vs Rounded Time** side by side; **approved timesheets are not recalculated** by rounding; reopened timesheets recalculated per current rules; archived rules kept for reference.
- **Overtime**: rules configured under **work schedules**; types: daily OT, daily double OT, weekly OT, rest-day OT, public-holiday OT; each with threshold + multiplier rate; OT period ends at the workday **split time** (default midnight); weekly OT cannot be combined with daily/double/rest-day/holiday OT; unpaid breaks excluded from OT calculations; timesheet views (daily/weekly/monthly/detailed/payroll/pay-period) show OT hours; **payroll view** gives regular/OT breakdown and is editable; regional note: OT calculated differently when exporting to PayrollPanda (Malaysia Employment Act).
- Work schedules drive OT and can split timesheets for night work.
- Location settings: geofences can **restrict** clocking to locations or **automatically clock in/out** on entry/exit; GPS reminders.
- Reminders & **automatic clock out** (prevents forgotten clock-outs).
- Approvals: pay-period timesheet approvals; multi-level approvals for time off; timesheet vs project approvals distinguished.
- Integrations: timesheets sent to Xero, QuickBooks Online, Deel, PayrollPanda.
- Roles: Owners/Admins configure rules; managers approve; members track time.

### Deputy (evidence layer A — official help articles)

- **Deputy Kiosk/Time Clock apps**: "let your team clock in and out of their shifts from a shared device in the workplace. They record accurate start, break, and finish times and help managers verify attendance using **PIN login, facial recognition, or photo capture**." App generations: unified Deputy Time Clock (iPad/Android), legacy iPad Kiosk, legacy Android Time Clock, **Web Time Clock** (shared computer browser).
- Kiosk features across generations: offline mode (legacy iPad), voice/touchless clock-in, multi-language, employee self-service on kiosk (shift swap, unavailability, leave requests, tasks), micro-scheduling support, multi-location kiosk setup, shift visibility before clocking in.
- **Timesheet lifecycle**: statuses include **Pending**, **Absent**, time-approved, approved, **marked as paid**. Managers may edit only Pending or Absent timesheets; approved timesheets must be **unapproved** first; paid timesheets must be marked not-paid first.
- **Absent** status: team member was scheduled but did not clock in; timesheet auto-filled with scheduled shift details; manager can approve (if shift was worked), request leave on behalf, discard, or message the employee.
- Manual add: managers add timesheets on behalf of team members who forgot to clock in (date, start/end, area and location, meal/rest breaks) and approve.
- Editable details: date, area, shift start/end, break type/duration, break start/end, answers to **shift questions** (custom timesheet fields), pay rules.
- **Permissions**: Location Manager and System Administrator can amend and approve **time and pay**; **Supervisor can amend/approve time only and cannot view or amend pay**.
- **Approval workflow**: organizations review and approve timesheets for a past period before exporting to payroll; **cannot approve future timesheets**; chronological approval recommended for accurate overtime and shift-loading calculations; **auto-approval settings** (criteria-based, marked with icon); bulk approve; "approve with no issues" filter; completion signaled when pending count is zero.
- **Unapprove time vs unapprove pay** as separate actions; unapproving only on web, not mobile.
- **Recalculation**: approved timesheets may be recalculated if another timesheet in the same scheduling week is approved (configurable business setting); approved timesheets with overridden pay rules can be skipped during recalculation.
- **Leave timesheets**: generated from leave requests, appear auto-approved, distinguishable by icon; editable like others.
- **Comments & history**: shift notes from team member visible on timesheet; manager comments not visible to team members; full change history viewable.
- **Export**: Export Timesheets tab; CSV/Excel with all fields; editable export codes; **mark as paid** state.
- Pay precision: pay rates/hours to four decimal places (system-defined) to reduce rounding errors.

### Buddy Punch (evidence layer A for feature existence — official product pages; marketing-level wording)

- Positioning: "Employee Time Clock Software … custom-built for U.S. businesses with hourly workers."
- Clocking surfaces: employees clock in/out on computers, mobile phones, or a **time clock kiosk** using a **PIN, facial recognition, or QR code**; no unique email addresses required for users.
- Accountability/anti-fraud: **GPS tracking** (see where employees are while on the clock), **geofencing** (prevent offsite punching), **photos on punch** (selfie at clock in/out to prevent buddy punching), **IP address locks** (punch only on business Wi-Fi).
- Schedule coupling: **punch limiting** (prevent punching in before shift), **attendance alerts** (late, early out, missed shift), scheduling with roles/locations.
- Rules: **break rules** for state meal/rest break laws, **automatic breaks** (remove unpaid breaks from timesheets), **custom overtime policies** (automatically identify OT hours), **overtime alerts** (nearing OT).
- Exception handling: **automatic clock-outs** at shift end (prevent forgotten clock-outs), **punch reminders** (in-app notifications).
- Timesheets: "automatically generated based on clock-in/out data"; regular hours, overtime, and pay calculated automatically; **timesheet approvals** (admin/manager approve before payroll); reports tracking all timesheet corrections.
- Payroll handoff: reports formatted for payroll providers; integrations (QuickBooks, Gusto, ADP); optional built-in payroll service.
- PTO: accrual rules; approved time off deducted from balances, added to timesheets, displayed on schedules.
- Attribution: **job costing**; duration entry for salaried employees.
- Industries: field (construction/landscaping), office/remote (professional services), on-site (healthcare/restaurants/retail/schools).

## Cross-product Comparison

| Aspect | When I Work | Jibble | Deputy | Buddy Punch |
|---|---|---|---|---|
| Shared clocking surface | Time Clock Terminal (dedicated computer/mobile; employee ID/email) | Kiosk (QR, kiosk mode, app pinning/guided access); RFID/NFC | Kiosk/Time Clock apps (iPad/Android), Web Time Clock (shared browser) | Time clock kiosk (PIN / facial recognition / QR) |
| Personal clocking surface | web/iOS/Android app | mobile/web/desktop/Chrome | personal app (kiosk apps are shared) | computer/mobile apps |
| Identity verification at surface | employee ID or email; photo clock-in (iOS) | facial recognition; RFID/NFC; QR; PIN | PIN; facial recognition; photo capture | PIN; facial recognition; QR; photos on punch |
| Punch content | timestamp (hour+minute), position, job site, note, tips, break attestation | timestamp, project/activity/location attribution, notes | start/break/finish times, area/location, shift questions | timestamp, GPS location, photo, job attribution |
| Schedule linkage | shift-bound clock-in; window restriction; block early/unscheduled | work schedules drive OT; geofenced auto clock | scheduled shift vs actual; Absent auto-fill; micro-scheduling | punch limiting; attendance alerts |
| Location enforcement | physical address or IP restriction | geofences (restrict or auto-punch); GPS reminders | kiosk physically at workplace | GPS tracking; geofencing; IP locks |
| Breaks | break clocking; break attestation at clock out | break rounding; unpaid breaks excluded from OT | break type/duration editable; meal/rest on manual add | break rules (state laws); automatic breaks |
| Rounding | nearest 5/6/15 min; rounded or actual export | up/down/nearest; intervals; date-ranged rules; actual vs rounded shown | rounding settings | (not confirmed from fetched pages) |
| Overtime | (documented in product; not fetched in detail) | daily/double/weekly/rest-day/holiday; thresholds+multipliers; payroll view | OT + shift loading on approval; chronological approval advised | custom OT policies; OT alerts |
| Exceptions | attendance notices (late, missed out, wrong location, missed in) | reminders; automatic clock out; offline upload errors | Absent status; forgot-to-clock FAQ; manual add | attendance alerts; automatic clock-outs; punch reminders |
| Approval | approve before closing pay period | pay-period approvals; approved not recalculated; reopen recalculates | Pending→approve; unapprove time/pay; auto-approval; bulk | approve before payroll |
| Pay period | open/closed states; close & export | pay-period timesheets & approvals | period review; mark as paid | payroll-cycle reports |
| Payroll handoff | close & export; integrations | payroll view; Xero/QuickBooks/Deel/PayrollPanda | export (CSV/Excel, export codes); mark as paid | formatted reports; QuickBooks/Gusto/ADP; built-in payroll |
| Roles | Admin/Manager/Supervisor/Employee; supervisor scope = own schedule | Owners/Admins configure; managers approve | SysAdmin/Location Manager (time+pay); Supervisor (time only) | admin/manager approve; employees punch |
| Audit | edit history + clock-location map | actual vs rounded; archived rules | full history; comments (manager comments hidden from employees) | correction reports |

## Canonical Abstraction

### L0 — Defining Invariant

Minimal structure without which the product stops being an Employee Time Clock:

1. **Identified employee as clocking subject** — time is recorded against a specific, identified member of the organization.
2. **Work-time boundary events (punches)** — start/stop (and typically break) events recorded as timestamps at a clocking surface, by the employee or by an authorized manager on their behalf.
3. **Accumulation into an authoritative per-employee time record** — punches assemble into a per-employee, per-pay-period timesheet that is the organization's record of worked time.
4. **Organizational oversight and downstream use** — the record is reviewed/approved under organizational authority and handed to payroll/attendance processing; it is not a personal productivity log.

§24 historical check: a mechanical punch clock with paper timecards satisfies all four (badged worker; in/out punches; timecard per period; payroll clerk totals the cards). Mobile GPS, biometrics, geofencing, rounding, OT engines, schedules, kiosk apps are all later implementations, not invariants. The L0 holds across eras.

### L1 — Common Mature Structure

- Multiple clocking surfaces: personal device app + shared terminal/kiosk + web.
- Schedule linkage: shift-anchored clocking, early/late windows, block-unscheduled, late/absent detection.
- Break tracking: paid/unpaid breaks, attestation, automatic break deduction.
- Rounding rules (interval-based, applied to timestamps; actual vs rounded preserved).
- Overtime rules (daily/weekly thresholds, multipliers, rest-day/holiday classes).
- Exception machinery: missed punch, late, wrong location; reminders; automatic clock-out.
- Manager approval workflow: pending → approved; edit before approval; unapprove to amend.
- On-behalf clocking / manual timesheet creation for forgotten punches.
- Audit trail: change history, notes/comments, punch-location evidence.
- Payroll handoff: close pay period, export files/formats, integrations.
- Anti-fraud identity verification at the surface (PIN, photo, facial recognition, badge/QR).
- Employee self-service: view own hours.

### L2 — Variant / Optional Structure

- Location-enforcement method: geofence vs IP lock vs kiosk-only vs none.
- Identity substrate: employee ID, email, badge/RFID/NFC, QR, biometric/face.
- Attribution depth: position/job costing/area/location; tips.
- PTO/leave integration (leave timesheets, accruals).
- Offline mode; touchless/voice clock-in; multi-language kiosks.
- On-demand pay partnerships; built-in payroll vs external integration.
- Auto-approval policies; duration entry for salaried workers.
- Industry posture: field/GPS-heavy, on-site/kiosk-heavy, office/remote.

### L3 — Vendor-specific (research notes only)

- Deputy: separate unapprove-time vs unapprove-pay; 4-decimal pay precision; leave-timesheet iconography; auto-approval lightning-bolt marker; micro-scheduling; supervisor cannot see pay.
- Jibble: workday split time (default midnight) ending OT periods; weekly OT non-combinable with other OT classes; PayrollPanda/Malaysia OT variant; moon icon for OT days.
- When I Work: 5/15/30-minute clock-in window options; iOS-only photo clock-in; Clair on-demand pay; seconds never recorded.
- Buddy Punch: "punch limiting" and "IP address locks" as named features; built-in payroll service.

## Vendor-specific Findings

See L3 above. None of these should be promoted to the canonical model. The 5/15/30-minute window values, 5/6/15/30 rounding intervals, and midnight split are product-specific configuration menus, not industry constants.

## Boundary Findings

- **vs Time & Attendance System**: T&A is the system-level Type (schedule compliance, absence, accruals, labor-rule management, often forecasting). The time clock is the punch-recording + timesheet-assembly layer that T&A systems contain and that standalone products expose as their whole product. Test: remove punch recording → not a time clock; make scheduling/absence/forecasting primary → T&A/WFM. The directory keeps both leaves; they are nested, not duplicated.
- **vs Time Tracking Application**: time tracking is self-reported, task/project-attributed, often voluntary, for productivity/billing; the time clock is attendance-oriented, organization-authorized, shift-anchored, payroll-bound. Some products span both (Jibble explicitly markets both faces); the difference is the unit of truth (attendance hours for payroll vs task durations for billing/analysis).
- **vs Payroll System**: payroll computes wages from approved time; the time clock produces the approved time. Boundary = wage computation. Some products bundle both (Buddy Punch built-in payroll; Deputy Payroll AU/US).
- **vs Employee Scheduling Platform**: schedule = plan; time clock = actuals. Scheduling-led products (When I Work, Deputy) bundle both and couple them (window restrictions, absent detection).
- **vs Workforce Management Platform**: WFM is the suite (scheduling + T&A + forecasting + engagement); the time clock is one capability inside it.
- **"去掉什么就变成另一个 Type" 判据**: remove the organizational oversight/payroll destination and keep self-logged task time → Time Tracking Application; remove punch recording and keep schedule/absence/accruals → Time & Attendance / Scheduling; add wage computation as primary → Payroll System.

## Uncertainties

- Enterprise HCM time-clock behavior (Workday, UKG/Kronos, ADP, Paycom) could not be directly researched (gated/JS-rendered sources). Enterprise hardware terminals (badge/fingerprint readers) are known to exist but are not evidenced here; claims about enterprise tier are kept weak.
- Rounding intervals, clock-in window values, and OT thresholds vary per product; exact values documented here are product-specific configuration menus, not industry standards.
- Buddy Punch evidence is product-page level (Tier 2); operational depth (e.g., exact approval states) not confirmed.
- Legal/regional variation (rounding legality, break attestation, tips) is acknowledged by vendors but not researched in depth.

## Final Synthesis

The Employee Time Clock is the punch-recording and timesheet-assembly layer of workforce time management: identified employees record work-time boundary events (in / break / out) at clocking surfaces (shared kiosk/terminal, personal mobile/web); the system assembles punches into per-employee, per-pay-period timesheets under organizational rules (schedule windows, location restrictions, rounding, breaks, overtime); managers review, correct, and approve; the approved record is closed and exported to payroll. Everything else — biometrics, geofencing, GPS, tips, job costing, PTO, on-demand pay — is implementation depth layered on this spine. The Type is nested inside Time & Attendance (system level) and sits upstream of Payroll and alongside Scheduling (plan vs actual).
