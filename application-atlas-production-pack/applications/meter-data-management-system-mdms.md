# Meter Data Management System / MDMS

## Overview

A **Meter Data Management System (MDMS)** is the utility's system of record for billing-quality meter data. It ingests the raw readings and interval data produced by metering systems, runs them through systematic validation, estimation, and editing (the industry-standard **VEE** process) until they are fit to bill on, holds the resulting validated measurements as the utility's long-term authoritative consumption history, and computes and publishes billing determinants from that record to the systems that consume it — the billing/customer-information system, settlement processes, customer portals, and third parties.

The defining core is small:

```text
Measurement record of record
└── (raw reads in, from head-ends and other sources)
    └── VEE quality machinery (validate → estimate → edit)
        └── validated, billing-grade measurement history
            └── usage / bill determinants published to consuming systems
```

Everything else commonly associated with MDMS — the metering-point registry, exception work queues, analytics, virtual metering, archiving, settlement modules — is standard capability or an optional variant, not what makes the system an MDMS. In particular, the MDMS does **not** operate meters or the field communication network: that is the Advanced Metering Infrastructure (AMI) / head-end system upstream of it. The MDMS consumes what head-ends collect; it perfects, keeps, and serves the data.

## Users & Context

The operator is the **utility** (electric, gas, water, or multi-commodity; in some markets a vendor operates the system on the utility's behalf). The metered customer never touches the MDMS directly; customers see its data only through downstream portals.

Primary users inside the utility:

- **Meter-data analysts** — the day-to-day operators. They work the exception queues: review measurements that failed validation, resolve or override them, verify estimations, and release data for billing.
- **MDM administrators / implementation teams** — configure the quality machinery: validation and estimation rules, rule groups and their sequencing, usage-calculation rules, and the interfaces to head-ends and billing.
- **Billing and CIS teams** — downstream consumers; they request and receive billing determinants on the billing cycle and raise data questions back into the MDMS.

Secondary consumers of its outputs:

- **Settlement and market-facing teams** — use validated interval data for energy-market settlement (in some products as an add-on settlement module).
- **Analytics, loss-prevention, and grid-planning teams** — consume the measurement history and the non-billing channels (voltage, power quality, diagnostics) the system stores alongside consumption.

The work context is high-volume data quality operations: mature deployments process register and interval reads for populations from tens of thousands to many millions of meters, so the system is built around automated quality processing at scale, with people handling the exceptions the automation cannot resolve.

## Core Model

### The Defining Core

**The measurement record of record.** The central object is the individual measurement — a scalar reading (one value, e.g. a monthly register read) or an interval reading (one value per time interval, e.g. hourly kWh) — bound to an identified metering point: a specific meter or measuring component (channel) installed at a specific service point. Measurements accumulate across years as the utility's authoritative consumption history. Raw data enters as *initial* measurement data; what the system keeps and serves is the *final*, validated form. Without this accumulating, identified record, the product is a pass-through pipeline, not a system of record.

**The VEE quality machinery.** Validation, Estimation, and Editing is the process that turns raw collected data into billing-grade data. Validation rules test incoming measurements (missing reads, implausible values, gaps, inconsistencies between related channels). Estimation fills gaps and replaces failed values — and the result is *marked* as estimated rather than silently substituted. Editing covers corrections, including manual overrides by analysts under their own, less strict rule sets. Failures raise exceptions with severities; serious ones hold the measurement out of the final record until a person resolves it. The original (pre-VEE) and final (post-VEE) values remain distinguishable, so every change is auditable. Without this machinery the store holds raw telemetry, not billing-grade data.

**The billing-grade delivery loop.** The system computes usage — commonly called **bill determinants** — from the validated record: time-of-use-mapped interval consumption, scalar consumption, register readings, totals over a billing period. Determinants are published to consuming systems on an ongoing basis or on request: to the billing/CIS system on billing-cycle days, to settlement, to portals and third parties. When underlying data is corrected, the recomputed determinants reflow to consumers so bills can be corrected. Without this loop, the system is an archive that never reaches revenue.

These three are jointly load-bearing: a store without VEE is a raw archive; VEE without the record is a filter with no memory; delivery without the first two is a billing interface with nothing behind it.

### The Metering-Point Registry

Measurements are only useful when bound to what produced them. Mature products therefore hold a registry of **devices** (meters, communication modules), **device configurations** (which quantities a device measures), **measuring components** (the individual data channels — consumption, generation, voltage), **service points** (the premises where service is delivered), and **install events** (which device was installed where, when — including service connects and disconnects). Registry data is commonly synchronized from the CIS and asset systems. The binding of measurements to identified metering points is part of the defining core; the full registry machinery is standard capability that mature products carry.

### Standard Capabilities of Mature Products

- **Exception work queues** — failed validations and estimations become routed work items with severity and resolution tracking; resolved exceptions are retained in a closed state for reporting.
- **Manual edit / override** — analyst-created or analyst-corrected measurements, processed under distinct rule sets.
- **Consumption sync and profiling** — keeping scalar and interval data consistent; applying interval consumption shapes to scalar measurements.
- **Aggregation and virtual metering** — aggregated measurements and virtual meters/channels for complex metering arrangements (e.g. net metering, multi-meter billing).
- **Non-billing channels** — voltage, amperage, power-quality, and diagnostic data stored alongside consumption for grid and engineering use.
- **Analytics and reporting** — VEE-process monitoring, billing-exception metrics, operational dashboards.
- **Information lifecycle management** — rule-driven archiving and purging of the very large measurement store.
- **Integration spine** — standards-based inbound interfaces (head-end systems, file imports, manual entry) and outbound interfaces (billing/CIS, settlement, portals).

### One Structure, Many Implementations

```text
Concept:   Raw measurement intake
Realized as:  head-end feeds, file/CSV imports, manual entry, external-system imports

Concept:   Billing-grade quality gate
Realized as:  configurable VEE rule groups sequenced per meter type and data source,
              exception severities, estimation with condition codes

Concept:   Metering-point identity
Realized as:  device / measuring-component / service-point / install-event registries,
              meter-metadata repositories

Concept:   Determinant delivery
Realized as:  billing-cycle extracts to CIS, ongoing usage subscriptions,
              on-demand usage requests, settlement feeds
```

## How It Works

### The measurement lifecycle

```text
Head-end (or other source) delivers raw reads
→ stored as initial measurement data
→ VEE: validation rules run in defined sequence
   ├── passes → converted to final measurements in the record
   └── fails → exception raised, severity decides:
        ├── informational → noted, data proceeds
        └── issue/terminate → measurement held in exception state for analyst review
→ analyst resolves (correct, override, accept estimation) or estimation fills the gap
→ final measurement enters the validated record
→ usage calculation derives bill determinants from the record
→ determinants published to billing/CIS (billing-cycle days), settlement, portals
```

The lifecycle is a filtration pipeline: raw in one end, only clean validated data in the record at the other, with every transformation auditable.

### The exception loop

Analysts live in the exception queues. A typical loop: open the queue → inspect the failed measurement with its pre- and post-VEE values and condition codes → correct the value, override with a manual reading, or accept the system's estimation → release the measurement → the recomputed determinants flow to the consumers. Exceptions are not deleted when corrected; they persist in a closed state so quality problems remain reportable.

### The correction / re-billing loop

When data is found wrong after billing — a mis-read, a meter found faulty, an estimation later replaced by an actual read — the measurement is corrected in the record, reprocessed through VEE, and the affected usage is recalculated and re-published, letting billing re-bill. The record of record is what makes correction possible years later: the history, its quality markers, and its provenance are all retained.

### The registry loop

Meter exchanges, moves, and reconfigurations are registry events. Install events record which device sat at which service point when; usage calculations that span a billing period can legitimately draw on multiple devices and service points as equipment changes mid-period. This is what keeps measurement history continuous across the physical churn of the meter park.

### What the MDMS does not do

It does not talk to meters. Collection, device commands, and network management belong to the upstream head-end/AMI system; the MDMS receives what that system collects (and, in some products, can request an on-demand read *through* the head-end — but the device estate remains the head-end's). It does not produce invoices or hold tariffs; that is the billing/CIS system's. It sits between the two and guarantees that what crosses is billing-grade.

## Interfaces

Described conceptually; exact layouts vary by product.

### Exception / work queue

The analyst's primary surface.

- Typical information: failed measurements with severity, rule that failed, pre/post-VEE values, condition codes, linked meter and service point.
- Primary actions: inspect, correct or override a value, accept an estimation, release for billing, route to another team.

### Measurement / data explorer

Search and inspection over the record.

- Typical information: a metering point's measurement history (scalar and interval), quality markers, linked device, install events, usage results.
- Primary actions: search by meter/service point/account, view interval curves and register history, trace a value's VEE provenance, export data.

### Rule configuration (administrative)

Where the quality machinery is defined.

- Typical information: validation/estimation rules, rule groups and sequencing, eligibility conditions, usage-calculation rules, exception types and severities.
- Primary actions: create/modify rules, assign rule groups to meter types and data sources, tune estimation parameters.

### Usage / determinant configuration and monitoring

- Typical information: usage subscriptions (which service points' usage goes to which external system), calculation results, failed usage transactions.
- Primary actions: define or change a subscription, request usage on demand, reprocess a calculation, monitor billing-cycle extracts.

### Dashboards and reports

- Typical information: VEE pass rates, exception volumes and aging, billing-extract status, data-completeness metrics.
- Primary actions: monitor, drill into problem areas, export reports.

### Integration surfaces

Machine-facing: inbound from head-ends and import processes; outbound to billing/CIS, settlement, portals, and third parties.

## Important Rules / Behaviors

### Estimated data is marked, never silent

Estimation is a first-class outcome: estimated values carry condition codes distinguishing them from actual reads (system-estimated, externally estimated). Downstream systems and analysts can always tell what was measured from what was inferred. Some products suppress estimation during widespread outages so that missing data is not estimated from abnormal conditions.

### Nothing final fails silently

A measurement that fails a serious validation does not enter the final record; it is held in an exception state until a person resolves it. Severity levels separate interesting-but-nonblocking findings from blocking issues and from conditions that stop processing outright.

### Original values survive

Pre-VEE (original) and post-VEE (final) quantities are both retained, and exceptions persist in a closed state after correction. The system can always answer "what did the meter originally report, what did we change, why, and who changed it" — the auditability that billing-grade implies.

### The record outlives the devices

Meter exchanges and premise changes do not reset the record. Install events stitch measurement history together across equipment generations, and usage calculations handle periods that span device changes.

### Corrections reflow

Corrected measurements recompute determinants, and recomputed determinants re-publish to consumers. The delivery loop is continuous, not one-shot: billing-cycle extracts, ongoing subscriptions, and on-demand requests coexist.

### Billing quality is the gate

The system's output contract is "fit to bill on". Everything in its design — the VEE gate, the exception holds, the provenance, the determinant framing per rate structure — serves that contract. Data that has not passed the gate is not delivered as billing-grade.

## Variants

- **By commodity** — electric-only market MDMs; multi-commodity platforms covering electric, gas, water (and heat/cooling) over one record.
- **By market regime** — vertically integrated utilities consuming their own determinants; deregulated markets where validated interval data feeds settlement-quality roles and third-party suppliers.
- **By packaging** — standalone MDMS; the same functions embedded as modules inside a CIS/billing product (common in smaller utilities); settlement as an add-on or standalone module.
- **By deployment** — on-premises enterprise, cloud/SaaS, vendor-operated managed service.
- **By customer tier** — enterprise editions for large investor-owned utilities; essentials editions for municipal and cooperative utilities.
- **By data breadth** — consumption-only records vs records carrying non-billing channels (voltage, power quality, diagnostics) for grid engineering.
- **By era** — the Type predates AMI: interval-data processing for large commercial meters and settlement-quality data roles carried the same record + quality + determinant core before smart-meter rollouts; today's AMI-fed deployments are the dominant but not the defining shape.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Advanced Metering Infrastructure / AMI (head-end) | upstream sibling | AMI centers on the communicating device estate (collect, command, monitor, manage meters over a field network); MDMS centers on the billing-quality data record (validate, estimate, edit, store, share). Vendors ship them as separate products; AMI hands data off, MDMS perfects it. Some collection products are *marketed* as "meter data management" — naming drift, not structural identity |
| Utility Billing / CIS | downstream consumer | CIS holds accounts, tariffs, invoices, payments — money; MDMS holds the measurement record — data. The CIS requests and consumes billing determinants; the MDMS computes and publishes them. Validation functions embedded inside a CIS are a packaging variant of this Type |
| Industrial Historian | structural analog (plant domain) | both are time-stamped measurement archives, but the historian ingests control-system process tags for plant analysis, while the MDMS ingests revenue-meter data, runs meter-domain VEE, and serves revenue and settlement consumers |
| Energy Scheduling & Settlement | downstream consumer (market money) | settlement systems consume validated meter data as one input among market submissions and statements; the MDMS is the enterprise record those determinants are computed from. Settlement modules inside MDMS products are optional packaging |
| Data Warehouse / Analytics Platform | consumer | analytics consumes the governed record; without the VEE gate and determinant delivery the remainder is a warehouse, not an MDMS |
| Utility Revenue Assurance | downstream consumer | loss/theft detection consumes MDMS data; it does not hold the record |
| Customer Energy Management | consumer-facing sibling | portals surface consumption to customers; the consumer is the user there, the utility's data teams here |
| Master Data Management | name-adjacent only | MDM (master data) governs enterprise reference data generally; MDMS is domain-specific to meter measurements despite the shared acronym |

The most important boundary is with **AMI**: the head-end's central object is the device; the MDMS's central object is the data record. Remove device communication and management and an MDMS remains; remove validation and billing-grade storage and a head-end remains.

## Representative Products

- **Itron** — IEE Meter Data Management (and IEE Cloud); the globally most-deployed MDMS line, separate from Itron's OpenWay AMI and Temetra collection products; IEE MDM Settlements as standalone-or-add-on module
- **Landis+Gyr** — Meter Data Management System (MDMS), shipped separately from the Emerge head-end platform; VEE engines, exception management, and billing-cycle determinant extracts
- **Oracle** — Oracle Utilities Meter Data Management; hardware-agnostic enterprise MDMS consuming from any head-end via the separately shipped Smart Grid Gateway adapters; documented in a public user guide

The defining core was checked against the pre-AMI interval-data lineage (still shipped as a distinct product), the settlement-module packaging, and the CIS-embedded variant, to avoid over-fitting the definition to the current AMI-era, multi-commodity, cloud deployment pattern.

## Sources

Research date: **2026-09-09**

- Itron — Meter Data Management (solution page): https://na.itron.com/what-we-offer/meter-data-management
- Itron — IEE Meter Data Management (product page): https://na.itron.com/products/itron-enterprise-edition-meter-data-management
- Landis+Gyr — Software catalog: https://www.landisgyr.com/us/en/home/software.html
- Landis+Gyr — Meter Data Management System (product page): https://www.landisgyr.com/us/en/home/software/meter-data-management-system.html
- Oracle — Utilities Meter Data Management (product page): https://www.oracle.com/utilities/meter-data-management/
- Oracle — Meter Data Management documentation: https://docs.oracle.com/en/industries/energy-water/meter-data-management
- Oracle — MDM Business User Guide: Functional Overview; Glossary of Terms; About Initial Measurement Data; About VEE; About Usage Calculation (under the documentation URL above)
- Kamstrup — Electricity solutions (boundary evidence: AMI system bundling meter-data management): https://www.kamstrup.com/en-en/electricity-solutions

> Sourcing limitation: vendor operational manuals are behind customer portals and were not reachable; Siemens, Honeywell, and Sensus product surfaces were unreachable (errors/timeouts) and were not used. Oracle's public user guide provides the deepest operational evidence; Itron and Landis+Gyr evidence is product-page level, so their internal VEE/audit mechanics are described at the strength their pages support. Vendor scale figures (meters under management, reads per hour) are vendor positioning and are not asserted as facts. No precise retention periods or numeric limits are stated anywhere in this document for lack of direct evidence.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
