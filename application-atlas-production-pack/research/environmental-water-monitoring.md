# Research Notes — Environmental Water Monitoring

## Research Goal

Understand what "Environmental Water Monitoring" is as an Application Type: the software that operates the observation loop over **ambient/environmental waters** — rivers, streams, lakes, reservoirs, wetlands, estuaries, coastal waters, groundwater. Identify its core objects (monitoring stations, sensor time series, sampling events, lab results, the persistent water record), its data flow (telemetry + discrete sampling → validation → record → presentation → alerting/publishing), who uses it across market segments, and where its boundaries lie against the processed water family (water-quality-management §19, water-network-monitoring §19, wastewater-compliance-management §21, environmental-data-platform §21, environmental-monitoring-platform §21, air-quality-monitoring §21, emissions-monitoring-cems §21) and the unprocessed siblings.

This pass must discharge three inherited forward seams:
1. **wastewater-compliance-management (§21, processed 2026-09-10)** — flag (b): "same specialist-sibling pattern as AQM/CEMS: water-discharge compliance is the regulated-source pole of the water family (permit-bound limits + exceedance records + regulator reports vs observation loop)."
2. **water-quality-management (§19, processed 2026-09-10)** — forward seam: "the utility's own product water vs ambient/receiving environmental waters; compliance program vs observation loop"; plus confirmation of the naming-collision resolution (the ambient-monitoring sense of "water quality management" was assigned to this leaf).
3. **water-network-monitoring (§19, processed 2026-09-10)** — forward seam: "receiving waters vs own network" (that leaf's 2026-09-08 run failed rc=143; this is the re-run).

## Initial Boundary (working hypothesis before research)

- Core use: software that collects, manages, and presents measurements of water conditions (level, flow, temperature, dissolved oxygen, pH, turbidity, conductivity, nutrients, algae pigments, etc.) at identified monitoring stations in environmental waters, over time.
- Likely users: environmental agencies (national/state/regional), basin/watershed authorities, drinking-water utilities watching source waters, hydropower operators, mining/industrial operators watching receiving waters, researchers, consultants, volunteer programs.
- Nearest Types: Environmental Monitoring Platform (media-agnostic loop), Air Quality Monitoring (air twin), Wastewater Compliance Management (regulated-source pole), Water Quality Management (utility's own drinking water), Water Network Monitoring (utility's own distribution network), Environmental Data Platform (corpus of record), SCADA/IIoT (telemetry substrate).
- Open questions: is the discrete sampling + laboratory path a defining structure (vs air monitoring's sensor-only pattern)? is hydrology (level/flow, rating curves) in scope? is "current conditions" load-bearing for archive-first agency systems? where exactly is the seam against the environmental-data-platform pole (WISKI was sampled there as its water specimen)?

## Research Questions

1. What are the core objects — monitoring station, water body/watershed organization, sensor time series, sampling event, lab result, vertical/depth?
2. How do the two data paths (continuous telemetry vs discrete sampling with laboratory analysis) relate, and is either required?
3. What does the data-quality/defensibility machinery look like (validation, correction, approval, audit trail)?
4. What role do hydrology (stage/discharge, rating curves) and rainfall play?
5. How are thresholds, alerts, and standards-based assessment handled — and where does compliance semantics end (sibling seam)?
6. What are the main interfaces (map/network view, station time series, sample management, device health, publishing)?
7. Where are the boundaries vs the media-agnostic platform, the air twin, the regulated-source pole, the utility-side Types, and the data-corpus platform?

## Representative Products

| Product | Vendor | Pole / philosophy | Why selected |
|---|---|---|---|
| AQUARIUS | Aquatic Informatics (Veralto) | Agency water-data platform: acquire → process → model → publish for monitoring agencies | the flagship of the government-agency pole (USGS, Environment Canada, NIWA observed as clients); hydrology + water quality + discrete samples in one system |
| WISKI | KISTERS | European agency water-information system; modular, on-prem/cloud | second agency-pole specimen for cross-product commonality; already fetched Layer-A by the environmental-data-platform pass (2026-09-09) — reused here with the seam addressed |
| YSI (surface-water systems) | YSI / Xylem | Instrument-maker field systems: sondes, handhelds, buoys, auto samplers, telemetry | the field-instrument pole; defines the deployment forms and the water-quality parameter vocabulary |
| OptiRTC | OptiRTC (Aliaxis) | Stormwater Continuous Monitoring and Adaptive Control (CMAC) | the control-inclusive boundary pole: monitoring feeding automated infrastructure control; stormwater/receiving-water variant |
| LG Sonic (MPC-Buoy / MPC-View) | LG Sonic | Lake/reservoir real-time buoy monitoring + bloom prediction + ultrasonic treatment | the lake/HAB real-time pole; monitor-predict-control posture; vendor-operated service model |

Coverage: national/federal + state agencies (AQUARIUS, WISKI), European public authorities (WISKI), research/consulting field programs (YSI), municipal stormwater utilities (OptiRTC), drinking-water and power utilities with lakes/reservoirs (LG Sonic); philosophies from archive-first agency record (AQUARIUS/WISKI) to operations-first real-time control (OptiRTC, LG Sonic).

## Sources

Fetched 2026-09-10 (WebFetch, official pages):

- Aquatic Informatics — root https://aquaticinformatics.com/ (fetched; product family, positioning, client logos, water-cycle framing) and Aquarius product page https://aquaticinformatics.com/products/aquarius-environmental-water-data-management/ (fetched; rich operational detail: acquisition, QA/QC, rating curves, sample management, HydroCorrect, dashboards, publishing)
- YSI — surface-water application page https://www.ysi.com/applications/surface-water (fetched; measurement methods, deployment forms, parameters, applications) and site navigation (applications/parameters taxonomy); https://www.ysi.com/wqms (fetched — a discontinued hardware datalogger product; shows the integrated-station product form, not software)
- OptiRTC — root https://www.optirtc.com/ (fetched; CMAC solution, pillars, compliance framing, project flow)
- LG Sonic — root https://www.lgsonic.com/ (fetched; industries, technology framing) and MPC-Buoy product page https://www.lgsonic.com/products/mpc-buoy/ (fetched; monitor/predict/control detail, MPC-View software, telemetry, sensors)

Failed / abandoned (per network rules, 2 attempts each):

- KISTERS WISKI — https://www.kisters.net/wiski timed out twice on 2026-09-10. **Fallback:** Layer-A observations from the environmental-data-platform pass (fetched 2026-09-09, recorded in research/environmental-data-platform.md) are cross-referenced and marked as such. No new WISKI claims beyond that record.
- In-Situ (HydroVu) — https://in-situ.com/ and https://www.in-situ.com/ returned 403 twice. Product dropped from the sample; the sensor-cloud pole is evidenced instead by LG Sonic MPC-View and YSI telemetry.

Source-access limitations:

- Vendor help centers / user manuals were not fetched in this pass; all observations come from official product, application, and solution pages.
- YSI's cloud software (Kor Software / EcoNet telemetry portal) was not directly observed; YSI claims below are restricted to the fetched application page and site structure (instrument + telemetry + "custom visual display" language).
- Regulatory assessment depth (e.g., EU WFD classification, US ambient criteria programs) is asserted only qualitatively; no regime-specific workflow was directly observed.

## Product Observations

### AQUARIUS (Aquatic Informatics) — evidence layer A (directly observed)

From the root and product pages:

- Positioning: "Water Data Management Software for the Full Water Cycle"; "From source water through to the receiving environment, our interconnected data management platforms drive the efficient management of water information across the water cycle." Aquarius is the natural-environment line: "analytics software for natural environments that provides an integrated suite from data acquisition, to data management, and right through to web-based data dissemination and decision support."
- Core loop (product page): "Water monitoring agencies worldwide trust Aquarius™ to acquire, process, model, and publish water information in real time."
- Data acquisition: "Access Any Data Source In Real Time — Extend the value of your existing investments, third-party sensors, or systems by normalizing any type of data to manage, qualify, and analyze centrally." (hardware-agnostic ingestion posture)
- Analysis/QA: "Easily visualize, scan, and QA/QC your data with best-in-class rating curves, automated error detections, and intuitive correction tools that compare historic time-series or discrete data, with a defensible audit trail."
- Single source of truth: "Environmental data from multiple sources are securely stored for fast, central access to easily correct and quality control data, build better rating curves, derive statistics, and report in real-time... unify your data to establish a smart water monitoring system for flood analysis, real-time water quality monitoring, predicting water availability, and water compliance."
- **Discrete sample path (first-class):** "Sample Management Made Easy — Streamline the collection and management of environmental lab and field sample data... All your discrete water, air, soil, and biological data are securely stored and validated online for rapid analysis and visualization."
- Presentation: "Contextual Visualization, Maps, & Dashboards — Stakeholders internally or externally can self-serve quality-assured data, real-time statistics, user-specific dashboards, and set custom parameters to easily see status indicators and deliver warning notifications. You can respond quickly to flooding and weather events with proactive communication and decision-support."
- Trust/defensibility: "With streamlined QA/QC capabilities and a rich audit trail, your team can rely on the information to be accurate, timely, and defensible. Use predictive analytics, trend analysis, and contextual alerts..."
- HydroCorrect (AI/ML QA/QC module): "automating data review, cleansing, and error detection"; "rule recommendations to accept or reject based on your use case"; "centralizes data correction suggestions, rule changes, and alert parameters"; "detailed and easy-to-understand audit trail, enabling you to oversee the process with the flexibility to approve or reject the tool's actions"; "user-defined rules that can be applied across your network."
- Hydrology: "build better rating curves, derive accurate flows, and model hydrological systems" (source-water card); stormwater card: "real-time and predicted reservoir levels, stream-flows, and rainfall" against "flood dangers."
- Deployment: Aquarius Cloud (managed SaaS on AWS) alongside the on-prem heritage ("By migrating to Aquarius Cloud... eliminate the need to manage infrastructure").
- Clients (logos): USGS, Environment Canada, NIWA (New Zealand), South Dakota, Idaho Power (hydropower), City of Orlando (stormwater — rainfall-intensity evaluation quote), St. Johns River Water Management District ("Water Quality Monitoring Program... clear, centralized system with alerts and easy-to-use dashboards").
- Industries: National & Federal Agencies, State & Local Government, Consulting & Engineering, Hydropower, Mining, Utilities, Food & Beverage.
- Sibling products in the same vendor family (boundary context): Rio/WIMS (utility compliance/operations), WaterTrax (drinking/wastewater compliance), Tokay (backflow), Linko (FOG/pretreatment) — the vendor itself separates the ambient/natural-environment line (Aquarius) from the utility compliance lines.

### WISKI (KISTERS) — evidence layer A via sibling pass (cross-referenced; direct fetch failed this pass)

From research/environmental-data-platform.md (fetched 2026-09-09):

- Positioning: "modular Water Information System for managing, validating, analyzing & visualising hydrological & environmental data across its full lifecycle"; "used worldwide by public authorities, utilities & consultancy firms"; "scale from local monitoring networks to national systems."
- Unit of record: "central time-series + observation corpus per monitoring network (stations, parameters, time series)"; telemetry/SCADA/models ingestion as core.
- Water-quality modules: KiWQM & KiECO — "Combine laboratory results and sensor data into one consistent, auditable system"; trend analysis; compliance-ready workflows. (The lab+sensor merge is explicit.)
- Hydrometry: BIBER & SKED — "discharge calculations, rating curves, ADCP support; 'accurate, traceable and defensible hydrometric data'."
- Field: FieldVisits — "mobile field data collection, offline, sync to central system."
- Publishing: WISKI Web — "publish trusted data in real time via secure web portals; access control; 'transparent data sharing for compliance and public communication'."
- Analytics: KISTERS Analytics — "automation of validation/alarming/analysis; AI, predictive modelling, digital twins."

**Seam note:** the environmental-data-platform pass used WISKI to prove the corpus-of-record Type holds without a contamination frame. This pass reads the same product from the water-observation-loop center (network operation, telemetry, field visits, real-time publishing) and addresses the corpus-vs-loop seam in Boundary Findings.

### YSI (Xylem) — evidence layer A (directly observed)

From the surface-water application page and site structure:

- Subject framing: "Surface water — lakes, rivers, streams, reservoirs, wetlands, estuaries — are all threatened daily from harmful algal blooms, anoxic conditions, sediment plumes, and much more."
- Two measurement modes: "instruments for both baseline sampling efforts, as well as continuous monitoring systems... capable of recording high temporal resolution data, which detects events (meteorological, pollution-related, or otherwise) that may impact water quality."
- Spot sampling: handhelds "allow people to gather lab-quality measurements in the field... capture measurements of parameters that may drift before they reach a laboratory."
- Continuous: sondes — "long term unattended monitoring — the constant monitoring that allows scientists to observe midnight activity and chart diurnal cycles... monitor remote locations constantly, for long periods, without the need for an operator on-site."
- Buoys/telemetry: "thousands of hydrometeorological data delivery solutions... Add satellite, radio, or cellular telemetry to provide data to a custom visual display, making it easy for researchers and operators alike to receive critical data on a daily basis."
- Auto samplers: "sample based on time, analog signal, digital pulse, and/or optional measurement from an SDI-12 device" — stormwater, industrial discharge, rivers, streams.
- Parameter vocabulary (site taxonomy): temperature, dissolved oxygen, depth/level, pH, conductivity, ORP, turbidity; advanced: blue-green algae (phycocyanin), chlorophyll, CDOM-fDOM, PAR, ammonia, nitrate, chloride, rhodamine; plus flow (SonTek ADCPs) and weather.
- Applications (observed narratives): streams & rivers (compliance standards; "sources of contamination or alteration — such as urban sewage, agricultural runoff, or industrial effluent — can be determined"); nutrients & HABs ("early warning systems can be developed to better alert communities when bodies of water may be unsafe"; surrogate analysis comparing pigment sensor data "to collected samples analyzed in the laboratory"); dredging (turbidity/DO monitored "to ensure environmental compliance as dredging takes place"); limnology (lakes as drinking-water sources; recreational safety); dissolved oxygen at energy sites ("Hydroelectric power plants are mandated to maintain certain levels of dissolved oxygen downstream of the dam... operators... can take corrective actions").
- Instrument QC: EXO "SmartQC ensures top performance"; "anti-fouling wiper enables extended deployments"; calibration solutions category.
- Site structure: applications span Surface Water, Groundwater, Ocean & Coastal, Stormwater, HABs, Source/Raw & Drinking Water, Smart Watershed, Flooding, Flow; "Water Monitoring Services" (a services pole); "Turn Key Data Collection Platform — Complete Solution for Data Logging and Telemetry."
- The /wqms page (fetched) is a discontinued integrated hardware station (multichannel datalogger + 4–20 mA sensors, PC/PDA software) — evidence of the integrated-station product form, not a software platform.

### OptiRTC — evidence layer A (directly observed)

From the root page:

- Positioning: "Opti's Continuous Monitoring and Adaptive Control (CMAC) solution optimizes the collection, storage, and treatment of stormwater runoff."
- Three pillars: "Real-Time Sensor Data and Forecast Information"; "Automated Stormwater Infrastructure Controls"; "Continuous Monitoring and Adaptation."
- Track record framing: "Over 60,000 storms managed"; "Performance and compliance reporting"; "Forecast-based automated control"; "Continuous adaptation to changing climate, watersheds, and regulations."
- Challenges addressed: Flooding; Regulatory Compliance "(MS4, CSO, Development)"; Land Availability; Water Quality.
- Project flow: Measure → Enhance → Optimize → Manage; "Smart Watershed Network."
- Customer quote (Albany): "identify existing conditions and develop strategies to adapt to a changing environment."
- Surroundings: user portal (portal.onopti.com), documentation site (docs.optirtc.com), certified hardware program, partner community, regulatory-approvals page, Maryland credit calculator.

### LG Sonic (MPC-Buoy / MPC-View) — evidence layer A (directly observed)

From the root and MPC-Buoy product pages:

- Positioning: "Monitor, Predict, and Control Algae" — an all-in-one floating platform for lakes, reservoirs, dams, cooling ponds; "The E-Line controls algae, while the MPC-Buoy monitors, predicts, and controls it."
- Monitor: "complete overview of your water quality by collecting the following parameters every 10 minutes: Chlorophyll α (green algae), Phycocyanin (blue-green algae), pH, Turbidity, Dissolved oxygen, Temperature"; additional sensors purchasable; automatic antifouling wiper; optional vertical profiling ("measure the entire water column").
- Predict: "database contains more than 10 years of information collected from thousands of LG Sonic devices operating around the world... continually refreshed... always optimizing predictive algorithms."
- Control: ultrasonic programs tuned per water body ("waveform, frequency, pause, and amplitude"); "adjusting settings before the algae mutate"; Chameleon Technology adjusts the program to water conditions.
- MPC-View (the software): "online water quality monitoring software... complete picture of your water body at every monitored location... real-time insights into water quality, algae growth, and treatment progress... create rules that trigger email alerts when predetermined parameters are breached... dashboard accessible on any electronic device."
- Telemetry/ops: 4G, Iridium satellite, LAN, GPS; solar-powered; "24/7 emergency support; Our team monitors your system 24 hours/day"; vendor experts "monitor and operate the MPC-Buoys remotely."
- Related products: Monitoring Buoy (monitor + predict, no treatment), Vertical Profiler, Remote Sensing (satellite).
- Industries: drinking-water reservoirs, recreational lakes, power generation, irrigation reservoirs, wastewater reservoirs, hydroelectric dams, oil & gas, mining.

## Cross-product Comparison

| Dimension | AQUARIUS | WISKI (sibling-pass evidence) | YSI | OptiRTC | LG Sonic |
|---|---|---|---|---|---|
| Monitored subject | ambient waters across the water cycle (source water → receiving environment) | hydrological & environmental data for public authorities | surface water/groundwater/coastal/stormwater via field instruments | stormwater infrastructure & receiving waters | lakes/reservoirs water quality & algae |
| Station concept | monitoring-network stations; any data source normalized centrally | stations in monitoring networks (local → national scale) | deployment platforms: sonde site, buoy, handheld station, sampler | sensor nodes on stormwater infrastructure | anchored buoy per water body/location |
| Data paths | telemetry + discrete samples (explicit sample management) | sensor + laboratory combined (KiWQM/KiECO) | continuous sondes + spot sampling + auto samplers | continuous sensors + forecast feeds | continuous buoy sensors (10-min cadence observed) |
| Parameters | water quality + hydrology (level, flow, rainfall) | hydrology + water quality | water-quality suite + level/flow + weather | stormwater quantities (level/flow/rainfall implied) | algae pigments + core WQ suite (DO, pH, turbidity, temperature) |
| QA/validation | QA/QC + correction tools + defensible audit trail; AI-assisted (HydroCorrect) | validation across the data lifecycle; "auditable" | instrument-grade QC (SmartQC, calibration, antifouling) | not observed | antifouling wipers; vendor remote QC/operation |
| Rating curves / hydrometry | "best-in-class rating curves", derive flows | BIBER/SKED discharge + rating curves, ADCP | flow instruments (ADCPs); no curve software observed | not observed | not observed |
| Current conditions | real-time statistics, dashboards, maps | real-time publishing (WISKI Web) | telemetry to "custom visual display" | real-time sensor data + forecasts | MPC-View real-time dashboard |
| Historical record | central time-series store; statistics; discrete data store | full-lifecycle corpus | onboard memory → data delivery | continuous monitoring record | MPC-View history; vendor-wide 10-year database |
| Thresholds/alerts | warning notifications, contextual alerts | automated alarming | early-warning-systems framing | compliance/performance reporting posture | email alert rules on parameter breach |
| Standards/assessment | "water compliance" framing | compliance-ready workflows | compliance references (dredging, dam DO mandates) | MS4/CSO/development compliance reporting | NPDES compliance mention (power gen) |
| Publishing/sharing | web-based dissemination; self-serve for internal/external stakeholders | WISKI Web secure portals | custom displays; data services | performance/compliance reporting | customer dashboard (any device) |
| Control/actuation | none observed | none observed | none (instruments only) | automated infrastructure controls (core) | ultrasonic treatment control (core) |
| Prediction/AI | HydroCorrect predictive analytics; flood prediction | KISTERS Analytics predictive modelling, digital twins | not observed | forecast-based control | algal-bloom prediction from vendor-wide database |
| Customer tier | national/federal + state agencies, hydropower, mining, utilities, consultants | public authorities, utilities, consultants | researchers, consultants, agencies, industry | municipalities, water utilities, developers | water utilities, power, industry |

Reading: every sampled product runs the same loop — identified stations in ambient waters → measurements accumulating into a persistent record → current + historical presentation → thresholds/alerts → publishing. The poles differ in emphasis (record-first agency systems vs operations-first real-time systems), in data-path mix (lab-heavy vs sensor-heavy), and in whether monitoring feeds actuation.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product stops being an environmental water monitoring application:

```text
Identified monitoring stations in ambient waters
└── Water measurements held as a persistent record at each station
    (continuous sensor series and/or discrete sample results)
    └── Presentation of current conditions
    └── Presentation of the historical record
```

- **Monitoring station in ambient waters**: an identified, fixed location on a water body — a river section, lake/reservoir station, groundwater well, coastal buoy — carrying identity, location, and the parameters measured there. The binding is to the water in the environment, not to water inside the utility's pipes or plant, not to a regulated discharge point. Without identified stations, measurements have no spatial meaning.
- **Water measurements as persistent record**: readings and results bound to station, parameter, and time, accumulating as the station's record. The record may be sensor time series, discrete sample results, or both. Without the record, it is not monitoring.
- **Current + historical presentation**: the observation loop's two standing views — what the waters are like now, and how they have changed. Remove currency → an archive (data-platform territory); remove history → a live indicator only.

§24 historical check: a paper-era hydrometric network (staff gauges + current meters, field notebooks, published yearbooks) satisfies all legs — stations, measurements as record, today's reading, the accumulated record. A 1990s agency database with published annual reports satisfies it. A sampling-only volunteer program (paper sheets + spreadsheet) satisfies it. Cloud, telemetry, AI, maps, and real-time streaming are correctly excluded from L0. Check passes.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Dual data path** — continuous sensor telemetry AND discrete sampling events with laboratory results, merged into one record (AQUARIUS sample management + telemetry; WISKI KiWQM/KiECO "combine laboratory results and sensor data"; YSI spot sampling + sondes + auto samplers). Most mature products support both; either alone still satisfies L0.
- **Data validation / QA / approval machinery with audit trail** — correction tools, error detection, approval states, defensibility framing (AQUARIUS "defensible audit trail" + HydroCorrect; WISKI "accurate, traceable and defensible"; YSI instrument QC). The agency pole treats the defensible record as the product's core value.
- **Hydrological context** — water level, flow/discharge, rainfall alongside quality parameters; rating curves (stage-discharge) as managed objects at the hydrometric pole (AQUARIUS rating curves; WISKI BIBER/SKED).
- **Thresholds and alerts** — user-defined rules on measurements (and device conditions) triggering notifications (AQUARIUS warning notifications; LG Sonic email alert rules; YSI early-warning framing).
- **Device/network health and maintenance** — antifouling, calibration, power/solar, connectivity, remote operation (LG Sonic Aquawiper + 24/7 remote ops; YSI SmartQC/antifouling wipers; AQUARIUS device-data normalization).
- **Spatial organization** — map views and water-body/watershed/network structure (AQUARIUS maps/dashboards; WISKI network scale; LG Sonic "every monitored location").
- **Data access and publishing** — APIs, exports, reports, secure portals, self-serve dashboards (AQUARIUS web dissemination; WISKI Web; MPC-View; OptiRTC reporting).
- **Standards/threshold assessment as context** — evaluation of ambient conditions against environmental quality standards or site thresholds (compliance-ready workflows at the agency pole; MS4/CSO reporting at the stormwater pole) — as assessment context, not as the permit-bound compliance record (see Boundary Findings).

### L2 — Variant / Optional Structure

Depends on segment, medium scope, posture, or business model:

- **Medium scope** — surface water (rivers/lakes/reservoirs), groundwater networks, coastal/marine, stormwater/receiving waters; programs often span several.
- **Posture** — record-first (agency archive, validation, publication: AQUARIUS/WISKI) vs operations-first (real-time dashboards, alerts, response: LG Sonic, OptiRTC).
- **Data-path emphasis** — telemetry-first (buoy networks) vs sampling-first (agency ambient programs) vs both.
- **Control-inclusive deployments** — monitoring feeding automated actuation (OptiRTC stormwater controls; LG Sonic ultrasonic treatment). A variant pole, not the definition — most products only observe and alert.
- **Prediction/AI** — algal-bloom prediction, anomaly detection, automated data review, flood/reservoir-level prediction (HydroCorrect, LG Sonic predict, KISTERS Analytics, OptiRTC forecast-based control). Era-current, not definitional.
- **Public publishing posture** — open data portals/public maps vs private dashboards vs regulator-facing submissions.
- **Customer tier / program scale** — national network (USGS-class) → state/regional agency → single reservoir or site.
- **National data-exchange formats** — program-dependent electronic submissions (WQX-class in the US context; evidenced at the sibling data-platform pass via Locus EIM's format support; not directly observed in this pass's products) — regional/program variant.
- **Service models** — self-operated software vs vendor-operated monitoring service (LG Sonic 24/7 remote operation; YSI Water Monitoring Services).

### L3 — Vendor-specific (Research Notes only)

- AQUARIUS: HydroCorrect branding; Aquarius Cloud on AWS packaging; the vendor's product-family split (Aquarius vs Rio/WIMS/WaterTrax/Tokay/Linko); named clients (USGS, Environment Canada, NIWA, Idaho Power, City of Orlando, St. Johns River WMD).
- WISKI: module names KiWQM, KiECO, BIBER, SKED, FieldVisits, WISKI Web, KISTERS Analytics.
- YSI: EXO/ProDIGITAL/ProSeries product lines; SmartQC; LSdata; Turn Key Data Collection Platform; SonTek ADCP line; Water Monitoring Services.
- OptiRTC: CMAC branding; "60,000+ storms managed" claim; Maryland credit calculator; certified-hardware program; portal.onopti.com.
- LG Sonic: MPC-Buoy/MPC-View/Chameleon Technology/Aquawiper brands; 10-minute collection cadence; 500 m treatment range; 10-year vendor database claim; E-Line vs MPC-Buoy split.

## Vendor-specific Findings

See L3. None of these entered the canonical model.

## Rejected Findings

- **"Environmental water monitoring = water quality management."** Rejected as a collapse: the market label "water quality management" spans four senses (utility drinking-water program → §19 leaf; discharger compliance → wastewater-compliance-management; ambient monitoring → this leaf; consumer pool care → pool-service-management). The ambient sense is this leaf's center; confirmed by the water-quality-management pass's own resolution.
- **"Real-time telemetry is definitional."** Rejected — sampling-only agency programs and the paper-era network satisfy L0 without any telemetry.
- **"Rating curves are definitional."** Rejected — only the hydrometric pole manages them; buoy and stormwater products lack them entirely.
- **"Control/actuation is definitional."** Rejected — most sampled products only observe and alert; control-inclusive deployment is a variant pole (OptiRTC, LG Sonic).
- **"Cloud SaaS is definitional."** Rejected — on-prem WISKI/AQUARIUS heritage and the paper-era check both satisfy.
- **"AI-driven validation is definitional."** Rejected — HydroCorrect-class automation is era-current; manual QA/QC with audit trails satisfies.
- **"The dual data path is definitional."** Rejected as an L0 requirement — sensor-only buoy networks (LG Sonic) and sampling-only programs each satisfy L0; the dual path is the mature norm (L1), not the invariant.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (remove/add test) |
|---|---|---|
| Environmental Monitoring Platform (§21, processed) | broader sibling | EMP is the media-agnostic observation loop (air, water, soil, noise, weather). Bind the loop to ambient waters with the water-specific object model (stations in water bodies, dual sensor/sample data path, hydrology, water-quality parameter vocabulary) → this Type. Generalize the medium → EMP. EMP's own document pre-declared single-medium specialists as sibling Types; ratified from this side. |
| Air Quality Monitoring (§21, processed) | structural twin | Same grammar (points + parameter time series + current/history) but air-pollutant semantics (AQI, collocation) vs water semantics (dual data path, hydrology, water-body siting). Different medium → different Type. |
| Wastewater Compliance Management (§21, processed) | regulated-source pole of the water family | That Type binds measurement to a **regulated discharge point** under permit limits, producing exceedance records and regulator-facing reports (DMR-class). This Type observes **ambient waters** with no permit-bound discharge object; standards appear as assessment context, not as the compliance record of a permitted source. Remove the permit/discharge binding → this Type; add it → wastewater compliance. **Flag (b) from that pass RATIFIED keep-both from this side.** |
| Water Quality Management (§19, processed) | utility-side sibling | That Type is the water utility's drinking-water quality program over **its own product water** (source→treatment→distribution) under drinking-water standards, with a compliance-program center. This Type observes **ambient environmental waters** with an observation-loop center. A utility may run both (its tap-water program here vs its source-water monitoring there). **Forward seam RATIFIED from this side; the naming-collision resolution is confirmed — the ambient sense lives here.** |
| Water Network Monitoring (§19, processed) | utility-side sibling | That Type watches the utility's **own distribution network** (pressures, flows, leak/burst detection, event-to-response loop). This Type watches **receiving/ambient waters** outside the network. **Forward seam RATIFIED from this side.** |
| Environmental Data Platform (§21, processed) | corpus vs loop | That Type holds the validated long-term corpus of record for any environmental program (no live loop required; WISKI was its water specimen). This Type operates the **live observation loop** over a water monitoring network (devices, telemetry, field visits, current conditions). AQUARIUS/WISKI-class products straddle the seam: their center of gravity here is the network's observation loop; the same products serve the corpus center for mixed programs. Keep-both with the loop-vs-corpus seam. |
| Emissions Monitoring / CEMS (§21, processed) | air-side analog of the source pole | CEMS measures at a regulated air source with reference methods; this Type's water analog (the regulated discharge) belongs to wastewater-compliance-management, not here. |
| Contaminated Site Management (§21, processed) | program frame | Groundwater monitoring **under a site investigation/remediation program** centers the site lifecycle; ambient groundwater networks without the site frame belong here. |
| SCADA / Industrial Historian / IIoT (§16/§14) | generic substrate | Process telemetry holds arbitrary channels; this Type adds water-environment semantics — stations in water bodies, water-quality parameter vocabulary, sample/lab path, hydrology, defensibility machinery. |
| Stormwater management (no dedicated leaf; OptiRTC as boundary specimen) | control-inclusive boundary | When monitoring's primary loop becomes driving infrastructure (gates/valves) or treatment, the product is a stormwater-performance/control tool that contains a monitoring loop — the boundary case documenting where observation ends and actuation begins. |

Key boundary judgment: **Environmental Water Monitoring is a distinct Type** (not a variant of the media-agnostic platform) because the water-medium object model is stable and product-defining across all sampled poles: stations in water bodies, the dual sensor/sample data path, hydrological context, and the defensible long-term record. The four water-family Types (this leaf, water-quality-management, water-network-monitoring, wastewater-compliance-management) are separated by **whose water and which grammar**: ambient environment (observation loop) vs the utility's product water (compliance program) vs the utility's network (operations watch) vs a regulated discharge (permit-bound compliance record).

## Uncertainties

- WISKI was not directly fetched in this pass (timeouts ×2); its observations are cross-referenced Layer-A evidence from the environmental-data-platform pass (2026-09-09) and marked as such. No new WISKI claims were made.
- In-Situ HydroVu was dropped after repeated 403s; the sensor-cloud pole is evidenced by LG Sonic MPC-View and YSI telemetry instead. HydroVu's specific capabilities are not asserted anywhere.
- YSI's cloud software layer (Kor/EcoNet) was not directly observed; YSI claims are restricted to instruments, telemetry, and "custom visual display" language from the fetched pages.
- Regulatory assessment depth (WFD classification, US ambient criteria, national data-exchange formats such as WQX) is asserted qualitatively only; no regime-specific workflow was directly observed in this pass's products.
- The volunteer/community monitoring pole (crowdsourced water data) was not sampled; its existence is known but unverified here — L0 was checked against it conceptually (a sampling-only program satisfies the core).
- Whether flood-forecasting platforms (e.g., agency hydrological forecasting systems) deserve a separate leaf was not researched; they are treated here only as adjacent consumers of monitoring data.

## Final Synthesis

An Environmental Water Monitoring application is software that operates the observation loop over **ambient waters**: it holds a network of **identified monitoring stations** on rivers, lakes, reservoirs, groundwater, and coastal waters; it accumulates **water measurements** at those stations into a persistent record — continuous sensor time series and/or discrete sampling events with laboratory results; it maintains the record with **validation and defensibility machinery**; it presents **current conditions and the historical record**; and it drives **threshold alerting, standards-context assessment, and data publishing** (portals, APIs, reports). The defining core is small (stations in ambient waters + measurements as persistent record + current + historical presentation). The dual data path, QA/approval machinery, hydrology and rating curves, alerts, device health, maps, and publishing are standard mature capabilities; medium scope, record-first vs operations-first posture, control-inclusive deployment, prediction/AI, and public-posture publishing are variants. The Type is distinct from the media-agnostic platform (water-specific object model), the air twin (different medium and data-path structure), the utility-side water Types (whose water: product water, network, vs ambient), the regulated-source compliance pole (permit-bound discharge vs ambient observation), and the data-corpus platform (live loop vs corpus of record).
