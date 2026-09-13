# Manufacturing Execution System / MES

## Overview

A **Manufacturing Execution System (MES)** is the manufacturer's execution layer between business systems and machines: it takes released production orders and runs them on the shop floor operation by operation against a defined process, and it produces the as-built record of what was actually made — per serialized unit or lot, with the materials consumed, the resources used, the people involved, and the quality results observed.

The defining structure is small:

```text
Business systems (ERP / planning — own orders, bills of material, inventory)
  │  released orders + product/process definitions flow down
  ▼
1. THE EXECUTED PRODUCTION ORDER — the unit of work, advanced at operation/step grain
  │  execution is bound to
2. THE DEFINED PROCESS — routings/recipes, work instructions, in-line quality gates
  │  execution accumulates
3. THE AS-BUILT RECORD — per unit/lot: materials, resources, people, results, genealogy
  ▼
Permanent production history → traceability, regulated batch/device records
```

Three properties. If any one is removed, the product is no longer recognizable as an MES:

- **The executed production order** — the MES does not merely plan or track orders; it manages their execution on the floor: dispatching them to lines, work centers, and machines, advancing steps, assigning resources, and completing them. Without this, it is a planning tool or a dispatch board.
- **Execution bound to the defined process** — what the floor does is held against a definition of how the product is made. Without this, it is generic job tracking.
- **The as-built record at unit/lot grain** — the system accumulates a lasting, evidence-grade production history. Without this, it is production monitoring or reporting with nothing of record.

Everything commonly associated with MES in the market — machine connectivity, OEE dashboards, scheduling, quality modules, electronic signatures, cloud delivery, AI insights — is widespread in current products but is standard or optional capability layered on this core. The definition also fits the pre-digital practice it digitized: a paper job packet moving with the order (router sheet, operation sign-offs, lot and inspection stamps) carries the same three structures with no software at all.

## Users & Context

The system's user population mirrors the factory's execution hierarchy:

Primary users:

- **Operators / machine attendants** — execute the steps of the order at their station or machine: confirm steps, follow instructions, record counts and measurements, log consumption of materials, and flag problems. In most deployments they are the largest user population.
- **Line / area supervisors** — own the queue of orders in execution: release them to the floor, dispatch and sequence them across work centers, respond to what blocks a step, and hand the shift over with the record in order.
- **Quality staff** — run in-line inspections, sample plans, and statistical checks inside the flow of execution; hold material that fails and disposition it (rework, scrap, accept).

Secondary users:

- **Production / manufacturing engineers** — maintain the process definitions the system executes: routings and recipes, parameters, work instructions, and quality specifications. Their masters govern what the floor is allowed to do.
- **Plant and operations management** — consume the performance picture derived from the execution record: output, yield, downtime, and schedule adherence.
- **IT / system integrators** — operate the integration machinery that moves orders and results between the MES and ERP, and connects machine data sources.

The work context is the factory floor: terminals and screens at stations, kiosks and tablets at the point of work, and engineering and management surfaces off the floor. The rhythm is the order's rhythm — release, execute, record, complete — nested inside shifts and production schedules. Factories range from single plants to global multi-site networks; in regulated industries (pharmaceuticals, medical devices), the record the MES produces is a compliance artifact, which raises the stakes of everything above.

## Core Model

### The Defining Core

The MES's world is organized around one mechanism: **an order is executed against a definition, and everything that happens becomes a permanent record of what was built.**

**1. The executed production order.** The production order (work order, manufacturing order, batch order) is the unit of executed work. It enters the MES in a released state — the planning decision of what to make and roughly when has already been made upstream — and the MES manages its floor life: which work centers and machines it runs on, which operations or steps are done in what sequence, which operators and materials are assigned, how far it has progressed, and when it is complete. Execution is tracked at operation and step grain, not merely at the order's aggregate: the difference between "order 1234 is running" and "order 1234 has completed steps 10–40 at work center 5, step 50 is in progress, two units are done and one is on hold."

**2. The defined process.** The order does not execute in a vacuum; it executes against a held definition of how the product is made. In discrete manufacturing this is the routing or process plan — operations, parameters, and instructions; in process industries, the recipe or master recipe; the vocabulary varies, the structure does not. The definition carries the work instructions shown to operators and the in-line quality checks (measurements, sample plans, statistical limits) that must be satisfied as the product moves through steps. The depth of binding varies by industry and deployment: at the shallow end the definition guides (the operator sees the next step); at the deep end it enforces (out-of-sequence steps are blocked, failed checks hold the unit, unapproved recipe versions cannot run, materials are issued against the bill of material). Regulated industries sit at the enforced end; a job shop may sit at the guided end. The binding itself — that execution answers to a definition — is constant across the Type.

**3. The as-built record.** As execution proceeds, the MES accumulates the as-built record: for each serialized unit or identified lot, which materials and material lots were consumed, on which equipment, by whom, when, with which measured values and inspection results, and against which definition version. This record is retained as the permanent production history. From it, the system can answer the questions that ordinary production reporting cannot: which end products contain material from lot X? Which equipment and operators touched unit Y? Which definition version was in force when unit Z was built? In regulated industries the same record takes the form of the electronic batch record or electronic device history record — the documentation that the product was made the way its process said it must be. Forward and backward traceability (material → units, unit → materials) is produced from this record, not bolted on.

The three legs are inseparable in practice: an order executed without a process definition has no standard to enforce; a definition without executed orders documents nothing; execution and definition without the record leave no evidence that anything happened.

### Standard Capabilities of Mature Products

These are widespread in the category but do not define it — thinner and older deployments remain members of the Type without them:

- **Machine and equipment connectivity** — collecting states, counts, and process values automatically from PLCs, SCADA systems, and industrial protocols, so the record fills itself where automation exists; operator entry remains a fully supported path where it does not.
- **Resource management** — tracking equipment usage and states, gating work on operator qualifications and certifications, and managing material movement and storage within and between work centers, including plant-level inventory visibility.
- **In-line quality execution** — sample plans, statistical process control, and holds/dispositions inside the flow of execution, feeding the plant's formal quality system.
- **Performance analysis** — output, yield, downtime, and OEE-class measures computed from the execution record, per machine, line, shift, and site.
- **Paperless operator work** — work instructions, SOPs, and checklists delivered at the point of work, replacing paper travelers and binders.
- **ERP integration machinery** — automated exchange of orders, definitions, and results with business systems in both directions.
- **Execution-grain sequencing** — optimizing the order of dispatched work within the day's released orders (full forward planning remains upstream).
- **Multi-site standardization** — templated or model-driven rollouts of the same execution model across plants, with rollup reporting.
- **Governed records** — electronic signatures, audit trails, and controlled review where the record serves compliance.
- **Analytics and AI overlays** — dashboards, historical comparison, and increasingly AI-generated insights on execution data.

### One Structure, Many Implementations

The core is written conceptually; products realize it in different vocabularies:

```text
Concept:   the executed order
Realized:  work order, manufacturing order, batch order, job;
           operations, steps, phases

Concept:   the defined process
Realized:  routing / process plan (discrete), recipe or master recipe
           (process industries), op sheets, eSOPs, control plans

Concept:   the as-built unit
Realized:  serialized unit (discrete/electronics), lot or batch
           (process/consumer goods), genealogy tree, batch record,
           device history record

Concept:   enforcement depth
Realized:  advisory guidance → guided steps → blocking enforcement
           (holds, sequence checks, recipe/BOM enforcement, e-signatures)
```

A reader who has seen only one industry flavor should still recognize the others: a pharma batch record, an electronics unit genealogy, and a machining shop's job tracker differ in packaging, not in the underlying triple.

## How It Works

### Release and dispatch

```text
ERP/planning releases orders (+ product definitions in force)
→ MES receives the order against the process definition
→ supervisor/engineer dispatches it to lines, work centers, machines
→ sequence optimized within the released set
→ materials staged and issued against the order
```

### Execute, guided by the definition

```text
Operator (or machine) starts the step
→ instruction and parameters shown at the point of work
→ machine data and/or operator entries fill the record as the step runs
→ in-line quality checks execute where the definition requires them
→ pass → next step; fail → unit/lot held for disposition
→ out-of-sequence or non-compliant actions prevented where enforcement is deep
```

### Complete and report back

```text
Final step completes
→ unit/lot status set; order quantities confirmed
→ results (output, yield, time, consumption, deviations) pushed to ERP
→ order closed as a permanent record
```

### Interrogate the record

```text
Traceability event (customer complaint, defect, recall, audit)
→ query the as-built record: which units contain lot X / what touched unit Y
→ forward and backward genealogy across the affected population
→ regulated deployments: the batch/device record is the compliance artifact
```

### Capability tiers

**Defining core** — without these, not an MES:

- order execution at operation/step grain with resource assignment
- execution bound to a held process definition (guidance at minimum; enforcement in depth)
- as-built record at unit/lot grain with materials, resources, people, results

**Standard capabilities** — present in most mature products:

- machine connectivity and automatic data collection; resource and material management; in-line quality execution; performance/OEE analysis; paperless instructions; ERP integration machinery; execution-grain sequencing; multi-site standardization; governed records

**Common variants / optional** — depend on industry, scale, and deployment:

- industry packaging (batch records for pharma, unit genealogy for electronics, recipe enforcement for consumer goods)
- enforcement depth (guided vs blocking)
- deployment shape (on-premise, cloud, hybrid; monolithic suite vs composable modules)
- scheduling depth beyond dispatch; maintenance or logistics modules bundled by suite vendors; AI overlays

## Interfaces

Surfaces are described conceptually; names and layouts vary by product.

### Operator terminal / point-of-work surface

The frontline's main surface at the machine or station.

- current order and step, work instructions and parameters, entry forms for counts/measurements, quality check prompts, material scan/issue prompts
- primary actions: start/complete step, record data, flag a problem, request material

### Order and floor tracking surface

The supervisor's picture of execution.

- orders in progress by line/work center with step-level status, queued and released work, holds and exceptions, resource assignments
- primary actions: dispatch, re-sequence, reassign, place/release holds, annotate the record

### Quality execution surface

Where in-line quality lives.

- sample plans and checklists due on the current work, statistical charts, failed checks with disposition paths
- primary actions: record results, hold/release material, disposition, escalate

### Traceability / genealogy surface

The record's investigative surface.

- unit/lot detail view (what was consumed, by whom, on what, when), forward/backward genealogy queries, batch/device record assembly
- primary actions: run a traceability query, export the record, review and sign (regulated deployments)

### Performance dashboards

The management layer over the execution record.

- output, yield, downtime, OEE-class measures by machine/line/shift/site; comparison of actual vs expected
- primary actions: drill into deviations, export, compare sites

### Engineering / configuration surface

Where the executable definition is maintained.

- routings/recipes with versions and approval states, work instructions, quality specifications, work center/machine definitions, integration configuration
- primary actions: define and version the process model, manage templates, configure integrations

### Integration surfaces

The machine-to-business boundary.

- order/definition inbound from ERP; results and actuals outbound; machine data inbound from PLC/SCADA layers; reconciliation tooling for failed exchanges

## Important Rules / Behaviors

### The plan is consumed, not owned

Orders, bills of material, and inventory of record belong to the business layer. The MES adapts execution to the released plan and reports results back; where it optimizes, it does so within the released set (sequencing and dispatch), not by re-planning the business. Vendors across the sample state this split in their own words, and adjacent platforms (which integrate *with* an MES precisely because they do not own orders) confirm it from the outside.

### The definition in force governs execution

Execution answers to the process definition — and to the version of it in force when the work runs. Mature products version and approve routings/recipes so that a past unit can always be interpreted against the definition it was made under. Changing the definition changes future execution, not the standing record.

### Enforcement depth is the regulated dividing line

The same structure runs advisory in a job shop and blocking in a regulated plant. Where the record is a compliance artifact, the system prevents non-compliant execution outright: out-of-sequence steps, unapproved recipe versions, unqualified operators, and failed checks do not pass silently — they block, hold, or require a recorded, signed exception.

### The record is evidence, not a log

The as-built record is append-oriented and, in regulated deployments, signature- and audit-trail-bound. It must remain interpretable years later — which is why unit/lot grain, definition versions, and resource attribution are structural rather than reporting conveniences.

### Quality stops the unit, not the record

A failed check or a hold does not erase work done; it changes the unit's disposition path while the record continues to accumulate. Quality execution feeds the formal quality system, but the in-line check, the hold, and the disposition remain part of the production history.

### Dual capture is normal

The record fills from machines where automation exists and from operator entry where it does not. Mature deployments are honest about the provenance of each value — measured vs entered — because every downstream measure inherits it.

## Variants

- **By industry packaging** — discrete/complex assembly (operations, serial units), electronics/PCB (unit genealogy across high-volume lines), process and consumer goods (batches, recipes, lots), pharmaceuticals (electronic batch records), medical devices (electronic device history records), semiconductors (lot-centric wafer execution). Packaging changes vocabulary and emphasis more than structure.
- **By enforcement depth** — guided execution for flexible/less-regulated environments; blocking enforcement where compliance or process discipline demands it. This is the Type's main segmentation axis.
- **By portfolio context** — standalone MES products vs MES as the execution engine inside a broader manufacturing-operations suite (with quality, planning, intelligence, and logistics siblings sold around it).
- **By deployment** — on-premise (traditional), cloud SaaS (mid-market), and hybrid shapes that keep mission-critical execution on plant premises while rolling up multi-site data to the cloud.
- **By scale and tier** — global multi-site enterprises standardizing one execution model across plants, down to single-plant deployments; packaging style ranges from monolithic suites to composable, modular deployments assembled from use-case libraries.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Manufacturing ERP | upstream system of record | ERP owns the business-grain record: orders, bills of material, inventory, costing; its shop-floor recording is aggregate confirmation. MES owns execution grain and the unit/lot as-built record. Remove the execution enforcement and as-built evidence from MES and what remains is ERP shop-floor recording |
| Production Planning / APS | upstream | planning decides what and when at schedule grain; MES executes released orders and optimizes only within execution (sequencing/dispatch). Suite vendors sell APS as a separate product beside MES |
| Factory Operations Management / MOM | overlapping sibling; bundled in suites | MES centers on enforcing order execution against the defined process and producing the as-built record; factory operations management centers on the live operational picture, the event-and-response loop, and the operational performance record. Remove live operations management and enforcement + record remain = MES; remove enforcement + record and the live loop remains = that Type. In suites the MES is the engine inside the MOM portfolio |
| Shop Floor Management | adjacent sibling | centers on the floor's daily management system (issues, andon, visual management); no unit genealogy or process enforcement at its core |
| SCADA / HMI | below (control layer) | supervises and controls machines and processes in real time without order/lot context; the distinction is drawn explicitly in vendor documentation across the sample. Remove the order and the definition → control-layer territory |
| Industrial Historian | data substrate below | stores time-series process tags; the unit-bound as-built record with genealogy is the MES increment. The historian is commonly a data source the MES consumes |
| Manufacturing Traceability | downstream record | genealogy is one leg of MES; standalone traceability systems keep and query the record without executing production. In suites, the record is produced by the execution engine |
| Manufacturing QMS / CAPA Management | adjacent | the quality system of record (audits, documents, CAPA, complaints) vs the MES's in-line quality execution feeding it |
| OEE Management Platform | downstream analytics | equipment-effectiveness measurement and loss analytics; OEE appears in essentially every MES sample but as a derived view — removing it leaves the MES intact |
| Industrial IoT Platform | substrate | connectivity and device-data infrastructure; the MES is a consumer of that substrate, not the substrate itself |

## Representative Products

- Siemens Opcenter Execution — industry-packaged MES family (discrete, process, electronics, medical device, pharma, semiconductor) inside the Opcenter manufacturing-operations portfolio
- AVEVA Manufacturing Execution System — model-driven, composable MES for batch and repetitive production, spanning on-premise and hybrid-cloud deployment

The boundary was sharpened against adjacent platforms that explicitly position themselves relative to MES — Tulip (frontline operations apps integrating to MES/ERP), L2L (connected operations platform deployed alongside ISA-95-grade MES in regulated plants), and MachineMetrics (machine-data platform labeled "MES" in its marketing) — and against the pre-digital paper-traveler practice, to keep the definition from over-fitting to any one era or vendor pattern.

## Sources

Research date: **2026-09-09**

- Siemens — Opcenter Execution (MES family): https://www.siemens.com/en-us/products/opcenter/execution/
- AVEVA — Manufacturing Execution System (product page and official FAQ, incl. MES vs ERP vs HMI/SCADA): https://www.aveva.com/en/products/manufacturing-execution-system/
- Tulip — Plan an integration between Tulip and an MES or ERP: https://support.tulip.co/docs/plan-an-integration-between-tulip-and-an-mes-or-erp
- Supporting context fetched 2026-09-08 for the adjacent Factory Operations Management leaf: Siemens Opcenter portfolio and MES solution pages; Tulip knowledge base; L2L platform and FAQ pages; MachineMetrics homepage (recorded in that leaf's research notes)

> Sourcing limitations: official documentation for several additional MES candidates (iBase-t, 42Q, Plex, Körber PAS-X, DELMIA Apriso) could not be retrieved during research, so the enterprise-suite and regulated-specialist poles rest on fewer samples than the market contains, and assertions were calibrated accordingly. No independent industry-standards text (ISA-95 or its predecessors) was accessible; the positioning between business planning and machine control reflects vendor-stated framing that is consistent across the sampled vendors, not a verified standard. Numeric performance claims in vendor marketing were excluded. Detailed observations and boundaries are recorded in the paired Research Notes.
