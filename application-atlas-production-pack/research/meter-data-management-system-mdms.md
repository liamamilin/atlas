# Research Notes — Meter Data Management System / MDMS

## Research Goal

Understand what a utility-side Meter Data Management System (MDMS) actually is and how it works: what objects exist inside it (measurements, initial vs final data, VEE rules/exceptions, service points, devices, usage/bill determinants), what the system does (ingest, validate/estimate/edit, store, calculate usage, publish), who operates it, how data flows in from head-ends and out to billing/settlement/portals, and where the boundary sits — especially against the sibling **Advanced Metering Infrastructure / AMI** leaf (whose pass flagged a joint review), **Utility Billing / CIS**, **Industrial Historian** (whose pass flagged this leaf as nearest sibling), and **Energy Scheduling & Settlement**.

Prior-pass obligations discharged in this pass:

1. **AMI pass joint-review flag** (STATUS.md Boundary Issues): "the head-end centers on the communicating device estate (collect/command/monitor/manage) while MDMS centers on billing-quality data records (validate/estimate/edit/store/share); Itron ships OpenWay (AMI) and IEE (MDMS) as separate product lines and Landis+Gyr ships Emerge (HES) and MDMS as separate products — but terminology drifts: Temetra (collection) and Neptune 360 (collection+analysis) are both marketed as 'meter data management' — flagged for joint review when MDMS is processed."
2. **Industrial Historian pass forward flag**: "structurally the nearest sibling — a time-stamped measurement archive — but with meter-domain validation/estimation (VEE) and billing consumption replacing plant acquisition/analysis; that pass should position its core against this Type explicitly."
3. Consistency with **energy-scheduling-settlement** ("vs MDM (enterprise record vs settlement determinant)") and **gas-utility-management** ("vs MDMS/AMI (meter exists to produce bills)" — from the CIS side the meter exists to produce bills; from the MDMS side the data record is the object).

## Initial Boundary

In industry usage, "meter data management" is a contested term: meter vendors market collection platforms (Itron Temetra, Neptune 360) as "meter data management", while the same vendors also ship separate, structurally different MDMS products (Itron IEE, Landis+Gyr MDMS). Enterprise vendors (Oracle) ship MDMS as a standalone system that consumes from any head-end. This pass anchors the leaf on the **billing-quality data system of record** (the IEE / L+G MDMS / Oracle MDM product category), treating collection platforms as AMI-side products and the terminology drift as a naming phenomenon to be documented, not a Type merger.

Nearest neighbors: AMI/head-end (upstream device estate), Utility Billing/CIS (downstream money), Industrial Historian (structural analog in plant domain), Energy Scheduling & Settlement (market money), Utility Revenue Assurance (consumer of the data), Customer Energy Management (consumer-facing surface), Data Warehouse/Analytics (ungoverned consumers).

## Research Questions

1. What is the central data object, and what lifecycle does it have (raw → validated → final → usage)?
2. What exactly is VEE in each product — validation, estimation, editing, exceptions, audit?
3. What does the system hold as its registry (meters, service points, devices, install events)?
4. How does data reach consuming systems (billing determinants, extracts, subscriptions, portals, settlement)?
5. What interfaces do the humans use (exception queues, rule configuration, data explorer)?
6. What rules govern the data (pre/post values, condition codes, severity gates, re-billing, retention)?
7. Where is the AMI/head-end boundary, really — and what explains the terminology drift?
8. Historical/regional check: pre-AMI interval-data processing, deregulated-market MDMs, CIS-embedded validation — do they fit the same core?

## Representative Products

| Product | Vendor | Pole | Why chosen |
|---|---|---|---|
| IEE Meter Data Management (IEE MDM / IEE Cloud) | Itron | meter-vendor MDMS, global multi-commodity, largest installed base | market leader; explicitly separate from OpenWay (AMI) and Temetra (collection) |
| Meter Data Management System (MDMS) | Landis+Gyr | meter-vendor MDMS #2, separate product from Emerge HES | second meter-vendor philosophy; rich feature list incl. VEE engines + billing extracts |
| Oracle Utilities Meter Data Management | Oracle | enterprise-software MDMS, hardware-agnostic, largest utilities | full public user guide (Tier 1); proves MDMS without any device estate of its own |

Boundary-adjacent evidence (not representative samples): Itron Temetra + MV-90 xi (collection/interval processing marketed near the MDM name), Neptune 360 (water collection+analysis marketed as "meter data management platform", per AMI pass), Kamstrup OMNIA (AMI system bundling "daily management of your meter data" — no separate MDMS product line), Oracle Smart Grid Gateway (head-end adapters shipped as a separate product).

## Sources

Fetched 2026-09-09 (all Layer A unless noted):

- Itron — Meter Data Management solution page: https://na.itron.com/what-we-offer/meter-data-management
- Itron — IEE MDM product page: https://na.itron.com/products/itron-enterprise-edition-meter-data-management
- Landis+Gyr — Software catalog: https://www.landisgyr.com/us/en/home/software.html
- Landis+Gyr — MDMS product page: https://www.landisgyr.com/us/en/home/software/meter-data-management-system.html
- Oracle — Utilities Meter Data Management product page: https://www.oracle.com/utilities/meter-data-management/
- Oracle — MDM documentation library: https://docs.oracle.com/en/industries/energy-water/meter-data-management
- Oracle — MDM Business User Guide: Functional Overview, Glossary of Terms, About Initial Measurement Data, About VEE, About Usage Calculation (URLs in source list below)
- Kamstrup — Electricity solutions (boundary evidence): https://www.kamstrup.com/en-en/electricity-solutions
- AMI pass research notes (sibling evidence): research/advanced-metering-infrastructure-ami.md

Fetch failures (recorded per source-access limitation): Siemens EnergyIP MDM (two 404s on guessed URLs — abandoned), Honeywell Smart Energy (transport error), Xylem/Sensus (403), DuckDuckGo search (timeout), Landis+Gyr MDMS product-sheet PDF (binary, unparseable), Oracle docs first URL (timeout; succeeded on retry via docs root). Oracle evidence is therefore the deepest (Tier 1 user guide); Itron and Landis+Gyr evidence is product-page level (Tier 1–2); no vendor operational manuals (customer-portal-gated) were reachable for any product.

## Product A — Itron IEE Meter Data Management

### Key observations (Layer A, product-page level)

- Solution page defines the category: "meter data management systems (MDMS) that **collect, store, validate, manage and share data**"; positioning: "Provide actionable insights to all your stakeholders—**consumers, third parties, regulators** and more".
- IEE MDM: "an industry-leading data management solution for **residential gas, water, and electric meters, commercial & industrial (C&I) meters, and Internet of Things (IoT) sensors**"; for large IOUs "a highly scalable enterprise application that **centralizes the collection, processing, storage, and complex analysis of smart device data, device events, and alarms**".
- Tier packaging: **IEE Essentials** for municipal/cooperative market ("focused capabilities... without sacrificing features"); **IEE Cloud** ("cloud-based meter data management (MDM) solution for collecting, processing, and managing AMI data at scale... foundation for **billing, operations, analytics**, and grid modernization").
- **IEE MDM Settlements**: "imports, validates, and stores interval readings data collected from metering devices to provide accurate energy market settlements for utilities. The IEE MDM Settlements module can be a **standalone or an add-on module** to IEE MDM." → settlement is a module, not the core.
- Scale claims (vendor positioning, not verified): "over 100 customers across six continents, with more than 50 million meters in production"; MDM page: "112M+ endpoints under management".
- **MV-90 xi** (separate product): "collecting and processing interval data from complex metering devices... ensures data integrity and process consistency" → the pre-AMI interval-data processing lineage still shipped as its own product.
- **Temetra** (separate product, collection): marketed as "meter data management solution" but described as multi-vendor collection + storage of reads (terminology drift; see Boundary Findings).
- Itron ships AMI (OpenWay), AMR, collection (Temetra/MV-90), and MDMS (IEE) as **separate product lines**.

## Product B — Landis+Gyr Meter Data Management System (MDMS)

### Key observations (Layer A, product-page level)

- "MDMS is a finely tuned **database repository that stores customer and meter metadata**. In addition, the usage and diagnostic data provides the foundation for the analytics and business processes within the MDMS and SmartData Applications."
- "standards-based system designed to rigorously **process and prepare data** for a variety of utility programs and operations, **according to customer-specified rules**. This single, unified system **consolidates metering, consumption, and related data from all read sources, into a centralized system-of-record repository**."
- Feature list (verbatim structure):
  - **Data Collection & Synchronization**: "Standards-based interfaces enable data to be consumed by the MDMS from smart meter systems or smart grid devices" → ingestion from external systems, not device operation.
  - **VEE Engines**: "Powerful analytic engines capable of processing hundreds of millions of **register and interval reads**".
  - **Exception Management**: "The workflows within the MDMS focus on efficient exception management and the **remediation of events related to the VEE process**".
  - **Billing Extracts**: "provides **cleansed, framed billing determinants for each rate structure** to the utility CIS and/or Billing applications **on the billing cycle days**".
  - **Analytics & Reports**: "current and valid data is correlated using embedded business logic".
  - **Virtual & Net Metering**: "flexibility to create both **virtual meters and virtual channels**".
  - **Distribution Network & Power Quality**: "maintains the network connectivity model"; benefits mention storing "non-billing data such as voltage and amperage".
- Benefits: "**VEE analytics ensure bill quality**"; "maximizing billing efficiency and accuracy".
- Landis+Gyr ships **Emerge** (head end) and **MDMS** as separate software products; MDUS–SAP adapter sold separately for billing integration.

## Product C — Oracle Utilities Meter Data Management

### Key observations (Layer A, user-guide level — deepest evidence)

Functional Overview lists the crucial business processes (verbatim):

1. "Defining meters, meter configurations, **service points**, and meter installations"
2. "Loading of meter readings and interval data from a **head-end system or other source**"
3. "Automatic **validation, editing, and estimation** of measurement data"
4. "Robust **editing** capabilities for readings and interval data"
5. "Calculation and publishing of **bill determinants** and other data from measurement data for use in external down-stream systems such as **billing, pricing**, etc."

Object model (Functional Overview + Glossary, Layer A):

- **Device** = "A physical meter, communication module, or some other device out in the field"; **Device Configuration** = "which types of data should be measured"; **Measuring Component** = "A logical container for measurement data... often channels for physical devices but can also be aggregators, weather data" (e.g., one device may have kWh-interval, kWh-scalar, and voltage-interval components).
- **Service Point** = "A location at which a company supplies service"; **Install Event** = "An instance of a specific device installed at a Service Point. This also includes a record of any time the service was turned on or off."
- **Initial Measurement Data (IMD)** = "The data measured on a device... stored in this initial record while it's being processed"; scalar components carry a single reading, interval components carry one reading per interval.
- **VEE** = "The process by which initial measurement data is validated, estimated (if necessary) and edited (if necessary) based on a set of user-defined rules." About VEE: "VEE acts as a **multi-layered filtration system** for IMDs. Raw data is received from the Head End as Initial Measurement Data and **only clean, validated data is received on the other end in the Measurement table**."
- **Measurement** = "This is the **final, validated** measurement information from a device. Measurement data is used in calculation of usage as part of the Usage Transaction process."
- **Usage Subscription** = "A record of an **ongoing request to send one or more Service Points' usage to one or more external systems (such as a billing application)**"; **Usage Transaction** = "A record of bill determinant calculations"; **Bill Determinants** = "Measurement data summarized for use by a billing application... TOU-mapped interval consumption, scalar consumption, scalar readings, and/or interval consumption".
- VEE machinery: **VEE Groups** (sequenced rule sets, per source role: Initial Load / Manual Override / Estimation / Projection), **VEE Rules** (validation/estimation/decision logic, base package + custom), **VEE Exceptions** with three severities (Info / Issue / Terminate; any Issue after all rules → IMD transitions to **Exception state**; Terminate stops VEE immediately), **eligibility criteria** (conditional rule application, e.g., only for kWh, only in first six months after installation).
- Data-quality semantics: **Pre-VEE vs Post-VEE quantities** both retained ("initial measurement data records contain both the original (Pre VEE) and final (Post VEE) versions"); **condition codes** travel with values ("Regular", "Missing", "External Estimated", "System Estimated"); "a measurement that was missing in the Pre VEE document will likely become 'System Estimated' in the Post VEE document once VEE has been executed."
- Exceptions persist: "exceptions are not deleted when an initial measurement is adjusted or corrected... the exceptions persist in a closed state for reporting purposes."
- Usage calculation: rules/groups with the same exception machinery; "The calculation period for bill determinant calculations can span many days... The Service Points linked to the Usage Subscription can change... The Device Configurations installed at the Service Point can change (due to device reconfigurations and **meter exchanges**)" → determinants computed across changing devices.
- Publication: "Oracle Utilities Meter Data Management can **calculate and publish usage** calculated from measurement data to **service providers** on an ongoing basis. In addition, **external systems can request usage** whenever needed."
- Standard/optional areas: Device Events, Communications (tracking remote commands against head-end systems), Aggregations, Master Data Sync (from CIS/asset systems), **Outage Storm Mode** ("detect widespread outages and **suppress estimation** for those meters until normal communication resumes"), Service Order Management (connects/disconnects/on-demand reads via head end), Market Settlement, Service Issue Monitors, Dashboards, **Information Lifecycle Management** ("prepare data for archiving or purging after a defined period").
- Product page (Tier 2): "Robust validation, estimation, and editing (VEE)... sophisticated prebuilt VEE and usage calculations for all meter types"; "Smart Grid Gateway includes **productized smart meter adapters for the most widely used head-end systems**" → head-end adapters are a separate product; "hardware-agnostic"; "pre-integration with both Oracle Utilities CIS and a rich third-party CIS integration architecture"; ILM: "configurable business rules to define data archive eligibility". Vendor scale claims (positioning): "more than 64 million meters in production", "processing more than 642 million meter reads per hour".
- The Business User Guide covers MDM together with Smart Grid Gateway, Market Settlements Management, and Meter Solution Cloud Service — the suite decomposition confirms MDM ≠ head-end ≠ settlement.

## Cross-product Comparison

| Dimension | Itron IEE | Landis+Gyr MDMS | Oracle MDM | Layer |
|---|---|---|---|---|
| Category definition | "collect, store, validate, manage and share data" | "centralized system-of-record repository" consolidating "data from all read sources" | "handling large volumes of meter data"; load → VEE → publish determinants | B |
| Central data object | smart device data (reads/events/alarms) | register + interval reads, usage + diagnostic data | IMD → Measurement (final validated), scalar + interval | B |
| VEE | "validate" in category definition; IEE processes/validates | named **VEE Engines**; "VEE analytics ensure bill quality"; exception-management workflows | full VEE machinery: groups/rules/exceptions/severities/eligibility | B |
| Registry | meters (residential + C&I + IoT sensors) | "customer and meter metadata" | Device / Device Configuration / Measuring Component / Service Point / Install Event | B |
| Billing hand-off | "foundation for billing"; Settlements module | "cleansed, framed **billing determinants** for each rate structure to the utility CIS... on the billing cycle days" | "calculate and publish usage... bill determinants" to external systems on request/ongoing | B |
| Head-end relationship | separate AMI line (OpenWay); IEE consumes AMI data | separate HES (Emerge); MDMS consumes "from smart meter systems" | consumes "from a head-end system or other source"; adapters = separate Smart Grid Gateway product | B |
| Exception work | device events and alarms surfaced | "exception management and the remediation of events related to the VEE process" | VEE/Usage exceptions → To Do entries → analyst queues | B |
| Estimation | implied by "validate" + Settlements "validates" | inside VEE engines | explicit: Estimation VEE rules, condition codes "System Estimated", periodic estimation | A (Oracle) / B |
| Audit trail | not stated at page level | not stated at page level | Pre-VEE/Post-VEE retained; exceptions persist closed | A (single product — held as standard-mature, not definitional) |
| Settlement | IEE MDM Settlements (standalone or add-on) | not on page | Market Settlements Management (separate product); Settlement chapter in shared guide | B (optional module) |
| Virtual/aggregated metering | not stated | virtual meters + virtual channels | Aggregations; measuring components as aggregators | B (optional) |
| Non-billing data | device events, alarms | voltage/amperage, network connectivity model | voltage-interval measuring components; device events | B |
| Outage interaction | not stated | not stated | Outage Storm Mode (suppress estimation) | A (single product — optional) |
| Remote commands / service orders | device events/alarms only at page level | not stated | Service Order Management, remote connect/disconnect/on-demand reads via head end | A (single product — optional) |
| Deployment | on-prem + IEE Cloud | not stated (product sheet unreachable) | on-premises + SaaS (Meter Solution Cloud Service) | B (variant) |
| Commodity | electric, gas, water, C&I, IoT sensors | multi-commodity implied (utility programs) | water, gas, electric | B (variant breadth) |
| Customer tiers | IOU (IEE) vs municipal/co-op (IEE Essentials) | utility programs, NA/LATAM/Brazil/APAC | "supports the largest utilities in the world" | B (variant) |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

The MDMS is the utility's **system of record for billing-quality meter data**. Its defining core is exactly three jointly-held structures:

1. **The measurement record of record** — persistent, individually identified consumption records (scalar readings and interval data) bound to identified metering points (meters / measuring components at service points), accumulated over years as the utility's authoritative measurement history. Remove → a pass-through pipeline or telemetry store; nothing accumulates as the record.
2. **The VEE quality machinery** — systematic validation, estimation, and editing that converts raw collected data into billing-grade (revenue-grade) data: rules flag failures, missing data is estimated and *marked* as estimated, exceptions are routed to people for resolution, and original vs final values are distinguishable. Remove → a passive archive with no quality guarantee; the data is not billing-grade.
3. **The billing-grade delivery loop** — usage/bill determinants computed from the validated record and published to consuming systems (billing/CIS, settlement, portals, third parties) on an ongoing or on-request basis, with corrected data reflowing to consumers. Remove → a quality-controlled archive with no revenue loop; the "management" is gone.

Jointly-held load-bearing:

- 1 alone = data warehouse / archive
- 2 without 1 = a VEE filter with no memory
- 3 without 1+2 = a billing interface with no data behind it
- 1+2 without 3 = quality-controlled archive that never reaches revenue
- 1+3 without 2 = pass-through store feeding billing unvalidated data
- 2+3 without 1 = ephemeral processing, no record of what was billed on

### L1 — Common Mature Structure

- **Metering-point registry** — devices, device configurations, measuring components (channels), service points, install events; master-data sync from CIS/asset systems. (The *binding* of measurements to identified metering points is L0 leg 1; the full registry machinery is L1.)
- **Exception work queues** — VEE/usage exceptions routed to analysts as work items with severity, resolution, and closed-state retention for reporting.
- **Manual edit / override** — user-created or user-corrected measurements under governed rules (a distinct source role with its own rule set).
- **Consumption sync / profiling** — keeping scalar and interval data consistent; applying interval shapes to scalar measurements.
- **Aggregation / virtual metering** — aggregated measurements, virtual meters/channels for complex billing situations.
- **Analytics & reports** — VEE-process monitoring, billing-exception KPIs, dashboards.
- **Information lifecycle management** — rule-driven archiving/purging of the very large measurement store.
- **Non-billing measurement channels** — voltage, amperage, power-quality and diagnostic data stored alongside consumption.
- **Integration spine** — standards-based inbound interfaces (head-ends, files, manual) and outbound interfaces (CIS/billing, settlement, portals).

### L2 — Variant / Optional Structure

- **Commodity breadth** — electric-only market MDMs vs multi-commodity (electric/gas/water/heat) platforms.
- **Settlement modules** — market-settlement calculation as add-on or standalone (IEE MDM Settlements; Oracle Market Settlements Management as separate product).
- **Remote device interaction** — service orders, remote connect/disconnect, on-demand reads, meter pings executed *via* the head end (Oracle carries this; not claimed on L+G/Itron MDMS pages) — structurally AMI-adjacent.
- **Outage interaction** — storm mode suppressing estimation during widespread outages (Oracle).
- **Deployment** — on-premises vs cloud/SaaS vs vendor-operated.
- **Customer-tier packaging** — enterprise edition vs essentials edition for municipal/cooperative utilities.
- **Market-regime roles** — deregulated-market data-aggregation/settlement-quality roles vs vertically integrated utility.
- **CIS-embedded packaging** — the same functions (validation, estimation, determinant delivery) shipped as modules inside a CIS/billing product rather than as a standalone system.

### L3 — Vendor-specific Structure (research notes only)

- Oracle: IMD business objects with Legacy vs Direct measurement processing; VEE Group Matrix via factors; To Do routing by message category; Usage Subscription Market Participants; Sub Usage Subscriptions (third-party billing); interval price sets; 360-degree search; Machine Learning Anomaly Scoring; CSV upload; IMD Control Staging Portal.
- Landis+Gyr: SmartData Applications family consuming MDMS data; MDUS–SAP adapter.
- Itron: IEE Essentials tiering; IEE Cloud AI; MV-90 xi lineage; IEE Application Center / distributed-intelligence apps.
- Vendor scale claims (112M+ endpoints, 64M meters, 642M reads/hour, 50M meters in production) — positioning numbers, not verified facts; not asserted in the final document.

## Vendor-specific Findings / Rejected Findings

- **"MDMS = collection"** — REJECTED as the Type definition. Collection platforms (Temetra, Neptune 360) are marketed as "meter data management", but the same vendors ship structurally separate MDMS products; the standalone MDMS category (IEE, L+G MDMS, Oracle MDM) is defined by VEE + billing-grade record + determinant delivery, not by device collection. Terminology drift documented, not ratified.
- **"The word 'collect' in Itron's MDMS definition proves MDMS collects from devices"** — REJECTED as a boundary eraser. In context, IEE "centralizes the collection, processing, storage" of data *from sources* (head-ends, imports, manual entry); Oracle's process list says "Loading of meter readings and interval data from a head-end system or other source". Ingestion at the system boundary ≠ operating the field-area network.
- **"VEE is optional"** — REJECTED. All three sampled products carry VEE as the named quality machinery (Itron "validate"; L+G "VEE Engines"; Oracle full VEE object model). A store without VEE is an archive, not an MDMS.
- **"Usage/bill-determinant calculation belongs to billing, not MDMS"** — REJECTED for the standalone Type. All three products compute determinants (L+G "framed billing determinants for each rate structure"; Oracle usage calculation as a core process; Itron "foundation for billing"). The CIS *requests and consumes* determinants; the MDMS *computes and publishes* them. (CIS-embedded determinant logic exists as a packaging variant — see L2.)
- **"MDMS includes settlement"** — held as optional module only (IEE MDM Settlements standalone-or-add-on; Oracle MSM separate product).

## Boundary Findings

### 1. vs Advanced Metering Infrastructure / AMI (head-end) — JOINT REVIEW DISCHARGED, keep-both RATIFIED

The AMI pass's structural test holds from this side with stronger evidence:

- The head-end's central object is the **communicating device**; the MDMS's central object is the **billing-quality data record**.
- Product decomposition: Itron ships OpenWay (AMI) vs IEE (MDMS) as separate lines; Landis+Gyr ships Emerge (HES) vs MDMS as separate products; Oracle ships Smart Grid Gateway (head-end adapters) as a separate product from MDM — Oracle MDM's own docs describe loading data "from a head-end system or other source" and never operating a network.
- Removal test: remove device communication/management from the pair → an MDMS remains (Oracle MDM is exactly this). Remove VEE/billing-grade storage → a head-end remains.
- **Terminology drift explained, not merged**: Temetra (multi-vendor collection) and Neptune 360 (water collection+analysis) are marketed as "meter data management" because they store and present reads; neither carries the standalone MDMS structure (VEE machinery + determinant delivery to CIS). Kamstrup ships no separate MDMS at all — OMNIA (AMI) bundles "daily management of your meter data", showing the *functions* can be packaged inside an AMI system for vertical deployments. Packaging variance across the market does not dissolve the product-category boundary that Itron, Landis+Gyr, and Oracle all maintain in their own catalogs.
- No directory change; the AMI pass's Boundary Issues entry is discharged.

### 2. vs Utility Billing / CIS

- CIS holds accounts, tariffs, invoices, payments — money. MDMS holds the measurement record — data. Oracle's glossary is explicit: Bill Determinants are "measurement data summarized **for use by** a billing application"; a Usage Subscription is "an ongoing request **to send**... usage to one or more external systems (such as a billing application)". The CIS is a *consumer* of MDMS output.
- The gas-utility-management pass held "meter exists to produce bills" for the CIS side; from the MDMS side, the bill is the *purpose* but the *record* is the object — the two Types meet at the determinant hand-off.
- CIS-embedded validation/estimation (common in smaller utilities) is a packaging variant of these functions, not a refutation of the standalone Type.

### 3. vs Industrial Historian (forward flag DISCHARGED)

- Both are time-stamped measurement archives — structurally nearest siblings, as the historian pass anticipated.
- Seam held on source + semantics + consumer: the historian ingests control-system process tags for plant analysis; the MDMS ingests revenue-meter data, runs meter-domain VEE, and serves revenue/settlement consumers. The MDMS's quality machinery (estimation marked as estimated, exceptions gated before finalization, determinants per rate structure) has no historian counterpart; the historian's high-density plant acquisition has no MDMS counterpart.
- Keep-both ratified; no directory change.

### 4. vs Energy Scheduling & Settlement

- Consistent with that pass's holding ("enterprise record vs settlement determinant"): settlement systems consume validated meter data as one input among market submissions and statements; the MDMS is the enterprise record those determinants are computed from. Settlement modules inside MDMS products (IEE MDM Settlements) are optional packaging.

### 5. vs Data Warehouse / Analytics Platform

- Analytics consumes the MDMS record; the MDMS is the governed, quality-gated record of record. Analytics modules inside MDMS products (L+G SmartData, Oracle Analytics, IEE analytics) do not dissolve the Type — without VEE + determinant delivery the remainder is a warehouse, not an MDMS.

### 6. vs Utility Revenue Assurance / Customer Energy Management

- Revenue assurance consumes MDMS data to find losses; customer energy management surfaces consumption to the consumer. Both are downstream consumers, not the record.

## Uncertainties

- **Landis+Gyr MDMS depth**: evidence is product-page level; the product-sheet PDF was unparseable and operational manuals are portal-gated. Estimation/audit details for L+G are inferred from the VEE-engine naming, not observed directly — held at B-layer strength.
- **Itron IEE operational detail**: product pages name the category and modules but do not expose VEE object detail; IEE's VEE machinery is asserted from the category definition ("validate") plus Settlements ("imports, validates, and stores") — B-layer.
- **Market-operator MDMs** (ERCOT-style, UK MOP/DA roles): not directly sampled (no reachable official documentation in this pass); the settlement-quality variant is held at reasoning level from the settlement-module evidence, not asserted as observed.
- **Retention periods**: regulatory retention lengths for interval data are commonly discussed in the industry but no sampled source stated a number; no precise retention claim is made.
- **Pre-AMI historical products**: MV-90 xi (still shipped, described as interval collection/processing with data integrity) is the closest reachable historical anchor; older standalone MDM generations were not directly documented — the historical check is therefore partly reasoning-level (recorded below).

## Historical / Market-Sample Check

- **Pre-AMI interval-data era (1990s–2000s)**: large C&I interval meters required collection + validation + estimation + determinant delivery before AMI existed; Itron still ships MV-90 xi for exactly this ("collecting and processing interval data from complex metering devices... ensures data integrity"). The three-leg core (record + VEE + determinants) describes that generation without AMI-era machinery. PASSES.
- **Deregulated-market MDMs**: settlement-quality meter data roles in restructured markets carry the same core with a market-facing consumer set; consistent with IEE MDM Settlements working "standalone". Held at reasoning level (see Uncertainties). PASSES with qualification.
- **CIS-embedded validation**: smaller utilities historically ran reading validation inside the billing system. The *functions* fit the core; the *packaging* (no standalone system) is a variant. The Type is defined by the structure, not the standalone packaging. PASSES as packaging variant.
- **Manual-reading-only utilities**: monthly route reads with billing-side validation approximate leg 1+3 with minimal leg 2; this is the thin end of the CIS-embedded variant, not a counterexample to the standalone Type.
- The definition does not depend on AMI, cloud, multi-commodity breadth, or any current-era implementation pattern.

## Final Synthesis

The MDMS is the utility's system of record for billing-quality meter data. Raw reads arrive from head-ends and other sources as initial measurement data; VEE machinery validates, estimates, and edits them into final, billing-grade measurements whose original and final values remain distinguishable; the validated record accumulates for years as the authoritative measurement history; usage/bill determinants are computed from it and published to the consuming systems — billing/CIS on billing-cycle days, settlement, portals, third parties — with corrections reflowing as re-billing. The head-end device estate is upstream input; the CIS is downstream money; analytics and portals are downstream consumers. The market's terminology drift (collection platforms marketed as "meter data management") is a naming phenomenon; the product category the vendors themselves separate (IEE vs OpenWay/Temetra, MDMS vs Emerge, MDM vs Smart Grid Gateway) is the Type documented here.
