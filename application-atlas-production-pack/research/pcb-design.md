# Research Notes — PCB Design

Research date: 2026-09-09

## Research Goal

Understand what a PCB Design application is as an Application Type: its core object world, its defining workflow (from circuit connectivity to fabricated board), its interfaces, rules, and its boundaries against neighboring Types — especially **ECAD / EDA**, whose electronic pole was flagged by the earlier ecad-eda pass as overlapping this leaf (joint review delegated to this pass).

## Initial Boundary

Working hypothesis before research:

- PCB Design software = tools for designing printed circuit boards: schematic capture, board layout (placement + routing), design-rule checking, fabrication output (Gerber/drill/assembly).
- Nearest neighbors: ECAD/EDA (family leaf, electronic pole overlap), Electrical Design Application (electrical pole), Mechanical CAD (co-discipline), Semiconductor Design Platform (IC-scale EDA), CAM (downstream manufacturing data).
- Known issue from STATUS.md Boundary Issues: ecad-eda pass found that the electronic pole of ECAD/EDA self-identifies as "PCB design software" — schematic capture + board layout + fabrication outputs are one product. This pass must discharge that joint review.

## Research Questions

1. What is the core object world? (board, layer stackup, footprint, pad, net, track/via/zone, design rules)
2. How does connectivity enter the board — schematic transfer, netlist import, or direct in-board definition?
3. How does the schematic↔board synchronization work (forward/back annotation, cross-probing)?
4. What does the routing interaction look like (modes, differential pairs, length tuning, autorouting)?
5. What design rules exist and how do they gate the design (DRC, net classes, constraint management)?
6. What are the fabrication outputs (Gerber, drill, pick-and-place, BOM, assembly drawings)?
7. What analysis capabilities exist (ERC/DRC, SPICE, signal/power integrity, DFM)?
8. How do libraries work (symbols, footprints, 3D models, component data portals)?
9. What differs across market tiers (open-source / professional / cloud-freemium / enterprise)?
10. Where exactly is the seam to ECAD/EDA, and can PCB Design stand as its own Type?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / Tier | Evidence tier reached |
|---|---|---|
| KiCad | open-source, full-flow suite; hobbyist → professional | Tier 1 (full official reference manual, PCB Editor) |
| Altium Designer | commercial professional desktop suite; SMB → enterprise | Tier 1 (official documentation: PCB layout, fabrication/release pages) |
| EasyEDA | web-based freemium, fabrication-integrated (JLCPCB/LCSC); maker → low-cost pro | Tier 1 (official user guide: PCB layout, DRC, board-only pages) |
| Cadence OrCAD X / Allegro X | enterprise commercial platform (PCB design + analysis) | Tier 2 (official product pages; operational docs gated) |

## Sources

- KiCad — PCB Editor reference manual (9.0): https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html (fetched in full)
- Altium — Altium Designer documentation portal: https://www.altium.com/documentation/altium-designer
- Altium — Laying Out Your PCB: https://www.altium.com/documentation/altium-designer/pcb
- Altium — Preparing Your Design for Manufacture: https://www.altium.com/documentation/altium-designer/preparing-for-manufacture
- EasyEDA — Std User Guide: Introduction, PCB Layout, Design Rule Check, Layout a PCB Without Schematic: https://docs.easyeda.com/en/... (multiple pages fetched)
- Cadence — OrCAD X Platform product page: https://www.orcad.com/ (fetched; saved output)
- (Context from prior pass) ecad-eda application document + research notes, 2026-09-07

## Product A — KiCad (open-source suite)

### Key observations (evidence layer A unless noted)

- Self-description: "The KiCad PCB Editor is a PCB layout application"; integrated with the Schematic Editor "for designing printed circuit boards from schematics without using any intermediate files"; can also **import netlist files** from other packages (board without KiCad schematic).
- **Basic PCB concepts** (doc's own list): a board is made up of **footprints** (components + pads), **nets** (how pads connect), **tracks, vias, filled zones** (copper connections), and graphic shapes (board edge, silkscreen). "KiCad normally keeps the information about nets on a PCB synchronized with an associated schematic, but nets can also be created and edited directly within the PCB editor."
- **Board-only mode exists**: "Starting from scratch — It is also possible to create a board with no matching schematic, although this workflow has some limitations and is not recommended for most users."
- **Layers**: copper layers + technical layers (silkscreen, solder mask, adhesive, solder paste) + user layers; active-layer model; layer visibility/opacity controls; board stackup editor with copper count, thickness, material; copper layers can be typed signal/power plane/mixed/jumper. Documented capacity: up to 32 copper layers (product/version-specific fact — L3).
- **Board outline**: graphical objects on an Edge.Cuts layer define a closed outline; interior cutouts supported; invalid outline disables 3D viewer and some DRC checks; zones only fill inside the outline.
- **Footprints**: added automatically by "Update PCB from Schematic" (forward annotation), clustered by schematic sheet; pads matched to symbol pins by number; can also be added manually (PCB-only workflows); placed/moved/rotated/flipped side; embedded copy from library, manual update from library; footprint editor for authoring; per-instance pad overrides.
- **Routing**: interactive router with three modes — Highlight Collisions (manual), Shove (push-and-shove), Walk Around; H/V/45 default with free-angle option; differential pair routing; length/skew tuning (serpentine); router respects design rules by default; track posture/corner modes; dragging re-routes attached tracks.
- **Zones**: copper pours assigned to a net; fill computed against clearance; thermal reliefs / solid pad connections; priority between zones; islands removal policy; manual refill model with warnings before output/DRC ("It is important to make sure zone fills are up-to-date before generating outputs").
- **Design rules**: Board Setup constraints (min clearance, track width, via sizes) as absolute minimums; **net classes** (clearance/width/via/diff-pair per class); **custom rules language** for conditional constraints; violation severity configuration (error/warning/ignore).
- **DRC**: verifies board meets setup rules **and that all pads are connected according to the netlist or schematic**; three result tabs — violations, unconnected items, **parity differences between schematic and PCB**; exclusion with comments; clearance/constraint resolution tools.
- **Forward/back annotation**: Update PCB from Schematic (adds footprints, updates nets; change list applied on confirm; UUID-based symbol↔footprint linking, optional re-link by reference designator); Update Schematic from PCB (back-annotates reference designators, values, footprint assignments, net names); geographical re-annotation tool.
- **Cross-probing**: bidirectional selection/highlight between schematic and PCB.
- **Ratsnest**: unrouted-connection display; per-net visibility/colors; "hiding nets in the ratsnest does not change the connectivity... only intended to make the ratsnest easier to understand."
- **Inspection**: net inspector, board statistics, measurement, find/search, **3D viewer** with exported 3D models (STEP etc.).
- **Fabrication outputs**: Gerber (primary plotting format; job file with stackup/materials; X2 attributes/netlist), drill files (Excellon/Gerber X2 + drill map), **component placement files** (pick-and-place: position/orientation per footprint, SMD/DNP filters), IPC-2581, ODB++, GenCAD, PDF/SVG/DXF/HPGL plots, IPC-D-356 netlist, BOM (board-side BOM "included for legacy reasons" — schematic-side BOM recommended).
- Scripting (Python), text variables, embedded files — advanced extras.

## Product B — Altium Designer (commercial professional)

### Key observations

- Positioning: unified design environment; editors for schematic, PCB, library, etc.; "create, edit, and verify your PCB designs" in the PCB editor.
- **Board shape**: default rectangle; redefined interactively in Board Planning Mode; board outline = extents of the board.
- **Layers**: electrical layers (documented capacity: 128 signal + 16 internal plane layers — L3 fact), component layers (overlay/silk, solder mask, paste), mechanical layers (pairable), other layers (keep-out, multi-layer, drill drawing/guide); layer display config; single-layer mode.
- **Layer Stack Manager**: a document-like editor for the fabrication stackup; add/remove/configure layers; material library; presets; **Via Types** tab defines allowed layer-spanning vias (thru, blind, buried, micro).
- **Design rules**: PCB Rules and Constraints Editor; rule categories/types/individual rules; **unary rules** (e.g., Width — one scope) vs **binary rules** (e.g., Clearance — two scopes); rule scope/query expressions; **rule priority** resolution; constraints per rule. Newer projects may use a **Constraint Manager** spanning schematic and layout instead.
- **Schematic→PCB transfer**: "Design » Update PCB Document" runs an **ECO (engineering change order) execution process**; footprints placed at arbitrary positions; pads connected by **connection lines** per nets from schematics.
- **Placement**: move/rotate/flip (L key flips side); connection lines re-optimize as components move (guides placement to reduce crossings).
- **Routing**: Interactive Routing; rule-driven (Clearance, Width, Routing Via Style must be configured first); conflict-resolution modes cycled during routing (Walkaround / Push / Ignore); corner modes; look-ahead segment; **clearance boundaries** visualization around other nets; auto-complete routing (Ctrl+Click); loop removal on reroute; track sliding/dragging.
- **Polygons**: polygon pour pours around existing objects, connects only to same-net objects; repour after modification; connection style governed by rules.
- **DRC**: online (real-time) and batch modes; violations displayed with custom graphics/overlay; violation detail shows measured vs constraint values; PCB Rules And Violations panel; per-rule enable/disable for online/batch; recommendation to stage checks during design (e.g., disable un-routed-net check until fully routed).
- **Fabrication/release**: outputs individually or via **OutputJob** (pre-configured output sets: assembly outputs, fabrication outputs, report outputs; containers: PDF/folder/print); **Project Releaser** staged flow — configure (source/fabrication/assembly data, per-variant) → **validate project** (DRC-class checks; release fails if validation fails) → generate data → review → upload → report; release to Workspace/folder/zip.
- **Workspace collaboration**: Altium 365 / on-prem Enterprise Server; web viewing/commenting/markup of PCB designs; multi-designer; **MCAD CoDesigner** push-pull sync with mechanical CAD; atomic design releases as manufacturing packages.
- Other documented areas: ActiveBOM, Draftsman (board documentation), multi-board design, harness design, rigid-flex, high-speed design, PSpice-class simulation (circuit simulation page), importing from PADS/EAGLE/Expedition/Allegro (evidence of a long-lived shared object model across the industry).

## Product C — EasyEDA (web-based, fabrication-integrated)

### Key observations

- Self-description: "a great web based EDA tool for electronics engineers, educators, students, makers and enthusiasts"; no install; browser-based; client optional.
- **Design flow**: schematic (with LTSpice-based simulation) → "Convert to PCB" (Menu - Design - Convert to PCB) → PCB layout → DRC → Gerber/drill generation → order PCB (JLCPCB integration); BOM export; pick-and-place export.
- **PCB canvas**: layer manager (colors/visibility, active layer); design manager (locate components/tracks/net pads); board outline editing; **ratline** (their term for ratsnest); PCB nets; copper pour; solid regions; panelize; PCB modules; 3D view / photo view; 3D model manager.
- **DRC**: real-time DRC ("when you routing the DRC will checking all the time... X flag"); rule dialog: per-rule **track width, clearance, via diameter, via drill diameter, track length**; rules assignable per net; "Apply Design Rule while Routing and Placing Via"; DRC error list in design manager with highlight navigation; error types: clearance, track length, track width, via diameter, via drill diameter. Doc's own caveat: "Design rule checking can only help you find some obvious errors."
- **Board-only mode exists**: dedicated doc page "Layout a PCB Without Schematic" — start a new PCB, add footprints directly from the footprint library, route tracks; pad-to-pad connection setting; ratline layer hidden by default in schematic-less PCBs.
- **Sync**: "Import Changes" page (schematic→PCB change import); Cross Probe / Cross Probe and Place pages (schematic↔PCB).
- **Fabrication**: Generate Fabrication File (Gerber); Export Pick and Place File; Export BOM; Export DXF; **Order PCB** page (direct ordering); recommends checking Gerber/drill in an external Gerber viewer before ordering.
- Documented capacity: up to 6 copper layers by default, more on request (L3 fact); board sizes over 100cm×100cm possible (L3).
- Libraries: >1,000,000 public symbol/footprint library entries (vendor-claimed, L3); footprint editor; import from Altium/Eagle/KiCad.

## Product D — Cadence OrCAD X / Allegro X (enterprise commercial)

### Key observations (evidence layer A for page content; product page is Tier-2 marketing — operational detail NOT directly observed)

- Self-labeling: "Next-Gen PCB Design Software"; "a comprehensive and AI-enabled PCB design software built for... small to medium-sized businesses" (OrCAD X); Allegro X positioned as "System and PCB design platform".
- Product decomposition (own naming): **OrCAD X PCB Layout** (layout/routing environment), **OrCAD X Capture** (schematic entry, "dynamic ERC, integrated mixed-signal simulation"), **PSpice** (simulation), **OrCAD X CIP** (component information profile), **OrCAD X OnCloud** (data management/collaboration), Allegro X AI.
- Capability claims (marketing tier — keep weak): intelligent routing engines "including interactive and auto-routing"; in-design DRCs; constraint management "unified interface across schematic and layout environments... hierarchical rule systems"; in-design analysis (Sigrity impedance/coupling); DFM checks with "immediate feedback on fabrication, assembly, and testing parameters"; ECAD/MCAD co-design "real-time bidirectional workflows"; **PCB team design** ("multiple engineers can work on the same PCB layout in real time"); Live BOM (supply-chain data); Live DOC (auto-generated fabrication/assembly drawings, drill tables); 3D viewer with STEP import and IDX exchange "for both rigid and flex PCBs".
- Tier structure: OrCAD X Standard / Professional / Professional Plus (licensing tiers — L3).
- Cadence's own taxonomy places these under "PCB Design & Analysis" alongside Sigrity (SI/PI analysis) — evidence that analysis is a neighboring capability often sold beside the design tool, not the design tool itself.

## Cross-product Comparison

| Structure | KiCad | Altium Designer | EasyEDA | OrCAD X / Allegro X |
|---|---|---|---|---|
| Board as central artifact (outline + layers) | Edge.Cuts outline; stackup editor; copper+technical layers | Board shape; Layer Stack Manager; 128 signal + 16 plane layers (doc) | Board outline; layer manager; 6 copper default (doc) | PCB Layout tool; 3D viewer rigid+flex (marketing) |
| Footprint-based placement | footprints auto-added from schematic; manual add; footprint editor | footprints placed by ECO update; move/rotate/flip | footprints from library; footprint editor | footprint placement (marketing) |
| Nets govern copper; ratsnest | ratsnest; net inspector; nets editable in-board | connection lines per nets; connectivity model doc | ratline; PCB nets; pad-to-pad connect in board-only mode | (not directly observed) |
| Copper geometry: tracks/vias/zones | interactive router (shove/walkaround); zones w/ thermal reliefs | interactive routing (push/walkaround/ignore); polygon pours | route tracks; copper pour | interactive + auto routing (marketing) |
| Design rules + DRC | constraints + net classes + custom rules; DRC w/ parity check | unary/binary rules, priorities; online+batch DRC; Constraint Manager | per-net rules; real-time DRC; 5 error types | constraint management; in-design DRC; DFM (marketing) |
| Schematic integration | Update PCB/Schematic from each other; cross-probing; netlist import | Update PCB Document via ECO; Constraint Manager | Convert to PCB; Import Changes; cross probe | Capture ↔ layout (marketing) |
| Fabrication outputs | Gerber(+job/X2), Excellon drill, pick-and-place, IPC-2581/ODB++, BOM | OutJobs; Project Releaser (validate→generate→release); fab+assembly data | Gerber, drill, pick-and-place, BOM; Order PCB | Live DOC fab/assembly drawings; manufacturing release (marketing) |
| 3D | 3D viewer; STEP export | native 3D + clearance checking; MCAD CoDesigner | 3D view; 3D model manager | 3D viewer STEP/IDX (marketing) |
| Simulation | SPICE (schematic-side; separate manual) | circuit simulation page (PSpice-class) | LTSpice-based simulation | PSpice built-in (marketing) |
| Board-only mode | yes (standalone board editor; netlist import) | (not documented on fetched pages) | yes (dedicated doc page) | (not observed) |
| Collaboration | scripting/community; no cloud in core | Workspace: web review/markup, co-design, releases | project sharing/members; public projects | OnCloud; team layout real-time (marketing) |
| Fab ordering integration | none (files out) | Altimade single-click ordering (doc) | Order PCB via JLCPCB | (not observed) |

**Layer-B commonalities (cross-product):** board outline + layer stackup; footprints with pads; nets binding pads; tracks/vias/zones as copper objects; ratsnest/unrouted-connection display; design rules with clearance/width/via constraints; DRC with violation navigation; schematic↔board transfer with a change-list/confirm step; Gerber + drill + pick-and-place + BOM outputs; 3D visualization; footprint/symbol libraries with editors.

**Product-specific / divergent:** KiCad custom-rules language + geographical reannotation; Altium ECO-based update + OutputJob/Project Releaser + Workspace; EasyEDA real-time DRC default + direct fab ordering + web form factor; OrCAD X team layout + Live BOM/Live DOC + PSpice/Sigrity bundling.

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (jointly-held; deliberately small)

1. **The board as the central persistent artifact** — a closed board outline on a layered substrate (copper layers plus fabrication layers: silkscreen, solder mask, paste); the board is the design of record that the whole application exists to produce. Remove → schematic capture / connectivity diagramming (ECAD schematic territory) or a generic layered drawing canvas.
2. **Footprint-based component placement** — components enter the board as physical footprints (pads carrying copper geometry) that are placed, oriented, and flipped between board sides. Remove → netlist editor or componentless copper artwork.
3. **Net-governed copper geometry** — the application maintains an electrical connectivity model (nets binding pads to each other), and the user realizes it by drawing copper — tracks, vias, zones — with not-yet-routed connections kept visible (ratsnest/connection lines); copper is electrical, not decorative. Remove → generic CAD drawing; remove the nets → copper artwork editing (fab-data CAM territory).
4. **Fabrication output** — the design terminates in manufacturing data for board fabrication and assembly (layer artwork, drill data, placement files, BOM). Remove → a 3D visualization/modeling surface, not a production design tool.

Jointly-held load-bearing analysis:
- 1 alone = layered drawing canvas
- 2 without 3 = mechanical placement/assembly layout
- 3 without 1+2 = connectivity editor (schematic/netlist territory)
- 4 without 1–3 = file converter
- 1+2 without 3 = footprint placement with no electrical routing
- 1+3 without 2 = copper artwork editing (PCB CAM/Gerber-editing territory)
- 2+3 without 1 = connectivity without a substrate — incoherent
- 1+2+3 without 4 = a design that cannot ship = visualization

Anti-overfit notes (shared implementations that are NOT invariants):
- **Schematic capture is NOT L0.** KiCad documents standalone board editing + netlist import; EasyEDA documents a dedicated "Layout a PCB Without Schematic" flow. The schematic is the dominant upstream connectivity source in integrated suites (L1), but the Type stands without it. This is also the seam vs ECAD/EDA (whose center IS the schematic).
- **Gerber specifically is NOT L0** — the invariant is manufacturing data for fabrication; Gerber is today's dominant format (KiCad: "primary plotting format"; EasyEDA: "Generate Fabrication File (Gerber)").
- **DRC is NOT L0** — near-universal in mature products (all four sampled), but a rules engine is a mechanism, not the definition; EasyEDA's own caveat ("can only help you find some obvious errors") shows checking depth varies.
- **3D, autorouting, simulation, cloud, MCAD sync** — none definitional (absent or optional across sample).

### L1 — Common Mature Structure

- Schematic capture integration as the upstream connectivity source: forward transfer (KiCad "Update PCB from Schematic"; Altium "Update PCB Document" ECO; EasyEDA "Convert to PCB"/"Import Changes"), back annotation (KiCad documented; others weaker evidence), cross-probing (KiCad, EasyEDA documented)
- Design rules + DRC: clearance/track-width/via-size constraints; net classes (KiCad, Altium) or per-net rules (EasyEDA); online/real-time + batch checking; violation lists with navigation; violation exclusion/severity
- Interactive routing: mode-based conflict resolution (push/shove vs walkaround vs ignore/highlight); H/V/45 geometry; differential pairs; length tuning (KiCad documented; high-end marketing claims)
- Copper zones/pours with pad-connection policies (thermal reliefs) and refill-before-output discipline
- Layer stackup management (copper count, dielectric/material parameters, via types incl. blind/buried/micro in high-end)
- Footprint/symbol libraries + dedicated library editors; board-embedded copies with manual library sync
- Ratsnest / unrouted-connection display
- 3D board visualization (viewer; STEP-class model exchange)
- BOM + pick-and-place outputs; fabrication/assembly documentation
- Multi-layer boards (layer count is product/version-specific — L3 facts)

### L2 — Variant / Optional Structure

- Circuit simulation (SPICE-class): EasyEDA (LTSpice-based), OrCAD X (PSpice), Altium (circuit simulation docs), KiCad (separate simulator) — common but not universal-in-depth
- Signal/power integrity analysis: high-end pole (Cadence Sigrity in-design; Altium high-speed docs) — segment-dependent
- Autorouter: EasyEDA documents one; OrCAD X marketing claims "interactive and auto-routing"; KiCad manual documents interactive-only routing — variant, not standard
- MCAD co-design: Altium CoDesigner, OrCAD X marketing — optional integration
- Cloud collaboration / multi-user layout: Workspace (Altium), OnCloud/team layout (OrCAD X marketing), project sharing (EasyEDA) — deployment/business-model variant
- Component supply-chain data / sourcing: Live BOM (OrCAD X), Altium supply-chain intelligence, EasyEDA-LCSC — business-model variant
- Direct fabrication ordering: EasyEDA Order PCB, Altium Altimade — ecosystem variant
- Rigid-flex, multi-board systems, panelization, harness design (Altium) — capability variants
- Unified constraint management across schematic+layout (Altium Constraint Manager, OrCAD X marketing) — high-end variant of L1 rules
- DFM analysis (OrCAD X marketing; KiCad has some DFM-oriented DRC checks like malformed outline/soldermask) — depth variant
- Design data management / release processes (Altium Project Releaser/Workspace) — team-deployment variant
- Web vs desktop form factor (EasyEDA vs others) — platform variant

### L3 — Vendor-specific (research notes only)

- KiCad: custom design-rules language; geographical re-annotation; teardrops; text variables; embedded files; 32-copper-layer capacity; 1 nm internal resolution; CMP-file back-annotation
- Altium: ECO execution process; OutputJob containers; Project Releaser staged flow; Draftsman; ActiveBOM; Altium 365 Workspace; MCAD CoDesigner; 128 signal + 16 plane layers; xSignals/high-speed tooling
- EasyEDA: JLCPCB/LCSC integration; Order PCB; 6-layer default; Gerbv recommendation; >1M public library entries (vendor claim); ratline terminology
- Cadence: OrCAD X tier structure (Standard/Professional/Professional Plus); PSpice; Ultra Librarian (18M+ parts claim); Sigrity in-design analysis; Live BOM/Live DOC; OnCloud; Allegro X AI Studio

## Boundary Findings

### 1. vs ECAD / EDA (the delegated joint review — discharge from this side)

The ecad-eda pass (2026-09-07) documented ECAD/EDA as a two-pole Type — electronic pole (boards) + electrical pole (cabinets/harnesses) — centered on **schematic capture + connectivity as the design of record**, and flagged that its electronic pole's products self-identify as "PCB design software".

This pass's findings:

- The overlap is real: the same products (KiCad, Altium, EasyEDA, OrCAD/Allegro) are evidence for both leaves' electronic pole. Schematic capture + board layout + fabrication outputs are one product in the market.
- But "PCB Design" is not merely a variant label: it is the market's own name for the board-design discipline (OrCAD X self-labels "PCB Design Software"; KiCad "PCB layout application"; EasyEDA's whole PCB Layout doc section). The board-centered object world (layer stackup, footprints, tracks/vias/zones, design rules, fabrication outputs) has its own center of gravity that a schematic-centered document does not and should not fully carry.
- **Working resolution (recorded, not silently applied to the directory): keep both leaves as a center-of-gravity split.** ECAD/EDA = the schematic/connectivity-centered family spanning electrical + electronic poles; PCB Design = the board-centered Type (the electronic pole's discipline, named as the market names it). The two documents are complementary: ecad-eda's center is the schematic and its connectivity semantics; this document's center is the board and its physical realization. Recommendation for a future joint review: either re-scope ECAD/EDA explicitly to the electrical pole (with the electronic pole pointing to PCB Design), or keep ECAD/EDA as the family leaf with an explicit "electronic pole ≡ PCB Design" note. Either outcome requires a directory-level decision that this pass does not make unilaterally.

### 2. vs Electrical Design Application

Electrical pole of the ECAD family: devices/terminals/cables/wire lists; physical realization is cabinet/panel/harness layout, not a copper board. No layer stackup, no copper routing, no Gerber-class outputs. Different Type (probable alias of the ECAD electrical pole per the ecad-eda pass).

### 3. vs Mechanical CAD

MCAD's design of record is geometry (solids/surfaces); PCB Design's is connectivity realized on a board. The seam is co-design: board outline/placement/3D flow into MCAD (Altium CoDesigner, OrCAD X marketing). A PCB tool without nets/footprints would be MCAD-adjacent shape drawing.

### 4. vs Semiconductor Design Platform

"EDA" in the broad industry sense spans IC design (HDL, verification, chip place-and-route). Different object world and scale; Cadence's own taxonomy separates "PCB Design & Analysis" from IC design product families. Directory keeps them separate; boundary asserted from directory structure + vendor taxonomy, not from sampling IC-EDA vendors.

### 5. vs CAM (manufacturing) and fabrication-data inspection

Downstream: fabrication outputs generated here are consumed by board houses' CAM processes. Note the terminology trap: in the PCB industry "CAM" also names fab-data preparation/editing tools (Gerber editors, panelization for production); inside design products these appear as auxiliary surfaces (Altium CAM Editor, KiCad GerbView) — inspection of outputs, not design authoring. The directory's CAM leaf (manufacturing context) is a different Type.

### 6. "去掉什么就变成另一个 Type" 判据

- Remove the board/layer stackup → schematic capture (ECAD center)
- Remove nets/connectivity semantics → generic 2D CAD / artwork editing
- Remove footprints/components → copper-cam/Gerber editing
- Remove fabrication outputs → 3D visualization/modeling
- Remove copper (keep schematic + connectivity) → ECAD/EDA electrical pole territory

## Historical / Market-Sample Check

- Would older products fit the four-leg definition? The sampled products themselves evidence the object model's longevity: KiCad's manual describes the older netlist-file workflow it replaced ("In older versions of KiCad, the equivalent process was to export a netlist from the Schematic Editor and import it into the Board Editor"); Altium documents importers from PADS/EAGLE/Expedition/Allegro; EasyEDA imports Eagle/KiCad/Altium. The shared object world (board, footprints, nets, tracks/vias, Gerber-class outputs) predates all four products.
- Direct observation of 1980s-era tools (Protel DOS, Tango, early PADS/Eagle) was NOT performed in this pass; the claim that they exhibit the same four structures is a reasoned inference from the import-lineage evidence above, not a directly observed fact. Kept weak.
- The conceptual ancestor (manual tape-up layout on film: board outline, component placement, taped copper, photoplot artwork) satisfies the conceptual model but is not software — recorded as lineage, not as a sample.
- The definition does not depend on: cloud, 3D, autorouting, SI analysis, push-and-shove routing, Gerber specifically, or schematic integration (netlist import and board-only design are documented alternatives).

## Uncertainties

1. **Cadence evidence is Tier-2 marketing.** Operational behavior of OrCAD X/Allegro X (routing modes, constraint manager mechanics, DRC flow) was not directly observed; claims kept weak and capability-level.
2. **Autorouter prevalence unverified.** EasyEDA documents one; KiCad's manual documents interactive routing only; Altium/OrCAD claims are marketing-level. Treated as variant with mixed evidence.
3. **Back-annotation breadth.** Directly documented only for KiCad (Update Schematic from PCB). Altium/EasyEDA sync direction evidence on fetched pages is forward-dominant. Kept as "common in mature products, documented depth varies".
4. **Layer-count and size limits** are product/version-specific (KiCad 32 copper; EasyEDA 6 default; Altium 128 signal) — recorded as L3 facts, excluded from the final document.
5. **Board-only mode in Altium/OrCAD** not confirmed from fetched pages (KiCad + EasyEDA confirmed). The final document says board-only workflows "exist in some products" rather than claiming universality.
6. **Historical products** not directly sampled (see above).

## Final Synthesis

PCB Design is a real, market-recognized Application Type — the board-design discipline. Its defining core is four jointly-held structures: the board (outline + layer stackup) as the central artifact of record; footprint-based component placement; net-governed copper geometry (tracks/vias/zones realizing a connectivity model, with unrouted connections visible); and fabrication output (manufacturing data for board fabrication and assembly). Schematic capture is the dominant upstream connectivity source and near-universal in integrated suites, but is not definitional — board-only workflows are documented in multiple products. The Type's center of gravity (the board and its physical realization) is distinct from ECAD/EDA's (the schematic and its connectivity semantics), which grounds the keep-both resolution of the delegated joint review. The market realizes the Type across tiers — open-source (KiCad), professional desktop (Altium), web freemium fab-integrated (EasyEDA), enterprise platform (Cadence OrCAD X/Allegro X) — with tier-dependent depth in rules/constraints, analysis, collaboration, and supply-chain/fabrication integration, all of which are variant structure, not definition.
