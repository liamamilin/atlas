# Research Notes — Soil Management

Research date: 2026-09-09
Leaf: Soil Management (DIRECTORY.md §20 Agriculture, Food & Natural Resources)
Slug: soil-management

## Research Goal

Understand what software called "soil management" actually is in the market: what the managed subject is (the soil resource? the soil test? the sampling operation?), what objects and records such products hold, how soil data is produced and refreshed, what decisions are made from it, who operates these products, and where the boundary sits against the neighboring §20 Types — especially the three pre-hung joint-review flags:

1. **agronomy-management** (processed 2026-09-06): "vs Nutrient Management / Crop Protection Management / Soil Management … these appear to be single-domain leaves (one input class as the center). Agronomy management is the multi-domain integration at field level… Risk: superset/capability relationship (each domain leaf may exist as a module inside agronomy suites)."
2. **field-management** (processed 2026-09-08): "vs Soil Management (§20, unprocessed) — soil as the managed subject (tests, amendments, programs) vs the field as subject with soil as one characterization. Soil-test records attach to fields in sampled products (farmOS lab-test logs; OneSoil soil uploads)."
3. **irrigation-management** (processed 2026-09-08): "New flags for unprocessed siblings: vs nutrient-management and soil-management (same single-domain pattern expected — joint review when those leaves are processed)."

Plus the forward obligation to leave a flag for **nutrient-management** (still unprocessed at this pass's date).

## Initial Boundary (working hypothesis before research)

- "Soil management" in an agricultural software context = managing the soil resource of a farming operation: knowing its measured state (fertility/chemistry — pH, nutrients, organic matter; sometimes physical/biological condition) and acting on it (lime/amendments, fertility programmes, soil-health practices).
- The soil test result is likely the central artifact; the sampling/testing loop is likely the distinctive operational machinery of this domain (no other input domain runs "sampling campaigns" as a first-class managed workflow).
- Nearest neighbors: Nutrient Management (unprocessed sibling — the fertility seam), Agronomy Management (the multi-domain integrator), Field Management (the land asset with soil as one attribute), Irrigation Management (soil moisture as its substrate), Precision Agriculture Platform (VRA execution), Agricultural IoT Platform (in-ground sensor fleets), Carbon Accounting / soil-carbon MRV (§21), Laboratory LIMS (the lab side).
- Unknowns: Is there a standalone "soil management" product category, or only modules inside agronomy/ERP suites? Is the sampling campaign machinery definitional or just the dominant implementation? Where does soil health (biology/structure) sit vs soil fertility (chemistry)? Does soil carbon drag the leaf into §21?

## Research Questions

1. What is the managed subject — the soil of a land unit, the sample, the test result, the amendment?
2. How is soil data produced (lab sampling, in-field tests, sensors, satellite inference) and matched back to locations?
3. What does the soil record look like (per field/zone/point, per depth, per round; which properties)?
4. What decisions/actions does the product support (lime, fertilizer, amendments, cover crops, tillage, conservation practices)? Are applications recorded?
5. Is change-over-time tracking (multi-year trends, re-measurement cycles) universal?
6. Who operates (agri-service/sampling contractors, advisors, growers, ERP tenants) and how is delivery organized (white-label, read-only farmer logins)?
7. What compliance/reporting regimes appear (nutrient management planning, USDA programs, carbon protocols)?
8. Where are the boundaries vs the flagged siblings and vs §21 carbon/environmental Types?

## Representative Products

Selected for market representation, documentation reachability, different product philosophies, different customer levels, and different geographies:

| Product | Vendor / origin | Philosophy pole | Customer level |
|---|---|---|---|
| GXLab ("Soil Management Platform") | FarmLab PTY LTD, Australia | measurement-workflow platform spanning soil sampling → lab → analysis → reporting, across agronomy + carbon + natural capital | advisors/agri-service, carbon teams, producers |
| Senus Soil | Senus, Ireland | sampling-campaign management + compliance-grade traceability + soil health/carbon reporting + regional nutrient planning | agronomists, carbon programmes, farmers (read-only) |
| KORE | SoilEssentials, Scotland | white-label precision-farming portal for agronomists and soil-sampling companies; soil sampling + VRA lime/P/K apps | agronomists, sampling contractors, co-ops |
| AgriERP Soil Management | AgriERP (Folio3), US | soil as one module inside a farm ERP: fertility planning + testing + fertilizer/amendment tracking + financials | commercial farm enterprises |
| Soilmentor (Regen Platform) | Integrity Soils, UK | farmer self-serve soil-health testing (spade tests, biology/chemistry/physics), GPS-mapped repeat samples, benchmarks | farmers/ranchers directly |

Boundary pole (fetched, used for edge calibration, not a primary sample member): **LandPKS** (Terraso; free public-good soil-science apps — Soil ID + Classic with soil-health tracking) — measurement + record with an advisory (not mechanized) decision layer; shows where the Type's boundary sits toward soil identification/survey.

Cross-pass corroborating evidence (Tier-1 where noted): Agworld soil-sampling machinery (agronomy pass, help center), farmOS soil-test logs (field pass, user guide), OneSoil soil data on fields + soil-sampling solution (field pass + this pass's search), CropX soil sensors as irrigation substrate (irrigation pass).

## Sources

All fetched 2026-09-09 unless noted.

Tier 2 (official product pages; **no Tier-1 help centers were reachable in this sample** — see Uncertainties):

- GXLab — https://gxlab.com/industries/agriculture/ (fetched; footer links "Soil Management Platform" product page)
- Senus Soil — https://senus.com/senus-soil/ (fetched)
- KORE — https://soilessentials.com/kore/ (fetched)
- AgriERP Soil Management — https://agrierp.com/product-features/crop-management/soil-management/ (fetched)
- LandPKS — https://landpotential.org/ (fetched; boundary pole)

Search-captured official page (live fetch failed ×2 — integritysoils.com and soilmentor.com both transport errors; content used with reduced assertion strength):

- Soilmentor (Integrity Soils) — https://www.integritysoils.com/pages/soilmentor-regen-platform (content captured via search index of the official page)

Search-surfaced (context/boundary only, not primary evidence): Livefarm (livefarm.ie/soil-sampling, Irish DAFM-compliant sampling workflow), OneSoil soil-sampling solution (onesoil.ai/en/solutions/soil-sampling), SoilBeat (soilbeat.com/agronomists), SoilSerdem, Siora (satellite soil analysis), SoilCASTOR/AgroCares (soil carbon), SoilBiom (soil health report service), Zixent Soil Card.

Evidence-layer legend: **A** = directly observed on an official page of one product; **B** = observed across multiple sampled products; **C** = canonical inference from cross-product comparison and boundary reasoning.

## Product Observations

### GXLab (FarmLab PTY LTD, Australia) — [A]

- Self-positioning: "Environmental measurement software for agriculture. GXLab helps agricultural teams plan, collect, analyse and report soil and environmental data across farms, projects and supply chains." "Use one workflow for farm assessments, soil sampling, lab results, carbon projects, natural capital programs and client-ready reporting." Footer product link literally named "Soil Management Platform".
- Platform loop (six named steps): Farm and project setup ("structure data by client, property, paddock, depth, sample round and objective") → Spatial sample planning ("sample plans using farm boundaries, project zones, stratification layers, soil variability and methodology requirements") → Mobile field collection ("Navigate to sample points, capture GPS locations, record barcodes, take photos and collect field notes") → Laboratory connections ("Link samples to lab submissions and bring results back against the correct farm, paddock, point, depth and sample round") → Data analysis ("Review soil results, compare changes over time, map variation and identify useful patterns across farms, zones and management units") → Reporting outputs ("for producers, advisors, corporates, carbon projects and sustainability programs").
- Field-workflow framing: "Sampling is where project data can fall apart. GXLab keeps sample locations, barcodes, photos, notes, lab submissions and results tied together from the start." Offline/online collection; "Depth, round and location metadata"; "Clear handover from field team to laboratory".
- Workflow: Assess → Plan → Collect → Report.
- Use cases: soil carbon projects ("Plan sample rounds, manage stratification, coordinate samplers, connect lab results"); natural capital; precision agriculture ("Use soil test data, spatial layers and sampling history to support better agronomic decisions and targeted management"); corporate sustainability; advisory workflows ("Manage client farms, sample plans, soil results and recommendations from one workspace"); benchmarking and monitoring ("Track soil and environmental indicators over time").
- Who it helps: advisors/agronomists; carbon and natural capital teams; producers and land managers ("Understand soil condition, track change over time and use data to support management decisions"); corporates/asset managers.
- Reports: environmental farm assessment reports; soil carbon and natural capital reports; "Soil fertility and productivity summaries"; project dashboards/client portals; spatial maps and sample round summaries; audit-ready data exports.
- Hardware/tools around the software: RemScan (soil scanner), bench stand, drying unit; SOC Stock Calculator, Sample Size Calculator data tools.

### Senus Soil (Ireland) — [A]

- Self-positioning: "We empower land custodians with innovative technology to optimise soil management strategies with precision and efficiency." "Software For Agronomists And Soil Carbon Programmes… powered by a full campaign management system, allowing companies to seamlessly coordinate large-scale soil sampling programmes with ease."
- Traceability framing: "Every sample collected is meticulously tracked from collection to analysis… This robust traceability ensures data integrity and fosters trust in your soil management practices."
- App (field side): "Collect data in-field via our app, which is adaptable to a wide range of sampling protocols that comply with national and international standards. Select your: Sampling type (e.g. – W Tracks), Depth, Soil Type, Analysis type (Standard, SOM, trace metals, etc), Laboratory. Track samples from field to lab to platform… Barcoding technology speeds up sampling, eliminates labelling error in field and at the lab and it ensures end to end transparency of all data points."
- Platform (office side): "a geospatial (mapping) system that enables the planning, collection and interpretation of soil sampling programmes… underpinned with a project management system."
- Named features: "Project management system giving full visualisation of sampling activity, logistics, admin and data flows. Automated laboratory data feeds and Advanced analytics. Farm maps with colour-coded data displays. Automated farm level soil health or soil carbon report."
- Geospatial modeling: sampling-location optimization ("reduce sample size by up to 50% vs random sampling" — vendor claim); predictive models for SOC concentration, SOC stock, soil pH with uncertainty estimation.
- Package feature list (Starter→Enterprise tiers): field mapping; manual soil data input; colour coded nutrient maps; soil sampling app; barcode labelling; paddock/composite sampling; automated soil health reports; manager dashboard (advisor); **nutrient management planner (Ireland)**; farmer read only login; **fertiliser planner**; laboratory CSV upload; soil health point sampling; multi depth sampling and display; soil carbon sampling management; work order management; sampling campaign dashboard; logistics tracking; SOC modelling; laboratory API; quality control alerts; admin and invoicing console; programme data dashboard; soil scanning data management; programme client login; NDVI yield maps; variable rate integrations; high precision GNSS.

### KORE (SoilEssentials, Scotland) — [A]

- Audience framing: "For agronomists and soil sampling professionals, managing large amounts of data, juggling multiple clients and handling slow, outdated workflows is a constant struggle." KORE = "independent precision farming software… to support agronomists and soil sampling companies to effectively manage their data."
- "With KORE, all your sampling data, reports and client information are brought into one seamless system… You can even brand it as your own" (white-label packages: Basic/Intermediate/Advanced with custom URL and branding).
- Soil Sampling app: "Accurately measure your soil pH, health, organic matter and nutrient indexes." "Field-Specific Results… across the field for more precise agronomic decision-making." "Identify Nutrient Hotspots: Pinpoint low and high nutrient areas for more effective input planning and application." "Enable Precision Management: Target lime, fertiliser, and amendments with confidence to balance soil fertility and pH levels." "Support Long-Term Soil Health: Make informed decisions that improve yields, support biodiversity, soil structure and future productivity."
- VRA Lime, P and K app: "Targeting crop inputs to soil indexes maximises the benefits from your fertiliser and lime costs." "Tailor Lime Application to Soil pH… ensuring optimal nutrient uptake." "Maintain Compliance… Follow industry best practices (RB209 guidelines) for better nutrient management."
- FAQ: "The key four offering areas of KORE are: an integrated soil sampling service; crop monitoring and variable rate – by satellite and drone imagery; analysis of historic field performance with HPI (Historic Potential Index); field performance by yield map processing." Data used: "Soil sampling data, Satellite imagery, Historical yield records, Processed satellite imagery."
- Customer quote: "display soil data that could be interpreted easily and would show changes over time."
- Ideal for: precision agriculture providers, agronomy consultants, crop & soil sampling contractors, co-operatives, environmental monitoring bodies, universities/R&D, agritech start-ups.

### AgriERP Soil Management module (US) — [A]

- Self-positioning: "AgriERP Soil Management is a farm ERP module that centralizes soil test results, fertility plans, fertilizer applications, and cost tracking in one system, so growers can plan by zone, cut over-application, and tie every input back to yield and margin."
- Soil Fertility Planning & Nutrient Management: "Plan zone-specific fertility programs by field, crop, and soil type using soil test data; Track soil pH levels, macro-nutrients (N-P-K), and micro-nutrients across all fields; Schedule soil testing and coordinate sample collection workflows; Forecast fertilizer and amendment needs aligned to crop plans and budgets; Monitor nutrient balances and predict future fertility requirements."
- Soil Testing & Data Centralization: "Import and centralize soil test results from any laboratory or testing service; Store multi-year soil inspection and sampling reports for trend analysis; Auto-flag nutrient deficiencies and soil health concerns; Generate USDA-compliant soil testing documentation; Archive historical soil data for compliance and auditing."
- Fertilizer & Amendment Application Tracking: "Record and track fertilizer applications by field, zone, and growth stage… Calculate true application costs per acre… Compare planned vs. actual fertilizer applications for quality control."
- Soil Health Monitoring & Analytics: "Track soil organic matter levels and soil structure improvements over time; Monitor soil moisture levels in coordination with irrigation management; Analyze soil health indicators linked to crop performance and yield; Identify soil-related yield limitations by field and management zone; Correlate soil management practices with crop outcomes."
- Mobile Soil Data Collection: "Record field observations and soil conditions from mobile devices; Capture georeferenced soil sample locations and photos; Log fertilizer applications and soil treatments offline."
- Compliance & Documentation: "Maintain records for USDA conservation programs (CSP, EQIP, CRP); Document soil conservation practices and nutrient management plans; Generate compliance reports for organic certification and audits."
- FAQ definition: "Soil management software centralizes soil fertility management, testing, fertilizer tracking, and compliance within one platform." Sustainable soil management: "Track sustainable soil management practices including organic fertilizers, soil conservation activities, nutrient management plans, and regenerative soil management techniques."

### Soilmentor (Integrity Soils, UK) — [A-limited: search-captured official page; live fetch failed ×2]

- "The Soilmentor Regen Platform is software that helps you learn what healthy soils and flourishing biodiversity look like on your property. Understand changes on your land above and below ground, make informed decisions and keep everyone in the loop."
- "Monitor your soil health with tests on soil biology, chemistry and physics. Tested in the Field by farmers and ranchers." "We have lots of simple soil health tests to choose from, most of which can be done with only a spade!"
- "Earthworm Index: Assess the ecology of your soil… easily compare different fields, observe the effects of different management techniques, and pitch your fields against UK benchmarks."
- "Map Your Samples: By mapping your soil sample locations on GPS, anyone in the team can return to the same spot over time, and monitor your soil health progress accurately!"
- "The app lists the soil tests you can do in each field. Just select the tests you want and enter the value to record your results… Back in the office, see all your test results across multiple fields over time and begin to understand what's working and what's not for your farm."
- Biodiversity tool (wildlife observation records); speedy in-field data collection with office-side sync.

### LandPKS (Terraso; boundary pole) — [A]

- "Ground-truth your soil decisions." "a suite of free and powerful mobile apps for people working with land and soil, from learners to experts. Built from the ground up to unlock field data for sustainable land decisions."
- Soil ID app: "Collect soil data with easy to follow guides; Identify soils by comparing field data with powerful soil maps; Determine ecological site and Land Capability Classification (USA); Share data with expert advisors; Work in teams; Custom soil depths."
- Classic app: "Monitor rangeland vegetation; Track soil health; Document land management; Calculate available water-holding capacity; Customize Land Capability Classification; Identify Soils."
- Audiences: agricultural extension, teachers/students, farmers/ranchers, researchers, rangeland managers, land-use planners. Public-good, free.
- Boundary reading: measurement + record + advisory decision purpose, with the decision layer thin (no amendment/fertility programme machinery observed on the fetched page) — the pole where the Type thins toward soil identification/land characterization.

### Cross-pass corroborating evidence

- **Agworld** (agronomy pass, Tier-1 help center): soil sampling as managed jobs — zone/grid/composite sample jobs created on the web, executed via mobile app, sequential numbering or barcodes for sample labeling, lab results uploaded via SHP/CSV or integrated labs, results viewed as data layers. Direct Tier-1 confirmation that the sampling-job machinery exists inside agronomy suites (module gradient).
- **farmOS** (field pass, Tier-1 user guide): "If you perform soil tests, these can be stored as 'Lab test' Logs associated with land Assets." Soil tests as one record family on the land asset (field-management gradient).
- **OneSoil** (field pass, Tier-1 help + this pass's search): soil nutrient/EC data uploadable onto fields; soil-sampling solution page — zone-based sampling from productivity zones, automated task maps, point navigation, lab results uploaded in standard formats and "automatically visualized and combined with field data", "Build VRA map based on Soil Sampling Results".
- **CropX** (irrigation pass): soil sensors (moisture/temperature/EC/salinity at multiple depths) as the data substrate for irrigation decisions — soil moisture sensing serving the water decision, not a soil-management center.

## Cross-product Comparison

| Dimension | GXLab | Senus Soil | KORE | AgriERP (module) | Soilmentor | LandPKS (boundary pole) |
|---|---|---|---|---|---|---|
| Soil record organized by | client/property/paddock/depth/sample round | farm maps; paddock/composite; multi-depth | field-specific results; GPS-referenced sampling | fields/zones; multi-year archive | fields; GPS-mapped repeat sample points | sites/points; custom soil depths |
| Measured properties | soil + environmental + carbon indicators | nutrients, pH, SOM, trace metals, SOC | pH, nutrient indexes, organic matter, health | pH, N-P-K, micros, OM, structure, moisture | biology/chemistry/physics (spade tests) | soil properties for ID; health indicators; plant-available water |
| Data production path | sample plans → mobile collection → lab connections → result matching | campaign management → protocol app + barcodes → lab feeds/API/CSV | integrated soil sampling service | schedule testing/coordinate collection; import from any lab | in-field self-tests recorded in app | guided field data collection |
| Result matching | "back against the correct farm, paddock, point, depth and sample round" | field-to-lab-to-platform traceability | (service-managed) | centralize from any lab | same spot over time | (site-based) |
| Decision layer | recommendations (advisory); fertility/productivity summaries | fertiliser planner; nutrient management planner (IE); VRA integrations | target lime/fertiliser/amendments; VRA Lime/P/K maps | fertility programs; fertilizer/amendment applications; planned vs actual | informed decisions (advisory) | sustainable land decisions (advisory) |
| Change over time | "compare changes over time"; benchmarking | predictive models "aiding the monitoring of soil changes" | "show changes over time" | multi-year trend analysis; OM/structure improvements over time | results across fields over time; return to same spot | monitoring posture |
| Outward reporting | producer/carbon/audit reports | automated farm soil health/carbon reports | client reports, white-label | USDA-compliant docs; compliance reports | UK benchmarks (informal) | data portal |
| Operating side | advisors, carbon teams, producers, corporates | agronomists, carbon programmes, farmers (read-only) | agronomists, sampling contractors, co-ops (white-label) | commercial farm enterprises (ERP) | farmers/ranchers self-serve | extension, farmers, researchers (free) |
| Compliance surface | audit-ready exports | carbon protocols; governmental standards | RB209 best practice | USDA CSP/EQIP/CRP; organic certification | — | Land Capability Classification (USA) |
| Map-first presentation | yes (spatial plans, maps) | yes (colour-coded farm maps) | yes (maps/reports) | zone/field framing | sample mapping | map-based soil ID |

### Convergent findings (B layer)

1. Every product holds soil data attached to identified land units (farms/fields/paddocks/zones/sample points), commonly organized per depth and per sampling round.
2. Every product's soil state is established by measurement — laboratory analysis of collected samples, or in-field tests — with results matched back to the correct location (and depth/round where kept).
3. Every product treats the soil record as cumulative: results across rounds/years are retained and compared; "changes over time" is a first-class view in all six.
4. Every product connects the record to decisions about the soil — lime/amendment/fertility decisions and/or soil-health practice judgment — mechanized as plans/VRA maps/recorded applications in some, advisory in others.
5. Map-based presentation of soil data per unit is universal (colour-coded nutrient maps, layers, spatial sample plans).
6. Every product produces outward-facing reports (client/farmer/programme/audit).
7. The service pole (advisor/sampling contractor operating for many clients, farmer read-only) and the self-serve pole (farmer operates directly) are both populated; multi-client machinery is standard in the service pole.
8. Mobile field collection + web/office analysis is the standard shape where collection is software-managed.

### Divergent findings (variant axes, not type structure)

- Data substrate: lab analysis of sampled soil (dominant) vs in-field self-tests (Soilmentor) vs sensor scans (RemScan/AgroCares-class) vs satellite/model inference (Siora/OneSoil-class; Senus predictive models).
- Sampling design: grid vs zone-based vs composite/paddock vs W-trails vs stratified; sample-count optimization via geospatial modeling (vendor-claimed at Senus/SoilSerdem/OneSoil).
- Purpose pole: agronomic fertility (pH/lime/P/K) vs soil health/regenerative (biology, structure, OM) vs soil carbon programmes (SOC stock, protocols, audit) vs environmental/natural-capital assessment.
- Decision depth: advisory summaries → fertiliser/VRA plans → recorded applications with planned-vs-actual and cost/ROI (ERP pole deepest).
- Operating side: agri-service/sampling contractor vs advisor vs grower self-serve vs ERP module.
- Compliance regimes: regional nutrient-management planning (Ireland), USDA conservation programs (US), RB209 (UK), carbon protocols (international) — regime packaging, not structure.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures. If any one is removed, the product is no longer recognizable as Soil Management:

1. **The soil record of record.** The soil of identified land units (fields/paddocks/zones/sample points) held as measured data — test/analysis results describing the soil's state (fertility and chemistry: pH, nutrients, organic matter; and, where kept, physical and biological condition) — attached to the unit, commonly per depth, and accumulating across sampling rounds and years as that unit's soil history. Remove → sampling logistics with no soil data, or a generic field record with no soil substance.
2. **The measurement cycle that produces and refreshes the record.** The soil's state is established and updated through sampling and analysis (or equivalent measurement: in-field tests, sensor or satellite inference), with results matched back to the correct location/depth/round, re-run on a cycle so the record stays current and change becomes visible. Remove → a one-shot test report, or recommendations working on assumed data; a living, slowly-changing resource stops being managed.
3. **The soil-management decision layer.** Decisions and actions on the soil resource itself, informed by the record: amendment and fertility decisions (lime, gypsum, fertiliser, amendments) and/or soil-health practices (cover crops, tillage, organic-matter building, conservation practices), held as recommendations, plans or fertiliser programmes and, in mature implementations, recorded applications tracked against the plan. Remove → a soil data archive / lab-results viewer — measurement without management.

Jointly-held is load-bearing:

- 1 alone = soil data archive / lab results store
- 2 alone = sampling campaign logistics
- 3 alone = generic fertility/recommendation calculator (nutrient-management/agronomy territory)
- 1+2 without 3 = soil testing/data platform (measurement without management)
- 1+3 without 2 = recommendations on stale/imported data
- 2+3 without 1 = sampling logistics + recommendations with no accumulated soil record

### L1 — Common Mature Structure

Present in most mature sampled products; expected by the market but not definitional:

- Managed sampling campaigns: sample plans (zones/grids/points/stratification), sampler tasking, GPS point navigation, barcode/sample-ID capture, photos/notes, depth metadata, offline capture
- Laboratory integration: submissions, CSV/API result feeds, automated matching of results back to location
- Map-first presentation: farm/field maps with colour-coded soil data displays; results as layers
- Multi-year trend views: compare results over time per field/zone/point
- Fertility/amendment planning outputs: fertiliser and lime plans, VRA application maps, regional nutrient-management planning
- Soil health reporting: farm-level soil health reports, benchmarks
- Multi-client/advisor operation: client/property registries, manager dashboards, farmer read-only logins, white-label delivery
- Mobile collection app + web analysis/reporting surfaces
- Compliance/audit reporting (regional nutrient/conservation/carbon regimes)

### L2 — Variant / Optional Structure

- Data substrate: lab-dominant; in-field self-tests; sensor scans; satellite/model inference
- Sampling design: grid / zone / composite / W-trail / stratified; model-guided sample-count reduction
- Purpose pole: agronomic fertility vs soil health/regenerative vs soil carbon vs environmental assessment
- Decision depth: advisory summary → fertiliser/VRA plan → recorded applications with planned-vs-actual, cost and ROI
- Operating side and delivery: agri-service/contractor, advisor, grower self-serve, ERP module; white-label
- Regional compliance regimes (Irish nutrient-management planning, USDA programs, RB209, carbon protocols)
- Carbon-programme machinery (protocols, traceability, audit-grade reporting) — drifts toward §21
- Environmental farm assessment / natural-capital baselining (one pole)

### L3 — Vendor-specific (Research Notes only)

- GXLab: "Soil Management Platform" product naming; Environmental Farm Assessments; RemScan hardware; SOC Stock Calculator / Sample Size Calculator / Soil Colour Analyser tools; Armidale NSW origin (FarmLab PTY LTD).
- Senus: package tiers (Starter/Original/Innovator/Pioneer/Enterprise); "reduce sample size by up to 50%" claim; SOC/pH predictive models with 95% prediction intervals (trained for Europe/USA/South America); W Tracks sampling type; app-store lineage (com.farmeye.soilmate); admin/invoicing console.
- KORE: white-label packages with custom URLs; HPI (Historic Potential Index); RB209 guideline reference; app suite (Satellite Imagery, HPI, Soil Sampling, VRA Nitrogen, VRA Seed, VRA Lime/P/K, Yield Mapping); DJL Agriculture customer story.
- AgriERP: Dynamics 365/Business Central/NetSuite hosting; USDA CSP/EQIP/CRP documentation; AI Companion; "500 to 50,000+ acres" scale claim; fertilizer procurement/inventory integration.
- Soilmentor: spade-test catalog (earthworm index, slake-class tests); UK benchmarks; biodiversity tool; "Regen Platform" naming; Integrity Soils retail context.
- LandPKS: Terraso governance; Land Capability Classification (USA); ecological site determination; free public-good model; Soil ID vs Classic app split.

## Rejected Findings (anti-overfit)

- **Laboratory sampling is not definitional** — Soilmentor's soil state comes from in-field spade tests; satellite/model inference poles exist (Siora-class; Senus predictive models). The invariant is measurement-based state, not the lab.
- **Grid sampling is not definitional** — zone-based, composite/paddock, W-trails, and stratified designs are all in-sample.
- **Barcodes/GPS/offline capture are not definitional** — modern collection machinery; the paper-era routine satisfies the core without them.
- **Carbon machinery is not definitional** — one pole (Senus, GXLab); soil carbon is one measured property among several in the general case.
- **VRA maps are not definitional** — an output form; advisory-only poles function without them.
- **Multi-client/white-label operation is not definitional** — grower self-serve (Soilmentor) and ERP-internal (AgriERP) poles lack it.
- **Soil moisture sensing is not the center** — it is irrigation management's substrate; AgriERP explicitly coordinates ("in coordination with irrigation management") rather than decides water.
- **Fertilizer planning is not exclusively this Type's center** — the soil-test-informed fertility decision is the shared seam with nutrient management; the soil-side center is the soil resource (pH correction, fertility indexes, OM/structure/biology), not nutrient inputs as materials.
- **"Soil management" as a label is not universal** — only some vendors use the phrase (GXLab footer, AgriERP module name, Senus copy); the population is mostly realized as the soil domain slice of agronomy/precision/ERP products. The Type is defined by structure, not vocabulary.

## Historical / Market-Sample Check (§24)

- The pre-digital routine: a farmer or advisor takes soil samples per field, sends them to a laboratory, files the soil test reports in the farm's per-field soil file (the soil record), decides lime and fertilizer from the report (the decision layer), applies them, and re-tests every few years to see the effect (the measurement cycle). All three L0 legs are satisfied with zero software, no GPS, no barcodes, no cloud. The definition holds for the paper era.
- Regional/traditional practice: soil survey maps plus per-field soil test files; land-grant/university soil test reports with lime and fertilizer recommendations — all fit the core under local vocabulary.
- A pure laboratory portal (submit sample, receive PDF) satisfies leg 2 only — correctly excluded: that is the lab's side (LIMS territory), not soil management.
- A fertilizer recommendation calculator with no soil record satisfies leg 3 only — nutrient-management/agronomy territory.
- A static soil-type map (soil survey reference) holds soil *data* but no measured per-unit state, no cycle, no decisions — soil survey/GIS reference territory (LandPKS Soil ID thins toward this pole).
- The definition names no sampling design, no lab, no sensor, no carbon protocol, no compliance regime; all eras and poles fit.

## Boundary Findings

1. **vs Nutrient Management (§20, unprocessed)** — the closest sibling; flagged for joint review at that pass. Working seam from this side: soil management centers the **soil resource** (its measured state and improvement — pH, fertility indexes, organic matter, structure, biology); nutrient management centers **nutrient inputs** (fertilizer/manure as materials — budgets, application planning, regulation). The soil test is the shared artifact; the soil test's fertility half feeds both. Direct evidence of the gradient inside this pass's sample: Senus ships a "Nutrient management planner (Ireland)" and "Fertiliser planner" inside its soil product; AgriERP titles its soil module "Soil Fertility Planning & Nutrient Management". Expected resolution: keep-both with a module/gradient seam, same pattern as irrigation.
2. **vs Agronomy Management (§20, processed 2026-09-06)** — flag DISCHARGED from this side, keep-both RATIFIED with the module/superset gradient confirmed: agronomy management centers the multi-domain recommendation practice (seed + nutrients + protection) on the field record; soil management centers the soil resource. Soil data and lime/fertility recommendations are inputs to agronomy recommendations. The gradient is directly evidenced: soil sampling machinery ships as a module inside agronomy suites (Agworld soil-sampling jobs — Tier-1 from that pass; AgriERP soil module inside the ERP) *and* standalone soil-first products exist (GXLab, Senus, KORE, Soilmentor).
3. **vs Field Management (§20, processed 2026-09-08)** — flag DISCHARGED from this side, keep-both RATIFIED: field management centers the land asset (extent, boundaries, standing characterization with soil as one attribute family); soil management centers the soil resource itself (measured state + improvement loop). Soil-test records attach to fields in field-management products (farmOS "Lab test" Logs on land assets; OneSoil soil uploads — Tier-1 from that pass); in soil management the soil data is the center, not one record family.
4. **vs Irrigation Management (§20, processed 2026-09-08)** — flag DISCHARGED from this side, keep-both RATIFIED: irrigation centers the water decision; soil moisture sensing is irrigation's data substrate (CropX evidence from that pass). Soil management's moisture interest is coordination-level (AgriERP: "Monitor soil moisture levels in coordination with irrigation management"). The irrigation pass's expectation ("same single-domain pattern expected") is confirmed: soil management is a single-domain sibling with its own decision loop.
5. **vs Precision Agriculture Platform (§20, processed)** — soil data → VRA application maps (KORE VRA Lime/P/K; OneSoil "Build VRA map based on Soil Sampling Results"; Senus "Variable rate integrations"): the prescription-execution loop is PA's center; soil management produces the soil-data basis and hands off.
6. **vs Agricultural IoT Platform (§20, processed)** — in-ground soil sensor fleets (moisture/EC probes) are the IoT platform's center; soil management's substrate is dominantly lab sampling, with sensors a variant input.
7. **vs Carbon Accounting / soil-carbon MRV (§21)** — soil carbon sampling programmes with protocols and audit-grade traceability (Senus "soil carbon sampling management"; GXLab carbon projects; SoilCASTOR) — the carbon stock/credit machinery is §21's center; soil management's carbon interest is one measured property among several. Products whose center is carbon programmes belong to §21.
8. **vs Laboratory LIMS** — the laboratory side (sample registration, analysis, QC) is LIS/LIMS territory; soil management consumes lab results (CSV/API feeds) and manages the farm/advisor side of the handover ("clear handover from field team to laboratory"), not the lab.
9. **vs Contaminated Site Management / environmental soil (§21)** — contaminated/remediation soil work is a different subject (pollution, not production soil); GXLab serves a Remediation industry with the same measurement machinery — the machinery is shared, the subject and regime are not.
10. **vs Agricultural GIS (§20, processed)** — soil data as map layers; GIS centers the spatial land base, soil management centers the soil record + loop.
11. **Boundary pole recorded** — LandPKS-class free soil-science apps (soil identification + soil-health tracking with advisory purpose) sit at the Type's thin edge: record + measurement present, decision layer advisory. They remain inside a generous reading of the Type but demonstrate the drift toward soil survey/identification territory.

## Uncertainties

- **No Tier-1 help centers were reachable for any sampled product** (all evidence is official product-page level, Tier 2). Operational mechanics (exact result-matching behavior, sampling-job state models, report scheduling) are asserted at product-page level only. The sampling-job machinery is nonetheless Tier-1 corroborated via the Agworld help center (agronomy pass).
- **Soilmentor live fetch failed twice** (integritysoils.com, soilmentor.com — transport errors); its evidence comes from search-captured content of the official page and is used with reduced assertion strength. The farmer-self-serve pole therefore rests on one product.
- **Nutrient-management overlap depth** could not be fully resolved without processing that leaf; the seam proposed here (soil resource vs nutrient inputs) is this side's position, flagged for joint review.
- **Prevalence of recorded soil-health practice tracking** (cover crops/tillage as recorded activities vs advisory-only) is documented deeply only at the ERP pole (AgriERP); kept as variant depth, not common structure.
- **Market-size claims** (e.g., Senus "reduce sample size by up to 50%") are vendor claims, recorded as such, not asserted in the final document.
- Whether a dedicated "soil moisture management" reading of the leaf exists in the market: no product found under that center; moisture consistently appears as irrigation's substrate or a coordination seam.

## Final Synthesis

Soil Management software is the agriculture-domain system of record for the **soil resource itself**. Its world is: identified land units whose **soil** is held as a measured, accumulating record (test results — pH, nutrients, organic matter, and where kept physical/biological condition — per unit, per depth, per round); a **measurement cycle** (sampling plans → field collection with location identity → laboratory analysis → results matched back) that produces and refreshes that record on a recurring cadence; and a **soil-management decision layer** that turns the record into actions on the soil — lime and amendments, fertility programmes, soil-health practices — with mature implementations recording what was applied and the next measurement round revealing the effect. The market realizes the Type across poles — measurement-workflow platforms for agri-services and carbon programmes, white-label portals for sampling contractors, ERP modules for commercial farms, farmer self-serve soil-health tools — and ships it equally as the soil slice inside agronomy and precision products. The defining core is exactly the three jointly-held structures (record + measurement cycle + decision layer); the sampling design, the data substrate, the purpose pole, the operating side, and the compliance regime are variant axes. The paper-era soil-test file with lime recommendations and a re-test cycle satisfies the core unchanged, which is why the definition depends on none of the modern machinery.
