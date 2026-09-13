# Research Notes — Personalized Content Feed

Research date: **2026-09-08**

## Research Goal

Understand what a Personalized Content Feed is as an Application Type: what its world consists of, what drives the selection of items for each individual user, how the consume→signal→re-assemble loop works, and where it separates from its three processed §02.08 siblings (Feed Reader, Content Aggregator, Content Curation Platform), from the news-scoped sibling (Personalized News Feed, §02.04, unprocessed), from search, from social-network feeds, and from the B2B recommendation/personalization Types of §06. Three sibling passes left explicit joint-review flags that this pass must discharge from this side:

- content-curation-platform: "personalized feed = algorithmic per-user stream with no curator and no collection artifact; flag for joint review"
- content-aggregator: "the sibling's defining machinery is per-user personalization; the aggregator's default surface is shared, with personal feeds as an optional tuning layer; flag for joint review" (+ unresolved Flipboard/Feedly consumer-pole straddle)
- feed-reader: "same seam on the inference side: per-user interest inference selects the flow; no explicit user-managed source list is required; flag remains open for that leaf's pass"

## Initial Boundary (hypothesis before research)

Working hypothesis: a Personalized Content Feed is a content-consumption surface where the flow each user sees is assembled **per user** by the product's interest model over that user's own signals — not from a user-managed subscription list (Feed Reader), not a shared product-assembled flow (Content Aggregator), not a curator-selected collection (Content Curation Platform).

Expected confusions:

- Feed Reader (§02.08, processed) — "personalized" colocations of subscriptions; readers increasingly add recommendation layers
- Content Aggregator (§02.08, processed) — algorithmic ranking on a *shared* surface
- Content Curation Platform (§02.08, processed) — human-selected collections
- News Aggregator / Personalized News Feed (§02.04, unprocessed) — same machinery, news scope
- General Web Search Engine (§02.02, processed) — per-query retrieval vs standing per-user flow
- Recommendation / Personalization Engine (§06, processed) — B2B engine vs consumer surface (their pass names this leaf as downstream surface)
- Marketing Personalization Platform (§06, processed) — same surface/engine split
- General Social Network / Microblogging / Short-form Video (§01.05) — social feeds; graph vs interest signals as the selection substrate
- Information Portal (§02.11, processed) — their pass: "keep only the personalized article stream → News Aggregator / Personalized Content Feed"
- Bookmark Manager / Read-it-later (§02.13/§02.09) — retention vs consumption

## Research Questions

1. What exactly is the selector? What distinguishes per-user selection from shared ranking (aggregator) and from user-list delivery (reader)?
2. What signals feed the model: implicit behavior (views, likes, comments, dwell), declared interests (followed topics/tags/sources), profile attributes? Which are definitional?
3. What is the candidate universe (corpus) and where does its content come from?
4. What is the interaction loop: consume → signals accumulate → flow re-assembles? Which feedback controls exist (like/hide/not-interested/follow)?
5. What happens at cold start (no signals yet)?
6. What rules gate what can appear (eligibility, language, safety)? Is completeness ever promised?
7. How does the user learn/steer the model (explanations, interest management)?
8. Boundaries: vs each sibling and adjacent Type; how the market packages the Type (standalone vs surface inside larger products).

## Representative Products

Selection intent: market representation + different packaging poles + different content kinds + different signal models. Reality constraint: the research environment could not reach any of the major consumer platforms this pass (see Sources). The reachable sample differs from the ideal sample; the four-sibling family structure is heavily ratified by three processed sibling passes, which compensates partly.

| Product | Pole | Evidence tier |
|---|---|---|
| WordPress.com Reader (subscription feed + Discover/Recommended/Post Recommendations) | reader product hosting a documented per-user recommendation feed beside its subscription feed; full signal machinery publicly documented | **Tier 1 — fetched 2026-09-08** (two official support guides) |
| Short-form video apps (TikTok-class "For You" feeds) | feed-first consumer app; interest inference without required follows | **unreachable** (support + newsroom timeout ×2 each; described structurally only) |
| Video-platform home/recommended feeds (YouTube-class) | personalized discovery surface inside a hosting platform | **unreachable** (timeout ×2 + 404; structural only) |
| Search-engine discovery surfaces (Google Discover-class) | query-free standing content feed beside a query engine | **unreachable** (timeout ×2 each on developer docs and user help; structural only) |
| Family evidence from processed sibling passes (NetNewsWire, Feedbin, AllTop, Techmeme, elink, Komoot, job boards) | reader/aggregator/social poles of the seams | Tier 1 as recorded in sibling passes (Layer B here) |
| StumbleUpon-class collaborative-filtering discovery products (2000s–2010s) | historical pole of the Type | **unreachable** (Wikipedia timeout ×3 across two hosts; conceptual only — no product claims) |

## Sources

Fetched successfully (2026-09-08):

- WordPress.com — "Use the WordPress.com Reader" https://wordpress.com/support/reader/ (subscription feed semantics, Reader surfaces, blocks, card formats)
- WordPress.com — "Learn about Reader recommendations" https://wordpress.com/support/reader/reader-recommendations/ (recommendation surfaces, algorithm factor list, cold-start defaults, exclusions, identity-bound signals, editorial layer)

Sibling-pass carry-over (recorded there at Tier 1; used here as Layer B):

- research/feed-reader.md — NetNewsWire homepage positioning ("relying on big tech social media and their algorithms" as the rejected alternative); Feedbin copy ("There's no algorithm… just the videos from your favorite creators in chronological order")
- research/content-aggregator.md — Techmeme (crawler + auto re-sorting machinery on a *shared* front page; no per-user surface), AllTop (MyAllTop follow/save layer), elink market evidence
- research/content-curation-platform.md — curator/collection artifact; elink separate solution pages
- research/hiking-trail-application.md — Komoot Home feed documented as "personalized feed … based on location, sports used, past activity, follows" (per-user inference in an adjacent Type)
- research/job-board.md — "job recommendations based on profile and preferences with a 'Why am I seeing this job?' explainer"
- research/recommendation-personalization-engine.md — this leaf named as consumer-facing surface; engine/surface test
- research/general-social-network.md / research/microblogging-platform.md / research/interest-based-social-network.md — social-feed seam notes
- research/information-portal.md — "keep only the personalized article stream → News Aggregator / Personalized Content Feed"

Unreachable this pass (abandoned per the 1–2 failure rule):

- support.tiktok.com (×2), newsroom.tiktok.com (×1) — no claims about TikTok
- developers.google.com/search/docs/appearance/google-discover (×1), support.google.com/websearch (×1) — no claims about Google Discover
- blog.youtube (404), www.youtube.com/howyoutubeworks (×1) — no claims about YouTube
- help.medium.com (×1) — no claims about Medium
- en.wikipedia.org (×2), simple.wikipedia.org (×1) — no historical product claims
- ground.news (×2) — no claims

**Source-access limitation (material):** the market's most prominent implementations of this Type (short-video feed-first apps, video-platform home feeds, search-engine discovery surfaces) could not be documented first-hand. All observations below rest on (a) the WordPress.com documentation (direct), (b) sibling-pass Tier-1 evidence about the *neighboring* poles of each seam, and (c) canonical inference. Assertion strength is calibrated accordingly: no precise operational claims (no numeric limits, no algorithm specifics, no default windows) are made for any unreachable product, and the historical check is conceptual only.

## Product Observations

### WordPress.com Reader + Recommendations (evidence layer A — fetched 2026-09-08)

This is one product hosting **both** the Feed Reader surface and a documented Personalized-Content-Feed surface, which makes it unusually strong boundary evidence.

The reader pole (Reader guide):

- "Your customized Reader feed displays posts from **all the sites you follow**. Posts appear in the **order they were published**, with the most recent posts at the top." — faithful delivery + chronological order + completeness from the subscription list.
- Surfaces: Recent (followed sites' newest posts), Shelves (user-named groupings of followed sites and tags), Lists, Tags (follow topics), Likes, Conversations; subscribe/manage subscriptions; block site from Reader; card formats (standard/text/photo/gallery/video); "The Reader is a feed aggregator, and you can use it to follow all of your desired blogs in one place."

The recommendation pole (Reader recommendations guide — self-described as "recommends posts and websites based on **editorial curation and algorithmic selection**"):

- **Discover opens on the Recommended tab**: "Popular posts **based on the tags you follow**. If you don't follow any tags, this defaults to the `dailyprompt` and `WordPress` tags." → declared interests as input; **cold-start default** when no signals exist.
- **Reader Post Recommendations**: "A feed of recommendations **based on what you've recently liked or commented on**, displayed in the Search tab of Discover." → a per-user flow driven by behavioral signals. This is the pass's cleanest direct observation of the Type's machinery.
- **Other recommendation surfaces**: "More on WordPress.com" related posts — "most popular content … **similar to the current post**" (item-conditioned recommendation); related-posts on one's own site (title/content/engagement selection).
- **Signal/factor list** (documented publicly): post features (title, content, tags, categories, links/images/videos, recency of publication); site features (total likes/comments, who liked/commented, subscriber count, who subscribed, posting regularity, "how often a site has been rejected from Reader recommendations"); **user features** ("The content of what you've liked and commented on").
- **Identity-bound signals**: "Your post likes and comments on other WordPress blogs influence recommendations. Take a look at your recent like activity to understand **what similar content you might see**." And: "To prevent your comments from being included in recommendations, **log out** before commenting." → signals attach to the account; the user can reason about and manage what the model sees.
- **Eligibility exclusions**: spam sites, mature content, objectionable content, "**Content not in your language**" → per-user language scoping of the candidate pool.
- **Editorial layer beside the algorithm**: Freshly Pressed — "A curated selection of **our team's favorite content**" (hand-selected), a separate tab from Recommended. The market keeps human curation and algorithmic selection apart even inside one product.
- **Query surface beside the personal flow**: Discover also has a Search tab ("posts matching a topic or keyword you enter; sort by Relevance or Date") and a Latest tab ("The latest posts related to tags you follow" — a *personalized-but-chronological* surface: per-user filter, recency order).

### Family seam evidence from processed sibling passes (evidence layer B)

- **NetNewsWire** (feed-reader pass, Tier 1 there): "Instead of going from site to site in your browser looking for new articles — **or relying on big tech social media and their algorithms** — let NetNewsWire bring you the news you actually want." The reader pole *defines itself against* the algorithmic personalized-feed pole — market confirmation that the two are distinct categories.
- **Feedbin** (feed-reader pass, Tier 1 there): YouTube intake framed as "There's **no algorithm** or confusion about what you have already watched, just the videos from your favorite creators in chronological order." Same contrast, second vendor.
- **Techmeme** (content-aggregator pass, Tier 1 there): crawler + filtering tools "which automatically re-sort our front page," editors making final calls — algorithmic machinery on a **shared** surface; no per-user personalization on the surface. Evidences that algorithmic ranking alone does not make a personalized feed.
- **AllTop** (content-aggregator pass, Tier 1 there): default view is the shared ranked scan; "MyAllTop … follow topics and sources, save stories" — the personal layer as **optional tuning on a shared assembled flow**, the aggregator-side pole of the seam.
- **elink** (content-curation pass, Tier 1 there): sells Bookmark Manager / RSS Feed Reader / Content Curation as separate solution pages — the market keeps the family's categories apart.
- **Komoot** (hiking pass, Tier 1 there): Home = "personalized feed (routes/collections from people you follow, popular routes, community Highlights in your region …) based on **location, sports used, past activity, follows**" — per-user inference pattern recurring in an adjacent Type.
- **Job boards** (job-board pass, Tier 1 there): "job recommendations based on profile and preferences with a **'Why am I seeing this job?' explainer**" — explanation surfaces exist in the market.

### Market-shape observation (structural — consumer platforms unreachable)

The Type is realized in the market in two packagings: (a) **feed-first consumer applications** where the personal feed is the product's primary surface (short-video apps are the commonly cited extreme; unreachable this pass), and (b) **named personalized-feed surfaces inside larger products** — video platforms' home/recommended feeds, search engines' query-free discovery surfaces, social products' discovery tabs, readers' recommendation feeds (WordPress documented here). The packaging is a variant, not the invariant. No precise claims are made about any unreachable product.

## Cross-product Comparison

| Dimension | WordPress Reader (A) | NetNewsWire/Feedbin (B, reader pole) | Techmeme/AllTop (B, aggregator pole) | Social feeds (structural) | Feed-first apps (structural, unreachable) |
|---|---|---|---|---|---|
| What the user gets | subscription feed (chronological, complete) **plus** recommendation feed (selected from corpus by tags + likes) | faithful delivery of subscribed sources | one shared ranked flow | flow distributed over member posts via graph + ranking | personal flow over platform corpus |
| Who/what selects | product machinery for Recommended (tags followed + likes/comments); user's list for Recent | the user's subscription list, solely | product machinery, same for everyone | social graph (who you follow) + product ranking | product's interest model per user |
| Per-user variation | yes (signals differ per account; cold-start defaults to generic tags) | personal list, no inference | no (shared surface; optional MyAllTop tuning on AllTop) | yes (graph differs per member) | yes (by design) |
| Completeness promised | Recent: yes ("all the sites you follow"); Recommended: no | yes (per subscription) | no | no | no |
| Ordering | chronological (Recent/Latest); selected (Recommended) | chronological | ranked | ranked/mixed | ranked |
| Explicit interest inputs | tags you follow | subscriptions | follows (MyAllTop) | follows | follows/topic picks where offered |
| Implicit behavior signals | likes, comments (documented as model input) | none (anti-algorithm posture) | none on the surface | reactions, dwell, etc. (structural) | behavior-led (structural) |
| Feedback controls | block site (reader); identity-bound signals; explain-your-feed doc | n/a (no model) | n/a | unfollow/mute (graph-side) | like/hide/not-interested class (structural) |
| Cold-start behavior | documented (default tags) | n/a (list exists from day one) | n/a (shared) | follow suggestion flows (structural) | onboarding interest picks (structural) |
| Editorial/curator layer | Freshly Pressed (separate tab) | none | Techmeme/AllTop editors on the shared flow | none (community selection) | mostly none (structural) |
| Corpus origin | all public WordPress/Jetpack sites | user's chosen feeds | crawled publications | member-authored posts | platform-hosted or collected content |

Stable across all observed poles: the defining variable of the family is **who/what selects the items a given user sees** — the user's list (reader), the product for everyone (aggregator), a curator (curation), or the product for each user from that user's signals (this Type). WordPress.com directly demonstrates the reader pole and this pole coexisting in one product with different promises (complete+chronological vs selected+per-user), which is the cleanest boundary evidence available.

## Abstraction Levels

### L0 — Defining Invariant (deliberately small)

A Personalized Content Feed is recognizable by exactly this structure:

```text
Content items drawn from a standing corpus the product can draw on
  (platform-hosted, collected, or member-published — the product's job is
   feeding, not authoring)
  └── Per-user selection: the product's selection machinery weighs corpus
        items by signals about the individual user — behavior the user
        generates in the product and/or interests the user declares —
        so each user's flow is their own
        (the user's list may be one input, but selection between items
         across the corpus is the product's, not a list's faithful delivery)
        └── The personal flow: a standing consumption surface that is
              re-assembled as the user's signals accumulate
```

Three legs, jointly held:

- Remove the corpus → nothing to select from; no feed (a private inbox of one's own messages is not a content feed).
- Remove per-user selection → the flow becomes the same for everyone (Content Aggregator), or delivery of the user's own list (Feed Reader), or answers to queries (Search), or a curator's set (Curation). The "personalized" is gone.
- Remove the standing, signal-updating flow → a one-shot personal edition or a per-query result list; the "feed" is gone.

Notes on the L0 boundary:

- **"Inference/algorithm" is not definitional — per-user selection from that user's signals is.** The selector can be a learned model (the dominant modern form) or simpler machinery (WordPress's "popular posts based on the tags you follow"); the analog ancestor (a clipping service cutting each subscriber a personal daily digest from a stated interest profile) satisfies all three legs with zero software. What the Type requires is that *the product* selects *for this user* from *that user's signals*.
- **"Ranking" is not definitional.** A personalized-but-chronological surface (WordPress's "Latest: the latest posts related to tags you follow") is still per-user selection with recency order. The invariant is selection, not ordering algorithm.
- **The user's explicit choices (follows, topic picks) are legitimate inputs, not contamination.** The seam vs the Feed Reader is whether the list is the *sole selector with faithful delivery* (reader) or *one signal among others feeding selection across the corpus* (here). WordPress shows both regimes in one product with different promises.
- **Accounts are not definitional** (signal accumulation can bind to an account — WordPress documents exactly this — but the abstract requirement is persistent per-user signals, however carried).
- **Attribution/origin display is NOT in L0** (unlike the aggregator sibling): the essence of this Type is the selector, not source assembly. Origin/creator visibility is universal in observed products and held as standard structure.

### L1 — Common Mature Structure (standard capabilities)

- **Item cards with origin/creator attribution** — every observed implementation shows where an item came from (author/site/channel/creator).
- **Explicit interest inputs** — follow topics/tags/sources as declared signals (WordPress tags; AllTop MyAllTop; follows in social feeds).
- **Feedback controls** — like/react/save/hide and less-of-this controls; behavior influences later recommendations (WordPress: "Your post likes and comments … influence recommendations").
- **Cold-start handling** — defaults until signals accumulate (WordPress: default tags; onboarding interest picks in consumer apps — structural).
- **Eligibility/exclusion rules** per user — spam/safety filtering, language scoping (WordPress direct).
- **Explanation surfaces** — some products document or expose why items appear (WordPress's public factor documentation; "Why am I seeing this job?" in job boards).
- **Search beside the flow** — query results as a separate surface in the same product (WordPress Search tab).
- **Freshness/chronological fallback views** beside the selected flow (WordPress Latest; Techmeme River in the sibling family).
- **Identity-bound signals across sessions and devices** — the model accumulates on a persistent user identity (WordPress: account-bound likes/comments).
- **A retention handoff** — save/share actions out of the flow toward read-later/bookmarking tools (family-standard).

### L2 — Variant / Optional Structure

- **Packaging**: standalone feed-first application (personal feed as the product) vs named feed surface inside a larger product (reader, search engine, video platform, social product, e-commerce app). Both are the same Type; packaging is variant.
- **Content kind and scope**: short video, articles, web pages, mixed; general vs domain-scoped (news-scoped implementations shade toward the Personalized News Feed sibling).
- **Signal emphasis**: behavior-led vs declaration-led (follows/tags) vs hybrid; profile-attribute inputs where they exist.
- **Editorial/curated layer beside the algorithmic one** (Freshly Pressed as separate tab; editor-led surfaces in the aggregator family).
- **Item-conditioned secondary surfaces** ("related/more like this" attached to a current item — WordPress direct).
- **Governance posture**: transparency/explanation machinery, opt-outs from signal use (WordPress log-out mechanism), interest-management surfaces — present in some products, not observed as universal.
- **Creator/publishing side**: products whose corpus is member-authored also host creators; the creator economy around feed-first apps is a variant extension, not part of the consumption core.
- **Ads against the flow**: common business layer; not observed as part of the Type's structure.

### L3 — Vendor-specific Detail (research notes only)

- WordPress.com: default cold-start tags (`dailyprompt`, `WordPress`); documented factor list (title/content/tags/categories; media presence; recency; posting regularity; likes/comments totals and *who* performed them; subscriber counts and who subscribed; per-site rejection frequency from recommendations); "Reader Post Recommendations" lives in Discover's Search tab; "More on WordPress.com" related posts selected on title/content/engagement; language-based exclusion; log-out-to-exclude-comments mechanism; Freshly Pressed hand-selection by the team; guide review dates Sept 1–2, 2026; Reader self-describes as "a feed aggregator."
- Sibling-recorded details relied on for seams: NetNewsWire anti-algorithm homepage copy; Feedbin "no algorithm" YouTube copy; AllTop MyAllTop feature set; Techmeme editor-pyramid description and no-editor sister sites; elink's three separate solution pages; Komoot Home-feed inputs (location, sports used, past activity, follows); job-board explainer quote.

## Rejected Findings (considered, not promoted)

- **"This Type = short-video feeds"** — rejected: content kind is a variant (WordPress documents an article/blog corpus; search-engine discovery surfaces are mixed-kind). The corpus is open-ended.
- **"The selector must be a learned model / AI"** — rejected: WordPress's documented machinery includes simple popularity-by-followed-tags selection; the analog clipping-service ancestor satisfies the core. The invariant is per-user selection from that user's signals.
- **"Following/friends have no place in this Type"** — rejected: follows are common inputs (WordPress tags, AllTop, Komoot). The seam vs reader/social is *whether the list or graph is the sole selector*, not whether explicit choices exist.
- **"Ordering must be ranked, non-chronological"** — rejected: WordPress's "Latest" surface is per-user filtered and chronological. Selection, not ranking, is the invariant.
- **"Accounts are definitional"** — rejected as an L0 matter: what is required is persistent per-user signals, however carried; account binding is the common implementation (and WordPress documents it directly).
- **"Origin attribution is definitional"** — rejected for this Type (it is definitional for the Content Aggregator, whose essence is multi-source assembly): origin display is standard structure here, not the invariant.
- **"Completeness is never promised"** — refined: the personalized flow never promises completeness (that is a defining behavioral contrast with the reader), but a product can host both regimes on different surfaces (WordPress Recent vs Recommended).
- **"Ads/personalized advertising are part of the Type"** — rejected: business layer; no evidence pulled into the core.

## Boundary Findings

1. **vs Feed Reader (§02.08, processed) — joint-review flag DISCHARGED from this side.** The test is *whether selection between items happens at all*. Reader: the user's subscription list is the sole selector; the app faithfully delivers what chosen sources publish, complete and ordered by recency; reading state (unread/read) is central. Personalized feed: the product selects between items across a corpus the user did not enumerate, weighted by that user's signals; completeness is not promised. Direct evidence: WordPress.com hosts both — "Recent" (chronological delivery from followed sites) vs "Reader Post Recommendations" (a feed of recommendations based on what you've recently liked or commented on) — with different promises attached. Reader vendors define themselves *against* the algorithmic pole (NetNewsWire, Feedbin quotes). Removal test: replace per-user selection with faithful list delivery → reader; replace the list's selector role with signal-weighted selection → this Type.
2. **vs Content Aggregator (§02.08, processed) — joint-review flag DISCHARGED from this side.** The test is *whether the flow is shared*. Aggregator: the product's machinery (editors, scoring, clustering) assembles one flow — the same for everyone; personal feeds are an optional tuning layer on the shared surface (AllTop MyAllTop). This Type: per-user assembly *is* the core; without signals the product cannot render its primary surface (it must fall back to cold-start defaults — a behavior aggregators never need). Techmeme's auto-re-sorting front page is algorithmic but shared — machinery alone does not make a personalized feed. Removal test: remove per-user weighting → aggregator.
3. **vs Content Curation Platform (§02.08, processed) — joint-review flag DISCHARGED from this side.** No curator and no collection artifact here: the artifact is the standing per-user flow. Where human editorial judgment exists in this family, it operates on flows (aggregator editors) or as a separate curated surface (WordPress Freshly Pressed tab beside Recommended) — the market itself keeps the two artifacts apart even inside one product. Removal test: replace per-user signal selection with a human building persistent named collections → curation.
4. **vs News Aggregator / Personalized News Feed (§02.04, unprocessed)** — same machinery, narrower scope: a personalized feed restricted to news content shades toward the Personalized News Feed sibling, exactly as the Content Aggregator shades toward the News Aggregator (precedent from the sibling pass). Boundary = content scope, not structure. **Flag for joint review when that leaf is processed.**
5. **vs General Web Search Engine (§02.02, processed)** — query-first transient retrieval vs query-free standing per-user flow. Search assembles results per query and holds no standing flow; this Type assembles a standing flow without a query, updated by accumulated signals. WordPress demonstrates the split in one product (Search tab vs Recommended tab). Market note (structural, unreachable): search-engine discovery surfaces (Google Discover-class) are the most explicitly query-free implementations of this Type. Removal test: require a query for the surface to exist → search.
6. **vs Recommendation / Personalization Engine (§06, processed)** — consistent with that pass's own boundary: the engine is the B2B decision machinery sold to merchants/marketers; this leaf is a consumer-facing surface where the user *consumes* the output. Test: who logs in — an end consumer (surface) or an operator (engine). WordPress's recommendation feed is the surface; an engine product could power it.
7. **vs Marketing Personalization Platform (§06, processed)** — same surface/operator split, recorded consistently with that pass.
8. **vs social feed Types (General Social Network, Microblogging, Interest-based, Short-form Video — §01.05)** — the organizing key of the core consumption loop. In social Types, member identity and the personal connection graph are the primary distribution substrate: the user joins as a *member* whose ties select candidates (plus ranking). Here the user is primarily an *audience member* whose signals select items from a corpus; social ties may exist as inputs (followed creators) or not at all. Products straddling the seam: feed-first short-video apps (social features attached to an interest-feed core) — the §01.05 short-form-video leaf is unprocessed; **flag for joint review when that leaf is processed**, applying the §01.05 family discriminator (organizing key of the core loop) recorded by the general-social-network pass.
9. **vs Information Portal (§02.11, processed)** — consistent with that pass: the portal's artifact is the whole entry surface (content + services + routing); keep only the personalized article stream → this Type.
10. **vs Bookmark Manager / Read-it-later (§02.13/§02.09)** — retention artifacts vs consumption flow; save actions are the standard handoff out of the feed. Structural, consistent with sibling passes.
11. **vs Information Portal/Directory "personalized start pages"** — user-*configured* pages (choosing modules) are not this Type: configuration arranges fixed containers; it does not select between corpus items by signals. The seam is selection vs arrangement.
12. **Historical / market-sample check (conceptual — no product claims possible this pass)** — the analog ancestor satisfies the core: a personal clipping service cuts each subscriber a personal daily digest from newspapers according to the subscriber's stated interest profile (corpus + per-user selection from that user's signals + standing personal flow that updates). Early collaborative-filtering discovery products of the 2000s–2010s satisfy the core conceptually as well (Wikipedia/Wayback unreachable — no product-level claims made; kept weak per evidence rules). The L0 deliberately does not require: machine learning, ranking algorithms, ads, accounts, mobile apps, short-video form, or any specific content kind — so older, regional, minimal, and analog forms fit.

## Uncertainties

- **Consumer-platform pole undocumented** — the market's most prominent implementations (short-video feed-first apps, video-platform home feeds, search-engine discovery surfaces) were unreachable (timeouts ×1–2 per host, abandoned). Everything about them in this pass is structural; no machinery, signal, or control claims are made. If a later pass reaches them, re-verify: (a) whether their feeds expose interest-management surfaces; (b) whether explanation surfaces ("why this video") are standard; (c) whether any of them promises completeness anywhere.
- **Historical check is conceptual only** — no historical product could be documented (Wikipedia ×2 hosts unreachable, Wayback not attempted after sibling-pass failures). The clipping-service and CF-reader arguments rest on structural reasoning, not citations.
- **Explanation surfaces** — direct evidence exists for two products in the family neighborhood (WordPress public factor documentation; job-board explainer). Whether they are standard in the Type's core market is unverified; held at "some products."
- **Feedback-control vocabulary** ("not interested", "see less like this") — near-universal in market memory but not directly documented for any reachable product; written as common structure with structural support only.
- **Whether "attribution" should be upgraded** — observed universal in the sample but not structurally necessary; kept standard-not-definitional, flagged for the News Aggregator sibling's pass to re-test.
- **Scope risk** — reachable evidence is blog/reader-centered; the dominant market image is short-video. Mitigated by the family ratification from three sibling passes and by the open-ended corpus in L0; the consumer pole remains unobserved.
- **Packaging vs Type** — confirmed as variant (one product can host both reader and personalized-feed surfaces, WordPress); no taxonomy change recommended for §02.08.

## Final Synthesis

A Personalized Content Feed is a content-consumption application whose defining core is three jointly-held structures: a standing corpus of content items the product can draw on (hosted, collected, or member-published); per-user selection, in which the product's selection machinery weighs corpus items by signals about the individual user — behavior generated in the product and/or interests the user declares — so that each user's flow is their own; and the personal flow itself, a standing consumption surface re-assembled as signals accumulate. The selector — not the ordering algorithm, not the content kind, not the packaging — is the invariant: the same family that contains the reader (user's list selects, faithful delivery), the aggregator (product selects, same flow for everyone), and the curation platform (a curator selects into collections) selects here *for each user, from that user's signals*. Standard capabilities around that core include origin attribution, explicit interest inputs (follows/tags), feedback controls, cold-start defaults, per-user eligibility filtering, explanation surfaces, search beside the flow, and freshness fallbacks; variants include packaging (standalone feed-first app vs surface inside larger products), content kind, signal emphasis, and editorial layers beside the algorithm. The analog personal clipping service and the early collaborative-filtering discovery products satisfy the core without any modern machinery, which is the strongest available sign that the abstraction is not over-fit to the current dominant implementation — though the historical check had to be run conceptually, because the research environment could not reach any of the market's flagship implementations or any encyclopedic source.
