# Electrical Design Application

## Overview

An **Electrical Design Application** is an engineering design application for electrical systems: engineers design how machines, control cabinets, vehicles, and installations are wired by drawing **wiring schematics** — diagrams of devices shown as symbols and joined by wires — and the application understands those drawings as an electrical network rather than as pictures. From the connected design it generates the lists and layouts that drive panel building, wire-harness manufacture, and installation.

The defining core is small:

```text
Device/Symbol Library (devices with connection points + part data)
└── Wiring Schematic (design of record — single-line and multi-line diagram pages)
    └── Connectivity (designated wires and connections held as electrical data)
        └── Generated Deliverables (wire lists, terminal documentation,
            parts lists, panel/harness production data)
```

Everything else commonly associated with these tools — cabinet layout in 3D, harness formboards, PLC documentation, device data portals, multi-user platforms — is standard capability or variant, not the definition. A tool that draws circuit-like diagrams without device libraries, connection-point semantics, and derived deliverables is a diagramming tool, not this Type.

Label note: this Type names the electrical-engineering side of the electrical/electronic design family. The circuit-board side is documented under ECAD / EDA and PCB Design; the defining structure is shared, while the object world differs (devices, wires, cables, terminals, cabinets and harnesses here; footprints, copper and boards there). The overlap between the directory leaves is recorded for review rather than silently resolved.

## Users & Context

Primary users are engineers and designers who define how electrical systems are wired:

- **electrical engineers / electrical designers** at machine builders and system integrators — design control systems and machine wiring; produce schematics, terminal plans and wire lists
- **panel / cabinet engineers** — lay out devices in control cabinets, route wires, and produce assembly and wiring documentation
- **harness / cable designers** at vehicle and machinery manufacturers — define cables, wires and connectors, and produce harness manufacturing documentation
- **building-automation, energy and installation engineers** — design measurement/control schematics, power distribution and installation diagrams

Secondary users consume the design rather than author it: panel wiremen and assembly teams (terminal plans, wire lists, work instructions), purchasing (parts lists), PLC programmers (I/O documentation), mechanical engineers (who receive device placements and harness routes into mechanical CAD), and reviewers or service staff (working in free viewers).

Typical settings: machine and plant building, control-panel and switchgear manufacturing, special vehicles and automotive, aerospace, building automation and energy. The work is almost entirely desktop; the design must survive into manufacturing, so precision of connectivity and device data matters more than visual polish.

## Core Model

### The Defining Core

**Device/symbol library.** Designs are composed from catalogued devices, not freehand shapes. A library entry carries the device's connection points (terminals or pins), its graphic symbol, and part data (manufacturer part numbers, technical attributes). Mature products draw on very large shared resources — vendor-operated device-data portals and manufacturer-provided parts repositories — alongside team-maintained collections, with dedicated editors for creating new symbols and devices.

**Wiring schematic (design of record).** The engineer places device symbols onto drawing pages and draws wires between their connection points. Electrical design uses two diagram forms: **single-line diagrams** (power distribution condensed to one line per circuit) and **multi-line diagrams** (every conductor of a circuit drawn individually), plus control-circuit diagrams. Projects are multi-page, typically structured by function or location, and every page carries a title block. Every placed device receives a unique designation so it can be addressed unambiguously across pages, lists and reports.

**Connectivity.** This is what separates the Type from drawing tools. The wires drawn between terminals are held as electrical data — named, numbered conductors and connections — not as lines on a page. The application maintains a model of "what is connected to what": wires are numbered (commonly automatically), connections cross page boundaries through labels and references, and coordinated device parts (for example a contactor's coil and its contacts, drawn on different pages) are linked by cross-references. Terminals are first-class objects: physical connection points where wires join, organized into terminal blocks and documented as terminal plans.

**Generated deliverables.** The deliverables that drive manufacturing and installation are derived from the connected design, not drawn by hand:

- wire/conductor lists and connection lists
- terminal plans / terminal diagrams
- parts lists (BOM/nomenclature) aggregated from the placed devices
- I/O lists tying signals to PLC addresses
- installation and production data: cabinet layouts, wire cut lists and lengths, harness documentation

### Standard Capabilities in Mature Products

Mature products commonly add:

- **cable management** — individual wires grouped into cables with cores, shields and twisted pairs, shown consistently in schematics and reports
- **cabinet/panel layout** — arranging devices in enclosures in 2D and 3D, with the signal logic inherited from the schematic; wire routing through the cabinet and wire-length calculation
- **harness documentation** — in harness-oriented products: wiring topology and full-size formboard drawings for harness manufacture
- **PLC documentation** — mapping signals to PLC I/O addresses, generating I/O lists and PLC diagrams
- **connectivity and design-rule checks** — unconnected points, naming conflicts, missing designations; runnable as reports with violations linked back to the drawing
- **cross-page navigation and cross-references** — between related pages, between coordinated device parts, and between a symbol and its physical representation
- **MCAD integration** — exchanging device placements, cabinet layouts and harness routes with mechanical CAD
- **design data management** — versions, release processes, reuse, where-used traceability, PLM/ERP synchronization
- **collaboration surfaces** — multi-user editing in teams, and free viewers/markup tools for non-designers

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:      Device/symbol library
Realizations: file-based symbol collections; managed team libraries;
              vendor-operated device-data portals; manufacturer parts repositories

Concept:      Wiring schematic as design of record
Realizations: drawing files in a project folder; pages inside a
              database-backed project; objects in a platform data model

Concept:      Connectivity
Realizations: numbered conductors computed from drawn wires and labels;
              connection records in an object-oriented design database

Concept:      Deliverables
Realizations: printed/PDF drawing sets and list reports; exported lists;
              machine-targeted manufacturing datasets
```

A reader who has only seen an enterprise platform should still recognize a minimal tool from this core: a free schematic editor with a symbol collection, wire numbering and a parts-list report is the same structure with fewer surrounding capabilities.

## How It Works

### The design loop

```text
Create a project
→ place devices from the library onto schematic pages
→ draw wires between device terminals (single-line and multi-line)
→ name and number wires; assign designations to every device
→ group wires into cables where needed; define terminal blocks
→ document PLC I/O assignments
→ run connectivity/design-rule checks and fix violations
→ generate deliverables (wire lists, terminal plans, parts lists, I/O lists)
```

### From schematic to built cabinet

```text
Complete and check the schematic
→ lay out devices in the cabinet (2D and often 3D); signal logic inherited from the schematic
→ route wires through the cabinet; calculate wire lengths and cut lists
→ produce terminal plans, wire lists and assembly documentation
→ hand off to panel building (in mature setups, directly to wire-processing machines)
```

Because mature products keep the whole design in one data model, an edit in one view (a schematic page, the cabinet layout, a report) is reflected in the others; the schematic remains the source of the signal logic that the physical views inherit.

### From schematic to harness

```text
Define the wiring topology between devices
→ group wires into bundles; add shields and twisted pairs
→ produce full-size formboard drawings and harness documentation
→ feed wire-processing and assembly machinery
```

### Capability tiers

- **Defining core** — device library, wiring schematic, connectivity, generated deliverables
- **Standard in mature products** — cables, terminals and PLC documentation; cabinet layout with routing; checks; cross-references; MCAD/PLM/ERP integration; data management; multi-user; viewers
- **Variant / optional** — discipline extensions (fluid, P&I, building automation, installation), harness manufacturing ecosystems, electrical simulation, AI assistance, open-source vs enterprise delivery

## Interfaces

### Schematic editor

The primary surface. Diagram pages with placed device symbols, wires and labels; single-line and multi-line representations; tool palettes for placing, wiring and annotating; page structure and title blocks. Primary actions: place/move/rotate symbols, draw and label wires, edit device properties, navigate between pages and cross-references, run checks.

### Library / collection editors

Editors for the symbols and devices the designs depend on: drawing the symbol graphic, defining terminals, attaching part data, organizing user and project collections.

### Navigators and structure views

Project trees and navigators over devices, terminals, cables, pages and PLC I/O — the queryable view of the design's data (which devices exist, which wires join which terminals, where a device appears). Exact names and layout vary by product.

### Cabinet/panel layout editor

A 2D or 2D+3D surface for arranging devices in enclosures, placing rails, ducts and terminals, routing wires, verifying fit and clearances, and deriving lengths and cut lists.

### Reports and output

Generators for wire/conductor lists, terminal plans, parts lists and I/O lists, plus drawing-set printing and PDF export, with format and grouping configuration; in mature products, machine-targeted manufacturing export.

### Data management / administration

Version and release handling, where-used queries, user rights, and integration panels for MCAD/PLM/ERP connections in team deployments.

### Viewers

Free or lightweight viewers that let reviewers, production and service staff open designs read-only, with markup in some products — the design of record stays with the engineers.

## Important Rules / Behaviors

- **Connectivity is semantic, not visual.** Wires that share a name or label are the same connection even across pages; lines that merely touch visually are not necessarily connected. This is the single most important behavior distinguishing the Type from drawing tools — and the source of a classic class of errors that the checkers exist to catch.
- **Every device instance must be uniquely designated.** Lists, terminal plans and I/O documentation are keyed by these designations; automatic numbering is the common implementation.
- **Terminals are first-class objects.** A terminal is a physical connection point where wires join; terminal blocks are documented, and wire lists are organized around them.
- **The schematic is the single source of signal logic.** Cabinet layouts, harness documentation and reports inherit it; a mismatch between the logical design and a physical view is treated as a defect.
- **Checks gate manufacturing outputs.** Wire lists, terminal plans and production data are generated from a checked design; unresolved violations are meant to block or at least flag the handoff.
- **Deliverables are derived, never hand-edited into truth.** The design of record is the schematic; lists and layouts are regenerated from it.
- **The library is the quality backbone.** Terminal definitions, symbols and part data come from the library, which is why mature deployments treat device-data management as a governed discipline of its own.

## Variants

- **Machine and panel-building platforms** — the enterprise center of the Type: schematic, cabinet, terminal and PLC machinery with data management and manufacturing integration
- **Vehicle/harness ecosystems** — wiring topology, formboards, harness builders, wire-processing machine integration, assembly work instructions
- **Multi-discipline suites** — the same core extended with fluid (hydraulic/pneumatic), piping & instrumentation, building automation and electrical installation modules on one platform
- **MCAD-embedded companions** — electrical schematics delivered as a companion to a mechanical CAD suite, trading standalone depth for tight mechanical integration
- **Minimal standalone and open-source tools** — project + diagram pages + symbol collections + basic lists; fully within the Type
- **AI-assisted editing** — the newest layer: copilots, automated checking, generated layouts

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| ECAD / EDA | family sibling — overlap recorded for review | this Type is the electrical-engineering pole of the family the ECAD/EDA leaf documents; the defining structure is shared, while the electronic pole's products (circuit-board design) carry a different object world |
| PCB Design | family sibling (electronic realization) | board layout with footprints, copper and fabrication outputs — the electronic pole's physical realization, not this Type's object world |
| Semiconductor Design Platform | namesake neighbor | IC design (hardware description, verification, place-and-route) is a different object world entirely |
| MEP Design | edge overlap | building-services design anchored in the building model (coordinated with architecture/structure) vs wiring design of record; some products in this Type carry building-installation modules while keeping the wiring-diagram center |
| CAE / Engineering Simulation | adjacent discipline | power-system studies (load-flow/short-circuit class) are solver studies on network models; here the design of record is the wiring schematic, and simulation is at most an embedded capability |
| Diagramming Application | visually similar | diagramming draws shapes and connectors with no device terminals, no connectivity semantics and no derived lists |
| Mechanical CAD | co-discipline | MCAD's design of record is geometry; it receives device placements and harness routes through integration bridges |
| PLM / Bill of Materials Management | downstream consumer | parts lists generated here are consumed and managed there; design-data management modules sit at this seam |
| CAM / CNC Programming | downstream handoff | cabinet-layout and wire data feed manufacturing machinery |

## Representative Products

- **Zuken E3.series** — electrical design platform for machinery, vehicles and harnesses: schematics, cable/harness design, cabinet layout, terminal plans, manufacturing integration
- **EPLAN (Eplan Platform / Electric P8 / Pro Panel)** — electrical engineering platform for machine and panel builders: assisted schematic creation, 3D panel layout, device-data portal, ERP/PDM/PLM integration
- **WSCAD ELECTRIX** — all-in-one electrical CAD suite (electrical, cabinet, fluid, P&I, building automation, installation) with a free manufacturer parts repository
- **QElectroTech** — free, open-source schematic editor: projects, single-line/multi-line diagrams, symbol collections, wire numbering, list reports

Other products commonly placed in this category by market and competitor sources (not directly documented in this pass): AutoCAD Electrical, SOLIDWORKS Electrical.

The defining core was checked from the enterprise to the minimal end of the market — including a free open-source tool — so it does not depend on enterprise platform features, 3D, data portals or multi-user machinery.

## Sources

Research date: **2026-09-08**

- Zuken — E3.series product pages: https://www.zuken.com/en/product/e3series/
- EPLAN — corporate homepage: https://www.eplan.com/en/
- WSCAD — corporate site: https://www.wscad.com/en/
- QElectroTech — project site: https://qelectrotech.org/ ; official documentation: https://qelectrotech.github.io/qelectrotech-doc/index.html

> Sourcing limitation: EPLAN's product subpages, AutoCAD Electrical (product page and help), SOLIDWORKS Electrical, ProfiCAD, IGE+XAO and the G2/Capterra category pages could not be fetched from the research environment (404 / 403 / timeout / transport errors). EPLAN evidence is therefore positioning-level; AutoCAD Electrical and SOLIDWORKS Electrical were observed only through a competitor's naming; the category-composition claim is not independently verified by a directory source. Precise numeric limits, default settings and product-internal parameters are intentionally not stated in this document; vendor marketing counts are kept in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the joint-review record against the ECAD/EDA leaf are in the paired Research Notes.
