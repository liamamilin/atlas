# Research Notes — Agricultural IoT Platform

## Research Goal

Understand what an **Agricultural IoT Platform** is as an Application Type: the core objects it manages, the workflows users perform, the interfaces it presents, the rules that shape its behavior, and — most importantly — where it begins and ends relative to neighboring Types (Irrigation Management, Precision Agriculture Platform, Agricultural GIS, Farm Equipment Telematics, Greenhouse Management, Livestock Management, Industrial IoT Platform, Environmental Monitoring Platform, SCADA).

## Initial Boundary

Working hypothesis before research:

- Core use: connect field-deployed sensing devices (weather stations, soil probes, water meters, insect traps, cameras, climate sensors) to a cloud platform where farm decision-makers monitor conditions, receive alerts, and sometimes control equipment remotely.
- Primary users: growers, farm/irrigation managers, agronomists/consultants, greenhouse operators.
- Nearest neighbors: Irrigation Management (decision/schedule-centric), Farm Equipment Telematics (machine-centric sibling), Precision Agriculture Platform / Agricultural GIS (spatial-analysis-centric), Industrial IoT Platform / Environmental Monitoring Platform (same structural family, different domain), SCADA (control-centric industrial ancestor).
- Unknowns: is remote control/actuation definitional or variant? Is agronomic intelligence (disease models, ET, recommendations) definitional or common? Does the L0 hold for older radio-telemetry-era products? Is "Agricultural IoT Platform" a real market category label?

## Research Questions

1. What are the core "things" in the system? (devices, sensors, gateways, sites/zones, measurements, alerts)
2. How do devices get enrolled, organized, and located (farm → field/room/zone containers)?
3. How does telemetry flow into the platform (connectivity substrates, gateway vs direct, schedules)?
4. What does the monitoring surface look like (map view, dashboards, time series, accumulators)?
5. How does alerting work (thresholds, models, notification channels)?
6. Where does remote control/actuation appear, and is it definitional?
7. What device-fleet management exists (status, health, battery, last-contact, configuration)?
8. What agronomic intelligence is layered on top (disease models, ET, degree days, recommendations, AI)?
9. How do integrations/APIs and third-party sensors/devices work?
10. Where are the boundaries vs the neighboring Types above?

## Representative Products

Selected for market representation + documentation reach + different product philosophies + different customer tiers and production contexts:

| Product | Philosophy / tier | Evidence level reached |
|---|---|---|
| Semios | enterprise sensor network + field services + agronomy service for specialty/perennial crops | Tier 2 (solution pages with operational depth) |
| Pessl Instruments (METOS / FieldClimate) | hardware-ecosystem + long-running cloud platform (since 2005), global, crop/animal/city sectors | Tier 2 (product, platform, and app pages with operational feature lists) |
| CropX | soil-sensor-first, grower/dealer self-serve digital agronomy platform, global | Tier 2 (product pages + detailed official FAQ describing how the system works) |
| Growlink | controlled-environment (CEA) cultivation platform, control/automation-first (sense → decide → act loop) | Tier 2 (product/OS pages; marketing-tier, no manual fetched) |

Rejected / not sampled: Davis WeatherLink (consumer weather focus, thin ag documentation), Arable / Teralytic (single-device science-first, smaller documentation footprint), Netafim NetBeat (better classified near Irrigation Management), generic industrial IoT platforms (out of domain).

## Sources

- Semios — home: https://semios.com/ (fetched 2026-09-06)
- Semios — Irrigation Management solution: https://semios.com/solutions/water-management/ (fetched 2026-09-06)
- Pessl Instruments — home: https://metos.at/ → https://metos.global/en/ (fetched 2026-09-06)
- Pessl Instruments — FieldClimate platform page: https://metos.global/en/fieldclimate/ (fetched 2026-09-06)
- CropX — home + official FAQ ("What is CropX?", "How exactly does it work?", "What makes CropX unique?"): https://cropx.com/ (fetched 2026-09-06)
- CropX — Farm Data Connectivity: https://cropx.com/cropx-system/farm-data-connectivity/ (fetched 2026-09-06)
- Growlink — home: https://growlink.com/ (fetched 2026-09-06)
- Growlink — GrowlinkOS + Blueprints: https://growlink.com/growlink-os.html (fetched 2026-09-06)

**Source-access limitations:** vendor *help centers / user manuals* (device enrollment flows, exact alert-configuration UIs, protocol specifications, numeric limits) were not fetched; evidence is Tier 2 product/solution documentation, in places unusually operational (CropX FAQ, FieldClimate feature lists, Semios water page). No precise numbers (device counts per gateway, battery life, polling intervals, notification latencies, pricing) are asserted anywhere except where a fetched page states them. Growlink evidence is marketing-tier; its control-loop structure is well documented but operational depth is lower. Historical radio-telemetry-era products (e.g., Adcon Telemetry lineage) were not fetched; the historical fit of the L0 is an inference recorded in Boundary Findings, not a direct observation.

## Product A — Semios

### Key observations (evidence layer A unless noted)

- Positioning: "On-farm solutions backed by trusted field services"; an "all-in-one ag service provider" for pest, weather, and irrigation; specialty crops (almonds, apples, cherries, citrus, grapes, pears, pistachios, stone fruit, walnuts) — perennial/orchard/vineyard segment.
- Solution stack (all under one app): Climate Monitoring ("understand the climate conditions on every acre", in-canopy); Mating Disruption (variable rate) & Insect Pest Management; Disease Management ("anticipate and pinpoint disease risk"); Frost Management ("remotely monitor frost conditions to act quickly"); Irrigation Management ("monitor, control, and automate your irrigation"); Plant Stress Monitoring (dendrometers); Alert and Reporting Tools; Field Services.
- Field services: vendor team handles installation, remote monitoring, and maintenance ("hands-off, hassle-free setup"; "IoT devices serviced" counter on homepage). Indicates a managed-service implementation of the same device-fleet concept.
- Irrigation page (operationally specific):
  - Monitor: "filter station and line pressure in real-time"; flow meter ("record water usage… simplify reporting"); weather via "on-site or virtual weather station".
  - Schedule/automate: "remote pump and valve scheduling through integrations with WiseConn and Nelson systems"; irrigation scheduler for "continuous or pulse irrigation"; "scheduling irrigation events for many zones at once"; "send your planned irrigation schedule for automatic execution in the field with our WiseConn DropControl integration"; "Compare irrigation activity alongside your plan to ensure it was executed properly."
  - Decision inputs: ET readings + 15-day forecast; soil moisture; soil salinity; plant stress (dendrometers); fruit-growth predictive models.
  - Auto-calibration: "system that automatically adapts to your soil's response to irrigation"; automatic calculation of wilting point and field capacity by soil type; "Infiltration Map Tool" for water movement through soil; available water content at various depths.
- Observation (layer B): the platform combines a physical device network, telemetry monitoring, model-based alerting (frost/disease), remote actuation through third-party control integrations, and human field services — the full loop for perennial crops.

## Product B — Pessl Instruments (METOS / FieldClimate)

### Key observations

- Hardware fleet (Tier 2 catalog): weather stations & dataloggers (METOS 5, iMETOS 3.3, METOS STREMO, miniMETOS, METOS VWS, hybrid station extension), iSCOUT (insect camera trap), CropVIEW (field camera), METOS TSM, iMETOS Trackers, Dualex / N-Pilot (plant sensors); sensor lines: precipitation, temperature, leaf, light, wind, barometer, soil temperature, soil moisture, water, plant.
- FieldClimate platform: "introduced in 2005 as the first-ever web platform for collecting and displaying agro-meteorological data for tens of thousands of weather stations and sensors installed worldwide" (vendor claim). It "gathers, calculates, analyses and graphically presents the data from measurements done by the sensors in the field."
- Highlighted platform features (verbatim-level): "Remote access to all in-field devices"; "Display current conditions from any device sensor"; "Map view of all devices for chosen variable"; "Site-specific forecasting — simple and detailed"; "Assess your soil moisture by sensor depth"; "View insects captured in your iSCOUT trap."
- Solution layers (subscription-licensed): weather monitoring & forecast; soil moisture monitoring; plant disease models; insect monitoring; satellite imagery; work planning tools (field accessibility, tillage ability, sowing window, plant protection, harvest window); yield prediction; dairy and poultry stress calculations; accumulator tools (degree days, chilling units, rain sum); data statistics & modelling; "Notifications & alarms"; data storage & API.
- Mobile apps: FieldClimate for iOS/Android ("field control… in the palm of your hand").
- 3rd-party integrations via API: FieldNET by Lindsay, John Deere, Davis Instruments, Azure FarmBeats, Horta, RIMpro, xarvio, Myirrigation "and many more."
- Sectors: "Crop growing, animal breeding, smart cities, OEM" — the platform extends beyond agriculture, confirming that the engine is domain-agnostic while the agriculture specialization is in devices, data models, and agronomic layers.
- User support: manuals/firmware user area, Freshdesk ticketing, distributor network.

## Product C — CropX

### Key observations

- Positioning: "complete digital agronomy platform"; FAQ: hardware + software + dealer tools; users are "farmers, dealers, agronomic advisors and agribusinesses"; 70+ countries, 100+ crop types (vendor claims).
- Official "how it works" (FAQ): "We continuously collect and analyze data from a variety of in-field sensors (such as soil sensors, ET sensors, weather stations – both our own and third party), satellites, and farm machinery" → "proprietary, research-backed agronomic models, data science, and AI tailored to your specific crop, field and weather conditions" → "up-to-date, accurate, and actionable recommendations" (when/how much to irrigate, fungicide type, root/canopy development).
- Hardware lines (FAQ): soil sensors (moisture, temperature, EC, salinity) at multiple depths; ET sensors; weather stations (WS); rain gauges (RG); "Telemetry / communication gateway devices (TD line) with built-in cellular connection to connect all these devices to the cloud"; in-field nitrate sensor in development.
- Farm Data Connectivity page: "Weather Stations and Rain Gauges — automatically collect data from on-farm sources"; "Third-Party Sensors — connect sensors from other manufacturers"; "Irrigation Equipment — monitor and control irrigation equipment from the CropX platform"; "Machine Data — automatically import data from almost any farm machinery"; "Partner Connections" (Reinke, John Deere Operations Center, FieldView, Talgil). Data also flows *out* ("farmers can share practices and results with their suppliers and customers"); bi-directional John Deere Operations Center integration (view CropX soil-sensor data in OC; import field data to simplify field set-up).
- Software modules (FAQ): "managing installs, status, health of field devices and sensors, both CropX and third party supported"; managing farm/field/crop/soil data; season plans & crop rotation; monitoring crop water use and scheduling irrigations; nutrition/salinity/leaching monitoring; disease risk; effluent systems and pumps; machine data and partner connections; dealer advice communication; tasks/activities/schedules; reports (seasonal review, audit, compliance); EU extras (financials, soil tests, crop recording/registration, inventory, contracts).
- Science models (FAQ): crop growth models (phenological stages, canopy, root depth from GDD/days-since-planting); "sensor auto-calibration and auto-set-point detection models, for field capacity, wilting point, refill points"; disease lifecycle/risk models; irrigation & water use models; leaching detection; satellite image processing.
- Observation (layer B): device fleet + connectivity gateway is the substrate; everything else (agronomy, records, dealer channel) is layered on top — a "sensors-first, all-in-one" implementation.

## Product D — Growlink

### Key observations (marketing-tier; structure well documented)

- Positioning: "Agentic Cultivation Platform for Commercial Growers" (cannabis/greenhouse CEA segment). Operating loop: "Sense → Decide → Act → Improve."
- Sense: "Substrate and climate data from every room, continuously" (TerraLINK substrate sensors, ClimateLINK climate sensors).
- Act: "Climate, lighting, irrigation, and nutrient delivery controlled through GrowlinkOS — executing your Blueprint strategy precisely, every room, every run, without manual intervention"; Core Controller hardware ("industrial wiring and Metz BACnet I/O").
- Blueprints (operating standard object): define "climate, irrigation, fertigation, lighting, tasks, and targets in one repeatable operating standard" — climate strategy (temperature, humidity, VPD, CO₂, lighting targets by growth stage), irrigation strategy (drybacks, shot timing, EC targets), fertigation strategy, team instructions (tasks by day/growth stage), automation logic ("rules, thresholds, and conditional triggers connected to your Blueprint").
- Decide: Nova AI agent — monitors active Blueprint, "detects drift, and recommends what to adjust"; plan-vs-actual comparison (e.g., "Room 4 drifted from target VPD for 18 hours… Irrigation events also ran 12% below the Blueprint target"); alerts and insights.
- Prove: dashboards/reporting "show how each decision impacted yield, consistency, labor, and cost" per run/room/cultivar.
- Builder Platform: APIs ("connect facility, crop, device, and performance data"), apps, AI workflows; installation/commissioning services.
- Observation (layer B): in CEA the same structural family appears but with the control loop closed tightly and an explicit "operating standard" object (Blueprint); the crop-steering domain replaces field weather as the dominant concern. Growlink demonstrates the *automation-first* pole of the Type.

## Cross-product Comparison

| Dimension | Semios | Pessl FieldClimate | CropX | Growlink |
|---|---|---|---|---|
| Domain / production context | perennial specialty crops (orchard/vine), open field | open-field crops + animal + smart cities + OEM | row crops, broadacre, global, many crop types | controlled-environment (indoor cannabis/greenhouse) |
| Device population | in-canopy climate, soil moisture/salinity probes, dendrometers, flow meters, pressure sensors, digital insect traps, weather stations | weather stations/dataloggers, soil probes, leaf/water/plant sensors, iSCOUT insect camera traps, CropVIEW cameras, trackers | soil sensors, ET sensors, weather stations, rain gauges + third-party sensors | substrate + climate sensors (dense per-room) |
| Connectivity substrate | vendor-managed device network + field services; integration with third-party irrigation control (WiseConn, Nelson) | vendor stations (various comms) + 1NCE cellular partnership announced; API out | vendor telemetry gateway (TD line) with built-in cellular; third-party sensors; partner connections | Core Controller (industrial I/O, BACnet) + sensors |
| Enrollment & fleet management | vendor field services install/maintain; "IoT devices serviced" | "remote access to all in-field devices"; manuals/firmware user area | "managing installs, status, health of field devices and sensors, both CropX and third party" | installer/commissioning services; controller-based |
| Monitoring surface | all-in-one app; real-time pressure/flow; climate; map-ish tools (infiltration map) | current conditions from any device sensor; **map view of all devices for chosen variable**; charts; soil moisture by depth | platform overview of field conditions; per-field monitoring; dashboards | per-room dashboards; drift vs Blueprint |
| Alerting | "Alert and Reporting Tools"; frost monitoring "to act quickly" | "Notifications & alarms" | recommendations/alerts via app (FAQ: monitoring + advice) | drift alerts; Nova insight notifications |
| Agronomic intelligence | disease models; ET + 15-day forecast; fruit-growth predictive models; auto-calibration of soil set points | disease models; degree days/chilling/rain accumulators; work windows (tillage/sowing/spray/harvest); yield prediction; dairy/poultry stress | agronomic models + AI → recommendations (irrigation, disease, nutrition, leaching, salinity) | Blueprint targets by growth stage; Nova AI recommendations |
| Remote control/actuation | yes — pump & valve scheduling via WiseConn/Nelson integrations; "send schedule for automatic execution" | not confirmed on fetched pages (monitoring-centric presentation) | "monitor and control irrigation equipment from the CropX platform" | yes — automation-first: climate/lighting/irrigation/fertigation executed by system |
| Plan-vs-execution verification | "Compare irrigation activity alongside your plan" | — (not on fetched pages) | — (not on fetched pages) | Nova plan-vs-actual drift detection |
| Integrations/API | WiseConn, Nelson (control side) | API; FieldNET/Lindsay, John Deere, Davis, Azure FarmBeats, xarvio… | Reinke, John Deere OC (bi-directional), FieldView, Talgil; share data out | Builder Platform APIs/apps |
| Mobile surface | all-in-one app | FieldClimate iOS/Android | app + web | dashboards; apps via Builder |
| Service model | managed service (vendor installs/maintains) | distributor network + subscriptions | self-install sensors + knowledge base + 24/7 support | installer/commissioning + advisory services |
| Data out / reporting | reporting tools; water-usage reporting | data storage & API; statistics | reports for audit/compliance; data sharing with supply chain | harvest analytics per run/room/cultivar |

### Stable commonalities (layer B, cross-product)

1. **Connected field device fleet** — every product is built around physically deployed, individually identified devices (sensors, stations, traps, controllers) enrolled in the platform and organized by location/site (field, zone, room, barn).
2. **Telemetry into a central platform** — measured conditions flow from devices into the platform (directly or via gateway/controller) and persist as history; "automatically collect data from on-farm sources" (CropX), "collecting and displaying agro-meteorological data" (Pessl).
3. **Condition monitoring surface** — current conditions plus historical time series rendered per device/location; map views and dashboards appear in every product ("map view of all devices for chosen variable" — Pessl; per-room dashboards — Growlink; per-field monitoring — CropX; all-in-one app — Semios).
4. **Alerting loop** — user-visible notifications when conditions warrant attention ("Notifications & alarms" — Pessl; Alert and Reporting Tools / frost alerts — Semios; drift alerts — Growlink; monitoring-with-alerts — CropX).
5. **Device-fleet health as a first-class concern** — device status/health/last-contact surfaces (CropX explicit; Pessl remote device access; Semios vendor-serviced fleet; Growlink commissioning) because unattended devices fail silently.
6. **Agronomic intelligence layered on telemetry** — models and accumulators turn raw readings into decision support (disease models, ET, degree days, growth stages, recommendations) in all four products, though depth and branding vary.
7. **Integrations in both directions** — third-party sensors/equipment/partner data in; data/API exports and partner platforms out (every product).
8. **Mobile companion** — phone/tablet app for field access and push alerts (all four).
9. **Site/context organization** — devices are placed in a spatial or structural container (farm/field/zone/room), and readings are meaningful only relative to that location.

### Product-specific findings (layer A, single-product — keep out of canonical core)

- Semios: variable-rate mating disruption service; WiseConn/Nelson pump-valve control integrations; dendrometer-based fruit-growth prediction; virtual weather station; managed field-service fleet.
- Pessl: iSCOUT insect camera traps with in-app insect viewing; CropVIEW cameras; work-window planners (tillage/sowing/spray/harvest); dairy & poultry stress calculators; subscription shop; smart-city/OEM sectors; 2005 "first web platform for agro-meteorological data" claim.
- CropX: TD telemetry gateway hardware line with built-in cellular; sensor auto-calibration/auto-set-point models (field capacity, wilting point, refill points); bi-directional John Deere Operations Center sync; EU farm-management extras (financials, crop registration, inventory); Cool Farm Platform integration (Scope 3 reporting, news item); SCIO acquisition (news item).
- Growlink: Blueprint object (repeatable operating standard incl. tasks and automation rules); Nova AI agent; Core Controller with BACnet I/O; "Agentic Cultivation" framing; Builder Platform for third-party apps.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

1. **Connected agricultural device fleet** — identified sensing (and optionally actuating) devices physically deployed in agricultural production environments (fields, orchards, greenhouses/rooms, barns, water infrastructure), enrolled in the platform as individually managed records with a location and a connectivity status.
2. **Telemetry into a central platform** — measured conditions flow from the devices into the platform over some network (provided or integrated by the platform) and persist as historical data.
3. **Condition monitoring surface** — current and historical conditions rendered per device/location (map, dashboard, charts) for farm decision-makers.
4. **Alerting loop** — the platform actively notifies responsible people when conditions (or model outputs derived from them) cross thresholds that warrant attention.

Remove any one and the Type collapses: remove (1) → a generic weather/data dashboard; remove (2) → a manual record-keeping app; remove (3) → a raw telemetry data pipeline rather than an application; remove (4) → a passive logger viewer rather than a monitoring platform (the monitoring loop requires that the platform comes to the user, not only the reverse).

Agricultural specialization lives in (1)+(3): the devices measure agronomically meaningful conditions (weather, soil, water, plant, pest, animal-environment), the locations are production sites, and the users are people responsible for crops or livestock.

### L1 — Common Mature Structure

- Device lifecycle & fleet health: enrollment/installation (self-install or vendor service), naming, placement, configuration, remote access, status/health surfaces (connectivity, last contact), maintenance workflows.
- Site/context organization: farm → field/zone/room containers; device placement within them.
- Broad sensor catalogs: weather (air temp, humidity, rain, wind, radiation), soil (moisture/temperature/EC/salinity at depth), water (flow, pressure, tank levels), plant (stress, canopy), pest (insect traps, cameras), animal-environment (barn climate, heat stress).
- Agronomic decision-support layers: disease/pest models, evapotranspiration, degree-day and chilling accumulators, growth-stage tracking, recommendations (e.g., irrigation timing/amount), auto-calibration of sensor-derived set points.
- Reporting & data out: reports (seasonal review, water use, compliance), API/export, partner-platform sharing.
- Integrations: third-party sensors/equipment/partner platforms in; machinery and irrigation-control systems out.
- Mobile companion app with push notifications.
- User/role organization (grower, agronomist/consultant, dealer) and sharing of farms/rooms with advisors.
- Multi-season persistence: history supports season-over-season comparison.

### L2 — Variant / Optional Structure

- Control/actuation depth: none (monitor+alert only) → remote scheduling/switching of existing irrigation equipment via integrations → full closed-loop automation (climate/lighting/fertigation controllers). CEA products sit at the automation pole; open-field products at the monitoring pole.
- Connectivity substrate: cellular gateway backhaul (CropX TD line evidenced), controller-based backhaul (Growlink evidenced), vendor device networks (Semios/Pessl; protocol specifics not verified in this pass) — implementation detail, not definition.
- Production-context emphasis: open-field perennial (frost/pest/disease), row-crop (soil/water), CEA (climate/substrate steering), livestock (barn climate/stress), water infrastructure (tanks/pumps/canals).
- Business/service model: self-install self-serve vs vendor-managed field services vs dealer channel.
- Intelligence depth: raw data + thresholds → vendor agronomic models → AI agents (drift detection, recommendations).
- Sector breadth: agriculture-only vs multi-sector platforms (animal, smart cities, OEM).
- Regional/regulatory extras (e.g., EU crop recording, compliance reporting).
- Business model: hardware sale + subscription, license tiers, free tiers.

### L3 — Vendor-specific (stays out of the final document)

- Semios: WiseConn DropControl, Nelson integrations, mating-disruption services, dendrometer fruit models, virtual weather station.
- Pessl: METOS hardware brand lines (iMETOS, METOS 5, STREMO, miniMETOS, iSCOUT, CropVIEW, TSM, Dualex, N-Pilot), FieldClimate brand, subscription shop, 1NCE partnership, Azure FarmBeats/xarvio/RIMpro integration names, 2005 first-mover claim.
- CropX: SV/ET/WS/RG/TD hardware lines, Cool Farm Platform integration, SCIO acquisition, John Deere OC bi-directional integration specifics, EU FMS module list.
- Growlink: Blueprint, Nova, Copilot, Core Controller (Metz BACnet I/O), TerraLINK/ClimateLINK, "Agentic Cultivation" trademark, Builder Platform.
- Vendor ROI/yield claims (Semios counters, CropX case studies, Growlink 54%/50%/36% figures) are marketing claims — excluded.

## Vendor-specific Findings

See L3 above. Marketing numbers ("tens of thousands of stations", "70+ countries", "20,000+ users", yield/water ROI percentages) are vendor claims recorded here only.

## Boundary Findings

1. **vs Irrigation Management** (sibling under §20): irrigation management centers the *irrigation decision itself* — water balance, scheduling, prescriptions — regardless of where the data comes from; an Agricultural IoT Platform centers the *device fleet and the telemetry/monitoring loop*, regardless of which decision the data feeds. Overlap is real: soil-moisture networks feed irrigation scheduling (Semios irrigation module; CropX irrigation planning), and Semios explicitly spans both. Structural test: remove the device fleet → an irrigation-management product can still exist (ET data from public sources); remove irrigation scheduling → the IoT platform still monitors frost, pest, disease, climate. Working distinction: center of gravity (sensing backbone vs water decision). A gradient, not a wall.
2. **vs Farm Equipment Telematics** (sibling under §20): both are "connected device fleet + telemetry + monitoring/alerting" by structure; the boundary is the *device population* — stationary/environmental condition sensors (weather, soil, water, pest, climate) vs moving machines/vehicles (location, engine, fuel, machine state). Telematics data can feed into an IoT platform; an integrated product spanning both is a platform family, not a different Type.
3. **vs Precision Agriculture Platform / Agricultural GIS** (siblings under §20, per prior research): precision-ag/ag-GIS center the *spatial land base* — field polygons, layers, zones, prescriptions — with data geometry of maps; the IoT platform centers *point devices and time series* — readings from fixed locations over time. Complementary rather than competing: a prescription may be built in a precision-ag platform from sensor data delivered by an IoT platform. Some vendors bundle both; the structural cores remain distinct.
4. **vs Industrial IoT Platform / SCADA** (§16) and **Environmental Monitoring Platform** (§21): all are the same structural family (device fleet + telemetry + monitoring + alarms; SCADA adds supervisory control). The Agricultural IoT Platform is the agriculture-domain specialization: agronomic semantics, seasonal/crop framing, farm-scale deployments, low-power remote sites. Observation: the directory has no generic "IoT Platform" leaf (only Industrial IoT Platform, IoT Security); Pessl's own positioning spans crop/animal/smart cities/OEM, showing the engine is domain-agnostic. Same taxonomy situation as agricultural-gis vs government-gis/utility-gis.
5. **vs Greenhouse Management / Livestock Management** (§20 siblings): those Types center *operational management* of the production unit (records, batches, inventory, labor, sales); the IoT platform provides the sensing/control backbone they may consume. Growlink approaches the boundary from the CEA side — its control loop is tight, but its core remains sense→decide→act on environment, not operational records; it remains within this Type as the automation-first variant.
6. **Naming observation:** like "agricultural GIS", "Agricultural IoT Platform" is rarely used as a market category label; products are marketed as sensor networks, monitoring platforms, ag telemetry, or cultivation automation. The leaf is best understood as the *device-connectivity-structured segment* of agricultural software — defined by structure (fleet + telemetry + monitoring + alerts), not vendor vocabulary.
7. **Historical / market-sample check (§24):** the L0 holds for the radio-telemetry era (late-20th-century ag weather-station networks with base stations, registered stations, dial-up/radio backhaul, alarms) and for modern LoRaWAN/cellular networks; it does not require cloud-native AI, smartphone apps, remote control, or any particular protocol. Conversely, removing the device fleet (using only public weather data) leaves a decision-support product, not an IoT platform. The definition is not over-fitted to the current cloud/AI era; the historical fit is an inference (historical products were not fetched), recorded as such.

## Uncertainties

- No Tier-1 help-center/manual fetches: exact enrollment flows, alert-configuration mechanics, protocol lists, and numeric limits (devices per gateway, battery life, polling intervals) are **not asserted** anywhere in this research or the final document.
- Remote-control depth per product is unevenly documented: confirmed for Semios (via integrations) and CropX ("monitor and control irrigation equipment") and Growlink (automation-first); not confirmed on fetched Pessl pages. Market-wide prevalence of actuation is therefore treated as variant, not common-defining.
- Growlink evidence is marketing-tier; operational details beyond the Blueprint/automation loop are unverified.
- Historical radio-telemetry products were not fetched; their fit to the L0 is reasoned, not observed.
- Whether the market would merge this leaf into Irrigation Management or Precision Agriculture Platform is not a live risk (centers of gravity differ clearly), but the sibling gradient with Farm Equipment Telematics (same engine family) is genuine and recorded.

## Final Synthesis

An Agricultural IoT Platform is the agriculture-domain specialization of an IoT monitoring platform: a system whose world is a **connected fleet of devices deployed in agricultural production environments**, streaming **telemetry into a central platform**, where decision-makers **monitor current and historical conditions per site**, receive **alerts** when conditions warrant action, and — in some products — **act remotely** on connected equipment. Everything commonly bundled (agronomic models and accumulators, recommendations, fleet-health dashboards, integrations/APIs, mobile apps, roles, reports) is standard mature structure; connectivity substrate, sensor population, control depth, service model, and AI depth are variants. The Type's sharpest boundaries are: device fleet vs water decision (Irrigation Management), condition sensors vs machines (Farm Equipment Telematics), point devices + time series vs spatial land base (Precision Agriculture Platform / Agricultural GIS), and farm domain vs industrial/urban domains (Industrial IoT Platform / Environmental Monitoring Platform).
