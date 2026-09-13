# Research Notes — Recurring Commerce Management

Research date: 2026-09-07
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

## Research Goal

Understand what the Application Type "Recurring Commerce Management" (DIRECTORY 05.16 Subscription Commerce, sibling of "Subscription Commerce Platform") actually is in the real market: the objects it manages, the workflows it runs, its lifecycle and rules, and — critically — whether it is a distinct Type or an alias/umbrella of its sibling leaf.

Terminology note: Recharge's own documentation uses the term "recurring commerce" directly ("Recurring commerce offers the ability for merchants to foresee (to a certain extent) the future orders of their customers" — Customer Delivery Schedule doc). The market term is real and vendor-anchored.

## Initial Boundary

Working hypothesis before research:

- Core use: merchant-side software for selling physical/consumable goods on a repeating schedule — subscription boxes, replenishment (subscribe & save), auto-ship, clubs.
- Users: e-commerce merchants (subscription/DTC brands), their retention/support teams; subscribers via self-service portal.
- Nearest Types:
  - **Subscription Commerce Platform** (sibling leaf, unprocessed) — probable alias/umbrella risk; market products (Recharge, Ordergroove, Skio) self-describe as "subscription platform".
  - **Subscription Billing Platform** (08 Finance) — digital/SaaS recurring billing; invoice/entitlement-centric, no goods fulfillment.
  - **E-commerce Platform** (05.01) — the storefront/checkout substrate this type usually rides on.
  - **Order Management System** (05.07) — per-order, not per-commitment.
  - **Loyalty Program Management** (05.15) — optional bundled module in several products.
- Unknowns: whether sibling leaf = same referent; exact subscription state models; how prepaid/gift/one-time interact with the core cycle.

## Research Questions

1. What are the core objects (subscriber, subscription, line items, orders, charges, addresses)?
2. What is the subscription lifecycle (states, skip/pause/cancel/expiry/dunning semantics)?
3. How does the system derive and execute future recurring orders (queue, charge regeneration, fulfillment handoff)?
4. What can subscribers self-manage (portal action surface), and what do merchants manage (admin surface)?
5. What retention machinery exists (dunning, cancel flows, winbacks, save offers, churn analytics)?
6. What deployment postures exist (storefront-embedded app / headless API / all-in-one host / marketplace)?
7. Where is the boundary vs Subscription Billing Platform, E-commerce Platform, OMS, Loyalty?
8. Does the sibling leaf "Subscription Commerce Platform" have a distinct referent?

## Representative Products

Selection: market representation + documentation depth + different philosophies + different customer tiers.

| Product | Posture | Segment | Why selected |
|---|---|---|---|
| Recharge | Storefront-embedded subscription platform (Shopify-native; custom API for headless) | Mid-market to enterprise consumer brands | Market leader ("powering 71% of subscriptions sold on Shopify stores" — vendor claim); deepest public developer docs |
| Skio | Modern Shopify-native subscription platform, migration-led | Fast-growing CPG / mid-market | Full Tier-1 help center; portal/retention-first philosophy |
| Ordergroove | Enterprise API-first "autonomous subscription platform", everychannel | Enterprise CPG (Clarins, Dollar Shave Club, OLLY) | Enterprise pole; relationship/journey philosophy |
| Cratejoy | All-in-one host + consumer marketplace for subscription box businesses | SMB box creators | All-in-one + marketplace pole; historical box-native anchor |

## Sources

### Recharge (Tier-1 developer docs; .md-fetched)
- https://rechargepayments.com/ (product root) — 2026-09-07
- https://docs.getrecharge.com/docs (Understanding Recharge) — 2026-09-07
- https://docs.getrecharge.com/llms.txt (documentation index) — 2026-09-07
- https://docs.getrecharge.com/docs/glossary.md (Glossary) — 2026-09-07
- https://docs.getrecharge.com/docs/subscriptions.md (Subscriptions resource) — 2026-09-07

### Skio (Tier-1 help center)
- https://skio.com/ (product root) — 2026-09-07
- https://help.skio.com/ (help center home + topic structure) — 2026-09-07
- https://help.skio.com/docs/subscription-management (Subscription Management article, full text) — 2026-09-07
- https://help.skio.com/llms.txt (full article index) — 2026-09-07

### Ordergroove (Tier-2 product pages; Knowledge Center unreachable)
- https://www.ordergroove.com/ (product root) — 2026-09-07
- https://www.ordergroove.com/product/subscriber-experience/ — 2026-09-07
- https://www.ordergroove.com/retain/ — 2026-09-07

### Cratejoy (Tier-2 seller platform pages)
- https://www.cratejoy.com/ (marketplace root) — 2026-09-07
- https://sell.cratejoy.com/ (seller platform root) — 2026-09-07
- https://sell.cratejoy.com/features/ (platform features) — 2026-09-07

### Source-access Limitation
- **Ordergroove Knowledge Center** (ordergroove.zendesk.com) failed 2× (transport error) → abandoned per network rules. Ordergroove evidence is Tier-2 product pages only; Ordergroove-specific mechanics (API internals, admin console detail) are NOT asserted.
- **Cratejoy seller support KB** (support.cratejoy.com) not fetched; Cratejoy evidence is Tier-2 marketing/features pages. Cratejoy is treated as a market-context pole, not a source of precise operational rules.
- Vendor performance claims (Recharge "71% of subscriptions on Shopify", "$1B+/month", "100M subscribers"; Ordergroove case-study lift figures; Skio "5X reduction in cancellations") are marketing claims — recorded as claims, never asserted as facts in the final document.

## Product A — Recharge

### Key observations (evidence layer tagged)

- Positioning: "subscription payments solution... offer subscriptions and recurring billing"; two integration modes: pre-built ecommerce-platform integrations (Shopify) or custom API integration for bespoke stacks. [A]
- **Subscription widget** on the product page displays subscription options/frequencies; shopper chooses recurring vs one-time purchase. [A]
- Core API resources: **Subscriptions** ("represent individual items a customer receives on a recurring basis... the core resources"), **Addresses** (subscriptions tied per address; many subscriptions per address; a customer can have only one subscription of the same product on one address), **Customers**, **Products** ("items tied to a subscription"), **Charges** ("financial transaction linked to the purchase of an item (past or future)... Completed charges have an order associated"), **Orders** ("created after a Charge is successfully processed"), **One-times** (single non-recurring items alongside subscriptions), **Discounts**, **Payments** (RCPM: multiple payment vehicles per customer, linked to addresses), **Checkouts** (Recharge-hosted / self-hosted / third-party options), **Webhooks**, **Async batches** (bulk). [A]
- **Prepaid**: "a single charge results in multiple orders. When a customer purchases a prepaid subscription, Recharge generates queued orders that represent the future remaining orders"; identified by charge_interval_frequency > order_interval_frequency. [A]
- **Customer Delivery Schedule**: merchants can pull a customer's upcoming order info and projected data — "Recurring commerce offers the ability for merchants to foresee (to a certain extent) the future orders of their customers." [A]
- Subscription status values include ACTIVE and CANCELLED (with cancelled_at, cancellation_reason, cancellation_reason_comments; reactivation clears cancellation fields); auto-expire subscriptions possible ("automatically expire after a set number of charges"). [A]
- **Charge regeneration**: every subscription update triggers a charge regeneration; frequency/interval updates remove skips on the upcoming charge and can reschedule it; product/variant swaps update the existing charge in place. [A]
- Customer portal: hosted out-of-the-box ("Affinity" portal — overview page, upsell/retention config, cancel navigation, custom extensions, reschedule options) or fully custom via API/Theme Engine. [A]
- Feature surface from product root: customer portal, churn prevention, upsell & cross-sell, bundles (build-your-own-box), analytics, rewards/referrals (loyalty), concierge SMS support, integrations; verticals incl. meal kits, beauty, food & beverage, pets, digital subscriptions. [A]
- Bundles: one SKU bundling multiple products, "build-your-own-box" experience; as one-time and/or subscription. [A]
- Gift subscriptions exist (gifting widget for Shopify themes). [A]

## Product B — Skio

### Key observations

- Positioning: "subscription platform top Shopify brands graduate to"; portal/retention-first philosophy ("A customer portal so user friendly... manage everything — skips, swaps, gifts, updates — without asking for help"). [A]
- **Merchant dashboard — Subscription Management tab**: subscription cards showing next billing date, status (Active, Paused, Canceled, Failed, 3DS Error, Under Review), frequency + completed order count, order summary (products/quantities/price), delivery method (Shipping / Pickup / Local delivery, editable per subscription), timeline, customer info; search by email/name/phone/subscription ID. [A]
- **Merchant actions on a subscription**: cancel, skip next charge, get now (send next order immediately), set next billing date, edit frequency, pause, merge (combine subscriptions into one billing), split (separate products into different subscriptions), product skip (skip individual items), gift on skip, quantity editing, apply discount, price override (per-subscription), payment management, backup payment methods. [A]
- **Portal link vs Magic link**: portal link = shareable customer portal URL; magic link = log in as the customer to manage on their behalf. [A]
- Portal actions are **merchant-configurable**: which actions customers can self-serve is a setting (Customer Portal settings / CPv3). [A]
- **Analytics suite**: Overview, Products, **Dunning Dashboard**, Forecasting, Cohort Retention, **Cancel Flow Dashboard** (save rates, cancellation reasons), Segments; glossary includes MRR, LTV, AOV, ARG, AOC. Status semantics documented: Active/Failed/Paused/Cancelled; **Entered Dunning / Recovered / Actively Cancelled / Passively Cancelled / Recovered Revenue**. [A]
- **Payment Recovery**: retry logic, Smart Retries, backup payment methods ("fallback when a primary payment method fails... reduce failed charges"); 3DS handling for renewals. [A]
- **Cancel Flows**: configurable flows (splash screen, loyalty/loss-aversion screen), A/B testing of cancel flows, save rates; **Winbacks** (1-click, Klaviyo/Postscript integration). [A]
- **Enrollment**: Plan Picker on product page (Shopify app block), Selling Plans (Shopify concept), prepaid subscriptions (upfront payment, "locking in revenue"), prepaid gift subscriptions, checkout link builder, subscription-only product restriction, first-order discount changing for recurring orders. [A]
- **Journeys**: trigger/condition/action automation (e.g., auto-expand bundles, portal banners, sunset prepaid). Surprise & Delight rules (rewards/discounts/free products at lifecycle moments), Reward Milestones, Streaks, SkioSMS (one-way notifications, two-way SMS subscription management, quiet hours), Quick Actions, Smart Upsell, Checkout Add-on Upsell, Volume discounts, Loyalty (credits/tiers/referrals). [A]
- **Build-a-Box**: static/dynamic/sectioned builders; managing Build-a-Box subscriptions for customers. [A]
- **Auto-Merge Billing**: combines orders before sending to Shopify to reduce shipping costs; **Interval matching and auto-split**; order days & cutoffs for fulfillment timing. [A]
- Bulk operations (price changes, product swaps, deleted-variant swap, add/remove products), data exports, segments, fraud prevention tools, audit logs (Activity/Customer/Subscription), user permissions. [A]
- Migration machinery as a first-class workflow (from WooCommerce/BigCommerce/Magento/custom; every subscriber audited pre-launch). [A]

## Product C — Ordergroove

### Key observations (Tier-2 only — no help-center access)

- Positioning: "Autonomous Subscription Platform"; "The enterprise standard for subscriptions"; "Subscription infrastructure for the AI era". Enterprise client logos incl. Dollar Shave Club, BarkBox, OLLY, Clarins. [A]
- Product pillars: **Acquire** ("turn transactions into lifelong relationships"), **Retain** (churn prevention), **Scale** ("maximize subscriber lifetime value"); experiences: Subscriptions, Bundles & Clubs, Digital Access, Paid Memberships. [A]
- Named modules: Subscriber Experience, A/B Testing, **Flex Incentives**, **Involuntary Churn Suite**, Performance Analytics, Subscription-first Experiences, Frontier AI (agents), Customer Success & Support. [A]
- Subscriber experience: enroll/manage "during every step of their shopping experience from the PDP to the cart"; on-brand portals; subscribers "skip or pause orders, or swap out SKUs for different flavors, colors, and sizes". [A]
- Churn prevention: "Prevent the No. 1 cause of subscriber churn — overstock. Identify subscribers at risk of churn due to oversupply and actively prevent cancellations by prompting them to skip their upcoming order or engaging them with personalized offers." [A]
- Retain page: frictionless subscription management; personalized retention incentives (escalating offers, milestone gifts, **prepaid** — "1-Year Prepaid Subscription... Prepay for 12 shipments"; loyalty integrations); cancellation prevention ("canceling available, but rarely the best choice" — skip/pause/swap/add-on options); **cancel-save offers** ("WAIT! BEFORE YOU LEAVE... Get an extra 15% off") and **winbacks** ("We miss you. Reactivate now & get 15% off... 1-click winbacks"); rotating subscriptions / surprise & delight (option to reveal or hide upcoming shipments). [A]
- **Involuntary Churn Suite**: intelligent payment retries ("Retry American Express with Insufficient funds on the 1st" — Recovery Optimizer), automated subscriber communications (card-expiry warnings), advanced billing analytics ("Recurring Revenue Waterfall": scheduled → failed → recovered → successful revenue). [A]
- Automation: workflow builder ("Workflows that run themselves") with subscription-event triggers ("Recurring Order Placed"), filters, conditional splits, actions (apply gift, swap, skip, change cadence, update subscription), integrations (Klaviyo, OMS, ESP, warehouse); AI agents propose variants tested at 1%/5%/10% traffic. [A]
- Integrations: Shopify, Shopify Plus, BigCommerce, Commercetools, Adobe Commerce, Magento, Salesforce, custom cart; "everychannel infrastructure" (storefronts, retail, voice); MCP layer / GraphQL APIs / webhooks. [A]
- Migration as flagship capability (Dollar Shave Club "99.99% migration success moving millions of subscribers" — vendor claim). [A]

## Product D — Cratejoy

### Key observations (Tier-2 only)

- Positioning: "The Ecommerce Platform for Subscription Box Businesses" — subscription box software + consumer Marketplace + support. [A]
- Two-sided: consumer marketplace (discovery, gift cards, "cancel anytime" badge, purchase protection) + seller platform (Sitebuilder/custom storefront + themes, listing on marketplace, apps). [A]
- Feature surface: **Subscription Box CRM** (customer profiles & history, billing/shipping updates, cancellations & refunds with a few clicks); "Subscribers can manage their subscriptions from their own account" (self-service portal); **skip a renewal** ("keep your subscribers from cancelling by letting them skip a renewal cycle"); subscription options ("manage logistics and fulfillment for your subscription boxes"); subscription KPIs dashboard (**churn, cancellation analytics, conversion funnel, traffic sources, lifetime value**); **cash flow reports on cash or accrual basis**; coupons; shipping- and tax-smart checkout; discounted shipping rates; print shipping labels; shipping exports showing customer variants/gifts/notes/surveys; fulfillment integrations (ShipStation, Pirate Ship); one-time product add-ons ("one-time sales engine"); referral campaigns (dual-incentive, built into checkout/account pages); multi-user logins with role permissions; customizable event emails (welcome, shipping/refund notices, tracking, receipts); PCI Level-1 vault; CSV exports + API. [A]
- Marketplace claims: 4M monthly page views, 30,000+ monthly sales, 2,500+ creators (vendor claims). [A]

## Cross-product Comparison

| Structure / capability | Recharge | Skio | Ordergroove | Cratejoy | Layer |
|---|---|---|---|---|---|
| Subscription = standing commitment record (subscriber × product(s) × frequency × destination) | ✔ ("core resource"; product+address) | ✔ (subscription card; subscriber→subscription→lines) | ✔ ("lifelong relationships") | ✔ (subscriber accounts) | **L0** |
| Derived future order/charge schedule (next charge date; queued orders; forecast) | ✔ (next_charge_scheduled_at; queued orders; Delivery Schedule) | ✔ (next billing date; Forecasting Dashboard) | ✔ (Recurring Order Placed trigger; future shipments) | ✔ ("see months in advance what my actual orders will be" — seller quote; KPI reports) | **L0** |
| Per-cycle execution: charge → order → fulfillment handoff | ✔ (charge→order; webhooks to external systems) | ✔ (orders in Shopify; delivery methods; auto-merge before sending) | ✔ (OMS integration; everychannel) | ✔ (shipping labels; ShipStation/Pirate Ship) | **L0** |
| Commitment lifecycle management (modify schedule/products; skip; pause; cancel; expiry) | ✔ (update status/frequency/swap; auto-expire) | ✔ (skip/pause/cancel/merge/split/get-now) | ✔ (skip/pause/swap/change cadence) | ✔ (skip renewal; cancel/refund) | **L0** |
| Storefront enrollment surface (widget/plan picker: one-time vs subscribe, frequency choice) | ✔ subscription widget | ✔ plan picker / selling plans | ✔ PDP→cart enrollment | ✔ own storefront + marketplace listing | L1 |
| Subscriber self-service portal (skip/pause/swap/cancel/update payment) | ✔ (hosted Affinity or custom) | ✔ (v2/v3, merchant-configurable actions) | ✔ | ✔ | L1 (common implementation of lifecycle mgmt) |
| One-time add-ons alongside subscriptions | ✔ (One-times resource) | ✔ (one-time upsells; add to order) | ✔ ("add to my order") | ✔ (one-time add-ons) | L1 |
| Dunning / payment recovery | ✔ (Failed-adjacent machinery: charge errors; not directly fetched) | ✔ (Payment Recovery, Smart Retries, backup payment methods, Dunning Dashboard) | ✔ (Involuntary Churn Suite, Recovery Optimizer, card-expiry comms) | ✔ (self-service billing updates to reduce loss) | L1 |
| Cancel flows / save offers / winbacks | ✔ (churn prevention pillar; cancel navigation; prevent-cancel config) | ✔ (Cancel Flows + A/B testing + save rates; Winbacks) | ✔ (cancel-save offers, 1-click winbacks, escalating offers) | ✔ (skip-as-alternative framing) | L1 |
| Discounts / subscription pricing incentives | ✔ (Discounts API, discount use cases for churn/LTV) | ✔ (volume discounts, first-order discount, stacking) | ✔ (Flex Incentives) | ✔ (coupons) | L1 |
| Bundles / build-a-box | ✔ (Bundles, build-your-own-box) | ✔ (Build-a-Box static/dynamic/sectioned) | ✔ (Bundles & Clubs) | ✔ (box-native) | L1 |
| Prepaid (one charge → multiple future deliveries) | ✔ (queued orders) | ✔ (prepaid + prepaid gift) | ✔ (prepay for 12 shipments) | — (not observed) | L1 |
| Gift subscriptions | ✔ (gifting widget) | ✔ (prepaid gift; gifting billing semantics) | — (not directly observed) | ✔ (gift cards/gifting surfaces) | L1 |
| Subscription lifecycle analytics (MRR/LTV/churn/cohort/recovery) | ✔ (analytics pillar) | ✔ (full dashboard suite) | ✔ (Performance Analytics, revenue waterfall) | ✔ (churn/cancellation/LTV KPIs, cash-flow reports) | L1 |
| Notifications (order/payment/lifecycle emails & SMS) | ✔ (order emails; concierge SMS; webhooks) | ✔ (email notifications; SkioSMS two-way) | ✔ (automated subscriber communications) | ✔ (event email templates) | L1 |
| Merchant admin: search, per-subscription ops, bulk ops, audit logs | ✔ (merchant portal, Bulk Updater, async batches) | ✔ (subscription cards, bulk ops, audit logs) | ✔ (Subscription Manager) | ✔ (CRM interface, multi-user roles) | L1 |
| Webhooks / API / integration fabric | ✔ | ✔ | ✔ (GraphQL, MCP, webhooks) | ✔ (API, exports) | L1 |
| Loyalty/rewards/referrals module | ✔ (Rewards, Referrals) | ✔ (credits/tiers/referrals) | ✔ (loyalty integrations) | ✔ (referral campaigns) | L2 |
| Automation/journey builders; AI agents | — (partial: Shopify Flow recipes) | ✔ (Journeys; AI-era features) | ✔ (workflow builder; AI agents) | — | L2 |
| Churn-risk detection (overstock prediction) | — | — (implicit via segments) | ✔ (overstock churn prompt) | — | L2 |
| A/B testing of retention machinery | — | ✔ (cancel-flow A/B) | ✔ (product module) | — | L2 |
| Marketplace channel for acquiring subscribers | — | — | — | ✔ (defining Cratejoy posture) | L2 |
| Local delivery/pickup methods | — | ✔ | — | — | L2 |
| Fraud prevention tooling | — | ✔ | — | — | L2 |
| All-in-one host (owns storefront + checkout + subscription engine) | — (custom checkout options) | — | — | ✔ | L2 (deployment posture) |
| Named portals (Affinity), RCPM, Theme Engine; SkioSMS/Streaks/Magic links/Quick Actions/Backup Products/Swap Recommendations; Flex Incentives/Recovery Optimizer/Groove Network/Everychannel/MCP; Cratejoy marketplace referral fees/Sitebuilder/one-time sales engine | ✔ | ✔ | ✔ | ✔ | L3 |

## Canonical Model

### L0 — Defining Invariant (smallest stable structure)

```text
Subscriber commitment record
  (identified customer × specified product(s) × repeating schedule × destination)
  └── Derived recurring order schedule
      (system-projected queue of upcoming charge+order events)
      └── Per-cycle execution
          (each event executed as a real commerce transaction:
           payment charged, order created, handed off for fulfillment)
          └── Managed commitment lifecycle
              (the commitment persists between cycles and its schedule,
               contents and existence can be changed and ended —
               by merchant and/or subscriber)
```

Four properties. Remove any one and the Type stops being recognizable:

- Remove the **commitment record** → one-off e-commerce with a reorder button.
- Remove the **derived schedule** → a plan that never produces future events (no "see months in advance what orders will be").
- Remove **per-cycle execution** → a wishlist/reminder tool, not commerce.
- Remove **lifecycle management** → a fixed installment schedule that cannot respond (skip/pause/swap/cancel); the "management" in the Type's name disappears. Note the object being managed is the *commitment to receive goods*, not debt repayment (installment/layaway differs here).

### L1 — Common Mature Structure (very common; not definitional)

- Storefront enrollment surface (product-page widget / plan picker: one-time vs subscribe & save, frequency options)
- Subscriber self-service portal (skip, pause, swap, reschedule, cancel, update payment/address, add one-time items)
- Dunning & payment recovery (retry logic, backup payment methods, card-expiry communications, recovery analytics)
- Cancel-flow machinery (intervene before cancellation, save offers, cancellation reasons, winbacks)
- Discount/subscription-pricing machinery
- Bundles / build-a-box; one-time add-ons
- Prepaid subscriptions (one charge → multiple future deliveries); gift subscriptions
- Subscription analytics (MRR/LTV/churn/cohort/recovery; forecasting)
- Lifecycle notifications (email/SMS: upcoming order, order confirmations, payment issues)
- Merchant admin (subscription search & per-subscription operations, bulk operations, audit logs, user permissions)
- API/webhooks + storefront-platform integration; fulfillment handoff (order pushed to platform/OMS/carrier tools)

### L2 — Variant / Optional Structure

- Loyalty/rewards/referrals modules
- Automation/journey builders; AI agents for retention operations
- Churn-risk detection (e.g., overstock prediction), A/B testing of retention machinery
- Marketplace channel (Cratejoy pole)
- Local delivery/pickup fulfillment methods; fraud-prevention tooling
- Paid memberships / digital access / clubs as adjacent subscription shapes
- Segment/vertical tuning (meal kits, beauty, coffee, pet, wellness, direct selling)
- Deployment posture: storefront-embedded app (Shopify/BigCommerce/Adobe/Salesforce/custom) vs headless API-first vs all-in-one host

### L3 — Vendor-specific (kept out of final document)

- Recharge: Affinity portal, RCPM payment-method model, Theme Engine, Bulk Updater tool, charge-regeneration mechanics, one-product-per-address rule, subscription_id semantics
- Skio: SkioSMS, Streaks, Magic links, Quick Actions, Journeys naming, Smart Retries, interval matching/auto-split, Backup Products, Swap Recommendations, Auto-Merge Billing, Under Review / 3DS Error state names
- Ordergroove: Autonomous Subscription Platform framing, Groove Network, Everychannel, Flex Incentives, Involuntary Churn Suite, Recovery Optimizer, MCP/GraphQL agent surface, AI-variant deployment percentages
- Cratejoy: marketplace referral fees, Sitebuilder, one-time sales engine, cash-vs-accrual report labels, performance pricing

## Vendor-specific Findings

(All single-product; recorded per evidence rules)

- Recharge: a subscription binds exactly one product to one address ("A subscription can only be linked to one product under a customer's address"); multi-product offerings are modeled as a single bundle product; prepaid identified by charge_interval_frequency > order_interval_frequency; every subscription update triggers charge regeneration; frequency updates remove pending skips.
- Skio: six-status merchant-visible state set (Active/Paused/Canceled/Failed/3DS Error/Under Review) plus dunning states (Entered Dunning/Recovered/Actively Cancelled/Passively Cancelled); merchant "magic link" login-as-customer; auto-merge billing aligns multiple subscriptions into one shipment before pushing to Shopify; permanently canceled subscriptions cannot be reactivated (per FAQ title).
- Ordergroove: overstock named as "No. 1 cause of subscriber churn" with proactive skip prompting; recovery prompt can schedule a retry of a specific card on a specific date ("retry on the 1st").
- Cratejoy: cash-flow reporting on both cash and accrual basis inside the subscription admin; dual-incentive referral campaigns built into checkout/account pages; marketplace with category-based referral fees.

## Boundary Findings

1. **vs Subscription Commerce Platform (sibling leaf, 05.16)** — probable alias/umbrella. All four sampled products self-describe as "subscription platform" and Recharge's docs use "recurring commerce" as the activity name for the same referent. No sampled market product maps to only one of the two labels. **Flag for joint review.** If both leaves are kept, the only defensible seam is emphasis: platform/enablement (enrollment, checkout, integration) vs management/operations (lifecycle, retention, fulfillment ops) — but every sampled product straddles both. This document therefore defines the Type on the shared structure and records the seam rather than inventing a second structure.
2. **vs Subscription Billing Platform (08 Finance)** — sharpest structural seam: this Type's unit is the *recurring goods order* (charge → order → shipment handoff; "Customer delivery schedule"); billing platforms center the *invoice/entitlement/revenue-recognition* relationship (SaaS/access), where nothing physical ships per cycle. Removing the goods-delivery schedule and fulfillment handoff from this Type collapses it into subscription billing. Removing recurring-goods commitments from a billing platform never yields this Type.
3. **vs E-commerce Platform (05.01)** — substrate vs layer: storefront/cart/checkout handle the *transaction*; this Type adds the *standing commitment machinery* the storefront cannot express (future schedule, between-cycle state, dunning over time). A subscription platform that owns the whole storefront (Cratejoy) still shows the same core objects, proving the recurring layer is the Type, not the storefront.
4. **vs Order Management System (05.07)** — unit of record: OMS manages individual orders across channels; this Type manages the *commitment* that generates future orders and holds between-cycle state (skip/pause). The recurring commitment is not an OMS object.
5. **vs Loyalty Program Management (05.15)** — loyalty appears as an embedded optional module in three of four sampled products; loyalty's managed object is points/earn/redeem, not the recurring order. Optional, not definitional.
6. **vs Marketing Automation (06)** — winback/save-offer machinery overlaps marketing flows, but the intervention surface operates directly on the subscription object and its states; cross-product placement inside the subscription admin (not the marketing suite) marks it as this Type's capability.

## Historical / Market-Sample Check

Would older, regional, platform-native products still fit the L0?

- **Mail-order clubs** (record/CD clubs, book-of-the-month clubs, wine clubs): standing member commitment (X per month), club-side derived shipping/billing calendar, per-cycle execution (charge + shipment), lifecycle managed by correspondence/phone (skip, pause, cancel). Fits — without portal, dunning automation, analytics. Confirms those are L1.
- **Regional standing-delivery services** (milk delivery, newspaper goods delivery, periodic grocery boxes): same minimal structure. Fits.
- **Platform-native implementations** (Shopify selling plans / native subscriptions, store-built engines): the commitment + derived schedule + execution structure is present even when the vendor ships it as platform features rather than a standalone product. The Type is the structure, not the packaging.
- Modern digital/media subscriptions (SaaS, streaming) do NOT fit the goods-shaped L0 well (no per-cycle shipment; entitlement-centric) — they belong to Subscription Billing Platform. The L0's "receive specified products" phrasing deliberately leaves room for curated boxes (product = the box) and consumables.

Conclusion: L0 is not over-fitted to the current DTC-subscription era.

## Uncertainties

1. Recharge's exact dunning feature set (Smart Retries equivalent) was not directly observed in fetched pages; dunning was asserted cross-product from Skio + Ordergroove only. Final doc uses "mature products commonly" wording.
2. Ordergroove operational internals (admin console, API object model, state names) unverified (Knowledge Center unreachable) — no Ordergroove-specific mechanics asserted.
3. Cratejoy evidence is marketing/features-tier only; its operational depth (e.g., dunning automation) unknown — Cratejoy not used for any precise claim.
4. Whether the market sustains two Types under the sibling leaf names is unresolved; flagged for joint review.
5. Gift-subscription mechanics differ per product (prepaid-gift vs recurring-gift); final doc stays conceptual.
6. Relative market sizes, pricing models, and numeric limits deliberately not asserted.

## Final Synthesis

Recurring Commerce Management is the merchant-side system of record for *recurring goods commerce*: it holds each customer's standing commitment (subscriber × products × frequency × destination), projects it forward as a schedule of upcoming order/charge events, executes each event as a real commerce transaction with a fulfillment handoff, and manages the commitment's life between cycles — for both the merchant (operations, retention, analytics) and the subscriber (self-service adjustment). Mature products wrap this core with storefront enrollment surfaces, subscriber portals, dunning/recovery, cancel-flow retention machinery, bundles/prepaid/gift shapes, and subscription analytics; they ride on storefront platforms (or, more rarely, own the storefront), and the market expresses the same structure under the labels "subscription platform" and "recurring commerce". The sibling leaf "Subscription Commerce Platform" is most likely the same referent (alias risk flagged); the structural boundary that *does* hold is against Subscription Billing Platform (entitlements/invoices vs goods deliveries), against plain e-commerce (no standing commitment), and against OMS (orders, not commitments).
