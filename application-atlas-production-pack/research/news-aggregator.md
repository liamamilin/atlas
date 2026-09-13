# Research Notes — News Aggregator

Research date: **2026-09-10**

## Research Goal

Understand the News Aggregator as an Application Type: what its world consists of, how a product assembles a *shared* news flow from many publishers, how that shared machinery relates to per-user personalization (which sibling passes say is optional here, definitional elsewhere), and where it separates from its processed siblings — Content Aggregator (§02.08), Feed Reader (§02.08), Personalized News Feed (§02.04), Information Portal (§02.11) — and its unprocessed §02.04 sibling (News Application). Four prior passes left flags this pass must discharge:

- **content-aggregator** (§02.08, processed): "same machinery, news-only scope (Techmeme self-labels 'tech news aggregator')" — joint review recommended when this leaf processes.
- **feed-reader** (§02.08, processed 2026-09-07): four-sibling family test — "collection+curator (curation) / stream+product-machinery (aggregator) / user-assembled subscription list (reader) / per-user inference (personalized feed)", with news-only scope shading to the News Aggregator.
- **personalized-news-feed** (§02.04, processed 2026-09-08): "machinery seam = shared product-side assembly vs per-user selection, expect one product to host both surfaces (editorial front page + personal flow) in the same news product — joint review recommended when that leaf processes."
- **financial-news-research-platform** (§08, processed): mild flag — vertical finance news products held there on instrument anchoring + market data + investment-decision purpose; revisit if this pass claims domain-vertical news products.

## Initial Boundary (hypothesis before research)

Working hypothesis: a News Aggregator is a news-scoped consumption application whose defining act is **product-side assembly of a shared news flow** — the product crawls/collects journalistic stories from many identifiable publishers, clusters and ranks them with machinery (editors, scoring, clustering) that is the same for every reader, and presents the result as a standing flow. Per-user personalization is at most an optional tuning layer. The product feeds the news; it does not (normally) author it.

Expected confusions:

- Content Aggregator (§02.08, processed) — same machinery, all-content scope
- Personalized News Feed (§02.04, processed) — per-user selection is the core there
- Feed Reader (§02.08, processed) — the user's subscription list is the sole selector there
- News Application (§02.04, unprocessed) — a single publisher's own product
- Information Portal (§02.11, processed) — whole-session gateway vs article stream
- General Web Search Engine (§02.02) — per-query results vs standing flow
- Social feed Types (§01.05) — social-graph distribution vs editorial/algorithmic assembly

## Research Questions

1. What is the unit of the flow (the story), and what does it carry (headline, publisher/source, recency, topic, cluster membership)?
2. Who/what assembles the flow: editors, ranking models, clustering, crawling? Is the assembly shared (same for everyone) or per-user?
3. How does clustering work — are multiple versions of the same story merged into one story with many sources attached? Is source attribution visible and load-bearing?
4. What role does the editorial layer play vs the algorithmic layer? Are both required?
5. Is per-user personalization present, and is it core or optional tuning?
6. Does the product host content or link out to publishers?
7. What user actions exist on the flow (read, follow topics/sources, save, share)?
8. Boundaries: vs each sibling and adjacent Type; where do portal-embedded news modules sit?

## Representative Products

Selection intent: market representation + different product philosophies (pure-editorial machinery vs editor+algorithm hybrid vs platform-native mixed product) + different customer tiers. Reality constraint: the research environment could reach only two vendors' surfaces this pass; the reachable sample differs from the ideal sample, and the Type family is heavily ratified by four processed sibling passes, which compensates partly.

| Product | Pole | Evidence tier |
|---|---|---|
| Techmeme | editorial-machinery pole: crawler + filtering tools + editors making final calls on a shared front page; self-labels "tech news aggregator" | **Tier 1 — fetched 2026-09-10** (About page) |
| AllTop | editor+algorithm hybrid with explicit clustering layer; prediction-market context module; MyAllTop personal feeds as optional layer | **Tier 1 — fetched 2026-09-10** (homepage + About page) |
| Apple News | platform-native news product hosting the aggregator surface (editor-selected top stories) beside a per-user flow | **Tier 1 in the personalized-news-feed pass (2026-09-08); Layer B here** |
| Google News | search-giant algorithmic news aggregation | **Tier 2 only** — one official positioning sentence (Google blog index, recorded in the personalized-news-feed pass); all feature documentation unreachable both passes |
| Drudge Report | single-editor headline-aggregation ancestor pole | **Tier 1 in the content-aggregator pass; Layer B here** |

## Sources

Fetched successfully (2026-09-10):

- Techmeme — About page: https://techmeme.com/about (editorial pyramid: editors make final calls + write headlines; news filtering/discovery tools automatically re-sort the front page; underlying crawling technology; "the only tech news aggregator"; sister sites incl. memeorandum which runs *without* human editors; River view; Leaderboards)
- AllTop — homepage: https://www.alltop.com/ (ranked stories with per-story source counts "11 sources", source links to multiple outlets, topic sections, live-updated marker)
- AllTop — About page: https://www.alltop.com/about (three layers: editors decide top stories; ranking model scores every story continuously from freshness/outlet count/authority/coverage velocity with corroboration holdback and lead-stability safeguards; clustering groups incoming articles by meaning so "twenty versions of the same headline become one story with twenty sources attached"; MyAllTop personal feeds — follow topics and sources, save stories, reading list — explicitly "separate from market browsing")

Sibling-pass carry-over (recorded there at Tier 1; used here as Layer B):

- research/personalized-news-feed.md — Apple News User Guide observations (Today = editor-selected top stories + followed stories; channels as first-class publisher objects; restrict-to-followed mode); Google News positioning sentence
- research/content-aggregator.md — Techmeme/AllTop/Drudge observations; "attribution load-bearing" for aggregation; the four-sibling family test wording
- research/feed-reader.md — NetNewsWire/Feedbin anti-algorithm positioning; subscription-list-as-sole-selector
- research/information-portal.md — whole-session-gateway test

Unreachable this pass (abandoned per the 1–2 failure rule):

- support.google.com/news (×2 timeout), news.google.com (×1 timeout) — no claims about Google News features beyond the positioning sentence
- support.apple.com (404 ×2 on guide URLs) — Apple News claims rest on the prior pass's Tier-1 fetches
- about.flipboard.com (×1 timeout), smartnews.com (×1 timeout) — no claims about Flipboard or SmartNews

**Source-access limitation (material):** only Techmeme and AllTop could be documented first-hand this pass. Claims about the broader market rest on (a) these two Tier-1 fetches (direct), (b) the four processed sibling passes' Tier-1 evidence (Layer B), and (c) canonical inference. No feature claims are made about Google News, SmartNews, or Flipboard beyond what prior passes recorded.

## Product Observations

### Techmeme (evidence layer A — fetched 2026-09-10)

**Self-identification.** "It is the only tech news aggregator great enough for top CEOs. By sourcing news from thousands of outlets, we're uniquely able to highlight the best and earliest reports on important industry events."

**The assembly machinery is explicitly a people+software pyramid.** "Techmeme's aggregation is made possible by people and software forming a sort of editorial *pyramid*. At the top, editors make final calls on what we feature, and write descriptive, straightforward headlines for that news. Below that are news filtering and discovery tools that our editors rely on and which automatically re-sort our front page. And underlying both is our state-of-the-art crawling technology."

**The flow is shared.** One front page, automatically re-sorted by the machinery; a "River" view offers "pure reverse chronological order" as an alternative rendering of the same shared corpus. Editors work "around the clock" across five continents — the flow is continuously refilled.

**Scope is vertical.** Techmeme aggregates technology news; sister sites aggregate for other scopes (Mediagazer — media industry; memeorandum — politics; WeSmirch — celebrity). Notably, memeorandum and WeSmirch "run *without* human editors" — direct evidence that the editor layer is removable while the product remains an aggregator in the same family.

**Attribution and provenance.** The front page links out to the originating outlets; the Leaderboards product ranks authors and sources — the source is a first-class object in the model.

**No per-user surface.** Nothing on the fetched page describes per-user feeds or personalization; the surface is the same for every reader. (Newsletter subscription exists as a delivery channel, not a personal flow.)

### AllTop (evidence layer A — fetched 2026-09-10)

**Positioning.** "AllTop ranks the stories moving across the web" — "one place to see what is rising, where it is being covered, and which sources are adding new information."

**Three explicit assembly layers.**
1. "Editors decide the top stories — The ranking model surfaces candidates and sorts the feed, but a human makes the final call on what leads the homepage and how the headline is framed."
2. "The ranking model scores every story continuously — Each story gets a score built from how fresh it is, how many separate outlets are covering it, the authority of those outlets, and how fast new coverage is arriving… Two safeguards keep it steady: a story only one outlet is running gets held back until others corroborate it, and a story already leading holds its place unless a challenger clearly outscores it."
3. "Clustering and ingestion do the groundwork — Incoming articles are grouped by meaning, so twenty versions of the same headline become one story with twenty sources attached rather than twenty separate entries. That source count is what feeds the ranking above it."

**The story is the unit, and it is a cluster.** The homepage shows stories with source attribution ("Holly Otterbein / Axios", "11 sources", "27 sources") and links to the multiple outlets covering the same story ("More: The Hill, Al Jazeera English, NPR Politics, Washington Post…"). Provenance is visible and structural.

**Standing, continuously refilled flow.** "LIVE · updated 25s ago"; the ranking model "updates every few minutes, so the feed reflects the last few hours rather than whatever broke first."

**Topic sections.** Politics, Sports, Crypto, Tech, Business, AI, World, Science, Weather, Culture — the shared flow is organized by topic sections, each a rendering of the same machinery over a narrower corpus.

**Per-user layer is explicitly optional and separate.** "MyAllTop preserves the personal feed workflow: follow topics and sources, save stories, and keep a reading list that is separate from market browsing." The About page lists "My — Personal feeds" as one layer beside the shared ranked flow — the personal feed is a companion surface, not the product's core.

**Vertical module (prediction markets).** A distinct signal layer (Kalshi/Polymarket pricing) attached beside stories — "stories remain stories, market prices remain market prices." This is a product-specific extension, not family structure.

### Apple News (evidence layer B — Tier 1 in the personalized-news-feed pass, 2026-09-08)

- "Today … presents top stories selected by Apple News editors and stories from the channels and topics you follow" — the shared editorial surface (editor-selected top stories) and the per-user flow coexist in one product, exactly as the personalized-news-feed pass predicted for this leaf.
- Publisher as first-class object: channels are followable/blockable/subscribable; "Go to Channel" from a story.
- The restrict-to-followed mode narrows the personal flow to followed channels and strips the editorial surfaces — in-product evidence of the reader pole as an option.

### Google News (evidence layer A, thin — one positioning sentence, prior pass)

"Organizing what's happening in the world to help you learn about the stories that matter." No feature claims; treated as structural context only.

### Family seam evidence from processed sibling passes (evidence layer B)

- **content-aggregator pass**: the aggregator's flow is shared — "the same for everyone"; per-user feeds at most an optional tuning layer (AllTop MyAllTop); **attribution load-bearing** ("unattributed rehosting is not aggregation"); Techmeme self-labels "tech news aggregator" (same machinery, narrower scope).
- **feed-reader pass**: the reader's subscription list is the sole selector with faithful, complete, recency-ordered delivery; reader vendors define themselves against the algorithmic pole.
- **personalized-news-feed pass**: per-user selection is the core there; the aggregator is the fallback when per-user selection is removed; Apple's Today feed mixes both regimes in one product.
- **information-portal pass**: the portal's artifact is the whole entry surface; "keep only the personalized article stream → News Aggregator / Personalized Content Feed."

## Cross-product Comparison

| Dimension | Techmeme (A) | AllTop (A) | Apple News (B) | Feed Reader (B) | Personalized News Feed (B) |
|---|---|---|---|---|---|
| Corpus | tech news from thousands of outlets | news across topics from many outlets | stories from many publications (channels) | items from the user's own subscriptions | news from multiple publishers |
| Who selects between items | product machinery (editors + tools + crawler), same for everyone | product machinery (editors + ranking model + clustering), same for everyone | editors for top stories; per-user machinery for the personal flow | the user's list (faithful delivery) | the product, per user |
| Per-user variation | none documented | optional (MyAllTop companion feed) | yes (Today differs per user) | personal list, no inference | yes, by definition |
| Clustering | implied (front page highlights best reports per event) | explicit: articles grouped by meaning into one story with N sources | not documented | none (items are per-subscription) | not documented |
| Attribution | load-bearing (links out; source leaderboards) | load-bearing (per-story source counts + outlet links) | structural (publisher = channel) | primary (subscriptions are origins) | in-core for news scope |
| Editorial layer | the editors ARE the top layer | editors make the final call on leads | editor-selected top stories inside the feed | none | standard, removable via restrict-to-followed |
| Ordering | auto re-sorted front page; River = reverse-chron alternative | scored ranking with stability safeguards | ranked/mixed | chronological | ranked/mixed |
| Standing flow | yes (24/7 editors; auto re-sort) | yes (updated every few minutes) | yes | yes | yes |
| Scope | news (tech vertical) | news (multi-topic) | news | any feed content | news |

Stable across the sample: a multi-publisher news corpus; product-side assembly machinery (human, algorithmic, or both) operating on a **shared** flow; visible provenance per story; a standing, continuously refilled surface. Per-user variation appears only as an optional companion layer (AllTop) or as a sibling surface inside the same product (Apple).

## Abstraction Levels

### L0 — Defining Invariant (deliberately small)

A News Aggregator is recognizable by exactly this structure:

```text
Sourced news corpus: journalistic stories about current events drawn from
  multiple identifiable publishers (the product feeds the news; it does
  not have to be the publisher) — each story carrying its source
  └── Shared product-side assembly: the product's machinery — editors,
        ranking/scoring, clustering, crawling, in any combination —
        selects, merges, and orders the flow, and the assembled flow is
        the same for every reader (per-user selection is at most an
        optional tuning layer beside it)
        └── The standing news flow: a continuously refilled consumption
              surface of the assembled stories
```

Three legs, jointly held:

- Remove the sourced multi-publisher corpus (or provenance) → a single publisher's product is a News Application; an unattributed rehost is not aggregation at all (family-ratified: attribution load-bearing).
- Remove the shared product-side assembly → per-user selection makes it a Personalized News Feed; a user-assembled subscription list makes it a Feed Reader. The "aggregator" is gone — what remains is selection by someone else.
- Remove the standing refilled flow → a one-shot digest or a per-query result list; the "flow" is gone.

Notes on the L0 boundary:

- **Machinery composition is not definitional.** Editors-only (Techmeme's top layer), algorithm-only (memeorandum/WeSmirch "run without human editors" — direct Tier-1 evidence), or hybrid (AllTop's three layers) all satisfy. The invariant is that *the product assembles a shared flow*, not who or what does the assembling.
- **Clustering is load-bearing-adjacent but held at L1.** AllTop documents it explicitly and makes source counts feed ranking; Techmeme implies it ("best and earliest reports on important industry events"). Multiple versions of one story becoming one story with sources attached is the aggregator's characteristic act — but a headline-link aggregator without explicit clustering (Drudge-class, Layer B) still satisfies the core, so clustering is standard structure, not invariant. What IS invariant is that the flow's unit is the story *as sourced from publishers*, with provenance visible.
- **Scope is the seam vs Content Aggregator, not a fourth leg.** Same machinery; corpus restricted to news/journalism. Mirrors the ratified seam.
- **Vertical scope (tech, politics, finance) is a variant.** Techmeme is a tech-news aggregator; the machinery is identical. The financial-news-research-platform flag is answered: domain-vertical news products with instrument anchoring + market data + investment purpose stay in that Type; a plain vertical news aggregator (Techmeme-class) is this Type with a vertical corpus.

### L1 — Common Mature Structure (standard capabilities)

- **Clustering of duplicate coverage** — articles about the same event grouped into one story with multiple sources attached; source counts feeding prominence (AllTop direct; Techmeme implied).
- **Editorial layer** — editors making final calls on what leads and how headlines read (Techmeme direct, AllTop direct); removable in principle (memeorandum runs without editors).
- **Ranking/scoring machinery** — freshness, outlet count, source authority, coverage velocity as scoring inputs, with stability safeguards (AllTop direct).
- **Alternative renderings of the same flow** — ranked front page vs pure reverse-chronological river (Techmeme River direct); topic sections as narrower renderings (AllTop direct).
- **Topic sections/verticals** — the shared flow organized by topic (AllTop direct; Techmeme as a vertical itself).
- **Link-out to publishers** — the flow hands the reader to the source (Techmeme, AllTop direct); in-app hosting is the platform-native variant (Apple, Layer B).
- **Follow/save tuning layer** — optional personal feeds beside the shared flow: follow topics and sources, save stories, reading list (AllTop MyAllTop direct).
- **Newsletter delivery** — the flow delivered by email as a companion channel (Techmeme direct).
- **Search/navigation** — finding stories/topics within the flow (AllTop search bar direct).

### L2 — Variant / Optional Structure

- **Vertical scope** — general news vs tech (Techmeme) vs media (Mediagazer) vs politics (memeorandum) vs celebrity (WeSmirch); same machinery, narrower corpus.
- **Editorial posture** — editors-in-the-loop vs machinery-only vs hybrid; a spectrum, not a binary Type boundary.
- **Hosting model** — link-out (Techmeme/AllTop) vs in-app licensed hosting (Apple News, Layer B); provenance is the invariant, hosting is not.
- **Per-user companion layer** — personal feeds, follows, saved stories (AllTop MyAllTop direct; Apple's per-user flow as a sibling surface in the same product).
- **Attached context modules** — prediction-market pricing beside stories (AllTop, product-specific); scores/standings; weather.
- **Commercial model** — advertising/sponsorship (Techmeme direct), data sales (Techmeme Leaderboards), subscription tiers (Apple, Layer B).
- **Packaging** — standalone web product vs surface inside a platform news app vs module inside an information portal (MSN-class, Layer B); portal nesting is packaging, not identity.
- **Regional editions** — availability varies by region (family norm).

### L3 — Vendor-specific Detail (research notes only)

- Techmeme: "editorial pyramid" terminology; River view; Leaderboards (author/source ranking data sales); Sponsor Posts ($7k–$21k/month positions); Featured Podcast Players; paid event listings; sister-site family (Mediagazer, memeorandum, WeSmirch); five-continent editor team; 2005 launch, self-funded.
- AllTop: three-layer architecture naming; ranking inputs (freshness/outlet count/authority/velocity); corroboration holdback (single-outlet stories held until corroborated); lead-stability safeguard (incumbent lead holds unless clearly outscored); "updated 25s ago" live marker; MyAllTop; Kalshi/Polymarket market module with volume/OI dashboards; "News first, markets where useful" editorial rule; topic section list; editorial team roster.
- Apple News (from prior pass): channels terminology; Today composition; restrict-to-followed side effects; Suggested/Stop Suggesting; on-device intelligence posture.

## Rejected Findings (considered, not promoted)

- **"The Type = Google News-class algorithmic products"** — rejected: Techmeme is editor-led and is a self-labeled aggregator; memeorandum runs with no editors and stays in the family. Machinery composition is a variant.
- **"Editors are definitional"** — rejected: direct Tier-1 evidence of family products running without editors (memeorandum/WeSmirch).
- **"Clustering is definitional"** — rejected: strongly documented in one product (AllTop) and implied in another; the Drudge-class headline-list ancestor (Layer B) satisfies the core without explicit clustering. Held as standard structure.
- **"Per-user personalization is part of the Type"** — rejected: it is the *sibling's* invariant; here it is documented only as an optional companion layer (MyAllTop) or a co-hosted sibling surface (Apple Today). Promoting it would collapse the machinery seam ratified by three passes.
- **"The aggregator must link out"** — rejected: hosting is a variant; provenance is what survives across implementations.
- **"Vertical scope is definitional"** — rejected: Techmeme/Mediagazer/memeorandum differ only in corpus scope; the general-news form is the same Type.
- **"Accounts are definitional"** — rejected: Techmeme's shared flow requires no account; the personal layer is optional.
- **"Prediction-market/market-data modules are part of the Type"** — rejected: product-specific extension (AllTop); the financial-news-research-platform flag resolved accordingly.

## Boundary Findings

1. **vs Content Aggregator (§02.08, processed) — joint-review flag DISCHARGED from this side; keep both RATIFIED.** The assembly machinery is identical in kind (product-side selection over a standing refilled stream); the seam is **corpus scope**: this Type's corpus is news/journalism from identifiable publishers with provenance load-bearing; the generic sibling spans content kinds. Removal test: widen the corpus beyond news with no other change → Content Aggregator; restrict a generic aggregator's corpus to publisher journalism → this Type. Consistent with the ratified seam; no taxonomy change recommended.
2. **vs Feed Reader (§02.08, processed) — flag DISCHARGED from this side.** The reader's subscription list is the sole selector with faithful, complete delivery of the user's chosen sources; here the product's machinery selects across a corpus the user never enumerated, and completeness is not promised. Removal test: replace product machinery with the user's list as the sole selector → Feed Reader.
3. **vs Personalized News Feed (§02.04, processed) — joint-review flag DISCHARGED from this side; keep both RATIFIED.** The machinery seam holds: the aggregator's flow is assembled once and shared by everyone; per-user selection is at most an optional tuning layer. There, per-user assembly is the core: without the user's signals the primary surface cannot render. The expectation from their pass was confirmed: one product hosts both surfaces (Apple's Today feed mixes editor-selected top stories with per-user stories; AllTop runs the shared ranked flow beside MyAllTop). Removal test: remove per-user selection → this Type; make per-user selection the core → Personalized News Feed.
4. **vs News Application (§02.04, unprocessed)** — a single publisher's own product (its editors, its editions, its reporting). Here the corpus is multi-publisher and the product's job is feeding/assembly, not authoring. Removal test: make the product the publisher of everything it shows → News Application. Flag left for that leaf's pass.
5. **vs Information Portal (§02.11, processed)** — the portal's artifact is the whole entry surface (content + services + routing); keep only the assembled article stream → this Type. MSN-class portals host this Type's surface as a module; nesting is packaging, not identity.
6. **vs General Web Search Engine (§02.02, processed)** — per-query transient results vs a query-free standing shared flow; search may live beside the flow.
7. **vs social feed Types (§01.05)** — in social types the connection graph is the distribution substrate and the user is a member; here the user is an audience member of an editorially/algorithmically assembled publisher flow.
8. **vs Financial News & Research Platform (§08, processed) — flag answered.** Their flag asked whether this pass claims domain-vertical news products. Answer: a plain vertical news aggregator (Techmeme-class: same machinery, vertical corpus) is this Type; products with instrument anchoring + attached market data + investment-decision purpose + first-party editorial/analytical layer stay in that Type. No boundary change.
9. **Historical / market-sample check.** The analog ancestor satisfies the core: the wire-service digest and the edited front page assemble a shared flow of sourced stories from many correspondents/outlets for every reader alike — shared assembly, provenance, standing edition. The web-era ancestor (Drudge-class single-editor headline aggregation, Layer B from the content-aggregator pass) satisfies the core with one editor and no algorithm. The L0 deliberately does not require: algorithms, machine learning, clustering, apps, accounts, mobile surfaces, hosting of content, or any specific commercial model — so older, minimal, single-editor, and machinery-only forms all fit. Historical check passes.

## Uncertainties

- **Two deep products this pass.** Only Techmeme and AllTop were documented first-hand (Tier 1). Claims about the broader market rest on the four processed sibling passes (Layer B) and are worded accordingly. Google News carries one positioning sentence only; SmartNews/Flipboard carry no claims. If a later pass reaches them, re-verify: (a) whether clustering with visible source counts is standard; (b) whether per-user tuning layers are common; (c) hosting-vs-link-out distribution.
- **Whether clustering is universal** — documented explicitly in one product, implied in another, absent from the Drudge-class ancestor; held standard-not-definitional on this evidence.
- **Regional poles** (e.g., heavyweight East-Asian news aggregators) — unobserved; the minimal machinery should absorb them, but this is inference.
- **Cold-start behavior** — not applicable to a shared flow (no per-user state required); only relevant to the optional personal layer.

## Final Synthesis

A News Aggregator is the news-scoped member of the aggregator family: a consumption application whose defining core is three jointly-held structures — a sourced news corpus (journalistic stories about current events from multiple identifiable publishers, each story carrying its source), shared product-side assembly (the product's machinery — editors, ranking, clustering, crawling, in any combination — selects, merges, and orders a flow that is the same for every reader, with per-user selection at most an optional tuning layer), and the standing news flow (a continuously refilled consumption surface). Standard capabilities around the core: clustering of duplicate coverage into one story with many sources, an editorial layer making final calls, ranking/scoring machinery with stability safeguards, alternative renderings (river, topic sections), link-out provenance, optional personal feeds, newsletter delivery, and search. Variants: vertical scope, editorial posture spectrum, hosting model, per-user companion layer, attached context modules, commercial model, packaging. The machinery seam vs Personalized News Feed, the list seam vs Feed Reader, and the scope seam vs Content Aggregator are all ratified from this side; the News Application and financial-vertical flags are answered and forwarded. The wire-service digest, the single-editor web headline aggregator, and the machinery-only sister site all satisfy the core — the historical check passes without modern machinery.
