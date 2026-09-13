# CAM (Computer-Aided Manufacturing)

## Overview

A **CAM application** is manufacturing-preparation software: it takes the geometry of a part to be made, computes the motion of the machine that will make it, and produces a machine-executable program for a specific machine and control.

The defining structure is small:

```text
Part geometry (the thing to be made)
  → computed machine/tool motion (the toolpath)
    → machine-executable manufacturing program (NC code) for a specific machine/control
```

Everything else commonly associated with CAM — stock models, tool libraries, machining simulation, feature recognition, nesting, CAD authoring, AI assistance — is widespread in mature products but is not what makes a product a CAM. The Type has been structurally stable since its earliest form in the 1950s, when part geometry and tool motion were described in a dedicated programming language and the computer computed the cutter path for post-processing into machine control data; the same three-part skeleton holds for today's desktop suites, CAD-embedded add-ons, and hobbyist router software.

The boundary is equally clear: CAM is not the design tool (that is CAD — CAD answers what the part looks like, CAM answers how to make it), not the machine's controller (which executes the program at the machine), and not the production scheduler (which decides when and in what order work runs). CAM sits between design and execution: it turns a design into instructions a machine can run.

## Users & Context

**Primary users:**

- **CNC programmer / manufacturing engineer** — the central role: receives a part design, decides how it will be machined, and produces the machine program. This person understands both the geometry and the behavior of the shop's machines, tools and materials.
- **Machinist / machine operator** — receives the program, sets up the machine, and runs it; in many shops the operator is also the programmer for simpler work.

**Secondary users:**

- **Design engineer** — in CAD-integrated products, prepares designs for manufacturability while the design is still being developed, rather than after it is finished.
- **Small-shop owner / maker** — in the hobbyist and light-fabrication segment, one person often does the drawing, the programming, and the cutting.

**Context:** machine shops (milling, turning), mold and die work, aerospace/automotive/medical part production, woodworking and sign shops (CNC routers), fabrication shops (plasma, laser, waterjet cutting), and makerspaces. The work is engineering-side and preparatory: the output is a program that a machine executes later, on the shop floor. Mistakes caught late are expensive — machine time and material are consumed by bad programs — which is why verification before cutting is a central practice.

## Core Model

### The Defining Core

Three structures. Remove any one and the product is no longer CAM:

- **Part geometry as input.** The thing to be made exists as geometry — imported from a CAD model or drawn inside the application. The geometry is the authority the program must produce; every computed motion is justified by it.
- **Software-computed machine motion.** The application computes the path of the machine's working implement — a milling cutter, a lathe tool, a plasma or laser head — from that geometry, under a machining strategy the programmer selects and parameterizes. The motion is *computed from geometry by the software*. This is what distinguishes CAM from hand-written machine programs: the programmer describes intent and context, the system derives the physical path.
- **Machine-executable program as output.** The computed motion is translated into control data that a specific machine and control can execute — G-code-class NC code in the common case. The output is always for a *specific* machine/control combination, not an abstract machine.

### The Machining Process Layer

Around that core, mature products share a stable process model:

- **Setup** — how the part is oriented and held on the machine (workpiece orientation, fixtures, vises). Operations are grouped under setups.
- **Operation** — one machining step (a roughing pass, a finishing pass, a hole cycle). The operation is the working unit of programming: it binds a strategy, a tool, and cutting parameters to a region of the geometry.
- **Strategy** — the machining method an operation applies: how material is removed or the cut is made (roughing, finishing, drilling, threading, engraving, contouring, pocketing).
- **Tool** — the implement an operation uses: cutter geometry, holder, and its cutting parameters (feeds, speeds, depths of cut, allowances left for later passes).
- **Stock / workpiece** — the starting material shape the operations act on, in subtractive machining; in sheet cutting, the sheet itself plays this role.
- **Machine and control definition** — the axes, kinematics and travel limits of the target machine; the program's ultimate frame of reference.

### Post-processing: One Structure, Many Implementations

A distinctive and remarkably stable element of the Type is the **two-stage output architecture**: the system first computes machine-independent motion, then a **post processor** translates that motion into the dialect of a specific machine and control. Post processors are maintained per machine/control combination — mature vendors build and maintain large post libraries, often in collaboration with control manufacturers, because the same computed path must become correct code for many different machines. The conceptual requirement is the machine-executable output; the separate post-processing stage is the dominant way the market implements it.

```text
Concept:            part geometry
Implementations:    imported CAD model (native or neutral exchange formats),
                    profile drawn in the application,
                    2D data formats (DXF-class formats are common in the cutting segment)

Concept:            machining strategy
Implementations:    operation libraries chosen by the programmer,
                    feature recognition that proposes operations from geometry,
                    rules/knowledge-based automation encoding shop standards

Concept:            machine-executable output
Implementations:    post-processed NC programs per machine/control,
                    configurable or custom post processors,
                    transfer of the program to the machine
```

### Standard Capabilities of Mature Products

These are common across the researched sample and the market, without being definitional:

- CAD import (and, in many products, CAD authoring in the same environment)
- Stock and fixture definition in the machining context
- Tool libraries and tool assemblies
- An operation tree / program manager organizing setups and operations
- Toolpath simulation and verification — from a simple path preview to material-removal simulation and full machine-kinematics simulation that detects collisions and travel-limit violations
- Cycle time estimation
- Program output and transfer to the machine

## How It Works

### The canonical programming loop

```text
Bring in the part geometry (import a CAD model, or draw the profile)
→ define the manufacturing context (stock, machine, how the part is held)
→ plan the machining (create setups and operations; choose strategies;
   assign tools; set feeds, speeds, depths)
→ compute the toolpaths
→ simulate and verify (path preview → material removal → machine motion;
   catch collisions and travel-limit violations)
→ post-process to the target machine/control
→ output or transfer the NC program to the machine
→ iterate (design changes and program corrections loop back)
```

The loop is fundamentally iterative: a design revision, a different machine, a broken tool or a shop-floor correction all send the programmer back to an earlier step, and the computed motion is regenerated.

### The cutting-segment form of the same loop

For plasma, laser, waterjet and router cutting of sheet material, the loop takes a characteristic shape:

```text
import 2D profiles
→ nest the parts on the sheet (arrange, copy, rotate to minimize waste)
→ define the cutting technology (cut width compensation, cut ordering,
   piercing, head height control)
→ compute the cut paths
→ post-process and transfer to the cutting machine
```

### The CAD-embedded form

In CAD-integrated products the loop starts inside the design environment. The machining model is associated with the design model, so a design change propagates into the machining program automatically; programming can proceed concurrently with design rather than after it. In standalone products, the updated model is re-imported and operations are regenerated against it.

### Capability tiers

- **Defining core** — part geometry input; software-computed machine motion; machine-executable program output.
- **Standard capabilities** — setups/operations/strategies/tools; stock and machine definition; post-processing; simulation and verification; cycle time estimation; CAD import.
- **Common variants and optional capabilities** — feature recognition and rules/knowledge-based automation; tolerance-driven programming that reads model annotations; nesting and cutting-technology machinery; multiaxis and mill-turn depth; additive or inspection extensions in some suites; AI assistance in some current products.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### 3D viewport

The spatial work surface.

- shows the part, the stock, fixtures, and the computed toolpaths in position
- primary actions: inspect geometry and paths, run simulation, examine the result of an operation

### Operation / program manager

The organizational spine of a program.

- lists setups and their operations as a tree, with tools and states
- primary actions: create/reorder/copy operations, assign tools, regenerate paths, post-process

### Operation parameter dialogs

Where machining intent is expressed.

- strategy selection, tool selection, cutting parameters, depths and allowances, linking/approach moves
- primary actions: choose and tune a strategy, confirm and compute

### Simulation / verification view

The safety surface between computation and cutting.

- path backplot, material removal, and in the most complete form the full machine with kinematics
- primary actions: play/step through the program, detect collisions and travel-limit violations, inspect the resulting surface

### Post processor management

The machine-specific translation surface.

- selection of the post processor for the target machine/control, configuration of machine-specific options
- primary actions: select/configure a post, generate the NC program

### NC program view

The output surface.

- the generated machine code for the selected operation or program
- primary actions: review, save, transfer to the machine

### Nesting view (cutting segment)

The sheet-utilization surface.

- parts arranged on the sheet with spacing and orientation controls
- primary actions: auto-nest, manual arrange, copy/rotate/mirror parts

### Tool library

- cutter and holder definitions with their parameters
- primary actions: create/edit tools, assign to operations

## Important Rules / Behaviors

### The program is machine-specific

The same computed motion produces different code for different machines and controls. Post processors are built per machine/control combination — in mature products, often with the control manufacturer's involvement — because correct output depends on the controller's dialect and the machine's kinematics. A toolpath computed for one machine cannot simply be sent to another.

### Toolpath validity is contextual

A toolpath is only valid against the context it was computed for: the stock, the fixtures, the tool, the machine limits. Change the context and the path must be recomputed. Fixture collisions in particular are a recurring failure mode, which is why products let the programmer model fixtures and verify against them.

### Verification precedes cutting

Mature practice is to catch errors in simulation, not at the machine: a collision or a travel-limit violation discovered at the machine costs machine time and material. The most complete form of verification simulates the actual machine motion implied by the final NC code, not just the computed path.

### Design changes propagate — or must be re-imported

In CAD-integrated products, a design change updates the machining model and its operations automatically. In standalone products, the revised model is re-imported and the program is regenerated. Either way, the geometry remains the authority: the program never outlives its geometry.

### Automation encodes shop standards

Rules- and knowledge-based products let a shop encode its preferred strategies, tools and parameters once, so that repeated programming follows house standards and the programmer concentrates on the critical decisions rather than every feature.

### Cutting has its own process rules

In the cutting segment, the cut width must be compensated for (the path is offset so the finished part has the right dimensions), the order of cuts and the piercing strategy affect quality and distortion, and head height control governs the distance between the cutting head and the material.

### Estimates feed decisions before production

Cycle time estimation lets quoting and production planning account for the machining work before committing to production.

## Variants

- **By machining family** — milling (from 2.5D profile work to 3D surface and multiaxis machining), turning, mill-turn and Swiss-style machining, wire EDM, router work, laser/plasma/waterjet cutting, engraving. Products often specialize by family; large product lines cover several.
- **By delivery form** — standalone desktop application; add-on embedded in a CAD environment; module of an integrated CAD/CAM suite; some suites extend toward additive manufacturing or on-machine inspection.
- **By automation depth** — manual operation-by-operation programming; feature recognition with rules/knowledge-based automation; tolerance-driven programming that reads annotations in the model.
- **By customer tier** — industrial products (deep multiaxis, machine-kinematics simulation, post libraries built with control makers); prosumer cutting products (nesting-centric, one-time licenses); hobbyist/maker products (2D/2.5D router work, template-driven project flows, community project libraries).
- **By segment practice** — the cutting segment adds nesting, kerf compensation and cut ordering; the milling segment adds stock-aware roughing and high-speed machining strategies.

A variant remains a variant of this Type as long as the defining core holds: geometry in, computed motion, machine-executable program out.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Mechanical CAD | upstream | authors the geometry CAM consumes; design definition vs manufacturing motion computation |
| CNC Programming Application | probable alias / sibling leaf | the market uses "CAM software" and "CNC programming software" interchangeably — CAM's defining output *is* a CNC program; flagged for joint review |
| Additive Manufacturing Software | structurally adjacent | same skeleton (geometry → computed motion → machine output) but builds material layer by layer instead of machining it; some CAM suites include additive modules |
| Manufacturing Execution System / Production Planning | downstream | schedules and tracks production; CAM prepares the program a machine will run |
| CAE / Engineering Simulation | different question | predicts how a design behaves under physical conditions; CAM computes how to make it |
| Shop Floor Management / Machine monitoring | downstream | operates and observes the machines in production; CAM is engineering-side preparation |
| Tool Management | adjacent | administers the physical tool inventory; CAM references tool definitions inside programs |

The boundary with CAD is the cleanest: CAD defines what the part looks like; CAM defines how to make it. The boundary with the machine controller is equally clean: the controller executes the program at the machine; CAM produces it. The genuinely unresolved boundary is with the sibling leaf "CNC Programming Application", which the market treats as the same product category CAM vendors sell.

## Representative Products

- **Mastercam** — standalone CAM market leader; product family spanning mill, lathe, mill-turn, Swiss, router and wire EDM
- **SOLIDWORKS CAM** (powered by CAMWorks) — CAD-embedded CAM with rules-, knowledge- and tolerance-based automation
- **Vectric** (Cut2D / VCarve / Aspire) — hobbyist and small-workshop router CAM for woodworking and sign work
- **SheetCam** — prosumer cutting CAM (plasma/router) with nesting and cutting-technology machinery
- **APT (Automatically Programmed Tools)** — the 1950s language-based ancestor, included as the historical anchor

The definition was deliberately checked against the historical language-driven form (no GUI, no simulation, no stock models) and against hobbyist and cutting-segment products, so that it does not over-fit the modern industrial desktop pattern.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces (product-page level):

- Mastercam — https://www.mastercam.com/ , https://www.mastercam.com/solutions/products/ , https://www.mastercam.com/solutions/post-processors/
- SOLIDWORKS CAM — https://www.solidworks.com/product/solidworks-cam
- Vectric — https://www.vectric.com/
- SheetCam — https://www.sheetcam.com/
- DBpedia (APT, programming language) — https://dbpedia.org/page/APT_(programming_language)

> Sourcing limitation: no help-center / user-guide level documentation was reachable for any sampled product during the research window (vendor help domains were blocked, redirected or JS-gated; the high-end enterprise products in this category could not be fetched at all). All product evidence is therefore product-page level, plus one third-party historical extract. Precise operational details (numeric limits, parameter defaults, exact state names, format lists beyond those directly observed) are intentionally not stated in this document; such details remain in the paired Research Notes, and claims here are calibrated to the reachable evidence.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical breadth check are recorded in the paired Research Notes.
