# Research Notes — Precision Agriculture Platform

Research date: 2026-09-10

## Research Goal

Understand what a **Precision Agriculture Platform** is as an Application Type: what its managed objects are, what the characteristic workflow (the variable-rate execution loop) looks like in real products, who operates it, and — most importantly — where its boundary sits against the neighboring already-processed §20 Types (Agricultural GIS, Crop Remote Sensing Platform, Farm Equipment Telematics, Nutrient Management, Soil Management, Agronomy Management, Irrigation Management, Crop Protection Management, Crop Management, Harvest Management, Farm Management Platform, Agricultural IoT Platform), discharging the joint-review flags hung by the agricultural-gis and crop-remote-sensing passes.

## Initial Boundary

Working hypothesis before research (informed by eight sibling passes that consistently described this leaf as "centers the variable-rate execution loop (prescription → machine → as-applied verification) with equipment data as a first-class citizen"):

- Core use: manage the chain from field-variability data → rate prescription → machine execution → recorded application → verification/analysis, for agricultural inputs (seed, fertilizer, lime, crop protection, water).
- Primary users: commercial row-crop growers and their agronomists/advisors, precision-ag specialists, equipment dealers.
- Nearest neighbors: Agricultural GIS (spatial data base & analysis), Crop Remote Sensing (sensing→decisions), Farm Equipment Telematics (machine connection), Nutrient/Agronomy Management (prescription basis).
- Unknowns: is the as-applied return leg definitional or common? Is "variable-rate" definitional or does flat-rate ride the same loop? Is the prescription object definitional or just one output form? Does the definition over-fit the current OEM/cloud era?

## Research Questions

1. What are the core objects? (field, data layers, zones, prescription/Rx map, rates, as-applied record, yield dataset, work plan)
2. How is a prescription created (zones, equations, manual drawing, templates) and what does it contain?
3. How does the prescription reach the machine (file formats, platform push, work orders, displays)?
4. What returns from the machine (as-applied rates, target-vs-applied attributes, yield) and how is the loop verified?
5. What role does equipment data play vs satellite/soil data?
6. Who uses the platform and from which surfaces (web, mobile, in-cab)?
7. Where are the boundaries vs the twelve neighboring Types above?
8. Historical check: does the loop hold for pre-cloud, pre-OEM-platform, regional forms?

## Representative Products

| Product | Pole | Evidence level reached |
|---|---|---|
| GeoPard | software-only precision-ag analytics + VRA export platform (growers→consultants→co-ops→dealers) | Tier 1 (official docs, extensive) |
| Climate FieldView (Bayer/Climate LLC) | grower-tier data platform: equipment data collection + prescriptions + yield analysis | Tier 2 (solution pages) |
| PTx FarmENGAGE (AGCO/Trimble JV) | OEM-agnostic mixed-fleet precision-ag operations platform | Tier 2 (product page) |
| OneSoil | satellite-first, free-entry platform with VRA task maps (farmers + agri-service partners) | Tier 2 (platform page + FAQ) |

Named context (not directly observed): John Deere Operations Center (market-defining OEM platform; structure asserted only where GeoPard's official integration docs describe it); Case IH FieldOps / Precision Technology (nav-level only); Topcon TAP (Tier-2 evidence via the farm-equipment-telematics pass).

Rejected / unreachable samples (per network rule, abandoned after 2 failures):

- **John Deere Operations Center** — deere.com JS-blocked again on 2026-09-10 (same as 2026-09-08 telematics pass); abandoned after 1 attempt this pass.
- **Precision Planting (Panorama / 20|20)** — precisionplanting.com 403 ×2; the retrofit-hardware pole is therefore under-evidenced.
- **Yara Atfarm** — atfarm.farm transport error ×2; the software-only satellite-VRA pole is under-evidenced (partially covered by the nutrient-management pass's Atfarm sample).
- **xarvio FIELD MANAGER** — 404 ×3 in the 2026-09-07 RS pass; not retried.

## Sources

- GeoPard docs sitemap: https://docs.geopard.tech/geopard-tutorials/sitemap.md (fetched 2026-09-10)
- GeoPard — Evaluate Accuracy of Seeding Application: https://docs.geopard.tech/geopard-tutorials/agronomy/evaluate-accuracy-of-seeding-application.md (fetched 2026-09-10)
- GeoPard — Export VRA Map in ISOXML Format: https://docs.geopard.tech/geopard-tutorials/product-tour-web-app/export-download/export-vra-map-in-isoxml-format.md (fetched 2026-09-10)
- GeoPard — As-Applied/As-Planted Data Import: https://docs.geopard.tech/geopard-tutorials/product-tour-web-app/import-precision-agriculture-data/as-applied-as-planted-data-import.md (fetched 2026-09-10)
- GeoPard agronomy use-case index (titles observed in sitemap): Variable Rate Seeding/Fertilizer Maps; VR Lime from Soil pH; Weed Patches → Herbicide VRA Rx; NUE & Nitrogen Uptake; Yield Report ("validate variable-rate performance"); Field Trial Analytics; Synthetic Yield Map; Yield Calibration & Cleaning (fetched 2026-09-10)
- Climate FieldView — Build Prescriptions: https://climate.com/en-us/solutions/build-prescriptions.html (fetched 2026-09-10); Analyze Data / hardware / adapter-kit pages observed in nav (fetched 2026-09-10)
- PTx FarmENGAGE: https://www.ptxag.com/us/en/products/digital-farming-solutions/farmengage.html (fetched 2026-09-10)
- OneSoil Platform: https://onesoil.ai/en/platform (fetched 2026-09-10)
- Case IH Precision Technology: https://www.caseih.com/en-us/unitedstates/products/precision-technology (fetched 2026-09-10; JS-thin, nav-level only)
- Cross-referenced sibling evidence: research/agricultural-gis.md, research/crop-remote-sensing-platform.md, research/farm-equipment-telematics.md (2026-09-06/07/08)

**Source-access limitations:** John Deere Operations Center remains unobservable (JS-blocked across three passes); Precision Planting and Yara Atfarm unreachable this pass. Claims about OEM platforms and the retrofit-hardware pole are kept weak and anchored in cross-referenced sibling evidence and named context only. GeoPard's numeric file limits (100 MB, 20 attributes, 100-layer batch) are Tier-1 but vendor-specific — recorded here, excluded from the final document.

## Product A — GeoPard

### Key observations (Tier 1 unless noted)

- **Data basis**: Farm → Field hierarchy; boundaries drawn/uploaded/imported (incl. John Deere); layers attach to fields — satellite imagery, yield datasets, soil datasets (shapefile/lab CSV/scanner: EC, moisture, Veris, SoilOptix), as-applied/as-planted data, topography.
- **Prescription machinery**: Zones Maps (multi-layer clustering; user controls weights, indices, zone count, clustering type, minimum polygon area; classification methods incl. AUTO/Natural Breaks/Equal Interval/Equal Count/Spatially Localized; merge/split editing; manual drawing; multi-year stable zones; heterogeneity/relative-variation metrics) + **Rates Distribution Tool** ("Assign seed, fertilizer, lime, or input rates to zones and build machine-ready prescription maps") + equation-based maps (predefined agronomic equation catalog + custom Python functions).
- **Machine delivery**: export zones maps as shapefile; **VRA maps as ISOXML (ISO 11783)** — zip with three variants, "Check your monitor spec to choose the right one"; direct push to John Deere Ops Center as files, **Work Plans** ("Send GeoPard prescription maps to John Deere as Work Plans for execution"), map layers, or application-operation data; batch export.
- **Return leg**: As-Applied/As-Planted import (shapefile WGS84; machinery proprietary formats jdl/cn1/adm/dat; John Deere sync). Documented attribute schema: **ApplRate** (actual applied rate), **CtrlRate** (controller-reported), **TargetRate** (prescription/target rate) — the prescription's rate travels inside the machinery-logged record; per-product-type rate units (l/ha liquid, kg/ha dry, t/ha lime, seeds/ha).
- **Verification leg (the decisive Tier-1 evidence)**: "Evaluate Accuracy of Seeding Application" / "Evaluate Accuracy of Fertilizer Application" — "comparing the prescribed Target rates with the actual Applied rates on a spatial basis", via a Spatial Correlation Analysis equation producing a similarity score 0–1 ("the closer the similarity score is to 1, the more accurately the seeding application was executed"); explicitly covers "VRA or Flat Rate Application". Further: NUE/nitrogen-uptake analysis "from as-applied N and yield/protein data… spot over- and under-application zones and plan next-season nitrogen"; Yield Report "validate variable-rate performance"; Field Trial Analytics (spatial statistics, ROI).
- **Yield pipeline**: import → clean & calibrate (USDA protocol, outliers, striping, multi-combine alignment) → restore gaps (synthetic yield maps) → recommendations → share.
- **Agronomy use cases** (sitemap titles): VR seeding, VR fertilizer, VR lime from soil pH, herbicide ON/OFF Rx from weed detection, VR tillage from compaction, VRA N from PAW/OM.
- Positioning (Tier 2): "All-in-One Precision Agriculture Software… powerhouse analytics platform".

## Product B — Climate FieldView

### Key observations (Tier 2)

- Four solution pillars: Gather Information; Scout Fields; **Build Prescriptions**; Analyze Data.
- **Prescriptions**: "Create tailored prescriptions to optimize seeding rates, fertility and crop protection." Adjustable Scripts; Automated Rates (seed scripts from vendor-claimed "million test plots" — marketing, notes only); Fertility Prescription Tools (N, P, K, lime); Crop Protection Plans (herbicide/fungicide/insecticide); Enhanced Scripts; **Easy Exporting** ("Convert your script into one of the many different file types to upload or send wirelessly").
- **Equipment data first-class**: FieldView Drive 2.0 cab hardware "recording every pass throughout the season"; display adapter kits for CNH and John Deere GreenStar; "upload data seamlessly from flash drives or other systems".
- **Analysis**: "Compare hybrids, inputs or practices on the same map"; yield in color-coded maps/charts; Side-by-Side Maps; Custom Reports (PDF/CSV).
- Sharing with agronomist; 60+ partners claim.

## Product C — PTx FarmENGAGE

### Key observations (Tier 2)

- Positioning: "farm operations management… your entire fleet… regardless of make or model year" (OEM-agnostic).
- **Execution-loop legs**: "Connectivity makes it easier to move data between the office and in-cab displays, track equipment use and job progress live, and **automate the collection and sharing of as-applied records**"; "the ability to **send prescription files** and work order capabilities".
- **Task-setup machinery**: Direct Send (boundaries, guidance lines, implement profiles to device/vehicle — "eliminating the need to manually move data with USB drives"); AutoSync (guidance lines, field names, boundaries, materials, implements, vehicles, operators across connected devices); Work Orders ("instructions for completing in-field tasks… created on the web and then synced to connected… displays… to facilitate remote task setup").
- Editions: **Data** ("take control of their precision ag data across a mixed fleet… simplifies information transfer between the office and in-cab displays, tracks equipment use and job progress, and automates the collection and sharing of as-applied records") / **Operations** (analytics, coordination).
- Third-party compatibility agreements (Raven, John Deere, Case IH, New Holland); App Central on GFX displays; related platforms Precision-IQ displays, OutRun autonomy kit, Panorama (Precision Planting).

## Product D — OneSoil

### Key observations (Tier 2)

- Positioning: "field monitoring, scouting, productivity analysis, variable-rate application maps, soil sampling, field trials… in one connected system"; "Satellite-powered intelligence for modern agriculture".
- Zero-data onboarding (predefined boundaries or draw/upload).
- **Execution loop without OEM hardware**: "Create VRA maps. Build machine-ready maps for seeding, fertilizing, and spraying"; "Estimate savings upfront. See the expected savings before application"; "Connect to your machinery. Send maps to John Deere or export in the right format"; FAQ: "integrates directly with John Deere Operations Center and supports export formats compatible with most modern variable-rate equipment, making it easy to transfer prescription maps and import yield data for analysis."
- Productivity zones (vendor-claimed ">90% correlation to yield map" — marketing, notes only); zone-based soil sampling; field trials (control/treatment strips); batch task-map creation; machinery telemetry overlay; yield import.
- Web (Pro) + Mobile + API; free entry; farmers + agro consultants + machinery dealers + input suppliers.

## Cross-product Comparison

| Loop leg | GeoPard | FieldView | PTx FarmENGAGE | OneSoil |
|---|---|---|---|---|
| Field variability data basis | satellite, yield, soil, as-applied, topography layers | field data + imagery + equipment passes | field data, boundaries, as-applied records | satellite indices, machinery overlay, yield import |
| Prescription as managed artifact | zones maps + rates distribution + equation maps; named exportable objects | scripts (seed/fertility/crop protection) | prescription files sent to displays | VRA/task maps (seeding, fertilizing, spraying) |
| Machine-ready delivery | ISOXML (3 variants), shapefile, JD Work Plans/files | "many different file types… upload or send wirelessly" | Direct Send / Work Orders synced to displays | John Deere push + "right format" export |
| Execution record returning | as-applied import (ApplRate/CtrlRate/TargetRate) | Drive records "every pass" | automated as-applied collection/sharing | yield data import |
| Verification/analysis | Target-vs-Applied spatial similarity (0–1); NUE; yield report "validate variable-rate performance"; trials | side-by-side hybrid/input/practice comparison | Operations-edition analytics | trials with control strips; savings estimates |
| Equipment posture | software-only; rides ISOXML/ADAPT + JD integration | own cab hardware + display adapters | mixed-fleet connectivity + displays | software-only; JD integration + format export |
| Imagery posture | satellite layers as Rx inputs | imagery one pillar beside equipment data | not centered | satellite-first |
| Customer tier | growers→consultants→co-ops→dealers | commercial growers (US-centric) | mixed-fleet operations | farmers + agri-service partners; free entry |

### Stable commonalities (layer B, cross-product)

1. **The execution loop is documented in every sampled product**: variability data → prescription → machine-ready delivery → execution/outcome record → verification/analysis.
2. **The prescription is a named, managed, exportable artifact** — a rate specification bound to field geography (zones or gridded/equation maps).
3. **Machine-consumable delivery is a first-class surface** — ISOXML/ISOBUS, proprietary formats, platform push (John Deere named by 3/4), work orders/task setup.
4. **Execution/outcome data returns** — as-applied rates (with target-vs-applied attributes), pass records, yield; the loop closes in analysis.
5. **Equipment data is a first-class citizen** — every product either collects machinery data, imports it, or automates its flow.
6. **Agronomic inputs covered**: seed, fertilizer (liquid/dry/NH₃), lime, crop protection; extending to tillage (GeoPard VR tillage).
7. **Mixed realization poles**: OEM ecosystems / OEM-agnostic / software-only analytics / grower data platform.

### Product-specific findings (layer A, single-product)

- GeoPard: Target-vs-Applied similarity equation (0–1); synthetic yield maps; equation catalog + custom Python; on-farm trial designs (RCBD etc.); soil-sampling route planning; MCP server for LLM agents; documented as-applied attribute schema.
- FieldView: Drive 2.0 hardware; display adapter kits; seed-script "million test plots" claim; Combyne grain futures.
- PTx FarmENGAGE: Connectivity Center; Direct Send; AutoSync; Work Orders; Data/Operations editions; Farmer Voice Network.
- OneSoil: predefined country-scale boundary library; AgroCopilot AI; Global Analytics data product; savings calculator.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

Three jointly-held structures over one binding:

1. **The field-variability data basis** — identified fields carrying georeferenced agronomic variability data (soil, yield, imagery, prior applications — in some minimal form, even hand-drawn zones) from which application decisions are derived. Remove → equipment control / telematics with no agronomic content.
2. **The prescription as the managed artifact** — a rate specification for an agricultural input, bound to field geography (rates by zone or by location), held as a persistent, editable, exportable object. Remove → a data platform or GIS with no rate output; the prescription basis alone belongs to nutrient/agronomy management.
3. **The machine-execution loop with verification** — the prescription is delivered to equipment in machine-consumable form; the machine's execution and/or outcome is recorded back; the loop closes with evaluation comparing prescription, execution, and agronomic response. Remove → prescription generation without execution (advisory output), or equipment data collection without prescriptions (telematics).

Binding: agricultural inputs (seed, fertilizer, lime, crop protection, and extensions such as tillage and water) applied to fields by machines. Remove the binding → generic spatial tasking.

Jointly-held is load-bearing: (1) alone = ag GIS / remote sensing; (2) alone = a prescription generator (nutrient/agronomy output seam); (3) without (1)+(2) = equipment control; (1)+(2) without (3) = analytics with no execution; (2)+(3) without (1) = rate cards with no variability basis.

### L1 — Common Mature Structure

- Zone machinery: management/productivity zones from single or multi-layer inputs; editable; multi-year stable zones; variability metrics.
- Yield data pipeline: import (ISOXML + proprietary formats) → clean & calibrate → analyze → reuse for prescriptions.
- As-applied data handling: import/sync with target-vs-applied attributes; application-accuracy evaluation.
- Multi-input prescription coverage: seed, fertilizer (N/P/K), lime, crop protection; tillage extension.
- Platform integrations (John Deere Operations Center named by 3/4) and industry data formats (ISOXML, ADAPT framework).
- Comparison/evaluation surfaces: side-by-side maps, trials (strip/RCBD/zone-based), savings estimates, profit maps.
- Soil-sampling planning (grid/zone), scouting support, field diary.
- Web + mobile surfaces; sharing with agronomists/clients; organizations/roles.
- Reports and exports (PDF/CSV, shapefile, GeoTIFF).

### L2 — Variant / Optional Structure

- Equipment posture: OEM-bound ecosystem vs OEM-agnostic mixed-fleet vs software-only riding equipment standards.
- Imagery posture: satellite-first vs imagery-as-one-input vs none.
- Connection substrate: embedded modem, retrofit device, display adapter, file export, platform push, USB manual fallback.
- Packaging: standalone platform vs suite module vs grower data platform spanning sensing+prescriptions+analysis.
- Business model: free tier, per-hectare, subscription, OEM-bundled.
- Customer tier: grower self-service vs consultant/dealer multi-client vs enterprise.
- Region: ISOXML-heavy (Europe) vs proprietary-format-heavy (North America); regional OEM ecosystems.
- AI assistance (era-current): ranked attention lists, weed detection, equation assistants.

### L3 — Vendor-specific (stays out of the final document)

- GeoPard: similarity-equation branding; ZonesMap/RasterMap API objects; USDA yield-cleaning protocol naming; MCP server; specific classification method names; file-size/attribute limits.
- FieldView: Drive 2.0; adapter kits; "million test plots"; Combyne.
- PTx: Connectivity Center, Direct Send, AutoSync, Work Orders, editions, Farmer Voice Network.
- OneSoil: predefined boundary library; AgroCopilot; Global Analytics; ROI claims (3x–28x, >90% correlation — marketing).

## Vendor-specific Findings

See L3. All vendor ROI/yield claims excluded from the final document.

## Boundary Findings

1. **vs Agricultural GIS** (§20, processed 2026-09-06) — **JOINT REVIEW FLAG DISCHARGED: keep-both RATIFIED.** Confirmed from this side: GeoPard, FieldView, OneSoil all implement the full ag-GIS core (land base + layers + map + spatial operations), and the ag-GIS pass's structural tests hold both ways — remove the machine-execution loop and an ag GIS remains (GeoPard-minus-Rx-export would still be a spatial analytics platform); remove the land base/layer model and what remains is equipment control (PTx FarmENGAGE—Data is the near-pole: prescription *transfer* without the agronomic data basis is data logistics). The working distinction is center of gravity: ag GIS centers the spatial data base and analysis (outputs: maps, layers, reports); precision ag centers the rate-prescription-and-machine-execution loop (outputs: prescriptions, verified applications, application-accuracy evaluations) with equipment data as first-class citizen. A gradient, not a wall — GeoPard and FieldView legitimately span both; the sampled products' own agronomy use-case documentation (VR seeding/fertilizer/lime/herbicide Rx workflows) centers the loop.
2. **vs Crop Remote Sensing Platform** (§20, processed 2026-09-07) — **JOINT REVIEW FLAG DISCHARGED: keep-both RATIFIED.** The RS pass held the seam on center of gravity (sensing→indicators→variability→decisions vs equipment-data collection→execution loop) and named FieldView as the embedded pole. Confirmed from this side: FieldView's four pillars span both leaves (imagery/scouting = RS territory; prescriptions + equipment passes + yield analysis = this Type's center); OneSoil similarly spans (satellite monitoring + VRA maps). The RS pass's test holds: remove remote sensing → FieldView-minus-imagery is still a precision-ag data platform; remove equipment telemetry/prescriptions → EOSDA/OneSoil/PIX4Dfields are still crop RS platforms.
3. **vs Farm Equipment Telematics** (§20, processed 2026-09-08): the telematics pass held "precision ag centers on spatial analysis/prescriptions; the telematics layer transfers prescriptions to machines and collects as-applied data back." Confirmed from this side with a sharpened seam: telematics centers the *machine connection* (connected fleet, live telemetry, fleet picture) and treats prescriptions/as-applied as data-transfer content; this Type centers the *rate specification and its verified execution* (what rate, where, why, did it land, what did it yield) and treats the machine connection as delivery plumbing. FarmENGAGE illustrates the gradient: its Data edition is telematics-shaped (transfer/tracking/as-applied automation); its Operations edition drifts toward this Type. Keep-both.
4. **vs Nutrient Management / Agronomy Management / Soil Management / Irrigation Management / Crop Protection Management** (all processed): those Types produce the prescription *basis* (nutrient budgets, agronomic recommendations, soil-data-derived rates, irrigation schedules, protection programs); this Type executes the rate specification through machines and verifies it. The VRA/prescription map is the handoff artifact — each of those passes already recorded "of which a variable-rate map is one output form". Keep-both (ratified from those sides; consistent from this side).
5. **vs Crop Management** (processed): season operation record vs execution loop (that pass's row ratified; consistent).
6. **vs Harvest Management** (processed): machine-executed harvest oversight shares only the campaign/telemetry leg; no credited product inventory here (that pass's row ratified; consistent).
7. **vs Farm Management Platform** (processed): whole-operation records/economics vs execution loop (that pass's row ratified; consistent).
8. **vs Agricultural IoT Platform** (processed): spatial land base + prescription machinery vs point devices + time series (that pass's row ratified; consistent).
9. **Naming observation**: unlike "agricultural GIS", "precision agriculture" IS a recognized market category — OEMs market "Precision Technology"/"precision ag" (Case IH Precision Technology; PTx "Where Precision Meets Possibility"; John Deere precision ag technology), and software products self-describe as "precision agriculture software/platform" (GeoPard, OneSoil). The leaf name matches market vocabulary.
10. **Historical / market-sample check**: the L0 holds for pre-cloud forms — the 1990s–2000s precision-ag pattern (yield monitor → yield map → grid soil samples → agronomist-drawn zones → rate card/prescription file loaded to a VRT controller → as-applied logged by the controller → next-year comparison) satisfies all three legs without cloud, satellites, or OEM platforms; GeoPard's own accuracy-evaluation doc explicitly covers "VRA or Flat Rate Application", showing the loop machinery predates and outlives any single data source. Regional variants (ISOXML-heavy Europe vs proprietary-format North America) fit. The definition does not over-fit the current OEM/cloud era.

## Uncertainties

1. John Deere Operations Center — the market's defining OEM platform — remains unobservable (JS-blocked in two passes). Its structure (boundaries, map layers, work plans, operation data) is asserted only where GeoPard's official integration docs describe it. No operational claims made.
2. The retrofit-hardware pole (Precision Planting 20|20/Panorama) and the software-only satellite-VRA pole (Yara Atfarm) were unreachable this pass; the sample's equipment-posture breadth rests on three poles (software-only, OEM-agnostic, grower-hardware) plus cross-referenced telematics evidence (Topcon, Case IH).
3. Whether every mature precision-ag platform documents application-accuracy evaluation as explicitly as GeoPard: strong Tier-1 evidence in one product; the verification leg is cross-product visible (FieldView side-by-side, OneSoil trials, PTx as-applied automation) but the *explicit target-vs-applied scoring* machinery may be product-specific depth — held as common-mature at moderate strength in the final document.
4. Exact numeric limits (zone counts, file sizes, acreage caps) not researched beyond what fetched pages state; none asserted in the final document.
5. Whether the market would merge this leaf into Agricultural GIS remains a genuine gradient question; resolved here as keep-both on center of gravity, consistent with eight sibling passes' seam language — recorded as a discharged flag, not a unilateral taxonomy change.

## Final Synthesis

A Precision Agriculture Platform is the execution-loop system for field-level crop input management: it holds the field's agronomic variability data, turns it into rate prescriptions bound to field geography, delivers those prescriptions to machines in machine-consumable form, records what the machines actually applied, and closes the loop by verifying execution against prescription and agronomic response. The defining core is the loop itself — data basis + prescription artifact + machine execution with verification — not any single data source (satellite imagery optional), not the machine connection (telematics territory), not the prescription's agronomic reasoning (nutrient/agronomy territory), and not the spatial cartography (ag GIS territory). Mature products add zone machinery, yield pipelines, application-accuracy evaluation, trials, multi-input coverage, platform integrations, and multi-client sharing. The market realizes the Type through OEM precision-ag ecosystems, OEM-agnostic mixed-fleet platforms, software-only analytics/VRA platforms, and grower data platforms spanning sensing and execution.
