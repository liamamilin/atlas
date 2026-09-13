# Research Notes — Agronomy Management

## Research Goal

Understand what "Agronomy Management" software actually is in the market: who operates it (ag retailer / crop consultant / farm), what its world model is (fields, observations, recommendations, execution), what the professional loop looks like, and how it differs from the neighboring agricultural Types already researched (Farm Management Platform, Agribusiness ERP, Agricultural GIS, Precision Agriculture Platform, and the narrower §20 input-domain siblings).

## Initial Boundary

Working hypothesis before research:

- "Agronomy" in ag software usage = the science/practice of crop input decisions: soil, nutrients, seed, crop protection — the agronomist's professional work, not the farm's general business.
- Likely core: field-level records + test/observation data + recommendations (products, rates, timing) + linkage to execution.
- Nearest neighbors: Farm Management Platform (whole-farm ops incl. finance), Precision Agriculture Platform (VRA execution loop), Agricultural GIS (spatial land base), Crop/Field/Nutrient/Crop-Protection Management (narrower domains), Agribusiness ERP (retail agronomy lives inside these).
- Risk: "Agronomy Management" is rarely a marketing category label; products are sold as "agronomy software", "crop planning", "field data", "recommendations". The leaf must be defined by structure, not vocabulary.

## Research Questions

1. Who is the operating organization and who are the primary users (agronomist, retail staff, applicator, grower)?
2. What are the core objects? Is there a stable recommendation/plan artifact across products?
3. What is the canonical loop: observe/test → diagnose → recommend → execute → record → history?
4. How does the recommendation reach execution in different operating models (retail blend/dispatch vs grower work order vs consultant handoff)?
5. What data feeds recommendations (soil/tissue tests, yield history, rotation, imagery, budgets)?
6. Which roles and permissions appear across products?
7. What rules matter (approvals, label/compliance record-keeping, plan→blend→ticket flow)?
8. What is clearly *not* this Type (map analytics without recommendations, equipment control, whole-farm ERP)?

## Representative Products

| Product | Operating model | Why sampled |
|---|---|---|
| Agvance Agronomy (SSI) | Ag-retail ERP vendor; "Agronomy" is one module family of a fully integrated ag-retail suite | The classic US ag-retail agronomy stack: planning → blending → dispatch → invoicing; deep execution machinery |
| Agworld (Semios Group) | Collaborative farm-data platform with a dedicated "For Agronomists" solution; AU/US/NZ/ZA/CA/UK/EU | The advisor-side workflow: plans → recommendations → grower approval → one-click records; multi-grower programs |
| E4 Crop Intelligence | Independent crop-consulting / agronomy-services provider with its own software suite | Consultant operating model; algorithm-assisted fertility & seed prescriptions; service + software bundling |
| MyFarmWeb (boundary check only) | Cloud map/analytics platform (South Africa) | Rejected as core sample: it is the Agricultural GIS pattern (layers + compare + maps) with no recommendation lifecycle — used as boundary evidence |

## Sources

Agvance (fetched 2026-09-06):

- https://agvance.net/ (suite framing: "fully integrated ERP system for ag retailers"; Accounting/Agronomy/Energy/Grain/Grower360)
- https://agvance.net/products/agronomy (Field Solutions, Schedule Jobs, Seed Management, Precise Data Tracking)
- https://agvance.net/products/agronomy/blending (formulation, plans→blend tickets→invoices)
- https://agvance.net/products/agronomy/dispatch (jobs list/schedules, Ops & Inform apps)
- https://agvance.net/products/agronomy/mapping (field data, boundaries, reports, VRT recommendations, machine integrations)

Agworld (fetched 2026-09-06):

- https://www.agworld.com/ (positioning; rec→compliant record one-click claim; planned-vs-actual N/P/K display; audit-ready standardized data)
- https://www.agworld.com/solutions/agronomists (agronomist feature set: plans, recommendations, multi-grower programs, observations, field histories, compliance, precision layers, soil sampling)
- https://www.agworld.com/products/activity-management/ (recs → work orders → activities → automatic spray/fertilizer records; operator mobile app; offline)
- https://help.agworld.com/ + https://help.agworld.com/en/collections/1474249-soil-sampling (Tier-1: zone/grid/composite sample jobs, sequential numbering vs barcodes, lab results via SHP/CSV, results as layers)

E4 Crop Intelligence (fetched 2026-09-06):

- https://e4cropintelligence.com/ (services framing: independent crop consulting, field visits, soil/tissue testing)
- https://www.e4cropintelligence.com/agronomy-services/e4-software/fertility-rx/ (prescription inputs: soil/tissue chemistry, yield history, rotation, production goals, input budget; adjustable parameters; blanket & VRT application cards/maps; Data Bank storage)

Rejected / limited:

- https://www.agrian.com/ — 403, abandoned (1 attempt)
- https://provaya.com/ — unrelated POS vendor (name collision), abandoned
- https://support.agworld.com/ — 404; https://support.agvance.net/ — empty response; Agvance and E4 therefore have **no reachable Tier-1 help centers**; their evidence is product-page level (Tier 2)
- https://www.myfarmweb.com/ — fetched for boundary check only

Evidence-layer legend below: **A** = directly observed on an official page of one product; **B** = observed across multiple sampled products.

## Product A — Agvance Agronomy (SSI)

### Key observations

- Positioning: Agvance is "a fully integrated ERP system for ag retailers"; Agronomy is one product family beside Accounting, Grain, Energy, Grower360 (A).
- Field Solutions: access maps from mobile devices; driving directions to fields; enter field observations while scouting; determine soil sampling points and create "unique identification bag labels" when collecting soil samples; share reports with customers (A).
- Schedule Jobs: data synced between applications immediately; sales staff, dispatcher, applicators "view data, leave notes and receive notifications of work to be done" (A).
- Seed Management: seed inventory, purchases, category, variety, lot within one system (A).
- Precise Data Tracking: collect data on planting, soil, yield "for site-specific agronomic recommendations"; add layers to maps per field; "record products, track plans and change plans to blends when ready" (A).
- Blending: create dry/liquid fertilizer blends and custom chemical/suspension/feed blends; the blending program **imports field plans and nutrient recommendations saved to a grower's field file from the Planning module**; Ratio Wizard; Product Sets; generate blends "to fill a requested analysis", or product at a specified rate per acre, or total amount for a mini bulk; Blend Tickets "import as invoices in Agvance Accounting without re-entering data" (A).
- Dispatch: Jobs List View of "Blend and Delivery Ticket jobs" with customer, field, acres, crop, products, applicable dates, priority, status; Schedules View with real-time applicator locations and reassign/reorder; in-app messaging referencing ticket numbers; weather; **Agvance Ops app** (applicators/drivers view assigned jobs, update statuses, Start/Complete Job) and **Inform app** (sales staff monitor application status, update jobs to Ready) (A).
- Mapping: import data from within Agvance or third-party platforms; connect John Deere / Climate / Raven Slingshot accounts with overnight retrieval; mobile data collection with offline sync; field boundaries via shapefiles import/export; field events; reports (yield maps, soil type maps, soil tests, recs, crop planning, application reports) assembled into branded "report books" shared via PDF/print/email/Grower360; **VRT recommendations** "for application, planting manually or by equation" from analysis layers (normalized yield, management area, profit & loss), or import third-party recommendations (A).
- Inference (C): the retail operating loop is explicitly **grower field file → plan/recommendation → blend/delivery ticket → dispatch → application → invoice**, with the field record as the join point.

## Product B — Agworld

### Key observations

- Positioning: "Farm Management Software" that "digitally connect[s] farmers with their staff, agronomist, contractor, ag retailer" — with a dedicated **"For Agronomists"** solution: "create detailed crop plans and recommendations, record field observations, generate application instructions, and maintain accurate records of products and rates used across every field... keeps recommendations, approvals, and completed operations organized so you always have a clear overview of what has been advised, what has been applied, and what still requires action" (A).
- Core chain (homepage claim): "Your agronomist turns your season's plans into individual recommendations, and with one click of a button these recommendations become compliant digital records" (A).
- Crop plans: "from a simple rotation all the way up to detailed, field by field, production plans" (A).
- Recommendations: "clear agronomic recommendations for every field, with products, rates, timing and other instructions specified" (A).
- Multi-client: "Manage crop plans and recommendations across many growers and farms in one place" (A).
- Planned vs actual: "Monitor planned inputs and compare to actual applications. Evaluate product performance, refine recommendations"; UI shows per-field N/P/K actual/plan (e.g. 12/150 lb/ac) and cost per acre by input class (A).
- Observations: "Record scouting notes, field observations and photos"; field histories across seasons; "Turn precision data into action — bring any precision data layer into Agworld, annotate maps, identify scouting locations" (A).
- Soil sampling (Tier-1 help center): sample **jobs** created on the website (zone / grid / composite), taken via mobile/iPad app; sequential numbering or barcodes for sample labeling; reports on sample results and viewing results **as data layers**; lab results uploaded via SHP/CSV or from integrated labs (A).
- Execution: "crop plans and agronomic recommendations can be converted directly into work orders and field activities... assigned to team members or contractors"; activities tracked planned/underway/completed; recorded in real time via mobile app (offline capable); "When activities are completed, Agworld can automatically convert them into detailed spray or fertilizer records" (A).
- Compliance/reporting: "all agronomic data structured and standardized"; audit-ready; multi-year field records (example UI shows 7 years of records for one field) (A).
- Budgeting: "Forecast your product requirements, and budget ahead... Compare your plans to actual costs in-season"; scenario columns (high input / low input / organic input) (A).

## Product C — E4 Crop Intelligence

### Key observations

- Operating model: independent agronomy services provider ("boots on the ground", regular field visits, soil & tissue testing services) with its own software suite (A).
- Software suite modules: Gateway (field parameter configuration), Data Bank (field data storage/history), Agronomic Testing, Crop Planning and Budgeting, Scheduling, Fertility Rx, Seed Rx, E4 Field Notes (scouting), Map Viewer, Weather (A).
- Fertility Rx: "factors together multiple metrics such as soil and plant tissue chemistry, yield history, crop rotation, production goals, and input budget to formulate a comprehensive prescription"; users "adjust various parameters to see the effects on performance and cost"; "Blanket and variable rate application cards and maps can be generated"; results saved to the Data Bank "for future reference"; can operate on "regional data and estimated yield metrics" when no field history exists (A).
- Inference (C): the consultant operating model keeps the same spine — field data in, prescription out — but the execution half (application/dispatch) is not part of the consultant's product surface; the prescription is the deliverable (application cards/maps handed to operators).
- Module mechanics asserted only at product-page level (no reachable help center).

## Product D (boundary check) — MyFarmWeb

- Cloud platform "for storing, visualizing and comparing all types of maps, geographic and IoT generated agricultural data": soil classification, leaf/tissue results, grid soil nutrition, precision pest monitoring, comparing tool, layer graphs, weather, measuring tool (A).
- No recommendation lifecycle, no plan→execution chain visible; it matches the Agricultural GIS pattern already documented in research/agricultural-gis.md. Included only to show that map-layer analytics alone does not constitute agronomy management.

## Cross-product Comparison

| Structure | Agvance | Agworld | E4 | Evidence |
|---|---|---|---|---|
| Identified field as unit of record (per grower/client) | ✔ grower field files | ✔ fields under farms | ✔ field parameters via Gateway | B |
| Multi-client registry (growers/farms) | ✔ customers | ✔ many growers | ✔ grower customers | B |
| Field observations / scouting capture | ✔ in-field observations, mobile | ✔ scouting notes, photos | ✔ Field Notes module | B |
| Soil sampling machinery (jobs, labels, points) | ✔ sampling points + bag labels | ✔ zone/grid/composite jobs, labels | ✔ (as a service feeding the software) | B |
| Test/lab data as field data layers | ✔ mapping layers | ✔ lab upload SHP/CSV, results as layers | ✔ soil/tissue chemistry inputs | B |
| Crop plans → field-level recommendations (products, rates, timing) | ✔ Planning → recommendations; plans → blends | ✔ plans → recommendations with products/rates/timing | ✔ prescriptions (Fertility/Seed Rx) | B |
| Algorithm-assisted recommendation | partial (VRT by equation) | manual-first | ✔ proprietary algorithms, adjustable parameters | B |
| VRT / variable-rate output | ✔ VRT recommendations (Premium) | ✔ precision layers into decisions | ✔ blanket & VRT cards/maps | B |
| Recommendation → execution handoff | ✔ plans → blend/delivery tickets → dispatch | ✔ recs → work orders → assigned activities | ✔ prescription handed to operators (cards/maps) | B |
| Execution capture back into the record | ✔ Ops app job statuses | ✔ automatic spray/fertilizer records | not visible on public pages | A(×2) |
| Planned vs actual / input usage | partial (analytics) | ✔ explicit actual/plan per nutrient | budget-constrained formulation | B |
| Compliance-oriented application records | application reports | ✔ audit-ready standardized records | not visible | A(×2) |
| Mapping / layers as a surface | ✔ | ✔ | ✔ Map Viewer | B |
| Machine-data integrations | ✔ John Deere/Climate/Slingshot, shapefiles | ✔ John Deere | not visible | A(×2) |
| Fertilizer blending / formulation (retail plant) | ✔ deep (analysis, ratios, sets, blend tickets→invoices) | — | — | A (single-product) |
| Dispatch of applicators/drivers | ✔ deep (3 apps) | contractors assignment (lighter) | — | A (single-product) |
| Grower approval loop of recommendations | implied via status flows | ✔ explicit ("recommendations, approvals, and completed operations") | — | A (single-product) |

## Canonical Model

```text
Grower / client registry
└── Identified field (per season/crop)  ← the agronomic unit of record
    ├── Agronomic observations & test data
    │     (scouting notes/photos, soil & tissue results, yield/planting data — as records or layers)
    ├── Agronomic recommendation / crop plan
    │     (input products + rates + timing + instructions; blanket or variable-rate; manual or algorithm-assigned)
    └── Execution record
          (work order / blend or application ticket / activity → what was actually applied)
    └── Field-level agronomic history across seasons (the accumulated record the next decision is made from)
```

### L0 — Defining Invariant

1. **Identified field as the agronomic unit of record**, carrying its crop/season context, belonging to a grower/operation.
2. **Field-level agronomic observations and test data** attached to that field (soil/tissue results, scouting observations, yield/planting history).
3. **The agronomic recommendation / crop plan** for that field — a recorded specification of input products (seed, nutrients, crop protection), rates and timing, produced by professional judgment (manually or algorithm-assisted).
4. **Persistent field-level agronomic history** linking observations, recommendations and recorded applications over seasons.

Remove the recommendation artifact → the product is field/crop record-keeping, not agronomy management. Remove fields+test data → it is a rec/label generator, not management. Remove multi-season history → single-shot calculators, not management.

Historical check (§24-style): the pre-cloud pattern — co-op agronomist's soil test report + paper recommendation slip + rec book — satisfies 1–4 (the rec book is the persistent history). Early desktop recommendation writers and scouting recorders also fit. The definition therefore does not depend on cloud, mobile, VRT, imagery or AI.

### L1 — Common Mature Structure

- Grower/client registry with farms/fields hierarchy; multi-client operation for retail/consultant variants
- Product catalog (seed varieties, fertilizers, crop protection) with lot/variety detail
- Recommendation builder: blanket and variable-rate; manual or algorithm-assisted; plan → per-field recommendations
- Soil sampling machinery: sample jobs (zone/grid/composite), sample labels/numbering, lab result import (files/integrated labs), results as data layers
- Scouting / observation capture on mobile, photos, offline capture with later sync
- Execution handoff: recommendations converted to work orders / blend & application tickets / assigned activities; status tracking; applicator/operator surfaces
- Execution capture: completed applications recorded back; automatic application/spray records
- Planned vs actual tracking; input usage and cost reporting
- Compliance/reporting: standardized data, audit-ready records, shareable (branded) reports to the grower
- Maps/layers as a presentation surface; boundary/shapefile handling
- Roles: agronomist/advisor, sales, dispatcher, applicator/operator, grower; scoped visibility per role
- Machine-data integrations (equipment/cloud accounts, shapefile interchange)

### L2 — Variant / Optional Structure

- Operating side: ag-retail/co-op (deep blending, dispatch, invoicing handoff) vs independent consultant (prescription as deliverable, budget-conscious formulation) vs grower-internal (execution emphasis) — the same spine, different center of gravity
- Formulation/blending depth (fill requested analysis, ratio tools, blend tickets → invoices) — retail-specific
- Dispatch depth (real-time applicator locations, reassignment, messaging) — retail-specific
- Grower-approval workflow of recommendations (explicit in one collaborative product)
- Precision-ag depth: VRT prescriptions from analysis layers, machine-file exchange, as-applied verification
- Compliance regime depth (regional label/regulatory frameworks; audit packaging)
- AI/algorithm posture (proprietary agronomic models vs manual-first)
- Regional data foundations, crop mix, languages
- Deployment era: cloud suites vs desktop-era tools (structure unchanged)

### L3 — Vendor-specific (Research Notes only)

- Agvance: Blend Tickets importing as invoices into Agvance Accounting; Ratio Wizard; Product Sets; mini-bulk quantities; SKY Dispatch Suite's three apps (Dispatch/Ops/Inform) with "Ready" status semantics; Grower360 portal; branded report books; overnight third-party account retrieval via support call.
- Agworld: one-click recommendation→spray-record conversion; sequential numbering vs barcodes for soil samples; SHP/CSV lab result import; high/low/organic budget scenario columns; 99.9% uptime marketing claim; pricing tiers per region.
- E4: Fertility Rx offered free of charge to Fertilizer Prescription service customers; Gateway/Data Bank module names; "regional data and estimated yield metrics" fallback when no field history exists.

## Vendor-specific Findings

See L3 above. None of these entered the canonical model. The single clearest case: **blending/formulation and applicator dispatch are ag-retail-segment structures**, not defining structures — they are absent from the consultant and collaborative products.

## Boundary Findings

1. **vs Farm Management Platform (§20 sibling)**: center-of-gravity gradient, not a wall. The researched "agronomist" platform (Agworld) self-describes as farm management software while shipping a dedicated agronomist solution — vendors legitimately span both. Working distinction: agronomy management centers the **input-decision practice** (test data → recommendation → execution record); farm management centers **whole-farm operations** (finance, inventory, labor, equipment, plans as operations). Test: remove recommendations/testing → farm management remains; remove whole-farm business ops → agronomy management remains. Consistent with the earlier agribusiness-erp flag (research/agribusiness-erp.md) that field/agronomy records feed, but do not constitute, the farm/business layer. Flagged for joint review when Farm Management Platform is processed.
2. **vs Precision Agriculture Platform (§20 sibling)**: per research/agricultural-gis.md, precision-ag centers the variable-rate **execution loop** (prescription → machine → as-applied verification) with equipment data as a first-class citizen. Agronomy management centers the **professional recommendation practice**; VRT prescriptions are one output form (all three sampled products generate blanket and/or VRT outputs). Gradient; the two share the prescription artifact. Flagged for joint review when Precision Agriculture Platform is processed.
3. **vs Nutrient Management / Crop Protection Management / Soil Management / Seed-adjacent siblings (§20)**: these appear to be single-domain leaves (one input class as the center). Agronomy management is the **multi-domain integration at field level** — one recommendation may span seed + nutrients + protection. Risk: superset/capability relationship (each domain leaf may exist as a module inside agronomy suites). Recorded as a boundary issue for joint review when those leaves are processed.
4. **vs Crop Management (§20 sibling)**: crop management likely centers the crop cycle (planting → growth → harvest operations per field); agronomy management centers the input decision (what to plant/apply, at what rate, when). Both sit on the same field record. Gradient; flagged for joint review.
5. **vs Agribusiness ERP / ag-retail ERP (§20)**: in the retail segment, agronomy operations (blend tickets → invoices, dispatch) are sold as modules of a fully integrated ERP (Agvance). Agronomy management as a Type is the agronomy practice without the books; where the books are the center, the product is the ERP Type. Consistent with research/agribusiness-erp.md boundary #2.
6. **vs Agricultural GIS (§20 sibling)**: map-layer analytics without a recommendation lifecycle is the GIS pattern (MyFarmWeb as sampled evidence), not agronomy management; conversely every sampled agronomy product carries maps as a secondary surface. Center-of-gravity test: the recommendation artifact vs the spatial land base.
7. **Naming observation**: no market category is literally named "agronomy management"; products are marketed as agronomy software/modules, crop planning, prescription/consulting software. The leaf is best understood as the **agronomy-practice-structured segment** of agricultural software — defined by structure (field record + test data + recommendation + execution linkage), not vocabulary. Recorded as observation, no taxonomy change proposed.

## Uncertainties

1. No reachable Tier-1 help center for Agvance or E4 (support.agvance.net empty, no public manuals found; E4 has no public docs beyond product pages). Agvance execution mechanics (ticket status flow details) and E4 module mechanics are asserted only at product-page level.
2. Agrian (recommendations/labels specialist) returned 403 on the single fetch attempt; the label-compliance depth of the Type (regulatory record-keeping for crop protection recommendations) is evidenced only indirectly (Agworld's "compliant digital records", application reports) and is kept weak in the final document.
3. Execution capture in the consultant model (E4) was not visible on public pages; the claim that prescriptions are "handed to operators" is an inference from the services framing (application cards/maps as deliverables), marked as inference.
4. The exact relationship to the single-domain siblings (Nutrient/Crop Protection/Soil Management) could not be resolved without processing those leaves; recorded as boundary issue, not resolved unilaterally.
5. Grower-approval of recommendations is explicitly documented for one product (Agworld); Agvance implies it via status flows but does not document an approval gate on public pages. Kept as variant, not common structure.

## Final Synthesis

Agronomy Management is the software of the **agronomy practice**: its world is a registry of clients (growers) and their **identified fields**, each field carrying **agronomic observations and test data** (soil/tissue results, scouting, yield and planting history) out of which the agronomist produces **recommendations and crop plans** — recorded specifications of seed, nutrient and crop-protection products with rates and timing — that are then **handed to execution** (work orders, blend/application tickets, operator activities) and **recorded back**, accumulating a season-over-season **field agronomic history** that becomes the substrate for the next decision. Everything else commonly bundled — multi-client management, product catalogs, soil-sampling job machinery, VRT outputs, maps and layers, compliance reporting, retail blending and dispatch, grower approval loops, machine integrations — is common mature or segment-specific structure. The Type's identity is the recommendation-centered professional loop on the field record; remove the recommendation artifact and the remainder is field/crop record-keeping, not agronomy.
