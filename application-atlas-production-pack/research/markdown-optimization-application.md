# Research Notes — Markdown Optimization Application

Research date: 2026-09-10
Slug: markdown-optimization-application
Directory leaf: Markdown Optimization Application (§05.14 Pricing & Promotion, Domain B — Commerce, Retail & Marketplace)

---

## Research Goal

Understand what a Markdown Optimization Application is as an Application Type: what the central managed object is (the markdown event, the markdown schedule/ladder, or the optimization run), what makes a markdown a markdown (permanence, clearance intent, inventory revaluation) as opposed to a price change or a promotion, how markdown schedules (ladders/waves/step-downs) work, what yardstick drives markdown decisions (sell-through targets, clearance deadlines), what the optimization layer recommends and against what objectives, what lifecycle and rules govern markdowns, and where the Type's boundaries sit against the two processed sibling leaves (Retail Pricing Management, Promotion Management) and other adjacent Types.

## Initial Boundary (pre-research hypothesis)

Markdown Optimization Application was hypothesized to be the retailer-side application that clears aging, seasonal-end, or excess inventory through permanent price reductions, deciding which items to mark down, when, how deep, and how fast, against sell-through targets and clearance deadlines. The two sibling passes pre-anchored the seams:

- research/retail-pricing-management.md: "markdown is a *permanent* reduction for clearance/end-of-life with inventory revaluation; pricing management owns the everyday price"; "the sibling leaf owns the markdown-optimization center of gravity."
- research/promotion-management.md: Oracle LPO defines markdown as "a permanent reduction in the item's price, typically for clearance or end-of-life management"; promotion is temporary.

Expected neighbors: Retail Pricing Management (everyday price), Promotion Management (temporary events), Inventory Management (owns the stock records markdowns consume), Merchandise Financial Planning (owns the markdown-dollar plan), commerce dynamic-pricing engines (continuous competitive repricing), POS/e-commerce (execution surfaces).

## Research Questions

1. What is the central object — the markdown event, the markdown schedule/ladder, or the optimization run?
2. What makes a markdown a markdown — permanence, clearance/end-of-life intent, inventory revaluation — and how is it distinguished from a price change and a promotion?
3. How do markdown schedules work (ladders, waves, step-downs; depth and timing constraints)?
4. What yardstick drives markdown decisions (sell-through targets, exit dates, weeks of supply, margin recovery)?
5. What does the optimization layer recommend (which items, when, how deep, how fast) and against what objectives (margin recovery vs leftover inventory vs revenue)?
6. How does markdown relate to inventory (unsold units, aging, season end; revaluation consequences)?
7. What lifecycle/states do markdown recommendations pass through (generate → review → approve → distribute)?
8. What rules matter (min/max depth, time between markdowns, no-touch windows, price ladders, margin floors, group coherence, budgets)?
9. What interfaces do users work in (run workbenches, recommendation tables, sell-through dashboards, exception lists)?
10. Who uses it (pricing analysts, buyers, merchandisers, planners)?
11. Where are the boundaries vs the two sibling levers and vs inventory/planning/dynamic-pricing Types?

## Representative Products

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Oracle Retail Lifecycle Pricing Optimization Cloud Service (LPO) + Retail Pricing Cloud Service (RPCS) | enterprise suite; optimization-run-centric markdown recommendations (LPO) over a clearance-event management spine (RPCS) | large chains | only sampled vendor with deep Tier-1 operational docs; separates optimization from management exactly as the sibling passes observed |
| Revionics (Aptos) | optimization-led pure-play markdown (cadence/depth AI) | enterprise retail | the "science-led" lifecycle-pricing philosophy; markdown as one of three levers |
| DemandTec | forecast-led markdown schedules on the same demand model as base price/promotions | grocery-centric retail | schedule-first philosophy ("each step earns its depth"); same-model coherence claim |
| Competera | AI/competitive-data-led markdown waves at SKU level | enterprise omnichannel | wave/campaign philosophy; SKU-level vs blanket-discount framing; explicit sell-through-goal FAQ |

Rejected/abandoned samples:
- Blue Yonder (historical "Markdown Optimization" category name-holder) — https://www.blueyonder.com/solutions/markdown-optimization returned 404 (also 404s on site paths in both prior sibling passes). Abandoned per network rule; recorded as source-access limitation.
- Competera's old domain competera.net/solutions/markdown-optimization returned 404; live site found at competera.ai (used).

## Sources

Fetched 2026-09-10:

- Oracle Retail Lifecycle Pricing Optimization Cloud Service User Guide 26.2.301.0 (docs.oracle.com, Tier-1):
  - Ch.1 Lifecycle Pricing Optimization — https://docs.oracle.com/en/industries/retail/retail-lifecycle-pricing-optimization-cloud/26.2.301.0/pooug/offer-optimization.htm
  - Ch.2 LPO Workflow and User Roles — https://docs.oracle.com/en/industries/retail/retail-lifecycle-pricing-optimization-cloud/26.2.301.0/pooug/lpo-workflow-user-roles.htm
  - Ch.5 Promotion/Markdown What-If Run — https://docs.oracle.com/en/industries/retail/retail-lifecycle-pricing-optimization-cloud/26.2.301.0/pooug/markdown-promotion.htm
- Oracle Retail Pricing Cloud Service — Clearance Overview (user guide, docs.oracle.com, Tier-1): fetched 2026-09-07 by the retail-pricing-management pass; content cross-referenced from research/retail-pricing-management.md (Product Observations §Oracle RPCS).
- Revionics — https://www.revionics.com/solutions/markdown (Tier-2 product page)
- DemandTec — https://www.demandtec.com/markdowns (Tier-2 product page)
- Competera — https://competera.ai/solutions/by-need/markdown-optimization (Tier-2 product page)

Not reachable / not sampled: Blue Yonder markdown (404, see above); SAP markdown offerings (help portal JS-shell per sibling passes); Revionics AI Markdown Optimization data sheet (gated resource).

---

## Product Observations

### Oracle Retail Lifecycle Pricing Optimization Cloud Service (Tier-1, evidence layer A)

**Definition (Ch.1):**

- "Markdown is a permanent reduction in the item's price, typically for clearance or end-of-life management, based on forecast data and configurations."
- "Markdown pricing recommendations in LPO help retailers clear aging inventory efficiently by providing optimal markdown recommendations to minimize margin erosion while maximizing sell-through."
- Examples given: "Marking down winter coats at the end of the season to clear inventory or permanently reducing the price of a slow-moving snack brand."
- Contrast definitions in the same chapter: regular price = "the initial price for a new item or a regular price update"; promotion = "a temporary reduction in the item's price to drive sales."
- "You can optimize promotions and markdowns to achieve higher in-season sell-through and potentially increase revenue and/or gross margin throughout the product's lifecycle."
- "By strategically controlling the timing and depth of these recommendations, you effectively manage inventory throughout the product lifecycle."
- Business values: maximize profit "from new item introduction to final clearance"; improve inventory turnover ("timely sell-through and minimizing the need for heavy end-of-season discounts"); localized markdown for an under-performing size/color "while keeping stronger-performing variants at full price"; weekly updates based on new sales, inventory levels, competitor pricing; exception-based retailing.

**Run-centric workflow (Ch.2 + Ch.5):**

- The unit of work is an optimization *run* (batch, typically weekly, or user-initiated what-if). Run stages: Scope → Business Rules → Results → Forecasting.
- Scope: season, department (or higher), company/location (or higher), effective week, price zone, strategy; objectives: Max Revenue, Max GM Amount, Max Revenue with Salvage, Max GM Amount with Salvage; budget constraints (total or separate promo/markdown budgets; allocation schemes: batch, optimally, inventory-value, custom percentages).
- Review Information panel: item counts and *unsold inventory units* by product-hierarchy processing level; "unsold inventory is the sum of all configured inventory components (such as on order, allocated, warehouse, in transit, and so on)."
- Recommendation lifecycle: batch recommendations land in "Ready for Review" → pricing analyst reviews (accept/reject/override) → "Reviewed" → routed to buyer → "Submitted" or "Approved" → sent to export interface and web service to a price execution system (e.g., Oracle Retail Price Management, Customer Engagement). What-if runs can be finalized to replace batch recommendations.
- Roles: Pricing Analyst (day-to-day recommendations), Pricing Manager (analytical super user), Pricing Administrator, Buyer ("owns departments, submits/approves/rejects recommendations, and oversees integration with RPM/CE"), Targeted Offer User, Regular Price User. Data-level security (merchandise/location scoping) + role-based privileges + status-based locks (cannot modify recommendations once reviewed/submitted/approved; cannot modify runs while running; administrators cannot delete runs with approved/submitted recommendations).
- Optimization setup at price zone or location node (not both simultaneously); recommendations generated at recommendation level: location/price zone, merchandise level (e.g., style/color), calendar level (week), customer segment level (targeted offers).

**Markdown rules (Ch.5, Rules — Markdown tab):**

- Markdown Start Day (when markdowns can begin within a week; e.g., Thursday).
- Min/Max First Markdown Discount; Min/Max Other Markdown Discount (per-step depth bounds, computed off the current ticket price); Max Absolute Markdown Discount (cap off full price for the season); worked example shows second-markdown range constrained by both the per-step bounds and the absolute cap.
- Min Time Between Markdowns (in periods/weeks; e.g., a four-week minimum in a four-month season allows roughly one markdown per month).
- Max No. of Markdown Weeks (defaults to total weeks in the season).
- Daily Weights (spread weekly forecast into daily forecasts).

**Sell-Through Target rules (Ch.5):**

- Target Sell-through per period per merchandise level (0–100%); "Sell-through target at end of Clearance Season" (the last markdown-eligible period; example default 85%) and "Sell-through target at end of Regular Season."
- "All Sell-through Targets are enforced as Hard?" — if hard, "the optimization will not return any solution" unless targets are met.
- Product Exit Date ("the date by which an item is expected to stop selling") and Product Start Date.
- Salvage Value (%) — "Salvage value percentage multiplied by the full price of the item" — the value of unsold leftovers, feeding the "with Salvage" objectives.
- Period Pricing Type per period: Promotion Allowed / Markdown Allowed / Ineligible.

**Temporal rules:** No Touch After Landing (price cannot change from initial full price until N weeks after the item starts selling); No Touch at End of Life (price cannot change during the last N weeks before the exit date); max/min markdown items per period.

**Price Ladder:** ladders typed for Promotions (P) or Markdowns (M); "percentage ladder (off full price or current ticket price) or a price-point ladder"; assigned at merchandise levels.

**Pricing Groups (markdown-relevant types):** Markdown All or Nothing (all items marked down together if any one is, discounts may differ); Same Markdown Discount (marked down together AND same discount; recommended prices may differ); Same Promotion and Markdown Discount; Markdown Nothing (no markdowns ever for the group).

**Results (Ch.5):**

- Six tiles: Revenue, Gross Margin, Sell-Through, Promotion, Markdown, Targeted. "Optimal" = percentage gain/loss vs staying at the current price.
- Markdown tile: system-recommended markdowns vs user-added markdowns; accept/reject/override per item for the effective week; add a markdown for non-recommended items.
- Item Details panel: Ticket Price, Recommended Price, plus Price Path, Sales Path, Inventory Path, Gross Margin Path graphs; price types color-coded (no-promo price, markdown, planned event); Projected Budget Usage.
- Sales Forecast: "Inventory units represent the total number of unsold inventory units the optimization system is trying to clear"; forecast decomposition into base sales units (at current ticket price), sales units from price changes (promotions/markdowns), sales units from planned events; discount bins; projected end-of-life sell-through; forecast horizon "until the exit date for a product."
- Returns Forecast: forecast return % and amount per class/segment; returns life-to-date.
- Exceptions: sell-through exceptions (end-of-life sell-through below threshold) and returns exceptions (forecast return % above threshold); comments and flags passed forward to the Manage Recommendations screen; example given of overriding a recommendation constrained by a rule.

**Integration:** recommendations exported to price execution systems (ORPM/RPCS, Customer Engagement) via export interface and web service; weekly data refresh (sales, inventory, competitor pricing).

### Oracle Retail Pricing Cloud Service — Clearance (Tier-1, via sibling pass cross-reference)

From research/retail-pricing-management.md (fetched 2026-09-07 from docs.oracle.com):

- "A clearance event is designed to clear out-of-date merchandise and slow-selling merchandise"; "a clearance markdown is considered a permanent price change, and inventory is consequently revalued."
- A clearance group holds markdowns (discount selling price) and resets ("close out the clearance event, setting the item/location combinations back to the last regular retail price").
- Same status machine as price changes (Worksheet/Submitted/Approved/Executed/Rejected/Processing), same conflict checking, same emergency-event mechanism, same zone-level scoping; approved events distributed to downstream selling systems in advance of the effective date.
- "Reset Clearance with Price Change" system option: executing a price change implies the item is no longer on clearance.

Structural takeaway: the *management* side holds the clearance event as a managed price event (markdowns + explicit resets) with permanence semantics that trigger inventory revaluation; the *optimization* side (LPO) generates the when/how-deep recommendations. Two products, one data spine — the same management/optimization split the retail-pricing pass observed.

### Revionics (Tier-2, evidence layer A for product claims)

- Page title: "Markdown Optimization Software for Retail" — "Manage Markdowns for Faster Sell-Through and Better Margins."
- "Reduce waste and generate greater value with AI-driven markdown recommendations."
- "Optimize markdown cadence and depth to capture waning demand and clear out inventory quickly and profitably, avoiding out-of-season dead weight."
- "Market-tuned automatic updates: Dynamic adjustments keep your markdown plans updated for current market conditions and inventory levels across locations throughout the product lifecycle."
- "Tailored by clearance type: Empower efficient and timely planning with intuitive decision support for every markdown, whether end of life, end of season, resets, or clearance."
- "Take the right marks at the right time for maximizing your clearance goals."
- Markdown is one of three solutions (Base Price / Promotions / Markdown) in a lifecycle pricing optimization platform; "20 years of AI learning" (vendor claim); Strategic Pricing Services human-expert layer; owned by Aptos, LLC.

### DemandTec (Tier-2, evidence layer A for product claims)

- Page: "Markdowns — Clearance without margin surprise" (Revenue Optimization suite, alongside Pricing and Promotions).
- "Clearance on the same demand model that sets everyday price — not a bolted-on tool. Forecast-led schedules that hit the sell-through date by design, and give away only the margin they have to."
- Markdown schedule illustration: 20% Wk 1–2 → 30% Wk 3–4 → 50% Wk 5–6; "Each step earns its depth"; "Projected sell-through by target date — 82% projected · adjusts as actuals land"; "Recovery — ahead of model."
- "A markdown schedule is a sequence of pricing decisions under a deadline. The forecast projects sell-through at each step, so the schedule holds shallow while it can and cuts deeper only when the date demands it."
- Three capabilities: (1) Forecast-led markdown schedules ("the demand model projects how each step will sell, so the schedule takes the depth the sell-through date requires — and no more"); (2) Dynamic Rules & Constraints ("price endings, minimum margins, and step logic enforced on every markdown"; vendor-cited "40+ rule types," the same rule engine that governs base price); (3) Revenue Intelligence & Post-Evaluation ("Every clearance event evaluated after the fact — recovery achieved vs. modeled — so next season's schedule starts smarter").
- Promises: "Sell-through on time, margin protected, price image intact"; "no end-of-season write-down nobody saw coming"; "Clearance runs inside the same rules as everyday price, so it never undercuts the category's standing."
- "Markdowns ships as part of Revenue Optimization, so clearance never fights the base price or the promo calendar — all three run on one demand model, in one workflow."
- Vendor-cited figures (not verified): 82% of merchants spend 10+ hours/week on manual pricing/promotion work; 90%+ forecast accuracy; 40+ rule types; 7,800+ connected CPG partners.

### Competera (Tier-2, evidence layer A for product claims)

- Page: "Markdown optimization for enterprise retailers" — "Reduce excess inventory and protect gross margin with markdown optimization that works at the SKU level... plan, test, and execute markdown campaigns."
- Definition: "Markdown optimization is the process of deciding when to discount a product, how much to reduce the price, and which products belong in each campaign." "It's not about simply clearing inventory. It's about balancing sell-through, revenue, and margins."
- Blanket vs SKU-level: "Blanket discounts are still widely applied... products rarely behave the same way. Some need deeper discounts to sell. Others don't need a markdown at all." "Applying the same markdown across an entire category often means giving away margin where it isn't necessary."
- Waves: "Rather than applying one large markdown, retailers usually introduce discounts in planned waves. Prices are reduced only when products fail to meet the expected sales pace." "A well-designed markdown pricing strategy gives every product the opportunity to sell at the highest possible price before moving to the next discount level."
- Timing: "An inventory markdown launched too early reduces margin. Waiting too long results in aging stock that becomes even harder to sell." Demand forecasting + elasticity modeling "support dynamic markdown pricing that adapts as inventory levels and demand change."
- Challenges named: which products to discount, when, how far; no visibility into outcomes before execution; campaigns that can't adapt mid-cycle; markdown isolated from the rest of pricing ("promotions undermine markdowns, price positioning is compromised"); scaling across channels/markets.
- Use cases: End-of-season clearance (planned waves instead of deepest markdown from day one); Lifecycle-triggered markdowns ("discounts are triggered by product performance and lifecycle stage rather than fixed calendar dates"); Overstock reduction (focus on products that actually need adjustments).
- Features: Goal-driven markdown waves ("products move to the next discount level only when the required performance indicator is reached"); What-if simulation before execution; Dynamic product assignment (auto-assigns SKUs to campaigns based on price elasticity, lifecycle stage, inventory level, past performance, business goals); AI-powered demand-based repricing; Unified with base and promo pricing; Repricing limits and margin guardrails ("price floors, minimum margins, and other business rules before optimization begins").
- FAQ: "The typical goals include end-of-season clearance, hitting the stock level, reaching a particular turnover rate, or protecting margins."
- Vendor-cited figures (not verified): 95%+ prediction accuracy; 2–5pp gross-margin uplift; 3–7% revenue growth; 50–70% less manual pricing work. Gartner citation: "Representative Vendor in 2024 Market Guide for Retail Pricing & Markdown Optimization" (vendor-cited).

---

## Cross-product Comparison

| Structure / capability | Oracle LPO (+RPCS) | Revionics | DemandTec | Competera | Layer |
|---|---|---|---|---|---|
| Markdown = permanent reduction for clearance/end-of-life | A (explicit definition; RPCS: "permanent price change, inventory consequently revalued") | A (clearance types incl. end of life; "avoiding out-of-season dead weight") | A ("clear the season"; clearance schedules) | A ("when to discount, how much, which products"; clearance use cases) | B |
| Item × location/zone scoping | A (item × price zone/location; recommendation level style/color × zone) | A ("across locations") | implied (stores + digital) | A (stores, regions, eCommerce channels) | B |
| Successive markdown steps (ladder/waves/step-downs) | A (price ladders P/M typed; min/max per-step discounts; min time between markdowns; max markdown weeks) | A ("markdown cadence and depth") | A (20%→30%→50% schedule; "each step earns its depth") | A (planned waves; "next discount level only when the required performance indicator is reached") | B |
| Sell-through targets as the yardstick | A (per-period targets, hard/soft enforcement, end-of-clearance-season target, product exit date) | A ("faster sell-through") | A ("hit the sell-through date by design"; projected sell-through adjusts as actuals land) | A ("prices are reduced only when products fail to meet the expected sales pace"; sell-through goals FAQ) | B |
| Inventory position of items being cleared | A (unsold inventory units/value by hierarchy; inventory path; "unsold inventory units the optimization system is trying to clear") | A ("inventory levels across locations") | A (implied: sell-through vs stock) | A (inventory level as assignment input) | B |
| Clearance deadline / exit date | A (product exit date; no-touch at end of life; forecast horizon until exit) | A ("avoiding out-of-season dead weight") | A ("sell-through date by design"; "under a deadline") | A (end-of-season clearance goal) | B |
| Optimization/recommendation engine (when/how deep/which items) | A (core: optimization algorithm over forecast inputs; batch + what-if runs) | A (core: AI-driven markdown recommendations) | A (forecast-led schedules) | A (core: AI recommendations, dynamic product assignment) | B |
| Demand forecast / elasticity as input | A (forecast configuration prerequisite; forecast decomposition base vs price-change vs planned-event) | A ("capture waning demand"; AI learning) | A ("same demand model that sets everyday price") | A (demand forecasting + elasticity modeling) | B |
| What-if / simulation before commit | A (what-if runs; recalculate after overrides) | not observed on fetched page | not observed on fetched page (post-evaluation observed) | A (what-if simulation before execution) | B |
| Human review / approval of recommendations | A (Ready for Review → Reviewed → Submitted/Approved; analyst + buyer roles; status locks) | not observed | not observed | A ("retailers stay in control... define the objectives and business constraints"; guardrails) | B (governance depth varies) |
| Distribution to selling systems | A (export interface + web service to price execution system, e.g., RPCS/ORPM, CE) | implied (feeds retailer systems) | A ("flighted" context from sibling pass; module page implies execution) | implied (campaign execution) | B |
| Rules/guardrails on depth & cadence | A (min/max discounts, min time between markdowns, absolute cap, start day, no-touch windows) | not observed in detail | A (price endings, minimum margins, step logic; "40+ rule types") | A (price floors, minimum margins, repricing limits) | B |
| Group coherence (items marked down together / same discount / never) | A (Markdown All or Nothing / Same Markdown Discount / Markdown Nothing pricing groups) | not observed | not observed | not observed (dynamic product assignment is the individual-SKU counterpart) | A→product-specific |
| Budget for markdown spend | A (total or separate promo/markdown budgets; allocation schemes) | not observed | not observed | not observed | A→product-specific |
| Salvage value of unsold leftovers | A (salvage % × full price; "with Salvage" objectives) | not observed | not observed | not observed | product-specific |
| Post-evaluation (recovery achieved vs modeled) | A (results tiles vs staying at current price; exceptions) | not observed | A ("recovery achieved vs. modeled — so next season's schedule starts smarter") | A (performance tracking; measurable capability framing) | B |
| Markdown isolated vs unified with base/promo pricing | A (one run family; separate rule sets) | A (one of three levers on one platform) | A ("all three run on one demand model") | A ("unified with base and promo pricing") | B |
| Clearance types (EOL / end-of-season / resets / overstock) | A (RPCS resets; LPO end-of-life machinery) | A (end of life, end of season, resets, clearance) | A (seasonal sets) | A (end-of-season, lifecycle-triggered, overstock) | B |
| Returns interaction | A (returns forecast; returns exceptions) | not observed | not observed | not observed | product-specific |
| Competitive data as input | A (weekly refresh incl. competitor pricing) | not observed | not observed | A (competitive-data platform heritage) | B |
| Explicit reset-to-regular-price action | A (RPCS resets; "Reset Clearance with Price Change" option) | A (resets named as a clearance type) | not observed | not observed | B (thin but multi-product) |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as a markdown optimization application:

1. **The markdown as a managed permanent price reduction** — identified items (item × location/zone) carry a price reduction that is permanent in kind: it is not time-boxed and does not restore automatically at an event's end (an explicit reset/superseding decision is a separate act), and it is bound to a clearance/end-of-life intent — aging, seasonal-end, or excess stock. The permanence is what carries the inventory-accounting consequence (revaluation of the remaining stock at the reduced price).
2. **The markdown schedule** — the reduction is planned as successive steps over the item's remaining life (ladder/wave/step-down), each step with a depth and a timing, constrained by rules (depth bounds, minimum time between steps, caps), moving the item from full price toward clearance.
3. **The sell-through-driven decision loop against a clearance deadline** — which items to mark down, when, how deep, and how fast are decided against sell-through/inventory performance measured against targets and an exit date; the decision may be made by human judgment on sell-through reports (historical form) or by a forecast/AI recommendation engine (modern form), but the loop — observe pace → adjust the next step — is the Type's working heart.

Remove #1 → a temporary-event tool (promotion management) or an everyday-price tool (pricing management). Remove #2 → one-off clearance price cuts with no schedule discipline. Remove #3 → a static markdown calendar or a price-change tool with a clearance flag; the "optimization" center of gravity lives in #3.

Jointly-held load-bearing: 1 alone = a price-change tool with a clearance flag (pricing-management territory); 2 alone = a step-down calculator; 3 alone = sell-through analytics with no price action; 1+2 without 3 = a fixed markdown calendar (the pre-optimization form); 1+3 without 2 = ad-hoc clearance cuts (atypical); 2+3 without 1 = a discount scheduler with no permanent-price semantics (promotion/dynamic-pricing territory).

Binding: the retailer's own aging/seasonal/excess inventory being cleared through permanent price reductions on the retailer's items. Remove the binding → generic price optimization.

### L1 — Common Mature Structure

Very common in mature modern products but not required to define the Type:

- demand forecast / elasticity model as the estimation engine behind recommendations
- optimization runs or campaign waves as the unit of planning work (batch + what-if)
- item-level recommendations with accept/reject/override and a review → approve → distribute lifecycle
- distribution of approved markdowns to selling systems (POS price files, e-commerce) ahead of effective dates
- rules/guardrails: price floors, minimum margins, price endings/price points, depth caps, step logic
- what-if simulation and projected metrics (revenue, margin, sell-through) before commit
- projected sell-through vs target, recalculated as actuals land; in-season adjustment
- post-evaluation (recovery achieved vs modeled) feeding the next season's plans
- exception handling (sell-through below threshold, returns above threshold)
- unified operation with base price and promotions on one data/demand spine
- roles and governance (analyst reviews, buyer approves; data scoping by merchandise/location)

### L2 — Variant / Optional Structure

- optimization-run-centric form (recommendations generated by an engine over rules) vs schedule/rules-centric form (human-authored schedules enforced by a rule engine) vs wave/campaign form
- clearance-type specialization: end of life, end of season, resets, overstock reduction
- group coherence machinery (all-or-nothing, same-discount, never-mark-down groups)
- markdown budgets as a constrained resource (with allocation schemes)
- salvage-value modeling of unsold leftovers in objectives
- returns forecasting integrated into markdown planning
- competitive data as an input to markdown timing
- lifecycle-triggered (performance-triggered) vs calendar-fixed markdown triggers
- channel-localized markdowns (stores, regions, e-commerce)
- human expert/consulting services wrapped around the platform
- where the management record lives: inside a pricing suite's clearance events vs a standalone optimization layer feeding it

### L3 — Vendor-specific Structure

(kept out of the final document; examples) Oracle: run types (batch/what-if), DEFAULT_SET strategy, rules tabs (Temporal/Planned Events/Promotion/Markdown/Sell-Through Target/Price Ladder/Pricing Groups/Budget), recommendation statuses (Ready for Review/Reviewed/Submitted/Approved), auto-approval criteria and frequency rules (regular pricing), salvage-value %, product exit date, no-touch windows, RPCS clearance groups with resets, "Reset Clearance with Price Change" option, interface tables (PRO_SEASON_PERIOD_STG etc.), Artie digital assistant. Revionics: "20 years of AI learning," Strategic Pricing Services, Aptos ownership. DemandTec: "Commercial Trade Intelligence" framing, "each step earns its depth" schedule illustration, "40+ rule types" claim, shared-demand-model coherence claim. Competera: named feature set (goal-driven waves, dynamic product assignment, guardrails), 95%+ accuracy / 2–5pp uplift / 3–7% growth claims, Gartner Market Guide citation, ISO 27001 badge.

## Vendor-specific Findings

- All numeric claims on vendor pages (95%+ accuracy, 2–5pp uplift, 90%+ forecast accuracy, 40+ rule types, 82% of merchants, 7,800+ partners) are vendor-cited marketing figures — recorded here, not promoted to the final document.
- Competera's Gartner "Market Guide for Retail (Unified) Price, Promotion and Markdown Optimization Applications" citation is vendor-cited; used only as evidence that the market frames a unified price/promo/markdown category (see Boundary Findings #8).
- Oracle's example defaults (e.g., 85% end-of-clearance-season sell-through target, Thursday markdown start day) are documentation examples of configurable values, not industry standards.
- Oracle splits markdown into a management service (RPCS clearance events) and an optimization service (LPO) — an architectural fact of one vendor; other vendors deliver both in one product.

## Boundary Findings

1. **vs Retail Pricing Management (§05.14 sibling)** — pricing management owns the everyday/base price; markdown is a *permanent reduction for clearance/end-of-life* with inventory revaluation. Sampled products co-deliver the levers on one platform (Oracle RPCS carries clearance events; Revionics/Competera/DemandTec unify the levers), but the markdown leaf owns the clearance center of gravity. Test: remove the clearance/end-of-life intent → pricing management. (Consistent with research/retail-pricing-management.md.)
2. **vs Promotion Management (§05.14 sibling)** — promotion is a *temporary* reduction (price restored at event end); markdown is permanent (no automatic restore; reset is a separate explicit act). Oracle defines the two in one sentence pair; DemandTec runs them as separate modules on one forecast ("clearance never fights the promo calendar"). Test: restore the full price when the event ends → promotion.
3. **vs Inventory Management / Retail Inventory (§05.12/§10)** — markdown optimization *consumes* inventory data (unsold units, aging, inventory value, inventory path) but does not own stock records, replenishment, or stock movements; its lever is price, not stock. Test: remove the price lever → inventory analytics/planning.
4. **vs Merchandise Financial Planning (§05.13-adjacent planning)** — planning owns the markdown-dollar plan at category/season level (a budget line); markdown optimization executes item-level price decisions within such constraints. Oracle's budget machinery shows the seam (markdown budgets as run inputs). Test: remove item-level price decisions → planning.
5. **vs Dynamic pricing / commerce repricing engines** — dynamic pricing adjusts prices continuously for competitiveness; markdown optimization clears aging inventory in planned permanent steps toward a deadline. Test: remove the clearance/end-of-life intent and the step-down schedule → dynamic pricing.
6. **vs POS / e-commerce selling systems (§05.10/§05.01)** — execution surfaces sell at the marked-down price; markdown optimization decides the reductions upstream and distributes them ("passing approved price events onto downstream selling systems" — RPCS). Downstream consumer vs upstream owner.
7. **vs Competitive Intelligence Platform (§06)** — competitive data is an *input* (Oracle refreshes competitor pricing weekly; Competera's heritage); the output here is markdown price decisions, not market insight. Test: output is insight only → competitive intelligence.
8. **Taxonomy note (joint review)** — the three §05.14 siblings (retail-pricing-management / promotion-management / markdown-optimization-application) are three levers of one platform family in the current market (Gartner "Retail Unified Price, Promotion and Markdown Optimization Applications" category name cited by Competera; Revionics lifecycle platform; Oracle LPO+RPCS spine; DemandTec Revenue Optimization). All three leaves are now processed; boundaries held structurally by lever (everyday price / temporary event / permanent clearance). The joint-review recommendation recorded by both sibling passes can be considered actionable from this side; no conflict found that would merge the leaves.
9. **vs Retail Loss Prevention / Shrink (§05.25)** — both touch "inventory loss," but shrink is unplanned loss; markdown is a planned price lever. No structural confusion observed.

## Historical / Market-Sample Check

Would older, regional, or platform-native products still fit the L0? Yes:

- Paper-era markdown: a buyer with end-of-season goods reads sell-through reports, takes 25% off, watches pace, takes 50% off the leftovers, and finally clears at 75% — a permanent reduction (recorded as a price change; inventory revalued at period end), a step-down schedule, and a sell-through-driven loop against a season-end deadline. All three L0 legs hold with no software beyond ledgers and reports.
- Legacy merchandising systems of the pre-optimization era carried clearance/markdown price-change types with effective dates, distributed to POS, with revaluation interfaces to finance — markdown event + schedule + distribution, without AI.
- Fixed-calendar "auto markdown" policies in fashion retail (fixed step-downs on fixed dates) satisfy legs 1–2 in the degenerate form noted in the load-bearing analysis; the sell-through loop is what distinguishes *optimization* from *calendar*.
- Regional practices (e.g., European sale-period regimes with legally defined sale windows) change the calendar around the loop, not the loop itself.

The L0 therefore does not over-fit to the current AI-optimization era. Conversely, the modern samples' shared features (forecast engines, what-if simulation, recommendation lifecycles, post-evaluation) are L1, not definition.

## Uncertainties

- Blue Yonder — the historical "Markdown Optimization" category name-holder — could not be reached (404 in this pass and in both sibling passes); its structure is unverified. The enterprise-optimization picture rests on Oracle (Tier-1) + Revionics/DemandTec/Competera (Tier-2).
- Revionics, DemandTec, and Competera evidence is Tier-2 (official product pages, no operational docs); no field-level or status-level claims were taken from them beyond what their pages state. Their approval-workflow internals, if any, are unobserved.
- Whether inventory revaluation is always triggered through the markdown system itself or in downstream merchandising/finance systems is only partially observed (Oracle RPCS states the consequence explicitly; other vendors' pages are silent). Treated as a semantic consequence of permanence, not a separately-owned object.
- The relative market weight of the optimization-run pole (Oracle), the schedule/rules pole (DemandTec), and the wave/campaign pole (Competera) is unclear from this sample; all three philosophies documented, no market-share claim made.
- Group-coherence machinery (all-or-nothing/same-discount groups) was observed only at Oracle; treated as product-specific-leaning-optional, kept out of L1.
- Salvage-value modeling and returns-forecast integration were observed only at Oracle; kept as L2/product-specific.
- The exact relationship between "resets" and season boundaries (when a reset is required vs optional) is documented only at Oracle RPCS; generalization avoided.

## Final Synthesis

Markdown Optimization Application is the retailer-side application that clears aging, seasonal-end, and excess inventory through permanent, scheduled price reductions. Its defining core is three jointly-held structures: the markdown as a managed permanent price reduction on identified items bound to a clearance/end-of-life intent (permanence being what distinguishes it from promotions and what carries the inventory-revaluation consequence), the markdown schedule (successive steps — ladder/wave/step-down — with depth and timing constraints moving the item from full price toward clearance), and the sell-through-driven decision loop against a clearance deadline (which items, when, how deep, how fast — decided against sell-through targets and exit dates, whether by human judgment on sell-through reports or by forecast/AI recommendation engines). Around this core, mature products add demand forecasting and elasticity estimation, optimization runs or campaign waves with what-if simulation, item-level recommendation lifecycles (review → approve → distribute to selling systems), guardrails (floors, margins, price endings, depth caps), in-season adjustment as actuals land, and post-evaluation of recovery achieved vs modeled. The Type sits beside its two sibling levers — pricing management owns the everyday price the markdown starts from; promotion management owns temporary events that restore — and upstream of the selling surfaces that execute the marked-down prices, while consuming inventory data it does not own. The market realization spans an optimization-run pole, a schedule/rules pole, and a wave/campaign pole, increasingly unified with base price and promotions on one demand/data spine.
