# Research Notes — Vineyard Management

Research date: 2026-09-10
Leaf: Vineyard Management (Directory §20 Agriculture, Food & Natural Resources)
Slug: vineyard-management

## Research Goal

Understand "Vineyard Management" as an Application Type: what its managed object is, who runs it, how the perennial viticultural cycle is organized in real products, where its boundaries sit against the neighboring already-processed Types (orchard-management, crop-management, harvest-management, farm-labor-management, farm-management-platform, field-management, irrigation-management, crop-protection-management, precision-agriculture-platform, agricultural-iot-platform, crop-remote-sensing-platform, agricultural-gis) and unprocessed siblings (winery-management, nursery-management), and — explicitly — whether the leaf is a genuine Type or a crop-type-scoped variant of Orchard Management or Crop Management.

**Prior-pass flags this pass must address:**

- orchard-management research (2026-09-09) §Boundary 2: "vs Vineyard Management (unprocessed sibling). Expected seam: vineyards bind blocks to winery-bound lots (harvest → crush → wine), a processing-oriented continuation orchards lack; orchards bind to fresh-fruit packhouse/traceability. Not resolved here — recorded for the vineyard pass."
- orchard-management STATUS entry: "forward flags for UNPROCESSED vineyard-management (expected seam: vineyard blocks bound to winery-bound lots — harvest→crush→wine — vs orchard's fresh-fruit packhouse/traceability; to be ratified in that pass)".
- crop-management research (2026-09-07) §Boundary 8 (Orchard/Greenhouse/Vineyard "probable variant-or-sibling"): the orchard portion was discharged 2026-09-09 (keep-both ratified); the vineyard portion falls to this pass.
- harvest-management research (2026-09-08) comparison row: "Orchard / Vineyard Management | crop-scoped management variants; harvest appears as one phase | leaf-level distinction".

## Initial Boundary (hypothesis before research)

- Core use hypothesis: grower-side management of winegrape production — the vineyard block as a long-lived asset (variety/clone/rootstock identity), perennial viticultural operations (pruning, canopy management, spray, irrigation, nutrition), ripening tracked through maturity sampling, harvest as tons credited to blocks and delivered toward the winery (crush).
- Users hypothesis: vineyard managers/viticulturists, growers, crew supervisors, cellar/winery teams at estate wineries, vineyard management companies (contract growers), labour contractors.
- Nearest Types: Orchard Management (perennial sibling), Winery Management (downstream crush/fermentation), Crop Management (season-scoped generic), Harvest Management (harvest operation), Farm Labor Management (crew/piece-rate), monitoring Types (sensors/models).
- Unknowns: does a distinct vineyard-specific product population exist (vs orchard software generalized to vines)? Is the winery-bound fruit flow (weigh tags, fruit contracts, wine-lot traceability) definitional or pole-dependent? How deep does row/vine granularity go? Is the vintage a structural object or just vocabulary?

## Research Questions

1. What is the managed object — vineyard? block? row? vine? What identity attributes (variety, clone, rootstock, planting year, spacing, trellis, area, vine count, appellation/AVA)?
2. How is time modeled — perennial asset vs annual vintage? Is "vintage" a structural object (records, lifecycle) or just a label?
3. Which operations are recorded against the asset (pruning, canopy management — shoot thinning/leaf pulling/hedging, trellis/repair, spray, irrigation, nutrition, netting, frost/damage events)? How is phenology recorded (modified E-L scale)?
4. How is ripening handled — maturity sampling (Brix/TA/pH), crop estimation (bunch counts, cluster weights), pick-timing decisions?
5. How is harvest handled — crews, tons per block, weigh tags/scale tickets, deliveries, traceability of fruit to the winery and of wine back to blocks?
6. What is the winery relationship — integration (maturity samples, harvest intakes), grape contracts, grower payments, spray diaries required by winery buyers?
7. What labor machinery (crews, piece rates for pruning/harvest, payroll, labour-contractor invoicing)?
8. What monitoring/decision support is bundled or integrated (sensors, weather, disease models, satellite/GIS)?
9. What interfaces (block map, row/vine lists, mobile capture, dashboard, winery handoff)?
10. Boundaries: vs Orchard Management (the flagged seam), vs Winery Management, vs Crop Management, vs Harvest Management, vs Farm Labor Management, vs monitoring Types, vs Field Management, vs Farm Management Platform.

## Representative Products

| Product | Origin / segment | Why selected | Evidence reached |
|---|---|---|---|
| AgCode (now AgilityAg) | US; began 2002 as a solution for grapes and vines (first customers E. & J. Gallo, Opus One, Piña Vineyard Management); now multi-crop specialty FMS | Grower-side operational pole with vineyard origin; harvest-at-scale machinery (certified weight tickets, trace loads/bins to block) | Tier 1: official homepage (post-rebrand); Tier 3: 20-year anniversary trade article |
| Vinea | New Zealand (Blenheim, founded 2010 by Information Power); grape growers, wine companies, labour managers | Grower-side viticulture-depth pole: block → row → vine, modified E-L phenology, pruning quality assessments, labour-contractor model, winery-software integration | Tier 1: official site (home/about/wine-companies/labour-managers/privacy), Microsoft Marketplace listing, company LinkedIn page |
| VineTrack | Australia (Orange NSW); built by a working vigneron; small-vineyard tier (75+ vineyards, 22.8 ha average) | Small-grower mobile-first pole: GPS blocks, spray programs with canopy-based rates, E-L stages, cost by block/variety/vintage | Tier 1: official site (home/about/discover), App Store listing, portal sign-in page |
| Crush.wine | US; winery software (cellar + vineyards + lab + TTB back office); small-winery tier | Winery-integrated pole: vineyard management as the front end of cellar operations; block vintages, weigh tags, AVA resolution | Tier 1: full Vineyard Management feature page |
| InnoVint | US; winery production suite (GROW/MAKE/SUPPLY/FINANCE); mid-market wineries | Winery-integrated pole #2: vineyard tracking module + grape/grower contract management inside the production suite | Tier 1: Vineyard Tracking product page; Tier 1: company blog article on growing-season tracking |

Boundary / corroborating specimens (fetched or captured to draw seams, not counted as primary sample):

- **vintrace + eVineyard** (winery production software that acquired a vineyard management product) — the winery↔vineyard seam stated by the vendor itself: "one unified system where vineyard and winery teams work in sync — from tracking fruit development in the field to optimizing fermentation in the cellar"; "full traceability from vineyard block to final bottle"; "track costs per vineyard block". (vintrace.com blog; encompasstech vineyard-management page.)
- **Vinsight** (Australia; winery + vineyard software) — "In the Vineyard: daily and seasonal vineyard operations from pruning to harvest; detailed spray diary reporting; maturity data on fruit throughout the growing season; operations history, vineyard, block and variety details; crop prediction, met data and soil analyses." (Official products page, captured via search index.)
- **JDE EnterpriseOne Grower Management** (Oracle documentation) — the enterprise processor-side pattern: farms (external = supplying growers, internal = estate) → blocks → harvests (harvest code = block + period + suffix), crush site, container type, quantity per load; "The growing cycle for a vineyard is a year, and the grapes are harvested annually."
- **Wine Business Monthly vineyard software reviews (2006, 2011)** — trade-press surveys of the then-market: comparison axes include "smallest vineyard unit tracked (block, sub-block or vine row)", "traceability to/from wine lots", "tracking of phenology, yield components, fruit maturity", weigh tags tracked "all the way through winery to shipping", spray diaries, labor/payroll. Historical anchor.
- **Semios** (from the orchard pass) — vineyard-serving monitoring pole (sensors, models, mating disruption); lacks the asset record.
- **NZ Winegrowers member portal** — industry-body compliance context: GrapeLink Spray Diary, Sustainable Winegrowing New Zealand (SWNZ) submissions.
- **Integrape** (NZ, trade article) — vineyard data aggregation/GIS layer with vine-level audits; monitoring/data pole adjacent to the record-keeping Type.

Rejected / unreachable (recorded, not used as evidence):

- **FarmSoft** — 403 on both attempts in the orchard pass (2026-09-09); not retried per the one-to-two-attempt rule. No claims made about its structure.
- **AgCode vineyard segment page** — the rebranded site (AgilityAg) serves a single-page app; the Segments navigation resolves to the generic homepage. Vineyard-specific depth asserted only at homepage + third-party-article level.

## Sources

Fetched 2026-09-10 (Layer A unless noted):

- AgCode/AgilityAg — official homepage: https://agcode.com/ (rebrand to AgilityAg; platform benefits; planning/labor/budgeting/tasks/scouting/harvest modules)
- Vinea — official site: https://www.vinea.co.nz/ (home), http://vinea.co.nz/about-1 , https://www.vinea.co.nz/wine-companies , http://vinea.co.nz/labour-managers , http://vinea.co.nz/privacy ; Microsoft Marketplace listing: https://marketplace.microsoft.com/en-us/product/saas/informationpowerlimited1610485179650.vinea_nova?tab=overview ; LinkedIn company page: http://linkedin.com/company/vinea-software
- VineTrack — official site: https://www.vinetrack.com.au/ , https://www.vinetrack.com.au/about , https://www.vinetrack.com.au/discover ; portal: https://portal.vinetrack.com.au/ ; App Store listing: https://apps.apple.com/au/app/vinetrack/id6761143377
- Crush.wine — Vineyard Management feature page: https://crush.wine/features/vineyards (full fetch)
- InnoVint — Vineyard Tracking product page: https://www.innovint.us/product/vineyard-tracking (full fetch); blog: https://www.innovint.us/insight/vineyard-information-anywhere-anytime
- vintrace — acquisition announcement: https://www.vintrace.com/vintrace-evineyard-bringing-the-winery-and-vineyard-closer-than-ever ; Encompass vineyard-management page: http://encompasstech.com/vintrace/vineyard-management ; winery software page: https://www.vintrace.com/wine-production-software
- Oracle — JDE EnterpriseOne Grower Management docs: https://docs.oracle.com/cd/E16582_01/doc.91/e15114/enter_farm_block_harvest.htm
- NZ Winegrowers member portal: https://portal.nzwine.com/

Captured via search-index excerpts (Layer A content, search-mediated access):

- Vinsight — products page: https://www.vinsight.net/products
- Wine Business Monthly — "Vineyard Management Software" review (July 2006): https://www.winebusiness.com/content/File/wbm_0706_vineyard_software.pdf ; "Product Review: Vineyard Management Support Software" (July 2011): https://www.winebusiness.com/content/file/wbm_july11_vineyardsoftware.pdf
- Wines & Vines — "Choosing Vineyard Management Software": https://winebusinessanalytics.com/sections/printout_article.cfm?article=feature&content=143821 ; "Vineyard Software Makes Tracking Easier": https://winebusinessanalytics.com/features/article/50804/Vineyard-Software-Makes-Tracking-Easier
- Vinifera — site and about page: https://viniferavineyardmanagement.com/ , https://viniferavineyardmanagement.com/about
- Fruit Growers News — "AgCode marks 20 years": https://fruitgrowersnews.com/news/agcode-marks-20-years-of-software-solutions-for-specialty-crops (Tier 3)
- Rural News Group (NZ) — "Integrape Pro: NZ Vineyard Data Gets Granular": https://www.ruralnewsgroup.co.nz/wine-grower/wg-industry/integrape-pro-vineyard-data-nz (Tier 3)
- Tabula — viticulture page: https://tabula.live/en-au/viticulture
- Farmable — US growers page: https://farmable.tech/

In-repo prior research cross-referenced (Layer B context, not new fetches):

- research/orchard-management.md (the flagged seam; family shape; historical-check pattern)
- applications/orchard-management.md, applications/crop-management.md, applications/harvest-management.md, applications/farm-labor-management.md, applications/farm-management-platform.md (Related Types framing)
- STATUS.md entries for the processed siblings listed above

## Product Observations

### AgCode / AgilityAg (evidence layer A — homepage; layer C context — trade article)

- Positioning (homepage): "the most used software in speciality crops"; "No other solution is as complete and capable of serving the needs of the world's largest growers." Multi-crop specialty FMS (vineyards, tree fruit, nuts, berries, field crops per the trade article).
- **Planning**: "Plan your season using historic data with details down to the field level"; "Create operational and financial plans based on accurate, block-level numbers"; "Track actuals to your budget".
- **Budgeting**: "Create annual crop estimates segmented by phenology"; "Track your entire costs as they're completed for true block level profit and loss"; "Produce budget variance for owners or summary reports to billed parties" — the billed-party framing fits the vineyard-management-company / contractor model.
- **Labor management**: crews or individuals, employees or contractors; pay rules by job classification; state overtime alerts; ID badges/barcodes for clock-in; multi-step approval and audit.
- **Tasks & work orders**: work orders for field operations assigned to teams; equipment assignment and maintenance schedules.
- **Field scouting & IPM**: "Record everything that happens in the field from pest scouting to crop maturity"; GPS + photos on notes; chemical/pesticide application tracking; "reports ready to be sent directly to government and regulatory entities".
- **Harvest management**: "Coordinate harvest crews and equipment"; "Monitor block and variety-level yields in real time"; "Receive deliveries at the scale"; "Print waterproof certified weight tickets in the field"; "Trace loads or bins back to the block"; "Eliminate losses due to misassigned loads, missing tickets and theft."
- Trade article (Tier 3): began January 2002 "as a solution for grapes and vines"; first three customers E. & J. Gallo Winery, Opus One Winery, and Piña Vineyard Management; now 24 crop types, 5,000 users, 700,000 acres; customers report "60% reduction in manual calculation of payroll and piece pay".

### Vinea (evidence layer A — official site + marketplace + LinkedIn)

- Positioning: "Integrated Vineyard Management Software"; "Vinea will digitize your entire vineyard so you get a precise picture"; "captures the data you need to monitor and optimise quality, yield and production costs and make time-critical intervention decisions"; "turning valuable data and insights into wine"; tagline "Turning Data into Wine".
- Audiences: **Grape Growers, Wine Companies, Labour Managers** ("built specifically for the wine industry: wine companies, growers, vineyards and contract labour providers").
- **Spatial model (marketplace)**: "From the block to the row and the row to the vine"; "Visualise Vineyards, blocks, rows and vine locations on maps"; ArcGIS integration "to load maps and spatial data for vineyards, blocks, rows and vines"; "geospatial digital twin" (LinkedIn).
- **Labor machinery (marketplace)**: "Job management and tracking include activity recording for individuals and teams in the field down to row level"; "Integrated Quality Assessments of common activities such as pruning with results displayed on performance dashboards"; "Tracking the distribution of consumables to workers"; "Tracking worker absences with alerts to pastoral care staff."
- **Crop measures (marketplace)**: "Create crop sampling requests and record data in the field (including sample bud, bunch and berry/bunch counts, maturity bunch and berry weights)"; "Sampling for pest and disease incidence and severity"; "Record phenological stages and dates using the Modified EL scale (such a budburst, flowering, veraison)"; "Record grape maturity measures (Brix, TA, pH)"; "Generate progressive yield estimates."
- **Integrations (marketplace)**: vineyard sensor providers (temperature, rainfall, humidity, growing degree days); "with winery software (e.g. Vintrace) to ingest data from Maturity Samples and Harvest intakes"; external service providers uploading job progress; ArcGIS.
- **Vintage framing (LinkedIn)**: "a vintage planning and management tool to help maximise productivity, profitability and sustainability for grape-growers, labour managers and contractors throughout the year, from pruning to harvest"; "planning for harvest with maturity analysis and recording crop samples — estimating and managing yield to targets — integrating with Vintrace in the winery — digitising timesheets with payroll and finance integration — carrying out QC on vineyard activities such as pruning"; data "across vintages and location" (marketplace).
- **Labour managers page**: labour tracking apps (Vinea Mobile, Vinea Personal); payroll module integrating with payroll systems; workforce records incl. immigration and health-and-safety compliance documents; customer quote (labour supply company): "we undertake work in the vineyards throughout the season including harvesting and pruning. This work is done on an hourly and piece rate basis… From creating jobs that include health and safety risks and locations, to supervisors in the field recording attendance and work undertaken, Vinea enables us to pay our workers and invoice our clients."

### VineTrack (evidence layer A — official site + App Store + portal)

- Positioning: "purpose-built vineyard management app that replaces spreadsheets, paper records, and scattered notebooks"; "Built by viticulturists, for viticulturists"; created by the owner/vigneron of a working winery (Stockman's Ridge Wines, Orange NSW); mobile app + web portal split ("field to office").
- Scale stats (official site): 1200+ ha under management, 75+ vineyards, 22.8 ha average per vineyard — small-vineyard tier.
- **Block asset (App Store)**: "Map every block with GPS boundaries, row configuration, vine spacing, and full irrigation detail. Whether you're managing one block or forty, every paddock record is accessible from the field."
- **Spray machinery (App Store)**: "Build spray programs with chemical rates calculated by canopy size and growth stage. Record every spray trip with a live GPS path, generate PDF reports…"; spray records manageable from the portal ("Make spray records easier to manage").
- **Costing (official site + App Store)**: "Capture operator time, fuel, and equipment costs as you go — so at the end of the season, you have a clear picture of what operations actually cost"; "report on vineyard costs by block, variety and vintage"; "Know What It Costs to Grow."
- **Season machinery (App Store)**: "Yield estimation, growth stage monitoring, and damage recording… Track E-L stages block by block, record bunch count samples, log frost, hail, and wind events, and export reports"; "Drop GPS repair pins when you spot a broken wire, missing vine, or pest issue" — trellis/vine repair as located work.
- **Pruning reports (App Store release notes)**: "Every pruning job for your vineyard in one complete report. Sort… by season, date range, worker, block, variety, status or linked Work Task"; "Reversed jobs stay visible for audit"; "Projected pruning completion is… worked out across the whole vineyard from your crew's real recent work rate"; **vintage stamping rule**: "Winter pruning is now always recorded against the right season and vintage — August 2026 is 2026 Winter Pruning, Vintage 2027."
- **Roles**: "role-based access — Owner, Manager, and Operator levels — all synced to the cloud in real time."

### Crush.wine (evidence layer A — full feature page)

- Positioning: winery software (Cellar Operations, Vineyards & Harvest, Lab Management, Back Office & TTB); the vineyard page frames vineyard management as "Step 1 of the season": "The vineyard is where a lot's identity begins — varietal, vintage, and the full set of AVAs, all set before harvest."
- **Block asset**: "Draw your vineyard blocks on a map or import from existing GIS data. Each block tracks its own varietal, rootstock, row spacing, and planting date. Once it's in, you don't touch it again unless something changes in the ground." GPS fence boundaries with automatic acreage; "Varietal, clone, rootstock, and row spacing per block"; "Automatic AVA lookup from GPS coordinates" — queries the TTB's official AVA boundary database, finds every containing AVA "including nested regions" (block in Stags Leap District also shows Napa Valley and North Coast). FAQ adds vine count and planting date to the block record.
- **Tasks**: "Create work orders for spraying, canopy management, or harvest. Assign them to blocks and crew members"; "Spray schedule tracking with re-entry intervals"; offline field app.
- **Maturity**: "Record Brix, pH, and TA samples right from the vineyard. Watch your blocks ripen and compare against previous years to make the call on pick date. Every sample links to the block vintage automatically"; maturity trends with year-over-year comparison; feeds lab management.
- **Vintage**: "Each harvest year gets its own vintage record. Crush generates block vintages for every block automatically — tracking expected tons, actual yield, and quality notes"; "Vintage lifecycle: planning → active → complete."
- **Weigh tags / cellar flow**: "When fruit arrives at the crush pad and you create a weigh tag, it links to the block vintage. That varietal and AVA information carries through every operation in the cellar — all the way to the bottle and the TTB report." "Weigh tags link to block vintage and flow into the cellar."
- Crew framing: "Your crew checks their phones before heading out — Today's blocks, today's tasks, right there."

### InnoVint (evidence layer A — product page + blog)

- Positioning: winery production suite; vineyard tracking is the "GROW" module beside MAKE (wine production), SUPPLY (case goods), FINANCE (cost accounting), TTB compliance. "From the moment the buds break in the vineyard to the departure of your finished product from your winery, we're there with you to track every activity from start to finish."
- **Growing season tracking**: "Observe, track, and manage all noteworthy vineyard and block-level activities… including photo and note attachments": phenology tracking (from budbreak to veraison); application tracking (irrigation, spraying, thinning); visual observations (pest, disease, nutrient status); analysis (cluster weights, maturity data). Offline mobile recording.
- **Harvest planning**: "Confidently Plan & Forecast Harvest Operations… with real-time vineyard data, including vintage-over-vintage trends"; winemaking teams "adjust production plans and better manage harvest operations."
- **Grape and grower contracts**: "Manage everything from contract terms, total costs, and projected cash flow in one location, providing the vineyard, finance and production teams easy access… keep track of each SKU's fruit sources to ensure fruit and farming investments are paying off."
- Blog (growing-season events worth tracking): grape contracts and farming costs "critical to measure, capture and report on for raw goods costing"; phenological events compared block-by-block against last year and historical averages; "Did we irrigate this year?… How often did we spray? Did we drop fruit?"; "Crop estimations can start anytime. Winemaking must ensure they have enough capacity and barrels on hand"; "Once veraison hits… we're now looking at maturity tracking. Start checking those Brix readings, pH, and TA"; "harvest planning… scheduling incoming fruit to forecast expected tonnage to receive per day visualized on a calendar or in a table"; "The single best thing you can do to capture full traceability from grape to bottle is to implement… vineyard tracking and winery management software."

### Boundary / corroborating specimens

**vintrace + eVineyard** (winery pole; vendor's own seam statement): pain points the acquisition fixes — vineyard data tracked separately from winemaking data; "Winemakers rely on reports from vineyard managers (which may be delayed or incomplete) instead of having instant access to the latest grape maturity data"; compliance/sustainability logging "across multiple platforms — none of which talk to your winery management software". Promises: "one unified system where vineyard and winery teams work in sync — from tracking fruit development in the field to optimizing fermentation in the cellar"; "winemakers can see vineyard conditions in real time, track ripening progress, and make data-driven decisions on when and how to harvest"; "full traceability from vineyard block to final bottle"; "Track costs per vineyard block — helping you identify the most (and least) profitable vineyard sites"; "Optimize fruit sourcing and blending — with visibility into how vineyard conditions impact wine quality and costs." Encompass page: "GPS tracking, cost supervision, work planning, irrigation and spraying decision support."

**Vinsight** (winery + vineyard, AU): "In the Vineyard — Daily and seasonal vineyard operations from pruning to harvest; Detailed spray diary reporting; Maturity data on fruit throughout the growing season; Operations history, vineyard, block and variety details; Crop prediction, met data and soil analyses"; "In the Winery — Maturity data on vineyards and blocks; Varieties and clone information; Fruit and bulk wine/juice received into the winery…"; "Vineyard management captures quality winegrowing information… aims to aid in regulatory compliance with record keeping."

**JDE EnterpriseOne Grower Management** (enterprise processor pole): "A farm consists of one or more blocks that grow the crop that is then supplied to the processing entity"; external farms (supplying entities) vs internal farms (estate, balance-sheet-managed); blocks carry "growing area, appellation and region, and coordinates"; harvest identified by "block code, harvest period, and harvest suffix"; block defaults include "Crush Site… Produced Site… Container Type… Quantity Per Load"; "The growing cycle for a vineyard is a year, and the grapes are harvested annually."

**WBM 2006 review** (historical anchor): comparison axes across then-current products — smallest vineyard unit tracked (block / sub-block / vine row), labor tracking and payroll, chemical application and reporting, farm planning, vineyard economics and budgeting, vineyard scouting, irrigation, "tracking of phenology, yield components, fruit maturity", decision support, GIS and mapping, laboratory sample tracking, **"traceability to/from wine lots"**, report generation. eSkye: "Weigh tags in field may be tracked all the way through winery to shipping of product… Tying wine attributes back to vineyard" — with the reviewer's verdict "Not really a vineyard management tool or a scouting tool; clearly winery-focused." CropTrak: "Weigh tag number may be referenced in harvest tracking function for interface to winery databases."

**WBM 2011 / Wines & Vines** (historical anchor): buyer's criteria — "Are you a grower, a winery or a winery with estate vineyards?"; "What is the smallest vineyard unit that can be tracked (i.e., block, sub-block or vine row)?"; re-entry and pre-harvest intervals; "calendar of operations and annual budgets per block or per ranch"; "Tracking of samples (e.g., petiole, soil, fruit) from the vineyard to the laboratory"; "Does the application facilitate tracking of harvested fruit from vineyard to winery (and traceability back to the vineyard)?… a way for wineries to identify their favorite vineyard blocks." Vintners Advantage: blocks defined "in just about any way they deem necessary… soil, pruning, trellis, irrigation, varietal, rootstock, and pesticide and disease information"; "field tags for contracts, tonnage, carrier, date and chemistry details"; "grower payments" and "work orders"; "field sampling can be used to determine when crush should start for a particular lot, and the harvest schedule can be organized for the grower's delivery date and crush volumes." Orion: vineyard module tracks "down to the sub-block level… complete history of block, sub-block or vineyard." Wine Management Systems: "history of each vineyard block included in a particular blend as well as a display of which tanks contain grapes from particular blocks." VineAccess/De Bortoli (AU): "Growers who supply grapes to more than one winery must currently maintain separate books to record spray data for each winery" — the spray-diary burden.

**NZ Winegrowers portal** (industry context): member data submissions include "Biosecurity Vineyard Register", "GrapeLink Spray Diary", "Sustainable Winegrowing New Zealand (SWNZ): Certification History… Audits… Vineyard Monitoring – Gross Margin; Vintage Survey."

**Integrape** (NZ; data/monitoring adjacent): 20+ years aggregating "lab results, winery data and vineyard records… presented via a geographical information system (GIS), so that the likes of nutrition and variability on vineyards are seen block by block, in a historical context"; new iteration at "10x10 metre scale… deeper insights into each vine's health and production, connecting data points from the soil right through to the resulting yield"; "Vine Audit service… to count individual vines and log individual vine health."

**Semios** (from the orchard pass): monitoring/IPM pole for permanent crops incl. vineyards — sensors, models, pheromone delivery, field service; no block registry, no work crediting.

**Vinifera** (small-grower Android pole): spray records with REI/PHI "unconditionally on for every plan"; block/row/vine mapping ("Add rows and individual vines with spacing math handled for you"); offline-first scouting; harvest events and yield estimates; "buyer settlements, and the year-end CPA bundle are downstream"; per-vineyard pricing; roles (manager, applicator, scout, read-only viewer) with append-only audit log.

**Tabula** (AU/NZ operations pole): job management and scheduling across vineyards and growing seasons; "Plan and assign sprays by block with clear instructions"; "Guide operators with precise, on-screen coverage"; "Prevent missed rows and double-ups"; "Automatic GPS-accurate job records… Accurate, audit-ready reports for compliance and export."

## Cross-product Comparison

| Dimension | AgCode/AgilityAg | Vinea | VineTrack | Crush.wine | InnoVint | vintrace+eVineyard / Vinsight (winery pole) |
|---|---|---|---|---|---|---|
| Asset hierarchy | field/block-level plans and P&L | vineyard → block → row → vine (maps, ArcGIS) | blocks with GPS boundaries, row configuration, vine spacing | vineyard → blocks (GPS fences, acreage) | block-level activities | vineyard, block and variety details; blocks |
| Planting identity | block-level numbers, phenology-segmented estimates | blocks/rows/vines located on maps | row configuration, vine spacing, irrigation detail | varietal, clone, rootstock, row spacing, vine count, planting date; AVA lookup | block-level | varieties and clone information |
| Perennial work recorded | work orders; scouting/IPM; chemical applications | jobs down to row level; pruning with quality assessments | spray trips with GPS paths; repair pins (broken wire, missing vine); machinery runs | work orders for spraying, canopy management, harvest; spray schedule with REI | applications (irrigation, spraying, thinning); observations | operations from pruning to harvest; spray diary |
| Phenology | "crop estimates segmented by phenology" | modified E-L scale (budburst, flowering, veraison) | E-L stages block by block | (maturity samples carry the season) | budbreak to veraison; block-by-block vs last year | maturity data through the season |
| Maturity sampling | crop maturity in scouting | Brix, TA, pH; sampling requests | bunch count samples | Brix, pH, TA linked to block vintage; year-over-year | Brix, pH, TA; cluster weights | maturity data on vineyards and blocks |
| Crop estimation | annual crop estimates; block-level budgeting | progressive yield estimates; yield to targets | yield estimation | expected tons per block vintage | crop estimations; expected tonnage per day | crop prediction |
| Harvest outcome credited to asset | block/variety yields in real time; deliveries at the scale; certified weight tickets; trace loads/bins to block | harvest intakes via winery integration | harvest data at season end; costs by block/variety/vintage | weigh tags link to block vintage; actual yield; quality notes | harvest planning calendar; vintage-over-vintage | fruit received into the winery; block-to-bottle traceability |
| Vintage as structure | season plans vs actuals | "across vintages"; vintage planning tool | pruning stamped with season + vintage | vintage records; block vintages; planning → active → complete | vintage-over-vintage trends | vintage survey (industry) |
| Winery-bound flow | deliveries at scale; tickets; trace to block | integration with winery software (maturity samples, harvest intakes) | (not visible) | weigh tags → cellar → bottle → TTB report | grape/grower contracts; SKU fruit sources; grape-to-bottle traceability | unified vineyard+winery; block to final bottle; tanks containing block grapes |
| Labor machinery | crews/individuals; pay rules; overtime alerts; badges | crews down to row; piece rates; payroll integration; labour-contractor invoicing; pastoral care | roles (owner/manager/operator); operator time capture | tasks to crew members | (not the module's center) | (winery-side) |
| Cost/profitability | true block-level P&L; budget variance to billed parties | quality, yield, production costs across vintages | costs by block, variety, vintage | expected vs actual tons | contract costs; raw goods costing | costs per vineyard block; most/least profitable sites |
| Compliance | regulatory-ready application reports | workforce compliance docs; record keeping | PDF spray reports; audit-visible reversed jobs | TTB reporting downstream | TTB compliance (suite) | spray diary reporting; regulatory compliance |
| Monitoring | scouting + GPS notes | sensor integration (climate, GDD); ArcGIS | weather/rainfall visibility | lab management integration | observations; (sensors via integrations) | met data; sensors (eVineyard) |
| Pole | grower-side operational (multi-crop) | grower-side viticulture-depth + labour contractors | grower-side small-vineyard mobile | winery-integrated (small wineries) | winery-integrated (mid-market) | winery-integrated |

## Canonical Abstraction

### L0 — Defining Invariant (three jointly-held structures)

1. **The vineyard planting as the persistent production asset of record.** An identified vineyard/estate → block hierarchy (commonly extending to rows and, where managed at that level, individual vines) carrying planting identity — variety, with clone and rootstock where kept; commonly area, planting year, row spacing/row configuration, trellis; appellation/region where the regime has one — persisting across vintages as the anchor to which work, observations, and outcomes attach. Remove → land/field registry (Field Management) or season-scoped crop records (Crop Management).
2. **Perennial-cycle viticultural work recorded against the asset.** Dated, attributed, location-bound records of the vineyard's care and protection operations — pruning, canopy management (shoot thinning, leaf pulling, hedging class work), trellis and vine repair, crop reduction (thinning/dropping fruit), spray, irrigation, nutrition where kept — with the vine's phenology recorded block by block through the season (commonly on the modified E-L scale: budburst, flowering, veraison). Remove → free-floating task log; the asset is no longer being managed.
3. **The vintage's fruit outcome credited to the asset.** Ripening tracked through the season via maturity sampling (commonly sugar/acidity/pH measures) and crop estimation per block (bunch/cluster counts and weights → progressive yield estimates, expected vs actual tons); harvest recorded per block — commonly as weighed production (loads/bins/tons; weigh-tagged deliveries where the winery-bound flow is in scope) — accumulating into the block's vintage-over-vintage performance history (yield, quality, cost), with the block's identity (variety, vintage, appellation) flowing with the fruit toward crush/wine where the system reaches that far. Remove → registry + work log with no production loop; or a yield log with no wine-bound identity.

Jointly-held load-bearing:

- 1 alone = land/asset registry (Field Management territory)
- 2 without 1 = free-floating work records
- 3 without 1+2 = bare yield/maturity log
- 1+2 without 3 = viticulture journal with no production loop
- 1+3 without 2 = registry + yield statistics, no work management
- 2+3 without 1 = records not bound to a persistent asset

### L1 — Common Mature Structure

- Variety catalog with clone/rootstock where kept; variety-specific recording and reporting.
- Spray programs and spray records with re-entry/pre-harvest interval awareness; chemical inventory; the winery-facing **spray diary** (AU/NZ tradition — growers supplying multiple wineries keep spray records per buyer; industry bodies run spray-diary submissions).
- Job/work-order machinery with crew assignment (today's blocks, today's tasks), timesheets, piece rates for pruning and harvest, payroll integration; labour-contractor invoicing (pay workers, invoice clients).
- Crop estimation machinery: sampling requests, bunch/cluster counts, berry weights, progressive yield estimates, expected-vs-actual tons.
- Maturity sampling programs linked to block and vintage; lab integration; year-over-year ripening comparison driving pick decisions.
- Quality assessment of work (pruning quality scores on performance dashboards).
- Block-level cost tracking and profitability: cost per block/variety/vintage, block-level P&L, budget variance reported to owners or billed parties.
- Vintage organization: vintage records per harvest year, block vintages, vintage lifecycle (planning → active → complete), vintage-over-vintage comparison.
- Harvest coordination: crews and equipment, deliveries received at the scale, certified weight tickets, trace loads/bins back to the block.
- Mobile field capture with offline capability + web dashboard; GPS throughout (block boundaries, spray paths, repair pins, harvest positions).
- Integration surface: winery software (maturity samples, harvest intakes), sensor providers (climate, growing degree days), GIS/spatial data, payroll/finance systems.

### L2 — Variant / Optional Structure

- **Pole: grower-side standalone vs winery-integrated module.** The market's biggest split. Grower-side products (AgCode, Vinea, VineTrack, Vinifera) center the planting asset and its work; winery-integrated products (Crush.wine, InnoVint, vintrace+eVineyard, Vinsight, eSkye, Orion, Vintners Advantage, JDE Grower Management) carry the same block asset as the front end of the wine production record — ripening feeds pick decisions, weigh tags feed the cellar, block identity flows to the bottle. A 2006 reviewer already drew this line ("not really a vineyard management tool… clearly winery-focused").
- **Business model served:** estate winery's own vineyards; independent grower selling fruit under contract (grape contracts, tonnage terms, buyer settlements); vineyard management company running client estates (billed-party reporting); vineyard labour contractor (crews supplied to growers, pay workers + invoice clients).
- **Regional regimes:** US AVA machinery (automated lookup against the TTB boundary database, nested appellations); AU/NZ spray-diary and export-compliance tradition; industry-body submissions (NZ GrapeLink Spray Diary, SWNZ certification, vintage surveys); EU treatment-record traditions by analogy to the orchard finding.
- **Vine-level granularity:** row-level standard; individual-vine identity and vine audits (Vinea row-to-vine; Integrape vine audits; Vinifera individual vines) as the deep-viticulture option.
- **Monitoring bundling vs integration:** sensors, weather stations, disease models, satellite/NDVI data layers (Semios, Integrape) — adjacent Types' machinery consumed via integration or bundling.
- **Sustainability/certification tracking:** organic/regenerative/sustainability-program records (vintrace+eVineyard framing; SWNZ).
- **Machinery/fleet management:** equipment records, maintenance schedules, fuel and operating costs (AgCode, VineTrack, Tabula).
- **Damage/event recording:** frost, hail, wind events logged against blocks (VineTrack).
- **Fruit contracts and grower payments:** contract terms, tonnage, carrier, chemistry details, grower payments (winery-integrated pole: InnoVint, Vintners Advantage, JDE); buyer settlements (Vinifera, grower side).

### L3 — Vendor-specific (kept out of the final document)

- Crush.wine: automatic AVA lookup against the TTB database with nested-region resolution; auto-generated block vintages; TTB report flow; "tons to gallons" tools.
- Vinea: modified-E-L-scale phenology recording; pastoral-care alerts on worker absences; consumable distribution tracking; Vintrace integration; ArcGIS loading; "Powered By Vinea" labour-contractor branding.
- VineTrack: chemical rates calculated by canopy size and growth stage; live GPS spray-path recording; the pruning season/vintage stamping rule ("August 2026 is 2026 Winter Pruning, Vintage 2027"); projected pruning completion from crew work rates.
- InnoVint: GROW/MAKE/SUPPLY/FINANCE suite packaging; SKU fruit-source tracking; "15-30 hours per week" claims.
- AgCode/AgilityAg: certified waterproof weight tickets; state overtime-rule alerts; Radfords product line; ROI calculator.
- vintrace: eVineyard acquisition; batch-tracking link for block-to-bottle traceability; Encompass maker-to-market platform framing.
- Vinifera: per-vineyard (not per-seat) pricing; REI/PHI free-tier policy; append-only audit log; Google Play distribution.
- JDE: harvest code = block + period + suffix; crush site / produced site business units; external vs internal farm accounting.
- Integrape: 10×10 m granularity; Vine Audit service; Vure App field collection.

## Anti-overfitting Checks

- **The winery-bound flow (weigh tags → cellar → wine lots) is NOT definitional.** The grower-side pole proves it: VineTrack shows no weigh-tag/cellar machinery; Vinea reaches the winery only through integration ("ingest data from Maturity Samples and Harvest intakes"); Vinifera stops at harvest events and buyer settlements. The winery-bound flow is the winery-integrated pole's realization and the seam with Winery Management — held in leg 3 as a "where the system reaches that far" clause, not as the invariant.
- **AVA/appellation machinery is NOT definitional.** US-specific (Crush.wine's TTB lookup; JDE's appellation field). Held L2 regional; "appellation/region where the regime has one" is the generalized attribute.
- **The modified E-L scale is NOT definitional.** Vinea and VineTrack name it; Crush.wine and InnoVint track phenology without naming a scale. The invariant is phenology recorded block by block; the scale is the common implementation.
- **Vine-level identity is NOT definitional.** Row-level is the standard working substrate; vine-level appears in deep-viticulture products (Vinea, Vinifera, Integrape audits). Held L2.
- **Piece-rate/payroll machinery is NOT definitional.** Deep in the grower-side operational products and the labour-contractor model; absent from the winery-integrated modules' center. Held L1.
- **Maturity sampling IS held inside leg 3** (not L1): every sampled product in both poles carries ripening/maturity machinery (Brix/TA/pH named in five), and pick-timing is the vineyard's characteristic season decision. The abstraction is "ripening tracked through maturity sampling and crop estimation" — measures named as "commonly", not as invariant.
- **Vintage-as-object is NOT definitional as a separate structure.** Crush.wine makes it an object with a lifecycle; VineTrack stamps records with vintage; Vinea plans "across vintages"; AgCode plans by season. The invariant is the season-scoped outcome credited to the persistent asset; "vintage" is the domain's name for that season and is used in the document as vocabulary.
- **Monitoring (sensors/models/satellite) is NOT definitional.** The monitoring pole (Semios, Integrape) lacks the asset record entirely; vineyard products consume monitoring via integration.
- **Spray-diary compliance is NOT definitional** (regional tradition) but spray records with safety intervals are common mature structure.
- **Cloud/mobile/GPS are NOT definitional** (historical check below).

## Historical / Market-Sample Check (§24)

Pre-digital vineyard practice, assembled from the trade-press historical record and standard viticultural record-keeping practice:

- **Vineyard block register/map**: block names with variety, clone, rootstock, year planted, spacing, trellis — leg 1 on paper. (The 2011 buyer's criteria treat "block, sub-block or vine row" granularity and block content fields — soil, trellis, varietal, rootstock — as the then-standard selection questions.)
- **Spray diaries / spray logs**: dated, block-anchored application records kept for winery buyers and regulators; the AU/NZ spray-diary tradition predates software ("Growers who supply grapes to more than one winery must currently maintain separate books…") — leg 2.
- **Pruning tallies / crew sheets**: rows or vines pruned per worker per block for piece-rate settlement — leg 2.
- **Maturity sampling notebooks**: Brix/TA/pH readings per block per date through ripening, informing pick dates — leg 3's ripening machinery.
- **Crop estimation sheets**: bunch counts × cluster weights per block — leg 3.
- **Weigh tags / delivery dockets**: tons delivered to the crush pad per grower/block, settled against fruit contracts — leg 3's winery-bound flow (historically kept on both sides of the scale).
- **Block × vintage yield/cost books**: year-over-year records per block informing management and renewal — leg 3's accumulated history.

All three legs satisfied with zero software-era machinery. The 2006 WBM survey's comparison axes (smallest unit tracked, traceability to/from wine lots, phenology/maturity tracking, chemical reporting, labor/payroll) are the same structures the modern products carry — the Type's shape predates its current mobile/cloud form. The definition names no GPS, cloud, mobile apps, sensors, AVA databases, or E-L scales.

## Boundary Findings

1. **vs Orchard Management — the flagged seam, RESOLVED from this side: keep-both RATIFIED with refinement.** The orchard pass expected the seam at "vineyard blocks bound to winery-bound lots (harvest → crush → wine) vs orchard's fresh-fruit packhouse/traceability". From the vineyard side the expectation is **confirmed at pole level and refined**: the winery-bound flow is the winery-integrated pole's structure (weigh tags → cellar → bottle; block identity in the wine) and the dominant continuation for winegrapes, but the grower-side pole (VineTrack, Vinifera; Vinea via integration) stops at harvest tons credited to blocks — so the flow cannot be the sole discriminator. The ratified seam has four strands: (a) **domain binding** — winegrapes with viticulture-specific operations (canopy management, trellis/vine repair, crop reduction, E-L-class phenology) and identity (variety/clone/rootstock; appellation) vs orchard's tree-fruit operations (per-tree piece work, grafting/top-working) and identity; (b) **ripening machinery** — maturity sampling (Brix/TA/pH) and crop estimation as standard season machinery in vineyard products of both poles vs optional vision tools in orchard products; (c) **downstream continuation** — winery-bound (weigh tags, fruit contracts, wine-lot traceability, block identity in the wine) vs packhouse-bound (bins, storage rooms, packout); (d) **the vintage** as the named season unit with vintage-over-vintage comparison as standard machinery. Both Types share the perennial-asset family shape (persistent planting + perennial work + season outcome credited to the asset). Removal tests hold both directions: strip the winegrape binding and winery-bound continuation → an orchard-shaped generic perennial-asset system; strip the tree-fruit binding and packhouse continuation → a vineyard-shaped one. Neither collapses into the other; both stand beside Crop Management per the orchard pass's ratification.
2. **vs Winery Management (unprocessed sibling) — forward flag.** The seam is the crush pad. Vineyard Management's leg 3 ends at weighed fruit credited to blocks, with block identity flowing toward the winery; Winery Management begins at fruit intake/receiving and runs fermentation → production → storage → bottling → compliance. The winery-integrated pole straddles the seam by packaging both sides (Crush.wine "vineyard is where a lot's identity begins"; InnoVint "grape to bottle"; vintrace "block to final bottle"; Wine Management Systems "which tanks contain grapes from particular blocks") — the vineyard module inside a winery suite is this Type at module grain, and the winery Type's center is the wine production record (lots/tanks/barrels/batches), not the planting asset. The winery pass should hold: vineyard module = Vineyard Management's structure; crush intake = the handoff object owned by the winery side.
3. **vs Crop Management.** Same seam as the orchard ratification: crop management's unit of record is the season-scoped crop (crop × field × season, closed with season history); the vineyard's is the persistent planting that outlives every vintage. General FMS platforms absorb vineyards as crop types within the season model (the orchard pass's Agrivi/Agworld finding applies unchanged). The vineyard-specific structures — canopy work, E-L-class phenology, maturity sampling, vintage organization, winery-bound flow — are not in the crop-management model. Keep-both consistent with the orchard pass.
4. **vs Harvest Management.** Harvest Management's center is the harvest operation itself (crews, ticketing, crediting, packhouse handoff) — crop-agnostic. The vineyard's leg 3 is the asset's outcome record. AgCode straddles the seam (its Harvest Management module is harvest-operation machinery — scale deliveries, weight tickets — inside a grower FMS). The two Types interlock; neither subsumes the other.
5. **vs Farm Labor Management.** Crew/time/piece-rate machinery is shared; vineyard pruning and harvest are piece-rate work; the vineyard labour contractor is a distinct user (Vinea's labour-managers audience: pay workers, invoice clients). The labor Type centers the workforce across the farm; the vineyard Type centers the asset.
6. **vs monitoring Types (Precision Agriculture Platform, Agricultural IoT Platform, Crop Remote Sensing; specimens Semios, Integrape).** Sensing/model-driven decision support is adjacent machinery: the monitoring pole lacks the asset record entirely (proving monitoring ≠ vineyard management), and vineyard products consume monitoring via integration (Vinea's sensor and ArcGIS integrations; Integrape as a data-aggregation layer beside vineyard records).
7. **vs Field Management.** The land-unit register (extent, soil, boundaries) is leg 1 alone. The vineyard Type adds the planting (a crop asset on the land) and the cycle around it.
8. **vs Farm Management Platform.** Whole-operation scope (land, livestock, finance, equipment) vs vineyard-scoped production management. A vineyard operation can be run inside a farm-management platform; the vineyard Type exists where the planting asset, its viticultural work, and the winery-bound outcome are the center.
9. **vs Agricultural GIS.** The spatial substrate (block boundaries, maps, ArcGIS layers) is machinery the vineyard Type consumes; Vinea and Integrape use GIS as the visualization layer over the vineyard model, not as the record itself.
10. **vs Nursery Management (unprocessed sibling).** Nursery propagates plants as sale inventory; the vineyard grows fruit for harvest from planted vines. Recorded for the nursery pass (same expectation as the orchard pass's).

## Uncertainties

- **AgCode's vineyard-specific depth**: the product rebranded to AgilityAg and the public site is now a multi-crop single-page app; the vineyard segment page was not reachable. Vineyard origin and first customers rest on a third-party trade article (Tier 3). All AgCode assertions in the final document are kept at homepage + article level; no vineyard-specific module claims are made.
- **FarmSoft** (vineyard management suite) remained unreachable (403 ×2 in the orchard pass; not retried). No structural claims made. The "packing-integrated orchard suite" gap noted there has a vineyard analog: the "full grower+winery suite" pole is represented indirectly (vintrace+eVineyard, Vinsight, the 2006/2011 reviews' eSkye/Orion/Vintners Advantage entries).
- **Vinsight, WBM reviews, Vinifera, Tabula, Farmable, Integrape** were captured via search-index excerpts rather than direct fetches; their content is used as corroborating/boundary evidence at moderate strength, and no precise operational claims rest on them alone.
- Whether a "pure viticulture records, no-harvest" product exists was not observed; leg 3 is kept because every sampled product in both poles carries harvest/yield outcome machinery. If such a product exists, leg 3 would need re-examination.
- **Vine-level granularity** is claimed by Vinea (row to vine) and Vinifera (individual vines) and practiced by Integrape's audits, but most products stop at row level; held as optional substrate, not invariant.
- **Grape contracts on the grower side**: contract machinery is directly observed at the winery-integrated pole (InnoVint, Vintners Advantage, JDE) and as buyer settlements (Vinifera); grower-side contract depth beyond that was not directly observed. Held L2.
- **Netting/bird protection** is standard viticulture practice but was not named on any fetched page; it is not listed in the final document's operation set (damage/event recording — frost, hail, wind — is evidenced via VineTrack).
- Winery Management and Nursery Management are unprocessed; boundary statements 2 and 10 are forward flags, not resolutions.

## Final Synthesis

Vineyard Management is the vineyard operation's system of record, organized around the vineyard planting — the long-lived block of winegrapes — as a persistent production asset. Its defining core is three jointly-held structures: the planting held as an identified, variety-carrying asset that outlives every vintage (vineyard/estate → block → rows, extending to vines where managed at that level; identity: variety with clone and rootstock where kept, commonly area, planting year, row spacing/trellis, appellation where the regime has one); the perennial cycle of viticultural work recorded against that asset (pruning, canopy management, trellis and vine repair, crop reduction, spray, irrigation, nutrition — with the vine's phenology recorded block by block through the season, commonly on the modified E-L scale); and the vintage's fruit outcome credited to the asset (ripening tracked through maturity sampling and crop estimation; harvest recorded per block as weighed production accumulating into block × vintage performance history, the block's identity flowing with the fruit toward crush/wine where the system reaches that far). Around this core, mature products add spray programs and records with safety intervals and the winery-facing spray diary, job/crew machinery with piece rates and labour-contractor invoicing, crop estimation and maturity programs driving pick decisions, block-level cost and profitability, vintage organization, mobile/GPS field capture, and integration with winery software, sensors, and GIS. The Type spans two poles — grower-side standalone systems and vineyard modules inside winery production suites — sharing one core; the pole is the primary variant axis, not a Type boundary. The orchard pass's flag is resolved: Vineyard Management is a genuine sibling Type — same perennial-asset family shape as Orchard Management, different domain binding (viticulture vs tree-fruit operations), different ripening machinery (maturity sampling as standard), and a different downstream continuation (winery-bound vs packhouse-bound). Monitoring services, harvest-operation machinery, labor machinery, spray-domain machinery, and the wine production record itself are adjacent Types that interlock with this one.
