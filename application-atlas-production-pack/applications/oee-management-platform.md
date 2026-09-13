# OEE Management Platform

## Overview

An **OEE Management Platform** is a manufacturer's system for measuring and managing the effectiveness of its production equipment. It tracks how much of the planned production time on a machine, line, or cell actually produced good output at the intended speed, breaks the gap down into attributed losses, and manages improvement against that measure over time.

The name comes from **Overall Equipment Effectiveness (OEE)** — a lean/TPM practice for quantifying production loss. The defining structure is small:

```text
Measured production unit (machine / line / cell / station)
└── Time-and-output accounting
    │   (planned production time · stopped time · output vs reference rate · good vs total output)
    └── Effectiveness score (OEE — Availability × Performance × Quality, or a documented subset)
        └── Loss attribution (coded reasons, component breakdown, Pareto)
            └── Effectiveness management (targets, trends, review rhythm, verified improvement)
```

Everything else commonly associated with these products — automatic machine connectivity, real-time shop-floor displays, alerts, AI summaries, ERP integration — is widespread in current products but is not what makes the product an OEE platform. The paper-and-spreadsheet OEE practice that predates all of them satisfies the same core.

When the center of gravity shifts to dispatching people to fix live problems, the product is drifting toward Factory Operations Management; when it shifts to enforcing work orders and recording as-built history, toward MES; when it only collects machine signals, toward machine monitoring and Industrial IoT.

## Users & Context

Primary users:

- **production / plant management** — owns the effectiveness score: sets targets, reviews trends, runs the daily and weekly performance meetings on the platform's data
- **continuous-improvement staff** — uses loss attribution to find the biggest losses, runs structured improvement projects, and verifies results with before/after comparisons on the same measure
- **operators** — record the reasons for stops on shop-floor devices and work to the live numbers displayed beside their machines

Secondary consumers:

- **maintenance** — receives downtime patterns and recurring-failure evidence that inform maintenance priorities
- **planners and finance** — use utilization and loss data for scheduling, costing, and investment cases (several products address these roles explicitly)

The work environment spans two surfaces: the **shop floor** (displays, tablets, and wall boards showing live status and collecting reason entries) and the **office** (dashboards, reports, and trend analysis used in the daily/weekly meeting rhythm). Typical context is a factory running in shifts; the shift is the natural unit around which live views and comparisons are organized.

## Core Model

### The measured production unit

The system's subject is a defined unit of production equipment — a machine, line, cell, or station — organized in a hierarchy up to factory and multi-site level. Every measurement, loss, and trend belongs to a specific unit at a specific grain; the same data rolls up (machine → line → factory → enterprise) and slices down (month → day → shift → hour).

### The time-and-output accounting model

This is the heart of the Type. For each measured unit the system maintains:

- **Planned production time** — the denominator. Scheduled shift time minus what the factory explicitly excludes (major maintenance shutdowns, demand-idled periods). What counts as "planned" is a configuration decision with real consequences: excluding too much hides losses.
- **Stopped / lost time** — when the unit was scheduled to produce but did not, coded by reason.
- **Output against a reference rate** — what was produced while running, compared with what the unit could have produced at its reference speed (an ideal cycle time, a maximum demonstrated rate, or a benchmark derived from the best observed performance).
- **Good vs total output** — how much of production was right the first time.

### The effectiveness score

These inputs compute an effectiveness score. The canonical decomposition is:

```text
OEE = Availability × Performance × Quality

Availability = run time / planned production time
Performance  = actual output / maximum possible output at the reference rate
Quality      = good parts / total parts
```

The full three-component formula is the dominant implementation, but not a requirement: a product can ship only Availability and Quality — or Availability alone — and remain squarely an OEE platform. What is constant is the accounting structure itself: planned time, losses against it, output against a reference, and quality of that output.

### Loss attribution

A score alone cannot drive action, so the system decomposes it into attributed losses:

- a **configured reason taxonomy** for stops (machine fault, tool broken, setup, unplanned maintenance, material shortage, changeover, and similar — each factory configures its own list)
- **component breakdown** — which of availability, performance, or quality absorbed the loss
- **loss categories** in the lean tradition (the "Six Big Losses": unplanned stops, planned stops, micro stops, slow cycles, production rejects, start-up rejects)
- **Pareto views** ranking reasons by lost time or lost output, so improvement effort lands on the biggest losses

### Targets and the improvement record

The measure is managed, not just displayed:

- **targets or benchmarks** — what "good" means for this factory, this line, this shift
- **trends over time** — the score and its components tracked across shifts, days, and months, compared against previous periods and against target
- **the review rhythm** — daily and weekly meetings, tier reviews, and kaizen events run on the platform's data
- **improvement verification** — before/after comparison against the same measure, closing the loop on each intervention

### One structure, many implementations

```text
Concept:            Reference rate for "full speed"
Implementations:    ideal cycle time · maximum demonstrated rate · nameplate speed ·
                    fastest recorded shift as benchmark

Concept:            Loss capture
Implementations:    automatic machine signals · operator reason entry · hybrid

Concept:            Effectiveness score
Implementations:    full A×P×Q · Availability + Quality · Availability-focused utilization
```

## How It Works

### Configure the measurement model

Before data flows, the system is configured to match the process: which units are measured and how they nest; what signals represent production (pieces, meters, liters, time); shift times and calendars (which define planned production time); products and their reference rates; the loss-reason taxonomy; and who the operators are. This configuration is what makes later numbers comparable — and misconfiguring it is the classic failure mode (see Rules).

### Capture what happened

```text
Machine signals (sensor / PLC / edge connection)  →  states and counts, automatically
Operator, at the shop-floor device                →  reason codes for stops
```

Automatic collection is the dominant posture — sensors detect products, edge devices read machine controls, and states and counts arrive without operator input. But it is not the only posture: operators log stop reasons on tablets or touch panels in most deployments (automatic signals rarely know *why* a machine stopped), and some products support operator-entry-only or integration-only setups for factories that cannot or will not add hardware.

### Compute and display

The system continuously computes the score and its components per unit and displays them live: shift views tracking the running shift, factory overviews showing every machine's status at a glance, and dashboards on shop-floor TVs, tablets, and office screens. Color-coded status makes abnormal units findable in seconds; the current shift's OEE, downtime, and speed loss are visible while there is still time to act on them.

### Analyze the losses

Beyond the live view, analysis surfaces answer "where is effectiveness being lost, and why": downtime Paretos ranking reasons, trend lines across shifts and months, comparisons between machines, shifts, products, and sites, and per-run reports measuring each production run against historical performance.

### Manage the improvement loop

```text
Set target / benchmark
→ review losses on the meeting rhythm (daily huddle · weekly review · tier meeting)
→ select and run an improvement action
→ verify against the same measure (before/after on OEE or its components)
→ sustain or repeat
```

This loop is what separates an OEE *management* platform from an OEE *report*: the measure exists to be moved. Products support it with target-vs-actual analysis, initiative tracking, and shared visibility that keeps improvement embedded in daily routines rather than one-off projects.

## Interfaces

### Shift view / live production view

The shop-floor's primary surface.

- shows the current shift's performance per machine or line, in real time
- typical information: current OEE or availability, output vs plan, current state, running loss reasons
- primary actions: read status at a glance, drill into a machine, record a stop reason

### Operator reason-entry surface

Tablet or touch panel at the machine.

- appears when a stop occurs; the operator selects (or enters) the reason
- primary actions: log reason, confirm restart; feeds the loss attribution that everything else depends on

### Dashboards

Configurable widget surfaces for offices, meeting rooms, and wall-mounted TVs.

- typical widgets: OEE, downtime, speed loss, scrap, checklists, trend lines, target comparison
- primary actions: filter by factory/unit/time period/reason, compare periods, share; often auto-rotating for always-on displays

### Analysis and reports

The office-side surface for loss analysis.

- typical information: downtime Pareto by reason, OEE and component trends, utilization by hour/shift/day/month, per-run and per-operator performance vs historical
- primary actions: slice by unit/period/reason/product, export, build the meeting agenda from the biggest losses

### Administration / configuration

Where the measurement model is defined.

- typical settings: equipment hierarchy, shift calendars, products and reference rates, loss-reason taxonomy, users and roles, targets
- primary actions: configure, adjust exclusions from planned time, maintain reason lists

### Alerts

Notifications when performance needs attention.

- typical triggers: long stops, repeated micro-stops, missed targets
- primary actions: notify the responsible role, track acknowledgment and resolution (depth varies by product; deep dispatch workflows belong to operations platforms)

## Important Rules / Behaviors

### The denominator rule

Availability is only meaningful against a honestly defined planned production time. Products treat the exclusions (major maintenance shutdowns, demand-idled shifts) as explicit configuration — and the documented failure mode is excluding too much: changeovers that overrun their scheduled time are losses, not planned time. The measure's honesty depends on this rule being configured and policed.

### The reference-rate rule

Performance compares actual speed against a reference. If the reference is wrong — typically set below what the machine can really do — performance exceeds 100% and the score loses meaning. Vendors explicitly advise verifying the reference with the machine builder or deriving a benchmark from the best recorded performance, then revisiting it as conditions change.

### Reason-coding discipline

Loss attribution is only as good as the reasons entered. Micro-stops too short to log, habitual "other" entries, and operator-blindness to repetitive small stops are documented distortions; automatic signals capture *that* a machine stopped but not *why*, which is why operator reason entry persists even in fully connected deployments.

### Late quality data

Quality counts often arrive after the shift ends (manual inspection, downstream checks). A documented way of handling this is to let the score's quality component be corrected in hindsight — the recorded score is provisional until quality data lands. How each product handles the lag varies; the distortion it causes is structural.

### Comparability is configuration-bound

OEE numbers are comparable only within a consistent measurement configuration. Two factories (or two products) with different planned-time exclusions, reference rates, or reason taxonomies produce scores that look identical but are not. This is why benchmarking across sites requires governance, and why "world-class OEE" claims are treated with caution.

### The score is a management object

The measure is expected to move. Targets, trend tracking, and before/after verification are structural behaviors of the Type, not reporting extras — a platform whose score never feeds a decision loop has degenerated into passive monitoring.

## Variants

- **Component scope** — full Availability × Performance × Quality vs partial implementations (Availability + Quality, or availability-focused utilization). A primary segmentation axis; partial products remain in-type.
- **Collection posture** — fully automatic machine connectivity vs operator-entry vs hybrid; plug-and-play sensor kits vs deep PLC/edge integration vs software-only integrations.
- **Standalone vs embedded** — dedicated OEE products vs OEE as a module inside manufacturing-operations suites, MES platforms, or frontline operations platforms (where it appears as a derived view on execution data).
- **Industry packaging** — discrete/CNC machining heritage vs packaging, food & beverage, and consumer goods vs process industries.
- **Scale and deployment** — single-line SME deployments (plug-and-play, days to install) vs multi-site enterprise rollups; cloud SaaS vs on-premise.
- **Adjacent applications on the same data** — energy monitoring, condition monitoring / predictive maintenance, scheduling assistance; commonly bundled, not definitional.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Factory Operations Management | closest sibling | centers the live operational picture and the event-response loop (dispatch, andon, routed resolution); OEE there is an output of the operations record, not the center. Remove the response loop from FOM → this Type's territory |
| Manufacturing Execution System / MES | adjacent, often bundled | centers enforcing order execution and the as-built record; OEE appears in MES products as a derived view on execution data |
| Machine monitoring / Industrial IoT Platform | substrate | collects machine signals and states; without the planned-time/loss/output accounting model it stays monitoring, not effectiveness management |
| CMMS / EAM | downstream consumer | receives downtime patterns and condition evidence; owns the asset-care center (work orders, PM schedules) |
| SPC / Manufacturing QMS | adjacent | owns formal quality records and control charts; here quality appears as counts feeding the score's quality component |
| Shop Floor Management | shares the response loop | visual/issue management at the point of work; can exist with no computed effectiveness score |
| Business Intelligence / analytics platforms | generic neighbor | lacks the domain measurement model (planned-time denominator, reference rates, loss taxonomy); OEE platforms typically export to BI rather than replace it |
| Production Planning / APS | upstream | owns the forward plan; this Type consumes planned time and order context |

The boundary with Factory Operations Management is the most important one, because the two Types share their data (machine states, downtime reasons, counts) and are frequently bundled. The structural difference is the center: the running operation and its response loop versus the effectiveness measure and its improvement loop.

## Representative Products

- **Evocon** — dedicated OEE software; sensor-based automatic collection, shift-centric live views, full A×P×Q methodology
- **MachineMetrics** — machine-data platform whose production-monitoring application delivers OEE, utilization, and downtime analytics for discrete manufacturers
- **FourJaw** — plug-and-play SME manufacturing analytics shipping Availability + Quality OEE with operator-logged downtime reasons

The Core Model was also checked against OEE-as-capability implementations inside broader platforms (connected-operations, frontline-operations, and enterprise MOM suites) to avoid over-fitting the definition to the dedicated-product shape.

## Sources

Research date: **2026-09-09**

- Evocon — OEE software product page: https://evocon.com/oee-software/
- Evocon — "What Is OEE and How Does It Work?" (methodology article): https://evocon.com/articles/what-is-oee-and-how-does-it-work/
- Evocon — OEE Dashboard feature page: https://evocon.com/feature/oee-dashboard/
- Evocon — How Evocon Works: https://evocon.com/how-evocon-works/
- Evocon — OEE Monitoring software page: https://evocon.com/oee-monitoring-software/
- MachineMetrics — Production Monitoring (OEE & production analytics): https://www.machinemetrics.com/production-monitoring
- MachineMetrics — homepage: https://www.machinemetrics.com/
- FourJaw — OEE Monitoring feature page: https://fourjaw.com/features/oee-machine-monitoring
- FourJaw — Continuous Improvement function page: https://fourjaw.com/functions/continuous-improvement
- FourJaw — homepage and FAQ: https://www.fourjaw.com/
- FourJaw — Help Center: https://help.fourjaw.com/knowledge

> Sourcing limitations: several mid-market OEE vendors (Mingo/SensrTrx, Amper, Matics) and two vendor documentation subdomains (Evocon docs, MachineMetrics support) were unreachable from the research environment; assertions relying on those surfaces are correspondingly weakened, and no precise numeric claims (benchmark scores, improvement percentages) are stated in this document. The OEE calculation model is stated on the strength of one vendor's detailed public methodology, corroborated by the other sampled products naming the same components and factors. Cross-referenced evidence for OEE as a derived view inside broader platforms (connected-operations, frontline-operations, MOM suite) is recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical / market-sample check are recorded in the paired Research Notes.
