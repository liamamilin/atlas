# Research Notes — Hotel Housekeeping Management

## Research Goal

Understand what a Hotel Housekeeping Management application is from real products: what its world is made of, how room servicing is planned, assigned, executed, verified, and how room readiness flows to the rest of the property — then abstract a vendor-neutral Application Type definition with the smallest possible defining core.

## Initial Boundary

Working hypothesis before research:

- Core purpose: coordinate the daily servicing of a lodging property's rooms — decide which rooms need servicing and how urgently, assign attendants, track each room through a readiness lifecycle, and publish readiness so rooms can be assigned/sold.
- Primary users: executive housekeeper / housekeeping manager, floor/housekeeping supervisors, room attendants; front desk as a downstream consumer (not the operator).
- Nearest neighbors: Hotel PMS (contains housekeeping as a module), Hotel Front Desk Application (consumes readiness, maintains occupancy), Property Maintenance Management / CMMS (repair work orders), generic task management, Hotel Guest Experience Platform (guest-facing intake).
- Suspected boundary: the front-desk pass documented that the desk "consumes status but does not run the service work" — this leaf should own the service work itself.

## Research Questions

1. What is the room service-readiness lifecycle (state vocabulary, states, transitions)?
2. What is the unit of housekeeping work, and how is it assigned to staff (zones, sections, task lists, workload weighting)?
3. How does the stay/occupancy picture drive the daily servicing plan (departure cleans, stayover service, arrival priorities)?
4. How is completion recorded (attendant surfaces, checklists, inspection sign-off), and how does readiness reach the front desk?
5. Which adjacent operations live inside or beside it (maintenance, laundry/linen, minibar, lost & found, guest requests)?
6. What are the main interfaces (housekeeping report/board, attendant mobile, supervisor inspection, configuration, analytics)?
7. What is the boundary between a PMS housekeeping module and a standalone housekeeping operations product, and between housekeeping and maintenance/CMMS?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy (PMS module vs standalone operations app) + different customer tiers:

| Product | Shape | Segment |
|---|---|---|
| WebRezPro | Housekeeping module of a long-established cloud PMS | SMB / mid-market independent hotels, hostels, B&Bs, vacation rentals |
| Mews | Housekeeping module of a modern cloud PMS, deeply documented via Open API | Independent hotels → groups/enterprise |
| Flexkeeping | Dedicated standalone housekeeping/maintenance/QA operations suite, PMS-integrated | Complex/large properties and hotel groups |
| Yanolja Cloud Solution (eZee lineage) | Cloud PMS platform for small independents (housekeeping evidenced indirectly) | SMB |

## Sources

Fetched 2026-09-08:

- WebRezPro — "Hospitality Housekeeping Software": https://www.webrezpro.com/housekeeping/ (feature page; Tier 1/2)
- Mews — Connector API use cases: Housekeeping: https://docs.mews.com/connector-api/use-cases/housekeeping.md (Tier 1)
- Mews — Connector API operations: Resources: https://docs.mews.com/connector-api/operations/resources.md (Resource state enum; occupancy-state operation; Tier 1)
- Mews — Glossary for Open API users: https://docs.mews.com/getting-started/glossary.md (Space/Resource/Task/Department definitions; Tier 1)
- Flexkeeping — Housekeeping Suite product page: https://flexkeeping.com/products/housekeeping-software and root https://www.flexkeeping.com/ (Tier 2, marketing prose — feature names treated as observations, performance statistics excluded)
- Yanolja Cloud Solution — Front Desk Managers solutions page: https://yanoljacloudsolution.com/solutions/front-desk-managers (Tier 2; housekeeping mentioned indirectly)

Source-access limitations:

- eZee Absolute root (https://www.ezeeabsolute.com/) returned an HTTP 307 redirect; no dedicated housekeeping page found on the Yanolja Cloud Solution site (solutions/housekeeping-managers → 404). Evidence from this vendor is limited to the FAQ statement that room status updates in real time keep housekeeping and front desk aligned.
- Oracle OPERA Cloud documentation was not attempted on this pass (deep docs unreachable in the same-day adjacent-leaf pass; JavaScript-rendered TOC / oversized PDF).
- Mews help-center articles (help.mews.com, Salesforce-hosted) not individually fetched; the docs.mews.com Markdown pages were used instead.

## Product Observations

### WebRezPro — Housekeeping module of a cloud PMS (evidence layer A)

Directly observed on the vendor's housekeeping feature page:

- **Room status display**: a unit status summary categorizes rooms by current state — explicitly listed: *dirty, clean, inspected, in service (housekeeper in room), do-not-disturb*. Positioned as real-time, integrated with front office; the report shows room status and occupancy together.
- **Housekeeping zones**: units grouped into customizable zones "that can be efficiently serviced together"; zones assigned to specific housekeeping personnel to balance workload.
- **Housekeeper checklists**: per unit type, divided into sections (example: Bathroom, Bed, Living) with tasks per section.
- **Housekeeping report**: table format for desk/office (sortable by unit number, status, unit type, occupancy, zone; keyword filter) and mobile-friendly tile format for housekeepers updating room status on the go.
- **Bulk actions**: change status or assign zones for multiple units at once.
- **Room notes**: two types — temporary (single day) and permanent (until removed).
- **Maintenance alarms**: can be added to any unit; alarm status lifecycle *active → in progress → completed*.
- Unit-by-unit or multi-room status updates.

### Mews — Housekeeping in the cloud PMS, documented via Open API (evidence layer A)

Directly observed in official developer documentation:

- Housekeeping integration pattern: "A Housekeeping integration pulls live information about the physical state of rooms and other space resources, allows the housekeeping staff to update the state from the Housekeeping system and pushes this data back into Mews." The PMS holds the room records; housekeeping systems read stay/reservation data and write back space states.
- **Resource state enum** (Resource = room/space; the PMS API's service-readiness axis): `Dirty`, `Clean`, `Inspected`, `OutOfService`, `OutOfOrder`. States updated by housekeeping staff via Update resources once "a staff member has cleaned or inspected a room".
- **Occupancy state is a separate axis**: a distinct operation returns per-resource *occupancy state* (`Vacant`, `Reserved`, …) filterable together with resource states — structural confirmation that occupancy (stay-derived) and service readiness (housekeeping-derived) are modeled as two independent axes.
- **Out-of-order / out-of-service**: "Resource blocks" are blocks of rooms set to 'out of order' or 'internal use'; housekeeping integrations can list, add, and delete blocks. (Separately, the glossary distinguishes these from availability blocks held for group sales.)
- **Staff tasks**: tasks can be created in the PMS and assigned to employees or departments (Housekeeping is named as an example department); tasks have open/closed state; employees see pending tasks on their dashboard.
- **Dirty-status rules**: configurable when a space becomes `Dirty` (on check-in or on check-out); a configured interval after which a vacant space automatically becomes `Dirty` (example value two days; automatic changes occur overnight; a maximum of seven days exists so vacant rooms are re-cleaned per Legionella regulations).
- The PMS's own housekeeping output is called the **Space Status Report** ("housekeeping report").
- Terminology: Property uses "Space/Resource" for rooms; Tasks are "pieces of work that need to be done within the Property" assigned to Employees or Departments.

### Flexkeeping — standalone housekeeping operations suite (evidence layer A for product shape, marketing prose otherwise)

Observed on official product pages (feature names treated as observations; performance statistics excluded):

- Dedicated **Housekeeping Suite** alongside Maintenance, Automation, Collaboration and Quality Assurance suites; positions itself as operational software layered over a PMS ("Works perfectly with your PMS"; integrations: Mews, Oracle/Opera Cloud, Cloudbeds, Apaleo, Shiji, RMS). A customer quote states PMS contents "reflected" in Flexkeeping — the PMS remains the property system of record.
- **Live Status Updates** — cleanliness status of any room in real time, automatic updates when reservation data changes; FAQ: "you always know which rooms are clean, inspected, or pending" plus real-time housekeeper locations.
- **Smart Scheduling & Auto Assignments** — dynamic cleaning schedules, task delegation, staffing forecasts; **Automated Cleanings** — "any number of cleaning schemas... depending on guest requests and PMS data".
- **Mobile Task Management** — housekeepers receive clear priorities on mobile.
- **Inspection & Quality Control** — digital checklists "to keep standards consistent"; checklists and SOPs are separate capabilities (QA Suite).
- **Linen Consumption Tracking** — amenities managed digitally.
- **Analytics** — trends, bottlenecks, idle labour.
- Other capabilities in the platform: Lost & Found, Guest Service Management, Guest Feedback Management.
- Audience segmentation by role: Housekeeping Managers, Housekeepers, Front Office Managers ("get real-time room readiness updates"), Maintenance Managers, General Managers, hotel groups.

### Yanolja Cloud Solution (eZee lineage) — cloud PMS platform (evidence layer A for one claim, indirect otherwise)

- FAQ on the front-desk solutions page: "Can housekeeping and front desk stay synchronised? Yes. Room status updates in real time, keeping housekeeping and front desk teams aligned throughout the day."
- The front-desk solution page mentions "Room status, housekeeping, and guest requests unified" in one view.
- No dedicated housekeeping page reachable on this date; deeper housekeeping-module claims are not drawn from this vendor.

## Cross-product Comparison

| Structure | WebRezPro | Mews | Flexkeeping | YCS (eZee) | Evidence layer |
|---|---|---|---|---|---|
| Per-room service-readiness state (dirty / clean / inspected) | yes (status summary) | yes (`Dirty`/`Clean`/`Inspected` enum) | yes ("clean, inspected, or pending") | implied | B — across sample |
| Out-of-order / out-of-service handling | maintenance alarms per unit | explicit (`OutOfService`/`OutOfOrder`, resource blocks) | adjacent Maintenance Suite | not observed | A per product; B for existence |
| Occupancy kept separate from readiness | yes (status + occupancy shown together) | yes (separate occupancy-state axis) | yes ("updates when reservation data changes") | implied | B |
| Stay events drive servicing (departure/stayover/arrival) | yes (occupancy in report; status+occupancy integration with front office) | yes (dirty on check-in/check-out; auto-dirty interval) | yes (schemas "depending on guest requests and PMS data") | implied | B |
| Zones / grouping of rooms for servicing | yes (customizable zones assigned to personnel) | not observed | scheduling assigns work (zones not explicitly named) | not observed | A (product-specific wording) |
| Per-room-type checklists / SOP tasks | yes (sections per unit type) | not observed (tasks at department level) | yes (digital checklists, SOPs) | not observed | B for checklists |
| Inspection / quality gate between clean and ready | yes (inspected state) | yes (inspected state; staff "cleaned or inspected") | yes (Inspection & QC; "clean, inspected, or pending") | not observed | B — across sample |
| Attendant-facing mobile update surface | yes (tile-format report) | implied (staff update states; tasks on dashboard) | yes (Mobile Task Management) | not observed | B |
| Real-time readiness consumed by front desk | yes (integrated with front office) | yes (integration pushes states back into PMS) | yes (front office gets real-time readiness) | yes (FAQ) | B — across all sampled |
| Maintenance tickets/alarms | yes (active/in-progress/completed) | adjacent (tasks; resource blocks) | adjacent (separate Maintenance Suite) | not observed | B for existence; often separate |
| Linen/laundry | not observed | not observed | yes (linen consumption tracking) | not observed | A, single product |
| Lost & found | not observed | not observed | yes | not observed | A, single product |
| Workload credits / minutes per room type | not observed | not observed | staffing forecasts mentioned; no credit system named | not observed | insufficient — do not assert |
| Multi-property / group-level control | multi-property PMS | portfolio module | hotel groups solution | multi-property platform | B (of the containing platform) |
| Analytics / performance reporting | not observed on page | not observed | yes | not observed | A, single product |

## Canonical Model

### Level 0 — Defining Invariant (deliberately minimal)

The Type is the lodging property's **room-servicing operations system**. Three jointly-held structures; remove any one and it stops being this Type:

1. **Rooms as individually serviced units with a service-readiness state.** The property's rooms (or bookable units) are each held as a persistent serviced unit carrying a readiness state — not-ready (dirty) versus ready (clean, optionally inspected) — plus removal-from-service states. Housekeeping maintains this state. Remove → a generic task/checklist app with no room semantics, or a room list nobody services.
2. **Stay-driven servicing demand.** What needs servicing, when, and how deeply derives from the property's stay/occupancy picture: departing stays generate full departure service, ongoing stays generate lighter stayover service, expected arrivals generate priority, and non-serviced vacancy rules regenerate work. Remove → a cleaning checklist app with no lodging operations behind it.
3. **The attendant servicing loop closed by a readiness handoff.** Work is organized and assigned to housekeeping staff, execution is recorded on the unit, quality is verified, and the resulting readiness is published to the property's room-assignment process (front office). Remove the loop → a static status list; remove the handoff → a private worklog that never feeds the property operation.

Jointly-held is load-bearing: 1 alone = a room status list; 2 alone = an abstract schedule; 3 without 1+2 = a generic task board; 1+2 without 3 = monitoring without work; 1+3 without 2 = servicing unrelated to stays.

Historical check: the paper-era pattern — a room board/assignment sheet listing departures and stayovers, attendants assigned to floors/sections, a dirty→clean→inspected flow signed by a floor supervisor, the desk informed via the board — satisfies all three structures. Mobile apps, cloud sync, PMS APIs, AI scheduling and analytics are era-current capability layers, not invariants.

### Level 1 — Common Mature Structure (very common, not definitional)

- **Housekeeping report / room-status board** — the per-room working view combining service state and occupancy; table format for the office, tile/mobile format for attendants (WebRezPro dual format; Mews Space Status Report; Flexkeeping live status).
- **Zones / sections** — rooms grouped for efficient servicing and assigned to attendants (WebRezPro explicit; Flexkeeping scheduling equivalent).
- **Per-room-type checklists and task procedures** — service steps per unit type, in sections (WebRezPro; Flexkeeping checklists/SOPs).
- **The inspection gate** — a distinct verified-ready state between "cleaned" and "assignable" (dirty → clean → inspected appears in all three deep-sample products as state or capability).
- **Attendant mobile update surface** — attendants mark work done from the floor.
- **Real-time sync with the front office** — readiness pushed to the desk as it changes (all four sampled products assert this).
- **Room notes** — temporary and standing notes attached to a unit (WebRezPro).
- **DND handling** — a guest signal that defers servicing (WebRezPro explicit; conceptually implied elsewhere).
- **Maintenance tickets at room level** — defects found during servicing raised as repair items (WebRezPro alarms with active/in-progress/completed; Flexkeeping and Mews ship maintenance as adjacent scope).
- **Role structure** — attendant vs supervisor/inspector vs manager; tasks assigned to employees or departments (Mews; WebRezPro zone assignment; Flexkeeping role segmentation).
- **Bulk operations and sorting/filtering of the board** (WebRezPro).

### Level 2 — Variant / Optional Structure

- **Linen/laundry management** — linen consumption/amenity tracking (Flexkeeping).
- **Lost & found** (Flexkeeping).
- **Guest-request-driven work items** — requests routed into housekeeping work (Flexkeeping "Automated Services"; guest service management).
- **Staffing forecasts / workload weighting** — forecasting labour and auto-balancing assignments (Flexkeeping); workload-credit systems are industry-practiced but were not directly evidenced in the sample (see Uncertainties).
- **Auto-dirty and sanitation rules** — vacant rooms automatically marked for service after a configured interval, sometimes regulatory (Mews, Legionella example).
- **QA/SOP programs** — digital SOPs, audit-style quality assurance suites (Flexkeeping).
- **Multi-property centralization** — group-level standards and cross-property views.
- **AI assistance** — scheduling and task automation (Flexkeeping Flexie AI; era-current).
- **Property-type semantics** — bed-level servicing in hostels, unit types for vacation rentals, campgrounds.
- **Offline/out-of-coverage mobile operation** — claimed in market but not evidenced in this sample (see Uncertainties).

### Level 3 — Vendor-specific (Research Notes only)

- Mews: exact `Dirty/Clean/Inspected/OutOfService/OutOfOrder` enum names; the overnight auto-dirty window (stated as occurring between 04:00 and 05:00, "unit" = 24h, 7-day maximum tied to Legionella regulations); resource-block add/delete API operations; "Space Status Report" naming.
- WebRezPro: dual-format report (table vs tile); two-class note system (temporary/permanent); explicit "in service (housekeeper in room)" status name; maintenance alarm lifecycle naming.
- Flexkeeping: suite packaging (Housekeeping/Maintenance/Automation/Collaboration/QA), "Flexie AI" branding, cleaning-schema automation vocabulary, customer statistics (excluded as marketing).
- YCS: "Pulse AI" intelligence layer branding.

## Rejected Findings

Considered and rejected during synthesis:

- **"Mobile app" as definitional** — rejected; the paper assignment sheet satisfies the loop (historical check), and the desk-pass evidence treats mobile as a delivery surface. Attendant update surfaces are common structure, not the invariant.
- **"Inspection" as definitional** — rejected for L0: small properties run dirty→clean directly; the inspected state is the common mature quality gate, not the minimum.
- **"PMS integration" as definitional** — rejected in API terms: in an all-in-one PMS the housekeeping loop is internal; in standalone products it crosses an API. The invariant is the data relationship (stay data in, readiness out), not the integration plumbing.
- **"Workload credits per room type"** — insufficient direct evidence in the sample; left as an Uncertainty rather than asserted.
- **"Minibar posting"** — industry-familiar but not directly observed in this sample; not asserted anywhere.
- **Cleaning-depth taxonomy (departure vs turndown vs deep clean) as a fixed standard** — products evidence "cleaning schemas" and stay-driven variants, but the specific canonical set of service types varies; kept conceptual.

## Boundary Findings

- **vs Hotel Property Management System / PMS** — the housekeeping function ships as a named module inside every full PMS (WebRezPro, Mews, YCS all carry one), and standalone products (Flexkeeping) exist as integration-dependent operations apps over the PMS's room/stay records ("Everything you see in our PMS, you see reflected in Flexkeeping"). Keep-both: the PMS is the property-wide system of record (stays, folios, distribution, rates); housekeeping is the room-servicing operations Type with its own users, object (service readiness) and loop. A PMS without the servicing loop is still a PMS (front desk + reservations + rates); a housekeeping product without its own property records is still housekeeping management.
- **vs Hotel Front Desk Application** — mirror-image boundary, now confirmed from both sides: the desk maintains occupancy and *consumes* readiness; housekeeping maintains readiness and *consumes* occupancy. Mews' API makes the split structural (separate occupancy-state and resource-state axes; housekeeping integrations write resource states, not occupancy). The desk cannot assign rooms without housekeeping's readiness; housekeeping cannot plan without the stay picture.
- **vs Property Maintenance Management / CMMS (§16–17 leaves)** — maintenance work is asset/equipment-centric repair work orders (preventive, recurring, asset histories); housekeeping is room-readiness servicing. Housekeeping *raises* room-level maintenance tickets (defect found while servicing) but the repair workflow belongs to maintenance. Market corroboration: Flexkeeping ships Maintenance as a separate suite; WebRezPro markets "Housekeeping & Maintenance" as one feature area but separates alarms from servicing.
- **vs Hotel Guest Experience Platform / Digital Concierge** — guest-facing request intake belongs to that sibling; housekeeping receives some of those requests as work items. One-way flow, different users.
- **vs Workforce Management / generic Task Management** — generic schedulers lack room-state semantics and stay-driven demand; housekeeping assignment is always over the property's room/stay structure.
- **"Remove what to become another Type"** — remove the stay-driven demand and readiness handoff → generic task management; remove the servicing loop → a room-status screen inside a PMS; remove the room/unit semantics → cleaning-services scheduling, outside the atlas.

## Uncertainties

- **Workload credits/minutes** (per-room-type effort weighting used to balance assignments) is industry-familiar but was not directly observed in any fetched source; treated as unverified, not asserted in the final document.
- **Minibar/consumables posting from housekeeping** (attendant records minibar consumption → folio) — plausible but unobserved in this sample; not asserted.
- **Offline-first attendant apps** — commonly claimed in the market; not evidenced in fetched sources; not asserted.
- **Exact depth of enterprise PMS housekeeping modules** (OPERA-class: complex credit systems, project/deep-cleaning programs) — could not be verified; claims kept at the level of the accessible sample.
- **Whether YCS/eZee's housekeeping module includes zone/credit machinery** — page not reachable; only the desk-sync FAQ was used.

## Final Synthesis

Hotel Housekeeping Management is the lodging property's room-servicing operations system. Its world has one center — the room as a serviced unit carrying a service-readiness state — powered by two flows: stay-driven demand coming in (departures, stayovers, arrivals, vacancy rules) and readiness going out to the room-assignment process. Between them runs the servicing loop: demand organized into assignments (zones, task lists, per-room-type procedures), executed by attendants (increasingly from mobile), verified (the clean→inspected quality gate), and published to the front office in real time. Around the loop stand the housekeeping board (the report combining readiness and occupancy), room-level maintenance tickets feeding out to repair workflows, and a manager layer of schedules, standards (checklists/SOPs/QA) and analytics.

The market ships this Type in two shapes: the housekeeping module inside every full PMS, and standalone housekeeping-operations suites that run against a PMS as the property system of record. Both satisfy the same core. Historically, the same core ran on a paper room board with a supervisor's inspection slip; the digital layer adds real-time sync, mobile execution, automation and analytics without changing the invariant.

Evidence calibration: the readiness lifecycle (dirty/clean/inspected), the occupancy/readiness split, stay-driven demand, attendant execution surfaces, and real-time desk sync are cross-product findings (layer B+, multiple direct observations). Zones, checklists, notes, DND, bulk operations are direct observations in one or two products, phrased as common implementations rather than requirements. Linen tracking, lost & found, AI scheduling, and the Mews dirty-status mechanics are product-specific observations.
