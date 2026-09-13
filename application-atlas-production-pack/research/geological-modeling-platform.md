# Research Notes — Geological Modeling Platform

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (update-v1)
Directory leaf: Geological Modeling Platform (§20 Agriculture, Food & Natural Resources)
Slug: geological-modeling-platform

---

## Research Goal

Establish what a Geological Modeling Platform actually is as an Application Type — from real products, not marketing abstractions — and fix its boundary against neighboring Types (Mine Planning, 3D Modeling, GIS, Digital Twin, CAE/simulation, environmental data platforms).

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis)**: software where geoscientists build an interpretive 3D (and 2D) model of the subsurface — the geology as computed geometry — from sparse observational data (drillholes, mapping, geophysics, points/surfaces), then interrogate, update, and hand that model downstream (resource estimation, mine planning, hydrogeology).
- **Who (hypothesis)**: geologists (exploration, resource, production/grade control), geotechnical engineers, hydrogeologists — in mining first, then energy/geothermal, civil/tunneling, groundwater.
- **Nearest neighbors (hypothesis)**: Mine Planning Application (§20 sibling), 3D Modeling Application (§04.13), GIS (Agricultural/Government), Digital Twin Platform (§16), CAE/Simulation (§16), Environmental Data Platform (§21), drillhole-data-management products.
- **Unknowns at start**: whether implicit vs explicit modeling is definitional or an implementation axis; whether block models / resource estimation belong in the core; how the market realizes oil & gas subsurface modeling; whether the mining-suite vendors' geology modules are the same Type as standalone modeling products.

## Research Questions

1. What are the core objects (project, drillhole database, domains, wireframes/solids, block model)?
2. What is the canonical workflow loop (import → validate → interpret → construct → validate → publish → update)?
3. Which modeling methods are implementations vs invariants (implicit, explicit wireframing, ML)?
4. What does the software compute vs what does the user author?
5. What interfaces do users actually work in (3D scene, project tree, sections)?
6. Where does resource estimation / block modeling sit — core, standard, or downstream?
7. How do models update as new drilling arrives (the "living model" claim)?
8. Boundaries: vs Mine Planning (who owns the block model?), vs CAD/3D modeling, vs GIS, vs data-management products.
9. Historical check: does a paper-era interpretation workflow satisfy the same structure?

## Representative Products

Selected for market representation + documentation accessibility + different product philosophies + different customer tiers:

1. **Seequent Leapfrog Geo** (Bentley) — the implicit-modeling specialist; engines sold by market (Geo/Energy/Works); strong public docs (help.seequent.com, Learning Centre). Fetched: product page, implicit-modelling explainer, help portal + Leapfrog Geo 2026.1 help intro.
2. **Maptek Vulcan + Maptek GeologyCore** — the mine-suite heritage pole (Vulcan: "3D mine planning & geological modelling") plus its dedicated connected geological modeling product (GeologyCore); both fetched.
3. **Micromine Origin** (+ family context Geobank/Beyond/Alastri/Spry/Advance/Nexus) — the exploration-to-grade-control single-environment pole; explicitly sells BOTH implicit and explicit modeling; subscription ladder by workflow stage. Fetched: product page.
4. **GEOVIA Surpac** (Dassault Systèmes) — market anchor only; 3ds.com product URLs 404 ×2 — dropped per network rule; no operational claims.
5. **Datamine (Studio family)** — market anchor only; site returns non-HTML (SVG shell) — dropped; no operational claims.

Oil & gas subsurface modeling products (Petrel-class) were not sampled (documentation gated); the definition is abstracted over their grid structures (see Uncertainties).

## Sources

Fetched 2026-09-08:

- Seequent — Leapfrog Geo product page: https://www.seequent.com/products-solutions/leapfrog-geo/
- Seequent — "What is Implicit Modelling?": https://www.seequent.com/community/learn-geoscience/implicit-modelling/
- Seequent — Help portal: https://help.seequent.com/ ; Leapfrog Geo 2026.1 help intro: https://help.seequent.com/Geo/2026.1/en-GB/Content/intro.htm
- Maptek — Vulcan product page: https://www.maptek.com/products/vulcan/
- Maptek — GeologyCore product page: https://www.maptek.com/products/geologycore/
- Micromine — Origin product page: https://www.micromine.com/origin/ ; Micromine site/product family: https://www.micromine.com/

Unreachable / not fetched:

- GEOVIA Surpac (3ds.com) — 404 ×2
- Datamine — site renders SVG shell, no content
- Maptek Help (help.maptek.com), Seequent Leapfrog Geo deep topic pages, Datamine Help — not attempted (enough evidence per stop conditions)

Evidence layers used below: **A** = directly observed on a fetched official page (product named); **B** = cross-product commonality across the researched sample; **C** = canonical inference from comparison + boundary reasoning.

---

## Product A — Seequent Leapfrog Geo

### Key observations (all A)

- Self-positioning: "Fast, accurate implicit modelling software for geological interpretation"; category label "Leapfrog 3D geological modelling".
- "Build well-informed and dynamically updatable geological models in a fraction of the time. Bypass time-consuming wireframing and rapidly generate, visualise, and maintain 3D implicit models."
- Data-in claim: "Collate and integrate all your geoscience data, including drillhole data, structural data, points, polylines, and meshes, to generate reliable models."
- "Effortlessly update models with new data — Dynamically update models as data becomes available."
- Collaboration: "Share and review models with built-in tools and cloud publishing through Seequent Central."
- Resource estimation link: Edge Extension — "Combine the insights from your 3D Leapfrog models with industry-standard resource estimation tools… links a living geological model to a real-time block model" (block model interrogation & reporting, domaining, estimators, variography).
- Subscription feature list: "Advanced geological modelling, Numeric modelling, Block modelling, 2D & 3D visualisation, Industry interoperability, Collaboration tools, Intuitive interface."
- Family: Leapfrog Geo (mining) / Leapfrog Energy ("energy projects including geothermal, offshore wind, CCUS, and hydrocarbon" — help portal) / Leapfrog Works ("civil & environmental projects"). Same engine, market-differentiated editions.
- Implicit vs explicit explainer: "Implicit modelling is the fast and automated formation of surfaces such as grade, faults and alteration directly from geological data. Explicit modelling is what is considered the 'traditional' manual method of wireframing and digitising." Leapfrog "pioneered" implicit modelling (launched 2004); engine handles "the labour intensive and repetitive work, to give you more time for interpretation and the consideration of multiple hypotheses."
- Help structure (2026.1): Managing Leapfrog Geo Projects; The Project Tree; The 3D Scene; Visualising Data; Slicing Through Data in the Scene; Organising Your Screen Space; Working With Data Tables.
- Leapfrog Viewer: "open scene files exported from Leapfrog Geo… change how models and data are displayed, create slices, and make measurements in the 3D scene."
- Extensions: Hydrogeology (MODFLOW/FEFLOW), Geophysics (seismic SEG-Y 2D/2D-crooked/3D, GPR, MT resistivity).

## Product B — Maptek Vulcan + GeologyCore

### Key observations (all A)

- Vulcan self-positioning: "3D mine planning & geological modelling"; "the world's premier 3D mining software solution, allows users to validate and transform technical data into dynamic 3D models, accurate mine designs and operating plans."
- "Sophisticated algorithms enable virtually instant validation of models, allowing users to build a continuous and up-to-date picture of a deposit."
- Vulcan functionality: "Create and edit design data; Import/export data routines; Visualise design data, triangulations, drillhole and samples databases, block models and grids; Create and manipulate block models; Reserving capabilities."
- Vulcan add-ons: Geology & Estimation (geology tools + geostatistics + estimation), Open Pit Design, Underground Design, Grade Control Suite, Geotechnical Suite, Scheduling Suite, Open Pit Optimisation, Stope Optimiser, Drillhole Optimiser.
- GeologyCore ("Connected geological modelling"): "streamlines the geology workflow from importing and validating drillhole data, through defining geological domains to generating accurate, reliable models."
- "Processes are intuitively grouped for importing and validating drillhole data, defining domains before generating and publishing geological models. Repeatable steps allow for easy experimentation, with changes to domains reflected immediately on the model."
- Methods: "Create models using machine learning, traditional vein, stratigraphic or implicit modelling techniques" (DomainMCF = ML domain boundaries from sample/drillhole data).
- Validation: "Validate models using section mode, juxtaposition view, filtering and numeric checks."
- Handoff: "Publish models to Vulcan… Data is published back to Vulcan to model grades and perform advanced statistical analysis." "Easily update models with new data."
- Maptek Geoscience solution framing: "Turn geological data into accurate models that maximize resource potential and form the foundation of every mine plan."

## Product C — Micromine Origin

### Key observations (all A)

- Self-positioning: "Exploration, geological modelling and resource estimation"; "Integrate, validate, interpret, and communicate critical mineral resource data… spanning from early exploration through to resource evaluation."
- Modeling breadth: "Industry-leading implicit modelling tools accelerate the creation of grade shells, lithology boundaries, faults, and surfaces. Guide results with your interpretation using strings, points, and structural disks to ensure models reflect your geological understanding. Comprehensive explicit wireframing tools provide detailed, hands-on modelling for those who prefer classical control — allowing you to build, edit, and manipulate wireframes."
- AI: Grade Copilot — "Powered by neural networks, it uncovers hidden patterns and refines domains… swiftly generate plausible grade and geology models."
- Estimation: "Run multiple estimates simultaneously, visualise block models interactively… Kriging and Inverse Distance Weighting (IDW) estimates across elements, domains, and search passes."
- Grade control: "define ore boundaries, plan dig blocks… real-time reconciliation… Automated dig line creation… Ore tracking and visualisation… blast displacement."
- Features: "3D GIS capability — A powerful 3D GIS visualisation environment for optimised interrogation… of spatial data"; "Visualisation of 2D, 3D and downhole geophysics data (LAS, 2D and 3D SEG-Y)… Create effective plans and cross-sections"; "Drillhole and surface data management"; "Interactive and flexible 3D modelling — tools to build, manage and manipulate 3D solids and surfaces for exploration, resource estimation and geological modelling"; "Geostatistical analysis"; plotting/charting/reporting; compatibility "70+ file formats from over 25 common industry software solutions"; big-data claims (15M rows / 10M points).
- Subscription ladder = workflow stages: Exploration / Geology Modelling / Resource Modelling / Grade Control / Enterprise Geology Teams.
- Family separation: Geobank = "Geoscience data logging and management" (data); Origin = geology + estimation; Beyond = "Mine design, planning and surveying"; Alastri/Spry/Advance = mine planning; Pitram = fleet/mine control; Nexus = cloud platform. Geology and mine design are different products from the same vendor.

## Market anchors (no operational claims)

- GEOVIA Surpac (Dassault Systèmes) — long-established geology & mine planning software family (Surpac/GEMS/Whittle). Named only.
- Datamine Studio family — geology & resource modeling suite. Named only.

---

## Cross-product Comparison

| Dimension | Leapfrog Geo | GeologyCore (+Vulcan context) | Micromine Origin |
|---|---|---|---|
| Entry workflow | integrate geoscience data (drillhole, structural, points, polylines, meshes) | import & validate drillhole data | integrate, validate drillhole + surface + geophysics data |
| Interpretive objects | implicit surfaces (grade, faults, alteration), geological models | geological domains; solids/surfaces via vein/stratigraphic/implicit/ML | lithology boundaries, faults, grade shells, 3D solids and surfaces, wireframes |
| Construction | implicit (engine "takes care of the labour intensive work") | ML + vein + stratigraphic + implicit; "changes to domains reflected immediately" | implicit + explicit wireframing + AI (Grade Copilot); user guides with strings/points/structural disks |
| Validation/interrogation | 2D & 3D visualisation; slicer; Viewer measures/slices | "section mode, juxtaposition view, filtering and numeric checks" | 3D GIS environment; plans & cross-sections; Distance-to-Drillhole uncertainty tool |
| Update loop | "dynamically update models as data becomes available" | "easily update models with new data"; repeatable steps | rapid implicit re-generation; AI refines domains |
| Estimation/block models | block modelling in base; Edge extension links "living geological model to a real-time block model" | publish to Vulcan "to model grades and perform advanced statistical analysis" | Kriging/IDW estimator; interactive block models; grade control |
| Downstream handoff | Central cloud publishing; Viewer scene files | publish to Vulcan (design/scheduling suite) | Nexus platform; mine-design products separate (Beyond/Alastri/Spry/Advance) |
| Collaboration layer | Central ("connected workflows, real time collaboration") | Vulcan roundtrip; Workbench platform | Nexus ("Connecting teams, data and technology in the cloud") |
| Editions | Geo/Energy/Works by market | Vulcan (mine suite) + GeologyCore (geology-first) | subscription by workflow stage (Exploration→Grade Control→Enterprise) |

### Evidence-layer mapping (B layer — cross-product commonality)

- Drillhole/geoscience data import + validation as the opening workflow — A×3 → B.
- Interpretive geometry objects (domains/boundaries as solids/surfaces/wireframes) — A×3 → B.
- Computed construction from sparse data with user guidance — A×3 → B.
- 3D scene + sectioning as the interrogation surface — A×3 → B (Leapfrog "Slicing Through Data in the Scene"; GeologyCore "section mode"; Origin "3D GIS visualisation environment… plans and cross-sections").
- Living-model update on new data — A×3 → B (all three state it nearly verbatim).
- Publish/handoff to estimation or mine-design machinery — A×3 → B.
- Resource estimation & block models adjacent to the geology model — A×3 → B, with different packaging (base feature / separate product / extension).
- Separate data-management and collaboration layers — A×3 → B (Central, Workbench, Nexus; plus sibling data products MX Deposit, Geobank).
- Market-differentiated editions of one engine — A×3 → B.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (deliberately minimal)

Four jointly-held structures. Remove any one and the product is no longer a Geological Modeling Platform:

1. **The interpretive geological model as the object of record** — a persistent project holding the geologist's interpretive 3D representation of a piece of the real earth (geological units/boundaries/faults/surfaces as bounded computed geometry). Remove → mine planning or CAD territory.
2. **Sparse real-earth observations as the input of record** — drillhole data (collars/surveys/logs/assays), surface mapping, points/surfaces/geophysics loaded, validated, and visualized in 3D as the evidence the interpretation must honor. The model is derived from measurements of the real earth, not authored from imagination. Remove → 3D Modeling Application.
3. **Data-driven construction of continuous geological geometry** — the software computes continuous geometry from the sparse observations (implicit interpolation, guided explicit wireframing, or machine learning — method is an implementation axis). Remove → a data viewer or section-plotting tool.
4. **The 3D interpretive loop** — model and observations coexist in one 3D scene; the geologist sections/slices, compares model against data, adjusts the interpretation, and regenerates; the model updates as new observations arrive. Remove → a one-shot processing utility.

The model-as-deliverable (published/handed to estimation, mine planning, hydrogeology) is the workflow terminus, not a fifth leg.

### L1 — Common Mature Structure (not definitional)

- Drillhole database machinery (collar/survey/lithology/assay tables, validation rules, import/export format breadth — "70+ file formats" claim at one vendor)
- Block models and grade estimation (kriging/IDW-class; variography; grade shells) — the geology model as the domain frame for estimation
- Sectioning/slicing tools, cross-section and plan generation, plotting/charting/reporting
- Model publishing/viewers (scene files, read-only viewers), model management/versioning (Central-class)
- Georeferencing/GIS utilities (coordinate conversion, contouring, online imagery)
- Extension surfaces: hydrogeology (MODFLOW/FEFLOW-class), geophysics (seismic, GPR), geotechnical
- Uncertainty tools (e.g., drillhole-spacing/distance analysis)
- Collaboration platforms and cloud data management layers

### L2 — Variant / Optional Structure

- Modeling philosophy: implicit-first vs explicit-first vs mixed vs ML-assisted (and cloud-ML options)
- Market edition of the same engine: mining / energy-geothermal-offshore-wind-CCUS / civil-environmental
- Grade control machinery (dig lines, ore tracking, blast displacement, reconciliation) — production-geology variant
- Suite packaging: standalone modeling product vs module inside a mine suite vs subscription ladder by workflow stage
- Deployment: desktop (historical norm) vs cloud platforms; license posture (named/shared seats)
- Regional/sector customers: exploration juniors → enterprise resource teams

### L3 — Vendor-specific (research notes only)

- FastRBF™ (Seequent's named algorithm; "well over 1,000,000 points" claim), Leapfrog 2004 launch date
- Domain Manager, DomainMCF (ML domain modeling), Seismic Tools add-on (Maptek)
- Grade Copilot (Micromine neural-network assistant), Distance to Drillhole Tool, Grade Estimator form
- Edge/Hydrogeology/Geophysics extension names; BlockSync; Seequent Evo; MX Deposit; Imago; Nexus; Workbench
- Specific numeric claims (15M rows / 10M points / 70+ formats / 25+ software products) — vendor marketing, kept here

### Anti-overfitting check (§22 rule applied)

- Implicit modelling is NOT in the core: the market's own explainer (Seequent) defines implicit as one method against "traditional" explicit wireframing, and Maptek documents "machine learning, traditional vein, stratigraphic or implicit" side by side; Micromine sells both. The invariant is "computed continuous geometry from sparse observations," method-agnostic.
- Block models are NOT in the core: they are the mining realization of a downstream estimation grid; Leapfrog sells estimation as an extension, Maptek moves grade modeling to Vulcan, and oil & gas / civil realizations use different grid forms. Held at L1.
- "Platform" in the leaf name: modern products are sold inside platform ecosystems (Central/Nexus/Workbench), but the modeling application is the Type; the ecosystem layer is L1/L2 furniture.

### Historical / Market-Sample Check (§24)

- **Analog pre-history**: paper-era geologists built cross-sections, plan maps and blockout sketches by hand from drill logs and assays — observations plotted (input), hand-interpreted sections/maps (model of record), manual interpolation/digitising (construction), re-drawn as new holes arrived (loop). All four L0 legs satisfy at analog level; the software Type digitizes the geologist's interpretation workflow.
- **Older software generation**: the 1980s mining-software generation (Vulcan, Surpac, Datamine, Micromine heritages) already carried drillhole databases, wireframing/triangulation, block models and 3D visualisation — no implicit algorithms, no cloud, no AI needed to satisfy the core. Implicit modelling (2004+) and ML are era machinery.
- The definition therefore names: no modeling method, no block/grid form, no cloud, no AI, no specific data format.

---

## Vendor-specific Findings

- Seequent sells the same engine by market (Geo/Energy/Works) and pushes "dynamic" model updating as its philosophy; estimation is an extension (Edge) linking "a living geological model to a real-time block model."
- Maptek splits geology from mine machinery: GeologyCore publishes models "to Vulcan to model grades and perform advanced statistical analysis" — an in-vendor articulation of the geology-vs-planning seam.
- Micromine sells workflow-stage subscriptions (Exploration / Geology Modelling / Resource Modelling / Grade Control) and bundles an AI assistant into modeling subscriptions.
- All three vendors ship separate drillhole-data-management products (MX Deposit / Vulcan databases / Geobank), confirming data management as a sibling, not this Type.

## Boundary Findings

1. **vs Mine Planning Application (§20 sibling, unprocessed)** — the strongest boundary. The mine plan consumes the geological model; planning objects are pits/stopes/schedules/sequences. Maptek's own split (GeologyCore → publish → Vulcan) and Micromine's split (Origin vs Beyond/Alastri/Spry/Advance) show geology modeling and mine design as separate products. Removal test: remove the interpretive geology model → a mine planning product still plans on imported models; remove the plan → a geological modeling product still models. Keep-both expected; forward flag left for the mine-planning pass. The block model sits on the seam: geology products create/constrain it, planning products consume reserves from it (Maptek: block models inside Vulcan functionality list; Micromine: estimation inside Origin subscriptions).
2. **vs 3D Modeling Application (§04.13)** — authored/imagined geometry vs geometry derived from measurements of the real earth; identical seam wording to the photogrammetry pass ("authored vs measured"). A geological modeling product with no observational data input is a CAD tool; a 3D-modeling product cannot honor drillhole validation rules.
3. **vs GIS (Agricultural GIS §20 / Government GIS §24)** — GIS centers mapped surface features and spatial analysis; geological modeling centers subsurface interpretive volumes. "3D GIS capability" appears inside modeling products as a feature (Micromine), confirming adjacency not identity.
4. **vs Digital Twin Platform (§16)** — the geology model is an iterated interpretive representation of nature, not an operations-linked live twin fed by plant telemetry. Some vendors' marketing says "digital twin"-adjacent things; the machinery is different.
5. **vs CAE/Engineering Simulation (§16)** — simulation runs physics through a model; geological modeling builds the model. Hydrogeology/numerical extensions (MODFLOW/FEFLOW-class) sit downstream of the geology model and are sold as extensions (Leapfrog Hydrogeology Extension), confirming the seam.
6. **vs Environmental Data Platform (§21, processed) / Environmental LIMS-class** — those Types hold the observational corpus as the system of record (samples, results, stations). Geological modeling consumes observations to compute geometry. The same drillhole dataset can live in both; the object of record differs (observations vs interpretive model).
7. **vs drillhole/sample data management products (MX Deposit, Geobank)** — capture/quality/management vs modeling. Separate sibling products inside the same vendors.
8. **Oil & gas subsurface modeling (no directory leaf)** — Petrel-class reservoir/geological modeling products serve the same structure in a different sector vocabulary (wells/logs/seismic horizons, structural frameworks, corner-point grids). Directory has no leaf for them; recorded as a taxonomy note, not a change request.

## Taxonomy observations

- The leaf name "Geological Modeling Platform" matches market vocabulary ("geological modelling software", "3D geological modelling", "connected geological modelling") well.
- The Type sits in §20 (Agriculture, Food & Natural Resources) with mining siblings; the market also serves civil/environmental/energy sectors from the same engines — sector breadth is a variant, not a definition issue.
- No alias/variant problem found: the leaf is a genuine standalone Type.

## Uncertainties

- GEOVIA Surpac and Datamine could not be fetched (404s / non-HTML shell) — held as named market anchors only; no operational claims about them. Their structures are assumed similar from market position only, and the core does not depend on them.
- Oil & gas subsurface modeling (Petrel-class) not sampled; the L0 is written to abstract over grid/corner-point realizations, but no first-hand evidence for that sector is cited.
- Explicit-wireframing depth at Leapfrog was not directly documented in fetched pages (Leapfrog positions itself implicit-first); explicit wireframing as a common capability rests on Micromine (A) and Seequent's own implicit-vs-explicit explainer (A).
- Maptek Help and deep Leapfrog Geo topic pages were not fetched (stop conditions reached); interface detail rests on help-intro level evidence.
- Historical check is conceptual (paper-era workflow reasoning); no archival software manuals were fetched.

## Final Synthesis

A Geological Modeling Platform is the geoscientist's interpretive-model workbench: it takes sparse observations of the real earth (drillholes, mapping, geophysics), validates and displays them in a 3D scene, computes continuous interpretive geometry from them (method-agnostic: implicit, explicit, or ML), supports the interpret→compare→adjust→regenerate loop with model-vs-data validation, and publishes the resulting geological model as the foundation for resource estimation, mine planning, hydrogeology, and other downstream uses. The defining core is the four-legged structure above; everything else the market sells — block models, grade control, collaboration platforms, market editions, AI assistants — is standard, optional, or vendor furniture.
