# Research Notes — Personalized News Feed

Research date: **2026-09-08**

## Research Goal

Understand the Personalized News Feed as an Application Type: what its world consists of, how a news product assembles a *different* flow for each user, how the personal flow coexists with shared editorial news surfaces, and where it separates from its processed siblings — Personalized Content Feed (§02.08), Content Aggregator (§02.08), Information Portal (§02.11) — and from its unprocessed §02.04 siblings (News Application, News Aggregator). Three prior passes left explicit joint-review flags that this pass must discharge from this side:

- **personalized-content-feed** (§02.08, processed 2026-09-08): "same per-user machinery, news-only scope — mirrors the ratified content-aggregator/news-aggregator scope seam; recommend joint review when that leaf is processed; there also re-test whether origin attribution should stay standard-not-definitional (held here on single-product evidence only)"
- **information-portal** (§02.11, processed 2026-09-07): the MSN-class portal homepage is feed-like and sits close to Personalized News Feed / Content Aggregator — seam held via the whole-session-gateway test; joint review recommended when this pass runs
- **content-aggregator** (§02.08, processed 2026-09-07): four-sibling family test — "collection+curator (curation) / stream+product-machinery (aggregator) / user-assembled subscription list (reader) / per-user inference (personalized feed)"

## Initial Boundary (hypothesis before research)

Working hypothesis: a Personalized News Feed is the news-scoped sibling of the ratified Personalized Content Feed — a standing personal flow of news items assembled per user by the product's selection machinery from that user's signals (declared follows, in-product behavior, location), drawn from a multi-publisher news corpus, coexisting in the same product with shared editorial surfaces (top stories, trending) that are *not* per-user.

Expected confusions:

- News Aggregator (§02.04, unprocessed) — shared product-assembled news flow; per-user tuning at most optional
- News Application (§02.04, unprocessed) — a single publisher's own product
- Personalized Content Feed (§02.08, processed) — same machinery, all-content scope
- Feed Reader (§02.08, processed) — faithful delivery of the user's subscription list
- Information Portal (§02.11, processed) — whole-session gateway vs article stream
- General Social Network (§01.05) — social-graph distribution vs audience-signal selection
- General Web Search Engine (§02.02) — per-query results vs standing flow

## Research Questions

1. What is the unit of the flow (story card), and what does it carry (headline, publisher, imagery, recency, topic)?
2. What signals drive per-user selection of news: declared follows (topics, publishers, teams), in-product behavior, location, explicit more/fewer feedback? Which are definitional?
3. How does the personal flow relate to the shared editorial layer (top stories, trending, spotlight) that news products also run? Is the mix definitional?
4. What role does the publisher play — is provenance visible, is the publisher a first-class object (followable/blockable), does the item link out or get hosted?
5. What controls does the user have over the flow (follow/unfollow, block, stop-suggesting, more/fewer, restrict-to-followed, clear history)?
6. How do local news, sports, and other vertical modules attach to the personal flow?
7. Boundaries: vs each sibling and adjacent Type; where do portal-embedded news modules and personal start pages sit?

## Representative Products

Selection intent: market representation + different product philosophies (algorithmic search-giant vs platform-native editorial mix vs lightweight download-first vs user-magazine hybrid vs portal descendant) + different customer tiers (consumer). Reality constraint: the research environment could reach only one vendor's documentation deeply this pass; the reachable sample differs from the ideal sample, and the type family is heavily ratified by four processed sibling passes, which compensates partly.

| Product | Pole | Evidence tier |
|---|---|---|
| Apple News | platform-native news feed; editor-curated top stories + per-user personalization ("Today" feed; channels/topics/teams follows; per-story more/fewer feedback; local; on-device signals posture) | **Tier 1 — fetched 2026-09-08** (User Guide: 5 pages + product marketing page) |
| Google News | search-giant algorithmic news feed ("For You"-class) | **Tier 2 only** — one official positioning sentence from the Google blog index; all feature documentation unreachable |
| SmartNews | lightweight algorithmic download-first news app | **unreachable** (smartnews.com, help.smartnews.com, about.smartnews.com timeouts) |
| Flipboard | user-magazine/personal-magazine hybrid with personalization | **unreachable** (about.flipboard.com timeout ×2; also unreachable in the content-aggregator pass) |
| Microsoft Start | portal-descendant personalized feed | **unreachable** (microsoftstart.msn.com JS shell; store page 410; support.microsoft.com 404) |
| Family evidence from processed sibling passes (Techmeme, AllTop, WordPress Reader, NetNewsWire/Feedbin, MSN portal) | reader/aggregator/portal poles of the seams | Tier 1 as recorded there (Layer B here) |

## Sources

Fetched successfully (2026-09-08):

- Apple — Apple News User Guide (macOS), Welcome: https://support.apple.com/guide/news/welcome (product structure: channels/topics, Today feed, saved stories, reading history)
- Apple — "Follow and unfollow channels and topics": https://support.apple.com/guide/news/follow-and-unfollow-channels-and-topics-iph776e48d55/mac (follow mechanics, sidebar, Favorites, restrict-to-followed option pointer)
- Apple — "See more or fewer stories like the current one": https://support.apple.com/guide/news/stories-current-iph1ddb4a8aa/mac (per-story feedback controls)
- Apple — "Explore channels, topics, and stories": https://support.apple.com/guide/news/explore-channels-topics-and-stories-iph523395af1/mac (Today composition, Suggested, Stop Suggesting, Go to Channel, local news, Shared with You)
- Apple — "Change settings": https://support.apple.com/guide/news/change-settings-iphca74e7adb/mac ("Restrict stories in Today", explicit-content restriction, My Sports sync, Siri suggestion opt-outs)
- Apple — Apple News product page: https://www.apple.com/apple-news/ (positioning; editor+algorithm composition; on-device intelligence claim; News+ tiers)
- Google — Google News product blog index: https://blog.google/products/news/ (one official positioning sentence)

Sibling-pass carry-over (recorded there at Tier 1; used here as Layer B):

- research/personalized-content-feed.md — ratified per-user feed core and family seams; WordPress Reader recommendation-feed observations (tags-followed selection, likes/comments signals, cold-start defaults, language exclusion)
- research/content-aggregator.md — Techmeme/AllTop/Drudge observations; attribution load-bearing for aggregation; family test wording
- research/feed-reader.md — NetNewsWire/Feedbin anti-algorithm positioning
- research/information-portal.md — whole-session-gateway test; MSN observations; personal-start-page variant note
- research/content-curation-platform.md — curator/collection artifact seam

Unreachable this pass (abandoned per the 1–2 failure rule):

- support.google.com/news (×2 timeout), news.google.com/about (×1), play.google.com (×2) — no claims about Google News features beyond the positioning sentence
- en.wikipedia.org (×2), web.archive.org (×1) — no historical product claims
- smartnews.com (×1), help.smartnews.com (×1), about.smartnews.com (×1) — no claims about SmartNews
- about.flipboard.com (×2) — no claims about Flipboard
- microsoftstart.msn.com (JS shell, ×1), apps.microsoft.com (410), support.microsoft.com (404) — no claims about Microsoft Start
- groundnews.com (×1 timeout), App Store listings (geo-redirect to CN storefront) — no claims

**Source-access limitation (material):** only Apple News could be documented first-hand at depth. All market-level claims below rest on (a) Apple's Tier-1 documentation (direct), (b) the ratified machinery of the personalized-content-feed sibling pass (Layer B), (c) the news-side family evidence in the aggregator pass (Layer B), and (d) canonical inference. No feature, signal, or default claims are made about Google News, SmartNews, Flipboard, or Microsoft Start beyond Google's single positioning sentence; the historical check is conceptual only.

## Product Observations

### Apple News (evidence layer A — fetched 2026-09-08)

**Product structure.** "Apple News collects and organizes stories from a wide range of publications (called *channels*) and topics." The sidebar carries: **Today** (the personal+editorial feed), News+ (premium magazine/newspaper catalog), Sports (My Sports), Puzzles (News+), Shared with You (stories shared via Messages), Favorites, **Following** (channels and topics followed, plus "Apple News Spotlight" — editor-selected event coverage), **Suggested** (channels/topics suggested by Siri or by the user's own actions in the app), reading history, saved stories.

**The feed's composition is explicitly editor-plus-personal.** "Today … presents top stories selected by Apple News editors and stories from the channels and topics you follow." In some regions the Today feed includes local news — "curated and personalized local stories and weather reports based on your location." Marketing copy confirms the same split at product level: "Top stories chosen by editors, personalized for you" (listed as included in the free tier); "Experienced Apple News editors curate the day's top stories from trusted sources, and advanced algorithms help you discover stories you'll find interesting."

**Per-user selection machinery and signals.** Following channels/topics puts them in the sidebar and — the documented causal claim — "their stories appear more often in the Today and other feeds. … When you follow channels and topics, Apple News better understands your interests and can recommend stories that more closely match them." Behavioral signals exist: "As you read, Apple News gets a better understanding of your interests and suggests relevant stories" (product page). The Suggested sidebar section is populated "by Siri or … by your actions in Apple News. For example, whether you follow or block channels and topics, or ask for more or fewer suggestions similar to a story you're reading." Location is a signal for the local-news slice. Privacy posture: "Apple News only uses on-device intelligence to recommend stories and doesn't access your information without your permission" (product page) — a signal-processing implementation choice, not a family requirement.

**Per-story feedback controls.** "See more or fewer stories like the current one": the user can ask News to suggest more or fewer stories like the one being read; afterwards the more/less marker "appears next to the story in your reading history and in the Today or other feeds" — the feedback is itself recorded in user-visible surfaces.

**Negative controls.** Block and unblock channels and topics; "Stop Suggesting" — a channel or topic surfaced in the feed can be stopped from being suggested ("If you change your mind … search for it, then follow it").

**The restrict-to-followed mode (the reader pole inside the product).** A settings option — "Restrict stories in Today: Show only stories from channels you follow in the Today feed. This option limits the variety of stories that appear in the Today feed; Top Stories and Trending Stories aren't shown." This is direct in-product evidence of the seam vs the Feed Reader: narrowing the personal flow to the followed list is an *option*, and when exercised it also removes the shared editorial surfaces. Default mode keeps editorial items in the flow.

**Provenance and the publisher as first-class object.** Stories come from "publications (called channels)"; the user follows channels, blocks channels, subscribes to individual channels, and can "Go to Channel" from a story. The publisher is therefore a selectable, blockable, subscribable object in the model — not just a byline. (Whether the story is hosted in-app or links out is not stated in the fetched pages; the marketing page emphasizes in-app reading; the link-out/hosting split is treated below as a variant with family evidence.)

**Story-level actions and retention.** Save stories (a Saved Stories surface); share stories / read stories shared with you (Shared with You via Messages); report a concern about a story; view or clear reading history; manage notifications; sync across devices; search for channels, topics, or stories.

**Vertical modules.** My Sports — follow "sports, leagues, teams, athletes" with scores/schedules/standings/highlights; synced across Apple apps. Local news — regional availability. News+ — subscription tier adding magazines/newspapers/puzzles/audio (commercial layer). Newsletters (email briefings from editors).

### Google News (evidence layer A, thin — one positioning sentence)

The official Google blog index describes Google News as "organizing what's happening in the world to help you learn about the stories that matter." Nothing else about Google News was verifiable this pass; no feature claims are made. Its market role (algorithmic personalized "For You"-style feed beside shared headlines) is treated as structural context only.

### Family seam evidence from processed sibling passes (evidence layer B)

- **personalized-content-feed pass** (Tier 1 there): ratified the per-user feed core — standing corpus + per-user selection from that user's signals + standing personal flow; "the user's list may be one input, but selection is the product's"; the feed is never complete; consuming is configuring. WordPress Reader documented: "a feed of recommendations based on what you've recently liked or commented on"; cold-start default tags; per-user language exclusion; editorial layer beside the algorithm kept as a separate surface.
- **content-aggregator pass** (Tier 1 there): the aggregator's flow is shared — "the same for everyone"; per-user feeds at most an optional tuning layer (AllTop MyAllTop); **attribution load-bearing** for aggregation ("unattributed rehosting is not aggregation"); Techmeme — algorithmic machinery on a shared surface, no per-user surface.
- **feed-reader pass** (Tier 1 there): the reader's subscription list is the sole selector with faithful, complete, recency-ordered delivery; reader vendors define themselves against the algorithmic pole (NetNewsWire: "relying on big tech social media and their algorithms" as the rejected alternative).
- **information-portal pass** (Tier 1 there): the portal's artifact is the whole entry surface (content + services + routing); "keep only the personalized article stream → News Aggregator / Personalized Content Feed."

## Cross-product Comparison

| Dimension | Apple News (A) | Personalized Content Feed core (B, ratified) | News Aggregator family (B: Techmeme/AllTop/Drudge) | Feed Reader (B) |
|---|---|---|---|---|
| Corpus | stories from many publications (channels) and topics | content items from any kind of source (hosted/collected/member-published) | news items crawled from many publishers | items from the user's own subscriptions |
| Who selects between items | the product, per user (follows + behavior + location + more/less feedback) | the product, per user (behavior + declared interests) | the product, same for everyone | the user's list (faithful delivery) |
| Per-user variation | yes (Today differs per user; follows/behavior differ) | yes, by definition | no (shared surface; MyAllTop tuning optional) | personal list, no inference |
| Editorial layer | explicit: editor-selected top stories inside the same feed; separate Spotlight; excluded under restrict-to-followed | separate surface where present (Freshly Pressed-class) | the shared flow *is* editorial/machine-assembled | none |
| Provenance | structural: publisher = channel, followable/blockable/subscribable; Go to Channel | standard structure (origin display universal, not invariant) | load-bearing (attribution is the aggregator's essence) | primary (subscriptions *are* origins) |
| Completeness | not promised (selection); restrict-to-followed mode narrows toward the list regime | never promised | not promised | promised per subscription |
| Ordering | ranked/mixed editorial+personal (no ordering algorithm documented as invariant) | selection is the invariant; ordering is not | ranked (shared) | chronological |
| Feedback controls | follow/unfollow, block, Stop Suggesting, Suggest More/Less per story, clear history | react/save/hide/follow class | follow/save tuning (AllTop) | subscribe/unsubscribe |
| Signals | declared (channels/topics/teams) + behavior + location + explicit feedback | behavior + declared | none per user | none |
| Scope | news/journalism only | any content kind | news | any feed content |

Stable across the sample: the news-scoped Type is the generic personalized feed machinery with (a) the corpus restricted to journalism from identifiable publishers, and (b) the publisher elevated to a first-class model object (follow/block/subscribe) with visible provenance. The editor-plus-personal feed composition is directly documented in one product and is best held as standard news-product structure, not invariant.

## Abstraction Levels

### L0 — Defining Invariant (deliberately small)

A Personalized News Feed is recognizable by exactly this structure:

```text
Sourced news corpus: journalistic content about current events drawn from
  multiple identifiable publishers (the product feeds the news; it does
  not have to be the publisher) — each item carrying its source
  └── Per-user selection: the product's selection machinery weighs corpus
        items by signals about the individual user — interests declared
        (followed topics/publishers), behavior generated in the product,
        location where supported, explicit more/fewer feedback —
        selecting BETWEEN items across a corpus the user never enumerated
        (the user's follows may be one input; selection is the product's)
        └── The personal news flow: a standing consumption surface,
              re-assembled as the user's signals accumulate
```

Three legs, jointly held:

- Remove the sourced news corpus (or the multi-publisher, provenance-carrying nature) → nothing news-like to select from; a single publisher's personal surface is a publisher app, an unattributed rehost is not a news feed at all.
- Remove per-user selection → the flow becomes the same for everyone (News Aggregator), or delivery of the user's own list (Feed Reader), or the whole-session gateway (Information Portal). The "personalized" is gone.
- Remove the standing, signal-updating flow → a one-shot personal newspaper edition or per-query results; the "feed" is gone.

Notes on the L0 boundary:

- **Scope is the seam, not a fourth leg.** The selection machinery is identical in kind to the ratified generic sibling (personalized-content-feed); what makes this a distinct directory Type is the corpus scope — news/journalism from publishers — exactly mirroring the ratified content-aggregator/news-aggregator scope seam. A personalized feed whose corpus is news-shaped belongs here regardless of packaging.
- **Provenance is inside the corpus leg for news.** The sibling pass held origin attribution standard-not-definitional on single-product evidence and asked this pass to re-test. Re-test result: **in news scope, attribution is load-bearing.** (a) Apple News Tier-1 makes the publisher a first-class object (follow/block/subscribe/Go to Channel), not a byline; (b) the aggregator family ratified attribution as load-bearing on the shared-machinery side (Layer B); (c) journalism itself is provenance-carrying content — a "news" item whose source is invisible stops being recognizable as news consumption. The generic sibling keeps its own call for all-content scope; the news-scoped Type carries provenance in its recognizable core.
- **Per-user selection from signals is the invariant — not the technique.** A learned model, simple popularity-by-followed-topic rules, or a personal clipping service cutting a digest to a stated interest profile all satisfy. Location and team follows are signal *kinds*, not requirements.
- **Ordering is not definitional.** Ranked, editorial-then-personal, or per-user-filtered recency all satisfy; the invariant is that *selection between items* happens per user.
- **The shared editorial layer (top stories/trending) is NOT definitional.** Directly documented coexisting with the personal flow (Apple: Today = editor-selected top stories + followed stories), but a fully-personalized pole is coherent; the mix is standard news-product structure.

### L1 — Common Mature Structure (standard capabilities)

- **Editorial layer beside the personal flow** — editor-selected top stories, trending, spotlight/event coverage in the same product; documented to be excluded when the feed is restricted to followed channels (Apple, direct).
- **Declared-interest inputs** — follow topics, publishers (channels), teams/leagues/athletes (Apple, direct); the declarations join behavior signals and visibly raise item frequency ("their stories appear more often in the Today and other feeds").
- **Per-story feedback controls** — "show more/fewer stories like this" recorded in user-visible surfaces (Apple, direct); the react/hide/not-interested class from the family (Layer B).
- **Negative controls** — block channels/topics; stop-suggesting a surfaced suggestion (Apple, direct).
- **Suggestion/cold-start machinery** — a Suggested layer seeded by platform signals or the user's actions (Apple, direct); onboarding interest picks and default content from the family (Layer B).
- **Local news and location relevance** — curated and personalized local stories with location-based selection, region-gated (Apple, direct).
- **Story-level actions and retention handoff** — save, share / shared-with-you, report a concern, view/clear reading history, notifications (Apple, direct); save-outward from the family (Layer B).
- **Search** — search for channels, topics, or stories beside the flow (Apple, direct).
- **Multi-surface delivery** — phone/tablet/desktop and companion surfaces (Apple: Mac/iPhone/CarPlay/Watch; direct), sync across devices.
- **Origin attribution on every item** — carried in the L0 corpus leg for news (see above); implementation varies (byline + logo on hosted items, source label + link-out).

### L2 — Variant / Optional Structure

- **Hosting model** — items hosted in-app (licensed/reformatted) vs link-out to the publisher site vs hybrid; family evidence covers both; hosting is not the invariant, provenance is.
- **Signal-processing posture** — on-device personalization (Apple's documented privacy posture) vs server/cloud personalization; where signals live is implementation, not invariant.
- **Commercial packaging** — free feed + premium subscription tier (magazines/newspapers/puzzles/audio), individual channel subscriptions, advertising against the flow (Apple direct for tier/puzzles; ads structural in the family).
- **Vertical modules** — sports with scores/standings (Apple direct), weather, podcasts/audio briefings, newsletters, cross-app profile reuse (My Sports syncs to other apps — Apple direct).
- **Packaging** — standalone news feed app vs feed surface embedded in a portal/start page vs platform-native preinstalled app; portal embedding shades toward Information Portal unless the article stream is the primary artifact.
- **Regional editions/availability** — feature and content availability varies by country/region (Apple explicit; regional editions are the family norm).
- **Regulatory/eligibility overlays** — explicit-content restriction (Apple direct), safety/spam exclusions, language scoping (family Layer B).

### L3 — Vendor-specific Detail (research notes only)

- Apple News: channels terminology; Today/News+/Sports/Puzzles/Shared with You/Favorites/Following/Suggested sidebar composition; "Apple News Spotlight" as editor showcase inside Following; Favorites count limited; Suggest More = Command-L, Suggest Less = Command-D; feedback markers stored in reading history and feeds; "Restrict stories in Today" option and its documented side effect (Top Stories and Trending Stories not shown); "Stop Suggesting" with search-to-refollow; on-device intelligence privacy claim; Siri suggestion learning with opt-outs ("Show Siri Suggestions in application", "Learn from this application"); My Sports sync across Apple apps via Apple Account; explicit-content restriction; local news regional gating; News+ magazines/newspapers/puzzles/audio stories/Apple News Today podcast; Family Sharing; "Go to Channel".
- Sibling-recorded details relied on for seams: WordPress default tags and factor list; AllTop MyAllTop; NetNewsWire/Feedbin anti-algorithm copy; Techmeme editor pyramid; MSN portal composition.

## Rejected Findings (considered, not promoted)

- **"The Type = Google News/SmartNews-class algorithmic products"** — rejected: the sampled deep product is editor-plus-algorithm; the machinery (per-user selection from signals) does not require any particular algorithm. Current market leadership is not the definition.
- **"The editorial layer is definitional"** — rejected: it is documented as co-present in one deep sample and as *removable by the user* (restrict-to-followed mode strips it); a fully-personalized pole satisfies the core.
- **"Location/local news is definitional"** — rejected: region-gated standard capability (Apple explicit "not available in all countries or regions" pattern).
- **"Ranking/AI is definitional"** — rejected (family precedent): selection from signals is the invariant; the analog personal clipping service satisfies it.
- **"The feed must link out to publishers"** — rejected: hosting model is a variant; what survives across implementations is visible provenance.
- **"Sports/weather/puzzles/other verticals are part of the Type"** — rejected: optional modules; product-specific in their packaged form.
- **"Accounts are definitional"** — rejected: persistent per-user signals are the requirement; account binding is the common implementation (consistent with the sibling pass).
- **"The personal flow replaces the news front page"** — rejected: products legitimately run both a shared editorial surface and per-user flows in one product; the Type claim is about the per-user flow being a first-class surface.

## Boundary Findings

1. **vs Personalized Content Feed (§02.08, processed) — joint-review flag DISCHARGED from this side; keep both RATIFIED.** The selection machinery is identical in kind (per-user selection from that user's signals; never complete; consuming is configuring). The seam is **corpus scope**: this Type's corpus is news/journalism from identifiable publishers, and its L0 carries provenance in the corpus leg (see re-test below); the generic sibling spans content kinds with origin display as standard structure only. Removal test: widen the corpus beyond news with no other change → generic sibling; restrict a generic feed's corpus to publisher journalism → this Type. This mirrors the ratified content-aggregator/news-aggregator scope seam; no taxonomy change recommended.
2. **Attribution re-test (from the personalized-content-feed pass) — DISCHARGED with an upgrade for news scope.** Their pass held origin attribution standard-not-definitional "on single-product evidence only" and asked the news-scoped passes to re-test. Result: for the news-scoped Type, "each item carries its publisher" is part of the recognizable core (Apple Tier-1: publisher as followable/blockable/subscribable channel object; aggregator family Layer B: attribution load-bearing; journalism as provenance-carrying content). The generic sibling's own call stands for its Type.
3. **vs News Aggregator (§02.04, unprocessed) — machinery seam, consistent with the family test.** The aggregator's news flow is assembled by product machinery *shared* by everyone (editors/scoring/clustering); per-user feeds at most an optional tuning layer. Here, per-user assembly *is* the core: without the user's signals the primary surface cannot render and must fall back to defaults. The market commonly runs both regimes in one product (Apple's Today feed literally mixes editor-selected top stories with followed/behavioral stories; a "Top Stories" surface beside "For You" is the family shape) — so the news-aggregator pass should expect to find this Type hosted beside its own surface in the same product. Removal test: remove per-user selection → News Aggregator. **Flag for joint review when that leaf is processed.**
4. **vs News Application (§02.04, unprocessed)** — a single publisher's own product (its editors, its editions, its reporting). Here the corpus is multi-publisher and the product's job is feeding/selection, not authoring. Removal test: make the product the publisher of everything it shows → News Application.
5. **vs Feed Reader (§02.08, processed)** — the list-vs-selection seam, restated for news: the reader faithfully delivers everything from the user's chosen sources; here follows are *inputs* to selection across a corpus the user never enumerated. Direct in-product evidence of the seam: Apple's "Restrict stories in Today" option narrows the personal flow to followed channels only — and the documented side effect is that the editorial surfaces (Top Stories, Trending) disappear, i.e., the feed drifts toward reader behavior as an *option* while the default mode remains selection. Removal test: selection between items disappears → Feed Reader.
6. **vs Information Portal (§02.11, processed) — joint-review flag DISCHARGED from this side; seam held.** The portal's artifact is the whole entry surface (content + services + routing; no transaction of record; ephemeral pointers). Keep only the personalized article stream → this Type. MSN-class products host this Type's surface inside the portal; that nesting is packaging, not identity.
7. **vs social feed Types (§01.05)** — in social types the connection graph is the distribution substrate and the user is a member; here the user is an audience member whose signals select from a publisher corpus; social ties may exist as inputs (following people) but are not required.
8. **vs General Web Search Engine (§02.02, processed)** — per-query transient results vs query-free standing personal flow; search may live beside the flow (Apple: search for channels/topics/stories) as a separate surface.
9. **vs Content Curation Platform (§02.08, processed)** — no curator and no collection artifact here; the artifact is the standing per-user flow.
10. **vs Bookmark Manager / Read-it-later (§02.13/§02.09)** — save actions are the retention handoff out of the flow; consumption surface vs retention store.
11. **Historical / market-sample check (conceptual — no product claims possible this pass).** The analog ancestor satisfies the core: a personal newspaper/clipping service cuts each subscriber a personal digest of current news according to the subscriber's stated interest profile, refreshed on a schedule (sourced multi-publisher corpus + per-user selection from declared signals + standing personal flow). Early web-era "my news" personal start-page modes sit at the information-portal boundary (user-configured modules ≠ per-user item selection; the seam is arrangement vs selection). The L0 deliberately does not require: machine learning, ranking algorithms, apps, accounts, mobile surfaces, hosting of content, or any specific commercial model — so older, regional, minimal, and analog forms fit. No specific historical product is claimed because encyclopedic sources were unreachable (Wikipedia ×2, Wayback ×1).

## Uncertainties

- **Single deep product.** Only Apple News was documented first-hand (Tier 1, five guide pages + product page). Claims about the broader market rest on the four processed sibling passes (Layer B) and are worded accordingly. Google News carries one positioning sentence only; SmartNews/Flipboard/Microsoft Start carry no claims. If a later pass reaches them, re-verify: (a) whether publisher-as-first-class-object (follow/block at publisher granularity) is standard; (b) whether the editor-plus-personal feed composition is standard; (c) whether restrict-to-followed modes exist elsewhere; (d) hosting-vs-link-out distribution.
- **Historical check is conceptual only** (no reachable encyclopedic sources) — kept weak per evidence rules.
- **Hosting model distribution** (in-app licensed vs link-out) — both documented in the family, distribution unknown; written as variant.
- **Regional poles** (e.g., heavyweight East-Asian news-feed superapps) — unobserved; the L0's minimal machinery should absorb them, but this is inference, not observation.
- **Cold-start defaults for news specifically** — family evidence exists (default tags, onboarding picks); Apple's Suggested layer is direct but its cold-start behavior beyond that was not documented. Held as standard capability with direct family support.
- **Whether "top stories"-style shared surfaces are always present in products of this Type** — directly documented in one product; held as standard structure, explicitly not definitional.

## Final Synthesis

A Personalized News Feed is the news-scoped member of the personalized-feed family: a consumption application whose defining core is three jointly-held structures — a sourced news corpus (journalistic content about current events drawn from multiple identifiable publishers, each item carrying its source), per-user selection (the product's machinery weighs corpus items by signals about the individual user — declared follows, in-product behavior, location, explicit more/fewer feedback — selecting between items across a corpus the user never enumerated), and the personal news flow (a standing consumption surface re-assembled as signals accumulate). The machinery is identical in kind to the ratified generic sibling; corpus scope and provenance-in-the-core are what make the Type distinct, mirroring the ratified aggregator scope seam. Standard capabilities around the core: an editorial layer beside the personal flow (top stories/trending, documented as removable via restrict-to-followed), declared-interest inputs with visible causal effect, per-story feedback controls, negative controls (block/stop-suggesting), suggestion and cold-start machinery, local news, retention handoffs, search, and multi-surface delivery. Variants: hosting model, signal-processing posture, commercial packaging, vertical modules, portal/platform embedding, regional editions. The analog personal clipping service and the personal-newspaper ancestor satisfy the core without any modern machinery — the historical check had to be run conceptually because encyclopedic sources were unreachable. Three sibling flags are discharged from this side: keep-both vs personalized-content-feed ratified on the scope seam; the attribution re-test answered with an upgrade for news scope; the information-portal article-stream seam confirmed.
