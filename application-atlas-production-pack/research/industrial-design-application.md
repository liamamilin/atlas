# Research Notes — Industrial Design Application

Research date: **2026-09-08**

## Research Goal

Understand, from real products, what an Industrial Design Application (the traditional "CAID" — computer-aided industrial design — lineage, listed in §16 Engineering, Manufacturing & Industrial) actually is: the objects in its world, the primary activity loop, the interfaces, the rules that govern its output, and — critically — how it stays distinct from Mechanical CAD, generic 3D modeling, and digital sculpting, given that the modern market heavily hybridizes all of these.

## Initial Boundary

Working hypothesis before research:

- **What**: software for designing the *form and appearance* of physical products — freeform, dimensionally accurate 3D geometry, refined iteratively, visualized, and handed to engineering/manufacturing.
- **Who**: industrial designers, product designers, automotive/mobility designers, footwear, furniture, consumer-electronics designers; sometimes engineers doing form studies.
- **Nearest Types**: Mechanical CAD (§16 sibling), 3D Modeling Application / Digital Sculpting Application (§04.13), 3D Rendering Application (§04.14), UI Design Application (§04.15), CAE / PLM (§16 downstream).
- **Possible boundary confusions**: (1) ID vs MCAD — modern products straddle the seam; (2) ID vs generic 3D modeling — same tools, different destination; (3) is the modeling medium (NURBS vs SubD vs parametric history) definitional?
- **Unknowns**: how strongly "handoff to engineering" is definitional; whether rendering/appearance is definitional or common; whether 2D output is in scope; whether the automotive Class-A surfacing pole differs structurally.

## Research Questions

1. What objects exist in the product's world (design/model, sketch, curve, surface, solid, subd, material, drawing, variant)?
2. Which geometry medium and modeling paradigm are definitional vs variant (NURBS / SubD / mesh; direct vs history-based parametric)?
3. What is the primary workflow loop from ideation to engineering handoff?
4. Is visual evaluation (materials, rendering, AR/VR) definitional or common?
5. What surface-quality / form analysis machinery is characteristic?
6. How does the downstream exchange to engineering/manufacturing actually work (formats, direction, fidelity)?
7. Do older / minimal / differently-positioned products still fit the definition (historical check)?
8. Where exactly are the boundaries vs Mechanical CAD, 3D Modeling Application, and Digital Sculpting?

## Representative Products

Selected for market representation, documentation accessibility, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / tier | Why sampled |
|---|---|---|---|
| Rhinoceros 3D (Rhino 8) | Robert McNeel & Associates | NURBS-first universal freeform modeler; independent→enterprise; ubiquitous in ID studios | The reference freeform-precision modeler; deep official feature documentation |
| Shapr3D | Shapr3D Zrt | Hybrid direct+parametric CAD, iPad/Pencil-first, desktop+Vision Pro; SMB→enterprise (automotive OEM references) | The modern "CAD that keeps pace with ideas" pole; explicit industrial-design positioning |
| Gravity Sketch | Gravity Sketch Ltd | VR-first immersive 3D ideation + collaboration for design teams (footwear, automotive, transport) | A different interaction surface entirely; enterprise design-team tier |
| Plasticity | (independent) | Direct-editing precision solids/surfaces, no history tree; perpetual license; solo designers | The current "CAD for industrial designers" precision pole; anti-parametric philosophy |
| MoI (Moment of Inspiration) | Triple Squid Software Design | Minimalist NURBS modeler "for designers and artists"; companion-modeler posture | The minimalist/long-lived pole; deliberately externalizes rendering |

Deliberately not sampled: Autodesk Fusion / Autodesk Alias (the integrated-cloud pole and the automotive Class-A pole) — Autodesk help and product surfaces were unreachable from this environment (see Sources); they are held as unsampled, and no product-specific claims about them appear anywhere.

## Sources

Fetched 2026-09-08 (all official vendor surfaces):

- Rhino — https://www.rhino3d.com/features/ (Tier 1–2; deep feature lists) and https://www.rhino3d.com/nurbs (official NURBS explainer)
- Shapr3D — https://www.shapr3d.com/ and https://www.shapr3d.com/use-case/industrial-design (Tier 2 product pages incl. vendor's own category definition and FAQ)
- Gravity Sketch — https://www.gravitysketch.com/ (Tier 2) and https://help.gravitysketch.com/ + https://help.gravitysketch.com/creation-tools (Tier 1 help-center structure)
- Plasticity — https://www.plasticity.xyz/ (Tier 2 with substantive workflow claims)
- MoI — https://moi3d.com/ (Tier 2, thin — positioning-level only)

**Source-access limitations:**

- https://help.autodesk.com (two path variants) and https://www.autodesk.com/products/... → 404/403. Autodesk products (Fusion, Alias) therefore NOT used as evidence; the integrated-cloud and Class-A poles are held at market-structure strength only.
- https://support.shapr3d.com (help center) → 403; main site used instead. Shapr3D claims held at product-page strength.
- https://support.gravitysketch.com → 404; help.gravitysketch.com reachable.
- No precise numeric limits, plan-gated feature matrices, or kernel-version details are asserted anywhere from these gaps.

## Product Observations

### Rhinoceros 3D (McNeel) — evidence layer A (direct, official feature docs + NURBS page)

- Self-description: "create, edit, analyze, document, render, animate, and translate NURBS curves, surfaces and solids, subdivision geometry (SubD), point clouds, and polygon meshes" — no complexity limits beyond hardware.
- Accuracy claim: "Accuracy needed to design, prototype, engineer, analyze, and manufacture anything from an airplane to jewelry" — precision for manufacture is an explicit product pillar.
- Model creation: full curve vocabulary (free-form curves, control points, sketch), surface creation (loft/sweep/blend/network/patch/revolve...), solids, meshes, SubD. Editing: trim/split/join/Boolean/fillet/match/rebuild; control-point editing of curves and surfaces.
- Rendering & presentation: built-in raytrace renderer (textures, lights, UV mapping, procedural textures), real-time preview, display modes; "High-quality presentations are critical to most design projects."
- Drafting: 2D drawings with dimensions/annotation; the vendor explicitly frames drafting as how "every type of physical product design" communicates "ideas, specifications, and instructions to people in design, development, and fabrication."
- Surface analysis: curvature graph, geometric continuity, deviation, draft angle, zebra stripes, environment map, Gaussian/mean curvature, naked edges — a surfacing-quality inspection suite.
- Digital fabrication section: models must be "accurate enough for and accessible to all the processes involved in a design becoming a reality"; ShrinkWrap for watertight 3D-print meshes.
- Compatibility: reads/repairs IGES; exchanges STEP/IGES/meshes with CAD/CAM/CAE/render/animation products; openNURBS/3DM.
- Historical anchor (documented by the vendor itself): "the Rhino development project started more than 25 years ago to provide marine designers with tools for building computer models that could be used to drive the digitally controlled fabrication equipment used in shipyards" — i.e., accurate product geometry bound to fabrication from the start.
- Grasshopper: graphical algorithm editor for form generation without code (parametric/algorithmic generation as an add-on layer, not the base paradigm).
- No parametric feature tree as the base paradigm; direct geometric editing throughout.

### Shapr3D — evidence layer A (direct, official product pages + ID use case + FAQ)

- The vendor's own category definition (FAQ): "3D industrial design software is a category of CAD used to create and visualize physical products before they are manufactured. Unlike 3D design software more often used by artists and animators, it prioritizes mechanical accuracy and manufacturability." And: modern industrial design software "bridges the gap between artistic form and functional engineering."
- Modeling: sketches with constraints; "integrates direct and history-based workflows"; direct modeler "so you can start fluid and design without parameters if it suits you," with parametric capability "preserving design intent."
- Geometry kernel: Siemens Parasolid under the hood; "Geometry is precise and accurate for simulation and manufacturing processes."
- Visualization: real-time PBR "with high quality materials and lighting. A single click switches between modeling and rendering modes"; materials, environments, AI renders.
- 2D drawings for technical documentation; AR "core workflow, not a plugin"; native Vision Pro with editing in XR.
- Design reviews: browser review links where collaborators rotate/zoom/comment; live edits in the meeting.
- Exchange: import STEP, IGES, XT (Parasolid), SLDPRT, CATPART, PRT-class natives; export STEP/XT "for seamless engineering handoff," STL/3MF for printing, OBJ/USDZ for visualization/AR. Format availability varies by plan (free plan restricts exports).
- Device story: iPad + Apple Pencil first, Mac/Windows/visionOS; offline local storage + cloud sync; team spaces/file management.
- Stated industries: industrial design (consumer electronics, appliances, lifestyle), mechanical engineering (jigs/fixtures), furniture/woodworking, automotive parts.

### Gravity Sketch — evidence layer A (direct, official site + help center)

- Self-description: "an immersive 3D workspace built for ideation and collaborative problem-solving" for design teams.
- Value framing: "Traditional product design can be slow and expensive, with collaboration left too late"; earlier collaboration and earlier decisions.
- Capability pillars on the site: ideate at speed in 3D ("map out objects and environments... to understand spatial constraints"); explore manufacturability ("comparing design ideas against engineering data in 3D. Understand component fit and balance aesthetics with hardpoint requirements"); assess ergonomics and proportions "at 1:1 scale in VR... with human factors experts"; contextualized feedback in immersive design reviews with annotations/edits.
- Help-center creation-tool structure (Tier 1): sketching tools, ink/strokes, weighted control points, sketching aid, snapping, mirror, reference images, layers, groups, grid, measurement tool, 1:1 scale, color & materials, paint brush; a full SubD editing suite (extrusion, crease, loop addition, thicken & offset, smooth, merge & separate, adjust roundedness).
- Collaboration: join via VR or desktop in the same virtual space; review mode; presentation mode; annotations.
- Import & export framed as "move data seamlessly between VR, screen, and downstream tools"; cloud file management (Web for individuals, LandingPad for businesses).
- Customer evidence (official testimonials): New Balance senior industrial designer on communicating design intent in 3D "rather than 2D orthographic views"; Polaris senior industrial designer: built an instrument panel model in hours "and was able to hand over that same model to engineering" (→ engineering handoff documented from the customer side on the vendor's official site).

### Plasticity — evidence layer A (direct, official site)

- Self-description: "Powerful solid and surface modeling"; "From vehicle design to industrial design to video game art, Plasticity gives you the tools to create perfect solids and surfaces."
- Paradigm: direct editing — "Push, pull, and adjust existing geometry without starting from scratch... Modify CAD data instantly with no history tree required."
- Precision: "live dimensions that update geometry instantly. Model with engineering-grade accuracy while keeping the flexibility of direct-editing workflows"; dimensions and PMI.
- Surface quality: "curvature-perfect fillets that adapt intelligently to edge conditions"; XNURBS G2-continuous blends "between even the most irregular shapes."
- Positioning vs parametric CAD: "Plasticity is a powerful complement to other CAD tools. History-based parametric modeling is valuable but costly: to keep feature trees robust, many advanced solid and surfacing tools are disabled. Plasticity... exposes the full power of Parasolid and xNURBS. With Plasticity, you can rapidly create precise surfaces and complex solids."
- Exchange: STEP import; export STEP, IGES, ACIS, Parasolid (XT), OBJ, STL by tier; Rhino import; Blender bridge.
- Tiers: free trial / Indie / Studio; perpetual license, no subscription.

### MoI (Moment of Inspiration) — evidence layer A (direct, official site; thin — positioning-level only)

- Self-description: "MoI, 3D modeling for designers and artists"; "CAD software that's a little different. Focused on being easy to use, it's a great tool for designers and artists who want to construct accurate models."
- Workflow: "Booleans and 2D profile curve driven workflow."
- Posture: "makes a great companion modeler for rendering/DCC projects" — i.e., rendering can live outside the ID modeler; MoI itself is the precision form-construction stage.
- "Best-in-industry mesh export supporting n-gon mesh generation. Great for 3D printing."

## Cross-product Comparison

| Dimension | Rhino | Shapr3D | Gravity Sketch | Plasticity | MoI |
|---|---|---|---|---|---|
| Primary medium | NURBS + SubD + mesh + point clouds | Parasolid solids/surfaces (+ sketches) | SubD over freehand strokes | Parasolid solids + xNURBS surfaces | NURBS (2D-profile-driven) |
| Paradigm | direct geometric editing (+ optional Grasshopper) | hybrid direct + history | freehand immersive + SubD | pure direct, explicitly no history | direct, 2D-profile booleans |
| Precision/manufacture framing | "accuracy needed to design... and manufacture" | "mechanical accuracy and manufacturability" | compare against engineering data; hand model to engineering | "engineering-grade accuracy" | "construct accurate models"; 3D printing |
| Appearance/visualization | built-in raytrace renderer + display modes | built-in PBR, one-click visualization | in-VR color & materials, environments | materials in-product | delegated to companion renderers |
| 2D documentation | full drafting/annotation | 2D drawings module | none documented (2D orthographic views named as the thing replaced) | dimensions/PMI only | — |
| Analysis of form | curvature/zebra/draft/continuity suite | — (not documented) | measurement, 1:1 scale, ergonomics in VR | continuity (G2) control, fillets | — |
| Exchange | STEP/IGES/meshes/3DM ecosystem | STEP/XT/IGES/native imports/print + AR formats | "VR, screen, and downstream tools" | STEP/IGES/Parasolid/meshes | mesh export, 3D printing |
| Collaboration | worksessions/files (thin) | cloud team spaces, review links | multi-user VR sessions, review mode | — | — |
| Interaction surface | desktop (Win/Mac) | iPad/stylus, desktop, Vision Pro | VR headsets + desktop | desktop | desktop |
| Ideation input | curves/sketch; scan/point clouds | Pencil sketching | 3D strokes in space at 1:1 | direct geometry | 2D profile curves |

**Pattern that unifies all five** (evidence layer B): precise, dimensionally real freeform geometry of a *physical product's form*, constructed through a sketch/curve-driven form-first loop, visually evaluated in or around the same environment, and exchanged toward engineering/manufacturing in geometry-preserving formats. Every product's marketing language ties the tool to *manufacture-bound accuracy*, and four of five explicitly contrast themselves with (or complement) either artists' 3D tools or history-based engineering CAD.

**Pattern across the sample about paradigms** (layer B): none of the five is a classical history-first parametric modeler — the sample spans "no history" (Plasticity, MoI), "history optional/hybrid" (Shapr3D), "history absent, algorithmic add-on available" (Rhino), "freehand immersive" (Gravity Sketch). The ID population gravitates toward *direct, exploratory* manipulation even where parametric machinery exists. This is characteristic of the Type but the *paradigm itself* is variant (see L2), not the invariant.

## Canonical Abstraction

### Level 0 — Defining Invariant

Three jointly-held structures:

1. **The product form as precise freeform geometry — the unit of record.**
   A persistent, dimensionally accurate 3D representation of a physical product's external form (curves → surfaces/solids, or subdivision surfaces), held in real-world units. It is the authoritative artifact of the design, and everything else (images, renderings, drawings, reviews) is derived from it. Remove → generic 3D modeling/illustration or a sketch tool; the "industrial" identity is gone.

2. **The form-first iteration loop.**
   The primary activity is exploring and refining *shape and appearance*: start from references/sketches/curves, build and directly edit surfaces/solids, evaluate visually, and repeat — converging on design intent. Construction is optimized for expressive exploration of form (direct manipulation, fluid push/pull/stroke, minimal constraint machinery), which is precisely what the sampled products advertise against history-first engineering CAD. Remove → the environment becomes Mechanical CAD territory (engineering-function-driven geometry).

3. **Manufacturing-bound precision and exchange.**
   The geometry exists so that a physical product can be made from it: real-world dimensional accuracy is structural, and the design must be exchangeable into engineering/manufacturing-usable forms (neutral CAD formats such as STEP/IGES/Parasolid-class, watertight solids/meshes for fabrication). Remove → a concept-visualization / art surface; the "physical product" purpose collapses.

Jointly-held load-bearing:

- 1 alone = precision geometry engine / generic 3D modeling (04.13)
- 1+3 without 2 = Mechanical CAD territory (engineering-centered construction)
- 2 without 1+3 = freeform sketching/sculpt ideation without manufacture-bound output
- 1+2 without 3 = concept-art / entertainment modeling
- 3 without 1+2 = geometry conversion / CAM utility, no design work

### Level 1 — Common Mature Structure

Present in most sampled products, not required for the definition:

- **Sketch/curve construction layer** — 2D profiles, construction planes, constraints (optional), reference image underlays, symmetry/mirror.
- **Surface & solid editing toolkit** — fillets, blends, Booleans, offsets/thicken, trim/split/join, direct face pushing/pulling, SubD crease/smooth.
- **Surface-quality evaluation** — continuity control (G2-class blends documented in two products), curvature/zebra/draft-class inspection suites (documented in one; measurement/1:1 ergonomics in another). Depth varies strongly; presence is common.
- **Materials/appearance and realistic display** — in-product PBR/raytrace rendering, display modes, environments, turntables. (MoI documents externalizing this stage — common, not definitional.)
- **2D communication outputs** — drawings/dimensions/annotation/technical documentation (absent/thin in the VR-first pole).
- **Neutral-format exchange + mesh exports** — STEP/IGES/Parasolid-class for engineering; STL/OBJ/3MF-class for printing and visualization.
- **Object management** — layers, groups, block/instance reuse, snapping, grids, numeric input, units.
- **Scan/capture ingestion** (one product, documented deeply) and 3D-print preparation (two products) — common modern capabilities.

### Level 2 — Variant / Optional Structure

- **Modeling medium**: NURBS (dominant, 4/5) vs SubD (one product's core; another's complement) vs solids kernels — the invariant is *precise freeform geometry*, not the mathematical medium. (Anti-overfitting: NURBS fails the "remove it and it's not this Type" test because the SubD-centric product is clearly in-type.)
- **Modeling paradigm**: no-history direct (2), hybrid direct+history (1), freehand immersive (1), direct + optional algorithmic editor (1).
- **Interaction surface**: desktop workstation, tablet/stylus-first, VR-first, XR review companion.
- **Rendering posture**: in-product photoreal rendering vs external-renderer/companion-modeler split.
- **Collaboration/review surfaces**: cloud team spaces, browser review links, multi-user VR sessions — modern-common, absent in classic minimal poles.
- **Parametric/algorithmic generation** (history trees, constraint systems, node-based form generation) — optional layer.
- **Ergonomics validation at 1:1 scale in XR** — immersive pole only.
- **AI-assisted rendering/imaging** — single vendor (L3-adjacent; optional modern capability).
- **Licensing shape** (perpetual vs subscription vs free tiers) — commercial variant.

### Level 3 — Vendor-specific Structure

Kept out of the canonical document:

- Grasshopper as a bundled graphical algorithm editor (vendor-named implementation of algorithmic form generation).
- LandingPad / Gravity Sketch Web cloud file management naming.
- xNURBS technology branding; Parasolid kernel naming as a marketing differentiator; Blender bridge.
- AI renders as a branded capability; Vision Pro-native editing as a platform exclusivity.
- Rhino's specific openNURBS/3DM ecosystem and Zoo/Cloud Zoo licensing machinery.

### Rejected Findings

- **"NURBS-based" as defining** — rejected by the historical/medium check above; recorded as dominant implementation.
- **"No parametric history" as defining** — rejected: one sampled product ships optional history; another sells parametric capability. The stable claim is weaker: the paradigm *de-emphasizes* constraint-first construction relative to engineering CAD.
- **"Includes photorealistic rendering" as defining** — rejected (MoI counterexample).
- **"Multi-device/cloud" as defining** — rejected: classic desktop-only and minimal poles satisfy the Type.
- **"Collaboration built-in" as defining** — rejected: only modern/team poles document it.
- **"CAD kernel X" as defining** — implementation detail, vendor-specific.

## Historical / Market-Sample Check

- **Rhino's own documented origin** (vendor page): mid-1990s marine-design tooling whose models "could be used to drive the digitally controlled fabrication equipment used in shipyards" — accurate freeform product geometry + form-first modeling + fabrication destination, with no cloud, no PBR, no AR/VR, no history trees, no SubD, no collaboration machinery. All three Level-0 legs hold.
- **MoI** (2000s minimalist, no cloud/paradigm machinery) satisfies all three legs.
- **Early CAID generation** (form•Z-class solids/surfaces modelers of the early 1990s; Alias-class industrial surfacing) satisfies the legs conceptually — kept conceptual because vendor documentation was not accessible this pass; no product-specific claims made.
- The pre-digital lineage (marker sketches + foam/clay models) is the conceptual ancestry of the loop but not the software Type itself.
- Conclusion: the definition names no era machinery — no specific kernel, rendering technology, device form, collaboration model, licensing model, or paradigm.

## Boundary Findings

**vs Mechanical CAD (§16 sibling — most important seam).**
Shared surface: both produce dimensionally accurate solids/surfaces and exchange STEP-class formats. Discriminator recorded from this pass: **center of gravity** — the industrial design application centers *form/appearance exploration* (freeform precision, direct fluid editing, appearance definition, design communication) while mechanical CAD centers *engineering function definition* (parametric feature trees carrying design intent for controlled change, assemblies, engineering drawings/GD&T, manufacturing features). Three of five sampled products explicitly position themselves *relative to* parametric engineering CAD (one as "complement to other CAD tools," one as "the link between concept design and engineering," one as offering both "so you can start fluid... but it also has parametric modeling"). The seam is heavily hybridized in the current market; both Types remain distinct populations, but **joint review with the mechanical-cad pass is recommended** to ratify the center-of-gravity discriminator (forward flag recorded in STATUS.md).

**vs 3D Modeling Application (§04.13).**
Same tool family surface (meshes/geometry/viewports), different destination and precision: the generic 3D modeling Type serves illustration/animation/games with no dimensional or manufacturing contract. Vendor-documented seam (one sampled product's FAQ): industrial design software "prioritizes mechanical accuracy and manufacturability" unlike "3D design software more often used by artists and animators." Test: remove manufacturing-bound precision + exchange → the product is that Type.

**vs Digital Sculpting Application (§04.13).**
Sculpting manipulates dense meshes artistically with no dimensional/manufacturing constraints; some ID ideation uses sculpting tools, but the sampled ID population uniformly stakes its identity on accuracy and manufacturability. Sculpt-in-ideation is a workflow variant, not a Type merger.

**vs 3D Rendering Application (§04.14).**
Rendering is a common *stage* (L1) but delegable — one sampled product is explicitly a companion modeler whose rendering happens elsewhere. A standalone renderer owns no product-form geometry of record → different Type.

**vs UI Design Application (§04.15).**
Different design domain (digital interfaces vs physical product form); no manufacturing contract. Only superficial vocabulary overlap ("design").

**vs CAE / Engineering Simulation and PLM (§16).**
Downstream consumers of the industrial design output (the geometry feeds simulation/engineering; the design record feeds the product record). Not form-defining environments → not this Type.

## Uncertainties

- **Automotive Class-A surfacing pole** (Alias/ICEM-class): structurally unverified this pass (Autodesk unreachable). Held at market-structure strength; nothing product-specific asserted. If that pole differs materially (e.g., much heavier continuity/grading machinery as core), the L1 "surface-quality evaluation" tier may need deepening, but the L0 legs should still hold.
- **Format availability granularity** varies by product edition/plan (documented in one sampled product); no per-plan format claims are made in the final document.
- **MoI evidence is thin** (single page); used only for positioning-level observations and as the minimal-pole historical/external-rendering counterexample.
- **Gravity Sketch's downstream fidelity** (how far SubD ideation geometry survives into engineering) is not fully verifiable from public docs; handoff claims are kept at the customer-testimonial strength documented on the vendor's own site.
- The **proportion of the ID population that works history-based** (hybrid products' parametric usage) is not measurable from marketing docs; final document says only that both paradigms are common.

## Final Synthesis

An Industrial Design Application is the **form-defining environment of physical product development**. Its world is organized around one authoritative artifact — the product's form as precise, dimensionally real freeform geometry — created and continuously reshaped through a form-first loop (references/sketches → curves → surfaces/solids/subdivision → direct refinement → visual evaluation → repeat), and consumed by a downstream that will manufacture what the geometry says. Everything else that modern products carry — photoreal rendering, 2D documentation, analysis suites, XR reviews, collaboration, parametric options, algorithmic generation, scan ingestion, print preparation — is accretion around that spine, and the definition deliberately names none of it.

The Type survives the historical check (1990s marine-design Rhino, 2000s minimalist MoI, and conceptually the early-1990s CAID generation), the medium check (NURBS and SubD products both in-type), the paradigm check (historyless and hybrid products both in-type), and the surface check (desktop, tablet, and VR poles all in-type).
