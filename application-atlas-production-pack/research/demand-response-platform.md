# Research Notes — Demand Response Platform

## Research Goal

Understand what "Demand Response Platform" software actually is as an Application Type: who operates it, what objects exist inside it, what lifecycle it drives (program → enrollment → event → response → measurement → settlement?), and where its boundary lies against neighboring Types — especially Virtual Power Plant Platform and DERMS (§19, unprocessed), Energy Management System / ADMS / Grid Operations (§19, unprocessed), Energy Trading (§19, unprocessed), Advanced Metering Infrastructure (§19, processed), Customer Energy Management (§19, processed — carries a joint-review flag for this leaf), Building Energy Management (§17, processed — carries a DR boundary note), Utility Billing / CIS (§19, unprocessed), and EV Charging Network Management (§19, unprocessed).

## Initial Boundary (hypothesis before research)

- A DR platform is software that runs demand response programs: the operator side (utility, grid operator, or aggregator/CSP) defines programs, enrolls customer sites/assets, dispatches DR events, measures response against a baseline, and settles compensation.
- Easily confused with: VPP platforms (many sampled products self-label as VPP), DERMS (utility grid-side), EMS/SCADA (grid operations), trading platforms (market bidding), customer energy apps (consumer side), building energy management (facility side).
- Expected core objects: Program, Enrollment/Participant, Event/Dispatch, Baseline/Measurement, Settlement.

## Research Questions

1. What is a DR program as an object? What program types exist (capacity/emergency, economic/energy, ancillary, behavioral)?
2. What is the enrollment record? What is committed (capacity/kW)? What participation states exist?
3. What is a DR event/dispatch? What lifecycle (forecast → call → notify → respond → cancel)?
4. How is response measured (baseline methods, meter vs device data) and settled (payments, penalties, reports)?
5. What control/automation paths exist (open signal standards, device control, manual curtailment)? Is automation definitional?
6. Who operates the platform (utility, aggregator/CSP, API platform, consumer app) and what does each see?
7. What participant-side surfaces exist (C&I portal, consumer app, partner API)?
8. Where are the exact seams vs VPP/DERMS/EMS/Trading/CEM/BEM/AMI/billing?
9. Historical check: do pre-smart-device, manually dispatched curtailment programs satisfy the minimal definition?

## Representative Products

Selected to cover the market's operator poles and customer tiers, with different product philosophies:

| Product | Pole | Customer tier | Why sampled |
|---|---|---|---|
| EnergyHub | Utility-facing "Edge DERMS" running DR/VPP programs for utilities | Utility program administrators | The utility program-operator console pole; BYOT program types across DER classes |
| Leap | API-first grid-services platform for DER/tech brands | DER platform companies (residential + C&I fleets) | Richest public operational documentation; full object model (meter/enrollment/nomination/bid/dispatch/performance/revenue) |
| CPower | C&I demand response / VPP aggregator (CSP) | Commercial & industrial energy users | The curtailment-service-provider pole; program menu; participant portal |
| OhmConnect | Consumer behavioral demand response app | Residential households | The customer-facing behavioral pole; event-notification + rewards model (note: platform closing announced 2026) |
| OpenADR Alliance | Open standard (not a product) for automated DR signaling | Utilities, ISOs, aggregators, control vendors | Defines the signal layer (VTN→VEN) and the manual-vs-automation distinction; FERC definition of DR |

Rejected alternatives: AutoGrid (now Uplight — domain unreachable, 403; recorded as source limitation); EnerNOC/Enel X (corporate changes, thin public operational docs); Itron/L+G DRMS (no public operational documentation found in-sample).

## Sources

Research date: 2026-09-07. All evidence below is marked A = directly observed on an official source, B = cross-product commonality, C = canonical inference.

- OpenADR Alliance — homepage; "What is Demand Response?"; FAQ (VTN/VEN, Auto-DR, FERC definition) — https://www.openadr.org/ , https://www.openadr.org/what-is-demand-response- , https://www.openadr.org/faq
- Leap — product pages (https://www.leap.energy/) and developer documentation: Welcome/Meter Journey (https://developer.leap.energy/docs/home), Dispatch Overview (…/docs/dispatch-automation-v2), Revenue Reporting (…/docs/revenue-settlement-data), Bidding Overview (…/docs/bidding-introduction), Utility Meters vs. Devices (…/docs/utility-meters-vs-devices), Event Performance & Interval Data (…/docs/event-performance-interval-data), API index (…/llms.txt)
- EnergyHub — Platform Overview (https://www.energyhub.com/edge-derms-platform/platform-overview) and Demand Response strategy page (https://www.energyhub.com/edge-derms-platform/vpp-strategies/demand-response); knowledge base link exists (help.energyhub.com) but content not fetched
- CPower — homepage (https://cpowerenergy.com/) and VPP Platform page (https://cpowerenergy.com/virtual-power-plant-platform/); customer portal referenced (portal.cpowercorp.com, not fetched)
- OhmConnect — "What is an OhmHour" (https://www.ohmconnect.com/what-is-an-ohmhour) and "Make Money" (https://www.ohmconnect.com/how-it-works/make-money); platform-closing notice on site

**Source-access limitations (recorded):** Uplight/AutoGrid returned 403 (also recorded by the customer-energy-management pass). OhmConnect's help-center index is JS-rendered and returned no content; article pages reachable via direct links were used instead. No utility-DRMS vendor help center was directly reachable; utility-operator-console semantics therefore rest on EnergyHub product pages (Tier 2) plus the Leap API docs (Tier 1, aggregator-side). Precise market-rule details (baselines formulas, penalty schedules, capacity-test frequencies) were not researched and are deliberately not asserted.

## Product A — OpenADR (standard; evidence layer A)

- FERC definition of Demand Response: "changes in electric usage by demand-side resources from their normal consumption patterns in response to changes in the price of electricity over time, or to incentive payments designed to induce lower electricity use at times of high wholesale market prices or when system reliability is jeopardized." (A)
- Auto-DR: "fully automated signaling from a utility, ISO, RTO or other appropriate entity to provide automated connectivity to customer end-use control systems… Auto-DR does not require full automation on the customer end." Signals "can be manual or automated." (A) — load-bearing for the historical check: automation is NOT definitional.
- Architecture: VTN (Virtual Top Node — typically a server transmitting OpenADR signals: utility/ISO/aggregator side) → VEN (Virtual End Node — client: EMS, thermostat, or other end device). A VTN can itself be a VEN — "a DR aggregation server can act both as a VEN for a utility DR signal, and as a VTN for end devices" (A) — the aggregation-chain pattern is native to the standard.
- Signals cover dynamic price and reliability; 2.0 profiles include reporting (feedback) of past/current/future data (Profile B); security via TLS + certificates. Used across commercial, industrial and residential segments; 3.0 oriented to the DER era (renewables, storage, EV, capacity management communication). (A)
- Members include utilities, software suppliers, DR aggregators, device manufacturers — the ecosystem the platform Type serves. (A)

## Product B — Leap (API platform for DER partners; evidence layer A)

Positioning: software-only platform letting technology brands enroll their customers' DERs into demand response and other grid-services programs and earn revenue; "end-to-end VPP management: from enrolling resources through dispatching and getting paid." (A)

- **Meter journey** (the platform's own phase model): Onboard (add meters for program enrollment) → Manage (sync inventory, manage participation) → Transact (participate in grid events) → Monetize (assess performance and revenue). (A)
- **Meter** = the basic unit of inventory providing grid services; represents the end customer and the assets behind the utility meter. `meter_type`: `utility_meter` (dispatch + measurement + revenue at the home/site) vs `device` (individual battery/EV charger/thermostat) vs rare `submeter`. Meter carries customer, utility, site, device information and a partner reference. (A)
- **Enrollment**: per-meter enrollment status, participation preferences, associated programs, required actions; idle periods (meter temporarily inactive); disenrollment requests ("remove as soon as possible — end of current month or participation period depending on program"); market-participation indication; market registration (can take weeks; refresh endpoint for ineligible meters). (A)
- **Nominations**: kW values "used for program enrollment"; suggested nominations are reviewed/approved/modified by the platform before becoming actual nominations. (A)
- **Bidding** (CAISO-specific in this implementation, platform-managed by default): bids are price ($/kWh) × capacity (kW) supply curves per meter/timeslot; day-ahead and hour-ahead markets with submission deadlines; standing bids generated from partner preferences; only meters with ACTIVE global enrollment can bid. (A) — program/market-specific: optional capability, not definitional.
- **Dispatch**: "signals from the platform about a grid event… requests for a meter or group of meters to curtail (or export in some cases) energy during a defined time period." Dispatch = recipient (meter or market group) + timeslots (start/end, energy_kw target, nomination_kw, cancelled flag, dispatch_event_types [day-ahead / hour-ahead / capacity-test], is_voluntary flag, priority). Delivery via push webhooks or polling. (A)
- **Capacity tests** are real program events affecting settlement (prove capacity to the market); distinct from communication tests and integration tests (partner-initiated, non-settlement). (A)
- **Performance**: per-event, per-interval energy (Wh): `event_energy_wh` (actual metered load during event), `baseline_wh` (expected load), `performance_wh` (the measured reduction); negative performance = event load higher than baseline; dispatch quantities awarded in kW, converted to Wh for performance; gap-filled interval data ("required by regulators"); data-coverage percentage per meter; unresponsive-meter categorization (NEVER_RESPONDS / RARELY_RESPONDS / NORMALLY_RESPONDS / NEW_METER). (A)
- **Revenue/settlement**: monthly revenue reports with preliminary → FINALIZED status and version history; revenue aggregatable by meter, customer, load type, market group, utility, region; missed_revenue vs potential_revenue; used to "automate customer reporting and payments". (A)

## Product C — EnergyHub (utility-facing DRMS/DERMS; evidence layer A on product pages, Tier 2)

Positioning: "Edge DERMS" for utilities to build and run VPPs from customer-owned DERs; "delivering successful load control programs since 2009". (A)

- **Program types** organized by DER class: thermostat programs (load shaping), battery programs, EV programs (managed charging), C&I programs, background aggregation. (A)
- **DR as a VPP strategy**: "forecast and call events to manage peak load." (A)
- **Operator console loop** (directly documented): forecast system-wide load/capacity → configure and schedule events ("group DERs and set event parameters… let the platform do the rest") → near-real-time event monitoring → review outcomes ("participation, net load shed vs. baseline, load shapes, download and share reports") → fine-tune dispatch strategy. (A)
- ML optimization recommends dispatch schedules across devices; dispatch per recommendations or operator specification; near-real-time adjustment via performance dashboards. (A)
- **DER partner ecosystem**: hundreds of device makes/models connected ("BYOT" — bring your own thermostat); partner management as an integrated service. (A)
- **Integrated services**: program design & management ("achieve program cost-effectiveness and event load shed results"), program marketing (increase enrollment/engagement), partner management. (A) — program design/marketing as services around the platform, common in the pole.
- Broader strategies beyond DR: dynamic load shaping, wholesale price optimization, customer rate optimization, distribution load management. (A) — the expansion surface toward DERMS/VPP.

## Product D — CPower (C&I aggregator/CSP; evidence layer A on product pages, Tier 2)

Positioning: VPP platform monetizing customer energy assets through "demand response and energy flexibility programs"; acquired by NRG; serves C&I industries (healthcare, education, industrial, data centers, retail…). (A)

- **Program menu** (as an aggregator's product taxonomy): Capacity ("resources available to be dispatched under peak conditions or generation scarcity"), Energy ("reduce demand or inject energy when prices are high"), Ancillary Services ("paid to be available to help balance the system"), Demand Charge Management ("shifting use away from peak times"). (A)
- Operator-as-service: "CPower manages your market participation, risk and performance so your assets earn"; curtailment plans per customer; performance fine-tuning. (A)
- **Participant portal** (CPower CONNECT): "tools to view, manage and unlock the full value of your energy assets, all in one secure platform… streamline your energy market activity, maximize revenue and savings, ensure performance and compliance, and track every payment." (A)
- VPP definition given by the vendor: network of energy assets (onsite generation, HVAC, lighting, solar, microgrids, storage, industrial operations, EV charging) participating in DR and on-bill programs. (A)

## Product E — OhmConnect (consumer behavioral DR app; evidence layer A; note: platform closing)

Positioning: residential members get paid for saving energy during grid events; connects to utility accounts (PG&E, SCE, SDG&E, Con Edison) and smart-home devices. Announced closing after ~10 years (2026). (A)

- **Event**: OhmHour ("energy saving events, usually an hour… OhmConnect has committed to the grid that our members will save energy") — called when the grid predicts an energy surge in the next 24 hours; AutoOhm — real-time events with as little as ~15 minutes' warning, device-automated, flat reward per connected device. (A)
- **Notification → response → measurement → reward**: notification via SMS or email; household reduces usage (manually or via smart thermostat/plugs automated power-down); "We measure how much energy you save and sell it back to the grid, passing the profit on to you." (A)
- **Baseline-as-forecast**: rewards for using less energy than you were predicted to use; "Potential Watts… calculated using your historical smart meter data" (the expected/baseline construct in consumer vocabulary). (A)
- **Rewards**: points ("Watts") redeemable as cash, gift cards, prize entries, donations; gamification (prizes, wheels); device-connected members earn more. (A)
- The aggregator position is explicit: the platform aggregates household reductions and sells them into the grid as a resource. (A)

## Cross-product Comparison

| Structure | OpenADR (std) | Leap | EnergyHub | CPower | OhmConnect | Layer |
|---|---|---|---|---|---|---|
| Operator-defined program with compensation | price/reliability signal programs; CPP; incentives | programs a meter enrolls into; per-program rules | utility DR programs by DER class | capacity/energy/ancillary/demand-charge menu | utility-connected savings events | B |
| Enrollment of identified participant/asset with commitment | VEN registration; aggregation chains (VTN-as-VEN) | meter enrollment, nomination kW, idle/disenroll, market registration | utility enrolls customer devices via partner ecosystem | customer sites/projects under managed participation | household + utility account + devices | B |
| Called event in a defined time window with a target | dispatch signal VTN→VEN | dispatch = recipient + timeslots + energy_kw + cancelled flag + event types | "call events": configure, group, schedule; parameters | dispatch under peak/scarcity conditions | OhmHour/AutoOhm notification | B |
| Response: manual or automated | "can be manual or automated"; Auto-DR needs no full customer automation | webhook/polling to partner control systems; is_voluntary flag | device control via platform (thermostats/batteries/EV) or C&I response | curtailment plans, controls in place (customer quote) | manual reduction OR smart-plug/thermostat automation | B |
| Measurement vs expected/baseline | reporting profiles (feedback data) | baseline_wh vs event_energy_wh vs performance_wh per interval | "net load shed vs baseline" reporting; participation | performance and compliance tracking | predicted (Potential Watts) vs actual usage | B |
| Compensation/settlement records | (out of scope for signal standard) | monthly revenue reports preliminary→FINALIZED, versions, by meter/customer/market; missed revenue | program cost-effectiveness/results reporting | "track every payment with confidence" | Watts → cash/gift cards/prizes | B |
| Forecasting before events | (n/a) | day-ahead/hour-ahead market cycles | forecast system load/capacity to plan events | (managed by CPower) | surge prediction (day-ahead vs real-time) | B |
| Market bidding (price×quantity curves) | (n/a) | CAISO bids, day-ahead/hour-ahead, standing bids | wholesale price optimization as a strategy | "manages your market participation" | aggregator sells reductions (transparent to user) | A (Leap) / B (direction) |
| Open signal protocol | the standard itself | (proprietary API) | (partner ecosystem integrations) | (not documented publicly) | (proprietary notifications) | A (std only) — optional capability |
| Consumer rewards/gamification | (n/a) | (partner-owned customer experience) | (utility-owned) | (not consumer) | Watts, prizes, wheels | A (single product) |
| Beyond-DR expansion (load shaping, distribution services, rate optimization) | 3.0 DER-era signals (price, GHG, capacity mgmt) | "other grid services programs" | dynamic load shaping, distribution load management, rate optimization | demand charge management; on-bill programs | (n/a) | B |

Reading: the five structures that repeat across every pole (program / enrollment / event / response / measurement→compensation) form the Type's spine. Bidding, open-protocol support, consumer rewards, and beyond-DR strategies are real but not universal — they sit above the spine.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

The smallest structure without which the software stops being a Demand Response Platform:

1. **The DR program** — an operator-defined offer of compensated load flexibility: participants enroll under stated conditions and qualify for compensation for responding. Remove → generic notification/alert system or energy-monitoring tool.
2. **The enrolled participant/asset** — an identified site, meter, or device held under an enrollment carrying its flexibility commitment (nominated/committed capacity) and participation state. Remove → anonymous broadcast alerts.
3. **The DR event (dispatch)** — a called, dated time window in which the operator requests load reduction (or export) from enrolled participants, delivered as a notification/signal with an explicit target. Remove → pricing/tariff tools or pure telemetry.
4. **Measured performance against a baseline, converted to compensation** — the participant's metered (or device-measured) load during the event is compared with an expected/baseline value, recorded as performance, and turned into payment/incentive/reward records. Remove → home automation or alerting with no resource semantics.

All four are cross-product (layer B); the baseline→performance→settlement leg is directly observed in three different measurement regimes (interval-meter baseline in Leap; shed-vs-baseline reporting in EnergyHub; forecast-vs-actual household measurement in OhmConnect).

### L1 — Common Mature Structure (layer B; common but not definitional)

- Forecasting machinery before events (system load/capacity forecasts; day-ahead vs real-time event classes)
- Event lifecycle states including cancellation; capacity/performance tests as settlement-affecting events
- Enrollment lifecycle management: participation periods/seasons, idle/active/disenrolled states, eligibility and (where applicable) market registration
- Portfolio views: participation rates, per-asset performance, unresponsive/underperforming asset identification, missed-revenue analysis
- Multi-program participation and program stacking per asset
- Notification fan-out to participants (SMS/email/app/push/API webhook)
- Device/DER integration layer connecting enrolled assets (thermostats, batteries, EVs, C&I control systems), often via a partner ecosystem
- Reporting/export for program oversight (program cost-effectiveness, event results, settlement reports)

### L2 — Variant / Optional Structure (layer A or B, segmented)

- Wholesale-market posture: price×quantity bid curves, day-ahead/hour-ahead market cycles, standing bids, platform-managed bidding (observed as a full implementation in one sample; present as strategy positioning in another)
- Open signaling standards (OpenADR VTN/VEN) vs proprietary APIs vs consumer push channels
- Measurement point: utility-meter interval data vs individual-device data vs submeter; partner-uploaded interval data vs utility-fed data; gap-filling and data-coverage policies
- Consumer rewards shape: points/cash/gift cards/prize gamification (consumer pole) vs incentive payments on bills vs direct market revenue sharing (C&I/API poles)
- Beyond-DR expansion: dynamic load shaping, distribution-asset management, customer-rate optimization, demand-charge management — the drift surface toward VPP/DERMS
- Automation depth: full device automation vs human-in-the-loop curtailment vs pure behavioral response
- Aggregation chains: utility→aggregator→devices (a platform being both client of an upstream signal and server to downstream devices)

### L3 — Vendor-specific Detail (research notes only)

- Leap: `meter_id`/`meter_type` model; nomination suggestion→review workflow; specific event-type arrays (`day-ahead`, `capacity-test`); NEVER/RARELY/NORMALLY_RESPONDS taxonomy; preliminary→FINALIZED report versions; 31-day query and 1M-data-point API limits; CAISO bid price bounds and deadline mechanics; gap-fill "required by regulators" phrasing.
- EnergyHub: "Edge DERMS" branding; background aggregation; integrated services (program marketing, partner management).
- CPower: CPower CONNECT portal; "CPowered" solutions taxonomy; NRG acquisition framing.
- OhmConnect: OhmHour/AutoOhm naming; Watts/Potential Watts vocabulary; prize/wheel gamification; platform-closing notice.
- OpenADR: VTN/VEN/EcoPort terms; profile A/B; 2.0 vs 3.0 certification.

## Vendor-specific Findings

- Self-labeling drift: sampled products variously call themselves VPP platform (Leap, CPower), Edge DERMS (EnergyHub), or consumer energy-saving app (OhmConnect) while all performing DR-program machinery. The DR spine is stable beneath unstable labels — a market-naming issue, not a Type-boundary issue (recorded for Boundary Issues).
- Bidding-as-product: only Leap documents market bidding as a first-class API; EnergyHub frames wholesale response as one strategy; CPower absorbs it into managed services. Treat bidding as optional/market-specific.
- Consumer rewards gamification exists only in the consumer pole; incentive delivery differs fundamentally across poles (bill incentives, revenue share, points).

## Rejected Findings

- "DR = automated device control" — REJECTED by the standard itself (signals can be manual or automated; Auto-DR does not require full customer-side automation) and by the behavioral pole (manual household reduction). Automation is the mature default, not the definition.
- "DR = VPP" — REJECTED as an equation: VPP is the broader aggregation-and-optimization framing; DR's program/event/settlement spine is what the sampled products actually operate. Conflation is a naming drift (see Boundary Findings).
- "DR platforms own the customer's energy-insight relationship" — REJECTED: event prompts and rewards are participant surfaces of DR; the continuous own-usage insight loop belongs to Customer Energy Management (consistent with that pass's recorded flag).
- "Baseline always = historical average formula" — REJECTED as too precise: only the *expected-load* concept is universal (Leap baseline_wh, EnergyHub shed-vs-baseline, OhmConnect forecast/Potential Watts); formulas vary by program/market and were not researched.

## Boundary Findings

1. **vs Virtual Power Plant Platform (§19, unprocessed).** Sharpest seam in this domain, made harder by naming drift: two sampled products self-label as VPP platforms. Discriminator proposed: the VPP Type's center of gravity is continuous multi-value optimization of an aggregated DER fleet (energy markets, capacity, ancillary, distribution services, asset health), while a DR platform's center of gravity is the program/event/settlement machinery for compensated load flexibility. A DR event engine embedded in a VPP is the same machinery; when dispatch becomes continuous optimization against multiple value streams and DER-fleet management becomes the core object, the product has crossed into VPP. **Recommend joint review when virtual-power-plant-platform is processed** (recorded in STATUS).
2. **vs DERMS (§19, unprocessed).** DERMS is utility-side DER integration for grid operations (visibility, forecasting, control of distribution-edge resources). A DR platform administers programs and events as a commercial resource. EnergyHub markets itself as "Edge DERMS" while its documented loop is exactly the DR program loop — evidence that the boundary is posture (grid-operations integration vs program administration), not vendor vocabulary.
3. **vs Energy Management System / EMS / ADMS / Grid Operations (§19).** EMS/ADMS operate the grid (SCADA, state estimation, outage); a DR platform calls flexibility from customers as a resource. OpenADR's positioning ("utilities and aggregators… send signals to customers") marks the seam: DR sits between market/program operators and customer assets.
4. **vs Energy Trading Platform (§19).** Trading platforms are systems of record for market positions; DR platforms may *bid into* markets (Leap's bid API) as a participation step inside the program machinery. Bidding is a capability seam; ownership of trades/portfolios belongs to trading.
5. **vs Customer Energy Management (§19, processed — flag DISCHARGED from this side).** That pass recorded: "the customer-facing participation experience (event prompts, enrollment, behavioral load shifting) sits inside [CEM] as a capability/pole while the program/event machinery belongs to DR." This pass resolves: a pure consumer-DR app (events + response + rewards, no continuous usage-insight loop) is the *participant surface* of this Type — the household participates in operator-called events for compensation, which is DR semantics. When the product's center of gravity is the household's own continuous usage insight (comparisons, forecasts, tips), it is CEM. Products doing both straddle the seam; the event/compensation machinery belongs to DR.
6. **vs Building Energy Management (§17, processed).** BEM may participate in DR as a variant capability (its own pass recorded this); the DR platform owns program/event machinery and treats the building as an enrolled asset. Removal test: remove program/settlement machinery → BEM/EMS territory.
7. **vs AMI / MDMS (§19, processed).** AMI collects the interval data; DR consumes it for baselines and performance. Measurement data path does not change the DR Type (utility-fed vs device-fed vs partner-uploaded all observed).
8. **vs Utility Billing / CIS (§19, unprocessed).** DR settlement is program compensation (revenue reports, incentive payments), distinct from the utility bill's money of record. CPower's "on-bill programs" phrasing marks the seam where compensation delivery may ride billing rails without becoming billing.
9. **vs EV Charging Network Management / Battery Storage Management (§19, unprocessed).** Those Types own the asset operations (chargers, storage fleets); DR enrolls their flexibility as resources. Device-level measurement (Leap `device` meter type) keeps the seam clean: the DR platform measures and dispatches, it does not operate the charger network or the battery plant.

### "去掉什么就变成另一个 Type" 判据 (removal tests)

- Remove the program/compensation structure → notification/alerting or energy monitoring.
- Remove events (continuous optimization instead of called events) → VPP/DERMS optimization layer.
- Remove the enrolled-asset population → broadcast messaging.
- Remove baseline/measurement/settlement → demand-side marketing or home automation.
- Remove the operator side (customer self-insight loop only) → Customer Energy Management.

## Historical / Market-Sample Check (§24)

- Demand response predates smart devices and AMI: utilities and ISOs have run curtailment programs dispatched by phone/fax/pager with manual C&I load shed and meter-based M&V for decades. The sampled standard itself documents that signals "can be manual or automated." → Automated device control, OpenADR support, and smart-thermostat fleets are NOT definitional; the manual-notification program passes the historical check.
- Consumer behavioral DR (OhmConnect-class) and C&I aggregator DR (CPower-class) and utility console DR (EnergyHub-class) and API DR (Leap-class) all satisfy the L0 set without sharing any specific channel, protocol, or reward shape. → Channel/protocol/reward specifics stay out of the definition.
- Pre-OpenADR proprietary Auto-DR (Berkeley Lab research era) satisfied enrollment+event+measurement with bespoke integrations → open standards are optional maturity, not definition.

## Uncertainties

- Utility-DRMS vendor help centers were not directly reachable (Uplight 403; no other DRMS vendor's operational docs fetched) — the utility-operator console description rests on EnergyHub product pages (Tier 2) plus cross-product reasoning; assertion strength for console details kept moderate.
- Penalty/non-compliance mechanics (capacity-test consequences, shortfall penalties) were observed only as hints (capacity tests "used in settlement calculations"; CPower "manages risk") — not asserted in the final document beyond qualified phrasing.
- Regional markets outside North America (Europe flexibility markets, Asia programs) were not directly sampled; the OpenADR 3.0 European initiative suggests structural similarity but no direct evidence — regional claims kept low.
- OhmConnect is closing; its evidence describes the consumer behavioral pole as it existed — the pole itself (behavioral DR) is corroborated by OpenADR's CPP/incentive framing and EnergyHub's thermostat programs, so the Type claim does not rest on the closing product.
- Exact program-taxonomy breadth (emergency DR, capacity DR, economic DR, ancillary) is industry-common but directly documented only via CPower's menu + FERC/OpenADR definitions; phrase as common industry categories rather than a fixed taxonomy.

## Final Synthesis

A Demand Response Platform is the program-side system of record for compensated load flexibility: software through which an operator (utility, grid operator, aggregator/CSP, or a DER platform company) defines demand response programs, enrolls identified customer sites/assets with committed capacity, calls DR events as dated dispatches with targets, delivers the call to participants as signals or notifications (manual or automated response), measures each participant's event performance against an expected baseline from meter or device data, and converts measured performance into compensation records (payments, incentives, or rewards) with program-level reporting and oversight. Its defining core is exactly four structures — program, enrollment, event dispatch, baseline-to-settlement measurement — realized across four operator poles (utility console, aggregator services, API platform, consumer app) that all share the same spine. Automation depth, bidding, open protocols, reward gamification, and beyond-DR strategies are common or optional maturity above the spine, not definition. The seams: VPP/DERMS optimize fleets continuously (DR calls events for compensated response); EMS/ADMS operate the grid; trading owns market positions; CEM owns the customer's own usage insight; BEM manages buildings; AMI/MDMS own the data collection; billing owns the bill.
