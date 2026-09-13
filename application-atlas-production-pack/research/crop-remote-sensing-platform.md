# Research Notes — Crop Remote Sensing Platform

Research date: 2026-09-07

## Research Goal

Understand what a Crop Remote Sensing Platform actually is as an Application Type: what objects exist inside it (fields, imagery, indicators, zones, scouts, prescriptions), how remote sensing data becomes crop-management decisions, who operates these systems, where the type's boundary sits against Precision Agriculture Platforms, Agricultural GIS, Farm Management Platforms, drone photogrammetry software, and general satellite imagery services.

## Initial Boundary (hypothesis before research)

- Core use: monitor crop condition across agricultural fields using satellite / aerial / drone imagery, detect within-field variability and problems, and feed crop-management decisions.
- Users: farmers, agronomists, crop consultants, agribusiness/food companies, insurers.
- Nearest neighbors: Precision Agriculture Platform, Agricultural GIS, Farm Management Platform, Environmental Monitoring Platform, drone photogrammetry software, satellite imagery services.
- Unknowns: is the field boundary a defining structure or an implementation detail? Is the imagery-to-action loop (scouting / prescriptions) definitional? Is multi-date monitoring definitional or common?

## Research Questions

1. What are the core objects? (field/parcel, imagery acquisition, vegetation index, zone, scouting record, prescription map, report)
2. How does imagery enter the system — which sensing platforms (free public satellites, commercial constellations, drones), and who runs the processing?
3. How is crop condition expressed (indices, biomass, moisture, growth stages) and how is change over time handled?
4. How does the platform connect observation to action (scouting, alerts, VRA maps, reports)?
5. Who uses it and in what role (grower vs agronomist vs consultant vs insurer)?
6. What rules/constraints matter (cloud cover, revisit frequency, resolution tiers, data ownership)?
7. Where is the boundary against: Precision Agriculture Platform, Agricultural GIS, Farm Management, photogrammetry software, imagery data services?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

1. **EOSDA Crop Monitoring (EOS Data Analytics)** — satellite-first standalone monitoring platform, freemium, global (growers + consultants, large plantations, insurers). Philosophy: remote analytics and risk management from space.
2. **OneSoil Platform** — free-start web + mobile platform, European origin, predefined field boundaries. Philosophy: no-data-needed onboarding, monitoring first, precision tools layered.
3. **Climate FieldView (Bayer / Climate LLC)** — digital farming platform for large commercial growers (Americas/Europe), where satellite imagery + scouting is one leg beside equipment data collection (Drive hardware), yield analysis, and prescriptions. Philosophy: agronomic data platform centered on the grower's own data.
4. **PIX4Dfields (Pix4D)** — drone-first desktop application with built-in satellite option, offline/edge processing. Philosophy: capture-to-prescription in minutes without cloud dependency.

Attempted but abandoned: **xarvio FIELD MANAGER (BASF Digital Farming)** — decision-support pole; www.xarvio.com returned 404 for every attempted URL (product page, /en/, root) from the research environment on 2026-09-07. Dropped per source-access rules; the decision-support-augmentation pattern remains unverified in this sample (see Uncertainties).

## Sources

- EOSDA Crop Monitoring product page: https://eos.com/products/crop-monitoring/ (fetched 2026-09-07)
- OneSoil Platform page + FAQ: https://onesoil.ai/en/platform (fetched 2026-09-07); Help Center noted at https://help.onesoil.ai/en/ (not fetched)
- Climate FieldView homepage: https://climate.com/ and Scout Fields solution page: https://climate.com/en-us/solutions/scout-fields.html (fetched 2026-09-07); Knowledge Center (support.climate.com) is a JS application — not fetchable
- PIX4Dfields product page: https://pix4d.com/product/pix4dfields/ (fetched 2026-09-07); support/documentation portal noted at https://support.pix4d.com (not fetched)
- xarvio: https://www.xarvio.com/en/products/field-manager, https://www.xarvio.com/en/, https://www.xarvio.com/ — all 404 (fetched 2026-09-07)

Evidence layers used below: **A = directly observed** on that product's official pages; **B = cross-product commonality** (observed in multiple sampled products); **C = canonical inference** (abstraction over the sample + boundary reasoning).

## Product Observations

### EOSDA Crop Monitoring

Key observations (all A unless noted):

- Positioning: "Crop Monitoring Platform For Remote Farm Risk Management"; self-described "smart precision agriculture platform" for tracking "crop health and field conditions".
- Stated users: Growers and Agricultural Consultants; case studies also feature insurers (damage-claims assessment), food/plantation companies, forestry, irrigation-service companies, and an API-driven farmer network in Africa.
- Documented 6-step workflow: (1) Add fields — upload a boundaries file or draw them, add current/previous season crop info; (2) Access satellite data — latest images "right when they capture your field", NDVI and other vegetation indices; (3) Analyze trends — historical vegetation and weather data; (4) Check current risks during the growing season; (5) Take action — "send scouts to the land plot or plan your field activities", track outcomes; (6) Share data — custom reports to stakeholders.
- Crop-health monitoring tool: vegetation indices ("ready-to-go 10 vegetation indices" — vendor number), Sentinel-2 and PlanetScope imagery "cleared of clouds and shadows", daily monitoring with up-to-3m imagery (vendor precision — research notes only).
- Growth Stages: chart based on the BBCH scale and sowing date, per crop.
- Risk Map: monitor risk of diseases, weather, and vegetation-index change across all fields; automated notifications about risks.
- VRA (variable-rate application) maps: generated from NDVI, NDMI, RECI, MSAVI, elevation, or machinery data; framed as saving fertilizer/seed/water.
- Field Activity Log: tillage, irrigation, scouting tasks; plan tasks, assign to plots, monitor completion; shared across the team.
- Yield estimation feature ("predicting yield and biomass … for the next 14 days" — vendor precision).
- Weather analytics: forecasts, historical weather, cold/heat stress, ground weather-station connection; spraying/tillage timing.
- John Deere Operations Center integration: field data sync, boundaries detection, application/harvest operations.
- Automated/customizable reports; Team management with role-based access ("unlimited team accounts" — vendor claim); field leaderboard for consultants managing many client plots.
- Freemium: free field monitoring tier; mobile scouting app; EOSDA API for embedding analytics.
- Customer-voice evidence of the core loop: NDVI maps → identify low-vigor areas → notify producers → field visit/scouting; historical data used to pinpoint when a problem began; insurers use imagery to date damage events.

### OneSoil Platform

Key observations (A):

- Positioning: "field monitoring, scouting, productivity analysis, variable-rate application maps, soil sampling, field trials… AI-powered agronomic recommendations in one connected system". Two connected products: OneSoil Mobile (fieldwork) + OneSoil Pro (browser, planning/analysis), sharing the same fields, users, and data.
- Zero-data onboarding: "No data is needed from your side to start getting value" — select fields from predefined boundaries or draw/upload them.
- Satellite field monitoring: NDVI, NDRE, RECI, moisture layers, weather layers (FAQ: "combines satellite imagery, vegetation indices, weather data, and field-level analytics").
- Anomaly/stress detection: "Find stress and anomalies before they spread" with highlighted stressed zones.
- Hyperlocal weather per field; spraying-window forecast; field diary.
- Season comparison: "Compare across seasons. Put current conditions in context."
- Machinery data: telemetry overlay matched with satellite imagery; John Deere Operations Center integration; export formats for variable-rate equipment; yield data import for analysis.
- Productivity zones ("over 90% correlation to yield map" — vendor marketing claim); zone-based soil sampling plans with homogeneity classes; VRA task maps (seeding, fertilizing, spraying) with batch creation; input savings calculator; field trials with control/treatment strips.
- Scouting: mobile app with observation categories (disease, pests, weeds, lodging, waterlogging, other); scouting-priority ranking ("Scout where it matters most" — heatmap of fields needing attention first).
- AI Agronomist (AgroCopilot): reads fields daily, cross-references satellite signals/weather/crop calendar, produces a ranked attention list; answers questions about a field's vegetation map.
- High-resolution Planet imagery as a paid layer. API access. Multiuser. Field-boundary export. Crop identification across countries (OneSoil Global Analytics — separate product).
- Business model: free start; Mobile subscription; Pro priced per region/hectares; 14-day Pro trial; audiences: growers + agro consultants.

### Climate FieldView

Key observations (A):

- Positioning: "all-in-one digital farming solution" for commercial growers; global footprint (Americas, Europe, Africa, Oceania country sites).
- Four solution pillars: Gather Information (collect, connect & share crop data), Scout Fields (assess field pressures from anywhere), Build Prescriptions, Analyze Data (yield data real-time).
- Scout Fields page: high-definition imagery "on every acre to monitor vegetation and biomass" (early detection); scouting pins with image + custom tags + notes; shareable pins to a crop scout's email/phone; permanent pins for fixed objects (fuel tanks, power lines); weather alerts (hail, equipment speed, crop health); field-level rainfall accumulation.
- Imagery sits beside equipment-data collection: FieldView Drive 2.0 (cab hardware connecting to displays, Bluetooth to iPad, records every pass), display adapter kits for CNH and John Deere GreenStar.
- Sharing: share an operation, a farm, or single fields with an agronomist for insights/recommendations.
- Analysis: color-coded yield maps and charts; field/input/practice comparison; seed scripts (vendor performance claim "+5 bu/ac" — marketing number, research notes only).
- Data ownership messaging: "Own your data and take control of who has access" (data-rights posture is a visible product principle).
- 60+ partner connectivity (vendor claim); real-time alerts.
- Boundary note: FieldView is broader than a pure crop remote sensing platform — imagery/scouting is one capability inside a grower data platform whose other legs (equipment passes, yield analysis, prescriptions) belong to Precision Agriculture / Farm Management territory. Included deliberately as the embedded-realization pole of this Type.

### PIX4Dfields

Key observations (A):

- Positioning: "Hybrid drone and satellite mapping software for aerial crop analysis and precision agriculture".
- Imagery in: drone imagery (RGB and multispectral; DJI Mavic 3 Multispectral demo datasets; supported-drone catalog) and built-in access to high-resolution satellite imagery ("Generate detailed crop insights and vegetation indices in seconds, from anywhere in the world").
- Outputs: orthomosaic, vegetation index maps, zonation maps, annotations, digital surface model (DSM), spot-spraying prescription maps.
- Processing: instant processing engine, minutes, fully offline on-device ("in-field or in-office… No internet required"); runs on Windows/macOS.
- Workflow tools: generate indices; zonate and prescribe (management zones); measure and annotate; "Magic tool" (instant weed detection for green-on-green spot-spraying prescriptions); crop scouting; boundaries/polygons incl. holes; measurements & counting; trial plot management; crop damage assessment.
- Action out: ready-to-use and customizable variable-rate and spot-spraying prescription maps for spray drones, tractors, and field sprayers; ISOXML (ISOBUS) export "compatible with all machinery brands"; John Deere Operations Center integration.
- Time: "Inspect, analyze and visualize your crop changes all year round" — multi-date comparison across the season/year.
- Sharing: via PIX4Dcloud, PDF reports, industry-standard formats.
- Use cases listed: crop scouting, variable rate application & spot spraying, boundaries/measurements/counting, trial plot management, reports & documentation, damage assessment.

## Cross-product Comparison

| Structure / capability | EOSDA | OneSoil | FieldView | PIX4Dfields | Layer |
|---|---|---|---|---|---|
| Fields with boundaries + crop/season context as anchor | A (draw/upload boundaries, seasons) | A (predefined or draw/upload) | A (fields/farms/operations) | A (field boundaries, polygons) | B → L0 |
| Imagery from remote sensing processed into crop indicators | A (Sentinel-2, PlanetScope, indices, cloud clearing) | A (satellite layers: NDVI/NDRE/RECI/moisture) | A (high-definition imagery, vegetation & biomass) | A (drone + satellite, index maps) | B → L0 |
| Multi-date / season monitoring & comparison | A (historical vegetation trends, growth stages) | A (season comparison, "every day") | A (season-long passes + imagery) | A ("crop changes all year round") | B → L0 |
| Within-field variability / problem-zone detection | A (risk map, problem areas) | A (anomaly/stress zones, productivity zones) | A (early detection, imagery detail) | A (zonation, spot-spraying zones) | B → L0 |
| Translation into action: scouting | A ("send scouts", scouting tasks, mobile app) | A (mobile scouting, categories, priority ranking) | A (pins, shareable to scout) | A (crop scouting, annotations) | B → L0 (part of the observation→action loop) |
| Translation into action: machine-ready prescriptions (VRA) | A (VRA maps from indices/machinery data) | A (VRA task maps, machinery export, JD OC) | A (Build Prescriptions pillar) | A (VR + spot-spraying maps, ISOXML) | B → L1 (mature, not definitional — see below) |
| Alerts / risk notifications | A (risk notifications) | A (AI attention ranking, anomaly alerts implied) | A (weather/crop-health alerts) | — (not observed on page) | B → L1 |
| Reports / stakeholder sharing | A (custom/automated reports) | A (AI report; sharing) | A (share fields with agronomist) | A (PDF reports, cloud sharing) | B → L1 |
| Weather layers | A (forecast, history, stress, stations) | A (hyperlocal, spraying windows) | A (rainfall, hail alerts) | — | B → L1 |
| Equipment-data integration | A (JD OC sync; machinery data as VRA source) | A (JD OC, telemetry overlay, yield import) | A (Drive hardware, display adapters, yield maps) | A (JD OC, ISOXML) | B → L1 |
| Team / multi-client management | A (roles, unlimited team, leaderboard) | A (multiuser) | A (share operation/farm/fields) | A (cloud sharing) | B → L1 |
| Growth-stage models | A (BBCH chart) | A (crop calendar reference in AI) | — | — | A (single product strong; common in category knowledge but not evidenced across sample) → L2-leaning |
| Yield/biomass estimation | A | A (yield import for analysis; productivity) | A (yield analysis) | — (damage assessment) | B → L1/L2 |
| AI assistance (anomaly, advisory, weed detection) | A (risk detection framing) | A (AgroCopilot) | — (alerts) | A (Magic tool weed detection) | B → L1 (era-typical), form varies |
| Drone imagery as primary source | — | — | — | A | Product-specific posture → L2 |
| Cloud vs offline processing | A (cloud platform) | A (web/mobile/cloud) | A (cloud + cab hardware) | A (offline desktop) | B → L2 (deployment philosophy) |
| Free tier / freemium | A | A | — (plans) | — (trial) | B → L2 (business model) |
| Boundary auto-detection of fields | A ("boundaries detection" via JD sync) | A (predefined boundaries, country-scale detection heritage) | — | A (polygon drawing; RTK boundaries) | Mixed evidence → L2 |
| Hardware (cab device) | — | — | A (Drive 2.0) | — | Vendor-specific → L3 |
| Predefined country-scale field library | — | A | — | — | Vendor-specific → L3 |
| Insurance/claims use | A (case studies) | — | — | — | Segment use → L2 |
| BBCH growth stages | A | — | — | — | Vendor-specific implementation → L3 |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

Three structures; remove any one and the product stops being a crop remote sensing platform:

1. **Field-anchored crop context** — identified fields/parcels (boundary geometry + crop and season context) to which all sensing and analysis attaches. Remove → general satellite imagery analytics (browse-any-imagery services) or a GIS tool.
2. **Remotely sensed crop-condition indicators** — imagery acquired by remote sensing platforms (satellite / aerial / drone), processed into crop-state layers (vegetation/biomass/moisture family) over those fields, across multiple dates. Remove → a scouting/record-keeping app with no sensing, or a photo archive.
3. **Variability-to-action translation** — the platform's output is decision-directed: it localizes within-field variability and problems (zones, anomalies, low-vigor areas) and delivers them into crop management — surfacing them to a human via views/alerts/reports/scout handoff, and/or converting them into machine-ready prescriptions. Remove → a static imagery viewer/archive.

Why the action leg is L0 and not just prescriptions: in all four sampled products the platform's stated purpose is "identify problems → decide/act" (EOS: "identify problems and risks… make smart decisions"; OneSoil: "turn insights into action"; FieldView: "assess field pressures from anywhere"; PIX4Dfields: "from images to insights… faster decision-making"). The specific action forms (VRA maps vs pins vs alerts) vary; the delivery of observed variability into crop management does not. The VRA-map *machinery* is therefore L1 while the delivery-into-decisions property is L0.

### L1 — Common Mature Structure

Present across the sample, expected in mature products, not definitional:

- index catalogs beyond a basic vegetation index (NDVI as default; NDRE/RECI/NDMI/MSAVI family)
- cloud/shadow handling and the free-public-constellation backbone (Sentinel-2/Landsat) with commercial high-resolution layers as a paid upgrade
- time-series charts per field/zone; historical season comparison
- zone machinery (management/productivity zones, zonation maps)
- scouting support (mobile capture with photos/tags/categories, shareable pins, task assignment)
- alerts/risk notifications
- weather layers (forecasts, stress, spraying windows, station connection)
- equipment integration (John Deere Operations Center; machinery data as VRA input; yield-data import)
- prescription/VRA map generation and machine-format export
- reports (custom/automated) and stakeholder sharing
- team/role management; multi-client (consultant) operation
- yield/biomass estimation
- APIs for embedding
- AI assistance (anomaly/stress detection, ranked attention lists, weed detection)

### L2 — Variant / Optional Structure

- Acquisition posture: satellite-first vs drone-first vs hybrid; free-constellation vs paid high-resolution
- Processing location: cloud platform vs offline edge (desktop) vs hybrid
- Packaging: standalone monitoring platform vs embedded capability inside a broader digital-farming platform vs desktop tool
- Business model: freemium + subscription vs plan-based vs license
- Customer tier: smallholder/free vs commercial grower vs consultant networks vs agribusiness/plantation/insurance use
- Region: free-constellation-heavy regions vs equipment-data-heavy regions (cab hardware, display adapters)
- Field-boundary sourcing: draw vs file upload (SHP) vs predefined libraries vs auto-detection vs equipment sync
- Growth-stage models (crop-calendar integration) — evidenced in one product strongly
- Adjacent additions: field activity logs/diary, soil-sampling plans, field trials, savings calculators

### L3 — Vendor-specific

- EOSDA: BBCH growth-stage chart; "10 ready indices" / "3 m daily" / "14-day yield forecast" marketing figures; field leaderboard; brand API surface.
- OneSoil: predefined country-scale field library; AgroCopilot AI branding; input savings calculator; Global Analytics crop-identification product.
- FieldView: Drive 2.0 cab hardware and display adapter kits; seed-script marketing claim; "60+ partners"; data-ownership program framing.
- PIX4Dfields: Magic tool weed detection; instant offline processing engine; DSM output; PIX4Dcloud sharing; RTK boundary flight workflow.

## Vendor-specific Findings (kept out of the final document)

- All numeric vendor claims (index counts, resolution, forecast windows, ROI multiples, partner counts, yield-delta claims) — marketing precision, unverifiable from fetched pages.
- FieldView's equipment-hardware ecosystem is a product family around the platform, not a property of the Type.
- OneSoil's predefined-boundary onboarding is an implementation of field creation, not the Type's requirement.

## Boundary Findings

**vs Precision Agriculture Platform** — PA is the broader discipline: equipment telemetry, section control, execution of prescriptions, field operations. The crop RS platform's center of gravity is sensing → indicators → variability → decisions; PA machinery (VRA export, JD sync) appears in all four samples as an *output seam*, but equipment-data collection (passes, as-applied maps) is not the center. Test: remove remote sensing/imagery → FieldView-minus-imagery is still a precision-ag data platform; remove equipment telemetry → EOSDA/OneSoil/PIX4Dfields are still crop RS platforms. Adjacent, with a real seam inside FieldView (deliberately sampled as the embedded pole).

**vs Farm Management Platform** — FMS centers on records, plans, inputs, inventory, compliance, economics. RS platforms only touch operations where observation feeds action (EOS Field Activity Log, OneSoil field diary) — adjacent capability, not core. Test: remove imagery/indicators → FMS still stands; remove records/economics → RS platform still stands.

**vs Agricultural GIS** — GIS is general geospatial layer management and cartography. RS platforms are crop-analytics pipelines with a fixed semantic (fields, seasons, crop indicators) and a monitoring mission. A GIS can produce an NDVI map; it does not run the season-long, alert-and-decide loop.

**vs Drone photogrammetry software** — photogrammetry builds orthomosaics/3D from photos (surveying mission). PIX4Dfields shows the split inside one vendor: PIX4Dmapper (photogrammetry) vs PIX4Dfields (crop indicators, zoning, prescriptions). Photogrammetry is upstream machinery for the drone-realization of this Type, not the Type itself.

**vs General satellite imagery services / marketplaces** (search-view-analyze any imagery; imagery APIs) — no field anchoring, no crop/season semantics, no action loop. EOS itself sells both (LandViewer vs Crop Monitoring) — the vendor maintains the distinction.

**vs Environmental Monitoring Platform** — environmental compliance/condition monitoring (air/water/emissions) lacks crop context and the field production mission. Overlap only where agri-environment programs (carbon, dMRV) consume crop-RS outputs.

**Degenerate tests ("remove X → becomes another Type")**:
- remove field anchoring → general satellite imagery analytics
- remove remote sensing → scouting/FMS records app
- remove variability detection + action delivery → imagery archive/viewer
- remove crop semantics (monitor any land) → land/environment monitoring platform

**Historical / market-sample check**: the L0 holds for older and differently positioned forms — aerial infrared photography interpreted by agronomists to locate stress/disease (field-anchored ✓, remotely sensed indicators ✓, variability→advisory ✓); regional/national satellite crop-monitoring programs (multi-date indicators over production areas ✓); platform-native imagery inside farm-management suites (FieldView, John Deere Operations Center imagery — the three structures appear as a module ✓). So L0 is not overfit to the current free-constellation + cloud era; free satellite backbones, cloud processing, AI, and VRA export are current-market implementations, not definitional.

## Uncertainties

- xarvio FIELD MANAGER (decision-support pole: imagery + disease models + spray recommendations) could not be reached; the "model-augmented decision layer" pattern is plausible industry knowledge but is NOT evidenced in this sample — the final document therefore describes advisory/AI augmentation generically and at moderate strength.
- Help-center depth not reached for any product (EOS help 404; OneSoil Help Center and Pix4D support portal not fetched; FieldView Knowledge Center is a JS app). Plan-tiered feature gating, exact imagery-delivery SLAs, and per-plan limits are unverified — no precise numbers in the final document.
- Whether "growth-stage models" are common across the category: strong evidence in one sample only; kept as variant-leaning, not common-structure.
- Whether boundary auto-detection is now a standard expectation: observed in two products in different forms; kept qualified.

## Final Synthesis

A Crop Remote Sensing Platform is a field-anchored agricultural monitoring application whose defining core is three structures: (1) identified fields with boundaries and crop/season context as the anchor of everything; (2) imagery from remote sensing platforms (satellite/aerial/drone) processed into dated crop-condition indicators over those fields; (3) translation of within-field variability into crop-management action — surfacing problems to people (views, alerts, reports, scouting handoff) and/or converting them into zone/prescription outputs for machines. Around that core, mature products add index catalogs, time-series and season comparison, zoning, scouting support, weather layers, equipment integration, reports, team/multi-client management, yield estimation, APIs, and AI assistance. Realizations range from satellite-first freemium web platforms (EOSDA, OneSoil) through drone-first offline desktop tools (PIX4Dfields) to imagery as one leg of a broader grower data platform (FieldView). The type is distinct from Precision Agriculture (execution/equipment-centered), Farm Management (records/economics-centered), Agricultural GIS (cartography-centered), photogrammetry (reconstruction-centered), and general imagery services (no crop anchor).
