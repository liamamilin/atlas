# Research Notes — General Web Search Engine

Research date: 2026-09-07

## Research Goal

Understand what a General Web Search Engine is as an Application Type: the minimal structure that makes a product recognizable as one, how the query→results loop works, what surfaces and rules shape it, and where its boundaries lie against Vertical Search Engine, Metasearch Engine, Answer Engine, Directory/Portal Types, and enterprise Search Platform.

## Initial Boundary

Hypothesis at start:

- Core use: retrieve web documents by free-form query; the primary output is a ranked list of references to documents hosted elsewhere on the web.
- Users: general public (demand side); site owners/webmasters (supply side, competing for placement); advertisers (monetization surface).
- Nearest neighbors: Vertical Search Engine (narrowed corpus), Metasearch Engine (aggregation of other engines), Answer Engine (synthesized answers as primary output), Directory Application / Information Portal (hand-curated standing records), Search Platform / Enterprise Search (organizational corpora), Web Browser (client surface that routes to engines).
- Open questions going in: (1) Is "own crawler/index" definitional, given wrapper engines exist in the market? (2) How much modern SERP furniture (ads, panels, AI answers, tabs) belongs to the definition vs. common structure? (3) Is there any definitional user state at all?

## Research Questions

1. What is the minimal interaction loop, and what is the unit of work?
2. How is the corpus acquired and maintained, and is acquisition mode definitional?
3. What does a result consist of?
4. What shapes ranking, and what does the engine disclose about it?
5. What does the results page carry beyond the ranked link list?
6. What query assistance and query-language machinery exists?
7. What user state persists (settings, history, filters, region)?
8. What does the supply side (site owners) see?
9. What distinguishes this Type from its neighbors?

## Representative Products

Selected for different philosophies/positions (all consumer-facing; there is no meaningful "enterprise tier" inside this Type):

| Product | Why sampled | Evidence level |
|---|---|---|
| Mojeek | Independent engine pole: own crawler + own index, no-tracking philosophy, UK-based; transparent operator docs | A (multiple pages directly fetched) |
| Microsoft Bing | Mainstream large-engine pole; help-center hub directly fetched (topic inventory level) | A for help-hub topic inventory; article bodies not fetched |
| Yandex | Regional-major pole (Russia/global); best-documented help system of the sample; several articles directly fetched | A (multiple articles directly fetched) |
| Google | Market anchor; attempted (support.google.com, google.com/search/howsearchworks, developers.google.com) | Unreachable — 3 timeouts; no claims made from Google |
| DuckDuckGo / Brave Search / Startpage | Privacy/wrapper poles; attempted | Unreachable — 2 timeouts each; no claims made |

## Sources

Fetched successfully (2026-09-07):

- Mojeek About — https://www.mojeek.com/about
- Mojeek Support index — https://www.mojeek.com/support/
- Mojeek Search Operators — https://www.mojeek.com/support/search-operators.html
- MojeekBot crawler doc — https://www.mojeek.com/bot.html
- Microsoft Bing help hub — https://support.microsoft.com/en-us/bing/microsoft-bing-help (redirected from https://support.microsoft.com/en-us/bing)
- Yandex Search FAQ index — https://yandex.com/support/search/
- Yandex Search settings — https://yandex.com/support/search/en/search-results/settings.md
- Yandex query language (pages & sites) — https://yandex.com/support/search/en/query-language/qlanguage.md
- Yandex operators (date/language/file type) — https://yandex.com/support/search/en/query-language/search-operators.md
- Yandex advanced date filter — https://yandex.com/support/search/en/search-results/serp.md

Unreachable (transport timeouts unless noted) and therefore unused:

- Google: support.google.com/websearch/answer/7089786 (timeout), google.com/search/howsearchworks/how-search-works/ranking-results/ (timeout), developers.google.com/search/docs/fundamentals/how-search-works (timeout)
- DuckDuckGo: duckduckgo.com/duckduckgo-help-pages/results/ and root (timeout ×2)
- Brave: search.brave.com/help (timeout), brave.com/search/docs/ (timeout)
- Startpage: startpage.com/en/ (timeout)
- Bing webmaster guidelines article (bing.com/webmasters/help/webmaster-guidelines-30fba23a) — renders only with JavaScript (empty shell)
- Bing help article bodies — constructed URLs returned 404 (GUID slugs unknown from the hub page)

Consequence: the evidence base is 2 strong + 1 partial product. All cross-product claims below rest on Mojeek + Yandex + (Bing topic inventory). Google is treated as a market anchor only; no Google-specific behavior is asserted anywhere.

## Product Observations

### Mojeek (A-layer, direct)

Positioning & infrastructure:

- Self-describes as "the alternative search engine... values and respects your privacy, whilst providing its own unique and unbiased search results"; search technology "built from the ground up"; founder "built Mojeek infrastructure, crawler, billion scale indexing and algorithms"; index passed 9 billion pages in 2025; independent search "without tracking for over 15 years".
- UK-based company; regional origin does not change the Type.

User-facing surfaces (observed in nav/support structure):

- Result tabs: Web / Images / News / Substack (blogs).
- Knowledge Box / infobox (launched 2018); Safesearch (2023); Semantic Search (2024); Search Summary (2024, AI-style summary layer); Search Choices (2022, "freedom to seek" — pathways to other engines); Focus (2022, "search the web you want" — custom web-scoped searches); cookieless preferences (2022).
- Query machinery: search operators — intitle:/intext:/inurl:/inanchor: (+ all* variants), since:/before: (page-modification date), site:; a dedicated Advanced Search page; a calculator quickbox.
- Settings page with tabs: Appearance / Search / Language-Location / Privacy; cookieless preferences mode.
- Mobile apps (iOS App Store, Android Play); setup guides for 12+ desktop browsers plus mobile browsers.
- Monetization/business: Mojeek Ads; Web Search API; Site Search API; embeddable search boxes.
- Crawling doc (MojeekBot): obeys robots.txt (first matching record, else *); honors noindex / nocache / nofollow meta-tags; rate limit ≈1 request/second per site; does not honor non-standard crawl-delay; published bot-verification procedure (reverse/forward DNS, IP list); separate FeedFetcher crawler.
- Image search uses Openverse as an external provider (observed twice in blog history) — direct evidence that even an own-index engine sources a vertical externally.
- Community forum, blog, newsletter, contact/feedback channels.

### Microsoft Bing (A-layer for help-hub topic inventory; article bodies not fetched)

The help hub (fetched) enumerates the user-facing feature set:

- SafeSearch (block adult content); homepage as a curated surface (explore the homepage, turn off homepage image/video); search history off/on; search suggestions off/on; save search results ("Save search results with Bing" — collections); Visual Search (image-based search, incl. local image upload terms); verticals: images (license-type filter), video ("Get started with Bing Video"), news ("Get the latest news"), maps (My Places, business listings, keyboard shortcuts); interests; medical information; ethical shopping; cash donations.
- "How Bing delivers search results" article exists (body unfetched); "Why am I seeing this ad?" article exists — direct evidence of an ads layer with a user-facing explanation surface; malware/phishing protection warnings; EU Digital Services Act information page.
- Microsoft account integration (sign out of a Microsoft account); Microsoft Rewards topic; Bing Webmaster Guidelines exist as a separate webmaster-facing doc (content unfetched — JS SPA).
- Interpretation care: topic titles confirm existence of these surfaces, not their exact behavior.

### Yandex (A-layer, multiple articles)

Settings article (directly fetched):

- Settings linked to a Yandex ID account when logged in; otherwise saved in browser cookies per-browser ("if you change the browser, Yandex search will have to be set up again").
- Interface language and theme (light/dark/system).
- Suggestions & history: "To suggest your favorite websites and show personalized search results, Yandex uses the history of your searches and website clicks from search results"; suggestions can be disabled ("Show tips" off); history can be cleared ("deleted within a few minutes").
- Location: automatic detection by default, manual region override "to get more relevant search results".
- Home page customization tab.
- Filter search results: Family mode (sexual content completely excluded), Moderate filter (default; excluded unless the query explicitly seeks it), No filter.
- Advertising tab: "ads are served based on your location and interests" by default; personalization can be turned off.
- Ranking statement: "Yandex analyzes how well the found document corresponds to the user's query. The more useful the answer, the higher it is on the search results page. Results are ranked automatically. Yandex takes into account the ease of site navigation, its structure, the quality of texts, advertising clutter, and other site properties."

Query language articles (directly fetched):

- Operators: url: (page address, with * prefix matching), site: (site + subdomains), host:, rhost: (reversed host), domain:; mime: (file type: pdf/xls/ods/rtf/ppt/odp/swf/odt/odg/doc); lang: (ISO 639-1 code); date: (exact, <, <=, >, >=, range YYYYMMDD..YYYYMMDD, wildcard YYYYMM*, YYYY*).
- Advanced filters UI: time period selector next to the search bar (Last day / Last 2 weeks / Last month); search by region; search by language; sort by date.
- FAQ index topics (existence evidence): enable family search; disable search suggestions; "Why do you claim that a site is infected" (harmful-site warnings); "The search results page is blocked" (smart captcha on the results page); "Report an error in Yandex Search"; site-owner docs — "What is indexing?", "How to speed up indexing", "How to improve your site", favicon in results, "Site title and description in search", "add a host to the Yandex database" (site submission).

### Google / DuckDuckGo / Brave / Startpage

Unreachable this pass. No observations. No claims. Listed here to document the sampling attempt.

## Cross-product Comparison

| Dimension | Mojeek | Bing | Yandex | Evidence |
|---|---|---|---|---|
| Free-form query entry | yes (search box on homepage) | yes (implied by hub topics; homepage topic) | yes ("enter your query in the search bar") | A×3 |
| Open-web scope, self-operated retrieval corpus | yes — own crawler + index (9B pages claim) | yes — "How Bing delivers search results" exists; own index implied, body unfetched | yes — webmaster indexing docs, "add a host to the Yandex database" | A×3 (acquisition detail varies) |
| Ranked result list of outbound links | yes (core product) | yes (implied by entire help hub) | yes ("the more useful the answer, the higher it is on the search results page") | A×3 |
| Algorithmic ranking authority, disclosed qualitatively | "independent and unbiased search results" positioning | "How Bing delivers search results" doc exists | explicit: automatic ranking; site navigation/structure/text quality/ad clutter signals | A (Yandex explicit), A-implied (others) |
| Vertical tabs / scoped views | Web/Images/News/Substack tabs | images/video/news/maps topics | time/language/file-type filters; region search | A×3 |
| Query operators / advanced syntax | intitle/intext/inurl/inanchor, since/before, site | not directly observed | url/site/host/rhost/domain/mime/lang/date | A×2 (syntax product-specific) |
| Query assistance (suggestions) | suggestions exist (disable implied by settings) | "Turn search suggestions off or on" | "Disable search suggestions" | A×3 |
| Search history + control | history in hints (cookieless mode; privacy settings) | "Turn search history off or on" | history used for personalization; disable + clear | A×3 |
| Adult-content filter | Safesearch (2023) | SafeSearch | Family / Moderate (default) / No filter | A×3 |
| Harmful-site warnings | not observed | "Protect yourself from malware and phishing" | "Why do you claim that a site is infected" | A×2 |
| Ads layer | Mojeek Ads product | "Why am I seeing this ad?" | Advertising tab; ad personalization | A×3 |
| User settings surface | Preferences (Appearance/Search/Language-Location/Privacy) | hub topics imply settings | full settings article | A×3 |
| Region/language relevance | Language-Location settings tab | not directly observed | auto-detect + manual region; interface language | A×2 |
| Account-linked state | cookieless pole (no account required) | Microsoft account sign-out topic | Yandex ID-linked settings, cookie fallback | A×3 (posture varies) |
| Supply-side (webmaster) surfaces | MojeekBot doc, robots/meta handling, contact | Webmaster Guidelines exist | indexing docs, site submission, title/description/favicon docs | A×3 |
| Mobile apps / browser integration | iOS/Android apps; 12+ browser guides | Edge/Microsoft ecosystem adjacency | Yandex ecosystem (browser assumed; captcha/anti-bot observed) | A (Mojeek explicit), A-topic (Bing), partial (Yandex) |
| Instant answers / knowledge panels | Calculator quickbox; Knowledge Box (2018) | not directly observed | not directly observed | A×1 — product-specific-observed, likely common, kept weak |
| AI summaries / semantic layer | Search Summary (2024); Semantic Search (2024) | Copilot-era positioning not directly observed | not observed | A×1 — variant, current-market |
| Save/collection features | not observed | "Save search results with Bing" | not observed | A×1 — product-specific |
| Loyalty/rewards | not observed | Microsoft Rewards topic | not observed | A×1 — vendor-specific |
| Homepage-as-portal | no (bare search box posture) | homepage image/video + turn-off topics; "Explore the homepage" | home page customization tab | A×2 — variant |
| API for embedding results | Web Search API, Site Search API, search boxes | not directly observed | not directly observed | A×1 — keep qualified |

## Four-layer Abstraction

### L0 — Defining Invariant

Four structures, each removable-to-a-different-Type:

1. **Open user-composed query** — the unit of work is a free-form information need expressed by the user. Remove → browsing/curated surfaces (Directory, Portal).
2. **Retrieval corpus spanning the open public web by default** — the default target of retrieval is the whole public web, not a bounded domain or internal collection. Remove → Vertical Search Engine (scoped corpus) or enterprise Search Platform (internal corpus).
3. **Ranked result list of outbound references to external documents** — results are references (title/URL/snippet) to documents the application does not host; the user exits the application to consume them. Remove → encyclopedia/portal (hosts content) or Answer Engine (primary output is a synthesized answer).
4. **The engine is the single algorithmic ranking authority over its corpus** — ordering is computed by the engine's own relevance machinery over one retrieval corpus it operates. Remove the single-authority property and make combining several engines' outputs the defining act → Metasearch Engine; replace algorithmic ordering with human curation → Directory.

Explicitly NOT in L0 (anti-overfitting):

- **Own crawler / own index.** Google/Bing/Yandex/Mojeek all operate crawls, but Mojeek itself sources a vertical (images) externally, and the market contains engines that source web results from other engines' indexes while remaining single-corpus retrieval products. Corpus-acquisition mode (own crawl vs licensed vs hybrid) is an implementation variant, not the invariant. The invariant is that the product answers from one retrieval corpus it operates as its own — contrasted with metasearch, whose defining act is combining other engines' result lists.
- **"Ten blue links" as a specific UI.** The ranked reference list is invariant; its exact visual form is not.
- **Ads, autocomplete, tabs, knowledge panels, AI answers, accounts, history** — all common mature structure or variants.

### L1 — Common Mature Structure

Present across the sample (B-layer unless noted):

- Query assistance: suggestions/autocomplete (A×3), spell correction implied by the category (kept weak — not directly observed), related searches (not directly observed — kept out).
- Result anatomy: title, URL, snippet; plus per-result enrichments (favicon, date, sitelinks — Yandex webmaster docs confirm title/description/favicon as engine-rendered fields).
- Vertical tabs / scoped views over the same corpus (images/video/news/maps/blogs) and filter panels (time, language, file type, region).
- Query operators / advanced search syntax (A×2; exact syntax product-specific).
- Search history and suggestions with user controls (view, disable, clear) (A×3).
- Adult-content filtering modes (A×3).
- Harmful-site / malware warnings (A×2).
- Region and language settings feeding relevance (A×2 + interface language A×3).
- Ads layer distinct from organic results, with personalization controls and explanation surfaces (A×3).
- User settings surface (appearance, search behavior, privacy) (A×3).
- Supply-side machinery: robots.txt compliance, meta noindex handling, webmaster guidelines, site submission (A×3).
- Mobile apps and browser-default integration as distribution surfaces (A×1 explicit, topic-level ×2).
- Anti-abuse posture (captcha on results; crawler verification) (A×1 + A×1).
- Homepage as an entry surface — bare query box vs portal-styled is a posture variant (see L2).

### L2 — Variant / Optional Structure

- Corpus acquisition mode: own crawler-built index vs licensed/hybrid sourcing (Mojeek own-crawl A; Mojeek image vertical via Openverse A shows external sourcing inside one product; wrapper products exist in the market but were unreachable — kept conceptual).
- Privacy posture: no-tracking engines (Mojeek positioning, cookieless mode A) vs account-personalized engines (Yandex ID-linked personalization A; Bing Microsoft account A-topic).
- AI layer: generated summaries / semantic search over results (Mojeek 2024 A; current-market trend, treated as variant not core).
- Homepage posture: bare query box (Mojeek) vs portal homepage with curated content (Bing A-topics; Yandex home-page tab A).
- Account & sync depth: cookie-only settings (Yandex logged-out mode A) vs account-linked sync (Yandex ID A, Bing account A-topic).
- Instant answers / knowledge panels: calculator, infobox (A×1; likely common, not directly observed elsewhere).
- Save/collection features (Bing A×1 — product-specific).
- Rewards/loyalty monetization twists (Bing A×1 — vendor-specific-leaning).
- Embedded-results APIs / site search boxes for third parties (A×1 direct).
- Regional/ecosystem anchoring: engines embedded in a broader ecosystem (mail, browser, captcha infra) (Yandex A).

### L3 — Vendor-specific

- Mojeek: Focus (custom web-scoped searches), Search Choices, NoML campaign, FeedFetcher, OrgSearch API, published index-size milestones (9B pages), bot IP list.
- Bing: E-tree, cash donations, ethical shopping, Microsoft Rewards, Bing Pros, EU DSA information page, COVID data sources, physician profiles.
- Yandex: rhost:/domain: operator syntax, Yandex DNS + hosts-file family-search deployment for organizations, Smart Captcha, "add a host" primary-address concept, Diplodoc-documented settings granularity.
- Bing homepage E-tree/donations and Microsoft Rewards — monetization surfaces unrelated to retrieval semantics.

## Rejected Findings

- "Own crawler is definitional" — rejected: Mojeek's own image vertical is externally sourced; wrapper engines are marketed as search engines; the metasearch boundary is the aggregation act, not index ownership.
- "Ads are definitional" — rejected: monetization is a business-model surface; nothing in retrieval semantics requires it. (In-sample all three monetize via ads — recorded as common, not defining.)
- "Account/personalization is definitional" — rejected: Yandex's own logged-out cookie mode and Mojeek's no-tracking/cookieless pole satisfy the core without accounts.
- "Vertical tabs are definitional" — rejected: they are scoped views over the same broad corpus; Yandex's evidence is filter-based rather than tab-based; a bare web-only engine passes the removal test.
- "AI summaries are definitional" — rejected: 2024-era additions in the sample; pre-AI engines satisfy the core.
- "Autocomplete is definitional" — rejected: assistance layer; disabling is a supported state in-sample.

## Boundary Findings

- **vs Vertical Search Engine**: same machinery, narrowed corpus (shopping, jobs, academic, video…). Removal test: restrict the corpus to one domain and the product becomes a vertical engine. Vertical tabs inside a general engine are scoped views, not separate Types; the directory leaf should be assigned by center of gravity (default surface = open web).
- **vs Metasearch Engine**: metasearch is defined by combining results from multiple underlying engines; a general engine is the single ranking authority over one corpus it operates. Removal test: make "merge other engines' outputs" the defining act → metasearch. Wrapper products (own UI over one licensed index) sit closest to this seam and were unreachable this pass — flagged as Uncertainty.
- **vs Answer Engine**: the defining surface of this Type is the ranked reference list the user exits through; an answer engine's primary output is a synthesized answer. AI summaries layered on top of results (Mojeek Search Summary) are an additive variant — the link list remains the primary surface. Removal test: remove the ranked reference list as the primary output → Answer Engine.
- **vs Directory Application / Information Portal**: directories hold standing, hand-curated records; search engines compute transient rankings over a live corpus per query. The historical directory/search split is exactly this line. Removal test: replace algorithmic ranking with human curation over a fixed catalog → Directory.
- **vs Search Platform / Enterprise Search / Internal Knowledge Search**: those operate on organizational, permissioned corpora with member identity; this Type's corpus is the open public web with no membership requirement. Removal test: replace "public web" with "the organization's internal sources" → sibling Type.
- **vs Web Browser**: browsers are the client surface and often route address-bar input to a default engine; the engine is a destination service the browser hands queries to. Distribution integration (browser defaults, apps) is common but not definitional.
- **vs Web Archive Viewer**: retrieval finds current references; an archive viewer renders historical snapshots. Cached copies inside search results are an optional enrichment, not archival custody.
- **vs Academic Search Engine (§23)**: corpus bounded to scholarly literature + citation machinery; the general engine's scope is unbounded by design.

## Uncertainties

1. Google — the canonical product of this Type — was unreachable (3 timeouts). The doc therefore under-represents the most influential implementation (knowledge panels, AI overviews, search operators canon). If a later pass reaches Google's help center, re-verify the standard-capabilities list and the ranking-signal framing against it.
2. Bing evidence is topic-inventory level; article bodies (history/suggestions/SafeSearch/Visual Search behavior, "How Bing delivers search results") were not fetchable (404s on constructed URLs; JS-only webmaster guidelines). Bing-specific behavior claims kept at existence level.
3. The "licensed/hybrid index" variant rests on one direct observation (Mojeek sourcing image results from Openverse) plus market reasoning; the wrapper pole (Startpage/Ecosia class) was unreachable, so the metasearch-boundary placement for wrapper products is argued, not observed.
4. Ranking-signal families are documented in detail only by Yandex (site structure, text quality, ad clutter) and Mojeek positioning ("unbiased"); the full modern signal set (links, engagement, freshness weighting) is not directly evidenced in-sample and is deliberately kept qualitative.
5. Historical check is conceptual: the definition is written so that a plain query-and-ranked-links engine (the early-web form) satisfies it without tabs, ads, accounts, or panels, and so that a human-curated web catalog does not (it is the Directory). No archived source from the early-engine era was fetchable this pass, so the check is reasoned rather than cited.
6. Spell correction ("did you mean") — near-universal in the category but not directly observed in fetched pages; kept out of the standard-capabilities list or marked weak.

## Final Synthesis

A General Web Search Engine is a query-first retrieval application over the open public web. Its defining core is: the open user-composed query; a retrieval corpus spanning the open web by default, operated by the engine as its own (however acquired); a ranked list of outbound references to external documents; and the engine's own algorithmic ranking as the single ordering authority. Everything else — suggestions, tabs, filters, panels, ads, history, accounts, AI summaries, apps, APIs — is standard mature structure or a variant layered on that core. The Type's neighbors are defined by single-subtraction tests: narrow the corpus → Vertical Search Engine; aggregate other engines → Metasearch Engine; promote synthesized answers to primary output → Answer Engine; hand-curate standing records → Directory/Portal; internalize the corpus → Enterprise Search. The Type has a distinctive two-sided shape: a demand side of end users with short query sessions and near-zero persistent state, and a supply side of site owners governed by crawling/ranking rules published as guidelines rather than formulas.
