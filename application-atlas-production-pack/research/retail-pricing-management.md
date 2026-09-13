# Research Notes — Retail Pricing Management

## Research Goal

Understand what a Retail Pricing Management application is from real products: what objects it manages, how prices change over time, how prices vary across locations/channels, how competitive data and optimization enter, and where its boundaries sit against the sibling leaves Promotion Management and Markdown Optimization Application (§05.14) and other adjacent Types.

## Initial Boundary (working hypothesis before research)

- Retail Pricing Management = the retailer-side back-office application that owns the **everyday/base price** of items as managed records: item price records per location/zone/channel, effective-dated price changes through a governed lifecycle, and delivery of approved prices to the surfaces that sell (POS, e-commerce).
- Expected neighbors: Promotion Management (temporary event prices), Markdown Optimization (permanent clearance reductions), commerce-platform pricing engines (execution-time evaluation), CPQ/Sales Pricing (B2B quotes), Retail Merchandising Platform (item/assortment system of record), Retail POS (execution surface), Competitive Intelligence Platform (market data without price execution).
- Sibling research already processed (research/promotion-management.md) pre-anchored the seam: "pricing management owns the everyday/base price; promotion management owns temporary, event-driven deviations."

## Research Questions

1. What is the central object — the price record, the price change, or the price list?
2. How do prices vary (zones, stores, channels, customer groups)?
3. What is the price change lifecycle (create → check → approve → effective date → distribute)?
4. How do competitive prices enter the system (tracking, matching, price index)?
5. How does optimization work (elasticity, KVI, rules, simulation) and is it part of the Type or a layer on it?
6. How do promotions and markdowns relate (integration seams vs owned objects)?
7. What interfaces do users actually work in (workbench, dashboards, rules screens)?
8. What rules matter (approval, effective dates, rounding, conflict checks, one-change-per-day)?
9. Who uses it (pricing managers, analysts, merchandisers, e-commerce ops, brand teams)?
10. Where does the price system of record live (pricing module vs store platform)?

## Representative Products

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Oracle Retail Pricing Cloud Service (RPCS) + Lifecycle Pricing Optimization (LPO) | enterprise suite module; price-event management system of record | large chains | only sampled vendor with deep Tier-1 operational docs; separates management from optimization |
| Revionics (Aptos) | optimization-led lifecycle pricing (base + promo + markdown) | enterprise grocery/c-store/general retail | the "science-led" philosophy; base price as foundation |
| Competera | enterprise AI pricing + competitive data | enterprise e-commerce/omnichannel | competitive-data-led + human-in-the-loop philosophy |
| Prisync | SMB e-commerce competitor tracking + dynamic repricing | SMB/online sellers | self-service pole; rules-based dynamic pricing |
| Wiser | price intelligence + execution for brands and retailers | mid/enterprise brands & retailers | two-sided pole (brands monitor resellers; retailers monitor competitors) |

## Sources

Fetched 2026-09-07:

- Oracle Retail Pricing Cloud Service — Get Started, Use index, Price Change Overview, Configure Zones, Clearance Overview (docs.oracle.com, Tier-1)
- Oracle Lifecycle Pricing Optimization Cloud Service 26.2.301.0 — Get Started, Use index (docs.oracle.com, Tier-1); Rules Based Regular Pricing User Guide title page only (body not reachable)
- Revionics — homepage, /solutions/base-price (Tier-2 product pages)
- Competera — homepage (Tier-2 product page)
- Prisync — homepage incl. plan table and FAQ (Tier-2 product page)
- Wiser — homepage, /products/price-execution (Tier-2 product pages)

Not reachable / not sampled: Blue Yonder pricing (404s in prior sibling pass), SAP pricing (help portal JS-shell), DemandTec (covered in promotion-management pass), Pricefx (B2B-leaning, dropped to keep the sample retail-native), Wiser help center (not fetched; product pages sufficient).

## Product Observations

### Oracle Retail Pricing Cloud Service (Tier-1, evidence layer A)

From the Get Started page: RPCS "provides the ability to define, maintain, and review price changes, clearances, and promotions, as well as provides the ability to execute the price events by passing approved price events onto downstream selling systems for execution." Pricing is one of the core merchandising cloud services (alongside merchandise/inventory management, replenishment, purchasing, sales auditing).

Price Change Overview (user guide):

- "A price change is a permanent change to the retail price of an item."
- A price change specifies: the item (by parent, parent/diff, or transaction item), where (zones or locations), how (percent or amount change, or new fixed price), optionally multi-unit pricing, when (effective date), why (optional reason code).
- Rounding rules "move the new price to established price points, or to round the price."
- Status lifecycle: a change "must go through a series of checks before it can be applied"; role-dependent ability to move status; transitions to submitted/approved (or back to worksheet) trigger a conflict check. Statuses seen across guides: Worksheet, Submitted, Approved, Executed, Rejected, Processing.
- Price change groups group multiple events for easier management; mass approval supported.
- Approved events "are made available in advance of their effective date to multiple downstream systems for ticketing, and to prepare selling locations for upcoming changes."
- Normally only one price change per item/location per day may be approved; an "emergency" price change (separate security privilege) can overlay it.
- Price Event Processing Days system option: minimum advance days between creation and effective date; emergency events bypass with a dedicated privilege.
- Conflict checking: "ensures that invalid prices, or prices out of alignment with your pricing strategy, are not sent down to the point of sale"; relies on a calculated "future retail" — the projected regular price on any given day — with roll-up batches holding future retail at the highest level possible.
- Supplier-controlled pricing for consignment/concession ownership models: item/locations with pricing control = Retailer can be priced by retailer users; Generated By field records retailer vs supplier origin.
- Best practice: enter at the highest level (parent/style for fashion, SKU for grocery), zone level rather than store, for consistency and efficiency.

Configure Zones (user guide):

- Zone structure = groupings of locations for pricing purposes; zone groups → zones → locations (stores or warehouses). Zone groups used in regular, clearance, and promotional pricing.
- Zone groups can be built on geography or customer characteristics (e.g., "US urban stores"); a location can exist in multiple zone groups but only one zone per group; all locations in a zone must share a currency.
- New stores auto-join zones via their pricing location; currency mismatches create new zones.
- Zone maintenance: a location added to a zone participates in future approved events but does not inherit existing approved events; removal keeps existing events. Re-setting an event to worksheet and re-approving adds the location.
- Initial Price Zone Definitions: per department/class/subclass, specify the primary zone group used for initial price setting of new items, plus markup percentage, markup type (cost or retail), and rounding rule. Also used for markdown recommendations by LPO (Markdown Zone Groups).

Clearance Overview (user guide):

- "A clearance event is designed to clear out-of-date merchandise and slow-selling merchandise"; "a clearance markdown is considered a permanent price change, and inventory is consequently revalued."
- Clearance group holds markdowns (discount selling price) and resets ("close out the clearance event, setting the item/location combinations back to the last regular retail price").
- Same status machine (Worksheet/Submitted/Approved/Executed/Rejected/Processing), same conflict checking, same emergency-event mechanism, same zone-level best practices.
- "Reset Clearance with Price Change" system option: executing a price change implies the item is no longer on clearance.

Promotions and Offers exist as a third event family inside RPCS (overview/create/manage pages listed in the Use index) — temporary price events alongside permanent price changes and clearance.

Price Inquiry page exists (lookup of current/future prices).

### Oracle Lifecycle Pricing Optimization Cloud Service (Tier-1, evidence layer A)

- Separate cloud service from RPCS (different suite family: Retail Analytics and Planning vs Merchandising).
- "LPO can accomplish this by empowering retailers to shape demand of their customer segments... leverages a variety of AI models to determine who, what, when, where and for how much the price of various items should be throughout their lifecycle, to maximize return on investment."
- Covers optimization of promotions, markdowns, and Customer Targeted Offers; a dedicated "Rules Based Regular Pricing" user guide exists (regular/base price optimization via rules).
- Consumes price zone groups from RPCS (Markdown Zone Groups configured in RPCS Foundation Data).

Structural takeaway: Oracle itself splits retail pricing into a **management** service (define/maintain/review price events → distribute) and an **optimization** service (AI recommendations) — two products, one data spine.

### Revionics (Tier-2, evidence layer A for product claims)

- Self-description: "AI Solutions for Retail Price Optimization"; "lifecycle pricing optimization" across three solutions: **Base Price**, **Promotions**, **Markdown** — one platform ("Advanced Pricing Platform": Your Data → Analytics → AI Engine → Optimal Pricing).
- Base price page: "Everyday Pricing that Wins Every Day"; "anticipate the impacts of every price change so you know exactly what pricing moves to make and when"; "answers to the 'what ifs' and 'why nots' of pricing"; "price at a localized level" (customer quote); "20 years of AI learning."
- Customer quote (Academy Sports): "understand how shoppers will react to different combinations of price increases and decreases, allowing us to price competitively on the items shoppers care most about" — the KVI (key value item) concept in market language.
- Strategic Pricing Services: a human expert layer around the platform.
- Owned by Aptos, LLC.

### Competera (Tier-2, evidence layer A for product claims)

- Two products: **Pricing Platform** ("increase trust by setting optimal prices") and **Competitive Data** ("including matching, scrapping and crawling").
- Solution pages by need: retail AI, omnichannel pricing, dynamic pricing, price intelligence, price tracking, pricing analytics, promo management, markdown optimization — the full price-lever family marketed from one platform.
- How it works (5 steps): Data Integration & Preprocessing (internal retail data + external market signals) → ML Model Preparation & Training → Holistic Demand Forecasting & AI Pricing Optimization ("contextual AI evaluates many demand drivers beyond simple elasticity") → Full Control & Strategic Alignment ("human-in-the-loop... your team's strategic oversight and business rules"; "transparent SKU-level visibility") → Continuous Refinement & Performance Tracking.
- "Predictive scenario planning — simulate any pricing strategy and forecast its precise business impact before execution."
- "Competera moves beyond traditional competitive or rule-based pricing."
- Industries: grocery, apparel, electronics, beauty, DIY, etc. Cited as a representative vendor in a Gartner "Market Guide for Retail Unified Price, Promotion and Markdown Optimization Applications" (vendor-cited claim).

### Prisync (Tier-2, evidence layer A for product claims)

- Self-description: "Competitor Price Tracking & Monitoring Software" + "Dynamic Pricing"; "AI-Powered Competitor Price Tracking, Dynamic Pricing & MAP Monitoring."
- Dashboard surfaces: price changes, "your store's overall price index," comparison with competitors, product detail view, dynamic-pricing rules screen ("Create custom rules to apply for your products. Select which product segments your pricing rules should apply to.").
- Competitor monitoring modes: URL-based (add competitor URLs per product), channel-based (track all competitors on a sales channel), hybrid.
- Channels: Shopify app, Google Shopping, Amazon; "ecommerce pricing software — adjust prices automatically in bulk."
- MAP Monitoring (for suppliers/brands): "Monitor reseller prices and maintain pricing consistency"; "Recommended Price Module" for suppliers.
- Price history (higher tiers); API access (surcharge); product-count-based plans; self-service ("no integration or technical operation beforehand").
- FAQ frames the alternative as "a giant spreadsheet" — the anti-pattern this Type replaces.

### Wiser (Tier-2, evidence layer A for product claims)

- Three products: **Price Intelligence/Execution** ("Optimize your entire catalog with actionable pricing data and powerful automation"), **Market Intelligence** (digital shelf), **MAP Execution** ("Flag and resolve unauthorized pricing across online marketplaces").
- Serves both sides: Brands (track online pricing, availability, MAP violations) and Retailers ("Optimize prices in real time by responding quickly to competitor moves").
- Price Intelligence in action: SKU-level live price movement; gaps vs key competitors; promo visibility (promo tags, price drops, cadence); stockout detection; historical pricing/availability trends.
- How it works: "Choose the SKUs and rivals that matter" (products, competitors, marketplaces, down to region or in-cart pricing) → "See the gaps and set your rules" (configure rules to drive price recommendations) → "Act fast, grow profit" (roll out; real-time dashboards).
- Features: automatic product matching ("aligns your products with direct competitors automatically"), Chrome extension for real-time checks, Live Prices API ("every team member, and every system, sees the same truth"), dashboards/CSV/API delivery, role-based access + SSO.

## Cross-product Comparison

| Structure / capability | Oracle RPCS/LPO | Revionics | Competera | Prisync | Wiser | Layer |
|---|---|---|---|---|---|---|
| Item-level price records as managed data | A (explicit; item×zone/location) | A (base price on platform data) | A (SKU-level visibility) | A (products imported; store prices) | A (SKU-level tracking) | B |
| Price variation structure (zones / channels) | A (zone groups → zones → locations) | A ("localized level") | A (omnichannel pricing) | A (sales channels) | A (region/marketplace scoping) | B |
| Effective-dated managed price changes | A (effective date, status machine, future retail) | implied (price moves over time) | implied (recommendations executed) | A (dynamic repricing applies changes) | A (roll out recommendations) | B |
| Distribution to selling systems | A (approved events → downstream selling systems, ticketing) | implied (feeds retailer systems) | A ("multi-channel operations" integration) | A (store platform integrations) | A (Live Prices API, ERP hookups) | B |
| Approval / governance workflow | A (worksheet→submitted→approved; roles; conflict check) | not observed | A ("human-in-the-loop... business rules") | not observed (self-serve rules) | A (RBAC/SSO guardrails) | B (governance depth varies) |
| Competitive price tracking + matching | not in RPCS (separate market data would be integrated) | not observed on fetched pages | A (Competitive Data product) | A (core) | A (core) | B |
| Price index / price position vs competitors | not observed | not observed | A ("360° market view") | A (store price index) | A (gaps vs key competitors) | B |
| Price recommendations / optimization | A (LPO: AI models; rules-based regular pricing) | A (core) | A (core) | A ("Recommended Price Module" supplier-side; dynamic engine) | A (recommendations from rules) | B |
| What-if / scenario simulation | not observed in fetched pages | A ("what ifs and why nots") | A (simulate before execution) | not observed | not observed | B |
| KVI / items that matter most | not observed | A (customer quote, market language) | A ("true demand elasticity" framing) | not observed | A ("key competitors" emphasis) | B (concept present, terminology varies) |
| Dynamic/automated repricing | not observed (batch-oriented) | not observed | A (dynamic pricing solution page) | A (core) | A (automation) | B (e-commerce-leaning pole) |
| Clearance/markdown handling | A (clearance events inside RPCS; LPO markdown optimization) | A (Markdown solution) | A (markdown optimization solution page) | not observed | not observed | B (sibling-Type overlap) |
| Promotion price events | A (promotions/offers inside RPCS) | A (Promotions solution) | A (promo management solution page) | not observed | A (promo visibility — observation only) | B (sibling-Type overlap) |
| MAP / reseller price monitoring | not observed | not observed | not observed | A (MAP Monitoring) | A (MAP Execution) | B (brand-side variant) |
| Rounding rules / price points | A (rounding rules) | not observed | not observed | not observed | not observed | A→product-specific leaning common |
| Reason codes on changes | A | not observed | not observed | not observed | not observed | product-specific |
| Bulk/spreadsheet operations | A (upload/download, groups, mass approval) | not observed | not observed | A (bulk adjust) | not observed | B |
| Price history / inquiry | A (Price Inquiry) | not observed | not observed | A (price history tier) | A (historical trends) | B |
| Alerts/notifications | A (notifications page exists) | not observed | not observed | A (email notifications) | A (real-time alerts) | B |
| Initial price setting (markup on cost) | A (Initial Price Zone Definitions) | not observed | not observed | not observed | not observed | product-specific |
| Multi-unit pricing | A (system option) | not observed | not observed | not observed | not observed | product-specific |
| Supplier-controlled pricing (consignment/concession) | A | not observed | not observed | not observed | not observed | product-specific |
| Human expert services layer | not observed | A (Strategic Pricing Services) | A (Pricing Consultancy) | A (free onboarding) | not observed | B |

## Canonical Abstraction Hierarchy

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as retail pricing management:

1. **Item-level price records** — the everyday/base selling price of identified items held as managed, queryable records in a dedicated system (not silent overwrites in a spreadsheet; the system is the price system of record or the authoritative feeder of it).
2. **Price variation structure** — the same item can carry different prices across selling contexts (locations/zones/channels); the record is item × context, even if a small retailer's context set is degenerate (one store, one channel).
3. **Effective-dated managed price changes** — prices change over time through managed change records (what, where, how, when — and typically why), each carrying an effective date and an attributable lifecycle, rather than direct current-value edits.
4. **Delivery to selling surfaces** — approved prices (or the changes that produce them) reach the systems/surfaces that actually sell the items (POS, e-commerce), so the shelf and the record agree.

Remove #1–2 → it is not managing retail prices at all. Remove #3 → it is a static price table, not management over time. Remove #4 → it is price analytics/intelligence, not pricing management.

### L1 — Common Mature Structure

Very common in mature modern products but not required to define the Type:

- price zones / price lists / channel scoping as the working mechanism of the variation structure
- approval workflow and status lifecycle on price changes (roles, review, mass approval)
- conflict/validity checking and a projected "future price" view before changes take effect
- rounding rules / price-point alignment; reason codes on changes
- bulk operations (spreadsheet upload/download, change groups, mass approval)
- price inquiry / price history lookup
- competitive price tracking with product matching, and a price-position/price-index view vs competitors
- price recommendations (elasticity/AI-based) and what-if simulation before execution
- integration to POS / e-commerce / ERP (the distribution seam, realized as batch extracts, APIs, or store-platform connectors)
- alerts/notifications on price-relevant events; role-based access

### L2 — Variant / Optional Structure

Depends on segment, side-of-market, or channel mix:

- dynamic/automated repricing (rules evaluated continuously; e-commerce-leaning pole)
- MAP / reseller price monitoring (brand/supplier-side variant)
- clearance/markdown events and markdown optimization inside the same platform (sibling-Type overlap)
- promotion price events inside the same platform (sibling-Type overlap)
- initial price setting for new items (markup on cost/retail by merchandise hierarchy)
- multi-unit pricing; supplier-controlled pricing (consignment/concession)
- customer-segment targeted offers; localized/regional pricing strategies
- stockout/availability and promo-tag monitoring alongside price (digital-shelf extension)
- human expert/consulting services wrapped around the platform
- where the system of record lives: pricing module as record (suite pole) vs store platform as record with the pricing tool pushing changes (SMB e-commerce pole)

### L3 — Vendor-specific Structure

(kept out of the final document; examples) Oracle: future-retail roll-up batches, Price Event Processing Days option, emergency-event security privilege, Generated By field, "Reset Clearance with Price Change" option, Initial Price Zone Definitions mechanics. Revionics: "The Exchange" resource, Aptos ownership, "20 years of AI learning" claim. Competera: named 5-step methodology, Gartner citation, accuracy claims. Prisync: plan tiers, update-frequency differences by plan, API surcharge, URL/channel/hybrid monitoring modes as packaged products. Wiser: "10B products tracked," "4M+ prices recommended," Chrome extension, Live Prices API branding.

## Vendor-specific Findings

- All numeric claims on vendor pages (e.g., "4M+ prices monitored daily," "95%+ accuracy," plan limits, update frequencies) are vendor-cited marketing figures — recorded here, not promoted to the final document.
- Competera's Gartner "Market Guide for Retail Unified Price, Promotion and Markdown Optimization Applications" citation is vendor-cited; it is used only as evidence that the market itself frames a unified price/promo/markdown category (see Boundary Findings #8).
- Oracle's RPCS carries all three price families (regular, clearance, promotion) in one service — an architectural fact of one vendor, not a definitional requirement.

## Boundary Findings

1. **vs Promotion Management (§05.14 sibling)** — pricing management owns the everyday/base price; promotion management owns temporary, event-driven deviations from it. In Oracle both live in one service but as distinct event families with distinct rules (price change = "permanent"; promotions = temporary offers). Test: remove temporality/event character → pricing management; add it → promotion management. (Consistent with research/promotion-management.md.)
2. **vs Markdown Optimization Application (§05.14 sibling)** — markdown is a *permanent* reduction for clearance/end-of-life with inventory revaluation; pricing management owns the everyday price. Sampled products routinely carry clearance events inside the pricing system (Oracle RPCS) and markdown optimization on the same platform (Revionics, Competera, Oracle LPO) — the lever is adjacent and often co-delivered, but the sibling leaf owns the markdown-optimization center of gravity. Test: remove the clearance/end-of-life intent → pricing management.
3. **vs Competitive Intelligence Platform (§06)** — competitive intelligence collects and analyzes market data for insight; retail pricing management turns price signals into governed price decisions and records. Wiser/Prisync/Competera straddle the seam (they bundle competitive data with price execution). Test: if the output is price records/changes distributed to selling systems → pricing management; if the output is market insight/reports only → competitive intelligence.
4. **vs commerce-platform pricing engines (E-commerce Platform §05.01)** — a commerce platform's pricing/discount machinery evaluates prices at cart/checkout time inside the transaction; retail pricing management is the back-office discipline that decides what those prices are, when they change, and pushes them out. Prisync/Wiser explicitly feed store platforms. Test: remove back-office price governance and effective-dated change management → capability inside a commerce platform, not this Type.
5. **vs CPQ / Sales Pricing Application (§07)** — CPQ prices individual B2B quotes/deals with configuration and approval; retail pricing management prices a catalog of items for everyday sale across locations/channels. Different object (quote vs item price record), different cadence (deal vs catalog-wide change).
6. **vs Retail Merchandising Platform (§05.13)** — merchandising owns the item lifecycle, assortment, and (historically) the item master that pricing consumes; pricing owns the price lever. In Oracle's own suite they are separate cloud services with a data spine between them. Test: remove price-change machinery → merchandising; remove item/assortment machinery → pricing.
7. **vs Retail POS (§05.10)** — POS executes sales at given prices; pricing management decides the prices POS sells at and hands them over ("passing approved price events onto downstream selling systems"). Downstream consumer vs upstream owner.
8. **Taxonomy note (for joint review, non-blocking)** — the market increasingly sells "unified price, promotion and markdown optimization" (the Gartner category name Competera cites; Revionics' lifecycle platform; Oracle LPO). The three §05.14 leaves (Retail Pricing Management / Promotion Management / Markdown Optimization Application) describe three levers that optimization-led vendors deliver as one platform. The leaves remain separable by lever (everyday price / temporary event / permanent clearance), and this pass holds those boundaries; a joint review of the three siblings is recommended when all are processed.
9. **vs Utility Rate Management (§19) / other domain pricing** — same word "pricing," different world (tariffs/rates vs item shelf prices); no structural confusion.

## Historical / Market-Sample Check

Would older, regional, or platform-native products still fit the L0? Yes:

- Legacy merchandising systems of the pre-optimization era maintained item×store price files with effective-dated price changes and batch distribution to POS — price records + managed changes + distribution, without optimization, competitive data, or dynamic repricing.
- Price-zone maintenance (geographic/customer zones) long predates AI pricing; it is a merchandising-system staple.
- Spreadsheet-and-approval price change processes in smaller chains satisfy "managed effective-dated changes" in a degenerate form; the dedicated-system aspect is what distinguishes the Type from ad-hoc spreadsheets, and the sampled SMB product (Prisync) explicitly frames the spreadsheet as the anti-pattern it replaces.

The L0 therefore does not over-fit to the current AI/competitive-intelligence era. Conversely, the modern samples' shared features (competitive tracking, recommendations, simulation, dynamic repricing) are L1/L2, not definition.

## Uncertainties

- The LPO "Rules Based Regular Pricing" guide body was not reachable (only the title page); the exact mechanics of Oracle's regular-price optimization are unverified. Assertions about optimization rest on LPO overview + Revionics + Competera (Tier-2 for the latter two).
- Blue Yonder and SAP pricing could not be reached; the enterprise-optimization picture rests on Oracle + Revionics + Competera.
- Revionics/Competera/Wiser/Prisync evidence is Tier-2 (official product pages, no operational docs); no field-level or status-level claims were taken from them beyond what their pages state.
- Whether approval workflow is universal is unverified — it is directly observed only at Oracle (Tier-1) and as "human-in-the-loop/business rules" at Competera; self-serve SMB tools may skip formal approval. Kept in L1, not L0.
- The relative market weight of the "system-of-record pole" (Oracle) vs the "intelligence/recommendation pole" (Wiser/Competera/Prisync) is unclear from this sample; both poles documented, no market-share claim made.
- KVI terminology was observed only in market language (Revionics customer quote); the concept is treated as common but not asserted as a universal named feature.

## Final Synthesis

Retail Pricing Management is the retailer-side application that treats the everyday selling price as a managed, governed, effective-dated business object: item price records held per selling context (zone/location/channel), changed through managed price-change records (what, where, how, when, why) that pass through checks and approval, and delivered to the selling systems (POS, e-commerce) where the prices actually apply. Around this core, mature products add the price-variation machinery (zones/lists), integrity machinery (conflict checks, future-price projection, rounding, reason codes), bulk operations, price inquiry/history, and — increasingly — a competitive-intelligence layer (tracking, matching, price index) and an optimization layer (elasticity/AI recommendations, simulation) that feed the same change pipeline. The Type sits upstream of execution surfaces (POS, commerce engines), beside its two sibling levers (promotions = temporary deviations; markdown = permanent clearance), and downstream of the item master (merchandising). Its market realization spans a system-of-record pole (suite pricing modules) and an intelligence/recommendation pole (competitive-data-led platforms), unified by the same change pipeline.
