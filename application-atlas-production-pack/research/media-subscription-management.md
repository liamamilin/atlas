# Research Notes — Media Subscription Management

Research date: **2026-09-08**

## Research Goal

Understand what "Media Subscription Management" is as an Application Type: what system sits inside a media company (publisher, news organization, streaming/media brand) to run its subscription business — what objects exist, how a subscription lives and dies, where money is handled, how paid access to content is granted and enforced, and how this Type differs from neighboring Types (magazine periodical management, media audience management, subscription billing platforms, subscription commerce, streaming platforms, membership systems).

## Initial Boundary (pre-research hypotheses)

1. Working hypothesis: the operator-side business system that manages subscriptions sold by a media company — plans/products, subscriber records, subscription lifecycle (start/renew/change/cancel), billing/payment, and the entitlement that unlocks content.
2. Nearest neighbors to test:
   - Magazine Periodical Management (§27 sibling; processed 2026-09-08 with a pre-hung flag expecting heavy overlap — its circulation machinery was described as "subscription management specialized to a periodical")
   - Media Audience Management (§27 sibling; processed 2026-09-08, pre-hung flag: seam = audience population/management-loop center vs subscription product/billing-lifecycle center; Pelcro named straddling pole)
   - Subscription Billing Platform (§08, unprocessed) — horizontal billing machinery
   - Subscription Commerce Platform (§05.16, processed) — recurring *goods* commerce
   - Video/Music Streaming Platform, Podcast Platform (§27 siblings, unprocessed) — consumer consumption surfaces
   - Membership Management System (§25, processed) — organizational membership/dues
   - Newsletter Marketing Platform (§27-adjacent, processed) — email publication; paid subscriptions noted there as standard-NOT-definitional
3. Name ambiguity risk (like the media-rights pass): "media subscription management" could be misread as consumer-side "manage my subscriptions" trackers — but the §27 placement (beside Royalty Management, Media Audience Management) and the market both support the operator-side business-system reading.

## Research Questions

1. What are the core objects? (product/plan/offer/term/entitlement/resource/SKU…)
2. What is the subscription's lifecycle and who drives it (subscriber self-service, CSR, automation)?
3. Where does money live — in-product billing, delegated (Stripe/Zuora), or both? Is the money cycle definitional if implementation varies?
4. How is paid access expressed and enforced (entitlement vs SKU vs paywall rule)? Is the access-binding what makes this Type "media"?
5. Do print/physical subscriptions belong (Piano Print, Pelcro fulfillment) — and if so, what separates this from the magazine Type's circulation machinery?
6. What is the consumer-facing surface vs the operator surface?
7. What roles exist (subscriber, CSR/customer care, marketing/growth, admin)?
8. Where exactly are the seams vs the pre-hung flags?

## Representative Products

| Product | Tier/philosophy | Why sampled |
|---|---|---|
| Piano (Subscriptions) | Enterprise publishers; conversion-experience suite with in-product subscription management + billing (Stripe Billing option); print module | Strongest Tier-1 docs; the paywall-centric philosophy |
| Arc XP Subscriptions (Washington Post's platform) | Enterprise news; Subscriptions as a module of a full publishing platform | Media-native; documents Retail (products/offers/campaigns), Identity, Paywall, entitlements, CSR admin separately |
| Zephr (by Zuora) | Enterprise media; "subscription experience platform" — experience/decisioning pole; billing delegated to Zuora Billing | The delegation pole: proves billing-in-product is not definitional |
| Pelcro | Mid-market publishers + membership orgs; all-in-one (paywalls, entitlements, fulfillment, billing, portal) | The named straddling pole (audience pass); mid-market tier |
| Memberful | Indie creators/publishers/newsletters; membership-first, own-Stripe, permission-sync into WordPress/Discord | Indie tier; access-execution-by-integration pole |

Sample covers: market representation (all are prominent in the media/publisher subscription market), documentation completeness (Piano + Arc XP Tier-1), different product philosophies (experience-first / platform-module / delegation / all-in-one / membership-first), different customer tiers (enterprise → mid-market → indie).

## Sources

- Piano Documentation (docs.piano.io): /en/subscriptions; /en/subscriptions/getting-started-with-subscription-management-billing; /en/subscriptions/manage-subscriptions; /en/subscriptions/print — fetched 2026-09-08 (Tier 1)
- Arc XP Documentation (docs.arcxp.com): /en/products/subscriptions.html tree; arc-xp-subscriptions-retail/managing-products; arc-xp-subscriptions-paywall/managing-paywall-entitlements — fetched 2026-09-08 (Tier 1)
- Zephr product page (zephr.com → zuora.com "Zephr: AI Paywalls for Media and Publishers") — fetched 2026-09-08 (Tier 2)
- Pelcro (pelcro.com root: product/nav + use-case surfaces) — fetched 2026-09-08 (Tier 2)
- Memberful (memberful.com root) — fetched 2026-09-08 (Tier 2)
- STATUS.md pre-hung flags: magazine-periodical-management (2026-09-08), media-audience-management (2026-09-08); processed-adjacent seams: subscription-commerce-platform (2026-09-08), media-rights-management (2026-09-08), newsletter-marketing-platform (2026-09-08)

### Source-access limitations

- docs.zephr.com unreachable (transport error this pass; also failed ×2 in the media-audience pass). Zephr evidence = product/FAQ page only → capability-level assertions only; no operational detail claimed.
- Pelcro deeper doc pages not fetched (one attempted path 404'd; root page carried module-level evidence). No precise Pelcro operational claims made.
- Memberful docs not fetched; root product page only. No precise operational claims.
- Per the evidence rules: no precise numbers, time windows, or default settings from these weaker sources are used in the final document; the one precise number observed anywhere (Arc XP's "roughly ten products" catalog best practice) stays here in the Research Notes.

## Product Observations

### Piano (Subscriptions) — evidence layer A (Tier-1 docs)

- Product modules: Composer (paywall/experience), Identity Management, **Subscription Management + Billing**, Subscription Insights, ESP (email), plus Amplifier/Analytics/Audience elsewhere.
- Canonical object chain documented in "Getting Started with Subscription Management + Billing":
  - **Resource** — "used to control the content that you are gating. Resources act as tokens that allow users to view your content. Every subscriber to your site must have access to a resource, by definition – that access distinguishes the subscriber from non-subscribed users." (entitlement leg, near-verbatim)
  - **Term** — "define the 'terms' of the deal you are striking with your audience… a mutual agreement that you will provide access to a resource (and therefore your content) in exchange for a fee." Billing configuration: **Subscription** ("access to the resource continues for an interval of time before the user renews") vs **Fixed time** ("does not have a renewal option… one-off products"). Other term kinds: external service, registration, gift, custom.
  - **Offer** — "simply a collection of terms" presented to the user, who picks one.
- Subscription Management + Billing module surface: Resources, Terms, Upgrade options, Offers, Stripe Billing, Promotions, Churn Prevention, Site Licensing, Checkout flows, Email Manager, Action Manager, Webhooks, Localization, APIs, My Account, Payment Providers, Print, Reports, Manage Subscriptions, User Access & Admin.
- Manage Subscriptions (CSR operations): creating subscriptions for new or existing users, disputed transaction status, importing dynamic subscriptions, **shared subscriptions**, **subscriptions with a future start date**.
- **Print** module: Print Address Collection and Delivery Zones, Print Subscription Confirmation (PSC), Print Subscription Emails, Print Users, print collection-address editing, exporting print address lists → print subscriptions are a first-class record type inside the same system (physical delivery machinery), not a separate world.
- Stripe Billing documented as an external billing engine under Piano — money machinery can be delegated while subscription state stays in Piano.
- Churn Prevention, Promotions, Upgrade options → retention/change machinery is a named module layer.

### Arc XP Subscriptions — evidence layer A (Tier-1 docs)

- A named product "Subscriptions" inside the Arc XP publishing platform (alongside Composer/PageBuilder content machinery) → confirms the Type exists as the business layer of a media platform, distinct from content creation/delivery.
- Four documented sub-systems:
  - **Retail**: Products (name, SKU uneditable after creation, description, product image, prices; status Published/Draft/Archived; "allow associate subscribers" for family/group sharing; seasonal scenario: monthly recurring payments May–July, "allowing your customers to renew or cancel each time"), Offers, Campaigns, **Group packages**.
  - **Identity**: customer identity accounts, account management incl. CSR perspective.
  - **Paywall**: paywalls, rulesets, rules, **entitlements**, Edge Content Protection, Vindicia (payment) integration.
  - **Customer Service Admin portal**: "Managing subscriptions" for CSRs.
- **Entitlements** ("Managing paywall entitlements"): "At Arc XP, entitlements determine the content access granted when your customers buy a subscription. Entitlements categorize sections, sites, and content types, separating product SKUs from paywall controls. Each product might have multiple entitlements, but a paywall rule typically uses one entitlement to govern access." Scenario: *Basic News Access* vs *Premium Content Access*; paywall rules specify when content is restricted and which entitlements bypass.
- Settings: payment provider setup, tax rates, product currency, **failed payment retry optimization**, offer categories/templates, CDP user segments, authentication providers, password policy.
- Themes: "Subscription and Identity blocks" — the consumer-facing checkout/account surfaces are platform components.
- Catalog-shape note (product-specific): best practice "roughly ten items" in the subscription product catalog.

### Zephr (by Zuora) — evidence layer A-page/B (Tier-2 product page; docs unreachable)

- Self-label: "The Subscription Experience Platform That Drives Conversion and Growth"; "Zephr by Zuora" (ownership consolidation signal).
- Core surface: drag-and-drop **rules builder** (decision nodes), AI paywall optimization (soft/metered/hard/dynamic paywalls), personalized subscriber journeys, first-party data capture/activation.
- **Corporate Subscription Management** (B2B subscriptions with access controls) and **Dynamic Offers** module that "integrates directly with **Zuora Billing**" — billing explicitly external/delegated; Zephr holds the experience + access decisions, Zuora Billing holds the money.
- FAQ confirms: paywall types (soft/metered/hard/dynamic); integrations with CMS/analytics/billing; IAM features (login rules, social sign-in, passwordless, MFA, share detection).
- Evidence caution: no operational docs → all Zephr-derived claims in final doc stay capability-level.

### Pelcro — evidence layer A-page/B (Tier-2 root page; module-level)

- Self-label: "Subscription and Membership Management Software… Recurring billing, paywalls, member data, and access — built for the way publishers and membership orgs actually work."
- Module nav (verbatim labels): Subscriptions & Paywalls — *Paywall software (metered and premium gating)*, *Subscriber services (manage the full lifecycle)*, *Entitlement management (plan-based access control)* (URL slug "digital-rights-management"), *Fulfillment management (print + digital delivery)*, *Client portal (self-service for subscribers)*; Payments & Billing — *Payment processing (multi-gateway, multi-currency)*, Invoice automation, Accounts receivable, Accounts payable, Deferred revenue recognition (GAAP/IFRS); Identity & Trust — *Authentication (passwordless, SSO, social)*, USPS address verification.
- Industries: Magazines, Newspapers, Media billing, Nonprofits, Associations → membership/dues and content subscriptions run on the same machinery (straddle confirmed).
- Use-case surfaces: digital & physical subscriptions (metered paywall UI, recurring billing with "smart retries", print & digital lifecycle dashboard), memberships & communities (tiers, dues, auto-renew), donations, e-commerce/merch, complex metered usage billing, free & paid newsletters, **group licences & enterprise** (seats, SSO, domain-based access).
- AI agents layered on the lifecycle (AI Billing "autonomous dunning + revenue recovery", AI customer service for subscriber resolution) — era machinery, capability layer.
- Straddle confirmed: this is one product centering subscription lifecycle + billing while also carrying audience/membership surfaces — matches the audience pass's prediction.

### Memberful — evidence layer A-page/B (Tier-2 root page)

- Self-label: "Build a membership that's truly yours — sell subscriptions, share content, and connect with your audience, all on your own website or app." Audiences: creators, independent publishers ("writers, journalists, and newsrooms"), communities.
- Philosophy: ownership/white-label (brand on own domain), **own Stripe account** (billing delegated), WordPress plugin + integrations (Discord, Mailchimp, Kit) that "sync members, permissions, and more" → access enforcement executed by the destination systems via permission sync.
- Member management: subscriptions and refunds, private notes, unlimited staff accounts, acquisition insights; checkout: one-click, free and paid trials, coupons/discounts, group subscriptions, international payments; content surfaces: newsletters, podcasts, digital downloads, community content.
- Confirms the indie pole: same object chain (plans → member → subscription → access grant), executed through integrations rather than a built-in paywall.

## Cross-product Comparison

| Dimension | Piano | Arc XP Subscriptions | Zephr (by Zuora) | Pelcro | Memberful |
|---|---|---|---|---|---|
| Subscription product/offer catalog | Resources + Terms + Offers | Products (SKU) + Offers + Campaigns + Group packages | Dynamic Offers (plans/rate plans via Zuora) | Plans/tiers (digital+print, membership, usage) | Plans (monthly/annual/custom, group) |
| Entitlement/access object | Resource = access token (definitional per docs) | Entitlement object, separate from SKU; paywall rules consume it | Rules-builder access decisions (capability level) | Entitlement management ("plan-based access control") | Permission sync to WordPress/Discord/podcast feeds |
| Subscriber identity | Identity Management module | Identity accounts (CSR-manageable) | IAM (login rules, social, passwordless, MFA) | Authentication (passwordless, SSO, social) | Sign-in (password or link) |
| Subscription lifecycle ops | Manage Subscriptions: create, shared, future-start, disputed transactions | Customer Service Admin: managing subscriptions | (not documented here) | Subscriber services: "manage the full lifecycle" | Subscriptions and refunds, staff accounts |
| Money machinery | In-product billing OR Stripe Billing | Payment provider config; tax/currency; failed-payment retries; Vindicia integration | Delegated to Zuora Billing | Full stack: payment processing, invoices, AR/AP, deferred revenue | Delegated to own Stripe |
| Renewal/retention layer | Churn Prevention, Promotions, Upgrade options | Campaigns; failed-payment retry optimization | Win-back campaigns, dynamic paywalls | Smart retries, pre-dunning, save offers | Coupons/discounts |
| Print/physical delivery | Print module (addresses, zones, confirmations) | (not observed in fetched pages) | (not observed) | Fulfillment management (print + digital), USPS verification | Digital downloads only |
| Consumer self-service | My Account | Themes identity/subscription blocks; account management | Personalized journeys | Client portal | Member accounts on own domain |
| B2B/group | Site Licensing | Group packages; associated subscribers | Corporate Subscription Management | Group licences, seats, SSO | Group subscriptions |
| Analytics | Subscription Insights; reports | (CDP segments; not deep-documented here) | Dashboards, funnel analytics | Reporting/analytics surfaces | Acquisition insights |

### Synthesis across the table (evidence layer B)

All five products independently realize the same four-part skeleton:

1. a purchasable **access product/offer** (catalog with pricing and billing period),
2. a **subscription instance** held by an identified subscriber with a managed lifecycle (acquire → active/renewing → change → cancel/end; CSR tools + self-service),
3. a **recurring commercial cycle** against that instance (renewal charges, payment collection, failed-payment handling, refunds/receipts) — with the money engine either in-product (Pelcro, Piano-native, Arc XP-native) or delegated (Stripe under Piano/Memberful, Zuora under Zephr),
4. a **content-access binding** (entitlement/resource distinct from the SKU, consumed by the media product's access enforcement — paywall rules, permission sync, or physical delivery of print).

Identity/registration machinery is adjacent-everywhere (all five) but not what defines the Type. Paywall experience machinery (metering, AI decisioning, journey builders) is the distinctive *modern* layer on two poles (Piano, Zephr) but absent as a center on the others (Memberful syncs permissions; Pelcro's center is the lifecycle+billing stack) → capability, not invariant.

## Canonical Model

### L0 — Defining Invariant (four jointly-held structures)

**The media company's subscription business system of record, whose defining core is exactly four jointly-held structures:**

1. **The purchasable access product of record** — subscription products/plans/offers configured with price and billing period/term, held as the catalog the business sells from (Piano resource+term+offer; Arc XP product+price+offer+campaign; Zephr dynamic offers; Pelcro plans/tiers; Memberful plans). Remove → a subscriber list with no sellable offering.
2. **The subscriber's subscription instance lifecycle** — an identified subscriber holds subscription instances that advance acquire (incl. trial/gift/group/future-start variants) → active → renew → change (upgrade/downgrade/pause/share) → cancel → end/lapsed, with the system of record holding the subscription state and driving renewals; CSR and subscriber self-service both operate it. Remove → one-time sales/order processing, or a CRM.
3. **The recurring commercial cycle run against the subscription** — renewal charging and payment collection (via in-product machinery or connected payment/billing engines), failed-payment retry/dunning, refunds and receipts/invoices; the money cycle is bound to the subscription record even where the ledger is external. Remove → free registration/entitlement grants, not a subscription business.
4. **The content-access binding (entitlement)** — the subscription determines what the holder can access of the media product (articles/sections/sites; streaming/audio catalogs; print delivery), expressed as an access grant distinct from the SKU and consumed by the media product's enforcement (paywall rules, permission sync, physical fulfillment). Remove → horizontal subscription billing (Subscription Billing Platform territory); this leg is the media binding.

**Jointly-held is load-bearing:**
- 1 alone = a pricing page/catalog
- 2 alone = subscriber CRM
- 3 alone = subscription billing engine (§08 territory)
- 4 alone = paywall/access-control tooling
- 1+2 without 3+4 = membership directory
- 1+3 without 4 = horizontal subscription billing
- 1+4 without 3 = free registration/access grants
- 2+3 without 4 = generic (non-media) subscription management
- 2+4 without 3 = freemium access without a business

**Domain binding:** what is sold is ongoing access to a media company's content/product (news, journalism, streaming, audio, print delivery). Remove → horizontal subscription management.

**Historical check (§24) — passed.** Paper-era newspaper/magazine subscription office: rate/term offerings (annual, monthly) + subscriber cards with term start/renewal/cancel + payment records and renewal notices + the delivered paper itself as the "access" — satisfies all four legs at analog level (leg 4 = delivery of the publication). Streaming-era and app-store-era media subscriptions satisfy legs as-is. The definition names no paywall, no metering, no registration wall, no AI decisioning, no email deliverability — all era machinery of the current digital-dominant implementation.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Subscriber identity/registration machinery (email-based accounts, SSO/social/passwordless, password policy) — present 5/5 as a companion module
- Paywall / access-decision layer (metered, hard, freemium, dynamic/AI-optimized; rules builders) — the modern signature surface on the experience-led poles
- Checkout and offer presentation (checkout flows, campaigns, coupons/promotions, trials, gift terms)
- Churn/retention machinery (churn prevention, failed-payment retries/dunning, win-back/save offers, pre-dunning reminders)
- Upgrade/downgrade with proration; pause; shared/group subscriptions (family sharing, site licensing, group packages, seats)
- Consumer self-service account (My Account / client portal: plan, renewal, payment method, invoices, cancel)
- CSR console (search subscriber, adjust subscription, comp/grant, cancel/refund, reason codes)
- Revenue reporting/analytics (MRR-class reporting, conversion funnels, churn/subscription insights, revenue recognition on the deepest pole)
- API/webhooks/SDK integration fabric ( entitlement checks called by the media product; events out to marketing stack)
- Consent/privacy and tax/currency/localization settings

### L2 — Variant / Optional Structure

- Print + digital subscription bundles with physical fulfillment (addresses, delivery zones, confirmations) — publisher variant (Piano Print, Pelcro fulfillment); digital-only poles lack it
- Membership/dues posture (tiers, perks, community access) — the association/nonprofit/creator straddle (Pelcro industries, Memberful)
- Usage/metered billing models (Pelcro complex services) — edge variant beyond flat/recurring access
- B2B/group licensing as a dedicated motion (Zephr corporate subscriptions; Piano site licensing; Arc XP group packages)
- App-store-mediated billing (mobile SDK commerce module in Arc XP) — implementation variant of the money cycle
- Donations/recurring giving on the same rails (Pelcro nonprofits)
- AI agents for dunning/support/offer decisioning — era-current implementations of L1 layers
- Newsroom/publisher-suite embedding (Arc XP Subscriptions inside the Arc XP platform) — packaging variant

### L3 — Vendor-specific (kept out of the final document)

- Piano's exact object vocabulary (Resource/Term/Offer; "fixed time" vs "subscription" billing kinds; PSC print confirmations)
- Arc XP's SKU immutability, entitlement-id scheme, "roughly ten products" catalog guidance, Edge Content Protection, Vindicia partnership, associated-subscriber cap
- Zephr's "50+ decision nodes", "30+ extensions" claims (marketing-page numbers)
- Pelcro's AI agent suite names (AI Billing/AI Orchestrator…), SOC 2 posture marketing
- Memberful's Patreon ownership, migration services, "choose what you pay"
- All precise numbers/defaults stayed out of the final document per evidence rules.

## Vendor-specific Findings (explicit list)

- Piano: Resource is *defined* as the access token ("every subscriber … must have access to a resource, by definition") — the clearest single-vendor statement of the entitlement leg; treated as Tier-1 evidence for the leg, not as a universal vocabulary.
- Arc XP: entitlements explicitly "separat[e] product SKUs from paywall controls" — the same conceptual separation with different vocabulary; strong Tier-1 support.
- Zephr: existence proves billing-delegation is a full product philosophy (experience layer + Zuora Billing) — supports keeping the money-cycle leg implementation-neutral.
- Pelcro: the only sampled product whose center explicitly spans subscription + membership + dues on one platform — the straddling pole predicted by the media-audience pass, confirmed.
- Memberful: access enforcement fully externalized to destination systems via permission sync — supports keeping "enforcement mechanism" out of the definition (the binding, not the paywall, is the invariant).

## Rejected Findings

- "Paywall is the defining structure" — rejected. Metering/hard/dynamic paywalls are the current dominant *implementation* of the access binding on news poles; print-era and creator-membership realizations have no paywall at all. The invariant is the access binding, not the wall.
- "In-product billing engine is definitional" — rejected. Zephr (Zuora Billing), Piano (Stripe Billing option), Memberful (own Stripe) all delegate while remaining full instances of the Type. What is definitional is the managed recurring commercial cycle against the subscription.
- "Identity/registration is part of the definition" — rejected. Paper-era subscriptions ran on name+address; identity machinery is L1 common structure.
- "AI paywall optimization / dynamic decisioning is definitional" — rejected (era machinery; Zephr-page marketing numbers ignored).
- "Media subscription management = consumer-side subscription trackers (Rocket Money-class)" — rejected as a reading; the §27 placement and market usage both support the operator-side business system; the consumer tracker would fail the system-of-record and operator-user tests.
- "This Type = Subscription Billing Platform with a media logo" — rejected; the access binding + media product catalog + CSR/lifecycle surface make a distinct system of record even when the ledger is shared/delegated.

## Boundary Findings

**Joint review 1 — DISCHARGES magazine-periodical-management's flag (§27, processed 2026-09-08).** That pass documented its circulation machinery (subscriber records, terms, renewals, auto-charge, fulfillment) as "subscription management specialized to a periodical" and hung a joint-review flag with this leaf. Resolution from this side: **keep-both; the adopted seam (publication-binding) holds.** Evidence: this Type's sampled products carry *print subscription machinery* (Piano Print: addresses/delivery zones/confirmations; Pelcro fulfillment print+digital) — so print subscriptions are IN this Type — but none of the sampled surfaces documents the *issue-cycle-bound* machinery the magazine pass identified as its differentiator (issue-based terms/pricing, delayed starts, drops-and-adds, back issues/single-copy sales, controlled-circulation qualification/requalification, circulation-audit compliance). The magazine Type centers the publication + recurring issue cycle; this Type centers the subscription/access + revenue lifecycle without requiring an issue cadence. Product-spanning evidence recorded: Piano and Pelcro both serve magazine/newspaper publishers (Pelcro has a dedicated magazine-subscription industry page), consistent with the magazine pass's note that generic subscription machinery appears inside periodical systems. No directory change made from either side.

**Joint review 2 — DISCHARGES media-audience-management's flag (§27, processed 2026-09-08, item 3).** That pass adopted the seam "audience population + management loop as center vs subscription product/billing lifecycle as center," named Pelcro as the straddling pole, and requested joint review. Resolution from this side: **keep-both; seam confirmed.** This pass's Pelcro observation confirms the straddle prediction (subscription lifecycle + billing at the center of its own description, with audience/CRM surfaces alongside), and the sample's centers (catalog → lifecycle → money → access) sit squarely on the subscription side; audience profiling/segmentation/activation appears only as a standard capability (Arc XP CDP segments integration, Zephr first-party data activation, Pelcro subscriber CRM/engagement surfaces). Remove the audience loop → this Type stands intact; remove the subscription/billing lifecycle → what remains is the audience Type. Ratification of the keep-both decision is recorded; no directory change made.

**vs Subscription Billing Platform (§08, unprocessed):** expected heaviest machinery overlap (recurring charging, dunning, proration). Proposed seam for that pass: horizontal billing machinery serving any industry vs the media business system of record whose L0 includes the media access binding and media product catalog; products deliberately span the seam (Stripe under Piano/Memberful, Zuora under Zephr, Arc XP/Vindicia) — packaging/integration evidence, not alias evidence. Forward flag.

**vs Subscription Commerce Platform (§05.16, processed 2026-09-08):** seam held = per-cycle execution creates *commerce orders for goods* there (commitment × products × frequency × delivery destination) vs *renewal charges granting continued content access* here; their "digital access" program shape is the acknowledged overlap zone. Keep-both; consistent with that pass's own L0 (delivery-destination + order-fulfillment legs have no analogue here beyond print fulfillment, which is delivery of the *publication itself* as the access object).

**vs Video/Music Streaming Platform, Podcast Platform, Internet Radio (§27 siblings, unprocessed):** consumption/playback surface vs operator business layer. Streaming platforms embed subscription management internally (the same L0 legs exist inside them); the vendor market sampled here sells the business layer to media companies. Forward flags for those passes to test whether their L0s embed this core or treat it as a separate Type.

**vs Membership Management System (§25, processed):** membership/dues machinery is structurally adjacent (and Pelcro/Memberful straddle with "membership" language); seam = the subject of the ongoing relationship (member standing/benefits/governance of an organization vs paid access to a media company's content). Where a media brand sells "memberships" with content access, this Type's core applies.

**vs Newsletter Marketing Platform (§27-adjacent, processed 2026-09-08):** consistent — that pass held paid subscriptions/paywall as standard-NOT-definitional for email publication machinery; when the paid subscription business itself becomes the center (plans, trials, dunning, subscriber service), products realize this Type (Memberful's newsletter surface, Pelcro's free & paid newsletters use case).

**vs Media Rights Management (§27, processed 2026-09-08):** clean — rights grants between businesses (territory/window/exclusivity) vs consumer-side recurring access sales; no machinery overlap beyond both touching "what may be consumed."

**vs Customer Portal (§07):** the subscriber self-service portal (Pelcro client portal, Piano My Account, Arc XP account management) is a surface *of* this Type, not a separate Type instance — it is the subscriber-side face of the lifecycle.

## Uncertainties

- Exact lifecycle state names and dunning/grace behavior vary by product and were only Tier-1-documented on Piano/Arc XP partially (retries optimization page title-level). Final document deliberately avoids precise state lists and timing.
- Whether streaming-native subscription stacks (e.g., inside large SVOD platforms) would self-describe under this Type is untested (siblings unprocessed) — forward flag.
- Zephr's operational depth (does it hold subscription state at all, or purely experience decisions?) is unverified — docs unreachable; treated strictly as the experience-layer pole.
- Print machinery depth on Arc XP not fetched (print integration page exists in nav but was not read) — print leg supported by Piano/Pelcro evidence only, held at "common in publisher-facing products" strength.
- The relative market weight of delegated vs in-product billing across the whole media-subscription market is unknown; the sample shows both postures are fully realized products.

## Final Synthesis

Media Subscription Management is the media company's subscription business system of record. Its defining core is four jointly-held structures: the purchasable access product (plans/terms/offers with price and billing period), the subscriber's subscription instance lifecycle (acquire → active/renew → change → cancel/end, CSR + self-service operated), the recurring commercial cycle run against that instance (renewal charging, collection, failed-payment handling, refunds — in-product or delegated), and the content-access binding (an entitlement distinct from the SKU that the media product's enforcement consumes — paywall rules, permission sync, or physical print delivery). The money engine, identity layer, paywall experience layer, and audience loop are all real, heavily-invested layers, but each can be removed or delegated without destroying the Type; remove any one of the four core legs and the product becomes a different Type (billing engine, CRM, access tooling, registration system). Historical check passes from the paper-era subscription desk (rate/term card + subscriber cards + payments + the delivered paper) through the streaming era. Boundaries: magazine periodical management = publication+issue-bound edition of subscription machinery (keep-both, publication-binding seam); media audience management = audience-population center (keep-both, lifecycle-vs-population seam); subscription billing platform = horizontal machinery without the media access binding; subscription commerce = goods fulfillment per cycle; streaming platforms = the consumption surfaces this business layer serves.
