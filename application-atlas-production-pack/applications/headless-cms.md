# Headless CMS

## Overview

A **Headless CMS** is a content management system that stores and manages structured content in a repository that is deliberately decoupled from presentation. Content is created against a customer-defined content model, and delivered to websites, apps, and other digital channels through APIs — while the end-user-facing interface (the "head") is built outside the product by the consuming team.

It solves a specific problem: organizations whose content must flow into multiple, independently built digital properties (websites, mobile apps, kiosks, in-store screens) need a single place where content is structured, authored, reviewed, and published — without that place also owning how pages look. A traditional CMS couples the content repository with page rendering; a headless CMS removes the rendering half and exposes the repository through APIs instead.

The defining structure is small:

```text
Content model (content types with typed fields — defined by the customer)
└── Content entries stored against the model
    ├── References between entries
    └── Media assets
        ↓ delivered as
Read APIs (published content)  ← consumed by  →  External frontends (built outside)
Management APIs (create/update/publish)
```

Everything else commonly associated with the category — CDN delivery, GraphQL, visual editing, AI assistance, app marketplaces — is widespread in current products but is not what makes the product a headless CMS.

## Users & Context

Three user groups with a clear division of labor:

- **Developers** — define and evolve the content model, build the frontends that consume the content, and integrate the APIs. In every researched product the content model is a developer-owned artifact (configured in a GUI, written in code, or both).
- **Content editors / authors** — the daily users. They create and edit entries, upload media, link content together, translate, preview, and publish. They work entirely inside the product's editorial application and never see the frontends' code.
- **Content managers / admins** — configure roles and permissions, manage locales, environments, API keys, and webhooks, and often own review workflows and publishing governance.

Typical context: a digital team where the engineering function and the content function are organizationally separate. The content team needs autonomy to publish without developer involvement; the engineering team needs clean, structured, versioned data without being locked into a rendering technology. The headless CMS is the contract between the two.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a headless CMS:

- **Content model** — a schema of *content types* (for example: article, product page, author, navigation menu), each made of *typed fields* (text, rich text, numbers, dates, locations, media, references to other entries) with validation rules. The model is defined by the implementing team, not fixed by the product, and is defined independently of any page design. Without it, the product is a generic database.
- **Content entries** — the items of content created and stored against the model. Entries link to each other through *reference fields* (an article references its author; a page references its components) and to *media assets* (images, video, documents) held in an attached asset store. Entries — not pages — are the system of record.
- **API delivery** — published content is retrieved programmatically through a read API by the external frontends; content is created and managed through a management API (which the product's own editorial application typically uses as well). The API is the primary delivery surface.
- **Decoupled presentation** — the product does not render the end-user experience. Frontends are built outside it. Preview and visual-editing features render the *external* frontend showing draft content; they assist editing but are not the delivery surface.

### Standard Capabilities

Mature products commonly add the following. They make the model operational but do not define the Type:

- **Editorial application** — a web surface for editors: a content list with search, filters, and saved views; an entry editor presenting the fields of the selected content type; a media library; bulk actions.
- **Draft/publish lifecycle** — editing happens on a draft; *publish* is the explicit act that makes content available through the delivery API; *unpublish* withdraws it. Version history with compare and revert sits underneath.
- **Scheduled publishing and releases** — publish at a future time; group multiple entries and assets for simultaneous release.
- **Preview** — draft content rendered in a preview deployment of the real frontend, so editors see content in context before publishing.
- **Localization** — locale definitions with per-field or per-entry translation, and locale-aware publishing.
- **Roles, permissions, and API credentials** — editorial roles that separate "can edit" from "can publish"; admin roles; API keys or tokens for delivery and management access.
- **Webhooks** — HTTP notifications fired when content changes, typically consumed to rebuild static frontends or sync other systems.
- **Environment isolation** — containers for staging versus production (implemented variously as environments, datasets, or separate instances), so model and content changes can be tested before release.
- **SDKs and client libraries** — first-class libraries for the delivery and management APIs.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:            Content repository container
Implementations:    space, project/dataset, self-hosted instance

Concept:            Content model definition
Implementations:    visual model editor (GUI), schema-as-code, GUI + code files

Concept:            Unit of content
Implementations:    entry, JSON document, story composed of blocks

Concept:            Delivery API
Implementations:    REST, GraphQL, both; CDN-hosted read endpoints

Concept:            Preview
Implementations:    preview API + preview deployment, live visual editing overlay
```

A reader who has only seen one implementation — say, a SaaS product with spaces and a REST delivery API — should still be able to recognize a self-hosted product with schema files and a GraphQL API as the same Type.

## How It Works

### 1. Define the content model (developer-led)

```text
Identify the content the application needs
→ create content types (article, author, page section, …)
→ add typed fields with validation rules
→ define references between types
→ iterate with editors until the model fits both authoring and the frontend
```

This is the project's foundation step. The model is designed from the needs of the end application, not from a fixed page template — the same content model can later serve a website, an app, and any future channel.

### 2. Author content (editor loop)

```text
Create a new entry of a content type
→ fill in the fields (text, rich text, media, references)
→ save as draft
→ preview the draft in the external frontend
→ (optionally) submit for review / comments / tasks
→ publish
```

Editors work only with the model the developers defined: fields, validations, and reference pickers come from it. Publishing is the boundary between the editorial world and the delivery world.

### 3. Deliver content to frontends

```text
Frontend requests content from the read API
→ receives structured JSON for published entries (with referenced entries and asset URLs resolved)
→ renders the experience in its own way
```

The same published content can feed a website, a mobile app, and a digital signage player simultaneously. Media files are served from the product's asset delivery infrastructure; many products also offer on-the-fly image transformations.

### 4. Keep frontends in sync

```text
Editor publishes (or unpublishes) content
→ webhook fires to the frontend's infrastructure
→ frontend rebuilds, revalidates, or updates its cache
→ change appears on the end-user surface
```

The synchronization strategy belongs to the consuming team: static rebuild, incremental revalidation, or on-request fetching are all common; the CMS's obligation ends at the API and the webhook.

### 5. Operate at scale

Localization (translate entries per locale), role management (who may edit, who may publish), environment promotion (build and test in staging, promote to production), and scheduled releases become the operational rhythm of larger teams.

### Capability Tiers

**Defining core** — without these, not a headless CMS:

- customer-defined content model (content types + typed fields)
- structured content entries with references and media assets
- read API delivery of published content to external frontends
- management API / programmatic content administration
- decoupled presentation (no owned page rendering as the delivery surface)

**Standard capabilities** — present in essentially all mature products:

- editorial application (content list, entry editor, media library)
- draft/publish lifecycle with versions and unpublish
- scheduled publishing and releases
- preview of draft content in the external frontend
- localization
- roles, permissions, API keys/tokens
- webhooks
- environment isolation
- SDKs

**Optional / variant** — depends on product and segment:

- visual editing overlays (click-to-edit on the real frontend)
- block/page composition features and visual experience builders
- AI content generation and AI assistance
- review workflows, tasks, comments
- app/plugin marketplaces
- taxonomy/tag governance, audit logs, SSO/SCIM
- real-time content delivery
- commerce references and e-commerce integrations

## Interfaces

### Content list

The editor's home surface.

- lists entries in the repository, with status, content type, and last-updated information
- search, filters, saved views, bulk actions
- primary actions: create entry, open entry, publish/unpublish in bulk

### Entry editor

The authoring surface for one entry.

- fields laid out per the content type; validation feedback inline
- sidebar or panels for status/publish, versions, references, translations, preview, tasks/comments where offered
- primary actions: edit fields, save draft, publish, unpublish, schedule, compare versions

### Media library

The asset surface.

- lists uploaded images, videos, documents with metadata
- primary actions: upload, edit metadata, publish asset, link asset into entries

### Model editor

The developer-facing surface where the content model is defined — either a visual editor inside the product, schema files in the customer's codebase, or both. Primary actions: create/edit content types and fields, set validations, define references.

### Preview surface

Renders draft content inside a preview deployment of the external frontend, sometimes with click-to-edit interaction back into the entry editor.

### Settings / administration

Roles and permissions, API keys and tokens, webhooks, locales, environments, and repository/project configuration. Admin-facing.

### Developer surfaces

The APIs themselves (delivery and management), SDKs, CLI tools, and often an API explorer or playground. For this Type, the API is not an internal detail — it is a primary user interface for the engineering half of the audience.

## Important Rules / Behaviors

- **Publish is the delivery gate.** The public read API serves published content only. Drafts are never exposed through it; they are visible only inside the editorial application (and through authenticated preview mechanisms).
- **Draft and published versions coexist.** Editing a published entry creates draft changes while the published version keeps serving; publishing applies the draft. Unpublishing withdraws the public version, with products differing on whether the last draft is kept or replaced.
- **Model changes reach into existing content.** Adding a field makes it available on existing entries (typically empty until filled); required-field validation usually applies at the next edit/publish of an old entry rather than retroactively breaking it. Deleting a model element is guarded — products commonly require a disable/deactivate step first, because consuming frontends depend on the shape of the API response.
- **References must be published to resolve.** An entry referencing an unpublished entry may deliver without the referenced content; publishing related content together (or via releases) is a routine operational concern.
- **Edit and publish are separately permissioned.** The classic role split — writers draft, editors/publishers release — is supported through roles in mature products; API credentials are scoped separately from user accounts.
- **Webhooks report content changes.** External systems learn about publishes, unpublishes, and other changes through webhook events; delivery caching is the frontend's responsibility to invalidate.
- **Containers isolate change.** Model and content changes made in a staging container do not affect production until promoted; the container mechanism (environments, datasets, instances) varies but the isolation behavior is standard.

## Variants

Common market forms of the same Type:

- **API-first SaaS platform** — hosted repository, CDN delivery, enterprise governance; the original and still central form of the category.
- **Developer-first, schema-as-code** — the content model lives in the customer's codebase; the editorial UI is generated from it and is often itself customizable or embeddable.
- **Open-source, self-hosted** — the product runs inside the customer's infrastructure; the content APIs are served by the customer's own deployment; a vendor-hosted option is common.
- **Editor-friendly visual hybrid** — headless delivery plus a strong visual editing layer (live preview of the real frontend, click-to-edit), aimed at marketing-led teams that still need API delivery.
- **Suite-embedded content module** — content management offered as a module of a broader digital-experience or commerce suite, used in a headless posture.

A variant stays a variant while the defining core holds. When page composition and rendering become the product's own delivery surface, the product has drifted toward a different Type (see Related Application Types).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Content Management System / CMS | sibling; the sharpest boundary | A coupled CMS renders pages itself (templates/themes) — its delivery surface is the rendered site. A headless CMS delivers content via APIs and the site is built outside. A coupled CMS that also exposes a content API is used *in a headless mode*; the Type describes products whose defining posture is the decoupled repository. |
| Blogging Platform | adjacent | A blogging platform owns the presentation (themes, hosted pages) and serves end users directly. A headless CMS has no owned presentation and serves developer-built frontends. |
| Digital Asset Management / DAM | adjacent; integration seam | A DAM's system of record is media assets with a rich asset lifecycle. A headless CMS's system of record is structured content entries, with assets as a supporting object. Headless CMS products commonly integrate with DAMs rather than replace them. |
| Headless Commerce Platform | structural sibling | Same decoupling pattern, different domain: the commerce engine's objects are products, carts, orders, and payments; the headless CMS's objects are content entries and assets. The two are frequently used together, with the CMS referencing commerce data. |
| Product Documentation Portal / Help Center | downstream consumer | Those are published, end-user-facing output surfaces; a headless CMS can be their backend. |
| Visual Website Builder | drift boundary | When block-based page composition plus hosting/rendering of the end-user page becomes the product's primary surface, it has left this Type. Page-composition features inside a headless CMS remain optional capabilities as long as API delivery stays the defining surface. |
| Backend/API platform (database-as-a-service) | adjacent | A generic data platform lacks the content model, the editorial application, and the publishing lifecycle. Remove those and what remains is not a CMS. |

## Representative Products

- **Contentful** — API-first SaaS content platform; enterprise segment; spaces/environments model with a multi-API delivery stack.
- **Sanity** — developer-first; schema defined in code; hosted content datastore with a customizable, open-source editorial studio.
- **Strapi** — open-source, self-hosted (with a vendor cloud option); content types and components defined in an admin builder or code; REST/GraphQL content APIs.
- **Storyblok** — component-based SaaS headless CMS with a visual editor that previews the real frontend; marketing-team-friendly pole.

The sample deliberately spans enterprise SaaS, developer-first, open-source self-hosted, and editor-friendly visual philosophies. The defining core was checked against this spread to avoid over-fitting the definition to any one delivery model or generation.

## Sources

Research date: **2026-09-07**

- Contentful Developers Docs — Domain model, Data model, API basics: https://www.contentful.com/developers/docs/concepts/ , https://www.contentful.com/developers/docs/concepts/data-model/ , https://www.contentful.com/developers/docs/concepts/apis/
- Contentful Help Center — Content modeling basics; Web app overview: https://www.contentful.com/help/content-models/content-modelling-basics/ , https://www.contentful.com/help/getting-started/contentful-web-app-overview/
- Sanity Docs — Content Lake; Documents; Datasets; Studio: https://www.sanity.io/docs/content-lake , https://www.sanity.io/docs/content-lake/documents , https://www.sanity.io/docs/content-lake/datasets , https://www.sanity.io/docs/studio
- Strapi 5 Documentation — Models; Draft & Publish; Content APIs: https://docs.strapi.io/cms/backend-customization/models , https://docs.strapi.io/cms/features/draft-and-publish , https://docs.strapi.io/cms/api/content-api
- Storyblok Docs — Content Modeling; Visual Editor; Stories; Spaces: https://www.storyblok.com/docs/concepts/content-modeling , https://www.storyblok.com/docs/concepts/visual-editor , https://www.storyblok.com/docs/manuals/stories , https://www.storyblok.com/docs/manuals/spaces

All listed sources were fetched directly on the research date. Precise product-specific limits and mechanics (field-count limits, dataset rules, API endpoint hosts, preview-token parameters) are intentionally not stated in this document; they are recorded in the paired Research Notes.
