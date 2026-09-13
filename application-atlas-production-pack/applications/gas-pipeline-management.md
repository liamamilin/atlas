# Gas Pipeline Management

## Overview

A **Gas Pipeline Management** application is the pipeline operator's system of record for the physical pipeline network itself. It maintains a connected model of the pipeline system — pipe segments joined and regulated by valves, regulator stations, compressor stations, storage, and supply or meter points — and manages the operator's pipeline lifecycle against that model: integrity and risk analysis, inspection and maintenance activity, anomaly and leak handling, pressure and hydraulic studies, and the compliance records these generate.

It answers a question no other system in a gas business answers: *what pipes and network equipment exist, where, in what condition, connected how — and what has been done, decided, and proven about them over time.*

The defining core is deliberately small — a connected network model of record, plus a pipeline-specific managed lifecycle bound to network locations. Neither alone is enough: a connected model without the lifecycle is a mapping platform; a lifecycle without the network model is a task tracker with no network semantics. This is also why the Type is distinct from the gas utility's customer and business systems: there the customer is the managed object, while here the network is, and customer information enters mainly as load or as affected parties.

## Users & Context

Primary users are the gas utility and pipeline operator staff whose work exists *because of the network*:

- **Pipeline integrity engineers and managers** — run risk and integrity programs: assess threats, manage inspection data, prioritize and schedule mitigation, keep the integrity plan current.
- **Network planning and hydraulic engineers** — model the system, study pressure and flow, evaluate load growth, new connections, design options and operating scenarios.
- **Compliance and regulatory staff** — maintain the records, audit trails and reports that demonstrate the operator meets pipeline-safety obligations in its jurisdiction.
- **GIS / network records staff** — steward the authoritative network model: keep features, attributes and connectivity accurate as construction and replacement change the system.

Secondary users:

- **Operations and emergency response** — use network connectivity and analysis to plan isolations, evaluate shutdown impact, and identify affected areas and customers.
- **Field crews** — receive and execute inspection, repair and replacement work; their completions flow back as records on the network.

The work context is asset-heavy, safety-regulated, and long-lived: pipelines persist for decades, so the system of record outlives systems around it, and its historical records (tests, surveys, repairs, incidents) carry real operational weight.

## Core Model

### The pipeline network model of record

The center of the system is a persistent, connected, identified model of the physical pipeline system:

```text
Pipeline network model of record
├── Pipe segments (material, size, pressure rating, age, location …)
├── Network equipment (valves, regulator stations, compressor stations …)
├── Storage, supply and metering points
└── Connectivity — how everything joins, upstream/downstream, what isolates what
```

The model is *connected*, not just catalogued: topology is a first-class property, which is what makes trace, isolation and impact reasoning possible. It carries engineering attributes per element and accumulates the managed history of each.

A structural fact of this market: the model may live in two places. In many operators it is mastered in an enterprise GIS, and pipeline applications consume it as master data. In others — and the sampled evidence shows this explicitly — the application holds and manages the network data itself, with GIS integration optional. Both postures define the same structure: an authoritative connected model somewhere in the system, governed as data.

### The managed lifecycle bound to the network

Around that model, the system accumulates the operator's pipeline lifecycle as records tied to network locations:

- **Integrity and risk records** — threat assessments and risk models over the network, in-line inspection data aligned to segments, the anomaly lifecycle (found → assessed → mitigated → verified), and the prioritized integrity plan that schedules inspection and mitigation activity. Products in this space make visibility into how risk results are produced an explicit feature, because operators must be able to stand behind the numbers.
- **Activity records** — inspection, maintenance, repair and replacement work, planned and tracked against the network and fed back from the field.
- **Analysis records** — pressure and hydraulic studies, load and capacity assessments, scenario and what-if evaluations of the connected model.
- **Compliance records** — the location-anchored evidence of safe operation: consequence-area and occupancy-class assessments, pressure-protection studies, activity compliance status, audit trails, versions and change history.

### Analysis engines over the model

Two engines are standard in mature products, sold in this market either as one suite or as sibling products:

- **Risk/integrity analysis** — configurable assessment models over network and inspection data; transparent, auditable calculation is a stated expectation in this domain.
- **Hydraulic/network analysis** — a computed representation of gas behavior over the model: pressures, flows, capacities under steady-state and, in mature products, transient conditions; used for design, load growth, overpressure assessment and operational scenarios.

The analysis results land back on the network record, which is what makes the system cumulative rather than episodic.

### Concept vs implementation

```text
Concept:  Connected network model of record
Ways it is realized:  enterprise GIS as master data · data held inside the application ·
                      industry-standard pipeline data models · custom data models

Concept:  Location-anchored compliance program
Ways it is realized:  jurisdiction-specific assessments and reports — the program shape is
                      general, the specific assessments and formats follow the operator's
                      regulatory regime
```

## How It Works

### Build and govern the network model

The model is created from surveys, as-built drawings, GIS data or imports, and — critically — *kept current*: when construction, replacement or repairs change the system, the model is updated and the change is governed (quality rules, validation, role-based edit rights). Because every downstream answer (isolation, risk, capacity, compliance) depends on the model, data quality is treated as a first-order concern, and products expose lineage, rules and review over it.

### Run the integrity loop

```text
Threat and inspection data in
→ risk assessment over the network
→ prioritized integrity plan (what to inspect, repair, mitigate, when)
→ activities executed and completed
→ results and anomalies recorded back on the network
→ re-assess; keep the audit trail
```

The loop is continuous and auditable. Integrity managers work from the plan; compliance staff can reconstruct, for any location and date, what was known, decided and done.

### Analyze the network

Engineers maintain a calculated representation of the system and use it forward and backward: capacity for expected loads, pressure behavior under normal and disturbed conditions, the effect of a new large customer, the consequence of isolating a zone, options for reinforcement. Where live measurement feeds are connected, model output is compared against them to keep the calculated model honest. Scenario comparison — evaluating alternatives side by side — is a typical working mode.

### Plan and respond through connectivity

Because the model is connected, routine and emergency questions are answered structurally: which valves isolate this segment; what is downstream of this break; which customers and loads are affected by this shutdown. Emergency and planned-outage analysis over the topology is a standard working pattern in the sampled evidence.

### Prove compliance

Compliance is not a side report: activity status, assessments, versions and changes are maintained so that annual reporting and audits draw from the same repository as daily work. Products in this space make audit trail and change tracking a headline capability, and reporting templates may be aligned to the operator's regional regulatory formats.

## Interfaces

Described conceptually; exact layouts vary by product.

### Map / network views

The network drawn geographically or schematically — the shared visual language of the Type. Typical information: segments and equipment, attributes on selection, overlaid analysis results (risk, pressure, inspection coverage). Primary actions: navigate, query, inspect element history, launch traces.

### Model editor

Where the network model itself is built and maintained: features, attributes, connectivity, assemblies (e.g., inside a station), and the governance rules over edits. Primary actions: add/modify features, validate connectivity, apply rules, manage versions.

### Integrity / risk workspace

Where the integrity program lives: risk dashboards over the network, threat and inspection data, the anomaly list and lifecycle, the prioritized plan. Primary actions: run assessments, triage anomalies, schedule activities, drill from enterprise view to a single segment.

### Analysis / scenario surfaces

Where the calculated model is exercised: build scenarios, set loads and supply conditions, run steady-state or transient studies, compare alternatives, review pressure/flow results on maps and charts. Primary actions: define scenario, run, compare, report.

### Activity planning and records

Boards and lists of planned and completed inspection/maintenance/repair work tied to network locations, with status, responsibility and history. Primary actions: plan, assign, record completion, attach documents.

### Compliance and audit surfaces

The record-facing view: assessments by location, activity compliance status, change history, document attachments, report generation. Primary actions: review status, produce reports, export audit evidence.

### Integration surfaces

Connections that feed the system: GIS (master network data), SCADA/control systems (live measurements for calibration), customer/billing systems (loads and affected-customer information), enterprise systems (spend, materials). Integration direction matters: pipeline management consumes from these; it is not the billing system, the control system, or the work-order system of general facilities.

## Important Rules / Behaviors

- **Connectivity governs answers.** Isolation, trace, affected-area and affected-customer determinations are computed from the network topology, so a wrong model produces wrong operational answers — the reason data governance on the model is treated as safety-relevant, not clerical.
- **The record is cumulative and auditable.** Assessments, activities, anomalies, versions and changes persist against the network for years; audit trail and change tracking are structural capabilities of this Type, not add-ons, because regulators and the operator's own management of change depend on them.
- **Master-data direction varies, governance does not.** Whether the network model is mastered in a GIS or inside the application, one authoritative source with rules, quality controls and role-based edit rights is the expectation; where a GIS is master, the application synchronizes with it rather than duplicating it.
- **Compliance is location-anchored and jurisdiction-shaped.** The *program shape* — consequence-area assessment, pressure-protection studies, activity tracking, periodic reporting — is general across products; the specific assessments and formats follow the operator's regulatory regime, and reporting templates may be aligned to those regional formats.
- **Analysis must be calibrated.** Where live measurement feeds are connected, calculated models are calibrated against them so the analysis remains trustworthy; analysis results carry operational and safety weight, so transparency of calculation is an expected property in this domain.
- **Customers appear as load, not as the managed object.** Customer and billing data enter for capacity studies and affected-party determination; the managed entity remains the network.

## Variants

Common forms the Type takes in the market:

- **By segment**: distribution networks (city-scale, dense valve counts, low-pressure systems), transmission pipelines (long-distance, compressor-driven), gathering systems, offshore — the core model holds across segments, and products may be licensed across several at once.
- **By packaging pole**: integrity-led products (risk, inspection, compliance at the center), simulation-led products (hydraulic analysis and network engineering at the center), and network-model platforms (the connected model as a horizontal layer) — the market realizes the Type across these poles.
- **By deployment**: vendor-hosted SaaS or on-premises installation, both common in this industry.
- **Fluid family**: gas is the defining medium; product families often extend with liquid and multiphase siblings for the same operator.
- **Program extensions**: mains replacement/modernization planning; energy-transition analysis (blended and alternative gases with composition tracking) as a growing modern variant.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Gas Utility Management | the utility's customer and business operation (customers, billing, rates, service orders) is the managed world; here the network is the managed object and customers appear only as load or affected parties |
| Utility GIS / network-model platform | holds the connected model, governance and tracing; lacks the pipeline-specific managed lifecycle (integrity, risk, hydraulic analysis, compliance programs) — that lifecycle is what makes this a management system |
| Utility Asset Management / EAM | manages maintainable assets as records; without connected-network semantics (topology, trace, isolation) it cannot do this Type's core work |
| SCADA | live telemetry and control of field instrumentation; pipeline management consumes SCADA measurements for calibration but does not itself run the process |
| CMMS / Maintenance Management | maintenance execution as work orders; here maintenance is one strand of a network-bound lifecycle, not the whole |
| Grid Operations Platform / Water Network Monitoring | same pattern over a different medium and physics; medium and failure semantics (pressure, gas release, integrity threats) keep the Types distinct |
| Energy Trading / gas scheduling | transmission pipelines also carry commercial machinery over capacity (transactions, nominations); that machinery is transaction-shaped rather than network-shaped and sits outside this Type |

The most important boundary is the one with Gas Utility Management: the two meet at service points and loads, and a gas utility runs both systems — but they answer different questions about different objects.

## Representative Products

- **DNV Synergi Pipeline** — the integrity-led pole: pipeline integrity and risk management across gathering, transmission and distribution.
- **DNV Synergi Gas** — the simulation-led pole: network analysis and hydraulic modelling for gas distribution, transmission and gathering systems.
- **Esri ArcGIS Utility Network** — the network-model pole: the connected network information model as a platform layer used by gas utilities.

The two DNV products are sibling poles from one vendor (integrity vs simulation) and were sampled deliberately as opposite ends of the same Type. The Esri product was sampled to document the network-model layer on its own terms — it demonstrates the shape a product takes when the managed-lifecycle half is absent.

## Sources

Research date: **2026-09-08**

- DNV — Synergi Pipeline (product page): https://www.dnv.com/services/synergi-pipeline/
- DNV — Synergi Gas (product page): https://www.dnv.com/services/synergi-gas/
- DNV — software products overview and pipeline category: https://www.dnv.com/software/products/ , https://www.dnv.com/services/?types=2688
- Esri — ArcGIS Utility Network (product overview): https://www.esri.com/en-us/arcgis/products/arcgis-utility-network/overview

> Sourcing limitation: several other vendors active in this market could not be reached from the research environment on 2026-09-08 (a midstream commercial/transaction software family, a major gas-distribution GIS vendor, and two utility-geospatial vendors — connection errors or timeouts). Claims touching those areas — the commercial nomination/scheduling side of transmission pipelines, and GIS-as-master-data patterns beyond what the sampled products document — are kept at qualified strength in this document, and no operational details from unreachable vendors are asserted anywhere. Vendor-marked figures (network sizes, history, blend percentages) observed on marketing pages are recorded in the Research Notes only.

Detailed observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
