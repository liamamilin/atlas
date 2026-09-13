# Research Notes — Demand Planning

## Research Goal

Understand what a Demand Planning application really is — as distinct from the sibling leaves Supply Planning and Supply Chain Planning Platform (both already processed), from Inventory Management System, from APS, and from Sales Forecasting Platform — and produce the canonical model: what exists inside the system, what users do with it, how the forecast work actually flows, which rules govern it, and where the Type boundary sits.

This pass also carries three pre-hung joint-review obligations from earlier passes:
1. the **supply-chain-planning-platform** pass flagged "platform vs demand-planning + supply-planning (capability slices or one family?)" for decision in the siblings' passes;
2. the **supply-planning** pass requested ratification of "produces the forecast vs consumes it" from the demand side;
3. the **advanced-planning-scheduling-aps** pass flagged the §10 sibling family with the structural test "finite-capacity operation-level time assignment".

## Initial Boundary

Working hypothesis before research:

- Core use: produce and maintain a forward forecast of product demand (what will be needed, where, when) that the organization plans supply against.
- Users: demand planners, forecast analysts, plus contributing functions (sales, marketing, operations) and S&OP participants.
- Nearest types: Supply Planning (consumes the forecast), Supply Chain Planning Platform (holds demand + supply + network model together), Inventory Management System (records what is), APS (finite-capacity scheduling), Sales Forecasting Platform (revenue projection from pipeline), Energy Forecasting Platform (same skeleton, different subject).
- Unknowns: is the accuracy-measurement loop definitional or merely common? Is multi-function consensus definitional? Is the demand-plan-of-record granular at item × location always? How do SMB products differ structurally (not just in scale)?

## Research Questions

1. What is the central object — a "forecast of record"? At what granularity is it held (item × location × time bucket)?
2. How is the baseline forecast generated? (statistical models, ML, model selection/back-testing, history cleaning)
3. What do planners actually do to the forecast? (adjust, freeze/protect, revert, correct events, approve)
4. How do other functions participate? (consensus, S&OP, forecast value-add)
5. How is forecast accuracy measured and fed back? (forecast history, error/bias, per level/vintage)
6. What demand streams compose the total forecast (sales, distribution, BOM)?
7. What consumes the forecast (replenishment, supply planning, MRP, financial alignment) — and is consumption part of this Type?
8. What varies by segment/industry? (granularity, demand sensing, probabilistic forecasting, NPI handling)

## Representative Products

Chosen for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Evidence strength |
|---|---|---|
| Kinaxis (Maestro / RapidResponse) | enterprise concurrent-planning platform; consensus-collaboration emphasis | A (solution page) |
| SAP Integrated Business Planning — Demand Planning | ERP-suite IBP module; AI+time-series automation emphasis | A (features page) |
| Blue Yonder Demand Planning | enterprise specialist heritage (JDA); glass-box / causal-transparency emphasis | A (product page; detailed help docs not fetched) |
| RELEX Solutions | retail/CPG high-granularity pole; ML automation + planner correction | A (solution page + official guide) |
| Netstock | SMB ERP-companion pole | A — Tier 1 operational help center |
| GMDH Streamline | standalone SMB/mid statistical forecasting specialist | A (vendor site + docs index; webhelp not fetched) |

## Sources

Fetched 2026-09-08:

- Kinaxis — Demand Planning solution page — https://www.kinaxis.com/en/solutions/demand-planning
- SAP — Integrated Business Planning, Demand Planning features — https://www.sap.com/products/scm/integrated-business-planning/features/demand-planning.html
- Blue Yonder — Demand Planning solution page — https://www.blueyonder.com/solutions/supply-chain-planning/demand-planning (first URL /solutions/demand-planning 404; second path succeeded)
- RELEX — Demand planning software solution page — https://www.relexsolutions.com/solutions/demand-planning-software/ (first URL /solutions/demand-forecasting/ 404) and official guide "Demand forecasting for retail and consumer goods" — https://www.relexsolutions.com/resources/demand-forecasting/
- Netstock Help Center (Tier 1) — https://help.netstock.com/en/ ; Forecasting collection — https://help.netstock.com/en/collections/18733700-forecasting ; "Mastering Forecasting" — https://help.netstock.com/en/articles/12528486-mastering-forecasting ; "Demand Types & Sales Forecast Generation Explained" — https://help.netstock.com/en/articles/12528487-demand-types-sales-forecast-generation-explained
- GMDH Streamline — "Demand Forecasting" page — https://gmdhsoftware.com/demand-forecasting/ (webhelp at docs.streamlineplan.com listed but not fetched)

Internal cross-references (prior passes, same pack): research/applications for supply-chain-planning-platform, supply-planning, inventory-management-system, advanced-planning-scheduling-aps, sales-forecasting-platform.

Source-access limitations: no vendor's full user manual was fetched. Netstock's help center is the only Tier-1 operational documentation; Kinaxis knowledge base is login-gated, SAP Help Portal is a known JS shell (per ERP/SCP passes), Blue Yonder docs portal not attempted after product page, Streamline webhelp not fetched. All enterprise mechanics are therefore asserted at process level from official product/solution pages, and no numeric limits, defaults, algorithm parameters, or UI-level claims are made for enterprise vendors.

## Product Observations

### Kinaxis — evidence layer A (demand planning solution page), positioning

- Demand planning presented as "collaborative demand planning and advanced analytics"; "drive consensus".
- Forecast accuracy "across all time horizons, with the right combination of advanced techniques and machine learning".
- Demand sensing: "Incorporate dynamic external signals — such as weather, social media, or a shift in consumer behavior".
- "Pinpoint demand at risk and make order fulfillment decisions" — forecast connected to fulfillment decision support.
- "Effortlessly gather demand input from all key stakeholders to create a fully transparent consensus plan".
- Forecast explainability: "understand and explain which data drive the greatest impact on your forecasts".
- Segmentation strategy applied to automate forecasts.
- Solution sits beside Supply, S&OP, Inventory, Scheduling, Order Management on one platform (nav).

### SAP Integrated Business Planning (Demand Planning) — evidence layer A (features page), positioning + capability vocabulary

- "Start with a highly accurate, AI-driven forecast. Combine AI and traditional time-series algorithms."
- Demand drivers: "Automatically calculate the effects of both external and internal demand drivers on the forecast… Planners can determine which demand drivers are correlated and have the largest impact."
- AI-assisted forecast results analysis: planners "see what algorithms were used" and get "suggestions for improvements".
- Collaboration: "Coordinated feedback from multiple groups" — input from "sales, marketing, and demand planning teams".
- Post-planning intelligence: "Use forecast-value-add analysis to determine which inputs lead to more accurate demand plans" — accuracy accountability for human inputs.
- Demand sensing: "AI automatically adjusts the short-term forecast based on real-time order patterns and downstream demand signals (such as point-of-sale data)".
- Automated statistical forecasting: "AI-based history classification, outlier detection and correction, and best-fit forecast algorithm selection".
- New products: "forecasting without any history using representative products to generate synthetic history or curves mined from history".
- Demand Planning is one module of IBP beside S&OP, Inventory planning, Response & Supply, Control Tower.

### Blue Yonder Demand Planning — evidence layer A (product page; product-page strength)

- "Demand forecasting" (statistical methods + machine learning + AI, demand sensing).
- "Consensus demand planning" as a named capability; "integrating inputs from sales, marketing, and operations into a unified process".
- "Greater demand transparency — glass box approach to understand underlying causal factors of demand".
- "Outside-in forecasting": processing "hundreds of internal and external signals to arrive at unbiased predictions".
- Pairing with supply planning: "Harmonize decision-making when demand and supply planning are one" — separate but paired products.
- Persona page "Demand Planner": "Gain accurate forecasts to ensure the right products are available at the right time, minimizing stockouts and overstock" — the user's job framed as availability vs stock.
- Vendor outcome claims (12% accuracy, 75% planner efficiency, etc.) — marketing claims, not operational evidence; excluded from canonical doc.

### RELEX Solutions — evidence layer A (solution page + official guide), retail/CPG pole

- Solution page key features: "Automated demand forecasting combines with exception-based and collaborative demand planning workflows to better manage new product introductions, seasons, promotions, and forecast discrepancies."
- ML predicts impact of "all relevant demand drivers, including merchandising decisions, internal commercial decisions, external events, consumer preferences, and seasonality".
- "The RELEX user interface makes it easy for users to manually correct forecasts, with clear dashboards at different levels… forecast visualizations that show how different demand factors impact forecasts."
- Probabilistic planning as an option: "Probabilistic AI-based modeling ensures uncertainty in supply and demand is translated into automated, and transparent actions."
- Official guide (resources/demand-forecasting): demand forecasting defined as evaluating "historical demand patterns, internal business decisions, and external factors" to predict future demand.
- Granularity doctrine: forecasts "at different levels of granularity—monthly, weekly, daily, or even hourly"; granular product-location-day forecasts; "flexible data pooling across products or over different planning horizons" so one forecast serves replenishment, capacity, workforce, markdowns, planograms.
- Composition: granular forecasts let a manufacturer aggregate products sharing a raw material to reveal material needs.
- Internal decisions modeled: promotions, marketing, display, price elasticity, cannibalization, visibility/placement.
- External factors: weather forecasts, local events, competitor pricing, retailer data (POS, promotions, assortment) for CPG.
- NPI: reference products selected by attributes automatically; forecasts update as actuals emerge.
- Omnichannel: separate forecasts per sales/fulfillment channel.
- Accuracy: "accuracy is always important but should be analyzed on different levels… evaluated for different periods and levels of aggregation"; companion guide "Measuring forecast accuracy"; explicit doctrine that "machine learning can never replace human expertise… we will always need demand planners to observe and understand real-world changes and correct the automated forecasts accordingly."
- Named persona "Demand planner" in benefits section.
- Vendor metrics (99% accuracy, 85% stockout reduction, 30% inventory reduction; weather reduces error 5–15%…) — vendor claims, excluded from canonical doc.

### Netstock — evidence layer A, Tier 1 operational (help center) — the deepest mechanics in the sample

- **Forecast generation cycle**: "At the beginning of every month, the app automatically regenerates forecasts for every item at every location." Three stages:
  1. Analyze sales history per item-location combination — "identifying trends, patterns, and gaps"; "cleans irregularities such as once-off bulk sales or missing months".
  2. Test and compare forecasting models — "flat, trend, seasonal, sporadic"; back-testing ("which one would have predicted past sales most accurately?"); "the model with the lowest forecast error becomes the best fit".
  3. Assign the demand type and generate forecasts; recalculated "every month and whenever new data is imported or manually refreshed".
- **Demand types** (the item's classification): No History (forecast of zero), Young (weighted moving average), Slow Mover (moving average), Sporadic (smoothed moving average), Seasonal (seasonal model, possibly with trend), Linear Trend, No Trend/No Seasonality; plus special types Sum of Locations (region forecast aggregated from member locations) and Seasonal Group (group seasonal curve applied to low-history item). "Demand types may change automatically over time as the system collects more history."
- **Manual adjustment**: adjust forecasts at item level and macro/group level; "adjust, freeze, or defrost forecasts at both macro and item levels, and how these actions affect replenishment calculations"; bulk revert via upload/download.
- **Attention workflow**: "Forecasts That Need Attention" — "Recognize when forecasts require manual review or correction and what signals to watch for in variance panels and forecast patterns."
- **Event correction**: "correct your forecast and safety-stock inputs after a major disruption such as a pandemic, strike, or supplier shutdown" — history distortion removal.
- **Accuracy history**: "See how past forecasts are recorded, how forecast 'shots' capture historical accuracy, and how forecast history influences future planning." Variance panels and reports for interpretation.
- **Forecast risk and offset**: "how forecast risk and offset are calculated, how they affect safety stock" — forecast quality feeds policy inputs.
- **Demand streams**: "how multiple demand sources combine to form the total forecast, including customer sales, internal transfers, and component demand from Bills of Material" (Sales / Distribution / BOM).
- **Consumption rule**: "While all items receive a forecast, only stocked items use this forecast to generate replenishment recommendations. Non-stocked and obsolete items do not generate recommended orders based on their forecast."
- **NPI handling**: No History type + "Top New Items" dashboard section + "Use Supersessions when a new item replaces an older one. This transfers the historical sales from the old item to the new one."
- **Advanced forecasting feature**: forecast disaggregation, group seasonal forecasting, multi-item manual adjustment, forecast downloads/uploads.
- **Extended planning horizon feature** — longer horizon option.

### GMDH Streamline — evidence layer A (vendor site + docs index), standalone statistical pole

- Product self-description: "AI-native Demand Forecasting Software"; separate named pages for "Demand Planning Software", "Demand Management Software", "Sales Forecasting Software" — vendor itself trades on the terminology split.
- "Accurate Statistical Forecast": warns against "model fit" selection causing overfitting; "generate statistical models on the current periods"; built-in "expert system that automatically analyzes each item for levels, seasonality, trends, and intermittency."
- **Forecast Approval System**: "each SKU to have a status of Approved, Unapproved, or Needs Attention. Approved SKUs are locked from further changes."
- **Flexible Manual Adjustments**: "For many businesses, the final forecast is a consensus between statistical projections and management/planner assumptions. Streamline provides an environment where you can manage, reevaluated, and modified forecasts based on additional information available internally by your management team or provided by your vendors and suppliers."
- **New Products Forecasting**: "link such profiles to the sales history of similar, existing products (substitutions) or set seasonal coefficients."
- **Revenue Planning**: "import sales prices and sales history, allowing revenue forecasts to align with demand forecasts" — value overlay on unit forecast.
- Docs index: Time Series Decomposition, Custom Rows and **Forecast Versions**, ABC Analysis, Adjusting and Approving the Forecasts, Seasonality Pattern, Holidays; Forecast Analysis / Projections / Historical / KPIs reports; dashboards.
- Consumption: ordering plan calculation, safety stock calculation, MRP via BOM, "automatic export of forecasted order information back to your ERP system."
- Vendor's own definitional split (useful boundary evidence): "demand planning is a business process of outlining and management of customer demand… consists of a statistical forecast using the most appropriate model. As a result of the demand planning process, a company gets a sales plan that initiates a service-planning process, production, inventory planning, and revenue planning." And "demand planners take into account forecast accuracy and forecast error levels when doing demand forecasting."

## Cross-product Comparison

| Structure / capability | Kinaxis | SAP IBP | Blue Yonder | RELEX | Netstock | Streamline | Reading |
|---|---|---|---|---|---|---|---|
| Forecast of record per item × location × time bucket | implied (platform) | implied | implied | explicit (product-location-day) | explicit (item × location × month) | explicit (SKU-level) | **defining** |
| Baseline generation from history (statistical and/or ML) | ✓ ML+techniques | ✓ AI+time-series, best-fit selection | ✓ statistical+ML | ✓ ML | ✓ model back-testing, demand types | ✓ expert system, time-series decomposition | **defining** (engine varies) |
| Planner refinement of the forecast (adjust/override) | ✓ collaboration | ✓ coordinated feedback | ✓ consensus | ✓ manual correction | ✓ item+macro adjust, freeze/defrost | ✓ flexible adjustments + approval | **defining** |
| Accuracy vs actuals measured & retained | ✓ (accuracy emphasis) | ✓ forecast value-add | implied | ✓ multi-level accuracy doctrine | ✓ forecast history + "shots" + variance | ✓ KPI/analysis reports | **defining** |
| History cleaning / event correction | — | ✓ outlier detection & correction | — | — | ✓ once-off bulk sales, event correction | — | common |
| New-product forecasting (reference/synthetic/curve) | — | ✓ synthetic data/curves | — | ✓ reference products by attributes | ✓ supersessions, No-History type | ✓ substitutions, seasonal coefficients | common |
| Multi-function consensus (sales/marketing/ops) | ✓ consensus plan | ✓ coordinated feedback | ✓ consensus | ✓ collaborative workflows | ✗ (single planner) | ✓ management consensus framing | common (segment-dependent) |
| Demand sensing (short-term external signals) | ✓ weather/social | ✓ POS/order patterns | ✓ outside-in signals | ✓ weather/events/retailer data | ✗ | ✗ | common in enterprise, absent SMB |
| Demand streams composition (sales+distribution+BOM) | — | — | — | ✓ (raw-material aggregation) | ✓ explicit streams | ✓ BOM/MRP | common |
| Hierarchical aggregation/disaggregation | implied | implied | ✓ multi-dimensional | ✓ data pooling across levels | ✓ macro adjustment, disaggregation feature, Sum of Locations | ✓ (versions/rows) | common |
| Adjustments protected from regeneration | — | — | — | — | ✓ freeze/defrost | ✓ approved = locked | common (naming varies) |
| Exception-based attention lists | — | ✓ suggestions | — | ✓ exception-based workflows | ✓ needs-attention/variance | ✓ Needs Attention status | common |
| Accuracy → policy feedback (risk → safety stock) | — | — | — | implied | ✓ forecast risk & offset | ✓ safety stock from forecast | common |
| Probabilistic forecasting | ✗ | — | — | ✓ option | ✗ | ✗ | optional |
| Scenario / what-if | ✓ (platform) | ✓ (S&OP) | ✓ scenario planning | ✓ (case-study cited) | ✗ | ✗ | optional/enterprise |
| Revenue/value overlay | — | ✓ (S&OP financials) | — | — | ✗ | ✓ revenue planning | optional |
| Granularity range | all horizons | — | — | month→hour, day-level | month (extended horizon feature) | day-resolution timeline | variant |
| Downstream consumption (replenishment/supply/MRP) | ✓ platform | ✓ response & supply module | ✓ paired product | ✓ replenishment/allocation | ✓ replenishment recommendations | ✓ ordering plan/MRP/ERP export | standard context (the seam, not the record) |

## Canonical Model (L0–L3)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The demand forecast of record** — product demand projected as quantities over future time buckets, held per item (and, in practice, per location) as persistent, addressable planning records that the organization plans against. Composed where applicable from multiple demand streams. Remove → a report or spreadsheet of numbers with no standing in the planning process.
2. **The forecast working loop** — a baseline forecast generated from history (statistical and/or machine-learned, with model classification/selection) and then *worked*: planners adjust at item and aggregate level, correct historical distortions, handle new products, and (in mature deployments) reconcile inputs across functions. Remove → a raw prediction feed or an auto-reorder engine; nobody works the forecast.
3. **The accuracy feedback loop** — issued forecasts are retained and compared against actual demand; error and bias are tracked per item, level, and forecast vintage, feeding re-forecasting, model selection, and accountability for both system and human contributions. Remove → a projection calculator with no accountability.

Jointly-held is load-bearing:
- 1 alone = forecast archive / spreadsheet.
- 2 without 1 = a meeting process with no shared record.
- 3 without 1+2 = analytics over someone else's numbers (BI).
- 1+2 without 3 = unaccountable forecast workshop.
- 1+3 without 2 = passive auto-forecast with a scoreboard — the demand *forecasting* tool pole, below the Type.
- 2+3 without 1 = process discipline with nothing persistent.

### L1 — Common Mature Structure

- history cleaning / outlier and event correction before forecasting;
- new-product forecasting machinery (reference products, synthetic history, supersessions, seasonal curves);
- multi-function consensus / collaborative workflows (sales, marketing, operations input; S&OP participation);
- demand sensing (short-horizon adjustment from order patterns and external signals: POS, weather, events);
- demand-stream composition (sales + distribution/transfers + BOM component demand);
- hierarchical aggregation/disaggregation with flexible data pooling across levels and horizons;
- adjustment protection (freeze/defrost/lock/approve states distinguishing human judgment from statistical output);
- exception-based attention lists ("forecasts that need attention");
- accuracy → policy feedback (forecast risk feeding safety stock) and accuracy dashboards;
- downstream consumption interfaces (replenishment, supply planning, MRP, ERP export).

### L2 — Variant / Optional Structure

- engine philosophy: classic statistical families vs ML/AI vs probabilistic forecasting;
- time granularity: monthly (SMB) vs weekly/daily/intraday (retail/fresh);
- consensus depth: single-planner shop vs formal S&OP consensus cycle;
- demand sensing as standalone sibling capability vs embedded;
- scenario/what-if planning; revenue/value overlay; segmentation-based automation; forecast approval workflows; horizon length; retail/CPG channel-level forecasting; industry flavors (fresh/spoilage, sporadic service parts, omnichannel).

### L3 — Vendor-specific (research notes only)

- Netstock: demand-type names (No History/Young/Slow Mover/Sporadic/…), "shots" as the accuracy-history unit, "forecast risk and offset", Advanced Forecasting / Extended Planning Horizon features, Supersessions.
- SAP IBP: forecast-value-add analysis phrasing, AI-assisted forecast results analysis, synthetic-history NPI.
- Kinaxis: consensus-plan phrasing, demand-at-risk pinning, segmentation automation.
- Blue Yonder: "glass box" transparency framing, outside-in forecasting, demand+supply pairing.
- RELEX: Product Attribute AI agent, probabilistic planning option, fresh/spoilage framing.
- Streamline: Forecast Approval System statuses, .gsl project file, group EOQ/discrete-event simulation (inventory side), "AI-native" self-labeling.
- All vendor outcome percentages (accuracy gains, stockout reductions) are marketing claims — excluded everywhere.

## Evidence → Assertion Mapping

- Tier-1 (Netstock help center) supports strong process claims about the SMB pole: regeneration cadence, three-stage generation, demand types, adjust/freeze/defrost, event correction, forecast history/shots, streams, consumption rule.
- Cross-product commonality (≥4 products) supports: baseline generation + planner refinement + accuracy measurement as the working spine; NPI machinery; hierarchy handling; exception lists.
- Consensus/multi-function collaboration: 4/6 products (enterprise-weighted) → common, not definitional (Netstock lacks it; Streamline frames it loosely).
- Demand sensing: 4/6 (same enterprise four) → common-but-era-current, absent in SMB pole.
- Probabilistic, scenarios, revenue overlay, granular sub-week buckets: single or few products → optional/variant.
- No precise numeric limits, default horizons, metric names (MAPE/bias levels), or algorithm parameters asserted for any vendor — evidence does not reach that precision except where Netstock states its own mechanics.

## Boundary Findings

1. **vs Supply Planning** — produces vs consumes: the demand side holds and works the forecast; supply planning takes a demand picture as input and computes the response (planned orders). The seam is the object of record: forecast-of-demand vs plan-of-supply. **RATIFIES the supply-planning pass's requested seam from the demand side.** The same vendors sell both as separate named capabilities (Kinaxis Demand / Supply; SAP IBP Demand / Response & Supply; Blue Yonder demand planning / demand-and-supply pairing), which confirms the split is real in the market, not a directory artifact.
2. **vs Supply Chain Planning Platform** — **DISCHARGES that pass's joint-review flag from the demand side: keep-both RATIFIED.** The platform's defining core is the *integrated whole* (network model + demand plan + supply plan + reconciliation/release loop); demand planning is the demand-domain application that also exists standalone (Netstock, Streamline, RELEX demand planning, Blue Yonder demand planning as separately-named products). The platform's own demand leg is exactly this Type's core embedded in the larger structure — slice-of-whole, sibling Types, consistent with the supply-planning pass's resolution.
3. **vs Inventory Management System** — forward forecast of what will be needed vs stock record of what is and what moved; consistent with that pass's "vs Demand/Supply Planning (record vs forecast)".
4. **vs Advanced Planning & Scheduling / APS and Production Planning** — **DISCHARGES the APS pass's sibling-family flag from the demand side**: demand planning holds no finite-capacity, operation-level time assignment; it produces bucketed demand quantities that APS/production planning may consume as input. The APS structural test (keep it → APS; remove it → bucketed planning) places demand planning on the "remove" side cleanly.
5. **vs Sales Forecasting Platform** — sales forecasting projects revenue/countable measures from the sales organization's own pipeline data, anchored by won actuals, with organizational roll-up; demand planning projects product demand per item × location from history + drivers to drive supply decisions. Different object (money per period per seller vs units per item per location), different source (pipeline vs sales history), different consumer (finance/sales leadership vs supply chain). A product can carry both (Streamline's revenue planning overlays value on the unit forecast) without merging the Types.
6. **vs Energy Forecasting Platform** — same production skeleton (subject of record, recurring model-driven forecast production, verification loop) with a different subject (energy quantities for energy/market operations) and different consumers; domain sibling, not the same Type. Demand planning's subject is product demand per item/location in a supply chain.
7. **vs FP&A / Budgeting & Forecasting** — units of product demand vs currency of accounts; item-level operational planning vs org-level financial model; consistent with those passes' boundaries.
8. **Demand sensing** — a named sibling capability category (RELEX, and others sell it separately); held as a short-horizon adjustment layer inside/near this Type, not a separate directory Type (no leaf exists).
9. **False friend**: Demand Response Platform (§19) shares only the word "demand" (electricity grid events) — no structural relation. Recorded to prevent future confusion.
10. **Thin ancestor / below-the-Type pole**: standalone statistical forecasting tools and passive auto-forecast feeds satisfy forecast production + accuracy but lack the worked, standing forecast-of-record (leg 2 or 1) — treated as the forecasting-tool pole, not the Type center (matches the SCP pass's "1+2 without 3 = forecasting tool" reading from the demand side).

## Historical / Market-Sample Check

- Spreadsheet-era practice: a planner maintaining a SKU × month forecast worksheet with seasonal judgment, adjusting after promotions, and comparing forecasts to actuals satisfies all three legs (the worksheet is the forecast of record; judgment is the working loop; the comparison is the accuracy loop). No ML, no cloud, no demand sensing required.
- ERP-era statistical forecasting modules: history cleaning, automatic model testing/selection (the back-testing Netstock documents has direct lineage in classic forecasting practice), planner override of the forecast, and forecast-vs-actual error tracking satisfy the core. (Generic reasoning; no specific legacy product claimed — not directly fetched this pass.)
- Paper-era analog: forecast sheets in the planning office with hand-adjustments and variance reviews satisfy the shape; reorder-point cards without any forward demand picture do not (thin ancestor, consistent with sibling passes).
- Conclusion: the definition does not depend on ML/AI, demand sensing, consensus S&OP, cloud, or any specific granularity — the §24 check passes.

## Uncertainties

1. Enterprise UI-level mechanics (how Kinaxis/SAP/Blue Yonder/RELEX surfaces actually organize adjustment, approval, and consensus states) are inferred from official product pages and one SMB Tier-1 sample — described at process level only; no interface claims beyond "such surfaces exist" for enterprise vendors.
2. Whether *some* demand planning products lack an accuracy-feedback loop entirely (leg 3): no sampled product did — accuracy measurement appeared in all six samples in some form; but the sample is documentation-reachable products, which biases toward mature offerings. Kept in L0 on the strength of six/six + the discipline's self-description ("planners take into account forecast accuracy and forecast error levels" — Streamline), flagged as a mild residual risk.
3. Location granularity: every sampled product is item × location (or channel), but a single-site organization collapsing location is trivially possible; held as "per item (and in practice per location)".
4. Consensus as a *required* structure was rejected partly on Netstock (single-planner SMB) — if the SMB pole were re-sampled and multi-function consensus proved near-universal even there, leg 2's wording ("in mature deployments") absorbs it; no change to L0 needed.
5. Netstock's "IA Demand Planning" help collection was seen in the navigation but not fetched — AI-era positioning of the SMB pole unverified in detail.

## Final Synthesis

A Demand Planning application is the demand-side planning system of record: it holds a forward forecast of product demand — per item, in practice per location, over time buckets — generated from history by statistical and/or machine-learned models, worked by planners (adjustments, corrections, new products, cross-functional reconciliation), measured against actuals so the forecast keeps improving, and made available to the planning processes that act on it (replenishment, supply planning, production, finance alignment). It plans demand; it does not execute supply, record stock, schedule operations, or project sales revenue. The three legs (forecast of record + working loop + accuracy loop) are jointly held and individually load-bearing; everything else in the market — ML, demand sensing, consensus S&OP, probabilistic forecasting, granular retail buckets — is standard, optional, or variant structure layered on that spine.
