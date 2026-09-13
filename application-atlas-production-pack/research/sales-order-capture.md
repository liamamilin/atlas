# Research Notes — Sales Order Capture

Research date: 2026-09-07

## Research Goal

Explain what a Sales Order Capture application actually is and how it works: what objects exist inside it, how a customer's order is recorded and confirmed, what checks and rules apply at capture, how the order drives fulfillment and billing, and where the Type ends relative to CPQ, Purchase Order Management, Order Management System, Checkout, Invoicing, and B2B commerce.

## Initial Boundary

- Working hypothesis: Sales Order Capture is the seller-side recording of a customer's committed purchase — the seller (or the seller's systems) creates a persistent order record stating what the customer will buy, at what prices, under what terms, and that record then drives fulfillment and billing.
- The leaf sits in §07 (Sales, Customer & Revenue) between Configure Price Quote / CPQ and Contract-to-order Platform. The CPQ pass (2026-09-07) recorded: "CPQ ends by design at acceptance/commitment; order capture consumes the quote" — joint review recommended when this leaf is processed.
- The Purchase Order Management pass (2026-09-06) recorded the mirror: "a PO received by a supplier becomes that supplier's sales order. Different users, different center (customer orders vs supplier commitments)."
- Nearest neighbors: CPQ (upstream commitment), Contract-to-order Platform (§07 sibling, unprocessed), Order Management System / OMS §05.07 (fulfillment orchestration after capture, unprocessed), Checkout Platform §05.06 (buyer-facing completion that creates the order), B2B E-commerce Platform §05.17 (self-service channel), Invoicing Application §08 (downstream billing document), Purchase Order Management §10 (buyer-side mirror), Retail POS §05.10 (immediate paid sale), Proposal Management §07 (offer document, ends at decision).
- Known unknowns at start: how universal the quote→order conversion is; whether credit/stock checks at capture are definitional or common; how orders close (auto vs manual); whether the order is an accounting document or a pre-accounting commitment; how self-service/EDI intake changes the model.

## Research Questions

1. What is a sales order, and how does it differ from a quote, an invoice, and a purchase order?
2. What objects compose the order (header, lines, customer, terms, references)?
3. What is the order lifecycle (draft → confirmed → partially fulfilled → completed / closed / cancelled / held)?
4. How do orders originate: manual entry, quote conversion, self-service, EDI, API, POS/cash sale, recurring?
5. What checks happen at capture: price lists, credit limits, stock availability, approvals?
6. How does the order drive downstream processes (reservation, picking, delivery, invoicing, payment)?
7. How are orders amended, partially fulfilled, partially billed, closed, or cancelled?
8. What interfaces exist (order entry form, order list, customer order history, approval queue)?
9. Who uses the application and with what permissions?
10. Where is the boundary against OMS, checkout, invoicing, POS, and CPQ?

## Representative Products

| Product | Pole | Tier used |
|---|---|---|
| Microsoft Dynamics 365 Business Central | mid-market ERP, document/posting model | Tier-1 (Microsoft Learn, full article) |
| Zoho Books | SMB accounting suite, ledger-centric | Tier-1 (KB, 8 articles) |
| Microsoft Dynamics 365 Sales | CRM-side sales transaction record | Tier-1 (Microsoft Learn, full article) |
| ERPNext | open-source ERP, explicit order-to-cash spine | Tier-1 (official docs, full article) |
| NetSuite | cloud ERP, order-management-centric | Tier-2 (official guide titles; PDFs login-gated) |
| OroCommerce | B2B commerce order capture | dropped — transport errors ×2 (consistent with the 2026-09-06 b2b pass) |

Odoo was attempted as the open-source pole first (documentation 403 ×2) and replaced by ERPNext. SAP Help Portal returned a JS-only landing page (1 attempt) and was abandoned; the enterprise-ERP pole rests on Business Central + NetSuite titles.

## Sources

- Microsoft Learn — "Create a customer sales order and sell products" (Business Central): https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-sell-products — fetched 2026-09-07
- Microsoft Learn — "Create or edit sales orders" (Dynamics 365 Sales): https://learn.microsoft.com/en-us/dynamics365/sales/create-edit-order-sales — fetched 2026-09-07
- Zoho Books KB — Sales Order topic index + articles: create-sales-order, sales-order-inventory, include-sales-orders-amount-in-customers-credit-limit, close-sales-orders, void-cancel-in-so, link-sales-order-to-purchase-order, invoice-sales-orders-partially — https://www.zoho.com/books/kb/sales-order/ — fetched 2026-09-07
- ERPNext official documentation — "Sales Order": https://docs.frappe.io/erpnext/user/manual/en/sales-order — fetched 2026-09-07
- NetSuite Help Center — User Guides index (Order Management Guides section): https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/preface_3710621755.html — fetched 2026-09-07; "Sales Orders and Cash Sales Guide" PDF login-gated (recorded as source limitation)
- Cross-references: research/configure-price-quote-cpq.md, research/purchase-order-management.md, research/checkout-platform.md (STATUS.md boundary notes)

## Product A — Microsoft Dynamics 365 Business Central (mid-market ERP)

### Key observations (Layer A — directly observed)

- Definition: "Describes how to create a sales order to record your agreement with a customer to sell or trade products under specific terms."
- Order vs invoice: "If your sales process requires you to only ship part of an order… you must process that sale by making a sales order." Also required for drop shipments. "In all other respects, sales orders work the same way as sales invoices." — the order is the multi-step instrument; the invoice is the single-step one.
- Posting model: "When you post a sales order, you create a shipment and an invoice. These documents can be done at the same time or independently." Partial shipment/partial invoice via per-line "Qty. to Ship" / "Qty. to Invoice". "You cannot create an invoice from the Sales Orders page for something that has not shipped" (ship must be recorded first, or ship+invoice together). "When the sales order is fully posted, Business Central removes it from the list of sales orders."
- Order lines: Type (item / service / resource / charge / comment), No., Quantity, Unit Price, Line Discount %, invoice discount; "The price and line amounts are shown with or without sales tax depending on… the customer card." Special prices/line discounts auto-apply from customer/item price agreements.
- Customer anchoring: entering Customer Name fills header fields from the customer card. Cash customers supported ("create directly paid orders for unregistered customers by first setting up a 'cash customer' card").
- Buyer-side reference: "External document number… record the number that the customer assigned to the order, invoice, or credit memo" — i.e., the customer's PO number is a first-class field; can be made mandatory.
- Recurring sales lines ("Get Recurring Sales Lines", e.g., monthly replenishment); copy document (header/lines, recalculate prices for a different customer).
- Shipping advice: if set to "Complete", partial shipments cannot be posted.
- Quote adjacency: Sales Quotes page exists; "Make Invoice" action on quotes; order is the document that carries fulfillment.
- Payment: immediate-payment methods (cash/PayPal) recorded when posting; payment method code on the order.

## Product B — Zoho Books (SMB accounting suite)

### Key observations (Layer A)

- Definition: "A sales order is created when the quote you sent to your customer is accepted. A sales order is a financial document that is sent as a confirmation for the sale. The sales order predominantly contains the products to be delivered, delivery date and other details relating to the sale."
- Order vs inventory: "Raising a sales order will not affect the inventory. Inventory will be affected only if an invoice is sent. However, creating a sales order will affect Committed Stock (the stock of an item that is committed to a sales order but not invoiced)." — the order commits, the invoice executes.
- Credit control at capture: preference to "include sales orders' amount in limiting the credit given to customers"; "whenever you create or edit sales orders for a customer, and the total amount exceeds their credit limit, a warning will be displayed when you attempt to save the sales order, or you may not be able to save the sales order, depending on the credit limit preference."
- Lifecycle: "It is not possible to close a sales order manually. The sales order will be closed automatically if you convert or link it to an invoice." With the inventory add-on, closing follows general preferences. Status "Partially Invoiced" after partial conversion.
- Cancellation: "Cancel Items" cancels selected lines; "Void" voids the whole order.
- Downstream conversion: Convert to Invoice (partial by removing lines or adjusting quantities); multiple sales orders can be associated with one invoice (article title); instant invoice from a sales order; SO→PO conversion recorded in Comments & History ("Purchase order raised for Sales order" / "Purchase order created from Sales order") — the drop-ship-style bridge to the buyer-side mirror.
- Editing: closed sales orders can be protected from editing by role restriction.

## Product C — Microsoft Dynamics 365 Sales (CRM-side)

### Key observations (Layer A)

- Definition: "Use orders to track details of the products or services that your customers want to place an order for."
- Origin: "Create an order when the customer is ready to buy… an order can originate from a customer's acceptance of a quote, or you can place an order without an accepted quote." Create Order from an active quote copies all products, price list, and currency; "Date Won" recorded.
- Pricing structure: Price List and Currency required to add products (admin can make price list optional); "Prices Locked" field controls whether prices can change; behavior differs when "sales order processing integration" (ERP handoff) is enabled — the CRM order is explicitly designed to hand off to ERP order processing.
- Lines: products added manually or pulled from the opportunity ("Get Products"); bundles/product families for upsell; tax entered manually per product line (CRM does not auto-calculate line tax).
- Lifecycle: "You close an order by either fulfilling the order or canceling the order. Products or services that are shipped are fulfilled." "You can't update or change an order after it's closed, or if it's partially or completely fulfilled." Fulfillment is per order (not bulk).
- Next step: invoice creation from the order; sales process framed as "nurturing sales from lead to order".

## Product D — ERPNext (open-source ERP)

### Key observations (Layer A)

- Definition: "A Sales Order in ERPNext records a customer's confirmed request, including Items, prices, quantities, delivery dates, shipping details, and terms." Motivation: if the agreement "remains in an email or spreadsheet, the warehouse may not know what to prepare, finance may invoice the wrong quantity, and the sales team cannot easily track what remains to be delivered."
- Spine: "The standard order-to-cash flow is Quotation → Sales Order → Delivery Note → Sales Invoice → Payment Entry." SO can also be created directly from a submitted quotation (carries customer, items, rates, taxes, terms), without a quotation, from integrations, or from the shopping cart (Order Type "Shopping Cart").
- Commitment semantics: "Saving and submitting are different actions. You can edit a draft freely. Submission confirms the order and enables downstream transactions." "Does submitting a Sales Order change stock or create accounting entries? The Sales Order itself records a commitment. Normal submission does not deliver stock or recognize an invoice. Stock and accounting effects occur through the linked fulfillment and billing documents."
- Header/line fields: Company, Customer (fetches address/contact/territory/price list/payment terms), Order Type (Sales / Maintenance / Shopping Cart), Date, Delivery Date (order-level default + per-row split delivery schedules), "Customer's Purchase Order" (buyer's PO reference + date, "useful for matching documents"), Price List, Exchange Rate, Ignore Pricing Rule, barcode scan (re-scan increments quantity), source warehouse, per-row warehouse, Reserve Stock (stock reservation without stock-ledger movement), billing/shipping addresses, contact, tax templates + manual rows, Shipping Rule (freight), Incoterms, order-level additional discount (on net or grand total), Payment Terms Template → Payment Schedule, Terms and Conditions, Project link, Inter Company Order Reference.
- Availability signal: stock-availability dot on item rows (green in stock / red out of stock).
- Downstream generation from a submitted order: Pick List, Delivery Note, Sales Invoice, Payment Request/Payment, Material Request/Purchase Order (procurement), Work Order/Production Plan (manufacturing), Project.
- Partial processing: "An order can be partially delivered or billed across multiple documents. ERPNext updates its delivery and billing percentages." Per-row delivery dates.
- Amendment discipline: "Update Items" after submission, restricted by quantities already picked/delivered/billed/assigned to production; Hold/Resume; Close ("when you intentionally will not fulfill its remaining quantity") vs Cancel ("when the entire transaction should be reversed"); Amend a cancelled order → new draft linked to the cancelled order.
- Statuses: Draft, To Deliver and Bill, To Deliver, To Bill, Completed, On Hold, Closed, Cancelled; separate Delivery Status / Billing Status / Advance Payment Status filters. Order list shows delivery date, grand total, % delivered, % billed.
- Recurring: Blanket Order and Auto Repeat for recurring requirements.
- Permissions: "You need create permission and submit permission to confirm an order."

## Product E — NetSuite (cloud ERP) — Tier-2 evidence only

### Key observations (Layer B — official guide titles, content login-gated)

- The official User Guides index lists, under "Order Management Guides": **Sales Orders and Cash Sales Guide**, Order Fulfillment Guide, Billing and Invoices Guide, Auto Close Back Orders, Order Guides, Grid Order Management, Recurring Billing, Returns and Refunds, Payments.
- Title evidence: sales order and cash sale are sibling transaction types (order with immediate payment vs on-terms order); back orders are a managed concept with auto-close; "Order Guides" (customer-specific ordering guides) and "Grid Order Management" (matrix/grid order entry) exist as first-class features; fulfillment is documented separately from order capture.
- No precise operational details asserted from NetSuite (login-gated). Source limitation recorded.

## Cross-product Comparison

| Dimension | Business Central | Zoho Books | D365 Sales | ERPNext | NetSuite (titles) |
|---|---|---|---|---|---|
| Order definition | agreement with customer to sell under specific terms | confirmation document for the accepted quote | record of products/services customer wants to order | customer's confirmed request (items, prices, quantities, dates, terms) | "Sales Orders" core transaction |
| Origin channels | manual entry; copy; recurring lines; quote adjacency | quote acceptance (stated); manual | quote acceptance or direct; from opportunity | quotation conversion, direct, integrations, shopping cart | manual; order guides; (EDI not verified) |
| Line structure | typed lines (item/service/charge/comment), qty, price, discounts | item lines with qty/rate | product lines w/ price list, manual tax | item rows w/ qty, rate, warehouse, per-row delivery date | (not observed) |
| Pricing at capture | auto from customer/item price agreements | item rates | price list required (configurable); Prices Locked | price list + pricing rules; fetched rate editable by permission | (not observed) |
| Stock at capture | shipping advice; partial ship fields | Committed Stock (no inventory effect) | not applicable (no inventory) | availability dot; Reserve Stock; source warehouse | back orders (title) |
| Credit check | (credit mgmt exists; not in fetched article) | SO amounts count toward credit limit; warn or block | (not observed) | (not observed) | (not observed) |
| Fulfillment linkage | post = shipment + invoice (same or independent); removed when fully posted | closes when invoiced/linked | close = fulfilled or cancelled; frozen after partial fulfillment | Delivery Note / Pick List; % delivered, % billed | Order Fulfillment separate guide |
| Billing linkage | invoice from order; ship-before-invoice rule | convert to invoice (partial; multiple SOs → one invoice) | invoice as next step | Sales Invoice; skip-delivery for services | Billing and Invoices guide |
| Amendment | copy document; version/occurrence fields | edit restrictions on closed orders | cannot change after close/partial fulfillment | Update Items restricted by picked/delivered/billed; amend cancelled | (not observed) |
| Close semantics | fully posted → removed from list | auto-close on invoicing (manual close not possible in base) | fulfilled or cancelled | Close (won't fulfill remainder) vs Cancel (reverse) vs Hold | Auto Close Back Orders (title) |
| Buyer's PO reference | External Document No. (can be mandatory) | (not observed) | (not observed) | Customer's Purchase Order field | (not observed) |
| Cash/immediate payment | cash customer card; payment method on order | (payments module adjacent) | (not observed) | (payment entry downstream) | Cash Sale sibling type (title) |
| Order confirmation output | post and send as PDF/email | "sent as a confirmation for the sale" | (not observed) | print format | (not observed) |

### Cross-product commonalities (Layer B)

1. Every product centers on a persistent, identified, customer-anchored order record.
2. Every product structures the order as itemized lines (product/service + quantity + price), priced from seller-side pricing structures (price lists / price agreements / pricing rules).
3. Every product treats the order as a commitment that downstream processes execute and track against: fulfillment (shipment/delivery) and billing (invoice) are recorded against the order; the order carries remaining-quantity state (partial fulfillment/billing is universal).
4. Every product distinguishes the order from the invoice: the order records the commitment; the invoice is the billing/accounting event (Zoho: inventory affected only at invoice; ERPNext: SO creates no stock/accounting movement; BC: order vs invoice as alternate instruments).
5. Quote→order conversion is the standard upstream (Zoho states it as the definition; D365 and ERPNext implement it; BC has quotes with order adjacency).
6. Lifecycle discipline is universal: draft/confirmation distinction, restriction of changes once fulfillment has begun, close vs cancel semantics, hold in two products.
7. The buyer's PO reference appears as a first-class field in two products (BC External Document No., ERPNext Customer's Purchase Order) — the seller-side mirror of Purchase Order Management.
8. Order confirmation output to the customer (print/email/PDF) appears in three products.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (three structures)

1. **The sales order as a persistent, customer-anchored seller-side record of a committed purchase.** A customer has committed to buy; the seller holds that commitment as an identified record (not an email, not a conversation). Remove → demand lives only in quotes/conversations; no order record exists.
2. **Itemized priced lines drawn from the seller's offering.** The order decomposes into lines naming the seller's products/services with quantities and prices under the seller's pricing structure (price lists, agreed prices, discounts). Remove → a memo or ledger note, not an order.
3. **The order as an open commitment that fulfillment and billing track against.** The order remains open until fulfilled and billed (or closed/cancelled); downstream documents/entries are recorded against it, and remaining quantities are tracked. Remove → a quote or wish list; the order-capture discipline is precisely that the record drives and measures execution.

Historical check (§24): the paper order desk (order form: customer, itemized lines, prices, terms; tracked to shipment and invoice), EDI-era order entry (buyer's 850 PO auto-creating the seller's order), and AS/400-era order processing all satisfy these three structures. The definition does not depend on any modern channel, cloud deployment, or specific status vocabulary.

### L1 — Common Mature Structure

- Quote/estimate → order conversion (carrying lines, prices, terms)
- Order lifecycle/status management (draft → confirmed → partially fulfilled → completed; hold; close vs cancel; amend with restrictions)
- Partial fulfillment and partial billing with remaining-quantity/backorder tracking
- Customer master linkage (addresses, contacts, payment terms, credit)
- Price-list/pricing-rule application at entry (auto-pricing, line and order discounts)
- Stock availability signals and stock commitment/reservation at capture
- Order confirmation document output (print/email/PDF)
- Credit-limit checking at capture (warn or block)
- Buyer's PO reference (external document number)
- Order list/search with status and progress filters; per-customer order history
- Downstream document generation (pick list, delivery/shipment, invoice, payment)
- Copy/duplicate order; recurring/standing orders

### L2 — Variant / Optional Structure

- Intake channel: seller-staff entry, quote conversion, buyer self-service (web store), EDI, API, field-rep order writing, POS/cash sale
- Cash sale / immediate-payment orders vs on-terms orders (gradient toward POS)
- Drop shipment (order fulfilled directly by the seller's vendor)
- Blanket orders / auto-repeat / subscription-style recurring orders
- Order types by fulfillment mode (goods vs services vs maintenance; shopping-cart orders)
- B2B terms machinery at capture (customer-specific price lists, payment terms, credit, order guides)
- Regional tax treatment and e-invoicing adjacency at capture
- Approval workflow at capture
- Multi-currency, multi-company/inter-company orders
- Packaging: ERP module (dominant), accounting-suite feature, CRM transaction, commerce-embedded

### L3 — Vendor-specific (kept out of the final document)

- Business Central: Shipping Advice "Complete", Qty. to Ship/Qty. to Invoice fields, catalog (nonstock) items, recurring sales lines, cash customer card, Doc. Occurrence/Version fields
- Zoho Books: Committed Stock report, Instant Invoice, Comments & History audit of SO→PO conversion, base-edition auto-close-only behavior
- D365 Sales: Prices Locked, Order Close entity, Get Products from opportunity, sales order processing integration toggle
- ERPNext: Reserve Stock, Skip Delivery Note, Amend-to-new-draft, per-row split delivery schedules, stock-availability dots, Ignore Pricing Rule
- NetSuite: Grid Order Management, Order Guides, Auto Close Back Orders, Cash Sale transaction type (title-level evidence only)

## Vendor-specific Findings

See L3 above. None of these were promoted to the canonical model.

## Boundary Findings

- **vs Configure Price Quote / CPQ (§07, processed)**: CPQ ends by design at the accepted quote — the commercial commitment; order capture consumes that commitment and creates the executable order record. Consistent with the CPQ pass's recorded seam. The gradient case: ERP-embedded CPQ (e.g., NetSuite CPQ) writes orders directly inside the same suite — the seam is functional, not packaging.
- **vs Purchase Order Management (§10, processed)**: exact mirror. The buyer's PO is the seller's order input; two sampled products carry the buyer's PO number as a first-class order field. Different users, different center (supplier commitments vs customer commitments).
- **vs Order Management System / OMS (§05.07, unprocessed)**: order capture records the commitment at the point of sale; OMS orchestrates fulfillment across channels/locations/segments after capture. ERP "sales order management" modules span both, so the seam needs joint review when OMS is processed. Working seam: capture = create/confirm/amend the order record; OMS = route/split/source/fulfill across a network.
- **vs Checkout Platform (§05.06, processed)**: checkout is the buyer-facing completion stage that produces the transaction record and hands it back to seller systems; order capture is the seller-side record-keeping that receives it. Self-service order placement is the overlap zone; the discriminator is which side operates the surface and what the record is for.
- **vs B2B E-commerce Platform (§05.17, processed)**: the commerce channel through which buyers self-capture orders; the resulting order lands in the seller's order-capture world. Channel vs record.
- **vs Invoicing Application (§08, unprocessed)**: the invoice is the billing/accounting document; the sales order precedes it and is not itself an accounting event (directly observed in Zoho and ERPNext). Some sales skip the order entirely (direct invoicing in BC; Zoho's invoice-first flow) — the order is optional machinery for multi-step fulfillment.
- **vs Retail POS (§05.10, processed)**: POS = immediate paid sale completed live; sales order = commitment with a fulfillment lifecycle. The gradient case is the cash sale / cash customer (order with immediate payment, no lifecycle) — acknowledged as a gradient, not resolved into a Type change.
- **vs Contract-to-order Platform (§07, unprocessed)**: contract-driven generation of orders (renewals, contracted quantities) is a specialized intake channel into order capture; flag for joint review.
- **Packaging reality**: standalone "sales order capture" products are rare; the Type is realized overwhelmingly as ERP/accounting/CRM/commerce modules. This is a packaging observation, not a taxonomy problem — the center (order record + commitment lifecycle) is stable across all packaging.

## Uncertainties

- NetSuite operational detail is unverified (login-gated); NetSuite findings rest on official guide titles only.
- Credit checking at capture is directly observed in one product (Zoho); BC/ERPNext have credit machinery but it was not in the fetched pages — written as "common", not definitional.
- EDI intake is industry-standard knowledge but was not directly observed in the fetched sample; written as a variant channel without product-specific claims.
- Approval workflow at capture was not directly observed in the sample (D365 Sales has quote approval, not order approval, in the fetched article); written as optional.
- Field-rep order-writing apps (wholesale) were not researched; the channel is recorded as a variant from market knowledge, without product claims.
- The exact status vocabularies differ per product; canonical states are written conceptually.

## Final Synthesis

Sales Order Capture is the seller-side discipline of turning a customer's commitment to buy into a persistent, executable order record. Its defining core is exactly three structures: the customer-anchored order record; itemized priced lines from the seller's offering; and the open-commitment lifecycle that fulfillment and billing track against. Everything else — quote conversion, credit and stock checks, partial fulfillment, confirmation documents, self-service/EDI intake, recurring orders — is common mature structure or variant machinery layered on that spine. The Type is the seller-side mirror of Purchase Order Management, the downstream consumer of CPQ's accepted quote, and the upstream feeder of fulfillment (OMS) and billing (invoicing).
