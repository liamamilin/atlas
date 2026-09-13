# Research Notes — Utility Rate Management

Research date: 2026-09-10

## Research Goal

Understand what "Utility Rate Management" actually is from real products: what object a "rate"/"tariff" is in these systems, what designing / managing / analyzing rates concretely means, how the work relates to the billing system that executes rates, and where the boundaries run — especially against the processed sibling **Utility Billing Platform** (which pre-hung this leaf as "adjacent layer — rate design, modeling, and analysis; here rates are *executed* inside the bill cycle"), and against the customer-side and data-side neighbors (Customer Energy Management, tariff-data APIs).

## Initial Boundary

Hypothesis before research:

- The leaf sits in §19 between "Utility Billing Platform" (processed 2026-09-10) and "Utility Revenue Assurance" (unprocessed). The billing pass explicitly reserved this leaf for the rate design/modeling/analysis layer.
- Working hypothesis: Utility Rate Management = the system layer that holds the utility's retail rate structures (tariffs) as managed data, computes what bills *would be* under those rates, and runs the design/analysis loop (model proposed rates, compare, quantify bill/revenue/customer impacts) that decides which rates exist — as opposed to the billing platform, which *executes* the chosen rates in production bills.
- Suspected second pole: tariff-data platforms (collecting and normalizing tariffs across many utilities and serving them to third parties — solar, suppliers, enterprises). Suspected adjacent poles: customer-facing rate engines (Opower-style), utility-data-collection APIs where tariff is just metadata.
- Suspected risks: (a) collapse into the billing platform's rate-configuration table (must show what the standalone analysis layer adds); (b) confusion with wholesale energy trading (market prices vs retail tariffs); (c) confusion with customer energy management (customer-facing cost insights); (d) the leaf name "rate management" is also used in billing marketing for mere rate configuration — must not let the execution pole swallow the leaf.

## Research Questions

1. What is the rate/tariff as an object of record — what components (charges, tiers, TOU periods, demand, riders, taxes), what structure, what versioning/effective-dating, what lifecycle states?
2. What does "rate design" concretely mean in products (build tariff structures, cost-of-service inputs, revenue requirement, bill impact)?
3. What does rate analysis concretely mean (bill simulation, full-population impact, winners/losers, what-if load, rate switching/optimization, rate case filings)?
4. What is the calculation engine — what inputs (consumption, demand, interval data, applicability properties), what outputs (line items, accuracy), what fidelity grades (billing-grade vs analytical)?
5. How does the system relate to billing (export rates to CIS? add-on billing engine? trigger calculation externally?) and where exactly is the execution/analysis seam?
6. Who are the users (rate designers, regulatory teams, billing config teams, suppliers, solar companies, enterprises)?
7. Is there a tariff-data-aggregation pole (cross-utility library, change tracking, API distribution)? What does it share with the utility-side pole?
8. How does the regulatory dimension appear (rate cases, proposed/approved states, closed/grandfathered tariffs)?
9. Where do the boundaries run: vs billing, CIS, customer energy management, revenue assurance, energy trading, telecom product catalog, generic pricing, data-collection APIs?

## Representative Products

Chosen for market representation + documentation accessibility + different product philosophies + different customer tiers:

| Product | Vendor | Pole | Evidence depth |
|---|---|---|---|
| GridX Enterprise Rate & Data Platform (Design / Analyze / Calculate) | GridX | standalone utility-side rate design & analytics specialist | A — multiple product pages fetched verbatim |
| Oracle Utilities Rate Cloud Service + Billing Cloud Service (+ Opower Rate Engine as boundary) | Oracle | enterprise-suite pole: rate calculation extracted from CIS; rate management inside billing | A — official docs pages fetched verbatim |
| Arcadia (Signal tariff database & calculation engine; Switch APIs; Rate Monitoring & Optimization) | Arcadia | cross-utility tariff-data platform pole | A — product pages + developer docs fetched verbatim |
| UtilityAPI | UtilityAPI | boundary specimen: utility-data collection where tariff is metadata | A — docs/terminology fetched verbatim |
| NREL/OpenEI Utility Rate Database (URDB) | National Laboratory of the Rockies (public) | public-infrastructure corroboration of the tariff-estate concept | A — wiki page fetched verbatim |

## Sources

- GridX — homepage: https://gridx.com/ ; Rate Design & Analytics: https://gridx.com/rate-design-analytics/ ; GridX Design: https://gridx.com/design/ ; GridX Analyze: https://gridx.com/analyze/ ; GridX Platform (Enterprise Rate Engine): https://gridx.com/gridx-enterprise-rate-platform-2/ ; Design onesheet PDF: https://20562761.fs1.hubspotusercontent-na1.net/hubfs/20562761/Product%20One%20Sheets/GridX-Design-Onesheet-2024.pdf (all fetched 2026-09-10)
- Oracle Utilities Rate Cloud Service — Get Started: https://docs.oracle.com/en/industries/utilities/rate-cloud/index.html ; Rates introduction: https://docs.oracle.com/en/industries/utilities/rate-cloud/264/rcs-user-guides/Topics/C1_BP14_Rates_Rates_Introduction.html ; RCS chapter: .../Topics/X1_BP96RateCloudService_RateCloudService.html ; RCS Overview: .../Topics/X1_BP96RateCloudService_Overview.html ; Using Rate Check: .../Topics/X1_BP96RateCloudService_UsingRateCheckWithRateCloudService.html ; Oracle Utilities Billing Cloud Service product page: https://www.oracle.com/europe/utilities/products/billing-cloud-service/ ; Opower Rate Engine: https://docs.oracle.com/en/industries/energy-water/energy-efficiency/energy-efficiency-overview/Content/Rate_Engine.htm ; Rates Modeling: https://docs.oracle.com/en/industries/utilities/rates-engagement/rates-engagement-overview/rates-modeling.html (all fetched 2026-09-10)
- Arcadia — Tariff & Energy Rate Calculator (Signal): https://www.arcadia.com/platform/tariff-energy-rate-calculator ; Rate Monitoring & Optimization: https://www.arcadia.com/rate-monitoring-optimization ; Switch docs — Tariff APIs overview: https://docs.arcadia.com/v2022-12-21-Switch/reference/tariff-apis ; Account Tariffs API: https://docs.arcadia.com/v2022-12-21-Switch/reference/account-tariffs-api ; Account Rates API: https://docs.arcadia.com/v2022-12-21-Switch/reference/account-rates ; Account Cost Calculation: https://docs.arcadia.com/v2022-12-21-Switch/reference/account-cost-calculation.md ; Tariff History API: https://docs.arcadia.com/v2022-12-21-Switch/reference/tariff-history-api.md ; Select the Right Utility and Tariff: https://docs.arcadia.com/v2022-12-21-Switch/docs/select-the-right-utility-and-tariff (all fetched 2026-09-10)
- UtilityAPI — Terminology: https://utilityapi.com/docs/terminology ; API docs: https://utilityapi.com/docs/api ; Utility Data Service: https://utilityapi.com/products/uds (all fetched 2026-09-10)
- NREL/OpenEI — Utility Rate Database: https://openei.org/wiki/Utility_Rate_Database (fetched 2026-09-10)

**Source-access limitation**: SAP's utilities rate-design tooling was not researched this pass (Oracle covers the enterprise-suite pole with directly fetchable official docs); no claims about SAP are made. Water-utility rate design depth was not separately verified — the sample is electricity-dominant (with gas and solar-PV service types documented at Arcadia); commodity breadth is asserted only at that strength. All four commercial samples were directly reachable; no evidence downgrade was needed.

## Product A — GridX (Enterprise Rate & Data Platform)

### Key observations (Layer A — directly observed)

- Positioning (verbatim): "The GridX Enterprise Rate & Data Platform manages the end-to-end rate and program lifecycle. Powered by the industry's leading Rate Engine, GridX delivers solutions for forecasting, designing, measuring, implementing, and billing advanced rates and programs."
- Product taxonomy (the vendor's own decomposition of the Type): **Forecast** ("Organize and plan around your data"), **Design** ("Design any rate or tariff imaginable"), **Analyze** ("Run billing quality analytics for every customer"), **Empower** ("Communicate highly accurate cost data through APIs"), **Explore** ("Visualize and bundle clean energy options"), **Advise** ("Get your business customers on the right rate"), **Calculate** ("Bill complex rates in your existing CIS").
- **Digitized rates** (verbatim): "The single source of rates truth. Digitizing a rate means its DNA is componentized, shareable and reusable."
- **Rate modeling** (verbatim): "Test rates with real customer data to understand exactly how a new rate or program will impact individual customers or segments." Design page: "Easily design any rate or tariff structure imaginable, including Time-of-Use (TOU), real-time pricing, and dynamic rates"; "Quickly iterate on new tariffs by copying over existing ones and adjusting criteria to meet new requirements"; "Changes to the model are instantly reflected in accounts so users can quickly see the impact and make adjustments as needed."
- **Rates sourced from billing** (verbatim): "Leverage rate and tariff definitions and their associated price tables, which were previously only available in the billing system, to easily modify rate parameters and analyze the impact across customers." And: "Create a single source-of-truth for rate calculations using CIS data."
- **Cost-of-service input to design** (verbatim): "Calculate proposed pricing based on user-input cost of service and calculation rules, allowing rapid development based on changing scenarios."
- **Population impact analysis** (verbatim): "Conduct full population analysis of proposed rates and programs to ensure customers or segments aren't impacted in unexpected ways, e.g. identify winners and losers." "Identify how a proposed rate change will impact each and every one of your customers to ensure none are unfairly impacted and nobody suffers rate shock."
- **What-if load modification** (verbatim): "Modify load in real time to answer what-if rate and cost questions regarding behavior change and behind-the-meter technologies like solar, EVs, heat pumps, and battery storage."
- **Rate case filings** (Analyze page, verbatim): "GridX Analyze is the premier solution for building accurate and auditable rate case filings." "Generate Robust Data for Filings — Perform full-population analysis and simulate various scenarios, providing the comprehensive, auditable data needed for regulatory submissions." "Understand the revenue implications of new rates and programs across the full population."
- **Billing-grade computation** (verbatim): "penny-level accuracy"; "Run full-population, billing quality analytics"; platform stats: "33m Meters under contract", "500 Tariffs modeled", "49m Bills calculated daily".
- **Execution seam** (verbatim): "Simplify the journey of implementing and billing advanced rates, like time-varying rates (TVRs), with an add-on billing engine that enhances and complements the existing CIS." — i.e., the same platform optionally extends into billing execution; the analysis platform is the core, billing an add-on.
- **Anti-spreadsheet framing** (verbatim): "Unlike traditional methods that rely on manual spreadsheets and disconnected data, GridX Design offers a single, cloud-native platform for designing, modeling, and analyzing rates." — the displaced baseline is the spreadsheet-era rate office.
- APIs named on the Model page: iCost ("Costing at the interval and daily levels... such as demand charges"), compareResult ("Monthly rate analysis results... per scenario"), compareCalculate ("Real-time rate analysis calculation with the ability to apply modifiers to simulate behavior changes").

## Product B — Oracle Utilities (Rate Cloud Service / Billing Cloud Service / Opower Rate Engine)

### Key observations (Layer A — directly observed)

- **Rate Cloud Service definition** (verbatim): "Oracle Utilities Rate Cloud Service provides access to the rate calculation functionality of Oracle Utilities Customer Cloud Service. This includes the ability to configure and test rate calculations via the user interface, as well as the ability to trigger the rate calculation process from an external system." Scope note (verbatim): "supports rate calculation for traditional scalar or volume-based billing quantities only. It does not include capabilities for generating billing determinants from interval data input."
- **The rate as configuration object** (Rates chapter, verbatim): "The most important information specified on a service agreement is the rate. The rate controls: How the service's charges are calculated. How the charges are described on the customer's bills. How the general ledger is affected by the charges." Also: rates can calculate adjustments; the SA Type controls which rates may be used.
- **Rate structure flexibility** (verbatim): "Do not equate a rate in your legacy system with a rate in this system... your current rate structure may have three rates for service because there are different prices based on the customer's geographic area. In this system, however, you can set up a single rate and vary the price based on where the customer lives." Two engine generations documented: "Calculation Rule-Based Rates" (current) vs "Component-Based Rates" (classic, not recommended for new implementations).
- **Rate Check = the test harness** (verbatim): "In addition to rate configuration functionality, Oracle Utilities Rate Cloud Service includes access to the Rate Check feature, which allows users to test their rates. When using Rate Check, service quantities and characteristic types/values must be provided by the user and entered via the user interface." — i.e., configure + test with user-supplied quantities, deliberately decoupled from production service agreements/bill segments.
- **Billing Cloud Service marketing of the same machinery** (verbatim): "Get end-to-end rate management, usage and charge calculations, and bill preparation"; "A dynamic rate engine — Support a wide range of simple to complex scenarios, including volume-based rates, time-of-use (TOU) pricing, dynamic real-time pricing, net metering, unbundling of charges, proration, rate comparison, and pass-through rates"; "precise multiple-decimal values, effective-dating, and usage and charges proration"; "Streamline rate changes from months to minutes with point-and-click configuration and built-in rates testing. Prebuilt calculation rules for simple-to-complex rates and copy-merge features make it easy to create new rates without coding."
- **Boundary specimen — Opower Rate Engine** (verbatim): "The Oracle Utilities Opower Rate Engine is a computing model that relies on rate configuration data, rate plan data, and customer energy use data as its primary inputs... Note that the Rate Engine is not designed to be a billing-grade engine. Its purpose is to convert customer energy use values to dollar values, and to then deliver estimated cost insights and trends based on those dollar values." Rates Modeling doc: generic rate calculators for "tiered rate plans, time-of-use rate plans, and flat charges"; custom calculators when needed; setup is a vendor-delivered "rates modeling" service.

## Product C — Arcadia (Signal / Switch / Rate Monitoring & Optimization)

### Key observations (Layer A — directly observed)

- **Tariff database positioning** (verbatim): "Signal collects, models, and maintains rates across 25K+ North American tariffs with automatic tracking and aggregation of all rate changes." "Signal APIs accurately calculate the cost of every energy usage scenario against North American tariffs." Rate Monitoring page: "database of 30,000+ North American tariffs", "70K rate updates per month".
- **The tariff data model** (Tariff APIs overview, verbatim): "Tariff data is connected to utilities, service territories, seasonal schedules, time-of-use periods, calendars, applicability properties, and tariff revision history." API set: Tariffs, Load Serving Entities, Territories, Seasons, Time of Uses, Calendars, Properties, **Tariff History**.
- **Versioning machinery** (Tariff History, verbatim): "Tariff history gives you the complete revision history for a tariff family, identified by `masterTariffId`... when tariff rates changed, when attached riders were versioned, and when variable pricing indexes associated with the tariff changed." "Tariff rates are rates specific to the tariff. They change when the utility issues a new tariff document. Rider rates are rates that can be shared across multiple tariffs within the same utility... Lookups are frequently changing rates recorded as price schedules, such as Fuel Cost Adjustments."
- **Lifecycle states** (verbatim): `customerClass` includes `PROPOSED` — "Utility rates that have been proposed by utilities and approved by utility commissions, but are not yet effective"; `closedDate` — "Date on which a tariff became closed to new customers, but still available for customers who were on it at the time" (grandfathering); tariff filtering guidance: pass `openOn` to "filter out tariffs that are closed to new enrollment... Don't filter on this property if your use case is to select the existing tariff a customer is on, as they might be grandfathered into a closed tariff."
- **Calculation engine** (Account Cost Calculation, verbatim): "To run a calculation, provide the tariff to use and the inputs that drive the rates. These inputs typically include consumption in kilowatt-hours (kWh), but can also include... demand (kW), applicability criteria... quantity of other items." "Passing an hourly load profile produces more accurate calculations than passing aggregate monthly consumption." Output: `CalculatedCost` with per-rate line items (`CalculatedCostItem`: rateGroupName, rateName, quantityKey fixed/consumption/minimum/demand, rateType COST_PER_UNIT/PERCENTAGE/BLOCK, tier limits, chargeType, chargeClass TRANSMISSION/DISTRIBUTION/SUPPLY/TAX, TOU period, season), an explicit `accuracy` field ("As more 'best guess' assumptions are made, the calculation will become less accurate"), and an `assumptions` list.
- **Version pinning and rate modeling** (verbatim): `tariffEffectiveOn` — "This field enables doing a calculation with a single, specified version of a given tariff. For example... the 2016-01-01 version of PG&E's E-1 tariff"; `rateInputs` — "The rate input values are used to override existing rates on the tariff during the calculation. This enables modeling and/or setting customer-specific rates during a calculation."
- **Account tariff assignment** (Account Tariffs API, verbatim): "An account tariff is similar to the Tariff object, but it represents the tariff assignment for a specific account." "To store multiple tariffs, set an `effectiveDate` for each account tariff. Account calculations use the account tariffs and their effective dates to determine which tariff applies to the calculation period." "When switching an account from one tariff to another at a specific point in time, set `effectiveDate`. Switch checks for overlapping effective ranges and returns an error if one exists."
- **Analysis loop** (verbatim): "Use the Account Cost Calculation API to reproduce a customer's utility bill, compare the result, and calibrate calculation inputs" (bill matching); Analysis APIs "to compare multiple scenarios and calculate forecasted savings"; Savings Analysis workflow "compare before, after, and solar scenarios".
- **Rate optimization as a service** (Rate Monitoring & Optimization, verbatim): "Using Arcadia's high-accuracy bill simulation engine and database of 30,000+ North American tariffs, we model every meter against every applicable tariff to identify the optimal choice." "Arcadia's industry-leading tariff calculator quantifies the cost impact of switching, so every decision is backed by accurate financial analysis." "Utility rates are revised regularly... Regular audits ensure every meter stays on its optimal rate as conditions evolve." "When optimization opportunities are identified, Arcadia manages the rate transition with the utility on your behalf."
- **Tariff selection mechanics** (verbatim): "We collect utility and tariff data across the USA, Canada, and Mexico... We maintain data on which utilities operate in which locations... We also track all the tariff rate plans that a utility has, including how many customers are on that plan and whether it's the default option." Characteristic filters: hasNetMetering, hasTimeOfUseRates, hasTieredRates, hasContractedRates.

## Product D — UtilityAPI (boundary specimen)

### Key observations (Layer A — directly observed)

- Center of gravity is **customer-authorized utility data collection**: Authorizations, Meters ("the utility services for an authorized utility customer"), Bills, Intervals, Accounting endpoints.
- **Tariff as metadata, not estate** (Terminology, verbatim): "Tariff — The utility rate schedule that a utility service is on. This is a piece of information we include when collecting utility data, but it can be called 'rate' or 'rate schedule'. We are going to always refer to it as `service_tariff` and avoid using the term 'rate' to avoid confusion."
- Bills carry structured line items (tiers with rates/volumes, taxes) and the observed `service_tariff` name; per-utility docs list "the tariffs you will likely see" and are "updated regularly as we see new tariffs" — an observed-tariff census, not a modeled tariff library.
- No calculation engine, no rate design, no scenario analysis in the fetched docs; downstream tools (e.g., Energy Toolbase integration) do the rate comparison using collected interval data.
- Reading: this pole shares the *vocabulary* (tariff/rate schedule) but not the *structure* — it is the data-collection layer adjacent to rate management, exactly as MDMS is adjacent to billing.

## Product E — NREL/OpenEI Utility Rate Database (public corroboration)

### Key observations (Layer A — directly observed)

- "The Utility Rate Database (URDB) is a free storehouse of rate structure information from utilities in the United States" — "rate structure information for over 3,700 U.S. utilities"; rates "checked and updated annually"; "Each record indicates the date of the last update."
- Structure vocabulary (verbatim, via SAM integration note): "complex rate structures that include time-of-use rates, demand charges, tiered rates, fixed monthly fees, adjustment riders, and separate buy and sell rates."
- Distribution: bulk download (csv/json), web interface, API — "The URDB allows anyone to access these rates via bulk download, web interface, or computer-readable Application Programming Interface (API) for use in their tools and models."
- Approval state: "Download all **approved** U.S. rates" — records carry an approval state.
- Industry pain point (verbatim): "NLR has formed working groups with utilities and industry to explore options for adopting a standard machine-readable format that utilities could use to publish their rates" — corroborates that tariff digitization/currency is the core operational burden of the whole category.

## Cross-product Comparison

| Structure | GridX | Oracle (RCS/BCS) | Arcadia | UtilityAPI | URDB |
|---|---|---|---|---|---|
| Tariff/rate as structured versioned artifact | "Digitized rates... componentized, shareable and reusable"; tariff modeling incl. TOU/RTP/dynamic; copy-and-iterate | Rate as configuration object (charges, bill description, GL); rule-based rate engine; effective-dating (BCS) | Tariff family + versions + riders + lookups + effective ranges + closedDate + PROPOSED class | tariff as observed `service_tariff` name only | rate-structure records with effective dates, approval state, last-update date |
| Charge computation from consumption | Rate Engine, "penny-accurate", "billing quality", 49m bills/day | Rate calculation; Rate Check test harness (user-supplied quantities); scalar/volume only | Account Cost Calculation: tariff × inputs → line items + accuracy + assumptions; version pinning; rate overrides | none (collects bills) | none (data + API; SAM computes) |
| Analysis/design loop | Design (model, bill impacts, winners/losers, what-if load, cost-of-service input); Analyze (full-population, revenue, rate case filings) | configure + test (Rate Check); BCS: rate comparison, built-in rates testing, copy-merge | Savings Analysis (scenario comparison), bill matching, portfolio rate optimization + switch management | none | community studies built on the data |
| Who holds the estate | the utility's own rates (sourced from CIS/billing) | the utility's own rates (inside its CIS/billing) | cross-utility library (25K–30K+ tariffs, North America) | per-utility observed tariffs (as data) | public cross-utility library |
| Output target | billing (add-on engine), CX APIs, rate cases | billing execution (BCS) or external triggering (RCS) | third-party products' cost/savings analyses; portfolio optimization | downstream tools | analysis community (SAM etc.) |

Reading: three structures recur across every genuine rate-management product — (1) the tariff as structured, versioned data; (2) computation of charges from consumption under a tariff; (3) the comparative analysis loop. The poles differ in *whose* tariffs are held (own vs cross-utility), the *grade* of computation (billing-grade vs analytical), and *which* analysis the loop serves (design new rates vs select/optimize existing rates). UtilityAPI fails legs 2–3 and is thereby excluded from the Type — the cleanest boundary specimen in the sample.

## Canonical Model (L0–L3)

### L0 — Defining Invariant

Three jointly-held structures over retail utility tariffs:

1. **The tariff/rate schedule as a structured, versioned artifact of record** — the retail rate structure held as machine-readable data: charge components (fixed, volumetric, tiered, time-of-use, demand, riders/adjustments, taxes), applicability rules, and effective-dated versions/revision history. Remove → scattered tariff documents and spreadsheets; no managed rate estate.
2. **Tariff-driven charge computation** — a calculation engine that applies a tariff to consumption/load inputs and produces bill-level charges with line-item detail. Remove → a tariff library nobody can calculate with (a document archive).
3. **The analysis loop over the tariff estate** — computation used comparatively: model proposed/alternative rate structures, compare tariffs, quantify bill/revenue/customer impacts, iterate. Remove → rate configuration inside a billing engine only (execution without analysis = the billing platform's rate table), or a tariff data feed nobody analyzes.

Binding condition: the objects are **retail tariffs for metered utility service** — consumption-priced, regulated-context structures — not wholesale market prices, not commercial product/offer catalogs.

Jointly-held load-bearing checks:
- 1 alone = tariff document archive / rate book (paper era satisfies in paper form).
- 2 alone = a rate calculator / billing engine's rating step.
- 3 without 1+2 = a consulting study.
- 1+2 without 3 = billing platform's rate configuration (execution only).
- 1+3 without 2 = manual analysis with no engine (spreadsheet-era rate office — the displaced baseline).
- 2+3 without 1 = ad-hoc calculations with no managed estate.

### L1 — Common Mature Structure

- Full-population bill/revenue impact analysis ("winners and losers", rate-shock detection) — GridX, implied by Arcadia portfolio optimization
- Rate case / regulatory filing support (auditable, defensible scenario data) — GridX verbatim; Arcadia PROPOSED class corroborates the regulatory lifecycle
- What-if load modification (EV, solar, heat pumps, storage, behavior change) — GridX verbatim; Arcadia scenario/savings analyses
- Rate switching / enrollment analysis (which rate should a customer be on; grandfathering awareness) — Arcadia verbatim; GridX Advise
- Cost-of-service / pricing inputs feeding rate design — GridX verbatim
- Single source of truth for rates shared across departments (anti-spreadsheet framing) — GridX verbatim; Oracle "single rate... vary the price"
- APIs exposing rate data and calculations to surrounding systems — GridX Empower, Arcadia Signal/Switch, Oracle RCS external triggering
- Copy/iterate/version discipline on tariff structures — GridX, Oracle copy-merge, Arcadia tariff history
- Change tracking of externally-issued tariff revisions (riders, lookups, fuel adjustments) — Arcadia verbatim; URDB annual updates

### L2 — Variant / Optional Structure

- **Estate ownership**: the utility's own rates (GridX, Oracle) vs a cross-utility library (Arcadia, URDB)
- **Computation grade**: billing-grade (GridX "penny-accurate", Oracle BCS) vs analytical-grade with explicit accuracy/assumptions (Arcadia, Opower Rate Engine)
- **Design depth**: full rate design with cost-of-service inputs (GridX) vs analysis/optimization only (Arcadia)
- **Regulatory lifecycle depth**: proposed/approved/effective states, closed-to-new-enrollment grandfathering (Arcadia explicit; others implicit)
- **Commodity scope**: electricity-dominant sample; gas and solar-PV service types documented (Arcadia); water not separately verified
- **Data grain**: interval/AMI-driven analysis (GridX, Arcadia hourly) vs scalar/volume quantities (Oracle RCS explicitly scalar-only)
- **Delivery/packaging**: standalone platform (GridX), suite-extracted cloud service (Oracle RCS), inside-billing module (Oracle BCS), API-only data platform (Arcadia Switch), public database (URDB)

### L3 — Vendor-specific (Research Notes only)

- GridX product names (Forecast/Design/Analyze/Empower/Explore/Advise/Calculate), iCost/compareResult/compareCalculate APIs, "penny-level accuracy" guarantee, marketing stats (33m meters, 500 tariffs, 49m bills/day), "up to 5 accounts at a time" interactive-design limit
- Arcadia Signal/Switch names, masterTariffId/tariffId two-level versioning scheme, PropertyData/assumptions/accuracy model, intelligent baselining, Bill Solve, "70K rate updates per month", customerLikelihood defaulting
- Oracle Rate Cloud Service / Billing Cloud Service packaging, Calculation Rule-Based vs Component-Based engine generations, Rate Check UI constraints (no service agreements/bill segments/service points), Opower "rates modeling" delivery service
- URDB approval workflow, annual update cadence for ~150 utilities comprising 70% of US load, NLR machine-readable-format working groups

### Anti-overfitting checks

- **AMI/interval data is NOT definitional**: Oracle RCS explicitly scalar-only and still a rate product; the spreadsheet-era rate office ran the same loop on monthly data. Interval grain is the modern realization, not the invariant.
- **"Design" is NOT definitional**: Arcadia's core is analysis/optimization of existing tariffs, not designing new ones; the design leg is the utility-side pole's extension. The invariant is the *analysis loop*, of which design is one purpose.
- **Regulatory states are NOT definitional**: only Arcadia documents PROPOSED/closed states explicitly; GridX documents rate-case support as a capability. The regulatory context is the binding's backdrop, not a required object.
- **Cross-utility breadth is NOT definitional**: GridX/Oracle hold one utility's rates; Arcadia holds thousands. The invariant is the managed tariff estate, whatever its breadth.
- **Historical check (§24)**: the paper-era utility rate office — tariff sheets/books filed with the regulator, rate analysts computing sample bills by hand, designing new structures on paper, comparing old vs new for hearings — satisfies all three L0 legs in manual form. The 1990s CIS rate table + test-bill feature satisfies legs 1+2 with a minimal loop. The definition is era-neutral. Passed.

## Vendor-specific Findings

See L3. Additional notes:
- GridX's own framing locates the displaced baseline: "manual spreadsheets and disconnected data" — the category exists to replace the spreadsheet rate office.
- Oracle's two engine generations (Component-Based vs Calculation Rule-Based) show the rate engine itself has a migration lifecycle inside the enterprise suite.
- Arcadia's `customerLikelihood` field (defaulting a customer's tariff by probability) is a data-platform-specific mechanism with no utility-side analog in the sample.
- Opower's Rate Engine is the sampled vendor's own explicit statement of the customer-insight boundary: "not designed to be a billing-grade engine."

## Boundary Findings

1. **vs Utility Billing Platform** (the central seam, pre-hung by the billing pass): billing *executes* rates in production bills over service accounts; rate management *designs and analyzes* rates over the tariff estate. The seam is real but thin at the engine level: GridX sells Calculate as an "add-on billing engine that enhances and complements the existing CIS"; Oracle extracts Rate Cloud Service *from* Customer Cloud Service and sells Billing Cloud Service with "end-to-end rate management". Test: remove the analysis loop and the standalone estate → billing platform's rate configuration; remove the production bill/account machinery → rate management. Both vendors' packaging confirms the seam from both sides.
2. **vs Customer Energy Management**: customer-facing cost insights (Opower Rate Engine: convert usage to dollars for customer features; explicitly not billing-grade) vs analyst/operator-facing work over the tariff estate. GridX Empower/Advise extends toward this seam from the platform side (APIs delivering cost data; getting business customers on the right rate) — an extension, not the center.
3. **vs Utility Revenue Assurance**: revenue assurance audits *executed* bills for leakage; rate management works *upstream* of execution, on the structures and their impacts.
4. **vs Energy Trading Platform**: wholesale market prices/clearing vs retail tariff structures for metered service. (GridX Forecast's wholesale-settlement vocabulary marks the adjacent edge inside the platform pole.)
5. **vs utility-data-collection APIs (UtilityAPI)**: tariff as observed metadata on collected customer data vs tariff as the managed, modeled estate. UtilityAPI's own terminology page draws the line: tariff is "a piece of information we include when collecting utility data".
6. **vs Telecom Product Catalog / generic pricing (§05.14 Retail Pricing Management) / CPQ**: commercial offer catalogs and sales pricing vs regulated, consumption-priced tariff structures maintained under regulatory process and effective-dated by filing.
7. **vs Energy Forecasting Platform**: forecasting demand vs managing rate structures; forecasting appears inside rate platforms (GridX Forecast) as an adjacent capability.
8. **"去掉什么就变成另一个 Type" 判据**: remove the analysis/design loop → the rate table of a billing platform (Utility Billing territory). Remove the tariff estate and computation → a consulting study or a data feed (UtilityAPI/URDB territory). Remove the retail-tariff binding (regulated, consumption-priced) → generic pricing/product-catalog territory. Remove the operator/analyst seat → customer energy management.

## Uncertainties

- **Water/wastewater rate design depth** not separately verified; the sample is electricity-dominant (gas and solar-PV documented at Arcadia). Commodity breadth asserted only at that strength.
- **SAP's rate-design tooling** not researched; the enterprise-suite pole rests on Oracle alone. The suite-pole pattern (rate engine extracted as a service) is therefore single-vendor-supported at the packaging level and marked as such.
- **Rate-case workflow depth** (filing assembly, docket management) observed only as GridX marketing claims about "auditable rate case filings"; no docket-management machinery was documented. Rate-case support is asserted as a capability, not as a workflow structure.
- **Cost-of-service / revenue-requirement allocation depth**: GridX documents "user-input cost of service and calculation rules" as an input; no sampled product documents a full cost-of-service study engine. Deep ratemaking analytics may live in consulting tools not sampled here.
- **Non-US markets**: Arcadia covers USA/Canada/Mexico; URDB has international coverage; regulated-market structures outside North America (e.g., fully regulated European tariffs) were not separately sampled.

## Final Synthesis

Utility Rate Management is the utility sector's **rate-structure layer**: it holds retail tariffs as structured, versioned, effective-dated data of record; computes what bills cost under those tariffs from consumption inputs; and runs the comparative analysis loop — model proposed rates, compare alternatives, quantify bill/revenue/customer impacts — that decides which rates exist, which customers should be on which rate, and what to file with regulators. Its two market poles share this spine: the utility-side design & analysis platform (GridX; Oracle's suite-extracted Rate Cloud Service) works the utility's own rates and hands results to billing and the regulator; the cross-utility tariff-data platform (Arcadia; URDB as public analog) maintains a library of many utilities' tariffs and serves computation and optimization to third parties. The defining seam against billing is analysis vs execution; against customer energy management, the analyst seat vs the customer seat; against data-collection APIs, the modeled estate vs observed metadata. The core is era-neutral: the paper-era rate office with tariff books, hand-computed sample bills, and design comparisons satisfies the same three structures.
