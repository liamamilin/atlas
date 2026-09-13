# Research Notes — District Energy Management

Research date: **2026-09-07**

---

## Research Goal

Understand what real-world software the directory leaf "District Energy Management" refers to: what applications exist for operators of district heating / district cooling networks, what objects they manage, how the operational loop works, and where the boundary lies against neighboring Types (EMS / DMS, SCADA, Energy Forecasting, Demand Response, Virtual Power Plant, Building Energy Management, Customer Energy Management, Utility Billing).

---

## Initial Boundary

Working hypothesis before research:

- **What**: operator-side (utility-side) software for a *shared thermal energy network* — centralized production (CHP plants, boilers, heat pumps, storage) + a distribution network (pipes, pumps) + many connected consumption points (substations / buildings).
- **Who**: district heating / cooling utilities, typically municipally owned energy companies.
- **Confusable with**: Energy Management System / EMS (electrical), DMS / ADMS (electrical distribution), SCADA, Energy Forecasting Platform, Demand Response Platform, VPP Platform, Building Energy Management, Customer Energy Management, Utility Billing Platform, Water Utility Management (structural analogy).
- **Unknowns**: whether the market term "district energy management" is actually vendor usage; whether the Type is monitoring-centric, optimization-centric, or planning-centric; whether demand-side (substation/building) modules belong inside the Type.

---

## Research Questions

1. What does "district energy" cover — heating only, or cooling / steam / CO₂ grids as well?
2. What are the core objects (production units, network, delivery points, forecasts, plans)?
3. What is the operational loop: how do forecasts, measurements, and plans connect?
4. What role does the network model / digital twin play?
5. Why do supply temperature and thermal storage appear so prominently?
6. How does the demand side (substations, buildings) relate to the network operator's system?
7. Who uses the software (roles)?
8. Where are the boundaries vs electric-grid Types, forecasting, DR/VPP, building-side, billing?
9. Historical check: would older / regional / platform-native products still fit the definition?

---

## Representative Products

Selected (market representativeness + documentation reachability + different product philosophies + different poles of the Type):

| Product | Vendor | Country | Pole represented |
|---|---|---|---|
| Digital Twin Platform | Gradyent | Netherlands | real-time network digital twin (production → network → end users) |
| Leanheat® Software Suite | Danfoss | Denmark | modular suite: production forecasting/optimization + thermo-hydraulic network modeling + system monitoring + building-level demand side |
| Energy Optima 3 | Energy Opticon AB | Sweden | economic total optimization / production planning + power-market coupling (since 1992, 50+ utilities) |
| energyPRO | EMD International | Denmark | offline design / feasibility / scenario modeling of district heating systems (boundary-adjacent sample) |

Rejected / mismatched samples (recorded for honesty):

- **NODA (noda.ai)** — today an agentic-AI building-operations product (BMS fault detection, portfolio optimization). **Product Mismatch**: building-side, not district-network operator software. (The Icelandic district-heating lineage of the name was not verifiable in this pass.)
- **Process Vision (processvision.com)** — natural-gas pipeline inspection cameras (LineVu). **Product Mismatch** — different domain entirely.
- **TERMIS (Schneider Electric)** — district heating/cooling network simulation & operation tool; **source unreachable** (HTTP 403 on se.com product page). The network-modeling pole is covered by Gradyent + Leanheat Network + Energy Optima's topology editor, so the sample stands at four.

---

## Sources

All fetched 2026-09-07. All evidence below is from official vendor web surfaces (product/marketing pages — Tier 2). No vendor help centers / user manuals were reachable in this pass; see Uncertainties.

- Gradyent — homepage https://www.gradyent.ai/ and Digital Twin page https://www.gradyent.ai/digital-twin
- Danfoss — Leanheat® Building https://www.danfoss.com/en/products/dhs/software-solutions/danfoss-leanheat-software-suite-services/leanheat-building/ ; Leanheat® Production https://www.danfoss.com/en/products/dhs/software-solutions/danfoss-leanheat-software-suite-services/leanheat-production/ ; Leanheat® Network and Leanheat® Monitor described on the Building page's "Related Solutions" section
- Energy Opticon — https://www.energyopticon.com/ (Swedish-language site; company + Energy Optima 3 product description)
- EMD International — energyPRO District Heating use case https://www.emd-international.com/district-heating-in-energypro and company site https://www.emd-international.com/
- (Failed) Schneider Electric TERMIS product page — HTTP 403

**Source-access limitation**: only vendor product/marketing pages were reachable; no operational user guides, help centers, or manuals. All workflow claims below are calibrated to what those pages state. Vendor-quoted numbers (savings percentages, forecast horizons, accuracy) are recorded as vendor claims and are deliberately **not** promoted into the canonical document.

---

## Product A — Gradyent Digital Twin Platform

### Key observations (evidence layer A per item)

- Positioning: "Upgrade your Grid with our real-time Digital Twin Platform" — for "heating, cooling, steam or CO₂ grids" (scope beyond heating).
- "Our real-time Digital Twin Platform lets you optimise your grid from production to network and end users in real-time and run simulations of future situations." → the managed span is explicitly production + network + end users.
- Digital twin page: "we create a digital copy of your complete grid that runs in real-time, combining geographical, weather and sensor data with physics-based models and AI. It provides insights for your entire network — even for places where you don't have data or smart meters."
- Two operating modes stated: optimise the grid, and run simulations of future situations (planning).
- Purpose named: save operating costs, reduce CO₂, unlock flexibility, "smarter business decisions"; also decarbonise and *grow* the grid (connection growth).
- Implied data inputs: geographical (GIS) data, weather, sensor data; physics-based models + AI.

---

## Product B — Danfoss Leanheat® Software Suite

### Key observations (evidence layer A per item)

Suite of four named modules under "Leanheat® Software Suite & Services" in Danfoss's "Climate Solutions for heating / Software solutions" line ("District energy" is a named Danfoss industry segment).

**Leanheat® Building** — AI-powered optimization of buildings connected to district heating:
- "AI, powered by over a decade of real-time data … continuously learns and adapts to each building's unique behavior. It integrates weather forecasts, heating system data, energy tariffs, and other signals to optimize heating."
- "With real-time control and minute-level precision, the system forecasts the optimal heating plan for 48 hours, updating hourly" (vendor claim).
- Solution includes: heating optimization, peak load optimization, tariff optimization, return temperature optimization, indoor climate monitoring, demand side management.
- Two audiences: building owners ("Intelligent heating optimization for building owners") **and** energy suppliers ("Demand side management for energy suppliers… reduce peak loads… balancing supply and demand… optimize your existing infrastructure to reduce the need for costly network and production investments… using buildings as virtual heat storages").

**Leanheat® Production** — "an advanced software for forecasting, planning, and optimizing district energy production and distribution"; explicitly called "a world-class **district energy management**, optimization, and planning tool" (direct vendor usage of the leaf's term — strong naming evidence).
- Modular: modules for **load forecasting** (Leanheat® HEATFOR™ — "forecasting of heat demand in district heating systems… self-learning and self-calibrating… based on machine learning, weather forecasts, historical demand, and online measurements"; assesses heat consumption six days ahead — vendor claim), **temperature optimization** (Leanheat® HEATTO™ — "uses heat demand forecasts and online measurements from the heating network to control the supply temperature, such that heat losses, heat costs and CO2 emissions are reduced while security of supply is increased"), and **production optimization** ("choosing the right mix of sources" based on price and availability).
- Also Leanheat® METFOR™ (locally optimized weather forecasts) and Leanheat® COOLFOR™ ("cooling demand forecasting for **district cooling** systems").
- "the load forecast working as the indispensable cornerstone" → forecast is the foundation of the whole chain.

**Leanheat® Network** — "a thermo-hydraulic modeling tool, developed specifically for use in district energy systems to support the planning, design, and operational processes."

**Leanheat® Monitor** — "a reliable connected solution for the efficient and cost-effective management of your district energy system. Tailor-made for district energy applications, the open software is easily integrated."

---

## Product C — Energy Optima 3 (Energy Opticon AB)

### Key observations (evidence layer A per item)

- Positioning: "en kraftfull och välbeprövad programvara för ekonomisk totaloptimering av integrerade energisystem och elhandel, med noggranna last- och prisprognoser" — a decision-support tool for **economic total optimization of integrated energy systems and electricity trading** with load and price forecasting. For "energibolag och industrier" (energy companies and industry).
- Coverage statement: "från enheterna i produktionsanläggningen och anslutna industrier och förnybara energikällor, till fjärrvärmenätet, energilagring och konsumentsidan" — from production units, connected industry and renewables, to the district heating network, energy storage, and the consumer side.
- Documented workflow (Steg 1–6): **1 Modeling** — "Enkel och intuitiv konfiguration av ditt energisystem i Topology Editor (”Digital Twin”)… teknisk och ekonomisk data, och sömlös integrering av realtidsmätningar från SCADA-system samt last- och prisprognoser"; **2 Optimization** — "Ekonomiskt och miljömässigt optimerade produktionsplaner (kort- och långsiktiga)"; **3 Visualization** — "Smart Data View… skapa intuitiva instrumentpaneler för personalen i kontrollrummet" (control-room dashboards); **4 Electricity trading** — integration with trading partners; day-ahead, block bids, intraday, ancillary services, 15-minute steps; **5 Reporting / follow-up** — BI integrations (Microsoft SSIS/SSRS), APIs; **6 Special modeling / long-term simulation** — investment calculations, payback, green-transition planning.
- Feature list includes: mätvärden (measurements), prognoser (forecasts), kort- och långtids produktions­optimering (short- and long-term production optimization), stöd för elhandel (trading support), **Smart Optima Heat Network (SOHN)** — "Optimering av framtemperaturen i fjärrvärmenätet… sänka framtemperaturen, lagra värme i nätet, eller höja framtemperaturen tillfälligt innan lasttoppen kommer, för att undvika start av spetslastpannor" (optimize the network forward temperature: lower it, store heat in the network, or raise it temporarily ahead of a load peak to avoid starting peak-load boilers), unit-size optimization (CAPEX), maintenance optimization, battery storage / hydrogen / hydro optimization, **platform for consumer flexibility** ("totaloptimering med tillgänglig flexibilitet… på byggnadssidan… aktiveras vid bekräftelse").
- Users named in testimonials: "Produktionsplanerare" (production planners), "Driftansvariga" (operations managers); dashboards "för personalen i kontrollrummet" (control-room personnel).
- Deployment: on-premise servers or vendor-run private cloud.
- Since 1992; over 50 energy companies and industries in the Nordics, Baltics and Europe.
- Services arm: Energy Management Services — consultants run studies in the same tool.

---

## Product D — energyPRO (EMD International) — boundary-adjacent sample

### Key observations (evidence layer A per item)

- Use case page: "Design efficient and economically viable district heating systems" — investment analysis (evaluate and plan investments in heat production units) + scenario analysis (operation robustness).
- Named priorities of DH operators (vendor's framing of customer problems): minimising system imbalances, reducing costs with smart heat delivery, using the most cost-effective production units, meeting market and contract obligations, clear transparent tariffs and billing, future-proof investment.
- Modelled components: heat demand distribution (degree-dependent vs degree-independent load, from measured temperature), heat storage capacity (from measured forward/return temperatures), heat-producing units with technical power curves and COP, investment scenarios with automated capacity sizing.
- Modules: DESIGN (component structure), COMPARE (alternative strategies), INTERFACE (massive scenario running), OPTIMIZE (investment sizing), ACCOUNT/FINANCE (feasibility, multi-year).
- "Optimal production plan — generate an optimal production plan that dispatches units based on cost" — the same planning abstraction as operational tools, used here offline.
- Integrates with Excel/Python; downloadable desktop product with trial.

**Classification decision**: energyPRO shares the network-model + unit-economics abstractions but has **no live-measurement/operations closure** — it is an offline modeling/feasibility tool. It is therefore recorded as **adjacent to the Type** (planning/design pole), not a defining member. Its DH-specific feature set (forward/return temperatures, heat storage, DH demand profiles) corroborates the domain's object vocabulary.

---

## Cross-product Comparison

| Dimension | Gradyent | Leanheat Suite | Energy Optima 3 | energyPRO |
|---|---|---|---|---|
| Managed scope | production + network + end users, real-time | production + network + monitor + buildings | production units + DH network + storage + consumer side + power markets | production units + storage + demand profile (offline) |
| System model of record | real-time digital twin (physics + AI + GIS + sensors) | thermo-hydraulic network model (Network module) | Topology Editor "Digital Twin" (technical + economic data) | component-based system model |
| Demand forecast | yes (with AI, incl. un-metered points) | HEATFOR™ / COOLFOR™ (ML, self-calibrating, multi-day) | load + price forecasts | demand distribution from measured temperature |
| Production decisions | "optimise your grid… production to end users" | production optimization module ("right mix of sources" by price/availability) | optimized production plans short- and long-term | optimal production plan (cost dispatch) |
| Supply temperature optimization | yes (network optimization) | HEATTO™ (controls supply temperature; heat loss vs security of supply) | SOHN (forward temperature, heat storage in network, peak avoidance) | n/a (uses forward/return temps for storage sizing) |
| Live measurements | yes (real-time; sensor data; even where no smart meters) | online measurements feed HeatTO; Monitor module | real-time measurements from SCADA integrated | no (offline) |
| Thermal storage | flexibility named | buildings as "virtual heat storages" | network as heat store; energy storage in model | heat storage in model |
| Demand side / buildings | "end users" in optimization span | full module (Leanheat Building; demand side management; indoor climate monitoring) | consumer flexibility platform (activation on confirmation) | n/a |
| Power-market coupling | not stated | tariff optimization (signals) | full trading support (day-ahead/intraday/ancillary, 15-min) | market prices as inputs; FINANCE multi-year |
| Cooling | yes (cooling grids) | COOLFOR™ (district cooling forecasting) | not stated (DH-centric; hydro/battery/hydrogen as separate systems) | not stated on DH page |
| Users | grid operators (unnamed roles) | building owners + energy suppliers (demand side) | production planners, operations managers, control-room staff | engineers/consultants (feasibility) |
| Deployment | SaaS cloud (implied) | cloud suite (GDPR compliance claimed) | on-premise or private cloud | desktop (trial download) |
| Closure | live operation + simulation | live monitoring + control + forecast/plan | plan → trade → follow-up loop | offline study |

### What repeats across products (evidence layer B)

1. A **model of the whole system** — production units + distribution network + (most) consumption side — as the basis of everything (4/4).
2. **Demand forecast over time** as an input layer (4/4, in different depths).
3. **Optimized production/distribution decisions** — which unit runs when, how much, and for heat networks at what supply temperature (4/4 as decisions; 3/4 as operational acts).
4. **Integration of live measurements** (SCADA / sensors / online meters) into the model for supervision and correction (3/4 — all except offline energyPRO).
5. **Supply temperature as a controllable operating variable** of the network, traded against heat losses and security of supply (3/4 — signature of the thermal domain).
6. **Thermal storage as an operating resource** — tanks, the network itself, buildings (4/4 in some form).
7. **Peak-load management** — avoiding peak-load boilers / capacity investments (3/4).
8. **Economic optimization posture** — plans evaluated in money and CO₂, not just physics (4/4).
9. Demand-side/consumer flexibility as a managed resource (3/4).
10. Power-market coupling where production includes CHP/electric assets (1 full, 1 partial, 1 via inputs — market-dependent, layer for L2).

---

## Canonical Model

### L0 — Defining Invariant (minimal)

A District Energy Management application is **operator-side software for a shared thermal energy network** that holds three structures jointly:

1. **The whole-system model of record** — a persistent representation of the district energy system as one connected system: production units, the distribution network, and the delivery/consumption points. (Remove → generic dashboards/BI or a bare SCADA.)
2. **Demand–supply coordination over time** — demand forecasts turned into production and distribution decisions: which units to run and when, how much to produce, and (for heat networks) at what supply temperature. (Remove → historian or forecasting-only tool.)
3. **Integration of live measurements for supervision of the running system** — observed plant/network data folded back into the model so operators can monitor and steer. (Remove → offline planning/design tool, i.e., the energyPRO pole.)

Jointly-held is load-bearing: 1+2 without 3 = offline design/optimization modeling tool; 1+3 without 2 = monitoring suite; 2+3 without 1 = spreadsheet-era dispatch spreadsheets, not a network-management Type.

**Thermal carrier is part of the Type's identity** (the network distributes heat or cold — steam networks included per one sample): the defining physics (heat losses, temperatures, thermal inertia) is what separates this Type from electric EMS/DMS. This is a property of the network being managed, not a feature.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Supply-temperature optimization (heat-loss vs security-of-supply trade)
- Thermal storage usage: storage tanks, network-as-storage, buildings-as-storage
- Peak-load management (peak-load boilers, capacity investment avoidance)
- Delivery-point / substation / building-level monitoring and optimization (return temperature, indoor climate)
- Production-economics follow-up (plan vs actual, BI/reporting integration)
- Weather-forecast integration (incl. locally calibrated forecasts)
- Scenario simulation on the system model ("simulations of future situations")
- Consumer/demand-side flexibility activation
- Control-room dashboards / plan visualization
- District cooling as a second carrier in the same system

### L2 — Variant / Optional Structure

- Power-market coupling (trading interfaces, multi-market bidding in 15-min granularity) — depends on whether the operator owns electricity-producing assets (CHP) and on market structure
- Closed-loop control of supply temperature vs advisory plans (varies by product and by operator's willingness to delegate)
- Scope extension beyond heat/cool: steam grids, CO₂ grids (one sample)
- Offline design/feasibility mode as a separate product (adjacent pole — energyPRO; investment sizing, scenario robustness)
- Deployment: on-premise vs private cloud vs SaaS
- Services arm (vendor consultants running studies in the tool)
- Maintenance optimization, unit-size/CAPEX optimization (one-two samples each)

### L3 — Vendor-specific (research notes only)

- Leanheat's branded module names (HEATFOR™, HEATTO™, METFOR™, COOLFOR™); vendor metrics (">95% forecast accuracy", "48h plan updated hourly", "6 days ahead", "5–10% heat-loss reduction", "1–3% fuel savings", "peak-load reduction", payback claims, "6,000 buildings" data heritage).
- Energy Optima 3's named modules (Smart Data View, SOHN, Topology Editor) and BI integrations (Microsoft SSIS/SSRS).
- Gradyent's anonymized customer screenshots (Uniper Leiden) and "grow your grid" growth positioning.
- energyPRO's module names (DESIGN/COMPARE/INTERFACE/OPTIMIZE/ACCOUNT/FINANCE) and Danish Energy Agency Technology Catalogue integration.

---

## Vendor-specific Findings

(As L3 above; none promoted to canonical.)

- **Dual-audience demand side**: Leanheat Building is sold both to building owners (comfort + cost) and to energy suppliers (peak-shaving, infrastructure deferral) — the same operational capability appears under two commercial frames. Relevant to the Building Energy Management boundary.
- **Direct vendor usage of the leaf's term**: Danfoss calls Leanheat Production "a district energy management, optimization, and planning tool" — the directory leaf's name is real market vocabulary.
- **Opticon's economics-first philosophy**: "ekonomisk totaloptimering" — everything is a cost/CO₂ optimization over an integrated energy system; the heat network is one storage/loss element among many.
- **Gradyent's twin-first philosophy**: physics-based digital twin even for un-metered network segments; operations and growth planning on the same model.

---

## Boundary Findings

| Neighboring Type | Relationship | Distinction (remove-what-to-become test) |
|---|---|---|
| Energy Management System / EMS | adjacent (electric) | EMS supervises electrical generation/transmission (frequency, interchange, AGC, state estimation). Strip the thermal carrier (heat losses, supply temperature, thermal storage) → it becomes electric EMS. District energy management is bound to thermal networks. |
| Distribution Management System / DMS, ADMS | adjacent (electric) | DMS/ADMS operate electrical distribution (switching, outages, restoration). Different carrier, different operational acts (no temperature/heat-loss semantics). |
| SCADA / Industrial Historian | complementary | SCADA is the telemetry/control substrate. District energy management **consumes** SCADA measurements ("sömlös integrering av realtidsmätningar från SCADA-system") and adds the model + forecast + planning/optimization layer. Remove the SCADA link and it degrades; remove model+forecast and it collapses into SCADA. |
| Energy Forecasting Platform | overlapping capability | Forecasting exists in all four samples but as a *module* ("indispensable cornerstone"). The Type's defining closure is forecast → production/distribution decision; a forecast product without decisions is the neighbor Type. |
| Demand Response Platform / VPP Platform | overlapping capability | Consumer flexibility appears (Energy Optima platform; Leanheat demand-side management) but inside supply coordination. DR/VPP Types are market/aggregation-centric on the *electric* side; here flexibility is a thermal-network operating resource. |
| Building Energy Management | adjacent, different operator | BMS/BEMS manages one building's systems; here the operator manages the *network* of many buildings. Same product line can serve both audiences (Leanheat Building dual positioning) — the boundary is who operates: network operator vs building owner. |
| Customer Energy Management | adjacent, opposite side | Customer Energy Management serves the energy customer acting on their own premises' energy; District Energy Management serves the network operator acting on the shared system. The substation/building data flows across this seam. |
| Utility Billing Platform | adjacent | Delivery-point consumption is measured here; invoicing/customers/money is the billing Type. energyPRO lists "transparent tariffs and billing" as an operator concern — billing itself is not operated in the sampled products. |
| Water Utility Management | structural analogy only | Same production→network→consumer skeleton, different carrier physics (pressure/quality vs temperature/heat loss). No product-level confusion observed. |
| Energy system design/modeling tools (energyPRO pole) | boundary-adjacent | Shares model-of-record + unit economics; lacks live-measurement operations closure. Recorded as adjacent pole, not inside L0. |

---

## Historical / Market-Sample Check (§24-style)

- Would a **1990s Nordic district-heating utility toolset** (SCADA + spreadsheet production planning + a network register) fit? The L0 elements existed as *separated artifacts* (SCADA = measurements; network drawing register = model; spreadsheet = demand–supply coordination). An integrated Type product merges them — the definition describes the integrated form. A pure network GIS register (model without coordination or live supervision) does **not** fit — and is arguably a network-information-system capability, not this Type. Verdict: L0 survives the check; the Type is defined by the joined closure, which is what modern products sell and what utilities historically assembled from parts.
- Regional skew acknowledged: all four samples are European (NL/DK/SE), where district heating is strongest. The definition does not depend on European market structure (trading, tariffs are L2); heating-vs-cooling balance varies by region (cooling stronger in dense warm climates) and remains inside the Type via the thermal-carrier abstraction.

---

## Uncertainties

1. **No operational documentation reached** — vendor product/marketing pages only. Workflow granularity (who confirms plans, how setpoints reach SCADA, alarm handling, user management) is inferred from product-page statements and marked accordingly; no precise operational rules are asserted in the final document.
2. **TERMIS unreachable** (403) — the classic network-simulation-and-operations product is unresearched; the network-modeling pole rests on three other products.
3. **Customer/billing-side depth unverified** — whether district-energy suites typically bundle billing/consumer CRM was not observable; treated as adjacent Type (Utility Billing Platform) with low confidence on the packaging question.
4. **Non-European market shape unknown** — no sample from e.g. China (large DH market) or North America; regional variants (e.g., steam-dominated systems, regulatory heat-network regimes like UK market supervision) not directly evidenced.
5. **NODA's history** — the Icelandic district-heating optimizer of that name has pivoted/renamed to building operations; earlier-generation district-heating products of that lineage were not verifiable in this pass.

---

## Final Synthesis

District Energy Management is the **network-operator-side operational application Type for shared thermal energy networks** (district heating / district cooling; steam grids included in one sample). Its defining core is a triple structure held jointly: (1) a whole-system model of record spanning production units, distribution network, and delivery/consumption points; (2) demand–supply coordination that turns demand forecasts into production and distribution decisions — unit dispatch, energy quantities, and the network's supply temperature; (3) integration of live plant/network measurements so the running system can be supervised and steered. Around that core, mature products add supply-temperature optimization, thermal storage exploitation (tanks, network, buildings), peak-load management, substation/building-level monitoring, production-economics follow-up, scenario simulation, and consumer flexibility; market coupling (CHP operators trading power) and closed-loop control are variants. The Type is cleanly separated from electric EMS/DMS by carrier physics, from SCADA by the model+forecast+decision layer, from forecasting by the decision closure, and from building/customer-side Types by the operator's seat. Offline design/feasibility modeling tools (energyPRO pole) share the abstractions but lack the live-operations closure and are recorded as adjacent.
