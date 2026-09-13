# Research Notes — Retail Merchandising Platform

Research date: 2026-09-07
Slug: retail-merchandising-platform
Directory leaf: Retail Merchandising Platform (05.13 Merchandising)

## Research Goal

Understand what a "Retail Merchandising Platform" actually is as an Application Type, from real products. The leaf name is ambiguous in the market, so the first goal is disambiguation:

- Hypothesis A: the leaf maps to the classic retail **merchandise management system** ("merchandising system") — the back-office system of record for the merchandise lifecycle: item setup, purchasing/receiving, cost and price management, perpetual inventory / stock ledger, distribution to stores, feeding POS and financials.
- Hypothesis B (raised by the processed sibling `assortment-planning-application`): the leaf is an **umbrella** over the merchandising planning disciplines (assortment, category, space, pricing/promotion planning).
- Hypothesis C: the leaf maps to **digital/e-commerce merchandising** (searchandising — controlling product ranking/presentation in online storefronts).

Then: extract the core objects, the canonical merchandise lifecycle, the interfaces, the rules, and the boundaries against the unusually large neighbor set (Retail Inventory Management, PIM, Purchase Order Management, Retail Pricing Management, Promotion Management, Assortment Planning, Category Management, Space Planning, Retail POS, Order Management, ERP, WMS).

## Initial Boundary

Working hypotheses before research:

- Core use (A): administer the merchandise lifecycle of a multi-location retailer — what the items are, what they cost, what they sell for, who supplies them, how much is where, and how merchandise moves from supplier to shelf.
- Users: merchandisers, buyers, pricing analysts, inventory control, allocation analysts, merchandise controllers/finance; store staff at the receiving/counting edge.
- Nearest neighbors: Retail Inventory Management (stock discipline), PIM (product data), Purchase Order Management (generic PO machinery), Retail Pricing Management and Promotion Management (pricing/promo disciplines), Assortment/Category/Space Planning (planning disciplines), Retail POS (selling surface), Order Management (customer orders), ERP (company-wide back office), WMS (warehouse operations).
- Unknowns: which hypothesis the market supports; whether allocation/replenishment is definitional; whether sales audit is definitional; how the SMB end realizes the Type; whether the digital-merchandising homonym needs a taxonomy note.

## Research Questions

1. What do vendors that sell products named "merchandising" actually put inside them?
2. What is the core object set — item, merchandise hierarchy, supplier, purchase order, receipt, stock ledger, price?
3. What is the canonical merchandise lifecycle workflow from item setup to financial posting?
4. What exactly is the "stock ledger", and how does it relate to operational inventory?
5. How does the system relate to POS / e-commerce (downstream consumers) and to the general ledger (financial export)?
6. Which capabilities are common vs variant: replenishment, allocation, sales audit, promotions, markdowns, transfers, RTV, counts, franchise/consignment, import management?
7. How do customer segments differ — enterprise modular cloud services vs integrated retail ERP vs vertical specialist MMS vs POS-integrated mid-market retail management?
8. Where are the boundaries against each neighbor, with removal tests?
9. Is the "umbrella" hypothesis (B) or the "merchandise management system" hypothesis (A) correct?
10. Does the digital-merchandising homonym (C) constitute a separate Type that this leaf must not absorb?

## Representative Products

| Product | Pole | Customer tier | Why selected |
|---|---|---|---|
| Oracle Retail Merchandising Foundation Cloud Service (RMFCS) | modular cloud merchandising system (the classic "merchandising system" lineage) | enterprise | the reference implementation of the Type; only sampled product with public Tier-1 operational documentation |
| Aptos Merchandising | integrated retail ERP suite module | enterprise | explicit "retail ERP" framing; stock ledger + AP matching narrative; allocation/forecasting/replenishment sold as sibling |
| Island Pacific SmartRetail (Merchandise Management System) | vertical specialist MMS (fashion/apparel heritage) | mid-market to enterprise | vendor whose core product is literally named "Merchandise Management System (MMS)"; clean suite-structure evidence |
| Retail Pro (Retail Pro International) | POS-integrated retail management platform | SMB to mid-market, international | shows the low/mid end where merchandising machinery (POs, min/max, transfers, allocation, price changes) is embedded in a retail management system |
| Constructor (boundary check only) | digital product discovery / e-commerce merchandising | enterprise e-commerce | homonym check — confirms Hypothesis C is a different Type, not part of this leaf |

Considered and unreachable (recorded as source-access limitations, no claims made): Blue Yonder merchandise management (blueyonder.com 404 on two URL patterns across two passes), STORIS (storis.com 503 ×2), Futura4Retail (transport error), Aptos operational documentation (no public help library found), Retail Pro operational documentation (partner/customer-portal gated).

## Sources

Fetched 2026-09-07:

- Oracle Retail index (documentation library listing): https://docs.oracle.com/en/industries/retail/
- Oracle Retail Merchandising Foundation Cloud Service — Get Started: https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/
- Oracle RMFCS — Use Merchandising (task/book listing): https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/use.html
- Oracle RMFCS — Stock Ledger Overview (Financial Management user guide): https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/rmfug/stock-ledger-overview.htm
- Oracle RMFCS — Item Overview (Items user guide): https://docs.oracle.com/en/industries/retail/retail-merchandising-foundation-cloud/latest/ritug/item-overview.htm
- Aptos Merchandising product page: https://www.aptos.com/product/merchandising
- Aptos homepage (suite structure): https://www.aptos.com/
- Island Pacific homepage (suite structure): https://www.islandpacific.com/
- Island Pacific Merchandise Management System page: https://www.islandpacific.com/merchandise-management-system
- Retail Pro homepage: https://www.retailpro.com/
- Constructor homepage (homonym check): https://constructor.io/

Unreachable (limitations): Blue Yonder (404 ×2), STORIS (503 ×2), Futura4Retail (transport error), Oracle RMFCS Functional Overview / data model (My Oracle Support login-gated), Aptos and Retail Pro documentation portals (gated or not publicly indexed).

## Product Observations

### Oracle Retail Merchandising Foundation Cloud Service (Tier 1 — official docs; Evidence Layer A)

Definition observed on the Get Started page:

> "Retailers leverage Oracle Retail Merchandising Foundation Cloud Service (RMFCS) functionality to execute core merchandising activities, including item management, inventory replenishment, purchasing, import processes, sales auditing, and financial tracking. RMFCS includes both the Sales Audit and the Trade Management modules."

Sales Audit: "evaluates sales transactions from all channels, identifying any missing, duplicate, or erroneous data and highlighting any suspicious transactions, to ensure errors are resolved so that downstream systems operate off the same cleansed sales information." Trade Management: manages the import process (automating import steps, file exchanges with trading partners, central database of import order information).

Use Merchandising task structure (directly observed TOC):

- **Foundation Data**: Locations destination (stores, warehouses, location lists, cost zones), Organizational Hierarchy, Merchandise Hierarchy (departments → classes → subclasses), Suppliers, Partners, Expense Profiles.
- **Items**: Create an Item; Add Suppliers; Define Initial Prices; Add Locations; Create Child Items; Classify Import Items; Create a Like Item; Manage Items; Upload/Download Items from a Spreadsheet; Reclassify Items; Manage/Use Item Lists; Item Foundation Data.
- **Order and Contracts**: Create/Manage Purchase Orders; Specialty Purchase Orders; Upload/Download Orders from a Spreadsheet; Create/Manage Contracts.
- **Deals and Cost Changes**: Create/Manage Cost Changes; Create/Manage Deals; Fixed Deals.
- **Finance**: Stock Ledger Overview; View Transaction Data; Average Cost Adjustment; Receiver Cost Adjustment; Budgeted Shrink Rates; Financial Administration Data.
- **Inventory Management**: View Inventory by Location; Create/Manage Transfers; Mass Return Transfers (MRT); Return to Vendor (RTV); Ship a Purchase Order; Ship a Transfer; Receive a Shipment; Reconcile Transfers and Allocations; Inventory Adjustments (by item / by location); Stock Counts (schedule / request / manage).
- **Price Management**: View Price Change History; Manage Competitive Pricing.
- **Franchise**: Franchise Overview; Franchise Costs; Franchise Orders; Franchise Returns.
- **Replenishment**: Activate Items on Replenishment; Manage Attributes; Scheduled Updates; Buyer Worksheet; Replenishment Results for Purchase Orders; Replenishment Foundation Data.
- **Global Tax Change**: overview, configuration, maintenance, tax builder.
- **Mobile Workflows**: recent transfers, recent orders.

Stock Ledger Overview (directly observed):

> "The Merchandising financial management module primarily aims to maintain an accurate stock ledger, export financial data to an external financial system, and monitor a company's performance based on key performance indices."
> "The stock ledger in Merchandising records the financial results of the merchandising processes such as buying, selling, price changes, and transfers. All of these transactions are recorded in the Merchandising stock ledger and rolled up to the subclass/location level for days, weeks, and months, depending on calendar settings."

Stock ledger details: multi-currency (transaction-level local currency, rollup converted to primary currency); supports both **retail method and cost method** of accounting (cost method uses standard or average cost per configuration); supports the **retail 4-5-4 calendar** and the Gregorian calendar, with daily/weekly/monthly maintenance; supports **multiple sets of books** mapped to locations of an external financial system.

Item Overview (directly observed):

> "Merchandising is usually the master of all items for a retail organization. It manages the creation and maintenance of items, as well as the communication of these items to other dependent solutions."

- Item hierarchy: up to three levels (referred to as Style / SKU / Reference Item; fashion uses style→SKU→barcode, grocery may use SKU→barcode); one level designated the **transaction level** (where transactions and inventory occur).
- Item type indicators: **Sellable** ("will be sent to the selling systems (e.g. POS, OMS)"), **Orderable**, **Inventoried** ("track inventory and to have stock on hold in Merchandising"), **Catch Weight** (items purchased/sold in varying weights, weighed at receiving).
- Ownership type: **owned, consignment, or concession** per supplier terms at location level.
- Item types: Regular; **Pack** (simple = multiples of one component; complex = many components; buyer packs vs vendor packs); **Deposit** items (contents/container/crate/returned components — bottle-deposit semantics); **Transformable** items (ordered as one item, transformed into sellable components — e.g., cheese wheel cut into pieces; production-loss yield).
- Item page sections: Descriptions (with AI-assisted description suggestion), Pack, **Cost and Price** (cost zone group, suggested retail, selling unit retail, selling UOM), Usage and Units (store order multiple each/inner/case, standard UOM, UOM conversion factor, merchandise/forecastable/on-replenishment flags), Attributes (service level, product classification, brand, gift wrap, ship alone), Differentiators (**diffs** — up to four characteristics such as color/size that generate child items), Grocery Attributes (deposit linkage, package size, wastage %, perishable, retail label, temperature sensitivity), Comments.
- More Actions from the item: Suppliers, Retails by Zone, Locations, Up Charges, Children, Pack setup, Transformation, Replenishment attributes, Substitute Items, User Defined Attributes, Related Items, Import attributes/HTS/tariffs, Timelines, Required Documents, VAT, Season/Phases, Ticket Type, Images.
- Item status lifecycle: a new item starts with status **"Worksheet"** (approval workflow implied; approval errors review is a named task).
- AI assistance: attribute extraction from item image/text at creation, description suggestion/refinement — optional, configuration-gated.

### Aptos Merchandising (Tier 2 — official product page; Evidence Layer A for this product, marketing depth)

Page title: "Retail Merchandising and Inventory — Make the most of every dollar invested in your assortments."

- Framing: "Put our full **retail ERP suite** of integrated applications to work to manage your merchandise in every channel and location."
- Core capabilities listed: **perpetual inventory management; item, vendor and cost management; purchase order management; actionable analytics.**
- Warehouse: "Our optional WMS integrates with Aptos Merchandising" (receiving/ticketing/inventory; picking/packing/shipping; cross-docking; vendor compliance).
- Financial coupling: "Integrated Accounts Payable matching capabilities and our integrated **Stock Ledger** closely connect Merchandising and Accounting ensuring tight controls over every facet of merchandise accounting." "From PO to payment: Purchase Orders, Receipts, Invoices."
- **Allocation, Forecasting & Replenishment (AF&R)** is a separate named product: "forecast, allocate and replenish based on plans, actuals, and trends" (automated forecast algorithm selection, what-ifs, SKU-level forecasts from daily sales/inventory patterns).
- Suite siblings on the homepage nav: Order Management, Store Fulfillment, Point of Sale (Aptos ONE), Analytics, CRM, Sales Audit, Merchandising.
- Marketing claims observed (kept as claims): 100 clients use Aptos Merchandising; 35 years merchandising experience.

### Island Pacific SmartRetail — Merchandise Management System (Tier 2 — official product pages; Evidence Layer A for this product, marketing depth)

Homepage: "Island Pacific provides the **Core Retail Merchandise Management System** you need to scale in an omnichannel fashion to thousands of stores." Suite: "Choose our integrated Merchandise Management (MMS), Order Management System (OMS) and Business Intelligence (BI) Solutions for today's global multi channel retailer. Our core MMS also plays nice with 3rd Party Solutions."

MMS page — "SmartRetail is our comprehensive Merchandise Management System offering a robust suite of tools to streamline your merchandise operations, from inventory management to insightful business intelligence." Core features listed:

- **Inventory Management & Stock Ledger** — "Maintain accurate inventory levels, track stock movement... We maintain a detailed record of all stock transactions, providing complete visibility into your inventory's history."
- **Master Data Management** — "Centralized management of product information, ensuring data accuracy and consistency across all systems."
- **Purchasing** — "Efficiently manage the procurement process, from supplier selection to order tracking and invoice processing."
- **Supplier Portal** — "Streamlined communication and collaboration with your suppliers through a dedicated online portal."
- **Price & Promo Management** — "Easily manage pricing strategies, promotions, and discounts."
- **Retail Finance & Sales Audit** — "Gain detailed insights into your financial performance, sales trends, and key metrics."
- Integrated extras: **WMS**, OMS, BI, POS, **Merchandise Planning (SmartPlanning)**, **Omnichannel (SmartOmni)**, and **Retail Robot** (a separate cloud all-in-one for small business: "smart inventory, offline POS... from mom & pop shops to enterprise chains").

Positioning copy: "powerful tools for forecasting, allocation and assortment management, replenishment, and merchandising" — planning and allocation named as siblings of the MMS. Industries: fashion & apparel, footwear, general merchandise, outdoor & sports, jewelry/perfume/gifts.

### Retail Pro (Tier 2 — official homepage; Evidence Layer A for this product, marketing depth)

Positioning: "Powerful POS & Retail Management for Specialty Retail" — POS-first, with merchandising machinery embedded:

- Headline capabilities: intuitive tailorable POS; **robust pricing & promotions**; store operations & back office; performance & KPI reporting; **replenishment & inventory management**; customer & employee management.
- Customer quote (Pet Station, observed on page): "smart features such as **purchase orders, min/max functionality and calculators, auto utilities, such as transfers, item allocation functions, sale functions, price change schedules**."
- Customer quote (Earthbound Trading): "When we started using replenishment functionality in Retail Pro, we saw business grow 20%."
- Add-ons sold separately: Planning & Open-to-Buy, Visual Analytics, Reporting, SAP Link, Loyalty, RFID — confirming that planning is NOT inside the base merchandising/retail-management product.
- Localization emphasis: fiscal & tax compliance (VAT, India GST, Canada GST/HST, Brazil ICMS, tax zones), regional adaptations via API, fully translatable UI; marketing claims: 130+ countries, 54,000 customers, 540,000... (54,000 customers / 159,000 POS as displayed).
- Unified-commerce framing: "Unify your retail data in Retail Pro POS for a single point of truth about your inventory, operations and customers."

### Constructor (Tier 2 — homonym check only; Evidence Layer A for the homonym's existence)

Constructor positions itself as "AI Ecommerce Search and Product Discovery" — a "Commerce Reasoning Engine" delivering search & autosuggest, browse/category-page personalization, recommendations, retail media, collections, AI shopping agents, and "Merchandiser Controls" (dashboards, controls, experiments over result ranking). Its object of work is the **digital presentation and ranking of products in a storefront**, not the acquisition, costing, pricing, or stock of physical merchandise. No purchase orders, no stock ledger, no supplier machinery. Confirms Hypothesis C is a different Application Type that merely shares the word "merchandising."

## Cross-product Comparison

| Dimension | Oracle RMFCS | Aptos Merchandising | Island Pacific MMS | Retail Pro |
|---|---|---|---|---|
| Self-description | "core merchandising activities: item management, inventory replenishment, purchasing, import processes, sales auditing, financial tracking" | "retail ERP suite... manage your merchandise in every channel and location" | "Core Retail Merchandise Management System" | "POS & Retail Management" with merchandising machinery embedded |
| Item master | explicit system-of-record claim ("usually the master of all items"); 3-level hierarchy; diffs; item types; sellable/orderable/inventoried | "item, vendor and cost management" | "Master Data Management — centralized management of product information" | item catalog inside retail management (customizable fields observed in customer quote) |
| Supplier/purchasing | suppliers, item-supplier, POs, contracts, deals, cost changes | "purchase order management"; vendor management | "Purchasing — supplier selection to order tracking and invoice processing"; Supplier Portal | purchase orders (customer-attested) |
| Receiving | Ship PO / Receive a Shipment / Reconcile | "Purchase Orders, Receipts, Invoices" (PO→payment) | purchasing incl. invoice processing | receiving within back office |
| Cost machinery | deals, fixed deals, cost changes, bracket costing, average/receiver cost adjustments | "cost management" | (within purchasing/finance) | (vendor cost on POs) |
| Price machinery | retail by zone, price change history, competitive pricing | (pricing within suite; promotions at POS) | "Price & Promo Management" | "robust pricing & promotions"; price change schedules |
| Stock ledger | named, financial: records buying/selling/price changes/transfers; cost & retail methods; 4-5-4 calendar; multi-currency; multi-books; GL export | named: "integrated Stock Ledger closely connect[s] Merchandising and Accounting" | named: "Inventory Management & Stock Ledger — detailed record of all stock transactions" | (inventory management; no named stock ledger at marketing depth) |
| Inventory operations | transfers, MRT, RTV, adjustments, stock counts, view by location | "perpetual inventory management" | inventory management module | transfers, item allocation, min/max |
| Replenishment | named module (activate items, buyer worksheet, results → POs) | separate AF&R product | named sibling capability ("replenishment") | named capability (min/max, replenishment) |
| Allocation | separate Retail Allocation Cloud Service; reconcile transfers and allocations | separate AF&R product | named sibling capability ("allocation") | item allocation functions |
| Sales audit | named module (Sales Audit) | separate Sales Audit product | "Retail Finance & Sales Audit" | (not at marketing depth) |
| Ownership models | owned / consignment / concession; franchise module | (not observed) | (not observed) | (not observed) |
| Financial integration | export to external financial system; multiple sets of books | AP matching; "connect Merchandising and Accounting" | Retail Finance | SAP Link add-on |
| Planning | separate planning cloud services (MFP, Assortment, etc.) | (planning not in this product) | separate Merchandise Planning (SmartPlanning) | separate Planning & Open-to-Buy add-on |
| POS relationship | items "sent to the selling systems (e.g. POS, OMS)" | sibling Aptos ONE POS | sibling POS product | POS is the flagship; merchandising embedded around it |
| Packaging | modular cloud services under one merchandising umbrella | module of retail ERP suite | core MMS + integrated suite | retail management platform (POS-first) |
| Tier | enterprise | enterprise | mid-market/enterprise, fashion vertical | SMB/mid-market, international specialty |

Cross-product commonalities (Layer B): item master as the governed center; supplier + purchase orders + receiving; cost and price carried on the item; perpetual stock by location with a financial valuation layer (named "stock ledger" at three of four vendors); transfers/RTV/adjustments/counts; replenishment; price changes; financial export/AP matching; distribution of item+price to selling systems; planning sold as a separate product.

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant

Minimal structure; removing any element stops the product from being recognizable as a retail merchandising system:

1. **Merchandise item master (system of record)** — governed records for the retailer's sellable items: identity (SKU/barcode), placement in a merchandise hierarchy (department/class/subclass), commercial attributes (unit cost, retail price, units of measure), supplier linkage, and lifecycle status; the system is the master that communicates items to dependent selling systems.
2. **Merchandise acquisition** — supplier records, purchase orders, and recorded receiving that bring merchandise into the business, with supplier cost terms (deals/cost changes) attached.
3. **Stock ledger (perpetual inventory with financial valuation)** — on-hand stock per item per location (stores/warehouses), changed only by recorded movements (sales, receipts, transfers, adjustments, returns to vendor), valued and rolled up (by merchandise hierarchy × location × time) as the financial record of merchandise, exportable to the external financial system.

Framing: a back-office, item-centric system of record for multi-location retail, feeding selling systems (POS/OMS/e-commerce) and financials. "Merchandising" here is the retail-IT discipline of running the merchandise lifecycle — not marketing merchandising and not digital result-ranking.

§24 historical check: the classic 1990s-era merchandising systems (the Retek/JDA/Island Pacific/STS lineage that today's products descend from) operated on exactly this core — item master, POs/receiving, pricing, stock ledger, allocation — without cloud delivery, AI, or omnichannel; POS-integrated SMB back offices satisfy the same core at smaller scale. The core survives the historical check. Digital merchandising (Hypothesis C) does NOT satisfy it (no acquisition, no stock ledger) — confirming it is a different Type.

### L1 — Common Mature Structure

Present across the researched sample; expected in mature products but not definitional:

- merchandise hierarchy management (department/class/subclass) and organizational hierarchy (stores, warehouses, cost zones)
- item variants (style–color–size via differentiator characteristics), packs, deposit items, transformable/catch-weight items (vertical-dependent)
- price management machinery: prices by zone/location, price changes as effective-dated events, promotions, markdowns
- supplier deals, cost changes, invoice matching (PO → receipt → invoice → AP)
- inter-location transfers, returns to vendor, mass return transfers, inventory adjustments with reasons, physical stock counts
- replenishment (min/max-class logic, reorder suggestions, auto-PO generation)
- allocation of receipts to stores (in-suite or as a sibling optimization product)
- sales audit — cleansing POS transaction feeds before financial posting
- franchise / consignment / concession ownership models
- tax machinery (VAT/GST regimes, tax zones, global tax change)
- import/trade management (import orders, trading-partner file exchange)
- spreadsheet bulk upload/download; item lists; like-item creation; substitute/related items
- reporting/analytics; mobile companion views; supplier portals
- multi-currency, retail (4-5-4) calendar, multiple sets of books (enterprise tier)
- integration posture: item/price/stock distribution to POS/OMS/e-commerce; GL export; ERP/SAP links

### L2 — Variant / Optional Structure

Depends on segment, vertical, geography, deployment:

- segment pole: enterprise modular cloud services (merchandising foundation + separate allocation/pricing/invoice-matching services) vs integrated retail ERP suite vs vertical specialist MMS vs POS-integrated retail management platform (merchandising embedded; the SMB/mid realization)
- vertical tuning: grocery (catch weight, perishability/wastage, deposit containers), fashion (style-color-size, seasons/phases), general merchandise/hardlines
- deployment: cloud SaaS vs on-premise heritage
- ownership models activated: owned-only vs consignment/concession/franchise
- allocation/replenishment depth: basic min/max in-suite vs dedicated optimization products
- WMS bundling (optional module vs separate product vs none)
- omnichannel scope: store/warehouse-centric core vs omnichannel extensions (endless aisle, order orchestration siblings)
- regional localization depth (fiscal/tax regimes, multi-country, translatable UI)
- AI assistance (attribute extraction, description drafting) — modern, optional
- planning attachment: none vs bundled planning add-ons vs sibling planning products

### L3 — Vendor-specific (research notes only)

- Oracle: RMFCS module names (Sales Audit, Trade Management), item status "Worksheet", "Retail by Zone", cost zone groups, store order multiple (each/inner/case), diffs (up to four), deposit item component model (contents/container/crate/returned), transformable orderable/sellable with production-loss yield, 4-5-4 calendar, multiple sets of books, budgeted shrink rates, buyer worksheet, mass return transfers, ODA/AI Assist configuration gating
- Aptos: AF&R (Allocation, Forecasting & Replenishment) as named sibling; "optional WMS"; "100 clients / 35 years" marketing claims
- Island Pacific: SmartRetail (MMS), SmartPlanning, SmartOmni, Retail Robot (SMB all-in-one), "Core Merchandising Diagram" infographic
- Retail Pro: Prism POS lineage, App Market / SAP Link, localization claims (130+ countries, VAT/GST/ICMS), Nayax acquisition context

## Vendor-specific Findings

- The named "stock ledger" is explicit at Oracle, Aptos, and Island Pacific — strong cross-product signal for the financial-valuation layer, but the *term* is vendor vocabulary; the underlying concept (perpetual stock + valuation + rollup + GL export) is the invariant.
- Oracle's item-status lifecycle ("Worksheet" → approved) is directly observed; equivalent approval workflows at other vendors are implied but not verified at marketing depth.
- Oracle's franchise module and consignment/concession ownership types are directly observed; other vendors' ownership-model support is unverified.
- Retail Pro's localization breadth claims are marketing claims (kept as claims, not asserted as operational fact).

## Rejected Findings

- **Hypothesis B ("umbrella over planning disciplines") — rejected as the Type definition.** All sampled vendors sell planning (merchandise financial planning, assortment planning, open-to-buy) as *separate* products or add-ons (Oracle planning cloud services; Island Pacific SmartPlanning; Retail Pro Planning & Open-to-Buy add-on; Aptos sells planning outside the Merchandising page). The merchandising product is the operations system of record. The umbrella exists only as marketing language around a product family.
- **"Allocation/replenishment is definitional" — rejected.** Oracle and Aptos ship allocation/replenishment as separate products; smaller systems do manual allocation. → L1.
- **"Sales audit is definitional" — rejected.** Named at Oracle/Island Pacific and sold separately by Aptos; not universal. → L1.
- **"WMS is definitional" — rejected.** Optional module (Aptos) / integrated extra (Island Pacific). → L2.
- **"Multi-currency / multi-books / 4-5-4 calendar is definitional" — rejected.** Enterprise-tier features. → L1.
- **"Omnichannel/e-commerce scope is definitional" — rejected.** Classic merchandising systems are store/warehouse-centric; omnichannel is an extension posture. → L2.
- **"AI assistance is definitional" — rejected.** Configuration-gated modern add-on. → L2.
- **"Digital merchandising belongs to this Type" — rejected.** Different objects (result ranking vs merchandise lifecycle), different users (e-commerce/merchandising-experience teams vs retail back office), no acquisition/stock machinery. Homonym only.

## Boundary Findings

| Neighbor | Relationship | Distinction | Removal test (what flips the Type) |
|---|---|---|---|
| Retail Inventory Management (05.12, processed) | contains / overlaps on stock | Inventory management is the *stock discipline* application: quantities, movements, counts, replenishment, POs — usable without item-master governance, supplier terms, or price machinery. The merchandising system is the *item-lifecycle system of record* that contains an inventory layer and adds item governance, supplier/cost/price machinery, and financial valuation. | Strip item-master governance + supplier + pricing machinery, keep the stock discipline → Retail Inventory Management. Strip the stock ledger from the merchandising system → PIM + PO tool (not merchandising). |
| PIM (05.04, processed) | adjacent data layer | PIM manages product *content/attributes* for distribution to selling/marketing channels (enrichment, syndication); the merchandising item master manages the *commercial* item record (cost, price, supplier, stock) for operations. They integrate; some MMS modules are even named "Master Data Management" (Island Pacific) — the seam is what the record is for. | Remove cost/price/supplier/stock and acquisition, keep enrichment/content syndication → PIM. |
| Purchase Order Management (§10, processed) | contains a specialized instance | Generic buyer-side PO commitment machinery vs the merchandising system's retail-specific acquisition (deals, costing, receiving into retail stock, RTV, item-supplier records). | Remove the merchandise context (deals/costing/stock receipt), keep generic PO commitments → Purchase Order Management. |
| Retail Pricing Management (05.14, unprocessed) | adjacent discipline | Pricing management owns price *strategy/optimization/execution* as a discipline; the merchandising system holds base item prices and price-change machinery as part of the item lifecycle. Oracle ships a separate Retail Pricing Cloud Service beside RMFCS. | Remove item/stock/PO machinery, keep price strategy/optimization → Retail Pricing Management. |
| Promotion Management (05.14, processed) | adjacent discipline | Promotion management owns the promotion record lifecycle and performance; the merchandising system's promo machinery is one module inside merchandise operations. | Remove merchandise operations, keep promotion objects/lifecycle/performance → Promotion Management. |
| Assortment Planning (05.13, processed) | upstream planning | Assortment planning produces the period-bound SKU offering plan; the merchandising system executes it (items created, POs cut, stock distributed). Assortment plans reconcile to financial plans; merchandising records actuals. | Remove operations, keep the period-bound offering plan → Assortment Planning. |
| Category Management (05.13, unprocessed) | upstream planning | Category management owns ongoing category strategy/performance; merchandising owns item-level operations. | Remove operations, keep category strategy/performance view → Category Management. |
| Retail Space Planning (05.13, unprocessed) | adjacent planning | Space planning owns physical shelf (planograms); merchandising owns the offering and its stock. | Replace merchandise lifecycle with shelf-layout objects → Space Planning. |
| Retail POS (05.10, processed) | downstream consumer | POS is the selling surface (priced catalog → sale → tender); merchandising is the back office that defines the catalog, prices, and stock the POS consumes. Sales flow back as postings. | Remove the back office, keep the selling surface → Retail POS. |
| Order Management (05.07, processed sibling family) | different order object | OMS manages *customer* orders through fulfillment; the merchandising system manages *supplier* orders (POs) and the stock they create. | Replace POs/receiving with customer-order lifecycle → Order Management. |
| ERP (§10) | integrates / partial overlap | The merchandising system is retail-merchandise-specific; ERP is company-wide (finance, HR, manufacturing). Merchandising systems export to external financials and are often flanked by ERP ("retail ERP" framing at Aptos describes the suite, not generality). | Generalize beyond merchandise to company-wide back office → ERP. |
| WMS (§10) | optional add-on | WMS owns warehouse *operations* (putaway, picking, bins); merchandising owns the merchandise record and stock levels, delegating warehouse execution. | Replace item lifecycle with warehouse execution → WMS. |
| Digital merchandising (Constructor/Algolia-class; no directory leaf) | homonym only | Digital merchandising controls product ranking/presentation in digital storefronts (search, browse, recommendations); no acquisition, no stock ledger, different users. | n/a — different Type; recorded as a taxonomy note. |

Resolution of the sibling flag from `assortment-planning-application`: the 05.13 bundle concern is resolved from this side — "Retail Merchandising Platform" is realized in the market as the **merchandise management system** (operations system of record), not as a planning umbrella and not as assortment/category planning under another name. The three 05.13 planning leaves and this operations leaf remain distinct Types with a planning→execution handoff.

## Uncertainties

- Blue Yonder, STORIS, Futura4Retail documentation could not be reached; their inclusion would likely confirm the same core (they are commonly described as merchandise management systems) but no claims about them are made.
- Aptos, Island Pacific, and Retail Pro evidence is product-page depth (Tier 2); operational mechanics (statuses, editability rules, exact workflows) are verified only for Oracle. Cross-product claims about operational detail are therefore calibrated down.
- The exact boundary between the merchandising system's inventory layer and a separately purchased Retail Inventory Management product is fuzzy in the SMB segment (Retail Pro-class platforms embed both); the boundary is drawn on the item-lifecycle vs stock-discipline center of gravity, not on product packaging.
- Whether every merchandising system includes an approval workflow on item creation (Oracle's "Worksheet" status is the only directly observed instance) is unverified.
- SMB-native realization: the low end of the market appears to run POS+inventory applications without a distinct merchandising system; inferred from Retail Pro's positioning and the prior retail-inventory-management pass (Square/Erply/Cin7), not independently verified here.
- Oracle's data model and functional overview are login-gated; some module-depth claims (e.g., exact stock-ledger posting rules) rest on the overview page only.

## Final Synthesis

A Retail Merchandising Platform — realized in the market as the retail **merchandise management system** ("merchandising system") — is the retailer's back-office system of record for its merchandise. Its defining core is three objects and the lifecycle that binds them: a governed **item master** (SKU records in a merchandise hierarchy, carrying cost, retail price, supplier linkage, and sellable/orderable/inventoried status, communicated to POS/OMS/e-commerce), **merchandise acquisition** (suppliers, purchase orders, deals and cost changes, receiving), and the **stock ledger** (perpetual stock per item per location, changed only by recorded movements, valued by cost or retail method, rolled up by hierarchy × location × time, and exported to the financial system). Around this core, mature products add price-change and promotion machinery, replenishment and allocation, transfers/RTV/counts/adjustments, sales audit of POS feeds, franchise/consignment ownership models, tax and import management, and enterprise financial machinery (multi-currency, retail calendar, sets of books). The Type is distinct from the planning disciplines that feed it (assortment, category, space, merchandise financial planning — all sold as separate products by the same vendors), from the stock-discipline application (Retail Inventory Management), from PIM (content vs commercial record), and from the digital "merchandising" homonym (result ranking in e-commerce discovery). The umbrella reading of the leaf name is rejected on vendor evidence: "merchandising" as a product category is the merchandise management system; planning hangs off it, not inside it.
