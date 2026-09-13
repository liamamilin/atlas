# Paid Community Platform

## Overview

A **Paid Community Platform** is software for running a community whose admission is organized by payment: the community host prices access to the venue, buyers join through checkout, and member access follows the state of that payment.

The defining structure is small:

```text
Community venue (hosted, participatory member spaces)
└── Purchase offer on admission (host-authored plan / pricing)
    └── Completed purchase → member access
        └── Access maintained while payment is active
            └── Access ends or degrades when payment lapses
```

Everything commonly associated with these products — free plans inside paid venues, tiered benefits, trials, courses, events, chat, gamification, landing pages, mobile apps — is widespread but is not what makes the product a paid community platform. A free, open community with no purchase offer is a community platform; a subscription to a creator's output stream with no participatory venue is a creator subscription. This Type sits precisely where the two overlap: the thing being sold is **access to a place where members participate**.

## Users & Context

Primary users:

- **The community host** — the operator of the venue: a creator, coach, expert, educator, or brand that charges for membership. The host designs the venue's spaces, authors the purchase offers, screens or approves applicants where desired, manages the member roster, and runs the money side (pricing changes, comps, refunds, payouts).
- **The paying member** — a participant who purchases access and then uses the venue like any community member: posting, replying, chatting, attending events, taking courses, messaging other members.

Secondary concerns: moderators and admins who help run the venue (some products add a dedicated billing-capable role), and prospective members — often funneled through free lead-magnet spaces or trials before purchasing.

The typical context is a host monetizing an audience through a standing community rather than through one-off content sales: coaching and practitioner groups, creator fan communities, expert/mastermind groups, education cohorts, and brand or customer communities run as paid spaces.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product stops being recognizable as a paid community platform:

- **The paid venue** — a hosted community container with participatory member spaces (discussions, feed, chat, events, courses, member directory — the mix varies by product). The venue itself is the product being sold; it is not an add-on to something else.
- **Purchase offers on admission** — the host authors named offers (plans/pricing) that define what a buyer pays and what that payment covers. An offer attaches to the whole venue, to an individual space, or to a bundle of spaces. Recurring payment is typical; one-time payment for permanent or fixed-term access is common.
- **Payment-state-linked access** — a completed purchase converts the buyer into a member with immediate access to what the offer covered. Access persists across renewals and ends or degrades when payment does: cancellation takes effect at the end of the billing period, failed payment can deactivate the plan, and the host can revoke or grant access manually (refund, comp, removal).
- **Host-side monetization management** — the operator surface that makes the offer and its access consequences manageable: offer authoring, a member/purchaser roster, billing operations (cancel, comp, refund, price changes), and revenue disposition (payouts, platform fees, tax handling per the platform's money posture).

The third structure is the one that organizes everything else: the purchase is not a donation or a content download; it converts into a **standing entitlement to a place**.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They make the Type practical but do not define it:

- **The standard space set** — discussion/feed spaces, chat spaces, direct messaging, member profiles and a searchable directory, events (sometimes paid or livestreamed), courses or a classroom area, gamification (points, levels, leaderboards), onboarding checklists.
- **Roles and permissions** — host, moderator, and member roles with per-space permissions; capability differences between full members and members who only purchased a single space or bundle.
- **Storefront and funnel surfaces** — a public landing page presenting the venue and its offers; offers placed on the landing page, on space pages, or reachable only via private link; free "lead magnet" spaces or mini-courses that funnel toward paid access.
- **Member billing self-service** — members manage their payment method, view invoices or purchase history, and cancel from their own settings.
- **Purchase-state automations** — tagging buyers, automatically granting access to the right spaces on purchase, win-back messaging on cancellation, rewards on renewal or upgrade.
- **Notifications, digests, mobile apps, search, moderation tooling, analytics** — both engagement metrics and revenue metrics.
- **Integrations** — SSO, webhooks/API, migration tooling for moving paying members from another platform.

### One Structure, Many Implementations

The Core Model is written conceptually; implementations differ:

```text
Concept:            Purchase offer on admission
Implementations:    subscription plans (monthly/annual/other intervals), one-time
                    purchase, freemium (free plan + paid plan in one venue),
                    tiered plans with per-tier benefits, paid single spaces or bundles

Concept:            Payment-state-linked access
Implementations:    instant access on checkout, access until period end on cancel,
                    deactivation on failed payment, host-side comp/grant/revoke,
                    price grandfathering for existing members

Concept:            Scope of the sale
Implementations:    whole-venue membership, space-scoped membership, standalone
                    course/event bundles inside the venue

Concept:            Money posture
Implementations:    platform-managed processing with payouts and platform fees,
                    host-owned payment processor, payments handled off platform,
                    app-store purchases inside branded mobile apps
```

A reader who encounters only one implementation (say, a monthly-subscription community) should still recognize one-time "lifetime access" venues or space-scoped selling as the same Type.

## How It Works

### The host's loop

```text
Create the venue and its spaces
→ author purchase offers (price, billing interval, what's included)
→ place the offers where prospects will find them
   (landing page, space pages, private share links)
→ optionally layer other gates on admission (screening questions, approval)
→ manage members: watch the roster, comp or refund, adjust pricing
→ run the revenue side: payouts, fees, taxes, churn follow-up
```

### The member's loop

```text
Discover the venue (or receive an invite/link)
→ review the offer page for the venue or a specific space
→ pay (checkout) — access starts immediately in the mature pattern
→ participate inside the spaces the offer covered
→ renew automatically while subscribed
→ cancel from self-service settings — access runs to the end of the paid period
```

### The billing lifecycle

The access state tracks the payment state throughout:

- **Activation** — payment converts to access without manual approval in typical implementations ("pay and they're in"); products that screen members add question/approval gates *on top of* payment, not instead of it.
- **Renewal** — recurring offers keep access alive across billing periods; upgrades and plan changes move the member between offers, with proration in some products.
- **Cancellation** — initiated by the member (or host); access continues to the end of the current billing period, then lapses.
- **Lapse** — failed payment can put the plan into a past-due state and eventually deactivate it, ending access.
- **Exceptions** — refunds and comps are host-side actions: a refund typically accompanies revoked access; a comp grants paid access without payment. Some products let the host close admission temporarily or show a host-authored message at the moment of cancellation.

### Selling parts of the venue

Offers need not cover the whole venue. Mature products let the host sell access to specific spaces or bundles — for example, a free community where premium spaces are individually purchasable, or a standalone course space sold without full community membership. In that architecture, buyers of a single space are members of the venue in a limited sense: they participate in what they paid for and not in what they did not.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Venue landing / offer page

The storefront surface.

- presents the venue, its promised value, and its purchase offers
- primary actions: choose an offer, start a trial where offered, begin checkout

### Host admin

The operator console, usually organized around venue, people, and money.

- **Offer/pricing configuration** — create and edit plans, set intervals and prices, define what each offer includes, place offers, set trials or promo codes
- **Member roster / member detail** — see each member's plan and access, grant or revoke, move between plans, comp, remove
- **Billing operations** — cancellations and their notifications, refund handling, payout status, fees and taxes, revenue reports
- **Venue configuration** — spaces, categories, roles, rules, branding, discovery settings
- **Analytics** — engagement and revenue views

### Member-side venue

The participatory surface after purchase.

- **Feed / discussion spaces** — post, reply, react; per-space membership
- **Chat spaces and direct messaging** — live conversation within the access boundary
- **Events and livestreams** — RSVP, attend, replays; occasionally ticketed separately
- **Courses / classroom** — structured content with progress, sometimes gated behind plan or progress
- **Member directory and profiles** — who else is here; member discovery
- **Billing self-service** — plan and payment management, invoices, cancellation

## Important Rules / Behaviors

- **Access follows payment, not attendance or activity.** A lapsed payment — not a rule violation, not inactivity — is what ends an entitlement (rule violations are handled separately through moderation).
- **Cancellation is not immediate expulsion.** The standard behavior is access until the end of the paid period; immediate removal is reserved for host action (removal, refund-with-revoke) or member account deletion.
- **Payment is the primary gate, but not the only one.** Screening questions and approval gates are commonly layered onto a paid offer; invite-only and hidden (link-only) offers exist for private sales.
- **The scope of the offer defines the entitlement.** Whole-venue offers grant full membership; space-scoped offers grant a limited membership whose capabilities are visibly narrower (for example, reduced venue-wide messaging or search).
- **Price changes typically protect existing members.** Grandfathering — new members pay the new price, existing members keep the price they joined at — is the commonly documented pattern.
- **Refunds and comps are host-discretionary.** The platform usually processes the money but leaves the refund decision and execution to the host; where app-store purchases are involved, refunds route through the app store instead.
- **One-time offers create durable access.** A one-time purchase does not lapse; it ends only by host action or account deletion, which is why one-time and recurring offers coexist as distinct choices rather than a single model.

## Variants

- **Offer-architecture variants** — single subscription; freemium venue with in-venue upgrade; multi-tier benefits; one-time/lifetime access; trials and installment plans as purchase modifiers.
- **Scope variants** — whole-venue selling; premium spaces sold individually inside a free venue; standalone course or event bundles inside the community shell.
- **Admission-posture variants** — pay-first open venues; screened venues where approval and payment combine; waitlisted and temporarily-closed venues; hidden offers sold via private link.
- **Payment-posture variants** — platform as merchant of record (platform collects, remits taxes, pays out); host-owned processor; payments off platform; in-app purchases inside host-branded mobile apps; token-gated admission in a niche variant.
- **Audience variants** — creator fan communities; coaching/mastermind groups; education cohorts; expert-practitioner networks; brand/customer communities run as paid spaces.
- **Surface variants** — web-first venues, native-mobile-first venues, and venues running inside host-branded apps.
- A related market pattern: chat and streaming products selling paid, subscriber-only community spaces as a feature of their own venues. This is the same purchase→venue-access conversion realized inside another Type rather than a standalone product.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Community Platform | sibling underlier | there the operated community container defines the Type and monetization is optional; here a purchase converting into venue access organizes the product |
| Private Community Platform | adjacent | there the closed boundary is the organizing object and payment is one admission mechanism among several; here the purchase and its billing lifecycle are the primary admission machinery |
| Creator Subscription Platform | cluster sibling | there a purchase converts into a standing relationship with the creator's output stream, with community access at most one declared benefit (often hosted elsewhere and synced); here the venue itself is the fulfillment object |
| Fan Membership Platform | cluster sibling | there the product is the creator's membership program with declared benefits; remove the program and keep the venue and it becomes this Type |
| Creator Course Commerce Platform | cluster sibling | there the purchase converts into curriculum access; here courses are a space type inside the venue, not the organizing object |
| Coaching Commerce Platform | cluster sibling | there the purchase converts into human service time; here into venue access — coaching can exist inside a paid community as an event or space without changing the Type |
| Membership Management System / AMS | adjacent | there the system of record is an organization's membership roster, dues cycle, and benefits administration; here the record of value is venue access sold through offers |
| Subscription Billing Platform | adjacent | generic recurring invoicing and entitlement machinery with no venue or community operations; this Type embeds a billing loop scoped to venue access |
| Community Chat Platform | adjacent | a live chat container; chat may be one space type here, but the chat container does not organize a purchase→access loop around the venue |
| Event Ticketing Platform | adjacent | one-off event admission; here a standing venue entitlement — though paid events can be sold inside a paid community as one-off commerce |
| Online Donation / Tip Platform | distinct | money with no entitlement: no access conversion, no standing venue membership |

## Representative Products

- Circle
- Mighty Networks
- Skool

These span different product philosophies (all-in-one branded community home; host-centric engagement platform with native apps; minimalist group-with-classroom) and customer tiers (solo hosts through enterprise branded-app programs). The defining model was also checked against older and regional shapes — pay-to-access forum setups and paid-circle communities — to confirm the definition does not depend on the current all-in-one packaging.

## Sources

Research date: **2026-09-08**

- Skool Help Center — Payments category, "How to setup pricing for the group?", "Skool Payments FAQs" — https://help.skool.com/
- Mighty Networks Help Center — "Payments and Access" section, incl. "How Do I Gate Access to All or Parts of My Mighty Network?", "What is a Full vs. Limited Membership?", "What Happens When a Member Cancels or Requests a Refund" — https://docs.mightynetworks.com/
- Mighty Networks — product pages: https://www.mightynetworks.com/ , https://www.mightynetworks.com/payments
- Circle — Pricing page: https://circle.so/pricing

> Sourcing limitation: Circle's help center was not reachable from the research environment (JavaScript-rendered; operational articles could not be fetched), so Circle claims rest on its product/pricing pages only. Platform-native chat subscriptions and self-hosted forum paywalling could not be verified this pass and are described only as market patterns, without product-specific claims. Precise figures (fee schedules, payout timing, limits, trial lengths) are intentionally omitted from this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
