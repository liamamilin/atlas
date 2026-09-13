# Research Notes — Machine Vision Platform

Research date: 2026-09-09
Leaf: Machine Vision Platform (DIRECTORY §16 Engineering, Manufacturing & Industrial)
Slug: machine-vision-platform

## Research Goal

Understand what a Machine Vision Platform actually is as an Application Type: the software layer that builds and operates image-based automatic inspection, identification, and guidance applications on production lines — as distinct from camera utilities, offline image-processing libraries, metrology software, and general ML platforms.

## Initial Boundary

Initial hypothesis (before research):

- Core use: acquire images from industrial cameras, process them with configurable vision tools, output per-item decisions (pass/fail, measurements, identifications, positions) to the production process.
- Users: vision engineers / system integrators (build), line operators (run and respond), quality engineers (review results, tune).
- Nearest neighbors: Inspection & Metrology Software, Industrial IoT Platform, Machine Learning Platform, SCADA/HMI, Robot programming environments, Data Labeling Platform.
- Likely confusion: "machine vision" (the discipline) vs "computer vision" (the broader field) vs vision hardware (cameras, frame grabbers, lighting) vs vision sensors (product form).

## Research Questions

1. What is the core object model — job / recipe / program / flowchart / tool chain?
2. How is image acquisition configured (cameras, frame grabbers, trigger, lighting)?
3. How are results delivered to the line (I/O, industrial protocols, sockets)?
4. Is there a development/runtime split, and how is it realized?
5. What tool families are standard (locate, measure, inspect, identify, classify)?
6. How does product changeover work (recipes, PLC-driven switching)?
7. What role does deep learning play — core or capability?
8. Where are the boundaries vs metrology software, ML platforms, IIoT, HMI/SCADA, robot guidance?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer tiers:

| Product | Vendor | Pole | Customer tier |
|---|---|---|---|
| VisionPro | Cognex | PC-based development environment + runtime for integrators | integrators / large manufacturers |
| HALCON | MVTec | algorithm library + interactive IDE (HDevelop), deployed into OEM applications | OEM / machine-builder developers |
| MERLIC | MVTec | no-code all-in-one configuration software (same vendor, opposite philosophy to HALCON) | non-programmer engineers / machine builders |
| Vision Systems (CV-X / XG series class) | Keyence | integrated vision system vendor (controller + cameras + software sold as one system) | end-user factories, vendor-configured |

Deliberate contrast: HALCON vs MERLIC shows the same vendor shipping both a library pole and a no-code pole — strong evidence that the programming model is a variant axis, not the definition. Keyence shows the integrated-system pole where software is inseparable from hardware in the buyer's eyes.

## Sources

Fetched 2026-09-09 (Tier 1/2 — official product and feature pages):

- Cognex — Machine Vision Software overview: https://www.cognex.com/products/machine-vision/vision-software
- Cognex — VisionPro product page: https://www.cognex.com/en/products/machine-vision-software/visionpro-software
- Cognex — VisionPro support hub: https://support.cognex.com/en/products/visionpro (JS shell; no operational content retrieved)
- MVTec — HALCON product page: https://www.mvtec.com/products/halcon
- MVTec — HALCON Features & Tools: https://www.mvtec.com/products/halcon/features-tools
- MVTec — MERLIC product page: https://www.mvtec.com/products/merlic
- Keyence — Machine Vision overview: https://www.keyence.com/products/vision/

Unreachable / not fetched (recorded limitations):

- Cognex VisionPro user documentation (support.cognex.com docs render via JS; deep object-model details not verified from Tier-1)
- Matrox Design Assistant X (404 on both attempted URLs)
- Zebra Aurora (transport error)
- Keyence CV-X product page (404); manuals behind login
- Basler pylon, NI Vision, Hikrobot — not attempted (sample sufficient)

Per the evidence rules: no precise operational claims below rely on the unreachable sources; where a claim rests on a single product it is marked product-specific.

## Product A — Cognex VisionPro (PC-based development environment pole)

### Key observations (evidence layer A — direct from official pages)

- Positioning: "Advanced PC-based vision software for complex and custom manufacturing"; "robust prototyping and unmatched programming control"; combines rule-based tools with AI capabilities.
- Development environment named **QuickBuild**: "combines advanced programming with the speed and simplicity of graphical, drag-and-drop application development. You can easily configure acquisition settings, connect tools, and set pass/fail decisions using modular tool blocks that can be easily created, reused, and adapted for flexible deployment."
- Scripting for advanced applications; "quickly load and execute jobs to reduce cycle time" — job as the executable unit.
- Rule-based tool families listed: object location and pattern matching; edge and blob detection; measurement tools; bead inspection (adhesive/sealant/weld beads); identification tools (1D/2D barcodes, alphanumeric codes).
- AI tools: AI-powered segmentation (foreground/background, foreign objects, defect areas); AI-powered classification ("go beyond OK/NG"); example-based training "using as few as 5 to 10 images" (vendor claim — recorded, not generalized).
- Acquisition breadth: "supports all types of image capture: analog, digital, color, monochrome, area scan, line scan, high-resolution, multi-channel, and multiplexed"; "hundreds of industrial cameras and video formats"; Cognex cameras (GigE, PoE) and frame grabbers as companions.
- Line integration hardware: CC24 I/O card — 24 I/Os (8 isolated inputs, 16 isolated outputs), encoder support for motion control, factory protocols EtherNet/IP, PROFINET, SLMP, TCP/IP; real-time subsystem for I/O handling.
- Programming integration: ".NET, C#, and C++ class libraries and user controls".
- Vendor's own framing of the category (from the software overview page): machine vision software "interprets and processes visual information from cameras, primarily for industrial applications… drives decision-making and data collection"; PC-based vs fully-embedded distinction; rule-based vs AI-based distinction; machine vision vs computer vision distinction (industrial, embedded in production vs general-purpose).
- Vendor's own AI training loop: data collection → labeling/annotation → algorithm training → validation → deployment.

## Product B — MVTec HALCON (library / toolbox pole)

### Key observations (evidence layer A)

- Positioning: "comprehensive machine vision software designed for developing, deploying, and operating reliable vision applications across industries… faster development, stable operation, and long-term use in productive environments."
- Scope: "the most extensive toolset in the vision market, from image acquisition to deep learning in one package."
- Performance framing: multicore, GPU acceleration, automatic operator parallelization "for high throughput"; deep-learning acceleration via Intel OpenVINO and NVIDIA TensorRT.
- Accuracy framing: "subpixel-accurate measurements… supported by calibration tools that correct lens distortions and enable world-coordinate measurements."
- Application areas (vendor taxonomy): Quality Inspection, Object Recognition, Measuring, Identification, 3D Matching.
- Technology list (knowledge base): 3D Vision, Bar Code & 2D Code Reading, Blob Analysis, Classification, Computational Imaging, Deep Learning, Filtering, Inspection, Matching, Measuring, Morphology, OCR, Subpixel.
- Development tools: "dedicated tools for creating, testing, debugging, and integrating machine vision logic… interactive development, smooth integration into applications, and maintainable execution in productive systems." HDevelop named in tutorials ("Develop in HDevelop, run on D3: set ROI, learn shapes, measure diameters, save scripts").
- Deployment: "standard PCs as well as embedded and Arm-based platforms"; HALCON Embedded on smart cameras.
- Deep learning sold as a separate companion product (Deep Learning Tool) — packaging evidence that model training is a capability beside the core, not the core.
- Success stories span: automotive weld-seam anomaly detection, battery inspection, pharmaceutical ampoules, food packaging, bin picking with 3D vision, robot guidance (hand-eye calibration), rice-grain inspection on embedded hardware, train-roof defect inspection.

## Product C — MVTec MERLIC (no-code all-in-one pole)

### Key observations (evidence layer A)

- Positioning: "complete machine vision applications can be created quickly and intuitively… a clear, image-centered operating concept… supports the entire workflow of a vision application… from initial setup to productive operation."
- No-code: "configuration of image processing applications without code by combining and configuring standardized tools. The image-centered interface allows parameters and processing steps to be set directly on the image."
- All-in-one: "covering image acquisition, image processing and analysis, integrated communication interfaces, and result visualization in a single environment… applications can be developed, deployed, and operated without the need to switch between different systems."
- Task coverage: "classification, measurement and counting, inspection and testing, OCR, barcode and 2D code reading (matrix codes), position determination, and 3D vision based on height maps."
- Image Source Manager (ISM): dedicated tutorial on "configuring image sources" — acquisition as a first-class configured object.
- **Recipes / changeover**: "MERLIC recipes let the PLC reconfigure or switch vision apps on demand" (process-integration tutorial) — direct Tier-1 evidence of PLC-driven recipe switching.
- Operator frontend: MERLIC Designer — "create your own frontend for machine vision applications… interactive, customizable"; live parameter tuning on the line.
- easyTouch: "hover to detect, align, measure, or read text" — interaction simplification.
- Calibration: "calibrate your camera in MERLIC using a simple calibration plate"; alignment tools "automatically align moving parts, enabling robust positioning and precise measurements."
- Deep learning tools inside the no-code flow: "Classify Image", "Detect Anomalies" (trained with only good samples), "Read Text and Numbers with Deep Learning" (Deep OCR); models prepared in the separate Deep Learning Tool and integrated per license.
- Edge deployment: MERLIC on Siemens Industrial Edge — run MVApps on edge devices.

## Product D — Keyence Vision Systems (integrated system pole)

### Key observations (evidence layer A, product-line page)

- Lineup framing: "KEYENCE vision system offerings range from modular high-speed controllers to all-in-one smart cameras. Inspection tools ranging from rule-based tools to AI functions provide solutions for various applications." Separate "Vision Sensors" line ("featuring built-in Artificial Intelligence for stable results") — the vendor itself treats vision sensors as a product-form sibling.
- Category definition (vendor FAQ): "Machine vision technology provides image-based automation to control various production processes, including automatic inspection, analysis, process control, and robot guidance… The machine vision software captures and interprets this information, which performs subsequent operations based on the interpreted information while storing data for later inspection."
- Application catalog (vendor's own taxonomy): presence/absence, measurement, flaw detection, positioning/alignment, character and barcode reading, line scan, 3D inspection and measurement, 3D vision-guided robotic and bin picking, weld inspection, position correction, color and product type, quantity inspection, appearance inspection, dimension measurement, identification & connector inspection.
- Robot integration framing: software "can identify and classify various objects within the captured image, make various decisions, and trigger adequate, pre-set actions in robotic systems."
- Manuals and detailed setup documentation are behind login — operational details not verified; no precise claims drawn from this vendor.

## Cross-product Comparison

| Aspect | VisionPro (Cognex) | HALCON (MVTec) | MERLIC (MVTec) | Keyence Vision Systems |
|---|---|---|---|---|
| Form | PC-based dev environment + runtime | Library + interactive IDE (HDevelop) + runtime | All-in-one no-code config + runtime | Integrated controller/smart camera + software |
| Acquisition | configured in QuickBuild; "all types of image capture"; frame grabbers + cameras | "from image acquisition to deep learning in one package"; broad hardware compatibility | Image Source Manager; "various hardware types" | built into the system (controller + cameras) |
| Processing unit | tool blocks connected in jobs; scripting | operators/functions called from user code or HDevelop scripts | standardized tools configured on the image | inspection tools (rule-based → AI) |
| Decision | "set pass/fail decisions" in tool blocks | results computed; decision logic in application | tools produce results; app logic configured | OK/NG verdicts per inspection |
| Line output | I/O card (24 I/O), EtherNet/IP, PROFINET, SLMP, TCP/IP, encoder | integration into applications; sockets (generic sockets tutorial) | "integrated communication interfaces"; PLC switches recipes | PLC/line integration (mechanism not verified) |
| Operator surface | runtime UI (not detailed on fetched pages) | — (application-dependent) | MERLIC Designer frontends | built-in display/monitor |
| Calibration | not stated on fetched pages | calibration tools; lens distortion; world coordinates | calibration plate; alignment tools | position correction (framing only) |
| Deployment | PC + Cognex hardware | PCs, embedded, Arm | PCs, Siemens Industrial Edge | controller / smart camera |
| Deep learning | AI segmentation/classification; example-based training | deep learning incl. anomaly detection; separate Deep Learning Tool | DL tools in no-code flow; separate Deep Learning Tool | AI functions; vision sensors with built-in AI |
| 3D | not stated on fetched pages | 3D matching, sheet-of-light, point clouds | 3D vision based on height maps | 3D inspection, vision-guided bin picking |

### Stable commonalities (evidence layer B — cross-product)

1. **Camera-driven image acquisition as a configured input.** All four products treat acquiring images from industrial cameras (and/or frame grabbers) as a first-class, configured part of the application — not a driver afterthought. (VisionPro: "configure acquisition settings"; HALCON: "from image acquisition to…"; MERLIC: Image Source Manager; Keyence: integrated acquisition.)
2. **A buildable, reusable vision application as the unit of record.** All four organize the work as an editable program — job/tool blocks (VisionPro), script/program (HALCON), configured tool chain (MERLIC), inspection setup (Keyence) — that is saved, versioned, and re-executed per item.
3. **Vision tools as the building blocks.** The same tool families recur: locating/matching, measurement, presence/defect inspection, identification (barcode/2D code/OCR), classification.
4. **Per-item results and pass/fail decisions.** The output of a run is a decision about the item in the image (OK/NG, measurements, code content, position), not aggregate analytics.
5. **Line integration.** All four position the vision application inside the production process: results/signals out to PLCs and equipment, execution synchronized with the line (triggers, encoders, protocols). VisionPro documents I/O + protocols; MERLIC documents PLC-driven recipe switching; Keyence frames the whole category as "image-based automation to control production processes"; HALCON realizes it through the applications built on it (integration into applications, sockets).
6. **Development/runtime separation.** VisionPro (QuickBuild vs runtime jobs), HALCON (HDevelop vs deployed application), MERLIC (Creator vs Runner — all-in-one but still develop-then-operate), Keyence (setup vs run). The packaging differs; the split recurs.
7. **Deep learning as an embedded capability.** All four now embed DL tools (classification, defect detection, anomaly detection, segmentation, OCR) beside rule-based tools — and two vendors (MVTec, Cognex) sell the training environment as a separate companion product. Training happens on images inside the vision workflow, not in a general ML platform.

### Where products differ (variant axes)

- Programming model: library API (HALCON) vs graphical drag-and-drop + scripting (VisionPro) vs no-code configuration (MERLIC) vs vendor-configured integrated system (Keyence).
- Form factor: PC + any camera vs embedded/Arm vs integrated controller/smart camera.
- Customer: integrator/OEM developer vs end-user factory.
- Depth of calibration/metrology-grade accuracy: varies (HALCON emphasizes subpixel + world coordinates; others less on fetched pages).
- 3D vision: present in all four at different depths (height maps, point clouds, laser profilers).

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Machine Vision Platform:

1. **Configured camera-driven image acquisition.** The platform acquires images from industrial cameras/frame grabbers under application control — triggered and timed to the production process — as its input. Remove → a generic image-processing library or a camera utility/viewer.
2. **The buildable vision application as the unit of record.** A persistent, editable program of vision tools/operators — locate, measure, inspect, identify, classify — that computes per-item results and pass/fail decisions from images, saved and re-executed for every item. Remove → a camera SDK, or offline image analysis.
3. **Line-integrated execution.** The vision run is synchronized with the production process (triggers/encoders/signals) and its results — verdicts, measurements, identifications, positions — are delivered to line equipment (PLCs, rejectors, robots) so the process can act. Remove → an offline vision toolkit with no production consequence.

Jointly-held load-bearing checks:

- 1 alone = camera SDK / viewer utility
- 2 alone = image-processing library / computer-vision toolkit
- 3 alone = PLC / line control
- 1+2 without 3 = offline/lab vision analysis
- 2+3 without 1 = line control without images
- 1+3 without 2 = acquisition plumbing with no vision logic

### L1 — Common Mature Structure

Present across the sample; expected in mature products; not definitional:

- development/runtime separation (build environment + production runtime)
- standard tool families: locating/matching, measurement, presence/defect inspection, identification (barcode/2D code/OCR), classification
- calibration (lens distortion, world coordinates; hand-eye for robot guidance)
- recipe / product-variant management and changeover (PLC-driven switching documented in MERLIC)
- operator frontend (live image, results, statistics) — MERLIC Designer documented; others implied
- trigger/synchronization machinery (hardware trigger, encoder support — VisionPro CC24)
- result logging / data storage for traceability (Keyence framing: "storing data for later inspection")
- deep learning tools beside rule-based tools (classification, defect detection, anomaly detection, segmentation, OCR)
- 3D vision (height maps, point clouds, sheet-of-light/laser profilers)
- performance machinery (multicore, GPU, parallelization)

### L2 — Variant / Optional Structure

- form factor: PC-based vs embedded/smart camera vs integrated controller system vs edge devices
- programming model: library API vs graphical flowchart vs no-code configuration vs vendor-configured
- vision-guided robotics (pose output, hand-eye calibration, bin picking)
- line-scan / web inspection for continuous material
- OEM licensing / runtime licensing models
- AI training environments as separate companion products (MVTec Deep Learning Tool; Cognex VisionPro Deep Learning / OneVision)
- industry packaging (pharma, food, battery, electronics)

### L3 — Vendor-specific (research notes only)

- Cognex: QuickBuild, tool blocks, CC24 I/O card specifics, In-Sight Vision Suite (smart-camera line), EasyBuilder, DataMan Setup Tool, OneVision (multi-site AI development), "5 to 10 images" training claim
- MVTec: HDevelop, easyTouch, Image Source Manager, MERLIC Designer/Runner, MERLIC on Siemens Industrial Edge, calibration plates as a physical product line, MVTec AD anomaly-detection datasets
- Keyence: CV-X/XG/IV series naming, vision-sensor vs vision-system split, seller-configured sales model, login-walled manuals
- Cognex/Keyence marketing taxonomies of applications (presence/absence, flaw detection, weld inspection, etc.)

## Vendor-specific Findings

- Cognex publishes its own category framing (PC-based vs embedded; rule-based vs AI-based; machine vision vs computer vision) — useful as vendor corroboration of the Type's boundaries, not as definition.
- MVTec ships two opposite philosophies (HALCON library vs MERLIC no-code) under one brand — the strongest single piece of evidence that the programming model is a variant axis.
- Keyence sells vision as hardware systems with software inside; the software layer still exhibits the same three L0 structures (acquisition, inspection setup, line integration) per its own category description.
- Deep-learning training environments are packaged as separate products at both MVTec and Cognex — packaging evidence that model training is a capability, not the platform's defining core.

## Boundary Findings

- **vs Inspection & Metrology Software** (adjacent, pre-hung seam corroborated from the metrology side's own research entry): metrology software produces metrology-grade dimensional verdicts against nominal geometry/tolerances (CAD/drawing reference, per-characteristic evaluation); machine vision platforms produce line-rate decisions for 100% in-line inspection/identification/guidance. Vision-based measurement exists in both; the seam is purpose and operating context (accuracy/traceability vs speed/robustness in-line), not the presence of measurement.
- **vs Machine Learning Platform / MLOps Platform**: ML platforms build, train, register, and serve general models; the machine vision platform's unit of record is the vision application (job/recipe), with DL models as embedded tools trained on images inside the vision workflow. A vision platform does not manage feature stores, pipelines, or model registries as its core.
- **vs Data Labeling Platform**: labeling/annotation appears as a step inside DL tool workflows (Cognex training loop), not as the platform's core.
- **vs Industrial IoT Platform / Network Monitoring**: IIoT observes and aggregates process data; machine vision decides per item and actuates (reject/sort/guide signals). Overlap: both produce data for analytics; only machine vision produces per-item image-based verdicts.
- **vs SCADA / HMI**: HMI is the operator-facing live interface to a controlled process; machine vision is an automated image-based decision system. A vision platform may provide an operator frontend (MERLIC Designer), but the core is the vision application, not process visualization/control.
- **vs Robotics Engineering Platform / Robot Fleet Management**: vision-guided robotics is a variant; the robot consumes vision results (positions/poses). The vision platform does not program or manage robots.
- **vs Computer Vision (research/general software)**: machine vision is industrial, embedded in production, real-time, deterministic, and integrated with line equipment; computer vision is the broader discipline/general-purpose software. Cognex itself publishes this distinction.
- **vs Vision Sensor (product form)**: a vision sensor is a miniaturized integrated product form (Keyence's own split); the software inside still realizes the same three L0 structures. Form factor is a variant, not a Type boundary.
- **去掉什么就变成另一个 Type**: remove line integration → offline image-analysis/computer-vision toolkit; remove the buildable application → camera SDK; remove camera acquisition → PLC/line control; remove per-item decision purpose → IIoT monitoring; remove line-rate purpose and add metrology-grade traceability → Inspection & Metrology Software.

## Historical / Market-Sample Check (per §24)

Would older, regional, platform-native products still fit the L0 definition?

- **1980s–90s generation**: camera + frame grabber + tool library + pass/fail logic + discrete I/O to PLCs — satisfies all three legs with no deep learning, no 3D, no GigE Vision, no cloud, no graphical IDE. ✓
- **Platform-native / camera-vendor software** (e.g., camera SDKs with vision tools, LabVIEW-based vision): acquisition + buildable application + line integration via user-built systems. ✓ (not fetched — conceptual check only)
- **Regional integrated-system vendors** (Keyence, Omron — Japan; Hikrobot — China): integrated systems with software inside; same three structures per vendor's own category descriptions. ✓
- **Smart-camera generation** (In-Sight class): all three structures inside the camera. ✓

Conclusion: L0 holds across eras and form factors. Deep learning, 3D vision, GigE Vision, specific protocols, graphical IDEs, and cloud are era machinery — excluded from L0.

## Uncertainties

- Exact runtime/development product splits and object-model names for Keyence (manuals behind login) — not claimed anywhere.
- Cognex VisionPro's precise object model (job manager, tool block internals) not verified from Tier-1 documentation (support docs JS shell); final document avoids naming internal object types.
- Matrox Design Assistant X and Zebra Aurora unreachable — the flowchart-pole and unified-suite-pole are represented only indirectly (VisionPro's drag-and-drop; MERLIC's no-code).
- Whether every integrated-system vendor exposes recipe management the way MERLIC documents it — PLC-driven recipe switching is Tier-1 documented only for MERLIC; treated as common-but-not-universal.
- Operator-frontend depth varies; only MERLIC documents a dedicated frontend designer in the fetched sample.

## Final Synthesis

A Machine Vision Platform is the software layer that builds and operates image-based automatic inspection, identification, and guidance applications on production lines. Its defining core is three jointly-held structures: configured camera-driven image acquisition; a buildable, reusable vision application (tools → per-item results and pass/fail decisions) as the unit of record; and line-integrated execution (synchronized with the process, results delivered to line equipment so the process can act). Everything else — development/runtime split, tool families, calibration, recipes, operator frontends, deep learning, 3D, form factors, programming models — is common mature structure or variant machinery, documented as such.
