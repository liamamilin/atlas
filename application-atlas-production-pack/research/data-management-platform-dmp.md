# Research Notes — Data Management Platform / DMP

Research date: 2026-09-08
Directory leaf: "Data Management Platform / DMP" (§06 Marketing, Advertising & Growth)
Slug: data-management-platform-dmp

---

## Research Goal

Understand what a Data Management Platform actually is as an application type — its defining structure, its core objects, its workflows, its interfaces, and its boundaries against neighboring types (CDP, DSP, Ad Server, Audience Management Platform, data marketplaces/providers, data clean rooms, tag managers) — from real product documentation, not vendor marketing.

## Initial Boundary

Working hypothesis before research:

- A DMP is an advertising-side platform that collects audience data from multiple sources (own properties, partners, purchased third-party data), organizes it into managed audience segments, and makes those segments available to advertising/media systems (DSPs, ad servers, ad networks, social platforms) for targeting.
- The central object hypothesis: the **audience segment** (a targetable group), not the persistent individual profile (that is the CDP's center).
- Most confusable neighbors: Customer Data Platform / CDP (closest sibling — profile-of-record vs audience-of-record), Demand-side Platform / DSP (buys media with audiences), Ad Server (delivers ads, holds simple targeting data), Audience Management Platform (directory sibling leaf in the same section — potential alias), third-party data providers/marketplaces (the supply side the DMP buys from), data clean rooms, tag managers.
- Known market tension: the DMP category is widely described as declining/converging with CDPs after third-party cookie deprecation; several classic DMPs (Oracle BlueKai, Salesforce DMP/Krux) have been sunset. The type must be defined so that both the classic cookie-era DMP and the modern privacy-safe cohort-based DMP fit.

## Research Questions

1. What is the central object — segment/audience/cohort? How is it defined, stored, organized (taxonomy)?
2. What data comes in — first-party (tags/SDKs/CRM onboarding), second-party (partner data), third-party (data providers/exchanges/marketplaces)?
3. How are segments built — rule/traits, boolean + recency/frequency, lookalike/algorithmic models, contextual?
4. What identity/addressability model — cookies, device IDs, cross-device graphs, hashed emails, cohort codes? How persistent?
5. How does activation work — destination types, sync mechanisms (cookie/URL/S2S/bidstream), which ad systems?
6. What insights/analytics surround the segments?
7. What variants exist — advertiser-side vs publisher-side vs agency-side; suite module vs independent; data monetization?
8. Where are the boundaries vs CDP, DSP, ad server, Audience Management Platform, data providers, clean rooms?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| Adobe Audience Manager | enterprise suite DMP (canonical, explicitly self-described DMP) | the most fully documented classic DMP; advertiser+publisher both |
| Lotame (Spherical) | independent pure-play DMP, repositioned as "data collaboration platform" | classic independent DMP lineage; shows the category's current repositioning; marketer/agency/media-seller poles |
| Permutive | modern publisher-side, privacy-safe cohort-based DMP | the post-cookie DMP pole; strong official docs |
| OnAudience | third-party audience data provider (boundary-adjacent sample) | the data-supply side of the DMP ecosystem; used for boundary analysis, not as a core representative |

Not sampled: Oracle BlueKai and Salesforce DMP (both sunset; docs not fetched this pass), Nielsen DMP, 1plusX (transport error).

## Sources

Fetched 2026-09-08:

- Adobe Audience Manager (Tier 1 — official product documentation, Experience League):
  - Docs root: https://experienceleague.adobe.com/en/docs/audience-manager
  - Audience Manager Overview (incl. "Three functions of a Data Management Platform (DMP)"): https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/overview/aam-overview
  - Signals, Traits, and Segments: https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/reference/signal-trait-segment
  - Segments: Purpose, Composition, and Rules: https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/features/segments/segments-purpose
  - Destinations Overview: https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/features/destinations/destinations
  - Types of Data Collected (first/second/third-party): https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/overview/data-types-collected
  - Profile Merge Rules Overview: https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/features/profile-merge-rules/merge-rules-overview
  - Algorithmic Models Overview (Look-Alike Modeling, Predictive Audiences): https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/features/algorithmic-models/algo-models-overview
  - Audience Marketplace: https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/features/audience-marketplace/audience-marketplace
  - Audience Manager Guide (main functionality TOC): https://experienceleague.adobe.com/en/docs/audience-manager/user-guide/aam-home
- Permutive (Tier 1 — official product documentation):
  - Docs root / Introduction: https://docs.permutive.com/
  - Concepts overview: https://docs.permutive.com/concepts
  - Cohorts: https://docs.permutive.com/concepts/cohorts
  - Activations: https://docs.permutive.com/concepts/activations
  - Events: https://docs.permutive.com/concepts/events
  - Identity: https://docs.permutive.com/concepts/identity
- Lotame (Tier 2 — official product/marketing pages only; help center unreachable):
  - Home: https://www.lotame.com/
  - Spherical Platform: https://www.lotame.com/products/spherical-platform/
- OnAudience (Tier 2 — official product/marketing pages only):
  - Home: https://www.onaudience.com/

Source-access limitations:

- Lotame operational documentation (docs.lotame.com, help.lotame.com) was unreachable (transport errors, 2 attempts each). Lotame observations rest on official product pages (Tier 2); operational-detail claims for Lotame are held at reduced strength.
- 1plusX unreachable (transport error, 1 attempt) — abandoned per network rule.
- Oracle BlueKai / Salesforce DMP sunset-product documentation not fetched; the classic DMP pattern is instead evidenced through Adobe's own DMP framing and Permutive's description of the "traditional" cookie-based pattern (both Tier 1).
- Marketing numbers observed on product pages (e.g., OnAudience "25B+ devices", "4,100 predefined segments"; Lotame "100+ connections") are recorded here only and deliberately excluded from the final document.

---

## Product Observations

### Adobe Audience Manager

Evidence layer: A (direct observation of official docs)

Key observations:

- Self-description: "bring your audience data assets together... collect commercially relevant information about site visitors, create marketable segments, and serve targeted advertising and content to the right audience." Explicitly frames "Three functions of a Data Management Platform (DMP)": **Data In** (collects first-party data from channels and devices — web analytics, CRM, device data, e-commerce), **Audience Creation** (unifies data into audience profiles; look-alike models; audience segments; supplement with second- and third-party data sources), **Data Out** (activates audience segments by pushing them to DSPs, campaign management systems, and other marketing platforms).
- Positioning: "not tied to a data seller, exchange, or demand-side platform... completely agnostic when it comes to our partners' data assets"; serves "digital publishers" as well as advertisers.
- Core data model: **Signals** (smallest data units, key-value pairs, e.g. `product=camera`, `price>1000`) → **Traits** (combinations of signals with Boolean/comparison qualification rules) → **Segments** ("users who share a set of common attributes and qualify for related traits"; Boolean expressions + recency/frequency requirements). Data arrives via **event calls** (HTTP requests carrying key-value pairs). Traits/segments managed with visual tools and code editors.
- Segments: "a set of users who share common attributes"; server-side rules built from behavior, demographics, other characteristics; Segment Builder supports Boolean operators, comparison expressions, recency/frequency; segments combine first- and third-party traits; segment data sent to destination partners; performance monitored with reports. Adobe Analytics segments can be mapped in as read-only segments/traits.
- Data types collected: **first-party** (customers; online consumer interactions or offline), **second-party** (strategic partners/advertisers; typically via placing the container tag on the partner site), **third-party** (data providers and/or exchanges; intent, demography, social/lifestyle, psychographic). Collected data managed with **time-to-live (TTL)** values controlling data expiration across sources. Raw data mapped to a customer-defined **taxonomy** adjustable without changing collection code.
- Data in mechanisms: Data Collection Servers (DCS event calls), batch data ingestion (file transfer), log ingestion, forwarding Adobe Analytics data.
- Identity: **Profile Merge Rules** — two profile types: **device profile** (tied to cookie ID or mobile device ID; rule-based traits when unauthenticated; onboarded traits tied to device ID such as cookie-based third-party data) and **authenticated profile** (tied to user ID passed at login; rule-based traits across devices; onboarded offline traits linked to the user ID). **Profile Link Device Graph** = stored mapping of a person's devices to their authenticated profile (deterministic device graph). Merge rules control which data sets are used for segmentation and enable cross-device targeting.
- Algorithmic: **Look-Alike Modeling** (select a trait or segment, a time interval, and first- and third-party data sources; the model finds eligible users with shared characteristics; output lands in Trait Builder as algorithmic traits with accuracy/reach tradeoff; combinable with rule-based traits) and **Predictive Audiences** (classifies unknown audiences into personas by propensity for known audiences).
- Third-party data acquisition: **Audience Marketplace** — data providers and buyers execute data deals self-service; specialized features per role (buyer/seller, can be both); handles contracts, billing, payments; data feeds; private data feeds; role-based permissions.
- Data out: **Destinations** — "any third-party system (ad server, DSP, ad network, etc.) that you want to share data with"; **Destination Builder** creates/manages cookie, URL, or server-to-server destinations. Types: Adobe Experience Cloud destinations; **People-Based Destinations** (audience segments to people-based environments such as Facebook, via hashed identifiers; Google Customer Match); **Device-Based Destinations** (server-to-server; build large audience pools over time; visitors need not be seen again); **Custom Destinations** (URL/cookie; immediate action on qualified users; visitors must be seen again). Delivery method depends on the partner's technical capability.
- Consent: IAB TCF v2.2 plug-in listed among latest features.
- Administration: user roles (administrators vs users) in Audience Marketplace; activity usage reporting.

### Lotame (Spherical)

Evidence layer: A for existence/positioning of capabilities on official product pages; Tier 2 only — operational depth not verifiable this pass.

Key observations:

- Positioning: "Epsilon Lotame" (acquired by Publicis Groupe); 20 years of data experience; self-described data/identity company for digital marketers.
- Products: **Spherical Platform** ("data collaboration platform (DCP)" — orchestration, enrichment, insights & activation capabilities), **Addressable Audiences** (Curated Marketplaces + **Lotame Data Exchange (LDX)** marketplace), **Data & Identity Services** (standalone services).
- Spherical capability set (product pages): First-Party Data Onboarding & Management ("connect, enrich, analyze, and segment offline and online data"), Audience Creation & Modeling ("segment customers, find patterns, and create lookalikes" — "with trusted data sources, AI/machine learning and lookalikes"), Audience Enrichment ("expand and enrich your target audiences with scalable, trusted partner data"), Audience Insights ("easily compare audiences, create charts"), Identity Resolution & Activation ("identify unique users across various channels and devices"), CTV Targeting, Curation ("get all the upside of advertising via Private Marketplace (PMP)... Data Empowered Curated Marketplaces"), Collaborations: Insights & Targeting ("collaborate directly with data providers and media owners in a privacy-safe way"; "clean-room-like capabilities without moving data"), Revenue & Monetization ("media owners show off your high-value traffic by creating the first-party audiences that buyers can't get elsewhere").
- Packaging poles (capability matrix on the Spherical page): **Spherical Data Collaboration Platform** (for marketers: 1P onboarding, insights, modeling, creation, enrichment, LDX marketplace, branded data sources, collaborations, identity resolution, activation connections), **Spherical Data Buyer** (for agencies: "build, plan, and learn from their own segments"; access LDX/branded partners/collaborations; finetune personas, discover insights, target smarter), **Spherical Data Seller** (for media companies: "collect your first-party data and create revenue-driving audiences"; "permission audiences directly to marketers and agencies via data collaboration tools"; "control syndication and extension of your audience segments across browsers and devices to leading DSPs"; audience monetization).
- Interop: "Connect with leading SSPs, DSPs, ad servers, social platforms, CDPs, data warehouses, personalization and measurement platforms, clean rooms, and more" (partner logos include DV360, Meta, The Trade Desk, Roku, Snowflake, Tealium, BlueConic, Amazon).

### Permutive

Evidence layer: A (direct observation of official docs)

Key observations:

- Self-description: "the predictive data collaboration platform for the open internet"; serves media companies and advertisers; built on first-party signals; claims 100% addressability including privacy-safe environments (Safari, Firefox, iOS) via edge/on-device processing.
- Product areas: **Data Management** ("build and activate publisher signals for cohort, identity, and contextual data that drive advertiser outcomes; plan campaigns, optimize targeting, and report on performance — AI-driven workflows"), **Data Clean Room** (secure collaboration between media companies and advertisers to match, model, and activate audiences without sharing PII or moving data), **Curation** ("package publisher signals with AI into curated audiences available in SSP marketplaces").
- **Cohort** (the central object): "a privacy-safe representation of an audience." Contrast with the traditional pattern (documented by Permutive itself): "Traditionally, user IDs like third-party cookies have been used to communicate information about audiences and activate (target) them... the ad server can later target an ad for a request from that user based on the information it has attached to their cookie ID." With cohorts, "a code represents the group of users that fall into an audience"; the cohort code — not a user ID — is included in the ad request; no user profile can be built from it; works in environments where third-party cookies and deterministic IDs are prohibited.
- Cohort types: **custom cohorts** (publisher-defined from first-party behavioral data, e.g. article-category readers), **contextual & affinity cohorts** (page-level signals; NLP classification of categories/keywords/sentiment; affinity scores computed from consented users' engagement), **modeled cohorts** (lookalike modeling or classification models from a seed audience), **standard cohorts** (pre-built taxonomies such as IAB categories).
- **Activation**: "a cohort configured for delivery to a specific ad platform." Cohort membership is computed **on-device** by the SDK; when a user is a member of an activated cohort, the SDK delivers the activation data directly to the ad platform during the ad request — typically as key-value pairs to the ad server — in real time on the first pageview. Activation types: **ad server activations** (Google Ad Manager, Xandr, FreeWheel), **bidstream activations** (via Prebid, making audiences available to demand-side buyers), **identity-based activations** (server-to-server integrations using hashed emails, advertising IDs, or IP addresses, enabling activation with DSPs/SSPs). Publishers control which cohorts go to which platforms (platform-specific targeting, data governance, performance).
- **Events**: user actions on site/app (pageviews, clicks, video views); publisher-defined event schemas with properties and data types; default event types for common publisher use cases; events enable "granular segmentation of users into cohorts for real-time activation & insights, and warehousing of first-party data."
- **Identity**: SDK allocates a first-party **user ID** per device per publisher (distinct across publishers; no reliance on third-party cookies or mobile device IDs); used in the cloud for publisher-level audience insights and on-device to store cohort information across sessions. **Identifiers** (tag + value, e.g. `email`, `uid2`, `rampid`) enable cross-device unification, connecting auxiliary third-party audience data (with consent), and identity-based activation. **Identity Graph** configured in the dashboard; identity resolution merges profiles matching an identifier, resolved in priority order. **User group identifiers** (e.g. household ID) enable household-level cohorts, cross-device household targeting (CTV), household frequency caps; household graphs imported from warehouses (BigQuery, Snowflake, S3).
- **Insights**: understanding audience reach. **Workspaces**: sites/business units across the organization. **Source/Destination**: connecting data to and from Permutive.

### OnAudience (boundary-adjacent sample — third-party data provider)

Evidence layer: A for positioning (official site); Tier 2 only.

Key observations:

- Self-description: "Global data provider... fuel digital campaigns and business solutions through high quality data with global reach."
- Products: Audience Data, AI Audiences, OnAudience Curate, Data Enrichment, Raw Data, Cookieless solutions. Clients: marketers & agencies, data partners, platforms, data science teams, investors & consulting.
- Marketing-scale claims (Research Notes only): 25B+ devices, 200+ markets, 4,100 predefined segments; testimonials from platform partners (Microsoft Advertising, PubMatic) about supplying audience segments and custom auction packages.
- Structural read: this is the **data-supply side** of the DMP ecosystem — it sells predefined audience segments and raw data to platforms/DSPs/agencies; it does not provide the buyer with an operator-side environment to collect, manage, and activate their own audience data. Useful for the boundary against data providers/marketplaces.

---

## Cross-product Comparison

| Dimension | Adobe Audience Manager | Lotame (Spherical) | Permutive |
|---|---|---|---|
| Central object | Segment (rule over traits over signals), held in a customer-defined taxonomy | Audience/segment (built from onboarded + enriched + marketplace data) | Cohort (privacy-safe audience representation; code-based) |
| Data in | Event calls (HTTP key-value pairs), batch file ingestion, log ingestion, Analytics forwarding; first/second/third-party | First-party onboarding (offline + online), enrichment from LDX marketplace and branded partners, collaborations | SDK events with schemas (pageviews, video views...), warehouse connectivity (household graphs), identifiers |
| Identity/addressability | Device profile (cookie/mobile ID) + authenticated profile (user ID); Profile Link Device Graph; ID sync with partners | Identity resolution & activation ("unique users across various channels and devices") | First-party SDK user ID (per publisher); identifiers (email, uid2, rampid); Identity Graph; household IDs |
| Segmentation machinery | Trait Builder + Segment Builder: Boolean, comparison operators, recency/frequency | Audience creation & modeling: patterns, lookalikes, AI/ML | Custom / contextual & affinity / modeled / standard cohorts; on-device membership computation |
| Algorithmic expansion | Look-Alike Modeling; Predictive Audiences (personas) | Lookalikes, AI/ML modeling | Modeled cohorts (lookalike/classification) |
| Third-party data acquisition | Audience Marketplace (data feeds, buyer/seller roles, contracts/billing) + third-party providers/exchanges | LDX marketplace + branded data sources + collaborations | Auxiliary third-party audience data via identifiers (consent-gated) |
| Activation out | Destinations: cookie/URL/S2S; Adobe Experience Cloud; People-Based (hashed IDs → social platforms); device-based S2S | Connections to SSPs, DSPs, ad servers, social platforms, CDPs, warehouses; syndication to DSPs | Ad server activations (GAM/Xandr/FreeWheel), bidstream (Prebid), identity-based S2S (DSPs/SSPs) |
| Insights | Audience optimization reports; segment performance monitoring | Audience insights (compare audiences, charts) | Insights (audience reach) |
| Privacy/consent | IAB TCF v2.2 plug-in; TTL-based data expiration | Privacy-safe collaborations; clean-room-like without moving data | Privacy-safe cohorts (no user IDs in ad requests); on-device processing; consent-gated auxiliary data |
| Side of market | Advertisers + publishers | Marketers, agencies (Data Buyer), media companies (Data Seller) | Media owners first + advertisers |
| Monetization of audiences | Audience Marketplace as seller | Data Seller pole; Curated Marketplaces | Curation into SSP marketplaces |
| Suite posture | Adobe Experience Cloud module | Independent (Epsilon/Publicis-owned) | Independent |

## Canonical Model

### L0 — Defining Invariant (deliberately minimal)

A Data Management Platform is definable by three jointly-held structures:

1. **The managed audience segment as the unit of record** — persistent, named groups of addressable people/devices, defined by qualification rules and/or models over collected audience data, held in an organized library/taxonomy the operator maintains and curates. The segment — not the individual profile — is the system's central object.
   - Remove → a raw data store / tag manager / analytics tool (data without managed targetable groups).
2. **Multi-source audience data aggregation** — audience data collected from the operator's own properties (first-party behavioral/CRM), exchanged with partners (second-party), and/or acquired from external providers (third-party data marketplaces/exchanges) is combined into the segment pool. The DMP is deliberately open to data it does not itself collect.
   - Remove → a single-platform audience builder (an ad platform's own native audience tools on its own data).
3. **Audience activation into advertising/media systems** — segments are exported/synced to external advertising systems (DSPs, ad servers, ad networks, social/people-based platforms) where they are used for media targeting. The DMP prepares and delivers audiences; it does not buy media or serve ads itself.
   - Remove → an audience analytics/insights tool (data in, nothing targeted with it).

Jointly-held is load-bearing:

- 1 alone = a segment library with no data flowing through it
- 2 without 1+3 = an audience data warehouse
- 3 without 1+2 = a one-off audience sync utility
- 1+2 without 3 = audience analytics
- 1+3 without 2 = segment building on own data only (ad-platform-native territory)
- 2+3 without 1 = an anonymous data conduit

Identity substrate is deliberately abstracted: segments are held over **addressable identifiers usable in media targeting** — cookies, device IDs, mobile advertising IDs, hashed emails, or cohort codes. This keeps the definition era-safe: the classic cookie-pool DMP and the modern cohort-code DMP both satisfy it.

Historical / market-sample check: the classic early-2010s DMP — pixel-based collection into cookie pools, trait/segment taxonomy, third-party data marketplace, DSP sync — satisfies all three legs with no AI, no cookieless cohorts, no clean rooms, and no CDP convergence. This pattern is directly evidenced in the sample: Permutive's own documentation describes the "traditional" pattern (audience data attached to cookie IDs, ad server targets on it), and Adobe's documentation still frames the DMP as Data In / Audience Creation / Data Out. A pre-digital list-broker practice (aggregated mailing lists, organized segments, rented per campaign) is a thin paper-era ancestor by reasoning, not by documented continuity. Conversely: a DSP fails leg 3 (it buys media rather than managing audiences); a pure data provider (OnAudience) fails leg 1 (no operator-side segment management); a CDP fails the center-of-gravity test (persistent individual profiles, not segments, are its object).

### L1 — Common Mature Structure

Present across the sample (evidence layer B), not required to recognize the Type:

- Rule/qualification builders with Boolean logic, comparison operators, recency/frequency (Adobe explicit; Permutive custom cohorts; Lotame audience creation)
- Look-alike/algorithmic modeling for audience expansion (all three: Adobe Look-Alike + Predictive Audiences; Lotame lookalikes/AI-ML; Permutive modeled cohorts)
- An identity/addressability layer: device graphs, identity resolution, identity graphs (all three)
- Third-party data acquisition machinery: marketplace with buyer/seller roles and billing (Adobe Audience Marketplace, Lotame LDX), or identifier-based auxiliary data (Permutive)
- Destination/activation catalogs toward DSPs, ad servers, ad networks, social platforms (all three)
- Audience insights/reporting (all three)
- Consent/privacy machinery (Adobe IAB TCF plug-in; Lotame privacy-safe collaborations; Permutive privacy-safe cohorts + consent-gated auxiliary data)
- Offline/CRM data onboarding into audience data (Adobe batch ingestion; Lotame first-party onboarding)

### L2 — Variant / Optional Structure

- Side of market: advertiser-side vs publisher-side vs agency-side (Lotame explicitly packages Data Buyer for agencies and Data Seller for media companies; Permutive is publisher-first; Adobe serves both)
- Audience monetization: selling one's own audiences (Adobe Audience Marketplace seller role; Lotame Data Seller; Permutive Curation into SSP marketplaces)
- Data collaboration / clean-room-like capability (Lotame collaborations without moving data; Permutive Data Clean Room as a product area)
- Contextual/page-level targeting alongside user-level (Permutive contextual & affinity cohorts)
- CTV/household targeting (Permutive household IDs; Lotame CTV targeting)
- Suite module vs independent product (Adobe Experience Cloud module vs Lotame/Permutive independent)
- Standard/pre-built taxonomies (Permutive standard cohorts on IAB categories; Adobe's taxonomy mapping)

### L3 — Vendor-specific Structure (Research Notes only)

- Adobe: Signals/Traits/Segments terminology; DCS event-call API; Destination Builder with cookie/URL/S2S types; People-Based Destinations (hashed identifiers); Profile Merge Rules + Profile Link Device Graph; Audience Marketplace with private data feeds; Predictive Audiences; TTL values; Adobe Audience Finder directory; Analytics segment mapping as read-only.
- Lotame: Spherical DCP / Data Buyer / Data Seller packaging; LDX (Lotame Data Exchange); Curated Marketplaces; Epsilon/Publicis ownership; "20 years" positioning.
- Permutive: cohort codes; on-device SDK membership computation; edge computing posture; contextual/affinity cohorts with NLP classification; workspaces; "100% addressability" claim; named integrations (GAM, Xandr, FreeWheel, Prebid, uid2, rampid).
- OnAudience: 25B+ devices / 200+ markets / 4,100 predefined segments (marketing figures); Curate; Raw Data; AI Audiences.

## Vendor-specific Findings

- Adobe is the only sampled product that explicitly self-defines the DMP category ("Three functions of a Data Management Platform") — its framing (Data In / Audience Creation / Data Out) is vendor framing, but it matches the cross-product structure and is therefore usable as corroborating evidence, not as the definition itself.
- Permutive inverts the classic identity model: instead of attaching data to user IDs, it attaches cohort codes to ad requests and computes membership on-device. This is the clearest documented evidence that the segment, not the user profile, is the DMP's load-bearing object.
- Lotame's repositioning from "DMP" to "data collaboration platform (DCP)" with marketer/agency/media-seller poles documents the category's current drift; its capability set remains the DMP capability set (onboarding, segmentation, enrichment, modeling, activation, insights).
- None of the sampled DMPs executes media buying or ad delivery; all name DSPs/ad servers as *destinations*. This supports holding "does not transact media" as part of the Type's boundary.
- OnAudience (and Adobe's Audience Marketplace seller role) show that audience *selling* is an ecosystem role adjacent to the DMP, not the DMP itself: a pure data provider has no operator-side segment management surface.

## Boundary Findings

- **vs Customer Data Platform / CDP**: the CDP's central object is the persistent individual profile of record (identified, first-party-led, accumulating history); the DMP's central object is the audience segment (targetable group, historically anonymous, open to third-party data). CDP activation is broad (messaging, personalization, analytics, warehouses); DMP activation is advertising-specific. Remove persistent individual profiles + broad activation → DMP. Market convergence is real: with third-party cookie deprecation, DMPs have repositioned toward first-party data and collaboration (Lotame → Spherical; Adobe ships AAM beside Real-Time CDP in the same suite). The CDP research pass already recorded this boundary from the other side.
- **vs Demand-side Platform / DSP**: the DSP executes media buying using audiences; the DMP builds, manages, and delivers audiences but never transacts media. The DSP is a *destination* of the DMP (Adobe destinations list; Permutive identity-based activations to DSPs; Lotame connections to DSPs). Remove audience management, add bidding/media buying → DSP.
- **vs Ad Server**: the ad server delivers ads and can hold simple targeting key-values; the DMP is the cross-system audience data layer that feeds it. The ad server is also a destination (Permutive ad-server activations; Adobe cookie/URL destinations). Add ad delivery/campaign serving → ad server.
- **vs Audience Management Platform (directory sibling leaf)**: genuine taxonomy tension. The DMP *is* the market's established audience-management platform for advertising; a separately-defined "Audience Management Platform" leaf risks being an alias of DMP (or a capability slice of it). Flagged for joint review in STATUS Boundary Issues. The CDP research pass independently flagged the same sibling.
- **vs third-party data provider / data marketplace (OnAudience-class)**: data providers sell predefined audience segments and raw data; the DMP is the operator-side platform where such data is acquired, combined with own data, and activated. A pure provider fails the "managed segment library" leg. Marketplace *features inside* a DMP (Adobe Audience Marketplace, Lotame LDX) are the DMP's acquisition machinery, not a separate Type.
- **vs Data Clean Room**: clean rooms match/join datasets between parties without moving data; the DMP aggregates and activates. Modern DMPs add clean-room-like collaboration (Lotame, Permutive) — variant structure, not core.
- **vs Tag Manager / client-side data collection**: tag managers collect data; the DMP turns collected data into managed, targetable segments with taxonomy, identity, and activation. Collection is the DMP's input leg, not its whole.
- **vs Marketing Automation Platform**: MA executes owned-channel campaigns over identified contact records; the DMP targets advertising media over mostly anonymous addressable identifiers. Different users, objects, and channels.

## Uncertainties

- Lotame's operational documentation was unreachable; all Lotame observations are Tier 2 (product pages). Operational claims about Lotame (how its segment builder, identity resolution, or syndication actually work) are held at reduced strength and excluded from the final document.
- Oracle BlueKai and Salesforce DMP (sunset classic DMPs) were not directly documented; the classic pattern is evidenced indirectly (Adobe's DMP framing; Permutive's "traditionally" description). The historical check therefore rests on two Tier 1 descriptions of the classic pattern, not on sunset-product docs.
- The market-size/decline narrative for the DMP category was not researched (no third-party market reports fetched). The contraction is *visible in the sample* (Lotame's repositioning; OnAudience positioning as a data provider; Adobe AAM documented as a mature/stable product) but is recorded as observation, not as a market claim.
- Adobe AAM's current strategic status within Adobe's portfolio (relative to Real-Time CDP) was not researched beyond what the docs show.
- Permutive's "100% addressability" and "milliseconds" claims are vendor performance claims; recorded as claims, not verified facts.

## Final Synthesis

The Data Management Platform is best understood as **the advertising-side audience data platform**: it collects audience data from multiple sources (the operator's own properties, partner data, purchased third-party data), organizes it into managed audience segments held in a curated taxonomy, and activates those segments into advertising/media systems for targeting.

The defining core is the jointly-held triple: **managed audience segment as unit of record + multi-source audience data aggregation + activation into advertising systems**. Everything else — trait/rule builders, lookalike modeling, identity graphs, marketplaces, destination catalogs, insights, consent machinery — is common mature structure; side-of-market packaging (advertiser/publisher/agency), monetization, contextual targeting, CTV/household handling, and clean-room collaboration are variant structure.

The Type's sharpest boundaries are against the **CDP** (segment-of-record vs profile-of-record; advertising activation vs broad activation), the **DSP** (manages audiences vs transacts media), and the **ad server** (audience data layer vs ad delivery). Its deepest current tension is era-driven: the classic cookie/third-party-data DMP vs the modern privacy-safe, first-party-led, cohort-based DMP. Both satisfy the same core; the identity substrate and data openness simply moved. A taxonomy tension with the directory sibling "Audience Management Platform" is recorded for joint review.
