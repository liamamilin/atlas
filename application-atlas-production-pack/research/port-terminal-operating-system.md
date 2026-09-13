# Research Notes — Port Terminal Operating System

## Research Goal

Understand what a Port Terminal Operating System (TOS) actually is from real products: the objects it manages, the workflows it executes, the roles that use it, the rules that govern it, and where its boundary lies against neighboring Types (YMS, WMS, TMS, vessel/fleet platforms, marina systems, port-authority systems).

## Initial Boundary

Working hypothesis before research:

- A TOS is the terminal operator's execution system for a marine terminal: vessel calls (berth, stowage), yard stacking, gate transactions, equipment dispatch, billing of shipping lines.
- Nearest neighbors: Yard Management System (trailer yard at a DC), Warehouse Management System, Transportation Management System, Marine Fleet Management / Vessel Operations Platform (ship-side), Marina Management (recreational berthing), port-authority / port community systems (port level, multi-party).
- Pre-hung flags from earlier passes:
  - yard-management-system pass: "cross-mode analog boundary recorded (berth/crane/vessel-call machinery vs trailer yard at a DC; convergence at intermodal container yards — kaleris sells both TOS and YMS)" — this pass must ratify from the TOS side.
  - marina-management pass: "vs port-terminal-operating-system (cargo vs recreational)" — consistent, no conflict.

## Research Questions

1. What are the core objects: vessel call, berth, cargo unit, yard block/stack, move, gate transaction, rail front?
2. How does a vessel call flow: berth allocation → discharge/load plan → crane sequencing → yard positioning → completion?
3. How is the yard modeled (blocks/stacks/rows; cargo heaps; warehouses) and how does it differ by cargo type?
4. How does the landside work: gate transactions, truck time slots, rail fronts?
5. What data exchange exists with shipping lines, customs, port community systems?
6. What is billing's role (tariffs, storage, lifting charges) — definitional or adjacent?
7. What roles use the system (vessel planner, yard planner, gate clerk, equipment driver, finance)?
8. What variants exist: container vs bulk vs RoRo vs mixed; small vs mega; on-prem vs cloud; marine vs inland depot?
9. Where exactly is the TOS/YMS/WMS boundary, and does the same vendor draw it?
10. Would older / regional / non-software terminal operations still fit the definition?

## Representative Products

Selected for market coverage, documentation access, different product philosophies and customer tiers:

1. **Kaleris N4 (Navis N4)** — global market leader for container terminals (vendor claims 350+ sites, 90+ countries); deep optimization and automation stack. Tier: mega/large terminals.
2. **Kaleris Octopi (cloud-based TOS)** — SaaS TOS for small/mid-sized container and mixed-cargo terminals and inland depots; replaces "pen and paper, spreadsheets, and legacy TOS systems". Tier: small/mid. (Same vendor family as N4 but a distinct product philosophy; used together with N4 pages as one vendor family.)
3. **Kaleris Master Terminal (Jade Master Terminal)** — mixed/general-cargo TOS (bulk, break-bulk, RoRo, railcars, warehouse goods); cargo granularity by type/subtype, billable events in CBM/revenue tons. (Same vendor family; included for the multi-cargo pole.)
4. **Solvo.TOS** — independent Russian vendor; multi-cargo (marine container, general, bulk, RoRo, river, inland/dry port, multipurpose logistics centers); explicit "What is a TOS?" section with three key functions. Tier: regional multi-cargo.
5. **Tideworks Mainsail** — independent US vendor (Carrix/SSA-affiliated, Blackstone-backed); marine TOS for container/RoRo/general cargo; separate rail TOS product (Intermodal Pro); separate billing engine. Tier: mid-size marine terminals, Americas.
6. **CyberLogitec OPUS Terminal / OPUS Terminal M** — independent Korean vendor; container TOS and cloud multipurpose TOS; berth/vessel/yard/gate in one platform; billing sold as a separate product (TABS). Tier: Asia/global challenger.

## Sources

Research date: 2026-09-09. All sources fetched live.

- Kaleris — https://kaleris.com/ (root; TOS positioned as "global leader in terminal operating systems")
- Kaleris — https://kaleris.com/solutions/terminal-operating-system/ (TOS family page: N4 / General Cargo / SaaS TOS; "the berth, the yard, and the gate")
- Kaleris — https://kaleris.com/what-is-a-terminal-operating-system/ (definitional article; N4, Master Terminal, Octopi descriptions; user roles; integration targets)
- Kaleris — https://kaleris.com/solutions/terminal-operating-system/container-terminals/ (N4 optimization modules: Expert Decking, PrimeRoute, Vessel Autostow, RTG Optimization, VMT, Control Room; LBCT automation quote)
- Kaleris — https://kaleris.com/solutions/terminal-operating-system/cloud-based-tos/ (Octopi: berth/vessel/yard planning, EDI EDIFACT+ANSI X12, automatic invoicing, container stacks/cargo heaps/warehouses)
- Solvo — https://www.solvo.ru/en/ (root; product family: TOS / WMS / YMS / TMS as separate products)
- Solvo — https://www.solvo.ru/products/solvo-tos/ (Solvo.TOS product page; "Что такое TOS?" three key functions; fronts: quay/rail/road/internal zones; EDIFACT/XLS/XML; billing and KPI as technology pages)
- Tideworks — https://tideworks.com/ (root; Mainsail/Spinnaker/Forecast marine, Intermodal Pro rail, Traffic Control, Terminal View)
- Tideworks — https://tideworks.com/mainsail/ (Mainsail definition: "manage cargo, inventory, vessel activity, and gate operations from a single platform"; separate billing engine)
- Tideworks — https://tideworks.com/faq/ (integration targets: gate/quay OCR, position detection, PCS, gate technologies, ERP)
- CyberLogitec — https://www.cyberlogitec.com/ (root; OPUS Terminal, OPUS Terminal M, OPUS DigiPort, TABS; press releases: Shuwaikh, Incheon IGCT, TTI Algeciras — "manages berth, vessel, yard, and gate operations within a single unified platform"; "interface with automated equipment control systems")

Access notes / limitations:

- getoctopi.com (Octopi's own site) unreachable (2 attempts, empty responses) — Octopi evidence taken from Kaleris's cloud-based-TOS and what-is-a-TOS pages instead.
- solvo.com unreachable (transport error) — solvo.ru used (Russian-language; quotes translated).
- No vendor's in-product help center / user manual was reachable in this pass (Kaleris docs portal, Tideworks support portal, CyberLogitec support are login-gated). Evidence is from official product/marketing/FAQ pages — Tier 1–2. Precise operational parameters (exact EDI message names, numeric limits, state-machine labels, tariff structures) were NOT observed and are NOT claimed.
- Specific UN/EDIFACT message types (e.g., COPRAR/CODECO-class) were not observed in fetched pages; only "EDIFACT / ANSI X12" families are claimed.

## Product Observations

### Kaleris N4 (container terminals) — evidence layer A

- TOS family page: "Our digital platform automates the parts of your terminal that you care about most, regardless of the size or scale of your operation – the berth, the yard, and the gate." Benefits list: "Keep a bead on terminal inventory; Track vessel moments in real-time; Improve yard utilization; Reduce demurrage and detention rates (including containers, trucks, rail, and cranes); Improve planning and decision-making support for vessel visits."
- N4 positioned for container terminals: "The leading terminal operating system on the market. Trusted by the world's largest operators." Claims: 350+ customers in 92+ countries; scalable "up to 12m TEUs of a single site"; "Prevent Revenue Drain: Capture all billable events and invoices with N4 billing"; "Robust EDI and API Integration: Handles all major EDI for container cargo".
- Optimization modules (all named as N4 modules):
  - **Expert Decking** — "automates yard planning by distributing containers throughout the yard based on pre-defined business rules."
  - **PrimeRoute** — "optimal, real-time routing, dispatching and monitoring of straddle carriers, terminal tractors and other internal transportation vehicles within the container terminal."
  - **Vessel Autostow** — "automatically generates stowage plans for the entire ship or by specific bay based on rules set by the ship planner in compliance with the vessel planning stowage strategy."
  - **RTG Optimization / RTG Automation** — optimizes yard crane job decisions; automation for advanced terminals.
  - **VMT** (Vehicle Mounted Terminal) — "the next-generation console for RTG and RMG drivers… enables them to easily complete jobs."
  - **Control Room** — "centralizes views and functions critical to monitoring and maintaining operations. It allows operators to visualize where containers, cranes, and trucks are in the yard."
- Automation: "N4 extends the TOS to coordinate, optimize, and execute automated terminal operations across yard, transport, quay, and gate. It connects planning with real-time equipment execution through ECS integration." LBCT case: "N4 serves as the brains of the automated operations… controlling when the container is supposed to move, which piece of equipment is going to move it and where it's going."
- Roles implied: ship planner, yard planners, dispatchers, crane/RTG drivers, control room operators.

### Kaleris Octopi (cloud SaaS TOS) — evidence layer A

- "a modern and affordable software-as-a-service (SaaS) terminal operating system designed for small and medium-sized container and mixed cargo terminals — replacing pen and paper, spreadsheets, and legacy TOS systems."
- Who it serves: small/mid terminals (bulk, break bulk, project cargo), RORO/intermodal terminals, inland container depots.
- Feature set: Containers ("Keep track of every container that passes through your terminal"); General Cargo; Real-Time KPIs (dashboard); EDI ("supports both EDIFACT and ANSI X12 messages… carrier-terminal data exchange"); **Berth, Vessel & Yard Planning** ("Digitize and customize berth requests and approval processes to visualize your berth utilization… Easily configure and manage container stacks, cargo heaps, or warehouses"); **Automatic Invoicing** ("generate a voyage invoice in just one click… configure your tariffs and automatically generate invoices for your customers in real-time as you provide them with services").
- From the what-is-a-TOS page: "Octopi is web based, and can be used as a web portal for the community"; "70-80% pre-configured application with standard workflows… designed based on the operations of small-medium terminals/depots using pen/paper or old inhouse systems"; remote onboarding "in 4-6 months".

### Kaleris Master Terminal (mixed/general cargo) — evidence layer A

- "TOS specifically designed for mixed cargo terminals, as well as containers, bulk, break bulk, and project cargo, automobiles, trucks, semi-trailer trucks, trailers, and railroad cars."
- "Real-Time Cargo Visibility… Cargo movements are recorded in real time… inventory visibility and better yard utilization, mobile & vehicle apps, as well as a webportal."
- "Minimize Revenue Leakage: Capture all billable events (CBM, FRT/Revenue Tons etc), manage contracts and invoices… with in-built billing options."
- "Cargo Granularity: Cargo can be individually tracked via types and subtypes making it easy to serve a variety of customer contracts, even for the same products/goods that may have different handling rules."
- "Customizable Workflows: Add tasks that are specific to your product or operation, enabling granular billing for additional services (such as a task for weighing of cargo, or applying labels)."
- "Robust EDI Integration: Handles all major EDI for container cargo as well as definable file formats to drive standardization for mixed cargo."
- "Value Added Services: Allows terminals to generate new revenue streams via VAS (blending, bagging, aggregating, CFS etc)."

### Solvo.TOS — evidence layer A

- Definition: "TOS (Terminal Operating System) – это программный продукт, который комплексно автоматизирует все операции и бизнес-процессы перевалочного комплекса: порта или сухого терминала." (A software product that comprehensively automates all operations and business processes of a transshipment complex: a port or dry terminal.)
- **Three key functions of a TOS** (vendor's own articulation):
  1. **Production** — "Fixes in real time information about all movements of cargo and transport. Plans and coordinates operational processes — work of handling equipment, vessel calls, railway operations, truck visits. Manages terminal resources: personnel, equipment and transport."
  2. **Documentary** — "Exchanges data with clients, shipping lines, customs authorities and other supply chain participants. Receives, decodes and processes documents and forms electronic messages."
  3. **Record-keeping** — "Processes and stores information on cargo, transport, clients across dozens of parameters and attributes. Provides configurable external and internal reporting forms."
- Terminal types served: marine container, general cargo, bulk, RoRo/passenger cars, river terminals, multipurpose transshipment complexes, inland terminals (dry ports).
- Production areas ("fronts"):
  - **Quay line**: berth planning, vessel call processing, cargo handling (load/discharge) planning, cargo planning, "automated data exchange with counterparties in EDIFACT, XLS, XML formats."
  - **Railway**: train handling planning, double operations, empty-platform loading calculation, document flow with Russian Railways' "ETRAN" system.
  - **Road transport**: "management of transport flows through time-slotting, access control, forming cargo batches for truck pickup, routing of vehicles on the terminal."
  - **Internal zones**: "management of operations in each area of the terminal: storage zones, inspection, stuffing/de-stuffing, reefer zone, repair area, empty container depot; management of handling equipment and optimization of its routes."
- Cargo types: marine containers, bulk (насыпные/навалочные), general cargo, RoRo and passenger cars.
- Core system components: "Terminal topology; processing of all cargo and transport types by fronts; workstations for operational staff and on-site staff; role-based access configuration; integration with external systems."
- Application modules: "gate in/out zone management; berth and equipment reservation for vessel calls; working with weighbridges, empty containers and repair operations; analytical reporting; web portal; STS crane operator workstation; surveyor application for the vehicle yard."
- Separate technology pages: KPI for ports; Billing for ports. Solvo also sells Solvo.WMS (warehouse), Solvo.YMS ("управление грузовым двором складского комплекса" — truck yard of a warehouse complex), Solvo.TMS as separate products — vendor-drawn TOS/YMS/WMS boundary.
- Claims >45% of Russia's marine container turnover handled on Solvo.TOS; 50+ projects.

### Tideworks Mainsail — evidence layer A

- Definition: "Mainsail is a terminal operating system (TOS) that helps marine terminals manage cargo, inventory, vessel activity, and gate operations from a single platform. Designed for container, RoRo, and general cargo, Mainsail provides real-time visibility, streamlined workflows, and integration with terminal technologies and business systems."
- Root page: "For marine terminals, coordinate vessel, yard, and gate operations with greater precision."
- Mainsail 10 enhancements: comprehensive inventory control ("active inventory control"), interactive search tools, advanced reporting, third-party integrations, customized UX, optimized response times.
- Billing: "By creating a proprietary billing engine separate from the TOS, Tideworks can now establish centralized management of billing contracts of rates, tariffs, invoicing, etc. to expand billing capabilities from the terminal to the corporate level." — billing is part of the offer but architecturally separable.
- FAQ — integration targets: "Back-office systems; ERP and accounting packages; Gate and quay OCR; Position Detection Systems; Business intelligence (BI) tools; Port Community Systems; Gate technologies (kiosks, scales, RFID and more)." Partners include Camco (gate OCR), ABB, Identec Solutions, Liebherr.
- Rail: separate product **Intermodal Pro** ("Advanced rail TOS… coordinate rail, yard, and gate operations") — the same vendor draws a marine/rail TOS product line split.
- Also ships Traffic Control (equipment control) and Terminal View (3D digital-twin visualization) as companion products.
- Scale: "powering 100+ marine and intermodal terminals."

### CyberLogitec OPUS Terminal / OPUS Terminal M — evidence layer A

- OPUS Terminal: "Container Terminal Operation and Decision Support System… enables the container terminal's operations including loading and unloading, classification and storage."
- OPUS Terminal M: "an advanced terminal operating system for multipurpose terminals (Container, General Cargo, RORO, etc.)… applicable for the container, RORO and Bulk… various types of cargo in a single system." Cloud-based (AWS); article documents one cloud server operating five terminals across Indonesian islands; interface protocols RESTful/SOAP/MQ/FTP; "Private EDI" processing; external inventory integrated as "Virtual Terminal".
- Incheon IGCT press release: "a TOS based on OPUS Terminal that manages berth, vessel, yard, and gate operations within a single unified platform. The system will interface with automated equipment control systems to support operational planning and field execution."
- Shuwaikh press release: "supports vessel operations, planning, yard and equipment management, gate operations, operational monitoring, and data management."
- Billing: separate product **TABS** ("Total Advanced Billing System… automated billing tasks for terminals") — packaging evidence that billing is adjacent, not definitional.
- Digital twin: separate product **OPUS DigiPort**. Article: "Conventional TOS (Terminal Operating Systems) include optimization logic, but these are based on fixed rules…" — TOS framed as the core system that AI add-ons augment.

## Cross-product Comparison

| Aspect | N4 (Kaleris) | Octopi (Kaleris) | Master Terminal (Kaleris) | Solvo.TOS | Mainsail (Tideworks) | OPUS Terminal (CLT) |
|---|---|---|---|---|---|---|
| Cargo scope | container (some general) | container + mixed + inland depots | mixed: bulk/break-bulk/RoRo/railcars | container/general/bulk/RoRo/river/inland | container/RoRo/general | container; M variant: container/RoRo/bulk |
| Vessel call machinery | berth/yard/gate; Vessel Autostow stowage plans | berth requests/approval, vessel planning | vessel visits | berth planning, vessel call processing | vessel activity | berth, vessel operations |
| Yard model | Expert Decking distributes containers by rules; Control Room shows containers/cranes/trucks in yard | container stacks, cargo heaps, warehouses | cargo tracked by type/subtype | terminal topology; storage/inspection/stuffing/reefer/repair/empty-depot zones | active inventory control | yard management |
| Move execution | PrimeRoute dispatch of straddles/tractors; RTG Optimization; VMT driver console | (lighter; workflows) | customizable task workflows | equipment management + route optimization | workflows | equipment management; ECS interface for automation |
| Gate | gate in berth/yard/gate triad | (implied) | (implied) | time-slotting, access control, gate in/out zone module | gate operations | gate operations |
| Rail | (inland depots via family) | inland container depots | railroad cars | rail front + ETRAN integration | separate rail TOS (Intermodal Pro) | — |
| EDI | "all major EDI for container cargo" | EDIFACT + ANSI X12 | major EDI + definable formats | EDIFACT, XLS, XML | third-party integration incl. PCS | RESTful/SOAP/MQ/FTP, Private EDI |
| Billing | N4 billing ("capture all billable events") | automatic invoicing from tariffs; voyage invoice | billable events (CBM, revenue tons), contracts, invoices | separate billing technology page | separate billing engine (terminal→corporate) | separate product (TABS) |
| KPI/reporting | optimization insights | real-time KPI dashboard | KPIs | KPI for ports page | advanced reporting | operational monitoring |
| Automation | ECS integration; ASC/AGV/auto-truck; "brains" of automated terminal | — | — | digital twin / remote crane control as advanced path | automation support; Traffic Control companion | ECS interface; DigiPort digital twin |
| Deployment | on-prem + cloud (N4 4.0) | SaaS | (family) | on-prem/license | cloud platform | cloud (AWS) / on-prem |

**Cross-product commonalities (evidence layer B):**

1. Every product organizes the terminal around **vessel calls** (berth + ship stay + load/discharge plan). Wording varies: "vessel visits" (Kaleris), "судозаходы" (Solvo), "vessel activity" (Tideworks), "berth, vessel" (CyberLogitec).
2. Every product maintains a **positioned cargo inventory inside the terminal's own geography** — containers in stacks/blocks, general cargo by type/subtype, bulk as measured quantities; zones include storage, reefer, inspection, empty depot, repair.
3. Every product **plans work and dispatches it to equipment/labor, then records what happened** — from PrimeRoute/RTG dispatch and VMT consoles (N4) to Solvo's "fixes in real time information about all movements" and equipment route optimization, to Mainsail workflows.
4. Every product covers the **gate / landside interface** (truck gate, time slots, access control) — explicit at Solvo, Tideworks, CyberLogitec, Kaleris ("the berth, the yard, and the gate").
5. Every product exchanges **electronic messages with shipping lines and authorities** (EDI: EDIFACT/ANSI X12/definable formats; documentary function at Solvo).
6. Every product **bills for terminal services** (tariffs, billable events, invoices) — though two vendors ship billing as a separate product/engine (Tideworks billing engine, CyberLogitec TABS), showing it is adjacent rather than definitional.
7. Every product offers **KPI / reporting / operational monitoring**.
8. Role structure recurs: vessel/ship planner, yard planner/controller, gate clerk, equipment driver (VMT), finance/billing, management dashboards, customer portal.

**Vendor-drawn boundaries (evidence layer A):**

- Solvo sells TOS, WMS, YMS, TMS as four separate products; its YMS is explicitly "the truck yard of a warehouse complex" — the vendor itself separates port/terminal systems from warehouse and DC-yard systems.
- Tideworks sells marine TOS (Mainsail) and rail TOS (Intermodal Pro) as separate product lines — mode-specific product split within one TOS concept.
- Kaleris sells TOS, YMS, TMS, CVS (carrier & vessel) as separate solution lines — the ship-side (carrier/vessel) is a different product family from the terminal-side (TOS).
- CyberLogitec sells billing (TABS) and digital twin (DigiPort) beside the TOS.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

Three jointly-held structures:

1. **The vessel call as the terminal's unit of production.** The terminal's work is organized around a vessel's visit: berth allocation, the ship's stay window, and the load/discharge (stowage) plan that determines which cargo moves between ship and quay. Remove it → berth-booking/traffic tool or generic yard system; the terminal's shipside production rhythm disappears.
2. **The cargo lot tracked through the terminal's own geography.** Each cargo unit (an identified container; a typed/measured cargo lot for break-bulk, bulk, RoRo units) is individually recorded and positioned within the terminal's spatial model — quay, yard blocks/stacks/rows, warehouses, specialized zones (reefer, inspection, empty depot, repair), gate, rail front — from landside receipt to shipside loading or vice versa. Remove it → shipment tracking with no facility, or a berth scheduler with no cargo memory.
3. **The planned-and-confirmed move as the work primitive.** Transfer work is decomposed into individual moves (quay-crane lift, yard transfer, gate transaction), planned in advance, dispatched to equipment and labor, and confirmed back so the system's record converges with physical reality in real time. Remove it → a static plan + inventory system; the "operating" in TOS dies.

Jointly-held load-bearing analysis:

- 1 alone = berth scheduling / vessel-traffic tool (port-authority territory)
- 2 alone = yard inventory system (WMS/YMS territory)
- 3 alone = generic task dispatch
- 1+2 without 3 = plan + inventory with no execution loop
- 1+3 without 2 = crane operations with no yard memory
- 2+3 without 1 = trailer-yard / warehouse territory (YMS/WMS)

### L1 — Common Mature Structure

- Gate operations: truck gate-in/gate-out transactions, access control, truck time-slotting/appointments.
- Rail front: train handling where the terminal interchanges with rail (Solvo includes it in-product; Tideworks ships a dedicated rail TOS; Kaleris serves inland depots).
- EDI exchange with shipping lines and authorities (EDIFACT / ANSI X12 families; documentary function).
- Billing of shipping lines/carriers/consignees: tariffs, billable events (lifts, storage, CBM/revenue tons), invoices — sometimes a separate product/engine.
- KPI dashboards and operational reporting.
- Role-based workstations: vessel planner, yard planner/controller, gate clerk, equipment driver console, finance, management, customer web portal.
- Equipment and resource management: cranes, yard equipment, terminal tractors, labor shifts.

### L2 — Variant / Optional Structure

- Automation integration: equipment control systems (ECS), automated stacking cranes, AGVs/autotrucks, remote crane operation, digital twins.
- Optimization modules: autostow, automated yard decking, RTG dispatch optimization, truck scheduling.
- OCR / position detection / RFID / weighbridge integrations.
- Cargo-type specialization: container vs bulk (measured quantities) vs RoRo vs mixed; multipurpose single-system vs mode-specific products.
- Deployment: on-prem vs cloud SaaS; single terminal vs multi-terminal/multi-site (one cloud server, several terminals; "virtual terminal" for external inventory).
- Customs/security integrations and port community system connectivity.
- Inland/dry-port deployment of the same product family (train/truck fronts replace the vessel call).
- Value-added services (stuffing/destuffing, blending, bagging, CFS).

### L3 — Vendor-specific (research notes only)

- N4: Expert Decking, PrimeRoute, Vessel Autostow, RTG Optimization/Automation, VMT, Control Room; groovy-language extensibility; "scalable up to 12m TEUs of a single site"; 350+ sites claim; N4 4.0 cloud.
- Octopi: 70–80% preconfigured; 4–6 month remote onboarding; in-house EDI experts; community web portal.
- Master Terminal: RTLS real-time cargo visibility; billable-event capture in CBM/FRT/revenue tons; VAS module set.
- Solvo: ETRAN (Russian Railways) document integration; STS crane operator workstation; surveyor app; ГОСТ-era standardization context; >45% Russian container turnover claim.
- Tideworks: Spinnaker, Forecast, Traffic Control, Terminal View (3D digital twin); corporate-level billing engine; partner stack (Camco, ABB, Identec, Liebherr).
- CyberLogitec: TABS billing; OPUS DigiPort digital twin; AWS multi-terminal cloud (Indonesia); RESTful/SOAP/MQ/FTP interface set; "Private EDI"; Virtual Terminal for external inventory.

## Historical / Market-Sample Check

Paper-era terminal operations satisfy the three L0 legs without any modern machinery:

- vessel call as unit of production: berth allocation board + ship's stowage/bay plan + hatch sequence;
- cargo lot through terminal geography: container/unit numbers on yard/stack plans and tally sheets, warehouse ledgers for general cargo, stockpile records for bulk;
- planned-and-confirmed moves: planned lifts vs tally confirmations; gate tickets; shift handover records.

Older and regional software generations (1990s-generation TOS; regional vendors; Solvo operating since 1995; Tideworks' two-decade customer relationships) fit the same core. EDI, optimization engines, cloud, automation/ECS, digital twins, AI are era-current additions, not definitional. The definition does not depend on containerization alone — general-cargo and bulk terminals satisfy it with measured cargo lots instead of containers.

## Vendor-specific Findings

See L3 above. None of these entered the canonical core.

## Boundary Findings

1. **vs Yard Management System** (pre-hung flag from the yard-management-system pass — ratifying from this side): the TOS's unit of work is the vessel call plus cargo lots moving through a terminal's geography with shipside crane operations; the YMS's unit is the trailer and its moves in a shipper/DC yard, gate-in to gate-out, with no vessel and no shipside. Convergence exists at intermodal container yards: kaleris sells both N4 (TOS) and YMS; Solvo sells TOS and YMS as separate products and defines its YMS as the truck yard of a warehouse complex; Tideworks splits marine TOS (Mainsail) from rail TOS (Intermodal Pro). **Keep both Types.** The shipside anchor (berth + vessel call + quay crane operations) is the discriminator. Inland container depots are served by TOS-family products as a variant where the vessel call leg is replaced by train/truck fronts — recorded as a variant extension, not a redefinition of this port-scoped Type.
2. **vs Warehouse Management System**: a warehouse handles goods inside a building driven by orders (receive, put away, pick, ship); a terminal is a transport interchange driven by vessel calls and transport fronts, where storage is a buffer between carriers, not the point. Solvo sells WMS and TOS as separate products.
3. **vs Transportation Management System**: the TMS plans transport for a shipper/carrier across journeys; the TOS executes cargo transfer inside one facility for the facility's operator. Different party, different unit of work. Solvo and Kaleris sell both as separate lines.
4. **vs Marine Fleet Management / Vessel Operations Platform**: ship-side systems serve the vessel owner's operations (the ship as asset); the TOS serves the terminal operator (the facility as asset). Kaleris separates Carrier & Vessel Solutions from TOS.
5. **vs Ocean Freight Management**: forwarder/carrier shipment business vs terminal execution. Different system of record.
6. **vs Marina Management**: cargo interchange vs recreational berthing (ratified from the marina pass; consistent here — different users, objects, and economics).
7. **vs Dock Scheduling Platform**: dock scheduling plans appointments before arrival at DC docks; berth request/approval exists inside the TOS's vessel-call leg (Octopi digitizes berth requests). Port-authority-level berth planning and port community systems are adjacent multi-party coordination surfaces — Tideworks lists PCS as an *integration target*, i.e., external to the TOS.
8. **Cross-mode analogs**: airport operations platforms and ground-handling systems play analogous roles for air cargo but are distinct Types with different objects (flights, stands, ULDs handled by different systems).

## Uncertainties

- Exact EDI message vocabularies per workflow (load/discharge orders, status messages) were not observed; only the EDIFACT/ANSI X12 families and "definable formats" are claimed.
- Bulk-terminal depth (stockpile management, weighing, ship loading rates) is evidenced only at the marketing-page level (Solvo bulk terminal page exists but was not fetched; Master Terminal mentions bulk billable events). Claims kept moderate.
- Truck appointment mechanics (booking windows, pre-arrival data) only partially evidenced (Solvo time-slotting; Tideworks gate technologies). Kept generic.
- Whether every TOS includes rail fronts in-product is not universal (Tideworks ships a separate rail TOS) — rail held as common-not-definitional.
- State-machine labels for container status (import/export/transshipment) were not directly observed in fetched pages; the container lifecycle is described generically.
- No in-product manuals were reachable; all evidence is from official product pages/FAQ/press. Assertion strength calibrated accordingly.

## Final Synthesis

A Port Terminal Operating System is the terminal operator's execution system of record for a cargo terminal. Its defining core is three jointly-held structures: the vessel call as the unit of terminal production (berth + ship stay + load/discharge plan); the cargo lot individually tracked through the terminal's own geography (quay, yard, specialized zones, gate, rail front); and the planned-and-confirmed move as the work primitive (plan → dispatch → execute → confirm, in real time). Around that core, mature products add gate operations, rail fronts, EDI exchange with lines and authorities, tariff-based billing, KPIs, role-based workstations, and customer portals; variants span cargo types (container/bulk/RoRo/mixed), automation depth, deployment (on-prem/cloud), scale, and inland-depot extensions of the same family. The Type is bounded against YMS/WMS (no vessel call, order- or trailer-driven), TMS (journey planning for shippers/carriers), vessel/fleet platforms (ship-side), marina systems (recreational), and port-authority/PCS surfaces (multi-party coordination, not terminal execution).
