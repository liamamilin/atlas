# Research Notes — Marine Fleet Management

## Research Goal

Understand what "Marine Fleet Management" is as an Application Type: what software shipowners, ship managers, and operators run to manage a fleet of vessels as assets — and how it differs from road-vehicle Fleet Management, from vessel tracking, from freight/chartering systems, and from the neighboring §18 marine leaves.

## Initial Boundary

- Leaf: Marine Fleet Management (§18 Transportation, Mobility & Logistics, between Flight Planning Application and Vessel Operations Platform).
- Hypothesis at start: the owner/manager-side system for a fleet of vessels — technical management (planned maintenance, spares), crewing, compliance, procurement, costs — as opposed to voyage execution, cargo/chartering, port operations, or marina berthing.
- Confusable neighbors flagged by prior passes:
  - fleet-management-system (§18, processed): "same register + activity + oversight pattern generalizes to non-road fleets, but those leaves carry domain-specific telemetry/operations the road-vehicle core model does not capture — related Types sharing an oversight pattern; flagged for joint review when those leaves are processed."
  - fisheries-management (§20, processed): "vessels as authorized participants inside the fishery's record world vs vessels as logistics/crew/maintenance assets."
  - vessel-operations-platform (§18, unprocessed sibling), ocean-freight-management (§18, unprocessed), marina-management (§18, processed — boundary already held from that side), mining-fleet-management / robot-fleet-management (§16/§20 siblings).

## Research Questions

1. What is the unit of record — the vessel? the fleet? the component? the job?
2. How is a vessel's technical record organized (component/equipment tree vs flat)?
3. Who executes work (crew onboard) and who manages (shore office)? How does the ship–shore loop work, especially with intermittent connectivity?
4. What compliance machinery is structural (class, statutory certificates, ISM/ISPS-class safety management) vs module packaging?
5. Which modules are definitional vs common vs optional: crewing, procurement, HSQE, dry dock, voyage/fuel/performance, logbooks, accounting?
6. Where is the seam vs road Fleet Management System, vs Vessel Operations Platform, vs Ocean Freight Management, vs Fisheries Management, vs generic CMMS/EAM?
7. Historical check: does the definition survive the paper-era ship management office and the 1980s–90s software generation?

## Representative Products

| Product | Vendor | Why sampled | Evidence tier reached |
|---|---|---|---|
| AMOS (AMOS™ / Gateway / Horizon / Enterprise) | SpecTec | Market-leading maritime asset management suite, 40+ years, class-approved PMS; maintenance-led philosophy; all fleet sizes | A (root + Maintenance module page) |
| SERTICA | RINA (Logimatic heritage) | Class-society-owned modular ship management system; strong ship–shore framing; module-level packaging visible | A (root + Maintenance page incl. FAQ) |
| smartPAL | MariApps | ERP-style 30+ module suite with segment editions (cruise/offshore/ferry/yacht); offline replication; SaaS pole | A (root + smartPAL page incl. FAQ) |
| ShipPalm (+ ZeroNorth platform) | ZeroNorth | Modern AI-native performance/voyage-optimization vendor that also ships a fleet-management ERP; documents the performance-layer vs fleet-record seam from the inside | A (root + ShipPalm page incl. FAQ) |

Considered and dropped (network-restricted, per rules — no claims made about them): ABS Nautical Systems / NS Enterprise (abs-ns.com transport error; nautical-systems.com 403), DNV ShipManager (dnv.com 404 ×2), Kongsberg K-Fleet (403), Danaos (429 ×2), BASS Software (transport error). These absences are recorded as a sourcing limitation; the four-product sample still spans four philosophies and multiple customer tiers (MSC/Grimaldi-class owners at AMOS; Hapag-Lloyd/Svitzer at SERTICA; Maersk/BSM/MOL/BP at MariApps; Cargill/CMB/Maersk Tankers at ZeroNorth).

## Sources

- SpecTec — https://spectec.net/ (fetched 2026-09-09) — positioning, module map, product tiers, FAQ
- SpecTec — AMOS Maintenance — https://spectec.net/amos-software/amos-maintenance/ (fetched 2026-09-09) — class-approved PMS, scheduling triggers, on-board/ashore split, FAQ
- SERTICA by RINA — https://www.sertica.com/ (fetched 2026-09-09) — product map (Maintenance, Procurement, HSQE, Crewing, Performance, VRS, Logbook, Fleet), customer cases
- SERTICA — Maintenance — https://www.sertica.com/maintenance/ (fetched 2026-09-09) — component tree, job list, defect reporting, inventory-linked maintenance, module list, PMS FAQ
- MariApps — https://www.mariapps.com/ (fetched 2026-09-09) — product family, segment editions, scale claims
- MariApps — smartPAL — https://www.mariapps.com/smartpal/ (fetched 2026-09-09) — full module map (Technical/Procurement/HR/Commercial/HSEQ/Finance/Insurance/LiveFleet), offline replication FAQ, class certification
- ZeroNorth — https://zeronorth.com/ (fetched 2026-09-09) — platform map (SMARTShip, Voyage Optimisation, Vessel Reporting, Emission Analytics, Bunker Procurement, eBDN, ShipPalm)
- ZeroNorth — ShipPalm — https://zeronorth.com/shippalm (fetched 2026-09-09) — unified fleet management, document/certificate management, maintenance & dry dock, ShipPalm-vs-SMARTShip split FAQ

Prior-pass context (not fetched this pass): research/fleet-management-system.md (road FMS core + sibling flag), research/fisheries-management.md (vessel-as-participant framing), research/marina-management.md (facility-side boundary), research/aircraft-maintenance-management.md (parallel register+maintenance-program+airworthiness structure).

## Product A — SpecTec AMOS

### Key observations [A — direct]

- Self-label: "Maritime Asset Management" / "purpose-built ship management software"; "AMOS is maritime fleet and asset management software designed for the real-world demands of ship and shore teams operating under regulatory, commercial, and operational pressure."
- Scope sentence: "From planned maintenance and inventory control to procurement, compliance, and workforce management, AMOS connects your critical workflows into one secure, audit-ready platform."
- "It centralises maintenance, inventory, procurement, quality & safety, dry dock planning, and crew management into one connected maritime platform."
- Users: "technical, procurement, HSEQ, and executive teams"; "ship and shore teams"; "Shipowners, operators, and technical managers rely on AMOS™ as their digital backbone."
- Fleet types: "bulk, container, offshore, RoRo, and mixed fleet operations"; "Whether managing a few vessels or hundreds."
- Modules: Maintenance ("Class-approved planned maintenance software"), Inventory ("right spares on board and ashore with full fleet-wide inventory visibility"), Procurement, Quality & Safety ("Integrated ISM, ISPS, SOLAS, and MARPOL compliance management with full audit traceability and corrective action control"), Data Analytics, Staff Management ("Crew and workforce planning aligned with certifications, compliance, and operational readiness").
- Product tiers: Gateway ("Structured asset management for growing fleets"), Horizon ("Fleet-wide standardisation for scaling fleets"), Enterprise ("Enterprise asset management for complex operations"), Procure Smart.
- Maintenance page: "class-approved planned maintenance system (PMS) designed for fleets operating safety-critical assets in regulated environments"; "a single, consistent framework for planning, executing, and recording maintenance across vessels – giving shore teams fleet-wide visibility while allowing crews to work effectively on board, even in low-connectivity conditions."
- Scheduling triggers: "time, running hours, or condition"; condition monitoring/predictive via sensor integration (FAQ).
- On-board vs Ashore split: onboard crews get "clear task lists, structured work instructions, and full equipment history"; ashore superintendents get "fleet-wide oversight of maintenance status, asset condition, and compliance from shore… consolidated data from across the fleet."
- Central Data Management: "standardising task structures and asset hierarchies across vessels."
- Drydock Project Management "within the same maintenance framework, linking tasks, budgets, and execution history."
- Critical Analysis: "Identify critical equipment and failure modes."
- Mobile: "crews to execute, record, and close maintenance tasks on board – even in low-bandwidth or offline environments."
- FAQ: core modules "Maintenance Management, Procurement, Inventory Tracking, Quality Assurance, and Compliance. Additional features like Fleet Analytics and Reporting are also available"; integrates "with Enterprise Resource Planning (ERP) systems, crewing software, and accounting tools"; deployment "on-premise, cloud, or hybrid"; tracks "labor, materials, and third-party service costs for each maintenance task."
- Approved by major classification societies (ABS, Bureau Veritas, CCS, ClassNK, DNV, Lloyd's Register, RINA logos shown).
- Scale claims: 3,000+ vessels, 40+ years (marketing numbers — L3).

## Product B — SERTICA (RINA)

### Key observations [A — direct]

- Self-label: "Ship Management Software"; page title "Fleet Management System | Planned Maintenance | SERTICA"; "Built for maritime operations, SERTICA replaces disconnected tools with a single digital ecosystem. Plan maintenance, control purchasing, prove compliance and optimize fuel. Connecting everything from bridge to office."
- Products: Maintenance, Procurement, HSQE, Crewing, Performance, VRS (Vessel Reporting System), Logbook, Fleet (data-integration layer: "Retrieve data from any system… Demolish data silos").
- Maintenance page: "At the heart of the system is a structured component tree that reflects the real-world layout of your vessel. Each component and subcomponent forms part of the hierarchy, allowing you to plan, execute, and document tasks with accuracy and consistency."
- Job machinery: "structured job lists and task breakdowns… ensuring tasks are performed in the right order… with job relations"; "standardizing and automatically generating recurring jobs based on predefined intervals or usage data"; corrective work logged "alongside scheduled tasks."
- Users: "From chief engineers to superintendents, everyone works from the same operational picture."
- Fleet-wide supervision: "Track maintenance activity across all vessels from a single point of control… dashboards to monitor performance trends… Apply centralized standards to unify planning across vessels."
- Defects: "Log defects as they occur and convert them directly into corrective jobs… Link each report to the relevant component, assign responsibility, and track resolution."
- Inventory-linked maintenance: "Link jobs directly to inventory items, trigger requisitions when stock runs low, and track consumption automatically during task execution."
- Modules included: Analytics (KPIs, dry dock analysis), Defect Reporting, Document Management, Inventory Management, Job List, SYNC ("Synchronize data between SERTICA and other third-party systems").
- Add-on modules: Approval Web App, Dry Dock ("from the first specification and tendering to execution, final reporting, and preparation of the next dry docking"), Dynamic Dashboard, Forms ("permits to work, checklists"), Item Certificate ("Manage item certificates and Inventory of Hazardous Materials from purchase to consumption"), Jobtext Management ("Share makers manuals electronically and change procedures and parameters on several ships at once"), Maintenance API, Master Data Management, Mobile App (QR codes).
- PMS definition (FAQ): "A Planned Maintenance System (PMS) is a digital tool that helps shipping companies plan, execute, and document maintenance to ensure optimal vessel performance and compliance with industry standards."
- Maintenance strategies (FAQ): preventive (time/usage), predictive (condition monitoring), corrective; "a maintenance job can be set up based on calendar time, running hours, or condition-based indicators."
- Maritime CMMS framing: "Investing in a Maritime CMMS… improves internal workflows and ensures reliable data exchange between vessels and shore-based offices."
- Packaging: "Choose modules you need today and add more as you grow"; SERTICA Cloud service; single-vessel to global fleets ("single operated super yachts to the world's largest container ships").
- Customer cases: Svitzer (400+ vessels, standardization), Hapag-Lloyd (replaced several systems with SERTICA for maintenance, procurement, HSQE), Stena RoRo (master data: "our crew will see the same component structure regardless of which vessel they are assigned to"), Condor Ferries (Safety Management System digitalization).
- Class-society heritage: RINA; customer quote praises "skills typical of a Class Society."

## Product C — MariApps smartPAL

### Key observations [A — direct]

- Self-label: "Ship management software for smarter maritime operations"; "a comprehensive suite of web-based, cloud-supported, and mobile-compliant maritime digital solutions. With over 30 modules."
- Module map (grouped):
  - Technical: Maintenance ("full data library of vessel equipment, spares, and jobs managed in a centralized setup, simplifying moving spares between ships. Certified by DNV, Bureau veritas, ABS, LR, and CCS"), Drydock ("standardized platform for dry dock planning"), Data Library.
  - Procurement: Procurement ("from requisition of goods and/or services to finalizing stock inventory through recording of goods received… multi-level approval"), eConnect (buyer–vendor eCommerce), Catering (provisions).
  - HR: Crewing ("manage the ship crew pool, sign on/off, transfer, and promote/demote seafarers… PAL-created CVs… certifications, documentation, and licenses"), Payroll (multi-national, multi-currency), Sea Roster ("compliance with crew work and rest hour regulations"), New Applicant (recruitment).
  - Commercial: "management of vessel employment, voyages, charter expenses, and owner expenses… tracks vessel availability, delivery, and redelivery status with voyage schedules."
  - HSEQ: HSEQ ("highlights non-conformities"), QDMS ("ship-shore integrated ship safety management module… document management"), Certification ("all certification documents and survey records related to the HSEQ operations of vessels").
  - Finance: Accounts ("multinational, multicurrency, multicompany… from the time a vessel enters management until it leaves"), Financial Reporting, Treasury, Fixed Assets, I2P (invoice processing), PAL eXtrack.
  - Insurance: claims handling. Plus CRM, BI, LiveFleet ("near real-time data on a vessel's operating KPIs (both technical and non-technical)").
- Ship–shore data: "seamless data migration between shore and sea, that is updated every second"; offline: "smartPAL supports offline modules where crews can continue working. The replication module within the suite will sync up data between the ship and shore once internet is available."
- Class certified: "complies with most class certification societies, following the international regulatory framework."
- FAQ: "vessel operations to be managed from a single dashboard, including crew, safety, compliance, maintenance, procurement, and more"; compliance machinery: "built-in rule engines to identify nonconformities, audit trails, checklists, certificate tracking, expiration reminders, and automated reporting"; RBAC/MFA/audit trails/encryption.
- Segment editions: smartPAL (shipping), cruisePAL, offshorePAL (adds offshore financials/CRM), ferryPAL, yachtPAL ("yacht management software… from ownership and crew management to procurement, finance, and environmental compliance").
- Scale claims: 5,100+ vessels, 127+ clients (marketing — L3). Clients incl. Maersk, BSM, MOL, BP Shipping, Hapag-Lloyd, Bourbon (logos).

## Product D — ZeroNorth ShipPalm (+ platform)

### Key observations [A — direct]

- ShipPalm self-label: "Vessel management software for ship owners and managers"; "Maritime ERP for fleet management and operations."
- "Unify vessel operations, documentation, procurement, and reporting into one structured system. ShipPalm transforms fragmented ship management workflows into a single source of truth across your fleet."
- "Unified Fleet Management System — Manage procurement, maintenance, and reporting within a single platform. Replace siloed tools with a structured system that connects all operational workflows."
- Document & Certificate Management: "Maintain ship-specific statutory documents and certificates in a structured system. Automatically track expiry timelines and ensure compliance across the fleet."
- Procurement & Purchase Management: "Centralise procurement workflows across vessels. Manage purchase orders, vendors, and approvals."
- Maintenance & Dry Dock Management: "Manage planned maintenance, defect reporting, and dry dock activities within one system."
- FAQ coverage: "crewing, procurement, maintenance, document management, compliance tracking, and performance reporting within a single system."
- ShipPalm vs SMARTShip split (FAQ): "ShipPalm provides the operational data foundation and workflow management. SmartShip uses that data to monitor performance and ensure voyages execute as planned." Also: "ShipPalm acts as the underlying data infrastructure for ZeroNorth's optimisation products ensuring voyage, vessel, and bunker decisions are based on accurate, structured operational data."
- Scale claims: 6M+ work orders/year, $1.4B annual purchases, 23M+ purchase lines, 5,500+ vessels on platform (marketing — L3).
- Surrounding platform (separate products): SMARTShip (onboard data acquisition/reporting), Voyage Optimisation, Vessel Reporting (automated noon/arrival reports), Emission Analytics (CO₂, CII/EU ETS framing), Bunker Procurement/Pricer, eBDN, Charter Select, Scope 3.
- Governance: "Multi-layered data validation", RBAC, enterprise-grade data governance.

## Cross-product Comparison

| Dimension | AMOS (SpecTec) | SERTICA (RINA) | smartPAL (MariApps) | ShipPalm (ZeroNorth) | Layer |
|---|---|---|---|---|---|
| Fleet register of identified vessels | ✔ (asset hierarchies across vessels; few→hundreds) | ✔ (all vessels from single point of control; single yacht→container ships) | ✔ (5,100+ vessels; segment editions) | ✔ (across vessels and shore teams; 5,500+ platform) | A×4 |
| Per-vessel technical record on equipment structure | ✔ (asset hierarchies, equipment history, critical equipment) | ✔ (component tree mirrors the vessel; jobs/history/documents/spares per component) | ✔ (data library of vessel equipment, spares, jobs) | ✔ (maintenance with defect reporting; work orders 6M+/yr) | A×4 |
| Planned maintenance triggers: time / running hours / condition | ✔ (FAQ) | ✔ (FAQ) | ✔ (PMS module; class-certified) | ✔ (planned maintenance) | A×3 (ShipPalm triggers not itemized) |
| Defects → corrective jobs | ✔ (reporting module) | ✔ (defect reporting module) | ✔ (via maintenance/HSEQ) | ✔ (defect reporting named) | A×4 |
| Spares/inventory linked to jobs | ✔ (inventory module) | ✔ (inventory-linked maintenance; requisitions on low stock) | ✔ (spares moving between ships) | ✔ (procurement/purchase management) | A×4 |
| Ship–shore loop with offline-tolerant onboard execution | ✔ ("low-connectivity or offline") | ✔ (SYNC module; synchronized onboard/ashore) | ✔ (replication module; offline modules) | ✔ (ship–shore single source of truth; validation layers) | A×4 |
| Crew executed work onboard (job lists, forms, mobile) | ✔ (mobile, low-bandwidth) | ✔ (app, QR codes, forms/permits) | ✔ (mobile apps, offline) | ✔ (workflow management; crewing in FAQ) | A×4 |
| Crewing module (records, certification, rotation, payroll) | ✔ (Staff Management; also integrates external crewing software) | ✔ (Crewing product) | ✔ (Crewing/Payroll/Sea Roster/New Applicant) | ✔ (crewing in FAQ coverage) | A×4 — but AMOS FAQ shows external crewing integration ⇒ module, not invariant |
| Procurement (requisition→approval→PO→receipt) | ✔ | ✔ | ✔ (+eConnect marketplace) | ✔ ($1.4B purchases) | A×4 |
| HSQE / safety management (ISM-class) | ✔ (Quality & Safety: ISM/ISPS/SOLAS/MARPOL framing) | ✔ (HSQE product; SMS cases) | ✔ (HSEQ/QDMS) | ✔ (compliance tracking) | A×4 |
| Certificates/surveys with expiry tracking | ✔ (compliance records; class approval) | ✔ (Item Certificate module) | ✔ (Certification module; expiration reminders) | ✔ (statutory documents, expiry timelines) | A×4 |
| Dry dock as managed project | ✔ | ✔ (add-on module: spec→tender→execution→report) | ✔ (Drydock module) | ✔ (Maintenance & Dry Dock) | A×4 |
| Master data / structure standardization across fleet | ✔ (central data management) | ✔ (MDM module; Stena case) | ✔ (Data Library templates) | ✔ (structured single source of truth) | A×4 |
| Budgets/costs per vessel | ✔ (labor/materials/service costs) | ✔ (dry dock budgeting; analytics) | ✔ (Accounts/budgets) | ✔ (budgets on dashboard) | A×4 |
| Voyage/fuel/performance layer | △ (Data Analytics; IoT data in FAQ) | ✔ (Performance, VRS, Logbook products) | ✔ (LiveFleet, FleetPulse, smartLogs, smartOps) | △ (separate SMARTShip/Voyage products; ShipPalm is the data foundation) | A×2 full + A×2 adjacent ⇒ common, not definitional |
| Electronic logbooks | — (not observed) | ✔ (Logbook product) | ✔ (smartLogs) | — (not observed) | A×2 ⇒ common |
| Accounting/finance suite inside the product | △ (integrates ERP/accounting) | — (not observed as product) | ✔ (full finance suite) | △ (reporting; purchases) | mixed ⇒ variant |
| Commercial/chartering module | — | — | ✔ (Commercial) | — (Charter Select is a separate product) | A×1 ⇒ optional |
| Segment editions (cruise/ferry/offshore/yacht) | — (fleet types listed) | — (vessel types listed) | ✔ (PAL family) | — | A×1 ⇒ variant |
| Deployment: on-prem/cloud/hybrid | ✔ (FAQ) | ✔ (SERTICA Cloud) | ✔ (SaaS) | ✔ (SaaS implied; governance) | A×4 ⇒ variant |
| Class approval of the maintenance system itself | ✔ (class-approved; society logos) | ✔ (RINA heritage; class framing) | ✔ ("Certified by DNV, BV, ABS, LR, CCS") | — (not observed) | A×3 ⇒ strong common structure |
| AI overlays | ✔ (Procure Smart; predictive FAQ) | — | ✔ (OceanAI; I2P) | ✔ (agentic Propel; AI-native framing) | A×4 ⇒ era machinery |

## Canonical Abstraction

### L0 — Defining Invariant

Marine Fleet Management is the shipowner/manager's fleet-side system of record. Its defining core is exactly three jointly-held structures:

1. **The fleet register of identified vessels** — the operator's vessels exist as individually identified, managed records (vessel identity, attributes, fleet grouping) inside one organization-scoped system (owner's or third-party manager's). Remove → disconnected per-vessel tools or a bare vessel list; there is no fleet to manage.

2. **The per-vessel technical record organized around the vessel's equipment** — each vessel carries a living technical file structured on its equipment/components, accumulating planned-maintenance jobs (triggered by calendar time, running hours, or condition), defects and corrective work, spare parts, certificates/documents, and costs against that structure. Remove → a flat asset list or a standalone CMMS with no vessel-shaped memory; maintenance, spares, and certificates stop cohering.

3. **The ship–shore management loop** — work is executed and recorded onboard by the vessel's crew (tolerant of intermittent connectivity), synchronized to the shore office, where superintendents/technical managers oversee fleet-wide status, plan, approve, and standardize, with management actions flowing back to vessels. Remove → a shore-only archive or an onboard tool; fleet-level management disappears.

Jointly-held load-bearing:
- 1 alone = vessel registry / contact-style list
- 2 without 1 = single-vessel maritime CMMS
- 3 without 1+2 = messaging/sync plumbing
- 1+2 without 3 = shore archive the crew never feeds
- 1+3 without 2 = oversight with no technical memory
- Domain binding: the managed assets are ships/vessels in marine operation — remove the marine context (equipment tree of ship systems, class/statutory machinery, crew certification, dry dock, sea-going connectivity) and the remainder is generic fleet/asset management.

### L1 — Common Mature Structure

Present in essentially all mature products; expected by the market but not definitional:

- Planned-maintenance machinery depth: job relations, recurring job generation, templates, critical-equipment analysis
- Crewing management: seafarer records, certification/competency tracking, sign on/off, rotation planning, payroll, work/rest-hour compliance
- Procurement & spares: requisitions (often raised onboard), multi-level approvals, POs, vendors, goods receipt; spares linked to components and jobs
- HSQE / safety management: incident and non-conformity reporting, audits, corrective actions, permits-to-work/forms, ISM/ISPS-class safety-management-system support
- Certificate & survey tracking: statutory/class certificates with expiry alerts, survey records
- Dry dock management: specification, tendering, execution, reporting, budget
- Fleet-wide dashboards & analytics: overdue jobs, defects, KPIs, budgets across vessels
- Document management: ship–shore distribution of manuals, procedures, job texts
- Master data standardization: shared component structures across sister vessels
- Mobile/offline onboard apps; QR-code equipment access
- Roles & permissions separating office and onboard; approval chains
- Class approval of the maintenance system itself (PMS certified by class societies)

### L2 — Variant / Optional Structure

- Voyage/fuel/performance layer: noon/arrival reporting, fuel consumption, emissions (CII/EU ETS/FuelEU-class), voyage optimization, weather routing — realized as modules (SERTICA Performance/VRS, smartPAL LiveFleet) or as separate products layered on the fleet record (ZeroNorth SMARTShip/Voyage Optimisation)
- Electronic logbooks (regulatory record books: bilge/sludge/garbage class)
- Segment editions: deep-sea cargo, ferries/RoRo, offshore/workboats, cruise, yachts, tugs
- Commercial/chartering modules (vessel employment, voyage estimates) — seam with Ocean Freight Management
- Full accounting/finance suites vs integration to external ERP/accounting
- Insurance/claims modules; catering/provisions; CRM
- Onboard sensor/IoT condition monitoring and predictive maintenance depth
- Deployment: on-premise / cloud / hybrid; SaaS
- AI overlays (procurement intelligence, invoice processing, agentic assistants)
- Single-vessel pole (yacht management) through global fleets

### L3 — Vendor-specific (kept out of the final document)

- AMOS tiering (Gateway/Horizon/Enterprise), AMOS-X naming, "Asset Management Operating System" backronym, 3,000+ vessels / 40 years claims, SFI-expert consulting framing
- SERTICA's INEXTIA sibling product, FuelEU simulator lead-gen, specific customer cases (Svitzer 400+, Stena master-data quote)
- smartPAL PAL-family naming, eConnect marketplace, OceanAI/OceanOpt/SeaMedix satellite products, 5,100+ vessels claim
- ZeroNorth Propel agent, SMARTShip/eBDN/Charter Select product names, 6M+ work orders / $1.4B / 5,500+ vessels claims
- Class-society parentage of specific vendors (RINA owns SERTICA; DNV/ABS market their own suites — unreachable this pass)

## Rejected Findings (anti-overfit)

- **"Ship–shore cloud sync" is not definitional** — the invariant is the two-sided loop (crew executes/records onboard; shore plans/approves/oversees); the transport (paper, replication module, real-time sync) is era/implementation machinery. Paper-era offices satisfy the loop.
- **Component-tree hierarchy as a hard requirement is not asserted** — all four deep samples organize the technical record on equipment structures, and the tree is the standard realization, but the L0 leg is phrased as "organized around the vessel's equipment," not as a specific tree UI.
- **Crewing module is not definitional** — AMOS's own FAQ documents integration with external crewing software; the *crew as executing party* is part of the loop (L0 leg 3), while crew *management* is L1.
- **HSQE/ISM module is not definitional** — module-level packaging varies (SERTICA sells modules separately; AMOS Gateway is an entry tier); certificates/surveys are L1-strong.
- **Voyage/fuel/performance is not definitional** — ZeroNorth's own ShipPalm-vs-SMARTShip split documents it as a separate layer over the fleet record; AMOS's core is maintenance-led with analytics as an add-on.
- **AIS/GPS tracking is not definitional** — no sampled product centers on tracking; tracking appears as an adjacent product class (LiveFleet, SMARTShip data acquisition) consistent with the road-FMS pass's telematics-vs-management seam.
- **Class-society ownership is not definitional** — it is a market-structure fact (RINA/SERTICA; DNV/ABS suites) that shapes trust framing, not a Type property.
- **Specific regulation sets (ISM/ISPS/SOLAS/MARPOL/CII/EU ETS) are not definitional** — regime machinery that varies by era and flag; the invariant is that the system maintains compliance records the operator must produce, not any specific code list.

## Boundary Findings

- **vs Fleet Management System (road, §18 — joint review flag DISCHARGED)**: the two Types share the family pattern (register + per-unit record + oversight loop). The road FMS core model does not capture the marine Type's defining structures: the equipment-structured technical record (component tree with class-linked maintenance), the crew-executed ship–shore loop with offline tolerance (vs dispatcher-watched live telemetry), class/statutory survey & certificate machinery, dry dock as a managed project, and crew certification/rotation. Conversely the marine core does not capture driver-centric oversight (HOS, driver scores, driver apps as the main sensor). Verdict: **keep-both, related Types sharing an oversight pattern** — consistent with the fleet pass's own framing ("domain-specific telemetry/operations the road-vehicle core model does not capture"). Removal test: strip the marine structures → a generic register+record+oversight product (road-FMS-shaped); add drivers/road telemetry to the marine core → road FMS.
- **vs Fisheries Management (§20 — forward flag DISCHARGED)**: in this Type the vessel is a **logistics/crew/maintenance asset** of its owner; in fisheries-management the vessel is an **authorized participant** inside the fishery's frame, and the record world is catch/effort/entitlements. No shared record objects; a fishing company can run both (fleet management for its vessels, fisheries compliance for its catch). Keep-both ratified.
- **vs Vessel Operations Platform (§18 sibling, unprocessed — forward flag left)**: evidence from inside one vendor family (ZeroNorth): ShipPalm = "operational data foundation and workflow management" for the fleet; SMARTShip/Voyage products = performance monitoring and voyage execution over that data. SERTICA similarly splits Maintenance/Procurement/HSQE/Crewing from Performance/VRS/Logbook. Hypothesis for that pass: Vessel Operations Platform centers on voyage execution/operations (voyage lifecycle, onboard operational reporting, fleet operations monitoring), while Marine Fleet Management centers on the fleet-as-asset administration (technical, crew, compliance, procurement, costs). Flag left for that pass; this-side evidence only.
- **vs Ocean Freight Management (§18, unprocessed)**: freight/chartering is the cargo business (bookings, rates, documents, demurrage); this Type is the vessel-asset business. smartPAL's Commercial module and ZeroNorth's Charter Select sit on the seam inside suites — packaging evidence that the two record worlds are distinct.
- **vs Marina Management (§18, processed)**: boundary already held from that side ("those manage the vessel owner's fleet; marina manages the facility operator's spaces and berthing business"). Confirmed: no berth/space inventory exists in this Type's core.
- **vs Boat/Yacht Charter Platform (§18, unprocessed)**: demand-side time-use marketplace vs owner-side asset management; yachtPAL shows yacht *management* is a single-vessel variant of this Type, not the charter marketplace.
- **vs Aircraft Maintenance Management (§06-adjacent, processed)**: parallel structure (identified-unit register + usage-driven maintenance program + airworthiness/survey record). Marine analog of the airworthiness record is the class/statutory survey & certificate state. Related Type, different domain; no merge.
- **vs CMMS / EAM (§16, processed)**: the maintenance module is a "maritime CMMS" (SERTICA's own term) — generic CMMS lacks the vessel register, ship–shore loop, and class machinery; EAM spans all asset classes without the marine operational context. The marine Type is the domain-specialized sibling.
- **vs Mining/Robot Fleet Management (§16/§20 siblings)**: same family pattern; mining is production-cycle-centric (per construction-equipment pass), robots are task-execution-centric; marine is asset-administration-centric with crew and compliance machinery. Related Types.

## Historical / Market-Sample Check (§24)

- **Paper-era ship management office**: per-vessel file with maintenance schedule cards, survey status records, certificate register, crew lists and agreements, requisition books sent to ships, returned reports and vouchers, OPEX ledgers; the office planned and approved while ships executed and reported back. Satisfies all three L0 legs with no software, no AIS, no cloud. → L0 survives.
- **1980s–90s software generation**: AMOS itself carries a 40-year framing; the class-approved PMS + spares + purchasing + crewing generation ran on-premise with scheduled data exchange — satisfies the core with no cloud/AI/real-time telemetry. → L0 survives.
- **Regional/segment breadth**: Greek-style third-party managers (Danaos class — unreachable but market-known), Indian ERP suites (MariApps), Nordic class-society tools (SERTICA), single-yacht management (yachtPAL) — all fit the three legs. The definition names no flag state, no regulation set, no connectivity level, no deployment shape.
- **Platform-native check**: no sampled product requires AIS data, sensor feeds, or real-time connectivity to satisfy the core; offline-tolerant operation is explicitly documented (AMOS, smartPAL). → tracking-free form is first-class.

## Uncertainties

1. **ABS NS Enterprise / DNV ShipManager / Kongsberg K-Fleet / Danaos unreachable** (403/404/429/transport errors). The class-society-vendor pole and the Greek ship-management ERP pole are therefore held at market-structure strength only; no product-specific claims made about them. The four-product sample is judged sufficient (four philosophies, four customer tiers), but the sample is Europe/India-weighted; Japanese/Korean owner-built systems unobserved.
2. **Entry-tier minimal pole unobserved**: whether any current product ships *only* the three L0 legs (register + technical record + loop) without crewing/procurement/HSQE was not directly verified; AMOS Gateway ("structured asset management for growing fleets") and SERTICA's module-level packaging suggest yes, but this is inference from packaging, not a documented minimal deployment.
3. **Vessel Operations Platform seam** is hypothesized from the ShipPalm/SMARTShip split and SERTICA's module split; the sibling leaf is unprocessed, so the seam is a forward flag, not a settled boundary.
4. **Multi-owner segregation machinery** (third-party managers running many owners' fleets in one system) was not directly evidenced; mentioned as context only.
5. **Onboard sensor/condition-monitoring depth** varies and was observed only at FAQ/marketing strength (AMOS condition-based triggers; SERTICA predictive strategy) — held at L2.
6. **Work/rest-hour regulation machinery** (Sea Roster) observed in one product — held product-specific-in-sample.

## Final Synthesis

Marine Fleet Management is the shipowner's or ship manager's fleet-side system of record: it holds the fleet as identified vessel records, gives each vessel a living technical file organized on its equipment (planned maintenance, defects, spares, certificates, costs), and runs the ship–shore loop through which crews execute and record work onboard while shore-based superintendents and technical managers plan, approve, standardize, and oversee the whole fleet. Around that core, mature products add crewing, procurement, HSQE/safety management, certificate and dry-dock machinery, document distribution, analytics, and class-approved maintenance records; voyage/fuel/performance layers, electronic logbooks, segment editions, commercial/chartering modules, and finance suites are variant packaging. The Type shares the register + record + oversight family pattern with road Fleet Management but is defined by marine-specific structures the road core does not capture; it is distinct from vessel tracking (data layer), from voyage/freight systems (cargo business), from fisheries management (vessels as participants, not assets), and from marina management (facility side).
