# Research Notes — SMS Marketing Platform

Research date: 2026-09-07
Methodology: WORKFLOW v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what an SMS Marketing Platform actually is as an Application Type: its defining core structure, standard capabilities, variants, and boundaries against neighboring marketing/messaging Types — based on how real products work, not vendor positioning.

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis):** a marketer-facing platform for building a consented audience of phone numbers (subscribers) and sending marketing text messages to them through telecom carriers, with opt-out/compliance machinery and measurement as first-class structures.
- **Who uses it (hypothesis):** ecommerce brands (dominant modern segment), local/SMB businesses, nonprofits and political organizations; marketers, not developers.
- **Nearest neighbors (hypothesis):** Email Marketing Platform and Push Notification Marketing Platform (same campaign grammar, different channel mechanics), Mobile Marketing Platform (broader umbrella), Marketing Automation Platform (channel-agnostic orchestration), CPaaS / SMS gateways (infrastructure without marketing layer), Customer-to-Business Messaging (conversational surface), Church Communication Platform (audience-tuned sibling flagged in STATUS.md).
- **Unknowns:** how consent is modeled and captured per product; whether two-way conversation is definitional or optional; sender-number type taxonomy (short code / long code / toll-free / alphanumeric); how deep compliance enforcement goes; whether MMS/RCS is core; audience model (number-only vs person profile).

## Research Questions

1. What is the audience model — subscribers, phone numbers, consent state, profiles/attributes?
2. How is consent captured (keywords, forms, checkout, imports) and what are the documented consent rules?
3. How is opt-out handled (STOP-class keywords, suppression, resubscribe rules)?
4. What sender identities exist (short codes, long codes/10DLC, toll-free, alphanumeric) and what setup/verification do they require?
5. What campaign/send objects exist — broadcast, scheduled, recurring, multi-message flows, triggered automations, API sends?
6. What message design machinery exists — personalization, links, coupons, MMS, encoding/character mechanics, opt-out language?
7. What compliance machinery is structural — quiet hours, content restrictions (SHAFT), carrier registration, consent records, state/country laws?
8. What delivery governance exists — throttling, smart sending/frequency controls, carrier filtering?
9. Is two-way conversation / inbox part of the core or a common add-on?
10. What measurement exists — delivery reports, clicks, conversions/attribution, A/B testing?
11. Where are the boundaries vs email/push marketing, CPaaS, marketing automation, mobile marketing, conversational business messaging?
12. Would older / differently-positioned products still fit the definition (historical check)?

## Representative Products

| Product | Position | Why sampled |
|---|---|---|
| Tatango (marketed 2026 as momoGood) | Pure-play veteran (since 2007), now nonprofit/political fundraising texting | Longest-lived pure-play; audience pole outside ecommerce; rich compliance documentation |
| SimpleTexting | Self-serve SMB pure-play SMS/MMS | Clearest SMB pole; full keyword/number/inbox/analytics surface documented |
| Attentive | Enterprise ecommerce messaging (SMS+email), conversational commerce philosophy | Enterprise tier; campaign composer, Smart Sending, quiet hours, attribution documented |
| Klaviyo | Email-first B2C CRM suite with SMS as an embedded channel | Suite-embedded pole; strongest consent-rule documentation; multi-country sending numbers |
| Postscript | Shopify-vertical SMS/MMS pure-play | Vertical variant; most explicit compliance/regulatory documentation (TCPA, CTIA, state laws, SHAFT, carrier rules) |

Coverage: pure-play vs suite vs vertical packaging; self-serve SMB vs enterprise; SMS-only vs multi-channel; consumer-commerce vs nonprofit/political audiences; US-centric vs multi-country sending.

## Sources

All Tier-1 official documentation, fetched 2026-09-07. One failed path (Tatango's Zendesk help center is closed); Tatango was documented from its official product site instead. Zero other failures.

- Tatango/momoGood — https://www.tatango.com/help/ (redirects to product site), https://www.momogood.com/messaging (official product page served on Tatango domains; references platform.tatango.com API)
- SimpleTexting — https://help.simpletexting.com/en/ (collections: SMS Campaigns, Add Contacts, Compliance)
- Attentive — https://help.attentive.com/ (= help.attentivemobile.com), categories: Campaigns (6084266093076), Settings (6084290680340)
- Klaviyo — https://help.klaviyo.com/hc/en-us/categories/29173800271259 (SMS), article 360035056972 (Understanding SMS consent collection)
- Postscript — https://help.postscript.io/en/ (collections: Compliance 18197737, Campaigns 18197742), article 13563920 (SMS Marketing Compliance Overview)

---

## Product Observations

### Tatango / momoGood (evidence layer A — official product site; help center closed, noted as sourcing limitation)

- **Positioning:** "nonprofit text messaging platform" for SMS/MMS/RCS fundraising, mass texting, text-to-give, two-way donor conversations; "built for fundraising. Not generic marketing." Political/PAC messaging use case. Heritage: "since 2007", "10+ billion text messages sent".
- **Compliance engine (documented as platform-enforced):** consent capture from keywords, web forms, checkout, imports — with source and timestamp kept on every subscriber; STOP/UNSUBSCRIBE "honored instantly and permanently" with exportable audit trail; quiet hours held per recipient timezone; throttling; number/carrier hygiene filtering (landlines, disconnected/ported-out numbers, spam-flagged carriers) before send, with "$0 billed for filtered numbers".
- **Carrier infrastructure:** 10DLC carrier registration handled ("brand & campaign tier kept current"); STIR/SHAKEN attestation; carrier-grade redundancy across providers; burst capacity for time-sensitive sends.
- **Audience model:** subscribers with consent log; AI donor profiles from giving history/behavior; behavioral segments (lapsed donors, recent givers, event attendees) updating in real time.
- **Sending:** mass texting to entire list; text-to-give (keyword + amount, receipt + recurring upsell + thank-you automatic); two-way conversations routed to team with full donor history; AI-drafted replies with human review.
- **Message machinery:** MMS and RCS with automatic SMS fallback; A/B testing (up to 4 variants on a test share, winner auto-promoted); tracked short links with click attribution by segment/campaign/donor tier; webhook confirmations when gifts complete.
- **Analytics:** open rates, click-through, gift attribution, revenue per send, by segment/campaign/donor tier.
- **Integrations:** nonprofit CRMs and donation platforms (Salesforce, Blackbaud, Fundraise Up, Classy, ActBlue-class), Zapier, REST API + webhooks + developer sandbox via platform.tatango.com.

### SimpleTexting (evidence layer A — official Intercom knowledge base)

- **Structure of docs (itself evidence of the object model):** Texting 101 / Compliance / Add Contacts / Manage Contacts / SMS Campaigns / MMS Campaigns / The Inbox / Local Numbers / Toll-Free Numbers / Short Codes / Automations / API & Integrations / Settings and Billing / Analytics / Add Multiple Numbers / Team Members.
- **Audience model:** contacts with opt-in/opt-out states; import/export with "Import Guidelines and Rules"; custom fields for personalization; audience segments; segmentation by click behavior.
- **Consent capture:** text-to-join keywords (setup, alternate confirmation messages, triggers on keywords, promotion rules, keywords bound to numbers); web sign-up forms; mobile sign-up widget; click-to-text button; text-to-win contests; text-to-vote polls; "automatic compliance message" sent on opt-in (configurable); opt-in/opt-out explainer.
- **Campaigns:** send first campaign; templates; duplicating; scheduling; recurring campaigns; detailed delivery report; personalization via custom fields; dynamic URL pre-fill from custom fields.
- **Channel mechanics documented:** "What carriers can SimpleTexting reach?"; "Why carriers don't allow bit.ly and other third-party link shorteners" (platform provides link shortening/tracking instead); "Why is my message caught in monitoring?" (carrier spam filtering); "Why don't some of my contacts receive my messages?"; special-character/encoding artifacts article; line-break article; message-count limits article.
- **Two-way:** The Inbox collection (shared inbox for replies).
- **Compliance:** Complying with the Law; Express Consent; TCPA Compliance; Free Compliance Message; CTIA audit explainer; spam policy; why a number or message can be blocked; restricted messaging content (cannabis/CBD; donations/fundraising rules); HIPAA (SMS is not HIPAA compliant).
- **Numbers:** local numbers, toll-free numbers, short codes as separate product surfaces; multiple numbers per account.

### Attentive (evidence layer A — official Zendesk help center, Campaigns + Settings categories)

- **Campaigns (Campaign Composer):** single-message and multiple-message text campaigns; schedule a campaign; recurring campaigns; pause and edit a campaign or campaign message; copy/delete campaign messages; campaign performance and metrics; Campaign messages vs message segments; "How message character counts are calculated in text messages".
- **Message design:** add images, video, or a contact card to a text message (MMS); dynamic links and variables (personalization); custom link tracking parameters; offers in campaigns; "Message opt-out language" and "International message opt-out language" (compliance language handled by product).
- **AI:** Send Time AI (send at the right time); Copy Assistant (generate SMS copy); Audiences AI (targeting).
- **Settings:** Smart Sending (skip messaging people recently messaged — frequency discipline); Quiet hours; Autoresponders; company/region settings; Sending Time Zone; custom attributes; contact cards; link tracking (global + per-message + attribution settings); user access and permissions; 2FA; billing ("View your spending and message counts" — per-message spend visible).
- **List growth (root):** sign-up units ("mobile bubbles, landing pages, and more") to invite opt-in; welcome journeys with offers; subscriber segments; Concierge ("personalized, people-powered conversations at scale" — two-way); Email as sibling channel; APIs/developer docs.
- **FAQs:** attribution model; shortcodes.

### Klaviyo (evidence layer A — official help center SMS product category + consent article)

- **SMS as product within suite:** SMS category with sections: Getting started with SMS (31 articles), Grow your SMS list (15), Send SMS campaigns (15), Send SMS from flows (9), SMS segments and profiles (7), SMS compliance and deliverability (33), Analyze SMS performance (4), RCS (12). Klaviyo also sells email, push, WhatsApp, reviews, etc. — SMS is one channel of a B2C CRM/marketing platform.
- **Consent rules (detailed, quoted):** "SMS is more regulated than most other marketing channels"; individuals must explicitly agree; consent must be **separate from every other channel** (separate checkbox/button; a general "agree to marketing" is insufficient in most countries); a single consent cannot cover multiple brands; "Lead generation, affiliate related, or purchased lists are not valid SMS consent"; cannot force or appear-to-force consent as a condition of purchase; disclosure language required at every opt-in point (forms, checkout, email banners, social, API-fed sources); **double opt-in is a US carrier requirement for cart-abandonment flows**; having a phone number is not consent; email consent is not SMS consent.
- **Consent storage:** consent stored on profiles ("how Klaviyo stores consent"); transactional vs marketing SMS consent distinguished; upload of SMS contacts with add/remove of consent classes.
- **Opt-out/resubscribe mechanics:** STOP keyword; for toll-free numbers carriers only deliver after the user texts START/UNSTOP — profile may show opted-in but carriers won't deliver until then (carrier-state vs platform-state distinction documented); resubscribe paths differ by number type and opt-out method.
- **Consent capture surfaces:** sign-up forms (incl. tap-to-text forms that open the messaging app with a pre-filled message), checkout consent for Shopify/WooCommerce/BigCommerce/Magento/PrestaShop, subscribe links for ads/social (incl. Instagram stickers), email-to-SMS conversion of engaged email subscribers, API consent transfer.
- **Numbers:** "Understanding SMS sending numbers" per country — number types differ per country and what each type can do; numbers may need verification/registration before use; SMS availability varies by country (multi-country product).
- **Sending objects:** campaigns (Send SMS campaigns section) and flows (Send SMS from flows, e.g. SMS welcome flow, abandoned cart); segments and profiles; A/B testing exists at platform level.
- **RCS:** separate section (12 articles) — richer channel adjacent to SMS.
- **Analytics:** Analyze SMS performance section; platform-level marketing analytics/attribution.

### Postscript (evidence layer A — official Intercom help center, Compliance collection + compliance overview article + Campaigns collection)

- **Compliance overview (deep, US-centric):** TCPA — prior express written consent required for automated marketing texts; consent must contain explicit language for: recurring marketing messages to that number, possible use of an automatic telephone dialing system, consent not a condition of purchase; sender bears burden of proof in litigation → retain consent records; CTIA Messaging Principles & Short Code Monitoring Handbook apply; template compliance language with TERMS/PRIVACY links, "Reply HELP for help; STOP to opt-out", "Msg & data rates may apply".
- **State laws:** dedicated articles for Florida, Connecticut, Maryland, New Jersey, Oklahoma, Washington, Texas, Oregon; FCC 1-to-1 consent rule explainer.
- **Quiet hours (product-enforced):** no explicit federal quiet hours for texts but TCPA/FCC guidance 8am–9pm recipient local time; several states stricter (8am–8pm); NJ 8am–9pm; Oklahoma caps 3 messages per subscriber per rolling 24h; Postscript blocks campaign/automation sends outside configured waking hours per recipient timezone (automations queued to next waking window); opt-in/opt-out confirmation messages exempt (sent even during quiet hours as required).
- **Carrier-enforced content/behavior rules:** abandoned-cart automations limited to one message within 48 hours of trigger — industry-wide carrier policy (documented as affecting every SMS platform); SHAFT content restrictions (sex, hate, alcohol, firearms, tobacco/CBD) — alcohol permitted only with age verification on site and in-thread; CTIA profanity/spam criteria; first-campaign approval process; automatic subscriber removals; list upload requires certification of TCPA-compliant collection, reviewed by the vendor's team.
- **Numbers:** short codes (dedicated; provisioning timeline; compliance audit checklist), toll-free numbers (verification process; call forwarding compliance update), comparison of short codes vs toll-free; UK long-code requirements; 10DLC context.
- **Campaign objects:** Campaigns (62 articles) — campaign flows (single or multi-message sequences), templates, cloning, message scheduling, subscriber event splits, A/B testing with optimized split; segments (high-intent filters, popup opt-in source, phone carrier, flow activity, engaged/unengaged, AND/OR connectors); campaign types library (flash sale, back in stock, product launch, win-back, feedback, content drip, follow-up, mystery, interactive); coupons/offers (Postscript vs Shopify coupons; free-shipping coupons; Shopify discount-code limit management); custom GIFs/text art; RCS campaign flows (cards, carousels, video, suggested actions, webview, iOS vs Android rendering); link previews for iOS.
- **Transactional messaging:** separate guides and setup (transactional distinct from marketing).
- **List growth:** 31 articles (popups with binding ToS language, onsite opt-in vs confirmed opt-in, etc.).
- **Shopify-native** (integrations collection is the largest at 131 articles).

---

## Cross-product Comparison

| Dimension | Tatango/momoGood | SimpleTexting | Attentive | Klaviyo | Postscript | Evidence |
|---|---|---|---|---|---|---|
| Subscriber base of phone numbers as audience unit | ✓ (subscribers + consent log) | ✓ (contacts) | ✓ (subscribers) | ✓ (profiles with SMS consent) | ✓ (subscribers) | B |
| Opt-in recorded with source/timestamp | ✓ (explicit) | ✓ (implicit via import rules/keywords) | ✓ (sign-up units) | ✓ (explicit, per-profile) | ✓ (explicit, certification + review) | B |
| Keyword opt-in (text-to-join) | ✓ | ✓ (first-class) | (sign-up units + keywords implied) | ✓ (subscribe keywords; START/UNSTOP) | ✓ (keywords referenced in consent language) | B |
| Web/checkout form opt-in | ✓ (checkout) | ✓ (web forms/widget) | ✓ (sign-up units, landing pages) | ✓ (forms + 5 ecommerce checkouts) | ✓ (popups with binding ToS) | B |
| Import of consented lists with compliance gate | ✓ (consent verified at import) | ✓ (import guidelines) | (not observed in fetched pages) | ✓ (upload with consent classes) | ✓ (certification + manual review) | B (4/5) |
| Disclosure language requirement | ✓ (built into capture) | ✓ (compliance message) | ✓ (opt-out language articles) | ✓ (detailed rules) | ✓ (detailed template) | B |
| STOP-class opt-out honored and recorded | ✓ (instant, permanent, audit trail) | ✓ | ✓ (opt-out language + settings) | ✓ (STOP + carrier-state resubscribe rules) | ✓ (opt-out compliance + automatic removals) | B |
| SMS-format message with character/segment mechanics | ✓ | ✓ (encoding articles) | ✓ (character-count article) | ✓ | ✓ | B |
| MMS (media) | ✓ (MMS+RCS w/ fallback) | ✓ (MMS campaigns collection) | ✓ (images/video/contact cards) | (SMS focus; RCS section exists) | ✓ (GIFs; RCS cards) | B |
| Tracked links (platform shortener; third-party shorteners blocked by carriers) | ✓ (attribution by segment/campaign/donor) | ✓ (explicit carrier-rule article) | ✓ (global + per-message params) | ✓ (link tracking at platform level) | ✓ (link previews; campaign links) | B |
| Personalization (custom fields/properties/variables) | ✓ | ✓ | ✓ (dynamic links/variables) | ✓ (profile properties) | ✓ (custom properties, tags) | B |
| One-time broadcast campaign | ✓ (mass texting) | ✓ | ✓ | ✓ | ✓ | B |
| Scheduled send | ✓ | ✓ | ✓ (Schedule a Campaign) | ✓ | ✓ (message scheduling in flows) | B |
| Recurring send | (implied by program sends) | ✓ (recurring campaigns) | ✓ (Set up recurring campaigns) | (flows cover) | (campaign types imply) | B (direct 3/5) |
| Multi-message campaign flows | ✓ (journey-type sends) | (not prominent) | ✓ (multiple-message campaigns) | ✓ (flows) | ✓ (campaign flows) | B |
| Triggered automations (welcome, abandoned cart, post-purchase) | ✓ (welcome-type; text-to-give flows) | ✓ (Automations collection) | ✓ (welcome journeys; autoresponders) | ✓ (flows incl. abandoned cart) | ✓ (automation flows; carrier-capped abandoned cart) | B |
| Two-way replies / shared inbox | ✓ (donor conversations + Inbox) | ✓ (The Inbox) | ✓ (Concierge) | ✓ (Conversations topic exists at platform level) | (reply handling implied; inbox not in fetched pages) | B (4/5 direct) |
| Segments (filter-defined audiences) | ✓ (behavioral, real-time) | ✓ (+ click-behavior) | ✓ | ✓ (SMS segments and profiles) | ✓ (rich builder) | B |
| Quiet hours by recipient timezone | ✓ (enforced) | (not observed in fetched pages) | ✓ (Quiet hours setting) | (not directly observed; compliance section is large) | ✓ (enforced, state matrix) | B (3/5 direct) |
| Frequency discipline / smart sending | ✓ (throttling) | ✓ (message limits) | ✓ (Smart Sending) | (not directly observed) | ✓ (OK 3/24h law; carrier cart cap) | B |
| Carrier registration/verification of numbers | ✓ (10DLC, STIR/SHAKEN) | ✓ (short codes; toll-free) | ✓ (shortcodes FAQ) | ✓ (number verification/registration per country) | ✓ (TFN verification; short code audit; 10DLC) | B |
| Content restrictions (SHAFT-class) | ✓ (spam-flagged filtering; compliance engine) | ✓ (restricted content articles) | (not observed in fetched pages) | ✓ (compliance/deliverability section) | ✓ (SHAFT + age verification) | B (4/5) |
| State/country law matrix | ✓ (TCPA/quiet hours) | ✓ (TCPA/CTIA) | ✓ (international opt-out language) | ✓ (per-country availability + rules) | ✓ (8 state-law articles) | B |
| Delivery reports (sent/delivered/failed) | ✓ | ✓ (detailed delivery report) | ✓ (campaign metrics) | ✓ (performance section) | ✓ | B |
| Click tracking + attribution | ✓ (revenue per send) | ✓ (click segments) | ✓ (attribution model) | ✓ (platform analytics) | ✓ | B |
| A/B testing | ✓ (4 variants, auto-promote) | (not observed in fetched pages) | (not observed in fetched pages; experimentation adjacent) | ✓ (platform-level A/B) | ✓ (optimized A/B split) | B (3/5 direct) |
| Per-message spend visible / volume-based billing | ✓ ($0 billed for filtered) | ✓ (limits; billing collection) | ✓ (spending and message counts) | (not directly observed) | (not directly observed) | B (3/5 direct) |
| Email as sibling channel | ✗ (fundraising-focused) | ✗ | ✓ | ✓ (email-first) | (email subscriber collection fields article) | B (2/5 + adjacent) |
| Vertical/audience tuning | Nonprofit/political fundraising | Generic SMB (contests, polls, coupons) | Ecommerce | Ecommerce/retail | Ecommerce (Shopify) | B |
| Multi-country sending | (US-centric pole) | (US-centric pole) | ✓ (international opt-out language) | ✓ (per-country numbers) | ✓ (international waking hours; UK codes) | B |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being an SMS marketing platform:

```text
Marketer-side platform (dashboard, usually + API)
└── SMS subscriber base
    (phone numbers recorded by the platform as opted in to this sender's marketing messages,
     with the opt-out state enforced and recorded — opted-out numbers are excluded from sending)
    └── Text message composition in the SMS format
        (short text message as the unit; media via MMS is an extension, not the core)
    └── Carrier-mediated delivery
        (sending through telecom carriers to the subscribers' phone numbers
         via registered sender numbers — short code, long code, toll-free, or regional equivalent)
    └── Measurement
        (delivery outcomes and engagement recorded per send)
```

Five properties. Remove any one and the Type collapses:

- **Consent-gated phone-number subscriber base** — without recorded consent per number, it's a bulk-SMS blaster or CPaaS gateway, not a lawful marketing platform; without phone numbers it's not SMS.
- **SMS-format message composition** — without it, it's a generic campaign tool or CRM; the short text message (and its encoding/length mechanics) is the channel's message unit.
- **Carrier-mediated delivery through registered sender numbers** — without it, delivery would run over some other substrate (inbox → email marketing; OS push services → push marketing).
- **Opt-out enforcement and record** — carriers and telecom regulation require it; a product without it cannot operate as an SMS marketing platform in any major market, and no era of the category has existed without it (the shortcode-keyword era already had STOP).
- **Measurement** — without it, it's a messaging utility (gateway), not a *marketing* platform. This is what separates the Type from CPaaS/SMS APIs.

Note: opt-out enforcement is in L0 (not just opt-in) because the SMS channel's gate is the regulatory/carrier consent regime, and its enforcement mechanism — the STOP-class keyword and suppression list — is structural to the channel, symmetrical to the OS permission gate in push marketing.

### L1 — Common Mature Structure

Present across the sample; expected in the market but not definitional:

- **Consent capture surfaces:** text-to-join keywords on sender numbers; web sign-up forms, checkout checkboxes, popups/landing pages; tap-to-text/click-to-text links; QR/print; imports of previously collected lists with compliance gating/certification; disclosure language at every opt-in point; double opt-in/verification where required (carrier rule for cart-abandonment in the US).
- **Person layer over numbers:** profiles with custom fields/attributes, tags, ecommerce or donor data in suite/vertical poles.
- **Segments:** filter-defined audiences (properties, behavior, engagement, opt-in source, carrier, geography), dynamic evaluation, estimated size.
- **Campaign types:** one-time broadcast; scheduled; recurring; multi-message campaign flows/sequences; triggered automations (welcome, abandoned cart [carrier-capped], post-purchase, win-back); API-triggered sends.
- **Message design machinery:** personalization variables, platform-managed tracked short links (third-party shorteners blocked by carriers), coupons/offers, MMS media, emoji/encoding handling, mandatory opt-out language inserted into messages.
- **Two-way conversation surfaces:** shared inbox for replies, autoresponders, in some products AI-assisted reply handling.
- **Delivery governance:** quiet hours per recipient timezone (in some products hard-enforced by the platform, in others configurable), frequency discipline (smart sending, message caps, throttling).
- **Compliance tooling:** consent records/audit trails for litigation defense, number/carrier registration and verification (10DLC, TFN verification, short-code audits), content restriction enforcement (SHAFT-class, age verification for alcohol), transactional vs marketing separation.
- **Analytics:** delivery reports with carrier failure detail, click tracking, opt-out/unsubscribe tracking, conversion/revenue attribution (ecommerce and fundraising poles), A/B testing of message variants.
- **Integration fabric:** ecommerce platform integrations, CRMs/donor CRMs, automation tools, REST APIs, webhooks.
- **Commercial mechanics:** spend tied to message volume (per-message/per-credit), with visible spend/counts in-product.

### L2 — Variant / Optional Structure

- **Channel breadth:** SMS-only pure-play vs email+SMS vs omnichannel engagement suite; SMS as flagship vs embedded channel.
- **Audience/vertical pole:** ecommerce (abandoned cart, coupons, checkout opt-in) vs nonprofit/political fundraising (text-to-give, donor CRM sync, disaster-response bursts) vs generic SMB (contests, polls, appointments) vs agency/enterprise.
- **Sender-number type mix:** dedicated short codes, 10DLC long codes, toll-free numbers, alphanumeric sender IDs (regional); per-market availability and per-type capabilities (e.g., resubscribe mechanics differ by number type).
- **Richer channels:** MMS depth; RCS as an emerging richer sibling channel with cards/carousels and SMS fallback.
- **Regional/regulatory regime:** US TCPA/CTIA + state laws vs EU and other regimes; quiet-hours and consent-rule variation by jurisdiction; multi-country sending matrices.
- **Two-way depth:** broadcast-first platforms with light autoresponse vs full conversational inbox with AI drafting.
- **AI assistance:** copy generation, send-time optimization, reply drafting, AI segmentation.
- **Interactive machinery:** text-to-win, text-to-vote, text-to-give payment keyword flows.

### L3 — Vendor-specific (kept out of the final document)

- Tatango/momoGood: five-stage pre-send compliance filter (consent → liveness → mobile → carrier risk → timezone) with $0-billed filtered numbers; STIR/SHAKEN attestation language; text-to-give keyword+amount flow; 4-variant auto-promote A/B; donor-tier click attribution; disaster-response burst positioning.
- SimpleTexting: free compliance message; graphic generator; text-to-win/vote tooling; multiple numbers per account; partner program.
- Attentive: Campaign Composer; Smart Sending; Send Time AI; Copy Assistant; Audiences AI; Concierge; Offers; contact cards.
- Klaviyo: Smart Opt-in forms; per-country sending-number matrix; START/UNSTOP carrier-state resubscribe rules on toll-free; integration of SMS into B2C CRM/Flows/reviews stack; tap-to-text forms.
- Postscript: campaign flows with subscriber event splits; first-campaign approval process; automatic subscriber removals; state-law waking-hours matrix (incl. Oklahoma 3-per-24h cap); Brand Center offers; Shopper; in-thread alcohol age verification; 131-article integrations collection (Shopify-native).

## Rejected Findings (considered, not promoted)

- **"SMS marketing = ecommerce abandoned-cart messaging"** — rejected: the fundraising and generic-SMB poles lack it entirely; ecommerce is the dominant modern segment but a variant (L2).
- **"Short codes are definitional"** — rejected: long codes (10DLC), toll-free, and regional alphanumeric/long-code types are equally first-class; short codes are one sender-number variant. (Klaviyo documents that opt-out/resubscribe mechanics differ by number type — implementation variance, not identity.)
- **"Two-way conversation is the core"** — rejected: broadcast/campaign-first platforms (e.g., the fundraising pole) fit the Type with only autoresponse-level reply handling; the conversational inbox is common-but-not-definitional.
- **"Platform-enforced quiet hours are universal"** — rejected as universal claim: directly observed as platform-enforced in 3 of 5 samples; others document the rules without showing enforcement in fetched pages. Stated as "commonly enforced/managed".
- **"160 characters per segment"** — the number is industry-famous but was not directly observed in the fetched pages; character/segment mechanics are documented (Attentive/SimpleTexting articles) without a reliable universal figure in the sample. Final document describes the mechanics without the number.
- **"RCS is part of the Type"** — rejected for now: RCS appears in 3 of 5 samples as an adjacent richer channel; the Type's name and core remain SMS. Recorded as a boundary watch item.

## Boundary Findings

| Neighboring Type | Boundary test | Distinction |
|---|---|---|
| Email Marketing Platform | Same campaign grammar (audience → message → schedule → measure); different delivery substrate | SMS: carrier-mediated, phone-number-addressed, short-format, per-message telecom costs, stricter consent regime, opt-out via STOP keywords, quiet-hour regulation, messages land in the phone's native messaging thread. Email: inbox delivery, email-address addressing, anti-spam (not telecom) consent, no per-message carrier cost. Sibling channel Types. |
| Push Notification Marketing Platform | Same campaign grammar; different gate and substrate | Push: OS/browser permission gate, device/browser registrations, transient banner surface, no per-message cost. SMS: regulatory/carrier consent gate, phone numbers, persistent native messaging thread, per-message cost. |
| CPaaS / SMS API gateway (developer infrastructure) | The sharpest negative case | A gateway sends SMS via carriers but has no consent-gated subscriber base, no campaign lifecycle, no opt-out enforcement machinery, no marketing measurement. Add those four → becomes this Type. "去掉什么就变成另一个 Type" holds in both directions. |
| Mobile Marketing Platform | Broader umbrella | Mobile marketing includes paid user acquisition, ASO, mobile ads, push, in-app; the SMS platform is one owned channel's machinery. |
| Marketing Automation Platform | Automation overlap | MA is channel-agnostic orchestration of lifecycle programs; SMS platform is defined by the SMS channel's audience (consented numbers), carrier delivery, and compliance mechanics. Journey builders here are convergence, not identity. |
| Customer-to-Business Messaging Application | Two-way overlap | C2B messaging centers on person-initiated conversations with a business (support/concierge); SMS marketing centers on marketer-initiated campaigns to a consented audience. Two-way inboxes here serve campaign replies, not conversation-first support. |
| Church Communication Platform (flagged sibling) | Audience substrate seam | Same messaging grammar; the church tool's audience is the church's own people records with church-life consent capture and congregational jobs; SMS marketing's audience is a commercial consented subscriber base under telecom consent regimes. Supports keeping both Types; joint review pending (STATUS.md). |
| Survey/contest tools (text-to-vote/win) | Feature overlap | Those are opt-in/capture and engagement features inside this Type (observed as product tooling), not separate Types. |

**"去掉什么就变成另一个 Type" 判据：**
- 去掉 carrier/SMS 通道（换成邮箱收件箱投递）→ Email Marketing Platform
- 去掉营销层（consent 订阅者库、campaign、opt-out 强制、度量），只留 carrier 发送 → CPaaS / SMS gateway
- 去掉 telecom 通道机制（换成 OS push 服务 + 设备注册）→ Push Notification Marketing Platform
- 以双向对话为中心而非营销 campaign → Customer-to-Business Messaging / conversational commerce
- 去掉单一通道限定、以跨通道编排为主 → Marketing Automation / Mobile Marketing umbrella（市场定位漂移方向）

## Historical / Market-Sample Check

- **Older products:** the shortcode-keyword era (2000s origin of the category — the sampled veteran dates to 2007) already had: keyword opt-in, confirmation/compliance messages, STOP handling, broadcast + scheduled campaigns, delivery reporting. All L0 properties hold; journeys, MMS depth, AI, segments richness are correctly L1/L2.
- **Regional products:** markets using alphanumeric sender IDs / non-US long codes change the sender-number type and some opt-in/opt-out mechanics, not the structure — L2. (Klaviyo's per-country sending-number documentation and Postscript's UK long-code article evidence this directly.)
- **Platform-native check:** SMS has no OS-vendor marketing console; the closest negative case is the CPaaS gateway, which fails the marketing layer (consent base + campaigns + opt-out machinery + measurement) — confirming the marketing layer as definitional.
- **Regulatory era-shifts:** carrier policy changes (abandoned-cart caps, 1-to-1 consent rule, 10DLC registration, SHAFT tightening) alter the compliance surface but none of them changes the L0 loop — they reinforce that the consent/opt-out layer is structural.

Conclusion: the minimal definition is era-stable and not overfit to the current ecommerce/AI-heavy market.

## Uncertainties

- **Postscript two-way inbox depth:** reply handling and autoresponders are implied (opt-out compliance, transactional messaging) but no inbox collection appeared in fetched pages; final document treats the shared inbox as "common" (4/5 direct) with variation in depth.
- **Quiet-hours enforcement:** platform-enforced directly observed in 3 of 5 (Postscript, Tatango/momoGood, Attentive); Klaviyo/SimpleTexting compliance sections are large but the specific enforcement behavior was not in the fetched pages. Stated as commonly managed, varying in strictness.
- **A/B testing:** directly observed in 3 of 5; stated as common, not universal.
- **Exact numeric rules** (character/segment counts, quiet-hour clock times, state-law caps, TTL-like values, plan limits): observed per product and jurisdiction-dependent; deliberately excluded from the final document except where a rule is load-bearing for understanding (e.g., "some jurisdictions impose stricter waking hours" without the specific hours; the Oklahoma-style per-subscriber caps mentioned only qualitatively in research notes).
- **Market positioning drift:** several vendors now self-describe as broader "customer engagement"/"B2C CRM" platforms (Klaviyo most explicitly; Tatango niching into nonprofit). Structural cores remain distinct; recorded as positioning drift, not Type merger.
- **Tatango help center closure:** product documentation for that sample comes from the official product/marketing site (Tier-2) rather than a help center (Tier-1); observations marked accordingly and precision kept low for that product.

## Final Synthesis

An SMS Marketing Platform is a marketer-side platform whose defining loop is: **build and keep a consent-gated subscriber base of phone numbers → compose short SMS-format messages → deliver through telecom carriers via registered sender numbers → enforce and record opt-outs → measure delivery and engagement.**

Around that loop, mature products add consent capture surfaces (keywords, forms, checkout, imports — with disclosure language and, where required, double opt-in), person profiles and segments, campaign types (broadcast / scheduled / recurring / multi-message flows / triggered automations / API), message design machinery (personalization, tracked links, coupons, MMS), two-way reply surfaces, delivery governance (quiet hours, frequency discipline, throttling), a compliance apparatus that is unusually deep for a marketing Type (consent records, carrier registration, content restrictions, transactional separation, state/country law matrices), delivery/click/revenue analytics, A/B testing, and per-message-volume economics.

The Type is channel-defined: its identity comes from the SMS channel's mechanics — phone-number addressing, carrier mediation with per-message economics, the telecom consent regime with STOP-class opt-out, and the native messaging thread as the receiving surface — not from the campaign grammar it shares with email and push marketing platforms.
