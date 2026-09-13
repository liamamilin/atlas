# Research Notes — Vehicle Inspection / Diagnostic Application

Research date: **2026-09-09**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what "Vehicle Inspection / Diagnostic Application" is as an Application Type: software whose job is to examine a specific vehicle and produce structured condition findings — either by reading the vehicle's own onboard diagnostic data (fault codes, sensor values, monitors) or by recording a human examiner's structured observations (checklist inspections). Establish the core objects and the canonical examination loop, and fix the boundary against Auto Repair Shop Management (whose digital vehicle inspection is a module), Fleet Management System (whose DVIR is a module), Vehicle Telematics Platform (continuous data vs examination sessions), and Property Inspection Application (same inspection pattern, different object).

Prior sibling evidence loaded before research:
- `research/auto-repair-shop-management.md` (2026-09-06) flagged this leaf: "the DVI is a module inside this Type; standalone inspection/diagnostic products are technician instruments (scan tools, inspection checklists) without the business lifecycle. Fragment, not duplicate." DVI module evidence exists there for 4 shop-management products (Tekmetric, Shopmonkey, R.O. Writer, Shop-Ware): inspection templates, photos/videos/markups, findings, canned jobs auto-added to ROs, declined-work retention, customer-facing inspection reports.
- `research/home-inspection-application.md` (2026-09-08) lists this leaf as a related Type ("different object — vehicles vs real property").

## Initial Boundary

Initial hypothesis (before research):

- Core use: examine one vehicle at a time and answer "what condition is it in / what's wrong with it" — via (a) electronic read-out of the vehicle's own diagnostic systems (OBD-style scan tools) and/or (b) structured human inspection (checklists, DVIR, multi-point inspection).
- Primary users: vehicle owners/DIYers, technicians, drivers, fleet/shop managers.
- Nearest types: Auto Repair Shop Management (inspection as module; business lifecycle absent here), Fleet Management System (DVIR as module), Vehicle Telematics Platform (§18; continuous streaming vs deliberate session), Property Inspection Application (§29; same pattern, different object), Government Inspection Management (public-sector regimes, not vehicle-specific software).
- Expected distinguishing structures: no repair order, no parts/labor billing, no business lifecycle of record — the output is findings + recommended action, not a commercial transaction.
- Unknowns: whether the two halves (checklist inspection vs electronic diagnostics) share one core structure or are two Types; how much regulatory structure (smog readiness, DVIR) is definitional; how pro-tier capabilities (bi-directional, repair-info integration) sit in the abstraction.

## Research Questions

1. What is the canonical examination loop for an electronic diagnostic session (connect → identify → read → interpret → report)?
2. What condition data does the software read, and how is it structured (code types, monitors, freeze frame, live parameters)?
3. How does the vehicle-specific interpretation layer work (code definitions, repair reports, procedures, wiring diagrams)?
4. What does the checklist-inspection loop look like (forms, pass/fail, photos, failed-item handling, confirmation on next inspection)?
5. How are findings retained and shared (per-vehicle history, export, customer-facing reports, compliance records)?
6. Which capabilities are consumer vs professional vs fleet (bi-directional routines, repair info, ADAS, compliance)?
7. Where do inspection/diagnostic outputs hand off to other Types (declined work → RO, failed item → work order)?
8. What regulatory structures bind the output (emissions readiness, DVIR), and are they definitional or regional?
9. Where exactly are the boundaries vs shop management, fleet management, telematics, and property inspection?

## Representative Products

Selected for market representativeness, documentation accessibility, different product philosophies, and different customer tiers:

| Product | Tier / philosophy | Why selected |
|---|---|---|
| BlueDriver (Lemur Monitors / Repairify) | Consumer/prosumer: dongle + phone app; "professional-grade diagnostics made simple" | Best-documented consumer scan tool; help center + feature page reachable |
| OBD Auto Doctor (Creosys) | Prosumer cross-platform app (iOS/Android/macOS/Windows) + generic ELM327 dongles; app-only philosophy (no proprietary hardware) | Deeply documented feature set (DTC modes, monitors, PIDs, routines); European vendor — regional breadth |
| Bosch ADS X + ESI[truck] (Bosch Automotive Service Solutions) | Professional workshop diagnostics: tablet scan tool + wireless VCI + OEM repair data; heavy-duty line | Professional tier + heavy-duty variant from an OE-parts maker |
| Fleetio Inspections (Rarestep) | Fleet operations: DVIR/checklist inspections embedded in a Fleet Management System | Documents the inspection-checklist branch and the embedded-module boundary |

Non-researched anchors (recorded as limitations): FIXD (fixdme.com HTTP 445; support.fixdme.com transport error — 2 attempts, abandoned), Whip Around (whiparound.com timeout ×2, abandoned), Autel/Launch (not attempted — stop conditions met). BlueDriver help-article bodies did not render (Intercom SPA shell only); article titles/collections used.

## Sources

### BlueDriver (official product page — Tier 2; official help center inventory — Tier 1, article bodies not renderable)

- Product site: https://www.bluedriver.com/ — features: read & clear codes (plain-language), Repair Reports (vehicle-specific, "built from millions of verified fixes"), Mode 6, Freeze Frame, Smog Check (readiness monitors), Live Data streaming; "9,000+ diagnostic codes"; multi-vehicle support; BlueDriver MAX (dealership product line, separate support portal).
- Help center root: https://support.bluedriver.com/en/ — collections: Popular Questions / General Questions / Troubleshooting / **BlueDriver Features (23 articles)** / Extra Manufacturer Tips & Tricks.
- Features collection: https://support.bluedriver.com/en/collections/19635115-bluedriver-features — sub-collections: Freeze Frame (How to Use; with no Check Engine Light), Live Data (Setup; Guide; Fuel Trim N/A; O2 sensors; Fuel System B), Mode 6 (Introduction; References), Reading and Clearing Codes (**Confirmed, Pending, Permanent, and Enhanced Codes**; Reading & Clearing; Can Codes be Permanently Cleared?; What is a P1000 Code?; History Codes; **Odometer Entry**), Saved Reports (Removing Old Scans and Reports), Smog Check (**Completing Drive Cycles**; Smog Test Results Complete vs Incomplete; How to Run a Smog Check; Resetting Emissions Tests), Vehicle Information (**Vehicle Identification**; Removing Old Vehicles; recalls applicability).
- Related-article evidence: "How do I check to see if codes have been cleared recently?" (cleared-code detection exists as a capability).
- Limitation: article bodies render empty via fetch (Intercom SPA); titles and grouping only.

### OBD Auto Doctor / Creosys (official product + features pages — Tier 1/2; very detailed)

- Root: https://www.obdautodoctor.com/ — OBD2 diagnostic app + ELM327 dongle; iPhone/Android/macOS/Windows; audiences: everyday drivers, DIY mechanics, dealers and small repair shops; 6.7M+ downloads; read/clear codes, reset MIL; emissions-inspection readiness self-check; real-time sensor monitoring; bi-directional routines (e.g. DPF regeneration).
- Features page: https://www.obdautodoctor.com/features/ —
  - DTC types: **Stored/Confirmed (Mode $03), Pending (Mode $07), Permanent (Mode $0A)**; categories P/B/C/U; manufacturer-specific codes supported; **reset DTCs / clear Check Engine Light**; **offline DTC database 18,000+ codes** for search/browse; export DTC + freeze frame to text file for sharing/archiving.
  - Freeze Frame: captured recording of engine conditions at malfunction time (DTC + parameter readings).
  - **Readiness monitors**: up to 11 system tests; two status groups (since DTCs cleared; this driving cycle); Complete/Incomplete/Disabled; inspection-readiness framing; US EPA guidance on allowable incomplete monitors quoted (model-year-dependent).
  - Sensors & parameters: real-time values + min/avg/max; metric & imperial units; 126+ powertrain PIDs ($00–$7F); **CSV export**; Sensor Graph ("oscilloscope"), Graph Grid, Histogram; graph image export ("share with your mechanics or forums"); up to 6 sensors simultaneously.
  - **Diagnostic monitoring tests**: Oxygen sensor monitor tests (Mode $05, protocol-dependent); On-board monitoring tests (Mode $06, CAN).
  - **Bi-directional controls (Mode 8)**: evaporative system leak test; particulate filter regeneration; inducement system reinitialization. In-Use Performance Tracking counters.
  - Vehicle/ECU info: ECU name, **VIN**, CALID, CVN, supported sensors; advanced raw-command **troubleshoot console**; multiple control units (engine + e.g. transmission).
- OBD2 explainer: app communicates with the vehicle's onboard computer via dongle bridging the 16-pin OBD2 port; Bluetooth/Wi-Fi/USB adapters.

### Bosch Diagnostics (official product pages — Tier 2)

- Root: https://www.boschdiagnostics.com/ — navigation: Diagnostic Systems, ADAS, Heavy Duty, J2534, accessories; owned by Bosch Automotive Service Solutions; sister brands OTC, Robinair.
- ADS X platform: https://boschdiagnostics.com/ads-x — professional scan tools (ADS 525X, ADS 10X Plus): tablet + wireless J2534-compliant VCI (DoIP, CAN FD); **Rapid DTC Scan — all-systems scans, Topology View, complete pre/post-scan reporting**; **Secure Gateway access (OE-approved)**; **MOTOR TruSpeed Repair — OEM repair procedures, wiring diagrams, component locations, ADAS calibration data, on-tool + PC**; 3,300+ ADAS calibration procedures (10X Plus); wiring-diagram database (700,000+ diagrams claim); coverage across domestic/European/Asian makes + EVs; subscription software (Basic/Enhanced tiers), over-the-air updates; audience: independent shops/technicians.
- Heavy duty: https://boschdiagnostics.com/hd — ESI[truck]: troubleshooting integrated on-tool ("code to fix at the truck"); **automatic vehicle ID**; single UI across all trucks; read/clear fault codes; **cylinder cut-out, cylinder compression/balance, injector actuations, key component actuations, key system tests**; wiring diagrams, component pictures/locations, test procedures, DTC lookup at the truck; coverage across truck/engine/brake/transmission/trailer-ABS brands; Bluetooth.

### Fleetio Inspections (official feature page — Tier 2; embedded module of a Fleet Management System)

- Feature page: https://www.fleetio.com/features/vehicle-inspections/ —
  - **Driver inspection app**: conduct inspections from mobile device or computer; attach photos and comments; **offline capable**; odometer readings logged.
  - **DVIR compliance**: "FMCSA-compliant DVIRs"; complete inspection history as compliance record; audit reporting; customizable forms (vehicles, trailers, equipment, facilities).
  - **Failed-item workflow**: administrators immediately alerted to failed inspection items; failed items **converted into work orders in a few clicks**; repairs completed and **recorded against the original inspection report**; **driver confirms resolution in next inspection**.
  - Canonical loop published by the vendor: driver inspects & records findings → results appear, manager schedules repairs → repairs recorded against report → driver confirms resolution in next inspection → vehicle road-ready with compliant report.
  - Inspection data analytics: most-failed items/vehicles dashboards; compliance reports for uninspected vehicles; **GPS-based alerting for inspections submitted from suspicious locations ("pencil whipping")** — Fleetio-specific.
  - Pre/post-trip framing ("Pre & Post-Trip Inspection Software"); inspection scheduling with due alerts.

### Sibling research evidence (already processed leaves)

- Auto Repair Shop Management (4 products): DVI as a standard module — inspection templates per work type; photos/videos/markups; findings; canned jobs auto-added to repair orders; customer e-signatures; inspection reports sent to customers (text/email); declined estimate lines retained for follow-up; DVI reporting/benchmarking. (Tekmetric, Shopmonkey, R.O. Writer, Shop-Ware — see `research/auto-repair-shop-management.md`.)
- Home Inspection Application: same inspection pattern on a different object (real property), client-commissioned fee-bearing orders. (See `research/home-inspection-application.md`.)

---

## Product A — BlueDriver

### Key observations (evidence layer A for feature facts; article bodies not renderable)

- Form factor: proprietary Bluetooth dongle into the OBD2 port + phone app; positioning "turn your phone into the same tool they use in the shop" for DIYers; separate MAX line for dealerships.
- Core readout set: read & clear trouble codes with plain-language translation; **Confirmed / Pending / Permanent / Enhanced (manufacturer) code types**; history codes; P1000 handling.
- **Vehicle identification**: article "Vehicle Identification"; multi-vehicle management (removing old vehicles); recalls applicability article.
- **Odometer entry** at scan time.
- Interpretation layer: **Repair Reports — vehicle-specific repair suggestions ("confirmed fixes") built from a verified-fix database**; 9,000+ diagnostic codes.
- Advanced readouts: **Mode 6** on-board test results; **Freeze Frame** (sensor snapshot at fault time, even with no CEL); **Live Data** streaming (setup + guide; fuel trim, O2 sensors, fuel system status); **Smog Check** — emissions readiness monitors, complete vs incomplete, drive-cycle completion guidance, emissions-test resetting.
- **Saved Reports**: scans/reports persist in the app; removal is an explicit operation.
- Integrity: "check to see if codes have been cleared recently" — cleared-code detection.
- Account creation (BlueDriver Account); 24/7 support incl. in-app chat.

## Product B — OBD Auto Doctor

### Key observations (evidence layer A — directly observed, detailed)

- Form factor: app-only (iOS/Android/macOS/Windows) over any ELM327-compatible dongle (Bluetooth/Wi-Fi/USB); multi-language (11 UI languages incl. Finnish, German, Swedish — European vendor); since 2010.
- Readout set identical in structure to BlueDriver: Confirmed (Mode 3) / Pending (Mode 7) / Permanent (Mode 0A) codes; P/B/C/U categories; manufacturer-specific codes; **reset DTCs clears the MIL**.
- **Offline DTC database (18,000+ codes)** for search/browse — interpretation layer is shipped with the app, not cloud-only.
- Freeze Frame; Readiness monitors (two status groups; Complete/Incomplete/Disabled; explicit inspection-readiness purpose incl. quoted EPA model-year guidance); Oxygen sensor monitor tests (Mode 5, protocol-dependent); On-board monitoring tests (Mode 6, CAN); In-Use Performance Tracking.
- **Bi-directional service routines (Mode 8)**: evap leak test, particulate filter regeneration, inducement system reinitialization — "command the vehicle's onboard system to initiate or perform specific tests".
- Live data: values + min/avg/max; 126+ PIDs; metric/imperial; graphs/grid/histogram; CSV export; graph-image export framed for sharing with mechanics/forums.
- Vehicle/ECU info: VIN, CALID, CVN, ECU name, supported sensors; multi-ECU access (engine + transmission); raw-command console for advanced users.
- **Export/share**: DTC + freeze-frame to text file; CSV; PNG — the findings record is designed to travel (mechanic, forums, archive).
- Audience segmentation on one product: everyday drivers / DIY mechanics / dealers and small repair shops (post-repair code reset use case).

## Product C — Bosch ADS X / ESI[truck]

### Key observations (evidence layer A for module inventory; marketing-depth source)

- Form factor: rugged tablet scan tool + wireless J2534 VCI; software on subscription with over-the-air updates; tiered plans (Basic/Enhanced); model tiers (525X/10X Plus).
- **All-systems DTC scan in under 40 seconds (vendor claim); Topology View; pre/post scan reporting** — pre/post scans are a documented shop practice (e.g., before/after repair for liability documentation).
- **Automatic/assisted vehicle identification** (auto vehicle ID on ESI[truck]); broad vehicle-coverage matrix as a first-class product dimension (domestic/European/Asian, EV, ADAS-equipped; truck/engine/brake/transmission brands for HD).
- Interpretation layer at professional depth: **OEM repair procedures, wiring diagrams (700k+ database claim), component locations, DTC lookup, test procedures — on-tool + PC (MOTOR TruSpeed Repair)**; "code to fix at the truck" (ESI[truck]).
- **Bi-directional actuation as a professional core function**: cylinder cut-out, cylinder compression/balance, injector actuations, key component actuations, key system tests (HD); J2534 reflash/programming posture; **Secure Gateway access** (OE-approved) for security-protected vehicles.
- **ADAS calibration data/calibration procedures** as an adjacent capability on the diagnostic platform.
- Diagnostic results are embedded in the repair workflow ("get the repair done right and the vehicle back in operation") but the tool itself performs no repair-order/billing functions — the business lifecycle lives in separate shop software.

## Product D — Fleetio Inspections (module)

### Key observations (evidence layer A for feature facts; module-of-FMS context)

- Object: the inspection as a **completed form instance bound to a specific vehicle**, with per-item results, photos, comments, odometer reading.
- Forms: **customizable inspection templates** per vehicle/equipment type; pre-trip/post-trip (DVIR) forms; offline completion on mobile.
- **Compliance**: FMCSA-compliant DVIRs; inspection history retained as audit/compliance record; compliance reports (uninspected vehicles flagged); due-date alerts.
- **Failed-item workflow**: real-time alerts to administrators; failed items convert to work orders in a few clicks; repairs recorded against the original inspection report; **driver confirms fix in next inspection** — a closed defect→repair→confirm loop.
- Integrity/measurement: GPS checks for suspicious submission locations ("pencil whipping") — **Fleetio-specific**; inspection analytics (most-failed items/vehicles).
- Context: inspections are one feature of a fleet platform (work orders, service history, parts, fuel, vendors) — the inspection output hands off into fleet maintenance machinery, exactly as DVI hands off into repair orders in shop software.

---

## Cross-product Comparison

| Structure | BlueDriver | OBD Auto Doctor | Bosch ADS X / ESI[truck] | Fleetio Inspections (module) | Assessment |
|---|---|---|---|---|---|
| Binds to a specific vehicle per examination | Yes (vehicle identification; multi-vehicle records) | Yes (connected vehicle; VIN/ECU info) | Yes (auto vehicle ID; coverage matrix) | Yes (form bound to vehicle) | **Core (4/4)** |
| Structured condition capture | codes + monitors + live PIDs + freeze frame | codes + monitors + live PIDs + freeze frame + tests | all-systems code scan + tests + actuations | checklist items + photos + odometer | **Core (4/4)** |
| Vehicle-specific interpretation layer | plain-language code translation; Repair Reports (verified fixes) | offline DTC database (18k+); code definitions | OEM repair procedures, wiring diagrams, DTC lookup, test procedures | form items = pre-defined checks with pass/fail semantics | **Core (4/4)** |
| Findings surfaced/retained as the product's output | displayed + Saved Reports | displayed + text/CSV/PNG export | displayed + pre/post scan reports | submitted report + history + compliance record | **Core (4/4)** |
| DTC read (confirmed/pending/permanent, +enhanced) | Yes | Yes (Modes 3/7/0A) | Yes (all-systems; enhanced) | n/a (human branch) | Core of electronic branch (3/3) |
| Code clearing / MIL reset | Yes (clear codes) | Yes (reset DTCs → clear MIL) | Yes (read/clear fault codes) | n/a | Core of electronic branch (3/3) |
| Live sensor data with graphs | Yes (Live Data) | Yes (graph/grid/histogram; CSV) | Yes (implied; live data standard on pro tools — see uncertainty) | n/a | Common electronic-branch (2–3/3) |
| Freeze frame | Yes | Yes | — (not directly observed) | n/a | Common electronic branch (2/3 observed) |
| Emissions readiness monitors / smog readiness | Yes (Smog Check; drive cycles) | Yes (explicit inspection-readiness purpose) | — | n/a | Common electronic branch; regional regulatory driver (2/3) |
| Bi-directional tests/service routines | — (not observed) | Yes (Mode 8; 3 routines) | Yes (cylinder/injector/system actuations) | n/a | Professional/prosumer tier; depth varies |
| OEM repair info integration (procedures/diagrams) | partial (Repair Reports = fix suggestions) | — (code database only) | Yes (full OEM repair data on-tool) | n/a | Professional tier differentiator |
| Inspection templates / customizable forms | n/a | n/a | n/a | Yes | Core of checklist branch |
| Photos/comments attached to findings | n/a (implied via reports? not observed) | n/a (graph export instead) | n/a (photos on DVI in shop module) | Yes | Common checklist branch (Fleetio + shop-DVI siblings) |
| Findings → downstream action handoff | implicit (repair suggestions; DIY) | implicit (share with mechanic) | embedded in repair workflow (no RO) | **explicit** (failed item → work order; confirm next inspection) | Common; explicit handoff in managed operations |
| Per-vehicle examination history | Yes (Saved Reports; old scans removal) | Yes (export/archive; implied storage) | Yes (scan records; pre/post) | Yes (inspection history) | Common (4/4) |
| Odometer captured at examination | Yes (Odometer Entry) | — (not directly observed) | — (not directly observed) | Yes | Common (2/4 + shop-DVI siblings) |
| Multi-vehicle management | Yes (add/remove vehicles) | — (session-focused; not observed) | Yes (coverage; HD fleets) | Yes (whole-fleet population) | Common in managed contexts |
| Compliance-record retention (regulatory) | — | readiness guidance (EPA) | — | Yes (FMCSA DVIR; audit reports) | Regional/regulatory variant |
| Cleared-code detection / integrity checks | Yes (cleared-recently check) | — (not observed) | — | Yes (GPS pencil-whip detection) | Optional; integrity-oriented, 2 vendors, different mechanisms |
| Subscription/paid tiers | hardware + free/paid app features | freemium + subscription | hardware + software subscription | part of FMS pricing | Commercial model, not structural |

### Key finding — one core, two capture modes

The checklist branch (Fleetio; DVI modules in shop software) and the electronic branch (BlueDriver, OBD Auto Doctor, Bosch) share the same spine: **a specific vehicle → a structured capture of its condition (human observations against a form, or electronic read-out against the vehicle's own protocols) → interpretation against vehicle-specific reference knowledge → findings surfaced and retained**. The two branches differ in capture mechanism, not structure. Historical forms (paper multi-point sheets, handheld code readers) fit the same spine.

### Key finding — the Type ends at findings; it does not own the business lifecycle

None of the four samples writes repair orders, sells parts/labor, or bills customers as the system of record. Recommendations and handoffs exist (Repair Reports; "share with your mechanic"; failed item → work order), but the money-and-work lifecycle belongs to Auto Repair Shop Management or Fleet Management System. This confirms the auto-repair sibling's boundary verdict.

### Key finding — interpretation depth is the tier axis

Consumer: code definitions + (optionally) fix suggestions. Prosumer: large offline code databases + sharing. Professional: OEM repair procedures, wiring diagrams, component locations, test procedures on-tool. The interpretation layer scales with the audience; the capture loop does not.

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being a vehicle inspection/diagnostic application:

```text
Specific vehicle under examination
└── Structured condition capture
    │   (electronic read-out of the vehicle's own systems,
    │    and/or examiner observations against a defined form)
    └── Vehicle-specific interpretation
    │   (code definitions, specifications, procedures, pass/fail criteria)
    └── Findings surfaced to the examiner
        (the interpreted result is the product's output)
```

Four properties:

1. **A specific vehicle as the subject** — every examination session binds to one identified (or at least selected) vehicle. Remove it → generic form builder or data logger.
2. **Structured condition capture** — observations are recorded against a defined structure (diagnostic modes/parameters, or checklist items), not freeform notes. Remove it → a conversation or a blank notepad.
3. **Vehicle-specific interpretation** — raw readings/codes/observations are translated through reference knowledge tied to the vehicle (code definitions, specs, procedures, pass/fail criteria). Remove it → raw telemetry, not diagnosis.
4. **Findings as the output** — the product's deliverable is the interpreted findings (display, report, record), not a transaction. Remove it → the capture serves some other system and this Type stops being the point.

Deliberately NOT in L0: OBD2 specifically (any vehicle-data interface qualifies; pre-OBD and heavy-duty use other protocols); dongle hardware (app-only and handheld-device implementations exist); saved cloud history (handheld readers display without storing); work orders / billing / scheduling (other Types); DTC codes specifically (the checklist branch captures human observations).

### L1 — Common Mature Structure

Present across most mature modern products; not required to recognize the Type:

- vehicle identification built into the session (VIN auto-read, plate/manual entry, selection from a vehicle list) and per-vehicle records retaining past examinations
- DTC reading across code types (confirmed/stored, pending, permanent, history, manufacturer-enhanced) and code clearing with MIL reset
- live parameter display with graphs; min/avg/max; unit selection; export (CSV/text/image)
- freeze frame (sensor snapshot at fault time)
- emissions readiness monitors and inspection-readiness guidance (drive cycles, complete/incomplete states)
- on-board monitor test results (Mode 5/6-style readouts)
- DTC reference databases (offline or online) with search/browse
- inspection forms/templates with pass-fail or measured items; photos and comments attached to findings; odometer capture
- saved examination history per vehicle; report export/share (PDF/text; customer- or mechanic-facing)
- recommended actions attached to findings (fix suggestions, maintenance recommendations)
- alerts/notifications on failed or due items in managed contexts (fleet/shop)
- findings handoff to downstream action: declined/recommended work retained for follow-up (shop DVI), failed item → work order with confirmation at next inspection (fleet)

### L2 — Variant / Optional Structure

Depends on segment, region, regulation, vehicle class:

- segment forms: consumer DIY scan-tool app; prosumer cross-platform app; professional workshop platform; fleet/driver inspection app; dealer/used-car condition reporting (pre-purchase inspections — same core, client-commissioned)
- hardware postures: proprietary dongle + phone; generic dongle + app; rugged tablet + VCI; standalone handheld reader with on-device definitions
- regulatory layer: emissions-readiness regimes (e.g., US smog programs, EPA model-year guidance); commercial driver inspection regimes (e.g., FMCSA DVIR); other roadworthiness regimes — regional, not definitional
- vehicle class: light-duty passenger vs heavy-duty/commercial (cylinder cut-out, injector actuation, truck/engine/brake coverage) vs EV/ADAS-era coverage
- bi-directional capability depth: none → a few standardized routines (evap test, DPF regeneration) → full professional actuation suites and secure-gateway access; J2534 reflash/programming posture
- integration depth: standalone instrument vs embedded module (DVI inside shop management; DVIR inside fleet management) vs platform with repair-data subscription
- integrity/compliance tooling: cleared-code detection; submission-location checks; audit/compliance reporting
- commercial models: hardware + app purchase, freemium, software subscription, included in a wider platform

### L3 — Vendor-specific Structure

(Research Notes only)

- BlueDriver: Repair Reports ("millions of verified fixes"), Mode 6 collections, Smog Check packaging, BlueDriver MAX dealership line, odometer-entry feature, cleared-recently check, Repairify ownership.
- OBD Auto Doctor: Sensor Graph/"oscilloscope"/grid/histogram trio, raw-command Troubleshoot console, 18,000-code offline database, Mode 8 routine set (evap/PF-regen/inducement), CALID/CVN display, Creosys (Finland), 11 UI languages.
- Bosch: ADS X tiering (525X/10X Plus), Topology View, pre/post-scan reporting, MOTOR TruSpeed Repair, Secure Gateway OE-approved access, 3,300+ ADAS procedures, 700k wiring diagrams claim, ESI[truck] HD line, "under 40 seconds" scan claim, subscription tiers with OTA updates.
- Fleetio: GPS pencil-whipping detection, Maintenance Shop Integration (third-party repair approvals), Inspection Failures report, FMCSA-DVIR packaging, part of Fleet Management platform (Rarestep).

---

## Historical / Market-Sample Check (§24)

Question: would older, regional, or differently positioned products still fit the L0?

- **Handheld standalone code readers** (pre-app era; still sold): plug into the diagnostic port, read codes, display definitions on-device, no cloud, no account, no history. Satisfies L0 fully (vehicle + structured capture + definitions + surfaced findings). Saved history, graphs, sharing are L1.
- **Paper multi-point inspection sheets / paper DVIR** (still in use): printed form items (the reference structure), examiner marks pass/fail + notes (capture), completed sheet (findings record). Satisfies L0. Digital templates, photos, alerts, work-order handoff are L1.
- **Regional/electronic**: OBD2 is the North American implementation (1996+); EOBD/JOBD and heavy-duty protocols are other implementations of the same "vehicle's own systems" interface; OBD Auto Doctor (Finland, 11 languages) works across these. FMCSA DVIR is a US regulatory wrapper around the same inspection loop. Nothing in L0 names a protocol or a regulator.
- **Differently positioned**: a shop's DVI module (inside repair-shop software) satisfies the L0 for its inspection part — consistent with it being a module of another Type; a used-car pre-purchase inspection app satisfies it with the client-commissioned variant; a telematics vendor's automatic fault alerts do NOT satisfy it (no deliberate examination session — continuous monitoring, different Type).
- Conclusion: the L0 survives the historical and regional check; protocols, hardware, regulatory wrappers, and cloud features are implementation layers.

## Boundary Findings

1. **vs Auto Repair Shop Management (§29 sibling)**: the shop Type owns the business lifecycle — repair order, estimates/authorization, parts & labor, invoicing. Its DVI is this Type's core embedded as a module (templates, findings, photos, customer reports, declined-work follow-up). Test: remove the DVI from shop software and it remains shop software; add RO/billing to a scan tool and it becomes shop software. Standalone inspection/diagnostic products (consumer scan tools, fleet inspection apps) exist entirely without the business lifecycle. Verdict: real standalone Type; the shop module is an embedded instance. This **confirms and refines** the auto-repair sibling's "fragment" flag — fragmentary when embedded, standalone when sold to consumers/fleets.
2. **vs Fleet Management System (§18)**: FMS manages the vehicle population (assignments, fuel, cost, compliance) and embeds inspections (Fleetio evidence). Remove inspections from FMS → still FMS; an inspection product without population management is this Type. Standalone fleet-inspection vendors exist (Whip Around — access-blocked this session).
3. **vs Vehicle Telematics Platform (§18)**: telematics continuously streams from operating vehicles and can surface fault events; the diagnostic application runs **deliberate examination sessions** (connect → read → test → report) often on a non-operating vehicle. Fleetio explicitly integrates telematics for automatic maintenance triggers while keeping its inspection workflow manual/session-bound — evidence that the market itself treats these as different capture modes.
4. **vs Property Inspection Application (§29, processed)**: same inspection pattern (form → on-site examination → findings → report) but different object (real property vs vehicle) and, critically, the vehicle branch has an **electronics read-out mode** (reading the vehicle's own diagnostic systems) that property inspection lacks; property inspection is client-commissioned with fee-bearing orders, while vehicle inspection is usually not a client-commissioned engagement (pre-purchase inspection is the exception variant).
5. **vs Government Inspection Management (§24)**: public-sector inspection software manages inspection regimes across many object types (buildings, food establishments, vehicles); vehicle inspection/diagnostic software is object-specific and often private-side. Official roadworthiness inspection stations may use this Type's tools, but the regime machinery belongs to the government Type.
6. **Internal structure note**: the leaf's two halves (checklist inspection vs electronic diagnostics) are held together by one L0 abstraction (examine vehicle → structured capture → interpret → findings). The market mostly sells them separately (scan tools vs inspection apps), with professional shops using both (DVI + scan tool). Not a taxonomy conflict — but the final document must present both branches under one core, not pick one as "the real" Type.

## Uncertainties

- **Professional live-data depth**: Bosch product pages confirm actuations and scan reporting; live-data surfaces on pro tools were not directly article-verified (Tier-2 marketing depth). Treated as common for the electronic branch, not stated with precision.
- **BlueDriver article bodies**: not renderable; feature existence confirmed via collection/article titles and product page. No precise operational details (e.g., exact number of codes per make, exact monitor lists) claimed.
- **Fleet/inspection standalone market**: Whip Around (standalone fleet inspection product) unreachable; the fleet-inspection evidence comes from an FMS module. Standalone-ness of that segment is inferred from market structure, not directly documented here.
- **Used-car/dealer condition-report products**: not sampled (documentation access); the pre-purchase variant is asserted as a variant on market-knowledge grounds only — keep at variant strength.
- **Clearing-codes side effects**: readiness-monitor reset on clearing is evidenced (OBD Auto Doctor readiness "since DTCs cleared"; BlueDriver "Resetting Emissions Tests" article). Other side effects (freeze-frame erasure) not directly evidenced — not claimed.
- **Regional products outside NA/EU**: not sampled; OBD Auto Doctor provides European breadth only.

## Final Synthesis

A Vehicle Inspection / Diagnostic Application is an examination instrument for a specific vehicle: it captures the vehicle's condition through a defined structure — the vehicle's own self-reported data (fault codes, readiness monitors, sensor values, test results) and/or a human examiner's structured observations — interprets the capture against vehicle-specific reference knowledge (code definitions, specifications, repair procedures, pass/fail criteria), and surfaces the findings as its product: a readable result, a retained record, a shareable report. The defining core is deliberately minimal: vehicle subject, structured capture, vehicle-specific interpretation, findings output. Everything else scales with audience — code clearing and readiness guidance for the consumer; large offline code databases and sharing for the prosumer; OEM procedures, wiring diagrams, bi-directional actuation, and secure-gateway access for the professional; templated forms, photo evidence, failure alerts, work-order handoff, and compliance retention for managed fleet/shop operations. The Type ends where the money begins: recommendations and handoffs live here, but repair orders, parts, labor, and billing belong to Auto Repair Shop Management, and fleet population management belongs to Fleet Management System. Telematics watches vehicles continuously; this Type sits down with one vehicle and asks it questions.
