# Research Notes — Aquaculture Management

Research date: **2026-09-06**

## Research Goal

Understand what "Aquaculture Management" software actually is, from real products: what its central records are, how a production cycle is modeled, which rearing activities are recorded, what hardware/data integration looks like, who uses it, and where its boundary lies against Fisheries Management, Livestock Management, and general Farm Management software.

## Initial Boundary

Working hypothesis before research:

- Aquaculture Management software supports the **farming of aquatic organisms** (finfish, shrimp, shellfish) in water-based production environments: ponds, tanks, raceways, sea cages, longlines/rafts, land-based recirculating systems.
- Likely core: production units + stocked living populations + rearing event records (feeding, water condition, mortality, treatments, growth) + harvest.
- Confusable neighbors: Fisheries Management (wild capture), Livestock Management (terrestrial animals), Farm Management Platform (land/crop), Agribusiness ERP (financial back office), Food Traceability Platform (post-harvest).
- Open question at start: is water-quality monitoring definitional, or only common? Is feeding definitional? (Shellfish are not fed — checked against this during abstraction.)

## Research Questions

1. What is the central record — production unit, batch/stock, or individual animal?
2. How is a production cycle modeled (stocking → rearing → harvest)?
3. Which rearing events are recorded: feeding, water quality, mortality, treatments, grading/moving, growth?
4. How is biomass/growth tracked (manual sampling vs sensors vs computer vision)?
5. What hardware/sensor/actuator integration exists, and is it standard or optional?
6. What roles and surfaces exist (office dashboard vs pond-side mobile vs feeding consoles)?
7. What planning/forecasting capabilities exist (yield, harvest scheduling, scenarios)?
8. What financial capabilities are bundled (costs, budgets, income)?
9. What regulatory/compliance reporting is supported, and how region-dependent is it?
10. What recorded at harvest, and does data flow downstream (traceability)?
11. Boundary questions: what separates this Type from Fisheries Management, Livestock Management, generic Farm Management, Agricultural IoT, Feed Management, Food Traceability?

## Representative Products

Selected for market representativeness (two species segments × four product philosophies × enterprise vs regional/SMB customer tiers):

| Product | Vendor | Segment | Philosophy | Customer tier |
|---|---|---|---|---|
| AKVA fishtalk / connect / observe / Smart camera | AKVA group (Norway) | Sea-cage finfish (salmon; also land-based) | Integrated hardware+software suite; biological+financial production control | Enterprise |
| Aquabyte (Weight, Lice, Welfare, Behaviour, Feeding, SmartDecision) | Aquabyte AS (Norway) | Sea-cage finfish (salmon) | Computer-vision data layer over pens | Enterprise |
| AquaExchange (NextFarm App + device line) | AquaExchange (India) | Intensive shrimp ponds | IoT-first ecosystem (feeders, power, water, AI counting) | SMB → mid-market |
| JALA App (+ Baruno device) | PT JALA Akuakultur (Indonesia) | Intensive shrimp ponds | Mobile-first, freemium cloud recording & management | Smallholder → mid-market |

## Sources

All fetches 2026-09-06. Evidence Layer A unless noted.

- AKVA group — Home / Our digital solutions: https://www.akvagroup.com/ , https://www.akvagroup.com/digital/solutions/
- AKVA group — AKVA fishtalk product page: https://www.akvagroup.com/fishtalk/akva-fishtalk
- Aquabyte — Home/products overview: https://aquabyte.ai/ (aquabyte.co failed with transport error; .ai used)
- AquaExchange — Home/products: https://aquaexchange.com/
- JALA — Home, JALA App page, FAQ hub, App Basic FAQ: https://jala.tech/ , https://jala.tech/app , https://jala.tech/faq , https://jala.tech/faq/jala-app (first fetch of /faq/jala-app timed out; second succeeded)

Source-access limitation: AKVA group gates user manuals, product sheets, and detailed documentation behind customer login ("Gain access to user manuals, product sheets, and other documents via login"). Detailed operational rules for AKVA products could not be directly observed; claims for AKVA are restricted to what its public product pages state. JALA's deeper how-to articles exist but were only partially fetched. Vendor numeric claims (e.g., AquaExchange "20,000 devices / 80,000 acres / 4 countries", Aquabyte "1.3 million daily images per camera / over 800 systems in pens") are Layer-A marketing self-claims, not independently verified, and are recorded only as vendor-reported scale.

## Product Observations

### Product A — AKVA group (AKVA fishtalk suite)

Key observations (Layer A, from public product pages; deeper docs gated):

- Positions its digital line as "precision aquaculture": monitoring and control of fish growth and health, precision feeding, early alerts for cleaning/maintenance of cages and equipment, monitoring of stress and behavior, escape tracking, control of water quality and temperature, management of sea lice. (Marketing-page phrasing — vendor framing, treat directionally.)
- **AKVA fishtalk**: "a digital system for planning, control and analysis of aquaculture production — both biological and financial. It provides full traceability from broodstock to harvest and is equally relevant for day-to-day operations and strategic management." Supports site level and company level, "from daily operations to five-year plans."
- Named key data points: **FCR, SGR, mortality, treatments, full traceability**; users can submit records via API; external sensors/data sources can be connected for "more accurate growth forecasts."
- Modular: core module **AKVA control** ("from broodstock to harvest"), **AKVA finance** ("Gain financial control through your biology"), **AKVA plan** (reporting system to compare scenarios for operational decisions), **AKVA control app** (mobile).
- Other digital products: **AKVA connect** (open platform for feeding performance and operations), **AKVA observe** (intelligent feeding assistant), **Smart camera** (digital surveillance and reporting).
- Cloud-based, open API (fishtalk 5 generation). Implementation consultancy + training offered.
- Not directly observed (gated): actual record structures, screen flows, permission models, regulatory report formats.

### Product B — Aquabyte

Key observations (Layer A, from official site):

- Camera systems deployed inside sea pens (HYDRA 360: fish health + feeding camera, integrated sonar and environmental sensors; Hammerhead: engineered for submerged pens). Vendor-reported scale: "1.3 million daily images per camera", "over 800 systems in pens", "8 years of data collection" (unverified marketing figures).
- Product line (User Portal surface): **Weight** (biomass, weight & growth estimation), **Lice** (automatic lice counting & forecast), **Welfare** (real-time welfare monitoring), **Behaviour** (continuous behavioral monitoring), **Feeding** (appetite prediction and sonar), **Decision Support** (SmartDecision — "short-term planning").
- Framing: insights "throughout the entire production cycle", enabling tracking of developments over time, early detection of changes, and action. Site has category facets: production phase, species, farming technology — species focus is salmon (Norwegian origin, global markets).
- This product is a **data/insight layer**: it does not (per its own pages) replace unit registers or financials; it feeds decision-making (feeding optimization, harvest timing per marketing claims).

### Product C — AquaExchange

Key observations (Layer A, from official site):

- Positions an IoT-first "One Smart Ecosystem" for shrimp farming around **four essentials: healthy shrimp, the right feed, clean water, and reliable power** — i.e., livestock, feed, water, and electricity are all first-class managed concerns.
- Device line (each paired with app control):
  - **PowerMon** (+APFC): real-time power/aerator monitoring with instant fault alerts — power failure is treated as a crop-killing risk.
  - **AquaBot** (automated feeding robot: precision movement, controlled dosage, app control), **Static Feeders** (100/200 kg, app-controlled), **Smart Scale** (real-time weight validation synced to feeder and app), **Feed Mon** ("feed only when shrimp demand it" — acoustic demand sensing to minimize waste and FCR), **CheckTray** (feed consumption + shrimp behavior monitoring).
  - **WaterMon**: GPS-enabled handheld water-quality device, "accurate, traceable, real-time water quality monitoring across ponds."
  - **Shrimp Counter**: AI-powered smartphone imaging to count post-larvae (PL) and shrimp for stock estimation.
  - **Patholense**: AI microscopy pathogen detection for early disease identification.
  - **Starter** (smart aerator controller), **PumpMon** (pump/flow monitoring), **ProBrew Master** (probiotics brewing), **Feed Mixer**.
- **NextFarm App**: "Comprehensive farm management application for data-driven decision making and operational efficiency."
- Value-add process beyond software: farm automation, flexible financing, disease insurance, direct market linkage (Layer A as vendor description; ecosystem services are vendor business model, not generic Type structure).

### Product D — JALA (JALA App)

Key observations (Layer A, from official site + FAQ):

- **JALA App** = "all-in-one shrimp farm management application"; web dashboard ("Control Ponds Effortlessly from One Browser Dashboard") + mobile app ("Daily Pond Recording Made Easy... Record daily activities directly at the pond, securely stored, and accessible anytime from your phone", works **offline**).
- Recording: "**40+ Farming Parameters** — Record water quality, feed, and shrimp growth in detail, all in one app"; "Quick Daily Logs — Input water quality, feed, and activities directly from the pond."
- Monitoring: "Pond and Cycle Monitoring", "Data Charts and Trends", "**Cultivation Estimation** — Predict yields more accurately" (harvest forecasting on mobile too).
- Team: "Involve owners, managers, and technicians with **customized access** for smooth teamwork."
- Tiers (FAQ): **Basic** (free): recording + monitoring, shrimp prices, shrimp news, disease info. **Pro**: Excel input (bulk import), cultivation analysis charts, **Financial Management (Expenses, Incomes, Assets, Overview)**, cultivation report, financial report, **stock management**. **Plus** (mobile): smart input, chemical prediction.
- Subscription is priced **per pond and per cycle** (monthly / annual / per-cycle options) — direct evidence that *pond* and *cycle* are the licensed/operational units of this Type.
- Companion ecosystem (vendor-specific): **Baruno/Baruni** water-quality measurement device; JALA Harvest (harvesting service), JALA SmartFarm (joint-operation program), JALA Lab (disease health check & diagnosis), ShrimpHub (community), Shrimp News / Shrimp Prices (market info).

## Cross-product Comparison

| Dimension | AKVA fishtalk suite | Aquabyte | AquaExchange | JALA App |
|---|---|---|---|---|
| Species segment | Sea-cage finfish (salmon); land-based too | Sea-cage finfish (salmon) | Shrimp ponds | Shrimp ponds |
| Central unit | Cage/site ("broodstock to harvest", site & company level) | Pen (camera system per pen) | Pond | Pond (subscription per pond; monitoring per pond & cycle) |
| Production cycle explicit? | Yes (broodstock→harvest; 5-year plans) | Yes ("entire production cycle") | Yes (seed to harvest framing) | Yes (cycle monitoring; per-cycle pricing) |
| Rearing event recording | Records incl. treatments, mortality; API submission | Derived from CV imagery (weight/lice/welfare) | App + devices auto-record | Manual daily logs (40+ parameters), offline mobile |
| Feeding | Precision feeding (connect/observe) | Appetite prediction + sonar | Automated feeders + demand sensing + FCR focus | Feed recorded (manual), analysis in charts |
| Water condition | "Control of water quality and temperature" | Environmental sensors on cameras | WaterMon GPS handheld; "clean water" essential | Water quality recording; Baruno device |
| Mortality / stock accounting | Mortality named as key data point | Biomass/weight estimation | Shrimp Counter for stock estimation | Growth recording; Pro stock management |
| Growth/biomass method | Growth forecasts from records + external sensors | CV weight/biomass estimation (core) | AI shrimp counting (smartphone) | Growth sampling recorded manually |
| Hardware integration | Feeding systems, cameras, sensors (suite vendor) | Own pen cameras (sonar + environmental) | Own IoT device line (power, feed, water, counting) | Own water-quality device (Baruno) |
| Planning | AKVA plan (scenario comparison); 5-year plans | SmartDecision (short-term planning) | Harvest optimization framing | Cultivation estimation / harvest forecasting |
| Financial layer | AKVA finance (biology-linked) | Not observed | Financing/insurance as services | Pro financial management (expenses/incomes/assets) |
| Multi-user roles | Site vs company level; not detailed publicly | User Portal + Customer Success teams | App for farmers | Owners / managers / technicians, customized access |
| Health/disease | Sea lice management; stress/behavior monitoring | Lice counting + forecast; welfare indicators | Patholense pathogen detection | Disease info content; JALA Lab service |
| Compliance/traceability | "Full traceability from broodstock to harvest"; escape tracking | Not observed | Not observed | Not observed |

Layer-B commonalities (observed across ≥3 of 4 products): production-unit register (pond/cage/pen/site); production cycle as the operative time-bounded span; rearing event recording (feed, water, mortality/stock state); growth/biomass estimation; harvest as output; hardware/sensor integration; dashboards/charts; mobile or field-side access; multi-user roles; health/loss monitoring.

## Canonical Model

### L0 — Defining Invariant (minimal)

1. **Identified aquatic production units** — the farm's water-based production containers (ponds, tanks, raceways, cages, lines) held as managed records.
2. **Stocked living population per unit, across a production cycle** — aquatic stock is placed in a unit (stocking) and tracked as a population over a bounded rearing span; individual-animal identity is not the norm.
3. **Rearing event records attached to the unit/population** — dated operational events and observations (feeding, water condition, mortality, treatment, growth sampling — content varies by species) accumulated during the cycle.
4. **Cycle quantity accounting ending in harvest** — the running account of stock quantities (count and/or biomass) through stocking input, growth, and losses, with harvest (partial or total) as the cycle-closing production event.

Remove any one: without units it is generic livestock/herd software; without a stocked living population it is an IoT/monitoring platform; without rearing event records it is a registry; without cycle accounting and harvest it is a sensor dashboard, not farm production management.

### L1 — Common Mature Structure (cross-product)

- Water-quality monitoring (manual entry or sensor feeds) — near-universal in the sample
- Feeding management for fed species (records, rates, feed-conversion metrics; optionally feeder control)
- Mortality recording and standing-stock update
- Growth / biomass estimation (manual sampling, CV, sonar) and yield/harvest forecasting
- Sensor/actuator integration (oxygen/temperature probes, feeders, aerators, cameras, power monitors)
- Field-side mobile recording (often offline-capable) + office web dashboard
- Alerts and threshold monitoring
- Charts/trends, cycle reports, cycle-vs-cycle comparison
- Multi-user roles with customized access (owner/manager/technician patterns)
- Planning support: scenario comparison, harvest scheduling, short-term decision support

### L2 — Variant / Optional Structure

- Regulatory/compliance and traceability depth (region-dependent; strongest in regulated salmon farming: lice, escapes, reporting; enterprise traceability "broodstock to harvest")
- Financial layer (costs/expenses/income/assets, biology-linked costing/budgeting)
- Automation posture: automated feeding control, demand-based feeding, aerator/power automation (species/region dependent)
- Species-specific modules: sea-lice management and welfare indicators (salmon); post-larvae counting, probiotics, chemical prediction (shrimp); hatchery/broodstock management
- Business-model extensions: input supply, harvest services, financing, insurance, market linkage (vendor ecosystem plays)
- Deployment: cloud SaaS vs hardware-bundled/on-premises legacy; open APIs
- Scale features: multi-site/company portfolio, five-year planning

### L3 — Vendor-specific (kept out of the final document)

- AKVA: module names (fishtalk 5, connect, observe, Smart camera), named metrics FCR/SGR, open API positioning, consultancy model, gated manuals
- Aquabyte: HYDRA 360 / Hammerhead camera hardware, SmartDecision tool, vendor-reported image/system counts
- AquaExchange: PowerMon/APFC power infrastructure, Feed Mon acoustic demand sensing, Shrimp Counter, Patholense, ProBrew Master, financing/insurance/market-linkage process
- JALA: "40+ parameters" packaging, pond/cycle subscription pricing, Baruno device, Shrimp News/Prices, JALA Lab, SmartFarm, ShrimpHub

## Vendor-specific Findings

- Per-pond/per-cycle subscription pricing (JALA) is a business-model choice, not a Type property.
- Power reliability as a first-class managed concern (AquaExchange PowerMon) reflects land-based shrimp-pond electrification in its markets; sea-cage products do not feature it.
- Computer-vision lice counting & welfare scoring (Aquabyte) is a salmon-region response to salmon-specific biology and regulation.
- "Full traceability from broodstock to harvest" (AKVA) is an enterprise-suite claim; smaller-farm products in the sample do not advertise genealogy-level traceability.

## Rejected Findings

- **"Water-quality sensor integration is definitional"** — rejected as L0: JALA's free tier is manual recording; historical systems were manual. Sensor integration is L1/L2 (common, optionally deep).
- **"Feeding is definitional"** — rejected as L0: shellfish aquaculture does not feed; feeding management is species-dependent (L1 for fed species).
- **"Financial management is definitional"** — rejected: JALA Basic (free, recording/monitoring only) is a valid instance; finance is a common module (L1/L2).
- **"Individual-animal identity tracking is the core"** — rejected: the sample tracks populations per unit (CV estimates distributions, pond counts, biomass); individual identity appears only for broodstock contexts. Population-level recording is canonical.
- **"Full life-cycle genealogy/traceability is definitional"** — rejected as L0: only the enterprise product claims broodstock-level traceability; smallholder products do not. L1/L2.
- **"Aquaculture Management ≈ Fisheries Management"** — rejected: no sampled product manages wild-capture stocks, vessels, quotas, or landings; all manage reared populations in owned production units.
- **"Aquaculture Management is just an Agricultural IoT Platform for water"** — rejected: device data is bound to production units and cycle accounting; the object model, not the plumbing, defines the Type.

## Boundary Findings

- **vs Fisheries Management** (adjacent leaf, same directory section): distinct Types. Fisheries Management targets wild stocks, capture effort, vessels, quotas, landings, stock assessment. Aquaculture Management targets reared populations in owned production units with stocking/feeding/harvest. Remove the production-unit register + stocking/harvest cycle and add capture/quota/vessel objects → you are in Fisheries Management. Verified distinct; no taxonomy conflict.
- **vs Livestock Management**: structurally similar (population + events + health + feed) but the rearing medium is water and the unit taxonomy is aquatic (pond/cage/tank/line); water condition is a managed production parameter. Livestock systems model barns/paddocks and (often) individual animals or flocks. Boundary is real but the closest structural cousin; a product that models only generic "animals + events" without water/production-unit semantics would not be recognized as aquaculture-specific.
- **vs Farm Management Platform**: land/field/crop-centric; an aquatic producer is not served by field records. A generic farm platform with a small fish-record module remains a Farm Management Platform; the Type here is defined by the aquatic production model being primary.
- **vs Feed Management** (separate leaf): Feed Management concerns feed formulation/inventory for feed operations; aquaculture feeding is an execution/recording activity inside the rearing loop.
- **vs Agricultural IoT Platform**: aquaculture IoT devices exist, but this Type binds their data to units/populations/cycles and adds production accounting; IoT platforms stop at device data.
- **vs Food Traceability Platform / Food Manufacturing ERP**: downstream of harvest. Enterprise aquaculture suites may extend traceability upstream to broodstock, but post-harvest processing/distribution is a different Type.
- **vs Marine Fleet Management / Vessel Operations**: support vessels/workboats for cage sites are logistics objects, not stock; different operational domain.

## Uncertainties

- **Shellfish coverage unverified**: none of the four sampled products advertises shellfish (oyster/mussel) management. The claim that the L0 model accommodates shellfish (units = lines/rafts; unfed stock) is an analytic inference, not an observed product — flagged as such. Species breadth of mainstream products may be narrower than the Type concept.
- **Exact compliance/reporting modules** not directly observed (AKVA documentation gated; no regulatory-report screenshots fetched). Only "escape tracking" and sea-lice management surfaced publicly for AKVA; Norwegian regulatory specifics not confirmed.
- **Numeric scale claims** (devices, acres, images/day, systems in pens) are vendor marketing figures, unverified.
- **Hatchery/broodstock depth**: AKVA claims broodstock-to-harvest scope; other products' hatchery support unverified.
- **Historical product lineage** (pre-IoT salmon systems of the 2000s) not independently researched; the §24 historical check is satisfied analytically (paper-diary-era recording still fits L0) rather than by fetching an archived product's manual.

## Final Synthesis

Aquaculture Management software is farm-operated production management for reared aquatic organisms. Its world model: a farm's water-based production units hold living stock populations; each population lives in a unit across a bounded production cycle; during the cycle the farm records rearing events (feeding where applicable, water condition, mortality, treatments, growth); the system maintains standing-stock quantities and closes the cycle with harvest. Around this minimal core, mature products add water-quality monitoring and sensor/actuator integration, feeding management, growth/biomass estimation and yield forecasting, field-side mobile recording and dashboards, roles, alerts, and reporting; enterprise products add financial control, planning, traceability, and multi-site portfolio management; regional/species contexts add compliance depth and automation posture. The Type is distinct from Fisheries Management (wild capture), from generic Farm Management (land/crop), and from Agricultural IoT (device plumbing), and is structurally closest to Livestock Management while differing in rearing medium, unit taxonomy, and population-level (not individual-animal) recording.
