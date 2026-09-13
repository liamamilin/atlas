# Research Notes — Dealer / Distributor Commerce Portal

## Research Goal

Understand what a Dealer / Distributor Commerce Portal actually is as an Application Type: who operates it, who uses it, what objects exist inside it, how ordering works, and how it differs from the adjacent B2B commerce Types (B2B E-commerce Platform, Wholesale Commerce Platform) and from PRM / Supplier Portal / Customer Portal.

## Initial Boundary

- Leaf sits under 05.17 B2B Commerce, alongside "B2B E-commerce Platform" and "Wholesale Commerce Platform".
- Hypothesis: the distinguishing binding is the **channel relationship** — the portal is operated by an upstream seller (manufacturer/brand/supplier) for its own reselling partners (dealers/distributors), not for end consumers and not as generic commerce machinery.
- Nearest confusions: B2B E-commerce Platform (generic machinery), Wholesale Commerce Platform (wholesaler's own trade storefront), PRM (partner lifecycle, not commerce), Supplier Portal (reverse direction), Customer Portal (generic self-service).

## Research Questions

1. Who operates the portal and who logs in?
2. What is the account model — one login per partner business? Multiple users per partner?
3. How does partner-specific pricing/catalog visibility work?
4. Is order approval by the seller part of the defining flow, or a variant?
5. What non-ordering content lives in the portal (invoices, statements, RMA, marketing assets, programs)?
6. What is the relationship to the seller's back office (ERP/QuickBooks/SAP)?
7. Where is the line to B2B E-commerce Platform and Wholesale Commerce Platform?

## Representative Products

| Product | Segment / philosophy | Evidence |
|---|---|---|
| Orderwerks | SMB manufacturer dealer portal, QuickBooks-centric, approval-first | A (full official page fetch) |
| OroCommerce | Enterprise open-source B2B commerce platform with dealer-portal packaging | A (official pages surfaced via search; direct fetch blocked 403) |
| Corevist | SAP-integrated dealer/distributor portal for manufacturers | A (official page surfaced via search) |
| DistributorOS | Brand-side wholesale/distributor portal for ecommerce brands | A (official pricing page surfaced via search) |

Sample spans: SMB QuickBooks manufacturer → enterprise SAP manufacturer → enterprise open-source platform → ecommerce-brand wholesale. Different packaging poles (standalone portal vs platform module).

## Sources

- Orderwerks — https://www.orderwerks.com/solutions/dealer-portal (fetched 2026-09-10)
- OroCommerce — https://oroinc.com/b2b-ecommerce/b2b-dealer-portal-solution , https://oroinc.com/b2b-ecommerce/b2b-portal-solution-for-ecommerce , https://oroinc.com/b2b-ecommerce/b2b-ecommerce-for-distributors , https://oroinc.com/b2b-ecommerce/features (surfaced via search 2026-09-10; direct fetch returned 403)
- Corevist — https://www.corevist.com/dealer-distributor-portal-for-manufacturers (surfaced via search 2026-09-10)
- DistributorOS — https://mydistributoros.com/pricing (surfaced via search 2026-09-10)
- XoroONE B2B Portal — https://xorosoft.com/xoroone/b2b-portal (surfaced via search 2026-09-10; used as corroborating observation only)
- WizCommerce B2B Ordering Portal — https://wizcommerce.com/product/b2b-ordering-portal (surfaced via search 2026-09-10; corroborating)

## Product Observations

### Orderwerks (Layer A — direct fetch)

- Operator = manufacturer; users = its dealers ("manufacturers who sell through dealer networks": firearms, equipment, auto parts, building materials, industrial).
- Each dealer has "their own account on your branded portal" — white-labeled with the manufacturer's logo/colors.
- Dealer sees "their products, their pricing, their order history" — customer-specific pricing (contract rates, volume tiers, product-specific discounts) applied automatically at login.
- Dealer-specific catalogs: "You control which products each dealer can see and order" (tiered dealer levels, regional products, exclusive lines).
- Ordering flow: dealer logs in → browses catalog → cart → submit; one-click reorder from history; desktop/tablet/phone.
- **Order approval workflow**: "Orders don't bypass you. Review incoming orders, verify inventory, check dealer account status. Make adjustments if needed" — then approve. Seller-side control is a headline feature ("You review before shipping").
- Approved orders push to QuickBooks as invoices; products/inventory sync from QuickBooks. The portal is an ordering layer over the seller's back office, not the books of record.
- Real-time inventory visibility before ordering; 24/7 self-service replacing phone/email/fax ordering.
- Sales-rep / on-behalf ordering exists ("You can still enter orders on their behalf — same system, same workflow").
- Dealer-activity visibility for the manufacturer ("which dealers are growing… who hasn't ordered").

### OroCommerce (Layer A via search-surfaced official pages)

- Dealer portal positioned as a solution of the B2B commerce platform: "brings your entire product catalog, order history, and customer relationships into one place" for a manufacturer's dealer network.
- Role- and region-based catalog visibility: "Each user (dealer, distributor, branch, or service team) sees only the products, prices, and resources meant for their company and user role."
- Custom catalogs and pricing per region/partner; automated price and inventory feeds from ERP.
- Channel-program content in the same portal: "Integrated Marketing Resource Library: Publish campaigns, sell sheets, and promotional assets in the same portal dealers use to order"; "In-Portal Programs: Promotions, rebates, and marketing campaigns are created, managed, and tracked within the portal."
- Order tracking and self-service RMA; buyer self-service for order history, invoices, packing slips, tracking; invoicing and payment in-portal (OroPay); RFQ/negotiation workflows.
- Corporate account hierarchies and permissions; multi-org/multi-site; workflow engine for order approvals; ERP integrations (SAP, Dynamics, NetSuite).
- Also markets a generic "B2B portal" and "distributor" solution — the dealer portal is a channel-shaped packaging of the same commerce core.

### Corevist (Layer A via search-surfaced official page)

- "Built for manufacturers who sell to dealers & distributors" — SAP ERP real-time integration covering the order-to-cash cycle.
- Robust product catalogs; real-time price & inventory from SAP; personalized online ordering ("End phone, fax, & email ordering"); SKU-based order entry, order upload, self-service payments.
- Positioning: "The best of B2B ecommerce & customer portals" — portal + commerce fused, with the manufacturer's ERP as the source of truth.

### DistributorOS (Layer A via search-surfaced official page)

- Operator = an ecommerce brand running a wholesale channel ("You own the distributor relationship").
- Branded distributor portal with pending applications & approvals (partner onboarding as a portal function), license & tax doc review.
- Per-distributor pricing tiers; distributor team accounts (multiple buyers per distributor); in-app messaging with distributors.
- Wholesale-tier pricing & quantity breaks; MOQs per product and per order; one-click reorder; custom orders placed on behalf of a distributor; real-time order pipeline.
- Syncs to Shopify/WooCommerce (the brand's commerce backend) — again an ordering layer over an existing commerce/ops system.

### Corroborating observations (XoroONE, WizCommerce — Layer A via search)

- Same structure: login-gated portal, customer/partner-specific catalog and pricing (contract/tier/volume), real-time inventory, self-service invoices/statements/tracking/RMA, account management, ERP sync, rep/dealer on-behalf ordering, buyer-approval on signup.

## Cross-product Comparison

| Structure | Orderwerks | OroCommerce | Corevist | DistributorOS |
|---|---|---|---|---|
| Seller-operated portal for channel partners | ✓ | ✓ | ✓ | ✓ |
| Login-gated per-partner account | ✓ | ✓ | ✓ | ✓ |
| Partner-specific pricing | ✓ | ✓ | ✓ | ✓ |
| Partner-specific catalog visibility | ✓ | ✓ (role/region) | ✓ (personalized) | ✓ (per-distributor) |
| Partner-initiated ordering into seller's pipeline | ✓ | ✓ | ✓ | ✓ |
| Order history / reorder / tracking | ✓ | ✓ | ✓ | ✓ |
| Seller-side order approval before fulfillment | ✓ headline | ✓ (workflow engine, configurable) | not stated | ✓ (application approval; order pipeline) |
| Back-office integration as source of truth | QuickBooks | ERP (multi) | SAP | Shopify/WooCommerce |
| Self-service documents (invoices/statements/RMA) | order history only | ✓ | payments | — |
| Channel programs (rebates/promos/marketing assets) | — | ✓ | — | — |
| Partner onboarding/approval in portal | account setup by seller | — | — | ✓ |
| White-labeling / seller branding | ✓ | ✓ | ✓ | ✓ |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **Seller-operated partner-facing venue** — the portal is operated by the upstream seller (manufacturer/brand/supplier) for its own distribution channel; the logged-in customer is a reselling partner business (dealer/distributor), not an end consumer. Remove → generic B2B e-commerce storefront.
2. **Per-partner account with partner-specific commercial terms** — each partner is a persistent account whose pricing (contract/tier/volume) and catalog visibility are configured per partner; what a partner sees and pays is a function of its account, not of a public price list. Remove → anonymous wholesale storefront.
3. **Partner-initiated ordering into the seller's fulfillment pipeline** — the partner composes and submits orders against the seller's catalog (browse/cart/reorder), and the order enters the seller's order/ERP pipeline for fulfillment. Remove → marketing resource site or PRM with no commerce.

Binding: the three exist together because the partner relationship is the unit around which the whole portal is configured.

### L1 — Common Mature Structure

- Order history, status tracking, one-click reorder
- Real-time inventory visibility
- Seller branding / white-labeling
- Back-office integration (ERP/accounting) as the system of record behind the portal
- Multiple users per partner account; roles within the partner
- On-behalf ordering by the seller's reps
- Self-service documents: invoices, statements, payments, RMA

### L2 — Variant / Optional

- Seller-side order approval gate before fulfillment (headline in approval-first products; configurable/absent in straight-through products)
- Partner onboarding/approval workflow inside the portal (applications, license/tax doc review)
- Channel programs: rebates, promotions, marketing resource library, co-op/MDF
- Territory/region-based catalog and pricing
- Quote/RFQ negotiation flows
- Net-terms/credit visibility, integrated payments
- EDI and other parallel order channels normalized into the same pipeline

### L3 — Vendor-specific

- Orderwerks: QuickBooks Desktop/Online invoice push; SMS order entry; regulated-industry compliance (FFL/FastBound, NY SLA)
- OroCommerce: OroPay, AI SmartOrder (PDF→draft order), multi-ERP normalization, GMV-metered licensing
- Corevist: NetWeaver-certified SAP integration, S/4HANA migration path
- DistributorOS: Shopify/WooCommerce two-way sync, Stripe payments, per-store plans

## Vendor-specific Findings

See L3 above; none promoted to the canonical core.

## Boundary Findings

- **vs B2B E-commerce Platform**: the platform is generic machinery for any B2B selling (buyer may be any business); the dealer/distributor portal is a channel-shaped deployment where the buyer is an intermediary in the seller's distribution chain and the partner relationship (per-partner terms, territories, programs, onboarding) is the organizing unit. Remove the channel-relationship binding and the portal is just a B2B storefront — the decisive test. Note: several sampled products are B2B commerce platforms *packaging* a dealer-portal solution — the Type is the deployment shape, not the engine.
- **vs Wholesale Commerce Platform**: close seam. The wholesale platform serves a wholesaler's trade customers generally; the dealer/distributor portal emphasizes a managed distribution network (partner onboarding, territories, channel programs, reseller identity). Boundary issue recorded for STATUS.md.
- **vs PRM**: PRM's center is partner lifecycle/enablement (recruiting, training, deal reg, MDF); the commerce portal's center is ordering. Channel programs may appear in both — overlap zone, not identity.
- **vs Supplier Portal**: reverse direction (buying organization's vendors vs selling organization's resellers).
- **vs Customer Portal**: generic self-service account surface; lacks the reseller-partner binding and partner-specific commercial terms as the organizing unit.
- **Historical check**: pre-portal era dealer ordering ran on phone/fax/EDI price contracts; early-2000s dealer portals were login-gated catalogs with per-dealer price lists. All satisfy the L0 triple — the definition does not depend on modern ERP sync, white-labeling, or channel-program modules.

## Uncertainties

- Whether the market treats "dealer portal" and "wholesale portal" as one category with different vocabulary (several vendors use both terms for the same product). Recorded as a boundary issue rather than resolved unilaterally.
- Direct fetch of OroCommerce pages blocked (403); observations rest on search-surfaced official page content — treated as Layer A but with slightly reduced confidence on fine detail.
- No evidence sampled on dealer portals in automotive OEM style (parts ordering with VIN/fitment) — possible industry variant not covered by the sample.

## Final Synthesis

The Dealer / Distributor Commerce Portal is the upstream seller's login-gated ordering portal for its own channel partners. Its defining core is the triple: seller-operated partner-facing venue + per-partner account with partner-specific commercial terms + partner-initiated ordering into the seller's fulfillment pipeline. Everything else — approval gates, channel programs, marketing libraries, onboarding workflows, payments, EDI normalization — is common, variant, or vendor-specific structure layered on that triple.
