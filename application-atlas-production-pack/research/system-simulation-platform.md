# Research Notes — System Simulation Platform

Research date: 2026-09-10
Slug: `system-simulation-platform` (DIRECTORY.md §16 Engineering, Manufacturing & Industrial, between "CAE / Engineering Simulation" and "MBSE Platform")

## Research Goal

Understand what a System Simulation Platform actually is as an Application Type: what its core model objects are, what "system simulation" means as a user activity, how models are composed and executed, what results users work with, and where the Type's boundaries lie against CAE / Engineering Simulation, MBSE Platform, Digital Twin Platform, PLC Programming Environment, and Software Architecture Modeling.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: this is the "1D / system-level / multi-domain dynamics" simulation Type — modeling an engineered system as interconnected behavioral components (mechanical, electrical, hydraulic, thermal, control) and computing its dynamic response over simulated time.
- Nearest neighbors: CAE (3D continuum FEA/CFD), MBSE (architecture-of-record modeling), Digital Twin Platform (operational synchronized replicas), PLC Programming (control code), Software Architecture Modeling (software structure).
- Pre-hung flag from the mbse-platform pass (2026-09-09): proposed seam "architecture-of-record vs dynamics-analysis-of-design"; MBSE tools export model fragments to simulation tools (Simulink exporters, FMI/FMU, ModelCenter bridges) — to be confirmed or corrected from this side's own sample.
- Sibling context: cae-engineering-simulation (2026-09-06) defined CAE as geometry+physics over a discretized representation; digital-twin-platform (2026-09-07) defined the twin instance + model layer + counterpart synchronization + twin-space access; robotics-engineering-platform (2026-09-09) and scada (2026-09-09) are adjacent but distinct subjects.

## Research Questions

1. What is the core model object? What does a "system model" consist of?
2. How is component behavior expressed — causal block diagrams (signal flow), acausal equation-based physical components, pre-built 1D component libraries?
3. What does running a simulation involve (solvers, time, initialization)?
4. How do multiple physical domains combine in one model?
5. What results do users get and how do they analyze them?
6. What role do component libraries play?
7. How do users run studies: parameter sweeps, calibration, optimization?
8. What exchange standards exist (FMI/FMU, Modelica, SSP) and what do they connect to?
9. What deployment paths exist (code generation, real-time, HIL, digital twins)?
10. Where are the boundaries vs CAE, MBSE, digital twin, PLC/embedded code, software modeling?
11. Historical check: would pre-GUI, single-domain, pre-Modelica tools (SPICE-class circuit simulators, analog computers, early block-diagram simulators) still fit the definition?

## Representative Products

Selected for market representation, documentation quality, different modeling philosophies, and different customer layers:

| Product | Vendor | Philosophy / pole | Evidence tier reached |
|---|---|---|---|
| Simulink (+ Simscape) | MathWorks | causal block diagram + physical networks; Model-Based Design; enterprise | Tier 2 (official pages via search snippets; direct fetch 403) |
| Simcenter Amesim | Siemens | 1D multi-physics validated component libraries; PLM-suite embedded | Tier 2 (official product page, direct) |
| Dymola | Dassault Systèmes | acausal equation-based (Modelica); open modeling environment | Tier 2 (official product pages via search result of 3ds.com) |
| Ansys Twin Builder | Ansys (now Synopsys) | multi-domain systems modeler + solver + reduced-order models from 3D | Tier 2 (official product page via search result) |
| OpenModelica | Open Source Modelica Consortium | open-source Modelica environment; academic + industrial | Tier 1 (official site + full User's Guide) |

Ecosystem context sources (Tier 1): Modelica language (Modelica Association), FMI standard (Modelica Association Project). Historical anchor (Tier 3): SPICE history (Laurence Nagel's first-person account; IEEE technav summary).

## Sources

- MathWorks — Simulink product page & product description (mathworks.com/products/simulink.html; de.mathworks.com/help/simulink/gs/product-description.html) — retrieved via search snippets 2026-09-10 (direct fetch 403)
- MathWorks — Simscape page + "Real-Time Simulation of Physical Systems Using Simscape" technical article (mathworks.com) — via search snippets 2026-09-10
- Siemens — Simcenter Amesim product page (siemens.com/en-us/products/simcenter/systems-simulation/amesim/) — fetched 2026-09-10
- Siemens — Simcenter Amesim ebook PDF (plm.automation.siemens.com media) — via search snippets 2026-09-10
- Dassault Systèmes — Dymola product page, Latest Release, Model Design Tools (3ds.com/products/catia/dymola) — via search result of official pages 2026-09-10
- Ansys — Twin Builder product page (ansys.com/en-in/products/digital-twin/ansys-twin-builder; ansys.synopsys.com mirror) — via search result 2026-09-10
- OpenModelica — openmodelica.org + User's Guide v1.28-dev TOC (openmodelica.org/doc/OpenModelicaUsersGuide/latest/) — fetched 2026-09-10
- Modelica Association — modelica.org language page — fetched 2026-09-10
- FMI Standard — fmi-standard.org — fetched 2026-09-10
- Laurence W. Nagel, "The Life of SPICE" (princetonacm.acm.org / omega-enterprises.net); IEEE Technology Navigator SPICE topic — fetched via search 2026-09-10

Access limitations: mathworks.com returned 403 on direct fetch (2 attempts, abandoned); Simulink evidence is Tier 2 via official-page snippets — Simulink-specific claims are kept at commonality strength, not precise operational detail. One Siemens URL 404 and one timeout before the correct URL was found; final Amesim fetch succeeded. OpenModelica User's Guide versioned URL 404 once; `latest` URL succeeded.

## Product Observations

### MathWorks Simulink (+ Simscape) — evidence layer A (official pages, via snippets)

- Self-description: "Simulink is a block diagram environment for multidomain simulation and Model-Based Design. It supports system-level design, simulation, automatic code generation, and continuous test and verification of embedded systems. Simulink provides a graphical editor, customizable block libraries, and solvers for modeling and simulating dynamic systems. It is integrated with MATLAB." (product description)
- Simulation engine: "fixed-step and variable-step ODE solvers"; simulation results exportable to MATLAB for further analysis.
- Multidomain composition: "Combine electrical, mechanical, thermal, hydraulic, and software components in one system model"; "Connect physics-based, reduced-order, and data-driven plant models with software and control logic"; "Build modular, hierarchical models that scale from components to full systems."
- Closed-loop framing: "Simulate plant, environment, and software together to assess closed-loop behavior."
- Interchange: "Integrate third-party plant and component models using FMUs."
- Deployment: desktop simulation, SIL, PIL, HIL workflows; "generates production-quality C, C++, CUDA, PLC, Verilog, and VHDL code."
- Simscape (physical modeling): "modeling and simulating multidomain physical systems"; technical article confirms hydraulic, electrical, mechanical, pneumatic, thermal elements; real-time preparation workflow (variable-step reference → fixed-step solver → fixed-cost simulation → real-time target).

### Siemens Simcenter Amesim — evidence layer A (official product page, direct)

- Self-description: "Simcenter Amesim is a mechatronic systems simulation platform that allows design engineers to virtually assess and optimize the systems' performance."
- Purpose framing: "virtual testing environment lets you discover optimal solutions before building physical prototypes"; "from early specification to subsystem testing" (sibling page).
- Libraries: "comprehensive multi-physics libraries with validated components"; "ready-to-use multiphysics libraries combined with application and industry-oriented solutions"; "extensive ready-to-use examples... comprehensive documentation and demo models."
- Analysis: "powerful exploration tools and advanced post-processing capabilities to uncover optimal system configurations."
- Positioning in the toolchain: "highly efficient 1D multiphysics system simulation"; "efficiently interfaces with many 1D and 3D computer-aided engineering (CAE) software solutions"; "quickly derive and export models for standard real-time targets by providing a consistent and continuous model-in-the-loop (MiL), software-in-the-loop (SiL) and hardware-in-the-loop (HiL) capable framework."
- Interop: "From Simulink to FMI and across the Simcenter portfolio"; ebook: "couple the software with major CAE, CAD and controls software packages, interoperate it with the Functional Mockup Interface (FMI), Modelica"; "optimize the interactions between mechanical, hydraulic, pneumatic, thermal, electric and electronic systems."

### Dassault Systèmes Dymola — evidence layer A (official pages, via search result)

- Self-description: "Dymola, Dynamic Modeling Laboratory, is a complete tool for modeling and simulation of integrated and complex systems for use within automotive, aerospace, robotics, process and other applications"; "Multi-Engineering Modeling and Simulation based on Modelica and FMI"; "a complete environment for model creation, testing, simulation and post-processing."
- Openness pole: "The Dymola environment is completely open in contrast to many modeling tools that have a fixed set of component models and proprietary methods for introducing new components. Users of Dymola can easily introduce components that match the user's own and unique needs... from scratch or by using existing components as templates."
- Solver technology: "unique and outstanding performance for solving differential algebraic equations (DAE). The key to high performance and robustness is symbolic manipulation which also handles algebraic loop and reduced degrees-of-freedom caused by constraints... enable real-time Hardware-in-the-Loop Simulations (HILS)."
- Model experimentation (Model Design Tools page): "Model experimentation involves running simulations for various combinations of parameters to determine the modeled system's properties... Few models are simulated only once. In fact, running several simulations with different parameters and comparing the results is one of most fundamental user tasks."
- Model calibration: "measured data from a real device is used to tune parameters such that the simulation results are in good agreement with the measured data."
- Design optimization: "tune parameters such that the system behavior is improved... criteria values are usually derived from simulation results, e.g., the overshoot or rise time of a response, but they can also be derived by frequency responses or eigenvalue analysis."
- Model management: "encryption of models, version control from Dymola (CVS, Subversion and GIT) and utilities for checking, testing and comparing models. Regression testing (checking simulation results against known [results])..."
- Interop: "full support of the FMI standard, Python scripting or use the Simulink interface"; release notes: parameter sweep with grouping, integrated calibration UI, Monte-Carlo simulation, dynamic optimization of FMUs, Modelica Standard Library 4.1.0, FMI co-simulation technology.

### Ansys Twin Builder — evidence layer A (official product page, via search result)

- Self-description: "Ansys Twin Builder is an open solution that allows engineers to create simulation-based digital twins"; the twin is "a connected, virtual replica of an in-service physical asset — in the form of an integrated multidomain system simulation."
- Modeler: "Multidomain Systems Modeler — Compose your system using multiple domains and languages. Create hierarchical schematics of complex power electronic circuits and multidomain systems. Model with standard languages and exchange formats."
- Libraries: "Extensive 0D Application-Specific Libraries."
- Solver: "Multidomain Systems Solver with Integrated Post-Processing... adaptive time-step controls and sophisticated solver synchronization... efficient and accurate simulation of continuous-time, discrete-time and analog/mixed-signal behaviors... multi-run analyses can be executed in parallel."
- 3D bridge: "Twin Builder couples with Ansys' physics-based simulation technology to bring the detail of 3D simulations, as reduced order models (ROMs), into the systems context."
- Deployment-side capabilities (twin side, not core simulation): XIL Integration, Embedded Software Integration, Rapid HMI Prototyping, System Optimization Tools, IIoT Connectivity, Twin Deployer (V&V, parametric sweeps on twins and FMUs), Hybrid Analytics (calibration combining physical and virtual sensors).

### OpenModelica — evidence layer A (official site + User's Guide)

- Self-description: "an open-source Modelica-based modeling and simulation environment intended for industrial and academic usage."
- User's Guide structure (direct observation of the full TOC):
  - OMEdit — OpenModelica Connection Editor: "Modeling a Model", "Simulating a Model", "2D Plotting", "Re-simulating a Model", "3D Visualization", "Animation of Realtime FMUs", "Interactive Simulation", "Debugger", "Install Library", "State Machines".
  - Solving Modelica Models: "Integration Methods", "DAE Mode Simulation", "Initialization", "Tearing", "Algebraic Solvers".
  - FMI: "FMI Export", "FMI Import - SSP"; OMSimulator with SSP (System Structure and Parameterization) support.
  - Studies: "Optimization with OpenModelica" (dynamic optimization, parameter sweep via OMOptim), "Parameter Sensitivities" (OMSens), "System Identification", "Data Reconciliation".
  - Linearization (via OMMatlab); scripting APIs (Python/Matlab/Julia); OMNotebook; package management for libraries; model encryption.
- The canonical loop is visible in the TOC ordering: model → simulate → plot → re-simulate → optimize/sensitivity → export.

### Ecosystem context — Modelica language & FMI standard — evidence layer A

- Modelica (Modelica Association): "a language for modeling of cyber-physical systems, supporting acausal connection of components governed by mathematical equations to facilitate modeling from first principles. It provides object-oriented constructs that facilitate reuse of models, and can be used conveniently for modeling complex systems containing, e.g., mechanical, electrical, electronic, magnetic, hydraulic, thermal, control, electric power or process-oriented subcomponents."
- FMI (Modelica Association Project): "a free standard that defines a container and an interface to exchange dynamic simulation models using a combination of XML files, binaries and C code, distributed as a ZIP file. It is supported by 280+ tools." Two modes: Model Exchange and Co-Simulation. Advisory committee spans the entire ecosystem (MathWorks, Siemens, Bosch, GM, VW, Volvo, Airbus, Boeing, Saab, DLR...). User quotes confirm the practice: Bosch — "preferred model exchange and co-simulation format... at system level enabling the exchange of models with internal and external partners using different modelling tools"; Saab — "tool neutral integration of simulation models from different technical disciplines."

### Historical anchor — SPICE — evidence layer C (Tier 3, first-person + IEEE)

- SPICE ("Simulation Program with Integrated Circuit Emphasis", UC Berkeley, released 1971/1973, SPICE2 1975): input as a circuit **netlist** (text description of interconnected components), **built-in device models** (diodes, BJTs, MOSFETs — "the user need only provide a set of model parameters"), analyses **DC, AC (small-signal), transient**; transient analysis = "numerical integration... solve the dynamical (differential equation) systems" with step control; outputs voltages/currents as functions of time. No GUI originally (punched cards, line printer); schematic capture and GUI added later. Public domain, which drove adoption.
- Interpretation for the historical check: the component-network + dynamic-simulation + trajectory-results core predates GUIs, multi-physics libraries, Modelica, and FMI by two decades. A definition requiring any modern machinery would exclude the Type's own ancestor.

## Cross-product Comparison

| Dimension | Simulink/Simscape | Simcenter Amesim | Dymola | Ansys Twin Builder | OpenModelica |
|---|---|---|---|---|---|
| Core artifact | block-diagram model (+ physical networks) | system sketch of 1D components | Modelica model (graphical + textual) | multidomain system schematic | Modelica model (graphical OMEdit + textual) |
| Behavior expression | causal blocks + acausal physical networks (Simscape) | pre-built validated 1D component libraries | acausal equations (Modelica), user-extensible | multi-domain components + standard languages/exchange formats | acausal equations (Modelica), user-extensible |
| Domain breadth | electrical, mechanical, thermal, hydraulic + software/control | mechanical, hydraulic, pneumatic, thermal, electric, electronic (mechatronic) | multi-domain (Modelica MSL + libraries) | multi-domain, power-electronics emphasis, 0D app libraries | multi-domain (MSL + open libraries) |
| Execution | fixed/variable-step ODE solvers | solver embedded; MiL/SiL/HiL framework | DAE solver with symbolic manipulation | multi-domain solver, adaptive time-step, parallel multi-run | integration methods, DAE mode, initialization, tearing |
| Results | scopes/plots; export to MATLAB | advanced post-processing, exploration tools | post-processing; criteria from results (overshoot, rise time, frequency response, eigenvalues) | integrated post-processing | 2D plotting, 3D visualization, re-simulation |
| Studies | (via MATLAB ecosystem) | exploration/optimization tools | parameter sweeps, Monte Carlo, calibration, design optimization | system optimization, multi-run | OMOptim, OMSens, system identification, data reconciliation |
| Interchange | FMU import (and export) | FMI, Modelica, Simulink coupling | full FMI, Simulink interface, Python | standard languages and exchange formats, FMUs | FMI export/import, SSP |
| Deployment path | code generation (C/C++/CUDA/PLC/Verilog/VHDL), SIL/PIL/HIL | real-time targets, MiL/SiL/HiL | real-time HILS | XIL, embedded software integration, twin deployment | FMI export; browser simulation; scripting |
| Suite embedding | MATLAB ecosystem | Simcenter / Teamcenter portfolio | 3DEXPERIENCE / CATIA | Ansys portfolio (+ IIoT platforms) | standalone open source |
| Openness | proprietary | proprietary | proprietary, open Modelica-based | proprietary | open source |

Cross-product commonalities (evidence layer B): every sampled product (1) composes a system model from components/blocks connected through ports, (2) executes it as a dynamic simulation over time with a numerical solver, (3) produces time-history results for analysis, (4) draws on reusable component libraries, (5) supports model exchange with other tools (FMI in all five), (6) offers studies beyond a single run (sweeps/optimization/calibration), (7) offers a path toward real-time or embedded use.

## Canonical Model — Four Abstraction Levels

### L0 — Defining Invariant

The smallest structure without which the product is not recognizable as a System Simulation Platform:

1. **The system model as the unit of work** — a user-composed model of an engineered system's dynamic behavior, built as a network of components/blocks, each carrying defined behavior (equations, transfer functions, lookup tables, pre-built physics), connected through ports that carry physical quantities or signals, with parameters. The model is a persistent, editable, re-runnable artifact.
2. **Dynamic simulation as the primary act** — executing the model over simulated time by numerical solution of the coupled dynamics (integration of the system's equations), under user-visible simulation settings (duration, solver, initialization).
3. **Trajectory results** — time histories of model variables as the primary output, inspected as plots/scopes and used as engineering evidence.

Jointly-held load-bearing argument:
- 1 alone = a diagramming/CAD tool (or an equation editor) — nothing computes.
- 2 alone = a numerical solver library — no composed system to solve.
- 3 alone = a plotting tool.
- 1+2 without 3 = simulation whose results cannot be observed — practically useless.
- 1+3 without 2 = static/transfer-function analysis without dynamic execution.
- 2+3 without 1 = a numerical computing environment (scripts + plots) — the composed system model as a first-class artifact is exactly what is missing; this is the MATLAB-vs-Simulink line.

### L1 — Common Mature Structure

Present in essentially all mature modern products, expected by the market, but not required to recognize the Type:

- **Component libraries** — domain libraries of validated/pre-built components (multi-physics: mechanical, electrical, hydraulic, pneumatic, thermal; application-specific); customizable block libraries; the Modelica Standard Library ecosystem.
- **Multi-domain composition** — combining several physical domains plus control/software behavior in one model ("mechatronic"/"multidomain" is the standard self-vocabulary).
- **Hierarchical/modular models** — components composed into subsystems composed into systems.
- **Solver choice and settings** — fixed-step vs variable-step, stiff-system handling, initialization.
- **Studies machinery** — parameter sweeps, batch/multi-run, calibration against measured data, design optimization, sensitivity analysis.
- **Model exchange** — FMI/FMU import/export (280+ tools); co-simulation; tool-to-tool coupling (Simulink↔Amesim↔Dymola↔CAE).
- **Linearization / frequency-domain analysis** — deriving small-signal models from the dynamic model.
- **Real-time path** — preparing/deriving models for real-time targets, SIL/PIL/HIL/XIL workflows.
- **Post-processing** — plotting, comparison across runs, export of results.

### L2 — Variant / Optional Structure

Depends on segment, philosophy, deployment, business model:

- **Modeling paradigm** (the big philosophical axis): causal block diagrams (explicit signal direction; control-theory heritage) vs acausal physical-component networks (equation-based, first-principles; Modelica heritage) vs curated 1D component libraries (pre-solved physics; fast authoring, less openness). Products mix these (Simulink+Simscape carries both causal and acausal).
- **Domain emphasis** — power electronics/electrification, automotive drivetrain/thermal, aerospace, process, machinery.
- **Deployment posture** — pure design-time analysis vs Model-Based Design (model as the source of production embedded code) vs digital-twin deployment (model running against operational data).
- **Openness** — open standard language + open-source implementation vs proprietary libraries and formats; model encryption/IP protection appears on both sides.
- **Suite embedding** — standalone workbench vs embedded in a PLM/CAE/simulation portfolio with shared data.
- **3D coupling depth** — one-way data exchange with CAE vs reduced-order models embedded as system components.
- **Textual vs graphical authoring** — netlist/text-first vs schematic-first (both exist; most modern products offer both).

### L3 — Vendor-specific Structure

Stays in Research Notes: Twin Builder's ROM toolchain, Hybrid Analytics, Twin Deployer, IIoT connectors; Amesim's Simcenter/Teamcenter/Flomaster/System Analyst integration; Dymola's symbolic DAE manipulation as a differentiator, TIL Suite library packaging, GitHub library browsing; Simulink's MATLAB language integration and specific codegen targets (C/C++/CUDA/PLC/Verilog/VHDL), vECU/virtual vehicle; OpenModelica's specific tools (OMOptim, OMSens, OMNotebook, OMEdit debugger, BaseModelica, PDEModelica).

## Vendor-specific Findings

- Twin Builder is *marketed* as a digital-twin product; its modeling/simulation core is a multidomain systems modeler + solver. The twin-deployment layer (Twin Deployer, IIoT connectivity, Hybrid Analytics) belongs to the digital-twin side of the seam. Its own words: the twin is "in the form of an integrated multidomain system simulation" — the system simulation is the substance.
- Amesim's page uses the exact leaf vocabulary: "System simulation platform" is a named Siemens capability ("Simcenter Systems offers... multiphysics system simulation platforms to model, run and analyze complex systems and components"). Confirms the market names this Type.
- Dymola's openness statement ("in contrast to many modeling tools that have a fixed set of component models") is evidence that fixed-library vs open-modeling is a real market axis, not a hypothetical one.
- Simulink's Model-Based Design framing extends the Type toward embedded software development (code generation, vECU) — a posture, not the core.
- "Platform" in the leaf name: vendors use it loosely (Amesim self-labels "platform"; Dymola self-labels "complete tool"). Single-tool products are in-Type; "platform" is not a structural requirement.

## Boundary Findings

1. **vs CAE / Engineering Simulation** (processed 2026-09-06): CAE = computational model of a physical design scenario (geometry + material properties) solved over a *discretized spatial representation* (mesh); System Simulation = system model as a *network of lumped/behavioral components* with no spatial discretization requirement. The market's own vocabulary holds the seam: Amesim — "interfaces with many 1D and 3D CAE software solutions"; Twin Builder — "bring the detail of 3D simulations, as reduced order models (ROMs), into the systems context." The ROM/FMI bridge is the seam made visible. Remove the component-network composition and require geometry+mesh → CAE.
2. **vs MBSE Platform** (processed 2026-09-09) — DISCHARGES the mbse pass's forward flag from this side: keep-both RATIFIED. Seam confirmed as proposed: MBSE = the system *architecture* model as system of record (requirements/structure/behavior elements, language-governed); System Simulation = the *dynamic behavior* model as the unit of work, executed over time. The bridge is exactly where the mbse pass predicted: MBSE tools export model fragments to simulation tools; from this side, all five sampled products support FMI import/export, and Dymola/Simulink/Amesim explicitly interoperate with MBSE-adjacent tooling. The FMI standard's own framing ("exchange dynamic simulation models... 280+ tools") confirms the simulation side of the bridge. Neither side subsumes the other.
3. **vs Digital Twin Platform** (processed 2026-09-07): twin platform = persistent twin instance per physical counterpart + counterpart synchronization + twin-space access surface; System Simulation = design-time behavioral model executed over simulated time. Straddle case documented: Twin Builder builds "simulation-based digital twins" — its simulation core is this Type; its twin instance/deployment/IIoT layer is the twin platform Type. A system-simulation model can *become* a twin's model, but synchronization to a physical counterpart is not required for the Type.
4. **vs PLC Programming Environment / embedded development**: the plant/system behavioral model vs the control-logic artifact deployed to controllers. Code generation from system models (Simulink PLC/Verilog/VHDL targets) is a bridge capability; authoring, structuring and downloading control programs is the PLC/embedded side. Model-Based Design straddles deliberately (plant model + controller model in one environment).
5. **vs Software Architecture Modeling** (§12): same network-diagram surface, different subject and execution — software component structure vs physical/behavioral dynamics solved by numerical integration. A system-simulation model has states, differential equations and solvers; a software architecture model has structure and (optionally) semantics but no dynamic trajectory as its primary output.
6. **vs numerical computing environments** (MATLAB-class, not a directory leaf): scripts/functions + numerical solvers + plots without a composed system-model artifact. Simulink exists precisely as the composed-model layer over MATLAB. Useful articulation of why "the model is a first-class persistent artifact" is load-bearing.
7. **vs circuit simulators (SPICE-class)**: single-domain ancestors satisfying the L0 core. Not a separate directory leaf; treated as historical/adjacent specialization. If a circuit-simulator leaf were ever added, the seam would be domain breadth + cross-domain coupling intent.

## Uncertainties

- Simulink evidence is Tier 2 (official-page snippets; direct fetch 403). Simulink-specific operational details (exact solver names, FMU export scope per release) are not asserted.
- Ansys Twin Builder evidence is from the product page (marketing-weighted); no Tier-1 help-center access. Its modeling/simulation core claims are corroborated by the page's capability list, but workflow detail is not asserted.
- Dymola evidence is from official product pages retrieved via search; the User's Guide itself was not fetched. Workflow claims (calibration, sweeps) are quoted from vendor pages, not exercised.
- The exact boundary of "platform" vs "tool" in market vocabulary is fuzzy (see Vendor-specific Findings); treated as non-structural.
- Historical breadth beyond SPICE (analog computers, bond graphs, early block-diagram simulators) is reasoned, not separately sourced; kept out of precise claims.

## Final Synthesis

A System Simulation Platform is the engineering application whose unit of work is a **composed behavioral model of an engineered system** — a network of components carrying defined dynamics, connected through ports, parameterized — and whose defining act is **executing that model as a dynamic simulation over simulated time** to produce **trajectory results** used as engineering evidence. Around this core, mature products add: multi-domain component libraries, hierarchical composition, solver machinery, studies (sweeps/calibration/optimization), model exchange (FMI), linearization, and real-time/embedded paths. The Type's philosophical variants (causal block diagram vs acausal equation-based vs curated 1D libraries) change how behavior is expressed, not what the Type is. The Type sits between CAE (3D continuum physics), MBSE (architecture of record), the digital twin (operational synchronized replica), and embedded/PLC development (control code artifacts) — with FMI/FMU and ROM/code-generation bridges as the visible seams.
