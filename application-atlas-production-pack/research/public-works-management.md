# Research Notes — Public Works Management

Research date: 2026-09-09
Slug: public-works-management
Directory leaf: Public Works Management (§24 Government, Public Sector & Civic)

## Research Goal

Understand what a "Public Works Management" application actually is as an Application Type: what objects exist inside it, who uses it, how work flows through it, what rules and states matter, and where its boundary sits against the heavily adjacent sibling Types in §24 and the maintenance/asset family in §16.

Prior context from already-processed sibling passes (read before research):

- **public-asset-management** (processed 2026-09-09): public-infrastructure asset estate lifecycle — asset register of record + recorded care + lifecycle outlook (repair-vs-replace, multi-year plans) under a public-stewardship frame. Left a **forward flag for this leaf**: "seam = asset-estate lifecycle vs department operations; sampled products position asset management as one system public-works teams use — to be ratified from the public-works side."
- **parks-recreation-administration**: park-as-venue vs park-as-asset seam (discharged by the PAM pass).
- **government-inspection-management**: inspection-as-managed-unit; explicitly held adjacent, not part of this Type's core.
- **facility-management-system**: recorded that FMX's public-works pole (citizens reporting street lights → dispatch) shades toward 311 / public-works territory.
- **311 / citizen-service-request-platform** leaf exists separately in the directory (unprocessed at research time) — intake venue expected to be its center.

## Initial Boundary (working hypothesis before research)

1. Core use: the municipal public-works department (streets, fleet, facilities, grounds, storm, sanitation, sometimes water/sewer) organizing its day-to-day service delivery: citizen/staff requests for service, work orders for crews, asset upkeep, cost and performance reporting to the public/budget.
2. Primary users: department operations staff (coordinators/dispatchers), field crews and supervisors, department directors, clerks; secondary: citizens submitting requests, finance/budget staff.
3. Nearest Types: Public Asset Management, 311 / Citizen Service Request Platform, CMMS / EAM, Government Inspection Management, Facility Management System, Fleet Management System, Government GIS, Capital Improvement Planning, Smart City Operations Platform, Utility Asset Management.
4. Likely boundary problem: this leaf and Public Asset Management may be one market family with two centers (estate stewardship vs department operations); suite products probably carry both.
5. Unknowns: is the service-request leg definitional or only common? Is asset data in the core or only an attachment point? How deep do seasonal operations (snow/storm) go in product machinery?

## Research Questions

1. What is the unit of demand? Where do requests come from (citizen portal, phone, staff) and what do they carry?
2. What is the unit of execution? How does a work order flow (create → assign → schedule → field complete → close) and what does it record (labor, equipment, materials, costs)?
3. What is the object of work? How are public-domain assets/locations held, and is the asset register this Type's center or an attachment point?
4. Who coordinates and who executes? What do dispatcher/office vs crew/supervisor surfaces look like?
5. What accountability outputs exist (response performance, costs, budget justification, FEMA/insurance/grant documentation) and are they definitional?
6. Which structures are era/region-specific (GIS, FEMA, 311 portals) vs timeless?
7. What exactly separates this Type from PAM, 311, CMMS, inspection management, and utility-field-service territory?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Trimble Unity Maintain (Cityworks lineage) | GIS-centric enterprise asset & work management (Cityworks + AgileAssets + Pavement Express + Unity Work Management merged) | cities → counties → state DOTs, airports, utilities |
| FMX | lightweight modern multi-tenant SaaS; public works as an industry deployment of a CMMS platform | counties, small/mid municipalities, school-district-style operators |
| iWorQ | module-suite built specifically for small local governments; public works package alongside community development package | small cities and counties (US) |

Attempted and unreachable (Source-access Limitation, not used for claims): Cartegraph (cartegraph.com 403; help.cartegraph.com transport error), Lucity (lucity.com timeout ×2; kb.lucity.com transport error), Pubworks (pubworks.com 404 — site gone), CityReporter (timeout ×2), OpenGov (403), Brightly/Siemens root reachable but its government-infrastructure product (Confirm) was already sampled by the public-asset-management pass — treated as PAM-side context, not re-sampled here.

Rejected sample: **Muni-Link** — fetched and found to be cloud utility billing / CIS (billing, payments, CIS service orders for water/wastewater utilities). Product Mismatch; useful as boundary evidence for the utility seam.

## Sources

All directly fetched 2026-09-09 (Tier 2 official product pages; Tier 1 help centers were not reachable this pass):

- Trimble Unity Maintain (Cityworks lineage) — https://www.trimble.com/en/products/trimble-unity-maintain (reached via cityworks.com redirect; includes product FAQ)
- FMX Public Works — https://www.gofmx.com/public-works-software/ ; FMX root — https://www.gofmx.com/
- iWorQ — https://iworq.com/ ; Work Management — https://iworq.com/systems/work-management-software/ ; Citizen Engagement — https://iworq.com/systems/citizen-engagement-software/
- Muni-Link (rejected) — https://muni-link.com/
- Sibling-pass context: research/public-asset-management.md, applications/public-asset-management.md (this repo)

Sourcing limitations: help.cartergaph.com, help.cityworks.com, Lucity KB all unreachable (403/transport/timeout). No Tier-1 operational documentation was obtained for any sampled product. All operational details below are calibrated to marketing/support-page specificity; no precise limits, status vocabularies, SLA timers, or permission models are claimed.

## Product Observations (evidence layer A unless noted)

### Trimble Unity Maintain (Cityworks lineage)

Positioning: "Optimize asset management... supports asset networks of all sizes, from international airports to local utilities, cities to state DOTs and healthcare to educational systems." "From inventory and work activity to performance analysis and strategic planning, ... provides one solution to manage all the built assets in your network."

Key capabilities listed: inventory management (location, condition, construction history per asset); geolocation & spatial analysis (embedded Esri ArcGIS maps, LRS support); risk assessment; predictive analytics (what-if scenarios over timelines/budgets/performance); work plan optimization; data visualization & reporting; work management ("Boost efficiency and streamline maintenance operations in the office and in the field"); work order management ("seamless field-to-office communications"); inspections ("connected data and automated workflows"); community engagement ("Empower your citizens with a public portal for community reported issues").

Operational specifics observed:
- The work-management showcase describes "a desktop interface displaying a work management dashboard with a list of service requests, work orders, and inspectors, alongside charts and numerical summaries" — service requests and work orders are first-class parallel objects.
- "Caller Information" pop-up with name, address, phone, email over a street map — requests carry reporter contact and location.
- "Consistently responding to citizen requests in a timely manner and providing visibility into work progress helps sustain public trust" — response performance framed as public accountability.
- "With visibility into maintenance records and related cost data, you can make informed decisions in real time and improve long term planning."
- "A simple, streamlined process maximizes the productivity of your workforce to efficiently manage service requests, inspections and work orders."
- FAQ: "GIS-centric" DNA — "Your GIS remains the authoritative source of truth for asset data"; Esri ArcGIS Velocity IoT sensor data can "automatically trigger work orders"; REST APIs/webhooks used to "chain work orders to municipal financial systems or HR software"; merged tech stacks (Cityworks + AgileAssets + Pavement Express + Trimble Unity Work Management); Pavement add-on "specifically designed for local governments (cities and counties) to manage streets and sidewalks."

### FMX (Public Works)

Positioning: "Public Works Software for Local Governments — Map, monitor, and maintain public assets"; "Manage public infrastructure, assets, public property, capital projects, and community events with FMX's public works management software." Key capabilities listed: asset mapping, capital planning, asset lifecycle management, community event management, maintenance management.

Operational specifics observed:
- "Visualize assets and work on a map — Via ESRI ArcGIS Online, give your team GIS mapping of daily work and asset locations."
- "Give community members an easy way to request service needs — Community members can submit requests in an easy-to-use portal. Learn about issues earlier, resolve them faster." Root-page illustration: "citizens can report broken street lights on their mobile device, knowing that field technicians will be dispatched and held accountable."
- "Centrally manage maintenance work — Manage team assignments, see work request details, set asset maintenance schedules, and monitor spare parts asset inventory."
- Feature catalog: capital planning & forecasting (status and cost of renovations/new builds/capital projects); asset & infrastructure tracking (predict asset lifespan and anticipated replacement cost); interactive maps and indoor floor plans; community service request portal; maintenance management ("Prioritize incoming work orders and manage proactive maintenance schedules to reduce deferred backlogs"); building services management; fleet management ("Request vehicle usage and track ongoing service, registrations, and expenses"); inspections & checklists; QR code tagging; grounds and park upkeep ("Schedule landscaping and building maintenance tasks and track associated costs and labor hours"); mobile app ("Technicians can access and close work requests while in the field", QR scan); worker availability ("See in progress tasks and identify field workers available for assignment"); automated assignment ("automatically assigning the technician best suited for the task"); time clock & labor tracking; cost tracking and summaries; inventory; satisfaction surveys; sensor alerts ("automatically dispatching maintenance team members following a detected equipment failure or water leak"); communication threads ("Consolidate records of emails, phone calls, and word-of-mouth conversations from multiple departments into a single thread"); events/reservations with payments.
- Reports: Work Summary Dashboard ("open, in process, and completed work"); Aged Work Requests (15/30/60/90-day backlog buckets); Reactive vs. Proactive; Comprehensive Costs; Capital Forecasting.
- Government context: county case studies (Ross County OH administrator: "I receive an email for every FMX work order... so I can expedite urgent requests"; Fairfield County OH); purchasing co-operatives (1GPA, TIPS-USA); "streamline resident service delivery."

### iWorQ (Work Management + Citizen Engagement + public-works suite)

Positioning: "Streamline Day-to-Day Tasks with Management Software Built for Community Development & Public Works Departments" — "a wide variety of CMMS solutions designed to help cities and counties run smoothly." Public works package modules: Work Management, Asset Management, Citizen Engagement, Facility Management, FEMA Reporting, Fleet Management, Pavement Management, Sign Management, Backflow Prevention, Stormwater Management, Water System Management, GIS Rest Services; plus a citizen portal.

Work Management module:
- "Work Management is a project management application that tracks the details of your work orders all in one place."
- "When included in the public works package, Work Management helps you to keep track of work being completed on an asset. When a work order is created on an asset, the data is automatically entered into your Work Management dashboard. Inventory, spending, equipment, and employee reports are a few examples of the data you can pull from the system within seconds."
- "Reporting is straightforward and can be used to budget plans or report to FEMA."
- Features: "Track time and costs of employees and equipment"; customizable forms; reports; mapping of job locations; notes, e-mails, scheduling, templates; mobile; upload images. Work-order templates pre-fill "supplies used, a description of the project, the department used to complete the order."
- FAQ: work orders "assigned to individuals or teams"; "automated text or email alerts... for new assignments or status changes"; status updates "(e.g., open, closed, pending)"; "Clerks or billing staff create work orders from the office"; "Each user has a personalized dashboard showing only their assigned work orders"; customizable fields; ad hoc reporting exported to Excel/PDF, scheduled auto-send.
- Testimonials: "receive and prioritize work orders... eliminated all paperwork... same-day response time"; "run a monthly report on maintenance... show it in our monthly meetings"; "Vastly improved labor & cost tracking for work orders"; "Established cost for work units performed"; "streamline our public works record keeping"; "capture our location request data, and give clear status updates."

Citizen Engagement module:
- "Empower citizens with online reporting and easily manage maintenance requests"; "save money on 311 services and track citizen complaints, road damage reports, infrastructure issues, maintenance requests, and internal staff tasks."
- Features: customizable fields; automatic email alerts "to the appropriate departments or personnel"; citizen photo upload; "Precise Location Tracking — GPS coordinates, drop a pin, or type the nearest address"; real-time status updates to citizens and staff; integration to other modules.
- "After the request is submitted, e-mails can be sent automatically to involved departments... Requests can then be exported to be created into a new work order or case."
- FAQ: phone requests manually entered; "You can export a request as a work order and assign it to a department or individual"; "If your agency uses Asset Management, you can attach work orders directly to tracked assets" (roads, signs); "updating a request in one will automatically update it in the other"; insurance reports for pothole claims; no resident app needed (web portal).
- Testimonial: "better coordination of Citizen requests through Citizen Request and immediate ability to manage town emergencies."

## Cross-product Comparison

| Structure | Trimble Unity Maintain | FMX | iWorQ | Reading |
|---|---|---|---|---|
| Service request as recorded demand (citizen + phone + staff intake) | ✔ dashboard object #1; caller info; citizen portal; "responding to citizen requests... public trust" | ✔ community service request portal; "resolve them faster" | ✔ Citizen Engagement module; phone entry; "track citizen complaints, road damage..." | Cross-product commonality; presented as the entry object of the department's work |
| Request → work-order conversion | implied by SR + WO pairing on one dashboard ("manage service requests, inspections and work orders") | ✔ requests become work; "technicians... dispatched and held accountable" | ✔ explicit: "export a request as a work order and assign it to a department or individual" | Cross-product commonality; the conversion is the operational pivot |
| Crew/worker assignment + notification | ✔ "inspectors" on dashboard; field-to-office communications | ✔ team assignments, automated assignment, worker availability | ✔ assign to individuals/teams; email/text alerts | Cross-product commonality |
| Work order lifecycle with completion records (labor/equipment/materials/costs) | ✔ work order management; cost data alongside maintenance records | ✔ close in field; time clock; labor tracking; cost tracking | ✔ open/closed/pending statuses; time and costs of employees and equipment; supplies in templates | Cross-product commonality; conceptual states, exact vocabularies not compared |
| Maintained public estate as object of work | ✔ "all the built assets in your network"; GIS authoritative for asset data | ✔ public infrastructure, assets, property; asset mapping | ✔ work orders created on tracked assets (roads, signs); domain modules | Cross-product commonality |
| Multi-domain department scope (infrastructure + facilities + fleet + grounds) | ✔ airports→DOTs; pavement for streets/sidewalks | ✔ building services + fleet + grounds + infrastructure in one system | ✔ facility + fleet + pavement + sign + stormwater + water modules | Cross-product commonality |
| Public accountability outputs (reports, budget/capital justification, external documentation) | ✔ cost data → "improve long term planning"; what-if funding scenarios | ✔ dashboards; capital forecasting; community transparency | ✔ monthly maintenance reports; budget plans; FEMA reporting; pothole insurance reports | Cross-product commonality, region/module-variable depth |
| GIS map as work/asset surface | ✔ native, GIS-centric pole | ✔ via ESRI ArcGIS Online integration | ✔ mapping of job locations + GIS rest services | Common; depth varies from authoritative-GIS to lightweight map |
| Capital planning / predictive asset analytics | ✔ strong (what-if, risk, work plan optimization) | ✔ capital planner + forecasting reports | ✖ not in fetched pages (budgeting tool exists in community-development package) | Optional/variant |
| Events/reservations for community | ✖ not observed | ✔ events + payments | ✖ not observed (facility scheduling not in fetched PW pages) | Optional/variant |
| FEMA / disaster cost reporting | ✖ not observed | ✖ not observed | ✔ dedicated module + Knott County case study | Region-specific variant (US) |
| Sensor/IoT auto-triggering work | ✔ ArcGIS Velocity → work orders | ✔ SensorHubb → auto work order | ✖ not observed | Optional |

## L0 — Defining Invariant

Three jointly-held structures, held by a public-agency operator:

1. **The service request as the unit of demand intake.** A persistent, recorded, located request for public-works response — reported by a citizen (portal, phone taken by staff, app) or raised internally — carrying issue type, location, reporter contact (and commonly a photo), triaged/prioritized and routed, with status visible back to the requester. Remove it → internal-only CMMS / complaint log; the public-facing service-delivery loop collapses.
2. **The crew work order as the unit of execution.** A planned or request-derived work order binding work type + asset/location + assigned crew/worker(s) + schedule, advancing through a lifecycle (open → assigned/scheduled → in progress → completed/closed) and recording labor, equipment, materials and cost at completion. Remove it → a request log or asset registry with no operations.
3. **The maintained public estate as the object of work.** Work attaches to the public-domain assets and locations the agency stewards — streets/pavement, signs, street lights, storm/drainage infrastructure, grounds, public buildings, fleet — and completed work accumulates as per-object history across the department's multiple service domains. Remove it → generic ticketing + work-order SaaS.

Public-agency operator posture is part of the Type's identity frame (as in the PAM pass): the records exist to demonstrate service delivery and justify spending to the public — response performance to citizens, costs to the budget process — with FEMA/insurance/grant documentation as regime-specific expressions. Remove the frame → generic field service / CMMS.

Jointly-held load-bearing tests:
- 1 alone = 311 / citizen-request intake venue territory.
- 2 without 1 = CMMS / field-service territory.
- 3 without 1+2 = bare asset registry (or the PAM spine without operations).
- 1+2 without 3 = generic request+work-order SaaS.
- 2+3 without 1 = per-asset care loop (PAM's recorded-care leg).
- 1+3 without 2 = intake portal with a map and nothing executed.

## L1 — Common Mature Structure

Present across the researched sample; expected in mature products, not definitional:

- asset/inventory records for the maintained estate (location, class, condition, history) that requests and work orders attach to
- citizen/self-service request portal with notifications and real-time status visibility; staff intake for phone/walk-in reports
- automatic assignment notifications (email/text) to crews/individuals; personalized "my work" dashboards
- planned/preventive maintenance schedules alongside demand-driven work
- inspections and checklists tied to assets or work
- cost accounting on work orders (labor hours × cost, equipment time, materials/supplies) with exportable reports
- mobile field app: view assigned work, navigate to location, attach photos, complete/close work, QR/barcode asset lookup
- GIS mapping of assets and work (from authoritative-GIS to lightweight map layers)
- reporting/dashboards: open/in-progress/completed, aging/backlog buckets, reactive-vs-proactive mix, cost summaries
- photo/file attachments, notes, communication threads; work-order templates for recurring job types
- parts/inventory tracking feeding work orders
- multi-domain scope in one system (streets + facilities + fleet + grounds under one department roof)

## L2 — Variant / Optional Structure

- capital planning & predictive asset analytics (lifespan forecasting, what-if funding scenarios, risk scoring) — strong at the enterprise pole, absent/light at the small-city pole
- FEMA / disaster cost-recovery reporting — US federal-disaster regime (iWorQ only, in-sample)
- insurance/liability reporting (pothole claim documentation) — regime-specific output
- seasonal and emergency mobilization programs (snow/ice, storm response) — part of the department's operating reality; dedicated machinery (routes, events, storm work codes) was **not directly evidenced** in fetched sources this pass; treat as probable variant, unverified
- community events/reservations and payment processing (FMX)
- utility-domain modules (stormwater, water, backflow) for departments that also run utilities (iWorQ)
- fleet depth (usage requests, registrations, vehicle inspections feeding work)
- IoT/sensor auto-dispatch of work orders
- satisfaction surveys after completed work
- internal service billing between departments (weak evidence — FMX invoices generically; unclaimed)
- GIS posture: GIS-centric (asset data authoritative in GIS) vs map-integrated vs light mapping

## L3 — Vendor-specific Structure (research notes only)

- Trimble Unity Maintain: Cityworks + AgileAssets + Pavement Express + Unity Work Management merger; LRS support; Esri ArcGIS Velocity auto-WO; "GIS remains the authoritative source of truth"; Pavement as turnkey local-government add-on; Unity suite siblings (Permit, Construct, Field).
- FMX: named modules (Work Manager, Capital Planner, Fleet Manager, Warehouse Manager, IT Asset Manager); SensorHubb and Zonar integrations; EventSync BAS integration; Stripe payment processing; purchasing co-ops (1GPA, TIPS-USA); "no per-seat"-style pricing claims absent but support/training positioning.
- iWorQ: module family names (Portal Home, XworQ AI); AWS GovCloud hosting; "first web-based solution for local governments" (since 2001); no-per-seat pricing; unlimited training/support positioning; FEMA Reporting module.
- Muni-Link (rejected): utility billing/CIS with service orders — illustrates the utility-side seam.

## Vendor-specific Findings

See L3. None of these enter the canonical model.

## Rejected Findings

- "Public works software = utility billing + service orders" — rejected: Muni-Link's service orders hang off customer accounts/meters, not the public estate or citizen requests for service. Product mismatch recorded.
- "Public works management = CMMS for government" — rejected as the whole story: private CMMS centers on owned equipment maintenance; the researched public-works products all carry the citizen/staff demand loop and public-accountability outputs as first-class structures. CMMS machinery (work orders, PM, inventory) is shared substrate, not the differentiator.
- "Asset register is the center of this Type" — rejected: asset records are ubiquitous but function as attachment points for demand and work; the estate's stewardship lifecycle (condition → repair-vs-replace → multi-year plan) belongs to the PAM center. Sampling products themselves position "asset management" as one system public-works teams use (matches the PAM pass's reading).
- "GIS-centricity is definitional" — rejected: one pole is GIS-authoritative, another integrates Esri maps, a third maps job locations without a GIS-center claim.

## Boundary Findings

1. **vs Public Asset Management (PAM)** — the closest sibling; the seam is a center-of-gravity seam, ratified here from this side: PAM centers the estate's stewardship record (register + condition + lifecycle outlook + long-term plans); this Type centers the department's service-delivery operation (demand intake → triage/dispatch → crew completion → cost/history), with the estate as object of work. Suite-class products (Cartegraph/Cityworks/Confirm-class) legitimately carry both faces; a product without the demand/dispatch operations center is PAM territory; a product without per-asset stewardship outlook can still be fully this Type (FMX, iWorQ poles).
2. **vs 311 / Citizen Service Request Platform** — the 311 leaf centers the intake venue and complaint lifecycle (case handling, transparency); here the request record exists to be converted into crew work and resolved, with work outcomes flowing back. Remove work execution → 311 territory. iWorQ's own framing ("save money on 311 services") shows the market sees them as complements.
3. **vs CMMS / EAM (§16)** — shared machinery (work orders, PM, inventory, assets); differentiators are the demand loop from the public, the public-domain estate, multi-domain department scope, and public-accountability outputs. Remove those → CMMS.
4. **vs Government Inspection Management** — inspection program as regulatory managed unit (planned examinations against criteria, outcomes/violations) vs service delivery; inspections appear here as common modules tied to work/assets, not as the managed unit.
5. **vs Facility Management System** — facility-centered vs domain-wide department operations; facilities are one domain among many here (FMX straddles both markets).
6. **vs Fleet Management System** — vehicle-centered subset; fleet appears here as one service domain module.
7. **vs Government GIS** — spatial data platform vs work management; the GIS-centric pole's posture ("GIS is authoritative") is an integration stance, not identity.
8. **vs Capital Improvement Planning** — capital project/program decisions vs recurring operations; capital planning appears here as an optional module consuming operations data.
9. **vs Utility Asset Management / Utility Field Service** — utility network estate + utility operations (CIS service orders, meter-to-cash) vs municipal multi-domain operations; Muni-Link sampling confirmed the utility-billing side is a different world.
10. **vs Smart City Operations Platform** — sensing/eventing/monitoring vs executing work; IoT auto-triggering of work orders is the integration seam.
11. **vs Parks & Recreation Administration** — venue/program administration vs maintenance/operations of the estate; parks crews may be tenants of this Type in their maintenance role.

## Historical / Market-Sample Check (§24)

Paper-era DPW: complaint slips / complaint card file at the counter (demand intake with location + reporter); work order pads / duplicate job tickets with crew assignment, time sheets and equipment logs (execution with labor/equipment record); street/sign/storm inventory card files and the streets themselves (the maintained estate); the annual department report to council with work accomplished and costs (public accountability). All three legs hold with no software. Older/regional: 1990s–2000s local work-order systems for DPWs; UK "highways maintenance" practice; Australian/NZ council "works & assets" practice — same frame without US FEMA machinery. The definition does not depend on GIS, cloud, citizen web portals, phone apps, or FEMA. No era/region over-fit detected.

## Uncertainties

1. No Tier-1 help-center documentation was reachable for any sampled product (Cityworks help 403; Cartegraph 403; Lucity KB transport error). Exact request-merging behavior, SLA timers, permission models, and status vocabularies are unverified — final document stays conceptual.
2. Seasonal operations machinery (snow routes, storm events) not directly evidenced; recorded as probable variant only.
3. Crew-level dispatch-board UI details not directly observed (no Tier-1 screenshots/docs).
4. Internal cost transfer between departments: weak evidence; unclaimed.
5. Market breadth beyond the three sampled products rests partly on the PAM pass's independently-sampled products (Cartegraph, Confirm, Assetic) — cross-pass context, not this pass's own observation.
6. Whether any pure "public works operations" product exists with no asset records at all — none encountered; treated as unlikely but unverified.

## Final Synthesis

The Application Type is the **public-works department's service-delivery operations system**: it takes demand for service (from citizens and staff), turns it into crew-executed work on the maintained public estate, records execution with labor/equipment/material/cost, and reports performance and costs outward to citizens, management, and the budget process. The defining core is the request→work→estate loop; the asset-management stewardship spine (condition, lifecycle outlook, long-term plans), GIS-centricity, capital analytics, FEMA reporting, and seasonal programs are common-to-variant structures around that core. The PAM forward flag is **RATIFIED**: estate stewardship vs department operations is the seam; suite products carry both faces.
