# ECAD / EDA

## Overview

An **ECAD / EDA application** is an engineering design application for electrical and electronic systems: the engineer designs a system of electrically connected parts by drawing **schematics** — diagrams of components shown as symbols and joined by connections — and the application understands those drawings as an electrical network, not as pictures.

The defining core is small:

```text
Component Library (parts with pin-level electrical interfaces)
└── Schematic Capture (symbol-based design of record)
    └── Connectivity (the electrical network implied by the drawing)
        └── Generated Deliverables (connection lists, parts lists,
            manufacturing / installation artifacts)
```

Everything else commonly associated with these tools — PCB layout, cabinet/panel layout, simulation, 3D, cloud collaboration, supply-chain data — is standard capability or variant, not the definition. A tool that draws circuit-like diagrams without connectivity semantics, an electrical part library, and derived deliverables is a diagramming or drawing tool, not this Type.

The Type has two market poles that share this one core:

- the **electronic pole** — circuits and printed circuit boards (symbols, footprints, copper, fabrication files)
- the **electrical pole** — machines, control cabinets, vehicles and wiring harnesses (devices, terminals, cables, wire lists, panel layouts)

## Users & Context

Primary users are engineers and designers who define how electrical or electronic systems are wired:

- **electrical engineers / electrical designers** — design control systems, power distribution, machine and plant wiring; produce schematics, terminal plans and wire lists for panel builders
- **electronics / hardware engineers** — design circuits and printed circuit boards; produce schematics, layouts and fabrication files for board manufacturers
- **harness / cable designers** — define cable bundles, wires and connectors for vehicles and machinery
- **panel / cabinet designers** — arrange devices inside control cabinets and route wires

Secondary users consume the design rather than author it: reviewers and checkers (often working in free viewers), purchasing (parts lists), manufacturing and assembly teams (terminal plans, formboards, fabrication outputs), and mechanical engineers (who receive device placements and harness routes into MCAD).

Typical settings: machine and panel building, industrial automation, automotive and special vehicles, aerospace, consumer and industrial electronics, building automation and energy. The work is almost entirely desktop; the design must survive into manufacturing, so precision of connectivity and part data matters more than visual polish.

## Core Model

### The Defining Core

**Component library.** Designs are composed from catalogued parts, not freehand shapes. A library entry carries the part's electrical interface — its pins or connection points — together with part data (values, manufacturer part numbers, and, depending on the pole, the physical representation: a footprint for a board, a 2D/3D device representation for a cabinet). Mature products ship large libraries and connect to vendor-maintained component data portals; teams also author their own entries in dedicated library editors.

**Schematic capture.** The design of record is a schematic: the engineer places symbols from the library onto drawing pages and draws connections between their pins. Schematics are typically multi-page and often hierarchical — a block on one page expands into a sub-schematic. Every placed component instance receives a unique designation (a tag such as a reference designator) so it can be addressed unambiguously across all pages and reports.

**Connectivity.** This is what separates the Type from drawing tools. The connections drawn on a page are interpreted as an electrical network — nets between pins. Connectivity does not stop at page edges: nets with the same name are the same net, so a label on one page and a power symbol on another join the same electrical node without a visible wire. The application therefore maintains a queryable model of "what is connected to what," from which it can answer questions (which pins are on this net? which devices does this cable join?) and against which it can check the design.

**Generated deliverables.** The deliverables that drive manufacturing and installation are derived from the connected design, not drawn by hand:

- connection lists — netlists in the electronic pole; wire lists and cable schedules in the electrical pole
- parts lists (BOM) aggregated from the placed components
- pole-specific artifacts: fabrication outputs for boards (layer plots and drill data); terminal plans, panel layouts and harness documentation for cabinets, machines and vehicles

### Standard Capabilities

Mature products across both poles commonly add:

- **a physical-layout surface** that realizes the connectivity in physical arrangement — placing footprints and routing copper tracks on a board (electronic pole), or arranging devices in a cabinet and routing wires (electrical pole) — kept consistent with the schematic
- **connectivity and design-rule checking** — unconnected pins, shorted nets, undriven inputs, clearance violations, missing designations; usually runnable as a report with violations linked back to the drawing
- **cross-references** between related pages and between a symbol and all its physical representations
- **simulation** — circuit behavior simulation is standard in the electronic pole; the electrical pole commonly offers electrical/logical checks instead, with simulation optional
- **MCAD integration** — exchanging device placements, board outlines or harness routes with mechanical CAD so electrical and mechanical design stay aligned
- **design data management** — versions, release processes, reuse, where-used traceability, and synchronization with PLM/ERP systems
- **report generation** — beyond BOM: terminal schedules, wire lists, cable documentation
- **collaboration surfaces** — multi-user editing or co-authoring in larger teams, and free viewers/markup tools for non-designers

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:      Component library
Realizations: file-based symbol/footprint libraries; centralized managed
              component databases; vendor-operated component data portals

Concept:      Schematic as design of record
Realizations: drawing files in a project folder; pages inside a
              database-backed project; objects in a platform data model

Concept:      Connectivity
Realizations: nets computed from drawn wires and labels; connection
              records in an object-oriented design database

Concept:      Deliverables
Realizations: exported report files; generated fabrication datasets;
              machine-targeted manufacturing data
```

A reader who has only seen one pole should still recognize the other from this core: a cabinet wiring design and a circuit board design are the same structure — symbols, connections, nets, parts, derived lists — with different physical realizations.

## How It Works

### The design loop (both poles)

```text
Create a project
→ place components from the library onto schematic pages
→ draw connections between pins (wires, cables, buses)
→ name nets / label connections so connectivity crosses page boundaries
→ assign designations and part data to every component
→ run connectivity / design-rule checks and fix violations
→ generate deliverables (connection lists, parts lists)
```

### The electronic pole: from schematic to fabricated board

```text
Complete and check the schematic
→ assign a physical footprint to each component
→ transfer the design into the board editor
→ draw the board outline; place footprints (guided by unrouted-connection indicators)
→ route copper tracks between pads, changing layers with vias
→ pour copper zones for power/ground; re-check with design rules
→ generate fabrication outputs (layer plots, drill files) for the board manufacturer
```

Schematic and board stay synchronized: schematic changes are transferred forward into the layout, and layout-side changes can be pushed back. The checkers on both sides (electrical rules on the schematic, design rules on the layout) gate the release of fabrication data.

### The electrical pole: from schematic to wired cabinet or harness

```text
Complete and check the schematic (devices, PLC I/O, function blocks)
→ define cables and wires: bundles, cores, shields, twisted pairs
→ lay out devices in the cabinet (2D and often 3D); signal logic inherited from the schematic
→ route wires through the cabinet; determine wire lengths and cut lists
→ produce terminal plans, wire lists and assembly documentation
→ hand off to panel building / wire processing (in mature setups, directly to machines)
```

Because the electrical pole's products typically keep the whole design in one data model, an edit in one view (a schematic page, the cabinet layout, a report) is reflected in the others; the schematic remains the source of the signal logic that the physical views inherit.

### Capability tiers

- **Defining core** — component library, schematic capture, connectivity, generated deliverables
- **Standard in mature products** — physical-layout surface, checking, cross-references, designations, MCAD integration, data management, reports
- **Variant / optional** — simulation depth, harness/cable tooling, fluid (hydraulic/pneumatic) schematics, PLC documentation, supply-chain data integration, cloud co-authoring, manufacturing-machine integration

## Interfaces

### Schematic editor

The primary surface. Drawing pages with placed symbols, wires and labels; tool palettes for placing, wiring and annotating; cross-reference and navigation aids to jump between related pages and between a symbol and its representations. Primary actions: place/move/rotate symbols, draw connections, label nets, edit properties, run checks.

### Library editors

Dedicated editors for creating and maintaining the parts the designs depend on — symbols (and, in the electronic pole, footprints; in the electrical pole, device and cable definitions). Primary actions: draw the symbol graphic, define pins, attach part data, link the symbol to its physical representation(s).

### Physical layout editor

Pole-dependent: the board editor (outline, placement, routing, zones, layer stackup, design rules) in the electronic pole; the cabinet/panel layout (device arrangement in 2D/3D, wire routing, ducts and terminals) in the electrical pole. Primary actions: place, orient and route; verify clearances; keep consistency with the schematic.

### Checking views

Violation lists produced by the electrical/design-rule checkers, each entry linked to the offending location in the drawing; severity configuration; exclusion of justified violations.

### Output and report generation

Dialogs and generators for BOM, connection/wire lists, terminal plans, fabrication datasets and manufacturing documentation; format and grouping configuration; preview of the derived output.

### Project / data management

Project trees listing pages, layouts, libraries and reports; version and release handling in team deployments; where-used queries; integrations panels for MCAD, PLM/ERP connections.

### Viewers

Free or lightweight viewers that let reviewers, production and service staff open designs read-only, with markup in some products — the design of record stays with the engineers.

## Important Rules / Behaviors

- **Connectivity is semantic, not visual.** Two points with the same net name are electrically connected even if no wire is drawn between them; conversely, wires that merely touch visually without sharing a net are not connected. This is the single most important behavior distinguishing the Type from drawing tools — and the source of a classic class of user errors that the checkers exist to catch.
- **Every component instance must be uniquely designated.** Reports, terminal plans and netlists are keyed by these designations; unannotated symbols are treated as errors.
- **The library is the quality backbone.** A design is only as correct as its parts: pin definitions, footprints/device representations and part data come from the library, which is why mature deployments treat library management as a governed discipline of its own.
- **Checks gate release.** Fabrication outputs, wire lists and panel production data are generated from a checked design; unresolved violations are meant to block or at least flag the handoff.
- **Schematic and physical layout must not drift apart.** Whether synchronization is manual (designer-triggered transfer) or automatic (one shared data model), a mismatch between the logical design and the physical realization is treated as a defect.
- **Deliverables are derived, never hand-drawn.** Editing a wire list or a BOM by hand does not change the design; the design of record is the schematic, and the lists are regenerated from it.

## Variants

- **Electronic pole (board-centric)** — schematic capture plus PCB layout; objects are footprints, tracks, vias, copper zones and layer stackups; deliverables are fabrication datasets. Ranges from free/open-source tools to commercial environments with simulation, signal-integrity analysis and cloud collaboration.
- **Electrical pole (machine/panel/harness-centric)** — schematic capture plus cabinet layout, cable/harness design and terminal management; objects are devices, terminals, cables, wires and PLC I/O; deliverables are terminal plans, wire lists and panel/harness production data. Often extends to fluid (hydraulic/pneumatic) schematics in the same tool family.
- **MCAD-embedded electrical design** — electrical schematics delivered as a companion to a mechanical CAD suite, trading standalone depth for tight mechanical integration.
- **Enterprise platform deployments** — database-backed, multi-user, with governed libraries, release processes and PLM/ERP integration; contrasted with file-based single-designer projects.
- **Industry tunings** — automotive/vehicle harness ecosystems, aerospace wiring, building automation and energy, machine and panel building; the core is unchanged, the object families and deliverable sets are tuned.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Mechanical CAD | co-discipline, frequently integrated | MCAD's design of record is geometry (solids/surfaces); here it is connectivity. MCAD receives placements and routes; it does not hold the electrical network. |
| Diagramming Application | visually similar | diagramming tools draw shapes and connectors with no pin/net semantics, no electrical part library and no derived deliverables. |
| PCB Design | pole-level overlap | the electronic pole's products are marketed as PCB design software; board layout is the physical-realization surface of this Type, not a separate object world. See note below. |
| Semiconductor Design Platform | namesake neighbor | "EDA" in the industry's broadest sense also covers IC design (a different object world: hardware description, verification, place-and-route); treated here as a separate Type. |
| Electrical Design Application | probable alias | vendors market this Type's electrical pole as "electrical design software"; the same product family. See note below. |
| CAE / Engineering Simulation | capability overlap | simulation is an embedded capability here; CAE's design of record is a solver study, not a connected design. |
| PLM / Bill of Materials Management | downstream consumer | parts lists generated here are consumed and managed there; design-data management modules sit at this seam. |
| CAM | downstream handoff | fabrication outputs generated here are transformed into manufacturing tooling there. |

Two directory-level observations: the boundary between this Type and the PCB Design leaf is a pole overlap rather than a clean seam (the same products are commonly described by both labels), and the Electrical Design Application leaf appears to name the electrical pole of this same Type. Both are recorded for joint review rather than silently resolved here.

## Representative Products

- **KiCad** — open-source electronic design suite: project-based schematic capture, PCB layout, symbol/footprint editors, SPICE simulation, fabrication outputs
- **Altium Designer** — commercial electronic design environment: unified schematic-to-manufacturing data model, interactive routing, constraint management, cloud collaboration and supply-chain data
- **Zuken E3.series** — electrical design platform for machinery, vehicles and harnesses: schematics, cable/harness design, cabinet layout, terminal plans, manufacturing integration
- **EPLAN (Eplan Platform / Electric P8 / Pro Panel)** — electrical engineering platform for machine and panel builders: assisted schematic creation, 3D panel layout, component data portal, ERP/PDM/PLM integration

The defining core was checked across both poles and against the historical form of the Type (1980s-generation schematic-capture tools already exhibit all four core structures), so the definition does not depend on current cloud or supply-chain features.

## Sources

Research date: **2026-09-07**

- KiCad — Getting Started in KiCad (official documentation): https://docs.kicad.org/9.0/en/getting_started_in_kicad/getting_started_in_kicad.html
- Zuken — E3.series product pages: https://www.zuken.com/en/product/e3series/
- Zuken — E3.series Online Documentation portal: https://www.zuken.com/doc/e3/series/en/Content/reference/welcome/welcome_help.htm
- Altium — Altium Designer product page: https://www.altium.com/altium-designer/
- EPLAN — corporate homepage: https://www.eplan.com/en/

> Sourcing limitation: EPLAN's product subpages and SOLIDWORKS Electrical's product pages could not be fetched from the research environment (repeated 404s / timeouts). EPLAN evidence is therefore positioning-level, and the MCAD-embedded electrical pole was not directly observed; claims about those products are kept correspondingly weak. Electrical-pole operational detail rests mainly on Zuken's product documentation. Precise numeric limits, default settings and product-internal parameters are intentionally not stated in this document.
