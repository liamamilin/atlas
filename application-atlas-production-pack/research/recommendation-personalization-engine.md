# Research Notes — Recommendation / Personalization Engine

Research date: 2026-09-07

## Research Goal

Understand what a Recommendation / Personalization Engine is as an Application Type: what objects exist inside it, who operates it, how recommendations are produced and delivered, what rules govern them, and where the Type's boundary sits against neighboring Types (Marketing Personalization Platform, Search Platform, A/B Testing Platform, CDP, ML Platform, consumer-facing discovery products).

## Initial Boundary

Working hypothesis at start:

- The leaf sits in Directory section 06 (Marketing, Advertising & Growth), so the Type is a **B2B marketing/commerce technology**, not a consumer-facing product.
- Core purpose hypothesis: given a catalog of recommendable items and behavioral data about users, produce ranked, context-conditioned item suggestions and deliver them programmatically into customer-facing digital experiences (site pages, apps, email).
- Likely confusions:
  - Marketing Personalization Platform (same section; products overlap heavily)
  - Search Platform (same vendors often ship both; query-driven vs query-less)
  - A/B Testing Platform (Target embeds recommendations inside experiments)
  - CDP (data layer vs decision layer)
  - Machine Learning Platform (general ML lifecycle vs packaged recommendation capability)
  - Product Discovery Application (§05.05, consumer-facing) and Personalized Content Feed (§02.08, consumer-facing) — these are surfaces, this is the engine behind them

## Research Questions

1. What are the core objects? (catalog/items, signals/events, strategy/algorithm/recipe, placement/pod, rules, results)
2. How does an operator define a recommendation? (strategy selection, conditions, filters, exclusions, promotions)
3. How are the catalog and behavioral signals ingested?
4. How are results served? (API, widgets, batch/email, on-site vs off-site)
5. What standard strategy families exist across products?
6. How do business rules interact with algorithmic ranking?
7. How is performance measured and attributed?
8. What happens at the edges: cold start, sparse data, empty results, fallback?
9. Where is the boundary vs Marketing Personalization Platform, Search, A/B Testing, CDP, ML Platform?
10. What varies by segment (retail vs media vs B2B) and delivery posture?

## Representative Products

Selected for market representativeness, documentation quality, and spread of product philosophy and customer level:

| Product | Pole | Why selected |
|---|---|---|
| Algolia (Recommend) | API-first developer product from a search vendor | documents models, training, serving API, rules in depth |
| Amazon Personalize | managed cloud ML service (infrastructure pole) | documents datasets/recipes/campaigns/filters/batch in depth |
| Constructor | e-commerce product discovery suite, recommendations module | documents pods/strategies/searchandising/analytics in depth |
| Adobe Target (Recommendations) | enterprise experimentation & personalization suite module | documents criteria/catalog/collections/exclusions/activities; boundary anchor vs A/B testing |

Rejected / unreachable:

- **Dynamic Yield** — intended as the pure-play personalization-platform pole. All three host attempts failed (help.dynamicyield.com transport error; developer.dynamicyield.com transport error; www.dynamicyield.com 403). Abandoned per network rule. No claims made about Dynamic Yield.
- **Bloomreach** — docs.bloomreach.com timed out; developer.bloomreach.com transport error. Abandoned. No claims made.

## Sources

All fetched 2026-09-07. All Tier 1 (official product documentation).

**Algolia**
- Algolia docs index — https://www.algolia.com/doc/
- Algolia Recommend overview — https://www.algolia.com/doc/guides/algolia-recommend/overview
- Set up Algolia Recommend — https://www.algolia.com/doc/guides/algolia-recommend/how-to/set-up
- Refine recommendations with rules — https://www.algolia.com/doc/guides/algolia-recommend/how-to/rules

**Amazon Personalize**
- What is Amazon Personalize — https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html
- How Amazon Personalize works — https://docs.aws.amazon.com/personalize/latest/dg/how-it-works.html
- Amazon Personalize terms — https://docs.aws.amazon.com/personalize/latest/dg/terms.md
- Creating a dataset group — https://docs.aws.amazon.com/personalize/latest/dg/domain-dataset-groups.html
- Filtering recommendations and user segments — https://docs.aws.amazon.com/personalize/latest/dg/filter.html
- Promoting items in real-time recommendations — https://docs.aws.amazon.com/personalize/latest/dg/promoting-items.html

**Constructor**
- Documentation index — https://docs.constructor.io/ and https://docs.constructor.com/llms.txt
- Learn about Recommendations — https://docs.constructor.com/docs/products-recommendations-learn-about-recommendations.md
- Create a recommendations pod — https://docs.constructor.com/docs/using-the-constructor-dashboard-recommendations-create-a-recommendations-pod.md
- Recommendations Searchandising — https://docs.constructor.com/docs/products-recommendations-recommendations-searchandising.md
- Monitor pod performance (Analytics > Recommendations) — https://docs.constructor.com/docs/analytics-recommendations.md
- Learn about Email Recommendations — https://docs.constructor.com/docs/products-cross-channel-offsite-discovery-learn-about-email-recommendations.md

**Adobe Target**
- What is Target Recommendations — https://experienceleague.adobe.com/en/docs/target/using/recommendations/recommendations
- Criteria — https://experienceleague.adobe.com/en/docs/target/using/recommendations/criteria/algorithms
- Recommendations as an offer — https://experienceleague.adobe.com/en/docs/target/using/recommendations/recommendations-as-an-offer
- Exclusions — https://experienceleague.adobe.com/en/docs/target/using/recommendations/entities/exclusions

## Product Observations

Evidence layer A = directly observed in that product's official docs. Layer B = cross-product commonality.

### Algolia (Recommend) — API-first developer pole

Key observations (Layer A):

- **Data inputs**: the searchable index is the item corpus; click and conversion events (keyed by `userToken` × `objectID`) are the behavioral signals. Historical events can be bulk-uploaded via CSV. An events debugger exists for diagnosing event problems.
- **Models** (the strategy unit): Frequently bought together (collaborative filtering over purchase events; relaxed vs strict variants), Related items (collaborative filtering over click/conversion events), Related content (content-based filtering over item attributes — used when interaction data is sparse), Trending items, Trending facets value, Looking similar (image-based, requires no events).
- **Training**: models are created and trained from the dashboard; re-trained once per day automatically; documented minimum/maximum event thresholds per model; training summary shows coverage (share of items with recommendations); preview shows per-recommendation confidence score.
- **Serving**: Recommend API (`getRecommendations`) plus InstantSearch widgets (e.g., `relatedProducts`); request-time parameters include `facetFilters`/`numericFilters` (refinement), `fallbackParameters` (fallback recommendations when the model returns too few), and `limit`.
- **Rules**: if-then rules with conditions (any source item / specific item viewed / subset of source items matching a filter, optional context and timeframe) and consequences (pin items at position, hide items, boost items, bury items, filter items; `sameAsViewedItem` value support). A documented precedence algorithm resolves competing rules; responses can include `appliedRules` for debugging.
- **Plan dependence**: the number of rules per scenario depends on the Algolia plan (no numbers asserted here).
- A/B testing exists as a separate Algolia capability (search A/B testing), not bundled inside Recommend docs.

### Amazon Personalize — managed cloud ML service pole

Key observations (Layer A):

- **Data model**: dataset group (isolated container) holding typed datasets — Users, Items, Item interactions, Actions, Action interactions — each with an Avro schema. Bulk import from CSV in S3 plus real-time events (`PutEvents`). Contextual metadata (device, location) can be attached to events.
- **Recipes** (the strategy unit), grouped: USER_PERSONALIZATION (User-Personalization-v2, Popularity-count), RELATED_ITEMS (SIMS, Similar-Items), PERSONALIZED_RANKING (personalized-ranking, Personalized-Ranking-v2 — re-ranks a supplied collection, e.g., search results), USER_SEGMENTATION (item-affinity, item-attribute-affinity — produce user segments, not item lists), Next-Best-Action (recommends actions, not items).
- **Domain dataset groups**: ECOMMERCE and VIDEO_ON_DEMAND domains with use-case-optimized recommenders (e.g., "Recommended for you", "Frequently bought together", "Customers who viewed X also viewed"; "Top picks for you", "Because you watched X", "Most popular"). Custom dataset groups expose solutions → solution versions (FULL/UPDATE training modes) → campaigns (deployed model with provisioned capacity).
- **Serving**: real-time `GetRecommendations` / `GetPersonalizedRanking` / `GetActionRecommendations` APIs; batch inference jobs (bulk recommendations to S3 — documented for personalized emails) and batch segment jobs (user segments for campaigns).
- **Filters**: named filter expressions (`INCLUDE ItemID WHERE Items.OWNER IN ("in-house")`) applied at request time; filter updates propagate within seconds for streamed events. **Promotions**: a percentage of recommended items must match a promotion filter (e.g., in-house content); promoted items are flagged in the response.
- **Exploration**: some recipes can interleave less-popular/new items (exploration weighted against relevance); impressions data (what was shown) can be recorded implicitly or explicitly.
- **Measurement**: metric attribution reports impact against chosen metrics (e.g., total watch length, click events).
- **Ecosystem**: integrates with Segment (data in), Braze (personalized email out), Optimizely (A/B testing), Amplitude (measurement), Amplify (event capture).

### Constructor — e-commerce discovery suite, recommendations module

Key observations (Layer A):

- **Pods** (the placement unit): a named, ID'd location on a page or page template (Home, PLP, PDP, Cart; top of page, within results, modals, bottom). A page may have multiple pods. Pods have a channel (on-site vs off-site).
- **Strategies** (the algorithm unit), out of the box: Abandoned in cart, Alternative (similar items via co-occurrence), Bestsellers (default 14-day window; customizable 7/14/30), Bundles (frequently bought as a set), Buy it again, Complementary (co-purchase, e.g., toothpaste → toothbrush), Filtered items (inherits browse ranking with request-time filter), Query recommendations (for zero-result pages), Recently viewed, User featured (per-user personalization score), Visually similar items.
- **Conditions**: per-pod hide/slot of specific items or attribute-based item groups.
- **Backfilling**: when a strategy returns too few items, another strategy (default Bestsellers) automatically fills remaining slots; can be disabled by request.
- **Personalization posture**: personalization is on by default across recommendations; can be turned off by request (except User featured, which is entirely personalization-based). Optional toggles: remove converted items; filter same-naming-convention variations.
- **Searchandising rules**: Boost, Bury, Slotting, Blocklisting, Show only; rules attach to one or more pods (up to 5 per rule) with conditions (specific item page or any page where an attribute matches). The Filtered strategy ignores slot/boost/bury (it inherits browse ranking) but honors allow/block lists.
- **Serving**: "Retrieve by pod" API for on-site; Offsite Discovery API for email/SMS/push/social/paid. Email recommendations: pod + notification campaign in the dashboard; ESP integration via data feed templates (generation at send or open time depending on ESP) or HTML snippets (generation at open time); broadcast vs triggered campaign types; documented lead-time and batching guidance for broadcast sends.
- **Analytics**: per-pod impressions, clickthrough rate, add-to-cart rate, top clicked items; attribution; A/B testing module; rule performance reports.
- **Catalog**: items/variations/item groups; JSON/CSV feeds via HTTP/FTPS or REST; platform connectors (Shopify, Salesforce B2C, BigCommerce, commercetools, VTEX, Akeneo, etc.).
- **Behavioral tracking**: beacon/data-attribute instrumentation, identification parameters, success/purchase event tracking, omnichannel personalization.

### Adobe Target (Recommendations) — experimentation suite module

Key observations (Layer A):

- **Positioning**: Recommendations activities are part of Target Premium (not Standard). Recommendations "automatically display products, services, or content that might interest your visitors based on previous user activity, preferences, or other criteria."
- **Entities** (the item corpus): "the items you want to recommend... products, content (articles, slide shows, images, movies, tv shows), job listings, restaurants, and so forth." Ingested via **Feeds** (CSV, Google Product Search feed format, Adobe Analytics product classifications). **Catalog** = the entire entity set; **Collections** = logical buckets (e.g., a category); **Exclusions** = account-wide rule-defined subsets that must never be recommended (discontinued products, seasonal catalogs, inappropriate items, incomplete metadata, fake/QA SKUs).
- **Criteria** (the strategy unit) with a documented taxonomy by algorithm type:
  - Cart-Based: people who viewed these also viewed / also bought; bought these also bought
  - Popularity-Based: most viewed across site / by category / by item attribute; top sellers across site / by category / by item attribute; top by analytics metric
  - Item-Based: people who viewed this viewed that / bought that; bought this bought that; items with similar attributes
  - User-Based: recently viewed items; recommended for you
  - Custom Criteria: uploaded custom algorithm output
- **Recommendation keys**: current item, last purchased item, favorite category, or a custom profile attribute (e.g., "last show added to watchlist").
- **Industry verticals**: Retail/Ecommerce (purchase conversion), Lead Generation/B2B/Financial Services (non-purchase conversion), Media/Publishing (engagement) — the vertical changes which criteria options are offered.
- **Delivery**: **Designs** (row/column/table/grid templates) rendered into **Locations** (page areas) for **Audiences**; delivered via JavaScript snippets across channels, apps, pages, email.
- **Experimentation integration**: recommendations can be inserted as an **offer** inside A/B Test (including Auto-Allocate and Auto-Target) and Experience Targeting activities — test recommendations vs non-recommendation content, test placement, auto-allocate traffic to the best-performing recommendations experience. Offer status states include Results Ready / Results Not Ready / Feed Failure.
- **Promotions**: front promotion and back promotion configurable on a recommendation offer (fixed items at the start/end of the results).

## Cross-product Comparison

| Dimension | Algolia | Amazon Personalize | Constructor | Adobe Target |
|---|---|---|---|---|
| Item corpus concept | index | Items dataset (in dataset group) | catalog (items/variations/groups) | catalog of entities |
| Signal concept | click/conversion events (userToken × objectID) | item interactions events (+ contextual metadata) | behavioral tracking (search/browse/purchase) | visitor behavior (site activity, profile attributes) |
| Strategy unit | model (Frequently bought together, Related items, Trending…) | recipe / recommender (USER_PERSONALIZATION, RELATED_ITEMS, PERSONALIZED_RANKING…) | strategy (Alternative, Complementary, Bestsellers…) | criteria (Cart-Based, Popularity-Based, Item-Based, User-Based, Custom) |
| Placement unit | widget / API call (developer-side) | recommender or campaign endpoint | pod (named page location) | activity + location + design |
| Business rules | rules: pin/hide/boost/bury/filter, conditions, precedence | filters (request-time expressions) + promotions (% of slots) | searchandising: boost/bury/slot/blocklist/show-only + per-pod conditions | collections (inclusion scope), exclusions (account-wide), front/back promotions |
| Fallback behavior | fallbackParameters (filter-based fallback results) | (not observed in fetched pages) | backfilling with another strategy (default Bestsellers) | (not observed in fetched pages) |
| Serving | Recommend API + InstantSearch widgets | GetRecommendations API + batch inference jobs | pod API + offsite/email APIs | JS delivery in activities, across pages/apps/email |
| Batch / email | (not observed in fetched pages) | batch inference jobs (documented for email) | email/offsite pods, ESP integration | email among delivery options |
| Measurement | training coverage, confidence preview; analytics elsewhere | metric attribution reports | per-pod impressions/CTR/add-to-cart, attribution | activity reports; offer status |
| Experimentation | separate A/B testing capability | via partners (Optimizely) | A/B testing module | native: recommendations as offer inside A/B/XT activities |
| User segments | (not observed) | USER_SEGMENTATION recipes → batch segments | Audience Hub (analytics side) | audiences (targeting input, not output) |
| Operator surface | dashboard (models, rules) + API-first | console/CLI/SDK (developer/data-team oriented) | dashboard (pods, rules, analytics) + API | web UI (activities, criteria, designs) |

Layer B findings (cross-product commonality):

1. Every product separates **what to recommend from where to recommend it** — a strategy/algorithm/recipe/criteria object and a placement/pod/location/activity object, bound together at serving time. (B)
2. Every product maintains an **item corpus** distinct from the **behavioral event stream**, with separate ingestion paths for each. (B)
3. Every product exposes a **library of named strategy types** spanning the same families: popularity-based, item-similarity/co-occurrence-based, user-personalization-based, recently-viewed. (B)
4. Every product provides a **business-rule layer** that modifies algorithmic output (boost/bury/pin/slot/hide/filter/exclude/promote). (B)
5. Every product measures recommendation performance (impressions, clicks, conversion-class metrics) and ties results back to the strategy/placement. (B)
6. Strategy families recur with near-identical semantics across products despite different names: "frequently bought together" (Algolia / Personalize / Constructor Bundles-Complementary / Target bought-this-bought-that), "similar items" (Algolia Related / Personalize SIMS / Constructor Alternative / Target viewed-this-viewed-that + similar attributes), "personalized for you" (Algolia via personalization / Personalize User-Personalization / Constructor User featured / Target Recommended for you), "recently viewed" (Constructor / Target; Algolia via session context), "trending/bestsellers/most popular" (all four). (B)
7. Cold-start handling via content/attribute/image similarity exists in at least three products (Algolia content-based + Looking similar; Constructor product inheritance + Visually similar; Target items with similar attributes). (B)
8. Delivery extends beyond the website to email/off-site in at least three products (Personalize batch for email; Constructor offsite/email; Target email delivery). (B)

## Canonical Model

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as this Type:

```text
Recommendable item corpus
  + Behavioral/interaction signals about users and/or items
  → Context-conditioned ranked recommendation computation
  → Programmatic delivery of ranked results into customer-facing digital experiences
```

Four properties:

1. **Recommendable item corpus** — a maintained set of items (products, content, media, actions) that can be suggested. Without it there is nothing to recommend.
2. **Behavioral/interaction signals** — recorded interactions (views, clicks, purchases, watch events) and/or item/user attributes used as the basis of computation. Without signals the output is not a recommendation computation but a static list.
3. **Context-conditioned ranked recommendation** — the output is a ranked item list whose composition depends on the request context (target user, target item, session, cart, audience), not a fixed global list. This is the shared abstraction behind both "recommendations" (item-conditioned) and "personalization" (user-conditioned).
4. **Programmatic delivery into customer-facing experiences** — results are served through an API/endpoint/feed/widget for embedding in sites, apps, or messages. Without delivery it is only an analytics or modeling exercise.

§24 historical check: the item-to-item collaborative-filtering generation of recommenders (catalog + co-purchase co-occurrence + offline computation + serving on product pages) satisfies all four properties with no ML suite, no dashboard, no pods, no experimentation, no email. Older marketing recommenders and self-hosted/open-source engines fit the same four properties. Therefore none of those modern structures belong in L0. Per-user personalization is also NOT in L0: item-conditioned recommendations ("similar items") satisfy the Type without any user model — the invariant is context-conditioning, of which user-conditioning is one pole.

### L1 — Common Mature Structure

Present in essentially all mature modern products; not required for recognition:

- Named strategy/recipe library (popularity, item similarity, co-purchase/complementary, user personalization, recently viewed, trending)
- Placement abstraction binding strategy to page location (pod / activity+location / widget / endpoint)
- Business-rule layer over algorithmic output (boost/bury/pin/slot/hide/filter, exclusions, promotions)
- Fallback/backfill behavior when a strategy returns too few items
- Measurement loop (impressions, CTR, conversion-class metrics, per-placement analytics, attribution)
- Catalog ingestion machinery (feeds, connectors, APIs, bulk upload)
- Event collection machinery (beacon/SDK/API + historical import)
- Cold-start handling via content/attribute/image similarity
- Operator dashboard + developer API as dual surfaces
- Experimentation/testing of strategies and placements
- Cross-channel delivery (email/off-site, batch generation)
- Preview/debug tooling (see what a strategy returns, which rules applied)

### L2 — Variant / Optional Structure

- Delivery posture: standalone API product / commerce-discovery suite module / marketing-experimentation suite module / managed cloud ML service / (structurally: self-hosted or open-source engine — not directly sampled)
- Domain specialization: e-commerce vs media/video vs generic; industry-vertical configuration (Target's verticals)
- Output extensions: user segments/audiences derived from affinity (Personalize USER_SEGMENTATION, Constructor Audience Hub); next-best-action (actions as recommendable objects — Personalize)
- Personalization posture: on-by-default vs opt-in; consent/privacy machinery
- Retail media blending: sponsored/paid items inside recommendation slots (Constructor retail media module)
- Real-time in-session behavioral adaptation vs daily batch retraining cadence
- Integration fabric: CDP/ESP/analytics/experimentation stacks (Segment, Braze, Optimizely, Amplitude)
- Ranking of supplied collections (personalized re-ranking of search results or curated lists — Personalize PERSONALIZED_RANKING)

### L3 — Vendor-specific Structure

(kept out of the final document; examples)

- Algolia: model names and documented numeric thresholds (event windows 30–90 days, per-model min/max event counts, 30-recommendation cap, daily retraining, 0–100 confidence scores, rule precedence algorithm, plan-dependent rule counts)
- Amazon Personalize: ARN-based resources, dataset-group/campaign/solution-version lifecycle, recipe names, promotion percent semantics, filter update timing (seconds for streamed events), free-tier quotas
- Constructor: pod/strategy names (Abandoned in cart, Buy it again, Bundles…), pod-level rule rollout, 5-pods-per-rule limit, email campaign lead time and batching guidance, send-time vs open-time generation per ESP, Proof Schedule onboarding
- Adobe Target: criteria names ("People Who Bought This, Bought That"), industry verticals, designs, host groups/environments, Premium-only licensing, front/back promotions, offer status states

## Vendor-specific Findings

- Target's **industry vertical** configuration (retail vs lead-gen vs media) changing available criteria is product-specific as a mechanism, though the underlying segment split (purchase vs engagement goals) is a plausible market pattern.
- Personalize's **Next-Best-Action** (recommending actions rather than items) is currently product-specific in this sample; treated as an L2 output extension, not a Type feature.
- Constructor's **pod-level searchandising rollout** and its **Filtered strategy ignoring boost/bury/slot** are product-specific implementation details.
- Algolia's **rule precedence algorithm** and **appliedRules debugging** are product-specific implementations of the general "business rules over ML output" pattern.
- Personalize's **exploration** (deliberately interleaving less-popular items) is product-specific as a named feature; exploration-style behavior is a known general technique but was not observed as a named capability elsewhere in the sample.

## Boundary Findings

1. **vs Marketing Personalization Platform (same directory section — sharpest seam).** The recommendation engine's managed object is the **ranked item decision** (which items, in what order, for which context). The marketing personalization platform's managed object is the **experience/segment decision** (which variation of content/experience for which audience segment). Products overlap heavily: Target does both (activities + audiences vs criteria + designs); Dynamic Yield (unreachable, not claimed) is positioned across both. The two leaves are best understood as capability-emphasis slices of a shared market; flag for joint review. Test: if the system's primary output is a ranked item list computed from behavioral signals → this Type; if the primary output is audience-conditioned experience variation → Marketing Personalization Platform.
2. **vs Search Platform.** Query-driven retrieval vs query-less context-conditioned suggestion. Same vendors ship both (Algolia, Constructor), often on shared infrastructure (Constructor: "the exact same personalization signals and graph algorithms as our search engine"; Personalize can re-rank OpenSearch results). Distinct Type because the input (no query), the operator workflow (strategy selection vs query relevance tuning), and the failure modes (zero results vs sparse signals) differ. Test: remove the query → if the system still produces ranked output from context, it is doing recommendation.
3. **vs A/B Testing Platform.** Target embeds recommendations as an offer inside A/B/XT activities: experimentation is the governance/traffic layer, recommendation is the content decision being tested. Distinct Types; the seam is documented from the Target side.
4. **vs Customer Data Platform.** CDP aggregates/identifies customer data for activation; the engine consumes signals and computes item decisions. Documented integrations (Segment → Personalize) confirm the data-in relationship. Distinct Types.
5. **vs Machine Learning Platform / Feature Store / Model Registry.** General ML lifecycle tooling vs packaged recommendation capability. Personalize is the closest neighbor (it is an ML service) but its managed objects are recommendation-specific (datasets, recipes, recommenders, campaigns), not notebooks/pipelines/registries. Distinct Type.
6. **vs Product Discovery Application (§05.05) / Personalized Content Feed (§02.08) / News Aggregator (§02.04).** Those are consumer-facing surfaces; this Type is the B2B engine that powers such surfaces. Test: who logs in — an end consumer (surface) or a merchant/marketer/operator (engine).
7. **vs Ad Server / retail media.** Recommendations are organic content decisions; ads are paid placements decided by auction. The seam blurs where retail media injects sponsored items into recommendation slots (Constructor ships both) — recorded as an L2 variant, not a Type feature.
8. **Capability-level observation:** "personalization" in the leaf name maps to the user-conditioned pole of context-conditioning; "recommendation" maps to the item-conditioned pole and the ranked-list output. The sample shows both poles in every product, supporting one Type rather than two.

## Uncertainties

- The pure-play personalization-platform pole (Dynamic Yield) could not be sampled (all hosts unreachable). Claims about that pole are kept generic; the suite-module and service poles are well documented.
- Bloomreach unreachable; no claims.
- Market-size or category-leadership claims: none made (no evidence fetched).
- Whether the industry term "personalization engine" (as used by analyst categories) always includes recommendation capability was not verified against analyst sources; the document therefore defines the Type from product behavior, not from analyst taxonomy.
- Fallback behavior was observed in two of four products (Algolia fallbackParameters, Constructor backfilling); treated as L1 common rather than universal.
- Batch/email delivery observed in three of four products (not in Algolia's fetched pages); treated as L1 common with product-level variance.
- Historical samples (item-to-item CF era, 2000s marketing recommenders, open-source engines) were reasoned about structurally; the item-to-item CF paper was not fetched, so no precise claims about it are made.

## Final Synthesis

A Recommendation / Personalization Engine is a B2B system whose defining core is: a maintained item corpus + ingested behavioral signals → context-conditioned ranked recommendation computation → programmatic delivery into customer-facing digital experiences. Around that core, mature products add a standard structure: a named strategy library, placements binding strategies to page locations, a business-rule layer over algorithmic output, fallback behavior, a measurement loop, catalog/event ingestion machinery, cold-start handling, dual operator/developer surfaces, experimentation, and cross-channel (email/off-site) delivery. The Type's variants are dominated by delivery posture (API product / commerce suite module / experimentation suite module / managed ML service) and domain (retail vs media). The sharpest boundary is against the Marketing Personalization Platform (ranked-item decision vs audience-experience decision; products straddle); other boundaries (search, A/B testing, CDP, ML platform, consumer discovery surfaces) are clean and documented from product evidence.
