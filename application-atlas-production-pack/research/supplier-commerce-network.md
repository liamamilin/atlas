# Research Notes — Supplier Commerce Network

Research date: 2026-09-08
Directory leaf: Supplier Commerce Network (§05.20 Dropshipping, sibling of Dropshipping Platform)
Slug: supplier-commerce-network

## Research Goal

Understand what a "Supplier Commerce Network" is as an Application Type: what objects exist inside it, who uses it (both sides, if two-sided), how a retail seller connects to product suppliers, how an end-customer order becomes a supplier shipment, what rules govern the flow, and where the boundary lies with Dropshipping Platform (the taxonomy sibling), Online Marketplace, Wholesale/B2B Commerce, Order Fulfillment Platform, Print-on-demand, and supplier directories.

## Initial Boundary

Working hypothesis before research:

- The leaf sits under **05.20 Dropshipping** next to "Dropshipping Platform", suggesting a two-leaf split of the dropshipping market: one leaf for the seller-side operation, one for the supplier side.
- Hypothesis: a Supplier Commerce Network is a third-party-operated network that aggregates many independent product suppliers and connects them to retail sellers, who resell the suppliers' goods through their own storefronts with the supplier shipping directly to the end customer.
- Most likely confusions:
  - Dropshipping Platform (sibling leaf — seller-side automation tooling)
  - Online Marketplace (consumer-facing venue)
  - Wholesale Commerce Platform / B2B E-commerce (retailer buys stock, takes inventory)
  - Order Fulfillment Platform (3PL ships the seller's own stored inventory)
  - Supplier directory (discovery without a commerce loop)
  - Print-on-demand Commerce Platform (also a supplier network, but goods are made after the sale)

## Research Questions

1. Is the Type two-sided? Does it have a real supplier side (supplier onboarding, supplier dashboards, supplier payouts) or only a retailer-side catalog?
2. What is the unit of supply — the individual product, the catalog feed, or the supplier relationship?
3. Is there an access/connection gate: supplier admission review, retailer approval, private listings?
4. How does an end-customer order on the retailer's own storefront get routed to the supplier, and what flows back (status, tracking)?
5. Who holds inventory, and who ships to the end customer? Under whose name/brand?
6. How do money flows work between retailer and supplier — does the network operator become merchant of record, provide a payment channel, or stay out of the trading process?
7. How does pricing work — who sets wholesale cost, who sets retail price, what pricing machinery exists?
8. What are the interfaces for each side?
9. What is the "out-of-network" pole (products that explicitly serve suppliers/catalogs that are NOT part of the network)?
10. Where are the boundaries with the adjacent Types listed above?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different operator postures:

| Product | Philosophy / posture | Evidence quality |
|---|---|---|
| **Spocket** | Curated US/EU supplier network; strong two-sided program (separate supplier dashboards, payouts, branded invoices) | Tier-1 help center fully reachable (Intercom) |
| **Syncee** | Open global B2B dropshipping & wholesale network; explicitly positions itself as a "bridge between retailers and suppliers" not involved in the trading process; richest connection-gate machinery | Tier-1 help center fully reachable (Intercom) |
| **CJ Dropshipping** | Operator-as-fulfiller pole: the network operator also warehouses, sources on demand, and offers agents; supplier network of factories | Official site reachable; help center not article-level fetched |
| **AppScenic** | Verified-supplier network with automation emphasis; separate retailer/supplier dashboards and money flow through a network wallet | Official site + Freshdesk knowledge base fully reachable |

SaleHoo was considered (directory heritage, good historical anchor) but dropped: salehoo.com returned HTTP 403 and help.salehoo.com transport errors (2 attempts each) — see Source-access Limitation.

## Sources

- Spocket Help Center (Intercom): https://help.spocket.co/ — collections "Quick 5-Step Process to Launching your Store", "Spocket for Suppliers" (Joining / Getting Started / Processing Orders / Supplier Payouts / FAQ), article "How do I process and fulfill orders on Spocket?"
- Syncee Help Center (Intercom): https://help.syncee.co/ — "What is Syncee?", "What is the difference between the Marketplace and the DataFeed Manager?", collections "Basics", "Retailers", "Suppliers" (incl. Retailer Approval and Rejection), "What is Auto Order?", "How Retailer Approval works on Syncee?"
- CJ Dropshipping official site: https://cjdropshipping.com/ — homepage flow ("How to start dropshipping with CJ", services footer: sourcing, custom packaging, ODM, print-on-demand, bulk purchase, fulfillment service, warehouses, partner couriers, supplier portal)
- AppScenic official site: https://www.appscenic.com/ — product pages (dropshipping suppliers, automation, integrations); Freshdesk HelpDesk: https://helpdesk.appscenic.com/ — solutions "Retailers Dashboard", "Suppliers Dashboard", "Quick Start Retailers/Suppliers", "How does AppScenic actually work?"
- (blocked) SaleHoo: https://www.salehoo.com/ (403), https://help.salehoo.com/ (transport error ×2)

## Product Observations

### Spocket — key observations (Evidence layer A unless marked)

- Two-sided by construction: help center has major collections for **Dropshippers** (retailers) and **Suppliers** (and a partners/affiliates collection). Suppliers have their own product ("Spocket for Suppliers") with its own dashboard (supplier.spocket.co).
- Retailer flow (official 5-step): create Spocket account → connect store (e-commerce platform integration, e.g. Shopify, eBay) → choose products to sell → review cost and margin (calculate selling price) → publish dropshipping store.
- Supplier side — joining: "What are the requirements of becoming a supplier", "next steps after I've been accepted as a supplier" — **supplier admission is a review/acceptance process** (curated network), plus IP policy and defined supplier responsibilities.
- Supplier side — catalog: add products (upload/publish), set categories/subcategories, variants, product pricing + discount percentage, retail price markup suggestion, configure shipping rates, update inventory, deactivate products; can integrate the supplier's own Shopify store with Spocket for Suppliers so the network catalog mirrors the supplier's store.
- Supplier side — orders: order email notification; if supplier is Shopify-integrated, network orders flow into the supplier's own Shopify with an **S- order prefix** distinguishing network orders from the supplier's own store orders; order note carries the **Spocket branded invoice** to include in the package (white-labeling); supplier fulfills as usual; entering a tracking number on the supplier's Shopify **automatically syncs back to Spocket and the retailer**. Without Shopify integration: supplier dashboard "My Orders" → filter unfulfilled → "Set to Processing" (explicitly "to inform the retailer") → prepare label/package with branded invoice → "Add Tracking Information" (carrier name, tracking number, tracking URL) → bulk export orders to CSV.
- Supplier side — money: payout setup (banking information), PayPal connection, payout schedule, payout history — **the network pays suppliers for orders** (operator-intermediated money flow).
- Supplier side — relationships: retailers can message suppliers (service-level agreement article for supplier chat), suppliers can see which of their products were pushed to retailers' stores.
- AliScraper product line = explicit **out-of-network pole**: AliExpress dropshipping automation (suppliers outside the curated network).

### Syncee — key observations (Evidence layer A unless marked)

- Self-definition: "Syncee is a global B2B dropshipping & wholesale platform designed to help retailers and suppliers connect… **Syncee is a bridge between retailers and suppliers and is not involved in the trading process between them.**" — the network operator explicitly disclaims merchant-of-record status.
- Three solution lines: **Marketplace** (the network: "reliable, pre-vetted suppliers", millions of products, filters, automatic order synchronization, built-in retailer-supplier messenger), **Alibaba Dropshipping** (network-adjacent integration to Alibaba suppliers), **DataFeed Manager** (explicit **out-of-network pole**: work with external suppliers not listed on the marketplace via CSV/XML/XLS/JSON feed files from URL/FTP/cloud sources — a data pipe without the network's vetting, messaging, or order automation guarantees).
- Supplier side — joining: "Supplier Requirements" → "Supplier application review process" → "Conditions for listed suppliers" → "Why is my supplier listing pending" — **gated supplier admission**; pre-vetting is an explicit marketplace quality claim.
- Supplier side — catalog: complete/modify a **supplier storefront** (profile), list products in dashboard, via own store integration (Shopify/Wix/WooCommerce/BigCommerce/Squarespace/Ecwid/Jumpseller), or **via datafeed file**; set pricing; categorize products; set shipping conditions, carriers, weight/price-based fees; set a **Return & Refund policy**; set **minimum order amount rules for wholesale orders**.
- Supplier side — relationships: "Retailer Approval and Rejection" collection — supplier can require **retailer approval** before a retailer may upload their products (request pending → approve/reject in the Retailers menu; product-private listings possible: "How to list my products as a private supplier"); "Explore Retailers" feature (supplier browses retailers); **two-way rating system** (supplier rating and retailer rating); article "My retail partner sells my product at a different price than I recommended. What can I do?" — retail price is the retailer's, supplier's price is a **recommendation**.
- Supplier side — orders & money: "What is Auto Order?" — the canonical order process: (1) retailer's store receives the customer order, (2) **retailer pays for the order in their Syncee account**, (3) Syncee sends the **paid order** to the supplier's store admin with billing and shipping info, (4) supplier fulfills from their own store admin, (5) supplier enters tracking number in their own store admin, (6) Syncee sends tracking back to the retailer's store. Payment mechanics: "**Syncee does not handle the payments (or refund) of the orders.** Payments go from the retailer to the supplier directly through a secure channel provided by PayPal or Stripe." Supplier connects PayPal/Stripe to enable Auto Order; "Getting Paid" collection; supplier currency choice.
- Retailer side: browse/filter marketplace products, import one-by-one or in bulk; "Approval Needed" state in the marketplace (supplier gate); **Import list** as a staging area (price margin and pricing rules, category mapping, field/variant renaming, out-of-stock handling, price update toggles) before pushing to the store; Product cost vs Retail Price with recommended margin; contact suppliers directly (messenger); order management (view, export, archive); shipping information pages; refund request flow.

### CJ Dropshipping — key observations (Evidence layer A for homepage; lower depth — help-center articles not fetched)

- Operator-as-fulfiller pole: CJ itself operates **global warehouses** ("10+ global shipping warehouses"), claims "1M+ cooperated factories" as its supplier base, and 120+ partner couriers; product pages show per-product "**Lists: N**" (how many stores carry the item) and price ranges.
- Retailer flow (homepage "How to start dropshipping with CJ"): ① find and sell winning products → ② authorize/connect store and list products → ③ auto-sync store orders, place order on CJ → ④ fulfill and track customer orders. Store connection via Miaoshou ERP to many platforms (Shopify, WooCommerce, TikTok Shop, Temu, eBay, Etsy, Lazada, Shopee, etc.) plus browser plugin to import found products.
- Distinctive supply-side machinery: **sourcing requests with quotes** ("Fast Sourcing": submit sourcing requests, compare quotes), a **sourcing-agent marketplace** (agents with profiles, price floors, e.g. "From $500/$800") — procurement on demand inside the network; **custom packaging/branding**, **ODM/product development**, **print-on-demand**, **bulk purchase/wholesale**, **quality inspection**, "ready-to-ship" inventory, fulfillment service ("host your products in CJ's warehouses, CJ dropships for you") — the operator can take over warehousing of the retailer's (or supplier's) goods.
- Supplier side exists as a separate portal ("CJ Suppliers", suppliers.cjdropshipping.cn) — supplier onboarding into the network (observed only as a portal existence; depth limited).
- Money posture: orders are paid **on CJ** (payment methods page, wallet/credit services) — the operator is in the payment path, unlike Syncee's explicit disclaimer. (Layer A for "orders placed on CJ"; the exact settlement structure not verified at article level.)

### AppScenic — key observations (Evidence layer A unless marked)

- Self-description (FAQ): retailer sells on own website/marketplace; products are held by the supplier/wholesaler; when a customer orders from the dropshipper's site, **AppScenic receives the notification and forwards the order to the supplier automatically**; **the supplier fulfills and ships directly to the customer under the dropshipper's name** — white-label shipping stated verbatim. "Verified domestic suppliers" is the network quality claim; supplier-facing onboarding page ("Become our supplier") and separate supplier login exist — two-sided.
- Retailer side (Quick Start): create account → **connect store** (Shopify/WooCommerce/Wix/Ecwid/eBay/Walmart) → choose subscription plan → store & shipping settings → configure **Default Price Formula**. Product Catalogue browsing with **Premium badge**; import one/bulk; "All Products" area with **Push to Store** / "In Store" states and auto-push; **Price Formulas** (retailer pricing rules); **Boards/Collections** for organizing; orders area with **Order ID vs Integration Order ID**, total-price breakdown, **PROFIT calculated** per order; **Store Wallet** — retailer deposits funds into a wallet that pays suppliers (deposit bonus, payment methods); shipping settings incl. **default phone number for orders** (a supplier-ships-to-customer artifact); international shipping options.
- Supplier side (Quick Start): create account + **Business Profile** → configure **ship-from and ship-to locations (warehouses)** → set **Returns Policy** → **import and publish products** (via own Shopify/WooCommerce store integration, manual "Add New", or **Online Feeds** — feed files for catalog publication) → set up **getting-paid profile**. Orders: statuses **On Hold** (delivery address hidden while On Hold), **Pending Payment**; add tracking numbers; "when is an order complete"; view invoice. Business Profile extras: **invoicing on the supplier's behalf** (network issues invoices in the supplier's name), business currency, VAT number, **"What happens if I select one or any marketplace as a restriction of selling my products?"** — supplier can restrict which marketplaces retailers may sell on. Payments: "When am I getting paid?", "How does the money from Retailers get to my account?", "Who guarantees that I will get the funds for my products?" — **network-intermediated money flow** (Layer A for existence; exact settlement terms not verified).
- AI tools (titles/descriptions, image upscaling, SEO, marketing) — era-current add-ons (evidence of current packaging, not structural).

## Cross-product Comparison

| Structure | Spocket | Syncee | CJ Dropshipping | AppScenic | Layer |
|---|---|---|---|---|---|
| Two-sided network (supplier program with own dashboard + retailer program) | Yes (Spocket for Suppliers) | Yes (explicit "bridge") | Yes (CJ Suppliers portal; depth limited) | Yes (Suppliers Dashboard) | B |
| Many independent suppliers, each with own identity/profile/catalog | Yes | Yes (supplier storefronts) | Yes (factory network + product catalog) | Yes (Business Profile + My Products) | B |
| Gated supplier admission (application/review) | Yes (requirements → accepted) | Yes (application review, listing pending, pre-vetted claim) | Not verified (portal exists) | Verified-supplier claim; profile + publish flow | B (A for Spocket/Syncee) |
| Retailer–supplier connection gate | Not observed (open work with network suppliers) | Yes (Retailer Approval feature, private suppliers) | Not observed | Not observed; supplier marketplace-sales restrictions instead | A, product-dependent |
| Multi-supplier catalog browsing/filtering for retailers | Yes | Yes (Marketplace, filters) | Yes (+ sourcing requests) | Yes (Product Catalogue, Premium badge) | B |
| Product publication modes (dashboard, supplier store integration, feed file) | Dashboard + supplier Shopify integration | Dashboard + supplier store integration + datafeed file | Supplier portal (depth limited) | Manual + supplier store integration + Online Feeds | B |
| Catalog/inventory sync into retailer's store | Yes (push; updates) | Yes (import lists, daily automatic updates) | Yes (auto-sync) | Yes (Push to Store, auto-push, 24/7 sync) | B |
| Pricing machinery (supplier cost + retailer markup/margin rules) | Yes (cost & margin, retail price markup) | Yes (product cost vs retail price, recommended margin, dynamic pricing; supplier price = recommendation) | Yes (retail price markup) | Yes (Price Formulas both sides) | B |
| Order routing: retailer's end-customer order → network → supplier | Yes (orders flow to supplier, distinguishable prefix) | Yes (Auto Order sends paid order to supplier store admin) | Yes (auto-sync orders, place order on CJ) | Yes (order forwarded to supplier automatically) | B |
| Supplier ships directly to end customer under retailer's brand | Yes (branded invoice in package) | Yes (dropshipping service; tracking to retailer's store) | Yes (custom packaging/branding) | Yes (verbatim "under the dropshipper's name") | B |
| Status/tracking flows back to retailer | Yes (automatic tracking sync; Set to Processing informs retailer) | Yes (tracking sent to retailer's store) | Yes (fulfill and track) | Yes (supplier adds tracking; order statuses; retailer sees PROFIT) | B |
| Order exception machinery visible in docs | Cancel order (as supplier), bulk export | Order management, refund requests, archiving | Not verified at article level | On Hold (address hidden), Pending Payment, completion rule | A, product-dependent |
| Money flow | Operator pays suppliers (payout setup/schedule/history) | Retailer pays supplier via PayPal/Stripe channel; operator disclaims handling | Orders paid on operator | Retailer Store Wallet → operator pays supplier; invoicing on supplier's behalf | A — **genuinely variant, three postures** |
| In-network retailer↔supplier communication | Yes (chat SLA) | Yes (built-in messenger) | Support chat (not per-partner, unverified) | Ticket system (not per-partner messenger observed) | A/B, depth varies |
| Two-way reputation/ratings | Not observed at article level | Yes (supplier rating + retailer rating) | Not verified | Not observed at article level | A, product-dependent |
| Out-of-network pole (explicit non-network supply) | AliScraper (AliExpress) | DataFeed Manager | Sourcing agents procure on demand | — (API listed "soon") | A |
| Operator-added services beyond bridging | — (curated network itself is the value) | Wholesale/bulk modes | Warehousing, sourcing agents, ODM/POD, quality inspection, loans, prime | AI tools, wallet bonus | A, product-specific |

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures. The Type stops being recognizable as a Supplier Commerce Network if any one is removed:

1. **The multi-supplier network of record** — a third-party-operated aggregation of many independent suppliers, each with its own identity/profile, catalog (products with wholesale terms), and fulfillment capability/coverage, browsable and selectable by retail sellers. The suppliers are onboarded as participants of the network (commonly via a review/acceptance gate), not merely listed as data.
   - Remove → single-supplier integration tooling, a plain product feed, or a store app; the "network" is gone.
2. **The retailer–supplier working connection** — the retail seller selects suppliers/products and establishes a working relationship through the network (commonly gated on one or both sides: supplier admission review, retailer approval for specific suppliers, private listings, marketplace restrictions). The connection is a managed object: it can carry permissions, terms, and communication.
   - Remove → an anonymous catalog or lead list with no managed relationship (supplier-directory territory).
3. **The fulfillment routing loop** — an end customer orders on the **retailer's own storefront**; the network captures that order, routes it to the connected supplier as a fulfillment instruction (items, billing/shipping data), the **supplier ships directly to the end customer under the retailer's brand**, and fulfillment status/tracking flows back into the retailer's storefront and network view. The retailer never takes inventory ownership of the goods.
   - Remove → a wholesale/lead venue (retailer buys stock) or a directory; the dropshipping loop — the leaf's defining commerce semantics — is gone.

Jointly-held is load-bearing:
- 1 alone = supplier catalog/directory (thin ancestor: paper/CD-era supplier directories).
- 1+2 without 3 = vetted supplier directory with relationships but no commerce loop (the historical directory pole; the market's own modern echo: feed-pipe products).
- 2+3 without 1 = a single-supplier dropship program/integration (e.g., one brand's direct-ship agreement or a one-supplier routing app), not a network.
- 1+3 without 2 = an unvetted anonymous data pipe (the market itself labels this pole as outside the network — Syncee's DataFeed Manager is deliberately not the Marketplace).

Historical check: a pre-web mail-order retailer working with a wholesaler/distributor association's catalog, phoning/faxing end-customer orders to the distributor for direct shipment, satisfies all three structures without any software platform (multi-supplier via the association/catalog, managed trade relationship, routing loop with the distributor shipping direct). Modern automation (API sync, wallets, feeds) is not part of the core. Historical check passed.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Storefront integration layer** — retailer connects their e-commerce platform/store (several platforms per product); supplier-side store integration also common (supplier mirrors their own store into the network).
- **Catalog publication and sync machinery** — supplier publishes products (dashboard, own-store integration, or feed files); catalog/inventory/price updates propagate on a schedule; a staging area on the retailer side (import lists / push-to-store states) before products go live in the retailer's store.
- **Pricing machinery** — supplier holds product/wholesale cost and commonly a recommended retail markup; retailer holds margin/pricing rules (formulas, dynamic pricing) applied at import and kept in sync.
- **Order status model with backflow** — processing/shipped/completed visible to the retailer; tracking number/carrier/URL captured from the supplier and synced into the retailer's store; exception states (on hold, pending payment, cancel/refund paths) exist in most mature products.
- **White-label fulfillment elements** — shipping under the retailer's name; branded invoice/packing slip inside the package (explicit in 3 of 4 samples, second-hand implied in the fourth).
- **Supplier payment path** — the network either pays suppliers (payouts) or operates the payment channel rails between retailer and supplier; suppliers configure payout/receiving profiles.
- **Discovery and trust surfaces** — filtering by location/lead time/category; supplier profiles; ratings/reviews (explicit two-way in one sample; product-level "how many stores list this" in another).
- **In-network communication** between retailer and supplier (messenger/chat) — present as first-class in two samples.
- **Store settings carrying supplier-fulfillment semantics** — retailer's shipping location/phone defaults for supplier shipments; ship-from/ship-to coverage and return policies configured by suppliers.

### L2 — Variant / Optional Structure

Depends on operator posture, segment, geography, business model:

- **Operator money posture** (the deepest split observed): operator-as-payer (payouts from the network) vs operator-as-channel (retailer pays supplier directly through provider rails; operator explicitly not involved) vs operator-as-merchant (orders paid to the operator). All three postures exist in the sample.
- **Connection gate posture**: open network (work with any listed supplier) vs supplier-side retailer approval / private listings vs marketplace-restriction controls.
- **Supply-side services**: on-demand sourcing with quotes and agents; warehousing/3PL-like services; custom packaging/branding; ODM/product development; print-on-demand; quality inspection — the "operator-as-fulfiller" pole.
- **Wholesale/bulk modes** alongside dropshipping (retailer buys stock) — a different fulfillment relationship offered by the same network.
- **Feed-file ingestion/publication** as the explicit out-of-network pole (external suppliers via data files).
- **Regional footprint as a product axis** (curated domestic supplier pools vs global factory networks).
- **Era-current add-ons**: AI content/SEO/marketing tools; browser plugins; consumer mobile apps; affiliate/partner programs; credit/loan services.

### L3 — Vendor-specific Structure (stays in Research Notes)

- Spocket: S- order prefix convention for network orders in the supplier's Shopify; "Set to Processing" as the retailer-notification step; branded invoice retrieval flow; AliScraper product line.
- Syncee: DataFeed Manager (named out-of-network product); Import List as a named staging object; Auto Order naming; "Explore Retailers"; referral widget; the 2-day retailer-approval response SLA and the operator's right to disable the feature if ignored.
- CJ: Miaoshou ERP as the connection substrate; sourcing-agent marketplace with per-agent pricing floors; CJ Prime; credit/loan services; "Lists: N" counters on product pages.
- AppScenic: Store Wallet with deposit bonus; Boards/Collections; Premium badge; default-phone-for-orders requirement; "invoicing on my behalf" mechanics; Order ID vs Integration Order ID.

## Vendor-specific Findings (summary)

See L3. Additionally: two-way ratings, sourcing-agent marketplace, wallet-based settlement, and marketplace-sales restrictions are each observed in only one sample and must not be promoted to the Type definition.

## Rejected Findings

- "Supplier Commerce Network = product-import automation" — rejected. Automation is mature common structure (L1), but the network of record and the managed relationship are the discriminators; feed-pipe products deliberately position themselves as outside the network while providing the same sync machinery.
- "The retailer browses products, not suppliers" — rejected as a definition of the Type's unit of supply. All sampled networks surface the supplier as an entity (profiles, storefronts, ship-from coverage, ratings); supplier-selection is a first-class act even where product-first browsing dominates.
- "The operator must be merchant of record / wallet-based" — rejected. Three different money postures coexist in the sample; the invariant is only that supplier compensation flows through an operator-governed path or channel.
- "Type requires US/EU curated domestic suppliers" — rejected; global factory-network and open-marketplace postures satisfy the same core.
- "POD platforms are a Supplier Commerce Network subtype" — rejected per the production test (already held by the print-on-demand pass): POD goods are made after the sale from a seller design; here goods are picked from existing supplier stock.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove X → becomes Y" test) |
|---|---|---|
| **Dropshipping Platform** (taxonomy sibling, §05.20, unprocessed) | Twin leaf / overlapping market | The network's primary object is the **supplier population and the retailer–supplier relationship** (supplier onboarding, supplier dashboards, supplier payouts, connection gates); a seller-side dropshipping platform centers the **retailer's own operation** (import/pricing/order automation) over one or a few supply sources. Remove the supplier-side program and multi-supplier network of record → seller-side dropshipping tooling. Market products blend both faces; flag for joint review. |
| **Online Marketplace** (§05.02, unprocessed) | adjacent, easily confused by "multi-seller venue" surface | In a marketplace the **end customer buys on the venue**; the venue is the sales channel of record. In a supplier network the **buyer on the venue is the retailer**, and end-customer sales happen outside the network on retailers' own storefronts. Remove retailer-buyers/end-customer-sales-outside → marketplace. |
| **Wholesale Commerce Platform / B2B E-commerce Platform** (§05.17; B2B leaf processed) | adjacent | B2B e-commerce is a seller-operated channel through buying-organization accounts where the **buyer takes inventory** (goods ship to the buyer). Here the retailer-buyer never takes inventory; goods ship to the retailer's end customer. Wholesale/bulk modes inside networks are a variant, not the core. |
| **Order Fulfillment Platform** (§05.08, unprocessed) | adjacent | A fulfillment platform stores and ships **the seller's own inventory** (3PL relationship). In a supplier network the goods remain the **supplier's stock** and the supplier fulfills. The operator-as-fulfiller pole (warehousing services) leans toward the fulfillment Type at the edge. |
| **Supplier directory / lead-list products** | thin ancestor / outside the Type | Discovery and contact data without the routing loop: "remove the routing loop → supplier directory." Historical paper/CD directories are the thin ancestor, not the Type. |
| **Print-on-demand Commerce Platform** (processed) | structural sibling | Both are seller↔producer networks with routing loops; the production test separates them: POD makes the item **after the sale** from a seller design; supplier networks pick **existing supplier stock**. |
| **Supplier Portal / PRM-adjacent Types** (processed: supplier-portal noted under PRM pass as buy-side) | different direction | Those center the **buyer organization's procurement** of its supply base (buy-side records, onboarding, compliance). Here the network is a commerce venue connecting independent suppliers with retailers who resell. |

## Uncertainties

- **CJ Dropshipping depth**: homepage-level evidence only (flow steps, services, warehouse/supplier claims); help-center articles not fetched. CJ's supplier-side program depth and its exact settlement structure (operator as merchant vs channel) are unverified — the "operator-as-merchant" posture is inferred from orders being placed and paid on CJ (existence-level evidence only).
- **SaleHoo** unreachable (403/transport ×2): the directory-heritage pole is therefore evidenced indirectly (via the market's own "what is dropshipping" explainers on other vendors' sites and the POD pass's recorded boundary work), not directly.
- **Whether the sibling "Dropshipping Platform" leaf will center automation tooling (DSers/AutoDS class) or network apps**: the two-leaf split of §05.20 looks like two faces of one market; the boundary drawn here (supplier population + managed relationship as primary object) is the cleanest structural cut found, but joint review is recommended when the sibling is processed.
- Ratings/reviews, per-partner chat, and order-exception depth vary in documentation completeness; treated as L1/L2 with varying evidence rather than universal claims.

## Final Synthesis

A Supplier Commerce Network is a third-party-operated, two-sided commerce network that aggregates many independent product suppliers and connects them with retail sellers. Its defining structure is three jointly-held parts: the multi-supplier network of record (suppliers onboarded as participants with identities, catalogs, fulfillment coverage — commonly admission-gated); the managed retailer–supplier connection (selection plus one- or two-sided access gates, carrying terms and communication); and the fulfillment routing loop (end-customer orders captured from the retailer's own storefront, routed to the supplier as fulfillment instructions, shipped by the supplier directly to the end customer under the retailer's brand, with status/tracking flowing back). Money compensation flows to suppliers through an operator-governed path whose exact posture (payer, channel, or merchant) is a variant, not a definition. Everything else — storefront integrations, catalog sync, pricing formulas, ratings, messaging, wallets, sourcing agents, warehousing, AI tools — is mature structure or optional machinery, not the Type.

The Type's cleanest negative test: remove the multi-supplier network → single-supplier dropship integration; remove the managed relationship → anonymous feed pipe or directory; remove the routing loop → wholesale venue or supplier directory. Historical practice (retailers holding direct-ship relationships with distributors via trade catalogs, routing orders manually) satisfies the core without any modern platform.
