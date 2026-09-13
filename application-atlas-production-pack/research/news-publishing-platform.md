# Research Notes — News Publishing Platform

Directory location: §27 Media, Entertainment, Creator & Culture (siblings: Newsroom Management System, Magazine & Periodical Management, Media Subscription Management, Content Distribution Platform, Publishing Editorial Workflow; family neighbors: CMS / Headless CMS / Blogging Platform in §02.07; News Application / News Aggregator / Personalized News Feed in §02.04).

Research date: 2026-09-08.

## Research Goal

Understand what a News Publishing Platform actually is as an Application Type: its unit of record, the editorial workflow around it, how published news is kept current, how news surfaces are assembled, what channels one story reaches, and where the Type ends relative to CMS, blogging, newsroom planning, and the consumer-side news reading Types.

## Initial Boundary (working hypothesis before research)

- Hypothesis: the software news organizations (newspapers, digital-native outlets, broadcasters' text newsrooms, agencies) use to author, edit, curate, and continuously publish news content to their public channels, with print integration at the newspaper pole.
- Likely adjacent to: Content Management System / CMS (the obvious taxonomy risk — this may be "just" a news-vertical CMS), Newsroom Management System (§27 sibling, unprocessed), Blogging Platform (processed sibling), News Application / News Aggregator (02.04, consumer side), Media Subscription Management (paywall seam), Content Distribution Platform (syndication seam).
- Pre-hung flags from the magazine-periodical-management pass: center-of-gravity test applies to this leaf (daily news content flow / web content delivery vs issue-cadence business records), and a newspaper-adjacency question (MediaOS/Advantage serve newspapers — is a distinct newspaper Type warranted?).
- Unknowns: whether wire/agency ingestion is definitional or merely common; whether curation machinery (front pages) is definitional; how print integration is realized in modern platforms; whether "publish → update/correct" is a distinct structural loop vs generic CMS re-publishing.

## Research Questions

1. What is the unit of record and what does it carry? (story/article fields, media associations, byline, placement)
2. What does the editorial workflow look like? (states, transitions, who may do what, scheduling/embargo)
3. What happens to a story after it is published? (updates, corrections, removal, redirects — the "news is never finished" loop)
4. How does external/agency (wire) content enter the pipeline and how is it treated?
5. How are front pages / sections / homepages assembled and kept current? (curation machinery)
6. What channels does one published story reach? (web, apps, syndication feeds, newsletters, print, social)
7. How do roles and permissions structure newsroom work?
8. Where do paywall/subscription machinery and analytics sit — in-type or on a seam?
9. What realization forms exist? (SaaS suite, self-hosted open source, CMS distribution, headless-first)
10. Where exactly is the boundary with CMS / blogging / newsroom-planning / news-reading Types?

## Representative Products

Selected for market representativeness + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / position | Customer tier | Evidence strength |
|---|---|---|---|
| Arc XP | News-native end-to-end commercial SaaS suite, built inside a major news organization, now sold to other publishers | Large enterprise publishers | Strong (Tier-1 docs fetched, multiple pages) |
| Brightspot | Commercial enterprise CMS/DMS with a dedicated editorial-publishing practice | Enterprise (news + non-news) | Strong (Tier-1 docs fetched) |
| Superdesk | Open-source end-to-end news creation/production/distribution platform with news-agency heritage | Newsrooms/agencies, self-hosted | Strong (Tier-1 server docs fetched) |
| Thunder | Open-source Drupal distribution for professional publishers — the "general CMS adapted to publishing" pole | Mid-market publishers, self-hosted | Strong (Tier-1 docs fetched) |
| Quintype Bold | Commercial SaaS, headless-first newsroom CMS from a regional vendor | Mid-market / regional digital-native publishers | Strong (Tier-1 help center fetched) |

Dropped: WordPress VIP (docs.wpvip.com timed out ×1 and wpvip.com transport-error ×1 — abandoned per source-access rules; the general-CMS-at-news-scale pole is covered conceptually by Thunder). Not probed: legacy newspaper publishing systems (TownNews BLOX, Saxotech/CCI/DTI class) — historical check carried with degraded strength (see Historical Check).

## Sources

- Arc XP Learning Center — https://docs.arcxp.com/ (fetched 2026-09-08)
  - Composer overview; How to Setup Workflow Statuses; Curating in PageBuilder Editor; How to Ingest Wire Content Using an Inbound Wires Adapter; products index (Site Service, WebSked, Subscriptions, Outbound Feeds, Photo/Video Center, print integration, ANS).
- Brightspot Docs — https://docs.brightspot.com/ (fetched 2026-09-08)
  - Documentation hub (user guide / content types / integrations); Workflows (admin + usage).
- Superdesk documentation — https://superdesk.readthedocs.io/en/latest/ (fetched 2026-09-08)
  - Index (positioning: "open-source end-to-end news creation, production, distribution and publishing platform"); Publishing; Ingest; module map (Item Schema, Content Profiles, Content API, AI services).
- Thunder — https://thunder.github.io/ and https://thunder.github.io/user-guide/feature-overview.html (fetched 2026-09-08)
- Quintype help center — https://help.quintype.com/ (fetched 2026-09-08)
  - Bold overview; Articles category (Breaking News, Timeline, Embargo, Story Alternatives, Story Metadata, live blog, Sage AI); Content category (Collections, Sections, menus, scheduled stories); Collections article (manual/automated, Sorter, Home collection); https://developers.quintype.com/ (headless/API posture).
- Reachability notes: docs.wpvip.com and wpvip.com unreachable (timeout/transport error; abandoned after 2 attempts); support.quintype.com is a JS shell — help.quintype.com used instead; legacy newspaper-system vendors not fetched.

## Product Observations

### Product A — Arc XP (evidence layer A: direct observation, Tier-1)

- Positioning: Arc XP is described as a SaaS digital experience and content platform for news/media publishers; documentation is organized as a news-native product suite.
- **Authoring (Composer)**: "content authoring tool that serves as your centralized hub for your website content… drafting, editing, and publishing functionalities"; stories combine content elements (photos, videos, galleries) managed in companion apps (Photo Center, Video Center, Audio Center). Stories have revision history, suggesting mode, story templates, custom headlines, kickers and labels, featured media, story variants, story validation rules, proofreading integrations, live blogging ("Implementing Live Blogging in Arc XP"), and "Send to Print" functionality.
- **Workflow statuses**: default statuses Draft / Edit / Publish; organizations customize them ("Some organizations might use four or five statuses… others might need over a dozen"); status changes are manual (no save/publish auto-trigger); a status change can auto-create a task in the planning product (WebSked) assigned to an editor group, with Slack/email/Teams notifications.
- **Planning (WebSked)**: content tasks, pitching, publications, collections, publish window intervals, platforms; workflow-status changes trigger tasks; WebSked collections can add stories and have dynamic backfill.
- **Curation (PageBuilder Editor)**: pages/templates are "configured, curated, and published" from a dashboard; building elements are blocks and chains ("Every element on a page, including stories, titles, video playlists, and navigation bars, is a block"); content comes from feeds/sources (e.g. `content-api`, RSS feed block, global content feeds); drafts are previewed (output types desktop/mobile, device preview) and published; scenario documents curating a page "for special coverage… a gala or an election".
- **Wire ingestion**: "Arc XP supports feeding content into Composer, Photo Center and Video Center from external sources — this is called a 'wire'. One well recognized external provider of news content is The Associated Press." Wire content arrives unpublished, is mapped into the platform's native content format (ANS), inventoried/deduplicated, placed into websites/sections, and (strongly recommended) published by newsroom action rather than auto-published.
- **Publishing/distribution**: Draft API "circulate/decirculate" documents to websites with generated URLs and redirects; unpublish; content event streams (Kinesis); Content API for search/delivery; Outbound Feeds (syndication feeds); multi-site via Site Service (websites, sections, navigation, section custom fields); display/publish date overrides.
- **Media**: Photo Center (uploads, galleries, lightboxes, IPTC metadata mapping, focal point, restrictions, usage logs, deletion policy); Video Center (live streams, VOD, clipping); Audio Center.
- **Monetization/audience (separate pillars)**: Subscriptions product (identity, retail offers, paywall rulesets/entitlements, edge content protection, customer service admin); Audience Insights; integrations with analytics (Chartbeat, Google Analytics) and optimization (Sophi).
- **Migration**: Migration Center for historical CMS imports (with ANS maps).

### Product B — Brightspot (evidence layer A: direct observation, Tier-1)

- Positioning: CMS platform with a dedicated "for editorial publishing teams" practice; docs organized around content types, publishing, dashboards, sites & settings, users & roles, workflows.
- **Workflows**: "A workflow moves an asset through a defined sequence of statuses—such as first draft, final draft, and publication"; workflows are configurable per content type and per site; statuses have colors and named transitions; comment-on-transition can be required; Brightspot saves a draft for each workflow status; version history widget; role permissions can limit specific workflow transitions (e.g. one role edits, another proofreads); a Publish Override exists for roles with publish permission who must skip steps; workflow notifications; bulk workflow moves; assets searchable by workflow status; published items can be pulled back into a workflow via new revision/republish.
- **Content model**: content types (editorial content types creatable by admins), assets (incl. Article-class types per content-types guide), pages/modules; sites & settings (multi-site); redirects manager; audiences; dashboards/widgets (Recent Activity, Unpublished Drafts).
- **Delivery**: GraphQL/REST APIs; integrations (analytics, tag manager); theme/design system.

### Product C — Superdesk (evidence layer A: direct observation, Tier-1)

- Positioning (self-description, index page): "Superdesk is an open-source end-to-end news creation, production, distribution and publishing platform." (AGPL; Sourcefabric.)
- **Ingest (the wire-in channel)**: ingest providers configured per external source; feeding services transport over HTTP, FTP, file system, e-mail, RSS; feed parsers for ANPA 1312, IPTC 7901, NewsML 1.2, NewsML 2, NITF, plus agency-specific parsers (AP ANPA variant, AFP NewsML variant, dpa IPTC 7901 variant, Press Association NITF variant, WENN); rule sets and routing schemes transform/route ingested items; webhooks can trigger ingestion; providers have schedules, idle warnings, closure states, critical errors.
- **Publish workflow (the full news lifecycle)**: publish actions exposed as endpoints — publish, correct, kill, unpublish, takedown, resend; item states include published, corrected, killed, recalled, unpublished, spiked, scheduled; validation blocks: embargoes combined with schedules, unpublished related items, locked/killed/spiked/recalled associations; packages (groupings of items) publish per-subscriber with wanted/unwanted items; version counters increment per operation; pubstatus vocabulary (e.g. "usable") used on publish.
- **Distribution**: subscribers/destinations with types (e.g. a WIRE subscriber only receives text/preformatted content); products + content filters (filter conditions, global filters, geo targeting regions) match items to subscribers; formatters produce JSON/XML/HTML; publish queue/task states; Content API as a delivery surface; legal archive; Event & Planning as a parallel exchange type.
- **Content model**: item schema (identifiers, content metadata, controlled vocabularies/CVs); content profiles per content type (text, preformatted, packages) with field validation; media storage; AI/ML service hooks (article analysis, LLM actions); spellchecking.

### Product D — Thunder (evidence layer A: direct observation, Tier-1)

- Positioning: "Thunder is a Drupal distribution for professional publishers", established 2016 by Hubert Burda Media's Thunder Coalition; current docs updated 2025-12.
- **Editorial workflow**: Content Moderation module "enables you to have an editorial workflow. Editors can have different permissions for creating, editing and publishing articles. It also allows you to have a published version of an article, and have a separate working copy that is undergoing review before it is published."
- **Article structure**: Paragraphs module — articles composed of typed sub-elements (text block, image, video, social cards, slideshows) created, edited, reorganized; media browser (drag-drop upload, auto-crop, focal point); galleries; device preview; autosave; content lock (blocks concurrent editing); Diff for revisions.
- **Lifecycle**: Scheduler (schedule publish and unpublish dates; media expire with placeholder replacement); Access Unpublished (share unpublished content via unique URL); Pathauto URL aliases + automatic Redirect when an article URL changes; Metatag (SEO + Open Graph/Twitter cards); XML sitemaps; Length Indicator for SEO fields.
- **Regional/optional**: Search API framework; IVW integration (German audience-measurement organization) — regional variant evidence.

### Product E — Quintype Bold (evidence layer A: direct observation, Tier-1)

- Positioning: "Quintype helps publishers hit the ground running with a powerful, data-driven, headless CMS"; product family: Bold (CMS — "create, curate, distribute content"), Page Builder (presentation), Accesstype (subscription management), Metype (engagement), Mobile Apps; Malibu React framework + REST APIs on the front-end side.
- **Story model**: stories are the unit; Story Editor with card/element structure; story templates: text stories, photo stories, video stories, listicle stories, visual stories, live blogs ("How To Create A Live Blog"); each save creates a new version (Timeline; restore previous version); Story Metadata tab; Story Alternatives ("a story can have a Headline and a Hero image used on the story page… it can also…" have alternatives used elsewhere); Story SEO + SEO scores; photo editor; card reuse and card sharing; public preview; clone story; guest authors vs contributors; Embargo ("set a fixed publishing time for a story, which remains locked for a designated period"); Retain Last Publish Time when republishing updates.
- **Speed path**: Breaking News — "announce 'breaking news' to your audience, bypassing the typical workflow a story goes through."
- **Curation**: Sections ("the most fundamental methods for content categorization"); creating a section automatically creates a Collection; Collections are "a group of published stories or collections referencing published stories" — manual (explicitly added, refined via advanced search) or automated (filters by tags/sections/authors/story types/trending; exclude-section rules); a Sorter tab lists candidates and lets editors pin and drag-rank items; pinned stories take precedence over automated picks; scheduled stories can be ranked before publication; the Homepage is managed through the default "Home" collection, which typically composes other collections (optionally mirroring navigation); collection templates provide layouts (magazine template carries date/price metadata); collection preview (mobile/web).
- **Distribution**: headless delivery via APIs to web (Malibu/Page Builder) and mobile apps; Story Social Notifications tab controls notifications shown to readers when a story publishes; magazines/issues managed as collections with dedicated APIs.
- **AI**: Sage AI assistant (headline/sub-headline/meta suggestions, translation, RAG-based recommendations, tag suggestions, AI summary element).

## Cross-product Comparison

| Dimension | Arc XP | Brightspot | Superdesk | Thunder | Quintype Bold |
|---|---|---|---|---|---|
| Unit of record | story (ANS document) | asset / content type (Article-class) | item (content profiles; text/preformatted/package) | node/article (Paragraphs structure) | story (card/element structure) |
| Editorial gate | workflow statuses (default Draft/Edit/Publish, org-customizable; manual changes) | configurable workflow per content type (statuses, transitions, comments) | state machine (draft → published; spiked, scheduled) + content profiles validation | Content Moderation (published version vs working copy, permissions) | typical workflow + Breaking News bypass; embargo lock |
| Update loop after publication | republish/circulate updates; unpublish; URL redirects; decirculate | republish from draft / new revision re-enters workflow; Publish Override | correct / kill / takedown / unpublish / resend actions with states (corrected, killed, recalled) | re-edit published; published vs working copy; redirects on URL change | update + republish (retain last publish time); restore versions |
| Wire/agency in | yes — inbound wires adapter, arrives unpublished, mapped to native format (A) | not observed in reachable docs | yes — ingest providers + legacy/agency formats (A) | not observed in reachable docs | not observed in reachable docs |
| Curation surface | PageBuilder Editor pages: blocks/chains + content feeds; special-coverage scenario (A) | pages + modules over content types (A, lighter detail) | packages/groupings; front-end publisher in ecosystem (partial A) | Drupal pages (generic machinery; A) | Collections + Sorter; Home collection composes collections (A) |
| Scheduling / embargo | display/publish date overrides; WebSked publish windows (A) | workflow steps (scheduling not directly observed) | publish schedule + embargo with validation rules (A) | Scheduler module publish/unpublish dates (A) | Embargo; scheduled stories rankable in collections (A) |
| Revisions/versioning | revision history (A) | version history + draft per status (A) | version counters per operation; version records (A) | Diff / revisions (A) | Timeline per save; restore (A) |
| Roles | roles, squads, per-website permissions (A) | users & roles; role-limited transitions (A) | authentication/authorization layers; desks (server docs) (A-) | Content Moderation permissions (A) | users & roles category; schedule/publish permission decoupling note (A) |
| Delivery channels | websites (multi-site), Content API, mobile SDK, outbound feeds, print (send-to-print) (A) | web front-ends + GraphQL/REST APIs (A) | subscribers/destinations (wire/print/web), Content API (A) | web (Drupal theme); modules (A) | web (Malibu/Page Builder), mobile apps, notifications, magazines (A) |
| Media machinery | Photo/Video/Audio Center; IPTC metadata (A) | assets incl. images/videos (A, light) | media storage; associated items validation (A) | Media Library; galleries; focal point (A) | photo editor; image engine; video stories (A) |
| Monetization | Subscriptions product (paywall rulesets, entitlements) (A) | not center (audiences exist) | — (agency distribution, not reader revenue) | — (IVW measurement variant) | Accesstype sibling product (paywall/subscription) (A) |
| Planning surface | WebSked (tasks, pitches, publications, collections) (A) | dashboards/notifications (light) | Event & Planning exchange type exists (A-) | — | — |
| Realization form | commercial SaaS suite | commercial enterprise CMS | open-source (AGPL) self-hosted | open-source Drupal distribution | commercial SaaS, headless-first |

Evidence-layer notes: rows marked (A) have direct per-product documentation support; wire-ingest and print show up in only a minority of the sample and are therefore held as common/variant, not definitional; Superdesk's subscriber/product/filter distribution machinery is the news-agency pole of the same publish loop.

## Canonical Abstraction

### L0 — Defining Invariant

A News Publishing Platform is the newsroom's continuous produce-and-publish system. Its defining core is three jointly-held structures:

1. **The story as the unit of editorial record** — a persistent, individually identified article carrying headline, body content, media associations, authorship, and placement metadata (sections/taxonomy). Remove → a writing tool or a generic web page builder; there is no news record.

2. **The gated, revisable publication lifecycle** — work happens in non-public states and reaches the organization's public channel(s) through an explicit publish act controlled by workflow and (commonly) roles/schedules; a published story remains a living record that can be updated, corrected, moved, or removed through dedicated operations. Remove the gate → self-publication (blog territory); remove the revisability of published records → static publishing with no news loop.

3. **The curated presentation surface(s)** — at least one editorially ordered assembly (front page/homepage, section pages, collections/editions) built from the story stream and kept current by editorial action independently of individual stories. Remove → a chronological feed (blog) or a headless content store.

The publish act in (2) presumes delivery machinery: the platform itself renders or feeds the published story to the organization's public channel(s) (web pages and/or APIs/feeds to apps and partners). Channel breadth (web, apps, syndication, newsletters, print) is a variant property; the existence of platform-operated delivery is not.

Jointly-held load-bearing tests:

- 1 alone = writing tool (word processor / blog editor).
- 2 without 1 = a generic workflow tool.
- 1+2 without 3 = newsroom content store / feed with no editorial presentation (headless content API pole).
- 3 without 1+2 = website builder or aggregator.
- 1+3 without 2 = a mockup of a news site with no newsroom gate; published records would be directly editable public pages (blog/CMS territory).

### L1 — Common Mature Structure

Present in most mature products (several with direct Tier-1 evidence), but not required to recognize the Type:

- wire/agency ingestion (external content streams enter as unpublished drafts for newsroom treatment; observed in 2 of 5 sampled products, both news-native/agency-heritage — held common-not-definitional)
- multi-role newsroom permissions (reporter/editor/desk; workflow-transition permissions; per-site/per-section scoping)
- scheduling and embargo/timing controls (scheduled publish/unpublish; locked publish times; publish windows)
- revision history and per-status drafts
- media management surfaces (photo/video libraries, galleries, IPTC-class metadata, focal points)
- speed paths for breaking coverage (bypass routes, live blogs)
- SEO/structured metadata, social cards, and redirects when story URLs change
- headless delivery (Content APIs) and multi-site/multi-brand organization
- editorial planning surfaces (task boards, pitch/planning calendars) attached to the story flow
- analytics/audience-tooling integrations; AI assistance overlays

### L2 — Variant / Optional Structure

- print/pagination integration (newspaper pole; "send to print" machinery; print-era systems were print-only — the same core structure served by different channels)
- reader-revenue machinery at the content boundary (paywall rules, entitlement checks) — realized in-type (bundled product pillar) or via sibling subscription products
- outbound syndication/agency distribution (wire-out pole: subscribers, products, filters, agency formats)
- live coverage machinery (live blogs, live video) as first-class story types
- deployment/ownership form: commercial SaaS suite vs self-hosted open source vs open-source CMS distribution vs headless-first
- regional/sector realizations: magazines/issues managed as collections, audience-measurement integrations (national media-measurement bodies), multilingual editions
- adjacent surface bundling: community/engagement widgets, advertising blocks, event/calendar content types

### L3 — Vendor-specific Structure (Research Notes only)

- Arc XP: ANS native content format; Composer/PageBuilder/WebSked/Photo Center product names; circulation ("circulate/decirculate") API vocabulary; Clavis/Sophi recommendations; Bandito content testing; Kinesis event streams; Vindicia payment integration; PoWa player.
- Quintype: Bold/Accesstype/Metype/Malibu/Sage product names; Story Alternatives framing; Ahead multi-publisher line; Home collection's 15-collection front-end rendering note (product-specific limit, not asserted in final doc).
- Superdesk: ANPA 1312/IPTC 7901/NewsML/NITF parser inventory; pubstatus vocabulary; kill/correct/takedown endpoint naming; legal archive.
- Thunder: Drupal module inventory (Gin, Paragraphs, Tagify…); IVW module.
- Brightspot: Esca automations; publish-override button naming; numerical transition-prefix convention.

## Vendor-specific / Rejected Findings

Rejected from the canonical core (anti-overfitting):

- **"It's a CMS"** as the definition — CMS machinery (content types, media, pages, SEO) is the shared substrate, not the differentiator; a definition that stops there cannot separate this Type from general web publishing.
- **Wire/agency ingestion as definitional** — only a minority of the sample documents it in reachable docs; small digital-native outlets operate without wires; held common (L1).
- **Multi-channel breadth (web + app + social + newsletter) as definitional** — single-channel poles exist; the invariant is platform-operated delivery of the published record, not channel count.
- **Live blogs / breaking-news buttons as definitional** — variant realizations of the speed path; the underlying invariant (revisable published records + gated fast lane) is already in L0.
- **Paywalls as definitional** — monetization is a segment/business-model variant (L2) and sits on the seam with Media Subscription Management.
- **Print integration as definitional** — newspaper-pole variant (L2).
- **Specific workflow state names** (Draft/Edit/Publish; published/corrected/killed/recalled) — vendor/configurable realizations; the canonical concept is the gate + the post-publication operations, exact labels vary by product.
- **Homepage as the only curation surface** — curated assemblies include sections, collections, editions, and packages; the homepage is the most common realization, not the definition.

## Boundary Findings

- **vs Content Management System / CMS (§02.07) — the central seam.** Shared substrate: content types, editorial workflow, media libraries, pages, SEO/redirects. The distinguishing structure is the news-operation loop layered on that substrate: external wire/agency input, gated speed paths, post-publication correction/removal semantics treated as first-class record operations, and editorially-ordered front/section assemblies kept current as the stream changes. Remove-tests: strip the news loop from a news platform → a general CMS/DMS remains (Thunder demonstrates the reverse direction: a general CMS + publishing modules approaches this Type but, in its default doc set, lacks the wire and post-publication record operations). Verdict: keep-both; this Type is the news-operation realization of publishing machinery, recorded as a vertical-realization relationship rather than an alias — flagged for the taxonomy pass (see Boundary Issues).
- **vs Newsroom Management System (§27 sibling, unprocessed).** Planning/assignment machinery (what will be covered, by whom, when, on which platform) vs the production-and-publication machinery of the content itself. Straddle documented first-hand: Arc XP's planning product (tasks, pitches, publications, workflow-status-triggered tasks) ships inside the publishing suite, so planning appears here as a pillar. Proposed seam for that pass: assignment/planning records (pitches, tasks, rundowns, budgets of coverage) as its center vs the story publication record as this Type's center; product-spanning planning modules held as bundling evidence, not Type identity.
- **vs Magazine & Periodical Management (§27, processed) — discharges that pass's pre-hung flag.** Center-of-gravity confirmed: this Type centers the content flow (story → publish → update → curate → deliver); the magazine pass centers issue-cadence business records (publications, issues, ad/circulation machinery). Content machinery inside magazine systems is one pillar there (their pass already documented this); business machinery inside news platforms (reader-revenue pillars) is one pillar here. Newspapers adjacency: newspaper operations are held to be a variant of this Type (content machinery + print integration), while newspaper business records (ad sales, circulation) belong to the magazine-pass machinery — no separate newspaper Type is warranted from this side.
- **vs Blogging Platform (§02.07, processed).** The processed sibling's core is the author-owned publication of dated posts in a reverse-chronological stream. The news Type differs structurally: institutional multi-role operation with an editorial gate, curated (not purely chronological) presentation surfaces, and post-publication record operations (correct/remove) as system semantics. Remove-test: strip the gate, curation assemblies, and multi-role structure → the product is a blog.
- **vs News Application / News Aggregator / Personalized News Feed (§02.04).** Those are consumer-side reading surfaces (selection, presentation, personalization of news for a reader); this Type is the newsroom-side production system. The two interlock: publishing platforms expose content APIs that news applications consume. Different users, objects, and workflows — clean boundary.
- **vs Content Distribution Platform (§27, unprocessed).** Distributing finished content to external surfaces/partners vs the internal produce-and-publish loop. Superdesk's subscriber/product/filter machinery is the wire-out (agency) pole that sits near this seam — recorded as a variant realization of the publish loop, flagged for that pass's attention.
- **vs Media Subscription Management (§27, unprocessed).** Paywall/entitlement checks at the content boundary are in-type here as an L2 capability; subscription products, billing, renewal, and subscriber service are that Type's center. Straddle poles documented (bundled subscription pillars in two sampled products) — joint review recommended when that leaf is processed.
- **vs Headless CMS (§02.07).** Headless delivery is an architecture variant inside this Type (one sampled product is headless-first; two others expose Content APIs), not a boundary.
- **vs Media Asset Management (§27, processed).** Photo/video libraries inside news platforms are bounded production media surfaces attached to stories; the MAM Type owns media-asset corpus custody/archive machinery. Bundled media centers are capability evidence, not Type merger.
- **vs Publishing Editorial Workflow (§27, unprocessed).** Book/periodical editorial workflow (title/edition cadence) vs the news continuous loop; expected to be distinguishable by object and cadence — noted for that pass.

## Historical / Market-Sample Check

Would older, regional, or differently positioned products still fit the L0?

- Print-era newspaper workflow: story slug/copy as the record; copy desk as the gate; corrections and kills as standing wire-industry operations; the front page and section fronts as curated assemblies; delivery to print channels. All three L0 structures hold with print as the delivery channel — the definition does not name web, apps, or SaaS. (Conceptual; print-era systems were not directly documented this pass.)
- Direct documentary support for the lineage: the open-source sample still ships parsers for ANPA 1312, IPTC 7901, NewsML 1.2, and NITF — wire-industry formats of the teletype/newspaper era — proving the same record-and-distribute structure persists across eras.
- Regional pole: a German publishing coalition's CMS distribution (with a national audience-measurement integration) and an Indian headless newsroom SaaS both satisfy the L0 without any US-market-specific machinery.
- General-CMS pole: a generic CMS adapted for publishers satisfies the L0 once the news-operation loop is present; where that loop's machinery is absent (wire, record-level corrections), the product sits on the CMS side of the seam — the seam, not the brand, decides.
- Conclusion: the L0 is not over-fitted to the current SaaS-suite implementation; wire, paywalls, AI, and multi-channel breadth stay out of the definition.

## Uncertainties

- Brightspot's news-specific surfaces (wire handling, print, live coverage) were not observable in the reachable docs; its evidence supports the substrate + workflow legs strongly, the news-loop legs only via positioning ("for editorial publishing teams").
- Superdesk's client-side curation UX (desks, monitoring queues) is documented in a user manual PDF not fetched; server-side evidence is strong, client-side curation detail is partial.
- Legacy newspaper systems (TownNews/Saxotech/CCI class) not directly documented; print-era reasoning kept conceptual; assertions about them carry lineage strength only.
- Whether curation machinery is strictly L0 vs L1 was a genuine judgment call; held in L0 on the strength that the editorially-ordered front/section surface is the oldest and most universal news artifact, and that 3 of 5 sampled products document dedicated curation machinery. If a future pass finds a recognized newsroom product with no curation surface at all, this leg should be re-tested.
- Reader-revenue machinery depth varies (bundled pillar vs sibling product); exact boundary with Media Subscription Management deferred to joint review.

## Final Synthesis

A News Publishing Platform is the newsroom's system of record and continuous production line for news: stories are authored and held as identified records; they pass an editorial gate into publication on the organization's public channels; published stories remain living records that can be updated, corrected, or removed through dedicated operations; and editorially curated surfaces (front pages, sections, collections) are kept current over the story stream. Wire/agency ingestion, newsroom roles, scheduling/embargo, revisions, media centers, speed paths, SEO/redirects, headless APIs, planning boards, print integration, paywalls, and AI assistance are the standard, variant, or era-specific machinery layered on that core. The Type is bounded against CMS (substrate without the news-operation loop), blogging (personal stream without gate/curation/corrections), newsroom management (planning of work vs publication of work), and the consumer-side news reading Types.
