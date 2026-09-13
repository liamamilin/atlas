# Visual Website Builder

## Overview

A **Visual Website Builder** is a no-code site-creation application: it lets a person assemble a complete website — its pages, sections, content, and appearance — through direct visual manipulation in a purpose-built editor, and publish it as a functioning website at a web address, without writing code as the primary building act.

The defining structure is small:

```text
The Site (a whole web presence — one or more pages)
└── composed of arranged sections/elements carrying content
    └── assembled and continuously re-edited visually, without code
        └── published as a live functioning website at a web address
```

Three properties. If any one is removed, the product is no longer recognizable as a visual website builder:

- **Visual no-code assembly** — the building act is direct manipulation of pages, sections, and elements in an editor. Without it, the product is a code-first web development tool.
- **The whole website as the unit of work** — the artifact is a whole web presence, not a single campaign page and not a fragment embedded in pages owned by other systems. Without it, the product is a landing page builder or an embedded-content tool.
- **The published live website as the deliverable** — the assembled artifact becomes a functioning website reachable at a web address, with the product providing the path to publication. Without it, the product is a design tool or an unpublished prototype.

Everything commonly associated with modern builders — template libraries, drag-and-drop as a specific gesture, responsive machinery, AI site generation, commerce, blogging, CMS, app marketplaces, contributor roles — is widespread in current products but is not part of the defining core. Hosted page-builder ancestry, desktop publish-to-host builders, and Flash-era site builders all fit this definition without any of those specifics.

## Users & Context

The primary user is a person or small organization that needs a web presence — a business site, portfolio, personal site, or organization site — and does not develop software for a living. They typically arrive with content (text, images, a logo) and an idea of the pages they need, but not with the skills or desire to write HTML/CSS or operate a server.

Typical reasons to open the application:

- create a first website for a business, practice, portfolio, or event
- rework an existing site's pages, content, or look without touching code
- publish changes to the live site and connect a custom domain
- add a capability to an existing site — a contact form, a blog, a store, a booking surface

Secondary actors appear as sites become organizational: contributors with restricted permissions, clients of an agency (who may be allowed to edit only some parts of a site), and professionals hired through the product's own marketplace to build or maintain the site. The work environment is a browser; the editor is an online application, and the site it produces is served by the same platform in the dominant implementation.

## Core Model

### The Defining Core

```text
The Site
└── Pages (one or more)
    └── Sections / arranged elements
        └── Content (text, images, media, buttons, forms)
└── Design layer (site-wide styles)
└── Publication (the live website at a web address)
```

- **The site** is the persistent, re-editable artifact. It is a whole web presence: it has pages, navigation, and an address. It outlives any single editing session and is edited again and again over time.
- **Pages** are the site's primary subdivisions. A site has one or more pages, organized into navigation (menus, headers, footers).
- **Sections and elements** are the building units inside a page. Products differ in what they call them and how freely they can be placed — free-canvas elements, drag-and-drop blocks inside sections, or widgets within rows and columns — but in every case the user composes the page by placing and arranging ready-made units and filling them with content.
- **The design layer** is the site-wide style system: colors, text styles, buttons, spacing, backgrounds. It exists so that changing the theme changes the whole site, not one page.
- **Publication** is what turns the artifact into a website: the composed site is published to a web address — a platform-provided address or the user's own connected domain — and becomes reachable by visitors.

### Capabilities Shared by Mature Products

A typical modern product carries most of these. They are not what makes the product a website builder, but they make building a site practical:

- **Template library** — a catalog of pre-designed sites, usually filtered by industry or purpose, used as the starting point. A blank start remains available in professional-oriented products.
- **Element/block palette** — a searchable panel of ready-made units (text, image, gallery, video, button, form, map, social embed, shapes) placed onto the page, typically appearing with placeholder content to be replaced.
- **Page management** — add, duplicate, reorder, and delete pages; define navigation menus, headers, and footers.
- **Device handling** — a surface for how the site appears on phones and tablets: a separate mobile editor, breakpoint editing, or device views, commonly with the ability to hide or rearrange elements per device.
- **Save → preview → publish loop** — work is saved as an editable draft, previewed as visitors would see it, and published to the live site; version history allows returning to a previous state, and unpublishing takes the site offline.
- **Custom domain** — purchase, connect, or transfer a domain so the site lives at the user's own address.
- **Media library** — upload and organize images, videos, and files used across the site.
- **SEO settings** — per-page titles, descriptions, and site-level search settings.
- **Contact forms** — visitor-facing forms with submission handling.
- **Contributors and permissions** — invite other people to work on the site with defined roles.
- **Extension marketplace** — installable third-party or first-party apps that add capabilities to the site.
- **AI generation and assistance** — answering a few questions to generate a starting site, or generating sections/content inside the editor (era-current; an onboarding path, not a structure).

### One Structure, Many Implementations

The core model is written in conceptual terms. Common implementations realize each concept differently:

```text
Concept:            Building unit
Implementations:    free-placed elements on a canvas; drag-and-drop blocks
                    inside sections; widgets within rows and columns;
                    style-panel-composed elements

Concept:            Starting point
Implementations:    template library; blank site; AI-generated site from
                    a short questionnaire

Concept:            Device handling
Implementations:    separate mobile editor; breakpoint editing; device
                    preview views with per-device visibility rules

Concept:            Publication
Implementations:    platform-operated hosting with a publish button;
                    staging + production environments; publishing
                    machinery to external hosting
```

A reader who has only seen one implementation (e.g., a template-plus-drag-and-drop hosted builder) should still be able to recognize the others from the core model.

## How It Works

### Start the site

```text
Choose a starting point (template / blank / AI-generated from a short
questionnaire)
→ a site project is created with pages, sections, and placeholder content
→ open the visual editor
```

### Assemble pages

```text
Pick a page (or add one)
→ place sections/elements from the palette onto the page
→ replace placeholder content with real text, images, media
→ rearrange, resize, duplicate, delete
→ repeat across pages; build navigation menus, headers, footers
```

The editor shows the page as visitors will see it. Placement and content editing happen directly on that representation.

### Style the site

```text
Open the design/theme panel
→ set site-wide colors, text styles, buttons, spacing
→ adjust individual sections/elements where needed
→ the design layer keeps the site visually consistent
```

### Handle devices

```text
Switch to the device surface (mobile editor / breakpoints / device views)
→ adjust how pages appear on smaller screens
→ hide or reorder elements per device where needed
```

### Publish

```text
Save the draft
→ preview as visitors would see it
→ publish → the site goes live at its web address
→ connect (or purchase) a custom domain
→ later: edit again → save → publish again
```

Publishing is repeatable and non-destructive: the live site keeps serving while new edits accumulate as a draft, and version history allows rolling back.

### Maintain and extend

```text
Edit the live site at any time
→ add capabilities as needed (forms, blog, store, bookings)
→ invite contributors with defined roles
→ monitor traffic through the platform's analytics surface
```

### Core vs Common vs Optional

**Defining core** — without these, not a visual website builder:

- visual no-code assembly of pages from sections/elements
- the site as a persistent, re-editable whole web presence
- publication of the artifact as a live functioning website at a web address

**Common mature structure** — present in most modern products:

- template library; element/block palette with placeholder content
- page management and navigation
- site-wide design layer
- device-handling surface
- save → preview → publish loop with version history
- custom domain connection; media library; SEO settings; contact forms
- contributors/permissions; extension marketplace; AI onboarding

**Variant / optional** — depends on audience, segment, and posture:

- editing model (free canvas vs structured sections vs professional flex/grid)
- commerce depth (none → buy buttons → native store → full store admin)
- content depth (static pages → blog → CMS collections/dynamic pages)
- code posture (none → embeds/custom-code blocks → scripting/dev platform → code export)
- hosting posture (platform-operated hosting vs publishing machinery to external hosting)
- agency posture (multi-site client management, white label, client-scoped editing locks)
- scope (one-page minimal sites ↔ multi-page sites ↔ multi-site management)

## Interfaces

The following surfaces are described conceptually. Exact layouts and names vary by product.

### Site dashboard

The management surface outside the editor.

- lists the account's sites; entry point to open the editor
- plan/billing, domain status, analytics summaries
- primary actions: open editor, manage settings, view traffic

### Visual editor

The central working surface.

- a canvas showing the page as visitors see it, surrounded by panels
- an add-panel/palette of sections, elements, or widgets (searchable)
- a page manager for the site's page structure
- a design panel for the selected element and the site-wide theme
- primary actions: add/place elements, edit content in place, customize design, switch device view

### Device view / mobile editor

The surface for smaller screens.

- the page rendered at phone/tablet width, or breakpoint controls
- primary actions: adjust layout per device, hide/show elements

### Publish and domain settings

The surface where the artifact becomes and stays live.

- publish/unpublish controls, version history
- domain purchase/connection/transfer, site address settings
- primary actions: publish changes, connect domain, restore a version

### Media library

The site's asset store.

- uploaded images, videos, documents; organization into folders/categories
- primary actions: upload, organize, insert into pages

### SEO settings

- per-page titles and descriptions, site-level search settings
- primary actions: edit metadata, check site-level search visibility

### Module surfaces (store, blog, forms, bookings)

Capability modules add their own surfaces (product management, post editor, form submissions, appointment settings). They are optional layers on the site, not part of the core editor.

## Important Rules / Behaviors

### Edits and the live site are separated by publish

Work accumulates as a draft; visitors see the last published state. Saved changes do not appear on the live site until publish. This separation — draft vs live — is the central state rule of the Type.

### The live site remains editable

Publication is not an end state. The site can be reopened and edited at any time after publishing; changes go live on the next publish. Unpublishing takes the site offline while preserving the artifact.

### Concurrent editing is commonly constrained

Some products constrain simultaneous editing of the same site — parallel edits from multiple sessions risk overwriting each other. Real-time multi-user editing exists in the professional pole but is not universal; contributor roles commonly gate who may edit what.

### Structure constrains placement

The editing model defines where units may be placed. Structured editors distinguish freely-editable areas from structured areas (e.g., collection or gallery sections that render their own content) — blocks cannot be added everywhere. Free-canvas editors constrain differently (absolute placement rather than flow layout). The rule is product-specific in form but structural in kind: the editor's layout model governs what placements are legal.

### The editor is an online application (dominant implementation)

In the dominant hosted shape, the editor requires a connection to the platform; work cannot proceed offline, and the site's files are not handled as local documents. Desktop/export lineages relax this, at the cost of operating hosting themselves.

### Version history protects the artifact

Publishing repeatedly does not destroy prior states; products retain site history so a previous version can be restored. This is the safety net that makes continuous live editing safe.

## Variants

- **Mass-market hosted builder** — template + guided start + free-canvas or block editing, all-in-one business tools attached; consumer and small-business audience.
- **Design-led template builder** — curated templates with a strong design system; premium consumer/creative audience; editing deliberately more constrained to protect design quality.
- **Professional visual development builder** — designer/agency audience; CSS-level style control, breakpoints, staging environments, code export; leans toward development while remaining visually driven.
- **Agency / white-label builder** — the product is operated by agencies on behalf of clients: multi-site management, client-scoped permissions, white-label branding of the builder itself.
- **Minimal one-page builder** — the site may be a single page; the unit of work is still the whole web presence.
- **Guided small-business builder** — questionnaire-driven setup with section-based editing; distributed through adjacent channels (e.g., domain registrars).
- **Domain-specialized siblings** — the same substrate with domain-shaped content objects and integrations (e.g., church website builders); a specialized variant relationship, not a different building act.
- **AI-first posture** — prompt-to-site generation as the front door, with the visual editor as the refinement surface (era-current; increasingly the default onboarding).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Landing Page Builder | centers on a single conversion page with conversion machinery (forms, testing, lead capture) as the organizing structure; the website builder's unit is the whole persistent web presence |
| Interactive Web Design Application | centers on authored behavior — trigger→response interactions as the design act on a freeform canvas; in a website builder, interactions/animations are one capability among many, and site assembly is the center |
| Online Store Builder | the buying-and-ordering machinery (catalog → cart → checkout → orders) is the organizing structure with dedicated store administration; in a website builder, commerce is an optional module on the site substrate |
| Church Website Builder | same building substrate plus church-shaped content objects and church-operations integration as first-class structure; a domain-specialized sibling |
| CMS | content-first: the site is a container for ongoing content production through a content model, with presentation from themes; the website builder is assembly-first: the user composes structure and appearance directly. Modern products converge (builders ship CMS layers; CMSs add page composition) — the seam is the center of gravity |
| No-code Application Builder | builds a data-and-logic application (databases, user accounts, record-level permissions); the website builder builds a published content/presentation site for web audiences |
| Web Development IDE | code-first site construction; the website builder's defining property is that code is not the primary building act |
| UI Design Application / UX Prototyping Application | produces a design artifact or unpublished prototype implemented elsewhere; the website builder's artifact is the working site itself |
| Template-based Design Platform | produces design artifacts (images, PDFs, print, video); even when it publishes web pages, the deliverable is a designed artifact, not a functioning hosted website with structure and content |
| AI Design Generator | produces design artifacts from described intent; AI site generation inside builders produces a functioning editable site — a different deliverable container |
| Blogging Platform | content-stream-first: the site is organized around an ongoing content feed; blog capability appears in website builders as a module |
| Web Hosting | provides server space and traffic without the assembly surface; the website builder's defining act is visual assembly, with hosting as the delivery path |

## Representative Products

- Wix — mass-market hosted builder; free-canvas element editing; all-in-one business tools
- Squarespace — design-led template builder; premium consumer/creative audience
- Webflow — professional visual site development; designer/agency pole
- Duda — agency/white-label builder; multi-site client management

The defining core was checked against hosted page-builder ancestry, desktop publish-to-host builders, and Flash-era site builders to avoid over-fitting to the current hosted, template-first, AI-onboarded implementation.

## Sources

Research date: **2026-09-09**

- Wix Help Center — https://support.wix.com/en/ ; "Creating a website" topic — https://support.wix.com/en/creating-a-website ; "Getting Started with the Wix Editor" — https://support.wix.com/en/article/wix-editor-getting-started-with-the-wix-editor
- Squarespace Help Center — https://support.squarespace.com/hc/en-us ; "Add content to your site with blocks" — https://support.squarespace.com/hc/en-us/articles/206543757
- Webflow Help Center, "Intro to Webflow" — https://university.webflow.com/lesson/intro-to-webflow
- Duda Support — https://support.duda.co/hc/en-us ; "Editor Overview" — https://support.duda.co/hc/en-us/articles/26519221644439-Editor-Overview

> Sourcing limitation: the GoDaddy Website Builder and Carrd help surfaces were unreachable from the research environment (repeated timeouts) and are therefore not sampled for operational detail; no product-specific claims about them are made in this document. Precise product-specific figures and editor-generation details are intentionally omitted here and remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
