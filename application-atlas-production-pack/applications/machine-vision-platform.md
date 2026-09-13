# Machine Vision Platform

## Overview

A **Machine Vision Platform** is the software layer that builds and operates image-based automatic inspection, identification, and guidance applications on production lines. It acquires images from industrial cameras under line synchronization, processes them with configurable vision tools, produces a decision about each item — pass/fail, measurement, identification, position — and delivers that decision to the production process so the line can act on it: reject, sort, mark, guide a robot, or record the result.

The defining structure is small:

```text
Industrial cameras / frame grabbers
└── Configured image acquisition (triggered and timed to the line)
    └── Vision application (the unit of record)
        └── Vision tools (locate / measure / inspect / identify / classify)
            └── Per-item results and pass/fail decisions
                └── Line integration (signals and data to PLCs and equipment)
```

Everything else commonly associated with modern machine vision — deep-learning tools, 3D vision, graphical IDEs, recipe databases, edge deployment, specific camera interfaces and protocols — is widespread in current products but is not part of the defining core. Older generations (camera + frame grabber + tool library + discrete I/O to a PLC), smart cameras with the software inside, and regional integrated-system vendors all fit the same definition without any of those specifics.

When the software stops deciding per item inside a production process — when it only observes and aggregates, or only measures with metrology-grade traceability, or only builds general models — it is drifting toward a different Application Type (Industrial IoT monitoring, Inspection & Metrology Software, Machine Learning Platform).

## Users & Context

The primary users are engineers who make the line "see":

- **vision engineer / system integrator**: builds the vision application — configures the camera and lighting, places and connects vision tools, sets pass/fail criteria, wires the results to the line's control system
- **machine builder / OEM developer**: embeds vision applications into the machines they ship, often using a library or configuration environment rather than writing everything from scratch

Secondary users operate and supervise the result:

- **line operator**: watches the live view and verdicts, responds to rejects and errors, performs product changeover
- **quality engineer**: reviews logged results and reject images, tunes tolerances, re-teaches tools when the product or conditions change
- **maintenance / controls engineer**: keeps cameras, lighting, triggers, and communication healthy

The work environment is the factory floor: the software runs next to PLCs, robots, reject mechanisms, and motion systems, on PCs, industrial controllers, smart cameras, or edge devices. Development typically happens on an engineering workstation; execution happens continuously in production, synchronized to the line's cycle.

## Core Model

### The Defining Core

Three structures. If any one is removed, the product is no longer recognizable as a machine vision platform:

- **Configured camera-driven image acquisition** — the platform acquires images from industrial cameras and/or frame grabbers as a first-class, configured part of the application: exposure, gain, lighting, and above all the trigger that fires the image at the right moment in the line's motion. Without this, the product is a generic image-processing library or a camera utility.
- **The buildable vision application** — a persistent, editable program of vision tools that computes per-item results and pass/fail decisions from images. It is saved, versioned, re-executed for every item, and adapted per product variant. Without this, the product is a camera SDK or offline image analysis.
- **Line-integrated execution** — the vision run is synchronized with the production process (triggers, encoders, handshakes) and its results — verdicts, measurements, code contents, positions — are delivered to line equipment (PLCs, rejectors, robots) so the process can act. Without this, the product is an offline vision toolkit with no production consequence.

### The Vision Application and Its Tools

The vision application is the center of the platform's world. It is built from **vision tools** — packaged image-processing capabilities that a developer places, configures, and connects. Across the researched sample, the same tool families recur:

- **locating / matching** — find the part or a reference feature in the image; the anchor for everything downstream
- **measurement** — distances, angles, diameters, widths, positions against tolerances
- **presence / defect inspection** — is the component there, is the surface flawed, is the assembly complete
- **identification** — read and verify 1D/2D barcodes, data-matrix codes, and printed characters (OCR)
- **classification** — sort items or defects into categories; in modern products increasingly realized by embedded deep-learning tools trained on example images

A typical application chains these: locate the part → run inspection/measurement/identification tools relative to the located position → combine the tool results into a per-item verdict → emit the verdict and data to the line.

### What Mature Products Add

These capabilities are standard in mature products and make the platform practical, but they do not define the Type:

- **development/runtime separation** — an engineering environment for building and testing the vision application, and a production runtime that executes it continuously
- **calibration** — correcting lens distortion and mapping pixels to real-world coordinates so measurements mean physical units; hand-eye calibration when a robot consumes the results
- **recipe / product-variant management** — multiple saved applications or parameter sets, switched at changeover, commonly driven by the PLC
- **operator frontend** — live image with tool overlays, per-item verdicts, counters and statistics, reject-image review
- **trigger and synchronization machinery** — hardware trigger inputs, encoder support, handshake signals with the line
- **result logging** — per-item results and images stored for traceability and later review
- **deep-learning tools** beside rule-based tools — classification, defect detection, anomaly detection, segmentation, OCR — with training done on images inside the vision workflow
- **3D vision** — height maps, point clouds, laser profilers for dimension, volume, and robot guidance
- **performance machinery** — multicore and GPU acceleration for line-rate throughput

### One Structure, Many Implementations

The core model is conceptual. Products realize it very differently, and the differences are variants, not definitions:

```text
Concept:   Buildable vision application
Realized as:  job of connected tool blocks (PC-based environments)
              script/program over an operator library (vision libraries)
              configured chain of standardized tools (no-code software)
              inspection setup inside an integrated system

Concept:   Line integration
Realized as:  industrial I/O + factory protocols (EtherNet/IP, PROFINET, TCP/IP)
              PLC-driven recipe switching
              sockets / application integration
              built-in line wiring of an integrated vision system

Concept:   Deployment form
Realized as:  industrial PC + any camera
              smart camera / embedded runtime
              integrated controller + cameras sold as one system
              edge device
```

A reader who has only seen one form — say, a smart camera with built-in inspection tools — should still be able to recognize a PC-based development environment or a no-code configuration suite as the same Application Type.

## How It Works

### Build the vision application

```text
Open the development environment
→ configure the image source (camera, exposure, lighting, trigger)
→ capture test images of good and bad parts
→ place vision tools on the image (locate → inspect / measure / identify)
→ configure each tool (regions of interest, reference patterns, tolerances)
→ connect tool results into a pass/fail decision
→ test against sample images until the verdict behaves correctly
→ save the vision application
```

The interaction is image-centered: the developer works directly on captured images, drawing regions and watching tool outputs. Programming models differ — drag-and-drop tool blocks with optional scripting, code over a function library, or pure configuration — but the build loop is the same.

### Deploy to the runtime

The saved application is loaded into the production runtime — on the same PC, an industrial controller, a smart camera, or an edge device — and wired to the line: trigger input in, verdict signals and data out.

### Run in production

```text
Line reaches inspection point → trigger fires
→ camera acquires image
→ vision application executes: locate part → run tools → compute verdict
→ verdict and data sent to the PLC / line equipment (accept, reject, sort, guide)
→ result and image logged
→ next item
```

This loop repeats for every item, at line rate. The vision platform is a per-item decision machine embedded in the line's cycle — not a monitoring dashboard and not a batch analysis.

### Change product

```text
Product changeover
→ operator or PLC selects the recipe for the new product
→ platform switches the active vision application / parameter set
→ first articles verified, then production continues
```

In documented implementations the PLC can reconfigure or switch vision applications on demand, making changeover part of line control rather than a manual re-engineering task.

### Maintain and improve

Rejects and drift feed a continuous loop: review logged reject images → adjust tolerances or re-teach tools → for deep-learning tools, collect and label new example images → retrain → redeploy. The vision application is a living program that is tuned over the life of the line, not a one-time configuration.

### Capability tiers

**Defining core** — without these, not a machine vision platform:

- configured camera-driven image acquisition
- buildable vision application of vision tools
- per-item results and pass/fail decisions
- line-integrated execution with results delivered to the process

**Standard capabilities** — present in most mature products:

- development/runtime separation
- locating, measurement, inspection, identification, classification tool families
- calibration (pixel → world coordinates)
- recipe / product-variant management
- operator frontend with live view and statistics
- trigger/encoder synchronization
- result logging and reject-image review
- deep-learning tools beside rule-based tools
- 3D vision
- performance acceleration

**Optional / variant** — depends on segment, form factor, and customer:

- vision-guided robotics (pose output, hand-eye calibration, bin picking)
- line-scan / continuous web inspection
- edge deployment
- OEM/runtime licensing models
- industry-specific packaging (pharmaceutical, food, battery, electronics)
- AI training environments as separate companion products

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Development environment

The engineer's primary surface for building the vision application.

- image view with tool overlays, tool palette, tool configuration panels, decision logic editor, test-image management
- primary actions: configure acquisition, place/connect tools, set tolerances and pass/fail criteria, run tests, save the application

### Runtime / operator frontend

The surface production staff live with.

- live camera image with result overlays, per-item verdict indicators, counters (total / pass / fail), reject-image gallery, current recipe
- primary actions: acknowledge errors, switch recipes, review rejects, request re-teach or call engineering

### Acquisition and calibration configuration

- camera list and settings (exposure, gain, trigger mode), lighting control, calibration procedure (calibration target, distortion correction, coordinate mapping)

### Communication / I/O configuration

- mapping of vision results to line signals: digital I/O, industrial protocols, sockets; handshake behavior with the PLC; recipe-switch commands

### Result data / logging views

- per-item result records, stored images, statistics and trends for quality review

## Important Rules / Behaviors

### Execution is synchronized to the line

The vision run does not happen on its own schedule. It is fired by the line — a sensor trigger, an encoder position, a PLC command — and its verdict must be back within the line's cycle time. A missed trigger means a missed item; a slow application means a production bottleneck. This timing discipline is structural, not a feature.

### Decisions are per-item

The unit of output is a verdict about the item in the image, plus its measurements and identifications. Aggregated statistics exist, but they are derived from the per-item record, not the other way around.

### Locate first, then inspect

Applications almost universally locate the part (or a reference feature) before running downstream tools, so that inspection regions follow the part's actual position. Position correction is what makes inspection robust to part presentation variation.

### Measurement claims rest on calibration

Measurements in physical units are only meaningful after calibration (distortion correction, pixel-to-world mapping). Uncalibrated tools produce image-space results.

### The recipe determines the active logic

At any moment exactly one vision application (or parameter set) is active per station. Changeover switches it; the PLC commonly drives the switch. Results are interpreted against the active recipe.

### AI tools are trained, then executed

Deep-learning tools follow a different authoring loop than rule-based tools: collect example images → label → train → validate → deploy. After deployment they execute like any other tool inside the vision application, and are retrained when the product or defects drift. Training environments are commonly packaged as companion products beside the platform.

### Results are records

Per-item results and images are logged for traceability — quality audits, reject analysis, and process improvement all consume this record.

## Variants

- **PC-based development platform** — industrial PC + cameras of any brand; graphical development with scripting; favored by integrators for complex, multi-camera, high-resolution applications
- **vision library / toolbox** — a function library plus interactive development environment; the machine builder or OEM developer writes the application and embeds it in their own software; maximum flexibility, maximum engineering effort
- **no-code configuration suite** — applications assembled by configuring standardized tools directly on the image; all-in-one (acquisition, processing, communication, operator frontend); favored where engineers without programming background must build and maintain vision
- **integrated vision system** — controller + cameras + software sold as one system; software configured within the vendor's environment; favored by end-user factories that buy working systems rather than build them
- **smart camera / embedded** — the whole platform inside the camera; single-station simplicity
- **edge deployment** — vision applications run on industrial edge devices, managed centrally
- **vision-guided robotics** — the vision application's output is positions/poses consumed by robots (pick-and-place, bin picking, seam guidance)
- **line-scan / web inspection** — continuous material (film, paper, metal strip) inspected line by line at web speed

A variant remains a variant unless it changes the core structures — for example, a product that only aggregates vision data for dashboards, without per-item decisions delivered to the line, has left the Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Inspection & Metrology Software | adjacent | metrology-grade dimensional verdicts against nominal geometry with traceability, typically off-line or slower; machine vision produces line-rate per-item decisions for 100% in-line inspection — vision-based measurement exists in both, the seam is purpose and operating context |
| Machine Learning Platform | adjacent | model-centric: builds, registers, and serves general ML models; the machine vision platform's unit of record is the vision application, with DL models as embedded tools trained on images inside the vision workflow |
| Data Labeling Platform | capability | labeling appears as a step inside deep-learning tool workflows, not as the platform's core |
| Industrial IoT Platform | adjacent | observes and aggregates process data; machine vision decides per item and actuates (reject/sort/guide signals) |
| SCADA / HMI | adjacent | operator-facing live interface to a controlled process; a vision platform may include an operator frontend, but its core is the automated image-based decision system |
| Robotics Engineering Platform | adjacent | programs and simulates robots; in vision-guided robotics the robot consumes the vision platform's position results |
| Industrial Historian / Monitoring | adjacent | stores and trends process data over time; the vision platform produces the per-item verdicts that such systems may archive |
| Vision Sensor (product form) | variant | a miniaturized integrated product (camera + lighting + software); the software inside still realizes the same core structures — form factor, not a separate Type |

The most important boundary is with **Inspection & Metrology Software**: both "inspect parts with cameras," but the metrology Type is organized around nominal geometry, tolerances, and measurement traceability, while the machine vision platform is organized around the line-synchronized per-item decision loop.

## Representative Products

- **Cognex VisionPro** — PC-based development environment and runtime for complex, custom inspection applications
- **MVTec HALCON** — machine vision library and interactive development environment, deployed into OEM and machine-builder applications
- **MVTec MERLIC** — no-code, all-in-one configuration software for building and operating vision applications
- **Keyence Vision Systems** — integrated vision systems (controller + cameras + software) sold and configured as complete systems

The core model was deliberately checked across opposite philosophies — a function library and a no-code suite from the same vendor, a PC-based environment, and an integrated-system vendor — and against older and platform-native generations, to avoid defining the Type by any one era, form factor, or programming model.

## Sources

Research date: **2026-09-09**

- Cognex — Machine Vision Software overview: https://www.cognex.com/products/machine-vision/vision-software
- Cognex — VisionPro product page: https://www.cognex.com/en/products/machine-vision-software/visionpro-software
- MVTec — HALCON product page: https://www.mvtec.com/products/halcon
- MVTec — HALCON Features & Tools: https://www.mvtec.com/products/halcon/features-tools
- MVTec — MERLIC product page: https://www.mvtec.com/products/merlic
- Keyence — Machine Vision overview: https://www.keyence.com/products/vision/

> Sourcing limitation: deep user manuals (Cognex VisionPro documentation portal, Keyence manuals) were not reachable from the research environment on 2026-09-09; Matrox Design Assistant and Zebra Aurora product pages were unreachable and are not represented in the sample. Precise operational details (exact I/O counts, protocol lists beyond those documented on fetched pages, timing figures, training-image minimums) are intentionally not stated in this document; such details remain in the Research Notes where directly evidenced.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
