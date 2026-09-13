# Research Notes — Customer-to-Business Messaging Application

## Research Goal

Understand what a "Customer-to-Business Messaging Application" is as an Application Type: messaging software in which an **individual customer initiates and conducts a two-way conversation with an identified business**. This pass must (a) characterize the C2B view on its own evidence, and (b) resolve — or honestly bound — the relationship to the already-processed sibling leaf `business-messaging-application`, whose boundary notes flagged the two as "probable two-sided pair or near-alias, flagged for joint review."

## Initial Boundary

- Directory position: 01.01 Messaging & Chat, sibling of Instant Messaging, Group Messaging, Chat Room, Team Messaging, Community Chat, and Business Messaging Application.
- Committed framing from the processed siblings (instant-messaging-application.md, business-messaging-application.md): Business Messaging = "identity is organizational; conversation is customer ↔ business; flows are CRM/support-shaped"; C2B Messaging = "customer-initiated contact with a business, often through a public profile or short code". This research must validate or refine that split, not silently rewrite it.
- Prior boundary note (business-messaging-application.md §Boundary Findings): same underlying object model (org participant + thread + external individual); C2B emphasizes **customer-initiated entry** through public entry points; Business Messaging covers the **organization-operated messaging application as a whole** including business-initiated exchange. Hypothesis to test this pass: is "customer-initiated entry" a structural, enforceable property of a distinct product category — or only an emphasis inside one shared model?
- Risks: confusing this leaf with internal team messaging (excluded by audience), with SMS marketing broadcast (excluded by conversation-first), or with help-desk ticketing (excluded by thread-vs-ticket centrality).

## Research Questions

1. How exactly does a customer start a conversation with a business? What are the entry points, and who must act first?
2. What is the business-side identity that makes it publicly addressable (business ID, official account, short code, business phone number, verified profile), and does it require registration/verification?
3. What identity does the customer carry, and can it be anonymous?
4. What rules constrain the business's outbound behavior (reply windows, template gating, proactive-message limits, opt-out), and do those rules structurally protect customer initiative?
5. How does the business side handle the conversation (agent console, automation, escalation), and how does that relate to the sibling leaf's shared-inbox model?
6. Where does this Type end: vs Business Messaging, SMS Marketing, Customer Support Chat/Help Desk, Chatbot Platform, Instant Messaging?

## Representative Products

Chosen for market coverage, documentation depth, different product philosophies, different geographies and customer tiers:

| Product | Philosophy | Customer tier | Direct docs fetched? |
|---|---|---|---|
| Apple Messages for Business | platform-native channel on a device OS's default messaging app; strict registration + review regime | enterprise (via MSPs) | **Yes** (register.apple.com docs ×2) |
| Twilio Programmable Messaging (SMS/MMS/RCS/WhatsApp/Messenger) | network-neutral conversation infrastructure as APIs; business registers numbers/brands | developer / enterprise | **Yes** (twilio.com/docs) |
| LINE Messaging API / Official Account | regional consumer-messaging network with official-account model; friend-gated entry | SMB → enterprise | **Yes** (developers.line.biz) |
| WhatsApp Business | consumer messaging network's business participation mode | SMB app / enterprise platform | **No** (Meta dev docs transport error ×1 this pass; whatsapp.com hosts ×3 in prior pass) — documented indirectly via Intercom's official channel docs (fetched 2026-09-06) |
| Intercom / Shopify Inbox (context) | org-side inbox handling for conversations that customers start on widgets/profiles | mid-market / SMB | Fetched 2026-09-06 in the sibling pass; reused here as cross-product context only |

## Sources

Fetched 2026-09-07 (this pass):

- Apple — Messages for Business documentation, introduction — https://register.apple.com/resources/messages/messaging-documentation/ (Tier 1)
- Apple — Messages for Business FAQ — https://register.apple.com/resources/messages/messaging-documentation/faq (Tier 1)
- Apple — Messages for Business product page — https://developer.apple.com/business-chat/ (Tier 2)
- Twilio Docs — Programmable Messaging — https://www.twilio.com/docs/messaging (Tier 1)
- LINE Developers — Messaging API overview — https://developers.line.biz/en/docs/messaging-api/overview/ (Tier 1; re-fetched this pass after sibling-pass fetch on 2026-09-06)

Carried from the sibling pass (fetched 2026-09-06, first-hand in that session):

- Intercom Help — Using WhatsApp as a channel — https://www.intercom.com/help/en/articles/9881312-using-whatsapp-as-a-channel (Tier 1; official third-party platform documentation of WhatsApp business-channel behavior)
- Intercom Help — Messenger/Inbox articles (Tier 1) — org-side inbox evidence
- Shopify App Store — Shopify Inbox listing — https://www.shopify.com/inbox (Tier 2)
- Twilio Docs — Conversations — https://www.twilio.com/docs/conversations (Tier 1)

Source-access limitations:

- Meta developer documentation (developers.facebook.com/docs/whatsapp) failed with a transport error on the single attempt this pass; three whatsapp.com hosts failed in the prior pass. Per network rules, Meta surfaces are abandoned. WhatsApp facts below are limited to behavior documented in official third-party platform documentation (Intercom) plus positioning-level knowledge; no precise claims beyond those.
- Regional official-account products beyond LINE (WeChat 公众号, KakaoTalk) not directly sampled; the official-account pattern rests on the LINE sample.
- Google Business Messages existed as a major C2B entry-point product but is discontinued; not sampled and not used as evidence.

## Product A — Apple Messages for Business

Evidence layer: A (directly observed, official Tier-1 documentation, v3.1 dated 2026-07-21).

### Customer-side entry (the C2B heart)

- "Customers can initiate a conversation by tapping a Messages button placed on: your website or mobile site, your iOS/iPadOS app, email marketing, QR codes and NFC tags, Apple Maps listing, a registered business phone number (via Message Suggest), Wallet passes."
- "Customers can only reach businesses that have registered with Apple and received approval" — the business must be a registered, approved participant; customers cannot message arbitrary businesses.
- Use cases documented as customer-initiated journeys: tap a link in a shipping email → track order; scan a QR code → book an appointment (Time Picker + calendar confirmation); tap "Message Us" on the website → authenticate, resolve account issues; tap a phone number → Message Suggest offers messaging instead of calling.

### Identity model

- The business is identified by a **Business ID** assigned by Apple at registration — explicitly "not a phone number."
- The customer–business relationship is identified by an **Opaque ID**: unique, anonymous, stable for the same customer messaging the same business, different per business, and "not the customer's phone number, email, or Apple Account." The business never sees the customer's phone number unless the customer shares it. Customers decide what personal information to share in the conversation.
- Conversations are always **one-to-one**: "Group chat with a business is not supported."

### Outbound rules (structural protection of customer initiative)

- Proactive messages: businesses may send proactive messages **only to customers who previously started a conversation, and only in the customer's direct interest** (order status, delivery notifications, appointment reminders, flight/booking changes, opted-in account alerts). "Proactive messages should not be used for promotional or marketing content unless the customer has explicitly requested it."
- **Conversation end is customer-controlled**: "When a customer ends a conversation, stop messaging them. The customer must initiate a new conversation to receive further messages." Only an immediate post-session CSAT is acceptable; opt-out keywords (STOP/UNSUBSCRIBE) must be respected "with no exceptions."
- Async posture: "Apple Messages for Business is async — let them respond in their own time."

### Business-side handling

- Deployment requires an Apple-approved **Messaging Service Provider (MSP)**: provides the asynchronous messaging platform, message delivery/routing/processing, interactive features, automation/bots, a **live agent console**, and back-end integrations (CRM, order management, authentication).
- Apple **requires a blend of automated and human agents**: "deployments without live agent support will not be approved"; customers must always be able to reach a live agent via "help"/"agent" keywords; automation should send the first reply within seconds and identify itself; agent transitions must be announced with wait times.
- Message flow: customer → Apple service → MSP platform → agent queue or automation → MSP → Apple → customer device.
- Interactive features: Quick Reply, List Picker, Time Picker, Apple Pay, iMessage apps, OAuth2 authentication inside the conversation.
- Registration lifecycle: Apple Business Register account → test mode → Experience Review (screen recording) → commercial account; one commercial account per business.

Type-relevant reading: this is the purest documentation of the C2B pole — customer-initiated entry through published surfaces, business as a registered public participant, and outbound initiative structurally limited so that entry and re-entry belong to the customer. Even here, though, in-interest proactive messages within an existing conversation exist — the customer's initiative governs entry/re-entry, not every message.

## Product B — Twilio Programmable Messaging

Evidence layer: A (directly observed, official docs).

- "Send messages to customers across preferred channels like SMS, MMS, RCS, and WhatsApp with one API"; buy/port phone numbers; send **and receive** programmatically (two-way SMS/MMS).
- Business identity registration regimes: A2P 10DLC compliance and toll-free (TFN) verification for US SMS; reusable message templates; messaging fraud prevention guidance.
- RCS positioning: "Send text and media messages from your brand — not from a phone number"; supports rich cards/carousels and read receipts.
- Facebook Messenger channel: "Click-to-message marketing and promotions", "Customer support and chatbots", "persistent conversations".
- Use cases: appointment scheduling and reminders, order updates and delivery notifications, authentication (OTP), marketing and promotions, feedback and surveys.
- Related products complete the picture: Conversations (web chat + WhatsApp + SMS threads), Flex (digital engagement center for sales/support teams), Studio (no-code builder).
- API philosophy: the Type's objects — message, sender identity, channel, thread, template — are delivered as primitives; the org composes its own agent surfaces (Flex or its own).

Type-relevant reading: the business addresses customers **as the brand** across channels; the customer-side counterpart is an ordinary phone/SMS/RCS/Messenger user. Inbound capability is first-class ("send and receive"), making customer-initiated threads (e.g., a customer texting a published number or clicking a Messenger ad) a supported pattern; business-initiated notifications are equally supported — on this infrastructure the initiative direction is the org's design choice, governed by registration/consent regimes (A2P, templates, fraud rules).

## Product C — LINE Messaging API / Official Account

Evidence layer: A (directly observed, official docs; consistent with the sibling pass).

- The org-side participant is a **LINE Official Account**; users must add the account as a friend (QR code shown in the docs' own demo); the friend relationship gates the conversation.
- Flow: user sends a message to the Official Account → LINE Platform sends a webhook event to the bot server → bot server responds.
- Outbound: reply messages within the exchange + "send messages directly to users at all times" (push, multicast, broadcast) — free-form push to friends, plan-metered.
- Message types: text, sticker, image, video, audio, location, coupon, imagemap, template, Flex (rich cards).
- Rich menus in the chat, LINE Beacon region triggers, account linking to the org's own user system, user profiles.
- Quotas: free monthly message count depends on the Official Account subscription plan.

Type-relevant reading: the regional official-account shape — customer initiates by adding the account and messaging first; once the friend relationship exists, the business may push at any time. The entry is customer-initiated; subsequent initiative policy is the most permissive in the sample.

## Product D — WhatsApp Business (indirect)

Evidence layer: A- for channel behavior only (documented by Intercom's official channel docs, fetched 2026-09-06); positioning-level otherwise. Direct vendor docs unreachable across both passes (4 distinct host failures).

Documented channel behavior (via official third-party platform documentation):

- Connection requires a **WhatsApp business number**; inbound + outbound supported.
- **24-hour customer care window**: if the customer's last message is more than 24 hours old, the business cannot reply with free text — only pre-approved **message templates**; a customer reply re-opens the window. Starting a new conversation business-side requires a template.
- Single continuous thread per customer–business pair; the org's tooling defines when a closed thread counts as a new conversation.
- Inbound media: text, images, attachments, video, audio/voice notes, locations.

Type-relevant reading: a consumer messaging network exposing an organizational participation mode where **outbound initiative is time-boxed by network policy** — between LINE's free push and Apple's customer-controlled re-entry. The customer's last message is what keeps free-form replies available; the network structurally privileges the customer-initiated state.

## Cross-product Comparison

| Aspect | Apple Messages for Business | Twilio Messaging | LINE Official Account | WhatsApp Business (via 3P docs) |
|---|---|---|---|---|
| Business identity | Business ID registered/approved by Apple (explicitly not a phone number) | purchased/portable numbers, brand sender (RCS), A2P-verified campaigns | Official Account on the network | WhatsApp business number |
| Customer identity | Opaque ID (anonymous, stable per customer–business pair) | phone number / channel address | LINE account (friend) | phone-based user |
| Entry point (who acts first) | customer taps a published button (site, app, email, QR/NFC, Maps, Message Suggest, Wallet) | customer texts/clicks; org may also initiate (consent-regulated) | customer adds friend + messages first | customer messages the business number (or business opens with a template) |
| Thread | 1:1 only, no group chat | two-way per channel address | 1:1 chat (+ group support for bots) | single continuous thread |
| Persistent history | conversation record at MSP; Opaque ID gives continuity | message resource records; org-composed storage | platform + bot-side records | network thread + org tooling |
| Outbound policy | in-interest proactive only; re-entry = customer must start new conversation; STOP honored absolutely | channel/regulatory regimes (A2P 10DLC, templates, fraud rules) | free push at any time to friends | free text only within the response window; templates otherwise |
| Automation + human | automation **must** coexist with live agents; "help"/"agent" keywords mandatory | org-composed (bots, Flex agents) | bot server (human agents optional behind the bot) | org tooling (agents via platforms) |
| Rich/interactive | Quick Reply, List Picker, Time Picker, Apple Pay, iMessage apps | cards/carousels (RCS), templates | Flex/template/coupon messages | media types |
| Delivery form | device-native channel via approved MSP | APIs/SDKs (compose your own) | network-native official account + API | network-native business mode + platform APIs |
| Metering | free channel; MSP pricing | usage-based | plan quotas | per-conversation/network pricing |

### Abstraction result

Layer 0 — Defining Invariant:

1. **Customer-initiated entry through a public business-published point.** The individual starts the conversation at their own initiative — tapping a chat button, scanning a code, adding an official account, texting a published number. The business publishes the entry; the customer decides to act. Without customer-side initiation the leaf collapses into business-initiated outbound messaging (notification/marketing), not C2B messaging.
2. **Identified business as the addressed participant.** The counterpart is a registered/verified organizational identity (business ID, official account, business number/short code, business profile) that is publicly reachable through the entry point — not a private individual and not an arbitrary contact.
3. **Two-way conversation thread between the individual and the business** in chat form — genuinely conversational, in both directions, 1:1.
4. **Business-held persistent conversation record.** The thread and its history are retained on the business side (console/platform/network), so the conversation survives sessions and can be consulted or continued by the organization.

Layer 1 — Common mature structure (common across the sample, not definitional):

- Business-side agent handling: console/inbox where conversations queue, get answered by human agents or automation, and are tracked to resolution (shared with the Business Messaging sibling's model — Intercom/Shopify evidence).
- Automation with human escalation: bots/AI answer first or assist; every mature regime in the sample either requires or commonly provides a path to a live human (Apple makes it an approval condition).
- Availability and expectation messaging: greetings, away messages, expected reply times; async "answer on your own time" posture.
- Relationship continuity: the same customer re-connecting is re-recognized (opaque relationship ID, phone number, friend relationship, account link) rather than treated as a stranger.
- In-interest proactive updates inside an existing conversation/relationship: order status, delivery, reminders, booking changes — permitted across the sample in bounded forms.
- Templates / quick replies / canned responses.
- Rich message forms: cards, pickers, carousels, lists, payments inside the conversation.
- Opt-out and consent machinery: STOP/UNSUBSCRIBE keywords, registration regimes for business messaging (A2P-style), template approval regimes.
- Commerce in-conversation: payments (Apple Pay), catalog-grounded answers, order operations.
- Analytics: CSAT, response performance, deflected-call volume.

Layer 2 — Variant / optional structure (depends on channel, geography, segment):

- Outbound-initiative policy — the single widest variance: free push at any time once related (LINE); time-boxed free-text window with template gating afterward (WhatsApp); in-interest-only proactive plus customer-controlled re-entry (Apple); consent/registration-regulated (SMS A2P).
- Identity substrate for the customer: phone number, network account/friendship, anonymous relationship-specific ID, identified app user, name+email.
- Identity substrate for the business: device-platform business ID without a phone number, business phone number/short code, official account, verified brand sender.
- Entry surface: device-native messaging app, SMS inbox, web/app chat widget, messaging-network chat, Maps/listing surfaces, Wallet passes, QR/NFC, email links.
- Delivery form: platform-native channel (via approved intermediaries), consumer-network business mode, regional official account, network-neutral API infrastructure, storefront/app-embedded chat.
- Verification/approval regimes for the business (Apple Experience Review, A2P campaign vetting, network business verification) — present in modern regulated channels, absent in older web-chat forms.
- Metering models: free channel + intermediary pricing, usage-based, plan quotas, per-conversation pricing.

Layer 3 — Vendor-specific (kept out of the final document):

- Apple: Opaque ID, Business ID, MSP requirement, Experience Review screen-recording, Message Suggest, 5-second automation best practice, one-commercial-account rule, ISO 27001/27018 coverage, OAuth2 + password autofill.
- LINE: friend-add gate, rich menus, LINE Beacon, coupon/imagemap types, plan quotas.
- WhatsApp: 24-hour customer care window mechanics, pre-approved template management, per-conversation pricing.
- Twilio: A2P 10DLC/TFN verification specifics, Messaging Services, Flex/Studio/Conversations product names.
- Intercom/Shopify (context): Fin, Spaces, lead-vs-user model; Shop sign-in, catalog-grounded agent, orders-assisted analytics.

## Historical / Market-Sample Check

Would older, regional, platform-native or differently positioned products still fit the Layer 0?

- **2000s website click-to-chat** ("Chat with us" button → operator console): customer clicks a published button; business identity (the company console); two-way thread; transcript retained → fits, without registration regimes, AI, payments, or templates.
- **Two-way SMS on a published short code/long code** (customer texts a keyword or number): fits — customer-initiated entry, business identity, thread, carrier/operator-side retention plus org-side records.
- **Regional official accounts** (LINE documented; WeChat 公众号-style and KakaoTalk channels by the same pattern): user adds the account and messages first → fits.
- **Platform-native business channels** (Apple): fits with the strongest structural enforcement of customer initiative.
- **Email-based customer contact**: envelope/mailbox model, not a chat thread → excluded by the chat-form element (consistent with the sibling's boundary).

The Layer 0 deliberately avoids: any specific identity substrate (phone, account, anonymous ID all appear), any specific entry surface (buttons, codes, listings, numbers), AI/bots, payments, business hours, and any particular outbound policy (which ranges from free push to customer-controlled re-entry). The customer-initiated *entry* is retained as the invariant because it is the property that distinguishes this leaf's scope from business-initiated messaging — and it holds in every sampled era and shape, from 2000s click-to-chat to platform-native channels.

## Vendor-specific Findings

See Layer 3. Notable for boundary work: Apple's documentation is the only sampled source that states the initiative rule as an absolute ("The customer must initiate a new conversation to receive further messages"); LINE's is the most permissive for the business ("send messages directly to users at all times"). Outbound-initiative policy is therefore a **spectrum across channels**, not a definitional property at either extreme.

## Boundary Findings

- **vs Business Messaging Application (sibling leaf)**: market evidence confirms the prior flag — the two leaves describe **one shared conversation model** (identified organizational participant + two-way thread with an external individual + org-held history) viewed from two sides. The researched distinction: C2B is the **customer-initiated view** — entry (and on the strongest evidence, re-entry) through public business-published points, with outbound initiative constrained to varying degrees; Business Messaging is the **organization-operated application as a whole**, including business-initiated exchange as a first-class loop (campaigns, notifications, outbound sequences). Every product sampled here could equally serve as a Business Messaging sample; the difference is which side of the initiative axis the documentation foregrounds. Recorded as a boundary issue for joint review: probable two-sided pair / variant, not two disjoint Types.
- **vs SMS Marketing Platform**: campaign/list-broadcast-first vs conversation-first. Business-initiated bulk outbound exists inside C2B products as an optional layer (and is policy-constrained); when the list campaign is the core, the product is SMS Marketing.
- **vs Customer Support Chat / Help Desk / Ticketing / Customer Service Platform**: intent vs medium. C2B conversations are intent-agnostic (sales, support, booking, operations — Apple's own use-case table spans all). When threads are fundamentally tickets with SLAs and service workflow, the product is a help desk.
- **vs Customer Service Chatbot Platform**: bot-construction-first vs conversation-first; note Apple requires a human escalation path, evidence that even the most automated deployments in this Type are human-inclusive.
- **vs Instant Messaging Application**: the addressed participant is an identified organization reachable through public business points, vs a personal contact graph between private individuals.
- **vs Team Messaging Application**: external customers vs internal employees.
- **vs Community Chat Platform**: 1:1 customer↔business threads (Apple: "Group chat with a business is not supported") vs many-to-many discoverable community spaces.
- **vs Digital Concierge / hotel guest messaging (adjacent Types elsewhere in the directory)**: domain-scoped variants of the same conversation model; not distinct by medium.

## Uncertainties

- WhatsApp Business direct vendor documentation unreachable across two passes (4 distinct host failures). Channel behavior rests on official third-party platform documentation; WhatsApp SMB-app details (labels, catalogs, quick replies, business profile) unverified — no precise claims made.
- The directory's intended distinction between Business Messaging Application and Customer-to-Business Messaging Application is **not settled by market evidence**: products and vendors do not partition the market along this line. The customer-initiated-entry emphasis is real and documented (strongest on Apple), but whether it justifies two Types is a taxonomy judgment recorded for joint review, not resolved here.
- Regional official-account products beyond LINE not directly sampled this pass.
- Discontinued products (e.g., Google Business Messages) suggest the entry-point landscape shifts with platform policies over time; the entry-point list in the final document is described as examples, not a stable canon.

## Final Synthesis

A Customer-to-Business Messaging Application is messaging software through which an **individual customer starts and conducts a two-way conversation with an identified business**: the business registers a public, addressable identity and publishes entry points (chat buttons, business profiles, QR/short codes, official accounts); the customer initiates from their own messaging surface at their own initiative; the exchange is a persistent 1:1 chat thread held as a record on the business side and handled there by agents and automation with a path to a live human. Conversational initiative rests with the customer at entry — and, on channels with the strictest policy, at re-entry — while the business's outbound freedom varies widely by channel policy, from free push to in-interest-only proactive messages. The org-side handling machinery is shared with the Business Messaging sibling; what distinguishes this leaf is the customer-initiated view through public entry points. Whether that emphasis constitutes a separate Type or a documented view of one shared model is flagged for joint review.
