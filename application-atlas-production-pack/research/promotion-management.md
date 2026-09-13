# Research Notes — Promotion Management

Research date: 2026-09-06
Slug: promotion-management
Directory leaf: Promotion Management (§05.14 Pricing & Promotion, Domain B — Commerce, Retail & Marketplace)

---

## Research Goal

Understand what a Promotion Management application is as an Application Type: what the central managed object is, what lifecycle it goes through, how promotions relate to regular prices and markdowns, how promotions reach execution channels, how performance is evaluated, and where the Type's boundaries lie against neighboring Types (Retail Pricing Management, Markdown Optimization, Marketing Campaign Management, Loyalty, commerce-platform discount engines, CPG-side trade promotion management).

## Initial Boundary (pre-research hypothesis)

Promotion Management (in the retail/commerce context of §05.14) was hypothesized to be a merchant-side application for planning, defining, executing, and evaluating temporary promotional price events (discounts, BOGO, coupons, member offers) on selected products over defined periods across channels. Neighbors: Retail Pricing Management (everyday price), Markdown Optimization (clearance), Loyalty Program Management (member benefits), Marketing Campaign Management (customer communication), Trade Promotion Management (CPG manufacturer-side — suspected different Type), e-commerce discount engines (suspected capability, not Type).

## Research Questions

1. What is the central managed object (the promotion) and what does it contain — mechanic, scope, validity period, budget?
2. What lifecycle does a promotion go through (draft → approve → schedule → active → evaluate → archive)?
3. How does the promotion price relate to the regular/base price and to markdowns?
4. How are promotions distributed to execution channels (POS, e-commerce, ERP price engines)?
5. How is performance evaluated (uplift, margin, cannibalization, ROI, base vs incremental)?
6. What roles and approval structures exist?
7. What role does vendor funding (trade spend) play on the retailer side?
8. What distinguishes this Type from Retail Pricing Management, Markdown Optimization, Marketing Campaign Management, Loyalty, and commerce-platform discount engines?

## Representative Products

| Product | Segment / philosophy | Evidence tier |
|---|---|---|
| Oracle Retail Lifecycle Pricing Optimization Cloud Service (LPO; successor of Promotion and Markdown Optimization / Offer Optimization Cloud) | Enterprise retailer-side; optimization-run-centric, forecast-driven recommendations | Tier 1 (docs.oracle.com user guide, release 26.2.301.0) |
| Pricefx (Agreements & Promotions capability) | B2B pricing platform; agreement-document-centric with approval workflow | Tier 1 (knowledge.pricefx.com) + Tier 2 product page |
| DemandTec (Revenue Optimization · Promotions + Trade Performance) | Retailer-side grocery; calendar/event-centric, forecast-led, vendor-fund aware, bilateral retailer↔CPG deal layer | Tier 2 (demandtec.com product pages) |
| Revionics (Promotions, within Base Price / Promotions / Markdown suite) | Retailer-side; AI promotions planning + performance measurement | Tier 2 (revionics.com product pages) |

Boundary sample: commercetools Cart Discounts / Discount Codes (commerce-platform promotion engine — API docs, Tier 1) used to test the "discount engine is a capability, not this Type" boundary.

Rejected/abandoned samples:
- SAP Promotion Management for Retail — help.sap.com is a JS shell; two fetch attempts returned no content. Abandoned per network rule; recorded as source-access limitation.
- Blue Yonder pricing — two 404s on site paths; abandoned.
- Acoustic DemandTec legacy URLs 404; live product found at demandtec.com (used).

## Sources

- Oracle Retail Lifecycle Pricing Optimization Cloud Service User Guide 26.2.301.0 (docs.oracle.com): Get Started page; Use page; User Guide TOC; Ch.1 Lifecycle Pricing Optimization; Ch.2 LPO Workflow and User Roles; Ch.5 Promotion/Markdown What-If Run. URLs:
  - https://docs.oracle.com/en/industries/retail/retail-lifecycle-pricing-optimization-cloud/26.2.301.0/
  - https://docs.oracle.com/en/industries/retail/retail-lifecycle-pricing-optimization-cloud/26.2.301.0/pooug/index.html (toc, offer-optimization.htm, lpo-workflow-user-roles.htm, markdown-promotion.htm)
- Oracle Retail Help Center — Retail index (product portfolio context): https://docs.oracle.com/en/industries/retail/
- Pricefx Knowledge Base: https://knowledge.pricefx.com/pricefx-unity-documentation/pricefx-capabilities/agreements-promotions (+ agreement-promotion-documents, agreements-promotions-detail)
- Pricefx product page: https://www.pricefx.com/platform/promotions/
- DemandTec: https://www.demandtec.com/ and https://www.demandtec.com/promotions
- Revionics: https://www.revionics.com/ and https://www.revionics.com/solutions/promotions
- commercetools API docs (boundary): https://docs.commercetools.com/api/projects/cartDiscounts
- SAP Help Portal (unreachable, JS shell): https://help.sap.com/docs/SAP_PROMOTION_MANAGEMENT — limitation recorded.

---

## Product A — Oracle Retail Lifecycle Pricing Optimization Cloud (LPO)

### Key observations (evidence layer A — directly observed in official user guide)

- **Definition of the lever set.** LPO "recommending promotions, markdowns, regular pricing, and targeted offers". Promotion is defined as "a temporary reduction in the item's price to drive sales, based on forecast data and configurations". Markdown is "a permanent reduction in the item's price, typically for clearance or end-of-life management". Regular price is the base price. Targeted recommendation is "personalized price or offer designed for a specific customer segment or individual".
- **Run-centric workflow.** The unit of work is an optimization *run* (batch or what-if). Run stages: Scope → Business Rules → Results → Forecasting.
  - Scope: season, department (or higher), company/location (or higher), effective week, price zone, strategy; objectives (Max Revenue, Max GM Amount, each ± Salvage; targeted offers = Maximize Redemption Rate); budget constraints.
  - Rules tabs: Temporal (period eligibility: Promotion Allowed / Markdown Allowed / Ineligible; max/min promo items per period; "no touch" windows after landing and before end of life), Planned Events (named promotional events with start/end dates, discount %, merchandise/location/price zone), Promotion (min/max discount for first and subsequent promotions, min time between promotions, max number of promotions per item per season), Markdown (start day, min/max discounts, min time between markdowns), Sell-Through Target (per week, hard/soft enforcement), Price Ladder (percentage or price-point ladders typed for promotions vs markdowns), Pricing Groups (Promote At most One / Promote All or Nothing / Markdown All or Nothing / Same Promotion Discount / Same Markdown Discount / Same Promotion and Markdown Discount / Promote Nothing / Markdown Nothing), Budget (total or separate promo/markdown budgets; allocation schemes: batch, optimally, inventory-value, custom percentages).
  - Results: accept / reject / override per item recommendation; tiles for Revenue, Gross Margin, Sell-Through, Promotion, Markdown, Targeted; item detail with price path / sales path / inventory path / gross margin path; price types color-coded (no-promo price, markdown, planned event, override, promotion).
  - Forecasting: sales forecast decomposed into base sales units (at current ticket price), sales units from price changes (promotions/markdowns), and sales units from planned events; discount bins; returns forecast; exceptions review.
- **Recommendation lifecycle and statuses.** Batch recommendations land in "Ready for Review" → pricing analyst reviews (accept/reject/override) → "Reviewed" → routed to buyer → "Submitted" or "Approved" → sent to export interface and web service to a price execution system (e.g., Oracle Retail Price Management, Customer Engagement). What-if runs can be finalized to replace batch recommendations.
- **Roles and permissions.** Roles: Pricing Analyst, Pricing Manager (analytical super user), Pricing Administrator, Buyer, Targeted Offer User, Regular Price User. Data-level security (merchandise/location scoping) + role-based privileges (create run, view, optimize, review, submit, approve, modify recommendations, delete). Status-based locks: cannot modify runs while running; cannot modify recommendations once reviewed/submitted/approved; administrators cannot delete runs with approved/submitted recommendations.
- **Cadence and automation.** Batch runs typically weekly. Auto-approval criteria configurable (price below threshold, % change below limit, absolute delta within amount). Frequency rules: minimum days since last regular price change, recommendations only on specific weekdays, minimum days since end of previous promotional price period, minimum lead time between regular price changes.
- **Granularity.** Optimization set up at season/department/zone/week; recommendations generated at item (style/color), location/price zone, week, and customer-segment level.
- **Integration.** Exports to price execution systems; integration with Oracle Retail Planning and Execution systems; weekly data refresh (sales, inventory, competitor pricing).

## Product B — Pricefx (Agreements & Promotions)

### Key observations (evidence layer A for KB pages; A/Tier-2 for product page)

- **Positioning.** B2B pricing platform; Promotions is one capability among Price Management, Quoting, Agreements, Rebates, Channel Management. Product page: "Plan, launch, and measure promotions in one place"; "Plan and measure promotions that protect margin".
- **Document-centric model.** Promotions (and customer agreements/contracts) are defined in "Agreement & Promotion documents". "Any number of Agreement/Promotion types (line items), any complexity of calculations and any assignment level (customer/product)."
- **Condition types.** Discounts are defined as **Condition Types**, "each representing a different way of calculating discounts", each with an associated pricing logic. Condition types are "the basic building blocks of any Agreement/Promotion". Supports on-invoice special conditions at product-customer level or general level; "timely limited promotions or 'buy 3 pay 2' can be defined, managed and monitored".
- **Document structure.** Header (start/end dates, calculation and payout dates, user group entitlements, input parameters selecting customer and products, description); Items tab (condition types as line items, folders/subfolders, per-item input parameters, mass edit); Attachments; Workflow (approval steps, status, possible approvers, add approver/watcher); Workflow History; Messages; Activity Log (user actions logged, retention configurable); Documents; Actions; Notes. Document status and workflow status displayed at top.
- **Lifecycle.** Create agreement linked to a condition type → calculation → approval workflow → once approved, **Price Records are automatically generated** for each promotion agreement, tracked in the Price Records section → published into ERP, CRM, CPQ, and eCommerce systems where campaigns run (per FAQ). Statuses observed: Draft, Approved, Denied, Withdrawn, Invalidated.
- **Mass operations.** Submit multiple promotion agreements at once; filter by status (draft/approved); schedule background jobs for mass processing (Calculation Flow); mass edit of line-item inputs.
- **Roles.** "Administer A&P Module" and "Manage A&P Module" roles govern attachment/document actions; user group entitlements for viewing/editing.
- **Planning features (product page).** Promotion calendar and history (active and upcoming promotions with terms/timing); flexible promotion structures (standardized or custom discounts, multiple offer types in one promotion); simulation and ROI modeling (expected volume lift and margin impact before launch); bulk updates and fast rollout (filters, bulk approvals); analytics (ROI, margin change, year-over-year). Four-step process: Design the campaign → Simulate the impact → Roll out and execute → Track and refine.
- **AI.** Promo Pricing Agent (evaluates whether promotions deliver profitable volume), Promotion Volume Agent (compares predicted vs actual volume lift); AI Price Optimization for promotional pricing decisions.
- **Data prerequisites.** Product master, customer master, extensions/attributes, sales transactions, forecasting data, competitive information, historical data, condition types.

## Product C — DemandTec (Revenue Optimization · Promotions; Trade Performance)

### Key observations (evidence layer A/Tier-2 — official product pages; no operational docs fetched)

- **Positioning.** "Commercial Trade Intelligence" platform; two suites on one shared data model: Revenue Optimization (retailer-side: Pricing / Promotions / Markdowns "against one demand model") and Trade Performance (bilateral retailer↔CPG/broker deal layer: Trade Fund Collaboration, Deal & Offer Management, Funds Tracking & Reconciliation).
- **Promotions module.** "Forecast-led promotion planning on the same demand model that sets your base price." Promo calendar shows events by week with event types (illustrated: TPR [temporary price reduction], Ad, Disp [display]).
- **Lifecycle.** Model (predicted lift, cannibalization, margin impact before commit) → Fund (backed by committed vendor dollars) → Run (flighted to stores and digital, tracked live against forecast) → Prove (evaluated on live data, feeds next quarter).
- **Three capabilities.** Promo Planning (events built forecast-first); Promo Flighting & Execution (approved plan flighted to stores and digital, execution tracked against forecast while running); Promotion Eventing & Slotting (events slotted against calendar, evaluated on live data afterward).
- **Vendor funding.** Calendar pulls funding from Trade Performance: each event backed by a committed fund balance both sides see; shared deal record shows vendor funding, committed balance, retail window, CPG committed / retailer accepted status. "The event you promote is the deal your supplier funded. Same record, both sides."
- **Suite coherence.** Promotions ships as part of Revenue Optimization alongside Pricing (base price promotions are planned around and measured against) and Markdowns (clearance on same forecast, "so clearance never fights the promo calendar").
- **Vendor-cited marketing figures (not verified facts):** "72% of trade promotions fail to break even (Nielsen · McKinsey)"; "CPGs fund 40 to 60 percent of every promotional event"; "90%+ forecast accuracy". Treated as vendor claims only.

## Product D — Revionics (Promotions)

### Key observations (evidence layer A/Tier-2 — official product pages)

- **Positioning.** "Retail Promotion Intelligence Powered by AI"; promotions is one of three solutions (Base Price / Promotions / Markdown) in a lifecycle pricing optimization platform.
- **Scope of promise.** "Improve your promotions from planning to performance measurement"; "Simulate outcomes and tailor promotional strategies to the most efficient offers"; "Evaluate impacts, results, and cross effects to determine promotional winners, eliminate under-performers and identify new opportunities"; "Unite your pricing, marketing, and category teams to streamline promotional planning, hone marketing spend, and enhance vendor partnerships."
- **Blog titles observed (topic signals, not operational evidence):** promotional price elasticity; designing promotions that outperform last year; private label promotions; promotional performance analysis.

## Boundary sample — commercetools Cart Discounts (commerce-platform promotion engine)

### Key observations (evidence layer A)

- Cart Discount object: value (relative %, absolute amount, fixed price, gift line item), target (line items, custom line items, shipping cost, total price; multi-buy and pattern targets for "buy X get Y" mechanics), cart predicate (eligibility conditions), valid from/until, active flag, sort order, stacking mode, discount groups, requires-discount-code, stores scoping. Discount Codes as separate object.
- This is **execution machinery evaluated at cart time** inside a commerce platform: no planning calendar, no demand forecast/simulation, no vendor funds, no approval workflow, no post-event performance evaluation, no budget. It is the surface a Promotion Management application feeds (Pricefx FAQ explicitly says approved promotional prices are published "into the ERP, CRM, CPQ, and eCommerce systems where campaigns run").

---

## Cross-product Comparison

| Aspect | Oracle LPO | Pricefx A&P | DemandTec Promotions | Revionics Promotions |
|---|---|---|---|---|
| Side / segment | retailer (pricing/merchandising) | B2B seller (pricing team) | retailer, grocery-centric (+ bilateral CPG layer) | retailer |
| Central object | optimization run → item-level price recommendations | Agreement/Promotion document (condition-type line items) | promotion event on a promo calendar | promotion offer (planned → measured) |
| Scope dimensions | season × department × location/price zone × week × (customer segment) | customer × product × dates (+ user groups) | category × week × event type (TPR/ad/display) | items × stores (zones implied) |
| Mechanic representation | discount %, price ladders (percent/price-point), planned events | condition types with calculation logic (incl. "buy 3 pay 2") | event types (TPR, ad, display) | offer types (undocumented detail) |
| Lifecycle | run: scope→rules→optimize→Ready for Review→Reviewed→Submitted/Approved→export | Draft→approval workflow→Approved→Price Records generated→publish | Model→Fund→Run→Prove | plan→simulate→execute→measure |
| Forecast / simulation | demand forecast; base vs price-change vs planned-event sales; returns forecast | simulation & ROI modeling (volume lift, margin impact) | predicted lift, cannibalization, margin impact before commit | simulate outcomes; cross effects (cannibalization/affinity) |
| Funding / budget | promo & markdown budgets with allocation schemes | (seller's own margin; no vendor-fund layer observed) | committed vendor dollars from bilateral deal layer | "vendor partnerships" (undocumented) |
| Evaluation | results tiles (revenue/GM/sell-through), forecast review, exceptions | ROI, margin change, YoY analytics; predicted-vs-actual agents | live tracking vs forecast; post-evaluation feeds next quarter | performance analysis; winners/under-performers |
| Distribution | export/web service to price execution system (ORPM/RPCS) | Price Records → ERP/CRM/CPQ/eCommerce | flighted to stores and digital | not documented |
| Governance | roles (analyst/manager/admin/buyer) + status locks + data scoping | module roles + approval workflow + activity log + entitlements | both-side visibility (committed/accepted) | not documented |
| Optimization/AI | core (optimization engine generates recommendations) | optional AI agents + AI optimization | forecast-led modeling core; agentic AI | AI core |

### Convergent findings (evidence layer B — cross-product commonality)

1. The promotion is a **defined, temporary offer on a selected product scope over a defined validity period** — present in all four products (Oracle: temporary reduction + effective week; Pricefx: start/end dates; DemandTec: retail window; Revionics: planning→measurement of offers).
2. A **governed lifecycle with explicit states and approval** — Oracle (Ready for Review→Reviewed→Submitted/Approved), Pricefx (Draft→workflow→Approved), DemandTec (committed/accepted deal states), Revionics (plan→execute implied governance).
3. **Evaluation against intended commercial outcomes** — all four: Oracle (results vs current price), Pricefx (ROI/margin), DemandTec (lift/ROI vs forecast), Revionics (winners/under-performers).
4. **Relationship to base price and markdown as sibling levers** — Oracle and DemandTec and Revionics all structure regular price / promotion / markdown as distinct levers, often on one demand model; promotion is explicitly *temporary*, markdown *permanent*.
5. **Distribution to execution systems** — Oracle (price execution system export), Pricefx (ERP/CRM/CPQ/eCommerce publish), DemandTec (flighted to stores and digital).
6. **Simulation/forecasting before commit** — Oracle, Pricefx, DemandTec, Revionics all offer pre-launch impact estimation (lift, margin, cannibalization/cross effects).
7. **Calendar as planning surface** — Pricefx (promotion calendar and history), DemandTec (promo calendar by week), Oracle (effective week / planned events / temporal rules). Revionics implies planning cadence.

### Divergent findings (vendor/segment-specific)

- **Run-centric optimization** (Oracle): the promotion plan is produced by an optimization engine over rules; humans review recommendations. Other samples are human-authored plans with optional AI.
- **Document/agreement-centric** (Pricefx): promotion as a contract-like document with condition-type line items, approval workflow, generated price records — B2B shape.
- **Bilateral vendor-fund layer** (DemandTec): promotion events bound to committed vendor funds shared with CPG partners — grocery/trade-spend shape; unique in sample.
- **Targeted/customer-segment offers** (Oracle Targeted Offers; Pricefx customer-segment eligibility): personalization as an extension, not universal.

## Canonical Model (synthesis)

### L0 — Defining Invariant (deliberately small)

A Promotion Management application is recognizable when all of the following hold:

1. **Promotion record** — a defined offer (the mechanic: e.g., a discount) bound to (a) a product scope, (b) a validity period (start/end), and optionally (c) a location/customer scope. The record is the unit of planning.
2. **Governed lifecycle** — the record moves through created/planned → approved → activated/scheduled states under human accountability, and is distributed to the surfaces where the promotion actually applies (price execution / commerce).
3. **Tracked performance** — the promotion record persists as the anchor for measuring what the promotion did (sales/margin/ROI against a baseline).

Remove the temporality → everyday price management. Remove the governed lifecycle and measurement → a discount engine (capability). Remove the offer/price mechanics → campaign management. Remove the product/price object entirely → generic project/campaign planning.

### L1 — Common Mature Structure

- Promotion calendar (planning surface over time; active/upcoming/history)
- Library of promotion mechanics/types (condition types, event types, offer templates)
- Simulation / impact forecast before commit (volume lift, margin impact, cannibalization/cross effects)
- Approval workflow with roles and status locks; audit/activity history
- Bulk/mass operations (mass update, bulk approval, copy/relaunch)
- Distribution/publishing to execution systems (POS price files, e-commerce engines, ERP conditions)
- Performance analytics (base vs incremental, ROI, margin change, period-over-period)
- Budget tracking for promotional spend
- Overlap/stacking/conflict handling between concurrent promotions
- Integration data: product master, customer/store master, sales history, cost/margin data

### L2 — Variant / Optional Structure

- Vendor-funded promotions (trade funds, committed balances, bilateral deal records) — grocery/CPG shape
- Customer-segment / targeted / member offers (personalized promotions; loyalty adjacency)
- Optimization engine generating recommended promotions (vs human-authored plans)
- Location/price-zone granularity; store clusters
- Coupon codes as a distribution mechanic
- Markdown as sibling module (separate leaf in directory) — some products share one engine
- B2B agreement-style promotions (net-price conditions, payout dates, rebate adjacency)
- Seasonal/annual promotion planning integrated with merchandise financial planning
- AI agents monitoring promotion performance (predicted vs actual)

### L3 — Vendor-specific (research notes only)

- Oracle: run types (batch/what-if), DEFAULT_SET strategy, rules tabs (Temporal/Planned Events/Promotion/Markdown/Sell-Through/Price Ladder/Pricing Groups/Budget), recommendation statuses, RPCS/ORPM export, auto-approval criteria, Digital Assistant integration, GenAI explanation panel, Innovation Workbench.
- Pricefx: Condition Types, Price Records, A&P module roles, Calculation Flow mass processing, header/input-parameter logic configuration, activity-log retention configuration.
- DemandTec: Commercial Trade Intelligence framing, Trade Performance suite (Trade Fund Collaboration, Deal & Offer Management, Funds Tracking & Reconciliation), buyer intelligence, AI confidence scoring, SPARK Matrix claims, "7,800+ connected CPG partners" (vendor figure).
- Revionics: proprietary AI models, "The Exchange" customer references, Aptos ownership.

## Vendor-specific Findings

See L3 above. Additionally: DemandTec's marketing cites third-party figures (72% of trade promotions fail to break even; CPGs fund 40–60% of promotional events) — recorded as vendor-cited claims, not established facts; not used in the final document.

## Boundary Findings

1. **vs Retail Pricing Management** (sibling leaf): pricing management owns the everyday/base price; promotion management owns *temporary, event-driven* deviations. In Oracle and DemandTec both levers share one demand model but remain distinct objects with distinct rules (regular-price frequency rules explicitly reference "since the end of the previous promotional price period"). Test: remove temporality/event character → pricing management.
2. **vs Markdown Optimization Application** (sibling leaf): markdown is a *permanent* reduction for clearance/end-of-life; promotion is temporary. Oracle defines both in one sentence pair and gives them separate rule sets within one run type; DemandTec ships them as separate modules on one forecast ("clearance never fights the promo calendar"). Test: remove the temporary/restore-full-price intent → markdown.
3. **vs Marketing Campaign Management Platform** (§06): campaigns communicate with customers (email/ads/social); promotion management owns the *commercial offer terms and their price execution*. A campaign may announce a promotion; it does not define promo prices or measure price lift. Test: remove offer/price mechanics and price-lift measurement → campaign management.
4. **vs Loyalty Program Management** (sibling §05.15): loyalty owns the member program and its benefits; promotion management may *issue* member-targeted promotional offers (Oracle Targeted Offers) but does not run the program (points, tiers, accrual). Test: remove program membership machinery → promotion variant.
5. **vs commerce-platform discount engines** (commercetools Cart Discounts/Discount Codes; Shopify/Salesforce equivalents): engines evaluate discount conditions at cart/checkout time inside a commerce platform — no planning calendar, no forecast, no vendor funds, no approval, no post-evaluation. Promotion Management *feeds* engines. Test: remove planning/governance/measurement → capability inside a commerce platform, not a Type.
6. **vs Trade Promotion Management (CPG-side)**: TPM is the manufacturer planning/funding promotions *through* retailers; this leaf is the seller/retailer running its own promotional events. DemandTec's Trade Performance suite is the bilateral bridge (same deal record both sides). The directory has no CPG-side TPM leaf; no conflict, but the seam is real and recorded.
7. **vs Deal Discovery Platform** (§05.05): consumer-side discovery of deals; promotion management is merchant-side creation of the deals. Opposite sides of the same promotional event.

## Historical / Market-Sample Check

Would older, regional, or platform-native products still fit the L0? Yes: promotion planning predates optimization AI — merchandising systems' "deal" records (temporary promo prices with start/end dates distributed to POS), spreadsheet-and-calendar promotion planning, and grocery TPR/ad/display planning all satisfy "promotion record + governed lifecycle + tracked performance" without forecasting engines, vendor-fund layers, or customer-segment targeting. The L0 does not over-fit to the current AI-optimization era. Conversely, the modern samples' shared features (calendar, simulation, approval, distribution, analytics) are L1, not definition.

## Uncertainties

- SAP Promotion Management for Retail could not be reached (JS-shell help portal); the event/tactic/fund structure of the other major enterprise vendor is unverified. Assertions about enterprise promotion structure rest on Oracle + DemandTec + Pricefx + Revionics.
- Blue Yonder unreachable (404s); not sampled.
- DemandTec and Revionics evidence is Tier-2 (official product pages, no operational docs); no field-level or status-level claims were taken from them beyond what their pages state.
- Exact numeric limits (e.g., Oracle run-name length, discount defaults) are vendor-specific and were not promoted to the final document.
- The relative market weight of "optimization-led" vs "calendar-led" promotion management is unclear from this sample; both philosophies documented, no market-share claim made.
- Whether vendor-funded promotion management (trade funds) should eventually be a separate Type (CPG-side TPM) is a taxonomy question for joint review; no directory leaf conflicts today.

## Final Synthesis

Promotion Management is the merchant-side application that treats temporary promotional offers as managed, governed, measurable business objects: a promotion record (mechanic + product scope + validity period, optionally location/customer scope) moves through a governed lifecycle (plan → approve → activate → distribute) and remains the anchor for performance evaluation (lift, margin, ROI against baseline). It sits between everyday price management (which owns the base price the promotion deviates from) and campaign communication (which announces the offer), and it feeds execution surfaces (POS price engines, e-commerce discount engines, ERP pricing conditions) where the promotion actually applies. Mature products add a calendar, mechanic libraries, simulation, budgets, bulk operations, and analytics; variants add vendor funding, customer-segment targeting, and optimization engines.
