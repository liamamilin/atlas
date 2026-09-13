# Research Notes — Ad Server

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1
Cross-reference: research/ad-delivery-platform.md (sibling leaf, processed earlier the same day; its Boundary Findings flagged a probable alias with this leaf and deferred the joint review to this document)

## Research Goal

Understand what an "Ad Server" is as an Application Type — the market-canonical name under which the request-time ad execution engine is sold and self-described. Determine: the core objects (demand side, supply side, the request-time decision), the delivery loop, the competition and pacing rules, the users, the historical breadth of the definition, and the boundaries against neighboring advertising-stack Types (DSP, SSP, Programmatic Advertising Platform, Advertising Campaign Management, Creative Management Platform, Recommendation/Personalization Engine). Additionally: complete the joint review requested by the Ad Delivery Platform research regarding whether "Ad Delivery Platform" is a distinct Type or an alias of "Ad Server".

## Initial Boundary (pre-research hypothesis)

- Hypothesis: an Ad Server is the system that holds ad campaigns and, for every ad request arriving from a delivery surface (tag, SDK, API), selects and returns the ad to render under targeting/competition/pacing rules, recording each delivery for reporting and billing.
- Likely confusions:
  1. **Ad Delivery Platform** (sibling leaf) — already flagged as probable alias by its own research; every sampled product in that research self-identified as an "ad server".
  2. **DSP** — also "delivers ads" but via bidding in external auctions.
  3. **SSP** — also publisher-side, but focused on selling machinery, not request-time selection.
  4. **Advertising Campaign Management** — planning layer.
  5. **Creative Management Platform / DCO** — produce/adapt creatives; do not decide what renders.
  6. **Recommendation / Personalization Engine** — per-request selection from a candidate pool, but organic content.
  7. **CDN / creative hosting** — transport only.
- Unknowns: whether any market actor uses "ad delivery platform" as a primary category name (test the alias finding); whether advertiser-side ad serving changes the structure; whether Google Ad Manager (dominant publisher ad server) exposes any structure that breaks the model.

## Research Questions

1. What do products that the market calls "ad servers" actually call themselves, and what do they claim to do?
2. What are the core demand-side objects and how do they nest?
3. What are the core supply-side objects and how do they nest?
4. What exactly happens between an ad request and a rendered ad?
5. How is competition among eligible ads resolved (priority tiers / waterfall vs weights vs auction), and are these alternatives or layers?
6. How do goals, budgets, pacing, caps, and reservation govern delivery over time?
7. Which targeting dimensions exist and at which object do they attach?
8. What happens when no ad qualifies (house ads, default ads, programmatic backfill)?
9. How are delivery events recorded, and how do they feed reporting and billing?
10. What integration surfaces exist (client tags, SDKs, server-to-server decision APIs, video templates)?
11. Who operates the system (ad ops, yield managers, advertisers, publishers, developers)?
12. Is the ad server inherently publisher-side, or does the advertiser-side form have the same structure?
13. Does the historical, self-hosted, tag-and-banner-era ad server still fit the definition (historical/market-sample check)?
14. Does any product primarily self-identify as an "ad delivery platform" rather than an ad server?
15. Where exactly do the boundaries run against DSP, SSP, campaign management, creative management, personalization, and CDN?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy / segment | Role in sample |
|---|---|---|
| Kevel (ex-Adzerk) | API-first ad server; "build your own ad platform"; retail media / sponsored listings | developer-centric, embedded-delivery philosophy |
| Microsoft Monetize (Xandr) | enterprise end-to-end suite: explicit "Ad server" role plus SSP and buying platform | enterprise, full-stack, both sides |
| AdButler | independent multi-channel ad server with self-serve/white-label portals | SMB/mid-market publishers and commerce media, UI-first |
| Revive Adserver | free open-source self-hosted ad server (phpAdsNew → Openads/OpenX lineage) | historical/era check + self-hosted variant |

Supplementary anchors (weaker evidence):

- **Equativ** (ex-Smart AdServer) — global end-to-end media platform; homepage nav positions "CTV Ad Server" and "Monetization / SSP" as distinct publisher-solution lines (Tier 2 positioning only; product docs returned 404). Supports: (a) "ad server" remains the product-line name at enterprise platforms, (b) ad server and SSP are named as distinct lines within one suite.
- **Google Ad Manager** — dominant publisher ad server; unreachable (see Sources). Retained as a market anchor with zero product-specific claims.

## Sources

### Kevel (Tier 1 — official developer docs, fetched 2026-09-06)

- Introduction to Kevel: https://dev.kevel.com/docs/understanding-kevel.md
- Ad Decision Engine Overview: https://dev.kevel.com/docs/delivery-basics.md
- (Documentation index https://dev.kevel.com/llms.txt additionally confirms: Priorities, Flights, Decision/Management/Reporting APIs, Forecast, Console, UserDB, targeting pages, tracking/data-shipping, retail media, RTB/Relay, header bidding)

### Microsoft Monetize / Xandr (Tier 1 — official product docs on Microsoft Learn, fetched 2026-09-06)

- About Monetize: https://learn.microsoft.com/en-us/xandr/monetize/about-monetize
- Object Hierarchy: https://learn.microsoft.com/en-us/xandr/monetize/object-hierarchy
- Hub: https://learn.microsoft.com/en-us/xandr/

### AdButler (Tier 1 — official help center, fetched 2026-09-06)

- How AdButler serves ads: https://www.adbutler.com/help/article/how-adbutler-serves-ads
- Help center (confirms related articles: What is AdButler?, Requests vs. impressions, Glossary, AdButler's CDN): https://www.adbutler.com/help
- Product site (positioning; see also prior sibling research for fetched glossary/quick-start detail): https://www.adbutler.com/

### Revive Adserver (Tier 1/2 — official repository README via GitHub; site previously returned 403, fetched 2026-09-06)

- Repository README: https://github.com/revive-adserver/revive-adserver
- README confirms: hosted edition at revive-adserver.net; GeoLite2 geotargeting plugin; era artifacts `phpadsnew.inc.php`, `adview.php`, `adclick.php`, `adframe.php`, `adjs.php`, `adx.js` in repo root

### Equativ (Tier 2 — positioning page only, fetched 2026-09-06)

- Homepage: https://equativ.com/ — nav/footer lists publisher solutions "Monetization / SSP", "CTV Ad Server", "Retail Media"; advertiser platform; agentic suite
- Deeper docs unreachable: https://docs.equativ.com/ (transport error), https://equativ.com/en/solutions-for-publishers (404) — abandoned after 2 attempts

### Unreachable

- Google Ad Manager: https://support.google.com/admanager/answer/177901 (timeout ×2 today, cumulative ×4 across both sibling and this research), https://developers.google.com/ad-manager (timeout) — abandoned per network-restriction rule. No GAM-specific claim is made anywhere in this research.
- Broadstreet: name collision — broadstreet.net is a South Carolina web-consulting firm, not the ad server product; not pursued further.

## Product Observations

### Kevel — Key observations (Evidence layer A)

**Self-description.** "Kevel is a set of APIs that lets customers build a unified ad platform supporting any ad format, any creative, and the management of multiple demand sources." And directly: "Kevel is a **fully featured ad server** that can serve any creative and any ad format, including standard IAB ads, video ads, DOOH, audio ads, sponsored listings, native ads, and any other digital asset that requires a serving decision."

**Server-to-server posture.** The customer's server handles the ad response and renders; "not constrained by client-side ad code written for specific ad formats". "Most ad servers function this way [client-side] and are built for a limited set of ad formats" — vendor's own framing of the category contrast.

**Demand hierarchy.** Advertisers → Campaigns → Flights → Ads → Creatives. Flight = "a collection of ads grouped under a campaign"; most targeting and delivery rules live at flight level (goals, dates, targeting, tracking).

**Decision engine.** Inputs: creative size; targeting/goal settings on Ad/Flight/Campaign; the Channel's Priority for the flight. Process: Decision API request arrives (placement location, user agent, keywords, user key, custom targeting data, location) → engine filters all ads by criteria → walks priorities in order (example given: Sponsorship, then Auction, then House) → selects a winner by the priority's selection method.

**Selection methods.** **Lottery** (default): proportional to weights ("an ad with a weight of 50 would have 50 balls in the bowl"); **Auction**: highest eCPM wins. A **balancer** recomputes creative weights every 5 minutes or on save; percentage-goal flights get static weights; goal-based flights get dynamic weights from projected vs actual delivery. Percentages-goal ads in a lottery priority are eligible first; remaining requests fill from other goal types.

**Priorities.** Numbered precedence per Channel (example defaults: Sponsorship 1, Premium 5, House 20); unfilled impressions cascade down the waterfall; "House Ads only appear if there's no advertiser to fill the slot".

**Goals & caps.** Goal types: impressions, percentage, click, conversion, revenue, daily/monthly revenue; engine throttles delivery to hit the goal by the end date. Caps are hard limits that pause the flight; the vendor explicitly documents slight overserve at high event rates ("stopping on a dime is not feasible").

**Supply hierarchy.** Network → Channels → Sites → Zones; ad codes/zone tags trigger ad requests; VAST ad code for video.

**Around the loop.** Impression/click/conversion/custom-event logs; data shipping of log-level events to external stores; availability/deliverable forecasting; RTB programmatic fill ("Relay"), demand partners, header bidding; retail media objects (Catalog, sponsored listings/brands, Console self-serve UI with user/permission management, SSO, audit log).

### Microsoft Monetize (Xandr) — Key observations (Evidence layer A)

**Self-description and ad server role.** "Microsoft Monetize is a web-based application for your programmatic advertising." "Instead of operating an ad server and a buying platform, Monetize can perform both functions." Explicit role: "**Ad server** — As an ad server user, you have access to your end-to-end setup of advertiser and publisher information. You can set up publishers and available inventory, as well as advertisers and their selling specifications. With an ad server, you can set up and manage your buy-side systems and your sell-side systems, as well as manage forecasting, priorities, and many other types of functionality between the two."

**Process flow.** Ad calls received from supply partners (client-side tag or server-side) → segment data overlaid from server-side cookie store → bid requests to bidders (milliseconds) → bidder processes campaigns/targeting/bidding → impression bus evaluates bids and publisher preferences → winning ad served (directly if client-side; via partner if server-side).

**Buy-side hierarchy.** Network → **Advertiser** ("a single client or brand on whose behalf you want to serve ads") → **Insertion Order** ("a financial agreement... total budget... for a period of time") → **Line Item** ("the agreed upon strategies... budget... targeting") → **Creative** ("an actual ad, hosted either by Microsoft Advertising or by a third-party ad server"). Supporting: segment pixels (audience build), conversion pixels (attribution), impression/click **trackers** attached as piggyback pixels to externally hosted creatives, third-party creative pixels (verification).

**Sell-side hierarchy.** Network → **Publisher** → **Placement Group** → **Placement** ("a piece of web or mobile inventory where a creative with matching specifications can serve"; size/types, reserve price, self-classification). **Payment rules** (financial agreement with publisher), **network ad quality** + **publisher ad quality** ("restrictions set in your network ad quality profile cannot be loosened at the publisher level... may only be more strict"), **content categories** (universal + custom), **packages and deals** (pre-made or one-off inventory+data offerings).

**Suitability for boundary work.** The docs name the ad server function, the selling machinery (SSP-side: payment rules, deals, reselling exposure, buyer eligibility), and the buying machinery (bidder) as distinct things inside one suite — direct evidence that "ad server" is a named, bounded function even when bundled.

### AdButler — Key observations (Evidence layer A)

**Self-description.** "AdButler is a self-managed ad serving platform that helps you quickly and easily manage online ad campaigns. Whether you're solely an advertiser or a publisher, or someone who manages ad networks..." (help center). Related help-center articles confirm "Requests vs. impressions" and CDN as creative-hosting infrastructure.

**Object model.** "**An advertiser** is a company or individual who has ads available for display. An individual ad creative is referred to as an **ad item**. These ad items exist as part of an **ad campaign**." "**A publisher** is a website or entity that has space available for displaying advertisements. These advertising spaces are called **zones**." "You can start serving advertiser campaigns to publisher zones by connecting them with a **zone assignment**. The zone assignment is what holds all the settings that determine how an ad is selected when an ad request comes in."

**Delivery mechanics** (from prior sibling fetches of the same help center, reconfirmed by today's fetch of the serving-model article): ad request = "a call sent by a zone tag to AdButler's server asking for an ad to display"; static weights dictate relative serving frequency; schedules set start/end; default ads and programmatic backfill (OpenRTB) when nothing fits; requests are distinct from countable impressions.

### Revive Adserver — Key observations (Evidence layer A for README claims; era check)

**Self-description (README, verbatim).** "Revive Adserver is an open source ad serving tool that enables publishers to: Serve ads on their websites; Manage their campaigns from different advertisers and/or ad networks using the simple, easy-to-use interface; Track and report on campaign success, including click-through rates; Set rules to target the delivery of campaigns, or even ads, to specific users, to help maximise the effectiveness of campaigns."

**Era evidence.** Repo root contains `phpadsnew.inc.php` (phpAdsNew → Openads/OpenX → Revive lineage, early 2000s) and the classic delivery endpoints (`adview.php`, `adclick.php`, `adframe.php`, `adjs.php`, `adlayer.php`, `adx.js`) — the tag-requested, per-request delivery model of the tag-and-banner era. GeoLite2-based geotargeting plugin documented. A hosted edition exists for non-self-hosters.

**Historical check result.** The 2000s-era model (zones + banners + campaigns + weights + targeting + delivery logging, requested via page tags) satisfies the same defining structure as the modern samples; modern additions (RTB fill, header bidding, eCPM optimization, first-party segments, forecasting, self-serve consoles) are accretions.

### Equativ — Key observations (Evidence layer B/C — positioning only; weak)

Homepage positions "CTV Ad Server" and "Monetization / SSP" as separate named lines under Publisher Solutions, alongside an Advertiser Platform and retail media. Two inferences, both weakly held and used only for market-structure corroboration: (1) "ad server" remains the standard product-line name at enterprise platforms; (2) ad server and SSP are named as distinct lines within one vendor's suite, consistent with the Xandr structure. No operational detail was reachable (docs 404), so nothing from Equativ feeds the canonical model.

## Cross-product Comparison

| Dimension | Kevel | Xandr Monetize | AdButler | Revive Adserver |
|---|---|---|---|---|
| Self-description | "fully featured ad server"; APIs to build ad platforms | contains an explicit "Ad server" role in an end-to-end suite | "self-managed ad serving platform" | "open source ad serving tool" |
| Demand hierarchy | Advertiser → Campaign → Flight → Ad → Creative | Advertiser → Insertion Order → Line Item → Creative | Advertiser → Campaign → Ad Item → Creative | Advertiser → Campaign → Banner (era naming) |
| Supply hierarchy | Channel → Site → Zone | Publisher → Placement Group → Placement | Publisher → Zone (+Channel grouping) | Publisher → Zone (era naming) |
| Request-time entry | Decision API (server-to-server); ad codes/VAST | client-side tag (Seller Tag) or server-side calls | zone tag on page | adview/adframe/adjs PHP endpoints (era) |
| Selection model | priority waterfall × selection method (lottery weights / eCPM auction) | priority tiers; guaranteed vs RTB competition | zone assignment + static weights | weights/rotation rules (era) |
| Goals/pacing/caps | goal types + daily recalculation; caps pause flights; overserve documented | budget + pacing % + underspend catch-up; reservation | impression quotas; schedules | scheduling + weights (era) |
| Targeting | geo/keyword/custom/category/daypart/site-zone/segments/behavioral/frequency | device/inventory/category/key-value/video/system/page/geo/segments/frequency-recency/demographics | keywords/geo/device/data-keys | geo + rules (era) |
| Fallback | House priority; RTB programmatic fill | reselling priority; Open Market demand | default ad; backfill (OpenRTB) | default/house ads (era) |
| Event recording | impression/click/conversion/custom logs; log-level shipping | impression/click/conversion pixels; trackers for third-party-hosted creatives | requests vs impressions distinction; tracking pixels | impression/click logging (era) |
| Creative hosting | hosts creatives; templates for non-standard formats | hosts OR tracks third-party-hosted creatives | media library; CDN hosting | local banner store (era) |
| Forecasting | availability/deliverable/yield | available impressions, capacity, contending line items | — (not observed in fetched pages) | — |
| Rate types | Flat/CPM/CPC/CPA(view/click) | CPM/Viewable CPM/Fixed Fee | CPM/CPC/CPA | CPM/CPC (era) |
| Deployment | SaaS, API-first | SaaS enterprise suite | SaaS, self-managed | self-hosted OSS (+hosted edition) |

**Layer B (cross-product commonality) findings.** Across all four sampled products, independently and in their own words: (1) a two-sided registry — advertisers/campaigns/ads on one side, publishers/placements/zones on the other; (2) a per-request delivery decision triggered by a tag/SDK/API call; (3) rule-based selection combining eligibility (targeting, size, schedule) with competition (weights, priorities, or auction); (4) delivery-event recording (impressions; typically clicks and conversions) as the basis of reporting and billing; (5) fallback behavior when nothing qualifies; (6) rate types anchored on impressions/clicks/actions; (7) an operations UI for trafficking and monitoring. These are Type-level features, not vendor features.

**Alias test (Layer B).** All four sampled products self-identify as "ad server" / "ad serving" (Kevel: "fully featured ad server"; Xandr: explicit "Ad server" role; AdButler: "ad serving platform"; Revive: "ad serving tool"). Equativ names a "CTV Ad Server" line. No product in either this or the sibling research self-identifies primarily as an "ad delivery platform". The alias finding from research/ad-delivery-platform.md is confirmed from this side.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

**A managed ad pool + per-request ad call + rule-based selection + response + accountable delivery.**

1. **Managed ad pool** — ads (paid promotional content registered on behalf of advertisers) held in the system, organized into campaigns, each carrying delivery rules (when, where, to whom, how much).
2. **Per-request ad call** — at delivery time, a surface (tag, SDK, server-to-server API, video template, or downstream system) calls the platform identifying a placement and its context.
3. **Rule-based selection decision** — the platform evaluates which ads are eligible for this request (targeting, schedule, size, caps, frequency) and resolves competition among the eligible ones (priority tiers, weights, or an auction) to select a winner — or none.
4. **Response with the selected ad** — the creative or decision data is returned to the surface for rendering.
5. **Accountable delivery** — delivery events (at minimum impressions; typically clicks and conversions) are recorded against the delivered ad/campaign, forming the substrate of reporting, pacing, and billing.

Remove-the-piece tests:
- Remove the per-request decision → scheduled sends / planned-buys system (email marketing, campaign management).
- Remove the managed ad pool → a CDN (transport only).
- Remove paid/accountable ad semantics → a recommendation/personalization engine or content rotator.
- Remove event recording → pacing, capping, reporting, and billing all become inoperable; no market counterpart exists.

### L1 — Common Mature Structure

- Two-sided object hierarchy: advertiser → campaign → flight/line item → ad/creative; publisher/site → placement/zone (+ grouping objects)
- Targeting dimensions: geography, device/platform, keyword/contextual, custom key–values, audience segments, dayparting, frequency capping
- Goals, budgets, pacing (even/front/back-loaded), hard caps; reservation of guaranteed delivery
- Competition model: priority tiers/waterfall and/or auctions (eCPM); house/default ads and programmatic backfill beneath
- Creative management: hosting or third-party hosting with trackers, size/type validation, third-party tags, macros, rotation strategies
- Delivery-event tracking: impression/click/conversion pixels, redirects, server events; requests-vs-impressions hygiene
- Reporting: delivery vs goals, CTR/CVR, revenue by rate type (CPM/CPC/CPA/flat + effective metrics), breakdowns, custom/scheduled reports, log-level export in data-heavy products
- Forecasting: availability/capacity for targeting combinations; contending campaigns
- Programmatic demand integration: OpenRTB endpoints, header bidding, reselling tiers
- Conversion tracking / attribution
- Roles & portals: ad-ops console, scoped advertiser/publisher access, self-service, white-labeling
- Integration surfaces: ad tags, mobile SDKs, server-to-server decision APIs, video templates (VAST)

### L2 — Variant / Optional Structure

- **Side**: publisher-side (direct sales + yield) / advertiser-side (third-party serving across publishers) / both in one suite
- **Surface/format**: web display, in-app, video (VAST/VMAP, CTV/SSAI), audio, DOOH, email newsletters, native, retail-media onsite (sponsored products/listings)
- **Demand posture**: direct-only; direct + programmatic fill; unified auction; header bidding
- **Delivery posture**: client-side tags vs server-to-server decision API vs hybrid
- **Creative-hosting posture**: platform-hosted, third-party-hosted with trackers, or either
- **Deployment**: SaaS vs hosted OSS vs self-hosted OSS
- **Business model**: publisher tool vs white-label media-network platform vs embedded "build your own ad platform"
- **Identity/data posture**: cookie-based vs first-party/cookieless segments
- **Segment**: SMB/niche publishers vs enterprise suites

### L3 — Vendor-specific Structure (research notes only)

- Kevel: Flights; numbered Priorities (1–100) with per-priority selection algorithm fixed at creation; Lottery vs Auction; 5-minute balancer; Zerkel query language; UserDB; Relay (RTB); Decision/Management/Reporting API triad; Console; Catalog/product ads; data-shipping log taxonomy (request/decision/selection/auction logs); documented cap-overserve at 25K+ requests/second
- Xandr: Augmented Line Item; GDALI (guaranteed delivery, priority ranges 11–17 impressions / 18–20 exclusive); Seamless Insertion Orders; Allow RTB Competition; Programmable Splits; Impression Bus; Viewable CPM; network-vs-publisher ad-quality strictness rule; payment rules; packages/deals
- AdButler: Ad Items; zone assignments as the selection-rule container; static weights; Accupixel; header-bidding zones; white-label portals
- Revive: PHP delivery endpoints (adview/adclick/adframe/adjs/adlayer); plugin architecture; hosted edition; GeoLite2 geotargeting
- Equativ: Maestro agentic-suite branding (homepage-level only)

## Rejected Findings

1. **"Real-time bidding is definitional" — rejected.** Revive (era) and direct-only deployments serve without RTB; programmatic fill is integration beneath the selection engine. Even in Xandr, guaranteed line items can exclude RTB competition.
2. **"Client-side ad tags are definitional" — rejected.** Kevel is explicitly server-to-server ("any digital asset that requires a serving decision"); Xandr supports server-side calls; the invariant is the per-request call, whatever its transport.
3. **"Auction-based selection is definitional" — rejected.** Weight/lottery rotation (Kevel lottery, AdButler static weights, era rotation) is equally native; auctions are one selection method within tiers.
4. **"An ad server is publisher-side only" — rejected.** Xandr's buy-side hierarchy (advertiser → insertion order → line item → creative + impression/click trackers for externally hosted creatives) is the advertiser-side serving structure inside the same product; Kevel equally serves "advertiser campaigns". The two-sided registry supports both directions.
5. **"The ad server must host the creatives" — rejected.** Xandr explicitly traffics creatives "hosted either by Microsoft Advertising or by a third-party ad server", tracked via piggyback impression/click trackers; hosting is separable from decisioning.
6. **"Forecasting/reservation are definitional" — rejected.** Present in Kevel/Xandr; absent from fetched AdButler/Revive material; mature but not invariant.
7. **"Unified auction across direct and programmatic demand is the modern definition" — rejected.** Priority waterfalls with programmatic fill coexist in the same products; both are competition-model variants.
8. **"Ad server = a creative CDN" — rejected.** CDN is at most hosting infrastructure (AdButler documents its CDN as such); selection, not transport, is the essence.

## Boundary Findings

1. **vs Ad Delivery Platform (sibling leaf) — probable ALIAS; joint review completed.** Every product sampled across both researches self-identifies as an "ad server"/"ad serving" system; none primarily self-identifies as an "ad delivery platform". "Ad delivery" is the delivery-centric framing of the same request-time selection engine (request → decision → response → tracking). Test: substitute "ad delivery platform" for "ad server" in any sampled product's self-description — every sentence still holds; substitute in the reverse direction and nothing changes either. Recommendation: **Ad Server is the canonical name** for the Type (dominant market usage, vendor self-description, industry vocabulary); Ad Delivery Platform should be treated as an alias/merge candidate. Recorded here and in STATUS.md; no unilateral DIRECTORY change.
2. **vs Demand-side Platform / DSP** — the DSP's unit of work is the **bid response** to external bid requests on behalf of advertisers, across many sellers; it holds no placement registry and no managed pool on known inventory. The ad server's unit is the **managed ad pool + per-request selection on known placements**. Remove the pool/placement structure and operate only through external auctions → DSP. Enterprise suites bundle both (Xandr's bidder/Impression Bus vs its ad-server role).
3. **vs Supply-side Platform / SSP** — the SSP packages and **sells** inventory (deals, packages, payment rules, buyer eligibility, reselling exposure); request-time selection is the ad server's job. Remove selection, keep selling machinery → SSP. Direct evidence of the split: Xandr documents ad quality/payment rules/deals as separate from its ad-server role; Equativ lists "CTV Ad Server" and "Monetization / SSP" as separate publisher-solution lines.
4. **vs Programmatic Advertising Platform** — umbrella/marketing term spanning DSP + SSP + exchange + data; no distinct structure of its own. Not a separate Type.
5. **vs Advertising Campaign Management** — the planning/management layer (media plans, budgets, cross-channel coordination). It decides what should run; the ad server decides what actually renders on this request. Remove request-time execution → campaign management.
6. **vs Creative Management Platform / DCO** — produce and adapt creatives (assembly, versioning, dynamic composition); the ad server decides when/where they render. Output of the CMP is trafficked into the ad server as creatives.
7. **vs Recommendation / Personalization Engine** — both select an item per request from a candidate pool under rules. Distinguishing test: ads are **paid promotional content with accountable delivery** (impression/click billing, campaign goals, advertiser–publisher relationship, rate types); recommendations are organic content optimizing engagement with no per-delivery accountability to a paying third party. Remove payment/accountability semantics → personalization engine.
8. **vs CDN / creative hosting** — transport without selection decisions or campaign rules; hosting is at most an L1/L2 capability of ad serving.
9. **vs Email Marketing Platform** — scheduled sends to a list; no per-request placement call, no impression semantics. (Serving ads *inside* newsletters via zone tags is a surface variant of this Type, not email marketing.)

## Uncertainties

1. **Google Ad Manager** documentation was unreachable (timeouts across both research passes). GAM is universally described in the market as an ad server and is assumed to fit the defining structure, but no product-specific claim about it is made. The model is derived from four directly evidenced products.
2. **Advertiser-side ad serving** (dedicated third-party ad servers) was not directly fetched; its structure is evidenced through Xandr's buy-side hierarchy and impression/click trackers for externally hosted creatives. Advertiser-side-specific workflows (brand verification, cross-publisher reach reporting) are asserted only weakly and kept out of the canonical document's core.
3. **Equativ** evidence is homepage-level positioning only (docs 404); used solely to corroborate market naming and suite structure, never for operational claims.
4. **CTV/SSAI, audio, DOOH, email serving** confirmed only via product positioning pages (Kevel, AdButler, Equativ nav), not via fetched operational docs; treated as surface variants with moderate confidence.
5. Exact numeric behaviors (priority ranges, pacing defaults, balancer intervals, overserve tolerances) are vendor-specific and deliberately excluded from the canonical document.
6. Whether the directory intends "Ad Delivery Platform" as a distinct Type could not be determined from market evidence; recorded as a boundary issue and resolved (as a recommendation) in the joint review above.

## Final Synthesis

An Ad Server is the request-time execution engine of digital advertising — the market-canonical name for the system the sibling leaf calls an "ad delivery platform". It holds a managed pool of ads — registered on behalf of advertisers, organized into campaigns, each carrying delivery rules — and, for every ad call arriving from a delivery surface (web tag, app SDK, server-to-server API, video template, or downstream system), it decides which ad, if any, to deliver: filtering by eligibility (targeting, schedule, size, caps, frequency), resolving competition among eligible ads (priority tiers, weights, or auctions), and returning the selected creative for rendering. Every delivery is recorded — impressions, clicks, conversions — and those records are the substrate for reporting, pacing, billing, and optimization. Around this loop, mature products add the two-sided registry (advertiser/campaign/creative vs publisher/placement), goals and pacing with reservation of guaranteed delivery, forecasting, programmatic demand integration, creative management with hosting or third-party tracking, self-service portals, and multi-surface support (display, video/CTV, in-app, native, email, DOOH, retail media). The definition holds across eras (self-hosted tag-and-banner servers), philosophies (API-first vs UI-first), deployment models (SaaS vs OSS), and sides (publisher-side, advertiser-side, combined suites). The four-product evidence base, the era check, and the alias joint review all converge on one structure; "Ad Server" is its canonical name.
