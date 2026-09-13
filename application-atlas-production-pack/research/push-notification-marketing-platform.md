# Research Notes — Push Notification Marketing Platform

Research date: 2026-09-07
Methodology: WORKFLOW v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what a Push Notification Marketing Platform actually is as an Application Type: its defining core structure, its standard capabilities, its variants, and its boundaries against neighboring marketing/messaging Types — based on how real products work, not vendor positioning.

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis):** a marketer-facing platform for composing, targeting, scheduling/sending, and measuring push notifications — short messages rendered by the mobile OS or web browser, delivered to users of the marketer's own app/website who have granted notification permission.
- **Who uses it (hypothesis):** growth/marketing teams of app and web publishers; developers for the integration layer.
- **Nearest neighbors (hypothesis):** Email Marketing Platform, SMS Marketing Platform (same campaign grammar, different channel mechanics), Mobile Marketing Platform (broader umbrella), Marketing Automation Platform (channel-agnostic journeys), Marketing Campaign Management (broader), In-app messaging (different surface), CDP (data layer), CPaaS / push gateways like FCM (infrastructure without marketing layer).
- **Unknowns:** audience model (device tokens vs unified user profiles), campaign type taxonomy, whether web push is first-class, how opt-in is modeled, analytics depth.

## Research Questions

1. What is a push notification as an object inside these systems (anatomy, payload, link behavior)?
2. What is the audience model — device registrations, tokens, channels, users/contacts, tags/attributes/events, segments?
3. How is opt-in / permission modeled, given the OS/browser permission gate?
4. What campaign types exist — broadcast, scheduled, recurring, triggered, API-triggered, journeys?
5. What delivery controls exist — frequency capping, quiet hours, throttling, TTL, timezone delivery, send-time optimization?
6. What experimentation machinery exists — A/B tests, split delivery, control groups?
7. What analytics exist — delivery, open, click, conversion, uninstall?
8. What interfaces does the operator face — composer, audience builder, campaign dashboard, analytics, settings, developer setup?
9. Where is the boundary vs email/SMS marketing, marketing automation, mobile marketing, in-app messaging, CDP, and raw push gateways (FCM console)?
10. Would older / differently-positioned products still fit the definition (historical check)?

## Representative Products

| Product | Position | Why sampled |
|---|---|---|
| OneSignal | Pure-play push/web push, self-serve, SMB→mid-market | The clearest push-first product; excellent public docs |
| Braze | Enterprise customer-engagement suite, push as flagship channel | Enterprise tier; deep channel + governance docs |
| Airship | Enterprise mobile-first push pioneer (formerly Urban Airship) | Historical anchor of the category; distinct identity model |
| CleverTap | Mobile analytics + engagement, mid/enterprise, strong in emerging markets | Analytics-led philosophy; regional platform support |
| Pushwoosh | Pure-play push, mid-market, global | Push-first heritage; broadest channel list incl. regional messengers |

Coverage: different product philosophies (pure-play vs suite), customer tiers (self-serve SMB vs enterprise), channel emphasis (web push vs mobile-first), and geography (global vs emerging-market platform support).

## Sources

All Tier-1 official documentation, fetched 2026-09-07. Zero fetch failures across the sample.

- OneSignal: https://documentation.onesignal.com/docs/ , /docs/push , /docs/segmentation
- Braze: https://www.braze.com/docs/ , /docs/user_guide/home/ , /docs/user_guide/channels/push/push_setup/push_subscription_states/
- Airship: https://www.airship.com/docs/ , /docs/guides/audience/ , /docs/guides/audience/your-audience/ , /docs/guides/features/messaging/push-notifications/
- CleverTap: https://docs.clevertap.com/docs/push-notifications , /docs/create-message-push.md , llms.txt index
- Pushwoosh: https://docs.pushwoosh.com/ , /product/ , /product/messaging-channels/push-notifications/send-push-notifications/

---

## Product Observations

### OneSignal (evidence layer A)

- **Positioning:** "complete platform to manage push notifications across mobile, web, and desktop"; also sells email, SMS/RCS, in-app messages, Live Activities; Journeys for automated multi-channel flows.
- **Audience model:** `User` = individual with one or more `Subscriptions` (the specific channel/device through which a user can receive messages: push, email, SMS). `Tags` = custom metadata for targeting. `Segments` = dynamic groups defined by filters (device type, language, app version, session recency/count/duration, country, location radius, user tags, message events, custom events) with AND/OR logic; segments auto-update; subscribed vs unsubscribed counts shown per channel; only opted-in (subscribed) Subscriptions receive push/email/SMS. External ID links to the customer's own user system; OneSignal ID is platform-generated.
- **Opt-in:** dedicated docs for mobile push prompts, web push prompts, iOS provisional push, Android notification categories — "a well-designed opt-in experience maximizes your push audience."
- **Platform setup:** credentials for iOS (APNs), Android (FCM), Huawei (HMS), Amazon (ADM), web browsers (Chrome/Firefox/Safari/Edge), macOS, Windows, watchOS/Wear OS; SDK integration; migration guides from Firebase/Airship/Braze.
- **Sending:** dashboard composer or REST API; Journeys; A/B testing (multiple variants); templates; AI message composer. Audience = include/exclude segments; defaults to all "Subscribed Users".
- **Scheduling:** send immediately; scheduled (bounded future window); per-user delivery time — "Intelligent Delivery" (optimal time per user based on session activity) or custom local time per timezone; delivery spans 24h so every recipient gets it. Audience membership is evaluated at send time.
- **Delivery controls:** throttling (delivery speed for large audiences), frequency capping (per-user limits, overridable per message).
- **Message anatomy:** title, subtitle (iOS/macOS only), message body, icons, image, action buttons, launch URL / deep link / web URL, badges, sound, additional custom key-value data, collapse ID (mobile, replaces earlier notification), web push topic, priority, TTL (offline persistence window; expired messages discarded), notification grouping. Display notifications vs background/data-only notifications. OS controls rendering/truncation; payload size is a hard platform limit enforced by APNs/FCM.
- **Cancel:** can cancel a message before it is delivered; delivered notifications cannot be removed (only replaced via collapse ID/topic).
- **Analytics:** message reports (delivery, open rate, click-through), "confirmed delivery" (verification that push was delivered and displayed on device), custom outcomes (conversion events), event streams to warehouses/BI, message events feed (delivered/confirmed/clicked/failed per channel).
- **Integrations:** HubSpot, Mixpanel, Amplitude, Zapier, CRMs, data pipelines; webhooks.

### Braze (evidence layer A)

- **Positioning:** customer engagement platform; push is one channel among email, SMS/MMS/RCS, WhatsApp, LINE, KakaoTalk, in-app messages, Content Cards, banners, webhooks, landing pages, feature flags.
- **Data model:** user profiles with standard + custom attributes, custom events (with properties), purchase events, catalogs; Cloud Data Ingestion from warehouses; Currents (event streaming); anonymous users supported.
- **Audience:** segments with segmentation filters (incl. `Foreground Push Enabled`, `Foreground Push Enabled for App`), Segment Extensions (SQL), location targeting + geofences, subscription preferences/groups + preference center, Global Control Group (holdout), suppression lists.
- **Push subscription model (key structural finding):** "Push Subscription State" is a **user-level** global preference (`Subscribed` default / `Opted-In` / `Unsubscribed`), distinct from **push enablement** (OS/browser-level permission per device) and from **push registration** (a valid foreground push token on the profile). A user is *reachable* for push only with valid token + Subscribed/Opted-In state. Push tokens are device+app-specific; one push subscription per device per app; token reassigned when another user logs in on the device. Braze does not auto-set `Unsubscribed` on OS-level opt-out; brands must sync it.
- **Campaigns:** scheduled delivery, action-based (trigger) delivery, attribute triggers, API-triggered delivery, content calendar; conversion events; funnel and retention reports; campaign alerts; approvals/governance; statuses; archiving.
- **Canvas:** journey builder with components (Message, Audience Paths, Action Paths, Decision Split, Delay, Experiment Paths, User Update, Audience Sync, etc.).
- **Messaging fundamentals:** quiet hours (workspace-level), rate limiting and frequency capping, re-eligibility, localization (multi-language, RTL), send test messages, Liquid personalization, Connected Content (external API data at send time), promotion codes.
- **Push specifics:** push token lifecycle; rich notifications; Push Stories; Quick Push; multiple-platform messages; Android notification channels/categories; Push Max; iOS badge count; web push; push error codes; best practices incl. push primer in-app messages (to win the OS prompt) and Chinese Android deliverability.

### Airship (evidence layer A)

- **Positioning:** "customer engagement" platform descended from the push pioneer; channels: push, Message Center, email, in-app (Scenes/In-App Automation), SMS/MMS/RCS, Open Channels (custom platforms), wallet, live activities/real-time app updates.
- **Identity model:** `Contact` (anonymous or Named) with associated `Channels` (a device or address: iOS/Android device, email address, phone number, web browser registered for web push). Channel registration creates the contact. Named users map multiple devices/addresses to one person via external ID.
- **Opt-in model:** "Opt-in status controls whether a channel is eligible to receive messages. A user can match your audience criteria and still be unreachable if they are not opted in." App/web push requires device/browser notification permission; in-app/Scene/Message Center do not require notification permission (delivered by SDK in-app); email/SMS have their own opt-in paths; **subscription lists** record topic-level opt-ins managed via Preference Centers, separate from channel opt-in.
- **User data:** attributes (comparison operators), tags (presence/absence, tag groups), events (triggering, goals, personalization), device properties (locale, timezone, app version, notification opt-in status — channel-level). Data sources: SDK, REST API, dashboard/CSV upload, SFTP, partner integrations, zero-copy warehouse integration.
- **Audience lists:** lifecycle lists (auto-populated: new/active/dormant), uploaded lists (CSV/SFTP), subscription lists. Segments = reusable audience groups with conditions/Boolean logic. Audience Pulse (RFM scoring). Retargeting a previous message's audience. Lookalike audiences via Ad IDs (IDFA/AAID) exported to ad platforms.
- **Audience evaluation:** contact-level vs channel-level evaluation (platform migration in progress) — determines whether cross-channel data rolls up to the person.
- **Push specifics:** banner alerts, not persistent; require text; optional buttons (one or two), title, media, summary; silent push (background wake, no display); web push across desktop/mobile browsers; combining push with in-app/Message Center.
- **Orchestration:** Journeys (multi-step cross-channel), Sequences/Automations with triggers; delivery options; ban lists; message limits.
- **Experimentation:** A/B tests (messages/scenes/sequences), Intelligent Rollouts, Feature Flags, Holdout Experiments, Control Groups.
- **Analytics:** Goals (event-based conversion attribution), message reports, engagement reports, Performance Analytics (explorable), Real-Time Data Streaming, activity log.

### CleverTap (evidence layer A)

- **Positioning:** "drive conversions with Push notifications"; rich segmentation + infrastructure for time-sensitive, personalized push at scale; broader suite: in-app, email, web push, web pop-up, web native display, App Inbox, Native Display, WhatsApp, SMS, RCS, webhooks, Google Ads, TikTok remarketing, Journeys.
- **Campaign creation flow (Who/What/When):**
  - *Start:* integrated platforms check (FCM, Xiaomi, iOS...); qualification criteria = Past behavior / Custom list, Live behavior, or External trigger; optional conversion **goal** (event + conversion time window).
  - *Who:* target segment (saved or ad-hoc; past-behavior or live-behavior); user property filters (custom properties, demographics, geography, geography radius, **reachability flags** `MSG-push`/`MSG-sms`/`MSG-email`/`MSG-whatsapp`, app fields like OS version); **estimated reach** (users + devices, per-platform breakdown, approximate); control group; targeting cap (limit number of recipients, e.g. for limited coupon stock).
  - *What:* message types = Single, A/B Test (test group → winner auto-sent to remainder; equal distribution during test), Split Delivery (fixed percentages, no winner), By User Property (variant per property value, e.g. language); up to several variants; personalization; test profiles.
  - *When:* schedule (specific date/time, multiple dates, recurring); live campaigns triggered by user event, event+inaction combos, or date-type event property values; delivery preferences: global campaign limits (push per user per day, overridable per campaign), DND hours (discard or delay), delivery in user's timezone, campaign cut-off time; **TTL** (relative duration or absolute deadline; governed by FCM/APNs/etc.; offline users get it only if they come online within TTL).
- **Push-specific extras:** RenderMax (improve render rate), collapse key (update/replace notifications), push primer via in-app (win the OS permission), push editor with templates, push stats (sent/clicked/conversions), uninstalls view.
- **Journeys:** entry criteria/segments, nodes/links, goals, states, A/B via IntelliNode.
- **AI:** Scribe (copy), Image Creator, IntelliChannel (channel selection per user), IntelliTime (send-time), IntelliAB (adaptive A/B), Predictions (churn etc.), MCP server.

### Pushwoosh (evidence layer A)

- **Positioning:** messaging solutions: mobile push, web push, in-app, email, SMS, WhatsApp + Customer Journey Builder; "Actionable CDP"; industry packs (gaming, fintech, mobility, media, subscription apps, e-commerce).
- **Setup:** create project → configure platforms (incl. regional: Huawei, plus messengers KakaoTalk/Telegram/Viber/LINE) → register users (SDK, API, CSV import) → set custom User IDs → test devices.
- **Audience:** tags (user data), events (default/custom/conversion; recommended event packs per vertical), segments (by tags, events, existing segments, User ID, geolocation, compound filters, anniversary, import, AI-built), RFM segmentation, control groups, User Explorer, subscription forms (web, double opt-in).
- **Push sending:** one-time push (segment or all users; immediate or scheduled), recurring push (daily/weekly/specific dates), scheduled push, targeted push (via Journey Builder), push to all devices of a User ID; geo campaigns (geozones, clusters, CSV import); advanced: silent push, iOS interactive push, deep links, custom data; subscription prompt widget (pre-permission); message inbox (persistent in-app inbox channel); import push subscribers.
- **Customer Journey:** entry elements (trigger-based, API-based, audience-based); channel elements (push, email, in-app, SMS, WhatsApp, Viber, Kakao, Telegram, LINE, data-to-app, webhook, Multi-Armed Bandit); flow controls (condition split, wait for trigger, A/B/n split, reachability check, time delay, update user profile, audience sync, exit); Liquid dynamic content.
- **Content:** push presets (reusable), AI composer, translation; personalization (dynamic content, Liquid, multi-language); media store; vouchers; product catalog.
- **Analytics:** dashboards (customizable), project statistics, journey statistics (element-level, user path), messaging statistics (push: delivery/open/click), message history, user retention, metrics glossary; event streaming integrations (Segment, mParticle, Amplitude, Mixpanel, BigQuery...).
- **Troubleshooting:** sending errors documented per platform (iOS/macOS/Safari, Android/Chrome/Firefox, Huawei, Windows, Amazon, email) — evidence that platform-credential/token failure handling is a first-class operational concern.

---

## Cross-product Comparison

| Dimension | OneSignal | Braze | Airship | CleverTap | Pushwoosh | Evidence |
|---|---|---|---|---|---|---|
| Compose push (title/body + rich options) | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Audience registry of device/browser registrations | Subscriptions | Push tokens + profiles | Channels + contacts | Devices under user profiles | Registered devices | B |
| OS/browser permission (opt-in) modeled explicitly | ✓ (prompts, provisional) | ✓ (subscription state vs enablement vs token) | ✓ (opt-in vs subscription lists) | ✓ (reachability flags, push primer) | ✓ (subscription prompt widget) | B |
| Unified person across devices | User + External ID | User profile | Named users / contacts | User profile (multi-device) | User ID | B |
| Targeting data: tags/attributes + events | Tags, custom events | Attributes, events, catalogs | Attributes, tags, events | User properties, events | Tags, events | B |
| Dynamic segments (filter-defined, auto-updating) | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| One-time broadcast send | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Scheduled send | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Recurring send | (via scheduling/Journeys) | ✓ | ✓ (Sequences) | ✓ | ✓ | B |
| Event/action-triggered send | ✓ (Journeys) | ✓ (action-based) | ✓ (Automations/Sequences) | ✓ (live behavior) | ✓ (trigger entry) | B |
| API-triggered send | ✓ (REST API) | ✓ | ✓ (REST API) | ✓ (External trigger) | ✓ (API-based entry) | B |
| Multi-step journey builder | ✓ (Journeys) | ✓ (Canvas) | ✓ (Journeys/Sequences) | ✓ (Journeys) | ✓ (Customer Journey) | B |
| A/B testing of message variants | ✓ | ✓ | ✓ | ✓ (incl. split delivery, by-property) | ✓ (A/B/n in journeys) | B |
| Control group / holdout | — (not observed in fetched pages) | ✓ (Global Control Group) | ✓ (Holdout, Control Groups) | ✓ | ✓ | B (4/5) |
| Frequency capping | ✓ | ✓ | ✓ (message limits) | ✓ (global campaign limits) | ✓ (global frequency capping) | B |
| Quiet hours / DND | — (not observed in fetched pages) | ✓ | — (not observed) | ✓ (DND hours) | — (not observed in fetched pages) | B (2/5 observed; likely broader — see Uncertainties) |
| TTL / offline persistence window | ✓ | (push token lifecycle implies) | — (not observed in fetched pages) | ✓ (relative/absolute) | (platform docs imply) | B (2/5 directly observed) |
| Timezone-aware / per-user send time | ✓ (Intelligent Delivery, per-timezone) | ✓ (intelligent + timezone options in scheduling family) | ✓ (Optimal Send Time) | ✓ (user timezone, best time) | ✓ (recurring/scheduled; timezone in delivery options) | B |
| Deep links / launch URLs | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Rich media, buttons, badges, sounds | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Silent / data-only push | ✓ | ✓ (background push) | ✓ | ✓ (implied by collapse-key/pull docs) | ✓ | B |
| Collapse/replace notifications | ✓ (collapse ID, web topic) | — (not observed in fetched pages) | — | ✓ (collapse key) | ✓ (legacy preset options) | B (3/5) |
| Personalization (merge/liquid/handlebars) | ✓ | ✓ (Liquid) | ✓ (Handlebars) | ✓ (Liquid tags, linked content) | ✓ (Liquid) | B |
| Multi-language messages | ✓ | ✓ | ✓ (localization) | ✓ | ✓ | B |
| Templates/presets | ✓ | ✓ | ✓ (templates, snippets) | ✓ (push editor templates, content manager) | ✓ (push presets) | B |
| Delivery/open/click analytics | ✓ | ✓ | ✓ | ✓ | ✓ | B |
| Conversion tracking (goals/outcomes) | ✓ (Custom Outcomes) | ✓ (conversion events) | ✓ (Goals) | ✓ (campaign goals + windows) | ✓ (conversion events) | B |
| Uninstall tracking | — (not observed) | — (not observed in fetched pages) | — (not observed) | ✓ (Uninstalls view) | ✓ (user retention stats) | B (2/5) |
| Test users / test devices / previews | ✓ | ✓ (test messages) | ✓ (testing tools) | ✓ (test profiles) | ✓ (test devices) | B |
| Multi-channel beyond push | email, SMS, in-app, live activities | email, SMS/RCS, WhatsApp, LINE, Kakao, in-app, Content Cards, webhooks | email, SMS, in-app/Scenes, Message Center, open channels, wallet | in-app, email, web push, WhatsApp, SMS, RCS, App Inbox, ads retargeting | in-app, email, SMS, WhatsApp, LINE, Telegram, Kakao, Viber, wallet, inbox | B |
| CDP/analytics integrations + event streaming | ✓ | ✓ (Currents, CDI) | ✓ (zero-copy, streaming) | ✓ (Segment/mParticle/EventBridge) | ✓ | B |
| Web push first-class | ✓ | ✓ | ✓ | ✓ (separate web push module) | ✓ | B |
| Regional Android platforms (Huawei/Xiaomi/etc.) | ✓ (Huawei, Amazon) | ✓ (Chinese Android deliverability guidance) | — (not observed) | ✓ (Xiaomi, Baidu via TTL note) | ✓ (Huawei errors; regional messengers) | B |
| AI assistance (copy/send-time/segment) | ✓ (AI composer) | ✓ (Braze Agents, AI) | ✓ (AI content, Audience Pulse) | ✓ (Scribe, IntelliTime/Channel/AB) | ✓ (AI composer, AI segments) | B |
| Governance (approvals, statuses, audit) | ✓ (audit logs on segments) | ✓ (approvals, statuses, archiving) | ✓ (activity log, manage/change status) | ✓ (campaign approval workflow, audit logs) | ✓ (account access mgmt) | B |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being a push notification marketing platform:

```text
Marketer-side platform (dashboard + API)
└── Push notification as composed message object
    (short OS/browser-rendered alert: title + body, optional link target)
    └── Audience of opted-in app/browser users
        (addressable through device/browser push registrations held by the platform)
        └── Send machinery
            (deliver through OS/browser push services to the targeted audience)
            └── Delivery & engagement measurement
                (sent / delivered / opened / clicked reporting per campaign)
```

Four properties. Remove any one and the Type collapses:

- **Composed push message object** — without it, it's just a gateway passthrough, not a marketing tool.
- **Audience of opted-in device/browser registrations maintained by the platform** — without it, there is no targeting and no marketing (a raw OS push console has no audience registry).
- **Send machinery through OS/browser push services** — without it, it's not the push channel (it would be email/SMS/in-app marketing).
- **Delivery/engagement measurement** — without it, it's a messaging utility, not a *marketing* platform (this is what separates the Type from a developer push gateway like the FCM console, which composes and sends but has no marketing audience/campaign/measurement layer).

Note on opt-in: the OS/browser permission gate is a structural property of the push channel itself, so "opted-in registrations" belongs in L0; the *tooling* to win opt-in (prompts, primers, preference centers) is L1.

### L1 — Common Mature Structure

Present across the sample; expected in the market but not definitional:

- Unified person layer over multiple device registrations (external IDs / named users / user profiles)
- Targeting data: tags, attributes/custom properties, events (custom + conversion), device properties
- Dynamic segments (filter-defined, auto-updating) + saved/ad-hoc audience selection + estimated audience size
- Campaign types: one-time broadcast, scheduled, recurring, event/action-triggered, API-triggered
- Multi-step journey/automation builders (entry → steps → exit; waits, splits, reachability checks)
- A/B testing (variant distribution, winner selection), split delivery, control groups/holdouts
- Message design: rich media, action buttons, badges, sounds, deep links/launch URLs, custom key-value payloads, silent/data notifications, collapse/replace semantics
- Delivery controls: frequency capping, quiet hours/DND, throttling/rate limits, TTL, timezone-aware and optimized send times
- Personalization (merge/liquid/handlebars), multi-language, templates/presets
- Analytics: delivery/open/click funnels, conversion goals, campaign reports, dashboards; uninstall/retention in some
- Subscription/consent management: opt-in/opt-out states, preference centers, subscription lists
- Test users/devices and previews before send
- Multi-channel expansion (email, SMS, in-app, messengers) and CDP/analytics integrations, event streaming, webhooks
- Platform setup layer: OS push-service credentials (APNs/FCM/HMS/ADM/web push), SDK integration, error/troubleshooting surfaces

### L2 — Variant / Optional Structure

- **Channel breadth:** pure-play push(+web) vs omnichannel engagement suite with push as one channel
- **Identity posture:** anonymous device-first vs contact/named-user unification; channel-level vs person-level audience evaluation
- **Web push depth:** first-class module vs secondary
- **Regional platform support:** Huawei HMS, Xiaomi, Baidu, Amazon ADM; regional messengers (LINE, Kakao, Telegram, Viber)
- **Location machinery:** geo-targeted segments vs geofence-triggered campaigns vs geozone/cluster management
- **AI depth:** copy generation, send-time optimization, adaptive A/B, channel selection, predictions
- **OS-surface extensions:** Live Activities / live updates, notification categories, provisional push
- **Experimentation depth:** simple A/B vs holdout groups vs multi-armed bandits vs feature flags
- **Commercial posture:** self-serve freemium vs enterprise contract; plan-gated limits (segment counts, retention windows)

### L3 — Vendor-specific (kept out of the final document)

- OneSignal: Intelligent Delivery, confirmed receipt, Custom Outcomes, Event Streams, segment pause/limits, per-message throttle override
- Braze: Canvas components (Audience/Action/Experiment Paths, Decision Split), Currents, Cloud Data Ingestion, Push Max, Quick Push, Push Stories, random bucket numbers, data-points billing, Global Control Group
- Airship: Named Users terminology, Scenes, Message Center, Open Channels, Wallet, Audience Pulse (RFM), channel-vs-contact evaluation migration, Ad-ID lookalike exports
- CleverTap: RenderMax, IntelliChannel/IntelliTime/IntelliAB, IntelliNode, Predictions, Scribe/Image Creator, App Inbox, Native Display, Web Popups, external-trigger campaigns
- Pushwoosh: Customer Journey element set (Multi-Armed Bandit, Reachability check, Data-to-app), geozones/clusters, Message Inbox, Wallet passes, Cloud Pages, ManyMoney AI

## Rejected Findings (considered, not promoted)

- **"Push platforms are defined by journeys"** — rejected: journeys are L1; pure broadcast+scheduling products still fit the Type; older products predate journeys.
- **"Phone number / email is the identity"** — rejected: push identity is the device/browser registration (token/channel); email/phone are other channels' addresses. Person unification is L1.
- **"AI send-time optimization is core"** — rejected: single-era pattern; L2.
- **"Omnichannel is definitional"** — rejected: pure-play push products (and the historical category) are push-only; multi-channel is L1/L2 expansion.
- **"Payload size limits / exact TTL defaults / variant counts"** — rejected for the final document: product- and platform-specific numbers (observed values differ per product and per OS push service); kept in research notes only.

## Boundary Findings

| Neighboring Type | Boundary test | Distinction |
|---|---|---|
| Email Marketing Platform / SMS Marketing Platform | Same campaign grammar (audience → message → schedule → measure); different delivery substrate | Push: OS/browser push services, device-token addressing, OS permission gate, non-persistent banner surface, real-time. Email/SMS: inbox/carrier delivery, address-based (email/phone), persistent messages. Sibling channel Types under one campaign grammar — the channel mechanics are the seam. |
| Mobile Marketing Platform | Broader umbrella | Mobile marketing includes paid user acquisition, app-store/ASO, mobile ads, SMS, in-app. Push platform is one owned channel's machinery. Remove the other mobile channels and Mobile Marketing collapses into this Type + ads; remove push and this Type disappears. |
| Marketing Automation Platform | Journeys overlap | MA is channel-agnostic orchestration (often email-centric, lead-oriented); push platform is defined by the push channel's audience registry and delivery mechanics. Journey builders appearing here are L1 convergence, not identity. |
| Marketing Campaign Management Platform | Campaign object overlap | Campaign management orchestrates campaigns across channels/teams/budgets; push platform executes one channel with channel-specific objects (tokens, opt-in, TTL, collapse). |
| In-app messaging | Same SDK, different surface | In-app messages render inside the running app, need no OS notification permission, and are not delivered when the app is closed. Frequently bundled in the same product (all five samples bundle it) but structurally a different delivery surface. |
| Customer Data Platform | Data overlap | Push platforms ingest attributes/events *for targeting and messaging*; CDPs are identity-resolution/data-infrastructure systems of record. Push platforms are consumers/activators of customer data, not its canonical home. |
| Push gateway / developer messaging service (e.g. FCM console-class tools) | The sharpest negative case | A raw push gateway composes and sends notifications but has no marketing audience registry (segments/attributes), no campaign lifecycle, no marketing measurement. Add audience + campaign + measurement → becomes this Type. This is the "去掉什么就变成另一个 Type" test in both directions. |
| Ad platforms (DSP/ad networks) | Audience overlap (Ad-ID exports) | Paid media buying vs owned-channel messaging; some push platforms export device ad IDs *to* ad platforms — evidence of the boundary, not blur. |

**"去掉什么就变成另一个 Type" 判据：**
- 去掉 push 通道机制（换成 email 地址/收件箱投递）→ Email Marketing Platform
- 去掉营销层（受众注册表、campaign、度量），只留发送 → developer push gateway
- 去掉单一通道限定、以跨通道编排为主 → Marketing Automation / Customer Engagement Platform（市场定位漂移方向）
- 去掉 OS 权限门与锁屏/通知中心表面（改为应用内渲染）→ In-app messaging

## Historical / Market-Sample Check

- **Older products:** the category's founding products (late-2000s mobile push platforms) already had: app audience registry, segmentation, campaign composition, OS push delivery, delivery/open reporting. They lacked journeys, AI, multi-channel breadth, web push. All of those are correctly L1/L2 — the L0 loop holds for the category's origin.
- **Platform-native tools:** OS/OS-vendor push consoles (FCM-class) fail the L0 marketing layer — confirming that the marketing layer (audience + campaign + measurement) is definitional, not the raw delivery pipe.
- **Regional products:** regional Android push platforms (Huawei/Xiaomi-class ecosystems) and regional messengers change the *platform list*, not the structure — L2.
- **Web push era (mid-2010s+):** web browsers joined as registration surfaces; structure unchanged — the audience registry simply gained a browser registration type. L2 surface expansion.

Conclusion: the minimal definition is era-stable and not overfit to the current omnichannel/AI-heavy market.

## Uncertainties

- **Quiet hours / DND:** directly observed in 2 of 5 fetched samples (Braze, CleverTap); likely near-universal in the market but not verified across the full sample — final document says "commonly" not "always".
- **TTL controls:** directly observed in 2 of 5 (OneSignal, CleverTap); Pushwoosh/Braze imply it via platform docs. Stated as common capability without exact defaults.
- **Uninstall tracking:** observed in 2 of 5 (CleverTap, Pushwoosh); treated as optional analytics extension.
- **Control groups:** observed in 4 of 5; OneSignal's fetched pages did not show it — treated as common-but-not-universal.
- **Exact numeric limits** (payload sizes, scheduling horizons, variant counts, segment limits, retention windows): observed per product but plan- and platform-dependent; deliberately excluded from the final document.
- **Market positioning drift:** all five vendors now self-describe as "customer engagement" / "omnichannel messaging" platforms; pure-play push-only positioning survives mainly in entry tiers. This is positioning drift, not structural evidence that the Type has merged with Marketing Automation. Recorded as a boundary issue for STATUS.md.
- **Pricing/packaging:** not researched (out of scope for the Type definition).

## Final Synthesis

A Push Notification Marketing Platform is a marketer-side platform whose defining loop is: **compose a push notification → target an audience of opted-in app/browser users held as device/browser registrations in the platform's audience registry → deliver through OS/browser push services (immediately, on schedule, on recurrence, on trigger, or via API) → measure delivery and engagement.**

Around that loop, mature products add a person layer over devices, tag/attribute/event targeting data, dynamic segments, journey automation, A/B testing and control groups, rich message design (media, buttons, deep links, silent/data pushes, collapse semantics), delivery governance (frequency capping, quiet hours, throttling, TTL, optimized send times), personalization and localization, conversion analytics, consent/preference management, multi-channel expansion, and integration fabric.

The Type is channel-defined: its identity comes from the push channel's mechanics (OS/browser permission gate, device-token addressing, non-persistent real-time surface), not from the campaign grammar it shares with email/SMS marketing platforms. Market positioning has drifted toward "customer engagement platform," but the structural core remains the push channel loop.
