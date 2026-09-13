# Content Management System / CMS

## Overview

A **Content Management System (CMS)** is software through which an organization creates, structures, stores, and manages digital content items, and assembles them into a delivered website — without requiring the people who write the content to write code.

The defining core is small:

```text
Structured content items (typed, field-based)
  stored in a managed content repository
    authored by non-developers in an administrative interface
      assembled into delivered web pages by a coupled presentation layer
        moved through a controlled publishing lifecycle
```

Everything else commonly associated with CMS products — media libraries, categories and tags, revision history, menus, SEO tooling, multilingual content, plugin ecosystems, headless APIs, personalization — is widely supported by mature products but is not what makes a product a CMS. Older, regional, and platform-native CMS products satisfy the definition without most of those capabilities, and modern products add them without changing what the Type is.

When the coupled presentation layer is removed and content is delivered only through APIs, the product becomes a different Application Type (Headless CMS). When the structured content repository is removed and only visual page construction remains, it becomes a Website Builder.

## Users & Context

The CMS is operated by an organization that needs to run a website whose content changes more often than its design.

Primary users:

- **Content editors / authors** — the central role. They create and update content items, place images and files, and publish. They are typically writers, marketers, or subject-matter staff, not developers.
- **Site administrators** — configure the system: users and roles, site settings, navigation, integrations, extensions.

Secondary users:

- **Developers / implementers** — build the presentation layer (themes, templates, components) and custom extensions. They shape the system once; editors then run it day to day.
- **Reviewers / approvers** — in organizations with editorial oversight, they gate what gets published.
- **Marketers** — use the published site and its content for campaigns; in enterprise products they may also operate personalization and analytics.

The typical context is a marketing site, corporate site, publication, or campaign site: content that is updated continuously by staff, presented under a design that changes rarely. The CMS is the system of record for that content and the production line that turns it into public pages.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a CMS:

- **Structured content items** — content exists as discrete, typed items with fields (a news item with a headline, body, date, and image; a product page; a landing page), not as loose files or raw code. Typing is what lets the system list, relate, reuse, and re-present content.
- **Content repository** — the persistent store where items live, together with their media assets and organizational metadata. The repository is the system of record: the website is a projection of it.
- **Editor-facing authoring interface** — an administrative surface (the "back end") where non-developers create and edit items through forms, rich-text editors, or block editors. This is what distinguishes a CMS from a web framework.
- **Coupled presentation layer** — the same system renders stored content into the public website ("front end") through templates, themes, and components. The CMS owns both the content and its delivery: change the content, and the site updates; change the theme, and the content re-presents.
- **Publishing lifecycle** — items move through managed states: work-in-progress (draft) → published → updated → archived or unpublished. The published state is a visibility switch controlled by the system, not by the file system.

### Capabilities Shared by Mature Products

These are standard in modern CMS products. They make a CMS practical, but a product lacking some of them can still be a CMS:

- **Media library** — central management of images, video, and documents as reusable assets referenced from content items.
- **Taxonomy** — categories, tags, and metadata used to organize and dynamically list content (topic pages, archives, related items).
- **Revision history** — every save produces a version; editors can compare and revert.
- **Navigation management** — menus and link structures managed as data, separate from page content.
- **Preview** — see how unpublished content will look before publishing it.
- **Scheduled publishing** — publish now, or at a future time.
- **Roles and permissions** — at minimum a separation between who may edit and who may publish; commonly finer-grained control per section of the site.
- **SEO surfaces** — editable meta data, friendly URLs, redirects.
- **Multilingual content** — parallel language versions of items, managed as translations of the same item.
- **Extensibility** — plugins, modules, or extensions that add capability without changing the core.
- **Site and content search** — both for visitors and for editors managing large repositories.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:            Structured content items
Implementations:    posts and pages with fields; page types with properties;
                    content elements on pages; content types with entries;
                    components and content fragments

Concept:            Presentation layer
Implementations:    themes with template files; templating engines configured
                    per site; component-based page editors; page types
                    rendered by the site

Concept:            Publishing lifecycle
Implementations:    draft/publish buttons; publish/unpublish (activate/deactivate)
                    with scheduled release; draft versions with autosave;
                    batch releases of many items

Concept:            Repository topology
Implementations:    one system for authoring and delivery; separate author and
                    publish environments; API-only delivery (the headless form)
```

A reader who has only seen one implementation — for example a page-tree CMS where editors drag components onto pages — should still be able to recognize an entry-based CMS where editors fill in content-type forms, and vice versa.

## How It Works

### 1. Shape the system (once, by implementers and administrators)

```text
Define the content types the organization needs
→ build or select the presentation layer (theme / templates / components)
→ define the site structure (page tree or navigation)
→ set up users, roles, and languages
→ install extensions where capability is missing
```

This phase is developer- and administrator-heavy. Its output is an empty but structured CMS: types exist, templates render, roles are defined.

### 2. Author content (continuously, by editors)

```text
Create a new item (of a chosen type)
→ fill in its fields (title, body, image, dates, taxonomy)
→ save as draft (work-in-progress; often autosaved)
→ preview how it will appear on the site
→ submit for review, where review exists
```

Editing happens in the administrative interface, never in the public site. Editors work against the repository, not against the live pages.

### 3. Publish (the visibility switch)

```text
Publish now, or schedule for later
→ the item becomes publicly visible on the site at its URL
→ later edits are saved as new versions and re-published
→ unpublish (or archive) removes the item from the public site
   while keeping it in the repository
```

Publishing is the defining transaction of the Type: it is the moment content in the repository becomes content on the website. Unpublishing reverses visibility without destroying the record.

### 4. Maintain the site (ongoing)

```text
Update the presentation layer without touching content (new theme, template changes)
→ reorganize navigation and taxonomy as the site grows
→ roll back to a previous version when an edit goes wrong
→ manage media, redirects, and SEO metadata
→ extend the system as requirements grow
```

### Capability tiers

**Defining core** — without these, not a CMS:

- structured content items
- content repository
- editor-facing authoring interface
- coupled presentation layer (site assembly and delivery)
- publishing lifecycle with a visibility switch

**Standard capabilities** — present in most mature products:

- media library, taxonomy, revisions, menus, preview, scheduling, roles, SEO surfaces, multilingual, extensibility, search

**Optional / variant capabilities** — depend on segment and posture:

- headless/API delivery as an additional channel
- separate author and publish environments
- editorial approval workflows
- personalization and experimentation
- multi-site management, e-commerce integration
- comments, membership, AI assistance

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Administrative dashboard

The editor's entry point after login.

- recent activity, quick actions, system status
- primary actions: navigate to content areas, open the item editor, administer the site

### Content list

The inventory of content items by type.

- filterable/searchable list with status (draft, published, scheduled), author, dates
- primary actions: create item, open for editing, publish, unpublish, delete, duplicate

### Item editor

The surface where one content item is written.

- fields per the item's type; rich-text or block-based body editing; media selection from the library; taxonomy assignment
- primary actions: save draft, preview, publish, schedule, view revisions

### Site structure / page tree

The hierarchical map of the site.

- pages arranged in a tree mirroring the URL structure; reorganized by moving pages
- primary actions: create/move/rename pages, open page for editing, set page properties

### Page editor (where the presentation layer is editable)

In page-centric products, the surface where a page is assembled from components or blocks.

- live or structured view of the page; the set of available components or blocks; per-component settings
- primary actions: insert/move/configure components, preview, publish page

### Media library

The asset store.

- browsable collection of images, videos, documents with metadata
- primary actions: upload, organize, edit metadata, insert into content

### Appearance / theme settings

The presentation control surface.

- installed themes or templates and their configuration
- primary actions: activate theme, configure layout, customize design

### User and role administration

- users, groups, roles, per-section permissions
- primary actions: invite users, assign roles, restrict sections

### Settings

- site identity, URLs and redirects, languages, integrations, extensions, caching

## Important Rules / Behaviors

### Draft and published are different worlds

An unpublished draft is invisible to the public site no matter how complete it is. Preview exists precisely because the editor must see the published rendering without publishing. Conversely, unpublishing removes public visibility but keeps the item in the repository — removal from the site is not deletion of the record.

### Content and presentation are separable

The same content renders under whatever theme or template is active. Changing the presentation layer re-presents the repository without rewriting it; changing content does not require touching templates. This separation is the CMS's central engineering idea and the reason editors and developers can work independently.

### Publishing is permission-gated

In mature products, the right to edit and the right to publish are distinct permissions. An editor may be able to save drafts that only a publisher can release. Access rights also gate scheduling and section-level administration.

### Revisions are the safety net

Every significant save produces a version. Editors can compare and revert. Published-but-wrong content is corrected by publishing a new version, not by editing history.

### URLs are managed, not incidental

Content items have system-managed addresses (permalinks). Products provide redirect management because moving or renaming content must not break inbound links — the URL structure is part of the managed content model.

### The repository is the system of record

Lists, archives, topic pages, and feeds are generated views over the repository (for example, a category page listing its items). Deleting or unpublishing an item changes every view that includes it.

## Variants

Common forms of the Type:

- **Open-source self-hosted CMS** — the operator runs the software on its own hosting; themes and plugins from a community ecosystem (e.g. WordPress, TYPO3).
- **Commercial SaaS CMS** — vendor-operated hosting and updates; editors log in to a service (mid-market and marketing-site products).
- **Enterprise experience platform** — the CMS is the content core of a larger digital-experience suite with personalization, analytics, and multi-site governance; commonly adds a separate author/publish environment split and API delivery (e.g. Adobe Experience Manager, Optimizely CMS).
- **Hybrid CMS** — a coupled site plus headless API delivery from the same repository; increasingly the default posture of enterprise products.
- **Publication-focused CMS** — pre-shaped for chronological publication with themes and audience features; the boundary toward the Blogging Platform Type (e.g. Ghost).
- **Regional / legacy enterprise CMS** — long-lived open-source products with strong regional bases and their own templating and configuration machinery (e.g. TYPO3 in the European market).

A variant remains a variant unless it changes the defining core. The headless form changes the core (no coupled presentation layer) and is therefore treated as a separate Type, not a variant.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Headless CMS | sibling; sharpest boundary | content repository + authoring + API delivery, but **no coupled presentation layer** — no site assembly, no themes; pages are built by external front ends |
| Blogging Platform | specialized sibling | pre-shaped for chronological posts with minimal configuration; a CMS lets the operator define content types and own the whole site structure |
| Website Builder | adjacent | visual page construction without a structured content repository as the central object; content is not typed, stored, and re-listed as items |
| Wiki Application | adjacent | collaborative pages edited in place are the deliverable; no separate presentation layer, no publish lifecycle, no content-type modeling |
| Enterprise Content Management | adjacent, different domain | manages organizational documents and records (files, retention, compliance), not web content assembly and site delivery |
| News Publishing Platform | specialized downstream | newsroom-specific editorial workflow and output; a CMS is the general substrate beneath it |
| Product Documentation Portal | specialized sibling | structured content specialized for versioned product documentation |
| Digital Asset Management (DAM) | capability vs product | the CMS media library is one capability; DAM makes assets the whole product |

The boundary with **Headless CMS** is the most important one: modern CMS products increasingly expose API delivery alongside their site, but the coupled presentation layer — the CMS owning the website — remains what makes the Type. Remove it, and the product is headless.

## Representative Products

- **WordPress** — dominant open-source web CMS; blog heritage generalized into full site management; theme and plugin ecosystems
- **TYPO3** — long-lived open-source enterprise CMS with a strong European base; page tree + content elements model
- **Adobe Experience Manager** — enterprise experience platform with the CMS at its core; author/publish split; hybrid headless delivery
- **Optimizely CMS** — commercial mid/enterprise CMS built on explicit page types and properties

Boundary samples consulted to sharpen the Type's edges: **Ghost** (publication-focused pole) and **Contentful** (headless pole).

## Sources

Research date: **2026-09-07**

- WordPress — https://wordpress.org/documentation/ , https://wordpress.org/documentation/overview/ , https://wordpress.org/documentation/article/introduction-to-blogging/ , https://wordpress.org/documentation/article/first-steps-with-wordpress-block-editor/
- TYPO3 — https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/ , https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Concepts/Index.html
- Adobe Experience Manager — https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/introduction , https://experienceleague.adobe.com/en/docs/experience-manager-learn/sites/overview , https://experienceleague.adobe.com/en/docs/experience-manager-65/content/sites/authoring/essentials/first-steps
- Optimizely CMS — https://docs.developers.optimizely.com/content-management-system/docs , https://docs.developers.optimizely.com/content-management-system/docs/learn-basic-editing
- Ghost — https://ghost.org/docs/ , https://docs.ghost.org/product/
- Contentful — https://www.contentful.com/developers/docs/concepts/

> Sourcing limitation: drupal.org could not be fetched from the research environment (JavaScript-gated on repeated attempts, 2026-09-07). No product-specific claims about Drupal are made in this document. Precise operational details (numeric limits, default settings, exact state names) are intentionally not stated; detailed evidence and product-by-product observations are recorded in the paired Research Notes.
