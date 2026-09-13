# Research Notes — Blogging Platform

## Research Goal

Understand what a Blogging Platform actually is as an Application Type: its core object model, the post lifecycle, how the reading surface is organized, how distribution/subscription works, and where it ends relative to CMS, microblogging, newsletter publishing, and website builders.

## Initial Boundary

- Candidate definition: software that lets an author publish dated articles (posts) to a persistent, author-owned web publication (the blog), presented newest-first.
- Nearest directory neighbors: Content Management System / CMS, Headless CMS, Product Documentation Portal (same family 02.07 Content Publishing); Microblogging Platform (01.05); newsletter-first publishing products (adjacent market, not a clean directory neighbor).
- Known straddler: WordPress is simultaneously the canonical blogging platform and the dominant CMS. The boundary must be drawn on the primary object model (post stream vs arbitrary content structure), not on the product name.
- Potential confusion: a blog post and a social feed post share "dated, reverse-chronological" surface traits. The distinguishing candidate is the author-owned publication container.

## Research Questions

1. What is the core object model? (post, page, draft, taxonomy, comment, theme, author)
2. What is the post lifecycle? (draft → publish → edit after publication; scheduling; revisions)
3. How is the reading surface organized? (stream, archives, permalinks, pages)
4. How does distribution work? (feeds, email, network discovery, social sharing)
5. What reader interaction exists? (comments, reactions, subscriptions)
6. How do hosted multi-tenant vs self-hosted software differ as deployment variants?
7. Where exactly is the boundary with CMS / microblogging / newsletter platforms / website builders?
8. Which capabilities are common-but-not-defining (themes, SEO, analytics, monetization)?

## Representative Products

| Product | Philosophy | Customer tier | Evidence quality |
|---|---|---|---|
| WordPress (WordPress.com hosted; WordPress.org self-hosted) | full-featured publishing + extensibility (blocks, themes, plugins) | consumer → enterprise (VIP) | Strong (Tier 1 support docs fetched) |
| Ghost | minimal professional publishing; open source; memberships/newsletters native | professional creators/teams | Strong (Tier 1 docs fetched) |
| Medium | hosted network-centric writing platform | consumer writers | Degraded (official sources unreachable) |
| Blogger | free consumer hosted platform, platform-account identity | consumer | Degraded (official sources unreachable) |
| Substack | newsletter-first publishing with web archive | professional writers | Degraded (official sources unreachable) |

Selection rationale: market representation (WordPress dominant; Medium/Blogger/Substack well-known), different product philosophies (extensibility vs minimalism vs network vs free-consumer vs email-first), different customer tiers, and coverage of the hosted-vs-self-hosted split.

## Sources

Fetched successfully (research date 2026-09-06):

- WordPress.com Support — "Create a post" — https://wordpress.com/support/posts/
- WordPress.com Support — "Create a page" — https://wordpress.com/support/pages/
- WordPress.com Support — "Enable or disable comments" — https://wordpress.com/support/comments/
- Ghost Documentation index — https://docs.ghost.org/llms.txt
- Ghost Documentation — "Publishing" — https://docs.ghost.org/publishing.md

Unreachable after repeated attempts (recorded as source-access limitation):

- Medium Help Center (https://help.medium.com/) — timed out ×2
- Medium product page (https://medium.com/creators) — timed out
- Blogger Help (https://support.google.com/blogger/) — timed out ×2
- Blogger product page (https://www.blogger.com/about/) — timed out
- Substack Support (https://support.substack.com/) — timed out ×2
- WordPress.org documentation article slugs attempted — 404 ×2

Consequence: all claims about Medium, Blogger, and Substack are held at positioning level only; no precise operational details are asserted for them. Cross-product commonality claims below rest primarily on WordPress + Ghost direct evidence, with historical/positioning knowledge used only for the historical-sample check, not for precise claims.

## Product A — WordPress (WordPress.com)

### Key observations (evidence layer A — directly observed)

- "Posts are individual pieces of content on a blog. Often referred to as blog posts or blogs, each post makes up the whole of your blog." Posts are the stream content; the blog is composed of posts.
- Editor: title field + block-based content editor; featured image, excerpt, and other post settings; preview on desktop/mobile/tablet; save draft; revisions restore.
- Publish flow: create → (optional settings) → Publish with pre-publish checks → after publication the button reads "Save" (i.e., published posts are edited in place and re-saved).
- Publishing a post triggers: appears as the newest entry on the blog page; appears in Reader feeds (unless site private); subscribers receive an email notification (unless turned off); auto-share to connected social profiles if configured.
- Scheduling exists ("publish or schedule the post" in the course description of the same guide).
- Post/page distinction: "A website uses pages to display content – Home, About, and Contact are common examples of pages." Pages are added to menus or set as homepage; they are not part of the post stream. Posts flow into the blog page and feeds.
- Display machinery: theme may include an Index template (all posts) and Archive template (posts by category, tag, month, year); a "default post page" that automatically updates with posts; Blog Posts block / Query Loop block to place posts on any page; display posts by category.
- Taxonomy: categories and tags are separate guides ("Organize posts with categories", "Organize posts with tags"); post formats exist; post order can be changed (chronological order guide exists — so newest-first is default, not forced).
- Comments: site-wide default setting ("Allow people to submit comments on new posts") plus per-post Open/Closed toggle; pingbacks; moderation options (require login, approve before public, required fields); spam protection; comment management surface (view, reply, delete, spam).
- Distribution/audience: Reader feeds; email notification to subscribers; social auto-sharing; likes and sharing buttons; SEO tools (plan-gated); shortlinks; social previews.
- Platform posture: WordPress.com positions itself across website builder, ecommerce, blog, newsletter, hosting — the blog is one publishing mode of a broader platform. AI authoring (WordPress Agent, external AI agents via MCP) is a 2026-era addition.
- Identity/tenancy: user account creates one or more sites; each site is an independent publication with its own address (subdomain or custom domain on eligible plans).

## Product B — Ghost

### Key observations (evidence layer A — directly observed)

- Positioning: "Ghost is an open source, professional publishing platform built on a modern Node.js technology stack — designed for teams who need power, flexibility and performance." Deployment: Ghost(Pro) hosted or self-hosted (Ubuntu/Docker/local); MIT-licensed open source.
- "Posts are the primary entry-type within Ghost, and generally represent the majority of stored data."
- "By default Ghost will return a reverse chronological feed of posts in the traditional format of a blog. However, a great deal of customisation is available for this behaviour."
- Post fields: title, description/excerpt, slug, metadata (meta title/description, OG/Twitter cards, canonical URL), authors, tags, feature image, published_at, visibility, access (membership gating), reading time, code injection.
- Editor: Medium-like writing experience; plaintext with formatting, Markdown conversion as you type; rich media "Cards"; standardized JSON document storage (Lexical) rendered per delivery destination.
- Pages: "a subset of posts which are excluded from all feeds… static and generally independent content like an About or Contact page… only ever published on the slug given to them, and do not automatically appear anywhere on your site."
- Tags: "the primary taxonomy within Ghost"; tag archives auto-generated at /tag/{slug}/ with pagination and RSS; primary_tag concept; internal tags prefixed with # are not rendered publicly (used to drive design/automation).
- Authors: "a subset of users who have published posts associated with them"; staff users have varying permission levels in the admin area.
- Admin API supports: creating/updating/publishing/scheduling posts, email-only posts, sending a post via email, tiers, newsletters, members, offers, webhooks.
- Members/tiers/newsletters: "launch a membership business from any Ghost publication, with member signup, paid subscriptions and email newsletters built-in"; tiers connect to Stripe; visibility/access fields gate content per tier.
- Themes: Handlebars template layer with contexts (index, post, page, author, tag, error); routing system maps URL patterns to data/templates, customizable; native search; prev/next post navigation; reading time.
- Content API: read-only REST API delivering published content to any client (headless/JAMstack usage is a first-class mode).

## Product C — Medium (degraded evidence)

- Official help center and product pages unreachable during research. Positioning-level knowledge only: hosted writing platform where individual stories are published under user profiles and "publications"; discovery happens through the platform's own network/feeds rather than the author's independent site. No precise operational claims are made. Treated as the network-centric hosted variant.

## Product D — Blogger (degraded evidence)

- Official help unreachable during research. Positioning-level knowledge only: one of the oldest free hosted blogging platforms (late 1990s origin), blogspot.com subdomain addresses, platform-account (Google) identity, template/gadget customization. Used mainly as the historical/older-market sample for the historical check. No precise operational claims.

## Product E — Substack (degraded evidence)

- Official support unreachable during research. Positioning-level knowledge only: email-newsletter-first publishing product where posts also form a web archive; paid subscriptions are central. Used in the boundary discussion (newsletter-first vs web-publication-first). No precise operational claims.

## Cross-product Comparison

| Dimension | WordPress | Ghost | Observation strength |
|---|---|---|---|
| Post as primary entry type | yes ("each post makes up the whole of your blog") | yes ("posts are the primary entry-type") | A×2 → strong |
| Dated stream, newest-first default | yes (newest entry on blog page; order changeable) | yes ("reverse chronological feed… traditional format of a blog"; customizable) | A×2 → strong |
| Per-post permalink/slug | yes (post ID, shortlink, permalink settings) | yes (slug + url in post object) | A×2 → strong |
| Edit after publication | yes (published post → "Save") | yes (updating posts via Admin API; editor) | A×2 → strong |
| Draft → publish lifecycle | yes (draft, preview, pre-publish checks, schedule) | yes (draft/schedule/publish via Admin API) | A×2 → strong |
| Static pages outside the stream | yes (Home/About/Contact; menus; homepage) | yes ("excluded from all feeds") | A×2 → strong |
| Taxonomy → archives | categories + tags; archive templates by category/tag/month/year | tags primary; auto tag archives with RSS | A×2 → strong |
| Comments with moderation | yes (per-post toggle, approval, spam) | native comments helper exists ({{comments}}); moderation depth not fetched | A×1 + partial |
| Themes/appearance layer | themes (classic + block) | Handlebars themes + custom settings | A×2 → strong |
| Feed/subscription distribution | Reader feeds + email to subscribers + RSS heritage | RSS per collection/tag; email newsletters | A×2 → strong |
| Email newsletter delivery | yes (newsletter options on posts) | yes (built-in newsletters, email-only posts) | A×2 → strong |
| Membership/paid content | paid subscriptions feature exists | members/tiers/offers native, Stripe-connected | A×2 → strong |
| Multi-author with roles | user roles on WordPress sites | staff roles (varying permissions) | A×2 → strong |
| Extensibility | plugins/blocks/patterns ecosystem | apps/integrations, Content/Admin API, custom routing | A×2 → strong |
| Hosted vs self-hosted | WordPress.com hosted ↔ WordPress.org self-hosted software | Ghost(Pro) ↔ self-hosted open source | A×2 → strong |
| Network discovery layer | WordPress.com Reader (opt-in feeds of other blogs) | none (independent publication posture) | A×1 → product-specific |
| AI authoring assistance | WordPress Agent, external AI agents | not observed in fetched docs | A×1 → product-specific |
| Headless/API-first usage | possible (REST API) but not the primary posture | first-class (Content API, JAMstack guides) | A×2, different emphasis |

## Canonical Model

### L0 — Defining Invariant

```text
Author-owned Publication (the blog: stable identity + own address)
└── Post (authored, dated, self-contained article — the unit of publication)
    └── Dated stream (posts presented as an ongoing archive ordered by publication time, newest-first by default)
        └── Per-post addressability (each post has its own stable URL)
```

Four properties. Remove any one and the Type stops being recognizable:

- **Author-owned publication** — a persistent, titled, addressable publication owned by an identified author (or small team). Without it, content dissolves into an anonymous feed or a platform-owned network surface.
- **Post as unit of publication** — a self-contained authored article (long-form text with media), published as a discrete dated entry. Without it, the product is a microblog (short status updates) or a page-based website.
- **Dated stream** — the publication's organizing principle is publication time: posts accumulate as an ongoing, browsable archive (newest-first by default; some products allow reordering, so direction is default rather than invariant). Without it, the product is a general website/CMS.
- **Per-post addressability** — every post has its own stable URL that can be linked and cited. Without it, there is no citable publication unit.

### L1 — Common Mature Structure

- composing editor (rich text/blocks or Markdown; media embedding; preview)
- draft → publish lifecycle with scheduling and revisions; published posts remain editable in place
- static pages (About/Contact) living outside the stream, reachable via navigation
- taxonomy (categories and/or tags) driving archive views (by tag/category/date)
- comments with moderation machinery (per-post toggle, approval, spam control) — common but optional per post
- themes / appearance layer separating design from content
- subscription/distribution: feeds (RSS heritage) and/or email notification to subscribers
- author identity: bylines, author pages/archives; multi-author support with roles on team publications
- search over the publication
- basic traffic analytics
- SEO metadata (titles/descriptions, social previews)

### L2 — Variant / Optional Structure

- deployment: hosted multi-tenant service vs self-hosted software (WordPress.com↔WordPress.org; Ghost(Pro)↔self-hosted)
- custom domains vs platform subdomains
- email newsletter delivery as a channel (including email-only posts)
- membership/paywall/paid subscriptions/tiers
- network discovery layer (platform feed of member blogs) vs fully independent publication
- monetization beyond subscriptions (ads, affiliate)
- import/export/migration tooling between platforms
- plugin/extension ecosystems; headless/API-first usage
- privacy posture (private sites, password-protected posts, member-only content)
- post formats, featured content, custom templates/routing, code injection
- AI authoring assistance (emerging)

### L3 — Vendor-specific Structure (stays in Research Notes)

- Ghost: Lexical JSON document storage; Handlebars theme engine with contexts; internal #hashtag tags; code injection fields; email-only posts; JAMstack/headless guides; GScan theme validation.
- WordPress.com: block editor + block themes; Jetpack tool family; WordPress Agent (AI) and MCP access for external agents; plan-gated features (e.g., SEO tools on eligible plans); Reader as a discovery surface; plugins marketplace.
- Medium: claps/responses, publications, partner-program monetization (positioning-level only; unverified during research).
- Blogger: blogspot subdomains, template gadgets (positioning-level only; unverified during research).

## Vendor-specific Findings

- WordPress.com's self-presentation has broadened to website builder/ecommerce/newsletter/hosting; the blog remains a first-class publishing mode ("Create a Blog" product line, blog courses, posts guides). This is platform drift at the product level, not a change to the Type.
- Ghost explicitly frames itself as a "professional publishing platform" for "independent publications", with membership business machinery as a differentiator.
- Network-affiliated vs independent publication is a real strategic axis: WordPress.com Reader and (positioning-level) Medium pull member blogs into a discovery surface; Ghost deliberately has none.

## Boundary Findings

- **vs Content Management System / CMS**: a CMS's primary object model is arbitrary content structure (pages, custom content types, application-like sites) managed by an organization; a blogging platform's primary object model is the dated post stream of an author-owned publication. WordPress straddles both: when the site is organized around posts, it is being used as a blogging platform; when organized around pages/custom types, as a CMS. Test: if the dated post stream were removed and only arbitrary pages remained, the product would still be a CMS but no longer a blogging platform.
- **vs Headless CMS**: headless CMS exposes content authoring without an owned reading surface; a blogging platform ships the reading surface (the blog) as the product. Ghost can be used headless, but that is an optional mode (L2), not the Type.
- **vs Microblogging Platform**: microblogging posts are short status updates consumed in a social follow-feed aggregating many authors; there is no author-owned publication container with its own address and archive. Blogging centers the author's publication; microblogging centers the social graph feed.
- **vs Newsletter publishing products (e.g., Substack-style)**: when email delivery + paid subscriptions are the primary product and the web archive is secondary, the product is newsletter-first. A blogging platform keeps the web publication primary; email is a delivery channel (L2). Ghost sits on the blogging side with strong email machinery; Substack sits on the newsletter side with a web archive.
- **vs Website Builder**: website builders center arbitrary page composition for a site; blogging is one module among many. A blogging platform centers the post stream.
- **vs Online Forum / Community Platform**: forums center topic threads with many participants; a blog centers one author's publication with readers reacting. Comments do not make a blog a forum.
- **vs Social Network**: the blog's primary surface is the publication, not a profile/feed/follow graph. Network-affiliated blogging platforms (Medium-style) drift toward social/network territory when discovery feeds become the primary surface.
- **去掉什么就变成另一个 Type**: remove the author-owned publication container → microblogging/social feed; remove the dated stream (keep arbitrary pages) → CMS/website builder; remove the web reading surface (keep authoring + email) → newsletter platform; remove per-post addressability → ephemeral broadcast surface.

## Historical / Market-Sample Check

Older and regional products — Blogger (1999-era), Movable Type, TypePad, LiveJournal, early WordPress, regional blog services — all fit the L0: an author-owned publication of dated posts in a reverse-chronological stream with permalinks. None of them require themes-as-products, plugins, newsletters, memberships, or network discovery to be recognizable as blogs. Therefore the L0 is not over-fitted to the current creator-economy implementation (memberships/newsletters stay in L2). Conversely, the check confirms that modern additions (email delivery, paywalls, AI authoring) must not enter the definition.

## Uncertainties

- Medium, Blogger, Substack official documentation was unreachable; their inclusion rests on positioning-level evidence. Any precise claim about their mechanics is deliberately absent.
- Comment moderation depth in Ghost (native {{comments}} helper observed; moderation workflow not fetched).
- Whether "newest-first" should be treated as invariant: WordPress and Ghost both allow reordering/custom routing, so it is recorded as the default presentation, not the invariant.
- The exact boundary behavior of network-affiliated platforms (Medium) could not be verified against current official docs; the network-vs-independent axis is asserted at positioning level.

## Final Synthesis

A Blogging Platform is software for publishing an author-owned web publication (the blog) whose content is a dated stream of individually addressable posts. The defining core is small: author-owned publication + post as unit + dated stream + permalink. Everything else — editors, taxonomy, comments, themes, feeds, email, memberships, analytics, extensibility, hosting models — is common mature structure or variant machinery layered on that core. The Type is bounded against CMS (arbitrary content structure), microblogging (social feed without publication container), newsletter products (email-first), and website builders (page-composition-first). The historical check confirms the definition holds for 1990s-era and regional products as well as current creator-economy platforms.
