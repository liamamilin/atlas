# Intranet Platform

## Overview

An **Intranet Platform** is an application for building and operating an organization's internal web estate: a private, authenticated set of sites and pages where the organization publishes news, resources, documents, people, and access to tools for its own employees to visit and use.

The defining structure is small:

```text
Organization-internal, employment-based population
└── Buildable, governed estate of internal sites/pages
    └── Standing destination employees visit (pull)
        └── Organization-published content: news, resources,
            documents, people, tool access
```

Everything else commonly associated with the category — news feeds, communities and comments, analytics, micro-apps, AI answers, mobile apps, bundled newsletters — is widespread in current products but is not what makes a product this Type. A portal-server-era platform with sites, pages, and permission-controlled publishing satisfies the same core without any of the modern packaging.

The boundary signals are threefold: the **audience** is the organization's own workforce (not the public); the **structure** is a buildable, governed estate of internal surfaces (not one fixed home page); and the **mode** is a destination employees go to on their own initiative (not a channel that pushes content to them). When any of these shifts, the product is drifting toward a different Application Type.

## Users & Context

The platform serves two fundamentally different populations:

**Builders and operators** — the people who construct and run the estate:

- intranet owners: set direction, information architecture, and governance for the whole estate
- IT administrators: manage the platform itself — identity, integrations, provisioning, security
- site owners: responsible for individual sites or sections (a department, a region, a function)
- content authors and contributors: internal comms, HR, IT, Legal, and other functions that publish news and maintain long-lived pages ("HR offers its services to the rest of the organization" is the canonical pattern)
- community managers: moderate discussion spaces where they exist

**Employees** — everyone in the organization. They do not build the estate; they visit it. A typical session: open the intranet home, scan the news, navigate or search for a policy or a form, look up a colleague, follow a link into a tool or a request.

The typical context is any organization large or distributed enough that "what's happening and where do I find things" can no longer be answered by email and hallway conversation. The estate is the organization's shared answer: one branded, governed place that says what the organization publishes, offers, and expects employees to know.

## Core Model

### The Defining Core

Three structures. Remove any one and the product is no longer recognizable as this Type:

- **Organization-internal population with employment-based access** — the estate belongs to one organization, and its members come from that organization's employment relationship: directory or SSO identity, HR-sourced accounts, or organization-issued credentials (including access methods that work without corporate email for frontline staff). Employees are known members, not registrants. This is what separates the estate from any public website.
- **Building and governance machinery** — the platform provides the means for non-developers to create and structure internal surfaces: pages and sites composed from reusable components (content blocks, widgets, templates), arranged by navigation, administered through roles (administrator, site owner, editor, contributor) and permissions, with a content lifecycle (draft, publish, review, archive, remove). This machinery is what makes the product a *platform*: the organization assembles its own estate on it, and reassembles it as the organization changes.
- **A standing pull destination** — authorized organizational publishers place content on the estate for employees to visit: news and announcements organized in channels or streams, long-lived pages carrying policies and how-to resources, document and file access, the people directory, and links or entry points into internal tools. Employees consume on their own initiative, by navigating, searching, or following what the estate surfaces. The intranet is where employees go — not primarily a channel that delivers to them.

### Standard Capabilities

Mature products commonly add the following. They make the estate practical; they do not define it:

- **News publishing with audience targeting** — announcements and articles in organized channels, with visibility targeted to groups defined by role, location, department, or attributes synced from HR and identity systems.
- **Permission-aware search** — search over the estate's content, and in many products across connected systems, where results respect each employee's access rights.
- **Curated navigation and personalization** — organization-designed menus and hub navigation whose items follow permissions, plus audience-specific variations of pages and experiences (desk and frontline, headquarters and sites).
- **Tool access and in-place actions** — launchers, link collections, embedded widgets, and small forms that let employees start requests and reach HR, IT, and business systems without leaving the estate; the heavy processing stays in those systems.
- **People directory and profiles** — who's who, what they do, how to reach them.
- **Community layer** — spaces where employees discuss, react, comment (usually with moderation), and register for events.
- **Measurement** — page and news analytics (visitors, views, reach, engagement) so operators can see what employees actually use.
- **Governance tooling** — approval and review workflows, ownership and validation metadata on content, retention and archival behavior, and compliance surfaces such as policy acknowledgements.
- **Branding, multi-language, multi-device** — the estate carries the organization's identity; desktop web is the primary surface with a mobile companion; content can exist in multiple languages.
- **Identity and HR integrations** — SSO, directory synchronization, and HRIS feeds that keep the population and its attributes current.
- **AI assistance** — permission-aware answers over company content, drafting and page-generation help, and conversational assistants (common in current products, but recent).

### One Structure, Many Implementations

The core model is conceptual; products realize each part differently:

```text
Concept:  Internal population
Implementations:  tenant/directory identity, SSO federation, HR sync,
                  CSV import, organization-issued access credentials

Concept:  Building machinery
Implementations:  sites with page templates and web parts,
                  block-based page designers with widget catalogs,
                  low-code hub configuration, portal-framework machinery

Concept:  Estate scope
Implementations:  families of sites connected by shared navigation,
                  self-contained spaces per brand or subsidiary,
                  sections of one central hub

Concept:  Pull destination
Implementations:  curated home site, personalized hub pages,
                  news channels, resource libraries, people directory
```

A reader who has only seen a modern hosted intranet should still be able to recognize a tenant-assembled estate of independent sites as the same Type — and vice versa.

## How It Works

### Stand up the population and the estate

```text
Connect identity (SSO/directory) and HR sources
→ employees appear as members with attributes
→ plan the information architecture (top-level topics, site structure)
→ build sites and pages from components and templates
→ wire navigation and set permissions
→ brand the estate, add languages
→ launch
```

Operator guidance across products treats launch as a beginning, not an end: the estate needs continuous ownership, review, and renewal, or it loses value as content goes stale.

### Publish

```text
Author creates news or updates a page
→ applies targeting (audience groups) and language versions
→ submits for review where governance requires it
→ publishes
→ the item appears in the channel/page and, where targeted,
   only for the selected audience
```

Two content rhythms coexist: **news** (dated, flows through channels, decays) and **pages** (long-lived, versioned, owned). Both are organization-published; neither is peer conversation.

### Visit and find

```text
Employee opens the intranet home
→ scans news targeted to them
→ navigates the menu or searches
→ opens a page, document, or person
→ follows a link into a tool or starts a request
```

Finding works through three mechanisms the platform provides: **navigation** (curated menus that show only what the employee may see), **search** (permission-aware, increasingly answer-shaped), and **targeted surfaces** (the estate itself shows different content per audience).

### Govern

```text
Operators review content freshness and analytics
→ update, merge, or archive stale items
→ manage access as people join, move, or leave
→ adjust navigation and structure as the organization changes
```

Because the estate is the organization's system of "what we tell employees and where things live," governance — roles, ownership, review cycles, permissions — is a first-class part of operating it, not an afterthought.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Employee home

The entry surface of the estate.

- typical information: targeted news, quick links, upcoming events, shortcuts to tools
- primary actions: read, navigate into sites, search, reach the directory

### Sites and pages

The long-lived content surfaces.

- typical information: policies, how-to resources, service pages for functions like HR and IT, embedded widgets (news roll-ups, links, documents, event lists)
- primary actions: read, download, follow links; for owners: edit, restructure, retarget

### News channels

The dated publishing surface.

- typical information: announcements and articles organized by channel or topic, with targeting indicators
- primary actions: read, react, comment where enabled; for authors: compose, target, schedule

### Search

- purpose: find content, documents, people, and answers without knowing where they live
- typical information: permission-filtered results from the estate (and often connected systems), with ownership or freshness cues in some products
- primary actions: query, refine, open results

### Tool access surfaces

Launchers, tiles, and embedded forms.

- purpose: reach the tools and requests employees need without leaving the estate
- typical information: link collections, app shortcuts, request forms that hand off to HR/IT systems
- primary actions: open tools, start and track requests

### Community surfaces

Spaces for employee discussion and events.

- typical information: topic spaces, posts, comments, event registrations
- primary actions: post, react, join

### Operator console and analytics

The builder/administrator side, separate from the employee view.

- typical information: site and page management, component and template catalogs, user/group administration, permission settings, content analytics
- primary actions: build, configure, grant access, review, archive, measure

## Important Rules / Behaviors

### Permissions decide visibility everywhere

Access is not a page-level gate only. What an employee sees in menus, search results, roll-ups, and community spaces follows their permissions. Restricted content does not merely fail to open — it does not appear at all. This makes the permission model simultaneously a security surface and the shape of each employee's experience.

### Targeting narrows the estate per audience

The same estate shows different content to different groups: news targeted to a site or role, navigation items scoped to a population, audience-specific home experiences. Targeting here is about *relevance of the destination*; it is not the same behavior as distributing an item to segments across channels.

### Push features ride on top of a pull core

Modern products bundle newsletters, campaigns, notifications, and signage. These push behaviors sit on top of the estate — an announcement is published on the estate *and* delivered. When the push machinery becomes the product's center of gravity and the estate secondary, the product has crossed into Employee Communication Platform territory.

### The estate is a managed artifact with a lifecycle

Content has owners and review cycles; stale items are updated, merged, or archived; products commonly provide trash/restore semantics and validation metadata. Products' own guidance treats maintenance as defining: an unmaintained estate decays into disuse.

### Structure follows organizational change

Because sites and sections model the organization, reorganizations force estate restructuring. Mature machinery keeps relationships flexible (association and shared navigation rather than hard-coded hierarchy) so surfaces can be re-connected without rebuilding content.

### Actions are entered here, processed elsewhere

Request forms, tiles, and launchers hand work to HR, IT, and business systems. The estate is the front door and the record of entry, not the fulfillment engine.

## Variants

- **Suite-native toolkit** — the platform is part of a broader productivity suite; the organization assembles the intranet from sites, pages, and components; maximum flexibility, more assembly effort.
- **Turnkey SaaS intranet** — a hosted product that ships a branded hub out of the box; faster to launch, less assembly.
- **Intranet-in-a-box** — prebuilt templates and component catalogs layered on a suite tenant, compressing time-to-launch.
- **Portal-platform machinery** — self-hosted platform frameworks from which an intranet is built; strong fit for organizations needing deep customization or data residency.
- **Comms-suite intranet module** — the web estate inside an employee communication/app product line; the same platform also carries push machinery (email, SMS, signage).
- **Center-of-gravity flavors** — knowledge-home-leaning, communications-leaning, culture/engagement-leaning, or work-hub-leaning (actions, micro-apps, agents).
- **Frontline-inclusive deployments** — access without corporate email, mobile-first experiences, shift- and location-scoped content.
- **Multi-brand / multi-subsidiary scope** — self-contained spaces with their own administrators and audiences under one platform.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Employee Communication Platform | managed, targeted *delivery* to workforce segments with reach measurement (push); the intranet is a destination employees visit (pull); the same vendors ship both, and products bundle both — the center of gravity decides |
| Employee Portal | one aggregated, curated entry surface (the front door); typically built *on* intranet machinery; the intranet platform is the broader buildable estate |
| Enterprise Wiki / Knowledge Base | open co-authoring by members vs organization-published content under designated authors and governance; intranets commonly embed wiki-like spaces |
| Enterprise Content Management | governed repository and records for business content vs the publishing/communication surface employees visit; large platforms span both |
| Enterprise Search Platform / Internal Knowledge Search | retrieval as the product vs search as one embedded capability of the estate |
| Collaborative Workspace | bounded team working container vs the organization-wide publishing estate |
| Employee Experience Platform | umbrella consolidation over several workforce domains, with the intranet as one foundation domain; not a sibling structure |
| Employee Service Portal | centers the service request loop (catalog → case → fulfillment); inside an intranet, service delivery appears as one stream among others |
| Public CMS / corporate website | audience and authentication: employees vs public visitors |

The two most important boundaries are with the **Employee Communication Platform** (mode: destination vs distribution) and the **Employee Portal** (scope: buildable estate vs single curated entry). Both are gradients rather than walls — products bundle both behaviors, vendors are shared, and analyst coverage groups these same products under intranet categories — so the center of gravity of each product is the working test.

## Representative Products

- Microsoft SharePoint (Microsoft 365) — suite-native toolkit: sites, pages, web parts, and hub sites from which the intranet is assembled
- Staffbase (App/Intranet) — the web estate inside an employee app/communication platform line, frontline-inclusive
- LumApps — standalone SaaS intranet-first vendor, now positioning as an "AI employee hub"
- Simpplr — AI-first turnkey SaaS intranet, positioned as the foundation of employee experience

The model was additionally checked against portal-platform and intranet-in-a-box implementations (Liferay, Powell Software) and against a comms vendor's own definition of the intranet as the pull-side counterpart, to avoid over-fitting to any one substrate.

## Sources

Research date: **2026-09-07**

- Microsoft Learn — Intelligent intranet introduction (SharePoint in Microsoft 365): https://learn.microsoft.com/en-us/sharepoint/intranet-overview
- Microsoft Learn — Planning your SharePoint hub sites: https://learn.microsoft.com/en-us/sharepoint/planning-hub-sites
- Staffbase Support Portal — Content Management category: https://support.staffbase.com/hc/en-us/categories/25325356852754-Content-Management
- Staffbase Support Portal — Staffbase Product Glossary: https://support.staffbase.com/hc/en-us/articles/34983080575506-Staffbase-Product-Glossary
- Staffbase Support Portal — Overview of the Intranet Menu: https://support.staffbase.com/hc/en-us/articles/360010002239-Overview-of-the-Intranet-Menu
- LumApps — Employee Intranet platform page: https://www.lumapps.com/platform/employee-intranet
- Simpplr — Modern Intranet (AI Intranet) page: https://www.simpplr.com/modern-intranet/

> Sourcing limitation: the help centers and documentation sites of LumApps and Simpplr could not be reached from the research environment on 2026-09-07 (JavaScript-only surfaces); observations for those two products rest on official product pages, and their operational details are stated more weakly than for SharePoint and Staffbase. One additional vendor (Interact Software) could not be reached at all and was excluded without any claims drawn from it. Precise numeric limits (site counts, navigation depths, caps) are product-specific and intentionally not stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
