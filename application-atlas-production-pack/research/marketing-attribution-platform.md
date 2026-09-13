# Research Notes — Marketing Attribution Platform

## Research Goal

Understand the software Type placed at directory leaf "Marketing Attribution Platform" (§06 Marketing, Advertising & Growth): applications through which an advertiser/marketing organization determines which marketing touchpoints deserve credit for the conversions it records (app installs, purchases, leads/stages, revenue), by linking recorded marketing interactions to those conversions under an explicit credit-assignment model, and by aggregating that credit into cross-channel views that inform budget and channel decisions. Determine the defining core, the standard capability set, the variant poles, and the boundaries against neighboring Types.

Context from prior passes that this pass must address:

- research/marketing-analytics-platform.md (§06, processed 2026-09-08) pre-flagged the seam to this leaf: "the measurement-modeling layer (credit assignment / aggregate spend-effect modeling) is NOT the center [of marketing analytics]" (Funnel ships Measure [MTA/MMM/incrementality] as a separate product line from its Data Hub; Improvado lists MMM as a use case; 2/4 samples lack it entirely) — joint review recommended when this leaf is processed. This pass discharges that flag from the attribution side.
- STATUS.md Boundary Issues (performance-attribution-platform pass, §08, processed 2026-09-08) recorded an "attribution" naming hazard: the word collides across two unrelated universes — investment portfolios/benchmarks/returns (§08) vs marketing channels/campaigns/conversions (§06) — and recommended the §06 leaf's pass state the mirror-side distinction. This pass discharges that obligation.

## Initial Boundary

Working hypothesis before research:

- The Type is the **advertiser-side credit-assignment application**: the operator is the marketing organization (or its agency); the subject is the organization's own conversions; the deliverable is per-conversion credit allocated across marketing touchpoints/channels and aggregated into cross-channel decision views.
- The reason the Type exists: every ad platform reports only itself and claims full credit for the same conversions; someone must record the journeys, allocate each conversion's credit once under explicit rules, and reconcile the total across channels.
- Likely confusions:
  1. Marketing Analytics Platform (§06, processed) — cross-channel KPI measurement/reporting vs per-conversion credit assignment.
  2. Marketing Mix Modeling Application (§06, unprocessed) — aggregate spend-effect modeling without user-level journeys vs user-level path credit.
  3. Web analytics (GA-class; no directory leaf) — site/app behavior measurement vs marketing credit.
  4. Customer Data Platform / Audience Management (§06) — identity for activation vs identity in service of credit.
  5. Ad platforms' native attribution / Ad Server / DSP (§06) — per-platform self-measurement vs independent cross-channel reconciler.
  6. Performance & Attribution Platform (§08, processed) — same word "attribution", unrelated universe (investment returns).
  7. A/B Testing / Digital Experimentation Platform (§06, processed) — controlled-experiment lift vs observational journey credit.
  8. Marketing Automation / Campaign Management (§06, unprocessed) — execution vs measurement.
  9. Affiliate Network / Affiliate Management (§06) — per-partner referral credit for commission vs whole-mix credit.
- Unknowns going in: (a) is the conversion event definitional or can a product be attribution with only touchpoints; (b) is spend joining part of the core; (c) is de-duplication vs platform credit definitional or a vendor story; (d) do mobile MMPs, e-commerce MTA, and B2B revenue attribution share one core or are they separate Types; (e) how do lookback windows and identity resolution sit in the abstraction.

## Research Questions

1. What is the central object — the conversion, the touchpoint, the journey, the model, the channel?
2. How do conversions enter the system (pixels, SDKs, webhooks, batch files, CRM syncs)? What is a conversion in each sub-market?
3. How do touchpoints enter the system (attribution links, referrers, device IDs, impression pixels, log files, promo codes, surveys)? How are they linked to the converting user?
4. What is an attribution model, concretely? Which models do products ship (rule-based vs data-driven)? Can users switch models, and what happens to reported credit when they do?
5. What role do lookback windows, attribution waterfalls, and view-through attribution play?
6. How does the product relate to the ad platforms' own reported numbers (de-duplication, discrepancy diagnostics)?
7. Where does spend enter, and what efficiency outputs (ROAS/CPA/ROI/CAC) are computed?
8. What are the main interfaces (cross-channel reports, path explorers, configuration surfaces, diagnostics)?
9. Where is the seam vs marketing analytics, MMM, web analytics, CDP, ad platforms, experimentation, CRM?
10. Which capabilities are definitional vs common vs optional vs vendor-specific? Would older/manual implementations (UTM + spreadsheet last-touch joins, coupon-code-per-channel tracking, ad-server click-through conversion tags) still satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier. Three poles of one Type:

| Product | Pole | Customer tier | Evidence tier reached |
|---|---|---|---|
| **AppsFlyer** (appsflyer.com) | mobile-app attribution / Mobile Measurement Partner (MMP): install & re-engagement attribution at app-ecosystem scale, deterministic device-ID methods + platform-adjudicated (SKAN) + probabilistic | enterprise app marketers (brands, agencies, ad networks) | Tier 1 (support KB: "AppsFlyer attribution model" full article + Attribution concepts / Attribution scenarios / Measure & Engage section structure) |
| **Rockerbox** (rockerbox.com) | e-commerce/DTC multi-touch attribution: de-duplicated user-level MTA over a first-party data foundation, incl. hard-to-track offline channels (promo codes, post-purchase surveys, direct-mail matchback, TV postlogs); ships MTA + MMM + incrementality testing as distinct methodologies | mid-market/enterprise DTC brands (Away, Staples, Unilever-class logos claimed) | Tier 2 (root product page) + Tier 1 (help docs: attribution types, touchpoint tracking methods, conversion tracking, spend ingestion, UI views, discrepancies) |
| **Dreamdata** (dreamdata.io) | B2B revenue attribution: account-based journeys from web tracking + CRM, credit assigned to pipeline stages/deals/revenue; 6 attribution models incl. data-driven and enterprise custom models | B2B SaaS/marketing teams (SMB→enterprise), agency partners | Tier 1 (docs: "Overview of Attribution Models" full article + docs structure: Data Hub, Stage Models, Revenue Analytics, Sources, Glossary) |

Rejected/unreachable samples (recorded, no claims made):

- **Northbeam** — e-commerce modeled-MTA candidate; www.northbeam.com and help.northbeam.io both transport-error → dropped after 2 attempts per network rules. The "modeled/probabilistic MTA" sub-pole is therefore evidenced mainly through Rockerbox's modeled multi-touch + synthetic events; assertion strength reduced accordingly.
- **Triple Whale** — e-commerce attribution candidate; help.triplewhale.com transport error, www.triplewhale.com 403 → dropped after 2 attempts.
- **AppsFlyer dev portal** (dev.appsflyer.com attribution-concepts reference) — 404; support KB used instead (Tier 1).
- **HockeyStack / LeadsRx / Wicked Reports / Adjust / Singular** — additional candidates not fetched; the three sampled products already cover the three structural poles (mobile / e-commerce / B2B) and further samples would mostly repeat existing evidence.

## Sources

Fetched 2026-09-08. All direct from official vendor surfaces.

- AppsFlyer support KB root — https://support.appsflyer.com/hc/en-us
- AppsFlyer — "AppsFlyer attribution model" — https://support.appsflyer.com/hc/en-us/articles/207447053-AppsFlyer-attribution-model
- AppsFlyer — "Attribution concepts" section (article index: attribution model, link structure & parameters, lookback windows, device identifiers, organic/non-organic installs, re-attribution window, media source types, assisted installs, loyal user, app-store discrepancies) — https://support.appsflyer.com/hc/en-us/sections/6551394235409-Attribution-concepts
- AppsFlyer — "Measure & Engage" / "Measure paid media" / "Get started" section structure — https://support.appsflyer.com/hc/en-us/sections/6551006275729-Measure-Engage , https://support.appsflyer.com/hc/en-us/sections/6550990672401-Measure-paid-media , https://support.appsflyer.com/hc/en-us/sections/6550753145745-Get-started
- Rockerbox root — https://www.rockerbox.com/
- Rockerbox Help Docs root (full category/article index) — https://help.rockerbox.com/
- Rockerbox — "Attribution types in Rockerbox" — https://help.rockerbox.com/article/079wwge05m-attribution-types-in-rockerbox
- Rockerbox — "Marketing Touchpoints - How We Track" — https://help.rockerbox.com/article/y2ezda94cq-marketing-touchpoints-how-we-track
- Dreamdata Documentation root (full category/article index) — https://docs.dreamdata.io/
- Dreamdata — "Overview of Attribution Models" — https://docs.dreamdata.io/article/tycc6odb2v-attribution-model

Unreachable/unused: docs.rockerbox.com (transport error; help.rockerbox.com used instead), dev.appsflyer.com/hc/reference/attribution-concepts (404), www.northbeam.com + help.northbeam.io (transport errors ×2), help.triplewhale.com (transport error) + www.triplewhale.com (403). No third-party review sites used.

## Product Observations

### AppsFlyer (evidence layer A — official support KB, Tier 1)

**Definition of the act.** "Attribution is the act of determining what motivated (caused) a user to install an app or to perform post-install acts like re-engagement and re-attribution." The attribution result is either a **non-organic media source** (the user interacted — usually impression or click — with a media source) or **organic** (no media-source interaction; "users installing organically aren't attributed at all").

**Definition of the model.** "The Attribution Model is a set of rules, that determine how credit for an event is assigned to touchpoints in conversion paths." Every ecosystem player (app stores, platforms, ad networks, MMPs) has its own model and "counts installs and events differently"; what matters is that rules are "clear and … implemented in a manner that is unbiased", enabling advertisers to optimize campaigns and compare user quality.

**Attributable events.** Install (recorded and attributed after download **and first launch** — the install timestamp is first launch, vs ad networks' engagement time and stores' download time); re-engagement and re-attribution (retargeting context).

**Attribution methods** (documented table): install referrer (Android; the referrer carries the original clicked URL), device ID matching (IDFA/IDFV/GAID/OAID etc.; incl. querying self-reporting networks via MMP APIs on first launch), probabilistic modeling ("uses statistics and is not based on unique IDs… estimates how many installs or engagements followed a developer's own marketing campaigns… The output is a campaign performance report, not an identification of any individual device or user"), preload campaigns (OEM/carrier pre-installs), SKAdNetwork (Apple-adjudicated), Apple Search Ads, deep link (re-engagement only).

**Attribution waterfall.** "Upon a new install, if there is more than one valid engagement, AppsFlyer prioritizes clicks over impressions, and deterministic over probabilistic methods." Preload campaigns get highest priority with longer lookback windows.

**Click-through vs view-through.** Click-through: a click lookback window opens (default 7 days, described as "the industry standard", range 1–30 days); installs within the window are non-organic and attributed; installs after it are organic. View-through: shorter, configurable window (0–24h, 1-day default for ID matching). "In cases where both a click and an impression occur, the click always prevails, as it's an active engagement." Enhanced engagement types (engaged click / engaged view) for selected partners.

**Single credit + assisted installs.** "AppsFlyer fully attributes only one media source per install, usually using the last ad click or the last ad impression (if there were no clicks)." Assisted installs (AKA multi-touch attribution) are installs where a media source "was not the last touchpoint but touched the user before the install … within the attribution lookback window"; assisting networks "are shown as contributors".

**Event attribution & lifecycle.** In-app events attributed to the media source via device ID/AppsFlyer ID. Organic vs non-organic installs. Reinstalls governed by the re-attribution window (90 days default); retargeting reinstalls recorded as re-attribution. App updates not countable as attribution events. App-store discrepancy resolution documented as a standing task.

**Platform structure.** Marketers KB organized as Get started / Measure & Engage (Measure paid media, Redirect & attribute users, Retarget users, Cross-platform measurement, Preserve user privacy) / Analyze & Optimize; per-network configuration guides for dozens of ad networks incl. a China-market section; "Working with agencies" section; user-based cross-platform attribution in Beta.

### Rockerbox (evidence layer A for help docs — Tier 1; layer A for positioning — Tier 2 root)

**Positioning (root).** "The Platform of Record for All Marketing Measurement… a unified measurement platform built on a centralized, SOC2-certified data foundation. By combining MTA, incrementality testing, and MMM…" Three methodologies answer different questions: "MTA provides tactical, campaign-level insights for day-to-day decisions. MMM delivers strategic planning and forecasting for budget allocation. Incrementality Testing validates true channel impact through controlled experiments." "Instead of debating which number is 'right,' Rockerbox shows you how different measurement approaches compare."

**The platform-attribution contrast (root FAQ).** "Platform attribution (Google, Meta, TikTok) shows each platform's performance in isolation, often over-crediting conversions. Rockerbox provides de-duplicated, user-level attribution that reconciles all touchpoints back to a single source of truth across your entire marketing mix." Channels tracked: "clicks and views across digital channels (paid social, search, display, video) and offline channels (CTV, linear TV, direct mail, podcasts) including hard-to-track channels through promo codes and post-purchase surveys." 100+ integrations; warehouse export (BigQuery/Redshift/Snowflake).

**Attribution types (help article).** Four types, toggleable in platform and reporting: **First touch** ("100% of the conversion credit goes to the first touchpoint in the user's path"), **Last touch** ("100% … to the last touchpoint"), **Even weight** ("the conversion is split evenly across each touchpoint… if the user had two touchpoints before converting each would receive 0.5 of the conversion"), **Multi-touch** ("allocates fractional credit to each touchpoint relative to impact in driving to conversion. This is built off your specific data set" — modeled; the Attribution Reports view "will default to Modeled Multi-Touch"). Beyond the pre-built options: Custom Credit Allocation ("redistribute conversion credit across channels"). "Because Rockerbox de-duplicates conversions - each of these attribution types will look different from what you may be used to seeing in-platform, in GA, or even in your own internal attribution model."

**Touchpoint capture methods (help article — the strongest single source).** Nine documented methods, chosen "depending on what's available and best suited for each channel": URL characteristics (utm_source, referrer URL, page URL, vanity URL — search/social/email/affiliate/video); impression-tracking pixels (viewthrough — display/OTT/native); synthetic events ("probabilistically tracked marketing touchpoints for walled gardens" — social/video); log files (event-level ad-server logs for viewthrough); postlogs (linear-TV spot files → "measure lift from an established baseline, and then assign events to users"); address matchback (direct-mail vendor files matched to billing addresses); promo codes (user-entered codes mapped to channels); surveys (user-entered responses mapped to channels); organic (referring domains without paid tracking characteristics).

**Conversion capture (help-doc structure).** Conversion Activity Tracking (onsite pixel; Shopify/GTM/Segment integrations; webhooks; batch files; in-app events; retail data; conversion QA; exclusions — admin users, staging domains); Deduplicating Conversions; Identifying Users; Historical Data and New vs. Repeat Customers; returns ingestion ("Returns - Ingesting and Understanding the Impact"); accounting for 3rd-party purchases (Amazon/Etsy/wholesale).

**Spend.** Dedicated "Ingesting Your Spend" category: Spend Ingestion, API integrations (Google/Microsoft/Meta accounts), batch spend reports from partners; direct-mail spend amortization; use-case guides on ROAS/CPA targets, budget allocation, payback periods, financial forecasting.

**Modeling.** Multi-Touch Attribution (MTA) Model overview + modeling deep dive (data-driven model built off the customer's own dataset); synthetic-event modeling for walled gardens; attribution windows ("lookback window") methodology; "Why Attribution Numbers Change"; historical data revisions (backfills); GA4 ingestion.

**Taxonomy/mapping.** Rockerbox Mapping Hierarchy (channels/vendors taxonomy with change-request guidelines), Unmapped Events, Marketing Classifications; naming-convention maintenance guides.

**UI views (MTA).** Marketing Paths (user paths), Funnel Position, Channel Overlap, Platform-Reported Performance, "Rockerbox de-duplicated view", Cross-Channel Attribution Report, Conversion Comparison, Time Period Comparison. Separate UI families for MMM (channel overview, scenario planner, model comparison) and Testing (geo lift results). Discrepancy FAQ family: "What is Deduplication? Why do Platforms take Full Credit?", "Why are conversion counts in Facebook different than Rockerbox?", "Rockerbox last touch vs. GA last touch", "Discrepancies between Ad Platforms and Rockerbox".

**Use-case guides.** In-channel optimization (placement-level performance, de-duplicated performance targets, heavy-ups/diminishing returns), determining optimal spend by channel, new-channel evaluation, path understanding (channel roles across the funnel, TOF evaluation, influencer impact), budgeting & forecasting, leveraging MTA with MMM.

### Dreamdata (evidence layer A — official docs, Tier 1)

**Definition (help article).** "Attribution models are frameworks used in digital marketing and analytics to assign credit to various touchpoints or interactions in a customer's journey toward a conversion or sale. These models help companies understand which channels, campaigns, or interactions are most effective in driving desired outcomes, such as sales, sign-ups, or other conversions." Purpose: "Optimize marketing budgets… Enhance campaign strategies… Improve ROI."

**Model catalog.** Six models: First-touch, Last-touch, Linear (equal credit; "if there are five touchpoints, each receives 20%"), W-shaped (30% first + 30% last + 30% conversion-touch + 10% middle), U-shaped (40% first + 40% last + 20% middle), Data-Driven ("replace specific business rules with a mathematical algorithm… uses data from all your journeys to dynamically determine which touchpoints influenced a given stage"). Two categories: **Position-Based** (rule-based, "analyze a single journey at a time… fixed, pre-defined set of rules"; advantage: explainability) vs **Data-Driven** ("analyzing all your customer journeys simultaneously… identify patterns across your entire data set, but it comes at the cost of transparency").

**Model switching.** "Within Dreamdata, you can switch between these models to compare their value distribution… As you switch between different models, you will notice that the value attributed across your different channels and sources changes to reflect the new logic." Applied via an attribution-model filter on reports. Custom attribution models (enterprise): "define complex business rules that divide credit based on any combination of event, campaign, channel, source, or position in the customer journey." Attribution Exclusions (exclude specific sessions from models). LinkedIn Impression Attribution (view-through).

**Scope semantics.** "Attribution models can be applied from the first interaction to the first stage of your sales funnel or across your entire funnel… the system always analyzes the touchpoints that occurred before a lead reached a specific stage. We will always calculate the value from the first interaction up to the stage you selected."

**B2B shape.** Video guide prerequisites: "consolidate siloed data into a unified Account-Based timeline and how to handle B2B journeys involving multiple stakeholders"; scope selection by pipeline stage ("measuring from First Touch to MQL"). Contact→company mapping ("How Dreamdata Maps Contacts to Companies"); anonymous traffic linked to companies (Reveal); company journey report; deals; funnel stages report; engagement score. Revenue Analytics: Revenue Reporting, Revenue Segmentation, Revenue Attribution, CAC report, Time to Value. "Understanding: Influenced vs Attributed Leads and Value"; "Understanding the Difference: Conversions vs. Stages"; stage models (e.g., "All Salesforce Opportunities entering specific Stage") with currency handling.

**Data platform.** Sources: paid (Google/LinkedIn/Meta/Microsoft/X/G2/Capterra), CRM (Salesforce/HubSpot/Pipedrive/Dynamics), marketing automation (Pardot/Marketo/Eloqua), Google Sheet imports (cost, events, CAC), custom uploads, Zapier; web tracking with UTM mapping rules; Event Builder; data modelling schedule. Data Hub. Warehouse export (BigQuery/Snowflake/S3/Azure) incl. "Build your own Revenue Attribution report in BigQuery"; BI connections (Looker Studio/Tableau). Glossary: source/channel/event, session, referrer, Monthly Tracked User, Unspecified/Unknown, first- vs third-party cookies; "Understanding changes in historic reporting of attribution".

**Activation side (adjacent).** Activation Hub: Signals, Matched Audiences (Google/Meta/LinkedIn/Microsoft), Conversions APIs (Google Enhanced Conversions, LinkedIn CAPI, Meta Conversions — feeding attributed conversions back to ad platforms), CRM syncs, reverse ETL, webhook syncs.

## Cross-product Comparison

| Dimension | AppsFlyer (mobile) | Rockerbox (e-commerce/DTC) | Dreamdata (B2B) |
|---|---|---|---|
| Conversion of record | app install (timestamp = first launch); re-engagement; re-attribution | purchase (onsite pixel/webhook/batch; returns ingested; 3rd-party purchases) | CRM stage/deal (sign-up, MQL, opportunity creation, won deal); revenue value |
| Journey unit | engagements (clicks/impressions) within lookback window, linked by device ID/referrer | touchpoints across digital + offline channels, linked by user identity | sessions/touchpoints + CRM events on an account-based timeline |
| Touchpoint capture | attribution links, install referrer, device-ID matching, SRN queries, SKAN, probabilistic modeling, preload | URL params/referrers, impression pixels, log files, synthetic events, postlogs, address matchback, promo codes, surveys, organic referrers | UTM-tagged sessions, referrers, ad-platform sources, CRM/MA events, sheet/custom imports |
| Attribution model | rule set per ecosystem player; last ad click/impression fully attributes; assisted installs as contributors | First touch / Last touch / Even weight / Modeled Multi-touch (+ custom credit allocation) | First/Last/Linear/W/U-shaped (position-based) + Data-Driven (+ enterprise custom models) |
| Model switching | fixed model per method; assisted installs shown alongside | toggle between 4 types; default Modeled Multi-Touch | toggle between 6 models; value re-allocates on switch |
| De-dup posture | one media source fully attributed per install (by design) | explicit de-duplication vs platform full-credit claims; platform-reported vs de-duplicated views | single allocation per conversion under the selected model; influenced vs attributed distinction |
| Spend & efficiency | cost aggregation present in platform (not fetched this pass) | spend ingestion (API/batch); ROAS/CPA targets, budget allocation, payback | Ad Spend, ROI, ROAS, CAC reports; sheet-imported cost |
| Organic/unattributed | organic installs (no qualifying engagement) | direct traffic; unmapped events | Unspecified/Unknown; CRM-based source in absence of tracking |
| Diagnostics | app-store discrepancy resolution | discrepancy FAQ family; why numbers change; backfills | historic-reporting changes; why LinkedIn shows 0 opps |
| Outputs | dashboards/reports (not fetched in detail) | cross-channel attribution report, paths, funnel position, channel overlap, exports/warehouse | revenue attribution dashboards, journeys, benchmarks, warehouse/BI export |
| Adjacent methodologies | retargeting measurement; cross-platform (Beta) | MMM + incrementality testing as sibling methodologies | activation (audiences, conversion APIs) as sibling capability |

Convergent observations (layer B, cross-product):

1. All three define attribution as **assigning credit for a recorded conversion to the touchpoints that preceded it** — the conversion is the anchor; the journey is the input; the model is the allocator.
2. All three maintain a **channel/source/campaign taxonomy** that raw touchpoints are mapped into before credit is reported.
3. All three carry an **organic/unattributed bucket** for conversions with no qualifying touchpoint.
4. All three expose **multiple attribution models** (rule-based and/or data-driven) and let the user compare or switch; reported credit changes with the model.
5. All three treat **platform-reported numbers vs the platform's own view** as a standing reconciliation concern (AppsFlyer: each player counts differently; Rockerbox: de-dup vs full credit; Dreamdata: influenced vs attributed, historic-reporting changes).
6. All three integrate **both ad-platform data and the advertiser's own conversion records** (pixels/SDKs/CRM) — the product sits between the two.
7. Spend joining + efficiency ratios (ROAS/CPA/ROI/CAC) documented in 2/3 (Rockerbox, Dreamdata) — common, not universal in fetched evidence.

## Canonical Model

### L0 — Defining Invariant

Three jointly-held structures:

1. **The conversion of record** — a persistent, identified outcome event on the advertiser's own user population (app install, purchase, lead/stage, revenue event) that credit is assigned for. Remove → touchpoint analytics with nothing to explain.
2. **The attributed journey** — recorded marketing touchpoints (clicks, impressions/views, sessions, engagements) captured across channels and linked to the same identified user, preceding the conversion in time. Remove → conversion reporting with no path; credit assignment impossible.
3. **The attribution model** — a selected/configured rule set or statistical model that distributes each conversion's credit across the journey's touchpoints/channels, producing a single reconciled per-conversion allocation that aggregates into channel/campaign/source credit views. Remove → path/journey analytics; "attribution" gone.

Jointly-held is load-bearing: 1 alone = platform-style conversion reporting; 2 without 1 = journey analytics; 3 without 1+2 = a formula with nothing to allocate; 1+2 without 3 = path explorer, not attribution; 1+3 without 2 = credit assigned to nothing.

Note on de-duplication: because the model distributes a fixed credit budget (one conversion) across the journey's touchpoints, the allocation is inherently single-counted — this is the conceptual basis of what vendors market as "de-duplication" vs platforms' full-credit claims. The allocation principle is L0; the anti-platform framing is vendor story.

### L1 — Common Mature Structure

- Spend ingestion joined to credit → efficiency ratios (ROAS/CPA/ROI/CAC) and budget-allocation views (2/3 documented)
- De-duplicated vs platform-reported comparison views + discrepancy diagnostics (Rockerbox explicit; AppsFlyer discrepancy articles; Dreamdata influenced-vs-attributed + historic changes)
- Multiple models incl. data-driven/statistical options alongside rule-based ones (3/3)
- Configurable lookback/eligibility windows bounding which touchpoints qualify (AppsFlyer explicit; Rockerbox documented; Dreamdata uses stage-scope instead — common, not universal)
- View-through/impression attribution (3/3: VTA, impression pixels/log files, LinkedIn impression attribution)
- Conversion-event configuration (definitions, stages, exclusions, QA)
- Channel/source/campaign taxonomy mapping machinery (mapping hierarchy, UTM mapping, media-source types)
- Identity resolution machinery (device IDs, cookies, email, contact→company mapping)
- Organic/unattributed/direct buckets
- Dashboards/reports, scheduled exports, warehouse/BI destinations

### L2 — Variant / Optional Structure

- Sub-market shape: mobile MMP (install/re-engagement conversions; SKAN/platform-adjudicated methods; SRN query APIs; re-attribution windows) vs e-commerce/DTC MTA (offline channels via promo codes/surveys/mail matchback/TV postlogs; returns and 3rd-party purchase handling) vs B2B revenue attribution (CRM stage/deal conversions; account-based journeys; influenced-vs-attributed semantics)
- Identity substrate: device ID / cookie / email / account / company mapping; deterministic-first vs probabilistic/modeled posture
- Sibling methodologies in measurement suites: MMM and incrementality testing (Rockerbox ships all three; Funnel ships Measure separately per the marketing-analytics pass)
- Activation side: audiences/signals and conversion-API feeds back to ad platforms (Dreamdata Activation Hub; Rockerbox CAPIs)
- Model customization depth (custom credit allocation; enterprise custom models)
- New-vs-repeat customer splits; retargeting/re-attribution semantics (mobile)
- Agency/multi-client structures (AppsFlyer agencies section; Rockerbox agency partners; Dreamdata agency partner program)

### L3 — Vendor-specific (research notes only)

AppsFlyer: attribution waterfall specifics (clicks>impressions, deterministic>probabilistic, preload highest), 7-day click LWW default / 1–30 range, 1-day VTA default, engaged click/view types, preload methods (referrer/pai/conf), 90-day re-attribution default, SKAN solution, OneLink/Smart Banners/Smart Script, IDFV test-device registration, SSOT guide, China-market network packs. Rockerbox: synthetic events, postlogs, address matchback, Fairing survey integration, CM360 usage, custom tracking domain (CNAME), pixel source name/account ID, SOC2-certified data foundation, mapping change-request workflow, MTA onboarding timeline (6–8 weeks per FAQ). Dreamdata: stage models, Reveal company identification, engagement score, B2B benchmarks, Analytics Hub + agent, Chrome extension, MTU metric, W/U-shaped exact percentages (30/30/30+10; 40/40+20), enterprise custom-model gating.

## Vendor-specific Findings

- Rockerbox's "de-duplicated vs platform-reported" duality is its central marketing story; the underlying allocation principle is generic, but the dedicated comparison UI views are product-specific.
- AppsFlyer's waterfall and method table are mobile-ecosystem-specific (referrers, device IDs, SKAN, SRNs) — not generalizable to web/B2B attribution.
- Dreamdata's stage models and account-based timeline are B2B-CRM-specific.
- No product in the sample leads with "marketing attribution platform" as a bare label (AppsFlyer: mobile attribution/MMP; Rockerbox: unified measurement platform; Dreamdata: B2B revenue attribution / data hub) — the referent is stable but naming drifts toward "measurement".

## Boundary Findings

1. **vs Marketing Analytics Platform (§06, processed)** — seam = per-conversion credit-assignment machinery over user journeys vs cross-channel KPI measurement/reporting on consolidated data. The sibling pass's own evidence supports the seam (Funnel ships Measure [MTA/MMM] as a separate product line; Improvado lists MMM as a use case; 2/4 samples lack modeling). Overlap zone: attribution platforms also report channel performance and ingest the same sources; analytics platforms may bolt on attribution modules. Removal tests: remove the model/journey from an attribution platform → it collapses into a marketing analytics platform; add per-conversion credit allocation to an analytics platform → it grows an attribution product. Keep-both ratified from this side.
2. **vs Marketing Mix Modeling Application (§06, unprocessed)** — user-level journey credit vs aggregate time-series spend-effect modeling without user identity. Rockerbox ships MTA and MMM as distinct methodologies with distinct onboarding tracks, UI view families, and documentation categories (self-evidence that the market treats them as different deliverables). Flag left for the MMM pass; joint review recommended.
3. **vs Web analytics (GA-class; no directory leaf)** — site/app behavior measurement vs marketing credit assignment. GA-class last-click conversion reports overlap the attribution surface, but the center differs (behavior analytics vs cross-channel credit reconciliation). Consistent with the marketing-analytics pass's treatment (web analytics as per-channel baseline and data source).
4. **vs Customer Data Platform / Audience Management (§06)** — identity resolution for activation (audiences out) vs identity in service of credit assignment. Attribution platforms consume identity; CDPs produce audiences. Dreamdata's Activation Hub (audiences, conversion APIs) is the adjacent pole inside an attribution product.
5. **vs ad platforms' native attribution / Ad Server / DSP (§06)** — independent cross-channel reconciler vs per-platform self-measurement. Rockerbox's FAQ states the contrast explicitly ("Platform attribution shows each platform's performance in isolation, often over-crediting conversions"); AppsFlyer's framing ("each of the players… have their own attribution models… what's important is… unbiased" rules) is the same independence argument from the mobile side.
6. **vs Performance & Attribution Platform (§08, processed)** — DISCHARGES the naming-hazard obligation: the word "attribution" names two unrelated universes. Investment attribution distributes portfolio returns across holdings/factors relative to a benchmark (§08; users: asset managers, performance analysts). Marketing attribution distributes conversion credit across marketing touchpoints (§06; users: marketers). No shared objects, users, or workflows; the mirror-side distinction is recorded here and in the final document's Related Types.
7. **vs A/B Testing / Digital Experimentation Platform (§06, processed)** — observational journey credit vs controlled-experiment lift. Incrementality testing (geo lift, holdouts) is the causal sibling methodology; Rockerbox ships it as a separate methodology with separate onboarding — adjacent, not the same Type.
8. **vs Marketing Automation Platform / Marketing Campaign Management (§06, unprocessed)** — execution (sending campaigns) vs measurement (crediting outcomes). Attribution platforms ingest campaign data; they do not run campaigns.
9. **vs Affiliate Network / Affiliate Management Platform (§06)** — per-partner referral credit for commission settlement vs whole-mix credit assignment. Affiliate networks are a credit source ingested by attribution platforms (Rockerbox integrates Impact/Rakuten/CJ/Partnerize); the affiliate platform's center is partner/commission management.
10. **vs CRM / Lead Management (§07)** — attribution outputs feed CRMs and CRMs hold journey history as activity records, but the credit-allocation machinery is not the CRM's center. Dreamdata's CRM syncs (inbound stages/deals, outbound CRM-based source fallback) illustrate the interlock.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native, or manual implementations still fit the L0?

- UTM-tagged links + a spreadsheet joining orders to last-touch source: conversion (order row) + linked touchpoint (last UTM) + credit rule (100% last touch) — satisfies the core. No cloud/AI/multi-touch required.
- Ad-server click-through conversion tags with fixed windows (pre-MTA era): conversion + click journey + last-click rule — satisfies.
- Coupon/promo-code-per-channel redemption tracking (print/radio era): code use as the linked touchpoint, 100% credit to the mapped channel — satisfies (Rockerbox still ships promo codes as a first-class capture method for offline channels).
- Call tracking "which ad drove the call" (per-call credit): satisfies for the call-conversion case.
- Historical check **passed**: nothing cloud-, AI-, or multi-touch-specific is in the core; multi-touch/data-driven models are era-current L1/L2, not definitional.

## Uncertainties

- **E-commerce modeled-MTA breadth**: Northbeam and Triple Whale unreachable (transport errors/403); the modeled/probabilistic MTA sub-pole is evidenced through one product (Rockerbox modeled multi-touch + synthetic events). Claims about that sub-pole are held at single-product strength.
- **AppsFlyer cost/ROAS reporting** not fetched this pass; spend-joining is held at 2/3 products (common, not universal).
- **Lookback-window universality**: explicit in AppsFlyer and Rockerbox; Dreamdata's fetched docs describe stage-scope ("first interaction up to the stage") without a lookback-window parameter — windows held as common implementation, not invariant.
- **Pricing/packaging**: no Tier-1 evidence fetched; nothing asserted.
- **Mobile fraud/verification**: not fetched; not asserted.
- **Dreamdata data-driven model internals**: algorithm details live in an article not fetched; described only at the documented level (algorithm over all journeys, less explainable).

## Final Synthesis

A Marketing Attribution Platform is the advertiser-side credit-assignment application. Its defining core is three jointly-held structures: the conversion of record (identified outcome event — install, purchase, stage, revenue), the attributed journey (cross-channel touchpoints linked to the same identified user preceding the conversion), and the attribution model (rule-based or statistical machinery distributing each conversion's credit across the journey, aggregating to channel/campaign/source views). Everything else — spend joins and efficiency ratios, de-dup vs platform-reported views, lookback windows, identity-resolution machinery, activation feeds, MMM/incrementality siblings — is standard capability or variant structure. The Type spans three stable sub-market shapes (mobile MMP, e-commerce/DTC MTA, B2B revenue attribution) that share the core and differ in conversion semantics, capture machinery, and identity substrate. The historical check passes: last-touch spreadsheet joins, ad-server conversion tags, and coupon-code tracking all satisfy the core without any modern machinery.
