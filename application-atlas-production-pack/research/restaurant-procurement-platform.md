# Research Notes — Restaurant Procurement Platform

Leaf: Restaurant Procurement Platform (DIRECTORY §26 Travel, Hospitality, Food Service & Events; slug restaurant-procurement-platform)
Research date: 2026-09-09
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "Restaurant Procurement Platform" applications actually are as a Type: their defining core structure, standard capabilities, variants, and boundaries against neighboring Types. Four prior-pass obligations shape this pass:

1. **restaurant-inventory-management** (§26, processed 2026-09-09) held the seam: "procurement's center is the order (POs, suppliers, ordering workflows, receiving as order fulfillment); inventory's center is the stock record (receiving as stock-in, par levels generating *suggestions*)." This pass must hold that seam from the procurement side.
2. **restaurant-food-cost-management** (§26, processed 2026-09-09) held the seam: "restaurant-procurement-platform (order-centered; purchase data = price feed)." This pass must confirm it.
3. **procurement-management-platform** (§10, processed 2026-09-06) pre-recorded: "Sector overlay leaves — Restaurant Procurement Platform (§26) and Sustainable Procurement Platform (§21) apply domain overlays (foodservice specifics; ESG criteria) to this structure; recorded as variants, not merged." This pass must research whether the restaurant instantiation is a mere overlay or a distinct domain instantiation (the family pattern set by restaurant-inventory-management vs generic inventory-management-system).
4. **foodservice-distribution-management** (§20, processed 2026-09-08) documented the distributor (sell side); this leaf is the buyer side of the same trading relationship.

## Initial Boundary

Working hypothesis before research:

- Core use: manage the restaurant's purchasing from suppliers — what to buy, from whom, at what price, ordered and tracked as purchase orders, received and checked against deliveries, reconciled against supplier invoices.
- Users: chef / kitchen manager (places orders), owner/GM (approves, watches spend), purchasing manager (multi-unit), bookkeeper/AP (invoice processing).
- Nearest types: Restaurant Inventory Management (stock-centered sibling), Restaurant Food Cost Management (money-centered sibling), Procurement Management Platform (generic family parent), Purchase Order Management (§10), Procure-to-pay Platform (§10), Foodservice Distribution Management (§20, supplier side), Supplier Portal (§10), Restaurant Management System (suite), AP Automation / Invoice Processing (§08).
- Key unknowns: (1) What is the central object — PO, order guide, supplier relationship, or invoice? (2) How do orders originate (par levels, forecasts, order guides, manual)? (3) Is the delivery+invoice closure loop definitional or common? (4) Is invoice/AP processing part of this Type's core or an adjacent capability? (5) Is this leaf a distinct Type or a sector variant of the generic Procurement Management Platform? (6) What is restaurant-specific in the supplier record (delivery schedules, lockup times, customer numbers, order guides)?

## Research Questions

1. What is the central object of the purchasing operation, and what does the supplier record carry?
2. How does an order come into being — need signals (par, stock position, sales forecast), saved order lists, manual entry?
3. What is the order lifecycle (draft → sent → outstanding → delivered → closed), and how are orders transmitted (email, EDI, portal, punch-out)?
4. What happens at delivery — verification against the order, shortages/substitutions, price paid vs expected, write-back to stock and prices?
5. How do supplier invoices enter and get reconciled (against orders, against receipts), and what follows from discrepancies (credits, settlements)?
6. What purchasing controls exist (budgets, price limits, minimum order amounts, approvals, permissions) and are they definitional?
7. What is restaurant-specific: order guides, par-driven ordering, delivery-day/lockup machinery, price volatility tracking, distributor integrations, foodservice units?
8. Where does payment sit (in-product, separate product, out of scope)?
9. Where are the boundaries vs inventory, food cost, the generic procurement family, P2P, PO management, foodservice distribution, and AP automation?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer levels:

| Product | Philosophy / position | Customer level | Evidence quality |
|---|---|---|---|
| Apicbase | enterprise F&B management suite with a fully documented Procurement module (ordering/receiving/suppliers/integrations) | enterprise / multi-unit / international (European vendor) | **Tier 1** (help center articles — deepest operational evidence) |
| MarketMan | standalone inventory-first cloud platform with a named Purchasing & Receiving solution | SMB independents → small chains → multi-unit | Tier 2 (product + FAQ pages; help center unreachable in prior passes) |
| Restaurant365 | restaurant management suite; Purchasing & Receiving as a named sub-product of the Inventory & Purchasing pillar | SMB → franchise/multi-location | Tier 2 (product pages + FAQ) |
| Toast (xtraCHEF by Toast) | POS-ecosystem pole; invoice-first heritage inside the Supplier & Accounting Suite | SMB → mid-market, Toast ecosystem | Tier 2 (product pages; ordering detail from the inventory pass) |
| Craftable | procurement-centered back-office pole ("Intelligent Ordering" as the lead module) | mid-market / multi-unit / hospitality (restaurants + hotels) | Tier 2 (dedicated ordering product page, rich) |

Cross-pass context (not primary samples): Crunchtime (RMS pass 2026-09-09 — vendor/supplier integrations: order guides, PO confirmations, invoices, purchase orders, bid sheets). MarginEdge unreachable in two prior passes (transport errors ×3) — not retried per network rules; no MarginEdge claims made.

## Sources

Fetched 2026-09-09:

- Apicbase Help Center (Tier 1):
  - Procurement module index — https://support.apicbase.com/help/procurement
  - The guide to procurement — https://support.apicbase.com/help/the-guide-to-procurement
  - How do I generate a purchase order? — https://support.apicbase.com/help/purchase-order
  - How can I receive orders? — https://support.apicbase.com/help/receive_order
  - Invoice Reconciliation — https://support.apicbase.com/help/invoice-reconciliation
  - Demand Forecasting / Order Suggestion — https://support.apicbase.com/help/demand-forecasting
  - Supplier information — https://support.apicbase.com/help/supplier_information
- MarketMan — https://www.marketman.com/platform/ (platform index); https://www.marketman.com/platform/restaurant-purchasing-software-and-order-management (self-labeled "Restaurant Purchasing & Procurement Software" page + FAQ)
- Restaurant365 — https://www.restaurant365.com/inventory/ (pillar hub); https://www.restaurant365.com/inventory/purchasing-receiving/ (dedicated page + FAQ)
- Toast / xtraCHEF — https://xtrachef.com/ (root; features nav incl. Procurement/purchase-order-management, AP Automation, Manufacturer Rebates); https://www.toasttab.com/xtrachef (redirects to Toast product page for xtraCHEF by Toast)
- Craftable — https://www.craftable.com/intelligent-ordering/ (dedicated Intelligent Ordering page + FAQ)

Unreachable / abandoned (per network rules): marketman.com/platform/purchasing-software (404 — correct URL found via platform index), restaurant365.com/purchasing/ and /inventory/purchasing/ (404 — correct URL found via pillar hub), toasttab.com/ordering, /purchasing, /xtrachef (404 — xtraCHEF domain used instead), xtrachef.com/features/ordering/ (404; /features/purchase-order-management/ redirects to the Toast product page). MarketMan help center remains unreachable from prior passes (transport error; not retried). R365 knowledge base sits behind a support portal and was not article-fetched.

## Product Observations

### Apicbase (evidence layer A — Tier 1 help center)

- **Module map**: Procurement = Ordering + Receiving + Suppliers + Supplier Integrations — a module *separate from* Inventory (Counting + Stock Management). "The procurement module works together with the Inventory and Sales Analytics module resulting in a realtime overview of your inventory."
- **Ordering prerequisites** (guide to procurement): ingredients in the library with minimum info (name, price, article number, quantity, unit); suppliers with minimum info (name + **email address for orders**).
- **PO generation** (purchase-order article): Procurement → Create Orders → choose **outlet** → ingredient list filterable by supplier → quantities (+/−, or the **"To Par"** button: "the quantity will be automatically calculated based on the difference of the par level and the remaining quantity in stock") → **Shopping Cart with one tab per supplier** ("if you create an order consisting out of ingredients from several suppliers… You have to send each order to each supplier separately") → set **delivery date and time** ("You will see the possible delivery dates according to the lockup times you have set for this supplier") → E-mail Order → confirm → order lands in the **"Sent Order"** tab; the supplier receives the order by email (can export Excel/CSV, print); a copy goes to the restaurant.
- **Order lists**: "If you often order the same set of items, you can create order lists that you can load easily."
- **Receiving** (receive_order article): "It is very important to register every order that you have received prior to a certain stock count **before** you do this count." Per stock item: **delivery state** (all / part / none delivered), **Delivered Qty** (only when part), **Price paid** ("This can differ from the expected price which was calculated using the price for the stock item in Apicbase"), remarks with standardized options (wrongly delivered, wrongly ordered, delivered too much, late delivery, pricing issue). **"Update price" checkbox**: "the price you paid will be updated for this product in your Apicbase library. This is an easy way to keep your prices in Apicbase up to date." Extra items delivered but not ordered can be added. Invoice status on the order: Not yet received / Received / Payable / Paid, plus invoice # and invoice document. **"Update Stock" checkbox**: uncheck so a late-registered delivery does not double-add stock already counted. Save Draft / Save Delivery (partial, keep open for next deliveries) / Save Delivery & Close Order → "Delivered" tab. Past events registrable.
- **Invoice Reconciliation** (AI module, Tier 1): three-step process — import (PDF/XML upload, email to an outlet-specific address, API, manual entry) → AI-powered matching to **closed** POs (supplier name, VAT, PO number, line items, quantities, subtotal excl. VAT; auto-link at a documented 60% match threshold, manual dropdown linking below) → comparison ("Invoice Amount − PO Amount = Difference") to "verify the goods listed on the invoice were actually ordered and received… ensures payment is only made for what was delivered." Differences route to **settlement or credit requests** with the supplier. Approval/payment statuses: Received, Verified/Pending approval, Flagged, Approved, Rejected, Paid — **"Apicbase does not process payments."** Supported scenarios: multiple invoices per PO, multiple POs per invoice, credit notes linked to POs, manual invoice creation.
- **Demand forecasting / order suggestion** (Tier 1): "sales-based ordering… uses your actual sales data to predict future needs. By translating past sales into ingredient demand, Apicbase suggests what to order and how much." Top-down: POS sales → recipes (Bill of Materials) → ingredient usage → historic patterns per weekday → expected demand for a chosen period. Configuration: ordering period (days), sales source (same period last week vs 4-week average), scale (revenue projection %, safety-stock %), inventory integration (subtract current stock; subtract outstanding orders). "Always review suggestions — forecasts are guidance, not guarantees." Prerequisites: POS items linked to recipes, sufficient sales history, consistent inventory management.
- **Supplier records** (supplier_information article, Tier 1): Supplier Dashboard (total order value, last order value; **orders in progress** [created, not sent] / **delivered orders** / **outstanding orders** [sent, delivery not yet registered]); contact details (address, contact person, phone, VAT number, supplier id, **email address for orders**, **customer number at this supplier**, linked outlets); **Outlet Ordering Details** per outlet: **minimum order amount**, per-outlet customer numbers, order email, **delivery dates and times with lockup day/time** ("if you have set your delivery day to Wednesday, you can choose your lockup day, which is basically the day you can order the latest"); **"sent reminder"** notifications when an order has not yet been made; missed-lockup alerts are reminders only ("this does not affect your ability to create orders"); minimum order amounts notify but "we will not block the order from being sent out"; **Ingredient List per supplier** (the order guide — every ingredient linked to that supplier, exportable/printable); optional CSV order attachment for manual suppliers; integrated suppliers may set their own lockup schedules; a supplier cannot be removed while linked to an active ingredient package.
- **Supplier integrations**: named distributor integrations (US Foods, Gordon Food Service, Bidfood NL/UK, Sligro, Hanos, Transgourmet, Brakes, Booker, Kespro, Solucious, …) plus "The Assortment Manager."

### MarketMan (evidence layer A for fetched pages; Tier 2 product/FAQ)

- Platform index: named solutions include **Purchasing and Receiving** ("one platform to communicate with all your vendors"), Accounts Payable Automation, Vendor Management, **Vendor Payments** (separate solution page: "pay your restaurant vendor bills online"), Multi-Unit & Commissary, and **"Solutions for food Distributors"** (the vendor also sells to the supply side).
- Purchasing page (self-labeled "Restaurant Purchasing & Procurement Software"): "Chefs and managers can submit purchase orders, check statuses, and manage vendors from one unified platform."
  - "Control Purchasing with Custom Permissions and Alerts — Create par levels, budgets, price limits, & user permissions. Set up alerts to track **shorts, subs, credits, & billing irregularities**."
  - "Manage All Restaurant Vendors from One Mobile App — Eliminate emails, texts, & calls by automatically submitting purchase orders via the web or mobile app… simply **fill to par with one click**."
  - "MarketMan tracks ingredient prices across all of your vendors to ensure optimal pricing."
  - "AI-powered Receiving, with real-time pricing"; "Smart Ordering… uses predictive analytics to forecast demand."
- FAQ: "MarketMan monitors your inventory levels against par levels you set… When stock drops below the par threshold, the system automatically generates a **suggested purchase order** for the relevant supplier. You review and approve the order with one click, then it's sent directly to the supplier." "You can manage catalogs, pricing, and order history for every supplier, **compare prices across vendors**, and send orders to multiple suppliers simultaneously." "When a delivery arrives, your team opens the purchase order in the MarketMan mobile app and **checks off items as they're received**. Any quantity discrepancies or missing items are flagged immediately. The system updates your inventory counts automatically once the delivery is confirmed." POS sales data → theoretical usage → "feeds directly into the automated reorder calculations."
- Integrations: major food distributors (Sysco, PFG logos on page), POS (Toast, Square, Lightspeed), accounting (QuickBooks, Xero).

### Restaurant365 (evidence layer A for fetched pages; Tier 2 product)

- Suite structure: **Inventory & Purchasing** pillar with named sub-products — Inventory Management, Recipes, Prep, **Purchasing and Receiving**, Cash Management, Commissary, AI Dashboards — beside Accounting (with its own AP Automation product), Workforce, Payroll & HR pillars.
- Purchasing & Receiving page: "Generate **AI-driven purchase orders** based on actual demand to reduce waste and over-ordering."
  - "Order exactly what you need — Forecast demand accurately to avoid overbuying and reduce waste."
  - "Spot issues fast — Automatically detect delivery problems, resolve them quickly, and **recover credits** before they hit your bottom line."
  - "Sync receiving with inventory — Automatically update stock as items arrive."
  - "Maintain margins with invoice accuracy — Quickly identify and resolve **invoice discrepancies**."
  - "Create purchase orders based on up-to-date inventory data for smarter buying"; "Rely on **forecasts and PAR levels** to minimize waste and prevent stockouts"; "Speed up purchasing with seamless **EDI** integration and automated workflows."
- FAQ: "R365 integrates vendor ordering, invoices, and inventory in one system. By tracking price changes in real time and flagging invoice discrepancies **before they're paid**, operators can control costs." "R365 connects with major food and beverage distributors, allowing you to place orders, receive deliveries, and update inventory automatically without duplicate data entry." "Invoices can be routed through a **digital approval workflow**… before payments are made." Multi-location: "standardize purchasing across locations, **compare vendor performance**, and consolidate reporting."

### Toast / xtraCHEF by Toast (evidence layer A for fetched pages; Tier 2; ordering detail cross-pass)

- xtraCHEF by Toast (Toast product page): "restaurant back-office software for **invoice automation**, recipe costing, inventory management, and cost reporting… built for US restaurants and hospitality groups that need to track ingredient costs, monitor margins, reduce manual data entry, and **connect purchasing data with accounting**." "Automating invoice processing unlocks line-item details allowing you to drill down into how fluctuating costs are impacting your financial performance."
- Toast nav: **Supplier & Accounting Suite** = "xtraCHEF cost analytics" + "Inventory management" as separately listed products; legacy xtraCHEF features nav listed **Procurement (purchase-order-management)**, AP Automation, Food Cost Management, Inventory Management, Recipe Management, Budgets + Forecasting, **Manufacturer Rebates**.
- Cross-pass context (inventory pass, 2026-09-09, Toast inventory product page): "Take inventory once, and we'll create an **order guide** for you based on what's on hand and what's required to maintain par"; "Schedule **recurring orders** to ensure you're maintaining par levels"; "Send orders directly to your suppliers."

### Craftable (evidence layer A; Tier 2 — procurement-centered pole)

- Intelligent Ordering page: "Stop losing margin at the purchase order… Craftable gives your team **one platform to order from every vendor, enforce contract pricing, approve spend, and track every dollar from PO to payment**."
- **Vendor Ordering** ("Place it"): "Order from every vendor in one place — no more jumping between emails, portals, and spreadsheets to fill a single cart. Place **multi-vendor orders from a single cart**; auto-generate purchase orders with vendor details; order via **EDI, Punchout, or Enhanced Catalogs**; standardized item descriptions prevent substitution errors."
- **Approval Workflows** ("Approve it"): "Customize approval limits by location, department, and amount; build multi-step approvals; keep a complete audit trail; **block unauthorized or duplicate orders** before they're placed."
- **Invoice Matching** ("Match it"): "Every invoice line verified against your **purchase order and delivery receipt** — before you pay a cent. Match invoices to orders and receipts line by line; flag discrepancies before payment is approved; block unreceived or unauthorized charges; **only pay for what was actually delivered**."
- **Overcharge Detection** ("Catch it"): "Auto-flags overcharges, substitutions, and price creep… auto-match invoices to contracts at the SKU level; drill into cost variances by vendor, department, or time period; spot product substitutions; track **vendor pricing reliability** over time."
- **Budget Management** ("Track it"): limits by budget status/location/GL code; proactive alerts; live spend vs budget across departments.
- **Budgets & Forecasting** ("Plan it"): budgets from purchasing history and vendor pricing trends; "track COGS with a live declining balance."
- FAQ: "Restaurant Intelligent Ordering software helps operators place orders with vendors digitally, track purchasing activity, and maintain **vendor catalogs and pricing** in one system… visibility into every purchase **from order to invoice**." Mobile approvals; multi-location centralized purchasing with standardized vendor catalogs and contract pricing; "Craftable connects purchasing, receiving, inventory, AP automation, and financial reporting in one platform."

### Crunchtime (cross-pass context from the restaurant-management-system pass, 2026-09-09)

- Integrations page: **Vendors & Suppliers** — "order guides, PO confirmations, invoices, purchase orders, bid sheets"; POS/accounting/HR integrations around a management layer that consumes them.

## Cross-product Comparison

| Structure / capability | Apicbase | MarketMan | R365 | Toast/xtraCHEF | Craftable |
|---|---|---|---|---|---|
| Supplier records with orderable supply (linked items/catalogs, prices) | ✓ (Ingredient List per supplier; packages/pricing) | ✓ ("catalogs, pricing, and order history for every supplier") | ✓ (vendor catalogs; standardized purchasing) | ✓ (vendor management, product catalogs) | ✓ ("vendor catalogs and pricing in one system") |
| Ordering arrangements on the supplier record (order email, customer #, delivery schedule) | ✓ Tier-1 (order email, customer numbers, delivery days + lockup times, min order amount) | implied (order submission per supplier) | implied (distributor connections) | — (not on fetched pages) | implied (vendor details on POs) |
| Purchase order as managed object with lifecycle | ✓ (in progress → sent/outstanding → delivered; cancel sent order) | ✓ (submit, check statuses) | ✓ (create, track) | ✓ (order guides → orders) | ✓ ("from PO to payment") |
| Order creation from need signals (par/stock/forecast) | ✓ ("To Par"; sales-based order suggestions subtracting stock + outstanding orders) | ✓ (par-threshold suggested POs; "fill to par"; predictive demand) | ✓ (AI-driven POs from actual demand; forecasts + PAR levels) | ✓ (order guide from count vs par; recurring orders) | ✓ (auto-generate POs; budgets/forecasting) |
| Saved order lists / recurring orders | ✓ (order lists) | ✓ (implied via par routine; recurring per inventory pass at Toast) | ✓ (implied) | ✓ (recurring orders) | — (not on fetched page) |
| Order transmission to suppliers | ✓ (email; CSV attachment; integrated suppliers) | ✓ (auto-submit web/mobile; "sent directly to the supplier") | ✓ (distributor connections; EDI) | ✓ ("send orders directly to your suppliers") | ✓ (EDI, Punchout, Enhanced Catalogs) |
| Delivery verification against the order | ✓ Tier-1 (all/part/none, delivered qty, price paid, standardized remarks) | ✓ (check off items; discrepancies flagged) | ✓ (detect delivery problems; recover credits; sync received to inventory) | implied (invoice quantities received) | ✓ (invoice vs PO **and delivery receipt**) |
| Price paid vs expected + price write-back | ✓ Tier-1 ("Update price" on receipt) | ✓ (price tracking across vendors; real-time pricing on receiving) | ✓ (tracking price changes in real time) | ✓ (ingredient price fluctuation alerts) | ✓ (overcharge detection; contract-price enforcement at SKU level) |
| Invoice capture & reconciliation against orders/receipts | ✓ Tier-1 (AI matching to closed POs; Difference; credit notes) | ✓ (invoice processing; billing irregularity alerts) | ✓ (invoice discrepancies flagged before payment; approval workflow) | ✓ (invoice automation is the heritage) | ✓ (line-by-line 3-way match) |
| Shorts / substitutions / credits machinery | ✓ (standardized remarks; settlement requests) | ✓ (alerts to track shorts, subs, credits) | ✓ (delivery problems → credits) | — (not on fetched pages) | ✓ (substitutions flagged; block unreceived charges) |
| Purchasing controls (budgets, price limits, approvals, permissions) | ✓ (min order amounts; per-outlet ordering details; user management) | ✓ (par levels, budgets, price limits, user permissions) | ✓ (invoice approval workflow; multi-location standardization) | — (not on fetched pages) | ✓ (approval limits by location/dept/amount; multi-step; budget limits) |
| Multi-vendor ordering in one place | ✓ (shopping cart, one tab per supplier) | ✓ (all vendors one app; multiple suppliers simultaneously) | ✓ (vendor ordering in one system) | ✓ (implied) | ✓ (single cart across vendors) |
| Sales-based demand forecasting | ✓ Tier-1 (sales-based ordering module) | ✓ (predictive analytics; POS → theoretical usage → reorder) | ✓ (AI-driven POs from actual demand) | ✓ (via POS data / AvT adjacency) | ✓ (budgets from history; forecasting) |
| EDI / punch-out / distributor integrations | ✓ (named distributor integrations; Assortment Manager) | ✓ (major food distributors) | ✓ (EDI integration) | ✓ (distributor connections implied) | ✓ (EDI, Punchout, Enhanced Catalogs) |
| Multi-location posture | ✓ (outlets; per-outlet ordering details; internal ordering to production kitchens) | ✓ (Enterprise: centralized ordering/receiving; commissary) | ✓ (standardize, compare vendor performance, consolidate) | ✓ (across locations) | ✓ (centralized purchasing across properties) |
| Payment execution | ✗ explicit ("Apicbase does not process payments") | separate product (Vendor Payments page) | via accounting/AP products | via accounting integrations | "PO to payment" framing; AP automation module |
| Sourcing events / RFx | ✗ (absent from module) | ✗ (absent) | ✗ (absent; bid sheets only at Crunchtime integrations) | ✗ | ✗ (absent) |
| Packaging | suite module (beside Inventory, separate) | standalone platform solution | suite sub-product | POS-ecosystem suite product | back-office platform lead module |

Reading of the table (evidence layer B — cross-product commonality):

- **Supplier records with orderable supply + PO lifecycle + delivery verification + invoice reconciliation** are present in 5/5. The closure loop (order → delivery → invoice → write-back) is universal in the sample.
- **Need-signal ordering** (par levels, stock positions, forecasts → suggested/drafted POs) is 5/5 — the demand model that distinguishes this instantiation from requisition-governed corporate buying.
- **Order transmission to suppliers** (email/EDI/portal) is 5/5.
- **Purchasing controls** (budgets, limits, approvals, permissions) are documented in 4/5 fetched surfaces (Toast not verified) — common mature, not definitional (a small operation orders without approval chains; the paper-era practice had none).
- **Sales-based forecasting** is 5/5 but always rides on recipes + POS data — common mature structure (a bar ordering by par without recipes is still this Type).
- **Payment execution** is NOT definitional: explicitly out of scope at Apicbase, a separate product at MarketMan, accounting-side elsewhere.
- **Sourcing events/RFx are absent** from all 5 sampled products' cores — a sharp difference from the generic procurement family.
- **Multi-location** posture is common (4/5 explicit) — variant layer by scale.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The Type is the **restaurant's purchasing operation as a managed order pipeline** — the buyer-side system of record for buying food, beverage, and supplies from vendors. Three jointly-held structures:

1. **Suppliers of record with their orderable supply and ordering arrangements** — identified vendors (broadline distributors, specialty vendors, farmers, beverage suppliers) held as persistent records carrying what the restaurant buys from them (per-supplier item lists / order guides with prices), plus the arrangements that make ordering executable: where orders go (order email/address), the account identity (customer numbers), when deliveries can happen (delivery days with order-by deadlines), and commercial constraints (minimum order amounts). Remove → a PO tool with free-typed payees, or a contact list.
2. **Purchase orders as managed commitments created from the operation's need signals** — persistent orders toward specific suppliers, drafted from par levels and stock positions, sales-based forecasts, saved order lists, or direct entry; transmitted to suppliers (email, EDI, portal, punch-out); tracked through a lifecycle (in preparation → sent/outstanding → delivered/closed). The demand signal originates in the kitchen's own consumption — what the operation will use — not in internal requisitions. Remove → a shopping list or a reorder suggestion; without the order object there is no purchasing operation.
3. **The delivery-and-invoice closure loop** — deliveries verified against the order (full / partial / none per line, shortages, substitutions, price paid vs expected), supplier invoices captured and reconciled against orders and receipts, discrepancies pursued as credits/settlement requests, and the verified quantities and prices written back into the operation's records (stock, item prices, downstream costing). Remove → order transmission with no closure; the operation never learns what actually arrived, what it truly cost, or whether the vendor billed correctly.

Jointly-held load-bearing checks:

- 1 alone = vendor contact list / price book.
- 2 without 1 = free-typed PO tool (generic Purchase Order Management territory).
- 3 without 1+2 = invoice processing / AP automation alone.
- 1+2 without 3 = ordering with no closure — conceivable (a pure ordering tool) but unsampled; every sampled product closes the loop, and the paper-era practice includes delivery check-in and invoice checking.
- 1+3 without 2 = standing arrangements + invoice processing without orders — AP + receiving, below the Type.
- 2+3 without 1 = anonymous ordering with closure — conceivable but unsampled.

Deliberately NOT in L0 (checked against the sample): par levels and reorder machinery (a manual-ordering operation is still this Type — the paper era ordered by judgment), sales-based forecasting (rides on recipes + POS), order guides as named structures (the supplier's item list satisfies leg 1 without the guide), EDI/punch-out (email satisfies transmission), purchasing controls/approvals (small operations order without them; paper era had none), invoice OCR/AI (manual entry satisfies closure), multi-location, commissary/internal ordering, payment execution (explicitly out of scope at one sampled product), sourcing events/RFx (absent from all sampled cores), mobile apps, cloud, AI.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- **Par levels / min quantities → suggested or drafted purchase orders** — "fill to par," order guides generated from stock vs par, one-click approval (5/5)
- **Sales-based demand forecasting / order suggestions** — POS sales × recipes → ingredient demand for a chosen period, minus current stock and outstanding orders (5/5; recipe+POS-dependent)
- **Order lists / recurring orders** — saved order templates for repeated purchases; scheduled recurring orders (documented 3/5 fetched + Toast cross-pass)
- **Order guides as named structures** — per-supplier lists of regularly ordered items (Apicbase ingredient lists per supplier; Toast order guides; Crunchtime order guides)
- **Price tracking across vendors + price write-back on receipt** — price paid vs expected at receiving; "update price" into the item library; price-fluctuation alerts; vendor price comparison (5/5)
- **Delivery scheduling machinery** — delivery days, order-by deadlines (lockup times), reminders when an order hasn't been placed (Apicbase Tier-1; implied elsewhere)
- **Shorts / substitutions / credits machinery** — standardized delivery-exception remarks, credit recovery, settlement requests (4/5 fetched)
- **Invoice processing depth** — capture (upload/email/API), extraction, GL coding, approval workflows, discrepancy flagging before payment (5/5 in some form)
- **Purchasing controls** — budgets, price limits, minimum order amounts, user permissions, approval workflows with audit trails (4/5 fetched)
- **Multi-vendor ordering in one place** — single cart across suppliers; orders sent per supplier (5/5)
- **EDI / punch-out / distributor integrations** — direct connections to major food distributors (5/5 in some form)
- **Multi-location structure** — per-location ordering, standardized catalogs, vendor-performance comparison, consolidated reporting (4/5 explicit)
- **Internal ordering / commissary** — orders to internal production kitchens, aggregated and turned into production plans and BoMs (Apicbase Tier-1; R365 commissary; MarketMan Enterprise)
- **Spend analytics / order dashboards** — spend by vendor/category/location; order history; purchasing patterns (5/5)
- **Mobile ordering and receiving** — order submission and delivery check-in from phones (4/5 fetched)

### L2 — Variant / Optional Structure

- **Payment execution** — vendor bill payment in-product (MarketMan Vendor Payments page) or out of scope entirely (Apicbase explicit); AP automation as bundled vs separate product
- **Manufacturer rebates** (xtraCHEF feature)
- **Budgets & forecasting depth** — COGS declining balance, budget-vs-actual with alerts (Craftable)
- **Bid sheets / light sourcing** (Crunchtime vendor integrations) — corporate-style RFx events are NOT restaurant-typical
- **Two-sided posture** — platforms selling solutions to distributors as well (MarketMan "Solutions for food Distributors")
- **Commissary sales to third parties** (R365)
- **AI layers** — AI-driven POs, AI invoice matching, AI receiving, AI assistants (era-current; 5/5 name some AI)
- **Hotel/institutional anchoring** (Craftable hospitality positioning; Apicbase outlets model)
- **Suite vs standalone vs POS-ecosystem packaging**; plan-tier gating
- **Regional machinery** — VAT handling, returnables/deposit containers (crates, bottles — Apicbase), e-invoicing where mandated

### L3 — Vendor-specific (research notes only)

- Apicbase: lockup times and delivery-day machinery; "To Par" button; shopping cart with per-supplier tabs; order states (in progress / outstanding / delivered); invoice-reconciliation 60% auto-match threshold and processing statuses; settlement requests; returnables (in/outgoing); "Update Stock" checkbox semantics; CSV order attachment; per-outlet ordering details; supplier dashboard; "cannot remove supplier linked to active ingredient package"; Assortment Manager; named European distributor integrations
- MarketMan: "fill to par with one click"; shorts/subs/credits alert framing; buyer-portal login domain; tier gating (Starter/Growth/Enterprise); "15,000+ customers," "10M+ invoices processed" claims (marketing)
- R365: "AI-driven purchase orders based on actual demand"; EDI integration framing; vendor-performance comparison; invoice approval workflow; "$400M food waste cut" claim (marketing)
- Toast: xtraCHEF branding inside Supplier & Accounting Suite; invoice-first heritage; "order guide from a single count"; Manufacturer Rebates feature
- Craftable: "One Cart" multi-vendor ordering; "Enhanced Catalogs"; overcharge detection with vendor-pricing-reliability tracking; COGS "live declining balance"; "95% operators battling food costs" NRA stat (marketing); "track every dollar from PO to payment" framing

## Vendor-specific / Rejected Findings

- **"Restaurant procurement = corporate procurement with food color"** — rejected as a merge. The skeleton (suppliers + orders + closure) is shared with the generic procurement family, but the instantiation differs structurally: demand originates in the operation's own consumption signals (par, stock, sales forecasts, order guides) rather than internal requisitions governed by policy; the closure loop writes back into stock and item prices (feeding the restaurant's own costing) rather than ending at a payable; governance is light (spend limits, order approval) rather than a policy engine; sourcing events/RFx are absent. Documented as a **domain instantiation** of the procurement family — keep-both, consistent with the restaurant-inventory vs generic-inventory family pattern. The PMP pass's "sector overlay variant" reading is refined, not overturned.
- **"Invoice/AP automation is the center of this Type"** — rejected as center. Invoice-first products exist (xtraCHEF heritage; MarginEdge by reputation) and invoice processing is universal, but the sampled products' own module structures center the order pipeline (Apicbase Procurement = Ordering/Receiving/Suppliers; Craftable's lead module is Intelligent Ordering; R365's sub-product is Purchasing *and* Receiving). Invoice processing serves the closure loop and doubles as an adjacent AP capability.
- **"Sourcing events / RFx are part of restaurant procurement"** — rejected: absent from all 5 sampled products' cores; corporate e-sourcing machinery has no restaurant counterpart in the sample (bid sheets appear only as an integration artifact at Crunchtime).
- **"Payment execution is definitional"** — rejected: Apicbase states "Apicbase does not process payments"; MarketMan sells vendor payments as a separate solution; R365 routes payment through its accounting products.
- **"AI ordering/matching is definitional"** — rejected: era-current layer over manual-equivalent structures (Apicbase documents manual linking paths beside AI matching; order lists and par ordering predate AI).
- **"Price comparison across distributors is definitional"** — held at L1: strong restaurant color (5/5 track prices) but a fixed-price-contract operation without comparison tooling is still this Type.
- Vendor marketing figures (MarketMan 15,000+/10M+/percent claims; R365 $400M; Craftable 95%/4.5%/$30K) — recorded as claims, never promoted to the final document.

## Boundary Findings

1. **vs Restaurant Inventory Management (§26 sibling, processed)** — the closest sibling; seam held from this side, ratifying the inventory pass's framing. Inventory's center is the **stock record** (what's on hand, counts, par, events); procurement's center is the **order lifecycle** (suppliers, POs, transmission, receiving as fulfillment, invoice closure). Inventory *generates* reorder suggestions from stock positions; procurement *owns* the order from drafting through closure. Receiving is the seam activity: in inventory it is stock-in (posting quantities); in procurement it is order fulfillment (verification against the order, shortages, price paid). Bundled in most products (MarketMan, R365, Toast) but structurally separable — Apicbase ships Procurement and Inventory as **separate modules**, and Craftable splits Intelligent Ordering from Inventory & Recipe Management. Removal tests: strip the order lifecycle (suppliers, POs, transmission) → inventory management remains; strip the stock record (counts, on-hand, events) → a purchasing operation on order guides and invoices remains.
2. **vs Restaurant Food Cost Management (§26 sibling, processed)** — seam held from this side: food cost consumes purchase data as its **price feed** (invoice prices → costed recipes → theoretical vs actual); procurement owns the buying that produces those prices. The closure loop's price write-back is the bridge. Remove the order pipeline → food cost management survives on invoice prices alone (the meez pole).
3. **vs Procurement Management Platform (§10 generic, processed)** — the family-parent relationship. Same PO-centered skeleton (suppliers + demand + orders + closure). Structural differences: (a) demand model — restaurant orders arise from the operation's consumption signals (par/stock/forecast/order guides); corporate demand arises from internal requesters governed by purchasing policy; (b) closure target — restaurant closure writes back into stock and item prices feeding the operation's costing; corporate closure ends at a payable handed to finance; (c) governance depth — light spend controls vs policy engines with budget checks at request time; (d) sourcing — RFx events are core-adjacent in corporate procurement and absent in restaurant procurement; (e) supplier-record content — ordering arrangements (delivery days, lockup times, customer numbers, order guides) vs onboarding/qualification/risk. **Keep-both as distinct leaves** (domain instantiation, family pattern per restaurant-inventory vs generic inventory). The PMP pass's "sector overlay" reading is refined: the overlay is structural (demand model + closure), not cosmetic.
4. **vs Purchase Order Management (§10, processed)** — POM centers the single PO object's lifecycle (create → approve → issue → fulfill → close). Restaurant procurement centers the whole purchasing operation around it: supplier relationships with ordering arrangements, need-signal order creation, and the delivery+invoice closure loop feeding the operation. Test: remove supplier management, need signals, and closure → a PO tool remains.
5. **vs Procure-to-pay Platform (§10, processed)** — P2P's definitional gate is invoice matching and its endpoint is a payment-ready payable. Restaurant procurement's closure ends at verified receipts and updated prices/stock; payment is typically out of scope (Apicbase explicit) or a separate product (MarketMan). Test: make the payable the endpoint → P2P; end at verified receipt + price write-back → this Type.
6. **vs Foodservice Distribution Management (§20, processed)** — the two sides of one trading relationship. The distributor's system runs the sell side (customer order guides as selling instruments, stock, routes, invoicing); the restaurant procurement platform runs the buy side consuming those order guides. The order guide and EDI connection are the shared integration surface. Test: flip the operating party → the other Type.
7. **vs Supplier Portal (§10, processed)** — some restaurant products give suppliers confirmation surfaces; the portal is the supplier-facing slice of the buyer's operation, not the operation itself. Test: remove the buyer-side operation → a supplier portal remains.
8. **vs Restaurant Management System (§26, processed)** — suite packaging. R365 ships Purchasing & Receiving as a sub-product of the Inventory & Purchasing pillar; Toast bundles xtraCHEF in the Supplier & Accounting Suite. Remove the suite neighbors → this Type remains.
9. **vs AP Automation / Invoice Processing (§08)** — invoice capture, extraction, coding, and approval are common adjacent capabilities and the closure loop's substrate, but invoice-only products (no suppliers, no orders, no receiving) sit beside this Type, not inside it. Test: remove the order pipeline → AP automation remains.
10. **vs Restaurant POS** — the POS is the sales/depletion input that feeds demand signals (sales-based ordering); it does not own purchasing. Integration, not identity.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the three-leg definition?

- **Paper-era restaurant purchasing** (conceptual lineage, high confidence): the order book with a page per vendor — items regularly bought, prices, customer/account numbers (leg 1); order sheets or phone orders placed against par lists and the chef's judgment, noted in the book (leg 2); delivery check-in against the order at the back door, invoice checked against the delivery and filed, prices noted for the next order (leg 3). The sampled products' own marketing describes exactly this pre-software practice ("no more jumping between emails, portals, and spreadsheets"; "eliminate emails, texts, & calls"; "ditch the sheets and clipboards" per the inventory pass). ✓
- **Standing orders** (milk/bread/beverage vendors on fixed schedules): recurring orders are L1; the standing arrangement itself satisfies legs 1+2 with the delivery/invoice check as leg 3. ✓
- **Regional**: Apicbase is a European vendor (VAT-excl. comparisons, lockup times, returnables/crates as deposit containers); US samples integrate Sysco/US Foods/PFG-class distributors. No region-specific machinery appears in the core. ✓
- **Era machinery kept outside the core**: EDI, punch-out, AI matching/extraction, OCR, mobile apps, cloud, dashboards — none required by the definition. ✓

Check passes: the three-leg core is era-agnostic and region-agnostic.

## Uncertainties

1. **Ordering-only tools unsampled** — vendor-ordering apps without receiving/invoice closure (pure "order from your phone" products) were not sampled; their classification (below the Type vs thin variant) is unverified. The L0's third leg rests on 5/5 sampled products plus the paper-era practice, not an exhaustive market census.
2. **MarketMan help center unverified** — unreachable in prior passes (transport error; not retried). Evidence is product/FAQ pages; FAQ statements are vendor claims, not help-documentation verification.
3. **R365 knowledge base not article-fetched** — support portal is a ticket/search portal; evidence is product pages + FAQ.
4. **Toast ordering depth** — verified via the inventory pass's product page (order guides, recurring orders, send-to-suppliers) and this pass's xtraCHEF pages; no Toast help-center articles fetched. Receiving mechanics at Toast unverified on fetched surfaces.
5. **Craftable evidence is Tier-2** — rich product page but no help-center articles; operational click-paths unverified.
6. **Bid sheets / light sourcing depth** — seen only as a Crunchtime integration artifact; no restaurant product sampled with a sourcing-events module.
7. **MarginEdge** — unreachable in two prior passes; no claims made.
8. **Approval-workflow universality** — documented at 4/5 fetched surfaces (Toast unverified); held L1.

## Final Synthesis

A Restaurant Procurement Platform is the restaurant's purchasing operation as a managed order pipeline: suppliers of record carrying their orderable supply (per-supplier item lists with prices) and their ordering arrangements (order addresses, customer numbers, delivery days with order-by deadlines, minimum order amounts); purchase orders created from the operation's own need signals — par levels and stock positions, sales-based forecasts, saved order lists, or direct entry — and transmitted to suppliers; and a closure loop that verifies deliveries against orders (shortages, substitutions, price paid vs expected), reconciles supplier invoices against orders and receipts, pursues discrepancies as credits, and writes the verified quantities and prices back into the operation's stock and costing records. Around that core, mature products add par-driven order suggestions, sales-based forecasting, order guides and recurring orders, price tracking across vendors, EDI/distributor integrations, purchasing controls (budgets, limits, approvals), multi-location central purchasing, commissary/internal ordering, and spend analytics. The Type's center is the order — inventory generates the suggestions and receives the stock; food cost consumes the prices; the generic procurement family shares the skeleton but requisitions its demand and ends at a payable, while this instantiation orders from consumption signals and closes at the back door. Products realize the Type as standalone platforms, suite sub-products, POS-ecosystem modules, and procurement-led back-offices — one order pipeline, several postures.
