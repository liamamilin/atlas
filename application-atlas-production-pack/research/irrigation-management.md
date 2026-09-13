# Research Notes — Irrigation Management

Research date: 2026-09-08
Leaf: Irrigation Management (DIRECTORY.md §20 Agriculture, Food & Natural Resources)
Slug: irrigation-management

## Research Goal

Understand what software called "irrigation management" actually is in the market: what objects it holds, how the irrigation decision is produced and executed, how water status is represented, how execution and verification work, and where its boundary lies against the neighboring §20 Types (Agricultural IoT Platform, Crop Management, Greenhouse Management, Field Management, Precision Agriculture, Agricultural GIS) and against utility-side water software.

The two prior passes left mandatory joint-review flags to discharge in this pass:

1. agricultural-iot-platform vs irrigation-management — "gradient, not a wall… center of gravity = sensing backbone vs water decision; flagged for joint review when Irrigation Management is processed."
2. crop-management (and crop-protection-management follow-up) — single-domain siblings Irrigation/Nutrient/Soil Management are "probable superset/capability relationship… irrigation management ships as one solution inside another."

## Initial Boundary (working hypothesis before research)

- Core use: help a grower/farm/irrigation manager decide when, where, and how much to irrigate — and increasingly execute and verify that decision against equipment.
- Users: growers, farm managers, irrigation managers, agronomists/consultants, dealer/service experts; in surface-irrigation markets, also district/water-delivery operators at the edge.
- Nearest neighbors: Agricultural IoT Platform (device fleet center), Crop Management (whole-cycle center), Greenhouse Management (facility climate loop), Field Management (land-asset center), Precision Agriculture Platform (variable-rate prescription center), Water Utility Management (§19, utility side).
- Unknowns: Is scheduling definitional or only advisory? Is control/actuation definitional? Is water accounting definitional? Is fertigation inside or outside?

## Research Questions

1. What are the core objects (areas, zones/bays/sets, pivots, valves, pumps, sensors, programs, recommendations)?
2. How is water status represented (soil moisture probes, water balance/ET, satellite, expert-entered data)?
3. How is the irrigation decision produced (user-set, model-computed, advisor-mediated), and what does it contain (when / where / how much / how long)?
4. How does execution work (manual, remote control, automated programs), and is actual application recorded and compared against the plan?
5. What data sources feed the decision (on-farm sensors, weather stations, public weather, satellite, soil data)?
6. What role does water accounting/reporting play (usage history, season reports, compliance)?
7. Who uses it and how (grower self-serve vs dealer/expert-mediated service)?
8. Where does fertigation sit?
9. What alert/alarm behaviors matter?
10. Where are the boundaries vs neighboring Types?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different customer segments:

| Product | Vendor | Philosophy pole | Segment |
|---|---|---|---|
| Irrigation Scheduling + AgSense 365 | Valley (Valmont Industries) | pivot-manufacturer ecosystem: recommendation service + remote pivot/pump control | broadacre center-pivot farming, dealer-delivered |
| Irrigation Planning (CropX system) | CropX | independent sensor-driven agronomy platform; irrigation as one agronomic module | row crop + orchard, global, self-install sensors |
| GrowSphere™ OS | Netafim | drip/fertigation-centric closed loop; "operating system for precision irrigation" | specialty crops, orchards, protected crops, global |
| FarmConnect | Rubicon Water | surface/flood (gravity) irrigation automation: programs + gates + water orders | bay/surface-irrigation farms (AU, US West, LatAm), plus district networks |

Second pivot pole (Lindsay FieldNET) was attempted and abandoned (SPA shell; transport errors) — see Sources / limitations. Manna Irrigation (the pure sensor-free advisory pole) was attempted and abandoned (site unreachable). The advisory-only pole is nonetheless covered inside the sample: Valley's "Modeled" scheduling mode is recommendation-only (no probe, no control commitment), and CropX leads with recommendations.

## Sources

Tier 1/2 (official vendor pages and documentation, all fetched 2026-09-08):

- Valley Irrigation (Valmont) — product page "Irrigation Scheduling" https://www.valleyirrigation.com/scheduling ; product page "AgSense 365" https://www.valleyirrigation.com/precision-ag/agsense-365 ; site root https://www.valleyirrigation.com/
- CropX — site root/FAQ https://cropx.com/ ; product page "Irrigation Planning" https://cropx.com/cropx-system/irrigation-planning/
- Netafim — Digital Farming / GrowSphere page https://www.netafim.com/en/digital-farming/ ; site root https://www.netafim.com/
- Rubicon Water — site root https://www.rubiconwater.com/ ; FarmConnect Knowledge Base https://farmconnect.docs.rubiconwater.com/ ; "FarmConnect Irrigations and Irrigation Programs" https://farmconnect.docs.rubiconwater.com/space/FCD/2022375454.md ; "Types of Irrigation Program" https://farmconnect.docs.rubiconwater.com/space/FCD/2015625957.md

Unreachable sources (attempted 1–2 times each, then abandoned per network-limitation rule):

- Lindsay FieldNET — https://www.lindsaycorp.com/fieldnet (transport error), https://www.myfieldnet.com/ (JavaScript-only SPA shell, no content)
- Manna Irrigation — https://www.manna-irrigation.com/ and https://manna-irrigation.com/ (transport errors)
- University of Minnesota Extension irrigation scheduling page — 403 (planned historical-check source)
- Netafim NetBeat URL — 404 (NetBeat appears superseded by GrowSphere on netafim.com)

## Product Observations

### Valley (Irrigation Scheduling + AgSense 365)

Evidence layer A (direct, official product pages).

- Self-positioning: Irrigation Scheduling is "advanced irrigation management software that provides easy-to-understand irrigation recommendations based on real, scientific data about your soil, crop type, development stage, and automatically updated weather conditions."
- Two delivery modes (feature table):
  - **Modeled**: "Recommendations are developed from a proprietary algorithm… The algorithm calculates irrigation needs based on weather, soil, crop and other data entered into the application by an agronomy expert. There is no physical soil probe in the field."
  - **Measured**: "A certified dealer or agronomy expert connects soil moisture sensors and weather station devices in the field to your software, then monitors the results… to calculate your irrigation schedule."
- Shared features (both modes): "Continuous data access via Valley Scheduling web and mobile app"; "5- to 7-day irrigation forecast, updated daily"; "Professional monitoring of data and calibration by a service expert"; "Interactive BaseStation3 view (Available)"; "Site visits periodically during the growing season"; "Unlimited technical phone support"; "Season-end water report."
- Suite framing (numbered parts of one solution): 1. Irrigation Scheduling 2. Remote Irrigation Management (AgSense 365) 3. AgSense Aqua Trac (soil moisture tracking) 4. Irrigation Equipment ("ensures your scheduling decisions are executed accurately in the field") 5. Ongoing Training and Support (certified irrigation experts) 6. Variable Rate Irrigation 7. Valley Weather Station ("collect localized weather data… to improve the accuracy of irrigation recommendations").
- Decision presentation: "Input your field data and preferences, and the system calculates crop water needs—delivering recommendations in easy-to-read map or list views so you can plan and apply irrigation with confidence."
- Stress framing: "Track potential crop stress from over- or under-watering and make proactive adjustments."
- AgSense 365 (separate product page): "real-time remote monitoring, irrigation control, diagnostics, and agronomic insights into one powerful platform." Monitor & Control: "Precisely control irrigation application rates throughout the field. Optimize pump performance and water delivery remotely. Track soil moisture levels and weather conditions. Monitor flow and tank levels. Visualize historical water application data. Analyze water usage and generate customized reports." Forecast & Plan: Irrigation Scheduling recommendations. Optimize & Apply: VRI ("apply water where it's needed and in the amount required"). Machine Diagnostics: "Track runtime of each tower and send real-time alerts that pinpoint faults in alignment, tire pressure and water application. Stay on top of maintenance intervals."
- Compatibility claim: "Compatible with Any Pivot Brand."
- Channel: delivered through certified Valley dealers; login portal at agsense365.com.

### CropX (Irrigation Planning module of the CropX system)

Evidence layer A (direct, official product/FAQ pages).

- Module promise: "Save water and keep crops healthy by irrigating before plants show signs of stress. Know exactly when and how much water to apply. Track, compare and report irrigation practices."
- Feature list on module page: Field Map ("visual display of water fill levels in a field"); Soil Moisture Status ("quick reference of Refill, Optimal, or Full level status"); Variable Rate Irrigation ("match water rates with soil type or topography"); Profile Summary ("graphical view of water fill levels for past and future dates"); Irrigation Insights ("recommendations on when and how much to irrigate"); Actual Evapotranspiration (ETa) ("track field-specific crop water use over a broad area in real time").
- Decision logic: "tracking the Actual ET of a crop allows for irrigation practices that replace water used by that crop. Effectively managing water in the crop root zone…" ; "The irrigation management capability of CropX is continuously monitoring this data and providing insights and advice on irrigation activities for more precise water applications."
- Status bands: "Growers know at all times if a field is at, above, or below optimal moisture levels."
- Execution: "Make confident irrigation decisions, automate irrigation schedules and implement variable-rate irrigation… Real-time data, advice, and automation accessed from desktop or mobile devices."
- From root FAQ: software modules include "Monitoring crop water use and scheduling irrigations"; agronomic models include "Irrigation & water use models" and "sensor auto-calibration and auto-set-point detection models, for field capacity, wilting point, refill points"; connectivity page: "Irrigation Equipment — monitor and control irrigation equipment from the CropX platform"; partner connections include irrigation-control systems (Reinke, Talgil etc. per earlier ag-iot pass fetch, reconfirmed by connectivity framing).
- Sensor basis: soil sensors (moisture/temperature/EC/salinity at multiple depths), ET sensors (Surface Renewal method, correlated to Eddy Covariance by UC Davis researchers), weather stations, rain gauges, telemetry gateways.

### Netafim GrowSphere™

Evidence layer A (direct, official Digital Farming page).

- Self-positioning: "GrowSphere™ OS… makes it easy to operate your irrigation and fertigation"; "the first operating system (OS) for precision irrigation"; "a simple, intuitive and visual digital farming work tool that helps you plan and execute your irrigation plans with greater reliability, transparency, and less effort."
- Headline promise: "100% Certainty Your Crops are Getting the Irrigation & Fertigation You Planned" — "Whether you simply want to remotely control (and validate) valve open/closing, monitor the irrigation status of your fields in real-time, get timely alerts about irrigation or system management issues or generate monthly reports."
- Capability set: Monitoring ("Monitor soil, weather, crop, and irrigation status with real-time updates from your fields"); Crop Advisor ("Enhance your irrigation plans with recommendations tailored to crop stage"); Reporting ("Generate reports to support traceability and track crop performance from season to season"); Control ("Control your irrigation and fertigation systems – from anywhere"); Alert Notifications ("timely alerts about irrigation or system maintenance issues").
- Safety/interlock language: "Prevent non-logical hydraulic commands."
- Progression framing: "GrowSphere™ Fits Every Stage of Your Precision Irrigation Journey" — new to precision irrigation → manual > automation → experienced ("acts like a 'second eye' to ensure you are executing the optimal irrigation plans").
- Architecture: "connects your controller, to your sensors, to the cloud, to your smartphone"; "Offline or remote control."
- FAQ: "It automates valve control and supports data-driven decisions, so water and nutrients are applied exactly when and where they're needed"; "Track soil moisture, weather, and crop conditions in real time; Automate irrigation and fertigation plans; Receive alerts when conditions change; Generate reports and maintain traceability by field or block."
- Fertigation is inseparable from irrigation in this product (dosing portfolio "Dosing 5G" sibling).

### Rubicon FarmConnect

Evidence layer A (direct, official site + Tier-1 knowledge-base pages).

- Site positioning: FarmConnect is "surface irrigation automation technology [that] transforms traditional manual on-farm surface/flood irrigation practices… improving application efficiencies, reducing labor requirements while maximising yield potential."
- Portal flow (root page, numbered): "1 Sensor data indicates the optimal time to irrigate. 2 The farmer requests water via phone or mobile app. 3 NeuroFlo software checks network capacity and customer rights then approves or offers alternatives. 4 Instructions are sent by radio to regulators and the customer's farm supply point. 5 The farm supply point automatically delivers requested water… 9 The farmer's crops receive water at the optimal time, duration and flow."
- Tier-1 doc, Irrigations module: "The Irrigations module in FarmConnect Portal is where you can create programs to automate the operation of your bay gates, valves, pumps, or supply gates and view and manage the results of irrigation programs."
- Tier-1 doc, program types: time-based programs ("actions that happen at a specified time… open and close a gate at specified times") vs event-based ("sensor-driven") programs ("actions triggered by events… open or close a gate when the water level measured by a water level sensor in the supplying channel exceeds a certain value").
- Tier-1 doc, execution architecture: "When you synchronise a time-based program, the fixed program is loaded as presets into the individual gates and runs at the scheduled times. When you synchronise an event-based program, the program is loaded into the FarmConnect gateway which manages all the event processing and sends commands to the relevant devices."
- Tier-1 doc, lifecycle naming: program saved as "<Name> (Template)"; synchronized run copies appear in the "Program Executions" list as "<Name> (start) (finish)".
- Tier-1 doc, alarm gating: "A synchronized program does not mean that the devices in the program are clear of alarms that may prevent the program running as expected. Please check the Alarms page before synchronizing a program."
- Device taxonomy (doc section titles): Bay Gates and RiserDrives, Valves, Pumps, SmartMeters, Soil Moisture Sensors, Water Level Sensors, Weather Stations and Rain Gauges.
- Water accounting surfaces: "Irrigation History and Water Usage", "Bay Water Usage", "Graphing", "Program Executions Screen", "Manual Control", "Alarms", "Device Status".

## Cross-product Comparison

| Dimension | Valley | CropX | Netafim GrowSphere | Rubicon FarmConnect |
|---|---|---|---|---|
| Decision unit | fields under pivots; pivot as executable | fields; sensor sites | fields/blocks (plots) | bays/sites; gates as executables |
| Water-status representation | modeled (algorithm from entered weather/soil/crop) or measured (dealer-installed sensors); crop stress tracking | sensor soil moisture with named bands (Refill/Optimal/Full); ETa; water fill levels past & future | real-time soil/weather/crop/irrigation status from sensors+controllers | sensor events (water level, soil moisture); weather stations; time defaults |
| Decision object | irrigation recommendations (map/list), 5–7 day forecast updated daily; irrigation schedule | Irrigation Insights (when/how much); automated irrigation schedules | irrigation plans + Crop Advisor recommendations tailored to crop stage | irrigation programs (time- or event-based) + water order flow (district-connected) |
| Execution | via connected pivots/pumps (AgSense 365); any pivot brand | manual first; "automate irrigation schedules"; control irrigation equipment via platform/integrations | remote valve/pump control with validation; automated plans; offline control | automated gate/valve/pump programs; manual control fallback |
| Verification | historical water application data; water-usage reports; season-end water report | "Track, compare and report irrigation practices"; profile summary past/future | "(and validate)"; "second eye… executing the optimal irrigation plans"; monthly reports | Program Executions list; Irrigation History and Water Usage; Bay Water Usage |
| Equipment status | machine diagnostics (tower runtime, alignment/tire-pressure/application alerts) | device health module (installs, status, health of devices) | alerts on irrigation or system maintenance issues; prevent non-logical hydraulic commands | Alarms gating program sync; Device Status; battery checks |
| Water accounting | analyze water usage; customized reports; season-end report | track/compare/report practices; sustainability reporting module | traceability reports per field/block | irrigation history; bay water usage; flow meters/SmartMeters |
| VRI / variable rate | VRI speed/zone/prescriptions | VRI by soil type/topography | — (not on fetched pages) | — (surface irrigation) |
| Fertigation | nutrient-management framing for dairy effluent (via pivot application) | nutrition monitoring separate module | fertigation inseparable from irrigation (dosing portfolio) | — |
| Advisory/service layer | certified dealer + agronomy expert monitor and calibrate | dealer advice channel; agronomist-validated features | Netafim experts; "designed by irrigation & fertigation experts" | Rubicon support; district operators on the network side |
| Data sources | proprietary model, entered data, Valley weather station, Aqua Trac sensors | own + third-party sensors, satellite, machinery | own controllers/sensors (+ cloud) | water-level/soil sensors, weather stations, SmartMeters |
| Sales/delivery channel | dealer channel | direct + dealer network | Netafim projects/services + dealers | districts + farm projects |

Convergent findings across all four (B layer):

1. Every product centers identified irrigated areas (fields, blocks, bays) as the object decisions attach to.
2. Every product maintains a water-status/demand picture from some mix of sensors, weather data, models, or expert-entered data.
3. Every product produces a dated, area-bound irrigation decision (recommendation, schedule, or program) answering when / where / how much.
4. Every product has an execution story — manual application, remote control, or automated programs — though its depth varies from none (recommendation-only mode) to full automation.
5. Every product records what was actually applied and reports water usage (verification/accounting).
6. Alerts on irrigation-relevant conditions and equipment faults are universal.
7. Expert/dealer-mediated setup, calibration, and monitoring is a notable service model in at least three of four.
8. Mobile + web access is universal; map and list views of areas are the standard presentation.

Divergent findings (variant axes, not type structure):

- Data substrate: modeled-from-entered-data vs sensor-measured vs event-sensor vs satellite/ET.
- Control depth: recommendation-only → remote manual control → scheduled automation → event-driven automation.
- Application technology: center pivot, drip/micro, surface bays — the decision object is technology-agnostic; program semantics differ accordingly (run hours & application rates vs valve/shift programs vs gate opening times).
- Fertigation coupling: inseparable (drip pole) vs absent (surface/pivot poles).
- District coupling: water orders and network-capacity checks exist only in the surface-irrigation/district pole.
- VRI/prescriptions: present in pivot/sensor poles, absent elsewhere in sample.

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

Three jointly-held structures. If any one is removed, the product is no longer recognizable as Irrigation Management:

1. **The irrigated area as the decision unit.** Identified production areas — fields, zones, blocks, bays, pivots — carrying crop/soil context, to which all water decisions attach. Remove → a land/farm record or GIS substrate with no water decision; the areas exist but nothing is decided about water.
2. **The water-status and demand picture.** A maintained representation of water present and water needed per area — from soil-moisture sensing, weather/ET and water-balance models, satellite/imagery, or expert-entered observations. Remove → equipment remote control without agronomic grounding (a remote pivot/valve switch), or a weather/sensor dashboard.
3. **The irrigation decision.** A produced, dated, area-bound statement of when / where / how much to apply water — a recommendation the user accepts, a schedule the user edits, or a program the system executes. Remove → passive monitoring (falls to the Agricultural IoT pattern) or bare device control.

The decision loop (status → decision → application → updated status) is the heart; execution machinery is optional depth, not part of the invariant.

### L1 — Common Mature Structure

Present in essentially all mature sampled products; expected by the market but not definitional:

- execution through connected equipment: remote monitoring and control of pivots, pumps, valves, gates (varies from none to full automation)
- plan-vs-executed verification: recording what was applied and comparing with the plan
- water accounting: usage history per area/period, water reports (e.g., season-end), increasingly for compliance/traceability
- equipment/irrigation-system status and alarms (faults, missed or blocked runs, hydraulic anomalies)
- weather data integration (on-farm stations and/or public forecasts)
- map + list presentation of areas and their water status
- mobile + web access
- agronomic recommendation layer (when/how much), commonly calibrated by an expert
- multi-season data retention (status history, application history)

### L2 — Variant / Optional Structure

- variable-rate irrigation (VRI) prescriptions by soil/topography
- fertigation/nutrient dosing coupled to irrigation events (drip-centric pole; inseparable there, absent elsewhere)
- water-order workflows and district/network-capability checks (surface-irrigation districts)
- satellite/remote-sensing water-status inputs (ETa over broad area)
- event-driven ("sensor-triggered") automation vs time-based schedules
- expert-service delivery models (dealer/agronomist monitors and calibrates) vs self-serve
- application-technology specialization: pivot run-hour semantics, drip shift/valve semantics, bay/flood-gate semantics
- regulatory/compliance water reporting (regional)
- landscape/turf smart controllers share the abstract pattern but serve a different market and are not crop-production irrigation management

### L3 — Vendor-specific (Research Notes only)

- Valley: "Irrigation Scheduling" and "AgSense 365" brand names; Modeled/Measured service tiers; 5- to 7-day forecast, updated daily (documented for this product); BaseStation3; ICON panels; Aqua Trac; Pump Command; "compatible with any pivot brand"; certified-dealer delivery.
- CropX: Refill/Optimal/Full status bands (product naming); ETa via patented Surface Renewal method; sensor auto-calibration of field capacity/wilting point/refill points; third-party irrigation-control integrations (Reinke, Talgil etc.).
- Netafim: GrowSphere "OS" framing; "100% certainty"/"second eye" validation language; "prevent non-logical hydraulic commands"; Dosing 5G portfolio; NetBeat legacy product name.
- Rubicon: FarmConnect program synchronization into gate presets; event-based programming enabled via support; Program Executions naming convention; NeuroFlo/Total Channel Control district network; water-order approval flow with rights checking.

### Rejected Findings (anti-overfit)

- **Remote control is not definitional** — Valley's Modeled mode and CropX's advisory core function without it; recommendation-only irrigation management is a documented, marketed configuration.
- **Sensors are not definitional** — Valley Modeled runs "with no physical soil probe in the field"; classic water-balance scheduling runs on weather tables and entered data.
- **Pivots/sprinklers are not definitional** — FarmConnect is built for surface/flood bays; Netafim for drip. The Type is application-technology-agnostic.
- **The multi-day numeric forecast window is not definitional** — documented for one product; kept generic ("rolling multi-day forecast" at most) in the final document.
- **Fertigation is not definitional** — only the drip pole couples it inseparably.
- **Water-order/district machinery is not definitional** — regional/market variant.
- **Named status bands (Refill/Optimal/Full) are not definitional** — one product's vocabulary; the invariant is status evaluated against defined thresholds.

### Historical / Market-Sample Check (§24)

- The analog routine — a grower keeping a water-balance ledger from an evaporation pan/ET table and rain gauge, probing soil by hand, deciding "block X gets Y hours tomorrow," recording what was applied — satisfies all three L0 legs with no software, sensors, network, or cloud. Definition holds.
- Extension-service "checkbook" irrigation schedulers (paper/account-book method) hold areas, a water balance, and recommendations; they fit the definition without any equipment connection. (Source for this class of tool was unreachable in this pass; the check is conceptual, consistent with prior passes' treatment of analog lineages.)
- A non-networked pivot control panel schedules a machine but holds no water-status picture and no area-bound water decision — it is equipment control, not irrigation management. Consistent with the boundary: control without the decision layer is outside the Type.
- The definition names no hardware kind, protocol, sensor type, cloud, AI, or business model; all eras and poles fit.

## Boundary Findings

1. **vs Agricultural IoT Platform** (flag from agricultural-iot-platform pass — now jointly reviewed): the IoT platform centers the device fleet and the telemetry/monitoring loop; irrigation management centers the water decision. Structural test re-confirmed on this pass's sample: remove the device fleet and irrigation management still stands (Valley Modeled: "no physical soil probe"; FarmConnect time-based programs run on schedules; classic water-balance scheduling on weather data alone); remove the irrigation decision and the IoT platform still monitors frost, pest, disease, and climate. Overlap is real — irrigation management commonly *consumes* IoT sensing and may *drive* irrigation equipment — but the center of gravity separates them. Flag discharged, boundary held: two Types.
2. **vs Crop Management** (flag from crop-management pass — now jointly reviewed): crop management centers the whole crop cycle (the crop-season record spanning planting→harvest); irrigation management centers one input domain — the water decision — with its own data substrate, decision machinery, and execution loop. The superset/capability relationship is confirmed: irrigation management ships as one module/solution inside broader agronomy platforms (CropX irrigation module inside the CropX system; Semios irrigation solution inside its monitoring platform, per prior passes) *and* exists as standalone products (Valley Irrigation Scheduling, Netafim GrowSphere, Rubicon FarmConnect). Flag discharged, boundary held: sibling Type with a documented module/superset gradient.
3. **vs Greenhouse Management**: the greenhouse pass held irrigation scheduling as standard-not-definitional there. Greenhouse management centers the enclosure's climate-and-water control loop across zones (heating/venting/lighting/CO₂/irrigation together); irrigation management centers the water decision for irrigated production areas and is enclosure-agnostic. Drip/fertigation control inside greenhouses can live in either; boundary = facility operating loop vs water decision.
4. **vs Field Management**: field management centers the land asset (boundaries, soil, layout); irrigation management attaches water decisions to areas. Irrigation zones may appear as attributes in field management and as layers in Agricultural GIS, but the decision loop is not there.
5. **vs Precision Agriculture Platform**: PA centers variable-rate prescription generation/execution across inputs (seed, fertilizer, water); irrigation management centers the water decision. VRI prescriptions are a variant capability inside irrigation management, not the center.
6. **vs Agricultural GIS**: irrigation zones/prescriptions live as map layers in GIS; GIS centers spatial data, not the recurring water decision loop.
7. **vs Water Utility Management (§19)**: utility side manages the network, customers, and billing of water; the farm side manages crop water decisions. Rubicon spans both (district network control + farm automation), which documents the seam rather than dissolving it.
8. **vs Farm Equipment Telematics**: pivot/pump diagnostics appear inside irrigation management as a common capability; telematics centers machine-fleet health across all equipment, not the water decision.
9. **vs landscape/turf smart irrigation controllers** (no directory leaf): same abstract pattern (zones, weather-based scheduling, valve control) but users are property/landscape managers, context is landscape maintenance, not crop production; kept adjacent, outside the canonical context of this §20 leaf.

## Uncertainties

- FieldNET (the other major pivot-ecosystem product) could not be fetched; pivot-ecosystem convergence rests on Valley alone within this pass, though it is corroborated by the prior ag-iot pass's third-party integration evidence (WiseConn/Nelson/FieldNET integrations referenced by Semios/CropX) and by Reinke's existence in that market. Assertion strength kept at "common implementations include remote pivot control" (B layer), not universal.
- Manna (pure satellite-advisory pole) unreachable; the advisory-only configuration is evidenced via Valley Modeled and CropX advisory framing instead — adequate but not from the specialist sensor-free vendor.
- Whether *all* irrigation-management products record applied water could not be confirmed for the advisory-only pole beyond Valley's season-end water report (which is included even in Modeled mode — evidence that accounting reaches deep into the advisory pole). Kept in L1 rather than L0.
- Event-based program enablement (Rubicon) is support-gated per docs; prevalence of event-driven automation market-wide unknown.
- NetBeat's exact relationship to GrowSphere (succession confirmed only by URL retirement) — treated as vendor product-line detail, not used in the final document.

## Final Synthesis

Irrigation Management software is the grower-side water-decision system: it holds the farm's irrigated areas as decision units, maintains a current and forward-looking picture of water status and crop water demand for each area, and turns that picture into dated, area-bound irrigation decisions — recommendations, schedules, or programs — that are applied manually or executed through connected equipment, with what was actually applied recorded back against the plan. The defining core is exactly the decision loop (status → decision → application → updated status) anchored on irrigated areas; the sensing substrate, the application technology, control depth, fertigation, water orders, and service models are variant axes. Sensing is the IoT platform's center, the whole crop cycle is crop management's center, the enclosure loop is greenhouse management's center — the water decision itself is this Type.
