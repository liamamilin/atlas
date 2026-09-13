# Research Notes — CNC Programming Application

## Research Goal

Process the directory leaf **CNC Programming Application** (§16 Engineering, Manufacturing & Industrial) and conduct the **joint review** explicitly requested by the CAM pass (research/cam.md §Boundary Findings, STATUS.md Boundary Issues): determine whether this leaf is (a) an **alias** of CAM, (b) a distinct **manual-programming-activity slice**, or (c) an independent Type. Produce a vendor-neutral Application Document for the leaf whatever the outcome.

## Initial Boundary (hypothesis before research)

- "CNC programming" is the *activity* of creating programs that drive CNC machines; "CAM software" is the dominant *product category* serving that activity.
- Suspected (inherited from the CAM pass): the market uses "CAM software" and "CNC programming software" interchangeably; Mastercam's homepage is literally titled "Your Solution for CNC Programming".
- Candidate distinct slice: software serving *manual/direct* CNC programming — G-code editors, DNC transfer, conversational programming, NC verification (CIMCO / Predator / Vericut class). Question: do these form a coherent market category called "CNC programming applications", or do they self-identify as editors / transfer / verification tools?
- Nearest neighbors: CAM (sibling leaf), Mechanical CAD (upstream), Additive Manufacturing Software (same skeleton, different process), CNC verification systems, DNC/program-management tools, CNC controls (machine-side programming), PLC Programming Environment (different machine domain), MES (downstream).

## Research Questions

1. What do vendors selling "CNC programming software" actually sell — geometry-driven CAM products or something else?
2. Is there a distinct, self-named product category of manual/G-code CNC programming environments? What does it contain (editor, backplot, DNC, verification, revision control)?
3. Where does conversational programming live — standalone desktop category, CAM mode, or machine-control mode?
4. Where does NC simulation/verification sit — inside programming, or a distinct adjacent family?
5. What is the life of the NC program *after* it leaves the programming application (transfer, editing, versioning, execution)?
6. What would the L0 be if this leaf were distinct, and does that L0 collapse into CAM's?
7. Historical check: would older / differently-positioned products (APT-era, manual tape programming, control-side programming) still fit the definition?

## Representative Products

| Product | Pole | Evidence tier reached |
|---|---|---|
| Mastercam (CNC Software) | standalone CAM market leader; the vendor that literally markets itself as "CNC programming" software | Tier 2 (homepage re-fetched this pass; products/post pages from CAM pass) |
| OneCNC | mid-market CAD/CAM; self-describes as "a CAM system for NC part programming" | Tier 2 (homepage) |
| SprutCAM X (SprutCAM Tech) | CAD/CAM marketed around a "CNC programming workflow"; robot OLP extension | Tier 2 (homepage) |
| Predator Software (CNC Editor / DNC / Virtual CNC / Post Processor / PDM) | the code-direct companion family: G-code editing, transfer, verification, post-processing, revision control | Tier 2 (homepage + product family descriptions) |
| Vericut (CGTech) | standalone NC simulation & verification family (since 1988) | Tier 2 (homepage + product nav) |
| Centroid CNC | control-side conversational programming (CNC control/retrofit vendor) | Tier 2 (homepage) |
| SOLIDWORKS CAM / Vectric / SheetCam / APT | joint-category evidence from the CAM pass (CAD-embedded, hobbyist, cutting, historical) | Tier 2 / Tier 3 via research/cam.md |

Selection rationale: three independent CAM vendors to test the naming equation across the market (layer B); the strongest available code-direct family (Predator) to test the "manual-programming slice" outcome; the leading verification family (Vericut) to test that boundary; a control vendor (Centroid) to locate conversational programming. CIMCO (the other major CNC-editor vendor) was targeted but unreachable (403 ×2) — see Sources.

## Sources

Fetched successfully (research date 2026-09-07, this pass):

- Mastercam homepage — https://www.mastercam.com/ (Tier 2)
- OneCNC homepage — https://www.onecnc.com/ (Tier 2)
- SprutCAM X homepage — https://sprutcam.com/ (Tier 2)
- Predator Software homepage (14-application digital-factory family) — https://www.predatorsoftware.com/ (Tier 2)
- Vericut homepage — https://www.vericut.com/ (Tier 2)
- Centroid CNC homepage — https://www.centroidcnc.com/ (Tier 2)

Cross-referenced from the CAM pass (fetched 2026-09-07, recorded in research/cam.md):

- Mastercam Products / Post Processors pages; SOLIDWORKS CAM product page; Vectric homepage; SheetCam homepage; DBpedia APT extract.

Failed / abandoned (per network-restriction rule, 1–2 failures then abandon):

- CIMCO — https://www.cimco.com/ 403; https://www.cimco.com/products/ 403 (2 failures, abandoned)
- Predator CNC Editor detail page — https://www.predatorsoftware.com/predator_cnc_editor_software.htm 404 (1 failure; editor facts already covered on the fetched homepage, not retried)
- FANUC / Haas control-side programming pages — not attempted (control vendors' sites historically JS-gated in this environment; control-side mode evidenced via Centroid instead)

**Source-access limitation**: No Tier-1 operational documentation (Help Center / User Guide) was reachable for any sampled product in this pass — same limitation as the CAM pass. All evidence is Tier-2 product/marketing-page level. Consequently: no precise operational details (numeric limits, parameter defaults, exact state names, format lists) are asserted anywhere; claims are calibrated to product-page granularity. The CNC-editor/DNC family is evidenced through Predator only; CIMCO's exact positioning is NOT characterized from memory and no claims are made about it beyond "targeted but unreachable".

## Product A — Mastercam (standalone CAM market leader)

### Key observations (evidence layer A = directly observed this pass)

- Homepage `<title>`: **"Mastercam Software: Your Solution for CNC Programming"** — the market leader's own naming equation.
- Badge: "#1 Most widely used CAM software" — same page, same product.
- IMTS 2026 blurb: "See what's next in **CNC programming**. Visit us at IMTS 2026 in Chicago to experience Mastercam 2027…"
- EverPath Technology: "a next generation toolpath platform designed to make **CNC programming** faster, simpler, and more flexible."
- Press release framing: "greater efficiency, accuracy, and confidence **from programming through machining**."
- (From CAM pass, same vendor:) products page "Program your CNC machines with the world's leading CAD/CAM software"; FAQ: "CAM tools then convert those models into toolpaths and G-code that CNC machines follow"; post processors "converting generic CAM system output to Mastercam-specific NC code", built with FANUC/Siemens/DMG MORI; post-driven machine simulation of "the actual machine motion defined by the NC code output".

**Reading**: one product, two names. "CNC programming" is the activity; "CAM software" is the category; Mastercam uses both for the same product.

## Product B — OneCNC (mid-market CAD/CAM)

### Key observations (layer A)

- "OneCNC CAD CAM is a market leader in computer aided manufacturing **CAM system for NC part programming**."
- "What is CAD/CAM?" explainer: "CAD/CAM applications are used to both design a product and **program manufacturing processes, specifically, CNC machining**. CAM software uses the models and assemblies created in CAD software to **generate tool paths that drive the machines** that turn the designs into physical parts."
- Product family: Mill (+ Multi Axis), Lathe (+ Mill Turn: "C Axis, CY Axis and CYB Axis"), Profiler (with part nesting), Wire EDM (+ Multi Axis: "fast, efficient wire programming"), Solid Design (the CAD portion).
- Programming workflow framing: Lathe "gives you a set of tools ready for **programming** from creating a wire frame or solid model with the ability to import CAD models right through to the completed turned part."
- Machine targeting: "OneCNC supports all standard machine controllers and machines without any additional costs for machine posts. The post is controlled by a powerful GUI interface, allowing personalized configuration."

**Reading**: a second independent vendor equates its CAM product with "NC part programming". Same skeleton: geometry in (drawn or imported) → toolpaths computed → posts per machine/controller.

## Product C — SprutCAM X (CAD/CAM + robot OLP)

### Key observations (layer A)

- Hero: "Enjoy the power/speed/safety of a natural easy to learn and use **CNC programming workflow**" — describing its CAD/CAM product.
- Company blurb: "we create powerful software for **programming CNC machines and industrial robots**."
- Mission: "create a natural CAD/CAM environment for **CNC machines and industrial robot programming**."
- Products: SprutCAM X (CAD/CAM "for next generation makers"), SprutCAM X Robot (CAD/CAM/OLP for robots), MachineMaker (digital-twin/machine component tool), CNC Post Processors download area, AI assistant.
- Version 17 highlights: multi-project workflow, project snapshots, machine setups, machining technologies, CAD module, AI assistant.

**Reading**: third independent vendor; "CNC programming" names the workflow its CAD/CAM product delivers. Also extends the same skeleton to industrial robots (OLP) — evidence that the programming skeleton generalizes across machine kinds (kept as vendor extension, not canonical).

## Product D — Predator Software (code-direct companion family)

### Key observations (layer A)

- Positions itself as a "Digital Factory" suite of **14 applications**; the CNC-program-adjacent ones are individually named and described:
  - **Predator CNC Editor** — "G code editing software"; bullets: "Compare & Edit G Code, Basic DNC, 3D Backplotting & Animation"; "improves the quality, capability and performance of CNC programs."
  - **Predator DNC** — "industrial network for CNCs, robots, CMMs, PLCs, part markers, tool presetters & test stands"; "Ethernet, RS232 & Parallel".
  - **Predator Virtual CNC** — "CNC machine simulation and 3D verification software"; "Machine Simulation & Verification; 2-5 Axis Mills, Lathes, EDMs & 3D Printers; **Actual CNC Code**."
  - **Predator Post Processor** — "CNC Post Processing; 2-5 Axis Mills, Lathes & 3D Printers; **Supports APTCL, INC and NCI input**" (i.e., consumes cutter-location / CAM intermediate data and produces machine code).
  - **Predator PDM** — "Production Data Management… vault(s), revision control & statuses."
- None of these is named or described as a "CNC programming application". The family's own vocabulary: *editing*, *transfer/networking*, *simulation & verification*, *post processing*, *revision control*.

**Reading**: the code-direct tool family exists, is real and substantial — and it self-identifies as program *handling* (edit/transfer/verify/version/translate), not as a "CNC programming software" category. This is the decisive evidence against the "manual-programming slice" outcome.

## Product E — Vericut (CGTech) (standalone NC verification family)

### Key observations (layer A)

- "Vericut's powerful **CNC verification, simulation and analysis software** creates an identical digital twin of your machine…"
- "Our CNC simulation software **works alongside your existing CAD/CAM system, NC program, and manufacturing process**." — Vericut consumes the finished NC program; it sits beside the programming application, not inside it.
- Pain framing: "Idle machines, damaged tools, costly collisions, scrapped parts, lengthy **prove-outs**, wasted material… By simulating your entire CNC production process to ensure every cut you make is the right one."
- Product family: Verification, CNC Simulation, Multi Axis, AUTO-DIFF (compare machined result vs design), Machine Probing, Grinder Dressing, Force Optimization, Machine Connectivity, Interfaces (to CAM systems), Additive Manufacturing Simulation, Composites (incl. "Vericut Composite **Programming**" — programming for a different machine domain), Icam Post / Custom Post Processor, Reviewer, Robot Simulation, AI.
- Testimonial (Starrag): "The tool design, fixture design, and **CAM programming** were completely checked and optimized in Vericut." — distinguishes CAM programming (upstream) from Vericut checking (downstream).
- Testimonial (RO-RA): "we simulate **every NC program** with Vericut before it runs on the real machine."

**Reading**: verification is a distinct, decades-old adjacent product family organized around the NC program as input. Not "CNC programming software"; a companion that safeguards the program.

## Product F — Centroid CNC (control-side conversational programming)

### Key observations (layer A)

- Centroid sells CNC **controls** (retrofit + DIY kits: Acorn/Hickory/Oak/Allin1DC), machines, rotary tables.
- Operator-interface framing: "User friendly operators interface with advanced features like: **Conversational programming**, Digitizing, Auto part set, Auto tool set, 3D contouring, 4th and 5th axis machining…"
- "CENTROID CNC controls are designed by machinists for machinists."

**Reading**: conversational programming — the classic non-CAM authoring mode — lives **inside the machine control** as an operator feature, not in a separate desktop application category. The control is the executing system; its conversational mode is machine-side programming for simpler work. This places conversational programming on the *control* side of the preparation/execution seam.

## Cross-referenced joint-category evidence (from research/cam.md, layer A there)

- SOLIDWORKS CAM — CAD-embedded CAM, rules/knowledge/tolerance-based automation, associativity with design.
- Vectric — hobbyist/maker router CAM ("Draw it, plan your toolpaths, and cut it").
- SheetCam — prosumer cutting CAM (nesting, kerf, cut ordering, configurable posts).
- APT (1950s) — the language-based ancestor: geometry + tool motion described in a language, computer computed cutter-location data, post-processor produced control tapes. The minimal historical form of the Type.

## Cross-product Comparison

| Structure | Mastercam | OneCNC | SprutCAM X | Predator family | Vericut | Centroid |
|---|---|---|---|---|---|---|
| Self-description as "CNC programming" software | ✓ ("Your Solution for CNC Programming") | ✓ ("CAM system for NC part programming") | ✓ ("CNC programming workflow") | ✗ (editor / DNC / verification / post naming) | ✗ ("CNC verification, simulation and analysis") | ✗ (control vendor; conversational is a control feature) |
| Part geometry as programming input | ✓ | ✓ (wire frame/solid/import) | ✓ (CAD/CAM) | ✗ (works on G-code / CL data) | ✗ (consumes NC program; design used as comparison reference) | ✗ (control-side) |
| Software-computed toolpaths from geometry | ✓ | ✓ ("generate tool paths") | ✓ | ✗ (Post Processor translates existing CL/NCI data) | ✗ (simulates existing code) | ✗ |
| Machine-specific NC output / posts | ✓ (post library, control-maker collaboration) | ✓ ("supports all standard machine controllers… machine posts") | ✓ (post processor downloads) | ✓ (Post Processor product; DNC delivery) | — (validates, doesn't produce) | executes G-code (control) |
| Simulation / verification | ✓ (post-driven machine simulation) | not observed on fetched page | not observed on fetched page | ✓ (Virtual CNC; Editor backplot) | ✓ (core) | not claimed |
| Program transfer / DNC | not observed on fetched page (CAM pass noted transfer as common) | not observed | not observed | ✓ (DNC core; Editor "Basic DNC") | ✓ (Machine Connectivity line) | ✗ |
| Revision control of programs | ✗ | ✗ | ✗ | ✓ (PDM) | ✗ | ✗ |
| Conversational programming | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (control feature) |
| Robot extension of the same skeleton | ✗ | ✗ | ✓ (SprutCAM X Robot OLP) | ✓ (DNC networks robots) | ✓ (Robot Simulation) | ✗ |

**Layer reading**: the three CAM vendors form a layer-B cross-product commonality (the naming equation); Predator/Vericut/Centroid are layer-A single-product boundary anchors.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

Resolved by the joint review: this leaf denotes the **same Application Type as CAM**. The L0 is therefore CAM's L0, restated from the programming vantage:

1. **Part geometry as input** — the thing to be made exists as geometry (imported CAD model or drawn in the application); the geometry is what the program must produce.
2. **Software-computed machine/tool motion** — the application computes the motion of the machine's working implement from that geometry under a machining strategy the programmer selects and parameterizes.
3. **Machine-executable NC program as output, bound to a specific machine/control** — the computed motion is translated into control data a specific machine and control can execute.

§24 historical check: APT (1959, language-driven) ✓; Vectric (hobbyist router) ✓; SheetCam (cutting) ✓; SOLIDWORKS CAM (CAD-embedded) ✓; Mastercam/OneCNC/SprutCAM ✓. The definition does not depend on era, vendor, or machining family.

Deliberately NOT in L0: stock models, tool libraries, simulation, machine kinematics, post-processing as a separate stage, CAD authoring, feature recognition, nesting, program transfer/DNC, revision control, conversational mode, AI.

### L1 — Common Mature Structure

- CAD import (and often CAD authoring in the same product)
- Stock/workpiece and fixture definition
- Machine and control definition (axes, kinematics, travel limits)
- Tool libraries / tool assemblies with cutting parameters
- Setups and operations organized as a program tree; strategies per operation
- Toolpath simulation / verification (backplot → material removal → full machine kinematics in the most advanced form)
- Post-processing as a distinct translation stage with per-machine/control post libraries
- Cycle time estimation
- Program output and transfer to the machine

### L2 — Variant / Optional Structure

- Machining-family specialization (mill 2.5D→5-axis, turning, mill-turn/Swiss, wire EDM, router, laser/plasma/waterjet cutting, engraving)
- Delivery form (standalone desktop / CAD-embedded add-on / integrated suite / cloud)
- Automation depth (feature recognition, rules/knowledge-based, tolerance-based programming)
- Cutting-segment machinery (nesting, kerf compensation, cut ordering, piercing, height control)
- Customer tier (industrial / prosumer / hobbyist-maker; pricing and community posture)
- Authoring surface beyond the desktop: conversational programming at the machine control; direct code adjustment in companion editors
- Companion toolchain depth around the program artifact (editors, DNC networks, standalone verification, revision control)
- Extensions of the same skeleton to other machine kinds (robot OLP; composite programming; additive modules in some suites)
- AI assistance (era-common, product-dependent)

### L3 — Vendor-specific Structure (research notes only)

- Mastercam: Dynamic Motion, EverPath (beta), Copilot AI, post library built with FANUC/Siemens/DMG MORI, post-driven simulation ("What you simulate is what you cut"), Learning Edition, product-per-family line (Mill/Lathe/Mill-Turn/Swiss/Router/Wire), 450K+ users / #1 claims.
- OneCNC: Active Cut Technology, HS Machining (70% savings claim), no-extra-cost posts with GUI post configuration, perpetual no-maintenance pricing posture, product ladder Mill/Lathe/Profiler/Wire EDM/Solid Design.
- SprutCAM X: X Robot OLP line, MachineMaker digital-twin component, Sprut-ID, SMC maintenance model, 30-day trial + online courses, AI assistant, "next generation makers" positioning.
- Predator: 14-application digital-factory suite naming (Virtual CNC, Touch HMI, Adaptive CNC, Travelers, FLM…), Editor "Compare & Edit G Code / Basic DNC / 3D Backplotting", Post Processor input formats APTCL/INC/NCI, since 1994, 115,000+ users claim.
- Vericut: AUTO-DIFF, Force Optimization, Icam Post (V27), Composite Programming (VCP), Drilling & Fastening (VDAF), Reviewer, Vericut Intelligence (AI), since 1988 / 35+ years claims, customer testimonials (Mercedes F1, Starrag, Pilatus, Sandvik Coromant).
- Centroid: control product line (Acorn/AcornSix/Hickory/Oak/Allin1DC), DIY kits from $369, retrofit targets (Haas/Fadal/Mazak/…), digitizing probes, since 1979.

## Rejected Findings

- **"CNC Programming Application is a distinct manual-G-code programming category"** — REJECTED as a Type. The products serving manual programming self-identify as *editors* (Predator CNC Editor: "G code editing software"), *transfer* (DNC), *verification* (Vericut, Predator Virtual CNC), *post-processing* (Predator Post Processor), and *revision control* (PDM) — none names itself a "CNC programming application". Meanwhile the market term "CNC programming software" refers to CAM products (three independent vendors evidenced). Manual code editing is a capability/mode (inside CAM products, inside companion editors, at the control), not a category boundary.
- **"Conversational programming is a standalone desktop category"** — REJECTED on sampled evidence. Conversational programming was observed as a *control feature* (Centroid). It may also exist inside some CAM products, but no sampled product presents it as a separate desktop application category.
- **"Verification is part of CNC programming"** — REJECTED as definitional. Verification is a distinct adjacent family (Vericut since 1988; Predator Virtual CNC) that consumes the finished NC program. Inside programming products, simulation is a standard capability (L1), not the Type boundary.
- **"DNC/transfer is definitional"** — REJECTED. Transfer is common (L1) and also exists as standalone adjacent infrastructure (Predator DNC, Multi-DNC). A program can reach the machine without the programming application managing transfer.
- **"Robot programming is part of this Type"** — REJECTED for the canonical core. One vendor extends the same skeleton to industrial robots (SprutCAM X Robot OLP); directory treats robotics as separate leaves (Robotics Engineering Platform etc.). Kept as vendor extension / L2 note.

## Boundary Findings

1. **CAM — RESOLVED: ALIAS.** The joint review requested by the CAM pass concludes: "CNC Programming Application" and "CAM" denote the **same Application Type** — the same products sold under two names. Evidence (layer B, three independent vendors): Mastercam homepage titled "Your Solution for CNC Programming" while badged "#1 most widely used CAM software"; OneCNC "CAM system for NC part programming"; SprutCAM "CNC programming workflow" for its CAD/CAM product. The candidate "manual-programming-activity slice" outcome is rejected (see Rejected Findings). Both leaves remain in the directory (no silent taxonomy rewrite); this document describes the same Type as applications/cam.md, written from the CNC-programming vantage (the program artifact and its journey), with the alias stated plainly. **Recommend taxonomy-owner consolidation of the duplicate leaf.**
2. **CNC program editors / DNC (Predator class; CIMCO unreachable)** — adjacent companion family. They edit, compare, transfer, and version the NC program artifact but never compute motion from geometry. Not instances of the Type; part of the program's life after it leaves the programming application.
3. **CNC verification / simulation (Vericut class)** — adjacent companion family. Consumes the NC program as input and simulates it against a digital twin of the machine; distinct market family since 1988. Inside programming products, simulation appears as a standard capability — same activity, different product boundary.
4. **CNC control / control-side programming (Centroid class; major control vendors not fetched)** — downstream. The control executes the program and offers machine-side conversational programming modes for simpler work. Preparation vs execution seam. (PLC Programming Environment is the analogous leaf for industrial *logic* control — different machine domain, different program semantics.)
5. **Mechanical CAD** — upstream, unchanged from the CAM pass: authors the geometry; "CAD defines what the part looks like, CAM defines how to make it."
6. **Additive Manufacturing Software** — structurally adjacent, unchanged: same geometry → computed motion → machine output skeleton, additive (material added) vs subtractive (material removed); some suites bundle both.
7. **MES / Production Planning / Shop Floor Management** — downstream execution: schedules and tracks production; the programming application prepares the program a machine will run.
8. **Tool Management** — adjacent: administers the physical tool inventory; programming applications reference tool definitions inside programs.

## Uncertainties

- No Tier-1 operational documentation reachable for any sampled product (this pass and the CAM pass) — fine-grained operation model, exact parameter sets, and exact state naming are inferred from product-page language only; the final document deliberately avoids precise operational claims.
- CIMCO unreachable (403 ×2) — the editor/DNC family's breadth is evidenced through Predator only; no claims made about CIMCO.
- OneCNC and SprutCAM verification/simulation capabilities were not observed on the fetched pages — not claimed either way.
- The practice of feeding shop-floor program corrections back into the programming application is plausible but not directly evidenced on fetched pages — kept out of the final document except as a weakly-worded iteration note already supported by the CAM pass ("design changes and program corrections loop back").
- Control-side conversational programming evidenced via one control vendor (Centroid); major control makers (FANUC Manual Guide i, Haas) not fetched — the control-side placement is asserted at "observed at one vendor, structurally consistent with the control's role" strength.
- Whether any market segment genuinely buys a standalone "CNC programming" product that has no geometry-driven computation at all cannot be excluded from Tier-2 evidence alone; if it exists, it did not surface under the "CNC programming software" name in this sample.

## Final Synthesis

The joint review resolves the flagged boundary: **CNC Programming Application is the market's second name for the CAM category.** The leaf documents the same Application Type as CAM: part geometry in → software-computed machine motion → machine-executable NC program out, bound to a specific machine/control. The name "CNC programming" foregrounds the activity and the program artifact; "CAM" foregrounds the computer-aided manufacturing process; vendors use both for the same products. Around the programming application sits a companion toolchain that moves and safeguards the program artifact — editors that compare and edit G-code, DNC networks that transfer it, verification systems that simulate the actual code against a digital twin, revision control that versions it — and, downstream, the machine control that executes it and offers its own conversational programming mode. All of these are adjacent, none of them is the Type. The manual-programming-slice outcome was tested and rejected: the code-direct family self-identifies as editing/transfer/verification, and the term "CNC programming software" belongs to the CAM vendors. Both directory leaves are documented; consolidation is recommended for the taxonomy owner.
