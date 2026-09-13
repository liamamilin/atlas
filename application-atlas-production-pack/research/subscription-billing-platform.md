# Research Notes — Subscription Billing Platform

Research date: 2026-09-10
Slug: `subscription-billing-platform` · Directory leaf: **Subscription Billing Platform** (§08 Finance, Banking, Insurance & Investment)
Methodology: WORKFLOW_v1.1 (10-step) · WRITING_GUIDE_v1.1

---

## Research Goal

Understand the **Subscription Billing Platform** as an Application Type: what the subscription object is, how recurring charging is driven from it, what lifecycle states and transitions exist, how mid-cycle changes are resolved, how billing state couples to product access, and where the boundary lies against the many siblings that prior passes have hung flags on.

This leaf carries **six prior flags/seams** that this pass must discharge or confirm:

1. **billing-platform (§08, processed 2026-09-06)** — joint-review flag: "subscription recurring billing is the most-marketed pole but only one charge source among several… generic leaf defined model-neutrally so the specialized siblings remain poles/Types of the same spine; flagged for joint review when Subscription Billing Platform is processed."
2. **membership-billing (§25, processed)** — "machinery overlaps heavily (stored-method auto-charge, card on file, dunning, plan changes, proration)… seam = dues-for-belonging with standing-as-fulfillment vs commercial product subscription; JOINT REVIEW recommended."
3. **membership-management-system (§25, processed)** — same joint-review flag stands.
4. **media-subscription-management (§27, processed)** — "heaviest expected machinery overlap; seam = horizontal billing machinery for any industry vs media system of record with the access-binding leg + media product catalog; products deliberately span the seam (Stripe under Piano/Memberful, Zuora under Zephr, Vindicia under Arc XP) — packaging/integration evidence, not alias evidence."
5. **renewal-management-platform (§07, processed)** — "billing executes charging/auto-renewal/dunning with no decision object — Stripe lifecycle documented as boundary pole."
6. **subscriber-management (§19, processed)** — "telecom-charging-platform / subscription-billing seam = money computation vs who-has-what-and-is-active."

Plus recorded seams from **subscription-commerce-platform / recurring-commerce-management (§05.16)** ("recurring goods deliveries vs invoices/entitlements, sharpest structural seam"), **creator-subscription-platform** ("fan support vs business invoicing"), and **utility-billing-platform** ("generic §08 Billing Platform spine" framing).

## Initial Boundary (hypothesis before research)

- Hypothesis: a subscription billing platform is the vendor-side system of record for **standing recurring commercial commitments** — the subscription is a first-class managed object whose lifecycle (trial → active → renewal/amendment → payment-failure → cancellation) drives automatic recurring charging, and whose state couples to product access.
- It necessarily sits ON the generic Billing Platform spine (billing accounts, charge computation, invoice as authoritative amount-due record, tracked settlement — per the billing-platform pass). The open question is whether the subscription layer is enough additional structure to be a distinct Type, or merely the generic leaf's dominant charge source.
- Nearest neighbors: generic Billing Platform (model-neutral engine), subscription commerce (goods per cycle), media subscription management (media operator system of record), membership billing (dues for belonging), creator subscription platforms (fan-facing), renewal management (decision layer), payments execution, AR, invoicing, CPQ, rev-rec, telecom subscriber management.
- Unknowns going in: Is the subscription object genuinely additional structure beyond "subscription as a charge source"? Is entitlements/access coupling defining or common? Is mid-cycle amendment machinery defining or mature-common? Does the definition survive pre-SaaS subscription billing?

## Research Questions

1. What exactly is the subscription object? What does it hold and what references it?
2. What is the plan/price catalog and how does a subscription instantiate it?
3. What lifecycle states exist and what drives transitions (payment outcomes, customer actions, admin actions)?
4. How do mid-cycle changes work (upgrade/downgrade, proration, timing options, scheduled changes)?
5. How does billing state gate product access (entitlements)?
6. What happens on payment failure (retries, dunning, past-due states, auto-expiry)?
7. What recurring-revenue analytics exist (MRR/ARR/churn) — defining or common?
8. What is handed off upstream (checkout/CPQ) and downstream (payments, rev-rec, AR, GL)?
9. Does the definition survive pre-SaaS / non-SaaS subscription billing (paper-era subscription offices, early recurring-billing modules, telco)?
10. Which recurring market patterns are L1 common, L2 variant, L3 vendor-specific?

## Representative Products

| Product | Why sampled | Segment / philosophy | Evidence level reached |
|---|---|---|---|
| **Chargebee** | The archetypal self-described "subscription billing platform" for SaaS; mid-market; plan-catalog-centric with strong API | SMB→enterprise SaaS, no-code + API | **A** — Tier-1 API docs fetched (Subscriptions resource, Entitlements resource) |
| **Recurly** | Subscriber-lifecycle and retention-first philosophy; deep operational docs; product suite decomposition visible | Mid-market digital-subscription businesses | **A** — Tier-1 docs fetched (subscription lifecycle, change-subscription/proration, expire/cancel, recurring-billing section) |
| **Stripe Billing** | Developer-first billing infrastructure; subscription lifecycle documented as a state machine with entitlements | SMB→enterprise, API-first infrastructure | **A** — Tier-1 docs fetched (subscriptions overview incl. full status table; upgrade-downgrade/prorations) |
| **Zuora** | The enterprise recurring-revenue monetization archetype; suite decomposition makes sibling boundaries visible | Enterprise SaaS/media/IoT | **B** — doc portal landing fetched (module positioning + cross-product Entitlements topic); deep pages did not render |
| **Maxio** | B2B SaaS finance-operations pole (billing + rev-rec + metrics); G2 "Subscription Billing" category leader badges | B2B SaaS/AI mid-market, finance-led | **B** — official product pages fetched (module split, positioning); help docs not fetched |

Sampling check: different customer tiers (self-serve SMB → mid-market → enterprise), different philosophies (API-infrastructure vs retention-first vs plan-catalog vs enterprise-suite vs finance-ops), different commercial models (plan-based, hybrid usage, B2B contracts). No two products from the same vendor.

## Sources

Fetched 2026-09-10 (all official):

- Chargebee — https://apidocs.chargebee.com/docs/api/subscriptions (A; subscription resource: definition sentence, components, full status enum, term/cycle attributes, cancel reasons, subscription-level MRR, scheduled changes)
- Chargebee — https://apidocs.chargebee.com/docs/api/entitlements (A; entitlement resource: feature × item/item_price binding)
- Recurly — https://docs.recurly.com/ (A; docs hub: product split Subscriptions/Commerce/Engage/RevRec/Recover)
- Recurly — https://docs.recurly.com/recurly-subscriptions/docs/subscription-lifecycle.md (A; lifecycle action set)
- Recurly — https://docs.recurly.com/recurly-subscriptions/docs/change-subscription.md (A; timing options, proration credit/charge machinery, OBWC, modification enforcement)
- Recurly — https://docs.recurly.com/recurly-subscriptions/docs/expire-subscription.md (A; cancel vs terminate vs expire, reactivation window, dunning-driven auto-expiry)
- Recurly — https://docs.recurly.com/recurly-subscriptions/docs/recurring-billing/llms.txt (A; section index: invoices, credit invoices, adjustments, calendar billing, subscription terms, taxes)
- Recurly — https://docs.recurly.com/recurly-subscriptions/docs/subscriber-management/llms.txt (A; section index: accounts, entitlements, wallet, lifecycle communications)
- Stripe — https://docs.stripe.com/billing/subscriptions/overview.md (A; full lifecycle narrative + complete status table + entitlements provisioning + failed-payment handling)
- Stripe — https://docs.stripe.com/billing/subscriptions/upgrade-downgrade.md (A; mid-cycle price change, billing-period semantics, proration, credit prorations, pending updates, subscription schedules)
- Zuora — https://knowledgecenter.zuora.com/ (B; portal landing: module decomposition Billing/Payments/Platform/CPQ/Zephr/Revenue/AR/AI + cross-product Entitlements topic; Billing charter sentence "Monetize new offerings, create and manage subscriptions, and invoice customers")
- Maxio — https://www.maxio.com/ (B; product split CPQ/Billing/Usage-Based Billing/Subscription Management/Revenue Recognition/Metrics/AR/Payments; B2B SaaS positioning; G2 Subscription Billing category badges)

Cross-reference within Atlas: research/billing-platform.md (generic spine + joint-review flag), research/membership-billing.md, research/media-subscription-management.md, research/subscription-commerce-platform.md, research/recurring-commerce-management.md, research/renewal-management-platform.md, research/subscriber-management.md, research/utility-billing-platform.md, research/creator-subscription-platform.md (STATUS entries).

**Source-access limitations.** Zuora's knowledge center has moved to a JS portal; the landing page renders (module decomposition + charter sentences) but section/deep pages returned only the landing content on one attempt — Zuora evidence stays at positioning level, no operational claims drawn. Maxio's help docs (docs.maxio.com) were not fetched; Maxio evidence stays at official product-page level. Chargebee's help-docs site (www.chargebee.com/docs) is JS-rendered; the API documentation (apidocs.chargebee.com, explicitly LLM-indexed) was used as the Tier-1 source instead. Per the evidence rules, no precise numeric parameters are asserted except those directly documented in fetched pages (e.g., Stripe's documented 23-hour initial-payment window — kept in these notes only, not in the final document).

---

## Product A — Chargebee (evidence layer A)

Official API documentation, fetched 2026-09-10.

- **Definition sentence**: "A Chargebee subscription connects a customer record to products/services. It describes what the customer has signed up for and how often they're charged for it." Components: a plan-item price, any addon- and charge-item prices, coupons, discounts. "The charges in a subscription are billed via invoices."
- **Subscription status enum** (the lifecycle state machine): `future` (scheduled start), `in_trial`, `active` ("active and will be charged for automatically based on the items in it"), `non_renewing` ("will be canceled at the end of the current term"), `paused` ("will not renew while in this state"), `cancelled` ("canceled and is no longer in service"), `transferred` (business-entity transfer artifact).
- **Term/cycle machinery**: `billing_period`/`billing_period_unit` (day/week/month/year), `remaining_billing_cycles` ("after the billing cycles are exhausted, the subscription is canceled automatically"), `current_term_start`/`current_term_end` ("Subscription is renewed immediately after this"), `next_billing_at`, contract terms, `trial_end`/`trial_end_action` (activate or cancel at trial end), free periods.
- **Scheduled changes**: `has_scheduled_changes`, `changes_scheduled_at`; backdated changes supported under documented prerequisites (accounting-close limits).
- **Payment-failure-driven cancellation**: `cancel_reason` enum includes `not_paid`, `no_card`, `fraud_review_failed`, `tax_calculation_failed`, `currency_incompatible_with_gateway` — the system itself cancels for commercial/compliance reasons.
- **Money state on the subscription**: `due_invoices_count`, `due_since`, `total_dues`, `auto_collection` (on/off — automatic charge vs offline payment), `net_term_days` (B2B invoicing terms), per-subscription `mrr` ("Monthly recurring revenue for the subscription").
- **Catalog**: Product Catalog / Items / Item Prices / Offers / Coupons / Credit Grants / Usage Based Billing as sibling API sections; plan/addon/charge item types; tiered/volume/stairstep pricing models on item prices.
- **Entitlements**: "The entitlement resource establishes a connection between a feature and an item or an item_price… it specifies the scope of access or rights the item or item price has in relation to that particular feature." Feature types: switch/quantity/range/custom with levels (e.g., "20 users", unlimited).
- **Omnichannel**: subscriptions synced from Apple App Store / Google Play Store (`channel` = web/app_store/play_store; in-app subscription resources with their own event vocabulary — renewed/paused/cancelled/revoked with voluntary vs system reasons).
- **Other structure**: consolidated invoicing, customer hierarchies (parent pays for child's invoices), business entities/brands, quotes, estimates, advance invoice schedules, metered billing with pending invoices, simulation tools ("Time Machine" for lifecycle testing).

## Product B — Recurly (evidence layer A)

Official docs, fetched 2026-09-10.

- **Product split** (docs hub): Recurly Subscriptions ("Subscription lifecycle management… plans, billing, payments, and analytics in one platform"), Recurly Commerce (Shopify), Recurly Engage (upsells/retention), Recurly RevRec, Recurly Recover ("A standalone retry engine… plug Recurly's optimized dunning into your existing billing stack").
- **Subscription lifecycle** organized as first-class managed actions: Create / Change / Pause / Postpone / Expire-cancel / Multiple subscriptions per account; subscription dashboard with filters and direct actions.
- **Change subscription** (the amendment machinery): changes to plan, price segment, price, quantity, add-ons; timing options — **immediate** (invoice created now, transaction attempted, failure → dunning), **at next bill date** (pending change, no proration, one pending change retained), **at term renewal**. Immediate changes generate **credit and/or charge invoices** with three calculation options (prorated / full / none); "Only Bill What Changed" bills only the difference when the plan is unchanged; plan changes always full-rebill; documented proration formula (time-remaining over full period); bill-date changes prorate credit for days paid + charge to new date; plan-period changes (monthly→annual) restart the term without proration.
- **Modification enforcement**: merchants can require paid invoices / successful transactions before allowing upgrades or downgrades — payment status gates subscription changes.
- **Expire/cancel**: **cancellation** = customer ends at next bill date or term end (pre-expiry state, retains access, **reactivatable until expiry**); **termination** = merchant ends mid-cycle (direct to expired, no reactivation); **expiry** terminal — "once a subscription is expired, it cannot be reactivated. A new subscription must be created instead." Auto-cancellation on gateway signals that a payment method/mandate is no longer valid. Dunning can be configured to **automatically expire** a subscription when its invoice ends the dunning cycle unpaid.
- **Recurring billing machinery**: invoices with lifecycle, **credit invoices** (separate credit-adjustment invoices), charge/credit adjustments (automatic during subscription billing events or manual), **calendar billing** (consolidate multiple subscriptions into one invoice; align renewals), **subscription terms** (multiple billing periods, end-of-term renewal behavior), manual invoicing with net terms/PO numbers (B2B), taxes (native + Avalara, VAT/GST, location validation).
- **Entitlements**: "Cross-platform Entitlements — create and manage customer access rights, establish effective paywalls, leverage API functionality for detailed entitlement checks."
- **Subscriber wallet**: multiple stored payment methods per account, per-subscription billing-info assignment, fallback methods to reduce involuntary churn.
- **Lifecycle communications**: automated emails across subscription actions, billing events, dunning scenarios; renewal reminders and trial-ending notifications.

## Product C — Stripe Billing (evidence layer A)

Official docs, fetched 2026-09-10 (overview + upgrade-downgrade; overview also fetched in the billing-platform pass 2026-09-06).

- **Definition**: "Subscriptions let customers make recurring payments to access a product or service. When you create a subscription, Stripe automatically generates invoices, attempts payment collection, and manages the subscription status throughout its lifecycle."
- **Lifecycle statuses** (documented table): `trialing`, `active`, `incomplete` (initial payment pending; documented 23-hour window), `incomplete_expired` (initial payment never succeeded), `past_due` (latest finalized invoice failed/unpaid; retries continue), `unpaid` (retries exhausted; subscription remains, payments stop, "Revoke access to your product when the subscription is unpaid"), `canceled` (terminal), `paused` (trial ended without payment method).
- **Access coupling**: "When a subscription becomes `active`, Stripe creates an active **entitlement** for each feature associated with the subscribed product. When a customer accesses your services, use their active entitlements to grant them access." Statuses explicitly guide provisioning: "Understanding these statuses helps you know when to provision access."
- **Automatic recurring charging**: subscription creation generates an Invoice + PaymentIntent; invoices auto-generate each billing period; failed-payment settings determine `past_due` → `canceled`/`unpaid` outcomes after Smart Retries; invoices continue generating in draft during non-collection.
- **Mid-cycle changes**: update subscription items (price/quantity) without recreation; proration applies the new price to the remaining period, previewable; proration can be disabled; **credit prorations** on downgrades/cancellations (two calculation approaches by billing_mode); same-billing-period changes retain billing dates, different-period changes reset the anchor; **pending updates** gate the change on successful payment; **subscription schedules** manage planned future transitions.
- **Cancellation semantics**: cancel immediately, at end of billing cycle, or after a set number of cycles; default cancellation disables new invoices and stops collection of outstanding invoices.

## Product D — Zuora (evidence layer B — positioning + module decomposition)

Official doc portal landing, fetched 2026-09-10 (portal now reachable; deep pages did not render).

- **Zuora Billing charter**: "Monetize new offerings, create and manage subscriptions, and invoice customers."
- **Sibling products under one vendor**: Zuora Payments, Zuora Platform, Zuora CPQ, Zephr ("Optimize digital subscription Journeys"), Zuora Revenue ("Recognize, reconcile, and analyze revenue"), **Accounts Receivable** ("Automate invoicing and collections"), Zuora AI — plus a **cross-product Entitlements topic** ("Explore entitlements for all Zuora product offerings").
- Structural reading (consistent with the billing-platform pass): billing / payments / revenue recognition / AR / CPQ are distinct systems with distinct charters even inside one vendor's monetization suite; entitlements is a first-class cross-product concept.

## Product E — Maxio (evidence layer B — official product pages)

Official site, fetched 2026-09-10.

- Positioning: "Billing and financial reporting for B2B SaaS & AI"; "Subscription and contract billing. Automated invoicing. GAAP & IFRS compliance."
- **Module split**: CPQ; Billing; Billing for AI; Usage-Based Billing ("Metering & Rating… Charge by license, overage, or meter"); Subscription Management ("Self-Serve Billing Portals, Flexible Product Catalog… Spin up plans or custom contracts… Configure pricing, fees, coupons, and upsells"); Revenue Recognition; Metrics and Reporting ("30+ one-click reports including ARR summary and DSO"); AR Management; Payments ("Connect to dozens of payment providers… or run payments through Maxio's built-in payment solution").
- Capability claims: "Recurring, usage-based, or event-triggered. Set renewal timing, prorate mid-cycle, or delay a charge"; "Automated dunning and payment reminders… Track DSO in real time"; multi-entity catalogs/gateways.
- Market-category evidence: G2 badges for "Subscription Billing" category leadership — the market itself treats "subscription billing" as a named product category.

---

## Cross-product Comparison

| Dimension | Chargebee | Recurly | Stripe Billing | Zuora | Maxio | Verdict |
|---|---|---|---|---|---|---|
| Subscription as named first-class object | "subscription connects a customer record to products/services… what the customer has signed up for and how often they're charged" | subscription dashboard; lifecycle actions per subscription | Subscription object with status; "recurring payments to access a product or service" | "create and manage subscriptions" | "Subscription Management" module | **All five → defining** |
| Recurring offer configuration (plan/price) | plan-item price + addon/charge items + coupons/discounts | plans, add-ons, price segments, coupons | product + price attached to subscription | offerings (positioning) | "plans or custom contracts… pricing, fees, coupons" | **All five → defining (the subscription's configuration source)** |
| Automatic recurring invoice generation from the subscription | "charges in a subscription are billed via invoices"; renewal at term end | automated invoicing per billing cycle; subscription terms | "automatically generates invoices, attempts payment collection" | "invoice customers" | "Automated invoicing" | **All five → defining** |
| Lifecycle state machine | future/in_trial/active/non_renewing/paused/cancelled | active → canceled (pre-expiry) → expired; paused; dunning states | trialing/active/incomplete/incomplete_expired/past_due/unpaid/paused/canceled | entitlements topic implies state coupling | renewal timing, dunning | **All five → defining (labels vary; the machine is universal)** |
| Payment-failure handling | cancel_reason not_paid/no_card; auto_collection | dunning management; auto-expiry at dunning end; wallet fallback | past_due → smart retries → canceled/unpaid; draft invoices continue | Payments module separate | "Automated dunning and payment reminders" | **All five → L1 (ubiquitous); depth varies** |
| Mid-cycle amendment + proration | scheduled changes, backdating, term reset rules | immediate/next-bill/term-renewal timing; prorated credit+charge; OBWC | proration, credit prorations, pending updates, schedules | (positioning-level) | "prorate mid-cycle" | **4/5 direct → L1 common mature (not defining: cancel-and-resubscribe model satisfies the core)** |
| Entitlements / access coupling | Entitlements resource (feature × item) | Cross-platform Entitlements, paywalls | entitlements created per feature on activation; status guides provisioning | cross-product Entitlements topic | (not evidenced) | **4/5 → L1 common mature** |
| Pauses / holds | paused state documented | pause subscription (N cycles) | paused status | — | — | **3/5 direct → L1** |
| Calendar billing / consolidation | consolidated invoicing | calendar billing (aggregate/align) | — | — | — | 2/5 → L2 variant |
| B2B invoicing terms (net D, PO, manual collection) | net_term_days, PO, auto_collection off | manual invoicing, net terms, MOTO | send_invoice collection method | (enterprise positioning) | contract billing, AR module | **Common → L1** |
| MRR/ARR/churn analytics | subscription-level mrr attribute | Reporting & Analytics section | — | — | Metrics & Reporting, ARR summary | **Common → L1** |
| Usage-based charging alongside recurring | Usage Based Billing section | usage-based add-ons | usage-based prices/meters | supported | Usage-Based Billing module | **Common → L1; specialist depth = L2** |
| Trials | in_trial state, trial_end_action | trials, trial-ending notices | trialing status, trial settings | — | — | **Common → L1** |
| Self-service customer portal | Self-Service Portal emails; hosted pages | hosted account management | customer portal | — | self-serve billing portals | **Common → L1** |
| App-store subscription sync | Omnichannel (app_store/play_store channels) | — | — | — | — | Single-product explicit → L2 |
| Rev-rec as separate product/module | — | Recurly RevRec | — | Zuora Revenue | Revenue Recognition module | **Adjacent module, not core** |
| AR/collections as separate module | — | — | — | Zuora AR | AR Management module | **Adjacent module, not core** |
| Payments execution | Payments API section | Payment Orchestration section; gateways | Stripe payments stack | Zuora Payments | Payments module / 20+ gateways | **Separate concern; billing decides, payments execute** |
| CPQ upstream | Quotes/Estimates | — | Quotes (billing-platform pass) | Zuora CPQ | Maxio CPQ | **Upstream handoff** |
| Acquisition surfaces (checkout/hosted pages) | Hosted Pages, checkout portal | Hosted Pages, Recurly.js | Stripe Checkout | Zephr (journeys) | PCI-compliant forms | **Common → L1** |

Reading: all five products share one organizing object — the subscription — and one engine — automatic recurring charging from that subscription's terms — governed by one lifecycle state machine. Everything else (amendment depth, entitlements, dunning sophistication, analytics, portals, usage charging, B2B invoicing terms) is layered on with varying emphasis. No product's defining structure depends on usage-based pricing, on any specific status vocabulary, on entitlements machinery, or on any UI layout.

## Canonical Abstraction Hierarchy

### Level 0 — Defining Invariant

**A Subscription Billing Platform is the vendor-side system of record for standing recurring commercial commitments, held on the generic billing spine (billing accounts, charge computation, the invoice as authoritative amount-due record, tracked settlement — the Billing Platform core), whose differentiating core is exactly three jointly-held structures:**

1. **The subscription as the unit of record** — a persistent, identified record binding a customer to a recurring commercial arrangement: what they have signed up for (a plan/price configuration drawn from the vendor's recurring-offer catalog) and how often they are charged (billing period/cadence). It persists across billing cycles and is the anchor to which charges, invoices, changes, and money state attach. Remove → the generic Billing Platform (charges from catalog/usage/one-time; no standing commitment object).
2. **Subscription-driven recurring charging** — the system automatically generates the recurring charges and invoices from the subscription's terms on its cadence, cycle after cycle, including renewal at term end, until the subscription ends. Remove → one-off invoicing or a manual charge scheduler.
3. **The subscription lifecycle state machine** — the subscription moves through managed states (trial → active → payment-failure states → renewal / non-renewing / paused / canceled-expired), transitions driven by payment outcomes and by customer/administrator actions, with defined semantics for ending (end-of-term cancellation vs immediate termination), reactivation before expiry, and what happens when payment finally fails. Remove → a charge scheduler with no managed relationship.

**Jointly-held load-bearing**: (1 alone = a contract/plan record in a CRM or a price list; 2 without 1 = a recurring-payment scheduler — a payment feature, not a billing system; 3 without 1+2 = a status board; 1+2 without 3 = auto-charging with no managed relationship; 1+3 without 2 = subscription records with no money engine). The billing spine beneath is shared with the generic leaf — remove the spine and only a subscription registry remains.

**Historical / market-sample check**: paper-era subscription operations (magazine/publisher subscription offices, record clubs, gyms — subscriber records with renewal terms, renewal notices, recorded payments, continued service as the fulfillment) satisfy all three legs without any software-era feature; early payment-gateway "recurring billing" modules (store card, charge monthly until cancelled) satisfy the core with a degenerate single-offer catalog and no amendments. The definition is not SaaS-era-overfit; trials, portals, entitlements, proration, and MRR dashboards are modern common structure, not the definition.

### Level 1 — Common Mature Structure

- **Catalog breadth** — plans with recurring price × interval, add-ons, one-time charges, coupons/discounts, trials, setup fees; tiered/volume/stepped pricing; multi-currency.
- **Mid-cycle amendment machinery** — plan/price/quantity changes without cancel-and-recreate; proration (credit + charge invoices, prorated/full/none options); change timing (immediate / at next bill date / at term renewal); scheduled/pending changes; preview of the resulting invoice.
- **Dunning & involuntary-churn machinery** — retry schedules, dunning customer communications, payment-failure states, configurable terminal outcomes (auto-cancel / hold open), stored-payment-method fallback.
- **Entitlements / access coupling** — features mapped to plans/prices; entitlement checks; subscription status as the provisioning signal (grant on active, revoke on lapse/cancel).
- **Customer self-service portal** — payment-method update, plan changes, cancellation, invoice access.
- **Recurring-revenue analytics** — MRR/ARR, churn, retention, cohort and recovery reporting.
- **B2B invoicing machinery** — net terms, PO numbers, manual/offline collection, account hierarchies with parent billing and invoice rollup, consolidated/calendar billing.
- **Usage-based charging alongside recurring charges** — metered add-ons billed in arrears.
- **Lifecycle communications** — renewal reminders, trial-ending notices, subscription-change and dunning emails.
- **Tax handling** on invoices (native or partner-integrated; depth varies).
- **Integration fabric** — APIs, webhooks/events on lifecycle transitions, exports.
- **Acquisition surfaces** — hosted checkout/payment pages, pricing tables (often co-sold with the billing core).

### Level 2 — Variant / Optional Structure

- **Commercial-model emphasis**: pure plan-based recurring vs usage-heavy hybrid vs prepaid credits vs enterprise commitments/contract terms (multi-year, fixed cycles, renewal rules).
- **B2B negotiated-contract posture vs self-serve plan posture** (quote-to-cash depth; CPQ integration).
- **Retention-first packaging** — cancel-flow/save-offer machinery, engagement prompts, churn analytics as the headline (Recurly's positioning).
- **Finance-operations packaging** — rev-rec, SaaS metrics, AR, DSO reporting bundled around the billing core (Maxio's positioning; Zuora Revenue/AR modules; Recurly RevRec).
- **Omnichannel/app-store subscription sync** — first-party web subscriptions alongside store-billed subscriptions reconciled in one platform.
- **Merchant-of-record posture** — some vendors take on tax/compliance/payment liability as reseller (market-known posture; not directly sampled — reasoning strength).
- **Industry packaging** — the same machinery sold into SaaS, media (via journey/entitlement layers like Zephr), AI/cloud, IoT, e-commerce add-ons.
- **Deployment** — SaaS vs API-infrastructure; sandbox/simulation tooling.

### Level 3 — Vendor-specific (research notes only)

- Chargebee: exact status vocabulary (`future`, `in_trial`, `non_renewing`, `transferred`); documented 900-subscriptions-per-customer maximum; `cancel_reason` enum values; subscription-level asynchronous `mrr` attribute; Time Machine simulation; business-entity transfer semantics; backdating prerequisites tied to accounting-close day limits.
- Recurly: "Only Bill What Changed" (auto-enabled on sites created after 2017-06-30); credit invoices as separate documents; the documented proration formula (denominator = full plan period); calendar billing's Aggregate Invoices vs Aligning Renewals modes; modification-enforcement settings; Subscriber Wallet fallback; dunning-driven auto-expiry; the rule that past-due invoices are not auto-failed on non-dunning expiry.
- Stripe: full status vocabulary (`incomplete_expired`, `past_due`, `unpaid`, `paused`); the documented 23-hour initial-payment window; Smart Retries as branded revenue-recovery; `payment_behavior`/`collection_method` configuration; billing_mode-dependent credit-proration approaches; pending updates; subscription schedules; billing-cycle-anchor reset semantics.
- Zuora: product-family split (Billing/Payments/Platform/CPQ/Zephr/Revenue/AR/AI) and charter sentences; cross-product Entitlements topic.
- Maxio: module brand split; "30+ one-click reports including ARR summary and DSO"; 20+ gateways claim; G2 Subscription Billing category badges.

## Vendor-specific Findings (summary)

See Level 3. None of these enter the canonical document; they illustrate the space rather than define it.

## Rejected Findings

1. **"Subscription billing = the generic Billing Platform with a marketing label."** Rejected as an alias outcome. The subscription is not merely a charge source here — it is the unit of record whose lifecycle drives the money engine, and every sampled product organizes its entire object world around it (subscription dashboards, subscription-level states, subscription-level dues and MRR, subscription-scoped actions). The generic leaf's own sample proves the complement: usage-first (Metronome) and telco (BRM) billing exist with no subscription object at all. Distinct Type, shared spine.
2. **"Entitlements/access gating is definitional."** Rejected for L0. Early recurring-billing modules charged and invoiced with access gating left entirely to the merchant application; the sampled evidence shows entitlements as a first-class *addition* in mature products (4/5), not a precondition. L1.
3. **"Mid-cycle proration is definitional."** Rejected for L0. A cancel-and-resubscribe model (the early-gateway form) is recognizably subscription billing without amendment machinery. L1.
4. **"Subscription billing includes payment execution."** Rejected. Every sampled vendor treats payment execution as a separate concern (separate modules, gateway integrations, or a separate product); Recurly even sells dunning/recovery as a standalone attachable product (Recurly Recover). Billing owns the amount due and its resolution state.
5. **"Subscription billing includes revenue recognition."** Rejected as core. RevRec ships as a separate product/module in three of five samples (Recurly RevRec, Zuora Revenue, Maxio Revenue Recognition).
6. **"MRR/ARR analytics are definitional."** Rejected. Ubiquitous but reporting-layer; paper-era and early-software subscription operations satisfy the core without them. L1.
7. **"Subscription billing is consumer-facing."** Rejected. The B2B pole is first-class (net terms, PO numbers, manual collection, account hierarchies, contract terms, quotes) — Maxio and Zuora are B2B-first.
8. **"A billing cycle/batch run is the organizing rhythm."** Partially rejected. In this Type the cadence is anchored to each subscription's own term (anniversary billing is the default pattern), with calendar billing/consolidation as an optional alignment layer. The global batch cycle is the generic billing platform's pattern.

## Boundary Findings

1. **vs Billing Platform (§08 sibling) — JOINT REVIEW DISCHARGED: keep-both RATIFIED.** The generic leaf is the model-neutral charging engine: its L0 (billing accounts → charge computation → invoice as authoritative amount-due record → tracked settlement) deliberately treats subscription as one charge source among usage, one-time, prepaid, commitments, hybrid. This leaf is the subscription-as-center specialization: the subscription object is the unit of record, its lifecycle state machine governs the money path, and the recurring charge schedule derives from the subscription rather than from a generic rating event. Removal tests: remove the subscription layer from this Type → the generic Billing Platform remains; add a subscription object to the generic spine → this Type. Consistent with the utility-billing pass's ratified pattern (generic spine + domain machinery = separate leaf). The generic pass's L1 items "entitlements/status linkage" and "billing cycles" reappear here with different weight: entitlements mature into the access-fulfillment layer, and the cadence anchors to the subscription rather than a global cycle.
2. **vs membership-billing (§25) — flag DISCHARGED: keep-both.** The recurring-charging machinery genuinely overlaps (stored methods, auto-charge, dunning, plan changes, proration — both territories document all of it). The seam is the billed relationship and the fulfillment structure: membership billing charges dues for BELONGING to an organization, with billing→standing coupling (good standing/suspension/benefit gating) as a defining leg and a member registry as the center; this Type charges for a product/service/access commitment, with a product/plan catalog as the configuration source and the organization as vendor billing external customers. The analogous coupling here (billing state → product access) is L1 machinery, not the defining standing relationship. Both documents stand.
3. **vs media-subscription-management (§27) — flag DISCHARGED: keep-both.** Confirmed from this side: the sampled products are industry-horizontal (SaaS, AI, cloud, media, e-commerce all named markets; Maxio is B2B-SaaS-first; Chargebee/Stripe serve any digital seller), carrying no media product catalog or content-access binding of their own — entitlements here are generic feature/plan mappings, not media-content grants. Media subscription management is the media operator's system of record with the access-binding leg and media catalog. The market deliberately spans the seam (Stripe under Piano/Memberful, Zuora under Zephr) — packaging/integration evidence, not alias evidence, exactly as that pass predicted.
4. **vs subscription-commerce-platform / recurring-commerce-management (§05.16) — seam CONFIRMED.** Sharpest structural seam in the family: subscription commerce executes each cycle as a goods transaction (charge → order → fulfillment handoff; skip/swap/ship); subscription billing executes each cycle as a money-and-access event (invoice → charge → entitlement continues). A subscription billing platform has no order/fulfillment objects; a subscription commerce platform's unit of record is the commitment to receive goods. The "digital access" program shape in commerce platforms is the acknowledged overlap zone.
5. **vs creator-subscription-platform — seam CONFIRMED.** Creator platforms center the fan→creator support relationship (creator-authored offer, fan-facing surfaces, platform-managed or creator-owned payments); this Type centers the operator-side billing relationship with business customers (invoices, net terms, account hierarchies, B2B contracts). A creator platform's subscription machinery is the fan-facing fulfillment wrapper; this Type is the money engine behind any vendor.
6. **vs renewal-management-platform (§07) — seam CONFIRMED.** Auto-renewal here is a mechanical default of the subscription object (renew at term end unless cancelled/non-renewing) — there is no renewal decision record, no forward renewal book, no retention-metrics decision object. Renewal management centers the renewal decision event; this Type executes the money consequence. Consistent with that pass's own boundary statement.
7. **vs subscriber-management (§19 telecom) — seam CONFIRMED.** Money computation (what is owed, invoiced, settled) vs who-has-what-and-is-active (service entitlements and commercial lifecycle in operator BSS). Subscription status gates billing here; in telecom BSS the subscriber record gates service. Telecom charging/billing remain industry leaves.
8. **vs utility-billing-platform (§19/§08 pattern)** — same family pattern: generic spine + domain machinery. Utility billing's differentiating leg is the metered-consumption basis and service-state coupling; this leaf's is the subscription object and its lifecycle. No conflict.
9. **vs payment gateway / processing / orchestration** — billing decides and records what/when/how much and tracks resolution; payments execute. Direct evidence: Maxio "connect to dozens of payment providers… or run payments through Maxio's built-in payment solution" (payments as a separate, optional module); Recurly ships Payment Orchestration as a separate docs section and Recover as a standalone attachable product.
10. **vs Invoicing Application (§08)** — invoicing surfaces inside subscription billing products are capabilities (Recurly's invoice management, Stripe Invoicing). The invoicing Type centers document authoring; this Type centers the subscription engine that generates invoices automatically at scale.
11. **vs CPQ / Order Management** — upstream one-way handoff: quotes/contracts establish the commercial agreement that the subscription instantiates (Maxio CPQ and Zuora CPQ are separate products; Chargebee Quotes/Estimates are adjacent API sections).
12. **vs Revenue Recognition / AR / Accounting** — downstream. Separate modules/products across the sample; billing feeds them finalization events.

## Uncertainties

1. **Zuora object model** (accounts → subscriptions → amendments → invoices; billing-run mechanics) unverified — positioning + module decomposition only. The canonical model does not depend on it.
2. **Maxio operational mechanics** (object model, dunning configuration, proration options) not fetched — product-page evidence only; no operational claims drawn.
3. **Chargebee help-docs depth** (dunning configuration UI, retention flows) JS-rendered — API-doc evidence used; UI-level mechanics not asserted.
4. **Merchant-of-record posture** (Paddle-class) reasoned from market knowledge, not sampled — held at variant strength, excluded from the final document's specifics.
5. **Exact numeric parameters** (retry counts, dunning cadences, trial defaults, subscription limits) documented only where directly fetched (Stripe's 23-hour window; Chargebee's 900-subscription maximum) — kept in these notes; none asserted in the final document.
6. **Prepaid-credits/commitments depth** in this Type (vs the generic billing leaf's coverage) not systematically compared — worded as variant.
7. **Regional e-invoicing/compliance machinery** in subscription billing (vs the generic leaf's L2 note) not compared — softly worded.

## Final Synthesis

The Subscription Billing Platform is the **vendor-side system of record for standing recurring commercial commitments**. It stands on the generic Billing Platform spine — billing accounts, charge computation, the invoice as the authoritative lifecycle-managed amount-due record, tracked settlement — and its differentiating core is the subscription layer: the subscription as a persistent, identified unit of record (customer × recurring plan/price configuration × billing cadence); subscription-driven automatic recurring charging that generates invoices cycle after cycle and renews at term end; and a managed lifecycle state machine (trial → active → payment-failure states → renewal/non-renewing/paused/canceled-expired) whose transitions are driven by payment outcomes and customer/admin actions, with defined cancellation, reactivation, and failure-termination semantics. Around this core, mature products add catalog breadth (add-ons, coupons, trials), mid-cycle amendment machinery with proration, dunning and involuntary-churn recovery, entitlements coupling billing state to product access, self-service portals, recurring-revenue analytics, B2B invoicing terms, usage-based charging, lifecycle communications, and integration fabric. The Type is industry-horizontal (SaaS, AI, media, cloud, e-commerce add-ons), spans self-serve and B2B-contract postures, and is distinct from the generic Billing Platform (model-neutral engine), subscription commerce (goods per cycle), media subscription management (media operator system of record), membership billing (dues for belonging), and the payments/AR/rev-rec Types it feeds. The definition survives the paper-era subscription office and the early recurring-billing module, not just the modern SaaS stack.
