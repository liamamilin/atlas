# Research Notes — Building Management System / BMS

Slug: building-management-system-bms
Research date: 2026-09-06
Methodology: v1.1 (update-v1)

## Research Goal

Understand what a Building Management System (BMS) actually is as an Application Type: what objects it manages (plant, devices, points, equipment), how control and supervision work, who operates it, and where its boundary lies against the neighboring building-stack Types (Building Energy Management, Building Access & Visitor Management, Building Asset Management, Building Maintenance Management, Building Commissioning Platform, Facility Management / IWMS) and against the industrial-control Types (SCADA / DCS / HMI).

## Initial Boundary

Initial hypothesis: a BMS is the operational control system for a building's mechanical and electrical plant — HVAC first, commonly lighting, energy metering, and monitored integration of other systems. It connects field devices (sensors, actuators, controllers), runs configured control logic automatically (schedules, setpoints, sequences), and gives facility staff a supervisory surface to observe live state and intervene. Historical names: "Building Automation System" (BAS) in North America, "BMS" globally, historically "Energy Management and Control System" (EMCS). Nearest confusions: energy analytics platforms (same buildings, different object), industrial SCADA (same control grammar, different domain), facility/maintenance management systems (same buildings, different loop: work orders vs control).

## Research Questions

1. What are the core objects — points, controllers, equipment, networks — and how do they relate?
2. What does "control" mean concretely: who executes the control loop, and what is configured vs automated vs human?
3. What does the operator actually do day to day (monitoring, alarm handling, setpoint/schedule changes, overrides)?
4. What engineering/configuration surfaces exist (programming sequences, templates, graphics authoring, device discovery)?
5. How is history captured (trend logs, runtimes) and consumed (charts, reports, analytics)?
6. How do the deployment shapes differ (on-prem workstation/server vs web/enterprise vs cloud-native SaaS)?
7. Where is the line vs Building Energy Management, SCADA/DCS/HMI, access control, maintenance/CMMS, and facility management?
8. Does the definition survive the historical check (pre-BACnet EMCS era) and the cloud-native challenger shape?

## Representative Products

| Product | Vendor | Why chosen | Evidence level reached |
|---|---|---|---|
| Metasys | Johnson Controls | legacy enterprise BAS incumbent; direct-sales giant | Tier-2 product pages (docs portal JS-gated) |
| RC-Studio + MACH/RC-FLEX controller stack | Reliable Controls | BACnet-native, dealer-channel, freely programmable philosophy | Tier-2 product pages with detailed feature lists |
| enteliWEB + Red5/O3 stack | Delta Controls | open-protocol enterprise + room-level + cloud SaaS posture | Tier-2 systems/product pages |
| Facilisight + CCU/SmartNode/HyperStat stack | 75F | cloud-native wireless SaaS challenger, mid-market, AI-tuned | Tier-1 help-center category structure (article pages blocked) |

Rejected/absent from sample (unreachable): Schneider EcoStruxure Building Operation (se.com 403), Tridium Niagara (tridium.com 404/500; docs portal login-gated), Distech Controls (403). Siemens Desigo CC not attempted (gating pattern). These are market-context names only — no claims made for them.

## Sources

- Johnson Controls — "Metasys BAS" product page — https://www.johnsoncontrols.com/building-automation-and-controls/metasys — 2026-09-06 (fetched)
- Johnson Controls — "Johnson Controls Launcher (SMP and SCT)" page — https://www.johnsoncontrols.com/metasys — 2026-09-06 (fetched; reveals Site Management Portal / System Configuration Tool / engine firmware terminology)
- Johnson Controls — docs.johnsoncontrols.com/bas (Building Automation Knowledge Exchange) — JS application, content not retrievable
- Reliable Controls — Products overview — https://www.reliablecontrols.com/products/ — 2026-09-06 (fetched)
- Reliable Controls — RC-Studio BACnet Advanced Workstation Software — https://www.reliablecontrols.com/products/software/RCST/ — 2026-09-06 (fetched; detailed feature list)
- Delta Controls — Building Management systems page — https://deltacontrols.com/systems/building-management/ — 2026-09-06 (fetched)
- Delta Controls — corporate home (product/protocol grid) — https://deltacontrols.com/ — 2026-09-06 (fetched)
- 75F — Support Center home — https://support.75f.io/ — 2026-09-06 (fetched)
- 75F — Facilisight help category — https://support.75f.io/hc/en-us/categories/5484597414931-Facilisight — 2026-09-06 (fetched; individual article fetches 403)

## Product A — Johnson Controls Metasys (Tier-2)

### Key observations (A = directly observed on fetched pages)

- Self-description: "Metasys is a leading building automation system (BAS) that integrates HVAC, lighting, security, and fire protection systems on one secure platform… makes it easy for facility managers to monitor building system performance, improve energy efficiency and decarbonization, and keep building occupants safe, comfortable and productive." (A)
- Operated from a browser: "You can operate Metasys from any device using a web-based interface, requiring no special software or plug-ins." (A)
- Integration openness: "truly open architecture that lets you seamlessly integrate third-party equipment and technologies." BACnet 19 support named. (A)
- Scale statements (vendor claims, L3): 1,300 IP devices and 65,000 objects per server; server redundancy for continuous operations. (A-as-claim)
- ASHRAE Guideline 36 alignment "including 40+ water-side and 64 air-side rules", "Fault Detection and Fault Triage … create a daily punch list to guide staff" (A-as-claim; G36 = pre-engineered sequences)
- Energy Management suite: dashboards, reports, IAQ monitoring/reporting, EPBD-ready dashboard (A-as-claim)
- Compliance variant: "Metasys for Validated Environments (MVE) provides traceable electronic records, signatures and time-stamped audit trails"; "Mean Kinetic Temperature reporting"; smoke control system UL 864 listed (A-as-claim)
- Engineering tooling terminology from the Launcher page: Site Management Portal (SMP), System Configuration Tool (SCT), supervisory devices/"engines", engine firmware, resource files (A)
- Lifecycle Management portal "to help design, configure and maintain building assets" (A-as-claim)
- Customer universe framing: facility managers; buildings from "small office buildings to massive, multi-site campuses and complex facilities like data centers, hospitals and universities" (A)

## Product B — Reliable Controls (RC-Studio + controller stack) (Tier-2)

### Key observations

- Company framing: "building control products for use in distributed control systems… simple to install and program, flexible to network"; "Integrated solution for HVAC, lighting, and security"; "freely programmable controllers"; BACnet industry-standard protocol. (A)
- Controller family: freely programmable BACnet Building Controllers spanning system-level (MACH-ProSys), air-handling/VAV terminal (MACH-ProAir, RC-FLEXair), lighting (MACH-ProLight), zone/room (MACH-ProZone, SMART-Space), with built-in web-server operator workstation (MACH-ProWeb series); access-control controllers listed separately as "Security Series" (MACH-CheckPoint door access). (A)
- RC-Studio = "BACnet Advanced Workstation (B-AWS)" — "multivendor, multiprotocol integration solution for database, alarming, scheduling, trending, and sequence of operation programming." (A)
- Workstation features (detailed list): automatic BACnet discovery of all devices; retain discovered devices between sessions; create/delete/drag BACnet objects; database worksheets; "Full priority array control"; Workstation Groups for third-party BACnet devices. (A)
- Programming: "Program inputs, outputs, values, loops, arrays, schedules, and calendars"; "Single-point Trend Logs, and Multipoint Trend Logs"; runtime logs; sequence-of-operation code editor with syntax highlighting and watch lists. (A)
- Graphics: System Group editor; RC-GrafxSet images/animations; "HTML5 graphics … animating equipment, buttons, dashboards, charts, gauges, maps"; links between graphics. (A)
- Deployment machinery: Templates — "Deploy and update multiple … controllers with a single Panel File Template. Changes are automatically propagated across the network"; automated file synchronization between workstations; automated network backup. (A)
- Simulate Mode: "program an entire system offline without controller hardware." (A)
- Alarm machinery: "Alarm monitoring and annunciation to screen, email, and printer." Reports: point-report worksheets, wild-card search. (A)
- Companion software (catalog): RC-WebView (BACnet Operator Workstation Software), RC-Archive (Data Archiving), RC-Reporter (Building Performance Reporting), RC-RemoteAccess (BACnet VPN), RC-Passport (Security Management), RC-GrafxSet, RC-Toolkit (Integration & Configuration), myControl App (customized mobile apps), MACH-ProWeb BUI. (A)
- Channel: authorized-dealer model (Dealer Locator; "Become a Dealer"). (A)

## Product C — Delta Controls (enteliWEB + Red5/O3) (Tier-2)

### Key observations

- Building Management system page: "our solutions unify HVAC, lighting, energy, and security into a single intelligent platform—helping owners, operators, and occupants thrive"; "open protocol platform." (A)
- Hardware decomposition: Red5 controllers "PLUS, EDGE, FIELD, ROOM, VAV — deliver scalable control from system-level to individual rooms"; O3 Sensor Hub — ceiling multi-sensor (temperature, humidity, motion, light, sound) "replaces multiple devices with one ceiling hub"; eZNT thermostats; eZNS sensors. (A)
- Enterprise software: "enteliWEB: Web-based enterprise building and energy management platform with dashboards, reporting, alarm management, and compliance tools." enteliCLOUD: "SaaS deployment option enabling secure, remote building management." enteliVIZ, enteliVAULT, Canvas (digital twin, design→construction→operations). (A)
- Protocols grid: BACnet/IP, BACnet MS/TP, BACnet/SC, Modbus, EnOcean, DALI, SMI, Bluetooth, NFC, Wi-Fi. (A)
- Sequences: "Guideline 36 Ready: Preloaded sequences for VAVs and AHUs to optimize energy and maintain compliance." (A)
- Programming freedom: GCL plus "Python and Node-RED support for custom programming and integration with business systems and cloud services." (A)
- Energy/sustainability layer: "Virtual metering, energy baselining, sustainability reporting"; ENERGY STAR; ESG reporting; Earthright Energy Dashboard; Multi-Site Portfolio Management. (A)
- Room-centric variant: "Red5 ROOM and O3 hubs unify HVAC, lighting, blinds, AV, and access in one controller"; occupant comfort framing ("fewer complaints"). (A)
- Commissioning ease: NFC/Bluetooth provisioning, Proviso mobile app. (A)
- Verticals: healthcare, higher education, K-12, data centers, government, multi-site retail, warehouse. (A)

## Product D — 75F (Facilisight cloud + wireless hardware) (Tier-1 category structure)

### Key observations (help-center category tree + support home)

- Hardware ecosystem categories: CCU (Central Control Unit), SmartNode, HyperStat / HyperStat Split, Mystat, HelioNode, Sensors, Connect Module. (A)
- Facilisight = "Web and Mobile Application" — the cloud supervision surface. (A)
- Surfaces and sections in the help center: User Management (incl. Billing Admin), Site Dashboard, Site Overview, Heatmap (Setting Up Your Floorplan, Zone Filters, Heatmap Data Points Review), Scheduling & Temperature (Scheduler Introduction; Master Controller (Building Temperature Control); Temperature Modes with single setpoint / setpoint offset / dual setpoint fixed & variable deadband; Bulk Applying Special Events & Vacations; Zone Schedule vs Shared Schedule; Overnight Schedules; Special Schedules Via API), Alerts (Managing Alerts in portal and mobile app; Interpreting Alerts; Custom Alerts with restricted times), Analytics & Visualizations (Portfolio Analytics Manager (PAM); predefined and custom visualizations; energy configuration in PAM), Occupant App, Certified Installer Options (Installers Tables, Notes & Cloud Storage, Alert Configuration), FAQs. (A)
- Installer/commissioning flow exists as a first-class concern (Site Installation Report Via "Easy Street"; pairing best practices; field installation best practices). (A)
- Tuning: "Working with Tuners" article title — implies a tuning layer over control. (A, title-level only)
- Positioning line: "The Future of Control, Today." (A)
- Article-level details not retrievable (403); no numeric claims used.

## Cross-product Comparison

| Dimension | Metasys (JCI) | Reliable Controls | Delta Controls | 75F |
|---|---|---|---|---|
| Self-identification | building automation system (BAS) | building control products / BACnet BAS | Building Management system | "Future of Control" (control company) |
| Field layer | engines/supervisory devices + third-party integration | freely programmable BACnet building controllers (system→zone) | Red5 controllers (system→room), O3 multi-sensor hub | CCU + SmartNode/HyperStat wireless controllers + sensors |
| Equipment organization | "objects" per server (65,000 claim) | BACnet objects; database worksheets | system-level→room-level decomposition | sites → zones → equipment (heatmap over floorplan) |
| Scheduling | standard BAS workflows (G36 alignment) | schedules + calendars programmed; templates | G36 preloaded sequences; schedules in software | Scheduler; zone vs shared schedules; special events/vacations; API |
| Alarms | FDD triage "punch list" | annunciation to screen/email/printer | enteliWEB alarm management | alerts in portal+mobile; custom alert config |
| History | energy suite analytics; reports | trend logs (single/multi-point), runtime logs, RC-Archive | energy baselining; virtual metering | heatmap data points; PAM visualizations |
| Graphics | web UI, dashboards; legacy graphics conversion tooling | System Group editor; HTML5 animations, gauges, maps | enteliWEB dashboards; Canvas digital twin | site floorplan heatmap; site overview |
| Integration posture | open architecture; third-party equipment; BACnet 19 | multivendor multiprotocol; third-party BACnet groups | BACnet/IP, MS/TP, BACnet/SC, Modbus, EnOcean, DALI, SMI | cloud-native stack; (protocol breadth not observed) |
| Engineering surface | SCT/Site Management Portal; Lifecycle portal | sequence-of-operation editor; simulate mode; templates | GCL + Python/Node-RED; NFC/Bluetooth provisioning | cloud commissioning; installers tables; Easy Street report |
| Access surfaces | browser, any device; mobile access | workstation (Windows), web (RC-WebView), mobile app | enteliWEB web; enteliCLOUD SaaS; mobile apps | web portal + mobile app + occupant app |
| Multi-site | multi-site campuses; enterprise dashboards | multi-controller templates; network backup | Multi-Site Portfolio Management | Portfolio Analytics Manager across sites |
| Deployment | on-prem servers + web client | on-prem workstation + web + controller-hosted | on-prem + SaaS (enteliCLOUD) | cloud-native SaaS |
| Channel | direct/global | authorized dealers | certified partners | certified installers |

### Stable commonalities (Layer B — cross-product)

1. **Instrumented, networked plant**: every product is a system of connected controllers/sensors/actuators across building mechanical/electrical systems.
2. **Automated execution of configured control**: schedules, setpoints, and control sequences run on the plant without a human commanding each step (Reliable: "program … schedules"; 75F: scheduler + modes; Delta/Metasys: G36 sequences).
3. **Central supervisory monitor-and-command surface**: live observation of equipment state + operator changes (graphics/dashboards everywhere; point/level access everywhere).
4. **Alarm/event machinery** (annunciation, handling).
5. **Trend/history capture** (trend logs, runtimes, archived data) consumed as charts/reports/analytics.
6. **Equipment/point organization** (objects, database worksheets, zones, equipment graphics).
7. **Engineering/configuration tooling** (sequence programming or pre-engineered sequence libraries; templates; device discovery; provisioning).
8. **Web/mobile operation** (all four).
9. **Multi-vendor/open-protocol integration** (three of four observed explicitly; 75F not observed on this point).
10. **Energy/sustainability reporting layer** (all four, in varying depth).
11. **Role/user management** (all four).
12. **Multi-site/portfolio posture at the upper tier** (three of four observed explicitly).

### Divergences (Layer C — variant axes)

- Deployment substrate: on-prem workstation/server (Reliable, Metasys) ↔ SaaS enterprise (Delta enteliCLOUD) ↔ cloud-native SaaS (75F).
- Control philosophy: operator/engineer-programmed sequences (Reliable code editor) ↔ pre-engineered standards-aligned sequences (Delta/Metasys G36) ↔ cloud-managed auto-tuning (75F tuners).
- Scope: HVAC-centric core with integration claims (all) vs room-centric comfort bundle (Delta Red5 ROOM/O3: HVAC+lighting+blinds+AV+access in one controller).
- Channel: direct enterprise vs dealer/integrator vs certified-installer SaaS.

## Canonical Abstraction (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (minimal)

A BMS exists when all three hold:

1. **Networked field instrumentation on building plant** — sensors, actuators, and controllers connected to the building's mechanical/electrical systems, carrying measurements in and commands out (two-way).
2. **Automated execution of configured control** — control logic (schedules, setpoints, sequences) configured in the system executes on the plant without a human commanding each action.
3. **Central supervisory monitor-and-command surface** — a shared interface through which an operator observes live state across the equipment and intervenes (change setpoints/schedules, override, start/stop).

Remove #1+#3 → isolated device controls (a thermostat, a timer), not a system. Remove #2 → a monitoring dashboard, not a management/automation system. Remove #3 → embedded controls with no supervisory operation, not a manageable system.

Historical check (§24): the pre-BACnet EMCS era (central console + field panels + time-of-day scheduling + point monitoring/override) satisfies L0 without BACnet, web UIs, graphics, or analytics → L0 is not era-overfit. A single smart thermostat is below the "system" threshold (no networked multi-device plant + no shared supervisory layer). Cloud-native challengers (75F) satisfy L0 with wireless mesh + cloud portal instead of wired buses + workstations → L0 is not deployment-overfit.

### L1 — Common Mature Structure

- **Point/equipment model**: controllers expose named points (inputs/outputs/values); points are organized under equipment (air handlers, chillers, terminal units/VAV, lighting zones, rooms) and sites.
- **Schedules & calendars**: time-of-day/weekly operation; holiday/special-event handling; shared vs equipment-scoped schedules.
- **Alarms/events**: detection of abnormal conditions, annunciation (list/screen/email/mobile), handling workflows; in mature products, fault-detection lists that direct staff.
- **Trends & history**: interval logging of point values, runtime logs, archives; consumed as trend charts and reports.
- **Graphics & dashboards**: equipment schematics and floor plans with live values; site/portfolio dashboards.
- **Integration machinery**: device discovery; multi-protocol integration (BACnet family, Modbus, and others) binding third-party equipment.
- **Engineering/configuration surface**: sequence programming (or pre-engineered sequence libraries), templates/mass deployment, graphics authoring, provisioning/commissioning tools.
- **Access control to the system itself**: user accounts, roles/permissions, audit trails; encrypted communications.
- **Web/mobile operation**: browser-based supervision; mobile apps for staff.
- **Energy/performance reporting**: consumption/performance views built on control data (overlaps Building Energy Management — see boundary).

### L2 — Variant / Optional Structure

- Deployment substrate: on-prem workstation+servers vs enterprise web server vs SaaS/cloud-native.
- Control philosophy: engineer-programmed sequences vs pre-engineered standards-aligned sequences vs cloud-managed auto-tuning/AI optimization.
- System scope: HVAC-only core vs integrated HVAC+lighting (+blinds/AV) vs monitored integration of fire/security/elevators (depth varies; life-safety control is regulated — usually monitoring/integration, sometimes listed smoke control).
- Scale posture: single building vs multi-site portfolio rollup.
- Segment tunings: healthcare/pharma validated environments (audit-grade records), data centers, education campuses, multi-site retail, government.
- Occupant-facing comfort surfaces (tenant/occupant apps).
- Advanced analytics: FDD depth, energy dashboards (interface to Building Energy Management), demand-response participation.
- Room-level bundles: sensor-hub devices combining comfort sensing, HVAC, lighting, and access in one room controller.

### L3 — Vendor-specific (research notes only)

- Metasys: SMP/SCT/Launcher tooling, engine firmware, "65,000 objects per server"/"1,300 devices" claims, release 16.0 specifics, MVE validated-environments package, Fast Track upgrade tool, UL 864 smoke-control listing, EPBD dashboard, "80% of lifecycle costs" marketing stat, G36 "40+ water-side and 64 air-side rules" counts.
- Reliable Controls: MACH-Pro/RC-FLEX product names, RC-Studio/RC-WebView/RC-Archive/RC-Reporter/RC-GrafxSet/RC-Toolkit/RC-RemoteAccess/RC-Passport/myControl, B-AWS BTL listing, full BACnet priority array, Simulate Mode, IPv6 support, Windows workstation requirements.
- Delta Controls: Red5 (PLUS/EDGE/FIELD/ROOM/VAV), O3 hub, eZNT/eZNS, enteliWEB/enteliCLOUD/enteliVIZ/enteliVAULT/Canvas, GCL, Node-RED/Python, UDMI collaboration with Google, Earthright dashboard, BACnet/SC emphasis.
- 75F: CCU/SmartNode/HyperStat/Mystat/HelioNode names, Facilisight, PAM, Easy Street, Tuners, occupant app, deadband mode naming, zone-vs-shared schedule concepts, Certified Installer program.

## Rejected Findings

- **"BMS = BACnet system"** — rejected. BACnet is the current dominant standard but 75F is cloud-native, historic systems predate BACnet, and Delta also carries Modbus/DALI/EnOcean. Protocol is implementation, not definition.
- **"BMS includes access control/security"** — rejected as definitional. Integration with security systems is common (all four claim integration), but Reliable lists access controllers as a separate "Security Series," Delta presents Access Controls as its own system, and the atlas has a separate Building Access & Visitor Management Type. Integration posture, not core.
- **"BMS = energy analytics platform"** — rejected. Energy/performance reporting is a common layer built on control data; the managing-the-consumption-data center is Building Energy Management (processed sibling records the seam: "control/optimization posture … blurs to BMS").
- **"BMS includes maintenance work orders"** — rejected. No sampled product's center is a work-order/PM loop; that is CMMS/Building Maintenance Management territory.
- **"A cloud thermostat/occupant app is a BMS"** — rejected. Below the "system" threshold of L0 (no networked multi-system plant + shared supervision). 75F qualifies as a BMS because of its multi-device control network + supervisory portal, not because of the thermostat.
- **"BMS = dashboard platform"** — rejected. Dashboards are surfaces; the control loop over field devices is the core.

## Boundary Findings

- **vs SCADA / DCS / HMI (§16 industrial)**: the same supervisory-control grammar (field devices + automated control + operator stations + alarms + trends). The discriminator is the managed world: building plant (HVAC, lighting, sanitary, vertical transport) with comfort/energy goals, building operators, building protocols — vs industrial production processes. If the domain shifts to factory processes → SCADA/DCS; machine-level interfaces → HMI. Held by domain, not by structure. (Worth recording: when the SCADA leaf is processed, the two should be jointly reviewed for a family statement.)
- **vs Building Energy Management (§17, processed)**: BEM treats energy consumption as managed data (bills, meters, baselines, benchmarking, M&V); BMS commands the plant. Seam: add control loops → BMS; remove control and center consumption analytics → BEM. They interconnect (BMS trend data feeds energy analytics; energy targets set back into schedules/setpoints). Consistent with the processed sibling's L2 note.
- **vs Building Access & Visitor Management (§17, processed)**: plant vs people (recorded there as "Remove people → BMS; remove plant → this Type"). Consistent.
- **vs Building Asset Management (§17, processed)**: durable asset register + lifecycle/renewal economics vs live control loop (recorded there as "different layer"). Consistent.
- **vs Building Commissioning Platform (§17, processed)**: verification records vs control loops (recorded there as "add control loops → BMS"). Consistent. Field commissioning tools (75F installer tables, NFC provisioning) are deployment aids inside the BMS, not the Cx record system.
- **vs Building Maintenance Management (§17 sibling, unprocessed)**: BMS executes and records what the plant does; maintenance management governs the care loop (work orders, PM programs). Add work-order lifecycle → maintenance system. Note for joint review when that sibling is processed.
- **vs Facility Management System / IWMS (§17 siblings, unprocessed)**: FM/IWMS is the business layer (space, leases, service, portfolio); BMS is the OT control layer beneath it. Integration common; loop differs (business operations vs physical plant control).
- **vs Air Quality Monitoring (§21, processed)**: observes air vs controls equipment (recorded there). IAQ sensors inside a BMS feed ventilation control — integration, not identity.
- **vs Digital Twin Platform**: digital-twin features (Delta Canvas) appear inside BMS ecosystems as optional overlays; the twin Type centers on model/asset representation, not live plant command.

## Uncertainties

- No Tier-1 operator manual was retrievable for Metasys (docs portal is a JS application); JCI evidence is product-page level, and all JCI numeric statements are vendor claims kept in L3, not asserted in the final document.
- 75F article-level pages return 403; the cloud-side model is documented at category/surface level only.
- Schneider EcoStruxure Building Operation, Tridium Niagara, Distech, Siemens Desigo CC unreachable; the "enterprise integration hub / middleware" philosophy is therefore covered only indirectly (via the observed samples' integration machinery). No claims made for the unreachable vendors.
- Life-safety/fire integration depth (monitor-only vs listed smoke control) varies by region and regulation; treated qualitatively.
- The exact split between "cloud-native smart-building platform" and "BMS" in the challenger segment may continue to blur; L0 threshold (networked plant + automated control + supervisory layer) held for this sample.
- Terminology: "BMS" (global), "BAS" (North America), historically "EMCS"; treated as one Type with naming variance (evidence: JCI self-describes as BAS while the market category name here is BMS; Delta uses "Building Management"; Reliable uses "building control/BAS").

## Final Synthesis

A Building Management System is the operational control layer of a building: a network of field devices (sensors, actuators, controllers) attached to the building's mechanical and electrical plant, control logic (schedules, setpoints, sequences) configured into the system and executed automatically on that plant, and a shared supervisory surface through which facility staff observe live equipment state and intervene. Around that core, mature products organize points under equipment, run alarm/event machinery, log trends and runtimes, render graphics and dashboards, integrate third-party equipment over standard protocols, provide engineering tooling (sequence programming or pre-engineered libraries, templates, discovery, provisioning), gate the system with roles and audit, operate from web and mobile, and report on energy/performance. Deployment ranges from on-prem workstations and servers to cloud-native SaaS; control philosophy ranges from engineer-programmed to pre-engineered to cloud-tuned; scope ranges from HVAC-only to integrated room-level bundles and portfolio rollups. The Type's identity is held by the control loop over networked building plant plus the supervisory surface — not by protocol, deployment, or analytics, which are implementation choices.
