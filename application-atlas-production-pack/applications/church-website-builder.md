# Church Website Builder

## Overview

A **Church Website Builder** is an application a church uses to build and maintain its public website. Its defining core has three parts:

```text
Hosted public website (the church's own domain, operated by the vendor)
└── Church-shaped building blocks (welcome/service info, sermons, events, giving, guest welcome)
    └── Built and maintained by non-technical church staff and volunteers
```

The managed output is not a document or a campaign but a **living public website**: the "front door" people check before visiting, where they find service times and location, watch or listen to messages, see events, give, and take a first step toward visiting. What separates this Type from a generic website builder is that the site is assembled from structures shaped around church life — provided ready-made by the product — rather than composed from generic business widgets, and that it connects into the church's operations (giving, member records, church app).

Everything else commonly bundled with these products — design libraries, podcast feeds, livestream embedding, SEO tooling, prayer walls, AI site drafts, done-for-you build services — is widespread but not what makes the product a church website builder.

## Users & Context

The primary users are **church staff and volunteers with no web background**: an administrator or communications/media volunteer who keeps the site current, a pastor who wants sermons published, an office manager who updates events. Products in this Type are explicitly designed so that "the most seasoned church volunteer" can edit the site — inline editing, templates, and pre-filled content replace coding.

The context is a small organization without a web team. A church needs a credible public web presence (service times, location, beliefs, staff, sermons, giving) but cannot justify a developer or agency retainer, and the people updating the site change frequently. Secondary users include:

- **church leadership** — approving the site's public face, branding, and messaging
- **guest-facing flows** — visitors themselves interact with the published site (plan-a-visit forms, giving, event registration), though they never see the builder
- **denominational or network offices** — in larger deployments, overseeing websites across many congregations

Typical triggers for opening the application: publishing this week's sermon, adding or changing an event, updating service times, announcing a cancellation, refreshing the design for a season, reviewing guest submissions.

## Core Model

### The Defining Core

```text
Church (identity: name, branding, locations, service times)
└── Website (hosted, public, under the church's domain)
    ├── Pages → composed of sections/blocks
    ├── Navigation menus
    ├── Design (template/theme + branding applied sitewide)
    └── Church-life objects (sermons, events, giving, guest capture, livestream, staff/ministries)
└── Operators (staff/volunteers with roles and permissions)
└── Connections (giving platform, member records, church app, calendars, social)
```

Three properties. If any one is removed, the product is no longer recognizable as a church website builder:

- **Hosted public website as the managed output.** The deliverable is a complete, publicly addressable website under the church's own domain. Hosting, security certificates, and uptime are operated by the vendor — the church never touches a server. Without this, the product is an authoring tool, not a website builder.
- **Church-shaped site structure.** The building blocks are pre-built around church life: a welcome/service-times-and-location core, a sermon/message library with podcast distribution, an events calendar, giving, and guest welcome/follow-up. The church fills in its own content rather than assembling these structures from generic widgets. Without this, the product is a generic website builder that a church happens to use.
- **Non-technical church operators.** Building and ongoing maintenance are done by staff and volunteers through template-driven, visual editing — no code. Without this, the product is a web agency service or a developer tool.

### Standard Capabilities

Mature products across the market carry most of the following. They make the builder practical; they do not define the Type.

- **Page and section editing** — pages composed of typed sections (text, image, map, forms, media); drag-and-drop or inline editing; navigation menu management.
- **Design system** — a library of church-oriented designs/templates, plus branding controls (logo, colors, fonts) that apply sitewide; in some products the entire design can be swapped without re-entering content.
- **Church identity data reused across the site** — the church's name, address, service times, and branding are entered once and surface everywhere they are needed.
- **Sermon/message publishing** — upload audio or video, categorize by date, series, topic, or speaker, attach scripture references or notes, display in a sermon hub, and distribute as a podcast feed.
- **Events** — a calendar of church events with details, images, recurrence, and registration.
- **Giving** — donate buttons or embedded giving experiences connected to a giving platform.
- **Guest capture** — "plan your visit" style forms that collect a guest's contact details and notify the church for follow-up.
- **Livestream embedding** — the weekly service stream embedded on the site; some products pair this with an automatic site notice while the stream is live.
- **Custom domain and staging** — connecting the church's existing domain (DNS/redirects), with a preview or staging address before launch.
- **SEO and analytics** — sitemaps, page metadata, search-friendly URLs, and analytics integration.
- **Multi-editor permissions** — multiple staff and volunteer editors, typically with scoped permissions (one person manages one page or form).
- **Mobile-responsive output** — the published site adapts to phones and tablets without separate mobile management.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Church-shaped building blocks
Realizations:  structured sermon hub + prayer flows + signup flows (one product);
               template with built-in sermon player, calendar, giving (another);
               pre-built sections fed automatically from the church's member records (a third)

Concept:  Non-technical operators
Realizations:  inline "click, type, save" editing; drag-and-drop sections;
               pre-populated site at signup; AI-generated draft; expert-built site handed over
```

A reader who has only seen one implementation (say, a template-based builder) should still be able to recognize the others from the core model.

## How It Works

### Establish the church identity

```text
Enter church name, address, service times, logo, colors
→ these become single-sourced data reused across the site
```

Most products start here: the identity data drives page headers, maps, contact blocks, and the design's branding. Change it once and it updates sitewide.

### Start the site

```text
Pick a path:
→ choose a church design/template and fill it in, or
→ accept a pre-populated starter site and customize it, or
→ answer a few questions and receive an editable draft (AI-assisted products), or
→ have the vendor's team build it and hand it over
```

All paths converge on the same state: a draft website the church can edit visually.

### Compose pages and fill the church-shaped objects

```text
Build the homepage first
→ add pages (about/beliefs, ministries, staff, give, events, sermons)
→ compose each page from sections
→ fill the sermon library, event calendar, giving, and guest forms with real content
→ arrange navigation menus
```

### Run the weekly loop

The ongoing work is a rhythm, not a project:

```text
Upload this week's sermon → it appears in the sermon hub and the podcast feed
→ add or update events → they appear on the calendar
→ schedule a banner or announcement for time-sensitive items (with an expiry)
→ go live on Sunday → the livestream embeds on the site (some products add an automatic notice)
→ review guest submissions and form responses → follow up
```

### Connect the church's operations

```text
Connect giving (donations flow to the church's giving account)
→ connect member records (form submissions become people records; events/sermons flow from the record system to the site)
→ connect the church app (content published once appears on site and app)
→ connect calendars, livestream platforms, and social channels
```

### Launch and maintain

```text
Connect the church's domain (DNS/redirects)
→ run a pre-launch checklist (content, privacy, SEO)
→ publish
→ ongoing: design swaps for a new season, volunteer editors added or removed, content kept current
```

### Core vs common vs optional

**Defining core** — hosted public website; church-shaped building blocks; non-technical church operators.

**Standard capabilities** — page/section editing, design library with sitewide branding, sermon publishing with podcast feed, events, giving, guest capture, livestream embedding, custom domain, SEO/analytics, multi-editor permissions, mobile-responsive output.

**Optional / variant** — AI site drafts, done-for-you build services, prayer walls with privacy controls, social-media scheduling, member-only or password-protected pages, congregant account portals, email/blog modules, multi-campus and denominational-network support.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Site editor (page canvas)

The builder's primary surface.

- the page as visitors will see it, edited inline or section-by-section
- typical information: page list, section types, content fields, publish state
- primary actions: add/edit/reorder sections, save, publish, preview

### Design / branding panel

Controls the site's appearance.

- design or template selection, logo, colors, fonts, custom styling
- primary actions: apply a design sitewide, adjust branding, advanced custom styling

### Content managers

Dedicated surfaces for the church-shaped objects.

- **sermon manager**: upload audio/video, set date/series/speaker/scripture, manage the display hub and podcast feed
- **event manager**: create events, recurrence, images, registration
- **form/flow builder**: guest-capture and signup forms, submission inboxes, follow-up triggers

### Site settings

- domain connection and redirects, staging/preview address
- SEO settings (sitemaps, page metadata), analytics keys
- privacy options for sensitive content

### People / submissions views

- form submissions and guest details, notifications, follow-up status
- in products with member-record integration, the boundary between these views and the record system varies

### Admin / permissions

- add and remove editors, set what each may manage (a single page, form, or content area)

### The public site itself

The congregant- and visitor-facing surface: pages, sermon hub, event calendar, giving, livestream, guest forms. In some products a congregant-side account (giving history, submissions) extends the public site into a light member portal.

## Important Rules / Behaviors

### The site is public; sensitive content needs explicit protection

Everything published is world-readable. Products therefore provide privacy machinery — for example, prayer requests kept out of search results and viewable only to signed-in members, password-protected pages, or private media playlists for internal material. Privacy is a structural concern, not an afterthought, because churches publish both public invitation and intimate community content on the same site.

### Church identity data is single-sourced

Name, address, service times, and branding are entered once and reused across the site. A service-time change is one edit, not a hunt through pages.

### Content objects are single-sourced and multi-surfaced

A sermon published once appears in the sermon hub, the podcast feed, and (where connected) the church app. An event appears on the calendar and in promotion surfaces. The publisher manages the object, not each surface.

### Design is layered over content

Refreshing or changing the design does not require re-entering the site's content; one product makes swapping the entire design a one-click operation. Churches redesign seasonally without rebuilding.

### Time-sensitive content can be given a lifecycle

Some products let announcements and banners be scheduled to appear and expire automatically, so stale content does not linger — a direct answer to the volunteer-maintained reality of church websites.

### The church keeps its domain; the vendor operates the hosting

The public address belongs to the church and can be pointed at the builder (and away from it). Hosting, certificates, and uptime are the vendor's responsibility — churches do not manage servers, backups, or security patches themselves.

### Editors are many and transient; permissions are scoped

Volunteers rotate. Products support multiple simultaneous editors with scoped permissions (one page, one form, one content area) so broad access is not required for narrow jobs.

### Giving is embedded, not owned

Donations initiated on the site are processed by a giving platform (native to the suite or integrated); the website builder provides the placement and the connection, not the payment rails.

## Variants

Common forms of the Type:

- **standalone builder** — a dedicated product focused on the website, integrating with whatever giving/record systems the church already uses
- **suite module** — the website builder as one product inside a church-software suite (giving, member management, apps, communication), with content flowing between modules
- **all-in-one platform** — website, giving, member records, app, and communication sold as one system with a universal login
- **build-path variants** — instant pre-populated site; template-first; AI-generated draft; expert/done-for-you build handed over to the church
- **substrate variants** — proprietary builders vs builders layered on general web platforms
- **scale variants** — single-congregation sites; multi-campus sites; denominational or network deployments overseeing many congregations' websites
- **segment flavors** — church plants (fast launch, low cost), established congregations (design refresh, sermon archives), denominations with shared design standards

A variant remains a variant unless it changes the core so much that the defining structure no longer applies.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Visual Website Builder | same substrate (hosted site, templates, visual editing), but generic business vocabulary and widgets; no church-shaped objects or church-operations integration. A church can use one — that is exactly the boundary |
| Content Management System / CMS | general-purpose content authoring and management; this Type is domain-specialized hosted site assembly for churches (some suites even wrap a CMS with church objects) |
| Church Management System / ChMS | the internal record system (people, groups, giving, events) vs the public web presence; they meet where form submissions become records and record content flows to the site. Remove the public site → ChMS |
| Church Communication Platform | targeted outbound messaging to known people vs a public web presence for anyone; they meet at guest capture → follow-up. Remove the public pages → communication platform |
| Sermon Management | the sermon record and preparation workflow vs the sermon library as a site display object with podcast distribution |
| Church Giving Platform | donation processing and management vs giving embedded or linked on the site |
| Event Management / Registration | dedicated event operations vs the site's calendar and registration objects |
| Landing Page Builder | single campaign pages vs the church's full persistent public site |

The boundary with the generic Visual Website Builder is the most important one, because the two Types share their substrate. The structural test: if the product's building blocks are church-shaped (service info, sermons, events, giving, guest welcome) and it connects to church operations, it is this Type; if it offers only generic widgets that a church could fill with anything, it is a generic website builder.

## Representative Products

- **Nucleus** — standalone, engagement-led builder (sermon hub, next-steps launcher, prayer and signup flows)
- **Tithe.ly Sites** — website builder as a module of a giving-first church software suite
- **Ministry Brands Amplify Websites** — suite module with multiple build paths (AI draft, template, expert-built); inherits legacy builders such as Clover Sites and Ekklesia 360
- **ChurchSpring** — all-in-one platform with an instant pre-populated site and volunteer-first editing

The defining core was checked against older and consolidated products (Clover Sites, Ekklesia 360, Sharefaith — now absorbed into suites) and against churches using generic tools, to avoid defining the Type by one era's or one posture's implementation.

## Sources

Research date: **2026-09-07**

- Nucleus — https://nucleus.church/ (product page); Help Center https://n2help.nucleus.church/ (Web, Sermons, Flows, Prayer, People, Posts, Messages, Giving, Church Settings collections); Web Getting Started https://n2help.nucleus.church/category/1180-getting-started
- Tithe.ly — https://www.tithely.com/ (product line); Sites product page https://www.tithely.com/product/church-website-builder (features + FAQ)
- Ministry Brands — Amplify Websites https://www.ministrybrands.com/websites (three build paths, CMS/content integration, FAQ); Clover Sites redirect https://www.cloversites.com/ (legacy-brand consolidation)
- ChurchSpring — https://churchspring.com/ and https://churchspring.com/church-website-builder/ (features + FAQ)

> Sourcing limitation: Faithlife Sites could not be reached (repeated timeouts) and is cited only as market context. Tithe.ly Sites evidence is product-page/FAQ level (help-center articles not fetched); claims about it are kept at that strength. Exact numeric limits, prices, and vendor-stated "unlimited" quotas are treated as vendor claims and are not asserted as operational facts in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
