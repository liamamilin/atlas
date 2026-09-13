# Research Notes — Nutrient Management

## Research Goal

Understand what a Nutrient Management application actually is, from real products: what its core objects are, what work flows through it, how it differs from the neighboring agriculture Types (Soil Management, Agronomy Management, Crop Management, Feed Management, Precision Agriculture), and whether the directory leaf is a genuine Type.

## Initial Boundary

Initial hypothesis: Nutrient Management centers the management of plant nutrients (fertilizer, manure, organic materials) as inputs to crop production — budgeting supply against crop demand, planning applications, and satisfying environmental/regulatory constraints. Likely confusions:

- Soil Management (processed 2026-09-09) — flagged Nutrient Management as its closest boundary: "both read the same soil test, but one manages the soil resource (its state and improvement) while the other manages nutrient inputs (their budgeting, application, and regulation)."
- Agronomy Management — fertility recommendations are one domain inside the agronomy practice.
- Feed Management — "nutrient" there means nutrients in animal rations; manure is feed management's output and nutrient management's input.
- Precision Agriculture Platform — variable-rate nutrient application is one execution form.
- Fertilizer recommendation calculators — a thinner, single-source artifact.

## Research Questions

1. What is the unit of record — the field, the farm, the plan, the application?
2. What does "budgeting" concretely mean: which sources are credited, against what demand?
3. Is regulation (NRCS 590, CAFO, NVZ, regional councils) definitional or a variant?
4. Is manure machinery (storage, allocation, exports) definitional, or does a fertilizer-only plan still belong?
5. What is planned vs recorded: do products track actual applications?
6. Where does the environmental dimension (nutrient loss risk) sit — core or common?
7. How do products relate to soil tests, agronomy recommendations, and VRA maps?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, different geographies and customer tiers:

1. **Purdue MMP — Manure Management Planner** (US; free desktop tool, national NRCS/EPA-supported software for CNMP development; the regulatory planning pole; extensive Tier-1 help file)
2. **OverseerFM** (New Zealand; whole-farm nutrient budgeting model owned by MPI/AgResearch/Fertiliser Association; Tier-1 knowledge base)
3. **PLANET / MANNER-NPK / NMPT-GB** (UK; Defra/ADAS free national nutrient management planning tools, RB209-based, NVZ compliance; Tier-1 product site + Defra blog)
4. **Yara Atfarm (+ N-Tester / N-Sensor)** (global commercial; crop-sensing nitrogen advisory and variable-rate maps; Tier-1 help center)

Pole coverage: regulatory multi-year manure-centric planning (MMP) / whole-farm nutrient-flow modeling (Overseer) / government field-level planning + compliance (NMPT) / commercial within-season nitrogen advisory (Atfarm). Historical/era check: MMP itself descends from paper manure-management plans (Purdue Extension publications describe the pre-software plan); fertilizer-only NMP document templates exist inside MMP.

## Sources

- Purdue MMP — Help file: https://www.agry.purdue.edu/mmp/mmphelp.html (fetched 2026-09-10)
- Purdue MMP — program page: https://ag.purdue.edu/department/agry/research/manure-management-planner.html
- MyFarms Purdue MMP page: https://www.purduemmp.myfarms.com/
- USDA NRCS MMP fact sheet: https://www.wcc.nrcs.usda.gov/ftpref/wntsc/nutrientMgt/MMP.pdf
- EPA CAFO guidance Section 6 (MMP walkthrough): https://www.epa.gov/sites/default/files/2015-08/documents/cafo_manure_guidance_section6.pdf
- Purdue Extension ID-208-W (dairy MMP): https://www.extension.purdue.edu/extmedia/ID/ID-208-W.html
- NRCS Conservation Practice Standard 590 (multiple state editions, 2006–2022): nrcs.usda.gov (NHCP 2019, Ohio 2012/2020, NY 2020, Delaware 2013, NC 2014, Missouri 2022)
- OverseerFM — product page: http://overseer.org.nz/overseerfm ; factsheet PDF
- Overseer Knowledge base — Overview of OverseerFM: https://support.overseer.org.nz/hc/en-us/articles/41985486824089 ; What information does OverseerFM give me: https://support.overseer.org.nz/hc/en-us/articles/205576977 (fetched 2026-09-10)
- NZ MPI — Overseer page: https://www.mpi.govt.nz/agriculture/farm-management-the-environment-and-land-use/overseer-a-nutrient-management-tool-for-farmers-and-growers ; Beca appendix on OVERSEER (2018)
- ADAS — Planet and MANNER-NPK: https://adas.co.uk/projects/planet-and-manner-npk/ ; Nutrient Management Planning service page
- planet4farmers.adas.co.uk (PLANET/MANNER-NPK/ENCASH product site, 2026 NMPT-GB update)
- Defra blog — Introducing the new nutrient management planning tool (NMPT-GB), Feb 2026: https://defrafarming.blog.gov.uk/2026/02/04/introducing-the-new-nutrient-management-planning-tool-on-gov-uk
- NMPT-GB beta site: https://nmp-dev1.azure.defra.cloud/
- AHDB — MANNER-NPK project page: https://ahdb.org.uk/manner-npk
- Yara Atfarm support — N-Tester articles: https://support.at.farm/hc/en-gb/articles/4410320887442 (fetched via search capture)
- Yara N-Sensor pages (UK/India/US) and N-Sensor PDF
- Minnesota PCA MMP spreadsheet user guide (state variant of nutrient management planning): https://www.pca.state.mn.us/sites/default/files/wq-f6-12b.pdf

## Product A — Purdue MMP (Manure Management Planner)

Evidence layer: A (direct observation of official help file, USDA fact sheet, EPA guidance).

### Key observations

- **Positioning**: free Windows desktop software, nationally supported by USDA-NRCS and US EPA for nutrient management planning and CNMP (Comprehensive Nutrient Management Plan) development; the official planning software in several state 590 standards. Now maintained with MyFarms (v4, 2024–2026 releases).
- **Unit of record: the plan file** (.mmp) for one operation, covering a multi-year horizon (help FAQ: plan length should cover the longest crop rotation; 1–10 years supported; monthly planning grid).
- **Data panels** (from help contents): General, Fields, Assessment, Soil Tests, Crops, Storage, Animals, Rations, Analysis, Equipment, Nutrient Mgmt. The plan assembles the operation's fields (with soils from county soil surveys, subfields), soil test results, crops and rotations with yield goals, manure storages, animals, manure analyses (lab or book values), and application equipment.
- **Multi-source crediting**: LGU (land-grant university) fertilizer recommendations computed automatically per state; manure nutrient availability from state-specific N availability factors; residual N credits from previous years' manure; legume N credits from rotation; planned commercial fertilizer and irrigation-water nitrates entered on the Nutrient Mgmt panel; starter fertilizer included in the budget.
- **The allocation act**: the planner allocates manure to fields (where, when, how much) on a monthly grid over the plan period; a Manure Application Rate Calculator computes rates; the Field Status grid flags months where no more manure is needed (red cells); Storage Status grid handles imports/exports of manure between operations.
- **Sufficiency assessment**: MMP "helps determine if the operation has enough storage, equipment, and spreadable acres to handle the manure produced" — the plan tests the operation's capacity, not just the field's need (EPA guidance).
- **Environmental risk machinery**: Assessment panel collects data for phosphorus indexes and other state risk tools; RUSLE2 erosion built in; National Setbacks database determines "spreadable acreage"; state P-Index custom tools.
- **Outputs**: built-in reports, planning calendars, nutrient balance and nutrient status reports, projected soil P/K levels, CNMP and plan documents generated from national/state templates; Manure Application Recordkeeping Tool (MART) records actual applications; EPA CAFO recordkeeping items supported.
- **Explicit self-description**: "MMP itself is not a recordkeeping program in the usual sense… MMP is a planning program." Recordkeeping is a companion tool.
- **Overrides**: custom fertilizer recs and measured manure analyses override defaults, with source documentation required — the plan is an accountable document.

## Product B — OverseerFM

Evidence layer: A (official knowledge base, product page, factsheet, MPI government page).

### Key observations

- **Positioning**: NZ online service (since 2018; desktop Overseer since early 2000s, model since 1990s) that models nutrient flows and GHG emissions for a farm system; owned by MPI, AgResearch and the Fertiliser Association; used in NZ environmental regulation contexts (regional councils).
- **Unit of record: the farm account** — "one account per farm," centrally stored, shared with permission between farmer and professionals (advisers, regional councils). Farm analysis built from location, management blocks, climate/soil auto-pulled, animals, fertiliser, crops, effluent.
- **Core output: the nutrient budget** — "calculates nutrient budgets for N, P, K, S, Ca, Mg and Na at farm and block level. A nutrient budget is a table of inputs and outputs for a nutrient, for a particular physical identity." Inputs include fertiliser, feed, supplements, effluent, irrigation water; outputs include produce, transfers, and losses (N leaching at root zone, P surface run-off).
- **Model-based, not rule-based**: a scientific model estimates flows; "decision support tool, not a decision-making tool"; long-term equilibrium model; scenario tool to compare management changes while keeping the farm system in equilibrium; farm impact report compares base year vs proposed changes.
- **Recommendations**: maintenance nutrient and lime requirements; N surplus and nitrogen conversion efficiency; benchmarking against other NZ farms; aggregated group reporting.
- **Adviser ecosystem**: certified nutrient management advisers programme (industry certification); the adviser, not only the farmer, operates the tool.
- **GHG extension**: methane, nitrous oxide, CO2, carbon sequestration — same model, additional outputs.

## Product C — PLANET / MANNER-NPK / NMPT-GB (UK)

Evidence layer: A (ADAS project pages, planet4farmers site, NMPT-GB beta site, Defra blog, AHDB project page).

### Key observations

- **Family of free national tools**: PLANET (field-level nutrient planning + NVZ compliance, England/Wales/Scotland), MANNER-NPK (quick estimate of crop-available N, P2O5, K2O supply from organic manure applications), ENCASH; replaced in 2025–2026 by Defra's web-based **NMPT-GB** ("Plan and Manage Nutrient Applications Tool"), which embeds the MANNER-NPK model.
- **Recommendation engine: RB209** (AHDB Nutrient Management Guide) — fertiliser recommendations for all major nutrients and lime for most crops, computed from the farm's own data: soil analysis, soil type, expected yields, previous crops, rainfall/altitude (auto-pulled from postcode in NMPT-GB).
- **Unit of record: the farm file with fields** — set up farm and fields, enter soil type and soil analysis; plan developed per season; "detailed records of cropping, soil analyses, and each fertiliser and manure application"; downloadable PDF plans; year-on-year plan building.
- **Organic materials as first-class sources**: manure types with standard values or user-entered analyses (saved for reuse); MANNER-NPK estimates crop-available supply and financial value (£/ha) of manure applications; digestate, biosolids, compost covered.
- **Compliance machinery**: NVZ confirmation inside the tool; "correct compliance reports"; NVZ rules require detailed nutrient application records; manure management plans confirm sufficient safe spreading area; spreading risk maps (ADAS service).
- **No legal requirement to use it** — the tool is guidance; compliance is the farmer's obligation, the tool supports demonstrating it.
- **Adviser-facing**: used by FACTS-qualified consultants to produce NMPs for farms; reports shareable with advisers, tenants, compliance audiences.

## Product D — Yara Atfarm (+ N-Tester, N-Sensor)

Evidence layer: A (official support help center, product pages).

### Key observations

- **Positioning**: free online service for crop nitrogen management; field-level N-rate recommendations from crop sensing; commercial fertilizer vendor's agronomy tooling.
- **Unit of record: the field** within a farm; field boundaries loaded; satellite biomass imagery; N-Tester BT handheld chlorophyll measurements synced via Bluetooth to the app.
- **Recommendation basis**: crop's actual N-uptake (chlorophyll/spectral measurement) + user-entered field info (expected yield, N already applied, last application) → N recommendation in kg/ha; used for 2nd/3rd/protein dressings; N-Photo Analysis for first application; Variable N-Rate Application maps generated from recommendations.
- **Within-season loop**: repeated measurement of N supply status per field during the season; recommendations at application time (N-Sensor: real-time VRA at the spreader); documented measurements tracked over time.
- **Constraint awareness is partial**: "We don't currently take fertiliser restrictions into account for the N-Tester Recommendations" — the user must respect government maximums themselves. Environmental benefit framed as outcome (reduce nitrate leaching, avoid lodging), not enforced.
- **Single-nutrient focus**: nitrogen (with some P/K in broader tools); no manure, no whole-farm budget, no multi-year plan.

## Cross-product Comparison

| Dimension | MMP (US) | OverseerFM (NZ) | PLANET/NMPT (UK) | Atfarm (global) |
|---|---|---|---|---|
| Unit of record | plan file for the operation, multi-year monthly grid | farm account, blocks | farm file with fields, seasonal plan | field within a farm |
| Demand side | crop nutrient requirements from LGU recs + yield goals, per rotation | modeled farm system (pasture/animal intake, crops) | crop nutrient requirements from RB209 | crop N need from crop sensing + user inputs |
| Supply sources credited | soil test, manure (lab/book), legume + residual N credits, starter fertilizer, irrigation nitrates | fertiliser, feed, supplements, effluent, irrigation, fixation (modeled) | soil analysis/soil N supply, organic materials (MANNER-NPK), fertiliser | N already applied, soil/crop status |
| Central artifact | nutrient plan + manure allocation across fields/months | nutrient budget (inputs vs outputs per nutrient) | nutrient application plan + records | N recommendation / VRA map |
| 4R specification (rate/source/placement/timing) | yes — rate calculator, method, timing, incorporation days | partially — fertiliser inputs modeled; placement less central | yes — RB209 rate/source/timing; application records | rate + timing; placement via VRA map |
| Environmental risk machinery | P-index tools, RUSLE2, setbacks, spreadable acreage | N leaching + P runoff modeled as core output | NVZ compliance reports, spreading risk | advisory framing only; restrictions not enforced |
| Application records | companion recordkeeping tool (MART) | not the focus (model inputs) | first-class: records each application | measurements tracked; applications user-entered |
| Multi-year horizon | 1–10 years, monthly | annual equilibrium + scenarios | seasonal, year-on-year plans | within-season |
| Regulation bindingness | plan must satisfy state 590; official software | used for regional council reporting | compliance reports produced; no legal requirement to use tool | explicitly not enforced |
| Business model | free (public-good) | subscription (public-interest owner) | free (government) | free tool from fertilizer vendor |

## Canonical Model (draft)

The Type's center is the **nutrient plan/budget for land units**: an accounting that matches crop nutrient demand against nutrient supply from all available sources, and expresses the result as planned applications (rate, source, placement, timing).

- **L0 — Defining Invariant** (jointly held; remove any one and the product stops being nutrient management):
  1. **The nutrient plan/budget as unit of record** — a persistent, revisable plan per land unit (field/block/farm) that budgets plant nutrients for a crop sequence: demand (crop requirement) vs supply (all sources).
  2. **Multi-source supply accounting** — supply is assembled and credited from multiple sources (soil/soil test supply, organic materials incl. manure, commercial fertilizer, legume/residual credits, irrigation water) before deciding what still must be applied; the plan decides each source's contribution.
  3. **Planned applications as the plan's output** — per land unit, applications specified by rate, source, placement/method, and timing (the 4R specification), possibly scheduled across a rotation; the plan is revisable and re-derivable as inputs change.

  Jointly-held load-bearing: (1) alone = a crop removal table; (2) without (1) = a manure analysis calculator; (3) without (1)+(2) = a fertilizer shopping list; (1)+(3) without (2) = a single-source fertilizer recommendation tool (a thinner artifact, arguably not "nutrient management" as the market names it).

- **L1 — Common Mature Structure**: soil test integration; manure/organic-material machinery (analyses, availability estimates, allocation, storage, imports/exports, spreading-area sufficiency); application records (planned vs actual); environmental loss-risk assessment bounding applications (P-index, N leaching, NVZ, setbacks); plan documents for regulators/certification; multi-year rotation planning; economic valuation of nutrient sources; adviser/multi-client operation.
- **L2 — Variant / Optional**: regulatory regime bindingness (mandatory plan formats vs guidance-only); modeling depth (rule-based calculators vs scientific flow models vs crop-sensing advisories); whole-farm vs field scope; GHG/carbon extensions; VRA map generation; benchmarking; scenario simulation.
- **L3 — Vendor-specific**: MMP's state-specific recommendation databases and CNMP document templates; Overseer's NZ regional-council use and national benchmarking; NMPT's NVZ compliance reports and RB209; Atfarm's N-Tester hardware integration and Yara calibrations.

### Historical / market-sample check (§24 reasoning)

- Would older products fit? The pre-software manure management plan (Purdue Extension paper-era: fields, crops, manure production, application plan) satisfies the core with no software. Fertilizer-only NMPs (MMP ships a national fertilizer-only NMP template) satisfy the core without manure. Desktop-era PLANET/MANNER satisfy it without cloud or maps.
- Would regional products fit? NZ (Overseer), UK (PLANET), US (MMP) all fit; the regulatory regimes differ but the budget-plan-record structure is the same.
- Anti-overfit: manure is NOT definitional (fertilizer-only plans in-type); regulation is NOT definitional (advisory pole in-type; NMPT explicitly "no legal requirement"); scientific modeling is NOT definitional (MMP is rule-based); multi-year horizon NOT definitional (Atfarm is within-season); whole-farm scope NOT definitional (field-scope poles in-type).

## Vendor-specific Findings

- MMP: state initialization files, per-state fertilizer rec sources, P-Index custom tools per state, CNMP document templates (national + state), MART recordkeeping, RUSLE2 integration, Missouri Clipper/SNMP GIS import, sample plan files.
- OverseerFM: NZ-specific farm systems, regional council engagement, national benchmarking, certified-adviser programme, GHG/carbon sequestration reports, RSU (revised stock units).
- NMPT-GB: RB209 engine, NVZ confirmation and compliance reports, postcode-pulled rainfall/altitude, PLANET data import migration, MANNER-NPK embedded.
- Atfarm: N-Tester BT hardware, chlorophyll calibrations per crop/region, N-Sensor real-time VRA, satellite biomass, Yara annual field trials.

## Boundary Findings

- **vs Soil Management**: soil management centers the soil resource itself — the measured soil state, the sampling/measurement cycle, and soil-improving decisions (lime, amendments, structure). Nutrient management consumes the soil test as one input into the nutrient budget and centers the nutrient inputs (what goes on, at what rate, from which source, when). The soil test is the shared artifact; the decision object differs. Lime sits at the seam: soil products decide lime from pH; RB209-based nutrient planning also carries lime recommendations. Recorded as a seam for joint review.
- **vs Agronomy Management**: agronomy is the multi-domain recommendation practice (seed + nutrients + protection) on the field record; nutrient management is the nutrient domain's own accounting discipline — the budget across sources and the plan's sufficiency/capacity questions (enough acres? storage? spreadable acres?) are not agronomy's center. Fertility recommendations are the shared seam; agronomy-suite fertility modules are the packaging overlap.
- **vs Feed Management**: feed management manages nutrients INTO animals (rations against nutrient targets); nutrient management manages nutrients ONTO land (manure as a nutrient source). The manure stream is feed's output and nutrient management's input; a livestock operation may use both.
- **vs Precision Agriculture Platform**: precision ag centers the variable-rate execution loop (prescription → machine → as-applied); nutrient management produces the prescription basis (the plan/budget) and may output VRA maps as one form.
- **vs Fertilizer recommendation calculators**: a single-source recommendation without the multi-source budget and plan of record is a capability, not this Type.
- **vs Environmental compliance / water quality (§21)**: nutrient loss to water is the environmental stake that shapes the plan, but the subject of record is the farm's nutrient inputs, not environmental monitoring or permitting. Overseer's loss modeling is the deepest extension toward §21; the center stays the farm nutrient budget.
- **vs Crop Management**: nutrient applications are one operation class in the crop cycle; crop management integrates all operation classes; nutrient management owns the nutrient accounting in depth.
- **Decisive "remove" test**: remove the multi-source budget and keep only application records → farm record-keeping. Remove the plan and keep only loss modeling → environmental modeling. Remove the land-unit binding and keep only nutrient math → a calculator.

## Uncertainties

- EU (beyond UK) and other regional products (e.g., continental-EU fertilizer planning tools, Canadian provincial tools) were not deeply sampled; the UK/NZ/US poles may over-represent English-language regulatory regimes. The core was checked against a fertilizer-only and an advisory pole to mitigate.
- Commercial ag-retail nutrient/fertility modules (covered by the agronomy-management pass) were not re-researched; their relationship is recorded via the agronomy boundary.
- The exact placement of lime (soil management vs nutrient management) is a genuine seam; both sides carry lime machinery in the sampled products.
- Whether "application records" should be L0 was considered and rejected (MMP explicitly separates planning from recordkeeping; Overseer does not record applications as its focus) — but the planned-vs-actual loop is near-universal in mature planning products and is recorded as L1.
- Atfarm's broader nutrient coverage beyond N (P/K tools) was not deeply verified; the pole is treated as nitrogen-advisory.

## Final Synthesis

A Nutrient Management application is the farm's nutrient-accounting system of record: it holds a nutrient plan/budget for the operation's land units, assembles nutrient supply from all available sources (soil supply, organic materials including manure, commercial fertilizer, credits), matches it against crop nutrient demand, and expresses the result as planned applications — rate, source, placement, timing — commonly bounded by environmental loss-risk constraints and recorded against actual applications. Mature products add soil-test integration, manure/organic-material machinery, compliance documents, multi-year rotation planning, VRA outputs, and adviser operation; regulation, manure-centrality, scientific modeling, and whole-farm scope are all variant axes, not the definition.
