# MEP Design

## Overview

An **MEP Design** application is an engineer-facing design environment for building services: the mechanical, electrical, and plumbing (and commonly fire-protection) systems that make a building work. In it, engineers lay out the physical networks of a building's services — ducts, pipes, cables, conduits, terminals, panels, fixtures, and equipment — inside the spatial context of the building those systems serve, size and verify the design against engineering quantities such as loads, flows, and capacities, and produce the deliverables (plans, schematics, schedules, calculation and compliance reports) that installers, reviewers, and permitting authorities work from.

The defining core is small:

```text
Building spatial context (levels, rooms/spaces/zones)
└── Building-services systems (mechanical / electrical / plumbing / fire)
    └── Physical components and networks carrying engineering parameters
        └── Sizing and verification by calculation
            └── Design deliverables for others
```

Everything else commonly associated with modern MEP software — 3D BIM models, manufacturer object libraries, clash detection, energy simulation, IFC exchange, automated routing — is widespread in current products but is not what makes the product an MEP design environment. Older and regional products built on 2D drafting with separate calculation programs satisfy the same definition.

When the object of work shifts to the building's spaces and envelope, the product is architecture design; when it shifts to the load-carrying frame, it is structural engineering; when the systems are those of a machine or an industrial plant rather than a building's occupants, it leaves this Type.

## Users & Context

The primary users are building-services engineers and designers, usually organized by discipline:

- **Mechanical / HVAC engineers** — design heating, ventilation, and air-conditioning systems: heating and cooling loads, air distribution, ductwork, terminals, and plant.
- **Electrical engineers** — design power, lighting, and low-voltage systems: circuits, panels and switchboards, cable routes, illumination.
- **Plumbing / sanitary engineers** — design water supply, hot-water circulation, drainage, and often gas systems.
- **Fire-protection designers** — lay out sprinkler systems and verify them hydraulically.

Secondary users shape the same environment:

- **BIM / design coordinators** — assemble discipline models, check collisions between services and with structure, manage issues across teams.
- **Senior engineers / reviewers** — check calculations and approve deliverables.
- **Contractors and fabricators** (downstream) — consume models, schedules, and drawings; some products extend into fabrication-level detailing.

The work context is a design consultancy or engineering department working on a specific building project, almost always against an architectural model or drawing set received from the design team, and against the calculation standards of the market the building is in. The application is typically open all day; the engineer moves repeatedly between laying out geometry, adjusting engineering parameters, running calculations, and updating deliverables as the architectural design changes underneath.

## Core Model

### The defining core

**Building spatial context.** The design lives inside a representation of the building: levels or floors, and the rooms, spaces, or zones the services must serve. This context may be authored in the application, imported from an architectural model, or drawn as a plan backdrop. It is not passive background: rooms and zones carry the occupancy, area, and environmental assumptions from which heating and cooling loads, ventilation air volumes, and lighting requirements are derived. Remove the building context and the work becomes industrial piping or product design.

**Building-services systems.** The objects of design are the services themselves, conventionally grouped by discipline:

- *Mechanical*: air-handling units, ducts, fittings, dampers, diffusers and terminals, heating and cooling plant, often underfloor heating circuits and radiators.
- *Electrical*: panels and switchboards, circuits, cables and cable packets, conduits and cable trays, luminaires and lighting tracks, low-voltage and data systems.
- *Plumbing*: water supply and hot-water circulation piping, drainage stacks and runs, sanitary fixtures, gas piping.
- *Fire protection*: sprinkler heads, pipework, and zone valves.

Components are not generic shapes. They carry engineering parameters — sizes, flow capacities, pressure characteristics, electrical ratings, acoustic data — and they connect: a duct connects to a diffuser, a pipe to a radiator, a cable to a panel. Connectivity and system assignment (which circuit, which duct system, which drainage stack a component belongs to) are part of the object, not an annotation.

**Sizing and verification by calculation.** The design loop is engineering, not just drawing. Loads are computed from the building context (heating and cooling loads from rooms and fabric; ventilation air volumes from occupancy; electrical demand from connected equipment); flows are accumulated through networks; components are sized against those quantities (duct and pipe dimensions, cable cross-sections, panel capacities, sprinkler densities); and the design is verified — pressure losses through ductwork and pipework, voltage behavior in circuits, sound levels, hydraulic adequacy of sprinkler systems. The calculation is bound to the designed objects: change a room's assumptions or reroute a duct and the affected numbers follow.

**Design deliverables for others.** The design leaves the application as deliverables that other parties consume: floor plans and sections showing the laid-out systems, schematic diagrams (single-line electrical diagrams, riser and system schematics), schedules and bills of materials generated from the components, and calculation or compliance reports. In model-based products the model itself is also a deliverable, handed to coordinators, contractors, and downstream tools.

### Standard capabilities mature products add

Around that core, mature products commonly provide:

- **Discipline toolsets** — separate modeling toolsets for ventilation, piping, electrical, and fire-protection work, each with its own component families and drawing aids.
- **Automated routing and drawing aids** — tools that draw duct and pipe runs with fittings inserted automatically, route cable packets, auto-connect devices to networks, and in some products auto-route entire circuits (for example underfloor heating loops).
- **Manufacturer product content** — libraries of real products with technical data, and selection tools that let the designer configure and validate a specific manufacturer's unit inside the design. Some products are built around large online BIM-object platforms; others ship curated equipment databases.
- **Coordination machinery** — combining discipline models in one spatial reference, checking for collisions between services and against structure, and managing issues between teams.
- **Schedules, quantities, and part lists** — generated from the designed components rather than counted by hand; part numbering for fabrication and installation.
- **Schematic editors** — single-line diagrams, switchboard schematics, and system/riser schematics that are kept consistent with the physical design.
- **Model–drawing associativity** — plans, sections, and reports generated from the model, so that editing the model (or, in some products, the drawing) updates the deliverables.
- **Interoperability** — exchange with other disciplines and tools through open formats (IFC being the common one) and links to specialist external calculators (for example lighting calculation or electrical-calculation software).

### One structure, many implementations

The core is best read conceptually; products realize it differently:

```text
Concept:   Building spatial context
Forms:     object-oriented 3D building model · imported architectural model ·
           drawn plan backdrop with assigned room data

Concept:   Services system
Forms:     connected 3D component network · 2D layout with attributed symbols ·
           schematic system/plant configuration without physical routing

Concept:   Sizing & verification
Forms:     embedded calculators bound to model objects ·
           separate calculation modules reading the same project ·
           external specialist tools linked in

Concept:   Deliverables
Forms:     installation drawings + schedules · calculation/compliance reports ·
           the coordinated model itself
```

A reader who has only seen one form — say, a 3D model-first product — should still recognize a drafting-first or calculation-first product as the same Type.

## How It Works

The typical work follows one repeating loop, run per discipline and per iteration of the building design:

```text
Establish the building context
→ lay out the services (route networks, place equipment and terminals)
→ connect components and assign them to systems
→ define or derive the engineering quantities (loads, air volumes, demands)
→ size components and run calculations
→ verify results, adjust the layout, repeat
→ coordinate with other disciplines
→ generate and update deliverables
```

**Establish the building context.** The engineer starts from the architectural reality of the project: a received model, a drawn plan, or rooms and floors defined in the tool. Rooms and zones receive the assumptions calculations will use — occupancy, area, construction, internal gains.

**Lay out the services.** Using the discipline toolset, the engineer routes the networks and places equipment: ducts from an air-handling unit to diffusers room by room; pipework from plant to radiators and fixtures; cable routes from panels to luminaires and socket circuits; sprinkler ranges across ceiling zones. Drawing aids insert fittings, maintain elevations, and keep components connected as the layout changes.

**Connect and assign.** Each terminal, fixture, or luminaire is attached to its system — the duct system, the hot-water circulation loop, the panel circuit, the sprinkler zone. This assignment is what lets the software accumulate flows and demands through the network.

**Derive quantities and size.** Loads and demands are computed from the rooms and the connected equipment: heating and cooling loads per room and for the whole building; ventilation air volumes; electrical demands per circuit and panel; water flow rates per pipe section. Components are then sized — duct and pipe dimensions selected against pressure-loss criteria, cable cross-sections against current-carrying capacity and voltage behavior, panels against accumulated load, sprinkler systems against hydraulic requirements.

**Verify and iterate.** The engineer reads the calculation results — pressure losses, sound levels, voltage behavior, hourly load profiles in the more calculation-deep products — and adjusts the layout or selections until the design verifies. In calculation-led products this step dominates: the building is modeled primarily to compute loads and compare system alternatives.

**Coordinate.** Discipline designs are brought together in a shared spatial reference; collisions between services, and between services and structure, are found and resolved; issues are tracked between teams. In drafting-era practice this happened on overlaid transparencies; in model-based practice it is a continuous check.

**Produce deliverables.** Plans, sections, schematics, schedules, and reports are generated from the design and issued — and regenerated as the design changes. Because deliverables derive from the same objects the engineer edits, updating after a change is a regeneration, not a redraft.

Discipline-specific loops sit inside this frame:

- *HVAC*: loads → air volumes → system selection → duct routing → duct sizing and pressure-loss/sound verification.
- *Electrical*: demands → circuit grouping → panel schedules → cable routing → cable sizing and verification; lighting design may be verified in-product or in linked specialist tools.
- *Plumbing*: fixture units and demands → pipe routing → supply, hot-water circulation, and drainage sizing against the applicable standard.
- *Fire protection*: hazard classification → sprinkler layout → hydraulic calculation of the most demanding zone.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Model / drawing canvas

The primary work surface: the building in plan (and, in model-based products, in 3D), with the services laid over it.

- shows the building context and the discipline's components in place
- primary actions: route a network, place a component, connect, edit geometry and parameters, inspect a component's data

### Discipline toolsets / palettes

The per-discipline catalogs of components and drawing tools.

- organized by system type (ducts, pipes, cables, sprinklers; terminals, fixtures, luminaires)
- primary actions: pick a component family or real product, set size and parameters, place and connect

### Calculation dialogs and reports

Where the engineering happens visibly.

- show the quantities behind the design: loads per room, flows per section, pressure losses, cable results, sprinkler hydraulics
- primary actions: choose the calculation standard and options, run the calculation, read and filter results, apply sizes back to the model

### Schedules / bills of materials

Tabular views generated from the designed components.

- list components with counts, sizes, part numbers, and technical data
- primary actions: filter, group, export (commonly to spreadsheets), feed procurement or fabrication

### Schematic editors

Diagram surfaces alongside the physical layout.

- single-line electrical diagrams, switchboard schematics, riser and system schematics
- primary actions: draw the schematic, keep it synchronized with the physical design, annotate

### Coordination views

Where disciplines meet.

- combined views of multiple discipline models, collision listings, issue lists
- primary actions: inspect clashes in context, assign and track issues, update after resolution

### Sheet / deliverable composition

Where drawings and reports are assembled for issue.

- plan and section views placed on sheets, title blocks, report templates
- primary actions: place and update views, annotate, publish or print

## Important Rules / Behaviors

### Calculations are standard-dependent

Sizing and verification are performed under named calculation standards, and the standard is a user-selectable setting that changes the numbers: domestic-water sizing, duct pressure loss, sprinkler hydraulics, and electrical calculations each have national and international variants (for example ASHRAE, CIBSE, DIN, EN, and NFPA families in the researched sample). The same layout sized under different standards can yield different results; products localize to the standards of their markets, and choosing the standard is part of setting up the design.

### Loads come from the building, flows come from connectivity

Room and zone data drive load and air-volume calculations; the connectivity graph drives flow accumulation and sizing. A terminal that is placed but not connected to its system contributes nothing to the network calculation — connectivity is load-bearing, not cosmetic.

### Deliverables derive from the design objects

Schedules, drawings, and reports are generated from the components and their parameters. Editing the design and regenerating is the normal update path; hand-edited deliverables drift out of sync. Some products extend this to bidirectional associativity, where editing a drawing updates the model.

### Coordination is a continuous constraint

Services must fit within ceiling voids, shafts, and risers alongside structure and each other. Collision checking against the other disciplines' geometry is a standing verification step, and unresolved clashes block deliverable issue in model-based practice.

### The design is versioned with the building

The architectural design changes during the project. The services design is repeatedly updated against the new context — rooms move, levels change — so the application's ability to re-anchor the design to a revised building context is a structural behavior, not a convenience.

### Verification gates issue

Calculation and compliance results (load summaries, pressure-loss and sound results, cable verifications, sprinkler hydraulics, energy or code-compliance outputs where packaged) are part of the deliverable set. A design that does not verify is not issued; the calculation report is evidence, not an afterthought.

## Variants

- **By discipline scope** — full multi-discipline environments (mechanical, electrical, plumbing, fire in one product); HVAC-only design tools (loads and duct design for residential and light-commercial work); electrical-design or piping-specialist tools. Scope varies with market: small residential practices run lighter, single-discipline tools; large consultancies run multi-discipline model-based environments.
- **By working method** — drafting-first (2D layouts with attributed components), model-first (object-oriented 3D BIM with generated deliverables), and hybrid 2D/3D working; the same Type spans all three, and older regional products remain drafting-based.
- **By calculation depth** — sizing-level calculation embedded in layout; dedicated load-design tools that model the building primarily to compute loads and compare system alternatives; and products that add dynamic thermal simulation, energy analysis, and economic comparison of design variants.
- **By platform form** — standalone applications; discipline modules or plugins that run inside a host CAD or BIM platform; and modules inside full multi-discipline building-design suites.
- **By market/regional standards** — products localize their calculation engines, component catalogs, and deliverable formats to national and regional standards; the same Type looks different in different markets while keeping the same core.
- **By downstream depth** — design-grade deliverables for permitting and installation vs fabrication-grade output (part numbering, production models, supports and hangers) feeding manufacture and assembly.
- **By compliance packaging** — bundled energy-code, certification, and incentive workflows (energy codes and standards compliance, certification schemes, tax-incentive documentation) depending on the market's regulatory regime.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| BIM Authoring | sibling / container | discipline-agnostic model authoring for all building parties; MEP Design is the building-services slice with its own objects and engineering loop |
| Architecture Design Application | adjacent discipline | designs spaces and envelope; MEP designs the services within; shares the building context, differs in objects and calculations |
| Structural Engineering Design | adjacent discipline | designs the load-carrying frame; different physics (member forces vs flows and capacities in networks) |
| Electrical Design Application | partial overlap, seam unresolved | building electrical design is one discipline inside MEP Design; industrial/power-systems electrical design is a different object world — the boundary needs its own research pass |
| Mechanical CAD | adjacent, different domain | designs products and machines; context is an assembly, not a building serving occupants |
| HVAC Load Calculation / Energy Modeling tools | calculation-led sibling pole | model the building to compute loads and compare systems; may lack physical network layout and installation deliverables — the seam is real and products exist at the edge |
| Building Energy Management / BMS | downstream, operations-time | operates the finished building's systems through control logic; MEP Design produces the design-time model those systems are built from |
| Construction Estimating / Quantity Takeoff | downstream consumer | prices and counts what MEP Design's schedules and models quantify |
| Building Commissioning | downstream, verification | verifies installed systems against design intent; consumes the design deliverables MEP Design produces |

The most important boundary is with **BIM Authoring**: the two overlap because MEP design work happens inside general BIM platforms. The structural difference is the discipline focus — MEP Design is defined by building-services objects and the sizing/verification loop, not by the platform the work happens in.

## Representative Products

- **MagiCAD** (for Revit / AutoCAD / BricsCAD) — MEP-specialized design layer with discipline modules, integrated calculations, per-country standard selection, and manufacturer BIM-object content; strong in European engineering consultancies.
- **ALLPLAN with AX3000** — MEP engineering inside a multi-discipline BIM platform: single building model, discipline modules (sanitation, heating, electrics, ventilation, sprinklers), load and ductwork calculations, deliverables generated from the model.
- **Trane TRACE 3D Plus** — calculation-led HVAC design: building canvas, hourly load design on an established simulation engine, system/plant configuration, energy and compliance analysis.
- **Wrightsoft Right-Suite Universal** — residential/light-commercial HVAC design: code-recognized load calculation methods, duct design, drawing tools, energy-code links.
- **Autodesk Revit and AutoCAD (MEP toolset)** — the market-dominant general platforms on which much MEP design is performed and into which discipline software integrates. (See Sources for a research limitation on these products' documentation.)

## Sources

Research date: **2026-09-09**

- MagiCAD Group — MEP Design overview: https://www.magicad.com/mep-design/ ; Ventilation module: https://www.magicad.com/applications/magicad-ventilation/ ; Piping module: https://www.magicad.com/applications/magicad-piping/ ; Electrical module: https://www.magicad.com/applications/magicad-electrical/ ; Supported standards and localisation: https://www.magicad.com/mep-design/resources/standards-and-localisation/
- ALLPLAN — MEP Engineering solution page: https://www.allplan.com/industry-solutions/mep-engineering-software/ ; company root: https://www.allplan.com/en/
- Trane — TRACE 3D Plus product page: https://www.trane.com/commercial/north-america/us/en/products-systems/design-and-analysis-tools/trace-3d-plus.html
- Wrightsoft — Right-Suite Universal product overview: https://wrightsoft.com/
- Carrier (commercial software navigation, incl. HVAC system design software line): https://www.commercial.carrier.com/

> Sourcing limitation: official Autodesk documentation for Revit and AutoCAD MEP could not be fetched from the research environment (product pages returned access errors; the help center rendered as an application shell; archived and third-party reference sites were unreachable). Revit and AutoCAD MEP are therefore named as market anchors on the strength of other vendors' official statements about these platforms, and no precise claims about their native feature sets are made in this document. Vendor marketing performance claims encountered during research were excluded from the evidence base. Detailed product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
