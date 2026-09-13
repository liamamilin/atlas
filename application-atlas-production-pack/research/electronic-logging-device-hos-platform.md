# Research Notes — Electronic Logging Device / HOS Platform

Research date: 2026-09-08

## Research Goal

Determine what an "Electronic Logging Device / HOS Platform" is as an Application Type: its core objects (duty-status log, clocks, rulesets, edits, inspections), who uses it, how the daily compliance loop works, and its boundaries against Fleet Management System, Driver Management, Vehicle Telematics Platform, Trucking Management System, and generic Time & Attendance systems.

## Initial Boundary

The leaf sits in DIRECTORY.md §18 between Driver Management and Trucking Management System.

Working hypothesis (to verify, not assert):

- ELD = the in-vehicle device/surface that automatically records driving time (in the US, a FMCSA-regulated device category).
- HOS Platform = the software side: duty-status logging, hour computation against regulatory rule sets, violation alerting, log edit governance, and inspection-facing recordkeeping.
- Neighbors that must not absorb it: Fleet Management System (asset-centered), Driver Management (person-centered entitlement — ratified 2026-09-07 in the driver-management pass: "ELD/HOS centers on duty-status logging against hours regulations; the driver is the subject of the log"), Vehicle Telematics Platform (data transport), TMS (freight), Time & Attendance (payroll time).

The fleet-management-system pass already observed that HOS/ELD compliance appears inside FMS suites as a "Compliance" dashboard module — so the seam is Type vs suite-module, and the same vendors sell both.

## Research Questions

1. What objects exist in the system world? (duty status, log/RODS, driver, vehicle, ruleset/cycle, clocks, edits, inspections, DVIR, unidentified driving)
2. How is driving time captured — device/ECM vs app-only? What is the ELD vs electronic-logbook mode distinction?
3. What are the standard duty statuses and special statuses (personal conveyance, yard move, waiting time)?
4. How do violation clocks work (break / drive / shift / cycle) and how do rule sets get assigned per driver?
5. What is the log edit lifecycle (driver vs carrier, remarks, re-certification, unaltered originals)?
6. What regulatory-facing machinery exists (certification, roadside inspection, data transfer, malfunction/diagnostics)?
7. Which regional regimes and exemptions are handled (US federal/state, Canada federal/provincial, exceptions: short-haul, adverse, agriculture, oilfield, utility)?
8. Where are the seams vs FMS / Driver Management / TMS / Time & Attendance / tachograph ecosystem?

## Representative Products

Chosen for market representativeness, documentation quality, and different product philosophies:

| Product | Philosophy / segment |
|---|---|
| Motive (formerly KeepTruckin) | ELD-native, driver-app-first compliance platform grown into fleet ops (trucking-heavy, SMB→enterprise) |
| Samsara | Telematics-platform suite where ELD/HOS is the Compliance pillar (broad fleet, mid-market→enterprise) |
| Geotab | Open telematics platform; HOS delivered through the Geotab Drive driver app / MyGeotab compliance layer (observed via the fleet-management-system sibling pass) |

FMCSA (the US regulator) was targeted as a definitional Tier-1 source but returned HTTP 403; the regulatory frame below is reconstructed from vendor documents that cite the specific regulations directly.

## Sources

- Motive Help Center (Zendesk API, worked):
  - "Hours of Service" — https://helpcenter.gomotive.com/hc/en-us/articles/30810628869405-Hours-of-Service
  - "Difference between the Motive Driver App and the Vehicle Gateway" — https://helpcenter.gomotive.com/hc/en-us/articles/6173250355613
  - "Drivers Exempt from the ELD Rule – FMCSA Guidelines" — https://helpcenter.gomotive.com/hc/en-us/articles/14720399809949
- Samsara Help Center (kb.samsara.com Zendesk API, worked):
  - "Edit an HOS Log" — https://kb.samsara.com/hc/en-us/articles/360043215192-Edit-an-HOS-Log
  - "HOS Dials in the Driver App" — https://kb.samsara.com/hc/en-us/articles/360043178192-HOS-Dials-in-the-Driver-App
  - Search result inventory of the HOS Compliance driver section (titles only): Roadside Inspection, Transfer Logs, Certify Your Logs, Review Carrier Edits, Set a Personal Conveyance (PC) Duty Status, Set a Yard Move Duty Status, Set the Split Sleeper Toggle, Team Driving, Unauthenticated Driving, HOS Violation Push Notifications, HOS Configuration Changes, Vehicle Regulation Modes for Mixed-Use Vehicles, Claim the Adverse Driving Exemption, Claim the Utility Service Vehicle Exemption, Defer Off-Duty Time, Change Your HOS Cycle (Canada), Understanding the Canada South HOS Daily Violation, Review Cumulative Hours, Go Off Duty, DVIR articles
- Geotab: observed via research/fleet-management-system.md (Geotab Drive driver app: HOS status page, HOS logs incl. editing, roadside checks, inspections, co-drivers)
- FMCSA ELD overview page (https://www.fmcsa.dot.gov/hours-service/elds/electronic-logging-devices) — **not reachable** (HTTP 403)
- Geotab docs (docs.geotab.com), Verizon Connect fleet support, BigRoad support — **not reachable** (transport errors / portal redirects; abandoned per retry limit)

Access limitation: two of the three sampled vendors' own article content was obtained; Geotab's HOS evidence is second-hand (sibling pass). Regulator content was not directly reachable. Precise regulatory numbers below are quoted as **vendor-cited** facts, not verified against the regulator.

## Product A — Motive

Layer A (directly observed from Motive help articles):

- **Two-part architecture**: the Vehicle Gateway is a hardware device connecting to the vehicle's ECM via the diagnostic port; with the Driver App it "automatically records driving time in compliance with US DOT / FMCSA rule 395.15". The Driver App alone is "a fully editable electronic logbook" compliant with rule 395.8 (RODS) and Canada's HOS regulations — i.e., the platform supports an **app-only logbook mode** for drivers not required to run a certified ELD.
- **Compliance mode per driver**: "ELD or Electronic Logbook (for ELD-exempt drivers)" is a driver-profile setting; other profile settings: HOS cycles (primary + secondary), home terminal time zone, odometer units, special-duty-status permissions.
- **HOS clocks**: four clocks in the Driver App — Break, Drive, Shift, Cycle — "automatically show how much time a driver has left under each HOS limit". Fleet managers can view each driver's clocks in the Fleet Dashboard (Driver Summary).
- **Cycles/rulesets**: all standard US federal cycles (70-hour/8-day, 60-hour/7-day) and Canadian cycles (North/South 70-hour/7-day, 120-hour/14-day) plus select state/provincial rules (California, Texas, Florida, Alberta). Managers assign cycles per driver. **Auto rule-switching at the US–Canada border** when both cycles are set (product-specific as documented).
- **Exceptions**: adverse driving conditions (extend driving + on-duty window by up to 2 hours, only when conditions were not known at trip start), 16-hour short-haul, agriculture (off-duty within 150 air-miles), oilfield waiting-time status.
- **Special duty statuses**: Personal Conveyance (off-duty personal use of a CMV; not counted against limits) and Yard Move (movement in a private area; counts as on-duty, not driving). Both must be **enabled by a fleet manager** per driver before use.
- **Regulation-mode per vehicle**: a vehicle can be set "Unregulated (Non-CMV)" so its trips are not treated as ELD-regulated driving.
- **Logging is unconditional**: even with 0 available hours, the system must create and retain a daily log, which must be **signed to certify accuracy**; HOS logging is driven by the vehicle's regulation mode, not by remaining hours.
- **Driver App capabilities**: change duty status, enable break, create a daily vehicle inspection report (DVIR), add co-drivers, claim and reject unidentified trips.
- **Exemptions documented** (vendor-cited to 49 CFR § 395): short-haul (100 air-mile CDL / 150 air-mile non-CDL radius, return daily, ≤8 days RODS in 30), driveaway-towaway, pre-2000 engine model years, drivers using paper logs ≤8 days in 30. Exempt-driver profiles can be marked as exempt in the ELD configuration to avoid unidentified-driver/diagnostic errors.
- **Suite adjacency**: Safety, Fuel & expense Cards, TMS/marketplace integrations — separate pillars, not HOS.

## Product B — Samsara

Layer A (directly observed from Samsara KB articles):

- **HOS dials (clocks)**: four dials in the Driver App for US fleets — Break, Drive, Shift, Cycle — explicitly described as remaining time toward HOS limits; **dials reflect the most constraining limit** (e.g., cycle shorter than daily cap drives the dial). Canada fleets get a different dial set (Drive, On Duty, Total Shift, Off Duty, Cycle) with region-specific counts.
- **Violation states are visual and push-based**: dial rings color-coded blue (no violation) / yellow (nearing) / red (in violation); popup notifications when nearing limits; "HOS Violation Push Notifications" and "Managing HOS Violations" as admin/driver workflows.
- **Edit governance (Layer A, detailed)**: per the ELD mandate, start/end times of **automatically recorded drive time cannot be edited**; manual entries can be edited with a mandatory **remark**; editing a certified log requires **re-certification** ("Agree – Save and Re-certify"); admins can enable editing of certified logs as a setting; converting Personal Conveyance / Yard Move to a non-driving status **must be done by a fleet administrator**, not in the app. Log access windows are regulated and region-dependent (US up to 8 days in-app; Canada 15; older/pending-edit logs up to 184 days viewable — vendor-precise numbers).
- **Certification**: "Certify Your Logs" driver workflow.
- **Roadside inspection + Transfer Logs**: driver-side inspection workflows exist as first-class articles.
- **Special statuses**: Personal Conveyance, Yard Move, Split Sleeper toggle, Defer Off-Duty Time (Canada), adverse-driving and utility-service-vehicle exemption claims.
- **Unidentified driving**: "Unauthenticated Driving" workflow (driver identity for vehicle movement not yet assigned).
- **Team driving**: co-driver workflow ("Team Driving").
- **Regulation modes**: "Vehicle Regulation Modes for Mixed-Use Vehicles" — vehicles can be regulated or not, per configuration.
- **DVIR bundled**: driver app DVIR workflows (including a "DVIR 2.0" iteration).
- **Regional handling**: Canada North/South cycles, Canada-specific violation explanation articles, "Change Your HOS Cycle (Canada)".
- **Manager side**: "Admin Dashboard: Editing HOS", "Managing HOS Violations" — carrier-side log edit and violation management exist as admin surfaces.

## Product C — Geotab

Layer A via sibling pass (research/fleet-management-system.md, researched 2026-09-06/07): Geotab Drive (driver app) exposes: login, selecting/removing vehicles and trailers, **HOS status page, HOS logs (including editing a log), roadside checks, asset inspections (performing, certifying previous, repairing defects), co-drivers, messaging**. MyGeotab (manager side) carries HOS ruleset setup and HOS logs among compliance reports. Provenance caveat: this pass did not fetch Geotab docs directly (docs.geotab.com unreachable); observations are inherited from the FMS pass.

## Regulator Frame (as cited by vendors — Layer A for the citations, not the regulator)

- US: FMCSA rule **395.15** (ELD automatic driving-time recording) and **395.8** (Record of Duty Status) — cited verbatim in Motive's device/app article. Samsara states "Per the ELD mandate, you cannot edit start or end times for automatically recorded drive time."
- ELD exemptions (Motive-cited to 49 CFR § 395.1(e), § 395.8(a)(1), § 395.22(h)): short-haul radius drivers, driveaway-towaway, pre-2000 engines, ≤8-days-RODS drivers; exempt-driver ELD profile configuration is itself specified in the ELD technical spec.
- Canada: commercial vehicle drivers' HOS regulations explicitly supported (Motive app-only mode claims Canadian compliance; both vendors carry Canada North/South cycles and Canada-specific articles).

## Cross-product Comparison

| Structure | Motive | Samsara | Geotab (via FMS pass) | Evidence |
|---|---|---|---|---|
| ECM-linked in-vehicle device ("Vehicle Gateway" class) | ✔ (diagnostic port, rule 395.15) | ✔ (Vehicle Gateway hardware) | ✔ (GO device family) | A (multi) |
| Driver app as primary logging surface | ✔ Driver App | ✔ Driver App | ✔ Geotab Drive | A (multi) |
| Duty-status vocabulary (driving / on-duty / off-duty / sleeper-berth) | ✔ (statuses incl. off-duty/on-duty-not-driving/driving) | ✔ (Off Duty / Driving / On Duty dials + sleeper split toggle) | ✔ (HOS logs) | A/B |
| Four regulatory clocks: break / drive / shift / cycle | ✔ named exactly | ✔ named exactly (US; Canada differs) | (not observed at dial level) | A (two products) |
| Clocks show remaining time + violation states | ✔ (red clock icon on driver profile; violation catching "early") | ✔ (color rings + push notifications) | (not observed) | A (two products) |
| Per-driver ruleset/cycle assignment | ✔ primary+secondary | ✔ cycle change workflows | ✔ (HOS rulesets in MyGeotab) | A (multi) |
| Governed edit workflow w/ remarks + re-certification + unaltered auto-recorded drive time | ✔ (log editing; certified-log signing) | ✔ detailed | ✔ (editing a log) | A (multi) |
| Certification / signing of daily logs | ✔ (even empty days signed) | ✔ ("Certify Your Logs") | ✔ (certifying inspections/logs) | A (multi) |
| Roadside inspection / transfer | (ELD inspection machinery implied; not fetched) | ✔ explicit articles | ✔ (roadside checks) | A (two products) |
| Special statuses: personal conveyance, yard move | ✔ (manager-enabled) | ✔ (manager-gated edits) | (not observed) | A (two products) |
| Exemption/exception machinery | ✔ (short-haul, adverse, agriculture, oilfield) | ✔ (adverse, utility, defer off-duty) | (not observed) | A (two products) |
| Unidentified/unauthenticated driving claims | ✔ (claim/reject unidentified trips) | ✔ (Unauthenticated Driving) | (not observed) | A (two products) |
| Co-driver / team driving | ✔ | ✔ | ✔ | A (multi) |
| DVIR bundled | ✔ | ✔ | ✔ (inspections) | A (multi) |
| Vehicle regulation mode (regulated vs non-CMV) | ✔ | ✔ | (not observed) | A (two products) |
| Border/region rule switching | ✔ (auto US↔Canada, product-specific detail) | ✔ (Canada cycles; region-based dials) | (not observed) | A |
| Manager-side compliance dashboard w/ driver clocks + violations | ✔ (Driver Summary, red clock) | ✔ (Managing HOS Violations) | ✔ (MyGeotab HOS reports) | A (multi) |
| Suite adjacency (safety/cameras, fuel/IFTA, maintenance, dispatch, cards) | ✔ | ✔ | ✔ | A (multi) — NOT core |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant (four jointly-held structures)

1. **The duty-status log of record** — a persistent, time-stamped, per-identified-driver record of duty statuses over time (driving / on-duty not driving / off-duty / sleeper berth, plus status remarks and locations), the RODS lineage. Remove → generic time tracking or a telematics event feed; the product is no longer an ELD/HOS system.
2. **Vehicle-derived driving-time capture** — in the mandated ELD mode, driving time enters the log from the vehicle itself (engine/ECM-linked device), not from driver self-report; edits cannot falsify auto-recorded drive segments. Remove → a plain electronic logbook / attendance app. (Documented degradation: platforms also offer a manual-entry **electronic-logbook mode** for exempt drivers — evidence Motive; the automatic mode is what makes the ELD.)
3. **Regulation-clock computation** — remaining break / drive / shift(window) / cycle time continuously computed against the driver's assigned rule set, with violation/nearing states surfaced before they happen. Remove → an activity log with no hours-of-service meaning.
4. **Compliance-record character** — the log is a legal record: driver certification/signing, governed edit workflow (remarks, re-certification, preserved originals, carrier/driver role split), and inspector-facing display/transfer. Remove → an internal productivity tool whose records carry no regulatory force.

Jointly-held is load-bearing: 1+3 without 2 = a self-reported time tracker; 2 without 1+4 = telematics motion data; 1+2 without 3 = a passive recorder (pre-rule AOBRD-era data logger, no clocks); without 4 the record is not a compliance artifact.

### L1 — Common Mature Structure

- Driver App surface: duty-status switcher, daily log grid/graph, clocks/dials, certification, inspection mode
- Manager dashboard: per-driver clock status, violation management, log review, edit-approval side
- DVIR (driver vehicle inspection reports) bundled alongside HOS
- Unidentified-driving claim/reject; co-driver support
- Alerting: nearing-limit warnings, violation push notifications, manager violation queues
- Exception/claim workflows: adverse driving, short-haul, industry exceptions
- Special duty statuses: personal conveyance, yard move (manager-enabled)
- Rule library: US federal + state, Canada federal + provincial cycles; per-driver primary/secondary rulesets
- ELD self-test / diagnostics / malfunction handling (referenced by both vendors' troubleshooting sections)
- Vehicle regulation modes (regulated vs non-CMV mixed fleets)

### L2 — Variant / Optional Structure

- Compliance posture: certified ELD vs electronic-logbook (exempt drivers) vs AOBRD legacy posture
- Regional regime: US FMCSA (49 CFR 395), Canada (federal + provincial, North/South), state/provincial cycle variants; EU tachograph ecosystem is a separate regulated-device family (different hardware/legislation) — recorded as an open boundary question
- Hardware form: bundled telematics gateway vs standalone ELD; BYOD app pairing vs fixed display
- Industry tuning: long-haul trucking vs local/delivery vs energy/utilities (oilfield waiting time, utility vehicle exemptions) vs agriculture
- Fleet scale and mixed regulated/unregulated vehicle populations
- Bundled-adjacent modules: IFTA/fuel taxes, maintenance, safety/cameras, dispatch, expense cards (suite territory — optional)

### L3 — Vendor-specific (Research Notes only)

- Motive: "Vehicle Gateway" naming; Driver Summary cards; automatic US–Canada border rule switching with optional border-crossing remark; 16-hour exception invocation via "+ Take 16-hour exception" in app; "Unregulated (Non-CMV)" vehicle setting; shipping-document field with no global disable
- Samsara: "HOS dials" terminology; color-ring state model (blue/yellow/red); most-constraining-limit dial adjustment; DVIR 2.0; precise log access windows (8/15/184 days as vendor-stated); QR-code/ID-card driver assignment hardware options
- Geotab: GO device + Geotab Drive + MyGeotab three-surface architecture; open marketplace/SDK ecosystem

## Vendor-specific Findings

- Motive's automatic border-cycle switching is product-specific as documented (only vendor observed claiming it).
- Samsara's "dials reflect the most constraining limit" adjustment is product-specific as documented.
- Both vendors sell wide fleet-ops suites around the HOS core; the HOS/ELD core itself is structurally stable across them.

## Rejected Findings

- "ELD = a specific hardware form factor" — rejected. Motive documents an app-only electronic-logbook compliance mode; the hardware ECM link defines the mandated ELD mode, not the Type's entire realization. Automatic capture remains L0 for the ELD mode.
- "GPS/location tracking is core" — rejected. Location/remarks appear in logs (regulator-required context) but continuous telematics tracking is the telematics/FMS domain; not definitional here.
- "IFTA/fuel tax is part of HOS" — rejected. Observed only as adjacent suite module (FMS pass: IFTA lives in Fuel/Reports pillars).
- "DVIR is part of the HOS definition" — rejected as definition; accepted as common mature bundling (multi-product).
- "HOS platforms dispatch freight" — rejected; freight/loads belong to TMS/dispatch (driver-management pass boundary, re-confirmed here).

## Boundary Findings

- **vs Fleet Management System**: FMS centers on the vehicle as asset (maintenance, fuel, utilization, location); HOS/ELD centers on the driver's duty time as a compliance record. In practice the same suite sells both (Samsara "Compliance" pillar inside the FMS dashboard; Motive grown from ELD into ops suite). Removal test: strip duty-status logging from an FMS and it still manages vehicles; strip vehicle maintenance from an ELD/HOS platform and the compliance core is intact. Distinct Types in a suite relationship.
- **vs Driver Management**: ratified from this side — Driver Management centers on the person's qualification/entitlement (license, checks, remediation); ELD/HOS centers on the duty-time record the person produces. HOS data may feed risk scoring; it is not the qualification record.
- **vs Vehicle Telematics Platform**: telematics is the data-transport/telemetry layer (location, diagnostics, behavior); the ELD/HOS platform consumes vehicle data to produce a regulated compliance record with clocks. An ELD without clocks/record-governance would collapse into telematics.
- **vs Trucking Management System / Dispatch**: TMS centers on loads, carriers, settlements; HOS clocks are inputs dispatchers watch, but freight workflow is not this Type.
- **vs Time & Attendance / HR time tracking**: T&A records worked time for payroll against shifts; HOS logs duty *statuses* for safety regulation against legal limits, with vehicle-derived driving capture and inspector-facing record governance. Different object vocabulary (duty status vs clock-in), different audience (regulator/inspector vs payroll), different capture (ECM vs timesheet).
- **vs EU tachograph ecosystem**: the EU smart tachograph + card-analysis software is a sibling regulated-record family. Whether it is a regional variant of this Type or a separate Type is an open taxonomy question (no tachograph leaf exists in DIRECTORY.md). Recorded in STATUS Boundary Issues.
- **Removal criterion**: remove the duty-status log → time tracking; remove vehicle-derived capture → manual logbook app; remove clocks/rulesets → passive recorder; remove compliance governance (certification/edits/inspection) → internal productivity tool. Only the four together are the Type.

## Historical / Market-Sample Check

- **AOBRDs (pre-mandate automatic on-board recording devices, legacy US)**: satisfy legs 1, 2, 3, 4 — automatic recording + clocks + recordkeeping — with older rule details. Fit the definition.
- **Paper logbooks (RODS on paper)**: satisfy legs 1 (status record), 3 (manual clock arithmetic), 4 (certification, inspection presentation) but not leg 2 (no automatic capture). A paper logbook is the *record lineage* this Type digitizes, not an instance of the Type — consistent: the leaf names an *electronic* logging device.
- **App-only electronic logbooks for exempt drivers (Motive mode)**: degrade leg 2 to manual entry while keeping the platform's clocks and record governance; treated as a documented in-Type posture for drivers outside the mandate, not a separate Type.
- **Regional check**: Canada cycles/regimes fully represented in both sampled products; EU tachograph world differs in hardware law but shares the same four-leg structure at the software layer (card data, clocks, governed records) — plausible variant, evidence not gathered in this pass.
- Conclusion: the four-leg core survives the historical and regional check without over-fitting to the current US-mandate implementation.

## Uncertainties

- Geotab's HOS detail is inherited from the sibling FMS pass, not directly fetched this pass (docs.geotab.com unreachable).
- FMCSA regulator pages unreachable (HTTP 403); regulation numbers/limits are vendor-cited, not regulator-verified.
- Roadside-inspection transfer mechanics (web services/email/USB etc.) and ELD file formats were not directly documented in fetched articles; asserted only at "inspector display/transfer exists" strength.
- Motive's log-edit workflow article was not fetched directly (edit governance observed via certification/signing statements + Samsara's detailed article); Motive edit specifics remain approximate.
- Verizon Connect, BigRoad, and other ELD vendors were not reachable; sample rests on two directly-documented vendors + one sibling-observed.
- EU tachograph software not researched; boundary recorded as open.

## Final Synthesis

An Electronic Logging Device / HOS Platform is the operator-side compliance system that produces and maintains **the commercial driver's duty-status record of hours**. Its world is organized around four jointly-held structures: the per-driver duty-status log of record; vehicle-derived automatic capture of driving time in the mandated ELD mode; continuous computation of remaining break/drive/shift/cycle time against each driver's assigned rule set with violation states surfaced in advance; and compliance-record governance (certification, governed edits with preserved originals, and inspector-facing display/transfer). Everything else — DVIRs, unidentified-driving claims, co-drivers, special statuses, exemption libraries, regional cycle catalogs, and the surrounding telematics/safety/maintenance suite — is common mature structure or optional bundling. The Type is the compliance sibling of Fleet Management (asset-centered) and Driver Management (person-entitlement-centered): all three share vendors and data, but the system of record here is the driver's log of duty time.
