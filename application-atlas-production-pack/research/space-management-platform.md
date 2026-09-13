# Research Notes — Space Management Platform

Leaf: Space Management Platform (DIRECTORY.md §10 Enterprise Operations & Administration)
Slug: space-management-platform
Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

---

## Research Goal

Understand what a Space Management Platform actually is from real products: what its system of record is, what operations users perform on it, which capabilities are definitional vs. merely common in the current market, and where its boundaries sit against IWMS suites, workplace-management platforms, facility management systems, booking tools, and asset registries.

## Initial Boundary

Working hypothesis before research:

- Core use: an organization-facing system of record for its physical space inventory (buildings → floors → rooms/desks), tracking who/what is allocated where, planning and executing space changes (moves, re-allocations, scenarios), and reporting occupancy/utilization.
- Likely users: corporate real estate, facilities, and workplace teams; space planners; move coordinators; secondarily employees (booking surfaces in modern products).
- Nearest types: Space & Occupancy Management (§17), IWMS (§17), Facility Management System (§17), Workplace Management Platform (§10 sibling), Office Operations Platform (§10 sibling), Resource Calendar (§03.08), Enterprise Asset Registry (§10, processed), Amenity Booking Platform (§17, processed), Coworking/Flexible Workspace Management (§17, processed), Hotel PMS (§26), Lease Administration (§17), Architecture Design / CAD (§16).
- Known unknowns: whether floor-plan anchoring is definitional or merely universal; whether booking/hoteling is core or an implementation-era layer; whether §10 "Space Management Platform" and §17 "Space & Occupancy Management" are the same Type; how much of the market has consolidated under one vendor family.

## Research Questions

1. What is the system of record — how is the space inventory structured (hierarchy, space types, attributes)?
2. What role do floor plans play — view/edit surface? CAD/BIM integration? Is plan-anchoring definitional?
3. How is allocation modeled — assigned vs. bookable vs. shared; allocation to people, departments, teams, neighborhoods?
4. What operations change space state — seat assignment, moves/adds/changes (MAC), block & stack, scenario planning, booking, check-in?
5. What analytics exist — occupancy, utilization, headcount vs. capacity, chargeback/cost allocation, forecasting?
6. Who uses which surface — planner console, admin, employee booking portal, mobile/kiosk?
7. What rules govern behavior — allocation semantics, booking policies, approval workflows, roles?
8. Boundaries: vs. booking-only tools, FM/CAFM/IWMS suites, workplace management platforms, asset registries, CAD authoring tools, hospitality PMS.

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different customer tiers:

| Product | Philosophy / posture | Tier | Evidence depth reached |
|---|---|---|---|
| OfficeSpace Software | Pure-play space planning + workplace platform, planner-first (block & stack, MAC) | Mid-market → enterprise | Tier 2 (home + feature pages: stack plans, move management) |
| SpaceIQ (SiQ, now Eptura) | Pure-play space management SaaS (planning + forecasting + move orders) | Mid-market → enterprise | Tier 1 (vendor knowledge center: full admin/employee doc tree) + Tier 2 |
| FM:Systems (FM:Interact, now Johnson Controls OpenBlue) | IWMS lineage, space management as named product line | Enterprise (corporate, gov, higher ed, healthcare) | Tier 2 (home + Space Management product page) |
| Archibus (now Eptura Archibus) | Classic CAD/BIM-integrated IWMS, space planning module | Large enterprise / government (FedRAMP) | Tier 2 only (Eptura product page; vendor docs not fetched) |
| Robin | Modern workplace-operations platform, booking-first + occupancy analytics | Mid-market → enterprise | Tier 2 (home + space-management page); help center unreachable |

Market-structure note (A, observed): Archibus, SpaceIQ, and Serraview have all been consolidated under the Eptura brand; FM:Systems is now part of Johnson Controls (OpenBlue). The category consolidates into large workplace/FM platforms, but space management remains a named, separable product line in each.

## Sources

All fetched 2026-09-08. Fetch environment could not render Salesforce Lightning help centers.

- OfficeSpace Software — home, Block & Stack Planning, Move Management pages: https://www.officespacesoftware.com/ , https://www.officespacesoftware.com/features/stack-plans/ , https://www.officespacesoftware.com/features/move-management/ (Tier 2). Help center https://workplace.officespacesoftware.com/s/ failed (Salesforce CSS error).
- SpaceIQ (Eptura) — Knowledge Center root: https://knowledge.eptura.com/SiQ (Tier 1); migration page https://spaceiq.com/ (Tier 2).
- FM:Systems — home + Space Management product page: https://fmsystems.com/ , https://fmsystems.com/products/workplace-management-solutions/space-management/ (Tier 2).
- Eptura (Archibus) — home + Archibus product page: https://eptura.com/ , https://eptura.com/our-platform/archibus/ (Tier 2). https://www.archibus.net/ returned 404.
- Robin — home + Space Management page: https://robinpowered.com/ , https://robinpowered.com/platform/space-management (Tier 2). Help center https://support.robinpowered.com/ transport error.

Source-access limitation: OfficeSpace and Robin help centers were unreachable (1 attempt each; per network rules not retried further). Archibus operational documentation was not fetched; Archibus claims below rest on its current product page only. Assertions are calibrated accordingly; no precise operational numbers are inferred from model memory.

---

## Product Observations

### OfficeSpace Software (evidence layer A unless noted)

- Positions a "Space Management" feature family: Block & Stack Planning, Moves Adds & Changes (MAC), Scenario Planning, OfficeSpace Studio (floor-plan tooling), AI Canvas. Adjacent families: Workplace Management (desk/room booking, wayfinding, neighborhoods, visitor management, facility requests), Workplace Analytics (reporting, "Workplace Intelligence"), Asset Management.
- Block & stack: "Visualize floor plans — see how departments and teams are allocated across floors and sites"; drag-and-drop teams via an "allocation queue", "instantly block out seats for teams or departments on the floor plan"; "create unlimited stack plans to build 'what-if' scenarios and seating configurations".
- MAC: "Manage ad hoc seat changes and large-scale relocations in a single platform. Highlight seats and drag and drop seating assignments on a digital floor plan"; move requests generated by dragging names on floor plans; configurable space-type tags and headcount-capacity data used to query/consolidate move plans; move instructions for IT, HR, facilities, movers, and employees; new-hire and termination "smart queues" fed by HRIS sync (Workday, SuccessFactors, BambooHR); employee move requests with review/approval workflows that auto-update location and dates; move history reports.
- Seat inventory semantics: "measure seat inventories by type, including assigned, bookable, reverse hoteling, vacant, and more"; control booking limits; define space, seating, and neighborhood settings.
- Occupancy/utilization analytics "directly on the floor plan"; Workplace Intelligence = usage and attendance insights from bookings and badging data (customer quote confirms bookings + badge data feeds).
- Integrations: HRIS (headcount assumptions), directories (Okta/Azure AD — "streamlined communication during moves"), SSO, roles and permissions; calendar (M365/Google), sensors partner logos (VergeSense et al.).
- FAQ defines block & stack as the method "used by space planners and facilities managers to visualize and plan the physical spaces within a building or across their real estate portfolio"; MAC defined as "updating employee seating assignments on floor plans" against "facility management systems of record"; positioning includes "single source of truth for move plans".
- Customer quotes evidence practice: moves (Dropbox "quick, one-off moves… and large-scale moves"), space allocation (banking), real-time density checking, real-estate right-sizing (HUB: cut real-estate costs ~20% — vendor-published, B for the practice not the number).

### SpaceIQ / SiQ (evidence layer A — Tier 1 knowledge center)

Full admin and employee documentation tree observed:

- Dashboard and Portfolio: Dashboard Summary, Global Map, Portfolio View, "View a Building and Floor's Seat Usage".
- Planning and Forecasting → Stacking: stack one or multiple buildings; view occupancy and seat availability; team breakdown; move departments; update number of seats; apply a projection plan onto the stack; export stack plan to CSV; undo moves/reset/clear building. Projections: by interval, by department, by building, by floor. Costs: cost overview.
- Move Orders: overview; manage move plans (add via floor map, add via move-order import, alternative move plan, duplicate, commit to a move plan); manage moves (search, tags, reschedule, cancel, send "moving day email", download move list, complete/reactivate/finish moves).
- Floor Map: overview (filter by location, read seating plans, search the floor map, floor-map colors, select/deselect seats); Manage Seats and Employees on Floor Maps → Allocation and Seats (understand departments, workplace groups, and neighborhoods); bulk-import employees to seats; Seating Charts for Fixed Desks (assign employees to seats, allocate a team or project team, unseat, move seated employees, share the assigned seat with the employee); Seating Charts for Flexible Desks (allocate seats to a neighborhood, to team(s), to a project team); Seating Charts for Hoteling Seats (allow all employees to book, allocate a department/workplace group to book, convert department/workplace-group/neighborhood desks to hoteling); Unallocate Seats; Manage Floor Map Spaces → Seat Usage Types (Reserved Desk, Secondary Seat, Shared Desk, Hot Desk — changeable per seat); Update Space Assets; Update Space Labels; Download floor map (with department occupancy, as image).
- Map Editor: floor-map editor controls; space icons (work space, office, kitchen, meeting room); space types; space codes (view/renumber); pins/points of interest (first aid, fire extinguisher, first responder, compass); text; devices (meeting-room device, wayfinder kiosk); furniture blocks.
- Employee surfaces: book own desk / hoteling desk / next to a coworker / desk with assets; recurring bookings; edit/cancel/share; check-in (with health check, from email notification, via QR code); book meeting rooms (future + ad hoc); quick search for person/space; find out who is coming into the office; customize floor-map views; book for someone else (Booking Manager); maintenance tickets incl. "request to move your desk location"; mobile app; kiosk touchscreen mode.
- Roles & Permissions: user role matrix; roles overview. Integrations section. SSO login.
- Migration page (Tier 2): "view workspace usage, update floorplans, plan office moves"; "consolidate space, map neighborhood seating for teams, explore alternative floorplans across multiple office scenarios, stack plan or reshuffle floors or buildings, and proactively plan office moves"; "global map views… badging and building attendance reports… lease management and forecast needs by headcount, department, or building"; employee "hot desking, hoteling, and meeting room booking calendar integrations… digital displays and mobile wayfinding".

### FM:Systems / FM:Interact (evidence layer A for product-page claims)

- Product line structure (Johnson Controls OpenBlue packaging): OpenBlue Workplace = Space Management, Move Management, Strategic Planning (scenario planning), Real Estate & Lease, Project Management; OpenBlue Facility Operations = facility management, maintenance, asset management, work orders, PM, sustainability; OpenBlue Employee = workplace experience, desk booking, interactive floorplans, room scheduling, catering/services, panels & kiosks, visitor management; OpenBlue Insights = portfolio analytics, utilization analytics, booking analytics, sensor analytics, environmental monitoring, dashboards, performance scoring.
- Space Management product page: "Space management involves the management of a company's physical space inventory"; users "facility professionals, department liaisons and executive management"; "tracking and maintaining your space allocation and occupancy information — identifying who sits where, understanding how much types of space your organization has, how it is categorized, how it's being used, and projecting and forecasting how much real estate you will need in the future"; "managing occupancy, allocations and chargebacks"; "bi-directionally integrated with existing AutoCAD drawings or Revit models"; "scenario modeling for floor plans"; cloud access, "on-the-fly reporting and data visualizations", automated space reports; lease and move management modules; scenario planning module.
- Industries: corporate, finance, government, healthcare, higher education, technology.

### Archibus / Eptura Archibus (evidence layer A for page claims; depth limited)

- Positioned as "IWMS for complex environments" (FedRAMP Authorized option; sold via partners): facility management tasks — maintenance, space planning, asset tracking — from one dashboard; "BIM-powered asset management" with BIM Viewer for spaces and equipment; field-technician app; capital project tracking; "Space planning and hybrid work — visualize, plan, and manage workspaces with drag-and-drop layouts and BIM integration. Support hybrid teams, maximize utilization"; workspace booking (rooms/desks, find colleagues, services); lease and contract management; Autodesk/BIM/GIS/Microsoft integrations; government pitch: "reallocate costs and optimize every square foot", real-time space analytics and automated reporting. Customer stories: NOAA (space insights, cost reduction), UMass Medical (lease cycle), SDG&E (asset uptime).

### Robin (evidence layer A for page claims)

- Platform: Resource booking ("book desks, rooms, lockers, parking and more with AI"), Space management ("collaboratively plan, edit and execute office updates"; "plan and adjust floor layouts"; "optimize every square foot with AI-driven recommendations"), Meeting management, Workplace analytics ("real-time insights, track utilization and forecast needs"), Visitor management, Employee experience.
- Space-management page: scenario planning — "collaboratively create and update floor plans. Draft, plan, and publish layouts as your offices evolve with an intuitive editor. Assign resources, execute moves and manage workplace transitions"; "Manage moves and expansions — collaboratively plan and execute office moves and workplace transitions"; resource management — "define and adjust collaborative areas"; space structure features: Neighborhoods ("organize spaces by team, role, or work style"), Shared assigned desks ("flexible, split desk assignments"), Priority booking, Workplace ticketing (catering/IT attached to reservations), Customizable reports, Occupancy tracking ("connect badge data and sensors"), Wayfinding, Collaborative drafting ("plan updates together and track changes with shareable drafts").
- Interfaces shown: map/floor editor with desk neighborhoods; adding desks and assigning them; assigned-spaces UI; executive insights; calendar integrations (Microsoft 365, Google).

---

## Cross-product Comparison

| Dimension | OfficeSpace | SpaceIQ/SiQ | FM:Systems | Archibus | Robin |
|---|---|---|---|---|---|
| Space inventory of record (site→building→floor→space/seat, types/attributes) | ✓ floors/sites, seat inventories, space-type tags | ✓ locations→buildings→floors→seats, space types, space codes, labels | ✓ "physical space inventory", categories | ✓ space portfolio with BIM models | ✓ spaces, floors/maps |
| Floor-plan anchoring | ✓ digital floor plans, Studio editor, unlimited plan changes service | ✓ Floor Map + Map Editor (icons, pins, furniture, renumbering) | ✓ AutoCAD/Revit bi-directional + interactive floorplans | ✓ BIM integration, drag-and-drop layouts | ✓ map editor, floor layouts, collaborative drafts |
| Allocation & occupancy state | ✓ assigned/bookable/reverse-hoteling/vacant; neighborhoods; booking limits | ✓ fixed/flexible/hoteling seating charts; reserved/secondary/shared/hot; departments, workplace groups, neighborhoods | ✓ "who sits where", allocations, occupancy | ✓ space allocation; hybrid support | ✓ assigned/shared desks, neighborhoods, priority booking |
| Space-changing operations | ✓ MAC: move requests, approvals, instructions, move history | ✓ Move Orders: plans → commit → execute → finish; imports; moving-day comms | ✓ Move Management module | ✓ moves coordinated in space planning | ✓ "execute moves and workplace transitions" |
| Planning (block & stack / scenario / forecast) | ✓ stack plans, unlimited scenarios, headcount forecasting | ✓ Stacking, Projections (by dept/building/floor/interval) | ✓ Strategic Planning module | ✓ space planning | ✓ scenario planning, AI layout suggestions |
| Booking (desk/room) | ✓ desk + room booking modules | ✓ desk/room booking, check-in, QR, kiosk | ✓ Desk Booking + Room Scheduling (separate product line) | ✓ workspace booking feature | ✓ resource booking core |
| Occupancy/utilization analytics | ✓ Workplace Intelligence (bookings + badging) | ✓ seat usage, badging/attendance reports | ✓ Utilization/Sensor/Booking analytics (separate line) | ✓ real-time analytics | ✓ occupancy via badge + sensors |
| Cost / chargeback / lease | ✓ real-estate cost claims; lease view (quote) | ✓ Costs; lease management | ✓ chargebacks; Real Estate & Lease module | ✓ cost reallocation; lease management | ✓ right-size spend |
| Org-data integration | ✓ HRIS + directories + calendar | ✓ bulk imports; calendar integrations | ✓ enterprise integrations | ✓ HR/finance/Autodesk/GIS | ✓ Microsoft/Google + access control |
| Roles & permissions | ✓ roles/permissions, SSO | ✓ role matrix | ✓ (implied by product lines) | ✓ (enterprise posture) | ✓ admin console (implied) |
| CAD/BIM integration named | own editor | own editor | AutoCAD/Revit bi-directional | BIM/Autodesk alliance | own editor |
| Sensors/badging | partner integrations | badging reports | sensor analytics line | IoT integrations | badge + sensors |
| AI features | AI Canvas, Space Planning Agent | (legacy) | — | Eptura AI | AI assistant, layout suggestions |

Reading: every sampled product holds all four candidate defining structures (inventory, plan-anchoring, allocation state, space-changing operations) — layer B. Booking, analytics, sensors, cost/chargeback, planning depth, and CAD/BIM mechanics vary in weight and packaging — layer B for commonality, but not definitional (see historical check).

## Canonical Model — Four-Level Abstraction

### L0 — Defining Invariant (deliberately small; jointly held)

1. **Space inventory of record** — a persistent, structured registry of the organization's physical spaces, hierarchically organized (site/campus → building → floor → spaces/seats), each individually identified with type and attributes (capacity, area, category). Remove → a drawing tool, a spreadsheet, or an asset list; not space management.
2. **Plan-anchored spatial representation** — the inventory is bound to a spatial representation of the physical layout (interactive floor plans in modern products; CAD/BIM drawings in older ones) through which spaces are browsed, edited, and reported. Remove → a generic facilities database or asset registry; the space discipline lives in the geometry.
3. **Allocation & occupancy state** — each space carries managed state binding it to the organization: assigned to a person, allocated to a department/team/neighborhood, bookable, shared, or vacant — i.e., the maintained org↔space map ("who sits where"). Remove → a floor-plan viewer or real-estate listing.
4. **Space-changing operations against the record** — the system executes and tracks changes to that state: seat assignments/re-allocations, moves (MAC), block re-allocations, and bookings on bookable spaces — recorded against the inventory, not applied elsewhere. Remove → a static snapshot or BI view, not a management system.

Jointly-held is load-bearing: 1+2 without 3 = CAD viewer; 3+4 without 1 = booking tool; 1+3 without 4 = space registry/snapshot; 1+4 without 2 = generic facilities database.

### L1 — Common Mature Structure (very common, not definitional)

- Scenario / stack planning (block & stack, what-if layouts, projections/forecasting by headcount/department/floor)
- Move management machinery (move plans vs. orders, approval workflows, move-day communications, move history/reports) — the mature packaging of L0-4
- Employee booking surfaces (desk/hoteling/room booking, check-in, kiosk/mobile) over the bookable part of the inventory
- Utilization & occupancy analytics (booking/badge/sensor feeds), dashboards, automated reports
- Org-data integrations (HRIS headcount sync, directories, calendar systems)
- Roles & permissions (planner/admin/employee split)
- Cost & lease surfaces (chargebacks, space cost, lease/portfolio views) at least as a light layer

### L2 — Variant / Optional Structure (segment-, scale-, deployment-dependent)

- CAD/BIM integration depth (own editor vs. AutoCAD/Revit bi-directional vs. BIM viewer)
- Sensor/badging-based real-time occupancy as a first-class data source
- Seat-usage-type vocabularies (hot desk / hoteling / reserved / secondary / shared) — vary per product; concept of usage types is common, exact taxonomy is not
- Chargeback and portfolio-cost machinery depth (heavy in government/enterprise, light elsewhere)
- Industry scoping (corporate office vs. government/healthcare/higher-ed portfolios)
- On-premise vs. SaaS delivery; FedRAMP-style government authorization
- AI assistance (layout suggestions, agents, forecasting) — current-market layer

### L3 — Vendor-specific (research notes only)

- OfficeSpace: AI Canvas agent family (Space Planning Agent, WEX/Insights/Facilities Agents); "OfficeSpace Studio"; 35-day implementation claims; "unlimited floor plan changes" professional-services framing; seat-type label "reverse hoteling".
- SpaceIQ: kiosk touchscreen mode; health-check check-ins (COVID-era artifact); "Moving Day Email"; furniture blocks; space-code renumbering; CSV stack export.
- FM:Systems: OpenBlue packaging under Johnson Controls; performance scoring; catering/panels/kiosks line.
- Archibus: FedRAMP authorization; partner-only sales; BIM Viewer; OnSite technician app; capital project management.
- Robin: Gartner MQ positioning; priority booking; workplace ticketing attached to reservations; AI assistant.

## Historical / Market-Sample Check (per §24 reasoning)

- Older CAD-era lineage (FM:Interact, Archibus — 1980s–90s CAFM/IWMS generation): plan-anchored space inventory + allocation + MAC + chargeback, no employee booking, no sensors, no AI. Fits L0. ✓
- Pre-software practice: paper floor plans with pinned space registers, manual "spacewalks" audits (the practice OfficeSpace's FAQ says the software eliminates). A clerk with a floor plan and an allocation register performs L0's structures manually. ✓
- Regional/platform variation: no mobile-first-only pattern exists; mobile apps are companion surfaces. Non-office industries (healthcare, universities, government portfolios) use the same structure with different space-type vocabularies. ✓
- Conclusion: L0 survives the historical check; booking/hoteling, sensors, AI, HRIS sync, and cloud delivery stay out of the definition.

## Vendor-specific Findings

See L3 above. Also: category consolidation (Archibus + SpaceIQ + Serraview → Eptura; FM:Systems → Johnson Controls) is a market fact worth recording — the Type is most often sold as a named product line of a broader workplace/FM platform, but pure-plays exist (OfficeSpace, historically SiQ).

## Boundary Findings

- **vs. Space & Occupancy Management (§17 leaf)**: FM:Systems' own page titles space management as "complete visibility into space and occupancy"; OfficeSpace describes "space and occupancy planning" as MAC's context; the market treats the phrases as the same domain. Strong likelihood the two directory leaves denote one Type. → Taxonomy note recorded; both leaves kept, alias suspected.
- **vs. Integrated Workplace Management System / IWMS (§17)**: IWMS bundles space management with facility maintenance, assets, lease, projects, sustainability (directly evidenced in FM:Systems and Archibus packaging). Space management is the space-domain module; relationship = contained capability, not duplicate Type.
- **vs. Workplace Management Platform (§10 sibling)**: workplace management centers employee-experience + workplace operations (booking, visitors, service requests, announcements); space management centers the space inventory and allocation discipline. Sampled vendors structure their products exactly this way (OfficeSpace: "Space Management" vs "Workplace Management" families; FM:Systems: OpenBlue Workplace vs OpenBlue Employee; Robin: space management as one platform module). Adjacent, keep-both.
- **vs. Facility Management System (§17)**: FMS centers building operations/maintenance/work orders; space management centers inventory/allocation/occupancy. They co-exist as product lines inside the same vendors. Adjacent.
- **vs. Desk booking / Room scheduling / Resource Calendar (§03.08)**: booking tools manage temporal reservations of bookable resources consumed via free/busy; space management owns the comprehensive spatial inventory and the allocation layer from which bookable spaces derive, and adds planning/moves. A booking tool without inventory/allocation/planning is a different, narrower Type; in mature platforms booking is a surface over the space inventory (SpaceIQ knowledge center shows booking docs nested under the employee surface of the space platform).
- **vs. Enterprise Asset Registry (§10, processed)**: registry centers durable per-item movable-asset records with custody flows; spaces are places, not items. Space platforms often add asset modules (OfficeSpace, Archibus, FM:Systems) but the space record is the anchor. Distinct.
- **vs. Coworking / Flexible Workspace Management (§17, processed)**: that Type is operator-side (memberships, billing, member CRM); space management is occupant-organization-side (planning, allocation, moves). Different seat and different objects of record. Distinct.
- **vs. Hotel PMS (§26)**: transient hospitality stays vs. organizational space allocation; different objects (reservation/stay/folio vs. space/allocation/move). Distinct.
- **vs. Architecture Design / CAD (§16)**: authoring building designs vs. operating the occupied-space record. Space platforms import CAD/BIM; they do not author construction documents. Distinct.
- **vs. Lease Administration (§17)**: lease administration centers the lease/financial obligation record; space platforms carry lease as a portfolio-cost surface (FM:Systems Real Estate & Lease; Archibus lease management) but the defining record is the space. Distinct; overlap noted.

**Removal test for the Type itself**: strip the floor-plan anchoring → generic facilities database; strip allocation state → CAD viewer; strip space-changing operations → space BI dashboard; strip the inventory → booking tool. Each strip lands in a different neighboring Type, confirming the four-part L0.

## Uncertainties

1. OfficeSpace and Robin operational documentation (help centers) unreachable; their observations rest on Tier 2 product pages — no precise limits/defaults claimed for them.
2. Archibus evidence limited to its current Eptura product page; the historical CAD-era module structure is corroborated indirectly (FM:Systems page for CAD integration; Archibus page for BIM) but not from Archibus's own docs.
3. Exact seat-usage-type vocabularies differ per product (OfficeSpace's "reverse hoteling" vs. SiQ's reserved/secondary/shared/hot vs. hoteling): the concept of seat usage types is cross-product common (B), exact taxonomies are product-specific (L3).
4. Whether the market majority reads "Space Management Platform" as including employee booking (post-2020 hybrid-work packaging) or as planner-only — packaging varies; the definition deliberately excludes booking from the core.
5. Serraview not directly researched (only its Eptura positioning line observed); its "visual block and stack" practice is consistent with the model but rests on one sentence.

## Final Synthesis

A Space Management Platform is the occupant-organization's system of record for its physical space inventory: structured, individually identified spaces bound to building/floor plans; each carrying managed allocation/occupancy state (who sits where, what is bookable, what is vacant); operated on through space-changing operations (seat assignments, moves, re-allocations, bookings); commonly extended with scenario/stack planning, move-order machinery, employee booking surfaces, utilization analytics, HRIS/calendar/CAD-BIM integrations, and cost/chargeback reporting. Its identity sits in the four jointly-held structures; everything else is common mature structure or variant.
