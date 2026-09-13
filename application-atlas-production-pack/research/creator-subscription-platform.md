# Research Notes — Creator Subscription Platform

Research date: 2026-09-07
Status: leaf processed under v1.1 methodology
Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Paid Community Platform, Fan Membership Platform, Creator Tip Platform, Creator Storefront, Digital Product Commerce Platform, Creator Course Commerce Platform [processed], Coaching Commerce Platform [processed], Creator CRM [processed], Creator Revenue Management [processed], Creator Affiliate Dashboard [processed]; distant family: Newsletter Marketing Platform §06, Subscription Billing Platform §08, Media Subscription Management §27)

---

## Research Goal

Understand what a "Creator Subscription Platform" is as an Application Type: what the central money/relationship object is, who operates which side (creator vs fan), what a subscription converts into, how the recurring billing and entitlement lifecycle work, and where the boundary sits against the §27 creator-economy siblings (especially Fan Membership Platform and Paid Community Platform, which share the same market space) and against adjacent Types (Newsletter Marketing §06, Subscription Billing §08, Media Subscription Management §27).

## Initial Boundary

- Working hypothesis: a platform where fans pay a creator on a recurring basis (subscription/membership) in exchange for ongoing access to the creator's output and/or declared perks; the creator authors the offer (tiers/levels), manages the subscriber roster, and receives recurring earnings.
- Primary users: the creator (offer author, roster manager, output producer) and the fan (subscriber).
- Nearest confusions going in:
  1. **Fan Membership Platform (§27 sibling)** — suspected near-alias; market uses "membership" and "subscription" interchangeably (Patreon "memberships", YouTube "channel memberships", Ko-fi "memberships", Substack "paid subscribers", Ghost "paid members").
  2. **Paid Community Platform (§27 sibling)** — venue access vs creator output stream.
  3. **Creator Tip Platform (§27 sibling)** — one-time support vs recurring commitment.
  4. **Newsletter Marketing Platform (§06)** — Substack/Ghost ship newsletter machinery; is the paid subscription layer the same Type?
  5. **Subscription Billing Platform (§08)** — same recurring-billing mechanics, different operator/counterparty.
  6. **Media Subscription Management (§27)** — subscription to a platform catalog vs to an individual creator.
- Known cluster seam test from prior passes: **what a purchase converts into** (coaching → tracked human-service engagement; course → curriculum access; storefront → goods/downloads; community/membership → venue access or stream). Feature presence is explicitly NOT the seam.
- Additional recorded seams from prior passes: Creator CRM owns the creator-side person records (a membership platform contains a member CRM as a component); Creator Revenue Management is the money layer ABOVE the earning mechanisms (subscription = one earning mechanism).

## Research Questions

1. What is the central object — subscription, member, tier, plan, level? How do they relate?
2. What does the fan subscribe to (the creator? a publication? a tier?), and who authors the offer?
3. What are the billing mechanics: cadences, auto-renewal, trials, upgrades/downgrades, gifts, coupons, lifetime?
4. What does an active subscription grant (gated content, community roles, private feeds, perks), and how is entitlement linked to subscription state?
5. What happens at the edges: cancellation, failed payments/dunning, pause, comps/free grants, price changes/grandfathering?
6. What does the creator-side surface contain (offer editor, roster, messaging, earnings, metrics)?
7. How do earnings reach the creator (platform-managed payouts vs creator's own processor; platform fee vs 0%)?
8. Where is the boundary vs Fan Membership Platform, Paid Community Platform, Tip Platform, Newsletter Marketing, Subscription Billing, Media Subscription?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

1. **Ghost** — open-source publishing platform with native memberships/paid subscriptions; the publishing-native pole; creator connects their own Stripe (0% platform fee). Tier-1 docs (excellent, fully reachable).
2. **Memberful** — membership/subscription infrastructure embedded in the creator's own site (WordPress plugin + hosted member pages); the infrastructure/embedded pole; professional publishers and businesses. Tier-1 docs (fully reachable).
3. **Buy Me a Coffee (BMAC)** — support-first creator platform (one-time tips + memberships + shop); the support-first/tip-adjacent pole; solo creators. Tier-1 help center (reachable).
4. **Patreon** — the canonical creator membership/subscription platform. Help center unreachable this pass (timeout ×2, consistent with creator-crm and creator-storefront passes) — treated **structurally** via Ghost's official migration documentation; no product-specific workflow claims.
5. **Substack** — the paid-newsletter pole. Help center unreachable this pass (timeout ×2) — treated **structurally** via Ghost's official migration documentation; no product-specific workflow claims beyond what that source states.

Unreachable this pass (recorded as limitations, not silently substituted from memory): support.substack.com (timeout ×2), support.patreon.com (timeout ×2), support.google.com/youtube channel-memberships article (timeout ×1 — platform-native pole left structural).

## Sources

### Ghost (Tier 1 — official docs, fetched 2026-09-07)
- Memberships — https://docs.ghost.org/members/ (member model, access levels, Stripe Connect, 0% fee, portability, imports)
- Tiers (Content API) — https://docs.ghost.org/content-api/tiers/ (tier object: name, type free/paid, monthly_price, yearly_price, benefits, welcome page, visibility)
- Migrating from Patreon — https://docs.ghost.org/migration/patreon/ (Patreon structure as described by Ghost)
- Migrating from Substack — https://docs.ghost.org/migration/substack/ (Substack structure, free vs paid subscribers, 10% fee)
- Docs index — https://docs.ghost.org/llms.txt (newsletters, email-only posts, offers, members admin API)

### Memberful (Tier 1 — official docs, fetched 2026-09-07)
- Docs index — https://memberful.com/docs/llms.txt (full article map with summaries)
- Create a plan — https://memberful.com/docs/plans/individual-plans/create-a-plan/ (plan/price model, intervals, trials, renewal settings, group plans, availability, taxes, links)
- How we handle failed payments — https://memberful.com/docs/member-management/payments-and-access/handle-failed-payments/ (dunning schedule, deactivation, MCC guidance)
- Key index-confirmed articles: admin dashboard, payment processing (Stripe), WordPress content protection, private RSS feeds, paid podcast, Discord/Discourse/Circle integrations, plan changes, group plans, choose-what-you-pay, coupons, gifts, referral/retention discounts, member management (modify subscription, pause, bulk edit, give free access), member self-service, metrics (MRR/churn/trials/paying members), cancellation survey, custom fields, staff roles, webhooks/API.

### Buy Me a Coffee (Tier 1 — official help center, fetched 2026-09-07)
- Help center root — https://help.buymeacoffee.com/ (collection map: One-Time Supports / Launching your Membership / Shop / Getting paid / For Supporters and Members)
- A simple guide to get started with memberships — https://help.buymeacoffee.com/en/articles/9969554 (level creation, rewards, billing, dunning, cancellation, pause/unpublish/delete, giveaways, lifetime, price-for-life FAQ, messaging)
- Launching your Membership collection — https://help.buymeacoffee.com/en/collections/2162972 (article map: lifetime, giveaways, pause, unpublish, Discord, pricing adjustment, free trials, membership recovery)

### Patreon (Tier 2 — structural only, via Ghost's official migration doc)
- https://docs.ghost.org/migration/patreon/ — "Patreon manages your subscriptions on your behalf"; patron CSV export from patreon.com/members; complimentary-status pattern for cross-platform access.

### Substack (Tier 2 — structural only, via Ghost's official migration doc)
- https://docs.ghost.org/migration/substack/ — free vs paid subscriber exports; Substack retains 10% fees on paid subscriptions; Stripe-connected billing; statement descriptor.

Evidence layers used below: **A** = directly observed on an official source for a specific product; **B** = cross-product commonality across the researched sample; **C** = canonical inference from comparison + boundary reasoning.

---

## Product A — Ghost

### Key observations (evidence layer A)

- **Positioning**: "The native Members feature in Ghost makes it possible to launch a membership business from any Ghost publication, with member signup, paid subscriptions and email newsletters built-in." Open-source publishing platform; hosted (Ghost(Pro)) or self-hosted.
- **Member model**: "A member of a Ghost site is someone who has opted to subscribe, and confirmed their subscription by clicking the link sent to their inbox." Members stored in Ghost with attributes: `email` (required), `name`, `note`, `subscribed_to_emails`, `stripe_customer_id`, `status` (free/paid/complimentary), `labels`, `created_at`. Passwordless JWT email-link authentication for signup/sign-in.
- **Access levels** (post settings in the editor): Public / Members only / Paid-members only / Specific tier(s). "Content is securely protected at server level and there is no way to circumvent gated content without being a logged-in member."
- **Tier object**: tiers have name, description, type (free/paid), monthly_price, yearly_price, currency, benefits list, welcome page URL, visibility, active flag. Tiers API returns them ordered by increasing monthly price. Admin API supports creating/updating tiers and offers.
- **Subscriptions**: "Members in Ghost can be free members, or become paid members with a direct Stripe integration." Publisher connects their **own** Stripe account via Stripe Connect; "Payments are handled by Stripe and billing information is stored securely inside your own Stripe account."
- **Fees**: "Ghost takes 0% of your revenue." Standard Stripe processing fees apply.
- **Portability**: member list exportable any time; subscriptions/billing live in the creator's own Stripe account ("you retain full ownership of it").
- **Alternative payment gateways**: Stripe is the only natively supported provider; members can be created via external providers (Patreon, PayPal) through API/Zapier.
- **Imports**: members importable from any platform via CSV, Zapier, or API; dedicated migrators (Substack, Patreon, WordPress, Kit, Mailchimp, Gumroad, Memberful…). For Patreon migrants: import patrons and set `complimentary_plan` status to give paid access while billing stays in Patreon.
- **Newsletters**: built-in email newsletters deliver posts to segments of the audience; email-only posts exist.
- **Offers**: a separate Offers concept (discounts) exists in the Admin API.

### Reading
Ghost's world model: publication (posts/newsletters) + member roster (free/paid/complimentary) + tiers (free/paid offers with monthly/yearly prices and benefits) + server-enforced access levels + creator-owned Stripe billing. The subscription is the billing wrapper around a content-entitlement relationship.

---

## Product B — Memberful

### Key observations (evidence layer A unless noted)

- **Positioning**: "Exactly what you need to build a membership home for your brand, business, and community." Membership infrastructure that plugs into the creator's own site (WordPress plugin with server-side content protection) or runs on Memberful-hosted member pages; audience spans individual creators to publishers/businesses.
- **Plan/price doctrine**: "Memberful plans define the benefits a member gets, while prices define how members pay for those benefits. A single plan can include one or more prices" (e.g., monthly + yearly under one plan; separate plans when benefits differ).
- **Billing intervals**: weekly, monthly, every 3 months, every 6 months, yearly, custom. Billing frequency cannot be edited once a plan has subscribers (support-mediated).
- **Renewal settings** (per price): automatic renewal ("subscription renews until the member cancels"; member can toggle from their account); **limited renewal payments** (end billing after N renewals — "members keep access after the last payment"); **different renewal price** after initial payment; **renew on a specific day** (fixed schedule instead of purchase anniversary; no proration).
- **Trials**: free trial without card, free trial with card required, paid trial with its own trial price; trial-ending emails for card-required trials ≥7 days; trial-length changes apply only to future members.
- **Choose-what-you-pay**: members can pay above the minimum (donation-flavored memberships).
- **Group plans**: one purchaser manages seats for a team/company/school; domain-restricted groups; seat management; group manager replacement; move group between plans.
- **Member management (creator-side)**: dashboard to find members, update details, manage subscriptions; add members manually (comped access); **modify a subscription** (cancel, toggle auto-renew, edit amount, delete, change renewal date); **pause subscription** (multiple approaches); bulk edit; move all members between plans/prices; refund or suspend orders.
- **Failed payments (dunning)**: first failure → past-due email + prompt to update payment details; retry up to 4 times at 12-hour intervals; "If we are unable to charge the member after 48 hours, we will deactivate their subscription." Expired-card reminders before renewal. Merchant-category-code guidance to reduce declines.
- **Free access / comps**: "Give free access to a Memberful plan so members, friends, or staff can join without paying. Useful for comps, team accounts, and lifetime members."
- **Free registration**: visitors can register free accounts before subscribing (lead capture, previews).
- **Fulfillment surfaces**: member website with members-only posts (public teasers possible); member newsletter (posts targeted to specific plans); **private podcast feeds** (personal authenticated RSS URLs; Spotify submission; dynamic bonus episodes); **downloads** (standalone products or bundled with plans); members-only video hosting.
- **Community attachment**: Discord integration ("Paid members are invited automatically and removed when their subscription ends"; role mapping between plans and Discord roles); Discourse, bbPress, Circle, BetterMode via SSO.
- **Monetization extras**: coupons (multi-code, availability windows); **gift subscriptions** (buyer purchases, recipient activates); **referral discounts** (members earn discounts for referrals); **retention discounts** (automatic discount presented in the cancellation flow); external payments (wire/cheque marked as paid); taxes collection; currency/language localization.
- **Metrics**: paying members, MRR, churn, trials, orders, net revenue, plan comparison, CSV exports; Google Analytics integration; member attributes (custom data per profile); cancellation survey.
- **Member self-service**: sign-in via email link or password; update personal info; manage subscription (toggle auto-renew, update payment method, switch plans); access benefits (private podcasts, downloads, Discord); manage referrals.
- **Email-vs-subscription rule**: "your newsletter's unsubscribe link doesn't cancel a member's Memberful subscription" — email opt-out and subscription cancellation are separate actions.
- **Platform plumbing**: Stripe for payment processing (creator connects own Stripe); test mode; staff members with role-based permissions; custom domains; white-label transactional emails (own SMTP); OAuth sign-in for apps; GraphQL API; webhooks (member/subscription/plan events); Zapier.

### Reading
Memberful is the subscription/membership engine as infrastructure: the deepest billing-lifecycle machinery in the sample (plans/prices, renewal variants, dunning, group seats, gifts, coupons, retention offers) wrapped around content entitlements that live on the creator's own property. It demonstrates that the Type can exist without hosting the content at all — entitlement enforcement can be delegated to WordPress/Discord/podcast players via keys, roles, and SSO.

---

## Product C — Buy Me a Coffee

### Key observations (evidence layer A)

- **Positioning**: "Buy Me a Coffee is best known for allowing creators to receive one-time support, but what if you could get support every month? That's where memberships come in! Setting up different membership levels allows you to turn your income into something steady and reliable." One account spans one-time supports, memberships, shop, posts/gallery/messages.
- **Membership level creation**: enable Membership; create levels with name, image, description, **monthly and yearly subscription fees**; select **rewards** from a reward library or write custom reward descriptions ("You can add as many rewards as you want"); welcome message shown after payment.
- **Level options**: limit the number of members per level (workload management / exclusivity); connect Discord roles per level (exclusive channels/badges); highlight a level on the page.
- **Page settings**: accept annual memberships (pay upfront for a year); display member count (social proof); display monthly earnings.
- **Level lifecycle**: edit anytime; **pause** (stops billing for current members and prevents new sign-ups; 1/3/6-month periods, auto-resume); **unpublish** (stops new members; current members keep content and keep being billed); **delete** (permanent; only when no active members or posts).
- **Billing**: "Memberships renew either monthly or yearly… This continues automatically unless the member or creator cancels or if the card doesn't have enough funds." Members charged immediately on subscribe, then "every 30 days for monthly memberships and every 365 days for yearly memberships" from the first payment date. Renewal payment triggers an email notification to the member.
- **Dunning**: "If the card lacks balance, the system will try up to three more times. If the payment still fails, the membership is canceled." A "membership recovery" flow exists (article title observed).
- **Cancellation**: members can cancel anytime; "They'll continue to have access to all benefits until the current subscription period (monthly or yearly) ends, but no further renewals will occur." Creators can also cancel a member's subscription from the member's profile ("view info" → cancel).
- **Price grandfathering**: "Whatever price people are charged when they sign up for the Membership is their price for life. Only your new members will be charged the new price."
- **Giveaways**: comped memberships with expiry "as short as 7 days" to let people experience perks.
- **Lifetime membership**: "a lifetime membership option… allows supporters to become members forever with a single payment."
- **Free trials**: enabled per membership level (article title observed).
- **Messaging**: creator can message member groups ("Select the member's group, type in your message, and click the send button").
- **Payouts**: "Getting paid" collection (16 articles) — platform-mediated payouts with account/content moderation gates (collection titles observed; article bodies not individually fetched).

### Reading
BMAC is the support-first pole: the subscription is framed as recurring *support* ("get support every month") with rewards as the declared return. It confirms every core structure (levels, monthly/yearly auto-renewal, state-linked benefits, dunning, end-of-period cancellation, comps, creator-side roster management) and adds the lifetime-membership variant that bends recurrence.

---

## Product D — Patreon (structural, Tier 2 via Ghost's official migration doc)

- "Since Patreon manages your subscriptions on your behalf, there is no direct migration path to move your paid subscriptions from Patreon to other platforms." — Patreon operates the billing relationship for the creator (platform-managed payments pole).
- Patron export: creators export their member list as CSV from patreon.com/members; email is the required field for import elsewhere.
- Cross-platform pattern: import patrons into another platform with complimentary/paid access while billing remains in Patreon (Ghost documents exactly this with `complimentary_plan`).
- No further Patreon-specific claims made (help center unreachable ×2 this pass and in prior passes).

## Product E — Substack (structural, Tier 2 via Ghost's official migration doc)

- Substack publications have **free subscribers** and **paid subscribers** as separate exports — the free→paid funnel is native to the model.
- "Substack will continue to take 10% fees on your existing paid subscriptions" (per Ghost's migration doc) — platform-fee pole.
- Paid subscriptions are Stripe-connected (migration requires connecting the same Stripe account); statement descriptor may include 'Substack'.
- No further Substack-specific claims made (help center unreachable ×2).

---

## Cross-product Comparison

| Dimension | Ghost | Memberful | BMAC | Patreon (structural) | Substack (structural) |
|---|---|---|---|---|---|
| Self-description | publishing platform with native memberships ("launch a membership business from any Ghost publication") | "build a membership home for your brand, business, and community" | one-time support platform + memberships ("get support every month") | creator membership platform (patrons) | newsletter platform with free + paid subscribers |
| Central objects | Member (free/paid/complimentary) + Tier + Subscription | Member + Subscription + Plan/Price | Member + Membership Level | Patron + tier (structural) | Subscriber (free/paid) (structural) |
| Offer authoring | tiers with monthly/yearly prices + benefits + welcome page | plans (benefits) with 1+ prices (amount + interval) | levels with monthly/yearly fees + rewards + welcome message | creator-defined tiers (structural) | publication-level paid subscription (structural) |
| Billing cadence | monthly/yearly per tier | weekly→yearly + custom intervals | monthly/yearly (+ lifetime one-time) | recurring (structural) | recurring (structural) |
| Auto-renew until cancel | yes (Stripe subscriptions) | yes (toggleable; limited-renewal and fixed-day variants) | yes ("continues automatically unless… cancelled") | yes | yes |
| Free tier | yes (free members) | yes (free registration) | no free membership tier (one-time supporters are the free-side funnel) | free follow tier (structural) | free subscribers |
| What entitlement grants | gated posts at access levels (public/members/paid/tier-specific) + newsletters | protected WordPress content, member-site posts, member newsletter, private podcast feeds, downloads, video | rewards/perks, Discord roles, members-only posts | perks per tier (structural) | paid posts (structural) |
| Entitlement ↔ state | server-enforced; logged-in members access content matching their tier | access enforced via plugin/keys/SSO; Discord auto-remove when subscription ends | benefits until period end; canceled = no further renewals | platform-managed (structural) | platform-managed (structural) |
| Comps/grants | complimentary status (manual; used for Patreon migrants) | give free access (comps/team/lifetime) | membership giveaways (min 7-day expiry) | (structural) | (structural) |
| Trials | not observed in members doc | free/paid trials, card-required variants | free trials per level | — | — |
| Dunning | via Stripe | past-due email → 4 retries @12h → deactivate after 48h | up to 3 more attempts → membership canceled; recovery flow | platform-managed | platform-managed |
| Cancellation semantics | member cancels (email-link account) | member toggles auto-renew; admin cancel/pause/edit | access until period end; creator-side cancel available | platform-managed | platform-managed |
| Pause | — | pause subscription (approaches compared) | pause level 1/3/6 months (billing stops, auto-resume) | — | — |
| Group plans | — | group plans with seats, domain restriction | — | — | — |
| Lifetime | — | (lifetime as comp use case) | lifetime membership (single payment, members forever) | — | — |
| Community attach | comments; community via integrations | Discord/Discourse/Circle/bbPress SSO with auto-invite/auto-remove | Discord roles per level | community feed (structural) | — |
| Content delivery | posts + email newsletters, server-level gating | member website + newsletter + private RSS + downloads | posts/gallery + messages to member groups | posts/feed (structural) | newsletter posts (structural) |
| Earnings rail | creator's own Stripe via Stripe Connect; Ghost 0% | creator's own Stripe | platform payouts (moderation-gated) | platform-managed ("on your behalf") | platform-managed; 10% fee (per Ghost doc) |
| Metrics | member counts (theme helpers total_members/total_paid_members) | MRR, churn, paying members, trials, orders, plan comparison, exports | member count + monthly earnings display toggles | — | — |
| Growth machinery | offers (discounts) | coupons, gifts, referral + retention discounts, cancellation survey | giveaways, highlighted levels, free trials | — | — |
| Migration/import | CSV/Zapier/API + platform migrators | CSV/Stripe-subscription imports, hands-on migration | — | export CSV (structural) | export CSV (structural) |

**Stop condition check.** With three direct samples + two structural poles, the core model (offer → subscription → state-linked entitlement → creator-side management), the billing lifecycle (renew/dunning/cancel/pause/comp), and the boundary behavior are stable; additional samples would repeat evidence. Stopping here.

---

## Canonical Abstraction

### L0 — Defining Invariant

A Creator Subscription Platform is recognizable when all four hold; remove any one and it becomes a different Type:

1. **Recurring fan→creator payment commitment** — a fan establishes an automatically renewing paid commitment to a *specific creator* (not to a platform catalog, not to a business's product line). The commitment persists across billing cycles until cancelled or lapsed. Remove recurrence → one-time tip/purchase (Creator Tip Platform / storefront). Remove the individual creator as counterparty → media subscription / SaaS billing.
2. **Creator-authored subscription offer** — the creator defines what can be subscribed to: named levels/tiers/plans carrying a recurring price (monthly/annual cadences typical) and a declared set of benefits. Single-price offers are the degenerate case of the same structure. Remove creator-authored offers → platform-defined media subscription.
3. **State-linked standing entitlement** — while the subscription is active, the fan holds a standing entitlement to what the offer declares — most concretely continuous access to the creator's gated output and/or declared perks (in the pure-support degenerate case, the entitlement is the supporter standing itself). The entitlement follows subscription state: granted on activation, maintained across renewals, ended by cancellation lapse or failed-payment deactivation. Remove state-linked continuous fulfillment (buy a discrete good instead) → storefront / course commerce.
4. **Creator-side subscription management** — the creator operates a surface to author offers, see and manage the subscriber roster (grant comps, cancel, pause, edit), communicate with member groups, and receive the recurring earnings (platform payouts or a creator-owned processor connection). Remove it → a bare payment processor, not an application.

Deliberately NOT in L0 (modern common, not definitional — historical check below): free tiers, trials, tiers/multiple levels (single-price qualifies), Discord/community attachment, private podcast feeds, MRR/churn dashboards, gift subscriptions, dunning schedules, coupons, group plans, Stripe specifically, digital delivery itself (mailed newsletters qualify).

### L1 — Common Mature Structure

Present across the researched sample (evidence layer B unless noted):

- **Free tier / free registration** as the top of the funnel (Ghost free members; Memberful free registration; Substack free subscribers; BMAC's free-side funnel is one-time supporters instead — common, not universal)
- **Monthly + annual billing options** on the same offer (Ghost tiers carry both prices; Memberful multiple prices per plan; BMAC monthly/yearly fees)
- **Trials** (Memberful free/paid trials; BMAC free trials per level)
- **Dunning / failed-payment recovery** (Memberful retry-then-deactivate; BMAC retry-then-cancel + recovery flow; Ghost via Stripe's machinery)
- **Cancellation with end-of-period access** (BMAC explicit; Memberful auto-renew toggle semantics; the general pattern: cancellation stops future renewals, not current-period access)
- **Comps / free grants** (Ghost complimentary status; Memberful give-free-access; BMAC giveaways)
- **Pause** (BMAC level pause; Memberful subscription pause)
- **Member self-service account** (update payment method, toggle auto-renew, switch plans — Memberful explicit; passwordless email-link auth in Ghost)
- **Community attachment with state-synced access** (Discord roles auto-granted and auto-removed — Memberful, BMAC; forum SSO — Memberful)
- **Gated-content delivery machinery** (access levels on posts — Ghost; WordPress protection + private RSS + member newsletter — Memberful; members-only posts — BMAC)
- **Creator→member messaging** (member-group messaging — BMAC; member newsletter — Memberful/Ghost)
- **Recurring-revenue metrics** (MRR, churn, paying members, trials — Memberful; member-count/earnings displays — BMAC)
- **Discounts, gifts, referral/retention offers** (Memberful coupons/gifts/referral/retention; Ghost offers; BMAC giveaways)
- **Price grandfathering** (BMAC explicit "price for life"; Memberful legacy-price pattern — common posture, exact semantics product-dependent)
- **Import/migration tooling** (Ghost migrators; Memberful CSV/Stripe imports)
- **Taxes collection** (Memberful; platform-handled at the platform-managed pole)
- **API/webhooks/automation** (Ghost Admin API + webhooks; Memberful GraphQL + webhooks + Zapier)

### L2 — Variant / Optional Structure

- **Packaging**: hosted all-in-one platform (BMAC) / publishing-platform-native (Ghost, Substack) / embedded infrastructure on the creator's own site (Memberful + WordPress) / platform-native channel memberships on large content platforms (structural pole; not directly researched this pass)
- **Payment posture**: creator-owned processor with 0% platform fee (Ghost, Memberful) ↔ platform-managed payments with platform fee (Substack 10% per Ghost's doc; Patreon "manages your subscriptions on your behalf")
- **Content-type emphasis**: written posts/newsletters (Ghost, Substack, Memberful), podcast (Memberful private feeds), video (Memberful members-only video), art/general support with rewards (BMAC), community-perks mixes
- **Lifetime membership** — one-time payment granting permanent standing (BMAC explicit; Memberful references lifetime members as a comp use case). Bends the recurrence invariant; documented as a variant, not the definition.
- **Group/organization plans** with seats and domain restrictions (Memberful)
- **Choose-what-you-pay pricing** (Memberful) — donation-flavored subscription pricing
- **Limited-renewal plans** (billing ends after N renewals, access retained — Memberful) and **fixed-day renewal schedules** (Memberful)
- **Member caps per level** (BMAC direct — single-product observation; exclusivity/workload rationale)
- **Audience scale**: solo creators ↔ professional publishers/media businesses (Memberful positioning; Ghost's newspaper/magazine heritage)
- **White-label/branding depth**: custom domains, branded checkout, white-label transactional email (Memberful)
- **Physical perks** as declared benefits (creator-fulfilled; BMAC tips mention stickers/T-shirts as reward examples)

### L3 — Vendor-specific (research notes only)

- **Ghost**: 0% platform fee; Stripe-only native payments; member attribute schema (email/name/note/subscribed_to_emails/stripe_customer_id/status/labels); access-level vocabulary (Public/Members only/Paid-members only/Specific tiers); passwordless JWT email-link auth; `complimentary_plan` import pattern for Patreon migrants; Offers API; theme helpers `total_members`/`total_paid_members`; email-only posts.
- **Memberful**: plans-vs-prices doctrine; interval set (weekly/monthly/3-month/6-month/yearly/custom); billing-frequency lock after first subscriber; limited renewal payments with post-term access retention; renew-on-specific-day without proration; different-renewal-price; dunning schedule (past-due email → 4 retries @12h → deactivate after 48h); expired-card pre-renewal reminders; MCC guidance (avoid entertainment/digital-product codes; prefer professional services/membership organizations/education); group plans (seats, domain restriction, manager replacement); cancellation survey; digital membership cards via Zapier+PassKit; OAuth; GraphQL API; white-label SMTP; test mode; staff role-based permissions.
- **BMAC**: reward library; giveaway minimum expiry 7 days; pause periods 1/3/6 months with auto-resume; unpublish vs pause vs delete semantics; billing cadence 30/365 days from first payment; renewal notification emails; dunning (3 more attempts then cancel); price-for-life FAQ; creator-side member cancel via "view info"; member-count and monthly-earnings display toggles; lifetime membership; account/content moderation before payouts.
- **Patreon** (structural): platform-managed subscriptions ("on your behalf"); no direct subscription migration path; patron CSV export from patreon.com/members.
- **Substack** (structural): free/paid subscriber split; 10% fee on paid subscriptions (per Ghost's migration doc); Stripe-connected billing; statement descriptor may include 'Substack'.

---

## Rejected Findings (considered and not promoted)

- **"Tiers are definitional"** — rejected: single-price subscription offers exist (Substack's publication-level paid subscription is structural evidence; Ghost tiers can be a single paid tier). Tiering is the common shape, not the invariant; the invariant is the creator-authored offer.
- **"Community access is definitional"** — rejected: Discord/community attachment is a benefit some offers declare (Memberful, BMAC), absent in others (pure newsletters). The entitlement is whatever the offer declares.
- **"The platform must host the content"** — rejected: Memberful enforces entitlements on the creator's own WordPress site, podcast players (private RSS), and third-party communities via SSO/keys. Hosting is a packaging variant.
- **"The platform must process payments (Merchant-of-Record-style)"** — rejected: Ghost and Memberful connect the creator's own Stripe account; the platform may or may not touch funds.
- **"Free tier is definitional"** — rejected: BMAC has no free membership tier (its free-side funnel is one-time supporters). Common, not invariant.
- **"Digital delivery is definitional"** — rejected by the historical check: mailed paid newsletters and postal fan clubs with dues satisfy the core without digital delivery.
- **"Subscription = access to content"** — refined: pure-support subscriptions with no declared perks exist in the market (support-first framing at BMAC; no-benefit tiers are a known Patreon pattern). The invariant is the state-linked standing entitlement, whose content is offer-defined and may be nominally empty.

## Boundary Findings

1. **vs Fan Membership Platform (§27 sibling) — near-alias risk.** The market uses "membership" and "subscription" interchangeably for this exact structure: BMAC's recurring product is "memberships" bought with "subscription fees"; Memberful sells "membership plans" that are auto-renewing subscriptions; Ghost calls paid subscribers "paid members" with "paid subscriptions"; Patreon's patrons are "members". The two directory leaves appear to describe one product family under two names. Working distinction if the taxonomy keeps both: *subscription* emphasizes the recurring payment relationship and the gated output stream; *membership* emphasizes belonging to a roster with benefits/perks. But every sampled product exhibits both emphases in one structure. → Recorded in STATUS.md Boundary Issues; joint review recommended.
2. **vs Paid Community Platform (§27 sibling)** — fulfillment-structure test: a paid community sells access to a *venue* (the community space is the product); a creator subscription sells a standing relationship with the creator's *output stream*, with community access as one possible declared benefit. Memberful's paid-community guide is the seam datum: the subscription platform manages the entitlement ("integrates with Discord, Discourse, Circle… to manage access as memberships change") while the venue is hosted elsewhere. Diagnostic: remove the creator's output stream and keep the venue → Paid Community Platform.
3. **vs Creator Tip Platform (§27 sibling)** — recurrence is the seam: tips are one-time voluntary support; subscriptions are auto-renewing commitments. BMAC ships both in one account (separate "One-Time Supports" and "Launching your Membership" collections) — feature presence is not the seam (cluster-established test). Diagnostic: remove auto-renewal → tip.
4. **vs Creator Storefront / Digital Product Commerce (§27)** — a storefront purchase converts into goods/downloads (discrete fulfillment); a subscription converts into a standing entitlement maintained across cycles. Memberful's downloads feature shows the seam from inside: downloads can be sold standalone (storefront-shaped) OR bundled with plans (entitlement-shaped).
5. **vs Creator Course Commerce (§27, processed)** — course purchase converts into curriculum access (structured content object with progress, consumed self-serve); subscription converts into an ongoing entitlement to the creator's stream/benefits with no curriculum structure. Course platforms ship memberships as sibling product types — feature presence is not the seam (cluster-established; consistent with that pass).
6. **vs Coaching Commerce Platform (§27, processed)** — coaching purchase converts into a tracked human-service engagement (session credits/program/subscription period tracked to delivery); creator subscription converts into access/support standing with no delivery-tracking machinery. Note: coaching commerce can sell "subscriptions" — the fulfillment object (tracked human service vs stream entitlement) is the seam, per that pass's recorded test.
7. **vs Creator CRM (§27, processed)** — the subscriber roster inside a subscription platform is a Creator CRM-shaped layer (person records with status/history), but this Type centers the fan-facing paywall and recurring billing; the CRM centers creator-side person records and audience→payer progression. Consistent with that pass's recorded seam ("a membership platform contains a member CRM as a component").
8. **vs Creator Revenue Management (§27, processed)** — this Type is a fan-facing earning mechanism; revenue management is the creator-side money layer above mechanisms (source-attributed income records, consolidated payouts). One product can span both; objects differ (subscription/entitlement vs income record). Consistent with that pass's recorded seam.
9. **vs Newsletter Marketing Platform (§06)** — Substack/Ghost ship newsletter sending, but the defining core here is the paid recurring relationship, not bulk outreach to a marketing list; the newsletter is a delivery vehicle for the gated output stream. Test: keep person records + consent + sending but remove the paid subscription layer → email/newsletter marketing platform; keep the paid relationship and treat sending as one channel → this Type.
10. **vs Subscription Billing Platform (§08)** — family resemblance (recurring billing, plans, dunning, MRR/churn vocabulary) but different operator, counterparty, and fulfillment: subscription billing platforms are business-side invoicing/ledger infrastructure for a company's customers; creator subscription platforms are fan-facing support relationships where the "product" is the creator's ongoing output. Memberful sits closest to the seam (it is literally subscription infrastructure) but its world is memberships-for-creators (content gating, community roles, private feeds), not invoice/ledger machinery.
11. **vs Media Subscription Management (§27) / Video Streaming Platform** — counterparty test: media subscriptions are paid to a platform/publisher for a catalog; creator subscriptions are paid to an individual creator for their ongoing output. Remove the individual creator as counterparty → media subscription.

### "去掉什么就变成另一个 Type" tests

- Remove auto-renewal → Creator Tip Platform (one-time support).
- Remove the individual creator as counterparty (pay for a platform catalog) → Media Subscription / Streaming.
- Remove standing entitlement (buy discrete goods) → Creator Storefront / Digital Product Commerce.
- Remove the creator's output stream, keep the venue → Paid Community Platform.
- Remove the fan-facing paywall (keep creator-side records) → Creator CRM.
- Remove the fan side entirely (business invoices customers) → Subscription Billing Platform (§08).
- Remove the paid layer entirely (free outreach to a list) → Newsletter/Email Marketing Platform (§06).

### Taxonomy observation (for STATUS.md Boundary Issues)

The leaf is real and documentable, but the §27 cluster contains three adjacent leaves — Paid Community Platform, Fan Membership Platform, Creator Subscription Platform — whose market realizations overlap heavily. Direct evidence from this pass shows "membership" and "subscription" used interchangeably for the same recurring fan→creator structure (BMAC memberships with subscription fees; Memberful membership plans = subscriptions; Ghost paid members = paid subscriptions). Fan Membership Platform is the highest alias risk. Recommendation: joint review of the three leaves; if kept separate, the defensible emphasis axes are venue-vs-stream (community vs subscription) and payment-vs-belonging (subscription vs membership), with the caveat that all sampled products exhibit both emphases in one structure.

### Historical / market-sample check (§24)

Would older/regional/platform-native products still fit?

- **Postal paid newsletter (pre-internet)**: a reader pays a recurring annual fee to an individual writer and receives ongoing issues by post; the writer keeps a subscription ledger. Satisfies L0: recurring fan→creator payment, creator-authored offer (the subscription offer itself), continuous fulfillment (mailed issues), creator-side ledger. No digital delivery, no tiers, no Stripe, no community — fits.
- **20th-century fan club with annual dues**: members pay recurring dues to support a specific artist and receive fan-club newsletters/perks. Satisfies L0 (the "membership" word itself is the belonging emphasis — supporting the near-alias reading of the sibling leaf).
- **Platform-native channel memberships (YouTube/Twitch-style)**: recurring fan payments to a channel with perks — fits the core; not directly researched this pass (docs unreachable), treated as a structural pole.
- **Counter-check**: a one-time Kickstarter-style backing fails L0 (no recurrence); a Netflix subscription fails L0 (counterparty is a platform catalog, not a creator-authored offer); a gym membership fails (counterparty is a business, not a creator's output relationship).

Therefore L0 must not include: digital delivery, tiers, free tiers, community attachment, Stripe/processor specifics, MRR dashboards, trials. The identity abstraction is "recurring fan→creator support relationship with offer-defined standing entitlement", not "Patreon-style tier page".

## Uncertainties

1. **Patreon and Substack help centers unreachable** (timeouts ×2 each) — both treated structurally via Ghost's official migration docs. No product-specific workflow claims made for either. If later researched, the L1 list may gain items (e.g., Patreon's perk-fulfillment tooling, Substack's founding-tier structure — NOT asserted here).
2. **Platform-native channel memberships (YouTube/Twitch-class)** — docs unreachable; the pole is described structurally only. Whether their machinery differs materially (e.g., revenue-share terms, tier rigidity) is unknown.
3. **Free-tier universality** — Ghost/Memberful/Substack have free tiers; BMAC does not (one-time supporters instead). The L1 phrasing "common, not universal" reflects 3/4 direct-or-structural evidence.
4. **Entitlement edge semantics** — what exactly happens to access at the moment of lapse varies (Memberful deactivates after dunning; BMAC ends at period end; Memberful limited-renewal plans retain access after final payment). Asserted only as "access follows subscription state; exact edge timing is product-dependent".
5. **Fee structures** — only Ghost (0%) and Substack (10%, per Ghost's doc) have direct figures; BMAC/Memberful/Patreon fee structures not asserted.
6. **Buyer-side depth** — research focused on the creator-side application and the subscription lifecycle; fan-facing surfaces observed via member self-service docs (Memberful) and supporter collections (BMAC titles).
7. **Whether "lifetime membership" should be a variant or a disqualifier** — treated as a variant that bends recurrence (documented explicitly); if the taxonomy prefers strict recurrence, lifetime would be an edge case worth flagging at joint review.

## Final Synthesis

A Creator Subscription Platform is the fan-facing recurring-support application of the creator economy. Its world model:

```text
Creator-authored subscription offer (level/tier/plan: recurring price + declared benefits)
└── Subscription (fan → creator, auto-renewing until cancelled/lapsed)
    ├── state: active ⇄ past-due/paused → cancelled/lapsed
    └── standing entitlement (gated output stream / declared perks / supporter standing)
        ↑ granted on activation, maintained across renewals
        ↓ ended by cancellation or failed-payment deactivation
Creator-side management surface
└── offer authoring · subscriber roster (comps/cancel/pause/edit) · member messaging · earnings · metrics
```

The defining core is deliberately small: a recurring fan→creator payment commitment, a creator-authored offer, a state-linked standing entitlement, and creator-side management of both. Everything else commonly seen — free tiers, trials, dunning schedules, Discord roles, private podcast feeds, MRR dashboards, gifts, coupons, group seats, lifetime purchases — is mature-market structure, variant, or vendor detail. The Type's sharpest internal seam is with Fan Membership Platform (near-alias: the market uses both names for this structure); its sharpest external seams are with Paid Community Platform (venue vs output stream), Creator Tip Platform (one-time vs recurring), the goods/course/coaching commerce siblings (discrete fulfillment vs standing entitlement), Newsletter Marketing (paid relationship vs outreach machinery), and Subscription Billing (fan support vs business invoicing).
