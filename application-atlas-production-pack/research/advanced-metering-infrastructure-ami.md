# Research Notes — Advanced Metering Infrastructure / AMI

Research date: 2026-09-06
Slug: `advanced-metering-infrastructure-ami`
Directory leaf: "Advanced Metering Infrastructure / AMI" (§19 Energy, Utilities & Telecommunications)

---

## Research Goal

Understand what the utility-side software behind "Advanced Metering Infrastructure" actually is and how it works: what objects exist (meters, endpoints, network devices, reads, events), what the platform does (collection, events, device/network management), who operates it, how data flows downstream, and where the boundary lies against Meter Data Management (MDMS), SCADA/ADMS, AMR, and generic IoT platforms.

Important framing decision: in the market, "AMI" is an umbrella term for meters + communication network + head-end system + (sometimes) MDM. The directory has a separate **Meter Data Management System / MDMS** leaf, so this leaf is anchored on the **metering-operations platform side** (head-end / collection / device & network management), with MDMS treated as the adjacent downstream Type.

## Initial Boundary (hypothesis before research)

- Core use: the utility-operated platform that communicates with a large deployed population of revenue meters, collects measurement data on schedules and on demand, receives meter events, and manages meters and the field-area network as managed devices.
- Likely users: utility metering/AMI operations teams; field installers (via commissioning tools); downstream consumers of the data (billing, outage management, analytics).
- Nearest neighbors: MDMS (downstream data), SCADA/ADMS/DMS (grid devices vs customer meters), Utility Field Service (install work), Customer Energy Management (consumer-facing), Industrial IoT Platform (same shape, different domain), AMR (predecessor).
- Open questions: is "AMI software" = head-end system? Is one-way AMR inside or outside the Type? How regional is the structure?

## Research Questions

1. What are the core objects? (endpoint/meter, metering point, network device/collector, read/interval data, event/alarm, device group, firmware, commissioning)
2. What does the head-end actually do? (scheduled collection, on-demand reads, event receipt, commands, firmware, network management)
3. What operational actions exist? (remote connect/disconnect, service control, demand response, prepayment, tamper/outage/leak handling)
4. How does data flow downstream (to MDM/billing/OMS)?
5. What interfaces exist (operations console, network monitoring, installer tools, consumer portal)?
6. How do commodities differ (electric / gas / water / heat)?
7. How regional is the structure (US RF mesh vs European smart metering vs Asia)?
8. Does one-way AMR fit the definition? Where is the AMR/AMI line?
9. What distinguishes an AMI head-end from a generic IIoT platform?

## Representative Products

Selected for market representation, documentation reachability, different product philosophies, different regions and commodities:

| Product | Vendor | Why selected | Commodity focus | Region |
|---|---|---|---|---|
| OpenWay / Temetra / IEE | Itron | Largest global endpoint base; explicitly separates AMI vs AMR vs MDM offerings | electric, gas, water | US-origin, global |
| GridStream / Emerge Head End Platform | Landis+Gyr | Global #1 meter vendor; HES product page with explicit feature list | electric, gas, water | Switzerland/global |
| OMNIA | Kamstrup | European DSO-oriented AMI system; turnkey/managed-service philosophy; multi-commodity incl. heat/cooling | electricity, water, heat, cooling | Denmark/EU |
| Neptune 360 + endpoints/data collectors | Neptune Technology Group | Water-specialist; shows the water variant of the same structure | water | North America |
| AclaraONE | Aclara (Hubbell) | Multi-commodity unified software platform | electric, gas, water | US |

## Sources

All fetches 2026-09-06. Tier 2 (official product pages) dominated; Tier 1 (operational manuals) mostly behind customer logins.

- Itron — Advanced Metering Infrastructure (solution page): https://na.itron.com/what-we-offer/advanced-metering-infrastructure
- Itron — Automated Meter Reading (solution page): https://na.itron.com/what-we-offer/automated-meter-reading
- Itron — Temetra (product page): https://na.itron.com/products/temetra
- Itron — Meter Data Management (solution page): https://na.itron.com/what-we-offer/meter-data-management
- Landis+Gyr — Next Gen AMI (solution page): https://www.landisgyr.com/us/en/home/solutions/next-gen-ami.html
- Landis+Gyr — Software catalog: https://www.landisgyr.com/us/en/home/software.html
- Landis+Gyr — Emerge Head End Platform (product page): https://www.landisgyr.com/us/en/home/software/emerge-head-end-platform.html
- Kamstrup — Electricity solutions: https://www.kamstrup.com/en-en/electricity-solutions
- Kamstrup — Meter reading / OMNIA: https://www.kamstrup.com/en-en/electricity-solutions/electricity-meter-reading
- Kamstrup — root: https://www.kamstrup.com/en-en
- Neptune Technology Group — root: https://www.neptunetg.com/
- Neptune — Neptune 360 (product page): https://www.neptunetg.com/products/software/software/neptune-360/
- Aclara (Hubbell) — root: https://www.aclara.com/

**Source-access limitations:**
- Aclara deep pages (AclaraONE solution page) returned 404 twice; only the vendor root was reachable. Aclara observations are therefore reduced-strength (positioning only, no feature detail).
- Wikipedia (planned Tier 3 structural grounding) timed out twice; abandoned per network rules. No external encyclopedia grounding was used.
- Vendor operational documentation (user guides for head-end consoles) is behind customer portals (Itron customer/partner login, Landis+Gyr customer login, AclaraConnect portal, MyKamstrup). Console-level UI details are therefore NOT directly observed; interface descriptions in the final document are kept at the conceptual level and calibrated accordingly.
- No precise numeric operational parameters (read intervals, endpoint limits, latency figures) are asserted anywhere; none were directly observed.

---

## Product A — Itron (OpenWay / Temetra / IEE)

### Key observations (evidence layer A unless noted)

- AMI solution page defines the stack as four composed parts: **AMI HEADEND + DISTRIBUTED MANAGEMENT + FIELD AREA NETWORKS + DI-ENABLED DEVICES**. AMI is explicitly "more than smart meters".
- Original business case framing: "automating and optimizing meter-to-cash with Advanced Metering Infrastructure (AMI) and smart meters".
- Smart electricity meters described with: "two-way communication, remote meter reading, TOU and DR applications, tamper detection, data analytics, renewable integration and consumer engagement capabilities".
- Outage direction: utility case study quote — "We had a late-night storm and Advanced Metering Infrastructure was reporting outages before customers were ever calling us" (Avista). Meter-originated outage events are a first-class AMI behavior.
- Related software: "Operations Management Software — Realize operational savings, understand the state of your system and apply corrective actions where and when needed" (AMI Operations Management, used by Dominion per case study).
- **AMR boundary evidence**: Itron maintains a separate "Automated Meter Reading" offering. AMR = walk-by/drive-by/mobile collection: "Temetra collects, optimizes and dispatches meter reading work to mobile employees, then returns collected data to supervisors"; Mobile Collection System = "drive-by data collection, including consumption and tamper data from radio-based endpoints". AMR history: "Itron has led the industry since we introduced automated meter reading in the 1980s... over 100 million gas, water and electric endpoints shipped".
- "Advanced AMR" blurs the line: CENTRON R450 meter supports "walk-by and drive-by AMR with a meter featuring remote disconnect and connect, interval data, time-of-use data, demand read and reset"; Gen5 500W ERT module adds "meter reading, high flow alarms, interval data and remote firmware download". So even mobile-collection meters can carry advanced functions; the structural difference vs AMI is the **fixed two-way network**.
- Temetra (product page): "globally adopted, cloud-based, multi-vendor, multi-commodity, meter data management solution. Temetra supports a variety of meter manufacturers and communications protocols enabling a smooth migration from AMR to AMI. Storing meter read data from a variety of sources in one location, combined with... map-based routing... several hundred meters to several million, with more than 40 million endpoints hosted globally." Note the terminology drift: Itron markets Temetra (a collection system) as "meter data management".
- MDM page (boundary evidence): MDMS = "collect, store, validate, manage and share data"; products: IEE Meter Data Management ("enterprise-wide, highly-scalable MDMS architecture"), IEE Cloud AI ("cloud-based meter data management (MDM) solution for collecting, processing, and managing AMI data at scale... foundation for billing, operations, analytics"), MV-90 xi ("collecting and processing interval data from complex metering devices"), AMI Essentials Water. Itron thus ships AMI (head-end/network) and MDMS (validation/billing-grade data) as **separate product lines**.
- Distributed Intelligence: "DI applications can be downloaded from the Itron Enterprise Application Center to devices in the field" — device-software distribution over the AMI network (edge apps).
- Scale markers (vendor-claimed, not independently verified): 310M+ communicating endpoints delivered; 124M+ endpoints under management; 200M+ communication modules deployed.

## Product B — Landis+Gyr (Gridstream / Emerge)

### Key observations

- Next Gen AMI solution page: AMI's role is to "sense, validate, and convert energy usage into accurate and timely bills for their customers" — meter-to-cash framing; now extended "beyond the initial business case of gathering consumption data and automating billing".
- Unified portfolio across "electric, gas, and water"; anchored by "Gridstream® Connect, Landis+Gyr's flexible, scalable IoT platform".
- Smart Gas: "smart retrofit gas modules that enable two-way AMI communications and remote meter operations"; ultrasonic platform with "autonomous safety shutoff for overpressure, temperature, and excess-flow conditions".
- Smart Water: "retrofit communication modules add smart functionality to existing water meters without requiring meter replacement, capturing consumption data and securely transmitting it to support capabilities such as leak detection, reverse-flow monitoring, and anti-theft alerts".
- Smart Electric: meters as "intelligent grid sensors that unlock advanced applications such as prepayment, load disaggregation, and demand management directly at the point of delivery".
- **Emerge Head End Platform** (the HES product): "state-of-the-art head end system (HES) for managing the network and devices". Features: "reliable communications whether using a wired, wireless, cellular, or a hybrid approach"; "remote metering and real-time monitoring through **bidirectional communication with every device on the network**"; "supports a network of connected devices from **multiple manufacturers and in various generations of technology**"; "comprehensive data for actionable insights"; "state-of-the-art security at multiple levels to protect data when collected, during transit, and while in storage". Deployment: "Cloud, SaaS, On-premises, or Hosted". Benefits include "accurate billing", "regulatory compliance", "back-office integrations".
- Software catalog shows the AMI-adjacent module structure as separate products: **MDMS** ("finely tuned database repository that stores customer and meter metadata... usage and diagnostic data"), **TechStudio** ("commissioning, testing, and modification capability for RF network devices, including street light controllers, electric meters, gas/water modules, and line sensors, all from a single software platform"), **Smart Community Center** (street-light CMS on the same network), **IoT Gateway** ("Secure Integration Between Distribution Devices, SCADA Networks..."), **MDUS – SAP for Utilities Adapter** ("integrates your Advanced Metering Infrastructure with daily processes like billing, contract management and customer service"), **SmartData for Outage Management**, **Consumer Engagement**.
- TEPCO case study: "world's largest utility IoT network—collecting 1.4+ billion data points daily" (vendor-claimed).
- Shared-network case: water utility and electric utility "leveraging AMI infrastructure" together (City of Neenah Water Utility + WE Energies) — one AMI network serving multiple utilities.

## Product C — Kamstrup (OMNIA)

### Key observations

- OMNIA definition (best single-sentence definition found in the sample): "Kamstrup OMNIA® is a modular, scalable next-generation AMI system that supports **all the tasks involved in remote reading of smart meters and daily management of your meter data and communication network**."
- OMNIA page: "OMNIA® smart grid platform – a modular, scalable next-generation AMI system"; "OMNIA® Express is a cloud-based standard package that lets you try out the system quickly with a minimal investment... always possible to expand the solution" (SaaS entry tier).
- Communication technology as a choice: "Our OMNIA® smart metering system gives you the choice between **RF mesh and cellular IoT technologies** – and allows you to switch to cellular when the need arises."
- Security: "defence-in-depth strategy... State-of-the-art AES 128-bit encryption covers all communication within and between AMI components" (vendor-claimed); ISO 27001 mentioned.
- Managed/turnkey posture: "We get our hands dirty every day hosting and operating our own smart metering systems for a number of our utility customers"; services include "several models for AMI deployment, cloud-based 'as a Service'-packages and day-to-day support".
- Multi-commodity breadth beyond electric/gas/water: heat and cooling solutions (district energy), submetering; "collecting high-density data from its heat, cooling, water, and electricity meters" (Axel Towers case).
- Cases: Radius (Danish DSO) turnkey replacement of "approximately 1 million mechanical meters"; Göteborg Energi "Turnkey AMI project with OMNIA® 6 suite"; Lephalale (South Africa) "smart prepaid meters... curb meter tampering, prevent electricity theft" (prepayment variant).
- Grid Management Services: "detailed picture of the entire power grid's condition, enabling power supplies to validate, optimize, and invest" — analytics layered on meter data.

## Product D — Neptune Technology Group (Neptune 360)

### Key observations

- Product structure for water AMI: Water Meters / Registers / **Endpoints** / **Data Collectors** / Software — the endpoint + collector + software layering is explicit in the catalog.
- "Neptune works with your utility to build an adaptable AMI system that fits your needs and protects your investments with full compatibility"; "thousands of utility customers across North America save time, labor, water, and money through our innovative **AMR and AMI Systems**" — AMR and AMI coexist as offerings.
- Neptune 360: "meter data management platform... From **mobile meter reading to an AMI network**, your utility and consumer data is all in one place, without the burden of maintaining IT infrastructure"; "quickly identify potential **leaks, excessive consumption, and reverse flow**"; cloud-based, browser-accessed, "Monitored 24/7 from a world-class data center"; SOC badge shown.
- Neptune 360 Mobile application: "direct communication via wireless network from the field to the office. Upload data on-demand" — field-side surface.
- My360 Consumer Portal: consumers "monitor their own water consumption 24/7" — consumer-facing extension.
- ENZO AI assistant for help content (vendor-specific add-on).
- White paper listed: "Leading-edge security for AMI and AMR Systems" — security treated as spanning both.

## Product E — Aclara (Hubbell) — reduced strength (root page only)

### Key observations

- AclaraONE® positioned as "Software Utility Solutions"; homepage banner: "The AclaraONE Advantage: Enhanced Meter Data Management and Monitoring is Here... Unlock total network visibility with our Enhanced AclaraONE platform."
- Product categories: Utility Measurement Systems (Smart Meters), Sensors and Controls (Demand Response, Grid Monitoring, Leak Detection, Lighting Control), Utility Communications (Metrum Cellular, RF Networks, **Software**, TWACS PLC).
- Markets: Electric / Gas / Water / Combo utilities — multi-commodity.
- "Harness your automated metering infrastructure (AMI) technologies and edge intelligence applications to run your distribution operations more efficiently and reliably."
- No feature-level detail was reachable (deep pages 404). Treat all Aclara-specific claims as positioning-level only.

---

## Cross-product Comparison

| Dimension | Itron | Landis+Gyr | Kamstrup | Neptune | Aclara | Evidence |
|---|---|---|---|---|---|---|
| Head-end/HES as the software core | Yes ("AMI HEADEND" component) | Yes (Emerge, "head end system (HES)") | Yes (OMNIA "AMI system") | Yes (Neptune 360 platform over endpoints/collectors) | Yes (AclaraONE platform) | B |
| Managed population of identified endpoints | Yes (endpoints/modules) | Yes ("every device on the network") | Yes (smart meters) | Yes (endpoints) | Yes | B |
| Fixed field-area network (collectors/routers) | Yes ("FIELD AREA NETWORKS") | Yes (RF network devices; wired/wireless/cellular/hybrid) | Yes (RF mesh or cellular IoT) | Yes (Data Collectors product line) | Yes (RF Networks, cellular, PLC) | B |
| Scheduled + on-demand remote collection | Yes (interval data; demand read; Temetra) | Yes ("remote metering and real-time monitoring") | Yes ("remote reading of smart meters") | Yes (mobile reading → AMI; on-demand upload) | Positioning only | B |
| Meter-originated events/status | Yes (outage reporting, tamper detection, high-flow alarms) | Yes (leak/reverse-flow/anti-theft alerts; safety shutoff) | Yes (tamper/prepaid theft cases; grid condition) | Yes (leaks, excessive consumption, reverse flow) | Yes (leak detection category) | B |
| Two-way command to devices | Yes (remote disconnect/connect; DI app download) | Yes ("bidirectional communication"; "remote meter operations") | Yes (implied by AMI system + prepaid) | Yes (implied by AMI system) | Positioning only | B |
| Device/network management (commissioning, firmware, multi-vendor) | Yes (Temetra multi-vendor; DI apps to field) | Yes (Emerge multi-manufacturer/multi-generation; TechStudio commissioning) | Yes (network management in OMNIA scope) | Yes (collectors as products; adaptable system) | Positioning only | B |
| Downstream integration (billing/CIS/MDM) | Yes (IEE/IEE Cloud as separate MDMS line) | Yes (MDMS product; MDUS SAP adapter for billing) | Yes (meter data daily management; analytics) | Yes (data to utility systems; consumer portal) | Yes (AclaraONE incl. MDM positioning) | B |
| Outage/leak operational use | Yes (outage reporting before customer calls) | Yes (SmartData for Outage Management) | Yes (grid condition services) | Yes (leak identification) | Yes (fault/outage management positioning) | B |
| Consumer-facing portal | Yes (customer experience line) | Yes (Consumer Engagement) | Not observed on fetched pages | Yes (My360) | Not observed | B (partial) |
| Deployment options | Cloud (Temetra/IEE Cloud) | Cloud/SaaS/On-prem/Hosted (Emerge) | SaaS (OMNIA Express), turnkey, vendor-hosted | Cloud SaaS (Neptune 360) | Not observed | B |
| Commodity breadth | electric, gas, water | electric, gas, water | electricity, water, heat, cooling, submetering | water only | electric, gas, water | B |
| AMR coexistence/migration | Yes (Temetra "migration from AMR to AMI"; separate AMR line) | Not observed on fetched pages | Not observed | Yes ("AMR and AMI Systems") | Not observed | A/B (partial) |
| Prepayment | Not observed on fetched pages | Yes (smart electric applications) | Yes (Lephalale case) | n/a (water) | Not observed | A (2 products) |

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

The utility-side platform is recognizable as AMI software only with all of:

1. **Utility-operated platform** — operated by the utility (or its turnkey delegate), not by the metered customer.
2. **Managed population of identified metering endpoints** — revenue meters / communication modules held as individually identified, addressable device records at scale (hundreds to millions).
3. **Fixed field-area communication network** — a dedicated network (RF mesh, PLC, cellular, hybrid) between the platform and the endpoints, with intermediate network devices (collectors/routers) as part of the managed estate. This excludes mobile walk-by/drive-by collection (AMR).
4. **Remote collection of measurement data** — scheduled (interval/profile) and on-demand reads of consumption/measurement data.
5. **Meter-originated status/events** — the return path: alarms and status from endpoints (outage, tamper, leak/reverse-flow, high-flow, fault indicators) surfaced to the utility.

§24 historical check: one-way mobile AMR (walk-by/drive-by) fails #3 and is a separate offering at every vendor that ships both — correctly outside. One-way fixed-network collection (early fixed-network AMR) fails #5; the market does not call it AMI. European smart metering (Kamstrup/OMNIA), Japanese-scale deployments (TEPCO/L+G), and water-only AMI (Neptune) all satisfy the five properties, so the definition is not over-fitted to the North-American RF-mesh pattern. "Advanced" is an era/marketing label (same pattern as ADMS), not a structural test.

### L1 — Common Mature Structure

- **Device lifecycle management** — commissioning/registration of endpoints, device status monitoring, firmware/software distribution to field devices (Itron DI apps; Gen5 remote firmware download; TechStudio commissioning).
- **Remote service control** — remote connect/disconnect (electric and gas), service switching.
- **Network management** — collectors/routers/repeaters as managed devices; network health/topology/communication-quality monitoring; multi-technology and multi-vendor support.
- **Demand-side applications** — time-of-use data, demand response/load control, load management.
- **Operational consoles** — device explorer, event/alarm queues, read-status monitoring, reports; corrective-action workflows (Itron Operations Management).
- **Downstream integration** — export of reads/events to MDM/CIS/billing (SAP adapter at L+G; IEE at Itron), and to outage management (AMI pings for outage confirmation, per ADMS research notes).
- **Security posture** — encryption of data in transit/at rest, defense-in-depth, security certification (Kamstrup AES-128/ISO 27001; L+G multi-level security; Neptune SOC).
- **Field/installer surfaces** — walk-by programmers, commissioning/testing tools, mobile apps (Itron Mobile Radio; TechStudio; Neptune 360 Mobile).

### L2 — Variant / Optional Structure

- **Commodity** — electric (outage/tamper/TOU/DR), gas (safety shutoff, high-flow), water (leak, reverse-flow, excessive consumption), heat/cooling (district energy), submetering.
- **Communication technology** — RF mesh vs PLC (PRIME/G3-class) vs cellular IoT vs hybrid; proprietary vs standards-based; switchable (Kamstrup RF-mesh↔cellular).
- **Deployment & service model** — on-premises HES, cloud/SaaS, vendor-hosted/turnkey (Kamstrup hosting; Radius/Göteborg turnkey), managed services.
- **Regional/regulatory regime** — European DSO smart-metering rollouts, North-American investor-owned/co-op utilities, prepaid markets (South Africa), shared networks across utilities (Neenah/WE Energies).
- **Migration posture** — AMR→AMI coexistence and migration tooling (Temetra; Neptune AMR+AMI).
- **Scale tier** — from several hundred meters (Temetra small utilities) to millions (TEPCO; Radius ~1M).
- **Consumer engagement** — consumer portals (My360; Consumer Engagement) as optional extensions.
- **Edge intelligence** — distributed-intelligence apps executed on the meters themselves (Itron DI; L+G edge apps ecosystem) as an emerging layer.

### L3 — Vendor-specific (research notes only)

- Itron: OpenWay, Riva, CENTRON R450, Gen5 500W ERT, Temetra, IEE / IEE Cloud AI, MV-90 xi, AMI Essentials Water, Distributed Intelligence apps, Enterprise Application Center, Gen6 network, CityEdge.
- Landis+Gyr: Gridstream Connect, Emerge, TechStudio, SmartData, Smart Community Center, IoT Gateway, MDUS (SAP adapter), Revelo, Surent G480, SPAN Edge, OATI-powered DERMS.
- Kamstrup: OMNIA / OMNIA Express, Grid Management Services, Power/Heat Intelligence, Return Temperature Optimizer (RTO), Metering Cloud posture.
- Neptune: Neptune 360, My360, ENZO AI assistant, R900-family endpoints, 360 ORBCON? (not verified), data collector lines.
- Aclara: AclaraONE, Metrum Cellular, TWACS PLC, Enhanced AclaraONE.

## Vendor-specific Findings (do not generalize)

- Itron's Distributed Intelligence (apps downloaded to meters, executed at the edge) is a specific architecture; other vendors express edge intelligence differently (L+G app ecosystem). Treat "edge apps on meters" as an emerging variant, not core.
- Kamstrup's turnkey/hosted operating model (vendor runs the AMI system for the DSO) is a business-model variant; Itron/L+G also offer managed services but the sampled evidence is strongest at Kamstrup.
- Landis+Gyr's MDUS SAP adapter is a specific ERP-integration product; downstream integration is common, the SAP-specific adapter is not.
- Neptune's ENZO AI assistant is vendor-specific.
- Itron's Temetra is marketed as "meter data management" while functioning as multi-vendor collection — terminology drift, see Rejected Findings.

## Rejected Findings

- **"AMI = smart meters"** — rejected. Every vendor frames AMI as head-end + network + devices; Itron explicitly says "More than smart meters".
- **"AMI software includes VEE/billing-grade data management"** — rejected as defining. VEE/validation belongs to MDMS (Itron ships IEE separately; L+G ships MDMS separately). Some products blur the line (Temetra, Neptune 360 marketed as "meter data management platform"), which is terminology drift, not structure.
- **"AMI requires RF mesh"** — rejected. Kamstrup offers RF mesh *or* cellular; L+G Emerge lists wired/wireless/cellular/hybrid; Aclara ships PLC (TWACS) and cellular (Metrum). Technology is L2.
- **"AMI is electric-only"** — rejected. Gas modules (L+G, Itron), water (Neptune, all), heat/cooling (Kamstrup).
- **"AMI includes consumer portals by definition"** — rejected; portals are optional extensions (absent from some fetched product pages).
- **"AMI = generic IIoT platform"** — rejected. Same shape, but AMI is defined by revenue-metering semantics (billing-grade measurement, metrology, commodity events, regulatory context). Vendors themselves call their platforms "utility IoT" only as positioning (TEPCO case), while the operational structure remains metering-specific.

## Boundary Findings

**vs Meter Data Management System / MDMS (sibling §19).** The structural test: the head-end's central object is the **communicating device** (collect data from it, command it, monitor it, upgrade it); the MDMS's central object is the **billing-quality data record** (validate, estimate, edit, store, share). Evidence: Itron ships OpenWay (AMI) and IEE (MDMS) as separate lines; L+G ships Emerge (HES) and MDMS as separate products; Itron's MDM page defines MDMS as "collect, store, validate, manage and share". Test: remove device/network communication and management → an MDMS remains; remove validation/billing-grade storage → a head-end remains. **Terminology drift**: Temetra (collection) and Neptune 360 (collection+analysis) are both marketed as "meter data management" — flagged for joint review when MDMS is processed.

**vs SCADA / ADMS / DMS (§16/§19).** AMI manages **customer revenue meters** at massive scale with scheduled interval data; SCADA/ADMS manages **grid primary equipment** (feeders, transformers, switches) with real-time telemetry and control on a connected network model. They integrate: the ADMS research notes show OMS consuming "AMI requests (meter ping, load-side status, voltage reading)" for outage confirmation. Test: remove the revenue-metering population → SCADA remains; remove the grid-device model/control → AMI remains.

**vs Automated Meter Reading (AMR) — no dedicated leaf in the directory.** AMR = mobile (walk-by/drive-by) or early one-way collection; Itron and Neptune ship AMR and AMI as distinct offerings, and Temetra's stated purpose is "migration from AMR to AMI". "Advanced AMR" (drive-by meters with remote disconnect) blurs the edge case. The structural test is the **fixed two-way field-area network**. No directory conflict exists; recorded as an observation.

**vs Utility Field Service Management (§19).** AMI commissioning involves device installation/registration, but the management object is the **device estate**, not the workforce/crew schedule. No crew dispatch, no work-order lifecycle as primary structure observed in the sampled AMI pages.

**vs Customer Energy Management (§19).** Consumer portals (My360, Consumer Engagement) are optional extensions of AMI data; the consumer-facing usage/insight application is a different Type with the consumer as operator.

**vs Industrial IoT Platform (§13).** Same abstract shape (devices → network → platform → data → apps). AMI is distinguished by revenue-metering domain semantics: billing-grade measurement, metrology and commodity-specific events (outage/tamper/leak), utility field-area networks, and regulatory billing context. A generic IIoT platform lacks the metering object model; AMI vendors calling themselves "utility IoT" (TEPCO/L+G, Itron IIoT) is positioning, not identity.

**Naming.** "Advanced" is a market-era label (two-way fixed network vs one-way/mobile AMR), parallel to the "Advanced" in ADMS. In European usage the same structure is often called "smart metering" (Kamstrup: "smart metering solutions"; OMNIA described as AMI system). One Type; no rename proposed.

## Uncertainties

1. Console-level UI details (exact pages, queues, workflows inside head-end consoles) were not directly observed — operational manuals are behind customer portals. Interface descriptions are kept conceptual.
2. AclaraONE feature detail unreachable (404s); Aclara evidence is positioning-level only.
3. Exact read-schedule semantics (default intervals, read success-rate targets) not observed; deliberately not asserted.
4. Whether install/swap "service orders" are a standard head-end object could not be confirmed from fetched pages (TechStudio confirms commissioning/testing; order management not confirmed). Kept out of the final document.
5. Prepayment evidence spans two products (L+G feature list, Kamstrup case) but both are single-mentions; kept as variant, not common.
6. Wikipedia grounding failed (timeouts); no third-party structural reference was used — all structure claims rest on the five vendor sources.

## Final Synthesis

Advanced Metering Infrastructure software is the utility-operated platform — in practice the **head-end system** plus its managed network and endpoint estate — that maintains a fixed two-way field-area network over a large population of identified revenue meters, collects measurement data on schedules and on demand, receives meter-originated events and status, and manages the devices and the network themselves (commissioning, firmware, service control, communication health). Its purpose is meter-to-cash: converting metered consumption into accurate, timely billing, and extending meter data into outage response, loss/theft/leak detection, demand-side programs, and grid analytics. Mature products add device lifecycle management, network management, demand-side applications, operational consoles, security, and downstream integration to MDM/CIS/billing and outage management. Commodity (electric/gas/water/heat), communication technology, deployment model (on-prem/SaaS/turnkey), regional regime, and AMR-migration posture are variants. The defining core is deliberately small and era-robust: utility-operated platform + identified endpoint population + fixed field-area network + scheduled/on-demand collection + meter-originated events.
