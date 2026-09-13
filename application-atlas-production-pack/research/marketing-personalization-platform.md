# Research Notes — Marketing Personalization Platform

Research date: 2026-09-08

## Research Goal

Understand what a Marketing Personalization Platform is as an Application Type: what objects exist inside it, who operates it, how the audience→experience decision is made and executed, what rules govern it, and where the Type's boundary sits against neighboring Types — especially Recommendation / Personalization Engine (joint-review mandate from the 2026-09-07 pass), A/B Testing Platform, CDP, Marketing Automation Platform, CMS, and consumer-facing personalized surfaces.

## Initial Boundary

Working hypothesis at start:

- The leaf sits in Directory section 06 (Marketing, Advertising & Growth), so the Type is a **B2B marketing technology**, not a consumer-facing product.
- Core purpose hypothesis: given marketer-defined visitor segments and prepared experience variations, decide at runtime — per incoming visitor — which variation to serve in the brand's owned digital channels (site, app, email), and measure the impact.
- Prior passes constrain the seam:
  - `recommendation-personalization-engine` (2026-09-07): "the recommendation engine's managed object is the ranked item decision... while the marketing personalization platform's managed object is the audience-experience decision (which content/experience variation per segment)"; products straddle heavily (Adobe Target ships both); joint review recommended.
  - `a-b-testing-platform` (2026-09-07): "Same delivery machinery (who sees which experience), different assignment logic: personalization assigns deterministically by segment rule; A/B testing assigns randomly to compare."
  - `customer-data-platform-cdp` (2026-09-07): CDPs expose "edge personalization destinations" (Adobe Target named); BlueConic-class CDPs drift toward personalization/execution territory.
- Likely confusions: A/B Testing Platform, CDP, Marketing Automation Platform, CMS, Recommendation / Personalization Engine, Conversion Rate Optimization Platform, Personalized Content Feed (§02.08, consumer surface), Web Experience Design (§04.16, authoring tools).

## Research Questions

1. What are the core objects? (audience/segment, experience/variation, campaign/activity container, decision rule, placement/page, metric)
2. How does an operator define targeting? (segment criteria, data sources, reusable libraries)
3. How are variations created? (visual editor, code, templates, dynamic content)
4. How is the audience→experience binding executed at runtime? (client-side, server-side, on-device; priority resolution; ML decisioning)
5. How do measurement and experimentation relate to personalization? (holdback, goals, bandits, experimentation-in-personalization)
6. What lifecycle and governance exist? (draft/preview/live/ended, permissions, multi-brand)
7. What data flows in and out? (behavioral events, first-party datasets, CDP segments)
8. Where is the boundary vs Recommendation Engine, A/B Testing, CDP, MA, CMS?
9. What varies by segment (retail vs B2B vs media) and delivery posture?
10. Historical check: would older/regional/platform-native personalization satisfy the definition?

## Representative Products

Selected for market representativeness, documentation quality, and spread of product philosophy and customer level:

| Product | Pole | Why selected |
|---|---|---|
| Adobe Target | enterprise experience cloud suite; the documented straddle anchor (ships recommendations + experience targeting + automated personalization) | deep Tier 1 docs; boundary anchor vs A/B testing and vs Recommendation Engine |
| Optimizely (Personalization) | pure-play experimentation vendor's separate personalization product; engineering-leaning | documents campaign object model (pages/events/tags/audiences/experiences/holdback) in depth |
| VWO (Personalize) | mid-market CRO suite pillar | documents data-layer targeting, layered experiences, assignment resolution (priority/random/weightage) |
| Monetate (Kibo) | commerce-attached pure-play personalization engine | documents the WHO/WHAT/WHEN/WHY/HOW experience sentence, experience types, omnichannel, first-party data onboarding |

Rejected / unreachable:

- **Dynamic Yield** — intended as the pure-play personalization-platform pole. help.dynamicyield.com transport error again on 2026-09-08 (same failure as 2026-09-07 pass). Abandoned per network rule. No claims made about Dynamic Yield.
- Bloomreach — unreachable in the prior pass; not retried. No claims made.

## Sources

All fetched 2026-09-08. Tier 1 = official product documentation; Tier 2 = official product pages.

**Adobe Target (Tier 1)**
- Introduction to Target — https://experienceleague.adobe.com/en/docs/target/using/introduction/intro
- Activities overview — https://experienceleague.adobe.com/en/docs/target/using/activities/activities
- Experience Targeting (XT) — https://experienceleague.adobe.com/en/docs/target/using/activities/experience-targeting/experience-target
- Create audiences — https://experienceleague.adobe.com/en/docs/target/using/audiences/create-audiences/audiences

**Optimizely (Tier 1)**
- Optimizely Personalization overview — https://support.optimizely.com/hc/en-us/articles/27294865902733-Optimizely-Personalization-overview
- Core concepts of Optimizely Personalization — https://support.optimizely.com/hc/en-us/articles/27733776221453-Core-concepts-of-Optimizely-Personalization
- Web Experimentation docs index / Customer Behavior (developer docs) — https://docs.developers.optimizely.com/web-experimentation/docs , https://docs.developers.optimizely.com/web-experimentation/docs/customer-behavior.md

**VWO (Tier 2)**
- VWO Personalize product page — https://vwo.com/personalization/

**Monetate (Tier 1)**
- Monetate Knowledge Base index — https://docs.monetate.com/docs
- Monetate Experiences Overview — https://docs.monetate.com/docs/monetate-experiences-overview

## Product Observations

Evidence layer A = directly observed in that product's official docs/pages. Layer B = cross-product commonality.

### Adobe Target — enterprise suite pole (Layer A)

- **Positioning**: "comprehensive tools to personalize customer experiences across web, mobile sites, apps, social media, and other digital channels." Licensed as Standard/Premium.
- **Activity** = the container unit. Types: A/B Test, Auto-Allocate, Auto-Target, Multivariate Test, **Experience Targeting (XT)**, **Automated Personalization (AP)**, Recommendations.
  - XT: "delivers content to a specific audience based on a set of marketer-defined rules and criteria... When visitors view your site, XT evaluates those visitors to determine whether they meet the criteria you set. If they meet the criteria, they enter the activity and the experience designed for qualifying audiences displays. You can create experiences for multiple audiences within a single activity." Experiences are ordered; ordering determines delivery.
  - XT framed as the bridge from testing to personalization: "Experience Targeting is a first step into the world of personalization and often begins with A/B testing... switch to long-term targeting of content to those different user segments."
  - AP: "combines offers or messages, and uses advanced machine learning to match different variations to each visitor based on their individual customer profile."
  - Auto-Target: ML "serves the most tailored experience to each visitor based on the individual customer's profile and the behavior of previous visitors with similar profiles."
- **Audiences**: "determine who sees content and experiences in a targeted activity." Reusable Audiences list + activity-only audiences + combining multiple audiences into ad hoc audiences. Two uses: **targeting audiences** (deliver different content to different visitor types) vs **reporting audiences** (analyze how visitor types respond to same content). Sources: Target, API, Experience Cloud, Adobe Experience Platform (RTCDP). Predefined audiences (New Visitors, Returning Visitors). Custom profile parameters targetable. Audience usage tracking (which live/inactive/archived activities reference an audience).
- **Composers**: Visual Experience Composer (edit pages without code) and Form-Based composer.
- **Runtime**: decisioning method filter — Server-Side vs Client-Side (on-device decisioning).
- **Lifecycle**: Live / Scheduled / Inactive / Ended / Archived; activate/deactivate/copy/delete/archive; reactivation restores prior visitors to the activity.
- **Conflict resolution**: Priority — "if multiple activities are assigned to the same location with the same audience, the activity with the highest priority displays" (legacy Low/Medium/High or fine-grained 0–999).
- **Measurement**: success metrics (Conversion, Revenue, Engagement); reporting source Target or Analytics (A4T); Estimated Lift in Revenue column.
- **Channels**: "Web and mobile sites; Internet-connected screens and devices, including kiosks and ATMs; Email and other acquisition channels or partner sites; Mobile apps; Anywhere else you can deliver tagged content."
- **Governance**: Enterprise User Permissions — properties, product profiles, roles restricting view/edit/approve/publish by region/environment/channel.
- **Straddle**: Recommendations activities + "Recommendations as an offer" inside A/B/Auto-Allocate/Auto-Target/XT activities.
- Numeric limits exist (e.g., 350 offers per experience, 50 audiences/locations) — L3, not promoted.

### Optimizely Personalization — pure-play experimentation vendor pole (Layer A)

- **Positioning**: "deliver targeted experiences in real time to different visitors based on their behaviors." Abilities: "Create and manage audiences based on data from multiple sources. Build personalized web experiences with a visual editor. Target audiences in real time. Measure the impact of personalization efforts."
- **Object model** (Core concepts page):
  - **Pages** — "sections of your site where you modify the experience and track behavior" (single URL, URL pattern, global URL). "Pages are always on" — constant behavior data gathering regardless of campaigns.
  - **Events and metrics** — click/pageview/custom events; "always on"; feed both behavioral audiences and measurement. Example audience: "people who searched more than two times in the last 30 days."
  - **Tags** — page context (Price, Category, Name); enable targeting like "customers who spent more than $100."
  - **Audiences** — "groups of customers to whom you deliver a targeted experience... a group of visitors with something in common." Behaviorally built (Heavy Spenders, Shoe Shoppers, Abandoned Cart).
  - **Experiences** — created in the Visual Editor "based on the page they visit and the audiences they qualify for."
  - **Personalization campaigns** — "the framework to organize your personalization strategy": name, pages, audiences, primary metric, holdback. "A campaign takes a piece of your site... and shows content for different audiences." Multiple campaigns per page; one campaign can span pages.
- **Conflict resolution**: "If a visitor belongs to multiple audiences, they only see one experience... Visitors see the highest priority experience for which they qualify."
- **Holdback**: "the control group of an A/B test. By default, Optimizely Personalization shows a personalized experience to 95% of campaign visitors and holds back 5% who see the original" — measures the lift of personalization vs the generic experience. Changing holdback mid-campaign invalidates stats.
- **Experimentation-in-Personalization**: A/B test personalized experiences; "test how you segment" (segmentation schemes themselves testable).
- **Bandits**: multi-armed bandit / contextual bandits for experience selection (merchandising use case).
- **CDP integration**: real-time segments from Optimizely Data Platform (ODP); CDP audience sync from third-party CDPs.
- **Use cases documented**: behavioral targeting, symmetric messaging (match site experience to ad/email campaigns), category affinity, loyalty promotion, CMS personalization where the CMS lacks it, quick website changes.
- Developer side: behavioral queries (JSON), Dynamic Customer Profiles (DCP), list attributes (target users in externally defined audiences).

### VWO Personalize — mid-market suite pillar (Tier 2, Layer A at page level)

- **Positioning**: "deliver 1000s of such unique journeys to the right audience, at the right place, and at the right time."
- **Data layer**: "browser-based properties, website engagement or browsing behavior data, uploaded attribute lists, and third-party data (both native and API-based)"; integrations with analytics, CMS, CDP, ABM platforms; "single view of unified customer data"; ML enrichment ("predictive insights").
- **Targeting**: "rule-based audience segments on top of" the data layer; triggers (page refresh, scroll depth, time on page); buyer-journey-stage experiences.
- **Assignment resolution for overlapping segments**: layered experiences with fall-backs per micro-segment; choose **By Priority** ("the order they are listed among the qualified experiences"), **By Random Selection**, or **By Weightage** (weightage marked "coming soon" on the page).
- **Variation creation**: WYSIWYG Visual Editor, Widget Library (pop-ups, countdowns, sticky promos), Code Editor for custom JS; dynamic text in content.
- **Measurement**: conversions per campaign, impact "across segments and dimensions," real-time reports, traffic split, platform-level metrics architecture.
- **Suite framing**: Testing, Behavior Analytics, Personalization, Web Rollouts, Customer Data Platform, Program Management as sibling pillars.

### Monetate (Kibo) — commerce-attached pure-play engine (Layer A)

- **Experience sentence structure** (documented pedagogy): "Monetate's sentence-based experience structure allows you to create and manage any personalized experience in the platform. It consists of four parts: WHO, WHAT, WHEN, and WHY." Automated Personalization adds a fifth — HOW (Engine Context).
  - **WHO — Audience Targets**: "Segment customers by marketing referral channels, new versus returning visitors, location, behavioral interactions, device information, weather, and more... import any first-party data from CRM tools, point-of-sale (POS) systems, or business intelligence (BI) platforms." Target Builder; named segments; cross-device behavioral targets; datasets targets; disjoint group targets; on-site search-terms targets; travel targets.
  - **WHAT — Site Changes**: "inserting, editing, or hiding any content of your site... lightboxes, or countdown timers; full-page and customer journey changes; product recommendations; and editing functional aspects of the site"; WYSIWYG Action Builder for business users; advanced users deploy JS/CSS/HTML.
  - **WHEN — Campaign Timing**: "Fixed start/stop times and dayparting... flash sales, call center availability."
  - **WHY — Experience Purpose**: "any experience is evaluated against any business KPI. Monetate offers a range of testing strategies: full-page tests, A/B and A/B/n tests, multivariate tests, and tests with dynamic auto-optimized traffic allocation."
  - **HOW — Context**: Engine Context variables (e.g., device type) used "when it makes one-to-one decisions."
- **Experience types**: 100% Experiences ("shows every site visitor in your defined audience the same experience"), Standard Test (fixed traffic distribution), Dynamic Testing (engine auto-exploits the winning variant), Automated Personalization ("leverage machine learning and your data to serve the most appropriate variant to each and every customer automatically... true one-to-one personalization").
- **Experience management**: statuses, priority, preview/QA, change history, duplication, markets (account-level segmentation for multi-site/multi-brand), stealth groups (excluding internal/bot traffic from samples).
- **Data**: customer attributes datasets (SFTP/API uploads), ID collectors + customer view (cross-device identity), product catalog datasets, offline purchases datasets; consumer data privacy APIs.
- **Omnichannel experiences**: web + other channels (email etc.) from one experience definition.
- **Audience tooling**: Audience Explorer (define audiences), Audience Discovery (auto-discovered audiences), AdLink.
- **Straddle**: Product Recommendations (strategies, slotted recs, email recs), Personalized Search, Dynamic Bundles, Product Finder, Social Proof, Product Badging — a full recommendation/merchandising layer beside the experience layer.
- **Strategy taxonomy** (training): Agility / Optimization / Segmentation / Personalization experiences.

## Cross-product Comparison

| Dimension | Adobe Target | Optimizely Personalization | VWO Personalize | Monetate |
|---|---|---|---|---|
| Container unit | Activity (XT / AP / Auto-Target / A-B / MVT) | Campaign | Experience campaign | Experience (WHO/WHAT/WHEN/WHY[/HOW]) |
| Audience concept | Audiences (reusable library, activity-only, combinable; targeting vs reporting uses) | Audiences (behavioral, from always-on events/tags; ODP real-time segments) | Rule-based segments over a unified data layer (browser, behavior, uploaded lists, third-party) | WHO targets (behavioral, referral, location, device, weather; imported CRM/POS/BI data; named segments) |
| Variation concept | Experiences per audience (VEC / form composer) | Experiences (Visual Editor) | Experiences (Visual Editor / widgets / code) | Actions (insert/edit/hide content, lightbox, countdown, recs) + variants |
| Assignment logic | Rule-based per audience (XT); ML per visitor profile (AP, Auto-Target) | Rule-based per audience; priority wins; holdback %; bandit modes | Priority / random / weightage among qualified experiences | 100% / fixed-split test / auto-optimized / ML one-to-one; experience priority |
| Runtime locus | Server-side or client-side (on-device) decisioning | Real-time in browser (snippet) | Real-time triggers in browser | Real-time session decisioning |
| Conflict resolution | Activity priority at same location+audience | Audience priority ordering | Priority / random / weightage | Experience priority |
| Measurement | Success metrics (conversion/revenue/engagement); Target or Analytics reporting; estimated lift | Primary metric + holdback control group | Goals, real-time reports, traffic split, segment dimensions | WHY metrics; experience results; statistical confidence; holdouts in AP |
| Data in | Profile params, AEP/RTCDP audiences, Analytics | Always-on events/tags; ODP; CDP sync; list attributes | Data layer, uploaded lists, third-party integrations | Customer datasets (CRM/POS/BI), ID sync, catalog, behavioral events |
| Channels | Web, mobile sites, apps, email, kiosks/ATMs | Web (CMS) | Web | Web + omnichannel (email etc.) |
| Experimentation | Native activity types (A/B, MVT, Auto-Allocate) | Experimentation-in-Personalization; bandits | Sibling Testing pillar | WHY layer: A/B, MVT, dynamic testing |
| Recommendation capability | Recommendations activities + recs as offer | (not in this product line) | (not observed at page level) | Product Recommendations / Personalized Search / Dynamic Bundles modules |

Layer B findings (cross-product commonality):

1. Every product separates **who the visitor is** (audience/segment/target) from **what they see** (experience/variation/action), bound inside a **container** (activity / campaign / experience). (B)
2. Every product resolves **overlapping qualifications** with an explicit precedence mechanism (activity priority, audience priority, experience priority/order). (B)
3. Every product maintains a **visitor-conditioning data layer**: behavioral events, attributes, context, plus imported first-party/third-party data. (B)
4. Every product offers a **visual no-code editor** for variations plus a code path for advanced users. (B)
5. Every product **measures** personalization against goals/metrics, with a control mechanism (holdback/holdout) or testing strategies to attribute impact. (B)
6. Every product runs the decision **at delivery time, per visitor** (real-time targeting / session decisioning / on-device or server-side decisioning). (B)
7. Two decision modes recur: **rule-based** (marketer-defined audience→experience rules) and **model-based** (ML/bandit picks the variant per visitor profile) — Target AP/Auto-Target, Optimizely bandits, Monetate AP/Dynamic Testing. (B)
8. Lifecycle machinery recurs: draft/preview/QA → scheduled → live → ended/archived, with change history. (B)
9. CDP/data integration recurs as the data-in relationship (AEP/RTCDP, ODP, AgilOne, generic CDP syncs). (B)
10. Delivery beyond the web page recurs (email, mobile apps, kiosks/ATMs, omnichannel experiences). (B)

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as this Type:

```text
Visitor-conditioning basis (marketer-defined segments and/or individual visitor profiles)
  + Prepared experience variations for the brand's owned digital channels
  → Runtime per-visitor decision binding the visitor's condition to one variation
  → Impact measurement of the served variations
```

Four properties:

1. **Visitor-conditioning basis** — a maintained, marketer-defined basis for telling visitors apart: segments (attribute/behavior/context rules) and/or individual visitor profiles. Without it there is no targeting basis and the product collapses into plain site editing or randomized testing.
2. **Prepared experience variations** — alternative content/experience variants (page variations, content blocks, offers, messages) authored for delivery in owned digital channels. Without them there is nothing to personalize.
3. **Runtime per-visitor decision** — the binding of conditions to variations, evaluated for each incoming visitor at delivery time (rule-evaluated or model-chosen), rendering the matched variation. The assignment basis is who the visitor is — not chance. (Randomization appears only as a measurement overlay — the holdback — not as the assignment logic.) Without runtime decisioning it is a targeting plan, not a platform.
4. **Impact measurement** — the served variations are evaluated against goals/metrics so the marketer can see what personalization achieved. Without it the product is a content-switching utility, not a marketing platform.

Jointly-held is load-bearing: conditioning without variations = audience tooling; variations without conditioning = site editing; conditioning + variations without runtime decision = campaign planning document; all without measurement = content-switching utility.

§24 historical check: early-2000s rule-based web personalization (visitor profile + segment rules + server-side per-request content substitution) satisfies all four properties with no visual editor, no ML, no CDP, no holdback. Segment-conditioned direct-mail variants (different catalog covers per segment, executed at delivery) satisfy the core without software. Email merge-field substitution alone does NOT (no audience→variation decision — per-record field fill only). Therefore none of the modern structures (visual editor, ML decisioning, holdback defaults, CDP sync, omnichannel) belong in the defining core.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required for recognition:

- Visual (WYSIWYG) editor for variations + code editor/HTML/CSS/JS path
- Reusable audience library + ad hoc audience combining + audience usage tracking
- Always-on behavioral event collection feeding both targeting and measurement
- Precedence resolution for overlapping qualifications (priority ordering)
- Per-campaign/experience results with goals/metrics and statistical machinery
- Holdback/control group measuring aggregate personalization lift
- Lifecycle: draft/preview/QA → scheduled → live → ended/archived; change history
- URL/page targeting (single URL, pattern, global/site-wide)
- First-party data ingestion (CRM/POS/BI datasets, uploaded lists) + CDP integrations
- Multi-page/multi-campaign coordination on one site
- Experimentation machinery bundled (A/B, MVT, auto-optimization)
- ML decisioning mode (automated personalization / dynamic optimization / bandits)
- Governance: user roles/permissions, properties/workspaces, approval
- Cross-channel delivery (email, mobile apps, kiosks) / omnichannel experiences

### L2 — Variant / Optional Structure

- Delivery posture: standalone personalization product vs suite pillar (testing/analytics/CDP suite) vs commerce-suite module
- Decisioning locus: client-side snippet vs server-side vs on-device/edge
- Recommendation/merchandising modules inside the platform (the straddle zone with Recommendation / Personalization Engine)
- Industry packaging: retail/commerce vs B2B (firmographic targets, ABM integrations) vs media vs e-learning
- Privacy machinery: consent surfaces, consumer data privacy APIs, internal-traffic exclusion (stealth groups)
- Account segmentation: markets/multi-site/multi-brand
- Third-party signal targets (weather, travel, live session signals)
- AI assistants / agentic campaign building (era-current)
- Audience discovery (auto-surfaced segments) vs marketer-defined only

### L3 — Vendor-specific Structure

(kept out of the final document; examples)

- Adobe Target: activity-type taxonomy (XT/AP/Auto-Target/Auto-Allocate), Standard vs Premium licensing, VEC/form composers, A4T reporting, numeric limits (350 offers/experience, 50 audiences/locations), priority scales (0–999)
- Optimizely: holdback default (95/5), ODP/DCP naming, contextual bandits, Experimentation-in-Personalization, list attributes
- VWO: priority/random/weightage assignment triad, Wandz/AdaptiveCX AI layer, widget library
- Monetate: WHO/WHAT/WHEN/WHY/HOW sentence pedagogy, experience-type names (100%, Standard Test, Dynamic Testing, Automated Personalization), Engine Context, Markets, Stealth Mode, MONET AI

## Vendor-specific Findings

- Target's **activity-type taxonomy** (separating XT from AP from Auto-Target) is product-specific packaging of the general rule-based vs model-based decision modes.
- Optimizely's **holdback default (95/5)** and its "test how you segment" framing are product-specific articulations of the general measurement overlay.
- VWO's **random/weightage assignment options** (alongside priority) are product-specific; other products resolve overlaps by priority only.
- Monetate's **experience sentence (WHO/WHAT/WHEN/WHY/HOW)** is a documented pedagogical frame unique to this vendor, but it maps cleanly onto the cross-product object set — useful as evidence that the object model is real, not as canonical terminology.
- Monetate's **Markets** (account-level segmentation) and **Stealth Mode** (internal-traffic exclusion) are product-specific implementations of multi-brand governance and sample hygiene.

## Boundary Findings

1. **vs Recommendation / Personalization Engine (joint-review mandate — resolved from this side).** The recommendation engine's managed object is the **ranked item decision** (which items, in what order, for which request context, computed from behavioral signals). This Type's managed object is the **audience-experience decision** (which experience variation for which visitor condition). Both passes confirm the split; both also confirm a real straddle zone: Target ships Recommendations activities and embeds recommendations as offers inside XT/AP activities; Monetate ships Product Recommendations/Personalized Search/Dynamic Bundles beside its experience layer. **Resolution: keep both Types, split by managed object, with the straddle zone documented.** Test: primary output = ranked item list computed from behavioral signals → Recommendation / Personalization Engine; primary output = audience-conditioned experience variation → Marketing Personalization Platform. When a recommendation is embedded as one variation inside an audience-conditioned experience, the personalization platform is the container and the engine is the content source. The leaf name "Recommendation / Personalization Engine" maps to the item-conditioned pole; "Marketing Personalization Platform" to the audience-conditioned pole.
2. **vs A/B Testing Platform.** Same delivery machinery (who sees which experience), different assignment logic: personalization assigns by visitor condition (rule or model); A/B testing assigns randomly to compare. Products bundle both (Target activity types; Optimizely Experimentation-in-Personalization; VWO Testing pillar; Monetate WHY layer). Randomization as measurement overlay (holdback) does not turn personalization into testing. Test: replace the assignment basis — rule/model-conditioned → this Type; randomized-for-comparison → A/B Testing Platform.
3. **vs Customer Data Platform.** CDP aggregates/identifies customer data and exports profiles/segments; this Type consumes them for in-experience decisions. Documented from both sides: CDP pass recorded "edge personalization destinations" (Adobe Target named in Tealium docs); this pass recorded CDP-segment consumption (Optimizely ODP real-time segments, VWO CDP integrations, Monetate AgilOne/first-party datasets). Distinct Types; BlueConic-class execution drift noted in the CDP pass.
4. **vs Marketing Automation Platform.** MA's core (per the 2026-09-08 pass) is the marketing person database + reusable automated program + per-contact program execution state — outbound journeys over known contacts. This Type decides in-experience, at delivery time, for anonymous and known visitors on owned digital properties. MA dynamic content (per-contact content selection inside outbound sends) is the nearest MA capability; the seam is the decision locus (inside an outbound program vs inside the live experience) and the audience substrate (contact database vs visitor conditioning layer). Distinct Types.
5. **vs CMS.** CMS stores/manages/renders content; this Type decides which variant per visitor at runtime. Optimizely explicitly positions personalization for CMSs "that do not support personalization." Some CMSs have native personalization features — those are capabilities inside another Type, not this Type.
6. **vs Conversion Rate Optimization Platform.** Practice-framed superset (testing + personalization + behavior analytics + program management) — same resolution as the A/B testing pass; vendors market the same product under both labels. Flag stands from that pass.
7. **vs Personalized Content Feed (§02.08) / Personalized News Feed (§02.04) / Product Discovery Application (§05.05).** Consumer-facing surfaces; this Type is the B2B decision layer behind such surfaces. Test: who logs in — an end consumer (surface) or a marketer/operator (platform).
8. **vs Web Experience Design (§04.16).** Design/authoring tools produce the experience assets; this Type decides and serves them at runtime. Distinct Types.
9. **vs Ad Server / DSP.** This Type personalizes the brand's owned channels; ad serving decides paid placements in earned/bought inventory. Distinct delivery surfaces and decision economics.

## Uncertainties

- The pure-play personalization-platform pole (Dynamic Yield) could not be sampled in either pass (transport errors). The pure-play shape is evidenced via Monetate (commerce-attached) and Optimizely (experimentation-attached); claims about the standalone pure-play pole are kept generic.
- VWO evidence is Tier 2 (product page) for this pass; its help-center articles were not fetched. VWO's suite framing is corroborated by the A/B testing pass's Tier 1 sources.
- Whether the market category "personalization platform" always includes recommendation capability was not verified against analyst sources; the Type is defined from product behavior, not analyst taxonomy.
- Email/off-site delivery depth varies by product (Target and Monetate document it; Optimizely/VWO pages emphasize web); held as L1 common with variance, not definitional.
- Numeric limits and defaults (Target's activity limits, Optimizely's 95/5 holdback) are recorded as L3 and excluded from the final document.

## Final Synthesis

A Marketing Personalization Platform is a marketer-side system whose defining core is: a visitor-conditioning basis (marketer-defined segments and/or individual visitor profiles) + prepared experience variations for owned digital channels → a runtime per-visitor decision binding condition to variation (rule-evaluated or model-chosen) → impact measurement of the served variations. Around that core, mature products add a standard structure: visual editors, reusable audience libraries, always-on behavioral collection, precedence resolution, holdback-based measurement, lifecycle/governance machinery, first-party/CDP data ingestion, experimentation modes, ML decisioning modes, and cross-channel delivery. The Type's variants are dominated by delivery posture (standalone vs suite pillar vs commerce module) and decisioning locus (client/server/on-device). The sharpest boundary — resolved jointly with the prior pass — is against the Recommendation / Personalization Engine (audience-experience decision vs ranked-item decision, with a documented straddle zone); other boundaries (A/B testing, CDP, MA, CMS, consumer surfaces, design tools, ad serving) are clean and documented from product evidence.
