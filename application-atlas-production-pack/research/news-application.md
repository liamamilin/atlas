# Research Notes — News Application

## Research Goal

Understand the **News Application** Application Type (DIRECTORY §02.04): what a single news publisher's own reader-facing product is, what structures define it, how it works, and where its boundaries sit against the two processed siblings in the same section (News Aggregator, Personalized News Feed), the production-side Types in §27 (News Publishing Platform, Newsroom Management System), and adjacent Types in §06/§08/§02.11.

## Initial Boundary

Working hypothesis before research:

- A News Application is the consumer-facing product of a single news publisher (newspaper, broadcaster, agency): its own journalism, presented on its own standing news surface.
- Nearest neighbors: News Aggregator (multi-publisher assembly), Personalized News Feed (per-user selection over multi-publisher corpus), News Publishing Platform (production side), Financial News & Research Platform (finance-vertical), Information Portal (portal-hosted news modules), Media Monitoring Platform (organization-side watch).
- Known pre-hung flags to discharge:
  1. news-aggregator pass (2026-09-10): joint review recommended at this leaf's pass — seam = multi-publisher feeding/assembly vs single-publisher authoring; removal test = make the product the publisher of everything it shows → News Application.
  2. financial-news-research-platform pass (§08): finance-vertical news products (MarketWatch-class) held in that Type on instrument anchoring + attached market data + investment-decision purpose + first-party editorial/analytical layer; mild flag in case §02.04 processing claims domain-vertical news products.
  3. personalized-news-feed pass (2026-09-08): forwarded pending flags to news-aggregator and news-application; defines this Type by negation ("when the stories all come from the product's own newsroom, it is a News Application").
  4. information-portal pass: portal-hosted news surfaces are packaging, not identity (MSN-class).

## Research Questions

1. What is the minimal structure without which a product is no longer recognizable as a single publisher's news application?
2. What does the publisher's own editorial surface contribute that an assembled multi-publisher flow does not?
3. Which reader-relationship structures (registration, metering, subscription, free access) are definitional vs variant?
4. How do sections, editions, breaking-news handling, and live coverage work as the surface's organizing machinery?
5. Where is the line to the production-side Types (§27) and to the aggregation/feed siblings?
6. Does the definition survive the historical check (printed newspaper, teletext, early free web editions, wire agencies)?

## Representative Products

Selected for market representation, different product philosophies, and different customer tiers:

- **The New York Times** — subscription-first national newspaper of record; the paywall/metering pole.
- **BBC News** — public broadcaster; free at the point of use; global + domestic editions; the no-commercial-gate pole.
- **The Guardian** — free at the point of use, reader-contribution funded; the open-journalism pole.
- **CNN** — ad-funded commercial broadcaster; app-first, video-led, with subscription tier; the commercial-broadcast pole.
- **AP News** — wire agency operating a direct-to-consumer surface; the agency-as-publisher boundary probe.

## Sources

Fetched directly this pass (research date 2026-09-10):

- CNN — App download/product page: https://www.cnn.com/app (Tier 2, fetched successfully)

Fetch attempts that failed (recorded per the source-access limitation rules; each abandoned after the retry limit):

- The New York Times — https://help.nytimes.com/hc/en-us/articles/115014893428 (timeout ×1), https://www.nytimes.com/ (timeout ×1) — abandoned
- BBC News — https://www.bbc.co.uk/news/help-41670342 (timeout ×1), https://www.bbc.com/news (timeout ×1) — abandoned
- The Guardian — https://www.theguardian.com/help (timeout ×1), https://support.theguardian.com/hc/en-gb (timeout ×1) — abandoned
- AP News — https://apnews.com/ (HTTP 403) — abandoned
- Le Monde — https://www.lemonde.fr/en/ (timeout ×1) — abandoned

Cross-pass first-hand evidence relied on (recorded in processed sibling research notes in this repo):

- applications/news-aggregator.md + research/news-aggregator.md (2026-09-10) — defines this Type by negation; removal test; portal-embedding note.
- applications/personalized-news-feed.md + research/personalized-news-feed.md (2026-09-08) — Apple News Tier-1 documentation (channels/topics, Today feed, editorial layer); defines the single-publisher pole.
- applications/news-publishing-platform.md + research/news-publishing-platform.md (2026-09-08) — production-side core (story records, gated revisable publication, curated front/section assemblies, delivery); Related Types row for the consumer-side counterpart.
- applications/newsroom-management-system.md (2026-09-08) — planning/assignment side.
- applications/media-monitoring-platform.md (2026-09-08) — explicitly excludes the consumer news app from that Type.
- applications/financial-news-research-platform.md (§08) — finance-vertical holding seam.

## Product Observations

### CNN (directly observed this pass — Evidence Layer A, Tier 2 product page)

From https://www.cnn.com/app (fetched 2026-09-10):

- Positioning: "Understand the world. Download the CNN app." / "The fastest way to stay updated on the stories you need to know." — a single brand's own news product, app-first.
- A deep section taxonomy organizes the surface: US (with sub-beats: Crime & Justice, Immigration, Education, Transportation, Race & Identity), World (by region), Politics (incl. Elections, Facts First fact-checking, Polls), Business, Markets, Health, Entertainment, Style, Travel, Sports, Science, Climate, Weather, and standing war-coverage sections. Sections are the publisher's own editorial organization of its own coverage.
- Video is a first-class surface: Watch (featured, shows & films, network TV live stream, clips, "CNN Headlines" fast-video product, CNN 10, TV schedule).
- Audio surface: Listen (podcasts incl. a daily brief "CNN 5 Things").
- Games module (crossword, sudoku, quizzes) — engagement modules beside the news.
- Newsletters as a delivery channel (a dedicated newsletters surface).
- "Topics you follow" — a personalization layer exists inside the publisher's own product.
- Subscribe — a paid subscription offering exists beside the ad-funded surface.
- Regional structure in navigation (US edition anchor; world regions as sections).
- Account machinery: sign in, settings, my account.

Evidence layer: A (direct, Tier 2). What this page does not document: metering mechanics, push behavior, offline reading, app-internal layout. No claims made on those.

### The New York Times (not directly reachable — Evidence Layer C only)

Help center and product page both timed out. From the sibling passes and general market position: subscription-first digital newspaper; the metering/paywall pole; digital editions (app + web + games + cooking + wirecutter + audio as sibling products under one subscription brand). **No feature-level claims are made in the final document from this pass.** Listed as a market anchor for the subscription pole.

### BBC News (not directly reachable — Evidence Layer C only)

Both BBC URLs timed out. Market position: public broadcaster, free at the point of use, no commercial gate, global + UK editions. Listed as a market anchor for the public-broadcaster pole. No feature claims.

### The Guardian (not directly reachable — Evidence Layer C only)

Both Guardian URLs timed out. Market position: free at the point of use, reader-contribution and supporter-funded ownership structure, "open journalism" positioning. Listed as a market anchor for the reader-funded pole. No feature claims.

### AP News (not directly reachable — Evidence Layer C only)

HTTP 403. Market position: wire agency (content supplier to other publishers) that also operates a direct-to-consumer news surface. Important as the boundary probe: the agency's syndication feed alone is not a News Application; the agency's own consumer surface is. No feature claims.

## Cross-product Comparison

| Dimension | CNN (A) | NYT (C) | BBC News (C) | Guardian (C) | AP News (C) |
|---|---|---|---|---|---|
| First-party newsroom corpus | yes (own reporting) | yes | yes | yes | yes (own agency reporting) |
| Standing editorial surface (front/sections) | yes (documented taxonomy) | yes (market) | yes (market) | yes (market) | yes (market) |
| Commercial gate | subscription exists beside ads | subscription/metering pole | none (public funding) | none (contribution-funded) | free/ads (market) |
| Video/live | first-class (documented) | present (market) | present (market) | present (market) | present (market) |
| Personalization layer | "Topics you follow" (documented) | present (market) | present (market) | present (market) | limited (market) |
| Engagement modules | games, podcasts, newsletters (documented) | games/cooking/audio sibling products (market) | sport/weather/live (market) | live blogs (market) | minimal (market) |

The comparison is deliberately coarse: only the CNN column rests on this pass's direct observation; the others are market-orientation anchors whose details were not verifiable this pass. The structural commonality that matters — first-party corpus + standing editorial surface + direct audience channel — is supported by the CNN observation plus the sibling passes' first-hand definitions of the neighboring Types (which define this Type by negation from both sides).

## Canonical Abstraction

### L0 — Defining Invariant

Three jointly-held structures:

1. **First-party newsroom corpus** — the stories the product presents are the publisher's own journalism, produced by its own editorial operation. The product is the publisher of what it shows; it authors, it does not feed. Remove → the multi-publisher feeding/assembly Types (News Aggregator, Personalized News Feed).
2. **The publisher's standing editorial surface** — a continuously updated consumption surface organized by the publisher's own editorial judgment: front page, sections, editions, breaking-news placement. Remove → a raw stream or archive of the publisher's output (feed/archive territory), or the production-side system (§27).
3. **The publisher's direct audience channel** — the product is operated by (or for) the publisher as its own audience surface; the reader's relationship is with the publisher itself, under the publisher's brand and editorial voice. Remove → a syndication or licensed-hosting surface (third-party assembly/packaging).

Jointly-held load-bearing:

- 1 alone = a content supplier / syndication feed (the wire-out pole)
- 2 without 1 = an assembled flow of others' news = aggregator territory
- 3 without 1+2 = a brand shell with nothing of the publisher's own behind it
- 1+2 without 3 = the publisher's output presented on someone else's surface (licensed hosting/syndication packaging)

### L1 — Common Mature Structure

Present across the market's mature products (Layer B, supported by CNN direct observation + sibling-pass evidence):

- section/topic taxonomy organizing the corpus (CNN documented)
- breaking-news handling and continuous in-day updates
- video and live coverage surfaces (CNN documented)
- audio: podcasts, daily briefs (CNN documented)
- newsletters as a delivery channel (CNN documented)
- a personalization layer inside the publisher's product (CNN "Topics you follow" documented)
- registration/accounts, push notifications
- search and archives
- engagement modules (games, quizzes — CNN documented)
- regional/international editions

### L2 — Variant / Optional Structure

- **Commercial posture** — subscription/metering (NYT pole), free + advertising (CNN pole), public funding (BBC pole), reader contributions (Guardian pole), free agency surface (AP pole). NOT definitional: the historical check shows free, ungated publisher products satisfy the core.
- **Vertical scope** — general news vs a strong vertical emphasis (business, sports); a finance-vertical product with instrument anchoring + market data + investment purpose stays in Financial News & Research Platform (flag ratified below).
- **Modality emphasis** — text-led (newspaper pole) vs video-led (broadcaster pole) vs audio-brief-led.
- **Platform packaging** — web site, native apps, widget/lock-screen surfaces, print edition as sibling artifact.
- **Bundled non-news products** — games, cooking, shopping guides, weather; these are engagement/commerce extensions, not identity.

### L3 — Vendor-specific (Research Notes only)

- CNN's specific section names, "CNN Headlines" fast-video product, "CNN 10", "5 Things" brief, CNN Underscored commerce vertical, Bleacher Report sports brand linkage — product-specific facts from the fetched page, kept here.
- NYT's sibling-product bundling (Games/Cooking/Wirecutter/Audio) under one subscription — market-level, not verified this pass.

## Historical / Market-Sample Check (§24 reasoning)

Would older, regional, platform-native products still fit the L0?

- **The printed daily newspaper** — first-party newsroom corpus (own reporters), standing editorial surface (front page + sections, produced fresh per edition), direct audience channel (the publisher's own readership). Fits. The digital News Application is this Type's current realization, not a new Type.
- **Teletext services (broadcaster text news, e.g. Ceefax-class)** — broadcaster-operated, first-party news operation, standing editorially-organized pages, continuously updated. Fits.
- **Early free newspaper web editions (no registration, no paywall, no app)** — fit. Confirms registration/subscription/paywall are variant, not core.
- **A wire service feeding other publishers (no consumer surface)** — fails legs 2+3: content supplier, not a News Application. Confirms the boundary.
- **A state/party news organization's consumer product** — fits the core (first-party corpus, standing surface, direct channel); editorial posture is a variant axis, not a boundary.

The definition survives the historical check; nothing era-specific (apps, paywalls, personalization, push) is in the core.

## Vendor-specific Findings

- CNN: section taxonomy as fetched; Watch/Listen/Games module structure; "Topics you follow"; subscription offering; regional nav structure. (Layer A, this pass.)
- NYT/BBC/Guardian/AP/Le Monde: no vendor-specific findings recorded this pass — sources unreachable; nothing filled from memory.

## Boundary Findings

| Neighbor Type | Seam | Removal test |
|---|---|---|
| News Aggregator | multi-publisher feeding/assembly vs single-publisher authoring | make the product the publisher of everything it shows → News Application; make it feed many publishers → aggregator |
| Personalized News Feed | per-user selection across a multi-publisher corpus vs the publisher's own output | collapse the corpus to one publisher → News Application; per-user selection is at most an optional layer here |
| News Publishing Platform (§27) | production system of record vs reader-facing consumption product | different users and objects; served through content APIs; ratified from that side, confirmed here |
| Newsroom Management System (§27) | planning/assignment of the work vs consumption of the output | strip planning → still a News Application; strip the audience surface → planning tool |
| Financial News & Research Platform (§08) | instrument anchoring + attached market data + investment-decision purpose + first-party editorial/analytical layer vs general news with business/markets as sections | a Markets/Business section inside a general news product stays here; the finance-vertical instrument-anchored product stays there |
| Media Monitoring Platform (§06) | organization-side standing watch over its own media presence vs consumer news consumption | that pass explicitly excludes the consumer news app; no overlap |
| Information Portal (§02.11) | whole entry surface (content + services + routing) vs the publisher's own news surface | portal-hosted news modules are packaging, not identity (MSN-class note carried) |
| Blogging Platform | author-owned dated post stream without editorial gate/front-page assemblies | no editorial organization → blog, not a news application |
| Video Streaming Platform | video as one module of the news surface vs the catalog of shows/films as the artifact | strip the news surface → streaming platform |
| Podcast Platform | audio shows as the artifact vs audio as one channel of the news surface | strip the news surface → podcast platform |
| Social Network / social feed Types | connection graph as distribution substrate vs publisher audience | the user is an audience member here, not a member of a graph |

## Flag Dispositions (this pass)

1. **news-aggregator joint-review flag — DISCHARGED, keep-both RATIFIED from this side.** The seam holds in both directions: the aggregator's defining corpus is multi-publisher with visible provenance and shared assembly; this Type's defining corpus is first-party with the publisher as author. The removal test is symmetric and clean. One product commonly hosts both surfaces (a publisher's app may carry an "aggregation-like" curated flow of partners' content beside its own reporting) — packaging beside the core, not identity.
2. **financial-news-research-platform flag — RATIFIED from this side.** §02.04 processing makes no claim on domain-vertical finance news products: instrument-anchored, market-data-attached, investment-purpose products stay in that Type. A general news application carrying Business/Markets sections (CNN documented) remains in this Type — sections are editorial organization, not instrument anchoring.
3. **personalized-news-feed forwarded flags — DISCHARGED.** The single-publisher pole is confirmed as this Type's identity; the attribution upgrade (provenance load-bearing in news scope) is consistent here — the publisher's branding IS the product's identity, provenance is trivially first-party.
4. **information-portal packaging note — carried and confirmed**: portal-hosted news surfaces are packaging; the artifact test (publisher's own news surface vs whole entry surface) holds.
5. **news-publishing-platform consumer-side row — CONFIRMED from this side** (that pass ratified it from the production side).

## Uncertainties

- Only one product (CNN, Tier 2 product page) was directly documentable this pass; the environment timed out on all other vendor surfaces (NYT, BBC, Guardian, Le Monde) and blocked AP (403). All product-specific claims beyond CNN are avoided in the final document; market-level statements rest on sibling-pass first-hand evidence and are worded accordingly.
- The precise mechanics of metering/paywall variants (free-article counts, thresholds) were not researched; no numeric claims are made anywhere.
- The historical check (print newspaper, teletext) is conceptual — no archival sources were reachable; the argument is structural, not documentary.
- Whether a strongly vertical non-finance news product (e.g., a sports-only publisher product) is a Variant of this Type or shades toward a different Type was not deeply probed; held as Variant pending evidence.

## Final Synthesis

The News Application is the single news publisher's own reader-facing product. Its defining core is three jointly-held structures: a first-party newsroom corpus (the product publishes what it shows), the publisher's standing editorial surface (front page/sections/editions, continuously updated by the publisher's own editorial judgment), and the publisher's direct audience channel (the reader's relationship is with the publisher itself, under its brand and editorial voice). Everything commonly associated with modern news products — apps, paywalls, personalization, push, video, games, newsletters, regional editions — is standard or variant structure, not definition. The Type is the digital continuation of the newspaper/broadcaster consumer product; the historical check passes. Boundaries to the aggregation/feed siblings rest on the authoring-vs-feeding seam (ratified jointly); boundaries to §27 rest on production-vs-consumption; the finance-vertical seam is ratified without claiming vertical products.
