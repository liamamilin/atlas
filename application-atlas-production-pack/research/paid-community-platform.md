# Research Notes — Paid Community Platform

Research date: 2026-09-08
Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Creator Subscription Platform [processed 2026-09-07], Fan Membership Platform [processed], Creator Tip Platform [processed], Creator Storefront [processed], Digital Product Commerce Platform [processed], Creator Course Commerce Platform [processed], Coaching Commerce Platform [processed], Creator CRM [processed], Creator Revenue Management [processed], Creator Affiliate Dashboard [processed]; adjacent: Community Platform / Private Community Platform / Online Forum / Interest Community Platform §01.06 [all processed], Community Chat Platform §01.01 [processed], Fan Engagement Platform §27 [processed — label-collision counterparty], Membership Management System §25, Subscription Billing Platform §08)

---

## Research Goal

Understand what a "Paid Community Platform" is as an Application Type: what the community venue contributes, how payment attaches to admission, what the purchase converts into, how the access lifecycle follows the payment lifecycle, what the host does on the operator side, and where the boundary sits against the §27 creator-cluster siblings and the §01.06 community family.

This pass is the designated resolution point for three pre-hung flags from earlier passes:

1. **creator-cluster fulfillment seam** (creator-subscription-platform, fan-membership-platform passes): "a purchase converts into access to a *venue* (the space is the product); a creator subscription/fan membership sells the creator's *output stream/program*" — this pass must document the venue pole.
2. **private-community-platform flag**: "Mighty/Circle are monetization-heavy closed-venue poles and remain here; flag for that pass" — this pass must draw the monetization-vs-boundary discriminator.
3. **community-platform / member-community-platform flags**: "in the creator pole, a purchase converts into venue access and monetization organizes the product; in this Type, monetization is a variant capability" — same seam, §01.06 side.

## Initial Boundary

Working hypothesis entering research:

- Core purpose: software for running a community whose admission is organized by payment — the host prices membership in the venue, buyers become members, and access follows payment state.
- Primary users: community host (creator, coach, expert, brand, educator) on the operator side; paying members on the participant side.
- Nearest confusions: Community Platform / Private Community Platform (monetization optional / gate one-of-several), Creator Subscription Platform / Fan Membership Platform (output stream / program vs venue), Creator Course Commerce (curriculum vs venue), Membership Management System (org dues/roster vs venue purchase), Subscription Billing (generic recurring invoicing vs venue-scoped), Community Chat Platform (chat container vs monetized venue).
- Unknowns entering research: whether recurrence is definitional (Skool/Mighty both support one-time pricing — likely NOT definitional); how space-scoped selling works (plans attaching to individual spaces vs the whole venue); whether token-gating exists in the wild (suspected in Mighty); regional/historical fit of the definition.

## Research Questions

1. What is the world model: venue, spaces, plans, members, purchases, access states?
2. What does a purchase convert into, concretely, in each product's documentation?
3. How is the offer authored (free / subscription / freemium / tiers / one-time; trials; coupons; installments; currency)?
4. How does access follow payment (activation, renewal, downgrade, past due, cancel, refund, comp, grandfathering)?
5. How is the offer attached — whole venue, individual spaces, bundles, feature levels?
6. What does the host-side operator surface look like (plan config, roster, payouts, fees, taxes)?
7. What does the member-side surface look like (checkout, billing self-service, billing/history)?
8. What gate types coexist with payment (screening questions, approval, invite, token)?
9. Where are the boundaries against the ten adjacent/sibling Types listed above?
10. Historical/regional check: would older forum-software pay-to-access setups and regional paid-circle products fit the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / position | Customer tier | Evidence quality this pass |
|---|---|---|---|
| **Circle** (circle.so) | All-in-one branded community home for creators & businesses; paywalls as headline feature | Creator → SMB → enterprise (Circle Plus, branded apps) | Tier 2 product/pricing pages; help center JS-rendered, unreachable |
| **Mighty Networks** (mightynetworks.com) | "Community Platform, Courses & Memberships"; host-centric, engagement/"People Magic" philosophy, native apps | Solo host → pro host → branded-app enterprise (Mighty Pro) | Tier 1 operational docs (docs.mightynetworks.com, machine-readable) + Tier 2 pages |
| **Skool** (skool.com) | Minimalist community+classroom ("group"), single-product philosophy, aggressive monetization defaults (Growth Boost) | Solo creator/host | Tier 1 operational help center (help.skool.com) |

Variant anchors attempted (not required for the core): Discord Server Subscriptions (platform-native chat pole — support article timed out 2×, abandoned), Discourse + subscriptions plugin (self-hosted forum pole — meta topic 404, abandoned). Both recorded as Uncertainties; not used as evidence.

## Sources

Tier 1 (official operational documentation, directly fetched 2026-09-08):

- Skool Help Center — home/categories: https://help.skool.com/ (Admin: Payments, Billing, Roles, Community, Classroom, Calendar, Leaderboards, Discovery, Plugins, Affiliate; Member: How Skool Works, Accounts, Payments)
- Skool — "How to setup pricing for the group?": https://help.skool.com/article/215-how-to-setup-pricing-for-the-group
- Skool — "Skool Payments FAQs": https://help.skool.com/article/86-subscriptions-faq
- Mighty Networks Help Center index: https://docs.mightynetworks.com/llms.txt (For Hosts, 181 pages incl. "Payments and Access" section)
- Mighty Networks — "How Do I Gate Access to All or Parts of My Mighty Network?": https://docs.mightynetworks.com/for-hosts/payments-and-access/how-do-i-gate-access-to-all-or-parts-of-my-mighty-network.md
- Mighty Networks — "What is a Full vs. Limited Membership?": https://docs.mightynetworks.com/for-hosts/payments-and-access/what-is-a-full-vs-limited-membership.md
- Mighty Networks — "What Happens When a Member Cancels or Requests a Refund": https://docs.mightynetworks.com/for-hosts/payments-and-access/what-happens-when-a-member-cancels-or-requests-a-refund.md

Tier 2 (official product pages, directly fetched 2026-09-08):

- Circle — Pricing page: https://circle.so/pricing (plans, feature matrix, transaction fees, SSO integrations, migration services)
- Mighty Networks — Homepage: https://www.mightynetworks.com/ (positioning, plan lineup, revenue calculator)
- Mighty Networks — Payments page: https://www.mightynetworks.com/payments (checkout, intervals, installments, promo codes, currencies, purchase automations)

Unreachable / degraded:

- Circle Knowledge Base (https://help.circle.so/, /en/, /c/getting-started) — JS-rendered shell, no article content (2 attempts + 1 fallback → degraded to Tier 2 pricing evidence only)
- Discord support "Server Subscriptions" — request timed out 2× → abandoned
- meta.discourse.org Discourse Subscriptions plugin topic — 404 → abandoned
- No historical products (forum-software pay-to-access add-ons, regional paid-circle apps) fetched this pass — historical check done conceptually (see Uncertainties)

---

## Product Observations

### Skool (evidence layer: A — directly observed in Tier 1 help center)

**Offer authoring** ("How to setup pricing for the group?"): a Skool "group" (community + classroom) supports five pricing models: 1) Free group; 2) Subscription group — monthly or annual membership, optional 7-day free trial; 3) Freemium — free plan + paid plan in the same group, members upgrade inside the group, paid plan carries a declared premium benefit; 4) Tiers — multiple paid plans, each with its own benefit; 5) One-time payment — "lifetime access courses, pop-up groups, and seminars".

**Money machinery** ("Skool Payments FAQs"): platform processes payments and pays hosts out (merchant-of-record posture: Skool handles EU VAT, "Skool is responsible for all sales tax collection, filing, and payments"); per-plan fee schedules differ (Pro vs Hobby plan); payouts weekly to local currency; per-transaction price ceiling exists; all subscription prices in USD. Host connects bank account via payout onboarding with identity verification. Refunds: "Skool's policy is to let Creators offer refunds to Members at their discretion… Skool will not refund on behalf of Creators."

**Access-state rules**: existing members grandfathered on the price they currently pay (explicit examples: free→paid keeps existing members free; price increase keeps existing members at old price). "How to make paid member free" article = comping. Proration exists for members changing plans. "How to temporarily close the group" = host-side admission control. Cancellation video = host-authored retention surface shown at cancel.

**Growth Boost**: default-ON discovery/paid-acquisition program — group shown at top of search results and off-site ads run by the platform; platform fronts cost and takes a commission on acquired customers for as long as the subscription is active; can be toggled off. This is a strong signal that monetization is the organizing concern of the product (discovery itself is packaged as customer acquisition).

**Venue structure** (help center categories): Community (categories, rules, moderation), Classroom (courses and unlock mechanisms — i.e., content gated by progress or plan), Calendar (events, Skool Call, Go Live), Leaderboards (gamification, levels, points), Discovery (categories, ranking, algorithm), Plugins (membership questions, auto-DM), Affiliate program. Roles: Owner, admin, moderator, **billing manager**. Member side: How Skool Works, Accounts, Payments ("manage, update, cancel, refund"), Billing ("updating, canceling, invoices").

### Mighty Networks (evidence layer: A — directly observed in Tier 1 docs; B for product pages)

**Gating as plan composition** ("How Do I Gate Access…"): "Plans offer the most options and flexibility for gating access to your Mighty Network, Spaces, or both." A plan can require one or more of: **Pay (Payment gate)**, **Answer questions (Screening Questions gate)**, **Request approval (Approval gate)**. Plans attach to the Network, to individual Spaces, or to bundles of Spaces. Plans appear on the Network Landing Page / Collection Pages / Space About Pages, or exist as hidden plans accessible only via link/share links.

**Standard architectures documented** (same article): (1) screen at network level (approval gate, no payment), then charge subscriptions for Spaces — the "value journey" architecture; (2) charge a subscription for the whole Network, spaces free to join inside. Plus: limited memberships via plans that include only Spaces; one-time purchase plans that include only Spaces ("members keep access to these Spaces regardless of whether they are also on a plan that includes the Network").

**Full vs limited membership** ("What is a Full vs. Limited Membership?"): full membership = access to the entire Network; limited = access to specific Spaces/features. **Limited members can only join Spaces through paid plans — invites do not grant access, and "Anyone Can Join" settings do not apply to them** ("must have a valid payment for a plan that includes the Space in order to access it"). Demoting a full member to limited removes global features (private messaging, global feed/search, points); limited members cannot become hosts/moderators. Detailed per-feature access tables for both member types.

**Billing lifecycle** ("What Happens When a Member Cancels or Requests a Refund"): members can cancel at any time; **cancellation takes effect at the end of the current billing period**; members cannot leave a paid plan immediately unless they delete their account or the host removes them. Failed payment → **Past Due** state → "the plan may automatically cancel." Refunds handled entirely by the host, at host discretion (web purchases refunded via the host's connected Stripe account; iOS purchases billed by Apple and refunded via Apple's flow). Free/Access plans and one-time payments have no built-in cancel — member is manually removed by host or deletes account. Hosts receive cancellation notification emails with member links (churn-touch workflow).

**Pricing machinery** (Payments page + docs section titles): charge for memberships, courses, events, and bundles ("Mighty handles checkout — you get the revenue"); intervals: annual, monthly, weekly, daily, or one-time; installment plans; promo codes; multiple currencies; free trials; token-gated plans exist as a doc category; Stripe connect or payments off platform; taxes docs; "How Can I Move Paying Members from Another Platform" (subscription migration); price changes doc; waitlists; default plan for invites (Beta).

**Purchase-linked automations** (Payments page, Tier 2): "Tag new buyers… Unlock access instantly — when someone buys, invite them to the right spaces automatically… Celebrate the Purchase… Follow Up on Cancellations — automatically add a tag and send a message… VIP Invitation — when a member renews for 6+ months or upgrades to a higher plan, invite them to an exclusive space." Purchase state is a first-class automation trigger.

**Venue structure** (docs index): Spaces with templates and per-space features (feed/posts, chat, courses with sections/lessons/quizzes/certificates, events/livestreams, member-led content), member profiles, People Explorer (member discovery), welcome checklist, host/moderator roles at Network and Space level with distinct permissions, admin settings, member detail page, "view as member", moderation tools, member block/report, Insights analytics, email digests, notifications, SSO, APIs (Admin + Headless), Zapier, custom domain, branded iOS/Android apps (Mighty Pro) with native in-app purchases, GDPR/CCPA, EU Consumer Rights Directive cancellation path.

**Positioning** (homepage, Tier 2): "Community Platform, Courses & Memberships"; customers called "hosts"; "Community Design™" methodology; $500M host earnings claim; "$48 avg monthly price of memberships sold by our Hosts"; revenue calculator (members × price); plan lineup Launch/Scale/Growth + Mighty Pro branded apps; funnel framing (challenges/mini-courses → membership → bonuses).

### Circle (evidence layer: A for the pricing page itself; overall layer degraded — B/C)

**Positioning** (pricing page): all-in-one community platform; plan features include: unlimited members, courses, discussions, events, website builder, live streams/live rooms, custom branding, reporting & analytics, searchable member directory, rich member profiles, **paid memberships**, gamification, custom domain, weekly digest, **migration services for payments**; higher tiers add workflows, custom profile fields, APIs (Admin + Headless Member), branded email, content co-pilot, transcriptions; top tier adds AI agents, SSO, sandbox community, lower fees; optional branded apps with **native in-app purchases**; optional Email Hub (broadcasts, forms, automations, segments).

**Monetization is a platform-revenue pillar**: transaction fees scale down by plan tier (2% → 1% → 0.5%); free payment-migration service "transfers active subscriptions and payment information from your legacy platform to Circle"; payment migrations prioritized on higher plans.

**External-paywall interop**: SSO integration list includes Memberful, MemberSpace, Outseta, Memberstack, Teachable, WordPress, Auth0 — i.e., Circle venues can be paywalled by external subscription tools, with Circle handling the venue and the paywall handling the money (the inverse of the Mighty default). Important seam datum vs Creator Subscription Platform (which documented Memberful as entitlement manager over external venues).

**Venue structure** (feature matrix): spaces, group chat, direct messaging, scheduled posts, in-app notifications, events, member profiles & directory, basic moderation, weekly digest, desktop + iOS/Android apps, search, gamification, custom domain/CSS, embeds, Zapier, AI suite. Admin limits (admins/moderators/spaces/storage) per plan.

**Not observed** (help center unreachable): paywall configuration steps, plan/offer semantics, dunning behavior, refund defaults. No operational claims about Circle internals are made beyond the pricing page in the final document.

---

## Cross-product Comparison

| Dimension | Circle | Mighty Networks | Skool | Reading |
|---|---|---|---|---|
| The thing sold | The community venue ("paid memberships" over community home) | The venue and/or specific Spaces ("charge for memberships, courses, events, bundles") | The group (community + classroom) membership | All three sell **access to a venue**; purchase→access is the organizing conversion |
| Offer authoring | Paywalls (config docs unreachable); pricing is per-platform-plan for the host | Plans w/ payment / questions / approval gates; attach to Network, Space, or bundles; full vs limited memberships | Free / subscription (trial) / freemium / tiers / one-time per group | A **host-authored purchase offer attached to the venue (whole or parts)** is universal; offer granularity differs |
| Recurrence | Subscriptions implied (payment migration of "active subscriptions"); one-time unknown | Recurring (multiple intervals incl. weekly/daily) AND one-time plans | Recurring AND one-time ("lifetime access") | **Recurrence is common but NOT definitional** — one-time venue admission exists in 2/3 sampled directly |
| Purchase→access | Instant access implied by product framing (not doc-verified) | "Members pay and they're in. No waiting, no manual approvals" (Payments page); automations "unlock access instantly" | Free trial then membership; members upgrade inside group | Purchase converts into member access **immediately on payment** in the mature pattern |
| Access ends when payment ends | Not doc-verified | Cancel → access to end of billing period; Past Due → plan may auto-cancel; refund → host revokes access | Cancel/refund documented member-side; grandfathering on price changes | **Payment-state-linked access lifecycle** is the shared control loop; exact grace behavior is product-specific |
| Gating beyond payment | SSO with external paywalls (Memberful etc.) | Screening questions + approval gates combinable with payment; invite-only; token-gated plans | Membership questions (plugins); temporarily close group | Payment is the primary gate; other gates **layer on top**, not replace it |
| Money machinery | Platform transaction fees 2/1/0.5%; payment migration service | Stripe connect or off-platform; host refunds at discretion; iOS via Apple | Merchant-of-record (VAT/sales tax handled); weekly payouts; per-plan fee schedules; comping; proration | The platform operates the **revenue loop** (checkout, fees, payouts, taxes, refunds, comps) scoped to venue access |
| Monetization-adjacent growth | Email Hub, workflows | Purchase-state automations; affiliate program; SEO | **Growth Boost** (default-ON paid acquisition for a commission); affiliate; discovery ranking | Monetization machinery extends into acquisition/retention — signature of the Type |
| Venue contents | Spaces, chat, DMs, courses, events/live, directory, gamification, digest | Spaces (feed/chat/courses/events/livestream), profiles, People Explorer, gamification, welcome checklist | Community (posts/moderation), Classroom (courses+unlock), Calendar (events), Leaderboards | The venue carries the standard operated-community space set; **which space types exist is variant, not definitional** |
| Roles | Admins/moderators per plan | Host/moderator at Network & Space level; host vs limited member capabilities | Owner/admin/mod/**billing manager** | Operator roles are community roles; monetization adds a **billing-capable role** |

Evidence-strength summary: purchase→venue-access conversion, host-authored offers, and payment-state-linked access are cross-product commonalities (layer B, 3/3 products with at least Tier 2 evidence; 2/3 with Tier 1). Immediate-access-on-payment is documented in 2/3 (Mighty docs + page; Skool flow). The rest of the money machinery details vary per product.

---

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (deliberately minimal)

1. **The paid venue** — a hosted community container with participatory member spaces (discussions, feed, chat, events, courses, directory — mix varies). The venue itself is the product being sold. Remove the venue → checkout for content (creator subscription) or generic billing; the Type stops existing.
2. **Host-authored purchase offers on admission** — the operator (community host) prices access: a named offer (plan/pricing) attached to the whole venue or to bundles of individual spaces, with a price and billing structure (recurring typical, one-time common), joined via checkout. Remove the offer → free community platform.
3. **Payment-state-linked access** — a completed purchase converts the buyer into a member with access to what the offer covered; access persists while payment is active (renewals included) and ends or degrades when it lapses (cancellation at period end, past-due deactivation, host removal), with host-side exceptions (refund → revoke, comp → grant). Remove this link → two unrelated products (a community + a payment form).
4. **Host-side monetization management** — the operator surface that makes 2–3 operable: offer authoring, member/purchaser roster, billing operations (cancel/comp/refund/pricing changes), and revenue disposition (payouts/fees/taxes per the platform's money posture).

Test: would an older forum gated by a paid-subscription add-on satisfy all four? Yes (venue = boards; offer = subscription product; access follows payment; admin panel manages both). Would a free Discord server? No — no purchase offer. Would a Substack? No — no participatory venue. Would an association dues system? It has roster+dues but the organizing object is the organization membership record, not a venue being sold as the product — boundary documented below.

### L1 — Common Mature Structure (cross-product commonality, not definitional)

- Standard space set inside the venue: discussion/feed, chat spaces, direct messaging, member profiles & directory, events (sometimes paid/livestreamed), courses/classroom with gating/unlock, gamification/leaderboards, welcome/onboarding checklists
- Host/moderator/member roles with per-space permissions; dedicated billing-capable role (Skool) or billing sections in admin
- Marketing & storefront surfaces: landing pages about the venue and its offers, offer placement (landing page / collection / space about page / share-link-only), funnels (free challenges/mini-courses as lead magnets into paid access)
- Member billing self-service: manage/update payment method, cancel, invoices/billing history
- Notifications, digests, mobile apps, search, moderation tooling, analytics (engagement + revenue)
- Purchase-state automations (tag buyers, auto-grant space access, win-back on cancel)
- Integrations/API/SSO; data ownership/export assurances; migration tooling for paying members from other platforms

### L2 — Variant / Optional Structure

- Offer architecture: freemium (free plan inside a paid venue), multi-tier benefits, trials, coupons/promo codes, installments, multi-currency, group/seat pricing (not observed this pass — unverified), lifetime/one-time vs recurring emphasis
- Admission posture: open venue with optional payment vs approval-gated venue with payment layered; waitlists; hidden/share-link-only offers; temporarily closing admission
- Scope of sale: whole-venue membership vs space-scoped limited membership vs standalone course/event bundles inside the venue
- Payment posture: platform-managed processing (merchant of record, platform fees, payouts) vs host-owned processor (Stripe connect) vs payments off platform entirely vs external paywall tools via SSO vs app-store IAP (Apple-billed purchases with Apple-side refunds)
- Token-gated admission (crypto-token ownership as the "payment") — documented variant in one product
- Branded mobile apps with native in-app purchases (higher-tier variant)
- Platform-native channel subscriptions: paid venue access sold inside chat/streaming platforms (not directly evidenced this pass — recorded as variant hypothesis only)
- Acquisition machinery attached to monetization: paid discovery/ads-for-commission (Skool Growth Boost), affiliate programs, SEO

### L3 — Vendor-specific (research notes only)

- Skool: Pro vs Hobby fee schedules (2.9%+30¢ up to $899 / 10%+30¢; international tiers), $100k transaction ceiling, USD-only pricing, weekly Wednesday payouts w/ verification, reverse payout invoices, Growth Boost 30% commission on platform-acquired customers (default ON, toggle in Discovery settings), cancellation-video feature, UK VAT exemption posture, 7-day trial parameter, "pop-up groups" positioning of one-time pricing
- Mighty Networks: full vs limited membership feature tables (limited members lose DMs/global feed/search/points, can't host/moderate), demotion preserving chat history on restore, iOS-purchase cancellations routed through Apple settings + reportaproblem.apple.com, host-refunded web purchases via Stripe minus fees, "Access plans" (no payment gate), default plan for invites (Beta), Community Design™/People Magic branding, Launch/Scale/Growth + Pro plan ladder, mn.co domain customization, EU Consumer Rights Directive cancellation-rights doc
- Circle: transaction-fee ladder by host plan (2%/1%/0.5%), admin/moderator/space/storage limits per tier, Circle AI credit system, Email Hub add-on pricing, Circle Plus concierge/branded-apps services, 30-day money-back guarantee, SSO catalog (Memberful/MemberSpace/Outseta/Memberstack/Teachable/WordPress/Auth0…)

---

## Vendor-specific Findings

(kept out of the final document; see L3 above for the full list)

- Skool is the only sampled product that packages **paid customer acquisition** (Growth Boost) as a default-on monetization feature — evidence that in this Type the platform competes on members' revenue outcomes, but it is a vendor strategy, not a Type property.
- Mighty Networks is the only sampled product with documented **token-gated plans** and **space-scoped limited memberships** with formal capability tables — the strongest single-product operational evidence for the access-architecture axes (marked product-specific).
- Circle is the only sampled product whose documented interop pattern (SSO to external paywalls) implements the **inverse** money posture — venue here, entitlement elsewhere — which is exactly the Creator Subscription Platform's pattern; useful seam datum, marked product-specific.

## Boundary Findings

The cluster established a **fulfillment-structure test**: what does a purchase convert into?

1. **vs Community Platform (§01.06, processed)** — there, the operated container + managed members + participatory spaces define the Type and monetization is an optional capability (2/4 sample). Here a purchase converting into venue access *organizes* the product and the money loop is a first-class pillar. Diagnostic: delete the monetization machinery; if the product remains the same software, it is a Community Platform; if it stops making sense, it is this Type.
2. **vs Private Community Platform (§01.06, processed)** — there the closed boundary is the organizing object and payment is one admission gate among several (invitation, application, SSO). Here the purchase is admission's primary path and the billing lifecycle (renewal, lapse, refund, comp, payout) is productized. Diagnostic: replace payment with free-but-closed admission; if the product story is intact → Private Community Platform. Realization note: Circle/Mighty genuinely straddle (sampled by both passes); the discriminator above is the resolution (see Boundary Issues).
3. **vs Creator Subscription Platform (§27, processed)** — there the purchase converts into a standing relationship with the creator's *output stream*; the venue is at most one declared benefit and is often hosted elsewhere with access synced (Memberful→Discord/Discourse/Circle pattern — corroborated from the Circle side by its SSO catalog). Here the venue *is* the fulfillment object. Diagnostic: remove the venue and keep the output stream → Creator Subscription; remove the output stream and keep the venue → this Type.
4. **vs Fan Membership Platform (§27, processed)** — same test as 3 with "the creator's program + declared benefits" in place of output stream; that pass already recorded "remove the creator's program and keep the venue → Paid Community Platform." Reciprocal diagnostic recorded here.
5. **vs Creator Course Commerce Platform (§27, processed)** — there the purchase converts into curriculum content access; course platforms embed communities as add-ons (absorption noted by that pass). Here courses are a space type inside the venue; the curriculum is not the organizing object. Diagnostic: is the offer selling "the classroom" or "the room"?
6. **vs Coaching Commerce Platform (§27, processed)** — purchase → human service time there; venue access here. Coaching can be a declared space/event inside a paid community without changing the Type.
7. **vs Membership Management System / AMS / Member Portal (§25)** — there the membership record + dues cycle + benefits administration around an organization's roster is the system of record; the community is one benefit surface. Here the venue-commerce loop is the record. The community-platform pass additionally recorded: "dues-for-benefit in the member segment is a membership relationship, not a content purchase."
8. **vs Subscription Billing Platform (§08)** — generic recurring invoicing/entitlement machinery for arbitrary businesses, no venue, no participatory spaces, no community operations. This Type embeds a billing loop *scoped to venue access* inside a community product.
9. **vs Community Chat Platform (§01.01, processed)** — live chat rooms under a container there; chat may be one space type here, and chat containers can host paid channels (platform-native subscriptions — unverified this pass), but the chat container does not productize the purchase→access loop as its organizing concern.
10. **vs Event Ticketing / Registration (§26)** — one-off event purchases there; standing venue access here. Paid events exist inside paid communities as one-off commerce (documented in Mighty), a bundle variant, not the Type.
11. **vs Online Donation / Tip Platforms (§25/§27, processed)** — no entitlement, no access conversion there.
12. **vs Fan Engagement Platform (§27, processed)** — label-collision note from that pass confirmed: the creator-economy "engagement" sense (paid memberships/DMs) belongs to this cluster; the organization-side fan-records Type is distinct.

**"去掉什么就变成另一个 Type" 判据**：去掉付费与访问联动 → Community Platform / Private Community Platform；去掉场所（参与式空间）→ Creator Subscription / Fan Membership / Subscription Billing；去掉购买（免费开放）→ Community Platform；把履约对象换成课程/服务/商品 → Course/Coaching/Storefront siblings。

## Historical / Market-Sample Check (per workflow §24)

Would older, regional, platform-native products still fit the L0?

- **Older forum software with pay-to-access subscription add-ons** (the classic "paid subscriptions" add-on of self-hosted forum platforms): venue = boards, offer = subscription product, access follows payment, admin manages both. Fits L0. Not directly fetched this pass — recorded as conceptual check, not cited evidence.
- **Regional paid-circle products** (e.g., Chinese 知识星球-style paid circles: pay to join a circle, post/comment inside): pay→join venue with participatory spaces. Fits L0. Not fetched this pass — same caveat.
- **Platform-native channel subscriptions** (chat/streaming platforms selling paid venue access): fits L0 conceptually (venue = channel/server); not evidenced this pass; kept as variant hypothesis.
- **Ning-era operator-built networks with paid tiers**: fits L0 (network + paid access), predating the current all-in-one wave.

Conclusion: the definition does not over-fit the current all-in-one creator-tool generation; the invariant (venue + purchase offer + payment-linked access + host-side management) survives era/geography/platform substitution. The one definitional choice that required abstraction: recurrence is NOT required (one-time venue admission exists in 2/3 sampled products directly), and the space-type mix is NOT required.

## Uncertainties

1. **Circle operational detail** — help center JS-rendered and unreachable (2 attempts + fallback). Plan/paywall semantics, dunning, refund defaults for Circle are unverified; final document makes no precise Circle operational claims. Evidence for Circle is pricing-page-level (degraded layer).
2. **Platform-native channel subscriptions** (Discord-style server subscriptions) — support article unreachable 2×. Recorded as variant hypothesis from prior passes' notes (fan-engagement-platform pass), not as observed evidence.
3. **Self-hosted forum pole** (Discourse subscriptions plugin) — meta topic 404. The "older forum software" historical anchor is conceptual, not cited.
4. **Group/seat/corporate pricing** — not observed in the fetched sample (Mighty docs show member-level plans; Skool shows member-level). Unverified whether B2B seat selling is common; final doc does not claim it.
5. **Dunning specifics** — Mighty: past-due → plan may auto-cancel (verified). Retry schedules/grace windows beyond that are product-specific and not asserted.
6. **Whether "paid community platform" ever denotes an *organization-side* product** — the market sample (creator/host side) shows no operator-side B2B employee/community-management product under this exact name; the §01.06 Community Platform leaf already covers organization-operated communities. Recorded as resolved for this pass.
7. **Acquisition machinery** (Growth Boost-style ads-for-commission) — single-product; treated as variant, not common structure.

## Final Synthesis

The Paid Community Platform is the **venue pole of the purchase-to-access cluster**: software a host uses to run a community whose admission is organized by payment. Its world has three load-bearing structures — the participatory venue itself, host-authored purchase offers attached to the venue (whole or space bundles), and an access state that follows the payment state. Around these, mature products add the standard operated-community space set (discussions, chat, courses, events, directory, gamification), marketing/storefront surfaces, purchase-state automations, member billing self-service, and a host-side revenue loop (checkout, fees, payouts, taxes, refunds, comps). The Type's sharpest seams: monetization-organizes (vs Community/Private Community), venue-is-the-product (vs Creator Subscription/Fan Membership), curriculum-not-organizing (vs Course Commerce), venue-commerce-not-roster (vs Membership Management System). Definition survives the historical/regional check because it depends on the pay→venue-access conversion, not on any modern packaging.
