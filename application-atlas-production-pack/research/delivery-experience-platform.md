# Research Notes — Delivery Experience Platform

Slug: delivery-experience-platform
Directory placement: §05.08 Fulfillment (Commerce, Retail & Marketplace)
Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

## Research Goal

Understand what a "Delivery Experience Platform" really is as an Application Type: what objects exist inside it, who operates it, who is served by it, how the post-purchase delivery phase is actually managed, and where its boundaries sit against the dense §18 delivery cluster (courier management, last-mile, shipment visibility, delivery scheduling, proof of delivery) and the §05 commerce siblings (returns, order management, fulfillment).

## Initial Boundary

Hypothesis before research: this leaf sits in the e-commerce fulfillment family, not the transportation family. The likely center is the brand/retailer-side, customer-facing post-purchase layer — branded order tracking, proactive delivery communication, delivery exception handling — as opposed to the execution-oriented §18 types. The market label candidates: "post-purchase platform" (AfterShip, parcelLab), "Delivery Experience Management" (Narvar's heritage positioning), "delivery experience" (parcelLab's own navigation), "Intelligent e-Commerce Logistics" (project44's product family).

Nearest neighbors flagged up front:

- Shipment Visibility Platform (§18, unprocessed) — same tracking surface, different audience?
- Last-mile Delivery Platform (§18, unprocessed) — execution vs communication
- Delivery Scheduling Platform (§18, processed) — when-structure vs experience presentation
- Returns Management Platform (§05.09, unprocessed) — returns modules appear inside every sampled product
- Order Management System (§05.07, unprocessed) — order lifecycle ownership
- Parcel Management Platform (§18, unprocessed) — pre-purchase shipping execution vs post-purchase communication
- Customer Communication Management (§07) — generic outbound comms vs delivery-domain comms

## Research Questions

1. What is the unit of record — the order, the shipment, the parcel, the delivery?
2. Where does the delivery data come from (carriers, commerce platforms, fulfillment systems) and how is it normalized?
3. Who is the served audience: the brand's logistics team, or the brand's end customers?
4. What surfaces exist (consumer-facing vs operator-facing)?
5. Is proactive communication definitional or common?
6. How are delivery exceptions detected and resolved, and where does claims management sit?
7. How far does the category extend (pre-purchase promises, returns, protection, marketing) before it becomes other Types?
8. What distinguishes this Type from shipment visibility when one vendor (project44) ships both?

## Representative Products

| Product | Positioning (own words) | Segment / geography | Evidence quality |
|---|---|---|---|
| Narvar | "Intelligent Personalization 'Beyond Buy'" — post-purchase platform; heritage claim to "Delivery Experience Management" | Enterprise retail, US-founded, global | Strong (root + /track product pages, Layer A) |
| AfterShip | "Make every post-purchase moment count" — post-purchase suite | SMB → enterprise (GMV-tiered), global, API-first | Strong (root + /tracking product page + pricing tiers, Layer A) |
| parcelLab | "The post-purchase platform built for retailers, from delivery to returns" — "Post-Purchase Experience Software" | Enterprise retail, EU-founded (Munich), global | Strong (root + /enhance-delivery-experience page, Layer A) |
| project44 | "Decision Intelligence Platform" (Movement) — supply-chain visibility platform with an "Intelligent e-Commerce Logistics" family | Enterprise shippers/LSPs, global | Strong (root page; eCommerce family = straddle case, Layer A) |
| Route | "Post-Purchase Platform. Protection, Tracking, Returns" | SMB/mid-market D2C, US, consumer-app pole | Unreachable — root and help center JS-rendered, 3 fetch attempts failed; no claims made |

Selection rationale: category-defining enterprise vendor that coined the "delivery experience" framing (Narvar), API-first tier-spanning suite (AfterShip), European enterprise pole with the strongest "delivery experience" self-labeling (parcelLab), and the visibility-giant straddle case that ships both ops-facing visibility and consumer-facing delivery experience under one roof (project44). Route would have covered the consumer-app + shipping-protection pole; documented as a limitation instead.

## Sources

All fetched 2026-09-08:

- https://www.narvar.com/ (root; product set Promise/Secure/Track/Notify/Assist/Shield; journey stages; team solutions)
- https://www.narvar.com/track (Track product page; FAQ)
- https://www.aftership.com/ (root; post-purchase suite; solutions by industry)
- https://www.aftership.com/tracking (Tracking product page; carrier network; status model; pricing tiers; FAQ)
- https://www.parcellab.com/en/ (root; platform pillars; roles; use cases)
- https://parcellab.com/enhance-delivery-experience/ (delivery-experience product page; feature blocks; FAQ; G2 reviews)
- https://www.project44.com/ (root; platform families incl. eCommerce Logistics: Last Mile Resolution, Last Mile Insights, Consumer Visibility, Predictive Delivery Dates)
- https://www.route.com/ and https://help.route.com/ — unreachable (JS-rendered, empty content), 3 attempts

Evidence layers used below: A = directly observed on the cited official page; B = cross-product commonality across the sample; C = canonical inference from comparison and boundary reasoning.

## Product Observations

### Narvar (Layer A)

- Positioning: post-purchase platform "Beyond Buy"; "THE #1 PLATFORM FOR Intelligent Personalization"; 1,500+ brands, 1,000+ carriers; AI engine "IRIS" trained on consumer interactions.
- Product set: **Promise** (AI delivery date estimates, pre-purchase), **Secure** (delivery protection), **Track** (personalized tracking pages), **Shield** (returns & exchanges management), **Notify** (proactive communication), **Assist** (delivery claim management with fraud prevention).
- Journey stages named on the site: Pre-Purchase (product page, cart, checkout) → Delivery (anticipation, in-transit, exception) → Post-Delivery (delivered, delivery issue, returns & exchanges, delivery & return fraud).
- Teams addressed: Ecommerce & Digital, Customer Care, Supply Chain & Logistics, Fraud & Risk.
- Track page specifics: contextual branded tracking pages customized by shipment status and locale; post-purchase marketing with dynamic product recommendations; proactive SMS order updates to opted-in consumers; shipment performance monitoring ("investigate delivery exceptions"); embed tracking-page modules (EDD, marketing assets, recommendations) into any page of the retailer's website; self-serve track page editor; "resolve in-flight delivery exceptions … whether that's with a reorder or a refund"; Track app embedded in service platforms (Salesforce Service Cloud, Gladly, Zendesk) for support reps.
- FAQ claims: consumers check tracking ~3–4 times per order; WISMO reduction ("up to a 40% drop in support tickets" phrasing appears in FAQ); "Instead of sending customers to carrier sites, it keeps them in your ecosystem."
- Stated metrics (marketing): 50% decrease in call center costs; +10% conversion; 3.2x tracking page visits per order.

### AfterShip (Layer A)

- Positioning: "Make every post-purchase moment count"; post-purchase suite: Tracking, Returns, Shipping, AI EDD, Warranty, Order Edits, Protection, Parser, Green; plus a Channel Growth suite (TikTok Shop) and Marketing suite. 20,000+ brands; 1,600+ carriers; 70 platform integrations.
- Tracking product page: "Proactive shipment tracking that delights your customers, reduces WISMO tickets, and optimizes your delivery performance."
- Carrier data layer: 1,600+ carriers, direct connections "no credentials required", webhook (instant) + API updates ("around 60 min. or less"), automatic delivery-status standardization, AI carrier auto-detection when tracking number/carrier mismatch, AI data standardization; published normalized status model ("standardized 7 main- and 33 sub-statuses").
- Consumer-facing layer: branded tracking pages on the brand's own domain (custom CSS, multiple branded pages per brand/market/campaign), configurable notifications (email/SMS on sub-status change or EDD shift, automated flows with templates), Apple Wallet order tracking, multi-language support, AI product recommendations on pages and notifications.
- Operator layer: order & shipment tracking dashboard (filter, track, view, resolve exceptions); order fulfillment reporting (shipment counts, processing times, transit times, exceptions, on-time rates); customer engagement reporting (tracking page visits, CTR, shipping reviews); data lake up to 3 years.
- Suite extensions: Returns (branded returns page, exchange-first flows, rule-based automation), Warranty, Protection (shipping protection with claim management portal), AI EDD (predictive delivery dates), Order Edits (self-serve order changes for shoppers).
- Consumer app: "AfterShip for Shoppers" — free consumer package-tracking app.
- Pricing tiers by GMV: Essentials (<$1M), Premium ($1M–$10M), Enterprise (>$10M) — the same core (branded page + notifications + dashboard) ships at the lowest tier.
- Stated metrics (marketing): 95% delivery date accuracy; 65% fewer WISMO tickets; 3.2x views per order on branded tracking page.

### parcelLab (Layer A)

- Positioning: "The post-purchase platform built for retailers, from delivery to returns. Delivery tracking, branded messages and journeys, returns, exchanges, refunds, fraud, checkout promise and AI — connected in one platform." Platform pillars: Convert (checkout delivery promises), Engage ("Enhance delivery experience"), Retain (returns), Insights, AI Agents (WISMO/R agent). 550+ carrier integrations.
- "Enhance delivery experience" page (the leaf's namesake language): "Take control of your delivery experience."
  - **Track and communicate**: end-to-end visibility for all orders with real-time tracking, split-shipment management, performance monitoring across warehousing, delivery, returns, repairs, claims — centralized dashboard; proactive notifications across email, SMS, app push, chatbots; embedded tracking experiences across channels (marketplace, dropship, ship-from-store, BOPIS, offline store purchases).
  - **Branded tracking portal**: customizable tracking page embedded on the retailer's website or app via JavaScript snippet; detailed order summaries including split shipments.
  - **Personalized journeys**: trigger personalized updates, promotions, alerts based on real-time order status, carrier updates, customer actions.
  - **Targeted campaigns**: customer segmentation; upsell/cross-sell embedded in emails, in-app notifications, tracking pages.
  - **Predict delivery delays**: AI delay prediction ("Trending Late", "pL Promise" named in FAQ); custom delay thresholds by region/carrier/priority; predictions refine at every tracking checkpoint.
  - **Streamline claims management**: claims data and investigation reports in one place; self-service portal for customers to report lost/damaged parcels.
  - **Resolve customer inquiries**: agents get real-time order details, tracking updates, delivery statuses in one place; integrations with Salesforce, Zendesk, Gorgias.
- Roles addressed: eCommerce, Operations & Logistics, Customer Service, Customer Experience, Marketing.
- FAQ: delivery exceptions detected and flagged in real time → proactive notifications; analytics on delivery success rates, notification engagement, carrier performance; fully customizable tracking page.
- G2 review (MediaMarkt): "We had difficulty in unifying the messages that our customers receive from more than 6 different carriers, thanks to parcelLab we've managed to unify the communication to our customers both the content and the design."

### project44 (Layer A)

- Positioning: "Decision Intelligence Platform" (Movement) for the supply chain; product families: Intelligent Transportation Management (TMS), Intelligent Shipment & Inventory Visibility, Intelligent Yard Management, **Intelligent e-Commerce Logistics**.
- eCommerce Logistics family description: "Improve delivery experience with visibility, exception management, and insights." Sub-products: **Last Mile Resolution** (final-mile delivery exception management), **Last Mile Insights** (network-wide insights), **Consumer Visibility** (post-purchase consumer visibility), **Predictive Delivery Dates** (pre-purchase delivery dates).
- The rest of the platform is ops-facing freight visibility (ocean/OTR/air/rail/ports), TMS, yard management, AI agents for exception resolution — i.e., the delivery-experience surface is one family inside a much broader supply-chain platform.
- Sectors: shippers, LSPs; industries: automotive, chemical, F&B, manufacturing, life sciences, retail.

## Cross-product Comparison

| Dimension | Narvar | AfterShip | parcelLab | project44 (eCommerce family) | Layer |
|---|---|---|---|---|---|
| Unit of record | order/shipment journey (delivery → post-delivery stages) | order + shipment (tracking numbers, split shipments) | order + parcels (split shipments explicit) | shipment/order in last-mile network | B |
| Delivery data source | 1,000+ carriers | 1,600+ carriers, direct connections, webhooks | 550+ carriers | carrier network (282K carriers claimed platform-wide) | B |
| Status normalization | implied (status-customized pages) | explicit: standardized main + sub-statuses, AI standardization | real-time exception flagging | exception detection | B |
| Consumer-facing surface | branded tracking pages, locale/status variants, embeddable modules | branded tracking pages on own domain, Apple Wallet, consumer app | branded tracking portal embedded via JS snippet, order summaries | Consumer Visibility (post-purchase consumer visibility) | B |
| Proactive communication | Notify product; SMS to opted-in consumers | configurable email/SMS notifications on status/EDD change | email, SMS, app push, chatbots | proactive customer communications | B |
| Exception management | in-flight exception resolution (reorder/refund); Assist claims | resolve exceptions in dashboard; AI standardization for WISMO | delay prediction, claims management, inquiry resolution | Last Mile Resolution | B |
| Service-team integration | Track app in Salesforce/Gladly/Zendesk | Zendesk/Gorgias integrations | Salesforce/Zendesk/Gorgias agent view | — (not observed at this level) | B |
| Analytics | shipment performance monitoring; engagement | fulfillment + engagement reporting, data lake | delivery success rates, carrier performance, engagement benchmarks | Last Mile Insights | B |
| Marketing on the surface | product recommendations, campaigns | AI product recommendations | personalized journeys, targeted campaigns | — | B |
| Pre-purchase promise | Promise (AI EDD) | AI EDD | Convert (checkout promise) | Predictive Delivery Dates | B |
| Returns | Shield (returns & exchanges) | Returns product | Retain (returns/exchanges/refunds) | — | B |
| Protection/claims | Secure + Assist | Protection + Warranty | claims management | — | B (3/4) |
| Order edits (self-serve) | — | Order Edits | — | — | A, single product |
| Consumer tracking app | — | AfterShip app | — | — | A, single product |
| Tenant | brand/retailer | brand/retailer (+3PL/marketplace solutions) | brand/retailer | shipper/LSP (eCommerce family serves retail) | B |

## Canonical Model

### L0 — Defining Invariant (deliberately small)

1. **The delivery journey of record for the brand's customer orders** — the platform maintains, per order and per shipment (including split shipments), a live delivery state assembled from carrier/fulfillment event feeds and normalized into a coherent status model. Without it there is no delivery data to present or communicate — the product collapses into a generic messaging tool or a bare tracking-number link.
2. **The consumer-facing delivery experience surface under the brand's identity** — the brand presents that delivery state to the end shopper on brand-owned surfaces, the branded tracking page/portal being the signature form (embedded in the brand's site/app, replacing the carrier's own tracking page as the destination). Without it, the product is an internal logistics visibility tool (shipment-visibility territory); without brand ownership, it is just the carrier's page.
3. **Proactive delivery communication to the customer** — the platform pushes milestone and exception updates to the shopper (email/SMS/push) rather than waiting for the customer to check. Without it, the product regresses to the pull-only "track your order" page — the thin ancestor form.

Jointly-held is load-bearing: (1) alone = carrier tracking API / parcel-management data layer; (2) without (1) = static branded page with no live delivery data; (3) without (1) = generic customer-communication tool; (2)+(3) without (1) = communications skin with no delivery model; (1)+(2) without (3) = pull-only tracker (ancestor); (1)+(3) without (2) = push-only shipping notifications.

Historical / market-sample check: the 2000s-era retailer "order status / track your order" page plus shipping-confirmation emails satisfies all three legs in thin form — the retailer's page presented order/carrier delivery state under the brand's identity (leg 2), shipping emails proactively announced the shipment (leg 3), and the order record carried delivery state (leg 1). What is era-current — carrier-network scale (hundreds to thousands of integrations), normalized cross-carrier status taxonomies, AI delay prediction, marketing on the tracking surface, returns initiation, protection products — is deliberately NOT in the core. The definition does not depend on the modern SaaS post-purchase suite pattern.

### L1 — Common Mature Structure

- Multi-carrier event-ingestion network (hundreds–thousands of carrier integrations) with a normalized cross-carrier status model; carrier auto-detection; webhook/API delivery of events
- Commerce-platform / OMS integration binding orders to shipments; split-shipment handling; multi-channel fulfillment contexts (marketplace, dropship, ship-from-store, BOPIS)
- Exception detection and resolution: delay prediction, exception flagging, claims management (lost/damaged), reship/refund resolution paths
- Delivery performance analytics (on-time rates, transit times, exceptions by carrier/lane) and engagement analytics (tracking-page visits, CTR, revenue attribution)
- Service-team enablement: order/tracking context surfaced inside helpdesk tools (Zendesk, Salesforce, Gorgias); WISMO/WISMR deflection as the measured outcome
- Marketing on the delivery surface: product recommendations, campaigns, promotions embedded in tracking pages and notifications
- Returns/exchanges initiation and management as a suite module (overlaps the Returns Management Type)
- Pre-purchase delivery promises / estimated delivery dates at checkout (Narvar Promise, AfterShip AI EDD, parcelLab Convert, project44 Predictive Delivery Dates — 4/4)
- Shipping protection / delivery claims products (3/4)
- Multi-language, locale-based page/notification variants; multi-brand/multi-org management at enterprise tier
- Consumer-facing tracking app (brand-agnostic) as an adjacent surface (AfterShip; Route per market position, unverified)

### L2 — Variant / Optional Structure

- Packaging pole: standalone post-purchase suite (AfterShip, parcelLab, Narvar) vs delivery-experience family inside a supply-chain visibility/decision platform (project44)
- Customer-tier pole: self-serve SMB (AfterShip Essentials tier ships the core) vs enterprise (Narvar, parcelLab, project44)
- Consumer-app pole: brand-agnostic consumer tracking app + package protection (Route-class; unverified this pass)
- Geographic pole: US-founded (Narvar, AfterShip) vs EU-founded (parcelLab); regional carrier coverage as differentiator
- Returns depth: initiation-only vs full returns/exchange management with fraud screening
- AI posture: delay prediction, AI agents resolving WISMO/WISMR inquiries (era-current)
- Fulfillment-context breadth: pure parcel e-commerce vs marketplace/3PL tenancy (AfterShip marketplace & logistics solutions)

### L3 — Vendor-specific (kept out of the final document)

- Narvar: product names Promise/Secure/Track/Notify/Assist/Shield; IRIS AI engine; "74B+ interactions / 2B packages annually"; specific customer-story metrics (50% call-center cost decrease, 3.2x visits, +10% conversion)
- AfterShip: published status taxonomy ("7 main- and 33 sub-statuses"); "around 60 min or less" API update latency; 99.99%+ uptime claim; GMV-tiered pricing ($9/$59/custom); UPU Consultative Committee membership claim; Apple Wallet order tracking; "AfterShip for Shoppers" app
- parcelLab: "Trending Late" and "pL Promise" AI feature names; "detect 90% of delivery delays" claim; 550+ carrier count; "under four weeks" carrier onboarding; PPX Maturity Curve framework
- project44: Movement platform; "3.7T data points / 700M+ events daily"; Mo AI analyst; Agentic Workflow Manager; IDC/G2 placements

## Vendor-specific Findings

See L3. Single-product findings that must not generalize: self-serve order edits (AfterShip Order Edits); consumer tracking app (AfterShip; Route by market position only); Apple Wallet order tracking (AfterShip); claims-fraud scoring as a distinct product (Narvar Assist); marketplace/3PL tenancy solutions (AfterShip).

## Rejected Findings (considered and rejected as core)

- **Pre-purchase delivery promises (EDD) as definitional**: present in 4/4 samples, but it is checkout-conversion machinery upstream of the purchase; the Type is defined by the post-purchase delivery experience. A platform without EDD (the historical ancestor; the AfterShip Essentials core) remains fully recognizable. Held as a common extension.
- **Returns management as definitional**: present in 3/3 pure-play samples as a suite module, but the Returns Management Platform is its own directory Type (§05.09); the delivery-experience center is the delivery journey, not the return authorization lifecycle.
- **Shipping protection / package claims insurance as definitional**: 3/4 samples; a monetization extension tied to delivery failures, not the experience machinery itself.
- **Marketing/recommendations on tracking pages as definitional**: very common (3/4 + Narvar), but a delivery-experience platform without marketing surfaces still satisfies the core; marketing is the "monetize the attention" layer.
- **AI delay prediction as definitional**: era-current capability; the exception loop existed before prediction (reactive exception flagging).
- **"Platform = carrier network marketplace" reading**: the carrier network is infrastructure feeding the experience layer; no sampled product is a demand marketplace for delivery capacity.
- **WISMO deflection as definitional**: it is the measured *outcome* the category sells, not a structure inside the system.

## Boundary Findings

| Neighboring Type | Relationship | Distinction (the "remove-what" test) |
|---|---|---|
| Shipment Visibility Platform (§18, unprocessed) | closest surface overlap; live straddle vendor | project44 ships both under one roof: Visibility (ops-facing freight visibility across ocean/OTR/air/rail for the shipper's logistics team) vs eCommerce Logistics (consumer-facing post-purchase delivery experience). The seam is the served audience + the surface: visibility serves logistics operations watching freight in its network on ops consoles; delivery experience serves the brand's end customers watching their own orders on brand-owned surfaces with proactive customer comms. Remove the consumer-facing surface + customer comms → shipment visibility; add them → delivery experience. Feature presence (tracking) is explicitly NOT the seam. JOINT REVIEW flagged for shipment-visibility-platform. |
| Last-mile Delivery Platform (§18, unprocessed) | adjacent, frequent co-selling | Last-mile platforms orchestrate execution (carrier selection, dispatch, driver apps, routing); delivery experience manages the communication/presentation of delivery to the customer and holds no execution machinery. Remove the customer-experience layer → last-mile territory; remove execution orchestration → delivery experience. Consistent with the courier pass's tenant-identity seam: this leaf is shipper/brand-side and experience-facing, not operator-business or dispatch-facing. |
| Delivery Scheduling Platform (§18, processed) | upstream neighbor | DISCHARGES that pass's prediction from this side: confirmed — scheduling owns the when-structure (offered times, windows, commitments, availability rules); delivery experience owns the post-purchase presentation and communication of delivery state. Notifications about committed windows overlap, but the experience platform does not define schedulable times or manage the schedule. |
| Returns Management Platform (§05.09, unprocessed) | suite-module overlap | Every pure-play sample ships returns as a first-class module (Narvar Shield, AfterShip Returns, parcelLab Retain). The seam: returns management centers the return authorization/processing lifecycle (eligibility, RMA, disposition, refund/exchange); delivery experience centers the outbound delivery journey, with returns as the post-delivery extension. Remove returns → delivery experience intact; remove the delivery-experience layer → returns platform intact. JOINT REVIEW flagged for returns-management-platform. |
| Order Management System (§05.07, unprocessed) | upstream data consumer | OMS owns the order lifecycle and fulfillment orchestration; delivery experience consumes order/fulfillment data (via integrations) and owns the customer-facing delivery presentation and communication. Remove order orchestration → delivery experience intact. |
| Parcel Management Platform (§18, unprocessed) | pre-purchase vs post-purchase | Parcel management is shipper-side multi-carrier shipping execution (rates, labels, manifesting) before handoff; delivery experience is post-handoff communication and presentation. The courier pass recorded this boundary at moderate confidence; this pass corroborates the phase split (pre-purchase execution vs post-purchase experience) from the experience side. |
| Customer Communication Management (§07) | generic vs domain-specific | CCM is generic outbound customer-communication infrastructure (statements, notices, any domain); delivery experience is delivery-domain-specific — its data model (shipments, carriers, milestones, exceptions) and its surfaces (tracking pages) do not exist in CCM. Remove the delivery data model → generic CCM. |
| E-commerce Fulfillment Management / Order Fulfillment Platform (§05.08 siblings, unprocessed) | same family, different phase | Fulfillment owns warehouse/3PL execution (pick/pack/ship, inventory movement); delivery experience owns the post-handoff customer journey. Phase seam: inside-the-building vs after-the-handoff. |
| Customer Service Platform (§07, processed) | consumer of its data, partner surface | Service platforms own the case/ticket operation; delivery experience feeds agents order/tracking context (embeds in Zendesk/Salesforce/Gorgias) and deflects WISMO before tickets exist. Remove the case operation → delivery experience intact. |
| Food Delivery Marketplace / On-demand Delivery (§18/§26) | different object | Those types dispatch couriers for near-now orders; delivery experience presides over parcel-carrier delivery of e-commerce orders. Different fulfillment model, different urgency semantics. |

## Uncertainties

1. **Consumer-app + protection pole unverified**: Route (the clearest consumer-app + package-protection representative) could not be fetched (root + help center JS-rendered, 3 attempts). The pole is characterized only via AfterShip's shopper app and market position. No Route-specific claims are made anywhere.
2. **Help-center-level operational detail**: for Narvar and parcelLab, evidence is product-page level; exact notification trigger sets, editor capabilities, and API mechanics were not verified at help-center depth. Assertions kept at the level the vendors' own pages state.
3. **Label ↔ population mapping**: the market uses "post-purchase platform" (AfterShip, parcelLab), "delivery experience" (parcelLab navigation, Narvar heritage), and "eCommerce logistics" (project44) for the same population. The directory label "Delivery Experience Platform" matches the Narvar/parcelLab lineage; confidence moderate that the label covers the whole population including visibility-embedded families.
4. **SMB self-serve pole**: documented via AfterShip's pricing tiers at product-page level; no SMB-native vendor (e.g., Shopify-app-only trackers) directly sampled.
5. **Regional products** (APAC, LATAM post-purchase vendors) not sampled; assertions kept conceptual.
6. **project44's Consumer Visibility depth**: the family is confirmed to exist and its sub-products are named, but consumer-surface mechanics (page editor, notification flows) were not verifiable at help-center level; treated as the straddle case, not as a pure-play observation.

## Final Synthesis

A Delivery Experience Platform is the **brand-side system that turns the post-purchase delivery phase into a managed customer experience**. Its defining core is three jointly-held structures: (1) the delivery journey of record — live, normalized delivery state per order/shipment assembled from carrier and fulfillment event feeds; (2) the consumer-facing delivery experience surface — the branded tracking page/portal on brand-owned properties that replaces the carrier's page as the customer's destination; (3) proactive delivery communication — milestone and exception updates pushed to the shopper across channels. Around that spine, mature products add the carrier-ingestion network at scale, exception detection/resolution and claims, delivery and engagement analytics, service-team embeds, marketing on the tracking surface, returns initiation, pre-purchase delivery promises, and shipping protection — the capability stack that makes the core operational and monetizable. The Type sits deliberately between the execution-oriented §18 delivery family (it holds no execution machinery) and the commerce back-office (it owns no order lifecycle): remove the consumer-facing surface and proactive comms and it becomes shipment visibility; remove the delivery data model and it becomes generic customer communication; remove the brand ownership and it becomes the carrier's tracking page.
