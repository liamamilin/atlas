# Research Notes — Media Audience Management

Date: 2026-09-08
Leaf: Media Audience Management (§27 Media, Entertainment, Creator & Culture)
Slug: media-audience-management

## Research Goal

Understand what "media audience management" software actually is in the market: what object a media organization manages, how audience data enters and unifies, what segmentation and activation machinery exists, how the audience connects to monetization (subscriptions, advertising, events), and where the boundary runs against the §06 audience/data types (Audience Management Platform, CDP, DMP), the §06 campaign types (email marketing, newsletters, marketing automation), and the §27 siblings (Media Subscription Management, magazine-periodical-management circulation machinery, Creator CRM, creator-audience-analytics).

## Initial Boundary

Initial hypothesis at task start:

- The Type is the media organization's audience data + engagement system: the audience (readers/viewers/listeners/members) held as identified person records, data captured across media touchpoints (site, newsletter, subscription, events), segmented, and activated (email/newsletters, on-site experiences, paywall/entitlement decisions, advertiser-facing audiences).
- Nearest neighbors to separate from:
  - §06 Audience Management Platform (unprocessed; DMP pass hung a "taxonomy tension" flag saying the DMP is the market's audience-management platform for advertising)
  - §06 CDP (customer profiles, commerce-oriented per Omeda's own FAQ and BlueConic's repositioning)
  - §06 DMP (segment-of-record for ad targeting; processed 2026-09-08)
  - §06 email-marketing / newsletter-marketing / marketing-automation (campaign- and program-centric; processed)
  - §27 Media Subscription Management (unprocessed; magazine pass pre-hung heavy-overlap flag on circulation machinery)
  - §27 magazine-periodical-management (publication+issue center; processed 2026-09-08)
  - §27 Creator CRM (creator-side person records + monetization spine; processed 2026-09-07)
  - §27 creator-audience-analytics (creator-side measurement only; processed 2026-09-07)
- Alternative reading checked and rejected as the primary reading: "audience management" as studio-audience ticketing for TV tapings (1iota/OCA class). That is event-ticketing territory (no distinct software Type; agency-operated). The directory's §27 placement among media business systems (MAM, rights, royalty, subscription) and the market's own usage (Omeda self-labels "Audience Management Platform for Media") confirm the audience-data/engagement reading.

## Research Questions

1. What is the central object — the audience record/profile? What does one record carry?
2. How does audience data enter the system (registration, forms, behavioral tracking, imports, integrations)?
3. How are anonymous visitors connected to known people (identity resolution / single profile)?
4. What segmentation machinery exists (criteria-based, static lists, lookalike, combined, contextual)?
5. What activation surfaces exist (email/newsletters, journeys, personalization, metering/paywall/entitlements, advertiser-facing audience export)?
6. How do subscriptions/entitlements attach to the audience record (boundary vs Media Subscription Management)?
7. What governance exists (consent, privacy, permissions)?
8. Who uses it (roles) and what do they do day-to-day?
9. What is media-specific here vs generic CRM/CDP?
10. What did the pre-digital form look like (subscriber/circulation lists)?

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different customer layers:

1. **Omeda** — self-named "Audience Management Platform for Media"; the purest naming anchor for this Type; publisher/B2B-media/events organizations; audience-data-led with subscription and newsletter extensions. (Media-native, mid-to-enterprise.)
2. **Piano** — enterprise media/publishing platform family: Audience (customer data layer, Cxense heritage), Subscriptions (identity/entitlement/billing), Analytics, Amplifier. (Enterprise pole; data-layer + access-layer split across named products.)
3. **Zephr (by Zuora)** — subscription experience platform: registration/identity, paywall/entitlement rules, first-party data activation; billing delegated to Zuora Billing. (Access/experience-engine pole; media enterprise customers: Forbes, The Irish Times, The Globe and Mail, etc.)
4. **Pelcro** — all-in-one "Subscription & Membership Management Software" for publishers and membership orgs: subscriber CRM + paywalls + entitlements + billing. (Mid-market pole; documented straddling pole toward Media Subscription Management.)

Boundary corroboration sample (not a Type representative): **BlueConic** (horizontal CDP now positioning as "Customer Growth Engine for e-commerce brands"; industries: retail/CPG/travel — no media industry page) — used only to corroborate the CDP-side boundary.

## Sources

Fetched 2026-09-08 (WebFetch, live):

| # | Source | Tier | Status |
|---|---|---|---|
| 1 | Omeda — https://www.omeda.com/ (root; positioning, platform structure, FAQ, customer stories) | 2 | OK |
| 2 | Omeda — https://www.omeda.com/platform/ (platform page; foundational core, extensions, FAQ incl. CDP comparison) | 2 | OK |
| 3 | Omeda — https://knowledgebase.omeda.com/omedaclientkb/ (client knowledge base root: full module taxonomy) | 1 | OK |
| 4 | Piano — https://piano.io/ (root; product family, industries) | 2 | OK |
| 5 | Piano — https://docs.piano.io/ (documentation root; product structure) | 1 | OK |
| 6 | Piano — https://docs.piano.io/en/audience and /en/audience/piano-audience (Audience product doc) | 1 | OK |
| 7 | Piano — https://docs.piano.io/en/audience/segments-in-audience (segment machinery TOC) | 1 | OK |
| 8 | Zephr — https://zephr.com/ (root, served by Zuora; product capabilities + FAQ) | 2 | OK |
| 9 | Zephr — https://www.zuora.com/products/zephr/first-party-data-strategies/ | 2 | OK |
| 10 | Pelcro — https://www.pelcro.com/ (root; capabilities, industries, comparison set) | 2 | OK |
| 11 | BlueConic — https://www.blueconic.com/ (root; repositioning) | 2 | OK (boundary use only) |

Source-access limitations:

- **docs.zephr.com unreachable** (transport error ×2: / and /docs). Zephr evidence is Tier 2 (vendor marketing/product pages) only. Zephr-specific operational details (exact rule-node behavior, profile schema) are NOT asserted anywhere; Zephr claims below are kept at the capability level visible on its product pages.
- BlueConic media/publishing industry page 404; only the root was fetched. CDP-side boundary corroborated structurally (no media-industry vertical on the sampled horizontal CDP), not via a dedicated media page.
- Omeda's deeper KB articles (Olytics, Metering, Audience Builder/OnQ, Issue Closes, etc.) were evidenced via the KB's own category and article listing (fetched root), not individual article bodies. Assertions from Omeda KB are therefore capability-level (module exists, named in KB), not workflow-detail level.
- No numeric limits, no pricing, no precise defaults asserted anywhere.

## Product Observations

### Omeda (evidence layer A unless noted)

Self-positioning: "Audience Management Platform for Media". "Your audience members are people, not email addresses. Omeda unifies every signal into one profile — so subscriptions, marketing, and ad revenue all work from the same source of truth."

Platform structure (platform page):

- "Omeda brings identity, data capture, segmentation, activation, and monetization together in a single platform."
- **Audience Management Platform = "Foundational Core"**, with four named blocks:
  1. Know Your Audience — "identity resolution across channels; behavioral website audience tracking; connect unknown visitors to known profiles"
  2. Grow Your Audience — "forms and first-party data capture; personalized content and targeted experiences; conversion-focused on-site engagement"
  3. Organize & Activate — "audience builder and segmentation; data ingestion and integrations; faster audience refinement and reuse"
  4. Understand & Govern — "first-party data insights; AI task assistant; permissions, privacy, and compliance controls"
- Platform extensions: Newsletters & Marketing Automation ("email service provider and email builder; audience journeys and automations; lead scoring; hosted content; campaign and performance insights"); Subscriptions & Product Management ("promotions, gifting, and group subscriptions; payments, invoicing, and renewals; content metering and access control; product entitlements and authentication; subscription lifecycle management and insights").
- Optional accelerators: AI research/insight assistant, Snowflake secure data sharing, polls/surveys/quizzes (CredSpark), SMS/MMS, customer service management.

FAQ (vendor-drawn seams — A for Omeda's own framing):

- "connects identity, engagement data, subscriptions, newsletters, and events into a single audience record… segment audiences, activate campaigns, and understand which behaviors drive revenue"
- "How is Omeda different from a traditional customer data platform? Most CDPs serve ecommerce brands. Omeda was built for media companies. The platform connects content engagement, subscriptions, newsletters, advertising audiences, and events in one system."
- "How does Omeda create a single audience record? Omeda connects known and anonymous interactions across websites, newsletters, subscriptions, and events. These interactions link to a single audience profile."
- Data types: "Behavioral, demographic, and transactional data are stored in one system so teams understand audience interests, engagement patterns, and lifecycle stages."

Client knowledge base (Tier 1) module taxonomy (module existence evidenced, capability level):

- CDP – Customer Data Platform: **Olytics** (behavioral web tracking), **Metering**, **Personalization**
- Data Management & Governance: **Audience Builder (OnQ)**, **Data Loader**, Data Management, Manage Users UI
- Marketing Automation & Email Builder: **Email Builder (Omail)**, **Marketing Automation (Odyssey)**, SMS
- Subscription Management & Fulfillment: Fulfillment, **Audience Search (customer view)**, **Issue Closes**, Open Ended Coding (OEC — record coding), Production Schedule
- Forms & Landing Pages: **Form Builder (Dragon Forms)**
- Insights & Analytics: Reports, Audience Insights, Data Science, Snowflake secure data share
- Data Governance, Privacy & Compliance: **GDPR Consent Management**, GDPR Permission API, Compliance Library
- Professional services: data append services (ABM, events), email validation
- Payment gateways: Stripe Connect integration guide
- Video library: "Audience Relationship Management", "Audience Data — Strategic Path To Growth"

Marketing stats (positioning only, not asserted as fact in final doc): "425M+ audience records cleansed and matched", "8B+ client emails sent annually".

Customer stories (role and use-case evidence): Director of Audience Development (segmentation, data management, magazine "issue close" process), VP Data & Technology (tagging + Audience Builder + personalization "in one ecosystem"), Digital Content Lead ("eliminate data silos… target audiences at the company level" — B2B), VP Marketing ("build granular target audiences for advertisers").

Solutions pages: media breadth beyond publishing — Associations, Broadcast Media; solution intents: convert anonymous visitors, win back inactive audiences, reduce subscriber churn, increase subscription revenue, increase ad & sponsorship revenue, monetize event data, unify audience data.

### Piano (evidence layer A unless noted)

Self-positioning (root): "Revenue Intelligence + Monetization Platform"; "Piano's integrated platform connects analytics, segmentation, and subscriptions"; industry list leads with **Media + Publishing**.

Product family: **Analytics**; **Subscriptions** ("Segment, engage and convert audiences into loyal customers"; sub-pages: Journey Orchestration, Management + Billing, Print Subscriptions, **Identity Management**); **Audience** ("Customer data, made more powerful"; sub-pages: Customer Data Integration, Customer Data Segmentation, Customer Data Activation); **Amplifier** ("Grow and engage your social audience": social distribution, newsletters + notifications, campaign optimization).

Documentation (Tier 1):

- Audience product: "Ingest and enhance visitor data from any source and seamlessly put it to work on segmentation, analytics, targeting, and machine learning."
- Audience doc sections: Get Started, **Segments**, Radar, Audience Reporting, **Connectivity Hub**, **Integration Designer**, Audience Notifications, Admin, APIs, Compliance & Privacy, FAQ. (Doc tree shows Cxense lineage: "Piano Insight", "Piano Content"; Japanese doc slug for Piano Audience is literally "piano-dmp" — heritage evidence.)
- Segment machinery TOC (capability-level A): user segments, segmentation criteria, segment operations, segment creation API, advanced mode, **combined segments**, **contextual segments**, **lookalike segments**, managed segments, segments based on marketing campaign data, segments used for targeting, bulk upload in segment builder, **computed traits**, contextual targeting, conversion segments, "DMP segments", instant segmentation, lookalike modeling, user interest segments, user profile segmentation.

Structure note: Piano splits the same world into named products — the Audience layer (profiles/segments/connections) and the Subscriptions layer (identity, entitlements, billing, print subscriptions) — plus analytics. The audience profile is the substrate the other layers use.

### Zephr by Zuora (evidence layer A for its own pages; details degraded to capability level per source limitation)

Self-positioning: "The Subscription Experience Platform That Drives Conversion and Growth"; "AI Paywalls for Media and Publishers"; customers named: Forbes, The Irish Times, The Globe and Mail, New York Post, MediaHuis, Kaleva, Dumont, SCI.

Capabilities (root + first-party-data page):

- **Rules builder**: "Design and deploy personalized subscriber journeys using 50+ pre-built decision nodes… without engineering dependencies" (low-code); "user segments are available within Zephr's Rules Builder".
- **Paywalls/access**: soft, metered, hard, dynamic (AI-adjusted) paywalls; "AI-driven decisioning… adjusts access models and offers based on user behavior".
- **Identity**: "Seamlessly manage user registrations" — login rules, social sign-in, passwordless, MFA; account-sharing prevention; "Zephr Identity" as IAM for content access.
- **Data capture**: "fully customizable data capture forms… personalized data collection strategies to the right user at the right time"; "progressive profiling… as they move from anonymous visitors to known users"; GDPR/CCPA-compliant capture.
- **Activation**: "activate your first-party data to deliver: higher registration rates, better subscription rates, increased email marketing open rates, lower customer acquisition cost, higher customer renewal rates, faster churn reactivation"; personalized offers/messages/pop-ups; win-back campaigns.
- **Integration posture**: "plug-and-play integrations allow Zephr Identity to sync with your data management and customer relationship softwares"; "Zephr Optimize, helps you leverage first party data off-platform and synchronize it with your favorite tools, like Google Analytics and Tableau"; dynamic offers pulled from **Zuora Billing**; corporate (B2B) subscription management.

Reading: Zephr realizes the capture→identity→segment→activate loop with the *experience surface* (rules/paywalls/offers) as its center of gravity, and delegates subscription billing.

### Pelcro (evidence layer A unless noted)

Self-positioning: "Subscription and Membership Management Software… Recurring billing, paywalls, member data, and access — built for the way publishers and membership orgs actually work." Industries: Magazines, Newspapers, Media billing, Nonprofits, Associations.

Capabilities visible on root:

- Subscriber CRM: "Segment, tag, and manage every reader from one subscriber CRM"; "One dashboard for print and digital subscribers, plans, and lifecycle events".
- Paywalls & entitlements: metered/freemium/hard paywalls ("Meter, gate, or lock any content… set up in minutes"); "Entitlement management — plan-based access control"; authentication (passwordless, SSO, social).
- Billing machinery: payment processing (multi-gateway/multi-currency, "Stripe under the hood"), invoicing, AR/AP, deferred revenue recognition (GAAP/IFRS), dunning/retries.
- Subscriptions: plans, tiers, trials, add-ons, proration, group licences/enterprise seats, newsletters (free & paid), donations, e-commerce.
- Subscriber services/client portal: self-service management for subscribers.
- AI agents (era-current layer): AI billing, AI customer service, AI data co-pilot, AI orchestrator.

Comparison-set evidence: Pelcro ships a "Compare" nav with **vs Zuora, vs Piano, vs Naviga, vs Zephr, vs Omeda, vs AdvantageCS** — the market's own competitive set for media audience/subscription platforms. Customer titles quoted: "Director of Audience at Frieze", "Director of Engagement at Stripes", "VP Marketing at EdWeek", "Director of Product & Marketing at High Country News" — audience/subscriber-facing roles.

### BlueConic (boundary corroboration only)

Root page 2026-09-08: "The Customer Growth Engine for e-commerce brands"; FAQ repeats "for e-commerce brands"; industries: Retail & eCommerce, CPG, Travel & Hospitality. No media/publishing vertical on the root nav. Growth plays are commerce-shaped (cart recovery, replenishment, loyalty). This corroborates (layer B, structural) the vendor-drawn (Omeda, layer A) seam: horizontal CDPs orient to commerce; media audience management orients to content engagement + media monetization.

## Cross-product Comparison

| Dimension | Omeda | Piano | Zephr (by Zuora) | Pelcro |
|---|---|---|---|---|
| Self-label | "Audience Management Platform for Media" | "Revenue Intelligence + Monetization Platform"; Audience = "Customer data, made more powerful" | "Subscription Experience Platform"; "AI Paywalls for Media and Publishers" | "Subscription & Membership Management Software" |
| Central object | single audience record per person (known+anonymous linked) | user profiles + segments (Audience layer) | user (unknown→known) + their journey/entitlement state | subscriber record (person) with plans/billing/access |
| Capture machinery | forms (Dragon Forms), behavioral tracking (Olytics), Data Loader, integrations | SDKs/APIs "from any source", mobile SDKs, Connectivity Hub, Integration Designer | registration forms, progressive profiling, behavioral signals | registration/checkout, authentication, imports |
| Identity | identity resolution across channels; connect unknown→known | Identity Management product (Subscriptions layer); profiles | Zephr Identity: social sign-in, passwordless, MFA, share prevention | authentication (passwordless, SSO, social) |
| Segmentation | Audience Builder (OnQ); "build segments you can actually activate" | richest documented: criteria, combined, contextual, lookalike, conversion, computed traits, bulk upload, API | segments available inside rules builder | "Segment, tag, and manage every reader" |
| Engagement activation | Omail email + Odyssey journeys + SMS; personalization | Amplifier: newsletters + notifications, social distribution, campaign optimization | rules-driven on-site experiences: paywalls, offers, pop-ups, win-back | subscriber services; client portal; (email/SMS via AI/automation) |
| Access / entitlement | Metering + Personalization + entitlements/authentication (extension) | Subscriptions layer: entitlements, metering implicit, print subs | center of gravity: soft/metered/hard/dynamic paywalls, IAM | paywalls + plan-based entitlement management (core) |
| Monetization tie | subscription mgmt extension; "ad & sponsorship revenue"; event data monetization | Subscriptions mgmt+billing; ads via targeting/DMP segments | offers/pricing via Zuora Billing; corporate subscriptions | full billing stack (payments, invoicing, AR/AP, rev rec) |
| Governance | GDPR consent management + permission API; permissions | Compliance & Privacy section | GDPR/CCPA-compliant capture | SOC 2 posture (security, not consent machinery detail) |
| Media-domain breadth | publishing, B2B media, associations, broadcast media | Media + Publishing first industry | "media and publishers" (news majors) | magazines, newspapers, media billing, nonprofits, associations |

Cross-product commonalities (layer B — across the sampled products):

1. **One persistent record per person** in the media organization's audience — every product centers on individual-level records (Omeda "one profile"; Piano profiles; Zephr known users; Pelcro subscriber CRM records).
2. **Unknown→known conversion machinery** — forms/registration/progressive profiling plus behavioral linking of anonymous engagement to profiles (Omeda, Zephr, Piano explicitly; Pelcro via registration/checkout).
3. **Segmentation as the pivot** between data and action — every product has a named audience/segment builder; Piano's is documented most deeply.
4. **Multi-surface activation** — email/newsletters, on-site experiences/personalization, and offers in all four; entitlement/paywall machinery in all four (as core in Zephr/Pelcro, extension/layer in Omeda/Piano).
5. **Media-touchpoint data model** — content/site engagement + newsletters + subscriptions + events as the touchpoint set (explicit in Omeda; structural in the others).
6. **Monetization anchoring in media business models** — subscriptions and advertising audiences; each product ties audience state to revenue.
7. **Consent/privacy machinery** — explicit in Omeda/Zephr/Piano doc structures; SOC/security posture in Pelcro.

## Canonical Model (L0–L3)

### L0 — Defining Invariant (three jointly-held structures + domain binding)

The media organization's audience held and operated as a managed asset:

1. **The audience population of record** — persistent individually identified records for the people who consume and engage with the organization's media products (readers/viewers/listeners/members), one person one record spanning the organization's brands and channels, carrying contactability, attributes, and engagement history. Remove → a campaign tool or analytics tool with no person-level audience database.
2. **Audience data capture and unification** — the system itself grows and maintains the population: converting anonymous engagement into known people (registration/data-capture surfaces, behavioral signals linked to profiles) and ingesting/unifying touchpoint data (content engagement, newsletters, subscriptions, events) onto those records. Remove → a static purchased/mailing list (the decaying pre-history); without unification the "one audience" is a pile of channel silos.
3. **Segment-and-act management loop** — the audience can be organized into usable groups (segments/lists by attributes, behavior, engagement) and acted upon through activation surfaces (email/newsletter sends, on-site experiences/personalization, access/entitlement-relevant experiences, audience hand-off to advertising), with results recorded back to the population. Remove → a profile store or reporting tool; the "management" is gone.

**Domain binding**: the record population is anchored in engagement with the organization's own content and media products — remove the media/content binding (engagement with the org's content as the record's anchor, media monetization as its purpose) → generic CRM / CDP territory.

Jointly-held is load-bearing:

- 1 alone = contact manager / address book
- 2 without 1 = anonymous traffic analytics (no audience of people)
- 3 without 1+2 = campaign machinery on empty lists
- 1+2 without 3 = a unified profile store (a data layer, not management)
- 1+3 without 2 = a static, decaying list you can slice but never refresh or grow
- 2+3 without 1 = anonymous segment tooling (ad-tech DMP-like) with no person-level audience

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Identity resolution / deduplication machinery as an explicit capability (Omeda names it; Piano has Identity Management; Zephr IAM; Pelcro authentication)
- Email/newsletter sending + journeys/automations built on the audience DB (Omeda extension; Piano Amplifier; Zephr messaging; Pelcro newsletters)
- Content metering, personalization, paywall/entitlement configuration (all four; core in the experience-engine pole)
- Rich segmentation machinery: combined/contextual/lookalike/conversion segments, computed traits (Piano-documented depth; builders in all)
- Consent management (GDPR-class), permission API, privacy controls
- Reporting/insights on audience health, growth, engagement, churn; AI assistants (era-current)
- Integrations/exports: CRM/analytics/warehouse connections (Snowflake share, GA/Tableau syncs, connectivity hubs); advertiser-facing audience delivery
- Data append/validation services (Omeda professional services)

### L2 — Variant / Optional Structure

- Center-of-gravity packaging: audience-data-led platform (Omeda) vs integrated suite split into named products (Piano) vs experience-engine pole (Zephr) vs subscriber-billing-led (Pelcro)
- Subscription billing depth: full in-product billing stack (Pelcro) vs delegated to external billing (Zephr→Zuora) vs subscription extension (Omeda)
- Segment organicity: dynamic criteria-based vs managed/static uploads vs lookalike/modelled (product-dependent mix)
- Domain breadth: B2B media (company-level targeting), consumer publishing, associations/membership, broadcast/streaming
- Events as an audience touchpoint with monetization (Omeda solution line; Questex case)
- AI layer: agentic assistants, AI paywall decisioning, AI audience builders (era-current; all four market it)

### L3 — Vendor-specific (research notes only)

- Omeda: Olytics, OnQ Audience Builder, Odyssey, Omail, Dragon Forms, CredSpark accelerator, Omeda MCP/Agentic Audience Builder, Issue Closes, Open Ended Coding (OEC), "State of Audience in Media" report
- Piano: Cxense heritage (Insight/Content; "piano-dmp" doc slug), Radar, Connectivity Hub, Integration Designer, Amplifier naming
- Zephr: 50+ decision nodes claim, Zephr Identity/Optimize naming, Dynamic Offers module on Zuora Billing
- Pelcro: AI Agents suite (Coding Agent, AI Billing, AI Orchestrator…), USPS address verification, Stripe-under-the-hood, GAAP/IFSR rev-rec module
- BlueConic: Agent Studio, Growth Plays, Jebbit experiences acquisition (boundary pole only)

## Rejected Findings

- **"Audience management = email marketing for media"** — rejected: campaign machinery is an extension in the audience-data pole and the experience pole, not the center; the audience population and its management loop persist independent of any channel.
- **"Audience management = paywall/subscription tooling"** — rejected: Pelcro's billing-heavy center and Zephr's access-heavy center both still hold the audience population + capture + segmentation; the paywall is one activation surface. In Omeda's own packaging, subscriptions are an *extension*, not the foundational core.
- **"A CDP by another name"** — rejected as an alias: the media domain binding (content engagement as the record's anchor; anonymous→known audience growth; media monetization outputs) is load-bearing in the sampled products' own positioning (Omeda FAQ; Piano media-first industry; Zephr "media and publishers"; Pelcro publishing industries). The object world overlaps heavily with CDP/DMP, but the Type's center is the media organization's audience asset, not the generic customer profile or the advertising segment.
- **Phone/email-address-centric definition** — rejected: like the IM phone-number case, contact substrate (email, postal, member ID) is implementation; the invariant is the identified person record's contactability.
- **Anonymous-only segment tooling (ad-tech DMP posture)** — rejected for this Type: DMP's center is the segment for ad targeting with third-party data openness; here the center is the person-level population of the org's own audience.

## Historical / Market-Sample Check

Pre-digital and early-digital forms (conceptual level — no primary archive fetched):

- Magazine/newspaper publisher's subscriber & circulation files: a card/ledger per subscriber with name, address, demographic/industry coding (B2B controlled-circulation qualification), renewal and requalification campaigns, and the audited circulation "issue close" — leg 1 (population of identified records) ✓, leg 2 (capture via subscription forms, surveys, service cards; hand-maintained unification) ✓ analog, leg 3 (list segmentation — demographic/industry selects — and activation via postal campaigns, renewals, and list rental to advertisers) ✓ analog. Media binding ✓.
- B2B publisher list rental and advertiser-audience production (selects sold from the file) = the pre-history of "audiences for advertisers".
- Newsletter/association membership rolls with member segmentation = same structure in adjacent domains.

Conclusion: the definition passes the historical check without naming any era machinery (cookies, behavioral tags, AI, meters, warehouses). All of those are L1/L2 implementations.

## Boundary Findings

1. **vs Customer Data Platform (§06, unprocessed pass, timeout 2026-09-08)** — heaviest structural overlap (profiles, unification, segments, activation). Seam adopted: domain binding + monetization posture. CDP = generic cross-industry customer profile for commerce/journey activation (sampled horizontal CDP now self-describes "for e-commerce brands", commerce-shaped plays); Media Audience Management = the media organization's audience anchored in content engagement with media monetization outputs (subscriptions, advertising audiences, events). Vendor-drawn seam recorded first-hand (Omeda FAQ: "Most CDPs serve ecommerce brands. Omeda was built for media companies"). Keep-both. Ratification requested when the CDP leaf is processed.
2. **vs Data Management Platform (§06, processed)** — clean seam per the DMP pass's own L0: DMP centers the *segment* (advertising targeting unit, open to third-party data, activation into media systems); Media Audience Management centers the *person-level audience population* of the org's own audience with content-engagement capture. Advertising-audience export is here an L1/L2 capability (Omeda "target audiences for advertisers"; Piano targeting/"DMP segments"), not the center. No tension; consistent.
3. **vs Audience Management Platform (§06, unprocessed; failed run 2026-09-06)** — taxonomy risk pre-hung by the DMP pass (the DMP is the market's "audience management platform" for advertising). This pass adds: the media-industry usage of exactly that phrase is realized by Omeda under this §27 leaf. When audience-management-platform is processed, joint review should decide: (a) alias of DMP, (b) capability slice, (c) martech audience tools — and whether §06 leaf should explicitly exclude the media-industry reading documented here. No directory change made from this side.
4. **vs Media Subscription Management (§27, unprocessed; magazine pass pre-hung flag)** — subscription/billing machinery appears in 4/4 sampled products at varying depth (extension → full stack). Adopted seam: this Type's center is the audience population and its management loop across all media products; the subscription is one attached monetization context (lifecycle + entitlement states riding on the audience record). Media Subscription Management should center the subscription product/billing lifecycle itself. Pelcro recorded as the straddling pole (full billing stack + subscriber CRM). Joint review requested when that leaf is processed.
5. **vs magazine-periodical-management (§27, processed)** — consistent with that pass: the publication+issue is the center there; here the person-audience is the center and the publication/issue is one touchpoint context (Omeda KB documents "Issue Closes" inside an audience platform — product-spanning evidence, keep-both; matches that pass's "audience CDP = standard capability" note read in reverse).
6. **vs email-marketing-platform / newsletter-marketing-platform / marketing-automation-platform (§06, processed)** — the campaign/send/program is the organizing object there; here the audience asset is the organizing object and campaigns/journeys are activation surfaces built on it. Consistent with the organizing-object seams those passes recorded. Omeda ships an ESP+automation extension on the audience core — spanner evidence, keep-both.
7. **vs Creator CRM (§27, processed)** — side seam: creator-side person records + monetization spine for the creator's own audience vs organization-side media audience management (multi-brand, events, advertising audiences, anonymous→known at site scale). Keep-both, consistent with that pass's domain-instantiation note.
8. **vs creator-audience-analytics (§27, processed)** — measurement-only vs managed population; analytics surfaces exist here as standard capabilities, but this Type requires the record population + management loop. No conflict.
9. **vs Broadcast/streaming measurement tools (not a directory leaf; Conviva/Nielsen class, not fetched)** — audience *measurement* (panel/census ratings) is adjacent analytics, not management of a record population; noted as a naming collision zone ("audience" in media = both measurement and relationship). Not hung as a flag; recorded for awareness.
10. **Name-ambiguity note (like content-distribution-platform pass)** — "audience management" also names ad-tech practice (DMP) and studio-audience ticketing; this leaf is the media-organization audience-asset Type per directory placement and market naming (Omeda). No overlap with ticketing territory.

## Uncertainties

- Piano's Audience product vs its Subscriptions product: exact boundary of what lives where is documented only at TOC level (fetched); no workflow-level claims made.
- Zephr: Tier-1 docs unreachable; all Zephr-specific machinery statements are capability-level from vendor pages (rules builder, identity, paywall modes, progressive profiling). Product-specific numbers (e.g., "50+ decision nodes") not asserted in the final document.
- Omeda KB module internals (Olytics, Metering, OnQ) evidenced at module-existence level only.
- Whether the broadcast/streaming pole has distinct audience-management products with materially different object worlds (beyond Omeda's broadcast solution page) — unexplored; likely a variant, not a distinct Type, but unverified.
- Pelcro's "subscriber CRM" segment machinery depth (dynamic vs static) not documented at fetched depth.

## Final Synthesis

A Media Audience Management application is the media organization's audience system of record and management environment. Its defining core is three jointly-held structures bound to the media domain: (1) the audience as a persistent population of identified person records spanning the organization's brands and channels; (2) the machinery that grows and unifies that population from the media operation's touchpoints — converting anonymous engagement into known people and consolidating content engagement, newsletter, subscription, and event data onto single records; (3) the segment-and-act loop — organizing the population into usable groups and activating them through email/newsletters, on-site experiences and access decisions, and advertiser-facing audience delivery, with outcomes recorded back. Everything else commonly present (identity-resolution tooling as a named capability, consent management, metering/paywalls, rich segment types, billing, AI assistants, warehouse integrations) is standard or variant machinery layered on that core. The Type's nearest dangerous neighbor is the horizontal CDP; the adopted seam is the media domain binding plus media monetization posture, drawn by the vendors themselves and corroborated by the sampled horizontal CDP's commerce-only repositioning.

