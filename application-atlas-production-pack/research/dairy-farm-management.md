# Research Notes — Dairy Farm Management

Research date: 2026-09-07
Slug: dairy-farm-management (DIRECTORY §20 Agriculture, Food & Natural Resources — "Dairy Farm Management")

## Research Goal

Understand what a Dairy Farm Management application actually is as an Application Type: its core objects, the daily operational loop, how data enters the system, which rules and states matter, and where its boundary lies against neighboring Types (Livestock Management, Farm Management Platform, Feed Management, Poultry/Swine Management, Agricultural IoT Platform, milk-recording/processor systems, veterinary tools).

## Initial Boundary (working hypothesis before research)

- Core use: manage a dairy herd — individual animal records, milk production through repeated lactation cycles, reproduction, health/treatment, feeding, and the daily work those generate.
- Users: farm owner/manager, herd manager/herdsman, milking staff, vets, nutritionists, consultants, milk-recording field officers.
- Nearest neighbors: Livestock Management (beef/sheep), Farm Management Platform (crop-centric), Feed Management, Poultry/Swine Management, Agricultural IoT Platform.
- Likely confusion: "farm management" (crop) vs "herd management" (dairy); sensor platforms vs the herd system of record.
- Unknowns: depth of milking-event capture across products; regional traceability regimes; whether feeding is in-scope; robot-vs-parlor split; withdrawal-period mechanics.

## Research Questions

1. What is the core object model? (animal, lactation, milking/test-day event, breeding events, health/treatment events, groups, rations)
2. What is the daily operational loop? (how records become work: attention lists, action lists, protocols)
3. How does data enter? (manual entry, milk meters/parlors, robots, sensors, milk recording agencies, national databases, third-party herd software)
4. Which rules/states matter? (lactation lifecycle, breeding windows, treatment/medicine registration, group movements, exit/culling)
5. What interfaces exist? (dashboard, cow card, action lists, reports, parlor/robot surfaces, mobile)
6. Where is the boundary vs Livestock Management / Farm Management / Feed Management / IoT platforms?

## Representative Products (selection rationale)

Chosen for market representativeness + documentation quality + different product philosophies + different customer tiers/geographies:

1. **VAS — DairyComp / VAS PULSE Platform** (US; 40-year herd-management lineage; record-analysis philosophy; command-line analytics; consultant tier; editions from small to large; ~18M animals claimed managed)
2. **Afimilk — AfiFarm** (Israel/global; parlor-and-sensor-integrated philosophy; ABC Dashboard; codes; automated sorting; scales to very large farms; official User Academy documentation portal)
3. **Uniform-Agri — UNIFORM** (Netherlands/EU mid-market; admin-first philosophy; editions by herd size; multiherd consultant version; strong integration list; official product pages + Academy)
4. **Lely — T4C / Horizon** (Netherlands; robot-ecosystem-first philosophy; farm management software aggregating robot milking/feeding data) — partial evidence, see Source-access Limitations.

Also referenced for cross-checks (not sampled with claims): DeLaval DelPro (unreachable), BouMatic SmartDairy, GEA, Nedap, SenseHub, CowManager, smaXtec (as integration partners named by sampled vendors).

## Sources

Fetched 2026-09-07 (WebFetch):

- VAS root site — https://www.vas.com/ (Tier 2; product map, integrations, positioning)
- VAS DairyComp product page — https://vas.com/dairycomp/ (Tier 2; capabilities, editions, mobile, ParlorBoss)
- VAS DairyComp Help Center — https://dc-help.vas.com/ (Tier 1 attempt; returned empty twice — abandoned)
- Afimilk root site — https://www.afimilk.com/ (Tier 2; solution map)
- Afimilk AfiFarm product page — https://www.afimilk.com/solution/afifarm/ (Tier 2 incl. FAQ; ABC Dashboard, codes, thresholds, sorting, third-party integration)
- Afimilk User Academy portal — https://docs.afimilk.com/user-academy/en-us/documents/academy/portal.htm (Tier 1; section map + "What's New" article titles)
- Afimilk Academy Fertility portal — https://docs.afimilk.com/user-academy/en-us/documents/academy/fertility_portal.htm (Tier 1; titles only — JS-rendered body not retrievable)
- Afimilk Academy Animal Data & Events Management portal — https://docs.afimilk.com/user-academy/en-us/documents/academy/data%20management%20-%20animals.htm (Tier 1; titles only — JS-rendered body not retrievable)
- Uniform-Agri root site — https://www.uniform-agri.com/ (Tier 2; solutions map, app, integrations summary)
- Uniform-Agri dairy product page — https://www.uniform-agri.com/solutions/for-dairy-cow-farmers/ (Tier 2; editions, module list, dashboard description)
- Uniform-Agri integrations page — https://www.uniform-agri.com/what-does-the-uniform-management-program-interface-with/ (Tier 2; full integration taxonomy)
- Lely international site — https://www.lely.com/en/farming/management-systems/ (Tier 2; Horizon/Hub farm management software, robot ecosystem, SCC/dry-cow-therapy articles)
- Lely T4C site — https://www.lelyt4c.com/en/ (timed out twice — abandoned)
- DeLaval DelPro applications page — https://www.delaval.com/en-us/explore-our-farm-solutions/delaval-delpro/applications/ (JS-only app shell — abandoned)

### Source-access Limitations

- VAS Help Center (dc-help.vas.com) returned empty content twice → VAS evidence is product-page level (Tier 2). No Tier-1 operational detail for DairyComp.
- Lely T4C site timed out twice → abandoned. Lely evidence is from lely.com (Horizon/Hub positioning + farming-insights articles). T4C is known to exist via VAS's integration list (A-layer from VAS's side).
- DeLaval site is a JavaScript app; content not retrievable → DeLaval not sampled with claims.
- Afimilk Academy article bodies are JS-rendered; only the portal structure and article titles were retrievable. Titles are still informative (event taxonomy, tag management, sort lists, third-party imports).
- No fetched source documents precise withdrawal-period mechanics, milk-payment/quota mechanics, or 305-day lactation standardization. These are therefore written at reduced strength or omitted.

## Product A — VAS (DairyComp / VAS PULSE Platform)

### Key observations (evidence layer A unless noted)

- Self-label: "Dairy Herd Management Software"; DairyComp described as "the world's most powerful Dairy herd management tool"; "Gold standard in Herd management software for 40 Years"; "nearly 18 million animals are managed with DairyComp"; producers in 52 countries.
- Positioning: "connect farmers to their data through herd and feed management software solutions... make the best management decisions with reliable, accurate data."
- Capability claims (product page):
  - "Empowers data-driven decisions"; "Unmatched fertility analysis"; "Fast and simple data entry with the mobile app"; "Customizable reports".
  - "Make bulletproof health and repro protocols so every cow gets what she needs" — protocols as a first-class concept.
  - "Save time with rapid batch entry and mobile worklists" — worklists as the mobile operational surface.
  - "Reveal problems and discover hidden value by using the powerful Command Line to explore your data" — command-line data exploration is a signature (vendor-specific).
  - "VAS Pulse Platform – your dairy's dashboard for performance metrics and industry leading integrations."
  - Mobile: "Bring animal information, data entry and worklists to the barn"; "Enter events and worklists online, or offline on a phone"; "Eliminate data entry errors by pairing the app with a RFID scanner"; "Pull up any cow's health history standing next to her."
- Editions: DairyComp Unlimited (flagship), MyDC on PULSE ("designed specifically for small- to medium-sized producers"), DairyComp Consultant ("premier analysis tool for high-performance consultants... Deep dive into dairy data to make the best recommendations on farms"), GrowerComp ("heifer growers and beef producers").
- Companion product: ParlorBoss — "Quickly and easily identify tasks that need to be performed while cows are milking – reducing lockup times and improving labor efficiency" (parlor-side task surface).
- Feed side: FeedComp ("inventory, shrink and loss"; "optimize pen feeding with always accurate counts from DairyComp") — feed is a separate product integrated with the herd system; herd counts feed the feed program.
- Integrations: "Integrated with over 50 world-renowned industry partners" — AfiFarm, DeLaval DelPro, Lely T4C, BouMatic SmartDairy, Smaxtec, Allflex (Silent Herdsman); genetics partners (URUS, Alta, Genex, PEAK...); ear tags & accessories hardware line.
- Scale claim: "from large multi-site operations to small."

## Product B — Afimilk (AfiFarm)

### Key observations

- Self-label: "AfiFarm herd management software is the heart of the Afimilk solution, using data collected from sensors – on the cows or in the parlor – to create a comprehensive farm profile with easy-to-analyze insights."
- ABC Dashboard: "every morning starts with a visit to the ABC Dashboard. On one screen, users see their current status of inventory and production, and attention and action lists with role-based tasks to perform and problems to solve that day." (daily operational loop, role-based)
- Reports: standard + custom; "insights... on health, reproduction, feeding, employee management and more"; "visualizations of heat, rumination, eating, heat stress and other group trends."
- FAQ (high-value operational evidence):
  - **Codes**: "A code is a customizable identifier assigned to an animal to categorize her status, condition or management group, such as: Fresh cow, High SCC, Treatment group, Do not breed, Watch list. Codes allow farms to filter, sort, report, and automate decisions quickly – including sorting and task generation."
  - **Third-party herd management integration**: "AfiFarm integrates with several third-party herd management systems, including Dairy Comp 305. Data such as reproduction events, health treatments and inventory information can be exchanged."
  - **Thresholds/KPIs**: "Producers can define: heat detection thresholds, rumination alerts, milk yield deviations, conductivity alerts, health event triggers."
  - **Sensors optional**: "Animals without activity devices remain fully visible in AfiFarm for: Milk production tracking, Health records, Reproduction records, Group management. However, behavioral analytics (activity/rumination) require a monitoring device." → the animal record is the core; sensors are enrichment.
  - **Per-milking data**: "Individual cow data is displayed: per milking session, in structured data tables, through interactive graphs, with trend analysis over time. Data aligns directly with your parlor sessions."
  - **Scale**: "from a few hundred cows to herds exceeding 120,000 animals."
  - **Automated sorting**: "When a cow meets defined criteria (health alert, heat detection treatment list), AfiFarm communicates directly with AfiSort gates to automatically draft animals."
- Hardware/software ecosystem: MPC & milk meter (ICAR-approved; "milk flow, milk yield, conductivity and parlor performance from every cow at every milking"; conductivity → mastitis detection), AfiLab (inline fat/protein/lactose per cow per milking), AfiCollar (rumination, eating, heat, feed efficiency), AfiAct III pedometer (heat, calving, rest, welfare), AfiSort/AfiWeigh, AfiFeed (individualized feeding), Afi2Go Prime mobile app, AfiFarm Spark ("See what matters. Prioritize your day.").
- Academy portal structure (Tier 1 titles): Active Tags Management ("Receive, assign, and manage active Afimilk ID tags"); Afi2Go Prime & Wand ("paperless... online farming"); Feed Efficiency ("Manage breeding and culling decisions based on Feed Efficiency and Profitability data"); Fertility; Health and Welfare ("each cow's health and group welfare... quick, apt responses"); **Animal Data Management ("Monitor and manage all animals and events")**; Farm Data Management ("Monitor and manage farm operations"); Parlor and Production Quality ("Milking sessions management; Working with AfiLabs; Rotary Control Terminal"); Milking Efficiency; MPC Milk Meter and Control Box; Feeding and Nutrition ("Manage group and individual feed allocations for all lactation cycles"); Maintenance, Calibration, Faults.
- Academy "What's New" article titles (event-model evidence): "Enter a Bulk Natural Mating Event (Heifers)"; "Correct a Heifer's Date of Birth following DNA Test"; "Confirm Herd ID Removed After Exit Event"; "Identify Failed Events from a Third Party Import"; "Identify and Process Faulty Tags"; "Enter Group Drying Event (and Remove Tags)"; "Record Heat Events from the Animals for Insemination Report"; "Creating a Sort List from an Imported Group"; "Sort Cows using Afi2Go Prime"; "Turn Off Sort Codes"; "Assign Tags in Offline Mode".
  → Confirms: event-based data model (mating, drying, exit, heat), heifer-vs-cow distinction, group events, tag lifecycle, third-party import reconciliation, sort lists.

## Product C — Uniform-Agri (UNIFORM)

### Key observations

- Self-label: "Herd Management Software"; "The core product of UNIFORM-Agri is the herd management software for dairy cow farmers. We provide the complete herd management package for the dairy farmer."
- Daily loop: "With quick one screen data entry UNIFORM controls the day to day administration and management reporting requirements for the herd. The dashboard highlights the events that are due to happen, cows that require attention and key performance indicators give a clear overview of the herd's targets and its performance."
- Editions/modules (product page):
  - UNIFORM Global Base (<100 cows): **Cow Calendar (incl. medicine registration)**, **Treatment Protocols (Action scheduler)**, **Herd Status Overview (fertility)**, Health registration, Herd reports, International Farm Comparison, DataSafe (online backup), UNIFORM App; optional country-specific links.
  - UNIFORM Global Professional: adds Milkproduction analysis, Fertility analysis, Health analysis, Individual feeding calculation, **Vet check list**; "flexible actionlists and vet check reports to schedule daily and weekly events and highlight cows that require special attention"; "Intelligent reporting tools analyse production, fertility and herd health to highlight problems and then monitor any changes in herd management or feeding"; Big Farm Modules (group level reporting, "US Fertility Key Performance Indicators"; up to 15,000 cows); optional: UNIFORM-Touch for parlour, Link with TMR Tracker, Network installation, Multiherd, Animal exchange module, Economy.
- UNIFORM App: "Installable on multiple smartphones and tablets; Instantly, wherever you are, view and add animal information; No permanent internet connection required; **Attention list always at hand**; Dashboard with key figures."
- Consultant tier: "multiherd version... designed as a solution for consultants in Dairy Industry"; vet cheat-sheet and analysis tool for veterinarians.
- Other species: separate beef version ("suckling herd") and goat version ("based on the same principles as their dairy cow program but adapted specifically for goats") — same vendor ships dairy as the core product and beef/goat as tailored siblings → supports dairy as its own Type.
- Other customer segments: AI (artificial-insemination) companies, breed advisors, **milk recording organizations** (they are a customer segment AND an integration source).
- Integrations page (full taxonomy):
  - Milking Robots & Parlors: Lely, GEA, DeLaval, BouMatic, Fullwood JOZ, SAC, Dairymaster, Waikato, PANAzoo
  - Activity & Health Monitoring: CowManager, SenseHub, Nedap, smaXtec, Afimilk, CowScout, CowWatch, BouMatic RealTime, DataFlow II
  - Identification & Weighing: Iconix, Tru-Test, Gallagher, Datamars Livestock, Allflex
  - Milk Recording Agencies: "Officially compatible with all major dairy records processing centers"
  - "Connections with national databases for efficient administration"
  - Stickreaders: "scan animals and automatically transfer the data to the UNIFORM App"
- Partnerships: Nedap Now (health/fertility insights in one overview), Zoetis CLARIFIDE Plus (genetic results inside the herd software).
- Scale: "over 18,000 users worldwide"; 40 years.

## Product D — Lely (T4C / Horizon) — partial evidence

### Key observations

- lely.com positions "Farm Management Software" (products: **Horizon**, **Hub**) as the layer that aggregates data from its automation ecosystem: milking robots (Astronaut, Dairy XL, Meteor), automatic feeding (Vector, Juno, Calm calf feeder), barn products (Tags, Grazeway...).
- "The data and insights generated by these solutions are brought together in Lely Horizon. This creates one connected narrative, one clear overview and one partner to build on." Also: "from calf to cow" — whole-lifespan framing (calf feeding → adult production).
- Farming-insights articles (management-software context): SCC as the key udder-health indicator ("Changes in SCC often signal udder inflammation, even before visible symptoms appear"); MQC-C automatic cell-count measurement; **selective dry cow therapy** ("treatment decisions are based on individual cow health. Accurate and timely insight into somatic cell count (SCC) is essential"); "Which cows need attention today?"; feed intake as foundation of health/fertility/production.
- T4C: not directly reachable (timeouts). VAS's integration list names "Lely T4C" (lelyt4c.com) as a partner system — A-layer evidence from VAS that T4C exists as a Lely farm-management system in the integration ecosystem.
- Interpretation (Layer C): the robot-first philosophy treats the herd system as the coordinator of machine-generated data (milking, feeding, manure, barn) with the same animal/event backbone.

## Cross-product Comparison

| Dimension | VAS DairyComp/PULSE | Afimilk AfiFarm | Uniform-Agri UNIFORM | Lely Horizon/T4C |
|---|---|---|---|---|
| Category self-label | "Dairy herd management software" | "herd management software... heart of the Afimilk solution" | "herd management software for dairy cow farmers" | "Farm Management Software" |
| Defining center | animal records + events; deep analysis (command line) | animal records + events + sensor/milking data | animal records + events; one-screen entry | animals + machine/robot data aggregated |
| Daily surface | mobile worklists; batch entry; PULSE dashboard | ABC Dashboard: status + attention & action lists, role-based tasks | Dashboard: events due + cows requiring attention + KPIs; actionlists; vet check | Horizon "one clear overview" |
| Reproduction | "unmatched fertility analysis"; repro protocols | Fertility portal; heat/insemination/mating events | Fertility analysis; Herd Status Overview (fertility) | heat detection via robot/sensor data |
| Health | health protocols; cow-side history | Health & welfare portal; health event triggers | Health registration; medicine registration; vet check list | udder health, SCC, selective dry cow therapy |
| Milk production | performance metrics on PULSE | per-milking yields + components + conductivity | Milkproduction analysis | robot milking data; MQC-C SCC |
| Feeding | separate product (FeedComp), herd counts feed it | AfiFeed; group & individual allocations | Individual feeding calculation; TMR Tracker link | Vector feeding data in Horizon |
| Animal ID | ear tags/RFID hardware; RFID scanner pairing | active tag management; faulty-tag process | stickreaders; ID systems; national databases | Tags product |
| Sorting automation | — | sort codes/lists → AfiSort gates | — | — |
| Consultant tier | DairyComp Consultant | — | UNIFORM Consultant (multiherd); vet tools | Farm Management Support service |
| Editions by scale | Unlimited / MyDC (small-mid) / GrowerComp | few hundred → 120,000+ cows | Base <100 / Professional <250→15,000 | — |
| Integration spine | 50+ partners (parlors, sensors, genetics) | Afimilk ecosystem + third-party herd software (DairyComp 305) | robots/parlors + monitors + ID + milk recording agencies + national databases | Lely ecosystem (milking/feeding robots) |
| Mobile | mobile app offline + RFID | Afi2Go Prime (offline tag assignment) | UNIFORM App (offline; attention list) | My Lely / Horizon clients |

### Cross-product commonalities (Layer B)

1. Every product centers on **individually identified animals** (tags/RFID/national IDs) — never batch/flock accounting.
2. Every product records **events against animals** (heat/insemination/mating, calving, drying, health/treatment, exit) — the event timeline is the animal's history.
3. Every product turns records into a **daily work surface**: attention/action lists, worklists, vet check lists, protocols, dashboards with "cows that require attention."
4. Every product has **production analysis** (milk yields; components/quality where hardware allows) and **fertility analysis** as the two headline analytics.
5. Every product has an **integration spine**: milk meters/parlors, milking robots, activity/rumination monitors, ID systems, milk recording agencies, national databases, third-party herd software.
6. Every product has a **mobile/offline barn-side client** with scanning (RFID/stickreader).
7. Group/pen management appears in all sampled products (group events, group-level reporting, management groups).
8. Feeding appears in all, but at different depths (calculation → allocations → separate product) — never as the defining center.
9. Consultant/vet access is a distinct tier or mode in 3 of 4 (VAS, Uniform, Lely service; Afimilk via role-based tasks).

### Product-specific (Layer A, kept out of canonical core)

- DairyComp command-line data exploration; ParlorBoss; GrowerComp; Pocket CowCard.
- AfiFarm "codes" vocabulary; ABC Dashboard; Afi2Go Wand; AfiSort gates; AfiLab inline components; Spark.
- UNIFORM "Cow Calendar", "DataSafe", "UNIFORM-Touch for parlour", "US Fertility KPIs", "International Farm Comparison".
- Lely Horizon/Hub naming; MQC-C; Lely Center service model.

## Canonical Model (Layer C)

### L0 — Defining Invariant (deliberately minimal)

A Dairy Farm Management application is recognizable by four properties together:

1. **Individually identified animal records** — the herd is a population of persistent, individually identified animals (ear tag / national ID / farm number), each carrying pedigree/birth/lactation-number context. Remove → batch or herd-level accounting (poultry/swine style), or a milk-plant record; not dairy herd management.
2. **Milk-production recording organized around the lactation cycle** — production is attributed to the individual animal and to her successive lactations (calving → lactation → dry-off → calving). Remove → generic livestock management (beef/sheep growth cycles).
3. **Reproductive and health event history per animal** — breeding/heat/insemination, calving, treatments/health events recorded as dated events on the animal record; these events drive the cycle. Remove → a production log without management content.
4. **Records drive daily herd work** — the record set is continuously turned into operational decisions and tasks: which animals to breed, pregnancy-check, treat, dry off, move, or cull (attention/action lists, protocols, reports). Remove → a registry/herd book (archive), not a management application.

Historical check: paper herd books + milk-recording-association test days (individual cow identity, lactation yield totals, breeding and treatment notes, decisions on paper) satisfy all four without sensors, robots, parlors, cloud, or apps. Pasture-based and smallholder dairies with periodic milk recording satisfy them. National dairy-recording schemes satisfy the record side; the farm-side management loop is what the software adds. → L0 is not over-fitted to the current sensor-rich market.

### L1 — Common Mature Structure

- Dashboard / daily work surface (events due, attention & action lists, role-based tasks)
- Cow card / animal detail (event timeline, lactation history, production trend)
- Reports & analysis: production, fertility, health; standard + custom; KPIs/benchmarks
- Treatment protocols / action scheduler; medicine registration; vet check lists
- Groups/pens (lactating, dry, fresh, hospital/sick; group events; group-level reporting)
- Mobile barn-side client (offline entry, RFID/stickreader scanning)
- Integration spine: milk meters/parlors, milking robots, activity/rumination monitors, ID systems, milk recording agencies, national databases, third-party herd software, genetics
- ID/tag management (tag assignment, faulty-tag handling, offline assignment)
- Feeding layer (group/individual allocations; deeper feed management via linked or separate products)
- Sorting automation (criteria → sort lists → sort gates) in sensor-integrated products
- Multi-farm / consultant (multiherd) access

### L2 — Variant / Optional Structure

- Philosophy poles: record-analysis-first vs sensor/parlor-integrated vs robot-ecosystem-first vs admin-first mid-market
- Scale packaging: editions by herd size (small-farm base → mega-farm modules)
- Milking context: parlor vs robotic vs historical pipeline/bucket
- Regional: national ID/traceability database links, milk-recording agency formats, country-specific links, languages
- Feeding depth: none → calculation → full feed management (separate product)
- Deployment: on-farm install/network vs cloud platform
- Genetics integration (genomic results, semen/AI companies)
- Species siblings shipped by the same vendors (beef, goats) — tailored variants of the same backbone

### L3 — Vendor-specific (research notes only)

DairyComp command line; ParlorBoss; AfiFarm codes/ABC Dashboard/Afi2Go Wand/AfiSort/AfiLab/Spark; UNIFORM Cow Calendar/DataSafe/Touch/US Fertility KPIs; Lely Horizon/Hub/MQC-C; brand-specific sensor lineups (AfiCollar, AfiAct, Nedap, SenseHub, CowManager, smaXtec...).

## Vendor-specific Findings

See L3 above. Notable: VAS and Afimilk integrate with *each other* (VAS lists AfiFarm; AfiFarm FAQ names Dairy Comp 305) — evidence that the herd-management system of record and the sensor/parlor data layer are separable roles, often filled by different products on the same farm.

## Boundary Findings

- **vs Livestock Management**: dairy's defining rhythm is the individual lactation/milking cycle. Uniform ships a separate beef product ("suckling herd") and a goat product "based on the same principles... adapted specifically for goats" — same vendor, different products → the dairy Type is distinct. Remove the lactation/milking production cycle → Livestock Management.
- **vs Farm Management Platform (crop)**: field/crop operations vs animal herd; different core objects (fields/crops vs animals/events). Some whole-farm platforms include livestock modules, but the dairy herd system is animal-centric and stands alone.
- **vs Feed Management**: ration formulation/feed inventory (TMR Tracker, FeedComp) is a distinct discipline; the herd system links to it (Uniform optional link; VAS separate product; Afimilk AfiFeed). Feeding is a layer, not the core.
- **vs Poultry/Swine Management**: those are batch/population-based (flocks, all-in/all-out); dairy is individual-animal, cycle-based. (Consistent with the aquaculture research note that aquaculture manages groups per unit unlike dairy/beef individual identity.)
- **vs Agricultural IoT Platform**: sensor platforms deliver telemetry; the herd system is the animal/event system of record. AfiFarm FAQ is direct evidence: animals without devices remain fully visible for production/health/reproduction/group management; behavioral analytics require a device.
- **vs milk recording / processor side**: milk recording agencies are data suppliers and even customers of the software vendor (Uniform segment), not the farm's management system; milk collection/payment is processor-side (adjacent, outside this Type).
- **vs veterinary practice management**: vets are users (vet check lists, consultant tools) but the system of record belongs to the farm.
- **"去掉什么就变成另一个 Type" 判据**: remove individual animal identity → batch livestock accounting; remove the lactation/milking cycle → generic Livestock Management; remove the daily-work loop → herd book/registry; remove animals (keep fields) → Farm Management Platform.

## Uncertainties

- **Withdrawal/withholding mechanics**: medicine registration is documented (Uniform "Cow Calendar incl. medicine registration"; AfiFarm "Treatment group" code; Lely selective dry cow therapy), but precise milk-withholding/diversion workflow mechanics were not directly documented in fetched sources. Written at moderate strength in the final doc.
- **Milk recording/test-day mechanics** (periodic official recording, lactation standardization): milk recording agencies are documented as integration partners/segments; the internal test-day mechanics are not documented in fetched sources. Written generically ("periodic milk-recording data flows in").
- **Lely T4C operational detail**: unreachable; Lely claims kept at site level.
- **DeLaval DelPro**: unreachable; excluded from claims.
- **Quota/milk-payment mechanics**: no evidence; omitted entirely.
- **Exact KPI definitions** (e.g., pregnancy rate formulas): vendor-specific; not canonicalized.

## Final Synthesis

A Dairy Farm Management application is the dairy farm's animal-centered system of record and daily operations console. Its world is made of individually identified animals; each animal carries a dated event history (reproduction, health/treatment, movements, exit) and successive lactations with recorded milk production; the record set is continuously converted into daily work (attention/action lists, protocols, vet checks) and analyzed through production/fertility/health reports and KPIs. Data flows in from manual entry (often one-screen, mobile, offline, scan-assisted) and from an integration spine of milk meters/parlors, milking robots, sensors, milk recording agencies, and national databases. Products differ mainly in philosophy (analysis-first vs sensor-integrated vs robot-first vs admin-first) and scale packaging, not in the backbone. The Type is distinct from Livestock Management (lactation cycle), Feed Management (ration discipline), crop-centric Farm Management Platforms, and batch-based Poultry/Swine types.
