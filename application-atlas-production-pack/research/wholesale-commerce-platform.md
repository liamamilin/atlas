# Research Notes — Wholesale Commerce Platform

## Research Goal

Understand what a Wholesale Commerce Platform actually is as an Application Type: the seller-side system a wholesaler, brand, distributor, or manufacturer uses to sell goods to business buyers (retailers, dealers, other businesses) through digital ordering surfaces, and how the resulting orders are managed through fulfillment and payment.

## Initial Boundary

Initial hypothesis: this leaf sits in the B2B Commerce family (05.17) between:

- **B2B E-commerce Platform** — the generic sibling; wholesale may be a Variant of it
- **Dealer / Distributor Commerce Portal** — the manufacturer→dealer sibling
- **E-commerce Platform / Online Store Builder** — B2C, anonymous shoppers
- **Online Marketplace** — multi-seller venue
- **Order Management System / OMS** — back-office only, no buyer-facing commerce surface
- **Sales-order capture / CPQ** — order capture without a standing buyer-facing storefront

Key early question: is "wholesale" a distinct Type or an audience Variant of B2B E-commerce? The directory keeps three leaves in 05.17; this pass documents the wholesale pole and records the seam.

## Research Questions

1. Who are the two sides of the system (seller operator, buyer users) and what roles exist on each?
2. What does a buyer account mean here — how is access controlled, and why?
3. How is the wholesale offer presented (catalog, variants, case packs, price lists)?
4. How does account-specific pricing work (price lists, discounts, terms)?
5. Through which channels do orders enter (self-service portal, sales rep, phone/email entry)?
6. What is the order lifecycle — how do order, invoice, shipment, payment relate? Partial shipments, backorders, deposits?
7. How do payments work — prepay vs net terms, credit memos, statements?
8. What integrations are structural (ERP, accounting, shipping)?
9. Where is the boundary with B2C e-commerce, marketplaces, and OMS?

## Representative Products

Selected for market representability, documentation quality, and different product philosophies / customer tiers:

| Product | Philosophy / pole | Segment |
|---|---|---|
| NuORDER (by Lightspeed) | brand-side wholesale commerce + retailer buying/assortment tools + network marketplace | fashion/lifestyle brands, department stores |
| JOOR | network-centric fashion wholesale: virtual showrooms, linesheets, embedded payments, digital tradeshows | fashion brands & retail buyers |
| Zoey | B2B ordering platform for wholesale distributors: multi-document OMS + storefront + rep mobile app | distributors, manufacturers, B2B brands |
| B2B Wave | lightweight out-of-the-box B2B ecommerce for wholesalers/distributors | SMB wholesalers, brands, manufacturers |

## Sources

- NuORDER — https://www.nuorder.com/ (product pages: /wholesale/, order management, integrated payments); Knowledge Base https://helpdesk.nuorder.com/hc/en-us/ (listed, not deep-fetched)
- JOOR — https://www.joor.com/ (brands, retailers, wholesale-management, joor-pay, order-management pages); Help Center https://help.jooraccess.com/hc (listed, not deep-fetched)
- Zoey — https://www.zoey.com/ (homepage, /features/order-management/ deep-fetched); support docs https://support.zoey.com/ (listed)
- B2B Wave — https://www.b2bwave.com/ (homepage, feature sections); Knowledge Base https://docs.b2bwave.com/ (category structure fetched)

Research date: 2026-09-10. All four vendor sites fetched successfully. Deep help-center articles were fetched for Zoey (order management feature page) and B2B Wave (KB category structure); NuORDER and JOOR evidence is mainly from official product pages (Tier 2), so operational detail from those two is held at lower assertion strength.

## Product Observations

### NuORDER (evidence layer A, product pages)

- Positions as "the global B2B commerce platform" for wholesale selling and buying.
- Brand side: "fully-branded wholesale website" accepting orders 24/7; **account-specific pricing, discounts, and product selections**; built-in reporting for sales trends and upsell.
- Order management module; integrated payments; flexible configurations.
- Retailer side: Assortments platform (visual roll-ups to catch duplicate buys, inventory allocation, collaborative editing) — a buying-side planning layer.
- Marketplace: discover/connect with 3,000+ brands, browse digital catalogs, centralized order management and fulfillment tracking.
- 120+ ERP, PLM, POS integrations feeding "real-time product, inventory, and order data."
- Case study framing: moving wholesale orders to self-serve.

### JOOR (evidence layer A, product pages)

- "B2B wholesale fashion platform": brands, distributors, showrooms sell; retailers buy.
- Selling: **virtual showrooms, digital linesheets, B2B order management**, reporting; JOOR Pay embedded payments ("get paid by retailers").
- Buying: source new brands (Discover marketplace), visual assortment planning, "place, edit, and pay for orders with brand partners in one platform."
- 100+ ERP/PLM integrations; Shopify sync app for retailers.
- Digital tradeshows (JOOR Passport) — network/tradeshow digitization layer.
- Network framing: 14,000+ brands, 700,000+ retail buyers.

### Zoey (evidence layer A, homepage + order-management feature page)

- "B2B ordering platform built for wholesale distributors": orders come in "by phone, email, trade show, and self-service portal — Zoey puts all of it in one place."
- **Multi-document OMS**: "Sales Orders are separate from Invoices which are also separate from Shipments and Payments" — matches ERP document types, explicitly contrasted with "B2C ecommerce data model."
- Invoices: item substitutions, quantity/price adjustments, revised shipping, early-pay discounts, late fees, surcharges, adjusted tax, deposit/balance; auto-pay from saved card/bank or emailed for payment; net terms with early-pay discounts/late fees applied at payment time.
- Shipments: partial shipments, multiple tracking numbers, 3rd-party fulfillment imports, packing slips.
- Payments & credit memos: pay at order submission or later on invoice; per-customer pre-pay vs terms/invoice/statement; saved cards; credit memos to account.
- Custom order status workflows; pick lists (single and consolidated); deposits (partial invoice/payment, balance later); statements over AR.
- Storefront: buyer self-service portal — "their pricing, their history, reorder in seconds."
- Rep mobile app: write orders online/offline, scan barcodes, capture payment.
- Sales CRM (contacts, accounts, activity, order history); quotes → cart conversion; AR automation; ERP/accounting sync (NetSuite, QuickBooks).

### B2B Wave (evidence layer A, homepage + KB structure)

- "B2B ecommerce platform" for wholesale distributors, brands, manufacturers, suppliers.
- **Access-protected** branded wholesale website; mass product import with variants and inventory status.
- Personalized product lists; **privacy groups** controlling which customers see which products; PDF catalogs per customer.
- Customer management: profiles, **approving registrations**, custom prices, personalized discounts, custom tax rates, personalized shipping options.
- Order management: new orders, **reorders, backorders**, order history, order status, auto-synced inventory and shipping.
- Pricing & payment: personalized prices, MSRP listing, price adjustment for product options, multiple payment options; master price list import via file upload.
- Sales rep management: rep accounts, placing orders for customers, permissions, rep performance reporting.
- Reporting: order summary, customer activity, product sales, inventory, rep performance, coupons.
- Integrations: QuickBooks, Xero, Stripe, ShipStation, Zapier, API.
- KB categories confirm operational surfaces: storefront, products, price management, customer management, sales rep management, payments, importing/exporting.

## Cross-product Comparison

| Structure | NuORDER | JOOR | Zoey | B2B Wave | Reading |
|---|---|---|---|---|---|
| Seller-operated platform with buyer-facing ordering surface | ✓ | ✓ | ✓ | ✓ | Core |
| Identified business-buyer accounts with controlled access (registration/approval, gated catalog) | ✓ (account-specific selections) | ✓ (vetted network) | ✓ (per-customer config) | ✓ (approval, privacy groups) | Core |
| Wholesale catalog with variants + inventory visibility | ✓ | ✓ | ✓ | ✓ | Core |
| Account-specific pricing / price lists / discounts | ✓ | ✓ (via terms) | ✓ | ✓ | Core-adjacent (universal in sample; see L1 note) |
| Multi-channel order capture (self-service portal + rep + staff-entered phone/email) | ✓ (self-serve emphasis) | ✓ | ✓ (explicit) | ✓ (rep mgmt) | Core |
| Order lifecycle as separate documents: order → invoice → shipment → payment | ✓ (order mgmt) | ✓ | ✓ (explicit multi-document OMS) | ✓ (order status/history) | Core |
| Partial fulfillment / backorders | implied | implied | ✓ explicit | ✓ explicit | Common |
| Net terms vs prepay; credit memos; statements | ✓ (payments) | ✓ (JOOR Pay) | ✓ explicit | ✓ (payments KB) | Common |
| Reordering from history | ✓ | ✓ | ✓ | ✓ | Common |
| Quotes | — | — | ✓ | ✓ (orders & quotes) | Common |
| Sales rep layer (rep accounts, order-on-behalf, credit) | ✓ | ✓ | ✓ | ✓ | Common |
| ERP/accounting/shipping integrations | ✓ | ✓ | ✓ | ✓ | Common |
| Network/marketplace discovery layer (multi-brand) | ✓ | ✓ | — | — | Variant (network pole) |
| Buying-side assortment planning | ✓ | ✓ | — | — | Variant (fashion/retail pole) |
| Virtual showrooms / linesheets / digital tradeshows | — | ✓ | — | — | Vendor/industry-specific (fashion) |
| PDF catalogs | — | — | — | ✓ | Variant |
| AR automation / statements | — | — | ✓ | partial | Variant |

## Canonical Model (abstraction layers)

### L0 — Defining Invariant

A **seller-operated commerce platform for business buyers**, where:

1. **Gated business-buyer accounts** — buyers participate as identified business customer accounts (company-level, with user logins), not anonymous shoppers; access to the offer is controlled by the seller (registration/approval, catalog visibility).
2. **The wholesale offer presented per account** — a product catalog (with variants and inventory) whose commercial presentation (pricing, discounts, visible selection, terms) is configured per account or account group.
3. **Orders against the account flowing into a managed B2B order lifecycle** — an order record that progresses through fulfillment and invoicing to payment, supporting the partial/backorder realities of wholesale trade.

Remove (1) → anonymous B2C storefront (E-commerce Platform). Remove (2) → a storefront with no wholesale commercial semantics. Remove (3) → a catalog/price-list publication tool, not commerce.

### L1 — Common Mature Structure

- Account-specific pricing machinery (price lists, tiered/customer discounts, terms)
- Multi-channel order capture: buyer self-service portal, sales-rep order writing (often mobile, sometimes offline), staff entry of phone/email orders
- Reordering from order history; order status visibility for buyers
- Net-terms payment posture alongside prepay; credit memos; statements
- Quotes → orders
- Sales rep management (accounts, permissions, order-on-behalf, performance)
- ERP / accounting / shipping integrations as the assumed data spine
- Reporting (orders, customers, products, reps)

### L2 — Variant / Optional Structure

- Network/marketplace layer connecting many brands with many retail buyers (NuORDER, JOOR)
- Buying-side assortment planning tools (department-store/specialty-retail pole)
- Industry packaging: fashion (virtual showrooms, linesheets, digital tradeshows), food/beverage, building materials, etc.
- PDF catalog generation
- AR automation suites, deposits/pre-orders, custom order-status workflows
- Dropshipping / supplier-feed modes

### L3 — Vendor-specific

- JOOR Passport (digital tradeshow portal), JOOR Pay branding
- NuORDER Assortments (visual roll-ups, size curves)
- Zoey's multi-document OMS framing and pick-list consolidation options
- B2B Wave privacy groups naming, MSRP listing mode

## Historical / Market-Sample Check

Would older, regional, or non-web wholesale commerce still fit the L0? Yes: the paper-era wholesale relationship — a trade account with the wholesaler, a wholesale price list, orders placed by mail/phone/rep order-book, invoices and partial shipments, payment on terms — satisfies all three L0 legs without any web storefront. The web storefront, portal, and rep app are the modern realization of the order-capture surface, not the definition. Conversely, a modern B2C-style storefront with anonymous checkout fails leg (1) and is not wholesale commerce. The definition therefore does not over-fit to the current SaaS portal pattern.

## Vendor-specific Findings

- JOOR: fashion-industry packaging (showrooms, linesheets, Passport tradeshows, Studio photography services).
- NuORDER: Assortments buying platform; marketplace network scale claims.
- Zoey: explicit multi-document OMS doctrine; pick lists; deposits; custom statuses.
- B2B Wave: privacy groups; PDF catalogs; MSRP listing.

## Boundary Findings

- **vs E-commerce Platform / Online Store Builder (B2C)**: B2C serves anonymous or consumer accounts with a single public price; wholesale requires gated business accounts and per-account commercial terms. Remove account gating + per-account terms → B2C storefront.
- **vs B2B E-commerce Platform (sibling leaf)**: same family; the wholesale pole is defined by wholesale trade semantics (trade accounts, wholesale price lists/terms, case/variant ordering, net terms, partial fulfillment). The generic B2B leaf also covers non-wholesale B2B (services, SaaS-style B2B checkout). Likely overlapping leaves; recorded as a taxonomy seam, keep-both with wholesale as the trade-goods pole.
- **vs Dealer / Distributor Commerce Portal (sibling leaf)**: the dealer portal is the manufacturer→authorized-dealer relationship variant (dealer networks, franchise/authorization semantics). Wholesale commerce is the broader trade-goods pattern; dealer portal is a relationship-shaped variant. Boundary deserves its own pass.
- **vs Online Marketplace**: marketplace is a multi-seller venue where the operator is not the seller of record; wholesale commerce platform is seller-operated (the wholesaler runs it for its own buyers). Network products (NuORDER/JOOR marketplace layers) add a marketplace layer on top — that layer is Variant, not core.
- **vs Order Management System / OMS**: OMS is back-office order processing without a buyer-facing commerce surface; the wholesale platform's defining surface includes the buyer-facing ordering portal. Zoey bundles an OMS inside the platform — packaging, not identity.
- **vs Sales-order capture / CPQ / Sales Rep apps**: those are single-channel order-capture tools; the wholesale platform is the whole seller-side commerce system including the buyer portal and account/price machinery.
- **vs Product Information Management / Catalog**: PIM manages product data with no transactions or buyer accounts.

**Decisive test**: remove the gated business-buyer accounts and per-account commercial terms → it becomes a B2C e-commerce storefront; remove the buyer-facing ordering surface → it becomes an OMS/back-office; remove the order lifecycle → it becomes a catalog/price-list publisher.

## Uncertainties

- Exact order-status vocabularies, minimum-order quantities, MOQ handling, and per-product payment-term defaults were not consistently documented across the sample; no precise numbers asserted.
- NuORDER and JOOR operational detail (order editing rules, approval flows) rests on product pages, not deep help-center articles — assertions kept moderate.
- The seam between "Wholesale Commerce Platform" and "B2B E-commerce Platform" (and the dealer-portal sibling) is a directory-level question; flagged for STATUS Boundary Issues rather than resolved here.

## Final Synthesis

A Wholesale Commerce Platform is the seller-side commerce system of record for wholesale trade: the wholesaler/brand/distributor operates it; business buyers participate through gated accounts; the offer is presented per account with wholesale commercial terms; orders enter from multiple channels (buyer self-service, sales reps, staff entry) and are managed through a B2B order lifecycle of fulfillment, invoicing, and payment (prepay or net terms), with integrations to ERP/accounting/shipping as the assumed data spine. Its identity sits between B2C e-commerce (which it structurally resembles) and back-office OMS (which it contains), distinguished by the gated-account + per-account-terms + trade-lifecycle triad.
