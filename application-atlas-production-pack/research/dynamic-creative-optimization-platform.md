# Research Notes — Dynamic Creative Optimization Platform

Research date: 2026-09-08
Slug: dynamic-creative-optimization-platform
Directory section: 06 Marketing, Advertising & Growth

## Research Goal

Understand what a Dynamic Creative Optimization (DCO) Platform actually is as an Application Type: its core object model, its end-to-end workflow, where it sits in the ad-delivery chain, how decisioning works, and where its boundary lies against neighboring Types (Creative Management Platform, Ad Server, DSP, A/B Testing, Marketing Personalization, Recommendation Engine).

## Initial Boundary (pre-research hypothesis)

- Core use: automatically assemble/personalize advertising creative from reusable components driven by data and decision logic, at serving time or at scale, and optimize which version is shown.
- Users: media traders / ad ops, creative teams, agencies, performance marketers.
- Nearest neighbors: Creative Management Platform (CMP) — likely the hardest boundary; Ad Server (decides which ad, not what's in it); DSP (buys impressions); A/B Testing (tests fixed variants); Marketing Personalization (owned channels); Recommendation Engine (owned surfaces).
- Unknowns: exact object model per product; whether "optimization" is definitional or just the mature layer; whether serving-time assembly is definitional or an implementation variant; how platform-native DCO (Google/Meta) realizes the model.

## Research Questions

1. What are the core objects? (template/shell, elements/slots, feed/catalog, versions, decision rules/strategy, rendered variants)
2. How does a dynamic creative get built end-to-end?
3. What drives the decision — configured rules, algorithmic optimization, or both?
4. Where does DCO sit in the delivery chain (own ad server/DSP, walled-garden publish, third-party ad server)?
5. What data inputs drive personalization (product feeds, audience segments, context, performance)?
6. What reporting granularity exists (campaign/version/element)?
7. What is the DCO vs CMP boundary in real products?
8. What variants exist (channel focus, decision granularity, decision authority, vertical catalogs)?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, different customer tiers:

1. **Adform** (Adform FLOW DSP/Ad Server + Adform Studio) — independent European ad-tech suite; DCO as a module inside the buying/serving stack; rules + version-spreadsheet philosophy. Tier-1 help center reachable.
2. **Innovid (with Flashtalking, Mediaocean)** — independent omnichannel creative/ad-management platform (display, video, TV/CTV, social); agency/enterprise-facing; "create, decision, measure" philosophy. Tier-2 product page; help center sign-in-gated.
3. **Hunch** — paid-social creative performance platform (Meta, Snapchat, TikTok); catalog/DPA-centric creative automation; designer-workflow philosophy (Figma/PSD import, dynamic layers). Tier-1 help center + Tier-2 product pages reachable.
4. **RTB House** — performance DSP; deep-learning personalized retargeting with "shoppable creative"; fully algorithmic, vendor-managed decisioning philosophy. Tier-2 site reachable.

Rejected/abandoned samples:
- **Google Marketing Platform (CM360/Studio, DV360 dynamic remarketing)** — support.google.com and marketingplatform.google.com timed out repeatedly (3+ attempts). Abandoned per network rules. Platform-native pole left under-evidenced.
- **Meta (dynamic ads / Advantage+)** — facebook.com transport errors (3 attempts). Abandoned. Partial indirect evidence via Hunch's Tier-1 documentation of Meta's catalog requirements.
- **Flashtalking standalone help center** — sign-in-gated except reporting category.
- **Smartly.io** — help.smartly.io transport errors (2 attempts). Abandoned.
- **Amazon Ad Server (ex-Sizmek)** — 404 on attempted doc URLs; abandoned after 2 attempts.
- **Sizmek wiki** — 404; abandoned.

## Sources

Tier-1 (official operational documentation):
- Adform Help Center — "Learn About Dynamic Ads" — https://www.adformhelp.com/hc/en-us/articles/9738629148049-Learn-About-Dynamic-Ads (updated 2025-09-28; fetched 2026-09-08)
- Adform Help Center — "Build Dynamic Ads" — https://www.adformhelp.com/hc/en-us/articles/11376593619473-Build-Dynamic-Ads (updated 2025-03-31; fetched 2026-09-08)
- Adform Help Center — "Build Product-Targeting Ads" — https://www.adformhelp.com/hc/en-us/articles/11376632397713-Build-Product-Targeting-Ads (updated 2025-09-29; fetched 2026-09-08)
- Hunch Help Center — "DPA Catalogs" — https://help.hunchads.com/en/articles/7843614-dpa-catalogs (fetched 2026-09-08)
- Hunch Help Center — "Dynamic templates preview & review" — https://help.hunchads.com/en/articles/7010809-dynamic-templates-preview-review (fetched 2026-09-08)
- Hunch Help Center — Catalog Management collection index — https://help.hunchads.com/en/collections/3833638-catalog-management (fetched 2026-09-08)

Tier-2 (official product/marketing pages):
- Innovid — "Dynamic Ads" product page — https://www.innovid.com/platform/dynamic-ads (fetched 2026-09-08)
- Innovid — homepage/platform nav (create/deliver/measure/optimize structure) — https://www.innovid.com/ (fetched 2026-09-08)
- Hunch — homepage + Creative product page — https://www.hunchads.com/ , https://www.hunchads.com/product/creative (fetched 2026-09-08)
- RTB House — homepage + "Personalized Retargeting" offer page — https://www.rtbhouse.com/ , https://www.rtbhouse.com/offer/personalized-retargeting (fetched 2026-09-08)

Unreachable (recorded limitations):
- support.google.com (Campaign Manager 360 / Display & Video 360 / Studio help) — timeouts ×3
- marketingplatform.google.com — timeout
- facebook.com / Meta Business Help Center — transport errors ×3
- help.smartly.io — transport errors ×2
- flashtalking.com — transport errors ×2; support.flashtalking.com reachable but sign-in-gated
- sizmek.atlassian.net, advertising.amazon.com — 404

## Product Observations

### Adform (evidence layer: A — direct, Tier-1)

Positioning: "Adform offers Dynamic Creative Optimization (DCO) features and tools for you to personalize ads based on your visitors' preferences, to optimize your campaign performance, and to automate ad creation." Two solutions: **dynamic ads** and **product retargeting**. "A dynamic ad adjusts its presentation based on specific parameters." Works with any campaign — direct or programmatic. DCO incurs an additional CPM cost on top of regular ad serving.

Object model (direct quotes/structures):
- **Creative shell** — "a dynamic ad template with built-in logic to render relevant images, videos, text, and landing page information as indicated in the versioning spreadsheet." HTML5 standard, rich media, or pre-roll (VAST) shells. Up to 15 creative shells per dynamic ad.
- **Dynamic content** — images, videos, text and other elements that populate the shell. "Each banner component is saved separately, allowing you to mix and match different creative parts. You can select one or more parts to be dynamic."
- **Version spreadsheet** (.xlsx) — "one spreadsheet row for each version of a dynamic ad. The columns indicate the changing elements that determine the dynamic ad's content. Each specified element (such as a targeting definition or schedule) needs a separate column with a unique name."
- **Dynamic ad setup** — "an entity that consists of information about creative shells, versions data, and dynamic strategy set."
- **Strategy** — "you indicate a strategy to show the most relevant personalized messages for all impressions."
- **Dynamic Ad Version** (reporting dimension) — "a single set of data variables and values used for messaging."

Decision dimensions (rules-based targeting of versions): date/time (season, holidays, daypart), geo (country/state/region/city/postal/DMA), audience (DMP segments — requires DMP account; first- and third-party data), retargeting (site visitors; customize product images, headlines, CTA text, price), Adform Signal (impression-delivery data: winning line item, deal ID, media, domain — via macros), key-value/external signal (key value passed in the ad tag, e.g. page category, gender).

Product-feed route (product retargeting / product-targeting ads): import advertiser product data into Adform (feed file; TID = "ID of data feed imported to Adform"); ads fetch data via JavaScript (AdMessage.build with cid/tid/dcoEngineId); product fields include product_id, product_name, product_image, product_price, product_category, product_deeplink, top_offer; backend "can return up to 100 products"; carousel rendering via pageSize/getPage; "Dynamic Product View" event sent back with product/feed identifiers; clicks must use the platform-wrapped $link (tracker) not the raw deeplink.

Build depth ladder: (1) Adform Studio drag-and-drop shell building (no code); (2) Dynamic Ads Helper library — element IDs bound to spreadsheet column names (autoWire, addText, addImage, setDemoData for local testing, getVar/getVars, data-transform plugins); (3) fully custom coded shells ("Advanced DCO Ads") — third-party APIs, custom calculations, image manipulation, complex animations.

Setup flow: upload assets → create/upload creative shells → start dynamic ads setup + specify strategy → assign shells → upload version spreadsheet → preview → save → assign to campaigns/line items.

Reporting: custom reports with four unique dimensions — Dynamic Ads, Dynamic Ad Creative Shell, Dynamic Ad Setup, Dynamic Ad Version — crossed with standard campaign metrics (Tracked Ads, Clicks, Viewability %, eCPM, Conversions).

### Innovid / Flashtalking (evidence layer: A for positioning page, B for workflow detail)

Positioning (product page): "Create, decision, and measure dynamic ads at scale." "Personalize your TV, video, display, and social advertising with intuitive tools." Claims:
- "dynamic headlines, images, and video elements. Use targeting, location, and other data-driven criteria to increase campaign relevance."
- "Across TV, video, display, and social ads, manage DCO campaigns via a single partner."
- "Unlock deep intelligence about your ads with **content-, version-, and element-level reporting**. Test and learn to quickly optimize your creative strategy."
- "Generate mass creative versions in minutes, make creative updates to a live campaign quickly, and solve for scale."
- "Connect your DCO to our measurement and optimization capabilities to gain insights into what performs best for your audience. Boost your most important KPIs in real time."
- Case-study metrics (vendor-claimed): 600K+ customized creatives served per year; data feed updates launch in under a minute; 5x faster version rendering.

Platform context: Innovid platform = Create (ad authoring, interactive ads, dynamic ads, creative intelligence) / Deliver (digital ad management = independent ad serving, social ads management, audience management) / Measure / Optimize. DCO sits inside a full ad-management stack with its own ad server. Flashtalking heritage: help center sign-in-gated; public reporting category only. Mediaocean parent.

### Hunch (evidence layer: A — direct, Tier-1 + Tier-2)

Positioning: "Creative Performance Platform" for paid social (Meta, Snapchat, TikTok; also Pinterest/Google icons on site). "Build dynamic, data-driven creatives that scale instantly."

Catalog/feed machinery (Tier-1):
- "Dynamic product catalog is a structured data feed that contains information about the products that an advertiser wants to promote on Meta." Mandatory fields: id, title, description, availability, condition, price, link, image_link, brand. Vertical variants documented by reference: hotel, flight, destination, automotive (vehicle), property (home listing), streaming.
- "Using the information in the product catalog, Meta can dynamically generate personalized ads that feature the specific products that a person has viewed, added to cart, or purchased on an advertiser's website or app." (Indirect Tier-1 evidence about Meta's DPA model via a Meta Business Partner's docs.)
- Feed formats: csv, tsv, xml, json. **Feed Mapper** maps custom fields to required fields (custom verticals like Betting/Education). **Extender** enriches. **Filters** select items for automated catalogs.
- Catalog sync frequency: hourly / daily / weekly / monthly; "1st sync" creates the catalog; products with errors will not appear in promotions; products with warnings still show. Catalogs created in Hunch are replicated on Meta; Hunch campaigns use Hunch-created catalogs.
- **Product Sets** — subsets of the catalog (e.g., Smart Sets pulled from GA4/conversion data, refreshed weekly).

Template machinery (Tier-1 + Tier-2):
- "DPA template" — design with dynamic layers bound to feed data. Creative workflow: import key visual (Photoshop/Figma direct import) → define dynamic layers (feed data) → enrich with AI (background removal, product-color extraction, orientation detection) → set conditional visibility (discounts, savings, countdown timers, regional localization) → scale template across formats/placements → turn image to video (predefined/custom animations).
- Preview & review at scale: rendered images per product; flag individual images for editing; review filtered sets; view-only share links for external reviewers.
- Personalization dimensions: "location, language, time of the day, or weather."
- Automated campaigns: "Base your creative output or campaign setup on any kind of data"; bulk hyper-localized campaign launch from a single sheet; publish directly to Meta/Snapchat.
- Insights: SKU-level product insights; campaign insights; optimization collection (rules and alerts, email reports, trigger events based on reports).

### RTB House (evidence layer: A for positioning, B for mechanics)

Positioning: "Next-generation Performance DSP." Personalized retargeting powered by deep learning:
- "Deep Learning-powered product recommendations... Deep Learning uses contextual data to assess intent and serve ads to online users who will be of value to your brand. More data means better product recommendations, showing users new products that they will truly love."
- "Elevate your product catalog with amazing in-house creatives tailored to your brand."
- "We display on-brand shoppable creative with personalized product recommendations based on first-party signals. Delivered across the entire purchase journey."
- Advertiser "choose[s] your goals" (purchase frequency, CTR/conversion, engagement, AOV, ROAS, LTV); "campaigns that self-calibrate over time."
- 61% of purchased products "were not previously viewed" (vendor-claimed) — recommendation beyond retargeting.
- Funnel phases: next-gen retargeting, acquisition (dynamic product ads), quality traffic, demand generation (video/display with product overlays).
- Philosophy: vendor-managed algorithmic decisioning; advertiser does not configure templates/rules — the platform generates personalized creative from first-party signals + catalog.

## Cross-product Comparison

| Dimension | Adform | Innovid/Flashtalking | Hunch | RTB House |
|---|---|---|---|---|
| Type posture | DCO module inside DSP/ad-server suite | DCO inside independent omnichannel ad-management platform (own ad server) | DCO/creative automation for paid social; publishes to walled gardens | DCO embedded in managed performance DSP |
| Creative structure | creative shell (HTML5/rich media/pre-roll) + dynamic content parts | dynamic elements (headlines, images, video) across TV/video/display/social | DPA template with dynamic layers (Figma/PSD import) | vendor-built "shoppable creative" from catalog |
| Data substrate | version spreadsheet (.xlsx) + imported product feed (TID) + DMP segments + impression signals | data feeds; targeting/location criteria; measurement data | product catalog feed (csv/tsv/xml/json) + custom fields + extenders + product sets | first-party signals + product catalog |
| Decision logic | strategy + rules over versions (time/geo/audience/retargeting/signal/key-value) | "decision" as named capability; optimization connected to measurement | conditional visibility rules; automated campaigns from data; (platform-side optimization by Meta) | fully algorithmic (deep learning), self-calibrating to goals |
| Assembly timing | serving-time rendering from shell + version data | decision at delivery; mass version generation | pre-rendered variant sets from template × feed, uploaded as ads | serving-time personalized composition |
| Variant scale | rows in spreadsheet; up to 15 shells | "mass creative versions in minutes"; 600K+/yr (vendor claim) | "one design, thousands of creatives"; 8k unique ads (vendor claim) | per-user recommendations |
| Reporting | 4 DCO-specific dimensions × campaign metrics | content-/version-/element-level | rendered-image review; SKU/product insights; campaign insights | real-time metrics vs goals |
| Delivery connection | assigned to line items in own DSP/ad server | own ad serving across channels | campaigns published to Meta/Snap/TikTok | own DSP buying |
| Pricing signal | DCO = additional CPM on serving | enterprise platform | platform subscription | managed DSP economics |
| User builds decisioning? | yes (trader/agency configures) | yes (with vendor support) | yes (marketer configures templates/rules) | no (vendor algorithm; advertiser sets goals) |

Cross-product commonalities (Layer B):
1. Creative exists as a parameterized structure (shell/template with variable elements) — 4/4.
2. A data substrate feeds the variables (product/catalog feed, version data, audience/context data) — 4/4.
3. Decision logic (rules and/or learned) selects element values/variants — 4/4 (form varies).
4. Automated variant production at a scale manual production cannot reach — 4/4.
5. Output connects to ad delivery (own serving stack or walled-garden publish) — 4/4.
6. Reporting below campaign level (version/element/product) — 4/4 (granularity labels differ).
7. Live updates without re-trafficking (feed syncs, creative updates to live campaigns) — 3/4 explicit (Adform implied via spreadsheet reuse; Innovid and Hunch explicit).

Divergences (implementation, not Type):
- Assembly timing: serving-time (Adform, RTB House, Innovid decisioning) vs pre-rendered variant sets (Hunch).
- Decision authority: advertiser-configured (Adform, Hunch, Innovid) vs vendor-managed algorithm (RTB House).
- Channel focus: open web + video + CTV (Adform, Innovid, RTB House) vs paid social (Hunch).
- Template authoring depth: code shells ↔ design-tool import ↔ vendor-built.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant

A DCO platform is defined by three jointly-held structures:

1. **Creative as parameterized composition.** The ad is held as a reusable structure (template/shell) with variable elements — image, video, text, offer, CTA, layout — whose values come from outside the design. Remove → fixed pre-made ads; the product becomes a design tool or ad gallery.
2. **Data-driven decision logic over the composition.** Configured rules and/or learned optimization map available inputs (product/catalog data, audience attributes, context such as geo/time/weather, delivery/performance signals) to element values or variant selection. Remove → manual variant production (CMP territory) or generic A/B testing of fixed variants.
3. **Automated variant scale connected to ad delivery.** The system produces tailored ad versions — rendered in advance or assembled at impression time — in volume/freshness unattainable by hand, and connects them to ad-serving/delivery machinery with per-variant tracking. Remove delivery connection → a creative generation tool or owned-channel personalization engine; remove scale → hand-made ads.

Jointly-held is load-bearing:
- 1 alone = template design tool.
- 2 alone = a rules engine / recommendation model with nothing to dress.
- 3 alone = an ad server.
- 1+2 without 3 = creative generation / CMP territory.
- 1+3 without 2 = mail-merge-style versioning without decisioning.
- 2+3 without 1 = audience targeting with no creative structure.

### L1 — Common Mature Structure

- Product/catalog feed ingestion and management (structured feed formats, mandatory field schemas, mapping of custom fields, enrichment/extenders, scheduled syncs, error/warning handling).
- Template authoring surfaces at multiple depths (no-code builders, design-tool import with dynamic layers, developer-coded shells with helper libraries).
- Preview/QA of rendered variants at scale (galleries, flagging, review workflows, share links).
- Audience/context decision dimensions (geo, date/time, weather, audience segments, retargeting signals, impression-level signals, key-values).
- Performance-based optimization (algorithmic selection of best-performing combinations; goal-based self-calibration).
- Reporting below campaign level (version-, element-, content-, product-level breakdowns crossed with delivery metrics).
- Multi-format/multi-channel scaling (sizes, placements, channels from one template).
- Live-campaign creative updates (feed syncs propagate without re-trafficking).

### L2 — Variant / Optional Structure

- Assembly timing: serving-time composition vs pre-rendered variant sets uploaded to a channel.
- Decision authority: advertiser-configured rules vs vendor-managed algorithms (managed service posture).
- Channel focus: open-web display/video/CTV vs paid social vs retail media.
- Vertical catalog schemas: retail products, hotels, flights, destinations, automotive, real estate, streaming.
- Data inputs: first-party behavioral, DMP segments, contextual, weather, inventory/price feeds, GA/conversion data.
- Serving substrate: own ad server/DSP vs publishing to walled gardens vs third-party ad servers.
- Commercial model: CPM uplift on serving vs platform subscription vs managed DSP economics.
- AI enrichment (background removal, color extraction, auto video) — era-current capability layer.

### L3 — Vendor-specific (kept out of final document)

- Adform: "creative shell" terminology; .xlsx version spreadsheet; DynAdsHelper autoWire/addText/addImage/setDemoData; element-ID↔column-name binding; up to 15 shells per dynamic ad; backend returns up to 100 products; dcoEngineId; DCO CPM uplift; four reporting dimensions (Dynamic Ads / Creative Shell / Setup / Version); Adform Signal macros (winning line item, deal ID, media, domain).
- Hunch: Feed Mapper, Extender, Filters, Smart Sets, Catalog Product Video, Autopilot, Figma/PSD direct import, color discovery/orientation detection, hourly/daily/weekly/monthly sync options, error-vs-warning product eligibility rule, catalog replication on Meta.
- Innovid: content-/version-/element-level reporting triad; NIVO AI agents; "single partner" omnichannel DCO claim; vendor-claimed metrics (600K+ creatives/yr, <1 min feed updates, 5x render speed).
- RTB House: deep-learning recommendation engine; "shoppable creative"; self-calibrating goal pursuit; 61%-not-previously-viewed claim; funnel-phase product naming (Quality Traffic, Demand Generation).

## Rejected Findings (anti-overfitting)

- **"Optimization" is NOT definitional.** Adform documents fully rules-based dynamic ads (time/geo/audience rules, no performance-based selection) as DCO. Algorithmic optimization is the mature layer (L1), not the invariant. The Type's name overstates the floor.
- **Serving-time assembly is NOT definitional.** Hunch pre-renders variant sets and uploads them as ads; Adform/RTB House assemble at serving time. The invariant is data-driven decisioning + automated scale, not the timing.
- **Product/catalog feeds are NOT definitional.** Adform's date/geo/audience dynamic ads run without a product feed. Feeds are the dominant substrate (4/4 have them) but one product documents feed-less dynamic ads explicitly → L1, not L0.
- **AI/ML is NOT definitional.** Rules-only DCO satisfies the core; RTB House's deep learning is a philosophy pole.
- **Specific channels are NOT definitional.** Display, video, CTV, social, search-adjacent all appear; none is required.
- **Multi-channel management is NOT definitional.** Hunch is single-channel-family (social) and still clearly the Type.

## Historical / Market-Sample Check (§24 reasoning, conceptual)

- Would older products fit? Early-2010s DCO (element libraries + rules + algorithmic selection served through ad servers) satisfies all three L0 legs without any modern machinery (no AI, no CTV, no social APIs, no cloud dashboards). The core holds.
- Analog ancestor: variable-data printing / mail merge (template + data file → per-recipient personalized pieces) satisfies legs 1–2 at analog level but not leg 3 (no ad-delivery machinery, no delivery-coupled measurement) — correctly the pre-history of the *composition* idea, not of the Type.
- Primitive digital form: query-driven text substitution in search ads (insertion slots filled per query at serving time) fits the legs minimally; not directly sourced in this pass (Google unreachable) — kept conceptual, weak claim.
- Platform-native DCO (walled-garden dynamic ads driven by advertiser catalogs) is a major market realization; direct vendor documentation was unreachable in this environment. Indirect Tier-1 evidence via Hunch's documentation of Meta's catalog requirements confirms the catalog→personalized-ads model. The L0 as defined covers it (catalog = data substrate; platform = decision logic; delivery = walled-garden serving). No platform-native-specific machinery was placed in the core.

## Boundary Findings

- **vs Creative Management Platform (CMP)** — hardest boundary; modern products merge both (Innovid: ad authoring + dynamic ads; Hunch: creative studio + DPA automation; Adform: Studio + dynamic ads). Seam: **who/what decides the composition** — CMP centers on humans producing/managing many finished ad versions at scale (production automation, versioning, brand governance); DCO centers on data+logic deciding the composition per delivery/audience. DCO without decisioning collapses into CMP; CMP without data-driven assembly is static versioning. FLAG for joint review with the CMP leaf.
- **vs Ad Server** — ad server decides *which* ad/campaign to serve (targeting, pacing, frequency); DCO decides *what the ad's content is*. DCO rides on serving infrastructure (own or third-party). Distinct Types; suite overlap common.
- **vs Programmatic Advertising Platform / DSP** — DSP buys impressions; DCO is the creative layer. RTB House is a DSP whose core includes DCO — suite overlap, not identity. Distinct Types.
- **vs A/B Testing Platform** — A/B tests a small set of fixed variants with statistical measurement as the center; DCO continuously assembles/optimizes across a large combinatorial space as part of delivery. Distinct; DCO platforms include testing-like "test and learn" but not as the center.
- **vs Marketing Personalization Platform** — personalizes owned-channel content (web/email/app); DCO personalizes paid ad creative delivered through ad-buying machinery. Distinct.
- **vs Recommendation / Personalization Engine** — recommends products on owned surfaces; DCO uses recommendation-like logic to compose *ads*. RTB House straddles conceptually (recommendation-driven ads) but its output is ad delivery. Distinct.
- **vs Email Marketing Platform** — email merge fields are per-recipient content assembly, but the channel/machinery/optimization loop is owned-channel sending, not ad delivery. Distinct.

## Uncertainties

1. Platform-native DCO (Google Studio/DV360 dynamic remarketing, Meta dynamic ads/Advantage+) could not be verified from primary sources in this environment. The model is inferred from market structure + indirect Tier-1 evidence (Hunch's Meta catalog docs). Precise platform-native mechanics (e.g., exact Meta Advantage+ creative behavior, Google Studio profile mechanics) are deliberately not asserted.
2. Exact decisioning mechanics inside Innovid ("decision" capability) are behind a sign-in-gated help center; only Tier-2 positioning evidence available.
3. Whether "optimization" should be promoted into L0 was resolved as NO based on Adform's rules-only dynamic ads; a vendor with only algorithmic DCO (RTB House) and one with only rules (Adform) both sit inside the Type, supporting the decision — but the market's center of gravity is clearly optimization-augmented.
4. Retail-media DCO (on-site sponsored placements with creative assembly) was not sampled; likely a variant, unverified.
5. The CMP leaf is unprocessed at time of writing; the DCO/CMP seam documented here should be reconciled when that leaf is produced.

## Final Synthesis

A Dynamic Creative Optimization Platform is the advertising-creative decisioning layer: it holds ad creative as parameterized compositions, connects them to data (product/catalog feeds, audience/context signals, delivery/performance data), applies configured rules and/or learned optimization to decide the composition per audience or impression, produces tailored ad versions at a scale manual production cannot reach, and connects those versions into ad delivery with per-variant measurement. The market realizes one Type across four poles — rules-configured inside a DSP/ad server (Adform), decision-centric omnichannel platform (Innovid/Flashtalking), social catalog-automation suite (Hunch), fully algorithmic managed DSP (RTB House) — plus a platform-native pole (walled-garden dynamic ads) verified only indirectly in this pass. The defining core deliberately excludes: performance-based optimization (mature layer, not floor), serving-time assembly (implementation variant), product feeds (dominant substrate, not requirement), AI (era-current), and any specific channel.
