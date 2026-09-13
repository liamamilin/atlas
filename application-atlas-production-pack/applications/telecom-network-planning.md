# Telecom Network Planning

## Overview

A **Telecom Network Planning** application is the operator-side decision application that turns demand into costed, prioritized deployment intent. It establishes where service is needed against the network that already exists, generates and compares alternative ways to build — routes, topologies, site placements, technology choices — quantifies each option's cost and expected performance or return, and converts that comparison into investment decisions and deployment priorities that downstream design and construction execute.

The defining structure is small:

```text
Demand & existing-network picture
└── Build alternatives (routes / topologies / sites / technology), compared as scenarios
    └── Quantified outcomes (cost, coverage or capacity gained, return)
        └── Prioritized deployment intent, handed to design & construction
```

Everything commonly associated with modern planning tools — GIS map canvases, automated route generation, AI-driven propagation models, crowdsourced traffic data, SaaS delivery — is widespread in current products but is not part of the defining core. Paper-era planning (demand studies, coverage curves on paper maps, route studies with cost estimates, capital plans) fits this definition without any of that machinery.

When the output becomes a constructible, connected network definition — strand-level routing, equipment placement, work packets — the work has crossed into **Telecom Network Design**. When the subject is the persistent record of what has already been built, it is **Fiber Network Management**.

## Users & Context

The primary users are the operator's network planning teams — fiber planners on the fixed-line side, radio/RF planners on the wireless side — who are asked "where should we build next, what should it be, and what will it cost and return?"

Typical reasons to open the application:

- assess which areas, buildings, or regions have enough demand to justify a build
- check what the existing network already covers and what can be reused
- generate and compare build options for a candidate area (routes, architectures, site locations)
- produce the cost estimate and business case behind an investment decision
- decide which candidate builds go first, and hand them forward for engineering

Secondary users shape the product's edges: sales and sales-engineering teams use planning tools to qualify opportunities and respond to build requests before committing engineering effort; engineering firms and consultancies run planning as a service for operators; executives and investment teams consume the business-case outputs. The work is desk-based and analysis-heavy, organized around geographic areas and candidate projects rather than tickets or live operations.

## Core Model

### The Defining Core

```text
Demand & existing-network picture
└── Build alternatives (routes / topologies / sites / technology), compared as scenarios
    └── Quantified outcomes (cost, coverage or capacity gained, return)
        └── Prioritized deployment intent, handed to design & construction
```

Four properties. If any one is removed, the product is no longer recognizable as network planning:

- **Demand and existing-network grounding** — every proposal is justified against where service is needed (demand points, traffic, coverage or capacity gaps) and against the network that already exists. Without this, the product is a cost calculator or a drawing tool with no basis for deciding.
- **Compared build alternatives** — the unit of planning work is a set of options (route options, topology or architecture variants, site placements, technology choices) held as scenarios that can be evaluated side by side. Without this, the product is a single-answer sketch — design, not planning.
- **Quantified outcomes per alternative** — each scenario carries decision-grade numbers: order-of-magnitude or budgetary cost estimates, bills of materials, expected coverage or capacity gained, revenue and return metrics. Without this, alternatives cannot be ranked and the comparison is theater.
- **A prioritized decision as the terminal output** — planning ends in a choice: which areas, sites, or builds to pursue, in what order, at what cost and expected return — producing deployment intent that downstream design and construction consume. Without this, the product is analysis with no deployment consequence.

### What Mature Products Add

A typical modern planning product carries most of these capabilities. They are not what makes the product a planning application, but they make planning practical:

- **Geographic working context** — demand layers, streets, buildings, existing plant, and candidate routes or sites on a map (fiber pole); terrain, clutter, and 3D building models as the propagation environment (wireless pole).
- **A high-level network model** — how the proposed assets would connect, at corridor or topology level rather than strand level.
- **Automation** — rules-based route generation, automated site placement, automated frequency assignment, automatic cost and BOM rollups.
- **Real-world data feedback** — field surveys, crowdsourced network data, call traces, and drive-test or measurement data used to correct and calibrate plans.
- **Infrastructure reuse** — brownfield planning that routes through or upgrades existing plant alongside greenfield builds.
- **Configurable rules and cost inputs** — the operator's own routing constraints, cost regions, and business-case parameters, so scenarios reflect how the operator actually plans, prices, and prioritizes.
- **Collaboration and handoff** — sharing scenarios for review, and carrying results into design tools, inventory or plant records, and construction or tendering processes.

### One Structure, Many Implementations

The core model is written in conceptual terms. The Variants section below enumerates how specific implementations realize each concept.

```text
Concept:     Demand & coverage picture
Realized as: demand points / homes-passed data, traffic maps, population and
             coverage studies, capacity-gap analysis against existing plant

Concept:     Build alternative
Realized as: route options, topology/architecture variants, candidate site
             placements, technology choices (new overlay, expansion, densification)

Concept:     Quantified outcome
Realized as: budgetary or order-of-magnitude cost estimates, bills of materials,
             coverage/capacity predictions, revenue / ROI / total-cost metrics

Concept:     Deployment intent
Realized as: a prioritized build program or business case, handed to design
             and construction as the basis for detailed engineering
```

A reader who has only seen one implementation (e.g., map-based fiber demand planning) should still be able to recognize wireless radio-network planning from the core model: the demand picture becomes traffic and coverage analysis, the alternatives become site placements and technology scenarios, and the quantified outcomes become coverage predictions balanced against cost and return.

## How It Works

### Turn demand into a decision

```text
Assemble the demand and network picture
→ generate build alternatives for the candidate area
→ quantify each alternative (cost, coverage/capacity, return)
→ compare scenarios side by side
→ decide and prioritize (which builds deserve the next level of attention)
→ hand the deployment intent forward to design and construction
```

This is the defining loop. Vendors describe its absence with striking consistency: manual, spreadsheet-based feasibility analysis; static views with limited network insight; uncertain, inconsistent cost assumptions; planning results disconnected from downstream workflows. The product exists to replace that state.

### Assemble the picture

Planning starts by bringing together what the operator knows: demand (homes, buildings, traffic, population), the existing network (routes, plant, coverage, capacity), and the geography that constrains both. On the wireless side this includes calibrated propagation data, because coverage — not street geometry — determines what a site can serve.

### Generate and compare alternatives

For a candidate area, the planner generates options: which route a cable takes, which topology or architecture the network uses, which sites serve which demand, whether to overlay a new technology or expand the existing one. Each option is quantified with the operator's own cost inputs and rules. The comparison is the point — a planning tool that produces only one answer is doing design.

### Decide and hand forward

The ranked comparison becomes the investment decision: which areas or builds go first, at what cost, with what expected return. The output is decision-grade — budgetary estimates and high-level topology, not strand-level construction data. It flows forward as the foundation for detailed design, and its material quantities can feed procurement and tendering.

### Core vs Common vs Optional

**Defining core** — without these, not network planning:

- demand and existing-network grounding
- compared build alternatives as scenarios
- quantified outcomes per alternative
- a prioritized decision / deployment intent as the terminal output

**Standard capabilities** — present in most modern products:

- geographic or propagation working context
- high-level connected network model
- automation of route generation, site placement, frequency assignment, cost rollups
- real-world data feedback (surveys, crowdsourced data, measurements)
- infrastructure reuse / brownfield planning
- configurable rules and cost inputs
- collaboration, review, and downstream handoff

**Variant / optional** — depends on domain, operator, and era:

- backhaul and transport dimensioning (topology, capacity, latency; fiber vs microwave)
- spectrum and interference planning as an explicit face of wireless planning
- sales-engineering / opportunity-qualification workflows
- SaaS delivery of planning tools
- AI-driven propagation and optimization machinery

## Interfaces

The following surfaces are described in conceptual terms. Exact layouts and names vary by product.

### Map-based planning canvas

The primary working surface.

- demand layers, existing network, candidate routes or sites, coverage or prediction overlays
- primary actions: define a study area, generate or draw route/site options, inspect demand and constraints

### Scenario comparison view

Where the decision happens.

- alternatives listed side by side with their quantified outcomes (cost, coverage or capacity, return)
- primary actions: adjust assumptions, re-run a scenario, rank and select

### Cost / BOM outputs

The investment-facing surface.

- budgetary or order-of-magnitude cost estimates, material quantities, per-area or per-route breakdowns
- primary actions: produce estimates for a business case, export quantities for procurement or tendering

### Coverage / prediction views (wireless pole)

The radio planner's evidence surface.

- predicted coverage, capacity, and interference for candidate configurations
- primary actions: place or move sites, adjust technology parameters, compare predictions against targets or measurements

### Reports and business-case outputs

The decision-facing surface for executives and investment teams.

- prioritized build programs, cost/return summaries, feasibility conclusions
- primary actions: assemble the case, present the ranking, record the decision

## Important Rules / Behaviors

### Planning outputs are decision-grade, not build-grade

Planning produces order-of-magnitude or budgetary estimates and high-level topology. The constructible, connected network definition is produced downstream by design. Products blur this in practice (some planning tools can produce detailed bills of materials), but the center of gravity of the planning act is the decision, and its outputs are calibrated for investment choices, not construction crews.

### Alternatives must be comparable

Scenarios only support a decision if they are quantified on a consistent basis — the same demand assumptions, the same cost inputs. Vendors explicitly frame inconsistent cost assumptions as the failure state planning tools exist to fix.

### The existing network both constrains and enables

Plans are made against what already exists: routes follow or connect to existing plant, expansions reuse capacity, densification fills gaps in current coverage. Greenfield planning is the special case, not the default.

### Real-world data corrects plans

Plans are calibrated against reality — field surveys, measurements, crowdsourced usage data — and corrected before they harden into design. A plan that never meets real-world data is a hypothesis.

### Prioritization is the terminal act

Planning ends by ranking: which builds deserve the next level of attention. The ranking, not any single study, is the product's reason to exist.

## Variants

The Type is realized in several common forms:

- **Fixed-line fiber/copper planning** — demand points and service areas turned into route options and costed deployment programs; business-case-driven prioritization (which areas to deploy first).
- **Wireless radio-network planning** — traffic and coverage analysis turned into site placements, technology scenarios (new overlay, capacity expansion, densification), and frequency plans; coverage/capacity/interference physics balanced against cost and return.
- **Backhaul/transport planning** — dimensioning of the links that carry traffic: topology, capacity, latency, and fiber-vs-microwave choices.
- **Opportunity-qualification planning** — sales-engineering-facing planning that answers "is this build worth pursuing?" before deep engineering effort is committed.
- **Automation-depth variants** — manual feasibility studies, rules-based generation of routes/sites, and automated optimization sit on one gradient; the core does not change.
- **Hosting variants** — standalone planning tools, planning modules inside plant-record platforms, suite products alongside design and operations, and SaaS planning services.

A variant remains a **Variant** unless it changes the core users, objects, workflow, or rules so fundamentally that the defining core no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Telecom Network Design | the closest sibling: planning produces decision-grade intent (where/what/invest/prioritize); design engineers that intent into a constructible, connected network definition. Many products carry both as adjacent workflows and are marketed as one "planning & design" solution — the center of gravity differs, not the product list |
| Fiber Network Management | centers the persistent plant of record (the built network as connected, geospatial record); planning consumes that record as context and proposes what to add to it |
| Telecom Inventory Management | holds the estate of equipment and services as records; planning reads it as context and proposes changes to it |
| Network Construction Management | executes the build as projects (schedules, contractors, progress); planning's terminal output is the costed intent that construction eventually consumes |
| Telecom Provisioning Platform | activates services on the built network; fulfillment takes over after planning (via design and build) has decided what the network is |
| Mobile Network Management | operates the live radio network (cells, KPIs); planning engineers the future network and imports live data only to inform decisions |
| Telecom Service Assurance | monitors and restores live services; its data feeds planning, but operation of the live network is a different Type |
| Site Selection Platform | real-estate site search; cell-site selection is one subtask inside wireless planning, not the whole deployment decision |
| Capacity Management (IT infrastructure) | plans IT capacity supply over time; telecom network planning covers the full deployment decision including greenfield builds and technology choice |
| Utility GIS / Government GIS | supply the geographic substrate and data models; the planning act sits on top |

The boundary with **Telecom Network Design** is the most important one, because the two Types share objects (routes, sites, topologies) and are frequently bundled. The structural difference is the grade of the artifact: planning ends in a compared, quantified, prioritized decision; design ends in a buildable, connected network definition. The boundary with **Fiber Network Management** is the second: planning is an act that produces intent; the plant record is the persistent thing the intent eventually modifies.

## Representative Products

- Comsof Fiber (IQGeo) — automated FTTx planning and estimating
- IQGeo Optimized Planning — high-level fiber planning and feasibility
- 3-GIS | Prospector — demand-to-routes opportunity evaluation
- Infovista VistaPlan / Planet — RF planning and investment optimization
- ATDI HTZ Communications — technology-neutral radio network planning and modelling

The defining core was checked against adjacent products from neighboring Types (Forsk Atoll, VETRO FiberMap, Netadmin Nine) to confirm the planning/design and planning/plant-record boundaries from both directions.

## Sources

Research date: **2026-09-10**

Primary vendor surfaces (official product / solution / FAQ pages):

- IQGeo — Comsof Fiber: https://www.iqgeo.com/products/comsof-fiber ; FAQ: https://www.iqgeo.com/product/comsof-fiber/faq ; Optimized Planning: https://www.iqgeo.com/telecom-use-cases/optimized-planning
- 3-GIS — Prospector: https://www.3-gis.com/software/3-gis-prospector
- Infovista — VistaPlan: https://www.infovista.com/products/planet-suite/network-planning-optimization ; Planet: https://www.infovista.com/products/planet/rf-planning-software
- ATDI — Radio Network Planning: https://atdi.com/products-and-solutions/radio-network-planning/

Cross-referenced vendor pages (fetched 2026-09-08 / 2026-09-10): Forsk Atoll — https://www.forsk.com/atoll ; VETRO FiberMap — https://vetrofibermap.com/ ; 3-GIS fiber planning & design FAQ — https://www.3-gis.com/telecom/fiber-network-planning-design ; Netadmin Nine — https://www.netadminsystems.com/

> Sourcing limitation: live fetch of vendor help-center documentation was not possible from the research environment on 2026-09-10; evidence is official product/solution/FAQ pages. TEOCO and Ranplan (additional wireless planning vendors) were unreachable and are not sampled. Precise operational details — numeric limits, cost-model mechanics, state vocabularies, vendor marketing figures — are intentionally not stated in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical market-sample check are recorded in the paired Research Notes.
