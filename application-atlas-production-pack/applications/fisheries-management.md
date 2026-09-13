# Fisheries Management

## Overview

A **Fisheries Management** application is the system of record for governing wild-capture fishing: it organizes its world around defined fisheries — identified fish stocks in defined management areas — each carrying the rules and limits under which capture is allowed. Within that frame it holds records of the authorized participants (vessels, fishers, and their rights or entitlements), records the fishing activity itself (trips, fishing events, effort) and the catch taken or landed, and then acts on that record: validating and correcting it, balancing catch against entitlements and limits, producing the returns and registers the regime requires, and accumulating the data that governs the resource over time.

The defining core is small:

```text
Fishery (stock × area) with its governing rules and limits
└── Authorized participants: vessels / fishers, permits, rights or entitlements
    └── Fishing activity of record (trips, fishing events, effort)
        └── Catch / landing records (species × quantity, at sea or at landing)
            └── Management loop: accounting against limits · validation ·
                reporting · registers · resource data record
```

Everything else commonly associated with the category — quota shares and annual entitlements, electronic logbooks, vessel position reporting, observer and electronic-monitoring programs, public registers, stock-assessment feeds — is widespread in mature implementations but is not what makes the software fisheries management. A paper-era administration running license registers, catch logbooks, and landing declarations satisfies the same core; a vessel-tracking dashboard with no catch records and no governed fishery does not.

When the software instead manages reared populations in owned production units with stocking-feeding-harvest cycles, it belongs to Aquaculture Management, a neighboring Type. When it manages vessels purely as logistics assets, it belongs to Marine Fleet Management.

## Users & Context

The Type spans two cooperating seats, and most real systems are built around one of them:

**The administration seat** (fishery authorities and their contracted registry operators):

- **registry/administration staff** — maintain the registers of participants, vessels, permits, and entitlements; process applications and transfers; run the reporting machinery.
- **fisheries officers / compliance staff** — watch reported catch against limits, monitor vessel positions, work validation exceptions and suspected breaches.

**The industry seat** (fishing companies, vessel operators, and their service providers):

- **skippers and crew** — record the trip's fishing events and catch, at sea or at landing.
- **company administrators** — hold and trade entitlements, submit periodic returns, check balances.
- **monitoring providers** — independently verify catch at the dock or at sea (observers, electronic monitoring) and deliver the record to authorities and industry alike.

The work context is distinctive: fishing is dispersed over the sea and regulated as a shared natural resource, so the record must be trustworthy enough to carry legal consequence, and it is produced by several independent hands — the fisher's own declaration, an independent verifier, and automatic position reporting — rather than by one office. Duty-of-record accuracy, not speed, is the operating constraint.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the software stops being recognizable as fisheries management:

- **The fishery as the governing frame.** The system's world is organized around defined fisheries — typically a fish stock (a species in an area) inside a management area — each carrying the rules that govern its capture: catch limits or entitlements, effort limits, seasons and closures, gear rules. These limits are applied configuration, not stored documents; the system computes and enforces against them. Without the frame, records have no governed subject and the product degenerates into generic marine operations or inert statistics.
- **The fishing-activity and catch record.** Persistent, individually identified records of fishing operations: trips or voyages; fishing events within them (gear used, where, when, how much effort); and the catch — species and quantity — declared at sea, at landing, or verified independently. Every record is attributed to an authorized participant within a fishery. Without the record, there is nothing to manage.
- **The management loop over the record.** The record has consequence: catch is accounted against entitlements or limits (with balances, overage treatment, and closure effects), declarations are validated and corrected, obligations are reported (regulatory returns, inter-governmental reporting, public registers), and the accumulated record becomes the resource's data history — the basis for assessing stock and adjusting the rules. Without the loop, the product is a fishing logbook, not a management system.

The three legs are interdependent: the frame gives the records meaning, the records give the frame effect, and the loop closes the circle.

### Standard Capabilities in Mature Products

These appear across the researched implementations and make the software practical, but they do not define the Type:

- **Registers of record** — vessels, fishing permits, licensed receivers or processors, and quota or entitlement holdings, maintained as authoritative registers.
- **Entitlement machinery** — in quota-regime fisheries: shares of a total allowable catch, annually derived entitlements in weight, transfers and purchases between holders, running balances.
- **Electronic catch reporting** — logbook applications in which fishers declare every fishing event; a validation process on receipt; error-correction workflows back to the declarant.
- **Periodic returns** — monthly or per-period harvest and landing declarations that reconcile detailed event reports into accountable totals.
- **Vessel position reporting** — automatic transmission of vessel positions during trips (dedicated position-reporting devices, or vessel tracking from AIS-class systems), retained as the effort and compliance record.
- **Independent verification** — observers at sea, dockside monitoring of landed catch, and camera-based electronic monitoring with review tooling.
- **Reference/master data** — species and stock codes, management areas, gear types, conversion factors, vessel lists — the shared vocabulary of every record.
- **Reporting outputs** — regulatory returns, commission-level reporting templates, aggregate catch reports (catch against entitlement, catch by period), and public registers where the regime provides them.
- **Field-side capture** — mobile and offline-capable collection apps, from vessel logbooks to landing and market surveys in small-scale fisheries.
- **Monitoring and alerting** — real-time fleet or compliance views, closed-area and protected-zone alerts, event detection.

### One Structure, Many Implementations

The core model is conceptual; products realize each concept differently:

```text
Concept:     The fishery's governing frame
Implements:  stock × quota-management-area with TAC-derived limits (quota regimes);
             license + effort limits + seasons + closures (effort regimes);
             community rules for artisanal fisheries

Concept:     Authorized participants
Implements:  vessel register + permits + quota shares + annual entitlements;
             license registers; community fisher lists

Concept:     The activity-and-catch record
Implements:  e-logbooks with per-event reports; paper logbooks digitized on receipt;
             landing/market survey forms; observer and electronic-monitoring records;
             position-reporting streams

Concept:     The management loop
Implements:  catch-vs-entitlement balancing with overage charges; validation and
             correction queues; statutory returns; commission reporting templates;
             public registers; catch-and-effort databases feeding stock assessment
```

A reader who has only seen one implementation — say, a quota registry — should still be able to recognize a data-management or small-scale fisheries product from the same core.

## How It Works

### Establish the frame and its participants

```text
Define the fisheries (stock × management area) and their limits
→ register participants: vessels, permits, entitlements
→ publish reference data (species codes, gear types, areas)
```

This is the setup that makes every later record meaningful: each catch record will name a stock in an area, a vessel, and a right exercised.

### Record the fishing activity and catch

```text
Trip begins (vessel departs; position reporting starts where required)
→ fishing events recorded as they occur — gear, location, effort
→ catch declared per event (at sea, via logbook) or at landing
→ independent verification where the regime requires it
  (observers, dockside weighing, electronic monitoring)
→ records flow into the system and pass validation
```

Capture is deliberately multi-channel. The fisher's own declaration, an independent verifier's record, and the automatic position stream are different hands on the same record world; in mature regimes the declaration channel is standardized so third-party logbook software can submit into the system of record.

### Account for the catch against the frame

```text
Validated event reports and landings accumulate per participant
→ periodic return reconciles the detail into accountable totals
→ catch balanced against available entitlement or limits
→ overage handled per the regime's rules (charges, penalties, forfeiture)
→ balances and history visible to the participant and the authority
```

This loop is the heart of the quota-regime form; in effort- and data-managed regimes the same loop reconciles activity against licenses, effort caps, or data obligations instead of weight entitlements.

### Report, verify, and govern the resource

```text
Regulatory returns and commission reports produced from the record
→ registers and aggregate reports published where the regime provides
→ accumulated catch-and-effort data feeds stock assessment
→ assessment findings feed back into the frame's limits — and the cycle repeats
```

### Core vs Common vs Optional

**Defining core** — without these, not fisheries management:

- the fishery as governing frame (defined stocks/areas with applicable limits)
- authorized participants holding rights and obligations within it
- the fishing-activity and catch record, attributed to participants
- the management loop that gives the record consequence

**Standard capabilities** — present in most mature implementations:

- registers, permits, entitlement machinery and transfers
- electronic catch reporting with validation and corrections
- periodic returns and reconciliations
- position reporting, observer/dockside/electronic-monitoring verification
- reference data, reporting outputs, public registers, field capture apps, monitoring views

**Variant / optional** — depends on regime, region, and segment:

- quota trading and market functions
- protected-species interaction reporting hooks
- science-layer interfaces (assessment tools, conversion-factor management, CPUE analytics)
- supply-chain/traceability extensions from the landing onward
- small-scale/artisanal and recreational populations

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product and seat.

### Client / operator portal

The participant's home surface (fishing company, permit holder).

- typical information: permits and entitlements held, current balances, transaction history, pending obligations
- primary actions: apply or renew permits, transfer or purchase entitlements, submit returns, correct reported records, run own reports

### Catch-reporting surface (logbook / e-reporting app)

The fisher-side capture surface, at sea or at landing.

- typical information: trip context, fishing events (gear, position, effort), catch lines by species and quantity, prompts for protected-species interactions
- primary actions: submit fishing and non-fishing events, amend prior submissions, work offline and sync

### Records and validation workspace

The administration-side surface of record.

- typical information: submitted reports with validation status, error queues, participant and vessel registers
- primary actions: correct or confirm records, process applications and transfers, maintain registers and reference data

### Monitoring and compliance view

The oversight surface.

- typical information: vessel positions and activity, catch vs limit standing, alerts (closed areas, limits, declared events), verification status
- primary actions: inspect vessel activity, verify reported catch against observed catch, escalate exceptions

### Reporting and registers

The output surface.

- typical information: regulatory returns, aggregate catch reports (catch against entitlement by period), public register extracts
- primary actions: generate, inspect, download; publish register information where the regime provides

## Important Rules / Behaviors

### The record carries legal consequence

Declarations are statutory obligations, not analytics input: every fishing event is reportable in mature regimes, records are retained and attributed to identified vessels and holders, and corrections are themselves recorded. This evidentiary posture — validation on receipt, auditable corrections, independent verification — is the Type's defining discipline.

### Catch is balanced against limits

In quota regimes, reported catch is reconciled against available entitlement; exceeding it triggers defined consequences (overage charges or penalties). In effort regimes the same reconciliation runs against licenses and effort caps. The balance — not the raw report — is the management fact.

### Multiple hands, one record

The fisher declares; the verifier confirms; the position device reports. Divergence between channels is not an error state but the system's working condition, handled through validation, cross-checks, and correction workflows.

### The frame defines what a record means

A catch record is always a catch **of a stock, in an area, against a right**. Stock codes, management areas, gear types, and conversion factors are governed reference data; a record without them is not computable against the frame.

### Participants see their own record

The participant's view (balances, history, obligations) is drawn from the same record the authority manages — one record, two projections. Public registers and aggregate reports extend the same record outward where the regime requires transparency.

## Variants

- **Quota-regime administration** (the registry-of-record form) — statutory registers, individual transferable shares with annually derived entitlements, transfers and trading, monthly reconciliation of catch against entitlement, public registers. The dominant form in heavily commercialized fisheries.
- **National fisheries data management** — catch-and-effort databases for fisheries administrations, often covering small-scale and artisanal as well as industrial fleets; reporting toward regional commissions; the management loop runs through data quality, reporting, and assessment rather than quota balancing.
- **Monitoring-service implementations** — observer, dockside, and electronic-monitoring programs operated for regulators and industry; the verification layer of the same record world, often productized with onboard hardware and review tooling.
- **Small-scale / artisanal variants** — data collected at landing sites and markets, sometimes without vessel identity; survey apps for enumerators; community-level frames.
- **Regime families** — quota-based, effort-based, license-plus-limits; the core survives all of them, which is why the definition carries "limits and obligations" rather than any specific instrument.
- **Regional-commission contexts** — obligations and reporting templates defined by inter-governmental bodies, layered on national systems.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Aquaculture Management | sibling, most confused | reared populations in owned production units across stocking→harvest cycles; no wild-capture entitlements, effort records, or landings; remove the fishery frame and capture records, add owned units and a rearing loop, and you are there |
| Marine Fleet Management / Vessel Operations Platform | adjacent | vessels as logistics/maintenance/crew assets; here vessels are authorized participants inside a fishery's record world, subordinate to it |
| Government Licensing Management | adjacent | licensing is one register slice here (permits), embedded in the catch/effort/entitlement world; that Type centers the licensing program itself |
| Food Traceability Platform | downstream | chain of custody from landing to consumer; this Type's record ends at (or shortly after) the landing |
| Environmental Monitoring Platform | consumer | observes environmental conditions; here the "monitored" resource is governed through its own catch record |
| Public Data Portal | output consumer | registers and aggregate reports are outputs of the record; the portal publishes without holding it |
| Vessel-tracking / transparency platforms (monitoring layer) | supplier, not the Type | activity visibility and alerts feed the record world but hold no entitlements, catch records of record, or obligations |
| Stock-assessment science tools | consumer layer | analyze the accumulated record to advise the frame's limits; analysis instruments, not the system of record |

The boundary that most often causes confusion is with Aquaculture Management, because both concern fish and water. The structural test is the object model: a wild stock under a fishery's governing frame, recorded through capture effort and catch (Fisheries Management) versus a reared population in an owned production unit, recorded through a stocking→harvest cycle (Aquaculture Management).

## Representative Products

- **Fishserve** (New Zealand) — operates the administration system for the country's Quota Management System: client portal for permits, entitlement transfers, returns and balances; electronic reporting connections for third-party logbooks; public registers and aggregate catch reports.
- **SPC — TUFMAN 2 and the e-reporting suite** (Pacific Community) — national fisheries data management for Pacific Island countries: cloud catch-and-effort database, query and reporting tools, field collection apps from vessel logbooks to landing surveys.
- **Archipelago Marine Research** (Canada) — fisheries monitoring services and technology: at-sea observers, dockside monitoring, electronic monitoring, with onboard and onshore products spanning e-logbooks to real-time fleet monitoring.

Boundary specimens studied to hold the edge: **Global Fishing Watch** (public transparency/monitoring platform) and **Pelagic Data Systems** (artisanal-fleet vessel tracking and analytics) — both feed the Type without holding its record.

## Sources

Research date: **2026-09-08**

- Fishserve — https://www.fishserve.co.nz/ (home, Client Website, QMS and Regulations, eLogbook Providers, Obligations, Catch Reports, About Public Registers)
- SPC Fisheries, Aquaculture and Marine Ecosystems — https://fame.spc.int/ and https://fame.spc.int/fisheries-data/database-systems-and-access
- Archipelago Marine Research — https://www.archipelago.ca/
- Global Fishing Watch — https://globalfishingwatch.org/
- Pelagic Data Systems — https://pelagicdata.com/

> Sourcing limitation: official user documentation for several relevant systems (including United States catch-accounting platforms and Norwegian seafood-industry catch-management products) was unreachable from the research environment (repeated transport errors and timeouts). Quota-balancing workflow detail therefore rests primarily on the New Zealand administration implementation and is stated at cross-product-commonality strength rather than as a universal rule; the industry-operator seat is evidenced through participant-facing administration functions and monitoring products rather than through industry ERP documentation. Precise operational specifics (reporting deadlines, formats, numeric limits) are intentionally not asserted in this document.

Detailed product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
