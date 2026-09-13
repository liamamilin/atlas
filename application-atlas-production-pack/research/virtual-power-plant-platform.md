# Research Notes — Virtual Power Plant Platform

## Research Goal

Understand what a Virtual Power Plant (VPP) Platform actually is as an Application Type: who operates it, what objects exist inside it, what work it drives (aggregate → forecast → optimize → bid/dispatch → measure → settle?), and where its boundary lies against neighboring Types — especially DERMS (§19, processed — joint-review flag carried), Demand Response Platform (§19, processed — joint-review flag carried), Power Plant Management (§19, processed — seam note carried), Energy Management System / EMS (§19, processed — name-collision joint-review flag carried), Energy Trading Platform (§19, processed), Battery Energy Storage Management / Renewable-Solar-Wind Asset Management (§19, unprocessed), EV Charging Network Management (§19, unprocessed), Customer Energy Management (§19, processed), and AMI/MDMS (§19, processed).

Three prior passes issued joint-review flags that this pass must resolve:

1. **demand-response-platform (2026-09-07):** sampled DR products self-label as "VPP platform" while running the DR program spine; proposed discriminator = continuous multi-value optimization of an aggregated DER fleet (VPP) vs called compensated events with program/settlement machinery (DR).
2. **derms (2026-09-07):** proposed purpose discriminator = DERMS coordinates DER behavior within distribution-grid constraints for grid operations; VPP centers continuous commercial optimization of an aggregated DER fleet across market value streams; center-of-gravity decides, not vendor vocabulary.
3. **power-plant-management (2026-09-09):** proposed discriminator = owned utility-scale generation fleets (PPM) vs aggregated distributed-resource portfolios (VPP).
4. **energy-management-system-ems (2026-09-08):** EMS name collision (grid control-center vs site/microgrid pole); joint review recommended with this leaf among others.

## Initial Boundary (hypothesis before research)

- A VPP platform is software through which an operator (aggregator, utility, DER brand, asset owner, trader) aggregates many distributed energy resources — solar, wind, batteries, EV charging, flexible loads, C&I assets, small generation — into a single dispatchable "virtual" power plant, and operates that plant as a commercial resource: forecasting its capability, optimizing its deployment across value streams (wholesale energy, balancing/ancillary, capacity, retail programs, distribution services), dispatching it, measuring delivery, and settling revenue with asset owners.
- Easily confused with: DERMS (grid-coordination purpose), DR platforms (called events under programs), energy trading (market positions without the fleet), site/microgrid EMS (one site), power-plant management (owned utility-scale fleets), single-asset-class management Types.
- Expected core objects: DER asset/fleet record, capability/commitment, forecast, optimization/schedule, bid/offer, dispatch instruction, measurement/performance, revenue/settlement.
- Unknowns: whether "multi-value" is definitional or common; whether direct device control is definitional; how deep market bidding penetrates the definition; whether participant compensation is definitional; how the utility-pole products (DERMS-branded VPP builders) fit.

## Research Questions

1. What is "the plant" as an object — what does the fleet record carry (assets, capability, ownership, site, constraints)?
2. What value streams do these platforms sell into (wholesale energy, balancing/ancillary, capacity, retail programs, distribution services, bill savings)? Is multi-stream stacking definitional?
3. What does the optimization layer decide (schedules, bids, dispatch allocations), on what inputs (forecasts, prices, constraints), and at what cadence?
4. How are assets onboarded (enrollment, prequalification, utility authorization, device connection)? What commitments are recorded (nominations, capability)?
5. How does dispatch reach assets (direct control, partner APIs, aggregator chains, telecontrol)? Is direct control definitional?
6. How is delivery measured and settled (baselines, performance, revenue reports, owner compensation)?
7. Who operates the platform (aggregator/CSP, utility, DER brand, asset owner, trader) and what surfaces does each get?
8. Where are the exact seams vs DERMS / DR / trading / PPM / site EMS / single-asset Types?
9. Historical check: do pre-AI, telecontrol-era aggregation pools (European CHP/biogas pools, direct-load-control fleets) satisfy the minimal definition?

## Representative Products

Selected to cover the market's realization poles, customer tiers, and philosophies. Web search was usable in this pass (unlike the derms/demand-response passes); several large-vendor sites remained unreachable (recorded under Source-access limitations).

| Product | Pole | Customer tier | Why sampled |
|---|---|---|---|
| Leap | Software-only API platform; partners (tech brands) build VPPs under their own brands | DER platform companies (residential + C&I fleets) | Richest public operational documentation (Tier 1 developer docs); the "VPP-as-API" pole; multi-market value-stack machinery |
| Next Kraftwerke (Next Pool) | European VPP operator pooling third-party plants, consumers and storage; own trading floor | Plant owners (biogas, CHP, wind, solar, batteries), C&I consumers, TSOs | The classic operator-pool pole; documents the full loop (connect → prequalify → optimize → dispatch → revenue) without AI framing — best historical-anchor product |
| CPower | C&I aggregator/CSP self-labeling as a "Virtual Power Plant Platform" | Commercial & industrial energy users, DER project developers | The aggregator-services pole; carries the naming-drift evidence for the DR seam; program menu = value-stream taxonomy |
| EnergyHub | Utility-facing SaaS ("Edge DERMS") building VPPs from customer-owned BTM DERs | Utilities (US + Canada) | The utility VPP-builder pole; documents forecast→optimize→dispatch loop and the VPP-strategy taxonomy; the triple-seam product (DR/DERMS/VPP labels) |
| Fluence Mosaic | Market-bidding/optimization engine for storage portfolios (per-market editions) | Storage asset owners, QSEs, trading desks | The optimization/bidding layer as a standalone product — anchors the seam vs Energy Trading and shows the optimization layer can be unbundled |

Cross-reference products (evidence from search results and/or prior passes, used for breadth not spine): OATI DERMS ("Enterprise DERMS: One VPP Platform from Grid Edge to Markets"), ABB OPTIMAX for VPP, Uplight VPP, AspenTech OSI DERMS VPP brochure, Cirrus Flex (SGS), SolarEdge Grid Services/VPP API, OpenADR (standard, from the demand-response pass).

Rejected/abandoned alternatives: Tesla Electric / Autobidder (tesla.com 403), Uplight (403 — same as prior passes), ABB (403), OATI (timeout ×2), SolarEdge (403), sonnen (404), GE Vernova/Siemens/Hitachi (unreachable in prior passes; not retried). Recorded as source-access limitations, not product judgments.

## Sources

Research date: 2026-09-10. Evidence marks: A = directly observed on an official source; B = cross-product commonality; C = canonical inference. S = search-result snippet of an official page (degraded evidence — page itself not fetched).

- Leap — root (https://www.leap.energy/), Product (…/product), Why VPPs (…/vpps), Market Access (…/product/marketaccess); developer documentation home (https://developer.leap.energy/docs/home — meter journey Onboard→Manage→Transact→Monetize). Deeper API object detail (enrollment, nominations, bidding, dispatch, performance, revenue) previously documented Tier-1 in research/demand-response-platform.md (2026-09-07) and reused as cross-reference.
- Next Kraftwerke — root (https://www.next-kraftwerke.com/), VPP Concept & Technology (…/vpp/virtual-power-plant), Balancing Energy (…/products/balancing-energy)
- CPower — Virtual Power Plant Platform page (https://cpowerenergy.com/virtual-power-plant-platform/)
- EnergyHub — Platform Overview (https://www.energyhub.com/edge-derms-platform/platform-overview); prior-pass documentation in research/derms.md and research/demand-response-platform.md (2026-09-07)
- Fluence Mosaic for ERCOT (https://fluenceenergy.com/mosaic-for-ercot/; product family at …/mosaic-intelligent-bidding-software/)

**Snippet-level sources (S — official pages surfaced via search engine but not directly fetchable):**
- OATI DERMS (https://www.oati.com/grid-solutions/derms/) — "Enterprise DERMS: One VPP Platform from Grid Edge to Markets"; program-manager console (define program rules, self-service enrollment portal, validate enrollments, configurable baseline and settlement engine); operator picture (ADMS/AMI/IoT-SCADA united, geospatial heat map, 7-day load forecast, live load curve, event calling with per-program call-count tracking); market desk (real-time/day-ahead prices, build VPP manually or automatically, forecast capability, submit offers, reconcile and settle); executive rollup. Direct fetch timed out ×2.
- ABB OPTIMAX for Virtual Power Plants (new.abb.com …optimax-for-virtual-power-plants) — "seamlessly aggregates and integrates decentralized generation, flexible loads, and storage systems… into a virtual power plant"; automatic asset dispatch and real-time control; ancillary-service distribution (mFRR, aFRR, FCR); schedule disaggregation; day-ahead and intraday optimization; forecasting and trading; reports to billing system per asset/market/customer. Direct fetch 403.
- Uplight VPP (https://uplight.com/solutions/virtual-power-plant/) — vendor VPP definition ("aggregation of multiple energy asset types and customer segments… operated like a conventional power plant to support a wide range of grid services year-round"); explicit VPP-vs-DR distinctions (multiple asset types vs single resource; multiple grid services vs peak-load reduction; dispatchable year-round vs seasonal). Direct fetch 403 (consistent with prior passes).
- AspenTech OSI DERMS VPP brochure PDF (aspentech.com media library) — "Virtual power plants are logical groupings or aggregations of DERs that can provide traditional grid services similar to a traditional power plant—including energy market participation"; multiple objective functions for grid operations and market participation; DER types (SCADA-controlled backup generators, fuel cells, batteries, large solar/wind, BTM aggregations, DR programs, EVs); native integration with monarch SCADA, GMS, EMS, ADMS; IEEE 2030.5/OpenADR/DNP3. PDF fetch returned binary; content from search snippet.
- Cirrus Flex (SGS) brochure PDF (agilitycms cloud CDN) — "cloud hosted Virtual Power Plant (VPP) platform" for DER owners; stacked revenue streams across energy/flexibility markets; configurable optimization with customer-specified objective functions; opt-in/opt-out from events; settlement/baseline/performance data stores; dynamic grouping by DER type/zone substation/ISO node. PDF not fetched; content from search snippet.
- SolarEdge Grid Services (solaredge.com …/services/grid-services) — aggregator-facing VPP APIs (fleet-level management, market response for wholesale/capacity/imbalance, dispatch programs from price plans, PV Live monitoring). Direct fetch 403; content from search snippet.

**Source-access limitations (recorded):**
- OATI, ABB, Uplight, SolarEdge, Tesla pages unreachable (403/timeout); AspenTech/Cirrus Flex PDFs not parseable. Their evidence is snippet-level (S) and used only for breadth and seam documentation, never for the defining core.
- No sampled product exposes a full operational user manual; Leap's developer docs are the deepest Tier-1 source and are aggregator-side (partner API), not operator-console UI. Console semantics for utility/enterprise poles rest on product pages and snippets — assertion strength kept moderate.
- Vendor numeric claims (Next Kraftwerke 14,375 units / 15.1 TWh 2024 / 7 TSO areas; Leap "87% more $/kW"; DOE 80–160 GW by 2030) recorded here as vendor/third-party claims only; kept out of the final document.
- Market-rule specifics (balancing-product prequalification details, baseline formulas, penalty schedules) not researched; not asserted.

## Product A — Leap (evidence layer A, Tier 1 + Tier 2)

Positioning: software-only platform; "Leading technology brands partner with Leap to earn new revenue in energy programs"; "Turn your distributed energy resources into revenue"; "Build and scale your virtual power plants." (A)

- **VPP definition (vendor's own):** "networks of hundreds, thousands, or even millions of distributed energy resources (DERs) aggregated together to operate like traditional power plants, delivering energy and capacity to the grid." (A)
- **The operating loop (vendor-documented, 4 steps):** 1. "Virtually aggregate DERs from across our partner network" → 2. "Sell energy and capacity into relevant energy markets" → 3. "Signal partners to dispatch customers during grid events" → 4. monetize. (A)
- **No-hardware posture:** "No hardware required… software-only solution integrates with your existing systems"; "Bring your own device"; "No load minimums — even very small energy devices can earn grid revenues." (A) — the fleet is composed through partner integrations, not owned gateways.
- **Meter journey (Tier 1):** Onboard (add meters for program enrollment) → Manage (sync inventory, manage participation) → Transact (participate in grid events) → Monetize (assess performance and revenue). Meters are "the basic units of inventory providing grid services," representing end customers and devices behind the utility meter. (A; consistent with the demand-response pass's Tier-1 documentation of enrollment/nominations/bidding/dispatch/performance/revenue objects)
- **Value-stack machinery:** "One interface, many markets — stack value by participating in multiple markets and programs"; market pages enumerate per-market revenue options (ERCOT ERS + utility programs + economic price-signal dispatch; New England utility programs + Clean Peak Standard; NYISO + utility programs; California DSGS + CAISO energy + capacity + emergency; PJM capacity). End-to-end process named: "Engagement, Bidding, Opportunity Sizing, Dispatching, Insights, Payments." (A)
- **Dispatch posture:** partners "receive dispatches from Leap and use their controls software to change device behavior" — dispatch is partner-mediated; the platform also lets partners "bid fast-responding, highly flexible resources into real-time markets." (A)
- **Monetization:** "Detailed performance insights… detailed and predictive performance analytics"; revenue & analytics product line. (A; settlement object detail from prior pass: monthly revenue reports preliminary→FINALIZED, per meter/customer/market, missed vs potential revenue)

## Product B — Next Kraftwerke / Next Pool (evidence layer A, Tier 2)

Positioning: "As one of the largest Virtual Power Plants in Europe, we network thousands of decentralized electricity generators, consumers and storage units… With our own trading floor, we trade on various European power exchanges and provide balancing power for grid stabilization." (A)

- **VPP definition (vendor's own):** "a network of decentralized, medium-scale power generating units as well as flexible power consumers and storage systems." Objective: "network distributed energy resources such as wind farms, solar parks, and CHP units, in order to monitor, forecast, optimize and trade their power." (A)
- **Why aggregation exists (the Type's economic rationale, vendor-stated):** "Individual small plants can in general not provide balancing services or offer their flexibility on the power exchanges… their generation profile varies too strongly or they simply do not meet the minimum bid size of the markets. By aggregating the power of several units, a VPP can deliver the same service and redundancy and subsequently trade on the same markets as large central power plants or industrial consumers." (A)
- **Control system (the technological core):** central system monitors, coordinates and controls all networked assets; stores the data needed to compute optimal operation schedules (actual power, readiness, performance range for balancing energy, gas/heat storage, temperatures, water levels); "uses a special algorithm to adjust to balancing reserve commands from transmission system operators, just as larger conventional power plants do"; real-time data feeds forecasts "for electricity trading and scheduling of the controllable power plants." (A) — optimization is algorithmic but not framed as AI/ML; schedules + balancing-order response.
- **Asset connection (own gateway):** the Next Box remote control unit (PLC + modem + antenna) connects plants via encrypted, tunneled wireless using IEC 60870-5-104 telecontrol over SIM/APN closed user group. (A) — hardware-gateway pole vs Leap's software-only pole.
- **Ownership boundary (load-bearing quote):** "Even though we are able to control the networked units via the Next Box, the individual units remain independently owned and operated." (A) — the "plant" is virtual: composed of third-party assets the operator does not own.
- **Value streams (product menu):** Power Trading (market access to major European power exchanges), Balancing Energy (ancillary services in 7 European TSO areas), Power Scheduling (scheduling of steerable assets/flexible consumption). (A)
- **Onboarding lifecycle (vendor's 3 steps):** 1. Connection (encrypted Next Box link) → 2. Prequalification (unit technically/functionally checked against the TSO transmission code) → 3. Revenues ("the asset owner receives revenues according to his contribution to grid stability"). (A)
- **Dispatch semantics:** on frequency imbalance the VPP "will receive an order from the TSO requesting a certain amount of power"; asset requirements: continuous power production, remote control, fast reaction. C&I demand response: "The operator or factory owner sets the restrictions in which the process can provide flexibility. The actual call for flexibility only uses a fraction of the entire consumption process." (A) — owner-set constraints bound dispatch.
- **Scale claims (vendor, research notes only):** 14,375 aggregated units, 2,555 MW aggregated flexibility, 15,541 MW networked capacity (Q4/2025), 15.1 TWh traded energy (2024), 7 TSO areas. (A, vendor claims)

## Product C — CPower (evidence layer A, Tier 2)

Positioning: "CPower's Virtual Power Plant Platform — Turn Energy Flexibility into Revenue, Resilience and Sustainability"; "CPower connects your energy assets to programs that value flexibility." (A)

- **VPP definition (vendor's own):** "A network of energy assets such as onsite generation, HVAC systems, lighting, solar, microgrids, energy storage, industrial operations and EV charging infrastructure. These customer resources participate in demand response and on-bill programs, responding to changing grid dynamics and generating revenue and savings for both energy users and DER project developers whenever their flexibility is called upon." (A) — note: the vendor's VPP is defined through DR/on-bill program participation; "whenever their flexibility is called upon" is event language. Naming-drift evidence for the DR seam.
- **Value-stream menu:** Capacity (available to be dispatched under peak/scarcity), Energy (reduce demand or inject when prices are high), Ancillary Services (paid to be available to balance), Demand Charge Management (shift use away from peaks). (A)
- **Operator-as-service:** "CPower manages your market participation, risk and performance so your assets earn while you stay focused on your core business"; curtailment plans per customer; performance fine-tuning. (A)
- **Platform promise:** "streamline your energy market activity, maximize revenue and savings, ensure performance and compliance, and track every payment with confidence." Participant portal (CPower CONNECT). (A)

## Product D — EnergyHub (evidence layer A, Tier 2; prior-pass cross-reference)

Positioning: "The premier platform for all your customer-owned DERs… Deliver grid flexibility and reliability using a single VPP across devices." (A)

- **Cross-DER VPP:** "Manage multiple DER classes in one integrated platform" (thermostats, EVs, batteries, C&I); "background aggregation" (enrolling already-installed devices); partner ecosystem of "hundreds of makes and models." (A)
- **Operating loop (vendor-documented):** forecast system-wide load and capacity → ML optimization recommends dispatch schedules across devices (with utility input) → dispatch per recommendations or operator specs → optimize and adjust in near-real time with performance dashboards. (A)
- **VPP-strategy taxonomy (the value-stream list):** demand response, dynamic load shaping, wholesale price optimization, customer rate optimization, distribution load management. (A) — one product spans market, bill, and distribution value streams.
- **Case-study framing:** IESO "Canada's largest residential virtual power plant" (100,000+ homes); APS "cross-DER VPP"; National Grid pay-for-performance battery program. (A, titles)
- Prior passes documented: utility-systems REST gateway; GE Vernova GridOS DERMS two-tier partnership; integrated program services (design, marketing, partner management). (A, prior)

## Product E — Fluence Mosaic (evidence layer A, Tier 2)

Positioning: "Optimized bidding solutions for energy storage in ERCOT… captures revenue across energy and ancillary services with AI-powered bidding software and trading solutions." Per-market editions (CAISO, ERCOT, MISO, NEM, Japan). (A)

- **The optimization layer in isolation:** forecasting (ML price forecasts from market behavior, prices, weather, load) → optimization ("calculates the optimal bids for market products, considering price forecasts, operational constraints, and business objectives") → bidding ("creates market-compliant bids and makes them available for the Qualified Scheduling Entities (QSEs) or customer's trading desk"). (A)
- **Fleet semantics:** technology-agnostic across providers; "configured to meet the unique warranty constraints and operating parameters of each asset"; co-optimization across energy and ancillary products in day-ahead, managing contracted commitments; warranty constraints and degradation costs inside the optimization. (A)
- **Trading-desk posture:** simulation environment, adjustable risk profile, visibility into bidding decisions "across your organization." (A) — the commercial book stays with the customer's desk/QSE; Mosaic is the fleet-side optimization/bidding engine, not the book of record.

## Cross-product Comparison

| Structure | Leap | Next Kraftwerke | CPower | EnergyHub | Fluence Mosaic | Layer |
|---|---|---|---|---|---|---|
| Aggregated DER fleet as one managed portfolio | "virtually aggregate DERs from across our partner network"; meters as inventory units | "network of decentralized… generating units… flexible consumers and storage"; 14k+ units | "network of energy assets" (onsite generation, HVAC, solar, storage, EV) | "a single VPP across devices"; cross-DER classes | storage portfolio, technology-agnostic | B |
| Assets owned by third parties, not the operator | partners' resources, BYOD | "units remain independently owned and operated" | customer resources | customer-owned DERs | customer's assets (warranty constraints) | B |
| Combined capability offered into external value streams | "sell energy and capacity into relevant energy markets"; multi-market stack | power exchanges + balancing markets (7 TSO areas) + scheduling | capacity/energy/ancillary/demand-charge programs | VPP strategies: DR, load shaping, wholesale, rate, distribution | energy + ancillary products, day-ahead | B |
| Optimization deciding allocation/dispatch | dispatch parameters + real-time market bidding; automation use cases | central control system computes optimal schedules; responds to TSO balancing orders | managed by CPower (plans, fine-tuning) | ML recommends dispatch schedules; near-real-time adjust | ML forecast → optimal bids every market cycle | B |
| Dispatch reaching assets (direct or mediated) | signals partners; partners' controls change device behavior | Next Box telecontrol (IEC 60870-5-104) | curtailment plans, controls in place | dispatch devices via platform/partner ecosystem | bids handed to QSE/trading desk (execution downstream) | B |
| Measurement → revenue settled with owners | performance analytics; monthly revenue reports; "getting paid" | "asset owner receives revenues according to his contribution" | "track every payment"; performance and compliance | performance dashboards; pay-for-performance programs | (bidding layer; settlement downstream) | B |
| Onboarding with capability commitment | meter enrollment, nominations (kW), utility authorization | connection → prequalification (TSO transmission code) → revenue | enrollment under managed participation | enrollment via partner ecosystem; background aggregation | asset configuration (warranty/operating parameters) | B |
| Forecasting feeding decisions | (predictive analytics) | forecasts for trading and scheduling | (managed) | forecast system-wide load/capacity | ML price forecasting | B |
| Multi-stream stacking | "stack value by participating in multiple markets and programs" | trading + balancing + scheduling as one pool's menu | capacity + energy + ancillary + demand-charge menu | five VPP strategies on one fleet | energy + ancillary co-optimization | B |
| AI/ML optimization framing | (automation emphasis) | NOT framed as AI (algorithm + schedules) | (not claimed) | ML optimization | AI-powered (core pitch) | B — varies |
| Own gateway hardware | no (software-only) | yes (Next Box) | (not documented) | no (partner ecosystem) | no | A (two poles) |
| Consumer/participant surfaces | partner-owned customer experience | plant-owner revenue share | CPower CONNECT portal | utility-owned program experience | (none — desk tool) | B — varies |

Reading: six structures repeat across every pole (aggregated third-party fleet as one portfolio; external commercial value streams; optimization-driven allocation/dispatch; dispatch reaching assets directly or through mediators; measurement→revenue settled with owners; onboarding with capability commitments). Everything else — AI/ML framing, gateway hardware, consumer surfaces, specific market machinery — varies by pole and sits above the spine.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being a VPP Platform:

1. **The aggregated DER fleet as one dispatchable resource of record** — identified distributed assets (generation, storage, EV charging, flexible loads) across many sites and owners, enrolled/connected into a persistent portfolio operated as a single "virtual" power plant with a combined capability. The assets remain owned and operated by third parties; the platform holds them as one resource. Remove → single-site EMS, asset monitoring, or a grid-side DER registry (DERMS).
2. **Commercial value-stream participation** — the fleet's combined capability is offered into external value streams (wholesale energy markets, balancing/ancillary services, capacity programs, retail/utility programs, distribution services) as a revenue-earning resource. Remove → internal site optimization (site EMS) or grid-coordination-only (DERMS).
3. **Optimization-driven allocation and dispatch** — the platform decides how to deploy the fleet's capability across its value streams (forecast → optimize → bid/offer/schedule → dispatch) and drives assets directly or through partners/aggregators. Remove → passive aggregation or a manual brokerage.
4. **Measured delivery converted into revenue settled with asset owners** — the fleet's delivered performance is measured against commitment/expectation and converted into revenue/compensation records shared with the asset owners/participants. Remove → a control platform with no commercial loop.

All four are cross-product (layer B): the third-party fleet is explicit in Next Kraftwerke's ownership quote and structural in Leap (partner resources), CPower (customer resources), EnergyHub (customer-owned DERs), Mosaic (customer assets with warranty constraints); value-stream participation is the product menu of all five; optimization-driven dispatch is documented in all five (algorithmic schedules in Next Kraftwerke, ML in EnergyHub/Mosaic, dispatch parameters in Leap, managed plans in CPower); measurement→settlement is documented in four (Mosaic delegates execution/settlement downstream — the optimization layer alone is a component, not the whole Type).

**Jointly-held load-bearing:**
- 1 alone = DER asset inventory / monitoring portal
- 2 without 1 = market-access brokerage with no fleet (energy-trading territory)
- 3 without 1+2 = a generic optimization engine
- 4 without 1–3 = settlement accounting
- 1+2 without 3 = a fleet enrolled in markets but not operated (passive aggregation)
- 1+3 without 2 = internal fleet control with no commercial purpose (site/microgrid EMS)
- 1+4 without 2+3 = monitoring plus payments with no optimization (rewards program)
- 2+3 without 1 = a trading desk with no assets (energy trading)
- 2+4 without 1+3 = program administration (demand response)
- 3+4 without 1+2 = generic dispatch-and-settlement machinery

### L1 — Common Mature Structure (layer B; common but not definitional)

- Forecasting machinery (load, generation, prices, available capability) feeding optimization
- Enrollment/onboarding with capability commitments (nominations, prequalification, utility authorization) and lifecycle states (active, idle, disenrolled)
- Bid/offer construction for market products (day-ahead/real-time energy, ancillary, capacity) with market-compliant formats and deadlines
- Dispatch lifecycle (schedule → signal → execute → confirm) with cancellation and opt-out/voluntary flags
- Performance measurement against baseline/commitment; settlement and revenue reporting per asset/program/market; missed-vs-potential revenue analysis
- Portfolio dashboards: fleet state, available capability, forecasts, revenue
- Partner/device-ecosystem integration (BYOT) and/or direct device control; aggregation chains (platform → aggregator → devices)
- Multi-market/multi-program stacking on one fleet
- Consumer/participant surfaces (owner portals, apps, bill credits, rewards) on the participant side

### L2 — Variant / Optional Structure (segmented)

- Operator pole: aggregator/CSP (CPower), utility VPP-builder (EnergyHub, Uplight, OATI), API platform for DER brands (Leap), European pool operator (Next Kraftwerke), asset-owner platform (Cirrus Flex), OEM/consumer VPP (Tesla-class; unreachable, not sampled)
- Asset-population emphasis: residential BTM (thermostats/batteries/EVs) vs C&I (industrial processes, HVAC) vs utility-scale renewables+storage vs mixed
- Value-stream mix: wholesale-only vs + capacity vs + retail programs vs + distribution services vs + bill savings
- Control depth: direct device control (gateway/telecontrol) vs partner-mediated signals vs schedule-only vs bid-handoff to QSE/trading desk
- Optimization style: ML/AI real-time vs algorithmic schedules + balancing-order response vs managed human plans
- Regional market machinery: ERCOT/CAISO/PJM/NEM products, European TSO balancing products (aFRR/mFRR/FCR class), Clean Peak, DSGS, FERC 2222 — market-specific, not definitional
- Hardware posture: dedicated gateway boxes (Next Box) vs software-only BYOD (Leap)
- Participant compensation shape: revenue share, bill credits, incentives, points

### L3 — Vendor-specific Detail (research notes only)

- Leap: Leap Connect brandable enrollment app; universal API; SOC2 posture; per-market program stacks; "87% more $/kW" partner stat; sonnen ROI case study.
- Next Kraftwerke: Next Box (PLC + modem + antenna, IEC 60870-5-104, SIM/APN closed user group); "the power of many" branding; VPP Simulation tool; REMIT data page; tolling agreements for utility-scale batteries; unit/capacity/TWh stats.
- CPower: CPower CONNECT portal; NRG co-branding; "Estimate My Revenue" tool; industry-vertical menu (data centers, crypto mining, education…).
- EnergyHub: "Edge DERMS" branding; background aggregation; GE Vernova GridOS partnership; integrated services (program design/marketing/partner management); IESO/APS/National Grid case studies.
- Fluence Mosaic: per-market editions (CAISO/ERCOT/MISO/NEM/Japan); QSE hand-off; simulation environment; adjustable risk profile; warranty/degradation-aware optimization; AMS Armada login portals.
- OATI (S): live load curve with per-program call-count tracking; geospatial heat map; 7-day load forecast; Con Edison/TVA/Dairyland case studies; "first DERMS in 2009" claim.
- ABB (S): OPTIMAX branding; schedule disaggregation; mFRR/aFRR/FCR distribution; billing-system reporting per asset/market/customer.
- Uplight (S): Flex DERMS branding; Guidehouse leaderboard citations; M&V same-day feedback; 40+ OEMs / 10+ protocols claims.
- AspenTech OSI (S): DERMS VPP as suite sibling (monarch SCADA, GMS, EMS, ADMS); topology-aware VPPs; DNP3/IEEE 2030.5/OpenADR.
- Cirrus Flex (S): AMPL-based configurable optimization; opt-in/opt-out per event; dynamic grouping by DER type/zone substation/ISO node; Element Flex grid-edge device product.

## Vendor-specific Findings

- **Self-labeling spans the whole DR/DERMS/VPP seam.** CPower (a DR aggregator) titles its product "Virtual Power Plant Platform" while defining the VPP through DR/on-bill program participation; EnergyHub (a DERMS) brands itself a VPP-building platform; OATI (a DERMS) titles its page "One VPP Platform from Grid Edge to Markets"; OSI (a DERMS) ships a "DERMS VPP" brochure; Leap (an API platform) and Next Kraftwerke (a pool operator) use VPP as the primary identity. The label is a marketing continuum; the spine beneath it is stable. This confirms both prior passes' naming-drift observations from the VPP side.
- **The optimization layer can be unbundled.** Fluence Mosaic sells only forecast→optimize→bid for storage portfolios, handing execution to QSEs/trading desks — evidence that optimization/bidding is a separable component of the VPP stack (and the seam vs Energy Trading).
- **Hardware posture is a real fork:** Next Kraftwerke ships its own telecontrol gateway; Leap is explicitly software-only with "no hardware required." Both satisfy the spine — hardware is implementation.
- **AI framing varies from absent (Next Kraftwerke: "a special algorithm") to core pitch (Mosaic, EnergyHub ML)** — era-current maturity, not definition.

## Rejected Findings

- **"VPP = AI/ML real-time optimization"** — REJECTED. Next Kraftwerke, one of Europe's largest pools, describes algorithmic schedules plus balancing-order response without AI framing; the historical pool model (telecontrol era) satisfies the spine. ML is common maturity.
- **"VPP = direct control of every device"** — REJECTED. Leap dispatches through partners' control software; Mosaic hands execution to QSEs; CPower manages participation as a service; Next Kraftwerke controls via optional gateway hardware. Dispatch mediation varies; the allocation decision is the invariant.
- **"VPP = wholesale market participation only"** — REJECTED. EnergyHub's strategy taxonomy includes customer rate optimization and distribution load management; CPower's menu includes demand charge management; value streams span markets, programs, and bills.
- **"VPP requires the operator to own the assets"** — REJECTED. The sampled products uniformly aggregate third-party/customer-owned assets; Next Kraftwerke states it verbatim. Owned-fleet operation is Power Plant Management territory.
- **"VPP = DR program with a new name"** — REJECTED as an equation (see Boundary Findings #2): the DR spine (program → enrollment → called event → baseline → settlement) appears in VPP products as one value stream among several, while the VPP spine (fleet-as-resource, continuous optimization across streams) never appears as the DR platform's own core.
- **"Multi-stream stacking is definitional"** — DOWNGRADED to L1. Every sampled product supports multiple streams, but a single-market pool (e.g., balancing-only) is still recognizably a VPP; the definitional part is commercial value-stream participation, not the count of streams.

## Boundary Findings

1. **vs DERMS (§19, processed — flag DISCHARGED from this side).** The derms pass's purpose discriminator is ratified with direct evidence: DERMS coordinates DER behavior within distribution-grid constraints for grid operations (registry + visibility + dispatch serve the network); the VPP platform operates an aggregated fleet as a commercial resource across value streams (optimization serves revenue/value). The overlap is real and vendor-documented: OATI titles its DERMS "One VPP Platform from Grid Edge to Markets" (program + operator + market desks in one product); OSI ships a "DERMS VPP" brochure ("multiple objective functions… in both grid operations and energy market participation"); EnergyHub (Edge DERMS) builds VPPs for utilities. Center of gravity decides: when the product's organizing purpose is distribution-constraint coordination for grid operations, it is DERMS (even with a VPP module); when it is commercial optimization of the aggregated fleet, it is VPP (even when it also serves distribution constraints). Removal tests both ways recorded.
2. **vs Demand Response Platform (§19, processed — flag DISCHARGED from this side).** The DR pass's discriminator is ratified: DR = called compensated events under programs with baseline→settlement machinery; VPP = continuous multi-value optimization of an aggregated fleet as a resource. Supporting evidence from this pass: Uplight's own VPP-vs-DR distinction (multiple asset types vs single resource; multiple grid services vs peak-load reduction; dispatchable year-round vs seasonal) (S); CPower's VPP defined through "whenever their flexibility is called upon" (event language — the DR spine inside a VPP-labeled product); Leap's DR programs as one stream in the value stack. When dispatch is only called events under compensated programs, the product is DR (whatever it calls itself); when the fleet is operated continuously as a resource across streams, it is VPP. The DR event engine embedded in a VPP is the same machinery — keep both Types.
3. **vs Power Plant Management (§19, processed — seam ratified).** The power-plant-management pass's discriminator is ratified: PPM manages owned utility-scale generation fleets (plant as owned asset; production vs expectation; availability; accounting); the VPP platform aggregates distributed portfolios across many owners (the "plant" is virtual, composed of third-party assets — Next Kraftwerke's ownership quote is the anchor). Edge case: a VPP that aggregates utility-scale batteries under tolling agreements (Next Kraftwerke's ECO STOR/ju:niz deals) — the assets are still third-party (tolling = contracted control, not ownership), and the organizing purpose is commercial optimization, so it stays VPP.
4. **vs Energy Trading Platform (§19, processed).** Trading platforms are systems of record for market positions/books; the VPP platform's record is the fleet and its dispatch. The seam is bidding: a VPP may construct and submit bids (Leap's bid API; Mosaic's bid generation) as the fleet's commercial act, while the position/book stays with the trading desk or QSE (Mosaic explicitly "makes bids available for the QSEs or customer's trading desk"). When the product's center of gravity is the book/positions and the assets are just an execution channel, it is trading (Mosaic-class bidding engines sit on this seam).
5. **vs Energy Management System — site/microgrid pole (§19, processed; EMS name-collision flag addressed from this side).** The site/microgrid EMS pole orchestrates one site's or enclave's assets for that site's objectives (cost, resilience, islanding); the VPP platform aggregates across many sites and owners for external commercial value. Removal test: restrict the fleet to one site → site EMS. The grid control-center EMS pole (transmission balancing) is not confusable once scope is stated. The EMS pass's joint-review recommendation is answered: the VPP Type is distinct from both EMS poles; the site/microgrid split-leaf decision remains with the EMS pass.
6. **vs Battery Energy Storage Management / Renewable-Solar-Wind Asset Management (§19, unprocessed — flag issued for those passes).** Those Types (per the power-plant-management pass's evidence) own operations of one asset class for a fleet owner (production, availability, maintenance, accounting). The VPP platform coordinates across asset classes as a commercial portfolio, usually for assets it does not own. Removal test: restrict to one asset class owned by the operator with production/availability/maintenance semantics → those Types. Joint review recommended when those leaves are processed.
7. **vs EV Charging Network Management (§19, unprocessed).** Charger-network operations (chargers, sessions, roaming, billing) vs flexibility participation of charging load as fleet capacity. Leap's EV-charging partner line shows the seam: the VPP platform enrolls and dispatches charging flexibility; it does not operate the charger network.
8. **vs Customer Energy Management (§19, processed).** CEM serves the customer's own continuous usage-insight loop; the VPP platform serves the operator's fleet-commercial loop. Participant surfaces (enrollment, rewards, bill credits) in VPP products are participant surfaces of the fleet business, not the CEM core — consistent with the demand-response pass's discharge.
9. **vs AMI / MDMS (§19, processed).** Meter data is one measurement input (Leap's utility-meter measurement point); the data path does not change the Type.
10. **vs Utility Billing / CIS (§19, processed).** VPP settlement is program/market revenue shared with owners; bill credits are a delivery channel (CPower "on-bill programs"), not the utility bill of record.

### "去掉什么就变成另一个 Type" 判据 (removal tests)

- Remove the aggregated third-party fleet (single owner's plant) → Power Plant Management / single-asset Types.
- Remove commercial value streams (grid-constraint coordination only) → DERMS.
- Remove continuous fleet optimization (called events only) → Demand Response Platform.
- Remove the fleet (positions/book only) → Energy Trading Platform.
- Remove multi-site aggregation (one site) → site/microgrid EMS.
- Remove optimization-driven dispatch (passive listing) → DER monitoring portal / aggregation brokerage.
- Remove measurement→settlement → a control platform with no commercial loop.

## Historical / Market-Sample Check (§24)

- The VPP label is 2000s-era, but the minimal form predates the AI era and is directly documented by the sample's oldest-pole product: Next Kraftwerke (founded 2009) describes a pool of third-party CHP/biogas/renewable units connected by telecontrol (IEC 60870-5-104), scheduled by a central control system algorithm, dispatched against TSO balancing orders and traded on power exchanges, with owners paid "according to his contribution." No AI/ML, no cloud consumer apps, no FERC 2222 — the spine (fleet-as-resource + commercial streams + optimization-driven dispatch + measurement→revenue) is fully present. → AI/ML optimization, cloud SaaS, consumer apps, FERC 2222 machinery, and OpenADR-class protocols are NOT definitional.
- The pre-digital ancestry also passes: an aggregator manually scheduling a pool of distributed generators against market prices and settling with plant owners (phone/fax era) satisfies all four L0 structures. The "virtual" in VPP is the composition of the plant from third-party assets, not any specific technology.
- Regional check: the sample spans US markets (ERCOT/CAISO/PJM/NYISO/ISO-NE class), European TSO balancing markets, and Australia (NEM, via Mosaic editions) — no single market's machinery is definitional.
- The utility pole (EnergyHub/Uplight/OATI) demonstrates the Type inside utility program contexts without changing the spine: the utility acts as the VPP operator, customer DERs as the fleet.

## Uncertainties

- No full operational user manual was fetchable for any sampled product; Leap's developer docs (aggregator-side API) are the deepest Tier-1 source. Operator-console semantics for the utility/enterprise poles rest on product pages and search snippets — assertion strength kept moderate in the final document.
- OATI, ABB, Uplight, SolarEdge, Tesla evidence is snippet-level (S); used for breadth and seam documentation only, never for the defining core. Tesla's consumer/OEM pole (Tesla Electric, Autobidder) is therefore asserted only as "a known market pole," not from direct evidence.
- Whether every VPP platform carries participant-facing compensation surfaces is unclear (Leap's partner-owned CX; EnergyHub's utility-owned CX; Mosaic has none) — participant surfaces kept at L1/L2, not L0.
- The exact split of bidding authority between VPP platform, QSE, and trading desk is deployment-specific (Mosaic documents the hand-off; Leap documents platform-managed bidding; Next Kraftwerke trades in-house) — final-document wording kept at "bidding may be platform-managed or handed to a market intermediary" strength.
- Interconnection, hosting-capacity, and grid-constraint machinery were not evidenced in the VPP sample beyond EnergyHub's distribution-load-management strategy — not claimed as part of the Type.
- Penalty/non-performance mechanics (capacity-test consequences, shortfall penalties) observed only as hints (CPower "ensure performance and compliance"; Leap capacity tests in settlement) — qualified phrasing only.

## Final Synthesis

A Virtual Power Plant Platform is the operator-side system for running an aggregated fleet of distributed energy resources as one commercial power plant: it holds a persistent portfolio of third-party-owned assets (generation, storage, EV charging, flexible loads) across many sites as a single dispatchable resource with a combined capability; it offers that capability into external value streams (wholesale energy markets, balancing/ancillary services, capacity programs, retail/utility programs, distribution services); it continuously decides how to allocate and dispatch the fleet across those streams (forecast → optimize → bid/schedule → dispatch, reaching assets directly or through partners and aggregators); and it measures what the fleet delivered against commitment and converts it into revenue settled with the asset owners. Its defining core is exactly four structures — the aggregated third-party fleet as one resource, commercial value-stream participation, optimization-driven allocation/dispatch, and measured-delivery-to-revenue settlement — realized across distinct market poles (API platform for DER brands, European pool operator, C&I aggregator, utility VPP-builder, asset-owner platform, storage bidding engine) that all share the same spine. AI/ML optimization, gateway hardware, consumer surfaces, specific market machinery, and multi-stream stacking are common or optional maturity above the spine, not definition. The seams: DERMS coordinates DER behavior within distribution-grid constraints for grid operations; DR platforms call compensated events under programs; trading owns the market book; power-plant management runs owned utility-scale fleets; site/microgrid EMS orchestrates one site; single-asset Types own one asset class for its owner; AMI owns meter data; billing owns the bill.
