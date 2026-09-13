# Research Notes — Mobile Marketing Platform

Research date: 2026-09-08
Methodology: WORKFLOW v1.1 (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

---

## Research Goal

Understand what a "Mobile Marketing Platform" actually is as an Application Type: whether the leaf names one product structure or an umbrella over several, what its defining core is, and how it sits against the already-processed sibling Types in §06 (Push Notification Marketing Platform, SMS Marketing Platform, Marketing Automation Platform, Marketing Attribution Platform) — based on how real products work, not vendor positioning.

## Initial Boundary (hypothesis before research)

- **What it is (hypothesis):** an umbrella term. Two prior sibling passes (SMS, push) each recorded in their boundary tables that "Mobile Marketing Platform" is a *broader umbrella* — "paid user acquisition, app-store optimization, mobile ads, push, in-app" — without defining it. The structural candidates underneath:
  1. **Mobile measurement / attribution family (MMP)** — AppsFlyer, Adjust, Singular, Kochava, Branch — the app-install measurement stack;
  2. **App engagement / messaging family** — CleverTap, MoEngage, Airship, Braze, OneSignal — owned-channel engagement for app users;
  3. **Paid UA / mobile ad buying** — ad networks, DSPs (covered by DSP / media-buying leaves);
  4. **Store visibility / ASO family** — AppTweak, Sensor Tower (no dedicated directory leaf).
- **Critical constraint discovered before research:** the Marketing Attribution Platform pass (processed 2026-09-08, same day) already includes **mobile-app attribution (MMP) as one of its Variants** and uses AppsFlyer as a representative product. The Push and SMS passes claim their own channel loops and call this leaf the umbrella. Therefore defining this leaf as *MMP core* or as *engagement core* would collide with already-published sibling documents.
- **Unknowns:** whether any single product structure spans the umbrella; how the families interlock (who measures, who messages, who links); whether the term's referent spread is real in current self-descriptions; how store/OS privacy regimes reshape the substrate.

## Research Questions

1. How do products that carry (or carried) the "mobile marketing" label describe themselves today — one family or several?
2. What is the shared substrate: app stores, OS channels, ad networks, device/privacy frameworks — which of these are constitutive?
3. What is the unit of marketing in these products (the app? the install base? the campaign?) and what is the population of record?
4. How do the families interlock — e.g., do engagement platforms implement attribution or integrate attribution providers?
5. What does the paid-media side look like from the app marketer's side (ad-network configuration fabric, SKAN/Privacy Sandbox regimes)?
6. What does the owned/organic side look like (deep links, web-to-app, store listing/keywords)?
7. Where are the boundaries vs Marketing Attribution Platform, Marketing Automation Platform, Push/SMS Marketing, DSP/ad networks, product analytics?
8. Would older / differently-positioned products still fit a definition (historical check)? Where does pre-app-era mobile marketing (SMS/QR/mobile-web) belong?

## Representative Products

| Product | Family pole | Why sampled |
|---|---|---|
| AppsFlyer | Measurement/attribution (MMP) at app-ecosystem scale | Market-leading measurement platform; docs show the full substrate: SDK integration, ad-network fabric, SKAN/Privacy Sandbox, owned-media links, retargeting |
| Branch | Linking + attribution (owned/organic + paid) | Different philosophy: the link as the spine; explicit Engagement (owned/organic) vs Performance (paid) product split; ties itself to "mobile marketing" in its own training framing |
| CleverTap | App engagement / retention suite | The engagement-family pole; official docs show it *integrates* attribution providers (Branch, AppsFlyer) rather than implementing attribution — key interlock evidence |
| AppTweak | Store visibility / ASO + Apple Search Ads management | The store-ecosystem pole; self-describes as "App Store Marketing & Intelligence Platform"; shows organic (ASO) and paid (store ads) store-channel machinery |

Coverage: four different product philosophies (measure-first, link-first, engage-first, store-visibility-first); different customer tiers (self-serve trial SMB to enterprise/gaming); different geography emphases (AppsFlyer's China-market sections). Adjust, TUNE, and MoEngage were also intended as samples but could not be reached (see Sources).

## Sources

All fetches on 2026-09-08, official surfaces.

- AppsFlyer Knowledge Base — https://support.appsflyer.com/hc/en-us (root; Marketers tabs)
- AppsFlyer — "Measure & Engage" section — https://support.appsflyer.com/hc/en-us/sections/6551006275729-Measure-Engage
- AppsFlyer — "Measure paid media" section — https://support.appsflyer.com/hc/en-us/sections/6550990672401-Measure-paid-media
- AppsFlyer — "Redirect & attribute users" section — https://support.appsflyer.com/hc/en-us/sections/6551169161745-Redirect-attribute-users
- AppsFlyer — "Get started" section — https://support.appsflyer.com/hc/en-us/sections/6550753145745-Get-started
- Branch Help Center — https://help.branch.io/ (root incl. products FAQ, hubs)
- CleverTap Docs — Overview — https://docs.clevertap.com/
- AppTweak — product site — https://www.apptweak.com/en

**Source-access limitations:** Adjust (help.adjust.com timed out twice; www.adjust.com returned 403), TUNE (www.tune.com 403), and MoEngage (timed out twice) could not be reached and were abandoned per the retry rule. The sample is therefore four products, one per family pole, rather than a deeper per-family sample. Claims that would have leaned on those products (e.g., Adjust's product scope, TUNE's heritage naming) are either dropped or held at reduced strength. Sibling-pass research already in the atlas (push, SMS, marketing attribution, marketing automation — see STATUS.md) is used as corroborating context for family structures but not as primary evidence for new product claims.

---

## Product Observations

### AppsFlyer (evidence layer A — official Knowledge Base, five surfaces)

- **Audience segmentation of the help center itself:** tabs for *Marketers*, *Partners*, and *Developers* — the platform serves the advertiser's marketers (primary), ad-network partners (data counterpart), and developers (SDK integration).
- **Marketer-side top sections:** "Get started", "Measure & Engage", "Analyze & Optimize".
- **Get started section:** Marketer onboarding; Manage your account; **Manage your apps**; **Integrate the AppsFlyer SDK**; Integrate 3rd-party platforms; AppsFlyer basics; AI. → The app is the unit of administration; SDK integration is the onboarding spine.
- **Measure & Engage section:** Measure paid media; **Redirect & attribute users**; **Retarget users**; Cross-platform measurement; **Preserve user privacy**. → Measurement platform with engagement-side workflows (retargeting) and privacy as a first-class section.
- **Measure paid media section:** Media source configuration; **SKAN interoperation**; **SKAN solution**; **Android privacy sandbox**; then per-network configuration guides: Amazon Ads, Apple Ads, Google Ads, Google Marketing Platform, Meta ads (plus Meta campaign-management partners), Pinterest, Snap, TikTok, X Ads, generic A–F/G–Q/R–Z ad-network guides, **China market** and **China domestic market ad network configuration**; even a ChatGPT Ads (OpenAI) integration setup article. → The ad-network integration fabric is enormous and per-network; OS-privacy attribution regimes (SKAN, Privacy Sandbox) are first-class; regional ecosystem coverage (China) is structural.
- **Redirect & attribute users section:** "Set up owned media, deep link users, attribute web and mobile user journeys (PBA)" — Deep linking using OneLink; **Web-to-app attribution**; **Owned media attribution**; Email service providers. → The measurement platform also owns the link/redirect layer that carries users into the app and attributes owned-media journeys.

### Branch (evidence layer A — official Help Center root)

- **Structure:** Account Hub, **Marketer Hub** ("your daily Branch workflows, like campaign management and analytics"), **Developer Hub** (SDK, API, integrations).
- **Products split (documented FAQ):** "**Engagement** is for **owned** and **organic** channel campaigns, while **Performance** is for **paid** channel campaigns." Engagement features listed: Quick Links, Journeys, QR Codes, Email. Performance features: Ads, Engagement Builder, ROI Hub.
- **Deep linking:** "Deep linking takes users directly to content within your app, whereas deferred deep linking asks a user to install the app before taking them to the content."
- **Attribution windows:** "the length of time in which a conversion event (like an app install) can be claimed by an event caused by an advertising campaign (like a link click)" — configurable in the dashboard.
- **Privacy:** Advanced Compliance for regulated industries — data sent to an isolated endpoint, PII hashed/anonymized on receipt.
- **Positioning tie:** Branch University "training paths... to help marketers master deep linking, attribution, and the Branch Growth Platform for effective **mobile marketing**."

### CleverTap (evidence layer A — official Docs overview)

- **Self-positioning:** "a customer engagement and retention platform that provides the functionality to integrate **app analytics and marketing**." (Not "mobile marketing platform" — the engagement family's current label is engagement/retention.)
- **Platform parts:** dashboard (segment users, run targeted campaigns, analyze); **SDKs** (track actions in mobile apps and websites; personalize apps with profile data); **APIs** (push profile/event data in, export out); **Integrations** with communication platforms (SendGrid, Twilio), **attribution providers such as Branch and AppsFlyer**, and remarketing platforms (Facebook Audience Network); Webhooks.
- **Core concepts:** Users (profile created when a person launches the app or visits the website; default fields device/location; custom fields); Events (actions tracked in app/site, associated with profiles); Segments; Campaigns ("communicate with your users at scale... 13 different messaging channels"); Reports.
- **Interlock evidence:** CleverTap *integrates* Branch/AppsFlyer as "attribution providers" — the engagement suite consumes attribution rather than implementing the ad-network attribution loop itself.

### AppTweak (evidence layer A — official product site; marketing-tier source, treated accordingly)

- **Self-description:** "App Store Marketing & Intelligence Platform"; "the most comprehensive **ASO & Apple Search Ads platform** to optimize your apps' organic and paid performance in the app stores."
- **Modules:** ASO Intelligence (keyword performance, metadata suggestions, AI Visibility for app recommendations in AI assistants); Campaign Manager for **Apple Search Ads** (keyword discovery, bids/budgets automation, ROAS orientation); Reviews Manager; Market Intelligence (download/revenue estimates); consulting services.
- **Positioning claims:** ASO framed as "the foundation of any acquisition strategy"; audience = "mobile leaders", heavy gaming/finance/travel representation.
- **Structural note:** the store channel spans organic (ASO) and paid (store search ads) management inside one product — store-visibility machinery is a distinct family pole of the umbrella.

### Cross-family interlock observations (evidence layer B)

- The same substrate objects recur across all four: **the app** (registered per store/OS), **the SDK** (instrumentation spine), **the install/active user base**, **the ad-network integration fabric**, **the link/redirect layer into the app**, **the store surface** (listing/keywords/search ads), **OS privacy frameworks** (SKAN, Privacy Sandbox, anonymization modes).
- The families specialize on different slices of one loop: grow the base (UA/ads, ASO), engage the base (messaging), measure the base (attribution/analytics), route users (links). No sampled product spans all slices as its core; each integrates or defers to the others on adjacent slices (CleverTap ↔ Branch/AppsFlyer integration documented).

---

## Cross-product Comparison

| Dimension | AppsFlyer | Branch | CleverTap | AppTweak | Evidence |
|---|---|---|---|---|---|
| The marketer's own app as the administered unit | ✓ (Manage your apps; SDK integration) | ✓ (Developer Hub: SDK/API per app) | ✓ (SDK creates profiles on app launch / site visit) | ✓ (apps & games as the objects of ASO/market data) | B |
| App user base as standing population | ✓ (attribution of installs + in-app events; retargeting) | ✓ (install/convert attribution against links) | ✓ (user profiles, events, segments, lapsed/lifecycle) | ✓ (installs/downloads, ratings, reviews per app) | B |
| Store-ecosystem surface as constitutive | (implied by app/store setup; SKAN for store-ecosystem attribution) | (deep links bridge web/store; app content targets) | (app-launch profile; store not central) | ✓ (ASO + Apple Search Ads + market data) | B (store leg clearest in AppTweak; app leg everywhere) |
| OS channels/privacy frameworks as first-class | ✓ (SKAN solution/interoperation; Android Privacy Sandbox; Preserve user privacy section) | ✓ (Advanced Compliance; attribution windows) | (privacy present at platform level; not in fetched overview) | (Apple/Google store rules tracked; ASO news) | B (2–4 of 4 per facet; privacy regimes clearest in measurement family) |
| Ad-network integration fabric | ✓ (dozens of per-network configuration guides; China market) | ✓ (Ads product for paid campaigns; network attribution) | ✓ (remarketing-platform integrations; comms providers) | (Apple Ads management only — store channel) | B |
| Link/redirect layer into the app | ✓ (OneLink deep linking; web-to-app; owned media attribution) | ✓ (core identity: deep/deferred deep links, Quick Links, QR, Journeys) | (messaging into app surfaces; links via providers) | ✗ | B |
| Owned-channel engagement machinery | (retargeting measurement; ESP section) | ✓ (Journeys, Email, QR — owned/organic Engagement product) | ✓ (campaigns over many messaging channels; segments; reports) | (reviews management adjacent) | B |
| Measurement/optimization against the base | ✓ (attribution, cross-platform measurement, Analyze & Optimize) | ✓ (ROI Hub; attribution windows; campaign analytics) | ✓ (campaign reports; engagement/business metrics) | ✓ (CPI/ROAS orientation in store ads; download/revenue estimates) | B |
| Self-description family | measurement/engage platform | growth platform for mobile marketing (linking+attribution) | customer engagement & retention platform | App Store Marketing & Intelligence platform | A (per product) |
| Developer role in product shape | ✓ (Developers tab; SDK integration section) | ✓ (Developer Hub) | ✓ (SDKs/APIs as platform parts) | (light — store-data product, no SDK) | B (3/4) |

Reading: the four products implement **different slices of one operation** — operate marketing for one's own mobile app over the mobile-ecosystem substrate. No single slice is shared by all as a *core*; the shared items are the substrate objects and the loop, not any one family's machinery.

## Canonical Abstraction

### L0 — Defining Invariant

The leaf's referents are four structurally different product families. The smallest structure shared by all of them — without which a product is not a *mobile marketing* platform in any family — is three jointly-held structures at the app-portfolio level:

```text
App-operator-side platform (dashboard-led; SDK or store-data connected)
├── The marketer's own mobile app(s) as the unit of marketing
│    (registered with app-store/OS ecosystems; instrumented via SDK
│     or store-data connection — the app, not the campaign, is what the
│     platform administers and everything hangs from)
├── The app user base as the standing marketing population of record
│    (installs / active / lapsed users held and tracked over time,
│     plus the prospective users being acquired into it;
│     every family grows, engages, and/or measures against this base)
└── Marketing actions executed through the mobile-ecosystem substrate
     (app stores and their search ads · OS channels and privacy frameworks ·
      ad networks · owned links into the app), recorded so marketing
      is measured and optimized against the app user base
```

Three legs, jointly held:

- **The app as the unit of marketing** — remove it and the product becomes a generic web marketing/analytics tool (no store/OS substrate, no install semantics).
- **The app user base as the population of record** — remove it and the product becomes an ad platform serving arbitrary audiences, or raw store data.
- **Mobile-ecosystem substrate as the action surface, with measurement against the base** — remove the substrate and it is generic marketing automation; remove the measurement/optimization and it is a raw messaging or store-listing utility.

Note what is deliberately **not** in L0: any one channel loop (push, SMS), the attribution model machinery (that is the measurement family's specialization, already documented as a variant of Marketing Attribution Platform), journey/automation program structure (Marketing Automation's core), deep-link mechanics (one family's specialization), ASO keyword tooling (one family's specialization), UA media buying (DSP/ad-network territory).

### L1 — Common Mature Structure

Present across the sample; expected in the market but not definitional:

- **SDK-instrumented event spine** — install, session, and in-app events flowing from the app into the platform (measurement and engagement families; store-data connection in the visibility family).
- **Ad-network integration fabric** — per-network configuration (credentials, postbacks, attribution settings) treated as standing operational infrastructure, with per-network documentation guides; regional ecosystem coverage (e.g., China markets observed).
- **Privacy-regime machinery** — SKAdNetwork and Android Privacy Sandbox interoperation, anonymization/compliance modes for regulated industries, configurable attribution windows.
- **Owned-media link layer** — deep/deferred deep links, web-to-app routing, QR, email-to-app attribution; links both route users and carry measurement.
- **Retargeting/re-engagement workflows** — audiences exported or activated to ad networks; measurement of re-engagement campaigns.
- **Segments over the user base** — behavior/attribute-defined groups used by engagement, measurement, and store-marketing families alike.
- **Campaign/report surfaces** — per-channel campaign management plus cross-campaign analytics (installs, ROI/ROAS, retention, store visibility, engagement metrics).
- **Developer partnership in the product shape** — SDK/API surfaces and developer hubs alongside marketer dashboards (3 of 4 sampled products structure docs this way).
- **AI assistance** — copy/agent/metadata/keyword recommendations across families (era-current).

### L2 — Variant / Optional Structure

- **Family specialization (the major variant axis):** measurement/attribution-led (MMP), engagement-led, linking-led, store-visibility-led; whole-product positioning follows the family, and vendors self-describe accordingly (see observations).
- **Web presence breadth:** app-only vs web+app (web-to-app attribution, Journeys, cross-platform measurement).
- **Paid-UA depth:** measuring paid media vs managing store-ad campaigns vs full media buying (the last belongs to DSP/ad-network Types).
- **Regional substrate coverage:** China domestic ad networks, regional store ecosystems.
- **Partner-side surfaces:** data exchange for ad networks/partners (AppsFlyer's Partners tab) vs advertiser-only.
- **Vertical tuning:** gaming/finance/travel emphasis (AppTweak audience), commerce/retail emphasis (engagement family).

### L3 — Vendor-specific (kept out of the final document)

- AppsFlyer: OneLink branded deep linking; PBA (people-based attribution) terminology; SKAN "solution/interoperation" product split; China domestic market configuration guides; ChatGPT Ads integration; Partners tab.
- Branch: Engagement vs Performance product taxonomy; Quick Links; Journeys; Engagement Builder; ROI Hub; Advanced Compliance isolated-endpoint design; Branch University.
- CleverTap: "13 messaging channels" count; SendGrid/Twilio/Facebook Audience Network named integrations; platform-parts framing (dashboard/SDK/API/integrations/webhooks).
- AppTweak: ASO Agent / Ad Agent / Reviews Agent / Atlas AI product names; "60% of top grossing games" style marketing figures (marketing claims, not structural facts).

## Rejected Findings (considered, not promoted)

- **"Mobile Marketing Platform = MMP (measurement/attribution core)"** — rejected: it would collide with the processed Marketing Attribution Platform document, which already holds mobile-app attribution as one of its variants with AppsFlyer as a representative product. The measurement family is a *variant family* here, not the leaf's core.
- **"Mobile Marketing Platform = the app engagement suite"** — rejected: the engagement family's structure is marketing automation over app audiences plus owned channel loops — claimed as cores by Marketing Automation Platform and Push Notification Marketing Platform. The push and SMS passes explicitly designate this leaf as the umbrella.
- **"Paid user acquisition is the core"** — rejected: buying mobile media is DSP/ad-network/ad-buying territory; the sampled advertiser-side products *manage and measure* UA, they are not the media itself. AppTweak's Apple Ads campaign manager is advertiser-side store-channel management, a variant of the store family.
- **"Deep links are definitional"** — rejected: central to the linking family and present in the measurement family's owned-media sections, but absent from the store-visibility family as fetched. L1.
- **"SKAN/Privacy Sandbox machinery is definitional"** — rejected: era-current implementations of the privacy-regime facet; pre-SKAN attribution-era products satisfy the core without them. L1.
- **"The leaf has no structure at all (pure alias)"** — rejected at document level: while no single product structure spans the umbrella, the three-leg substrate structure is jointly held by all four sampled family poles and organizes the market's usage of the term. The alias/umbrella concern is recorded as a taxonomy issue (below), not as a reason to skip the document.
- **Precise counts/limits** (channel counts, integration counts, plan figures) — excluded from the final document; product-specific or marketing-derived.

## Boundary Findings

| Neighboring Type | Boundary test | Distinction |
|---|---|---|
| Push Notification Marketing Platform / SMS Marketing Platform / Email Marketing Platform | Single owned-channel loop vs domain umbrella | The channel Types are defined by one channel's loop (compose → permissioned audience → channel delivery → measure). This Type is defined at the app-portfolio level across paid + owned + organic store/OS/ad-network substrate. The channel Types' own documents designate this leaf as the broader umbrella. Remove the app/store/OS substrate from a channel product and it still stands; remove any channel loop from an umbrella product and it still stands. |
| Marketing Automation Platform | Program-structure overlap (engagement family) | MA's core is the person database + reusable automated program + per-contact execution state, channel-agnostic. The engagement family here is MA machinery applied to app audiences — an audience/surface variant, not this leaf's core. |
| Marketing Attribution Platform | Measurement family overlap | Attribution's core: conversion of record + attributed journey + credit-assignment model (any market). The measurement family here is that machinery specialized to the app-install market plus the app-ecosystem substrate (SDK spine, store/OS privacy regimes, ad-network fabric). The attribution leaf documents mobile-app attribution as its variant; this leaf hosts the same family as one variant family of the umbrella. **Seam flagged for joint review.** |
| Demand-side Platform / Media Buying / Ad networks | Buying vs operating | DSPs/networks sell and serve media; this Type is the app operator's own marketing operating layer (which configures networks as integrations and measures their outcomes). |
| Web / Product Analytics (no dedicated leaves here) | Analytics vs marketing operations | Analytics measure behavior; this Type runs marketing actions (acquire/engage/grow store presence) and measures them against the app base. Analytics feeds exist inside products but are not the operation. |
| Mobile Commerce Application / Mobile App Development Platform | Different universes | Consumer-side shopping surface and dev tooling; no marketing-operation loop over a user base. |
| Mobile Measurement Partner (industry term, MMP) | Naming, not structure | The measurement family's industry name; belongs inside this umbrella as a variant family. |
| App Store Optimization tools (no dedicated leaf) | Family, not separate Type | Store-visibility machinery is one variant family here (the directory has no ASO leaf; recorded as an observation, not a defect). |

**"去掉什么就变成另一个 Type" 判据：**
- 去掉 app/store/OS 底座（人群与渠道换成 email/person 数据库 + 任意渠道）→ Marketing Automation Platform
- 收缩到单一 owned channel 的 loop → Push / SMS / Email Marketing Platform（兄弟叶）
- 把核心换成 credit-assignment 模型 + journeys（不限 app 生态）→ Marketing Attribution Platform（mobile 归因是它的 variant）
- 把核心换成媒体购买本身 → DSP / Media Buying / Ad Network
- 去掉营销运营层，只留 app 用户行为分析 → Product/Web Analytics
- 去掉 app 生态只留手机号短信（pre-app 时代的 mobile marketing）→ SMS Marketing Platform 的领地

## Historical / Market-Sample Check

- **App-ecosystem-era structure:** the three-leg core (app as unit; install base as population; store/OS/ad-network substrate with measurement) holds across the measurement family's origin era (install attribution around app-store growth), the engagement-SDK era, and the current privacy-regime era. SKAN/Privacy Sandbox and AI agents are era-current L1 implementations, not the core.
- **Pre-app mobile marketing (SMS/MMS/QR/mobile-web agency platforms, roughly the pre-app-store era):** those products' machinery is the SMS Marketing Platform sibling's territory (the SMS pass already researched the shortcode-keyword era as that Type's origin). The umbrella as defined here is the app-ecosystem-era structure; the pre-app pole is recorded as a boundary note, not a counterexample — its substrate (phone numbers/carriers) fails the app leg by design.
- **Positioning drift:** the engagement family once commonly carried the "mobile marketing platform" label and today self-describes as "customer engagement/retention" (observed: CleverTap's own docs); the measurement family self-describes as measurement/attribution; the store family as "App Store Marketing". The *label* has drifted family to family over time; the *substrate structure* is what remains common. This directly supports defining the leaf at the substrate level rather than by any family's machinery.
- **Older/regional products:** regional ad-network ecosystems (China market sections observed) change the network list, not the structure. Store-visibility tools without SDKs (AppTweak) satisfy the core via the store-data connection — the SDK is the common implementation of the instrumented-app leg, not the leg itself.

Conclusion: the three-leg definition is era-stable for the app-ecosystem era and does not overfit to any single family, era, or region. The umbrella concern is a taxonomy issue, recorded below.

## Uncertainties

- **Sample breadth:** one product per family pole (four total) rather than multiple per family; Adjust/TUNE/MoEngage unreachable. Family-level claims rest on one strong product each plus sibling-pass corroboration (push/SMS/attribution passes) — stated at family level, not per-product.
- **Engagement-family privacy machinery:** CleverTap's fetched overview does not surface privacy/regulation sections; the privacy facet of the substrate is evidenced mainly in the measurement/linking families. Held as "commonly first-class", strongest in measurement.
- **Store leg outside the visibility family:** AppsFlyer/CleverTap/Branch fetched pages imply but do not foreground store-listing machinery; the store surface as a constitutive substrate element is evidenced most directly by AppTweak. Held at B (cross-family structural inference).
- **Whether the leaf should be an alias/aggregation node** rather than an independent Type: the evidence (no single product spans the umbrella as a core; sibling passes already claim the family cores) supports either reading. Decision deferred to maintainers; flagged for joint review with the marketing-attribution, push, and SMS leaves.
- **Historical label lineage:** claims about which families historically carried the "mobile marketing platform" name (analyst-category era naming, specific vendor heritage names) are qualitative; the current self-description spread is directly observed, the historical sequence is not. Kept qualitative.

## Final Synthesis

"Mobile Marketing Platform" names a **domain-level Type**: the app operator's marketing operating layer over the mobile ecosystem. Its defining structure is three jointly-held legs — **the marketer's own app(s) as the unit of marketing, the app user base as the standing population of record, and marketing actions executed through the mobile-ecosystem substrate (stores, OS channels/privacy frameworks, ad networks, owned links) with measurement against that base.**

No single product family implements the whole domain as its core. The market resolves the domain into four structural families — **measurement/attribution (MMP), owned-channel engagement, linking, and store visibility (ASO/store ads)** — each specialized on one or two legs and integrating the others (documented: the engagement suite integrating the attribution providers). The family cores are documented as Types/variants elsewhere in the atlas (Push/SMS Marketing, Marketing Automation, Marketing Attribution); this leaf holds the shared substrate structure and the inter-family seam.

The leaf therefore functions partly as an umbrella/aggregation node over §06 siblings. The document below is written for the substrate structure (the only honest joint core), with the families as variants and the seams made explicit. Joint review with the marketing-attribution, push-notification, and SMS leaves is recommended to decide alias-vs-Type status.
