# Research Notes — Energy Forecasting Platform

## Research Goal

Understand what an Energy Forecasting Platform really is as an Application Type: what it forecasts, for whom, what structures it is built from, how the forecasting work actually flows, and where its boundary lies against Energy Trading Platforms, Grid Operations/EMS, Demand Planning, Weather Services, and generic ML Platforms.

## Initial Boundary

Working hypothesis before research:

- Core use: produce forecasts of energy quantities (electricity load/demand, wind/solar generation, market prices) for future time intervals, to support trading, grid operation, scheduling, and asset management decisions.
- Likely users: energy traders, forecast analysts, TSO/DSO forecasting and scheduling teams, renewable asset owners/operators.
- Nearest types: Energy Trading Platform (consumes forecasts), Grid Operations Platform / EMS (real-time grid state, may embed load forecasting), Demand Planning (same forecast grammar, different domain), Weather Forecasting Services (upstream input), ML Platform (generic substrate), Energy & Carbon Management (backward-looking sibling in the same directory section).
- Unknowns: is the verification/accuracy loop definitional or merely standard? Is weather input definitional? Are delivery surfaces definitional? Does "platform" imply self-service model management or is the managed-service posture still in-type?

## Research Questions

1. What quantities do products forecast (load, wind, solar, price, hydro, net load, grid flows)?
2. What scopes do forecasts attach to (single asset, portfolio, control zone, price zone, country)?
3. What inputs drive forecast production (NWP weather, measurements/SCADA, availability/curtailment, market data)?
4. How is production organized (runs, horizons, resolution, refresh cadence, re-issuance)?
5. How is accuracy handled (metrics, monitoring, calibration, blending, provider selection)?
6. How are forecasts delivered and consumed (portal, files, API, alerts), and by whom?
7. What sits inside vs outside the Type (nowcasting, weather layers, optimization, monitoring)?
8. How do vendors position against trading/ops software — standalone, service, or suite module?

## Representative Products

Selected 3 (target was 2–5; two further candidates were unreachable — see Sources):

| Product | Vendor / origin | Philosophy | Customer tier | Geography |
|---|---|---|---|---|
| Previento + market forecasts + portal | energy & meteo systems GmbH (emsys renewables group), Oldenburg, Germany | meteorology-specialist forecasting service with web portal and 24/7 on-call | grid operators (100+ incl. 20 TSOs), power traders, plant operators | Europe + worldwide |
| WindFor / LoadFor / PriceFor / MetFor / Regional Forecast | Enfor A/S, Denmark | productized, self-learning forecasting services, deployable on-prem or hosted | TSOs, electricity traders, renewable asset owners | Nordic origin, deployed worldwide |
| Scipher.Fx (+ short-term NEM service) | Utopus Insights (Vestas-owned), SaaS | forecasting product embedded in a renewable asset-management suite; turbine-data-centric | renewable asset owners/operators, power traders; regulatory self-forecasting in Australia's NEM | global (Vestas fleet), Australia NEM focus for short-term |

Selection rationale: three genuinely different product philosophies (specialist meteorology service vs productized self-learning services vs suite-embedded SaaS), three customer tiers (TSO / trader / asset owner), different geographies and regulatory regimes (European zones vs Nordic vs Australian NEM). Amperon (US trading/asset tier) was intended as a fourth but its site timed out twice; Rebase Energy (self-service API pole) timed out once; a DNV forecasting page guess returned 404. Sample stays at three.

## Sources

All fetched 2026-09-08. Evidence layer A (directly observed) unless noted.

- energy & meteo systems / emsys renewables — root (EN): https://www.energymeteo.com/en/ (redirects to https://www.emsys-renewables.com/)
- energy & meteo systems — wind power forecasts (Previento, curtailment, meta forecast, situational awareness): https://www.emsys-renewables.com/products/power_forecasts/wind-power-forecasts.php
- energy & meteo systems — European market forecasts: https://www.emsys-renewables.com/products/power_forecasts/market-forecasts-wind-solar.php
- Enfor — root/services overview: https://enfor.dk/
- Enfor — WindFor: https://enfor.dk/services/windfor/
- Enfor — LoadFor: https://enfor.dk/services/loadfor/
- Enfor — PriceFor: https://enfor.dk/services/pricefor/
- Utopus Insights — root: https://www.utopusinsights.com/
- Utopus Insights — Scipher.Fx: https://www.utopusinsights.com/Scipher.Fx
- Utopus Insights — Short-Term Power Forecasting (NEM): https://www.utopusinsights.com/power-forecasting

Access limitations:

- https://www.amperon.com/ — timed out twice; dropped per network rule. US trading/asset tier therefore not directly observed.
- https://www.rebaseenergy.com/ — timed out once; dropped.
- DNV forecasting page — URL guess returned 404; not pursued further.
- No vendor help-center/login-protected operational documentation was reachable; all evidence is from public product/marketing pages. Precise operational parameters (exact refresh schedules per customer, exact metric thresholds, pricing) are therefore not asserted anywhere.

## Product Observations

### energy & meteo systems (emsys renewables group) — Evidence Layer A

- Positions itself as forecasting wind and solar power "for individual assets, portfolios, or entire markets"; customers: power traders, grid operators, plant operators. Claims ~400 GW wind and ~400 GW solar under forecast, 350 customers, 100+ grid operators including 20 TSOs, "several million prediction data sets" delivered to customers on 6 continents.
- Wind forecasting system **Previento**: forecasts "for any onshore and offshore location as well as for control zones and grid nodes"; horizon "from 5 minutes to 15 days in advance"; uses numerical data from all leading weather services; **KombiBox method** — the forecast with the lowest forecast error for the respective weather situation is given greater consideration (situation-dependent weighting of weather models); calculates an associated **uncertainty for each forecast situation**; adapts to real-time measurement data.
- Handles extreme weather (thunderstorms, cold fronts, snow) and production-reducing factors: night/bird/bat shutdowns, storm shutdowns; incorporates market curtailments and grid-operator curtailments into models.
- **Two forecast variants**: (1) forecast of *real feed-in* — includes all curtailments (grid measures, technical restrictions, scheduled unavailability); (2) forecast of *technically possible feed-in* — technical/scheduled unavailability only, no market/grid curtailments. Curtailment forecasts validated against measures published by DSOs/TSOs; available at wind-farm, portfolio, or whole-market level.
- **Meta performance forecast**: combines its own model with other providers' forecasts; optimal weighting determined from historical performance; weighting adjustable automatically and manually; short-term correction reacts dynamically to weather changes; claimed above-average precision beyond four days.
- **Situational awareness reports**: meteorologist-written warnings for storms, icing, thunderstorms for grid operators and traders, in real time.
- **Market forecasts** (Europe): wind/solar aggregated at **price zone and country level** (wind >30 countries, solar >15); horizons from intraday with quarter-hourly updates up to ten days; all forecasts in quarter-hourly resolution; **model spreads** for uncertainty assessment; **historical forecast data** available on request; expert weather reports for Germany each morning with alerts for intraday/day-ahead trading.
- **Solar power estimate**: real-time solar estimation (nowcast) as separate product.
- **Vertical grid load** forecasts (grid management arm): forecast of vertical grid load and power flows for grid operators.
- Delivery: web-based **customer portal** for visualizing and managing measurement and forecast data; 24/7 on-call expert service; customized delivery formats.
- Group context: energy & meteo systems (forecasts) sits alongside emsys VPP (virtual power plant) and emsys grid services (grid platform) — the forecasting arm feeds the group's trading/VPP/grid products.

### Enfor (ENFOR™ platform) — Evidence Layer A

- Platform of named forecasting services: WindFor (wind power), SolarFor (solar), LoadFor (electricity load), MetFor (locally optimized weather forecasting), Regional Forecast (country/zonal wind, solar, load), PriceFor (power price), HydroFor (hydro), plus ChargeME (EV smart charging) and PMon (performance monitoring) — the latter two are adjacent capabilities, not forecasting.
- **WindFor**: "predictions of wind power production for the operational horizon (ranging from a few minutes ahead in time, up to a couple of weeks)"; portfolio scale or country-wide; combination of **physical models and machine learning**; initialized from the wind farm's design power curve or from historical weather + production data; **forecasts produced every time new data arrives** (updated weather forecasts or new production data); **online mode** (continuous real-time production data, e.g. SCADA integration) or **offline mode** (historical data retrieved monthly or other interval); uses one or more weather forecast providers, **automatically detecting the optimal prioritization per wind farm and per forecast horizon**; ensemble weather forecasts supported; weather data also made available to the client for comparison; self-learning/self-calibrating — adapts to changing conditions, season, turbine aging; client-provided availability and curtailment schedules are taken into account; real-time availability/curtailment data trains models and adjusts short-term forecasts; configurable horizons, time resolution (different intervals for intraday vs day-ahead/week-ahead), update frequency; **spatio-temporal correction** using error correlation between farms in the same region; configurable performance reports; data integration via FTP/SFTP/web services (CSV, XML, SOAP, JSON); browser-based GUI; local install or hosted service; error handling, fallback procedures, substitute-value estimation, warning system.
- Special modules: uncertainty bands (quantiles) for bidding/risk; scenario generation; cut-out risk at high winds; ramping probability; ice detection and ice-decay forecasting; **combination module** (optimal weighting of multiple internal forecasts based on different weather providers and/or external forecasts); downscaling for complex terrain; **upscaling** (online measurements from some farms improve forecasts for farms without online measurements); curtailment lost-production estimation; high-resolution forecasting (5 minutes or less).
- **LoadFor**: ML-based, self-learning/self-calibrating; inputs: historical load, historical meteorological data, meteorological forecasts, optionally online power measurements; portfolio or country-wide; automatically models building thermal dynamics (heating/cooling smoothing); adapts to changes in consumer behavior, consumer count, meteorological models, grid characteristics; **data collection and validation module** with automatic detection/correction of missing/erroneous measurements feeding the core module; web interface for configuration and monitoring; FTP/SFTP/web-services integration; local or hosted.
- **PriceFor**: day-ahead electricity price forecasting; inputs: historical prices, capacity margins, wind power predictions, consumption predictions; **updated three times daily, last update right before gate closure** (N2EX UK; Nordic on request); self-learning/self-calibrating; delivery in almost any file format, integrated into the client's operational IT platform; hosted service.
- Customers: TSOs (system stability, balancing cost, curtailment minimization), traders/retailers (nomination, imbalance fees/penalties, price prediction), asset owners (nomination and trading of production).
- Vendor claims "availability of 99.9% and above" for clients requiring it — vendor claim, not independently verified.

### Utopus Insights (Scipher.Fx) — Evidence Layer A

- Vestas-owned SaaS analytics company; **Scipher** suite: data platform, Vx/Vx+ asset management/visualization, **Scipher.Fx power forecasting**, mobile app. Claims 103 billion signals processed daily, 55,000+ turbines, 128 GW assets, 70+ countries.
- **Scipher.Fx**: "comprehensive wind and solar PV power forecasting" for "renewable asset farm owners, operators, and power traders"; forecasts **day-ahead, intraday, and longer-term**; combines **turbine metadata, global Numerical Weather Prediction models, and historical data**; direct real-time data ingestion from Vestas turbines; **computes accuracy using standard metrics: MAE, RMSE, MAPE**; "advanced user interface to visualize and analyze forecast accuracy"; ability to include **maintenance schedules to adjust power forecasts**; forecast data delivered via **sFTP/FTP/email at user-defined intervals**.
- **Short-Term Power Forecasting (Australia NEM)**: 5-minute-ahead continuous forecasting enabling **self-forecasting** by semi-scheduled generators in the National Electricity Market; producers submit 5-minute dispatch forecasts alongside ANEMOS dispatch forecasts to align output with offers in the dispatch engine (NEMDE); **forecast submission <4 minutes from farm to forecast** via secured API; secured direct farm connectivity ingesting from all OEMs; high-resolution/low-latency measurement flow; 24/7 data and model monitoring and support; ARENA-qualified first self-forecasting provider; vendor-claimed outcomes: >15% accuracy improvement, 26% reduction in causer-pay penalties (vendor claim from ARENA-participating pilot).
- Forecasting is one product inside an asset-management suite; the suite's other products (asset visualization, performance) are adjacent Types.

## Cross-product Comparison

| Dimension | energy & meteo systems | Enfor | Utopus Insights |
|---|---|---|---|
| Forecast targets | wind power, solar power, vertical grid load, solar nowcast | wind, solar, load, price, hydro, regional aggregates | wind, solar PV power |
| Forecast scope | single turbines → farms → control zones → grid nodes → price zones/countries | single farms/portfolios → country-wide | wind/solar farms (asset level) |
| Weather input | multiple leading NWP models, situation-weighted (KombiBox) | multi-provider, per-farm/per-horizon auto-prioritization, ensembles; weather also sold standalone (MetFor) | global NWP models |
| Measurement/actuals input | real-time measurements adapt forecasts; portal holds measurement data | online SCADA mode or offline historical mode; validation module | direct real-time turbine ingestion (Vestas; all-OEM connectivity for NEM) |
| Production trigger | scheduled updates (intraday quarter-hourly for market forecasts) + short-term correction | every new data arrival; configurable update frequency | continuous (5-min cadence for NEM); user-defined delivery intervals |
| Horizon range | 5 min – 15 days (wind); intraday – 10 days (market) | minutes – ~2 weeks | day-ahead, intraday, longer-term; 5-min-ahead short-term |
| Uncertainty | per-situation uncertainty; model spreads | quantile bands, scenario generation, ramping/cut-out probabilities | not evidenced on public pages |
| Blending/combination | KombiBox + meta-forecast incl. external providers, weighted by historical performance | combination module (internal + external), multi-provider prioritization, upscaling | not evidenced |
| Curtailment/availability | real vs technically-possible feed-in variants; curtailment forecasts validated vs published measures | availability/curtailment schedules as input; curtailment lost-production module; real-time curtailment data adjusts short-term | maintenance schedules adjust forecasts |
| Accuracy management | historical-performance weighting; validation against published curtailments | configurable performance reports; self-calibration | MAE/RMSE/MAPE; accuracy-analysis UI; 24/7 model monitoring |
| Delivery | web portal; customized formats; 24/7 on-call | FTP/SFTP/web services; browser GUI; local or hosted | sFTP/FTP/email; secured API submission (NEM); product portal |
| Human layer | meteorologist situational-awareness reports | support/maintenance agreements | 24/7 support |
| Deployment | managed service + portal | on-prem software or hosted service | SaaS suite module |

## Canonical Model

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The forecast subject of record** — a defined energy quantity (renewable generation, electricity demand, market price) over an identified scope (asset, portfolio, control/price zone, market area), for future time intervals. Remove → weather service (weather is input, not output) or generic analytics.
2. **Recurring model-driven forecast production** — models combining historical behavior of the subject with forward-looking exogenous drivers (weather forecasts above all; also calendars, availability/curtailment, market data) producing values at future timestamps at a defined horizon and resolution, re-issued as inputs update. Remove → historical analytics/reporting.
3. **The forecast-vs-actual verification loop** — actual outcomes are captured and compared against issued forecasts; accuracy is measured, tracked, and fed back (calibration, re-weighting, provider/model selection, retraining). Remove → one-off prediction calculator with no accountability or improvement.

Jointly-held is load-bearing: 1+2 without 3 = forecast generator with no accuracy discipline; 2+3 without 1 = generic time-series ML platform; 1+3 without 2 = a manual analyst desk, not a platform.

### L1 — Common Mature Structure

- Multi-target catalogs: wind, solar, load, price, hydro under one platform (all three products cover ≥2 targets; Enfor covers five).
- Weather forecast data as the dominant input, often multi-provider with automatic per-subject/per-horizon selection or weighting.
- Real-time measurements/actuals ingestion (SCADA, meters) improving short-term forecasts.
- Configurable horizons, resolutions, and update frequencies; forecast re-issuance on a schedule.
- Uncertainty quantification (quantile bands, scenario generation, per-situation uncertainty, model spreads) — evidenced at 2 of 3 products; treated as common, not definitional.
- Model blending/combination across weather providers and across vendors' forecasts, weighted by historical performance — evidenced at 2 of 3.
- Availability/curtailment/maintenance awareness in forecasts — all three.
- Accuracy measurement with standard metrics (MAE/RMSE/MAPE named by one; performance reports by another; historical-performance weighting by the third) and accuracy-monitoring surfaces.
- Data ingestion + validation machinery (missing/erroneous data detection, fallback/substitute values, warnings).
- Delivery surfaces: web portal/dashboard + machine feeds (FTP/SFTP/web services/API/email).
- Managed-service posture with human expert layer (24/7 on-call, meteorologist reports) in service-led products.

### L2 — Variant / Optional Structure

- Target specialization as productization (separate named products per target vs one platform).
- Market-level aggregated forecasts (price zone/country) vs asset/portfolio-level.
- Real feed-in vs technically possible feed-in as parallel forecast variants.
- Nowcasting / real-time estimation as an extension of short-term forecasting.
- Weather forecasting itself productized as a layer (MetFor) vs consumed from third parties.
- Regulatory-regime variants: self-forecasting markets (Australia NEM 5-minute dispatch), balancing/imbalance penalty regimes (Europe), nomination obligations.
- Deployment: managed service vs on-prem software vs hosted vs SaaS suite module.
- Human-in-the-loop meteorologist reporting (situational awareness) as an add-on.
- Historical forecast archives as a deliverable.

### L3 — Vendor-specific (kept out of final document)

- Named systems and methods: Previento, KombiBox method, meta performance forecast, WindFor/LoadFor/PriceFor/MetFor naming, Scipher.Fx, ANEMOS/NEMDE submission specifics, ARENA qualification claims, vendor-claimed accuracy/penalty numbers (15%, 26%), scale claims (400 GW, 55,000 turbines, 103 billion signals), availability claims (99.9%).

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- 1990s–2000s utility short-term load forecasting systems (statistical regression on weather-service inputs, run daily, error tracked and models re-fit): satisfy all three L0 structures — no ML, no ensembles, no cloud portal required.
- Early wind power forecasting tools of the 1990s–2000s (physical power-curve models + NWP feeds, daily runs, error verification): satisfy the core.
- A spreadsheet-era forecasting desk (weather fax/phone inputs, regression, manual re-fit) satisfies 1+3 but not recurring automated production at platform grade — correctly excluded as "not a platform," matching the L0's joint-hold logic.
- Regional regimes (Australian self-forecasting, European imbalance penalties, Indian forecasting-fee regimes referenced in vendor project pages) all instantiate the same core with different regulatory pressure.

Conclusion: L0 survives the historical check; ML, ensembles, portals, APIs, and quantile machinery are era-current implementations, not definitional.

## Vendor-specific Findings

- energy & meteo systems: KombiBox situation-dependent weather-model weighting; meta-forecast that ingests competitors' forecasts; dual real/potential feed-in variants validated against published TSO/DSO curtailment measures; meteorologist-written situational awareness reports; vertical grid load forecasting for grid congestion management.
- Enfor: upscaling module (online measurements from some farms improve forecasts for farms without online data); spatio-temporal error correction; ice detection/decay and cut-out/ramping probability modules; building-thermal-dynamics smoothing in load forecasting; data-validation toolbox with substitute-value estimation; price forecasting updated three times daily with last update before gate closure (N2EX).
- Utopus Insights: forecasting embedded in an asset-management suite over a turbine fleet; direct Vestas turbine ingestion; NEM self-forecasting submission with <4-minute farm-to-forecast latency; MAE/RMSE/MAPE as named accuracy metrics.

## Boundary Findings

- **vs Energy Trading Platform**: trading consumes forecasts; its core objects are positions, orders, bids, portfolios. The forecasting platform's core object is the forecast itself plus its accuracy record. A forecasting module inside a trading terminal is a capability overlap, not this Type's center. Remove the forecast-production/verification core and keep trading objects → Energy Trading Platform.
- **vs Grid Operations Platform / EMS**: EMS centers on real-time grid state and dispatch; load forecasting is a classic embedded EMS function. When forecast production + verification is the system's center of gravity, it is this Type; when supervisory control and grid state is, it is EMS/Grid Ops. emsys's grid arm (redispatch, congestion) is a different product line from its forecasting arm — a live seam specimen.
- **vs Demand Planning (supply chain)**: same forecast grammar (history + drivers → future demand), but the subject is product demand for goods in inventory/distribution networks; energy forecasting's subject is energy quantities under weather physics and grid/market geography. Different domain objects, different inputs, different consumers.
- **vs Weather Forecasting Services**: weather is the dominant input, not the output. A weather-API vendor producing meteorological fields is upstream. The seam: the output quantity. Enfor's MetFor shows a forecasting vendor productizing the weather layer — the weather product alone would be out-of-type.
- **vs ML Platform (generic)**: generic ML platforms offer training/deployment for arbitrary data. Here targets, inputs (NWP, SCADA, curtailment), scopes (zones/farms), and the verification discipline are domain-defined. Remove the energy-domain packaging → generic ML platform.
- **vs Energy & Carbon Management** (sibling leaf, processed): that Type is the backward-looking energy data of record + carbon + performance loop; this Type is forward-looking production of future quantities. Remove the future orientation → energy management/analytics; add it → forecasting.
- **vs Renewable/Wind/Solar Asset Management**: asset management monitors and operates the installed fleet (performance, availability, maintenance); forecasting predicts future production of that fleet. Utopus shows both in one suite — distinct products (Vx vs Fx).
- **vs Demand Response Platform / VPP**: those act on flexibility (dispatch, curtail, aggregate); forecasting predicts. emsys group structure (forecast company + VPP company + grid company) is a live specimen of the seam.
- **"去掉什么就变成另一个 Type" 判据**: remove the energy-quantity subject → weather service / generic ML; remove future orientation → energy analytics/management; remove the verification loop → prediction calculator/API; remove recurring production → study/consulting.

## Uncertainties

- US trading-tier products (Amperon and peers) not directly observed; the trader-facing pole is evidenced via emsys market forecasts and Enfor PriceFor/trader positioning, but US-specific shapes (e.g., nodal/ISO forecasting) are unverified.
- Self-service model-management surfaces (customer-trainable models) not evidenced in the sample; all three products keep model ownership with the vendor. Whether a "build-your-own-forecast-model" pole exists as a distinct variant is unverified.
- Uncertainty quantification at Utopus not evidenced on public pages; treated as common (2 of 3) rather than universal.
- Pricing, exact SLA terms, and per-customer refresh schedules are not public; no precise operational parameters asserted.
- Whether grid-operators' internal EMS-embedded load forecasting should count as an instance of this Type or only as an embedded capability: recorded as a boundary question, resolved in favor of "embedded capability" (the standalone Type is the forecast-centric system).

## Final Synthesis

An Energy Forecasting Platform is the energy sector's forecast-production system of record: it holds defined energy quantities (renewable generation, demand, price) over identified scopes as forecast subjects, produces future values for them repeatedly through models that combine historical behavior with forward-looking drivers (weather forecasts above all), and runs a permanent verification loop in which actuals are compared against issued forecasts and accuracy is measured, tracked, and fed back into calibration and model/provider selection. Everything else — multi-target catalogs, ensembles, quantile bands, blending, portals, APIs, nowcasting, meteorologist reports, regulatory self-forecasting — is mature structure or variant layered on that core. The Type is bounded against trading (consumes forecasts), grid ops/EMS (real-time state), demand planning (different domain), weather services (input supplier), generic ML (domain-free substrate), and energy & carbon management (backward-looking sibling).
