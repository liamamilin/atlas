# Research Notes — B2B E-commerce Platform

Research date: 2026-09-06

## Research Goal

Understand what a B2B E-commerce Platform actually is as an Application Type: what objects exist inside it, how business buying differs structurally from consumer online shopping, who operates it and who uses it, and where its boundary lies against consumer e-commerce platforms, wholesale platforms, dealer portals, marketplaces, and procurement systems.

## Initial Boundary

Working hypothesis before research:

- Core use: a seller business (manufacturer, brand, wholesaler, distributor) runs an online ordering channel aimed at business customers, so that buyers order without a sales rep transcribing the order.
- Likely structural differences vs consumer e-commerce: buying party is a company, not an anonymous individual; pricing is negotiated/contractual; payment on credit terms and POs; large catalogs; repeat ordering.
- Nearest Types: E-commerce Platform (B2C), Online Store Builder, Wholesale Commerce Platform (sibling leaf), Dealer/Distributor Commerce Portal (sibling leaf), Online Marketplace, CPQ, Order Management System, Procurement Platform (buyer side), Customer Portal.
- Unknowns: how B2B-native products differ structurally from consumer platforms with B2B modules; whether "payment on terms" is defining or merely common; role of quotes and buyer-side approvals; integration depth (ERP, EDI, punchout).

## Research Questions

1. What is the buying party in the system's model? (individual customer vs organization with multiple buyer users)
2. How is pricing structured? (single public price vs price lists/shared catalogs/negotiated levels)
3. What settlement paths exist beyond anonymous card checkout? (payment on account, credit lines, payment terms, invoicing, tax exemption)
4. What objects support the buying workflow? (cart, quick order, requisition/shopping lists, quotes/RFQ, purchase orders, approval workflows)
5. What does the seller side manage? (companies, price lists, quotes, orders, credit, sales reps)
6. What roles exist on both sides, and how do permissions work inside the buying organization?
7. How does the platform relate to the seller's back office (ERP) and other systems?
8. How do products position B2B relative to B2C (same instance vs separate experiences)?
9. What are the market segments and product philosophies (B2B-native vs consumer-platform-plus-module vs ERP-embedded)?
10. Where is the boundary against consumer e-commerce, wholesale, dealer portals, marketplaces, CPQ, procurement?

## Representative Products

| Product | Philosophy / segment | Why selected |
|---|---|---|
| Shopify Plus B2B | consumer SaaS store-builder lineage, B2B as a layer on the consumer platform (SMB→enterprise) | dominant mainstream platform; shows B2B bolted onto a consumer core |
| Adobe Commerce (Magento) B2B | enterprise/mid-market suite; B2B as an integrated module in a commerce suite | deepest documented classic B2B feature set (companies, shared catalogs, quotes, POs) |
| BigCommerce B2B Edition | SaaS platform with a dedicated B2B add-on edition and separate Buyer Portal | shows the add-on-edition packaging and buyer-portal pattern |
| Sana Commerce Cloud | B2B-first platform embedded in the seller's ERP (SAP / Microsoft Dynamics) | shows the ERP-integrated philosophy; no local pricing/inventory copy |

Fallback candidates: OroCommerce (B2B-native open source) — official docs unreachable during research (see Sources / limitations), therefore not used as evidence; SAP Commerce Cloud — not attempted after sample already spanned four philosophies (stop conditions reached).

## Sources

Tier 1 (official operational / developer documentation):

- Adobe Experience League — "Introduction to Adobe Commerce B2B" — https://experienceleague.adobe.com/en/docs/commerce-admin/b2b/introduction (retrieved 2026-09-06)
- Shopify Dev — "Apps and B2B" — https://shopify.dev/docs/apps/build/b2b (retrieved 2026-09-06)
- BigCommerce Dev Docs — "B2B Edition for Stencil Themes (Legacy Experience)" — https://docs.bigcommerce.com/developer/docs/b2b-edition/storefront/stencil.md (retrieved 2026-09-06; includes references to the BigCommerce Help Center B2B Edition overview)

Tier 2 (official product pages; marketing-grade, used for positioning and FAQ-level operational claims):

- Sana Commerce — official site incl. platform pages and FAQ — https://www.sana-commerce.com/ (retrieved 2026-09-06). FAQ claims used: direct ERP integration (SAP ECC/S4, Dynamics 365 F&SC/BC), live pricing/stock/terms from ERP, order types (standard, repeat, quote-to-order, split, against customer-specific catalogs/contracts/credit limits), self-service (order history, invoices, shipment status, account balances), approval workflows per ERP config, EDI mentioned for medical-supplies industry.

Access failures (limitation recorded per evidence rules; no model-memory compensation):

- help.shopify.com/en/manual/b2b → HTTP 403 (×1; not retried) — substituted with shopify.dev official B2B guide (Tier 1).
- doc.orocommerce.com → transport error ×2 (index.html and book/) — OroCommerce abandoned entirely; no OroCommerce-specific claims made anywhere.
- support.bigcommerce.com → script-rendered ("CSS Error") ×1 — substituted with official BigCommerce developer docs (.md endpoint).
- commercehelp.sana-commerce.com → transport error ×2 — Sana evidence rests on its official site Tier-2 pages/FAQ; assertion strength reduced accordingly.

Consequences: no precise numeric claims (credit limits, plan gating details, approval-rule thresholds, price-list counts) asserted anywhere; order-type and integration claims for Sana kept at the level its own FAQ states; all single-product findings marked product-specific.

## Product A — Shopify (B2B / Shopify Plus)

### Key observations (Layer A — official dev docs)

- Framing: "merchants sell directly to other companies. When a company is the customer, there are often multiple contacts and locations, pre-negotiated payment terms, and catalogs to manage."
- Object model: `Company` = "the business entity that makes a B2B purchase. A company contains locations and contacts." `CompanyLocation` = "a single location or branch"; holds billing/shipping addresses; catalogs, tax exemptions, and payment terms are assigned to it. `CompanyContact` = "a person that acts on behalf of the company", associated with a retail customer record.
- Catalogs are assigned to company locations: "exclusive product selections and negotiated pricing levels to contacts at different company locations."
- Draft orders can be created by the merchant and sent to company contacts for review, approval and invoicing.
- Buyer logs in "with an account that's attached to a company" to select products, review draft orders, complete checkout; an order/transaction is then created.
- Orders/draft orders can be associated with company, location, or contact; B2B orders can be imported from operations outside the platform.
- Product-specific: B2B features are plan-gated (Plus); purchase options like subscriptions are not supported for B2B; catalogs only assignable at location level.

### Interpretation

Consumer platform core (products, carts, checkout, customers) is retained; the B2B layer inserts an organization entity between the platform and the buyer person, and re-binds catalogs/pricing/terms to that organization (down to branch level).

## Product B — Adobe Commerce B2B

### Key observations (Layer A — official admin docs)

- "Unlike the standard business-to-consumer model, integrated B2B features are designed for sellers (merchants) whose customers are companies… the transaction takes place between your business and theirs." Supports both B2B and B2C in one store.
- Company account = "a key entity within B2B on which all other features are in some way dependent." Joins multiple buyers of one company into one account; company administrator builds structure (divisions, subdivisions, users) and assigns roles/permissions controlling "ordering, quoting, purchasing, access to company credit information or profile."
- Company management (merchant admin side): companies managed from Admin; **company hierarchy** with parent/subsidiaries managed as a group (product-specific depth).
- Shared catalogs = "pricing levels that allow setting custom prices per product for different companies"; requires company accounts.
- Pay on Account: purchases on a company credit line; merchant allocates credit, manages credit settings and reimbursement.
- Quick Order: for logged-in customers who know SKU/name, reduces ordering to a few steps.
- Negotiable Quotes: buyer initiates from cart (seller can also initiate); both sides negotiate (add items, update quantities, request/apply discounts) "until they reach an agreement"; quotes grid maintains history.
- Purchase orders: when activated for a company, **all** orders become POs; users with permission create/edit/delete their own POs and those of subordinate users; approval rules apply depending on role and order.
- Requisition lists: save frequently ordered items, multiple lists per purpose (vendor, buyer, team), add to cart directly.
- Merchant configuration decides which B2B capabilities are available (payment methods, pricing levels, quoting, requisition lists).

### Interpretation

The full classic B2B structure: organization accounts with internal roles → account-scoped catalogs/pricing → quote negotiation → PO + buyer-side approvals → credit settlement. Seller admin is a second, substantial operating surface.

## Product C — BigCommerce B2B Edition

### Key observations (Layer A — official dev docs)

- B2B Edition = "BigCommerce's Enterprise business-to-business (B2B) solution" layered on a BigCommerce store, delivered as an add-on app.
- Feature list: client business management with **company accounts**; predefined B2B customer roles with storefront permissions; shared shopping lists and "buy again"; sales representative enablement tools; quote management; invoice and payment management; Quick Order Pad.
- Company-account onboarding can run through a "Trade Professional Application" (company signup request) — storefront API allows anonymous company creation.
- Two experiences: legacy Stencil storefront experience vs a separate **Buyer Portal** (deployed React app; channel-aware; supports separate B2B and B2C storefronts, region/brand-specific B2B experiences).
- API surface spans orders, companies, addresses, payments, sales reps, company users; integration with third-party tools (e.g., Salesforce, Zendesk).
- Product-specific: B3 container/theme customization system; edition distributed via BigCommerce representative.

### Interpretation

Same structural core as Adobe, packaged as an add-on edition with a distinct buyer-facing portal; sales-rep enablement is explicit; company signup can be buyer-initiated application rather than seller-provisioned.

## Product D — Sana Commerce Cloud

### Key observations (Layer A/B — official site pages + FAQ; Tier 2)

- Positioning: "B2B commerce platform" for manufacturers, machinery, automotive & multi-parts, distribution, construction, electronics, medical supplies, wholesale, chemicals.
- Philosophy: direct ERP integration — "reads pricing, inventory, customer and order data from the ERP itself rather than through middleware or a separate database" (SAP ECC/S4HANA, Dynamics 365 F&SC, Dynamics 365 BC).
- Customer-specific pricing, discounts, contract terms "read live from the ERP each time a buyer logs in"; negotiated price = displayed price; payment terms (e.g., Net 60) applied at checkout.
- Order types buyers can place: standard orders, repeat orders, quote-to-order requests, split orders, orders against customer-specific catalogs, contracts and credit limits.
- Self-service portal: order history, invoices, shipment status, account balances.
- Approval workflows and multi-address shipping "supported where they exist in your ERP configuration" — i.e., rules live in the ERP, platform surfaces them.
- EDI mentioned as a sibling data channel (medical supplies industry page: "shared data across web, phone & EDI").
- Platform modules around the storefront: PIM, OMS, payments, self-service portal, analytics, Commerce Console.

### Interpretation

The ERP-integrated philosophy: the platform deliberately keeps no independent pricing/inventory/customer master; the buying account and its terms ARE the ERP customer record surfaced online. Same buyer-side objects (quotes, approvals, catalogs, credit limits) but sourced from the back office.

## Cross-product Comparison

| Dimension | Shopify B2B | Adobe Commerce B2B | BigCommerce B2B Edition | Sana Commerce Cloud |
|---|---|---|---|---|
| Buying party | Company (business entity) with contacts | Company account with structured users/divisions | Company accounts with buyer roles | ERP customer record (company) with buyer users |
| Buyer identity | CompanyContact linked to customer record | Company users with roles/permissions | Predefined B2B roles with storefront permissions | Buyers under customer account |
| Account structure | Company → locations → contacts | Company → divisions/subdivisions/users (+ parent hierarchy) | Company → users | Per ERP customer/hierarchy config |
| Pricing | Catalogs per location, negotiated pricing levels | Shared catalogs = pricing levels per company | Price management via edition features | Customer-specific prices read live from ERP |
| Product selection scoping | Exclusive catalog selections per location | Shared catalogs scope products/prices | Company-scoped catalogs/prices | Customer-specific catalogs per ERP |
| Quotes | — (draft orders as seller-initiated alternative) | Negotiable quotes (buyer or seller initiated, history) | Quote management | Quote-to-order (per ERP) |
| POs / approvals | Draft orders for approval | PO mode + approval rules over subordinate users | Invoice & payment management (approvals in edition) | Approval workflows per ERP config |
| Settlement | Payment terms attached to location; invoicing via draft orders | Pay on Account (company credit line), credit management | Invoice and payment management | Payment terms (e.g., Net 60) at checkout, credit limits |
| Quick order / lists | (via apps) | Quick Order + requisition lists | Quick Order Pad + shared shopping lists, buy again | Repeat orders |
| Sales-rep tools | — (draft orders for contacts) | Seller-initiated quotes | Sales rep enablement tools explicit | Self-service positioned vs "talking to your sales rep"; rep parity of data |
| Seller admin | Merchant admin + apps | Full Admin (companies, quotes grid, credit) | Control panel B2B area + Buyer Portal backend | Commerce Console + ERP as system of record |
| Back-office integration | Import B2B orders (external ops) | Services (catalog service, search, recommendations) | API to CRM/support tools | Native ERP = the integration model |
| B2B/B2C coexistence | Same platform, B2B layer | Explicitly both models in one store | Separate B2B and B2C storefronts (channel-aware portal) | B2B-first (B2C not the focus) |
| Onboarding of companies | Merchant creates company | Merchant creates from Admin | Buyer-initiated Trade Professional Application possible | ERP customer onboarding |
| Tax exemption | Per company location | — (observed) | — (observed) | Per ERP |

Key observation: all four products independently converge on the same structural spine — (1) buying organizations as managed accounts, (2) buyer users acting on the org's behalf with internal roles, (3) account-scoped product selection and pricing, (4) an ordering workflow extended with quote/PO/approval mechanics, (5) settlement through the account (terms/credit/invoice) in addition to card, (6) a substantial seller-side management surface, (7) integration with the seller's back office. Differences are packaging (layer vs module vs edition vs ERP-embedded) and where master data lives.

## Canonical Model (three-layer synthesis)

### L0 — Defining Invariant (minimal)

A B2B E-commerce Platform is a seller-operated commerce platform on which:

1. **Buying organizations are managed accounts.** The seller maintains a registry of customer companies; purchases are made by authenticated buyer users acting on behalf of one of these organizations. Remove this → consumer e-commerce platform.
2. **The commerce core runs against that account.** Seller-published catalog → cart/order → order record, executed within the account relationship. Remove this → customer portal / CRM, not commerce.
3. **Pricing and product availability are mediated by the account relationship.** What a buyer sees (prices, assortment) is determined by the seller-account binding (trade pricing), not by one anonymous public retail price. Remove this (single public anonymous pricing, guest checkout) → consumer store, even if business buyers occasionally shop there.

Everything else is L1/L2. Deliberately NOT in L0: payment on terms (card-only wholesale stores exist and are still recognizably B2B), quotes, POs, approvals, requisition lists, buyer portals, punchout.

### L1 — Common Mature Structure (cross-product, Layer B)

- Buyer roles and permissions inside the company account (who may order, quote, approve, see credit) — Adobe A, BigCommerce A, Sana A
- Per-account / per-segment price lists and catalogs (shared catalogs, location catalogs, customer-specific catalogs) — all four
- Quote/RFQ negotiation between buyer and seller — Adobe A, BigCommerce A, Sana A (Shopify addresses the same need via merchant draft orders — variant mechanism)
- Purchase orders and buyer-side approval chains (incl. orders by subordinate users) — Adobe A, Sana A, BigCommerce A (partial: invoice/payment management)
- Payment on account: credit line, payment terms, invoicing; seller-side credit management — all four
- Quick order / SKU-based ordering, repeat/reorder, requisition & shopping lists — Adobe A, BigCommerce A, Sana A
- Sales-rep enablement / assisted selling — BigCommerce A explicit; Adobe variant (seller-initiated quotes); Shopify variant (draft orders); Sana frames self-service against rep parity
- Substantial seller-side admin surface (company management, quotes, orders, credit) — all four
- Integration into the seller's back office (ERP or equivalent) as the normal operating mode — Sana A (defining philosophy), Adobe/BigCommerce via services/APIs, Shopify via order import/apps
- Tax exemptions bound to the buying account — Shopify A (location-level)

### L2 — Variant / Optional Structure

- Packaging philosophy: B2B-native platform vs B2B module on consumer platform vs add-on edition vs ERP-embedded (all four differ)
- B2C coexistence: one store both models (Adobe explicit) vs separate B2B/B2C storefronts (BigCommerce channel-aware portal) vs B2B-first (Sana)
- Account onboarding direction: seller-provisioned (Adobe, Shopify) vs buyer-initiated application (BigCommerce Trade Professional Application) vs ERP-borne (Sana)
- Org-structure depth: flat company → divisions/subdivisions → multi-company hierarchy (increasing depth, Adobe deepest observed)
- Catalog scoping unit: per location (Shopify) vs per company/customer group (Adobe) vs per ERP customer (Sana)
- Where quoting/buying rules live: platform-native vs ERP-borne (Sana explicitly defers to ERP config)
- EDI as sibling order channel (Sana A, single-product observation → treat as variant, not standard)
- Procurement-system integration (PunchOut/OCI): known market pattern, NOT verified in this sample — not asserted anywhere (see Uncertainties)
- Industry overlays: verticalized catalogs/filters (e.g., automotive make/model filtering — Sana), regulated goods, etc.
- Plan/edition gating of B2B features (Shopify Plus gating — product-specific)

### L3 — Vendor-specific (research notes only)

- Shopify: Company/CompanyLocation/CompanyContact object naming; catalogs only at location level; draft-order-based approval; B2B order import; Plus plan gating; no subscriptions for B2B.
- Adobe: "Shared catalogs", "Pay on Account", company hierarchy (parent/subsidiary group management), quotes grid with communication history, requisition lists per vendor/team framing.
- BigCommerce: B2B Edition add-on packaging, B3 containers/styles/text/lifecycle customization system, legacy Stencil experience vs Buyer Portal (React, Scripts API), Trade Professional Application, storefront API with anonymous company creation.
- Sana: direct ERP reading (no middleware/second database claim), SCI analytics, Commerce Console, industry page framing, Gartner MQ mention.

## Boundary Findings

- **vs E-commerce Platform (B2C) / Online Store Builder** — the most important boundary. Consumer store: buying party is an individual (optionally anonymous/guest), one public price, anonymous card checkout. B2B platform: buying party is an organization account; pricing/assortment is account-mediated; the account carries terms. Structural test: delete the organization-account layer → the product collapses into a consumer store; every sampled vendor treats this layer as what makes it "B2B" (Shopify: "when a company is the customer…"; Adobe: "customers that are companies"). Both poles ship inside single products (Adobe explicitly dual-model), so the boundary is a mode/layer, not a vendor wall.
- **vs Wholesale Commerce Platform (sibling leaf 05.17)** — probable overlap. Wholesale is a commercial relationship (bulk selling to retailers) that is commonly executed ON a B2B e-commerce platform; every wholesale ordering site sampled or known fits the B2B core (org accounts, trade pricing, catalog ordering). Without a dedicated research pass on that leaf, recorded as probable Alias/Variant needing joint review. No taxonomy change made unilaterally.
- **vs Dealer / Distributor Commerce Portal (sibling leaf 05.17)** — same structure with a specific channel relationship (manufacturer→dealer). The dealer portal is plausibly a Variant of this Type (account relationship + contract pricing + ordering are identical in kind); needs joint review with that leaf.
- **vs Online Marketplace / Multi-vendor Marketplace** — marketplace: plurality of third-party sellers, platform mediates between them. B2B e-commerce platform: one seller operates its own channel to its business customers. Different core object (vendor registry vs customer-company registry).
- **vs CPQ** — CPQ centers on configuring complex products into a priced quote; B2B commerce includes quote negotiation as one workflow object but does not center on product configuration. Overlap zone: quote-to-order paths (Sana).
- **vs Procurement Platform (buyer side) / Government Procurement** — procurement is the buyer's sourcing tooling; B2B e-commerce is the seller's selling channel. They interconnect (buyer procurement systems punch into seller catalogs — unverified in this sample, see Uncertainties) but the operating party differs.
- **vs Order Management System / Sales Order Capture** — OMS orchestrates fulfillment of orders after capture; B2B commerce ends its primary flow at the order + settlement record handoff. Sibling leaf "Sales Order Capture" (07) plausibly covers the order-entry slice; boundary recorded for joint awareness.
- **vs Customer Portal** — self-service account views (order history, invoices, balances) exist in both; in B2B e-commerce they are a secondary surface of the commerce flow, in a Customer Portal they are the whole.

Historical / market-sample check (§24): older and simpler market shapes — distributor web shops behind a trade login (single trade price list for all approved accounts, invoice settlement, email/fax replaced by an order form), EDI-era ordering, and manufacturer dealer portals — all satisfy the L0 above (org accounts, account-gated trade pricing, catalog ordering) without quotes, approvals, buyer portals, or per-location catalogs. Those are L1/L2 additions of the modern era. The L0 therefore does not over-fit to the current enterprise implementation pattern.

## Uncertainties

1. PunchOut/procurement-gateway integration is widely associated with B2B commerce in the market, but was not observed in any sampled official source; not asserted anywhere in the final document.
2. Exact approval-rule mechanics (rule dimensions, thresholds) observed only for Adobe at a high level ("approval rules depending on role and order") — no precise rule model asserted.
3. Whether card-only wholesale stores (no terms) are placed inside this Type or form a lightweight variant: market evidence suggests they exist inside the same platforms (B2B layer on card checkout); treated as a variant within the Type, not a separate Type.
4. OroCommerce (B2B-native open source) could not be researched — the B2B-native-vs-module contrast rests on Sana (ERP-embedded) vs the three module/edition platforms; a B2B-native platform would presumably sit between these poles.
5. Relationship of the two sibling leaves (Wholesale Commerce Platform, Dealer/Distributor Commerce Portal) to this Type — flagged for joint review rather than resolved.
6. Whether "B2B E-commerce Platform" and directory sibling "E-commerce Platform" (05.01) should cross-reference as mode-of-one-product — recorded, no taxonomy change.

## Final Synthesis

The B2B E-commerce Platform is the seller-side commerce channel for business buying. Its defining core is: a registry of buying-organization accounts operated by the seller; buyer users acting on behalf of those organizations; the catalog→cart→order commerce core executed inside the account relationship; and pricing/assortment mediated by that relationship rather than by one anonymous public price. Around this core, mature products add a recognizable standard kit: buyer roles, per-account price lists and catalogs, quotes, POs with buyer-side approvals, payment on account/terms/credit, quick order and reorder lists, sales-rep enablement, seller-side company management, and back-office (ERP) integration. Products differ mainly in packaging (B2B-native, module-on-consumer-platform, add-on edition, ERP-embedded) and in where the master data (pricing, stock, terms) lives. The Type sits on a shared product continuum with consumer e-commerce — the same vendors ship both — and the organization-account layer is the structural dividing line.
