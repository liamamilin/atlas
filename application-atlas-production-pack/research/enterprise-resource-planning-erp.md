# Research Notes — Enterprise Resource Planning / ERP

## Research Goal

Understand what an ERP actually is as an Application Type: what its defining structure is, what objects and workflows it contains, how operational business activity connects to financial accounting, how it is configured and operated, and where its boundary lies against accounting software, supply-chain point solutions, and business suites.

## Initial Boundary (hypothesis before research)

- ERP = integrated business back office: sales, purchasing, inventory, production, and finance operating on one shared transactional data core, with operational documents posting into a shared financial ledger.
- Nearest neighbors: Accounting Software (finance only), Inventory Management System / WMS (physical stock execution), MES (shop-floor execution), CRM (customer-facing), HRIS (workforce), Business Management Suite (possible alias/umbrella), Manufacturing ERP / Agribusiness ERP (industry variants, separate leaves in the directory).
- Suspected defining property: integration (shared core + automatic financial posting), not any single function.
- Unknowns: how products organize functional scope; how posting works in each product; permission models; configuration/implementation model; deployment/tier variants.

## Research Questions

1. What is the shared data core, and how do operational documents post into the financial ledger?
2. What are the core objects (GL/chart of accounts, journals, customer, vendor, item, BOM, sales order, purchase order, inventory, production order)?
3. How do the canonical end-to-end flows work (order-to-cash, procure-to-pay, plan-to-produce, record-to-report)?
4. Which functional areas are standard, and which are optional/variant?
5. How do roles and permissions work?
6. How does configuration/implementation happen (this is a major difference from ordinary applications)?
7. What varies by deployment, customer tier, industry, and region?
8. Where exactly is the boundary against Accounting Software, WMS, MES, CRM, HRIS, and "business management suite" products?

## Representative Products

Selected for market representativeness + documentation quality + different philosophies + different customer tiers:

| Product | Tier / philosophy | Why selected |
|---|---|---|
| SAP S/4HANA Cloud (Public Edition) | Enterprise tier; modular classic ERP lineage (R/2 → R/3 → ECC → S/4HANA); public/private cloud | The archetypal enterprise ERP; process-naming vocabulary (order-to-cash, procure-to-pay, record-to-report) |
| Microsoft Dynamics 365 Business Central | SMB/mid-market; cloud-first; functional-area organization (descendant of NAV) | Best publicly accessible operational documentation; document/posting model fully exposed |
| Oracle NetSuite | Mid/enterprise; cloud-native SaaS suite ("one unified business management suite") | Records + transactions model; GL-impact-of-transactions documentation |
| Odoo | SMB; open-source, app-based modular model | Different packaging philosophy (installable apps on one core); docs site blocked, evidence degraded to structure level |

## Sources

Research date: 2026-09-06

Fetched successfully (Tier 1/2):

- Microsoft Learn — Business Central documentation hub: https://learn.microsoft.com/en-us/dynamics365/business-central/
- Microsoft Learn — Financial management: https://learn.microsoft.com/en-us/dynamics365/business-central/finance
- Microsoft Learn — Sales overview: https://learn.microsoft.com/en-us/dynamics365/business-central/sales-manage-sales
- Microsoft Learn — Purchasing overview: https://learn.microsoft.com/en-us/dynamics365/business-central/purchasing-manage-purchasing
- Microsoft Learn — Posting sales documents: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-post-sales
- Microsoft Learn — Managing inventory: https://learn.microsoft.com/en-us/dynamics365/business-central/inventory-manage-inventory
- Microsoft Learn — Manufacturing overview: https://learn.microsoft.com/en-us/dynamics365/business-central/production-manage-manufacturing
- Microsoft Learn — About production orders: https://learn.microsoft.com/en-us/dynamics365/business-central/production-about-production-orders
- Microsoft Learn — Define granular permissions: https://learn.microsoft.com/en-us/dynamics365/business-central/ui-define-granular-permissions
- Oracle Docs — NetSuite portal: https://docs.oracle.com/en/cloud/saas/netsuite/
- Oracle Docs — NetSuite Basics / Working with Records, Transactions, and Lists: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_N488023.html
- Oracle Docs — Accounting set / General Accounting: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/preface_3710627041.html
- Oracle Docs — General Ledger Impact of Transactions: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_N1459499.html
- Oracle Docs — Order Management set: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/set_4423275132.html
- Oracle Docs — SCM set / Manufacturing book / Inventory Management book: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/set_N1734902.html , book_1506002637.html , book_N2249433.html
- SAP — S/4HANA Cloud Public Edition product page (positioning + FAQ): https://www.sap.com/products/erp/s4hana.html
- SAP — GROW finance page (process/capability naming): https://www.sap.com/products/erp/grow/finance.html
- GitHub (official Odoo documentation source repo) — applications tree: https://github.com/odoo/documentation/tree/17.0/content/applications and raw inventory_and_mrp.rst

Source-access limitations:

- SAP Help Portal (help.sap.com) returned a JavaScript shell; no operational SAP documentation could be fetched. SAP evidence is therefore positioning/process-naming level (Tier 2), not operational detail. All SAP-specific structural claims (company codes, movement types, etc.) are NOT asserted from fetched evidence and are kept out of the final document or marked as general knowledge without citation.
- odoo.com/documentation returned 403 twice; raw.githubusercontent.com fetch of finance.rst timed out twice. Odoo evidence is degraded to the observed documentation structure (app categories) only. No detailed Odoo operational claims are made.
- NetSuite SuiteAnswers and PDF user guides require login; public docs.oracle.com help was used instead.

## Product Observations

### Microsoft Dynamics 365 Business Central (evidence layer A — directly observed)

Documentation hub organizes the product into functional areas: General (journals, incoming documents), Finance, Sales, Purchasing, Inventory, Warehouse Management, Fixed Assets, Planning, Assembly, Manufacturing, Project Management, Service Management, Relationship Management (CRM), Human Resources, Local functionality; plus administration (users/permissions, environments, telemetry), extension development (AL), and integration (APIs, Power Platform, Shopify connector).

Finance (directly observed):
- Default configuration includes a chart of accounts and standard posting groups that assign default GL posting accounts to customers, vendors, and items.
- Dimensions add analytical segmentation to entries.
- AR/AP management: applying incoming payments, reconciling bank accounts, collecting outstanding balances, paying vendors.
- Multi-company: intercompany transactions, consolidation of GL entries from multiple companies into a virtual consolidated company.
- Period-end: ensure documents/journals posted, close books; inventory cost reconciliation with GL; payroll transaction import into GL.
- Cost accounting / managerial analytics; cash-flow analysis; budgets vs actuals.

Sales (directly observed):
- Sales quote → sales order → shipment → sales invoice; sales orders required for partial shipments and drop shipments; order promising (ATP/CTP) communicates delivery dates.
- Posted invoices correctable before payment; after payment, credit memo / sales return order required.
- Approval workflows can require manager approval for large sales.
- Customer cards, price/discount setup, salespeople, shipment methods.

Purchasing (directly observed):
- Purchase quote → purchase order → receipt → purchase invoice; purchase invoices update inventory levels and AP; purchase costs contribute to financial KPIs.
- OCR service converts vendor PDF invoices into purchase invoices via incoming documents.
- Approval workflows for large purchases; external document numbers (vendor's own numbering) can be made mandatory for posting.

Posting sales documents (directly observed — key evidence):
- "When a sales order is posted, the customer's account, the general ledger, and the item ledger entries are updated."
- Posting creates: G/L entry, customer ledger entry (receivables account), item ledger entries per line, VAT entries, possible discount postings; shipment + invoice documents created (same time or independently; partial quantities via Qty. to Ship / Qty. to Invoice).
- Cannot invoice before shipment (unless direct invoice document).
- Posted documents: only limited fields editable; critical audit-trail fields require reversal/undo posting.

Inventory (directly observed):
- Item cards (Inventory type) vs catalog (non-stock) items; item ledger entries; increases/decreases posted directly or via purchase/sales documents; transfers between locations.
- Inventory reconciliation: item value entries; inventory costs automatically posted to inventory account, adjustment account, and COGS account in the GL; cost adjustment for outbound sales.
- BOMs (kits/assembly), item categories/attributes, physical inventory counting (documents or journals), reservations, serial/lot/package tracking with tracing, item blocking, responsibility centers.

Manufacturing (directly observed; Premium experience tier):
- Production BOMs define components; routings define operations; work/machine centers model capacity and costs.
- Production orders coordinate material consumption, operation time, output, finished goods.
- Production order statuses: Simulated → Planned → Firm Planned → Released → Finished; status controls what can be done; Finished orders cannot be changed (reopen once, with restrictions).
- Consumption/output/scrap/operation time recorded in journals or auto-flushed (Manual/Forward/Backward flushing methods); production journal combines consumption+output for a released order.
- Consumption posted as negative item ledger entries; output as positive; time as capacity ledger entries.
- Finished production order costs adjusted and reconciled with GL; WIP account credited by by-products (negative consumption).
- Subcontracting; capacity journal; shop-floor load view.

Permissions (directly observed):
- License entitlement + permission sets (Read/Insert/Modify/Delete/Execute per object; Indirect permission allows action only through another object, e.g., posting codeunit modifies Sales Line).
- Security groups; record-level security filters; company-scoped permission assignment; SUPER set; User Setup (posting time constraints, responsibility centers); delegated admin; change log (audit).

### Oracle NetSuite (evidence layer A for structure/concepts)

Portal positioning: "The #1 Cloud ERP. One unified business management suite, encompassing ERP/Financials, CRM and ecommerce."

Top-level functional sets (directly observed): Account Administration, Globalization, SuiteAnalytics, Country-Specific Features, Employee Management, Marketing/Sales Force Automation/Partners, Projects, Order Management, Accounting, SCM, Support Management, Commerce, SuiteCloud Platform, Mobile, SuiteApps, Non-Profit SuiteApps.

Core concepts (directly observed):
- "All the information you need to keep your business running smoothly is organized and stored in records in NetSuite... Transactions, which are records of financial exchanges, are also included in this section." Records accessed via list pages; duplicate detection; groups.
- Accounting set: General Accounting, Banking, Revenue and Expense Recognition, Taxation, Financial Statements, Fixed Assets Management, Statistical Accounting, Multi-Book Accounting.
- General Accounting: Chart of Accounts Management, Accounting Period Management, General Ledger Impact of Transactions, Journal Entries, Budgets, Account Registers, Accounting-Related Reports, Currency Management, Intelligent Close Manager.
- GL impact: "Transactions in NetSuite include a GL Impact page or subtab"; documented GL impacts for sales transactions, customer transactions, vendor/purchase transactions, COGS, bank transactions; SuiteGL allows customizing line-level GL impact and specialized transaction types.
- Order Management set: Sales Orders and Cash Sales, Order Fulfillment and Shipping, Billing and Invoices, Payment Processing, Customer Returns, Overdue Balances and Collections, Order Management Reports.
- SCM set: Item Record Management, Inventory Management (Basic/Advanced/Consigned, Smart Count, Quality Management), Manufacturing (Assembly Items, Assembly Work Orders, WIP, Routing, Advanced BOM, Outsourced Manufacturing, Engineering Change Order, Available To Build, Manufacturing Scheduler), Vendors/Purchasing/Receiving, Warehouse Management.

### SAP S/4HANA Cloud Public Edition (evidence layer A for positioning; layer B/C only beyond that)

Product page (directly observed):
- "A modular ERP solution... across your finance, supply chain, HR, and sales business processes."
- FAQ: "supports hundreds of business processes across finance, supply chain, project and service management, and HR—including order-to-cash, procure-to-pay, record-to-report, ideation-to-market, service excellence, and hire-to-retire processes."
- FAQ on traditional ERP: "Traditional ERP systems focused on financial accounting, invoice verification, and inventory management. They integrate business processes... typically implemented on-premises." ECC described as modular architecture where "businesses can select the specific modules that meet their needs."
- Deployment: public and private cloud editions; subscription; industry best practices preconfigured; localization "more than 1,000 local versions"; extensibility via SAP BTP / Integration Suite; customer story describing a two-tier ERP model (private cloud for one region, public cloud for another).
- GROW finance page (directly observed): unified order-to-cash, procure-to-pay, record-to-report; record-to-close aggregating "general ledger and subledgers for full multilevel transparency"; integrated spend management connected to logistics and finance; treasury/cash/liquidity; role-based access and segregation-of-duty enforcement; embedded compliance/localized statutory reports; built-in localizations across 60 countries.

### Odoo (evidence layer A for structure only; degraded)

- Official documentation source repo (17.0) organizes applications into: essentials, finance, general, hr, inventory_and_mrp, marketing, productivity, sales, services, studio, websites.
- inventory_and_mrp ("Supply Chain") comprises: inventory, manufacturing, purchase, barcode, quality, maintenance, plm, repairs.
- No operational page content could be fetched (site 403; raw file timeouts). No detailed Odoo claims are made in this research beyond the packaging/structure observation: ERP capability delivered as individually installable apps over a shared core.

## Cross-product Comparison

| Dimension | Business Central | NetSuite | SAP S/4HANA Cloud | Odoo |
|---|---|---|---|---|
| Shared transactional core | Yes — one database; posting updates GL + subledgers + item ledger simultaneously | Yes — records + transactions on one platform; every transaction has a GL Impact | Yes — "integrate business processes"; record-to-close aggregates GL + subledgers | Yes — apps share one core (structure-level evidence) |
| Operational documents | Quote/order/shipment/invoice; PO/receipt/invoice; credit memos | Sales orders, fulfillment, billing, vendor/purchase transactions | Order-to-cash, procure-to-pay named as unified processes | Sales/purchase/inventory/manufacturing apps |
| Automatic financial posting | Explicit: sales order posting → G/L entry + customer ledger + item ledger + VAT | Explicit: GL Impact page/subtab on transactions; SuiteGL customization | Implied by record-to-report/close positioning | Implied by shared core (not directly observed) |
| Inventory + costing | Item ledger entries; value entries auto-posted to inventory/adjustment/COGS accounts | Inventory Management (basic/advanced/consigned); COGS GL impact documented | Supply chain processes incl. logistics | Inventory app |
| Production | Production BOM, routing, work centers, production order status machine, consumption/output/capacity postings, WIP costing | Assembly items/work orders, WIP, routing, BOM, outsourced manufacturing, ECO | Supply chain incl. production (positioning level) | Manufacturing app |
| Planning | Planning worksheet, MPS/MRP, forecasts, order promising (ATP/CTP) | Available To Build, Manufacturing Scheduler, Supply 360 | (positioning level) | (not observed) |
| AR/AP + cash | Customer/vendor ledger entries, payment application, bank reconciliation | Customer/vendor transactions, payment processing, collections | Receivables/payables agents, bank connectivity | Finance app |
| Period close | Period-end tasks, closing fiscal periods, inventory cost reconciliation | Accounting Period Management, Intelligent Close Manager | Financial Closing capability / record-to-close | (not observed) |
| Multi-company | Companies, intercompany, consolidation | Subsidiaries (One World), Multi-Book Accounting | Multi-entity reporting, consolidation | Multi-company (not directly observed) |
| Permissions | License entitlement + permission sets + security filters + company scoping | (role-based access implied by suite; not directly observed in fetched pages) | Role-based access + segregation of duties (positioning) | (not observed) |
| Approval workflows | Sales/purchase approval workflows | (not directly observed in fetched pages) | Automated approvals in procure-to-pay (positioning) | (not observed) |
| Localization | Local functionality per country | Country-Specific Features, Globalization | 1,000+ local versions; 60-country built-in localizations | (not observed) |
| Packaging philosophy | Functional areas in one product; experience tiers (Essential/Premium); extensions via AppSource | Suite: ERP/Financials + CRM + ecommerce; SuiteApps add-ons | Modular ERP; public/private editions; BTP extensions | Installable apps over shared core |
| Adjacent functions included | CRM-lite (Relationship Mgmt), HR-lite, Service, Projects, Fixed Assets | CRM, ecommerce, HR (Employee Management), Projects, Support | HR, project/service mgmt (positioning) | HR, websites, marketing, services apps |

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately minimal)

An ERP is recognizable only if all of the following hold:

1. **Shared transactional data core** — the organization's business transactions from different functions are recorded in one system of record (not separate applications synchronized afterward).
2. **Operational business documents as native transactional units** — sales, purchasing, inventory movement (and where in scope, production) activity is recorded as documents/transactions inside the system.
3. **Automatic financial posting** — posting an operational document generates the corresponding financial entries (general ledger + relevant subledgers such as receivables, payables, inventory) without separate re-entry; operational activity and accounting are one integrated record.
4. **Multi-function coverage on that core** — the same core serves at least finance plus the trade/operations functions (sales, purchasing, inventory; production where the business makes things).

Removal tests:
- Remove the shared core (keep the functions as separate apps with sync) → best-of-breed stack, not an ERP.
- Remove automatic posting (keep operational documents but accounting elsewhere) → operational suite + accounting software, not an ERP.
- Remove operational documents (keep only the ledger) → accounting software.
- Remove multi-function coverage → point solution (inventory system, purchasing system).

### L1 — Common Mature Structure (very common, not definitional)

- General ledger with chart of accounts, accounting periods, journals; financial statements.
- AR/AP subledgers (customer/vendor ledger entries), payment application, bank reconciliation, collections.
- Master data: customer, vendor, item/material records with pricing/discount and tax configuration.
- Sales document chain: quote → order → shipment → invoice → credit memo/return; partial shipments; drop shipment; order promising.
- Purchase document chain: quote → order → receipt → invoice → return; vendor invoice intake (incl. OCR in some products).
- Inventory: item ledger, valuation/costing posting to GL inventory/COGS accounts, transfers, physical count, locations, serial/lot tracking.
- Production (where in scope): BOM, routing/work centers, production order lifecycle, consumption/output posting, WIP costing, subcontracting.
- Supply planning: demand → planned supply orders (MRP-style); order promising.
- Approval workflows on documents.
- Reporting/analytics: financial statements, operational reports, dashboards, ad-hoc analysis.
- Roles/permissions scoped by function and company; audit trail/change log; posting controls.
- Multi-company/multi-entity, intercompany, consolidation, multi-currency.
- Period-end close machinery.
- Integration surfaces: APIs, electronic documents, commerce/connector ecosystems.
- Adjacent functions commonly bundled: CRM-lite, HR-lite, service, projects, fixed assets.

### L2 — Variant / Optional Structure

- Deployment: on-premises, public cloud, private cloud, hybrid; two-tier ERP strategies.
- Customer tier: SMB editions vs enterprise editions (scope, governance depth, implementation method).
- Packaging: all-in-one suite vs modular apps vs module licensing; experience/edition tiers gating features (e.g., manufacturing gated behind a premium tier in one sampled product).
- Industry editions/verticals (manufacturing, agribusiness, food, retail, services) — separate directory leaves exist for some.
- Localization packs (tax, e-invoicing, statutory reporting) per country.
- Customization/extension platforms: low-code customization, scripting, add-on marketplaces.
- Embedded AI assistants over finance/operations processes (current-era feature).
- Depth of adjacent functions (full CRM vs CRM-lite; payroll vs HR-lite; ecommerce native vs connector).

### L3 — Vendor-specific (kept out of final document; examples only)

- Business Central: posting groups, dimensions, Role Centers, Essential/Premium experiences, AL/AppSource extension model, incoming-document OCR service, Company Hub for accountants, indirect-permission mechanics.
- NetSuite: subsidiaries/One World, Multi-Book Accounting, SuiteGL, SuiteApps, SuiteAnalytics Workbook, saved searches, Smart Count.
- SAP: public/private edition split, SAP Activate implementation framework, BTP/Integration Suite extension platform, Joule AI assistants, RISE/GROW commercial packaging, two-tier ERP customer patterns.
- Odoo: app-install packaging, Studio customization, community/enterprise editions.

## Rejected Findings

- "ERP = accounting software plus extras" — rejected: the defining direction is the opposite; operational documents are native and accounting is the posting target. Accounting-only products lack the operational document chains.
- "ERP must include manufacturing" — rejected: service and trading businesses run ERPs without production modules; production is L1/L2 (in-scope variant), not definitional.
- "ERP must be cloud / real-time / AI" — rejected as era-specific; historical on-premises, batch-posting ERPs (and current regional products) still fit the Type. The §24-style historical check holds: mainframe-era and regional ERPs satisfy the L0 structure.
- "ERP = CRM + finance + inventory bundle" — rejected: bundles of separate apps with sync are explicitly not the defining structure; the shared core with single-event posting is.
- "Real-time analytics is definitional" — rejected: it is a modern implementation property (one vendor's FAQ contrasts it with traditional ERP); the Type predates it.
- "Every ERP includes HR/payroll" — rejected: HR appears as lite modules or is absent/delegated to dedicated HR systems; treat as L2 depth-of-breadth variation.

## Boundary Findings

- **vs Accounting Software**: accounting software's center is the ledger with AR/AP subledgers; an ERP's center is the operational document chains that post into that ledger. Remove sales orders/purchase orders/inventory movements/production orders and you have accounting software. (Directory also contains General Ledger System, Invoicing, AP/AR automation as separate leaves — adjacent, narrower.)
- **vs Inventory Management System / WMS**: inventory management in an ERP is valuation-and-quantity record keeping tied to posting; a WMS's center is physical warehouse execution (bins, waves, picks, device-directed work). A WMS can run without a ledger; ERP inventory cannot.
- **vs MES**: production orders in an ERP plan and cost production and post consumption/output; an MES's center is real-time shop-floor execution and control (machine signals, dispatching, quality at the line). Boundary is execution depth.
- **vs CRM**: ERP may include a CRM-lite (contacts, segments); a CRM's center is the customer relationship pipeline (leads/opportunities/activities), not document posting. NetSuite bundles full CRM; BC has Relationship Management; still distinct Types.
- **vs HRIS/HCM**: ERP HR modules are typically lite (employee records, absence); dedicated HRIS/payroll Types remain separate.
- **vs Business Management Suite (directory leaf)**: market products described as "business management suite" (NetSuite's own tagline) are functionally ERPs. Suspected alias/umbrella — flagged in Boundary Issues rather than silently merged.
- **vs Manufacturing ERP / Agribusiness ERP (directory leaves)**: industry editions of this same Type; treated as Variants here.
- **vs Supply Chain Planning / APS / Demand Planning**: planning inside ERP is replenishment-level (MRP-style); dedicated planning Types center on optimization/forecasting depth.
- **vs Procurement / P2P platforms**: purchasing inside ERP is document-and-posting centric; dedicated procurement Types center on sourcing, supplier management, and spend processes that may integrate to the ERP.

## Uncertainties

- SAP operational detail (organizational structure, posting mechanics) could not be verified from fetched sources; SAP is used only for positioning/process vocabulary. Any SAP-specific mechanism named in the final document is avoided.
- Odoo operational behavior (posting model, permissions) not observed; Odoo contributes packaging-philosophy evidence only.
- NetSuite role/permission detail not directly observed in fetched pages (role-based access is implied by suite administration but not documented here); permission claims in the final document rest on Business Central (direct) and SAP positioning (SoD), phrased accordingly.
- Exact feature gating (which functions sit in which edition/tier) varies by product and plan; the final document states this as variation, not as a rule.
- The precise historical boundary of "ERP" vs "MRP II" (1980s–90s) is not researched from primary sources; the document avoids making historical claims beyond "the Type predates current cloud/AI implementations."

## Final Synthesis

The ERP Application Type is best modeled as an **integrated business back office on a shared transactional core**: the organization records its operational activity (selling, buying, moving stock, making goods) as documents in one system, and each posted document simultaneously produces the financial record — ledger entries, receivables/payables, inventory value — so that operations and accounting are one continuously reconciled system of record. Around this defining core, mature products add the standard document chains (order-to-cash, procure-to-pay), inventory costing, production where relevant, planning, close machinery, multi-company/multi-currency, permissions and audit, reporting, and integration surfaces. Deployment, tier, packaging (suite vs apps vs modules), industry editions, localization, and the depth of adjacent functions (CRM/HR/ecommerce) are variants, not definitions. The boundary against accounting software is the operational document layer; against WMS/MES it is execution depth; against CRM/HRIS it is which relationship (customer-facing vs workforce) is the center; against "business management suite" it is likely nothing — probable alias.
