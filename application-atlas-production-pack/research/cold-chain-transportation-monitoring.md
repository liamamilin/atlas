# Research Notes — Cold Chain Transportation Monitoring

Research date: 2026-09-07
Slug: `cold-chain-transportation-monitoring`
Directory leaf: Cold Chain Transportation Monitoring (§18 Transportation, Mobility & Logistics)

---

## Research Goal

Understand what software of this Type actually is and how it works, from real products:

> What does a "cold chain transportation monitoring" application monitor, against what, with what machinery, for whom, and what does it produce — and where does it end and neighboring Types (shipment visibility, vehicle telematics, food cold chain management, environmental monitoring) begin?

## Initial Boundary (hypothesis before research)

- Core use hypothesis: monitor temperature (and related conditions) of temperature-sensitive cargo **while it is being transported**, detect excursions against a defined requirement, alert someone who can intervene, and retain a record usable as delivery evidence.
- Likely users: shippers (food, pharma, chemicals), carriers/3PLs, QA/quality teams, dispatchers, drivers, receivers.
- Likely confusions:
  - Shipment Visibility Platform (location/status of any shipment — not condition-vs-requirement)
  - Vehicle Telematics Platform (vehicle/asset health — not cargo condition)
  - Food Cold Chain Management (§20 sibling — food-industry-wide, includes facilities)
  - Environmental Monitoring Platform (§21 — facility-centric, fixed locations)
  - TMS (transport planning/execution — not condition observation)
  - Dangerous Goods Transportation Management (sibling special-cargo type — hazard compliance, not condition preservation)
- Unknowns going in: the central monitored object (shipment vs trip vs asset vs logger); how requirements are configured and bound; what delivery evidence looks like; how much is hardware vs software; whether "release decision" (pharma) is part of the Type.

## Research Questions

1. What is the central monitored object — shipment, trip, container, vehicle, or logger?
2. How is the temperature requirement defined, and how is it bound to cargo/shipments?
3. How does condition data enter the system (real-time trackers, USB loggers, reefer telematics, gateways)?
4. What does live monitoring look like (map, dashboard, alerts, escalation, managed services)?
5. What happens on excursion — who is told, what can they do, how is it documented?
6. What evidence is produced at delivery (reports, audit trails, release decisions)?
7. How are monitoring devices managed (activation, calibration, battery, reuse/return)?
8. Which transport modes and cargo levels (vehicle vs container vs box) are covered?
9. Which roles use it and on which surfaces?
10. Where are the boundaries vs Shipment Visibility, Telematics, Food Cold Chain Management, Environmental Monitoring?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer layers:

| Product | Pole | Why selected |
|---|---|---|
| **Tive** | shipment-centric real-time IoT tracker platform (food + pharma + high-value) | modern pure-play; rich public documentation; multi-industry |
| **Controlant** | pharma-grade platform + reusable devices + 24/7 managed monitoring + release automation | regulated-enterprise pole; managed-service philosophy |
| **Sensitech (Carrier)** | heritage monitoring-device family + SensiWatch platform + release evaluation (Lynx FacTOR) + professional services | 35+ year heritage vendor; widest device spectrum incl. historical forms |
| **Thermo King TracKing (ConnectedSuite)** | reefer-equipment-native telematics | equipment-manufacturer pole; shows the telematics seam |

Rejected/considered: Copeland (Emerson) Go Real-Time — official pages returned HTTP 403 twice; abandoned per source-access rules. Tive's own framing ("shipment visibility platform" with cold chain as a use case) was used carefully so the platform's broader visibility scope did not leak into the Type definition.

## Sources

All fetched 2026-09-07 (Tier 1/2 official vendor pages):

- Tive — homepage; `/solutions/cold-chain-monitoring`; `/platform-features`; `/smart-alerts` (tive.com)
- Controlant — homepage; `/platform`; `/go` (controlant.com)
- Sensitech — homepage; `/en/solutions/cold-chain/`; `/en/products/sensiwatch-platform/`; `/en/solutions/lynx-factor/`; `/en/products/monitors/` (sensitech.com)
- Thermo King — homepage; `/na/en/connectedsuite-telematics/tracking-telematics.html` (thermoking.com)

Source-access limitation: Copeland cold-chain pages (copeland.com) returned 403 on both attempts; no claims about Copeland products are made anywhere. Help-center subpages (e.g., support.controlant.com article referenced from the platform page) were not fetched; platform-level claims for Controlant rely on its official marketing/product pages, so operational precision is kept low. No numeric limits, prices, or device specs are asserted in the final document beyond what vendor pages directly state.

---

## Product Observations

Evidence tags: **[A]** directly observed on an official page of that product; **[B]** cross-product commonality (observed in multiple samples).

### Tive

Key observations (all [A] unless noted):

- Product family: real-time trackers (Solo 5G, Solo Pro, Solo Lite — disposable), Tive Tag (paper-thin **passive** temperature logger), Tive Seal, accessories; tracker return program exists.
- Sensors: temperature, humidity, light, shock, tilt; location via cellular/GPS/WiFi. Vendor states range "−200°C to 60°C with probes" covering ambient to cryogenic (dry ice/cryo probes on higher models).
- Platform: shipment creation with route; **shipment templates for regular lanes**; reporting-frequency control trading detail vs tracker battery life.
- Alerts: real-time condition alerts (temperature, humidity, light, shock); **configurable thresholds per product/temperature profile**; alert types described: single-excursion, **cumulative time-out-of-range**, **mean kinetic temperature (MKT)**; alerts shareable "with the teams responsible for taking action".
- Smart Alerts (AI): **Smart Route Deviation** (auto-generates expected routes from historical data, flags deviations as theft/timing/compliance risk); **Smart Reefer Cycle Detection** (detects start/stop cycling behavior from temperature patterns even when thresholds are not exceeded — a documented spoilage cause).
- Geofencing/location alerts: inbound, delayed, stopped too long; route deviation; device connectivity and battery alerts.
- Collaboration: share shipment view via URL, white-label tracking links, per-user view/edit/contribute permissions.
- Reporting/analytics: "clear, verifiable reports" for claims/disputes; carrier and lane comparison/benchmarking; custom dashboards.
- **24/7 live monitoring service**: expert monitoring team collaborates with customer and carrier when issues arise (e.g., customer story: reefer set to cycle instead of continuous — intervention saved a load).
- Compliance/evidence: complete time-stamped digital audit trail per shipment; supports FSMA, FDA 21 CFR Part 11, EU Annex 11; 3-point NIST-traceable calibration certificate ships with trackers; ISO 9001 / SOC 2 Type 2 / ISO 27001; GxP/GAMP 5 development posture; on-device "Product Release Assist" on the pharma-grade tracker.
- Industries: food & beverage (produce, seafood, meat, floral, dairy, frozen, beverage), life sciences (biologics, vaccines, cell & gene, clinical trials, specialty), high-value goods, transportation & logistics.
- Framing: Tive self-describes as shipment visibility ("track shipment location and condition in real time") with cold chain monitoring as a named use case — the cold-chain slice is condition-vs-range monitoring with excursion alerts and audit trail.

### Controlant

Key observations (all [A]):

- Positioning: pharma supply chain visibility platform + IoT devices + 24/7/365 monitoring & response services; GxP-validated (21 CFR Part 11 / Annex 11).
- Platform: real-time temperature and location monitoring; customized notifications and alerts; **Shipment Overview dashboard** (shipment numbers, excursion instances, logistics metrics) with drill-down into location/temperature; customizable dashboards/filters per role.
- **Excursion graph per shipment**: each reported temperature instance tied to a geolocation — where the excursion happened, its severity, when.
- Devices: **reusable, pre-configured, calibrated GxP-compliant loggers** (Saga family); device health assessments; service-center distribution; high device-return rate claimed (sustainability framing).
- Excursion notifications + **quality reports** used for inspections, decisions, prompt intervention.
- **Automatic release mechanism ("Zero-Touch Release")**: if no excursions occurred during shipment, the system automatically releases the pharmaceutical product for further processing/distribution.
- **Robust audit trail**: every activity within the system recorded — compliance record for inspections.
- **Controlant Go** (self-serve logistics pole): order pre-configured devices for a temperature range → receive calibrated, charged devices → attach, press START, ship → press STOP on receipt → **scan QR code → instant quality report** from the cloud; one-click shareable live shipment view; "no implementation, no USB uploads, no training".
- Integrations with multiple third-party data sources; AI use cases incl. **lane risk assessment**.

### Sensitech (Carrier)

Key observations (all [A]):

- Device spectrum (widest in sample, incl. historical forms): **real-time temperature and location monitors** (TempTale GEO family), **conventional USB dataloggers**, **wireless monitors**, **Ryan strip chart recorders** (mechanical, still sold), **shipping temperature indicators** (chemical threshold indicators); every TempTale monitor ships with a **NIST-traceable validation certificate**.
- **SensiWatch Platform**: cloud supply-chain visibility platform; end-to-end inbound/outbound shipment monitoring; actionable alerts; "comprehensive IoT ecosystem" integrating a wide range of data sources and third-party software/platforms; companion mobile app.
- **Lynx FacTOR** (release evaluation): SaaS that automatically detects/creates **Time Out of Range (TOR) events**, applies expiration-date and mode-of-transport rules, tracks **remaining stability budget** from manufacturing to first economic customer, and produces **release recommendations** — final accept/reject stays with the customer's team; claims evaluation time reduced "from days to minutes".
- **ColdStream Select**: life-sciences product-release decision support with real-time monitoring, full traceability, cGXP compliance.
- **ColdStream Site**: stationary/facility temperature monitoring (the fixed-location sibling of the in-transit products).
- **Professional services** ("cold chain as a service"): identify weaknesses/variability in cold chain processes, root-cause analysis.
- FAQ guidance: monitor both the insulated package **and** the truck — a holistic picture of what caused a spike/drop; real-time visibility enables faster accept/reject decisions mid-shipment.
- Industries: food, life sciences, consumer & industrial. Scale claims: 17M shipments monitored annually, 130 countries.

### Thermo King TracKing (ConnectedSuite)

Key observations (all [A]):

- Context: telematics portfolio of a transport-refrigeration-unit (TRU) manufacturer — trailers, trucks/vans, rail, marine; "monitor and control your truck or trailer refrigeration units or APUs anywhere, in real time".
- **Reefer monitoring**: is the unit on? what is the temperature set-point? unit alarms.
- **Load condition**: "keep an eye on the real temperature of individual loads in transit, rather than relying on the temperature setpoint, to guarantee quality of delivery" — the cargo-condition-vs-setpoint distinction is explicit.
- **Temperature compliance**: "use temperature reports and graphs to prove that sensitive cargo was maintained at the desired temperature throughout every point in the journey".
- Asset location; **door sensor data** recording all door openings (temperature + load security).
- Cargo traceability: shipment location and condition; know instantly when a delay occurs; proactively manage exceptions.
- Fleet dashboards: fleet performance (unit operation, alarm summaries, **zone metrics for multi-temp fleets**, cycle-sentry/continuous mix), readiness score (alarms, open campaigns, predictive alerts, communication lapses).
- Fuel and maintenance reporting; scheduled reports (daily/weekly/monthly) to multiple stakeholders/customers.
- **Data sharing/integration** into third-party websites/backend systems; **Remote Operating Center**; remote control of units.
- Pole note: this is vehicle/asset-centric telematics whose cold-chain slice (load condition, setpoint, compliance reports, door events) overlaps the Type — the clearest boundary specimen in the sample.

---

## Cross-product Comparison

| Aspect | Tive | Controlant | Sensitech | Thermo King TracKing |
|---|---|---|---|---|
| Central monitored unit | shipment/trip (tracker inside) | shipment (logger inside) | shipment / batch | vehicle/trailer + its loads |
| Condition data capture | disposable real-time trackers + passive logger | reusable real-time loggers | real-time + USB + wireless + strip chart + chemical indicators | reefer-unit sensors + door sensors |
| Defining condition | temperature (+humidity/light/shock/tilt) | temperature (+location) | temperature/humidity | temperature (actual vs setpoint) |
| Requirement | configurable thresholds per product/profile | GxP range per device configuration | product/lane requirements; TOR rules | setpoint + desired-temperature compliance |
| Excursion semantics | single / cumulative / MKT alerts | excursion instances with geo + severity | auto-created TOR events + stability budget | alarms + compliance graphs |
| Live operations | platform + 24/7 monitoring service | platform + 24/7 monitoring & response | SensiWatch + professional services | fleet dashboards + Remote Operating Center |
| Delivery evidence | time-stamped audit trail; verifiable reports | quality reports; audit trail; auto-release | accept/reject decisions; release recommendations; calibration certs | temperature compliance reports/graphs |
| Release/quality decision support | on-device Product Release Assist | Zero-Touch Release | Lynx FacTOR recommendations | — |
| Location layer | GPS/cellular/WiFi; geofencing; route deviation | geolocation-tied readings | real-time location monitors | asset location; geofences/POI |
| Equipment control | — | — | — | remote reefer control |
| Industry emphasis | food + pharma + high-value | pharma | food + pharma + industrial | refrigerated road fleets |

### Cross-product commonalities (Layer B)

Present in **all four** (strongest candidates for the defining structure):

1. A condition measurement stream captured in/around the cargo environment during transport.
2. A defined temperature requirement the cargo must satisfy.
3. Evaluation of measurements against the requirement, producing flagged excursion events (alert, alarm, TOR event, or visible excursion on a graph).
4. A retained condition record for the journey, retrievable as evidence (report/graph/audit trail) — every vendor's compliance framing rests on it.

Present in **three or four** (common mature structure, not defining):

- Real-time telemetry with live dashboards/maps (all four; mechanism differs).
- Location tracking tied to condition readings (all four in some form).
- Alerting with configurable thresholds and routing to responsible people (all four).
- Device fleet management: activation, calibration certificates, battery/health, return/reuse (Tive, Controlant, Sensitech; TracKing manages the vehicle instead).
- Integration/data sharing with third-party systems (all four).
- Analytics over historical shipments (all four in some form).
- Quality/release decision support at delivery (Tive, Controlant, Sensitech — pharma-flavored; absent in TracKing).
- Managed 24/7 monitoring services (Tive, Controlant; Sensitech professional services adjacent; absent in TracKing).

Present in **one or two** (variant/vendor-specific):

- Remote control of refrigeration equipment (TracKing — equipment-native pole).
- Passive/chemical no-power indicators (Sensitech).
- Reusable-device circularity programs with carbon claims (Controlant; Sensitech takeback program exists).
- AI route-deviation theft detection (Tive).

---

## Canonical Abstraction

### L0 — Defining Invariant (deliberately minimal)

```text
Monitored transport of temperature-sensitive cargo
└── Condition measurement stream from the cargo's transport environment
    └── (temperature is the defining condition)
    └── Defined temperature requirement for the cargo
    └── Excursion evaluation: measurement vs requirement → flagged excursion events
    └── Retained condition record retrievable as delivery evidence
```

Four properties. Remove any one and the product stops being recognizable as this Type:

1. **Monitored transport context** — a shipment/trip of temperature-sensitive cargo moving between origin and destination is the unit of monitoring. Without it, the product is facility monitoring or asset telematics.
2. **Condition measurement stream** — readings captured in/around the cargo environment during transport. Without measurement there is nothing to monitor.
3. **Requirement + excursion evaluation** — a defined acceptable range for the cargo, against which readings are compared, producing flagged excursion events. Without the requirement and evaluation, the product is a thermometer or a data dump, not monitoring.
4. **Retained condition record as delivery evidence** — the journey's condition history persists and can be produced as a report/record. Without it, monitoring leaves no trace and the core value (proving the cold chain held, or explaining why it didn't) disappears.

**Historical / market-sample check (deliberately applied):** Sensitech still sells Ryan **strip chart recorders** (mechanical, paper) and **chemical shipping temperature indicators** (no electronics at all). Both satisfy L0: measurement during transport, a requirement (chart range / threshold chemistry), excursion visible against it, retained record (chart / indicator state). USB PDF loggers satisfy it. Modern real-time platforms satisfy it. Therefore real-time connectivity, GPS, multi-sensor arrays, alerting services, dashboards, calibration programs, and compliance frameworks are all **excluded from L0** — they are how modern products realize the invariants, not what makes the Type.

### L1 — Common Mature Structure

Very common in current products; expected by the market; not definitional:

- Real-time telemetry (cellular/SAT/GPS trackers, reefer telematics, gateways) with live shipment views on map + temperature graph.
- Location layer: geolocation-tied readings, geofences, route/ETA/delay awareness.
- Alerting & escalation: configurable thresholds per product/lane, notification routing to responsible teams, device-health alerts (battery/connectivity).
- Multi-sensor condition beyond temperature: humidity, light, shock, tilt, door openings.
- Monitoring-device management: activation/start-stop, calibration certificates, battery/health, return/reuse programs.
- Delivery documentation: per-shipment reports, audit trails, compliance support (food-safety and pharma frameworks).
- Shipment templates / lane configuration for repeat lanes.
- Sharing & collaboration: shareable live views, white-label links, role permissions.
- Analytics: excursion rates, lane/carrier comparison, custom dashboards.
- Quality decision support at delivery: accept/reject workflows; in pharma, release automation (MKT/stability-budget logic).
- Managed monitoring services (24/7 control-tower) offered by several vendors.

### L2 — Variant / Optional Structure

- **Regulatory depth**: pharma GxP grade (21 CFR Part 11 / EU Annex 11, GDP, calibration, release automation) vs food grade (FSMA-era food-safety evidence, spoilage/claims focus) vs general industrial.
- **Data-capture mechanism**: disposable real-time trackers; reusable loggers with service centers; passive USB/PDF loggers; chemical indicators; reefer-native telematics; fixed gateways at handoffs.
- **Mode & cargo level**: road trailer/truck, ocean container, air (flight-safe devices), rail; vehicle-level vs container-level vs individual box/package-level.
- **Operating model**: self-serve software+hardware vs vendor-run 24/7 monitoring & response vs professional/consulting services.
- **Equipment relationship**: cargo-side sensing only vs equipment-native telematics with remote reefer control.
- **Release decision automation depth**: none → on-device assist → auto-release → rule-engine recommendations with human sign-off.
- **Sustainability programs**: reusable vs disposable device economics, takeback, carbon claims.
- **Integration posture**: TMS/WMS/ERP/third-party data ingestion; data-sharing APIs.

### L3 — Vendor-specific (kept out of the final document)

- Tive: Solo 5G / Solo Pro / Solo Lite / Tive Tag product line; Smart Route Deviation; Smart Reefer Cycle Detection; Product Release Assist; probe-based cryogenic support; network-coverage claims.
- Controlant: Saga reusable devices; Zero-Touch Release; Controlant Go starter-pack flow; lane-risk-assessment AI; scale claims (vaccine doses, boxes/year).
- Sensitech: TempTale family; Ryan strip charts; ColdStream Select / ColdStream Site; Lynx FacTOR (TOR events, stability budget); SensiWatch; Berlinger line; device takeback program.
- Thermo King: TracKing / TracKing Pro / Smart Trailer; ConnectedSuite; Remote Operating Center; readiness score; cycle-sentry metrics; CARB compliance tooling.

---

## Vendor-specific Findings

(Consolidated L3 list — see above. None of these entered the canonical model. Notable near-misses that were deliberately kept out of the Type definition:)

- **Reefer cycle detection** (Tive) is a vendor-named AI capability; the underlying concern (refrigeration unit behavior vs cargo condition) is general, but the specific alert is product-specific.
- **Stability budget / MKT** mechanics are pharma-domain concepts that appear in vendor-specific forms (Lynx FacTOR, Tive MKT alerts); the general capability — "quality decision support using the retained record" — is L1; the specific math is vendor/domain detail.
- **Zone metrics / cycle-sentry** (TracKing) are TRU-equipment concepts, not Type concepts.

## Boundary Findings

| Neighboring Type | Relationship | Distinction | "Remove what → becomes the other" |
|---|---|---|---|
| Shipment Visibility Platform | adjacent, heavy overlap | Visibility = location/status/milestones of any shipment; this Type = cargo **condition vs a temperature requirement**. Tive spans both; its cold-chain use case is the Type studied here. | Remove condition-vs-requirement monitoring → shipment visibility platform |
| Vehicle Telematics Platform | adjacent | Telematics = vehicle/asset health, driver, fuel, maintenance; this Type = cargo environment. TracKing is telematics whose cold-chain slice overlaps. | Remove cargo-condition-vs-requirement → vehicle telematics |
| Food Cold Chain Management (§20 leaf) | industry sibling | Food cold chain management spans the food supply chain incl. production/storage/retail with food-industry semantics; this Type is the **transport leg**, cargo-agnostic (pharma, chemicals, flowers, organs). | Add food-industry scope + non-transport legs → food cold chain management; strip them → this Type |
| Environmental Monitoring Platform (§21) | adjacent | Facility-centric monitoring of fixed locations; this Type monitors **moving** cargo in transit. Sensitech ships both (ColdStream Site vs in-transit products) as separate product lines. | Remove the transport context → environmental monitoring |
| Transportation Management System (§10) | complementary | TMS plans/executes transport (orders, rates, carriers, routes); this Type observes condition and does not execute transport. | — |
| Dangerous Goods Transportation Management | sibling special-cargo type | DG = hazard-class compliance (classification, placarding, docs); this Type = condition preservation. Different regulatory object, same "special cargo transport" family. | — |
| Industrial IoT Platform | generic substrate | IIoT manages generic connected devices; this Type is domain-specific (requirement + excursion semantics + evidence). | — |

Boundary verdict: the leaf is a legitimate distinct Type — in-transit condition monitoring with an evidence function. No taxonomy conflict found. The seam with Shipment Visibility Platform is the blurriest because several vendors (Tive, SensiWatch) market one platform for both; the Type boundary is drawn at the condition-vs-requirement core, not at vendor packaging.

## Uncertainties

- **Help-center depth**: research relied on official product/solution pages; deep help-center articles (e.g., Controlant support portal) were not fetched. Operational micro-details (exact alert latency, data intervals, retention periods) are therefore not asserted anywhere.
- **Copeland/Emerson** (a major food-retail cold chain player) could not be reached (403). The food-retail pole is covered indirectly via Tive/Sensitech food programs; risk of slight pharma/transport bias in the sample is acknowledged.
- **Pricing/packaging** was not researched (out of scope for the Type model).
- **Facility-vs-transport split** inside vendors (Sensitech ColdStream Site vs in-transit; Emerson Go Real-Time vs Oversee per public knowledge) suggests the market itself treats these as distinct product lines — consistent with the boundary drawn here, but the facility side belongs to Environmental Monitoring, not this leaf.
- Whether "release decision automation" should eventually be its own Type (pharma QA domain) is left open; in this sample it is a capability layer on top of monitoring, not a standalone product.

## Final Synthesis

A Cold Chain Transportation Monitoring application is defined by a small loop: **measure the cargo environment during transport → compare against a defined temperature requirement → flag excursions → retain the record as evidence**. Everything else in modern products — real-time telemetry, maps, multi-sensor arrays, alerting services, device fleets, compliance frameworks, release automation, analytics — is mature implementation mass around that loop, varying by industry (pharma vs food vs industrial), device mechanism (disposable/reusable/passive/equipment-native), and operating model (self-serve vs managed control tower). The Type's center of gravity is the **shipment as monitored unit**; its two nearest neighbors (shipment visibility, vehicle telematics) share data layers but lack the requirement-vs-condition core; its industry sibling (Food Cold Chain Management) owns the food-supply-chain-wide scope; its fixed-location cousin (Environmental Monitoring) owns facilities.
