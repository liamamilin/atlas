# Research Notes — Customer Energy Management

## Research Goal

Understand what "Customer Energy Management" software actually is as an Application Type: who operates it, what objects exist inside it, what loop it drives, and where its boundary lies against neighboring Types — especially Building Energy Management (§17, processed), Advanced Metering Infrastructure / AMI (§19, processed), Utility Billing / CIS (§19, unprocessed), Demand Response Platform (§19, unprocessed), EV Charging Network Management (§19, unprocessed), smart-home/thermostat apps (outside directory), and solar/DER monitoring apps (outside directory).

Open cross-references to discharge from sibling passes:
- Building Energy Management pass recorded: "vs Customer Energy Management (§19) — consumer/home pole of energy data; BEM's users are organizations managing buildings."
- AMI pass recorded: "Consumer portals (My360, Consumer Engagement) are optional extensions of AMI data; the consumer-facing usage/insight application is a different Type with the consumer as operator."

## Initial Boundary (hypothesis before research)

Working hypothesis: this is the energy-customer-side application — software used by the users of energy (households, and per Opower evidence, also business customers) to observe, understand, and act on their own energy consumption and cost at their own premises. The name "customer" comes from the utility industry ("the utility's customer"), so one pole is utility-provided, white-labeled customer engagement software; another pole is consumer-owned home energy monitor apps. Expected neighbors: utility-side systems (AMI/MDMS/CIS/billing), building-side management (BEM), demand response, smart home, solar monitoring.

## Research Questions

1. Who operates the application — the utility, a third party, or the customer themselves? What changes with the operator?
2. What is the central object: the utility account, the home, the device fleet, or the usage record?
3. Where does usage data come from (AMI feed, in-home monitor, smart plugs, device gateway) and does the data path change the Type?
4. What does the customer actually do: view usage, compare, get alerts, compare rates, control devices, join programs, pay bills?
5. What role do bills/costs play, and where does billing itself sit (in or out of this Type)?
6. Are business customers inside this Type or a different one?
7. Where are the exact seams vs BEM, AMI, Utility Billing, Demand Response Platform, smart-home apps, solar monitoring apps?
8. Historical check: do pre-AMI, monthly-read-era and regional products (paper home energy reports, in-home displays, monthly web portals) satisfy the definition?

## Representative Products

| Product | Pole | Why selected |
|---|---|---|
| Oracle Utilities Opower / Digital Self Service – Energy Management | utility-provided white-label consumer engagement (market-leading heritage: behavioral Home Energy Reports) | deepest available Tier-1 documentation of the utility pole; covers residential AND business customers |
| Emporia Energy | consumer-owned monitor + control platform | consumer pole with full control/automation machinery; rich help center |
| Sense | consumer-owned insight/monitoring (no primary control) | insight-first philosophy; second data path via utility smart meter; ML device detection |
| Enphase (Enphase App) | generation-integrated home energy (solar/battery/EV) | the DER-owner pole: production, storage, and export flows managed beside consumption |

Rejected/alternate candidates: Uplight (utility customer-experience suite — site returned HTTP 403, abandoned), NISC SmartHub (utility consumer portal — request timeout, abandoned), Bidgely/Grid4C (white-label AI engagement — thin public docs), Tesla app (device-app first), utility-branded portals (deployments of the above, not independent structures).

## Sources

- Oracle Utilities — product catalog: https://www.oracle.com/utilities/ (fetched 2026-09-07)
- Oracle Utilities — Opower Digital Engagement product page: https://www.oracle.com/utilities/products/opower-engagement/ (fetched 2026-09-07)
- Oracle Help Center — Digital Self Service – Energy Management docs root: https://docs.oracle.com/en/industries/utilities/digital-self-service/ (fetched 2026-09-07)
- Emporia Energy — site + Home Energy Management Platform page: https://www.emporiaenergy.com/ , https://www.emporiaenergy.com/home-energy-management/ (fetched 2026-09-07)
- Emporia Help Center — Energy Management and Emporia App collections: https://help.emporiaenergy.com/en/ , https://help.emporiaenergy.com/en/collections/17275032-energy-management , https://help.emporiaenergy.com/en/collections/8823780-emporia-app (fetched 2026-09-07)
- Sense Help Center — root + "Introducing the Sense Home App" section + "How Does Sense Help Me Save Energy and Money?" + "How Sense Learns About Your Home's Energy Use": https://help.sense.com/hc/en-us (+ articles) (fetched 2026-09-07)
- Enphase — Enphase App page: https://enphase.com/homeowners/enphase-app ; Enphase Support + Enphase Assistant FAQ: https://support.enphase.com/s/ (fetched 2026-09-07)

Source-access limitations:
- Uplight: HTTP 403 (root), abandoned after one attempt. No claims about Uplight anywhere.
- NISC SmartHub: request timeout, abandoned. No claims about SmartHub anywhere.
- support.emporiaenergy.com: transport error ×1; help.emporiaenergy.com reachable and used instead (Tier 1 for Emporia stands).
- Oracle DSS-EM docs root fetched; the deeper per-feature guide pages were not fetched individually (linked via redirects). Claims for the utility pole rest on the DSS-EM docs root + the Opower Digital Engagement product page + the Oracle Utilities catalog page — all directly fetched.
- No second utility-pole vendor was reachable; utility-pole findings marked Layer A rest on Opower alone and are flagged; cross-pole findings (Layer B) span the poles instead.

## Product Observations

### Oracle Utilities Opower — Digital Self Service – Energy Management (utility pole)

Evidence layer: A (directly observed on Oracle's product page and docs root).

- Positioning (docs root): "Digital Self Service - Energy Management gives utilities unprecedented flexibility in creating highly engaging, targeted web and mobile experiences for their customers. The solution provides online energy and billing insights and tools that enable customers to explore and change their energy behavior." — the operator is the UTILITY; the customer is the utility's customer.
- Scope spans residential AND business customers: "Accelerate your customer experience roadmap across residential and business customers." A separate Business Customer Engagement service exists for SMB/C&I with: self-serve energy insights, bill forecast/comparison, data browser, "advanced insights" (demand heatmaps, reactive power), Green Button download (customer exports their usage data to a tool of their choice), and guest user access (business users grant web-tool access to other people — energy managers, facility managers, finance).
- Feature set observed on the product page: web and mobile experiences deployed as "widgets embedded directly into utility websites, seamless single sign-on pages, and APIs" (white-label); neighbor comparison ("gauge their energy consumption against similar homes in their neighborhood"); bill forecast and comparison (projected usage/cost for the current billing period; current bill vs previous/year-ago benchmarks); home energy audits; energy use insights (visualize/explore behavior, trends, costs); personalized savings tips library; targeted digital marketing (segmentation tool driving program promotions); high bill alerts (identify customers "trending toward a high bill", auto-send alerts with insights/tips/program promotions); weekly energy updates "powered by smart meter data" (day-by-day benchmarking); rates engagement (rate education reports; TOU rate plan recommendation "based on a personalized analysis of past energy use"; on-demand rate analysis tool with cost forecasts per plan; behavioral load shaping — a "rate plan coach" with week-over-week peak vs off-peak comparisons and shifting recommendations).
- Purpose framing: deliver on the AMI business case ("displaying interval energy use data directly to customers"), reduce cost-to-serve (deflect call-center volume), increase program adoption, demand-side management/decarbonization.
- The platform family confirms boundary objects: bill/pay lives in the sibling "Digital Self Service - Transactions"; direct device control lives in a separate "Device Control" cloud service; behavioral demand response lives in "Peak Management: Behavioral Demand Response" and "Peak Time Rebates" services. DSS-EM itself is insight + advice + program-connecting, with control and transactions as separable siblings.
- Heritage: Opower home energy reports (behavioral) are named on the utilities catalog page as the engagement vehicle since 2009 — i.e., the neighborhood-comparison + tips pattern predates the web app (paper reports). Vendor-published aggregate statistics (TWh saved, reads managed) are claims and are NOT repeated in the final document.

### Emporia Energy (consumer pole — monitor + control)

Evidence layer: A (directly observed on site + help center collections).

- The platform: "monitor energy usage in real-time, down to individual circuits and appliances, and automatically adjusts connected devices to optimize electricity use and maximize savings." Operator = the homeowner (own account, own devices).
- Data paths: Vue energy monitor (panel CT clamps, circuit-level), Smart Plugs (per-appliance), Vue Utility Connect (wireless monitoring from the utility smart meter "in select utility service areas") — a consumer product that can attach to the utility's meter.
- The "Home" object: devices grouped by property — "location, utility rates, billing, and sharing stay in one place, including if you manage more than one." Homes carry utility-rate configuration; Home sharing exists (multi-user); Invite2Charge adds access control for EV chargers.
- Cost machinery: "Utility Rates and Energy Costs — add utility rates to track energy costs with manual or NREL-based plans"; solar buyback rates; usage charts with drill-down/custom dates; CSV export "to align with utility billing cycles"; data storage/deletion management.
- Automation machinery (all help-center documented): Device Schedules (time-based), Smart Scheduling (shift usage to cheapest hours, synced with utility TOU rates), Peak Demand Management ("automatically manage usage to avoid peak demand charges... adjusts connected devices before you cross your utility's peak threshold"), PowerSmart (EV charging rate regulated in real time against whole-home panel load), Intelligent Load Sharing / ChargeBoost (multiple chargers / smart-meter-assisted), Excess Solar Management + Solar Window (auto-activate devices on surplus solar generation), Home Battery ("smart enough to skip peak rates").
- Proactive surfaces: customizable notifications and alerts; new Home Screen showing "costs, controls, and savings"; EV charger savings reports; AI Energy Assistant ("explore your energy data through natural conversation") + MCP server for external AI tools.
- Integrations: Nest thermostat, Home Connect appliances, Alexa/Google voice control.
- Retail-plan extension (deregulated market): "Electricity Plans built for your devices, now available in Texas" — the vendor also retails electricity plans shaped for EV charging/solar; a business-model extension of the energy-management relationship.

### Sense (consumer pole — insight first)

Evidence layer: A (directly observed on help center articles).

- Definition (article): "Sense is a mobile app that you use from your phone to measure and manage your home energy use in real time. Sense collects your home's electrical usage data from your utility, working either with a Sense-enabled smart meter installed by your utility or with a monitoring device installed in your electrical panel." — two data paths: utility smart meter OR own panel monitor. This is direct evidence that the utility data path and the own-hardware path lead into the same kind of customer-side application.
- Insight machinery: real-time power meter ("turn devices on and off" to identify them); ML device detection ("signatures", detection takes "days to weeks"; user names and merges detected devices); smart plugs for hard-to-detect devices; direct circuit monitoring for large 240V loads; "Always On" tracking (standby/vampire load) — vendor statistic about its share of bills NOT repeated; usage reports across hourly → annual periods; TOU cost tracking — "If your electricity provider has instituted Time of Use (TOU) period variations, you can simply tell the app what rate variations are in place and Sense will help you track those as well" (the customer configures the tariff).
- Action machinery (behavioral, not control): energy-saving goals ("set realistic energy-saving goals and track your progress in the app"); anomaly/fault detection ("well pump turning on frequently... could mean something is leaking"; appliance usage creeping up "possibly indicating a costly problem").
- Bill relationship stated explicitly: "Now, in addition to receiving a bill at the end of each month, Sense gives you insight into how and when your appliances and devices use electricity and how much their use costs you." — the application complements the bill; it does not replace billing.
- No evidence in fetched pages of Sense controlling HVAC/battery directly; presence of smart-plug integration is for monitoring precision. Treat "control" as product-dependent, not definitional.

### Enphase (Enphase App) (generation-integrated pole)

Evidence layer: A (product page directly observed; support/Assistant FAQ directly observed).

- Positioning: "Make, use, save, and sell your own power right from the palm of your hand." — the household as producer-consumer (prosumer); grid as counterparty.
- Monitoring: system status anywhere; production by day/week/month/year; panel-level production detail; grid imports AND exports tracked; battery activity; consumption.
- Metrics: "Solar Offset, Grid Dependence, and Energy Independence, along with a five-day production forecast"; money saved + environmental impact; downloadable/emailable reports.
- Control: battery modes, reserve level, grid charging on/off, Storm Guard (storm-preparation mode), discharge schedules; EV charger control ("Start charging my EV"); load controllers ("manage power-hungry appliances"); all changes gated by explicit user confirmation in the Assistant.
- Cost dimension: assistant can ingest an uploaded electricity bill "for a better understanding of your energy costs"; assistant knows "tariff or rate plan" as account data; "optimize my battery to save money" as a query.
- AI layer: Enphase Assistant (AI-powered energy advisor with access to real-time system data when logged in; conversation history retained; settings changes only with confirmation).
- Two-sided product: installers have a separate portal (Enlighten/Installer Portal); the homeowner app is the customer-side surface. Business-owner products exist separately.

## Cross-product Comparison

| Dimension | Opower DSS-EM (utility pole) | Emporia | Sense | Enphase |
|---|---|---|---|---|
| Operator | utility (white-label web/mobile) | homeowner (own account) | homeowner | homeowner (installer portal separate) |
| Managed unit | the utility customer's premises/account (residential & business) | the "Home" (device grouping per property) | the home | the home energy system (site) |
| Usage data path | utility meter/AMI feed via utility integration | own monitor/plugs; optionally utility meter (wireless) | utility smart meter OR own panel monitor | own gateway metering (production + consumption + grid) |
| Usage visibility | usage insights, trends, data browser | usage charts, drill-down, CSV export | real-time meter, periods hourly→annual | production/consumption/grid/battery flows |
| Cost machinery | bill forecast/comparison; rate-plan analysis | utility rates (manual/NREL), buyback rates, cost views | TOU configured by user; cost per device | bill upload; tariff/rate plan known to assistant; savings |
| Comparison | neighbor comparison (similar homes), bill vs prior/year-ago | period-over-period charts | trends over time; goals | savings/offset metrics, forecast |
| Proactive outreach | high-bill alerts, weekly updates, rate education, program marketing | notifications/alerts; savings reports | anomaly/fault detection framing | storm prep, forecast, assistant |
| Advice | personalized tips, audits, rate coach | automated schedules (advice embedded in automation) | tips, goals, fault flags | assistant recommendations, upgrade suggestions |
| Customer action | behavior change, plan choice, program enrollment | automated device control + schedules | behavior change + goals | direct device/battery/EV control |
| Program/plan participation | central (program promotions, TOU enrollment) | utility incentives; retail electricity plans (one market) | not observed | grid-services surface (installer-facing) |
| Bill/pay | bill insight in Type; pay in sibling Transactions product | cost tracking aligned to billing cycle; no bill pay | explicitly "in addition to receiving a bill" | bill upload for cost understanding |
| Business customers | first-class (SMB/C&I variant) | no | no | separate business products |
| AI/ML | behavioral science + analytics (vendor-framed) | AI assistant + MCP | ML device detection | AI assistant |

### What is constant (candidate defining core)

1. **The customer's own premise as the managed context.** Every product organizes everything under one identified site/account that belongs to the user of the energy (utility account + service point; "Home"; home; system/site). Business variants keep the same shape (the business's premises/account).
2. **The customer's own usage made visible as data.** Consumption recorded over time and shown to the customer — regardless of whether it arrives from the utility meter, an in-home monitor, smart plugs, or a device gateway. Where production/storage exist, they join the same picture.
3. **The insight → action loop.** Usage is turned into findings — cost, comparisons, forecasts, anomalies, tips, goals — whose purpose is customer action: changing behavior, controlling/automating devices, choosing rates/plans, participating in programs. All four products frame the purpose in exactly these terms ("explore and change their energy behavior"; "monitor... and automatically adjusts"; "make smart choices and set goals"; "make, use, save, and sell").

### What is common-but-not-defining

- Cost dimension (rates/tariffs applied to usage) — present in all four, but TOU/tariff setup is user-configured in some products and pre-integrated in others.
- Proactive outreach (alerts, updates, reports) — all four in some form.
- Peer/temporal comparison — neighbor comparison is utility-pole signature; period comparison everywhere.
- Device-level detail — device detection/disaggregation or plug-level metering.
- Device control/automation — strong in consumer pole; separable sibling in utility pole; absent in the insight-only sample.
- Bills — bill forecast/comparison/export common; bill PAYMENT not part of this Type in any sampled product.
- Multi-surface delivery (mobile + web), multi-user sharing, AI assistants.

### What is variant/pole-dependent

- Operator model (utility-provided vs customer-owned product) — the biggest fork.
- Data path (AMI/utility feed vs in-home monitor vs smart plugs vs device gateway).
- Generation/storage integration (prosumer pole).
- Business-customer support (utility pole only in sample).
- Retail-plan distribution (deregulated markets).
- Real-time vs monthly cadence (data-path-dependent).

## Abstraction Levels

### L0 — Defining Invariant (minimal)

A customer-side energy management application is:

1. **Customer-side operation on one's own energy** — the operator is the energy customer (a household or a business customer) acting on their own premises' energy, not an organization managing a portfolio or a utility managing the grid. (remove → Building Energy Management / utility-side systems)
2. **The premise's usage made visible to the customer as data over time** — their consumption (and where present production/storage) recorded and shown in the application. (remove → marketing site / raw data export only)
3. **The insight → action loop** — the application turns usage into findings (cost, comparison, forecast, anomaly, advice, goals) whose purpose is customer action: behavior change, device control/automation, rate/plan decisions, program participation. (remove → passive data feed/portal without management purpose; keep only the action leg → smart-home control app; keep only the insight leg → an energy data dashboard without the management loop)

Historical check (per §24 discipline): monthly-read-era utility web portals (usage shown from monthly meter reads) satisfy all three; the paper home energy report tradition (neighbor comparison + tips by mail) is the behavioral ancestor of the same loop; regional in-home display + app pairs and non-US HEMS traditions satisfy the core without AMI, real-time data, control, solar, or ML. Therefore none of those belong in L0.

### L1 — Common Mature Structure

- cost machinery: rates/tariffs (TOU) attached to usage; cost views and savings figures
- comparison machinery: period-over-period, peer/neighbor benchmark (utility pole), expectations/goals
- proactive outreach: alerts (high-bill risk, anomalies), scheduled usage updates/reports, tips
- device-level insight: disaggregation/detection or per-plug/circuit metering
- bill relationship: bill forecast/comparison/export aligned to billing cycles (not payment)
- device control/automation in the consumer pole; program enrollment + rate-plan tools in the utility pole
- mobile + web surfaces; account with sharing in some products; AI assistance (era-typical)

### L2 — Variant / Optional

- operator model: utility white-label vs customer-owned product vs (retail supplier) plan provider
- data path: AMI/utility feed / panel monitor / smart plugs / device gateway / utility-meter wireless bridge
- generation + storage integration (prosumer pole), grid export tracking, self-consumption optimization
- business-customer variant (demand-level insights, data export, guest access)
- direct load control / DR participation depth (from advice-only to automated response)
- retail electricity plan distribution (deregulated markets)
- carbon/footprint estimates, environmental impact reporting
- real-time cadence (data-path-dependent), regional shapes (TOU regimes, IHD pairing, data-portability exports)

### L3 — Vendor-specific (research notes only)

- Opower: "neighbor comparison" against "similar homes"; Green Button download; guest user access; demand heatmaps/reactive power for business; behavioral load shaping "coach"; aggregate vendor statistics (TWh, reads) — claims, not repeated.
- Emporia: PowerSmart / ChargeBoost / Invite2Charge / Solar Window naming; NREL-based rate plans; Texas "Electricity Plans"; Emporia MCP server; brand-device ecosystem (Vue, smart plugs, home battery).
- Sense: "Always On" metric framing; device "signatures" learning narrative (days-to-weeks detection); Sense-enabled smart meter program; vendor statistic about Always On share of bills — claim, not repeated.
- Enphase: Storm Guard; Solar Offset / Grid Dependence / Energy Independence metrics; Enlighten installer portal split; panel-level microinverter monitoring; Enphase Assistant confirmation gating.

## Canonical Model

```text
The Customer's Premise (utility account / home / site — the energy user's own)
└── Energy flows made visible to the customer
    │   consumption over time (meter/monitor/plug data)
    │   + production, storage, grid exchange where present
    └── Rates/tariffs applied → cost and savings
    └── Insight machinery: comparisons, forecasts, alerts, tips, goals, device detail
        └── Action: behavior change · device control/automation ·
            rate/plan choice · program participation
```

Two poles realize the same model: the utility-provided pole (operator = utility; data = utility meter feed; action = insight + advice + program connection, control as separable sibling) and the customer-owned pole (operator = customer; data = own hardware or utility meter link; action = monitoring + direct control/automation). The operator flips; the model does not.

## Vendor-specific Findings

- Opower's deployment model (widgets/SSO/APIs embedded in utility websites) is product-specific; the underlying pattern — customer energy tools surfaced under utility branding — is the utility-pole norm.
- Sense's two data paths (utility smart meter program OR panel monitor) are directly documented and useful as the canonical statement that the data path does not change the Type.
- Emporia's "Homes" object (per-property grouping of devices, rates, billing, sharing) is a clean consumer-pole realization of the premise object; the name is vendor vocabulary.
- Enphase's prosumer metrics (Solar Offset etc.) are vendor formulations of the production-aware variant.
- Business-customer energy self-service (demand heatmaps, reactive power insights, guest access, Green Button export) is documented only at Opower in this sample — flag as utility-pole-specific until another utility-pole source is examined.

## Boundary Findings

1. **vs Building Energy Management (§17, processed — flag from that pass DISCHARGED from this side).** BEM's user is an organization managing a portfolio of buildings (facility/energy manager as a job role); this Type's user is the energy customer managing their own premises' usage. Refinement recorded: the BEM pass phrased the seam as "consumer/home pole", but the utility pole demonstrably serves business customers (SMB/C&I) as well — so the load-bearing discriminator is the OPERATOR-OBJECT relation (own-premise self-management vs portfolio/facility management), not residentialness. Removal tests: strip the customer-as-operator (make the user an organization managing buildings) → BEM; strip portfolio/multi-building estate machinery → this Type. A commercial customer managing one site's own energy sits in this Type; the same customer running a multi-building estate with M&V workflows has crossed into BEM.
2. **vs AMI / MDMS (§19, processed — flag from AMI pass DISCHARGED from this side).** AMI is utility-side metering infrastructure; consumer-facing portals are optional extensions of AMI data. This Type consumes meter data with the customer as operator. Removal test: remove the customer-side operator and management loop → AMI/metering infrastructure.
3. **vs Utility Billing / Utility Customer Information System (§19, unprocessed).** Billing/CIS is the utility-side system of record for accounts, tariffs, and payment. Bill PAYMENT and billing transactions sit there (Opower explicitly splits "Digital Self Service - Transactions" from DSS-EM). This Type's bill involvement is insight: forecast, comparison, alignment, export. Test: remove usage insight/management → bill-pay portal (billing's customer surface); remove billing transactions → this Type stands.
4. **vs Demand Response Platform (§19, unprocessed).** DR platform = utility/program-side event and program machinery. This Type carries the customer-facing participation experience (event alerts, enrollment, behavioral load shifting) as a capability or adjacent service, not the program engine. Pure consumer-DR apps (curtailment events + rewards as the whole product) are a drift pole of this Type toward the DR seam; record for joint review when Demand Response Platform is processed.
5. **vs smart-home / thermostat apps (no directory leaf).** Comfort-centric device control is not energy management. The energy framing (usage, cost, savings, tariffs) is the discriminator. Energy apps adding device control are variants of this Type; comfort apps adding energy views are smart-home products with an energy feature. The action leg alone (control without usage visibility/insight) fails L0 property 2.
6. **vs solar/DER monitoring apps (no directory leaf).** Production-first monitoring for system owners (array health, panel-level output) is device/system monitoring. When production integrates into the household's energy decisions (self-consumption optimization, storage dispatch, import/export management beside consumption), it is this Type's prosumer pole (Enphase realization). Production-only monitoring remains adjacent.
7. **vs EV Charging Network Management (§19, unprocessed).** Network/charging-station operations vs home charging as one managed load within the household's energy picture. An EV charger app that only manages charging is the sibling Type's surface; EV charging absorbed into tariff-aware home energy optimization is this Type.
8. **vs Personal Finance Management / bill trackers (§08, processed).** PFM records money movements; this Type manages energy usage with cost as one derived view. A bill snapshot inside a PFM is not energy management.

## Uncertainties

- No second utility-pole vendor was directly reachable (Uplight 403, NISC timeout, Bidgely/Grid4C thin) — utility-pole specific claims (guest access, Green Button export, neighbor comparison mechanics, business insights) rest on one vendor and are flagged accordingly; the utility-pole existence itself is corroborated by the AMI pass's recorded observation of consumer portals as an AMI extension market.
- Whether program participation (DR/TOU enrollment) reaches deeper than "promote + enroll" inside utility-pole customer tools could not be verified beyond product-page framing (separate sibling services exist for behavioral DR and device control, which supports the separable reading).
- The exact split between "insight widgets embedded in utility websites" vs standalone web apps per utility could not be fully documented; deployment flexibility is documented, canonical form treated as "customer-facing energy experience under the energy seller's brand or the customer's own product".
- Regional products (UK IHD ecosystems, EU supplier apps, Japan HEMS) were not fetched; the historical/regional check for them rests on the monthly-read-era argument rather than direct observation — assertion strength for regional variants kept low.

## Final Synthesis

Customer Energy Management is the customer-side application Type of the energy domain: software through which the user of energy — a household or a business customer — observes, understands, and acts on their own premises' energy usage and cost. Its defining core is three properties: customer-side operation on one's own energy; the premise's usage made visible to the customer as data over time; and an insight → action loop that turns usage into cost, comparisons, forecasts, anomalies, advice, and goals that drive customer action. Everything else — real-time data, AMI feeds, device control, solar/storage integration, neighbor comparison, AI assistants, bill payment, business-customer tooling — is common mature structure or variant, not definition. Two operator poles (utility-provided white-label engagement vs customer-owned products) realize the same model with the operator flipped. The seams: BEM manages buildings as an organization's portfolio; AMI/MDMS collect the data utility-side; billing owns the money; demand response owns the program; smart home owns comfort; solar monitoring owns the array. This Type owns the customer's own energy picture.
