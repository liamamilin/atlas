# Research Notes — Enterprise Resource Scheduling Platform

Research date: 2026-09-06
Slug: enterprise-resource-scheduling-platform (DIRECTORY §10 Enterprise Operations & Administration)

## Research Goal

Understand what an Enterprise Resource Scheduling Platform is from real products: what objects exist inside it, what counts as a "resource", who operates it, how a booking gets made and governed, what rules control allocation, and where the boundary lies against neighboring Types (Resource Calendar, Meeting/Appointment Scheduling, Employee Scheduling, Space Management/IWMS, Event Management, PSA, Academic Timetabling, APS).

## Initial Boundary (hypothesis before research)

- Core use: organization-side scheduling of shared, capacity-limited resources (rooms, desks, equipment, vehicles, and in some products people) over time, with conflict prevention and shared visibility.
- Primary users: schedulers/coordinators/administrators who own the registry and rules; end users (staff, students, members) as self-service requesters.
- Nearest neighbors: Resource Calendar (§03.08 — a calendar surface, not an operations platform), Meeting Scheduling (person-calendar coordination), Appointment Scheduling (customer-facing service time), Employee Scheduling (people as labor/shifts), Space Management / IWMS (space portfolio management), Event Management (event programs), PSA (project financials suite with people resourcing), Academic Timetabling (teaching-activity model), APS (manufacturing semantics).
- Unknowns: does "resource" include people across the market, or only things? Is the defining surface a calendar, a floor plan, or a timeline? How do rule engines relate to approval workflows? Is check-in/no-show handling core or optional?

## Research Questions

1. What is a "resource" in these products? (rooms, desks, equipment, vehicles, parking, people?)
2. What is the central object — booking, reservation, allocation? What does it attach (resource × time × requester × purpose)?
3. How is availability modeled, and how are conflicts/double-bookings prevented or resolved?
4. What governance exists: rule engines (conditions/quotas/windows), approval workflows, roles?
5. What is the booking lifecycle (draft/pending/tentative/confirmed/checked-in/completed/cancelled/no-show)?
6. What interfaces exist (calendar grid, timeline/Gantt, floor plan, kiosk/signage, mobile)?
7. How do integrations work (Outlook/Google calendars, video conferencing, HR/identity, access control)?
8. What reporting exists (utilization, capacity, actuals vs scheduled)?
9. What variants exist by segment (corporate workplace, higher ed, professional services) and what is bundled vs standalone?

## Representative Products

| Product | Segment | Philosophy | Why selected |
|---|---|---|---|
| Skedda | Corporate workplaces + universities; space/room/desk booking | self-service booking governed by automated deny-rules (minimize admin approvals) | market-leading space booking SaaS; strong public help center; rule-engine depth |
| Resource Guru | Agencies/consultancies/studios; people + equipment + rooms | dedicated multi-resource-type scheduling with clash management and approvals | shows "resource" beyond spaces (equipment, vehicles, people) |
| Float | Professional services / in-house delivery teams; people-centric | visual people-allocation schedule tied to projects, estimates, actuals | people-as-resource pole; shows the planning (not booking) emphasis |
| Accruent EMS | Enterprise + higher education (campus) | classic centralized "room and resource scheduling" for any resource type, inside a workplace suite | the product most literally marketed as enterprise resource scheduling; shows enterprise/campus bundling |

Coverage: space-booking pole vs people-planning pole; SMB/mid-market vs enterprise; standalone vs suite-embedded; rule-engine-first vs approval-first governance.

## Sources

- Skedda — https://www.skedda.com/ (root, fetched 2026-09-06)
- Skedda Support — https://support.skedda.com/en/ (help center index, fetched 2026-09-06)
- Skedda — 6 Quick Steps to get started with Skedda https://support.skedda.com/en/articles/2689785-6-quick-steps-to-get-started-with-skedda (fetched 2026-09-06)
- Skedda — Booking Conditions https://support.skedda.com/en/articles/112700-booking-conditions (fetched 2026-09-06)
- Resource Guru — https://resourceguruapp.com/ (root, fetched 2026-09-06)
- Resource Guru — Resource Scheduling feature page https://resourceguruapp.com/features/resource-scheduling-software (fetched 2026-09-06)
- Resource Guru Help Center — https://help.resourceguruapp.com/en (index, fetched 2026-09-06)
- Resource Guru Help Center — Using Resource Guru category https://help.resourceguruapp.com/en/categories/463490-using-resource-guru (fetched 2026-09-06)
- Float — https://www.float.com/ (root, fetched 2026-09-06)
- Float — Resource scheduling feature page https://www.float.com/product/scheduling (fetched 2026-09-06)
- Accruent EMS — https://www.emssoftware.com/ (product page, fetched 2026-09-06)
- Accruent EMS — Shared Space and Resource Scheduling https://www.accruent.com/products/ems/shared-space-resource-scheduling-software (fetched 2026-09-06)

### Source-access Limitations

- Accruent EMS operational documentation lives in the Accruent Customer Center (login required); evidence is product-page and FAQ level, not manual level. All EMS-specific claims kept at positioning/capability level; no precise limits/defaults asserted.
- Resource Guru individual help articles were not fetched (category listing used); article-level specifics (e.g., exact clash behavior) are not asserted.
- No numeric limits, default values, or pricing-tier specifics from any product are asserted in the final document.

## Product A — Skedda (evidence layer A: direct; root page + help articles)

Positioning: "world's leading space booking and scheduling software"; self-serve booking for desks, rooms, and resources; "automated rules keep it fair, and real data shows you what's actually happening". Use cases: desk booking, hot desking, meeting rooms, office space/hoteling, car parks, academic labs, universities, coworking (separate AllBooked brand), consulting rooms, classrooms, sports facilities.

Key observations (help-center level):

- **Venue model**: the organization deploys a "venue". Setup steps: add spaces (names, photos, descriptions, capacity, features) → access & visibility → booking conditions → test → fine-tune → launch to users.
- **Spaces registry**: spaces carry descriptive information, features, capacity, photographs/floor plans; spaces can be visible to everyone but bookable only by certain users.
- **Access & visibility**: venue can be public or login-protected; who can book = anyone / system users only / users with certain tags; booking transparency configurable (see others' bookings or not).
- **Booking conditions (rule engine)**: deny-based — "Skedda will allow all bookings by default unless a rule/setting denies it". Conditions customizable by space, day of week, time of day, booking duration, holder tags. Examples from official docs: max booking time on Saturday evenings; strictly one-hour bookings; strict two-hour blocks starting only at specified times; deny a tagged user group on Sunday before 2pm. Layered with hours of availability, booking window, quotas, priority windows. Conditions do not apply to System users (admin override). Time granularity setting governs increments.
- **Governance automation vs approvals**: rules ("approvals, quotas, priority windows, and check-in rules control when, where, and how people book, and release seats that go unused") are positioned as reducing the approval bottleneck.
- **Calendar two-way sync**: Microsoft 365 / Google Workspace two-way sync; native Teams/Slack apps; Zoom links; SSO (SAML) and SCIM user provisioning.
- **Interfaces**: day/week booking calendar; interactive floor plan with one-tap booking, photos, tags; neighborhoods; mobile; kiosk/display surfaces implied by visitor management; admin console (Settings).
- **Utilization insights**: desk/room usage, peak hours, booking patterns over time, filterable; occupancy detection; attendance/RTO reporting.
- **Booking lifecycle signals**: booking confirmation emails, cancellation policy, check-in rules with automatic release of unused bookings.

## Product B — Resource Guru (evidence layer A: root + feature page; help category listing)

Positioning: "resource management software" for scheduling people and resources; industries: agencies, consultants, construction, engineering, IT.

Key observations:

- **Resource kinds**: "Schedule people, equipment, vehicles and meeting rooms in one place" — explicitly multi-kind. Help taxonomy: People, Placeholders and Resources as distinct record types (add/edit/archive/delete, import, permissions).
- **Booking**: central act; bookings carry color-coding by project/client/activity type; booking types observed in official imagery: personal vacation, recurring bookings, bookings synced from external calendars (Outlook), sick leave, duration bookings.
- **Clash management**: "proactive clash management, a waiting list for unresolved bookings, and approval workflows that protect in-demand people"; heatmap view flags clashes and over-capacity (amber warning states).
- **Booking Approvals** (help category): "Specify who can approve bookings for specific people and resources" — approvals scoped per resource/person.
- **Schedule manipulation**: expand, split, duplicate bookings; drag & drop reassignment; "Total Hours bookings" that automatically reallocate effort; resource placeholders; tentative bookings convertible to firm; saved filtered views; zoom levels; personalized dashboards with daily breakdowns; real-time updates; email schedules to staff.
- **Availability realism**: custom availability, external calendar sync, timezones, sick days, out-of-offices; separate Time off management.
- **Projects & Clients**: bookings attach to projects, which belong to clients; custom fields for skills; reports on utilization (scheduled vs billable), timesheets with scheduled-vs-actual and approvals.

## Product C — Float (evidence layer A: root + scheduling feature page)

Positioning: "#1 resource management software for modern delivery teams"; 4,500+ professional services firms and in-house delivery teams.

Key observations:

- **People-as-resource**: "your people's availability, roles, and skills live in Float and update in real time"; schedule shows who's working on what.
- **Visual Schedule**: allocate work by hours or percentages; drag-and-drop adjustment; statuses to show work options (tentative allocations); color coding, custom tags, filters; saved views.
- **Capacity live**: live utilization indicators, pre-booked time off, over-capacity warnings on the schedule itself.
- **Project linkage**: project estimates (price, budget, roles, timeline), AI-assisted staffing ("find the best-fit person"), baseline vs adjusted scope; time tracking (actuals vs scheduled); reporting/dashboards on utilization, margin, budget burn.
- **Positioning toward adjacent systems**: "Float doesn't replace your existing CRM, spreadsheets, HRIS, project and finance tools: it works alongside them" — integrations with PM/time/finance tools (Jira, Asana, Slack, Google Calendar, Outlook, Zapier).

## Product D — Accruent EMS (evidence layer A: product pages + FAQ; help center login-gated)

Positioning: "advanced room and resource scheduling software"; "From desk booking to event scheduling… smooth operations and optimal space utilization"; corporate + higher education.

Key observations:

- **Resource breadth**: "Parking spots, lab equipment, pool lanes: Schedule any space imaginable." FAQ: parking spaces, bike racks, lab equipment, pool lanes, fitness facilities, shared IT resources — "If your organization uses a resource that needs reservations, EMS can manage it."
- **Self-service**: book/update/cancel from mobile app (Direct Spaces), web tool, digital signs, kiosks; "eliminates manual assignments".
- **People as schedulable**: customer quote — the registrar, events services, and performance facilities use it "to schedule their people as well as their equipment".
- **Calendar ecosystem**: integrates with Outlook, Teams, Zoom; recurring meetings; alerts.
- **Campus overlays**: classroom and exam scheduling; conference and event management; SIS integration (higher-ed edition marketed with "fully integrated with SIS").
- **Analytics**: space utilization and optimization; "100+ standard reports" plus custom report/query builder; FAQ names double bookings and resource shortages as the problems minimized.
- **Bundling**: part of Accruent's workplace/IWMS stack (FAMIS 360, Space Intelligence, event management, signage, HVAC/lighting/AV integration).

## Cross-product Comparison

| Dimension | Skedda | Resource Guru | Float | Accruent EMS |
|---|---|---|---|---|
| Resource kinds at core | spaces (desks, rooms, parking, labs) | people + equipment + vehicles + meeting rooms | people (staff capacity) | spaces + equipment + any reservable resource (+ people in some deployments) |
| Central object | booking on a space | booking (types: work, time off, tentative) | allocation of person-time to project | reservation |
| Availability model | hours of availability + booking window + granularity; deny rules | custom availability + external calendar sync + time off | live capacity/utilization per person | per-resource availability; exam/classroom overlays |
| Conflict handling | prevented at entry via rules; conditions/quota denial | proactive clash management + waiting list | over-capacity warnings; tentative state | "double bookings… minimized" |
| Governance | deny-rule engine, quotas, priority windows, check-in rules; admin (System users) exempt | approvals scoped per person/resource; waiting list | manager/resource-manager roles | admin console; event approval flows |
| Recurring bookings | implied by settings; conditions govern repeats | recurring bookings as a booking type | repeat allocations | recurring meetings (FAQ) |
| Tentative/pending states | — (approval flow implied) | tentative bookings; waiting list | tentative allocations | — |
| Calendar surface | day/week calendar + interactive floor plan | timeline schedule grid + heatmap | timeline schedule grid | web scheduler + kiosks + digital signage |
| Calendar sync | two-way Microsoft 365 / Google | external calendar sync (Outlook etc.) | Google/Outlook integration | Outlook, Teams, Zoom |
| Check-in / no-show | check-in rules; release unused seats | not observed | not observed | check people in via mobile (FAQ) |
| Utilization reporting | utilization insights, peak hours, patterns | heatmap + utilization/billable reports | dashboards, actuals vs scheduled, margin | 100+ reports, utilization analytics |
| Segment | corporate + university | agencies/consultancies | professional services/delivery teams | enterprise + campus (+ healthcare) |
| Deployment posture | SaaS | SaaS | SaaS | suite/cloud (legacy on-prem heritage) |

## Canonical Model (abstraction)

### L0 — Defining Invariant

1. **Registry of shared schedulable resources** — the organization registers the things it schedules as identified records with availability (rooms, desks, equipment, vehicles — and optionally people).
2. **Time-bound reservation** — the central act: a booking/allocation binds one resource (or a set) to a requester and a purpose over a defined time window.
3. **Availability checking / conflict handling** — the platform knows what is free and what is taken, and prevents, flags, or queues conflicting demands (double-booking is *the* failure mode this Type exists to remove).
4. **Shared schedule as system of record** — allocations are visible on a shared calendar/timeline surface to the people who operate and depend on them, not confined to one person's private calendar.

Remove the registry → generic calendar. Remove conflict handling → a notice board, not scheduling. Remove time-binding → an inventory/asset system. Remove the shared schedule → isolated requests with no operational visibility.

### L1 — Common Mature Structure

- self-service booking by end users (vs scheduler-only entry)
- rule engines: hours of availability, booking windows, min/max duration, blocks, quotas, priority windows, per-space/per-user denial rules
- approval/request workflows, scoped per resource or per person
- booking lifecycle states (pending/tentative → confirmed → (checked-in) → completed / cancelled / no-show); exact labels vary by product
- recurring bookings and repeated allocations
- resource attributes: capacity, features, location, photos, tags, custom fields/skills
- people-availability modeling: time off, sick days, working hours, timezones
- calendar integrations (Microsoft 365 / Google, two-way sync), video-conferencing links
- notifications: confirmation emails, reminders, schedule emails, real-time updates
- drag-and-drop reassignment, duplicate/split/expand booking operations
- utilization reporting and capacity dashboards
- roles: scheduler/admin (rule-setting, override) vs requester/user; scoped permissions
- search/filter/color-coding and saved views over the schedule
- multi-location / multi-building scope

### L2 — Variant / Optional Structure

- resource-kind emphasis: space/desk/hoteling (workplace), equipment/vehicles, parking, people-capacity planning (professional services) — the pole a product sits on is a segment variant, not the Type
- check-in / no-show release of unused bookings
- waiting lists for contested bookings
- interactive floor plans / map-based booking; kiosk and digital-signage surfaces
- visitor management bundling; occupancy detection (wifi/sensors)
- pricing/payments for external-facing venues (member/community booking)
- exam & classroom scheduling overlays; SIS integration (higher ed)
- event management bundling (conference/catering/services attached to bookings)
- AI assistance (best-fit staffing, booking assistants), MCP/AI integrations
- HRIS/CRM/PM/finance integration depth (people-planning pole)
- actuals capture (timesheets) vs schedule comparison
- deployment form: standalone SaaS vs module inside a workplace/IWMS suite

### L3 — Vendor-specific (Research Notes only)

- Skedda "venue" concept; AllBooked spin-off brand for member/community booking; test user "Skedda Fred"; condition-count tied to subscription plan.
- Resource Guru "Total Hours bookings"; placeholders; Office Hours video series.
- Float AI best-fit staffing; "Smart insights" profiles; MCP server.
- Accruent EMS Direct Spaces mobile app; 100+ standard reports/query builder; legacy on-prem heritage; FAMIS 360/Space Intelligence suite coupling.

## Vendor-specific Findings

- The deny-rule engine (allow-by-default, deny-by-condition) is Skedda's documented governance philosophy; Resource Guru and Float lean on approvals and capacity warnings instead. Governance posture (automated rules vs approvals) is therefore a spectrum, not a defining structure.
- People-as-resource is primary in Float/Resource Guru, present-but-secondary in EMS, and largely absent in Skedda (spaces only). "Resource" must be defined generically.
- Waiting lists and placeholders observed in Resource Guru only → optional.
- Check-in/no-show release observed in Skedda and EMS (space pole) → common on the space pole, not observed on the people pole.

## Boundary Findings

1. **vs Resource Calendar (§03.08)** — a resource calendar is a calendar surface showing a resource's availability; it is a *feature/interface* inside this Type. The platform adds the registry, the booking workflow, rules/approvals, and utilization measurement. Test: remove the registry + governance + booking lifecycle → you have a calendar feature, not the platform.
2. **vs Meeting Scheduling Application (§03.09)** — meeting scheduling coordinates attendees' personal calendars to find a mutual time (person-centric graph); resource scheduling books organizationally-owned resources. Overlap: room-booking inside meeting tools (Exchange/Outlook rooms) is a thin embedded capability of the same concept, not the platform.
3. **vs Appointment Scheduling Application (§03.09)** — appointment scheduling is customer/externally-facing, books *provider time for a service*, often with payments and client records; resource scheduling is organization/employee-facing and books shared resources. External-facing venues with payments (AllBooked-style) are a variant that blurs this edge — noted as L2, not defining.
4. **vs Employee Scheduling Platform (§09)** — employee scheduling books *people as labor* into shifts with wages, qualifications, availability rules, and labor-law constraints; people-centric resource scheduling books *people as capacity* onto projects/work with utilization aims. Different object semantics (shift vs booking/allocation), different rule families. Adjacent, not identical.
5. **vs Space Management Platform / IWMS (§10, §17)** — space management owns the space portfolio (floor plans, occupancy measurement, moves, lease); resource scheduling owns the *usage over time* of the resources. Suite products bundle both. Test: remove booking/conflict machinery → space management; remove portfolio/moves machinery → resource scheduling.
6. **vs Event Management Platform (§26)** — event management runs event programs (registration, attendees, agendas); resource scheduling provides the venue/resource allocation substrate beneath events. EMS bundles both; the booking core is the Type.
7. **vs Academic Timetabling (§23)** — consistent with research/academic-timetabling.md: timetabling binds rooms to a teaching-activity model (curricula, cohorts, loads, terms); generic resource scheduling lacks that model. Timetabling products embed room booking as a capability (capability-inside-Type).
8. **vs APS / Production Planning (§16)** — APS binds scheduling to manufacturing semantics (operations, routings, BOMs, setups). Test: remove manufacturing semantics → generic resource scheduling.
9. **vs Professional Services Automation (§10)** — PSA spans CRM→project→billing; people-resourcing is one module. Float explicitly positions as "alongside" those systems. The people-planning pole of this Type overlaps PSA's resourcing module; the platform Type is narrower.
10. **vs Amenity Booking Platform** — amenity booking adds building-amenity rule semantics (deposits, lease-based eligibility, guest limits) for residents; generic resource scheduling serves an internal employee/user population.
11. **vs Dock Scheduling Platform** — dock scheduling is logistics-specific appointment machinery for dock doors/carriers; same abstract pattern, domain-specific variant, own Type.

## Uncertainties

- Exact booking-state vocabularies per product not verified at article level (pending/tentative/confirmed labels vary); kept generic in the final document.
- Whether approval workflows are universal or rule-engine-dependent: both postures observed; final document presents approvals and rules as two common governance mechanisms.
- EMS's people-scheduling depth is evidenced by a customer quote only; kept qualified.
- Legacy on-prem resource schedulers (e.g., Exchange-room-mailbox era) not directly researched; the L0 was written to include them (registry + booking + conflict + shared schedule holds without any modern feature).

## Final Synthesis

The market samples resolve into one Type with two poles: **space/equipment booking** (Skedda, EMS) and **people-capacity scheduling** (Float, Resource Guru — which also books equipment and rooms). The shared, Type-defining skeleton is: an organization-owned registry of shared schedulable resources + time-bound reservations (bookings) + availability checking with conflict handling + a shared schedule as the operational system of record. Everything else — rule engines, approvals, check-ins, utilization analytics, floor plans, kiosks, calendar sync, payments, event/classroom overlays — is common mature or variant structure that makes the Type practical in specific segments, but no single item of it is required to recognize the Type.
