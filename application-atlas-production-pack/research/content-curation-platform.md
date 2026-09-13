# Research Notes — Content Curation Platform

Research date: 2026-09-07
Leaf: Content Curation Platform (DIRECTORY §02.08 Feeds & Curation)
Slug: content-curation-platform

## Research Goal

Understand what a Content Curation Platform actually is as an Application Type — its defining structure, its standard capabilities, its variants — from real products, and establish clean boundaries against the sibling leaves in §02.08 (Feed Reader, Content Aggregator, Personalized Content Feed) and against adjacent Types (Bookmark Manager §02.13, Read-it-later §02.09, Social Networking §01.05, Content Publishing §02.07, marketing Types §06).

## Initial Boundary (hypothesis before research)

- Hypothesis: curation = selective human choice of third-party content + organization into persistent collections + presentation to an audience.
- Nearest neighbors: Feed Reader (subscription stream consumption), Content Aggregator (automated gathering), Personalized Content Feed (algorithmic per-user stream), Bookmark Manager (personal saving/retrieval), Read-it-later (consumption queue), Social Network (person/feed-centric), CMS/Blogging (owned content authoring), Newsletter Marketing / Social Media Management (distribution channels).
- Known unknowns: is a suggestion/discovery engine definitional? Is "third-party content" definitional? Where exactly does curation end and aggregation begin (automated curation products)? Is the consumer-social pole (Flipboard/Pinterest class) the same Type?

## Research Questions

1. What objects exist in the system (item, collection/topic/board/magazine, source, curator profile, suggestion queue, workspace)?
2. Where do items come from (suggestion engine, RSS, clipper/extension, email-in, social import, manual add, upload)?
3. What does the curation loop look like end-to-end (discover → select → enrich → organize → publish → distribute → measure)?
4. Who consumes the output and through what surfaces (public topic page, link, embed, newsletter, team board, profile)?
5. What lifecycle and rules matter (privacy defaults, collaboration permissions, attribution/rights, staging areas, update propagation)?
6. Which capabilities are variant (suggestion engine, analytics, governance, education templates, AI) vs defining?
7. How do the §02.08 siblings differ structurally?

## Representative Products

Selected for market representation + different product philosophies + different customer tiers:

| Product | Pole | Customer tier | Evidence obtained |
|---|---|---|---|
| Scoop.it | curation-as-publishing for professionals/organizations (Select → Organize → Share) | prosumer → business/public sector/education | Tier-2 homepage + business use-case page (fetched) |
| Curata CCS | enterprise B2B content-marketing curation engine (Find → Curate → Share) | enterprise marketing teams | Tier-2 product page (fetched); app docs login-gated |
| Wakelet | education/community visual collections | education (free→institution) + teams | Tier-1 help center (index + 3 articles) + Tier-2 homepage (fetched) |
| Pearltrees | consumer visual curation with social interest graph | consumer freemium | Tier-1 FAQ (full) + root page (fetched) |
| elink.io | links→bundles→published outputs (webpage/newsletter/widget) | SMB/prosumer teams | Tier-2 product page (fetched) |

Boundary/market anchors (not primary samples):

- Flipboard — consumer social curation (magazines). Unreachable: about.flipboard.com timeout ×2, about.flipboard.com/faq timeout, flipboard.com timeout ×1. Abandoned per network rule. Market context only; no claims.
- Paper.li — automated "digital newspaper" curation. Domain repurposed (now a German content blog; the original service described in past tense on its own former domain). Market-drift observation only; not official product documentation of the original service.
- Pinterest-class visual discovery — straddle candidate vs Social Network; not sampled; flagged for the §01.05 pass.
- Feedly — feed reader with team curation boards; straddle candidate vs Feed Reader; sibling leaf unprocessed; not sampled.

## Sources

Fetched 2026-09-07 (all official vendor surfaces):

- Scoop.it homepage — https://www.scoop.it/
- Scoop.it for Businesses — https://www.scoop.it/en/scoop-it-for-businesses
- Curata Content Curation Software — https://www.curata.com/products/content-curation-software
- Wakelet homepage + FAQ — https://wakelet.com/
- Wakelet Help Center index — https://help.wakelet.com/
- Wakelet "What is Wakelet?" — https://help.wakelet.com/migration/what-is-wakelet
- Wakelet "What are Items?" — https://help.wakelet.com/migration/items
- Wakelet "All about Workspaces" — https://help.wakelet.com/migration/all-about-workspaces
- Pearltrees root — https://www.pearltrees.com/
- Pearltrees FAQ — http://www.pearltrees.com/s/faq/en
- elink.io homepage — https://elink.io/
- Paper.li (repurposed domain, market-drift observation) — https://www.paper.li/

Unreachable (recorded limitations):

- Flipboard: about.flipboard.com, about.flipboard.com/faq, flipboard.com — timeout ×4 total. No claims drawn.
- Scoop.it Help Center (intercom.help/meltwater-scoop-it/en) — timeout ×1. Operational details not verified from help center.
- Curata application docs — login-gated; product-page evidence only.

## Product Observations

### Scoop.it (evidence layer A — official homepage + business page)

- Self-description: "a simple and flexible content curation platform that allows you to engage your external or internal audiences with relevant information organized by themes."
- Three-step loop stated on homepage: 1. Select, 2. Organize, 3. Share.
- Select: "advanced content engine monitors millions of sources worldwide to help you detect and select the best content. Discover new sources, add the sources you typically follow or upload your own content." Business page adds: Boolean searches with filters/keywords; add monitored sources via RSS feeds; 1-click publish of the article being read via "smart bookmarklet"; create/upload own content (PDFs, images, videos); "Share your perspective on the selected article by adding value for your audience."
- Organize: "Create your personalized, private or public topic pages to store relevant content. Enrich each content with your expert analysis and tags... Animate your content hubs collaboratively." Topic pages can become "a true intelligence portal."
- Share: feed social networks; integrate on website/blog/intranet/document portal; "Create, automate and send your personalized newsletters from Scoop.it"; "Measure impact and ROI."
- Platform features: governance (administration of user rights and roles), SSO, API, embed windows, RSS feeds, Microsoft Teams/Slack integration, exportable statistics, SaaS hosted in France, GDPR compliance, dedicated account manager.
- Use cases: businesses, public sector, education, internal communication, external communication, knowledge management, newsletter, content distribution.
- Audience framing: "external or internal audiences."

### Curata CCS (evidence layer A — official product page)

- Positioning: B2B content marketing; curation as a service to audiences ("combat information overload for your most valued audiences"); "source up to 25 percent of their content via trusted, industry resources" (vendor claim).
- Three-step loop: Find → Curate → Share.
- Find: "hundreds of thousands of sources"; engine "learns and dynamically adapts to your content preferences"; NLP discovery; refine content flow by source; social-media sourcing; browser plugin to "curate on the fly"; team crowdsourcing ("enable your team to contribute and suggest content"); programmatic quality filtering (out-of-date, other languages, duplicative).
- Curate: "organize, annotate and create"; self-learning recommendation engine "suggests content and prioritizes by relevancy"; "intelligently pre-populates the curated post"; review workflow ("review hundreds of articles, videos and images in just 20 minutes a day" — vendor claim); optional original authoring inside Curata; contextualization ("add your own unique perspective & insight"); automatic categorization against "a customized taxonomy"; trending-topic landing pages for SEO (vendor feature); content enrichment metadata (pictures, quotes, videos); smart recommendations; "archive & index... full text search"; royalty-free image suggestions.
- Share: "publish and promote to all of your channels with one click"; built-in responsive site & blog; CMS integrations (WordPress, Joomla, Drupal "and many more"); marketing-automation integrations (Eloqua, Marketo, HubSpot, MailChimp, Act-On); social scheduling with "customizable hashtags and author attributions"; email newsletters ("lead capture, templates, list segmentation, and automated scheduling"); exportable feeds & API for widgets/mobile apps/integrations; "define customized schedules, templates and publishing rules"; automatic posting.

### Wakelet (evidence layer A — Tier-1 help center + homepage)

- Self-description (help center): "the best way for people to save, organize, and share the online content that is most important to them, all in one place - from videos and podcasts to news articles, tweets, and Instagram posts. Wakelet enables that content to be organized, annotated and interacted with natively. Keep it private or share it with others."
- Homepage: "content curation platform that helps you save, organize, and share links, files, and ideas in visual collections." Loop: Organize / Collaborate / Present. "Save links, files, videos, images, PDFs, and notes into clear collections"; "Invite others to contribute"; "Turn your content into visual pages that are easy to present, publish, and share."
- Items (help center): "your go-to spot for collecting and organizing diverse types of multimedia content, ranging from links and images to videos, text, and PDFs. Think of it as a modern take on bookmarks." Items tab: keyword search; All Items / Unsorted filters (Unsorted = saved items not yet placed into collections — a staging state); type filters (Text/Link/Image/Video/PDF); sort options (last updated, date asc/desc, name A-Z/Z-A).
- Collections: cover image, copy collection, export items to PDF; publish collections to profile; profile sections organize public collections; share profile.
- Workspaces (help center): "a digital hub for schools or districts" (Education/Education Pro plans); hierarchy organization → schools → groups → members; rostering integrations (Clever, ClassLink) auto-populate schools; roles: Super Admin (org-wide control, analytics, feature access/sharing permissions, role assignment), Admin (group-level permissions, view/manage group content), Editor (create collections within groups, collaborate); admins can view/edit Editors' collections; workspaces are self-contained (collections cannot move between workspaces).
- Plans: Starter / Pro / Education / Education Pro / Business / Enterprise (plan names from help center index).
- Use cases (homepage nav): lesson plans, portfolios, research, newsletters, collaboration, resource sharing, bookmarking, trip planning.
- Browser extension; ambassador program (community).

### Pearltrees (evidence layer A — official FAQ, full)

- Self-description: "a place to organize everything... organize, explore and share everything you're interested in. Save web pages, files, photos or notes and organize them. Explore amazing collections that relate to your interests and subscribe to their updates."
- Objects: items ("pearls": web pages, files, photos, notes); collections ("A collection works as a folder in which you can organize items or other collections" — nested collections); dropzone ("where you can store items before organizing your account. Only you have access to your dropzone"); editorial ("a short description of a collection... explain the purpose"); sections/groups inside collections; collection image/background customization.
- Capture: Add button + URL paste; web clipper (Chrome/Firefox) with destination choice (dropzone / new collection / existing collection); mobile share; email-in (send URL to add@pearltrees.com); social import (auto-collect links tweeted/posted; #CollectionName hashtag routing into named collections); drag-and-drop files; import favorites (Chrome, Firefox, Diigo, etc.).
- Organization: nested collections ("create as many folders and sub-folders you want"); drag-and-drop ordering; groups & sections; inserted texts; duplicate an item into several collections ("creates connections between these collections and improves the relevance of your interest graph").
- Privacy: "Collections are visible to everyone. This is what creates the social wealth of Pearltrees" — public by default; private collections are Premium; private teams Premium-only; share a private collection via generated key "that will give access... for one month" (view + comment, cannot pick up pearls).
- Social/discovery: "My interests" (recently updated collections around interests); "My Network" (activity of connections/followed collections); "Additions" (see where other members added your items/collections); "Related collections" (algorithmic, based on common elements — "interest graph"); search over collection titles/editorials/pearl titles; subscribe to collection updates; team-up (collaborative curation: all members add/organize; founder writes editorial, can freeze a member's rights, only founder creates subteams; history to recover deleted items; private messages among members).
- Publishing out: share via email/Facebook/Twitter/Reddit; embed a collection on a blog; permalink; auto-publish new items to Twitter/Facebook with pacing controls (vendor-specified cadence details in FAQ — L3).
- Premium tiers (vendor-stated): Personal $1.99/mo (10GB, privacy, offline, personalization), Advanced $3.99/mo (100GB, + edit collected web pages, archive web pages), Professional $9.99/mo (1TB, + white-label embeds, data protection); free default 1GB storage.
- Data ownership: export account in W3C-compliant RDF or HTML.
- Publisher opt-out: meta tag `<meta name="pearltrees" content="ignore">` prevents a site's content from being added.
- History: "tree-shape" visualization replaced by "dynamic grid" on May 23, 2014 (vendor-stated); visualization code open-sourced.
- Pearltrees AI: education-platform teaching assistant for teachers (LLM-based, 1,000 queries/month per teacher, teacher-only at v1.0, March 2025 update — vendor-stated); "not designed as a newsreader or monitoring tool."
- No public API ("Not yet").

### elink.io (evidence layer A — official product page)

- Self-description: "elink has everything you need to save bookmarks and build webpages, email newsletters, RSS website widgets, social bio links, social walls, automated content and more... by just adding web links."
- Explicit multi-function positioning (boundary-relevant): solutions nav lists Bookmark Manager, Email Newsletters, Web Pages, RSS Builder, Website Widget, Content Automation, Social Bio Links; "Content Curation: Bundle Links & Create Content — the fastest and most professional way to share curated content on any topic... Think of it as a professional Pinterest!" — with "Replaces: Get Revue, Scoop.it, Paper.li" logos.
- Bookmark manager module: browser extension, "save anything online as a visual bookmark. Organize your visual bookmarks with folders, tags and filters" — "Replaces: Pocket, Raindrop, Chrome Bookmarks."
- RSS feed reader module: "Follow an unlimited number of RSS feeds... Bundle articles directly from your RSS Feed Reader and build email newsletters and web content" — "Replaces: Feedly, Feeder."
- Content automation: "Generate automatic newsletters or website content from your selected sources."
- Publishing: hosted web pages or embed on any website; responsive HTML email newsletters "for any 3rd party email services"; website widgets; social bio links; Zapier integration ("1,000+ popular applications" — vendor claim); 50+ interchangeable templates, layouts updateable after publish ("Whenever you make a change, it's live and updates wherever you've sent it" — customer quote).
- Collaboration: "Invite your team to join you and collaborate together on content saving, research, bundling, creating and sharing content."
- Use cases: marketing, sales, PR (press clipping), research, management, remote teams, education, developers, politics, real estate, affiliate marketers, nonprofits.

### Flipboard (unreachable — market context only)

- Four fetch attempts failed (timeouts). No product claims drawn. Included in the sample plan as the consumer-social curation pole; the pole is instead evidenced structurally via Pearltrees (public collections, interest graph, following) and noted as a gap.

### Paper.li (market-drift observation)

- The paper.li domain now serves a German-language content blog; the original "digital newspaper" service is described on the domain itself in the past tense ("Paper.li war ein Online-Dienst..."), including its mechanics (algorithmic collection from Twitter/Facebook/RSS by keywords/hashtags/sources, automated scheduled publishing, limited per-item control). Treated as a market-drift observation, not as product documentation: fully automated curation products have largely exited the market; elink lists Paper.li among products it "replaces."

## Cross-product Comparison

| Dimension | Scoop.it | Curata CCS | Wakelet | Pearltrees | elink |
|---|---|---|---|---|---|
| Primary user | professionals, businesses, public sector, education | B2B content-marketing teams | educators, students, teams, individuals | consumers | marketers, PR, research teams, SMBs |
| Central managed artifact | topic page (private or public) | curated content stream + taxonomy categories | collection (visual) | collection (nested) | bundle/post → published outputs |
| Item types | articles + own uploads (PDF/image/video) | articles, videos, images | links, files, videos, images, text notes, PDFs | web pages, files, photos, notes | web links |
| Capture paths | suggestion engine, RSS sources, bookmarklet, upload | suggestion engine (NLP), browser plugin, team suggestions, social sourcing | browser extension, manual add | clipper, email-in, social import, favorites import, drag-drop | extension, RSS reader, manual add |
| Selection | human selects from engine suggestions | human reviews engine flow (assisted) | human saves | human saves | human saves or automation from sources |
| Enrichment | expert analysis + tags | summary in brand voice, contextualization, images | notes, cover images | notes, editorial, sections | title/description edits, images |
| Organization | topic pages + tags | auto-categorization to taxonomy, archive/index | collections + profile sections | nested collections + groups/sections | folders/tags + bundles |
| Staging area | — (implicit) | content flow queue | Unsorted items | dropzone | — |
| Collaboration | collaborative content hubs | team crowdsourcing/suggestions | collaborators; workspaces/groups/roles | teams (founder rights, freeze, history) | team collaboration |
| Audience surfaces | topic page, newsletter, social, embed/RSS/API, Teams/Slack, intranet | built-in site/blog, CMS, marketing automation, social, newsletters, feeds/API | link, public profile, PDF export | permalink, embed, social auto-post | hosted page, embed, newsletter via ESP, widgets, bio links |
| Discovery of others' collections | public topic pages | — | Explore page | interest graph, related collections, additions, follow | — |
| Privacy posture | private or public topic pages | (enterprise internal) | private or shared/published | public by default; private = paid | private or published |
| Measurement | engagement statistics, ROI | (marketing measurement posture) | org-wide analytics (workspace tier) | — | — |
| Governance | user rights/roles, SSO | enterprise posture | Super Admin/Admin/Editor, rostering integrations | founder controls in teams | team |
| AI | (era-current posture) | NLP self-learning engine | — | Pearltrees AI (education assistant) | content automation |

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

A Content Curation Platform is recognizable by exactly this structure:

```text
Captured content items (persistent discrete records,
  most commonly references to content that lives outside the platform)
  └── Curator's selective organization into persistent named collections
        (human choice + arrangement + added context)
        └── Audience-facing presentation of the collection
              (shareable/publishable surface beyond the curator)
```

Three properties. Remove any one and the Type collapses into a neighbor:

- Remove the curated collection as the managed artifact → the product becomes a feed reader or aggregator (streams, not collections).
- Remove human selection/organization (fully automated assembly) → the product becomes an aggregator (Paper.li-class; that pole has largely exited the market).
- Remove audience-facing presentation → the product becomes a personal bookmark manager.

Notes on the boundary of L0:

- "Third-party content" is the typical case (the curation act is about content that exists elsewhere), but own uploads/notes are common secondary item types (Scoop.it uploads, Wakelet text notes, Pearltrees notes) — so L0 says "most commonly references," not "exclusively references."
- Human selection is definitional; machine assistance (suggestions, auto-categorization, automation) is a common implementation layered on top. The collection remains a curated set, not an exhaustive automated stream.
- The audience can be as small as a team or as large as the public web; what matters is that presentation beyond the curator is a first-class product surface.

### L1 — Common Mature Structure (standard capabilities)

- Capture machinery: browser extension/clipper, bookmarklet, mobile share, email-in, favorites import (Pearltrees, Wakelet, elink, Curata, Scoop.it all ship at least one; the set varies).
- Item enrichment: auto-fetched title/thumbnail/description + curator's note/annotation + tags (all five).
- Collection design: layouts/templates, cover images, sections/groups, nested collections (Wakelet, Pearltrees, elink; Scoop.it topic pages; Curata taxonomy categories).
- Staging area between capture and organization: Wakelet "Unsorted", Pearltrees "dropzone" (two direct observations; treat as common pattern, not universal — Scoop.it/Curata evidence does not name one).
- Collaboration on collections: invite contributors, team curation, roles (all five in some form).
- Privacy control over collections: private vs public/shared (all five).
- Publishing/sharing outputs: permalink/share link, embed, social sharing, newsletter generation (all five; exact channel sets vary).
- Curator profile as public identity surface with organized public collections (Wakelet profile sections, Pearltrees account, Scoop.it public topic pages).
- Discovery of other people's collections (Pearltrees interest graph/related/follow; Wakelet Explore; Scoop.it public topic pages) — present in the consumer/community pole; absent in the B2B pole (Curata) where the audience is reached through distribution channels instead.

### L2 — Variant / Optional Structure

- Suggestion/discovery engine (source monitoring, keyword/Boolean queries, RSS source management, self-learning recommendations): B2B/professional pole (Curata, Scoop.it); elink has a lighter form (RSS reader + automation); absent in Wakelet/Pearltrees. NOT definitional.
- Distribution machinery depth: scheduled social posting, CMS/marketing-automation integrations, feeds/API (Curata, Scoop.it, elink) — marketing-pole variant.
- Measurement/analytics: engagement stats/ROI (Scoop.it), workspace analytics (Wakelet org tier) — segment variant.
- Organizational governance: workspaces with org→school→group hierarchy, role ladders, rostering integrations, SSO (Wakelet Education, Scoop.it business) — enterprise/education variant.
- Education-shaped use cases and templates (lesson plans, portfolios, class newsletters; student import) — segment variant.
- AI assistance: NLP curation engines (Curata), teaching-assistant AI (Pearltrees Education) — era-current variant.
- Freemium storage/plan tiers (Pearltrees 1GB free → paid tiers; Wakelet Starter/Pro/Education/Business/Enterprise) — business-model variant.
- Data ownership/export (Pearltrees RDF/HTML export) — posture variant.
- Publisher rights handling: opt-out meta tag (Pearltrees), author attributions in social sharing (Curata) — rights-posture variant.
- Visual organization metaphor (Pearltrees tree→grid history) — implementation variant.

### L3 — Vendor-specific (research notes only)

- Curata: "20 minutes a day" review claim; trending-topic SEO landing pages; royalty-free image suggestions; named CMS/MA integrations; "up to 25%" sourcing claim.
- Scoop.it: Meltwater ownership (help center domain), France hosting/GDPR statements, Teams/Slack integration, "8M users over 15 years" claim, Boolean search setup.
- Wakelet: Clever/ClassLink rostering; Super Admin/Admin/Editor role names; workspaces self-contained (no cross-workspace moves); ambassador program; plan names.
- Pearltrees: add@pearltrees.com email-in; #CollectionName Twitter routing; auto-publish cadence rules (5 items / every 10 additions — vendor-stated); private-collection one-month key; founder freeze rights; $1.99/$3.99/$9.99 tiers; 1GB default storage; 3.5MB collection-image limit; tree→grid change May 23, 2014; RDF export; pearltrees-ignore meta tag; Pearltrees AI 1,000 queries/month, teacher-only, March 2025.
- elink: "professional Pinterest" self-positioning; "replaces Pocket/Raindrop/Feedly/Scoop.it/Paper.li/Revue" competitive set; Zapier 1,000+ apps claim; 50+ templates; bio links/social walls modules.

## Vendor-specific Findings

See L3 above. Additionally: elink is the clearest demonstration that the market itself treats bookmark manager, feed reader, and curation as distinct solution categories that one product can span — it sells all three as separate solution pages. This is direct evidence for the boundary seams below.

## Boundary Findings

1. **vs Feed Reader (§02.08 sibling, unprocessed)** — sharpest intra-family seam. Reader's center: subscribe to sources, read streams (consumption loop; the stream is the artifact). Curation's center: the collection as the managed artifact (selection + organization + presentation). Evidence: elink ships "RSS Feed Reader" and "Content Curation" as separate solution pages in one product; Curata/Scoop.it treat source monitoring as input machinery, not the product's center. Removal test: remove the organized collection as deliverable → feed reader. Straddle risk: Feedly-class readers with team boards (sibling unprocessed — flag for joint review).
2. **vs Content Aggregator (§02.08 sibling, unprocessed)** — aggregator = automated comprehensive gathering into a unified stream/site; curation = selective human choice with the collection as deliverable. Evidence: Curata automates discovery but centers the human review/selection step; Paper.li (fully automated assembly) is defunct (domain repurposed) and is listed by elink as replaced. Removal test: remove human selection → aggregator. Flag for joint review when sibling is processed.
3. **vs Personalized Content Feed (§02.08 sibling, unprocessed)** — personalized feed = algorithmic per-user stream with no curator and no collection artifact; curation = explicit human selection into a shared collection. Structural only (sibling unprocessed); flag for joint review.
4. **vs Bookmark Manager (§02.13 sibling, unprocessed)** — bookmark manager = personal saving/retrieval (folders/tags serving the saver); curation = organization for an audience + publication surface. Evidence: elink sells "Bookmark Manager" and curation separately; Wakelet calls items "a modern take on bookmarks" yet centers collections + sharing + profile publication. Removal test: remove audience-facing presentation → bookmark manager. Flag for joint review.
5. **vs Read-it-later (§02.09 sibling, unprocessed)** — read-later centers the personal consumption queue; curation centers the durable organized collection as a deliverable. Structural only.
6. **vs Social Network (§01.05, unprocessed)** — curation platforms can carry profiles, following, and discovery (Pearltrees) but the primary object is the collection, not the person or the feed. Pinterest-class visual discovery is the known straddle; not sampled; flag recorded for the §01.05 pass.
7. **vs Content Publishing (CMS/Blogging §02.07) and marketing Types (§06)** — curation publishes collections of referenced items with added context; CMS/blogging authors owned content. B2B curation products overlap marketing distribution (newsletters, social scheduling); seam = the curated collection as the central managed artifact vs campaign/program management. Curata's own framing (curation software feeding marketing channels) supports the seam.
8. **Historical/market-sample check (§24)** — pre-platform link blogs/blogrolls and hand-maintained link roundups satisfy items + selection + audience presentation but lack the platform's managed collection objects and capture/publish machinery; they are the practice, not the product Type. Storify-class social curation (discontinued) and Symbaloo-class education tile boards (structural reasoning, not fetched) fit the L0. The definition does not depend on the modern B2B suggestion-engine pattern (Wakelet/Pearltrees lack it and are still clearly curation platforms), nor on any single surface metaphor (Pearltrees changed its visualization entirely and remained the same product).

## Uncertainties

- Flipboard (major consumer curation product) unreachable — the consumer-social pole rests on Pearltrees plus structural reasoning; no Flipboard claims made.
- Scoop.it help center unreachable — Scoop.it operational details (plan limits, exact mechanics) not verified; homepage/business-page evidence only.
- Curata application docs login-gated — Curata evidence is product-page level; no workflow internals claimed.
- Whether a staging area (Unsorted/dropzone) is universal: observed in 2 of 5 products; treated as common pattern, not standard requirement.
- Whether "audience-facing presentation" can degrade to team-only sharing and still count: yes in the sampled products (private team collections are a mode, not a different Type); the defining test is that presentation beyond the curator is a first-class surface, which all five products have.
- Pinterest-class visual discovery not sampled — boundary vs Social Network flagged, not resolved.
- Paper.li evidence comes from a repurposed domain — used only as a market-drift observation.

## Final Synthesis

A Content Curation Platform is a platform in which a curator captures discrete content items — most often references to content that lives elsewhere on the web — selectively organizes them into persistent, named collections enriched with the curator's own context, and presents those collections to an audience through shareable or publishable surfaces.

The defining core is small: captured items + curator's selective organization into persistent collections + audience-facing presentation. Everything else commonly seen — suggestion engines, RSS source monitoring, auto-categorization, analytics, org governance, education templates, AI assistance, freemium tiers — is standard or variant capability layered on that core, and the market's own product taxonomy (elink selling bookmark manager, RSS reader, and curation as separate solutions; Curata centering human review over automated discovery; the death of fully automated curation products) confirms that human selection into a presented collection is what makes the Type.

The Type sits in a family of stream/collection products (§02.08) and is separated from its siblings by two tests: what the managed artifact is (collection vs stream) and who does the selecting (a curator vs an algorithm vs nobody-in-particular). Its closest non-family neighbor is the Bookmark Manager, separated by the audience-facing presentation surface.
