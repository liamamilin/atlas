# Research Notes — Wind Asset Management

## Research Goal

Determine what a **Wind Asset Management** application is, from real products: what system of record it holds, what its production expectation is anchored on, how availability is recorded and restored, how production resolves into money and reporting — and where its boundaries sit against the technology-generic renewable sibling (renewable-energy-asset-management), the dispatch-operations sibling (power-plant-management), OEM turbine-side digital services, condition-monitoring specialists, wind-farm design tools, and market-facing systems.

This pass also has a delegated duty: the renewable-energy-asset-management pass (2026-09-09) and the solar-asset-management pass (2026-09-09) both pre-hung a flag that **wind-asset-management and battery-energy-storage-management are expected population specializations** of the four-leg generation-management spine, "same population-specialization resolution expected by symmetry, their passes to confirm". The virtual-power-plant-platform pass (2026-09-10) forwarded the same removal test. This pass must confirm or refute that resolution with wind-native first-hand evidence.

## Initial Boundary

Working hypothesis before research:

- Core use: the wind fleet owner/operator's management system for **operating** wind farms — production performance, availability, maintenance coordination, commercial resolution.
- Primary users: wind asset managers, performance engineers, control-room/monitoring staff, O&M coordinators, reliability engineers, finance, executives; third-party technical asset managers; O&M service providers.
- Nearest neighbors: Renewable Energy Asset Management (technology-generic sibling), Power Plant Management (dispatch-operations seat), Solar/BESS Asset Management (population siblings), OEM turbine SCADA/digital services (control + OEM-side analytics), CMS/condition-monitoring specialists, CMMS/FSM (work execution), wind-farm design tools (upstream), energy trading/scheduling (market-facing), VPP/DERMS (aggregated third-party portfolios).
- Likely confusion: with OEM SCADA portals (Vestas-class) and with condition-monitoring products; both sit at or below the control/detection substrate.
- Unknowns: whether wind carries any population-specific **structure** beyond texture (candidates: contractual-availability reconciliation against OEM calculations; power-curve-based underperformance; FSA/O&M-contract machinery; CMS integration; offshore segment).

## Research Questions

1. What is the system of record? (farms/sites, turbines, balance of plant, commercial context)
2. What is the expectation anchor? (wind resource measurement, power curves, long-term yield estimates, budgets)
3. How is availability recorded, classified, computed, and restored? (turbine states, fault/downtime classification, contractual vs standard categorizations, work coordination, service-provider oversight)
4. How does production resolve into money and stakeholder reporting? (offtake revenue, availability-guarantee economics, OPEX, owner/investor/lender reporting)
5. What is wind-specific **texture** vs wind-specific **structure**?
6. Where exactly are the boundaries: OEM digital services, CMS specialists, design tools, optimization specialists, trading, VPP?
7. Historical check: would a paper-era wind farm operator satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers — mirroring the sibling passes' pole structure:

| Product | Pole | Customer tier | Wind-native? |
|---|---|---|---|
| **Bazefield** | operator platform (monitoring / analysis / operations management) | owner-operators, third-party AM firms (Invenergy Services, SSE Renewables, W3 Energy, TruBoard) | wind heritage (Norwegian; SSE onshore-wind control room; multi-tech today) |
| **Clir Renewables** | investor/lender analytics (reporting, contractual-availability reconciliation, budget reforecast) | infrastructure funds, asset & investment managers (CPP, CIP, Glennmont, CWP Energy) | wind-origin (Calgary; wind + solar + BESS today) |
| **ONYX Insight** | reliability/condition-monitoring-led technical asset management | owner-operators, O&M/reliability teams (bp Wind, Pattern, EDF, ScottishPower, RWE, ERG) | purely wind-native (since 2008) |
| **Power Factors Unity** | full-suite multi-tech owner platform (boundary anchor, documented in the REAM pass) | large IPPs/utilities (Pattern, EDF Renewables, bp, Engie, Eneco, Parkwind) | multi-tech; wind via the 3megawatt Blade + Greenbyte lineage |

Boundary probes: **Vestas Digital Services** (OEM side: VestasOnline, Scipher, VestasDeveloper, ShopVestas, multibrand service), **PulseSense Dynamics** (the domain windesco.com now redirects to — performance-optimization specialist), **EMD WindPRO** (design/siting — unreachable, see Sources).

## Sources

Research date: **2026-09-10**. All product observations below are from official vendor pages fetched live on this date unless marked otherwise.

- Bazefield — homepage: https://bazefield.com/
- Bazefield — Our Products (Monitoring / Analysis / Operations Management / Cutting-Edge Technology): https://bazefield.com/our-products/
- Clir Renewables — homepage: https://www.clir.eco/
- Clir Renewables — Clir Portfolio: https://www.clir.eco/portfolio
- ONYX Insight — homepage: https://onyxinsight.com/
- ONYX Insight — Case Management: https://onyxinsight.com/software-analytics/case-management/
- Power Factors — homepage (Unity pillars; REMI): https://www.powerfactors.com/
- Vestas — Digital Services (VestasOnline, Scipher, VestasDeveloper, ShopVestas, multibrand): https://www.vestas.com/en/services/digital-services (served at /en/energy-solutions/service/digital-services)
- PulseSense Dynamics — homepage (windesco.com redirect target): https://www.pulsesense.io (fetched via windesco.com redirect)
- Sibling-pass context (read, not fetched): research/renewable-energy-asset-management.md, applications/renewable-energy-asset-management.md, applications/solar-asset-management.md, STATUS.md entries for power-plant-management / renewable-energy-asset-management / solar-asset-management / virtual-power-plant-platform.

**Source-access limitations:**

- EMD WindPRO (https://www.emd-int.com/windpro and site root) — transport error ×2 → abandoned per network rule. The wind-farm design-tool boundary is therefore documented **indirectly** (Clir's "outdated pre-construction assumptions" language; ONYX pre-construction technical advisory) and at reduced strength.
- windesco.com no longer serves the historical WindESCo product surface (redirects to PulseSense Dynamics) — recorded as market-structure evidence only; the historical product could not be examined.
- No operational help centers / user manuals were reachable in depth for any sampled product. All workflow/rule claims are calibrated to official product and marketing pages. Precise operational details (availability formula definitions, numeric limits, billing cadences, state taxonomies) are intentionally not asserted.
- Vendor scale figures (32,000+ turbines, 350+ GW, 30 GW, 600+ customers, downtime-reduction percentages) are the vendors' own marketing claims, recorded as claims, not verified facts.

---

## Product Observations

### Bazefield — operator platform (evidence layer A unless noted)

Self-label: "renewable energy asset management system" / "renewables management system"; Norwegian; "30 GW of wind and solar managed" (marketing claim). Three product pillars: **Monitoring**, **Analysis**, **Operations Management**.

- **Fleet record (leg 1):** portfolio → power plant → asset hierarchy; "capture all your power plants data in one uniform software platform"; power-plant overview screens can include "substation mimics, met masts, forecasts"; interfacing to "transmission and substation, production metering, MET mast and LIDAR, weather forecast, power forecast, CMMS, ERP, document- and HSEQ systems". Turn-key support for turbine models "from vendors such as Vestas, Siemens, Senvion, Nordex, Gamesa, Enercon, GE". Data model "based on the IEC 61400-25 standard as default" (wind-turbine SCADA information model); OPC, IEC 60870-5-101/104, ODBC/SQL, PI historian.
- **Production vs expectation (leg 2):** monitoring of "production data, warnings, alarms and other key metrics in real-time"; assets-overview app to "identify stopped and underperforming assets… typically used as a 'control room' function for everyday operation"; **power curve analyzer** — "detect abnormalities or sudden unexpected changes in your power curves… compare power curves before and after an OEM software upgrade"; trending of measured or calculated values; 2D/3D plotter to tag level; weather forecasting "standard… or the ability to integrate any weather forecasting service"; "In order to have accurate Production Forecasting, you need to have control over availability planning (service, repair, substation or grid outage etc.)".
- **Availability record & restoration (leg 3):** **availability analytics** — "generate your own availability calculations based upon your contractual categorization or based upon other measures such as IEC-61400… a much stronger negotiation position with your OEM in availability meetings"; alarm statistics "from both a frequency and duration standpoint… filter… for time and root causes"; **availability planner** — "manually schedule both corrective and planned maintenance… can be integrated to a maintenance system if required"; **site activity / HSE** — "planning and tracking service activities and personnel for sites and turbines… contacts and companies management including safe passes and site inductions, work orders, turbine controls and general site access tracking… handle and report on HSE related information and statistics".
- **Money & stakeholder (leg 4):** positioning toward "investors, asset managers, and operators"; "increased our customers profitability"; "strengthen users' negotiation power with vendors and suppliers"; "Increase energy value". No invoicing/billing module claimed on fetched pages — commercial depth left to ERP/other systems (operator-pole shape).
- **Clients:** Invenergy Services ("Data-Driven Owner's Platform" for "wind, solar, and storage asset owners… expected to top 25-gigawatts by 2025"); SSE Renewables ("onshore wind control room solution"); W3 Energy (five-year cooperation); Oak Creek; TruBoard Partners (India third-party AM).
- Deployment: cloud service or in-house installations; iPad/iPhone/Android/Windows clients; SDK with .NET + REST APIs.

### Clir Renewables — investor analytics (evidence layer A unless noted)

Self-label: "The AI behind high-performance renewable portfolios"; "Built On 350+ GW of Assets Across Solar, Wind & BESS" (marketing claim). Products: **Clir Portfolio** (APM platform), **Clir Enhance** (enriches "secondary SCADA systems… with Clir data model"), **Clir Associate** (executive workflows). Serves asset managers, investment managers, corporate offtakers.

- **Fleet record (leg 1):** "renewable energy–specific data model"; pipeline "Ingest and standardize — transforms disparate OEM and turbine data into a clearly defined standard"; "Enrich and enhance — labelled events data and layered data sources"; portfolio-wide unification.
- **Production vs expectation (leg 2):** portfolio performance monitoring — "turning messy SCADA data into clean standardized data to enable anomaly detection, and industry benchmarking"; power-curve charting; "quickly identify underperforming assets"; **budget reconciliation & reforecast energy yield** — "reforecasting long-term energy yield based on historical performance, loss drivers, and scenario analysis"; "forecasts are based on outdated pre-construction assumptions that no longer reflect how assets actually perform".
- **Availability record (leg 3, analytics side):** **contractual availability reconciliation** — "standardizing SCADA data, event logs, and contract logic into a transparent, auditable framework"; "interrogate availability calculations, identify mislabeled or missing data"; "Independently validate OEM contractual availability calculations"; "Reduce bonus overpayments and recover liquidated damages"; "Generate audit- and dispute-ready CA reports"; "challenge inflated bonus claims or conservative liquidated damage claims"; "Increase confidence when challenging service providers".
- **Money & stakeholder (leg 4):** "Investor Grade Portfolio Reporting and Intelligence" — "effectively explain to their board which assets are over or underperforming, understand why"; "budgets, cash flow projections, and valuations more accurate and credible"; "Strengthen valuations and refinancing models"; "restore trust with investors and lenders".
- No control, no field execution, no invoicing engine claimed — the deliverable is the explanation and the reconciliation (investor-analytics pole).
- Clients: Glennmont/Nuveen, HASI, Northleaf, CPP Investments, Copenhagen Infrastructure Partners, Palisade, Arjun, Tokio Marine HCC, CWP Energy (wind), NTR, Octopus Energy Generation, Swift Current.

### ONYX Insight — reliability/condition-monitoring-led (evidence layer A unless noted)

Self-label: "Your whole turbine predictive analytics partner"; wind-only; "monitoring 32,000+ wind turbines in 45+ countries"; "helping turbine owners and operators since 2008"; "connecting 15 different CMS hardware types"; "$14 billion worth of assets" (all marketing claims). Three pillars: **Advanced Sensing**, **Software & Analytics**, **Engineering & Consultancy**.

- **Fleet record (leg 1):** fleet-to-component case tracking; EDF case study — "centralising 6GW+ of wind assets with x6 CMS and x7 turbine OEMs into one platform"; Finerge — "unifies monitoring across 5 turbine OEM platforms"; ERG — "x4 wind turbine OEMs across 300+ wind turbines"; "OEM and hardware-agnostic".
- **Production vs expectation (leg 2):** outcome framing "maximise reliability, minimise downtime and increase annual energy production"; case studies "increase AEP and decrease O&M costs"; underperformance surfaced via dashboards ("spot derated turbines"); OPEX forecasting "benchmarking your turbines against 160GW+ of assets". The pole's expectation anchor leans reliability-first; AEP is the outcome metric. (Layer B: cross-product commonality of AEP framing.)
- **Availability record & restoration (leg 3):** **Case Management** — "connects the dots between fault detection and resolution"; "centralises fault tracking, inspection and maintenance workflows into one shared workspace"; "Fleet-to-component case tracking with full historical fault and action log and communications across site, central and external teams"; KPIs "to minimise downtime, response time and derated days"; "the platform has truly become our data historian" (Clearlight Energy); bp Wind and Pattern Energy (4.2 GW "AI Hub") references; **fleetMONITOR** — "Monitor the health of your entire wind fleet from a single platform"; **Shadow Monitoring** — "Maximise your FSA & OEM partnership with your own data" (owner's independent record alongside the OEM's full-service agreement); **fieldPRO** — field inspections "built for wind"; sensing: ecoBLADE (blade structures), ecoPITCH (blade root connections), ecoCMS (drivetrain retrofit/upgrade, oil particle counting), structural health monitoring (towers/foundations), pitch bearings, portable health sweeps.
- **Money & stakeholder (leg 4):** **End of Warranty Campaigns** — "Combine analytics and inspections for ultimate clarity"; Vietnam case study — "warranty bond extension secured following end of warranty inspection"; **OPEX Forecasting**; life-extension consultancy; Aviva partnership "to manage wind turbine insurance risks and help extend asset life". No offtake invoicing claimed — money texture is warranty/OPEX/insurance-shaped (reliability-pole shape).
- **failureATLAS** — free "online encyclopaedia of wind turbine failure modes — covering blades, bearings and everything in between" (wind failure-mode taxonomy as domain knowledge artifact).

### Power Factors Unity — full-suite boundary anchor (evidence layer A; wind lens)

Documented in depth in the REAM pass (2026-09-09). Re-fetched homepage confirms the three-pillar suite: **Monitoring & Control** (Local/Central SCADA, Power Plant Controller, EMS), **Technical Asset Management** (Asset Performance Management, Advanced Insights, Field Service Management), **Commercial Asset Management** (Asset Oversight — "comprehensive system of record… oversight of operations, service providers, and revenue", Invoice Management). "600+ global customers"; wind-relevant customers visible: Pattern, EDF Renewables, bp, Engie, Eneco, Parkwind (offshore), Nadara, W3 Energy, European Energy. REMI ("Renewable Energy Management Intelligence") agentic-AI layer is era-current packaging, not structure. Wind-specific depth (3megawatt Blade lineage) is recorded in the REAM pass's market-structure probes (3megawatt.com redirects to powerfactors.com).

### Boundary probes

**Vestas Digital Services (OEM side):** VestasOnline — "personalised wind turbine self-service" customer portal; **Scipher** — "industrial energy analytics platform" over "the industry's largest and most robust dataset" (the OEM's own installed fleet); **VestasDeveloper** — "secure, standardised APIs… to access and receive Vestas operations data" (the data pipe third-party systems consume); ShopVestas (spare parts); **Multibrand services** — "service more than 6 GW of non-Vestas turbines" (the OEM as service provider). Interpretation: the turbine OEM ships portals/analytics over its **own** fleet and sells the **service** the owner must oversee; the owner-side wind asset management system is OEM-agnostic over multi-OEM fleets and exists precisely to hold the owner's independent record — including checking the OEM's availability numbers (Clir) and running shadow monitoring against the FSA (ONYX). The OEM surface is the control/data substrate and the counterparty's system, not the owner's system of record.

**PulseSense Dynamics (windesco.com redirect target):** "helps assets owners and operators improve performance, reduce downtime and extend equipment life across wind and hydro power operating assets"; **Wind PulseSense** — "Detect and address hidden wind turbine underperformance. Use high-resolution turbine data to find performance losses that conventional SCADA data analytics miss and recommend corrective actions"; **Swarm** — "Real-time wind farm control to recover wake losses. Coordinate turbine yaw positions in real time… increase total plant-level energy production"; "15 GW capacity analyzed, 6,000 assets monitored" (marketing claims). Interpretation: a performance-optimization specialist pole — underperformance detection (leg-2 analytics) plus wake-steering **control** (control substrate). It holds no fleet system of record with commercial context and no money/stakeholder loop on the fetched pages — adjacent specialist, not the Type's center.

**EMD WindPRO (design/siting):** unreachable (transport error ×2). Boundary documented indirectly: Clir's framing that budgets rest on "outdated pre-construction assumptions" implies the design-time yield estimate is produced upstream of this Type; ONYX sells "pre-construction" technical advisory as a distinct service. Design tools (resource assessment, layout design, energy-yield estimation) are the upstream lifecycle; this Type begins at the operating asset. (Reduced-strength finding.)

---

## Cross-product Comparison

| Structure | Bazefield | Clir | ONYX | Power Factors | Verdict |
|---|---|---|---|---|---|
| Wind fleet as system of record (farms + turbines + BoP + commercial context) | ✓ portfolio→plant→asset; met masts, substations, metering; multi-OEM turn-key | ✓ renewables data model; OEM/turbine data standardized | ✓ fleet-to-component; 7 OEMs / 6 CMS types unified (EDF case) | ✓ Asset Oversight "system of record" | **Core** (all four) |
| Production vs wind-resource expectation, gap attributed | ✓ power-curve analyzer; met mast/lidar; weather/power forecast; production forecasting tied to availability planning | ✓ anomaly detection, benchmarking, power-curve charting; reforecast yield | ✓ AEP framing; derated-turbine dashboards; reliability-first anchor | ✓ APM "asset availability and yield" | **Core** (all four) |
| Availability record & restoration | ✓ availability analytics (contractual categorization / IEC-61400); availability planner; site activity, work orders, HSE | ✓ contractual-availability reconciliation (analytics side; dispute-ready) | ✓ case management fault→resolution; fleetMONITOR; shadow monitoring vs FSA; field inspections | ✓ APM + FSM work orders | **Core** (all four) |
| Money & stakeholder resolution | ✓ negotiation position vs OEM; profitability framing; investors/asset managers named; no invoicing module claimed | ✓ bonus/LD economics; budget reconciliation; valuations/refinancing; board/investor reporting | ✓ end-of-warranty campaigns; OPEX forecasting; insurance; no offtake invoicing claimed | ✓ Invoice Management, Asset Oversight revenue | **Core** (all four; depth pole-variable) |
| Multi-OEM data integration as substrate | ✓ turn-key turbine models; IEC 61400-25 default | ✓ "disparate OEM and turbine data" | ✓ 15 CMS hardware types; OEM-agnostic | ✓ multi-vendor fleets | **Common** (substrate, not definition — paper-era satisfies without) |
| Control-room monitoring | ✓ explicit "control room" function | ✓ real-time monitoring (analytics grade) | ✓ dashboards | ✓ SCADA pillar (sibling product) | **Common** |
| Condition monitoring / CMS | — (integrates CMMS; not CMS-led) | — | ✓ sensing hardware + services (pole signature) | — | **Optional** (pole) |
| Contractual-availability reconciliation vs OEM | ✓ owner-side availability computation for "availability meetings" | ✓ flagship capability | ✓ shadow monitoring vs FSA; end-of-warranty | — (CAM adjacent) | **Common** (wind signature texture; realization of legs 3+4) |
| Invoicing/billing engine | — | — | — | ✓ Invoice Management | **Optional** (pole depth) |
| Controls (SCADA/PPC/EMS/wake steering) | turbine controls touch; integration to SCADA | — | — | ✓ sibling pillar | **Optional** (sibling products) |
| AI/agentic packaging | — | ✓ "Clir AI" | ✓ "AI Hub" (Pattern case) | ✓ REMI | **Optional** (era-current) |

## Canonical Abstraction

### L0 — Defining Invariant

The four-leg generation-management spine (as ratified for renewable-energy-asset-management), **bound to the wind population**:

1. **The wind fleet as the system of record** — persistent, identified records for each wind farm/site and its producing assets (wind turbines; balance of plant: substations, met masts, metering), each site carrying its commercial context (offtake contracts, O&M/full-service agreements, warranties, financing). Remove → asset registry / site list.
2. **Production managed against wind-resource expectation** — what the wind actually made possible (measured wind resource → power-curve-based expected energy), commonly alongside budgets and long-term yield estimates, vs actual; every gap attributed (turbine downtime, balance-of-plant downtime, grid outage/curtailment, weather, underperformance). Remove → production statistics with no standard of judgment.
3. **The availability record and its restoration** — turbine/farm availability held as the constraint on production; downtime, derates and curtailment recorded and classified under contractual or standard categorizations; restoration coordinated with service providers/technicians to recorded closure. Remove → analytics with no restoration loop, or bare ticketing.
4. **Money and stakeholder resolution** — production reconciled to revenue where contracted, availability-guarantee and O&M economics administered, budgets closed, and periodic reports produced for owners, investors, lenders. Remove → operation with no economic or accountability closure.

Jointly load-bearing: 1 alone = registry; 2 alone = yield analytics; 3 alone = O&M ticketing/CMMS; 4 alone = billing software; 1+2 without 3 = analytics with no restoration loop; 1+3 without 2 = maintenance management with no production judgment; 2+3 without 1 = analytics over anonymous turbines; 1+4 without 2 = contract admin with no performance judgment; 2+4 without 1+3 = reporting over nothing held.

**Population binding:** the operator is a wind-fleet owner/operator; the producing assets are wind turbines in wind farms; the expectation anchor is the wind resource realized through power curves. Remove the wind population → the technology-generic Type (renewable-energy-asset-management). The generic pass without wind-native market texture → this leaf.

### L1 — Common Mature Structure

- multi-OEM SCADA/data integration and normalization (the substrate problem; IEC 61400-25-class turbine data models as one implementation)
- monitoring/alerting with portfolio → farm → turbine drill-down; control-room function
- power-curve analysis and performance benchmarking (before/after-intervention comparison)
- availability computation under selectable definitions (contractual categorization vs IEC-61400-class standards)
- loss attribution across downtime / curtailment / weather / underperformance
- availability planning around service and grid outages; work orders; site activity, access and HSE tracking; CMMS integration
- condition-monitoring (CMS) integration and SCADA-based anomaly detection
- weather/power forecast inputs
- scheduled, audit-ready stakeholder reporting with provenance

### L2 — Variant / Optional Structure

- commercial depth: contract storage, invoice generation, budget reconciliation, reforecast yield, valuations/refinancing (investor-analytics and full-suite poles)
- reliability-led depth: CMS sensing hardware, shadow monitoring, end-of-warranty campaigns, OPEX forecasting, root-cause analysis, life extension (reliability pole)
- controls adjacency: SCADA/PPC/EMS as sibling products; wake-steering control (optimization-specialist pole)
- performance-optimization specialist pole (hidden-underperformance detection, wake-loss recovery)
- onshore vs offshore segment (offshore economics shift the O&M texture, not the structure)
- single-technology wind fleet vs multi-tech portfolio (population axis, not structural)
- operator model: owner in-house, third-party technical asset manager, O&M provider operating on the owner's behalf
- deployment: cloud vs in-house; AI packaging era-current

### L3 — Vendor-specific (Research Notes only)

- Bazefield: IEC 61400-25 default data model; OPC / IEC 60870-5-101/104 / PI interfaces; named turn-key turbine-vendor list (Vestas, Siemens, Senvion, Nordex, Gamesa, Enercon, GE); 2D/3D plotter; safe passes & site inductions; PlantPredict integration (solar modeling).
- Clir: Clir Portfolio / Enhance / Associate product names; 350+ GW proprietary dataset claim; AI Layer framing; anti-reflective-coating insight case (solar-side example).
- ONYX: fleetMONITOR / fieldPRO / ecoBLADE / ecoPITCH / ecoCMS product names; failureATLAS; 32,000+ turbines / 45+ countries / 15 CMS hardware types / $14B claims; bp Wind downtime-reduction percentages (70% downtime / 30% derated days — vendor claims); Pattern 4.2 GW AI Hub; Aviva insurance partnership.
- Power Factors: Unity / REMI naming; pillar structure; 600+ customers claim.
- Vestas: VestasOnline / Scipher / VestasDeveloper / ShopVestas names; multibrand 6 GW claim.
- PulseSense: Wind PulseSense / Swarm / Hydro PulseSense naming; 15 GW / 6,000 assets claims.

## Vendor-specific Findings

See L3. Additionally: Bazefield's "control room" self-description and SSE onshore-wind control-room deployment show the operator pole selling into the control-room seat while remaining a management layer; Clir's dispute-ready framing shows the adversarial-symmetric OEM relationship institutionalized in software; ONYX's growth path (sensing → monitoring → case management → consultancy) shows a condition-monitoring specialist expanding **into** the Type rather than being a separate species.

## Rejected Findings (not definitional)

- **AI / agentic optimization** (REMI, Clir AI, ONYX AI Hub) — era-current packaging over the same spine.
- **Digital twins** — implementation texture.
- **CMS sensing hardware** — the detection substrate; its presence defines a pole, not the Type.
- **Wake steering / yaw control** — control substrate (PulseSense Swarm).
- **Multi-vendor SCADA integration as a defining requirement** — it is the modern substrate problem, but the paper-era operator satisfies the Type without it; the invariant is the fleet record, not the pipe.
- **IEC 61400-25 data model specifically** — Bazefield's implementation choice; other products integrate OEM SCADA differently.
- **Offshore-specific machinery** — segment texture.
- **Invoicing/billing engine** — pole-variable (present at full-suite pole; absent at operator and reliability poles as claimed on fetched pages).
- **Wind-farm design/siting** — upstream lifecycle, different surface.
- **Availability formula specifics (time-based vs production-based definitions)** — real and consequential, but the exact formulas are contractual/standard detail not asserted here (no Tier-1 source fetched states them).

## Boundary Findings

1. **Renewable Energy Asset Management** — population seam. The four-leg spine is identical; the wind population binding is the seam. Keep-both RATIFIED: this pass confirms the solar pass's symmetry prediction with wind-native first-hand evidence (a wind-native vendor family — ONYX purely wind, Bazefield wind-heritage, Clir wind-origin — sells the same spine with wind-specific texture: power-curve analytics, contractual-availability reconciliation vs OEMs, FSA shadow monitoring, CMS/end-of-warranty machinery). Vendor populations partially overlap (multi-tech suites serve wind fleets), mirroring the solar↔REAM pattern, unlike the disjoint PPM↔REAM seat seam.
2. **Power Plant Management** — seat seam (ratified in prior passes, consistent here): dispatch-operations seat with expectation anchored on dispatch schedules/market awards vs owner asset-management seat with expectation anchored on the wind resource and the budget. Not re-litigated; no conflict found.
3. **OEM digital services / turbine SCADA (Vestas-class)** — below/beside the Type. The OEM ships portals and analytics over its own fleet (VestasOnline, Scipher) and exposes operations data via APIs (VestasDeveloper); it also sells the service (multibrand, FSA-class) that the owner's system oversees. The owner-side Type is OEM-agnostic, holds the owner's independent record, and exists partly to check the OEM's numbers. Remove the owner seat and multi-OEM record → OEM portal, not this Type.
4. **CMS / condition-monitoring specialists** — sensing-and-detection substrate feeding the availability record; a specialist can grow into the Type by adding the fleet record, case management and money texture (ONYX demonstrates the full path). A pure CMS product without the four legs stays below the Type.
5. **Wind-farm design / siting tools (WindPRO class)** — upstream lifecycle: resource assessment, layout, design-time energy yield. The design-time estimate becomes this Type's expectation baseline ("outdated pre-construction assumptions" — Clir). Evidence indirect (EMD unreachable); reduced strength.
6. **Performance-optimization specialists (PulseSense/WindESCo lineage)** — optimization-led adjacent pole: hidden-underperformance detection (leg-2 analytics) and wake-steering control (control substrate); no fleet system of record with commercial context, no money/stakeholder loop on fetched pages.
7. **CMMS / Field Service Management** — work-order execution and maintenance logistics; this Type coordinates, delegates and tracks to closure, then hands over (Bazefield "integrated to a maintenance system if required"; ONYX case management tracks but field execution is field teams; Power Factors ships FSM as a sibling pillar).
8. **Energy Trading / Energy Scheduling & Settlement** — the commercial book and market-facing settlement vs this Type's asset-side revenue resolution; interlock at settlement data (consistent with REAM pass; not re-sampled here).
9. **VPP / DERMS** — aggregated third-party-resource portfolios vs the owned wind fleet; the VPP pass's removal test ("restrict to one asset class owned by the operator with production/availability/maintenance semantics → those Types") passes from this side.
10. **Utility Asset Management / EAM** — network-plant registries with no production-vs-resource semantics.

## Historical / Market-Sample Check

Paper-era wind farm operator (1990s Danish/German/early-US wind farms): turbine log sheets and OEM service correspondence against an availability guarantee in the turbine supply agreement; monthly production compared with expected energy from met-mast wind measurements and the turbines' power curves; invoices to the offtaker; O&M cost tracking; reports to owners (in the cooperative case, to member-owners). All four legs present with no software beyond spreadsheets/paper — the definition must not require multi-vendor SCADA platforms, AI, digital twins, CMS hardware, or cloud delivery. Single-turbine cooperative ownership (Denmark) passes as the minimal-scale extreme. OEM-SCADA-only operation (owner running on the OEM's portal + spreadsheets) also satisfies the legs — confirming the OEM portal is a sufficient-but-not-defining substrate. Regional breadth: onshore and offshore, European/US/Asian fleets, all fit. **Historical check passed.**

## Uncertainties

- EMD WindPRO unreachable — design-tool boundary documented indirectly only.
- Historical WindESCo product surface unreachable (domain redirects to PulseSense Dynamics) — recorded as market-structure evidence only.
- No Tier-1 operational manuals reached for any sampled product; workflow/rule claims calibrated to official product/marketing pages; precise availability formulas, numeric limits and state taxonomies intentionally not asserted.
- Whether any wind product carries a **definitional** money leg deeper than pole-variable (e.g., settlement-grade invoicing as standard) — evidence shows invoicing only at the full-suite pole; treated as optional.
- Power Factors' wind-specific depth rests on the REAM pass's probes (3megawatt redirect) plus homepage customer logos; no wind-specific product page fetched (404 on guessed URL).
- IEC 61400-26 (availability state categories) not directly fetched; referenced only via Bazefield's "IEC-61400" mention — standard-level detail not asserted.

## Final Synthesis

**Wind Asset Management is confirmed as a population specialization of Renewable Energy Asset Management: the wind fleet owner/operator's management system of record, running the same four-leg generation-management spine — wind fleet record · production managed against wind-resource expectation · availability record & restoration · money & stakeholder resolution — with the wind population as the binding and wind-native market texture (multi-OEM turbine fleets, power-curve analytics, contractual-availability reconciliation against OEM calculations, FSA shadow monitoring, CMS/end-of-warranty machinery, onshore/offshore segments) as the realization layer.** Keep-both with the technology-generic sibling; seat seam with Power Plant Management unchanged; OEM digital services, CMS specialists, design tools, optimization specialists, CMMS, trading and VPP all held as boundaries. No directory change.
