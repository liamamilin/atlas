# Research Notes — Enterprise Asset Management / EAM

Research date: 2026-09-08
Slug: enterprise-asset-management-eam
Directory leaf: Enterprise Asset Management / EAM (§16 Engineering, Manufacturing & Industrial)

---

## Research Goal

Understand what Enterprise Asset Management (EAM) software actually is as an Application Type: what the "enterprise" adds beyond maintenance work management (CMMS), how the asset lifecycle (acquisition → in-service → disposal) is governed, how asset costs and financial tracking work, how the register / work / lifecycle structures relate, and where the Type's boundary sits against CMMS, asset registries, ERP, ITAM, aftermarket service, and domain-specific asset systems.

This leaf carries a **joint-review obligation** from the processed cmms-maintenance-management pass, which flagged a convergent-market gradient ("every EAM contains a CMMS") and recorded removal tests (strip asset financial lifecycle → CMMS; strip work orders → asset registry). This pass ratifies or refines that seam from the EAM side.

## Initial Boundary (hypothesis before research)

- Core use: organization-wide system of record for physical assets across their full life — register + maintenance work management + asset lifecycle/financial governance (procurement, capitalization/cost, capital planning, disposal).
- Primary users: maintenance/asset operations (planners, supervisors, technicians) plus asset managers, reliability engineers, finance-adjacent roles.
- Nearest neighbors: CMMS / Maintenance Management (closest, joint-review sibling), Enterprise Asset Registry, ERP, IT Asset Management, CMDB, Reliability Management, Aftermarket Service Management, Fleet Management System, Aircraft Maintenance Management, Utility Asset Management, Building Asset Management, Facility Management / IWMS, Asset Investment Planning (no directory leaf).
- Likely boundary (inherited from CMMS pass): EAM = first-class asset financial/lifecycle governance over the same work-management core; CMMS = maintenance work management center of gravity.
- Unknowns: how ERP-embedded EAM (Oracle/SAP) distributes cost accounting between EAM and finance; whether depreciation is definitional; whether multi-site is definitional; whether APM/capital-planning pillars are consolidating into the Type.

## Research Questions

1. What does the asset record contain, and how are assets organized (functional/location hierarchies, parent/child)?
2. What maintenance work management does an EAM carry (work orders, PM, requests, scheduling, mobile execution)?
3. How is the whole asset lifecycle governed: acquisition/procurement, in-service cost tracking, warranty, refurbish-vs-replace, decommissioning/disposal?
4. How do asset costs work: work-order cost roll-up, TCO, maintenance cost analysis, depreciation/capitalization, integration with finance?
5. What is organization-wide / multi-site governance (hierarchies, roles, standardization across sites)?
6. What sits in adjacent pillars (APM, asset investment planning, MRO optimization) vs the EAM core?
7. How do vendors themselves articulate the EAM/CMMS/ERP/APM/ITAM seams?
8. Would older / on-premise / ERP-embedded / differently positioned products still fit the definition (historical check)?

## Representative Products

Selected for market representation + different product philosophies + different customer tiers. All Tier 2 (official product/solution pages); see Sources.

| Product | Positioning | Pole represented |
|---|---|---|
| IBM Maximo Application Suite | heritage enterprise EAM for asset-intensive industries (utilities, transport, oil & gas, government); suite of EAM + APM + AIP pillars | standalone enterprise suite, deep heritage anchor |
| Oracle Fusion Cloud Maintenance | EAM as a pillar of the ERP/SCM cloud suite; asset lifecycle + maintenance cost management + parts + project capitalization | ERP-embedded pole |
| SAP Cloud ERP — Asset Management | maintenance process as an ERP capability; functional-location/equipment asset model; maintenance cost analytics | ERP-embedded pole #2 |
| Accruent Maintenance Connection (+ EAM solution suite) | mid-market multi-site "CMMS & EAM"; FM/real-estate-rooted vendor selling separate CMMS / EAM / FAM / IWMS solutions | mid-market pole + the market's own taxonomy articulation |
| eMaint (Fluke) | convergent "Enterprise-grade CMMS and EAM software" | convergent-gradient corroboration |

Attempted but unreachable (source-access limitations, recorded):
- **Hexagon EAM (ex-Infor EAM)** — hexagon.com 403 ×2 → abandoned. The major pure-play enterprise EAM pole is therefore evidenced indirectly (Maximo heritage + vendor articulations), not by direct observation.
- **IBM Maximo documentation** (ibm.com/docs/mas) — 403; consistent with the prior CMMS pass (ibm.com/docs 403). Maximo evidence is product-page level.
- **Eptura / ManagerPlus** (SMB EAM pole) — eptura.com product URLs 404 ×2, managerplus.com transport error → abandoned.
- Carried over from the CMMS pass: Fiix and Odoo unreachable; UpKeep FAQ reachable and used there (EAM definition quote reused here as corroboration).

## Sources

Tier 2 (official product/solution pages), all fetched 2026-09-08:
- IBM Maximo Application Suite — https://www.ibm.com/products/maximo and EAM pillar page https://www.ibm.com/products/maximo/asset-management
- Oracle Fusion Cloud Maintenance — https://www.oracle.com/scm/maintenance/
- SAP Cloud ERP Asset Management — https://www.sap.com/products/erp/asset-management.html
- Accruent Maintenance Connection — https://www.accruent.com/products/maintenance-connection ; Accruent EAM solution page + FAQ — https://www.accruent.com/solutions/enterprise-asset-management-software
- eMaint — https://www.emaint.com/eam-software ("Why Enterprises Upgrade to eMaint EAM")

Corroboration from the paired CMMS pass (2026-09-07): UpKeep FAQ ("Every EAM contains a CMMS"); eMaint CMMS/EAM nav taxonomy.

---

## Product Observations

### IBM Maximo Application Suite (Tier 2 — product pages)

Evidence layer: A for statements about Maximo itself (official IBM pages); no help-center depth (docs 403).

- Root positioning: "unified asset and facilities management solution that brings maintenance, inspections and reliability together … for critical equipment and infrastructure".
- **Suite pillar structure (directly observed)**: (1) AI in asset lifecycle management; (2) **Enterprise asset management (EAM)**; (3) **Asset performance management (APM)**; (4) **Asset investment planning (AIP)**. APM and AIP are separate pillars with their own pages, not features inside EAM.
- **EAM pillar page — lifecycle span stated**: "Maximo provides **end-to-end management of assets, from procurement and maintenance to decommissioning**. This comprehensive lifecycle management ensures assets are optimized throughout their entire service life."
- EAM key capabilities (pillar page): Work Order Management ("create, assign, and track work orders"; "automate scheduling and approvals for **planned and corrective** maintenance"; "integrate **failure codes, job plans, and asset history**"); Mobile EAM ("online or offline"; "barcode and RFID scanning"); **Inventory and spare parts management** ("MRO … track parts availability, reorder points, and warehouse locations; automate replenishment; **link inventory to work orders**; multi-location; supplier integration"); customizable dashboards ("asset health, work order trends"; "automated reports on **maintenance history, costs, and compliance**").
- **Maximo Manage** = "a fully integrated EAM platform that enables your teams to go beyond time-scheduled maintenance". **EAM Add-ons**: "advanced scheduling and optimization, spatial asset visualization, **linear asset manager, calibration**, and connectors to ERP and other systems".
- **AIP pillar (capital planning)**: "connect asset condition, risk and financial impact so teams can evaluate scenarios, compare priorities and align investments to business goals, budgets"; "asset lifecycle planning".
- Asset-class deployments: real estate & facilities, renewables, IT assets, data centers — the same machinery applied to different asset populations.
- Case-study scale markers (vendor-claimed): ~60,000 assets across four power plants (VPI); 10,000 field technicians (Transport for London); infrastructure assets with 100-year lifespans (Sund & Bælt).
- Deployment/licensing: SaaS or client-managed software; AppPoints credit-based licensing.

### Oracle Fusion Cloud Maintenance (Tier 2 — product page)

Evidence layer: A for statements about Oracle Maintenance itself.

- Positioning: "Oracle Fusion Cloud Maintenance is an automated Smart Operations solution that **streamlines your enterprise asset management**."
- **Asset management block**: "Manage the **entire lifecycle** of your physical assets"; "Track any asset — whether it's **enterprise-owned or customer-owned**"; "360-degree view of asset information across your organization including **cost, maintenance history, asset meter and hierarchy, parts list, and warranty**"; "Integrate end-to-end processes across Oracle Fusion Cloud SCM, CX, and **ERP Financials**, enabling access to a **single source of truth for asset data**."
- **Maintenance planning and execution block**: preventive maintenance (forecast/schedule/monitor); condition-based maintenance (connected equipment); **work requests** ("Capture work requests to create work orders"); work order scheduling and dispatch ("real-time resource availability"; "assigning skilled technicians"); work order execution ("track material used and labor hours charged against plans, install and remove components, complete inspections"); **contracted maintenance** ("internal and external resources"; labor agreements; request services from the work order); **supplier warranty tracking** ("throughout the lifecycle … automate warranty claims"); closed-loop quality inspections.
- **Maintenance cost management block (the ERP-embedded financial machinery, directly observed)**: "Monitor and manage costs at a granular level, adjusting details by item"; "work cost monitoring — monitor material, labor, and other costs throughout the entire lifecycle of the work order"; "Multiple cost methods and representations — standard, actual, average, periodic average … **cost books**"; "Determine a **repair versus replace strategy** by analyzing work order charges and overall asset costs."
- **Parts inventory management block**: automated spare-parts replenishment; "purchase parts and services **from the work order**"; serialized/rotable item tracking; procurement/sourcing machinery.
- **Project-specific maintenance block**: "Manage maintenance by project … project striping"; "Collect project expenditures in Oracle Project Portfolio Management and **capitalize based on project rules**"; project-based billing.
- Separate **Service logistics and depot repair** product for "asset-based service" (customer-owned units) — the aftermarket side lives in a different product.
- Licensing table: role-based licensing across service agents, field technicians, depot repair technicians, parts managers — evidence that the asset/maintenance workforce is role-differentiated.

### SAP Cloud ERP — Asset Management (Tier 2 — product page)

Evidence layer: A for statements about SAP's asset management capability.

- Positioning: "Minimize downtime by establishing a **comprehensive corporate maintenance process**" — asset management presented as an ERP feature area (Finance/SCM suite page).
- **Technical asset management block**: "Onboarding assets and maintaining master data"; "Asset lifecycle management — establish **points of asset measurement to record instantaneous or counter-based values**"; "**Asset hierarchies based on time segments** … by using **functional locations and equipment**" (the classic SAP asset master model); "Engineer **reusable maintenance task lists**".
- **Demand monitoring block**: tracking/analysis of maintenance requests; "Categorize, prioritize, and react to maintenance requests based on **asset criticality, safety, compliance**"; reactive maintenance on breakdowns.
- **Planning, scheduling, dispatching block**: "maintenance order planning — define workflows for approving maintenance order execution costs and **procuring spare parts and services**"; grouped order views; "consider … resource availability, operational constraints, and priority, then assign jobs to the right workers".
- **Maintenance execution block**: "record malfunction information, document time and measurement, handle planned and unplanned goods"; technician malfunction recording and confirmations; **offline mobile** task completion.
- **Embedded asset analytics block**: "Asset breakdown analysis"; "Proactive analytical queries"; "**Maintenance cost analysis — identify the gap between planned and actual costs** by analyzing asset maintenance expenses with drill-down capabilities."

### Accruent Maintenance Connection + EAM solution suite (Tier 2 — product + solution pages + FAQ)

Evidence layer: A for statements about Accruent products; the FAQ taxonomy is vendor articulation (used as evidence of how the market frames the seams, not as ground truth).

- Product positioning: "Why Choose Maintenance Connection **CMMS & EAM**": "feature-rich, purpose-built, **multi-site** CMMS and EAM solution."
- Product capabilities: work order management; mobile-friendly CMMS ("offline capabilities and barcode & QR code scanning"); self-service reporting & analytics; security; **integrations (ArcGIS/Esri, ERP, SCADA, HR systems, EDMS, IoT; open API)**; automated notifications; **SaaS or on-premises** deployment.
- **EAM solution page — lifecycle span stated**: "An EAM solution provides a wider range of features to track, manage, and analyze **asset performance and costs through the whole asset lifecycle, from acquisition to disposal**."
- **EAM superset statement**: "A robust EAM **leverages CMMS components** to streamline maintenance … It **transcends basic maintenance** by unifying inventory, purchasing, and document control with **integrated accounting, project management, and multisite management** tools — all within a single, centralized platform."
- **Vendor-articulated EAM vs CMMS**: "The formal difference between an EAM and a CMMS is that an EAM tends to provide a wider array of features … to track, manage, and analyze asset performance throughout the asset lifecycle. This can include features like: inventory management, a purchasing management system, document and knowledge management, multi-site management tools, labor management tools, service management, an accounting system and financial management, supply chain management. **However, the lines are far more blurred in reality**, as a modern and robust CMMS also boasts these functionalities."
- **Vendor-articulated taxonomy** (product FAQ): CMMS = "managing maintenance tasks and schedules"; EAM = "managing an organization's assets **throughout their lifecycle**"; ERP = "integrates maintenance with broader business processes like finance, HR, and supply chain"; APM; FM; IoT-enabled maintenance — all named as distinct categories.
- **EAM vs ERP**: "an ERP manages all operations, while an EAM helps to improve the monitoring, operations, and maintenance of assets and work orders."
- **EAM vs ITAM**: "EAM revolves around managing an organization's **physical** assets and infrastructure … ITAM specifically deals with … **digital** assets, including hardware, software, licenses, and data."
- "How does an EAM system work" (vendor summary): centralized asset data; proactive maintenance; integrated workflows (scheduling, work orders, inspections); field mobility (GIS mapping noted); "EAM systems integrate with ERP and energy platforms".
- Suite architecture: EAM suite = Maintenance Connection (CMMS/EAM core) + RedEye/Meridian (engineering document management) + Observe (IoT remote monitoring) — the EAM brand is sold as a multi-product suite.
- Compliance depth: e-signatures, versioned procedures, audit trails (pharma/regulated framing).
- Industries: utilities, manufacturing, mining, pharma, oil & gas, food & beverage.

### eMaint / Fluke (Tier 2 — EAM page)

Evidence layer: A for statements about eMaint itself (corroboration role).

- "Enterprise-grade **CMMS and EAM software** for maintenance teams" — one product family carrying both labels; confirms the convergent gradient from the CMMS side of the market.
- Asset management framing: "Hierarchies, history, **total cost of ownership**" (nav taxonomy).
- Connected reliability: Fluke IIoT sensors trigger automated work orders (predictive maintenance) — condition-based triggering as an extension of the work-order engine.
- EAM page claims are promotional (support quality, ROI); structural content limited — used only for the dual CMMS/EAM positioning and TCO framing.

---

## Cross-product Comparison

| Structure | Maximo | Oracle Maintenance | SAP AM | Accruent MC/EAM | eMaint | Verdict |
|---|---|---|---|---|---|---|
| Identified asset register with hierarchy | ✔ ("asset and work registry"; asset classes; hierarchies implied by add-ons) | ✔ ("asset meter and hierarchy"; 360° asset view) | ✔ (functional locations + equipment, time-segmented hierarchies) | ✔ (asset tracking, centralized asset data) | ✔ ("hierarchies, history, TCO") | Universal → Core |
| Work orders bound to assets (planned + corrective), execution, history | ✔ (WO mgmt; failure codes, job plans, asset history) | ✔ (WO execution: material, labor, components, inspections) | ✔ (order planning → execution → confirmation) | ✔ (centralized WO management) | ✔ (CMMS core) | Universal → Core |
| Whole-lifecycle span articulated (acquisition/procurement → disposal/decommissioning) | ✔ ("from procurement and maintenance to decommissioning") | ✔ ("entire lifecycle"; supplier warranty; disposal via lifecycle) | ✔ (asset onboarding/master data → lifecycle mgmt) | ✔ ("from acquisition to disposal") | (TCO framing only) | Universal (4/5 direct) → Core (the "EAM delta") |
| Asset-level cost tracking / cost analysis | ✔ (reports on maintenance history, costs; AIP financial impact) | ✔ (work cost monitoring; cost books; repair-vs-replace) | ✔ (maintenance cost analysis, planned vs actual) | ✔ ("asset performance and costs"; "integrated accounting") | ✔ (TCO framing) | Universal → Core (as governance structure; implementations vary) |
| PM scheduling engine (time/meter/condition) | ✔ ("beyond time-scheduled maintenance") | ✔ (PM + condition-based) | ✔ (preventive/predictive plans; measurement points/counters) | ✔ (rule-based PM; IoT triggers) | ✔ (PM core of CMMS heritage) | Universal → Common (inherited from CMMS core, not the EAM delta) |
| Work request intake | (implied; WO-centric) | ✔ (work requests → WOs) | ✔ (demand monitoring, screening) | ✔ (service request management) | ✔ (CMMS heritage) | Common |
| MRO parts inventory tied to WOs | ✔ (dedicated capability block) | ✔ (dedicated block; purchase parts from WO) | ✔ (procure spare parts from order planning) | ✔ (inventory control) | ✔ (parts & inventory) | Universal → Common |
| Procurement/purchasing linkage | ✔ (ERP connectors) | ✔ (parts/services from WO; sourcing) | ✔ (procure spare parts and services in order planning) | ✔ ("purchasing management system" in EAM-wider list) | ✔ (connects MRO to purchasing) | Common |
| Mobile execution (offline, scan) | ✔ (Mobile EAM, offline, barcode/RFID) | (technician workbench "mobile-enabled") | ✔ (offline task completion) | ✔ (offline, barcode/QR) | ✔ (mobile app) | Common |
| Multi-site / organization hierarchy & governance | ✔ (asset classes across sites; case-study scale) | ✔ ("across your organization") | ✔ (corporate maintenance process; org hierarchy) | ✔ ("multi-site management"; purpose-built multi-site) | ✔ (multi-site & enterprise) | Common (organization-wide scope is Core; literal multi-site tooling Common) |
| Asset cost → finance integration | ✔ (ERP connectors add-on) | ✔ (ERP Financials integration; cost books) | ✔ (native, inside Cloud ERP) | ✔ (ERP integration; "integrated accounting") | ✔ (ERP integrations) | Universal → Common (mechanism varies: native vs integration) |
| Maintenance cost analytics (planned vs actual, TCO) | ✔ (dashboards/reports; AIP) | ✔ (repair-vs-replace analysis) | ✔ (dedicated analytics block) | ✔ (reporting/analytics) | ✔ (TCO framing) | Common |
| Depreciation / capitalization in-product | (not enumerated on fetched pages) | ✔ (project capitalization per project rules; cost accounting) | (fixed-asset accounting in ERP finance; not on this page) | ("integrated accounting" claimed; not detailed) | (Limble CMMS shows depreciation — CMMS-side) | **NOT definitional** — mechanism varies (in-system vs finance module); held Common/Optional |
| Capital planning / investment scenarios | ✔ (AIP pillar, separate) | (project capitalization only) | — | — | — | Optional/variant (single-product pillar) |
| APM / reliability deep analytics | ✔ (APM pillar, separate) | (Smart Operations monitoring; AI suggestions) | (breakdown analysis only) | (IoT anomaly detection) | (sensor→WO triggers) | Optional/variant; adjacent Type (reliability-management) |
| Linear / spatial / GIS assets | ✔ (linear asset manager add-on) | — | — | ✔ (Esri/ArcGIS integration) | — | Variant (industry: infrastructure) |
| Regulated-industry compliance depth | ✔ (compliance reporting) | — | — | ✔ (e-signatures, versioned procedures, audit trails) | ✔ (life sciences heritage) | Variant |
| Contracted maintenance / external labor | (case study: third-party contracts) | ✔ (contracted maintenance block) | (lean services in task lists) | (labor management tools; vendor portal) | ✔ (vendor management) | Common |
| Document management linkage | ✔ (asset data + manuals implied) | — | — | ✔ (EDMS suite; docs on WOs) | (attachments) | Optional/variant (suite packaging) |
| Condition monitoring / IIoT triggers | ✔ (CBM use case; APM) | ✔ (connected equipment) | (predictive plans) | ✔ (Observe IoT; anomaly → WO) | ✔ (Fluke sensors → WOs) | Common (as trigger), deep analytics is variant |
| Deployment: SaaS vs on-prem | ✔ (SaaS or client-managed) | ✔ (cloud) | ✔ (cloud ERP) | ✔ (SaaS or on-premises) | ✔ (cloud) | Variant |
| AI assistance | ✔ (watsonx; WO intelligence; assistant) | ✔ (AI agents, repair summaries) | (era-current) | (era-current) | ✔ (eMaint AI) | Era-common variant |

## Canonical Abstraction

### L0 — Defining Invariant (smallest stable structure)

```text
Enterprise Asset Register        (the operator's own physical asset base as identified records
│                                 in a location/functional hierarchy — the record backbone)
├── Maintenance Work Management   (work orders bound to assets — planned and corrective —
│                                 executed and closed into persistent maintenance history)
└── Whole-Life Asset Governance   (the asset managed as a long-lived, cost-bearing entity from
                                  acquisition/procurement through in-service life to
                                  decommissioning/disposal — with asset-level cost tracking and
                                  organization-wide scope as first-class structures)
```

Three jointly-held structures. Tests:

- Remove whole-life governance → maintenance work management system = **CMMS** (the sibling Type; exactly the seam the CMMS pass recorded).
- Remove work management → asset registry / fixed-asset register (record-keeping without the work engine; two other directory Types).
- Remove the register → cost accounting and work tracking with no asset backbone (generic job costing).
- The three are load-bearing jointly: the register tells the system *what* it owns; work management keeps it *in service*; whole-life governance manages *what it costs and when it ends* — and makes the results inspectable at the level of the individual asset and the whole estate.

Deliberately NOT in L0 (each fails the "remove it and it's still EAM" test):

- **Depreciation schedules / fixed-asset accounting** — mechanism varies fundamentally: ERP-embedded EAMs (Oracle/SAP pole) leave the general ledger to finance modules and integrate; standalone products may carry depreciation-like fields (Limble, a CMMS, even shows them). What is invariant is asset-level cost visibility and lifecycle governance, not where the depreciation posting happens.
- **Multi-site management tooling** — organization-wide scope is invariant ("enterprise"); literal multi-site administration is a common implementation. Single-site whole-life deployments still fit.
- **PM scheduling engine** — inherited from the CMMS core the Type contains; universally present in the sample but not the EAM delta. (CMMS pass already established PM is not even definitional for CMMS.)
- **MRO inventory, procurement, mobile apps, cloud delivery** — common mature structure; historical and minimal deployments exist without each.
- **APM / reliability analytics, capital-planning scenario machinery** — separate pillars or adjacent Types in the market itself (Maximo ships APM and AIP as distinct products).
- **IIoT/condition-based triggering, AI** — era-current additions.

### L1 — Common Mature Structure

- Preventive maintenance: recurring schedules per asset (calendar and meter/usage/condition triggers) generating work orders; reusable task lists/job plans; failure coding.
- Work request intake and screening (criticality/safety/compliance triage) feeding the work-order engine.
- MRO spare-parts inventory tied to work orders: storerooms/locations, reservations, reorder points, replenishment; parts issued to work.
- Procurement linkage: purchase parts/services from work orders; supplier and contracted-labor records; supplier warranty tracking.
- Labor and cost tracking on work orders rolling up to the asset: actual vs planned cost, maintenance cost analysis, total cost of ownership.
- Planning and scheduling surfaces: backlog, dispatch, resource availability, technician assignment.
- Mobile execution: work lists, offline capture, barcode/RFID identification, photos/measurements/confirmations.
- Organization hierarchy and governance: sites/regions, roles (planner, supervisor, technician, asset manager), audit trails.
- Analytics and reporting: asset health, downtime, backlog, PM compliance, cost reports; integrations outward to ERP/finance, procurement, sensors/SCADA, GIS, document systems.
- Multi-site estates: the same machinery deployed per asset class (plant, facilities, fleet, infrastructure) across an organization.

### L2 — Variant / Optional Structure

- **Asset performance management / reliability engineering depth** (RCM/FMEA, condition-monitoring analytics, strategy optimization) — packaged by suite vendors as separate pillars or adjacent products (Maximo APM; reliability-management directory leaf).
- **Asset investment planning / capital planning** (scenario evaluation of maintain/refurbish/replace against budgets and risk) — single-product pillar in the sample (Maximo AIP); may be an emerging boundary.
- **Linear and spatial asset management** (roads, rail, pipelines; GIS mapping; Esri integrations) — infrastructure-industry variant.
- **Regulated-industry compliance depth** (e-signatures, procedure versioning, validation, audit-grade records) — pharma/energy variant.
- **Project-based maintenance with capitalization rules** (project striping, project billing) — capital-project-heavy estates.
- **Engineering document management integration** (drawings/manuals on work orders) — suite-packaged variant.
- **Deployment postures**: cloud SaaS vs client-managed/on-premise; suite module vs standalone.
- **Industry verticals**: utilities, transport, oil & gas, mining, government infrastructure, healthcare facilities, data centers, manufacturing.
- **Customer-owned assets on the same machinery** (service/depot-repair extensions) — the aftermarket seam; maintained as a separate product/leaf.
- **AI assistance** (WO intelligence, repair summaries, conversational data access) — era-current.

### L3 — Vendor-specific (research notes only)

- **Maximo**: AppPoints credit licensing; Manage/Mobile/Visual Inspection product decomposition; add-ons (linear asset manager, calibration, spatial); APM/AIP as separate pillars; IDC/Verdantix analyst positioning; case-study metrics (60,000 assets VPI; 10,000 TfL technicians; 100-year bridge lifespans).
- **Oracle**: Smart Operations framing; "enterprise-owned or customer-owned" asset tracking in one system; cost books and multiple costing methods; role-based licensing table; Service Logistics/depot repair as sibling product; Fusion SCM/CX/ERP Financials integration fabric.
- **SAP**: functional locations + equipment with time-segmented hierarchies (the classic SAP asset master model); maintenance task lists; order-type machinery (approval workflows for execution costs); planned-vs-actual cost drill-down; GROW/RISE packaging.
- **Accruent**: Maintenance Connection as CMMS & EAM dual-branded product; EAM suite bundling (MC + RedEye/Meridian EDMS + Observe IoT); Esri integration; SaaS-or-on-premises; the market taxonomy FAQ (CMMS/EAM/ERP/APM/FM/IoT) and the "lines are far more blurred in reality" admission.
- **eMaint**: X4/X5 versions; Fluke 3563 vibration sensor → auto-WO; Accelix connected-reliability ecosystem; G2-rating marketing claims.

## Rejected Findings

- **"EAM = CMMS + an accounting ledger"** — rejected. Even ERP-embedded implementations keep general-ledger accounting in the finance module; the EAM carries asset-level cost tracking, lifecycle governance, and finance integration. Accruent lists "an accounting system" among EAM-wider features, but the observed mechanics are integration/cost-visibility, not ledger replacement.
- **"Depreciation schedules are definitional"** — rejected. Not enumerated on the EAM pages of the ERP-embedded poles; depreciation appears in lower-tier CMMS products too. Held as common implementation; the invariant is whole-life cost visibility.
- **"EAM is definitional multi-site"** — rejected as stated. Organization-wide scope is invariant; literal multi-site tooling is common structure. A single-site plant running full lifecycle governance still fits.
- **"EAM includes APM/reliability analytics"** — rejected as definitional; the market itself separates APM as a pillar/product (Maximo; Accruent taxonomy FAQ). Deep reliability is the reliability-management leaf.
- **"EAM includes asset investment planning"** — rejected as definitional (single-product pillar evidence); flagged as possible emerging boundary.
- **"EAM = ITAM"** — rejected; vendor-articulated seam (physical/infrastructure vs digital/IT estate). Maximo's "IT asset" class is an asset-class deployment of the same machinery, not evidence of type merger.
- **"EAM is a superset containing everything vendors sell"** — rejected; suite breadth (EHS, LMS, field service, safety) is packaging. The Type is the asset-lifecycle core, not the vendor's whole catalog.

## Boundary Findings

- **vs CMMS / Maintenance Management (joint-review sibling)**: **RATIFIED from this side — keep both, center-of-gravity seam.** Both vendors' own articulations match the seam recorded in the CMMS pass: EAM = the CMMS work-management core **plus whole-life asset governance as a first-class structure** ("from procurement and maintenance to decommissioning" — Maximo; "from acquisition to disposal" — Accruent; "leverages CMMS components … transcends basic maintenance" — Accruent; "Every EAM contains a CMMS" — UpKeep, CMMS pass). Both sides also record that the market is converging and vendors themselves call the lines "far more blurred in reality" (Accruent). Removal tests (both directions agreed): strip whole-life/financial governance → CMMS; strip work orders → asset registry. This is a gradient, not a wall; the canonical discriminator is whether whole-life asset cost/lifecycle governance is a defining structure or an add-on.
- **vs Enterprise Asset Registry**: registry = the record backbone alone (identity, custody, status, history). EAM = registry + work management + whole-life governance. "Remove the work orders" separates them cleanly; "remove the lifecycle governance" hands the register to CMMS.
- **vs ERP**: ERP = organization-wide transactional back office (finance, HR, supply chain); EAM = the asset/maintenance domain system. The ERP-embedded pole (Oracle Maintenance, SAP AM) realizes the same domain core as a pillar of the ERP suite — the domain objects (assets, work orders, meters, PM, maintenance costs) are identical; packaging differs. Accruent's articulation: ERP "manages all operations"; EAM "improves the monitoring, operations, and maintenance of assets and work orders."
- **vs Aftermarket Service Management**: EAM maintains the operator's OWN production/service assets; aftermarket manages SOLD units at customer sites. Oracle's page ("enterprise-owned or customer-owned") shows the machinery is shared but the customer-owned leg is sold as a separate product (Service Logistics/depot repair) — consistent with the seam recorded in the aftermarket pass.
- **vs IT Asset Management / CMDB**: physical-asset operations vs IT estate (discovery, licensing, contracts) and service-relationship configuration records. Vendor-articulated (Accruent EAM-vs-ITAM FAQ); Maximo's IT asset class is a deployment of the same machinery, not a merger.
- **vs Reliability Management**: strategy/analysis layer (RCM/FMEA, failure analysis) consuming EAM/CMMS data; packaged by suite vendors as separate pillars (Maximo APM). In-product predictive triggers are an extension, not the discipline.
- **vs Facility Management System / IWMS**: buildings/space/leases/occupancy center vs equipment/asset lifecycle machinery. Accruent sells EAM, FAM (facility asset management), and IWMS as separate solutions — the vendor's own seam.
- **vs domain-specific asset systems (Fleet Management System, Aircraft Maintenance Management, Utility Asset Management, Building Asset Management)**: domain cousins with their own regulatory/operational spines (telematics, airworthiness, network/grid assets, building systems). EAM is the general machinery; these either ride inside an EAM deployment as asset classes (Maximo asset classes include fleets, renewables, IT, data centers) or exist as separate Types when the domain spine dominates.
- **vs Asset Investment Planning** (no directory leaf): scenario/capital-planning machinery emerging as a distinct pillar inside suites (Maximo AIP). Flagged lightly; no taxonomy action.

## Historical / Market-Sample Check

- The L0 does not depend on cloud, mobile, IIoT, or AI: mainframe-era plant systems (Maximo's 1980s lineage; SAP PM since the R/3 era) and on-premise deployments still sold today (Accruent on-premises option) hold the register + work + whole-life-governance trio.
- Pre-software practice — the plant asset register, the maintenance log/planning board, and the capital budget with disposal records — satisfies the trio conceptually: a record of what the plant owns, work managed against it, and money/lifecycle tracked from purchase to scrap. The "enterprise" scope predates software as organization-wide accountability for plant and equipment.
- ERP-embedded and standalone poles both satisfy the same core; the core does not assume any packaging.
- Conclusion: the definition is not over-fitted to the current cloud/AI market.

## Uncertainties

- **No Tier 1 help-center depth for any sampled product.** Maximo docs 403 (repeated from the CMMS pass); Oracle/SAP evidence is product-page level; Accruent pages are product/solution/FAQ level. Consequently: exact asset-record field lists, exact status vocabularies and allowed transitions, and numeric limits are **not asserted** anywhere in the final document; conceptual states only.
- **Hexagon EAM (ex-Infor)** — the major pure-play enterprise EAM — was unreachable (403 ×2). The pure-play pole is evidenced indirectly (Maximo heritage + vendor articulations). Assertions that depend on pure-play packaging specifics are avoided.
- **Depreciation depth per product** was not directly verified on fetched pages for Maximo/SAP; the final document holds depreciation as a common implementation with moderate wording, not a structural claim.
- **Asset investment planning**: only one sampled product ships it as a dedicated pillar; whether it is consolidating into the EAM Type is unresolved (flagged in Boundary Findings, no taxonomy action).
- **Contracted/external labor management** evidence is strongest at Oracle/Accruent; generalized with moderate wording only.

## Final Synthesis

EAM is the operator's organization-wide system of record for its physical asset base, defined by three jointly-held structures: the enterprise asset register (identified assets in a functional/location hierarchy), maintenance work management over that register (the CMMS core it contains — work orders, planned and corrective, persistent history), and whole-life asset governance as a first-class structure (acquisition/procurement → in-service cost and condition → decommissioning/disposal, with asset-level cost tracking and organization-wide scope). Mature products add the same recognizable layer: PM engines, request intake, MRO inventory tied to work, procurement and contracted labor, cost roll-up and maintenance cost analysis, planning/dispatch surfaces, mobile execution, multi-site governance, analytics, and finance/sensor/GIS/document integrations. Variants extend toward APM/reliability depth, capital-planning scenarios, linear/spatial assets, regulated compliance, project capitalization, and industry verticals. The CMMS seam is ratified as a center-of-gravity gradient that vendors themselves acknowledge; the registry, ERP, ITAM, aftermarket, and reliability seams are each held by a single structural removal test.
