# Research Notes — Environmental Monitoring Platform

Research date: 2026-09-08
Directory leaf: Environmental Monitoring Platform (§21 Environment, Sustainability & Climate)
Slug: environmental-monitoring-platform

---

## Research Goal

Understand what software sold as an **environmental monitoring platform** actually is as an Application Type: its core objects, the observation loop it operates, who uses it across market segments, and where its boundary lies against neighboring Types — especially the media-specialized monitoring leaves (Air Quality Monitoring, Emissions Monitoring / CEMS, Environmental Water Monitoring), Environmental Data Platform, Environmental Compliance Management, industrial telemetry Types (SCADA / historian / IIoT), and the facility/asset "environmental monitoring" population that shares the market label.

## Joint-review context (from sibling passes)

- **air-quality-monitoring** (processed 2026-09-06) declared this leaf "broader sibling — multi-medium (air, water, soil, noise, weather) monitoring. Generalize the pollutant model to arbitrary environmental media → Environmental Monitoring Platform. AQM is the air-specific instance with pollutant-specific semantics (AQI, regional standards)."
- **emissions-monitoring-cems** (processed 2026-09-08) expected this leaf "to name the broader multi-media category; CEMS is the regulated-source instrument specialist within it."
- **environmental-compliance-management** (processed 2026-09-08) flagged the media-specific leaves (including this one) with "candidate seam = operational media object vs obligation register + conformance loop."
- **environmental-data-platform** (research complete 2026-09-08, leaf not yet finalized) held: "Monitoring platform = ongoing observation of current conditions (sensor networks, live readings, alarms, network health). Data platform = the validated long-term corpus of record."

This pass performs this leaf's side of all four seams.

## Initial Boundary (working hypothesis before research)

- Core use: software that operates ongoing observation of environmental conditions — air, water, soil, noise, vibration, weather, indoor climate — at identified monitoring points, presenting current conditions and history and alerting on thresholds.
- Likely users: environmental managers/coordinators at industrial and infrastructure sites (mining, landfills, wastewater, airports, construction), public agencies and research organizations, consultants, facility operators.
- Nearest Types: the three media-specialist monitoring leaves; Environmental Data Platform (corpus vs live operations); Environmental Compliance Management (evidence vs obligation register); SCADA/historian/IIoT (process telemetry substrate); Building Management System (control vs observation); facility condition monitoring (same label, different subject).
- Open questions: (1) is the multi-medium span definitional or is the Type media-agnostic with multi-medium as the platform pole? (2) are alerts definitional or common? (3) does the facility/asset "environmental monitoring" population (temperature/humidity/leak for asset protection) belong inside this Type or is it a naming collision? (4) how central are prediction/dispersion modelling and community/complaint engagement?

## Research Questions

1. What are the core objects — monitoring point/station, device, parameter, time series, threshold, alert, event?
2. How does the observation loop run (sensor → ingest → validation → storage → presentation → alert → response)?
3. What does "multi-medium" mean structurally — one system spanning air/noise/water/vibration, or one parameter family per deployment?
4. What role do compliance limits, exceedances, and regulator-facing reporting play vs pure observation?
5. What role do prediction (dispersion/trajectory modelling) and source attribution play?
6. What role do community engagement and complaint management play?
7. How do device/network health, calibration, and data quality surface?
8. Where is the boundary vs media specialists, data platforms, compliance management, industrial telemetry, and the facility-monitoring population?

## Representative Products

Selection rationale: market representation across the distinct poles of this market, documentation completeness, different product philosophies (intelligence-led platform vs instrument-maker ecosystem vs open measurement system vs alert-led condition monitoring), different customer tiers (enterprise infrastructure operators → agencies/consultants → research/infrastructure organizations → SMB facility operators), and one deliberate outside-the-§21-frame product to test the naming-collision boundary.

| Product | Pole | Tier / segments | Why selected |
|---|---|---|---|
| Envirosuite (Omnis) | multi-medium environmental intelligence platform (air, dust, odour, methane, noise, vibration, water) + prediction + complaint management | mining, industrial, waste, wastewater, aviation (enterprise operators) | the clearest multi-medium platform; prediction and community engagement as first-class capabilities |
| Acoem (Cadence) | instrument-maker ecosystem: noise & vibration + ambient air + continuous emission devices under one cloud platform | smart city, construction, industry, wind farm, airport; agencies, consultants, industry | manufacturer-ecosystem philosophy; AI source recognition; temporary-to-permanent networks |
| Campbell Scientific | open measurement-system pole: data loggers / DAQ + any sensor + software, media-agnostic | hydrology, meteorology, soil, early warning, aviation weather, infrastructure; research/agency/infrastructure | 50-year lineage; open architecture (third-party sensors); the research/agency pole |
| Sensaphone | facility/asset condition monitoring pole (temperature, humidity, water, power, equipment status) | cold storage, greenhouse, data center, pump stations, residential (SMB) | the "environmental monitoring" naming-collision population; 1985 phone-dialer lineage for the historical check |

Deliberately not sampled: Casella (construction boundary monitoring — overlaps Acoem's pole), OTT HydroMet / Vaisala (hydromet instrument networks — overlaps Campbell's pole), Monnit/Dickson (facility pole — Sensaphone covers it), agency national networks (not directly fetchable; checked conceptually), Kaiterra/IQAir/Clarity (already sampled by the air-quality pass as the air specialist).

## Sources

Fetched 2026-09-08 (WebFetch, official pages; all Layer A unless noted):

- Envirosuite homepage — https://www.envirosuite.com/ (fetched successfully)
- Envirosuite Omnis platform page — https://envirosuite.com/platforms/industrial/omnis (fetched successfully; rich operational detail incl. FAQ)
- Acoem homepage — https://acoem.com/ (fetched successfully; full solution/range navigation)
- Acoem Cadence platform page — https://www.acoem.com/en/products/environmental-platforms/cadence/ (fetched successfully; rich operational detail)
- Campbell Scientific homepage — https://www.campbellsci.com/ (fetched successfully)
- Campbell Scientific Environmental Solutions page — https://www.campbellsci.com/environmental (fetched successfully)
- Sensaphone homepage — https://www.sensaphone.com/ (fetched successfully; positioning, industries, product navigation)

Source-access limitations:

- No vendor help centers / user manuals were fetched this pass; all observations are product/platform/solution-page level. Operational specifics (exact alert latency, data-retention terms, API semantics, per-model data-logging behavior) were not directly observed and are not asserted.
- Campbell Scientific's software products (data-logger support software, cloud services) were not individually fetched; claims about Campbell are restricted to its positioning, solution domains, and open-architecture statements.
- Sensaphone's per-product data-logging/dashboard behavior was not fetched; claims restricted to homepage-level positioning (sensors + condition readings + phone/email/text alerts + real-time status view).
- Agency/public environmental monitoring networks (national EPA-class) were not directly fetched; the L0 was checked against them conceptually (historical/market-sample check) rather than by direct observation.

## Product Observations

### Envirosuite (Omnis) — evidence layer A

From homepage and Omnis platform page:

- Positioning: "Real-time Environmental Monitoring Software" / "environmental intelligence platform"; "Software and hardware solutions helping you monitor and predict environmental events and community sentiment."
- Multi-medium solution span (directly observed): Air Quality Monitoring, Dust Monitoring, Odour Management, Methane Monitoring, Airport Noise Monitoring, Industrial Noise Monitoring, Vibration Monitoring, Water Quality, Community Engagement.
- Industries: Mining, Industrial, Waste, Wastewater, Aviation. Platform family: Omnis (industrial), SeweX (water), ANOMS NoiseDesk / ANOMS Advanced / WebTrak (aviation noise), Carbon Emissions, EVS IOT.
- Omnis operational detail (directly observed):
  - "displays your site's emission levels across multiple parameters, when you run the risk of exceeding them and exactly where you should focus mitigation efforts" — multi-parameter display + compliance-limit risk + mitigation targeting.
  - Real-time monitoring + air emissions modelling: dispersion models, forward/reverse trajectory modelling; hyperlocal hourly weather forecasts "up to 100m resolution"; forecast modelling "out to 72 hours into the future at 1-hour timesteps"; discrete receptor locations can be set.
  - Smart alerts "of potential impact leading to compliance breaches"; colour-coded dashboard; "arcs of influence" to pinpoint issues and lower investigation times.
  - Noise: "24/7 secondly noise reporting, event playback and classification"; non-compliance event playback to classify root cause.
  - Water: "intelligent insights from water monitoring data across your site."
  - Complaint attribution: automatic reverse trajectory modelling "to determine the likely sources of dust complaints lodged by nearby communities"; "identify if it was your operation that caused the issue lodged by the community, or it was another culprit."
  - Automated regulator reporting; publicly accessible reports for communities (customer stories: Newmont — dust, noise, odour, water with public reports; Heathrow — noise + engagement; Ada County Landfill).
  - Users quoted: Environmental Compliance Manager (landfill), Manager Asset and Planning (wastewater utility), Sustainability Director (aggregates).
- Value framing: "responsible productivity" — plan operations around environmental risk, meet compliance standards, engage community.

### Acoem (Cadence) — evidence layer A

From homepage and Cadence platform page:

- Positioning: manufacturer spanning Environmental Monitoring (ambient air incl. particulates/nephelometers/gas analyzers/indoor AQ/hyperlocal sensors/black carbon; continuous emission incl. opacity/dust/marine smoke; noise & vibration stations and sound level meters; specialized: dust & blast monitoring, tunnel sensors) + Industrial Reliability (machine condition monitoring — different domain) + Security (acoustic threat detection, urban noise).
- Environmental platforms: Cadence ("the ultimate environmental monitoring software platform"), Aerovision, Healthy Schools network. Services: calibration, training, accreditation/certification.
- Cadence operational detail (directly observed):
  - "online management platform that gives you the power to measure and track environmental data in real time from a single acoustic monitor or your entire network of sensors."
  - Customised dashboard; AI-powered alert management ("AI able to recognise and identify alert sources"); automated reporting + data integration; "Effortless communication hub" for stakeholders "from project managers to the public"; Class 1 instrument compatibility.
  - Cloud-based delivery using MQTT "with no public IP required"; real-time notifications; synchronise with historical data for "data comparison, reporting and compliance requirements."
  - Remote device configuration "without needing to be on-site"; "understand the status and performance of every device at any time"; connect a single device or an entire network; export data "for regulatory reports or public-facing websites"; individual commissioning keys.
  - Real-time "heatmap, overall level, and multiple indicator data centralised on your dashboard."
  - AI source recognition: "For each noise exceedance experienced, the AI will give you the main and secondary source that it recognises as the source of the alert" — attribution of exceedances to sources; results "ready to be printed on your report."
  - Weather-station integration "to correlate weather data such as rain, wind direction and wind speed, and add relevant context to your noise emissions."
  - Applications: smart city, construction (schedule noisy works in authorised periods, verify compliance with maximum permissible levels), industry (keep activities under regulatory limits, avoid "agency-imposed operational shutdowns and fines"), wind farm, airport (stakeholder-facing consultation website).
  - Users: "industries, government authorities, environmental consultants and businesses"; single user or entire team; "from the smallest temporary monitoring job to a major construction site."

### Campbell Scientific — evidence layer A (positioning level)

From homepage and Environmental Solutions page:

- Positioning: "designer and manufacturer of data loggers, data acquisition systems, and measurement and control products"; "rugged, low-power systems for long-term, stand-alone monitoring and control"; 50+ years.
- Environmental solution domains (directly observed): Aviation Weather, Early Warning and ALERT/2 Systems (floods, fires, severe weather), Extreme Application Series (water resources, extreme weather, climate), Hydrology ("monitor and control water systems with real-time data"), Meteorology, Micromet and Flux (surface-atmosphere exchanges), Soil ("track soil conditions and weather parameters"), Surface Transportation (roadway weather).
- Infrastructure solutions: dams, mining, structural health, geotechnical DAQ. Renewable energy: solar/wind met stations.
- Open architecture (directly observed): "integrate our sensors or virtually any third-party technology, so you're never locked in to a single vendor's solution"; "expand and scale your network over time"; "hardware and software solutions give you the flexibility... to extend capabilities, customize workflows."
- Case studies observed: real-time urban air quality (Oslo), fire weather + utility monitoring, dam safety monitoring.
- Note: this pole sells the measurement system (loggers + sensors + software) from which environmental monitoring networks are assembled; the platform surface is data acquisition, storage, and delivery rather than a packaged multi-medium SaaS dashboard.

### Sensaphone — evidence layer A (positioning level)

From homepage:

- Positioning: "Remote Monitoring Systems and Controls" — "Sensaphone systems provide an extra layer of protection 24/7, instantly notifying you of changes in temperature, equipment status and other critical conditions. Alerts can be sent straight to your mobile device."
- Notification channels (directly observed): "Receive immediate notification of environmental or equipment changes via phone call, email or text message."
- Real-time status view: "real-time status of equipment and environmental conditions from a smartphone, tablet or computer."
- Industries (directly observed): Data Center, Water and Wastewater (unattended pump stations, wells, tank farms — tank levels, power failure, turbidity, flow rates), Residential, Oil & Natural Gas, Medical Cold Storage, Greenhouse, Livestock, Food & Beverage Cold Storage, HVAC, Environmental Remediation, Cannabis Growing Facilities.
- Value framing: asset/inventory protection ("Is Your Cold Inventory Protected Against Environmental Threats?"; "documentation to prove it"); "Family owned and made in the USA since 1985."
- Product family: Sentry, Stratus EMS, Sentinel, 400/800, 1400/1800, IMS-4000E Enterprise host, WSG30, sensors & accessories.
- Note: this population uses the market label "environmental monitoring" for condition monitoring of enclosed/asset environments (temperature, humidity, water leak, power, equipment status) — structurally the same observation loop, different subject and purpose (asset protection, not environmental stewardship).

## Cross-product Comparison

| Dimension | Envirosuite Omnis | Acoem Cadence | Campbell Scientific | Sensaphone |
|---|---|---|---|---|
| Identified monitoring points | site monitoring positions + discrete receptors | acoustic/vibration monitors + sensor networks, single device to entire network | stations built from loggers + sensors (hydro/met/soil/air) | sensors/zones at facility locations |
| Environmental parameters | air quality, dust, odour, methane, noise, vibration, water | noise, vibration (+ air, CEM ranges in the wider ecosystem) | any sensor: water level/flow, weather, soil, gas flux, air quality | temperature, humidity, water, power, equipment status |
| Time series + history | real-time data + trends visualization | real-time data + synchronise with historical data for comparison | long-term stand-alone recording (positioning) | real-time status (history not directly observed) |
| Current-conditions view | colour-coded real-time dashboard | real-time dashboard: heatmap, overall level, indicators | real-time data for operations/early warning | real-time status on phone/tablet/computer |
| Thresholds/alerts | smart alerts of potential compliance breach | AI-powered alert management; real-time alerts + event notifications | early-warning alerting (flood/fire/severe weather) | instant notification: phone call, email, text — the core pitch |
| Exceedance/compliance semantics | compliance limits + risk of exceeding + mitigation focus | compliance reporting; keep activities under regulatory limits | not compliance-framed (research/early-warning) | documentation to prove conditions (cold-chain evidence) |
| Source attribution / prediction | dispersion + forward/reverse trajectory modelling; 72h forecast; complaint attribution | AI source recognition (main/secondary source of each exceedance) | not observed | not observed |
| Device/network health | EVS IOT platform (fleet) | device status/performance at any time; remote configuration | rugged long-term stand-alone operation (positioning) | 24/7 unattended monitoring; power-failure sensing |
| Weather/met context | hyperlocal weather forecasts as modelling input | weather station integration for context | meteorology is a monitored domain | not observed |
| Spatial presentation | arcs of influence around facility; pinpoint risk | heatmap; network view | station networks | zones/locations per facility |
| Reporting | automated regulator reporting; public reports | automated reporting; export for regulatory reports or public websites | case-study/research outputs | documentation records |
| Community/stakeholder surface | community engagement; complaint management; public reports | communication hub; stakeholder-facing consultation website | not observed | not observed |
| Roles/access | team access | authorised personnel; commissioning keys | not observed | not observed |
| Hardware coupling | sells hardware + software | sells Class 1 instruments + platform | sells loggers/sensors + software; open to third-party sensors | sells sensors + monitoring systems |
| Deployment scale | site-wide enterprise operations | single device → network; temporary job → major site | small network → regional/infrastructure scale | single facility → enterprise host |

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product stops being an environmental monitoring platform:

```text
Identified monitoring points (locations where environmental conditions are measured)
└── Environmental measurements recorded as persistent time series per point/parameter
    └── Presentation of current conditions at those points
    └── Presentation of historical trends for those points
```

- **Identified monitoring points** — an environmental monitoring platform's data has spatial meaning: every measurement belongs to a named/located point (station, sensor position, monitoring zone, receptor). Without identified points, the system is an anonymous telemetry feed.
- **Environmental measurements as persistent time series** — defined environmental parameters (of one or more media: air, water, soil, noise, vibration, weather, indoor climate) recorded over time per point. Without persistence over time, it is spot-checking, not monitoring.
- **Current + historical presentation** — monitoring is an ongoing observation loop: what are conditions now, and how have they changed. Remove currency and it becomes a data archive (Environmental Data Platform territory); remove history and it becomes a live indicator only.

Media-agnostic by design: the parameter set is environmental conditions, not one fixed medium. The multi-medium span (one system covering several media) is the platform pole's common mature structure, not the invariant — single-medium specialists (air, water, emissions) share this same core with medium-specific semantics added.

Historical / market-sample check (§24-style): a 1990s-era agency hydromet/water-quality network (stations + logger time series + current readings + published history), a 1985 phone-dialer condition-monitoring lineage (sensors + readings + call-out alerts; the software Type's thin ancestor — the modern cloud products in the same lineage satisfy the full core), and a modern multi-medium SaaS platform all satisfy this definition. No cloud, AI, dispersion modelling, AQI, maps, or complaint management is in the core. Passed.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Thresholds and alerts** — user-defined limits on measurements (and device conditions) triggering notifications. 4/4 (Envirosuite smart alerts; Cadence AI-powered alert management; Campbell early-warning systems; Sensaphone's entire value proposition). In the facility pole, alerting is the primary delivered value; structurally still an addition to the observation loop.
- **Multi-parameter / multi-medium span** — one system holding several environmental parameter families (air + noise + water + weather...). 4/4 across the sample (Envirosuite 7+ media; Acoem noise/vibration/air/CEM; Campbell any-sensor; Sensaphone temp/humidity/leak/power). This is what makes the *platform* pole recognizable against single-medium specialists.
- **Device/network health management** — device status, connectivity, remote configuration, unattended-operation reliability. 3–4/4 (Cadence device status/performance + remote config; Envirosuite EVS IOT; Sensaphone unattended 24/7 + power sensing; Campbell rugged long-term stand-alone positioning).
- **Spatial presentation** — map/site-layout/heatmap surfaces locating points and impacts. 4/4 in some form (arcs of influence; heatmap; station networks; facility zones).
- **Reporting and data export** — automated/scheduled reports, regulator-facing or stakeholder-facing outputs, data export. 4/4.
- **Weather/meteorological context** — weather either as a monitored domain or as context/modelling input for other parameters. 3/4 (Envirosuite hyperlocal forecasts; Cadence weather-station correlation; Campbell meteorology domain).
- **Data access beyond the dashboard** — APIs/exports/publication surfaces. 3/4 observed (Cadence export for regulatory/public websites; Envirosuite public reports; Campbell open architecture).

### L2 — Variant / Optional Structure

Depends on segment, posture, or business model:

- **Product-shape poles**: environmental-intelligence platform (packaged multi-medium SaaS with modelling) vs instrument-maker ecosystem (platform bound to vendor's device line) vs open measurement system (loggers + any sensor + software; user assembles the network) vs facility condition monitoring (asset-protection alerting).
- **Compliance posture**: compliance-limit monitoring with exceedance risk and regulator reporting (Envirosuite, Cadence) vs research/early-warning posture (Campbell) vs evidence/documentation posture (Sensaphone cold chain).
- **Prediction and source attribution**: dispersion/trajectory modelling, forecast-driven operational planning, complaint attribution (Envirosuite); AI source recognition of exceedances (Cadence). Absent in the other poles.
- **Community/stakeholder engagement**: complaint management, public reports, consultation websites (Envirosuite, Cadence) — present where operations have affected communities; absent in research/facility poles.
- **Fixed network vs temporary campaign**: permanent site networks vs temporary construction/monitoring jobs (Cadence explicitly spans both).
- **Indoor/outdoor/enclosed scope**: ambient outdoor networks vs indoor IAQ vs enclosed facility spaces.
- **Hardware coupling**: vendor instruments vs open third-party sensor integration.
- **Roles/permissions**: team access, authorized personnel, commissioning keys — depth varies; weakly evidenced, held as variant.

### L3 — Vendor-specific (Research Notes only)

- **Envirosuite**: Omnis/SeweX/ANOMS/WebTrak/EVS IOT brand names; "arcs of influence"; 100m-resolution hyperlocal forecasts; 72h/1-hour-step forecast window; "secondly" noise reporting; complaint-reduction and ROI claims (66%, AUD$700,000 — vendor claims); "responsible productivity" framing; Aeroqual partnership MoU.
- **Acoem**: Cadence/Aerovision/Healthy Schools brand names; Cube/ACT-400/Fusion/Orion device names; Class 1 metrology; MQTT with no public IP; individual commissioning keys; AI main/secondary source recognition; calibration/training/accreditation services; the Industrial Reliability and Security divisions (different domains under one company).
- **Campbell Scientific**: ALERT/2 early-warning protocol naming; Extreme Application Series; specific case-study sites (Oslo air quality, fire weather, Nicaragua dams); LoggerNet-class software not directly observed this pass — not asserted.
- **Sensaphone**: Sentry/Stratus/Sentinel/400/800/1400/1800/IMS-4000E/WSG30 product names; phone-call readout notification channel; "since 1985" lineage; made-in-USA positioning.

## Vendor-specific Findings

See L3. None of these entered the canonical model. Vendor performance claims (complaint reduction %, ROI) are recorded as claims only.

## Rejected Findings

- **"Environmental Monitoring Platform = Air Quality Monitoring generalized, therefore not its own Type."** Rejected as a collapse: the sampled market contains products whose defining property is operating monitoring across multiple media or media-agnostically (Envirosuite, Campbell), and the directory deliberately holds the generic leaf alongside media specialists. The generic leaf's center of gravity is the media-agnostic observation loop; media specialists add medium-specific semantics (AQI/regional standards for air; permit-limit compliance transforms for CEMS; water-specific rules). Keep-both with the medium-specialization seam.
- **"Alerting is definitional."** Rejected — a monitoring network that records and presents without alerting (research posture) is still recognizable; alerts are 4/4 common but the observation loop stands without them. (The facility pole inverts the emphasis — alerting is its primary value — but its structure still contains the full loop.)
- **"Prediction/dispersion modelling is definitional."** Rejected — present in the intelligence-led pole only (Envirosuite; attribution-only in Cadence); absent in Campbell/Sensaphone.
- **"Compliance-limit evaluation is definitional."** Rejected — that is the CEMS specialist's core (source-bound permit limits + compliance records) and the compliance-management Type's center (obligation register). Monitoring platforms display configured limits and exceedance risk, but the obligation register and conformance loop are not theirs.
- **"Multi-medium span is definitional."** Rejected as invariant — held as the platform pole's common structure. Single-medium products satisfy the L0; they are the specialist Types.
- **"Cloud SaaS dashboard is definitional."** Rejected — Campbell's assembled-network pole and historical agency networks satisfy the core without a packaged SaaS dashboard.
- **"Facility condition monitoring is a different Type."** Rejected for this pass — structurally it satisfies the same L0 (points + condition time series + current/history + alerts); the difference is subject and purpose (asset protection vs environment), documented as a variant pole + naming-collision flag rather than a split. See Boundary Issues.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (remove/add test) |
|---|---|---|
| Air Quality Monitoring (§21, processed) | specialist sibling | Same structural core; AQM adds air-pollutant semantics (pollutant parameter model, AQI/regional indices, collocation/calibration practice, ambient siting). Bind the parameter model to air pollutants → AQM. Generalize to arbitrary media → this Type. |
| Emissions Monitoring / CEMS (§21, processed) | specialist sibling | CEMS binds measurement to regulated industrial emission sources with reference-method transforms, validity machinery, and compliance records/reports. Remove the regulated-source + compliance-record frame → this Type; add it → CEMS. |
| Environmental Water Monitoring (§21, unprocessed) | specialist sibling | Same pattern with water-medium parameters and water-specific rules. Different medium → different Type. |
| Environmental Data Platform (research complete) | adjacent, ingestion handoff | This Type operates live observation (sensor networks, live readings, alarms, network health); the data platform holds the validated long-term corpus of record. Monitoring streams feed the corpus. Remove live operations → data platform; remove corpus-of-record governance → monitoring platform. |
| Environmental Compliance Management (§21, processed) | downstream consumer | Monitoring produces the evidence (measurements, exceedances, reports); compliance management holds the obligation register + conformance loop + corrective action. Monitoring platforms display configured limits but hold no obligations. Remove the obligation register → this Type. |
| EHS/HSE Platform (§21, processed) | adjacent program layer | EHS centers the organization-wide occurrence register + corrective actions; monitoring centers the observation loop. An EHS platform consumes monitoring summaries; it does not run sensor networks. |
| SCADA / Industrial Historian / IIoT (§16, unprocessed) | generic substrate | Process telemetry/control holds arbitrary channels for plant operations; this Type adds environmental semantics: media/parameter vocabularies, monitoring-point siting, environmental thresholds/exceedances, environmental reporting. Campbell's DAQ leg is adjacent at acquisition. Remove environmental semantics → IIoT/historian. |
| Agricultural IoT Platform (§20, processed) | same engine family | Boundary = device population + purpose (production-agriculture sensing vs environmental conditions). Campbell's soil solutions straddle the seam — flagged. |
| Building Management System (§17, unprocessed) | control vs observation | BMS drives HVAC/equipment; monitoring observes and alerts. When the primary loop becomes driving equipment, the product drifts to BMS. |
| Facility condition monitoring population (Sensaphone/Monnit/Dickson-class) | same-structure, different-subject population | Same observation loop; subject is enclosed/asset environments (temperature, humidity, leak, power, equipment) for asset protection, not environmental stewardship. Held inside this Type as a variant pole; naming collision flagged (see Boundary Issues). |
| Weather application / public data portal | presentation-only surface | Portals and weather apps present existing data; this Type operates the measurement loop (devices, ingestion, health, alerting). |
| Public Alert & Warning System (§24, unprocessed) | one-way public warning | Public warning broadcasts to populations; monitoring is the operator-side observation loop that may feed such warnings. |

Remove-what tests: remove identified points → anonymous telemetry feed (historian); remove time-series persistence → spot-check tool; remove current presentation → data archive (data-platform territory); remove environmental semantics → generic IoT platform; remove multi-parameter span → single-medium specialist leaf; remove alerts → still this Type (thin, research posture).

## Uncertainties

- No Tier-1 operational documentation (help centers/user manuals) was fetched for any sampled product; all observations are product/platform/solution-page level. Exact alert latencies, retention terms, API semantics, and per-model data-logging behavior are intentionally absent from both documents.
- Campbell Scientific's software surface (logger-support software, cloud services) was not individually fetched; its L1 contributions rest on positioning-level evidence and are marked accordingly.
- Sensaphone's historical-data handling was not directly observed; its L0 satisfaction for current products rests on the observed real-time status view + the product family's monitoring-system framing, with history held at reduced strength.
- Agency/public monitoring networks (national EPA-class multi-medium networks) were not directly fetched; the L0 was checked against them conceptually, not by direct observation.
- The facility-condition population's size and internal variety (Monnit, Dickson, AKCP, Hanwell-class products) was not sampled beyond Sensaphone; the variant-pole placement is a single-sample judgment.
- Whether indoor IAQ deployments of multi-medium platforms should be treated as variants (consistent with the air-quality pass) is held as variant here; no counter-evidence observed.

## Final Synthesis

An Environmental Monitoring Platform is software that operates an ongoing observation loop over **identified monitoring points**: it ingests **environmental measurements** (one or more media — air, water, soil, noise, vibration, weather, indoor climate) at those points as **persistent time series**, presents **current conditions and historical trends**, and — in mature products — evaluates **thresholds**, raises **alerts**, maintains **device/network health**, produces **reports/exports**, and adds **weather context**. The defining core is small (points + environmental time series + current + historical presentation); the multi-medium span is the platform pole's common structure, with single-medium specialists (air, emissions, water) as sibling Types sharing the same core plus medium-specific semantics. Around the core, products differentiate into poles: intelligence-led platforms (prediction, dispersion modelling, complaint attribution, community engagement), instrument-maker ecosystems (platform bound to a vendor device line, AI source recognition), open measurement systems (loggers + any sensor, user-assembled networks), and facility condition monitoring (asset-protection alerting under the same market label). The seams with the data platform (corpus vs live operations), compliance management (evidence vs obligation register), CEMS (ambient vs regulated source), and industrial telemetry (environmental semantics vs process channels) are all held on the center of gravity, not on shared features.
