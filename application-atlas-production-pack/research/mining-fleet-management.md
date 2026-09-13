# Research Notes — Mining Fleet Management

Research date: 2026-09-09
Slug: mining-fleet-management
Directory leaf: Mining Fleet Management (§20 Agriculture, Food & Natural Resources)

## Research Goal

Understand, from real products, what "Mining Fleet Management" is as an Application Type: the industry's mine-site **FMS (Fleet Management System)** / dispatch / mine-control software. What objects exist inside it (machines, locations, material, operators, shifts), what the daily operational loop is (assignment → cycle → capture → adjust), which roles operate which surfaces, which states and rules matter, and where its boundaries sit against Mine Planning (upstream), road Fleet Management System (§18), Vehicle Telematics, Mining Operations Management (§20 sibling, unprocessed), Construction Equipment Management (§16), Autonomous Fleet Management (§18), and Robot Fleet Management (§16, unprocessed).

## Initial Boundary

- Core hypothesis: software that manages a mine's mobile equipment fleet (haul trucks, loading units, drills, support machines) in real time — tracking machines, assigning them to work (which dig, which destination), and recording production (loads, tonnes, cycles) against the shift plan.
- Industry vocabulary: "FMS", "fleet management system", "dispatch system", "mine control system". Micromine's own Pitram page title is literally "Mining Fleet Management | Mine Asset Management System".
- Likely confusions: Mine Planning Application (schedule vs live dispatch — seam already recorded by the mine-planning pass); road Fleet Management System (§18, open joint-review flag on this leaf); Vehicle Telematics Platform (feed vs management); Mining Operations Management (fleet vs whole mine); Construction Equipment Management (production cycles vs job allocation — seam already recorded by that pass); Autonomous Fleet Management (road AV fleets vs mine-site autonomous haulage); SCADA/HMI (fixed plant vs mobile fleet); Quarry Management (§20 sibling, unprocessed).
- Prior-pass context honored:
  - mine-planning-application (§20, processed 2026-09-09): "vs Mining Fleet Management (in-plan haulage routes/cycle-times vs live dispatch)"; also flagged Deswik.OPS as sitting ON the seam.
  - construction-equipment-management (§16, processed): "mining fleet systems center on production cycles (loading/hauling); construction equipment management centers on job allocation".
  - fleet-management-system (§18, processed): open flag — "the same register + activity + oversight pattern generalizes to non-road fleets, but those leaves carry domain-specific telemetry/operations the road-vehicle core model does not capture — flagged for joint review when those leaves are processed". The marine pass (marine-fleet-management, 2026-09-09) discharged its side with keep-both; this pass discharges the mining side.
  - autonomous-fleet-management (§18, processed): "autonomous haulage trucks in mines satisfy the same L0 pattern, but the leaf carries mine-site specifics (pit operations, haul profiles, dispatch systems). Related Type."
  - farm-equipment-telematics (§20, processed): noted "vs mining-fleet-management no-dispatch distinction".

## Research Questions

1. What machines/objects does the system manage? Is the fleet only haul trucks or all mobile equipment?
2. What is the unit of managed work — the truck cycle/load, the assignment, the shift?
3. How does dispatch work — automatic optimization vs manual assignment? What are the inputs (production targets, grade/blending, shovel queues, road conditions)?
4. How is production captured (loads, payload, cycles, material type) and attributed (machine, operator, shift, source, destination)?
5. What live state is maintained per machine (position, status, operator, payload)?
6. What roles exist (dispatcher/mine controller, supervisor, operator, engineer, administrator) and what surfaces (control-room console, in-cab terminal, mobile, reports)?
7. How does the shift plan connect to execution (SIC, plan compliance, deviation alerts)?
8. How deep is machine-health/maintenance integration?
9. How does autonomous haulage change the model?
10. Boundaries: vs mine planning, road FMS, telematics, SCADA, construction equipment management, mining operations management, robot fleet management.

## Representative Products

Selected for market representation, documentation reachability, different product philosophies, and different mining environments:

| Product | Vendor / family | Pole | Environment |
|---|---|---|---|
| DISPATCH | Modular Mining (a Komatsu company) | the category-defining dispatch-optimization FMS; open, mixed-fleet | open pit |
| Pitram | Micromine (a WEIR company) | OEM-agnostic "fleet management and mine control"; modular connectivity tiers | underground + surface |
| Deswik.OPS + ORB (+ AutoMine) | Sandvik (Deswik, Polymathian) | underground shift-execution + dispatch-decision optimization; automation line | underground |

Market anchors named but not directly documentable this pass (see Source-access Limitation): Wenco FMS (Hitachi Construction Machinery), Caterpillar MineStar, Hexagon HxGN MineOperate OP Pro.

Rejected/considered: Epiroc (telematics/automation line, no classic FMS found in reachable pages), RPMGlobal and Micromine planning lines (mine-planning territory), FLSmidth/ABB (fixed-plant/process digital lines).

## Sources

Tier 2 (official product pages) unless noted; all fetched 2026-09-09:

1. Komatsu — Modular ecosystem page: https://www.modularmining.com/ (served under komatsu.com/en-us/technology/smart-mining/modular)
2. Komatsu — Smart Mining overview: https://www.komatsu.com/en-us/technology/smart-mining
3. Komatsu — Loading and haulage: https://www.komatsu.com/en-us/technology/smart-mining/loading-and-haulage
4. Komatsu — DISPATCH product page: https://www.komatsu.com/en-us/technology/smart-mining/loading-and-haulage/dispatch
5. Komatsu — FrontRunner AHS: https://www.komatsu.com/en-us/technology/smart-mining/loading-and-haulage/autonomous-haulage-system
6. Micromine — Pitram product page ("Fleet management and mine control"): https://www.micromine.com/pitram/
7. Micromine — Pitram Material Management: https://www.micromine.com/pitram/material-management/
8. Micromine — blog "Could Short Interval Control Be the Key…": https://www.micromine.com/pitram-short-interval-control/
9. Micromine — blog "Seven common challenges in fleet management": https://www.micromine.com/seven-common-challenges-fleet-management/
10. Sandvik — Operational planning and shift execution (Deswik.OPS + ORB): https://www.rocktechnology.sandvik/en/digital-solutions/operations-and-connected-fleet/operational-planning-and-shift-execution/
11. Sandvik — rocktechnology.sandvik root (digital solutions nav: AutoMine, telemetry, mixed-fleet telemetry, Remote Monitoring Service)

Unreachable (abandoned per network rules; named as market anchors only, no operational claims drawn from them):
- Wenco (wenco.com) — bot-check IP echo ×2, 404 ×2
- Caterpillar (cat.com 403; minecat.com 403; mining.cat.com transport error)
- Hexagon Mining (hxgnmineoperate.hexagonmining.com transport error; hexagon.com 403) — consistent with the mine-planning pass's recorded 403 + transport error

## Product A — Modular Mining DISPATCH (Komatsu)

### Key observations (evidence layer A unless noted)

- Self-labeling: "DISPATCH is Modular's foundational fleet management system (FMS), giving you real-time visibility and control across your loading and hauling operations."
- Defining act: "By intelligently assigning trucks to the most efficient loading and dumping points, DISPATCH helps reduce idle time, increase equipment utilization and keep your operation on plan."
- Stated outcomes (vendor claims): optimize truck and shovel assignments; minimize queuing and idle time; maximize fleet effectiveness; improve execution of mine plans; real-time operational visibility. "Move 8%+ more material each year by optimizing equipment assignments."
- Feature table: **Total site optimization** ("keep trucks moving, reduce idle or hang and boost overall haulage productivity"); **Parkup module** ("maximize production and efficiency at the end of each shift"); **Haulage tracking functionality** ("turn accurate haul data into actionable insights for better mine planning"); **Fueling module** ("minimize queuing at fueling locations"); **Blending module** ("automate crusher and stockpile blending to drive consistency and reduce variation").
- Live model: "DISPATCH maintains a live digital twin of your mine, capturing equipment, locations and haulage roads in real time. By continuously optimizing routes and automating communication, the system keeps truck operators connected, informed and moving efficiently toward the mine plan."
- Ecosystem apps extending DISPATCH: **Roadways** (haul-road optimization; "automatically updating your road network with real-time data"; ETAs, cycle times, hazards, congestion); **Replenish** (fuel management; "ensure every truck is fueled or charged at the right time and place"; diesel and electric); **Adaptive Config / Adapt** ("AI-powered fleet optimization… continuously analyzes real-time conditions to automate truck assignments, balance load flow… Balance loads dynamically across shovels and dumps. Align assignments to your mine plan").
- Ecosystem roles: "built to meet the needs of dispatchers, operators, planners and leaders." Three platforms: **Mine platform** ("orchestrate assignments, maintenance and plan execution for mixed fleets from a single interface"); **Machine platform** ("one screen, one UI — operator-first workflows that perform online or offline in tough conditions"); **Mine analytics platform** ("enterprise-wide KPIs, benchmarks and anomaly alerts").
- Smart Mining solution map: Load and haul / Drilling and blasting / Autonomous haulage / Mine compliance / Maintenance and reliability ("insights into equipment health… maximize asset availability"; MineCare named in imagery) / Asset management.
- Companion technologies around the FMS: **ProVision Guided Spotting** (centimeter-level truck positioning at the shovel), **Argus payload management** (real-time payload for shovels, loaders, draglines; operator coaching).
- Autonomous haulage (FrontRunner AHS): "Your operation can benefit from DISPATCH-optimized truck assignments"; "Enterprise-level visibility and central command control"; "predictable, consistent performance from a smart system that delivers visibility and optimum compliance to mine plans." AHS is an execution mode inside the DISPATCH frame, not a separate management system.
- Mixed fleet: Mine platform "orchestrate assignments, maintenance and plan execution for **mixed fleets**"; ecosystem "integrates with mixed fleets via open APIs, minimizing vendor lock-in".

## Product B — Micromine Pitram

### Key observations (evidence layer A unless noted)

- Self-labeling: "Fleet management and mine control"; "a comprehensive mine control and fleet management solution (FMS) for capturing, managing, analysing, and optimising holistic mine site activity." Page title: "Mining Fleet Management | Mine Asset Management System". Suite position: the **Operate** stage of Micromine's mining life cycle (Explore → Evaluate & Design → Plan → **Operate** → Platform).
- Object world: "consolidates key operational data, such as **equipment, material, locations, and people**, to provide data-driven insights in real or near-real-time." "By capturing and connecting data across equipment, locations, material, and personnel… From tracking shift progress to analysing long-term trends."
- Connectivity tiers (deployment ladder, both current product tiers):
  - **Voice-Enabled Productivity**: "captures shift activity through your radio network, allowing mine controllers to log events and track operational data in real-time… Capture near real-time data without new infrastructure." Mine controllers log activities called in by field personnel; dashboards and reports; integrates third-party systems (autonomous fleets, weighbridges, conveyors) via the PRIS open API; OLAP analysis module.
  - **Network-Enabled Productivity**: "equips your mobile fleet with ruggedised touchscreen devices to digitise in-field data capture… Operators use ruggedised in-cab touchscreens to log production data, which is automatically transmitted when equipment enters Wi-Fi range"; adds Pitram Vision (AI), P2P relay, location tracking via tags, integrations. "Supporting everything from radio-based activity logging to fully connected, real-time mine control."
- Feature set: **Pitram Mobile** (onboard capture of operator and equipment activity); **P2P** (mobile vehicles relay fleet data beyond Wi-Fi range); **Pitram Connect** (mobile access to real-time shift plans, equipment and personnel data); **Pitram Vision** ("AI-powered onboard cameras that automate LHD cycle tracking"); **API Integration** (PRIS); **Material Management**; **Shift Planner** ("plan, assign, and update shift activities in real-time"); **Controlled Areas** ("digitally manage access, occupancy, and safety compliance in restricted zones with automated alerts and permit tracking"); **3D Mine** ("real-time 3D visualisation of site activity using GPS and tagging data integrated with CAD, GIS, and block model references"); **Pitram Positioning** ("accurately track equipment location in real-time without Wi-Fi or cabling").
- Material Management (dedicated page): "Classify material as **ore, waste, or development** at the point of loading"; "Track every movement across **locations, equipment, operators, and time**, creating a complete chain of custody spanning **heading, stockpile and processing plant**"; "Each load is recorded by **location, equipment, shift and destination**"; "Material status updates flow directly into **dispatch, production tracking and shift dashboards**"; "Align production data with geological expectations in real time" (reconciliation); "Maintain real-time visibility into stockpile inventories, material quality and rehandling"; "Designed for low-connectivity environments".
- Time Usage Model: "equipment-centric Time Usage Model captures all **operating, idle and downtime states**, converting shift activity into clear timelines, availability metrics and performance reports."
- Rules-based data capture: "Pitram applies intelligent rules to operational events so **equipment status, locations and material assignments update automatically** as work progresses… helping prevent material mismatches."
- Short Interval Control (blog, Tier 2 official): "a reliable Fleet Management System (FMS) and Mine Monitoring solution essential to bridge the data utilisation gap." SIC machinery: (1) **shift schedule management** — "creating or importing of a shift plan with granularity of each individual equipment and activity… available in the control room, to equipment operators on the onboard tablets, shift supervisors, or any other users in the mobile app… monitoring compliance with objectives"; (2) real-time monitoring (equipment status, personnel location, production metrics, safety parameters); (3) **deviation tracking** — automatic alerts to the Control Room: "Time of the first loader bucket…, Shift tasks progress (expected vs actual), **Incorrect source and/or destination of material movements**"; (4) safety (personnel entering restricted areas); (5) ERP integration.
- Roles observed: **mine controllers** (control room; log events, track equipment and personnel locations, monitor production metrics), **equipment operators** (onboard tablets/touchscreens), **shift supervisors** (SIC, dashboards), **Pitram Administrator** (dedicated system owner — "manages internal processes, procedures, and serves as the crucial point of contact… across site operational teams"), engineers and geologists (feedback, reconciliation).
- Operational discipline (blog "Seven common challenges"): FMS as the **single source of truth** vs "competing data sources, such as spreadsheets or separate data bases"; "Regular audits of equipment, personnel, and configured locations"; live dashboards show "real-time production activity, operator assignment, equipment, and location statuses… without the need to call or visit the mine control room"; site-specific configuration ("No two mining operations are identical"); integrations with weighbridges and on-board equipment systems (Loadscan payload partnership named).
- Scale/context (vendor claims): "60+ implementations across underground and surface operations spanning 9 commodities"; "leading operational excellence in 14 countries"; customer story: "increased our equipment fleet from 50 to 220 units, and implemented a multi-roster system"; "For almost 30 years" of product evolution; "one of the few remaining OEM-independent solutions".

## Product C — Sandvik (Deswik.OPS + ORB + AutoMine line)

### Key observations (evidence layer A unless noted)

- Sandvik's "Operational planning and shift execution" node (under Digital solutions → Operations and connected fleet) is delivered through acquired products:
  - **Deswik.OPS**: "a Gantt based scheduler specifically designed to handle the complexity and granularity of underground mining cycles… maintaining schedule integrity down to, and including, the **Shift Planning and Shift Execution** levels." "Multi-user, web-based platform allowing multiple departments to work in the one plan… create baselines of agreed plans and **capture actuals to track progress against plan in near real time**." "Extend operational plans into the **Control Room** and underground on **mobile tablet devices** to support **SIC** throughout the shift… Supervisors and Operators have clear visibility on task progress, location and equipment status." "Digital data capture… at the face in near-real-time."
  - **ORB** (Polymathian): "targets strategic objectives by **optimising equipment dispatch decisions** through consideration of dynamic constraints, cave compliance and real-time performance of assets in an underground caving operation"; "Highly automated Short Interval Control (SIC) tool for optimising equipment dispatch decisions… through utilisation of Industrial Mathematics."
- Adjacent Sandvik lines (same digital-solutions nav): **AutoMine** (Tele-Remote, Lite, Multi-Lite, Core, Drill Fleet, Machine Fleet, Control Room, Autonomous — automation/tele-remote execution), **Sandvik telemetry / Mixed fleet telemetry** (data feed), **Remote Monitoring Service** ("prevention and prediction of breakdowns"), **iLink data interface**.
- Interpretation: in the underground market the FMS function is decomposed — plan/shift-execution (Deswik.OPS), dispatch-decision optimization (ORB), telemetry (Sandvik/mixed-fleet), automation execution (AutoMine) — sold as separate products that together cover the same operational loop the open-pit FMS bundles. This confirms both the shared loop and the packaging variance.

## Cross-product Comparison

| Dimension | DISPATCH (Komatsu/Modular) | Pitram (Micromine) | Deswik.OPS + ORB (Sandvik) | Strength |
|---|---|---|---|---|
| Fleet as identified managed units | equipment in a "live digital twin… capturing equipment, locations and haulage roads" | "equipment, material, locations, and people" consolidated; equipment-centric Time Usage Model | equipment scheduled and tracked per task in OPS; assets' "real-time performance" in ORB | B (all three) |
| Assignment of machines to work | "intelligently assigning trucks to the most efficient loading and dumping points"; Adaptive Config automates assignments "across shovels and dumps" | dispatch + Shift Planner ("plan, assign, and update shift activities"); rules update "material assignments" automatically | ORB "optimising equipment dispatch decisions"; OPS shift plans assign equipment to tasks | B (all three) |
| Production record at machine/load grain | haulage tracking ("accurate haul data"); blending at "crusher and stockpile" | "each load is recorded by location, equipment, shift and destination"; ore/waste/development classification at point of loading; chain of custody heading→stockpile→plant | actuals captured against plan (task grain); ORB real-time performance | B (all three; load-grain deepest in Pitram evidence) |
| Live machine state (position/status) | digital twin, real-time; routes optimized continuously | positioning (GPS/tags, no-Wi-Fi option), equipment status, P2P relay | near-real-time actuals; task progress, location, equipment status | B (all three) |
| Operator identity / in-cab surface | Machine platform: "one screen, one UI — operator-first workflows… online or offline" | in-cab ruggedized touchscreens; operator logs production data; Pitram Connect mobile | tablets underground; operators see task progress | B (all three) |
| Control-room role | dispatchers (ecosystem "built… for dispatchers") | mine controllers log/track in control room; deviation alerts to Control Room | Control Room extends plans; SIC | B (all three) |
| Plan connection / compliance | "keep your operation on plan"; "improve execution of mine plans"; Adaptive Config "align assignments to your mine plan" | shift-plan compliance monitoring; SIC deviation alerts (expected vs actual) | OPS baselines + actuals vs plan; ORB cave compliance | B (all three) |
| Shift as operating rhythm | Parkup module "at the end of each shift" | shift planner, shift dashboards, multi-roster | shift planning/execution levels explicitly | B (all three) |
| Machine health / maintenance | ecosystem Mine platform "orchestrate assignments, **maintenance**…"; MineCare; asset management | Time Usage Model (operating/idle/downtime → availability); maintenance teams "aligned in real time" | Remote Monitoring Service (separate product) | B common, depth varies — NOT definitional |
| Optimization depth | total site optimization; AI Adaptive Config | rules-based automation; OLAP analysis; dispatch present, optimization depth not documented | ORB industrial-mathematics optimization | Variant (manual→rules→optimization→AI ladder) |
| Positioning technology | real-time digital twin (technology unspecified in fetched pages) | GPS, tags, no-Wi-Fi positioning, P2P | not documented this pass | B common — NOT definitional (radio tier proves) |
| Material/grade machinery | Blending module (crusher/stockpile) | Material Management (ore/waste/development; reconciliation vs geology) | not documented this pass | B common, depth varies |
| Autonomy | FrontRunner AHS inside DISPATCH frame ("DISPATCH-optimized truck assignments") | integrates autonomous fleets via API | AutoMine line (separate products) | Variant / execution mode |
| Environment | open pit (loading and haulage) | underground + surface ("60+ implementations across underground and surface") | underground (caving, development cycles) | Variant |
| Packaging | bundled FMS + ecosystem apps | modular FMS with connectivity tiers | decomposed: scheduler + optimizer + telemetry + automation | Variant |

## Canonical Model (abstraction ladder)

### L0 — Defining Invariant (deliberately small)

Three jointly-held structures. The Type is recognizable only when all three are present:

1. **The mine's mobile equipment fleet as individually identified managed units.** Haul trucks, loading units (shovels/excavators/loaders/LHDs), drills, and support machines held as persistent identified records the system watches and directs. Remove → vehicle telematics (feed without management) or mine planning (which manages mining units, not machines).
2. **The assignment loop maintained through the shift.** Machines are continuously directed to work — which loading unit/feed point a truck serves, which destination it hauls to, which task a drill or support machine works — and assignments are adjusted as the shift unfolds. The loop binds machines to the mine's own work locations and material destinations (dig/source → destination), not to customer jobs or public-road routes. Remove → a plan/schedule (mine-planning territory) or a tracking display with no direction.
3. **The production record at machine/load grain.** What the fleet actually moved is captured as attributed records — loads/cycles carrying machine, operator, source, destination, material, time — accumulating per shift into the operational production record (tonnes moved, cycles, equipment time). Remove → a dispatch board with no memory; production reporting, reconciliation, and pay/benchmark inputs collapse.

Jointly-held is load-bearing:
- 1 alone = telematics/asset tracking
- 2 without 1 = a schedule or whiteboard (planning territory)
- 3 without 1+2 = weighbridge/scale reports with no fleet behind them
- 1+2 without 3 = live dispatch with no production record (the "management" is blind to output)
- 1+3 without 2 = tracking + reports with no direction loop (monitoring, not management)

Mining anchoring is population+context: the machines are mine production machines and the work is extraction/haulage cycles at a private mine site. Swap the population to road vehicles → Fleet Management System (§18); to task-executing robots → Robot Fleet Management (§16); to fixed plant → SCADA/HMI territory.

### L1 — Common Mature Structure (standard in modern products, not definitional)

- live positioning of machines (GPS / high-precision / tag-based; underground no-infrastructure options)
- machine status model and equipment time usage (operating / idle / down; availability, utilization)
- operator identity: operators log onto machines; operator assignment tracked with production
- shift plan / shift targets and plan-compliance monitoring (SIC); deviation alerts (expected vs actual, wrong source/destination)
- in-cab operator terminal (assignments, guidance, messaging; offline-tolerant)
- control-room console for dispatchers/mine controllers (fleet map, statuses, queues)
- production reporting and KPIs (tonnes, loads, cycle times, availability/utilization, plan vs actual)
- machine-health monitoring and maintenance integration (companion modules; depth varies)
- haul-road / route data; payload monitoring; fuel management; blending/grade machinery
- reporting/analytics layer (dashboards, OLAP, enterprise KPIs)

### L2 — Variant / Optional Structure

- environment: open pit vs underground (positioning technology, connectivity, cycle shape, method-specific machinery such as caving compliance)
- OEM posture: OEM-integrated (vendor's own machines) vs OEM-agnostic/mixed-fleet (open APIs)
- optimization depth: manual dispatch → rules-based → mathematical optimization → AI-adaptive
- execution mode: manual-driven vs tele-remote vs autonomous haulage (mixed fleets common)
- connectivity tier: radio/voice logging → networked real-time (a deployment ladder inside single products)
- commodity/method tuning (coal, iron ore, caving, room-and-pillar), scale (single pit → multi-site), integration posture (ERP, weighbridge, conveyor, geological models/block models)

### L3 — Vendor-specific (kept out of the final document)

DISPATCH modules (Parkup, Roadways, Replenish, Adaptive Config), ProVision, Argus, MineCare, KMAP; Pitram modules (Vision, P2P, PRIS, Controlled Areas, 3D Mine, Connect, Positioning, OLAP); Deswik.OPS, ORB, AutoMine product names; FrontRunner AHS; MineStar module names; vendor outcome claims (8%+ material, $1M fuel, 28.6% queue reduction, 40% tire/brake life, 900+ trucks, 10+ billion tons — marketing figures, attributed only).

## Anti-overfitting Notes

- **GPS/positioning is NOT definitional.** Pitram ships a current Voice-Enabled tier operating over radio with controllers logging events called in by field personnel — the assignment+production core runs without network positioning. Positioning is the strongest common-mature capability, not the invariant.
- **Optimization/AI is NOT definitional.** The optimization ladder spans manual dispatch (radio era, still a product tier) to AI-adaptive assignment (Adaptive Config) to industrial-mathematics dispatch (ORB). The invariant is the assignment act, not its intelligence.
- **Real-time infrastructure is NOT definitional.** "Real or near-real-time" (Pitram's own phrasing); near-real-time actuals (Deswik.OPS). The invariant is that the loop runs at shift tempo, not that data is streaming.
- **Autonomy is NOT definitional.** Autonomous haulage is an execution mode inside the FMS frame (DISPATCH-optimized assignments drive AHS trucks; Pitram integrates autonomous fleets via API; AutoMine is a separate product line).
- **Maintenance/machine health is NOT definitional.** Present across the sample as companion modules (MineCare, Remote Monitoring Service, Time Usage Model) with varying depth; the FMS's center is assignment+production.
- **Load-grain material classification** is documented in depth at one product (Pitram Material Management) with blending machinery at another (DISPATCH Blending) — held as common-mature machinery, not invariant; the invariant is the attributed production record.

## Historical / Market-Sample Check (§24 workflow)

- Would older, regional, platform-native products still fit? The radio-dispatch mode — dispatcher directs trucks by radio and tallies loads — satisfies all three L0 legs with no GPS, no network, no optimization engine. It survives as a *current product tier* (Pitram Voice-Enabled: "capture near real-time data without new infrastructure"), which is direct evidence the core predates modern connectivity machinery.
- The founding-generation FMS (the category's dispatch systems) and today's AI-assisted ecosystems both fit the three-leg core; the definition names no protocol, no positioning technology, no optimization method, no deployment shape.
- Underground and open-pit realizations both fit; OEM-integrated and OEM-agnostic both fit; single-machine-class and mixed fleets both fit.
- Conclusion: L0 survives the historical check; GPS, optimization, autonomy, cloud, and AI are era machinery.

## Vendor-specific Findings (L3, not for the final document)

- DISPATCH: Parkup (end-of-shift production), Roadways (haul-road network updates), Replenish (fuel/charge scheduling), Adaptive Config (AI assignment tuning), Blending module; ProVision guided spotting; Argus payload coaching; MineCare health; Mine/Machine/Mine-analytics platform trio; Komatsu FrontRunner AHS integration and its marketing figures.
- Pitram: PRIS API; Pitram Vision (AI LHD cycle tracking from onboard cameras); P2P vehicle relay; Controlled Areas (restricted-zone access/permits); 3D Mine (CAD/GIS/block-model overlay); OLAP module; Loadscan payload partnership; twice-yearly release cadence; LMS training; "60+ implementations, 9 commodities, 14 countries" claims.
- Sandvik: Deswik.OPS (Gantt, baselines, multi-department), ORB (caving dispatch optimization, "Industrial Mathematics"), AutoMine tiers (Tele-Remote/Lite/Multi-Lite/Core/Control Room/Autonomous), iLink interface, Remote Monitoring Service.

## Boundary Findings

| Type | Relationship | Distinction / removal test |
|---|---|---|
| Mine Planning Application (§20, processed) | upstream, plan-of-record | Planning answers where/when to mine (design, reserves, schedule over periods); this Type answers which machine does what now and records what moved. The shift plan is the handoff artifact; DISPATCH haulage tracking "turns accurate haul data into actionable insights for better mine planning" (feedback direction). Deswik.OPS sits ON the seam (short-interval scheduling + shift execution) — consistent with the mine-planning pass's note. Remove the live assignment/production loop → planning; remove the deposit model/design/reserves → this Type. |
| Fleet Management System (§18, processed) | sibling sharing the register+oversight family pattern | Road FMS centers on drivers (behavior, HOS, licensing), compliance, and public-road routes over an organization's vehicles; this Type centers on production cycles (load→haul→dump), material identity, and plan execution at a private mine site. **Discharges the fleet-management-system pass's sibling flag from the mining side: keep-both RATIFIED** (same verdict as the marine pass). Remove production cycles/material → road FMS; remove driver/compliance machinery → this Type. |
| Vehicle Telematics Platform (§18) | data layer | Telematics is the feed (position/state/engine data); this Type is the management application over the feed — assignment decisions and production records. Remove the management loop → telematics. |
| Mining Operations Management (§20, unprocessed) | probable broader sibling | Hypothesis: whole-mine operations (production accounting, planning reconciliation, cost, compliance) vs this Type's fleet-level execution loop. **Forward flag for joint review when that leaf is processed.** |
| Robot Fleet Management (§16, unprocessed) | probable sibling | Hypothesis: task-execution-centric robot missions vs production-cycle-centric mine fleet. **Forward flag for joint review when that leaf is processed.** |
| Autonomous Fleet Management (§18, processed) | related; execution-mode overlap | Road AV fleets run autonomy-executed missions under a supervisory loop; in mines, autonomous haulage is an execution mode inside the mining FMS (DISPATCH-optimized assignments drive AHS trucks). Related Types; the road-AFM core does not capture mine-site production cycles. |
| Construction Equipment Management (§16, processed) | adjacent (other industry) | Ratified from this side: production-cycle-centric (loading/hauling with material and destinations) vs job-allocation-centric (machines to jobsites with cost/charge-out). Remove the production cycle → construction equipment management. |
| SCADA / HMI (§16) | different plant | SCADA/HMI supervises fixed process equipment via control loops; this Type directs mobile machines through an assignment loop and records production. Different object world; both may share a control room. |
| Dispatch Management (§18, processed) | shared mechanism, different center | Generic dispatch centers on a queue of incoming work (loads/jobs/orders) assigned to field resources; mine dispatch centers on the production cycle — the "work" is the mine's own material movement, not customer jobs. The assignment mechanism is shared; the object world and records differ. |
| Quarry Management (§20, unprocessed) | §20 sibling | Aggregates operations likely share the load/haul grammar at smaller scale. Flagged by the mine-planning pass; noted here, left to that pass. |

## Uncertainties

- **Wenco FMS, Cat MineStar, Hexagon OP Pro unreachable** (bot-check/403/transport errors, consistent with the mine-planning pass's Hexagon record). These are major market anchors; their module structures are NOT independently verified this pass. No operational claims are drawn from them; they are named as representative products only. Assertion strength for "all major FMS products do X" is calibrated to the three reachable products (B-layer).
- **DISPATCH's positioning technology** (GPS vs high-precision ranging) not documented in fetched pages — positioning held generic.
- **Pitram's dispatch optimization depth** (whether it ships mathematical optimization like ORB/Adaptive Config) not documented — optimization ladder endpoints evidenced at Komatsu and Sandvik only.
- **Underground open-pit FMS packaging at Cat/Hexagon** (module names, tier ladders) unverified.
- **Whether any FMS ships without a control-room surface** (e.g., purely in-cab + reports) — not observed; control room held common-mature rather than definitional for safety.
- **Pay/benchmark consumption of the production record** (how tonnes flow to contractor pay or corporate reporting) — only indirectly evidenced (MATSA multi-roster expansion; "month-end closings" quote in a Pitram SIC slide); held weak.

## Final Synthesis

Mining Fleet Management is the mine's real-time execution system for its mobile equipment fleet. Its defining core is three jointly-held structures: the fleet as individually identified managed units; the assignment loop that continuously directs machines to the mine's own work (loading unit → destination) through the shift; and the production record at machine/load grain (attributed loads/cycles with source, destination, material, operator, time) accumulating per shift. Around that core, mature products add live positioning, equipment time-usage states, operator logon, shift plans with compliance monitoring (SIC), in-cab terminals, control-room consoles, production KPIs, machine-health modules, payload/fuel/blending machinery, and analytics. The market realizes the Type across an optimization ladder (manual → rules → mathematical → AI), an OEM posture axis (integrated vs agnostic), an environment axis (open pit vs underground), and an execution-mode axis (manual vs tele-remote vs autonomous), with connectivity tiers inside single products proving the core predates modern network machinery. The Type ends where planning begins (deposit model, design, reserves, period schedules — Mine Planning) and where the road-fleet frame begins (drivers, compliance, public routes — Fleet Management System).
