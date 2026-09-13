# District Energy Management

## Overview

A **District Energy Management** application is operator-side software for running a shared thermal energy network — a district heating or district cooling system — in which energy is produced centrally, distributed through a pipe network, and delivered to many connected buildings.

Its purpose is to let the network operator see and steer the whole system as one entity: how much heat or cold will be needed, which production units should run and when, at what temperature the network should be supplied, and how the running system is actually performing against the plan.

The defining structure is small:

```text
Whole-system model of record
(production units + distribution network + delivery/consumption points)
└── Demand–supply coordination over time
    (demand forecast → production and distribution decisions,
     including the network's supply temperature)
    └── Live measurement integration
        (the running system is supervised and steered against the plan)
```

Everything commonly added by mature products — supply-temperature optimization, thermal storage exploitation, peak-load management, building-level monitoring, power-market coupling, scenario planning — is standard or optional capability, not what makes the product this Type. Remove the live-operations leg and the product becomes an offline design and feasibility modeling tool; remove the whole-system model and it collapses into dashboards or bare SCADA; remove the coordination leg and it becomes a forecasting tool or historian.

## Users & Context

The operator of the application is the **district energy utility** — the organization that owns or runs the network. These are frequently municipally owned energy companies operating one city or region's heating (and sometimes cooling) network, and the software is also used by industrial energy suppliers running their own thermal systems.

Typical roles and their relationship to the system:

- **Production planners** — work with the forecast and the optimized production plans; decide and schedule which units run, manage storage levels, and follow up production economics.
- **Network operations / control-room staff** — watch the live state of production, network, and delivery points on dashboards; execute or supervise plan changes.
- **Network planners / engineers** — use the system model and simulations for design, connection growth, and investment decisions.
- **Demand-side / customer-operations teams** (in some deployments) — monitor and optimize the connected buildings and substations on behalf of the network's goals (peak shaving, return temperature, indoor climate).

The work context is seasonal and weather-driven: demand depends strongly on outdoor temperature, production often couples heat and electricity (CHP), and mistakes are expensive in both fuel and comfort. The software typically sits beside an existing SCADA/control system, consuming its measurements and handing decisions back to it or to plant controls.

## Core Model

### The Defining Core

**The whole-system model of record.** The application holds a persistent, connected representation of the entire district energy system: the production units (boilers, CHP units, heat pumps, chillers, solar thermal, storage tanks) with their technical and economic characteristics; the distribution network (topology, pipes, pumps, losses); and the delivery points — the substations and buildings where energy leaves the network to customers. Different products realize this as a physics-based real-time digital twin, a thermo-hydraulic network model, or an editable topology model of the "energy system" — but in all cases it is the single picture of the whole system on which forecasts, plans, and simulations run.

**Demand–supply coordination over time.** The application forecasts the system's demand (heated by weather forecasts, historical consumption, and live measurements; cooling demand is forecast the same way where the operator runs a cooling network), and turns it into decisions on the supply side: which production units to commit in each period and at what output, how to charge or discharge storage, and — distinctive of heat networks — at what supply temperature to run the network. Supply temperature is a genuine operating decision, not a setting: lower temperatures mean lower network heat losses, while higher temperatures secure delivery capacity. Plans are evaluated economically and in emissions, not only in physics.

**Live measurement integration.** The application takes in measurements from the running system — production data and network data via SCADA, sensors, and online meters — so that operators can supervise actual performance, compare it with the plan, and correct course. In mature products the same measurements continuously recalibrate the model and the forecasts; in some, they also close the loop and directly control variables such as the supply temperature.

Remove any leg and the product stops being this Type: without the model there is no whole-system picture; without coordination the software merely reports; without live integration it is an offline study tool.

### Standard Capabilities

Mature products commonly add these capabilities around the core. They make the Type practical, but a product lacking a given one can still be a district energy management application:

- **Supply-temperature optimization** — continuously choosing network supply temperature to balance heat loss, cost, and security of supply.
- **Thermal storage exploitation** — using storage tanks, the thermal mass of the network itself, and connected buildings ("virtual storage") to shift production away from expensive or high-emission periods.
- **Peak-load management** — flattening demand peaks to avoid starting peak-load boilers and to defer network and production capacity investments.
- **Delivery-point and building-level monitoring** — per-substation or per-building consumption, return temperature, and indoor climate, used both for network steering and for demand-side optimization.
- **Demand-side flexibility** — coordinating with connected buildings so that consumption can be shifted or shed when the network needs it, with the building's comfort constraints respected.
- **Production-economics follow-up** — plan-versus-actual analysis, cost and CO₂ reporting, integration with business-intelligence and reporting systems.
- **Scenario simulation** — running "what if" situations on the system model: new units, new connections, changed tariffs, fuel switching.
- **Weather-forecast integration** — standard outdoor-temperature-driven forecasting, sometimes with locally calibrated meteorological forecasts.
- **Cooling as a second carrier** — forecasting and optimizing district cooling in the same system where the operator runs one.

### One Structure, Many Implementations

The core is written conceptually; concrete products realize it differently:

```text
Concept:   Whole-system model of record
Realized as: real-time physics-based digital twin / thermo-hydraulic
             network model / editable topology model of production
             units and networks

Concept:   Demand forecast
Realized as: self-learning machine-learning forecasts fed by weather
             and online measurements / statistical load and price
             forecasting / measured-temperature demand profiles

Concept:   Supply-side decision
Realized as: advisory optimized production plans the operator executes
             in plant controls / direct closed-loop control of network
             supply temperature / manual planning supported by
             forecasts and dashboards
```

## How It Works

### The daily operational loop

```text
Maintain the system model
  (units, network, delivery points; technical + economic parameters)
→ integrate live measurements
  (SCADA / sensors / online meters; model recalibrates)
→ forecast demand
  (weather-driven, per period, whole-network)
→ produce the optimized plan
  (unit dispatch, storage use, supply temperature — cost and CO₂ evaluated)
→ execute
  (operators follow the plan in plant/network controls, or the system
   issues setpoints itself)
→ follow up
  (actual vs plan; economics; forecast quality feeds the next cycle)
```

This loop repeats continuously through the day; the forecast horizon and replanning rhythm vary by product. The forecast is the foundation of the chain — most products treat it as the indispensable first module.

### The planning and investment loop

The same system model serves longer-horizon work: simulating future demand and prices, testing new production units or new network connections, sizing investments, and comparing transition scenarios. In some products this happens in the same application; in others it is an offline companion tool built on the same abstractions (see Variants).

### The demand-side loop

Where the operator manages connected buildings, the application monitors each building's substation and indoor climate, optimizes its consumption against network goals (peaks, return temperature, supply temperature), and can activate building-side flexibility when the network needs it — trading network-level economics against per-building comfort, which the system keeps inside defined limits.

## Interfaces

Described conceptually; layouts and names vary by product.

### System model / topology editor

The model of record surface.

- production units, network, and delivery points as a connected diagram or map
- technical and economic parameters per component
- primary actions: build and edit the model, attach data sources, keep it current

### Forecast and measurement views

Where the data layer lives.

- demand forecasts against weather, measurement series from SCADA and meters
- primary actions: inspect forecast quality, trace measurements, compare periods

### Production plan view

The central decision surface.

- time-resolved plan of unit dispatch, storage levels, supply temperature, costs and emissions
- short-term (operational) and long-term (strategic) horizons
- primary actions: generate plan, adjust constraints, compare plan variants, hand over to operations

### Control-room dashboards

The supervision surface for operations staff.

- live system state across production, network, and delivery points
- primary actions: monitor against plan, drill into deviations, alarms and anomalies

### Building / substation views

The demand-side surface.

- per-building or per-substation consumption, return temperature, indoor climate
- primary actions: inspect a building, adjust its optimization, activate or review flexibility

### Reporting and scenario surfaces

- plan-versus-actual economics, emissions reporting, BI-system integration
- scenario comparison for investments and network changes

## Important Rules / Behaviors

- **The forecast anchors the chain.** Production plans, temperature optimization, and trading decisions are all built on the demand forecast; products make its quality a first-class concern and feed measured actuals back into it.
- **Supply temperature is a running compromise.** Lower supply temperature cuts network heat losses; too low threatens delivery capacity and comfort. Products optimize this trade explicitly, and security of supply constrains the optimization.
- **The network has thermal inertia — and that is a resource.** Heat can be stored in tanks, in the network itself, and in connected buildings, and released when it is cheap or clean to have produced it. Storage levels are planned variables, not background physics.
- **Peaks drive the economics.** A large share of cost and investment pressure comes from short peak periods; flattening them (demand-side management, pre-stored heat, temporary temperature raises) is a core reason the planning exists.
- **The application is not the SCADA.** Measurements and control execution normally live in the SCADA/control layer; the district energy management application consumes measurements and hands decisions or setpoints across that seam. How much it directly controls varies by product and by the operator's willingness to delegate.
- **Model quality bounds plan quality.** Optimizations are only as good as the technical and economic parameters of the system model; keeping the model current with the real network is part of operating the software.
- **Plans are usually advisory.** In many deployments the application recommends and humans execute; closed-loop control of network variables is a product-dependent posture, and operators differ in how much autonomy they grant.
- **Market coupling is conditional.** Where production includes electricity-generating units, the production plan extends into bidding and trading decisions on power markets; where it does not, this surface is absent.

## Variants

- **Heating-centric vs cooling-inclusive vs extended carriers** — heating networks are the classic core; mature suites add district cooling forecasting/optimization; one product family extends the same model to steam and even CO₂ grids for industrial users.
- **Philosophy poles** — economics-first production planning (the whole energy system as one cost/CO₂ optimization, power trading included), network-twin-first operations (real-time physics model of the grid down to un-metered segments), and demand-side-first suites (building-level AI optimization serving network goals).
- **Advisory vs closed-loop** — from plan recommendation to direct control of supply temperature and building-level heating.
- **Operational suite vs offline planning tool** — the same abstractions (system model, unit economics, optimal production plan) also appear in standalone design/feasibility products used by engineers and consultants for investment and scenario studies, without the live-operations leg; these are adjacent to this Type rather than instances of it.
- **Market-participant operators** — CHP-heavy utilities couple planning to electricity markets (day-ahead, intraday, ancillary services); non-participating operators run without that surface.
- **Deployment** — on-premise servers, vendor-operated private cloud, or cloud SaaS; long-lived utilities often keep the model of record on-premise.
- **Vendor-services coupling** — some vendors deliver the software together with consultant-run studies and special modeling as an ongoing service.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Energy Management System / EMS | adjacent (electric) | EMS supervises electrical generation and transmission; the carrier, physics, and operating decisions (frequency vs temperature/heat loss) differ |
| Distribution Management System / DMS | adjacent (electric) | operates electrical distribution networks (switching, outage restoration); different carrier and different operational acts |
| SCADA / Industrial Historian | complementary substrate | SCADA provides the telemetry and control layer; this Type consumes its measurements and adds the model, forecast, and planning/optimization layer on top |
| Energy Forecasting Platform | overlapping capability | forecasting exists here as a module; the defining closure is forecast → production/distribution decision, which the neighbor Type lacks |
| Demand Response Platform | overlapping capability | consumer flexibility appears here as a network operating resource; DR platforms are market-facing aggregation products on the electric side |
| Virtual Power Plant Platform | adjacent | VPP aggregates and dispatches distributed electricity assets for markets; the thermal analog here is storage/flexibility in service of the network, not market bidding |
| Building Energy Management | adjacent, different operator | BMS/BEMS serves a building owner managing one building's systems; here the network operator manages many buildings as delivery points; the same product line can be sold to both seats |
| Customer Energy Management | adjacent, opposite side | serves the energy customer acting on their own premises; this Type serves the operator acting on the shared network |
| Utility Billing Platform | adjacent | delivery-point consumption is measured here, but customer accounts, invoicing, and money belong to billing |
| Water Utility Management | structural analogy only | same production→network→consumer skeleton with different carrier physics (pressure/quality vs temperature/heat loss) |

The sharpest seams are with EMS/DMS (carrier physics define the Type), with SCADA (layering, not duplication), and with the building/customer-side Types (the operator's seat defines which side of the seam a product is on).

## Representative Products

- **Gradyent Digital Twin Platform** — real-time digital twin for heating, cooling, steam, and CO₂ grids; optimization from production to end users plus future-situation simulation.
- **Danfoss Leanheat Software Suite** — modular district energy suite: load forecasting, temperature optimization, and production optimization (Leanheat Production), thermo-hydraulic network modeling (Leanheat Network), system monitoring (Leanheat Monitor), and building-level demand-side optimization (Leanheat Building).
- **Energy Optima 3 (Energy Opticon AB)** — economic total optimization of integrated energy systems: topology model, SCADA integration, load/price forecasting, optimized production plans, power-market coupling, and network forward-temperature optimization; used by energy companies across the Nordics, Baltics, and Europe since the early 1990s.
- **energyPRO (EMD International)** — offline design, feasibility, and scenario modeling of district heating systems (investment sizing, unit dispatch studies), recorded as the adjacent planning pole of the Type.

The definition was checked against the market's older and regional breadth: the sampled products span three countries and three decades of lineage (one product documented since 1992), and the defining core deliberately excludes market coupling, closed-loop control, and AI forecasting, all of which are era- or market-dependent.

## Sources

Research date: **2026-09-07**

- Gradyent — https://www.gradyent.ai/ (homepage, Digital Twin page)
- Danfoss — Leanheat® Building and Leanheat® Production product pages, https://www.danfoss.com/en/products/dhs/software-solutions/
- Energy Opticon AB — Energy Optima 3, https://www.energyopticon.com/
- EMD International — energyPRO District Heating use case, https://www.emd-international.com/district-heating-in-energypro

> Sourcing limitation: research was limited to official vendor product pages; operational user guides and help centers were not reachable in this pass (one further network-modeling vendor's product page returned an access error). Precise operational figures quoted by vendors (forecast horizons, accuracy, savings percentages) are therefore not restated in this document. Detailed observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
