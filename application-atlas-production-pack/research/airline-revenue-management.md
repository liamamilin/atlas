# Research Notes — Airline Revenue Management

Research date: 2026-09-06

## Research Goal

Understand what an Airline Revenue Management (RM) system really is, from real products: what objects exist inside it (forecasts, availability controls, bid prices, booking classes), who operates it (revenue management analysts and pricing teams), how the forecast → optimize → publish loop works and couples to the reservation system that actually sells, and where its boundary lies against the passenger service system (which holds and executes inventory), the airline operations platform (which runs the day), hotel revenue management (the hospitality analog), dynamic pricing (the modern pricing sibling), and generic demand/pricing optimization products.

## Initial Boundary

- Hypothesis going in: this Type is the airline's commercial optimization brain. It does not hold seat inventory and does not sell; it forecasts demand on future flights and decides what the selling systems should offer — which booking classes to open/close, how many seats to protect for later/higher-value demand, how far beyond physical capacity to accept bookings — and hands those controls to the reservation system.
- The sibling research file research/airline-reservation-passenger-service-system.md already established the division from the PSS side: "RM computes inventory levels; the PSS holds and executes them" (Videcom: nightly data export to an external RM provider and import of updated inventory levels; iFly: inventory record "that can be optimized through a revenue management system").
- Adjacent Types flagged from the start: Airline Reservation / PSS (execution side, documented sibling), Airline Operations Platform (operational side, documented sibling), Hotel Revenue Management System (hospitality analog, separate directory leaf), Flight Search / Booking Platform (consumer side), Air Cargo Management (cargo-side RM analog), Demand Planning / Retail Pricing Management (generic analogs in other directory sections), Dynamic Pricing (modern pricing sibling products inside the same vendor families).
- Unknowns going in: exact control vocabulary (bid price vs authorization level vs protection level); whether overbooking is in the defining core or a common mechanism; leg-based vs O&D control as variant or common structure; how the modern "class-free / continuous pricing" wave changes the Type; packaging (standalone RM vs platform module).

## Research Questions

1. What are the core objects — forecast, controls, bid prices, booking classes — and how do they relate?
2. What exactly does the system compute, and what does it hand to the selling system?
3. What is the analyst's role: does the system decide, recommend, or execute?
4. How do leg-based and network (O&D) optimization differ as product strategies?
5. What data flows in (bookings, cancellations, no-shows, competitor fares, market capacity) and out (controls to PSS/availability engines)?
6. Where does overbooking sit in the model?
7. How does the modern dynamic-pricing / class-free wave relate to classic RM — same Type, sibling product, or successor?
8. Where are the boundaries: PSS, ops platform, hotel RM, cargo RM, revenue accounting, generic pricing products?

## Representative Products

Sample selection intent: market representativeness + different product philosophies + different customer tiers. Reachability constrained the final sample (see Sources).

| Product | Vendor | Tier / philosophy | Status |
|---|---|---|---|
| PROS Revenue Management (+ Real-Time Dynamic Pricing, Group Sales Optimizer as sibling products) | PROS | RM pioneer lineage ("40 years of airline industry experience"); enterprise tier; 130+ airline customers claimed; science/AI-led positioning; RM + pricing + group sales as separate product lines | Researched (official product pages, unusually detailed) |
| FLX ONE Revenue Management (+ FLX ONE Dynamic Pricing as sibling product) | Accelya | PSS-agnostic standalone RM inside a modern-retailing platform; 70+ airline customers claimed across FSC/hybrid/LCC/ULCC; modular retailing philosophy | Researched (official product pages + press release citing T2RL market report) |
| Amadeus RM family | Amadeus | Largest enterprise RM installed base (per market reputation) | Unreachable (bot wall; also blocked in both sibling airline researches) |
| Sabre RM (AirVision lineage) | Sabre | Enterprise RM from GDS lineage | Unreachable (bot wall / 404s in sibling researches) |
| Kambr | Kambr | Smaller analytics-led RM vendor | Unreachable (bot wall ×2) |
| SITA RM | SITA | Regional/legacy RM | Unreachable (403) |
| IBS iFly RM | IBS Software | Cloud-native RM from the PSS sibling vendor | Unreachable (404 ×2, 403 on product index) |

## Sources

Fetched 2026-09-06 (all official vendor pages):

- PROS — Revenue Management product page: https://pros.com/products/airline-revenue-management-software/ (fetched 2026-09-06)
- PROS — Real-Time Dynamic Pricing product page: https://pros.com/products/real-time-dynamic-pricing-software/ (fetched 2026-09-06)
- PROS — Group Sales Optimizer product page: https://pros.com/products/airline-group-sales-software/ (fetched 2026-09-06)
- PROS — corporate home (platform/product map): https://www.pros.com/ (fetched 2026-09-06)
- Accelya — FLX ONE Revenue Management product page: https://w3.accelya.com/products/flx-revenue-management/ (fetched 2026-09-06)
- Accelya — FLX ONE Dynamic Pricing product page: https://w3.accelya.com/products/flx-dynamic-pricing/ (fetched 2026-09-06)
- Accelya — press release "Accelya Revenue Management business surpasses 712 million passengers" (citing T2RL, The Market for Airline Revenue Management Systems 2026): https://w3.accelya.com/resources/press-releases/accelya-revenue-management-712-million-passengers/ (fetched 2026-09-06)
- Accelya — corporate home (product map): https://www.accelya.com/ (fetched 2026-09-06)

Sibling research files used as cross-boundary evidence (their own fetched sources are listed there):

- research/airline-reservation-passenger-service-system.md — Videcom nightly RM export/import (B6); iFly inventory-optimized-through-RM (A7/A8); boundary finding on RM vs PSS
- research/airline-operations-platform.md — ops/RM non-overlap (ops research contains no RM concern; boundary finding vs PSS)

Unreachable (1–2 attempts each, then abandoned): amadeus.com (bot wall; consistent with sibling researches), kambr.com (bot wall ×2), sita.co (403), ibsplc.com RM URLs (404 ×2; 403 on /products index), sabre.com (bot wall / 404s per sibling researches), hitit (unreachable per sibling researches).

Sourcing limitation: the enterprise-flagship tier (Amadeus, Sabre) and smaller vendors (Kambr, SITA, IBS RM) could not be observed directly. Claims about the Type rest on two verified products at different tiers/philosophies, plus sibling-research corroboration of the RM↔PSS coupling and an independent market-research reference (T2RL) confirming the category's recognized core. Vendor help centers / user guides were not reachable for any sampled product. All claims below are calibrated accordingly; vendor marketing figures stay in these notes and are not used as structure evidence.

## Product A — PROS Revenue Management (with Real-Time Dynamic Pricing and Group Sales Optimizer as sibling products)

### Key observations (evidence layer A = directly observed on official pages; interpretation marked)

- A1. Definition-by-positioning: "Optimize Revenue with the Right RM System for Your Network. Forecast demand accurately, model elasticity intelligently, and stay ahead of market shifts." RM is framed as network-scoped forecasting + optimization.
- A2. The optimization output named explicitly: "Maximize revenue performance with a proven, 5-step optimization process. PROS RM determines the ideal passenger mix, bid prices, and inventory controls—helping you make every departure as profitable as possible." → the system's product is *decisions about each departure*: passenger mix, bid prices, inventory controls.
- A3. Forecast inputs: "PROS forecasting science helps you drill into bookings, cancellations, and no-shows to reveal emerging trends and support more confident RM decisions." → bookings, cancellations, no-shows are the forecast substrate.
- A4. Forecasting science: "machine learning, Bayesian updating, and multiple demand dimensions to model passenger demand... capturing elasticity across key demand drivers... aggregate booking patterns and demand elasticity across product categories." Also: "Forecast at unmatched granularity across 11 dimensions" (dimension count = vendor claim).
- A5. Availability decision as the core act: "Optimize availability decisions with models that respond to changing demand conditions. Whether your strategy is leg-based or network-based, PROS RM uses elasticity insight and expected demand to determine the right mix of seats to accept now versus protect for later." → accept-now vs protect-for-later is the central trade-off; leg-based vs network-based is an explicit strategy choice.
- A6. Network effects: "PROS RM evaluates how passengers traveling across the network impact demand... The system identifies the best passenger mix for each departure and supports analysts with clear, science-backed recommendations."
- A7. Dynamic programming framing: "Dynamic programming evaluates RM decisions over time by balancing current demand with the expected value of future demand against capacity. By comparing the value of accepting a booking now versus holding inventory for later..." → the perishability trade-off is the mathematical core.
- A8. Fare valuation inside RM: "Fare Valuation: Set more accurate fares and increase revenue by leveraging real-time pricing data."
- A9. Analyst workflow philosophy: "Focus on what's most important with easy-to-understand workflows built on 'manage by exception.' Start analysis at a higher level and then quickly drill down on your markets, so you can easily interpret data and take action." Plus: "surfaces the most relevant insights through intuitive dashboards, streamlining analyst workflows so teams can quickly spot issues, explore more data with less effort, and make faster, more informed decisions."
- A10. Class-free direction: "Elasticity-Driven Forecasting: Progress toward class-free RM... enable analysts to effectively address buy-down." → classic RM is class-based; class-free is the stated destination.
- A11. Segment packaging: "Point-to-Point Airlines: ...leg-based optimization... advanced bid price and AU control" vs "Origin & Destination Airlines: ...network-aware forecasting and optimization to balance demand across itineraries and protect high-value flows... clearer insight into O&D performance." → two product configurations by network shape. ("AU" = authorization-level vocabulary; vendor term.)
- A12. Integration surface: "seamless integrations with Passenger Service Systems (PSS), Competitive data providers, Revenue Accounting providers, ATPCO, Availability engines, and more, ensuring smooth operations and real-time synchronization across applications." Named partner logos: Amadeus, Sabre, ATPCO, OAG. → RM consumes PSS sales data + external market data; publishes to PSS/availability engines; revenue accounting is a data source, not a function of RM.
- A13. Downstream consumers of RM forecasts: "Operational, commercial, and planning teams gain clearer visibility into demand patterns and performance expectations." → forecasts are consumed beyond the RM team.
- A14. Customer-side evidence of RM as an organizational function: Air Canada "Managing Director, Revenue Optimization" (30+ year relationship); flydubai "SVP, Revenue Management"; Saudia/Malaysia/TAP/Lufthansa CCO-level quotes about RM + dynamic pricing strategies.
- A15. Sibling product — Real-Time Dynamic Pricing (RTDP): "Evolve your pricing beyond rigid, class-based fares using real-time demand and availability... supporting your transition toward class-free continuous pricing." "calculating availability in real time, optimizing pricing based on demand, capacity constraints, and your business strategies and rules." "acts as a price recommendation engine." "shields core airline inventory systems from unnecessary load while delivering fast, accurate availability across all sales channels, distribution partners, codeshare and interline networks."
- A16. RTDP three-stage maturity model (vendor's own journey framing): Stage 1 Dynamic Availability ("analysts use real-time demand signals and business strategies to dynamically calculate availability at any moment, resulting in the most relevant filed fare"); Stage 2 Continuous Pricing ("generate price points between filed fares—creating smoother pricing curves"); Stage 3 Request-Specific Pricing ("neural networks to analyze demand signals, itinerary attributes, and market conditions").
- A17. RTDP integrations: "Revenue Management Systems (RMS), Shopping engines, PROS Group Sales Optimizer (GSO), Global Distribution Systems (GDS), Passenger Service Systems (PSS)". FAQ: "PROS RTDP is integrated with PROS Revenue Management to help ensure the seamless execution of your airline's RM strategy." → pricing engine executes the RM strategy; RM and dynamic pricing are distinct product layers.
- A18. RTDP named failure modes: "prevents spillage (underpricing) and spoilage (overpricing)"; "discourage buy-down". Also abuse controls: "married segment control and integrity reporting". Simulation: "Test pricing and availability strategies before deploying them. Simulation tools enable analysts to validate the impact of new rules, configurations, and business strategies."
- A19. RTDP analytics: "BI reports that track look-to-book ratios, availability requests, and sell request volumes across channels."
- A20. Sibling product — Group Sales Optimizer (GSO): "calculates the true marginal revenue of group bookings—the real economic impact of allocating seats to a group instead of individual passengers"; "evaluates real-time demand, remaining capacity, and expected future sales to recommend fares"; "Group Policy Management... aligning RM, sales, and agency partners"; "Group Booking Management: Seamlessly manage group bookings with PSS integration, automated PNR creation and updates". Customer quote from Turkish Airlines "Revenue Management Group Supervisor". → group evaluation is a distinct product line that consumes RM-style economics and writes back into the PSS; it is adjacent to RM, not RM itself.
- A21. Marketing metrics on pages (recorded, not used as structure evidence): 2–3% average revenue uplift; >25% forecasting-accuracy boost; +30% analyst efficiency; 130+ airline customers; 40 years of airline experience; "400 million prices and 1.7 billion forecasts every day"; RTDP "13.7B+ transactions daily", "99.99% uptime", "up to 3.5% direct revenue uplift"; GSO "60% faster time to quote" etc.
- A22. Vendor blog title (corroboration of the class substrate): "the 26 rigid booking classes that have defined airline pricing for decades" (PROS blog listing). → the fixed alphabet of booking classes is presented by the vendor itself as the decades-old pricing substrate.

## Product B — Accelya FLX ONE Revenue Management (with FLX ONE Dynamic Pricing as sibling product)

### Key observations

- B1. Definition-by-positioning: "Next-gen airline revenue management enabling airlines to identify sales opportunities, maximize passenger revenues, closely control pricing, and analyze performance." And: "an advanced RM product designed to help airlines optimize inventory, pricing, and reporting in real time."
- B2. The traditional core acknowledged: "Traditional automated revenue management often fails when historical data is missing or unreliable, limiting airlines' ability to make fast, profitable decisions." → classic RM is historical-data-driven; the vendor differentiates on real-time data.
- B3. Forecasting feature: "Advanced forecasting based on historical trends, behavior, and competition, allowing users to customize and track flight forecasts across inventory strategies." → forecasts are per-flight, user-visible, and user-adjustable; they span "inventory strategies".
- B4. Optimization feature: "Bringing together different optimization models to help airlines maximize revenue. It offers flexibility to choose the right model and adjust settings for the whole system, specific markets, or individual flights." → model choice and configuration authority at system/market/flight granularity.
- B5. Controls feature: "Leverage Controls in Real-time: Respond to market changes with automated inventory control and quick decision-making tools, streamlining flight management with ease." → automated inventory control is the act; "inventory control" is the vendor's own term for the output.
- B6. Decision-support surface: "access to over 60 data points, including fare, bookings, competitor info, and forecasts, enabling rapid scenario analysis and informed decisions across hundreds of flights." (60 = vendor claim.) → scenario analysis across flight portfolios is a first-class surface.
- B7. PSS-agnostic integration posture (FAQ): "FLX ONE Revenue Management has integrations with more than 28 reservation systems." "used by more than 70 airline customers with a full range of business models (full-service carriers, hybrid, LCC and ULCC)." "can take data from many different sources such as market capacity data, ancillary data and competitor fares." → RM is a layer beside/above whatever PSS the airline runs; external market data is a standard input class.
- B8. Sibling product — FLX ONE Dynamic Pricing: "AI & ML driven dynamic pricing that enhances every shopping opportunity"; "adjust fares and ancillaries based on demand, competition, inventory, and customer behavior"; "optimizes shopping by determining the best fares for each flight to maximize the value of every shopping session"; "combining choice modeling with competitive analysis... customer Willingness to Pay (WTP), competitive pricing, and alternative offers"; FAQ inputs: "willingness to pay data, flight performance data, customer information and ancillary business rules"; "Customer Choice Model is an analytical model that identifies the likelihood of each passenger buying a flight among a collection of alternatives." → per-shopping-session pricing optimization is a separate product from RM; both sit in the same retailing platform.
- B9. Platform context: FLX ONE decomposes airline retailing into Offer Management (Select, NDC, Vision, Merchandising, Shop and Price, Revenue Management, Dynamic Pricing, Product Catalog, Stock Keeper, Order Accounting, Schedule Builder, Availability Calculator) + Financial + Cargo. RM is one module of the retailing platform; Stock Keeper and Availability Calculator are separate modules (inventory/availability execution lives outside RM even within the same platform). → strong evidence that "compute the controls" and "hold/execute the inventory" are structurally separate concerns.
- B10. Independent market-category confirmation (press release citing T2RL, The Market for Airline Revenue Management Systems 2026): "revenue management is evolving beyond traditional forecasting and inventory control toward AI-enabled decision support, dynamic pricing, and closer integration with offer creation" (T2RL's framing, quoted in Accelya's PR). Also: "standalone revenue management provider" as a recognized market category; "FLX ONE Revenue Management helps airlines optimize pricing and inventory decisions through advanced forecasting, automation, and data-driven insights. The solution supports low-cost, hybrid, and network carriers." Small-carrier evidence: BermudAir ("a growing airline... lean operation") as new customer choosing RM "without the cost, risk, and disruption of a large-scale technology program."
- B11. Marketing metrics (recorded, not used): 712M passengers carried in 2025 by airlines using the platform; 6.2% YoY growth vs 4.2% market; "up to 20% revenue increase in the first year"; "#1 market-leading enabler... across 70+ airlines"; ancillary attachment "up to 30%" and "$12 incremental revenue per ticket" (platform-wide claims).

## Cross-boundary corroboration (from sibling research files, layer B)

- Videcom VRS (PSS sibling research, B6): "can also be integrated with external Revenue Management system … Data is exported nightly to your chosen provider and receives updates to inventory levels." → the classic coupling is a batch data exchange: sales/booking data out, inventory levels in. RM computes; PSS holds and executes.
- Videcom VRS (B5): ticket time limits exist for "Revenue Integrity … to reduce the number of empty seats left on an aircraft due to late cancellations" — the PSS polices the hold→ticket transition; RM's demand-shaping happens upstream of it.
- iFly RES (PSS sibling research, A7/A8): "integrated tour operator allotment and seat-only flight inventory record that can be optimized through a revenue management system" — same division, native coupling.
- Airline Operations Platform sibling research: contains no RM concern; the ops platform owns flights as operational objects (legs, tails, disruptions), RM owns flights as future revenue objects. The two researches do not collide.
- Air Cargo Management sibling research: cargo suites contain their own RM engines ("dedicated RM engine built specifically for air cargo business") — the RM discipline repeats on the freight side with weight/volume capacity, confirming that "RM" is a reusable optimization discipline whose identity comes from the inventory substrate it optimizes.

## Cross-product Comparison

| Aspect | PROS RM | Accelya FLX ONE RM | Reading |
|---|---|---|---|
| Self-description | "Forecast demand accurately, model elasticity intelligently"; "determines the ideal passenger mix, bid prices, and inventory controls" | "optimize inventory, pricing, and reporting in real time"; "identify sales opportunities, maximize passenger revenues, closely control pricing" | forecast + inventory/pricing control is the shared self-definition |
| Central object | the departure ("make every departure as profitable as possible"; "best passenger mix for each departure") | the flight ("customize and track flight forecasts"; "settings for... individual flights"; "decisions across hundreds of flights") | future flights/departures as the optimization unit |
| Forecast | bookings, cancellations, no-shows; ML/Bayesian; elasticity; 11 dimensions (claim) | historical trends, behavior, competition; user-customizable and trackable | demand forecasting is the shared first layer |
| Optimization output | bid prices + inventory controls; accept-now vs protect-for-later | automated inventory control; model choice per system/market/flight | computed availability controls are the shared output |
| Control mechanism substrate | class-based today, "progress toward class-free RM" | inventory strategies (class ladder implied by market); DP sibling handles per-session pricing | class-ladder control is the traditional substrate; class-free is the modern direction (both vendors) |
| Leg vs network | explicit strategy choice (point-to-point leg-based vs O&D network-aware) | not surfaced on fetched pages | leg-vs-O&D is directly evidenced in one product; treat as common strategy dimension, shape varies |
| Analyst role | manage-by-exception dashboards; drill-down; science-backed recommendations | quick decision-making tools; scenario analysis across hundreds of flights; customize forecasts | human-in-the-loop decision support, not autonomous execution |
| External data | competitive data providers, ATPCO, OAG | market capacity data, ancillary data, competitor fares; 60+ data points (claim) | external market/competitive data is a standard input class |
| PSS coupling | integrations with PSS + availability engines; real-time synchronization | 28+ reservation-system integrations; PSS-agnostic | RM is PSS-adjacent by design; the selling system is always external |
| Pricing sibling | Real-Time Dynamic Pricing (separate product; executes RM strategy) | FLX ONE Dynamic Pricing (separate product; per-session fare/ancillary optimization) | RM vs dynamic pricing is a two-layer pattern in both vendor families |
| Group handling | Group Sales Optimizer (separate product; marginal-revenue group pricing; PSS write-back) | not surfaced on fetched pages | group evaluation is an adjacent product line, evidenced in one family |
| Downstream data | revenue accounting providers as data sources | (platform separates Revenue Accounting as its own product family) | RM is pre-sale optimization; settlement is downstream and separate |
| Packaging | RM product inside a retail/offer platform | RM module inside FLX ONE retailing platform | standalone-product lineage, increasingly platform-modular |
| Segment breadth | point-to-point ↔ O&D configurations; 130+ airlines claimed | FSC/hybrid/LCC/ULCC; small carriers (BermudAir) | all carrier segments; configuration varies by network shape |

### Evidence layer B (cross-product commonality, supports L1)

Present in both sampled products:

- demand forecasting on the airline's future flights as the first layer
- computed inventory/availability controls as the optimization output
- the selling system (PSS / availability engines) as an external execution boundary the controls are published to
- analyst-facing decision surfaces (dashboards, drill-down, scenario analysis) rather than autonomous operation
- external market/competitive data ingestion
- performance monitoring/reporting
- a separate dynamic-pricing product layer executing/extended from RM strategy
- configuration authority for humans at system/market/flight granularity

## Abstraction Hierarchy

### L0 — Defining Invariant

```text
Demand forecast over the airline's future flights
└── capacity-constrained revenue optimization
    └── computed inventory/availability controls (what to accept, protect, and at which price points)
    └── handoff of those controls into the selling pipeline (reservation system / availability engines)
```

Three properties. Remove any one and the product stops being recognizable as this Type:

1. **Demand forecast on future flights** — without it there is no optimization input; the product degenerates into reporting.
2. **Capacity-constrained optimization producing availability/pricing controls** — without computed controls the product is a forecast dashboard, not a revenue management system.
3. **Handoff into the selling pipeline** — the controls must govern what the reservation system actually sells. Without this, the product is demand analytics, not revenue management; the airline's seats would be sold by whatever static limits happen to sit in the PSS.

§24 historical check: the yield-management systems that pioneered this category in the post-deregulation airline industry (forecast demand per flight/booking class → set class availability and overbooking limits → feed the reservation system → monitor) satisfy all three properties without ML, real-time data, continuous pricing, or O&D network optimization. Those are all later additions. The L0 holds for the historical form.

### L1 — Common Mature Structure

Present across the researched sample; expected in the market; not defining:

- **booking-class availability control as the classic mechanism** — the fixed alphabet of booking classes (vendor literature: "26 rigid booking classes... for decades") with availability limits per class; bid prices and authorization/protection levels as the control vocabulary (directly evidenced: PROS "bid prices", "accept now versus protect for later", "AU control")
- **overbooking-relevant forecasting** — forecasts extend to cancellations and no-shows (directly evidenced: PROS), which is the informational basis for accepting bookings beyond physical capacity; exact overbooking mechanics were not observed in sampled documentation
- **leg-based and network (O&D) optimization modes** — explicit strategy choice in one product (PROS); network effects ("passengers traveling across the network") as the optimization concern
- **analyst workbench** — manage-by-exception dashboards, portfolio → market → flight drill-down, forecast review and customization, scenario analysis across flight portfolios
- **configuration authority** — model choice and settings at whole-system, market, and individual-flight granularity (Accelya); science-backed recommendations with human decisions (PROS)
- **external data ingestion** — competitor fares, market capacity data, ancillary data; named data partners (ATPCO fares, OAG schedules) in one product
- **performance monitoring & reporting** — revenue vs forecast, per-flight and portfolio views
- **re-optimization cadence** — periodic re-forecasting with real-time/intra-day responsiveness as the modern posture (both vendors position real-time as their differentiator over "traditional automated revenue management")
- **group request evaluation** — adjacent product line consuming RM economics (marginal revenue of allocating seats to a group vs individuals) with PSS write-back (PROS GSO; one family only → keep as common-adjacent, not universal)
- **PSS-agnostic integration posture** — many-reservation-system integration as a selling point (28+ per Accelya; PSS + availability engines per PROS)

### L2 — Variant / Optional Structure

- **control paradigm**: class-based availability control (traditional) vs class-free / continuous pricing (modern direction; both vendors ship it as a separate pricing layer or roadmap)
- **pricing extension depth**: RM alone vs RM + real-time dynamic pricing + dynamic ancillary pricing (sibling products in both families)
- **optimization scope**: leg-based vs O&D/network; single-departure vs portfolio-level decision support
- **carrier segment**: network carriers (O&D complexity, connections) vs point-to-point/LCC/ULCC (leg-based, price-sensitive) vs hybrid vs small/lean carriers (BermudAir evidence: RM adopted as a lightweight capability without a large technology program)
- **packaging**: standalone best-of-breed RM vs module of a retailing platform (FLX ONE) vs product line inside an offer-optimization platform (PROS)
- **data posture**: historical-bookings-based vs real-time multi-source (60+ data points claim) vs elasticity/WTP models
- **cadence**: nightly batch cycles (classic; corroborated by the Videcom nightly exchange) vs continuous/real-time re-optimization
- **cargo analog**: the same RM discipline exists on the freight side (cargo RM engines) but belongs to Air Cargo Management, not this Type

### L3 — Vendor-specific Detail (research notes only)

- PROS: "5-Step Optimization" process name; "11 dimensions" forecast granularity; "AU control" vocabulary; RTDP three-stage journey naming (Dynamic Availability → Continuous Pricing → Request-Specific Pricing); "married segment control"; GSO "true marginal revenue" framing; metrics (2–3% uplift, >25% forecast accuracy, +30% analyst efficiency, 13.7B+ daily transactions, 99.99% uptime, 3.5% RSP uplift); customer names/quotes (Air Canada, Lufthansa Group, Saudia, Malaysia, flydubai, TAP, Turkish, China Southern, Japan Airlines, Air Europa)
- Accelya: "60+ data points"; "28+ reservation systems"; "70+ airlines"; 712M passengers / 6.2% vs 4.2% growth (T2RL-cited); "up to 20% revenue increase"; FLX ONE module names (Stock Keeper, Availability Calculator, Shop and Price, Schedule Builder); BermudAir customer quote; ancillary attachment claims
- Named integration partners: ATPCO (fare data), OAG (schedule/capacity data), Amadeus/Sabre (as PSS/GDS integration targets)

## Vendor-specific Findings

- The explicit "leg-based vs O&D" product packaging (two configurations by network shape) is documented only by PROS → keep the *distinction* as a common strategy dimension (network effects are evidenced in PROS's network-optimization copy and implied by Accelya's O&D data usage), but the two-configuration packaging is product-specific.
- The three-stage dynamic-pricing maturity model (Dynamic Availability → Continuous Pricing → RSP) is PROS's own journey framing → product-specific; the underlying direction (class-based → class-free) is cross-vendor.
- "60+ data points", "28+ integrations", "11 dimensions", all uplift percentages → vendor claims, recorded only.
- Group Sales Optimizer as a separate product with marginal-revenue group pricing → one family; treat group evaluation as an adjacent capability, not a common requirement.

## Boundary Findings

- **vs Airline Reservation / Passenger Service System** (documented sibling): the PSS holds the airline's flight inventory, sells, tickets, and checks in; RM computes what that inventory should offer. Coupling is a data interface (nightly batch in the classic form; native/real-time in modern forms). Structural test: remove optimization and keep selling → PSS; remove inventory holding/selling and keep optimization → RM. Neither can absorb the other: the PSS research explicitly records "RM computes inventory levels; the PSS holds and executes them."
- **vs Airline Operations Platform** (documented sibling): the ops platform owns flights as *operational* objects (legs, tails, live state, disruptions) and runs the day of operation; RM owns flights as *future revenue* objects and optimizes what to sell. The ops research contains no RM concern and vice versa. A schedule change made by ops changes RM's optimization input; the propagation edge is data, not authority.
- **vs Dynamic Pricing (product layer, not a directory leaf)**: RM decides availability/controls ahead of and around sale time; dynamic pricing computes a price for each shopping request at sale time. Both vendors ship them as separate products, and both describe the pricing layer as *executing* the RM strategy (PROS FAQ: RTDP "seamless execution of your airline's RM strategy"). The boundary is decision time (pre-sale aggregate controls vs per-request prices), not data or goals.
- **vs Hotel Revenue Management System** (separate directory leaf): same optimization discipline (forecast → controls → selling system handoff), different inventory economics. Airline RM's identity comes from the airline substrate: perishable per-departure seats, a booking-class fare ladder, O&D network effects across itineraries, no-show-driven capacity decisions, and interline/codeshare partner availability. Remove the airline flight substrate and the discipline collapses into the hotel/generic pattern — which is why they are different Types.
- **vs Air Cargo Management** (documented sibling): cargo suites contain their own RM engines optimizing weight/volume capacity; the discipline repeats but the objects (AWB shipments, freighter capacity) belong to the cargo Type.
- **vs Revenue Accounting**: RM is pre-sale optimization; revenue accounting is post-sale settlement/audit. In both sampled vendor families they are separate product lines; RM consumes revenue accounting data as feedback, it does not settle anything.
- **vs Flight Search / Booking Platform**: consumer-facing selling vs back-office optimization. RM has no consumer surface at all; its "users" are airline analysts.
- **vs Demand Planning / Retail Pricing Management / Markdown Optimization (other directory sections)**: generic forecasting/pricing analogs. Airline RM is defined by the airline inventory substrate plus the PSS handoff; a demand-planning tool without flight/class/network semantics and without a selling-system handoff is not this Type.
- **"去掉什么就变成另一个 Type" 判据**: remove the forecast → manual availability management (a PSS function); remove the optimization → demand analytics/reporting; remove the selling-pipeline handoff → a forecasting workbench; remove the airline flight substrate (classes, O&D, perishable seats) → generic pricing/demand optimization or the hotel RM pattern; add a consumer selling surface → a booking platform, not RM.

## Uncertainties

1. **Enterprise-flagship tier under-observed.** Amadeus and Sabre (the largest RM installed bases by market reputation) were unreachable, as were Kambr, SITA, and IBS's RM product. Claims rest on two verified products plus sibling corroboration and the T2RL market-category reference. Anything only flagship platforms do (e.g., large-scale interline proration effects on RM, embedded RM inside PSS suites) is deliberately not claimed.
2. **Overbooking mechanics.** No-show/cancellation forecasting is directly evidenced; the overbooking decision itself (accepting bookings beyond physical capacity) is standard industry practice referenced in the sibling PSS research ("including overbooking posture") but no sampled RM page documented the mechanics. The final document states the forecast basis and marks the mechanics as not directly observed.
3. **Control vocabulary universality.** "Bid price" and "protect" are directly evidenced (PROS); "authorization level (AU)" appears once (PROS, point-to-point configuration). Nested-class protection structures are industry-standard in the literature but were not independently evidenced across the sample → the final document uses the evidenced vocabulary and keeps mechanism depth calibrated.
4. **Leg vs O&D universality.** Explicitly packaged by PROS; not surfaced on Accelya's fetched pages. Treated as a common strategy dimension with product-specific packaging.
5. **RM-inside-PSS suites.** Some PSS vendors bundle RM with the reservation system (the iFly case study hints at native coupling). Whether the market treats bundled RM as the same Type is unresolved; the directory leaf stands alone and the research supports it as a distinct Type regardless of packaging.
6. **Help-center depth.** No user guides reachable; UI-level workflows (exact screens, queue/audit mechanics, user-role models inside RM teams) are described conceptually only.
7. **Convergence trajectory.** T2RL (via Accelya PR) frames RM as "evolving beyond traditional forecasting and inventory control toward AI-enabled decision support, dynamic pricing, and closer integration with offer creation." The end-state (RM absorbed into offer optimization vs remaining a distinct control layer) is uncertain; the document models today's stable two-layer pattern (RM decides, pricing/availability executes) without betting on the end-state.

## Final Synthesis

Airline Revenue Management is the airline's commercial optimization system. Its defining loop is small: forecast demand on the airline's future flights; optimize revenue against finite seat capacity, producing inventory and availability controls — which bookings to accept now, which demand to protect for later, at which price points; and hand those controls to the selling pipeline (the reservation system and availability engines) that enforces them every time a customer shops. Around that loop, mature products add the classic control vocabulary of booking classes, bid prices and protection levels; leg-based and network (O&D) optimization modes; no-show/cancellation forecasting that underpins selling beyond physical capacity; analyst workbenches built on manage-by-exception with scenario analysis and system/market/flight configuration authority; external competitive and market data; performance reporting; and — increasingly — sibling dynamic-pricing layers that execute the RM strategy per shopping request, and group-sales evaluators that price group requests against the same capacity economics. The Type's boundaries: against the PSS it is the brain vs the ledger-and-counter (RM computes, the PSS holds and sells); against the operations platform it is future revenue objects vs today's operational objects; against hotel RM it is the same discipline over a different inventory substrate; against revenue accounting it is pre-sale optimization vs post-sale settlement; against generic pricing products it is the airline substrate (perishable seats, fare classes, network itineraries) plus the selling-system handoff. What remains — forecasting demand and deciding what the airline's future flights should sell, so that the selling systems sell it — is this Type.
