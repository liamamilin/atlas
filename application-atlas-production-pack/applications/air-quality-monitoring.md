# Air Quality Monitoring

## Overview

An **Air Quality Monitoring** application collects, manages, and presents measurements of air pollutants at identified monitoring points over time. It answers two standing questions for its users: *what is the air like right now at the places we watch?* and *how has it changed over time?* — and, in most products, *when should someone be alerted?*

The defining core is deliberately small:

```text
Identified monitoring points (outdoor sites, rooms, or ducts where air is measured)
└── Pollutant measurements recorded as time series at each point
    └── Presentation of current conditions at those points
    └── Presentation of historical trends for those points
```

Everything else commonly associated with the category — air quality indices (AQI), maps, threshold alerts, device health dashboards, calibration and collocation workflows, public data sharing, APIs — is a standard capability of mature products rather than part of the definition. A legacy government network publishing station readings and history, a crowdsourced neighborhood sensor map, and an enterprise building-IAQ platform all satisfy the same core.

The application observes air; it does not control equipment, does not measure emissions at a regulated source, and does not manage other environmental media (water, soil, noise). When a product's center of gravity moves to those, it becomes a different Application Type (see Related Application Types).

## Users & Context

Users span a wide range, but they all stand in the same relationship to the system: they own, operate, or consume a set of monitoring points.

- **Environmental agencies and city governments** — operate dense sensor networks alongside sparse regulatory stations; use the data for public reporting, policy, and hotspot identification.
- **Industrial, mining, and construction operators** — monitor perimeter and site air (dust, fenceline pollutants) to detect issues, respond to complaints, and support mitigation.
- **Building owners, facility managers, and workplace teams** — monitor indoor (and outdoor reference) air across a portfolio of spaces; often to support occupant wellbeing and building certifications.
- **Schools and campuses** — protect students and use real data in teaching.
- **Community groups and researchers** — deploy sensors to make local pollution visible and study it.
- **Individuals** — check current and forecast air quality where they live, work, and travel.

The work environment differs by segment: agencies and enterprises work in a web dashboard over their own network; the public consumes a map or app; building teams additionally read data inside facility workflows.

## Core Model

### The Defining Core

**Monitoring point.** An identified, fixed location where air is measured — a regulatory station, a pole-mounted sensor, a room, a duct. The point carries identity (name, location, sometimes grouping into projects, buildings, or districts) and is the anchor to which all measurements attach. Without identified points, measurements have no spatial meaning.

**Pollutant parameters.** Each point measures one or more defined air-quality parameters: particulate matter (PM2.5, PM10), gases (NO₂, O₃, SO₂, CO, NOx), and, depending on context, black carbon, dust, CO₂, VOCs, temperature, and humidity. The parameter set is the vocabulary of the system; modules or sensor choices determine which parameters a given point carries.

**Measurement time series.** Each parameter at each point produces a continuous, timestamped record. The series is persistent: users return to past periods, compare them, aggregate them (hourly, daily, monthly), and export them.

**Current conditions and historical trends.** The system's two standing views. Current conditions summarize the latest readings per point (often color-coded); historical views let users inspect any past window, compare points, and analyze events after the fact.

### Standard Capabilities of Mature Products

These are widespread across the researched market and expected in practice, but a product remains an air quality monitoring application without any single one of them:

- **Air quality index (AQI).** A derived, color-coded index computed from pollutant concentrations according to a regional standard. Dominant in public-facing products; building-focused products often work with raw parameters and thresholds instead. The index is a presentation layer over the measurements, and which index applies varies by region.
- **Thresholds and alerts.** User-defined rules on measurements (and on device status) that trigger notifications — email, app, or dashboard flags. Alerts are how monitoring becomes action.
- **Device and network health.** Status tracking for the fleet: connectivity, battery/power, sensor or module health, offline detection, troubleshooting guidance, replacement workflows. A monitoring network is only as good as its uptime, so mature products treat device health as a first-class surface.
- **Data quality machinery.** Calibration, collocation against reference instruments, validation, and accuracy reporting (agreement metrics, scatter and time-series comparisons). Low-cost sensors in particular require correction against reference equipment; aggregator products distinguish raw from validated data.
- **Map as spatial surface.** Outdoor products present points on an interactive, color-coded map; indoor products present them on floorplans. The map is the dominant — but not definitional — presentation.
- **Data access.** APIs, CSV/raw/validated downloads, embeddable widgets, and scheduled or on-demand reports for stakeholders.
- **Roles and permissions.** Organization-scoped roles for operating a network (administration, device deployment/maintenance, data analysis, read-only observation, guests). Present in organization-facing products; absent in consumer and community products.

### One Structure, Many Implementations

```text
Concept:   Monitoring point
Forms:     regulatory station, low-cost sensor, indoor wall monitor, in-duct probe

Concept:   Parameter set
Forms:     regional pollutant suite (PM2.5/NO₂/O₃/...), IAQ suite (CO₂/VOC/PM), dust, black carbon, wind

Concept:   Current + historical presentation
Forms:     public map, agency dashboard, building portfolio view, consumer app, kiosk display

Concept:   Data quality
Forms:     reference-grade instruments (no correction needed), collocation + correction factors, validated-data tiers
```

## How It Works

The operational loop of an air quality monitoring application runs from deployment to distribution:

```text
1. Deploy / register monitoring points
   → choose locations, mount devices, register them into the system
   → organize points into projects, buildings, districts, or groups

2. Ingest measurements
   → devices transmit readings continuously (cellular, Wi-Fi, or building network)
   → the platform validates, stores, and processes the stream

3. Assure data quality
   → calibrate / collocate sensors against reference instruments where needed
   → apply corrections; flag or tier data quality; monitor device health

4. Present conditions
   → current view: latest readings per point, color-coded, on map / floorplan / list
   → historical view: time series per point, comparisons across points, aggregations

5. Alert on thresholds
   → define rules on measurements and device status
   → notify responsible people when air quality or network health crosses limits

6. Analyze, export, report
   → compare periods and locations, investigate events, export data
   → produce reports and summaries for stakeholders or regulators

7. Distribute (optional)
   → publish selected points publicly (open map, widgets, open data API)
   → feed downstream systems (building systems, analytics, portals)
```

Two loops recur in daily use. The **observation loop** — open the current view, scan for outliers or threshold breaches, drill into a point's history, decide and act. The **network-operations loop** — check fleet health, respond to offline or drifting devices, schedule maintenance or module replacement, re-verify data quality after intervention.

## Interfaces

Exact layouts vary by product; the following surfaces recur across the market.

### Map / spatial overview

The primary entry surface for outdoor networks.

- points plotted and color-coded by current level or index
- primary actions: pan/zoom, select a point, filter by parameter or time, share or embed

### Dashboard / snapshot

The operator's overview of a network or portfolio.

- current conditions summary, recent changes, outlier points, compliance or target status
- primary actions: drill into a point, compare locations, configure views

### Point detail (time series)

The analytical surface for one monitoring point.

- parameter readings over selectable time windows, aggregations, event inspection
- primary actions: change time range, compare parameters or points, annotate, export

### Device / network management

The operations surface for the fleet.

- device status (online/offline, power, connectivity, sensor/module health), grouping, settings
- primary actions: register/assign devices, troubleshoot, replace modules, set maintenance alerts

### Alert configuration

- threshold rules on measurements and device status, recipients, notification channels
- primary actions: create/edit rules, test, review alert history

### Data access surfaces

- API documentation and keys, CSV/raw/validated downloads, widgets for embedding, scheduled reports

### Public-facing surface (optional)

- open map or consumer app showing current levels, index, and history for public points; embeddable widgets; city or station pages

## Important Rules / Behaviors

- **Data quality is managed, not assumed.** Measurements from low-cost sensors carry uncertainty; mature products require calibration or collocation against reference instruments and expose accuracy evidence. Aggregators distinguish raw from validated data. Claims made from the data inherit its quality tier.
- **Device state conditions data trust.** A point that is offline, low on power, or reporting sensor faults is visibly flagged; its recent data is treated with caution. Network health and data credibility are coupled.
- **Thresholds are user-defined.** Alert limits reflect the operator's goals (health guidance, compliance, comfort, certification) rather than a single built-in standard; products let users tune rules per parameter, point, and group.
- **The index is regional.** Where an AQI is offered, it is computed per a named regional standard; the same concentration can map to different index values under different standards. Products typically let users select the standard.
- **Ownership and publication are explicit.** Organization products treat data as customer-owned; public sharing is an opt-in posture (publish a station, join an open map, enable an open-data API), not a default.
- **Placement rules matter.** Where a point sits determines what it means: outdoor siting follows exposure and source-proximity logic; indoor siting follows occupancy zones, HVAC coverage, and breathing-zone guidance. Products document placement because data validity depends on it.

## Variants

- **Ambient regulatory / agency networks** — reference-grade and indicative sensors combined; emphasis on public reporting, coverage gaps, and data validation.
- **Community / crowdsourced networks** — many individually owned sensors feeding a shared public map; emphasis on openness and accessibility.
- **Industrial and construction monitoring** — perimeter, dust, and fenceline focus; emphasis on incident response, complaint handling, and site rules.
- **Building / indoor air quality (IAQ)** — points are rooms, floors, and ducts; parameters include CO₂ and VOCs; emphasis on occupant experience, certification evidence, and integration with building systems.
- **Consumer app + global aggregator** — the operator's network is everyone's; emphasis on coverage, forecasts, health guidance, and city rankings.
- **Wildfire / emergency response deployments** — rapid-deploy networks for smoke events; emphasis on speed of installation and real-time public communication.

A variant remains a variant while the core model holds. If the product's primary loop becomes driving HVAC equipment rather than measuring and alerting, it has moved toward building control; if it generalizes to water, soil, and noise, it has become a multi-medium environmental monitoring platform.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Emissions Monitoring / CEMS | adjacent, often confused | measures at the regulated **source** (stack, duct) with defined reference methods for compliance reporting; air quality monitoring measures **ambient/environmental** concentrations at locations |
| Environmental Monitoring Platform | broader sibling | monitors multiple media (air, water, soil, noise); air quality monitoring is the air-specific instance with pollutant-specific semantics (parameters, indices, calibration practice) |
| Environmental Water Monitoring | sibling | same structural pattern (points + parameter time series + current/history) but water-quality parameters and water-specific rules |
| Building Management System / BMS | adjacent | BMS **controls** building equipment; air quality monitoring **observes** and alerts. Integration exists (monitoring feeds ventilation decisions), but control is not this Type's core |
| Environmental Data Platform / Public Data Portal | adjacent | portals publish existing data; air quality monitoring operates the measurement loop (devices, ingestion, quality assurance) behind the data |
| Weather Application | adjacent surface | weather apps present meteorological conditions; pollutant measurement is not their managed object. Air quality products show weather as context, not core |
| Industrial IoT Platform | generic substrate | handles arbitrary device telemetry; air quality monitoring adds pollutant-specific semantics — parameters, indices, calibration, health thresholds, regional standards |
| Sustainability / ESG Platform | downstream consumer | consumes environmental data for reporting and disclosure; does not operate pollutant measurement networks |

The most consequential boundary is with **Emissions Monitoring / CEMS**: both produce pollutant concentration records, but the measured subject differs — the ambient environment versus a regulated emission source — and with it the rules (methods, compliance, reporting) that shape the software.

## Representative Products

- **PurpleAir** — crowdsourced sensor network with a public real-time map and API
- **IQAir (AirVisual)** — consumer air quality app plus a global data aggregation platform and enterprise dashboard
- **Clarity Movement** — turnkey sensor networks with cloud dashboard, calibration support, and optional public OpenMap for agencies, cities, and industry
- **Kaiterra** — enterprise indoor/outdoor air quality monitors and data platform for building portfolios and certifications

These were chosen to span the market's customer tiers (individual → community → city/agency → enterprise/building) and product philosophies (open crowdsourced map, curated global aggregator, turnkey managed network, certification-driven IAQ platform).

## Sources

Research date: **2026-09-06**

- Clarity Movement — https://www.clarity.io/ and https://www.clarity.io/air-quality-monitoring-solution/cloud/dashboard (product and dashboard documentation)
- Kaiterra — https://www.kaiterra.com/ and https://www.kaiterra.com/dashboard (product and Data Platform documentation)
- IQAir — https://www.iqair.com/ and https://www.iqair.com/commercial-air-quality-monitors/airvisual-platform (AirVisual Platform and Enterprise Dashboard documentation)
- PurpleAir — https://www.purpleair.com/ and https://api.purpleair.com/ (site structure; see limitation below)

> Sourcing limitation: PurpleAir's website is a JavaScript application; only its navigation structure (real-time map, sensor registration, community, API documentation, segment solutions) was directly observable on 2026-09-06. Operational details for that product are intentionally not asserted here. Vendor help-center articles for the other products were not individually fetched; claims rely on the fetched product and platform pages. Precise numeric limits, correction factors, and certification specifics are recorded, where observed, only in the Research Notes.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
