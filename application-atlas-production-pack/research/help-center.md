# Research Notes — Help Center

Research date: 2026-09-07
Methodology: update-v1 workflow (Understand → Plan → Sample → Research → Model → Compare → Synthesize → Write → Review → Cite)

## Research Goal

Understand "Help Center" as an Application Type (DIRECTORY §02.06 Wiki & Knowledge Base): what the software category actually consists of when organizations run a customer-facing help center, what its stable structures are across products with very different packaging (help-desk suite component vs standalone pure-play vs legacy self-hosted), and where its boundaries sit against the neighboring Types — especially Self-service Support Portal (§07, processed), Knowledge Base Application (§02.06 sibling, unprocessed), Product Documentation Portal (§02.07, unprocessed), Enterprise Wiki (§02.06, processed), and Community/Forum Types.

## Initial Boundary (working hypothesis before research)

A Help Center is the organization's published self-service support site (articles/FAQs for customers), together with the authoring machinery to run it. Expected confusions:

- vs **Self-service Support Portal** — portal adds customer request intake + own-request tracking. Prior pass (self-service-support-portal, 2026-09-07) recorded: "the content-only pole (published answers without request intake + own-request view) is exactly where the Help Center/KB Types begin — keep-both ratified from this side."
- vs **Knowledge Base Application** — naming overlap hazard: the market sells this exact external-facing Type as "knowledge base software."
- vs **Product Documentation Portal** — support answers vs structured product docs; tooling overlap suspected.
- vs **Enterprise Wiki** — internal open editing vs external curated publishing (already held by the enterprise-wiki pass).
- vs **Community Platform / Q&A Community** — member-generated vs organization-authored.

## Research Questions

1. What objects exist in a help-center product? (article, category/section/collection, author, draft/publish state, feedback, search, theme, audience segments)
2. Who operates it, and what does the authoring/operations side look like?
3. What is the authoring-to-publication workflow (draft → review → publish → update → unpublish)?
4. How is content organized and retrieved (hierarchy, search, suggestions, AI answers)?
5. How does the surface handle audience control (public vs signed-in vs internal-only)?
6. How does it connect to the support operation (contact affordances, deflection, ticket forms) — and where exactly is the seam to the Portal/Help Desk Types?
7. What feedback/analytics machinery exists, and is it structural?
8. Multi-brand / multi-language / multi-product handling?
9. How does the market package the Type (suite component vs standalone), and what does each pole include?
10. What would older / minimal / differently-positioned products (FAQ pages, self-hosted KB apps) still satisfy — i.e., what is definitional vs era-typical?

## Representative Products

Selection: market representation + documentation completeness + different product philosophies + different customer tiers + different packaging poles.

| Product | Pole | Why sampled |
|---|---|---|
| Zendesk (Help Center / Knowledge) | help-desk suite component, market leader | deepest public operational docs; defines the suite-embedded pattern |
| Freshdesk (Customer Portal / Knowledge Base) | help-desk suite component, SMB tier | portal-section architecture makes the KB-vs-tickets-vs-forums decomposition explicit |
| Intercom (Help Center + Knowledge) | conversational-first suite | different philosophy: articles as fuel for AI agent/messenger; public/internal article split |
| Document360 | standalone knowledge-base/help-center pure-play | the non-suite pole; two-sided (Portal + Site) architecture; strong Tier-1 docs |
| KBPublisher | legacy self-hosted KB software | older-generation, dual internal/external positioning; historical/era counterweight |

Also attempted and abandoned (see Sources): phpMyFAQ (docs unreachable ×2), Helpjuice (not attempted after 5-product coverage sufficed).

## Sources

All fetched 2026-09-07 unless noted.

- Zendesk (Tier-1, official help articles retrieved via the Help Center content API JSON):
  - Organizing knowledge base content in categories and sections — https://support.zendesk.com/api/v2/help_center/en-us/articles/4408845897370.json
  - Viewing and managing your content hierarchy in Arrange Articles — https://support.zendesk.com/api/v2/help_center/en-us/articles/4408824317594.json
  - Help Center article search API (titles index) — https://support.zendesk.com/api/v2/help_center/articles/search.json?query="about the help center"
  - Observed titles incl.: About search sources in the help center; About SEO in the help center; Creating help center content using ticket data and generative AI; Enabling anonymous user tracking; Using the help center templating language; Using Zendesk Support and Zendesk Knowledge together
- Freshdesk (Tier-1, official support KB):
  - Overview of Freshdesk Portal — https://support.freshdesk.com/support/solutions/articles/50000003752
  - Manage Portal Sections — https://support.freshdesk.com/support/solutions/articles/50000004905
- Intercom (Tier-1, official help center):
  - Knowledge collection — https://www.intercom.com/help/en/collections/9615439-knowledge
  - Help Center explained — https://www.intercom.com/help/en/articles/56640-help-center-explained
- Document360 (Tier-1, official docs site):
  - Docs home (product architecture overview) — https://docs.document360.com/
  - Managing workflow status — https://docs.document360.com/docs/managing-workflow-status
  - Analytics overview — https://docs.document360.com/docs/analytics
  - Ticket deflector analytics — https://docs.document360.com/docs/ticket-deflector-overview
- KBPublisher (Tier-2, official product site):
  - Home / positioning — https://www.kbpublisher.com/ (Features page and user manual linked but not fetched in depth)
- Adjacent processed docs used for boundary work (internal): applications/self-service-support-portal.md, applications/enterprise-wiki.md, STATUS.md boundary notes.

Sourcing limitations:

- phpMyFAQ documentation (https://www.phpmyfaq.net/docs/) — transport error ×2 on 2026-09-07; abandoned per network rules. No claims rest on it. Intended role (open-source minimal FAQ pole) partially covered instead by KBPublisher.
- Zendesk HTML help pages returned 404 on the attempted section URL; content-API JSON worked and is the same official content.
- KBPublisher evidence is product-page level (Tier-2); no operational manual pages fetched; claims about it kept at positioning/feature-name level.
- Document360 homepage feature list is marketing-grade; operational claims about Document360 taken only from its docs site (Tier-1).

## Product Observations

### Zendesk (help-desk suite component; evidence layer A — directly observed)

- Help center = published public site; content organized as **categories** (top-level containers) → **sections** (contain related articles; subsections allowed) → **articles** (A).
- Operations side = **Knowledge admin** (and in-help-center editing); role-gated: "You must be a Knowledge admin to add and edit sections and categories" (A).
- **Drafts**: categories/sections can be marked draft; drafts "are not viewable by end-users" (A). Articles likewise have draft states (article JSON has a `draft` flag; labels include "draft") (A).
- **Article-level visibility**: "Access to a section is not set for the section as a whole, but is determined by the visibility of each article"; sections with all-internal articles are hidden from end-users (A). Article JSON carries `user_segment_id` / `permission_group_id` — audience segmentation and permission groups are article-level concepts (A).
- **Deletion is archival**: deleting a section archives its articles; "You can restore archived articles to another section" (A).
- **Ordering**: manual drag-and-drop reorder or automatic sort ("Order articles by") for categories/sections/articles (A).
- **Templates/theming**: live theme with category/section templates; a help-center templating language exists; SEO settings; search sources configuration (A for existence; detail not researched).
- Plan gating pervasive (banner tables per Suite plan on every article) (A).
- Zendesk ships a related-but-separate product (**Knowledge**) alongside Support — packaging around knowledge exists at product level (A for existence; structure not researched).
- AI-era: "Creating help center content using ticket data and generative AI" — generative drafting from ticket data (A for existence).

### Freshdesk (help-desk suite component, SMB; evidence layer A)

- Customer portal is decomposed into **sections**: **Tickets**, **Knowledge Base**, **Forums** — "All sections … are enabled by default. You can choose to disable them" (A). The KB section is a component of a larger customer-facing surface; a portal can be KB-only or Tickets+KB+Forums (A).
- KB described as: "Build a scalable Knowledge Base with articles, FAQs, and other content about your product or service to help customers find answers faster" (A).
- **Article visibility configuration**: "Knowledge base articles on this portal can be viewed by — everyone or only logged-in users" (A). CAPTCHA on feedback for anonymous visitors (A).
- Category selection controls which KB categories appear on the portal (A). Author-name display toggle (A).
- **KB analytics** exist ("Knowledge Base Analytics"; article views; agent views counted separately from customer views) (A).
- Multiple portals per product/brand; portal custom URL/domain; multi-theme management; WCAG theme; collision detection when two admins edit portal customization; portal-only developer permissions (A; plan-gated — counts kept here only).
- Deflection lives on the **Tickets** section, not the KB: "Auto suggest solutions while creating a new ticket — related articles will be suggested on the right pane" (A). This locates the deflection seam precisely at the portal side.
- Forums = community section with moderation settings, separate from KB (A).

### Intercom (conversational-first suite; evidence layer A)

- **Knowledge** hub manages "all of your support content to empower your customers, AI agent, and teammates" (A). Content types: **public articles**, **internal articles**, snippets, plus external sources synced in (Zendesk, Salesforce Knowledge, Freshdesk, websites, documents) (A).
- **Help Center** = the published surface: "With Help Center, you can create articles which enable customers to self-serve and find support 24/7" (A).
- Publication rule: "articles are only visible on your Help Center if they're in a collection" — collections are the publication container (A). Collections organized by customer topics; short descriptions optimize for search (A).
- **Multi-help-center** for various products/brands; customization to match brand; translations for public articles (A).
- Articles power **Fin AI Agent** ("Fin AI Agent can use your public articles to hold conversations and provide AI answers"); articles also usable by agents in inbox conversations and outbound messages (A). Messenger can show articles without starting a conversation; orgs can require search before a conversation (A). Product-specific current-state note: embedding articles on one's own website not supported (A, product-specific).
- **Feedback**: reactions (positive/neutral/negative) on article end; per-article stats (A).
- **Articles report**: helpfulness, topics customers searched for but didn't find, most negative reactions, conversations sparked per article (A). The analytics→gap→write-next loop is explicit ("gain inspiration for what to write next").

### Document360 (standalone pure-play; evidence layer A)

- Two-sided architecture, stated on the docs home: **Knowledge Base Portal** "For Editors, Writers, and Reviewers" + **Knowledge Base Site** "For Customers and Employees" (A). The same tool sells internal KB and external KB use cases (A).
- Authoring: advanced **WYSIWYG & Markdown editors**; templates; snippets & variables; custom fields; glossary; central **Drive** media storage; in-line comments; duplicate content detection; scheduled publishing (A for feature existence).
- **Workflow statuses**: "workflow status tracks where an article is in your documentation cycle, from initial draft through review stages to publication" — statuses configurable in a **Workflow designer**; assignees, due dates, comments, auto-assign, read-only states, workflow history; per-language workflow status; bulk updates via **Tasks page**; Tasks tabs: Workflow / **Feedback** / **Review reminder** (A).
- Article versioning exists ("Article version" indicator; "Each version of an article revision has its own workflow history") (A).
- **Feedback manager**: "Capture article-level & AI response feedback to identify content gaps"; reader feedback becomes assigned tasks (A).
- **Analytics** (A): article views/reads/reading time/feedback ratings; search analytics incl. **no-result searches**; AI search analytics; MCP search analytics; reader analytics (who reads, location, duration); user (team) analytics; link-status; page-not-found; **ticket deflector analytics**. Analytics scoped per workspace and language (A).
- **Ticket deflector** (A): "a feature that reduces support tickets by surfacing relevant knowledge base articles while a user is filling out a ticket form. If the suggested articles answer their question, the user can exit the form without submitting a ticket." Metrics: answered-from-KB vs form-submitted; keywords with answer-found/answer-not-found; search success rate. The deflector hands off to a ticket form — it is not itself a tracked request record (A).
- Site side: homepage builder, custom domain, SEO, localization, IP restriction, JWT-authenticated widget access, knowledge base widget (A for existence).
- Roles/permissions, SSO/SCIM, audit logs, sandbox, private hosting (A for existence; detail not researched).
- Positioning/self-label: "Knowledge Base Software"; use cases include knowledge base, software documentation, user manuals, SOPs, API documentation (A — tooling overlap with docs Types is vendor-declared).

### KBPublisher (legacy self-hosted dual-use; evidence layer B/A-lite — product-page level)

- Self-described "Knowledge Management Software" aimed at both customer self-support ("reduce call volume", "help customers self-serve") and internal staff knowledge (A-lite).
- Publishes "articles, white papers, user manuals, business processes, FAQs, online help, APIs, or any other type of information" (A-lite).
- Categories ("list posts in several categories"), search, related articles (per user testimonial text on the vendor page — weak evidence, corroborated only by feature list) (A-lite).
- Self-hosted + cloud editions; community edition; user manual shipped as its own KB (A-lite).
- No workflow/review machinery, AI, or analytics surfaced at this evidence level — consistent with an earlier, minimal era of the Type (B).

## Cross-product Comparison

| Dimension | Zendesk | Freshdesk | Intercom | Document360 | KBPublisher |
|---|---|---|---|---|---|
| Packaging | suite component (Support/Knowledge) | suite component (portal section) | suite component (Knowledge + Help Center) | standalone pure-play | standalone, self-hosted/cloud |
| Published surface | help center site | portal KB section | Help Center site | KB Site | KB front-end |
| Unit of content | article | article (solutions/FAQs) | article (public + internal) | article | article |
| Publication container | category → section (subsections) | categories selected per portal | collection (required for visibility) | category manager | categories |
| Ops side | Knowledge admin | agent portal (Admin) | Knowledge hub | KB Portal (editors/writers/reviewers) | admin |
| Draft/publish | drafts (container + article), archive/restore | publish; visibility config | collection gating; translations | draft → review workflow statuses → publish; versions; scheduled publish | (not evidenced) |
| Audience control | article-level visibility; user segments; permission groups | everyone vs logged-in | public vs internal articles | public/private; readers incl. employees; IP/JWT gating | (not evidenced) |
| Search | search sources config; SEO | KB search | search + require-search-before-chat | search analytics incl. no-results; AI search | search |
| Feedback | votes (article JSON vote fields) | feedback w/ CAPTCHA | reactions (3-state) | feedback manager → tasks | (not evidenced) |
| Analytics | plan-gated; views | KB analytics (views) | articles report (searches without results, reactions, conversations) | full analytics suite | (not evidenced) |
| Contact/deflection seam | (suite) | auto-suggest on ticket form | articles in Messenger/Fin; require search | ticket deflector form | (not evidenced) |
| Community | (adjacent products) | Forums section (disableable) | community product (separate) | (not evidenced) | (not evidenced) |
| Multi-brand/language | multiple help centers; locales | multiple portals; themes; (locales) | multi-help-center; translations | workspaces; languages; localization | (not evidenced) |
| AI layer | generative drafting from tickets | (suite AI elsewhere) | articles power Fin answers | AI search/answers/writing; MCP exposure | — |

Reading: the **article corpus + published reader site + ops side** triad is present in every product (B). Everything else is tiered: search/feedback/analytics nearly universal in current products (B); contact affordances/deflection nearly universal in support-packaged products but realized very differently (B with high variance); community, workflow depth, segmentation, AI vary (A per product).

## Canonical Model — abstraction layers

### L0 — Defining Invariant

Three properties; removing any one stops the product from being recognizable as a Help Center:

1. **Organization-curated answer corpus** — a persistent body of individually addressable help articles (how-to guides, troubleshooting solutions, FAQs) authored and maintained by the organization's own team. Authorship is restricted to the organization; readers never author the record copy. Remove → community forum / Q&A site (member-generated).
2. **Reader-facing published help site** — the corpus is published as a branded web surface organized for self-serve retrieval — a browse hierarchy plus search — and reachable by the organization's customers/end users without staff mediation. The audience is *external* to the authoring team. Remove → internal knowledge tool (wiki / internal KB).
3. **Integrated authoring & publication management** — the same system provides the operations side through which the team creates, organizes, publishes, updates, and withdraws content and configures who can see it (draft states, visibility settings). Remove → a static hand-published page collection; not a managed system for running help content.

Historical check: a plain FAQ web page maintained by hand (pre-platform era) and a self-hosted KB application (KBPublisher generation) satisfy all three without search analytics, feedback votes, AI, theming, or plan gating. Search itself is NOT L0 — a categorized FAQ list is still recognizably the Type; the retrieval organization (structure + a way for readers to find things) is the invariant, search is the modern default realization.

### L1 — Common Mature Structure (standard capabilities, not definitional)

- Full-text search over the corpus (with no-result tracking in current products)
- Draft → publish workflow, updates, and withdrawal (unpublish/archive); versions in several products
- Article feedback (helpful votes / reactions / comments) feeding content improvement
- Content-performance analytics: views, search terms, content gaps
- Audience/visibility configuration: public vs signed-in readers; internal-only articles
- Contact affordances: links/buttons/deflector forms connecting readers to the support operation
- Branding, custom domains, theming
- Multi-language translations
- Multi-brand / multi-product help centers
- Roles and permissions on the operations side
- Migration/import tooling; SEO settings
- Related-article suggestions; article metadata (author, dates, labels)

### L2 — Variant / Optional Structure

- Community/forum section beside the articles (explicitly disableable in-sample)
- Request intake on the same surface (→ crosses into Self-service Support Portal territory; deflector forms that hand off are still help-center-side)
- Internal/employee knowledge sections in the same tool (dual-audience posture)
- Gated/authenticated content (user segments, JWT/SSO-gated readers, IP restriction)
- Documentation-genre stretch: software docs, user manuals, SOPs, API docs produced in the same tool
- Widget/embed form factor; in-product article surfaces
- AI-era layer: AI search with citations, AI answers/agents powered by the corpus, AI-assisted drafting, agent/MCP-facing corpus exposure
- Static/docs-as-code publication posture (drift boundary toward Product Documentation Portal)

### L3 — Vendor-specific (kept out of the final document)

- Zendesk: templating language for themes; permission groups vs user segments distinction; max 5 section levels / up to 200 sections per section; per-plan feature banners; the separate "Knowledge" product packaging; "Anatomy of the Help Center" framing.
- Freshdesk: named themes (Marina WCAG), theme import limits, collision detection in portal code editor, portal-specific ticket display, plan names/gates.
- Intercom: Fin AI Agent/Copilot, Messenger article browsing, require-search-before-conversation, no-embed restriction (current product state), Knowledge Hub source sync partners.
- Document360: Eddy AI suite, workflow designer/task pages mechanics, MCP server + MCP search analytics, private hosting, workspace/language scoping of analytics.
- KBPublisher: community edition, edition split.

## Vendor-specific Findings

See L3. Additionally: Zendesk and Freshdesk count "agent views" of articles separately from customer views — an operational-support-flavored metric (A, two products; kept out of final doc as detail). Intercom's "articles power the AI agent's resolution rate" phrasing shows the corpus being repositioned as AI infrastructure in the current era (A, one product; noted as era signal, not structure).

## Rejected Findings

- "A Help Center is part of a help desk" — rejected as definitional. Standalone pure-plays exist (Document360, KBPublisher); the content-only pole stands without any support operation (already ratified by the self-service-support-portal pass). Suite packaging is the market's dominant shape but not the Type's structure.
- "Search is definitional" — rejected after the historical check: categorized FAQ lists satisfy the Type without search. Retrieval organization is the invariant; search is the universal modern realization (L1).
- "Community/Q&A section is definitional" — rejected: explicitly a disableable section in-sample (Freshdesk), absent in others.
- "AI answers are definitional" — rejected: era-typical (3 of 5 in-sample products at product level), absent from the KBPublisher generation; L1/L2.
- "Multi-language is definitional" — rejected: varies by customer base; L1/L2.
- "Help center = any content site (blog/marketing pages)" — rejected: the corpus genre (problem-shaped answer articles), the retrieval organization, and the support purpose distinguish it from general publishing.

## Boundary Findings

1. **vs Self-service Support Portal (§07, processed)** — sharpest seam. Portal = answers + self-initiated request intake + the requester's own request record. Help Center = the content-only pole. Removal tests (recorded both directions): strip request intake + own-request view from a portal → a help center remains; add request intake + tracked own-request view to a help center → it becomes a portal. Contact affordances (contact buttons, suggested articles while typing) appear on the help-center side, but the persistent tracked request belongs to the portal/desk side. Document360's ticket deflector is direct evidence: it counts "form submitted" and hands off — it does not hold the request record (A).
2. **vs Knowledge Base Application (§02.06 sibling, unprocessed)** — naming overlap is severe: the market sells this external-facing Type as "knowledge base software" (Document360 self-label; KBPublisher likewise), and sampled tools are dual-audience (Document360 site serves "customers and employees"; Intercom ships public + internal articles in one hub). Proposed seam for the KB pass: external support publication (this Type) vs internal curated corpus (KB Application); joint review recommended; packaging must not drive the boundary.
3. **vs Product Documentation Portal (§02.07, unprocessed)** — genre and lifecycle seam: support answer corpus (problem-shaped, continuously maintained, success measured by deflection/feedback) vs structured product documentation (reference/tutorial/API, release-versioned). Tooling overlap is vendor-declared in-sample (Document360 sells software/API documentation as use cases of the same tool). Joint review recommended when that pass runs.
4. **vs Enterprise Wiki (§02.06, processed)** — held: internal audience + open member editing + emergent structure vs external audience + curated restricted authorship + publisher-governed corpus. The enterprise-wiki pass already records the same seam from its side.
5. **vs Community Platform / Q&A Community** — organization-authored record copy vs member-generated content; a community can sit beside the help center as a section/product, which proves separability.
6. **vs CMS / Blogging Platform / Website Builder** — general-purpose publishing vs purpose-built support publishing; the help-center Type is defined by the corpus genre, retrieval organization, and support-operation integration, not by page-design generality.
7. **vs Help Desk (§07, processed)** — the agent team's operating application; the help center is a publication surface over a corpus, not a work queue. Suite products bundle both; structurally independent.

## Historical / Market-Sample Check

Question: would older, regional, platform-native, differently-positioned products still fit the L0? Yes: hand-maintained FAQ pages (site-shaped), self-hosted KB applications of the 2000s generation (KBPublisher-class: categories + articles + search + admin), and open-source FAQ tools all satisfy the three L0 properties without any modern layer. Therefore nothing era-specific (search analytics, feedback votes, AI, theming, plan gating, cloud delivery) enters the definition. Conversely the definition does not depend on the suite-embedded packaging that dominates today's market — standalone pure-plays pass.

## Uncertainties

- Standalone-pure-play breadth rests mainly on Document360 (Helpjuice/HelpDocs not fetched; phpMyFAQ unreachable ×2). Claims about the standalone pole are calibrated accordingly; no numeric or plan-level claims made for the pole beyond Document360's own docs.
- Zendesk's "Knowledge" (vs "Guide") product split was observed but not researched; no claims about it beyond existence.
- Legacy samples evidenced at product-page level only (KBPublisher); workflow/permission mechanics of that generation inferred weakly and not asserted.
- Intercom's embedding restriction and Fin behavior are current product states; treated as product-specific facts, not Type structure.
- No pricing, plan-gating, or numeric limits are asserted in the final document; observed numbers (section nesting levels, theme counts, plan names) live only here.

## Final Synthesis

A Help Center is the organization's customer-facing self-service answer publication: a curated corpus of help articles, published as a branded reader-facing site organized for retrieval, operated through an integrated authoring/management side. The market realizes the Type overwhelmingly as the content layer of help-desk/customer-service suites, with a standalone-pure-play pole beside it. Its standard capabilities (search, feedback, analytics, visibility control, contact affordances, translations, multi-brand, AI answers) make the corpus maintainable and measurable but do not define it. The three load-bearing boundaries: the Self-service Support Portal begins where tracked request intake and the requester's own request view are added; the internal-facing curated corpus is the Knowledge Base Application's ground (joint review recommended); and the structured, release-versioned documentation genre is the Product Documentation Portal's ground (joint review recommended).
