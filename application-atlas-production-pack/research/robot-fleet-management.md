# Research Notes — Robot Fleet Management

## Research Goal

Understand what "Robot Fleet Management" software actually is in the market: what objects exist inside it (robots, missions/tasks, maps/sites, chargers, zones), how work is directed to robots and executed, what the operational loop looks like, which capabilities are common but not defining, and where the Type's boundary sits — especially against the sibling leaves Robotics Engineering Platform (§16, unprocessed), Machine Vision Platform (§16, processed), the fleet-management family (Fleet Management System §18, Autonomous Fleet Management §18, Mining Fleet Management §20, Marine Fleet Management §18 — all processed with open flags toward this leaf), Warehouse Management System (§10, processed), SCADA/HMI (§16), and Agent Orchestration Platform (§13, processed).

## Initial Boundary

Initial hypothesis: software to operate and oversee a deployed fleet of robots — typically autonomous mobile robots (AMRs/AGVs) in warehouses and factories, also inspection robots and drones — by registering robots onto the system, directing work to them as missions/tasks, monitoring live execution, intervening on exceptions, and managing fleet health (battery/charging, software, maps/traffic).

Open flags carried into this pass:

1. **fleet-management-system (§18, processed)**: "robot/mining/marine siblings — the same register + activity + oversight pattern generalizes to non-road fleets, but those leaves carry domain-specific telemetry/operations the road-vehicle core model does not capture — related Types sharing an oversight pattern; flagged for joint review when those leaves are processed."
2. **mining-fleet-management (§20, processed)**: "Robot Fleet Management (§16, unprocessed) — probable sibling. Hypothesis: task-execution-centric robot missions vs production-cycle-centric mine fleet. Forward flag for joint review when that leaf is processed."
3. **autonomous-fleet-management (§18, processed)**: "vs Robot Fleet Management (§16 sibling): same family pattern (register + executed tasks + oversight) for non-road robots (AMRs, arms, drones). AFM carries road-traffic specifics... Different Types; joint awareness when that leaf is processed."
4. **marine-fleet-management (§18, processed)**: "mining is production-cycle-centric, robots are task-execution-centric; marine is asset-administration-centric" — noted, no flag requiring action from this side.

## Research Questions

1. What are the core objects? (robots, missions/jobs/tasks, maps/facility models, endpoints/docks/chargers, zones, users)
2. How does a robot join the fleet (commissioning) and leave it?
3. What is the core operational loop: how does work get defined, queued, assigned, executed, monitored, closed?
4. What does "management" include beyond dispatch: health, battery/charging, software updates, maps/traffic, access control?
5. What states do robots and tasks have, and which states are user-visible?
6. What rules govern execution (traffic, priorities, restricted zones, battery thresholds, safety responsibility)?
7. What exceptions occur (stuck/lost robot, failed task, e-stop, obstacle) and how are they handled?
8. Who uses which interface (fleet map, robot detail, work queue, exception list, admin, analytics)?
9. Where are the boundaries: vs robotics engineering platform, vs WMS, vs road/AV/mining/marine fleet management, vs SCADA, vs agent orchestration, vs telematics?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Vendor | Philosophy / position | Customer tier | Evidence tier |
|---|---|---|---|---|
| OTTO Fleet Manager | OTTO by Rockwell Automation | AMR manufacturer's own fleet manager; enterprise manufacturing material handling | large manufacturers (Fortune 500 named) | Tier 1 (extensive public technical docs) |
| Fleet Central | Seegrid | AMR manufacturer's fleet software; multi-vendor orchestration via VDA 5050; perpetual license | manufacturers/warehouses (GM, Amazon, Ford named) | Tier 2 (product page + FAQ) |
| LocusONE | Locus Robotics | RaaS fulfillment platform; coordinates people + robots as one workforce | 3PL / retail / healthcare distribution | Tier 2 (product pages) |
| Formant | Formant | vendor-agnostic cloud robot operations platform (observability, teleop, commands, interventions) | robotics teams/operators across robot classes | Tier 1 (extensive public docs) |
| Orbit | Boston Dynamics | robot vendor's fleet/orchestration software for quadruped + case-handling robots; inspection-centric | enterprise industrial (Michelin, POSCO named) | Tier 2 (product page) |

Rejected/absent samples:

- **MiR (Mobile Industrial Robots) — MiR Fleet**: a major AMR vendor whose fleet product is a market anchor, but the vendor site returned empty content on 3 fetch attempts (JS-rendered). Excluded; no claims made about it. The AMR-manufacturer pole is covered by OTTO and Seegrid instead.
- **Omron Flow Core / Fleet Operation Manager, Zebra (Fetch) Cloud Fleet Manager, Geek+, InOrbit, Freedom Robotics, DJI FlightHub**: not fetched (time budget); the sampled five already show stable cross-product structure (stop condition satisfied).

## Sources

Fetched 2026-09-09:

- OTTO by Rockwell Automation — ottomotors.com root + /fleet-manager/ product page (Tier 2); docs.ottomotors.com documentation portal (Tier 1): About Fleet Manager, Task states, Robot statuses and states, plus full documentation TOC (monitoring, exceptions, fleet analytics, notifications, maps/endpoints/zones, workflows/tasks/steps, activities/bidding, adding a robot to a fleet, authentication, VDA5050, iAPI).
- Seegrid — seegrid.com root + /fleet-central/ product page incl. FAQ (Tier 2).
- Locus Robotics — locusrobotics.com root + /locusone platform page (Tier 2).
- Formant — docs.formant.io documentation hub + llms.txt index (Tier 1): Fleet management, Intervention requests, Plan a mission, Commands, plus full TOC (telemetry streams, views/modules, teleoperation, users/roles/teams, analytics, events/notifications, provisioning).
- Boston Dynamics — bostondynamics.com/products/orbit/ (Tier 2).

Unreachable / not fetched: mobileindustrialrobots.com (empty ×3, JS-rendered); Omron, Zebra/Fetch, Geek+, InOrbit, DJI (not attempted — stop condition reached).

## Product A — OTTO Fleet Manager (OTTO by Rockwell Automation)

### Key observations (Tier 1 unless noted)

- Positioning (Tier 2): "OTTO Fleet Manager gives you complete control of your material handling operations—all through one, easy-to-use platform"; "Whether you have one AMR or 100"; "software that intelligently pairs job requests and robots live, lowering average cycle time."
- Definition (Tier 1, About Fleet Manager): "OTTO Fleet Manager helps you automate materials handling at enterprise-scale." "OTTO Fleet Manager is in constant contact with the entire fleet of robots. Interfacing of a warehouse management system directly to OTTO Fleet Manager can be done using the OTTO Fleet Manager public API... Requests made to the OTTO Fleet Manager public API are translated into granular tasks which are then allocated and executed on the appropriate robot."
- Safety split (Tier 1): "OTTO Fleet Manager is NOT suitable as part of a safety system. Robots are independently responsible for their safe interaction with hardware and humans and the central management system is responsible for site automation safety coordination."
- UI (Tier 1): "web-based interface to command, control, and monitor various aspects of the complete robot solution... primary human interface... allows selective end point control of robots when required." Persistent storage of "pending, active, and completed tasks and metrics" (PostgreSQL).
- Work structure (Tier 1 TOC): Jobs → Workflows → Tasks → Steps. Task types: Charge, Empty Container, Fill Container, Load, Move, Mutate, Transport, Unload, Work In Place. Task states: QUEUED, EXECUTING, SUCCEEDED, CANCELLING, CANCELLED, FAILED, BLOCKED, STOPPED. "Activities" with "bidding" — robots bid on activities (auto-assignment mechanism).
- Robot states (Tier 1): UNKNOWN, OFFLINE (no heartbeat / shutdown), SYS (unavailable, manual, paused, neutral), STOP (emergency stop, lost, appliance, failed task, blocked), WAIT (safety stop, lost, queued, interlock, appliance, work in place, wait for input, paused); "Not Clear to Proceed" concept with a documented list of blocking states.
- Facility model (Tier 1 TOC): mapping a facility (recording maps, localization, remapping), map catalog (lock/duplicate/publish/distribute), endpoints (docks, chargers, parking, pallet, waypoint types; endpoint groups; queues), zones (exclusion, speed limit, traffic control single-robot, junction, narrow corridor, preferred direction, etc.), lanes/lines (stop line, yield line), workstations, annotations.
- Fleet ops (Tier 1 TOC): adding a robot to a fleet, removing, moving a robot to a different facility; installing AMR software; robot configuration files (import/apply/revert); monitoring jobs, AMRs, endpoints, interlocks; localizing a lost robot; changing robot mode; exceptions (accessing/filtering); notifications (SMTP/SMS/Slack channels, events); OTTO Fleet Analytics (work history monitor, export); statistics; Webviz (replay/root-cause analysis); scheduler (create/activate schedules); sending a robot to charge itself; demo mode.
- Integration (Tier 1 + Tier 2): public API for WMS; Industrial API (OPC-UA) for MES/PLC; VDA 5050 compliance (third-party controllers can order OTTO AMRs to move/charge/dock/activate lift/conveyor); commands issued "from a tablet, a computer, a button, or a pre-defined schedule."
- Auto-assignment (Tier 2): "Auto-assign AMRs for jobs based on battery levels, minimized idle time, and maximized utilization"; "charging opportunistically... between jobs"; "prevents congestion... exchange information between AMRs to predict approaching intersections."
- Scaling (Tier 2): new AMR "inheriting configurations from your existing fleet"; simulation before deployment.
- Auth/roles (Tier 1 TOC): LDAP, local, Okta (SSO) authentication; API access tokens; documentation organized by role (Integrator / Operator / Manager / Sales).
- Deployment (Tier 1 TOC): on-premises VMs (OVA images, single-node/multi-node: DB/Core/Web), offline install, firewall manual, NTP time sync — an on-prem server product.

## Product B — Fleet Central (Seegrid)

### Key observations (Tier 2)

- Definition: "Fleet Central is an enterprise software platform designed to orchestrate and manage your multi-vendor Autonomous Mobile Robot (AMR) fleet. With a user-friendly interface, Fleet Central connects directly to your facility's existing systems to automatically assign tasks and monitor vehicle battery health in real time to ensure your material handling operations run at peak efficiency."
- Work unit: "Create dynamic, adjustable AMR Jobs—sequences of locations and tasks—using an easy-to-use interface with no additional technical expertise required."
- Integration: "Easily integrate with your PLC devices, WMS/ERP/MES systems, and barcode scanners."
- Power management: "Leverage Auto-Charge to automatically dispatch... autonomous lift trucks to charging stations using Fleet Central's dedicated power management logic."
- Monitoring: "Track workflow utilization with real-time status monitoring of all AMRs and jobs."
- Traffic: "Manages complex environments and high-traffic aisles, ensuring mixed-fleet autonomous vehicles and manual equipment move smoothly without congestion."
- Interoperability: "As a VDA 5050 interoperable platform, Fleet Central can unify control of Seegrid AMRs alongside third-party automation equipment who also share VDA 5050 compliance."
- FAQ (load-bearing): "Seegrid AMRs can be trained and operated without Fleet Central; however we recommend this only for a single AMR. With multiple vehicles, you'll need Fleet Central to manage intersections, jobs, and a whole lot more." — direct evidence that the fleet manager's role is multi-vehicle orchestration (intersections, jobs, charging, workflows), not single-robot operation.
- Deployment/business model: "runs on a dedicated server that can be provided by the customer or purchased from Seegrid"; "sold as a perpetual license with a one-time fee."
- Lineage: "an advancement of the same proven software that was introduced as Seegrid's foundational fleet management and analytics platforms: Fleet Geek and Supervisor."

## Product C — LocusONE (Locus Robotics)

### Key observations (Tier 2)

- Definition: "A data science-driven warehouse automation platform for enterprise-wide AMR deployments and performance management." "Operate a single, coordinated fleet with multiple AMR form factors through one warehouse automation platform."
- Scale claim: "can support a thousand or more robots in sites as large as one million square feet or more, operating simultaneously in a single, intelligent, scalable, and orchestrated solution" (marketing claim; kept at claim strength).
- Work: unified fleet "performing multiple concurrent operations, including each picking & putaway, case picking & putaway, replenishment, autonomous fulfillment, routine tasks such as parts-to-line, dunnage, or milk runs, point-to-point transport, counting, and more — all within a single facility."
- Orchestration across humans and robots: "LocusONE dynamically coordinates work across associates and robots to keep operations moving" — the managed workforce includes people.
- Reporting: "LocusHub package, delivering data-driven, actionable insights across more than two dozen insightful reports and real-time dashboards, including labor guidance, predictive insights for work completion, operational comparisons against targets or time periods, order pool tracking and guidance, mission analysis and optimization."
- Integration: "LocusONE integrates with any WMS system to provide flexible and dynamic fleet management"; integrates with other automation (sortation, packaging).
- Business model: Robots-as-a-Service (RaaS) — vendor operates; fleet management is part of the service.

## Product D — Formant

### Key observations (Tier 1)

- Platform definition: "The Formant software platform allows companies to run fleets of robots or advanced connected devices, and implements workflows in remote monitoring, interventions, data management, teleoperation, tech-support investigations, and business analysis. It also provides the extensible cloud infrastructure that can be built upon to create custom robot management experiences."
- Robot register: devices provisioned with the Formant agent (Docker/Debian/apt install, provisioning tokens, bulk/automated provisioning); device groups; tags; configuration templates ("Create configuration templates to quickly and easily provision many robots at once"); delete/disable device.
- Telemetry: streams (ROS topics, localization, transform trees, video, files, directory watches), ingestion rates, on-demand streams; timeline; views and modules (map, 3D scene, video, heatmap, terminal, diagnostics); multi-device observability.
- Work direction: Commands ("tell our robot to take a predefined action... trigger data ingestion, run a script, or tell our robot to return to its home position"; issued from UI or during teleop; event-triggered; scheduled; command lifecycle issued → delivered → complete with cloud queueing and expiration); Mission planning (waypoints drawn in the 3D Scene module, sent to the robot's ROS service; per-waypoint properties).
- Intervention: "Intervention requests give your robot the ability to request user input to determine a course of action" — selection requests (choose from options) and labeling requests (draw a boundary + label); robot-initiated human help.
- Teleoperation: build teleop interfaces (joystick, video, buttons), real-time connections (WebRTC), network statistics during teleop.
- Events/notifications: events with notifications (PagerDuty, Slack, SMS, webhooks); incident management.
- Organization: users, roles, teams; access levels; SSO (Google, OIDC); audit log; service accounts.
- Analytics: SQL-queryable analytics, task summaries, data export (S3, Sheets).
- Extensibility: embedded views, white-labeling, custom modules, SDKs (Agent SDK, Cloud SDK, Data/UI SDK), adapters (ROS/ROS 2, ZeroMQ).

## Product E — Orbit (Boston Dynamics)

### Key observations (Tier 2)

- Definition: "Shared orchestration and intelligence software for all your Boston Dynamics robots." "It is your portal into your facilities, operations, and autonomous robots, with AI-driven insights, intuitive dashboards, and powerful integrations."
- Task management: "Orbit offers a powerful set of task management and orchestration tools to put your robots to work."
- Fleet management feature list: "Mission editing and scheduling; Map-based dashboard; Remote robot operation; Performance summaries."
- Inspection features: "Automated in-product and email alerts; Remote inspection authoring and editing; AI vision-language model for visual inspections."
- Enterprise: "Customize user profiles; Multi-site view; SSO access; SOC2 Type II certified."
- Integration: "APIs; Webhooks; Low-code work order generation (beta)"; "integrate into CMMS, WMS, and other systems of record."
- Deployment: Cloud (AWS-hosted), Site Hub (1U rack-mounted on-premise network application), Virtual Machine (OVA for VMware/Hyper-V/Azure/Google Cloud).
- Customer usage quotes: "Our team uses Orbit to control the robots. We also use it for scheduling missions, reviewing facility inspection data, and adjusting map parameters" (POSCO); "the brain behind what's happening with Spot... you can see every single motor scan" (Michelin).
- Multi-site: "centralized dashboards that aggregate data from all sites — giving you a unified view of robot activity, site performance, and fleet health."

## Cross-product Comparison

| Dimension | OTTO Fleet Manager | Seegrid Fleet Central | Locus LocusONE | Formant | Orbit |
|---|---|---|---|---|---|
| Robot register | add/remove robot to fleet; move between facilities; robot config files | multi-vendor AMR fleet; single AMR can run without it | unified multi-form-factor fleet | devices + agent provisioning; groups; tags | Spot/Stretch robots; multi-site |
| Work unit | Jobs → Workflows → Tasks → Steps | AMR Jobs (sequences of locations and tasks) | missions/tasks (pick, putaway, transport, count...) | commands; missions (waypoints) | missions (edit + schedule) |
| Assignment | auto-assign via "bidding" (battery/idle/utilization) | automatically assign tasks | coordinates work across people + robots | manual / scheduled / event-triggered | mission scheduling |
| Live monitoring | map; robot statuses/states; Monitor Work panel | real-time status of AMRs and jobs; battery | real-time dashboards | telemetry streams; views; timeline | map-based dashboard; live views |
| Exceptions | exceptions list; lost-robot localization; robot modes | (not documented at fetched tier) | (not documented at fetched tier) | intervention requests; events | alerts; remote operation |
| Energy | opportunistic charging; charge tasks | Auto-Charge power management | (not documented) | (device-dependent) | (robot-dependent) |
| Facility model | maps, endpoints, zones, lanes, queues, workstations | facility workflows; intersections | facility-wide | maps/3D scenes per device | Site View; map parameters |
| Business-system integration | WMS via API; MES/PLC via OPC-UA; VDA 5050 | PLC, WMS/ERP/MES, scanners; VDA 5050 | any WMS; sortation/packaging | APIs/SDKs; webhooks; PagerDuty/Slack | CMMS/WMS; APIs/webhooks |
| Analytics | Fleet Analytics; statistics; replay tooling | workflow-improvement data | LocusHub reports/dashboards | SQL analytics; task summaries | performance summaries; trends |
| People/roles | role-based docs; LDAP/Okta | low-touch operator experience | labor guidance | users/roles/teams; SSO; audit | user profiles; SSO; multi-site |
| Remote operation | OTTO App remote control | (not documented) | (not documented) | teleoperation | remote robot operation |
| Deployment | on-prem VMs (OVA) | dedicated server (customer or vendor) | vendor cloud (RaaS) | cloud SaaS | cloud / on-prem appliance / VM |
| Business model | bundled with AMR purchase | perpetual license | RaaS | subscription | subscription/bundled |

### Stable cross-product structure (Layer B evidence)

All five products hold: (1) a register of individually identified robots under management; (2) a work unit — mission/job/task — directed to robots and executed by the robots themselves; (3) a fleet-side oversight loop (live monitoring + dispatch/intervention + fleet health). All five also show: live status/map surfaces, business-system integration (WMS/MES/CMMS), notifications/alerts, analytics/reporting, user/role machinery. Four of five show battery/charging management (mobile robots; Orbit's robots are battery-powered too but charging machinery was not documented at the fetched tier). Three of five show explicit traffic/facility-rule machinery (OTTO, Seegrid; Locus implicitly). Two of five show teleoperation/remote operation as a first-class surface (Formant, Orbit; OTTO has remote control via OTTO App).

## Canonical Model (Layer C)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The robot register** — the fleet's robots held as individually identified managed units (each with identity, type, status), added onto and removed from the system as managed members. Remove → a robot inventory/asset list, not a management system.
2. **Work directed to robots as executable missions/tasks** — the system's unit of work is a task or mission assigned to robots, and the robots themselves are the executing party (transport, inspection, picking, patrol...). Remove → a monitoring dashboard over robots that do nothing directed.
3. **The fleet-side oversight loop** — a fleet-side role continuously watches live execution across the fleet and acts on it: dispatch/queue/prioritize work, intervene when a robot or task needs help, manage robot state and health. Remove → autonomy running unmanaged (a robot system, not fleet management).

Jointly-held load-bearing:

- 1 alone = robot inventory
- 2 alone = a task queue with no fleet
- 3 without 1+2 = an observability platform
- 1+2 without 3 = robots executing with no management surface
- 1+3 without 2 = monitoring with nothing directed
- 2+3 without 1 = dispatch machinery over no fleet

Deliberately excluded from L0 (tested against the historical check):

- **Maps / facility models** — dominant for mobile robots, but the register+work+oversight core does not require a spatial map (inspection-robot fleets can run schedule-driven missions; Formant's map is a per-device view module). Map machinery is L1.
- **Battery/charging management** — universal for mobile robots but a consequence of the robot population, not the definition; a wired/arm fleet would not carry it.
- **Traffic management / collision avoidance** — AMR-specific implementation of the oversight loop's rules; the invariant is that the operator can constrain and coordinate execution, not any specific traffic mechanism.
- **Auto-assignment intelligence** — the assignment act is the invariant; its intelligence (bidding, optimization, AI) spans manual to algorithmic.
- **Teleoperation** — one implementation of intervention; intervention paths vary (assistance, mode change, recovery, teleop).
- **VDA 5050, cloud, RaaS, SSO** — era/regime/business-model machinery.

### L1 — Common Mature Structure

- Live fleet map / status dashboard (robot positions, states, active work)
- Auto-assignment/dispatch logic (battery level, utilization, proximity, priority)
- User-visible robot states and task states (incl. blocked/failed/e-stop classes)
- Exception surfacing and recovery paths (stuck/lost robot, failed task, obstacle stops)
- Battery/charging management (opportunistic charging, charge tasks, power logic)
- Facility/site model (maps, endpoints/docks/chargers, zones, traffic rules, queues)
- Integration with business systems (WMS/MES/ERP/CMMS) and industrial control (PLC/OPC-UA); interoperability standards (VDA 5050)
- Notifications/alerts (email/SMS/Slack/PagerDuty/webhooks)
- Analytics/reporting (utilization, throughput, mission analysis, trends)
- Users, roles, authentication (local/LDAP/SSO), audit
- Remote operation / teleoperation (in some products first-class)
- Fleet maintenance machinery (software updates, configuration distribution, robot commissioning/decommissioning)

### L2 — Variant / Optional Structure

- Robot population: AMR/AGV material-handling fleets vs inspection quadrupeds vs drones vs (unverified) fixed arms; single-class vs mixed fleets; mixed robot+human workforces (Locus coordinates associates and robots).
- Vendor posture: robot-manufacturer-integrated (OTTO, Seegrid, Orbit) vs vendor-agnostic platform (Formant) vs RaaS operator (Locus).
- Interoperability: VDA 5050 multi-vendor orchestration (Seegrid, OTTO) vs proprietary single-vendor stacks.
- Deployment: on-prem server/VM (OTTO, Seegrid, Orbit Site Hub) vs cloud SaaS (Formant, Orbit cloud) vs vendor-operated (Locus RaaS).
- Business model: bundled with robots vs perpetual license vs subscription vs RaaS.
- Teleoperation depth: none / remote assistance / full teleop.
- AI overlays: vision-language inspection (Orbit), agentic AI (Locus), AI assignment tuning.
- Safety governance: safety owned by robot hardware with the fleet manager explicitly excluded from safety functions (OTTO's documented split); safety certification regimes vary.

### L3 — Vendor-specific (Research Notes only)

- OTTO: Activities "bidding" rules; Webviz replay/root-cause tool; Industrial API (iAPI); endpoint type taxonomy (hex dock, V-dock, wing dock...); zone type taxonomy (tunneling, lookahead, dilation...); OTTO App companion; demo mode; Clearpath telemetry endpoints.
- Seegrid: GRID Engine / Sliding Scale Autonomy; Fleet Geek/Supervisor lineage; Auto-Charge; ABM (Autonomous Buffer Management).
- Locus: LocusHub; Locus Array/Origin/Vector form factors; RaaS packaging; "2-3x productivity" claims.
- Formant: agent/SDK architecture (Agent SDK, Cloud SDK, Data/UI SDK); intervention request types (selection, labeling); 72-hour command expiration and on-device queue limit (product-specific operational details); adapters; white-labeling.
- Orbit: AIVI-Learning (Gemini-powered); Site View (360° imagery); Site Hub appliance; low-code work-order generation (beta).
- None of these enter the final document except as neutral examples.

## Vendor-specific Findings

- Seegrid's FAQ documents that its AMRs can run without the fleet software for a single robot — the strongest direct evidence that the fleet manager's defining role is multi-robot orchestration, not robot operation.
- OTTO's docs explicitly split safety responsibility: robots own their safe interaction; the fleet manager owns site-automation coordination and is "NOT suitable as part of a safety system." A structural rule of the Type, evidenced at one product (treat as strong single-source; consistent with industry practice but not independently confirmed elsewhere in this sample).
- Locus extends the managed workforce to humans ("coordinates work across associates and robots") — a warehouse-fulfillment variant where the fleet manager doubles as a labor-coordination layer.
- Formant is robot-agnostic and observability-first but still carries the full loop (commands, missions, interventions, teleop) — evidence that the oversight loop, not telemetry alone, defines the Type even at the platform pole.
- Orbit bundles inspection-data intelligence (AI vision models, digital-twin capture) with fleet management — a data-value overlay on the same core.

## Boundary Findings

1. **vs Fleet Management System (road, §18 — DISCHARGES the fleet-management-system pass's sibling flag from this side)**: the two Types share the family pattern (register + activity + oversight). The road FMS supervises human-driven vehicles — its center is the driver (behavior, hours, assignment) and its oversight acts by scheduling service and assigning people. Robot Fleet Management supervises robots that execute the work themselves — there is no driver dimension; the oversight acts by dispatching work and intervening on robots. Removal test: replace robot execution with human drivers → road FMS; add drivers/HOS/compliance to this Type → road FMS. **Verdict: keep-both RATIFIED — related Types sharing the register+oversight family pattern**, consistent with the marine and mining passes' verdicts.
2. **vs Autonomous Fleet Management (§18 — DISCHARGES the AFM pass's "joint awareness" note from this side)**: AFM's object of oversight is the road vehicle's autonomy execution (validated operating conditions, remote assistance, safe-state recovery) in public-road/mixed-traffic context. Robot FM's object of oversight is the work robots perform for a site operation (missions, tasks, facility rules). An AMR is autonomous, but autonomy is not the discriminator — the domain object world is (road traffic vs facility work). Removal test: move the fleet onto public roads with permits/traffic → AFM; bring it back inside a facility with maps/zones/work queues → this Type. Distinct sibling Types sharing the family pattern.
3. **vs Mining Fleet Management (§20 — DISCHARGES the mining pass's forward flag from this side)**: mining FMS centers the production cycle (load→haul→dump, material identity, shift production records). Robot FM centers task execution (missions/jobs assigned to robots). The mining pass's hypothesis ("task-execution-centric robot missions vs production-cycle-centric mine fleet") is CONFIRMED from this side. Removal test: add production-cycle machinery (loads, destinations, material, tonnes) → mining FMS; strip it to task/mission execution → this Type. Keep-both.
4. **vs Marine Fleet Management (§18)**: marine is asset-administration-centric (equipment-structured technical record, crew, class/certificates, ship–shore loop). No shared record objects with robot FM beyond the family pattern. Keep-both (already ratified from the marine side).
5. **vs Robotics Engineering Platform (§16 sibling, unprocessed — FORWARD FLAG)**: expected seam — authoring/programming/simulating robot applications vs operating deployed fleets. Evidence from this side: OTTO ships simulation as a separate service; Formant explicitly positions itself as operations infrastructure, not a robot-programming tool; Orbit consumes robots, doesn't build them. When that leaf is processed, expect "build/program robots vs run robots" as the seam; this pass leaves the flag for it.
6. **vs Warehouse Management System (§10, processed)**: WMS owns the warehouse's inventory and directed human work; robot FM owns the robots that execute part of that work. All sampled AMR-fleet products document WMS integration as the trigger path (OTTO: WMS via public API; Seegrid: WMS/ERP/MES integration; Locus: integrates with any WMS). The seam is decides-vs-executes: the WMS decides what work the operation needs; the robot FM executes it with robots. Removal test: remove the robots → WMS remains; remove the inventory/business layer → robot FM remains.
7. **vs SCADA / HMI (§16)**: SCADA supervises fixed process equipment through control loops; robot FM directs mobile/autonomous robots through a task loop over a facility model. Different object worlds; both may share a control-room posture.
8. **vs Agent Orchestration Platform (§13, processed)**: both "orchestrate" workers, but the record worlds are disjoint — software agents executing digital tasks vs physical robots executing physical missions with maps, batteries, and safety. No shared objects; naming-adjacent only.
9. **vs Vehicle Telematics Platform (§18)**: same seam as the road-FMS pass documented — telematics is the data-acquisition layer; robot FM is the management application over the fleet. Formant's observability depth shows the data layer can be rich, but its commands/missions/interventions are what make it fleet management rather than telemetry.
10. **vs Machine Vision Platform (§16, processed)**: vision systems give robots per-item decisions at the line; robot FM manages the fleet. Consistent with the machine-vision pass's own note ("robot consumes vision results").
11. **"去掉什么就变成另一个 Type" 判据**: remove robots-as-executors (humans execute, system tracks work) → WMS/CMMS territory; remove the fleet register → robot telemetry/observability; remove the oversight loop → an unmanned autonomy stack; add road-traffic machinery → AFM; add production cycles → mining FMS; make the workers software agents → agent orchestration.

## Historical / Market-Sample Check (§24)

- **AGV era (1980s–1990s)**: central AGV controllers/dispatch systems held vehicle registers, assigned transport jobs, and coordinated traffic — satisfying all three L0 legs with no cloud, no AI, no SLAM. Seegrid's own FAQ preserves the single-robot-without-fleet-manager vs multi-robot-requires-fleet-manager distinction, evidence that the core is about the fleet, not modern machinery.
- **Teleoperation-era robots and drone fleet operations** fit the same core (register + directed missions + oversight); not directly fetched, reasoned at canonical-inference strength.
- The definition names no navigation technology (SLAM/LiDAR/magnetic tape), no protocol (VDA 5050), no deployment shape (cloud/on-prem), no business model (purchase/license/RaaS). All are era or variant machinery.
- Regional check: the sample is North-America/Europe-weighted (US AMR vendors + Boston Dynamics). Asian AMR ecosystems (Geek+, Quicktron) were not fetched; the L0 is domain-neutral and should accommodate them, but this is not directly verified.

## Uncertainties

1. **MiR Fleet unreachable** (JS-rendered site, 3 attempts). A major AMR-fleet anchor is therefore unverified; no claims made about it. The AMR-manufacturer pole rests on OTTO (Tier 1) and Seegrid (Tier 2).
2. **Tier-2 evidence for Seegrid/Locus/Orbit**: state vocabularies, exception mechanics, and precise operational rules are asserted only for OTTO and Formant (Tier 1). Claims about the other three are kept at product-page strength.
3. **Fixed-arm fleet management** (e.g., vendor "connected robots" services for CNC/robot arms) not directly documented; the Type's population breadth beyond mobile robots is reasoned at canonical-inference strength.
4. **Drone fleet management** (DJI FlightHub class) not fetched; assumed to fit the core; unverified.
5. **Whether any product ships without a live map/dashboard surface** — not observed; the live fleet picture is held common-mature rather than definitional for safety.
6. **OTTO's safety-responsibility split** is single-source (Tier 1, explicit); treated as a strong product-documented rule, generalized only cautiously in the final document.
7. **Locus's human+robot coordination depth** (how labor assignment interleaves with robot dispatch) documented only at product-page strength.

## Final Synthesis

Robot Fleet Management is the operator-facing system for running a fleet of robots: it holds the fleet's robots as individually identified managed units, directs work to them as executable missions/tasks that the robots themselves carry out, and gives fleet-side staff a continuous oversight loop — watch the fleet live, dispatch and prioritize work, intervene when a robot or task needs help, and keep the fleet healthy (battery/charging, software, configuration). Around that core, mature products add live maps and status dashboards, auto-assignment logic, user-visible robot/task states, exception and recovery machinery, facility models (maps, endpoints, zones, traffic rules), business-system integration (WMS/MES/CMMS, PLC, VDA 5050), notifications, analytics, roles/SSO, and remote operation. The market realizes the Type across a vendor-posture axis (robot-maker-integrated vs vendor-agnostic vs RaaS), a robot-population axis (AMR material handling vs inspection robots vs drones), a deployment axis (on-prem server vs cloud), and an interoperability axis (proprietary stack vs VDA 5050 multi-vendor). The Type is bounded against road/AV/mining/marine fleet management (same family pattern, different object worlds), against WMS (decides-vs-executes), against robotics engineering platforms (build vs run — forward flag), against SCADA (fixed process vs mobile task execution), and against agent orchestration (software workers vs physical robots).
