# Electronic Logging Device / HOS Platform

## Overview

An **Electronic Logging Device / HOS Platform** is the compliance system that records a commercial driver's duty status over time — with driving time captured from the vehicle itself rather than self-reported — continuously computes how much driving, working, and rest time the driver has left under the applicable hours-of-service (HOS) regulations, and maintains that log as a certified, edit-governed record that can be shown to and transferred to roadside inspectors.

It exists because commercial vehicle operators are subject to legal limits on how long they may drive and work before resting, and carriers must be able to prove compliance. The Type digitized the paper logbook and, in regulated markets, formalized it: the driving record is produced from vehicle data, the remaining hours are computed by the system, and the record itself carries regulatory force.

The defining core is small:

```text
Identified driver with an assigned rule set
└── Duty-status log of record (persistent, time-stamped, per day)
    └── Duty-status entries (driving / on-duty not driving / off-duty / sleeper berth)
        └── Driving time captured from the vehicle
└── HOS clocks (break / drive / shift / cycle time remaining)
    └── computed against the rule set → violation states
└── Compliance governance (certification, governed edits, roadside inspection)
```

Everything commonly bundled around it — vehicle inspection reports, co-driver handling, exemption workflows, fuel-tax reporting, safety cameras, maintenance, dispatch — belongs to the same fleet-operations market but is not what makes this software an ELD/HOS platform.

## Users & Context

**Primary user: the commercial driver.** Drivers operate the log itself — they sign in before work, change duty status as their day changes, watch their remaining hours, annotate and certify their logs, and present them during roadside inspections. The driver is the subject of the record and its first-line author, even though driving time is captured automatically.

**Manager-side users:**

- *Fleet / compliance / safety managers* monitor every driver's clocks and violation status from a dashboard, review logs, and handle the carrier side of log edits and violations. In most products they also control which rule set each driver runs under and which special statuses each driver may use.
- *Dispatchers / supervisors* read driver clock status when planning work — a driver with no remaining drive time cannot be assigned driving work. Dispatch typically lives in a neighboring system; the clocks it consumes live here.

**External recipient: the roadside inspector.** During a stop, the driver must be able to display the log and transfer its data to the inspector. This external audience shapes what would otherwise be an internal tracking tool into a compliance record system.

Typical context: carriers and fleets operating regulated commercial vehicles (long-haul trucking being the classic case, with regional and short-haul operations as large segments), in markets with mandatory electronic logging — most prominently the United States (FMCSA regulations, cited by vendors as rules 395.15 for the device and 395.8 for the record of duty status) and Canada.

## Core Model

### The defining structure

**The driver, carrying an assigned rule set.** Every log belongs to an individually identified driver, and every driver profile carries the hours-of-service rule set that governs their work: which cycle applies, which region's rules, which exceptions they may claim, which special duty statuses they are allowed to use. Fleets commonly assign a primary and, where useful, a secondary rule set — for example a driver who works under US federal rules and also crosses into Canada.

**The duty-status log of record.** The central object is the driver's log: a persistent, day-by-day, time-stamped record of what duty status the driver was in. The working vocabulary is a small set of statuses — driving; on-duty (not driving); off-duty; and sleeper berth — plus remarks and context (location, vehicle, shipping information) that the regulations attach to each entry. The log is the digital descendant of the paper record of duty status, and it is what gets certified, edited, inspected, and retained.

**Driving time captured from the vehicle.** What separates this Type from any time tracker is where driving time comes from. In the mandated ELD mode, an in-vehicle device connects to the engine's diagnostic port and records driving time automatically from engine data whenever the vehicle moves. This capture is authoritative: the driver cannot rewrite automatically recorded driving segments. Some platforms additionally offer a manual-entry electronic-logbook mode for drivers who are exempt from the device mandate — the log and the clocks still run, but the entries are driver-authored.

**HOS clocks.** From the log and the assigned rule set, the system continuously computes the driver's remaining time on each regulatory limit. Products commonly show four clocks — time remaining until the next required break, remaining driving time, remaining on-duty (shift) time, and remaining cycle time over the multi-day limit. The clocks are the system's forward-looking intelligence: they turn the historical log into a prediction of what the driver may still legally do, and they drive alerts before violations occur.

**Compliance governance.** The log is a legal record, and the system enforces that character: drivers certify that their logs are true; corrections go through a governed edit workflow that records a remark and preserves what was originally recorded; logs and their data can be displayed and transferred to inspectors; and the system must retain records for the regulated retention period. Governance is what makes the object a record rather than a memo.

### How the pieces relate

```text
Driver profile (identity + assigned rule set)
   ↓ produces
Duty-status log of record
   ├── fed by: vehicle-derived driving capture (ELD device)
   ├── fed by: driver status changes, remarks, claims
   ↓ computes
HOS clocks (break / drive / shift / cycle) → violation & warning states
   ↓ closed by
Certification → governed edits → roadside inspection → retention
```

The vehicle and its regulation mode sit beside the driver: a vehicle configured as regulated produces ELD-treated driving for whichever identified driver is logged into it; a vehicle configured as unregulated (non-commercial use) does not. Movement in a regulated vehicle with no driver logged in becomes *unidentified driving*, which a driver must later claim or reject.

### Standard capabilities

Mature products in this Type commonly add, without these defining it:

- driver vehicle inspection reports (DVIR) alongside the HOS log
- co-driver / team-driving support on one vehicle
- unidentified-driving claim and reject workflows
- special duty statuses — personal conveyance (off-duty personal movement) and yard moves (on-duty, non-driving movement in a private area), typically enabled per driver by a manager
- exception and claim workflows (adverse driving conditions, short-haul, industry-specific exceptions such as agriculture or utility operations)
- nearing-limit warnings and violation notifications, plus manager-side violation queues
- ELD diagnostics and malfunction handling
- reporting on driver availability, violations, and log compliance

## How It Works

### Setup

```text
Register the driver (identity, license context)
→ assign the rule set (region, cycle, exceptions, permitted special statuses)
→ install the in-vehicle device / pair the driver app to the vehicle
→ set the vehicle's regulation mode (regulated / unregulated)
```

### The daily compliance loop

```text
Driver signs into the app in the vehicle
→ selects duty status as the day changes (off-duty → on-duty → driving …)
→ device records driving time automatically from engine data
→ clocks tick down against the assigned rule set
→ system warns as limits approach; flags violations when they occur
→ driver annotates, adds remarks, and at day's end certifies the log
```

The loop is continuous while the driver works: the application is open in the cab, the status vocabulary is small, and the clocks — not the driver's mental arithmetic — carry the regulatory computation. Movement detected in the vehicle while no driver is logged in accumulates as unidentified driving for later claim.

### Corrections

```text
Driver (or manager) proposes a change to a log segment
→ attaches a remark explaining why
→ carrier side reviews; if accepted, the record is re-certified
→ the originally recorded data is preserved, not overwritten
```

Automatically recorded driving segments are the hard case: their start and end times cannot be edited — a constraint documented in-market as an explicit consequence of the ELD mandate. Edits apply to manually entered time and to context; some status conversions are reserved to administrators rather than the app. Editing a log that was already certified triggers re-certification.

### Inspection

```text
Roadside stop
→ driver opens the inspection surface
→ displays the current and previous logs
→ transfers the record data to the inspector by the accepted method
→ device/app shows its operating condition (no active malfunction)
```

### Manager-side monitoring

Managers see the fleet's drivers as a live list of clock states — who is driving, on-duty, off-duty, in violation, or nearing a limit — and work from queues: logs needing review, edits awaiting approval, violations to address. This is the operational vantage point from which dispatch and planning systems consume driver availability.

## Interfaces

The Type has a characteristic two-sided shape: a driver app in the cab and a management console in the office, joined by the shared record.

### Driver app (mobile, paired to the vehicle)

- **Home / clocks view** — the driver's current duty status and the remaining-time clocks, the most-looked-at surface of the whole product.
- **Logs view** — the daily log as a graphical grid of status segments, navigable by day, with remarks, exceptions applied, and edit entry points; certification actions live here.
- **Status switcher** — the small, regulated vocabulary of statuses plus the special ones the driver has been enabled for.
- **Inspection mode** — the inspector-facing display and data transfer.
- **DVIR** — pre-trip and post-trip vehicle inspection reports, usually on adjacent screens.
- **Vehicle selection / pairing** — choosing the vehicle being operated; this is what binds the driver's log to the vehicle's driving events.

### Fleet management dashboard (web)

- **Driver compliance list** — every driver with current status, remaining clocks, and violation indicators.
- **Logs and edits** — log review, the carrier side of the edit workflow, re-certification, and violation management.
- **Configuration** — rule-set/cycle catalogs per region, driver rule assignments, special-status permissions, vehicle regulation modes.

### Admin/device layer

Device installation, diagnostics, and malfunction state — visible to both admins and drivers because a malfunctioning ELD is itself a compliance event.

## Important Rules / Behaviors

- **Driving time is the vehicle's word.** Automatically recorded driving segments are the anchor of the log; the system governs edits so that the original recording survives every correction.
- **The log exists regardless of hours.** Drivers with no remaining hours — or who did not drive at all — still produce a daily log that must be certified. Whether logging happens at all is determined by the vehicle's regulation mode, not by remaining time.
- **Certification closes the day.** An uncertified log is an open compliance item; corrections to certified logs require re-certification.
- **Edits are two-sided.** Driver proposals and carrier actions are distinct roles; remarks are mandatory context, and some status conversions are administrator-only.
- **Special statuses are privileged.** Personal conveyance and yard moves change what the time counts as, so managers enable them per driver, and the system records their use distinctly.
- **Clocks follow the binding rule set.** When several limits apply, the effective remaining time is the most restrictive one; crossing regions (for example a US–Canada border) changes which rule set applies, which some products handle automatically when both are assigned.
- **Exemptions change the obligation.** Short-haul radius drivers, limited-frequency drivers, and other excepted categories may not need full records; platforms model this as driver-level compliance modes and exception claims rather than pretending every driver logs identically.
- **Unassigned driving must be resolved.** Vehicle movement without a logged-in driver is captured and held for claim or rejection — the log's integrity does not depend on the driver remembering to sign in.

## Variants

- **Certified ELD vs electronic logbook.** The regulated device mode vs a manual-entry logbook mode for exempt drivers, offered on the same platform with the same clocks and governance.
- **Regional regimes.** US federal rules with state variants and Canadian federal/provincial rules (including distinct regional cycle families) are the regimes most documented in-market; each arrives as its own rule-set catalog, clocks, and violation logic.
- **Industry tuning.** Long-haul trucking is the center; short-haul/local delivery, energy and oilfield (waiting-time statuses), agriculture (radius-based exceptions), and utility operations appear as exception machinery and configuration more than as different cores.
- **Mixed fleets.** Fleets running both regulated and non-regulated vehicles use vehicle-level regulation modes so unregulated assets do not generate compliance obligations.
- **Suite position.** The same vendors sell this core inside broader fleet-operations platforms (safety cameras, telematics, maintenance, fuel and tax reporting, dispatch). The HOS core is stable; the bundling varies widely.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Fleet Management System | suite sibling | vehicle-as-asset is the record of record (maintenance, fuel, utilization, location); the HOS log is one compliance module inside FMS suites, but strip duty-status logging from an FMS and it still manages vehicles |
| Driver Management | person-entitlement sibling | manages the driver's qualification to drive (licenses, checks, remediation) rather than the duty-time record the driver produces; HOS data may feed it, but is not its record |
| Vehicle Telematics Platform | data-layer neighbor | provides the telemetry (location, engine, behavior) the ELD consumes; without the duty-status record, clocks, and compliance governance, vehicle data alone is telematics |
| Trucking Management System / Dispatch Management | workflow neighbor | loads, carriers, settlements, assignment; dispatchers read driver clocks from here, but freight work does not live in the ELD |
| Time & Attendance System | structural analogue, different world | records worked time for payroll against shifts and clocks employees in; the HOS log records duty statuses against legal limits, with vehicle-derived driving capture and an inspector as audience |
| Tachograph ecosystem (EU) | regional sibling (open question) | the EU's regulated in-vehicle recording family shares the same shape at the software layer (card data, clocks, governed records) but is its own hardware/legislation regime; treated here as a regional sibling pending its own pass |

The closest daily-use boundary is with the FMS suite: the same vendors sell both, and the HOS core is the piece whose removal breaks regulatory compliance rather than operational convenience.

## Representative Products

- **Motive** (formerly KeepTruckin) — ELD-native, driver-app-first compliance platform
- **Samsara** — telematics suite with ELD/HOS as its compliance pillar
- **Geotab** — open telematics platform delivering HOS through its driver app and manager console

The defining core was checked against these three products' documentation and against the pre-mandate lineage (paper record of duty status, legacy automatic on-board recording devices, and app-only logbook modes for exempt drivers) to avoid over-fitting the definition to the current US-mandate implementation.

## Sources

Research date: **2026-09-08**

- Motive Help Center — "Hours of Service" (helpcenter.gomotive.com/hc/en-us/articles/30810628869405); "Difference between the Motive Driver App and the Vehicle Gateway" (…/6173250355613); "Drivers Exempt from the ELD Rule – FMCSA Guidelines" (…/14720399809949)
- Samsara Help Center (kb.samsara.com) — "HOS Dials in the Driver App" (…/360043178192); "Edit an HOS Log" (…/360043215192); HOS Compliance driver-workflow section (article inventory: certification, roadside inspection, log transfer, carrier edits, personal conveyance, yard move, split sleeper, team driving, unidentified driving, violations, regulation modes, Canada cycles)
- Geotab — HOS surfaces (HOS status page, logs, roadside checks, co-drivers) observed in the fleet-management-system research pass (docs.geotab.com was not directly reachable)

> Sourcing limitations: the FMCSA regulator site was unreachable (HTTP 403), so regulatory specifics in this document are calibrated to what vendor documentation states and cites; Geotab evidence is inherited from the sibling research pass rather than fetched directly; other ELD vendors' help centers were unreachable. Precise numeric limits, retention windows, and transfer mechanisms are therefore stated only at the strength the fetched evidence supports, with product-specific detail kept out of the definition.
