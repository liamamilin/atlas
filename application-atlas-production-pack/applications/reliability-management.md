# Reliability Management

## Overview

A **Reliability Management** application is the reliability engineer's system for an operating equipment population: it holds what is known about **how the organization's equipment fails**, makes that failure knowledge analyzable and comparable, and turns it into **justified maintenance strategies** that are deployed to the maintenance program and revised as new failure experience arrives.

It exists because asset-intensive operations (refineries, plants, mines, utilities, fleets) cannot decide maintenance by intuition: what to maintain, by which task, how often, and at what cost versus risk are engineering decisions that must be traceable to failure modes and defensible against cost, safety, and operational consequences.

The defining structure is small:

```text
Equipment / Function / Failure-mode record
└── Failure evaluation (criticality · consequence · failure behavior · cost/risk)
    └── Maintenance strategy decisions (task · interval · justification)
        └── Deployment into the maintenance program
            └── Revision as new failure data and operating context arrive
```

The boundary matters as much as the core: this application does not execute maintenance work (that is the maintenance/asset-management system's job), does not measure production output (that is an equipment-effectiveness system's job), and does not plan product durability tests (that is a product-test system's job). It is the failure-and-strategy discipline that sits between the equipment's failure history and the maintenance program that responds to it.

## Users & Context

Primary users are reliability and maintenance-engineering roles:

- **reliability engineer** — builds and maintains failure-mode analyses, analyzes failure data, recommends strategy changes
- **RCM facilitator / analysis team** — runs structured failure-mode-and-consequence studies with operations and maintenance participants
- **maintenance engineering lead** — owns the maintenance strategy per equipment class; decides task and interval changes

Secondary users:

- **inspection/integrity engineers** (in facilities with fixed equipment) — provide inspection findings and thickness/corrosion data into the same record
- **asset managers / site leadership** — consume criticality rankings, risk positions, and strategy-coverage reporting
- **CMMS/EAM planners** — receive the strategy output as maintenance plans and master data

The work context is typically a fleet of similar equipment types replicated across units and sites, a maintenance history living in a separate maintenance/asset-management system, and a review rhythm in which strategies are revisited periodically or when failures surprise the program.

## Core Model

### The Defining Core

**Equipment failure knowledge of record.** The system holds persistent, structured records of how identified equipment fails. Equipment is organized in a hierarchy (unit → system → equipment class → component-class level), each carrying its **functions** and the **failure modes** by which those functions are lost. Two kinds of content feed this record, and mature products usually hold both:

- *failure-mode analyses* — authored engineering entries (FMEA/FMECA/RCM-style): for each function, the ways it can fail, the local and system effects, the causes, and the consequence class
- *failure experience* — recorded failure events, breakdowns, inspection findings, and repair history, typically imported from the maintenance/asset-management system rather than captured from scratch

The failure-mode entry — not the work order, not the asset record — is the anchor object. A failure event is valuable here because it can be attributed to a failure mode; an asset record is valuable because failure modes attach to it.

**Failure evaluation.** The failure knowledge is analyzed so failure modes can be compared and prioritized. The analytical depth varies widely by product and by customer maturity, and that depth is not what defines the Type:

- at the judgment end: criticality and consequence ranking by engineering assessment
- in the middle: failure-rate and life-data analysis (distributions fitted to failure times, mean-time metrics), cost-of-failure aggregation, worst-actor identification
- at the deep end: availability simulation of the plant model, quantitative probability-of-failure and consequence-of-failure risk models

**The maintenance strategy loop.** Evaluation resolves into **strategy decisions held as managed, revisable artifacts**: for each significant failure mode, which maintenance task (on-condition inspection, restoration, replacement, redesign, or a documented decision to run-to-failure), at what interval or condition trigger, justified against cost, safety, environmental, and operational consequences. Strategies are commonly built per equipment type and reused across sites through libraries or equipment knowledge bases. The loop closes in two directions: strategies are **deployed** outward into the maintenance program (typically as master data and task plans consumable by the EAM/CMMS), and **revised** inward as new failure data, inspection results, and operating-context changes accumulate — a living strategy, governed by review and approval where the organization requires it.

### Standard Capabilities

Mature products commonly carry most of the following, without these being what makes the product a reliability-management application:

- FMEA/FMECA and RCM analysis worksheets with configurable templates matching recognized RCM/FMEA reporting conventions
- criticality and risk matrices over equipment and failure modes
- life-data analysis on failure times and repairable-system data
- PM-interval optimization and maintenance-strategy cost comparison, often simulation-assisted
- strategy libraries / equipment knowledge bases shared across sites and projects
- EAM/CMMS integration in both directions: failure and work history in, strategies and master data out
- failure-event and corrective-action tracking (FRACAS-style closed loops) where capture is not delegated to the CMMS
- reporting for engineering review and management visibility (worst actors, strategy coverage, forecast versus actual performance)

### One Structure, Many Implementations

The core is written conceptually. Common realizations differ along two axes worth naming, because both are frequently mistaken for the definition:

```text
Concept:   Failure knowledge of record
Realizations:  own failure-event reporting modules
               authored FMEA/RCM worksheets
               failure/work history imported from EAM/CMMS
               equipment knowledge libraries

Concept:   Failure evaluation
Realizations:  expert-judgment criticality ranking
               statistical life-data analysis
               availability simulation
               quantitative risk models (probability/consequence)
```

A reader who has only seen one pole (for example, statistical life-data toolkits, or consulting-built strategy libraries) should still recognize the other pole from this model.

## How It Works

The characteristic cycle runs from failure knowledge to maintenance program and back:

```text
Establish the equipment/function structure
→ build or import failure-mode knowledge
  (FMEA/RCM studies · failure history from the EAM/CMMS · inspection findings · libraries)
→ evaluate failures
  (criticality/consequence · failure behavior over time · cost and risk)
→ decide strategy per failure mode
  (task type · interval or condition trigger · justification against standards)
→ deploy to the maintenance program
  (task plans and master data handed to the EAM/CMMS)
→ operate and collect
  (new failures, inspection results, strategy performance)
→ review and revise
  (worst-actor analysis · strategy updates under governance · re-deployment)
```

Three work modes coexist inside this cycle:

- **The analysis study** — a facilitated FMEA/RCM pass over an equipment class: functions, failure modes, effects, consequence evaluation, task selection. The study is recorded as reusable knowledge, not a one-off report.
- **The data analysis pass** — failure history imported from the maintenance system is examined for concentration and behavior (which equipment, which modes, what rate), feeding both strategy revision and new failure-mode entries.
- **The governance pass** — strategies under revision move through review and approval, and deployed plans are reconciled against what the maintenance system actually executes, exposing drift between agreed strategy and performed work.

## Interfaces

Described conceptually; layouts and names vary by product.

### Equipment / failure-mode explorer

The structural spine of the system.

- equipment hierarchy with functions and failure modes attached
- typical information: equipment class, function, failure mode, effects, causes, consequence class
- primary actions: navigate the hierarchy, add/edit failure modes and analyses, attach failure events, filter by criticality

### Analysis worksheet (FMEA / RCM)

The study surface where failure knowledge is authored and task decisions are made.

- rows per function/failure mode; columns for effects, causes, consequence ratings, and selected tasks
- primary actions: enter/rate failure modes, apply decision logic, select maintenance tasks, set intervals, compare strategy alternatives on cost and risk

### Analysis workbench (data and models)

Where failure behavior is quantified.

- life-data plots and fitted distributions over failure times; failure-rate and mean-time metrics
- criticality/risk matrices; simulation or risk-model results where offered
- primary actions: import data sets, fit and compare models, rank worst actors, feed results into strategy decisions

### Strategy library / register

The managed inventory of strategies.

- strategies per equipment type with task lists, intervals, justifications, version and approval state
- primary actions: build from templates or prior studies, adapt to operating context, submit for review, publish, compare forecast versus actual performance

### Integration surfaces

Rather than user-facing pages, this Type's most consequential "interfaces" are often connections: pulling failure/work history from the maintenance system, and emitting strategies and master data back to it.

## Important Rules / Behaviors

- **Strategy decisions must trace to failure modes.** A task exists because a specific failure mode on a specific function justifies it. Strategies detached from failure knowledge are not this discipline's output.
- **Consequence, not just likelihood, drives task selection.** The same failure mode can warrant different tasks depending on safety, environmental, operational, and cost consequences — and some failure modes are deliberately left to run to failure, as a recorded decision rather than an omission.
- **The strategy is living.** Strategies are revised when new failure data, inspection findings, or operating-context changes arrive. Products differ in how much of this revision is workflow-governed, but the revision expectation itself is structural.
- **Failure experience is usually borrowed, not captured.** In mature deployments the maintenance/asset-management system remains the system of record for work and often for failure events; the reliability system holds the failure-mode interpretation of that experience.
- **Standards shape the record, not the record structure.** Industry frameworks (RCM process standards in general industry, aviation maintenance-program methodology, fixed-equipment inspection frameworks) shape worksheets, decision diagrams, and reports; products adapt to several of them simultaneously through configurable templates.

## Variants

- **Analysis-toolkit products** — deep statistical and modeling machinery (life data, system availability modeling, reliability prediction) with FMEA/RCM worksheets; favored by engineering teams; may also serve product-design reliability work on the same machinery.
- **Strategy-management platforms** — the strategy artifact, its libraries, and its governance at enterprise scale; strong deployment machinery into EAM master data; favored by large multi-site operators.
- **Data-driven APM suites** — inspection/ITPM data systems (asset registry, inspection management, risk-based inspection) combined with RCM and quantitative risk/availability modeling; favored in process industries with heavy fixed-equipment integrity obligations.
- **Industry-wrapped realizations** — aviation maintenance-program development (a named methodology with its own task-selection logic) is the same strategy loop under a strict regulatory wrapper; automotive/energy reporting conventions similarly wrap the worksheets.
- **Design-reliability reuse** — the same tool families are used upstream on product designs (design FMEA, test-data reliability analysis); that subject matter belongs to product development and test processes, with this Type's center of gravity on operating equipment.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| CMMS / Maintenance Management | consuming/executing counterpart | holds asset register + work orders + maintenance history; executes what the strategy prescribes; its embedded failure dashboards are extensions, not the discipline |
| Enterprise Asset Management / EAM | broader sibling | whole-life asset cost and lifecycle governance over the same work-management core; consumes strategies as master data, does not own the failure-mode/strategy machinery |
| Enterprise Asset Registry | substrate | static identified-asset records; the equipment hierarchy inside a reliability product is the substrate, the failure/strategy loop is the Type |
| OEE Management Platform | adjacent measure | centers a production-effectiveness measure and its improvement loop on output; reliability centers failure behavior and maintenance strategy; downtime events may feed both |
| Product Test Management | upstream sibling | plans and records verification/durability tests of engineered products; reliability test data may flow into reliability analysis, but test execution is not this Type |
| Industrial IoT Platform / Industrial Historian | data substrate | device connectivity and condition telemetry; reliability machinery consumes condition data but does not center it |
| Aircraft Maintenance Management | domain instance | aviation carries the strategy loop inside an airworthiness-focused system; this Type is the discipline machinery independent of the airworthiness spine |
| SRE Management (IT domain) | name collision only | reliability objectives for software services (SLIs/SLOs/error budgets); entirely different subject matter — physical equipment failure vs service-level objectives |
| Manufacturing QMS / CAPA | neighboring loop | product-conformity corrective action; shares corrective-action mechanics but manages product quality, not equipment failure modes and maintenance strategy |
| Incident Management (IT) | name collision only | response workflow for service incidents; no failure-mode/maintenance-strategy content |

The most important boundary is with the CMMS/EAM: the two are complementary halves of one operation. The maintenance system knows what work was done and holds the equipment register; the reliability system knows why equipment fails and decides what work should exist. Remove the failure-and-strategy loop from a reliability product and nothing of the Type remains; remove it from an EAM and the EAM survives intact.

## Representative Products

- ReliaSoft suite (Weibull++, XFMEA, RCM++, XFRACAS) — HBK — analysis-toolkit pole
- Reliability Workbench / Availability Workbench (RCMCost, AvSim) — Isograph — modeling-and-RCM pole
- Cordant Asset Strategy (formerly OnePM, ARMS Reliability) — Baker Hughes — strategy-management pole
- Newton™ suite (RDMS, Intelligence) — Pinnacle — data-driven APM pole

## Sources

Research date: **2026-09-09**

- HBK / ReliaSoft — Reliability software catalog; RCM++ product page; XFRACAS product page — hbkworld.com
- Isograph — Reliability Workbench; RCMCost module; "Reliability Centered Maintenance" method page — isograph.com
- Baker Hughes / Cordant — ARMS Reliability landing page; Cordant Asset Strategy product page — bakerhughes.com / armsreliability.com
- Pinnacle — Newton™ overview; Newton™ RDMS product page — pinnaclereliability.com

> Sourcing limitation: enterprise vendor Bentley (Meridium-lineage asset performance management) could not be fetched (repeated timeouts) and one other enterprise vendor page returned 404; the enterprise pole is evidenced through the three reachable products' convergence and cross-references. No help-center-level operational documentation was reachable for any sampled product; all evidence is vendor product/method documentation. Accordingly, this document states no numeric limits, defaults, or precise workflow rules, and keeps cross-product claims at the structural level.
