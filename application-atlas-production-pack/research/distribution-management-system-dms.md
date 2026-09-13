# Research Notes — Distribution Management System / DMS

## Research Goal

Understand what "Distribution Management System / DMS" (§19, Energy, Utilities & Telecommunications) is as an Application Type, given a difficult naming situation:

- The sibling leaf **Advanced Distribution Management System / ADMS** (processed 2026-09-06) pre-hung a joint-review flag: "the researched market uses 'ADMS' as the umbrella term for the integrated platform (SCADA + DMS applications + OMS on one network model/UI); every sampled vendor markets 'ADMS' for the integrated whole and Oracle's own guide is titled 'ADMS Implementation Guide' while the applications layer keeps DMS-style names (power flow, FLISR, VVO) — probable supertype/alias relationship; flagged for joint review when DMS is processed."
- The **grid-operations-platform** pass (processed 2026-09-08) documented the control-room family map and named this leaf as an unprocessed member ("ADMS/DMS+OMS — distribution trouble/switching loop"); this pass must treat that document as counterparty.
- The **SCADA** (2026-09-09), **EMS** (2026-09-08), **OMS** (2026-09-09), and **DERMS** (2026-09-07) passes have already seamed the family; this pass must ratify or refine from the DMS side.

The central question: is DMS (a) an alias/historical name of ADMS, (b) a distinct strand of the control-room family with its own load-bearing core, or (c) a capability below the Type threshold?

## Initial Boundary

Working hypothesis at start: DMS is the **network-analysis strand** of the electric-distribution control-room family — the connected distribution network model plus electrical analysis applications (power flow, state estimation, fault analysis, FLISR, Volt/VAR, load forecasting) computed on that model — historically the name of the whole distribution control platform, today usually the applications layer inside an ADMS, with a standalone engineering-analysis product population still alive at the co-op/mid-market pole.

Nearest Types: ADMS (integrated real-time platform), SCADA (point-based telemetry/control substrate), OMS (outage-response loop), EMS (same pattern at transmission), DERMS (DER fleet layer), Utility GIS (as-built model of record), grid-operations-platform (family umbrella).

## Research Questions

1. What do products explicitly branded "DMS" contain today? Is "DMS" a standalone product population, a module family, or only a legacy name?
2. What is the minimum structure a DMS must have — and does it require real-time SCADA telemetry, supervisory control, or an operational event loop (the ADMS differentiators)?
3. What is the canonical application suite, and which single computation is the founding/minimum one?
4. Does a standalone (non-ADMS-embedded) DMS product population exist? At what customer tier?
5. Where do the boundaries run vs ADMS, SCADA, OMS, EMS, DERMS, Utility GIS — and what is the discharge of the ADMS pass's alias flag?
6. Historical check: do older/regional products (pre-SCADA-integration engineering analysis, mainframe-era load-flow studies) satisfy the core?
7. Name-collision guard: which other "DMS" product worlds exist (dealer management, logistics distribution) and must be kept separate?

## Representative Products

Selection logic: market representation across the family's packaging poles (DMS-branded module family / standalone engineering analysis / enterprise integrated suite), different customer tiers (co-op/muni vs large utility), and documentation accessibility. CYME (Eaton) was selected as a fourth engineering-analysis pole but was unreachable (timeout ×2: eaton.com, cyme.com) and was abandoned per network rules; the engineering-analysis pole is covered by Milsoft.

| Product | Vendor | Pole | Evidence |
|---|---|---|---|
| SurvalentONE DMS application family (DPF/DSE, load forecasting, FLISR/LOV, VVO, contingency analysis, fault location, protection settings, demand-response applications) | Survalent | DMS-branded module family beside SCADA and OMS; mid-market/co-op | Tier 2 product pages, fetched this pass |
| Milsoft Engineering Analysis (WindMil, LightTable, LandBase, Computer Aided Contingency Analysis, AEON) | Milsoft | Standalone distribution engineering analysis; co-op/public-power pole | Tier 2 product pages, fetched this pass |
| AspenTech OSI ADMS (DMS as named integrated component) | AspenTech | Enterprise integrated suite; DMS referenced as a component beside SCADA and OMS | Tier 2 product page, fetched this pass |
| Oracle Utilities Network Management System (DMS applications layer) | Oracle | Enterprise integrated platform; Tier-1 documentation | Docs library fetched this pass; page-level observations carried from the ADMS pass |

## Sources

Fetched this pass (2026-09-10):

- Survalent — Products catalog: https://www.survalent.com/products/
- Survalent — SurvalentONE Distribution Power Flow and Distribution State Estimation: https://www.survalent.com/analysis-forecasting-applications/distribution-power-flow/
- Survalent — SurvalentONE FLISR & Loss of Voltage: https://www.survalent.com/flisr-loss-of-voltage/
- Milsoft — Engineering & Operations root: https://www.milsoft.com/
- Milsoft — Engineering Analysis: https://www.milsoft.com/engineering-operations/engineering-analysis/
- AspenTech — AspenTech OSI Advanced Distribution Management System: https://www.aspentech.com/en/products/dgm/aspentech-osi-advanced-distribution-management-system
- Oracle — Utilities Network Management System documentation library (Release 25.12): https://docs.oracle.com/en/industries/energy-water/network-management-system/index.html

Carried from sibling passes (corroboration, not re-fetched):

- ADMS pass: Oracle NMS User Guide / ADMS Implementation Guide page-level observations (state estimation, fault location analysis, FLISR report, VVO, load forecasting; OMS Modules beside ADMS Modeling)
- OMS pass: Milsoft as the standalone OMS pole; Oracle OMS-layer observations
- grid-operations-platform pass: family map; SurvalentONE ADMS "fully integrated SCADA, OMS, and DMS solution" on "one network model and one database"; GE Vernova GridOS portfolio/FAQ
- SCADA pass: point-based substrate definition; EMS pass: transmission pattern; DERMS pass: DER layer definition

Unreachable / abandoned:

- CYME (Eaton) — eaton.com timeout, cyme.com timeout (×2 total) — abandoned per network rules; engineering-analysis pole covered by Milsoft instead
- Hitachi Energy Network Manager, Siemens Spectrum Power, Schneider EcoStruxure ADMS — unreachable in prior sibling passes (404/403 across attempts); not re-attempted
- AspenTech DMS-specific URL (aspentech-osi-distribution-management-system-dms) — "unable to display" maintenance page; the ADMS product page was fetched instead

## Product A — Survalent (SurvalentONE DMS application family) — evidence layer A

**Family structure (products catalog).** Survalent's catalog organizes the platform as: SurvalentONE ADMS Platform, SCADA, Substation Automation, EMS, DERMS, OMS (with Call Handler, portal, dashboard, damage assessment, Polaris), then three explicit DMS groups, then Advanced Applications:

- **DMS – Analysis and Forecasting**: Distribution Power Flow and Distribution State Estimation; Short-Term Load Forecasting and Load Estimation
- **DMS – Demand Response**: Dynamic Voltage Regulation; Load Curtailment; Rotational Load Shedding; Voltage Reduction
- **DMS – Distribution Automation**: Distribution Contingency Analysis; Fault Location Analysis; FLISR and Loss of Voltage; Power Factor Control; Protection Settings Manager; Volt/VAR Optimization

Site title itself: "Advanced Distribution Management Systems (ADMS) | SCADA, OMS & DMS" — DMS is a named pillar beside SCADA and OMS. The grid-operations-platform pass's carried quote ("fully integrated SCADA, OMS, and DMS solution" on "one network model and one database") matches.

**Distribution Power Flow / Distribution State Estimation (DPF/DSE page).**
- "assesses the electrical characteristics of a distribution network, identifies potential overloads and voltage violations, and provides an analytic, problem-solving framework"
- "uses substation SCADA measurements and the network model to calculate phase voltages, currents, and losses throughout the electric network"
- unbalanced three-phase power flow analysis; configurable alarms for security violations; visual maps of issues; "optional or mandatory pre-switching validation checks before operating a device"
- DSE is an optional add-on: "increases the accuracy of power flow calculations by including SCADA measurements from outside substations and eliminating time skews between measurements" — framed as particularly helpful with microgrids and DERs

**FLISR & Loss of Voltage (FLISR/LOV page).**
- FLISR: "uses a sophisticated fault location algorithm to identify and isolate faults, and automatically resupply power, restoring service to non-faulted areas"; "automatically analyzes the capacity of adjacent feeders and DERs to pickup the load before transferring it"
- LOV: "monitors the network for sudden voltage drops, attempts to isolate the cause of the voltage loss from the network, and reroutes power"
- Two execution postures, both first-class: **semi-automatic** — "creates a switch order that isolates the fault and provides service restoration around the isolated area, but the operator must approve and execute it"; **automatic** — "the solution automatically executes the switch order"
- Reliability framing: SAIDI/SAIFI/CMI improvement as the outcome

**Reading.** In the control-room realization, the DMS applications consume SCADA measurements and the network model and produce electrical analysis that gates or drives switching decisions. The applications are separately named, separately licensed modules — the DMS is a layer, not the whole platform.

## Product B — Milsoft Engineering Analysis (WindMil) — evidence layer A

**Positioning (Engineering Analysis page).** "Milsoft Engineering Analysis software allows utility engineers to perform system studies on a detailed system model." Benefits framed for three constituencies: utility managers (system studies → loss reduction, efficiency, "run a study whenever needed"), operations staff ("perform Fault Location, using field-measured faults to identify a possible fault location on the network… pre-plan for outage scenarios, testing switching scenarios for proper voltage and capacity limits before implementing in the field"), and engineers (modeling, optimization, planning studies).

**Model.** "create a detailed visual representation of your electric grid. Your model will accurately represent the entire utility network, from delivery point to meter." The model is rendered as a GIS-style map ("model the electrical network as a GIS, accurate, detailed system model"); LandBase provides geographic background (roads, counties, imagery, Bing streaming). All electrical elements plus map objects (poles, pedestals) represented.

**Applications.** Load flow and fault current calculation ("The WindMil model will calculate all of the Fault Current and Load Flow results on the network"); optimization analysis (load balancing, capacitor placement); protective device coordination (LightTable — a library of protective-device settings, coordination studies); arc flash hazard analysis (IEEE 1584); system planning studies (location-based load forecasting, projects representing planned changes and alternatives); Computer Aided Contingency Analysis (separate product page/brochure).

**Data posture.** "bring in data from other sources such as CIS, SCADA, and AMI" — SCADA is one optional input among several, not the substrate. A 2019 vendor paper "Report on Real-Time Grid Analysis Pilots" indicates real-time analysis is a pilot-era extension, not the base product. The new Milsoft AEON ("Automated Engineering and Operations Network") is positioned as "a bridge between real-time grid data and a utility's engineering and operations platforms" — again, the bridge is the new part; the analysis core predates it.

**Ecosystem.** MultiSpeak-certified integrations; student version distributed free to engineering students ("power systems planning software").

**Reading.** This is the standalone pole: a complete distribution analysis system on the utility's own model with no SCADA, no control room, no real-time requirement — sold to co-ops and public-power utilities, and used both by engineers (studies, coordination, planning) and by operations (fault location, switching pre-checks feeding their OMS work).

## Product C — AspenTech OSI ADMS — evidence layer A

**Suite structure (ADMS product page).** "Integrated solution suite for active management of distribution grids including advanced applications, outage management and distributed energy resource management." Three headline blocks: Advanced Distribution Management ("Real-time network topology and power flow coupled with robust visualization and study mode across all functionality"), Outage Management, Operator Training Simulator — plus **Switch Order Management**: "Conduct study, simulation and pre-operational checks fully integrated with SCADA, DMS and OMS."

**Reading.** At the enterprise-suite pole, "DMS" appears as a named component that switch-order management integrates across — SCADA, DMS, OMS as three integrated layers of one platform. The DGM suite lists monarch (platform), GMS, EMS, ADMS, DERMS, Cimphony Network Model Management, Grid Apps — no standalone "DMS" product in the current lineup; the DMS content lives inside the ADMS. This corroborates: DMS = the applications layer; ADMS = the integrated platform that carries it.

## Product D — Oracle Utilities Network Management System — evidence layer A (docs library this pass) + carried page-level observations (ADMS pass)

**Docs library (fetched this pass).** The NMS documentation structure: User Guide; OMS for Water User Guide; **Advanced Distribution Management System Implementation Guide**; Configuration Guide; Edge DERMS install/deploy guide; Adapters Guide; Smart Grid Gateway integration for outage operations. Product self-description: "provides utilities with outage management and advanced distribution management functions."

**Carried observations (ADMS pass, Tier 1).** The applications layer documented in the NMS User Guide: distribution state estimation, feeder load management, fault location analysis (short-circuit-based prediction from relay fault currents), FLISR (isolation + restoration plans checking feeder capacity, voltage violations, tags/grounds/crews), Volt/VAR optimization, load forecasting — computed on the network model with live SCADA measurements; study mode across functionality; OMS Modules (trouble management) beside ADMS Modeling.

**Reading.** Oracle brands the platform NMS/ADMS; the DMS-style applications (power flow, state estimation, FLA, FLISR, VVO, forecasting) are documented as the platform's advanced-distribution-management layer. Same pattern as AspenTech at the second enterprise vendor.

## Cross-product Comparison

| Aspect | Survalent (DMS module family) | Milsoft (standalone EA) | AspenTech OSI (suite) | Oracle NMS (integrated) |
|---|---|---|---|---|
| "DMS" naming | explicit product-family name (three DMS groups) | not used ("Engineering Analysis") | named component inside ADMS ("integrated with SCADA, DMS and OMS") | not the brand; applications inside NMS/ADMS |
| Network model | the platform's network model (one model, one database) | WindMil model, delivery point to meter, GIS-rendered | real-time network topology | network model derived/maintained (ADMS Modeling) |
| Founding computation | Distribution Power Flow (phase voltages, currents, losses) | Load Flow + Fault Current | power flow on real-time topology | power flow / state estimation |
| SCADA required? | measurements used as input (DPF "uses substation SCADA measurements") | optional input among CIS/AMI/manual | integrated (real-time topology) | integrated (live measurements) |
| Control/execution | FLISR semi-automatic (switch order + operator approval) or automatic | none — proposes; operations pre-plans switching | switch orders with study/simulation/pre-operational checks | operator executes; FLISR proposals |
| Application suite | DPF/DSE, load forecasting, contingency, FLA, FLISR/LOV, VVO, power factor, protection settings, DR applications | load flow, fault current, optimization (capacitor placement, load balancing), coordination (LightTable), arc flash, contingency, planning studies | advanced applications + study mode | state estimation, FLA, FLISR, VVO, forecasting, feeder load management |
| Customer tier | co-op/muni/mid-market | co-op/public power | large utilities | large utilities |
| Real-time posture | real-time-capable layer of a real-time platform | offline studies; real-time as pilot/bridge extension | real-time | real-time |

**Stable across the sample (layer B):**
1. a connected electrical model of the utility's own distribution network as the working subject (all four; Milsoft's "delivery point to meter" is the most explicit scope statement)
2. power-flow-class electrical computation on that model — voltages, currents, losses, fault currents (all four; the minimum common denominator)
3. results organized as limit violations and decision support — overloads, voltage violations, fault locations, restoration/switching proposals, coordination problems (all four)
4. the analysis serves both engineering (studies, planning, protection) and operations (switching checks, fault location, restoration) constituencies (Milsoft states this explicitly; the others structurally)
5. SCADA measurements as a common but optional input; the analysis core exists without them (Milsoft proves; Survalent DPF names SCADA as input; historical mainframe-era studies precede integration)

**Product-shaped (kept general in the final doc):** exact application names and suite membership; semi-automatic vs automatic FLISR execution; DSE as add-on; LightTable settings-library mechanics; AEON bridge positioning; student-version distribution.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — defining core (minimal; removal of any leg breaks the Type)

Three jointly-held structures:

1. **The utility's connected distribution network model as the working subject.** The system holds a connected electrical model of the utility's own distribution network — feeders, switches/reclosers/fuses, transformers, regulators/capacitors, conductors with electrical parameters, phases — maintained as the network's configuration changes. The model is the utility's actual network, not an abstract test circuit. Remove → a generic power-systems calculator, or a network diagram/GIS viewer.
2. **Electrical analysis computed on that model.** Power-flow-class computation at minimum — phase voltages, currents, losses under a given configuration — extended in mature products to fault currents, contingency what-ifs, and optimized configurations. The system answers "what does / what would the electricity do on this network." Remove → a model viewer with no computation.
3. **Distribution operating/planning decision support.** The analysis exists to answer the utility's operating and planning questions: is a proposed switching action electrically safe (voltage/capacity), where is the fault, how can healthy sections be restored, where are overloads and voltage violations, what equipment placement reduces losses, how will load grow. Remove → an engineering sandbox with no operational binding.

Jointly-held load-bearing:
- 1 alone = network model viewer / Utility GIS territory
- 2 without 1 = generic power-flow calculator on abstract circuits
- 3 without 1+2 = dashboards with no computation
- 1+2 without 3 = engineering sandbox (the Type's weakest edge; in-sample products all carry the decision binding)
- 1+3 without 2 = GIS/OMS territory (records and events, no electrical computation)
- 2+3 without 1 = calculators and spreadsheets

**Deliberately NOT in L0** (tested against the historical check):
- Real-time SCADA telemetry as the data source — Milsoft runs complete studies with CIS/AMI/manual data; SCADA is an input where available; mainframe-era distribution load-flow studies predate SCADA integration entirely.
- Supervisory control of field devices — that is the SCADA/ADMS substrate; the DMS proposes (switch orders, restoration plans), the operator or automation executes. Survalent's semi-automatic FLISR mode (switch order + operator approval) is a first-class posture, not a degraded one.
- Operational event loop (alarms → assessment → recorded actions) — the ADMS differentiator; a DMS study/analysis layer does not require it.
- Any specific application beyond power-flow-class computation (FLISR, VVO, state estimation, forecasting, contingency, coordination) — the canonical suite is common-mature structure, not definition; products ship subsets (Milsoft's coordination/arc-flash emphasis vs Survalent's automation emphasis).
- Unbalanced three-phase modeling, DER/microgrid support, cloud deployment, model-source mechanism, study mode — variant or common-mature.

**Historical check (passed).** The pre-software practice — distribution engineers computing voltage drop, fault currents, and load flows by hand and with mainframe feeder programs on paper-based feeder models — satisfies the core at analog level: the utility's feeder model + electrical computation + operating/planning decisions, with no SCADA, no real-time, no automation. The 1990s–2000s standalone distribution engineering packages (the class Milsoft WindMil descends from) satisfy it with no integration at all. The definition names no era machinery.

### L1 — common mature structure

- The canonical application suite on the power-flow core: distribution state estimation (reconciling measurements into a consistent state), fault location analysis, FLISR and loss-of-voltage restoration, Volt/VAR optimization, short-term load forecasting and load estimation, contingency analysis, capacitor placement / load-balancing optimization, protective-device coordination and settings management, arc-flash analysis
- Study mode — the same analysis applied to sandbox copies of the model for what-if and planning
- Switch-order integration — analysis results rendered as proposed switching steps for operator approval (semi-automatic posture) or executed automatically (automatic posture)
- Model sourcing and maintenance — import from GIS/CIM or native modeling, model validation tooling
- Data inputs — SCADA measurements, AMI/meter data, CIS load data, DER data
- Violation surfacing — overload and voltage-violation lists, visual maps of issues, configurable security alarms

### L2 — variant / optional

- Packaging: DMS applications layer inside an ADMS suite (dominant current form) vs standalone engineering-analysis product (co-op/mid-market pole) vs historical whole-platform DMS (now ADMS-branded)
- Automation posture: advisory → semi-automatic (proposals as switch orders) → supervised automatic execution
- Real-time posture: SCADA-fed continuous analysis vs offline/asynchronous studies vs pilot-stage real-time bridges
- Customer tier: enterprise IOU suites vs co-op/muni standalone tools
- Model scope: primary/feeder-level vs extension to secondary services ("delivery point to meter")
- DER/microgrid depth: DER as model elements and FLISR/VVO inputs vs deeper DER orchestration (DERMS territory)
- Regional practice: unbalanced three-phase conventions, protection philosophies, planning-study traditions

### L3 — vendor-specific (research notes only)

- Survalent: the three-group DMS taxonomy (Analysis & Forecasting / Demand Response / Distribution Automation); DPF/DSE as named add-on pair; LOV as a named companion application; GeoBridge/Schematic Generator/Network Topology Processor as supporting products
- Milsoft: WindMil/LightTable/LandBase product names; AEON bridge; free student-version program; MultiSpeak integration ecosystem
- AspenTech: monarch platform framing; Cimphony Network Model Management; Grid Apps; "integrated with SCADA, DMS and OMS" switch-order phrasing
- Oracle: NMS product name; ADMS Implementation Guide title; OMS Modules / ADMS Modeling module split; Smart Grid Gateway integration

## Vendor-specific Findings

- Survalent's explicit three-group DMS product taxonomy (including demand-response applications under the DMS banner) is vendor-specific packaging; other vendors do not place demand response inside DMS.
- Milsoft's LightTable protective-settings library and IEEE 1584 arc-flash analysis are product-depth features not universal in the sample.
- AspenTech's and Oracle's suite framing (DMS as internal component, ADMS as brand) is the enterprise-pole packaging; it should not be read as claiming standalone DMS products don't exist elsewhere.

## Rejected Findings

- **"DMS = ADMS" (alias verdict) — rejected as the sole verdict.** A product population answers to DMS that is not ADMS-branded: Survalent sells DMS as a module family beside SCADA and OMS (a utility can license SCADA + DMS without OMS), and the standalone engineering-analysis pole (Milsoft; CYME-class, unreachable but market-known) lives entirely outside the ADMS frame. The ADMS L0 requires real-time monitoring + supervisory control + an operational event loop; the DMS core requires none of these. Neither L0 contains the other. Keep-both ratified; the historical whole-platform usage of "DMS" is recorded as naming drift, not as the Type's identity.
- **"DMS requires real-time SCADA" — rejected.** Contradicted by Milsoft (studies without SCADA) and by the historical record (pre-integration engineering analysis).
- **"DMS includes supervisory control" (the 1980s EPRI-style whole-platform reading) — rejected as the modern definition.** The market renamed the integrated whole ADMS; retaining control in the DMS core would make the leaf a duplicate of ADMS. Control is recorded as the historical whole-platform usage.
- **"FLISR/VVO/state estimation are definitional" — rejected.** Milsoft's core strength is coordination/planning studies; Survalent sells DPF without DSE; suite membership varies. Only power-flow-class computation is universal.
- **"DMS = distribution planning software" (CYME/SINCAL-class identity) — rejected as too broad.** The sampled DMS products are bound to the utility's operating network and its operational decisions; pure green-field planning tools are an adjacent market sharing the analysis machinery.

## Boundary Findings

1. **vs Advanced Distribution Management System / ADMS (§19, processed) — DISCHARGES the pre-hung joint-review flag. Keep-both RATIFIED.** The seam is **real-time network operations vs analysis-on-model**. ADMS's discriminating core: live telemetry rendered on the connected model + supervisory control of field devices + the operational event loop. DMS's core: the connected model + electrical analysis computed on it — no live telemetry, control, or event loop required. Removal tests hold both directions: strip real-time monitoring/control/event-loop from an ADMS → a DMS-class analysis system remains (model + applications); strip the analysis from an ADMS → SCADA + OMS remains, not a DMS. In the current market the DMS is usually a layer of the ADMS on one network model (Survalent DMS groups beside SCADA/OMS; AspenTech "integrated with SCADA, DMS and OMS"; Oracle DMS applications inside NMS/ADMS) — packaging, not identity. The historical usage of "DMS" for the whole distribution control platform (the distribution analog of EMS, including SCADA) is recorded as naming drift: the market renamed that whole "ADMS" and retained "DMS" for the applications layer. This refines the ADMS doc's Related-Types row ("overlapping / historical") — the layer is live, not merely historical.
2. **vs SCADA (§16, processed)** — substrate vs analysis. SCADA acquires point-based telemetry and writes back control commands with no connected model required; DMS computes electrical analysis on a connected model and requires no telemetry. DMS consumes SCADA measurements where available (Survalent DPF; Oracle). Consistent with the SCADA pass's counterparty framing.
3. **vs Outage Management System / OMS (§19, processed)** — analysis vs outage-response loop. The OMS centers events → prediction → crews → restoration → reliability records; the DMS centers electrical computation. The contact points: fault-location analysis narrows patrol areas for OMS events; FLISR restoration proposals become switching executed during restoration; switching pre-checks validate restoration plans. Milsoft ships the analysis system beside its OMS as separate products. Consistent with the OMS pass's seams.
4. **vs Energy Management System / EMS (§19, processed)** — same analysis pattern, transmission network, balancing-loop center. The EMS pass already held "ADMS/DMS = same structural pattern on the distribution network"; this pass confirms from the DMS side: the DMS is the distribution instance of the network-analysis layer the EMS also carries.
5. **vs DERMS (§19, processed)** — DERMS centers the DER fleet (registry, visibility, dispatch within grid constraints); the DMS analyzes the network, with DERs as model elements and inputs to FLISR/VVO/forecasting (Survalent FLISR "analyzes the capacity of adjacent feeders and DERs"). DER orchestration belongs to DERMS; network analysis consuming DER data belongs here.
6. **vs Utility GIS (§19, processed)** — model of record vs analysis. The GIS holds the as-built georeferenced connected model; the DMS derives a working electrical model and computes on it (Milsoft pairs WindMil with LandBase backgrounds; the utility-gis pass ratified "operational systems derive working copies and run real-time loops"). Remove the computation → the GIS remains.
7. **vs grid-operations-platform (§19, processed, counterparty duty)** — consistency confirmed: the family map lists the control-room estate as SCADA substrate + EMS (transmission) + ADMS/DMS/OMS (distribution) + DERMS (DER layer). This pass refines the map's "ADMS/DMS+OMS" grouping: ADMS = the integrated real-time platform; DMS = the analysis strand (usually its applications layer, sometimes standalone); OMS = the outage loop. No conflict with the umbrella document.
8. **Name-collision guard** — "DMS" in the directory also collides with: Dealer Management System (automotive/equipment dealers — the directory's agricultural-dealer-management pass recorded the same observation) and "distribution management" in logistics (foodservice-distribution-management, book-distribution-management). The §19 leaf is exclusively the electric-utility control-room sense. No directory change proposed.
9. **Adjacent market, not a directory leaf** — distribution planning/engineering-analysis suites sold primarily for design studies (CYME-class; unreachable this pass) share the analysis machinery. The sampled standalone pole (Milsoft) is operations-bound (fault location, switching pre-checks beside its OMS), which keeps it inside this Type; a purely design-oriented planning tool would sit at this Type's boundary. Recorded as an observation; no directory change.

## Uncertainties

1. **CYME unverified** (timeout ×2). The engineering-analysis suite pole beyond Milsoft rests on market knowledge only; no claims about CYME's structure are made. If a future pass reaches CYME, the standalone-pole description should be revisited.
2. **Historical whole-platform DMS products** (1980s–2000s vendor DMS offerings) were not directly documented from primary sources this pass; the whole-platform reading rests on the ADMS pass's market observation and the EMS/ADMS family pattern. The alias-drift narrative is asserted at corroboration strength, not Tier-1 strength.
3. **Exact state-estimation/FLISR algorithm mechanics** are documented only in carried Oracle observations (ADMS pass); described here as conceptual structures.
4. **Whether "load estimation"/load allocation (meter-data-derived feeder loads) is universal** in the suite: observed at Survalent (Load Estimation) and Milsoft (CIS/AMI data in), not confirmed as universal.
5. **Non-electric DMS usage**: the sampled products are all electric-distribution. Whether water/gas control-room vendors market a "DMS" layer for their networks was not verified (Oracle ships "OMS for Water" but no water DMS was observed).

## Final Synthesis

A **Distribution Management System (DMS)** is the electric utility's distribution network-analysis system: software that holds a connected electrical model of the utility's own distribution network and computes electrical analysis on it — power-flow-class calculation of voltages, currents, losses, and fault currents as the founding and minimum computation, extended in mature products into the canonical suite (state estimation, fault location, FLISR/loss-of-voltage restoration, Volt/VAR optimization, load forecasting, contingency analysis, protection coordination) — so that the utility's engineering and operations decisions about that network (switching safety, fault response, restoration, voltage and loading management, loss reduction, planning) rest on computed electrical evidence rather than assumption.

Its position in the control-room family: the **analysis strand**. SCADA is the telemetry/control substrate; the OMS is the outage-response loop; the ADMS is the integrated real-time platform that commonly carries the DMS as its applications layer on one network model; the DMS itself requires none of the real-time machinery — it is the model plus the computation, realizable as an ADMS module family, as a standalone engineering-analysis system at the co-op/mid-market pole, and historically as the name of the whole distribution control platform before the market converged on "ADMS". The ADMS pass's alias flag is discharged as keep-both: overlapping siblings sharing the network-model substrate, separated by the real-time-operations requirement.
