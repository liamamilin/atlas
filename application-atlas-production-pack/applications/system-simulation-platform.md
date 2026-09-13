# System Simulation Platform

## Overview

A **System Simulation Platform** is an engineering application for modeling the dynamic behavior of an engineered *system* — a machine, vehicle, plant, powertrain, circuit, or process composed of mechanical, electrical, fluid, thermal, and control/software parts — and computing that behavior over simulated time, before physical hardware exists.

The defining core is small:

```text
System model (a composed network of behavioral components)
    → executed as a dynamic simulation over simulated time
        → producing trajectory results (how variables evolve)
```

Everything else commonly associated with the category — multi-physics component libraries, parameter sweeps, model calibration, model exchange standards, real-time and hardware-in-the-loop workflows — is standard capability that mature products carry, not what makes the product a system simulation platform.

The Type occupies the "system level" of engineering simulation: where a CAE tool discretizes a *geometry* and solves physical fields over it, a system simulation platform composes a *network of components* and solves the coupled dynamics of the whole. Where an MBSE platform records the *architecture* of a system (requirements, structure, interfaces), a system simulation platform holds and executes its *behavior*.

## Users & Context

Primary users are engineers who design or integrate dynamic systems:

- **system and integration engineers** — compose subsystem models into a full-system model to check that the parts work together
- **control engineers** — model the plant (the physical system being controlled) and design controller behavior against it in closed loop
- **domain engineers** (mechanical, electrical, hydraulic, thermal) — model their subsystem and study its behavior under realistic loads and boundary conditions supplied by other domains
- **simulation/CAE specialists** — build and maintain reusable model libraries, run studies, calibrate models against test data

Typical contexts: automotive (powertrain, braking, thermal management, electrification), aerospace, energy and process plants, industrial machinery, robotics, power electronics. The common situation is that physical prototypes are expensive or unavailable early, so the system's behavior must be assessed virtually — sizing components, tuning controllers, and trading off designs before anything is built.

Secondary users include embedded-software teams (who consume plant models to test control software) and test engineers (who supply measured data used to calibrate models).

## Core Model

### The Defining Core

```text
System model
└── Components (each carrying defined behavior)
    └── connected through Ports
        └── with Parameters
            → executed as a Simulation over simulated time
                → Results: time histories of model variables
```

- **System model** — the central artifact. A persistent, editable, re-runnable model of one engineered system's dynamic behavior. It is not a drawing (nothing is computed), not a script (the system structure is explicit, not buried in code), and not a single equation (it is a composition of many interacting parts). The model outlives any single simulation run and is iterated on over weeks, months, or the life of a program.
- **Component** — a part of the system carrying defined behavior: a physical element (valve, motor, battery, beam, heat exchanger), a signal-processing or control element (filter, PID controller, state machine), or an interface element (sensor, source, load). Behavior is expressed as equations, transfer functions, lookup tables, or pre-built physics packaged in the component.
- **Port and connection** — components interact only through ports. A connection between ports carries either a *signal* (a value flowing in one defined direction) or a *physical quantity pair* (effort and flow — voltage/current, force/velocity, pressure/flow, temperature/heat) exchanged between components according to the domain's physics. Ports constrain what may connect to what: a hydraulic port does not connect to an electrical one except through a transducer component.
- **Parameter** — the numbers that make a model a specific system rather than a generic one: a gear ratio, a pipe diameter, a motor constant, a controller gain. Parameters are the primary levers of iteration; most studies consist of re-running the same model with different parameter values.
- **Simulation** — the act of executing the model: the platform assembles the coupled dynamics of all components and numerically integrates them from an initial state over a user-specified time span. Simulation time is decoupled from wall-clock time — a millisecond of system behavior may take seconds of computing, or vice versa.
- **Results** — time histories of chosen model variables (positions, pressures, currents, temperatures, speeds, control signals), inspected as plots and scopes, compared across runs, and exported for further analysis. Results are the product's evidence: they are what design decisions are made against.

### Standard Capabilities of Mature Products

These are carried by essentially all mature products and are what make the core practical, but they do not define the Type:

- **Component libraries** — curated, validated collections of pre-built components organized by domain (mechanical, electrical, hydraulic, pneumatic, thermal, control, signal) and often by application (batteries, brakes, HVAC, power electronics). Libraries are the main reason a team can assemble a system model in days instead of months.
- **Multi-domain composition** — combining several physical domains plus control/software behavior in one model, so cross-domain interactions (an electric motor driving a hydraulic pump through a shaft, controlled by software) are captured in a single simulation.
- **Hierarchical composition** — components grouped into reusable subsystems; a subsystem appears as a single component at the level above.
- **Solver machinery** — choice of integration method (fixed-step vs variable-step), handling of stiff systems and algebraic constraints, initialization of consistent starting conditions, and solver settings that trade accuracy against speed.
- **Studies machinery** — running many simulations systematically: parameter sweeps, batch runs, calibration of parameters against measured test data, design optimization against criteria derived from results, sensitivity analysis.
- **Model exchange** — importing and exporting models in standard interchange formats (the Functional Mock-up Interface, FMU, is the dominant one, supported by a large tool ecosystem), so a component vendor's model can run inside a customer's platform and subsystem models from different teams can be integrated.
- **Linearization and frequency-domain analysis** — deriving small-signal or frequency-response views from the dynamic model, mainly for control design.
- **Real-time and embedded paths** — preparing or deriving models that run synchronized with wall-clock time on real-time targets (for hardware-in-the-loop testing), or generating production code from model behavior (most developed in the control/model-based-design pole).
- **Post-processing** — plotting, run-to-run comparison, and export of results.

### One Structure, Many Implementations

The core model is written conceptually. Products realize the same concepts in materially different ways — this is the Type's main philosophical axis:

```text
Concept:   component behavior
Realizations:
  - causal block with explicit input/output signal direction
  - acausal physical component governed by equations (direction of
    causality decided by the solver, not the modeler)
  - curated 1D component with pre-solved internal physics

Concept:   authoring surface
Realizations:
  - graphical schematic canvas
  - textual equation-based model language
  - both, kept synchronized

Concept:   model exchange
Realizations:
  - standard interchange containers (FMU)
  - direct tool-to-tool coupling
  - shared model language across vendors
```

A reader who has only seen one style — say, signal-flow block diagrams — should still be able to recognize an equation-based physical-modeling tool, or a library-of-validated-components tool, as the same Type.

## How It Works

### Compose the model

```text
Open or create a system model
→ drag components from domain libraries onto the canvas
  (or write/extend an equation-based component)
→ connect ports to assemble the system's structure
→ nest components into subsystems as the model grows
→ set parameters on every component
```

Composition is iterative and cumulative: models grow from a small skeleton (a motor, a load, a controller) toward full systems, and subsystems built once are reused across projects.

### Configure and run a simulation

```text
Set the simulation span (how much simulated time to cover)
→ choose or accept the solver and its settings
→ check or establish initial conditions
→ run
→ the platform assembles the coupled dynamics and integrates them
   step by step over simulated time
```

The run either completes or fails — failure is a normal, informative event (a solver that cannot converge usually points to a modeling problem: an inconsistent initial state, an impossible connection, an overly stiff combination of dynamics).

### Inspect results and iterate

```text
Plot chosen variables against simulated time
→ compare against expectations, requirements, or earlier runs
→ change parameters or structure
→ re-run
```

This compose → run → inspect → change loop is the working heart of the product. Product documentation across the researched sample describes re-running with different parameters and comparing results as among the most fundamental user tasks; a model is rarely simulated only once.

### Run studies

```text
Define a study over the model:
  - sweep a parameter across a range and compare outcomes
  - calibrate: adjust parameters until simulation matches measured data
  - optimize: tune parameters to minimize/maximize criteria
    computed from results (response time, overshoot, energy use)
→ execute the many runs (locally or in parallel)
→ inspect the comparison
```

Calibration closes the loop with the physical world: measured data from a real device tunes the model so its predictions can be trusted for the next design round.

### Exchange and deploy

```text
Export a subsystem or the full model as an interchange unit (FMU)
→ a partner or another team integrates it into their own platform
→ or: derive a real-time version for hardware-in-the-loop testing
→ or: generate controller code from the model (in the
     model-based-design pole)
```

Exchange is what makes the Type an ecosystem rather than an island: component suppliers deliver models, OEMs integrate them, and different disciplines' models meet in one simulation.

## Interfaces

Described conceptually; exact layout and naming vary by product.

### Model canvas (schematic editor)

The primary working surface.

- shows the system as connected component icons with ports
- primary actions: place component, connect ports, group into subsystem, navigate hierarchy

### Library browser

The palette of available behavior.

- domain and application libraries, searchable; custom and user libraries alongside
- primary actions: browse, search, drag onto canvas, inspect component documentation

### Parameter and property editors

Where a generic component becomes this system's part.

- per-component parameter forms; model-wide parameter lists; units
- primary actions: set value, define computed expressions, parameterize from scripts or data

### Simulation control

- simulation span, solver selection and settings, initialization
- primary actions: run, stop, re-run; interactive simulation in some products (changing inputs while the simulation runs)

### Results views

- plot windows of variables vs simulated time; scopes; run comparison; 3D animation of mechanical motion in some products
- primary actions: choose variables, overlay runs, export data

### Study managers

- sweep/batch definitions, calibration and optimization setups, sensitivity analyses
- primary actions: define parameter ranges or objectives, execute, review comparisons

### Textual model source

In equation-based products, the model's source is also a first-class surface: readable, editable, version-controllable equations alongside the graphical view.

## Important Rules / Behaviors

- **The model is the persistent artifact; runs are disposable.** Users accumulate, refine, version and reuse models; any individual simulation can be re-run or discarded. Model management (versioning, comparison, regression testing of results, access control) becomes significant at team scale.
- **Ports are a contract.** What a connection means is fixed by the ports' domain and type; the platform rejects or warns on incompatible connections. In physical (acausal) modeling, a connection asserts physical conservation (what flows out of one component flows into the other), not just data transfer.
- **Causality differs by paradigm.** In signal-flow (causal) modeling, the modeler decides what computes what: each block's output is a function of its inputs. In equation-based (acausal) modeling, components declare relations and the platform works out, per simulation, which variables are computed from which — the same physical model can be driven from either end.
- **Solver behavior is part of the result.** Step size, stiffness handling, and convergence settings affect both speed and accuracy; a failed or inaccurate run is a first-class outcome the user must diagnose, not a silent error. Real-time use adds a hard constraint: the computation for each step must fit within the step's wall-clock time, forcing accuracy/speed trade-offs.
- **Simulation time is not wall-clock time.** Except in real-time modes, simulated time advances as fast as the computation allows.
- **Results are only as trustworthy as the model.** The practice of calibrating models against measured data exists because component-library physics plus guessed parameters does not automatically match reality; validation against test data is a standing part of the workflow, not an afterthought.
- **Initial conditions matter.** A dynamic simulation starts from a state; establishing consistent initial conditions (especially in physical models with constraints) is a real step, and initialization failures are a common first obstacle for new modelers.

## Variants

- **By modeling paradigm** — signal-flow block diagrams (control-theory heritage; explicit direction of computation); equation-based physical modeling (first-principles components; the modeler describes *what*, the solver determines *how it computes*); curated 1D component libraries (pre-solved physics, fast authoring, vendor-maintained accuracy). Many products mix paradigms — block diagrams for control logic alongside physical networks for the plant.
- **By domain emphasis** — multi-physics generalists; poles specialized toward power electronics and electrification, automotive systems, fluid systems, thermal management, or process plants.
- **By deployment posture** — design-time analysis (studies and evidence); model-based design (the model is the source from which controller code is generated and through which software is verified); real-time/HIL (the model runs as a virtual plant for testing real controllers); digital-twin supply (the model becomes the substance of an asset's operational twin).
- **By openness** — open modeling language with multiple competing implementations and open-source poles; proprietary platforms with closed libraries; and mixed forms (proprietary tool, open interchange). Model protection (encryption) appears on both sides, since models are exchanged commercial assets.
- **By suite embedding** — standalone workbenches; products embedded in PLM/CAE/simulation portfolios where the system model shares data with CAD, 3D CAE, and test tools.

A variant remains a variant while the defining core — composed behavioral model, dynamic simulation, trajectory results — still describes it. When the artifact stops being an executable behavioral model (a pure architecture description, a static sizing calculator, a data dashboard), it has crossed into a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| CAE / Engineering Simulation | adjacent sibling | CAE solves physical fields over a *discretized geometry* (mesh); system simulation composes a *component network* with no spatial discretization requirement. The market's own vocabulary marks the seam: "1D" system simulation vs "3D" CAE, bridged by reduced-order models and data exchange |
| MBSE Platform | adjacent sibling | MBSE holds the system *architecture* as the record (requirements, structure, interfaces, language-governed elements); system simulation holds and executes the system's *dynamic behavior*. MBSE tools export model fragments into simulation tools; simulation models are exchanged back via standard interfaces — the bridge is the seam made visible |
| Digital Twin Platform | adjacent, straddled by some products | a digital twin is a persistent, synchronized replica of a *specific physical asset in operation*; a system simulation model is a design-time artifact executed over simulated time. A simulation model can become a twin's model, but counterpart synchronization and twin-space access are the twin platform's defining structures, not this Type's |
| PLC Programming Environment | adjacent | the control *program* that runs on industrial controllers vs the *plant/system model* used to study what the controller acts upon. Code generation from system models is a bridge capability; authoring and downloading control logic is the PLC side |
| Software Architecture Modeling | surface-similar | both draw boxes connected by lines, but the subject and execution differ: software component structure vs physical/behavioral dynamics solved by numerical integration. A system model has states, equations and trajectories; an architecture model does not |
| Robotics Engineering Platform | adjacent, domain-specific | authors and verifies *robot* behavior against a robot/cell model and carries it to real robot hardware; system simulation is domain-general and has no hardware-deployment terminus of its own |

The most important boundary is with **CAE / Engineering Simulation**, because vendors sell both and the word "simulation" is shared. The structural test: if the model's input is a geometry that gets meshed and physics solved over it, it is CAE; if the model is a network of behavioral components whose coupled dynamics are integrated over time, it is system simulation. Real products bridge the two (3D results reduced into system models), which is integration, not identity.

## Representative Products

- **MathWorks Simulink (with Simscape)** — the block-diagram environment for multidomain simulation and model-based design; physical-network modeling of electrical, mechanical, thermal, hydraulic systems alongside control logic
- **Siemens Simcenter Amesim** — mechatronic systems simulation built on validated 1D multi-physics component libraries, embedded in the Simcenter portfolio
- **Dassault Systèmes Dymola** — equation-based multi-engineering modeling on the Modelica language, with an open modeling environment and symbolic DAE solving
- **Ansys Twin Builder** — multidomain systems modeler and solver that also builds simulation-based digital twins, including reduced-order models from 3D physics
- **OpenModelica** — open-source Modelica-based modeling and simulation environment (industrial and academic)

These five were chosen because they represent the Type's main philosophical poles (causal block diagrams, acausal equation-based modeling, curated 1D libraries, multi-domain-plus-ROM integration, open source) and different customer layers (enterprise PLM suites to open-source community).

## Sources

Research date: **2026-09-10**

- MathWorks — Simulink product page and product description; Simscape pages; "Real-Time Simulation of Physical Systems Using Simscape" technical article — mathworks.com (retrieved via official-page excerpts; direct fetch was blocked)
- Siemens — Simcenter Amesim product page — siemens.com/en-us/products/simcenter/systems-simulation/amesim/
- Dassault Systèmes — Dymola product page, Latest Release notes, Model Design Tools — 3ds.com/products/catia/dymola
- Ansys — Twin Builder product page — ansys.com/products/digital-twin/ansys-twin-builder
- OpenModelica — openmodelica.org and OpenModelica User's Guide (latest) — openmodelica.org/doc/OpenModelicaUsersGuide/latest/
- Modelica Association — Modelica language — modelica.org/language/
- Modelica Association Project — Functional Mock-up Interface (FMI) standard — fmi-standard.org
- L. W. Nagel, "The Life of SPICE" (historical anchor for the Type's pre-GUI, single-domain ancestry); IEEE Technology Navigator, SPICE topic

> Sourcing limitation: direct fetches of mathworks.com were refused (403), so Simulink-specific evidence comes from official-page excerpts rather than full help-center articles; Simulink-specific operational details are therefore stated only at common-market strength. Ansys Twin Builder evidence is from the vendor product page (marketing-weighted); no help-center depth was reached. Precise solver names, numeric limits, and release-specific behaviors are intentionally not asserted in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
