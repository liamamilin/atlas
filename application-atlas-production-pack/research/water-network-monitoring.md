# Research Notes — Water Network Monitoring

## Research Goal

Understand what "Water Network Monitoring" is as an Application Type: what system a drinking-water utility runs to watch its distribution/transmission network — what objects live inside it (measurements, zones, events, water-loss accounting), what work flows through it (detection → investigation → field response → closure), who uses it, and where its boundaries lie against the processed horizontal utility family (GIS, asset, field service, AMI/MDMS, revenue assurance), the processed industrial-control siblings (SCADA, industrial-historian), the processed §19 siblings (OMS, gas/wastewater verticals), and the unprocessed water siblings (water-utility-management, water-quality-management, environmental-water-monitoring).

## Initial Boundary

The leaf sits in DIRECTORY §19 between Water Utility Management and Water Quality Management. Neighbors:

- Horizontal §19 family (all processed): utility-gis (network model of record), utility-asset-management (plant register), utility-field-service-management (crews/work orders), AMI + MDMS (metering estate + billing-grade data), utility-revenue-assurance (loss-control discipline over the meter-to-cash chain).
- Industrial-control siblings (§16, processed): SCADA (supervisory control over field units via point database), industrial-historian (process-measurement archive).
- Processed §19 siblings: outage-management-system-oms (electric outage response — structural analog), gas-utility-management and wastewater-utility-management (customer-service business systems of record — different object world).
- Unprocessed siblings: water-utility-management, water-quality-management (§19), environmental-water-monitoring (§21 — its 2026-09-08 run FAILED rc=143, still unprocessed).
- Name collision watch: §14 "Network Monitoring" is IT/data-network monitoring — a different domain entirely.

Prior seams inherited:

1. **utility-revenue-assurance (§19, processed 2026-09-10)** — forward seam: "water-utility-management + water-network-monitoring (this leaf claims ONLY the apparent/commercial half of water loss per the IWA/AWWA water balance — real losses [leakage] stay with network monitoring; honor this split when those leaves are processed)." This pass must discharge it from the water side.
2. **wastewater-utility-management (§19, processed 2026-09-10)** — observation: "§19 has Water Network Monitoring but no sewer/collection-network leaf; the collection estate is currently absorbed by the horizontal asset family + CCTV specialists."
3. **wastewater-compliance-management (§21, processed 2026-09-10)** — naming-collision watch on "water quality management" (label used for discharger-side compliance products and other senses); relevant to the unprocessed water-quality-management sibling.
4. **utility-gis / utility-asset-management passes** — sourcing limitation carried forward: Autodesk/Innovyze and Bentley water-network products unreachable (403/404 in prior passes).

## Research Questions

1. What does a water utility actually watch on its distribution network (pressure, flow, level, quality), and how is the watched object organized (points, zones/DMAs, assets)?
2. What data does the system ingest (SCADA, telemetry units, pressure/flow/level/quality sensors, acoustic loggers, smart meters/AMI, hydraulic models, GIS, customer calls)?
3. What does leak/burst detection actually consist of in products (learned-behavior anomaly detection, night-flow/water-balance analysis, acoustic correlation, threshold alarms)?
4. What is the event lifecycle (detection → validation/prioritization → investigation → field response → verification/closure), and where does field execution happen (native vs work-order integration)?
5. How is water loss handled — night flow, DMA water balance, NRW/ILI KPIs, regulatory leakage targets — and where is the real-vs-apparent-loss line?
6. What interfaces do operators actually use (map, event list, DMA view, dashboards, trends, reports)?
7. Where are the boundaries vs SCADA (control), GIS (network model of record), asset/field family (plant + crews), AMI/MDMS (metering), revenue assurance (apparent losses), OMS (outage analog), water-quality-management (quality program)?
8. Would older / regional / differently-positioned products still fit the definition (paper-era district night-flow charts + sounding surveys)?

## Representative Products

Sampled across the poles the market realizes (5 poles, different product philosophies and tiers):

| Product | Pole | Tier | Evidence |
|---|---|---|---|
| TaKaDu | pure-play SaaS Central Event Management (analytics-led) | global utilities (13+ countries) | official site fetched (solution page, Tier 1) + press releases |
| SUEZ — AQUADVANCED Water Networks | operator-owned digital suite (hydraulic/quality/pressure modules) | enterprise / local authorities, global | official product pages fetched (Tier 1) + brochure PDF |
| Xylem Vue (powered by GoAigua) | conglomerate platform (vendor-agnostic data integration + modular apps) | enterprise, global | official pages via search snippets (direct fetch 403) — snippet-level |
| Ovarro | device-led specialist (acoustic loggers + telemetry + analytics + managed service) | UK/global water utilities | official product/case pages fetched (Tier 1) + case-study PDFs |
| i2O Water | control-led pressure management (monitoring + PRV/pump optimization) | mid-tier utilities, global | official solution pages fetched (Tier 1) + support portal |

Rejected/abandoned: Autodesk/Innovyze Info360 and Bentley OpenFlows WaterOPS (engineering/hydraulic-modeling pole — 403/404 in prior passes per research/utility-gis.md and research/utility-asset-management.md; not retried per network rule; held as representative-but-unreachable), Badger Meter BEACON (metering-analytics pole — belongs to the AMI/MDMS seam, already documented from those passes), Gutermann/Aquarius Spectrum/Syrinix (acoustic detection specialists — appear in-sample as TaKaDu integration partners, sufficient for the substrate-variant evidence), Asterra (satellite leak detection — cited via SUEZ's satellite-diagnostics description instead).

## Sources

- TaKaDu: https://www.takadu.com/solution/ (fetched 2026-09-10), https://www.takadu.com/about-us , press releases via PRNewswire (Central Highlands Water 2019, Jyväskylä Energy 2018), waterfm.com Aquarius partnership article, en.gutermann-water.com partnership note
- SUEZ: https://www.suez.com/en/water/water-conservation/water-networks/aquadvanced/water-networks (fetched 2026-09-10), https://www.suez.com/en/water/water-conservation/water-networks/aquadvanced , https://www.suez.com/en/water/water-conservation/water-networks , UK page http://suez.com/en/uk/water-network-management/real-time-management-and-optimisation/real-time-water-networks-management (search snippet), brochure PDF https://www.suez.com/-/media/suez-global/files/publication-docs/pdf-english/advanced_solutions_for_water_networks.pdf , AQUADVANCED Quality Monitoring press (suez-asia.com)
- Xylem Vue: https://www.xylem.com/en-us/brand/xylem-vue , https://www.xylem.com/en-us/brand/xylem-vue/platform , https://www.xylem.com/en-us/brand/xylem-vue/platform/drinking-water , https://www.xylem.com/en-us/campaigns/vue/real-time-water-network-monitoring (all 403 on direct fetch; content via official-page search snippets)
- Ovarro: https://ovarro.com/en/global/home , Enigma product pages (…/enigma/enigma , …/enigma-hyq), Enigma brochure PDF (ovarro.com/content-media), Yorkshire Water smart-network trial news page, Southern Water LeakNavigator case (swan-forum.com PDF), https://ovarro.com/en/global/sectors/water
- i2O Water: https://en.i2owater.com/solutions , https://en.i2owater.com/solutions/advanced-pressure-management , https://en.i2owater.com/i2o-launches-control-logger , support portal https://support.i2owater.com/hc/en-gb , WaterWorld oNet launch article, wateronline.com eNet article
- Ownership note: i2O Water acquired by Mueller Water Products (~$20M, 2026-06 per Seeking Alpha/Tracxn), assets subsequently acquired by GWF (watermagazine.co.uk 2026-06); support portal references Mueller's Sentryx platform.

Research date: 2026-09-10.

## Product Observations

### TaKaDu — Central Event Management (pure-play SaaS pole) — evidence layer A

- Positioning: "Central Event Management (CEM) for water utilities" — "a single cloud-based software solution that leverages all your data sources such as flow, pressure, level meters, consumers' digital meters, water quality, and more. Monitor your network automatically, 24X7."
- Detection: "advanced statistical techniques and machine learning to detect and manage failures, such as leaks, early in their evolution, often when no other indications are available." Detection "works automatically, 24/7."
- Common detected events: "leaks, water breach between adjacent zones, pressure deviations, pressure reducing valve (PRV) failure, water quality (turbidity, chlorine, PH), broken meters, meter communication failures, reservoir level deviations, and negative supply."
- Leak-detection process (vendor's own four steps): (1) real-time data integrated — "SCADA data, meters & sensors"; (2) "learns the supply behavior — cleanses data, employs machine learning to create predictions, intelligently fills in short data gaps"; (3) "detects anomalies — compares the real-time data pattern with historic data and network prediction patterns; identifies trends (slow-developing leaks)"; (4) "event life-cycle management — all on one platform… When an anomaly is significant, the system immediately declares it an 'event' (typically within 1 hour)."
- Event management: "For each event, TaKaDu provides all the information your personnel need to efficiently manage the entire event lifecycle, prioritize actions, communicate with others in the organization, track progress of the operational activity in the field, and verify the repair." Event views show "magnitude, water loss, cost, and information from other systems… constantly updated insight into repair status until the leak is resolved."
- DMA monitoring: "Area View with a hierarchical list of all DMAs, ordered according to predefined key performance indicators (KPIs)… scores for Infrastructure Leakage Index (ILI), data quality, data availability, water loss, and more."
- Management dashboard: "high-level visibility into KPIs such as data availability, response time to events, water loss, nightline, data quality score." Reports: "drill down to investigate specific issues such as meters that don't transmit the expected amount of data, DMA quality, nightline."
- **SCADA boundary (vendor's own statement)**: "SCADA and CEM are complementary systems required in any smart water network. While SCADA systems provide rich data and enable monitoring and control of remote assets in real time, TaKaDu offers advanced data analysis tools, with a decision support process for managing events. As an analytics-based event detection and management system, CEM leverages the SCADA data… While having a SCADA system is ideal, with or without SCADA, you are well-positioned to benefit from CEM."
- Integration: "integrate with almost any sensors and devices, monitoring systems and IT solutions. Examples of pre-validated integrations include IBM Maximo, ABB Ability Symphony Plus SCADA, Aquarius Spectrum monitoring solution, Gutermann, Syrinix solutions." Press: "TaKaDu acts as the central management layer for all network events detected by its own data analytics engine and other external alerting systems (e.g. acoustic loggers, customer calls, sensor alerts). TaKaDu is integrated with other IT systems (e.g. work order, CRM, call centre and asset management)."
- Multi-source corroboration rationale: "When an alert generated by one system is complemented by insights from other systems, operators can be confident the alert is real, and set the appropriate priority."
- Partnership evidence for substrate variants: Gutermann ("acoustic sensor network with TaKaDu's big data analytics and event management"), Aquarius Spectrum ("two independent indications about the same problem in the same area, one from TaKaDu and one from Aquarius… operational teams can validate, track, prioritize and resolve events").

### SUEZ — AQUADVANCED Water Networks (operator-owned suite pole) — evidence layer A

- Positioning: "A water management software to improve the performance of drinking water networks… Real-time supervision of your drinking water networks… allows you to fully supervise your network in real time, alerts you in the event of an incident (water leak, microbiological risks, etc.) and informs you of its location."
- Mechanism: "The installation of sensors throughout your network, the analysis of data on flows, pressure and water quality."
- Module structure: the **"hydraulic" module** "forms the basis of the offer. It offers a hypervision of the network's operation, with the calculation of business indicators (nighttime flow, daily volume, network performance) and events based on hydraulic data (sectorisation, flows, volumes, pressures, etc.). It allows you to monitor and analyse the performance of your drinking water network, and detects events and leaks in real time, as well as their location." Two optional modules: **"Quality"** ("monitors the quality of the water, detects anomalies (taste problems, red water, coloured water, etc.)") and **"Pressure"** ("analyses the pressure stages and detects anomalies (pressure drifts, water hammer, overpressure waves, etc.)").
- Data integration: "an open data platform ready to be connected to all existing data sources (GIS, SCADA, AMI, LIMS, CRM…)". UK page: "collects data from a variety of sources, including sensors, supervisory control and data acquisition (SCADA) systems, historical database, hydraulic models, remote reading systems."
- Deployment: "software ecosystem is also marketed in SaaS mode"; modular ("You can choose any of our existing modules (hydraulics, pressure, quality…) and add as many features as needed: from monitoring and data processing to a digital twin that will help you predict risks, interventions and potential investments").
- Case-study evidence (vendor-published): Macau Water (NRW "from 18% to less than 10%"; "158 events detected in the first two years, 92% of which revealed anomalies"); Milan ("integrated digital twin that has helped to sectorise the only existing sector into 10 virtual sectors and 287 virtual sub-sectors"; "Generate events and identify risks through data mining and missing data modelling"); Versailles ("94 events were detected, 80% of which revealed an anomaly, as verified by the network operator"; "Detection of an increase in bacteria and a decrease in chlorine residual"); SEAAL Algiers (NRW 45.3% → 42.2%).
- Suite context: AQUADVANCED range spans Water Networks (drinking-water distribution), Water Supply (plants/pumps), Urban Drainage (wastewater network), Well Watch (boreholes), Quality Monitoring (network water quality). The wastewater twin (Urban Drainage) is a separate product in the same suite — evidence for the no-sewer-leaf taxonomy observation.
- Brochure: "AQUADVANCED control tool handles all key dimensions of water network management. It continuously monitors and improves network performance in real time, through: General view of network performance with a user-friendly dashboard; Event management to rapidly detect anomalies and identify risks of failure; Reporting and in-depth analysis of water network performance." Also "Integrates Customer Relationship Management and workforce management systems."
- Adjacent detection services sold by the same vendor: continuous acoustic diagnostics ("permanent acoustic pre-locators"), "digital bullets circulating in the networks", satellite diagnostics ("algorithms that compare different photos taken by satellites"), PIPEboard (corrosion/particle-emission indices) — the monitoring software "analysis and visualisation of the data reported by the sensors and by all the technologies implemented is carried out within the Aquadvanced water networks software."

### Xylem Vue (conglomerate platform pole) — evidence layer A- (snippet-level; direct fetch 403)

- Platform: "a secure, integrated, and vendor-agnostic software and analytics platform that can capture data from any source (sensors, SCADA, assets, business systems, etc.), including legacy solutions, creating a single, unified source of information." "Supports over 120 protocols/systems." Architecture: "1. Data sources: vendor-agnostic data integration (IoT sensors, ERP, dataloggers, GIS, SCADA, AMI/AMR…) 2. Smart Water Engine: single data model standardizing all data 3. Modular applications 4. Operational intelligence: real-time monitoring and actions on key indicators."
- Drinking-water applications (official page): Unified Network Management ("Process automation… advanced real-time algorithms based on sensor variables"), Plant Management, **Leak Detection** ("using integrated data analytics from SCADA, AMI/AMR, flow, pressure, acoustic sensors, and pressure transient monitoring devices"), Real-Time What-If Scenarios ("a real-time connected hydraulic model with what-if scenario simulation"), Meter Data Analytics ("AMI/AMR data visualization… customer leak detection algorithms"), Meter Asset Management, Pipe Planner ("optimized asset replacement plans using a risk-based approach").
- NRW framing: "Reduce non-revenue water — Detect and identify water losses through leak detection and visualization of key indicators, including DMAs and virtual DMAs."
- Network digital twin: "Network Real-Time Decision Support uses hydroinformatics to calibrate and optimize your existing hydraulic model. This enables the creation of a network digital twin which can visualize operating conditions, even in areas where there are no sensors… operators can manage and correct drinking water distribution in real-time, with a clear understanding of water age, pressure and plant mix."
- Case study (vendor-published): Hot Springs (US utility) — "Xylem Vue's Leak Detection application was deployed along with Xylem's digital solutions (Sensus Analytics, Revenue Locator, and Water Loss Management), the Sensus Flexnet communication network, and Sensus meters."

### Ovarro (device-led specialist pole) — evidence layer A

- Portfolio: "Remote Telemetry Units (Kingfisher), Acoustic Microphones, Data Loggers & Leak Noise Loggers, Flow Meters, Analytics, Telemetry, Managed Services" for water and other sectors.
- Enigma loggers (leak noise loggers/correlators): "deployed at multiple positions, typically on valves or hydrants… The loggers record the actual leak sound. When retrieved the leak sound is transferred to the host software where it is processed to display all leak positions between loggers." Night-time operation: "Night-time recording avoids interference from consumers' daytime water usage." "Three sound samples separate leakage from genuine water use." Enigma3hyQ: hydrophone sensor, "pinpoints leaks remotely in large diameter plastic or metal pipes, over long distances"; "data is fed into Ovarro's cloud-based analytics platform, PrimeWeb." "Having loggers distributed throughout the network and listening in at different points makes it possible to measure the time taken for noise to reach different loggers, making for greater accuracy in pinpointing leaks."
- Managed-service model: Southern Water "LeakNavigator, the UK's first fully-managed fixed network leakage service… integrates Enigma acoustic loggers, the LeakInsight analytics platform, and expert analysis. Ovarro planned logger networks, supported installations, and analyzed data to identify leaks, generating actionable points of interest (POIs)." ~1,650 loggers across 40 DMAs; "technicians began to find more leaks, much faster"; "Up to July 2024, a total of 1,170 leaks and 66 burst mains had been found." Analyst "reassessed each DMA and set specific individual filters using the LeakInsight software."
- Yorkshire Water smart-network trial: Enigma3hyQ loggers + "sensors, digital water meters, advanced analytics and telecommunications channels… presented in a single visualisation platform" — the logger data is one input among many.
- Significance: the detection substrate (acoustic loggers) can be the product's center of gravity, with the software layer (PrimeWeb/LeakInsight) organizing logger networks, correlations, DMA filters, and POIs for leakage technicians. Field execution stays with the utility's technicians.

### i2O Water (control-led pressure-management pole) — evidence layer A

- Solutions: "Advanced Pressure Management, Network Analytics, Event Management and Data Logging."
- Advanced Pressure Management (oNet): "remotely control and automatically optimise pressure across the entire network – at PRVs and pumping stations – to minimise water loss… i2O algorithms determine the optimal control philosophy for PRVs and pumps to achieve your target pressure at the critical point." "The first water management system that allows utilities to remotely control and automatically optimise both pressure reducing valves (PRVs) and variable-speed drive pumps via a single interface."
- Network Analytics (iNet): "brings together network-relevant data to maximise actionable insight in one place"; Control Logger "typically… used at the entry to a zone on a PRV to measure upstream, downstream and control space pressures and record flow"; "accurate and timely reporting on PRV condition as part of i2O's iNet network monitoring and analytics solution"; "Logs enhanced statistics for transient detection"; "A full set of alarm functions on all data channels"; "No need for an i2O logger at the critical point because our platform can ingest data from other manufacturer's loggers."
- Event Management (eNet): "an incident management system tailored to the needs of water utilities. It can be used for bursts, sewer overflows, water quality events, security breaches, and health & safety incidents" (powered by Badger Software's CLIO).
- Support portal (Tier 1): sections "dNet, iNet and oNet platform software", "Alarms — Displaying alarms by status", "Loggers — Deploying a Logger 17"; also "Logging on to Sentryx Intelligent Network" (Mueller platform reference post-acquisition).
- Significance: the control-inclusive edge of the Type — pressure control as a leak-reduction strategy. Monitoring semantics (zones, PRV condition, transients, alarms) are the same object world; control is the differentiating variant.

## Cross-product Comparison

| Structure | TaKaDu | SUEZ AWN | Xylem Vue | Ovarro | i2O |
|---|---|---|---|---|---|
| Live network condition (pressure/flow/level, bound to network points/zones, time series) | ✓ (flow, pressure, level, quality; DMA organization) | ✓ (flows, volumes, pressures; sectorisation) | ✓ (single data model; network digital twin) | ✓ (logger network + PrimeWeb; DMAs) | ✓ (zone-entry pressures/flow; iNet) |
| Water-quality signals in the condition | ✓ (turbidity, chlorine, pH events) | ✓ (Quality module — optional) | ✓ (water age/quality in twin; compliance framing) | — | ✓ (eNet water quality events) |
| Leak/burst detection against learned/expected behavior | ✓ (ML vs historic + network predictions; slow-developing leaks) | ✓ (events from hydraulic data; leak detection + location) | ✓ (Leak Detection app; SCADA+AMI+acoustic+transients) | ✓ (acoustic correlation; night recording; DMA filters) | ✓ (burst detection; transient detection) |
| Zone/DMA organization | ✓ (Area View, DMA KPIs, ILI) | ✓ (sectorisation; virtual sectors) | ✓ (DMAs and virtual DMAs) | ✓ (DMA-by-DMA logger planning/filters) | ✓ (zones at PRV entries) |
| Water-loss/NRW accounting layer | ✓ (water loss KPIs, nightline, ILI) | ✓ (nighttime flow, network performance, NRW cases) | ✓ (NRW reduction; Water Loss Management) | ✓ (leakage POIs; leakage-reduction service) | ✓ (leakage reduction via pressure) |
| Event as managed object with lifecycle | ✓ (declare → prioritize → track field activity → verify repair) | ✓ (event management; alerts with location) | ✓ (prioritize events; key indicators) | ✓ (POIs generated, followed up by technicians) | ✓ (eNet incident management) |
| Field response native vs via integration | via integration (work order, EAM, CRM, call center) | via integration (CRM, workforce management) | via platform integration (CMMS/ERP in data sources) | via managed-service handoff (POIs → utility technicians) | via integration (eNet; maintenance dispatch per Tracxn description) |
| Supervisory control in the product | ✗ (explicitly complementary to SCADA) | ✗ (monitoring; control via SCADA; suite has separate control products) | ✗ for network apps (process automation framed at plant level; what-if suggestions) | ✗ (RTUs are telemetry devices; control not the software's act) | ✓ (oNet controls PRVs/pumps — the variant) |
| Hydraulic model / digital twin | ✗ (behavior learned from data) | optional ("from monitoring… to a digital twin") | ✓ (connected hydraulic model, what-if) | ✗ | ✗ |
| Managed-service operating model | ✗ (SaaS self-use) | ✗ (software; operator services separate) | ✗ | ✓ (LeakNavigator fully-managed service) | ✗ |

Reading: all five products hold the same three-part skeleton — live network condition organized by network zones + detection machinery producing network events + a managed loop to field response. They differ in where the center of gravity sits (analytics vs suite vs platform vs devices vs control), in whether quality signals and hydraulic models are included, and in whether control is in scope. No product holds the crew/work-order execution natively — field response is reached through integration or managed-service handoff.

## Canonical Model (four abstraction layers)

### L0 — Defining Invariant

The water utility's distribution-network operations watch — three jointly-held structures:

1. **The live network condition as the watched object** — the drinking-water distribution/transmission network's operating state (pressures, flows, levels, and commonly quality parameters) held as continuously refreshed measurements bound to identified points on the network and organized by the network's zone/area structure, accumulating as time series. Remove → SCADA point telemetry or a device fleet with no network semantics.
2. **Detection machinery turning the condition into identified network events** — leak/burst detection against learned or expected behavior (night-flow/water-balance analysis, anomaly detection, acoustic/survey detections), plus threshold alarms and accepted external alert feeds, producing events as managed objects. Remove → a dashboard or alarm feed nobody works.
3. **The managed event-to-response loop** — each event a tracked case (type, location/zone, magnitude, status) driven through validation/prioritization → investigation → field response (reached through work-order integration or managed-service handoff) → verified closure, with outcomes feeding water-loss accounting and network performance history. Remove → generic ticket queue or a repair log with no detection semantics.

Binding: the subject is the utility's own piped drinking-water network (distribution and transmission). Remove the binding → environmental water monitoring (receiving waters), building/plumbing leak detection, or generic SCADA.

Jointly-held load-bearing: (1 alone = telemetry dashboard/SCADA-lite; 2 without 1 = detection over nothing; 3 without 1+2 = generic work orders; 1+2 without 3 = alarm console; 1+3 without 2 = complaint-driven repair log; 2+3 without 1 = blind event management).

### L1 — Common Mature Structure

- Zone/DMA organization as the working geography (DMAs, sectors, virtual sectors/DMAs where physical metering is absent)
- Water-loss/NRW accounting layer: night flow/nightline, DMA water balance, ILI-class KPIs, NRW trends, leakage-target reporting
- Water-quality signals in the condition (chlorine residual, turbidity, pH-class) and quality-event detection
- Multi-source data integration: SCADA, telemetry units, dedicated sensors, acoustic loggers, AMI/AMR meter data, GIS, hydraulic models, customer calls/complaints
- Multi-source corroboration and confidence/prioritization logic (two independent indications → validated event)
- Data-quality machinery as a first-class concern: data availability/quality scores, gap filling, missing-data modeling, telemetry/data issues as detectable events
- Management dashboards and KPIs (response time to events, water loss, data availability); operational and management reporting
- Alarm configuration across data channels; event prioritization (to-do lists per role)
- Integration outward to work order/EAM/CRM/call-center systems for field response
- PRV/asset condition monitoring (PRV failure events, meter failure events, reservoir level deviations)

### L2 — Variant / Optional Structure

- Detection substrate: hydraulic/flow-pressure analytics, fixed or lift-and-shift acoustic logger networks, satellite imagery analytics, in-pipe devices ("digital bullets"/spheres), smart-meter analytics, pressure-transient monitoring — substrate is implementation, not definition
- Hydraulic model / digital twin layer (calibrated model, what-if scenarios, sensor-gap inference) — optional advanced layer
- Pressure control in the product (PRV/pump optimization) — the control-inclusive variant (i2O oNet); elsewhere control stays in SCADA/telemetry
- Quality module as separately licensed add-on (SUEZ) vs included (TaKaDu)
- Managed-service operating model (vendor plans logger networks, runs analysis, hands POIs to utility technicians — Ovarro LeakNavigator)
- Suite breadth: drinking-water-network-only vs whole-water-cycle platforms (plants, wastewater network, wells, resources)
- Deployment: cloud SaaS vs operator-run; modular licensing
- Regulatory-context packaging: leakage-reduction targets as the framing (UK regulatory regime) vs NRW-as-economic-loss framing
- Scale tier: single-utility deployments to national programs

### L3 — Vendor-specific (Research Notes only)

- TaKaDu: "Central Event Management" category naming; event declaration "typically within 1 hour" of significant anomaly; Area View/Dashboard View/Reports module naming; pre-validated integration list (IBM Maximo, ABB Symphony Plus, Aquarius, Gutermann, Syrinix); "about 1 billion liters of water savings annually" claim.
- SUEZ: hydraulic/Quality/Pressure module split; business-indicator set (nighttime flow, daily volume, network performance); Milan virtual-sector counts (10 sectors, 287 sub-sectors); case-study NRW figures (Macau 18%→<10%, SEAAL 45.3%→42.2%); PIPEboard corrosion/particle indices; Nautilus smart sphere; "160 years of operator expertise" positioning.
- Xylem Vue: Smart Water Engine single data model; 120+ protocols claim; application naming (Unified Network Management, Leak Detection, Meter Data Analytics, Pipe Planner, Real-Time What-If Scenarios); GoAigua/Idrica lineage; Sensus meter/FlexNet pairing in the Hot Springs case.
- Ovarro: Enigma logger family (3m/hyQ/5M variants), night-recording epoch design (three samples), PrimeWeb cloud analytics, LeakInsight DMA filters, LeakNavigator managed-service packaging, Kingfisher RTU line.
- i2O: iNet/dNet/eNet/oNet module naming; Advanced Pilot Valve hardware; control-philosophy configuration (fixed outlet, flow modulation, critical-point optimization, no-flow-meter option); eNet powered by Badger Software CLIO; Sentryx (Mueller) platform reference post-acquisition.

## Anti-overfit Register

- **Acoustic/satellite/in-pipe detection substrates** — NOT definitional. All are implementations of "detection machinery"; the hydraulic-analytics pole (TaKaDu, SUEZ hydraulic module) detects leaks without any of them.
- **Machine learning / AI** — NOT definitional. Statistical anomaly detection against learned behavior is the invariant; ML is the current dominant implementation (TaKaDu names both "statistical techniques and machine learning").
- **Digital twin / hydraulic model** — NOT definitional (optional advanced layer; TaKaDu and Ovarro run without one).
- **DMA as a method** — NOT definitional per se; the zone/area organization is the invariant, DMAs (metered districts) and virtual DMAs are its common implementations.
- **NRW program accounting** — common mature structure (L1), not the defining core; the minimal form (district night-flow charts) predates formal NRW frameworks.
- **Water-quality signals** — common (L1), not definitional (i2O's monitoring core is pressure/flow; Ovarro's is acoustic).
- **Supervisory control** — NOT definitional; explicitly excluded by the SCADA seam (TaKaDu's own "complementary systems" statement); pressure control is the i2O variant.
- **Cloud/SaaS** — NOT definitional (deployment form).
- **Smart-city embedding** — integration variant (TaKaDu press: "part of a comprehensive Smart City solution"), not definitional.
- **Customer-meter analytics** — adjacent capability (input source and service-pipe leak detection), the metering estate belongs to AMI/MDMS.

## Historical / Market-Sample Check (§24)

- **Paper-era water network operations office** (mid-20th century municipal water department): district meter charts read each morning (night-flow measurement per district), waste/sounding surveys with listening rods, step tests isolating sections, complaint ledger driving leak digging, repair orders tracked to completion — satisfies all three L0 legs with zero digital machinery (condition bound to districts; detection = systematic survey practice + night-flow measurement; event → repair order → closure). PASS.
- **Telemetry-era (1980s–90s)**: district meters + telemetry outstations + control-room wall diagram + night-flow analysis + leak-survey programs — fits without cloud/ML. PASS.
- **Regional variant — regulated leakage regimes (UK)**: same L0 with leakage-target reporting as the dominant KPI layer; fits as variant. PASS (held at moderate strength; regime framing evidenced via SUEZ UK page and Southern Water case).
- **Control-inclusive variant (i2O)**: same L0 plus control act. PASS as variant.
- The L0 names no sensor technology, no protocol, no deployment form, no detection algorithm class. PASS.

## Boundary Findings

1. **vs SCADA (§16, processed) — seam RATIFIED keep-both, with first-hand vendor evidence.** SCADA's L0: field units + central point database + supervisory control write-back, "point-based organization with NO connected network model required." Water Network Monitoring's L0: network-condition watch + detection machinery + event-to-response loop, organized by network zones with water-network semantics (night flow, water balance, leak events). TaKaDu's own statement: "SCADA and CEM are complementary systems… SCADA systems provide rich data and enable monitoring and control of remote assets in real time, TaKaDu offers advanced data analysis tools, with a decision support process for managing events… with or without SCADA, you are well-positioned to benefit from CEM." SUEZ connects to SCADA as a data source; i2O's control variant is the one in-sample product whose act reaches devices — held as variant. The two Types co-exist in one utility: SCADA is the control/telemetry machinery, network monitoring is the water-domain application over its data.
2. **vs industrial-historian (§16, processed)** — the historian is the archival substrate (tags, high-density retention, retrieval); network monitoring is the operational application over network semantics. Historians appear as data sources (SUEZ "historical database"; WIMS-class interfaces). Keep-both.
3. **vs utility-gis (§19, processed)** — GIS holds the as-built network model of record (connectivity); monitoring holds the live condition over that frame. The network model enters monitoring as context (imported/connected: SUEZ "GIS" data source; Xylem GIS integration; Ovarro pipe schematics). Keep-both.
4. **vs utility-asset-management (§19, processed)** — asset register + care + capital governance vs live condition + events. PRV/pipe failures detected here become asset work orders there. Keep-both.
5. **vs utility-field-service-management (§19, processed)** — the event case lives here; the crew and work order live there. In-sample, field response is reached through work-order/EAM integration (TaKaDu, SUEZ) or managed-service handoff (Ovarro POIs → technicians). Same seam shape as OMS→FSM and RA→FSM. Keep-both.
6. **vs utility-revenue-assurance (§19, processed) — INHERITED SEAM DISCHARGED, RATIFIED from this side.** Per the IWA/AWWA water balance, water losses split into real losses (leakage/bursts/overflow) and apparent losses (meter inaccuracies, theft, billing). All five sampled products center REAL losses: leak/burst detection, night-flow analysis, acoustic correlation, pressure management. None handles billing-side loss recovery; where customer-meter data is used (Xylem Meter Data Analytics "customer leak detection algorithms"), it is physical-loss detection via service-pipe leaks, not revenue recovery. RA's claim ("this leaf claims ONLY the apparent/commercial half… real losses stay with network monitoring") is confirmed. Keep-both; the split is the IWA water balance itself.
7. **vs AMI / MDMS (§19, processed)** — the metering estate (endpoints, head-end, billing-grade VEE data) belongs there; network monitoring consumes AMI data as one input among several (TaKaDu "consumers' digital meters"; SUEZ "AMI"/"remote reading systems"; Xylem "AMI/AMR"). Customer-meter analytics products (BEACON-class) sit on the metering side. Keep-both.
8. **vs outage-management-system-oms (§19, processed)** — structural analog (event → field response), different object world: OMS predicts outaged devices on the electric connectivity model from trouble calls and restores supply; water network monitoring detects leaks/quality/pressure events on hydraulic evidence and drives repair to stop water loss. No water-OMS category found in-sample; burst response flows through this leaf's event loop + FSM. Keep-both; recorded as analogy, not identity.
9. **vs water-utility-management (§19, unprocessed)** — forward seam: per the ratified commodity-vertical pattern, that leaf is the customer-service business system of record (accounts, charges, bills, money); this leaf is the operations watch over the network. No object overlap. To be honored when that leaf is processed.
10. **vs water-quality-management (§19, unprocessed)** — forward seam + naming-collision watch (inherited from wastewater-compliance-management): the operational real-time quality signal inside the network condition (chlorine/turbidity events — TaKaDu, SUEZ Quality module) belongs to this leaf's condition; the quality-assurance/compliance program (sampling plans, drinking-water standards reporting) is expected to be that leaf's center. To be honored when that leaf is processed.
11. **vs environmental-water-monitoring (§21, unprocessed — pass FAILED 2026-09-08)** — subject binding differs: receiving waters/environment (observation loop over environmental media) vs the utility's own network (operations watch). Keep-both expected; flag stands for that leaf's re-run.
12. **vs wastewater-compliance-management (§21, processed)** — no overlap (discharge compliance vs network operations). Note: SUEZ AQUADVANCED Urban Drainage and Xylem Vue's wastewater network applications are the sewer-network twins of this Type — see taxonomy observation below.
13. **vs smart-city-operations-platform (§24, processed)** — single-domain operations watch vs cross-domain city platform; TaKaDu's smart-city mention is integration, not merger. Keep-both.
14. **vs §14 Network Monitoring (IT)** — name collision only; different domain (data networks). No seam.
15. **TAXONOMY OBSERVATION (no directory change)** — §19 has a dedicated monitoring leaf for the drinking-water network but none for the sewer/collection network, although the market sells the parallel product (SUEZ AQUADVANCED Urban Drainage "transforms wastewater network management. Continuous, real time monitoring detects anomalies…"; Xylem Vue wastewater network management). The wastewater-utility-management pass already observed this absorption (collection estate held by the horizontal asset family + CCTV specialists). Recorded in STATUS Boundary Issues as an observation for the taxonomy owner.

## Uncertainties

- **Engineering/hydraulic-modeling pole unreachable**: Autodesk/Innovyze Info360 and Bentley OpenFlows WaterOPS documentation was unreachable this pass and in prior passes (403/404, documented in research/utility-gis.md and research/utility-asset-management.md). The hydraulic-model-integrated monitoring pole is therefore held at lower evidence strength; no precise claims are made about those products.
- **Xylem Vue evidence is snippet-level** (official pages 403 on direct fetch; content from official-page search snippets). Platform architecture claims are Tier-2 snippet strength.
- **Event-declaration timing** ("typically within 1 hour" — TaKaDu) is a vendor-specific operational detail, kept out of the final document.
- **i2O ownership transition** (Mueller acquisition 2026-06, assets to GWF 2026-06): product family treated as continuing; Sentryx reference in the support portal noted but not asserted further.
- **Whether any product natively executes field work** (crews, work orders) rather than integrating: none found in-sample; the "through integration" reading is held at sample strength.
- **NRW/leakage regulatory regimes outside the UK**: the leakage-target framing is evidenced for the UK; other regimes assumed similar but not sampled.
- **SUEZ case-study figures** (NRW percentages, event counts) are vendor-published results, kept in Research Notes only.

## Final Synthesis

Water Network Monitoring is the drinking-water utility's distribution-network operations watch: the live network condition (pressures, flows, levels, commonly quality) held as continuously refreshed measurements bound to network points and organized by zones/DMAs; detection machinery that turns that condition into identified network events (leak/burst detection against learned or expected behavior — night-flow/water-balance analysis, anomaly detection, acoustic/survey detections — plus alarms and external alert feeds); and a managed event-to-response loop (validate/prioritize → investigate → field response via work-order integration or managed-service handoff → verified closure) whose outcomes feed water-loss accounting and network performance history. The market realizes one Type across five poles — pure-play SaaS event management (TaKaDu), operator-owned suites (SUEZ AQUADVANCED), conglomerate platforms (Xylem Vue), device-led specialists (Ovarro), and control-led pressure management (i2O) — differing in center of gravity, substrate, and whether control or the hydraulic model is in scope, not in the defining skeleton. The SCADA seam is ratified with first-hand vendor evidence (complementary systems); the revenue-assurance seam is discharged (real losses here, apparent losses there, per the IWA water balance); the paper-era district night-flow + sounding-survey office satisfies the definition, so no era-specific machinery is definitional.
