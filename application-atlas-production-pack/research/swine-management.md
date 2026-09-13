# Research Notes — Swine Management

## Research Goal

Understand what swine (pig) production management software actually is as an Application Type: what it holds as records, what events it captures, how records become decisions, how it is structured across the swine production phases (breeding herd vs growing pigs), and where its boundaries lie against Livestock Management, Poultry Farm Management, and Dairy Farm Management.

## Initial Boundary

Temporary hypothesis at start:

- Core use: system of record + daily management console for pig production operations — both the breeding herd (sows) and growing/finishing pigs.
- Likely tension: swine appears to span TWO production shapes — individually identified sows with a recorded reproductive cycle (dairy-like) AND batch/all-in-all-out growing flow (poultry-like).
- Two forwarded flags awaited this pass: the livestock-management pass expects a joint review on the batch-vs-breeding-herd seam ("assign by production-system shape, not species lists"); the poultry-farm-management pass expects confirmation that swine shares "the same batch-production seam".
- Nearest neighbors: Livestock Management, Poultry Farm Management, Dairy Farm Management, Feed Management, Farm Management Platform, Agribusiness ERP, Agricultural IoT Platform, Research Animal Facility Management.

## Research Questions

1. What is the unit of record — individual sows, litters, batches, pens, sites? Does it differ by production phase?
2. What event vocabulary does the system record around the swine production cycle (service, scan, farrowing, fostering, weaning, transfer, sale)?
3. What performance measures drive decisions (farrowing rate, PSY, litter size, mortality, growth, FCR, closeout economics)?
4. How are growing pigs managed — batch/all-in/all-out machinery, flow management, closeout?
5. How does multi-site pig flow appear (sow farm → nursery → finisher; transfers between sites)?
6. What integrations exist (electronic sow feeding, RFID/EID, genetics companies, slaughterhouses/packers, feed suppliers, accounting)?
7. Where is the money (cost reports, budgets, closeout, packer settlements)?
8. What roles use the system and through what surfaces (barn mobile vs office)?
9. Boundary: how does this differ from generic livestock management, poultry, dairy?
10. Historical check: would paper-era swine record keeping satisfy the core?

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different tiers:

1. **PigCHAMP** — classic sow-farm records + industry benchmarking specialist (30+ years, 40+ countries); data-collection/interpretation pole; US heritage, "Swine Management Software" self-label.
2. **AgroVision (PigVision / PigExpert)** — NL/EU records-first herd management for sow and grower farms; physical + financial performance; weekly monitors, quarterly benchmarks; consultant-facing tools.
3. **Cloudfarms** — cloud SaaS pig production suite (Slovakia/EU); Sow Management + Wean-to-Finish Management + Breeding & Multiplication; mobile-first capture; large-holding pole.
4. **MetaFarms** — US integrated production platform (SOW / FINISH / SALES / INSIGHTS); grow-finish groups + closeout + packer integration; integrator/large-system pole.
5. **Agrisys** — Danish equipment-integrated pole (successor of the Nedap pigs division as of 2023); Control System over feeding/weighing/welfare installations; barn-automation ecosystem philosophy.

## Sources

- PigCHAMP — official site and product pages (retrieved via search-index content of www.pigchamp.com; direct fetch timed out ×2): root (/), /benchmarking, /products/reproductive/reports, newsletters/january-2026.
- AgroVision — direct fetch of https://agrovision.com/uk/software/pigs/pigvision/ plus official pages agrovision.com/uk/software/pigs/, /software/pigs/ (international), /pigexpert/, blog "New: Sows dashboard", Google Play listing of PigVision Mobile.
- Cloudfarms — direct fetch of https://en.cloudfarms.com/ root plus /services/sow-management/ and /services/wean-to-finish-management/.
- MetaFarms — official pages retrieved via search-index content of www.metafarms.com (direct fetch blocked 403): /solutions.html, /sow.html, /finish.html, /sales.html, FINISH fact-sheet PDF.
- Agrisys — official pages retrieved via search-index content of en.agrisys.dk (direct fetch transport error): frontpage, Control System, AutoPig, AirSys, profile; Nedap division-transfer statement via nedap-livestockmanagement.com/pig-farming-activities/.

## Product Observations

### PigCHAMP

Evidence layer: A (official pages via search-index content; direct fetch unavailable — claims kept to listed features).

- Self-labels "Swine Management Software": "data collection, management and interpretation"; 30+ years; customers in 40+ countries.
- PigCHAMP Reproductive: "more than 40 standardized reporting options"; categories include Performance Reports, Production Analysis, Herd List, Data Reports, **Action List Reports**, Miscellaneous.
  - Production Summary: "services, farrowings, piglet losses, weanings and inventory on the farm during the selected reporting period".
  - Comparative Production Summary (side-by-side farms in same database/group); Performance Trend Analysis (five key areas); Farrowing Control Chart; Performance Analysis by Group; Herd Inventory. Reports customizable, filterable, drill-down to individual sows; edit/save/export.
- Benchmarking program since 2001: participants send data in quarterly; customized report benchmarking the farm against participating farms; quarterly/yearly summaries; annual Benchmark Magazine. Newsletter KPI vocabulary: Repeat Rate, Farrowing Rate, P/S/Y (pigs weaned per sow per year), Death Rate, Pre-weaning Mortality, Cull Rate; total born/litter; wean sow mortality; percentile comparisons (mean, median, upper/lower 10th).
- PigCHAMP Mobile: real-time reproductive data input, validation to minimize entry errors, offline/intermittent mode (Online or Client Hosted Application). Benchmark submission historically by sending a backup file; online customers' data "automatically included".

### AgroVision (PigVision / PigExpert)

Evidence layer: A (direct fetch of official UK page; other pages via search-index content of official domain).

- PigVision: "complete and advanced herd management system designed for sow and grower farms"; processes "essential physical and financial performance data"; real-time; entry/access "with or without internet connection"; registers "production, medicine, feed, environment and finance" key figures; dashboards and diagrams; detects deviations in real time.
- Sow card scanned and data entered in the barn ("Scan the sow card and immediately enter the data in the barn").
- Data exchange "with key partners, including slaughterhouses, breeding companies, and feed suppliers"; flexible dashboard setup; one-price package.
- Production Monitor (UK): weekly report generated from PigVision data, to inbox/PC/mobile, customisable layouts, "can be automatically sent to your vet, consultant, or any 3rd party".
- PigVision Mobile (Google Play): actions — service, create boar, farrowing, abortion, death piglet, transfer piglet, weaning, nursing sow, exit sow, relocate sow, medication, pregnancy test, numbering piglets, sow conditions; "a sowcard with all cycle information"; **action lists for services, farrowings and weanings**; custom worklists; animal list with filters/sortings; sow selected by sow number, tattoo, or Sanitel number; barcode/QR scanner; RFID scanners supported; works online and offline.
- PigExpert (sibling product): "combines all data about piglets, sows, and fattening pigs into one clear system … from gilts to sold fattening pigs"; weekly monitors + quarterly benchmarks (compare with other users); mobile app without internet; ProductionMonitor sows (weekly key figures); integrations with scales and feeding systems; Feed Monitor (feed intake via feeding-system links, deviations, departmental overviews); ConsultantMonitor (all customers' farms weekly — consultant-facing); KPIs named in customer quote: feed conversion, average daily growth (fattening pigs), total born, mortality rates and reasons; Track & Trace module (life-cycle traceability back to the slaughterhouse).
- AgroVision Pigs page: "software for sows, growers, and closed farms, and advisory tools for industry consultants"; new cloud Sows solution to "follow individual animals throughout their life cycle"; group-level or individual-animal views; API for pig-industry agribusinesses; farmers, employees and external parties work in the same program.

### Cloudfarms

Evidence layer: A (direct fetch of official pages).

- Positioning: "complete suite of services … oversight of your entire production and workflow data. No matter the size of your operation."
- Services: Sow Management; Wean-to-Finish Management; Breeding & Multiplication Management; Boar & Semen Management; Workflow & Alert Management; Data Analytics; Individual Animal Tracking; Traceability from Field to Fork. Demo form farm types: One/Multiple Farms – Sows; One/Multiple Farms – Finishers; Breeding & Multiplication Farm.
- **Sow Management Core Package**: KPI Goals; Stocktaking; Feed consumption; Medicine management/usage/prescription/multi-prescription; Herd overview; Animal transfers; Relocations; Buying; Selling; Dead animals; **Sow card (1-click full history)**; **Serving; Scanning evaluation results; Farrowing; Weaning; Fostering; Abortions**; Back fat registration; Problematic sows management.
- Mobile app (shared): recordings without internet + instant validation; animal card and events history; service/scan/farrowing/weaning/fostering registration; movements; death/sale/buy; back fat/body condition scoring; **semen tapping**; feed consumption/movements; medicine usage + planned medicine; stocktaking; farrowing alerts; lactation list; weighting; automatic information audit; QR reading; **ear tag readings (UHF, LF, RFID)**; batch creation.
- Reports: production report, efficiency report, KPI management, sow analysis, sow statistics, fertility report, service list, server success report, boar success report, feed consumption report, parity breed report, dead insight report, stocktaking, transfer report, statistics, accounting report, cost report.
- **Wean-to-Finish Core Package**: KPI Goals; Stocktaking; feed consumption; medicine management; herd overview; transfers; relocations; buying; selling; dead animals; "Weaners and finishers support"; **Easy batch overview; Movement registration; Weight registration; Growing curve; Batch management; Flow management**.
- Add-ons: Forecasting, Simulation & Budgeting ("reflect animal shipments between farms", holding-level consolidation); Multi-Site Reports & Benchmarking (KPI comparison own-farm-to-own-farm / to external farm / to industry average; communities ranking of farm sites; per-KPI share permissions).
- Integrations: Electronic Feeding Systems (Big Dutchman, BoPil, Jyga, Weda, Nedap, Skiold, Schauer, Agrisys); genetics companies (Danbred, PIC, Topigs Norsvin, Genesus, DanBred, DNA Genetics, Hermitage…); ear-tag readers (Allflex, Agrident, Tru-Test…); ERP/BI; GraphQL exports. Data protection: 2FA, per-user rights, Excel/PDF exports.

### MetaFarms

Evidence layer: A (official pages via search-index content; direct fetch blocked 403 — claims kept to listed features).

- Platform framing: control and visibility "over their entire operation by removing silos of information"; hundreds of integrations with feed mills, financial software, packers, hardware vendors (ESFs, RFID); Report Manager (customize, schedule, email reports; Excel compatibility); runs on standard devices.
- **SOW**: "next generation record keeping system for the swine industry's leading producers to track performance, compare to industry benchmarks and make data-driven management decisions. From a single unit farm to large integrated operations." SOW ENTERPRISE (premium): daily visibility; snapshot of KPIs; mobile app on consumer tablets (Android/iOS) with offline recording and data-validation warnings; "Individual ID entry with multiple events, events for multiple IDs, and batch treatments"; "Call-up complete sow history on handheld device"; customizable interface/reports per producer, site, barn and user; user-based security roles; ESF integration (Nedap, AP Schauer, others); Allflex RFID readers; QR codes; "Eliminates need for data bureau".
- **FINISH**: "tracking your grow finish (nursery, finish and wean-to-finish) operations for both **active group and closeout** performance"; records inventory events, health updates, expenses, feed deliveries, carcass data; MORTALITY mobile app (record on device, required fields and flags for missed entries, daily or weekly, mortality trends, alerts for missed recordings, per-producer/site/barn/user setup, bilingual English/Spanish, user-based security); reports by flow, business unit, producer, health status; roll-up organizational → individual barn; "Traceability through entire production lifecycle"; integrations with accounting, feed and packer software.
- **SALES**: market hog sales analytics; daily sales data imported from packers "applied seamlessly to your FINISH group performance closeout"; individual carcass data (backfat, loin, lean %, yield); target weight brackets (Packer Matrix); five weight categories; sort loss monitoring; track loads, premise IDs (SecureReady program), producer codes, tattoos; transit loss (dead in transit/yard); integrations with 20+ packer software systems.
- Customer quote: "quick, secure roll-up and summary reporting across our system" (Iowa Select Farms).

### Agrisys

Evidence layer: A (official pages via search-index content of en.agrisys.dk; direct fetch transport error).

- Positioning: "solutions for modern, professional pig producers with a focus on individual feeding, weighing systems, welfare, management, and biosecurity"; "Whether you run a single herd or an integrated production".
- Control System: "connects feeding, weighing and results so you can document, analyse and act"; one platform for feeding, weighing, welfare; accessible from any device; set up feed curves, monitor weight development; "full history is stored, allowing you to compare across **batches, barn sections, or entire herds**"; open APIs "into external management systems"; real-time + historical data.
- AutoPig®: automatic in-pen weighing (weight, activity, feed and water intake, pen temperature per passage); "weight curves, activity patterns, and event notes, you can compare progress against both **standard curves and previous groups**"; early detection of illness/feeding issues; app-based.
- AirSys: portion feeding system "in all barn sections – from weaners to sows and finishers"; LinkedIn product set: electronic sow feeding, dynamic separation, heat (brunst) detector, sow monitor, batchsys, chainsys, multifase, weighing, pig performance testing (PPT core), welfare/bedding distribution.
- Company: founded 2009, Herning, Denmark; the Nedap N.V. pigs division "transitioned to AgriHub (Canada) and Agrisys (Denmark)" as of Nov 15, 2023 (sales, support, parts for Europe/Asia ex-China) — Agrisys carries the Nedap sow-management lineage (ESF, heat detection, separation, weight monitoring; "management by exception" software reporting points of attention; track and manage the complete cycle of the animal; share data with slaughterhouses, breeders, veterinarians, feed suppliers).

## Cross-product Comparison

| Dimension | PigCHAMP | AgroVision (PigVision/PigExpert) | Cloudfarms | MetaFarms | Agrisys |
|---|---|---|---|---|---|
| Phase coverage | breeding (sow) records; breed-to-wean benchmarking database | sows AND growers ("from gilts to sold fattening pigs") | Sow Management + Wean-to-Finish (one platform, two services) | SOW (breeding) + FINISH (nursery/finish/wean-to-finish) + SALES | all sections — "weaners to sows and finishers" (barn side) |
| Unit of record — breeding | individual sow (drill-down to individual sows; sow history) | individual sow (sow card with all cycle info; sow number/tattoo/RFID) | individual sow (sow card 1-click full history; ear tags UHF/LF/RFID) | individual sow ("Individual ID entry", "complete sow history") | individual sow (ESF station identification; sow monitor) |
| Unit of record — growing | (wean-to-finish benchmark DB) | fattening pigs / batches (PigExpert; growers app) | batch ("Easy batch overview", Batch management, Flow management, batch creation) | group ("active group and closeout"; batch treatments) | batches ("compare across batches") |
| Cycle events recorded | services, farrowings, piglet losses, weanings; action list reports | service, farrowing, abortion, transfer/death piglet, weaning, nursing sow, exit sow, relocate, pregnancy test, medication | serving, scan evaluation, farrowing, weaning, fostering, abortions; transfers; buy/sell/dead | event entry per individual ID / batch treatments; inventory events; health updates | complete animal cycle tracked via ESF/heat/separation/weight (management by exception) |
| Growing-phase records | — | weights, feed (Feed Monitor via scales/feeding systems), FCR, ADG | weight registration, growing curve, feed consumption, movement, mortality | inventory events, feed deliveries, expenses, carcass data, MORTALITY app | weight/feed/water/activity per passage vs standard curves and previous groups |
| Performance machinery | 40+ report types; action lists; Farrowing Control Chart; trend analysis | dashboards; weekly ProductionMonitor; quarterly benchmarks; deviations in real time | KPI Goals; real-time reports; sow analysis; fertility report; parity/boar reports | compare to industry benchmarks; snapshot; roll-ups flow→business unit→barn | control-system dashboards; batch/barn/herd comparisons; early-warning from weight/activity curves |
| Benchmarks | quarterly/annual industry benchmarking (farrowing rate, PSY, repeat, mortality, cull) | vs other users (quarterly); targets in dashboards | own farm vs own farm / external farm / industry average; communities ranking | industry benchmarks | standard curves; previous groups/batches |
| Medicine/health | treatments within reproductive record set | medication registration; vets receive records | medicine management, usage, prescription, multi-prescription; planned medicine | health updates; treatment records | heat detection, health signals from feeding/weighing data |
| Money layer | benchmark program includes cost-of-production data | finance figures registered; financial performance | accounting report, cost report; budgets; forecasting | expenses; closeout; packer sales data; accounting integration | financial results ("efficiency, animal welfare and financial results") |
| Capture surfaces | desktop/client-hosted + mobile app with offline | office + mobile apps (sows, growers) offline; sow-card scanning | cloud web + mobile in-barn (offline, validation, audit) | consumer tablets/mobile; MORTALITY app; off-line feature | barn control system + app (AutoPig) |
| Integrations | (benchmark submissions; backup files) | slaughterhouses, breeding companies, feed suppliers, vets; scales/feeding systems | ESF vendors, ear-tag readers, genetics companies, ERP/BI | ESFs, RFID, packers (20+), feed mills, accounting | open APIs to external management systems; own feeding/weighing/welfare hardware |
| Deployment vocabulary | Online or Client Hosted Application | server-hosted or on-farm; cloud Sows solution | cloud SaaS; private cloud option; no local servers | cloud platform (MAP) | device-accessible control platform; open APIs |

## Abstraction Levels

### L0 — Defining Invariant

Three jointly-held structures. Remove any one and the product stops being swine production management:

1. **The swine production population as persistent records at phase-matched granularity.** The pigs being produced are held as records whose granularity matches their production phase: breeding herd (gilts, sows, boars) as individually identified animals accumulating histories across reproductive cycles (sow card / sow record with full cycle history — present in every breeding-capable sample); growing pigs (weaners, finishers) as batch/group records — counts with composition and location, the unit through which growth, feed and mortality are managed (batch/group management present in every growing-capable sample). The population persists across cycles and outlives individual events. Remove → a static animal register or an anonymous count ledger.
2. **The dated event stream in the swine production-cycle vocabulary, bound to the phase-appropriate unit.** Breeding side: service/insemination, pregnancy check/scan result, farrowing with litter outcome (born, losses), fostering/nursing, weaning, abortion, exit (cull/death/sale) — the cycle recorded per sow and per litter. Growing side: placement/receipt, weights/growth, feed, health/treatment, mortality, sales/movements — recorded per batch. Plus inventory transactions (buy/sell/dead), transfers between rooms/barns/sites, medicine usage. Every sample records exactly this vocabulary. Remove → a herd book with no operational content.
3. **The records → performance → decisions loop.** Accumulated records are continuously converted into production measures (farrowing rate, repeat rate, litter size, pre-weaning mortality, pigs-weaned-per-sow metrics on the breeding side; growth, feed conversion, mortality on the growing side), compared against targets, own history, other farms or industry benchmarks, and surfaced as action lists, alerts and dashboards that drive which sows to serve, scan, treat, wean or cull and which batches to adjust or market. Action lists and deviations/alerts appear in every sample. Remove → a passive archive; the "management" is gone.

Jointly-held load-bearing tests:
- 1 alone = static registry / herd book
- 2 without 1+2 = free-floating event log
- 3 without 1+2 = benchmark/report service over no farm record
- 1+2 without 3 = herd-book archive nobody manages with
- 1+3 without 2 = stale snapshot with no recorded work
- 2+3 without 1 = reporting over nothing

### L1 — Common Mature Structure

Present in most sampled products; not definitional:

- In-barn mobile capture with offline mode and entry validation (all five, in different forms)
- Sow card / animal card as the per-animal record surface (1-click full history)
- Action lists and worklists (services due, farrowings due, weanings due; custom worklists)
- KPI dashboards with own targets/goals; deviations surfaced in real time
- Medicine management including usage, planned medicine and prescriptions (Cloudfarms most explicit; AgroVision registers medicine; MetaFarms health updates)
- Feed consumption tracking; feed-system/scale integrations
- Inventory/stocktaking; buy/sell/dead registration; movements and relocations
- Weight recording and growth curves; standard-curve comparison (Agrisys, Cloudfarms)
- Multi-farm/multi-site roll-ups and consolidated reporting (Cloudfarms holding level, MetaFarms flow→business unit, AgroVision consultant view)
- Benchmark comparisons (own vs others vs industry — PigCHAMP program, AgroVision quarterly, Cloudfarms communities, MetaFarms industry benchmarks)
- External data exchange: slaughterhouses/packers, breeding/genetics companies, feed suppliers, vets/consultants
- Role-based access and per-user customization; audit/validation of entries
- Report libraries with export (Excel/PDF)

### L2 — Variant / Optional Structure

- Phase coverage of the individual product: sow-only (PigCHAMP Reproductive), grower-only (grower apps; Agrisys finisher barns), or full-cycle (PigExpert, Cloudfarms, MetaFarms platform)
- Production-system shape: single-site farrow-to-finish; multi-site flow (breeding → nursery → finisher with shipments between farms — Cloudfarms forecasting reflects animal shipments; MetaFarms flow filter); contract growing (US integrator pattern)
- Batch-management formalism (batch creation, weekly-batch rhythm, all-in/all-out) — strong in EU practice; US sample speaks of groups/flows/closeouts instead
- Breeding & multiplication / genetic-pyramid management; boar stud & semen management (separate Cloudfarms service; "create boar", semen tapping in PigVision)
- Individual identity for growing pigs (Cloudfarms sells Individual Animal Tracking as a separate service — optional, welfare/health-oriented)
- Equipment-ecosystem depth: control systems bound to the vendor's own feeding/weighing/welfare hardware (Agrisys; also the equipment vendors in Cloudfarms' integration list)
- Regional/national ID and traceability regimes (Sanitel number in PigVision; premise IDs in MetaFarms SALES; Track & Trace / field-to-fork modules)
- Welfare-machinery contexts (group housing, bedding/rooting distribution — Agrisys Welfare)
- Whole-farm suite embedding (Farmbrite-style multi-species suites carry a swine module — straddling pole)
- Chain modules beyond the farm gate (transport, packing, processing) — separate modules/products
- Money depth: from cost reports to closeout economics and packer settlements (MetaFarms SALES deepest in sample)

### L3 — Vendor-specific (Research Notes only)

- Cloudfarms: Day report; Communities ranking; named integration lists (Weda, BoPil, Jyga…); "reports automatically updating every 20 minutes"; Data Analytics service packaging
- MetaFarms: MORTALITY app (bilingual EN/ES); Packer Matrix; SecureReady premise IDs; five weight categories; PowerBI performance snapshot; "eliminates need for data bureau"
- PigCHAMP: Benchmark Magazine (since 2001); benchmark submission via backup file; 40+ standardized reproductive reports; Online vs Client Hosted editions
- AgroVision: ProductionMonitor/Feed Monitor/ConsultantMonitor naming; one-price package; Track & Trace module; Sanitel number support
- Agrisys: AutoPig®, AirSys, BatchSys, Brunst detector, PPT core product names; Nedap pigs-division succession (Nov 2023, AgriHub Canada / Agrisys Denmark)
- Evidence note: no precise numeric limits, time windows or KPI values are asserted anywhere in the final document; KPI names are documented as vocabulary only.

## Historical / Market-Sample Check

- Paper-era swine farm: individual sow record cards (sow number, services, farrowings, litters born/weaned), breeding/gestation calendar board, batch treatment sheets, feed delivery tickets, weaning and sale tallies, hand-computed annual summary per sow — satisfies all three L0 structures with no modern machinery. The dataset is the same; only capture and computation speed differ.
- 1980s–90s desktop sow-record programs (the lineage PigCHAMP claims, 30+ years) satisfy the core; MetaFarms' "eliminates need for data bureau" names the displaced baseline — paper barn records mailed to a data bureau for processing — which also satisfies the core with the bureau as human middleware.
- Older/regional: EU family-farm sow units, Danish batch-production practice, US farrow-to-finish and multi-site systems, national-ID regimes — all fit the core.
- Conclusion: the definition is not overfit to the current cloud/mobile/ESF implementation era. Historical check passed.

## Boundary Findings

1. **vs Livestock Management (seam = production-system shape, confirmed — and swine is the hybrid case).** The livestock pass defined generic Livestock Management around long-lived breeding herds as individuals or mobs, and predicted poultry/swine as batch. The swine sample confirms the seam is production-system shape, NOT species lists — but swine spans both shapes: the breeding herd is managed as individuals with cycle records (sow cards, individual ID, parity — livestock-style), while growing pigs are batches (poultry-style). Test holds: remove the swine cycle vocabulary (service/scan/farrow/litter/wean/parity) and the batch flow with closeout, and what remains is a generic livestock population+events+decisions core. Every sampled product's center of gravity is the swine cycle machinery + wean-to-market flow + PSY/batch economics — so Swine Management stands as its own specialty Type in the livestock family, exactly as Dairy does via the lactation cycle. Multi-species products (Farmbrite-style) straddle at packaging level.
2. **vs Poultry Farm Management (discharge of its forwarded flag — partially confirmed).** The poultry pass expected "the same batch-production seam". Confirmed for the growing half (weaners/finishers: batches, growth curves, closeout — structurally parallel to flock cycles). NOT confirmed for the breeding half: poultry farm records are population-level throughout (no individual bird identity in its sample), while every swine breeding-capable sample holds individually identified sows with cycle histories. The two Types meet at the weaned-batch interface; the sow side is where they diverge. Correction to the poultry document's wording ("Swine Management shares this Type's batch shape") applies to the growing phase only.
3. **vs Dairy Farm Management (both individual+cycle — the cycle content is the discriminator).** Dairy's cycle is the lactation/milking cycle with daily milk recording per lactation; swine's is the gestation/farrowing cycle with litter outcome recording and weaning at a fixed point. Swine has no milking machinery; dairy has no litter/parity batch-flow machinery. Both hold "individual animal + dated cycle events + records→decisions", so the cycle vocabulary is the boundary.
4. **vs Feed Management (interlocking disciplines).** The ration, feed supply and feeding loop are the subject there (feed-management pass explicitly covers swine operations on the feeding side); here feed consumption, deliveries and feed conversion are recorded as a layer of the production record. Ration formulation never appears as the center in any swine sample.
5. **vs Farm Management Platform (superset).** Whole-operation scope (land + crops + livestock + money + work) vs production-subject scope. Remove the whole-operation scope and the swine slice is this Type.
6. **vs Agribusiness ERP.** ERP centers the commercial/commodity flow (contracts, settlements, ledgers); swine management centers the animal/production record. MetaFarms SALES/closeout and Cloudfarms accounting/cost reports sit at this seam; they read as production-side money layers, not the ERP center.
7. **vs Agricultural IoT Platform.** IoT manages the connected device fleet (registry, connectivity, telemetry) as its packaged outcome; here controllers, ESF stations and readers are capture hardware bound to animals/batches. Agrisys (equipment-integrated control) is the closest pole — its Control System stores full history and compares across batches/herds, but its center is the barn installation it operates.
8. **vs Research Animal Facility Management.** Research-governance context (approved protocols, strains, per-diem billing) vs production-economics context. No overlap in the swine sample.
9. **Leaf-name observation.** The market's own umbrella term matches the leaf: PigCHAMP self-labels "Swine Management Software"; others say "pig production management" (Cloudfarms), "herd management for sow and grower farms" (AgroVision), "swine production platform" (MetaFarms). Center-of-gravity assignment consistent with the dairy pass's naming-drift note.

## Uncertainties

- PigCHAMP and MetaFarms content was retrieved through search-index copies of their official pages (direct fetch timed out / 403). Listed features are Layer A for those pages, but page-level completeness is uncertain (e.g., whether PigCHAMP ships grower-finisher modules beyond the benchmarking database).
- Agrisys documentation was reached at positioning + control-system level; its herd-record depth (individual sow records vs barn-level records) is inferred from the ESF/sow-monitor lineage and "compare across batches, barn sections, or entire herds" phrasing — kept at that strength.
- The exact KPI sets per product differ; the final document names KPI vocabulary (farrowing rate, repeat rate, PSY, FCR, ADG, mortality) without numeric values or product-specific formulas.
- Agritec Porcitec (a candidate genetic/data-depth pole) was unreachable (timeouts ×2) and was dropped rather than filled from memory.
- Whether a purely batch-focused finisher product with no sow machinery at all would be recognized by the market as "swine management" is well supported (Cloudfarms and MetaFarms sell wean-to-finish as standalone services; Agrisys serves finisher barns) — but the benchmarking/breeding-record products show the sow side is the historical heart of the category.

## Final Synthesis

A Swine Management application is the swine producer's production system of record and daily management console. Its defining core is three jointly-held structures: the swine production population held as persistent records at phase-matched granularity (individually identified breeding animals with multi-cycle histories; batch groups for growing pigs); the dated event stream in the swine production-cycle vocabulary bound to those units (service → scan → farrow/litter → foster → wean → re-serve/cull per sow and litter; placement → weight/feed/health/mortality → sale per batch, with inventory transactions and transfers); and the records → performance → decisions loop (cycle KPIs, batch performance, benchmarks against own history/other farms/industry, surfaced as action lists, alerts and dashboards). Everything else — ESF and RFID capture, mobile apps, cloud deployment, multi-site benchmarking programs, packer/packer-carcass integration, forecasting, traceability modules, welfare machinery — is common mature or variant structure, not definition. The Type is the hybrid member of the livestock family: individual-cycle breeding herd (livestock/dairy-shaped) plus batch growing flow (poultry-shaped), unified by the swine cycle vocabulary and the weaned-batch interface between the two halves.
