# Research Notes — Facility Management System

Research date: 2026-09-08
Slug: facility-management-system
Directory location: §17 Construction, Real Estate & Facilities (between "Integrated Workplace Management System / IWMS" and "Space & Occupancy Management")

---

## Research Goal

Understand what a Facility Management System (FMS) actually is as an Application Type: what objects exist inside it, who uses it, how facility work flows, which structures are defining (L0), which are common mature structure (L1), which are variant/optional (L2), and which are vendor-specific (L3). Resolve the dense seam neighborhood: CMMS, EAM, IWMS, space management, building maintenance, BMS, property management, field service.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: FMS = the operator-side system for running an organization's own buildings — building-estate-anchored work management (maintenance/service requests) plus the wider facility-operations span (inspections, scheduling, vendors, costs).
- Neighbors expected: CMMS (machinery-generic), IWMS (enterprise suite), space management (inventory/allocation), property management (income/tenancy side), BMS (OT control layer), building asset management (asset lifecycle/capital), field service (provider side).
- Prior passes' pre-recorded expectations (from STATUS.md Boundary Issues):
  - space-management-platform: "vs Facility Management System (inventory/allocation vs building maintenance)"
  - cmms-maintenance-management: "facility-management/IWMS centers buildings-space-leases with CMMS-like maintenance modules"
  - building-management-system-bms: "vs IWMS/Facility Management (business layer vs OT control layer)"
  - commercial-property-management: "vs IWMS/Facility Management (occupier-side, no income loop)"
  - building-asset-management: "vs FMS/IWMS (suite center = real-estate/space estate)"; also flagged "conceptually an industry-scoped member of the CMMS/EAM family — joint review with CMMS/EAM leaves recommended"
  - building-energy-management: "vs FM/IWMS (energy as sibling product)"

## Research Questions

1. What are the core objects? (facilities/sites/buildings, areas/rooms, assets/equipment, work orders, requests, PM schedules, inspections, vendors/providers, costs)
2. What is the canonical work loop? (intake → triage/assign → execute → close → history)
3. Who uses it? (facility manager, maintenance technicians, requesters/occupants, contractors, finance)
4. What binds work to place? Is the estate the organizing frame or just an attribute?
5. How do in-house crews vs outsourced providers change the model?
6. What is vendor-articulated CMMS vs CAFM vs FM software vs IWMS layering?
7. What separates FMS from a CMMS deployed at a building portfolio?
8. What older/regional products satisfy the definition (historical check)?

## Representative Products

Selected for market representation, documentation depth, different product philosophies, and different customer tiers:

| Product | Pole | Customer tier / segment |
|---|---|---|
| FMX | self-labeled facilities & maintenance management; operational simplicity; suite of focused products | K-12 schools, higher ed, government, mid-market orgs (US) |
| ServiceChannel | outsourced-FM / contractor-orchestration pole for multi-location brands | retail/restaurant/grocery brands, 10 → 10,000+ locations |
| Brightly Asset Essentials | facilities-scoped CMMS / asset-management pole | schools, government, manufacturing, healthcare (Siemens-owned) |
| AkitaBox | mid-market facility operations suite (data-capture + work + inspections + capital) | facility teams, AEC/facilities-services firms, education, government |
| Planon | enterprise IWMS-suite pole with strong FM vocabulary (client side) + provider-side business solution | universities, corporates, public estate (global/EU strong) |

Boundary anchors (no full pass): a CMMS pure-play reading via the processed cmms-maintenance-management pass; space management via the processed space-management-platform pass; BMS/building-asset/energy via their processed passes.

## Sources

- FMX — https://www.gofmx.com/ (product/use-case/industry structure, case studies) and https://www.gofmx.com/facilities-management-software/ (vendor FAQ: FMS definition; CMMS vs CAFM FAQ; feature/capability detail). help.gofmx.com timed out once (2026-09-08) — not retried further per network rule; no help-center depth for FMX.
- ServiceChannel — https://servicechannel.com/ (positioning, solutions, testimonials) and https://servicechannel.com/platform/ (FAQ: vendor definition of FM software; users; capability catalog).
- Planon — https://www.planonsoftware.com/us/ (solution structure: IWMS modules, Field Services, glossary topics) and https://www.planonsoftware.com/us/glossary/facility-management-software/ (vendor-articulated FM software scope; service-provider requirements). /us/products/ 404 (my URL guess, not a domain failure).
- Brightly — https://www.brightlysoftware.com/products/asset-essentials (positioning, capabilities, FAQ).
- AkitaBox — https://home.akitabox.com/ (suite structure: Pulse/Platform/Capture/FCA/Capital/Inspections/Connect; industries).
- Processed sibling passes (STATUS.md): space-management-platform, cmms-maintenance-management, enterprise-asset-management-eam, building-management-system-bms, building-asset-management, building-energy-management, building-condition-assessment, commercial-property-management.

Evidence layers: A = direct observation on the specific product's official pages (quoted/paraphrased above); B = cross-product commonality across the sample; C = canonical inference.

---

## Product A — FMX

### Key observations

- Self-label: "facilities and maintenance management solutions"; footer: "The easiest-to-use facilities and maintenance management solution on the market." (A)
- Vendor FAQ definition of the Type: "Facilities management software (FMS) is a set of solutions designed to help organizations plan, execute, track, and report on the work needed to keep their facilities operational. The software centralizes requests, asset information, facility requests, and more, allowing facilities teams to keep things running smoothly, reduce downtime, and make data-driven decisions." (A)
- Vendor-articulated layering FAQ: "A CMMS focuses on maintenance operations, while a CAFM also helps organizations manage space and facilities… A CMMS is best for organizations focused on improving their work order and PM processes for their facilities, while a CAFM is best for organizations with broader needs like facility scheduling, utility management, space planning, and more." (A)
- Suite decomposition (products): Work Manager (work orders + PM), Event Manager (internal/external events, facility scheduling/reservations/rentals incl. invoices and payments), Warehouse Manager (parts inventory, reorders, POs), Utility Manager (utility bills centralized, anomaly detection, cross-facility benchmarking), Capital Planner (asset replacement projections, project prioritization, funding scenarios), Fleet Manager, IT Asset Manager. (A)
- Work model: maintenance requests submitted by people in the organization; work orders auto-assigned to technicians by skill set, location, workload; time- and meter-based PM tasks; inspections and routine check-ins; open work visualized on an interactive map; mobile app to manage/update/close work orders; closing a work order can require the inventory used, syncing quantity on hand. (A)
- Reports: comprehensive costs (labor, inventory, requests), operations (request trends, staffing allocation), equipment maintenance summary, inventory usage, capital forecasting, reactive vs proactive balance. (A)
- Industries: K-12, higher ed, state & local government, public works, parks & rec, manufacturing, restaurants, property management, healthcare, religious, non-profit, zoos. Case studies: school districts, restaurant groups, churches, a cultural center, a manufacturer, a linen plant. (A)
- Testimonial quote evidencing the FM span: "We needed a solution that was a good balance between a maintenance database and facilities calendaring software." (Faith Baptist Church case) (A)
- Pricing per products + users closing requests; K-12 public districts priced per student enrolled; 60-day implementation frame; no stated limits on facilities/assets/WOs. (A)

## Product B — ServiceChannel

### Key observations

- Self-label: "The leader in facilities management software and contractor sourcing… manage all maintenance activity from a single platform"; "AI-powered source of truth for managing assets and service providers" for multi-location brands. (A)
- Vendor FAQ definition: "The ServiceChannel Platform is facilities management (FM) software used for the maintenance, repair, and day-to-day operations of locations, buildings, and equipment. Our platform is sometimes referred to as a computerized maintenance management system (CMMS) or an enterprise asset management (EAM) system." (A)
- "Used by operators of multi-location businesses to manage all of their maintenance and repair work orders, invoices, service providers, projects, and assets using a single system of record." Simple enough for 10 locations, scalable to 10,000+. (A)
- User roles across the facilities ecosystem: location staff + corporate managers (create/manage work orders, site audits via the ServiceChannel App); technicians internal or external (Provider App: track work, update asset records on the job); facilities managers (streamline operations, report on performance and costs, replace assets proactively); construction/real estate teams (durability and operating cost of designs, asset condition); finance teams (financial reporting, capital planning). (A)
- Capability catalog: Provider Sourcing (marketplace of providers by quality/speed/cost), Parts Inventory and Supplies, Work Order Software ("on autopilot"), Asset Management (downtime, operating costs), Preventive Maintenance, Provider Performance (data to hold providers accountable), Managed Services (FM-as-a-service), Data Analytics and Insights, Spend Optimization, Compliance and Risk, Sustainability, Capital Planning and Projects, Program Transformation. (A)
- Provider marketplace: 70,000+ providers already on the platform; benchmarking "based on over 150 million work orders completed on the platform." (A)
- Pricing per location. (A)
- Compliance examples: refrigerant tracking for compliance (Tops Friendly Markets testimonial). (A)

## Product C — Brightly Asset Essentials

### Key observations

- Self-label: "Industry-leading CMMS for smarter asset management"; "next-generation enterprise platform generates actionable operational insights from work order and asset management activities." (A)
- FAQ: "Asset management software includes cloud-based solutions to help facility and infrastructure asset managers keep track of the assets it takes to run a building or community. These tools… are designed to manage and track all work and parts associated with repairs and replacement of vital systems needed to maintain service levels." (A)
- Capabilities: work order management, PM schedules with automated work order creation, asset register (specifications, performance metrics, documentation), parts inventory with low-stock notifications and ERP-synced POs, IoT remote monitoring → auto-generated corrective work orders, AI Maintenance Copilot (summaries, duplicate WO detection, parts recommendations), analytics for capital planning and compliance. (A)
- Audience framing: "maintenance teams, asset managers and finance leaders… mobile-friendly"; segment pages for education, government, manufacturing, healthcare, senior living, infrastructure. Sibling products: TheWorxHub (senior-living facility CMMS), Predictor (capital planning), Origin (asset health from CMMS data), Energy Manager, Event Manager, Confirm (public infrastructure). (A)
- Case framing: facility maintenance and operations ("Streamlined facility management", "track and manage facilities", city facility maintenance + budget). (A)

## Product D — AkitaBox

### Key observations

- Self-label: "Facility Asset Lifecycle Management Software"; "Extraordinary software for assessing and optimizing the operation and condition of your facilities – from boiler room to boardroom." (A)
- Suite: AkitaBox Pulse ("Complete facility optimization… asset & maintenance management, inspections, capital management, facility condition assessments, and more all in one seamless system"); AkitaBox Platform ("Asset and maintenance management plus occupant portal"); Capture (facilities data collection); FCA (facility condition assessment capture); Capital Management (asset condition and failure probability); Inspections ("inspection software for improved compliance"); Connect (Procore construction handover integration). (A)
- "Occupant portal" as a named part of the platform — occupants are a served population. (A)
- Industries: healthcare, higher ed, K-12, government, CRE, AEC & facilities services firms ("Facilities management is a universal need across industries and geographies"). (A)
- Testimonials: maintenance directors at counties/school districts; asset data collection into a shared database; anticipation of parts before job-site trips. (A)

## Product E — Planon

### Key observations

- Self-label (current): "recognized world leader in Smart Sustainable Building Management software… connect buildings, people and processes"; also "leading global provider of Real Estate and Facility Management software… one source of truth… for building owners, building users, and service providers." (A)
- IWMS solution = four named modules: Real Estate Management; Space & Workplace Services Management; Asset & Maintenance Management; Energy & Sustainability Management. Campus Management Solution = the same four for higher education. (A)
- Vendor glossary — Facility Management Software: "Facility Management (FM) software has evolved from being a system merely for registering buildings and asset data, to one that aims at increasing efficiency in the planning and execution of facility processes." Includes workflow management, extensive reporting, business analytics, web/cloud mobility, integrations (ERP, building technology, GIS, BIM, CAD). "Some organizations move toward outsourcing FM services, modern facility management software has developed to include functionality for contracting services and monitoring agreed quality, budgets, and performances." (A)
- "In addition to supporting space, maintenance and services management, the best facility management software also assists managers with… information and analytics." Cost transparency: costs per square foot per year, per workplace, dashboards, benchmarking. (A)
- Sourcing strategy: organizations outsource "cleaning, catering, security, or maintenance to professional service providers"; FM software helps determine sourcing strategy, "monitor the performance of providers," implement contracts. (A)
- Customer-service orientation: self-service access for customers, automated surveys, "integrates FM, IT, and HR services in one single software solution." (A)
- Service-provider side (same glossary page): "Commercial providers of professional facility, maintenance, or real estate services have adopted facilities management software as a part of their core business to improve the planning, delivery, and quality of services." Requirements: planning/dispatching/execution/monitoring of contracted work; mobile field execution; H&S compliance; stock and purchase management; operational controlling; standardized processes across multiple customer contracts; billing-related data (time spent, travel, materials) integrated to ERP/financial systems. Planon sells a separate "Facility Services Business Solution" (Field Services: Hard-FM Technical Services, Soft-FM Services, Energy & Sustainability Services, Space & Real Estate Services). (A)
- Customer evidence: CSULB "facilities team will improve key processes, data management… keep all stakeholders better informed with the status of the work requested on campus"; Coventry University moving "away from reactive work" by monitoring "campus plant and equipment proactively." (A)
- Glossary topics maintained: CAFM, CMMS, IWMS, EAM, FSM, "Facility Management Software", "Service Management", Space Management, Workplace Management, PPM (Planned Preventative Maintenance), Lease Accounting, Property Management Software. (A)

---

## Cross-product Comparison

| Structure | FMX | ServiceChannel | Brightly AE | AkitaBox | Planon | Layer |
|---|---|---|---|---|---|---|
| Facilities/locations of the operator as identified records | Y (facilities, map) | Y (locations first; per-location pricing) | Y ("assets it takes to run a building or community") | Y (facility/site hierarchy, floor-plan rooted) | Y (real estate portfolio) | **L0 anchor** |
| Work orders/requests as the operational unit, tracked to completion + history | Y | Y ("single system of record" for WOs/invoices) | Y | Y | Y ("planning and execution of facility processes"; "work requested on campus") | **L0** |
| Requests from the served organization (staff/occupants/location staff) with service visibility | Y (anyone in org submits; staff status updates) | Y (location staff create/manage WOs) | Y (requests; mobile teams) | Y (occupant portal) | Y (self-service; stakeholder status; surveys) | **L0** |
| Equipment/asset records bound into the estate with maintenance history | Y | Y | Y (asset register is the product's center) | Y | Y (Asset & Maintenance Mgmt module) | L1 (near-universal) |
| Planned/preventive maintenance (time/meter-based) | Y | Y | Y | Y | Y (PPM vocabulary) | L1 |
| Mobile execution for technicians | Y | Y (Provider App internal+external) | Y | Y | Y (mobile field solutions) | L1 |
| Parts/consumables inventory tied to work | Y | Y (Parts Inventory and Supplies) | Y | (suite; data capture emphasis) | Y (stock/purchase for providers) | L1 |
| Inspections / compliance checks | Y | Y (site audits, compliance & risk, refrigerant) | Y (compliance documentation) | Y (named product) | Y (H&S in provider requirements) | L1 |
| Vendor/contractor coordination + provider performance | weak (in-house-crew centric) | Y (the center) | weak | partial (services firms as customers) | Y (contracting, monitoring quality/budgets) | L1–L2 (varies by sourcing posture) |
| Cost accounting on work (labor/parts/contract spend), reporting/dashboards | Y | Y (invoices, spend optimization) | Y | Y | Y (cost per sq ft/workplace, benchmarking) | L1 |
| Facility space/resource scheduling & events | Y (Event Manager) | – | (sibling Event Manager) | – | Y (Space & Workplace Services) | L2 |
| Utility/energy bill management | Y (Utility Manager) | – | (sibling Energy Manager) | – | Y (Energy & Sustainability) | L2 |
| Capital planning / FCI / funding scenarios | Y (Capital Planner) | Y (Capital Planning and Projects) | (sibling Predictor/Origin) | Y (Capital Management + FCA) | (Real Estate module adjacency) | L2 |
| Floor plans / interactive mapping | Y | – | – | Y (floor-plan rooted) | Y (CAD/BIM/GIS integrations) | L2 |
| IoT/BMS integration, predictive | – | – | Y (IoT monitoring) | – | Y (IoT-enabled platform) | L2 |
| Provider marketplace / managed FM services | – | Y (the differentiator) | – | – | (provider-side solution sold separately) | L2 |
| Space inventory/allocation (who sits where) | – | – | – | – | Y (module) | L2 (space-management Type territory) |

Reading: the three L0 rows hold across all five poles with radically different packaging (simplified suite / contractor marketplace / facilities CMMS / data-capture-led suite / enterprise IWMS). Everything else varies by pole.

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (three jointly-held structures)

1. **The facility estate of record.** The operator's own sites/buildings/locations (with their areas and grounds) held as persistent, individually identified records. The estate is the organizing spine: work, assets, programs, and costs all bind to places in it. Remove → generic maintenance machinery (CMMS) or a generic work tracker; the software stops being *facility* management.
2. **Place-anchored facility work management.** The intake-to-completion loop for work that keeps the estate operating: incoming service/maintenance requests and planned work (preventive maintenance, inspections), triaged, prioritized, assigned to in-house crews and/or contracted providers, executed (mobile in mature products), and closed with recorded outcome — accumulating location- and asset-level work history the operation runs on. Remove → an estate registry (buildings data with no operating loop).
3. **The facilities service loop with the served organization.** The system runs the facility function as a service operation for the organization that occupies the buildings: people across the organization (staff, students, store/location teams, occupants) submit requests and receive the service with status/quality/cost visibility, and the facility operation is accountable for it. Remove → machinery-only maintenance tooling with no served population (the CMMS seam).

Jointly-held is load-bearing:
- 1 alone = property/estate registry (or spreadsheets of buildings)
- 2 without 1 = generic CMMS/ticket machinery
- 3 without 1+2 = generic internal help desk / request tracker
- 1+2 without 3 = a buildings-scoped maintenance tool (boundary gradient toward CMMS — acknowledged, see Boundary Findings)
- 2+3 without 1 = a generic org service desk with no estate

### L1 — Common Mature Structure (standard capabilities, not definitional)

- equipment/asset register bound to locations, with per-asset maintenance history and costs (present 5/5, but it is the shared CMMS substrate, not the Type's identity)
- planned preventive maintenance scheduling (time/meter-based), recurring work programs
- mobile technician execution (photos, checklists, close-out data)
- parts/MRO inventory tied to work orders; reorder thresholds; POs
- inspections and compliance checks (safety, regulatory programs — e.g., refrigerant tracking observed)
- vendor/contractor records, dispatch of work to providers, provider performance tracking (center of the outsourced pole; thin in in-house-crew poles)
- cost accounting on work (labor hours, parts, contract spend) with dashboards/reports; chargebacks/cost transparency (cost per building/sq ft/workplace)
- requester notifications/status visibility; priorities/SLA-style handling
- integrations outward: ERP/finance, directory/HR, building technology, GIS/BIM/CAD

### L2 — Variant / Optional Structure

- facility space/resource scheduling and event/rental management (community/room bookings) — a capability in some suites; deep form = space-management/booking territory
- utility/energy bill management and building-performance analytics
- capital planning: condition assessment (FCA), replacement forecasting, funding scenarios, project prioritization
- floor plans / interactive mapping as the work-location surface
- IoT/BMS/sensor integration and predictive maintenance triggers
- provider marketplaces and managed-FM service wraps (outsourced-FM pole)
- multi-location brand scale-out (location-licensed commercial pole) vs campus/estate poles
- sector shapes: K-12/higher-ed, state & local government/public works, healthcare compliance, retail/restaurant chains, CRE, religious/non-profit
- regional/label vocabulary: "CAFM" (European tradition) ≈ this Type with space emphasis; "CMMS" label used by facilities-scoped products; "IWMS" for the enterprise-suite packaging

### L3 — Vendor-specific Detail (Research Notes only)

- FMX: seven-product suite decomposition (Work/Event/Warehouse/Utility/Capital/Fleet/IT Asset managers); "Intelligent Suggestions" photo capture; per-student K-12 pricing; 60-day implementation frame; "reactive vs proactive" report as a named report.
- ServiceChannel: provider marketplace (70,000+ providers claimed), benchmarking off 150M+ work orders claim, ServiceChannel Managed (FM-as-a-service), Provider App vs client App split, per-location subscription pricing, refrigerant tracking module.
- Brightly: suite context (Asset Essentials/TheWorxHub/Predictor/Origin/Confirm/Energy Manager/Event Manager); "Maintenance Copilot" AI (summaries, duplicate-WO detection, parts recommendations); Siemens ownership; IoT→auto-WO generation.
- AkitaBox: Pulse/Platform/Capture/FCA/Capital Management/Inspections/Connect naming; Procore handover integration (construction→operations); AEC/facilities-services firm audience as first-class; data-capture-led onboarding philosophy.
- Planon: rebrand from IWMS to "Smart Sustainable Building Management"; named IWMS module set; separate Field/Facility Services Business Solution for providers (Hard-FM/Soft-FM services); SAP solution-extension partnership; self-service + survey tooling framing.

---

## Vendor-specific / Rejected Findings

- **Rejected as definitional:** provider marketplaces (single-pole), utility management (2/5 poles), space scheduling (2–3/5), capital planning (common but sold as separate specialist products), IoT/predictive (minority), floor-plan mapping (minority), managed services.
- **Rejected as definitional:** asset register as the L0 anchor — 5/5 presence, but it is the shared CMMS/EAM substrate; making it definitional would collapse FMS into CMMS/EAM and contradict the estate-anchored + served-organization observations that all five poles also share. The estate-of-service posture is what the CMMS pass already recorded as the expected seam.
- **Rejected:** "FM = outsourcing only" (ServiceChannel's philosophy is one pole; in-house crews are the dominant execution mode in the other poles).
- **Rejected:** FMS = IWMS module list. The IWMS module list is one packaging of the estate side (Planon), not the Type definition.

## Boundary Findings

- **vs CMMS / Maintenance Management (§16, processed):** the two Types share the work-order/PM/asset substrate. Seam = organizing subject + service posture: CMMS is domain-generic maintenance machinery (equipment work management as the center); FMS centers the operator's building estate and runs facilities as a service to the occupying organization (requests from the served population, facility programs, cost transparency per place). Removal tests: strip the estate/service semantics from an FMS → a CMMS remains; add estate anchoring + served-org request loop + facility-operations span to a CMMS → it operates as FM software. Consistent with the cmms pass's recorded seam ("FM/IWMS centers buildings-space-leases with CMMS-like maintenance modules"). **Joint review recommended** (the cmms pass and building-asset pass both asked for this).
- **vs Integrated Workplace Management System / IWMS (§17 sibling, unprocessed):** IWMS is the enterprise-suite packaging that integrates real estate/lease + space + maintenance + capital + sustainability as named modules of one system (Planon's own module list is the exemplar). FMS is the operational run layer — sold standalone (FMX, Brightly, AkitaBox, ServiceChannel) and present as the facilities/maintenance module inside IWMS suites. The two leaves will overlap heavily at the suite pole. **Joint review required at the IWMS pass**; proposed seam: IWMS defined by the integrated multi-domain suite (RE portfolio + space + FM + sustainability as one system of record), FMS defined by the estate-anchored operational service loop regardless of suite packaging. Note: Planon now brands away from "IWMS" ("Smart Sustainable Building Management") — naming drift to record.
- **vs Building Maintenance Management (§17 sibling, unprocessed):** expected to be the maintenance-slice sibling (building-focused work orders); FMS carries the whole facility-operations service span (requests/occupants, inspections, vendors, programs) beyond building maintenance machinery. The BMS pass already left a joint-review note for this sibling. **Flag for that pass.**
- **vs Space & Occupancy Management (§17 sibling, unprocessed) / space-management-platform (§10, processed):** space management = space inventory + allocation/occupancy state + moves/MAC; FMS = operating the estate (work loop + service posture). Space scheduling appears inside some FMS suites as a capability only. Consistent with the space pass's recorded seam ("inventory/allocation vs building maintenance").
- **vs Building Asset Management (§17, processed):** that Type centers the durable asset register + care + lifecycle economics of building equipment; FMS centers the operating service loop over the estate. AkitaBox/Brightly ship both as named modules — packaging, not Type merger. Consistent with that pass's seam.
- **vs BMS (§17, processed):** BMS = OT control of plant (sensors/actuators, automated control sequences); FMS = business/records layer coordinating human+contracted work. BMS/IoT appear in FMS as integration sources only.
- **vs Property Maintenance Management (§17 sibling, unprocessed) / Commercial Property Management (§07… actually §17, processed):** property management = income-property landlord/tenancy economics (lease-driven billing); FMS = occupier-side operations of its own estate, no income loop. The commercial-property pass recorded "vs IWMS/Facility Management (occupier-side, no income loop)" from its side.
- **vs Field Service Management (§ sibling):** provider-side dispatch business (Planon Field Services, ServiceChannel's Provider App population) is the contractor's seat; FMS is the estate owner's seat procuring and coordinating service. Planon sells both as separate products — direct packaging evidence of the seam.
- **vs Workplace Management Platform / Office Operations Platform (§10 siblings, unprocessed):** expected employee-experience/operations surfaces; FMS holds the building-operations work records. Watch at those passes.
- **vs Enterprise Request Management / help-desk family:** generic internal request fulfillment has no estate, assets, or facility semantics; the served-org request loop alone is not the Type.
- **Public-sector overlap:** FMX's public-works pole (citizens reporting street lights → dispatch) shades toward 311/citizen-request and public-works territory; recorded as sector variant + adjacent note (public-works leaf unprocessed).

## Historical / Market-Sample Check

- Paper-era facilities department: building/site files, a request log book at the front office, a maintenance work log, PM/inspection checklists in a binder, vendor invoices, keys register — satisfies all three L0 legs (estate records, place-anchored work loop to completion, served occupants submitting requests). The Type predates its software labels.
- 1990s-era "CAFM" that only registers buildings and asset data fails legs 2–3 — Planon's own glossary names this as the stage FM software "evolved from," confirming it as below the Type (registry, not management).
- On-prem 1990s–2000s facility/maintenance systems (work orders + PM + requests on a building portfolio) satisfy the core with no cloud/mobile/marketplace/AI.
- The check passes: no cloud, mobile apps, marketplaces, IoT, or AI in the core.

## Uncertainties

- No Tier-1 help-center article depth for FMX (help center timed out) — FMX work-order field-level mechanics (states, approval chains) are documented only at product-page level; no precise state lists or numeric limits asserted.
- Brightly/AkitaBox evidence is product-page level; help-center/community portals exist but were not fetched — no article-level workflow claims made for them.
- Planon's client-side operational depth (work-order states, SLA machinery) inferred from glossary + case-study level only; Planon University/docs not fetched.
- The exact boundary behavior of European "CAFM" products (space-heavy FM suites) is recorded from Planon's vocabulary and FMX's FAQ, not from a dedicated European product sample — flagged as an uncertainty for the IWMS pass.
- Provider-side FM software (Planon Field Services, FM service contractors) was observed only at product-page level; its FSM-vs-FM-service-business seam needs its own evidence if ever a dedicated leaf exists.

## Final Synthesis

A Facility Management System is the building operator's operational system of record for its own facility estate. Three jointly-held structures define it: the estate of identified places (L0-1); the place-anchored work loop that keeps the estate operating — requests and planned work through to recorded completion and history, by in-house crews and/or contracted providers (L0-2); and the service loop with the organization occupying the buildings, whose members submit requests and to whom the facility function is accountable with cost/quality visibility (L0-3). Mature products add the CMMS substrate (assets, PM, mobile, parts), inspections, vendor coordination, cost reporting; suites extend with scheduling, utilities, capital planning, floor plans, IoT. The Type holds from a school district's simplified suite to a 10,000-store brand's contractor-orchestration platform to an enterprise IWMS's facilities module. The CMMS seam (machinery without the estate/service posture) and the IWMS seam (suite packaging vs operational layer) are the two that require joint review; both flags are pre-recorded from prior passes and discharged here from this side.
