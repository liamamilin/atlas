# Research Notes — Mine Planning Application

Research date: 2026-09-09
Directory leaf: Mine Planning Application (§20 Agriculture, Food & Natural Resources)
Slug: mine-planning-application

---

## Research Goal

Understand, from real products, what a Mine Planning Application is: what objects it holds, what mine planning engineers do with it, how the planning work flows from deposit model to design to reserves to schedule, and where its boundaries sit against Geological Modeling Platform (upstream), Mining Operations Management / Mining Fleet Management (downstream), CAD, and Project Management.

Special duty: **ratify the forward flag left by the geological-modeling-platform pass (2026-09-08)** — keep-both proposed with the model-consumption seam (the interpretive geological model is the modeling Type's object of record; the mine plan/schedule is the planning Type's), with the block model sitting on the seam.

## Initial Boundary

Working hypothesis before research:

- Core use: software for mining engineers to design mine geometry (open pit: pits/benches/ramps/dumps; underground: stopes/development), evaluate reserves from a geological/block model, and build production schedules (which material is mined when, with what equipment).
- Users: mine planning engineers, technical services teams, strategic planners, mining consultancies.
- Nearest types: Geological Modeling Platform (upstream), Mining Operations Management, Mining Fleet Management, Quarry Management (sibling), CAD, Project Management.
- Unknowns: is scheduling definitional or a variant split? Is pit/stope optimization definitional? How exactly is the design↔schedule link realized? Where is the plan→operations handoff?

## Research Questions

1. What are the core objects (deposit/block model, design solids, pit/stope, reserves, schedule, resources, scenarios)?
2. What is the open-pit design workflow? The underground design workflow?
3. How does reserve evaluation work (intersection of design with model, cutoff/economic rules, reporting)?
4. How does scheduling work (periods/horizons, resources, calendars, targets, manual vs rules-based, optimization)?
5. What is pit optimization (algorithms, nested shells, cutoff grade, NPV) and is it definitional?
6. How do vendors package design vs scheduling vs optimization (one product vs split products)?
7. What interfaces exist (3D viewport, Gantt, tables, scenario manager, reports)?
8. What rules/constraints matter (geotechnical slopes, mining sequence, equipment capacity, blend targets)?
9. What outputs does the plan produce, and how does it hand off to operations?
10. Boundary: what makes it not geological modeling, not operations management, not CAD, not project management?

## Representative Products

Selected for market representation, documentation reachability, different product philosophies (integrated vs split), and different customer tiers:

| Product | Vendor | Philosophy / pole | Evidence reached |
|---|---|---|---|
| Vulcan (+ Evolution) | Maptek | classic integrated 3D design environment; scheduling/optimization as add-ons + separate Evolution scheduling product | product + add-on pages (Tier 2, rich) |
| Deswik.Spatial / Deswik.Planning / Deswik.SO / Deswik.SPD / Deswik.APEX / Deswik.GO | Deswik (a Sandvik company) | explicit design(CAD)/scheduling split products that dynamically link; optimizer family | product pages (Tier 2, rich) |
| Beyond (+ Alastri / Spry / Advance) | Micromine | integrated "Evaluate & Design" product + dedicated Plan products per method; mid-tier/global | product pages (Tier 2, rich) |
| Whittle / MineSched / Surpac | GEOVIA (Dassault Systèmes) | strategic pit-optimization pole (Whittle) | page title only ("Advanced Strategic Mine Planning"); body JS-rendered, unreachable — named anchor only |
| MinePlan | Hexagon Mining | suite (design/schedule/optimize) | unreachable (403 + transport error) — named anchor only |

## Sources

Fetched 2026-09-09 (all official vendor surfaces):

- Maptek Vulcan: https://www.maptek.com/products/vulcan/index.html
- Maptek Vulcan Open Pit Design add-on: https://www.maptek.com/products/vulcan/open_pit_design.html
- Maptek Vulcan Underground Design add-on: https://www.maptek.com/products/vulcan/underground_design.html
- Maptek Vulcan Open Pit Optimisation add-on: https://www.maptek.com/products/vulcan/open_pit_optimisation.html
- Maptek Evolution: https://www.maptek.com/products/evolution/
- Deswik home: https://www.deswik.com/
- Deswik.Spatial: https://www.deswik.com/products/spatial
- Deswik.Planning: https://www.deswik.com/products/planning
- Deswik.SO: https://www.deswik.com/products/so
- Micromine home: https://micromine.com/
- Micromine Beyond: https://www.micromine.com/beyond/
- GEOVIA Whittle (title only): https://www.3ds.com/products/geovia/whittle

Unreachable / limitations:

- help.maptek.com — JavaScript SPA, content not fetchable (1 attempt).
- help.deswik.com — redirects to client-portal login wall (1 attempt).
- hexagon.com/products/mineplan — 403; hexagonmining.com — transport error (2 attempts, abandoned).
- 3ds.com GEOVIA Whittle — JS-rendered shell, body content not fetchable (2 attempts, abandoned).
- Consequence: no Tier-1 help-center articles from any sampled vendor. All operational claims below rest on Tier-2 official product pages (rich, feature-level). Precise numeric limits, algorithm parameters, and default settings are NOT claimed anywhere.

---

## Product A — Maptek Vulcan (+ Evolution)

### Key observations (evidence layer A unless noted)

Positioning (Vulcan home):

- "3D mine planning & geological modelling … allows users to validate and transform technical data into dynamic 3D models, accurate mine designs and operating plans."
- **"Whether developing day to day or long term mine plans, operations need to know where and when to mine."** — the crispest market statement of the Type's two axes (where = design, when = schedule).
- "Running animations and exploring alternative scenarios based on various resource and economic values is the most productive approach to developing practical mine plans."
- Base functionality list: create and edit design data; import/export; visualise design data, triangulations, drillhole and samples databases, **block models** and grids; create and manipulate block models; **reserving capabilities, with options for detailed information breakdown**.
- Packaging: add-ons per role — Geology & Estimation, Open Pit Design, Underground Design, Open Pit Optimisation, Scheduling Suite (Gantt Scheduler + Short Term Planner), Stope Optimiser, Grade Control Suite, Geotechnical Suite, Drillhole Optimiser, SDK. Geological modelling also exists as a separate product (GeologyCore, "Connected geological modelling"); scheduling also as a separate product (Evolution).

Open Pit Design add-on:

- "allows mining engineers to design, evaluate and ensure profitable mine operations. Designs can be easily updated with the latest data for generating daily production reports."
- "simple, repeatable workflows for automated and interactive road and ramp design."
- **"Translate designs into mineable solids and/or blocks ready for scheduling."**
- "Multiple methods to adhere to geotechnical domains with varying batter angle, berm, bench heights and slope angles."
- "Plan, design and construct road systems"; "Reconcile the mine plan with actual site topography."
- "Break down bench into mineable solids for planning and input to detailed schedules."
- Coal washability tools; oil sands design.

Underground Design add-on:

- "create detailed mining shapes for cut and fill, sub-level stoping, and room pillar mining methods. Engineers can generate development networks to connect these mineable shapes."
- "An automatic ramp tool facilitates decline design with intermediate access points, while interactive ramp editor allows users to individually modify ramp sections."
- "Design drives, levels, crosscuts, declines and shafts"; under/overbreak analysis; ring design for stope blasts; Panel Cave Designer for caving; export to VUMA3D/Ventsim ventilation packages (vendor-specific integration).

Open Pit Optimisation add-on:

- "pit optimiser, cut-off grade optimisation, and haulage profile tools."
- "working efficiently with current geological models … rapidly incorporates factors like loss and dilution, while adhering to complex geotechnical constraints … calculating the Net Present Value (NPV)."
- "Running multiple scenarios simultaneously, with on-the-fly reserving."
- "Run scenarios to determine the cut-off grade profile based on Lane's algorithm to account for mining, milling and refining to maximise NPV."
- "Work directly with a block model with the ability to reblock on the fly."
- "Pre-calculate the economic block value or use standard methodology (i.e. Revenue/Cost)."
- "Sensitivity analysis around economical parameters to understand the impact of the size of the pit."
- "Choose between standard Lerchs and Grossmann or push-relabel algorithms."
- "Export output to CSV/Excel or store in the block model."

Evolution (separate scheduling product):

- "produces short, medium, long term and strategic life of mine schedules alongside practical production plans."
- "optimises NPV using cut-off grade techniques"; "optimises the haulage fleet."
- "seamless workflow from strategic to short term scheduling using a single data source. Rapidly iterate scenarios that consider multiple objectives such as cut-off grade, production schedules, dynamic route allocation, haulage cycle times, waste dump allocation, fuel burn and productivity."
- "Rapidly assess thousands of scenarios based on the resource model."
- "Block-by-block scheduling across all planning horizons"; "Know where every block will be mined from and where it will go."
- Features list: align planning horizons; hit blending targets; variable cut-off grade ore definition; holistic scheduling; block-by-block scheduling; optimise NPV; schedule with multiple objectives; compare schedules with block models; drill down into schedules; schedule auditability.
- Sub-products: Evolution Strategy (strategic, cutoff-grade + sequencing, NPV); Evolution Origin (LOM→short term; **"integration with Vulcan closes the gap between design and scheduling"**); Evolution Epoch (short-term; "manage multiple mining activities, tasks and equipment, and apply different types of dependencies"; "attributed solids or block models"); Evolution Phase ("manipulate optimal shells developed in pit optimisation. Adjust, split and combine shells. Write new stage codes back to the model").
- SaaS + hybrid cloud processing.

## Product B — Deswik (Spatial / Planning / SO / SPD / APEX / GO)

### Key observations (evidence layer A)

Suite structure (home):

- Core products: **Spatial** ("The industry's most comprehensive, end-to-end, design solution" — CAD), **Planning** ("The leading scheduling solution that dynamically links your mine designs and schedules"), MDM ("A workflow management solution for your site's mine planning data"), OPS ("A short-term planning and shift execution tool for managing compliance to plan"), NOVA ("unifies mine scheduling, blending and haulage").
- Sector capability menus literally name **"Design & Reserving"** and **"Planning"** as separate capabilities across Surface Metals / Underground Metals / Surface Coal / Underground Coal.
- "Our integrated software platform bridges the gap between mine design and scheduling through seamless data flow."
- Optimizer family: SO (stopes), SPD ("Transform pit shells into final designs"), GO ("Optimize pit designs and schedules simultaneously"), APEX ("Strategic Underground Mine Plan Optimizer — Generate comprehensive Life of Mine schedules optimized for Net Present Value"), LHS (haulage), Blend, BOLT (value chain).
- Operations products (separate): OPS, Operator, ORB (dispatch), Drilling, Survey — the operations side is a different product family.

Deswik.Spatial (design):

- "the end-to-end CAD package to create detailed design plans."
- 3D Modeling: "Generate solids, slice and run Boolean commands. Automatic repair for invalid solids imported from other mining systems."
- Compatibility: "Flexible data import/export supporting industry standard formats including **block and grid models**, GIS & databases. Exceptional integration with Deswik Planning tools."
- Attributes: "**Assign individual mining blocks with location data. Interrogate block models, and write data back to the mining block.** Enable powerful filtering based on data."
- Auto Design toolkits: "Underground metals development, narrow-vein stopes, tabular deposits and backfill. **Pseudoflow pit shell, dig line optimizers.** Surface road design, **coal reserving** & dragline section tools. Underground coal longwall and development layouts."
- Plotting: "Communicate plans using flexible reports & dashboards, schedule animations and coloring."
- Compliance & Reconciliation: "Compliance to design, Compliance to plan, Road audit, Geotechnical reconciliation."
- Environmental: "cut/fill balanced landform and dump surfaces."

Deswik.Planning (scheduling):

- "unified solution to manage both long-range mine planning and detailed short-term schedules in a single environment."
- "Familiar Gantt chart interface with in-built mining functionality designed for underground mining and surface mining datasets."
- "Integrates production, ancillary and project activities with ease."
- **"Supports manual scheduling or automatic rules-based scheduling."**
- "Dynamically modify your schedule and see the impact on your production targets."
- "Select and modify your schedule in the graphics space using CAD and see updates directly in the scheduler."
- "Quickly convert designs into schedulable tasks using automated tools."
- Resource Leveling Engine: "Maximize your resource allocation using sophisticated leveling tools. Mirror real-world objectives with a variety of scheduling controls."
- Flexible Resourcing: "Model individual or pools of resources. Assign resources to activities manually … or use rules." "Customizable calendar tools to model your site's time usage model."
- Reporting: "customized static spreadsheet-style reports … dynamic or interactive dashboards … formula-based calculations."
- Case study title (evidence of optimization inside scheduling): "Maximizing underground project value using Pseudoflow in Deswik's mine scheduling solution."

Deswik.SO (stope optimization):

- "A strategic mine planning tool, Deswik SO automates stoping design for a range of methods used in underground mines so you can strategically maximize the value of your ore body."
- "Automatically generate highest value stope solids across a wide range of mining method geometries and orebody types. Delivers strategic stope designs and pillar location optimization."
- "Wizard-based setup for easy definition of stope parameters like strike and dip, as well as stope and pillar widths. Dilution offsets define planned dilution width on both footwall and hanging wall sides of the stope."
- Scenario Manager: "comparison of multiple design scenarios with rapid adjustments … re-evaluate scenarios against new geological data."
- CAD Integration: "Embedded in our CAD graphics platform (Deswik Spatial) for effortless generation of stope wireframes and solids. Seamless flow into our scheduling platform (Deswik Planning) … Automatically generate development from the stope shapes using the Auto Development Designer."

## Product C — Micromine (Beyond + Alastri / Spry / Advance)

### Key observations (evidence layer A)

Ecosystem structure (home):

- Lifecycle menu: Explore (Geobank, Origin — "Exploration, geological modeling and resource estimation") → **Evaluate & Design (Beyond — "Mine design, planning and surveying")** → **Plan (Alastri — "Mine planning for open-pit metals"; Spry — "open-pit and underground soft rock"; Advance — "Mine planning for underground metals")** → Operate (Pitram — "Fleet management and mine control") → Platform (Nexus).
- The vendor's own menu is a map of the seams: geology (Origin) / design (Beyond) / planning (Alastri, Spry, Advance) / operations (Pitram) are separate products.
- Case study: "Mine planning transformation at Veladero cuts schedule creation times by 40%" (Alastri) — scheduling is the planning products' center.
- Blog titles observed: "Why the ability to iterate is critical in underground mine planning"; "Building defensible underground mine plans faster."

Micromine Beyond (integrated design+optimize+schedule):

- "one integrated environment to streamline every aspect of open-pit optimization, mine design and strategic scheduling."
- Design: "Benches, ramps, berms, and switchbacks can be generated and adjusted quickly, ensuring designs are practical and aligned with geotechnical requirements."
- Optimize: "The integrated pit optimizer maximizes economic return from hard rock orebodies by uniting geotechnical, metallurgical, and financial inputs in one place. Multiple scenarios can be tested quickly, sensitivities compared with ease."
- Schedule: "Life-of-mine scheduling transforms pit designs and optimization results into robust, value-driven plans. Scenarios can be evaluated in detail, risks measured with accuracy."
- Role-based offerings: For Mine Planners ("strategic outputs required for all downstream activity"), For Mine Designers ("reconcile as-mined developments across all mineral commodities"), For Mine Schedulers ("short-term resource extraction planning"), For Mine Surveyors.
- Features: Pit design ("dynamic control over pit geometry, roads, and constraints"); Pit optimization ("industry-standard algorithms"); Strategic scheduling ("schedules that span the life of your mine, test multiple scenarios, and optimise for NPV while keeping every plan achievable").
- "Capable CAD Engine — rapid yet detailed design of surfaces, pits, drives, rises, shafts, declines and inclines."
- "Compatibility for 70+ file formats from over 25 common industry products."

## Product D / E — GEOVIA Whittle, Hexagon MinePlan (named anchors only)

- GEOVIA Whittle page title fetched: "Advanced Strategic Mine Planning". Body JS-rendered, unreachable. No operational claims made.
- Hexagon MinePlan: unreachable (403 / transport error). Known market anchor; no operational claims made.
- Both recorded as market anchors for the strategic-optimization pole and the suite pole respectively; the geological-modeling-platform pass (2026-09-08) independently recorded GEOVIA Surpac and Datamine as unreachable anchors.

---

## Cross-product Comparison

| Aspect | Maptek Vulcan + Evolution | Deswik Spatial + Planning (+SO/SPD) | Micromine Beyond (+Alastri/Spry/Advance) |
|---|---|---|---|
| Type positioning | "3D mine planning & geological modelling" | CAD (design) + scheduling products, "dynamically linked" | "Mine design, planning and surveying" (integrated) |
| "Where and when" framing | explicit: "operations need to know where and when to mine" | design↔schedule dynamic link; "convert designs into schedulable tasks" | design → "transforms … into … plans" |
| Deposit model substrate | block models created/manipulated in-product; "work directly with a block model, reblock on the fly" | imports block/grid models from other systems; interrogates and writes back to mining blocks | consumes models from Origin (separate geology product); 70+ format compatibility |
| Design objects | pit/dump designs, roads/ramps, benches → mineable solids/blocks; UG: mining shapes per method, development networks, drives/levels/crosscuts/declines/shafts | solids with mining-block attributes; pit shells → final designs; stope solids + auto development; longwall layouts | surfaces, pits, drives, rises, shafts, declines; benches/ramps/berms/switchbacks |
| Reserving | "reserving capabilities, detailed information breakdown"; on-the-fly reserving in optimizer; coal reserving tools | "Design & Reserving" capability; coal reserving tools | implicit in optimizer + scheduling outputs |
| Optimization | pit optimiser (Lerchs-Grossmann or push-relabel), Lane cutoff-grade profile, NPV, sensitivity, nested shells (Phase) | Pseudoflow pit shells; SO stope optimizer (strike/dip/pillar widths, dilution offsets); APEX underground NPV LOM; GO multi-pit | integrated pit optimizer, "industry-standard algorithms", sensitivities |
| Scheduling | Evolution: block-by-block, horizons (strategic→short), cutoff-grade policy, blending targets, haulage routes, waste dumps, auditability; Vulcan Gantt Scheduler + Short Term Planner | Gantt; manual OR rules-based auto; resource leveling; resource pools; site calendars; production targets; design-space editing synced to scheduler | strategic LOM scheduling, scenarios, NPV, "keeping every plan achievable"; short-term extraction planning |
| Design↔schedule link | "Translate designs into mineable solids and/or blocks ready for scheduling"; Evolution Origin "integration with Vulcan closes the gap between design and scheduling" | "dynamically link your mine designs and schedules"; edit in CAD graphics space, updates in scheduler | "Life-of-mine scheduling transforms pit designs and optimization results into … plans" |
| Scenario iteration | "thousands of scenarios"; animations; compare schedules with block models | Scenario Manager (SO); "re-evaluate scenarios against new geological data" | "multiple scenarios tested quickly, sensitivities compared" |
| Outputs | daily production reports; CSV/Excel export; results stored back into block model | reports & dashboards, schedule animations, plotting | reports; "strategic outputs required for all downstream activity" |
| Plan↔operations seam | "Reconcile the mine plan with actual site topography"; Resource Tracking = separate product | "Compliance to design, Compliance to plan"; OPS = separate short-term/shift-execution product | "reconcile as-mined developments"; Pitram = separate operations product |
| Sectors | open pit metalliferous/stratigraphic, underground, coal, oil sands | surface/underground metals, surface/underground coal | open-pit metals, soft rock, underground metals/soft rock |
| Deployment | desktop; Evolution SaaS + hybrid cloud | desktop; MDM/cloud data layer | desktop; Nexus cloud platform |

### Stable commonalities (layer B, cross-product)

1. Every product centers on a **plan for extracting a mineral deposit**, expressed as engineered geometry + quantities + time.
2. Every product consumes a **deposit model** (block model or equivalent) as the source of quantities; several import it from a separate geology product.
3. Every product provides **mine design** authoring: open-pit geometry (benches/ramps/roads/dumps) and/or underground geometry (stopes/development/shafts/declines), with geotechnical constraint adherence.
4. Every product **evaluates the design against the model** (reserving: tonnage/grade/content by intersection, with economic/cutoff logic).
5. Every product **schedules** the designed material into time periods with resources, targets, and constraints; horizons span strategic/LOM → medium → short term.
6. Every product supports **scenario iteration** (multiple designs/schedules compared on economic and physical outcomes).
7. Every product **reports/exports** the plan (reports, dashboards, plotting, data export) and connects to a **plan-vs-actual seam** (reconciliation/compliance; operations products are separate).
8. Design↔schedule linkage is a named, engineered feature in all three ("translate designs into … ready for scheduling" / "dynamically link" / "transforms pit designs … into plans").

### Vendor-specific (layer C / L3 — kept out of final doc)

- Maptek: Evolution sub-product split (Strategy/Origin/Epoch/Phase); Lane's algorithm + Lerchs-Grossmann/push-relabel naming; VUMA3D/Ventsim ventilation export; Maptek Workbench/Account licensing; "up to 30% increased value" / "10 times faster" marketing figures.
- Deswik: MDM data/workflow governance product; OPS shift-execution product; NOVA unified scheduling/blending/haulage; BOLT value-chain; RACE rail family (different domain); Pseudoflow branding in Spatial; multithreaded SO v5.0.
- Micromine: Nexus cloud platform; role-based Beyond packages (Planners/Designers/Schedulers/Surveyors); "50M points in under 20 seconds" / "70+ file formats" marketing figures; Pitram operations product.

---

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

The Mine Planning Application is the engineer's system of record for deciding **where and how to extract, and when** — the mine plan. Its defining core is four jointly-held structures:

1. **The deposit model as planning substrate** — a persistent volumetric model of the mineral deposit (block model being the dominant implementation) that the plan consumes; all quantities the plan speaks in are computed from it. Remove → geological modeling territory (if you build it) or generic CAD/scheduling (if you don't have it).
2. **Engineered extraction geometry** — the mine design: authored/edited 3D shapes of extraction (open pit: pit shells, benches, ramps, roads, dumps; underground: stopes, development networks, drives, declines, shafts) authored against mining-method and geotechnical constraints. Remove → a reserve database or a drawing tool; the "where" is gone.
3. **Evaluation of the design against the model (reserving)** — intersecting the designed geometry with the deposit model to compute tonnage/grade/content per mining unit under cutoff/economic rules. Remove → geometry without quantities; the plan cannot speak in tonnes.
4. **The time-phased extraction schedule** — designed mining units assigned to periods under resource, capacity, target and sequencing constraints, iterated as scenarios across planning horizons. Remove → design & reserving without a plan; the "when" is gone, and the Type's name (planning) no longer applies.

Jointly-held load-bearing analysis:

- 1 alone = geological modeling / data store
- 2 alone = CAD
- 3 without 2 = reserve reporting on the raw model (geology/estimation territory)
- 4 without 2+3 = generic project scheduling (Project Management territory)
- 1+2 without 3 = drawing without quantities
- 1+3 without 2 = resource estimation, not mine planning
- 2+3 without 4 = the market's own "Design & Reserving" packaging — a real sub-packaging (Deswik capability name; Maptek add-on structure) but not the Type's center; the plan is what "planning" hangs on
- 1+2+3 without 4 = a mine design system; 1+4 without 2+3 = a schedule over nothing

The "where and when to mine" formulation (Maptek's own words) captures legs 2 and 4; legs 1 and 3 are what make the where/when answerable in tonnes and grade.

### L1 — Common Mature Structure

- 3D visualization environment (design data, triangulations, drillholes, block models in one scene)
- Block model as the dominant substrate implementation (create/manipulate in integrated products; import in split products)
- Pit optimization (ultimate/nested pit shells; Lerchs-Grossmann / pseudoflow-class algorithms; NPV objective)
- Cut-off grade optimization (Lane-type policies; variable cutoff over life)
- Stope optimization (automated highest-value stope solids, pillar/dilution parameters)
- Rules-based / automatic scheduling alongside manual scheduling
- Resource modeling (equipment/fleet as individual or pooled resources), site calendars
- Production targets and blending targets as schedule constraints
- Scenario management (run, compare, iterate; sensitivity analysis)
- Design↔schedule dynamic linkage (edit design → schedule updates; convert designs to schedulable tasks)
- Reporting/dashboards/plotting; export to spreadsheets; write-back of results into the block model
- Reconciliation/compliance surfaces (plan vs as-mined topography; compliance to design/plan)
- Drill & blast design tooling (rings, patterns) — present in most suites as add-on or module

### L2 — Variant / Optional Structure

- Method/commodity packaging: open-pit metals vs underground metals vs coal (stratigraphic/soft rock, longwall, dragline) vs oil sands vs caving
- Packaging architecture: single integrated product (Vulcan, Beyond) vs split design/scheduling products (Deswik.Spatial + Planning) vs dedicated strategic optimizer products (Evolution Strategy, Deswik.APEX, Whittle-class)
- Planning-horizon specialization (strategic vs LOM vs medium vs short-term tools)
- Haulage/fleet optimization in-plan (routes, cycle times, waste dump allocation)
- Survey data handling (bundled in Beyond; separate products elsewhere)
- Grade control / ore control (separate products or suites)
- Geotechnical analysis suites
- Cloud/SaaS processing (Evolution hybrid cloud; Nexus) vs desktop-only
- Data/workflow governance layers (MDM-class)
- Environmental/closure design (landform/dump design, water modeling)

### L3 — Vendor-specific

See Vendor-specific list above; none of it enters the final document.

### Anti-overfitting checks

- **Block model is NOT definitional** — it is the dominant implementation of the substrate, but the substrate abstraction (deposit model) covers seam/stratigraphic models, pre-block-model sections, and imported models. Deswik ships no geological modeling at all and is squarely in-type.
- **3D is NOT definitional** — paper-era planning (long-section drawings + reserve calculations + period schedules) satisfies all four legs; all modern products are 3D (L1).
- **Pit/stope optimization is NOT definitional** — specialized add-ons or separate products; manual design+schedule pole exists (Deswik.Planning manual scheduling first-class; Vulcan design add-ons without optimisation add-on).
- **NPV optimization is NOT definitional** — scenario comparison on physical outcomes satisfies; NPV is the dominant objective in strategic tools (common, not invariant).
- **Automatic/rules-based scheduling is NOT definitional** — manual scheduling is first-class in-sample.
- **Gantt is NOT definitional** — dominant implementation of the schedule surface, not the concept.
- **Cloud/SaaS, AI, auto-haulage NOT definitional** — desktop-era products satisfy.

### Historical / market-sample check (§24)

- Paper era: mine long-sections/plan drawings (design), reserve calculations from sections/assays (evaluation), period-by-period production schedule tables (schedule), hand-drawn geological sections as substrate — all four legs present with no software. Passes.
- 1980s–90s desktop generation (Vulcan's own lineage; Surpac/Datamine/Micromine-era): design + block model + reserving + scheduling on desktop workstations, no cloud, no modern optimizers. Passes.
- Regional and mid-tier vendors (Datamine, RPMGlobal XPAC/Fusion, Snowden, Minemax — named from market position, not fetched): same object grammar. Held as conceptual support only.
- Conclusion: L0 holds across eras and regions; nothing era-specific leaked into the definition.

---

## Boundary Findings

### 1. vs Geological Modeling Platform — FORWARD FLAG RATIFIED (keep-both)

The model-consumption seam holds from this side:

- **Vendors split the two into different products**: Maptek sells GeologyCore ("Connected geological modelling") separately from Vulcan's design add-ons and Evolution; Micromine sells Origin (geology) separately from Beyond (design) and Alastri/Spry/Advance (planning); Deswik sells **no geological modeling product at all** — Spatial imports "block and grid models" from other systems and repairs "invalid solids imported from other mining systems."
- **The plan consumes the model**: quantities come from intersecting design with the model ("work directly with a block model"; "interrogate block models, and write data back to the mining block"). Planning writes results back into the model but does not construct geological geometry from sparse observations.
- **Removal test**: remove the interpretive geological model construction → a mine planning product still plans on imported models (Deswik proves it in the market). Remove the plan → a geological modeling product still models. Keep-both ratified.
- **The block model sits on the seam**: geology products build/constrain it; planning products consume reserves from it and may reblock or write results back (Maptek "reblock on the fly"; "store in the block model"). This matches the geological-modeling pass's finding ("geology products create/constrain it, planning products consume reserves from it").
- Note: integrated products (Vulcan, Beyond) bundle estimation add-ons, and Vulcan's own positioning says "mine planning & geological modelling" — bundling is packaging, not identity. The seam is between *constructing the interpretive geological model* and *planning extraction on it*.

### 2. vs Mining Operations Management (§20 sibling)

- The plan is the artifact handed to operations; the seam is **compliance-to-plan / reconciliation**. Evidence: Deswik OPS is a separate product ("short-term planning and shift execution tool for managing compliance to plan"); Maptek Resource Tracking ("Material tracking & reconciliation systems") is separate; Micromine Pitram ("Fleet management and mine control") is separate.
- Deswik OPS sits ON the seam (short-term planning + shift execution in one product) — recorded as a boundary case, not resolved as a Type split.
- Removal test: remove the future-facing plan (design/reserves/schedule) → operations management still runs the mine on execution records. Remove execution records → mine planning still plans.

### 3. vs Mining Fleet Management (§20 sibling)

- Fleet management = live dispatch/telemetry of equipment (Pitram, ORB-class). Mine planning's haulage work is *in-plan* (routes, cycle times, fleet sizing as schedule inputs — Evolution haulage, Deswik.LHS). Different time orientation (future vs live) and different unit of work (material movement plan vs vehicle).

### 4. vs CAD

- Mine design is CAD-like (Deswik.Spatial is literally "the end-to-end CAD package"), but the objects are mine-specific (mining blocks carrying attributes, pit shells under geotechnical constraints, stopes with dilution offsets) and the purpose is extraction planning (reserves + schedule). Remove the mine objects and the evaluation/schedule purpose → generic CAD. Deswik itself positions Spatial as one half of "mine planning software."

### 5. vs Project Management / Construction Scheduling

- Both schedule in periods with resources, but the mine schedule's tasks are **material quantities derived from a deposit model** (blocks/stopes/tonnes/grade) with blend and production targets — not WBS activities. Deswik.Planning "integrates production, ancillary and project activities" — project activities are the minority adjunct inside a mining schedule.

### 6. vs Quarry Management (§20 sibling)

- Not researched in this pass. Quarry/aggregates operations share geometry+reserves+scheduling grammar but at a different market tier and regulatory/commodity context. Held as adjacent sibling; flagged for that pass.

### 7. Strategic-optimization-only products (Whittle-class, Evolution Strategy, Deswik.APEX)

- Products that only do strategic pit/sequence optimization still produce LOM schedules/sequences from a deposit model — the strategic pole of the same Type, not a separate Type. Held as a packaging variant.

## Uncertainties

1. GEOVIA (Whittle/MineSched/Surpac) and Hexagon MinePlan unreachable — the strategic-optimizer pole and the suite pole are anchored by market position and page titles only; no operational claims from them.
2. No Tier-1 help-center documentation reached for any sampled vendor; all claims are feature-level from official product pages. Algorithm parameters, numeric limits, defaults, and exact workflow steps are deliberately not claimed.
3. Exact scheduling engines (MILP vs heuristic vs rules) per product unknown — not claimed.
4. Quarry Management boundary not researched.
5. Whether Deswik.OPS-class short-term-planning+shift-execution hybrids should eventually sit under Mining Operations Management — left to that pass.
6. Underground coal (longwall/shortwall) scheduling specifics only lightly evidenced (Deswik longwall layout tools named; Spry positioning).

## Final Synthesis

A Mine Planning Application is the mining engineer's planning system of record: it consumes a deposit model, turns it into engineered extraction geometry (open-pit or underground), evaluates that geometry against the model to produce reserves, and time-phases those reserves into a production schedule under resource, target and geotechnical constraints — iterated as scenarios across planning horizons from strategic life-of-mine to short term, and handed to operations as the plan the mine executes against.

The defining core is the jointly-held four-leg structure (deposit-model substrate + engineered extraction geometry + design-vs-model evaluation + time-phased schedule). Everything else — 3D, block models as such, pit/stope/cutoff optimization engines, auto-scheduling, Gantt, cloud, drill & blast, survey, haulage optimization — is common mature or variant structure, not definition.

The geological-modeling forward flag is **ratified: keep-both**, with the model-consumption seam (geology constructs the interpretive model; planning consumes it and writes results back; the block model sits on the seam; vendors split the two into different products, and one sampled vendor ships no geology product at all while remaining squarely in-type).
