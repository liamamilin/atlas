# Research Notes — Product Documentation Portal

Research date: **2026-09-08**

## Research Goal

Understand what a Product Documentation Portal (a.k.a. "product docs", "documentation platform") really is as an Application Type: what its core objects are, who uses it, how documentation flows from authoring to a published reader-facing site, what machinery keeps the docs aligned with the product, and how it differs from the adjacent Types Help Center, Knowledge Base Application, Developer Documentation Portal, CMS, and Blogging Platform.

## Initial Boundary

The leaf sits in DIRECTORY §02.07 Content Publishing, next to CMS, Headless CMS, and Blogging Platform. Immediate neighbor Types:

- **Help Center** (§02.06, processed 2026-09-07) — external support answer site; the pass left an advance note for this leaf: "genre/lifecycle seam is real but tooling overlap is vendor-declared in-sample (Document360 ships software documentation, user manuals, SOPs, and API documentation as use cases of the same tool)". Joint review recommended.
- **Knowledge Base Application** (§02.06, processed 2026-09-08) — curated answer corpus; left an advance note: "question-driven, continuously maintained answer corpus vs release-versioned structured documentation; tooling overlap is vendor-declared (Document360 sells API documentation as a use case of the same tool)".
- **Developer Documentation Portal** (§12, processed 2026-09-08) — build-with-product corpus for developers; left a joint-review flag: "genre/audience seam — build-with-product corpus vs product usage documentation for the product's audience generally; the seam narrows where a product's entire audience is developers; the two definitions should be ratified together rather than sequentially". This pass discharges that flag.
- **API Documentation Platform** (§12, processed 2026-09-06) — definition-bound API interface reference as central artifact (seam already established by the DDP pass).
- **CMS / Headless CMS / Blogging Platform** (§02.07, processed) — generic web content machinery; DDP pass recorded the doc-genre machinery seam ("doc-tree navigation, whole-tree release versioning, reference generation, documentation QA").
- **Enterprise Wiki** (§02.06, processed) — open member editing, emergent link structure.

Hypothesis at start: a documentation platform whose corpus documents *how to use a product*, published as a navigable reader-facing site, with machinery keeping the corpus current as the product ships. Risk: being an alias of Developer Documentation Portal (same machinery). Risk 2: being absorbed by Knowledge Base Application (Document360 straddles).

## Research Questions

1. What are the core objects? (project/space/site, page/article, tree/TOC, version, audience, contributor)
2. How does authoring work? (WYSIWYG vs Markdown-in-repo vs MDX; blocks/components)
3. How is content organized and navigated for readers?
4. What is the publishing flow? (draft → review → publish; previews; domains)
5. What currency mechanisms keep docs aligned with the product? (release-coupled versioning, changelog/release notes, repo sync, review reminders)
6. How is the published corpus access-controlled? (public / private / mixed)
7. What reader-side loops exist? (search, feedback, analytics, AI assistants)
8. Which capabilities are current-era machinery rather than definitional?
9. Where exactly do the boundaries with Help Center / KB / DDP / CMS / Blog run?

## Representative Products

Selected for market representation + documentation completeness + different product philosophies + different customer tiers:

| Product | Philosophy / pole | Tier |
|---|---|---|
| **GitBook** | Editor-first hosted platform with bi-directional Git Sync; markets product documentation explicitly; one docs site carrying multiple sections (product docs / API reference / help center / changelog) | Startup → enterprise |
| **Mintlify** | MDX docs-as-code with a Git-backed web editor; developer-leaning but documents help-center and KB use cases itself | Dev teams / startups |
| **Document360** | Enterprise WYSIWYG+Markdown knowledge-base platform; self-labels knowledge base *and* product documentation (user manuals, SOPs, API docs) | Enterprise mid-market |
| **ReadMe** | Reference-centric hosted platform: project = guides + API reference + changelog; whole-corpus doc versions tied to product versions | API product teams |

Legacy help-authoring pole (MadCap Flare class) attempted for the historical check — **unreachable (403)**; legacy claims kept conceptual (see Sourcing Limitations).

## Sources

All fetched 2026-09-08 (Tier-1 official documentation unless noted):

- GitBook — Documentation home `https://gitbook.com/docs`; Core concepts `https://gitbook.com/docs/reference/concepts.md`
- Mintlify — Documentation home `https://www.mintlify.com/docs`; Editor overview `https://www.mintlify.com/docs/editor/index`; docs index `https://www.mintlify.com/docs/llms.txt` (changelog/analytics/use-case guide titles)
- Document360 — Documentation home `https://docs.document360.com/` (features grid); Welcome `https://docs.document360.com/docs`; Organizing your knowledge base `https://docs.document360.com/docs/organizing-your-knowledge-base`; Article status `https://docs.document360.com/docs/article-status`; full docs index `https://docs.document360.com/llms.txt`
- ReadMe — Structuring Your Documentation `https://docs.readme.com/main/docs/structuring-your-docs.md`; Versioning `https://docs.readme.com/main/docs/versions.md`; Creating a Project `https://docs.readme.com/main/docs/creating-a-project.md`; index queries `https://docs.readme.com/main/llms.txt?query=…`
- MadCap Software — `https://www.madcapsoftware.com/products/flare/overview.aspx` → **403, abandoned after one attempt**

Note: these vendors all publish their own docs **on their own products** (GitBook on GitBook, Mintlify on Mintlify, Document360 on Document360, ReadMe on ReadMe) — dogfooding gives unusually direct operational evidence of the Type.

### Sourcing Limitations

- GitBook's `?ask` query endpoint timed out once; recovered via direct page fetch (no degradation).
- Document360 `llms.txt` does not honor ReadMe-style `?query=` filtering; full index returned and used as an index (page titles only for unopened pages — capabilities recorded at index-title strength).
- MadCap Flare (legacy help-authoring pole) unreachable (403 ×1, not retried per network rules). The legacy/printed-manual lineage is therefore held **conceptual**, with no vendor-specific claims.
- Mintlify whole-corpus versioning support was NOT directly evidenced; not claimed (changelog and git-based currency are evidenced).

---

## Product Observations

### GitBook (evidence layer A — direct)

- **Containers**: Organization → Groups → **Sections** → Pages. "A section is a project that lets you work on a set of related pages… Sections belong to a docs site… create separate sections for your product documentation, API reference, changelog, help center — and publish them all on one docs site."
- **Docs site** is the published surface: "your docs will be published and available to your selected audience as a website that you can customize with your own branding, analytics and custom domain."
- **Site structure**: **Sections** (multiple documentation types on one site, each a top-nav entry) and **Variants** ("multiple versions of the same documentation… localize your entire documentation into multiple languages, or document previous versions of your product"). Readers switch variants via picker.
- **Pages + TOC**: pages live in sections; table of contents on the left; page groups; nesting/subpages.
- **Block-based WYSIWYG editor**; Markdown supported as input for all blocks; editing desktop/laptop only.
- **Editing flow**: on published sites, edits happen via **change requests** (git-like branches): edit → request review → reviewers see diff, comment → approve → **merge** goes live and creates a version in section history.
- **Git Sync**: bi-directional sync with GitHub/GitLab; "changes you make in GitBook's visual editor are automatically synced — as are any commits made on GitHub or GitLab"; enables batch changes and linting.
- **Audience control**: default public + indexed; **share links** (private link access); **authenticated access** (identity provider gates the site; "ideal for… publishing an internal knowledge base"); **adaptive content** shows/hides pages or blocks by user attributes.
- **Customization**: logos/icons/colors/fonts/themes; SEO + AI optimization automatic (sitemap from TOC, CDN, `.md` versions of every page, MCP server per site, `llms.txt`/`llms-full.txt`).
- **AI layer**: GitBook Agent (drafts, edits, reviews change requests, flags gaps against style guide), reader-facing AI Assistant (answers from docs + connected support sources), AI Insights (visitor questions → knowledge gaps), MCP for docs.
- **Permissions**: org roles (Editor/Viewer) with per-content overrides.

### Mintlify (evidence layer A)

- **Model**: docs live in a Git repository; the web **editor** is a managed Git client. "The editor uses a docs-as-code workflow with all your changes backed by Git."
- **Editing**: visual mode + **source mode (MDX)** editing the same file; component menu; real-time collaboration (live cursors, comments, suggestions).
- **Publishing = Git**: "Publishing writes to Git… If you publish to your deployment branch, this updates your live site immediately. On a feature branch, you can save changes to the branch or open a pull request for review. Nothing on a feature branch reaches your live site until it merges."
- **Site structure**: sidebar "Publishing" tab = navigation structure of the site ("Organize pages as you want them to appear in your site"); file tree home with Personal/Workspace pages.
- **Roles**: Admins/editors edit and publish; viewers browse, comment, suggest.
- **Self-described platform span** (index titles): guides for "Create developer documentation", "Create a knowledge base", "Create a help center", "Headless docs with a custom frontend" — one machinery, multiple documentation genres.
- **Content genres** documented via the Diátaxis framework guide: "tutorials, how-to guides, reference, and explanation".
- **Changelog**: "Create product changelogs with date-based entries, RSS feed support, and subscriber notifications to keep users informed about updates."
- **Maintenance**: guide "How to maintain documentation over time — review schedules, ownership models, automated checks, content lifecycle"; automations run recurring docs maintenance on schedules; agent jobs open PRs.
- **Analytics** (REST API): page views split by **human and AI traffic**, unique visitors, search queries with click-through rates, per-page feedback (thumbs up/down), assistant conversations.
- **Access**: private docs via OAuth 2.0 (Auth0 guide with group-based access); custom domains; preview deployments per branch; static export to self-host.
- **Localization**: locale-based routing, language switcher; docs published in en/fr/es/zh.
- **Machine-readable surface**: `.md` versions, `llms.txt`, MCP; GEO guide for AI answer engines.

### Document360 (evidence layer A)

- **Five-level hierarchy**: **Project → Workspaces → Languages → Categories → Articles**. "A project is your top-level container… Each workspace… has its own content tree, its own URL, and can be set to different visibility levels — public, beta, or deprecated."
- **Workspaces = product-version documentation**: "Workspaces allow you to create separate documentation for specific product versions. This segregation helps to ensure that readers have access to the most relevant and up-to-date information." Default workspace auto-created named **v1**.
- **Categories**: folder/index/page types, nested subcategories, drag-and-drop without breaking URLs; category tree defines reader navigation.
- **Articles**: created blank/from template/Eddy AI; "Each article follows a draft-to-published workflow."
- **Article status model** (portal-side editorial state): Draft / Published / Unpublished / **Stale** (review reminder date reached; stays live until reviewed) / Published-with-active-draft / translation-pending (globe). Editing a published article creates a new unpublished version (revision history).
- **Status indicator** (reader-side): "New / Updated / Custom" badges on the site — explicitly separated from editorial status.
- **Two surfaces named**: "Knowledge base portal" (contributors) vs "Knowledge base site" (readers).
- **Review & approval**: workflow designer ("Manage reviews, approvals, and updates with structured workflows"); article review reminders; scheduled publishing; hide/unpublish; mark-as-deprecated.
- **Reusable content**: snippets, variables, templates, glossaries; duplicate-content detection.
- **Access control**: reader accounts & reader groups; per-article access control (team accounts, reader accounts, reader groups); private share links pre-publication; IP restriction; SSO/SCIM.
- **API documentation**: from OpenAPI spec files/URLs, CI/CD via CLI, Try-It console — same platform carries the reference genre.
- **PDF output**: "Compiling content for PDF" (index title) — manual-style export alongside the site; step-by-step guides exportable for offline use.
- **Localization**: languages per workspace, machine translation ("Translate with Eddy AI"), multilingual KB.
- **Analytics**: article reads/views/likes/dislikes, search analytics incl. no-result searches, content-gap insight; feedback manager (article-level + AI response feedback); read receipts (reader acknowledgement).
- **AI layer**: Eddy AI writer suite (style guides, FAQ generators, SEO descriptions), assistive search (Ask Eddy), AI chatbots trained on docs + external sources with ticket escalation to Zendesk/Freshdesk, MCP server, llms.txt generation, GEO/SEO tooling.
- **Self-described span**: "Build knowledge bases, publish API docs, write SOPs, create user manuals, deploy AI chatbots - all from one place"; workspace-vs-category guidance explicitly frames audience separation: "A developer and a customer support agent have nothing to search in common."

### ReadMe (evidence layer A)

- **Project = one documentation home**: "Name your project to match your API… choose your subdomain (e.g., yourcompany.readme.io)"; custom domain & SSL; team roles (Admins/Editors/Viewers).
- **Content types**: **Categories → Guides (pages) → Sections (within page)**; plus **Custom Pages**; content-type system: "Guides: explain concepts… API Reference: comprehensive details about endpoints… Recipes: complete, real-world examples… Changelog: communicate what's changed"; cross-linking with typed prefixes (`doc:`, `ref:`, `page:`, `changelog:`).
- **Whole-corpus versioning**: "Guides, Recipes, and Reference sections are versioned. Content for Landing Page, Discussions, and Changelog will persist across versions." New version **forks** from an existing one; version settings: display name, **beta** and **deprecated** badges (deprecated shows a banner), visibility (default/public/hidden) with a reader-facing version dropdown. "The most obvious use case is… your documentation version needs to match the versioning that might be taking place with your API or other technical product." Fork-a-version restructuring use case documented too.
- **Branches + Reviews** (docs-as-code collaboration on the hosted platform), Suggested Edits, two-way GitHub sync ("Documentation Structure… structured our documentation for two-way syncing"), GitHub AI Writer proposing doc updates when PRs change the codebase.
- **Reusable content**: version-scoped blocks (Enterprise: cross-version "Global Reusable Content").
- **Access**: internal documentation ("Control who can access your docs"), custom login page, custom data in docs.
- **Analytics**: ReadMe Metrics (API usage logs tied to docs), Docs Audit (score docs against style guide), search/discoverability tooling.
- **AI layer**: Owlbot AI (reader assistant + API), AI Agent panel (draft/edit/research), MCP server, AI discoverability guidance.

---

## Cross-product Comparison

| Structure | GitBook | Mintlify | Document360 | ReadMe | Strength |
|---|---|---|---|---|---|
| Product-bound docs corpus as unit of record | Section(s) per product docs | repo of MDX docs for a product | Project → Workspaces ("product versions") | Project per API/product | **4/4 — core** |
| Page/article as addressable unit | Page (blocks) | MDX page | Article | Guide / Custom Page | **4/4 — core** |
| Deliberate navigable tree (TOC) | Page groups + subpages + TOC; sitemap from TOC | "Publishing" navigation structure | Category tree (folder/index/page) | Categories → guides | **4/4 — core** |
| Two-sided surface: contributor portal vs published site | Editor vs docs site (custom domain) | Editor/dashboard vs live deployment | "Knowledge base portal" vs "Knowledge base site" | Dashboard vs hub | **4/4 — core** |
| Draft → review → publish lifecycle | Change requests (branch/review/merge) | Branch → PR → merge deploys | Draft/Needs review/Stale + workflow designer | Branches + Reviews, Suggested Edits | **4/4 — core** (mechanism varies: git-branch vs status-model) |
| Currency machinery vs product change | Git Sync (bi-directional); variants for previous product versions | Publish-to-deploy branch; automations; maintenance guide | Workspaces per product version; revision history; stale/review reminders; scheduled publishing | Whole-corpus version forks matching product/API versions; GitHub AI writer on code PRs | **4/4 — core** (mechanism varies) |
| Release-coupled versioning with reader switcher | Variants ("previous versions of your product") | not evidenced (not claimed) | Workspaces public/beta/deprecated | Version forks, beta/deprecated badges, dropdown | **3/4 — common, not universal** |
| Changelog / release notes | Section type example ("changelog") | Changelog pages (dated entries, RSS) | Release notes templates (index); what's-new page | Changelog content type (persists across versions) | **4/4 — common** |
| Reader search | Search + AI assistant | Smart search (API: queries, CTR) | Portal search + AI assistive search + no-result analytics | Search + AI discoverability | **4/4 — standard** |
| Reader feedback loop | AI Insights (gaps) | Per-page thumbs feedback API | Feedback manager, likes/dislikes, read receipts | Suggested Edits / Suggest in GitHub | **4/4 — standard** |
| Analytics incl. content-gap detection | AI Insights | Views/visitors split human vs AI; search CTR | Article analytics, search trends, health checks | Metrics (API usage), Docs Audit | **4/4 — standard** |
| Access control on published corpus | Public / share links / authenticated / adaptive content | Public; OAuth private docs | Public/beta/deprecated; reader accounts & groups; per-article ACL | Version visibility; internal docs; custom login | **4/4 — standard** (granularity varies) |
| Branding + custom domain | Yes | Yes | Yes (CSS/JS, domain mapping) | Yes (logo, auto brand colors) | **4/4 — standard** |
| WYSIWYG **and** Markdown authoring | WYSIWYG + Markdown input | Visual + MDX source | Advanced WYSIWYG + Markdown editor | Rich editor (Markdown-friendly) + md sync | **4/4 — standard** |
| Localization | Variants (languages) | Locale routing (en/fr/es/zh) | Languages per workspace + machine translation | not evidenced in fetched pages | **3/4 — common** |
| Reusable content (snippets/variables/templates) | not directly evidenced | components/templates guide | Snippets, variables, templates, glossaries | Reusable content (version-scoped) | **2/4 evidenced — common** |
| PDF / offline output | .md exports (page-level) | Static export (HTML bundle) | Compile to PDF; offline guide export | not evidenced | **2/4 evidenced — optional** (HAT heritage) |
| API reference section inside the docs site | Section example | OpenAPI-generated pages | From OpenAPI + Try-It console | Native API reference | **4/4 — standard capability** (but it is the API Documentation Platform's center) |
| AI writer / reader-assistant / MCP / llms.txt | Agent, Assistant, MCP, llms.txt | Agent jobs, Assistant, MCP, llms.txt | Eddy AI suite, chatbots, MCP, llms.txt | Owlbot, Agent, MCP, AI discoverability | **4/4 — current-era layer (2026)** |
| Multi-product/multi-audience architecture | Groups + sections | Multiple deployments/orgs | Workspaces per audience/product line | Child projects (Enterprise) | **4/4 — common** |

## Canonical Model (drafted abstraction)

```text
Product Documentation Portal
├── (1) The product's usage-documentation corpus of record
│       persistent, individually addressable pages, authored & maintained
│       by the product's own team; genre = how to use/operate/administer the product
│       (getting started / guides / how-tos / reference / release notes)
├── (2) The published navigable reader surface
│       the corpus published as a self-serve site: topical navigation tree
│       + retrieval (search), reachable by the product's audience without staff mediation
└── (3) The production-and-currency machinery
        a managed production side (integrated authoring/publishing platform
        or docs-as-code pipeline) carrying an explicit mechanism keeping the
        published corpus aligned with the product as it changes
        (release-coupled versioning, changelog/release notes, repo-coupled sync,
        editorial review/staleness workflows)
```

## Abstraction Hierarchy

### L0 — Defining Invariant (candidate, kept deliberately small)

Three jointly-held structures:

1. **The product's usage-documentation corpus of record** — persistent, individually addressable pages/articles authored and maintained by the producer side (the product's own team), whose content teaches how to use, operate, and administer a specific product. Authorship is restricted; readers contribute only through feedback/suggestion channels. *Remove → marketing material or an open community wiki/forum.*
2. **The published navigable reader surface** — the corpus published as a structure-organized, self-serve reading site (topical tree + search), reachable by the product's audience without staff mediation. *Remove → an internal manuscript/authoring tool. Chronological-only organization → blog.*
3. **The production-and-currency machinery** — a managed production side (integrated authoring/publishing platform or docs-as-code pipeline) with an explicit mechanism keeping the published corpus aligned with the product as it changes. *Remove → a hand-published page collection; corpus–product drift is the Type's canonical failure mode.*

Jointly-held is load-bearing:
- 1 alone = authoring tool / content repository (a wiki or CMS holding product material)
- 2 alone = a hand-built static docs site
- 3 alone = a generic publishing pipeline
- 1+2 without 3 = a hand-published page collection (the pre-history; drift)
- 1+3 without 2 = internal drafting system, no reader portal
- 2+3 without 1 = generic site builder/CI with nothing product-doc-shaped

Domain binding: the corpus is **about a specific product** of the authoring organization (remove → general knowledge base / wiki). The reader is **the product's audience generally** (users, admins, evaluators — not exclusively developers building against a programmable surface; remove/replace → Developer Documentation Portal).

### L1 — Common Mature Structure (standard capabilities, not definitional)

- WYSIWYG + Markdown dual authoring; block/component content model
- Draft→review→publish collaboration (branch/change-request machinery OR status-model workflows — same function, different mechanisms)
- Reader search; feedback widgets; analytics (views, search terms incl. no-result queries, content-gap insight)
- Access control over the published corpus (public/private/mixed; reader accounts/groups or authenticated access)
- Branding, theming, custom domains
- Changelog / release-notes content type
- Localization machinery
- Reusable content (snippets/variables/templates)
- API-reference sections hosted inside the same portal
- Multi-product/multi-audience structuring (sections/workspaces/deployments)

### L2 — Variant / Optional Structure

- Release-coupled **whole-corpus versioning** with reader-facing switcher (3/4 sampled; tooling elsewhere cautions against versioning when docs rarely change between releases — same finding as the Developer Documentation Portal pass, so versioning is a common currency mechanism, not the invariant)
- PDF/compiled-manual and offline output (legacy help-authoring heritage)
- AI-era layer: AI writing agents, reader-facing AI assistants grounded in the corpus, MCP servers, llms.txt/agent-readable surfaces, GEO/SEO tooling (2026-current; expected to age)
- Adaptive/conditional content (show/hide by reader attributes)
- Interactive guides: decision trees, step-by-step captured guides, embedded demos/videos
- Internal/SOP documentation carried on the same tool
- Community/changelog-forward postures; headless/frontend-custom deployments; static export/self-hosting

### L3 — Vendor-specific (research notes only)

- GitBook: sections/variants naming, adaptive content, `.md`+`ask` agent interface, AI Insights branding
- Mintlify: MDX source mode, Mintlify Index REST API, automations with scheduled triggers, static-export API
- Document360: Eddy AI (writer/search/chatbots with ticket escalation to Zendesk/Freshdesk), workspace visibility labels public/beta/deprecated, read receipts, duplicate-content detection
- ReadMe: Owlbot, ReadMe Metrics (API-log-documented integration), typed cross-link prefixes (`doc:`/`ref:`/`changelog:`), "Global Reusable Content" (Enterprise), version fork semantics + poetry in error payloads

## Boundary Findings

1. **vs Developer Documentation Portal (§12) — the critical seam (joint ratification).** Same machinery family, different corpus genre + audience. DDP (that pass): "the corpus that teaches developers how to build with the product… quickstarts/tutorials/how-tos/concepts/interface reference… teaching and referencing the product's programmable surface." This pass: the corpus teaches how to **use/operate/administer** the product for the product's audience **generally**. The seam narrows to convergence where the product's entire audience is developers (an API's product docs ARE developer docs) — exactly as that pass predicted. Vendor evidence that the machinery is shared: GitBook hosts product docs + API reference + help center as sections of one docs site; Document360 ships user manuals + API docs + SOPs as one tool; Mintlify documents dev-docs/KB/help-center as use cases of one platform. **Keep-both on the genre/audience seam; ratify the two definitions together.** The L0s are structurally parallel (corpus + reader surface + production/currency machinery), differing in corpus genre and audience binding — genre-parallel Types over one machinery family, like the §05.07 OMS family pattern.
2. **vs Help Center (§02.06) — genre/lifecycle seam (discharges that pass's advance note).** Help center: problem-shaped, continuously maintained answer corpus whose success is deflection/resolution, with contact affordances handing off to the support operation. This Type: structured usage documentation organized around the product (learning/reference structure, not question structure), currency coupled to product releases. Overlap is real and vendor-declared (Document360; GitBook help-center sections; Mintlify help-center guide) — a support answer corpus can be *deployed on* this Type's machinery, which is exactly why the market blurs the labels.
3. **vs Knowledge Base Application (§02.06).** KB's ratified center: the curated answer corpus and its authoring/ownership/review governance, audience-agnostic. This Type's center: product-usage corpus with release-coupled currency. Document360 straddles (self-labels KB software AND product documentation) — recorded as the market's straddling pole, consistent with the KB pass's own note.
4. **vs CMS / Headless CMS (§02.07).** CMS: typed content entries + presentation-agnostic repository for web content production. This Type: documentation corpus with doc-genre machinery (doc-tree navigation, whole-tree versioning, reference generation, doc-specific QA/analytics). Porous in one direction (Mintlify documents "headless docs with a custom frontend" — the docs platform offering a headless posture), but the center stays the doc corpus.
5. **vs Blogging Platform (§02.07).** Structure-organized tree vs time-ordered stream. The changelog is the dated exception that lives *inside* docs portals (ReadMe: changelog persists across versions; Mintlify: dated changelog entries with RSS) — a bounded chronology inside a structural corpus.
6. **vs Enterprise Wiki (§02.06).** Restricted producer-side authorship + deliberate publication pipeline vs open member editing + emergent link structure.
7. **vs API Documentation Platform (§12).** Central-artifact test inherited from the api-documentation-platform pass: that Type centers the definition-bound API reference; here an API reference is at most one section among many.
8. **What this Type is NOT:** a product-marketing site (content genre), a community forum (authorship direction), a learning/LMS platform (learner progression machinery absent), a static-site generator by itself (no managed portal machinery — the SSG is the code-first production substrate when combined with hosting/currency workflows).

## Historical / Market-Sample Check (conceptual — legacy vendors unreachable)

- **Paper-era product manual**: authored by the product team (corpus), bound book with table of contents/index (reader surface), revised and re-shipped with each product release (currency) — satisfies all three legs at analog level.
- **WinHelp/CHM/HTML-help era and printed PDF manuals**: same legs; compiled help with TOC + index + rebuild-on-release.
- The definition names no web-only surface (published reader-facing portal; web is the dominant realization, PDF/print an output variant), no AI, no cloud hosting, no specific versioning scheme. A single-current unversioned docs site satisfies the core (currency machinery ≠ versioning machinery; scheduled publishing/revision workflows suffice).
- Legacy dedicated help-authoring suites (single-sourcing → multi-channel output) would be a production-substrate variant; vendor evidence NOT fetched (403) — held unverified, no claims drawn.

## Escalation / Taxonomy Notes

- No directory change proposed from this side. The keep-both decision vs Developer Documentation Portal and Help Center follows the directory's precedent of genre/audience splits over shared machinery (online-marketplace/multi-vendor-marketplace; med-spa/appointment-business).
- If a future consolidation pass merges the documentation-platform family (PDP + DDP + API Documentation Platform), the recorded seams in this file and research/developer-documentation-portal.md are the arbitration basis.

## Uncertainties

- Mintlify versioned-docs support: not evidenced this pass; deliberately not claimed.
- ReadMe localization: not evidenced in fetched pages; localization marked 3/4.
- Legacy help-authoring pole (MadCap/RoboHelp class): unreachable; the historical check is conceptual only.
- Document360 PDF compilation verified at index-title strength only (page not opened).
- Market sizing/tier claims kept qualitative; no pricing/plan facts drawn beyond ReadMe's own FAQ statement (version counts by plan) which was observed but is a vendor plan detail (L3).

## Final Synthesis

A Product Documentation Portal is the managed system through which a product's own team authors, organizes, publishes, and keeps current the corpus that teaches the product's audience how to use it. Its defining structure is three jointly-held parts: the product-usage corpus of record, the published navigable reader surface, and the production-and-currency machinery binding the corpus to the product's evolution. Everything else — dual editors, review workflows, search/feedback/analytics, access control, branding, localization, AI assistants, versioning switches, PDF output — is standard, variant, or era machinery. The Type shares its machinery family with the Developer Documentation Portal (build-with corpus, developer audience) and overlaps in tooling with Help Centers and Knowledge Bases (problem-shaped answer corpora); the ratified seams are genre-and-audience, not machinery.
