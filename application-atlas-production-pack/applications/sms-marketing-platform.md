# SMS Marketing Platform

## Overview

An **SMS Marketing Platform** is a marketer-side platform for building and keeping a **consented audience of phone numbers** (subscribers) and sending **marketing text messages** to them through **telecom carriers**, with opt-out handling and measurement built into the send loop.

The defining core is small:

```text
SMS subscriber base
  (phone numbers recorded as opted in to this sender's marketing messages,
   minus honored opt-outs)
└── Text message composition in the SMS format
    └── Carrier-mediated delivery
        (through telecom carriers via registered sender numbers)
        └── Opt-out enforcement and record
        └── Delivery & engagement measurement
```

Everything commonly bundled with modern products — keyword opt-in tools, segments, automation flows, MMS media, coupons, two-way inboxes, AI copywriting — is standard or optional capability layered on this core, not what makes the product an SMS marketing platform.

Two things distinguish this Type from sibling campaign-messaging Types such as email or push notification marketing:

- the **channel mechanics**: phone-number addressing, short text messages, per-message telecom economics, delivery into the phone's native messaging thread;
- the **consent regime**: commercial texting is governed by telecom regulation and carrier policy, so recorded opt-in, machine-enforced opt-out (STOP-class keywords), quiet-hours discipline, and carrier registration of sender numbers are structural parts of the product, not afterthoughts.

## Users & Context

**Primary users** are marketing-side operators:

- **Ecommerce and retail marketing teams** — the dominant modern segment — grow subscriber lists at checkout and on-site, run promotional campaigns and cart/purchase automations, and measure revenue per send.
- **Local and mid-size business operators** (services, hospitality, events) send offers, reminders, and announcements to customers who opted in, often self-serve.
- **Nonprofit and political digital teams** run fundraising appeals, alerts, and mobilization sends to supporter lists, commonly integrated with donor or advocacy systems.

**Secondary users** include agency operators who run texting programs for clients, staff who answer replies in a shared inbox (support, fundraising, store teams), and administrators who configure sender numbers, quiet hours, and user access.

The work context is campaign operations: growing the consented list, composing and testing messages, scheduling and automating sends within consent and quiet-hours rules, and monitoring delivery, replies, opt-outs, and revenue.

## Core Model

### The defining core

```text
SMS subscriber base
└── Text message composition (SMS format)
    └── Carrier-mediated delivery via registered sender numbers
    └── Opt-out enforcement and record
    └── Measurement per send
```

Five structures. Remove any one and the product stops being recognizable as this Type:

- **SMS subscriber base** — the platform's record of who can be reached: phone numbers with recorded marketing consent, each carrying the opt-in source and the opt-out state. Reachability is the conjunction *opted in and not opted out*: a number that matches every targeting condition is still unreachable without recorded consent, and a number that has texted a stop keyword is excluded permanently. Mature products commonly place a person layer over the numbers — a profile with attributes, custom fields, and (in commerce settings) order or donor data — so one person may map to one or more reachable numbers.
- **Text message composition in the SMS format** — the short text message is the unit of communication. Products document length and encoding mechanics that determine how a message splits for delivery. Media (images, video, contact cards) extends the format as MMS; richer card-style messaging is an emerging extension with SMS fallback. Messages carry required elements such as opt-out instructions, and links are handled through platform-managed tracking (carriers commonly block third-party link shorteners).
- **Carrier-mediated delivery** — messages travel through telecom carriers to the recipients' phone numbers, sent from a registered **sender number** (a short code, a local/long code, a toll-free number, or a regional equivalent such as an alphanumeric sender ID). Sender numbers typically require registration or verification with carriers before they can send at scale, and delivery outcomes depend on carrier acceptance.
- **Opt-out enforcement and record** — stop-class reply keywords (and equivalent opt-out paths) are honored and recorded immediately and permanently; opted-out numbers are suppressed from future marketing sends. Consent and opt-out records are retained because the sender, not the platform, bears the burden of proving consent in many jurisdictions.
- **Measurement** — every send records delivery outcomes (with carrier-level failure detail in mature products), link clicks, opt-outs, and — where the platform is integrated with commerce or fundraising systems — downstream conversions and revenue attributed to sends. This is what makes the product a *marketing* platform rather than a bulk-texting utility.

### Standard capabilities of mature products

These are widespread across the researched sample and expected in the market, but they extend the core rather than define it:

- **Consent capture surfaces** — text-to-join keywords on sender numbers; web sign-up forms, checkout checkboxes, and on-site popups/landing pages; tap-to-text and click-to-text links; QR and print promotion; imports of previously collected lists, gated by compliance checks or certifications. Disclosure language is required at every opt-in point, and double opt-in (a confirming second action) is commonly used — in the US it is a carrier requirement for cart-abandonment messaging.
- **Profiles, attributes, and segments** — saved, dynamically evaluated audience groups built from properties, behavior, engagement, opt-in source, carrier, or geography.
- **Campaign types** — one-time broadcasts; scheduled sends; recurring sends; multi-message campaign sequences; triggered automations (welcome, abandoned cart, post-purchase, win-back); API-triggered sends.
- **Message design machinery** — personalization variables, platform-managed tracked links with attribution parameters, coupons and offers, MMS media, emoji/encoding handling, and automatic insertion of required opt-out language.
- **Two-way reply surfaces** — a shared inbox for incoming replies and autoresponders; in some products AI-assisted reply handling with human review.
- **Delivery governance** — quiet hours managed or enforced per recipient's local timezone; frequency discipline (skip-recently-messaged rules, per-subscriber caps, send throttling).
- **Compliance apparatus** — consent/audit records, sender-number registration and verification workflows, content restriction enforcement (categories carriers prohibit or restrict, with age verification for permitted restricted goods such as alcohol), and separation of transactional from marketing messaging.
- **Analytics and experimentation** — delivery reports, click tracking, opt-out tracking, conversion/revenue attribution, and A/B testing of message variants.
- **Integration and billing shape** — connections to ecommerce platforms, CRMs/donor systems, and automation tools; APIs and webhooks; costs tied to message volume, with spend and message counts visible in-product.

### One structure, many implementations

```text
Concept:  Sender identity
Implementations:  dedicated short code, long code (10DLC in the US), toll-free number,
                  alphanumeric sender ID (regional markets)

Concept:  Consent capture
Implementations:  keyword (text-to-join), checkout checkbox, web form/popup,
                  tap-to-text link, QR/print, certified import

Concept:  Reachable audience
Implementations:  per-number consent state; person profile over one or more numbers;
                  segment membership evaluated at send time

Concept:  Rich message
Implementations:  MMS media; card-style rich messaging (RCS) with automatic SMS fallback
```

## How It Works

### Establish the sending identity (one-time setup)

```text
Acquire or port a sender number (short code / long code / toll-free, per market)
→ register or verify it with carriers (brand and use-case registration where required)
→ configure the platform's compliance defaults (opt-out language, quiet hours)
→ test delivery
```

### Grow the consented audience

```text
Publish opt-in points (keyword, form, checkout, popup, tap-to-text, QR)
→ a person takes the opt-in action, seeing required disclosure language
→ the platform records the number, the consent, and the source
→ an automated confirmation/compliance message goes out
→ optionally: a second confirmation step (double opt-in)
→ imports of existing lists pass a compliance gate or certification
```

### Compose and target

```text
Create a campaign (or an automation)
→ select or build a segment
→ write the message; personalize with profile variables
→ add a tracked link and/or offer/coupon; add media (MMS) where wanted
→ preview per device; send test messages
→ required opt-out language is attached per product rules
```

### Send and govern delivery

```text
Choose the delivery plan: send now | scheduled | recurring | triggered by behavior | via API
→ the audience is evaluated at send time
→ platform-level controls apply (quiet hours in the recipient's timezone,
   frequency rules, throttling)
→ messages queue through carriers to each reachable number
→ a scheduled send can typically be cancelled or edited while pending;
   delivered messages cannot be recalled
```

### Handle replies and opt-outs

```text
Replies arrive in the platform (shared inbox / autoresponders)
→ help-type replies answered by staff (or drafted by AI, human-approved)
→ STOP-class replies processed immediately and permanently
→ opted-out numbers are suppressed from subsequent marketing sends
```

### Measure and iterate

```text
Delivery report: sent → delivered/failed (with carrier reasons) → clicks → opt-outs
→ conversions/revenue attributed to sends (commerce and fundraising integrations)
→ iterate: duplicate the campaign, adjust copy/timing/audience; A/B test variants
→ hygiene: win-back or prune unengaged subscribers to protect deliverability
```

The recurring operational loop is: **grow and clean the consented list → target → send within the rules → handle replies and opt-outs → measure → refine.**

### Core vs standard vs optional

**Defining core** — without these, not this Type:

- consent-gated phone-number subscriber base
- SMS-format message composition
- carrier-mediated delivery via registered sender numbers
- opt-out enforcement and record
- per-send measurement

**Standard capabilities** — present in most modern products:

- keyword/form/checkout consent capture with disclosure language
- profiles, attributes, segments
- broadcast / scheduled / recurring / multi-message / triggered / API sends
- personalization, tracked links, coupons, MMS
- two-way inbox and autoresponders
- quiet hours and frequency discipline
- consent records, number registration, content restrictions
- delivery/click/revenue analytics, A/B testing
- integrations and volume-based billing

**Optional / variant** — depends on segment, geography, and product philosophy:

- MMS depth and rich-card channels (RCS-class) with SMS fallback
- email or other channels sold alongside SMS
- AI copy, send-time optimization, AI reply drafting
- text-to-give payment flows, text-to-win/text-to-vote tooling
- alphanumeric sender IDs and other regional sender types
- multi-country sending under differing national regimes

## Interfaces

Exact layouts and names vary by product; the following surfaces are common.

### Subscribers / contacts

- Purpose: manage the consented audience.
- Typical information: phone numbers, consent and opt-out states with sources, profile attributes, list-growth source, engagement history.
- Primary actions: import/export with compliance checks, inspect a subscriber, tag/segment, remove.

### Campaign composer

The central working surface.

- Purpose: write a message and bind it to an audience and delivery plan.
- Typical information: message editor with character/segment feedback, audience selector with size estimate, schedule options, per-device preview, test-send.
- Primary actions: compose, personalize, add links/offers/media, schedule or send, duplicate, cancel pending sends.

### Campaign dashboard

- Purpose: oversee all campaigns and automations and their states.
- Typical information: names, status (draft/scheduled/sending/sent/paused), headline metrics.
- Primary actions: create, pause/resume, edit pending sends, archive, open report.

### Segments / audience builder

- Purpose: define who receives what.
- Typical information: filter conditions (properties, behavior, engagement, opt-in source, geography), estimated audience size.
- Primary actions: create/edit/clone segments, exclude audiences.

### Inbox / replies

- Purpose: handle two-way replies from subscribers.
- Typical information: conversation threads with subscriber context, autoresponder status.
- Primary actions: reply, assign, tag, opt out, escalate.

### List-growth tools (keywords, forms, popups)

- Purpose: create and manage the opt-in machinery.
- Typical information: keywords bound to sender numbers, confirmation/compliance message text, form/popup designs, display rules.
- Primary actions: set up keywords, edit confirmation messages, build forms/popups, review opt-in performance.

### Analytics / reports

- Purpose: quantify delivery, engagement, and revenue impact.
- Typical information: delivery with failure reasons, clicks per link, opt-outs per send, conversion/revenue attribution, list-growth and opt-out trends.
- Primary actions: filter by campaign/date, define attribution windows, export.

### Compliance & settings

- Purpose: keep the channel lawful and deliverable.
- Typical information: sender numbers and their registration status, quiet-hour configuration, message limits, user roles and access.
- Primary actions: register/verify numbers, configure quiet hours and frequency rules, manage users.

## Important Rules / Behaviors

### No consent, no sending

The most important rule of the Type: **a phone number alone is not consent**. Having someone's number, or their consent for another channel (email), does not permit marketing texts; consent must be explicit for SMS, untied from purchase conditions, and recorded with its source. Purchased or scraped lists are categorically invalid. Products enforce this through capture design, disclosure language, import gating, and consent records retained for proof.

### Opt-out is permanent, and carrier state can differ from platform state

Stop-class keywords are honored immediately and permanently. A nuance documented by products: the platform's record and the carriers' record of a subscriber's state can diverge — for example, after a stop on certain number types, carriers may require the subscriber to text a resubscribe keyword before delivering anything, regardless of what the platform's profile shows. Resubscribe paths depend on how the person opted out and which sender-number type is in use.

### Quiet hours are part of the channel

Sends are commonly managed — and in several products hard-enforced by the platform — against quiet hours in the **recipient's** local timezone, with stricter limits in some jurisdictions (some impose earlier evening cutoffs or per-subscriber message caps). Opt-in confirmations and opt-out acknowledgments are typically exempt so that consent actions are never delayed.

### Carriers gate the channel

The platform does not control delivery unilaterally. Sender numbers must be registered and verified; message content is screened against carrier rules (prohibited or restricted categories, spam filtering, link policies); some behaviors are capped by industry-wide carrier policy — for example, cart-abandonment automations are commonly limited to a small number of messages within a short window. Failed or filtered numbers show up in delivery reports as a first-class operational concern.

### Economics are per message

Cost scales with sending volume, and message length/encoding affects how a message splits — so copy length is an economic decision, not only a design one. Volume-based spend is visible in-product, and some products filter unreachable numbers before sending so senders are not billed for them.

### The receiving surface is the phone's native messaging thread

Messages land in the same app as personal conversations, with no subject lines, no inbox placement controls, and rendering governed by the device and carrier. This is why brevity, sender identity, and immediate recognition matter structurally, and why media arrives as MMS rather than layout-controlled content.

### Marketing and transactional messaging are separated

Products commonly distinguish marketing consent from transactional consent (order updates, appointments, receipts), with different rules for collection and sending; mixing them is a compliance risk.

## Variants

Common variants of the Type:

- **Ecommerce-centric platforms** — checkout and popup opt-in, abandoned-cart and post-purchase automations, coupons, revenue attribution; often sold alongside email or embedded in a commerce marketing suite.
- **Nonprofit / political fundraising platforms** — text-to-give keyword donations, donor-profile segmentation, rapid-response mass sends, integration with donor CRMs and donation platforms.
- **Generic SMB mass-texting platforms** — self-serve list tools, contests and polls, appointment-style reminders, simple shared inbox; volume-based credits.
- **Enterprise / agency programs** — high-throughput sending, governance, multiple brands or numbers, dedicated support.
- **Pure-play vs suite-embedded** — SMS as the entire product vs SMS as one channel inside an email-first or omnichannel marketing platform (the same core loop appears in both).
- **Regional variants** — sender-number types and consent mechanics differ by market (e.g., alphanumeric sender IDs and long codes in markets outside the US); multi-country products document per-country rules and availability.
- **Channel-extension variants** — deeper MMS, and rich-card messaging (RCS-class) delivered with automatic SMS fallback, emerging as a sibling surface rather than replacing the core.

A variant remains a variant while the defining loop still describes it: consented numbers → short text messages → carrier delivery → enforced opt-out → measurement. When two-way conversation becomes the center rather than campaigns, the product is drifting toward conversational business messaging; when the platform becomes channel-agnostic orchestration across many channels, it is drifting toward marketing automation territory.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Email Marketing Platform | sibling channel Type | Same campaign grammar (audience → message → schedule → measure), but delivery is inbox-based, addressed by email addresses, without per-message telecom costs, and governed by anti-spam consent rather than telecom consent regimes; opt-out is an unsubscribe link, not a reply keyword. |
| Push Notification Marketing Platform | sibling channel Type | Push addresses device/browser registrations through OS push services behind an OS permission gate, renders as transient banners, and carries no per-message cost; SMS addresses phone numbers through carriers behind a regulatory consent gate, lands in the native messaging thread, and costs per message. |
| Mobile Marketing Platform | broader umbrella | Includes paid user acquisition, app-store optimization, mobile advertising, and other channels; the SMS platform is one owned channel's machinery within that umbrella. |
| Marketing Automation Platform | overlapping capability | Channel-agnostic orchestration of journeys and lifecycle programs. Triggered automations appear here too, but this Type's identity is the SMS channel's consented audience, carrier delivery, and compliance mechanics. |
| Marketing Campaign Management Platform | adjacent | Manages campaigns across channels, teams, budgets, and approvals; does not itself own sender numbers, consent records, or carrier delivery. |
| SMS gateway / CPaaS (developer infrastructure) | upstream substrate | Sends SMS via carriers through APIs but has no consent-gated subscriber base, no campaign lifecycle, no opt-out machinery, no marketing measurement. Adding that layer is exactly what creates this Type. |
| Customer-to-Business Messaging Application | conversational neighbor | Centers on person-initiated conversations with a business (support, concierge); this Type centers on marketer-initiated campaigns to a consented audience. The two-way inbox here serves campaign replies, not conversation-first service. |
| Church Communication Platform | audience-tuned sibling | Shares the messaging grammar but its audience is the church's own people records with church-life consent capture and congregational jobs, rather than a commercial subscriber base under telecom consent regimes. |

The sharpest boundaries: **remove the marketing layer (consented subscriber base, campaigns, opt-out machinery, measurement) and this Type becomes a bulk-SMS gateway; swap the channel mechanics (inbox delivery or OS push delivery for carrier delivery) and it becomes the email or push marketing sibling.**

## Representative Products

- Tatango (marketed as momoGood) — pure-play veteran of the category (since 2007), now focused on nonprofit/political fundraising texting
- SimpleTexting — self-serve SMB pure-play SMS/MMS platform
- Attentive — enterprise ecommerce messaging (SMS and email), conversational-commerce philosophy
- Klaviyo — SMS as an embedded channel of an email-first B2C CRM/marketing platform
- Postscript — Shopify-vertical SMS/MMS platform

The definition was checked against the category's shortcode-keyword generation (its origin era), against regional sender-number markets, and against the CPaaS gateway as a negative case, to avoid over-fitting to today's ecommerce- and AI-heavy market.

## Sources

Research date: **2026-09-07**

Official product documentation (Tier-1 unless noted):

- SimpleTexting Knowledge Base — https://help.simpletexting.com/en/ (SMS Campaigns; Add Contacts; Compliance collections)
- Attentive Help Center — https://help.attentive.com/ (Campaigns and Settings categories)
- Klaviyo Help Center — https://help.klaviyo.com/hc/en-us/categories/29173800271259 (SMS category; "Understanding SMS consent collection")
- Postscript Help Center — https://help.postscript.io/en/ (Compliance and Campaigns collections; "SMS Marketing Compliance Overview")
- Tatango / momoGood — https://www.tatango.com/ , https://www.momogood.com/messaging (official product pages; Tier-2 — see sourcing note)

> Sourcing note: Tatango's public help center is no longer reachable; its observations were documented from the vendor's official product pages rather than operational help documentation, and claims resting on that sample are kept at lower precision. Regulatory specifics (statute names, carrier policy categories, jurisdictional quiet-hour differences) are described qualitatively; exact numeric rules (character/segment counts, specific clock windows, per-jurisdiction caps, plan limits) vary by product, number type, and jurisdiction, and are intentionally not stated in this document. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
