# Demand Planning

## Overview

A **Demand Planning** application is an organization's demand-side planning system of record. It holds a forward forecast of product demand — what will be needed, where, and when — as persistent planning records organized per item and location over time buckets. The forecast is generated from sales history by statistical methods (in modern products, machine-learned ones), then *worked*: demand planners adjust it with market knowledge, correct historical distortions, handle new products, and reconcile inputs across functions. Past forecasts are retained and measured against actual demand, so forecast accuracy is a managed number rather than a hope. The finished forecast is what downstream planning — replenishment, supply planning, production, finance — acts on.

The defining structure is small:

```text
Item × location × time-bucket demand forecast of record
└── Generated baseline (from history, by statistical or ML methods)
    └── Worked by planners (adjust, correct, reconcile, approve)
        └── Measured against actuals (accuracy retained and fed back)
```

Everything else commonly associated with the category — machine learning, demand sensing from external signals, cross-functional consensus cycles, promotion and price modeling, probabilistic forecasting, dashboards — is standard capability in mature products, not what makes the product a demand planning application.

Two boundaries frame the Type. First, demand planning **plans demand; it does not respond to it**: computing what to buy, make, and move in reaction to the forecast is Supply Planning. Second, it is **forward-looking**: recording what stock exists and what moved is an Inventory Management System's job, not this one.

## Users & Context

The primary user is the **demand planner** (in smaller organizations, often the buyer or inventory planner wearing the forecasting hat): the person accountable for the quality of the forward demand picture.

Typical work:

- review the statistical baseline and the items flagged as needing attention
- adjust forecasts where market knowledge contradicts the statistics — an upcoming promotion, a lost customer, a competitor's move
- correct historical distortions after one-off disruptions so they do not shape the future
- manage new-product forecasts that have no sales history yet
- answer for forecast accuracy at the levels that matter (by item, category, location, period)

Contributing and secondary users:

- **sales and marketing** — supply market-side knowledge and promotion plans that the statistics cannot know; in larger organizations their input is reconciled into a single consensus demand plan
- **S&OP participants and supply chain managers** — consume the demand plan as the "demand side" of the periodic cross-functional reconciliation of demand, supply, and financial expectations
- **supply and inventory planners** — the forecast's principal consumers: they translate it into replenishment and supply orders
- **executives and finance** — view the demand plan at aggregate level, often with a revenue or value overlay

Typical context: manufacturers, distributors, wholesalers, and retailers with enough items and locations that forecasting in spreadsheets breaks down. The work runs in a **rolling cycle**: the forecast covers a horizon extending weeks to months ahead, is regenerated as history accumulates, is reviewed and adjusted on a weekly or monthly rhythm, and is measured after each period closes. In organizations running sales and operations planning (S&OP), the demand plan is the object that process reconciles.

## Core Model

### The Defining Core

Three structures, held together. Remove any one and the product stops being demand planning:

- **The demand forecast of record** — product demand projected as quantities over future time buckets (months at the small-business pole; weeks, days, or even finer where operations require it), held per item and, in practice, per location. It is a persistent, addressable planning record: the same forecast the planners adjusted last week is the forecast the supply side consumes this week. Where the organization's demand is more than direct sales, the record is **composed from demand streams** — direct sales, the supply required by downstream locations the location feeds, and the component demand implied by planned production of finished goods. Without it there is nothing to plan against — just an analysis.
- **The forecast working loop** — the forecast is generated, then *worked*. A baseline is computed from sales history by statistical or machine-learned methods (history is cleaned of irregularities first; models are tested against how well they would have predicted the past; each item lands on the method that fits its demand pattern). Planners then shape it: adjustments at item and aggregate level, protection of important adjustments from being regenerated away, correction of one-off events out of history, handling of new items that have no history (transferring the sales history of the products they replace, or borrowing the pattern of similar products), and — in mature deployments — reconciliation of sales, marketing, and operations input into one consensus number. Without it, the product is a raw prediction feed.
- **The accuracy feedback loop** — issued forecasts are retained, and when a period closes, actual demand is compared against what was forecast: overall and per item, per level, and against the forecast *as it stood when issued*. Error and bias become visible, managed numbers. They drive re-modeling and re-forecasting, they calibrate which methods to trust for which items, and they make both the system's output and human overrides accountable (in mature products, the contribution of each planning input to accuracy is itself measured). Without it, the product is a projection calculator with no accountability.

### What the forecast looks like

A forecast record carries, conceptually:

- the item (and location, and channel where relevant)
- the quantity expected per time bucket, across the horizon
- the baseline (statistical) value and the final, human-shaped value — distinguished, not merged
- the item's demand classification — the system's judgment of the demand pattern (steady, trending, seasonal, sporadic, new) that determines how the forecast is computed
- the adjustments applied, who made them, and whether they are protected from regeneration
- the demand streams that compose the total, where the item's demand has multiple sources

### Standard capabilities around the core

Mature products commonly add:

- **History cleaning and event correction** — removing one-off bulk sales, gaps, and disruption-period distortions from the history the forecast is built on.
- **New-product forecasting** — reference products matched by attributes, synthetic history, seasonal curves borrowed from product groups, or supersession linkage.
- **Demand sensing** — short-horizon adjustment of the near-term forecast from fresh signals: recent order patterns, point-of-sale data, weather, events.
- **Hierarchical aggregation and disaggregation** — one forecast, usable at SKU-day granularity for replenishment and at category-month granularity for consensus and finance; adjustments entered at any level and spread coherently.
- **Exception-based review** — lists and panels of the forecasts that most need attention (large variance, unstable patterns, thin history), so scarce planner effort goes where it matters.
- **Accuracy machinery** — variance panels, accuracy dashboards by level and period, and feedback of forecast uncertainty into stocking policies.
- **Scenario analysis** (enterprise products) — copy the demand plan, change an assumption (a promotion, a price change, a demand shock), recompute, and compare before committing.
- **Value overlays** — revenue or financial views aligned to the unit forecast for finance-facing processes.
- **Integration** — sales history, item master, and actuals flow in from ERP or commerce systems; the forecast flows out to replenishment, supply planning, and production planning.

### One structure, many implementations

The Core Model is written in conceptual terms. Products realize it differently:

```text
Concept:            baseline generation
Implementations:    classic statistical model families with back-tested
                    selection; ML/AI models; probabilistic modeling

Concept:            the human-shaped forecast
Implementations:    frozen/protected adjustments, approval states that lock
                    items, consensus plans reconciled across functions

Concept:            accuracy history
Implementations:    point-in-time forecast snapshots compared to actuals,
                    variance panels, input-by-input value-added analysis

Concept:            demand classification
Implementations:    named pattern types per item (new / steady / seasonal /
                    sporadic / trending), ABC or velocity segmentation
```

A reader who has only seen one implementation — say, a small-business tool that produces a monthly unit forecast per item and warehouse — should still be able to recognize an enterprise ML-driven consensus platform as the same Type.

## How It Works

The canonical work of demand planning is a **rolling forecast cycle**:

### 1. Feed history and items

Sales history, item master, locations, and (where used) bills of material and open-order context flow in from the ERP or commerce systems. Keeping this data current is structural: every forecast inherits its quality.

### 2. Generate the baseline

The system analyzes each item's history at each location: classifies the demand pattern, cleans irregularities, selects or applies the forecasting method that fits, and produces the baseline forecast per item × location × bucket. In mature products this step is highly automated — the point of the machinery is that planners do not tune every item by hand.

### 3. Work the forecast

Planners review by exception: items flagged for attention first, then their own areas of knowledge. They adjust at item level or in aggregates (a category, a region), and their important adjustments can be protected so the next regeneration does not erase them — and reversed when no longer wanted. Events are corrected out of history; new products get a starting forecast from their references. Where the organization runs consensus planning, sales, marketing, and operations inputs are gathered, compared, and reconciled into one demand plan with recorded ownership.

### 4. Publish to the consumers

The finalized forecast becomes the forward demand picture for everything downstream: replenishment calculations and recommended orders, supply planning's input, production and material planning, and — with a value overlay — the financial view. The demand planning application plans demand; it does not create purchase orders, schedule production, or ship anything.

### 5. Measure and improve

When a period closes, actual demand is compared against the retained forecast: accuracy overall and per item, per level, and against each forecast vintage as it stood when issued. The results drive attention lists, method recalibration, and accountability — including measurement of whether human adjustments added value or destroyed it. The horizon rolls forward and the cycle repeats.

### Core vs common vs optional

- **Defining core** — forecast of record per item × location × bucket; baseline generation from history; planner refinement of the forecast; retained accuracy measurement against actuals.
- **Standard in mature products** — history cleaning; new-product machinery; hierarchical aggregation; exception lists; accuracy dashboards; integration to ERP and to replenishment/supply planning.
- **Optional / variant** — demand sensing from external signals; cross-functional consensus workflow; scenario analysis; probabilistic forecasting; value overlays; sub-week granularity; approval workflows.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Forecast workbench

The demand planner's home surface.

- Purpose: review and shape the forecast.
- Typical information: forecast per item × location × bucket alongside history, actuals, the statistical baseline, the item's demand classification, variance indicators, and flags for items needing attention.
- Primary actions: adjust at item or aggregate level, protect/freeze or revert adjustments, drill into demand streams, drill into the accuracy of past forecasts, export/import for bulk work.

### Item forecast detail

The deep view for one item × location.

- Purpose: understand and justify one forecast.
- Typical information: time-phased history, actuals, baseline vs final forecast, the pattern classification and why it was chosen, the factors the system identified as driving the forecast.
- Primary actions: adjust buckets, correct an event in history, set or change the reference for a new item, annotate.

### Exception / attention lists

- Purpose: focus review effort where the forecast is least trustworthy.
- Typical information: items with large variance, unstable or insufficient history, forecasts inconsistent with open orders or plans.
- Primary actions: open the workbench filtered to the exception, assign review, resolve.

### Accuracy dashboard

- Purpose: manage forecast quality as a number.
- Typical information: error and bias by level, period, and forecast vintage; comparison of statistical baseline vs final forecast vs actuals; contribution of planning inputs to accuracy.
- Primary actions: drill to the items behind a number, recalibrate methods, hold the process accountable.

### Consensus / collaboration views (enterprise)

- Purpose: gather and reconcile demand input from sales, marketing, and operations.
- Typical information: each function's input against the statistical baseline, gaps between them, the reconciled consensus plan and its ownership.
- Primary actions: submit input, compare versions, record the consensus decision.

### Scenario manager (optional)

- Purpose: test demand assumptions before committing.
- Typical information: side-by-side demand plans under changed assumptions (promotion, price change, shock) with their downstream consequences.
- Primary actions: copy a scenario, change inputs, recompute, compare, promote to the working plan.

### Configuration & administration

- Purpose: maintain the substrate — item master and classifications, locations and hierarchies, forecast methods and their parameters, adjustment policies, users and roles, integration settings.

## Important Rules / Behaviors

### The forecast is regenerated, and adjustments can be protected

Forecasting is not "edit once": products regenerate the baseline on a rolling cadence as history accumulates and inputs change. What keeps human judgment from being erased is protection — adjustments that are frozen, locked, or held as a separate layer that regeneration respects until deliberately reverted. The system therefore always distinguishes the statistical baseline from the final, human-shaped forecast.

### History is corrected, not blindly extrapolated

A strike, a pandemic dip, a one-off bulk sale in the history will otherwise shape every future period. Cleaning irregularities and correcting one-off events out of history is a first-class activity, not a data-hygiene afterthought.

### The forecast is a planning quantity, not a promise

Unlike a sales forecast committed by a salesperson, the demand plan is the organization's best forward estimate, expected to be wrong in both directions and managed for that: accuracy is measured, uncertainty feeds stocking policies, and the plan is revised every cycle. Treating it as a commitment misreads the Type.

### Accuracy is measured against what was known when the forecast was issued

Mature products retain forecast vintages — the forecast as it stood at each point — so improvement is measured against the information available at the time, not against a forecast quietly updated afterward. Both the system's baseline and human adjustments are held to this standard.

### Demand patterns differ, so forecasts are classified per item

Steady sellers, seasonal goods, trending lines, sporadic movers, and brand-new products cannot be forecast the same way. Products classify each item's demand pattern and forecast accordingly — and re-classify as history accumulates. Item classification is a planning input, not just a report filter: in some products, non-stocked or obsolete items receive forecasts but no forecast-driven recommendations.

### The total demand can be more than sales

Where items are transferred between locations or made from components, the demand for an item at a location includes the supply required downstream and the consumption implied by production. The forecast of record composes these streams; planning on direct sales alone under-forecasts exactly where the network is busiest.

### The forecast drives the plan, but never executes

Replenishment recommendations, planned orders, and production proposals computed from the forecast belong to the consuming applications. Demand planning's output is the forward demand picture; releasing and executing orders is downstream.

## Variants

Common forms of the Type:

- **Enterprise consensus / IBP-shaped** — demand planning inside an integrated business planning suite, with cross-functional consensus workflow, scenario analysis, and financial reconciliation as first-class layers.
- **Concurrent-platform module** — demand planning as the demand leg of a platform where forecast changes propagate immediately into supply and inventory views.
- **Retail / CPG high-granularity** — day- or sub-day-level forecasts per product × store (or channel), ML-driven promotion, price, and event effects, fresh-product spoilage sensitivity, and forecasts feeding automated replenishment and workforce planning.
- **SMB ERP-companion** — a monthly cadence per item × warehouse, transparent statistical models, hands-on planner adjustment, recommended orders exported to the ERP; the same core with lighter machinery.
- **Standalone statistical specialist** — forecasting depth (decomposition, pattern classification, approval states) sold as a focused product, with replenishment/MRP as the downstream consumer.
- **Probabilistic pole** — uncertainty expressed as distributions rather than single numbers, feeding service-level-driven stock policies.
- **Demand-sensing-heavy pole** — short-horizon signal ingestion (POS, weather, events) packaged as a named sibling capability alongside the core forecast.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Supply Planning | consumes the forecast and produces the response (planned buy/make/move orders). The seam is the object of record: demand planning holds the forecast; supply planning holds the plan of orders computed from it. The same vendors commonly sell both as separate capabilities |
| Supply Chain Planning Platform | the integrated whole — network model, demand plan, supply plan, and reconciliation/release loop in one system. Demand planning is the demand-domain application that also exists standalone; inside the platform it appears as this Type's core embedded in the larger structure |
| Inventory Management System | records what stock is and what moved (system of record for the present); demand planning holds the forward expectation. Replenishment logic keyed to stock levels alone is inventory territory, not planning |
| Advanced Planning & Scheduling / APS | assigns operations to finite capacity at operation-level time detail inside the plant; demand planning produces bucketed demand quantities with no operation-level scheduling. APS may consume the demand plan as input |
| Sales Forecasting Platform | projects revenue (or countable sales measures) from the sales organization's own pipeline data, rolled up through the sales hierarchy; demand planning projects product demand per item × location from history and drivers to drive supply. Money vs units; pipeline vs sales history; different consumers |
| Financial Planning & Analysis / Budgeting & Forecasting | org-level financial models in currency over accounts; demand planning is item-level operational planning in units. The forecast may feed a revenue view, but the financial plan of record stays with finance |
| Energy Forecasting Platform | same production skeleton (forecast subject of record, recurring model-driven production, verification loop) applied to energy quantities — generation, load, price — for energy operations; a domain sibling, not this Type |
| ERP | transactional system of record and data source; ERP-embedded forecasting modules are the historical ancestor implementation of this Type's logic, and released plans flow back into the ERP for execution |

The sharpest boundaries are the two supply-side siblings: against **Supply Planning** (produces the forecast vs consumes it) and against the **Supply Chain Planning Platform** (demand-domain application vs integrated whole). Both are ratified as sibling Types: standalone demand-planning products exist and are sold as such, while the platform holds the demand leg together with the rest.

## Representative Products

- **Kinaxis (Maestro / RapidResponse)** — demand planning as the demand application of an enterprise concurrent-planning platform; consensus-collaboration and forecast-explainability emphasis.
- **SAP Integrated Business Planning (Demand Planning)** — enterprise IBP module; AI + time-series baseline automation, coordinated multi-function feedback, forecast-value-add measurement.
- **Blue Yonder (Demand Planning)** — enterprise specialist heritage; consensus planning with a "glass box" causal-transparency emphasis, paired with supply planning.
- **RELEX Solutions** — retail/CPG pole; highly automated ML forecasting at product-location-day granularity with planner correction workflows and probabilistic options.
- **Netstock** — SMB/mid-market ERP-companion pole; transparent statistical forecasting per item × location with item- and group-level adjustment, event correction, and accuracy history.

The defining core was checked against older and thinner shapes — spreadsheet-era planning practice (a maintained SKU × period forecast worksheet with judgment-based adjustment and actuals comparison) and ERP-era statistical forecasting modules — both of which satisfy the core without any modern machinery: no machine learning, no cloud, no demand sensing, no consensus workflow.

## Sources

Research date: **2026-09-08**

Official sources used:

- Kinaxis — Demand Planning solution page — https://www.kinaxis.com/en/solutions/demand-planning
- SAP — Integrated Business Planning, Demand Planning features — https://www.sap.com/products/scm/integrated-business-planning/features/demand-planning.html
- Blue Yonder — Demand Planning solution page — https://www.blueyonder.com/solutions/supply-chain-planning/demand-planning
- RELEX Solutions — Demand planning software page — https://www.relexsolutions.com/solutions/demand-planning-software/ ; official guide "Demand forecasting for retail and consumer goods" — https://www.relexsolutions.com/resources/demand-forecasting/
- Netstock Help Center (operational documentation) — https://help.netstock.com/en/ ; Forecasting collection — https://help.netstock.com/en/collections/18733700-forecasting ; "Mastering Forecasting" — https://help.netstock.com/en/articles/12528486-mastering-forecasting ; "Demand Types & Sales Forecast Generation Explained" — https://help.netstock.com/en/articles/12528487-demand-types-sales-forecast-generation-explained
- GMDH Streamline — Demand forecasting page — https://gmdhsoftware.com/demand-forecasting/

> Sourcing limitation: operational (help-center-level) documentation was directly accessible only for the SMB-pole product (Netstock). The enterprise vendors' detailed documentation is login-gated or not fetched (Kinaxis knowledge base, SAP Help Portal, Blue Yonder docs, RELEX user docs, Streamline webhelp), so enterprise behavior is described at process level from official product and solution pages — not at UI level — and no precise vendor figures, defaults, limits, or algorithm parameters are asserted anywhere in this document. Vendor-published outcome percentages (accuracy gains, stockout reductions) are marketing claims and are not cited as evidence. Product-by-product observations, the cross-product comparison matrix, and the boundary record are kept in the paired Research Notes.
