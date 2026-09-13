# Research Notes — Online Forum

## Research Goal

Understand the Application Type "Online Forum" (DIRECTORY §01.06 Community & Discussion) from real products: what the defining structure of a forum venue is, how members / boards / topics work, how governance happens, and where the boundary lies with the sibling Types (Discussion Board, Community Platform, Q&A Community, Interest Community Platform) and adjacent Types (Community Chat, Social Network, Comment System, Blogging Platform).

This pass also discharges four incoming boundary flags from already-processed sibling leaves:

1. **discussion-board** — ALIAS-RISK: same market family; defensible line = discussion tool/surface (incl. embedded realizations) vs standing public community venue built from boards. Joint review recommended when online-forum is processed.
2. **community-platform** — ALIAS-RISK: Discourse self-describes as both; defensible line = standing public venue (boards/topics, typically open registration) vs operated container (managed membership + multiple surface families). Nesting: board ⊂ forum ⊂ community platform. Candidate outcomes: keep-both on venue-vs-container emphasis or documented overlap zone.
3. **interest-community-platform** — check the board-as-section-of-one-venue vs community-as-joinable-unit seam.
4. **community-chat-platform** — seam = live rooms under a container vs asynchronous content; flag if 01.06 processing encounters chat-centric community products.

## Initial Boundary

Working hypothesis at Understand step:

- Online Forum = a self-standing web venue where a community of members discusses topics organized in boards/forums/categories; threads persist; the venue has its own identity, member base, and moderation culture.
- Nearest neighbors: Discussion Board (tool/surface — possibly the same market family), Community Platform (operated container), Q&A Community (format), Community Chat Platform (live rooms), Social Network (feed/profile-organized), Blogging Platform (author-centered), Comment System (content-attached).
- Known unknowns: (1) can the venue be pinned down as the defining invariant without overfitting to the modern hosted-community implementation; (2) is the member base defining or merely common; (3) how the classic self-hosted pole differs structurally from the modern hosted pole.

## Research Questions

1. What is the venue structure — what does the software present as "the forum"?
2. What is the member model (registration, profiles, identity, standing)?
3. How do boards/categories/forums organize topics, and how do topics accumulate replies?
4. How does governance work (staff roles, moderation tools, rules, reputation)?
5. What access postures exist (open, invite-only, private spaces)?
6. How do the classic self-hosted and modern hosted poles differ?
7. What is standard equipment vs defining structure?
8. Where are the boundaries against Discussion Board, Community Platform, Q&A Community, Interest Community Platform, Community Chat?

## Representative Products

| Product | Pole | Why sampled |
|---|---|---|
| Discourse | modern open-source platform with commercial hosting | market leader; self-describes as both "community platform" and "forum software" — the straddler the community-platform pass flagged |
| XenForo | classic commercial self-hosted forum software (+ Cloud) | the classic-forum lineage still shipping; its own site runs on the product |
| Flarum | minimal open-source forum, extension-driven | the minimalist philosophy; successor of esoTalk and FluxBB |

phpBB (classic free OSS) was planned as a fourth sample but its userguide returned 403 (also unreachable in the discussion-board pass). Invision Community (hosted commercial suite) and ProBoards (free hosted classic) also unreachable. The classic-OSS pole is therefore evidenced indirectly (XenForo's classic lineage, Flarum's FluxBB/esoTalk succession) and structurally (prior-pass evidence recorded for XenForo's manual sections).

## Sources

Fetched 2026-09-08 (Tier 1 official):

- Discourse — https://www.discourse.org/about , https://www.discourse.org/features
- XenForo — https://xenforo.com/docs/xf2/manual/ (manual index + table of contents; section pages redirect to index from this environment)
- Flarum — https://docs.flarum.org/ (About page)

Unreachable (recorded as source-access limitation):

- phpBB userguide — https://www.phpbb.com/support/docs/en/3.3/ug/ → 403
- Invision Community features — https://invisioncommunity.com/features/ → 403
- ProBoards — https://www.proboards.com/ → JavaScript-only shell, no content

Reused prior-pass evidence (recorded observations from this repository's research files, fetched 2026-09-07):

- research/discussion-board.md — Discourse about/API, XenForo manual sections (forums/threads/posts, node structure, forum and thread types, questions), Flarum docs, Canvas LMS (embedded pole)
- research/community-platform.md — Discourse self-description straddle, Circle/Hivebrite (community-platform pole)
- research/interest-community-platform.md — Reddit/Meetup/Lemmy (multi-community venue pole)

## Product Observations

### Discourse

**Evidence layer: A (directly observed, official pages fetched 2026-09-08)**

Positioning: "the community platform that transforms conversation into a living, searchable resource"; mission says they deliver "the best community and forum software"; footer brand line "Discourse® and Discourse Forum™"; scale claims: 22k+ communities; customers are technology companies (OpenAI, Zoom, GitLab, Atlassian class). Open source (GPLv2) since 2013, self-host or official hosting; official API ("anything you see on screen, you can also do via an API call"), official plugins, Discourse Hub mobile apps.

Feature surface (features page):

- "Conversations, not pages" — flat forum, replies flow down the page, just-in-time loading instead of pagination; expandable context at post boundaries and inside quotes.
- "Simple, but with context" — self-description: "Discourse is a simple, flat forum".
- Chat channels as a side surface ("chat in real time"; "chat messages can be quoted in topics where the discussion can continue over time" — the product itself states topics are the durable/discussable place and chat the informal one).
- Trust system — "as members become trusted regulars over time, they earn abilities to help maintain their community"; community moderation (flagging, moderator flag queue); badges.
- Member machinery: profiles/preferences, avatars, 2FA, social login, SSO, email invitations, usergroups ("self-managing usergroups").
- Content machinery: Markdown/BBCode/HTML, file attachments, link auto-expansion, polls, post revision history, wiki posts (collaboratively edited), anonymous posting, spoilers, drafts.
- Communication: reply via email, mailing-list support, desktop notifications.
- Admin: admin dashboard (community-health metrics), sitewide alerts & pinned topics, invite-only mode, private spaces, post approval, inline & bulk moderation, SEO optimized for indexing.
- AI plugin: summarize topics, toxicity detection, compose assistance (era-current capability).

Interpretation: every defining candidate structure (venue of its own, boards/categories organizing topics, member base with standing, persistent searchable archive, moderation) is present and articulated by the vendor itself. The chat/Q&A/translation layers are explicitly additive.

### XenForo

**Evidence layer: A (manual index + TOC fetched 2026-09-08; section-level evidence from the discussion-board pass's 2026-09-07 fetch, recorded in research/discussion-board.md)**

Positioning: "Community platform by XenForo" (site-wide tagline). Products list: **Forum** (the core product), Media gallery, Resource manager, Enhanced search, Importers — a forum-first commercial product with optional add-ons; self-hosted purchase and XenForo Cloud subscription.

Manual structure (the vendor's own concept inventory):

- **"Forums, threads and posts"** — the content model as a first-class manual section.
- **Users** and **Access privileges** — member/staff machinery and permissions as first-class sections.
- **User-generated content**, **Communication**, **Configuration**, **Terms and rules**, **Importing content**, **Maintenance**.
- Admin Control Panel (ACP) — "separate from the public-facing side or *front-end* of XenForo that is accessible to regular visitors"; staff-only; re-login required. The distinction between a public visitor surface and a staff administration surface is built into the manual's first pages.
- **"Board active"** option ("Inactive board message") — the whole installation is treated as one board/venue that can be taken offline, evidencing the single-venue framing.
- From the prior pass: node tree (forums as nodes), thread/post model, forum and thread types including question threads, per-node permissions, polls, question-and-solution threads.

Interpretation: the classic pole's world is exactly venue → forums (nodes) → threads → posts, plus users and permissions. The "Terms and rules" manual section evidences venue-level rules as a standard concept.

### Flarum

**Evidence layer: A (docs About page fetched 2026-09-08)**

Positioning: "a delightfully simple discussion platform for your website"; "This is forum software for humans"; "all the features you need to run a successful community"; "thousands of Flarum sites out there, with millions of total end users". Goals: fast and simple (no clutter/bloat), beautiful and responsive, powerful and extensible (Extension API; customize/extend/integrate "to suit your community"), free and open (MIT). Lineage: combined successor of esoTalk and FluxBB (FluxBB = classic lightweight forum software; esoTalk = earlier minimal forum). Governance: volunteer foundation; community forum at discuss.flarum.org runs on the product. Management surface: Admin Dashboard, extensions, languages, theming, mail configuration.

Interpretation: the minimalist pole keeps the same world (a site runs a discussion venue for a community) and pushes everything else into extensions — evidence that the defining structure is small enough that a "delightfully simple" product can carry it.

### Cross-product notes

- All three vendors articulate the same job — run a standing community venue on the web — in their own words: "build communities that last" (Discourse), "Community platform by XenForo", "run a successful community" (Flarum).
- All three separate a staff/administration surface from the member front-end.
- All three are self-hostable open-source or commercial software whose deployment unit is **one venue/instance** (a site), not a multi-tenant host of many communities. (Contrast: Reddit/Meetup-class products are multi-community venues — that pole belongs to Interest Community Platform per that pass.)
- The classic lineage is explicit: Flarum succeeds FluxBB/esoTalk; XenForo continues the classic commercial forum line (vBulletin-descended team, per general market knowledge — not asserted from fetched evidence).
- Discourse's self-description straddles "community platform" and "forum software" — exactly the ALIAS-RISK the community-platform pass recorded.

## Cross-product Comparison

| Structure | Discourse | XenForo | Flarum | Layer |
|---|---|---|---|---|
| Deployment unit = one standing venue (a site) | yes ("22k+ communities", each an instance) | yes (per-installation ACP; "Board active") | yes ("for your website") | B |
| Board/category organization of topics | categories + tags | node tree (forums) | tags (extension-driven) | B |
| Member-opened topics with asynchronous replies accumulating persistently | topics + posts | threads + posts | discussions + posts | B |
| Standing member base with venue-level identity (profile, history) | profiles, avatars, badges, trust levels | Users manual section, member profiles | member accounts | B |
| Staff/admin surface separate from front-end | admin dashboard, flag queue | ACP vs front-end | Admin Dashboard | B |
| Moderation toolkit | flag queue, bulk moderation, post approval | moderation tools (per prior pass) | moderation via core/extensions | B |
| Reputation / recognition systems | trust levels, badges | (prior pass: member ranks/trust machinery) | extensions | B (uneven) |
| Search over the archive | yes | yes (Enhanced search add-on for advanced) | plugin | B |
| Notifications + email participation | reply via email, mailing-list support | Communication manual section | mail config, extensions | B |
| Private/personal messaging | personal messaging | yes | extension | B |
| Polls, rich posts, attachments | polls, Markdown/BBCode, attachments | polls, BBCode | extensions | B |
| Chat channels as side surface | yes (explicitly secondary to topics) | (not core in manual TOC) | extension | B (uneven) |
| Question/answer thread type available | (accepted-answer plugin per community-platform pass) | question threads (prior pass) | extension | B (uneven) |
| Q&A-as-primary-structure | no | no | no | B |
| Multi-surface suites (events, courses, monetization) as defining | no (plugins only) | add-ons (gallery/resources) but forum-first | no | B |
| Operator-as-organization container with managed membership | positioning serves orgs, but membership is venue signup | per-node permissions serve any operator | "for your website" | mixed — see boundary |

## Canonical Model (Four-Layer Abstraction)

### L0 — Defining Invariant

Three jointly-held structures; each removal test performed:

1. **A self-standing venue of its own** — the forum is a named, addressable place on the web with its own identity (site, URL, member base, rules), existing before and between conversations; the deployment unit of the software is one such venue. *Remove → a discussion tool embedded in a course/organization/product (Discussion Board territory) or a comment surface attached to content.*
2. **Board-organized topic discussion** — the venue's world is organized into boards/areas (forums/categories/tags), each holding member-opened topics that receive asynchronous replies over time, with topic+replies persisting as a readable thread and the archive remaining searchable/visible at the venue. *Remove the board organization → feed-organized social network; remove the async topic thread → live chat; remove persistence → ephemeral surface.*
3. **A standing member base with venue-level identity** — a persistent population of members who join the venue (registration/invitation) and carry identity, standing, and history across the whole venue; the community is the member population of the venue itself, not a course roster, an operator's customer list, or a platform account spanning many communities. *Remove → anonymous comment pool or embedded tool with no community; hand membership management to an operating organization's apparatus → community platform territory.*

Joint-held is load-bearing: 1 alone = a website; 2 alone = a discussion board tool; 3 alone = an account system; 1+3 without 2 = a social network without its feed is nothing — with a feed it *is* a social network; 2+3 without 1 = the discussion-board pole (embedded/course/group boards).

Historical check (§24): a classic self-hosted web forum of the 2000s (board index → forums → threads, member registration, ranks, moderator roles) satisfies all three with zero modern capability. A dial-up-era BBS (one system = one venue, message areas = boards, user accounts = members) satisfies conceptually. A Usenet newsgroup does **not** (no venue of its own, no member base of a venue) — correctly excluded as a discussion-surface ancestor. A mailing-list group does not (no venue, threads in inboxes). The definition therefore does not overfit the modern hosted-community era.

### L1 — Common Mature Structure

Very common in mature modern products, not definitional:

- member profiles with avatars and post history; user groups
- registration/authentication variety (email/password, social login, SSO, 2FA, invitations)
- topic lists ordered by latest activity/popularity with unread state and filters
- search across topics and posts
- notifications and subscriptions; email digests; reply-by-email
- moderation toolkit: staff roles (admin/moderator), flag queues, post approval, edit/move/merge/split/close/pin/lock, soft deletion preserving the record
- reputation/recognition: ranks, badges, trust systems that promote regulars into partial governance
- rich posts: formatting, attachments, images, quotes, reactions, post revision history
- private/personal messaging between members
- polls; wiki posts; anonymous posting modes
- admin control panel: site configuration, per-board permissions, appearance/theming, integrations, API
- SEO/indexing posture for the public archive

### L2 — Variant / Optional Structure

- hosting/deployment: self-hosted OSS vs vendor-hosted commercial vs vendor cloud
- access posture: open public vs invite-only vs members-only/private spaces within an open venue
- product shape: minimal core with extensions vs forum-first commercial suite with add-ons (media galleries, resource managers) vs modern platform with bundled chat/AI
- thread layout philosophy: classic paged/threaded trees vs modern flat scrolling with just-in-time loading
- question-and-solution thread types (Q&A capability inside the venue)
- chat channels as a bundled side surface
- mailing-list-style email participation
- AI assistance (summarization, toxicity detection, drafting)
- mobile apps / responsive-first design
- anonymous posting; spoilers; language/translation layers

### L3 — Vendor-specific Detail (research notes only)

- Discourse: trust-level ladder, "Civilized Discussion" branding, Discourse Hub apps, compare pages vs Circle/Discord/Reddit, "22k+ communities" figure, Ember/Rails/Postgres/Redis stack (irrelevant to the Type), GPLv2.
- XenForo: ACP at /admin.php, "Board active" option naming, XenForo Cloud, official add-ons (Media gallery, Resource manager, Enhanced search), node terminology, license-validation checks.
- Flarum: MIT license, Mithril front-end, esoTalk/FluxBB succession, Flarum Foundation governance, extension/bundled-extension mechanics.
- These names/limits are not asserted in the final document; no numeric limits were researched (and none are asserted).

## Vendor-specific Findings

- Discourse is the straddler: it markets itself as a community platform to organizations while self-identifying as forum software. Structurally its core remains the forum world (topics in categories, member base, moderation); organizational-seller features (SSO, private spaces, analytics, AI) are additive. This is the overlap zone with Community Platform (org-run forums), not a reason to collapse the Types.
- XenForo ships as a forum-first product with paid add-ons — evidence that "forum + optional surface add-ons" is a real market shape distinct from the multi-surface community suite.
- Flarum demonstrates the minimal-definition point: a product can strip to the core and still be recognized as forum software.

## Boundary Findings

1. **vs Discussion Board (§01.06, ALIAS-RISK — discharged).** The standalone market family is identical (Discourse/XenForo/Flarum class) — that is exactly why the leaves alias in everyday usage. The structural seam that survives research: **the Discussion Board is the discussion surface/tool** (topic+reply machinery), which exists embedded without any public venue — LMS course boards, organizational/group boards, boards inside other systems. **The Online Forum is the standing venue of its own** — a place with its own identity, member base, and governance, whose whole world is the venue. Every standalone forum product instantiates both (the venue runs on the tool), but the two Types answer different questions: "what is the discussion machinery" vs "what is the venue that stands on it". **Disposition: keep both** — Discussion Board defined by the surface core (prior pass), Online Forum defined by the venue invariant; the shared product family is recorded, and each document points at the other's pole. This discharges the discussion-board pass's joint-review flag.

2. **vs Community Platform (§01.06, ALIAS-RISK — discharged).** Seam = **venue vs operated container**. The forum's world is the venue itself (boards + members + discussion); nothing definitional requires an operating organization, managed-membership apparatus, or multi-surface families (events, courses, content, directories). The community platform's defining core is the operated container with managed membership and multiple participatory surfaces. Nesting observed: board ⊂ forum ⊂ community platform (a forum can be the discussion surface inside an operated container). Overlap zone: organizations running customer communities on forum software (two decades of practice; Discourse's current positioning lives here). **Disposition: keep both** — venue emphasis vs container emphasis; the overlap zone is documented in both documents.

3. **vs Interest Community Platform (§01.06 — seam checked as requested).** In a forum, boards are **sections of one venue** — they do not carry their own joinable membership, scope, or rules; the member joins the venue once. In an interest-community platform, the community unit itself is joinable and scoped, and the venue hosts many of them under one account. Checked against samples: XenForo nodes and Discourse categories/tags are venue-internal organization, not joinable communities. Seam holds.

4. **vs Q&A Community (§01.06, unprocessed).** Question-and-solution machinery exists inside forums as a thread type (documented for XenForo question threads and Discourse's accepted-answers plugin in prior passes) — format capability inside a venue-general Type. A product becomes a Q&A community when the question/answer/accepted-answer structure is the primary organizing principle of the whole venue. Note recorded for that leaf's pass (format-vs-container seam).

5. **vs Community Chat Platform (§01.01 — flag discharged from this side).** No chat-centric product in this sample; chat appears only as a bundled side surface, and Discourse's own feature copy states the direction of gravity (chat messages get "quoted in topics where the discussion can continue over time" — topics are the durable home). Async-topic venue vs live-room container seam holds.

6. **vs Social Network / Microblogging.** Content organization is topic/board-keyed with a standing member base of the venue, not author-keyed with a personal follow graph and feed. The forum has no personal broadcast feed as its spine.

7. **vs Comment System / Blogging Platform.** Comments attach to externally authored content items; a blog centers one author's publication. A forum is a standing venue where members themselves open the topics.

8. **Usenet newsgroups and mailing lists.** Structurally excluded: no venue of its own, no member base. They are discussion-surface ancestors (the discussion-board lineage), not forums. This is the historical-check outcome, not a value judgment.

## Uncertainties

- XenForo manual section pages could not be fetched from this environment (redirects to index); section-level claims for XenForo rest on the manual's TOC plus the discussion-board pass's 2026-09-07 fetch of those sections. Strength of XenForo-specific capability claims is accordingly reduced; no numeric limits asserted.
- phpBB, Invision Community, ProBoards unreachable — the classic-free-OSS and hosted-commercial-suite poles are evidenced indirectly (Flarum's FluxBB lineage; XenForo's classic line; prior-pass records). This does not affect the L0 determination, which was stable across all three fetched products and the prior-pass records.
- The exact prevalence of reputation machinery across the whole market is uneven (core in Discourse, extension-dependent in Flarum) — held as L1 common, not definitional.
- Whether the directory intends Discussion Board and Online Forum as distinct Types cannot be settled by products alone (same product family); the keep-both disposition with the tool-vs-venue seam is the defensible outcome recorded here and in both documents.

## Final Synthesis

An **Online Forum** is a self-standing web venue organized around boards and topics, with a standing member base whose discussion accumulates into a persistent, searchable archive under member-visible governance. The defining core is exactly three jointly-held structures — the venue of its own, board-organized persistent topic discussion, and the venue's own member population. Everything else modern products carry (profiles, ranks, moderation queues, search, notifications, email participation, chat channels, AI) is standard equipment or variant posture. The Type is distinct from the Discussion Board (tool vs venue), from the Community Platform (venue vs operated container), from the Interest Community Platform (sections vs joinable communities), and from chat/social Types (async topics vs live rooms / feed graphs). Keep-both dispositions for the two alias-risk flags are ratified by removal tests that hold in both directions.
