# Research Notes — Utility Asset Management

## Research Goal

Understand what "Utility Asset Management" is as an Application Type: what system of record a utility operator (electric T&D, gas, water/wastewater) runs for its physical network plant, what objects live inside it, what work flows through it, and where its boundary lies against the already-processed asset-management family (EAM, CMMS, Enterprise Asset Registry, Public Asset Management, Building Asset Management) and against the utility siblings (Utility GIS, OMS, Utility FSM, generation-side asset Types).

Context inherited from prior passes:

- **EAM (§16, 2026-09-08)**: defining core = enterprise asset register + maintenance work management + whole-life asset governance. Domain cousins (fleet/aircraft/utility/building) "ride inside as asset classes or keep their own spines" — this pass must decide which is true for utilities.
- **Public Asset Management (§24, 2026-09-09)**: left a forward flag — "utility-asset-management (seam = utility network estate + utility operations vs the agency's mixed civil estate)". This pass must ratify or reject that seam.
- **OMS (§19, 2026-09-09)**: held seams vs Utility GIS (model source) and Utility FSM (shared dispatch machinery; unplanned predicted events vs scheduled work orders) — forward notes for those passes; this pass sits upstream of both.
- **Power Plant Management / Renewable Energy Asset Management (§19)**: generation-side asset management Types; this pass must hold the generation-vs-network seam.

## Initial Boundary

Working hypothesis before research:

1. Core use: the utility's system of record for the physical plant of its delivery network (poles, conductors, transformers, substations, mains, valves, meters), across the whole asset life.
2. Primary users: utility asset/maintenance organizations — planners, field crews, inspectors, asset managers, capital planners.
3. Nearest Types: EAM/CMMS (same family), Utility GIS (network model), OMS (outage events on the network), Utility FSM (field work execution), Public Asset Management (mixed civil estate), generation-side asset Types.
4. Likely boundary: the estate (a connected service-delivery network) and the operator context (continuous service, regulatory obligations, capital recovered through rates) — not any single feature.
5. Unknowns: whether network connectivity is held inside the asset system or only in GIS; whether construction work (network expansion) is part of the Type; whether rate-base/capitalization accounting is definitional; whether a distinct product category exists at all vs "EAM sold to utilities".

## Research Questions

1. What asset populations does the system hold? (taxonomy: poles, conductors, transformers, mains, valves, meters…)
2. How is the estate structured — location hierarchy, network connectivity, GIS?
3. What work does the system manage — maintenance only, or also inspections, vegetation, construction/new services?
4. What lifecycle/governance exists — condition, risk, repair-vs-replace, capital planning, regulatory compliance?
5. How does asset cost interact with utility accounting (capitalization, fixed-asset interface, rate recovery)?
6. How does the system relate to the utility's operational estate (GIS, OMS, SCADA, AMI, CIS)?
7. What is utility-specific vs generic EAM machinery?
8. Do older/regional/smaller-utility implementations still fit the definition (historical check)?

## Representative Products

Selected for market representation, documentation quality, different product philosophies, and different customer tiers:

| Product | Pole | Why sampled |
|---|---|---|
| Oracle Utilities Work and Asset Management (WAM / Work and Asset Cloud Service) | utility-specific suite (Tier 1 docs) | the flagship product literally named for this category; electric, gas, and water utilities; deep official user guides reachable |
| Trimble Unity (Unity Maintain, ex-Cityworks + AgileAssets) | GIS-centric ALM suite straddling utilities and local government | tests the public-asset seam from the vendor side; embedded Esri GIS + LRS |
| SAP (Utilities industry + EAM/Asset Management) | ERP-embedded pole | asset management as an ERP capability with a utilities industry layer |
| IFS (Energy, Utilities & Resources; EAM + Asset Investment Planning) | standalone EAM with utilities vertical + capital-planning pillar | mid/large utility tier; shows capital planning packaged separately |
| IBM Maximo Application Suite | heritage EAM platform baseline | the generic-EAM reference point the utility products differentiate from |

Rejected/abandoned: Clevest (domain acquired; clevest.com now serves IFS content), Hexagon EAM (403), Autodesk/Innovyze Info360 Asset (403/404 — water-network-specialist pole unreachable), Bentley AssetWise (404), IBM utilities industry page (404).

## Sources

Research date: 2026-09-10. All fetched live.

- Oracle Utilities Work and Asset Management product page — https://www.oracle.com/utilities/work-asset-management/ (fetched OK)
- Oracle Utilities documentation hub — https://docs.oracle.com/en/industries/energy-water/ (fetched OK)
- Oracle WAM Get Started — https://docs.oracle.com/en/industries/energy-water/work-asset-management/ (fetched OK)
- Oracle WAM Business User Guide (TOC) — .../254/wam-user-guides/Topics/W1_UserGuide_container.html (fetched OK)
- Oracle WAM About WAM — .../W1_BG_About_Work_And_Asset_Management.html (fetched OK)
- Oracle WAM About Assets — .../W1_BG_About_Assets.html (fetched OK)
- Oracle WAM About Asset Locations — .../W1_BG_About_Asset_Locations.html (fetched OK)
- Oracle WAM About Operational Devices — .../W1_BG_About_Operational_Devices.html (fetched OK)
- Oracle WAM About Work Management — .../W1_BG_About_Work_Management.html (fetched OK)
- Oracle WAM About Construction Work — .../W1_BG_About_Construction_Work.html (fetched OK)
- Oracle WAM brochure PDF — binary garbage, unusable (noted as limitation)
- Trimble Unity suite page — https://www.trimble.com/en/products/trimble-unity (fetched OK)
- Trimble Unity Maintain page — https://www.trimble.com/en/products/trimble-unity-maintain (fetched OK)
- SAP Utilities industry page — https://www.sap.com/industries/utilities.html (fetched OK)
- IFS Energy, Utilities and Resources page — https://www.ifs.com/en/industries/energy-utilities-and-resources (fetched OK)
- IBM Maximo asset management page — https://www.ibm.com/products/maximo/asset-management (fetched OK)

## Product Observations

### Oracle Utilities Work and Asset Management (evidence layer A — official user guides, directly observed)

- Docs-hub positioning (verbatim): "Oracle Utilities Work and Asset Management provides functionality to handle large volumes of assets and to manage the receipt, installation, maintenance, tracking, and removal of those assets. The system also manages approval processing, tracks purchasing transactions, manages inventory and resources, and tracks costs, accounting, and financial transactions."
- Product page positioning: "supports the full asset lifecycle… Increase maintenance efficiencies, predict and prevent problems, extend asset life… Simplify investment planning and reduce the cost of aging infrastructure… Built-in Asset Performance Management provides real-time visibility into your assets' condition and uses AI for predictive maintenance planning." Customer quote from **Louisville Water** (a water utility): "forecast asset cost, perform predictive maintenance before failure incidents, and ultimately extend the life of our assets."
- **Asset model** (About Assets, verbatim): "An asset describes such objects as **meters, poles, pipes, transformers**, components, or any other material item owned or managed by an organization." Key aspects: monetary or functional value; able to be inspected; able to be serviced and maintained; disposition history; components; unique asset identifier (Asset Number + Badge Number). "Assets are always associated with a location… typically exist within a structured hierarchy based on the relationship between the asset and its locations and organizations."
- **Fixed assets / capital structure** (About Assets): fixed (capital) assets "initially capitalized but then depreciate over time"; depreciation "currently not managed within WAM" but interfaced "to an external fixed asset management system"; fixed-asset information obtained "during the receipt and accept process or through the construction work activity process"; **Property Units** = "Groupings of fixed assets"; **Member Assets** = "fixed assets that are not individually depreciated such as **poles, conductors, or pipes**"; ERP project/task numbers carried for project integration. This is the utility rate-base capitalization structure in vendor terms.
- **Linear assets / connectivity** (About Assets): "Setting up your assets so that they are recognized as a 'system'… If your organization uses GIS, this functionality can also help to position your assets on the mapping system… Linear assets include a '**Connected to**' field which allows you to define the connections between assets. For example, a pipe system would consist of a pipe, connected to a manhole, connected to the next pipe, and so on."
- **Asset locations** (About Asset Locations): "the physical location where the asset is *installed* after it leaves the storage location. Some examples of asset locations are **service points, underground connections, poles**." Locations have their own history and lifecycle, organized in a reporting hierarchy; **Service Area** is a location type.
- **Operational devices** (About Operational Devices): "any asset that is used in a **metering system**… physical objects, such as smart meters, communication components, or communication relays, or… virtual objects, such as firmware." With Measurements and Device Configuration sub-topics; separate **Operational Device Management** product/deployment mode exists (customers can run ODM without WAM).
- **Work model** (About Work Management): work performed by crews in the field through **activities** — "a task used to track changes and other actions performed in the field, such as **inspections, changes to assets, or even tree trimming**". Three activity classes sharing one Activity Type structure: **Field Activity** (no planning/cost), **Work Activity** (planning + cost), **Construction Work Activity** (planning + cost). Common details: unique ID, **Work Location** (addresses, intersections, lat/long), Schedule Details, Attachments, **Completion Events** ("execute the business processes resulting from the activity, such as asset updates, status transitions").
- Work-management surface also includes: Work Orders, Template Work Orders, Work Requests, Work Planning, **Permits**, Communication Logs, **Service Calls**, Projects, Activity Generators, Work Planning Dashboard.
- **Construction work** (About Construction Work): "such types of work as **pole extensions, excavations, subdivisions**… require planning and coordination between many different internal and external departments." Sub-structure: Work Designs, Design Elements, Construction Work Costs, Approving Construction Work, Construction Work Orders/Activities, Template CWOs, Construction Work Locations, Scheduling, **Activity Reconciliation**. Overview (verbatim): "Construction work management refers to… construction type work, such as new facilities, requests for new services or additions, and designing and estimating **line extensions**. Construction work uses **compatible units** to identify the resources necessary to install or remove assets associated with a work site."
- Other functional areas (About WAM): Home Page dashboards; Approvals (approval profiles, Approval Dashboard); Financial Transactions (purchasing/procurement costs, inventory/stocking costs, labor/equipment/materials costs of work); Inventory (stock allocated to work); Preventive Maintenance ("maintenance schedules and triggers identify the type of asset needing maintenance and triggers tell the system when the asset is due"); Purchasing (requisition to invoicing, vendors, stock items); Resource Management (crews and crew shifts, employees, equipment); Asset 360 Portal; GIS Map Viewer; 360 Degree Search; Digital Asset Management / Digital Asset Cloud Service (condition-monitoring companion).
- Integrations documented: to Oracle Fusion Assets (fixed assets), ERP connector, Oracle Field Service, Primavera.
- Oracle ships **Capital Asset Lifecycle Management** as a *separate* Utilities product line item (capital planning/investment pole) — deep capital planning is packaged outside WAM.

### Trimble Unity / Unity Maintain (evidence layer A for product claims; B for family generalization)

- Suite positioning: "The Trimble Unity asset lifecycle management solution provides centralized, **GIS-centric** data and connected workflows… **Plan, design, build, operate and maintain** your assets—all with one solution." Suite members: Unity Construct (capital program management / digital project delivery), **Unity Maintain ("GIS-centric enterprise asset management")**, Unity Permit, Unity Field ("Locate utility assets and streamline operations"), Trimble Connect.
- Unity Maintain: "supports **asset networks of all sizes, from international airports to local utilities, cities to state DOTs** and healthcare to educational systems." "From inventory and work activity to performance analysis and strategic planning… manage all the **built assets in your network**."
- Key capabilities: Inventory management ("location, condition, construction history and many other data points for each asset in your network"); Geolocation & spatial analysis ("embedded **Esri ArcGIS** maps, with **LRS** support"); Risk assessment ("Identify and evaluate high risk assets and make a case for maintenance or replacement"); Predictive analytics ("what if scenarios… impact of various timelines, budgets, performance… on your asset management plan"); Work plan optimization ("optimal mix of work activities to achieve your objectives for funding, performance"); Data visualization & reporting ("show the reasoning behind strategic decisions and the impact of infrastructure investments"); Work management; Work order management; Inspections ("Ensure safety and compliance"); Community engagement (public portal).
- Risk dashboards shown: "probability of failure, consequence of failure, and business risk exposure."
- Interpretation: the same platform sells to utilities and public agencies; the utility-specific content is the network estate (utility asset location, Unity Field "locate utility assets"). Strong evidence that the asset-management family core is shared and the estate is the differentiator.

### SAP (evidence layer B — industry page; ERP-embedded pole)

- Utilities industry page: "utilities industry includes electric, gas, water, and environmental services" (FAQ). Asset content: "Digitalize and optimize operations — Increase asset availability, and measure and improve asset performance by allowing asset owners, plant managers, and reliability engineers to optimize maintenance strategies"; "Maintain asset health, optimize performance, and reduce risk — Balancing asset performance decisions based on cost and risk profile… Planning, scheduling, and executing maintenance and service operations"; links to SAP Intelligent Asset Management / EAM, SAP APM, Field Service Management. "Autonomous Asset Management — Increase asset reliability and uptime while ensuring regulatory compliance, safety, and sustainability."
- Interpretation: SAP's utility asset management = the ERP's EAM capability + utilities industry context; no separate utility-asset product; the domain spine rides the ERP module.

### IFS (evidence layer B — standalone EAM with utilities vertical)

- Industry page: "a unified, composable solution that connects asset management, field service, and project management." Segments: Mills and Mining, Oil and Gas, Power Generation, **Transmission and Distribution** ("manage their assets, field service operations, and customer engagement"), **Water and Wastewater**, **Utility Operations** ("covering asset management, field service management, and enterprise resource planning").
- **Asset Investment Planning** product: "enables utility companies to make informed decisions about asset investments, prioritize maintenance, and optimize resource allocation. This leads to improved asset resilience and maximized capital efficiency." — capital planning packaged as a separate pillar (matches the EAM pass's flag and Oracle's separate CALM product).
- FAQ: "Energy asset management focuses on optimizing the performance, maintenance, and lifecycle of energy infrastructure. It supports **reliability, compliance**, and sustainability goals."

### IBM Maximo (evidence layer B — generic EAM baseline)

- "end-to-end management of assets, from procurement and maintenance to decommissioning"; work order management, mobile EAM, MRO inventory, dashboards; "Improve compliance and risk management — Ensure compliance with industry regulations and standards with tools to track and report on compliance." Add-ons include "spatial asset visualization, linear asset manager" — the machinery utilities need exists as add-ons to the generic platform.
- Interpretation: Maximo is the generic-EAM pole; utility deployments configure it (industry solutions exist but were not reachable in this pass — noted as limitation).

## Cross-product Comparison

| Dimension | Oracle WAM | Trimble Unity Maintain | SAP | IFS | IBM Maximo |
|---|---|---|---|---|---|
| Asset register with identity/classification/location | yes (asset number/badge, types, locations incl. service points) | yes (inventory with location/condition/construction history) | yes (EAM module) | yes (EAM) | yes |
| Utility plant taxonomy named | meters, poles, pipes, transformers, conductors | "built assets in your network"; utility asset location | utilities = electric/gas/water | T&D, water/wastewater segments | generic (add-ons for linear/spatial) |
| Network structure on the record | linear assets with "Connected to"; GIS Map Viewer | embedded Esri GIS + LRS | via ERP/GIS integration | via integrations | linear/spatial add-ons |
| Work management bound to assets | activities (field/work/construction), work orders, PM triggers | work orders, inspections, work management | maintenance planning/scheduling/execution | EAM work management | work order management |
| Construction/new-network work as first class | yes — construction work activity class, work designs, compatible units, line extensions, reconciliation | lifecycle includes "build" (suite level) | via ERP project machinery | project management pillar | not prominent |
| Metering/device layer | operational devices (smart meters, comms, firmware), measurements | — | meter measurement concepts (industry layer) | — | — |
| Condition/risk → repair-vs-replace | asset health visualizations, APM built in | risk assessment (PoF × CoF), work plan optimization | cost/risk balancing, APM | reliability + AIP | compliance/risk tools |
| Capital/investment planning | separate product (CALM); WAM does investment planning basics | predictive analytics what-if + work plan optimization | ERP finance | separate AIP pillar | — |
| Cost/capitalization structure | fixed-asset interface, property units, member assets (poles/conductors/pipes), ERP projects | cost data per asset | ERP-native | ERP | ERP integration |
| Vegetation | tree trimming named as field activity | — | — | — | — |
| Compliance | approvals, permits, audit-grade records | inspections "safety and compliance" | "regulatory compliance" (Autonomous AM) | "reliability, compliance" | compliance tracking/reporting |
| Field/mobile | portals on iOS, crews | Unity Field mobile | FSM product | FSM product | Maximo Mobile |
| GIS posture | integrated (GIS Map Viewer; connectivity fields) | embedded Esri + LRS | integrated | integrated | add-on |
| Customer tier | large utilities (electric/gas/water) | utilities + municipalities + DOTs + airports | large utilities | mid/large utilities | large enterprises |

Stable across all five: asset register with identity/classification/location; work (orders/activities) bound to assets and closed into history; condition/risk/cost informing repair-vs-replace and investment; field/mobile execution; compliance concern; GIS as the location substrate.

Utility-distinctive (vs the generic-EAM baseline): the plant taxonomy (poles/conductors/transformers/mains/meters); network position/connectivity on the record; construction work that creates and capitalizes new network assets; the metering device layer; the fixed-asset/member-asset capitalization structure; vegetation work; service-point locations.

## Canonical Abstraction

### L0 — Defining Invariant

The utility operator's system of record for the physical plant of its service-delivery network, held across the whole asset life. Three jointly-held structures over a binding estate:

1. **The network plant register of record** — one identified record per physical asset of the utility's delivery network (the plant that delivers service: poles, conductors, transformers, substations, mains, valves, meters, and their components), classified, located (including service points / along-network positions), and placed in the network structure (hierarchy and, commonly, connections).
2. **Recorded care attached to assets** — inspections/condition/readings and work (planned, corrective, and field activities) bound to assets, executed by crews, and closed into persistent per-asset service history.
3. **Whole-life governance feeding capital decisions** — condition, cost, and risk accumulated per asset and rolled up into repair-vs-replace judgment and multi-year investment plans, with asset-level cost tracked to support the utility's capitalization accounting (fixed-asset/ERP interface).

Binding estate condition: the operator is a **utility delivering a continuous service through a network** — the estate is the network plant itself, held to sustain service reliability under regulatory obligations, with asset investment recovered through the utility's capital process. Remove the estate condition → generic EAM. Remove leg 3 → CMMS. Remove leg 2 → registry. Remove leg 1 → work/cost tracking with no asset backbone.

Historical check (§24): paper-era utility practice — pole and transformer ledgers, circuit maps, inspection records, maintenance logs, and an annual capital budget with property-unit cost accounting — satisfies all three legs with no software, no GIS, no cloud. Older and smaller-utility implementations (co-ops, munis running generic CMMS/EAM products configured for utility plant) also fit. The definition does not depend on any current implementation pattern.

### L1 — Common Mature Structure

- Preventive/predictive maintenance engine (schedules and triggers), work requests, service calls
- Construction work management as a first-class work class (work designs, compatible units, line extensions/new services) that creates and capitalizes new network assets
- Operational device management (metering assets: smart meters, communication components, measurements, configurations)
- MRO inventory, purchasing, crew/resource management, approvals
- GIS integration (map viewer, embedded GIS, linear referencing) as the location/connectivity substrate
- Mobile field execution
- Asset health/condition scoring, APM/predictive maintenance
- Asset investment planning / capital-planning scenarios (sometimes a separate pillar/product)
- Compliance tracking and reporting
- Financial transaction tracking (labor/equipment/materials costs of work; fixed-asset/ERP interface)

### L2 — Variant / Optional

- Industry flavor: electric T&D vs gas vs water/wastewater — different plant taxonomies, compliance regimes, and work types
- Condition-monitoring depth (digital asset management companions, sensor/AI predictive layers)
- Vegetation management as a dedicated discipline/product vs a work activity class
- Packaging: utility-specific suite vs ERP-embedded module vs GIS-embedded platform vs generic EAM configured for utilities
- Customer tier: investor-owned utilities vs co-ops/municipals
- Integration depth: OMS, SCADA, AMI/MDMS, CIS, ERP

### L3 — Vendor-specific (research notes only)

- Oracle: OUAF framework; Activity Type business object with Work Role / Track Cost flags; Asset 360 Portal; 360 Degree Search; badge numbers; Property Units / Member Assets mechanics; Send Asset Information Update; Operational Device Management as a separately deployable mode; Digital Asset Management/DACS companion; Capital Asset Lifecycle Management as a separate product; Louisville Water customer quote.
- Trimble: Unity suite composition (Construct/Permit/Field/Maintain); embedded Esri ArcGIS + LRS; Cityworks/AgileAssets heritage; probability-of-failure × consequence-of-failure dashboards.
- IFS: Asset Investment Planning pillar; "composable" IFS Cloud positioning.
- SAP: industry layer on S/4HANA; meter measurement concept management; Autonomous Asset Management branding.
- IBM: Maximo add-ons (linear asset manager, spatial visualization); watsonx AI layer.

## Vendor-specific Findings

- Oracle's three-class activity model (Field / Work / Construction) with per-class planning and cost flags is an implementation of a conceptual distinction (light field tasks vs planned costed work vs network construction) — not evidence that every product uses three classes.
- "Compatible units" (Oracle) is a utility-construction standard concept but its presence as a named structure is vendor-specific.
- Trimble's embedded-GIS posture vs Oracle's integrated-GIS posture vs Maximo's add-on posture — three realizations of the same conceptual dependency on the network model.
- Capital planning lives outside the core asset product in at least two vendors (Oracle CALM, IFS AIP) — supports keeping deep capital planning out of the defining core.

## Boundary Findings

- **vs EAM (§16)**: the three-leg family core is genuinely shared (register + work + whole-life governance). The differentiator is the estate and operator context: a connected service-delivery network held by a utility to sustain continuous service under regulatory obligations, with rate-recovery capitalization — vs EAM's general physical asset base. The EAM pass ratified "domain cousins keep their own spines"; this pass RATIFIES that reading from the utility side. Remove the network estate + utility context → EAM remains.
- **vs CMMS (§16)**: strip whole-life governance → CMMS remains (same test as the EAM pass).
- **vs Enterprise Asset Registry (§10)**: strip work and governance → registry.
- **vs Public Asset Management (§24)**: forward flag DISCHARGED and RATIFIED. The public-agency Type centers a mixed civil estate (roads/signs/trees/parks/facilities) under a public-stewardship frame; this Type centers a networked service-delivery estate under utility operations. Trimble Unity sells one platform into both worlds — family membership confirmed, estates and frames distinct. Remove the network-service estate → public-asset territory; remove the civil-mixed estate → this Type.
- **vs Utility GIS (§19, unprocessed)**: the GIS holds the georeferenced network model (layers, connectivity, LRS); this Type holds the asset records and their lifecycle, consuming GIS as location/connectivity substrate (embedded or integrated). Forward note for that pass: the seam is network-model-of-record vs asset-lifecycle-of-record.
- **vs OMS (§19, processed)**: OMS holds outage events and the restoration loop on the network; this Type holds the asset estate those events occur on. Consistent with the OMS pass's seams.
- **vs Utility FSM (§19, unprocessed)**: FSM centers the field workforce and scheduled work execution; this Type centers the asset estate and whole-life governance. Work orders flow between them. Forward note for that pass.
- **vs Power Plant Management / Renewable-Solar-Wind-BESS Asset Management (§19, processed)**: generation-side asset populations (plants, generating units, turbines) vs network/delivery-side plant. RATIFIED from this side: the delivery network (T&D, gas, water) is this Type's estate; generation fleets belong to the generation Types.
- **vs Utility Vegetation Management (§19, unprocessed)**: vegetation work appears inside this Type as a field activity class (Oracle names tree trimming); a dedicated vegetation-management discipline/product is a specialization. Forward note.
- **vs AMI / MDMS (§19)**: the meter as a physical asset (install, maintain, retire) lives here (operational devices); meter data and its management live in MDMS/AMI.
- **vs Capital Improvement Planning (§24)**: CIP decides which new investments to fund; this Type holds existing-asset condition/cost that feeds those decisions; construction work here executes approved network builds.
- Name-collision note: "utility asset management" is also used loosely in the market for financial-asset management (rate-base portfolios) — not this Type.

## Uncertainties

- No water-network-specialist or gas-network-specialist vendor documentation was reachable (Innovyze/Bentley 403/404); the water/gas evidence rests on multi-utility products (Oracle WAM water customer and pipe/manhole examples; IFS water/wastewater segment; Trimble water-treatment imagery). The three-utility claim is therefore stated at "commonly" strength, not per-utility depth.
- IBM Maximo's utility industry solution was not reachable; Maximo is used as the generic-EAM baseline only.
- Oracle brochure PDF was binary-unusable; all Oracle evidence comes from HTML user-guide pages (still Tier 1).
- Regulatory-compliance depth (specific regimes: NERC-class, PHMSA-class, state PUC reporting) was not directly evidenced in fetched pages; compliance is asserted only as a standard concern (tracking/reporting), not as regime-specific machinery.
- Whether every utility asset product holds asset-to-asset connectivity natively (vs leaving it entirely to GIS) is uncertain; evidence shows both postures (Oracle native "Connected to" fields + GIS viewer; Trimble embedded GIS). Canonical statement kept at "network position (location and commonly connections) is part of the record; the full network model is commonly sourced from GIS".
- Numeric limits, default values, and status vocabularies were not collected and are not asserted anywhere.

## Final Synthesis

Utility Asset Management is the utility operator's system of record for the physical plant of its service-delivery network. It is a domain cousin inside the asset-management family: the family core (register + recorded care + whole-life governance) is held unchanged, but over a distinctive estate — the connected network plant (poles, conductors, transformers, substations, mains, valves, meters) whose job is to deliver continuous service to customers — and under a distinctive operator context — regulated service obligations and capital recovered through the utility's capitalization process. The market realizes the Type as utility-specific suites (Oracle WAM), GIS-embedded platforms (Trimble Unity Maintain), ERP-embedded modules (SAP), and generic EAM configured for utilities (Maximo, IFS), with deep capital planning often packaged as a separate pillar. The Type is distinct from EAM (estate + operator context), from Public Asset Management (networked service estate vs mixed civil estate), from Utility GIS (asset lifecycle vs network model), from OMS (asset estate vs outage events), and from the generation-side asset Types (delivery plant vs generation plant).
