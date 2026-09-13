# Research Notes — Poultry Farm Management

Research date: 2026-09-09
Leaf: Poultry Farm Management (DIRECTORY §20 Agriculture, Food & Natural Resources)
Slug: poultry-farm-management

## Research Goal

Understand what the poultry-farm-management Application Type is, from real products: what its system of record holds, what users do with it, how the production cycle flows through it, and where it ends relative to the sibling livestock leaves (livestock, dairy, swine), the feed discipline, the whole-farm platform, and the downstream egg/processing side.

## Initial Boundary Hypothesis

- Core use: manage a poultry operation (broilers, layers, breeders, hatchery) as batch flocks placed into houses — placement, daily production records (mortality, weights, feed/water, egg collection), cycle closure, and performance-driven decisions.
- Users: poultry farmers/growers, farm managers, production managers of integrated poultry companies, consultants/vets.
- Nearest neighbors (from sibling passes already processed):
  - **Livestock Management** (processed 2026-09-09): long-lived breeding herds managed as individuals or mobs; its pass left a FORWARD FLAG for this leaf — joint review expected on the batch-vs-breeding-herd seam; assign by production-system shape, not species lists.
  - **Dairy Farm Management** (processed 2026-09-07): individually identified animals + lactation cycle; its pass characterized poultry/swine as batch/population-based.
  - **Aquaculture Management** (processed 2026-09-06): per-unit populations across bounded cycles — structurally closest cousin; its pass also characterized poultry as batch/population production.
  - **Feed Management** (processed 2026-09-08): the ration/feed supply is the subject there; feeding is an execution/recording layer inside animal-production Types.
  - **Farm Management Platform** (processed 2026-09-08): whole-operation scope; production-subject Types are the slices.
  - Dairy pass naming-drift note (ratified by the livestock pass): assign Types by center of gravity, not vendor category labels.
- Expected L0 shape: flock-in-house as unit of record + cycle-bound production record stream + records→performance→decisions loop. Individual bird identity suspected NOT definitional (poultry managed at flock/batch level).

## Research Questions

1. What is the unit of record — the individual bird, the flock/batch, the house, or the flock-in-house? At what granularity is identity held?
2. What is the production cycle the system follows (placement → rearing/laying → depletion → clearance → clean/rest → next placement)? How do broiler, layer, breeder, and hatchery variants differ?
3. What daily/periodic records does the system carry (mortality/culls, weights, feed/water, egg collection, environment, treatments/vaccinations)?
4. How do records become decisions (performance measures, benchmarks vs previous flocks / other farms / breed standard, alerts, reports)?
5. Where do climate controllers, sensors, and feeding equipment sit — core or layer?
6. Where is the boundary with livestock management (batch vs breeding-herd seam — the pre-hung flag), dairy, swine, feed, whole-farm platforms, and the downstream egg-packing/processing side?
7. Would older/regional products (paper flock cards, daily egg books, desktop poultry software) still fit the definition?

## Representative Products

| Product | Pole | Customer tier / geography | Evidence strength |
|---|---|---|---|
| PoultryPlan | poultry-chain software for integrated operations (rearing, breeders, hatchery, layers, broilers, slaughter, feed) | Large-scale poultry operations & integrated companies; NL/EU + global (75+ companies claimed) | A — official site + solutions pages fetched |
| Eggbase | egg & poultry data specialist (pullet rearers, layers, broiler growers, breeders, packing stations, vets) | Multi-site egg producers & poultry businesses; UK | A — official site fetched |
| Farmbrite | multi-species whole-farm suite with a poultry module (straddling pole) | Small diversified farms worldwide; US | A — official poultry solutions page fetched (help center not fetched this pass) |
| Big Dutchman | equipment-integrated pole (house management bound to climate/feeding equipment) | Global poultry equipment customers | A — official poultry-house-management page fetched (positioning level) |
| Fancom | equipment-integrated pole (automation + daily process management software) | Poultry/pig automation customers; NL/global | A — official broilers page fetched (positioning level) |

Selection rationale: two poultry-specialist software vendors with different philosophies (PoultryPlan = chain-integrated planning & benchmarking; Eggbase = data/benchmarking/compliance specialist), one multi-species whole-farm straddling pole (Farmbrite), two equipment-integrated poles (Big Dutchman, Fancom). Different geographies (NL, UK, US, DE), customer tiers (integrated enterprises, multi-site producers, small diversified farms), and product philosophies.

Checked and dropped: M-Tech Systems (US poultry software) — site unreachable twice (transport errors); Poultry360 (NZ) — unreachable twice; PoultryCare.in — product mismatch (veterinary medicines company, not software). See Uncertainties and Rejected Findings.

## Sources

- PoultryPlan — https://poultryplan.com/ (fetched 2026-09-09)
- PoultryPlan solutions — https://poultryplan.com/solutions (fetched)
- PoultryPlan OptiBroilers — https://poultryplan.com/solutions/optibroilers (fetched)
- PoultryPlan OptiLayers — https://poultryplan.com/solutions/optilayers (fetched)
- Eggbase — https://eggbase.co.uk/ (fetched)
- Farmbrite chicken & poultry — https://www.farmbrite.com/solutions/chicken-and-poultry (fetched; reached via /poultry-management-software)
- Big Dutchman poultry house management (egg production) — https://www.bigdutchman.com/en/products/egg-production/poultry-house-management/ (fetched)
- Big Dutchman product navigation (poultry growing / egg production trees) — https://www.bigdutchman.com/en/ (fetched)
- Fancom — https://www.fancom.com/ and https://www.fancom.com/broilers (fetched)
- Sibling research notes: research/livestock-management.md, research/dairy-farm-management.md, research/aquaculture-management.md, research/feed-management.md, research/farm-management-platform.md (boundary seams; livestock pass forward flag)

Source-access limitations: M-Tech Systems (mtechsystems.com / www) returned transport errors twice — dropped; no US broiler-integrator software pole directly documented. Poultry360 (poultry360.co.nz / poultry360.com) unreachable twice — dropped. Farmbrite help center not fetched this pass; Farmbrite claims rest on its official poultry solutions page (Tier 2 product page). Big Dutchman and Fancom management-software detail pages (BFN Fusion, FAY/FarmManager) not fetched; their claims are kept at positioning level. No hatchery-only vendor documentation fetched; hatchery evidence comes from PoultryPlan's OptiHatch solution page.

## Product Observations

### PoultryPlan (evidence layer A — official site + solutions pages)

- Positioning: "Poultry Management Software… for large-scale poultry operations"; "complete solution for the entire poultry chain… fully or semi integrated poultry companies"; "from parent stock to laying hen or broilers, from production to logistics, from planning to financial."
- **Farm Monitor** (ships with all products): customized dashboard; "comprehensive results pages and summaries of the daily status"; lets production manager, general management, or selected third parties "monitor, check and manage the various production processes"; alerts to smartphone/email "in case of emergency."
- **OptiBroilers** features (directly observed list): Dashboard; Flock Set up; Registration – Technical Data; Flock Results; Flock Benchmark vs Self; Flock Benchmark vs Group; Flock Document Library; App – Farmer; App – Manager; Calamity Warning System; Registration – Vaccination, Actions & Tasks; Registration – Medicine & Pest; Flock Relocation; Breed Results; Financial Stock, Prices; Transport; Processor. Marketing copy: track "bird weight, feed usage, and mortality rates"; plan/schedule "feed, water, and lighting management"; track "disease outbreaks, vaccination schedules, and medication usage."
- **OptiLayers** features: Dashboard; Flock Set up; Registration – Technical Data; Flock Results; Flock Benchmark vs Self / vs Group; Flock Document Library; Top 25 & Average; App – Farmer; Calamity Warning System; Registration – Vaccination, Actions & Tasks; Registration – Medicine & Pest; Financial; Farm Inventory; Egg Storage; Transport; Breed Results; Egg Packing Station; Forecast. Tracks "egg production, bird weight, feed intake, and mortality rates"; plan "feeding, egg collection, and manure management."
- **OptiRearing** (pullet rearing): track hens' performance by entering key data; pulls information from parent stock; benchmarks vs previous flocks and other farms; personalized dashboard.
- **OptiBreed** (parent stock): breeding farm production results entered; compare with previous flocks and other parent stock farms.
- **OptiHatch** (hatchery): employees log "initial figures, hatching results, and quality parameters"; QR codes for "full traceability of every batch of eggs"; "hatching egg planning" with short-term and long-term forecasts.
- **OptiSlaughter**: benchmark and trace processing-plant results per batch; "measure and view the performance of flocks and barns in detail"; analyze "from farm to processing plant, all the way to retail."
- **OptiFeed** (feed mill): smart suggestions on type and amount of feed to deliver, "based on real-time flock data and feed schedules"; silo choice; compare to past deliveries and performance.
- **OptiGrading** (egg packing station, connectable module): batch known before arrival; supply/inspection/storage/packing/transport supported by QR scanning; results from Moba egg-sorting machines entered directly; benchmarked and traced per batch.
- Customer quotes corroborate: daily data upload; dashboards with "fertilization vs. hatchability of fertilized eggs, first week mortality compared to the age of the mother animals"; record-keeping for regulatory compliance; real-time data on "flock health, egg production, and inventory levels."

### Eggbase (evidence layer A — official site)

- Positioning: "Egg and Poultry Software for Performance, Sustainability and Welfare"; "pullet rearer, egg layer and poultry software"; "permissioned data sharing, supportive data analytics and carbon footprinting"; "Delivering compliance, professionalism, accountability, chick and egg traceability, benchmarking and supportive analysis across multiple remote sites."
- Data inventory (directly observed list): "House and flock placement; Genetic lines; All or male/female mortality and culls; All or male/female body weights and evenness; All male/female bird movements; Egg collection; Grading data; Checks and alarms; Feed and water consumption; Temperature, lighting levels, NH₃, CO₂, humidity, litter and feather scores, red mite; On-farm feed and other deliveries; Legislative compliance; Salmonella testing regime with system prompts to ensure compliance; Medical and veterinary interventions with system prompts alerting users to potential issues at an early stage; Management programmes; Financial margins."
- "Whole life flock data from day old to end of lay"; "Actual performance to breed standard comparison; Compare breeds to each other; Compare flocks to each other."
- Benchmarking: "real-time benchmarking of both physical and financial poultry flock data across current and historical flocks"; comparisons of genetic potential; multi-site enterprises with "geographically remote farms."
- Decision use: "analyse multiple locations and flocks to influence choice of breed, choice of feed and choice of management strategy"; evaluate "flock management programmes (e.g. growing, vaccination, housing) from the best performing flock"; pullet trials, feed trials, medical trials, research projects; collaboration with primary breeders.
- Segments served: pullet rearers & producers, egg packing stations, breeders, feed suppliers, veterinarians, researchers, broiler growers; adapted for "duck egg layers, quail egg layers and broilers growers."
- Carbon footprinting integrated into production software ("activity data collection and carbon footprinting output… rolled into one").

### Farmbrite (evidence layer A — official poultry solutions page)

- Positioning: "All-in-One Farm Management Software for Poultry Producers"; "Centralize egg production records and health, improve broiler feed conversion, and maintain strict biosecurity across all your houses and coops… track flock health, batch rotations, and daily operational workflows."
- Production recording: "Easily log daily egg collection, monitor laying percentages, or track broiler weight gain by batch. Identify production drops early…"
- Feed economics: "Track feed consumption, monitor feed conversion ratios (FCR), and calculate exact cost-per-bird or cost-per-dozen."
- Health/biosecurity: "logging mortality rates, vaccination schedules, and veterinary treatments in real time, ensuring strict biosecurity and hygiene protocols across every house and pen."
- Traceability/compliance: "audit-ready records for egg grading standards, organic certifications, animal welfare guidelines, and flock health regulations… complete traceability from hatchery to harvest using… batch tracking tools."
- Multi-house/batch management: "Streamline brooder, pullet, and layer operations with centralized house and batch management. Easily track bird movements, monitor flock density, and schedule coop cleaning and resting periods to optimize facility sanitation and biosecurity protocols."
- Accounting/analytics: "tracking feed expenses, packaging costs, and veterinary supplies… production costs per batch"; 100+ pre-built reports/dashboards.
- Suite context: task management, accounting, inventory, mapping, climate, commerce — the poultry module sits inside a whole-farm product (straddling pole).

### Big Dutchman (evidence layer A — positioning; equipment-integrated pole)

- Poultry house management page: "successful poultry farmers manage feeding, egg collection, climate control, data collection and data analysis with the aid of the computer – either in the office or on the tablet before going to bed."
- Products under poultry house management: BFN Fusion (farm management software), Alarm systems, ViperTouch climate and production computer, Breezy ventilation control, amacs (poultry house management), Vento climate and production computer.
- Product tree separates: egg production (pullet rearing, layer breeder management, poultry house management, climate control, lighting…) and poultry growing (broiler/turkey/duck production, broiler breeder management, poultry house management…) — the house-management layer is common to both, bound to the vendor's own equipment.

### Fancom (evidence layer A — positioning; equipment-integrated pole)

- Broiler systems list: climate system, light control, "accurate control of feed rations," "continuous water monitoring as an indicator of animal health," behaviour monitoring, "automatic animal weighing for an up-to-date overview of the growth processes in your house," and "Management software for daily process management."
- Data management framing: "Integrate the processes in your houses into one closed system and gain insight into all your houses' performance."
- Blog-level themes: personalized dashboards (climate conditions, feed intake), role-based access management, alarm features for malfunctions.
- Fancom One ecosystem: climate control, feed and water distribution, monitoring and data management "within a single centralised system."

### Cross-product commonalities (Layer B)

1. Every product organizes the world around **houses/barns holding flocks/batches** — the house is the persistent production unit, the flock/batch the population living in it (PoultryPlan "Flock Set up"/"Flock Relocation"; Eggbase "House and flock placement"; Farmbrite "houses and coops… batch rotations"; Big Dutchman "poultry house management"; Fancom "your houses' performance").
2. Every product records **daily/periodic production data against the flock**: mortality/culls, weights/growth, feed (and water) consumption, and — where the segment produces them — eggs (PoultryPlan, Eggbase, Farmbrite; equipment poles record the same via controllers).
3. Every product converts records into **performance output**: results pages, KPIs (FCR, laying %, mortality, weight vs standard), benchmarks (vs previous flocks, vs other farms/group, vs breed standard), dashboards, alerts.
4. Health machinery (vaccination schedules, medicine/pest registration, veterinary interventions) appears in all software-side products.
5. Environment/climate data (temperature, humidity, NH₃, CO₂, lighting) is recorded — manually in software-side products, automatically via controllers in equipment-integrated products.
6. Multi-house/multi-site operation with role separation (farmer app vs manager/production-manager view; permissioned sharing with third parties) appears in all.
7. The chain extends downstream (transport, packing station, processing) and upstream (hatchery, breeders, feed) in the chain-integrated product (PoultryPlan) and as separate segments in Eggbase — evidence that the farm-side Type is the center and the chain is packaging.

## Cross-product Comparison

| Structure | PoultryPlan | Eggbase | Farmbrite | Big Dutchman | Fancom | Assessment |
|---|---|---|---|---|---|---|
| Houses/barns as persistent production units | ✔ (flocks & barns; relocation) | ✔ (house & flock placement) | ✔ (houses/coops; multi-house tracking) | ✔ (house management) | ✔ (houses' performance) | Core (all) |
| Flock/batch as managed population (counts, breed/line, age) | ✔ (Flock Set up; Breed Results) | ✔ (flock placement; genetic lines; day-old to end of lay) | ✔ (batch rotations; batch tracking) | ✔ (implied by house management) | ✔ (implied) | Core (all) |
| Individual bird identity | — | — (male/female split only) | — | — | — | Absent across sample — NOT definitional |
| Placement → cycle → clearance rhythm | ✔ (Flock Set up → Results; relocation) | ✔ (day old → end of lay) | ✔ (batch rotations; cleaning & resting periods) | ✔ (house management per cycle) | ✔ (per-house processes) | Core (all) |
| Daily technical records (mortality, weights, feed/water) | ✔ (Registration – Technical Data) | ✔ (mortality/culls, body weights/evenness, feed & water) | ✔ (mortality, weight gain by batch, feed consumption) | ✔ (via controllers) | ✔ (auto weighing, water monitoring) | Core (all) |
| Egg production recording (layers) | ✔ (OptiLayers; egg storage; forecast) | ✔ (egg collection; grading data) | ✔ (daily egg collection; laying %) | ✔ (egg collection in house management) | n/a (broiler page) | Segment-dependent content of the record stream |
| Growth recording (broilers) | ✔ (bird weight) | ✔ (broiler growers segment) | ✔ (broiler weight gain by batch) | ✔ | ✔ (automatic weighing) | Segment-dependent content |
| Hatchery/breeder records | ✔ (OptiHatch; OptiBreed) | ✔ (breeders segment) | ✔ (hatchery-to-harvest traceability claim) | ✔ (layer/broiler breeder management) | ✔ (breeder house case) | Segment variant |
| Environment/climate recording | ✔ (via IoT integration news) | ✔ (temp, NH₃, CO₂, humidity, litter/feather, red mite) | ✔ (climate module in suite) | ✔ (climate & production computers) | ✔ (climate systems) | Common mature; auto vs manual is a variant |
| Health machinery (vaccination, medicine, vet) | ✔ (Vaccination/Actions & Tasks; Medicine & Pest) | ✔ (medical & veterinary interventions with prompts) | ✔ (vaccination schedules; veterinary treatments) | — (not on fetched page) | — (not on fetched page) | Common mature (software-side products) |
| Performance measures & benchmarks | ✔ (Flock Benchmark vs Self/Group; Top 25 & Average) | ✔ (vs breed standard; flocks/breeds compared; physical & financial) | ✔ (FCR; production drops early; costs per batch) | ✔ (data analysis) | ✔ (insight into performance) | Core (all) |
| Alerts / early warning | ✔ (Calamity Warning System; Farm Monitor alerts) | ✔ (checks and alarms; system prompts) | ✔ (identify production drops early) | ✔ (alarm systems) | ✔ (alarm features) | Common mature |
| Multi-site / multi-house portfolio | ✔ (integration-wide) | ✔ (geographically remote farms) | ✔ (multi-house) | ✔ (multi-house via BFN Fusion positioning) | ✔ (all your houses) | Common mature |
| Role separation (farmer vs manager vs third parties) | ✔ (App – Farmer / App – Manager; third-party monitor) | ✔ (permissioned data sharing) | ✔ (team roles in suite) | — | ✔ (role-based access blog) | Common mature |
| Downstream chain modules (transport, packing, processing) | ✔ (Transport; Processor; OptiGrading; OptiSlaughter) | ✔ (packing station segment) | ✔ (traceability to harvest; packaging costs) | — | — | Optional / chain packaging |
| Feed formulation / mill machinery | ✔ (OptiFeed = feed delivery scheduling) | ✔ (feed suppliers segment) | ✔ (feed consumption tracking only) | ✔ (feed storage/transport equipment) | ✔ (feed rations control) | Layer → Feed Management |
| Financial layer | ✔ (Financial Stock, Prices) | ✔ (financial margins; physical & financial benchmarking) | ✔ (accounting; cost per bird/dozen) | — | — | Common mature / optional |
| Compliance machinery | ✔ (regulatory compliance via record-keeping, quotes) | ✔ (legislative compliance; salmonella testing prompts) | ✔ (audit-ready records; certifications) | — | — | Variant (regional) |
| Carbon/sustainability | ✔ (Sustell partnership news) | ✔ (carbon footprinting integrated) | — | — | — | Variant (era-current) |

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **The flock-in-house as the managed unit of record.** Birds are held as batch populations — counts with breed/genetic line and age — placed into identified production units (houses/coops; setters/hatchers at the hatchery pole). The house persists across cycles; the flock lives in it for one cycle. Records are kept at population level, not as individually identified animals. Remove → long-lived-individual livestock management (breeding herds), or an anonymous bird count.
2. **The cycle-bound production record stream.** Each flock's bounded cycle — placement → rearing/laying → depletion → clearance — is documented with dated records against the flock-in-house: mortality and culls, weights/growth, feed and water consumption, the segment's production output (egg collection for layers, hatching eggs for breeders, growth for broilers), environment observations, and health events (vaccinations, treatments). The cycle closes with clearance/market and the unit's clean/rest before the next placement. Remove → a bare head-count ledger.
3. **The records → performance → decisions loop.** Accumulated records are continuously converted into performance measures (feed conversion, laying %, mortality %, weight vs standard), benchmarks (vs previous flocks, vs other farms/groups, vs breed standard), alerts, and reports that drive placement, feeding, health, and marketing decisions. Remove → a passive flock diary/archive.

Jointly-held is load-bearing:
- 1 alone = house/coop registry with bird counts
- 2 without 1 = free-floating daily log
- 3 without 1+2 = generic reporting
- 1+2 without 3 = flock diary/archive (the "management" gone)
- 2+3 without 1 = performance spreadsheet with no flocks
- 1+3 without 2 = benchmarking over static populations

Anti-overfitting:
- **Individual bird identity is NOT definitional** — no sampled product manages birds as individuals; the population (flock/batch) is the record, with male/female splits the finest grain observed (Eggbase).
- **No single production output is definitional** — broiler farms record growth, layer farms record eggs, breeders record hatching eggs, hatcheries record set/hatch results; the invariant is that the cycle's output is recorded against the flock.
- **Climate/sensor automation is NOT definitional** — manual daily entry (Farmbrite, Eggbase's data inventory) and paper-era practice satisfy the core; controller integration is the equipment-integrated realization.
- **No specific segment (broiler/layer/breeder/hatchery) is definitional** — the Type is the production-cycle shape, realized across segments.

### L1 — Common Mature Structure

- Dashboards / daily status surfaces (farm monitor, results pages, summaries of the daily status)
- Flock setup and lifecycle records (placement, relocation/movements between houses, clearance)
- Performance analysis: FCR, laying %, mortality %, weight/evenness vs breed standard; cycle-vs-cycle comparison
- Benchmarking: vs previous flocks, vs other farms/groups, vs genetic (breed) standard; Top-N and average views
- Health machinery: vaccination schedules and records, medicine & pest registration, veterinary interventions with prompts
- Environment recording: temperature, humidity, NH₃, CO₂, lighting, litter/feather scores, red mite
- Alerts / early-warning systems (calamity warnings, alarms, deviation pop-ups)
- Multi-house and multi-site portfolios; role separation (farmer / manager / third-party monitor); permissioned data sharing
- Feed consumption recording and feed-cost economics (cost per bird / per dozen / per batch)
- Financial layer (production costs, margins, stock prices)
- Mobile farmer apps + office/manager web views; offline capture (suite pole)
- Forecasting (egg production forecast, hatching-egg planning)
- Document libraries per flock; audit-ready records for compliance

### L2 — Variant / Optional Structure

- Segment packaging: broiler / layer / pullet-rearing / breeder / hatchery as separate solutions or editions of one product
- Chain scope: farm-only vs integrated chain (hatchery → rearing → production → transport → packing station → processing → retail)
- Equipment-integration posture: standalone record-keeping vs controller-bound house management (climate computers, feeding systems, auto-weighing, behavior monitoring)
- Regional compliance machinery (legislative compliance, salmonella testing regimes, certification records — egg grading standards, organic, welfare)
- Species breadth beyond chickens (ducks, quail, turkeys)
- Carbon footprinting / sustainability overlays
- Downstream modules (egg storage, grading/packing station, transport, processing plant results)
- Deployment: cloud SaaS vs on-farm computer bound to controllers
- Business model: per-farm subscription vs integration-wide licensing

### L3 — Vendor-specific (Research Notes only)

- PoultryPlan: Opti* solution naming (OptiRearing/OptiBreed/OptiHatch/OptiLayers/OptiBroilers/OptiSlaughter/OptiFeed/OptiValue/OptiCheck/OptiGrading), Farm Monitor, Calamity Warning System, Flock Document Library, Top 25 & Average, QR-code batch traceability, Moba machine-result ingestion, Sustell partnership.
- Eggbase: Eggsense/EggsenseLite product names, EggbaseAssure, permissioned data-sharing model, carbon footprinting with LCA partner, salmonella testing prompts, male/female-split data inventory.
- Farmbrite: whole-farm suite packaging (tasks/accounting/mapping/climate/commerce), smart groups, voice-to-text, plan tiers (inherited from the livestock pass's observations).
- Big Dutchman: BFN Fusion, amacs, ViperTouch/Vento climate and production computers, Breezy ventilation control, alarm systems; myBigDutchman portal.
- Fancom: Fancom One ecosystem, FAY cloud login, Lumina controllers, iFarming framing, MTT Stairstep / Fantura / i-fan hardware lines.

## Vendor-specific Findings

See L3. Notable structural observations: PoultryPlan and Eggbase both sell egg-packing-station capability as a separate solution/module beside the farm product — packaging evidence that the farm-side Type ends at the farm gate. Big Dutchman and Fancom are equipment vendors whose management software binds controller data to houses and flocks — the equipment-integrated realization of the same record model, not a different Type.

## Rejected Findings

- **"Individual bird identity is the core"** — rejected: no sampled product tracks birds as individuals; flock/batch population records with counts are universal. (Contrast with dairy, where individual identity is definitional.)
- **"Climate-control automation is definitional"** — rejected: manual-entry products (Farmbrite, Eggbase's data inventory) satisfy the core; paper-era practice satisfies it; controller integration is a realization posture.
- **"Egg production recording is definitional"** — rejected: broiler-focused products record growth, not eggs; the invariant is the cycle's production output, not eggs specifically.
- **"The hatchery is a separate Type"** — not supported: the sampled chain product treats the hatchery as one solution in the same platform (OptiHatch), and breeder/hatchery records appear inside poultry products (Eggbase breeders segment; Farmbrite hatchery-to-harvest). Treated as a segment variant. (No hatchery-only vendor was sampled; see Uncertainties.)
- **"PoultryCare is a poultry farm management product"** — rejected: poultrycare.in is a veterinary-medicines company (supplements), not software. Product mismatch; dropped from the sample.
- **"Poultry Farm Management ≈ Livestock Management with different species"** — rejected: the production-system shape differs (short-cycle batch flocks in houses vs long-lived breeding herds as individuals/mobs); see Boundary Findings.

## Boundary Findings

- **vs Livestock Management** (§20, processed 2026-09-09) — pre-hung FORWARD FLAG DISCHARGED from this side: keep-both RATIFIED. Seam = production-system shape, exactly as the livestock pass predicted: this Type manages short-cycle batch flocks placed into houses (all-in/all-out rhythm, population-level records, cycle closure with clean/rest), while Livestock Management manages long-lived breeding herds as individuals or mobs with open-ended event histories. Removal tests: remove the batch-cycle shape and hold long-lived individually-identified breeding animals → Livestock Management; hold batch flocks in houses with placement→clearance cycles → this Type. Straddling pole: Farmbrite (multi-species whole-farm suite with a poultry module) — center-of-gravity test applies per the dairy pass naming-drift note; its poultry page leads with houses/batches/FCR/laying %, i.e. the poultry core inside a whole-farm package.
- **vs Dairy Farm Management** (processed): dairy = individually identified animals + lactation cycle + milk production per lactation; poultry = batch flocks + placement-to-clearance cycles + population-level production. Both are animal-production systems of record; the unit of record and the cycle differ.
- **vs Swine Management** (§20, unprocessed): expected to share the batch-production seam (all-in/all-out, per-unit populations). This pass records the seam from the poultry side; the swine pass should confirm from its own sample. No directory change made.
- **vs Aquaculture Management** (processed): structurally closest cousin — per-unit populations across bounded cycles with standing-stock accounting. Difference: rearing medium and unit taxonomy (water units with water-quality parameters vs poultry houses with climate parameters), plus species. The aquaculture pass already characterized poultry as batch/population production — consistent.
- **vs Feed Management** (processed): feed consumption, feed deliveries, and FCR are recorded here as a layer; ration formulation and feed supply as a managed subject belong to Feed Management. PoultryPlan's OptiFeed (feed delivery scheduling from flock data) and Eggbase's feed-supplier segment sit at the seam — chain packaging, not the farm core.
- **vs Farm Management Platform** (processed): whole-operation scope (land + crops + livestock + money) vs poultry-production scope. Remove the whole-operation scope → the poultry slice = this Type. Farmbrite straddles at packaging level.
- **vs Agricultural IoT Platform** (§14, processed): climate controllers, sensors, and auto-weighing are capture hardware bound to houses/flocks here; the device-fleet-as-managed-resource product is the IoT Type. The equipment-integrated pole (Big Dutchman, Fancom) realizes the record model through controllers — the object of work remains the flock-in-house.
- **vs egg packing station / grading / processing / Food Manufacturing ERP**: downstream of the farm gate. PoultryPlan ships OptiGrading/OptiSlaughter and Eggbase a packing-station segment as separate solutions — the farm-side Type ends at clearance/market; post-farm processing is other Types' territory.
- **vs veterinary practice management**: vets are data consumers/collaborators (Eggbase sells a veterinarian segment; interventions recorded with prompts); the clinic-side system of record is a different category.
- **"去掉什么就变成另一个 Type" 判据**: remove the batch-cycle shape (hold long-lived individuals) → Livestock Management; add the lactation/milking cycle → Dairy Farm Management; move the rearing unit into water → Aquaculture Management; make the ration the subject → Feed Management; add whole-operation scope → Farm Management Platform; make the device fleet the object → Agricultural IoT Platform; move past the farm gate (grading/packing/processing) → food-processing Types.

## Historical / Market-Sample Check (§24)

- Paper-era practice: a flock card per house (placement date, breed, number placed), a daily egg book or weighing sheet, a mortality log, feed delivery notes, an end-of-flock summary compared against the breed standard — satisfies all three L0 structures with no software, sensors, or cloud. The definition holds for the pre-digital lineage.
- 1990s–2000s desktop poultry software generation satisfies: house/flock records, daily production entry, end-of-flock reports — no cloud/mobile/controllers in the core.
- Smallholder/backyard pole (one coop, one flock, manual records) satisfies: one production unit, one placed flock, a record stream, and a mental performance loop.
- Regional products (UK egg industry with salmonella testing regimes, NL integrated chains, US broiler belt) all satisfy without naming any specific regime in the core.
- Equipment-integrated house management (climate computers with production recording) is not a modern regression — it is the traditional integrated form; standalone record-keeping is the other pole. Both fit; neither is definitional.

## Uncertainties

- **US broiler-integrator pole not directly documented**: M-Tech Systems (the obvious US candidate) was unreachable twice; no US integrator-side vendor documentation was fetched. The chain-integration evidence comes from PoultryPlan (NL) and Eggbase's segments (UK). Claims about integrator-side machinery (contract growing, settlement per flock) are NOT made.
- **Hatchery-only vendors not sampled**: hatchery evidence is limited to PoultryPlan's OptiHatch solution page and segment mentions elsewhere. The hatchery-as-variant treatment is stated at that evidence strength; a dedicated hatchery-management product population may exist and was not researched.
- **Farmbrite help center not fetched this pass**; Farmbrite claims rest on its official poultry solutions page (Tier 2). No precise operational details asserted for Farmbrite.
- **Big Dutchman / Fancom management-software detail pages not fetched** (BFN Fusion, FAY/FarmManager); their claims are kept at positioning level — the house-management framing and the controller-bound data model are documented, the internal object model is not.
- **Poultry360 unreachable** (2 failures); no NZ broiler-farm pole documented.
- **Exact KPI definitions** (FCR formulas, laying-% denominators, mortality windows) are vendor-specific; not canonicalized.
- **Swine Management leaf unprocessed**: the batch seam is recorded from this side only; joint confirmation pending that pass.

## Final Synthesis

Poultry Farm Management is the poultry operation's production system of record and daily management console. Its defining core is three jointly-held structures: the flock-in-house as the managed unit of record (batch populations with counts, breed/line, and age, placed into identified houses/coops — population-level records, never individually identified birds); the cycle-bound production record stream (placement → mortality/culls, weights, feed & water, the segment's output — eggs, hatching eggs, or growth — environment, and health events → clearance, with the unit cleaned/rested before the next placement); and the records → performance → decisions loop (FCR, laying %, mortality %, weight vs breed standard, benchmarks vs previous flocks and other farms, alerts, and reports driving placement, feeding, health, and marketing decisions). Individual bird identity, climate/sensor automation, specific segments (broiler/layer/breeder/hatchery), chain modules (transport, packing, processing), feed formulation, financial depth, and compliance machinery are common mature or variant structures, not the definition. The Type is the batch-flock pole of the livestock family: beside Livestock Management (long-lived breeding herds), Dairy Farm Management (lactation cycle), and Swine Management (same batch seam, pending its pass), with Aquaculture Management as the structural cousin in water and Feed Management as the interlocking feed-side discipline.
