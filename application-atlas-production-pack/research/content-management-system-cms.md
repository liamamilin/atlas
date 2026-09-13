# Research Notes — Content Management System / CMS

Research date: 2026-09-07
Leaf: `Content Management System / CMS` (DIRECTORY §02.07 Content Publishing)
Slug: `content-management-system-cms`

---

## Research Goal

Understand what a Content Management System actually is as an Application Type — from real products, not from marketing definitions — and establish:

1. the minimal defining structure (what makes a CMS a CMS and not something else),
2. the common mature structure layered on top,
3. the variant space (deployment, audience, headless drift),
4. sharp boundaries against the neighboring Types in the directory: Headless CMS, Blogging Platform, Website Builder (§04.16), Wiki Application, Enterprise Content Management (§10), News Publishing Platform (§27), Product Documentation Portal.

## Initial Boundary (hypothesis before research)

- A CMS is software where an organization **creates, structures, stores, and manages digital content items** through an editor-facing interface, and **assembles/delivers them as a web experience** (typically a website) under a controlled **publishing lifecycle**.
- The coupled presentation layer (the CMS owns the site as well as the content) is what separates CMS from Headless CMS.
- Neighbors to watch: Headless CMS (sibling leaf), Blogging Platform (sibling leaf), Website Builder, Wiki, ECM, News Publishing Platform.

## Research Questions

1. What is the unit of content in each product, and how is it structured (types, fields)?
2. Where does content live (repository, media library, taxonomy)?
3. What does the authoring experience look like (editors, forms, blocks, on-page editing)?
4. How does stored content become a delivered page (themes, templates, components, page tree)?
5. What is the publishing lifecycle (draft → publish → update → unpublish; versions; scheduling)?
6. What roles and permissions exist?
7. How do products extend (plugins/modules/extensions)?
8. Where do headless/API delivery, personalization, multi-site, and other modern capabilities sit — definitional or variant?
9. Where exactly are the boundaries with Headless CMS, Blogging Platform, Website Builder, Wiki, ECM?

## Representative Products

Selected for market representativeness + documentation completeness + different philosophies + different customer tiers:

| Product | Pole | Why selected |
|---|---|---|
| WordPress | dominant open-source web CMS, blog heritage, monolithic coupled | largest installed base; blog→CMS framing is vendor-documented |
| TYPO3 | older, regional (DACH), open-source enterprise CMS | historical/regional check; classic page-tree + content-element model |
| Adobe Experience Manager (AEM) | enterprise commercial suite (DXP) | enterprise tier; author/publish split; hybrid headless drift |
| Optimizely CMS (12) | mid/enterprise commercial, .NET heritage | commercial mid-market; page-type/property model |
| Ghost | publication-focused platform | boundary sample (blogging pole) |
| Contentful | headless CMS | boundary sample (headless pole) |

Drupal was originally intended as the structured open-source pole but its site returned a JavaScript client challenge on both attempts (see Sources — limitation). TYPO3 covers the classic structured open-source pole instead.

## Sources

Fetched 2026-09-07 (all official):

- WordPress (wordpress.org/documentation):
  - https://wordpress.org/documentation/ (docs root: Dashboard / Publishing / Media / Appearance / Blocks)
  - https://wordpress.org/documentation/overview/ (overview index)
  - https://wordpress.org/documentation/article/introduction-to-blogging/ (blog vs CMS framing)
  - https://wordpress.org/documentation/article/first-steps-with-wordpress-block-editor/ (admin screens, themes, plugins, posts/categories, block editor, publish flow)
- TYPO3 (docs.typo3.org):
  - https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/ (Editors Guide: page tree, content elements, records, media, languages, access control, FAL)
  - https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Concepts/Index.html (backend/frontend, extensions, TypoScript, Fluid, TCA)
- Adobe Experience Manager (experienceleague.adobe.com):
  - https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/introduction (AEM as a Cloud Service overview; roles)
  - https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/overview (three delivery paths: Edge Delivery / headless / traditional; author vs publish stores)
  - https://experienceleague.adobe.com/en/docs/experience-manager-65/content/sites/authoring/essentials/first-steps (authoring flow: page tree, components, publish/unpublish, versions, preview, page properties)
- Optimizely CMS (docs.developers.optimizely.com):
  - https://docs.developers.optimizely.com/content-management-system/docs (CMS 12 getting started)
  - https://docs.developers.optimizely.com/content-management-system/docs/learn-basic-editing (edit view, page tree, page types/properties, publish/schedule, blocks/media)
- Ghost (docs.ghost.org):
  - https://ghost.org/docs/ (docs index: platform guide, themes, Content API, JAMstack headless)
  - https://docs.ghost.org/product/ (product principles)
- Contentful (contentful.com):
  - https://www.contentful.com/developers/docs/concepts/ (domain model: organization/space/environment, content model, entries, assets, locales, releases)

**Source-access limitation:** drupal.org returned a JavaScript client challenge on both fetch attempts (2026-09-07). No Drupal-specific claims are made in these notes beyond market-context naming; no model-memory details were substituted. Assertion strength for the open-source structured pole rests on TYPO3 instead.

---

## Product Observations

### WordPress (evidence layer A — directly observed)

From official documentation (docs root, overview, Introduction to Blogging, First Steps with Block Editor):

- **Self-description**: "Software that manages your website is commonly called a CMS… Many blogging software programs are considered a specific type of CMS… WordPress is an advanced blogging tool." The vendor itself frames blogging as a subset of CMS.
- **Back end / front end split**: administration area ("back end", wp-admin) vs the public site ("front end"). Dashboard is the entry.
- **Admin navigation**: Dashboard, Posts, Media, Pages, Comments, Appearance, Plugins, Users, Tools, Settings.
- **Content units**: Posts (chronological, organized in Categories and Tags; category pages and date archives are generated views) and Pages (static content). Content is composed in the Block Editor ("type / to choose a block").
- **Presentation**: Themes ("presentation styles that completely change the look of your site"), template files, Widgets, Menus. Changing theme changes presentation, not content.
- **Publishing**: compose → Publish button (two-step confirm) → live on the internet "instantly". Update for edits.
- **Extensibility**: Plugins ("software scripts that add functions and events to your website"); Theme Developer Handbook for custom themes.
- **Users**: Users screen; roles and capabilities (administrator etc.).
- **Comments**: reader feedback with moderation and spam handling (Akismet shipped).
- **Media**: Media library section in admin.
- **Permalinks**: URL structure management.

### TYPO3 (evidence layer A)

From official Editors Guide + Getting Started Concepts:

- **Backend / frontend split**: "The backend in TYPO3 is the administrative interface where users manage content… The frontend… refers to the part of the website that visitors see."
- **Page tree**: hierarchical page structure is the primary organizing surface; page types and page properties.
- **Content elements**: content on a page is added as content elements (rich text editor, images, video, contact form are documented element types).
- **Records**: a general record module for structured data objects; clipboard, copy/paste, mass editing.
- **Media**: Media module; FAL (File Abstraction Layer) as the file machinery.
- **Languages**: working with multiple languages is a first-class editor task.
- **Access control**: restrict access to pages and content; backend users and groups; administrator role.
- **Presentation machinery**: TypoScript (frontend output configuration), Fluid (standard templating engine), site management (sites, redirects).
- **Extensions**: "an add-on module that enhances the core functionality of the CMS."
- **SEO**: SEO dashboard widgets; link management (redirects, short URLs, QR codes).
- **Caching**: cache as a documented concept for frontend delivery.

### Adobe Experience Manager (evidence layer A)

From official Experience League docs:

- **Positioning**: AEM Sites = "authoring, management, and delivery of digital experiences, be it through a web site, mobile app, or any other digital channel." AEM as a Cloud Service includes Sites + Assets; roles named: content authors, developers, system administrators, marketing professionals.
- **Authoring flow (First Steps for Authors)**: content held in a **tree structure** → navigate to location → **create a page** → open → **edit** by **inserting Components (Paragraph)**, edit/configure/copy/cut/delete/paste components, undo/redo, **Preview Mode** ("to see how it will look when published"), locking a page → **publish (activate)** the page; **unpublish (deactivate)** to remove from the public site; page properties; **create a version / revert to a version**.
- **Author/publish split**: authored content store = AEM Author (JCR); delivery = AEM Publish (JCR) with Adobe CDN + Dispatcher. Authoring and delivery are separated environments.
- **Three delivery paths** (current): Edge Delivery Services (document-based authoring / Universal Editor, HTML), Headless/API-first (Content Fragments, JSON over HTTP for SPAs/mobile), Traditional AEM (Page Editor, HTML). Headless is an additional channel, not a replacement.
- **Assets**: AEM Assets as the DAM layer (separate product area).

### Optimizely CMS 12 (evidence layer A)

From official developer docs:

- **Edit view**: global menu, navigation panel (page tree), assets panel, work area. On-page editing vs "All properties editing view" (form view with more properties).
- **Page types**: "A site comprises a set of *page types* with *properties* where editors add information. Each page type is created for a specific purpose, such as a standard page…, a product page, a login page… A page is an *instance* of a page type."
- **Other content types**: media (images, videos, documents) and **blocks** — "smaller information components that you can add to pages to provide content reuse and page layout flexibility."
- **Publishing**: changes continuously autosaved; a **draft version** is created; editors with sufficient access rights can **publish directly or schedule** later publishing.
- **Suite membership**: CMS integrates with Optimizely CMP and Configured Commerce (vendor positioning; suite context).

### Ghost (boundary sample — evidence layer A)

From official docs:

- Self-describes as building "independent publications"; platform guide, **theme guide** (custom designed templates), **Content API** ("accessing content in and out of Ghost programmatically"), **JAMstack** docs ("Use Ghost as a headless CMS").
- Product principles: publication platform; Ghost(Pro) hosting; members/payments are part of the product story (from docs index: migration of "content, members and payments").
- Interpretation: Ghost sits at the blogging/publication pole — a pre-shaped content model (posts) with themes and an optional headless API. It is a CMS-shaped product specialized for publications.

### Contentful (boundary sample — evidence layer A)

From official developer docs (domain model):

- Entities: organization → space → environment; content model ("a structure for content that consists of content types and defines connections between them"); entries; assets; locales; tags; releases (group entries/assets for simultaneous publishing); webhooks; apps; content preview (link to pre-production environment using Preview API for unpublished content).
- **No presentation layer**: delivery is via APIs (Delivery/Preview API keys). The web app is for authoring only.
- Interpretation: Contentful is the headless pole — content repository + authoring + API delivery, no site assembly. Confirms that removing the presentation layer yields a different product shape (the Headless CMS leaf).

---

## Cross-product Comparison

| Aspect | WordPress | TYPO3 | AEM | Optimizely CMS | Ghost | Contentful |
|---|---|---|---|---|---|---|
| Content unit | Posts / Pages (block content) | Pages + content elements + records | Pages + components; Content Fragments | Page types → page instances; blocks; media | Posts (publication-shaped) | Content types → entries |
| Structured typing | post types + fields (documented admin structure) | records + TCA field machinery | components/templates; fragments | page types with properties (explicit) | fixed publication model | content types (explicit, central) |
| Authoring surface | wp-admin + block editor | backend + Layout module + RTE | Page Editor (insert components, preview mode) | edit view (on-page + all-properties) | admin editor | web app entry editor |
| Site structure | pages + menus + archives | page tree | page tree | page tree | publication flow | n/a (no site) |
| Media | Media library | Media module + FAL | AEM Assets (DAM) | assets panel | images in posts | assets |
| Taxonomy | categories, tags | (records; categories via extensions) | tags | (categories via page structure) | tags/authors | tags |
| Publish lifecycle | draft → publish → update | editor workflow states (documented editor tasks) | draft → publish(activate) → unpublish(deactivate); versions; revert | autosave draft → publish / schedule | draft → publish | draft → published; releases |
| Presentation layer | themes + template files + widgets + menus | TypoScript + Fluid templates | AEM Publish (HTML) via templates/components | page types rendered by site | themes | **none (API only)** |
| Preview | (theme preview; live preview in editor) | (frontend preview) | Preview Mode | (on-page editing is live preview) | (preview) | Content Preview API |
| Roles | users + roles & capabilities | backend users + groups | author/admin/developer roles | access rights gate publishing | publication roles | roles per space |
| Extensibility | plugins | extensions | (bundles; not fetched) | (add-ons) | (integrations) | apps |
| Headless/API | (not in fetched docs) | (not in fetched docs) | JSON over HTTP (one of three paths) | (not in fetched docs) | Content API / JAMstack | API-only |
| Deployment | self-hosted open source (+ .com hosted sibling) | self-hosted open source | cloud service (vendor-operated) | self-managed/.NET + cloud offerings | open source + hosted | SaaS |

### Stable commonalities (evidence layer B — cross-product)

1. **Structured content items in a managed repository** — every product stores content as discrete, typed items (posts/pages, content elements/records, pages+components/fragments, page-type instances/blocks, posts, entries), not as loose files.
2. **Editor-facing authoring surface distinct from the public site** — every product has an admin/backend/edit view where non-developers work; TYPO3 and WordPress name the backend/frontend split explicitly; AEM and Optimizely separate author store from delivery store.
3. **Presentation machinery that assembles stored content into delivered pages** — themes/template files (WordPress), TypoScript/Fluid (TYPO3), templates/components (AEM), page types rendered by the site (Optimizely), themes (Ghost). Contentful is the counter-case: no presentation layer → headless.
4. **Publishing lifecycle with a visibility switch** — draft/work-in-progress vs published; publish/unpublish (AEM's activate/deactivate), publish/schedule (Optimizely), publish button (WordPress), releases (Contentful). Versions/revisions for rollback (AEM versions; draft versions in Optimizely).
5. **Media library** — all products manage images/video/documents as reusable assets.
6. **Roles/permissions** — all products gate who can edit and who can publish.
7. **Extensibility** — plugins/extensions/apps as the standard way to add capability.

### Where products differ (implementation, not definition)

- Unit granularity: page-centric (TYPO3, AEM, Optimizely) vs entry/post-centric (WordPress, Ghost, Contentful).
- Where structure is defined: developer-defined page types (Optimizely), admin-defined content types (Contentful), code-defined templates (AEM), plugin-defined post types (WordPress).
- Delivery topology: single system (WordPress/TYPO3 self-hosted) vs author/publish split (AEM) vs API-only (Contentful).
- Structure-first vs content-first philosophy: Optimizely/Contentful make the type model explicit and central; WordPress/Ghost start from posts and generalize.

---

## Canonical Abstraction

### L0 — Defining Invariant (minimal)

A CMS is recognizable as a CMS if and only if all four hold:

1. **Structured content items** — content exists as discrete, typed, field-structured items stored persistently in a managed repository (not as loose files, not as raw code).
2. **Editor-facing authoring interface** — non-developers create and edit those items through forms/editors in an administrative surface.
3. **Coupled presentation layer** — the same system assembles stored content into delivered web pages (a site) through templates/themes/components; the CMS owns both the content and its site delivery.
4. **Publishing lifecycle** — items move through managed states (work-in-progress → published → updated/archived), and the published state controls public visibility.

Remove tests:
- Remove #3 → Headless CMS (different Type).
- Remove #1 (keep only visual page construction) → Website Builder.
- Remove #2 (keep repository + delivery, authoring by code) → web framework / static site generator.
- Remove #4 (everything immediately public, no publish state) → wiki-like collaborative surface.
- Replace #1's "structured items" with "organizational documents/records" → Enterprise Content Management.

Historical check (§24): early-2000s web CMS (TYPO3 heritage, Day CQ heritage, early WordPress) all satisfy these four; modern hybrids still satisfy them. The definition does not depend on blocks, plugins, cloud, or headless APIs.

### L1 — Common Mature Structure

- media library / asset management (DAM-lite)
- taxonomy (categories/tags) and metadata
- revisions/versioning with rollback
- navigation/menu management
- rich-text or block-based editing
- preview before publish
- scheduled publishing
- user roles with edit-vs-publish separation
- SEO surfaces (meta, sitemaps, redirects, friendly URLs)
- multilingual content
- extensibility ecosystem (plugins/modules/extensions)
- site search / admin search
- forms (contact forms as content elements)

### L2 — Variant / Optional Structure

- headless/API delivery as an additional channel (hybrid CMS)
- author/publish environment split, staging environments
- editorial workflow with approval chains
- personalization/experimentation (enterprise DXP territory)
- multi-site management
- e-commerce integration
- comments/community features; membership/payments (publication pole)
- AI assistance (era-current)
- deployment posture: self-hosted open source / vendor SaaS / cloud service
- content reuse across channels (structured fragments)

### L3 — Vendor-specific (research notes only)

- WordPress: wp-admin path, Block Editor ("type / to choose a block"), two-step publish confirm, Twenty Twenty-Two default theme, Widgets, Akismet anti-spam shipped, 5-minute install, WordPress.org vs WordPress.com split, permalinks screen.
- TYPO3: TypoScript (frontend output configuration language), TSconfig (backend configuration), TCA (Table Configuration Array defining table/field structure), FAL (File Abstraction Layer), Layout module, clipboard/mass editing, Introduction Package, site management (redirects, short URLs, QR codes), SEO dashboard widgets.
- AEM: JCR as content store, Author/Publish + Dispatcher + Adobe CDN, Edge Delivery Services (document-based authoring, Universal Editor), Content Fragments, Core Components, Editable Templates, WKND tutorial, Cloud Manager CI/CD, AEM Assets as separate DAM area, page locking.
- Optimizely: page types/properties model ("a page is an instance of a page type"), Alloy sample site, `episerver` login path, on-page editing vs All Properties view, autosave draft versions, CMP/Configured Commerce integration.
- Ghost: Ghost(Pro) hosting, members/newsletters/payments, Handlebars themes, Content API, JAMstack headless positioning, non-profit governance model.
- Contentful: organization/space/environment hierarchy, environment aliases, sandbox environments, locales as entities, releases, webhooks, apps (Tasks/Workflows), Preview API.

---

## Vendor-specific Findings

- WordPress's own documentation explicitly frames the blog⊂CMS relationship ("Many blogging software programs are considered a specific type of CMS") — useful boundary evidence from the vendor itself.
- AEM documents three coexisting delivery paths (Edge Delivery, headless JSON, traditional HTML) — evidence that headless is a delivery channel variant, not a replacement for the CMS Type.
- Optimizely's "page is an instance of a page type" is the cleanest vendor formulation of the type/instance structure that all sampled products share in some form.
- Contentful's domain model (space/environment/entries/assets/locales/releases) shows what a CMS looks like when the presentation layer is removed — the mirror image that defines the Headless CMS boundary.

## Boundary Findings

| Neighbor Type | Shared surface | The seam (remove X → becomes neighbor) |
|---|---|---|
| Headless CMS | content types, entries, authoring, media, API delivery | Remove the coupled presentation layer (site assembly + site delivery); deliver only via API → Headless CMS. Modern CMS products add API channels (hybrid), but the coupled site remains the defining surface of CMS. |
| Blogging Platform | posts, chronological views, themes, comments | Remove general content-type modeling and whole-site ownership; pre-shape everything for chronological publication → Blogging Platform. WordPress's own docs call blogging software "a specific type of CMS". |
| Website Builder | visual page editing, templates, published site | Remove the structured content repository (typed items reused across pages, queried/listed dynamically); keep only visual page construction → Website Builder. |
| Wiki Application | web content, editing by non-developers, history | Remove the publish lifecycle and the separate presentation layer; pages are the deliverable, edited in place → Wiki. |
| Enterprise Content Management (§10) | repositories, metadata, permissions, lifecycle | Replace web content items + page assembly with organizational documents/records and retention/compliance → ECM. |
| News Publishing Platform (§27) | editorial workflow, publishing | Specialize the content model and workflow for newsroom production → News Publishing Platform; CMS is the general substrate. |
| Product Documentation Portal (§02.07) | structured content, publishing | Specialize for versioned product documentation delivery → Documentation Portal. |
| DAM | media assets | CMS includes a media library as one capability; DAM is asset-centric as the whole product. |

## Uncertainties

- Drupal could not be fetched (JS challenge ×2). The open-source structured pole rests on TYPO3. Drupal-specific claims were not made.
- Exact workflow state names (draft/review/published) were not fetched in detail for WordPress/TYPO3; lifecycle claims are kept abstract (work-in-progress → published → updated/archived).
- AEM Edge Delivery Services is recent; treated as vendor-specific delivery posture, not a Type-level structure.
- No numeric limits, prices, or default settings are asserted anywhere (none were needed; none were reliably sourced).
- Ghost's exact role model was not fetched; Ghost is used only as a boundary sample.

## Final Synthesis

The CMS Type is best modeled as: **a managed repository of structured content items, authored by non-developers through an administrative interface, assembled into a delivered website by a coupled presentation layer, and moved through a controlled publishing lifecycle.**

Everything else commonly associated with CMS products — media libraries, taxonomy, revisions, menus, SEO, multilingual, plugins, headless APIs, personalization, multi-site, AI — is common mature structure or variant structure, not definition. The sharpest boundary is with Headless CMS (remove the coupled presentation layer) and Website Builder (remove the structured content repository); the historical check confirms the four-part definition holds for older, regional, and platform-native products as well as modern hybrids.
