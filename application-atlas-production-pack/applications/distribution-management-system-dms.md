# Distribution Management System / DMS

## Overview

A **Distribution Management System (DMS)** is an electric utility's distribution network-analysis system. It holds a connected electrical model of the utility's own distribution network and computes electrical analysis on that model — how power flows through the feeders, what the voltages and losses are, where faults would produce how much current — so that the utility's operating and planning decisions about its network rest on computed electrical evidence rather than assumption.

The defining core is deliberately small: the network model, the analysis computed on it, and the operating/planning decisions it serves. A system with those three is a DMS even if it has no real-time SCADA feed, no remote control of devices, and no outage management. Conversely, a telemetry-and-control system without a connected network model and analysis is SCADA; an integrated real-time platform that adds live telemetry, device control, and an operational event loop on top of this analysis layer is an Advanced Distribution Management System (ADMS); an outage call/event/crew system without electrical analysis is an OMS.

The name carries history. In earlier decades "DMS" named the whole distribution control platform (the distribution counterpart of the transmission EMS); the current market uses "ADMS" for that integrated whole and retains "DMS" for the analysis layer it carries — sold either as the applications layer of an ADMS suite or as a standalone engineering-analysis system.

## Users & Context

The analysis serves two constituencies over the same model:

- **distribution engineers** — run system studies: load flow and voltage analysis, fault-current studies, protective-device coordination, capacitor placement and load-balancing optimization, contingency analysis, and long-range planning studies with proposed future configurations
- **operations staff and control-room operators** — use the analysis operationally: check voltage and capacity limits before executing a switching action, locate faults from field-measured fault currents, evaluate restoration plans that re-energize healthy sections, watch for overloads and voltage violations

Secondary users include planning staff (forecasting future loading and evaluating projects), protection engineers (settings libraries and coordination studies), and — where the DMS is embedded in a control-room platform — the same dispatchers who operate the ADMS.

The context spans "blue-sky" work (studies, optimization, planning) and event-driven work (fault location and restoration analysis during outages). At the standalone pole the system lives in the engineering department and feeds the utility's outage-management and GIS systems; at the integrated pole it lives in the control room beside SCADA and OMS on one network model.

## Core Model

### The Defining Core

```text
Utility's connected distribution network model
└── Electrical analysis computed on the model
    └── Operating / planning decisions supported by the results
```

Three properties. If any one is removed, the product is no longer recognizable as a DMS:

- **The utility's connected distribution network model** — the system's working subject is a connected electrical model of the utility's actual network: feeders, switches/reclosers/fuses, transformers, regulators and capacitors, conductors with impedances, phases, from the delivery point down to (in mature models) the meter. The model knows what is connected to what, so the analysis can reason about de-energized sections, alternative supply paths, and proposed configurations. It is the utility's own network, not an abstract test circuit, and it is maintained as the network's configuration changes. Without it, the product is a generic calculator or a map viewer.
- **Electrical analysis computed on the model** — power-flow-class computation at minimum: phase voltages, currents, and losses under a given network configuration. Mature products extend the same computational core to fault currents (short-circuit analysis), what-if contingency analysis, and optimized configurations. Without computation, the product is a model viewer.
- **Operating/planning decision support** — the analysis exists to answer the utility's questions: is a proposed switching action electrically safe, where is the fault, how can healthy sections be restored, where are overloads and voltage violations, what equipment placement reduces losses, how will load grow. Without this binding, the product is an engineering sandbox.

### Standard Capabilities

Mature products commonly carry the following. They make a modern DMS practical, but they are modules and extensions, not the definition — products ship subsets, and the analysis core works without them.

**The application suite on the power-flow core.** Distribution state estimation (reconciling available measurements into a consistent network state, flagging bad data, estimating unmeasured quantities); fault location analysis (predicting probable fault points from relay-measured fault currents); fault location, isolation, and service restoration (FLISR — after a protective-device lockout, identifying the faulted section and formulating a plan to isolate it and restore healthy sections via tie points, checking feeder capacity, voltage limits, and safety constraints); loss-of-voltage monitoring and response; Volt/VAR optimization (adjusting regulators and capacitor controls for voltage conformance and loss reduction); short-term load forecasting and load estimation; contingency analysis (the electrical consequence of losing a device or section); capacitor placement and load-balancing optimization; protective-device coordination and settings management; arc-flash analysis.

**Study mode.** The same analysis applied to a sandbox copy of the model — proposed switching sequences, future loads, planned projects — without touching the working state. Used for switching-plan validation, what-if analysis, and planning studies.

**Switch-order integration.** Analysis results rendered as proposed switching steps. In the semi-automatic posture the system creates a switch order that the operator must approve and execute; in the automatic posture the system executes it directly. The advisory posture — analysis informs a human decision — is the base case.

**Model sourcing and data inputs.** The model is typically derived from the utility GIS or exchanged in industry-standard formats, or built and maintained natively; model-validation tooling accompanies it. Analysis inputs commonly include SCADA measurements (where available), meter/AMI data and customer-information loads for load allocation, and DER data as model elements and restoration resources.

**Violation surfacing.** Overload and voltage-violation lists, visual maps of problem areas, and configurable alarms when computed conditions violate security limits.

### One Structure, Many Implementations

```text
Concept:      Connected network model
Realizations: GIS-derived import, industry-standard model exchange,
              native modeling environments

Concept:      Analysis state
Realizations: live SCADA measurements, meter/CIS-derived load allocation,
              user-specified study loads

Concept:      Decision output
Realizations: violation lists and maps, fault-location panels,
              proposed switch orders, coordination reports, planning studies
```

A reader who has only seen one implementation — for example, a control-room DMS fed continuously by SCADA — should still recognize a standalone engineering-analysis system running studies on an imported feeder model as the same Type.

## How It Works

The characteristic loop is the analysis cycle:

```text
Maintain the model (import/derive from GIS or native editing; validate connectivity, phasing, parameters)
→ establish the analysis state (SCADA measurements where available, meter/CIS load allocation, or study loads)
→ compute (power flow → voltages/currents/losses; short circuit → fault currents; contingency → what-if results)
→ surface results against limits (overloads, voltage violations, coordination problems, fault locations)
→ decide and act (operator executes switching — often via a switch order the analysis produced;
   automation executes in automatic mode; planners adopt the configuration into a project)
```

Three recurring workflows dominate:

**Pre-switching validation.** Before a switching action (planned maintenance or storm response), the proposed configuration is analyzed: the resulting voltages, loading, and capacity of the receiving feeder are computed, and violations are flagged before any device is operated. In integrated deployments this check can be configured as a required gate before device operation.

**Fault response analysis.** When a protective device locks out, fault-location analysis narrows the probable faulted section from measured fault currents; FLISR formulates an isolation-and-restoration plan — analyzing adjacent feeders' and DERs' capacity to pick up load — and presents it as a switch order for operator approval, or executes it automatically depending on the utility's posture.

**Engineering studies and planning.** Engineers run coordination studies against the settings library, optimize capacitor placement and load balancing, test contingency scenarios, and build planning studies: forecast future loading, represent planned changes as projects, and analyze their voltage and capacity impact.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Network model viewer / one-line diagram

The primary surface: a schematic (often over a geographic background) of feeders and devices, with computed results overlaid.

- typical information: feeder topology, device states, computed voltages/currents/losses, violation markers, fault-location indicators
- primary actions: navigate the model, select devices, run traces, toggle result layers, switch between working and study models

### Analysis workbench

Where computation is driven.

- typical information: study definition (configuration, loads, scenario), solver options, run status
- primary actions: run power flow / fault study / contingency, modify the study configuration, compare alternatives

### Results and violation surfaces

- typical information: overload and voltage-violation lists, visual maps of issues, phase-level results, loss summaries
- primary actions: filter and acknowledge violations, drill into a device's results, export results

### Fault-location and restoration panels

- typical information: probable fault section, proposed isolation and restoration steps, capacity checks on alternative supply paths
- primary actions: review the proposal, generate a switch order, approve and execute (semi-automatic) or monitor automatic execution

### Coordination and settings surfaces

- typical information: protective-device settings library, coordination curves, coordination problems found on the network
- primary actions: adjust settings, re-run coordination, manage the settings library

### Planning and forecasting surfaces

- typical information: forecast loads by location, projects representing planned changes, before/after comparisons
- primary actions: create study scenarios, attach proposed configurations, produce study reports

## Important Rules / Behaviors

- **The model is the foundation.** Analysis quality depends on model quality — connectivity, phasing, and electrical parameters. Model preparation and validation are treated as a major ongoing task, and results are only as good as the maintained model.
- **Analysis proposes; execution belongs elsewhere.** The DMS computes what would happen; the switching itself is executed by the operator through the SCADA/control layer, or by automation under the utility's chosen posture. The semi-automatic pattern — the system produces a switch order, the operator approves and executes it — is a first-class operating mode, not a fallback.
- **Study and working states are separated.** What-if analysis and planning run on sandbox copies of the model; proposed configurations do not alter the working model until adopted.
- **Results are limit-relative.** The analysis is organized around violations of defined limits (equipment ratings, voltage bounds, protection coordination), not raw numbers alone.
- **Inputs are heterogeneous by design.** The same analysis core runs on live SCADA measurements, on meter/customer-data-derived loads, or on user-specified study loads; the absence of one input source degrades accuracy, not the product.
- **Safety constraints bind restoration logic.** Where the DMS is embedded in a control-room platform, restoration proposals respect safety documents, tags, and crew assignments recorded on devices; a standalone DMS supports the same discipline by leaving execution to the utility's operational process.

## Variants

- **Packaging** — the DMS applications layer inside an ADMS suite (the dominant current form, on one network model beside SCADA and OMS) versus a standalone engineering-analysis system (common at cooperatives and municipal utilities, feeding the utility's OMS and GIS as separate products).
- **Automation posture** — advisory (analysis informs people) → semi-automatic (proposals as switch orders requiring operator approval) → supervised automatic execution (the system executes within limits).
- **Data posture** — continuously SCADA-fed real-time analysis; offline/asynchronous studies; meter-data-enriched load allocation; pilot-stage real-time bridges connecting engineering models to live grid data.
- **Customer tier** — enterprise platforms for large utilities versus standalone tools for co-ops and public-power utilities.
- **Model scope** — feeder/primary-level models versus extension into secondary services down to the meter.
- **DER depth** — DERs as model elements and restoration resources versus deeper DER orchestration, which belongs to DER management systems.
- **Regional practice** — unbalanced three-phase modeling conventions, protection philosophies, and planning-study traditions differ by country and utility; products adapt through configuration.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Advanced Distribution Management System / ADMS | integrated superset platform | the ADMS adds real-time telemetry on the model, supervisory control of field devices, and the operational event loop; the DMS is the analysis layer it commonly carries — and can exist without any of that real-time machinery |
| SCADA | substrate | point-based telemetry, alarming, and remote control organized as points and devices, with no connected network model or analysis required; the DMS consumes SCADA measurements where available |
| Outage Management System / OMS | sibling / adjacent | centers the outage-response loop (events → prediction → crews → restoration → reliability records); the DMS centers electrical computation; fault-location and restoration analysis feed the OMS's response work |
| Energy Management System / EMS | same pattern, transmission | the same network-analysis layer applied to the transmission grid, with a generation-to-load balancing center; the DMS is the distribution instance |
| DERMS | sibling layer | centers the DER fleet (registry, visibility, dispatch within grid constraints); the DMS analyzes the network with DERs as model elements and inputs |
| Utility GIS | model source | holds the as-built georeferenced network model of record; the DMS derives a working electrical model from it and computes on it; no computation in the GIS |
| Grid Operations Platform | family umbrella | a market umbrella over the control-room estate (SCADA, EMS, ADMS/DMS, OMS, DERMS); the DMS is the analysis member of that family |

The most important boundary is against the ADMS: the analysis layer is what a DMS is; real-time network operations are what make an ADMS more. The second is against SCADA: a connected model with computed electrical results, not points and commands.

## Representative Products

- SurvalentONE DMS application family (Distribution Power Flow / State Estimation, FLISR & Loss of Voltage, Volt/VAR Optimization, load forecasting) — Survalent
- Milsoft Engineering Analysis (WindMil, LightTable, LandBase) — Milsoft Utility Solutions
- AspenTech OSI ADMS (DMS as the advanced-distribution-management layer of the integrated suite) — AspenTech
- Oracle Utilities Network Management System (advanced distribution management applications) — Oracle

The defining core was checked against narrower and adjacent structures — point-based SCADA, call-center-only OMS, and pure planning calculators — to avoid defining the Type by any single packaging form.

## Sources

Research date: **2026-09-10**

- Survalent — Products catalog; SurvalentONE Distribution Power Flow and Distribution State Estimation; SurvalentONE FLISR & Loss of Voltage — https://www.survalent.com/products/ , https://www.survalent.com/analysis-forecasting-applications/distribution-power-flow/ , https://www.survalent.com/flisr-loss-of-voltage/
- Milsoft Utility Solutions — Engineering & Operations; Engineering Analysis — https://www.milsoft.com/ , https://www.milsoft.com/engineering-operations/engineering-analysis/
- AspenTech — AspenTech OSI Advanced Distribution Management System product page — https://www.aspentech.com/en/products/dgm/aspentech-osi-advanced-distribution-management-system
- Oracle — Utilities Network Management System documentation library (Release 25.12) — https://docs.oracle.com/en/industries/energy-water/network-management-system/index.html

> Sourcing limitation: official product documentation was directly accessible for the four vendors above (product/catalog pages; Oracle's documentation library index). Vendor sites for CYME/Eaton, Hitachi Energy, Siemens, and Schneider Electric could not be reached from the research environment and were not used as evidence; the engineering-analysis pole beyond the sampled standalone product is therefore described only at market-corroboration strength. Workflow details verified in only one vendor's materials (for example, semi-automatic versus automatic FLISR execution, state-estimation add-on packaging) are described as product postures, not industry-uniform rules. Precise numeric limits and defaults are intentionally omitted.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
