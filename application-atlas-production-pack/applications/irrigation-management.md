# Irrigation Management

## Overview

An **Irrigation Management** application is the grower-side water-decision system for irrigated crop production. It holds a farm's irrigated areas — fields, zones, blocks, bays, pivots — as decision units, maintains a current and forward-looking picture of each area's water status and crop water demand, and turns that picture into dated, area-bound irrigation decisions: recommendations and schedules stating **when, where, and how much** water to apply. What is actually applied is recorded back against the plan, and the status picture updates as water goes on, rain falls, and the crop grows.

The defining core is the decision loop itself:

```text
Irrigated areas (decision units)
    └── Water-status & demand picture  (sensed, modeled, or expert-entered)
        └── Irrigation decision        (dated, area-bound: when / where / how much)
            └── Application            (manual, or executed through connected equipment)
                └── Recorded against the plan → status picture updates → next decision
```

Everything else commonly associated with the category — soil-moisture probes, remote pivot control, automated valves, fertigation, satellite imagery, variable-rate prescriptions — is standard capability or optional depth. A product can be genuine irrigation management with no sensors at all (a modeled schedule built from weather data and expert-entered field records), and a product full of sensors and remote-controlled valves is not irrigation management unless it produces the water decision.

## Users & Context

Primary users are people accountable for getting water onto crops on time:

- **growers and farm managers** — decide and approve irrigation for their fields; watch status and alerts; adjust plans as weather and crop stage change
- **irrigation and water managers** on larger operations — run the day-to-day loop across many areas and much equipment, coordinate pump and system capacity
- **agronomists and advisors** — enter or validate the field data behind modeled recommendations, interpret soil-moisture and water-use trends, advise on timing and amounts

A distinctive market trait is **expert- and dealer-mediated operation**: in common implementations the vendor's certified dealers or agronomy specialists install sensors, calibrate the model, monitor data through the season, and review results with the grower. Self-serve configurations exist alongside this service model.

Secondary touchpoints: equipment dealers and service technicians (installation, calibration, fault response), and — in surface-irrigation regions connected to delivery districts — district operators on the supply side.

The work context is seasonal and weather-driven: the loop runs daily through the irrigation season, decisions are time-critical (a missed or late irrigation is a crop event, not a backlog item), and much of the interaction happens from mobile devices in or near the field.

## Core Model

### The defining core

**The irrigated area as the decision unit.** Every water decision attaches to an identified production area. The area carries the context the decision depends on — the crop, its stage, the soil, the application equipment that serves it. Areas are held persistently across seasons, so status history and application history accumulate per area. Without this layer, water-related software is just sensing or equipment control with nothing to decide *for*.

**The water-status and demand picture.** For each area the system maintains where water stands against what the crop needs. This picture is built from whatever data sources the product offers — the substrate is a variant, the picture is not:

- measured soil moisture (probe- or sensor-based), often shown against defined thresholds or named bands indicating how close the soil is to its refill point
- a water balance: water used by the crop (evapotranspiration), water added by irrigation and rain
- modeled estimates from weather, soil, and crop data entered by the user or an advisor
- increasingly, remote-sensing inputs such as satellite-derived water-use estimates over broad areas

The picture is forward-looking as well as current — mature products commonly show water fill levels for past and coming dates, and a rolling multi-day forecast of irrigation need, updated as weather updates. Without this layer, there is no basis to decide anything; the product collapses into equipment control or weather display.

**The irrigation decision.** The system produces a dated, area-bound statement of when, where, and how much water to apply. Three realizations appear in the market and often coexist in one product:

- a **recommendation** — advisory output the grower reads and acts on (commonly presented as map or list views per field)
- a **schedule** — an explicit plan the user edits: dates/times, durations or depths or run hours per area
- a **program** — an executable configuration driving equipment: sequences of gate, valve, or pump actions, either time-based or triggered by sensor events

The decision is *recurring and revisable*: it is regenerated or adjusted as the status picture changes. Without it — if the software only shows conditions and never lands on "what to do" — the product is a monitoring platform, not irrigation management.

### Standard capabilities of mature products

These are widespread in the market and expected by buyers, but a product can be recognized as this Type without some of them:

- **Execution through connected equipment** — remote monitoring and control of pivots, pumps, valves, and gates from web and mobile; control depth ranges from none (advisory-only) through manual remote operation to fully automated programs
- **Plan-vs-executed verification** — recording what was actually applied and comparing it against the plan; several products make "confirm it ran as planned" an explicit step, because a schedule that never executed is worse than none
- **Water accounting** — application history and water-usage totals per area and per period, with reports covering the season's water use; increasingly used for traceability and compliance
- **Equipment and system status with alerts** — faults, missed or blocked runs, hydraulic anomalies, device health; alerts on both irrigation conditions and equipment problems
- **Weather integration** — on-farm stations and/or forecast services feeding the status picture
- **Map and list presentation** of areas and their water state
- **Mobile + web access**; some products add offline tolerance for poorly connected fields

### One decision, many substrates

The core model is technology-agnostic; the market realizes it on very different substrates:

```text
Concept:        Water-status picture
Realizations:   soil-moisture sensors · ET/water-balance models · satellite estimates ·
                expert-entered observations · any mix of these

Concept:        Irrigation decision
Realizations:   advisory recommendation · editable schedule ·
                executable program (time-based or sensor-event-triggered)

Concept:        Application equipment
Realizations:   center pivots and linears · drip and micro systems ·
                surface/flood bays with gates · pumps and valves of any kind
```

A reader who has only seen one realization — say, sensor-driven scheduling for drip orchards — should still be able to recognize a modeled, recommendation-only scheduler or a bay-gate automation system as the same Type.

## How It Works

### Season setup

Before the loop starts, the operation is structured: irrigated areas are registered with their crop, soil, and equipment; water sources, pumps, and application devices are configured; sensors (if any) are placed and commissioned; and the data inputs behind the status picture are chosen. In expert-mediated implementations, this is typically done with or by the vendor's agronomy specialists.

### The recurring decision loop

```text
Status picture updates (sensors, weather, models, entered records)
    → per-area water status evaluated (at / above / below target; stress risk)
    → decision produced: recommendation and/or schedule/program per area
    → grower reviews, adjusts, accepts
    → water applied (manually, or by remote control, or by automated program)
    → what was applied is recorded; alarms surface anything that went wrong
    → status picture updates … loop continues through the season
```

Two execution patterns dominate:

- **Advisory-first**: the system recommends; people apply. Verification is comparing what was applied against the recommendation, and the recorded applications feed the water balance.
- **Connected-first**: the system also drives equipment. Remote commands start/stop pivots, pumps, and valves; automated programs run to a schedule or fire on sensor events (for example, a gate opening when a channel water-level sensor crosses its threshold). Here verification gains a mechanical edge — confirm each program run actually executed on the equipment.

### Automation and its gatekeeping

Where programs are executed automatically, mature products treat **will it actually run?** as a first-class question: devices must be reachable and free of blocking alarms before a program is trusted, and non-sensical commands can be prevented outright. A synchronized program does not guarantee a wet field — this gap between plan and execution is the system's most important managed risk.

### Season closure

The season ends with accumulated evidence: application history, water-use totals per area and per period, and water reports. These close the accounting loop, support compliance or traceability where required, and inform next season's setup.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Map / field overview

The primary entry surface: the farm's irrigated areas on a map or in a list, each with its current water status at a glance.

- typical information: per-area status indicator (fill level or named band), crop, last/next irrigation, active alerts
- primary actions: drill into an area, review recommendations, acknowledge alerts

### Area detail — status & recommendation

The decision surface for one area.

- typical information: water fill levels over past and future dates, soil-moisture against thresholds, water use (ET) and rain, crop stage, recommendation ("when and how much")
- primary actions: accept or adjust the recommendation, edit the schedule, record an application, view history

### Schedule / program editor

Where decisions become executable plans.

- typical information: dates, times, durations or depths or run hours per area; program steps and their order; event triggers for sensor-driven automation
- primary actions: create/edit programs, synchronize them to equipment, enable or pause automation

### Equipment monitoring & control

The connected-equipment surface (where the product has one).

- typical information: pivot/pump/valve/gate state, position or run state, flow and pressure, tank or channel levels, device health
- primary actions: start/stop, set application rate or run time, respond to faults

### Water accounting & reports

- typical information: applied water per area/period, planned vs actual, water-use totals, season reports
- primary actions: generate/export reports, drill into history

### Alerts

Time-critical notifications pushed to mobile and web: irrigation-needed conditions, equipment faults, blocked or failed runs, threshold crossings.

## Important Rules / Behaviors

- **The decision loop runs on the status picture, not on the calendar alone.** Recommendations and schedules are regenerated or adjusted as weather, sensors, and crop stage change; a fixed season-long plan is a special case, not the norm.
- **Plan and execution are distinct records.** What was recommended, what was scheduled, and what actually ran are tracked separately; mature products surface the gaps, because equipment faults, dead batteries, channel shortfalls, and connectivity loss routinely break execution.
- **Automation is gated by equipment readiness.** A program synchronized to devices is not a program that will run: blocking alarms must be cleared, devices must respond, and some products explicitly prevent commands that would be hydraulically illogical.
- **Status is evaluated against defined thresholds.** Whether expressed as named bands or numeric targets, the product's judgment of "too dry / adequate / full" rests on thresholds set per area (soil, crop, method) — often calibrated by an expert during setup.
- **Water is accounted, not just applied.** Applications feed a per-area water ledger used for the status picture, for reporting, and commonly for compliance and traceability.
- **Advisory mode is a full mode, not a crippled one.** Recommendation-only configurations are deliberately marketed (for modeled scheduling without hardware); the absence of control does not demote the product out of the Type.
- **Fertigation may be inseparable or absent.** In drip-centric implementations, irrigation and nutrient dosing are planned, executed, and reported as one; in pivot and surface implementations, nutrients are typically out of scope.

## Variants

- **Pivot-ecosystem management** — built around center-pivot country; recommendations plus remote pivot/pump control and machine diagnostics, commonly dealer-delivered and often compatible across pivot brands
- **Sensor-driven agronomy platforms** — irrigation planning as one module beside disease, nutrition, and crop monitoring; own or third-party sensors, satellite inputs, strong reporting
- **Drip/fertigation closed loop** — specialty crops; irrigation and nutrient dosing planned and executed together with valve-level control and per-block traceability
- **Surface/flood irrigation automation** — bay-and-gate gravity systems; time-based and sensor-triggered gate programs, water orders against district supply, per-bay water usage
- **Advisory/service-delivered scheduling** — recommendation and expert monitoring without hardware (modeled scheduling); the vendor's agronomists are part of the product
- **District-connected variants** — where farms draw from managed canal networks, the farm loop touches water-order approval and network capacity
- **Application-technology flavors** — the decision object adapts its semantics: run hours and application rates for pivots, valve shifts for drip, gate open/close times for bays

A variant stays a variant unless it changes the center: a greenhouse climate computer that also runs irrigation belongs to greenhouse management (facility loop); a pivot that merely follows an on-board timer belongs to equipment, not management.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Agricultural IoT Platform | feeds & overlaps | centers the device fleet and the telemetry/monitoring loop (frost, pest, disease, climate); irrigation management centers the water decision. Structural test: remove the device fleet — irrigation management still stands on models and entered data; remove the irrigation decision — the IoT platform still monitors everything else |
| Crop Management | superset gradient | centers the whole crop-season record across all operations; irrigation management centers one operation domain and commonly ships as a module inside crop-management products, while also existing standalone |
| Greenhouse Management | adjacent | centers the protected-growing facility's climate-and-water control loop across zones; irrigation management centers the water decision and is enclosure-agnostic. Irrigation scheduling is a capability there, not the center |
| Field Management | adjacent | centers the land asset (boundaries, soil, layout); irrigation management attaches water decisions to those areas |
| Precision Agriculture Platform | adjacent | centers variable-rate prescription generation/execution across inputs; variable-rate *irrigation* prescriptions are one variant capability inside irrigation management |
| Agricultural GIS | capability host | holds irrigation zones and prescriptions as map layers; the recurring decision loop is not there |
| Water Utility Management (utility side) | different side | manages the water network, customers, and billing for a utility or district; irrigation management is the farm-side crop-water decision. District-connected surface-irrigation products span the seam |
| Farm Equipment Telematics | adjacent | centers machine-fleet health across equipment; pivot/pump diagnostics appear inside irrigation management as a common capability, not the center |

The most practically confusing boundary is with the Agricultural IoT Platform, because soil-moisture networks exist largely to feed irrigation decisions — and the two product families genuinely interlock. The center of gravity separates them: the sensing backbone versus the water decision.

## Representative Products

- **Valley Irrigation Scheduling / AgSense 365** (Valmont) — pivot-ecosystem pole: modeled or sensor-measured recommendation service plus remote pivot and pump management
- **CropX Irrigation Planning** (CropX) — independent sensor-driven platform pole: soil-moisture and ET-based irrigation insights beside the wider agronomy suite
- **Netafim GrowSphere™** (Netafim) — drip/fertigation closed-loop pole: plan–execute–validate irrigation and fertigation for specialty crops
- **FarmConnect** (Rubicon Water) — surface/gravity irrigation automation pole: gate, valve, and pump programs with water usage accounting, alongside district network delivery

The defining core was checked against older and hardware-free configurations (modeled scheduling with no in-field sensors; the analog water-balance-ledger routine) to avoid over-fitting to the current sensor-and-control market.

## Sources

Research date: **2026-09-08**

- Valley Irrigation (Valmont) — "Irrigation Scheduling" product page — https://www.valleyirrigation.com/scheduling
- Valley Irrigation (Valmont) — "AgSense 365" product page — https://www.valleyirrigation.com/precision-ag/agsense-365
- CropX — site overview & FAQ — https://cropx.com/
- CropX — "Irrigation Planning" product page — https://cropx.com/cropx-system/irrigation-planning/
- Netafim — GrowSphere™ / Digital Farming — https://www.netafim.com/en/digital-farming/
- Rubicon Water — site overview — https://www.rubiconwater.com/
- Rubicon Water — FarmConnect Knowledge Base (Irrigations module; Types of Irrigation Program) — https://farmconnect.docs.rubiconwater.com/

> Sourcing limitation: official pages for two additional candidate products (Lindsay FieldNET; Manna Irrigation) and a university-extension scheduling reference were unreachable from the research environment on 2026-09-08 and were abandoned after repeated attempts. Precise operational specifics observed on single products (forecast windows, named status bands, service-tier features) are kept out of this document and recorded only as product-specific behavior; market-wide claims are calibrated to the reachable sample.
