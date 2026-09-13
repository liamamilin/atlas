# Semiconductor Design Platform

## Overview

A **Semiconductor Design Platform** is the software environment in which an integrated circuit — a chip — is designed, verified, and prepared for fabrication. The industry calls this domain electronic design automation (EDA); this document covers the chip-design side of it, as distinct from board- and system-level electrical design tools.

The defining structure of the Type has three parts that always appear together:

```text
The chip design held as corresponding representations
    (functional description → circuit realization → physical layout)
        + verification against electrical behavior and manufacturing reality
            (simulation + process-rule checking, findings gate progress)
                + a transformation flow ending in fabrication-ready
                  manufacturing data (mask data a wafer fab can build)
```

Everything else the market associates with chip design — RTL synthesis engines, place-and-route automation, AI-assisted optimization, cloud delivery, 3D-IC packaging flows — is carried by current mature products but is not what makes the software this Type. A tool set that holds the three-part core is recognizable as a chip-design environment whether it is a modern AI-enhanced suite, a regional vendor's analog flow, or an older, manually operated environment.

When the object of work becomes a printed circuit board, a mechanical part, a running piece of software, or a programmed FPGA device, the product has moved into a different Application Type.

## Users & Context

Chip design is a team discipline organized along the flow. The primary users:

- **Digital design engineers** — write and refine the functional description of the chip (hardware description language) and drive it through synthesis.
- **Verification engineers** — build testbenches, run simulations, and chase functional bugs; verification is a first-class discipline with its own tools and career track. One major vendor states that verification can account for up to seventy percent of the IC design cycle (vendor-published claim).
- **Physical design engineers** — turn the synthesized logic into the actual floorplan, placement, and wiring of the chip, and close timing and power against the routed result.
- **Custom/analog circuit designers and layout designers** — design analog, mixed-signal, RF, and memory circuitry at the transistor level; these roles work in close collaboration, with the circuit designer working in schematics and the layout designer drawing the physical geometry.
- **Design-for-test (DFT) engineers** — add and validate the logic that lets manufactured chips be tested.
- **CAD/methodology teams** — build and maintain the tool flows, scripts, and libraries that the design teams use.

The organizational context is the semiconductor ecosystem: fabless chip companies, semiconductor divisions of system companies, integrated device manufacturers, and foundries' design-enablement groups. The silicon is manufactured externally by a foundry or internally by the company's own fab; either way, the manufacturing process — its rules, its device behavior, its limits — arrives in the design environment as data supplied by the process owner. Design projects run for months or years, fabrication is expensive and slow to redo, so the platform's overriding posture is correctness-first: a chip cannot be patched after it is made, so everything is verified before manufacturing data leaves the design environment.

## Core Model

### The design across abstraction levels

The central object is the chip design itself, held as several representations of the same circuit at different levels of detail, all connected:

- **Functional/logical description** — what the circuit should do. In digital design this is typically a hardware description language (RTL); in custom analog design it is a schematic — a drawn circuit of transistors, resistors, and capacitors; some flows start even higher, from C-level models refined by high-level synthesis.
- **Circuit realization (netlist)** — the circuit as a concrete interconnection of components: logic gates from standard-cell libraries for digital designs, transistors for custom circuits. Synthesis produces this from the description; custom circuits are entered as schematics and simulated directly at this level.
- **Physical layout** — the geometric shapes that will actually be manufactured on silicon: the floorplan placing major functions, the placed cells, and the routed wiring between them.

The correspondence between levels is itself part of the design. Synthesis and layout tools transform one level into the next; checking tools prove that two levels still agree (equivalence checking at the logic level, layout-vs-schematic checking at the physical level). A design that has drifted — where the layout no longer matches the netlist, or the netlist no longer matches the description — is not a finished design.

### The manufacturing process as data input

Chip design is bounded by a specific silicon manufacturing process. The process owner (a foundry or an internal fab) supplies the process as data: design rules stating what geometry can be manufactured, device models describing how transistors on that process behave, and parasitic models describing how wiring distorts signals. Design environments are certified against specific foundry processes, and vendors run joint certification programs with foundries so that flows are proven on a given process before customers commit. A design is manufacturable *relative to a process* — the same layout means nothing without the process rules that judge it.

### The library and IP foundation

Chips are assembled from pre-designed building blocks. Standard-cell libraries (the gates digital synthesis draws from) must be characterized — measured and modeled so that timing, power, and test tools can reason about them. Larger pre-designed blocks — processor cores, interface controllers, memory compilers — are integrated as IP and treated as design data inside the platform. Library characterization is a first-class capability: it produces the models that the rest of the flow consumes.

### Verification artifacts

Verification produces its own objects: testbenches that stimulate the design, simulation waveforms that show its behavior, coverage metrics that measure what has been exercised, and rule-checking results — geometry violations, correspondence mismatches, timing and power violations — attached to specific locations in the design. These artifacts are worked, prioritized, and closed like defects.

### The flow

The three-part core is experienced as a flow with a fixed terminus:

```text
Functional description
  → circuit realization (synthesis and/or schematic entry)
    → physical implementation (place & route and/or hand layout)
      → verification against process rules and electrical reality
        → signoff (all gates clean on trusted tools)
          → fabrication-ready manufacturing data (mask data)
```

The terminus is what distinguishes the Type: the platform does not end at a working program, a programmed device, or a board — it ends at manufacturing data for a silicon process.

## How It Works

### The digital flow

Digital chips — processors, SoCs — are designed through a heavily automated pipeline:

```text
Write/refine RTL description
→ simulate against testbenches; debug waveforms; fix; repeat
→ synthesize the description into a gate-level netlist
  (drawing cells from characterized standard-cell libraries)
→ prove the netlist still equals the description (equivalence checking)
→ floorplan the chip; place the cells; route the wiring
→ extract parasitics from the actual routing; re-analyze timing and power
→ check the geometry against the process design rules
→ iterate until timing, power, and physical checks are clean
→ sign off and generate manufacturing data
```

Two behaviors are worth understanding. First, **closure is iterative**: routing changes the electrical behavior (wire delay, coupling), so timing and power are re-checked against the routed reality and the design is adjusted until it converges. Second, **edits late in the flow are surgical**: rather than re-running the whole pipeline, engineers make targeted engineering change orders and re-prove equivalence afterwards.

### The custom analog / mixed-signal flow

Analog, RF, and mixed-signal circuitry follows a different rhythm — craft over automation:

```text
Draw the schematic (transistor-level circuit)
→ simulate with circuit simulation (SPICE-class, using the
  process's device models); inspect waveforms against specifications
→ size and adjust the circuit; repeat
→ draw the layout by hand (with automation assistance for
  common structures and rule checking while drawing)
→ extract parasitics; re-simulate with the layout's reality
  (post-layout simulation); fix mismatches
→ prove layout matches schematic; check geometry vs process rules
→ sign off and generate manufacturing data
```

Design intent flows from the schematic through every phase; the layout must be proven to correspond to the schematic before the design can be trusted. Mixed-signal chips combine both worlds — digital blocks are synthesized and implemented automatically, analog blocks are crafted, and the whole is verified together, with analog detail at transistor level.

### The verification loop (spans both flows)

Verification is a continuous loop, not a phase: build a testbench, simulate, inspect waveforms, file and fix failures, measure coverage, repeat. Where simulation is too slow — for whole-system workloads — mature platforms offer hardware-assisted acceleration (emulation and FPGA-based prototyping) that executes the design on specialized equipment. Formal verification proves properties mathematically where simulation cannot reach them.

### The gate: signoff and tape-out

Before manufacturing data is generated, the design passes **signoff**: the final checks run on the most trusted ("golden") tool configurations — design rules fully clean, layout matching the netlist, timing and power closed under the process's variation models, manufacturability rules satisfied. Signoff criteria come from the process owner; foundries certify which tools and flows they accept for signoff on their processes. Only after signoff does the platform emit the fabrication hand-off data — the mask-layout data the fab will build from. In industry language this milestone is tape-out.

### Core vs standard vs optional capabilities

**Defining core** — without these, not this Type:

- multi-level design representation with checkable correspondence
- simulation of electrical/logical behavior against process device models
- physical verification against process-specific design rules
- transformation flow from description to implemented layout
- manufacturing-data generation as the terminus

**Standard capabilities of mature products:**

- library characterization and IP integration
- timing, power, and signal-integrity analysis as named disciplines
- formal verification (equivalence, protocol/intent checking)
- design-for-test insertion and test/yield analysis
- waveform viewing, simulation management, coverage tracking
- unified design data model, flow automation, script-driven batch execution across compute clusters or cloud
- hardware-assisted verification (emulation/prototyping)

**Optional / variant:**

- 3D-IC, multi-die, and advanced-packaging design
- multiphysics co-analysis (thermal, electromagnetic) via adjacent product families
- AI-assisted optimization, verification, and agentic workflows
- MEMS, photonics, and flat-panel-display flows reusing the same anatomy
- cloud-managed delivery

## Interfaces

Chip-design work happens in a set of specialized surfaces, mostly desktop-class engineering applications backed by batch computation. Names vary by product; the surfaces are consistent.

### Schematic editor

Purpose: draw and edit the circuit as a schematic of connected components (custom/analog entry). Typical information: component symbols, connectivity, design properties, hierarchy into sub-blocks. Primary actions: place/connect components, parameterize devices, descend into sub-schematics, launch simulations from the schematic.

### Hardware-description editor and synthesis environment

Purpose: author and refine the RTL description and drive synthesis. Typical information: source hierarchy, constraint files, synthesis reports (timing, area, power estimates). Primary actions: edit code, apply constraints, run synthesis, inspect and constrain results.

### Simulation and waveform environment

Purpose: run simulations and inspect behavior. Typical information: simulation results as waveforms across time; measured values against specification limits; simulation logs. Primary actions: launch and manage simulation runs, probe signals, compare pre- and post-layout results, measure margins.

### Layout editor / implementation canvas

Purpose: create and edit the physical layout. In custom flows this is a precision polygon editor; in digital flows it is a floorplan-and-implementation canvas where cells are placed and wired automatically under engineer control. Typical information: process layers, cell instances, wiring, density, rule-checking overlays. Primary actions: draw/edit geometry, place and route, run incremental checks, inspect violations in context.

### Verification dashboards

Purpose: triage and close verification findings. Typical information: design-rule and layout-correspondence violations with locations, waiver status; timing and power reports against targets; coverage results against goals. Primary actions: inspect violations, group and waive with justification, assign fixes, track closure toward signoff.

### Library and design data management

Purpose: organize the design's parts. Typical information: cell libraries with their characterized models, IP blocks and versions, process kits, configuration data. Primary actions: import/characterize libraries, integrate IP, manage versions and configurations.

### Batch and compute surfaces

Purpose: the heavy engines (synthesis, place-and-route, extraction, verification) run as jobs across clusters or cloud, invoked from scripts and flow managers. Typical information: job status, resource usage, run histories, logs. Primary actions: launch/monitor jobs, manage flow steps, reproduce runs.

## Important Rules / Behaviors

- **Manufacturability is process-relative.** Design rules and device models belong to a specific silicon process. A layout clean against one process says nothing about another; migrating a design to a new process is a real project with its own tooling.
- **Correspondence must be proven, and re-proven.** The layout must match the netlist and the netlist must match the description. Every targeted edit late in the flow (an ECO) must be followed by renewed equivalence proof.
- **Routed reality beats estimates.** Wiring has electrical consequences (delay, coupling, voltage drop). Timing, power, and signal-integrity signoff happens against parasitics extracted from the actual layout, and closure iterates on those results.
- **Signoff gates manufacturing.** The design leaves for fabrication only when the trusted-tool checks are clean under the process owner's criteria; foundries certify which flows they accept. Unverified optimism has no path to silicon.
- **Verification dominates effort.** Industry claims — and the size of the verification tool families — make verification the largest single body of work on a chip project (one major vendor publishes a figure of up to seventy percent of the design cycle).
- **Automation depth differs by domain, not by quality.** Digital flows are highly automated pipelines; custom analog flows deliberately keep the human in the drawing loop, with automation assisting rather than replacing craft. Both are normal for the Type.
- **The design is big and hierarchical.** Modern chips are decomposed into blocks and worked in parallel; tools are built for very large hierarchical data, and results are attached to specific places in that hierarchy.

## Variants

- **Digital pole** — RTL-to-manufacturing-data pipelines; the automated synthesis/place-and-route world of SoCs and processors; the largest tool families.
- **Custom analog / mixed-signal pole** — schematic-and-layout craft for analog, power-management, and mixed-signal ICs; the founding form of the Type.
- **RF pole** — RFIC design with frequency-domain and electromagnetic analysis; circuit and package co-design.
- **Full-flow platform vs point tools** — the market's center of gravity is the integrated platform spanning the flow; standalone tools (a simulator, a layout viewer with rule-checking scripts, including free/open-source ones) exist as fragments of the same flow.
- **Leading-edge vs mature nodes** — advanced-node flows carry extra manufacturability and variation machinery; mature and analog nodes run leaner versions of the same anatomy.
- **Regional ecosystems** — domestic chip-design tool industries (most prominently China's) provide the same structures, coupled to local foundries' processes and enablement programs.
- **Open-source / low-cost tier** — free layout viewers/editors, open simulation engines, and academic toolchains; useful for learning and small designs, missing the certified-signoff depth of commercial flows.
- **Extended domains** — the same tooling pattern applied to MEMS, integrated photonics, and flat-panel displays; and extending layers for 3D-IC/multi-die packaging and hardware/software co-design.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| ECAD / EDA | sibling (shared industry umbrella) | board- and system-level electrical connectivity design: components, schematics of equipment, harnesses, cabinets; consumes component catalogs, not a foundry process; terminus is board fabrication output, not mask data |
| PCB Design | adjacent (board-side realization) | board layout centered on connecting packaged parts, not on manufacturing a die; the two Types meet in co-design (chip-to-package-to-board) without merging |
| Mechanical CAD | different object | geometry and mechanical function; no electrical-network semantics, no process-rule/correspondence machinery |
| CAE / Engineering Simulation | adjacent discipline | physics studies of designed artifacts; chip tools embed simulation inside the design loop for the artifact being made, not as external study management |
| System Simulation Platform / MBSE | adjacent, upstream | models system behavior and requirements before circuit realization; feeds this Type rather than producing manufacturing data |
| Code Editor / IDE | surface similarity only | front-end hardware description looks like code editing, but the object of record is the circuit and its manufacturing data, and the terminus is silicon, not running software |
| Version Control System | complementary | chip designs are versioned too — commonly by design-data management or general VCS — but versioning alone is not this Type |
| Embedded / Firmware Development IDE | different deliverable | develops software for chips; shares hardware-software co-design surfaces with modern platforms without being the design environment |
| FPGA implementation toolchains | closest adjacent flow | share the front-end (description, synthesis, simulation) but terminate at a programming image for a prefabricated device — no process design rules, no physical signoff, no mask data |
| Manufacturing Execution System | downstream world | runs the fab that consumes the hand-off data; object world of lots, wafers, and equipment, not designs |

The most important boundary is with ECAD/EDA: the industry umbrella term "EDA" covers both, vendors sell both, but the two are structurally different Types — different unit of design (die vs board), different governing data (foundry process rules vs component catalogs), different terminus (mask data vs board fabrication output).

## Representative Products

- **Synopsys** — full-flow digital (RTL-to-GDSII implementation, timing/physical signoff) plus custom analog/mixed-signal and FPGA families on a shared data model.
- **Cadence** — full-flow digital and the dominant custom/analog environment, with verification, emulation, and foundry-certified flows.
- **Siemens EDA** — IC design, verification and manufacturing portfolio anchored by physical-verification/design-for-manufacturing signoff, digital verification, and test.
- **Empyrean Technology** — China-based regional platform across analog/mixed-signal, PMIC, RF, digital, and foundry enablement.
- **KLayout** — open-source mask-layout viewer/editor with DRC/LVS scripting; a low-tier witness showing the same underlying objects in fragment form.

## Sources

Research date: **2026-09-09**

- Synopsys — Chip Design: https://www.synopsys.com/implementation-and-signoff.html
- Synopsys — "What is Integrated Circuit (IC) Design?" (glossary): https://www.synopsys.com/glossary/what-is-ic-design.html
- Cadence — Digital Design and Signoff: https://www.cadence.com/en_US/home/tools/digital-design-and-signoff.html
- Cadence — Virtuoso Studio: https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/virtuoso-studio.html
- Siemens — EDA Software, Hardware & Tools: https://www.siemens.com/en-us/company/electronic-design-automation/
- Siemens — IC Tool Portfolio: https://www.siemens.com/en-us/products/ic/
- Empyrean Technology — corporate site and solution catalog: https://www.empyrean-tech.com/
- KLayout — project site: https://www.klayout.de/

> Sourcing limitation: deep operational manuals of the major vendors are license-gated (support portals); this document's flows are reconstructed from official product, portfolio, and glossary pages. The RF/microwave vendor pole could not be fetched directly (HTTP 403) and is documented through the sampled vendors' RF offerings instead. Precise operational defaults, numeric limits, and tool-level mechanics are deliberately not asserted; vendor-published figures (e.g., verification share of design effort) are kept attributed.
