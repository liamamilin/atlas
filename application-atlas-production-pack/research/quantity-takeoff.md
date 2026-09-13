# Research Notes — Quantity Takeoff

## Research Goal

Understand what a Quantity Takeoff application really is as an Application Type: what the defining structure is (and is not), how the takeoff loop actually works across products, and where its boundaries lie against Construction Estimating, Preconstruction Management, Project Controls, BIM tooling, and general PDF markup tools.

## Initial Boundary (pre-research hypothesis)

- Quantity takeoff = measuring quantities of construction materials/work from drawings or models. Software category: on-screen takeoff tools (digital blueprint measuring).
- Users: estimators, quantity surveyors, specialty subcontractors.
- Nearest neighbors: Construction Estimating (pricing), Preconstruction Management (pursuit pipeline), BIM authoring/coordination (model data), PDF markup tools (measurement without intent), Construction Materials Management (post-award quantities).
- Likely core: documents as source + on-document measurement + per-item quantity aggregation. Pricing and pursuit machinery expected OUTSIDE the core.
- Sibling passes already recorded seams to ratify:
  - preconstruction-management: "takeoff = contained capability inside precon and estimating — no pursuit record, no solicitation loop, no award; keep separate, ratify at that pass" (takeoff explicitly anti-overfit there: 2D/3D/AI/external-integration/none).
  - project-controls-platform: "takeoff = contained capability inside estimating/precon/controls baselines — no baseline, no loop, no award; keep separate, ratify at that pass".
  - construction-estimating: "The discriminator: take off the pricing and what remains is a takeoff tool; remove the measuring entirely (templates, imports, manual entry) and what remains is still a working estimator."

## Research Questions

1. What is the unit of work? (project/bid containing plan set + takeoff results?)
2. What exactly gets measured, and how is measurement recorded on the document?
3. What is a "Condition" / takeoff item, and is an item catalog definitional?
4. Is scale calibration definitional, or a 2D-variant implementation?
5. How do model-based (BIM) takeoffs differ structurally from 2D drawing takeoffs?
6. Where does takeoff stop and estimating begin?
7. How are drawing revisions, typical/repeating areas, and location segmentation (bid areas/zones) handled?
8. What interfaces exist, and what does the results surface look like?
9. What distinguishes a takeoff tool from a PDF markup tool that also measures?
10. Would paper-era takeoff practice still fit the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Pole | Segment |
|---|---|---|
| On-Screen Takeoff (On Center / ConstructConnect) | classic dedicated takeoff tool (desktop, the Type's namesake), with estimate tab + separate Quick Bid estimating product | specialty subs + GCs |
| STACK (STACK Construction Technologies) | cloud-native takeoff + worksheet estimating bundle, AI takeoff | specialty subs, GCs, suppliers |
| Bluebeam Revu | general PDF markup platform with takeoff capability (capability pole — takeoff as a workflow inside a markup tool) | AEC-wide, estimators among 4M+ users |
| RIB CostX | quantity-surveyor-oriented 2D + 3D/BIM takeoff with live-linked estimating workbooks, BOQ tradition | QS firms, international |
| PlanSwift (ConstructConnect) | desktop takeoff-and-estimate tool, formula-driven, trade starter packs | trades / small GCs — lighter check via official help center chapter structure |

Deliberately not sampled: Autodesk Takeoff (autodesk.com and help.autodesk.com unreachable ×3 — recorded as sourcing limitation), Togal.AI/Beam AI/Bobyard (AI-first entrants; reachable only via competitor comparison pages of others — not enough Tier 1).

## Sources

Research date: 2026-09-09. All observations below are from official vendor surfaces (Tier 1 where noted, Tier 2 product pages otherwise).

- STACK product site: https://www.stackct.com/ (Takeoff/Estimate/Build navigation, AI takeoff framing, trade pages, integrations)
- STACK Help Center (Tier 1): https://support.stackct.com/hc/en-us — Takeoff & Estimate (TE) category: Projects (Plans & Takeoffs / Reports / Estimates), Libraries (items/variables/permissions), project & library permissions
- STACK Plans & Takeoffs section (Tier 1): https://support.stackct.com/hc/en-us/sections/47341814219795-Plans-Takeoffs — Overview/Plans/Takeoffs/Libraries/Audit Trails
- On Center (ConstructConnect) product site: https://www.oncenter.com/ — On-Screen Takeoff + Takeoff Boost + Quick Bid + Digital Production Control suite; takeoff FAQ defining the category; trade pages
- On-Screen Takeoff User Guide (Tier 1): https://help.constructconnect.com/on-screen-takeoff-user-guide-68 — full chapter structure: projects/bids/alternates/change orders; Takeoff Tab; Conditions & Layers; scale; auto count; bid areas & zones; annotations vs takeoff; typical groups/areas/repeating pages; plan organization & overlays; Summary tab; Estimate tab (Unit Cost Worksheet); pricing options; printing; import/export; collaboration; Masters; Databases
- ConstructConnect help center also hosts (Tier 1, chapter structure observed): ConstructConnect Takeoff (Webapp) User Guide (projects & documents; conditions/takeoff/annotations; exporting), PlanSwift User Guide (drawing takeoff & annotations; jobs; formulas; templates; Excel integration), Quick Bid User Guide (items as "building blocks")
- Bluebeam takeoff workflow page (Tier 2): https://www.bluebeam.com/workflows/takeoffs-and-estimation/ — measurement types, scale calibration, Viewports, Dynamic Fill, VisualSearch, Markups List, Legends, Quantity Link, export; FAQ defining quantity takeoff
- Bluebeam Markups & Data page (Tier 2): https://www.bluebeam.com/product/markups-and-data/ — markup data, Markups List, export formats
- Bluebeam Technical Support portal (Tier 1 surface): https://support.bluebeam.com/ — measurement troubleshooting topics ("Measurements don't appear in correct units", "Page turns blue when taking a measurement"), custom markups/Tool Chest
- RIB CostX product page (Tier 2): https://www.rib-software.com/en/rib-costx — 2D & BIM takeoff, Model Maps, auto-revisioning, live-linked workbooks, zones/codes, BOQ, plans comparison (Core/Complete/Quantify: 2D takeoff vs +3D/BIM)

Sourcing limitations: Autodesk (Takeoff product pages/help) unreachable (403/404 ×3) — Autodesk Takeoff therefore not sampled; no claim about it is made below. On Center docs.oncenter.com transport error; replaced by help.constructconnect.com user guide (reachable, Tier 1). STACK/Bluebeam/OST/RIB fine-grained parameter-level details (exact unit lists, per-plan limits, pricing) not exhaustively documented on reachable pages — no precise numeric claims are made anywhere below beyond what sources state.

---

## Product A — On-Screen Takeoff (ConstructConnect / On Center)

Evidence layer: A (direct observation: official FAQ + Tier 1 user-guide chapter structure).

Key observations:

- Vendor defines the category in its own FAQ: "Takeoff software is a digital tool that helps contractors measure quantities directly from construction plans. Instead of printing blueprints and counting by hand, estimators work with digital plans to measure linear footage, square footage, counts, and other job quantities faster and with fewer manual steps."
- Unit of work: Projects ("What are Projects, Bids, Jobs?"), with cover-sheet bid information, Plan Organizer for adding plans, alternates and change orders as project variants, job status filtering on the Projects tab.
- **Conditions** are the takeoff item: user guide chapter "Create a Condition from scratch — General Condition Properties (What are you measuring?)". Conditions can be assigned to Layers. "Patented Multi-Condition takeoff captures multiple trades in one pass."
- Scale is a first-class chapter: "What is Scale and Why is it so Important?", "Setting Page Scale", "Calculating Page Scale Using a Known Linear", "Verifying the Scale of a Plan" — dimensional measurement depends on it.
- Manual takeoff tools + Auto Takeoff and Auto Count; takeoff objects are editable (resizing, adding/removing vertices, splitting linear segments, adjusting angles) — implying quantities recompute.
- **Bid Areas and Zones**: "separate takeoff quantities by rooms, floors, buildings"; takeoff assigned to bid areas; sub-areas nest.
- **Annotations (Plan Markups) vs takeoff are distinct**: dimension lines, text, highlighter, shapes/callouts are annotations with an Image Legend; they do not feed quantities.
- Typical takeoff: Typical Groups, Typical Areas, Repeating Pages — measure a typical condition once, multiply.
- Advanced plan organization: renaming pages, collating, page folders by discipline; overlays (plan version comparison).
- Results surface: "The Summary Tab in Detail (Analyzing Takeoff Results)".
- Estimate surface inside the product: "The Estimate Tab in Detail (Unit Cost Worksheet)" + "Options for Pricing a Bid" — but pricing also lives in the separate Quick Bid product ("connects directly with your estimating tools to eliminate data re-entry").
- Reuse infrastructure: Masters (central saved data), Databases (project storage), Material Database Partners.
- Export/printing: "Printing Plans, Takeoff, and Reports", "Importing and Exporting Bids, Takeoff, and Reports". Free PlanViewer for viewing without authoring.
- AI: Takeoff Boost returns "a head start" (footprint/net area, linears, counts), explicitly positioned as review-and-refine: "reassign takeoff to different Conditions, fine-tune output, include or exclude items"; requires broadband internet (AI is a service).
- Trade coverage named page-by-page (concrete, doors & hardware, electrical, firestopping, flooring, GC, landscaping, masonry, mechanical, paint, plumbing, roofing, walls & ceilings).

## Product B — STACK (STACK Construction Technologies)

Evidence layer: A (official product site + Tier 1 help center).

Key observations:

- Cloud-based platform; two products: Takeoff & Estimate (TE) and Build & Operate (BO) — takeoff/estimate is the preconstruction side; "Quantity & Material Takeoff", "Detailed Estimates & Proposals", "Bid Management" listed as TE pillars.
- Unit of work: Project; help center sections: Projects (Home / Plans & Takeoffs / Reports / Estimates), Calendar, Libraries (items, variables, permissions), Integrations, Troubleshooting. Plans & Takeoffs section: Overview, Plans, Takeoffs, Libraries, Audit Trails — "accurately capture quantities and organize them for estimating".
- Measurement types stated on product site: "Measure linear, area, count, and volume in clicks — with AI auto-counting symbols and suggesting scope you might miss."
- Version handling: "Overlay drawing versions to catch every change"; AI "auto-names pages, and flags revisions".
- Libraries: "Item & Assembly Libraries — extensive, trade-specific catalogs empower material quantification on takeoffs"; import items into a library; library permissions; variables.
- Estimate linkage: "Quantities flow straight into live estimates"; "STACK for Excel" integration; ERP connectors; regional cost data integration (that's estimating-side).
- Collaboration: 100% cloud, "unlimited viewer seats", mark up plans and share estimates from any device; project permissions and library permissions documented.
- Audit Trails documented for plans & takeoffs.
- Serves specialty contractors, GCs, suppliers & manufacturers, owners & developers; trade-specific landing pages (concrete & masonry, drywall, electrical, framing, insulation, mechanical, painting, plumbing, roofing, site work).
- STACK IQ: conversational AI to "build takeoffs, audit estimates and generate proposals" — era-current layer.

## Product C — Bluebeam Revu

Evidence layer: A (official workflow/product pages + support portal surface).

Key observations:

- Bluebeam is a PDF markup platform first; takeoff is one marketed workflow ("Takeoffs" among workflows: drawing & doc management, design review, takeoffs, site logistics, RFIs, submittals, punch, handover).
- Its takeoff page defines the term: "A quantity takeoff is the process of measuring and listing all the materials, parts, and labor needed for a construction project. It's one of the first steps in estimating costs…" and separates takeoff (measure/count/quantify from drawings) from estimating (apply costs).
- Measurement set stated: "length, polylength, perimeter, area, volume, depth, radius, wall area, angle or arc, and count."
- Scale: "Apply scale calibration to ensure measurement accuracy across sheets"; **Viewports** = "multiple scaled viewports in a single drawing" for detail sheets at different scales.
- Measurement markups live in the **Markups List** with author/date/subject; "track all markups… create PDF, CSV or XML reports"; **Legends** = "visual summary of markup data on your PDF, which automatically updates".
- **Dynamic Fill**: "section off and fill complex drawing regions to easily generate markups, measurements and spaces."
- **VisualSearch**: search for symbols within PDFs and "apply custom counts to search results" — automated counting of repeated symbols.
- **Quantity Link**: "sync PDF data with Excel automatically, updating measurements and quantities in real time — no manual entry"; "link measurement totals from multiple PDFs to Excel worksheets".
- Custom columns on markups "to track metadata such as material type and price" — lightweight item identity, not a catalog; export to Excel for estimating.
- Saved tool sets / Profiles standardize takeoff workflows per trade; trade-specific sections (electrical counting fixtures via VisualSearch, plumbing pipe runs, mechanical duct lengths, roofing Dynamic Fill + slope, drywall wall takeoff reuse, concrete volume with depth inputs).
- Studio Sessions: multiple users mark up/measure the same drawings simultaneously.
- Support portal documents measurement-specific troubleshooting (units correctness; page turning blue when measuring) — measurement is a real, fallible surface.
- Structural note: Bluebeam has no item/assembly catalog or estimate worksheet in the takeoff loop — quantities leave via export/Quantity Link. This makes it the capability pole that still satisfies document+measurement+aggregation.

## Product D — RIB CostX

Evidence layer: A (official product page incl. plan comparison and FAQ).

Key observations:

- Positioning: "all-in-one takeoff, estimating, and reporting solution… quantity surveyors and estimators"; 2D + BIM takeoff; sold in tiers where the base tier (Quantify) is 2D takeoff and higher tiers add 3D/BIM + estimating — the vendor itself packages takeoff separable from estimating.
- 2D takeoff: "supports takeoff from a wide range of drawing types including scans, PDF and CAD files… calculating areas, lengths and counts with a single click."
- 3D/BIM takeoff: "accurately estimate quantities and costs based on BIM files… customize data extraction through Model Maps"; FAQ: "BIM takeoff software is a digital solution for measuring and extracting quantities from a BIM model… automatically extract quantities with a high degree of accuracy." Data source and method are named as THE two differences between 2D and BIM takeoff.
- Revisions: "Auto-Revisioning… automatically detect and highlight changes between different versions of a drawing… used to update the estimate, creating a comprehensive audit trail."
- Estimate side: "Workbooks are live-linked to the drawings and their own cost database"; "sort and group items based on codes and zones"; BOQ output; subcontractor quote comparison (free CostX Viewer for subs to submit quotes).
- Carbon (embodied carbon calculations, 6D framing) — adjacent capability riding on the same quantity data.
- Users named: Quantity Surveyor, Estimator, BIM Manager.
- Regional tradition: international QS practice / BOQ; subcontractor comparison "not available in the USA" — regional variant evidence.

## Product E — PlanSwift (lighter check)

Evidence layer: A-lite (official user-guide chapter structure via help.constructconnect.com; not deep-fetched).

Key observations:

- Desktop takeoff-and-estimate tool; guide chapters: "A Detailed Look at the Home Tab and Drawing Takeoff and Annotations", "All About Jobs (aka Projects, Tenders, Bids)", "Writing and Using Formulas", "Templates", "Reports", "PlanSwift Integration to Excel", "Plugins", "Starter Packs (adding Trade or Manufacturer Templates and Items)".
- Confirms the same loop (documents → drawing takeoff & annotations → per-item results → estimate/export) in a formula-driven desktop shape. Trade/manufacturer item packs confirm the catalog-as-optional-extension pattern.

## Cross-product Comparison

| Dimension | On-Screen Takeoff | STACK | Bluebeam Revu | RIB CostX | PlanSwift |
|---|---|---|---|---|---|
| Documents source | 2D plans (Plan Organizer, pages, folders, collating) | 2D plans (upload, auto-naming, AI revision flags) | PDF drawings | 2D scans/PDF/CAD + 3D BIM files | 2D drawings |
| Measurement recording | takeoff objects per Condition, editable | takeoff items measured on sheets | measurement markups in Markups List | takeoff against drawings/models (Model Maps for BIM) | drawing takeoff objects |
| Quantity types | linear, area, count (volume via conditions/Boost) | linear, area, count, volume | length, polylength, perimeter, area, volume, depth, radius, wall area, angle, count | areas, lengths, counts (2D); model-extracted quantities (BIM) | linear/area/count (+formulas) |
| Scale handling | dedicated scale chapters (set/verify/known-linear) | plan scaling (implied by linear/area/volume claims; not deep-verified) | calibration + multi-scale Viewports | 2D scale; BIM geometry carries dimensions | implied by takeoff tools |
| Item identity | Conditions + Layers; Masters | Items & Assemblies libraries (trade catalogs) | markup subjects + custom columns (no catalog) | items grouped by codes/zones; live-linked rate libraries | items + Templates + Starter Packs |
| Aggregation surface | Summary Tab | takeoff results feeding live estimates | Markups List totals + Legends + summaries | workbook/BOQ line items | results → estimate → reports |
| Location segmentation | Bid Areas & Zones (rooms/floors/buildings) | (organization of takeoffs; not deep-verified) | (color-coding/labels; not first-class areas) | zones + codes | (not deep-verified) |
| Repeating structures | Typical Groups/Areas, Repeating Pages | (not deep-verified) | copy/reuse wall takeoffs (trade page) | (not deep-verified) | Templates |
| Revision handling | overlays | version overlay + AI revision flags | measurements update when drawings change | Auto-Revisioning + audit trail | (not deep-verified) |
| Estimate linkage | internal Estimate Tab (Unit Cost Worksheet) + Quick Bid hand-off | quantities flow into live estimates | export / Quantity Link → Excel | live-linked workbooks + rate libraries | Excel integration |
| Collaboration | collaboration chapter; PlanViewer (view-only) | cloud, unlimited viewer seats, permissions | Studio Sessions real-time markup | network licenses, shared projects; Viewer for quote submission | (desktop-centric) |
| AI | Takeoff Boost head start (review-and-refine) | AI auto-count, scope suggestions, STACK IQ | Magic Markups (markup automation, not takeoff-core) | auto-revisioning (detection) | (none observed) |
| Delivery | desktop + web preview | cloud | desktop + cloud/mobile | desktop + cloud offering | desktop |

Convergent findings (evidence layer B unless noted):

1. Every product anchors the work in the project's drawing/model set. (A across all five)
2. Every product records measurement as objects placed on the document (traceable, editable, visible). (A)
3. Every product accumulates measurements into per-item quantity results. (A)
4. Quantity types converge on linear/area/count/volume. (B)
5. Pricing is separable: OST's estimate tab is optional and Quick Bid is a separate product; CostX ships a takeoff-only tier; Bluebeam hands off to Excel. (A — strong)
6. Item catalogs are common but not universal: Bluebeam operates with subjects/custom columns only. (B)
7. Revision comparison is a widespread mature capability. (B)
8. Collaboration on the same takeoff (cloud multi-user or simultaneous markup) is common in current products. (B)
9. AI-assisted measuring exists as an acceleration layer ("head start" + review/refine), uniformly positioned as not replacing estimator judgment. (B, era-current)

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being a Quantity Takeoff application:

1. **The project's construction documents as the dimensional source.** A takeoff project is, first, an organized set of the project's drawings (sheets/pages) or model(s). Quantities are *derived from* the documents, not typed from memory. Remove → a spreadsheet, a material calculator, or an estimating tool without takeoff.
2. **On-document measurement objects.** The act of measuring leaves a visible, selectable, editable object at its location on the document — a count marker, a traced length, a filled area, a volume with depth — so every quantity can be traced back to where and what was measured. Remove → typed quantity lists (estimating territory) or invisible dimension queries (PDF measuring tool territory).
3. **Per-item quantity aggregation.** Measurements accumulate into running quantities organized by identified item/condition — the takeoff results the user is actually producing ("how much of what"). Remove → a markup/dimensioning tool with measurements but no schedule of quantities.

Jointly-held load-bearing checks:

- 1 alone = plan viewer / PDF reader
- 2 alone = general measuring/markup tool
- 3 alone = estimating worksheet or quantity spreadsheet
- 1+2 without 3 = dimensioning doodles (review markup with measurements)
- 1+3 without 2 = a typed quantity list bound to a plan set — that is estimating input entry, not takeoff (the "measured from the document" property is lost)
- 2+3 without 1 = floating quantity arithmetic with no document basis

### L1 — Common Mature Structure

Present in essentially all mature products, but not required to recognize the Type:

- scale calibration of 2D sheets (set/verify, known-distance calibration; multi-scale viewports for detail sheets) — the 2D-variant implementation of "documents carry dimensions"
- item/condition libraries and catalogs, assemblies, saved masters/profiles for reuse
- a full measurement toolset (linear incl. segments/polylength/perimeter, area with cutouts/fill, count incl. search-driven counting, volume with depth/height)
- takeoff results summary per item, with grouping by codes/zones
- location segmentation: bid areas / zones (rooms, floors, buildings)
- typical/repeating areas, groups, repeating pages (measure once, multiply)
- drawing revision handling: overlays/version compare, addenda management, revision-driven quantity updates
- annotations distinct from takeoff (dimension lines, text, highlighter, clouds — don't feed quantities)
- printing of plans + takeoff, quantity reports, export (Excel/CSV/XML) into estimating
- concurrent collaboration on takeoffs (cloud multi-user, shared sessions) with project/library permissions

### L2 — Variant / Optional Structure

- document substrate: 2D PDF/scanned/CAD drawings vs 3D BIM models (geometry-driven extraction via model mapping)
- delivery: desktop licensed vs cloud; webapp companions; free viewers
- packaging: standalone takeoff; takeoff+estimating bundle; takeoff module inside a preconstruction/estimating platform; takeoff capability inside a general markup platform
- AI-assisted auto takeoff (auto-count, auto-area, scope suggestions) as a review-and-refine head start — era-current
- trade-specific toolsets, catalogs and starter packs; trade landing pages
- regional tradition: US subcontractor bid culture vs international QS/BOQ practice (zone/code structures, BOQ output)
- adjacent capabilities riding the same quantity data: embodied carbon, subcontractor quote comparison, bid management, field production control

### L3 — Vendor-specific Structure (research notes only)

- Takeoff Boost (On Center): AI first-pass takeoff, web preview, % speed claims, trade-specific detection updates
- Quantity Link, Dynamic Fill, VisualSearch, Viewports, Legends, Profiles (Bluebeam feature names)
- Model Maps, Auto-Revisioning, CostXL, CostX Viewer, EC3 carbon library integration (CostX)
- STACK IQ conversational AI, STACK for Excel/Velixo, unlimited viewer seats (STACK)
- Multi-Condition takeoff (patented), Digital Production Control, Free PlanViewer, Material Database Partners (On Center)
- PlanSwift formulas/plugins/starter packs ecosystem

## Rejected Findings (considered and rejected for the core)

- **Scale calibration as L0**: rejected — counts need no scale, and BIM takeoff takes dimensions from model geometry; calibration is the standard 2D implementation (L1).
- **Item/assembly catalogs as L0**: rejected — the capability pole (Bluebeam) accumulates per-item quantities with subjects/custom columns and no catalog; catalogs are the mature implementation of item identity.
- **Pricing/costing in the core**: rejected — vendors themselves split it (CostX takeoff-only tier; OST + separate Quick Bid; Bluebeam → Excel). Consistent with construction-estimating pass.
- **Bid pursuit/solicitation machinery in the core**: rejected — absent from all sampled takeoff products; precon pass already recorded the seam.
- **AI takeoff as definitional**: rejected — era-current layer on all sampled products, always positioned as head-start + review.
- **"Estimating worksheet inside the product" as definitional**: rejected — the purest takeoff products export instead (Bluebeam, OST→Quick Bid).
- **Model-based (BIM) takeoff as a separate Type**: rejected — same loop, different document substrate (L2 variant). CostX explicitly sells 2D and BIM takeoff as one capability continuum; its own FAQ names data source and method as the only differences.

## Boundary Findings

- **vs Construction Estimating** (RATIFIED from this side; sibling pass recorded the other side): the seam is pricing. Takeoff produces quantities; estimating attaches rates and produces money. Both directions verified: OST/Bluebeam measure quantities with no rate machinery in the loop (still takeoff); Clear Estimates (sibling sample) estimates with no takeoff (still estimating). Strip pricing from a bundle → takeoff remains; strip measuring → estimator remains.
- **vs Preconstruction Management** (RATIFIED from this side; forward note from that pass): no pursuit record, no bid-date pipeline, no subcontractor solicitation/leveling, no award resolution in any sampled takeoff product. Takeoff is a workstream the pursuit consumes.
- **vs Project Controls** (RATIFIED from this side; forward note from that pass): no cost/schedule baseline, no measure→variance→forecast loop. Takeoff feeds the budget's quantity basis before award; it is not a control surface after it.
- **vs PDF markup / review tools**: a markup tool used for design review with occasional dimension queries stays outside this Type. The takeoff loop begins when measurements are systematically accumulated per item as the deliverable (the Markups-List-as-quantity-takeoff pattern). Bluebeam legitimately straddles: it is a markup platform whose takeoff workflow satisfies this Type's core when used that way.
- **vs BIM Authoring / BIM Coordination**: authoring creates model geometry; coordination manages model information exchange. Model-based takeoff *consumes* model data for quantities (via mapping) and does not author or coordinate. (BIM coordination pass already recorded "information takeoffs" as optional there.)
- **vs Construction Materials Management** (consistent with that pass's record): takeoff produces required quantities before award; materials management consumes them and tracks actuals after award.
- **vs Design applications (architecture/civil/MEP)**: those passes recorded takeoff as "downstream consumer" — volume/quantity reporting there is a byproduct of authoring, not the center of gravity. Consistent.

## Historical / Market-Sample Check (§24)

Paper-era takeoff practice: printed blueprints + scale rule + highlighter/pencil + takeoff sheets. Documents as source ✓; measurement recorded on the document (highlighted regions, tally marks beside symbols) ✓; per-item aggregation in takeoff sheets ✓. On-screen takeoff digitizes exactly this loop (OST's own FAQ: "Instead of printing blueprints and counting by hand…"). Regional, older, or platform-native implementations (desktop licensed PlanSwift, single-user OST databases, paper practice) satisfy the core without cloud, AI, BIM, or catalogs. The definition does not overfit to the current AI/cloud moment. ✓ Passed.

## Uncertainties

- Exact measurement-type lists vary by product and page; only product-stated lists were recorded (no cross-vendor normalization invented).
- STACK's scale-calibration surface was not deep-verified at article level (Tier 1 section titles + product claims only); scale handling for STACK rests on its linear/area/volume measurement claims.
- PlanSwift observations rest on chapter structure, not article content.
- Autodesk Takeoff not sampled (unreachable ×3) — model-based pole rests on CostX's BIM takeoff; if Autodesk help becomes reachable, re-verify the BIM-pole variant list.
- Whether count-only takeoff products (no dimensional measurement at all) exist as a category — none sampled; counts appear alongside dimensional measurement in all samples. L0 phrased so counts fit without requiring scale.
- Bluebeam's takeoff framing is partly marketing ("purpose-built for construction") — the structural judgment (markup platform with takeoff capability) rests on the presence/absence of catalog and estimate machinery, which is directly observed.

## Final Synthesis

A Quantity Takeoff application is the document-measurement system of preconstruction: it organizes a project's drawings (or models), lets the estimator measure the work directly on them — counts, lengths, areas, volumes — as traceable, editable on-document objects attached to identified items, and accumulates those measurements into a per-item schedule of quantities that downstream estimating prices. Scale calibration, item catalogs, zones, typicals, revision comparison, collaboration, AI head starts, and even the estimate worksheet are mature accretions around that loop; pricing, pursuit machinery, and post-award control belong to neighboring Types. The Type's identity survived every packaging shift the market threw at it: desktop → cloud, 2D → BIM, manual → AI, standalone → bundled, markup platform → takeoff workflow — because the core loop (measure on the document, aggregate per item) is what all of them sell.
