# Research Notes — Ad Delivery Platform

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1

## Research Goal

Understand what an "Ad Delivery Platform" actually is as an Application Type: what objects exist inside it, what the request-time delivery loop looks like, who operates it, which rules govern delivery, and where its boundaries sit against the neighboring advertising-stack Types that share the same directory section (Ad Server, DSP, SSP, Programmatic Advertising Platform, Advertising Campaign Management).

## Initial Boundary (pre-research hypothesis)

- Hypothesis: an Ad Delivery Platform is the request-time engine of digital advertising — it receives ad calls, selects an ad from a managed pool under targeting/competition/pacing rules, returns it for rendering, and records delivery events.
- Likely confusions:
  1. **Ad Server** (sibling leaf) — in market usage "ad server" and "ad delivery" appear to describe the same system; the directory lists both.
  2. **DSP** — also "delivers ads" but through bidding in external auctions.
  3. **SSP** — also publisher-side, but focused on selling, not request-time selection.
  4. **Programmatic Advertising Platform** — umbrella term.
  5. **Advertising Campaign Management** — planning layer, not execution engine.
  6. **Recommendation/Personalization Engine** — also does per-request selection from a candidate pool.
- Unknowns: whether "ad delivery" denotes a distinct product category with its own terminology, or is a delivery-centric synonym of "ad server"; whether advertiser-side ad serving is in scope.

## Research Questions

1. What are the core objects (demand side, supply side, and the delivery-time decision)?
2. What exactly happens between an ad request and an ad being displayed?
3. How is competition among ads resolved (priority/waterfall vs auction vs weights)?
4. How do goals, budgets, pacing, and caps control delivery over time?
5. What targeting dimensions exist, and where do they attach (campaign/flight/line item)?
6. What happens when nothing qualifies (default/house/backfill)?
7. How are delivery events recorded and turned into reporting/billing?
8. What integration surfaces exist (tags, SDKs, server-to-server API, VAST)?
9. Who are the users (ad ops, yield, advertisers, publishers, developers)?
10. Where is the boundary against DSP / SSP / campaign management / personalization?
11. Does the core hold for older, self-hosted, and non-web (retail media, CTV, email, DOOH) implementations?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer levels:

| Product | Philosophy / segment | Role in sample |
|---|---|---|
| Kevel (ex-Adzerk) | API-first ad server; "build your own ad platform"; retail media / sponsored listings | developer-centric, embedded-delivery philosophy |
| Microsoft Monetize (Xandr) | enterprise publisher suite: ad server + SSP + RTB in one | enterprise, full-stack, both buy-side and sell-side |
| AdButler | independent multi-channel ad server + self-serve portals; SMB/mid-market publishers and commerce media | SMB/mid-market, UI-first, white-label |
| Revive Adserver | free open-source, self-hosted ad server (phpAdsNew → OpenX lineage) | historical/era check + self-hosted variant |

Google Ad Manager (dominant publisher ad server) was intended as a fifth sample; all Google domains timed out repeatedly (see Sources). It is retained as a market anchor only, with no direct evidence.

## Sources

### Kevel (Tier 1 — official developer docs, fetched 2026-09-06)

- Docs index: https://dev.kevel.com/llms.txt (full documentation map)
- Introduction to Kevel: https://dev.kevel.com/docs/understanding-kevel.md
- Ad Decision Engine Overview: https://dev.kevel.com/docs/delivery-basics.md
- Priorities / Waterfall: https://dev.kevel.com/docs/priorities.md
- Flights: https://dev.kevel.com/docs/flights.md
- (Index also confirms: Decision API, Management API, Reporting API, Forecast, Console, UserDB, targeting pages, tracking/data-shipping logs, retail media, RTB/Relay, header bidding)

### Microsoft Monetize / Xandr (Tier 1 — official product docs on Microsoft Learn, fetched 2026-09-06)

- Hub: https://learn.microsoft.com/en-us/xandr/
- Monetize landing: https://learn.microsoft.com/en-us/xandr/monetize/
- About Monetize: https://learn.microsoft.com/en-us/xandr/monetize/about-monetize
- Object Hierarchy: https://learn.microsoft.com/en-us/xandr/monetize/object-hierarchy
- Guaranteed Delivery Line Item (GDALI): https://learn.microsoft.com/en-us/xandr/monetize/create-a-guaranteed-delivery-line-item-gdali

### AdButler (Tier 1 — official help center, fetched 2026-09-06)

- Help center: https://www.adbutler.com/help
- What is AdButler?: https://www.adbutler.com/help/article/quick-start
- How AdButler serves ads: https://www.adbutler.com/help/article/how-adbutler-serves-ads
- Glossary of Terms: https://www.adbutler.com/help/article/glossary
- Product site (positioning): https://www.adbutler.com/

### Revive Adserver (Tier 1/2 — official README via GitHub; site blocked, fetched 2026-09-06)

- Repository README: https://github.com/revive-adserver/revive-adserver
- (www.revive-adserver.com returned HTTP 403; GitHub README used as the official description; repo tree confirms phpAdsNew heritage file `phpadsnew.inc.php` and classic delivery endpoints adview/adclick/adframe/adjs)

### Unreachable

- Google Ad Manager: support.google.com/admanager (×2 timeout), developers.google.com/ad-manager (timeout), admanager.google.com (timeout) — abandoned per network-restriction rule. No direct GAM evidence used anywhere in this research.
- Amazon Ad Server (advertiser-side) not fetched; advertiser-side ad serving is instead evidenced through Xandr Monetize's buy-side hierarchy (advertiser → insertion order → line item → creative), which is the same structure.

## Product Observations

### Kevel — Key observations (Evidence layer A unless noted)

**Positioning.** "Kevel is a set of APIs that lets customers build a unified ad platform supporting any ad format, any creative, and the management of multiple demand sources." Self-describes as "a fully featured ad server that can serve any creative and any ad format, including standard IAB ads, video ads, DOOH, audio ads, sponsored listings, native ads, and any other digital asset that requires a serving decision." Server-to-server philosophy: the customer's server handles the ad response and renders; not constrained by client-side ad code.

**Object model (demand).** Advertisers → Campaigns → Flights → Ads → Creatives. A flight is "a collection of ads grouped under a campaign. Most targeting and delivery rules are set at the flight level": impression goals, tracking methods, dates, targeting.

**Flight delivery rules.** Goal types: impressions, percentage (share of a priority), click, conversion, revenue, daily revenue, monthly revenue. The engine throttles delivery to hit the goal by the end date (example: 3M impressions over 30 days ≈ 100K/day, recalculated daily). Caps are hard limits (daily/lifetime; impressions/clicks/conversions/revenue) that shut a flight off; documented overserve risk when traffic surges or caps are set below ~one hour of traffic. Rate/price: Flat, CPM, CPC, CPA View, CPA Click, CPA View & Click — used for revenue estimation; on auction priorities Rate × Price feeds the eCPM bid.

**Object model (supply).** Network → Channels → Sites → Zones. Ad code / zone tags trigger ad requests; VAST ad code for video.

**Decision engine.** Inputs: creative size; targeting and goal settings on Ad/Flight/Campaign; the Channel's Priority for the flight. Process: Decision API request arrives (placement location, user agent, keywords, user key, custom targeting data, location) → engine filters all ads by criteria → walks priorities in order (e.g., Sponsorship, then Auction, then House) → picks a winner by the priority's selection method: **Lottery** (proportional to weights; "an ad with a weight of 50 would have 50 balls in the bowl") or **Auction** (highest eCPM wins; floor price; optional second-price; remainder percentage gives poor performers a second chance). A **balancer** recomputes creative weights every 5 minutes or on save; percentage-goal flights get static weights, goal-based flights get dynamic weights from projected vs actual delivery.

**Priorities / waterfall.** Priorities determine precedence ("House Ads only appear if there's no advertiser to fill the slot"); they work like a waterfall — unfilled impressions cascade to the next priority. Set per Channel; numbered 1 (highest) to 100 (lowest); defaults Sponsorship (1), Premium (5), House (20).

**Targeting.** Geo (country/region/metro), keyword (passed in request, with logic), custom targeting (custom fields + reserved keys, Zerkel query language), category/interest, day & hour parting, site/zone, user segments (first-party data via UserDB), behavioral, distance, frequency capping at advertiser/campaign/flight/ad levels.

**Tracking & data.** Impression/click/conversion/custom-event logs; conversion tracking (three approaches) and attribution; data shipping (log-level export to S3/BigQuery/Snowflake/etc.); request/decision/selection/auction logs — the decision process itself is logged per placement.

**Forecasting.** Availability forecast, deliverable forecast (new ads vs existing), yield forecast dashboards; reserved campaigns for not-yet-booked inventory.

**Programmatic & retail media.** Programmatic fill via RTB ("Relay"), demand partners, deals, header bidding (Prebid.js, ados.js). Retail media: Catalog, product ads from catalog, sponsored listings/brands/profiles/locations, Console (a UI for media owners and advertisers, incl. self-serve campaign creation, user/permission management, SSO, audit log).

### Microsoft Monetize (Xandr) — Key observations (Evidence layer A)

**Positioning.** "Microsoft Monetize is a web-based application for your programmatic advertising. Whether you're buying or selling ad space, or both, Monetize provides all the tools that you need to manage your accounts." Explicitly: "Instead of operating an ad server and a buying platform, Monetize can perform both functions."

**Ad server role (verbatim).** "As an ad server user, you have access to your end-to-end setup of advertiser and publisher information. You can set up publishers and available inventory, as well as advertisers and their selling specifications. With an ad server, you can set up and manage your buy-side systems and your sell-side systems, as well as manage forecasting, priorities, and many other types of functionality between the two."

**Process flow (verbatim summary).** Ad calls received from supply partners (client-side tag or server-side) → segment data overlaid from server-side cookie store → bid requests sent to all bidders (milliseconds to respond) → Monetize bidder processes (campaigns, targeting, bidding algorithms) → impression bus evaluates bids and publisher preferences → winning ad served (directly if client-side; via partner if server-side).

**Buy-side hierarchy.** Network → Advertiser → Insertion Order (financial agreement: budget, billing period) → Line Item (the strategy: budget, targeting) → Creative ("the actual ad, hosted either by Microsoft Advertising or by a third-party ad server"). Supporting objects: segment pixels (build audiences), conversion pixels (attribution), impression/click trackers for externally hosted creatives, third-party creative pixels (verification).

**Sell-side hierarchy.** Network → Publisher → Placement Group → Placement ("a piece of web or mobile inventory where a creative with matching specifications can serve"; size/types, reserve price, self-classification). Payment rules (publisher financial agreement), network + publisher ad quality (restrict which creatives serve; publisher-level may only be stricter than network-level), content categories (universal + custom), packages and deals (pre-made or one-off inventory+data offerings for buyers).

**Guaranteed Delivery Line Item (GDALI).** Delivery types: **Impressions** (impression goal; priorities typically 11–17) vs **Exclusive** (percentage/share-of-voice; priorities 18–20, take precedence over RTB). **Allow RTB Competition**: a guaranteed line item below the reselling priority can compete with Open Market (RTB) demand to maximize yield while ensuring full delivery. Budget & scheduling: budget (impressions/viewable impressions or %), revenue type (CPM, Viewable CPM, Fixed Fee), **pacing** (100% = even daily split; >100% front-loaded; <100% back-loaded; default 105%), **underspend catch-up** (Evenly vs ASAP), dayparting. Targeting: device type, inventory type (app/web), universal/custom categories, direct inventory (publishers/placement groups/placements), key/value, video targeting, system (OS/browser/language/device/carrier), page properties (tag position, query-string values), geography, audience segments (own + third-party), frequency & recency caps ("serve only 1 imp per page"; "include users without cookies" — serving to unidentified users ignores frequency/recency caps), demographics. Creatives: rotation strategies (auto-optimize by CTR / even / manual weights), landing page. **Programmable splits** for sophisticated allocation. **Forecasting footer**: available impressions, total capacity, contending line items; refreshes as targeting/budget/dates change. **Save and Reserve**: saving can reserve inventory so impressions cannot be allocated to other line items. Roadblocking: serve multiple linked creatives together (master + companion sizes; video slot positions).

### AdButler — Key observations (Evidence layer A)

**Positioning.** "AdButler is a self-managed ad serving platform that helps you quickly and easily manage online ad campaigns. Whether you're solely an advertiser or a publisher, or someone who manages ad networks..." "Serve and track your direct-sale and third-party ad sources from one place." Product site: ad servers "across every channel — display, video, email, mobile, native and CTV/OOH"; self-service portals "on top of AdButler or Google Ad Manager"; commerce/retail media network positioning; white-label branding.

**Object model.** Publisher (owns zones) → **Zone** ("a location on a website or an app where ads are served", with a **zone tag** placed on the publisher's site that "calls for ads to be displayed in a zone whenever a viewer loads the page") → **Channel** (group of zones across publishers). Advertiser → **Campaign** ("a collection of ad items... share a schedule and overall are treated as one placement") → **Ad Item** ("an individual ad") → **Creative** (the displayed part; stored in a Media Library). The **zone assignment** "holds all the settings that determine how an ad is selected when an ad request comes in."

**Delivery mechanics.** **Ad request**: "a call sent by a zone tag to AdButler's server asking for an ad to display." **Static weight**: "an integer that dictates how often an ad item or campaign should be served relative to other ad items or campaigns that are assigned to the same zone" (weight 2 vs 1 → serves twice as often). **Schedule**: campaign start/end dates (campaign-level or ad-item-level). Pacing & impression quotas; financial settings (CPM/CPC/CPA with effective eCPM/eCPC/eCPA metrics).

**Targeting.** "A method of serving ads to or excluding ads from a group of audiences based on parameters such as keywords, geography, or device" — plus Data Keys (custom targeting).

**Fallbacks & programmatic.** **Default ad**: "the ad item that will show when there's no ad that fits the requirements of a zone... usually a programmatic ad or an in-house ad." **Backfill**: reserve ad items used when no ads fit, "usually... from a programmatic source" (OpenRTB endpoints). **Header bidding zones** supported. **Roadblock** (home page takeover: all zones on a page).

**Measurement.** Requests vs impressions distinction (a request does not always produce a countable impression); Accupixel (loads pixels after ad load to ensure impressions are genuine); tracking pixels (impression/click/conversion); custom reports; CTR/CVR.

**Access model.** Sub-user accounts for advertisers and publishers "with limited access to sections and features"; white-label admin dashboard and serving domains; full API access.

### Revive Adserver — Key observations (Evidence layer A for README claims; era check)

**Positioning (README, verbatim).** "Revive Adserver is an open source ad serving tool that enables publishers to: Serve ads on their websites; Manage their campaigns from different advertisers and/or ad networks using the simple, easy-to-use interface; Track and report on campaign success, including click-through rates; Set rules to target the delivery of campaigns, or even ads, to specific users, to help maximise the effectiveness of campaigns." Hosted edition exists for those who don't want to self-host.

**Era evidence.** Repo tree contains `phpadsnew.inc.php` (phpAdsNew → Openads/OpenX → Revive lineage, early-2000s) and classic delivery endpoints (`adview.php`, `adclick.php`, `adframe.php`, `adjs.php`, `adlayer.php`, `adx.js`) — the tag-requested, per-request delivery model of the 2000s era. Geo-targeting plugin (MaxMind GeoLite2) documented in the README blog link.

**Cross-era check (§24).** The phpAdsNew-era model (zones + banners + campaigns + weights + targeting + delivery logging, requested via tags) is structurally identical to the modern samples: same L0. Modern additions (RTB fill, header bidding, eCPM auctions, first-party segments, forecasters, self-serve consoles) are accretions, not definitional structure.

## Cross-product Comparison

| Dimension | Kevel | Xandr Monetize | AdButler | Revive Adserver |
|---|---|---|---|---|
| Self-description | "fully featured ad server"; APIs to build ad platforms | web app for programmatic buying+selling; contains "Ad server" role | "self-managed ad serving platform" | "open source ad serving tool" |
| Demand hierarchy | Advertiser → Campaign → Flight → Ad → Creative | Advertiser → Insertion Order → Line Item → Creative | Advertiser → Campaign → Ad Item → Creative | Advertiser → Campaign → Banner (era naming) |
| Supply hierarchy | Channel → Site → Zone | Publisher → Placement Group → Placement | Publisher → Zone (+Channel grouping) | Publisher → Zone (era naming) |
| Request-time entry | Decision API (server-to-server); ad codes/VAST | client-side tag (Seller Tag) or server-side calls | zone tag on page; JSON API; VAST | adview/adframe/adjs PHP endpoints |
| Selection model | priorities (waterfall) × selection method (lottery by weights / eCPM auction) | priority tiers; guaranteed vs RTB competition; optimization levers | zone assignment + static weights; serve methods | weights/rotation rules (era) |
| Goals/pacing | goal types (impressions/%/click/conversion/revenue) + daily recalc; caps | budget + pacing % (even/front/back) + underspend catch-up; reservation | impression quotas; schedule; pacing | scheduling + weights (era) |
| Targeting | geo/keyword/custom/category/daypart/site-zone/segments/behavioral/frequency | device/inventory/category/key-value/video/system/page/geo/segments/frequency-recency/demographics | keywords/geo/device/data-keys | geo + rules (era) |
| Fallback | House priority; programmatic fill (RTB) | reselling priority; Open Market demand | default ad; backfill (OpenRTB) | default/house ads (era) |
| Event recording | impression/click/conversion/custom logs; log-level shipping | impression counting; trackers; log-level data feeds | requests vs impressions; Accupixel; pixels | impression/click logging (era) |
| Forecasting | availability/deliverable/yield forecasts | available impressions, capacity, contending line items | — (not observed in fetched pages) | — |
| Revenue types | Flat/CPM/CPC/CPA(view/click) | CPM/Viewable CPM/Fixed Fee | CPM/CPC/CPA (+e* metrics) | CPM/CPC (era) |
| Self-serve/portals | Console (media owners + advertisers) | (managed model; Partner Center) | sub-user accounts; white-label portals | — |
| Deployment | SaaS, API-first | SaaS enterprise suite | SaaS, self-managed | self-hosted OSS (+hosted edition) |

**Layer B (cross-product commonality) findings.** Across all four sampled products, independently and in their own words: (1) a two-sided registry — advertisers/campaigns/ads on one side, publishers/placements/zones on the other; (2) a per-request delivery decision triggered by a tag/SDK/API call; (3) rule-based selection combining eligibility (targeting, size, schedule) with competition (weights, priorities, or auction); (4) delivery-event recording (impressions/clicks/conversions) as the basis of reporting; (5) fallback behavior when nothing qualifies; (6) revenue-rate types anchored on impressions/clicks/actions; (7) an operations UI for trafficking and monitoring. These are Type-level, not vendor, features.

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

**A managed ad pool + per-request delivery decision + accountable delivery.**

1. **Managed ad pool** — ads (paid promotional content registered on behalf of advertisers) held in the system, organized into campaigns, each carrying delivery rules (when, where, to whom, how much).
2. **Per-request ad call** — at delivery time, a surface (tag, SDK, server-to-server API, or downstream system) calls the platform identifying a placement and its context.
3. **Rule-based selection decision** — the platform evaluates eligible ads against the request context and business rules (targeting, schedule, caps, frequency, priority/competition) and selects one (or none).
4. **Response with the selected ad** — the platform returns the creative or decision data for rendering on the surface.
5. **Accountable delivery** — delivery events (at minimum impressions; typically clicks and conversions) are recorded against the delivered ad/campaign, forming the basis of reporting and billing.

Remove the per-request decision → a scheduled content/email send system. Remove the managed ad pool → a CDN. Remove ad semantics (paid, third-party-promoting, accountable) → a personalization/recommendation engine. Remove event recording → nothing in the market resembles it (no reporting, no billing, no pacing — the delivery rules themselves become inoperable).

### L1 — Common Mature Structure

- Two-sided object hierarchy: advertiser → campaign → flight/line item → ad/creative; publisher/site → placement/zone (+ grouping)
- Targeting dimensions: geography, device/platform, keyword/contextual, custom key-values, audience segments, dayparting, frequency capping
- Goals, budgets, pacing (even/front/back-loaded), hard caps; reservation of guaranteed delivery
- Competition model: priority tiers/waterfall and/or auction (eCPM); house/default ads and programmatic backfill
- Creative management: upload, sizes/types, third-party tags, macros, rotation strategies (even/manual/optimized)
- Delivery-event tracking: impression/click/conversion pixels and logs; requests-vs-impressions hygiene
- Reporting: delivery vs goal, CTR/CVR, revenue by rate type (CPM/CPC/CPA + effective metrics), custom/scheduled reports, log-level export
- Forecasting: availability/capacity, contending campaigns
- Integration surfaces: ad tags, mobile SDKs, server-to-server decision API, video templates (VAST)
- Programmatic demand integration: OpenRTB endpoints, header bidding, reselling priority
- Roles & portals: ad-ops console, advertiser self-service, publisher access, white-labeling
- Conversion tracking / attribution

### L2 — Variant / Optional Structure

- **Side**: publisher-side ad server (direct + yield) / advertiser-side (third-party serving across publishers) / both in one suite
- **Surface/format**: web display, in-app, video (VAST/VMAP), CTV & SSAI, audio, DOOH, email newsletters, native, retail-media onsite (sponsored products/listings)
- **Demand posture**: direct-only; direct + programmatic fill; unified auction; header bidding
- **Delivery posture**: client-side tags vs server-to-server decision API vs hybrid
- **Deployment**: SaaS vs self-hosted open source vs hosted OSS
- **Business model**: publisher tool vs white-label media-network platform vs embedded "build your own ad platform"
- **Identity/data posture**: cookie-based vs first-party/cookieless segments
- **Segment**: SMB/niche publishers vs enterprise suites

### L3 — Vendor-specific Structure (research notes only)

- Kevel: "Flights", numbered Priorities (1–100) with per-priority selection algorithm fixed at creation, Zerkel query language, UserDB, Relay (RTB), 5-minute balancer recalc, Decision/Management/Reporting API triad, Console, Catalog/product ads, data-shipping log taxonomy (request/decision/selection/auction logs)
- Xandr: Augmented Line Item, GDALI, Seamless Insertion Orders, priority ranges (11–17 impressions / 18–20 exclusive), Allow RTB Competition, Programmable Splits, Impression Bus, Cadence Modifier / Chaos Factor, Viewable CPM, network-vs-publisher ad-quality strictness rule
- AdButler: Ad Items, zone assignments, Accupixel, static weights, bannerID/zoneID/advID naming, header-bidding zones
- Revive: PHP delivery endpoints, plugin architecture, hosted edition

## Rejected Findings

1. **"Real-time bidding is definitional" — rejected.** Revive (era) and direct-sold-only deployments serve without RTB; programmatic fill is L1/L2 integration. Even in Xandr, direct line items can be configured to exclude RTB competition.
2. **"Client-side ad tags are definitional" — rejected.** Kevel is explicitly server-to-server ("any digital asset that requires a serving decision"); Xandr supports server-side calls; the invariant is the per-request call, whatever its transport.
3. **"Auction-based selection is definitional" — rejected.** Weight/lottery selection (Kevel lottery, AdButler static weights, era rotation) is equally native; auctions are one selection method within priorities.
4. **"Ad delivery platform = creative delivery network (CDN-like)" — rejected.** No sampled product frames delivery as content distribution; CDN is at most an infrastructure detail (AdButler mentions its CDN for creative hosting). Selection, not transport, is the essence.
5. **"Forecasting/reservation are definitional" — rejected.** Present in Kevel/Xandr, absent from the fetched AdButler/Revive pages; common mature structure, not invariant.
6. **"Self-serve portals are definitional" — rejected.** Product-model dependent (L2).
7. **"Unified auction (direct vs programmatic in one pool) is the modern definition" — rejected.** Waterfall + reselling priority (Xandr) and priority waterfalls (Kevel) coexist; both are competition-model variants.

## Boundary Findings

1. **vs Ad Server (sibling leaf)** — probable **Alias**. Every sampled product self-identifies as an "ad server" / "ad serving" system; "ad delivery" is the delivery-centric description of the same functional Type (request → decision → response → tracking). No market evidence found of a distinct "ad delivery platform" category separate from ad serving. Test: remove the name "ad server" from any sampled product's self-description and substitute "ad delivery platform" — every sentence still holds. Flagged for joint review when Ad Server is processed; this document is written with the delivery-centric framing so it remains valid under either name.
2. **vs Demand-side Platform / DSP** — DSP's unit of work is the **bid response** to external bid requests on behalf of advertisers, across many sellers, with budget optimization across auctions; it holds no publisher placement structure. The ad delivery platform's unit is the **managed ad pool + per-request selection** on known/owned inventory. Remove the managed placement/pool structure and sell only via external auctions → DSP. (Xandr contains both: the bidder/Impression Bus is DSP-side; line items/priorities/forecasting are ad-server-side.)
3. **vs Supply-side Platform / SSP** — SSP packages and sells inventory (deals, packages, payment rules, reselling exposure, buyer eligibility). Request-time selection is the ad server's job; selling machinery is the SSP's. Remove per-request selection and keep only selling machinery → SSP. (Xandr Monetize literally contains both hierarchies; the ad-quality/payment-rule/deal objects are sell-side, the line-item/priority/forecast objects are ad-server-side.)
4. **vs Programmatic Advertising Platform** — umbrella/marketing term spanning DSP+SSP+exchange+DMP; no distinct structure of its own. Not a separate Type.
5. **vs Advertising Campaign Management** — planning/management layer (media plans, budgets, cross-channel coordination, trafficking instructions). It decides *what should run*; the delivery platform decides *what actually renders on this request*. Remove request-time execution → campaign management.
6. **vs Recommendation / Personalization Engine** — both select an item per request from a candidate pool under rules. Distinguishing test: ads are **paid promotional content with accountable delivery** (impression/click billing, campaign goals, advertiser–publisher relationship, rate types); recommendations are organic content optimizing engagement with no per-delivery accountability to a paying third party. Remove payment/accountability semantics → personalization engine.
7. **vs CDN / creative hosting** — transport without selection decisions or campaign rules; not the same Type.
8. **vs Email Marketing Platform** — scheduled sends to a list, no per-request placement call, no impression semantics. (Email *ad serving* — AdButler email zones — is a surface variant of this Type, not email marketing.)

## Uncertainties

1. Google Ad Manager documentation was unreachable (repeated timeouts); GAM-specific structures (e.g., its line-item/priority model, "unified pricing and controls") are **not** evidenced here. The canonical model is derived from four products only; GAM is assumed to fit the L0 (it is universally described as an ad server) but no product-specific claim about it is made.
2. Advertiser-side ad serving (Sizmek/Amazon Ad Server, Flashtalking) was not directly fetched; its structure is inferred from Xandr's buy-side hierarchy (advertiser → insertion order → line item → creative + trackers), which is the same shape. Advertiser-side specifics (brand verification workflows, cross-publisher reach reporting) are asserted only weakly.
3. Exact numeric behaviors (priority ranges, pacing defaults, cap overserve tolerances, balancer recalc intervals) are vendor-specific (L3) and deliberately excluded from the final document.
4. Whether the directory intends "Ad Delivery Platform" and "Ad Server" as distinct Types could not be determined from market evidence; recorded as a boundary issue rather than resolved unilaterally.
5. CTV/SSAI, audio, and DOOH serving were confirmed only via product positioning pages (AdButler/Kevel), not via fetched operational docs; treated as surface variants with moderate confidence.

## Final Synthesis

An Ad Delivery Platform is the request-time execution engine of digital advertising. It holds a managed pool of ads — registered on behalf of advertisers, organized into campaigns, each carrying delivery rules — and, for every ad call arriving from a delivery surface (web tag, app SDK, server-to-server API, video template, or downstream system), it decides which ad, if any, to deliver: filtering by eligibility (targeting, schedule, size, caps, frequency), resolving competition among eligible ads (priority tiers, weights, or auctions), and returning the selected creative for rendering. Every delivery is recorded — impressions, clicks, conversions — and those records are the substrate for reporting, pacing, billing, and optimization. Around this loop, mature products add two-sided hierarchies (advertisers/campaigns vs publishers/placements), goals and pacing with reservation of guaranteed delivery, forecasting, programmatic demand integration, self-service portals, and multi-surface support (display, video/CTV, in-app, native, email, DOOH, retail media). The market name for this system is most commonly "ad server"; "ad delivery platform" is the delivery-centric framing of the same Type — flagged as a probable alias in the directory.
