# Research Notes — Headless CMS

Research date: 2026-09-07
Methodology: WORKFLOW v1.1 (10-step), evidence layers A/B/C, L0–L3 abstraction.

---

## Research Goal

Understand, from real products, what a Headless CMS is: its defining structure, its core objects, how content flows from authoring to delivery, and where its boundary lies against the coupled Content Management System / CMS, DAM, blogging platforms, and headless commerce engines.

## Initial Boundary (hypothesis before research)

- A Headless CMS manages structured content in a repository that is decoupled from presentation ("the head"), and delivers content to any frontend through APIs.
- Nearest neighbors: Content Management System / CMS (coupled rendering), Blogging Platform (owned presentation), Digital Asset Management (asset-centric), Headless Commerce Platform (transaction-centric), API/backend platforms.
- Main risk of over-fitting: defining the Type by the current SaaS API-first generation and missing older, self-hosted, or hybrid products.

## Research Questions

1. What objects make up the content model (types, fields, components/blocks)?
2. What is the unit of content (entry/document/story) and how does it relate to the model?
3. How does the editorial lifecycle work (draft → review → publish → versions → unpublish)?
4. How is content delivered (REST/GraphQL, CDN, preview APIs, webhooks)?
5. What do developers configure vs what do editors author (the division of labor)?
6. What roles, permissions, and API credentials exist?
7. How are media/assets handled, and how do they relate to entries?
8. How do containers work (spaces/projects/datasets/environments)?
9. Where is the boundary vs coupled CMS, DAM, blogging platform, headless commerce?
10. Do visual-editing hybrids (preview overlays) break the "no owned presentation" property?

## Representative Products

| Product | Philosophy | Customer tier | Delivery model |
|---|---|---|---|
| Contentful | API-first content platform, enterprise | Enterprise | SaaS |
| Sanity | Developer-first, schema-as-code, customizable studio | Dev-led teams, startup→enterprise | SaaS (hosted data; studio self-hostable) |
| Strapi | Open-source, self-hosted admin + content APIs | Dev-led teams, SMB→enterprise | Self-hosted (npm) or vendor cloud |
| Storyblok | Component-based headless with visual editor | Marketing-led + dev teams, SMB→enterprise | SaaS |

Sample covers: enterprise SaaS pole, developer-first pole, open-source self-hosted pole, editor-friendly visual pole. All four official documentation sets were directly fetched (evidence layer A throughout).

## Sources

- Contentful Developers Docs — Domain model: https://www.contentful.com/developers/docs/concepts/
- Contentful Developers Docs — Data model: https://www.contentful.com/developers/docs/concepts/data-model/
- Contentful Developers Docs — API basics: https://www.contentful.com/developers/docs/concepts/apis/
- Contentful Help Center — Content modeling basics: https://www.contentful.com/help/content-models/content-modelling-basics/
- Contentful Help Center — Web app overview: https://www.contentful.com/help/getting-started/contentful-web-app-overview/
- Contentful Developers Docs — Content Management API reference (spaces): https://www.contentful.com/developers/docs/references/content-management-api/
- Sanity Docs — Content Lake: https://www.sanity.io/docs/content-lake
- Sanity Docs — Documents: https://www.sanity.io/docs/content-lake/documents
- Sanity Docs — Datasets: https://www.sanity.io/docs/content-lake/datasets
- Sanity Docs — Studio: https://www.sanity.io/docs/studio
- Strapi 5 Docs — Models: https://docs.strapi.io/cms/backend-customization/models
- Strapi 5 Docs — Draft & Publish: https://docs.strapi.io/cms/features/draft-and-publish
- Strapi 5 Docs — Content APIs: https://docs.strapi.io/cms/api/content-api
- Storyblok Docs — Content Modeling: https://www.storyblok.com/docs/concepts/content-modeling
- Storyblok Docs — Visual Editor: https://www.storyblok.com/docs/concepts/visual-editor
- Storyblok Docs — Stories manual: https://www.storyblok.com/docs/manuals/stories
- Storyblok Docs — Spaces manual: https://www.storyblok.com/docs/manuals/spaces

All sources fetched live on 2026-09-07. No source-access limitation to record; assertion strength is calibrated to direct documentation evidence.

---

## Product Observations

### Contentful (evidence layer A unless noted)

- **Domain model**: four main entity types — user, organization, space, environment. Organization = company account (billing, user grouping); space = container for all content and media of a project with its own content model; environment = version of space-specific data changed in isolation (master + sandbox environments); environment aliases point to a target environment and can be switched.
- **Content model**: "A content model gives structure and organization to your content"; content types are the "stencil" for entries; each content type made of fields with types, validations, and appearance settings. Modeling is explicitly contrasted with traditional CMSs: "your content doesn't have to fit into our model. Instead, you make the model fit your pieces of content." Developers design the model; editors are its end users.
- **Fields** (data model page): Symbol (short text), Text (long), RichText, Integer, Number, Date, Location, Boolean, Media (Link to asset), Reference (Link to entry), Array (of symbols or links), JSON Object. Field-level validations (required, regex, ranges, allowed content types) and appearance (editor widget) are configurable. Fields can be hidden from editors or omitted from API responses; field deletion is a two-step process (disable in API response first).
- **Entries & assets**: entries are items of content based on a content type; assets are binary files (images, videos, documents) with fixed fields (name, description, file). Assets are published like entries; embargoed assets exist; DAM services integrate as an alternative.
- **APIs**: Content Delivery API (read-only, CDN-hosted, JSON), Content Management API (read-write, user-authenticated; the web app itself is built on it), Content Preview API (CDA variant including unpublished content), Images API (resize/crop/convert), GraphQL Content API (per-space schema regenerated when content types change).
- **Web app**: Content tab (entries list, search/filter, saved views, bulk actions, scheduled content), Entry editor (fields, status/publish, tasks, preview, links, translation, versions, references, tags), Media tab + Asset editor, AI & Automations tab, space selector (organization → space → environment).
- **Lifecycle**: draft editing, publish/unpublish, scheduled publishing, versions with compare/revert, releases (group entries+assets for simultaneous publishing; Timeline/Launch apps), locale-based publishing.
- **Governance**: organization roles + space roles with custom roles, allow/deny rules, content permissions (incl. tag-based); teams; API keys per space; webhooks (HTTP callbacks on data change); tags and taxonomy for governance.
- **Extensibility**: Apps (Marketplace), App Framework, Functions, Automations, AI Actions; cross-space references; native/custom external references (Shopify, commercetools, Cloudinary).
- Vendor-specific (L3): spaces/environments/aliases naming, the five-API split, 50-fields-per-content-type limit, embargoed assets, Experiences (visual page builder), Personalization suite.

### Sanity (evidence layer A)

- **Content Lake**: hosted datastore storing content as structured JSON documents — "queryable, referenceable, and ready for delivery to any channel."
- **Documents**: JSON documents with system metadata (`_id`, `_type`, `_createdAt`, `_rev`…). "The document store doesn't know about your schema" — schema lives in the customer's code; document types are defined in schema configuration and "are the foundation of your content model."
- **Document variants**: published documents (non-prefixed ID), drafts (ID prefixed `drafts.`, visible only to authenticated users), versions (ID prefixed `versions.<release>.`, tied to Content Releases). Publishing applies draft/version contents to the published document and deletes the draft; unpublish deletes the published document and recreates a draft. Implied lifecycle states: created/updated/deleted; these events trigger Functions and Webhooks.
- **References**: reference fields create relationships between documents — "one of the core features of structured content and page-building"; "connected content" enables reusing the same chunk of content in different contexts.
- **Assets**: asset documents (`sanity.imageAsset`, `sanity.fileAsset`) with storage/resize/deletion API.
- **Datasets**: a dataset is a collection of JSON documents — "a 'database' where all of your content is stored, whereas the document's types would constitute 'tables'"; queryable via GROQ or GraphQL within, not across, datasets; typical uses: test/staging/production environments, segmentation. Public vs private datasets; export/import; cloud clone and hot-swap (paid).
- **Studio**: "an open-source, real-time collaborative content workbench where developers define content models using JavaScript objects. The Studio automatically generates a powerful editing environment based on these definitions," customizable via a React framework. Visual Editing adds shareable live previews and click-to-edit. Comments, Tasks, Dashboard, Content Releases, AI Assist.
- **Delivery**: GROQ query language, GraphQL API, API CDN (cached), Live Content API (real-time), perspectives (same query evaluated against published or draft state).
- Vendor-specific (L3): GROQ, dataset naming rules, perspectives, add-on datasets (comments/tasks), private datasets, `sanity.config.ts` schema-as-code.

### Strapi (evidence layer A)

- **Self-description**: "As Strapi is a headless Content Management System (CMS), creating a content structure for the content is one of the most important aspects of using the software."
- **Models**: content-types (collection types or single types) + components (reusable content structures). Created via the Content-type Builder in the admin panel or the CLI; stored as schema files in the project (`schema.json`), reviewable at code level.
- **Schema**: settings (kind, table name), info (display/API names), attributes (scalar types; Strapi-specific: `media`, `relation`, `customField`, `component`, `dynamiczone`, i18n `locale`/`localizations`), validations (required, min/max, length, unique, private), options (draftAndPublish default true for UI-created types).
- **Relations**: oneToOne, oneToMany, manyToOne, manyToMany; unidirectional or bidirectional.
- **Dynamic zones**: "a flexible space in which to compose content, based on a mixed list of components" — the page-composition primitive.
- **Draft & Publish**: per-content-type feature (available but disabled by default in v5). Statuses: Published / Modified / Draft. Draft tab editable, Published tab read-only. Publish, save, discard; unpublish with "keep last draft" or "replace last draft"; bulk publish with per-entry validation checks ("Ready to publish" vs field errors); scheduled publication via Releases. Reserved attribute name `status` when enabled. API access via `status` parameter and `publicationFilter`.
- **Content APIs**: REST (default) and GraphQL (plugin) for frontends; Document Service API (`strapi.documents`) for backend/plugins — handles documents ("an API-only concept which represents all the variations of content (for different locales, for the draft and published versions) for a given entry"); Query Engine API (`db.query`) as low-level database layer.
- **Platform features** (docs nav): API tokens, admin tokens, audit logs, content history, custom fields, data management, email, i18n, media library, MCP server, preview, RBAC, releases, review workflows, SSO, users & permissions, webhooks, lifecycle hooks, plugins marketplace.
- Vendor-specific (L3): Content-type Builder, dynamic zones, Document Service vs Query Engine split, lifecycle hooks, Draft&Publish disabled-by-default, reserved `status` attribute, self-hosted Node.js deployment.

### Storyblok (evidence layer A)

- **Content model**: "Content modeling is the process of identifying and structuring the various types of content that a project will contain." Three basic data types: Fields (individual inputs), Blocks (configurable content elements), Stories (complete content entries). Two schemas: Components (block schemas) and Content types (story schemas); "content types are a subset of components." Stakeholders: editors, developers, designers, marketing.
- **Stories**: "a story is a way to store information. Each story represents a unique piece of content or configuration, like an article, a landing page, or even a navigation menu." Stories are made of blocks; each story based on a content-type template; unique slug required; organized in folders (hierarchical, e.g. per language) and tags (thematic); search/filter/sort; favorites; trash-bin app for soft delete.
- **Spaces**: "a space is a flexible content repository for your project. Each space stores distinct stories, blocks, assets, datasources, and configurations (for example, workflows, users, roles, access tokens)." Server location choice (EU/US/Canada/Australia; dedicated China infra); content distributed via CDN regardless. Multi-space setups for team/language/environment separation; space duplication; cross-space linking not supported (web links instead).
- **Visual Editor**: WYSIWYG editing embedded in the Visual Editor with "complete freedom to customize both the website's backend and frontend." The editor loads the actual frontend in an iframe; draft content is fetched with an `_editable` property per block; a preview bridge (StoryblokBridge) connects editor and page; click a block in preview to open it in the editor and vice versa; changes reflect in real time. Preview URL configured per space; validation token parameters; HTTPS/CSP requirements.
- **Model building**: Block Library GUI for non-technical iteration, or Management API + CLI for version-controlled schemas across spaces (dev/staging/prod).
- **Other concepts** (docs index): Access Tokens, Assets, Backups, Blocks, Blueprints, Caching, CMS Migration, Datasources, E-commerce, Experiments, Fields, FlowMotion, Internationalization, References, Roles, SSO and SCIM, Visual Editor, Webhooks.
- Vendor-specific (L3): stories/blocks/content-type terminology, `_editable`/bridge mechanics, datasources, blueprints, FlowMotion, trash bin app, shared components app.

---

## Cross-product Comparison

| Dimension | Contentful | Sanity | Strapi | Storyblok | Reading |
|---|---|---|---|---|---|
| Top container | Organization → Space → Environment | Project → Dataset | Project (self-hosted instance) | Space | B: every product partitions content into named containers; naming/structure varies |
| Content model | Content types + typed fields + validations + appearance | Schema-as-code (document types + fields) | Content-types + components + dynamic zones (GUI or code) | Components + content types (GUI or Management API/CLI) | B: customer-defined model of typed content types is universal |
| Unit of content | Entry | Document (JSON) | Entry / Document (all variations) | Story (composed of blocks) | B: same concept, different names |
| References | Reference/Link fields (entries, assets; cross-space & external) | Reference fields ("connected content") | Relation fields (1:1, 1:N, N:M) | Reference fields | B: relationships between entries are core |
| Media | Assets (name/description/file), Images API, DAM integration | Asset documents + asset API | Media Library | Assets | B: asset store attached to the content repository |
| Draft/publish | Draft → publish/unpublish; scheduled; releases | Drafts./versions. prefixes; publish applies draft | Draft & Publish per type (statuses Draft/Modified/Published) | Draft version + publish; visual editor edits draft | B: two-state (draft vs published) content with publish as the delivery gate |
| Delivery API | CDA (read-only, CDN) + GraphQL + Preview API | GROQ/GraphQL + API CDN + Live API | REST (default) + GraphQL (plugin) | Content Delivery API (draft/published versions) | B: read API for published content is the primary delivery surface |
| Management API | CMA (web app built on it) | Mutations/Actions API | Document Service API + REST writes | Management API | B: programmatic write surface exists in all |
| Webhooks | Yes (on data change) | Yes (lifecycle-triggered) | Yes | Yes | B: change notification to external systems is standard |
| Editorial UI | Web app (Content/Media tabs, entry editor) | Studio (auto-generated from schema, customizable) | Admin panel (Content Manager, Content-type Builder) | App (Content section, Visual Editor) | B: all ship an editor-facing application |
| Preview | Preview API + live preview in entry editor | Visual Editing (live preview, click-to-edit) | Preview feature | Visual Editor (iframe of real frontend) | B: draft content rendered in the external frontend |
| Localization | Locales (region-language), field/entry-level, locale-based publishing | (documented via i18n patterns; not fetched in detail) | i18n plugin (locale/localizations attributes) | Field- and folder-level translation | B: multi-language content is standard; mechanism varies |
| Roles/credentials | Org roles + space roles (custom, allow/deny), API keys | Project members; private datasets; tokens | RBAC, users & permissions, API tokens | Roles, access tokens, SSO/SCIM | B: role-gated editorial access + API credentials |
| Environments | Environments + aliases in a space | Datasets in a project (staging/prod) | Separate instances (self-host) | Separate spaces (or field-level translation) | B: isolation of model+content changes before production |
| Extensibility | Apps marketplace, App Framework, Functions, Automations, AI Actions | Studio React customization, plugins, Functions, AI Assist | Plugins, custom fields, lifecycle hooks, MCP server | Apps, CLI, Management API, FlowMotion | B: extension surface is common; form varies |
| Delivery model | SaaS | SaaS data + self-hostable studio | Self-hosted OSS or vendor cloud | SaaS | C-variant: packaging varies, model identical |

### Evidence-layer notes

- All product observations above are Layer A (directly observed in official docs on 2026-09-07).
- Cross-product claims (the "Reading" column) are Layer B.
- The canonical abstraction below is Layer C.

---

## Canonical Abstraction

### L0 — Defining Invariant

A Headless CMS is recognizable by exactly this structure:

1. **Customer-defined content model** — a schema of content types, each with typed fields and validation rules, defined by the implementing team (developers in all sampled products) and independent of any page design. Remove → generic database or fixed-template CMS.
2. **Structured content entries as the system of record** — items of content created and stored against that model (with relationships between entries and attached media assets), not pages. Remove → asset library (DAM) or file store.
3. **API-first delivery of published content** — consuming applications retrieve content programmatically (read API over published content; management API for writes); the API is the primary delivery surface. Remove → coupled CMS that renders pages.
4. **Presentation decoupled** — the end-user experience is rendered by frontends built outside the product; the product does not own page rendering as its delivery surface (any shipped preview/visual tooling renders the external frontend, it does not replace it). Remove → traditional/coupled CMS.

Historical check (§24): early API-first headless products (Contentful generation, 2013+), self-hosted generation (Strapi generation), and schema-as-code products all satisfy this structure; a git-based CMS managing structured content files for static-site builds would also satisfy the model (content model + entries + programmatic delivery + external rendering) — not directly sampled, recorded as unverified in Uncertainties. The definition does not depend on SaaS, CDN, GraphQL, or visual editing.

### L1 — Common Mature Structure

Present in essentially all mature products; makes the Type practical but does not define it:

- **Editorial application** — a web surface for editors: content list with search/filter/saved views, entry editor (fields per content type), media library, bulk actions.
- **Draft/publish lifecycle** — draft editing separated from published content; publish as the explicit gate to the delivery API; unpublish; version history with compare/revert.
- **Scheduled publishing and releases** — time-based publication; grouping multiple entries/assets for simultaneous publish.
- **Preview** — draft content rendered in a preview deployment of the external frontend (preview API or visual editing).
- **Localization** — locale definitions with per-field or per-entry translation; locale-aware publishing.
- **Roles, permissions, and API credentials** — editorial roles (edit vs publish separation), admin roles, API keys/tokens for delivery and management.
- **Webhooks** — HTTP notifications on content change, typically consumed to rebuild frontends or sync systems.
- **References / connected content** — typed relationships between entries; reusable content chunks.
- **Rich text / structured rich text fields** — long-form content as structured data rather than HTML blobs.
- **Environments/containers for isolation** — staging vs production data isolation (environments, datasets, or separate instances).
- **SDKs/client libraries** — first-class libraries for the delivery and management APIs.
- **Search/filter over content** — editorial search; sometimes API-level query/search.

### L2 — Variant / Optional Structure

Depends on segment, deployment, business model:

- **Delivery model**: pure SaaS vs open-source self-hosted vs hybrid (hosted data + self-hosted studio).
- **Visual editing depth**: preview overlays (click-to-edit on the real frontend) vs no visual surface; page-composition features (block-based page building, dynamic zones, visual experience builders) — the drift boundary toward Visual Website Builder.
- **AI assistance**: AI content generation/actions, AI tagging, AI assistants (current-market common, not definitional).
- **Workflow/review machinery**: review workflows, tasks, comments, approvals.
- **Governance depth**: tags/taxonomy governance, audit logs, SSO/SCIM.
- **Ecosystem**: app/plugin marketplaces, integration catalogs (commerce, DAM, translation, analytics).
- **Commerce adjacency**: external references to commerce platforms; e-commerce field packs.
- **Real-time delivery**: live/streaming content APIs for fast-moving content.
- **Data residency / region choice**: EU residency, server-region selection.

### L3 — Vendor-specific (Research Notes only)

- Contentful: space/environment/alias hierarchy; the five-API split (CDA/CMA/CPA/Images/GraphQL); 50-field limit per content type; embargoed assets; Experiences; Personalization; Launch/Timeline; cross-space references.
- Sanity: Content Lake; GROQ; datasets with public/private modes; perspectives; Live Content API; Studio as customizable React app; add-on datasets; cloud clone/hot swap; `sanity.config.ts`.
- Strapi: Content-type Builder; dynamic zones; Document Service vs Query Engine APIs; lifecycle hooks; Draft&Publish disabled by default; reserved `status` attribute; Node.js self-hosting; MCP server.
- Storyblok: story/block/content-type terminology; Visual Editor bridge (`_editable`, preview token params); datasources; blueprints; FlowMotion; trash bin app; shared components app; server-location choice.

---

## Vendor-specific Findings

See L3 above. None of these were promoted into the canonical model. Notable near-misses that were deliberately kept out of L0/L1:

- **GraphQL**: 3 of 4 sampled products offer a GraphQL API (Contentful, Sanity, Strapi-via-plugin); Storyblok's documented delivery API is REST-style. Kept as common implementation, not core.
- **Visual editing**: present in all four in some form, but implemented very differently (iframe bridge vs preview API vs click-to-edit). The conceptual constant is "preview draft content in the external frontend," which is L1; the visual-editing depth is L2.
- **Environments**: the *need* for staging isolation is common, but the mechanism differs (environments vs datasets vs separate instances vs spaces). Kept at L1 as "isolation containers," mechanism-level detail in L3.

## Rejected Findings

- "A Headless CMS has no UI" — rejected. All sampled products ship a substantial editorial application. "Headless" refers to the delivery posture (no owned presentation layer), not the absence of tooling.
- "A Headless CMS is defined by REST/GraphQL JSON APIs" — too implementation-specific. The invariant is programmatic API delivery; protocol and format vary.
- "Content must be cloud-hosted" — rejected (Strapi self-hosted satisfies the model).
- "Page building is part of the Type" — rejected. Block/page composition is a common extension (L2) and a drift boundary toward Visual Website Builder.
- "A CDN is part of the definition" — rejected. CDN delivery is the common modern implementation of the read API, not the invariant.

---

## Boundary Findings

| Neighbor Type | Relationship | Discriminator ("remove what → becomes the other") |
|---|---|---|
| Content Management System / CMS (coupled) | sibling under 02.07; the sharpest seam | If the product's primary delivery surface is pages it renders itself (templates/themes), it is a coupled CMS. A coupled CMS exposing a content API gains a *headless mode*; the Type describes products whose defining posture is the decoupled repository. Remove API-first delivery + external rendering → coupled CMS. |
| Blogging Platform | adjacent | Blogging platform owns the presentation (themes, hosted pages) and is end-user-facing; a headless CMS has no owned presentation and serves developer-built frontends. |
| Digital Asset Management (DAM) | adjacent; integration seam | DAM's system of record is media assets with rich asset lifecycle; headless CMS's system of record is structured content entries, with assets as a supporting object. Contentful documents "working with a DAM service" as an integration — evidence of the seam. Remove entries/model → DAM. |
| Headless Commerce Platform | structural sibling (same decoupling pattern, different domain) | Commerce engine's objects are products/carts/orders/payments; headless CMS's objects are content entries/assets. They integrate (external references to commerce platforms documented in Contentful). |
| API/backend platform (BAAS, database) | adjacent | A generic data platform lacks the content model + editorial lifecycle + publishing semantics; a headless CMS is content-shaped. Remove content-model/editorial intent → BAAS. |
| Product Documentation Portal / Help Center | downstream consumer | Those are published output surfaces; a headless CMS can be their backend. |
| Visual Website Builder | drift boundary | When block/page composition becomes the primary surface and the platform starts owning rendering/hosting of the end-user page, the product drifts out of this Type. |

Taxonomy note: Headless CMS and Content Management System / CMS are separate leaves under 02.07. The research supports keeping both as distinct Types (delivery-posture discriminator). No directory change proposed.

---

## Uncertainties

- **Git-based / static CMSs** (content files in a repo, build-time delivery) plausibly satisfy the L0 model but were not sampled; recorded as unverified rather than asserted.
- **Sanity localization mechanics** were not fetched in detail (only inferred from the docs index); localization is asserted at L1 from the other three products plus Sanity's general model, with Sanity-specific mechanics left unstated.
- **Sanity roles/permissions detail** not fetched; roles asserted at L1 from cross-product commonality (Contentful, Strapi, Storyblok direct evidence).
- **Market-share / positioning claims** deliberately not made; no pricing or usage numbers were researched.
- **Decoupled/hybrid CMS products** (coupled CMSs used headless) straddle the boundary; the document handles this via the delivery-posture discriminator rather than a hard product list.

---

## Final Synthesis

A Headless CMS is a content management system whose defining posture is the separation of content management from content presentation. Its world model has four load-bearing structures: a customer-defined content model (content types with typed fields), structured content entries stored against that model together with media assets and entry-to-entry references, programmatic delivery of published content through read APIs consumed by externally built frontends, and programmatic management through management APIs — with the end-user presentation layer deliberately built outside the product.

Around this core, mature products converge on a stable operational pattern: developers define and evolve the model (in a GUI, in code, or both); editors author content in an editorial application (entry editor, media library, content lists); content moves through a draft → preview → publish lifecycle (with versions, scheduling, releases, and unpublish); published content is delivered via CDN-hosted read APIs (REST and/or GraphQL); webhooks notify external systems to rebuild or sync; localization, roles, and environment isolation scale the operation.

The Type's identity lives in the decoupling, not in any specific technology: not in REST vs GraphQL, not in SaaS vs self-hosted, not in the presence of a visual editor. The sharpest boundary is with the coupled CMS (which renders pages as its delivery surface); the clearest drift is toward visual website building when page composition and rendering become the product's own surface.
