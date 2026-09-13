# Research Notes — Sales Pricing Application

Research date: 2026-09-07
Evidence layers: **A** = directly observed on an official product source; **B** = cross-product commonality across the sampled set; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Research Goal

Understand what a **Sales Pricing Application** (directory leaf §07 Sales, sitting between Configure Price Quote / CPQ and Deal Desk / Commercial Approval Platform) actually is as a class of software: who runs it, what objects exist inside it, how the price-setting→release→selling→analysis cycle flows, which rules govern it, and where the Type ends relative to CPQ (quote-time pricing engine), Deal Desk (approval process), Retail Pricing Management (§05.14), ERP price masters, billing, and sales analytics.

This pass also discharges the joint-review flag recorded by the CPQ pass: *"sampled CPQ products embed a pricing engine (computation at quote time), not a pricing management discipline (price-setting, elasticity, market data). Flag for joint review: where 'Sales Pricing Application' ends and the CPQ-embedded pricing engine begins."*

## Initial Boundary

Working hypothesis before research:

- Core use: the selling organization's prices — what may be charged for each product, to which customers, under which conditions — are defined, governed, changed, and distributed from one place, instead of living in spreadsheets and ad-hoc overrides.
- Users: pricing managers/analysts/pricing teams; secondarily sales leadership and sellers (as consumers of prices/guidance); admins/integration engineers.
- Nearest neighbors: CPQ (quote-time engine consuming prices), Deal Desk (approval of commercial commitments), Retail Pricing Management (retail-side price files/promotions), ERP price condition records (storage/execution), Billing (money collection), Sales Forecasting / Revenue Intelligence (projections), FP&A (planning models).
- Unknowns: whether "sales pricing" is really the market category (analyst names suggested "price optimization and management"); how quote-time guidance and agreements fit; whether approval machinery is definitional or a Deal Desk seam.

## Research Questions

1. What is the central object — a price record? a price list? a strategy? a waterfall?
2. What is the canonical lifecycle of a price: inputs → strategy/rules → computed prices → review → publish → sell → analyze?
3. How do sellers consume prices at deal time, and how is deviation governed (floors, guidance ladders, approvals)?
4. What analytics close the loop (realization, waterfall/margin bridge, discount leakage, price-volume-mix)?
5. What is published where (ERP/CRM/CPQ/e-commerce/dealer networks), and what is the boundary vs the ERP price master?
6. Which capabilities are definitional vs common vs variant (optimization AI, agreements, rebates, market data, agreements/contracts)?
7. Where is the boundary vs CPQ, Deal Desk, Retail Pricing Management, Billing, and revenue-management (perishable-inventory yield) systems?

## Representative Products

Selected for market representativeness, documentation quality, distinct product philosophies, and distinct customer/industry poles:

| Product | Philosophy / pole | Evidence tier |
|---|---|---|
| **Zilliant** | Sales-guidance-led B2B pricing (Price Manager + Price IQ + CPQ + Agreements) | Tier-1 product documentation (docs.zilliant.com), 6 pages |
| **Pricefx** | Cloud-native standalone pricing platform ("pricing is our only focus") | Tier-1 knowledge base (knowledge.pricefx.com) + Tier-2 capability pages |
| **Vendavo** | Enterprise margin/profit-led platform (pricing + quoting + rebates + analytics) | Tier-2 product/solution pages (vendavo.com), rich |
| **Syncron** | OEM aftermarket / service-parts pricing pole | Tier-2 product pages (syncron.com) |
| **PROS (B2B line)** | AI/science heritage pole — B2B business now under Conga | Structural only: pros.com homepage banner "PROS B2B is now Conga!"; product surfaces unreachable (403 ×2) |

Analyst-category context observed on vendor pages (Layer A quotes): IDC MarketScape "Worldwide B2B price optimization and management applications"; Gartner Magic Quadrant "B2B Pricing and Rebate Optimization Software"; QKS SPARK Matrix "B2B Price Optimization & Management". The directory leaf maps to the market's **Price Optimization and Management (POM)** category.

## Sources

All fetched 2026-09-07.

- Zilliant: https://www.zilliant.com/ ; https://zilliant.com/products/price-manager ; https://docs.zilliant.com/ ; /docs/about-price-manager ; /docs/about-pricing-engine ; /docs/about-price-iq ; /docs/use-cases-for-price-manager ; /docs/about-agreements ; /docs/enable-pricing-guidance-and-data-in-quotes-and-agreements
- Pricefx: https://www.pricefx.com/ ; https://www.pricefx.com/platform/price-management/ ; https://knowledge.pricefx.com/ ; https://knowledge.pricefx.com/pricefx-unity-documentation
- Vendavo: https://www.vendavo.com/ ; https://www.vendavo.com/platform/pricing/
- Syncron: https://www.syncron.com/ ; https://www.syncron.com/solutions/parts-pricing
- PROS: https://www.pros.com/ (homepage banner only; /b2b and conga.com returned 403 — Source-access Limitation applies)

---

## Product A — Zilliant (Tier-1 docs; evidence layer A)

**Positioning.** "B2B Price Optimization & Management"; product lines: Price Manager, Price IQ, CPQ, Sales Agreements, Sales Insights and Actions.

**Price Manager** (docs "About Price Manager"): "gives pricing teams control over how and when to adjust prices… manage, adjust, and publish prices by using templates and scenarios."

- Use cases (docs): respond to cost changes (import new costs → apply passthrough strategies → review impact → select optimal scenario → **publish new prices**); manage **global list prices** (a baseline per product used as reference for local/customer prices; "review the history of price changes in your base workbook"); currency exchange rates (fixed rate for a period); **country prices** computed as `global list price × exchange rate × country discount`; **region prices** as `global list × exchange × country discount × region discount`; custom templates for price triggers (e.g., competitive data arrival); custom pricing structures registered via a Template Configuration workbook.
- Structure: **base workbook (master data)** → **templates** → **scenarios** → **publish**; price change **history** retained.
- Concept frame: the **pricing waterfall** — "analysis method used to visualize and examine the price transformation process."

**Pricing Engine** (docs "About Pricing Engine"): a **price build** represents the databases associated with a pricing waterfall. Terms: **price elements** (non-calculated waterfall elements: cost, markup, discount), **element lookup** (depth of an element in the waterfall), **lookup keys** (fields that break each lookup into a set), **element values**. Enables **price simulations** to model changes to discounts, costs, or promotional periods and see effects on underlying pricing data.

**Price IQ** (docs "About Price IQ"): "proprietary prediction and optimization engines that generate segment and customer-specific price recommendations from your business data"; answers "what is the optimal price for this product for this customer?" and "how will this price impact volume?" Workflow: configure + create **pricing strategies** → create a **scenario** ("a 'what if' version of a strategy sheet") → apply strategies → **optimize** → **review** → **publish**. Constraints: "enforce rational price relationships, such as minimum margin requirements and good/better/best product relationships." Outputs "immediately published… into CRM, CPQ, ERP, eCommerce, or other commercial systems."

**Agreements** (docs "About agreements"): customer **price agreements** with lifecycle **Under negotiation** (set pricing/discounts) → **Published** ("official, active price records based on which you create transactions like quotes and orders"; not directly editable) → **Revised** (new negotiation → new published revision). Role-based access, approval flows, AI price recommendations from Price IQ.

**Quote-time seam** (docs "Enable pricing guidance and data in quotes and agreements"): Zilliant CPQ attaches pricing guidance and price data to quotes/agreements: **Std. Price/Unit from Price Manager**; **Start / Target / Floor discount from Price IQ**; a computed **Health** indicator (GOOD / MEDIUM / BAD) comparing the manually entered discount to the guidance ladder. Guidance is keyed by product ERP ID × account ERP ID × quantity (+country, currency, UOM) — delivered via a Groovy script calling database formulas inside the pricing schema. This is the concrete mechanism of "pricing application feeds selling system."

**Observation summary (A):** price records under conditions (global/country/region/customer), strategy/scenario-driven setting with simulation, publish step into selling systems, retained price-change history, negotiated agreements as published price records, guidance ladder (start/target/floor) + health at quote time.

## Product B — Pricefx (Tier-1 KB + Tier-2; evidence layer A)

**Positioning.** "Enterprise Pricing Intelligence Platform"; capabilities: Price management, Quoting, Agreements, Promotions, Rebates, Channel Management, AI Optimization, Agents. "Pricefx Price Management works as a standalone capability" — start with price management, expand later.

**Price Management capability page** (A):

- Four-step flow: **Define pricing logic → Simulate and test → Publish prices → Monitor and optimize.**
- "Centralized price repository — eliminate version-control chaos and run from one source of truth for **list, base, and customer prices**."
- "Rule-based pricing logic — encode **markups, indexes, and corridors** as transparent rules — and have them recalculate automatically when costs or competitors move."
- "Scenario simulation — compare strategies side by side and see margin impact before any price goes live."
- "Configurable approval workflows — route any change through the right approvers, with **audit trails** finance can defend."
- "Outlier & performance alerts — see **price realization** versus benchmarks."
- FAQ boundary statement vs ERP: "ERP can store prices, but it typically is not where teams want to design, test, govern, and manage complex price changes… push approved prices back into the systems where execution happens."
- "Pricefx publishes approved prices into ERP, CRM, and CPQ environments."
- Positioning vs spreadsheets: annual price reviews, cost-driven increases, bulk list-price updates.

**Knowledge base** (A): "Pricefx is a SaaS pricing platform which provides Price Management & Optimization and CPQ solutions to cover all pricing processes end-to-end… From gathering insight on pricing data to managing strategy and bringing prices to market." Documentation covers capabilities, administration/data setup, CRM integration options, Groovy API, REST API, IntegrationManager.

**Observation summary (A):** governed price repository (list/base/customer prices), rule-encoded logic with automatic recalculation on cost/competitor movement, simulation-before-publish, approvals with audit, realization monitoring, publication into ERP/CRM/CPQ; explicit anti-spreadsheet and anti-ERP-as-design-tool positioning.

## Product C — Vendavo (Tier-2, rich; evidence layer A)

**Positioning.** "Pricing, quoting, and rebates… unified commercial platform"; industries: manufacturing, distribution, services.

**Platform > Pricing** (A):

- "Centralizes pricing strategy where teams can **set, manage, and control global and local prices** with confidence… governance, collaboration, and execution… across your products, markets, regions, channels, and customers."
- Set: "Operationalize pricing strategies through configurable **rules, formulas, and governance controls**… define pricing logic once and apply it consistently across products, regions, and customer segments… deploy changes across thousands or millions of price points."
- Guide: "market-aligned price guidance, including **floor, target, and stretch recommendations**… reflects how customers perceive value and what they are willing to pay"; "Pricing teams maintain strategic control by adjusting segmentation logic and policies."
- Optimize: "**elasticity modeling**… simulate scenarios to test how price adjustments impact volume, competitiveness, and profitability before deploying changes"; optimization "with guardrails like **floors, thresholds, and approvals**"; constraints "floors, ceilings, rounding, and change limits."
- Lifecycle governance: "Manage **list prices, customer agreements, and channel prices in one governed workflow — from creation to approval to publish**… with full auditability and clear ownership… **effective-dating** and controlled rollouts… execute price increases, regional updates, and contract renewals on time — without breaking downstream systems."
- Analytics: "price, volume and mix on margins"; "margin bridge analysis and pricing analytics"; compliance monitoring.
- Negotiated-deal support (FAQ): "calculates target, floor, and stretch prices that guide negotiations… pricing teams retain governance through policies and business rules."

**Observation summary (A):** same skeleton as A/B with explicit effective-dating, approval-to-publish governance, guardrailed optimization, and floor/target/stretch guidance; strong margin-bridge analytics emphasis.

## Product D — Syncron (Tier-2; evidence layer A)

**Positioning.** Aftermarket/service-parts pricing for equipment OEMs and dealer/distributor networks.

**Service Parts Pricing** (A):

- "Dynamic Pricing Management — pricing logic, **approval workflows**, and automation."
- "AI-driven segmentation… group parts and customers based on behavior and market dynamics."
- "Intelligent Pricing Analytics — competitive analysis, **price volume mix**, and modeling tools."
- "Multiple Model Support — price models that fit your business needs and maturity: **cost-plus, value-based, or competitor-based**."
- "Aftermarket-informed Pricing Options — **kit-based, lifecycle, and supersession pricing**."
- "Defensive Price Harmonization — limit grey market and cannibalization risk with targeted harmonization rules."
- FAQ: "Service parts pricing is the process of **setting and managing prices** for spare parts across products, markets, channels, and customer segments… When selling through dealer networks, OEMs must optimize pricing to safeguard their profits while allowing for dealer margin."
- Integration with parts planning and warranty solutions (stocking/claims data feeding pricing intelligence).

**Observation summary (A):** the same governing skeleton (logic + approvals + automation + analytics + segmentation + multiple strategy models) realized for the aftermarket pole, where prices flow to dealer networks and pricing semantics are part/lifecycle-specific.

## Product E — PROS B2B → Conga (structural only; evidence layer A, minimal)

- pros.com homepage banner (A): "**PROS B2B is now Conga!** — The same trusted solutions, now under a new name." The remaining pros.com site is airline offer/revenue management (a different Type: perishable-inventory revenue management).
- /pros.com/b2b and conga.com returned 403 (2 attempts each surface). No product-internal claims made. Used only as market-consolidation context; the AI/science heritage pole is acknowledged but not modeled from direct evidence.

---

## Cross-product Comparison

| Structure | Zilliant | Pricefx | Vendavo | Syncron | Strength |
|---|---|---|---|---|---|
| Centralized, governed price records (product × conditions; list/base/customer prices) | ✔ (global/country/region/customer prices; base workbook) | ✔ ("one source of truth for list, base, and customer prices") | ✔ ("set, manage, and control global and local prices") | ✔ (parts prices per market/channel/segment) | **B** — universal |
| Price-setting logic/strategy (rules, formulas, strategy models: cost-plus / market-competitor / value-based) | ✔ (templates, strategies, passthrough) | ✔ (markups, indexes, corridors) | ✔ (rules, formulas, value-based guidance) | ✔ (cost-plus, value-based, competitor-based) | **B** — universal |
| Simulation / what-if before release | ✔ (scenarios; "compare… which scenario yields the best overall results") | ✔ ("see margin impact before any price goes live") | ✔ ("simulate scenarios… before deploying changes") | ✔ (pricing simulations) | **B** — universal |
| Approval / governance with audit | ✔ (approval flows; role-based access) | ✔ (configurable approval workflows; audit trails) | ✔ (creation→approval→publish; full auditability) | ✔ (approval workflows) | **B** — universal |
| Publish / distribute to selling systems | ✔ ("published into CRM, CPQ, ERP, eCommerce") | ✔ ("publishes approved prices into ERP, CRM, and CPQ") | ✔ ("without breaking downstream systems") | ✔ (dealer/distributor networks) | **B** — universal |
| Realized-price analytics (realization, margin bridge, price-volume-mix, discount behavior) | ✔ (waterfall; history; sales insights) | ✔ (price realization vs benchmarks; outlier alerts) | ✔ (margin bridge; price-volume-mix; compliance) | ✔ (price-volume-mix; competitive analysis) | **B** — universal |
| Quote-time guidance ladder (start/target/floor-style + rationale) | ✔ (Start/Target/Floor discount + Health, A) | ◐ (deal guidance via AI optimization) | ✔ (floor/target/stretch, A) | — | **B-ish** — 2 direct + 1 partial; write as common, names vary |
| Optimization engine (elasticity/AI recommendations) | ✔ (Price IQ, A) | ✔ (AI Optimization, A) | ✔ (elasticity modeling, A) | ✔ (AI segmentation/forecasting, A) | **B** — universal in modern sample; NOT definitional (strategy+rules alone documented as a full operating mode) |
| Customer price agreements/contracts | ✔ (Agreements lifecycle, A) | ✔ (Agreements capability) | ✔ (agreement management; channel prices) | ◐ (dealer pricing relationships) | Common (3/4 direct) |
| Cost-change response / cost passthrough | ✔ (passthrough templates, A) | ✔ (rules recalc when costs move; cost agent) | ✔ (regional updates; cost signals) | ✔ (adapts to cost) | **B** |
| Currency/exchange and country/region derivation | ✔ (formulas, A) | ✔ (regions; corridors) | ✔ (regional updates) | ✔ (markets) | **B** |
| Market/competitor data ingestion | ◐ (custom trigger templates) | ✔ ("any market data feed") | ✔ (market data, competitive insights) | ✔ (competitive analysis) | Common |
| Segmentation (customer/product tiers) | ✔ (segments drive recommendations) | ✔ | ✔ (segmentation logic) | ✔ (AI-powered segmentation) | **B** |
| Retained price-change history / versioning | ✔ (history in base workbook; revised agreements) | ◐ | ✔ (effective-dating; auditability) | ◐ | Common |
| Suite adjacencies (quoting, rebates, promotions, channel mgmt, warranty/planning) | ✔ (CPQ, Sales Insights) | ✔ (Quoting/Rebates/Promotions/Channel) | ✔ (Quoting/Rebates/High-Tech RM) | ✔ (Planning/Warranty) | Variant — suite posture, not Type structure |

Evidence calibrations:
- All **Layer B universal** structures above were directly observed (A) on at least three of the four full samples; several on all four.
- Quote-time guidance: direct A evidence at Zilliant (start/target/floor + health) and Vendavo (floor/target/stretch); Pricefx documents deal-level guidance under AI marketing copy (weaker). Written into the final document as a common capability with varying names, not as a definitional structure.
- Optimization: universal in the current sample but the sampled products equally document rules/strategy-driven operation without optimization as a complete operating mode (Zilliant templates are explicitly strategy+rules; Pricefx FAQ sells price management as standalone). → Common mature structure, not defining.

## Canonical Abstraction

### Level 0 — Defining Invariant

Three structures. Remove any one and the product stops being a Sales Pricing Application:

1. **The governed price record population.** The application holds the selling organization's prices as managed records — a price for an offering under explicit conditions (customer / segment / region / channel / currency / validity), maintained as the source of truth for what the organization may charge. (Remove → prices are data fields inside individual quotes or ERP item masters, or rows in spreadsheets.)
2. **The price-setting-and-release cycle.** Prices are produced and updated by a managed cycle: strategy/rules/models applied to cost, market, and customer inputs → computed or adjusted price changes → simulation/review → approved release (publish, commonly with effective dating) of the records. (Remove → a static price table; or an analytics tool that recommends but never releases prices.)
3. **The selling seam.** The records connect to the selling motion: sellers and selling systems (ERP, CRM, CPQ, e-commerce, dealer/order systems) obtain their prices from this system — directly or via publication — so that what is charged in real deals is governed by it. (Remove → pricing analytics/consulting output that never reaches a transaction.)

Tested against §24 (historical / market-sample check): paper price lists under a price committee, ERP-era pricing condition records, and spreadsheet price books with email approvals all satisfy the three structures — records + a setting/maintenance cycle + distribution into the selling motion. Modern platform shapes (AI optimization, agents, suites) are not needed for the definition. Check passes.

### Level 1 — Common Mature Structure

- Price architecture in layers: list/base price → derived regional/country/customer prices → deal-level guidance; the **price waterfall** as the shared mental model (Zilliant's own documented frame; Vendavo "across the price waterfall").
- Strategy model vocabulary: cost-plus, market/competitor-based, value-based.
- Simulation/what-if comparison of strategies with margin/revenue/volume impact.
- Approval workflows on price changes with audit trails; effective dating.
- Realized-price analytics: price realization, margin bridge, price-volume-mix, discount/leakage analysis; retained price-change history.
- Quote-time guidance (floor/target/stretch-style ladders with rationale) delivered into CRM/CPQ.
- Optimization engines (elasticity, AI) with guardrails (floors, ceilings, rounding, change limits).
- Integration spine: publication/sync into ERP, CRM, CPQ, e-commerce; transaction-data ingestion for realization analysis.
- Segmentation of customers and products; roles (pricing manager/analyst/admin as operators; sellers/leadership as consumers).

### Level 2 — Variant / Optional Structure

- Customer agreements/contracts machinery (negotiated price agreements with negotiation→published→revised lifecycles).
- Market/competitor price-data ingestion ("price intelligence").
- Currency/exchange-rate machinery and country/region price derivation depth.
- Suite adjacencies: quoting, rebates, promotions, channel management (Pricefx/Vendavo), sales insights/campaigns (Zilliant), warranty/parts planning (Syncron).
- Vertical tuning: aftermarket parts semantics (kit, lifecycle, supersession, harmonization), distribution vs manufacturing vs chemicals; high-tech revenue-management packaging.
- Customer tier: mid-market editions vs enterprise platforms.
- Deployment: SaaS (dominant in sample), ERP-adjacent deployments; APIs/CLIs for configuration.
- AI posture: optimization engines, anomaly agents, conversational assistants (era-typical).

### Level 3 — Vendor-specific (research notes only)

- Zilliant: base-workbook/template/scenario model; Pricing Engine price builds (elements/element lookups/lookup keys/element values); Groovy-script guidance binding into CPQ pricing schemas; Health emoji indicator; scenario strategy sheets; published-under-negotiation agreement states.
- Pricefx: Agent template catalog (cost pass-through, discount creep, margin erosion…), PlatformManager/IntegrationManager/Studio, Groovy/Python/REST APIs, accelerators.
- Vendavo: margin-bridge analytics packaging, High-Tech Revenue Management solution, Pricing Assistant conversational AI.
- Syncron: kit-based/lifecycle/supersession pricing, price harmonization rules, SLM platform integration with planning/warranty.
- Marketing-numeric claims (margin basis points, ROI multiples, SKU counts, quote-turnaround percentages) recorded here only — none carried into the final document.

## Rejected Findings

- "A Sales Pricing Application computes prices inside each quote" — rejected as definitional: that is the CPQ-embedded pricing engine. Pricing applications govern **standing** price records released to selling systems; quote-time computation is the consumer seam. (Confirmed from both sides; CPQ pass flag discharged.)
- "Discount approvals are definitional" — rejected: approvals are universal in the sample but attach here to **price changes and deviations**; the cross-functional approval of whole deals is Deal Desk's center. Approval machinery is common-not-core; a deployment can govern prices through publication discipline alone.
- "AI optimization is definitional" — rejected: strategy+rules operation is documented as a complete mode; historical check passes without ML.
- "This Type owns quotes or orders" — rejected: quotes are CPQ's object; orders are order capture's; this Type ends at governed prices + guidance.
- "This is the same as Retail Pricing Management" — rejected as identical: retail pricing centers on store/e-commerce price files and promotional/markdown execution toward shoppers; the sampled sales-pricing population centers on the sales organization's governed prices for negotiated B2B selling. Same subject matter (prices), different operator, objects, and flows — family boundary, joint review flagged.
- "Agreements/contracts are definitional" — rejected: 3/4 sampled products ship them and they are the negotiated-price realization of governed records, but list-price-driven deployments operate without them.

## Boundary Findings

- **vs Configure Price Quote / CPQ** — the flagged joint review, now resolved from both sides. CPQ centers on the rule-governed configuration of an offer and the stateful quote record, with an embedded **quote-time** pricing engine; Sales Pricing centers on the **standing** price population and the discipline that sets, governs, and releases it. The designed seam is publication/consumption: Zilliant documents Price Manager/Price IQ attaching standard prices and start/target/floor discount guidance into CPQ quotes; Pricefx "publishes approved prices into ERP, CRM, and CPQ." When a CPQ suite adds price-setting/scenario tooling, it grows a Sales Pricing capability — the leaves remain distinct Types.
- **vs Deal Desk / Commercial Approval Platform** — Deal Desk owns the cross-functional approval *process* over commercial commitments (quotes, exceptions, non-standard terms); Sales Pricing owns the price records and their setting/governance. Approval of a price change (this Type) ≠ approval of a deal (Deal Desk). Unprocessed sibling — flag stands for that leaf's pass.
- **vs Retail Pricing Management / Promotion Management (§05.14)** — operator flip: retail-side pricing manages shopper-facing price files, promotions, and markdowns for stores/e-commerce; sales-side pricing governs the selling organization's prices (often negotiated, customer-specific, agreement-backed). Both manage "prices"; joint review recommended when the retail leaves are processed.
- **vs ERP price master** — ERP stores and executes price condition data in sales documents; the pricing application is where prices are designed, simulated, governed, and published from (Pricefx FAQ statement, A). Historical ERP-native pricing modules satisfy the minimal L0 — they are a deployment pole, not a different Type.
- **vs Billing / Subscription Billing** — billing executes invoicing of what was sold; pricing determines what may be charged. One-way upstream/downstream handoff (consistent with the billing pass's record).
- **vs Airline/Hotel-style Revenue Management** — yield over perishable inventory vs price governance over a product/customer catalog. PROS's remaining business is the former; its B2B pricing line (now Conga) was the latter — the same vendor house holding both is the clearest evidence they are different Types.
- **vs Sales Forecasting / Revenue Intelligence / Margin Analytics** — those observe/project sales outcomes; this Type produces and governs the price records that outcomes realize. Realized-price analytics inside pricing products is a closing loop, not a forecast center.
- **vs FP&A / Financial Modeling** — elasticity/optimization models here are operational inputs to released prices, not planning artifacts; no budget/plan objects.

## Uncertainties

- Vendavo/Pricefx-capability/Syncron evidence is product-page tier, not help-center tier: object models, exact workflow states, and numeric parameters were not observed; the final document keeps such specifics qualitative. Zilliant provided the only full Tier-1 operational depth (its structures may be richer than the market floor).
- PROS B2B (→ Conga) internals not evidenced (403 ×2); the AI/science pole rests on the consolidation banner only.
- Quote-time guidance naming (start/target/floor vs floor/target/stretch vs "deal guidance") varies; whether a guidance ladder appears in list-price-only deployments was not directly observed — written as common, not definitional.
- The retail-side sibling (§05.14) is unprocessed, so the sales-vs-retail pricing boundary is held one-sided.
- Market label mapping: directory leaf "Sales Pricing Application" ↔ market "Price Optimization and Management" — plausible and consistent across all sampled vendor/analyst names, but treated as mapping, not proof.

## Final Synthesis

A Sales Pricing Application is the selling organization's price-governance system of record. Its world is built from governed price records (product × conditions), a setting-and-release cycle (strategy/rules → computed changes → simulation → approval → effective-dated publication), and a selling seam that hands those prices to the systems and people who sell, then measures what was actually realized. Around that triple, mature products accumulate the price-waterfall architecture, strategy vocabulary, scenario simulation, approval/audit machinery, guidance ladders at quote time, optimization engines, agreements, market-data ingestion, and integration spine — each common, none definitional. The Type is deliberately upstream of CPQ (which consumes prices inside quotes), distinct from Deal Desk (which approves commitments), from retail-side pricing (a different operator), and from the ERP price master (which stores what this Type designs and governs). The definition survives the historical check: paper price lists under a price committee, ERP condition records, and spreadsheet price books all satisfy the core without any modern feature.
