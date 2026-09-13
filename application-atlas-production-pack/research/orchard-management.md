# Research Notes — Orchard Management

Research date: 2026-09-09
Leaf: Orchard Management (Directory §20 Agriculture, Food & Natural Resources)
Slug: orchard-management

## Research Goal

Understand "Orchard Management" as an Application Type: what its managed object is, who runs it, how the perennial production cycle is organized in real products, where its boundaries sit against the neighboring already-processed Types (crop-management, field-management, farm-management-platform, harvest-management, farm-labor-management, crop-protection-management, irrigation-management, greenhouse-management) and unprocessed siblings (vineyard-management, nursery-management), and — explicitly — whether the leaf is a genuine Type or a crop-type-scoped variant of Crop Management.

**Prior-pass flags this pass must address:**

- crop-management research (2026-09-07) §Boundary 8: "Croptracker ships a dedicated Orchard Management product — the crop-management pattern scoped to perennial tree crops. Probable variant-or-sibling question (crop-type scoping vs independent Type); flagged for joint review when those leaves are processed."
- harvest-management research (2026-09-08) comparison table: "Orchard / Vineyard Management | crop-scoped management variants; harvest appears as one phase | leaf-level distinction; harvest management is crop-agnostic within specialty/high-value."

## Initial Boundary (hypothesis before research)

- Core use hypothesis: grower-side management of perennial tree-fruit/nut production — the orchard block/tree as a long-lived asset, multi-year cycle (planting → non-bearing → bearing → renewal), orchard-specific operations (pruning, thinning, training, grafting, spray, irrigation, pollination), harvest as recurring annual outcome.
- Users hypothesis: orchard owners/growers, orchard managers, crew leaders, packers who grow, agronomists.
- Nearest Types: Crop Management (season-centric generic), Vineyard Management (grape sibling), Nursery Management (propagation for sale), Farm Management Platform (whole-farm), Harvest Management (harvest operation), Farm Labor Management (crew/piece-rate machinery), Crop Protection Management (spray domain).
- Unknowns: does a distinct orchard-specific product population exist? Is tree-level identity definitional or optional? How deep does the perennial-asset structure go? How is harvest/packing packaged?

## Research Questions

1. What is the managed object — orchard? block? row? tree? What identity attributes (variety, rootstock, planting year, spacing, area, tree count)?
2. How is time modeled — multi-year asset life vs annual season? Establishment → bearing → replanting?
3. Which operations are recorded against the asset (pruning, thinning, training, grafting, spray, irrigation/fertigation, nutrition, mowing, pollination)?
4. How is harvest handled — yield per block/variety, quality, integration with harvest operations/packing?
5. What monitoring/decision support is bundled (weather, disease/pest models, sensors, imagery)?
6. What compliance/records machinery (spray records, GAP/food-safety audits, traceability to block)?
7. What labor machinery (crews, piece rates for pruning/thinning/picking, payroll)?
8. What interfaces (block map, tree/row lists, season dashboard, mobile capture)?
9. Boundaries: vs Crop Management (the flagged joint review), vs Vineyard Management, vs Nursery Management, vs Farm Management Platform, vs Harvest Management, vs Farm Labor Management, vs Crop Protection Management, vs monitoring Types.

## Representative Products

| Product | Origin / segment | Why selected | Evidence reached |
|---|---|---|---|
| Hectre | New Zealand/Australia origin, sold to US/global orchard growers and packers (apples, cherries, pears, citrus, stone fruit) | Orchard-native self-label ("orchard management and fruit quality software"); operational pole (harvest/labor/quality); deep help center | Tier 1: root, orchard-management product page, help center (5 articles) |
| Croptracker | Canada; fruit & vegetable growers, orchard lineage ("first developed for orchard management", "20 years supporting tree fruit and nut growers") | Dedicated "Orchard Management Software" product page; records/compliance pole; vision tools | Tier 1: root, orchard page, farm-management page |
| Semios | North America; almonds/citrus/pome/stone permanent crops | Monitoring/IPM pole — boundary specimen (orchard-segment platform whose center is sensing, not the asset record) | Tier 1: root |
| FruitWeb | Germany (Jork); pome/stone fruit growing (Obstbau) | European regional decision-support pole — boundary specimen (weather stations + disease/pest forecast models + frost warning) | Tier 1: root |
| Agrivi | Croatia/global; enterprise farms | General-FMS angle — how generic farm management treats tree fruit ("Tree Fruit" crop fit) | Tier 1: root, 360 Farm Enterprise page |
| Agworld | Australia/US; part of Semios group | General-FMS angle — field/plan/record model, fruit clients visible | Tier 1: root |

Rejected / unreachable (recorded, not used as evidence):

- **FarmSoft** (farmsoft.com, with and without www) — 403 both attempts. Known from market presence as an orchard/fruit-management suite; **no claims about its structure are made in this pass.**
- **AgCode** (agcode.com, with and without www) — transport error both attempts.
- **PTx/Trimble Agriculture** (agriculture.trimble.com) — transport error, one attempt, not retried.

## Sources

Fetched 2026-09-09 (all Layer A unless noted):

- Hectre — root: https://hectre.com/ ; orchard management product page: https://hectre.com/products/farm-management-software/ ; help center root: https://hectre.helpscoutdocs.com/ ; "Add Orchards Location Details": https://hectre.helpscoutdocs.com/article/135-add-orchards-blocks-sub-blocks ; "Getting Started | Managers": https://hectre.helpscoutdocs.com/article/264-getting-started-managers ; "Record Pruning / Thinning Jobs": https://hectre.helpscoutdocs.com/article/64-recording-pruning-thinning-jobs ; "Harvest Maps": https://hectre.helpscoutdocs.com/article/272-harvest-maps ; "Add Varieties": https://hectre.helpscoutdocs.com/article/134-add-varieties ; Spray category: https://hectre.helpscoutdocs.com/category/292-spray
- Croptracker — root: https://www.croptracker.com/ ; Orchard Management Software: https://www.croptracker.com/product/orchard-management-software.html ; Farm Management Software: https://www.croptracker.com/product/farm-management-software.html
- Semios — root: https://semios.com/
- FruitWeb — root (EN): https://fruitweb.info/en/
- Agrivi — root: https://www.agrivi.com/ ; 360 Farm Enterprise: https://www.agrivi.com/products/360-farm-enterprise/
- Agworld — root: https://www.agworld.com/

In-repo prior research cross-referenced (Layer B context, not new fetches):

- research/crop-management.md (boundary flag 8; comparison row "✔ blocks/orchards"; variant list "perennial orchard")
- research/harvest-management.md (Hectre observations; boundary row vs Orchard/Vineyard Management)
- research/farm-labor-management.md (orchard/vineyard blocks + rows as labor anchors; historical check)
- research/logging-operations-management.md (annual crop cycles vs multi-year stands — structural analogy)
- STATUS.md entries for crop-management, field-management, farm-management-platform, harvest-management, farm-labor-management, crop-protection-management, irrigation-management, greenhouse-management

## Product Observations

### Hectre (evidence layer A — root + product page + 5 help articles)

- Positioning: "The orchard management and fruit quality software that growers and packers love to use." Product families: **Orchard Management** (Harvest, Timesheets, Payroll, Analytics Pro, QC/Hectre App) and **Fruit Quality AI** (Fruit Sizing, Color Grade). Crop types: Apples, Cherries, Pears, Citrus, Stone Fruits. Solutions split: Growers / Packers.
- Orchard Management suite framing: "Clock in workers, track agrochemical use, record harvest in real-time, and access detailed performance and cost insights, automating payroll calculations."
- **Asset structure (help, "Add Orchards Location Details")**: Admin → Orchards; hierarchy **Orchard/Ranch → Block → Sub-block → Rows → Tree numbers**. Block carries **Variety** (multiple varieties per block; each variety represented as a Sub Block) + optional land area + payroll cost code. Orchard carries optional industry code (PIN) and payroll cost code. Rows added to sub-blocks "for recording tree-specific piece rate jobs such as pruning or thinning"; row 0 / tree 0 shortcut when volume is needed without row/tree specificity.
- **Variety catalog (help, "Add Varieties")**: varieties added first, with **Fruit Type**; assigned to orchards "so that you can record variety-specific jobs"; optional packout/price/weight details.
- **Tree-shaped work (help, "Record Pruning / Thinning Jobs")**: clock in staff to a pruning/thinning job; select rows (green = all trees in row previously completed for that job type; orange = some); assign workers to rows; optional **piece rate per tree**; at clock-out, "Update Rates and Rows" to input how many trees each worker completed; multiple workers per row split trees evenly ("Add Max Trees"); day summary shows average hourly rate, total trees pruned/thinned, minutes/tree. **"Once a tree is marked as pruned or thinned, it'll no longer be available in the Hectre app for that same job type"** — reset-trees machinery makes trees available again. Method 2 records tree volume to an unspecified row (row 0).
- **Harvest (help + product pages)**: bin ticketing ("fast logging of bins", "real-time crediting of buckets, lugs, and bins", scan existing bin tickets or create waterproof tickets on-the-go, bin counts for progress, "trace your fruit back to where it was picked"); cherry bucket module (per-picker buckets); bin QC (defects, pick quality and number); bin ticket customization; bluetooth printers; treatments and export countries on bin dockets.
- **Harvest maps (help)**: dashboard map of picked bins (GPS from devices); bin record details: Bin ID, date picked, location, pickers, variety, recorder.
- **Analytics (product pages)**: "Real view of orchard performance, costs, production volume, fruit quality"; "Track key metrics such as cost per acre, bins per acre, and cost per bin by variety and block"; picker productivity (bins/hour), picking speed vs defect rate; notifications to supervisors.
- **Labor machinery**: timesheets (team + personal MyTimesheet), badge scanning, employee badges, pay types, minimum wage and account defaults, leave types, payroll exports/integrations; payroll module on dashboard.
- **Spray (help category)**: "Add Orchard Size", "Add Spray Settings", "Add a Spray Plan" — spray plans exist in-product (article bodies not fetched).
- **Setup sequence (help, "Getting Started | Managers")**: varieties → orchard details → (NZAPI settings, NZ only) → jobs → minimum wage/defaults → leave types → staff/modules/badges; then harvest details (bin/bucket pay rates, treatments/export countries, QC defects, pick quality/number, bin ticket customization, printer). Orchard manager value framing: "Know what, where, and by who jobs are being done in your orchards during each day"; visualize the pick with harvest maps; track picker performance; yield reports; job and location labor cost reports.
- **NZAPI mapping article title**: "Map NZAPI Production Sites, Management Areas and Varieties to Hectre locations" — industry-body data exchange (New Zealand Apples & Pears) mapped onto the product's location hierarchy (title-level evidence only).

### Croptracker (evidence layer A — root + orchard page + farm page)

- Positioning (orchard page): "Croptracker is the leading orchard management software system for growers of fruit and nuts." "Croptracker was first developed for orchard management and has been supporting tree fruit and nut growers to enhance their operations, increase their yields and productivity for over 20 years." Modular farm management system; "built for orchards of all sizes".
- Orchard-page feature set:
  - **Spray Record Keeping**: chemical and fertilizer applications; input usage/efficacy/costs over time; chemical inventory with automatic withdrawals; "Alert workers of safe re-entry and pre-harvest intervals before they enter an area."
  - **Harvest Yield Records**: record harvest and track inventory in real time; "Link location and picker information to harvested inventory"; "Track yields over the season and know your best-performing blocks and commodities."
  - **Production Practice Tracking**: "Record work done on your farm including pruning, mowing, thinning, cleaning and more"; custom activities linked to employee performance records; "Log tasks down to the row for detailed records"; labor and equipment costs, profitability.
  - **Work Crew Activity and Labor Tracking**: hourly and piecemeal pay rates; schedules; work crews; "Automate piece-rate calculations including minimum wage top-ups and performance bonuses"; payroll export formats.
  - **Field Mapping and Planting**: GIS growing-area mapping; field and row boundaries; **"Quickly replant and edit growing areas for up to date rotation records"**; hazards, irrigation zones, borders of any shape.
  - **Storage Records**: storage sites and rooms "including CA and cold storage rooms"; scan inventory tags into rooms; lots before/after packing; traceability with timestamps.
  - **GAP Reports and Audits**: digitized Good Agricultural Practice compliance forms; centralized logs for audit time.
  - **Quality Control**: digital QC templates; quality/food-safety metrics linked to inventory and locations.
  - **Vision products**: Harvest Quality Vision™ (fruit size/color in-bin scans), Crop Load Vision™ (count/size fruit "on the tree, bush or vine" pre-harvest yield estimation), Starch Quality Vision™ (apple starch-pattern/iodine assessment for harvest timing and storage grouping).
- Farm-management page framing: "Specialty crop production… You manage dozens of varieties with different spray schedules, coordinate crews across multiple harvest windows, and **trace every bin from block to buyer**." Adds Harvest Field Packing, Produce Packing Traceability Records (Traceability Lot Codes, KDEs at CTEs), Shipping Traceability Records, Inventory Receiving, API integration.
- Customer logos on orchard page: orchard/fruit co-ops and growers (Algoma Orchards, Sandy Shore Farms, Mr Apple, Norfolk Fruit Growers, Ontario Tender Fruit, Scotian Gold, Ontario Apple Growers…).

### Semios (evidence layer A — root; boundary specimen)

- Positioning: "On-farm solutions backed by trusted field services"; footer: "a leader in crop protection and resource optimization technology, trusted by growers across North America to improve **orchard and vineyard** performance."
- Solution set: Climate Monitoring (in-canopy), Mating Disruption (variable-rate pheromone emitters), Insect Pest Management, Disease Management, Frost Management, Irrigation Management, Plant Stress Monitoring, Alert and Reporting Tools, Field Services (installation/maintenance by vendor technicians).
- Scale claims: 200,000 IoT devices serviced; 1.4M acres of mating disruption; 600,000 pests counted. Blog content is orchard-IPM-native (navel orangeworm in almonds, California red scale degree-days).
- Interpretation: the center is sensing + models + pheromone delivery + field service — monitoring/IPM machinery, not the orchard asset record. No block/tree registry, no work crediting, no payroll visible at root level. Used as the monitoring-pole boundary specimen.

### FruitWeb (evidence layer A — root; boundary specimen, European)

- Positioning: "specialists in processing weather data in fruit growing" (Obstbau). Products: weather stations + frost-warning devices (Frostwecker; wet/dry bulb, solar, 2-minute transmission), forecast models for diseases/pests of fruit growing (apple scab, fire blight, apple mildew, codling moth, apple blossom weevil, apple sawfly…), fruitweb App (models, frost warning, counselling messages, weather forecast/rain radar).
- Interpretation: regional (German-speaking fruit growing) decision-support service — weather-data machinery for orchard spray/frost decisions. No asset registry, no work records, no harvest crediting. Second boundary specimen.

### Agrivi (evidence layer A — root + enterprise page; general-FMS angle)

- Positioning: "360 Farm Management Software… supporting farmers with data-driven tools… precise agronomic and economic decisions." Enterprise page: central farm operations management ("digital twin of your farm"), advanced crop planning "by crop and field", real-time field insights (weather, pest risk, crop health by field), farm analytics ("best performing fields, varieties and practices"), machinery/IoT/ERP connectivity, traceability and compliance (ISO 9001, Global GAP, HACCP).
- **Crop fit list**: Berries, **Tree Fruit**, Root Vegetables, Tropical Fruit, Spices, Industrial Food — tree fruit is a crop-type specialization of a general FMS, not a separate asset model on the page evidence.
- Case study visible: Moslavina voce (fruit production company) — work orders, certificate compliance reporting.
- Interpretation: the general-FMS pole handles orchards as crop types within the field/season/activity model; no tree-level substrate visible at page level.

### Agworld (evidence layer A — root; general-FMS angle)

- Positioning: "Plan your crop, mitigate your risks, improve your profitability"; plan → recommendation → record → report loop; standardized data; audit-ready; budgeting; financial performance by crop/farm/field. Clients include fruit operations (Sundquist Fruit, De Bortoli Wines) among broad row-crop/livestock base. Part of Semios group.
- Interpretation: field/plan-centric general FMS; orchards absorbed into the same plan/record loop. Second general-FMS angle.

## Cross-product Comparison

| Dimension | Hectre | Croptracker | Semios | FruitWeb | Agrivi / Agworld (general FMS) |
|---|---|---|---|---|---|
| Orchard asset hierarchy | ✔ Orchard/Ranch → Block → Sub-block (variety) → Row → Tree | ✔ growing areas with field/row boundaries; blocks as yield anchor; replant/rotation edits | ✗ (sensing sites, not visible) | ✗ (stations/models) | fields/farms; crop × field (orchard as crop type) |
| Variety as first-class catalog | ✔ varieties + fruit type; variety-specific jobs | ✔ varieties/commodities ("dozens of varieties with different spray schedules") | crop-level | crop-level (pome/stone/soft fruit models) | crop templates (Tree Fruit) |
| Tree/row-level work recording | ✔ per-tree piece-rate pruning/thinning with per-tree completion state + reset | ✔ "log tasks down to the row" | ✗ | ✗ | ✗ (activity by field) |
| Perennial care operations recorded | ✔ pruning/thinning (tree-shaped); spray plans; (jobs catalog) | ✔ pruning, mowing, thinning, cleaning + custom activities; spray records | pest/disease/frost management (service-delivered) | model-driven advice | activities by crop/field |
| Spray machinery | ✔ spray plans/settings; agrochemical use tracking | ✔ records, inventory auto-withdrawal, REI/PHI alerts | IPM programs + mating disruption | forecast models → spray timing | recommendations → records |
| Harvest outcome credited to asset | ✔ bins/buckets per block/variety/picker; trace to where picked | ✔ yield records linked to location + picker; best-performing blocks | ✗ | ✗ | harvest as activity/yield data |
| Labor/payroll machinery | ✔ deep (timesheets, badges, piece rates, payroll exports) | ✔ crews, piece rates + min-wage top-ups, payroll exports | ✗ | ✗ | task assignment (light) |
| Quality machinery | ✔ QC defects, picker performance; fruit sizing/color AI | ✔ QC templates; size/color/crop-load/starch vision | ✗ | ✗ | ✗ |
| Compliance/food safety | treatments/export countries on bin dockets | GAP reports/audits; traceability lot codes; FSMA resources | reporting tools | ✗ | Global GAP/HACCP/ISO reporting |
| Monitoring/decision support | ✗ (not visible) | ✗ (vision ≠ monitoring) | ✔ core (sensors, models, emitters, field service) | ✔ core (stations, models, frost) | via integrations (IoT/meteo) |
| Packing/storage adjacency | packer solutions; packout analytics | storage rooms (CA/cold), field packing, packing/shipping traceability | ✗ | ✗ | supply-chain/traceability products (separate) |
| Multi-year continuity signals | persistent orchard/block/variety structure; year-over-year analytics | "quickly replant… rotation records"; yields over season(s) | perennial crop programs | perennial model suite | rotation/plans by season |

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The orchard planting as the persistent production asset of record.** An identified orchard/ranch → block hierarchy (commonly subdivided into variety sub-blocks and, where work granularity requires, rows and trees) carrying planting identity — variety (with fruit type), commonly area, and where kept, planting year/rootstock/spacing — persisting across seasons as the anchor to which work, inputs, and outcomes attach. Remove → land/field registry (Field Management) or season-scoped crop records (Crop Management).
2. **Perennial-cycle work recorded against the asset.** Dated, attributed, location-bound records of the orchard's care and protection operations — pruning, thinning, training, grafting/top-working, spray, irrigation/fertigation, nutrition — attached to block/row/tree, with tree-level granularity available as the working substrate for tree-shaped jobs (piece-rate pruning/thinning/picking with per-tree completion state). Remove → free-floating task log; the asset is no longer being managed.
3. **The season's production outcome credited to the asset.** Harvest/yield recorded per block/variety — commonly with picker/crew identity and quality context — accumulating into the asset's year-over-year performance history that informs the next cycle's decisions (and, where kept, renewal/replant decisions). Remove → registry + work log with no production loop.

Jointly-held load-bearing:

- 1 alone = land/asset registry (Field Management territory)
- 2 without 1 = free-floating work records
- 3 without 1+2 = bare yield log
- 1+2 without 3 = agronomy journal with no production loop
- 1+3 without 2 = registry + yield statistics, no work management
- 2+3 without 1 = records not bound to a persistent asset

### L1 — Common Mature Structure

- Variety catalog with fruit-type assignment; variety-specific job recording and reporting.
- Job catalog (job types) with pay-rate structures (hourly + piece rates: per bin/bucket/tree).
- Crew/staff machinery: timesheets (team + individual), badges, leave types, payroll exports/integrations; piece-rate calculation with minimum-wage top-ups where law requires.
- Harvest crediting machinery: bins/buckets/loads recorded at picking, credited to pickers, ticketed, traced to block.
- Spray plans and spray records with chemical inventory (auto-withdrawal) and safety-interval awareness (REI/PHI).
- Analytics by block/variety: yield, cost per acre, bins per acre, cost per bin, picker productivity; harvest maps (GPS bin records).
- QC machinery: defect/pick-quality capture, picker performance comparison.
- Compliance reporting: GAP/food-safety audit packs; treatments/export destinations on harvest records.
- Mobile field capture (offline-capable) + web dashboard split.

### L2 — Variant / Optional Structure

- Crop-type scope: pome fruit, stone fruit, cherries, citrus, nuts; some products extend to berries/vines/vegetables (fruit&veg generalization).
- Grower-packer extension: fruit sizing/color grading at packhouse, packout analytics, storage-room (CA/cold) records, packing/shipping traceability — adjacent to Produce Packing House Management.
- Monitoring/decision-support bundling vs integration: weather stations, disease/pest models, frost warning, soil/canopy sensors (the Semios/FruitWeb center) — adjacent Types' machinery.
- Pre-harvest estimation: crop-load counting/fruit-size vision; maturity/starch testing.
- Regional regime machinery: US piece-rate/minimum-wage top-ups and WPS-style spray records; EU treatment journals; NZ industry-body data exchange (NZAPI).
- Planning depth: season/production plans and budgets (records pole) vs none (operational pole).
- Deployment/scale: cloud SaaS multi-ranch enterprises vs single-orchard operations; desktop-era predecessors.

### L3 — Vendor-specific (kept out of the final document)

- Hectre: NZAPI production-site/management-area mapping; cherry bucket module; TopDown/HandHeld sizing products; Analytics Pro metric set; "3.8 billion pieces of fruit scanned" class marketing claims.
- Croptracker: Harvest Quality Vision™ / Crop Load Vision™ / Starch Quality Vision™ branded products; Predictive Packout Toolkit; FSMA-204 resource framing.
- Semios: variable-rate mating-disruption emitters; in-canopy sensor network + field-service model; Semios Hub dashboard.
- FruitWeb: Frostwecker device line; German-language forecast-model suite (Schorf etc.).
- Agrivi: AI Engage advisory products; 360 suite packaging.

## Anti-overfitting Checks

- **Tree-level identity is NOT definitional.** Hectre explicitly supports row-0/tree-0 volume recording ("if you want to record volume for a tree-specific job, but don't need to know the specific row numbers or tree numbers"); Croptracker logs "down to the row". The invariant is the block-level asset with planting identity; row/tree granularity is the common substrate for tree-shaped work, not a requirement.
- **Piece-rate/payroll machinery is NOT definitional.** Deep in Hectre, present in Croptracker; but the records pole could exist without payroll (and the general-FMS pole handles labor lightly). Held L1.
- **Fruit-quality/vision tools are NOT definitional.** Present in both orchard-native samples as branded optional products. Held L2/optional.
- **Spray machinery is NOT definitional as a separate structure** — it is one of the recorded operations (the crop-protection domain machinery is its own Type). Held L1 as common content of leg 2.
- **Season-plan/agronomy planning is NOT definitional.** Hectre's operational pole shows no season-plan object; Croptracker/Agrivi carry planning. Held L2.
- **Monitoring (sensors/models/frost) is NOT definitional.** The monitoring pole (Semios, FruitWeb) lacks the asset record entirely — proving monitoring alone does not make orchard management, and orchard management does not require bundled monitoring.
- **Packing/storage is NOT definitional.** Packer-side machinery is adjacent (Produce Packing House Management); present as optional extension in both orchard-native samples.
- **Cloud/mobile/GPS are NOT definitional** (historical check below).

## Historical / Market-Sample Check (§24)

Pre-digital orchard practice, assembled from the products' own before-state framings and standard orchard record-keeping practice:

- **Planting plan / block register**: orchard map or register naming each block with variety, rootstock, year planted, spacing, tree count — leg 1 on paper.
- **Spray logs / treatment journals**: dated, block-anchored, product-and-rate records kept for inspection (EU treatment-register tradition; US grower spray logs) — leg 2.
- **Pruning/thinning tallies**: crew sheets recording trees pruned or thinned per worker per block/row for piece-rate settlement — leg 2 (tree-shaped work).
- **Picking tally sheets / bin tickets**: per-picker counts of boxes/buckets/bins by block, settled at season's end — leg 3.
- **Per-block yield books**: year-over-year records of yield per block/variety informing renewal and management — leg 3's accumulated history.
- **Replanting records**: block renewal entries changing the planting register — leg 1's multi-year continuity.

All three legs satisfied with zero software-era machinery. Regional variants (European Obstbau treatment journals, plantation-style registers) satisfy the same shape. The definition names no mobile app, GPS, cloud, piece-rate law, or vision AI.

## Boundary Findings

1. **vs Crop Management — the flagged joint review, RESOLVED from this side.** The seam is the unit of record. Crop Management's unit is the crop-season (crop/variety × field × season, closed with season history); Orchard Management's unit is the persistent planting (block with variety identity that outlives every season, carrying age-dependent care and renewal). Three structural differences keep Orchard Management a distinct Type rather than a crop-type filter: (a) the asset persists across seasons while the crop-management unit is season-scoped; (b) the operation set includes asset-shaping work (pruning, thinning, training, grafting/top-working) whose object is the planting's structure and future crop load, with no analog in an annual cycle; (c) the working substrate extends to rows/trees with per-tree work state. Evidence that the population is real, not a marketing filter: Hectre is orchard-native with no season-plan object at all (its world is asset + jobs + harvest + people + money); Croptracker — the very product the crop-management pass cited — ships a **separate dedicated Orchard Management product page** beside its farm-management product, i.e., the vendor's own split. Residual overlap is honest: records-pole orchard products sit close to crop management, and general-FMS products (Agrivi, Agworld) absorb orchards as crop types within the season model. Both facts are recorded as the overlap zone, not as grounds for merging.
2. **vs Vineyard Management (unprocessed sibling).** Expected seam: vineyards bind blocks to winery-bound lots (harvest → crush → wine), a processing-oriented continuation orchards lack; orchards bind to fresh-fruit packhouse/traceability. Not resolved here — recorded for the vineyard pass.
3. **vs Nursery Management (unprocessed sibling).** Nursery propagates plants as sale inventory (plant lots, sizes, orders); orchard grows fruit for harvest from planted trees. The orchard's asset is the production system; the nursery's lot is the product. Recorded for the nursery pass.
4. **vs Farm Management Platform.** Whole-operation scope (land + livestock + finance + equipment, operator as principal) vs orchard-scoped production management. An orchard operation can be run inside a farm-management platform; the orchard Type exists where the planting asset and its tree-shaped work are the center.
5. **vs Harvest Management.** Harvest Management's center is the harvest operation (bin ticketing, crediting, campaign management, packhouse handoff) — crop-agnostic within specialty crops. Orchard Management's leg 3 is the asset's outcome record (yield credited to block/variety as performance history), not the operation machinery. Hectre straddles the seam (its Harvest line is harvest management proper; its orchard frame adds the asset + perennial work). The two Types interlock; neither subsumes the other.
6. **vs Farm Labor Management.** Crew/time/piece-rate machinery is shared and deeply realized in orchard products (tree-shaped piece work is the extreme case). The labor Type's center is the workforce record across the farm; the orchard Type's center is the asset. Orchard products embed labor machinery as L1.
7. **vs Crop Protection Management.** Spray records/REI/PHI/chemical inventory are the crop-protection domain's machinery; orchard products carry them as one recorded operation among many. The domain Type stands alone for spray-centric operations.
8. **vs monitoring Types (Precision Agriculture Platform, Agricultural IoT Platform, and monitoring services like the two boundary specimens).** Sensing/model-driven decision support is adjacent machinery: the monitoring pole lacks the asset record entirely (proving monitoring ≠ orchard management), and orchard products consume monitoring via integration or bundling without being defined by it.
9. **vs Field Management.** Field Management is the land-unit register (extent, soil, boundaries) — leg 1 alone. Orchard Management adds the planting (a crop asset ON the land) and the cycle around it.

## Uncertainties

- **FarmSoft** — a known orchard/fruit-management suite — was unreachable (403 ×2). No structural claims about it are made. Its absence means the "packing-integrated orchard suite" pole is represented only indirectly (via Croptracker's packing/storage modules and Hectre's packer solutions).
- **AgCode, Trimble Ag** unreachable (transport errors). Not used.
- Hectre's spray article bodies were not fetched (category titles only) — spray-plan mechanics in Hectre asserted at title level only.
- Whether a "pure agronomy, no-harvest" orchard product exists was not observed; leg 3 is kept because every sampled orchard-native product carries harvest outcome records. If such a product exists, leg 3 would need re-examination.
- Vineyard Management and Nursery Management are unprocessed; boundary statements 2–3 are provisional expectations, not resolutions.
- Rootstock/planting-year identity: visible in the domain's practice and implied by "replant/rotation records" (Croptracker) and variety/area identity (Hectre), but no sampled product page explicitly enumerated rootstock/planting-year fields at fetch level. The L0 therefore requires "planting identity (variety; commonly area)" and treats rootstock/planting year as common-but-unverified-at-fetch-level attributes.
- NZAPI mapping verified at article-title level only.

## Final Synthesis

Orchard Management is the orchard operation's system of record, organized around the orchard planting — the long-lived block of fruit or nut trees — as a persistent production asset. Its defining core is three jointly-held structures: the planting held as an identified, variety-carrying asset that outlives every season (orchard/ranch → block → sub-block/variety, extending to rows/trees where work granularity requires); the perennial cycle of care and protection work recorded against that asset (pruning, thinning, training, grafting, spray, irrigation, nutrition — with tree-level piece-rate work as the characteristic extreme); and each season's harvest credited back to the asset as block/variety yield accumulating into year-over-year performance history that informs the next cycle. Around this core, mature products add variety and job catalogs, crew/timesheet/payroll machinery, bin crediting and traceability, spray plans and records, block/variety analytics and harvest maps, QC, compliance reporting, and packer-side extensions. The Type resolves the crop-management pass's flag: it is a genuine sibling Type, not a crop-type filter — the unit of record (persistent planting vs season-scoped crop) and the operation set (asset-shaping perennial work) differ structurally, while the overlap zone (records-pole products, general-FMS absorption) is recorded honestly. Monitoring services, harvest-operation machinery, labor machinery, spray-domain machinery, and packing operations are adjacent Types that interlock with this one.
