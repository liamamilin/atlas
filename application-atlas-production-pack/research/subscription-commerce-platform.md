# Research Notes — Subscription Commerce Platform

Research date: 2026-09-08
Methodology: WORKFLOW_v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

## Research Goal

Understand what the Application Type "Subscription Commerce Platform" (DIRECTORY 05.16 Subscription Commerce, sibling of "Recurring Commerce Management") actually is in the real market: the objects it manages, the workflows it runs, its lifecycle and rules — and, critically, resolve the joint-review flag raised by the sibling pass: whether this leaf is a distinct Type, an alias/umbrella of "Recurring Commerce Management", or has a distinct referent of its own.

Context: research/recurring-commerce-management.md (2026-09-07) sampled Recharge, Skio, Ordergroove, Cratejoy and flagged this sibling as a probable alias — all four self-described as "subscription platform" for the same referent. This pass deliberately samples a DIFFERENT set of products that market themselves under the "subscription commerce platform" / "subscription platform" label, to test the alias hypothesis independently and check whether any product falls on this leaf only.

## Initial Boundary

Working hypothesis before research:

- Core use: merchant-side software that lets a commerce business sell products on a repeating schedule — subscribe & save replenishment, subscription boxes, auto-ship, memberships with recurring deliveries.
- Users: subscription/DTC e-commerce merchants, their retention/support/ops teams; subscribers via self-service portal.
- Nearest Types:
  - **Recurring Commerce Management** (sibling, 05.16) — probable alias per the sibling's flag.
  - **Subscription Billing Platform** (08 Finance) — invoice/entitlement-centric recurring money, no per-cycle goods fulfillment.
  - **E-commerce Platform** (05.01) — storefront/checkout substrate.
  - **Order Management System** (05.07) — per-order unit of record, not per-commitment.
- Unknowns: does any market product map to "Subscription Commerce Platform" but NOT to recurring-goods commitment management? Do the "enablement vs operations" emphasis poles hold up as a seam?

## Research Questions

1. What objects does a product self-labeled "subscription commerce platform" manage (subscriber, subscription/commitment, schedule, orders, charges)?
2. What is the commitment lifecycle (states; skip/pause/cancel/reactivation semantics; dunning)?
3. How is the future order schedule derived and executed (charge → order → fulfillment handoff)?
4. What enrollment/checkout integration surfaces exist (the "platform/enablement" emphasis test)?
5. What retention machinery exists (cancel flows, save offers, winbacks)?
6. What deployment postures exist (all-in-one host / storefront-embedded app / app-suite / headless)?
7. ALIAS TEST: do products here and the sibling's four form one competitive set (migration paths, substitute positioning), or two distinct markets?
8. Same boundaries as the sibling found (vs billing / e-commerce / OMS / loyalty)?

## Representative Products

Selection: all four self-identify with this leaf's label family; different philosophies and customer tiers; documentation depth; deliberate non-overlap with the sibling's four.

| Product | Posture | Segment | Why selected |
|---|---|---|---|
| Subbly | All-in-one "subscription-first commerce platform": owns site builder + checkout + subscription engine | SMB / first-time subscription founders up to mid-market | Exact label match ("The Subscription-first Commerce Platform"); all-in-one pole; 11+ years in market |
| Bold Commerce | "Repeat commerce" app suite for Shopify; Subscriptions is one of six apps + headless checkout product | Mid-market to Plus merchants | Commerce-enablement pole; deepest help center of the sample (398 subscription articles); app-suite philosophy |
| Appstle | Retention-focused Shopify app suite (Subscriptions, Memberships, Loyalty, Bundles, Pickup & Delivery) | SMB to Shopify Plus | High-volume app-suite pole; explicit substitute-list of the whole market |
| Smartrr | Shopify-native "subscription platform" with brand-experience/retention emphasis | Growing DTC brands, mid-market/enterprise | Modern brand-experience pole; strong Tier-1 GitBook help docs |

Alias cross-check set (from sibling research, not re-sampled): Recharge, Skio, Ordergroove, Cratejoy.

## Sources

### Subbly (Tier-2 product pages + Tier-1 help center)
- https://www.subbly.com/ (product root, self-description, use cases, migration list) — 2026-09-08
- https://support.subbly.co/ (help center home, categories) — 2026-09-08
- https://support.subbly.co/customers (subscription-management article index) — 2026-09-08
- https://support.subbly.co/orders (orders article index) — 2026-09-08
- Developer docs referenced at https://www.subbly.dev (not fetched)

### Bold Commerce (Tier-2 product pages + Tier-1 help center)
- https://www.boldcommerce.com/ (product root, app-suite positioning) — 2026-09-08
- https://support.boldcommerce.com/ (help center home, collection list) — 2026-09-08
- https://support.boldcommerce.com/en/collections/19676983-bold-subscriptions (Bold Subscriptions article index, ~398 articles; collection/article titles observed) — 2026-09-08
- Individual article bodies NOT fetched (index-level evidence only)

### Appstle (Tier-2 product pages)
- https://www.appstle.com/ (product root, app suite, comparisons/substitute list, reviews) — 2026-09-08
- Help center not fetched (no Tier-1 operational detail asserted for Appstle)

### Smartrr (Tier-2 product pages + Tier-1 GitBook docs)
- https://www.smartrr.com/ (product root, platform structure, feature list, case studies) — 2026-09-08
- https://help.smartrr.com/docs (help docs home + full section index) — 2026-09-08
- https://help.smartrr.com/docs/support/customer-account-portal/manage-subscriptions.md (full article: portal actions) — 2026-09-08

### Source-access Limitation
- Bold Subscriptions evidence is index-level (article/collection titles + one-line descriptions); individual article bodies not fetched, so Bold-specific operational mechanics (exact dunning behavior, exact group semantics) are NOT asserted.
- Appstle evidence is Tier-2 product-page only; Appstle-specific mechanics not asserted.
- Vendor performance claims (Subbly "20,000+ users"; Bold "760,000+ installs/800K merchants"; Appstle "40,000+ merchants"; Smartrr "94% average subscriber retention", case-study growth figures) are marketing claims — recorded as claims, never asserted as facts.

## Product A — Subbly

### Key observations (evidence layer tagged)

- Self-description: "The Subscription-first Commerce Platform"; "an all-in-one commerce platform allowing you to use AI to launch, run, and grow any subscription business model." Positioning: "No plugins or complex costly stacks, everything in one"; embeddable checkout, APIs/SDKs, AI website builder. [A]
- Use cases named on product root: subscription boxes, personalized boxes, subscribe & save, D2C replenishment, meal delivery (kits & prep), memberships, CSA farms. [A]
- **Migration list on product root**: migrate from Shopify, WooCommerce, Wix, Bold, Squarespace, Recharge, Cratejoy, BigCommerce, PayWhirl, MoonClerk. This places Subbly in ONE competitive set with the sibling's sample (Recharge, Cratejoy) and with Bold — strong alias-test evidence. [A]
- Help-center structure: Account & Billing; **Checkout & Payments**; **Agentic Builder** (website builder, 31 articles); Products (33); **Customers — "Handling your customer's subscriptions"** (19); **Orders — "Handling your customer's orders"** (9); Growth & Retention (20); Integrations & App Store (28); FAQs. [A]
- **Subscription operations (Customers category)**: how customers manage their subscription (Customer portal); merchant can add a customer's subscriptions manually; customer labels; switch the subscription product; change renewal date; see customer preferences; change shipping address; customers add products to their subscription; process refunds; **reactivate a customer's subscription**; how skipping/pausing works; templated email notifications; account credit balance; export customer data; "Why my customer wasn't charged?"; cancel subscription; **Event Logs**; AI Author Bot. [A]
- **Orders category**: order labels; handling orders; filtering orders; importing orders; test orders; **create adhoc orders/charges**; add tracking number; **"Why my orders don't appear in my Shipstation admin"** — fulfillment handoff to ShipStation confirmed. [A]
- Marketing/retention surfaces on product root: gifting "designed for subscription businesses"; multiple checkout templates; bundles where "price dynamically adjusts" for complex models (meal kits); funnels, upsells, AI prediction models. [A]
- Deployment posture: owns the whole stack (site + checkout + subscriptions); also offers "Subbly X" done-for-you service and a separate done-for-you launch service. [A]

## Product B — Bold Commerce

### Key observations (index-level for help center; root-page observations tagged A)

- Self-description: "THE REPEAT COMMERCE COMPANY — Built for the buy-again." Six repeat-commerce apps for Shopify: rePete (reorder nudging), **Subscriptions**, Upsell, Custom Pricing, Memberships, Discounts. "App Suite" philosophy: apps share data/context; "open-first"; native Shopify Flow integration. [A]
- Bold Subscriptions description: "Flexible subscription plans with automated billing, built-in churn prevention, and upsell tools." Also ships a headless **Checkout** product and **Price Rules** ("Custom Checkout Logic", "Sell Anywhere") — commerce-enablement emphasis confirmed. [A]
- Subscriptions + rePete "Maximizer": "Turn cancelled subscribers into repeat customers" — cancelled subscribers auto-enrolled in reorder nudges (a distinctive post-cancellation retention variant). [A]
- **Help center (BOLD Subscriptions collection, 398 articles — index-level evidence)**: [A index]
  - "Subscriptions for Shopify Checkout" (current product generation) with **migrate-from articles: Recharge, Yotpo Subscriptions, PayWhirl, Stay Ai, Ordergroove, Seal, Skio, WooCommerce** — again one competitive set with the sibling sample.
  - **Create a Subscription**: Subscription Group Settings; Standard Subscription Group; **Prepaid Subscriptions**; **Convertible Subscriptions**; **Subscription-Only Products**; edit/deactivate/delete/re-sync a group; Buy Now Links.
  - **Subscription Management**: Shopify Customer Accounts portal extension ("shoppers manage subscriptions, upcoming orders, and self-serve account changes"); Set up and Manage the Customer Portal; "Subscription Management: Merchant Perspective"; "Subscription Management: Customer Perspective"; **Upcoming orders extension** ("customers can easily skip, resume, or immediately ship their next subscription order"); Refund a Subscription Order; subscription notes; passwordless login.
  - **Bulk Updates**: bulk price updates; bulk product swap; bulk swap deleted products.
  - **Settings, Notifications & Reports**: **Inventory Handling for Recurring Orders**; **Cancellation & Dunning Management**; Email Notifications; "Customer View: **Retention Actions in the Cancellation Flow**"; Dashboard Analytics, Reports & Activity Logs.
  - **MAXIMIZERS™**: Try Before You Subscribe; Dynamic Discounts; Default to Subscribe; Express Add-Ons Widget; Product Add-Ons; Subscription Upsells; Customer Portal Upsells; Subscription Email Upsells.
  - FAQ titles confirming commitment-granular operations: combine two subscriptions into a single shipment; process the next order sooner/earlier than scheduled; pause all active subscriptions at once; prevent cancelling too soon; swap products; delayed first shipment; set subscriptions to automatically cancel after a few months; gift subscriptions; one-time purchase option; **"Can I set up subscriptions for payment plans?"**; minimum/maximum subscription length; cancellation reasons; **"How to Recapture Customers with Cancelled or Paused Bold Subscriptions"** (winback); "What Are Cutoff Days?"; "How are subscription payments processed?"; sort subscriptions by upcoming order date.

## Product C — Appstle

### Key observations (Tier-2 only)

- Self-description: "Grow ecommerce revenue with retention focused experiences"; suite of Shopify apps: **Subscriptions**, Memberships, Loyalty & Rewards, Bundles & Upsells, **Pickup & Delivery**. Claimed 40,000+ merchants, 10,000+ reviews. [A]
- Appstle Subscriptions: "Create subscription offers that convert in just a few clicks. **Build-a-box, bundling offers, upsells, tiered discounts**... Reduce customer churn with flexible subscriptions... **Inventory management controls, customizable billing options, and bulk automations**." [A]
- Appstle Memberships: membership plan creation & management, tiered member perks, member billing. Appstle Pickup & Delivery: store pickup / local delivery / shipping scheduling with date & time selection, blackout dates, prep times, order cutoffs. [A]
- **Substitute/comparison list** (comparisons page): Bold, Recharge, PayWhirl, Seal, Skio, Recurpay, Casa, Subify, Ordergroove, Loop, Easy, Joy, Kaching, Super — the market's own map of the competitive set; includes the sibling's Recharge/Skio/Ordergroove and this pass's Bold. [A]
- Review quotes on product page mention: independent shipping options/profiles for subscriptions, customization of the subscription program using Shopify Checkout, migration support from a competing app. [A, vendor-published reviews — treated as claims]

## Product D — Smartrr

### Key observations

- Self-description: "The last **subscription platform** you'll ever need"; "Definitely, 100% Shopify Native." Products: **Subscriptions** (core), Smartrr Lifecycle ("Identify, target, and convert customers primed for a second purchase"), Loyalty Rewards & Referrals (add-on). [A]
- Feature list: Customer Account Portal, Advanced Analytics, Subscription Widget, Build-a-box Bundles, **Retention Actions** ("special offers or marketing actions tailored to the specific cancellation or pause reason given by a customer"), **Subscription Journey Builder**, Loyalty Tiers. "From basic Subscribe & Save to box-of-the-month and prepaid subscriptions." [A]
- Comparisons vs Recharge, Loop, Stay AI, Appstle, Yotpo; case studies describe migrations from Bold, Recharge, Yotpo, "Legacy App" — one competitive set again. [A]
- **Help docs (Tier-1, GitBook)**: [A]
  - Subscription Setup: programs; **anchor dates**; **maximum/minimum (finite) subscription plans**; email/SMS subscription notifications; discount codes; **prepaid subscriptions**; **Sequential Flow Builder**; **shipping methods for subscription products**; **what happens to a subscription when an item is out of stock**; BNPL payment methods for subscriptions; Checkout Extensions.
  - Admin Portal: view/adjust customers' subscriptions; adjust customer information; **"View as customer"**; **Subscription Events Timeline**; Advanced Analytics reporting; portal theming/translations/CSS; **"set which actions my customers can take on their subscriptions in their account portal"** (merchant-configurable portal actions); Marketing Banners; Retention; Bundles; Loyalty; creator upsells.
  - Customer Account Portal: access, account creation, **view next order**, manage subscriptions, order history.
  - Transactions: view subscription transactions; **rules around failed payments**; what happens when a payment method fails; **billing schedule** adjustment.
  - Integrations: Attentive, Blueprint, Gorgias, Klaviyo, LoyaltyLion, Postscript, **Recharge**, Shopify Flow; webhooks.
  - Bulk Updates: bulk update next order date.
  - Troubleshooting: "Why did my customer's subscription automatically pause?" (automatic pause exists as behavior).
- **Portal article (full text)**: customers view active and paused subscriptions in the portal; **canceled subscriptions do not appear in the portal — cannot be reactivated by customer or brand**; actions: **Edit frequency** (options limited to the plans available in the subscription program; if only one plan exists the action can be turned off), **Set next date** ("Your upcoming orders will be updated based on this new date"), **Edit bundle items** (adjust quantity, add/remove items, box-full progress, change bundle size), **Edit payment** (secure update link via email), **Pause** (customer must select a date for auto-resume within the next six months), **Cancel** (confirmation state; if Retention features are on, reason required). [A]

## Cross-product Comparison

Legend: ✔ observed (evidence layer A unless noted); ✔idx observed at help-index level; ~ from sibling research pass (A); — not observed.

| Structure / capability | Subbly | Bold | Appstle | Smartrr | Sibling sample (Recharge/Skio/Ordergroove/Cratejoy) | Layer |
|---|---|---|---|---|---|---|
| Subscription commitment record (customer × product(s) × frequency × destination) | ✔ (subscriptions per customer; renewal date; address; manual creation) | ✔ (subscription groups; subscriptions; notes) | ✔ ("subscription offers"; program config) | ✔ (subscription programs; active/paused/canceled states) | ✔ all four | **L0** |
| Derived recurring order schedule (upcoming/next order dates, projected queue) | ✔ (renewal dates; "why wasn't my customer charged"; adhoc orders) | ✔ ("upcoming orders" portal extension; sort by upcoming order date; bulk next-order-date update) | ✔ (bulk automations; billing options) | ✔ ("view next order"; "upcoming orders will be updated based on this new date"; billing schedule) | ✔ all four (next charge date, queued orders, forecasting) | **L0** |
| Per-cycle execution: charge → order → fulfillment handoff | ✔ (charges + orders as separate objects; ShipStation; tracking numbers) | ✔ ("how are subscription payments processed"; subscription order failure troubleshooting; inventory handling for recurring orders) | ✔ (billing options; inventory controls) | ✔ (transactions section; failed-payment handling; Shopify order stream) | ✔ all four (charge→order; OMS/carrier handoff) | **L0** |
| Managed commitment lifecycle (skip/pause/cancel/swap/reschedule; expiry) | ✔ (skip/pause; cancel; reactivate; switch product; change renewal date) | ✔ (skip/resume/ship now; pause all; cancel; swap; min/max length; auto-cancel after N months) | ✔ (flexible subscriptions; churn reduction) | ✔ (edit frequency; set next date; pause w/ auto-resume; cancel; no reactivation after cancel) | ✔ all four | **L0** |
| Storefront enrollment surface (widget/plan picker; subscribe vs one-time) | ✔ (checkout templates; embeddable checkout; site builder) | ✔ (subscription widget app block; Default to Subscribe; subscription-only products; buy-now links) | ✔ (subscription offers; Shopify checkout customization) | ✔ (subscription widget; checkout extensions) | ✔ all four | L1 |
| Subscriber self-service portal | ✔ (customer portal) | ✔ (customer portal; Shopify Customer Accounts extension) | ✔ (customer hub integration; portal) | ✔ (Customer Account Portal; merchant-configurable actions; full article) | ✔ all four | L1 |
| Merchant admin: per-commitment ops, bulk ops, audit | ✔ (manual subscription creation; event logs; labels) | ✔ (merchant perspective; bulk updates; activity logs) | ✔ (bulk automations) | ✔ (admin portal; bulk next-order-date; events timeline; view-as-customer) | ✔ all four | L1 |
| Dunning / payment recovery | ✔ ("why wasn't my customer charged"; payment retry surfaces implied) | ✔idx (Cancellation & Dunning Management collection) | ~ (implied) | ✔ (failed-payment rules; automatic pause troubleshooting) | ✔ (Skio Payment Recovery/Smart Retries; Ordergroove Involuntary Churn Suite) | L1 |
| Cancel flows / retention actions / winback | ✔ (Growth & Retention category) | ✔idx (Retention Actions in the Cancellation Flow; Recapture cancelled/paused; rePete post-cancel nudging) | ✔ (churn-reduction claims; cancellation reasons in comparisons) | ✔ (Retention Actions keyed to cancel/pause reasons) | ✔ (Skio cancel-flow A/B + winbacks; Ordergroove save offers/winbacks) | L1 |
| Discounts / subscription pricing | ✔ (checkout templates; dynamic bundle pricing) | ✔idx (Discounts app; Dynamic Discounts maximizer; discount codes) | ✔ (tiered discounts) | ✔ (discount codes; loyalty tiers) | ✔ all four | L1 |
| Bundles / build-a-box | ✔ (bundles with dynamic pricing for meal kits) | ✔idx (Bundles app; Build-a-Box with Easy Bundles) | ✔ (Build-a-box; Bundles & Upsells app) | ✔ (Build-a-box Bundles; bundle edit in portal) | ✔ (Recharge BYOB; Skio Build-a-Box; Ordergroove Bundles & Clubs; Cratejoy box-native) | L1 |
| Prepaid | — | ✔idx (Prepaid Subscriptions) | — | ✔ (prepaid subscriptions setup) | ✔ (Recharge queued orders; Skio prepaid gifts; Ordergroove 12-shipment prepay) | L1 |
| Gift subscriptions | ✔ (gifting designed for subscriptions) | ✔idx (gift subscriptions FAQ; Govalo gift-card integration) | — | — | ✔ (Recharge gifting widget; Skio prepaid gift; Cratejoy gift cards) | L1 |
| One-time items alongside subscriptions | ✔ (adhoc orders/charges; customers add products to subscription) | ✔idx (one-time items to a recurring order; Product Add-Ons; Express Add-Ons) | ✔ (upsells) | ✔ (one-time add-ons in portal) | ✔ (Recharge One-times; Skio; Ordergroove; Cratejoy) | L1 |
| Subscription analytics | ✔ (Growth & Retention surfaces; exports) | ✔idx (Dashboard Analytics, Reports & Activity Logs) | ~ (analytics claims) | ✔ (Advanced Analytics) | ✔ (Skio dunning/forecast/cohort dashboards; Ordergroove revenue waterfall; Cratejoy KPIs) | L1 |
| Lifecycle notifications (email/SMS) | ✔ (templated emails) | ✔idx (Email Notifications; SimpleTexting integration) | ~ | ✔ (email + SMS notifications setup) | ✔ all four | L1 |
| API / webhooks / integration fabric | ✔ (APIs/SDKs; integrations & app store; ShipStation) | ✔idx (APIs article; ~25 named integrations; Shopify Flow) | ✔ (integration list: Klaviyo, Gorgias, Yotpo, Zapier, Rebuy...) | ✔ (webhooks; named integrations; Shopify Flow) | ✔ all four | L1 |
| Loyalty / rewards / referrals module | ~ (marketing category) | ✔ (separate Memberships/Custom Pricing apps; Yotpo loyalty integration) | ✔ (separate Loyalty & Rewards app) | ✔ (native Loyalty add-on; LoyaltyLion integration) | ✔ (Recharge Rewards; Skio Loyalty; Ordergroove loyalty integrations) | L2 |
| Memberships (access/perks recurring) | ✔ (memberships use case) | ✔ (separate Bold Memberships app) | ✔ (separate Memberships app) | — | ~ (Ordergroove Paid Memberships pillar) | L2 |
| AI-era surfaces (builders, agents, lifecycle AI) | ✔ (agentic AI builder; AI prediction models; AI Author Bot) | ✔ (AI Upsells) | — | ✔ (Smartrr Lifecycle; Subscription Journey Builder) | ✔ (Ordergroove Frontier AI agents; Skio Journeys) | L2 |
| Reorder nudging for one-time buyers / post-cancel | — | ✔ (rePete app) | — | ✔ (Smartrr Lifecycle — "customers primed for a second purchase") | — | L2 |
| Pickup / local delivery scheduling | — | — | ✔ (Pickup & Delivery app) | — | ~ (Skio delivery methods) | L2 |
| BNPL payment methods for subscriptions | — | — | — | ✔ (setup article) | — | L2 |
| All-in-one host (owns storefront + checkout) | ✔ (defining posture) | — (checkout product is headless, not storefront) | — | — | ✔ (Cratejoy) | L2 (deployment posture) |
| Marketplace acquisition channel | — | — | — | — | ✔ (Cratejoy marketplace) | L2 |
| Migration machinery as first-class workflow | ✔ (migration from 10 platforms incl. Recharge/Cratejoy/Bold) | ✔idx (8 migrate-from articles incl. Recharge/Skio/Ordergroove) | ✔ (migrations page + per-competitor comparisons) | ✔ (migrate-to pages; case studies) | ✔ (Skio/Ordergroove flagship migrations) | L1 (market behavior) |
| Named vendor machinery (Subscription Groups, MAXIMIZERS, rePete, passwordless Shop Pay; anchor dates, Sequential Flow Builder, six-month pause auto-resume, no-cancel-reactivation, View-as-customer, creator upsells; agentic builder, Subbly X, account credit; shipping profiles, 24/7 chat) | ✔ | ✔ | ✔ | ✔ | ✔ | L3 |

### Alias test (joint review with recurring-commerce-management)

1. **Self-description overlap**: this pass's products self-describe as "subscription platform" (Smartrr), "subscription-first commerce platform" (Subbly), "repeat commerce company" whose Subscriptions app does "automated billing... churn prevention" (Bold), "retention focused... subscriptions" suite (Appstle). Sibling pass: Recharge/Skio/Ordergroove all "subscription platform", Cratejoy "ecommerce platform for subscription box businesses". The two label sets describe the same referent.
2. **One competitive set**: explicit migrate-from/migrate-to/comparison links cross the two samples in both directions — Bold migrates from Recharge/Skio/Ordergroove/PayWhirl/Stay Ai/Seal/Yotpo; Smartrr migrates/case-studies from Bold/Recharge/Yotpo; Subbly migrates from Recharge/Cratejoy/Bold/PayWhirl; Appstle compares against Bold/Recharge/Skio/Ordergroove; Smartrr even documents a coexistence/integration article with Recharge. Products in a competitive set with free movement are one market, not two Types.
3. **Structure identity**: the L0 structures derived independently by both passes are the same four-structure chain (commitment → schedule → per-cycle execution → managed lifecycle). No structural feature observed in this pass is absent from the sibling's, and vice versa (marketplace and all-in-one postures appear once each across the combined sample — both are L2 variants, not seams).
4. **Emphasis-seam test FAILED**: the candidate seam "commerce enablement/enrollment/checkout-integration vs ongoing operations/lifecycle/retention" does not hold — Subbly (the all-in-one "commerce platform" pole) has full retention/operations machinery (skip/pause/cancel/reactivate, event logs, refunds, growth & retention tooling), and Bold (the enablement pole) also ships dunning and cancel-flow collections. Every sampled product straddles.

**Verdict: alias/umbrella confirmed.** "Subscription Commerce Platform" and "Recurring Commerce Management" are two market labels for one Application Type. Both leaves are documented on the same defining core; the alias is recorded in Related Application Types of both final documents and in STATUS.md Boundary Issues. No market product maps to only one label.

## Canonical Model

### L0 — Defining Invariant (smallest stable structure)

```text
Subscription commitment of record
  (identified customer × specified product(s) × repeating frequency × delivery destination;
   persists between cycles)
  └── Derived recurring order schedule
      (system-projected queue of upcoming charge + order events)
      └── Per-cycle execution
          (each event executed as a real commerce transaction:
           payment charged → order created → handed off for fulfillment)
          └── Managed commitment lifecycle
              (schedule, contents and existence changeable and terminable
               between cycles — by subscriber and/or merchant)
```

Four jointly-held structures. Remove any one and the product stops being this Type:

- Remove the **commitment of record** → ordinary e-commerce with a reorder button; nothing persists between transactions.
- Remove the **derived schedule** → a commitment that never produces foreseeable future events; merchants cannot see what will ship and charge next.
- Remove **per-cycle execution** → a wishlist/reminder tool; nothing is commerce until money moves and an order exists.
- Remove **managed lifecycle** → a fixed installment plan; skip/pause/swap/cancel is what makes it a *managed* subscription program.

Note (carried from the sibling pass, consistent with this sample): the object being managed is the commitment to *receive goods*, not debt repayment — installment/payment-plan usage exists (Bold FAQ) but is a boundary-adjacent configuration, not the center.

### L1 — Common Mature Structure (very common; not definitional)

- Storefront enrollment surface (subscription widget / plan picker / subscription groups; subscribe-vs-one-time choice; subscription-only products; default-to-subscribe merchandising)
- Subscriber self-service portal (skip, pause, cancel, swap, edit frequency, set next date, update payment, add items) — with merchant-configurable action sets
- Merchant admin (per-commitment operations incl. manual creation, bulk updates, event/activity logs, refunds)
- Dunning / payment recovery (failed-payment handling, retries, automatic pause states, recovery analytics)
- Cancel-flow machinery (reason capture, retention/save offers keyed to reasons, winback/recapture of cancelled or paused subscribers)
- Discount / subscription-pricing machinery (recurring discounts, dynamic discounts, tiered pricing)
- Bundles / build-a-box; one-time add-ons and ad-hoc orders alongside commitments
- Prepaid commitments; gift subscriptions
- Subscription analytics (recurring revenue, churn, retention, forecasts; activity reporting)
- Lifecycle notifications (templated email, often SMS; shipping/payment notices)
- API / webhooks integration fabric; fulfillment handoff (platform order stream, OMS, carrier/label tools)
- Migration machinery between competing platforms (market-standard behavior)

### L2 — Variant / Optional Structure

- Loyalty / rewards / referrals modules (native add-on or separate app)
- Memberships with recurring perks/access (as adjacent program shape)
- AI-era surfaces: agentic site builders, AI upsells, AI retention agents, lifecycle prediction ("second-purchase" targeting)
- Reorder nudging for lapsed subscribers (post-cancellation conversion into one-time repeat buyers)
- Pickup / local-delivery scheduling; BNPL payment methods
- Deployment posture: all-in-one host (owns storefront + checkout) vs storefront-embedded app vs app-suite vs headless/API-first
- Vertical tuning (boxes, meal kits, CSA farms, coffee, beauty, pet, wellness)
- Marketplace acquisition channel (one known pole)
- Payment-plan configuration (installment-shaped use of the same machinery)

### L3 — Vendor-specific (kept out of final document)

- Subbly: agentic AI builder, Subbly X done-for-you, account credit balance, AI Author Bot, ad-hoc order/charge object naming, 10-platform migration menu
- Bold: Subscription Groups (product+frequency config container), MAXIMIZERS™, rePete reorder-nudge app, passwordless/Shop Pay login, convertible subscriptions, cutoff days, 398-article help corpus, headless Checkout + Price Rules products
- Appstle: independent shipping profiles for subscriptions, Pickup & Delivery scheduling app, per-competitor comparison pages, 24/7 support claims
- Smartrr: anchor dates, Sequential Flow Builder, pause requires auto-resume date within six months, cancelled subscriptions cannot be reactivated by customer or brand, View-as-customer, creator upsells, Instagram feed in portal, Subscription Events Timeline, Smartrr Lifecycle
- Sibling pass L3: Recharge Affinity/RCPM/one-product-per-address; Skio SkioSMS/Streaks/Journeys; Ordergroove Flex Incentives/Recovery Optimizer/Everychannel; Cratejoy marketplace/Sitebuilder

## Vendor-specific Findings

(All single-product; recorded per evidence rules)

- **Subbly**: merchant can create subscriptions manually for customers (phone-order path); reactivation of cancelled subscriptions is a documented operation; ad-hoc orders/charges exist as a distinct object; fulfillment via ShipStation is a named integration with troubleshooting articles; account-credit balance feature.
- **Bold**: subscription configuration is organized as "Subscription Groups" (products + frequencies configured as a group; moving customers between groups is a documented FAQ); "convertible subscriptions" (a subscription that converts to a different product); explicit "cutoff days" concept; payment-gateway compatibility FAQs dominate its FAQ corpus; payment plans configurable via subscriptions.
- **Appstle**: ships pickup & local-delivery scheduling as a sibling app (date/time selection, blackout dates, prep times, cutoffs); independent shipping profiles for subscriptions highlighted as a differentiator (vendor-published review).
- **Smartrr**: pause requires the customer to pick an auto-resume date within six months; cancelled subscriptions are hidden from the portal and cannot be reactivated by customer or brand (contrast: Subbly and Bold document reactivation/recapture paths — reactivation policy is product-specific, NOT canonical); frequency options are constrained by the program's configured plans; "View as customer" support tool; automatic pause can occur (troubleshooting article) tied to failed-payment handling.

## Boundary Findings

1. **vs Recurring Commerce Management (sibling leaf, 05.16) — RESOLVED: alias/umbrella.** See Alias test above. Both labels denote one Type: merchant-side software for recurring goods commerce. The candidate emphasis seam (enablement vs operations) failed. Joint review outcome: keep the directory as-is (both leaves documented), record the alias, recommend consolidation as one Type with two market labels if the directory is ever revised.
2. **vs Subscription Billing Platform (08 Finance)** — sharpest structural seam (consistent with sibling): this Type's unit is the recurring *goods* commitment whose every cycle ends in a charge and an order/shipment handoff; billing platforms center invoices/entitlements (SaaS/media/membership access) with no per-cycle fulfillment. Removing the fulfillment handoff and goods schedule collapses this Type into billing. Conversely, recurring *access* subscriptions (digital subscriptions) appear in this market only as an adjacent shape (Subbly "digital access" via sibling evidence; Ordergroove Digital Access pillar) — the goods-shaped core remains the Type.
3. **vs E-commerce Platform (05.01)** — substrate vs commitment layer: storefront/cart/checkout handle the transaction; this Type holds the standing commitment, its future schedule, and between-cycle state. The all-in-one pole (Subbly, Cratejoy) proves the commitment machinery is the Type: even when the vendor owns the whole storefront, the same four-structure core is what the product is *for* ("subscription-first", "subscription box businesses").
4. **vs Order Management System (05.07)** — unit of record: OMS manages individual orders; this Type manages the commitment that *generates* future orders and the state between them (skip/pause/dunning). Fulfillment deep operations (picking, packing, warehouse) stay outside; handoff is the seam (ShipStation/Shopify order stream/OMS integrations).
5. **vs Loyalty Program Management (05.15) / Memberships** — loyalty and memberships appear as separate apps or add-on modules across this sample (Appstle and Bold ship them as separate apps; Smartrr as an add-on); their managed objects (points/redemptions; access/perks) are not recurring goods orders. Optional adjacency, not definitional.
6. **vs Marketing Automation (06)** — retention interventions operate directly on the commitment object inside this system (pause instead of cancel, save offers on the subscription, winback reactivation of the commitment); campaigns may be executed through integrated marketing tools (Klaviyo/Attentive), but the authority over subscription state lives here.
7. **vs Subscription marketplaces** — a consumer-facing marketplace for discovering subscription products (Cratejoy marketplace pole) is an Online/Service Marketplace variant riding on this Type's output, not a distinct core; the seller-side machinery remains this Type.

## Historical / Market-Sample Check

Would older, regional, platform-native, or differently positioned products still fit the L0?

- **Mail-order / record / book / wine clubs**: standing member commitment, club-side billing & shipping calendar, per-cycle charge + shipment, lifecycle managed by correspondence. Fits — no portal, dunning automation, or analytics needed. Confirms those are L1.
- **Regional standing-delivery services** (milk delivery, newspaper delivery, periodic grocery boxes, **CSA farm shares** — Subbly explicitly lists CSA farms as a use case, giving a modern anchor to a pre-internet business form): same minimal structure. Fits.
- **Platform-native subscriptions** (Shopify's native subscription APIs / selling plans; store-built engines): the commitment + schedule + execution structure exists even when shipped as platform features rather than a standalone product. The Type is the structure, not the packaging.
- **Payment plans / installments** (Bold FAQ): configurable through the same machinery, but the canonical object there is debt repayment, not goods receipt — a boundary-adjacent configuration, consistent with the sibling's finding.
- **Digital/SaaS subscriptions** (streaming, software licenses): do NOT fit the goods-shaped core (no per-cycle shipment) — they belong to Subscription Billing Platform. The wording "receive specified products" keeps curated boxes (product = the box) inside the Type.

Conclusion: L0 is not over-fitted to the current Shopify/DTC-subscription era.

## Uncertainties

1. Bold Subscriptions evidence is help-index level; article bodies not fetched. Bold-specific mechanics (exact dunning behavior, group-change propagation) are NOT asserted anywhere.
2. Appstle evidence is Tier-2 product pages only; no Appstle-specific operational rules asserted.
3. Subbly's dunning/retry specifics were not directly observed (the "why wasn't my customer charged" article title was observed, not its body); dunning asserted cross-product from Smartrr (failed-payment rules) + Bold (dunning collection) + sibling sample.
4. Smartrr's "automatic pause" trigger conditions were not read in full (article title observed only); recorded as behavior-exists, mechanism unknown.
5. Market-size, pricing, and numeric limits deliberately not asserted anywhere.
6. Whether the directory should consolidate the two 05.16 leaves is a taxonomy decision reserved to joint review / directory owners; this pass records the alias rather than acting on it.

## Final Synthesis

Subscription Commerce Platform is — as its market usage and product self-descriptions show — the same Application Type its sibling leaf names: the merchant-side system of record for recurring goods commerce. It holds each customer's standing commitment (subscriber × products × frequency × destination), projects it forward as a schedule of upcoming charge/order events, executes each event as a real commerce transaction with a fulfillment handoff, and manages the commitment's life between cycles for both subscriber (self-service portal) and merchant (operations, dunning, retention, analytics). The joint review with Recurring Commerce Management confirms the two labels are an alias pair: eight sampled products across both passes form one competitive set with free migration paths, identical self-descriptions, and one identical four-structure core; the only candidate seam (enablement vs operations emphasis) is straddled by every product. Mature products wrap the core with enrollment surfaces, portals, dunning, cancel-flow retention, bundles/prepaid/gift shapes, and subscription analytics; deployment ranges from all-in-one hosts through storefront-embedded apps and app suites to headless API-first platforms. The structural boundaries that hold are against Subscription Billing Platform (entitlements/invoices vs goods deliveries), against plain e-commerce (no standing commitment), and against OMS (orders, not commitments).
