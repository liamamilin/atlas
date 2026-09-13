# Research Notes — Public Asset Management

## Research Goal

Understand Public Asset Management as an Application Type: what objects exist inside such a system, what workflows it supports, what (if anything) distinguishes it from the already-processed asset-management family (CMMS §16, EAM §16, Building Asset Management §17, Enterprise Asset Registry §10), and where its boundaries lie against neighboring government Types (Public Works Management, Government GIS, Capital Improvement Planning, Parks & Recreation Administration, 311/Citizen Service Request, Utility Asset Management).

## Initial Boundary

Working hypothesis at start: Public Asset Management is the government/public-sector member of the asset-management family — a system of record for a public agency's physical infrastructure estate (roads, bridges, sidewalks, signals, streetlights, trees, parks assets, pipes, facilities, fleet), registering assets, tracking condition, running maintenance, and planning lifecycle under public funding and accountability constraints.

Nearest neighbors flagged before research:
- EAM / CMMS (§16, both processed) — the generic family core
- Building Asset Management (§17, processed) — buildings-scoped sibling
- Enterprise Asset Registry (§10, processed) — record layer only
- Public Works Management (§24, unprocessed) — department operations
- Government GIS (§24, processed) — spatial layers vs asset lifecycle
- Capital Improvement Planning (§24, processed) — capital investment decisions
- Parks & Recreation Administration (§24, processed) — park-as-venue vs park-as-asset (forward flag to discharge)
- Utility Asset Management (§19, unprocessed) — utility-scoped sibling
- 311 / Citizen Service Request Platform (§24) — citizen intake
- Fleet Management System (§18, processed) — vehicles

## Research Questions

1. What is the central object structure? (asset register? classes? hierarchy? location?)
2. Which asset classes does the estate cover? (linear/network vs point vs facilities vs fleet)
3. What is the care loop? (inspections, condition, work orders, history)
4. What is the forward-looking loop? (condition/cost/risk → repair-vs-replace → long-term plans → funding justification)
5. What is distinctly "public"? (stewardship posture, accountability, citizen engagement, benchmarking, funding constraints)
6. How does GIS participate? (backbone vs integration vs native)
7. How do citizen requests enter? (portal → work order?)
8. Where are the boundaries vs EAM/CMMS/Public Works/GIS/CIP/Parks/311?
9. Historical check: would paper-era municipal practice satisfy the definition?

## Representative Products

Selected for market representation + documentation reach + different philosophies + different geographies/customer levels:

1. **Trimble Unity Maintain** (Trimble; the merged Cityworks + AgileAssets line) — GIS-centric public-infrastructure EAM; cities, state DOTs, utilities, airports. (cityworks.com now redirects here — market consolidation evidence.)
2. **Brightly Assetic** (Siemens Brightly) — cloud strategic asset management, AU/NZ government/infrastructure lineage; register + assessments + work + component-level accounting.
3. **Brightly Confirm** (Siemens Brightly) — UK government infrastructure (highways/councils); asset register + native GIS + contractor management + community engagement + benchmarking.
4. **AssetWorks EAM (Government & Public Works)** — US public-sector EAM pole: public works + facilities + parks + fleet; "justify every dollar" accountability framing.

Rejected/unreachable: Cartegraph (cartegraph.com 403), OpenGov (403), Tyler Technologies (403). Generic EAM (IBM Maximo/Hexagon) not fetched — the EAM boundary is carried by the processed EAM pass instead.

## Sources

All fetched 2026-09-09:

- Trimble Unity Maintain — https://www.cityworks.com/ (redirects to Trimble Unity Maintain page) and https://www.trimble.com/en/products/trimble-unity (hero + "Streamline your enterprise asset management" + Key capabilities + capabilities showcase sections)
- Brightly Assetic — https://www.brightlysoftware.com/products/assetic (product page + FAQ + case studies)
- Brightly Confirm — https://www.brightlysoftware.com/products/confirm (product page + FAQ + case studies)
- AssetWorks EAM — https://www.assetworks.com/eam/ and https://www.assetworks.com/eam/asset-management-software/
- Brightly government use case — https://www.brightlysoftware.com/use-cases/government (challenge/solution/benefits + maturity phases + registry-migration guidance + Beaufort County quote)

Internal cross-references (processed passes): STATUS.md entries for enterprise-asset-management-eam, cmms-maintenance-management, building-asset-management, enterprise-asset-registry, capital-improvement-planning, government-gis, parks-recreation-administration, fleet-management-system.

## Product Observations

### Trimble Unity Maintain (Cityworks + AgileAssets lineage) — Evidence Layer A

- Positioning: "Optimize asset management to increase efficiency and reduce costs"; "supports asset networks of all sizes, from international airports to local utilities, cities to state DOTs and healthcare to educational systems."
- Scope statement: "From inventory and work activity to performance analysis and strategic planning, Trimble Unity Maintain provides one solution to manage all the built assets in your network."
- Key benefits: "Inspect, manage, analyze and score each asset for data driven decision making"; "Use built in GIS, plus LRS support, to improve inventory and maintenance operations"; "configurable solution tailored to your organization's needs."
- Key capabilities (verbatim headers + gist):
  - Inventory management — "Know the location, condition, construction history and many other data points for each asset in your network."
  - Geolocation & spatial analysis — "Visualize the attributes and performance of your transportation network on embedded Esri ArcGIS maps, with LRS support."
  - Risk assessment — "Identify and evaluate high risk assets and make a case for maintenance or replacement."
  - Predictive analytics — "Compare what if scenarios that show the impact of various timelines, budgets, performance and other constraints on your asset management plan."
  - Work plan optimization — "Identify and select the optimal mix of work activities to achieve your objectives for funding, performance and more."
  - Data visualization & reporting — "Display and share interactive dashboards and reports that show the reasoning behind strategic decisions and the impact of infrastructure investments."
  - Work management / Work order management — office + field; "seamless field-to-office communications."
  - Inspections — "Ensure safety and compliance... connected data and automated workflows."
  - Community engagement — "Empower your citizens with a public portal for community reported issues."
- Capabilities showcase: "Fast responses — Consistently responding to citizen requests in a timely manner and providing visibility into work progress helps sustain public trust"; "Accurate insights — With visibility into maintenance records and related cost data... improve long term planning"; "Efficient work management — ...manage service requests, inspections and work orders." Screenshot described: "Asset Calculation Dashboard" with "probability of failure, consequence of failure, and business risk exposure"; service-request/work-order/inspector dashboard over a map.
- Suite context: Trimble Unity = "Plan, design, build, operate and maintain your assets—all with one solution"; "centralized, GIS-centric data and connected workflows... across the lifecycle." Unity Maintain described as "GIS-centric enterprise asset management."

### Brightly Assetic (Siemens) — Evidence Layer A

- Positioning: "cloud-based, end-to-end asset management system"; FAQ: "designed to help organizations gain a 360-degree view of maintenance, operations and physical infrastructure. This intelligent asset register serves as the central hub for all asset data. It facilitates the strategic management of assets throughout their entire lifecycle, from initial acquisition and maintenance to disposal."
- Register: "Our intelligent asset register is pre-configured for more than 100 asset classes, helping you store the right data to enable more informed decision-making and capital expenditures."
- Flexible asset structure: "powerful asset hierarchy allowing for ultimate flexibility... whether at the group, complex, component or simple level."
- Assessments module: "capture asset data, as well as photos and other attachments, with permission controls and printing capability. Easily raise work orders if issues are identified during assessments."
- Work: "out-of-the-box work management solution enables best practice maintenance processes — reactive, proactive and strategic"; work requests; "Drag and drop maintenance events to coordinate crews, contractors and resources in one view."
- Dashboards per module; Mobility module (field version of Assets/Maintenance/Assessments).
- Accounting module: "granular asset accounting at the component level. Apply depreciation patterns to individual asset components. The system automatically calculates written-down value, accumulated depreciation, remaining asset life and other key measures."
- FAQ audience: "beneficial for public sector organizations, utilities, infrastructure providers and any enterprise managing a significant portfolio of physical assets. These organizations often require robust tools for long-term planning, regulatory compliance and optimizing large-scale asset investments. It helps achieve greater transparency, accountability and cost-effectiveness."
- Integration: "seamless integration with existing enterprise systems. This includes platforms like Geographic Information Systems (GIS) and financial management software."
- Case studies (all government): City of Victor Harbor SA ("accurately map its assets... improve compliance and reporting"), Tasmanian DECYP ("improve its asset register... perform lifecycle scenario analysis"), Gunnedah Shire Council NSW ("centralize data, enhance regulatory reporting").
- Government/Infrastructure/Education tabs; infrastructure gist: "helps rail, ports, roads and utilities teams assess, maintain and plan across their asset portfolios — reducing risk, managing backlogs."

### Brightly Confirm (Siemens) — Evidence Layer A

- Positioning: "Asset management software for government infrastructure"; "The smart, cost-effective way to manage your public infrastructure assets."
- Why: "Accelerate response times, improve service levels and drive citizen engagement and satisfaction with how your city's assets are managed"; "Save on expensive GIS licensing costs — Power your in-field work scheduling and allocation with Siemens' native GIS capabilities that integrate with other GIS programs"; "Manage a complex network of assets — Build one centralized asset register that provides detailed data and actionable insights based on asset category, class and type level"; "Shift to risk-based preventive maintenance — Monitor and maintain thousands of physical and operational assets by compiling labor costs and repair histories into a comprehensive asset register."
- Featured capabilities:
  - Flexible asset register — "drill down through category, class and type for any asset... unlimited attributes and customizable fields... ideal for managing a network of complex linear assets."
  - Native GIS capabilities — powers work scheduling/allocation; integrates with other GIS programs.
  - Contractor management — "brings every operational and maintenance contractor into one system. Schedulers get a single view of active work."
  - Community engagement — "Residents submit and track requests through a centralized portal, and maintenance teams respond directly — keeping people informed as work moves from scheduled to in-progress to complete."
  - Data and insights — "interactive reports and predefined and customizable dashboards that include KPIs, GIS dashboards and data visualization tools. Confirm also offers benchmarking reports so that teams can compare their city's performance against other communities."
- FAQ (vendor's own Type definition): "Asset management software for infrastructure (like Confirm) combines a centralized asset register, GIS mapping and data and insights for confident decision-making."
- FAQ problem framing: "Cities are facing an aging infrastructure crisis — buildings, roads, bridges and parks all competing for limited repair budgets... Asset management software turns those decisions from guesswork into evidence. By centralizing asset condition, cost and risk data in one system, it helps public works teams prioritize the work that protects safety and service most — and justify those choices to the people funding them."
- FAQ checklist: asset register for complex assets/attributes; GIS capabilities and integration; spatial analysis and mobile access for on-site data collection; community engagement tools; data and analytics "to support confident decision-making, optimize maintenance and facilitate strategic planning."
- "Confirm also works alongside investment planning tools to help elevate and modernize capital plans."
- Case studies: City of Edinburgh Council, Lincolnshire County Council ("Head of Highways Asset Management"), Kent County Council ("Highways Systems Manager", safety-barrier data consolidation).

### AssetWorks EAM (Government & Public Works) — Evidence Layer A

- Positioning: "Built for Public Sector Operations. One Platform. Two Powerful Solutions. Every Asset Covered. From government fleets to public works infrastructure, AssetWorks gives your team the tools to manage every asset, track every cost, and justify every dollar."
- "AssetWorks EAM helps public works, facilities, and parks teams manage all asset types in one system — with GIS integration, mobile field access, capital planning, and the reporting tools you need to make data-backed decisions."
- Fleet sibling: "FleetFocus gives government fleet teams a complete view of every vehicle — maintenance history, fuel usage, EV charging, GPS data, and cost reporting — all in one connected system built for public sector accountability." (Fleet is a separate product line — family-split evidence.)
- Audience: "From city fleet garages to county park systems... government fleet, public works, facilities management, parks and recreation, and utilities."
- Case studies: New Hampshire DOT ("modernized infrastructure and equipment management... unified platform built for large-scale public asset operations"); Ramsey County Parks & Recreation ("tracking assets, scheduling maintenance... across a sprawling outdoor environment"); LA County ISD (fleet).
- Asset management product page:
  - "Manage and maintain all your assets—big, small, and everything in between. Every asset in your community has a purpose."
  - PM/inspections: "Your assets require unique preventive maintenance and inspection schedules... AssetWorks EAM automates PM and inspections."
  - Mapping: "All necessary information, including work orders, service requests, and projects, is displayed spatially, which significantly reduces the number of clicks and screens required to complete day-to-day work."
  - Lifecycle: "full lifecycle costing and management for all assets, including lifecycle status, preventive maintenance and inspections, labor costs, equipment usage, vendor/contractor work, and much more."
  - Asset templates: "standardizing traits, including lifecycle management, safety and procedural information, assigned staff/crews, and required parts, materials, tools, and equipment."
  - Mobile: "complete work orders, update asset information, manage service requests... online and offline environments."
  - Capital Planning: "track major goals and objectives, streamline project approvals, and see real-time spend VS budget and funding sources."
- FAQ: "EAM software is a comprehensive web-based solution created to manage all your business assets... manages the maintenance of all your assets in one system... even in offline environments"; "modernizes mapping operations as an Esri partner, offering near real-time synchronization of GIS data."

### Brightly government use-case page (cross-product framing) — Evidence Layer A

- Challenge: "Governments manage thousands of public assets across communities, but limited funding, aging infrastructure and growing public expectations make it difficult to prioritize spending and justify capital and operating decisions."
- Solution: "real-time, consolidated asset data to support capital planning, streamline maintenance, optimize energy usage and guide long-term investments."
- Maturity journey: Foundational phase (GIS, mobile work orders, "support for any asset class") → Insightful phase ("Add preventive maintenance, model funding scenarios, predict asset deterioration and prioritize capital projects, so your most critical assets rise to the top for funding") → Smart phase (IoT sensors, asset health + sustainability).
- Implementation guidance: "Building an accurate, high-quality asset registry is essential. Consolidate existing asset records, condition data and maintenance history before configuration to support reliable reporting and capital planning decisions."
- Beaufort County, SC quote: "We wanted [Siemens'] asset management system so that we could have the data to show that we needed more money, which proved that we needed more staff." — asset data as the instrument of budget justification.

## Cross-product Comparison

| Structure | Unity Maintain | Assetic | Confirm | AssetWorks EAM | Reading |
|---|---|---|---|---|---|
| Central asset register over a mixed public estate | ✔ "all the built assets in your network" | ✔ "intelligent asset register... 100+ asset classes" | ✔ "one centralized asset register... category, class and type" | ✔ "manage all asset types in one system" | Universal → family core |
| Asset classes span civil infrastructure + facilities + fleet/parks | ✔ cities/DOTs/utilities/airports | ✔ gov/infrastructure (rail, ports, roads) | ✔ "buildings, roads, bridges and parks"; linear assets | ✔ public works/facilities/parks/fleet | Universal → domain signature |
| Asset hierarchy/classification (category/class/type; group/component) | ✔ inventory per asset | ✔ group/complex/component/simple | ✔ category/class/type drill-down | ✔ asset templates | Universal realization |
| Location as structural dimension (GIS) | ✔ built-in GIS + LRS, embedded Esri | ✔ GIS integration | ✔ native GIS + integration | ✔ Esri partner, spatial display of WOs/SRs/projects | Universal; realization varies (native/embedded/integrated) → conceptual layer = located asset population |
| Condition capture / inspections | ✔ inspect/score; inspections capability | ✔ Assessments module → raise WOs | ✔ condition data central; risk-based PM | ✔ automated PM and inspections | Universal |
| Work management bound to assets (WOs, requests, scheduling) | ✔ WOs + service requests | ✔ work requests, drag-drop scheduling | ✔ scheduling/allocation, contractors | ✔ WOs, service requests, mobile crews | Universal → contains CMMS core |
| Persistent per-asset history (costs, repairs) | ✔ maintenance records + cost data | ✔ repair histories | ✔ labor costs and repair histories compiled | ✔ lifecycle costing, labor costs, vendor work | Universal |
| Lifecycle outlook: condition/age/cost/risk → repair-vs-replace | ✔ risk assessment "make a case for maintenance or replacement" | ✔ lifecycle scenario analysis; remaining asset life | ✔ risk-based preventive maintenance; "where preventive maintenance will pay off" | ✔ lifecycle status; full lifecycle costing | Universal |
| Long-term planning under funding constraints | ✔ what-if scenarios (timelines/budgets/performance); work plan optimization for funding objectives | ✔ model funding scenarios (Brightly gov page) | ✔ justify capital plans; works alongside investment planning tools | ✔ capital planning: spend vs budget and funding sources | Universal in public context |
| Accountability/justification to funders | ✔ reports "show the reasoning behind strategic decisions and the impact of infrastructure investments" | ✔ "transparency, accountability"; regulatory reporting | ✔ "justify those choices to the people funding them" | ✔ "justify every dollar"; "built for public sector accountability" | Universal → the "public" signature |
| Citizen request intake → work | ✔ public portal for community reported issues | ✖ not confirmed (work requests module; audience unclear) | ✔ residents submit and track requests | ✔ service requests (facilities/public) | 3/4 → common, not definitional |
| Benchmarking across communities | ✖ | ✖ | ✔ | ✖ | Product-specific |
| Component-level depreciation accounting | ✖ not observed | ✔ Accounting module | ✖ | ✖ (ERP-finance handoff implied) | Product-specific |
| LRS / linear-asset machinery | ✔ LRS support | ✖ not observed | ✔ "complex linear assets" | ✖ not observed | Domain-common, not definitional |
| Risk scoring (PoF × CoF) | ✔ dashboard | ✔ "reducing risk" (gist) | ✔ risk-based | ✔ asset performance assessment | Common |
| IoT/predictive sensors | ✖ not on fetched page | (Brightly smart phase) | ✖ | ✖ | Variant (maturity-phase) |
| Fleet as included class vs sibling product | unclear | unclear | unclear | sibling product (FleetFocus) | Variant |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Public Asset Management is the public-infrastructure-scoped member of the asset-management family. Its defining core is three jointly-held structures, held by a public-steward operator over a public-infrastructure estate:

1. **The public asset register of record** — one durable identified record per physical asset in the agency's estate, classified by category/class/type, carrying attributes, location, condition and accumulated history. The estate is the mixed civil-infrastructure population a public agency stewards in public space: roads/bridges/sidewalks, signals/lighting/signs, trees, parks and grounds assets, storm/waste lines, public buildings/facilities, and commonly fleet. Remove → generic work tracking / cost tracking with no asset backbone.
2. **Recorded care attached to each asset** — inspections/condition capture and maintenance work (requests → work orders → completion) bound to asset records and closed into persistent per-asset history. Remove → bare registry (Enterprise Asset Registry territory).
3. **Lifecycle outlook feeding stewardship decisions** — condition/age/cost/risk rolled up per asset and across the estate into repair-vs-replace judgment and multi-year maintenance/capital plans under constrained (public) funding, producing the evidence used to justify spending to funders. Remove → maintenance log with no forward view; the "management" collapses.

**Public-stewardship frame (part of Type identity, per the parks-recreation precedent):** the operator is a public agency holding the estate in trust for public service; the system's records exist to make stewardship defensible — evidence for budgets and capital programs, demonstrated service levels, and (commonly) citizen-facing responsiveness. Remove the public frame → generic EAM serving infrastructure owners.

Jointly-held load-bearing tests:
- 1 alone = asset registry / fixed-asset list
- 2 without 1 = free-floating work orders (CMMS without backbone)
- 3 without 1+2 = planning spreadsheet over nothing
- 1+2 without 3 = maintenance history archive, no forward planning
- 1+3 without 2 = condition survey + plan with no executed care
- all three without the public frame = EAM applied to infrastructure

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Work-order engine: reactive + preventive/planned maintenance, schedules, assignment, completion with labor/parts/contractor costs
- Inspection programs with schedules and checklists; condition scoring
- Service/citizen request intake converting to asset-bound work (3/4 observed)
- Mobile field execution (online/offline), photos, location-aware
- Contractor management (single view of contracted work)
- Per-asset cost rollup (labor, parts, vendor)
- GIS mapping/spatial display of assets, work, requests; GIS integration patterns vary
- Dashboards/KPIs/reports; risk scoring (probability × consequence of failure)
- Capital/renewal planning views: spend vs budget, funding sources, project approvals
- Asset templates/classes; configurable hierarchies and attributes

### L2 — Variant / Optional Structure

- GIS posture: GIS-centric platform (embedded Esri, LRS) vs native GIS vs integration/synchronization vs GIS-as-external-system
- Strategic depth: operational work management first vs strategic/financial asset management first (condition modeling, deterioration prediction, funding scenarios, component-level depreciation)
- Regional vocabulary and regime: US public works/DOT; UK highways/councils (street works); AU/NZ council asset management with long-term financial plans and regulatory reporting
- Asset-class breadth: whole-of-agency mixed estate vs department-scoped deployments (parks, facilities, fleet)
- Citizen engagement depth: public portal with request tracking vs internal-only requests
- Benchmarking across communities (product-specific in sample)
- IoT/predictive monitoring overlays; energy/sustainability overlays
- Maturity-model packaging (foundational → insightful → smart)
- Fleet as included asset class vs sibling product line
- Suite module vs standalone; cloud vs hosted

### L3 — Vendor-specific (Research Notes only)

- Assetic: "100+ asset classes pre-configured"; module names (Assets, Assessments, Mobility, Accounting); AU council case studies (Victor Harbor, Tasmanian DECYP, Gunnedah)
- Confirm: native-GIS licensing-cost pitch; pothole-inquiry product tour; UK council case studies (Edinburgh, Lincolnshire, Kent); benchmarking reports
- Trimble Unity Maintain: Cityworks + AgileAssets merger branding; embedded Esri ArcGIS + LRS; "Asset Calculation Dashboard" (PoF/CoF/business risk exposure); capabilities showcase
- AssetWorks: FleetFocus/FuelFocus/Connect app product names; "40 years", customer-count marketing stats; Esri partner "near real-time synchronization"
- Brightly: "12,000 clients" vs "11,000+ organizations" (inconsistent marketing figures — not used); maturity-phase packaging; Beaufort County quote

## Vendor-specific Findings

See L3 above. None of these enter the canonical core.

## Boundary Findings

1. **vs Enterprise Asset Management (§16, processed)** — same family core (register + work management + whole-life governance). PAM = the family core held over the public-infrastructure estate under the public-stewardship frame (funding justification to external funders, service levels, citizen responsiveness). Removal tests: strip the public frame → EAM serving an infrastructure owner; strip the register/care/lifecycle → a transparency/reporting shell. The EAM pass itself recorded "domain cousins (fleet/aircraft/utility/building asset systems ride inside as asset classes or keep their own spines)" — PAM is the public-infrastructure spine.
2. **vs CMMS (§16, processed)** — PAM contains the CMMS core (register + work orders + history) but adds the estate breadth, lifecycle outlook and stewardship frame. Strip lifecycle/stewardship → CMMS.
3. **vs Enterprise Asset Registry (§10, processed)** — registry = durable per-item record layer only. Strip care + lifecycle → registry.
4. **vs Public Works Management (§24, unprocessed)** — forward flag: the seam should be asset-estate lifecycle (this Type) vs department operations (crews, facilities, service delivery of the public-works department). Sampled products position asset management as one system used by public-works teams (Confirm: "maintenance and public works teams"; AssetWorks public-works line), suggesting PAM is the asset spine inside public-works operations. To be ratified from the public-works side when processed.
5. **vs Government GIS (§24, processed)** — adopted from that pass: GIS maintains georeferenced layers; PAM centers asset records and their care lifecycle. GIS integration is standard (universal in sample) but the realization varies (embedded/native/integrated), so GIS is not definitional; location of assets is part of the register's character, not a GIS engine.
6. **vs Capital Improvement Planning (§24, processed)** — adopted from that pass: CIP decides which new/renewal investments to fund in which years; PAM holds condition/maintenance of existing assets and its condition/cost data feeds capital needs. AssetWorks' capital-planning module is asset-renewal-scoped (spend vs budget, funding sources), not the jurisdiction-wide capital budget process.
7. **vs Parks & Recreation Administration (§24, processed)** — DISCHARGES the forward flag from that pass: park-as-venue (bookable inventory) vs park-as-asset (maintained estate) confirmed. Parks departments appear as PAM tenants in their asset-operator role (AssetWorks parks & rec line; Ramsey County Parks case study), but venue booking/program enrollment machinery belongs to the other Type; this pass does not assume parks departments as default tenants.
8. **vs Utility Asset Management (§19, unprocessed)** — forward flag: utilities hold networked assets and share the family core; the utility sibling should center the utility network estate and utility operations, while PAM centers the agency's mixed civil estate. To be ratified from the utility side.
9. **vs Building Asset Management (§17, processed)** — buildings-scoped sibling centers building equipment systems in site→building→floor locations; PAM's estate is dominated by civil/linear/network infrastructure, with facilities as one asset class among many.
10. **vs 311 / Citizen Service Request Platform (§24)** — citizen requests are an intake channel into PAM work management (portal → asset-bound work order); the 311 Type centers the citizen request case, not the asset estate.
11. **vs Fleet Management System (§18, processed)** — vehicles appear as one asset class inside PAM; dedicated fleet operations (telematics, driver oversight, fuel) are the FMS Type. AssetWorks even splits fleet into a sibling product line — family-split evidence.
12. **vs Building Condition Assessment (§17, processed)** — condition assessment is the survey deliverable; PAM is the living system of record that consumes condition data and acts on it.
13. **Asset investment planning** — the EAM pass flagged AIP as an emerging separately packaged pillar. From this side, long-term financial planning (funding scenarios, deterioration prediction, work-plan optimization) reads as a deepening of the lifecycle-outlook leg, not a separate Type; no directory change proposed.

## Historical / Market-Sample Check (§24)

Paper-era municipal practice: the city engineer's registry — ledger/card file of streets, bridges, culverts, signs, trees with location and condition notes; maintenance logs and work tickets; annual budget submissions to council justifying repair and replacement. This satisfies all three legs (register + recorded care + lifecycle outlook feeding funding justification) with no software, no GIS, no citizen portal, no ISO vocabulary. Pre-software DOT pavement condition surveys driving resurfacing programs fit the same shape. Regional regimes (UK council highways, AU council long-term plans, US city/DOT) all fit without each other's vocabulary. **Historical check passed.**

Anti-overfit checks:
- GIS is universal in the sample but realization varies (embedded Esri / native / integration); paper-era practice has no GIS → the invariant is the located asset population, not GIS machinery.
- Citizen portals are 3/4 → common, not definitional.
- LRS/linear-asset machinery is 2/4 → domain-common, not definitional.
- Component-level depreciation is 1/4 → product-specific.
- Benchmarking is 1/4 → product-specific.
- "100+ asset classes" is vendor marketing → not used.

## Uncertainties

- No Tier-1 help-center depth for any sampled product (all evidence is official product/marketing/use-case pages; help portals not fetched). Assertion strength reduced accordingly; no numeric limits, state names, or default values asserted in the final document.
- Cartegraph, OpenGov, Tyler Technologies unreachable (403 ×1 each) — the US pure-play local-government pole is evidenced indirectly via the sampled products' government positioning and case studies.
- Whether Assetic's work-request module accepts citizen-facing requests (not confirmed) — citizen intake held at 3/4.
- Whether Unity Maintain / Assetic include fleet as an internal class or hand off to sibling products (only AssetWorks' split directly observed).
- ISO 55000 alignment is market vocabulary (AU-flavored) but was not directly evidenced in fetched pages; the final document says "standards-flavored strategic asset management" only via the observed "regulatory compliance / long-term planning" framing.
- Exact condition-scoring scales, risk formulas, and planning horizons vary and were not researched to precision — deliberately not stated.

## Final Synthesis

Public Asset Management is the public-infrastructure-scoped member of the asset-management family: the public agency's system of record for the physical estate it stewards. Its defining core is the family core — asset register + recorded care + lifecycle outlook — held over a mixed civil-infrastructure estate by a public-steward operator, with the lifecycle outlook terminating in defensible stewardship: evidence for budgets and capital programs, demonstrated service levels, and citizen-facing responsiveness. Everything else commonly seen — GIS machinery, citizen portals, benchmarking, IoT, component accounting, regional vocabularies — is standard, variant, or vendor-specific structure, documented as such.
