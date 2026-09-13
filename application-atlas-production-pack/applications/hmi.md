# HMI (Human-Machine Interface)

## Overview

An **HMI (Human-Machine Interface) Application** is the operator-facing live interface between people and controlled industrial processes. It acquires live process data from controllers and devices, renders engineered graphical screens bound to that live data, and lets operators act on the process — entering setpoints, issuing commands, acknowledging abnormal conditions — with those actions written back through the same live-data layer.

The defining core is three structures held together:

```text
Live process data from controllers/devices
        ↓
Engineered operator screens bound to that data
        ↓
Operator actions written back to the process
```

Remove the live process data and the product is a graphics mockup or a business dashboard; remove the screens and it is a protocol gateway or data logger; remove the operator write-back and it is a passive monitoring display. The combination — see, act, and have the process answer — is what makes it a machine interface rather than a reporting surface.

## Users & Context

Two distinct user populations work on the same application, and the Type is defined by both:

**Operators (runtime users).** Machine operators, control-room and unit operators, plant technicians. They stand at a panel beside a machine, sit in a control room, or walk the plant with a tablet. Their work: watch the process on screens, respond to alarms, adjust setpoints, start and stop equipment, record or confirm what happened. They do not program anything.

**Builders (engineering users).** Control engineers, system integrators, and machine-builder engineering staff. They create the application: connect to controllers, define the live-data points, draw the screens, configure alarms and operator access, and deploy the result to panels, servers, or web sessions. In practice the same product serves both populations through different surfaces.

Typical contexts: discrete manufacturing lines and single machines (machine-builder scope), process plants (chemical, food, water/wastewater, energy), building and utility plants, packaging lines, and increasingly remote or mobile access to the same equipment.

## Core Model

### The Defining Core

**1. The live process-data layer.** The application holds a database of named data points — commonly called *tags* — that represent the process: temperatures, pressures, speeds, levels, motor states, valve positions, counters. Each tag acquires its value from a controller, drive, or device through an industrial driver or protocol, or is computed locally. Tags are deliberately decoupled from raw device addresses: a tag can be named for what it means to the process ("Motor 3 Amps") regardless of the register or path it maps to. Tags carry not only a value but also its state — whether the value is good, stale, or in communication error — because an operator's trust in a screen depends on knowing whether the data is alive.

**2. Engineered operator screens.** The visible world of the product is a set of graphical screens built in advance and executed at runtime: process overviews (pumps, valves, conveyors drawn as symbols whose appearance animates from live values), equipment detail faces, gauges, numeric indicators, buttons and input fields. Every graphical element is *bound* — a defined link between the graphic's appearance or behavior and a tag, so the screen literally renders the live process. Screens are organized by navigation into an operator path: overview → area → equipment.

**3. The operator write-back loop.** The same tags that drive the graphics also carry operator actions back to the process: a typed setpoint, a start/stop command, a mode selection, a recipe value. The operator's actions are writes to controller data, which the controller's own logic then executes. This loop is what separates the HMI from every monitoring-only display: the operator can not only see the process but change it, within the limits the application and controller enforce.

These three form one loop, not three features:

```text
controllers/devices
   ↕ (industrial drivers/protocols, cyclic acquisition)
live tag layer (values + data state)
   ↕ (binding)
operator screens (rendered live)
   ↕ (operator action)
write-back: setpoints, commands → the process
```

### Standard Capabilities of Mature Products

Around that core, mature HMI products carry a stable set of capabilities. They are what make the product practical, though none of them alone defines the Type:

- **Alarm machinery.** Alarms are conditions defined on the live data (a value over a limit, a bad state, a communication fault). When a condition occurs it is annunciated to the operator on dedicated alarm surfaces; the operator **acknowledges** it — a visible act of claiming the event that other operators can see — and the event is recorded with its timestamps and transitions even after the condition clears. The acknowledgment loop and the retained alarm history are central to how operators actually work; the richer variants (shelving for maintenance windows, notification by email/SMS/voice, escalation routing, on-call rosters) appear in the larger products.
- **Historical trends.** Selected data points are logged over time and displayed as trend charts alongside the live screens. Logging depth varies from a short embedded buffer to a full time-series database; larger installations pair the HMI with a dedicated historian product.
- **Engineering environment.** A separate development surface where all the runtime content is created: the screen editor with symbol and component libraries, the tag database browser, driver/connection configuration, alarm configuration, user management, and a deployment step that installs the finished project onto panels or servers. The engineering and runtime worlds are deliberately separate — screens are built and tested, then deployed, not edited live.
- **Operator security.** User accounts and role-based access decide which operators can view which screens and, critically, which actions they may take: viewing is usually open, commanding and setpoint changes are restricted, engineering is restricted further.
- **Reusable equipment objects.** Predefined templates for recurring equipment (motor, valve, tank, drive) that bundle graphics, tags, and alarms, so each new instance inherits a consistent face.
- **Data-state presentation.** Screens make missing or stale data visibly different from a legitimate value, so operators do not command a process on dead data.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently, and a reader who knows only one realization should still recognize the others:

```text
Concept:              live process-data layer
Implementations:      OPC-sourced tags, native controller drivers, MQTT/IIoT feeds,
                      locally computed/derived points

Concept:              engineered operator screens
Implementations:      embedded panel runtimes, desktop clients, HTML5/web sessions,
                      mobile-responsive sessions

Concept:              deployment
Implementations:      screen project downloaded to a panel, project saved to a
                      central server, web session launched from a server,
                      standalone edge runtime next to the machine
```

## How It Works

### Building the application (engineering loop)

```text
Configure device connections (drivers/protocols to controllers)
→ define the tag database (named points mapped to device data)
→ draw screens and bind their elements to tags
→ configure alarm conditions and operator access
→ deploy the project to its runtime (panel, server, web)
```

Everything the operator will ever see is created in this loop. Mature products let engineers test screens against live or simulated data before deployment, and let several engineers build one application concurrently; after deployment, changes are re-engineered and re-deployed, not edited under the operator's hands.

### Running the process (runtime loop)

```text
acquire live values from controllers, cyclically
→ render screens bound to the live data
→ operator navigates: overview → area → equipment
→ alarms evaluate against the live data
   → abnormal condition annunciated on alarm surfaces
   → operator acknowledges (claims) the event
   → operator acts: adjust setpoint / issue command / correct the fault
→ operator actions written back through the tag layer
→ values, alarm events, and history retained
→ the cycle continues for as long as the process runs
```

This loop is continuous and open-ended. An HMI application runs for years; screens change only through the engineering loop, and the runtime's job is to be present and correct every shift.

### Capability tiers

**Defining core** — without these, not an HMI:

- live process-data layer (tags from controllers/devices, with data state)
- engineered operator screens bound to that data
- operator write-back to the process

**Standard mature structure** — present in essentially all products:

- alarm annunciation with operator acknowledgment and event history
- historical logging and trend displays
- engineering environment with deployment step
- user accounts and role-based operational access
- reusable equipment templates and symbol libraries

**Common variants / optional** — depends on segment, scale, and era:

- notification and escalation beyond the panel (email/SMS/voice, rosters)
- recipe/parameter-set management
- web and mobile sessions, remote and multi-site access
- redundancy and store-and-forward for unreliable links
- cloud data upload and analytics layers
- graphics-standard programs (high-performance HMI styling)
- multi-language runtime

## Interfaces

### Runtime surfaces (what the operator sees)

**Process overview screen.** Purpose: the mental map of the machine or process area. Typical information: process graphics (tanks, pipes, conveyors, drives) animated by live values, key indicators, active-alarm banner, navigation to detail screens. Primary actions: navigate, open equipment detail.

**Equipment detail screen.** Purpose: faceplate for one machine or unit. Typical information: that unit's measurements, states, per-device alarms. Primary actions: start/stop, mode selection, setpoint entry — the write-back happens here and on the overview.

**Alarm summary.** Purpose: the operator's queue of abnormal conditions. Typical information: alarm list with time, source, description, active/cleared state, acknowledgment state. Primary actions: acknowledge, silence, (where offered) shelve, jump to the affected screen.

**Trend display.** Purpose: recent history beside the live picture. Typical information: time-series plots of selected tags. Primary actions: select pens, change time span, correlate with events.

**Parameter/recipe surfaces.** Purpose: managed entry of process settings. Primary actions: load/apply a parameter set, edit values within permission limits.

**Operator session context.** Login/logout; the current user identity gates what actions the runtime accepts. On mobile sessions the same surfaces adapt to touch and small screens; on fixed panels they run kiosk-style.

### Engineering surfaces (what the builder sees)

**Screen editor.** Drawing tools, symbol/component libraries, animation and binding dialogs (linking graphics to tags), screen templates.

**Tag database browser.** Create, organize (folders), and type tags; map to device addresses or logic; inspect live values and data state during development.

**Connection/driver configuration.** Define the controllers, networks, and protocols the runtime will talk to.

**Alarm and user configuration.** Define alarm conditions on tags; define user accounts, roles, and which screens/actions each role may reach.

**Deployment surface.** Save/download the finished project to panels or servers; version and distribute updates.

## Important Rules / Behaviors

- **The live-data layer is the spine.** Screens, alarms, trends, and write-back all read and write through the same named points. When the controller connection drops, the runtime does not show stale values as if they were good — mature products surface the data state so operators can distinguish a real zero from a dead link.
- **Write-back is bounded by the controller, not the screen.** The HMI sends setpoints and commands; the controller's own logic decides whether and how to execute them. The screen can make an action possible without making it safe — interlocks live in the controller, and the application is expected to respect them, not replace them.
- **Alarm acknowledgment is a deliberate operator act.** Acknowledging does not clear the condition; it records that an operator has seen and taken ownership of it. Conditions clear when the process recovers; acknowledgment and clearing are independent, and both are recorded.
- **Operator permission gates the commanding surface.** View, command, and engineer are different trust levels. A logged-in operator identity is required for actions that change the process; many products also let screens hide or disable actions the current user may not take.
- **Runtime content changes only through deployment.** What the operator sees is a deployed artifact; live editing is not part of the operating model. This separation protects process continuity — screens can be tested and staged before they replace what operators currently use.
- **No process logic is executed by the HMI.** The application observes and commands; it does not run the control loop. When an HMI product begins executing control logic itself, it has crossed into control-system territory.

## Variants

- **Machine-level panel HMI** — embedded on the machine, engineered by the machine builder, single-machine scope, small tag set; the volume backbone of the Type.
- **Plant/client-server HMI** — one or a few operator stations for a plant area, tags aggregated on a server, shared engineering.
- **Web/mobile HMI** — sessions delivered from a server to browsers and handhelds; same core loop, remote reach; often the newest layer on older systems.
- **Ecosystem-bundled HMI** — sold inside a controller vendor's automation suite, deeply integrated with that vendor's programming environment; also the independent-platform posture that connects to every vendor instead.
- **Hardware-attached HMI software** — configuration software paired with a vendor's own panels and meters, sold with the hardware for harsh environments.
- **Scale drift toward SCADA** — when the same product family is extended with multi-site telemetry, remote field stations, and central fleet historians, the system becomes a supervisory (SCADA) system that *contains* HMI surfaces; the operator-interface layer itself does not change.

## Related Application Types

| Application Type | Distinction |
|---|---|
| SCADA | the multi-site supervisory system (telemetry, central data collection, fleet-scale alarming); every SCADA deployment contains HMI surfaces, but the HMI Type is the operator-interface layer, not the supervisory system around it |
| PLC Programming Environment | engineers the controller's control logic; the HMI engineers screens/tags/alarms and observes or commands the result — logic execution vs operator surface |
| Distributed Control System (DCS) | the control system that runs the process; the HMI is its operator face, not the controller |
| Industrial Historian | the dedicated long-term time-series system of record; HMI trends are a display capability, often fed by such a historian |
| Industrial IoT Platform | device connectivity, data pipelines, and cloud analytics; an IIoT dashboard without operator write-back and alarm acknowledgment is monitoring, not a machine interface |
| Dashboard Platform (BI) | renders business/analytical data; no controller protocols, no process write-back, no alarm-acknowledgment loop, no engineering/deployment cycle |
| Digital Twin Platform | centers on a model/simulation of the asset; the HMI centers on the live process surface |
| Building Management System | operator control of building services, a closely related operator-interface pattern bound to the building domain rather than general industrial equipment |

The most important boundary is the SCADA one, because the market bundles the words freely ("HMI/SCADA"). The working line: HMI names the operator interface to a machine or local process; SCADA names the supervisory multi-site system. The same product family can serve both — the operator-screen core is identical either way.

## Representative Products

- **Ignition** (Inductive Automation) — independent, web-deployed HMI/SCADA platform; documented here at full operational depth
- **AVEVA InTouch HMI** (AVEVA) — the classic independent plant-HMI lineage, process-industry enterprise pole
- **Red Lion / HMS Networks** panel HMI line — hardware-attached visualization and control for machine builders and harsh environments

The defining core was checked against older and differently positioned realizations — the classic Windows-era plant HMI generation, hardware-embedded panel HMIs, and modern web/mobile sessions — so that the definition does not over-fit any single deployment shape, protocol, or business model.

## Sources

Research date: **2026-09-08**

- Inductive Automation — Ignition product page: https://inductiveautomation.com/ignition/
- Inductive Automation — Ignition HMI solution page: https://inductiveautomation.com/solutions/hmi
- Inductive Automation — Ignition 8.3 User Manual (Introducing Ignition; Tags; Alarming; Perspective and Vision): https://docs.inductiveautomation.com/docs/8.3/
- AVEVA — InTouch HMI product page: https://www.aveva.com/en/products/intouch-hmi/
- HMS Networks (Red Lion) — brand positioning: https://www.redlion.net/products/crimson (redirects to HMS Networks)

> Sourcing limitation: operational documentation for Siemens WinCC, Rockwell FactoryTalk View, and the AVEVA/Red Lion configuration tools was not reachable during research (site errors / JavaScript-only portals). Claims drawn from those products are limited to their public positioning; detailed operational rules in this document are supported primarily by the reachable product documentation, with cross-product patterns stated at commonality strength. Precise vendor figures (tag counts, limits, performance numbers) are intentionally omitted.

Detailed evidence, per-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
