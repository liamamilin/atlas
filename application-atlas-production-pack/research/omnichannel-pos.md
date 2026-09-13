# Research Notes — Omnichannel POS

## Research Goal

Determine what an "Omnichannel POS" actually is as an Application Type: whether it is a distinct Type, a variant of Retail Point of Sale, or an alias — and if it has its own defining core, what that core is. This leaf carries an open joint-review flag from both sibling passes (retail-point-of-sale, mobile-pos), which must be discharged here.

## Initial Boundary

- Under 05.10 Retail POS, siblings: Retail Point of Sale, Mobile POS, Omnichannel POS.
- Both prior passes observed: vendors ship all three as modes/editions/plans of one product family (Shopify POS, Square for Retail, Erply editions); the trio shares the sale spine (priced catalog → sale → tender → completed transaction).
- Hypothesis to test: Omnichannel POS = Retail POS + unified cross-channel commerce state + cross-channel fulfillment flows. If so, it is a channel-depth-defined sibling, like Mobile POS is a surface-defined sibling.
- Neighbors: E-commerce Platform (customer-side online selling), Order Management System (order orchestration), Retail Inventory Management (stock planning), Checkout Platform (remote customer self-service).

## Research Questions

1. What exactly do vendors mean by "omnichannel" when attached to a POS? What data is unified, and across which channels?
2. What cross-channel flows does the POS itself execute (vs. the back office or the online store)?
3. Is the sale machinery at the register different from a plain Retail POS, or identical?
4. Do standalone "omnichannel POS" products exist, or is the name always a posture/edition of a retail POS product?
5. What breaks when the unified state is removed (→ plain Retail POS) or when the sale spine is removed (→ back-office commerce platform)?
6. Historical check: does a pre-e-commerce POS fit the definition? (Expected: no — which locates the Type's origin in the unified-commerce era.)

## Representative Products

Selected for market representation, documentation access, and different product philosophies / packaging poles:

- **Shopify POS** — commerce-platform-first pole: POS as one selling surface of a unified online+offline commerce platform. Evidence: product pages (fetched, A-level).
- **Square for Retail** — payments-first pole: retail POS plan whose omnichannel capability comes from bundling Square Online. Evidence: features/capabilities pages + one help article (A-level).
- **Erply** — retail-first/mid-market pole: POS + back office that connects to external e-commerce platforms (Shopify, WooCommerce, Magento) rather than owning the online store. Evidence: official wiki (A-level; the "omnichannel" URL serves the Offline Mode article — noted below).
- **Lightspeed Retail** — retail-first SaaS pole; **not researched**: marketing site returned HTTP 403 and the help center transport-errored (2 attempts). Recorded as a sourcing limitation; no claims based on it.

## Sources

- Shopify — POS product page — https://www.shopify.com/pos (fetched 2026-09-10)
- Shopify — Omnichannel POS page — https://www.shopify.com/pos/omnichannel (fetched 2026-09-10)
- Square — Square for Retail features page (IE/GB variants) — https://squareup.com/ie/en/point-of-sale/retail/features , https://squareup.com/gb/en/point-of-sale/retail/features (via search excerpts, 2026-09-10)
- Square — Square for Retail capabilities page — https://squareup.com/us/en/retail/capabilities (via search excerpts, 2026-09-10)
- Square — "Set up pickup options for your online store" — https://squareup.com/help/us/en/article/6866-in-store-and-curbside-pickup-with-square-online-store (via search excerpt, 2026-09-10)
- Erply Wiki — "Compare e-commerce offerings" — https://wiki.erply.com/article/718-compare-e-commerce-offerings (fetched 2026-09-10)
- Erply Wiki — Offline Mode article (served at the /omnichannel URL) — https://wiki.erply.com/article/858-omnichannel (fetched 2026-09-10)
- Sibling documents: applications/retail-point-of-sale.md, applications/mobile-pos.md (research dates 2026-09-06 / 2026-09-08)

Research date: **2026-09-10**

## Product Observations

### Shopify POS (commerce-platform-first pole)

Evidence layer A (directly observed on official product pages).

Key observations:

- Shopify's own FAQ defines the category: "Multichannel POS systems allow retailers to sell in store and online… customers can buy online and pick up their purchase in your store—or they can buy in store and have the purchase shipped to their home." Shopify uses "multichannel POS" and "omnichannel selling" interchangeably.
- The omnichannel page's headline claim: "Every channel. One system." Cross-channel flows enumerated: **Buy online, pickup in store** (BOPIS); **Buy in store and ship** (endless-aisle-style: order online items for shoppers in store, ship home); **Browse in store, buy online** (email virtual carts).
- Unified state enumerated: automatic inventory syncing across locations "as items are sold, restocked, or returned"; centralized order management ("manage local delivery, in-store pickup, returns, and exchanges directly from your point of sale"); gift cards sold as physical or digital, redeemable "in store or online"; automatic customer profile syncing ("track customer data online and in store, from order history to personal preferences").
- One back office manages the business "across all your locations, in person and online"; the POS is described as "connected to that powerful back office for in-person sales, ensuring that inventory, payments, and customer data are fully synced."
- The POS FAQ's checkout loop is the standard retail loop (scan → total → pay → receipt → inventory/customer update) — identical machinery to the Retail POS sibling.
- Packaging: one product; omnichannel is a feature posture of the same POS, not a separate SKU.

### Square for Retail (payments-first pole)

Evidence layer A for the features/capabilities pages and the pickup help article (fetched via search excerpts of official squareup.com pages); the dedicated help-center article ID for "About Square for Retail" redirected elsewhere, so deep help-center detail was not reachable.

Key observations:

- Positioning: "All the tools you need – from open to close, in-store and online." "Keep your store in sync, in person and online with a centralised system designed for retail."
- Unified state: "Every sale you make and item in your catalogue is automatically synced on your POS from every sales channel"; "Orders and inventory sync automatically across locations and channels"; "Stock counts will stay accurate and synced across every location, in-store and online."
- Cross-channel fulfillment: "Offer click and collect and delivery — fulfil orders and give customers the option to collect items in person or have them delivered"; "Offer in-store pickup or delivery… work with an in-house or third-party courier."
- The online channel is a bundled sibling product (Square Online): "Build or sync your online store — set up an online store that matches your brand or connect your current website"; social selling (Google Product Listings, Facebook/Instagram) extends channels.
- Help article (Square Online pickup): in-store/curbside pickup is configured in the Dashboard under Fulfillment methods; pickup fulfillment is assigned to items in the item library; pickup timing can be auto-calculated; quantity limits for pickup/delivery orders are configurable. This shows the cross-channel order's lifecycle is administered across back office (setup) and POS (fulfillment).
- Packaging: Square for Retail is a plan tier of the Square POS product; Square Online is a bundled companion. Again one product family, omnichannel as posture.

### Erply (retail-first, integration-based pole)

Evidence layer A (official wiki). Note: the wiki URL slug "omnichannel" actually serves the "Offline Mode" article; Erply's omnichannel capability is documented across its E-commerce and Backoffice sections rather than one page.

Key observations:

- Erply's e-commerce section documents integrations with external platforms: Shopify, WooCommerce, Magento, plus its own Inventory.com offering; a comparison table ("Compare e-commerce offerings") enumerates what the integrations carry: **Buy online, pick up in-store** (X for both Shopify and WooCommerce), unique webshop pricing, price lists, multiple tax rates, product stock level management, matrix/bundle/assembly products, integrated payments, customer accounts, shipping integrations.
- This confirms the omnichannel capability can be realized through **integration with an external online store** rather than a native one — the unified state is the invariant, not the native storefront.
- The POS/back office is web-based; offline mode caches inventory and sales locally and syncs to the back office on reconnect — showing the sync posture (real-time vs. cached-and-reconciled) is a deployment variant.
- Chain/franchise section (HQ synchronization, shared-data franchise) shows multi-location/multi-entity scale is part of the same back-office fabric.
- Packaging: one POS + back office product with editions; e-commerce is an integration layer.

### Lightspeed Retail (not researched)

Both official surfaces failed (403; transport error). Recorded as a sourcing limitation. Lightspeed is widely positioned as an omnichannel retail POS (its own customers cite switching from it — Shopify's tokyobike case study), but no claims in this research rest on it.

## Cross-product Comparison

| Dimension | Shopify POS | Square for Retail | Erply |
|---|---|---|---|
| Sale machinery at register | standard retail loop (scan→total→tender→receipt→record) | standard retail loop | standard retail loop |
| Unified catalog/inventory across channels | yes, native | yes, native | yes, via e-commerce integrations |
| Unified customer profile across channels | yes, native ("order history… online and in store") | yes ("track every sale in one place") | yes (customer accounts carried by integrations) |
| Unified orders across channels | yes ("centralized order management… directly from your point of sale") | yes ("orders… sync automatically across locations and channels") | implied via integration table (stock levels, BOPIS) |
| Cross-channel fulfillment at POS | BOPIS, buy-in-store-ship, email carts, local delivery | click & collect, in-store pickup, delivery | BOPIS via integrations |
| Cross-channel tender/value | gift cards redeemable in store or online | gift cards (Square ecosystem) | gift cards (offline limitation: "check gift card balance" unavailable offline) |
| Online channel ownership | native (Shopify platform) | bundled sibling (Square Online) or external | external (Shopify/WooCommerce/Magento integrations) |
| Sync posture | native, continuous | native, continuous | integration-based; offline cache-and-reconcile variant |
| Packaging | one product, posture | plan of one product + bundled online store | one product + integration layer |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

The Retail POS sale spine **plus** the cross-channel layer that makes it "omnichannel":

1. **The retail sale spine, executed live in person on a store-operated surface** — store-defined priced catalog → operator-composed sale → tender → completed transaction record + receipt (inherited from Retail Point of Sale; remove → not a POS at all).
2. **Unified cross-channel commerce state** — one shared record set (catalog with prices, inventory/stock, customer profiles, and orders) spanning the retailer's in-person channel and its online channels, so that a sale or stock change in one channel is visible in the other. Remove → a standalone Retail POS with disconnected online selling (i.e., plain Retail POS + separate e-commerce).
3. **Cross-channel fulfillment and reversal flows executed at the POS** — the register (or its operator) acts on orders that originated in another channel and sends in-store activity to other channels: fulfilling a buy-online-pickup-in-store order, ordering an out-of-stock item in store for home shipping, accepting a return of an online purchase at the counter, honoring a gift card across channels. Remove → channels coexist but do not interoperate; the "omni" claim collapses.

Jointly-held load-bearing checks:

- 1 alone = Retail Point of Sale (the sibling Type).
- 2 alone = an e-commerce platform / commerce back office (no in-person sale surface).
- 3 without 2 = manual cross-channel workarounds (phone calls, spreadsheets) — not a system capability.
- 2+3 without 1 = order management / fulfillment software, not a POS.
- 1+2 without 3 = synced-but-siloed selling; the customer-facing cross-channel journeys (the substance of "omnichannel") do not exist.

### L1 — Common Mature Structure

- Real-time (or near-real-time) sync posture as the default; offline cache-and-reconcile as a reliability variant.
- Cross-channel gift cards / stored value redeemable in any channel.
- Customer profile with cross-channel order history surfaced at the register ("know your customer in store and online").
- Multi-location inventory visibility at the POS (which location has the item).
- Endless-aisle patterns: in-store ordering of items not on the shelf.
- Cross-channel reporting (sales by channel from one back office).

### L2 — Variant / Optional Structure

- **Online-channel ownership**: native platform-owned storefront (Shopify), bundled sibling storefront (Square Online), or external storefront via integration (Erply + Shopify/WooCommerce/Magento). This is a packaging axis, not the identity.
- **Sync topology**: native single-platform state vs. integration/synchronization layer between separate systems; continuous vs. cached-and-reconciled.
- **Fulfillment menu**: which cross-channel options are offered (BOPIS, curbside, ship-from-store, local delivery, email carts) — varies by product and plan.
- **Scale posture**: single store vs. chain/franchise with HQ synchronization.
- **Channel breadth**: beyond online store — social commerce, marketplaces, Google product listings.

### L3 — Vendor-specific (Research Notes only)

- Shopify's "email virtual carts" (browse in store, buy online) is a distinctive flow; not observed in the other sampled products.
- Square's pickup configuration lives in the Dashboard's Fulfillment methods with item-level pickup assignment and auto-calculated pickup timing; quantity limits for pickup orders.
- Erply's offline-mode feature matrix (what works/doesn't offline: no customer search, no pickup orders, no gift-card balance check offline) is product-specific operational detail.
- Shopify's interchange of "multichannel POS" and "omnichannel" in its own FAQ — terminology is vendor marketing, not a stable taxonomy.

## Vendor-specific Findings

See L3. Additionally: Shopify's case-study-driven marketing (Kowtow, tokyobike, elph ceramics) and its claim that third-party-API integrations suffer "slow refresh rates" are vendor positioning — not treated as evidence about the Type.

## Boundary Findings

- **vs Retail Point of Sale**: the sale machinery is identical (both siblings' passes already established the shared spine). The boundary is the cross-channel layer: unified commerce state + cross-channel fulfillment executed at the register. Remove the unified state and cross-channel flows from an Omnichannel POS and you have exactly a Retail POS. Conversely, a Retail POS that later gains a synced online store becomes an Omnichannel POS without changing its register behavior.
- **vs Mobile POS**: orthogonal axes — Mobile POS is defined by the sale surface's portability; Omnichannel POS by channel integration depth. A handheld used for line-busting inside an omnichannel stack is both; the Types classify different properties of the same sale spine.
- **vs E-commerce Platform**: the e-commerce platform owns the customer's remote buying surface; the Omnichannel POS is the store-side sale-execution surface that shares state with it. In the Shopify pole the same vendor ships both, but they remain different surfaces with different users.
- **vs Order Management System**: the OMS orchestrates orders across channels/fulfillment nodes as its primary object; the Omnichannel POS executes in-person sales and handles the store-side slice of cross-channel orders. The POS's order surface is a window onto shared order state, not an orchestration engine.
- **vs Checkout Platform**: remote customer self-service vs. staff-operated in-person sale surface.
- **Historical check (§24-style)**: a pre-e-commerce electronic cash register — or a modern standalone single-channel POS — does **not** satisfy L0 legs 2–3. This is expected and confirms the boundary: the Type is defined by the unified-commerce era. It also supports the siblings' observation that "omnichannel" names a posture of the retail POS product family rather than a different machine: the same register, connected.
- **Taxonomy disposition**: no standalone "omnichannel POS" product family distinct from retail POS vendors surfaced in research; all sampled products are retail POS products whose omnichannel capability is a posture/plan/integration layer. The leaf is best understood as the **channel-depth-defined sibling** of Retail POS (parallel to Mobile POS as the surface-defined sibling). Keep as a sibling leaf with the trio recorded as the canonical merge candidate; do not merge unilaterally.

## Uncertainties

- Lightspeed Retail — the most prominent "omnichannel retail POS" brand — could not be fetched; its confirmation of the pattern is inferred from market position and the Shopify case study, not direct observation.
- Erply's own "omnichannel" page was not reachable as such (URL serves the Offline Mode article); Erply's omnichannel capability is reconstructed from its E-commerce integration documentation. Its BOPIS support is documented at the integration-comparison level, not as a step-by-step POS workflow.
- Square's deep help-center detail for Square for Retail was not reachable (article redirect); its evidence is at features/capabilities-page level plus one Square Online pickup article.
- Whether enterprise-grade omnichannel POS (Oracle, Toshiba, Aptos class) realizes the same core differently was not researched; the sample skews SMB/mid-market.

## Final Synthesis

An Omnichannel POS is a retail point of sale whose register operates on **shared commerce state spanning the retailer's in-person and online channels**, and whose operator can **execute cross-channel fulfillment and reversals at the counter** — pick up an online order, order an online item for a customer in store, take a return of an online purchase, redeem a gift card across channels. The sale machinery is the retail POS machinery; what defines this Type is that the register is a live window onto one unified commerce state rather than an isolated store ledger. The online channel may be native, bundled, or integrated — that is packaging, not identity. The Type is the channel-depth sibling of Retail Point of Sale and Mobile POS; all three share one sale spine and are shipped by vendors as modes of single product families, making the trio the canonical merge candidate if surface/channel-defined siblings are ever consolidated.
