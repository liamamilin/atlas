# PCB Design

## Overview

A **PCB Design application** is an engineering design application for printed circuit boards: the designer places components onto a layered board substrate and draws copper — tracks, vias, and zones — that realizes the circuit's electrical connections, verifies the result against manufacturing constraints, and produces the fabrication data a board manufacturer needs to build the board.

The defining core is small:

```text
Board (outline + layer stackup) — the design of record
└── Footprints (components as physical pads) placed on the board
    └── Nets (the electrical connectivity model binding pads together)
        └── Copper geometry (tracks / vias / zones realizing the nets)
            └── Fabrication outputs (artwork, drill, assembly data)
```

Everything else commonly associated with these tools — schematic capture, design-rule checking, 3D visualization, simulation, signal-integrity analysis, cloud collaboration, supply-chain data — is standard capability or variant, not the definition. Notably, the schematic is not part of the defining core: several products support laying out a board directly, without a schematic, and the connectivity model can be defined in the board editor itself. What the Type cannot exist without is the board, the footprints on it, the nets that govern its copper, and the manufacturing data that ends the work.

## Users & Context

Primary users are the people who turn a circuit into a manufacturable board:

- **electronics / hardware engineers** — own the circuit; in smaller teams they also lay out the board
- **PCB layout designers** — specialists whose craft is placement and routing: fitting the design into the mechanical envelope while satisfying electrical and manufacturing constraints
- **high-speed / signal-integrity engineers** — in advanced products, define timing, impedance and coupling constraints that the layout must satisfy

Secondary users consume the design rather than author it: reviewers and managers (who inspect and mark up the board), purchasing (who consume the bill of materials), assembly and test teams (who consume placement data), mechanical engineers (who receive the board's shape and component positions into mechanical CAD), and the board fabricator (who consumes the fabrication outputs).

Typical settings range from individual makers and small teams designing simple boards, through professional product-development teams, to enterprise hardware organizations with high-speed, rigid-flex, or multi-board systems. The work is almost entirely desktop or browser-based design sessions; the output must survive into physical manufacturing, so precision of geometry, connectivity, and part data matters more than visual polish.

## Core Model

### The Defining Core

**The board.** The central artifact is the board itself: a closed outline defining the board's shape (with cutouts where supported), realized on a stack of layers — copper layers for signals and planes, plus fabrication layers such as silkscreen, solder mask, and solder paste. The layer stackup (how many copper layers, their thickness and materials) is a first-class design decision, because it determines both the routing capacity and the manufacturing cost of the board. The board — not the schematic — is the artifact this Type exists to produce.

**Footprints.** Components enter the board as footprints: the physical counterpart of a schematic symbol, carrying the pads (copper lands, with or without drilled holes) at which the component connects to the board. Footprints are placed, oriented, and flipped between the board's sides. Designs are composed from catalogued footprints held in libraries; mature products ship large libraries and provide dedicated footprint editors, and a placed footprint is typically embedded as a copy in the board so the design stays independent of library changes.

**Nets.** The application maintains an electrical connectivity model: nets that bind specific pads together as "must be connected". This model is what makes the copper electrical rather than decorative. Nets enter the board from an upstream schematic in integrated suites, from an imported netlist, or — in board-only workflows — are defined directly in the board editor. Wherever it comes from, the connectivity model drives the most characteristic display of the Type: the ratsnest (also called connection lines or ratlines), which draws every not-yet-routed connection as a direct line between the pads it must join, and disappears connection by connection as the board is routed.

**Copper geometry.** The designer realizes the nets by drawing copper: tracks (routes) that carry a signal between pads, vias that jump between copper layers, and zones (copper pours) that fill areas of a layer with a net — commonly ground or power. Routing is governed by the design rules (see below); zones fill automatically around obstacles while keeping clearance and connecting to same-net pads, often through thermal-relief spokes. The copper geometry is the physical realization of the connectivity model, and the gap between them — connections not yet routed — is exactly what the ratsnest shows.

**Fabrication outputs.** The design terminates in manufacturing data: layer-by-layer artwork (today overwhelmingly Gerber format), drill data for holes, pick-and-place files listing each component's position and orientation for assembly machines, and a bill of materials. These outputs are generated from the design, never drawn by hand, and they are the deliverable the board manufacturer consumes. Many products also generate fabrication/assembly drawings and can exchange richer manufacturing-data formats.

### Standard Capabilities

Mature products across the market commonly add:

- **Schematic capture integration** — the dominant way connectivity enters the board. Schematic changes are transferred forward into the layout through an explicit, reviewable update step (a change list the designer confirms); layout-side changes such as renamed nets or swapped footprint assignments can be pushed back; and cross-probing lets the designer select an object on one side and find it on the other. Schematic and board are kept consistent, and a mismatch between them is treated as a defect to be found by checking, not an acceptable state.
- **Design rules and checking (DRC)** — the manufacturability contract expressed as machine-checkable constraints: minimum clearances between copper of different nets, minimum track widths, via sizes, and more. Rules are commonly organized per net class (power nets wide and loose, signal nets fine and tight) with a priority scheme for conflicts. Checking runs continuously while routing and/or as a batch pass, producing violation lists that navigate to the offending geometry; violations can be reclassified or excluded with justification. In integrated suites the checker also verifies parity between schematic and board.
- **Interactive routing** — the core editing act. Modern routers offer mode-based behavior (shoving existing tracks out of the way, walking around obstacles, or highlighting collisions for fully manual work), 45-degree geometry conventions, differential-pair routing, and length tuning for timing-critical nets. Some products add an autorouter; others are deliberately interactive-only.
- **Layer stackup management** — editors for the copper layer count, dielectric materials and thicknesses, and the via types (through-hole, and in advanced products blind/buried/microvias) the design may use.
- **3D visualization** — the board with its components as a 3D model, used to check mechanical fit and to export board models into mechanical CAD.
- **Library infrastructure** — symbol and footprint libraries, library editors, and increasingly connections to vendor-maintained component-data portals with part data and 3D models.
- **Documentation outputs** — fabrication and assembly drawings, drill tables, and board statistics alongside the manufacturing data files.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:      Board as design of record
Realizations: a board file inside a project (desktop suites); a board
              document in a cloud workspace (web tools)

Concept:      Nets
Realizations: synced from a schematic in the same suite; imported as a
              netlist file; defined pad-to-pad directly in the board editor

Concept:      Copper geometry
Realizations: interactive router with rule-driven assistance; optional
              autorouter; zones refilled on demand or automatically

Concept:      Fabrication outputs
Realizations: per-format export dialogs; pre-configured output sets
              generated by a release process; direct ordering into an
              integrated fabrication service
```

A reader who has only seen one implementation should still recognize the others from this core: a hobbyist board routed by hand in a browser tool and a 16-layer server board with length-tuned differential pairs are the same structure — footprints on a layered board, nets governing copper, fabrication data at the end.

## How It Works

### The board design loop

```text
Set up the board (outline, layer stackup, design rules)
→ transfer the design from the schematic (or add footprints directly)
→ place footprints, guided by the ratsnest
→ route tracks between pads, changing layers with vias
→ pour copper zones for power/ground; refill them
→ run design-rule checking; fix violations
→ generate fabrication outputs (artwork, drill, placement, BOM)
```

Setup comes first because everything downstream is rule-driven: the router refuses placements that violate clearances, the checker compares geometry against constraints, and the outputs assume the stackup is real. Placement is guided by the ratsnest — designers arrange footprints to untangle the unrouted-connection lines before routing begins. Routing then consumes the ratsnest connection by connection. Zones are filled last (or refilled on demand) because their copper is computed from everything else on the layer; products warn or refill automatically before outputs are generated, because stale zone fills would produce wrong manufacturing data.

### The schematic ↔ board sync loop

In integrated suites, the circuit lives in a schematic and the board must follow it:

```text
Edit the schematic (add/move/change components or connections)
→ run the update-to-board command
→ review the proposed change list
→ apply: footprints appear, nets update, removed parts disappear
→ layout-side changes (net names, footprint swaps) can be pushed back
```

The two sides are linked per-component (by internal identifiers or reference designators), so a component's footprint keeps its placement across updates. The checker's schematic↔board parity test is the safety net for this loop.

### The release loop

Team-oriented products formalize the end of the work:

```text
Confirm the design passes checking
→ generate the configured output set (fabrication + assembly data)
→ review the generated data
→ release it as a versioned manufacturing package
```

Consumer-oriented products shorten the same loop to a button: generate the Gerber and drill files, optionally inspect them in a viewer, and place the fabrication order directly.

### Capability tiers

- **Defining core** — board (outline + stackup), footprints, nets, copper geometry, fabrication outputs
- **Standard in mature products** — schematic integration, design rules + DRC, interactive routing, zones, 3D view, libraries, documentation outputs
- **Variant / optional** — simulation, signal/power-integrity analysis, autorouting, MCAD co-design, cloud collaboration and multi-user layout, supply-chain data, direct fabrication ordering, rigid-flex and multi-board support, unified constraint management, formal release processes

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Board editor

The primary surface — a zoomable canvas showing the board's layers in registered overlay, with an active-layer model (new copper goes on the active layer) and per-layer visibility, color, and opacity controls. The ratsnest, violation markers, and clearance outlines are drawn directly on the canvas. Primary actions: place/move/rotate/flip footprints, route tracks and vias, draw and refill zones, edit the board outline, inspect objects.

### Layer / stackup management

A panel or dedicated editor listing the board's layers — copper and fabrication — with the stackup's physical parameters (thicknesses, materials) and, in advanced products, via-type definitions. Primary actions: enable/disable layers, edit stackup, set active layer.

### Schematic editor

The upstream surface in integrated suites: multi-page circuit drawings whose symbols and wires carry the connectivity that the board realizes. Primary actions: place symbols, wire connections, annotate, run electrical checks, transfer the design to the board.

### Footprint / library editors

Dedicated editors for authoring the parts designs depend on: pad geometry, courtyard outlines, silkscreen graphics, 3D models, and part data. Primary actions: draw pads and graphics, define pad properties, attach part data, manage libraries.

### Checking views

Violation lists produced by the design-rule checker, each entry linked to the offending location; severity configuration; exclusion with comments; in some products a schematic↔board parity report alongside the rule violations.

### 3D viewer

The assembled board as a 3D model — board, footprints, often imported component models — for mechanical-fit inspection and model export.

### Output / fabrication dialogs

Generators for the manufacturing data: layer selection for artwork, drill-file options, placement-file filters, BOM configuration; in team products, a release view that validates, generates, and packages the whole output set.

## Important Rules / Behaviors

- **Connectivity is semantic, not visual.** Copper only "counts" where the nets say so: two pads are connected when a continuous copper path of the same net joins them, and the ratsnest keeps showing any connection that is not yet realized. The checker's unconnected-items report is the authoritative statement of what remains to be routed.
- **Schematic and board must not drift apart.** Whether synchronization is a designer-triggered update or a shared data model, a mismatch between the logical circuit and the physical board is a defect — mature products check for it explicitly.
- **Design rules gate the release.** Fabrication outputs are meant to be generated from a checked design; unresolved violations are meant to block or at least flag the handoff. Rule severity is configurable, and justified exclusions are a normal part of the workflow — but they are recorded decisions, not silence.
- **Deliverables are derived, never hand-drawn.** Editing a Gerber file or a BOM by hand does not change the design; the design of record is the board (and its schematic), and the manufacturing data is regenerated from it.
- **Zone fills are computed state.** A zone's copper is recalculated from the outline, the rules, and the objects it interacts with; products treat stale fills as an error condition before checking or output, because the fill is what actually gets manufactured.
- **The library is the quality backbone.** Pad geometry, courtyard outlines, and 3D models come from footprints; a wrong footprint produces a board that cannot be assembled. Mature deployments treat library maintenance as a governed discipline, and boards embed library copies so they do not change unexpectedly.
- **The board outline is load-bearing.** Zones fill only inside it, 3D and several checks depend on it being a valid closed shape, and mechanical fit is judged against it — a malformed outline is itself a checkable violation.

## Variants

- **Open-source full-flow suites** — desktop, file-based projects, complete schematic-to-fabrication flow with no license cost; depth in core layout, lighter in analysis and collaboration.
- **Professional desktop suites** — commercial licenses, unified environments spanning schematic, layout, analysis, and documentation; constraint management and release processes for team use.
- **Web-based freemium tools** — browser editors with cloud projects and sharing, integrated component sourcing and direct fabrication ordering; optimized for fast simple boards.
- **Enterprise platforms** — the professional suite plus signal/power-integrity analysis, multi-user layout, formal data management, and ECAD-MCAD co-design; sold alongside separate analysis products.
- **Capability variants** — rigid-flex and multi-board design, panelization, harness design in adjacent modules, autorouting, simulation depth; these vary by product and tier without changing the core.

A variant remains a variant unless it changes the core objects or workflow: a tool that only edits fabrication data (Gerber-class files) without footprints and nets is a fabrication-data editor, not this Type; a tool that only captures schematics without a board is schematic capture.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| ECAD / EDA | family overlap (electronic pole) | ECAD/EDA centers on schematic capture and connectivity as the design of record, spanning electrical (cabinet/harness) and electronic (board) poles; PCB Design centers on the board and its physical realization. The electronic pole's products are the same market this document describes — the two Types are complementary views of one product family, recorded for directory-level joint review. |
| Electrical Design Application | adjacent (electrical pole) | physical realization is cabinet/panel/harness layout with wire lists and terminal plans — no copper layers, no board, no fabrication artwork. |
| Mechanical CAD | co-discipline, integrated | MCAD's design of record is geometry; it receives the board's shape, placement, and 3D model, but holds no electrical network. |
| Semiconductor Design Platform | namesake neighbor | "EDA" broadly also covers IC design (hardware description, verification, chip place-and-route) — a different object world and scale from board design. |
| CAM | downstream handoff | fabrication outputs generated here are consumed by manufacturing CAM; in the PCB industry "CAM" also names fab-data preparation tools, which inspect or edit manufacturing files rather than author board designs. |
| CAE / Engineering Simulation | capability overlap | circuit simulation and signal-integrity analysis are embedded or bundled capabilities here; CAE's design of record is a solver study, not a board. |
| PLM / Bill of Materials Management | downstream consumer | the BOM and released manufacturing data generated here are managed there. |

The boundary with ECAD/EDA is the most important one, because the two Types share their product population at the electronic pole. The structural difference is the center of gravity: ECAD/EDA's defining artifact is the schematic and its connectivity semantics; PCB Design's defining artifact is the board — the layered physical object whose copper realizes that connectivity and whose fabrication data ends the work.

## Representative Products

- **KiCad** — open-source full-flow suite: schematic capture, board editor with interactive push-and-shove routing, zones, net classes and custom design rules, DRC with schematic-parity checking, Gerber/drill/pick-and-place outputs, 3D viewer
- **Altium Designer** — commercial professional suite: unified schematic-PCB environment, layer stack and via-type management, rule-priority design rules, ECO-based schematic-board updates, OutputJob/Project Releaser manufacturing flow, workspace collaboration and MCAD co-design
- **EasyEDA** — web-based freemium tool: schematic-to-PCB conversion, real-time DRC, copper pour, Gerber/drill/pick-and-place generation, direct fabrication ordering, board-only layout mode
- **Cadence OrCAD X / Allegro X** — enterprise commercial platform: PCB layout with constraint management, in-design analysis, DFM checks, team layout, manufacturing documentation, and supply-chain data (evidence level: product documentation pages; operational detail not independently verified)

The defining core was checked across all four products and against board-only workflows (documented in KiCad and EasyEDA) to avoid defining the Type by the schematic-integrated pattern alone.

## Sources

Research date: **2026-09-09**

- KiCad — PCB Editor Reference Manual (9.0): https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html
- Altium — Altium Designer documentation portal: https://www.altium.com/documentation/altium-designer
- Altium — Laying Out Your PCB: https://www.altium.com/documentation/altium-designer/pcb
- Altium — Preparing Your Design for Manufacture: https://www.altium.com/documentation/altium-designer/preparing-for-manufacture
- EasyEDA — Std User Guide (Introduction; PCB Layout; Design Rule Check; Layout a PCB Without Schematic): https://docs.easyeda.com/en/
- Cadence — OrCAD X Platform product page: https://www.orcad.com/

> Sourcing limitation: Cadence's operational documentation is behind a support portal and could not be fetched; OrCAD X / Allegro X evidence is positioning- and capability-level from official product pages, and claims about those products are kept correspondingly weak. Numeric capacities (layer counts, board sizes, library sizes) are product- and version-specific and are intentionally not stated in this document. Detailed evidence, cross-product comparison, and the joint-review analysis against ECAD/EDA are recorded in the paired Research Notes.
