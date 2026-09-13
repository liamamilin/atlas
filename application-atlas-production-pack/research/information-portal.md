# Research Notes — Information Portal

Research date: 2026-09-07

## Research Goal

Understand what an "Information Portal" actually is as an Application Type, from real products: what its entry surface consists of, what structures it is built from, how users use it day to day, and where its boundaries lie against neighboring Types (Directory Application, Listings Platform, News Aggregator, Content Aggregator, Search Engine, Personal Dashboard, org-internal portals).

## Initial Boundary (hypothesis before research)

- Working hypothesis: the leaf names the classic **web portal** — a gateway/starting-point web destination that organizes access to a broad, continuously refreshed body of information and services from many sources.
- Nearest neighbors suspected: Directory Application (same sub-family), Listings Platform (same sub-family), News Aggregator / Personalized News Feed (02.04), Content Aggregator / Feed Reader (02.08), Search Engine (02.02), Personal Dashboard (03.13), Intranet Platform / Employee Portal (10), Government Service Portal (24).
- Risk noted up front: "portal" is an overloaded industry word (employee portal, patient portal, government portal, developer portal are all different things). The leaf must be anchored to the public general-information gateway.

## Research Questions

1. What is physically on a portal's entry surface (modules, channels, services)?
2. What are the core structures? Is there a "unit of work" like Deal/Order/Clip, or is the surface itself the unit?
3. Who produces the content — portal staff, licensed external publishers, linked sites?
4. What lifecycle do content items have? Does the surface persist while items expire?
5. What can users personalize (layout, topics, location, edition)? How does it persist?
6. What role does search play vs browse-and-click routing?
7. How are services (mail, shopping, finance) attached?
8. Where exactly is the seam to Directory Application, News Aggregator, and Personal Dashboard?

## Representative Products

Selected for market representativeness, documentation access, different product philosophies, and different eras/regions:

| Product | Why selected | Era / philosophy |
|---|---|---|
| Yahoo! JAPAN | the most complete surviving full-service portal; deep service ecosystem | full-service portal (search + news + many services) |
| Naver | living regional portal, Korean default home; block-based homepage | portal integrated with its own search engine |
| AOL | US legacy portal, now news-led | narrowed news-led gateway + mail |
| MSN | Microsoft's portal; default Edge homepage/new tab; only sample with substantial official operational docs | portal as browser-integrated start page |
| start.me / My Yahoo! / iGoogle | personalized start-page pole (user-arranged widget boards) | planned samples — access failed (see Sources) |

## Sources

### Directly observed (evidence layer A)

- Yahoo! JAPAN homepage — https://www.yahoo.co.jp/ — fetched 2026-09-07. Full portal surface visible in text.
- Naver homepage — https://www.naver.com/ — fetched 2026-09-07. JS-rendered, but accessibility skeleton names the page blocks (서비스 메뉴 service menu, 새소식 news block, 쇼핑 shopping block, 관심사 interests block, MY 영역 MY area, 위젯 보드 widget board, 보기 설정 view settings, 검색/AI 검색 search).
- AOL homepage — https://www.aol.com/ — fetched 2026-09-07. Full news-led gateway surface visible in text.

### Official operational documentation (evidence layer A)

- Microsoft Support — MSN section:
  - "MSN feedback frequently asked questions" — https://support.microsoft.com/en-us/msn/msn-feedback-frequently-asked-questions — content sourcing (thousands of publisher brands, publisher logo on every article, ad revenue shared with publishers), personalization (Personalize menu, interests, editorial override, hide/block publishers, My Interests blocked list), editions (60+, language/content selection, China rule), weather/local-news location settings, Edge homepage/new-tab feed modes (Focused / Custom / Content Off).
  - "Using the services stripe in MSN" — https://support.microsoft.com/en-us/msn/using-the-services-stripe-in-msn — services stripe on the homepage (Outlook.com, Gmail, Yahoo Mail, Facebook, Twitter, Skype, OneDrive, Office Web Apps, OneNote), per-service sign-in from the homepage, cross-device sync via Microsoft account, stripe items currently not removable.
  - "Welcome to the MSN home page" — https://support.microsoft.com/en-us/msn/welcome-to-the-msn-home-page — homepage components (Mega menu, services stripe, today stripe), customization (layout, themes, interests), cookie-vs-account persistence, settings list (account, social, privacy, market and language, home location), Bing as the search engine, and the documented link-out rule: "some of our agreements with content partners require that we take MSN customers to the originating site to view the content."

### Unreachable sources (limitations recorded)

- start.me — https://support.start.me/ and https://www.start.me/ — timed out / transport error (3 attempts). Abandoned per network rule.
- My Yahoo! — https://my.yahoo.com/ — returned only a mainland-China availability notice (geo-restricted from the research environment).
- Yahoo Help — https://help.yahoo.com/ — HTTP 403.
- Yahoo! JAPAN Help Center — https://support.yahoo-net.jp/ — JS-rendered shell ("CSS Error"), no article content fetchable.
- msn.com — JS-rendered, no content in text fetch (structure instead taken from official MSN support docs).
- Wikipedia "Web portal" — timed out twice; abandoned. Historical framing therefore rests on the sampled products themselves plus the directory-heritage visible inside them (e.g., Yahoo! JAPAN's "サービス一覧" full-services index), not on tertiary history articles.

Consequence: claims about the personalized start-page pole and about portal history are kept weak and marked as evidence-degraded. No precise numeric/time claims are made anywhere in this research beyond what fetched sources state.

## Product Observations

### Yahoo! JAPAN (direct observation of https://www.yahoo.co.jp/)

Key observations:

- The page explicitly invites "ホームページに設定する" (set as your homepage) — the portal positions itself as the browser start page. Also offers きっず版 (kids version) and アプリ版 (app version) surfaces.
- Prominent search box with vertical selectors: web, AI mode, images, videos, 知恵袋 (Q&A), maps, real-time.
- Disaster/alert layer at top (特別警報 special warnings with detail links) — urgent public information surfaced first.
- News module: continuously updated headlines with timestamps ("9/7(月) 23:53更新"), per-item comment counts, category tabs (主要/経済/エンタメ/スポーツ/国内/国際/IT/科学/地域), "もっと見る" (see more) and トピックス一覧 (topics list) link-outs; headlines attributed to outlets (e.g., 北國新聞社).
- Services navigation: 主なサービス (main services) — Shopping, Auctions, Flea market, ZOZOTOWN, LOHACO, Travel, 一休.com, ふるさと納税, 出前館, News, Weather, Sports, Finance, TV listings, Q&A, Games, Maps, Transit, Real estate, Autos, etc. — plus a full "サービス一覧" (services index) link. Commerce services are operated or affiliated (PayPay ecosystem).
- Personal module: 個人に関わる情報 (information related to you) — login ID registration, registration info, your status, Mail, おトク宝箱 daily lottery, PayPay balance check.
- Local utility module: today's/tomorrow's weather for the user's area (港区), precipitation probability, heatstroke index, rain radar, local government info, transit service delays (運行情報 9件).
- Sports scoreboard module (プロ野球/Jリーグ fixtures with "見どころ" links).
- Real-time trending keywords module (話題のキーワード with related words, "10年に1度話題のキーワード" link).
- Ads/promotions (PayPay card, EC store opening), corporate footer (LINE Yahoo Corporation).

Interpretation: the full-service portal = start page + search + refreshed multi-source news + services directory + personal area + local utilities + trends, all on one self-renewing surface that routes outward.

### Naver (direct observation of https://www.naver.com/ skeleton)

Key observations (from accessibility anchors — page blocks are named):

- 검색 / AI 검색 — search and AI search entry at top.
- 서비스 메뉴 — service menu (navigation to Naver's services).
- 새소식 블록 — "what's new" / news block.
- 쇼핑 블록 — shopping block.
- 관심사 블록 — interests block.
- MY 영역 — personal area ("MY").
- 위젯 보드 — widget board (user-arrangeable module area).
- 보기 설정 — view/display settings (layout customization).
- Naver Help (https://help.naver.com/) confirms the service breadth behind the portal: mail, MYBOX, blog, cafe, maps, train booking, local business info, shopping, etc. (help center reachable at directory level only).

Interpretation: Naver's homepage is explicitly block-structured — a service menu + refreshed content blocks + a personal area + a widget board with view settings. The portal is the front door of a search engine's service ecosystem, and the page itself is user-configurable.

### AOL (direct observation of https://www.aol.com/)

Key observations:

- Title: "News, Politics, Sports, Mail & Latest Headlines - AOL.com Home" — the portal self-describes as headlines + mail.
- Channel navigation: News, Politics, Sports, Weather, Entertainment, Finance, Food, Games, Health, Home & Garden, Shopping, Style, Travel, True Crime, Animals, Subscriptions, Local News — with dropdown sub-channels (Finance → Banking, Business News, Estate & Retirement Planning, Loans & Mortgages).
- Headline stream aggregated from many external publishers with visible attribution: Fox News, USA TODAY, TV Insider, Bored Panda, People, Reuters, AP, The Independent, BBC, The Hill, Time, Us Weekly, HuffPost, MoneyLion, TheStreet, Yahoo Sports, 24/7 Wall St., Islands, Parade, Simply Recipes, Tasting Table, Good Housekeeping, etc. Each topic module ends with "See all [topic]".
- Mail sign-in module ("Sign in / Mail") — the mail service attached to the portal.
- Weather module with "Change home location" — location-personalized forecast, hourly strip; "Local news not available now" module (location-scoped local news).
- Daily Horoscope module; Trending Now module; AOL Games module ("Play Hearts free"); newsletter signup ("daily roundup"); "Join AOL" membership; premium support phone line in header.
- Ads throughout; "From Our Partners" row; topic tag row; footer with Help/About/Advertising/Licensing/Sitemap.

Interpretation: the surviving US portal is a narrowed gateway — multi-source headlines + mail + weather/local + a few utility modules — still organized as a start surface that routes outward to publisher content and its own services.

### MSN (official documentation, support.microsoft.com)

Key observations:

- Homepage components (documented): **Mega menu** ("brings you every section in just one easy step"), **services stripe** ("all of the services that you use throughout your day all in one place"), **today stripe** ("most popular & trending topics from across MSN").
- Content sourcing (documented): "stories, galleries and videos — created by thousands of the world's best-known publishing brands. Their original work usually is not changed or altered... look for the prominent publisher logo at the top of every article." Ad revenue is shared with publishers. Sponsored/native content is labeled "Ad".
- Link-out rule (documented): "some of our agreements with content partners require that we take MSN customers to the originating site to view the content."
- Personalization (documented): Personalize menu → select/deselect interest topics; "news deemed important by our editors will still display prominently" (editorial override); per-story "Hide stories from..." with a **Blocked list** in the **My Interests** page; sign-in with Microsoft account persists personalization across devices; without sign-in, customizations live in cookies and are lost if cookies are deleted.
- Settings (documented): Microsoft account, social accounts, privacy, market and language, home location.
- Editions (documented): "over 60 editions"; language/content selection; in China only Chinese content is shown (regulatory).
- Weather/local (documented): weather card with default location + unit setting; local news location follows weather settings; local news not available in all areas.
- Search (documented): Bing is the search engine; the search bar searches the web or individual sections; results open in a new tab.
- Browser integration (documented): MSN is the Microsoft Edge default homepage and new tab page; the feed can be set to Focused mode or turned off entirely (Custom → Content Off); taskbar access uses the Windows-signed-in account.
- Services stripe (documented): Outlook.com, Gmail, Yahoo Mail, Facebook, Twitter, Skype, OneDrive, Office Web Apps, OneNote; per-service sign-in from the homepage; Facebook sign-in enables article commenting; stripe items currently cannot be removed (product-specific).

Interpretation: MSN documents the portal's anatomy more explicitly than any other sample: a start surface composed of navigation (mega menu), refreshed multi-source content (news feed with publisher attribution), services shortcuts (stripe), trends (today stripe), utilities (weather), personalization (interests/layout/themes), and regional editions — with search delegated to Bing and content often consumed at the originating publisher's site.

## Cross-product Comparison

| Structure | Yahoo! JAPAN | Naver | AOL | MSN |
|---|---|---|---|---|
| Start-page positioning | explicit "set as homepage"; kids/app editions | default home of Korean web; app | "AOL.com Home" | Edge default homepage/new tab; "start the new MSN experience earlier" |
| Search entry | prominent, with verticals (web/AI/images/video/Q&A/maps/realtime) | search + AI search | not prominent in fetched view | Bing bar; web or per-section |
| Channel/section navigation | news categories + services index | service menu | topic nav with sub-channels | mega menu + verticals (News/Weather/Money/Sports) |
| Multi-source refreshed content | headlines w/ timestamps, comment counts, outlet attribution | news block (새소식) | headlines from dozens of publishers, attributed | documented: thousands of publisher brands, logo on every article |
| Link-out to origin | news → outlets; services → sub-sites | blocks → services | "See all…" → topic pages; articles → publishers | documented partner rule: go to originating site |
| Services layer | large: shopping/auction/travel/finance/maps/games/Q&A + mail + PayPay | service menu + shopping block | mail sign-in, games, subscriptions/membership | services stripe: Outlook/Gmail/Yahoo Mail/FB/Twitter/Skype/OneDrive |
| Personal area | 個人に関わる情報 (ID, mail, PayPay balance, lottery) | MY 영역 | sign in / mail | sign-in personalization, cross-device sync |
| Local/utility modules | weather, transit delays, disaster alerts, rain radar | (not visible in skeleton) | weather + change home location, local news, horoscope | weather card + default location, local news |
| Trends | realtime trending keywords | (likely; not visible) | Trending Now | today stripe |
| Personalization/layout | kids edition; personal modules | widget board + view settings | limited in fetched view | interests, layout, themes; cookie vs account persistence; feed off mode |
| Regional editions | Japan | Korea | US/global | 60+ editions; market/language setting; China rule |
| Business model visible | ads + commerce ecosystem | ads + commerce | ads + membership | ads (revenue shared with publishers) |

### What is common to all four (cross-product commonality, evidence layer B)

1. A single persistent entry surface positioned as the beginning of a web session (start page/homepage).
2. Continuously refreshed information drawn from multiple sources, organized into channels/modules on that surface.
3. Outward routing as the primary job: search entry and/or channel navigation and/or service shortcuts; content is frequently consumed at the originating site.
4. A services layer attached to the same surface (mail everywhere; shopping/finance/maps/games in the fuller portals).
5. A personal area (sign-in, my mail, my settings).
6. Local/utility information (weather at minimum; transit/disaster/local news in several).
7. Advertising-funded free access.

### What varies (implementation variance)

- Breadth: full-service ecosystem (Yahoo! JAPAN, Naver) vs narrowed news-led gateway (AOL, MSN).
- Search prominence: own search engine front-and-center (Yahoo! JAPAN, Naver) vs delegated search bar (MSN/Bing) vs de-emphasized (AOL today).
- Personalization depth: view settings/widget board (Naver) vs interests+layout+themes (MSN) vs minimal (AOL's location setting).
- Edition model: single-market (Yahoo! JAPAN, Naver) vs multi-edition (MSN 60+).
- Content posture: portal-operated services + licensed headlines vs pure aggregation of external publishers.

## Canonical Model (abstraction)

### L0 — Defining Invariant (deliberately small)

An Information Portal is recognizable by three properties held together on one surface:

1. **The gateway entry surface** — a persistent web page that presents itself as the place where a session begins (start page / homepage), not as the destination for a single task or a single content item.
2. **The organized multi-source information space** — the surface assembles continuously refreshed information drawn from multiple sources (the operator's own services and/or external publishers), organized into channels/sections/modules.
3. **Onward routing as the primary job** — the surface's function is to route the user onward: a search entry, channel navigation, and/or service shortcuts; much of what it points to is consumed elsewhere (originating sites, sub-services).

Remove (1) → a content site / news site (a destination). Remove (2) → a bare link hub or directory page. Remove (3) → a content stream (aggregator/feed territory). All three are load-bearing.

Historical check: the 1990s portal generation (directory + search + headlines + weather + mail on one start page), regional portals, walled-garden-era gateways, and personalized start pages all satisfy these three properties without requiring any modern implementation detail. The definition does not require: a directory heritage, a mail service, personalization, accounts, news-led shape, ads, apps, or AI search.

### L1 — Common Mature Structure

- **Search entry** — usually the portal's own or an affiliated search engine, often with vertical selectors (images, video, maps, Q&A).
- **News/headline channel** — the dominant refreshed content module in surviving portals; timestamped, attributed, category-tabbed, with "see more" link-outs.
- **Services layer** — shortcuts to the operator's (or partners') services: mail, shopping, finance, maps, games, TV listings; per-service sign-in from the portal.
- **Personal area** — sign-in state, my mail, my balances, my settings.
- **Local/utility modules** — weather (location-settable), transit status, disaster alerts, local news, horoscope.
- **Trends module** — what is popular/trending now.
- **Personalization** — interests, layout, themes, home location; persisted via account and/or cookies.
- **Regional editions** — market/language scoping of content.
- **Advertising** — the free-access business model; sponsored content labeled.
- **Companion surfaces** — mobile apps, browser start-page/new-tab integration, kids/simplified editions.

### L2 — Variant / Optional Structure

- **Portal breadth poles**: full-service portal (search + news + large service ecosystem) vs news-led narrowed portal (headlines + mail + weather) vs personal start page (user-arranged widget board over feeds/bookmarks — evidence-degraded in this pass) vs vertical portal (single domain; weaker evidence, not directly sampled).
- **Directory heritage**: categorized web-index navigation as a module (the historical origin; survives as services indexes).
- **Membership/subscription layer** attached to the portal (one sample).
- **AI search/AI answers** as a new search mode (two samples).
- **Walled-garden vs open-web posture** (historical pole; today's portals are open-web routers).

### L3 — Vendor-specific (kept out of the final document)

- Yahoo! JAPAN: PayPay balance module, おトク宝箱 daily lottery, ZOZOTOWN/LOHACO/一休 service family, LINE Yahoo corporate framing, きっず版.
- Naver: named blocks (새소식/쇼핑/관심사/MY), Naver-specific service family (MYBOX, Cafe, VIBE...), ARS phone menu.
- MSN: services stripe items not removable; Edge taskbar/new-tab integration details; China content rule; Money error codes doc.
- AOL: premium support phone line, True Crime channel, "Join AOL" membership, horoscope module.

## Vendor-specific Findings

See L3 above. None of these are promoted to the canonical model. The MSN services-stripe "cannot remove items" detail is product-specific and time-sensitive; excluded from the final document.

## Boundary Findings

- **vs Directory Application** (same sub-family): a directory is a structured, browsable index of entity records (businesses, people, resources) whose job is entity lookup. A portal's channel/services navigation descends from directories (and a services index survives as one module in Yahoo! JAPAN), but the portal adds continuously refreshed multi-source content and a start-page role. **Removal test: strip the refreshed content and services, keep the categorized entity index → Directory Application.**
- **vs Listings Platform**: listings platforms carry user/merchant-submitted offers with a lifecycle (posted → expired). A portal has no listing of record; its content items are ephemeral pointers, not offers.
- **vs News Aggregator / Personalized News Feed (02.04)**: the aggregator's unit is the article stream (selected/algorithmic, single-purpose). The portal's unit is the whole entry surface organizing many kinds of information (content + services + utilities) with routing as the job. MSN is the closest sample to the seam — its homepage is feed-like — but its documented structure (mega menu, services stripe, weather, editions, start-page role) keeps it portal-shaped. **Removal test: keep only the personalized article stream → News Aggregator / Personalized Content Feed.**
- **vs Content Aggregator / Feed Reader (02.08)**: same seam, sharper for the feed reader — the reader's sources are user-subscribed; the portal's sources are operator-programmed.
- **vs Search Engine (02.02)**: the search engine's primary job is query → results. Portals embed search (often their own engine's) but browse-and-route is equally primary. Yahoo! JAPAN and Naver are portal faces of search engines; the search box is a module, not the whole.
- **vs Personal Dashboard (03.13)**: a dashboard organizes the user's own data and tasks (calendar, tasks, own metrics). A portal organizes access to public/shared information and services. The personal start page (widget board) is the drift zone: Naver's widget board personalizes a public portal; a dashboard's widgets surface one's own data. **Removal test: widgets show only the user's own data/tasks → Personal Dashboard.**
- **vs Intranet Platform / Employee Portal (10) / Government Service Portal (24) / Customer Portal (07)**: these are org-internal or transaction/service-completion surfaces with authenticated roles and case/transaction records. The Information Portal is the public, general-information gateway; no service transaction of record occurs on it.
- **vs Web Browser (02.01)**: the browser is client software; the portal is a destination. The relationship is symbiotic — portals live on the browser's start page/new tab (documented for MSN/Edge; invited by Yahoo! JAPAN).

## Uncertainties

1. The personalized start-page pole (My Yahoo!, iGoogle, start.me) could not be directly observed or documented in this pass (geo-block, 403, timeouts). Its existence as a variant is asserted only at variant level, supported indirectly by Naver's widget board + view settings and MSN's layout/theme customization. No claims about specific start-page products' current features.
2. Portal history (Yahoo Directory closure, iGoogle shutdown dates, walled-garden era) could not be source-verified (Wikipedia unreachable). No historical dates are asserted in the final document.
3. AOL's search prominence: the fetched homepage view did not surface a search box; older AOL had portal search. Treated as "search de-emphasized in the current sample view", not as a general claim.
4. Vertical information portals (single-domain portals) were not sampled; kept as a weak variant.
5. Naver's homepage content blocks were observed only as skeleton anchors (JS-rendered page); block semantics are inferred from names, marked accordingly.

## Final Synthesis

The Information Portal is the **gateway** Application Type: its world is one persistent, self-renewing entry surface that organizes access to a broad body of information and services from many sources. It has no deal, order, or clip — the surface itself is the central object, and its "content items" are ephemeral pointers (headlines, alerts, service shortcuts) that rotate while the surface persists. The defining core is the trio: gateway entry surface + organized multi-source refreshed information + onward routing (search/navigation/service links). Everything else — search verticals, mail, weather, trends, personalization, editions, ads, apps — is standard capability or variant, not definition. The Type's market center of gravity has narrowed from the 1990s "everything gateway" to news-led gateways attached to search engines and service ecosystems, with regional portals (Japan, Korea) retaining the fullest form. The sharpest boundaries: Directory Application (entity index vs refreshed gateway), News Aggregator/Personalized Feed (article stream vs whole-session gateway), Personal Dashboard (own data vs public information), and org-internal/service portals (transaction of record vs information access).
