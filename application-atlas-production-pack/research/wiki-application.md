# Research Notes — Wiki Application

Research date: 2026-09-09
Leaf: Wiki Application (DIRECTORY §02.06 Wiki & Knowledge Base)
Slug: wiki-application

## Research Goal

Understand the **Wiki Application** as an Application Type from real products: what the wiki pattern itself contributes (as distinct from the "enterprise" layer already documented by the processed sibling leaf Enterprise Wiki), what the core object model is (page / link / revision / access), how users actually work in public, community, and personal wikis, which capabilities are common but not defining, and where the boundary lies — especially against the sibling leaves Enterprise Wiki, Knowledge Base Application, Help Center, and the neighbors Online Encyclopedia, CMS/website building, Collaborative Workspace, Collaborative Document Editor, Online Forum / Q&A Community, and Personal Knowledge Management.

This pass also carries two prior flags:

1. **enterprise-wiki (processed 2026-09-07)** — taxonomy note: "Enterprise Wiki is arguably an audience/deployment variant of Wiki Application rather than a fully distinct Type; the directory carries both leaves… JOINT REVIEW recommended when wiki-application is processed (candidate outcomes: keep-both with the org-scope seam, or variant presentation)." This pass is that joint review and must end in a verdict.
2. **knowledge-base-application (processed 2026-09-08)** — advance note for this pass: "the KB/wiki seam is organizing principle, not audience — relevant to that pass's variant-vs-type decision."

## Initial Boundary (hypothesis before research)

- A Wiki Application is the software realization of the **wiki pattern**: a corpus of interlinked pages that its users can edit directly, with every change recorded in restorable version history.
- The sibling pass (Enterprise Wiki) defined its own core as the wiki pattern **plus organization-scoped access** and explicitly stated: "Remove → the general (public/community/personal) Wiki Application." Working hypothesis: the general Wiki Application's defining core is the pattern **without** organizational scope; the scope/audience axis (public / community / group / personal / organizational) is the variant axis.
- Nearest neighbors: Enterprise Wiki (same pattern + org scope), Knowledge Base Application (curated/owned/review-managed vs emergent/member-maintained), Help Center (customer-facing published help), Online Encyclopedia (Wikipedia overlap seat), CMS/website builder (publisher-governed vs open editing), Collaborative Workspace (governed container vs emergent page graph), Collaborative Document Editor (document-shaped vs topic-shaped pages), Online Forum / Q&A Community (thread-centric vs page-corpus-centric), PKM / Note-taking (personal pole drift).
- Open questions going in: is version history definitional for the general wiki (the sibling made it definitional for the enterprise flavor)? Is "open editing" definitional when some wikis restrict editing to small groups? Is the hosted-farm pole (Fandom-class) separable from the engine pole?

## Research Questions

1. What is the smallest structure every wiki product carries? (pages, links, editing, history — which of these are invariant?)
2. How does the edit→save→revision loop actually work, and what surrounds it (preview, drafts, conflict handling, undo/rollback)?
3. How do pages get created — direct creation, and/or link-first creation (undefined links inviting creation)?
4. How is the corpus organized (groups/namespaces/structures/categories/folders) and discovered (search, recent changes, backlinks, orphans, listings)?
5. What access models exist (fully open/anonymous, password-based, user accounts + groups, per-page overrides, public/private mix)?
6. What maintenance machinery exists (rename with link update, lock, delete/recover, watches/notifications, spam/abuse controls, revision approval)?
7. What varies: storage substrate, markup/editor, packaging (engine vs suite vs farm), scale, multilingual?
8. Where is the boundary against Enterprise Wiki, Knowledge Base, Help Center, Online Encyclopedia, CMS, forums, and PKM?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different deployment tiers:

| Product | Pole | Why sampled |
|---|---|---|
| **MediaWiki** | the canonical open-source wiki engine; platform for Wikipedia and the other Wikimedia projects | the largest-scale public-wiki anchor; extension ecosystem |
| **PmWiki** | classic lightweight PHP wiki engine, flat-file, wiki-based-CMS self-description | rich official documentation reachable; the "collaborative authoring" philosophy pole |
| **Tiki Wiki CMS Groupware** | wiki at the core of a full CMS/groupware suite | the suite-embedding pole; unusually complete user-guide documentation |
| **Wiki.js** | modern Node.js wiki app, git-backed storage, module system | the modern-engine pole; official feature documentation |
| **DokuWiki** | file-based open-source wiki engine | observed at repository level only (official docs site unreachable) — kept as a named representative, no operational claims drawn |

Unreachable probes (abandoned per network rules, recorded as limitations): Fandom (hosted fan-wiki farm; www.fandom.com and community.fandom.com timeouts ×2–3), TiddlyWiki (personal single-file wiki; tiddlywiki.com oversized, GitHub README timeouts ×2), Wikipedia/Wikimedia (en.wikipedia.org timeouts ×2), WikiWikiWeb origin site (c2.com JS-required). The hosted-farm and personal poles are therefore evidenced indirectly (farm concept via PmWiki "wiki farms" and Tiki "MultiTiki"; personal pole via cross-reference to the processed PKM pass, which sampled TiddlyWiki at Tier-1).

## Sources

Tier 1 (official operational documentation, fetched 2026-09-09):

- PmWiki — home (PmWiki/PmWiki), Features of PmWiki (PmWiki/PmWikiFeatures), PmWikiPhilosophy, WikiWikiWeb (concept page) — https://www.pmwiki.org/wiki/
- Tiki Wiki CMS Groupware — Documentation home (doc.tiki.org/Documentation), Using Wiki Pages (doc.tiki.org/Using-Wiki-Pages), keywords index — https://doc.tiki.org/
- Wiki.js — official website feature pages — https://js.wiki/ ; official repository README — https://github.com/Requarks/wiki

Tier 2 (official product/repo positioning):

- MediaWiki — official repository README — https://raw.githubusercontent.com/wikimedia/mediawiki/master/README.md
- DokuWiki — official repository (description + README) — https://github.com/dokuwiki/dokuwiki

Unreachable (limitation recorded): mediawiki.org, dokuwiki.org, community.fandom.com, www.fandom.com, en.wikipedia.org, wiki.c2.com, tiddlywiki.com, doc.tiki.org (first attempt 503, succeeded on retry), miraheze.org (403).

## Product Observations

Evidence layers: **A** = directly observed in this product's official documentation; **B** = cross-product commonality; **C** = canonical inference.

### MediaWiki (official repo README — positioning level)

- "Free and open-source wiki software package written in PHP. It serves as the platform for Wikipedia and the other Wikimedia projects, used by hundreds of millions of people each month." [A]
- "Feature-rich and extensible, both on-wiki and with hundreds of extensions." [A]
- "Scalable and suitable for both small and large sites." [A]
- "Localised in over 350 languages." [A]
- GPL v2 or later. [A]
- No operational detail (edit loop, history, namespaces) was reachable this pass — mediawiki.org timed out twice. All MediaWiki-specific operational claims are withheld; MediaWiki is used as the scale/anchor and extension-ecosystem witness only. [limitation]

### PmWiki (official site — rich)

- Self-description: "PmWiki is a wiki-based content-management system (CMS) for collaborative creation and maintenance of websites." Pages "look and act like normal web pages, except they have an 'Edit' link that makes it easy to modify existing pages and add new pages into the website… You do not need to know or use any HTML or CSS." [A]
- Access posture: "Page editing can be left open to the public or restricted to small groups of authors." [A]
- Pattern definition (its WikiWikiWeb concept page): "an 'open-editing' system where the emphasis is on the authoring and collaboration of documents rather than the simple browsing or viewing of them"; "the basic concept… is that (almost) anyone can edit any page"; "many systems (including this one) have built-in mechanisms to restore content that has been defaced or destroyed"; "In the process of creating the link you're creating the new page, if it doesn't already exist" (via [[double square brackets]] or WikiWords); "It's not necessary to learn all of the formatting rules; others will often come in and reformat things for you. After all, anyone can edit!" [A]
- Philosophy: "At its heart, PmWiki is a collaborative authoring system for hyperlinked documents"; "Favor writers over readers"; "Support collaborative maintenance of public web pages"; security note that arbitrary HTML is riskier "when pages can be created anonymously" (anonymous creation is a recognized scenario). [A]
- Page history: "History pages include Restore links. Configurable number of days and number of revisions of history." Editing "handles simultaneous edits"; optional save-as-draft; button bar + preview. [A]
- Organization: wiki groups (one level, "handles menus and styling by groups"); categories ("organise and find related pages with special Category markup"); navigation trails (author-created sequences of pages); site map via pagelists. [A]
- Discovery: search "the entire site or the current group"; Recent Changes; backlinks ("available since version 2.0.beta33"); missing and orphan pages search (RefCount). [A]
- Access control: "password protection can be applied to an entire site, to groups of pages, or to individual pages… controls who can read pages, edit pages, and upload attachments"; user authentication "available as an option (AuthUser)" — i.e., the engine can run without a user-account system, on passwords alone. [A]
- Spam controls (for open wikis): "blocking words, IP addresses (option), and by limiting the quantity of non-approved URLs (option)." [A]
- Content machinery: uploads/attachments; include other pages (part or complete); anchors; forms embedded in wiki pages; new page templates; page renaming (addon); skins/theming; printable layout; RSS/Atom web feeds; email notification of revised pages (Notify). [A]
- Storage: "Flat files; no need for a database. Can handle thousands of pages." [A]
- Wiki farms: "To have multiple wikis with a single installation of the wiki engine." [A]
- Extension ecosystem: "nearly 400 recipes" (Cookbook). [A]
- Live surface observed on the docs site itself: per-page actions View / Edit / History / Print / Backlinks; Recent Changes; Search; WikiSandbox; per-page talk pages (e.g., "PmWiki:PmWiki-Talk"). [A]

### Tiki Wiki CMS Groupware (official docs — rich)

- Self-description: "Tiki Wiki CMS Groupware" — a suite whose documentation organizes around wiki pages plus CMS/groupware features (trackers, forums, blogs, articles, file galleries, calendars, surveys, quizzes, newsletters, polls, maps, spreadsheets, shopping cart, payment, karma/score, friendship network, BigBlueButton integration…). [A]
- Wiki pages: "Create new pages / Edit existing pages / Read pages / Add Comments to pages / Find Similar pages." [A]
- Page creation is link-first: WikiWord ("Smashed Word") syntax or ((page name)); "when the page is saved the Wiki will add a question mark to indicate a new page. The question mark is a link to the Wiki page editor for that page. After the new page is saved, the question mark is replaced… and the link will be indicated." [A]
- Recent changes ("Last Changes"): per change — time/date, page name, user (and IP address), edit description/comment; actions: page history, view version, **rollback** ("revert a page to the specified version… prompt you for confirmation"), side-by-side diff against current or any version, view source. [A]
- Page history framed as "Version control & Accountability." [A]
- List pages: name, hits (reads), last modified, last modifier, number of versions, number of wiki links and backlinks, language, category; actions: edit, copy, history, delete. [A]
- Orphan pages: "pages… that have no incoming or backlinks… On many occasions, Orphan pages are old pages that were removed from the Wiki and should have been deleted." [A]
- Page-level operations: edit, print, PDF, save-to-notepad, **watch** ("when a change is made to the page, an email is automatically sent to every user who is monitoring the page"), backlinks listing, **remove** ("A deleted page can be recovered by admin"), **rename** ("all wiki links referencing the page will be updated as well"), **lock/unlock** ("a page can be locked to prevent it from being edited"), **permissions** (per-page group permissions), history, similar, **undo** ("removes the current version of the page making the last version in the history the current page"), export, threaded comments, attach file. [A]
- Permissions model: "If no individual permissions are applied to a page, global permissions apply. As soon as one permission is applied, all global permissions are overridden." [A]
- Structures: "a way of applying an order to Wiki pages, like building a directory tree"; structures can be watched. [A]
- Sandbox: "a safe place to experiment… The contents of the Sandbox are never saved." [A]
- Watches: user watches, group watches, category watches, structure watches — email notification. [A]
- Abuse controls (keywords index): "Spam protection (Anti-bot CAPTCHA)", "Banning". [A]
- Quality workflow variant: "Revision approval, Flagged Revisions." [A]
- Multi-wiki hosting: "MultiTiki — Multiple Tikis on a Single Server." [A]
- Philosophy keyword: "WYSIWYCA — What You See Is What You Can Access" (permissions shape the visible UI). [A]
- Migration: "Tiki Importer — MediaWiki Importer." [A]

### Wiki.js (official website + repo README — rich)

- Self-description: "The most powerful and extensible open source Wiki software"; "A modern, lightweight and powerful wiki app built on NodeJS." [A]
- Visibility posture: "Make your wiki public, completely private or a mix of both." [A]
- History: "Version Tracking — All content modifications are tracked. You can revert to a previous state or recover a deleted page at any time. Easily keep track of who changed what." "Compare Versions — visually compare two versions of the same page." "Export / Branch off — export a specific version or create a new page from an older version." [A]
- Editors: Markdown (live preview, toolbar/shortcuts), Visual Builder ("WYSIWYG editor for non-technical people"), plain HTML; WikiText (MediaWiki migration) and others listed as coming. [A]
- Authentication: local (self-registration + password recovery), social (Google/Facebook/Microsoft/GitHub/Discord/Slack…), enterprise (LDAP, SAML, CAS, Auth0, Okta, Azure AD, generic OAuth2/OIDC), 2FA. [A]
- Authorization: users; groups ("assign users into groups to control what they can do or access"); granular permissions ("page editing, assets management and access to various parts of the administration area"); page rules ("exact path, start/end with and regex filters"). [A]
- Storage: git sync ("synchronize or backup your content to popular Git services"), cloud storage (S3/Azure Blob/GCS…), local/network; database choice (PostgreSQL/MySQL/MariaDB/MS SQL/SQLite); runs on Docker/K8s/Linux/macOS/Windows; self-hosted or one-click cloud marketplace. [A]
- Search: built-in engine ("zero setup"), or external (Algolia, Azure Search, Elasticsearch). [A]
- Media assets manager (folders, usage tracking); rendering (code highlighting, diagrams, math); localization (40+ languages, RTL, per-page multilingual content); theming (dark mode, custom CSS/JS injection); admin area ("manage all aspects of your wiki"). [A]
- Module posture: "Not all teams need the same set of features. That's why Wiki.js offers a wide range of modules that can be turned on/off on demand." [A]

### DokuWiki (official repo — thin)

- "The DokuWiki Open Source Wiki Engine" (repo description); README points to dokuwiki.org for all documentation (unreachable this pass); GPL; project years 2004–2026. [A — repo level only]
- No operational claims drawn. Kept as a named representative of the file-based engine pole. [limitation]

### Unreachable probes

- **Fandom** (hosted fan-community wiki farm): www.fandom.com/about timeout, www.fandom.com timeout, community.fandom.com/Help:Contents timeout ×2 — abandoned. The hosted-farm pole is evidenced only indirectly (PmWiki documents "wiki farms"; Tiki documents MultiTiki). No Fandom-specific claims are made anywhere.
- **TiddlyWiki** (personal single-file wiki): tiddlywiki.com oversized (>5MB single-file app), GitHub README timeouts ×2 — abandoned. The personal pole is handled via cross-reference to the processed PKM pass (which sampled TiddlyWiki at Tier-1 and classifies it by center of gravity as a personal knowledge web).
- **Wikipedia / Wikimedia projects**: en.wikipedia.org timeouts ×2 — abandoned. Wikipedia is used only as the widely known instantiation named by MediaWiki's own README ("serves as the platform for Wikipedia").
- **WikiWikiWeb origin (c2.com)**: JS-required shell only. The pattern's origin concept is instead documented via PmWiki's WikiWikiWeb concept page (which describes the original system and links to it).

## Cross-product Comparison

| Structure | MediaWiki | PmWiki | Tiki | Wiki.js |
|---|---|---|---|---|
| Interlinked page corpus | positioning-level (platform for Wikipedia) | A — hyperlinked documents, free links/WikiWords, backlinks | A — wiki links, backlinks, orphan detection | self-labeled wiki app; linking not detailed on fetched surface |
| Direct editing by users | positioning-level | A — "Edit" link; "(almost) anyone can edit any page"; open-to-public or restricted | A — create/edit pages; permission-gated | A — page-editing permissions; public/private/mix |
| Version history + restore | positioning-level | A — history pages with Restore links; simultaneous edits handled | A — History = "version control & accountability"; rollback w/ confirmation; undo; recoverable delete | A — all modifications tracked; revert; recover deleted page; compare versions |
| Recent-changes stream | — | A — RecentChanges | A — Last Changes with user+IP+comment | — |
| Corpus search | — | A — site or group search | A — search + list pages | A — built-in + external engines |
| Backlinks / orphans | — | A — backlinks action; missing/orphan search | A — backlinks; orphan pages | — |
| Link-first page creation | — | A — "creating the link you're creating the new page" | A — question-mark link to editor | — |
| Organization layer | — | A — groups (one level) | A — structures (ordered tree) | A — path-based page rules (permission side) |
| Categories/labels | — | A — categories | A — categories | — |
| Templates | — | A — new page templates | A — content templates | — |
| Attachments/media | — | A — uploads | A — attach file; file galleries | A — assets manager |
| Watch / notify | — | A — email notification (Notify) | A — page/structure/category/group watches | — |
| Access control | — | A — passwords page/group/site; user auth optional | A — groups; per-page perms override global | A — users/groups/granular perms/page rules; local+social+enterprise auth; 2FA |
| Spam/abuse controls | — | A — blocklist, URL approvals | A — CAPTCHA, banning | — |
| Rename (links updated) | — | addon | A | — |
| Lock page | — | — | A | — |
| Talk / comments | — | A — talk pages | A — threaded comments | — |
| Sandbox | — | A — WikiSandbox | A — never-saved sandbox | — |
| Export / print / feeds | — | A — print view, RSS/Atom | A — print, PDF, export, dump | A — page export / branch off |
| Extension ecosystem | A — "hundreds of extensions" | A — ~400 recipes | A — feature bundle + plugins | A — on/off modules |
| Multilingual | A — 350+ languages | A — i18n, UTF-8 | A — multilingual wiki | A — 40+ languages, per-page |
| Multi-wiki hosting (farm) | — | A — wiki farms | A — MultiTiki | — |
| Storage substrate | — | A — flat files, no DB | — (DB-backed; not detailed on fetched pages) | A — DB choice + git sync + cloud storage |
| Editor model | — | A — markup + button bar + preview | A — wiki syntax + WYSIWYG | A — Markdown / WYSIWYG / HTML |
| Suite breadth | — | — (pure wiki engine) | A — CMS/groupware suite | — (pure wiki + modules) |

Reading: the three rich samples agree on the pattern core (pages + links + direct editing + attributed restorable history) and on a wide common layer (recent changes, search, backlinks/orphans, link-first creation, organization layer, templates, attachments, watches, access control, sandbox, export/print). MediaWiki corroborates scale, extension ecosystem, and multilingual reach at positioning level. DokuWiki corroborates the engine-pole population without operational detail.

## Canonical Abstraction

### L0 — Defining Invariant

Three properties. If any one is removed, the product is no longer recognizable as a wiki:

1. **Interlinked page corpus** — the unit of knowledge is the page; pages reference each other through links; the corpus's structure is emergent, grown by contributors through links and light organization rather than fixed by a schema or a publication pipeline. (PmWiki: "collaborative authoring system for hyperlinked documents"; Tiki: backlinks/orphan machinery exists because links are the structure.) Remove → an editable website / document repository / blog.
2. **Direct editing by the product's users** — the wiki's own users (however its access model defines them) create and edit pages in place; the audience are the authors; there is no separate publication pipeline between writing and reading. (PmWiki: "Edit" link on every page, "(almost) anyone can edit any page", "editing can be left open to the public or restricted to small groups of authors"; Tiki: create/edit pages; Wiki.js: page-editing permissions.) Remove → published website / CMS / help center.
3. **Durable version history with restore** — every change is recorded (who/what/when), revisions are comparable and restorable, and deletion is recoverable; this is the safety mechanism that makes open editing viable. (PmWiki: "built-in mechanisms to restore content that has been defaced or destroyed", history pages with Restore links; Tiki: History = "Version control & Accountability", rollback/undo, recoverable delete; Wiki.js: "All content modifications are tracked… revert… recover a deleted page.") Remove → a shared notepad / reckless editable site.

Jointly-held load-bearing tests:

- 1 alone = editable website / document repository
- 2 without 1 = a page editor, no corpus
- 3 without 1+2 = version control / backup system
- 1+2 without 3 = open editing without safety = shared notepad
- 1+3 without 2 = versioned published documentation (CMS with history)
- 2+3 without 1 = editing tool with history, no corpus

Note on what L0 deliberately does NOT contain: no organizational scope (that is the Enterprise Wiki sibling's addition), no user-account system (PmWiki runs on passwords with user auth optional; the canonical pattern description centers on open editing, not accounts), no specific markup (Wiki.js ships Markdown/WYSIWYG/HTML), no database (PmWiki is flat-file), no specific scale, no cloud delivery, no specific access breadth (open-to-the-world vs restricted-to-a-group are both documented postures).

### L1 — Common Mature Structure

Present across the rich samples; expected in practice, not definitional:

- recent-changes stream with attribution (PmWiki, Tiki)
- corpus search (PmWiki, Tiki, Wiki.js)
- backlinks + orphan-page detection (PmWiki, Tiki)
- link-first page creation — undefined links render as invitations to create (PmWiki, Tiki)
- organization layer over the flat corpus — groups / structures / path trees (implementations vary; PmWiki groups, Tiki structures)
- categories/labels (PmWiki, Tiki)
- templates for new pages (PmWiki, Tiki)
- attachments / media (PmWiki, Tiki, Wiki.js)
- watch/notification of changes (PmWiki, Tiki)
- user accounts + access control with page/group/site granularity (PmWiki passwords, Tiki groups+per-page, Wiki.js groups+page rules)
- sandbox for safe experimentation (PmWiki, Tiki)
- talk pages / comments attached to pages (PmWiki, Tiki)
- rename with link updating, page lock, recoverable deletion (Tiki; rename as addon in PmWiki)
- export / print / syndication feeds (PmWiki, Tiki, Wiki.js)
- extension/plugin/module ecosystem (MediaWiki, PmWiki, Tiki, Wiki.js)
- theming/skins (PmWiki, Tiki, Wiki.js)
- multilingual support (MediaWiki, PmWiki, Tiki, Wiki.js)
- spam/abuse controls for open wikis (PmWiki blocklist/URL approvals, Tiki CAPTCHA/banning)
- edit-conflict handling (PmWiki "handles simultaneous edits")
- optional drafts (PmWiki save-as-draft)

### L2 — Variant / Optional Structure

- **Corpus scope/audience** — the axis that generates the market's shapes: public reference wikis, community/fan wikis, group/team/project wikis, personal wikis, and the organization-scoped realization documented as the sibling leaf Enterprise Wiki.
- **Identity model** — anonymous editing permitted (PmWiki recognizes anonymous creation; the canonical pattern description does not center on accounts), self-registration (Wiki.js local auth), enterprise identity (Wiki.js LDAP/SAML/OIDC), password-only protection without accounts (PmWiki).
- **Access breadth** — fully open, public-read/restricted-write, fully private, mixed (Wiki.js "public, completely private or a mix of both"; PmWiki "open to the public or restricted to small groups").
- **Storage substrate** — flat files (PmWiki), database (Wiki.js DB choices), git-backed (Wiki.js git storage).
- **Content format** — wiki markup (PmWiki, Tiki), Markdown (Wiki.js), WYSIWYG (Wiki.js Visual Builder, Tiki WYSIWYG), HTML (Wiki.js).
- **Packaging** — pure wiki engine (PmWiki, Wiki.js, DokuWiki, MediaWiki), wiki-at-the-core suite (Tiki), wiki farm / multi-wiki hosting (PmWiki wiki farms, Tiki MultiTiki), hosted community platform (Fandom-class — not directly evidenced this pass).
- **Quality workflows** — revision approval / flagged revisions (Tiki) for quality-controlled public wikis.
- **Structured data in pages** — forms embedded in pages (PmWiki), trackers (Tiki) — the "application wiki" drift toward lightweight app-building.
- **Suite embedding** — wiki as one feature of a broader collaboration platform (the enterprise-wiki pass documented this pole for the org flavor).

### L3 — Vendor-specific Structure (research notes only)

- PmWiki: password-based protection model where user accounts are optional (AuthUser); flat-file storage; "recipes" ecosystem; wiki-farm concept; navigation trails.
- Tiki: WYSIWYCA philosophy; MultiTiki; trackers/karma/notepad/mail-in; MediaWiki importer; flagged revisions.
- Wiki.js: git storage sync; regex page rules; pluggable search engines; admin area; 2FA; module on/off architecture.
- MediaWiki: Wikimedia-platform role; 350+ languages; hundreds of extensions.

## Vendor-specific Findings

See L3. None of these enter the canonical core. The most instructive: PmWiki's accountless password model proves the user-account system is not definitional; Tiki's suite breadth proves the wiki core survives embedding in a much larger product; Wiki.js's git storage proves the storage substrate is not definitional.

## Rejected Findings (anti-overfit)

- **"Wiki = Wikipedia-like encyclopedia"** — REJECTED. The encyclopedia is a content genre hosted on wikis; sampled engines host non-encyclopedic corpora (documentation, community guides, personal notes). MediaWiki's README itself frames MediaWiki as software "for Wikipedia and… third-party users", i.e., engine ≠ encyclopedia.
- **"Wiki = wiki markup"** — REJECTED. Wiki.js ships Markdown, WYSIWYG, and HTML editors; Tiki ships wiki syntax and WYSIWYG. Markup is implementation.
- **"Wiki = open-to-the-world anonymous editing"** — REJECTED. PmWiki explicitly supports "restricted to small groups of authors"; Wiki.js supports fully private wikis. Access breadth is a variant; the invariant is that the product's users edit directly.
- **"Wiki = user-account system"** — REJECTED. PmWiki's protection is password-based with user authentication optional; the canonical pattern description (open editing) does not center on accounts.
- **"Wiki = database-backed web application"** — REJECTED. PmWiki stores flat files with no database.
- **"Wiki = self-hosted engine"** — REJECTED. PmWiki documents wiki farms (many wikis per installation) and Tiki documents MultiTiki; hosted platforms exist (not directly evidenced this pass — held weak).
- **"Wiki = free/open-source"** — REJECTED as definitional. All four evidenced samples are open-source, but the commercial wiki-pattern market is documented by the sibling enterprise-wiki pass (Confluence, Slite, Nuclino); openness is a property of this sample's shape, not of the Type.

## Historical / Market-Sample Check

- **Origin generation (WikiWikiWeb, 1995)** — evidenced via PmWiki's concept page: open editing, "(almost) anyone can edit any page", restore mechanisms for defaced content, recent changes, link-creates-page. Satisfies all three L0 properties with zero modern machinery (no accounts, no WYSIWYG, no cloud, no analytics). The L0 holds.
- **Classic 2000s self-hosted markup wikis (PmWiki, Tiki generation)** — satisfy the core with flat files, markup editing, password/group protection.
- **Modern engines (Wiki.js)** — satisfy the core with Markdown/WYSIWYG, git storage, module system.
- **Personal single-user wikis** — satisfy the core with the editor population = one person; not directly evidenced this pass (TiddlyWiki unreachable). Cross-reference: the processed PKM pass sampled TiddlyWiki at Tier-1 and classifies single-file personal web notebooks by center of gravity inside Personal Knowledge Management (link-network-as-the-point). Consequence: the personal pole of the wiki pattern overlaps PKM territory; the wiki Type's center is the (potentially multi-user) collaborative corpus. Held as a boundary note, not a core change.
- **Organizational wikis** — the sibling leaf; satisfy the core plus org scope.
- Conclusion: the definition survives the historical check; nothing era-specific (cloud, WYSIWYG, AI, accounts, databases) is in the core.

## Boundary Findings

1. **vs Enterprise Wiki (§02.06 sibling, processed — the flagged joint review, DISCHARGED from this side).** The wiki pattern (L0 items 1–3) is shared. The enterprise leaf's L0 item 4 — organization-scoped access (entry through organizational identity, layered site→container→page governance, internal audience) — is a real structural addition that changes users, rules, and deployment; it is not merely a label. **Verdict: keep-both RATIFIED.** The general Wiki Application's defining core deliberately excludes organizational scope; scope/audience (public / community / group / personal / organizational) is this Type's variant axis, and the organizational realization is documented as the sibling leaf. This matches the sibling's own framing ("Remove → the general (public/community/personal) Wiki Application") and its request that the joint review choose between keep-both and variant presentation. Both documents cross-reference each other. No directory change.
2. **vs Knowledge Base Application (§02.06 sibling, processed).** Adopting the KB pass's ratified seam: the discriminator is the **organizing principle**, not the audience — KB = curated, owned, review-managed answer corpus (readers react but never edit the record copy); wiki = emergent interlinked page corpus maintained by open direct editing. Market language blurs (products self-label "knowledge base"); the organizing principles differ. Echoed in the final document's Related Types.
3. **vs Help Center (§02.06 sibling, processed).** Help Center = customer-facing published support publication (reader-facing site is the center); wiki = user-authored corpus (the audience are the authors). A public documentation wiki is wiki machinery; a published help site is help-center machinery.
4. **vs Online Encyclopedia (§02.05, unprocessed).** Wikipedia is both the archetypal wiki and the archetypal online encyclopedia — the overlap seat. Distinction: Online Encyclopedia = a reader-facing reference product defined by its encyclopedic content corpus; Wiki Application = an authoring/collaboration system defined by the wiki pattern, indifferent to content genre (encyclopedic, fan, documentation, personal). MediaWiki is the wiki application; Wikipedia is an online encyclopedia built on one. Advance note recorded for the encyclopedia pass.
5. **vs CMS / Website Builder (§02.07 / §04.16).** A CMS publishes a designed site through a publisher-governed pipeline; a wiki's users edit the corpus directly. PmWiki self-describes as a "wiki-based CMS" — the label straddles, the editing model decides. Tiki bundles full CMS features around its wiki core while the wiki pattern remains the center of its page machinery.
6. **vs Collaborative Workspace (§03.12, processed — flag already discharged by the enterprise-wiki pass).** Boundary held on organizing principle: emergent interlinked topic-page graph with open editing vs governed container holding heterogeneous content (docs, data, files) under membership. Confluence's straddle (wiki heritage, workspace positioning) is documented by the sibling pass.
7. **vs Collaborative Document Editor (§03.01, processed).** Document-shaped freeform long-form composition vs topic-shaped, interlinked, continuously maintained pages (echoing the enterprise-wiki pass's row).
8. **vs Online Forum / Q&A Community (§01.06, processed).** Thread-centric discussion records vs page-corpus knowledge records. Comments/talk attached to pages (PmWiki talk pages, Tiki threaded comments) are an adjacent capability, not a Type change; Tiki bundles full forums beside its wiki without the wiki becoming a forum.
9. **vs Personal Knowledge Management / Note-taking (§03.02, processed).** The personal pole of the wiki pattern (single-user wiki) drifts toward PKM/note-taking; the PKM pass holds TiddlyWiki-class products by center of gravity (personal link-network-as-the-point). The wiki Type's center is the collaborative corpus; a single-user wiki is the degenerate case on the scope axis.
10. **vs Blogging Platform (§02.07, processed).** Reverse-chronological post stream vs topic-shaped maintained pages. PmWiki and Tiki both ship blogs as addons/features beside the wiki — adjacent, not identical.

## Uncertainties

1. **Hosted-farm pole (Fandom-class) unsampled** — all Fandom surfaces unreachable. The farm concept is documented (PmWiki wiki farms, Tiki MultiTiki), but consumer farm-platform specifics (onboarding, contributor tiers, content policies) are not evidenced. The final document makes no farm-specific operational claims.
2. **Personal pole not directly evidenced** — TiddlyWiki unreachable; handled via cross-reference to the PKM pass's Tier-1 sample. The personal-wiki variant is written conservatively in the final document.
3. **MediaWiki operational detail withheld** — mediawiki.org unreachable; MediaWiki enters the research at positioning level only (official README). No MediaWiki-specific workflow claims (namespaces, talk-page mechanics, watchlist behavior) are made.
4. **Wiki.js interlinking surface** — the fetched feature page does not explicitly document page-to-page linking (it is a wiki app, and its editors/markup imply it), so interlinking for Wiki.js is held at self-label strength rather than claimed as observed mechanics.
5. **Edit-conflict mechanics** — PmWiki documents that it "handles simultaneous edits" but the mechanism's detail page was not fetched; the final document states the capability without mechanism detail.
6. **Anonymous-editing prevalence** — PmWiki's philosophy page references anonymous page creation as a recognized scenario; how common anonymous editing is across the current market is not quantified this pass.

## Final Synthesis

The Wiki Application is the software realization of the wiki pattern: **a corpus of interlinked pages that its users edit directly, with every change recorded in durable, restorable version history.** Three properties are jointly definitional (interlinked emergent corpus; direct user editing — the audience are the authors; attributed restorable history — the safety mechanism that makes open editing viable). Everything else commonly associated with wikis — accounts, groups, recent changes, search, backlinks, templates, attachments, watches, spam controls, markup dialects, storage substrates, farms, suites — is common mature structure or variant, not definition.

The Type's market realizes one pattern across a scope axis: public reference wikis, community/fan wikis, group/team wikis, personal wikis, and — as a separately documented sibling leaf — the organization-scoped Enterprise Wiki. The joint review with the enterprise-wiki pass is discharged as **keep-both**: the org-scope layer is a real structural addition (organizational identity, layered governance, internal audience), while the general leaf holds the pattern itself without that scope.

The sharpest adjacent seams: Knowledge Base Application (curated owned review-managed answers vs emergent member-maintained corpus — organizing principle, not audience), Help Center (published support publication vs user-authored corpus), Online Encyclopedia (content genre vs software pattern; Wikipedia the overlap seat), CMS/website builder (publisher-governed vs open editing), forums/Q&A (threads vs pages), PKM (personal link-network vs collaborative corpus).
