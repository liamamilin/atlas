# Factory Operations Management

## Overview

A **Factory Operations Management** application is the manufacturer's system for running production on the factory floor in real time. It holds the live operational picture of the factory — which machines, lines, and work centers are running, stopped, or down and why; what orders and runs are in progress on them and how they stand against plan — captures operational events where they happen, drives each event through a routed, standardized response to resolution, and keeps the operational performance record that management uses to steer and improve the operation.

It occupies the layer between enterprise planning and machine control. ERP and planning systems own the production plan, orders, bills of material, and inventory; SCADA, PLCs, and HMIs own the machines themselves. A factory operations system consumes the plan from the enterprise side and consumes signals from the machine side, then manages what actually happens on the floor between the two — pulling plans down, pushing actuals and statuses back up, and coordinating the people and functions (production, maintenance, quality, materials) whose responses keep production moving.

The market most often labels this category **manufacturing operations management (MOM)**, alongside related labels such as "connected manufacturing operations" or "frontline operations platform". The Type is realized in two dominant shapes: enterprise suites whose engine is a manufacturing execution system (MES), and composable or connected-operations platforms that manage the running operation without MES-grade enforcement. Both share the same defining core and differ mainly in how much of execution they enforce — a distinction treated in Variants and Related Application Types.

## Users & Context

The primary users are the people who run production, organized by line, shift, and site:

- **Operators / frontline workers** — execute work at stations and machines, follow work instructions, report abnormalities (downtime, quality problems, material shortages, safety issues), and record output and events as they happen. In many deployments they are the largest user population by far.
- **Supervisors / production leads** — run the shift: see live line status and progress against plan, prioritize the queue of issues and work, escalate what the floor cannot solve, and hand over cleanly between shifts.
- **Responding functions** — maintenance technicians (repair and keep equipment available), quality staff (checks, holds, dispositions), and materials/logistics staff (feeds and shortages). They receive routed events from the floor and resolve them inside the same system.
- **Operations / plant management** — consume the performance record (OEE, downtime, throughput, yield) per machine, line, shift, and site; run improvement work from it; and align operations with the plan.
- **Engineers / system builders** — configure machines and stations, connect machine data sources, define states, downtime reasons, checks, and response workflows. In app-based products, manufacturing engineers themselves build and iterate the frontline applications.

The work context is the factory floor itself: shared displays and boards at lines, tablets and touch screens at stations, and offices overlooking the floor. Shift rhythm structures everything — shift start priorities, in-shift capture and response, and per-shift performance review. Plants range from a single line to global multi-site operations, and deployments exist both with full machine connectivity and with purely manual, operator-entered data.

## Core Model

### The defining core

Three structures, jointly held. Remove any one and the product is no longer factory operations management — it becomes something adjacent.

```text
Enterprise plan (ERP / APS — owned upstream)
  │  orders, BOMs, schedules pulled down
  ▼
1. LIVE OPERATIONAL PICTURE
   machines / lines / work centers / stations
   + the work running on them (orders, runs, jobs, per shift)
   + current state: running / stopped / idle / changeover / down with coded reasons
  │  events surface from state changes
  ▼
2. EVENT-AND-RESPONSE LOOP
   downtime, quality problems, material shortages, safety, deviations
   → captured at the source (operator report and/or machine signal)
   → routed to the responsible function
   → standardized response → tracked to resolution
  │  everything accumulates
  ▼
3. OPERATIONAL PERFORMANCE RECORD
   per machine / line / shift / site:
   OEE, downtime, throughput, yield (current products)
   → reviewed and acted on → improvements fed back into execution
  │  actuals, statuses, results
  ▼
Enterprise systems (actuals pushed back up)
```

**1. The live operational picture.** The factory's production resources and the work running on them are held as managed objects whose current state is continuously maintained. Machines and work centers appear not as static asset records but as live things with operational states (running, stopped, idle, changeover, down), coded downtime reasons, and the production order or run currently on them, organized by line and shift. This is what the supervisor sees when they ask "where are we?" mid-shift. Without this leg, the product is a planning tool or an asset registry — nothing live to manage.

**2. The event-and-response loop.** Operational events — an unplanned stop, a quality fail, a material starvation, an incident, a deviation from plan — are captured at the source, either by the operator or automatically from machine signals, and driven through a response: routed to the responsible function, answered with a defined (often standardized) procedure, and tracked to resolution. An abnormality raised during production can become a maintenance work order; a quality fail can escalate to supervision. The loop is closed — the event, the response, and the outcome live in one record. Without this leg, the product is a passive monitoring dashboard; the management is gone.

**3. The operational performance record.** The live state and the events accumulate into measures of operational performance — OEE, downtime, throughput, yield — computed per machine, line, shift, and site, and retained over time. This record is the object of daily management and continuous improvement: review, root-cause the losses, standardize what worked, feed the change back into execution. Without this leg, the product is an alerting or andon tool with nothing to manage by.

The three legs are inseparable in practice: a live picture without response is spectator tooling; a response loop without a performance record cannot improve anything; a performance record without live state has no real-time substance behind it.

### Standard capabilities of mature products

These capabilities are widespread in the category but do not define it — older and thinner deployments remain members of the Type without them:

- **Machine data connectivity** — edge gateways and industrial protocols (OPC UA, MQTT and peers) feeding states, counts, and process values automatically; the alternative path, operator entry, is a fully supported mode in parts of the market.
- **Work instructions, SOPs, and digital checklists** delivered to the operator at the point of work, often with photos, videos, and multi-language content.
- **Quality checks at the source** — inspection checklists, first-part checks, in-process captures — recorded against the order or run.
- **Alerting and escalation rules** — notifications, routing trees, and automatic triggers (for example, a machine alert creating a maintenance task).
- **Live dashboards and boards** — andon-style line boards, shift-priority queues, wall displays.
- **Root cause analysis and corrective action** — structured problem-solving on the recorded losses, feeding standard-work changes.
- **ERP integration** — order release and status/actuals exchange in both directions.
- **Skills and qualification checks** — ensuring only qualified personnel perform given work.
- **Shift and schedule management** — shifts, calendars, staffing counts.
- **Multi-site rollup** — benchmarking lines and plants against each other.
- **Governed records for regulated manufacturing** — electronic records, signatures, and review where compliance regimes require them.
- **AI assistance** — pattern detection and prescriptive suggestions on operational data; era-current and optional.

### One structure, many implementations

```text
Concept:  live operational picture
Implementations:  machine connections (OPC UA/MQTT/edge gateways), operator-entry
                  capture, or both; "machines", "assets", "stations", "work centers"

Concept:  the work on the resources
Implementations:  work orders pulled from ERP/MES, production runs defined in-system,
                  shift targets; order master data owned upstream, execution context local

Concept:  the event
Implementations:  operator-reported abnormality, machine-signal downtime,
                  failed check, missed target; coded reason lists (plant-customized)

Concept:  the response
Implementations:  dispatch queues with assignees, auto-created maintenance work
                  orders, escalation paths, guided SOP/checklist procedures

Concept:  the performance record
Implementations:  OEE and loss calculations from machine states, throughput and
                  yield tallies from operator or machine counts, reported dashboards
```

## How It Works

### The standing loop (daily operation)

```text
Shift start
→ priorities and targets for the shift are clear (from plan + standing issues)
→ production runs under the live picture (states, counts, progress)
→ events surface (machine signals and/or operator reports)
→ events route to the right function and get worked to resolution
→ actuals and statuses flow back to enterprise systems
→ shift review against the performance record
→ losses become improvement work → standard work changes → next shift
```

### Acquire the operational picture

Setup establishes the factory in the system: machines, lines, work centers, and stations are defined; machine data sources are connected where connectivity exists (industrial protocols via edge software) and states and downtime reasons are configured; shifts and organizational structures are set; the connection to the enterprise layer is established so released orders and schedules flow down. Where machines are not connected, the same picture is maintained by operator entry — the loop still works, just measured more coarsely.

### Capture events at the source

During production, the live picture updates continuously from machine signals (state changes, counts, process values) and from people (operator reports of stops, defects, shortages, incidents). Each event carries context: which resource, which order or run, which shift, and a coded reason. Reason coding is the discipline that makes the record analyzable later; products commonly ship default reason lists (changeover, maintenance, material, operator-related categories) that plants typically customize to their own failure vocabulary.

### Route and resolve

An event triggers the response machinery: routing rules send it to the responsible function — maintenance for equipment faults, quality for defects, materials for starvation, supervision for the rest. The responder gets the context they need (what broke, where, since when) and works through a defined procedure — a repair, a check, a replenishment — with the event tracked from raised to resolved. Timeliness is itself measured: response and resolution times are part of the record. Events can chain: a stop can spawn a maintenance task, which on completion returns the resource to running state; a quality fail can hold the line pending disposition.

### Measure and improve

State time and events roll into the performance record: availability losses from downtime, performance losses from slow running, quality losses from defects — combined in current products into OEE per machine and line, alongside throughput, yield, and response metrics, per shift and site. Supervisors and managers review the record (live boards during the shift, reports and dashboards across shifts and sites), run structured problem-solving on the biggest losses, and convert findings into standard work, new checks, or equipment changes — which then change what the next shift's record looks like.

### Exchange with the enterprise layer

The system pulls released orders, schedules, and item data from the enterprise layer and pushes actuals, statuses, and results back — quantities produced, time consumed, deviations raised. The division of ownership is a deliberate design point in this category: the plan, the orders, the bills of material, and inventory of record belong to the ERP/planning side; the operational context of executing them — the running state, the events, the responses, the performance of the floor — belongs here. Products that also enforce execution (routing, electronic records, traceability) extend into MES territory; products that do not, integrate with an MES or ERP for those pieces.

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Operator station surface

The frontline's main surface, running at the machine or workstation.

- work instructions and checklists for the current step; entry forms for counts, measurements, and inspections; one-touch abnormality reporting (what, why) with reason coding; machine state and alerts where connected
- primary actions: start/complete steps, record output, report an issue, call for help

### Live floor / shift board

The supervisor's real-time picture of a line, area, or site.

- resources with current states and current orders/runs; progress against shift target; open events and their age/owner; live run rates
- primary actions: prioritize and assign events, escalate, adjust the running schedule, annotate the shift

### Response queues

The responder's work surface (maintenance, quality, materials).

- events and tasks routed to the function, with asset/order context and history; status from raised to resolved
- primary actions: accept, work the procedure, record the fix/outcome, close

### Performance dashboards and reports

The management layer over the record.

- OEE and loss breakdowns, downtime pareto, throughput and yield trends by machine/line/shift/site; comparison across sites
- primary actions: drill into losses, export, launch improvement items

### Configuration and system-building surface

Where engineers shape the system.

- machine/station/line definitions, machine data connections, states and downtime reasons, reason lists, routing and escalation rules, instruction and checklist authoring, user roles and permissions, enterprise integrations
- in app-based products this extends to a no-code editor for building and versioning the frontline applications themselves

### Enterprise integration surface

The machine-to-business boundary.

- order/schedule/item data inbound from ERP or MES; actuals, statuses, and event summaries outbound; sometimes a direct line to scheduling to reflect floor reality

## Important Rules / Behaviors

### State is the primary fact

The system's fundamental assertion is a resource's current state, with coded reasons for non-running time. Disagreement between what machines report and what people report is a real phenomenon; mature deployments treat reason coding as a governed data discipline (standardized lists, review of "other"), because every downstream measure inherits it.

### The plan is consumed, not owned

Orders, schedules, bills of material, and inventory of record live in the enterprise layer. This system adapts execution to the plan and reports back; where it reschedules, it does so at execution grain (line, shift, order sequence) against floor reality — strategic planning stays upstream. Products vary in how much scheduling they take on, but none replaces the ERP as the plan's home in the market's own accounting of these systems.

### Response is routed, structured, and measured

Events do not resolve informally: they are assigned, worked through defined procedures, and closed with an outcome. Cross-function chaining is common — one event producing tasks in multiple functions — and response/resolution time is itself a managed metric. This is the behavioral difference between an operations platform and a notification system.

### Capture must not depend on perfection

Deployments run the same loop with full machine connectivity, partial connectivity, or none (operator entry only). Graceful behavior under missing data — and honest distinction between measured and entered values — is part of the operating model, not an edge case.

### Skill and compliance gating in managed environments

Work may be restricted to qualified personnel, and in regulated industries the record may require electronic signatures and controlled review. Where present, these constraints bind the response loop and the record, not just the UI.

### Improvement closes the loop

The record exists to be acted on: recurring losses become structured problem-solving, and the outcome (changed standard work, new checks, fixed equipment) changes future behavior. An operations system that only measures, without feeding change back into execution, is missing the loop that defines the Type.

## Variants

- **Enterprise MOM suite (MES at the core)** — full production execution enforcement: routing, electronic batch/device records, forward and backward traceability, resource and material control, plus quality, planning, and intelligence modules around the execution engine. Typical in large, regulated, or high-complexity manufacturers; on-premise or cloud.
- **Composable frontline operations platform** — the operator-experience-first shape: no-code apps at stations, connected machines, captured data, and analytics, integrating to ERP/MES rather than replacing them. Typical where lean/continuous-improvement programs drive adoption plant by plant.
- **Connected operations platform** — the response-loop-first shape: dispatch and abnormality management at the center, with production monitoring, maintenance, and skills around it; positioned as replacing a simple MES or coexisting with a full one in regulated plants.
- **Machine-data-first platform** — connectivity-first shape: automatic machine data collection and OEE/production monitoring as the wedge, extending toward job tracking, scheduling, and maintenance triggers. Typical in discrete machining environments.
- **By industry** — discrete assembly/machining versus process/batch (food, chemicals, pharma) packaging changes the objects emphasized (runs and batches versus jobs and routings) without changing the core loop.
- **By connectivity posture** — fully connected (automatic states/OEE) versus operator-entry (manual capture) versus hybrid; by deployment: cloud SaaS versus on-premise; by scale: single line/plant versus global multi-site rollup.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Manufacturing Execution System / MES | overlapping sibling; bundled in suites, integrated elsewhere | MES centers on enforcing order execution against defined routings and producing the as-built record (traceability, genealogy, e-records); factory operations management centers on the live management of the running operation. Remove the live operations management and enforcement remains = MES; remove enforcement and the operations loop remains = this Type |
| Shop Floor Management | adjacent sibling | centers on the floor's daily management system (issues, visual management, escalation); this Type adds the production-operations record and live order/resource state as defining increments |
| OEE Management Platform | downstream sibling | centers on equipment effectiveness measurement and loss analytics; here OEE is one output of the performance record, with the event-and-response loop as the part OEE platforms lack |
| Production Planning / APS | upstream | owns the forward plan and schedule; this Type consumes the plan and adapts execution to floor reality |
| SCADA / HMI / DCS | below (control layer) | supervises and controls machines and collects raw data; this Type manages operations above the control layer and consumes its signals |
| Industrial IoT Platform | substrate | provides connectivity and data infrastructure; this Type is an operations consumer of that substrate |
| CMMS / EAM | adjacent | keeps asset care and maintenance work management; here maintenance appears as one response class in the operations loop (suite products bundle CMMS modules) |
| Manufacturing QMS / CAPA Management | adjacent | keeps formal quality records and corrective-action systems; here quality appears as events and checks feeding the response loop |
| Manufacturing Traceability | downstream record | keeps the as-built genealogy record; in suites it is produced by the execution engine |
| Manufacturing ERP | upstream system of record | owns the business plan, orders, materials, and costing; this Type handles the "last mile" of executing that plan on the floor |

## Representative Products

- Siemens Opcenter — unified manufacturing operations management portfolio (execution, quality, planning, intelligence)
- Tulip — composable no-code frontline operations platform
- L2L — connected manufacturing operations platform (dispatch/abnormality-centered)
- MachineMetrics — machine-data-centric production monitoring and job tracking platform

These four span the Type's main product shapes and customer tiers, from enterprise suites to plant-level frontline platforms.

## Sources

Research date: **2026-09-08**

- Siemens — Opcenter (MOM portfolio): https://www.siemens.com/en-us/products/opcenter/
- Siemens — Manufacturing execution system software: https://www.siemens.com/en-us/solutions/manufacturing-execution-system-mes/
- Siemens — Opcenter Execution: https://www.siemens.com/en-us/products/opcenter/execution/
- Tulip — Knowledge Base (What is Tulip; Shop floor management; A Tour of the shop floor; Machine attributes, downtime reasons, and states; Plan an integration between Tulip and an MES or ERP): https://support.tulip.co/
- L2L — Connected Manufacturing Operations Platform (home, platform, shop floor execution, production management): https://www.l2l.com/
- MachineMetrics — Intelligent MES and machine monitoring (homepage): https://www.machinemetrics.com/

> Sourcing limitations: official documentation for two additional candidates in this category (GE Vernova Proficy Plant Applications; 42Q) could not be retrieved during research, so the enterprise-suite pole rests on a single deeply documented sample and assertions were calibrated accordingly. No independent industry-standards text was consulted; the positioning between planning and control layers reflects vendor-stated framing that is consistent across the sampled products. Numeric performance claims in vendor marketing were excluded. Detailed observations and boundaries are recorded in the paired Research Notes.
