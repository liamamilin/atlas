# Research Notes — Recommerce Platform

Research date: 2026-09-07
Slug: recommerce-platform
Directory location: §B / 05 Commerce, Retail & Marketplace / 05.19 Resale — sibling leaves: Resale Marketplace, Consignment Management Platform (both unprocessed at time of this pass)

---

## Research Goal

Understand what a "Recommerce Platform" actually is as an Application Type, from real products that market themselves in this category — not from the loose industry usage of "recommerce" (which is sometimes applied to any secondhand commerce, including consumer marketplaces).

## Initial Boundary

Working hypothesis at start:

- Recommerce Platform = B2B platform that enables a brand or retailer to operate its own resale program (trade-in / buy-back / consign-in / returns-to-resale), turning used items into sellable branded inventory and returning value to the original owners.
- Nearest neighbors: Resale Marketplace (consumer C2C venue), Consignment Management Platform (consignment-store operator software), Returns Management Platform (05.09), E-commerce Platform (05.01), Circular Economy Platform (§21), Online Marketplace (05.02).
- Terminology collision risk: "recommerce platform" is sometimes used loosely for consumer resale marketplaces. The directory's sibling leaf Resale Marketplace suggests the taxonomy intends a distinction; this pass must confirm it from market evidence.

## Research Questions

1. What is the unit of supply? (customer-owned used items, brand returns, excess inventory)
2. What happens between intake and a sellable listing? (identification, condition grading, cleaning/repair, pricing)
3. What is the selling surface? (dedicated branded resale site, integration into the brand's main e-commerce, in-store)
4. How does value flow back? (brand credit / store credit / gift card / cash payout; margin recovery on brand-owned items)
5. Who operates the program? (brand's own team vs the platform vendor's managed operations)
6. What roles exist? (brand operator, platform ops staff, selling customers, buying customers)
7. What integrations matter? (e-commerce, loyalty, CRM, gift cards, ERP, OMS, returns providers)
8. Where are the boundaries vs Resale Marketplace, Consignment Management, Returns Management, E-commerce Platform?

## Representative Products

Selected for market representation, different operating philosophies, and documentation quality:

1. **Trove** (trove.com) — full-stack recommerce: branded resale experiences + trade-in + returns management (Trove RMS) + Recommerce WMS; software plus managed operations ("your warehouse or ours"). Clients incl. Patagonia, Levi's, Canada Goose, Michael Kors, Eileen Fisher.
2. **Treet** (treet.co) — SaaS branded-resale platform, P2P-first with stackable Trade-In / Off-Price / Returns modules; vendor runs support & logistics for sellers. 250+ brands claimed.
3. **Archive** (archiveresale.com) — "operating system for branded resale": three-layer product taxonomy (Shopping Experience / Supply Generation / Platform Layer), software-first, brand-managed.
4. **ThredUp Resale-as-a-Service** (raas.thredup.com) — managed-service pole: ThredUp's warehouse infrastructure and processing power the brand's resale shop ("We do the work, you own the story").

Rejected / unavailable:
- **Recurate** — recurate.com now serves Trove's homepage (redirect). Treated as no longer an independent reachable product; not sampled. Status (acquisition vs shutdown) unconfirmed.
- Consumer marketplaces (Vinted, Depop, Poshmark, The RealReal) — different leaf (Resale Marketplace); not fetched in this pass; boundary argued structurally and from the sampled platforms' own terminology.

## Sources

All Tier 2 (official product/marketing pages). No help-center / user-guide depth was reachable for any sampled product — these vendors sell via demo requests, not public manuals. Consequence: no numeric limits, defaults, or precise workflow parameters are asserted in the final document; vendor-published statistics are recorded here as claims only.

| Product | URL | Fetched | Result |
|---|---|---|---|
| Trove | https://www.trove.com | 2026-09-07 | OK (homepage) |
| Trove | https://trove.com/resale-trade-in/ | 2026-09-07 | OK |
| Trove | https://trove.com/recommerce-operations/ | 2026-09-07 | OK |
| Treet | https://www.treet.co | 2026-09-07 | OK |
| Treet | https://www.treet.co/p2p | 2026-09-07 | OK |
| Treet | https://www.treet.co/trade-in | 2026-09-07 | OK |
| Treet | https://www.treet.co/returns | 2026-09-07 | OK |
| Archive | https://archiveresale.com | 2026-09-07 | OK |
| Archive | https://archiveresale.com/products/branded-recommerce-site | 2026-09-07 | OK |
| Archive | https://archiveresale.com/products/online-trade-in | 2026-09-07 | OK |
| Archive | https://archiveresale.com/products/resale-wms | 2026-09-07 | OK |
| ThredUp RaaS | https://www.thredup.com/raas | 2026-09-07 | 403 — abandoned after 1 failure |
| ThredUp RaaS | https://raas.thredup.com | 2026-09-07 | OK (homepage) |
| Recurate | https://www.recurate.com | 2026-09-07 | Serves Trove homepage (redirect) — abandoned |

---

## Product Observations

### Trove (evidence layer A unless noted)

Positioning: "Returns Management & Resale Software for Brands & 3PLs"; "Recommerce Experiences That Drive Growth & Profitability". Three solution lines: Resale & Trade-In; Returns Management (Trove RMS); Recommerce Operations (Recommerce WMS).

Resale & Trade-In page — four experience modules:

1. **Branded Resale Sites** — "sell returned inventory and customer trade-ins within one fully branded, catalog-powered experience"; configurable ecommerce sites; dynamic pricing algorithm; true-to-brand emails & packaging; catalog augmentation & integration; CS/CX support & integration; peer-to-peer shopping. "Trove's team leads the site build."
2. **Digital & Store Trade-In Experiences** — "instantly shoppable gift cards"; mail-in trade-in; store trade-in; start online / drop off in-store; peer-to-peer trade-in; "real-time decisioning engine powers item pricing, gift card payout, and logistics configurations"; targeted trade-in emails leveraging catalog data + customer purchase histories; reporting on profitability & LTV uplift.
3. **Integrated Used + New Experiences** — resale widget on PDPs (fill out-of-stock SKU gaps with used options); checkout API; resale catalog API; headless recommerce; shared checkout (used and new together).
4. **Supplemental Selling Channels** — marketplace selling integration; keep-in-store/sell-in-store; algorithm-directed channel routing; configurable routing engine ("route every item to its highest-impact selling channel").

Recommerce Operations page (ReWMS):

- "the assessment and routing brain for high-growth, high-satisfaction resale programs"; "location-agnostic – run your program from your facility or Trove's."
- Returns processing: rapidly identify items (brand's own SKUs, product info, naming conventions; catalog augmentation tools); guides associates through returns processing, auto-sorting items into value tiers; condition-grade at scale ("algorithm-guided, rule-based… consistent attributes"); "resale items are given a unique SKU that captures their quality grade and their specific product description attributes… used online and in-store to merchandise, price."
- Modules: Item Identification; Item Inspection; Inbound Shipments; Inventory Management & Data Integration.
- Pricing & catalog intelligence: ML-powered active pricing models on real-time demand metrics; configurable rule-based merchandising; computer-vision-assisted item identification.
- Channel routing: route every sellable item to highest economic outcome across owned + 3rd-party channels; configurable rules engine; tune disposition logic on demand, supply, seasonality, staffing.
- Integrations: returns/logistics providers, WMS, ERP; resale APIs to bring used inventory into the brand's current ecommerce.
- Claims (kept as claims): 7M+ resale items processed; 10M+ items to date; tens of thousands of items weekly; 50–65% of resale shoppers new-to-brand; 700+ stores with Trove POS software live; 2X–6X gift-card uplift; acquired reverse.supply (EU/UK).

### Treet (evidence layer A unless noted)

Positioning: "Branded Recommerce That Goes Further"; "Powering Recommerce for 250+ Global Brands". "A Full Recommerce Solution… connecting resale, returns, and recovery." Stackable solutions (combinations of the four modules).

Modules:

1. **Peer-to-Peer (P2P)** — "Your customers buy and sell items from each other for cash or brand credit. Treet handles 100% of the support and logistics." Machinery: listing approvals; item verification; dashboard + reporting; customer support; automated price drops; streamlined shipping; dispute resolutions; seller payout; AI-driven shopping recs; bulk listing upload.
2. **Trade-In** — "Let customers trade-in and trade-up for instant credit"; "Your customers send items to you or our partners for instant brand credit. Treet's partner network can receive, clean, list, and ship sold items on your behalf." Machinery: listing approvals; item verification; pricing recommendations; streamlined shipping; dispute resolutions; seller payout; bulk listing upload. Positioned for "sellers that prefer ease and speed over selling P2P" and for brand oversight of items sold.
3. **Off-Price** — "Sell excess inventory through resale."
4. **Returns** — "Reroute returns to be resold"; "Reclaim Revenue From Second-Quality Returns." Ways: customers list returns for sale in the returns portal; reroute returns based on condition to be resold; automatically list non-new returns on Treet. Machinery: one-click listing; returns integrations; integrated shipping; Treet Protection; WMS integrations; customer support; return assurance; pricing recs; dashboards + reporting. Treet + Loop (returns platform) integration: "turn policy-blocked returns into resale revenue."

Marketing/engagement engine (P2P page): price drop alerts; Treet Shop (drives new customers from the Treet community — cross-brand discovery layer); post-purchase emails at smart intervals; ISO ("In Search Of" — matches shoppers looking for items with people who have them); AI-driven shopping recs; listing & abandon-cart reminders; favorite listings; user communication (buyer/seller feedback).

Claims (kept as claims): 65% of sellers opt for brand credit over cash; 278% of allotted credit spent when redeemed on new items; 70% of brands stack trade-in with P2P; 33% of sellers choose trade-in over P2P; average 22 days from onboarding kickoff to first dollar; 80% sell-through on returned units; 25% CO2e reduction per item resold; case-study numbers (e.g., 84% credit choice at one brand; 175%/468% credit overspend at others; 500+ P2P listings at launch for another).

### Archive (evidence layer A unless noted)

Positioning: "powering brand-owned resale at scale"; "The Most Advanced Operating System for Branded Resale"; "Archive partners with brands to build and scale innovative, profitable resale businesses."

Product taxonomy (three layers):

- **Shopping Experience**: Branded Recommerce Site; Peer to Peer Marketplace; Resale Point of Sale.
- **Supply Generation**: In-Store Trade-In; Online Trade-In; Resale WMS.
- **Platform Layer**: Archive Intelligence (AI layer "woven across the entire platform"); Unified Product Catalog; Dynamic Pricing Engine; Analytics & Insights.

Solutions by use case: Resale; Trade-In; Resale Logistics; Take-Back; Warranty & Repair; In-Store Resale. By product type: Apparel; Footwear; Accessories; Oversized Goods; Small Hard Goods.

Branded Recommerce Site page: "Launch a fully branded resale site that feels as polished and trustworthy as your primary site. Archive's platform optimizes search and discovery, merchandising, pricing, and checkout for used and refurbished products." Features: built for secondhand (find the right product, condition, and price across every type of secondhand inventory); "Archive Designed, Managed By You" (custom design + built-in CMS for content and merchandising); special experiences (resale-specific merchandising/UI to spotlight one-of-a-kind items and surface hard-to-identify inventory); end-to-end ecosystem integration (loyalty program, CRM, gift card provider, ERP, OMS — "consistent customer identity, unified attribution, and end-to-end reporting across full-price and resale").

Online Trade-In page: "Capture High-Quality Resale Supply from Anywhere" — "Archive dynamically estimates trade-in values, generates shipping labels, issues credit and handles customer support." Features: simple online submission flow (capture product type, condition, age); intelligent valuation & credit issuance ("dynamic, rules-based valuation that reflects brand priorities, demand, condition, and seasonality… margin-aware"); seamless shipping (prepaid labels, route items to the right warehouse or partner); integrated take-back workflows ("for items not fit for resale, Archive routes products into appropriate end-of-life paths such as recycling, donation, or material recovery"). Benefits include "control intake quality and economics with specific acceptance rules and intelligent valuation."

Resale WMS page: "Efficiently process, refurbish and fulfill resale inventory in the warehouse… Streamline intake, condition grading, cleaning, and repair." Features: configurable services & routing (condition grading scheme, cleaning rules, repair instructions); AI-assisted workflows (identify and grade products); service event bus ("captures every touch of every item across every warehouse"); managed inventory analytics (position, trends, costs).

Claims (kept as claims): ~30% of consumer closets secondhand; secondhand apparel market to $367B by 2029; ~50% of a brand's resale shoppers new to brand; 2–3X LTV for shoppers buying both full-price and secondhand (sources cited by vendor: BCG x Vestiaire 2025; ThredUp 2025 Resale Report; Archive data).

### ThredUp Resale-as-a-Service (evidence layer A, homepage depth only)

Positioning: "Resale-as-a-Service (RaaS) — We do the work, you own the story." RaaS 2.0 modules: Clean Out; Resale; Dropship; Bulk. "Free to Launch. Built to Scale. No Platform Fees."

"The Powerful Operating System": patented infrastructure (proprietary software/systems/processes; three strategically placed US warehouses); "industry-leading technology & software — we invented a real-time database to identify, categorize, and value each secondhand clothing item that we receive to determine the optimal listing price"; proprietary data (17M+ unique items, 50,000 brands, 100 categories — powering customer acquisition and engagement).

Managed-service pole: ThredUp operates the physical processing; the brand owns the branded storefront and story.

---

## Cross-product Comparison

| Structure | Trove | Treet | Archive | ThredUp RaaS |
|---|---|---|---|---|
| Branded resale storefront | Branded Resale Sites + used+new widget/API integration | branded resale site per brand | Branded Recommerce Site (+CMS) | brand-owned resale shop |
| P2P module | peer-to-peer shopping / P2P trade-in | P2P (flagship module) | Peer to Peer Marketplace | not evidenced |
| Trade-in | digital + store trade-in, gift-card payout | Trade-In (instant brand credit) | Online + In-Store Trade-In | Clean Out |
| Returns-to-resale | returns processing in ReWMS; separate Trove RMS | Returns module (+ Loop integration) | Resale Logistics use case | not evidenced |
| Excess/off-price supply | channel routing of secondary inventory | Off-Price module | not evidenced | Bulk |
| Identify / grade / process | ReWMS: identify, sort into value tiers, condition-grade, unique per-item SKU | partner network receives, cleans, lists, ships | Resale WMS: intake, condition grading, cleaning, repair | warehouse processing; real-time item valuation DB |
| Pricing | dynamic pricing algorithm; ML active pricing; price by demand | pricing recommendations; automated price drops | Dynamic Pricing Engine (platform layer) | real-time valuation → optimal listing price |
| Payout to supply side | instantly shoppable gift cards | cash or brand credit (credit emphasized) | credit issuance | not evidenced at detail level |
| Channel routing | algorithm-directed routing engine (owned + 3rd-party marketplaces) | not evidenced as routing | routing inside WMS | not evidenced |
| Marketing/engagement | trade-in emails from catalog + purchase history | full engine: price-drop alerts, ISO, post-purchase emails, recs, reminders | not evidenced | not evidenced |
| Integrations | ERP, WMS, returns/logistics providers, resale APIs | returns integrations, WMS integrations | loyalty, CRM, gift card, ERP, OMS | not evidenced |
| Analytics | profitability & LTV uplift reporting | dashboards + reporting | Analytics & Insights | not evidenced |
| In-store | store trade-in; POS software live in 700+ stores (claim) | not evidenced | Resale POS; In-Store Trade-In | not evidenced |
| Operating model | software + managed ops ("your warehouse or ours") | SaaS; vendor runs seller support & logistics | software-first ("Managed By You") + logistics partners | managed service (vendor warehouses) |
| End-of-life paths | not evidenced | not evidenced | take-back → recycling / donation / material recovery | not evidenced |

### Cross-product commonalities (evidence layer B)

Present in all four sampled products (or strongly in three with no contradiction):

1. **Branded resale selling surface** — every product's deliverable is a resale shop under the brand's identity (dedicated site, embedded in the brand's e-commerce, or in-store).
2. **One-of-a-kind item records** — supply consists of individual used items, each identified against the brand's catalog and carrying condition/grade attributes (Trove's unique per-item SKU; Archive's "one-of-a-kind items"; ThredUp's per-item valuation).
3. **Condition grading** — explicit, rule- or algorithm-guided condition evaluation before listing (Trove, Archive WMS; Treet via partner network "clean, list"; ThredUp processing).
4. **Dynamic/valuation pricing** — pricing is computed per item from demand/condition/seasonality/margin rules, not from a fixed price list (all four).
5. **Trade-in intake with credit payout** — customers submit items online (and/or in-store), receive estimated value, ship with prepaid labels, get credit/gift card (Trove, Treet, Archive; ThredUp Clean Out is the managed variant).
6. **Returns and excess as supply sources** — non-new returns and excess inventory are routed into resale (Trove, Treet explicitly; Archive via Resale Logistics; ThredUp Bulk/Dropship adjacent).
7. **Ecosystem integration** — loyalty/CRM/gift-card/ERP/OMS/e-commerce connectivity for identity, attribution, and reporting (Trove, Archive, Treet; ThredUp implied by "brand-owned shop").
8. **Analytics on program economics** — sell-through, LTV uplift, new-to-brand share, profitability (all four, names differ).
9. **Vendor-operated processing option** — every product can run some or all of the physical operations (Trove "your warehouse or ours"; Treet partner network; Archive logistics partners; ThredUp warehouses).

### Single-product observations (kept product-specific)

- Cross-brand community discovery layer (Treet Shop) — only Treet.
- ISO (In Search Of) buyer/seller matching — only Treet.
- Service event bus capturing every touch per item — only Archive (as a named feature).
- Separate returns-management product line (Trove RMS) beside resale — only Trove.
- "No platform fees" commercial model — only ThredUp RaaS (claim).
- Named end-of-life routing (recycling/donation/material recovery) — only Archive.

---

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

A Recommerce Platform is infrastructure on which a brand or retailer operates the resale of previously-owned or previously-sold goods as a managed commercial program. Four properties; remove any one and the product stops being this Type:

1. **Secondhand item as the unit of supply** — individually identified, one-of-a-kind used items (customer-owned items taken back, non-new returns, excess stock), not infinitely-stocked catalog SKUs.
2. **Intake-to-sellable transformation** — the platform turns an incoming used item into a priced sellable listing: identification against the brand's catalog, condition grading, per-item pricing.
3. **Brand-operated resale surface** — selling happens under the brand's own identity (dedicated resale site, embedded in the brand's e-commerce, or in-store), not on a neutral open venue.
4. **Settled value loop** — each item's journey ends in a commercial close that returns value: credit/cash to the original owner (trade-in, consign, P2P sale) or recovered margin for the brand (returns/excess resale).

Historical check (§24 applied): older trade-in and buy-back programs (electronics trade-in, used-book buyback, early brand take-back like Patagonia Worn Wear) satisfy this loop with manual grading and static pricing — the L0 deliberately requires no AI, no computer vision, no SaaS delivery, no storefront CMS. Those are L1/L2-era capabilities.

### L1 — Common Mature Structure

- Trade-in machinery: online submission flow capturing item details; dynamic rules-based valuation; prepaid shipping labels; credit issuance; acceptance rules controlling intake quality.
- P2P module (brand-scoped): seller listings with approval and verification, platform-run shipping, seller payout (cash or brand credit), dispute resolution.
- Returns-to-resale routing: non-new returns graded and listed instead of liquidated.
- Dynamic pricing engine: demand-aware, margin-aware per-item pricing; automated price drops.
- Reverse-logistics/WMS layer: intake, grading, cleaning, repair, fulfillment; per-item event tracking; inventory analytics.
- Channel routing: allocate each item to its best selling channel (branded site, in-store, third-party marketplaces).
- Marketing/engagement engine: trade-in campaigns from purchase history, post-purchase emails, price-drop alerts, recommendations.
- Ecosystem integrations: loyalty, CRM, gift cards, ERP, OMS, e-commerce platform; unified customer identity and attribution across new and used.
- Program analytics: sell-through, margin, LTV uplift, new-to-brand share, sustainability metrics (e.g., CO2e avoided).
- Customer support & trust machinery: verification, protection/assurance, dispute resolution.

### L2 — Variant / Optional Structure

- Operating-model pole: managed service (vendor runs warehouses and processing — ThredUp RaaS, Trove "our warehouse") vs software-only SaaS (brand runs operations — Treet, Archive "Managed By You").
- Supply mix weighting: P2P-led vs trade-in-led vs returns-led vs off-price-led; most products stack several.
- Payout form: brand credit/store credit (dominant, marketed for overspend uplift) vs cash vs gift card.
- Category scope: apparel/footwear/accessories dominant; hard goods; oversized goods.
- In-store presence: in-store trade-in, resale POS, keep-in-store/sell-in-store vs online-only.
- Third-party marketplace routing as an output channel.
- Take-back end-of-life paths (recycling, donation, material recovery) for unsellable items.
- Adjacent circular services: warranty & repair add-ons.
- Headless/API posture: resale catalog API, checkout API, PDP widgets vs standalone site.
- Cross-brand discovery layer operated by the platform vendor (single-product observation, Treet).

### L3 — Vendor-specific (research notes only)

- Trove: ReWMS module names (Item Identification / Item Inspection / Inbound Shipments / Inventory Management & Data Integration); Trove RMS as a separate returns product; reverse.supply acquisition; stats (7M+/10M+ items, 50–65% new-to-brand, 700+ stores, 2X–6X gift-card uplift); B-Corp / SOC 2 posture.
- Treet: Treet Shop, ISO, Treet Protection, Return Assurance, "22 days to first dollar", 250+ brands, case-study economics (65%/84% credit choice, 278% credit overspend, 80% sell-through on returns).
- Archive: Archive Intelligence, Unified Product Catalog, Dynamic Pricing Engine, service event bus, product-type taxonomy (oversized goods, small hard goods), "Archive Designed, Managed By You" packaging.
- ThredUp: RaaS 2.0 module names (Clean Out / Resale / Dropship / Bulk), three US warehouses, 17M items / 50K brands / 100 categories proprietary data, "Free to Launch… No Platform Fees", Recommerce 100 program.

---

## Vendor-specific Findings

See L3 above. None of these were promoted into the final document; statistics are vendor claims, not verified measurements.

## Boundary Findings

1. **vs Resale Marketplace (sibling leaf, unprocessed)** — sharpest seam. Marketplace: open multi-seller venue; any seller self-lists; platform is a neutral venue taking commission; identity is the seller's, not a brand's. Recommerce Platform: the brand/retailer is the program operator; supply is program-managed (trade-in, returns, excess, brand-scoped P2P with listing approvals); selling happens under the brand's identity. Structural test: remove the brand-operator relationship and open listing to any seller → you have a marketplace. Note: recommerce platforms include P2P modules, but they are brand-scoped (only that brand's items, listing approval, brand credit) — a managed P2P, not an open venue. Also note the terminology collision: consumer marketplaces are sometimes loosely called "recommerce platforms"; the market's B2B segment consistently uses "recommerce/branded resale platform" for the brand-side infrastructure (all four sampled products).
2. **vs Consignment Management Platform (sibling leaf, unprocessed)** — both run a consign-in → sell → settle loop. Consignment management is store-operator software (consignor accounts, intake, store POS, settlements) for consignment shops; recommerce platform is brand-program infrastructure with a national e-commerce surface and reverse logistics. Different operator, different surface, different scale. Flag for joint review when that leaf is processed.
3. **vs Returns Management Platform (05.09)** — returns management's core object is the return authorization/refund; its loop ends when the returned item is dispositioned. Recommerce begins at that disposition point: turning non-new items into sellable branded inventory. Convergence is real and growing (Trove ships both; Treet has a Returns module and integrates with a returns platform) — the seam is the core object and the loop's terminal state.
4. **vs E-commerce Platform (05.01)** — e-commerce sells catalog SKUs in quantity; recommerce sells one-of-a-kind graded used items with per-item condition-based pricing. The branded resale site is a specialized storefront the recommerce platform provides; strip the used-item intake/grading and what remains is generic e-commerce.
5. **vs Circular Economy Platform (§21)** — circular-economy platforms manage sustainability programs/reporting; recommerce platforms run the commercial resale loop. Sustainability metrics (CO2e avoided) appear in recommerce as reporting outputs, not as the managed object.
6. **vs Online Marketplace / Multi-vendor Marketplace (05.02)** — same distinction as #1 at directory level.
7. **Possible taxonomy gap (not this leaf's problem)** — B2B liquidation/recovery marketplaces (bulk lots to business buyers) are adjacent to "off-price/excess" supply but are a different buyer model; not researched here; noted for future passes touching 05.02/05.19.

## Uncertainties

- **Recurate status**: recurate.com serves Trove's site. Acquisition vs shutdown unconfirmed (no further fetches spent). Recurate excluded from the sample.
- **ThredUp RaaS depth**: only homepage-level evidence (403 on /raas; raas.thredup.com homepage OK). Clean Out / Dropship / Bulk mechanics, payout structure, and integration surface not verified — kept structural only.
- **Consumer-marketplace side of the boundary** not fetched (Vinted/Depop/Poshmark unreachable-by-scope choice); the vs-Resale-Marketplace boundary is argued from the sampled platforms' own terminology and structure, not from marketplace-side evidence. The Resale Marketplace pass should re-check this seam.
- **No Tier-1 operational documentation** for any sampled product (no help centers/user guides reachable). All workflow descriptions above are vendor product-page descriptions (Tier 2). No numeric limits, defaults, or precise parameters are asserted in the final document.
- **Category breadth**: all four sampled products are apparel/fashion-adjacent (Archive lists hard goods too). Electronics trade-in platforms (a large recommerce segment) were not sampled; the L0 is written to include them, but the sample skews softlines. Flagged as an uncertainty rather than researched further in this pass.

## Final Synthesis

The Recommerce Platform is the brand-side operating system for resale: it takes previously-owned or previously-sold items back under a managed program (customer trade-in, brand-scoped P2P, non-new returns, excess stock), transforms each one-of-a-kind item into a graded, priced, sellable listing, sells it under the brand's own identity (dedicated resale site, embedded in the brand's e-commerce, or in-store), and closes the loop by returning value — credit or cash to the original owner, or recovered margin to the brand. Around that defining loop, mature products add trade-in machinery, P2P marketplace modules, returns routing, dynamic pricing, reverse-logistics/WMS processing, channel routing, marketing engines, ecosystem integrations, and program analytics. Products differentiate mainly by operating model (managed service vs software-only), supply-mix emphasis, payout form, and category scope. The Type is distinct from the consumer Resale Marketplace (open venue vs brand-operated program), from Consignment Management (store-operator software vs brand-program infrastructure), from Returns Management (disposition vs resale loop), and from generic E-commerce (catalog SKUs vs one-of-a-kind graded items).
