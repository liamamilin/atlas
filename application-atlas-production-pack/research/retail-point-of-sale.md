# Research Notes — Retail Point of Sale

Research date: **2026-09-06**
Methodology: `WORKFLOW_v1.1.md` + `WRITING_GUIDE_v1.1.md` (v1.1)

---

## Research Goal

Understand what a Retail Point of Sale (POS) application actually is as an Application Type: its core objects, the sale lifecycle, who operates it, what rules and permissions shape it, and where its boundary lies against Restaurant POS, e-commerce checkout, payment processing, retail inventory management, and the sibling directory leaves (Mobile POS, Omnichannel POS).

## Initial Boundary

Initial hypothesis (before research):

- Core use: an operator-facing transaction application used at a physical retail point of sale to compose a sale from a priced product catalog, collect payment, and record the completed transaction.
- Primary users: cashier / sales associate; shift manager (overrides, refunds); owner/admin (catalog, taxes, employees, reports).
- Nearest types: Restaurant POS (different sale semantics), Mobile POS and Omnichannel POS (siblings under 05.10, likely variants), Checkout Platform (customer self-service, remote), Payment Processing Platform (money rails), Retail Inventory Management (back office), Loyalty / Gift Card Management (attached modules).
- Unknowns: exact sale lifecycle states across products; how returns/exchanges are modeled; cash/shift management depth; offline behavior; where the POS/back-office line sits.

## Research Questions

1. What objects constitute a sale (cart / basket / ticket / order) and what is its lifecycle?
2. How does the product catalog (items, variations, barcodes, prices, taxes) feed the sale?
3. What tender/payment flows exist (cash, card, split, change, refunds)?
4. What roles and permissions gate sensitive actions (void, refund, discount)?
5. What register / shift / cash-management structures exist?
6. What hardware surfaces participate (scanner, printer, drawer, card terminal), and what form factors exist (counter, mobile, kiosk)?
7. What back-office surfaces exist, and where is the POS / back-office line?
8. How do returns, refunds, and exchanges work?
9. Where do customer records and loyalty attach?
10. Where is the boundary against Restaurant POS, checkout platforms, payment processing, and inventory management?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Tier / philosophy | Why selected |
|---|---|---|
| Square Point of Sale (incl. Square for Retail) | Micro-SMB; payments-first; software free, hardware light | Best-in-class public help center; defines the modern minimal POS |
| Shopify POS | SMB; commerce-platform-first; omnichannel by design | POS as a surface of a unified commerce back office |
| Clover (Fiserv) | SMB–mid; hardware-first; app-market platform | Official developer docs expose the full data model and payment semantics |
| Loyverse | Global SMB; mobile-first, free core, app-marketplace | Non-US-centric sample; strong article inventory across sales/shifts/tickets |
| Erply | Mid-market/enterprise; back-office-heavy; multi-country fiscal | Chain/franchise, sales-document model, user-group permissions, fiscal POS editions |

## Sources

### Square (official help center — Tier 1)

- Support center root: https://squareup.com/help/us/en
- Payments topic (article inventory): https://squareup.com/help/us/en/topic/payments
- Items and inventory topic (article inventory): https://squareup.com/help/us/en/topic/items-and-inventory
- Accept payments with Square Register (full article): https://squareup.com/help/us/en/article/6255-x2-accept-payments-on-your-square-register
- Process a return, exchange, or unlinked refund (full article): https://squareup.com/help/us/en/article/6350-process-a-return-or-exchange-with-square-for-retail
- Accept cash and checks with Square (full article): https://squareup.com/help/us/en/article/5177-accept-cash-and-checks-with-square
- Referenced titles (not individually fetched): split payments (5097), discounts (5362), custom sale amounts (5429), offline payments (7777), cash drawer management (5152), build your customer's cart in the retail POS app (8238), checkout your customer with the retail POS app (8239), customize payment types (6389), print receipts (6139), settle payments and manage tips (8375 — fetched; content confirms settlement states and POS modes)

### Shopify (official product page — Tier 2; help center inaccessible)

- POS product page incl. FAQ: https://www.shopify.com/pos
- Limitation: https://help.shopify.com/en/manual/sell-in-person returned HTTP 403 (twice-confirmed pattern; not retried further). Shopify-specific operational detail is therefore kept generic.

### Clover (official developer documentation — Tier 1 for structure; merchant help center is a JS app and returned no content)

- Docs root: https://docs.clover.com/
- Data model: https://docs.clover.com/dev/docs/clover-data-model.md
- Create an atomic order: https://docs.clover.com/dev/docs/create-an-atomic-order.md
- Transaction types (sale / auth / pre-auth / closeout / partial payments): https://docs.clover.com/dev/docs/transaction-types.md

### Loyverse (official help center — Tier 1 for capability inventory; article bodies 404)

- Help center root and Sales topic (article inventory): https://loyverse.com/help , https://loyverse.com/help/sales
- Limitation: individual article URLs (e.g. /help/make-sales, /help/shift-management-loyverse-pos, with and without locale prefix) returned 404. Capability existence is evidenced by the official topic inventory; article-level detail was not verified.

### Erply (official wiki — Tier 1)

- Wiki root (section inventory): https://wiki.erply.com/
- Which user rights are required to make a sale in Brazil POS: https://wiki.erply.com/article/2511-which-user-rights-are-required-to-make-a-sale-in-brazil-pos

---

## Product A — Square Point of Sale / Square for Retail

### Key observations (evidence layer A — directly observed)

- **Checkout flow (Register article)**: add items to the current sale from the item Library or Favorites tab; scan an item's barcode with a SKU saved to the Item Library; tap a line to select a variation or modifier, adjust quantity, add a note, or remove; tap **Charge**; customer pays (tap / dip / swipe; also cash, checks, gift cards, wallets); confirmation screen; customer can enter phone/email for a digital receipt; final "All Done" screen; payment can be canceled before processing completes.
- **Permissions**: articles are explicitly scoped — "checkout permission to take payments", "transactions permission to issue refunds / issue unlinked refunds"; permissions are set in the Square Dashboard (team permissions). Manager-level gating of sensitive actions is therefore structural.
- **Returns / exchanges / unlinked refunds (retail mode)**: three distinct flows — **Refund** (money back), **Return** (money back + item restocked to inventory), **Exchange** (return + replacement item; cart total adjusts to the price difference and can be positive, negative, or even). **Unlinked refund** = refund not linked to an earlier POS payment (no receipt / other channel), explicitly flagged as a fraud-risk action. Refunds can be issued to gift cards (store credit). Refund records show reason, amount, date, time, and the cashier who processed it.
- **Tender set**: payment cards, mobile wallets, gift cards (Square and third-party), cash, checks, card on file, house accounts (charge to a customer account), QR/wallet payments, BNPL (Afterpay), EBT SNAP, bitcoin (region-dependent), and "Custom Payment Methods" for recording externally processed transactions. Cash drawer automatically opens when cash is tendered on a connected drawer; cash rounding exists as a regional feature.
- **Split payments** and **custom sale amounts** (amount-only sale without catalog item) exist as first-class flows.
- **Item library / catalog**: items with variations and options, modifiers, categories, discounts, unit types including weight/decimal quantities, age-restricted items requiring age verification, item grid layout, sold-out marking, bundles, bottle deposits; inventory tracking with counts, adjustments, transfers between locations, purchase orders, vendors, SKUs, GTINs, barcode label printing.
- **Offline mode** exists (process card payments offline; view offline payments) — availability is product/region dependent.
- **Settlement states**: payments can be unsettled (e.g., awaiting tip) and later settled; settled payments appear in transfers and reports. Square POS ships in modes (standard, retail, quick service, full service, bar) — the same transaction core with different sale semantics.
- **Hardware surfaces**: Register (dual display: seller-facing POS + customer-facing display), Stand, Terminal, Handheld, phone/tablet readers, Tap to Pay, Kiosk (self-service), Virtual Terminal (amount-only, browser).

## Product B — Shopify POS

### Key observations (evidence layer A for positioning/flow; help-center detail inaccessible)

- **Positioning**: "POS system … to process transactions and accept payments in person"; POS is one selling surface of a unified back office that also runs the online store; inventory, payments, and customer data are synced across channels.
- **Documented checkout flow (product FAQ)**: 1) scan items to add them to the customer's cart; 2) POS calculates the order total including sales tax; 3) select Checkout — integrated hardware is ready to take payment; 4) customer pays by card / debit / digital wallet; 5) POS generates a receipt (print or email); 6) POS captures order and customer data and automatically updates inventory levels.
- **POS types taxonomy (vendor's own)**: countertop POS (permanent stores), mobile POS (pop-ups, markets, line-busting), multichannel POS (in-store + online, BOPIS / ship-to-home). This is vendor marketing taxonomy but confirms surface and channel are the axes of variation, not the core model.
- **Hardware**: tablet/phone app + payment terminal + cash drawer; optional receipt printer and barcode scanner.
- **Staff management**: "set staff permissions to control what employees can access."
- **Limitation**: help center (operational detail: returns, cash management, offline) returned 403; Shopify-specific claims kept at the level of the product page.

## Product C — Clover

### Key observations (evidence layer A — developer documentation; merchant UI inferred from data model)

- **Data model (official)**: Merchant (central association point) → Employees (take orders; associated with orders and payments), Customers (optional on orders; card-on-file tokens), **Inventory** (items with variants; modifiers "capture additional details about the item"; categories; tags; stock quantities tracked by default, can be turned off; items can be entered individually, scanned by barcode, or imported from a spreadsheet), **Orders** ("the core of Clover's transaction data; almost every transaction creates or updates an order"; order ↔ 0..1 customer, ↔ merchant, ↔ 0..n employees), **Payments** (associated with merchant, employee, 0..n customers).
- **Order lifecycle (atomic order)**: build an order cart (line items, modifiers, discounts, service charges; ad hoc / non-catalog items allowed) → "checkout" computes totals and taxes without finalizing → create the order record (visible on Merchant Dashboard and devices) → pay for the order. Error semantics: empty cart, nonexistent item, invalid modifier/discount. Order types classify orders (online, delivery, pick-up, dine-in).
- **Payment transaction types**: **sale** (authorize + settle at once), **auth** (tip-adjustable until closeout), **pre-auth** (hold, then capture; partial capture returns the remainder), **closeout** (batch settlement starting merchant funding), **partial payments** (insufficient funds → accept partial + second tender, or void), voids and refunds, offline payments handling. These are payment-layer semantics the POS orchestrates.
- **Platform shape**: Android-based POS devices; open app market; merchant manages employees, inventory, customers via device apps and a Web Dashboard; regional editions (US, Canada, UK/Ireland, Germany/Austria, Argentina) with region-specific payment flows; EBT support; custom tenders.
- **Limitation**: merchant-facing help center is a JS app (no content). Merchant UI flows are inferred from the data model and API docs, not observed directly; UI-level claims kept generic.

## Product D — Loyverse

### Key observations (evidence layer A for capability inventory; article bodies 404)

- Official Sales topic inventory (titles only): How to Make Sales; How to Issue a Refund; Sell Items by Weight; Sell Liquids; **Offline Use of Loyverse POS**; Dining Options; Sale Screen arrangement; Favorites; Home Sale Screen Layouts; Print Bill; Cancel Receipts (back office); Receipts List in the POS; Email Receipts; **Shift Management in Loyverse POS**; **Open Tickets** (work with / split / merge / predefined tickets named as tables / synchronization); Apply Discounts During a Sale; Set Up and Apply Modifiers; Redeem Customer Points for a Discount; Sell Items Using Barcode Scanners; Barcode Scanning by Built-in Camera; Barcodes with Embedded Weight; Accept Credit Card Payments; **Split Payment**; Cash Rounding.
- Companion products: Dashboard (back office), Kitchen Display, Customer Display, Inventory Management, Employee Management — i.e., POS app + back office + optional vertical modules.
- Interpretation: same core (catalog → sale → tender → receipt), same L1 set (discounts, modifiers, split payment, refunds, shifts, open tickets, barcodes incl. scale barcodes, cash rounding, offline). "Open tickets" and dining options show restaurant semantics available as a mode/module in a retail-capable product.
- Limitation: article bodies returned 404; detail claims not verified beyond titles.

## Product E — Erply

### Key observations (evidence layer A)

- **Permissions**: making a sale requires user rights — a support article instructs granting "Invoices" and "Payments" rights to a user group so users can make sales in POS. Sales are modeled as **sales documents (invoices)** with associated payments — a document-centric retail back office.
- **Product shape**: cloud POS + back office (Customers, Sales, PIM, Inventory, Purchase, Retail Chain) + POS editions (BerlinPOS, BrazilPOS, Flax POS, **Self-Service POS**, **Mobile POS**) + chain/franchise synchronization (HQ → stores) + integrations (e-commerce platforms, accounting, EDI, fiscal: Poland PosNet, EFSTA fiscalization) + Erply Payments (Adyen terminals).
- **Regional/fiscal depth**: VAT handling (e.g., a VAT-rate change article), cash transaction rounding (EU), fiscal printer integrations, country-specific POS editions (Brazil, Berlin) — confirms fiscal/regional adaptation as a variant axis.
- Interpretation: at the enterprise end, the POS is one surface of a retail suite; the sale remains a document with items and payments, gated by user-group rights, executed on multiple surface types (counter, mobile, self-service).

---

## Cross-product Comparison

| Dimension | Square | Shopify POS | Clover | Loyverse | Erply |
|---|---|---|---|---|---|
| Priced item catalog | Item Library (items, variations, modifiers, categories, SKUs/GTINs) | Products from unified Shopify catalog | Inventory (items, variants, modifiers, categories, tags) | Items list (incl. by-weight items) | Products/PIM in back office |
| Sale object | "current sale" / cart → payment | Cart → order | Order (cart → checkout → order record → pay) | Receipt / open ticket | Sales document (invoice) + payments |
| Barcode scanning | Yes (SKU lookup; scan-to-create items) | Yes (documented in flow) | Yes (scan to add / create items) | Yes (scanner + camera; embedded-weight barcodes) | Yes (scan merchandise barcodes) |
| Variations / modifiers | Variations + modifiers | Variants | Variants + modifiers | Modifiers (+ variants in items) | Variants + modifiers |
| Discounts at sale time | Yes (line/sale discounts) | Yes (discounts feature) | Yes (discounts in order cart) | Yes (during sale; points redemption) | Yes (incl. loyalty discounts) |
| Custom amount sale (no catalog item) | Yes (custom sale amounts) | Not verified | Yes (ad hoc / non-Clover items) | Not verified | Not verified |
| Split / multi-tender | Yes (split payments) | Not verified | Yes (partial payments flow) | Yes (split payment) | Not verified |
| Cash tender + drawer | Yes (record cash; drawer auto-opens; cash management; rounding) | Yes (cash drawer in hardware set) | Yes (cash drawer; open-drawer API) | Yes (cash rounding; shifts) | Yes (cash rounding EU) |
| Returns / refunds / exchanges | Refund / Return (restock) / Exchange / Unlinked refund | Not verified (help 403) | Voids and refunds (payment layer) | Refunds; cancel receipts | Sales documents support credit/reflow (not verified in detail) |
| Customer attach at sale | Yes (customers; house accounts; card on file) | Yes (customer data captured at checkout) | Yes (0..1 customer per order) | Yes (customers; points) | Yes (customers in back office) |
| Permission gating | Checkout / transactions / refunds permissions per team member | Staff permissions | Employee records; app permissions | Employee roles (per topic inventory) | User groups; "Invoices"+"Payments" rights required to sell |
| Inventory decrement on sale | Yes (tracking; counts; transfers) | Yes (auto-updates inventory) | Yes (stock tracked by default; can be off) | Yes (inventory module) | Yes (inventory + WMS) |
| Receipt | Print / email / SMS; reprint | Print or email | Print (device printers; reprint API) | Print / email; receipts list | Fiscal + standard receipts |
| Reporting / back office | Dashboard (reports, transactions) | Unified admin | Merchant Dashboard | Dashboard | Back office + chain HQ |
| Offline mode | Yes (offline payments) | Not verified | Offline payments handling (payment layer) | Yes (offline use) | Local-network/hybrid posture (microservices) |
| Omnichannel | Online store + POS; Google listings | Native (unified back office; BOPIS) | Ecommerce API; order types | Marketplace integrations | E-commerce platform integrations |
| Kiosk / self-service | Square Kiosk | Not verified | Kiosk integration docs | Customer display (not kiosk) | Self-Service POS edition |
| Restaurant semantics available | Yes (restaurant modes of same app) | No (retail-focused) | Yes (order types incl. dine-in; modifiers) | Yes (dining options, KDS) | Limited (separate verticals) |

**Reading**: every product implements the same spine — a store-defined priced catalog, an operator-composed sale, tender collection, and a completed, recorded transaction with a receipt. Everything else varies by tier, region, and vendor philosophy.

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

```text
Store-defined priced item catalog
└── Sale construction (operator composes basket of catalog items + quantities; system prices it, incl. tax)
    └── Payment collection (≥1 tender settles the basket)
        └── Completed transaction record + receipt
```

Executed **live, in person, at the point of exchange, on a store-operated surface** (staff-operated register, handheld, or store-controlled self-service kiosk).

Five properties. Removal tests:

- Remove the **priced item catalog** → the product becomes an amount-entry payment terminal / virtual terminal, not a POS.
- Remove **sale construction from catalog items** → same failure; a bare card charge is not a sale.
- Remove **payment collection** → quoting / wish list, not a POS.
- Remove the **completed transaction record + receipt** → an ephemeral calculator, not a retail system of record.
- Remove **live in-person execution at the point of exchange** → e-commerce checkout (remote, customer self-service), a different Type.

### Historical / market-sample check (§24)

- **1980s–90s electronic cash register (ECR)**: PLU table = priced catalog; ring-up = sale construction; cash tender; printed receipt + totals. Fits L0 with zero modern additions (no barcode scanning, no cloud, no customer records, no inventory decrement).
- **Regional fiscal POS** (Brazil, Poland, EU fiscalization): same L0 + fiscal receipt/printer as an L2 regional layer. Fits.
- **Market-stall mobile POS** (phone + card reader): fits; surface is L2.
- **Self-checkout kiosk**: fits; the "store-operated surface" wording deliberately includes customer-operated kiosks under store control.
- **Pure mechanical cash register** (amount keys only, no item-level entry): fails the catalog test — correctly excluded; it is ancestor hardware, not this software Type.
- Conclusion: L0 does not over-fit the current cloud/tablet era.

### L1 — Common Mature Structure

Present in most mature modern products; not required for the Type to be recognizable:

- **Item lookup surfaces**: barcode scan (SKU/GTIN), visual grid/favorites, search, manual/custom amount entry.
- **Item structure**: variations/variants, modifiers, categories; unit types incl. weight/scale items.
- **Price adjustment at sale time**: discounts (line/sale), price overrides, promotions; service charges/tips where relevant.
- **Sale-reversal flows**: refunds, returns (with restock), exchanges; voids before completion; unlinked refunds as a risk-gated exception.
- **Multi-tender / split payment**; cash tender with change computation; cash drawer integration.
- **Receipt**: printed, emailed, SMS; reprint.
- **Customer association**: attach a customer to the sale; store credit / house account / loyalty points redemption.
- **Cash & shift management**: cash drawer sessions, cash counts, shift open/close.
- **Held / parked sales** (open tickets / saved carts).
- **Employee accounts + permission gating**: sensitive actions (refund, void, discount, unlinked refund) require elevated rights or manager override; actions are attributed to the employee who performed them.
- **Inventory decrement on sale** and stock visibility at the POS.
- **Tax computation** (sales tax / VAT) at line or sale level.
- **Sales reporting** and a **back-office companion** (web dashboard) for catalog, employees, and reports.

### L2 — Variant / Optional Structure

- **Surface / form factor**: fixed counter register; tablet/handheld mobile POS; self-checkout kiosk; customer-facing display. (Maps to sibling leaves Mobile POS; kiosk is a surface variant.)
- **Channel integration depth**: standalone in-store only ↔ unified omnichannel (shared catalog/inventory/customers with e-commerce, BOPIS, ship-from-store). (Maps to sibling leaf Omnichannel POS.)
- **Deployment & reliability posture**: cloud-first vs local server; offline mode (none / payments-only / full).
- **Payments stack**: integrated processor (POS + processing from one vendor) vs BYO processor / external terminal vs processor-agnostic; settlement/closeout semantics follow the processor.
- **Vertical adaptations**: restaurant/quick-service modes (tables, checks, coursing, KDS), appointments/services, fuel, grocery (scale barcodes), age-restricted goods, EBT/benefits.
- **Regional / fiscal**: fiscal printers and certified receipts, VAT vs sales tax models, cash rounding rules, country editions.
- **Scale**: single register → multi-store chains/franchise with HQ synchronization.
- **Attached commerce modules**: loyalty, gift cards, marketing, payroll — modules, not the sale engine.

### L3 — Vendor-specific (research notes only; not in final document)

- **Square**: Item Library/Favorites; "retail mode" and Square for Retail app; hardware names (Register, Stand, Terminal, Handheld, Reader, Kiosk); Risk Manager; Cash App Pay; Afterpay; bitcoin sales; house accounts; custom payment methods; transfer/deposit schedules; offline-payment risk window; 36-hour tip settlement window.
- **Clover**: atomic-order API (checkout → create → pay); order types; sale/auth/pre-auth transaction types; closeout batching; App Market; Merchant Dashboard; item groups/tags; multiple service charges; region pills (US/CA/UK-IE/DE-AT/AR).
- **Shopify**: unified back office with online store; POS Pro/Lite plan split; Shopify Payments coupling; Shop-network features; hardware lineup.
- **Loyverse**: open-ticket synchronization across devices; kitchen display; customer display; advanced-inventory and employee-management add-ons; points-based loyalty.
- **Erply**: BerlinPOS/BrazilPOS/Flax editions; sales-document (invoice) model; user-group rights ("Invoices", "Payments"); Ground Control / chain sync; EFSTA/PosNet fiscal integrations; Adyen terminal integration; EU cash rounding.

---

## Vendor-specific Findings

See L3 above. Notable single-product findings that must not be promoted to the canonical core:

- Unlinked refunds as a named, risk-flagged flow (Square, product-specific naming; the underlying concept — refund without a linked prior payment — is plausibly general but was only directly observed in one product).
- "House accounts" (charge to a customer account, pay later) observed in Square only in this sample → Optional.
- Bitcoin tender (Square) and BNPL (Square/Shopify marketing) → Optional, region-dependent.
- Pre-auth/auth/closeout triad (Clover docs) is payment-industry standard semantics, but in this sample only Clover documents it explicitly → keep at payment-layer abstraction in the final document.

## Boundary Findings

### vs Restaurant POS (most important boundary)

Shared: the entire transaction spine (catalog-configured order → transaction → payment). Different: **sale semantics**. Retail: goods sale completed at the point of exchange; no table, no check lifecycle, no course production; returns/exchanges central; tips peripheral. Restaurant: order lives as an open check tied to a table/seat across a service period; items route to production (KDS); payment may come much later; tips/gratuity central.

**判据**: remove table/check/service-period semantics and production routing → you have a Retail POS. Add them as the primary structure → Restaurant POS. Field evidence that the boundary is semantic, not structural: the same vendor ships both as **modes of one application** (Square POS: standard/retail vs quick-service/full-service/bar modes; Loyverse: dining options + KDS modules; Clover: order types incl. dine-in). The two Types share L0 machinery; they differ in what a "sale" means while it is alive.

### vs Mobile POS / Omnichannel POS (sibling leaves under 05.10)

Both siblings implement the same L0 with a different axis of variation: Mobile POS = surface/form factor (handheld); Omnichannel POS = channel-integration depth (unified data with e-commerce). Vendors themselves treat these as configurations of one product (Shopify's own taxonomy: countertop / mobile / multichannel POS; Erply ships Mobile POS and Self-Service POS as editions of the same suite). **Assessment: both are likely Variants/Aliases of Retail Point of Sale rather than independent Types** — recorded as a taxonomy issue for review; this document treats them as L2 variants.

### vs Checkout Platform (05.06)

Checkout = customer self-service, remote (browser/app), no staff register, no in-person execution context, no store-operated surface. Remove the live in-person store-operated execution from POS → checkout. Remove the catalog/sale construction from POS → payment terminal.

### vs Payment Processing Platform / Payment Gateway (08)

Processing moves money (authorization, capture, settlement, chargebacks). POS composes and records the sale and *orchestrates* tender, delegating card processing to a processor (its own or external). Evidence: Clover documents sale/auth/pre-auth/closeout as its payments layer beneath the order; Square records cash/check/external payments it never processed. Remove sale construction → payment terminal/gateway; that product exists and is not called POS.

### vs Retail Inventory Management (05.12)

POS decrements stock and shows availability as a *side effect* of selling; Inventory Management plans, counts, receives, replenishes. Overlap exists (Square for Retail includes counts/transfer orders/purchase orders; Erply includes Inventory+WMS) — at the enterprise end the suite boundary blurs, but the POS surface remains the sale-execution surface.

### vs Loyalty / Gift Card Management (05.15)

Loyalty/gift cards attach to the sale as tender or discount sources; they are modules. A POS without them is still a POS.

### vs Self-checkout / kiosk

Surface variant (store-operated self-service surface), not a separate Type in this sample (Square Kiosk, Erply Self-Service POS). Recorded as L2.

## Uncertainties

1. **Shopify operational detail**: help center 403; returns/cash-management/offline behavior in Shopify POS not directly verified. Claims about Shopify kept to product-page level.
2. **Loyverse article bodies**: 404; capability inventory only. Shift-management and open-ticket *detail* unverified.
3. **Clover merchant UI**: developer docs verified the data model and flows; the merchant-facing UI was not directly observed.
4. **Held/parked sales in retail mode**: directly observed as "open tickets" in restaurant-leaning contexts (Loyverse, Square restaurant modes) and as saved carts in retail contexts (Square retail "build your customer's cart"); universality across retail products not verified → kept in L1 with qualified wording.
5. **Exact settlement semantics** (when money actually moves vs when the sale completes) vary by processor and region; kept conceptual in the final document.
6. **Erply sales-document model**: verified only via the permissions article and wiki structure; document-lifecycle detail not fetched.

## Final Synthesis

A Retail Point of Sale is the store's **sale-execution application**: it turns a store-defined priced catalog into live, in-person, paid transactions. Its defining spine is small — priced catalog → operator-composed sale → tender → completed transaction + receipt — executed live at the point of exchange on a store-operated surface. Everything else that modern products carry (barcode scanning, discounts, split tender, returns/exchanges, customer/loyalty attachment, cash/shift management, permissions, inventory decrement, reporting, offline mode, omnichannel sync, kiosk surfaces) is common mature structure or variant structure, not the definition. The Type's most important boundary is semantic, against Restaurant POS (what a sale *is* while it is alive), and structural, against checkout platforms (who operates, and where) and payment processing (what the POS orchestrates vs what the rails do). The sibling leaves Mobile POS and Omnichannel POS are surface/channel variants of this same core and are flagged for taxonomy review.
