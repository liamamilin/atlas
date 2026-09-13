# Career Site Platform

## Overview

A **Career Site Platform** is employer-side software for building and operating an organization's own public careers web presence — the site on which the organization presents itself as an employer, lists its open positions, and through which candidates apply.

It exists to solve three standing problems:

- an employer's openings change constantly, and the public site must reflect that state automatically, without hand-editing web pages;
- the site must express the employer's brand — culture, teams, locations, people — and stay up to date, ideally without involving developers for routine content;
- interest expressed on the site must be captured reliably and handed into the organization's recruiting process.

The canonical boundary: the site belongs to **one organization** and presents **that organization's own openings**. A public surface aggregating many employers' jobs is a job board; the recruiter-side process that receives the applications is the applicant tracking system; the paid-channel and campaign machinery that drives traffic to the site is recruitment marketing. Many vendors sell these together, but the career site is the employer-owned public storefront itself.

## Users & Context

**Employer-side operators** are the primary users:

- **Talent acquisition / recruiting operations** — publish job content, keep openings current, monitor whether the site is converting visitors into applicants.
- **Employer brand / talent marketing staff** — build and maintain brand pages (culture, values, benefits, locations, people), landing and campaign pages, and the site's look and feel.
- **Administrators** — configure domains, editor access, integrations to the recruiting backend, and site-wide settings.
- **Hiring managers** — in some products, submit or draft job content themselves; publication then passes through an approval step controlled by recruiting or admin roles.

A recurring design point: routine editing is deliberately taken away from IT. Mature products let employers invite non-technical contributors — for example marketing or design staff — as scoped page editors who can adjust content and styling without accessing the rest of the recruiting system. Developers appear only for the self-built delivery option (see Variants).

**Candidates** are the audience, not operators: they arrive from search engines, shared links, or the corporate website's "Careers" link, and browse, search, read, and apply. The site runs continuously alongside the organization's main website, and its live set of openings changes frequently — which is precisely why the job data, not hand-edited pages, must drive it.

## Core Model

### The defining core

```text
Organization's openings (managed job records)
  → published as public job pages (public visibility follows publication state)
    → organized for discovery (jobs page, departments, locations)
      → candidate response path on each opening
        → captured candidate record / handoff into the recruiting process
Supported by:
Employer-brand content pages + site design, both employer-managed
```

Four properties carry the Type. Remove any one and it is no longer a career site platform:

- **An employer-operated public careers web presence.** A public site dedicated to one organization's employment opportunities, operated by that organization. It may be hosted by the platform, embedded into the corporate website, or built by the employer on top of the platform's data — but the presence itself is the employer's, in the employer's brand.
- **Job content bound to the organization's own openings.** The site's primary content is pages for the organization's actual open positions, rendered from managed job records. Publication state is the visibility switch: publishing a job makes it findable on the site; closing, expiring, or removing it takes it off. The site mirrors the state of the employer's job data — it is a projection of it, not an independent list.
- **A candidate response path on every opening.** Each public listing offers a defined way to respond: an application form on the site, a redirect to an external application page, an instructed contact channel, or an off-site apply method. Expressed interest becomes a candidate record or is handed off into the recruiting process with its source attached.
- **Employer-side management machinery.** The employer — recruiting, brand, or marketing staff rather than developers, as a rule — controls branding, page content, and job publication through the platform: a no-code site editor, site settings with delegable editor roles, or a management API feeding an employer-built front-end. Without this, it is a hand-built web page, not a platform.

### Standard capabilities

Everything above is what makes the Type. Mature products add a common layer that makes it practical:

- **Discovery over openings** — keyword search plus filters (department, location, custom attributes), grouping and listing views, sometimes map layouts.
- **Generated structure pages** — department and location overviews (and often a page per department/location) produced automatically from account data rather than maintained by hand.
- **Employer-brand content pages** — home/landing pages, culture and values, benefits, teams, locations, employee profiles and testimonials, and ongoing content posts.
- **No-code design layer** — colors, fonts, logos, banners, and buttons matched to the employer's brand, with preview before publishing.
- **Application machinery** — configurable application forms and questions; conditional logic and rich question types in some products.
- **Backend seam** — applications and captured leads flow into the ATS or candidate pool; job records sync from (or bi-directionally with) the recruiting/HR system.
- **SEO and sharing** — meta and sharing images, sitemaps, custom domains, shareable and trackable links that count visits and applications.
- **Accessibility posture** — documented accessibility behavior, ranging from statements to explicit compliance choices for the site and its forms.
- **Multi-surface governance** — for larger employers: multiple boards or sites scoped by brand, language, country, or business entity, managed from one platform.
- **Site performance measurement** — traffic, visits, and applications by source, and conversion of visitors to applicants.

### One structure, many realizations

The core is conceptual; products realize each part differently:

```text
Site realization:   hosted site builder  |  embedded surface inside the corporate site  |  employer-built front-end over the platform's API
Job data source:    native records in the platform  |  synced from an ATS/HR system  |  fed through an API
Response path:      on-site application form  |  redirect to an external form  |  instructed contact channel  |  off-site apply integration
Scale structure:    one site  |  multiple boards/sites per language, brand, or entity
```

One sampled product documents all three site realizations as formal options of the same account — and notes that every option updates automatically when jobs are posted or removed. That sentence is the clearest market statement of the model: the job records are the truth, and the public site is a delivery surface over them.

## How It Works

### The job publication loop

```text
Opening created or synced into the platform
→ job content completed (description, location, department, attributes)
→ publication state set (immediately, on approval, or on a scheduled date)
→ job page goes live and becomes findable through the site's jobs page, search, and filters
→ opening closes or its end date passes
→ job page is withdrawn from the site; applications stop
```

The loop is the platform's engine: the employer's job data drives every public surface, and no step requires touching site templates. Where roles are split, a hiring manager may draft the job while recruiting or admin roles hold the publish authority.

### The site-building loop

```text
Set site-wide design (fonts, colors, logos)
→ structure the site: default pages generated from account data (home, jobs, departments, locations, people)
→ add custom pages and content blocks (culture, testimonials, videos, calls to action)
→ preview changes privately
→ publish to the public site
→ iterate: campaign pages, landing pages, and posts for hiring pushes
```

This is a content-management loop specialized for recruiting: the building blocks, default pages, and content types (jobs, departments, locations, people, testimonials) are recruiting-shaped rather than generic.

### The candidate journey

```text
Candidate arrives (search engine, shared link, corporate-site "Careers" link)
→ lands on the home or jobs page
→ searches or filters openings; reads job pages and brand content
→ responds: completes the application form, follows a redirect, or submits contact details
→ application/candidate record is created and handed into the recruiting process, source attached
```

A second, lighter path exists for passive visitors: **lead capture** surfaces that ask for contact details instead of an application, creating a candidate record linked to a role for later outreach. Some products formalize this as talent communities that are then nurtured through email or messaging campaigns.

### The backend seam

The platform connects to the recruiting system of record. In ATS-embedded products the seam is internal; in standalone products it is a documented integration that syncs job data (requisition status, locations) and pushes applications and candidate records back. Off-site apply integrations (apply directly on large external job boards) extend the same seam outward — the application still lands in the recruiting backend, but the career site is bypassed.

### Capability tiers

**The defining core** — without these, not a career site platform:

- employer-operated public careers web presence
- job pages driven by the organization's own openings, with publication state controlling visibility
- a candidate response path on each opening
- employer-side management of design, content, and publication

**Standard capabilities** — present in most current products:

- search and filters over openings; generated department/location structure
- employer-brand pages and content blocks; no-code design with preview
- application forms and lead capture; ATS/candidate-pool handoff
- SEO/sharing machinery; accessibility posture; site analytics; multi-brand/multi-language governance

**Optional, segment-dependent capabilities** — depending on scale, philosophy, and era:

- AI-driven personalization of jobs and content, semantic search, chatbots, generative content drafting
- passive-talent machinery (lead pages, talent communities) with campaign nurture
- scheduled publishing, expiry dates, unlisted test postings, role-based publication approval
- internal-only job boards alongside the public site
- employee-profile and employee-story content programs
- candidate self-scheduling surfaces styled with the site's brand

## Interfaces

**Employer-facing surfaces** (inside the platform):

- **Career site editor** — the site as pages and blocks. Purpose: build and maintain the public presence. Typical content: page tree (default and custom pages), content blocks, design settings. Primary actions: add/edit pages and blocks, set design, preview, publish.
- **Job publishing view** — the openings list with their publication states. Purpose: control what is public. Typical information: job, status (draft, pending approval, published, scheduled, unlisted, expired, archived, internal), dates. Primary actions: create/edit, publish, unlist, archive, bulk changes.
- **Settings** — domains, languages, editor roles, integrations to the recruiting backend, SEO defaults. Primary actions: connect domain, invite page editors, configure sync and apply behavior.
- **Site analytics** — visits, traffic sources, applications and conversion per job or source. Primary actions: review performance, trace shareable links.

**Candidate-facing surfaces** (the public site):

- **Home / landing pages** — first impression of the employer; brand imagery, headline content, calls to action into jobs or lead capture.
- **Jobs page** — the searchable list of openings. Typical information: title, location, department, often filters and map views. Primary actions: search, filter, open a job.
- **Job page** — the opening itself. Typical information: description, location, department, team, application questions. Primary actions: apply, share, sometimes join a talent community instead.
- **Department / location pages** — generated overviews plus per-team or per-site brand content, leading into their openings.
- **Lead / talent-community pages** — campaign-style pages asking for contact details rather than an application; submission creates a candidate record for follow-up.

## Important Rules / Behaviors

- **Publication state is the visibility switch.** A job that is draft, unlisted, internal, or archived does not appear on the public site; only published openings are findable. Some products add a scheduled start date and an expiry date that withdraws the job automatically.
- **The site mirrors the job data.** When a job is removed or closed in the source system, it disappears from the public site — across hosted, embedded, and API-built realizations alike. Employers cannot rely on the site to show stale openings, and must not treat it as an independent content store.
- **Approval may gate publication.** In some products, jobs created by hiring managers enter a pending state until a recruiting lead or administrator publishes them. Unlisted states can double as staging: a job reachable by direct link, used to test the full application flow before going public.
- **Every listing needs a live response path.** Disabling the careers surface removes the ability to apply; a redirect-based apply breaks if the external form changes. The response path is part of the listing's integrity, not an accessory.
- **Accessibility shapes the tooling.** Because careers sites are public and employment is a regulated context, products document accessibility behavior for the site, its forms, and candidate-facing sub-pages; deeper customization trades convenience against compliance headroom.
- **Brand governance scales by scoping.** Multiple boards or sites per language, brand, or business entity inherit or override site-wide design; in some products, styles applied at the board level extend to candidate-facing sub-pages (forms, scheduling) so the experience stays consistent.
- **Captured candidate data is regulated data.** Contact details and applications collected on the site fall under the employer's privacy obligations; products provide privacy and consent controls around the capture flow.

## Variants

- **Packaging.** The same Type ships three ways: as a named standalone product within an enterprise talent-experience or recruitment-marketing suite (career site with its own CMS); as a module embedded in an ATS (the common mid-market and SMB shape); and — less commonly — as an independent site builder over an external job source via API.
- **Delivery realization.** Hosted site builder on a platform domain or the employer's custom domain; an embeddable surface (widget/embed) inside the corporate website that inherits its styling; or a fully employer-built front-end consuming the platform's job and application APIs. Employers can migrate between these as they grow.
- **Scale structure.** Single site for one brand; multiple boards/sites per language, country, or business entity; global site networks consolidating many country sites into fewer multi-language ones.
- **Job data posture.** Native job records managed in the platform itself; records synced from an ATS/HR system (sync direction varies by product); records fed by API into a custom front-end.
- **Passive-talent depth.** None (pure job listing) → lead pages → standing talent communities with nurture campaigns. Enterprise suites push furthest here.
- **AI posture.** Static listing sites still function; increasingly, products add personalized job and content recommendations, semantic search, conversational assistants on the site, and generative drafting of job and brand content. None of these are required for the Type.
- **Internal surfaces.** Some products run internal job boards or internal job statuses side by side with the public site, explicitly excluded from it — an internal-mobility variant that shares the machinery but serves employees.
- **Segment tuning.** University/early-careers sites, high-volume hourly hiring, and per-industry brand content appear as specializations rather than separate structures.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Job Board | adjacent, easily confused by naming | a job board aggregates postings from **many** employers behind a neutral venue; the career site presents **one employer's own** openings on the employer's own presence. (Some ATS products call their hosted single-employer surface a "job board" — product vocabulary, not this Type.) |
| Applicant Tracking System / ATS | complementary; often same platform | the ATS is the recruiter-side pipeline (requisitions, candidates, stages, outcomes); the career site is the candidate-facing public storefront that feeds it. Applications from the site are handed into the ATS. |
| Recruitment Marketing Platform | broader demand-generation layer | recruitment marketing spans paid channels, job distribution, candidate CRM, and attribution; the career site is the owned surface those efforts drive traffic to. Enterprise vendors sell both; the surface is shared vocabulary. |
| Content Management System / CMS; Visual Website Builder | adjacent authoring tools | generic web authoring has no job-content binding, no generated job/department/location structures, and no apply machinery. An employer *can* build a careers page inside a generic CMS — career-site products document exactly how to connect their job data and apply flow to such pages, which confirms the two are different Types. |
| Employee Portal / Internal Talent Marketplace / Career Development Platform | internal-facing counterparts | those serve existing employees (services, internal mobility, development); the career site is external and pre-application. Products enforce the split explicitly — internal jobs are kept off the public site. |
| Corporate Intranet / Intranet Platform | adjacent infrastructure | the intranet serves employees inside the organization; the careers site serves outsiders deciding whether to join it. |

The sharpest boundary is the Job Board one, and it is a test of ownership, not of features: **whose openings does the public surface list?** One employer's own, under that employer's brand and domain — career site. Many employers', searchable across them — job board.

## Representative Products

- **Phenom** — enterprise talent-experience suite; career site sold as a named product with its own no-code CMS ("Design Studio"), personalization- and AI-led.
- **Radancy** — enterprise recruitment-marketing suite; operates a dedicated "Career Site & CMS" product area (with branded candidate experience) inside its Talent Acquisition Cloud.
- **Teamtailor** — mid-market ATS-first product with a first-class career site builder (default pages, content blocks, lead pages, multi-language).
- **Greenhouse** — enterprise/mid ATS; hosted customizable job-board surfaces plus documented options for integrating them with the corporate careers page.
- **Workable** — SMB/mid ATS; documents three careers-page delivery options (hosted builder, embeddable widget, API-built) as formal alternatives.

Together these cover the enterprise-suite pole, the ATS-embedded mid-market pole, and the SMB pole, and document all major delivery realizations.

## Sources

Research date: **2026-09-07**

Teamtailor (official support center):

- https://support.teamtailor.com/ (Career Site & Content; Publish Jobs; Multi-Brand & Entity Solutions collections)
- https://support.teamtailor.com/en/articles/128990 (Building your career site)
- https://support.teamtailor.com/en/articles/9881375 (Career site: Default pages)
- https://support.teamtailor.com/en/articles/2904179 (Career site: Lead pages)
- https://support.teamtailor.com/en/articles/2611060 (Job statuses)
- https://support.teamtailor.com/en/collections/33020 (Publish Jobs)

Greenhouse (official support):

- https://support.greenhouse.io/hc/en-us/articles/21270826058907 (External job board overview)
- https://support.greenhouse.io/hc/en-us/articles/18996861758363 (Customize your job board)
- https://support.greenhouse.io/hc/en-us/articles/11913197669019 (Getting started with careers page integration)

Workable (official help):

- https://help.workable.com/
- https://help.workable.com/hc/en-us/articles/115012944968 (Comparing careers page options)

Phenom (official product pages):

- https://www.phenom.com/career-site
- https://www.phenom.com/cms

Radancy (official pages):

- https://www.radancy.com/
- https://support.radancy.net/hc/en-us (support-center taxonomy)

> Sourcing limitation: Radancy's operational career-site documentation is behind customer login and was not reachable; claims from that vendor are limited to its public product positioning and the publicly visible support-center structure. Phenom has no public operational help center; its statements were used only where the underlying structure is corroborated by other vendors' operational documentation. Precise limits, defaults, and tier conditions from individual products are intentionally not asserted in this document; they are recorded in the paired Research Notes.
