# Research Notes — Shopping Search Engine

## Research Goal

Understand the Shopping Search Engine as an Application Type: its defining structure, how real products implement it, how shoppers and merchants work with it, and where its boundaries lie against neighboring Types — especially Shopping Comparison Platform (§05.05 sibling, processed, which carries a joint-review flag against this leaf), General Web Search Engine (§02.02, processed), Vertical Search Engine (§02.02 sibling, unprocessed), Metasearch Engine (§02.02, unprocessed), Online Marketplace (§05.02, unprocessed), Product Discovery Application (§05.05, processed), and Deal Discovery Platform (§05.05 sibling, unprocessed).

## Initial Boundary

- Leaf: **Shopping Search Engine** (§05.05 Shopping Discovery; siblings: Product Discovery Application, Shopping Comparison Platform, Deal Discovery Platform).
- Working hypothesis before research: a search engine whose corpus is products and offers from many sellers — the shopper types a query and receives purchase-shaped results (product/offer cards with price, seller, availability) that lead out to merchants to buy. The classic "comparison shopping engine" family, today mostly realized as shopping tabs inside general search engines plus standalone shopping-search destinations.
- Nearest confusion risks:
  - Shopping Comparison Platform: query-first retrieval vs comparison-centered offer set on a persistent product record (the sibling pass's proposed seam — this pass must discharge or refine it).
  - General Web Search Engine / Vertical Search Engine: narrowed corpus + domain-shaped results vs the open web.
  - Metasearch Engine: market literature sometimes classes comparison shopping engines as metasearch; the owned-corpus question decides.
  - Online Marketplace: routing to sellers vs hosting the transaction.
  - Product Discovery Application: query-driven vs query-independent browsing.
- Prior pass context: `research/shopping-comparison-platform.md` §Boundary Findings flagged joint review with this leaf and named Google Shopping as the market's center-of-gravity case (unreachable there).

## Research Questions

1. What is the defining act — what does the shopper do first, and what comes back?
2. What is the corpus — where do products/offers come from, and does the platform own a persistent ingested corpus or aggregate at query time only?
3. What is the unit of results — offer, product, or web document — and what attributes does a result carry?
4. How are results ranked (relevance vs price vs commercial performance), and what sorting does the shopper control?
5. How does the commercial loop work (merchant feeds, CPC, ads, CSS/reseller ecosystems), and where does the loop end (outbound click vs anything else)?
6. What consumer-side auxiliaries exist (categories, filters, deals, identity keys), and which are definitional vs additive?
7. Where are the boundaries vs the seven neighboring Types listed above?
8. Historical check: does the definition hold for the founding-generation comparison shopping engines and for regional / feed-era / search-embedded realizations?

## Representative Products

Selected for market representation, documentation completeness, different product philosophies, and different market positions:

| Product | Market position | Philosophy | Reachability |
|---|---|---|---|
| **Kelkoo / Kelkoo Group** (EU, founded ~1999 per self-documented "more than 25 years of ecommerce experience") | European shopping search engine that now also operates as a shopping-ads network and API provider | the shopping search engine documented as machinery: merchant feeds in, query-driven search out, CPC monetization, distribution to third-party surfaces | ✅ rich (corporate site, Help Center: advertiser product-data docs, publisher Shopping API docs incl. full offer model) |
| **Shopping.com** (US, eBay-owned) | classic US comparison-shopping engine, feed-era | provider-sourced offer data keyed to item records; thin consumer UI preserved as-is | ✅ medium-thin (home, full category taxonomy, category search results with offer items) |
| **Microsoft Bing Shopping** (global, search-embedded) | shopping vertical inside a general search engine | query-addressable shopping tab beside Web/Images/Videos/Maps; web-results fallback | ✅ thin (vertical entry surface; results page geo-unreachable from research environment) |

Market anchors used qualitatively (unreachable this pass): Google Shopping (support.google.com and developers.google.com both timed out — second consecutive pass with Google properties unreachable; no claims made about its internals), Microsoft merchant-side docs (404), Shopzilla (empty response), Kelkoo consumer sites (403), plus the sibling pass's unreachable set (idealo, Prisjakt, camelcamelcamel, Yahoo Shopping, PriceGrabber).

## Sources

Research date: 2026-09-07. All observations below are Evidence Layer A (directly observed on the fetched page) unless marked B (cross-product) or C (canonical inference).

- Kelkoo Group — https://www.kelkoogroup.com/ (corporate home), https://docs.kelkoogroup.com/ (Help Center), https://docs.kelkoogroup.com/for-advertisers/product-data (advertiser product-data section), https://docs.kelkoogroup.com/for-publishers/shopping-api-search (Shopping API Search section), https://docs.kelkoogroup.com/for-publishers/shopping-api-search/search-offers/offer-search , .../offer-search-model , .../offer-search-request , .../offer-search-result-sort
- Shopping.com — https://www.shopping.com/ (home), https://www.shopping.com/taxonomy.html (Site Index), https://www.shopping.com/search.html?c=Electronics~~1_11000000 (category search results)
- Bing — https://www.bing.com/shop (shopping vertical entry surface)

## Product A — Kelkoo / Kelkoo Group (Evidence Layer A)

### Positioning (corporate home)
- "Kelkoo Group connects advertisers with shoppers who are ready to buy through intelligent optimisation and a trusted global shopping network. With 25 years of experience…" (founding-generation vintage, self-documented).
- "Reach high-intent shoppers and protect margins across Google, Bing and our Kelkoo Group Shopping Network." "Access Google and Bing Shopping through our CSS" — direct evidence of the CSS (Comparison Shopping Service) ecosystem around search-embedded shopping properties.
- Scale claims (marketing figures — recorded as claims): 10k+ advertisers, 29 markets, €500m+ sales generated annually.
- Advertiser products: Performance Flex ("outcome-driven dynamic pricing… prices every click based on its real conversion potential" — CPC pricing machinery) and Advance (Shopping Ads management on Google and Bing).
- Publisher program exists as a separate pole (publisher.kelkoo.com, sign-up/login).

### The shopping search engine as machinery (Help Center)
- **Supply side (For Advertisers)**: Product data section — Product data feed, Product data specifications, Crossed Prices and Sales (rules for strikethrough/original pricing), FTP feed upload, feed FAQ, feed plugin suggestions; Kelkoo sales tracking (conversion attribution back to the engine); Merchant Center (advertiser console); Merchant Statistics API.
- **Demand/distribution side (For Publishers)**: "You want to provide a search engine to your end users but you don't have the ability or will to store all KelkooGroup offers and build your own search engine. In this case, you can benefit from our APIs that will do the job for you." — the engine holds the offer corpus; third parties consume query-driven search over it.
  - **Shopping API Search** (`/search/offers`): simple full-text search via a `query` parameter; rich applications via facets, filters, sort, pagination; "Need a large number of offers → NO — … use Offer feeds" (query-time retrieval explicitly distinguished from bulk export; pagination window capped, with the cap raisable via account contact).
  - **Offer model** (full documented result unit): `offerId`, `title`, `description`, `country`, `lastUpdateDate`; price machinery — `price`, `priceWithoutRebate`, `rebatePercentage`, `rebateEndDate`, `monthPrice` (installment), `deliveryCost`, `totalPrice` (explicitly "price+deliveryCost"), `priceDiscountText`, `currency`, `ecotax`; fulfillment — `availabilityStatus` (enum incl. in_stock / stock_on_order / pre_order / available_on_order / check_site / not_in_stock / out_of_stock), `timeToDeliver`; `condition` (enum incl. new / refurbished / used / download / preregistered); identity — `codeEan`, `codeGtin`, `codeMpn`, `codeSku`, `productId` + `productPopularity` (offers attached to a product entity); commercial keys — `brand`, `merchant` (id, name, logo, `websiteId` with documented 1:n merchant-to-domain relation), `sellerName`, `merchantProvidedCategory` vs platform `categoryId`/`categoryName` (+ `googleProductCategory` mapping field); content — images, `features` (category-dependent dynamic attributes); monetization — `goUrl` ("URL to be used by the publisher to monetize the offer", a tracked redirect), tracked landing URLs, `estimatedCpc` / `estimatedMobileCpc` ("Estimated revenue the publisher can earn for a lead on the offer"); quality flags — `flagOffensiveContent`, `flagGreenProduct`, `greenLabel`, `ethicalType`, `flagSaleEvent`, `performanceScore`.
  - **Ranking semantics**: "If not defined, the sort is done on the relevancy on `query`" — relevance-to-query is the default ordering; `sortBy=price` (asc/desc) is an explicit option; `topOffers` returns offers sorted by performance score and explicitly overrides query relevance ("use of query parameter should be avoided when requesting top offers") — a query-independent, performance-ranked mode for ads-style placements.
  - **Facets/filters**: faceting and filtering on price, totalPrice, rebatePercentage, brand, merchant, category, condition, EAN/GTIN, dynamic category features; continuous fields bucketed dynamically.
  - **Traffic taxonomy** (`publisherTrafficType` values): `searchengine`, `pcw` (Price Comparison Website), `placss` (PLA CSS), `browserui`, `browserextension`, `cashback`, `coupons`, `bnpl`, `classified`, `content`, `displaynative`, `emailmarketing`, `influencer`, `mediabuyer`, `programmaticplatforms`, `publishernetwork`, `retargeting`, `socialmedia`, `toolbar`, `domain`, `internal`… — a documented enumeration of the surfaces through which shopping-search offers reach shoppers, with search engines and price-comparison websites listed as distinct traffic classes.
  - **Reporting**: Reporting API, Publisher Center, click/lead tracking parameters (publisherClickId, subId/subName, custom parameters).

## Product B — Shopping.com (Evidence Layer A, medium-thin)

- Self-label (page title): "Shopping Online at Shopping.com | Price Comparison Site".
- **Category taxonomy** (Site Index, /taxonomy.html): full tree — Home & Garden, Office Supplies, Gifts/Flowers/Food, Automotive, Electronics, Pet Supplies, Health & Beauty, Toys & Games, Babies & Kids, Clothing & Accessories, Appliances, Computers & Software, Jewelry & Watches, Books & Magazines, Music, DVDs & Videos, Sports & Outdoors, Musical Instruments, Video Games. **Every category page is a search URL** (`/search.html?c=<category>`): browsing is implemented as pre-formed queries.
- **Category search results** (Electronics): each result is an **offer item** — URL pattern `/item.html?offer=true&id=…&provider=N` where `provider` distinguishes data sources (provider=0 items attributed to eBay; provider=1 to another feed; provider=3 to a third) — offers sourced from multiple provider feeds, with **merchant attribution shown per result** (eBay, Garage Giant). Condition language ("Condition is used but in good shape", "pre-owned… professionally inspected") appears in result descriptions; pagination present.
- Top Products and Top Deals sections exist as secondary surfaces (sibling pass observed /topProducts.html; /topOffers.html linked from home).
- Content quality is thin (feed-era, marketplace-heavy sourcing); no help center reachable. Used as structural evidence of the offer-result model, provider-feed supply, category-as-search entry, and classic positioning.

## Product C — Microsoft Bing Shopping (Evidence Layer A, thin — entry surface only)

- The shopping vertical is **query-addressable**: `/shop?q=<query>`; the page presents itself inside the search engine's vertical navigation (Web / Images / Videos / Academic / Dict / Maps / Flights / Shopping) — shopping is a sibling vertical of the search engine, one tab among the corpus-narrowed views.
- Positioning (page title): "Shop Online, Find Deals, and Compare Prices | Microsoft Shopping" — deals and price comparison named in the vertical's own framing.
- **Empty state**: with no query, "No shopping results found for … See web results for … instead" plus "Popular shop suggestions" (pre-formed shopping queries: School bags, Shoes, Tablets, Laptops…). The fallback-to-web-results behavior documents the relationship: the shopping vertical is a narrowed, commerce-specific corpus over/next to the general engine, not the same result set.
- **Market scoping observed live**: fetches from the research environment were routed to the CN market (国内版), where the shopping vertical is not served and queries fall back to general web results — the vertical's availability is market-dependent (geo-scoped deployment).
- The results page itself could not be observed (geo-unreachable from this environment; two attempts); no claims made about its result layout, filters, or consumer features.

## Cross-product Comparison

| Dimension | Kelkoo Group | Shopping.com | Bing Shopping |
|---|---|---|---|
| Defining act | full-text query over the offer corpus (`query` param); relevance default | category tree resolving to search URLs; results = offer items | query-addressable shopping vertical (`/shop?q=`) |
| Corpus | own ingested offer corpus ("store all KelkooGroup offers") fed by merchant data feeds | offer items sourced from multiple provider feeds (provider=0/1/3), marketplace-heavy | narrowed shopping corpus with fallback to web results when empty |
| Result unit | offer (complete documented model: price machinery, availability, condition, identity codes, merchant, brand, features, images) | offer item (title, description fragment, merchant attribution, condition in text) | (not observable from research environment) |
| Result attributes | price/rebate/totalPrice/delivery/installments, availabilityStatus enum, timeToDeliver, condition enum, EAN/GTIN/MPN/SKU, product entity + popularity, merchant identity, category mapping | merchant attribution, condition language, item ids | positioning names "Deals" and "Compare Prices" |
| Ranking | relevance-to-query default; price sort optional; performance-scored top-offers mode | (feed-order; not documented) | (not observable) |
| Purchase routing | tracked `goUrl` redirect per offer ("URL to be used by the publisher to monetize the offer") + estimated CPC per offer | item pages keyed to provider offers; merchant attribution (eBay) | (not observable; positioning implies seller routing) |
| Commercial model | CPC click pricing (ML-priced clicks), CSS reselling of Google/Bing shopping, sales tracking, statistics APIs | feed/provider model (eBay-owned) | search-engine advertising ecosystem (not directly documented this pass) |
| Distribution | Shopping API (search + feeds) powering third-party publishers; publisherTrafficType taxonomy of surfaces | consumer site only (legacy) | embedded in the general search engine |
| Scope | 29 markets claimed; country dimension in the offer model | US | market-dependent availability (live-observed geo fallback) |

Evidence Layer B (cross-product commonality, 2–3 products): query as the entry act (query parameter, query-shaped category URLs, query-addressable vertical); offer as the result unit with merchant attribution; multi-source offer supply (merchant feeds / provider feeds); purchase routing out to sellers (tracked monetized URLs / provider item pages); category taxonomy as the query-adjacent browse structure; deal/promotional layer (rebate fields and sale flags / Top Deals / "Deals" in positioning); country/market scoping.

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately minimal)

```text
Shopper query (query-first entry)
└── Multi-seller offer corpus (product/offer records sourced from many independent sellers)
    └── Purchase-shaped results (offer results carrying commerce attributes)
        └── Purchase handoff (results lead to the seller to buy)
```

Removal tests:
- Remove the query-first entry → a browsable catalog/inspiration surface (Product Discovery Application) or a persistent-record comparison platform; the search act is what makes this Type an engine.
- Remove the multi-seller corpus → a single store's site search (a storefront capability), not a shopping search engine.
- Remove purchase-shaped results (offers with price, seller, availability instead of web documents) → a general web search engine.
- Remove the purchase handoff → a shopping data service with no shopping loop; the engine exists to deliver buyers to sellers.

Historical check (§24): the founding generation self-documentation supports the core — Kelkoo states "more than 25 years of ecommerce experience" (founding-era vintage ~1999), and Shopping.com still runs the feed-era structure (provider-keyed offer items, category-as-search) unchanged from the classic comparison-shopping-engine generation. The core (query → multi-seller offers → click-out) predates the modern ads/CSS/API layers, which sit on top as additive machinery. Regional single-market engines and feed-era implementations fit the core without any modern feature. (Specific 1990s products beyond these self-documentations are recalled qualitatively, not verified live this pass.) Search-embedded realizations (Bing observed; Google structurally) satisfy the same core with a different packaging.

### L1 — Common Mature Structure

- **Category taxonomy + category browse that resolves into search** (category pages implemented as pre-formed queries; categories usable as result facets/filters).
- **Offer-level result attributes**: price with rebate/crossed-price machinery (original price, rebate %, rebate end date, promotional text), delivery cost and time-to-deliver, availability status, condition (new/used/refurbished/download), installment pricing, currency, images, merchant-provided vs platform-normalized category, brand.
- **Product identity layer**: standard product codes (EAN/GTIN/MPN/SKU) and a product entity beneath the offer layer (offers attached to products; popularity as a ranking signal).
- **Merchant attribution**: seller/merchant identity (id, name, logo, per-domain identity) shown on results.
- **Ranking + re-sorting**: relevance-to-query as the default ordering, with shopper-chosen re-sorting (documented: price asc/desc) and filter/facet refinement on commerce attributes.
- **Merchant-side supply chain**: product data feeds with formal specifications, upload channels, pricing-sales rules (crossed prices), an advertiser console, conversion/sales tracking, and statistics/reporting APIs.
- **Per-click commercial model**: tracked outbound monetized URLs per offer, estimated CPC per offer/device, performance-scored placement modes.
- **Distribution beyond the owned site**: search/offer APIs and feeds consumed by third-party surfaces (publisher networks, browser tools, cashback/coupon sites, content sites) — the engine as retrievable infrastructure.
- **Deal/promotional layer**: sale-event flags, rebate windows, top-deals surfaces.
- **Market scoping**: country dimension on the corpus; market-dependent availability and per-market deployments.

### L2 — Variant / Optional Structure

- **Packaging**: search-engine-embedded shopping vertical (Bing observed; Google Shopping structurally, unverified internally) vs standalone shopping-search destination (Shopping.com; Kelkoo consumer sites) vs headless/network form (APIs and feeds powering third-party publishers, CSS reselling).
- **Supply model**: merchant feeds vs provider/aggregated feeds vs marketplace-sourced offers (eBay observed as a dominant provider at one product).
- **Commercial posture**: pure CPC performance network vs classic destination-site monetization vs engine-as-plumbing for affiliate/CSS distribution.
- **Consumer-feature depth**: thin feed-era UI vs rich consumer tab (unverified in the reachable sample for the modern poles).
- **Regional scope**: single-market vs multi-market networks.

### L3 — Vendor-specific (stays here, not in the final document)

- Kelkoo: exact enum values of availabilityStatus/condition; pagination caps (pageSize < 100, page×size ≤ 500, raisable); `fieldsAlias` minimal/all; topOffers conflict rules; publisherTrafficType value list; Performance Flex / Advance product names; JWT auth; `googleProductCategory` mapping field; FTP feed upload; corporate scale claims (10k+ advertisers, 29 markets, €500m+).
- Shopping.com: item id formats (`v1-…`), `provider=0/1/3` feed keys, `offer=true` URL parameter, /taxonomy.html /topProducts.html /topOffers.html URLs.
- Bing: FORM parameters, 国内版/国际版 market toggle, "Popular shop suggestions" query seeds, exact fallback wording.

## Vendor-specific Findings

See L3. Additionally: Kelkoo's corporate evolution (consumer engine → performance-marketing group operating CSS access to Google/Bing Shopping plus API distribution) documents a market-wide structural fact — shopping search engines increasingly sell their retrieval machinery (feeds, search APIs, CPC plumbing) as infrastructure, not only as a destination. This is a business-model evolution, not a change to the defining core.

## Rejected Findings

- "A shopping search engine is just a general search engine with shopping ads" — rejected: the corpus is not the web. The result unit is an offer/product record sourced through merchant/provider feeds, with commerce attributes and purchase routing; the general engine's results are web documents. The observed fallback behavior (shopping vertical empty → web results) shows the two corpora are distinct systems that interoperate.
- "Shopping search = metasearch" — rejected: the engine ingests and stores its own offer corpus from merchant feeds ("store all KelkooGroup offers"); results are assembled from this owned corpus at query time. Metasearch combines other engines' result lists and owns no corpus. The persistent-owned-corpus test separates the Types.
- "The Type is defined by the comparison offer table" — rejected as the defining core: the price-led aligned offer table on a persistent product record is the Shopping Comparison Platform's center (sibling pass). At the search side, relevance-to-query is the documented default ordering with price-sort as an option. Where the persistent product record with its aligned offer table becomes the center of the product, the product is drifting to the sibling Type.
- "Hosted checkout is part of the Type" — not observed in the reachable sample; purchase handoff to the seller is the documented pattern (tracked outbound URLs). No claims made about search-embedded poles' purchase-assist features.
- "Consumer conveniences (price alerts, saved items, price tracking) define the Type" — not directly documented in the reachable sample this pass; excluded from standard capabilities rather than asserted from memory.

## Boundary Findings

### vs Shopping Comparison Platform (§05.05, processed) — joint-review flag DISCHARGED from this side

- The sibling's proposed seam (query-first retrieval across sellers vs comparison-centered offer set on a persistent product record) is **confirmed and evidenced from this side**:
  - Ranking semantics: the sampled engine documents **relevance-to-query as the default ordering**, with price-sort as an explicit shopper option; the sibling's products document price-first offer tables as their center ("lowest price first" ranking rules). The retrieval surface and the comparison surface organize results by different defaults.
  - Result assembly: the sampled engine documents query-time retrieval explicitly distinguished from bulk corpus export (search vs feeds, pagination-capped) — results are answers to queries; the sibling's products center a persistent product record whose offer table survives between visits (price history, alerts presuppose it).
  - The market's own vocabulary separates the surfaces: the sampled engine's traffic taxonomy lists `searchengine` and `placss` (shopping-ads/CSS) traffic as distinct classes from `pcw` (Price Comparison Website) traffic.
- Center-of-gravity test: shopping search engine's primary surface = the query and its result list; comparison platform's primary surface = the product record and its aligned offer table. Products commonly do both (a search leads to a product page with offers; a comparison site has a search box) — the center decides.
- Google Shopping remains unreachable (support.google.com and developers.google.com timed out, second consecutive pass) — its placement (search-embedded shopping vertical, the market's center-of-gravity case) is structural knowledge, but no internal claims are made; the discharge rests on the sampled engine's documented mechanics, not on Google evidence.
- Keep-both ratified; the sibling's document already carries the seam; this document cross-references it.

### vs General Web Search Engine (§02.02, processed)

- Same interaction loop (query → ranked results), different corpus and result unit: offers/products from many sellers with commerce attributes and purchase routing vs web documents with snippets and outbound references. The processed pass's family framework (primary output = ranked outbound reference list; defining act = single-corpus algorithmic ranking) is consistent from this side — with the corpus narrowed to commerce and the result unit shaped for purchase.

### vs Vertical Search Engine (§02.02, unprocessed) — flag for that pass

- A shopping search engine is the **commerce instance of vertical search**: narrowed corpus, domain-shaped results. What makes it a distinct directory leaf is the commerce supply chain (merchant feeds, product-identity normalization, CPC/ads machinery, purchase handoff), not merely narrowed scope. The vertical-search-engine pass should assign by center of gravity (corpus narrowing as the defining act vs the purchase-oriented corpus supply chain as the defining act) and treat this document as boundary counterparty; joint review recommended.

### vs Metasearch Engine (§02.02, unprocessed) — carries the sibling's flag from this side

- The persistent-owned-corpus test (documented here: the engine stores its ingested offer corpus; query-time search runs over it) supports the sibling's proposed discriminator against metasearch. Market-literature classifications of "comparison shopping engines" as metasearch are rejected for both Types. Joint review recommended when metasearch-engine is processed.

### vs Online Marketplace (§05.02, unprocessed)

- The marketplace is a transaction venue; the shopping search engine routes to sellers. Direct evidence of the relationship: marketplace offers (eBay) appear *inside* the sampled engine as a provider/source of results — the marketplace is supply, not the venue of this Type.

### vs Product Discovery Application (§05.05, processed)

- Query-first vs query-independent browsing, per that pass's own sibling test. Category tiles, trending suggestions, and top-products/deals surfaces exist in shopping search engines as auxiliary entries; the defining act remains the query.

### vs Deal Discovery Platform (§05.05, unprocessed)

- Deal machinery exists as a secondary layer (rebate fields with end dates, sale-event flags, top-deals surfaces, "Deals" in positioning) — but the unit of record is the offer/product result on the corpus, not the time-limited deal event.

### vs storefront site search (capability, no leaf)

- Remove the multi-seller corpus → a single store's site search. Site search is a capability of storefronts (§05.01 territory), not this Type.

## Uncertainties

1. **Google Shopping internals unverified** — support.google.com and developers.google.com timed out (second consecutive pass across both); no claims made about its consumer surfaces, merchant programs (free listings, Merchant Center), or ranking. Its center-of-gravity status is carried structurally from the sibling pass's flag.
2. **Bing results page unobservable** — the research environment is geo-routed to the CN market where the shopping vertical is not served (live-observed fallback to web results); evidence limited to the vertical's entry surface. No claims about its result layout, filters, alerts, or tracking features.
3. **Kelkoo consumer site unreachable** (kelkoo.com / kelkoo.co.uk 403) — consumer presentation documented via the B2B docs (the API model is what consumer/publisher surfaces render) and the publisher use case, not via live consumer pages.
4. **Microsoft merchant-side docs unreachable** (about.ads.microsoft.com 404) — search-embedded merchant supply documented only through the sampled CSS operator's description ("Access Google and Bing Shopping through our CSS").
5. Shopzilla empty response; Shopping.com content thin and feed-era — the standalone-destination pole rests on Kelkoo's documented machinery + Shopping.com's structure.
6. Consumer-side conveniences of modern engines (price tracking, alerts, saved lists, local inventory) not directly documented in the reachable sample — deliberately excluded from standard capabilities; recorded as market-common expectations only.
7. Historical 1990s products (Pricewatch, Bargain Finder, PriceGrabber, Shopzilla, NexTag) recalled qualitatively, not verified live; the historical check rests on Kelkoo's self-documented vintage, Shopping.com's preserved feed-era structure, and the structural argument.
8. Scale figures (10k+ advertisers, 29 markets, €500m+ sales) are vendor-displayed claims, recorded as claims.

## Final Synthesis

A Shopping Search Engine is a query-first product/offer retrieval application whose defining core is exactly four structures: the shopper query as the entry act (remove → discovery/browsing surface), the multi-seller offer corpus built from many independent sellers' product data (remove → single-store site search), purchase-shaped results (offer results carrying price, seller, availability — remove → general web search), and the purchase handoff to sellers (remove → a data service with no shopping loop). The corpus is owned and ingested (merchant/provider feeds), distinguishing the Type from metasearch; the result unit is the offer, with a product-identity layer (standard codes) beneath it; the default ordering is relevance-to-query with shopper re-sorting, distinguishing it from the comparison-centered sibling Type. Mature products commonly add: category taxonomy resolving into search, facets/filters on commerce attributes, price machinery (rebates, installments, totals), merchant-side supply chains (feeds, advertiser consoles, sales tracking, statistics), per-click CPC economics with tracked outbound URLs, distribution of the search machinery itself to third-party surfaces (APIs/feeds/CSS), deal layers, and market scoping. Variants: search-embedded vertical vs standalone destination vs headless network; merchant feeds vs provider/marketplace-sourced supply; destination monetization vs infrastructure posture; thin feed-era UIs vs rich consumer tabs; regional vs multi-market. The Type's sharpest seams: Shopping Comparison Platform (query-time relevance-ranked retrieval vs persistent product record with aligned offer table — joint review discharged, keep-both), General/Vertical Web Search Engine (commerce corpus + purchase-shaped results + commerce supply chain), Metasearch Engine (owned ingested corpus vs query-time aggregation), Online Marketplace (routing vs venue; marketplaces appear as offer sources), Product Discovery Application (query-first vs query-independent), Deal Discovery Platform (offer record vs deal event).
