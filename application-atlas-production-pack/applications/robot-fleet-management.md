# Robot Fleet Management

## Overview

A **Robot Fleet Management** application is the operator-facing system for running a fleet of robots — most commonly autonomous mobile robots (AMRs) in warehouses and factories, and in the wider market also inspection robots, drones, and other autonomous machines. It holds the fleet's robots as individually identified managed units, directs work to them as executable missions or tasks that the robots themselves carry out, and gives fleet-side staff a continuous oversight loop: watch the fleet live, dispatch and prioritize work, intervene when a robot or task needs help, and keep the fleet healthy.

The defining core is small:

```text
Robot register (the fleet as identified managed units)
└── Work directed to robots as executable missions/tasks
    (the robots are the executing party)
    └── Fleet-side oversight loop
        (monitor live → dispatch/intervene → keep the fleet healthy)
```

Everything else commonly associated with the category — live maps, traffic management, opportunistic charging, teleoperation, AI-based assignment, WMS integration — is widespread in current products but is not what makes a product a robot fleet manager. A single robot can run on its own; it is the *fleet* — many robots whose work must be directed, coordinated, and supervised from one place — that requires this Type of application.

When the robots are human-driven road vehicles, the product is a Fleet Management System; when they are road-going autonomous vehicles, it is Autonomous Fleet Management; when the "workers" are software agents, it is an agent orchestration platform. The robot fleet's defining difference is that the managed workers are physical robots executing the site's work themselves.

## Users & Context

The primary users are the people responsible for keeping an automated operation running:

- **Operations supervisors / shift leads** — watch the live fleet picture, monitor work progress, respond to exceptions, and keep throughput up during a shift.
- **Automation or robotics engineers** — commission robots onto the system, define and adjust workflows (routes, tasks, zones), tune traffic and assignment behavior, and diagnose recurring faults.
- **IT / systems administrators** — manage user accounts and authentication, deploy and update the fleet-management server or cloud tenant, and maintain integrations with business systems.

Secondary users include maintenance staff (robot health, charging infrastructure), and — in fulfillment-oriented deployments — the broader operation, because some platforms coordinate human workers and robots as one workforce.

The work environment is an industrial site: a warehouse, a factory floor, a distribution center, or a facility being inspected. The fleet-management application itself is operated from web dashboards on desktops and tablets, often alongside wall-mounted or control-room displays; field interaction with individual robots happens through companion apps or the robots' own interfaces. The system runs either on a dedicated on-premises server, as a cloud service, or — in robots-as-a-service arrangements — is operated by the vendor on the customer's behalf.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being a robot fleet manager:

- **Robot register.** Every robot in the fleet is an individually identified managed record — an identity, a type/model, a configuration, and a current status. Robots are added onto the system when commissioned (connected to the network, registered, configured) and removed when decommissioned or moved to another site. Without the register there is no fleet to manage — only disconnected robots or a bare asset list.

- **Work directed to robots as executable missions/tasks.** The system's unit of work is a task or mission — a transport job between two points, an inspection route, a pick-and-carry sequence, a patrol — expressed in terms the robot can execute. Critically, the *robot* is the executing party: the system hands work to robots, and the robots carry it out autonomously (or under remote control when needed). This is what distinguishes the Type from systems that merely track work done by humans. Without directed work, the product is a monitoring dashboard over robots that do nothing.

- **Fleet-side oversight loop.** A human role — supervisor, fleet operator, robotics engineer — continuously observes live execution across the whole fleet and acts on it: dispatching and prioritizing work, intervening when a robot is stuck, lost, faulted, or a task fails, changing robot modes, and managing fleet health (battery and charging, software updates, configuration). Without this loop, autonomy simply runs unmanaged — a robot system, not fleet *management*.

### Standard Capabilities

Mature products commonly carry most of the following. They make the core loop practical; they are not what defines the Type.

- **Live fleet picture** — a map or status dashboard showing where each robot is, what it is doing, its battery state, and the state of active work.
- **Assignment logic** — the system pairs incoming work with robots automatically, weighing battery level, current utilization, proximity, and priority. The sophistication ranges from simple rules to optimization and AI; the assignment act itself is part of the loop.
- **Robot states and task states** — user-visible status for each robot (working, waiting, charging, blocked, faulted, offline, in emergency stop) and for each task (queued, executing, completed, failed, cancelled). Exact vocabularies vary by product.
- **Exception handling** — surfacing faults and stalls (obstacle stops, lost localization, failed tasks, emergency stops) with recovery paths: re-localize a lost robot, retry or reassign a failed task, return a robot to service.
- **Battery and charging management** — for mobile robots, the system dispatches robots to chargers, charges opportunistically between jobs, and treats power as a constraint on assignment.
- **Facility model** — for site-running fleets, a spatial model of the workplace: recorded maps, named destinations (docks, workstations, chargers, parking), zones with rules (restricted areas, speed limits, traffic controls), and queues at shared locations.
- **Business-system integration** — connections upward to the systems that decide what work the operation needs (warehouse management, manufacturing execution, ERP, CMMS) and sideways to industrial control (PLCs), so that work requests flow in and results flow out. Interoperability standards for multi-vendor robot fleets exist in this space.
- **Notifications and alerts** — event-driven messages to the right people (email, SMS, chat, incident tools) when robots fault or work stalls.
- **Analytics and reporting** — utilization, throughput, mission analysis, trend dashboards, and data export for business analysis.
- **Users, roles, and access** — role-differentiated surfaces (operator vs engineer vs administrator), authentication including enterprise SSO, and audit trails.
- **Remote operation** — in many products, the ability to remotely drive or assist a robot, from occasional remote assistance to full teleoperation.
- **Fleet maintenance machinery** — software updates pushed to robots, configuration templates applied across the fleet, health monitoring over time.

### One Structure, Many Implementations

The core model is written conceptually; products realize each concept differently:

```text
Concept:            Robot register
Implementations:    robots registered on a fleet server (manufacturer stacks);
                    devices provisioned with a software agent (vendor-agnostic platforms);
                    robots bound to a vendor cloud account

Concept:            Work unit
Implementations:    jobs → workflows → tasks → steps (granular industrial stacks);
                    jobs as sequences of locations and tasks;
                    missions as waypoint paths;
                    simple commands and schedules

Concept:            Assignment
Implementations:    robot "bidding" on activities; rule-based auto-assignment;
                    optimization engines; manual dispatch; scheduled triggers

Concept:            Oversight surface
Implementations:    map-based fleet dashboards; status lists; live video;
                    exception queues; replay/analysis tooling
```

A reader who has only seen one implementation — say, a manufacturer's map-based AMR dispatcher — should still be able to recognize a vendor-agnostic observability platform with command and teleoperation surfaces as the same Type, because the register + directed work + oversight loop is intact.

## How It Works

### Commission a robot into the fleet

```text
Prepare the robot (network connection, software)
→ register it on the fleet system (identity, type, configuration)
→ give it a model of its workspace (record a map / define its operating area)
→ define destinations and rules (docks, chargers, zones, traffic)
→ verify it localizes and executes a test task
```

New robots can often inherit configuration from existing ones, which is what makes fleet scaling practical. Removing a robot, or moving it to another facility, is the reverse path — and multi-site operations keep per-site models under one enterprise view.

### Define the work

Work enters the system in two ways. People define reusable workflows — named sequences of locations and actions ("fetch a pallet from staging and drop it at line 3"; "run the nightly inspection route") — which become the operation's task library. And connected business systems raise work requests through integrations: a WMS asks for a pallet move, a MES calls for parts delivery, a CMMS opens an inspection work order. Requests are translated into executable tasks for the fleet.

### Run the operational loop

```text
Work request arrives (manual, scheduled, or from a business system)
→ task is queued
→ system assigns it to a suitable robot (battery, proximity, utilization, priority)
→ robot executes: navigates, docks, lifts, inspects — reporting state as it goes
→ fleet picture updates live; stakeholders watch progress
→ task completes (or fails / blocks) and is recorded
→ robot moves to its next assignment, or to a charger
```

This loop runs continuously across the whole fleet. The human role is supervision by exception: the system keeps work flowing automatically, and people step in when something needs judgment.

### Intervene when something needs help

Exceptions are a normal part of running a fleet, and products give them first-class treatment:

- a robot is **blocked** by an obstacle or congestion — it waits, reroutes, or raises the stall;
- a robot is **lost** (localization failed) — an operator re-localizes it against the map;
- a **task fails** — the supervisor inspects why, retries, reassigns, or cancels it;
- a robot hits an **emergency or safety stop** — it must be cleared and returned to service;
- a robot **requests input** — in some platforms the robot itself asks a human a question ("is this obstacle dangerous?") and proceeds based on the answer.

Remote operation is the deepest intervention path: an operator drives or assists the robot directly when autonomy cannot cope.

### Keep the fleet healthy

Alongside the live loop, the system accumulates the fleet's history — completed work, faults, battery cycles, utilization — surfaced as analytics and reports. Engineers use it to tune workflows and traffic, plan charging, schedule maintenance, and push software/configuration updates out to robots. This is the management layer that turns a pile of robots into a durable, improving operation.

### Core, standard, and optional

- **Defining core** — robot register; work directed to robots as executable missions/tasks; the fleet-side oversight loop.
- **Standard capabilities** — live fleet picture; assignment logic; robot/task states; exception handling; battery/charging; facility model; business-system integration; notifications; analytics; roles/access; fleet maintenance.
- **Optional / variant** — teleoperation depth; multi-vendor interoperability; AI overlays (vision-based inspection intelligence, adaptive assignment); human+robot joint workforces; simulation environments; digital-twin data products.

## Interfaces

The following surfaces are described conceptually; layouts and names vary by product.

### Fleet map / dashboard

The primary oversight surface.

- shows robots on a facility map or in a status list: position, state, battery, current task
- aggregates fleet-level health and active work
- primary actions: filter and group the fleet, drill into a robot, watch work progress

### Robot detail

The per-robot surface.

- identity, model/configuration, current state and mode, battery, recent history, live sensor/camera views where provided
- primary actions: change mode (autonomous/manual/paused), send to charge, re-localize, remote-control or teleoperate, update configuration

### Work / mission management

The work-direction surface.

- task and mission definitions (the workflow library), the live queue, schedules
- primary actions: create/edit workflows and missions, dispatch or schedule work, prioritize, cancel, inspect task states and results

### Exception / intervention surface

The by-exception supervision surface.

- fault and stall lists with filters, per-robot exception detail, recovery actions
- in some products, robot-initiated requests for human input, and teleoperation consoles

### Configuration / administration

The engineer and IT surface.

- facility model editing (maps, destinations, zones, traffic rules), robot commissioning and configuration templates, user/role/authentication management, integration setup (APIs, PLC links), server or tenant administration

### Analytics / reporting

The improvement surface.

- utilization, throughput, mission and fault analysis, trends over time, exports
- primary actions: build and view reports, compare periods, export data

## Important Rules / Behaviors

### The robots are the executing party

The system directs work; robots execute it. This inverts the driver-centric logic of vehicle fleet management: there are no driver records, hours-of-service, or behavior scores, because there are no drivers. Human roles exist on the oversight side, not the execution side (except where remote operation or joint human-robot workforces apply).

### Safety lives on the robot; coordination lives on the system

Robots carry their own safety machinery — onboard sensing and safety-rated hardware that stop the robot around people and obstacles — and safety stops and emergency stops are cleared through defined recovery paths on the robot side. The fleet-management layer coordinates site-level automation (traffic flow, work assignment) rather than replacing onboard safety; at least one major product states explicitly that its fleet manager must not be treated as part of a safety system. The practical consequence for operators: a stopped robot is recovered through the robot's own safety state, not by overriding it from the dashboard.

### State is user-visible and load-bearing

Robot states (working / waiting / charging / blocked / faulted / offline) and task states (queued / executing / succeeded / failed / cancelled) are exposed directly to operators, and certain robot states explicitly block a robot from accepting new work until cleared. The exception queue — not the map — is often where supervisors actually spend their time.

### Shared resources need coordination

Destinations, chargers, intersections, and narrow aisles are shared by the whole fleet. Products model them explicitly (queues at endpoints, single-robot zones, traffic controls, charging logic) because uncoordinated fleets deadlock themselves. This coordination machinery is why a multi-robot fleet needs the management layer at all — a single robot can run without it.

### The fleet manager sits below the business layer

Work typically originates in systems that own the operation's business logic (WMS, MES, ERP, CMMS). The fleet manager executes that work with robots and reports results back; it does not own inventory, orders, or maintenance business rules. Integration is therefore a structural feature, not an add-on.

## Variants

- **AMR material-handling fleets** (the dominant form) — transport, pallet handling, tugger trains in warehouses and factories; full facility models, traffic machinery, charging logic.
- **Fulfillment-platform variants** — robots-as-a-service picking/putaway fleets where the platform coordinates human associates and robots as one workforce and the vendor operates the system.
- **Inspection-robot fleets** — quadruped/mobile inspection robots running scheduled inspection missions; the work unit is the inspection route, and the value layer includes captured data, anomaly alerts, and integration with maintenance systems.
- **Vendor-agnostic operations platforms** — robot-agnostic cloud platforms providing observability, commands, interventions, and teleoperation across heterogeneous robots; strongest at the oversight and data layers.
- **Multi-vendor orchestration** — fleet managers that unify robots from different manufacturers under an interoperability standard, coordinating mixed fleets and even mixed autonomous/manual equipment.
- **Deployment variants** — on-premises server appliances (common in factories with no cloud posture), cloud SaaS, on-prem hub + cloud hybrid, and vendor-operated (RaaS).
- **Robot-population breadth** — single-class fleets vs mixed fleets; drones and other robot classes extend the same core (register + missions + oversight), though the sampled evidence is strongest for ground robots.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Fleet Management System (road) | sibling sharing the register + oversight family pattern | road FMS supervises human-driven vehicles — driver behavior, hours of service, licensing, compliance; here robots execute the work themselves and there is no driver dimension |
| Autonomous Fleet Management | sibling (road AVs) | supervises road-going autonomous vehicles — public-road permits, mixed traffic, validated operating conditions; this Type supervises site-running robots doing facility work |
| Mining Fleet Management | sibling (mine sites) | centers the production cycle — load/haul/dump records, material identity, shift production; this Type centers task/mission execution for site operations generally |
| Marine Fleet Management | sibling (shipping) | asset-administration-centric — per-vessel technical records, crew, surveys, ship–shore loop; no shared record objects beyond the family pattern |
| Robotics Engineering Platform | adjacent (unprocessed sibling) | authoring/programming/simulating robot applications vs operating deployed fleets; simulation may appear in both, but building robots' software is a different Type from running robots |
| Warehouse Management System | upstream integration partner | WMS owns inventory and decides what work the operation needs; the fleet manager executes the physical work with robots and reports back — decides-vs-executes |
| SCADA / HMI | adjacent (fixed equipment) | SCADA supervises fixed process equipment through control loops; this Type directs mobile/autonomous robots through a task loop over a facility model |
| Agent Orchestration Platform | naming-adjacent | orchestrates software agents executing digital tasks; here the workers are physical robots with maps, batteries, and safety — disjoint record worlds |
| Vehicle Telematics Platform | data layer | telematics acquires and streams machine data; the fleet manager is the management application over the fleet — monitoring alone, without work direction and intervention, is not this Type |
| Machine Vision Platform | adjacent (line-level) | vision systems give robots per-item decisions at the line; the fleet manager manages the fleet those robots belong to |

## Representative Products

- **OTTO Fleet Manager** (OTTO by Rockwell Automation) — AMR manufacturer's fleet-management platform for enterprise material handling; extensively documented operational machinery (workflows/tasks, robot and task states, maps/zones/endpoints, exceptions, analytics, on-prem deployment).
- **Fleet Central** (Seegrid) — AMR manufacturer's fleet software with multi-vendor orchestration via an interoperability standard; documents the single-robot-vs-fleet distinction directly.
- **LocusONE** (Locus Robotics) — robots-as-a-service fulfillment platform coordinating large AMR fleets and human associates as one workforce.
- **Formant** — vendor-agnostic cloud robot operations platform (observability, commands, missions, interventions, teleoperation) across robot classes.
- **Orbit** (Boston Dynamics) — fleet orchestration and intelligence software for inspection and case-handling robots, with multi-site enterprise views and maintenance-system integration.

## Sources

Research date: **2026-09-09**

- OTTO by Rockwell Automation — ottomotors.com (product pages) and docs.ottomotors.com (technical documentation portal: About Fleet Manager, Task states, Robot statuses and states, and the full documentation structure) — https://ottomotors.com/fleet-manager/ , https://docs.ottomotors.com/
- Seegrid — Fleet Central product page and FAQ — https://seegrid.com/fleet-central/
- Locus Robotics — LocusONE platform page — https://locusrobotics.com/locusone
- Formant — documentation hub (Fleet management, Intervention requests, Plan a mission, Commands, and the documentation index) — https://docs.formant.io/
- Boston Dynamics — Orbit product page — https://bostondynamics.com/products/orbit/

> Sourcing limitation: Mobile Industrial Robots (MiR Fleet), a major AMR-fleet anchor, could not be fetched (site returned no content on repeated attempts); no claims in this document rely on it. Seegrid, Locus, and Boston Dynamics evidence is product-page level; operational specifics (state vocabularies, exception mechanics, limits) are asserted only where Tier-1 documentation (OTTO, Formant) supports them. Detailed product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
