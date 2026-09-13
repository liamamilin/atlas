# Additive Manufacturing Software

## Overview

An **Additive Manufacturing Software** (in everyday use: 3D printing software, or a "slicer") is the application that stands between a 3D model and a 3D printer. It takes geometry created in another tool, places it inside a specific printer's build volume, attaches process settings, generates support structures, slices the model into layers, and produces machine-executable instructions that reach the printer as a file or through a direct connection.

The defining core is small:

```text
3D model input
└── Placement inside a specific printer's build volume
    └── Process settings bound to printer + material
        └── Slicing into layers + machine-executable instructions
            └── Handoff to a printer (file export or direct send)
```

Everything else commonly associated with 3D printing software — model repair, print-time estimates, cloud printer monitoring, marketplaces, production nesting — is widespread in mature products but is not what makes the product an additive manufacturing tool. Remove slicing and printer binding and what remains is a mesh viewer or editor; remove the model and there is nothing to print.

The name of the Type is broader than its core. Vendors use "additive manufacturing software" as an umbrella that also covers printer-fleet management, analytics, and simulation. This document covers the preparation-and-instruction core; fleet and production management appear here only as an adjacent structure (see Related Application Types).

## Users & Context

The primary user is a person who needs to turn a 3D model into a physical part on a 3D printer:

- **hobbyists and makers** — prepare and print models downloaded or designed at home, usually on one filament printer
- **engineers and designers** — produce prototypes, jigs, fixtures, and end-use parts from CAD data, often across several printers and materials
- **print operators and technicians** — run builds on industrial machines, prepare trays of parts, and keep printers fed with valid print files

Secondary concerns sit with the surrounding organization: IT administrators who deploy and manage the software across a company, and production managers who watch queues and printer utilization through companion fleet products rather than the preparation tool itself.

The work happens at a desk, in front of the printer, or — in production settings — at a dedicated preparation workstation. The software is typically a desktop application; cloud and printer-embedded variants exist (see Variants).

## Core Model

### The Defining Core

**Model.** The input object: 3D geometry produced by a CAD application, a 3D modeling/sculpting tool, a scanner, or downloaded from a model library. It arrives as a mesh file (STL, 3MF, OBJ are common interchange formats) or, in more capable products, as native CAD geometry. The software does not create this geometry; it consumes it.

**Printer profile (machine definition).** A description of a specific printer: its build volume, motion capabilities, number of extruders or light sources, and the output format it accepts. The printer profile is what makes the software printer-bound. Preparation always happens *for* a particular machine.

**Build volume / build plate.** The virtual space mirroring the printer's physical build area. The user places one or more model instances on it, positions, rotates, scales, and — critically — chooses the orientation in which the part will be built. Orientation is a first-class decision because it drives support needs, surface quality, and build time.

**Process settings.** The parameters that tell the machine *how* to build the part: layer height, wall thickness, infill, temperatures, speeds, exposure or sintering parameters depending on the technology. Settings are bound to the printer-and-material combination. Products expose them through preset profiles (quality presets, application-oriented "intent" profiles, vendor material profiles) and, for advanced users, through extensive custom controls.

**Supports.** Generated auxiliary geometry that holds overhangs and bridges during the build and is removed afterward. Related adhesion and stabilization aids (brims, rafts, and similar structures) anchor the part to the build plate. Supports belong to the print job, not to the model.

**Sliced output / machine instructions.** The defining transformation. The software decomposes the oriented, supported model into layers and converts each layer into machine-executable instructions — G-code for filament machines, or proprietary build files for other technologies. This output is the product's deliverable.

**Print job.** The unit of handoff: one prepared build (one or more parts with their settings and supports) destined for one printer. Jobs are exported as files or sent directly to a printer, where they may enter a queue.

### How the Objects Relate

```text
Model (from CAD / model library)
  ↓ imported into
Printer profile → defines Build volume + valid Process settings
  ↓
Placement (position / orient / scale instances on the build plate)
  ↓
Supports + adhesion aids generated for that placement
  ↓
Slicing → machine instructions (G-code / build file)
  ↓
Print job → handed to printer (file or direct send)
```

The center of gravity is the **print job**: everything the user does converges on producing one valid job for one machine. The **printer profile** is the frame around every decision — the same model prepared for two different printers yields two different jobs.

### One Structure, Many Implementations

The core is conceptual; products implement it differently:

```text
Concept:            Machine instructions
Implementations:    G-code (filament machines), proprietary build files (powder,
                    photopolymer, jetting), vendor-specific job packages

Concept:            Handoff
Implementations:    file export (SD card / USB), local network send,
                    cloud send with remote monitoring

Concept:            Process settings
Implementations:    quality presets, application/intent profiles,
                    vendor material profiles, fully custom parameter sets
```

A reader who has only seen one implementation (for example, a desktop slicer exporting G-code) should still be able to recognize industrial build-preparation suites and printer-embedded tools from this core model.

## How It Works

The canonical workflow runs from model to printed part:

```text
Import model
→ choose printer + material
→ place and orient on the build plate
→ attach process settings (preset or custom)
→ generate supports
→ validate and preview the sliced result
→ slice
→ hand off to the printer
→ (optionally) monitor the build
```

**Import.** The user brings in one or more models. Products differ in how much they accept: mesh formats everywhere; native CAD formats (for example STEP/IGES) in more professional tools, which spares the user a mesh-conversion step. Assemblies can be imported as multiple bodies.

**Choose printer and material.** Preparation is meaningless without a target machine. The user selects a printer profile and a material; this choice constrains the build volume, the available settings, and the output format.

**Place and orient.** The user arranges instances on the build plate. Orientation is the highest-leverage decision: it determines which surfaces need supports, which faces will show layer lines, and how long the build takes. Products provide automatic orientation aids; some industrial products add orientation analysis.

**Attach settings.** Most users pick a preset (a quality level or an application-oriented profile); advanced users override individual parameters. Some industrial products allow settings to be assigned per part or even per face of a part.

**Generate supports.** The software computes where the model needs support and adds it, along with plate-adhesion structures. Users can tune or reduce supports; some industrial products add structures that resist toppling of tall thin parts and curling of warping-prone ones.

**Validate and preview.** Before committing, the user inspects the sliced result layer by layer and checks the model for defects that would make it unprintable. Many products flag or repair such defects. Time and material estimates inform the go/no-go decision.

**Slice and hand off.** Slicing produces the machine instructions. The user then either exports the file (to storage the printer reads) or sends the job directly to a connected printer. In connected setups the job enters a printer queue; in production setups, queues, scheduling, and approval live in companion fleet products.

**Monitor.** Monitoring the build in progress is a common companion capability — through the same application, a local printer web interface, or a cloud service. Monitoring is not part of the defining core: a preparation tool that only exports files is still fully an additive manufacturing tool.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Build-volume viewport

The primary surface: a 3D view of the build plate with the placed models.

- typical information: build volume outline, model instances, supports, plate origin
- primary actions: import, move/rotate/scale, duplicate, lay flat, arrange multiple parts

### Settings panels

The parameter surface, usually a sidebar or dialog set.

- typical information: print settings grouped by category, material, quality level
- primary actions: pick a preset, switch to custom mode, adjust individual parameters, save a profile

### Slice preview

The verification surface: the model rendered as the machine will build it, layer by layer.

- typical information: per-layer toolpath or exposure, supports, estimated time and material
- primary actions: scrub through layers, inspect regions, confirm or go back and adjust

### Model/project list

The organization surface for multi-part builds.

- typical information: parts in the current job, per-part settings, group/assembly structure
- primary actions: assign settings per part, exclude parts, group edit

### Printer connection / queue surface

The handoff surface, present in connected products.

- typical information: available printers, their state, queued jobs
- primary actions: send job, select printer, monitor progress

### Profile manager

The configuration surface for printer and material definitions.

- typical information: installed printers, materials, custom profiles
- primary actions: add a printer, import a material profile, manage plugins/extensions (where the product has an ecosystem)

## Important Rules / Behaviors

**Output is printer-specific.** A sliced job is valid for the machine profile it was prepared for. Preparing the same model for a different printer means re-preparing against that machine's profile; instructions are not interchangeable across machines.

**Settings bind to printer + material.** Process parameters are only meaningful for a given machine-and-material combination. Switching either invalidates or reshapes the available settings; this is why profiles, not raw numbers, are the everyday unit of configuration.

**Supports are job geometry, not model geometry.** Generated supports and adhesion aids belong to the print job and are removed after the build. The source model is not modified by preparation (some products offer optional repair operations, which are explicit edits, not side effects).

**The slice preview is the source of truth.** What the preview shows — toolpaths, supports, layer structure — is what the machine will execute. Discrepancies between the model view and the sliced preview are resolved in favor of the preview.

**Unprintable geometry blocks the pipeline.** Models with defects that would make them unprintable must be repaired or explicitly accepted before a valid job can be produced; products flag or auto-repair such defects.

**Estimates are predictions.** Build time and material usage shown before printing are model-based estimates, not guarantees; actual values depend on the machine and material behavior.

**Handoff mode is a product property, not a user choice.** Whether a job travels as a file or through a direct connection is determined by the product and printer ecosystem; the preparation core is the same in both cases.

## Variants

Common forms of the Type:

- **Desktop slicer (open, multi-vendor)** — a standalone application supporting many printers through profiles; the dominant hobbyist/prosumer form. Output is typically a file; printer connection is optional.
- **Vendor-ecosystem slicer** — an open-source or bundled desktop tool centered on one printer maker's machines, with tight integration into that maker's monitoring services.
- **Printer-integrated preparation** — preparation running on or beside the printer itself; the build volume and settings come from the machine directly.
- **Industrial build-preparation suite** — multi-technology preparation for production environments: native CAD import, per-part/per-face settings, printability validation, production features such as nesting of many parts, build reports, and costing, and machine-specific build files across filament, photopolymer, powder, and jetting technologies.
- **Cloud slicer** — the same preparation core hosted in a browser, usually as part of a vendor's fleet platform; enables preparation without installation and from any device.
- **CAD-suite embedded module** — additive preparation shipped inside a CAD/CAM suite as a workspace, sharing the CAD session's geometry directly.

A variant remains a variant while the defining core holds. When the center of gravity moves to managing many printers, people, and production statistics — rather than preparing individual jobs — the product has crossed into fleet/production management (see Related Application Types).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| CAM / CNC Programming Application | closest sibling | both turn CAD models into machine instructions; CAM targets subtractive machines (cutting toolpaths, fixtures, cutting parameters), AM software targets printers (layer slicing, supports, printability) |
| 3D Modeling Application | upstream | creates/edits the geometry that AM software consumes; AM tools only repair and prepare, they do not model |
| Manufacturing Execution System / print-farm management | adjacent, downstream | manages printers, queues, users, approvals, and statistics at fleet scale; vendors ship it as a separate product even when branding sits next to the slicer; it cannot create print files, the slicer cannot run a fleet |
| 3D Rendering Application | different output modality | rendering produces images; AM software produces machine instructions for physical parts |
| Print-on-demand Commerce Platform | adjacent, commercial | ordering parts as a service vs preparing them for one's own printer; some prep tools integrate ordering, but the transaction is not part of the core |
| 3D Animation / 3D Creation Applications | different domain | both use 3D geometry, but animation targets rendered motion, not machine-built physical output |

The most important boundary is with **CAM**: the two Types share the "CAD → machine instructions" shape, and some suites bundle both. The structural test is the machine process — subtractive material removal versus additive layer building — and the printability-specific work (supports, orientation) that only exists on the additive side.

The second most important boundary is with **fleet/production management**: in the researched sample, every vendor that offers both ships them as separate products (a desktop/cloud slicer plus a monitoring/farm service), which is direct evidence that preparation and fleet operation are distinct structures even inside one brand.

## Representative Products

- **UltiMaker Cura** — free open-source desktop slicer; the reference form of the multi-vendor desktop variant, with preset/intent profiles, custom parameter mode, a material/plugin marketplace, and an enterprise edition for IT-managed deployment.
- **PrusaSlicer** — open-source slicer centered on one printer maker's ecosystem; its job ends at exported print files, with printer monitoring and farm control delegated to separate companion services (a local printer web interface and a cloud farm service).
- **GrabCAD Print / GrabCAD Print Pro** — industrial print-preparation client built into a printer maker's machines; native CAD import, printability validation, support generation with anti-toppling/anti-curl structures, print queues, multi-printer control, and production features (nesting, costing, build reports) across several printing technologies.

The industrial build-preparation tier (for example, long-established European AM build-preparation suites) was identified as part of the market structure but its official documentation could not be reached during research; claims about that tier are calibrated accordingly and the core model was checked against the industrial evidence available through the sampled products above.

## Sources

Research date: **2026-09-06**

- UltiMaker — UltiMaker Cura product page — https://ultimaker.com/software/ultimaker-cura/
- UltiMaker — UltiMaker Digital Factory product page — https://ultimaker.com/software/ultimaker-digital-factory/
- Prusa Research — PrusaSlicer product page — https://www.prusa3d.com/p/prusaslicer/
- Prusa Research — "Prusa Connect and PrusaLink explained" (Knowledge Base) — https://help.prusa3d.com/article/prusa-connect-and-prusalink-explained_302608
- Stratasys / GrabCAD — GrabCAD Print product page — https://grabcad.com/print
- Stratasys / GrabCAD — GrabCAD Print Getting Started (Help Center) — https://support.stratasys.com/Software/GrabCAD-Print/Getting-Started

> Sourcing limitation: official documentation for Bambu Studio (integrated consumer/prosumer ecosystem) and for Materialise Magics (industrial build-preparation suite) was not reachable from the research environment on 2026-09-06 (repeated 404s / transport errors). These products are therefore not used as evidence; assertions about the industrial tier and about single-product integrated ecosystems are correspondingly weakened, and no precise operational details (parameter counts, storage limits, format specifics beyond those directly observed) are stated in this document.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
