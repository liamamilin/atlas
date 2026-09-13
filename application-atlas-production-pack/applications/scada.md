# SCADA (Supervisory Control and Data Acquisition)

## Overview

A **SCADA system** is the central supervisory system through which operators watch and command a distributed estate of field equipment — remote sites, plant areas, pipelines, utility networks — from one place. It continuously acquires measurements, statuses, and events from field units (RTUs, PLCs, protective relays, meters, remote devices) into a central database of named points, annunciates abnormal conditions, and lets operators issue control commands back to those remote units, which the units' own local logic executes.

The defining core is three structures held together:

```text
Distributed field units (RTUs / PLCs / IEDs / remote devices)
  — each addressable, each running its own local control
        ↕ (communication network)
Central supervisory station
  — telemetry acquired into a point database (values + state)
        ↕ (supervisory commands)
Operators command remote devices; field units execute
```

Remove the distributed field units and what remains is the operator interface of a single local process — an HMI, not a SCADA. Remove the central acquisition and there is no system, only scattered device-local displays. Remove the control write-back and it is telemetry monitoring only — the "supervisory control" half of the name is gone. The combination — a distributed estate supervised and commanded from a center — is what makes it SCADA.

Everything else commonly associated with SCADA — operator screens, alarm acknowledgment, historians, redundancy, web and mobile clients — is the standard mature structure built around that core, not the core itself. Older systems from the founding era of the Type satisfy the definition with none of the modern machinery.

## Users & Context

**Operators (runtime users).** Control-room operators, plant operators, and utility dispatchers work shifts around the clock. They watch process displays and network pictures, respond to alarms, adjust setpoints, start and stop equipment, open and close devices, and record what happened. They do not program the system and do not run the control logic — that lives in the field units.

**Builders (engineering users).** SCADA engineers and system integrators create the system: configure the communication connections to field units, define the point database, draw the screens, configure alarms and operator access, and deploy the result to servers and clients. The same product serves both populations through different surfaces.

**Secondary users.** Maintenance and reliability staff consume history and event records; management often has view-only access; field crews benefit indirectly when the system's data helps locate faults. In utility deployments, corporate users may reach replicated data through segregated (DMZ) paths rather than the operational system itself.

Typical contexts: electric, gas, and water utility networks spread over wide areas; oil and gas pipelines and production sites; plant floors supervising many programmable controllers; infrastructure such as tunnels, airports, marine systems, and broadcasting; renewable generation sites. The common thread is a supervised estate that is *distributed* — classically geographically remote, connected over long-distance or plant-wide networks — and mission-critical: the system runs continuously, often for decades, and its failure modes are treated with the same seriousness as the process itself.

## Core Model

### The Defining Core

**1. The distributed field-unit population.** The system's supervised estate is a population of field endpoints — RTUs, PLCs, intelligent electronic devices, protective relays, meters, remote devices — each individually addressable, each acquiring its own local measurements and statuses, and each executing commands locally with **local control autonomy**: the process keeps running under field-side control even when the supervisory link is down. This autonomy is what "supervisory" means — the center supervises; the field executes. The units are classically geographically remote (pump stations, substations, well sites, treatment plants), which is why the communication machinery matters so much; a plant-wide estate of many autonomous controllers satisfies the same structure.

**2. Central acquisition into a point database.** A central master station continuously acquires telemetry — analog measurements, device statuses, events — from the field units over the communication network into a central database of **named points**. Each point carries a value and its state (good, stale, in communication error), and is named for what it means to the operation rather than for the register it maps to. The organization is point-based: the system does not require a model of what is connected to what. That distinction matters — the systems that *do* hold a connected network model are the neighboring control-room types (distribution and transmission management systems), which stand on a SCADA substrate.

**3. Supervisory control write-back.** Through the same point layer, operators issue commands to remote devices: start and stop, open and close, setpoint changes, mode selections. The command travels from the center to the field unit; the field unit's own logic decides whether and how to execute it. The operator acts from above the process, not inside it — interlocks and protection live in the field equipment, and the supervisory system is expected to respect them, not replace them.

These three form one loop, not three features:

```text
field units (local control autonomy)
   ↕ (communication network — polling, reporting, buffering)
central point database (values + data state)
   ↕ (binding)
operator surfaces (displays, alarm lists, trends)
   ↕ (operator command)
supervisory write-back → field units execute
```

### Standard Capabilities of Mature Products

Around that core, mature SCADA products carry a stable set of capabilities. They are what make the system practical; none of them alone defines the Type:

- **The operator HMI layer.** Every SCADA presents its data through engineered operator screens — process and network displays animated by live values, equipment faceplates, alarm lists, trend charts. The HMI layer is a component of SCADA (one vendor states it directly: SCADA systems "are comprised of HMI software"); the screens themselves are the subject of the separate HMI type.
- **Alarm machinery.** Abnormal conditions are defined on points, annunciated on dedicated alarm surfaces, and **acknowledged** by operators — a visible act of claiming the event. Mature products add shelving or suppression (silencing an alarm for a duration or grouping related alarms), retained alarm and event journals, and notification beyond the control room (email, SMS, voice, remote annunciation).
- **Historical logging and trends.** Selected points are logged over time and displayed as trends; history survives communication interruptions through store-and-forward buffering. Logging depth ranges from embedded modules to dedicated historian products paired beside the SCADA.
- **Communication-integrity machinery.** The unreliable-link reality is a first-class engineering concern: polling management, change-based reporting and deadbanding to reduce traffic, store-and-forward buffering, source time-stamping, modem and radio management, and redundant servers with automatic failover for mission-critical deployments.
- **Engineering environment.** A separate development surface where all runtime content is created: the point-database browser (often with device templates that auto-generate points), the screen editor with symbol libraries, driver and connection configuration, alarm configuration, user management, and a deployment step — commonly with version control and rollback. Runtime content changes only through deployment.
- **Security.** Role-based access decides who may view, command, and engineer. Commanding surfaces are gated; device-level control tokens or locks prevent conflicting operations; corporate access is commonly segregated behind DMZ patterns; certificate-based communications appear in current products.
- **Driver and protocol library.** Broad multi-vendor connectivity — Modbus, DNP3, IEC-class utility protocols, OPC, vendor-proprietary radio and device protocols — is the standard way the field population is reached. The specific protocol set is an implementation choice, not the structure.
- **Event and disturbance recording.** In utility and pipeline deployments: sequence-of-events logs, disturbance capture triggered by defined conditions, fault-data retrieval from protective relays, and operation/outage accounting built on the recorded event stream.
- **Master-to-master data exchange.** Mechanisms for sharing data between SCADA systems — republishing a set of points so another master station can poll them, or exchanging data over utility-standard channels.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently, and a reader who knows only one realization should still recognize the others:

```text
Concept:            distributed field units
Implementations:    RTUs, PLCs, protective relays/IEDs, meters,
                    remote devices reached through gateways

Concept:            central point database
Implementations:    in-memory tag databases, SQL-backed stores,
                    historian-integrated stores

Concept:            communication path
Implementations:    serial/radio/dial-up links, plant Ethernet,
                    wide-area networks, MQTT/IIoT transports

Concept:            operator surfaces
Implementations:    control-room desktop clients, panel displays,
                    web sessions, thin clients, mobile apps
```

## How It Works

### Building the system (engineering loop)

```text
Configure communication connections (drivers/protocols to field units)
→ define the point database (named points mapped to field data,
  often generated from device templates)
→ draw operator screens and bind them to points
→ configure alarm conditions and operator access
→ deploy the project to servers and clients
```

Everything the operator will ever see is created in this loop. Mature products let engineers build concurrently, test against live or simulated data, and deploy changes without interrupting the running system; version control with rollback is standard in current products. After deployment, changes are re-engineered and re-deployed, not edited under the operator's hands.

### Running the estate (supervisory loop)

```text
acquire telemetry from field units, continuously
→ update the central point database (values + data state)
→ render operator displays bound to the live points
→ alarms evaluate against the live data
   → abnormal condition annunciated
   → operator acknowledges (claims) the event
   → operator acts: command a device / adjust a setpoint
      / dispatch attention to the field
→ commands written back to field units; local logic executes
→ values, alarm events, and operator actions recorded
→ the cycle continues for as long as the estate operates
```

This loop is continuous and open-ended. A SCADA system runs for years; the supervised estate keeps operating even when individual links or servers fail, which is why redundancy, buffering, and failover are standard rather than exceptional.

### Capability tiers

**Defining core** — without these, not a SCADA system:

- distributed field units with local control autonomy
- central acquisition into a point database
- supervisory control write-back to remote devices

**Standard mature structure** — present in essentially all products:

- operator HMI layer (displays, alarm lists, trends)
- alarm machinery with acknowledgment and event history
- historical logging with store-and-forward
- communication-integrity machinery (polling management, deadbanding, redundancy/failover)
- engineering environment with deployment and version control
- role-based security with gated commanding
- broad driver/protocol library

**Common variants / optional** — depends on domain, scale, and era:

- web, mobile, and thin clients; remote and multi-site access
- event/SOE recording, disturbance capture, fault-data retrieval
- master-to-master data exchange between SCADA systems
- supervised automation add-ons (for example, feedback control of generation outputs sold as an option in utility SCADA)
- DMZ replication for corporate access; cloud-hosted and edge deployments
- equipment templates for recurring field installations

## Interfaces

### Runtime surfaces (what the operator sees)

**Process / network display.** Purpose: the mental map of the supervised estate. Typical information: sites, equipment, and flow paths drawn as symbols animated by live values, key measurements, active-alarm banner, navigation to detail. Primary actions: navigate, open equipment detail.

**Equipment faceplate.** Purpose: the operating face of one field unit or device. Typical information: that unit's measurements, states, and alarms; sometimes rendered as the device's own front panel. Primary actions: start/stop, open/close, setpoint entry — the supervisory write-back happens here.

**Alarm summary.** Purpose: the operator's queue of abnormal conditions across the estate. Typical information: alarm list with time, source, description, active/cleared state, acknowledgment state, priority. Primary actions: acknowledge, silence, shelve or suppress (where offered), jump to the affected display.

**Trend display.** Purpose: recent history beside the live picture. Typical information: time-series plots of selected points. Primary actions: select pens, change time span, correlate with events.

**Geographic / map views.** Purpose: situational awareness over spread-out estates. Typical information: sites and assets placed on maps with live status coloring. Primary actions: navigate, zoom, open site detail.

**Client reach.** The same surfaces delivered as control-room desktop clients, panel displays, web sessions, thin clients for PCs without the full software, and mobile apps — remote access to the same supervisory picture, with commanding gated by the same security model.

### Engineering surfaces (what the builder sees)

**Point-database browser.** Create, organize, and type points; map them to field data; inspect live values and data state during development; generate points from device templates.

**Screen editor.** Drawing tools, symbol and template libraries, binding dialogs linking graphics to points.

**Connection/driver configuration.** Define the field units, networks, and protocols the system will talk to.

**Alarm and user configuration.** Define alarm conditions on points; define accounts, roles, and which displays/actions each role may reach.

**Deployment surface.** Transfer the finished project to servers and clients; version, roll back, and distribute updates.

## Important Rules / Behaviors

- **Control is supervisory, not executing.** The SCADA issues commands; the field unit's own logic decides whether and how to execute them. Protection and interlocks live in the field equipment. When a SCADA product begins executing the process control itself, it has crossed into control-system territory.
- **The point database is the spine.** Displays, alarms, trends, history, and write-back all read and write through the same named points. The system does not require a model of what is connected to what — when such a model is added and made operational, the system has grown into the neighboring network-management types.
- **Data state is surfaced, not hidden.** When a field link drops, the system does not present stale values as if they were good — the data state (good, stale, failed) is visible so operators never command on dead data.
- **Alarm acknowledgment is a deliberate operator act.** Acknowledging does not clear the condition; it records that an operator has seen and taken ownership. Conditions clear when the field situation recovers; acknowledgment and clearing are independent, and both are recorded.
- **The communication link is a designed component.** Polling rates, change-based reporting, buffering, and store-and-forward exist because links are slow, expensive, or interruptible; history and events are expected to survive interruptions intact.
- **Runtime content changes only through deployment.** What the operator sees is a deployed artifact; live editing is not part of the operating model. This separation protects continuity of a system that may not be stopped.
- **Commanding is gated.** Viewing is commonly open to more roles; commanding and setpoint changes are restricted; engineering is restricted further. Device-level locks or tokens can block conflicting operations — including from automation.
- **Redundancy is the availability mechanism.** Mission-critical deployments run primary/backup servers with automatic failover; clients reconnect to the surviving server. The estate's operation is expected to outlive any single component.

## Variants

- **Utility network SCADA** — electric distribution, gas, water/wastewater, transit: wide-area estates of remote sites, radio and leased-line heritage, event/SOE and disturbance machinery, often the foundation beneath outage- and network-management systems.
- **Pipeline and oil & gas SCADA** — compressor stations, well sites, tank farms over long distances; leak/pressure monitoring and remote control along the line.
- **Plant / factory SCADA** — supervision of many programmable controllers across a plant; the same core with plant-Ethernet instead of wide-area links.
- **Infrastructure SCADA** — tunnels, airports, marine systems, broadcasting: distributed equipment estates with the same supervisory pattern.
- **Scale poles** — single-server small systems; distributed client/server estates; multi-site enterprise systems spanning regions.
- **Packaging poles** — standalone SCADA products; SCADA as the module composing a larger control-room estate (utility ADMS platforms sell SCADA as their foundation); SCADA as one solution on a multi-purpose industrial platform; SCADA inside an automation vendor's HMI/SCADA family.
- **Deployment poles** — on-premises hardened servers (classic); web-deployed clients; cloud-hosted and edge editions.
- **Control posture** — manual supervisory control as the base; supervised automation (feedback control of generation, pump scheduling) as add-ons within configured limits.
- **Era naming** — the same structure has been sold as telecontrol/telemetry systems, then SCADA, and currently as "industrial platforms" and "IoT-ready SCADA". The founding-generation master-plus-RTU systems satisfy the defining core with none of the modern machinery.

## Related Application Types

| Application Type | Distinction |
|---|---|
| HMI | the operator-interface layer for a machine or local process (screens + live data + write-back). Every SCADA *contains* HMI surfaces as its operator layer; the HMI type is defined by that operator surface itself, without the distributed field-unit population. Strip the distributed estate from a SCADA deployment and a clean HMI remains; add remote field units and a supervisory center to an HMI and it becomes SCADA. The market bundles the words freely ("HMI/SCADA") because single product families span both. |
| Distributed Control System (DCS) | the plant-wide integrated control system: distributed controllers executing configured control strategies as the system's core function, with integrated engineering of the control logic. SCADA supervises field units whose controllers run the process; it does not execute the control. Vendors sell them as separate product lines. |
| ADMS / EMS (distribution and transmission management) | stand on a SCADA substrate and add the connected electrical network model with network analysis and domain applications. Remove the network model and analysis and only SCADA remains — the seam both siblings use. |
| Industrial Historian | the archival system of record for process measurements, with no control duty. SCADA commonly embeds or pairs a historian; the archive is a distinct type. |
| Industrial IoT Platform | device connectivity, fleet management, and data access with asynchronous operations through agents and gateways; no live supervisory control duty over a process. SCADA's defining loop is live supervision plus command. IIoT transports (MQTT) increasingly feed SCADA data layers — transport does not separate the types. |
| PLC Programming Environment | engineers the controller's control logic; SCADA supervises the running result. Automation suites often bundle both — packaging, not identity. |
| Grid Operations Platform | an umbrella market name over the utility control-room family; SCADA is its substrate member. The umbrella's own removal test — strip the network model, analysis, and domain applications and SCADA remains — matches this type's core. |
| Monitoring dashboards / telemetry-only systems | acquisition and display without supervisory control write-back; the "supervisory control" half of the name is load-bearing. |

The most important boundary is the HMI one, because the market uses the words interchangeably. The working line: HMI names the operator interface to a machine or local process; SCADA names the supervisory system over a distributed field-unit population. The operator-screen machinery is shared; the supervisory architecture is not.

## Representative Products

- **Ignition** (Inductive Automation) — independent, web-deployed platform whose vendor positions SCADA as its flagship solution; documented here and (at manual depth) in the paired HMI research
- **AVEVA Plant SCADA** (AVEVA, ex-Citect SCADA) — the large-vendor industrial SCADA lineage for plant and infrastructure operations
- **SurvalentONE SCADA** (Survalent) — the utility/multi-utility SCADA specialist, marketed as the foundation beneath its ADMS estate
- **VTScada** (Trihedral) — independent all-in-one SCADA platform with a 35-year lineage, strongest in water and oil & gas
- **GE Vernova CIMPLICITY / iFIX / iPower** — the automation-vendor HMI/SCADA family, spanning plant supervision to utility control rooms

The defining core was checked against older and differently positioned realizations — founding-generation master-station-plus-RTU systems, the 1980s–90s software SCADA generation, and modern web-deployed platforms — so that the definition does not over-fit any single deployment shape, protocol, or business model.

## Sources

Research date: **2026-09-09**

- Inductive Automation — Ignition SCADA software page: https://inductiveautomation.com/scada-software
- Inductive Automation — Ignition product page: https://inductiveautomation.com/ignition/
- Inductive Automation — Ignition 8.3 User Manual (tags, alarming, architecture; reached in the paired HMI research, 2026-09-08): https://docs.inductiveautomation.com/docs/8.3/
- AVEVA — Plant SCADA product page: https://www.aveva.com/en/products/plant-scada/
- Survalent — SurvalentONE SCADA: https://www.survalent.com/products/scada/
- Survalent — SurvalentONE SCADA Optional Applications: https://www.survalent.com/products/survalentone-scada-optional-applications/
- Trihedral — What is VTScada Software: https://www.vtscada.com/what-is-vtscada/
- Trihedral — VTScada Software Licensing: https://www.vtscada.com/software-licensing/
- GE Vernova — CIMPLICITY HMI/SCADA (extensions page, incl. iPower): https://www.gevernova.com/software/products/hmi-scada/cimplicity

> Sourcing limitation: operational documentation for several large automation vendors (Siemens, Schneider Electric, Rockwell Automation, Hitachi Energy) could not be reached from the research environment, consistent with prior research passes in this domain; the automation-vendor pole is evidenced through one vendor's public pages plus cross-product patterns. No Tier-1 operational manual was newly fetched in this pass; detailed operational rules are stated at commonality strength, and precise vendor figures (device counts, driver counts, retention windows, license tiers) are intentionally omitted. The HMI↔SCADA boundary documented here was jointly reviewed with the paired HMI research.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis — including the resolution of the joint review with the HMI type — are recorded in the paired Research Notes.
