# Advanced Distribution Management System / ADMS

## Overview

An **Advanced Distribution Management System (ADMS)** is the real-time operations platform of an electric distribution utility's control room. It maintains a connected electrical model of the distribution network, renders live telemetry from field devices on that model, lets operators control network devices remotely, and runs the operational loop that turns alarms, trouble calls, and switching plans into recorded, safety-gated actions on the network.

Around that core, mature products add an outage-management layer (customer calls → outage events → crew dispatch → restoration → reliability records), a switching-management layer (switching sheets/orders with electronic safety documents), and a family of network applications computed on a power-flow engine — state estimation, fault location, fault location/isolation/service restoration (FLISR), Volt/VAR optimization, and load forecasting.

The defining core is deliberately small. A distribution control system with a network model, live monitoring, device control, and an operational event loop is an ADMS even if it has no outage management, no FLISR, and no DER support. Conversely, a telemetry-and-control system without a connected network model is SCADA, not an ADMS; an outage/call/crew system without real-time network operations is an OMS, not an ADMS. "Advanced" is a market-era label — the term spread as distribution SCADA, network applications (historically called DMS), and outage management converged into one platform — not a checklist of specific algorithms.

## Users & Context

The primary user is the **distribution system operator** (also called dispatcher or controller) working in a utility control room, in shifts, 24/7. Operators watch the network on one-line diagrams, respond to alarms, execute switching, and manage outage response. In some products the network is divided into operating areas, and an operator takes explicit authority over the area they are working.

Secondary users, each with a distinct surface:

- **trouble call takers / outage coordinators** — answer customer calls, create and group outage events, maintain estimated restoration times
- **crew dispatchers** — assign field crews to events and track their status (dispatched, en route, on site, released)
- **switching planners / field planners** — prepare planned switching requests and switching sheets for construction and maintenance work, often from a separate planning environment
- **reliability / operations engineers** — analyze events, maintain the network model, tune network applications, produce reliability reports
- **SCADA administrators / commissioning technicians** — configure field-device communications, test and commission new devices
- **trainers** — run the operator training simulator with fault, overload, and storm scenarios

The context switches character between "blue-sky" days (planned switching, monitoring, optimization) and "grey-sky" storm operations (mass outages, storm mode, emergency switching, damage assessment). The same platform serves both; storm mode typically changes priorities, staffing surfaces, and restoration-time calculations.

## Core Model

### The Defining Core

```text
Distribution Network Model (connected electrical model: feeders, devices, phases, sources)
└── Real-time network state (telemetry and status rendered on the model)
    └── Operator control actions (switching and device operations, recorded)
        └── Operational event loop (alarms/events → assessment → action → persistent record)
```

Four properties. If any one is removed, the product is no longer recognizable as an ADMS:

- **Distribution network model** — the system's organizing structure is a connected electrical model of the distribution system: feeders, breakers/reclosers/switches, transformers, capacitors, conductors with impedances, phases, nominal voltages, and supply points. The model knows what is connected to what, so the system can reason about de-energized sections, islands, and restoration paths. Without it, the product is a point-based SCADA system.
- **Real-time monitoring on the model** — live measurements (voltages, currents, loads) and device statuses are acquired continuously and displayed on the network model. Without it, the product is offline planning or GIS software.
- **Supervisory control** — operators operate devices (open/close switches, reclosers, regulators) from the platform, and each operation is recorded. Without it, the product is a monitoring dashboard, not an operations platform.
- **Operational event loop** — the system raises alarms and events, supports assessment against the model, and records the operational response (switching actions, restorations, event histories). Without it, the product is an engineering analysis tool.

### Standard Capabilities

Mature products commonly add the following layers. They are what make a modern ADMS practical, but they are modules, not the definition — vendors ship them as separately licensed components, and utilities deploy them incrementally.

**Outage management layer.** Customer trouble calls (including partial-information "fuzzy" calls) are entered and matched against the network model; the system predicts the outage device, groups related calls into outage events, and tracks each event with an estimated restoration time, affected-customer counts, and critical-customer flags (hospitals, emergency services, life-support). Crews are assigned and tracked through dispatch, en-route, on-site, and release. Damage from major storms is recorded through damage assessments. Completed events carry cause codes and feed reliability metrics such as customer-minutes interrupted and SAIDI/SAIFI-style indices.

**Switching management layer.** Planned and emergency switching is organized as switching sheets (also called switch orders): ordered lists of switching steps with a lifecycle (requested → approved/scheduled → issued → in progress → complete, with product-specific labels). Safety documents — the electronic form of paper tags, permits, and grounds — record the issuance and release of safety tags on devices and block conflicting operations. Switching sheets can be simulated in study mode, checked for customer impact and conflicts with other work, and then executed against the real network.

**Network applications.** A power-flow engine is the computational core: it calculates voltages and flows on the modeled network, scaled with live SCADA measurements and load profiles. The other applications depend on it:

- distribution state estimation — reconciles measurements into a consistent network state, flags bad data, and estimates unmeasured quantities
- feeder load management — system-wide view of current and near-future loading
- fault location analysis — predicts probable fault points from relay fault currents using short-circuit analysis
- FLISR — after a breaker lockout, identifies the faulted section from fault indicators, then formulates (and in some deployments automatically executes) a plan to isolate the faulted section and restore healthy sections via tie points, checking feeder capacity, voltage violations, and safety blocks
- Volt/VAR optimization — continuously or on-demand adjusts regulators and capacitor controls to meet objectives (loss reduction, voltage conformance) within equipment operation limits
- load forecasting — near-term load and DER-output forecasts used by the applications above

**Operational infrastructure.** Alarm management (alarm lists, shelving, nuisance-alarm handling, abnormal-device lists), a time-series historian for measurements and events, study mode, an operator training simulator, and reporting/dashboards.

**Integrations.** The network model is typically derived from the utility GIS or an enterprise network-model management tool; AMI meter pings confirm or refine outage extents; DER data feeds the model and applications; mobile field apps connect crews to events.

### One Structure, Many Implementations

```text
Concept:      Distribution network model
Realizations: GIS-derived model import, industry-standard (CIM-based) exchange,
              vendor network-model management tools

Concept:      Real-time measurements and control
Realizations: SCADA module embedded in the ADMS, integration with an existing
              third-party SCADA, field communications via front-end processors
              and intelligent electronic devices, AMI meter pings

Concept:      Switching safety workflow
Realizations: electronic switching sheets with safety documents/tags,
              switch orders with guarantees, digitized paper permit regimes

Concept:      Outage event record
Realizations: trouble-management events with restoration logs, work orders in
              companion systems, storm-management consoles
```

A reader who has only seen one implementation (for example, a cloud-deployed platform with built-in DER orchestration) should still be able to recognize an older deployment — an on-premises control room where the ADMS integrates a separate SCADA and gets its model from GIS — as the same Type.

## How It Works

Three loops dominate daily use.

### Normal operations: planned switching

```text
Field or planning group submits a switching request
→ operator/planner builds a switching sheet (ordered steps: open/close/ground/tag)
→ simulate the sheet in study mode (power flow checks, customer-impact preview, overlap checks)
→ issue safety documents (tags/grounds placed on devices)
→ approve and schedule; execute step by step against the real network
→ release safety documents, restore normal configuration, complete the sheet
```

Every step is logged. While switching proceeds, devices may temporarily sit on a different feeder than their normal ("nominal") configuration, and the system tracks both nominal and current associations.

### Outage response: the trouble loop

```text
Fault occurs → protective device locks out → SCADA alarm
→ customers call; call takers enter calls → system predicts the outage device
   and groups calls into an outage event on the network model
→ operator confirms the event; estimated restoration time is set and updated
→ FLISR / fault-location analysis / suggested switching propose isolation
   and restoration plans (respecting tags, grounds, and crews)
→ operator executes switching (or automation executes under supervision)
→ crews dispatched, patrol and damage assessment, repairs
→ restoration in stages; each stage updates customers restored and reliability records
→ event completed with cause codes; feeds reliability indices and storm reports
```

During storms, the platform enters storm mode: call volume surges are absorbed by grouping rules, restoration-time algorithms change, damage assessments and callback queues scale up, and view-only consoles extend situational awareness to management and support staff.

### Network optimization loop

```text
State estimation / power flow maintain a trusted real-time network state
→ Volt/VAR optimization and FLISR continuously or on-event evaluate the network
→ recommendations appear as operator-facing proposals (or execute automatically,
   depending on the utility's automation posture)
→ operator accepts, modifies, or demotes the plan to manual control
```

### Study mode

Every operational surface commonly has a real-time mode and a study mode. Study mode applies the same tools — switching, topology changes, power flow, optimization — to a sandbox copy of the network without touching live data. It is used for switching-plan validation, what-if analysis, and training.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### One-line diagram / network viewer

The operator's primary window: a schematic (sometimes geographic) rendering of feeders and devices, colored by energization state and alarm condition, with live measurements on devices.

- typical information: feeder topology, device states, live MW/kV values, outage and call symbols, tags and grounds
- primary actions: select a device, open its control dialog, run traces (upstream/downstream), toggle layers, switch between real-time and study mode

### Alarm and event lists

The work queue of the control room.

- typical information: unacknowledged alarms, active outage events with call counts, customers out, estimated restoration time, assigned crews
- primary actions: acknowledge, open event details, filter by area or severity

### Device control dialog

The point where monitoring becomes action.

- typical information: device identity, state, measurements, associated documents, safety tags
- primary actions: open/close, tag, place ground, inhibit automatic operations, view control history; control failures are surfaced explicitly

### Event details

The tabbed record of one outage event.

- typical information: calls and callers, customers out (with critical-customer breakdown), restoration log by stage, crews and contact times, damage assessments, cause codes, attached switching sheets
- primary actions: update estimated restoration time, group/ungroup calls, assign crews, complete the event with cause and remedy

### Switching sheet editor and safety documents

- typical information: ordered switching steps, sheet state, affected customers, conflicts/overlaps, linked safety documents
- primary actions: create from template or request, simulate in study mode, issue, implement step-by-step, release safety documents, complete

### Call entry and crew boards

Call takers search customers and log calls (including fuzzy, partial-information calls); dispatchers move crews through assignment states and track contact times.

### Training simulator and reports

A sandbox copy of the control room with scenario injection (faults, overloads, storms); reporting surfaces for reliability indices, storm summaries, and management statistics.

## Important Rules / Behaviors

- **Real-time and study mode are strictly separated.** Actions taken in study mode never affect live network data. This separation is what makes simulation, switching-plan validation, and training safe.
- **Safety gating is structural.** Safety documents (tags, grounds, permits) recorded on devices block conflicting operations — including automated ones. Restoration logic such as FLISR explicitly checks for tags, grounds, and crews before proposing or executing switching.
- **Operating authority is explicit.** Some products organize the network into control zones or operating areas and require an operator to hold authority over an area before operating devices in it; some products let planners delegate control of an area for a work period. Exact mechanisms vary by product.
- **Switching follows a lifecycle.** Switching sheets move through defined states (requested, approved, scheduled, issued, in progress, complete — labels vary by product); steps are executed and logged in order, and emergency switching can bypass the planning stages but is still recorded.
- **Outage events are predicted, not just entered.** Calls are matched to the network model to predict the outaged device; moving a call or customer to a different device re-runs the prediction and may regroup events. Grouping rules are configurable.
- **Estimated restoration time is a maintained field.** Events carry an ERT that operators update; storm mode typically switches to different calculation behavior; system-wide ERTs can be set for major events.
- **Reliability records are first-class.** Restoration stages accumulate customer-minutes interrupted; completed events carry structured cause codes; events can be excluded from reliability indices only with a recorded reason.
- **Control actions are auditable.** Device operations, alarm handling, and post-completion edits to event records leave audit trails; remote control failures are surfaced to the operator rather than silently dropped.
- **The power-flow core depends on model quality.** Network applications require a maintained model (connectivity, phasing, impedances, limits); products provide model-validation tooling, and implementation guides treat model preparation as a major deployment task.

## Variants

- **Automation posture** — FLISR and Volt/VAR optimization range from advisory (system proposes, operator executes) to supervised automation (system executes within limits, operator can demote to manual). Utilities choose per feeder and per objective.
- **Packaging** — one integrated platform versus a suite of separately licensed products (SCADA, OMS, DMS applications) that together form the ADMS; both exist in the current market.
- **DER management depth** — DER visibility inside the ADMS; a built-in DER-management module; or integration with a separate DERMS platform that handles aggregation, dispatch, and market participation.
- **Deployment** — on-premises control-room servers (traditional) versus hybrid or cloud deployment with web clients (current direction).
- **Network scope** — distribution-only versus an integrated transmission-and-distribution model with coordinated operations between transmission and distribution control rooms.
- **Substrate reuse in adjacent industries** — the same SCADA/OMS substrate is sold for water, gas, and other network industries; the ADMS itself (power flow, voltage, phases, FLISR) remains specific to electric distribution.
- **Regional operating practice** — safety-document regimes, switching-order conventions, and terminology differ by country and utility; products adapt through configuration.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| SCADA | substrate / sibling | telemetry and control organized as points and devices; no connected network model or network-aware applications required; in practice usually embedded in or integrated with the ADMS |
| Distribution Management System / DMS | overlapping / historical | historically the network-analysis application suite (power flow, FLISR, VVO); the current market uses "ADMS" for the integrated platform (SCADA + DMS applications + OMS on one model and UI) |
| Outage Management System / OMS | module / sibling | centers on the call → event → crew → restoration loop; a standalone OMS can exist without real-time network operations; in modern products it is a layer of the ADMS |
| Energy Management System / EMS | same pattern, transmission | same structural pattern (network model + real-time monitoring/control + operational loop + network applications) applied to the transmission grid, with transmission-specific applications and operators |
| DERMS | sibling / module | centers on the DER fleet (aggregation, forecasting, dispatch, market participation) rather than the distribution network itself; appears both as an ADMS module and as a separate integrated platform |
| Grid Operations Platform | generic umbrella | broad marketing term spanning transmission and distribution; the ADMS is the concrete distribution control-room platform |
| Utility GIS | model source | holds as-built geographic asset records; typically the source from which the ADMS operational network model is derived; no real-time operations |
| Advanced Metering Infrastructure / AMI | data integration | metering data collection; contributes meter pings and unsolicited meter status to outage confirmation, but does not operate the network |
| Industrial Historian | component | time-series storage of measurements and events; commonly embedded in or paired with the ADMS |

The most important boundary is against SCADA: the connected distribution network model with network-aware operations is what makes an ADMS more than telemetry and control. The second is against OMS: without real-time monitoring and control of the network, an outage system remains an OMS.

## Representative Products

- Oracle Utilities Network Management System (NMS)
- GE Vernova GridOS ADMS
- AspenTech OSI Advanced Distribution Management System
- SurvalentONE ADMS

The defining core was checked against narrower structures — plain distribution SCADA, network-application-only DMS, and call-center-only OMS — to avoid defining the Type by the current integrated implementation.

## Sources

Research date: **2026-09-06**

- Oracle Utilities Network Management System documentation library (Release 25.12), including the NMS User Guide and the Advanced Distribution Management System Implementation Guide — https://docs.oracle.com/en/industries/energy-water/network-management-system/index.html
- GE Vernova — GridOS ADMS product page and FAQ — https://www.gevernova.com/software/products/gridos/advanced-distribution-management-system
- AspenTech — AspenTech OSI Advanced Distribution Management System product page — https://www.aspentech.com/en/products/dgm/aspentech-osi-advanced-distribution-management-system
- Survalent — product catalog (SurvalentONE ADMS platform, SCADA, OMS, DMS applications) — https://www.survalent.com/products/

> Sourcing limitation: official product documentation was directly accessible for one vendor (Oracle) and product/catalog pages for three others. Vendor sites for Schneider Electric (EcoStruxure ADMS), Hitachi Energy (Network Manager), and Siemens (Spectrum Power) could not be reached from the research environment and were not used as evidence. Workflow details verified only in one vendor's documentation (for example, exact switching-sheet state labels, control-zone authority mechanics, FLISR algorithm steps) are described in this document as conceptual structures or attributed to "products commonly/some products", not as industry-uniform rules. Precise numeric limits and defaults are intentionally omitted.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
