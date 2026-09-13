# Research Notes — Contract-to-order Platform

Research date: 2026-09-07

## Research Goal

Understand what the "Contract-to-order" leaf in §07 (Sales, Customer & Revenue) actually refers to in real products: which software owns the span between an executed commercial agreement (contract / blanket order / sales agreement) and the individual sales orders drawn against it, and what structures define that span.

## Initial Boundary (hypothesis before research)

- Hypothesis: this is the seller-side "agreement → order" bridge. Nearest neighbors: Configure Price Quote / CPQ (upstream, ends at accepted quote), Sales Order Capture (downstream, the individual order record), Contract Lifecycle Management §11 / Business Contract Administration §10 (document/legal-centric contract systems), B2B E-commerce Platform §05.17 (buyer-side channel), Subscription Billing (§08) for the recurring-charges mirror.
- Prior passes set two flags for this pass:
  - CPQ pass: "CPQ embeds a quote-time pricing engine, discount-approval gates, and ends by design at the accepted quote as the commercial commitment; the pricing-management discipline, the cross-functional deal-policy center, and the order-capture/contract-to-order center belong to the unprocessed siblings."
  - Sales Order Capture pass: "contract-to-order-platform = contract-driven order generation, a specialized intake into order capture — cross-check recommended"; boundary note "contract-driven generation of orders (renewals, contracted quantities) is a specialized intake channel into order capture; flag for joint review."
- Taxonomy question to resolve: is this a real Type with its own defining core, or a capability/variant of Sales Order Capture or CPQ?

## Research Questions

1. What object does the system of record hold — the contract, the order, or both? What is the center of gravity?
2. What does a "contract" look like here: legal document, or commercial commitment (products, quantities/amounts, prices, validity)?
3. How do orders get generated from the agreement (release/call-off mechanics)? Can orders also be linked from the order side?
4. How is the commitment tracked — consumed quantities/amounts, remaining commitment, enforcement at limits?
5. What rules gate ordering: validity dates, exhaustion, price fidelity, price precedence?
6. How do amendments, returns, and cancellations flow back into the commitment?
7. Who uses it (roles), and what interfaces do they work in?
8. How do agreement terms interact with normal order-entry pricing (precedence, override)?
9. Is this always a module of a larger suite, or does a standalone product category exist?
10. Does the model survive the historical check (pre-SaaS / paper-era standing agreements)?

## Representative Products

Selected for market representation across customer tiers and product philosophies, and for accessible official operational documentation:

| Product | Pole | Why selected |
|---|---|---|
| Microsoft Dynamics 365 Supply Chain Management — Sales agreements | enterprise ERP | richest formal model: commitment types, pricing precedence, enforcement policies, versioned confirmations |
| Microsoft Dynamics 365 Business Central — Blanket sales orders | mid-market ERP / SMB | order-centric blanket form: pre-scheduled shipment lines, posting constraints, statistics |
| ERPNext (Frappe) — Blanket Orders | open-source ERP | same object serves selling and purchasing; explicit status/amendment discipline |
| OCA sale_blanket_order (Odoo ecosystem) — Sale Blanket Orders | open-source suite, community-module form | minimal viable model: pre-agreement + wizard-generated call-offs + line-level suggestion logic |

Notes on sampling: D365 SCM and Business Central are the same vendor but genuinely different products/segments (large-enterprise vs SMB); they are treated as two realizations of one pole. No CRM-suite (Salesforce-class) or quote-to-cash-suite (Conga/DealHub-class) realization could be documented — see Source-access Limitation. Zuora was evaluated and positioned as a boundary (subscription pattern), not a sample.

## Sources

### Tier 1 — official operational documentation (fetched and read)

- Microsoft Learn — "Sales agreements overview" (Dynamics 365 Supply Chain Management): https://learn.microsoft.com/en-us/dynamics365/supply-chain/sales-marketing/sales-agreements
- Microsoft Learn — "Work with blanket sales orders or purchase orders" (Dynamics 365 Business Central): https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-to-create-blanket-sales-orders
- ERPNext Documentation — "Blanket Order": https://docs.frappe.io/erpnext/blanket-order
- OCA (Odoo Community Association) — sale_blanket_order module README (Odoo 16.0): https://github.com/OCA/sale-workflow/tree/16.0/sale_blanket_order (README fetched via raw.githubusercontent.com)

### Source-access Limitation

- Salesforce Help (help.salesforce.com) is JS-rendered ("CSS Error" on fetch); developer.salesforce.com returned 403; web.archive.org timed out twice → Salesforce realizations could not be documented. No Salesforce-specific claims are made anywhere in this research or the final document.
- SAP Help Portal root returned no navigable content (JS-rendered); SAP SD quantity-contract → release-order flow is therefore NOT cited, despite being a likely canonical enterprise realization. Precise SAP terminology/limits are deliberately absent.
- Conga documentation.conga.com returned 403; DealHub support portal reachable but its Subscription/CLM sections contain no published content ("Coming soon!") → quote-to-cash-suite realizations could not be documented.
- Odoo core documentation (odoo.com) 403; GitHub-hosted Odoo docs tree (17.0/18.0) contains no blanket-order page → core-Odoo realization documented only via the OCA community module.
- Generic web search engines were unreachable from the research environment (Bing region-redirected without results, DuckDuckGo timed out, Mojeek 403, Ecosia redirected) → product discovery relied on Microsoft Learn search API + direct vendor-doc URL patterns. The sample skews ERP-realization-heavy; claims are calibrated accordingly (no claims about CRM-suite realizations beyond "could not be verified").

## Product observations

### Product A — Dynamics 365 Supply Chain Management: Sales agreements (Layer A — directly observed)

Definition observed: "A sales agreement is a contract that commits the customer to buy products in a specific quantity or for a specific amount over time, in exchange for special prices, special discounts, and other special terms, such as payment and delivery terms." Historical naming: "In earlier versions, sales agreements were referred to as blanket sales orders."

Key observations:

- **Agreement as governing record.** Header + lines. Lines express commitments; four commitment types by combining basis × scope: product quantity commitment, product value commitment, product category value commitment, open value commitment. Multiple commitment types can coexist in one agreement.
- **Validity period.** Effective date / expiration date; "A customer's sales order qualifies for the agreement terms if the requested ship date of the order is within the validity period."
- **Pricing precedence.** "The prices and discounts of the sales agreement override the prices and discounts that are stated in any trade agreements that exist." Affected price fields depend on commitment type (unit price/price unit for quantity commitments; discount percent for value commitments).
- **Order generation from the agreement.** "You can create a sales order directly from a sales agreement by using the **Release order** action." Alternatively the agreement can be selected during order entry ("Applying sales agreements during the ordering process"): header terms (payment, delivery, address) copied to the order; line prices/discounts copied for products in the agreement; an order may mix agreement-linked and non-linked lines.
- **Enforcement policies on links.** "Max is enforced" — total quantity/amount of order lines cannot exceed the commitment; "Price and discount is fixed" — if the order-line price is changed, the link breaks and the line no longer contributes to fulfillment; "Minimum release amount / Maximum release amount" — warnings when a release deviates.
- **Fulfillment accounting.** Fulfillment tab on line details: total quantities/amounts of all linked order lines + "the remaining amount or quantity that is required to fulfill the commitment."
- **Governance.** Confirming an agreement stores a version in a history table; changes + re-confirm store further versions; revisions can be previewed/printed and "shared with your customer to obtain approval." An unconfirmed agreement can still be used to create orders (no history kept).
- **Modification constraints.** Order lines linked to an agreement cannot change requested ship date outside the validity window, or price/quantity fields under fixed-price/max-enforced policies, without removing the link (prompted explicitly).
- **Returns loop.** A return order based on the original linked sales order "can find and automatically update the related sales agreement commitment to reflect the change in quantity or amount"; link can be removed/re-established manually; one return order links to one agreement only.
- **Automatic agreement search.** For indirectly created orders (credit notes, intercompany), the system can be configured to auto-search applicable agreements.
- **Financial dimensions** copied from agreement header/lines to release orders.
- Roles observed: "Typically, a sales order processor creates sales orders" (from the Create sales orders task doc surfaced in search).

### Product B — Dynamics 365 Business Central: Blanket sales orders (Layer A — directly observed)

Definition observed: "Blanket sales orders ... represent a framework for a long-term agreement between you and your customer or vendor." "Typically, you use a blanket order when a customer buys a large quantity that you deliver in small shipments over a period of time. Blanket orders often cover only one item with predetermined delivery dates."

Key observations:

- **Availability-neutral commitment.** "The main reason for using a blanket order rather than a sales order is that quantities entered on a blanket order don't affect item availability. You can use them as a worksheet for monitoring, forecasting, and planning."
- **Pre-scheduled shipment lines.** "Each separate shipment can be set up as an order line, which can then be converted into a sales order at the time of shipping." Example: 1,000 units split into four weekly 250-unit lines.
- **Order generation.** "Make Order" action converts selected quantities into a sales order; the blanket order is not deleted; the created sales order contains all blanket lines (unselected ones blank, editable/deletable).
- **Commitment enforcement at posting.** "The sales order line quantity must not exceed the quantity of the associated blanket order line. Otherwise, you can't post the sales order." After a blanket line's total quantity is ordered, no further orders can be created for that line; the blanket quantity can be increased to allow more.
- **Consumption accounting.** Posting shipment/invoice updates "Quantity Shipped" and "Quantity Invoiced" on the blanket order. Statistics page aggregates general/invoicing/shipping/prepayment totals.
- **Traceability.** "The blanket order number and line number are recorded as properties of the sales lines"; manual linking possible via "Blanket Order No." field on sales lines when orders are created outside the blanket order; unposted/posted views enumerate orders, invoices, return orders, credit memos, shipments, return receipts linked to a blanket line.
- **Retention.** "The invoiced blanket sales order remains in the system until you delete it" (manual or batch job).
- **Order date semantics.** Blanket order date left blank; each created sales order gets the actual work date.
- Purchasing mirror documented in the same article (blanket purchase orders; steps the same).

### Product C — ERPNext: Blanket Orders (Layer A — directly observed)

Definition observed: "A Blanket Order in ERPNext records a long-term commitment to buy or sell specified items within an agreed period and at negotiated rates. It does not deliver, receive, bill, or pay for goods by itself. Instead, it becomes the reference for multiple downstream transactions as quantities are released over time."

Key observations:

- **Single object, both directions.** Order Type = Selling (customer) or Purchasing (supplier); same form and machinery.
- **Fields observed.** Customer/Supplier, From Date / To Date, item lines with committed Quantity, Rate, item-specific Terms and Conditions, and an "Ordered Quantity" field = "the quantity already referenced by submitted downstream orders. Use it to monitor the remaining commitment."
- **Order generation.** After submission, Create → Quotation or Sales Order (selling) / Purchase Order (purchasing); "You can create multiple transactions from the same Blanket Order. ERPNext updates the ordered quantity as linked orders are submitted." Reverse linking: "You can also select a Blanket Order from an eligible downstream transaction," with advice to check mapped item, remaining quantity, rate, schedule date, warehouse, taxes, terms before saving.
- **Monitoring.** Blanket Order dashboard opens linked Quotations/Sales Orders/Purchase Orders; "Compare the committed Quantity with Ordered Quantity for each line. The outstanding quantity is the portion that has not yet been released into submitted orders."
- **Status machinery.** Draft (editable) → Submitted (usable for releases) → Cancelled (no new releases). Amendment: "cancel and amend it according to your permissions and audit policy. Review linked orders before changing the source agreement. Do not create a replacement merely to hide an existing transaction history."
- **Closure is not automatic.** "ERPNext may not automatically close an agreement when its period ends or its quantity is fully ordered. Use the dates, ordered quantities, dashboard, and internal review process to identify completed or expired commitments."
- **No inventory effect.** "It records a commercial commitment. Stock is reserved or moved only through the applicable downstream processes and settings." Each downstream order "still needs its own delivery schedule, warehouse, taxes, and approval before it moves through the standard sales or buying cycle."
- **Rate mapping.** "The negotiated rate is mapped from the Blanket Order. Any change should follow your permissions and commercial approval process."
- FAQ confirms multiple sales orders per blanket order until fulfillment or validity end.

### Product D — OCA sale_blanket_order (Odoo 16): Sale Blanket Orders (Layer A — module README; community-maintained, single-product implementation detail)

Definition observed: "A blanket order is a pre-agreement to sell a certain number of quantities of products at a specific price. From a confirmed blanket order, the users can create new sale orders at such price, until the blanket order expires, either due to reaching the validity date or exhausting all the quantities of products."

Key observations:

- Dedicated "Blanket Orders" menu in Sales; form fields: vendor/customer party, salesperson, payment terms, validity date, T&C; lines with product, accorded price, and "Original, Ordered, Invoiced, Received and Remaining quantities."
- Lifecycle: draft → confirmed/open (state "open" required before generating orders).
- "Create Sale Order" wizard asks the quantity per product for the new order; user can view sale orders associated to the blanket order.
- A "Blanket Order line" field on sale-order lines tracks the association; when adding a product to a new order line, a blanket line is suggested based on: closer validity date, and remaining quantity > requested quantity.
- A global "blanket order lines" list view supports assembling orders across blanket orders (README wording mixes purchase-order language in places; only the unambiguous sale-order mechanics are used here).
- Caveat: community module (maturity badge: Beta); represents the Odoo-ecosystem realization, not Odoo core documentation (core docs have no blanket-order page).

## Cross-product Comparison

| Structure | D365 SCM | Business Central | ERPNext | OCA/Odoo | Layer |
|---|---|---|---|---|---|
| Standing agreement object (customer + validity + committed lines) | ✔ (sales agreement) | ✔ (blanket sales order) | ✔ (blanket order, selling) | ✔ (sale blanket order) | A×4 |
| Committed quantity per product line | ✔ | ✔ | ✔ | ✔ | A×4 |
| Committed amount (value) as alternative/added basis | ✔ (product value / category value / open value) | — | — | — | A×1 → variant |
| Negotiated terms/pricing carried on the agreement | ✔ (prices+discounts+payment/delivery terms) | ✔ (line prices; terms copied) | ✔ (negotiated rate, T&C) | ✔ (accorded price, payment terms, T&C) | A×4 |
| Agreement pricing overrides ordinary pricing | ✔ explicit (overrides trade agreements) | (implicit — lines carry prices) | ✔ (rate mapped to orders) | ✔ (orders "at such price") | A×3 (B qualified) |
| Validity window gates ordering | ✔ (requested ship date within window) | ✔ (dates; order date at conversion) | ✔ (from/to dates) | ✔ (validity date expiry) | A×4 |
| Direct release/call-off generation of orders | ✔ (Release order action) | ✔ (Make Order) | ✔ (Create → Quotation/Sales Order) | ✔ (Create Sale Order wizard) | A×4 |
| Reverse linking from order side | ✔ (select agreement during order entry) | ✔ (Blanket Order No. field) | ✔ (select blanket order on transaction) | ✔ (blanket line field + suggestion) | A×4 |
| Consumption accounting on the agreement | ✔ (fulfillment totals + remaining) | ✔ (qty shipped/invoiced; statistics) | ✔ (ordered vs committed; outstanding) | ✔ (ordered/remaining quantities) | A×4 |
| Enforcement at commitment limit | ✔ (max enforced; exceed → unlink prompt) | ✔ (cannot post beyond line; fully-ordered line closes) | ○ (monitoring emphasized; remaining shown) | ✔ (expires on exhaustion) | A×3, C×1 → graded |
| Price-fidelity rule (deviation breaks the commitment link) | ✔ explicit | (exceed-blocks-posting only) | (change requires approval process) | (orders at agreed price) | A×1 explicit → common-not-core |
| Versioned confirmation / amendment governance | ✔ (confirm → version history) | — (no versioning documented; retention until deleted) | ✔ (submit/cancel-amend with audit discipline) | ○ (draft→open confirm step) | A×3 forms differ |
| Returns/credits adjust the commitment | ✔ (auto-update via linked return) | ✔ (return orders/credit memos linked to blanket lines) | ○ (cancelled orders not counted — FAQ) | — | A×2, C qualified |
| Availability/planning neutrality | (not documented) | ✔ explicit ("don't affect item availability") | ✔ explicit ("does not reserve stock") | — | A×2 |
| Pre-scheduled shipment lines on the agreement | (not documented as scheduled lines) | ✔ (per-shipment lines with delivery dates) | — (schedule set on each downstream order) | — | A×1 → variant |
| Auto-suggestion/auto-search of applicable agreement | ✔ (auto-search for indirect creation) | (manual link field) | (manual selection advised) | ✔ (line suggestion logic) | A×2 |
| Purchasing mirror on the same machinery | (purchase agreements exist — not fetched) | ✔ (same article) | ✔ (same object, Order Type) | — | A×2 (+C referenced) |
| Retention of fulfilled agreements as record | (history table for versions) | ✔ (invoiced blankets remain until deleted) | ✔ (do not replace to hide history) | — | A×3 |

Legend: ✔ directly observed; ○ qualified/partially observed; — not documented in the fetched source.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

Two structures. Remove either and the application is a different Type:

1. **The standing commercial agreement as a managed record** — a persistent, identified agreement with a customer, a validity window, committed supply (products with committed quantities — and in some realizations amounts/categories), and negotiated commercial terms (prices, payment/delivery terms, T&C) held as the governing object for future selling. Remove it → there is no agreement, just orders (Sales Order Capture); or a document without commercial force (contract administration).
2. **Commitment-constrained order generation with consumption accounting** — individual sales orders are generated from (or explicitly linked to) the agreement, take their commercial terms from it, count against its committed quantities/amounts, and the agreement surfaces the remaining commitment (stopping or warning at the limit; expiring at the validity end). Remove the generation/consumption → the agreement is a document of record, not an ordering engine (CLM territory); remove the constraint/consumption and any order link is decorative.

Historical/market-sample check (§24): the "framework agreement + call-offs" pattern predates SaaS — pre-software supply agreements were worked as open-order books with hand-tracked fill; the ERP term family (blanket orders, sales agreements, quantity contracts, release orders) is decades old. The L0 above describes the invariant, not the current packaging: nothing in it requires cloud, CRM integration, CPQ, or e-signature. D365 explicitly renamed the same object over time ("sales agreements were earlier referred to as blanket sales orders"), showing label drift over a stable structure.

### L1 — Common Mature Structure (cross-product commonality, Layer A×3–4)

- Reverse linking: orders can also be linked from the order-entry side (agreement selector / reference field / auto-suggestion), not only released from the agreement.
- Consumption dashboard: agreement-level or line-level view comparing committed vs released (ordered/shipped/invoiced) quantities with outstanding/remaining values.
- Traceability: links retained between agreement, orders, shipments/invoices, returns/credits (BC enumerated views; D365 return loop; ERPNext dashboard links).
- Terms propagation: header terms (payment, delivery, address) and line prices copied into the generated orders.
- Pricing precedence: agreement terms beat ordinary order-entry pricing (explicitly documented in D365 and OCA/ERPNext as "orders at such price / rate mapped").
- Mixed orders allowed in principle (D365 explicitly; reverse-linking in others implies partial linkage).
- Expiry/closure semantics: validity end and/or exhaustion end the agreement's usefulness (D365 policy-based; OCA explicit; BC line-level closure; ERPNext warns it may not auto-close — so "explicit closure machinery" is common but not universal in behavior).

### L2 — Variant / Optional Structure

- Commitment basis: quantity-only (BC, ERPNext, OCA) vs four-type commitment matrix incl. value and category commitments (D365).
- Release mode: demand-driven call-offs vs pre-scheduled shipment lines (BC's per-shipment lines with dates).
- Governance depth: versioned confirmations with customer-approvable revisions (D365) vs submit/cancel/amend states with audit discipline (ERPNext) vs lightweight draft→open (OCA) vs none documented (BC).
- Enforcement posture: hard block at posting (BC), policy-driven unlink-on-deviation (D365), monitoring-first (ERPNext: remaining quantity surfaced, approval process on rate changes).
- Availability posture: agreement as availability-neutral planning input (BC, ERPNext explicit).
- Direction: sales-only vs one object serving selling and purchasing (ERPNext single object; BC symmetric blanket orders).
- Retention: fulfilled agreements retained as record until deleted (BC) / version history (D365) / amend-not-replace discipline (ERPNext).
- Automatic agreement resolution: auto-search for indirect orders (D365), line-level suggestion (OCA) vs manual selection (BC, ERPNext).
- Packaging: ERP-suite module (all four sampled). CRM-suite and quote-to-cash-suite realizations suspected but unverifiable in this pass (see Source-access Limitation).

### L3 — Vendor-specific (stays in Research Notes)

- D365: four named commitment types; "Max is enforced" / "Price and discount is fixed" / min-max release amount policy checkboxes; financial-dimension propagation; intercompany/credit-note auto-search; requested-ship-date unlink prompt; Fulfillment tab on Line details FastTab.
- BC: page/form numbers; "Delete Invoiced Blanket Sales Orders" batch job; Blanket Order Statistics page FastTabs; interaction-log recording on print (marketing setup).
- ERPNext: Draft/Submitted/Cancelled state names; dashboard; pencil-icon row editor; "Do not create a replacement merely to hide an existing transaction history" phrasing.
- OCA: wizard fields; suggestion heuristics (closer validity, remaining > requested); module maturity (Beta); README's PO/PO-line wording inconsistencies (documentation quality artifact — not used for claims).

## Rejected Findings

- "Contract-to-order = CPQ." Rejected: the CPQ pass documents CPQ ending at the accepted quote; none of the sampled products' agreements are quotes. A quote→order conversion exists in suites, but the standing-agreement machinery (validity window, consumption accounting, call-off enforcement) is a different structure.
- "Contract-to-order = CLM." Rejected as identity: CLM samples (Ironclad/Icertis/LinkSquares per the CLM pass) center document authoring, negotiation, repository, obligations — no call-off generation or commitment consumption accounting appears in that model. Overlap exists at "contract record," but the operated object differs (document vs commercial force).
- "Agreements must reserve inventory or drive planning." Rejected as definitional: BC and ERPNext explicitly state the opposite (no availability effect / no stock reservation). Planning value exists but as a worksheet/forecast input, not a defining behavior.
- "Value commitments are core." Rejected: only D365 documents amount-based commitments; quantity commitments are universal. Value basis → variant.
- "Auto-close on expiry/exhaustion is core." Rejected: ERPNext explicitly may not auto-close; OCA closes on exhaustion/validity; BC closes per line. Behavior varies → common expectation, not invariant.
- Promoting the OCA module's UI mechanics (wizard fields, suggestion heuristics) to canonical: rejected — single-product, community-module implementation detail.

## Boundary Findings

- **vs Sales Order Capture (§07, processed)** — RESOLVES the sibling flag from that pass. Distinct centers of gravity: Sales Order Capture's unit of record is the individual order (create/confirm/amend, track commitment state); this Type's unit of record is the standing agreement that governs many orders. The two interlock: in sampled realizations, the generated order then flows through ordinary order processing (BC posts it; D365 order lines contribute to fulfillment). Seam adopted: contract-to-order ends when the linked, terms-applied order record exists; order capture owns that record's subsequent life. An order-capture application without standing agreements remains order capture; adding standing agreements + call-off machinery creates this Type. Both leaves kept.
- **vs Configure Price Quote / CPQ (§07, processed)** — RESOLVES the CPQ pass's sibling flag from this side. CPQ's commitment is quote-time and one-shot (accepted quote = commercial commitment); this Type's commitment is a standing supply obligation consumed over time by multiple orders. Upstream one-way handoff: an accepted quote/contract may become the agreement of record here, but the quote machinery (configuration, pricing engine, approval gates) is not this Type's machinery.
- **vs Contract Lifecycle Management (§11) / Business Contract Administration (§10, processed)** — CLM/BCA center the contract as document/legal record (authoring, negotiation, execution, repository, obligations, renewals). This Type centers the contract as commercial engine: its terms are applied to and consumed by transaction flow. CLM typically does not generate sales orders; this Type does not manage clause libraries or negotiation workflow. Overlap surface: both hold a contract record with dates/parties/terms.
- **vs Sales Document Automation (§07, processed)** — that pass already states the seam: converting the signed document into an order is the downstream neighbor's job. This Type is that neighbor when the commercial form is a standing agreement.
- **vs B2B E-commerce Platform (§05.17, unprocessed)** — buyer-side self-service channel vs seller-side commitment machinery; a storefront may allow buyers to call off against contract pricing (channel form), but commitment accounting/release mechanics belong here. To be cross-checked when that leaf is processed.
- **vs Order Management System / OMS + Distributed Order Management + Order Orchestration (§05.07, unprocessed)** — per the sales-order-capture pass's adopted seam, OMS routes/splits/sources/fulfills orders after the record exists; this Type operates strictly upstream (agreement → order creation). Cross-check recommended when OMS leaves are processed.
- **vs Subscription Billing Platform / Subscription Commerce (§05.16, unprocessed)** — subscription pattern inverts the direction: a recurring schedule of charges/fulfillments IS the contract's execution (system-generated, time-driven); here, call-offs are demand-driven human decisions against a fixed commitment. The subscription pole was not sampled (Zuora considered, positioned as boundary instead); keep qualitative.
- **vs Purchase Order Management / Procure-to-pay (§10)** — the same machinery pattern exists buyer-side (ERPNext single object both directions; BC symmetric blanket purchase orders). The directory places the sell-side leaf here; the buy-side machinery is noted as a mirror, not claimed as part of this leaf's core users.
- **Capability-vs-Type question** — in every sampled realization, this machinery ships inside an ERP/sales suite rather than as a standalone product, and no standalone "contract-to-order" product category surfaced in accessible sources. Judgment: the object set (agreement of record + release orders + consumption accounting) is distinct enough from siblings to stand as a Type, with the packaging reality recorded as a variant axis ("always a module/pole of a broader suite" in the accessible sample). Flagged for directory-level attention in STATUS.md.

## Uncertainties

1. CRM-suite (Salesforce-class) realizations could not be documented (help pages JS-blocked, dev docs 403, archive unreachable). If those realizations differ structurally (e.g., quote→order without standing agreements), the market picture would widen — the L0 given here would still hold (such flows would fall under Sales Order Capture, not this Type).
2. SAP's quantity-contract/scheduling-agreement realization is known to exist as a pattern family but was not verifiable from reachable sources — deliberately uncited; terminology avoided in the final document.
3. Quote-to-cash suites (Conga, DealHub): unreachable or unpublished docs; their "contract → order/billing" bridges are unverified.
4. Whether any standalone product markets itself primarily as a "contract-to-order platform" — unverified; the accessible sample says the machinery is suite-embedded.
5. Subscription/consumption agreements (committed spend → draw-down billing) as a variant pole: plausible from D365's value commitments, but the recurring-execution end was not sampled.
6. Small-SMB pole (e.g., lightweight CRMs/invoicing tools with "recurring profiles" or "standing orders"): not sampled; whether simple recurring-order profiles constitute a minimal realization is unresolved (recurring invoicing without commitment accounting would sit closer to billing/Subscription Billing).

## Final Synthesis

The leaf names a real, structurally distinct span of the sell side: **the system of record that holds the customer's standing commercial agreement and turns it into individual sales orders over time.** Its world is built from two load-bearing structures: the standing agreement (customer, validity window, committed products/quantities — occasionally amounts — and governing terms) and commitment-constrained order generation with consumption accounting (release or reverse-linked orders take their terms from the agreement and count against the commitment, which the system tracks to remaining/exhausted/expired). Around that core, mature products add reverse linking, consumption dashboards, traceability to shipments/invoices/returns, pricing precedence, and governance (versions or states). Realizations label the agreement "blanket sales order" (order-flavored) or "sales agreement / contract" (agreement-flavored) — label drift over one structure. The machinery always appeared as a suite module in the sampled products; boundaries with CPQ (upstream, one-shot commitment), Sales Order Capture (downstream, individual order record), CLM/BCA (document-centric contract record), and subscription billing (time-driven inverted pattern) are clear and held.
