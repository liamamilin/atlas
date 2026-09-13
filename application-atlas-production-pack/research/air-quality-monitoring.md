# Research Notes — Air Quality Monitoring

## Research Goal

Understand what an Air Quality Monitoring application actually is as an Application Type: its core objects, its data flow from measurement to presentation, who uses it across market segments, and where its boundary lies against neighboring Types (Emissions Monitoring / CEMS, Environmental Monitoring Platform, Environmental Water Monitoring, Building Management Systems, weather/data-portal surfaces).

## Initial Boundary (working hypothesis before research)

- Core use: software that collects, manages, and presents measurements of air pollutants (PM2.5, PM10, O₃, NO₂, SO₂, CO, etc.) at identified monitoring locations over time.
- Likely users: environmental agencies, city governments, industrial/construction operators, building/facility managers, researchers, community groups, individuals.
- Nearest Types: Environmental Monitoring Platform (multi-medium), Emissions Monitoring / CEMS (source-level compliance), Environmental Water Monitoring (different medium), BMS (control vs observation), weather apps and public data portals (presentation-only surfaces).
- Open questions: is indoor air quality in scope as a variant? how central are calibration/QA, alerts, maps, and AQI indices to the definition?

## Research Questions

1. What are the core objects (monitoring point, device, parameter, time series, index, threshold, alert)?
2. How does data flow from device to display (ingest → validation/correction → storage → presentation)?
3. Who uses these systems across segments (agency, enterprise, community, consumer, building)?
4. What role do calibration, collocation, and data-quality handling play?
5. How are thresholds and alerts defined and used?
6. What are the main interfaces (map, dashboard, device console, API, public app)?
7. Where is the boundary vs CEMS, multi-medium environmental monitoring, BMS/control, and data portals?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| PurpleAir | Community / crowdsourced sensor network + public map + API | consumer/community tier; open public-data posture |
| IQAir (AirVisual) | Consumer app + global data aggregator + enterprise dashboard | aggregator posture ("network of networks"); consumer + org tiers |
| Clarity Movement | Government/enterprise turnkey "Sensing-as-a-Service" networks | agency/city tier; hardware + cloud + calibration as one service |
| Kaiterra | Enterprise building/indoor air quality (IAQ) platform | building/facility tier; certification-driven (WELL/RESET); BMS integration |

Coverage: different customer tiers (individual → community → city/agency → enterprise/building), different philosophies (open crowdsourced map vs curated aggregator vs turnkey managed network vs certification-driven IAQ).

## Sources

Fetched 2026-09-06 (WebFetch, official pages):

- Clarity Movement — homepage https://www.clarity.io/ ; Dashboard page https://www.clarity.io/air-quality-monitoring-solution/cloud/dashboard (both fetched successfully; rich operational detail)
- Kaiterra — homepage https://www.kaiterra.com/ ; Data Platform page https://www.kaiterra.com/dashboard (both fetched successfully; rich operational detail)
- IQAir — homepage https://www.iqair.com/ ; AirVisual Platform page https://www.iqair.com/commercial-air-quality-monitors/airvisual-platform (both fetched successfully; feature matrix observed)
- PurpleAir — root https://www.purpleair.com/ and https://api.purpleair.com/ and https://www.purpleair.com/about (all returned navigation/JS shell only; **site structure observed, body content not reachable**)

Source-access limitations:

- PurpleAir's site is a JavaScript app; only the navigation structure was observable (Store / Solutions: Personal, Business, Education, Broadcasters, Government / Tools: Real-Time Map, Register Your Sensor, Sensor Utility / Resources: Community, FAQ, Scientific Papers, Projects & Integrations, API Documentation). Operational details (API semantics, correction factors, data layers) were NOT directly observed and are not asserted.
- Vendor help-center/knowledge-base articles (Clarity knowledge base, Kaiterra support, IQAir knowledge base) were not individually fetched; assertions below rely on the fetched product/cloud/dashboard pages.
- Airly was considered as a fifth sample but dropped after the four-product sample reached saturation (new products repeated existing evidence).

## Product Observations

### Clarity Movement (evidence layer A — directly observed)

From homepage and Dashboard page:

- Positioning: end-to-end "air quality monitoring system" = hardware (solar-powered Node-S sensor measuring PM2.5 and NO₂, plus add-on modules: Black Carbon, Dust/PM10, Multi-Gas CO/O₃/NO₂/NO/NOx, Ozone, Wind & Met) + cloud software + expert support ("Sensing-as-a-Service").
- Data flow: devices sample air → measurements uploaded via cellular to Clarity Cloud → "securely handles all aspects of your air quality data transmission, validation, storage, and processing" → accessible via Dashboard, REST API, OpenMap.
- Dashboard features (directly observed):
  - Air Quality Snapshot: instant overview of conditions at project site, real-time data, recent measurements, outlier sites.
  - Device Management and Status Tracking: fleet health, offline/unresponsive devices, sensor issues, troubleshooting, replacement.
  - Explore and Download Data: compare across locations, customize time periods and aggregations, export charts and CSV.
  - Advanced visualizations: Wind Roses (with wind module) for source attribution.
  - Accuracy Reporting for Collocated Devices: collocation reporting with R², MAE, time series, scatter plots vs reference equipment.
  - Custom Device Status and Measurement Alarms: alerts when device offline/unresponsive or when measurements exceed user-defined thresholds/rules.
  - User and Data Access Management: roles — Org Admin, Technician, Analyst, Observer, Guest; application/API permissions.
  - API-first: all Dashboard information accessible via Air Monitoring API.
- OpenMap: optional public platform sharing PM2.5 and AQI (hourly NowCast AQI, daily/monthly averages) alongside vetted government reference monitors; embeddable via iFrame.
- Data policy: customer owns data; no third-party sharing without consent; all measured data visible; optional public sharing.
- Support model: Environmental Project Manager guides project plan, collocation and calibration of devices.
- Segments: governments/agencies (expand coverage beyond sparse regulatory stations), businesses (industrial sites, construction), communities/NGOs; use cases include wildfire smoke monitoring, construction sites, schools.
- Deployment scale examples: citywide networks (Chicago ~280 sensors, Yerevan 170+, Paris 150, LAUSD 200, Breathe London 400+).

### Kaiterra (evidence layer A — directly observed)

From homepage and Data Platform page:

- Positioning: smart air quality monitors + data analytics for commercial buildings; WELL/LEED/RESET/Fitwel certification support; indoor + outdoor + in-duct monitors (Sensedge line).
- Data Platform ("Enterprise Air Quality Data Platform") features (directly observed):
  - Portfolio Overview: rank buildings by performance, track compliance against targets, portfolio health in one view.
  - Space Overview: per-building performance, filter by floor/space type, insights relative to outdoor conditions.
  - Live Data at Each Device: drill into individual readings, timelines, side-by-side parameter comparison.
  - Smart Alerts: customizable thresholds matched to building goals; reduce alert fatigue.
  - WELL Compliance Report: benchmark IAQ data against WELL v2 standards in one click; export formatted evidence.
  - Floorplan Visualizer: see air quality changes over space and time on a floorplan.
  - Diagnostics: out-of-the-box problem identification.
  - Weekly Digest Reports (email) and Kiosk display (share IAQ data transparently on screens).
  - Organization accounts: invite users, customize permissions per project.
- Hardware/ops: modular sensor design "simplifies calibration and maintenance"; module health viewable in web app with replacement notifications; placement guidance (breathing zone, coverage area per monitor, HVAC zones).
- BMS integration: BACnet/IP or Modbus for "automation and control" — monitoring feeds building systems but the product's own surface is data/alerts/reports, not control.
- FAQ-observed rules: monitors should be online for the platform to be useful; module lifespan varies and is user-visible.

### IQAir / AirVisual (evidence layer A — directly observed)

From homepage and AirVisual Platform page:

- Consumer app: real-time air quality + weather anywhere; pollutants PM2.5, PM10, NO₂, CO₂, SO₂; 80,000+ sensors/stations; 7-day air pollution and weather forecasts; air quality alerts; health recommendations; pollution news; purifier remote control.
- Aggregator posture: brings together data from governments, companies, and individuals (UNEP partnership); global city ranking; historical data for 5,000+ cities in 100+ countries; World Air Quality Report.
- Enterprise Dashboard feature matrix (directly observed):
  - Device management: real-time device status and AQI, detailed pollutant measurement, historic AQI and pollutant data, device status (Internet, battery), device settings, bulk settings, sorting/filtering, export device list, view devices on global map.
  - Organizational tools: location grouping, group devices into organizations, workspaces, add/remove members, assign device to another org.
  - Group management: group devices to get average data.
  - Alerts: email alert on device offline; email alert on data threshold.
  - Data publication: publish device as public (outdoor) station; web widgets for own devices and for city/station; full-screen monitor view.
  - Data export/API: device API, public station API, download historical aggregated hourly data, download full raw data, download validated station data.
- Tiering: free app; free dashboard for contributors (if devices public); paid dashboard with org tools.
- Segments: schools, offices, gyms, hospitality, hospitals, embassies.
- AQI⁺ (US AQI, metric) as the index layer; regional index selection visible in UI.

### PurpleAir (evidence layer B — structure only; JS app, body not reachable)

From navigation structure (directly observed structure, not operational detail):

- Real-Time Map as the flagship public surface; Register Your Sensor and Sensor Utility as onboarding/ops tools.
- Solutions segmented: Personal, Business, Education, Broadcasters, Government.
- Resources: Community, FAQ, Scientific Papers, Projects & Integrations, API Documentation — indicating a crowdsourced network with public data, third-party integrations, and an API.
- Posture: open public map; sensors owned by individuals feed a shared network.

**Limitation:** no operational detail (API fields, correction factors, data layers) was directly observed. Claims about PurpleAir below are restricted to what its site structure shows.

## Cross-product Comparison

| Dimension | PurpleAir | IQAir AirVisual | Clarity | Kaiterra |
|---|---|---|---|---|
| Identified monitoring points | registered sensors on public map | devices/stations + city stations | Node-S devices as "monitoring locations" | devices bound to spaces/floors/buildings |
| Pollutant parameters | PM focus (structure only) | PM2.5, PM10, NO₂, CO₂, SO₂ | PM2.5, NO₂ + modules (O₃, CO, NOx, PM10, black carbon, wind) | IAQ parameters (PM, CO₂, VOC, temp/humidity class), indoor/outdoor/duct |
| Time series + history | implied by map/API (not directly observed) | historic AQI/pollutant data; downloads | historical data, aggregations, CSV export | timelines, weekly digests, portfolio history |
| Current-conditions view | real-time map | app + live map + ranking | snapshot + interactive map | portfolio/space overview + live device data |
| Index (AQI) | map AQI (structure) | AQI⁺ central to app/ranking | OpenMap AQI/NowCast | not index-centric (raw parameters + thresholds) |
| Thresholds/alerts | not observed | email alerts (offline, threshold) | custom measurement + device-status alarms | smart alerts with customizable thresholds |
| Device/network health | sensor utility (structure) | device status (internet/battery), offline alerts | fleet status tracking, troubleshooting | module health + replacement notifications |
| Data quality / calibration | scientific papers (structure) | "validated station data" tier | collocation + calibration service, R²/MAE reports | modular sensor swap calibration, RESET data provider |
| Map | real-time map (core surface) | global map + city pages | interactive map in dashboard | floorplan visualizer (indoor spatial) |
| Roles/permissions | not observed | orgs, workspaces, members | Org Admin/Technician/Analyst/Observer/Guest | org accounts, per-project permissions |
| Public sharing | default public map | publish as public station, widgets | OpenMap + OpenData API, iFrame embed | kiosk display (private sharing) |
| API/export | API documentation (structure) | API + raw/validated downloads | REST API + CSV export | API (dev portal) |
| Reports | not observed | widgets, downloads | downloadable reports/summaries | weekly digest, WELL compliance report |
| Forecast | not observed | 7-day AQ + weather forecast | not observed | not observed |
| Weather context | not observed | weather alongside AQ | wind module / wind rose | outdoor-vs-indoor comparison |
| Control/integration | not observed | purifier control (adjacent) | not observed | BMS integration BACnet/Modbus (adjacent) |
| Hardware coupling | sells sensors | sells monitors; also aggregates third-party data | sells sensors (turnkey) | sells monitors; hardware-agnostic data platform claims |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product stops being an air quality monitoring application:

```text
Identified monitoring points (outdoor sites, spaces, or ducts where air is measured)
└── Pollutant measurements recorded as time series at each point
    └── Presentation of current conditions at those points
    └── Presentation of historical trends for those points
```

- **Monitoring point**: an identified, fixed location of measurement (station, sensor, room, duct). Without identified points, data has no spatial meaning.
- **Pollutant time series**: concentrations of defined air-quality parameters recorded over time. Without pollutant measurement, it is not air quality monitoring.
- **Current + historical presentation**: monitoring implies an ongoing observation loop — what is the air like now, and how has it changed. Remove history and it becomes a live indicator only; remove currency and it becomes a data archive.

§24 historical check: a legacy government reference-network data portal (stations + pollutant time series + current readings + history), a 2010s-era city AQ website, and a modern low-cost sensor network all satisfy this definition. Indoor IAQ products satisfy it with spaces as points. The definition does not depend on low-cost sensors, AQI indices, maps, or cloud delivery.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Air quality index (AQI)** computed from pollutant concentrations per a regional standard (US AQI, NowCast, etc.) — dominant in public-facing products (IQAir, Clarity OpenMap, PurpleAir map), absent as a center in building-focused products (Kaiterra uses raw parameters + thresholds).
- **Thresholds and alerts** — user-defined measurement thresholds and device-status conditions triggering notifications (Clarity, Kaiterra, IQAir all observed).
- **Device/network health management** — status, connectivity, battery/power, sensor/module health, offline detection, replacement workflows (all four).
- **Data quality machinery** — calibration, collocation against reference instruments, validation flags, accuracy reporting (Clarity R²/MAE collocation reports; IQAir "validated station data"; Kaiterra modular calibration; PurpleAir publishes scientific papers on correction).
- **Map as primary spatial surface** — outdoor products are map-centric; indoor products use floorplans. A presentation choice, not a definition.
- **Data access: API + export** — REST APIs, CSV/raw/validated downloads, widgets (all four).
- **Roles and permissions** — org-scoped roles for network operation (Clarity's five roles; Kaiterra per-project permissions; IQAir orgs/workspaces). Absent in consumer/community products.
- **Reports and summaries** — scheduled digests, compliance reports, stakeholder summaries (Kaiterra, Clarity, IQAir).

### L2 — Variant / Optional Structure

Depends on segment, posture, or business model:

- **Public vs private data posture** — crowdsourced public map (PurpleAir), opt-in public stations/widgets (IQAir), opt-in public OpenMap (Clarity), private enterprise (Kaiterra).
- **Aggregator vs own-network posture** — aggregating third-party/government data (IQAir's 80,000+ stations) vs operating own devices (Clarity, Kaiterra, PurpleAir).
- **Hardware-coupled vs hardware-agnostic** — turnkey sensor+cloud (Clarity) vs platform that can ingest multiple sources (IQAir, Kaiterra claims).
- **Indoor vs outdoor vs in-duct placement** — changes parameters (CO₂, VOC vs regional pollutants), spatial model (floorplan vs map), and rules (placement density, breathing zone).
- **Forecast and weather context** — 7-day AQ/weather forecasts (IQAir); wind data for source attribution (Clarity module).
- **Regulatory/certification alignment** — MCERTS certification (Clarity), EPA performance targets, RESET/WELL/LEED data-provider roles (Kaiterra), validated-data tiers (IQAir).
- **Adjacent control capabilities** — purifier control (IQAir app), BMS integration for automation (Kaiterra). Monitoring feeds control but control is not the monitoring Type's core.
- **Consumer app surface** — personal exposure view, health recommendations, news (IQAir).

### L3 — Vendor-specific (Research Notes only)

- Clarity "Sensing-as-a-Service" packaging; OpenMap brand; specific role names (Org Admin/Technician/Analyst/Observer/Guest).
- Kaiterra WELL Compliance Report; Floorplan Visualizer; Kiosk; weekly digest; BTL-certified BACnet integration; specific coverage-area guidance numbers.
- IQAir AQI⁺ branding; contributor tiering (free dashboard if devices public); UNEP partnership; World Air Quality Report.
- PurpleAir community/crowdsourced ownership model; Sensor Utility.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (what to remove/add to become the other) |
|---|---|---|
| Emissions Monitoring / CEMS | adjacent, often confused | CEMS measures at the **source** (stack/duct of a regulated facility) with defined reference methods for compliance reporting; AQM measures **ambient/environmental** concentrations at locations. Bind the measurement to a regulated emission source with compliance methods → CEMS. |
| Environmental Monitoring Platform | broader sibling | Multi-medium (air, water, soil, noise, weather) monitoring. Generalize the pollutant model to arbitrary environmental media → Environmental Monitoring Platform. AQM is the air-specific instance with pollutant-specific semantics (AQI, regional standards). |
| Environmental Water Monitoring | sibling | Same structural pattern (points + parameter time series + current/history) but water-quality parameters and water-specific rules. Different medium → different Type. |
| Building Management System / BMS | adjacent | BMS **controls** HVAC/equipment; AQM **observes**. When the product's primary loop becomes driving equipment rather than measuring and alerting, it drifts to BMS. Kaiterra integrates with BMS but its own surface remains measurement/alerts/reports. |
| Environmental Data Platform / Public Data Portal | adjacent | Portals publish existing data; AQM operates the measurement loop (devices, ingestion, QA). A portal without device/network operation is not AQM. |
| Weather application | adjacent presentation surface | Weather apps present meteorological conditions; pollutant measurement is not their managed object. AQ products often show weather as context (IQAir), not as core. |
| Industrial IoT Platform | generic substrate | IIoT handles arbitrary device telemetry; AQM adds pollutant-specific semantics: parameters, indices, calibration/collocation, health thresholds, regional standards. |
| Sustainability / ESG platforms | downstream consumer | ESG platforms consume environmental data for reporting; they do not operate pollutant measurement networks. |

Key boundary judgment: **Air Quality Monitoring is a distinct Type** (not merely a variant of Environmental Monitoring Platform) because the air-pollutant object model (parameters, indices, calibration practice, ambient siting) is stable and product-defining across all sampled segments. Indoor IAQ is treated as a **variant** (same core model; different point semantics and rules), consistent with products (Kaiterra, IQAir) that span both.

## Uncertainties

- PurpleAir operational details (API semantics, data-correction approach, map layers) were not directly observable (JS app). Its L1 contributions are inferred from site structure only and marked accordingly.
- Airly, AQMesh, Vaisala, Aclima were not sampled; the four-product sample reached saturation for the core model, but regional regulatory-network products (e.g., national EPA data systems) were not directly fetched — the L0 was checked against them conceptually (§24) rather than by direct observation.
- The exact regulatory status of low-cost sensor data (indicative vs reference-grade) varies by jurisdiction; asserted only qualitatively.
- Whether a future taxonomy pass should split "Indoor Air Quality Monitoring" as its own Type remains open; current evidence supports variant status.

## Final Synthesis

An Air Quality Monitoring application is software that operates a loop over **identified monitoring points**: it ingests **pollutant measurements** at those points as **time series**, maintains them with **data-quality machinery**, presents **current conditions and historical trends**, and drives **threshold-based alerting** and **data distribution** (API, export, reports, optional public publication). The defining core is small (points + pollutant time series + current + historical presentation). Indices, alerts, device health, calibration, maps, roles, and APIs are standard mature capabilities; public-vs-private posture, aggregation, hardware coupling, indoor/outdoor scope, forecasts, and control integrations are variants. The Type is distinct from source-level emissions monitoring (CEMS), multi-medium environmental monitoring, water monitoring, and control-oriented building systems.
