# Research Notes — Yard Management System (YMS)

## Research Goal

Understand what a Yard Management System actually is in the real market: what objects it manages (trailers? the yard itself? dock doors? yard tractors?), how a trailer's visit to a facility flows through the system (gate → yard → dock → gate), how yard-driver work is directed and recorded, and where the boundaries lie with neighboring Types (WMS, TMS, Dock Scheduling Platform, Fleet Management, Port Terminal Operating System). Determine which structures are definitional vs common vs variant.

## Initial Boundary

Initial hypothesis (pre-research): a YMS is the facility-side system of record for the trailer yard — the outdoor/adjacent space between the facility gate and the dock doors — tracking trailers and other movable units as they arrive, wait in parking spots, get spotted at doors, and depart; plus directed work for yard drivers (jockeys/spotters).

Neighboring Types to watch (pre-hung flags to discharge):
- **Warehouse Management System / WMS** (§10, processed 2026-09-08): its pass recorded the seam "trailers/dock doors in the yard vs goods handling inside the building; D365 driver check-in + staging/loading locations are the WMS-side edge — no merge, this pass should ratify."
- **Transportation Management System / TMS** (§10, processed 2026-09-08): its pass recorded seam (8) "dock-scheduling/yard-management = facility-level machinery shipped as TMS modules (Shipwell Dock Scheduling), standalone forms are their own Types."
- **Dock Scheduling Platform** (§10 sibling, unprocessed): appointment/plan layer — boundary must be drawn from this side for that pass to ratify.
- **garage-door-service-management** (§17, processed): name collision on "dock" already resolved vendor-side (ServiceTitan FAQ) — no action required, note only.
- **autonomous-fleet-management** (§18, processed 2026-09-06): its pass wrote "Yard Management System manages yard space, trailer inventory, and dock scheduling as a facility concern; this Type manages the autonomous vehicles performing yard moves."
- **Port Terminal Operating System** (§18, unprocessed): cross-mode analog (seaport berth/yard vs trailer yard).

## Research Questions

1. What is the core object model — yard space, trailer/unit, move, gate event, dock door, appointment?
2. How is the physical yard modeled (spots/rows/lanes, gates, dock doors)?
3. What is the trailer's lifecycle from arrival to departure, and which events bookend it?
4. How is yard-driver (jockey/spotter/shunter) work assigned, executed, confirmed?
5. How does location accuracy get maintained — manual updates, yard checks, RTLS/GPS?
6. What is the relationship to dock scheduling (appointments) — same system, module, or separate Type?
7. What is the relationship to WMS and TMS — module, integration, or "the gap between"?
8. What dwell/detention/demurrage machinery exists?
9. Which roles use the system, on which surfaces?
10. What variants exist: single site vs network, manual vs RTLS, terminal/intermodal vs DC, cold chain, parcel?
11. Historical check: what did yards run on before YMS, and would those forms satisfy the definition?

## Representative Products

| Product | Segment / philosophy | Why sampled | Evidence depth |
|---|---|---|---|
| YardView | Dedicated standalone SaaS YMS since 1998; mid-market-friendly; gate-yard-dock first | Dedicated-vendor pole; longest-running pure-play; rich product + blog + glossary content | Tier-2 (product pages, blog, glossary fetched) |
| kaleris (YMS; PINC lineage) | Enterprise dedicated YMS (since 2004); RTLS/IoT-forward; multi-modal estate (TOS, TMS, rail, MRO) | Enterprise dedicated pole + terminal/intermodal variant; vendor commentary on WMS-module seam | Tier-2 (solution pages, blog fetched) |
| C3 Solutions (C3 Yard) | Dedicated YMS since 2000 (Montreal); sells Dock Scheduling (C3 Reservations) as a sibling product; rule-engine configuration; EU/UK "shunter" terminology | Dedicated pole + first-hand vendor-drawn Dock-vs-Yard boundary (blog); bilingual/EU pole | Tier-2 (product page, boundary blog, FAQ fetched) |
| Module realizations (WMS/TMS-suite yard modules) | yard machinery packaged inside WMS/TMS/suites | Packaging-variant pole; evidenced via vendor commentary (kaleris, YardView, C3 blogs) and the prior TMS pass (Shipwell Dock Scheduling module) | Indirect (Tier-3 vendor commentary; no suite help-center reached) |

Attempted but unreachable (Source-access Limitation):
- Oracle WMS Cloud Yard Management docs — docs.oracle.com online help is a JS shell; yard-specific page 404/redirect (×2). Only the WMS↔TM integration-guide listing was confirmed on the reachable Get Started page.
- SAP Yard Logistics — help.sap.com returns a JS shell (per the WMS pass's experience; not retried this pass).
- Manhattan Associates — manh.com 403 (per WMS pass).
- PINC legacy site — merged into kaleris.

Consequence: no Tier-1 operational help-center for any sampled YMS was reachable. All observations below come from vendor product/solution documentation and vendor blogs (Tier-2) — operational in character (feature/FAQ/glossary) but marketing-hosted. Assertion strengths are calibrated accordingly; no precise numeric limits, time windows, or defaults are carried into the final document beyond what vendors publish as definitions, and those are attributed.

## Sources

Fetched 2026-09-08:

YardView (yardview.com, Tier-2):
- Homepage — https://www.yardview.com/
- YMS platform overview — https://www.yardview.com/features
- "What Is a Yard Management System? Benefits, Features, and Why It Matters" (blog) — https://www.yardview.com/post/history-of-yms (URL slug historical; article is the what-is explainer)
- Yard Management Glossary A–Z — https://www.yardview.com/yard-management-glossary

kaleris (kaleris.com, Tier-2):
- Homepage — https://kaleris.com/
- Yard Management Solutions — https://kaleris.com/solutions/yard-management/
- "Why a Purpose-Built YMS Outperforms WMS Yard Modules" (blog, 2026-05-28) — https://kaleris.com/why-a-purpose-built-yms-outperforms-wms/

C3 Solutions (c3solutions.com, Tier-2):
- Homepage — https://www.c3solutions.com/
- C3 Yard product page — https://www.c3solutions.com/yard-management/
- "Dock Scheduling vs. Yard Management: What You Actually Need at Scale" (blog, 2026-09-02) — https://www.c3solutions.com/blog-c3/dock-scheduling-vs-yard-management/

Oracle (docs.oracle.com, Tier-1 partial):
- Oracle Warehouse Management Get Started (reachable; confirms WMS↔TM integration guide listing) — https://docs.oracle.com/en/cloud/saas/warehouse-management/ (yard-specific docs unreachable)

Prior-pass evidence reused (recorded in STATUS.md, first-hand from those passes):
- TMS pass: yard/dock machinery shipped as TMS modules (Shipwell Dock Scheduling).
- WMS pass: D365 driver check-in + staging/loading locations as the WMS-side edge.

## Product A — YardView (dedicated SaaS YMS)

### Key observations (A = direct observation of this product)

- **Definition published by vendor (A):** "Yard management is the process of overseeing and coordinating the movement of trucks, trailers, and inventory between your gate and your dock doors, including tracking all activity within the yard." YMS = "software designed to manage trailers, containers, trucks, and equipment within a facility's yard."
- **Three-zone framing (A):** the product organizes everything as At the Gate (entry/security/check-in), At the Dock (flow/throughput/door assignment), In the Yard (visibility/tasking/asset tracking). Repeated across homepage, features page, and blog.
- **Gate (A):** digital check-in/check-out; manned or unmanned gate; kiosks, QR codes, AI-enabled cameras; "capture every detail to ensure security and eliminate driver back-ups."
- **Yard visibility (A):** "live view of all trailers, containers, dock doors, and yard locations"; "digital twin" yard map, drag-and-drop console; per-asset data points; "eliminating manual lot walks."
- **Driver tasking (A):** tasks sent directly to drivers' in-cab tablets; prioritized move lists; Accept → Start → Finish workflows; "eliminating radio dispatching."
- **Dock (A):** dock management + appointment scheduling; carrier self-scheduling; dock capacity planning; dwell-time tracking; door availability matched to trailer readiness.
- **Six "core features" as marketed (A):** dock mgmt/appointments; real-time visibility; gate & access control; driver communication & tasking; reporting & analytics (dwell time, dock utilization, trailer movement); integration/automation with WMS/TMS.
- **Four-phase lifecycle as marketed (A):** gate check-in & receiving → truck assignment & yard slotting → dock scheduling & door assignment → inbound processing, outbound release & warehouse handoff.
- **Detention & demurrage module (A):** tracks dwell in real time; alerts before fees accumulate; "documented timestamps for every gate and dock event"; detention = fee when a trailer is held beyond agreed time; demurrage = fee when freight sits at port/rail terminal beyond allowed time (glossary).
- **Security/compliance extras (A):** blind seal verification (verify seal before release); yard audits/lot checks digitized; automated safety/inspection prompts attached to move tasks; timestamped logs positioned as audit evidence.
- **WMS/TMS seam, vendor-articulated (A):** "WMS focuses on inventory, picking, and storage inside the warehouse. TMS plans and executes shipments to and from the facility. YMS coordinates all activities between the gate and dock. A YMS fills the operational gap that exists between warehouse and transportation systems." Also: "Some organizations attempt to manage yard operations using WMS or TMS extensions… 'free' yard tool bundled with their WMS."
- **Pre-history named by vendor (A):** "spreadsheets, phone calls, or paper logs"; "clipboards, whiteboards, spreadsheets, and legacy systems."
- **Glossary vocabulary (A):** gate management; dwell time ("total time a trailer spends in the yard or at a dock door"); turn time ("time between trailer arrival and departure"); trailer spotting; yard spotter; jockey ("a yard driver or tractor used to move trailers within the yard"); yard check / lot check ("a count or scan of trailers and equipment in the yard"); commitment ("the number of trailers a carrier agrees to maintain in your yard" — trailer pooling); chassis; container; reefer; digital twin; smart yard. (Note: the glossary's definitions for "blind seal verification" and "bobtail" appear swapped/corrupted on the page — not relied upon.)

## Product B — kaleris YMS (enterprise dedicated, ex-PINC)

### Key observations

- **Definition by capability set (A):** features list = Gate Management ("configure and manage the check-in/check-out process of assets"), Asset Management ("access and manage assets inventory, asset details, custom filters"), Dock Management ("configure and manage dock doors and their operational processes"), Exception Management, KPI Benchmarking, Configuration Management, Yard Analytics.
- **Asset record semantics (A):** "asset inventory + location; asset status + dwell in life cycle; time + date stamp all events; visibility in multiple locations; KPIs, dashboards, reports." Dwell is a property of the asset lifecycle.
- **Gate scope (A):** "gate velocity… check-in and check-out of yard tractor-trailers, yard trucks, shuttle trucks, tractors, and drivers" — tractors and drivers are checked-in entities too, not just trailers.
- **Tasking (A):** "two-way communication between traffic managers and drivers to assign, prioritize, and confirm tractor-trailer move tasks"; event-based automation triggers on "asset check-in, asset status change, or dock availability."
- **Product tiers (A):** Essentials ("gate, dock, and asset management plus analytics… no bells & whistles") → Tasking Spotter Kit ("adds the Tasking Spotter Kit for spotter management alongside all core yard functions") → RTLS Spotter Kit ("automates inventory and streamlines operations with advanced IoT, tracking, and analytics"). This documents a maturity gradient from manual to sensor-automated within one vendor's own packaging.
- **Dock appointments (A):** "Yard managers, warehouse teams, carriers, and suppliers can self-schedule inbound+outbound appointments" — appointments live inside the YMS.
- **Detention machinery (A):** "accessorial charge profiles, utilizing yard filters to group assets and define parameters for fee structures, free time, and calculation intervals to track detention and demurrage fees."
- **Enterprise/network (A):** multi-yard configuration; "cross-network EVP dashboards"; integration with WMS, TMS & ERP via web API.
- **Cold chain (A):** reefer temperature and fuel monitoring inside the platform (ColdLink branding for the yard+transport cold chain package).
- **Terminal/intermodal adjacency (A):** same vendor sells Terminal Operating Systems (ocean terminals) and rail solutions; blog discusses "container yard operations in terminals" — the yard pattern extends to intermodal facilities (variant context, not the DC core).
- **WMS-module seam, vendor-articulated (A):** "WMS platforms are fundamentally designed to optimize inventory and workflows inside the facility. The yard is not just an extension of the warehouse floor… Most WMS yard add-ons are not built to manage this activity in real time." FAQ: "While many WMS modules can record a trailer's location, they often lack the real-time synchronization and automated rules needed to optimize movement."
- **YMS+TMS relationship (A):** "When purchased in combination with Kaleris TMS, businesses have the power to execute an end-to-end transportation management plan and cover blind spots that can't be filled with a YMS alone" — YMS and TMS are separate purchasable products.

## Product C — C3 Solutions / C3 Yard (dedicated; dock-scheduling sibling)

### Key observations

- **Definition published by vendor (A):** "C3 Yard… allows logistics operators to control the flow of tractors, trailers and shunters entering the yard of their distribution center… gives you visibility down to the SKU level for everything in your yard from the gate to the dock and back out the gate again."
- **Zone framing (A):** gate control ("pre-arrival visibility, gate-pass printing, intelligent put-away… the gate stops being a bottleneck"), yard ("real-time visibility on yard assets — know where trailers and tractors are parked, how many empty trailers are available"), enterprise visibility (multiple sites under one view).
- **Tasking (A):** "a rule-based optimizer feeds shunter drivers clear mobile instructions and tracks execution in real time"; "the two-way radio days are over"; automated shunter task optimizer using an AI-driven algorithm over the pool of work. ("Shunter" = UK/EU term for yard tractor/driver.)
- **Business-rule engine (A):** "rule-based workflow engine automates repetitive tasks and links operations by mapping your processes to business rules."
- **Units managed (A):** trailers, tractors, shunters, containers (container-returns case study); empty-trailer availability explicitly tracked.
- **Extras (A):** seal management; document attachments; multilingual platform; carrier/supplier portal; scorecarding; capacity model for labor/equipment planning; integrations "through APIs to TMS, WMS, and RTV systems."
- **Dock-vs-Yard boundary, vendor-drawn (A) — the clearest first-hand source found this pass:**
  - Dock scheduling "governs everything that happens **before the truck arrives**… It answers a planning question: given the doors, labor, and equipment I have available, when should each carrier and supplier show up, and at which door?… **Dock scheduling's job effectively ends at the gate.**" Time horizon: days to weeks ahead. Unit of work: **the appointment**. Main question: "When should they come?"
  - Yard management "governs everything that happens **after the truck arrives**, from gate-in to gate-out. It answers an execution question: where is every trailer right now, which one should move next, and who is moving it?" Time horizon: right now. Unit of work: **the trailer and the move**. Primary users: "gate staff, yard drivers, yard controllers." Main question: "Where is it and what moves next?"
  - YMS core functions enumerated: "gate check-in that ties a physical arrival to the scheduled shipment; real-time visibility on every trailer, chassis, and tractor on the property, loaded or empty; automated task assignment for yard drivers, with priorities set by your business rules; dock door assignment and sequencing so the right trailer arrives at the right door at the right time; dwell tracking, detention exposure, and yard-level KPIs."
  - Confusion acknowledged: "Vendors on either side use the phrase 'dock and yard' loosely… plenty of WMS and TMS platforms include a scheduling module that gets described internally as yard management."
  - Coupling at scale: "the operational value at scale comes from one continuous record per shipment, running from the moment a carrier books through gate-in, yard moves, door assignment, unload, and gate-out."
- **Drop-and-hook insight (A):** "Live loading keeps the trailer and the appointment tightly coupled. Drop programs break that link on purpose. The trailer's life on your property now extends well beyond its appointment window, and your scheduling system has no visibility into that portion of the lifecycle." — the trailer stay, not the appointment, is the YMS's managed object.
- **Pre-history named by vendor (A):** manual tools "like spreadsheets and chalkboards"; below a threshold of trailers "an experienced yard supervisor holds the whole picture in their head and a whiteboard" (single-source vendor claim — kept out of the final document).
- **Scale targeting (A, marketing):** "Impactful with 4+ shunters and 100+ trailers-in-yard" — product-specific marketing threshold, research notes only.

## Cross-product Comparison

| Structure | YardView | kaleris | C3 Yard | Evidence |
|---|---|---|---|---|
| Yard as modeled space (gates, dock doors, yard locations/spots) | ✓ (digital-twin map, docks/spots/lanes) | ✓ (multi-location visibility, dock-door config) | ✓ (yard map, sites, offsite parking) | A, 3/3 |
| Trailer/container/tractor as tracked unit of record | ✓ ("every trailer and asset") | ✓ (asset inventory + status + dwell) | ✓ ("trailers, tractors and shunters… from the gate to the dock and back out") | A, 3/3 |
| Gate check-in / check-out bookends the visit | ✓ (gate access, timestamps) | ✓ (gate management feature) | ✓ (gate control, gate-pass) | A, 3/3 |
| Directed yard moves assigned to yard drivers | ✓ (in-cab tasking, Accept→Start→Finish) | ✓ (assign/prioritize/confirm move tasks) | ✓ (automated shunter task optimizer) | A, 3/3 |
| Movement recorded back; location of record maintained | ✓ (all post-arrival movement collected) | ✓ (time+date stamp all events) | ✓ (tracks execution in real time) | A, 3/3 |
| Dock door assignment/sequencing | ✓ | ✓ | ✓ | A, 3/3 |
| Lot checks / yard audits digitized | ✓ | ✓ (live inventory checks) | ✓ (implied by control tower; audit-log blog) | A, 3/3 (C3 indirect) |
| Dock appointment scheduling included | ✓ (separate product surface, same suite) | ✓ (inside YMS) | separate sibling product (C3 Reservations), coupled | A — packaging differs, capability common |
| Dwell/detention machinery | ✓ (D&D module, timestamps) | ✓ (charge profiles, free time, intervals) | ✓ (dwell tracking, detention exposure) | A, 3/3 |
| WMS/TMS/ERP integration | ✓ | ✓ | ✓ | A, 3/3 |
| RTLS/GPS/IoT automated location | optional/adjacent ("leverage existing GPS") | ✓ tier-gated (RTLS Spotter Kit) | not core (APIs to RTV) | A — implementation variant |
| Multi-site/network view | ✓ | ✓ (cross-network) | ✓ (enterprise visibility incl. non-C3 sites) | A, 3/3 |
| Cold chain (reefer temp/fuel) | – (not observed) | ✓ | – (temperature alerts mentioned in benefits FAQ) | A, kaleris-led → optional |
| Security/seals/cameras | ✓ | ✓ (kiosk, compliance) | ✓ (seal management) | A, 3/3 → common |
| Carrier self-service portal / scorecards | ✓ (carrier-booked appointments) | ✓ | ✓ (portal + scorecarding) | A, 3/3 → common (shared with Dock Scheduling) |
| Yard-driver mobile surface | ✓ (in-cab tablet) | ✓ (mobile workflows, no-download driver solutions) | ✓ (mobile everywhere) | A, 3/3 |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal; jointly held)

1. **The yard as a modeled physical space of record.** The facility's trailer-holding area held as addressable places (parking spots/rows/lanes/staging areas), plus the two boundary structures that define the Type's reach: the **gates** where vehicles enter and leave the property, and the **dock doors** where the yard meets the building. Remove → a trailer fleet tracker or a parking sheet with no facility structure; the Type stops being about *this facility's* yard.
2. **The movable-unit inventory of record.** Each trailer, container, or chassis on the property held as an individually identified record — carrier/shipment/load context, load status (loaded/empty; reefer-class attributes in cold-chain variants), current yard location, and its stay opened and closed by recorded arrival and departure at the gate. Remove → a gate log or a dock-appointment list with nothing managed between them; there is no yard.
3. **Yard movement work — directed and recorded.** Moves of units among yard places and to/from dock doors (spot a trailer at a door, pull it to a holding spot, shuttle it) assigned to yard drivers (jockeys/spotters/shunters) and recorded back against the unit, so the system's location picture is continuously reconciled with physical reality. How the update happens — manual update by a controller, mobile task accept/start/finish, or sensor feed — is implementation. Remove → a passive registry/visibility report; the "management" is gone.

Jointly-held is load-bearing:
- 1 alone = a facility map / parking management sketch.
- 2 alone = a trailer asset register or visibility feed (fleet-tracking territory).
- 3 alone = a generic task board.
- 1+2 without 3 = a static yard snapshot that decays (the documented failure mode of "passive record-keeper" WMS add-ons).
- 2+3 without 1 = trailer tracking unbound to any facility (Fleet Management territory).
- 1+3 without 2 = moving nothing.

### L1 — Common Mature Structure (very common in mature products; not definitional)

- Gate operation tooling: driver check-in workflows (manned or self-service kiosk/QR/camera), driver-tractor-trailer association, gate-pass printing, security checks.
- Dock door management: door master data, door assignment/sequencing, door availability status.
- Dock appointment scheduling (often carrier self-service) — standard inside YMS or bundled as a sibling product; also exists as the standalone Dock Scheduling Platform Type.
- Dwell/turn-time measurement and detention & demurrage support (fee profiles, free-time parameters, aging alerts, timestamped event evidence).
- Digitized yard checks / lot audits.
- Exception management (aging trailers, missed moves, temperature excursions) and alerting.
- Reporting/dashboards/KPIs (dwell, dock utilization, move counts, trailer pool size).
- Integration with WMS/TMS/ERP so trailers carry order/shipment context (SKU/PO-level content in deeper implementations).
- Mobile surfaces for yard drivers and controllers; control-room dashboards.
- Trailer-pool management (carrier commitments, empty-trailer availability).
- Multi-site/network visibility in enterprise deployments.

### L2 — Variant / Optional Structure

- Location-capture posture: manual/controller updates → mobile task confirmation → RTLS/GPS/IoT automated tracking (vendor tiers document this gradient).
- Security & compliance depth: seal management/blind-seal verification, camera/AI gate automation, safety-inspection prompts, emissions reporting (WAIRE-class, regional).
- Cold-chain monitoring (reefer temperature/fuel).
- Terminal/intermodal realization: container and chassis yards at ports/rail facilities (overlaps Terminal Operating System territory; "container yard operations in terminals").
- Drop-and-hook / trailer-pooling emphasis; carrier scorecarding.
- Packaging: standalone YMS ↔ WMS yard module ↔ TMS module ↔ logistics-suite component (kaleris sells YMS beside TOS/TMS; C3 and YardView sell dock scheduling beside YMS; WMS vendors bundle "free" yard tools — per vendor commentary).
- Scale/segment tuning: parcel hubs (shunter-heavy), retail/grocery DCs, manufacturing plants (shuttle scheduling), 3PL multi-client yards.

### L3 — Vendor-specific (research notes only)

- YardView: "digital twin" drag-and-drop console; per-asset data-point counts; 400+ reports claim; WAIRE module; blind-seal verification module; since-1998 positioning; three-phase implementation model.
- kaleris: RTLS Spotter Kit tiering; ColdLink; Execution & Visibility Platform (EVP) cross-network dashboards; SSO kiosk "no app download" driver check-in; ABI Research "#1 YMS" claim; PINC heritage (YMS since 2004).
- C3: C3 Reservations (dock) / C3 Yard / C3 Hive (driver pre-check-in collaboration) product family; business-rule engine; "shunter" UK/EU vocabulary; multilingual platform; 4+/100+ marketing thresholds; ~40-trailer whiteboard-threshold claim.

### Rejected Findings (candidates examined and not promoted)

- **"Real-time" / digital-twin map as definitional** — rejected: the C3/kaleris commentary itself frames pre-YMS forms (chalkboards, whiteboards, paper logs) as the same job done manually; the map is the modern presentation of the location-of-record, not the Type.
- **Dock appointment scheduling as definitional** — rejected: it is the Dock Scheduling Platform's own center of gravity; in YMS it is a bundled/coupled capability; drop-and-hook makes the appointment optional to the trailer stay (C3's own analysis).
- **RTLS/GPS/IoT as definitional** — rejected: kaleris's own Essentials tier and YardView's "no special hardware required" FAQ show the Type functions without sensors.
- **Detention & demurrage calculation as definitional** — rejected: it is a dwell-economics layer on the recorded timestamps; present across the sample but as a module; the timestamps themselves are the load-bearing structure (L1).
- **Tractor/vehicle fleet management as the center** — rejected: tractors appear as checked-in/movable assets and as task executors, but the managed inventory center of gravity is the trailer/unit waiting for or leaving the dock. (Consistent with the autonomous-fleet pass's boundary.)
- **"Supply chain visibility platform" reading** — rejected: visibility modules exist (kaleris EVP), but the sampled YMS core is facility execution, not network visibility.

## Boundary Findings

1. **vs Warehouse Management System (WMS) — DISCHARGES the WMS pass's pre-hung seam; RATIFIED from this side, no merge.** WMS = goods handling inside the building (bins, picking, directed warehouse labor); YMS = trailers/vehicles and dock doors outside the building (gate↔door slice). All three dedicated vendors draw the same line independently (YardView: "WMS focuses on inventory, picking, and storage inside the warehouse… YMS coordinates all activities between the gate and dock"; kaleris: "WMS platforms are fundamentally designed to optimize inventory and workflows inside the facility"; C3: YMS = "from gate-in to gate-out"). The handoff is concrete: a trailer spotted at a door hands its contents to the WMS; the WMS's outbound release hands a trailer back to the yard for departure. WMS-side edges (driver check-in, staging/loading locations) acknowledged in the WMS pass. WMS "yard modules" exist as packaging (see Related), not as a different structure.
2. **vs Dock Scheduling Platform (§10 sibling, unprocessed) — boundary drawn from this side for that pass to ratify.** C3's vendor-drawn distinction (vendor sells both): dock scheduling = plan-before-arrival (appointments, capacity, days-to-weeks horizon; unit of work = the appointment; "ends at the gate"); yard management = execute-after-arrival (gate-in to gate-out; unit of work = the trailer and the move). They couple into one continuous record at scale and are frequently bundled/sold together (all three vendors), but neither subsumes the other: a scheduling system has no execution picture of the yard (C3: "the plan on the screen no longer resembles what is happening outside the fence"), and a YMS "can execute brilliantly against a bad plan."
3. **vs Transportation Management System (TMS) — DISCHARGES the TMS pass's seam (8); RATIFIED, no merge.** Yard/dock machinery ships as TMS modules (Shipwell Dock Scheduling per TMS pass), and YMS+TMS are sold as separate products that integrate (kaleris explicitly: TMS "covers blind spots that can't be filled with a YMS alone"). TMS = between-locations freight; YMS = on-property execution.
4. **vs Fleet Management System** — fleet manages road tractors/trucks as revenue vehicles (drivers, HOS, telematics); YMS manages the facility's trailer population and yard moves. Yard tractors appear in a YMS as checked-in equipment/task executors, not as the managed fleet. Boundary consistent with the autonomous-fleet-management pass ("manages yard space, trailer inventory, and dock scheduling as a facility concern").
5. **vs Port Terminal Operating System** — cross-mode analog: berth/crane/vessel-call machinery vs trailer yard at a DC. Adjacent where intermodal/container yards meet drayage (kaleris sells both TOS and YMS; container-returns flows appear in C3 case studies).
6. **vs Inventory Management System / Construction Materials Management** — laydown yards and trailer contents can appear as location surfaces in those Types; the YMS object world is vehicles+yard places+dock doors, not material quantities.
7. **vs garage-door-service-management** — already resolved vendor-side (ServiceTitan FAQ, per that pass): door-level contractor service ops vs yard logistics. No action.

## Historical / Market-Sample Check

- Vendors name the pre-history themselves: "spreadsheets, phone calls, or paper logs" (YardView), "spreadsheets and chalkboards" (C3), "clipboards, whiteboards, spreadsheets, and legacy systems" (YardView blog). The analog yard office — gate logbook (trailer #, carrier, seal, arrival/departure times), chalkboard/whiteboard of yard spots and dock doors, radio dispatch of jockeys, periodic lot walks — satisfies all three L0 legs at analog level: modeled space (board of spots/doors), unit inventory of record (logbook + current board position), directed-and-recorded moves (radio instruction + board re-chalked after each move). The category digitized this office; the definition should not require its digital-tooling replacements (digital twin, kiosks, RTLS, mobile apps).
- The dedicated-YMS market dates to the late-1990s/2000s web era (YardView 1998, C3 2000, kaleris/PINC YMS 2004 per vendor statements), with earlier yard functions living inside WMS/ERP. Nothing in the L0 depends on that era's implementation: no cloud, no mobile, no sensors, no AI.
- Regional check: C3 documents the UK/EU "shunter" vocabulary against US "jockey/spotter"; the L0 is vocabulary-neutral ("yard driver", "move"). Multi-site enterprise, single-site, terminal, and parcel realizations all satisfy the core.

## Uncertainties

1. **No Tier-1 help-center reached for any sampled product.** All observations are Tier-2 vendor documentation (product/FAQ/blog). Operational depth (exact state machines, default dwell thresholds, permission models, edit rules) is therefore not asserted anywhere in the final document.
2. **Suite-embedded pole (SAP Yard Logistics, Manhattan, Oracle WMS Cloud yard area) under-observed.** The module-realization claim rests on vendor commentary (three independent sources) plus the TMS pass's Shipwell evidence, not on fetched suite documentation.
3. **Lot-check maturity at C3** inferred from product positioning and audit-log blog, not from a feature-by-feature doc — held as indirect (A, weak).
4. **"Yard" scope edge:** whether gate/security machinery (cameras, LPR, access control) is part of the Type or an adjacent security product is packaging-dependent; vendors bundle it (Gate Access Control), but the L0 only requires the gate *event*, not the hardware.
5. **Detention-fee computation depth** varies (YardView module, kaleris charge profiles); whether fee *invoicing* (vs tracking/exposure) is in-Type is unclear — held as optional machinery.

## Final Synthesis

A Yard Management System is the facility's system of record for the trailer yard — the bounded space between the property gate and the dock doors. Its defining core is three jointly-held structures: (1) the yard held as a modeled, addressable physical space whose boundary structures are the gates and the dock doors; (2) a movable-unit inventory of record — every trailer/container/chassis on the property as an identified record with load status, carrier/shipment context, and a stay bookended by recorded gate arrival and departure; (3) yard movement work — spot/pull/shuttle moves among yard places and dock doors — directed to yard drivers and recorded back against the unit, keeping the location picture reconciled with physical reality.

Around that core, mature products add gate operation tooling, dock-door management and appointments, dwell/detention machinery, digitized yard checks, exception alerting, mobile driver surfaces, WMS/TMS/ERP integration, and network-level reporting. Implementation postures (manual updates vs RTLS; standalone vs module packaging; single site vs network; DC vs terminal vs parcel) are variants.

The Type's identity comes from its slice of the supply chain: it manages the *between* — after transportation delivers a trailer to the property and before the warehouse takes the goods (and the reverse) — which is exactly why WMS, TMS, and Dock Scheduling are neighbors rather than equivalents, and why vendors across the sample independently describe the YMS as "the gap between warehouse and transportation systems" and "from gate-in to gate-out."
