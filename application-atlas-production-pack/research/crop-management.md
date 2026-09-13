# Research Notes — Crop Management

## Research Goal

Understand what "Crop Management" software actually is in the market: what the managed object is (the crop-season on a field/plot/block), what the canonical loop is (plan → execute → record → monitor → harvest → history), who operates it (grower, enterprise farm, agribusiness managing many growers, specialty-crop service provider), and how it differs from neighboring agricultural Types — especially Agronomy Management (joint-review flag from that pass), Farm Management Platform, Precision Agriculture Platform, Agricultural IoT Platform, and the single-domain §20 siblings.

## Initial Boundary

Working hypothesis before research:

- "Crop management" = managing a crop through its cycle on a specific piece of land: planning the crop and its operations, executing and recording field operations through the season, watching crop condition, closing with harvest, retaining season history.
- Nearest neighbors: Agronomy Management (input-decision recommendations), Farm Management Platform (whole-farm business), Precision Agriculture Platform (VRA execution loop), Agricultural IoT Platform (sensing backbone), Field Management (land unit as asset), Harvest Management (harvest operation), single-domain siblings (Irrigation / Crop Protection / Nutrient / Soil Management), crop-specific siblings (Orchard / Greenhouse / Vineyard Management).
- Risk: "crop management" is used loosely as marketing vocabulary; several structurally identical products self-label as "farm management software". The leaf must be defined by structure, not vocabulary.

## Research Questions

1. What is the unit of record — the field, the crop, the season, or the operation?
2. What is the canonical loop across products (plan → execute → record → monitor → close)?
3. Which operation classes are recorded (planting, input applications, care work, scouting, irrigation, harvest)?
4. How is in-season crop condition handled (monitoring, models, alerts, advisories)?
5. How do plans/schedules reach execution (work orders, crew tasks, spray windows)?
6. What rules matter (worker-safety intervals, food-safety audits, PoP adherence, traceability)?
7. What roles appear (grower, farm manager, agronomist, supervisor, field worker, crew, PCA)?
8. What is clearly NOT this Type (monitoring-only dashboards, whole-farm finance, VRA machine loops, single-domain tools)?

## Representative Products

| Product | Operating model | Why sampled |
|---|---|---|
| Agrivi 360 FMS (Farm Enterprise) | Europe-based farm management suite for enterprise farms/agribusiness; crop-production planning at the center | Planning/knowledge pole: crop plans by crop and field, activities/work orders, cost per activity, compliance reporting |
| Croptracker | North America specialty-crop (fruit & vegetable) record-keeping and operations platform | Records-first pole: spray/practice/harvest records, crew labor, worker-safety intervals, food-safety traceability, GAP audits; publishes a literal "Why Use Crop Management Software?" page |
| Semios | North America specialty-crop (tree crop/vine) monitoring-and-intervention service | Monitoring pole: self-named "Semios Crop Management Platform"; sensor networks, pest/disease models, spray timing, alerts, field services |
| Cropin Grow (SmartFarm Plus) | India-origin enterprise agri-food platform; farm digitization for agribusinesses/development/governments | Enterprise multi-grower pole: geotagged plots, activity logs, PoP advisories, multi-farm hierarchy, roles from C-suite to farmer |
| Bushel Farm (formerly FarmLogs) | US row-crop farm management + finance | Boundary check only: field activity records exist but center of gravity is farm business (grain contracts, profitability, banking) — the Farm Management Platform pattern |

## Sources

All fetched 2026-09-07.

Agrivi:

- https://www.agrivi.com/ (positioning; product family)
- https://www.agrivi.com/products/ (FMS tiers: Farm Insights / Farm Enterprise / Farm Advisory / Agriculture Supply Chain; Traceability; IoT Connect)
- https://www.agrivi.com/products/360-farm-enterprise/ (crop planning by crop and field; real-time field insights; work management; cost per crop/field/activity; compliance ISO 9001/Global GAP/HACCP; case-study quotes)

Croptracker:

- https://www.croptracker.com/ (four pillars: record-keeping, scheduling, work crew, analytics; traceability)
- https://www.croptracker.com/product/farm-management-software.html (feature set: spray records, harvest yield records, production practice tracking, labor, field mapping/planting, packing/shipping/storage/QC, GAP reports, API)
- https://www.croptracker.com/why-use-crop-management-software.html (PHI/REI auto-calculation and entry warnings; traceability event system from planting to shipping; season-over-season; audits)

Semios:

- https://semios.com/ (solutions: climate, pest, disease, frost, irrigation, plant stress, reporting, field services; specialty crops)
- https://semios.com/solutions/reporting-tools/ ("Semios Crop Management Platform" self-naming; weekly reports; threshold alerts; historical records)
- https://semios.com/solutions/insect-pest-management/ (automated camera traps; pest pressure alerts; site-specific pest models; degree-day modelling and forecast; spray timing; variable-rate mating disruption)

Cropin:

- https://www.cropin.com/ (Cropin Cloud family)
- https://www.cropin.com/cropin-grow-smartfarm-plus/ (geotag plots, crop detection, input usage, remote crop health; advisories, pest alerts, activity logs; workflows/task assignment; PoP; roles; audience)

Bushel Farm (boundary check):

- https://www.bushelfarm.com/ (farm management + finance positioning; field activity records; grain contracts; machine-data integrations)

Evidence-layer legend below: **A** = directly observed on an official page of one product; **B** = observed across multiple sampled products.

Source-access limitation: no Tier-1 help centers were reached in this pass (Croptracker how-to videos and Bushel's knowledge base were not fetched; Agrivi, Cropin and Semios expose no reachable operational manuals at the URLs tried). All evidence is Tier-2 official product/solution pages. No precise operational numbers are asserted beyond what those pages state.

## Product A — Agrivi 360 Farm Enterprise

### Key observations

- Positioning: "farm management software enabling large agribusiness companies to control complex farm operations, make data-driven decisions, optimize cost and improve yields" (A).
- "Advanced Crop Planning: plan better and budget your season with precision based on a 360 overview of agronomic, financial and operational plans by crop and field" (A).
- "Real-Time Field Insights: real-time insights into weather conditions, pest risk and crop health by field. Analyze satellite data and operations management data by field" (A).
- "Powerful Farm Analytics: gain deep insights into best performing fields, varieties and practices" (A).
- Work management (FAQ): "monitor operations, assign and track employee responsibilities, and standardize processes across your organization"; "platform empowers agronomists and farm managers... continuously monitoring crop performance, health, and nutrition... detect potential risks early" (A).
- Cost tracking (FAQ): "tracking real-time costs by crop, field, or activity... optimize input usage (like fertilizers, seeds, pesticides, and water), better plan labor and machinery allocation" (A).
- Compliance (benefit): "complete crop production traceability and secure compliance with food quality, food safety and sustainability standards such as ISO 9001, Global GAP and HACCP" (A).
- Integrations: machinery, weather stations, soil sensors, ERP via Open API (A).
- Case-study voice (farm agronomist): "If I need information about some activity I did a few days ago on the field, the data is there in a few clicks" (A) — activity records as the operation's memory.
- Case-study voice (production director): "easier communication of work orders and offer automatization of reporting to comply with international certificates" (A).
- Case-study voice: "calculates the cost every time you use the fertilizer... better insight into how much you are spending during your season" (A).

## Product B — Croptracker

### Key observations

- Self-description: "a record-keeping and operations management service" for "growers, packers, co-operations and associations" of fruit and vegetables (A).
- Four pillars: Record-Keeping ("spray, employee, harvest, irrigation, and other production practice records"), Scheduling ("create your own schedules quickly and easily or choose from thousands of schedule templates"), Work Crew Communications & Activity Tracking, Analytics & Reports ("more than 50 reports"; "over 80 generatable reports" on the why-use page) (A).
- Spray records: "Record chemical and fertilizer applications and analyze input usage, efficacy and costs over time"; chemical inventory with "automatic withdrawals"; "Alert workers of safe re-entry and pre-harvest intervals before they enter an area"; "auto-calculate your tank mix, chemical amounts, and PHI and REI times"; "receive notifications when the PHI and REI intervals end, and be warned if you try to schedule a production practice in an area that is not yet safe for entry" (A).
- Harvest yield records: "Record your harvest and track inventory in real-time as it comes in"; "Link location and picker information to harvested inventory"; "Track yields over the season and know your best-performing blocks and commodities" (A).
- Production practice tracking: "Record work done on your farm including pruning, mowing, thinning, cleaning and more. Add custom activities and link to employee performance records. Log tasks down to the row"; "Track labor and equipment costs and analyze profitability" (A).
- Field mapping and planting: "Map your growing areas... Creating field and row boundaries... Quickly replant and edit growing areas for up to date rotation records. Mark hazards, irrigation zones, field borders" (A).
- Traceability: "tracking of products right from planting through sprays, harvesting, packing and shipping with a simple event system"; "trace a product back to the exact originating block and responsible person"; GlobalGAP and FSMA named (A).
- Season-over-season: "Verify best management practices - monitor changes and results season over season" (A).
- GAP reports and audits: "digitized collection of Good Agricultural Practice compliance forms"; "Centralize your logs and records for easy access at audit time" (A).
- Labor: hourly and piecemeal rates, piece-rate calculation "including minimum wage top-ups", payroll export (A).
- Post-harvest modules: harvest field packing; produce packing traceability ("Traceability Lot Codes", "Key Data Elements at Critical Tracking Events"); shipping (labels, BOLs, waybills); inventory receiving; storage records (CA and cold storage rooms); quality control templates (A).
- Computer-vision add-ons: Harvest Quality Vision (fruit size/color), Crop Load Vision (pre-harvest yield estimation), Starch Quality Vision (apple starch grading) (A).

## Product C — Semios

### Key observations

- Self-naming: "the Semios Crop Management Platform" (A, reporting-tools page).
- Positioning: "on-farm solutions backed by trusted field services... help you produce a better crop and ease your labor burdens"; "one partner for pest, weather, and irrigation solutions" (A).
- Monitoring solutions: in-canopy climate monitoring, insect pest management, disease management ("anticipate and pinpoint disease risk"), frost management, irrigation management, plant stress monitoring (A).
- Pest machinery: automated camera traps ("images and summaries of daily trap catches at the click of a button"; "prioritize hot spots"); pest pressure alerts ("Set thresholds for any block or trap and get notifications straight to your phone... to improve application timing"); "Pest models customized to your orchard... site-specific pest models to fine-tune sprays"; "Pest-degree days modelling and forecast... accurately time sprays" (A).
- Intervention execution: variable-rate mating disruption ("maximum pheromone release when your crop is most at risk"; pheromones certified for organic and conventional production) (A).
- Reporting: "automatic email updates and SMS alerts"; weekly report summarizing "weather, pest, disease, water, and crop development updates"; customizable alert recipient lists; "Track and view historical data"; shareable reports for internal and external parties (A).
- Field services: professional installation and maintenance of the device network (A).
- Crops: specialty perennials — almonds, apples, cherries, citrus, grapes, pears, pistachios, stone fruit, walnuts (A).
- User voices: farm operations manager (spray timings, frost alerts, soil moisture, per-block temperature mapping); Pest Control Advisor (prioritize which areas to visit by trap catch) (A).

## Product D — Cropin Grow (SmartFarm Plus)

### Key observations

- Positioning: "farm digitization and business intelligence solution... a comprehensive and highly configurable farm management platform"; "digitize the entire cultivation process" (A).
- Key features: "Geotag plots, detect crops, and track input usage with remote crop health monitoring"; "Share weather advisories, set pest alerts, and manage activity logs for timely interventions"; "Create workflows, assign tasks, and leverage customizable dashboards" (A).
- Farmer-facing outputs: "Crop advisory on the package of practices (PoP); Crop-specific activity schedule; Permissible agrochemicals for operations; App/SMS notifications for crop and weather advisory" (A).
- Roles: C-suite ("multi-farm hierarchical management", "early warning for deviation"), supervisors ("agent tasks monitoring", "early problem detection"), field users ("capture data configured by agronomist", "communicate crop instructions"), farmers (advisories) (A).
- Compliance/sustainability: "PoP adherence, monitor carbon credits"; traceability named as a benefit (A).
- Audience: farming companies, agri-input companies, seed production, food processing, development agencies, government organizations, agri-insurance, commodity traders (A).

## Product E (boundary check) — Bushel Farm (formerly FarmLogs)

### Key observations

- Positioning: "farm management software gives you a ground-level and big-picture view of your farm's operational and financial performance" (A).
- Field activity records exist ("field activity screen showing a fertilizing record"; "a faster, easier way to keep farm records"); machine-data integrations (John Deere Operations Center, Climate FieldView) reduce manual entry (A).
- Center of gravity: grain contracts ("Track unsold bushels as prices change"; import "from over 3,500 grain and ag retail facilities"), field-level profitability, rainfall notifications per field, price alerts, and banking (Bushel Business Account) (A).
- Verdict: the crop-cycle record layer is present, but the product's center is farm business operations, grain marketing and finance — the Farm Management Platform pattern. Used as boundary evidence only.

## Cross-product Comparison

| Structure | Agrivi | Croptracker | Semios | Cropin Grow | Evidence |
|---|---|---|---|---|---|
| Crop on identified field/plot/block as managed unit | ✔ crop × field plans | ✔ blocks/rows | ✔ blocks/orchards | ✔ geotagged plots | B |
| Season/cycle plan or schedule of operations | ✔ crop plans by crop and field | ✔ schedules + template library | ✔ spray-timing tools (model-driven) | ✔ crop-specific activity schedules | B |
| Recorded field operations (inputs, care work) | ✔ activities/work orders, cost per activity | ✔ spray + practice records to the row | partial (historical records; depth not visible) | ✔ activity logs | B |
| In-season crop condition visibility | ✔ weather, pest risk, crop health, satellite | ✔ crop health notes (light) | ✔ core (climate/pest/disease/frost/water/stress) | ✔ remote crop health monitoring | B |
| Risk alerts / advisories to act | ✔ pest-risk insights | ✔ worker-safety interval alerts | ✔ threshold alerts (email/SMS) | ✔ weather/pest advisories (app/SMS) | B |
| Execution assignment (workers/crews/tasks) | ✔ assign & track responsibilities, work orders | ✔ crews, tasks, labor tracking | ✖ (device field services instead) | ✔ workflows, task assignment | B (3/4) |
| Harvest/yield closure + performance analytics | ✔ best fields/varieties/practices | ✔ yields, best blocks/commodities | not visible | ✔ predictable outputs | B (3/4) |
| Season-over-season history | ✔ analytics across seasons | ✔ season over season | ✔ historical data | ✔ multi-season digitization | B |
| Compliance/audit reporting | ✔ ISO 9001/Global GAP/HACCP framing | ✔ GAP/GlobalGAP/FSMA audits | ✔ external reporting | ✔ PoP adherence, traceability | B |
| Field/plot mapping with boundaries | ✔ field analytics by field | ✔ GIS field/row mapping | ✔ per-block maps/heatmaps | ✔ geotagged plots | B |
| Input/product linkage & inventory | ✔ input costs | ✔ chemical inventory auto-withdrawal | ✖ | ✔ input usage tracking | B (3/4) |
| Sensor/IoT + models | ✔ IoT integrations | ✖ | ✔ core (traps, degree-days, disease models) | ✔ satellite/remote sensing | B (3/4) |
| Labor/crew management depth | ✔ responsibilities | ✔ deep (piece rates, payroll export) | ✖ | ✔ agent tasks | B (3/4) |
| Post-harvest traceability chain | ✔ traceability product line | ✔ packing/shipping/storage | ✖ | ✔ Trace product line | B (3/4) |
| Multi-grower/enterprise hierarchy | ✔ enterprise farms | ✔ co-ops/associations | ✖ (grower-side) | ✔ multi-farm hierarchy, many farmers | B |
| Knowledge layer (templates/PoP/models) | ✔ agronomy heritage | ✔ schedule templates | ✔ site-specific pest models | ✔ PoP advisories | B |
| Whole-farm finance/grain marketing | partial (budgets/costs) | ✖ | ✖ | ✖ | Bushel only (boundary) |

## Canonical Model

```text
Farm / operation registry
└── Field / plot / block (the land unit, with boundaries)
    └── CROP-SEASON (the managed unit of record: a crop/variety grown on that land for one season/cycle)
        ├── Cycle plan / schedule (what operations, when — hand-built, template-, knowledge- or model-informed)
        ├── Operation & observation records (planting, input applications, care work, scouting,
        │     irrigation, harvest — dated, attributed, location-anchored)
        ├── In-season state & risk (weather, pest/disease pressure, crop health, growth stage —
        │     monitored, modeled, alerted)
        └── Closure & history (harvest/yield outcome, performance vs plan, retained season-over-season)
```

### L0 — Defining Invariant

1. **The crop-season as the managed unit of record** — an identified crop (variety) grown on an identified field/plot/block through a defined season or cycle; plans, records, observations and outcomes all attach to it. Remove → generic land records or task lists.
2. **Planned/scheduled crop operations** — the cycle is directed by a plan or schedule of operations (what will be done to the crop, when), whether hand-built, template-driven, knowledge-driven or model-driven. Remove → a pure record log or monitoring dashboard.
3. **Recorded operations and observations on the crop** — dated, attributed records of what was done and seen through the cycle (planting, input applications, care work, scouting, harvest). Remove → a planning/calendar tool with no memory.
4. **Cycle closure with retained season history** — the season ends in a recorded outcome (harvest/yield) and the record persists as season-over-season history that informs the next cycle. Remove → one-shot planning or logging calculators.

Historical check (§24-style): the pre-digital pattern — planting plan + spray log + field notebook + yield book — satisfies all four (the plan may live in the farmer's head, but the scheduled/recorded operations and the retained season books are the structure). Early desktop farm record-keepers also fit. The definition therefore does not depend on cloud, mobile, sensors, satellite, imagery, or AI.

### L1 — Common Mature Structure

- Field/plot/block registry with boundaries (GIS mapping; rows/blocks; hazards; irrigation zones)
- Crop/variety catalog; rotation tracking
- Input/product catalogs with inventory linkage (chemical inventory, automatic withdrawal on application)
- In-season crop condition monitoring: weather, pest/disease pressure, crop health (sensors, satellite/imagery, scouting), growth stage
- Risk alerts and advisories (threshold-based notifications; spray-timing tools; weather advisories)
- Task/work management: assign operations to workers/crews/contractors, status tracking, mobile capture
- Labor and cost tracking per crop/field/activity (hours, piece rates)
- Harvest/yield records and performance analytics (best blocks/varieties; planned vs actual)
- Compliance/audit reporting (spray records, GAP/GlobalGAP/FSMA-style audits, traceability chains)
- Reports/dashboards; multi-season comparison
- Mobile apps; integrations (machinery data, sensors/weather, ERP)

### L2 — Variant / Optional Structure

- Crop segment: row crops (field-scale, machine-data heavy) vs specialty/perennial horticulture (block/row-level, crew-heavy, food-safety heavy) vs smallholder/contract-farming plots (geotagging, SMS advisories)
- Operating side: grower-operated vs enterprise/processor-operated (managing many growers/plots) vs service-provider-operated (monitoring + field services)
- Monitoring depth: records-first vs sensor/model-first vs satellite/remote-first
- Knowledge layer depth: schedule templates, PoP libraries, site-specific pest/disease models
- Post-harvest extension: packing, storage, shipping traceability
- Compliance regime: food safety (GAP/FSMA), certification (GlobalGAP, organic), sustainability/carbon
- Deployment: SaaS subscription vs enterprise suite vs development-sector program deployments

### L3 — Vendor-specific (Research Notes only)

- Croptracker: PHI/REI auto-calculation with entry warnings; Traceability Lot Codes / Key Data Elements / Critical Tracking Events (FSMA 204 vocabulary); Harvest Quality Vision / Crop Load Vision / Starch Quality Vision computer-vision products; piece-rate minimum-wage top-ups; "over a billion pounds of produce annually"; 80+ reports; hourly backups replicated across 3 continents retained 180 days.
- Semios: automated camera traps; variable-rate mating disruption with pheromones certified for organic production; site-specific vs regional pest models; degree-day flight prediction; chill-hours/bee-hours regional reports; field-services installation; Greenbook labels/SDS linkage.
- Agrivi: 360 FMS product tiers (Farm Insights / Farm Enterprise / Farm Advisory / Agriculture Supply Chain); AI Engage (white-label WhatsApp/Viber AI advisor); QR-code consumer traceability; ROI claims (8–12 USD per 1 USD invested).
- Cropin: SmartFarm Plus naming; Package of Practices (PoP); crop detection from imagery; OrbitAI/Sage/Data Hub/Trace product family; Agristack digital public infrastructure positioning; Forrester TEI claims.
- Bushel: grain-contract import from 3,500+ facilities; Bushel Wallet banking (The Bancorp); John Deere Operations Center / Climate FieldView integrations.

## Vendor-specific Findings

None of the L3 items entered the canonical model. The clearest cases: worker-safety interval automation (PHI/REI) is Croptracker-specific in this sample (regulatory in origin, product-specific in implementation); sensor/model machinery is Semios-specific in depth; PoP advisories are Cropin-specific vocabulary; grain-contract marketing is Bushel-specific and belongs to the neighboring Type.

## Boundary Findings

1. **vs Agronomy Management (§20 sibling; joint-review flag DISCHARGED from this side)**: agronomy management centers the input-decision practice (field test data → professional recommendation → execution record); crop management centers the crop-cycle operation record (plan → execute → record → monitor → harvest). Both sit on the same field record and vendors legitimately span both (Agrivi embeds agronomic knowledge; the agronomy pass's Agworld ships both plans and records). Structural test: remove the recommendation/test-data loop → crop management remains (the season's operation record is intact); remove the season's operation record → agronomy management remains (recommendations + test data). In crop-management products, agronomic knowledge appears as plan inputs (templates, PoP, models), not as the professional recommendation artifact. Gradient; no taxonomy change.
2. **vs Farm Management Platform (§20 sibling)**: center-of-gravity gradient. Bushel Farm (boundary sample) carries field activity records but centers farm business: grain contracts, field-level profitability, banking. Test: remove crop-cycle records → farm management remains; remove whole-farm business ops (finance/grain/payroll) → crop management remains. Consistent with the agronomy pass's flag. Flagged for joint review when Farm Management Platform is processed.
3. **vs Precision Agriculture Platform (§20 sibling)**: precision-ag centers the variable-rate execution loop (prescription → machine → as-applied verification) with equipment data as first-class; crop management centers the season's operations at crop level. Machine-data integration is common in crop management but VRA execution is not the center. Gradient; flagged for joint review when Precision Agriculture Platform is processed.
4. **vs Agricultural IoT Platform (§20 sibling)**: a sensing backbone without the crop-operation record is the IoT pattern. Semios is the closest pole inside this Type — it carries the "Crop Management Platform" self-label, historical records, spray-timing decisions and intervention execution — but a pure sensor dashboard would fall outside. Center-of-gravity test: the crop-season operation loop vs the device fleet. Consistent with the agricultural-iot pass's irrigation flag. Flagged for joint review.
5. **vs single-domain siblings — Irrigation Management / Crop Protection Management / Nutrient Management / Soil Management (§20)**: these center one input domain or operation class; crop management integrates all operation classes across the cycle. Sampled evidence of the superset pattern: Croptracker ships spray records (crop-protection records) as one module; Semios ships irrigation management as one solution. Probable superset/capability relationship; flagged for joint review when those leaves are processed (extends the agronomy pass's flag).
6. **vs Harvest Management (§20 sibling)**: harvest is one phase of the crop cycle; harvest management centers the harvest operation itself. Croptracker ships a dedicated Harvest Management product beside its farm-management platform — direct evidence that harvest can stand alone; crop management treats harvest as the cycle's closing phase. Flagged for joint review when Harvest Management is processed.
7. **vs Field Management (§20 sibling)**: field management centers the land unit as a persistent asset (boundaries, soil, infrastructure); crop management centers the crop-season on that land. Field mapping appears in crop management as substrate (Croptracker field mapping). Flagged for joint review when Field Management is processed.
8. **vs Orchard / Greenhouse / Vineyard Management (§20 crop-specific siblings)**: Croptracker ships a dedicated Orchard Management product — the crop-management pattern scoped to perennial tree crops. Probable variant-or-sibling question (crop-type scoping vs independent Type); flagged for joint review when those leaves are processed.
9. **Naming observation**: "crop management" is used loosely — Semios names its platform "Crop Management Platform", Croptracker publishes "Why Use Crop Management Software?", while many structurally identical products market as "farm management software". The leaf is the crop-cycle-structured segment of agricultural software, defined by structure (crop-season + operation loop), not vocabulary. No taxonomy change proposed.

## Uncertainties

1. No Tier-1 help centers reached for any sampled product in this pass; all evidence is Tier-2 official product/solution pages. Operational mechanics (exact record schemas, workflow states, permission models) are asserted only at the level the pages state.
2. Semios's operation-record depth (whether spray/application records are kept as first-class records) is not visible on public pages; only "historical records" and reporting are documented. Kept weak.
3. Cropin Grow's activity-log and workflow mechanics are marketing-level; PoP/schedule internals not directly observed.
4. Agrivi's activity/work-order model is evidenced by product page + case-study quotes, not by operational docs.
5. The exact split vs single-domain siblings and crop-specific siblings (Orchard/Greenhouse/Vineyard) cannot be resolved without processing those leaves; recorded as flags, not resolved unilaterally.
6. Row-crop pole under-sampled: Bushel Farm was used as boundary evidence only; a dedicated row-crop crop-management sample (e.g. John Deere Operations Center) was not fetched. The row-crop variant description is therefore calibrated weaker.

## Final Synthesis

Crop Management is the software of the **crop cycle**: its world is a registry of fields/plots/blocks carrying **crop-seasons** — a defined crop grown on an identified piece of land for one season — each directed by a **plan/schedule of operations**, executed and captured as **dated, attributed operation and observation records** (planting, input applications, care work, scouting, harvest), watched through **in-season crop state and risk** (weather, pest/disease pressure, crop health) that triggers alerts and adjustments, and closed with a **harvest/yield outcome retained as season-over-season history** that informs the next cycle. Everything else commonly bundled — field mapping, input inventories, crew/labor management, compliance and audit reporting, traceability chains, sensor networks and models, satellite monitoring, post-harvest modules — is common mature or segment-specific structure. The Type's identity is the managed crop-season loop; remove the crop-season unit and the operation record and the remainder is a monitoring dashboard, a farm ledger, or a task list — other Types.
