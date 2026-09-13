# Water Network Monitoring

## Overview

A **Water Network Monitoring** application is a drinking-water utility's operations watch over its own distribution and transmission network. It holds the network's live operating condition — pressures, flows, tank levels, and commonly water-quality parameters — as continuously refreshed measurements bound to identified points on the network and organized by its zones; it turns that condition into identified network events (leaks, bursts, pressure and quality anomalies, asset failures); and it manages each event through validation, investigation, field response, and verified closure, feeding water-loss accounting and network performance history.

The problem it solves is structural: a piped water network fails quietly. Most leaks never surface, quality degrades invisibly, and pressure problems announce themselves only as complaints or bursts. The application exists to make the network's operating state continuously visible and its failures detectable and managed — before customers report them.

Its defining core is small:

```text
Live network condition (measurements bound to network points, organized by zones)
└── Detection machinery (leak/burst/anomaly detection against expected behavior)
    └── Network event (managed object: type, location, magnitude, status)
        └── Event-to-response loop (validate → investigate → field response → verified closure)
            └── Water-loss accounting & network performance history
```

Everything else commonly associated with the category — acoustic logger fleets, machine learning, digital twins, NRW dashboards, pressure control — is widespread in current products but is an implementation or extension, not the defining core. A paper-era water department running district night-flow charts, sounding surveys, and repair orders satisfies the same skeleton without any of it.

## Users & Context

The primary users are the water utility's network operations staff:

- **Control-room / network operators** — watch the live network condition, receive and triage events, coordinate response.
- **Leakage / water-loss teams** — work the event queue, run night-flow and water-balance analysis, follow leaks from detection through repair verification.
- **Water-quality operations** — watch residual disinfectant, turbidity, and related signals; handle quality events.
- **Engineering and planning** — consume network performance history, DMA-level loss statistics, and failure patterns for renewal and investment decisions.
- **Managers** — track KPIs (water loss, response times, data availability) and report against leakage or non-revenue-water objectives.

Field crews are not direct users of the monitoring application in most deployments: the event case lives here, but the work order and the crew live in the utility's field-service and asset systems, which the monitoring application feeds through integration. In managed-service variants, the vendor's own analysts work the detection layer and hand verified "points of interest" to the utility's technicians.

The context is a utility operating a distributed physical network under economic and often regulatory pressure to reduce leakage (frequently framed as non-revenue water) and to maintain safe water quality — with instrumentation that is always partial: sensors exist at some points, meters at others, and large parts of the network are observed only indirectly.

## Core Model

### The Defining Core

Three structures, held jointly. Remove any one and the product stops being a water network monitoring application.

**1. The live network condition.** The network's operating state held as continuously refreshed measurements — pressure, flow, level, and commonly quality parameters (residual chlorine, turbidity, pH-class) — each bound to an identified point on the network (a meter, sensor, logger, or telemetry point at a specific location), organized by the network's zone or area structure, and accumulating as time series. The zone organization is what makes it a *network* watch rather than a collection of devices: individual measurements gain meaning from their position in the network (a district's night flow, a zone's input versus consumption, a PRV's upstream/downstream pressures).

**2. Detection machinery.** The systematic conversion of the condition into identified network events. The canonical detections are leaks and bursts — found by comparing observed behavior against expected behavior (learned from history or computed from a hydraulic model), by night-flow and water-balance analysis at zone level, or by dedicated detection means such as acoustic logger networks. Around that core: pressure anomalies (drifts, transients), quality anomalies, reservoir level deviations, and asset failures (pressure-reducing valve faults, broken meters, telemetry and data-quality issues). Detection may be automated, human-executed survey practice, or both — the invariant is that the condition is systematically worked into named events, not merely displayed.

**3. The event-to-response loop.** Each detected event is a tracked case — type, location/zone, magnitude, estimated water loss, status — driven through validation and prioritization, investigation (desk analysis and/or field work), field response (reached through work-order integration with the utility's asset and field-service systems, or through a managed-service handoff), and verified closure. Outcomes accumulate into water-loss accounting and the network's performance history.

The binding: the subject is the utility's **own piped drinking-water network**. Point the same machinery at receiving waters and it becomes environmental monitoring; at a building's plumbing and it becomes premises leak detection; at generic field units with point semantics and it becomes SCADA.

### Standard Capabilities

Mature products commonly carry most of the following. They make the watch practical; they do not define the Type.

- **Zone/DMA organization** — the working geography: metered districts (district metered areas), pressure zones, and — where physical metering is absent — virtual districts inferred from data.
- **Water-loss accounting** — night flow/nightline indicators, zone water balance, leakage-index KPIs, non-revenue-water trends, and reporting against leakage targets.
- **Quality signals and quality events** — real-time quality parameters inside the network condition, with anomaly detection (e.g. disinfectant residual loss, taste/color indicators).
- **Multi-source integration** — SCADA and telemetry, dedicated pressure/flow/level/quality sensors, acoustic logger systems, smart-meter (AMI/AMR) data, GIS, hydraulic models, customer calls and complaints.
- **Corroboration and prioritization** — combining independent indications about the same area to raise confidence and set response priority; per-role event queues.
- **Data-quality machinery** — data-availability and data-quality scores, gap filling, missing-data modeling; telemetry failures treated as detectable events in their own right.
- **Dashboards and reporting** — management KPIs (water loss, response time to events, data availability) and operational reports drillable to zone and event level.
- **Alarm configuration** — thresholds and alarm rules across data channels.
- **Asset condition monitoring** — PRV condition, meter health, reservoir behavior as standing watch items.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:   the network's expected behavior
Implementations:  statistical/learned models from historic data · calibrated hydraulic
                  models and digital twins · fixed engineering thresholds

Concept:   leak detection
Implementations:  flow/pressure anomaly analysis · night-flow and water-balance
                  analysis · acoustic logger networks (fixed or redeployable) ·
                  satellite imagery analytics · in-pipe sensing devices ·
                  smart-meter consumption analytics

Concept:   zone organization
Implementations:  metered district metered areas · virtual districts/sectors ·
                  pressure zones

Concept:   field response
Implementations:  work-order/EAM integration · managed-service handoff
                  (vendor analysts hand verified locations to utility crews)
```

A reader who has only seen one implementation — say, an AI acoustic-logger platform — should still recognize a hydraulic-analytics product, or a paper-era night-flow office, as the same Type.

## How It Works

The operational loop runs continuously:

```text
Instrument & organize
→ ingest & condition data
→ learn/hold expected behavior
→ detect & declare events
→ validate & prioritize
→ investigate & respond (field work via integration)
→ verify & close
→ account & improve
```

**Instrument and organize.** The utility places measurement points on the network — flow and pressure sensors, level measurement on reservoirs, quality probes, acoustic loggers, telemetry units — and organizes them into zones or districts. The application's world is built on this frame: which points exist, where they sit, which zone they belong to.

**Ingest and condition data.** Feeds arrive from SCADA and telemetry systems, dedicated loggers, smart meters, and manual readings. Products commonly cleanse the streams, fill short data gaps, and score data availability and quality — because detection is only as good as the data, and a silent meter is itself a finding.

**Learn or hold expected behavior.** The system establishes what "normal" looks like: statistically learned supply behavior (demand patterns, seasonal effects) and/or a calibrated hydraulic model of the network. This is the reference against which deviation becomes meaningful.

**Detect and declare events.** When observed behavior departs from expected behavior significantly — a district's night flow creeping upward, a step change in a zone's input flow, an acoustic correlation between logger positions, a chlorine residual decline — the system declares an event. Slow-developing leaks are identified as trends, not just sudden breaks. External alert sources (acoustic systems, customer calls, other detection services) are accepted into the same event stream.

**Validate and prioritize.** Events are checked against other indications — a second, independent detection in the same area raises confidence; contradicting data lowers it. Events are prioritized by magnitude, estimated water loss, and risk, forming operators' working queues.

**Investigate and respond.** Desk investigation narrows the location; field response — leak detection crews, repair gangs, valve operations — is dispatched through the utility's work-order and asset-management systems, with the event case tracking progress. In managed-service variants, the vendor's analysts perform the detection and validation work and hand verified locations to the utility's technicians.

**Verify and close.** Closure is earned, not declared: the repair is verified (flow/pressure/acoustic evidence returns to normal) before the event closes, and the outcome — water lost, cost, repair effectiveness — is recorded.

**Account and improve.** Across events, the system maintains the water-loss picture: zone-level balance, leakage indicators, trends over time, response performance. This feeds management reporting, regulatory leakage reporting where applicable, and — in products that reach that far — renewal and investment planning.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Network map / geographic dashboard

The spatial entry surface.

- the network with zones and monitoring points, event locations, live values at points
- primary actions: locate events geographically, inspect a point or zone, drill into detail

### Event list and event detail

The working surface for operators and leakage teams.

- event queue with type, zone, magnitude, estimated water loss, status, age; per-event detail with the contributing data (flow/pressure graphs, acoustic results, related assets), status history, and linked field activity
- primary actions: validate, prioritize, assign, annotate, track field progress, verify and close

### Zone / DMA view

The water-loss working surface.

- hierarchical zone list with performance scores (leakage indicators, data quality, data availability, water loss); per-zone balance and night-flow detail
- primary actions: compare zones, drill into a zone's measurements and events, adjust zone configuration

### Time-series / trend charts

The analytical surface.

- measured values over time against expected behavior; event windows marked; multi-point comparison for correlation analysis
- primary actions: inspect periods, overlay points, export for analysis

### Management dashboard

The KPI surface for managers.

- water loss, event counts and response times, data availability, zone performance against targets
- primary actions: track performance, generate reports

### Reports

- operational and management reports: event history, water-loss accounting, zone performance, data quality; in regulated markets, leakage-reporting support

### Configuration and integration surfaces

- monitoring-point and zone configuration; alarm rules; integration setup toward SCADA/telemetry, GIS, metering, work-order and customer systems

## Important Rules / Behaviors

**Detection is against expected behavior, not just thresholds.** The characteristic detections — hidden leaks, slow-developing losses — come from deviation against learned or modeled behavior. Pure threshold alarming exists but misses the slow leak; mature products therefore learn or compute "normal" and watch for departure.

**Night-time analysis is the domain's standing technique.** Leak signals are read when consumption is lowest — night-flow indicators, night-time acoustic recording — because genuine usage masks leakage during the day. This behavior is visible across the category regardless of detection substrate.

**Corroboration raises confidence.** An alert confirmed by an independent second source (a different detection system, a customer call, a neighboring zone's data) is treated as more actionable; products explicitly integrate external alert feeds for this reason and support multi-source validation in the event workflow.

**Data quality is a first-class concern.** Data availability and quality are scored and surfaced as KPIs; missing data is modeled or flagged rather than silently ignored; telemetry and meter communication failures are themselves detectable events. A monitoring system that cannot tell "no leak" from "no data" is unusable.

**Closure is earned by verified repair.** An event closes when the field response is verified — measurements return to expected behavior — not when someone marks it done. Outcomes (water lost, cost, repair effectiveness) accumulate into the network's performance record.

**Decision support, not control.** The application watches and directs attention; it does not, in its defining form, operate the network. Supervisory control lives in SCADA and telemetry control systems, which the monitoring application consumes as data. The notable variant is pressure management, where a product class does control pressure-reducing valves and pumps — held as a variant, not the core.

**The zone structure is the working geography.** Events, balances, KPIs, and responsibilities are organized by zones. Where physical metering cannot define a district, virtual districts inferred from data serve the same role.

**Water loss is the economic spine.** Leakage reduction is the category's dominant justification: night-flow and water-balance accounting, leakage indicators, and leakage-target reporting are the numbers the application exists to move. The losses counted here are *real* losses — physical water escaping the network. Losses from meter inaccuracy, theft, and billing (apparent losses) belong to the utility's revenue-assurance discipline, not to network monitoring.

## Variants

Common forms the Type takes in the market:

- **Pure-play event-management SaaS** — analytics-led detection and central event management over the utility's existing data sources and detection systems; cloud-deployed; the utility keeps its SCADA and control estate.
- **Operator-owned software suites** — monitoring products built and sold by water-service operators, commonly modular (hydraulic base module with optional quality and pressure modules), often bundled with the vendor's operational services.
- **Conglomerate platforms** — whole-water-cycle platforms from metering and device vendors: vendor-agnostic data integration feeding modular applications (network monitoring, leak detection, meter analytics, asset planning), sometimes with connected hydraulic models and digital twins.
- **Device-led specialists** — detection hardware (acoustic loggers, correlators, telemetry units) with an analytics layer over the logger fleet; often sold with managed services in which the vendor plans deployments, runs analysis, and hands verified leak locations to utility crews.
- **Control-led pressure management** — the control-inclusive variant: remote control and automatic optimization of pressure-reducing valves and pumps as the leak-reduction strategy, with monitoring and event management around the controlled zones.
- **Detection-substrate variants** — hydraulic analytics, acoustic networks, satellite analytics, in-pipe devices, smart-meter analytics; frequently combined.
- **Regulatory-context packaging** — in markets with formal leakage targets, the same Type packaged around regulatory leakage reporting; elsewhere around economic non-revenue-water reduction.

A variant remains a variant while the defining core holds. When the surface shifts to the whole utility business (customers, billing), that is Water Utility Management; when it shifts to receiving waters, that is Environmental Water Monitoring; when it shifts to supervisory control of field units, that is SCADA.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| SCADA | complementary, upstream | supervisory control machinery over field units with point-based semantics; provides data and control; no water-network semantics, no leak/event management. The monitoring application consumes SCADA data; vendors themselves describe the two as complementary systems |
| Industrial Historian | substrate | archival engine for process measurements; a data source for network monitoring, not an operations watch |
| Utility GIS | frame provider | holds the as-built network model of record (connectivity); enters monitoring as context, not as the watched live condition |
| Utility Asset Management | adjacent, downstream | plant register and asset lifecycle; failures detected here become asset records and work orders there |
| Utility Field Service Management | adjacent, downstream | crews and work orders; the event case lives here, field execution lives there |
| Utility Revenue Assurance | sibling discipline | apparent losses (metering, theft, billing) vs this Type's real losses (physical leakage) — the two split the water balance |
| AMI / Meter Data Management | data provider | the metering estate and billing-grade consumption data; consumed as one input; customer-meter analytics is the metering side's territory |
| Outage Management System (electric) | structural analog | event → field response shape, but outage prediction/restoration on an electric connectivity model vs leak detection/repair on hydraulic evidence |
| Water Utility Management | sibling vertical | the utility's customer-service business system of record (accounts, charges, bills); this leaf is the operations watch over the network |
| Water Quality Management | sibling, program-side | the quality-assurance/compliance program (sampling, standards reporting) vs the operational real-time quality signal inside the network condition here |
| Environmental Water Monitoring | different subject | receiving waters and environmental media vs the utility's own network |
| Wastewater Compliance Management | different subject | permitted-discharge compliance vs distribution-network operations |
| Smart City Operations Platform | broader | cross-domain city operations vs single-domain network watch; monitoring products may feed city platforms |
| IT Network Monitoring | name collision only | data-network infrastructure monitoring; a different domain entirely |

The most important boundary is with SCADA: the two coexist in the same utility, and the monitoring application is defined by what SCADA does not carry — network-zone semantics, leak/water-loss detection, and the managed event-to-response loop.

## Representative Products

- **TaKaDu** — pure-play cloud Central Event Management for water utilities
- **SUEZ — AQUADVANCED Water Networks** — operator-built real-time network supervision suite (hydraulic / quality / pressure modules)
- **Xylem Vue (powered by GoAigua)** — vendor-agnostic water data platform with network monitoring and leak-detection applications
- **Ovarro** — acoustic leak-detection and telemetry specialist (Enigma loggers, LeakInsight analytics, managed leakage services)
- **i2O Water** — pressure-management-led smart network solutions (monitoring, analytics, event management, PRV/pump control)

The engineering-software pole of the market (hydraulic-model-integrated network monitoring products from simulation vendors) is recognized as part of this Type but could not be documented from primary sources in this research pass; see Sources.

## Sources

Research date: **2026-09-10**

- TaKaDu — Central Event Management solution page: https://www.takadu.com/solution/ ; About: https://www.takadu.com/about-us ; partnership/press items via PRNewswire and Water Finance & Management
- SUEZ — AQUADVANCED Water Networks product page: https://www.suez.com/en/water/water-conservation/water-networks/aquadvanced/water-networks ; AQUADVANCED range: https://www.suez.com/en/water/water-conservation/water-networks/aquadvanced ; water-networks overview: https://www.suez.com/en/water/water-conservation/water-networks ; UK real-time management page: http://suez.com/en/uk/water-network-management/real-time-management-and-optimisation/real-time-water-networks-management ; solutions brochure PDF (suez.com media library)
- Xylem Vue — platform and drinking-water pages: https://www.xylem.com/en-us/brand/xylem-vue , https://www.xylem.com/en-us/brand/xylem-vue/platform , https://www.xylem.com/en-us/brand/xylem-vue/platform/drinking-water , https://www.xylem.com/en-us/campaigns/vue/real-time-water-network-monitoring
- Ovarro — Enigma leak-noise logger pages and brochure: https://ovarro.com/en/global/solutions/monitoring--control-devices/data-loggers--leak-noise-loggers/leak-noise-loggers--correlators/enigma/enigma and related product pages; Yorkshire Water smart-network trial: https://ovarro.com/en/global/news/ovarro-collaborates-on-major-smart-water-network-trial ; Southern Water LeakNavigator case study (SWAN forum publication)
- i2O Water — solutions pages: https://en.i2owater.com/solutions , https://en.i2owater.com/solutions/advanced-pressure-management ; Control Logger announcement: https://en.i2owater.com/i2o-launches-control-logger ; support portal: https://support.i2owater.com/hc/en-gb

> Sourcing limitations: Xylem's official pages returned 403 to direct fetch; their content was taken from official-page search excerpts and is held at reduced strength. The engineering/hydraulic-modeling vendors' water-network monitoring products (Innovyze/Autodesk, Bentley) were not reachable in this pass or in prior passes; no claims in this document depend on them. Vendor-published performance figures (leakage percentages, event counts, savings claims) were used only as evidence that structures exist, not as factual baselines, and are kept in the Research Notes. Operational specifics that depend on documentation depth — numeric limits, exact event-declaration timing, module pricing — are intentionally not stated.
