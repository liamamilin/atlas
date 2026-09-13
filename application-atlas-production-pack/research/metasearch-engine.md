# Research Notes — Metasearch Engine

Research date: 2026-09-08

## Research Goal

Understand what a Metasearch Engine is as an Application Type: the minimal structure that makes a product recognizable as one, how the query→fan-out→merge loop works, what the product owns (corpus? ranking? neither?), what surfaces and rules shape it, and where its boundaries lie against General Web Search Engine, Vertical Search Engine, Answer Engine, the shopping Types, and the travel Types.

This pass also carries three joint-review obligations recorded by earlier passes:

1. **general-web-search-engine (§02.02, 2026-09-07)**: ratify or replace the "single-authority-vs-aggregation" placement, especially for wrapper products (own UI over one licensed index), which sat closest to the metasearch seam and were unreachable that pass.
2. **shopping-comparison-platform (§05.05, 2026-09-07)**: ratify or replace the proposed discriminator "metasearch aggregates third-party results at query time without a persistent owned registry" vs the comparison platform's persistent product catalog.
3. **shopping-search-engine (§05.05, 2026-09-07)**: same flag echoed with direct owned-corpus documentation; and **flight-search-booking-platform (§26, 2026-09-08)**: pure vertical search without booking/handoff path belongs to §02.02.

## Initial Boundary

Hypothesis at start:

- Core use: forward a user's query to several other search engines/services at query time and combine their results into one list.
- The product owns no retrieval corpus of its own; its own contribution is the aggregation/relay layer.
- Users: general public, with a strong privacy-conscious segment (the aggregation structure enables an anonymizing-relay posture).
- Nearest neighbors: General Web Search Engine (operates a corpus + own ranking), Vertical Search Engine (narrowed corpus), Answer Engine (synthesized answer as primary output), Shopping Comparison Platform (persistent owned product registry), Flight Search / Booking Platform (travel-domain objects + booking path), Privacy-focused Browser (client surface).
- Open questions going in: (1) Is "multiple upstreams" definitional, or is "upstream-fetched at query time" the invariant (single-upstream relay question)? (2) Is "no own index at all" definitional, given some products blend small own indexes? (3) Is the privacy posture definitional or the market's dominant posture? (4) Does the travel "metasearch" usage belong to this Type?

## Research Questions

1. What is the minimal interaction loop, and what is the unit of work?
2. What exactly does the product own — corpus, ranking, neither?
3. How are upstreams selected, configured, and combined (merge, dedupe, weighting, re-scoring)?
4. What does a merged result consist of, and does it carry upstream provenance?
5. How do users steer which upstreams are queried (per query, per session, per install)?
6. What rules connect filters to upstream capabilities?
7. What user state persists?
8. How do metasearch products monetize, and what does upstream access cost?
9. What is the supply side (how does a service become an upstream)?
10. What distinguishes this Type from its neighbors (the three joint-review questions above)?

## Representative Products

| Product | Why sampled | Evidence level |
|---|---|---|
| SearXNG | Open-source, self-hostable multi-source aggregator; the purest aggregation pole; exceptionally complete docs | A (5 pages directly fetched) |
| MetaGer | Nonprofit-run consumer metasearch with a paid-key model; publishes its own definition of metasearch and its ranking method | A (4 pages directly fetched) |
| Skyscanner (partner/API surfaces) | Travel-vertical application of the metasearch mechanism; documents the supply side and affiliate/referral model | A (2 pages directly fetched; consumer surface not sampled) |
| Startpage | Single-upstream relay pole (the wrapper question) | Unreachable — 2 timeouts (support hub + root); no claims |
| Dogpile | Classic ad-funded commercial consumer metasearch | Unreachable — 2 timeouts (help + root); no claims |
| Kayak | Travel metasearch commercial pole | Not sampled — /partners returned 404; consumer surface not attempted |
| Wikipedia (Metasearch engine article) | Historical lineage for the market-sample check | Unreachable — 2 timeouts (desktop + mobile); historical check reasoned, not cited |

Selection notes: the two web poles (SearXNG, MetaGer) have different philosophies (open-source self-host vs nonprofit paid service) and different customer tiers (instance operators vs consumer key buyers). The travel pole is sampled only at the partner/API layer to settle the §26 boundary; its consumer surface belongs to the Flight Search / Booking Platform pass. The classic commercial pole (Dogpile) and the relay pole (Startpage) were unreachable; both are treated as conceptual/weak below.

## Sources

Fetched successfully (2026-09-08):

- SearXNG docs root — https://docs.searxng.org/
- SearXNG Architecture — https://docs.searxng.org/admin/architecture.html
- SearXNG Configured Engines — https://docs.searxng.org/user/configured_engines.html
- SearXNG Why use a private instance — https://docs.searxng.org/own-instance.html
- SearXNG Search syntax — https://docs.searxng.org/user/search-syntax.html
- SearXNG Result (base type) — https://docs.searxng.org/dev/result_types/base_result.html
- SearXNG `engines:` settings — https://docs.searxng.org/admin/settings/settings_engines.html
- MetaGer home — https://metager.org/
- MetaGer Search engines — https://metager.org/search-engine
- MetaGer Transparency statement — https://metager.org/transparency
- MetaGer Settings — https://metager.org/meta/settings?focus=web
- Skyscanner API Developer Documentation — https://developers.skyscanner.net/
- Skyscanner Affiliate programme — https://www.partners.skyscanner.net/affiliates

Unreachable (transport timeouts / errors) and therefore unused:

- Startpage: https://support.startpage.com/hc/en-us and https://www.startpage.com/en/ (timeout ×2)
- Dogpile: https://help.dogpile.com/ and https://www.dogpile.com/ (timeout ×2)
- Kayak: https://www.kayak.com/partners (404)
- Ecosia: https://help.ecosia.org/ (transport error ×1 — abandoned)
- Wikipedia: https://en.wikipedia.org/wiki/Metasearch_engine and https://en.m.wikipedia.org/wiki/Metasearch_engine (timeout ×2)
- Skyscanner partnernetwork host: https://partnernetwork.skyscanner.net/ (transport error; developers + partners hosts reachable instead)

Consequence: the evidence base is 2 strong web-pole products + 1 travel-pole partner-layer product. All cross-product claims rest on SearXNG + MetaGer (+ Skyscanner for the travel boundary). Startpage/Dogpile-class behavior is reasoned, not observed, and is marked as such wherever it appears.

## Product Observations

### SearXNG (A-layer, direct — 5 pages)

Positioning & structure:

- Self-description: "SearXNG is a free internet metasearch engine which aggregates results from up to 269 search services. Users are neither tracked nor profiled." Tor supported for online anonymity. Fork of searx (2021).
- Feature list: self-hosted; no user tracking/profiling; JS & cookies optional; 269 search engines (83 enabled by default); ~70 well-maintained public instances on searx.space; "easy integration of search engines".
- Instance model: public instances (open to everyone, operated by unknown parties), private instances (select group — friends, company over VPN), single-user local instances.

Upstream registry (engines: settings — direct):

- Each upstream is a configured list entry: name, engine (python module), shortcut (bang), base_url, categories (multiple allowed), timeout, api_key, disabled, inactive, language, tokens, weight (default 1), display_error_messages, per-engine network settings (proxies, Tor, HTTP/2/3, retries, max_connections, retry_on_http_error).
- Engines requiring API keys are inactive by default until a key is provided.
- **Private engines (tokens)**: an engine can be restricted to holders of secret tokens — hidden from users without the token (not listed in preferences or /config API). Access control over upstreams is a built-in concept.
- Multilingual search workaround: add the same upstream twice with different languages.
- Offline engines concept: engines that search local data (command-line engines, NoSQL databases, SQL engines, local search-indexer APIs) — the aggregation layer can include non-network sources.

Categories & tabs (configured engines — direct):

- 269 engines of which 83 enabled by default; engines assignable to multiple categories; UI tabs configured via `categories_as_tabs`.
- Category groups observed: general (subgroups blogs, books, currency, translate, web, wikimedia + ungrouped), images (icons, web, photo/stock sources), plus (from nav and engine list) videos, news, music, it, files, maps, science, social media.
- Upstream set is NOT only web engines: dictionaries/translation services, currency conversion, science databases (arXiv, PubMed, Semantic Scholar, OpenAlex, CORE, Crossref), wikimedia family, image/stock sources (Unsplash, Pexels, Pixabay, Openverse...), social (Mastodon, Lemmy, PeerTube), package indexes (Alpine/Arch/Void Linux), and general web engines (Google, Bing, DuckDuckGo, Brave, Mojeek, Qwant, Startpage, Yahoo, Yandex, Baidu, Sogou, Naver, Seznam...).
- Per-engine feature matrix columns: Disabled, Timeout, Weight, Paging, Locale, Safe search, Time range.

Query machinery (search syntax — direct):

- `!` bang selects engine and/or category; chainable and inclusive (`!map !ddg !wp paris`). `:` selects language. `!!<bang>` external bangs re-use DuckDuckGo's bang service to jump directly to an external search page — with the explicit caveat "your search will be performed directly in the external search engine. SearXNG cannot protect your privacy with this." `!!` alone = redirect to first result ("Feeling Lucky" analog, same privacy caveat).
- Special queries (plugins/answerers): random uuid, average, user-agent, hash digests, calculator, unit converter, time zone.

Result object (dev docs — direct):

- Base `Result` carries: `url`, `engine` ("Name of the engine this result comes from"; plugins/answerers use prefixes), `parsed_url`. Result container merges results from engines; typed result families: main results (web/image/file/paper/code/key-value), answer results, correction results, suggestion results, infobox results.
- URL filtering hooks apply across url-bearing fields (iframe_src, img_src, thumbnail...).

Privacy behavior (own-instance — direct):

- Privacy protection in three forms: (1) removing private data from requests going to search services — no cookies sent to external engines, a random browser profile generated per request, the instance's IP used (optionally proxy/Tor); (2) not forwarding third-party content through search services (no ads/tracking forwarded); (3) removing private data from requests going to results pages — "both the referring page and search query are hidden from the results pages being visited."
- Upstream-dependence risk, documented: "public instances without proper protection are more vulnerable to abuse of the search service, which may cause the external service to enforce CAPTCHAs or to ban the IP address of the instance. Thus, search requests would return less results."
- Reference public-instance config: limiter on, image_proxy on, safe_search 2, autocomplete 'duckduckgo' (suggestions themselves upstream-sourced), formats [html].

Monetization: none in-product (free software; public instances volunteer-run; donations/community).

### MetaGer (A-layer, direct — 4 pages)

Positioning & structure:

- Home: "Open Source. Ad-Free. Anonymous." "Search and browse the web without being watched." Nonprofit (SUMA-EV — Association for Free Access to Knowledge). Source code public (GitLab).
- Access model: a randomly generated **key** ("Your key is your access – no account, no email address. Only your balance hangs off it."); one-time payment adds token credit; "About 500 token (€5) usually lasts around 2 months." Key usable on any number of devices, shareable. Anonymous payment methods incl. cash. Anonymous tokens for provable anonymity (with app/extension).
- Anonymous browsing: a server-side private browser ("open any website in a private browser that runs securely on our servers") — beyond search, sessions auto-deleted.
- No ads, no logging ("our search engine is built so that fighting spam doesn't require logs"), no captchas even over VPN.

Self-definition of the Type (transparency page — direct):

- "A metasearch engine combines the results of several search engines and evaluates them again according to its own criteria. This means that the metasearch engine does not have its own index. Therefore, metasearch engines do not use crawlers. They use the index of other search engines."
- Advantage: "the user only needs a single search query to access the results of several search engines. The metasearch engine outputs the relevant results in a once again sorted list of results."
- **Corpus nuance**: "MetaGer is not a pure metasearch engine, as we also use small indexes of our own."
- Ranking method: "We take the rankings from our source search engines and weigh them. These rankings are then converted into scores. Additional points are awarded or deducted for the occurrence of the search terms in the URL and in the snippet, as well as the excessive occurrence of special characters... We also use a blocking list to remove individual pages from the results list" (legal blocks; demonstrably incorrect info; extremely poor quality; dubious pages).
- Transparency posture: algorithms published ("Our Algorithm" page), source code free; authority-request table (0 fulfilled information requests, 0 blocking requests over last 5 years).

Upstream registry (search-engine page — direct):

- "MetaGer is a metasearch engine. Therefore, we use the indexes of various other search engines." Per-upstream profiles with index estimates.
- Per-focus upstream sets: **Web**: Mojeek, Brave, Serper (Google index). **Images**: Brave, Pixabay, Serper. **News**: Brave, Serper, TootNews (SUMA-EV's own). **Products**: eBay, Serper. **Science**: Minisucher Wissenschaft, TUBdok, BASE.
- Supply side: "How to integrate your search engine with MetaGer" — contact-based integration; "we can only integrate general web searches or searches in the area of our foci... web, image, news or product searches."

User settings (settings page — direct):

- Search focus: Web / Images / News / Products / Science.
- **Per-focus upstream on/off switches**: "Below you can see all search engines available for this focus. You can switch them on/off by clicking on the name."
- **Token-costed upstreams**: "Brave (0.8 Token) Mojeek (0.3 Token) Serper (0.2 Token)... We charge 1 Token per search query with the current settings. Note: The minimum cost per search is 1 Token per search." Upstream choice has a visible per-search price.
- **Capability intersection rule**: "With the selection of a search filter, only search engines are available that support this filter. Conversely, only search filters are displayed which are supported by the current search engine selection."
- Filters: Safe Search (Any/Strict/Moderate/Off), Date (Any/Last 60m/24h/week/month/year), Language (long locale list).
- Blacklist: domain exclusion list ("*." prefix for all subdomains).
- Preferences: search suggestions provider (Disabled / Serper 0.2 Token / Brave 0.1 Token — suggestions are upstream-sourced and priced too), tips, start-page tiles, appearance, open-in-new-tabs.
- State: settings in non-personally-identifiable plain-text cookies; restore-via-URL backup; browser extension to survive cookie clearing.
- Empty fan-out is a reachable state: "With the current search settings, no search engine is queried."

### Skyscanner (A-layer, partner/API surfaces — travel pole)

- API surface (developers.skyscanner.net): Flights live prices + indicative prices; Car Hire live/indicative + agents; Hotels live/indicative + content + reviews; Geo, Culture, Carriers, Autosuggest. The "live prices" pattern = query-time price retrieval from supply partners; "indicative" = cached/pre-computed layer.
- Affiliate programme (partners.skyscanner.net/affiliates): "Become a Skyscanner affiliate to earn competitive commission on the traffic you send us"; "1,200+ supply partners"; "10bn prices searched every day"; 180 countries via 52 domains; widgets/banners/text links; "The pay-out you receive is a percentage of the commission that Skyscanner receives from this supply partner"; referral data stored 30 days.
- Affiliate acceptance criteria include: "The website does not book tickets on behalf of their customers" — the affiliate/referral layer routes, it does not transact.
- Partner sectors: airlines, hotels, car hire, OTAs, airports, destinations, advertisers — the supply side of travel metasearch.

### Startpage / Dogpile / Kayak / Ecosia / Wikipedia

Unreachable this pass (see Sources). No observations. No claims. The relay pole and the classic commercial pole remain conceptual; the historical check is reasoned.

## Cross-product Comparison

| Dimension | SearXNG | MetaGer | Skyscanner (travel pole) | Evidence |
|---|---|---|---|---|
| Self-description as metasearch | "free internet metasearch engine which aggregates results from up to 269 search services" | "a metasearch engine... uses the indexes of various other search engines" | (industry term; partner docs describe aggregation supply) | A×2 |
| Upstream set | 269 services, 83 default-on; web engines + dictionaries/translate/currency/science/wikis/images/social | per-focus lists: Web (Mojeek, Brave, Serper), Images (Brave, Pixabay, Serper), News (Brave, Serper, TootNews), Products (eBay, Serper), Science (BASE, TUBdok...) | 1,200+ supply partners (airlines/OTAs/hotels/car hire) | A×3 |
| Own corpus | none (offline engines optional for local data) | "not a pure metasearch engine, as we also use small indexes of our own" | no owned flight/hotel inventory (live prices queried per search; indicative cache layer) | A×3 |
| Merge/aggregation logic | per-engine weight + timeout; result container merges; result carries `engine` provenance | "take the rankings from our source search engines and weigh them... converted into scores" + URL/snippet term bonuses + blocking list | offer ranking (not directly documented in fetched pages) | A×2, weak ×1 |
| Upstream selection surface | admin config + user preferences per category + per-query bangs | user on/off per focus; per-query focus tabs | platform-configured supplier network | A×3 |
| Query-level upstream steering | bangs (`!wp`, `!map`, chainable); external bangs `!!` (leave the product, privacy caveat) | focus tabs; per-focus toggles | route+dates query | A×2 |
| Filter↔upstream capability coupling | per-engine feature matrix (paging/locale/safe search/time range) | "only search engines are available that support this filter. Conversely, only search filters are displayed which are supported by the current search engine selection" | (not observed) | A×2 |
| Privacy posture | anonymized relay: no cookies to upstreams, random browser profile per request, optional Tor/proxy; referrer+query hidden from destinations; no ads/tracking forwarded | anonymous proxy, TOR hidden service, no logging, anonymous tokens, no ads | none (commercial travel) | A×2 |
| User state | preferences (engines per category, engine tokens, language), cookieless-optional | key/token account + non-PII cookie settings + blacklist + URL backup | (traveler side not sampled) | A×2 |
| Monetization | none (self-host/donations) | paid key: token credit, per-search minimum 1 token, per-upstream token prices | affiliate commission (% of platform's commission from supply partner); advertising products | A×3 |
| Upstream access cost | free (public upstreams) or API-key-gated (inactive until key provided) | token-priced per upstream; suggestions priced too | commercial API agreements | A×3 |
| Failure behavior | upstream CAPTCHA/bans degrade results (documented); per-engine timeout; displayable error messages | empty fan-out reachable ("no search engine is queried"); token minimum | live→indicative fallback pattern | A×2, weak ×1 |
| Supply side (become an upstream) | write an engine module; API-key engines inactive by default | contact-based integration; web/image/news/product searches only | supply-partner API agreements; affiliate routing | A×3 |
| Result provenance | `engine` field on every result | not directly observed on results page | (n/a) | A×1 — product-specific-observed |

## Four-layer Abstraction

### L0 — Defining Invariant

Four structures, each removable-to-a-different-outcome:

1. **Open user-composed query** — the unit of work is a free-form information need expressed by the user (family-inherited from the search Types). Remove → feed/browse surfaces.
2. **Query-time fan-out to multiple upstream search services** — at the moment of search, the query is forwarded to more than one external retrieval service the product does not operate. Remove the plurality → single-upstream relay (the flagged seam case, see Boundary Findings); remove the fan-out entirely → a launcher/directory of engines, not a search product.
3. **Merged result list under the product's own aggregation logic** — upstream results are combined into one ordered list (dedupe, weighting, re-scoring, filtering); each result remains an outbound reference to content the product does not host. Remove → a raw conduit between the user and each engine, not a search product.
4. **No retrieval corpus of its own as the primary source** — the product operates no index/crawler as its principal source; upstream services are where results come from. Small supplementary own sources do not disqualify (MetaGer: "not a pure metasearch engine, as we also use small indexes of our own" — and it remains a metasearch engine by self-description and market class). Remove → General Web Search Engine (operates a corpus + own ranking).

Jointly-held is load-bearing: 2+3 without 4 = a general engine that happens to blend; 4 without 2+3 = a proxy/portal with no search act; 2 without 3 = engine launcher; 3 without 2 = single-source re-ranking (the seam case).

Explicitly NOT in L0 (anti-overfitting):

- **Privacy/anonymization.** The dominant posture of the current web pole (both sampled products pitch it centrally) but structurally a consequence of the aggregation position (the product sits between user and upstreams and *can* anonymize), not the definition; the travel pole has no privacy posture.
- **Specific upstream count, identity, or mix** (269 vs 5; Google vs Mojeek vs eBay).
- **Categories/tabs, bangs, filters, suggestions, settings** — standard mature structure.
- **Monetization model** (free, paid key, ads, affiliate).
- **Deployment model** (hosted service vs self-hosted instances).

### L1 — Common Mature Structure

- **Upstream registry as configuration** — upstreams held as configured entries with per-engine attributes: enabled/disabled, weight, timeout, language/locale, category assignment, API-key requirement, network/proxy settings (SearXNG schema A; MetaGer per-focus lists A).
- **Category/focus tabs** mapping query surfaces to upstream groups (SearXNG categories_as_tabs A; MetaGer foci A).
- **User-steerable upstream selection** — per-query (bangs A×1) and/or persistent per-focus toggles (A×1); at least one of the two in each sampled web product.
- **Filter↔capability coupling** — filters (safe search, time range, language) apply only where upstreams support them; the upstream set and filter set constrain each other (A×2).
- **Merged result with provenance** — the result object carries which upstream(s) produced it (SearXNG `engine` field A×1; likely common, not directly observed elsewhere).
- **Anonymizing relay posture** — no cookies/identity forwarded to upstreams, randomized request profiles, optional Tor/proxy, referrer+query hidden from destination sites, no third-party ad/tracking content forwarded (A×2 — the web pole's standard posture).
- **Upstream-sourced assistance** — suggestions/autocomplete fetched from upstream services (SearXNG reference config autocomplete 'duckduckgo' A; MetaGer suggestion provider Serper/Brave A).
- **Non-web verticals as upstream categories** — images, news, science/papers, dictionaries/translate, shopping (A×2).
- **Settings persistence without mandatory accounts** — cookies/URL-backup (A×2).
- **Supply-side integration path** — a documented way for a new service to become an upstream (engine module A×1; contact integration A×1; supply-partner APIs A×1).
- **Upstream-dependence failure modes** — CAPTCHA/ban risk from upstreams (A×1 documented), per-engine timeouts (A×1), degraded results when upstreams fail.

### L2 — Variant / Optional Structure

- **Corpus purity**: pure aggregation (SearXNG) vs small own indexes blended in (MetaGer self-described "not a pure metasearch engine").
- **Privacy depth**: full anonymizing relay with Tor/anonymous tokens (both web poles, different depths) vs none (travel pole).
- **Monetization**: none/self-host+donations (SearXNG); paid key with per-upstream token pricing and per-search minimum (MetaGer); affiliate commission + advertising (travel pole); ads (classic commercial pole — unreachable, conceptual).
- **Deployment**: hosted consumer service (MetaGer) vs public/private/single-user instances (SearXNG); instance trust model documented (public = trust the operator).
- **Access control over upstreams**: private engines gated by tokens (SearXNG); key-gated search with token balance (MetaGer).
- **Vertical application**: the same mechanism applied to a travel domain (live price queries to supply partners, affiliate routing) — directory realizes it under §26 leaves when domain objects + booking/handoff paths are present.
- **Beyond-search adjuncts**: server-side anonymous browsing (MetaGer), external bangs/redirects that leave the product (SearXNG, with privacy caveat), maps/citation tools (MetaGer).
- **Local/offline sources in the aggregation set** (SearXNG offline engines: SQL/NoSQL/command-line/local indexers).

### L3 — Vendor-specific

- SearXNG: 269-engine count and 83 default; bang syntax specifics; `!!` external-bang integration with DuckDuckGo's bang service; answerers/plugins (calculator, hash, unit converter, time zone, Tor check); limiter/botdetection machinery; valkey cache; image_proxy; private-engine tokens; multilingual-via-duplicate-engine workaround; searx.space instance directory; uptime status site.
- MetaGer: token economy (per-upstream token prices — Brave 0.8 / Mojeek 0.3 / Serper 0.2; 1-token per-search minimum; ~500 token ≈ €5 ≈ 2 months), key model with anonymous payment, anonymous tokens, server-side anonymous browser, blocking-list policy (legal / demonstrably false / poor quality / dubious), authority-request transparency table (0/0 over 5 years), Maps/citation-search/widget tools, SUMA-EV membership/donation funding, TootNews (own news upstream), renewable-energy posture.
- Skyscanner: live vs indicative pricing API split, geo/culture/carriers/autosuggest APIs, affiliate acceptance criteria (working links, HTTPS, >5,000 monthly uniques, up-to-date travel content, no booking on behalf of customers), exclusion of coupon/network/subnetwork agencies, 30-day referral window, Impact.com as partner platform, creator programme.

## Rejected Findings

- **"A metasearch engine owns no index whatsoever"** — rejected as absolute: MetaGer keeps small own indexes and remains a metasearch engine. The invariant is that upstream services are the *primary* source.
- **"Privacy/anonymization is definitional"** — rejected: it is the web pole's dominant posture (A×2) but the travel pole lacks it entirely; structurally it is an affordance of the middleman position, not the defining act.
- **"Upstreams = other general web search engines"** — rejected: sampled upstream sets include dictionaries, translation, currency, academic databases, image/stock libraries, shopping sources, wikis, package indexes. The right abstraction is "upstream search services".
- **"Metasearch is just a privacy wrapper over one engine"** — rejected: the defining act is multi-source aggregation; the single-upstream relay is at most a degenerate pole (see Boundary Findings).
- **"Comparison shopping engines are metasearch"** — rejected (ratifies both shopping passes): comparison platforms maintain persistent owned product registries with attached offers; metasearch fetches results at query time and owns no registry. MetaGer's Products focus (eBay queried as an upstream per search) documents the metasearch form of shopping retrieval.
- **"Travel metasearch is a different mechanism"** — rejected: it is the same mechanism (query-time aggregation over upstreams, no owned inventory) applied to travel-domain objects; the directory assigns it to §26 leaves when booking/handoff paths and flight-domain service responsibilities are present.
- **"The merged list is the product's own ranking over its own corpus"** — rejected: the ordering is computed over upstream-fetched result lists (transient, per query), not over an operated index. MetaGer's method (weigh upstream rankings → scores → adjustments) is re-evaluation of upstream orderings, not corpus ranking.

## Boundary Findings

- **vs General Web Search Engine** (the family's primary seam): the discriminator is the pair (corpus posture, ordering source). A general engine operates a retrieval corpus as its own — however acquired (own crawl, licensed, hybrid) — and computes its own ordering over it. A metasearch engine fetches result lists from upstream services at query time and merges them under its own aggregation logic. **Ratification of the general pass's placement, with a refinement**: the seam is corpus-and-ordering, not "single vs multiple engines"; a hybrid engine that blends upstream results into a primarily own corpus is assigned by center of gravity (primary corpus own → general). Removal test: give the product an operated corpus as primary source → general engine.
- **The wrapper question (general pass's open item) — answered**: a *pure relay* (no own corpus, presents one upstream's results, no own ordering machinery) satisfies metasearch's corpus posture but not the plural fan-out. Placement proposed: the **thin/degenerate pole of the Metasearch Type** — the aggregation degenerates to relay when the upstream set has one member; the relay shares every other structural property (no corpus, upstream-fetched results, middleman position, upstream-dependence risk, privacy-by-proxy affordance). This is a C-layer canonical inference: the relay pole was unreachable this pass (Startpage ×2 timeouts) and the placement is reasoned, not observed. Products that operate a licensed corpus with their own ranking machinery remain general engines (the general pass's own rule). The truly gray middle — light re-ranking over a single upstream's per-query results — is assigned by center of gravity and remains flagged.
- **vs Vertical Search Engine**: orthogonal discriminators — vertical is about corpus *scope*, metasearch about corpus *posture*. A metasearch over a narrowed domain exists (travel); a vertical engine with its own corpus (academic, shopping) is not metasearch. The §02.02 leaf's canonical pole is web-reference metasearch.
- **vs Shopping Comparison Platform / Shopping Search Engine** (both flags discharged): the persistent-owned-registry vs query-time-aggregation discriminator is **ratified from the metasearch side**. Comparison platforms hold canonical product records with attached multi-seller offers that persist between visits (price history, alerts, product pages presuppose the registry); metasearch holds no registry — results are fetched from upstream services at the moment of search. MetaGer's Products focus is the metasearch form of shopping retrieval: eBay queried as an upstream per search, no product record maintained.
- **vs Flight Search / Booking Platform** (echoing that pass): the referral/metasearch pole of the flight leaf shares this Type's aggregation mechanism, but carries flight-domain objects (segments, fares, trip shapes) and a booking/handoff path with seller-of-record responsibilities. A product that is pure travel comparison without booking/handoff and without flight-domain service responsibilities would belong to §02.02; the sampled travel product (Skyscanner) documents the §26 side (affiliates must not book; supply partners transact). The §02.02 leaf's canonical pole remains web-reference metasearch.
- **vs Answer Engine**: the primary output remains a merged reference list; upstream-sourced answer/infobox results (SearXNG answer/infobox result types) are additive layers, same structure as AI summaries on general engines.
- **vs Directory Application**: directories hold standing hand-curated records; metasearch computes transient merged lists per query. A product that merely links to engines without merging is a launcher/directory, not metasearch (removal test for L0 #3).
- **vs Privacy-focused Browser / Web Browser**: browsers are client surfaces that can default to a metasearch engine; the metasearch is the destination service. Distribution integration (extensions, apps, default-engine settings) is common but not definitional.
- **vs Search Platform / Enterprise Search**: internal permissioned corpora with member identity vs upstream public services with anonymized relay; different trust models entirely.
- **"去掉什么就变成另一个 Type" summary**: give it an operated corpus + own ranking → General Web Search Engine; narrow the domain and add booking/handoff + domain objects → §26 travel Types; add a persistent owned product registry → Shopping Comparison Platform; promote a synthesized answer to primary output → Answer Engine; remove the merge → engine launcher/directory; remove the plurality of upstreams → the relay seam case.

## Uncertainties

1. **Startpage and Dogpile unreachable (2 timeouts each)** — the single-upstream relay pole and the classic ad-funded commercial pole have no direct evidence. The relay placement (thin pole of this Type) is reasoned (C-layer) and flagged for joint review. The ad-funded pole's behavior (ads in merged results, tracking posture) is unverified — monetization is kept out of all definitional claims.
2. **Wikipedia unreachable (2 timeouts)** — the historical/market-sample check is reasoned, not cited: the definition is written so that the founding-generation form (query fan-out to several engines, merge, no own index — the 1990s shape) satisfies all four L0 structures without ads, accounts, privacy promises, or categories; MetaGer's and SearXNG's published self-definitions are structurally identical to the classic definition, which supports time-stability. No archived source was fetchable this pass.
3. **Kayak not sampled** (404 on partner path; consumer surface bot-walled by market reputation) — the travel pole rests on Skyscanner's partner/API layer only.
4. **MetaGer's merge formula is documented qualitatively** (weigh upstream rankings → scores; URL/snippet term bonuses; special-character penalties; blocking list) — no numeric weights published; none asserted.
5. **Per-result upstream attribution** is directly observed only in SearXNG's result schema (`engine` field); whether MetaGer's results page shows per-result sources was not observed. Kept product-specific-observed, likely common.
6. **Ecosia-class light-re-ranking wrappers** (single upstream + own ranking layer) sit in the gray zone between the general Type's licensed-corpus pole and this Type's relay pole; unreachable; assignment by center of gravity proposed, not observed.
7. **Skyscanner's consumer-side result anatomy** (how merged offers are ranked/displayed) was not in the fetched pages; the travel pole's merge logic is asserted weakly.

## Final Synthesis

A Metasearch Engine is a query-first search application whose results are not computed from a corpus it operates but fetched, at the moment of search, from multiple upstream search services and merged into one list under the product's own aggregation logic. Its defining core is four jointly-held structures: the open user-composed query; query-time fan-out to multiple upstream services; the merged, re-evaluated result list (results remain outbound references); and the absence of an operated retrieval corpus as the primary source (small supplementary own sources do not disqualify). Everything else — the upstream registry and its per-engine configuration, category tabs, bangs, filters coupled to upstream capabilities, result provenance, the anonymizing-relay privacy posture, suggestions, settings, monetization shape, deployment model — is standard mature structure or variant. The Type's neighbors are defined by single-subtraction tests: operate a corpus with own ranking → General Web Search Engine; add a persistent owned product registry → Shopping Comparison Platform; add travel-domain objects and a booking/handoff path → the §26 travel Types; promote a synthesized answer to primary output → Answer Engine; remove the merge → a launcher, not a search product. The single-upstream pure relay is the Type's degenerate thin pole (reasoned placement, flagged for joint review). The Type's structural signature is dependency: the product's result quality, availability, and even its privacy promise are hostage to upstream services it does not control — which is why upstream configuration, capability coupling, failure degradation, and the middleman privacy posture are the load-bearing behaviors of everything sampled.
