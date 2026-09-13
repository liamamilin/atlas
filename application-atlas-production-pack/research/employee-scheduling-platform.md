# Research Notes — Employee Scheduling Platform

## Research Goal

Understand how real employee-scheduling products work: what objects they manage, how a schedule is built and published, how employees interact with it, which rules govern assignment, and where the Type's boundary lies against Time & Attendance, Workforce Management suites, contact-center WFM, and appointment scheduling.

## Initial Boundary

Working hypothesis before research:

- Core purpose: decide and communicate "who works when" for shift-based workforces.
- Users: managers/schedulers (build), employees (receive, respond, request changes).
- Likely core objects: employee, shift, schedule, availability, open shift, swap.
- Likely confusions: Time & Attendance (actuals vs plan), Workforce Management Platform (broader suite), Agent Scheduling Platform / Workforce Management for Contact Centers (interval-level queue staffing), Appointment Scheduling (customer-facing), Leave & Absence Management (absence vs presence), Resource Calendar (non-person resources), Academic Timetabling, Production Scheduling / APS.

Directory context: leaf sits in section 09 HR, Workforce & Talent, alongside Time & Attendance System, Employee Time Clock, Leave & Absence Management, Workforce Management Platform, and (in section 07) Workforce Management for Contact Centers / Agent Scheduling Platform.

## Research Questions

1. What is the central object (shift? schedule? employee?) and what does a shift consist of?
2. How is a schedule built (manual, copy, templates, auto-scheduling) and what is its container structure (week? location? department?)?
3. What is the lifecycle of a shift from draft to worked time?
4. How do employees receive the schedule and interact with it (view, confirm, swap, offer, claim open shifts, availability, time off)?
5. Which constraints and checks govern assignment (qualifications, availability, conflicts, labor rules, cost)?
6. What roles/permissions exist on the manager side?
7. Where does the schedule hand off to time & attendance / payroll?
8. What differs between SMB standalone products and enterprise WFM suites?

## Representative Products

| Product | Segment / philosophy | Evidence tier reached |
|---|---|---|
| Deputy | SMB→mid scheduling + attendance; recommendation-driven scheduling | Tier 1 (help center articles, full text) |
| When I Work | SMB, employee-first scheduling | Tier 1 (help center articles, full text) |
| Sling | SMB scheduling + communication; coverage/cost oriented | Tier 1 (help center articles, full text) |
| Quinyx | Enterprise AI-driven WFM (EU), forecasting + compliance | Tier 2 (marketing/product pages only; support portal login-walled) |
| UKG (Pro Workforce Management) | Enterprise HCM/WFM suite; scheduling as feature | Tier 2 (marketing/product pages only; docs community gated) |

Rejected/abandoned sources: 7shifts (transport errors ×2), Humanity (login wall), Workforce.com/Tanda (transport error), Skedulo (transport error), Planday (JS shell, no content), Quinyx support portal (401). Per source-access rules these were dropped after 1–2 failures; no memory-filling of their operational details.

## Sources

### Deputy (Tier 1)
- Help Center root: https://help.deputy.com/ (reached 2026-09-06)
- Scheduling category: https://help.deputy.com/hc/en-au/categories/4557613134479-Scheduling
- Creating shifts on your schedule: https://help.deputy.com/hc/en-au/articles/4688731978639-Creating-shifts-on-your-schedule
- Managing Open shifts: https://help.deputy.com/hc/en-au/articles/4688698300687-Managing-Open-shifts
- Allow team members to swap or offer shifts: https://help.deputy.com/hc/en-au/articles/4688726501135-Allow-team-members-to-swap-or-offer-shifts
- Shift status: https://help.deputy.com/hc/en-au/articles/6054132302991-Shift-status
- (Schedule overview article returned 403 on one fetch; category + sibling articles used instead.)

### When I Work (Tier 1)
- Help Center root: https://help.wheniwork.com/
- Scheduling category: https://help.wheniwork.com/article-categories/scheduling/
- Setting Up Scheduling for Your Workplace: https://help.wheniwork.com/articles/setting-up-scheduling-for-your-workplace-computer/
- OpenShifts category (How OpenShifts Work / Scheduling OpenShifts / Shift Bidding / Offer to Specific Users / Publishing OpenShifts / Labor Sharing): https://help.wheniwork.com/article-categories/openshifts/

### Sling (Tier 1)
- Help Center root: https://support.getsling.com/
- Schedules collection: https://support.getsling.com/en/collections/295552-schedules
- Unassigned versus available shifts: https://support.getsling.com/en/articles/511209-unassigned-versus-available-shifts
- Conflicts: https://support.getsling.com/en/articles/1821074-conflicts

### Quinyx (Tier 2)
- https://www.quinyx.com/ (positioning, module map)
- https://www.quinyx.com/workforce-management/scheduling (scheduling product page)

### UKG (Tier 2)
- https://www.ukg.com/ (suite positioning)
- https://www.ukg.com/products/features/scheduling (scheduling feature page)

Research date: 2026-09-06.

## Product Observations

### Deputy — key observations (Evidence Layer A)

**Shift anatomy.** A shift is created with: who (team member / open), start & finish time, area (work area within location), break duration, shift notes (vendor limit: 1000 characters — L3). Defaults for start time/length/break come from location scheduling settings; in "team member view" the system pre-fills from that person's historical schedules.

**Recommendation engine.** When assigning, Deputy ranks "most suitable" team members using five factors: fatigue, training, availability/leave, permission to work at the location, and conflicting shift. Managers can override warnings; a shift assigned despite a warning displays a warning state but can still be published and worked.

**Open vs empty shift.** Explicit distinction: an *Empty shift* is an unassigned placeholder "scaffolding" that cannot be published; an *Open shift* is unassigned but claimable by recommended team members (first-come-first-served) or claimable with manager approval. *Shift offers* invite a selected group (same or other locations the manager controls) to claim; offers can be cancelled before claim; offers cannot be combined with approval mode.

**Swap vs offer (employee-initiated).** *Shift swap*: employee requests a qualified colleague take their shift in exchange for one of the colleague's future shifts; manager approval optional (configurable per location); requires co-worker schedule visibility set to "Allow all". *Shift offer*: employee offers their shift to qualified co-workers; no manager approval required, manager is notified; if unclaimed, the original employee remains responsible. Swap/approval flows surface on the manager dashboard and in the schedule (SWAP marker).

**Shift status lifecycle.** States: Empty → Open (white unpublished / green published, with request counts when approval mode) / Filled (grey unpublished) → Published (green; visible to assigned employee) → Pending confirmation (manager asked employee to confirm; CONFIRMING label) → Locked (shift in the past with an associated timesheet; not editable). Warning shifts carry an overridden-recommendation flag. A status bar counts empty/unpublished/published/confirming/open/warning shifts plus approved/pending leave and unavailable people.

**Build acceleration.** Repeating shifts, copy shifts (single/day/2- or 4-week period), saved schedule templates, clone shifts, bulk update, auto-fill empty shifts, Auto-scheduling (Smart Scheduling using business data), auto-schedule regular working hours for fixed agreements.

**Cost & roles.** Scheduled shift costs visible to Location Manager / System Administrator; hidden from Supervisors. Costs update to actuals when timesheets are approved. Team member list sortable by hours, scheduled cost, stress, age, role, qualification, distance, tenure, leave/availability (L3 details).

**Adjacent modules in same product** (not scheduling core): timesheets, leave management, HR, payroll (AU/US), news feed, tasks, kiosk/time clock, analytics.

### When I Work — key observations (Evidence Layer A)

**Setup model.** Named *Schedules* as containers (default schedule; multiple schedules for locations/regions or teams/departments). *Positions* tie people and shifts to a duty/skill ("keeping users and shifts separated by position helps ensure skilled coverage"). *Users* added individually, imported, or self-registering with manager approval. *Shift templates* for standard recurring shifts. *Scheduling Settings* control how users interact with the schedule ("allow users to take accountability for their own schedule").

**Build & publish.** Build in the Scheduler using templates or custom shifts; guidance to keep shifts unpublished while building so changes don't notify staff prematurely; then *Publish & Notify* (publishes the viewed day/week/month and notifies staff). Schedule templates can be saved from a built week. Printing/exporting supported.

**OpenShifts.** Scheduled without a specific person; eligible users pick up. Two modes: first-come-first-served ("Take Shift") or approval-required ("Shift Bidding" — users bid, manager selects). Eligibility = qualified (position/skill) + available. Managers can offer an OpenShift to specific eligible users. OpenShifts can be shared across schedules ("Labor Sharing") to fill coverage from other schedules' eligible users.

**Employee side.** View personal schedule; set availability; request time off; drop/swap shifts (Shift Requests category); take/bid on OpenShifts; receive notifications. Separate product categories for Time Clock & Attendance and Team Communication.

### Sling — key observations (Evidence Layer A)

**Unassigned vs available.** *Unassigned shifts*: visible to managers only; a reminder of coverage needed; must be assigned or made available. *Available shifts*: unassigned but visible to employees, who can apply; used to fill open slots. Both show as "no employee" in month view; week view distinguishes them. (Same conceptual pair as Deputy's empty/open.)

**Conflict handling.** A conflicts filter shows when an employee is already scheduled elsewhere (other position/location) while filtering views — prevents double-booking across the org.

**Build tooling.** Creating a shift, shift notes, coverage guidance ("Getting your coverage right"), publish/unpublish (including publish specific shifts), bulk editing, auto-assign, tags, day notes, schedule templates, shift templates, time blocks/day parts, recurring shifts, copying shifts, open-ended shifts, breaks, scheduling multiple employees, undo scheduling, shift history/activity log, no-shows and sick callouts handling.

**Employee side.** "My schedule", shift acceptance, shift applications, how employees receive schedules (notifications), schedule visibility settings.

**Cost.** Labor cost collection: wages, holiday pay, projected and actual sales, overtime measurement. Time Clock and Timesheets is a separate collection (adjacent module).

### Quinyx — key observations (Evidence Layer B/C, Tier 2 only)

Positioning: AI-powered workforce management platform; scheduling is one module alongside Time & Attendance, Analytics, Forecasting, Employee Hub, Messenger, Task management. Scheduling claims (marketing): manual, semi-automatic, or fully automatic schedule building; smart rules and real-time cost visibility with alerts for rule violations, unavailability, and cost overruns while building; assign by skills and availability; shift swapping; multi-unit employees; staff portal & mobile app (schedules, leave requests); task scheduling & tags; compliance "built in" across regions/sites. Industries: retail, warehousing/logistics, hospitality/QSR, facility management, healthcare. No operational workflow detail accessible (support portal 401) — all Quinyx claims stay at positioning level.

### UKG — key observations (Evidence Layer B/C, Tier 2 only)

Positioning: scheduling is a feature of Workforce Management inside the UKG HCM/pay/WFM platform (UKG Pro Workforce Management; UKG Ready for smaller businesses). Scheduling feature page claims: AI demand forecasting at 15-minute intervals; auto-assign by skills/preferences/availability; rule-based automation for fatigue, compliance, cost; real-time alerts for labor-law compliance; fair workweek law support, certifications, fatigue rules, overtime caps; mobile self-service (swap, preferences, open shifts, time off); real-time coverage-gap management; multi-location role-based coverage modeling; scheduling data linked to payroll. Industries: healthcare, retail, hospitality, public sector, manufacturing, logistics. No operational docs accessible — claims stay at positioning level; the "15-minute intervals" figure is a vendor marketing claim (L3) and is not carried into the final document as fact.

## Cross-product Comparison

| Dimension | Deputy | When I Work | Sling | Quinyx (T2) | UKG (T2) |
|---|---|---|---|---|---|
| Central object | Shift (person × time × area × break) | Shift (person × position × time) | Shift (person × position × time) | Shift | Shift |
| Schedule container | Location + date range; areas | Named Schedules (location/team) | Location/position views | Sites/teams/regions | Multi-site, roles |
| Unassigned-shift concept | Empty shift (not publishable) vs Open shift (claimable) | OpenShift (claimable/biddable) | Unassigned (manager-only) vs Available (employee-visible) | implied | implied ("open shifts") |
| Claim modes | FCFS; with approval; offers to selected | FCFS; bidding (approval); offers | Apply to available shifts | shift pick-up (claimed) | pick up open shifts |
| Employee-initiated change | Swap (approval optional) + Offer (no approval) | Drop/swap via Shift Requests | Shift acceptance/applications | shift swapping | swap with coworkers |
| Availability/time off | Availability/leave feed recommendation; time off visible on schedule | Availability; time off requests | Unavailability & time off collection | leave requests via portal | submit availability, request time off |
| Qualification model | Training tags; location permission; 5-factor recommendation | Positions (duty/skill) | Positions + tags | skills | skills, certifications |
| Conflict handling | Conflicting-shift factor; warning + override | eligibility filtering | conflicts filter | alerts while building | real-time compliance alerts |
| Build acceleration | Repeat/copy/templates/auto-schedule | Templates; schedule templates | Templates; recurring; copy; auto-assign | semi/full automation | rule-based automation |
| Publish step | Publish (per shift/schedule); notify | Publish & Notify | Publish / publish specific shifts | publish schedules | schedule release (implied) |
| Employee confirmation | Shift confirmation (CONFIRMING) | — (not observed) | shift acceptance | — | — |
| Cost visibility | Scheduled cost per shift; role-gated | — (not observed in fetched pages) | labor cost w/ projected & actual sales | real-time cost visibility | cost control rules |
| Handoff to actuals | Locked shift = past shift with timesheet | Time Clock & Attendance module | Time Clock & Timesheets module | Time & Attendance module | Time & Attendance + payroll |
| Compliance depth | fatigue/training/availability factors | — | — | built-in regional compliance | fair workweek, fatigue, OT caps |
| Forecasting | Smart Scheduling from business data | — | — | AI demand forecasting | AI demand forecasting (interval-level claim) |

Stable across all five (B-layer commonality): employee roster; shift as unit; schedule as week-oriented container; assignment incl. unassigned/open state; publication as the pivotal release act; availability & time off as employee-declared constraints; qualification/position model; open-shift claiming with optional approval; swap/offer mechanics; templates/copy/recurring acceleration; notifications; manager/employee dual surfaces; handoff toward time & attendance.

Present in some, not all (L2): labor cost/budget views (Deputy, Sling, Quinyx, UKG; not observed in WIW pages), employee shift confirmation (Deputy, Sling), forecasting/auto-scheduling (Deputy, Quinyx, UKG), compliance-rule depth (Quinyx, UKG), cross-location labor sharing (WIW, Deputy offers, UKG multi-location), tasks (Deputy, Quinyx), communication bundling (Sling, Quinyx).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

1. **Schedulable employee roster** — identified people who can be assigned work.
2. **Shift** — a bounded unit of work time (start/end, work context such as position/area) as the central object.
3. **Schedule** — the time-organized container of shifts (calendar/week grid over a period).
4. **Assignment** — binding a shift to a specific employee, with "unassigned/open" as a first-class state of that binding.
5. **Publication** — the schedule is released to employees as the record of when they are expected to work (two-sided: manager-side construction, employee-side reception).

Remove any of these and the Type collapses: without the roster it is a blank calendar; without shifts it is a task list; without the schedule container it is ad-hoc dispatch; without assignment it is a notice board; without publication it is a private planning tool (resource calendar).

### L1 — Common Mature Structure

- Availability & time-off requests as employee-declared constraints feeding assignment
- Positions/roles/skills/qualifications attached to people and required by shifts
- Locations/areas/departments as organizational containers
- Open-shift claiming (FCFS and approval/bidding variants) and targeted offers
- Shift swap/offer between employees, with optional manager approval
- Shift/schedule templates, copy previous period, recurring shifts
- Conflict & eligibility checking (double-booking, availability, qualification)
- Publish-and-notify mechanics with change notifications
- Employee self-service surface (mobile/web): my schedule, requests, claiming
- Manager-side roles/permissions (admin/manager/supervisor/employee tiers)
- Break planning inside shifts
- Handoff to time & attendance (schedule → actuals), often same suite
- Labor cost visibility (scheduled cost, budget comparison)

### L2 — Variant / Optional Structure

- Demand forecasting + auto-scheduling (AI/algorithmic; enterprise skew)
- Compliance depth: regional labor law, fair-workweek/predictive-scheduling rules, fatigue rules, certification enforcement, overtime caps
- Employee shift confirmation step
- Cross-location/cross-schedule labor sharing
- Micro-scheduling (task-level granularity inside shifts)
- Bundled communication (messaging, newsfeed), tasks, kiosk/time clock
- Payroll integration depth
- Industry vertical editions (restaurant, retail, hospitality, healthcare, logistics)
- Print/export of schedules (legacy/paper workflows)

### L3 — Vendor-specific (research notes only)

- Deputy: five recommendation factors; 1000-char shift note limit; "stress" sort; borrowing team members across locations; micro-scheduling; kiosk; AU/US payroll modules
- When I Work: "Labor Sharing" branding; "Publish & Notify" button; shift-bidding terminology
- Sling: time blocks/day parts; open-ended shifts; world clock; projected vs actual sales
- Quinyx: Tags for cost centres; Employee Hub; Forrester/Gartner claims; ROI figures
- UKG: 15-minute interval forecasting claim; Bryte AI; fair-workweek packs; NMLS money-transmission footnote

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit L0?

- Paper/Excel-era scheduling (pre-cloud): roster + shifts + week grid + assignment + posting the schedule → fits (publication = posting/printing).
- Hospital nurse rostering systems (long-standing European tradition): roster + shift patterns + rotation rules + roster publication → fits; their rule depth is L2 compliance variant.
- Union/rota-based rostering (e.g., fire departments, police): fits; seniority/bid rules are L2.
- Early web scheduling tools (no mobile app, no labor cost, no open shifts): fit L0 — mobile app, cost, open shifts are L1/L2, not definitional.

Conclusion: L0 holds across eras and regions; nothing era-specific (mobile app, AI, cost) is in L0.

## Vendor-specific / Rejected Findings

- Rejected from core: labor cost/budget (not observed in all samples; absent from WIW fetched pages) → L1.
- Rejected from core: employee confirmation step (Deputy/Sling only) → L2.
- Rejected from core: AI forecasting (enterprise-only skew) → L2.
- Rejected from core: compliance-rule engines (depth varies; SMB products check eligibility/conflicts, not statute) → L1 (eligibility) + L2 (statutory depth).
- Rejected: "Workforce engagement/communication" as part of the Type → bundled L2 module.
- Rejected: contact-center interval staffing as same Type → different demand model; separate directory leaves exist (Agent Scheduling Platform; Workforce Management for Contact Centers).

## Boundary Findings

| Neighbor | Shared surface | Remove-what-to-become-the-other criterion |
|---|---|---|
| Time & Attendance System | the shift; employee identity | Remove planning/assignment of *future* shifts and keep only recording/approval of *worked* time → T&A. The schedule→timesheet handoff (Deputy's locked shift) marks the boundary. |
| Workforce Management Platform | scheduling module | WFM = scheduling + T&A + forecasting + engagement + analytics on one platform. If the center of gravity is the full labor lifecycle and demand optimization → WFM; scheduling is its core module. |
| Workforce Management for Contact Centers / Agent Scheduling Platform | assigning people to time | CC-WFM derives staffing from queue forecasts/service-level targets at interval granularity; employee scheduling assigns shifts against business coverage needs without queue math. |
| Appointment Scheduling Application | time slots + people | Appointments bind *customers* to service providers; employee scheduling binds *employees* to work. Customer-facing vs staff-facing. |
| Leave & Absence Management | employee time | Leave manages approved absence; scheduling consumes leave as an assignment constraint and shows it on the grid. |
| Resource Calendar / Enterprise Resource Scheduling | calendar grid | Resource calendars schedule rooms/equipment; employee scheduling schedules people as labor with wages/qualifications/availability. |
| Academic Timetabling | recurring time assignments | Timetabling's objects are teaching activities, rooms, student groups; not an employee roster with shifts/claims/swaps. |
| Production Scheduling / APS | scheduling word | APS schedules jobs/operations on machines/capacity; people are one constraint, not the scheduled subject. |
| Airline Crew Management / crew scheduling | shifts/duty periods | Crew scheduling operates under duty-time legality/pairing regimes specific to transport; different rule regime and objects. |
| Staffing Agency Management System | temp workers + shifts | Staffing agency systems manage client orders/placements/billing of external workers; scheduling is one downstream step. |

## Uncertainties

- Quinyx and UKG operational behavior (exact workflow, states, defaults) could not be verified (login-walled support portals); their inclusion rests on Tier-2 positioning pages. Enterprise-tier workflow claims in the final document are therefore kept generic ("enterprise products commonly…").
- When I Work's swap/drop mechanics were seen only at category level (Shift Requests), not full article text; described conservatively.
- Whether every product supports employee shift *confirmation* is unverified beyond Deputy (explicit) and Sling (shift acceptance); treated as L2.
- Deputy "Schedule overview" article returned 403; covered via category + sibling articles.

## Final Synthesis

An Employee Scheduling Platform is a two-sided labor-assignment system: a manager side that constructs a time-organized schedule of shifts and binds identified employees to them (or leaves shifts open for claiming), and an employee side that receives the published schedule and reacts to it (view, confirm, swap, offer, claim, declare availability, request time off). Assignment is governed by eligibility (qualification, availability, conflicts, and in some products statutory rules and cost), and the published schedule hands off to time & attendance when shifts are worked. The defining core is deliberately small: roster, shift, schedule, assignment (with open state), publication. Everything else — templates, open shifts, swaps, cost, forecasting, compliance engines, communication — is mature common structure or variant depth, not definition.
