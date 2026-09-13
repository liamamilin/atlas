# Job Board

## Overview

A **Job Board** is a third-party-operated employment venue where many independent employers advertise job openings as time-limited postings, and people looking for work search, browse, and respond to those openings.

The defining structure is small:

```text
Many independent employers, one neutral venue
└── Job posting (time-bounded advertisement of one opening)
    └── Seeker-facing discovery over the whole population
        └── Response path returning the seeker's interest to the posting employer
```

Three properties hold across every realization of the Type:

- **A population of job postings from many employers.** The unit of supply is the posting — a transitory advertisement of a specific opening at an identifiable employer. The venue is operated by a party separate from the hiring employers.
- **Seeker-facing discovery over the population.** People looking for work can find and compare openings across employers — by browsing at minimum; by keyword search, filters, and alerts in modern form.
- **A response path back to the employer.** Each posting carries or mediates a way for the seeker's interest to reach the employer — an application inside the venue, a redirect to the employer's own hiring process, or employer contact details in the posting. The venue is the meeting place; it is never the hiring party.

Everything else commonly associated with job boards — accounts and resumes, saved searches and alerts, resume databases, in-platform applications, paid promotion, AI matching — is standard in mature products but not required to recognize the Type. A newspaper's job-classified section, a public employment office's posting book, and a niche remote-work site all satisfy the three-property core.

## Users & Context

**Employers and their recruiters/hiring managers** are the supply side. They create postings for their openings, decide how widely and how prominently each posting is distributed, and review the interest that comes back. They are customers of the venue, not its operators.

**Job seekers** are the demand side. They arrive in active job-search mode: describing what they want, comparing openings across many employers, applying, and tracking what they have applied to.

**The venue operator** runs the marketplace: admission and content rules for postings, discovery quality, promotion products, and (in public-sector and association boards) a service mission in place of or alongside revenue.

The work context is high-volume and recurring on both sides: employers post openings continuously as roles open and fill; seekers run searches over days or weeks. A posting's audience is anonymous until the seeker chooses to respond.

## Core Model

### The job posting — the unit of supply

A posting is a structured advertisement of one opening. Across the researched products it consistently carries:

- job title
- the hiring organization's identity
- location (with remote/onsite/hybrid variants)
- employment type (full-time, part-time, contract, …)
- compensation, where disclosed
- the description: duties, responsibilities, requirements, qualifications, benefits
- application instructions or a deadline

Postings are **time-bounded**. They move through a managed lifecycle: drafted, published (live), then closed manually or expired when their run ends — exact state names vary by product — and can be reposted with a new run. The venue's content is therefore a **rolling current population** of openings, not a permanent registry.

### The posting population — many employers, one venue

The population aggregates openings from many independent employers under one operator. This is the property that separates a job board from an employer's own careers page, and it is what gives the board its value to seekers: one search reaches hundreds or thousands of employers' openings.

### The seeker and the seeker-side record

A seeker's presence on the board consists of:

- **identity**: an account in modern products, commonly required to apply, save, or be contacted — while browsing is often possible anonymously
- **profile and resume/documents**: the reusable material that applications draw on; mature boards let the seeker control whether this material is searchable by employers
- **saved jobs and saved searches with alerts**: standing queries against the posting population that notify the seeker when matching openings appear
- **an application record**: what the seeker has applied to, and — in mature products — where each application stands

### The response (application)

The response is the seeker's expression of interest routed to the posting employer. Three modes coexist across products, and a single product may support several:

- **in-platform application**: forms, resume attachment, screening questions, submitted inside the venue
- **redirect**: the venue hands the seeker to the employer's own site or hiring process to continue
- **direct contact**: the posting carries the employer's contact path (email address or instructions) and the response leaves the venue's machinery entirely

The applicant is visible to the posting employer through the venue's employer side; the venue's role ends at delivery and lightweight handling.

### The employer-side record set

Employers hold:

- **an employer account** (often multi-user)
- **their postings** with lifecycle status and, where promoted, budget and spend
- **the applicant flow** for each posting: who applied, application details, and a review/contact surface
- **performance data** where postings are promoted: views, clicks, applications, cost

### The searchable candidate layer

Mature boards commonly give employers a second discovery direction: a searchable database of seeker resumes/profiles accumulated on the board, with filters, saved searches, and new-candidate notifications. This is the board's employer-side search layer over its own seeker population.

### Promotion and visibility

Postings compete for attention inside the population. Boards sell visibility: promoted or sponsored placement, pay-per-click budgets, featured slots. Mature products label promoted postings and expose performance metrics to the employer.

## How It Works

### The employer loop

```text
Create employer account
→ compose a posting (title, location, type, compensation, description, application instructions)
→ [optional] attach a promotion budget and schedule
→ publish → posting goes live on the venue (larger boards also distribute it to partner sites and apps)
→ matching/alerts surface it to seekers whose preferences fit
→ applications and clicks accumulate against the posting
→ review, rate, and contact applicants from the venue's applicant surface
→ close the posting (filled) or let it expire
→ repost if the role reopens
```

Posting editors commonly include required-field enforcement, preview-as-seekers-see-it, and creation aids — templates, suggested titles, salary ranges, and skills drawn from the board's own matching data.

### The seeker loop

```text
Search or browse the population (keyword, location, filters, sort)
→ open posting detail and evaluate fit
→ save the job, or save the search with an alert
→ respond: apply in-platform, or follow the redirect/contact path to the employer
→ track applications where the board offers it (status, poster-viewed updates, personal tracker)
→ repeat over days or weeks
```

### The matching loop

Boards continuously push the population toward seekers rather than only waiting for queries: alerts on saved searches, recommendations computed from the seeker's profile and preferences, and automatic delivery of new postings that match declared interests. Employer-side mirrors exist: notification when a candidate matching a saved resume search enters the database.

### One venue, two inventories

The board runs two discovery systems over its two inventories: seekers search the **posting** inventory; employers search the **candidate** inventory. The application is the event that connects the two.

## Interfaces

### Job search / results page

The seeker's primary entry surface.

- purpose: find relevant openings across all employers on the board
- typical information: keyword and location bar, filter facets (employment type, compensation, category, remote/onsite), result cards with title, organization, location, compensation, posting age, promoted labels
- primary actions: search, filter, sort, open a posting, save a search, set an alert

### Posting detail page

- purpose: present one opening completely
- typical information: full description, organization, location, compensation, application instructions/deadline, organization context
- primary actions: apply (in-platform or via redirect), save, share, contact

### Seeker account surfaces

- profile/resume/documents management with searchability controls
- saved jobs and saved searches with alert settings
- application tracking: list of applications with status or a staged personal tracker

### Employer posting console

- purpose: create and manage postings and their visibility
- typical information: posting list with status (draft/live/closed/expired), applicant counts, views/clicks, budget and spend for promoted postings
- primary actions: create/edit posting, publish, promote with budget, close or repost, view live ad

### Applicant review surface

- purpose: handle the interest each posting receives
- typical information: applicant list with application details, resume, new/needs-review indicators
- primary actions: review, rate, message, reply/acknowledge (some boards provide auto-responses)

### Resume/profile search surface

- purpose: let employers discover candidates proactively on the board's own seeker base
- typical information: candidate cards with experience, skills, location, activity recency; filter facets
- primary actions: search, save search, view/contact candidate (often metered), message

### Settings and billing (employer)

- promotion budgets, credits/plans, team members, integrations

## Important Rules / Behaviors

### Postings are transitory

A posting is an advertisement with a run, not a permanent record. It closes when filled or withdrawn and expires when its run ends; the population continuously turns over. This transience is the structural seam against directories and registries.

### The response path belongs to the employer

Whatever the mode — in-platform, redirect, or contact details — the employer's process takes over after delivery. The board's applicant handling is deliberately lightweight: review, rating, messaging. Requisition management, interview loops, and hiring decisions live in the employer's own systems; boards commonly integrate with those systems rather than absorb them.

### Application submission is typically one-way

Several products do not allow editing or withdrawing an application once submitted through the venue; corrections route through contacting the employer. Boards differ on this — it is a product-dependent rule, not a universal one.

### Seeker visibility is controlled

Searching and applying are private activities by default; the seeker's network is not notified, and their identity becomes visible to an employer only through the response or through explicit searchability settings. Availability signals (for example, "open to work") are opt-in and can be scoped to a narrower audience than the whole board.

### Promotion affects visibility, and is labeled

Paid placement raises a posting's prominence; it does not change what the posting is. Products that sell placement label promoted postings and account for them with per-posting budgets and metrics.

### Eligibility can gate application

Some boards restrict who may respond: public-employment sites apply statutory eligibility and hiring-path rules; association and member boards gate application or pricing to their audience; employer-facing rules can screen applicants with required questions. The posting's response path is therefore a governed path, not always an open one.

## Variants

- **General commercial boards** — the classic form: broad categories, employer-pays posting and promotion, full seeker machinery (accounts, resumes, alerts), resume search, applicant handling.
- **Niche / vertical boards** — scoped to a labor-market segment (remote work, technology, healthcare, hourly work). Machinery is often thinner; value comes from audience fit. Attribute-rich postings and demand-signal sorting (by salary, most-applied) are common here; seeker-pays premium models appear.
- **Government / public employment services** — the state as operator: postings from many agencies, statutory structure in the posting (eligibility, required documents, evaluation method), free access, tracked application lifecycle as a public service obligation.
- **Association / member boards** — run by professional or membership organizations for their audience, with member identity and pricing; the machinery is the board's, the operator and purpose differ.
- **Review-attached boards** — job postings alongside community content about employers (reviews, salary data); the postings machinery is unchanged, the seeker's evaluation context is richer.
- **Aggregators** — boards whose posting supply is largely harvested from employers' own sites and other boards, with the response path routed back to the source. Same defining core, different supply model.
- **Monetization shapes** — per-post fees, pay-per-click/performance budgets, employer subscriptions, credit systems, free public service, seeker-pays premium, advertising.
- **Response-mode mix** — the same market spans in-platform applications, profile-prefill, redirects to employer sites, and plain contact details.
- **Thin vs full-stack** — a board can be a bare listing surface with per-posting apply, or carry the full modern stack (accounts, matching, trackers, resume databases, promotion analytics) without changing its nature.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Career Site Platform | one employer's own public careers surface under its own brand; the ownership test — whose openings the surface lists — separates the two; boards distribute to career sites and redirect to them |
| Classifieds Platform | generic ad-contact listings without the two-sided candidate machinery; a classifieds site's jobs category is the pure-ad pole of the same market; remove the candidate machinery (profiles, apply flows, applicant handling) and a board degrades into classifieds |
| Listings Platform | the generic expiring-offer Type; the Job Board is its employment-domain realization with job-specific semantics (openings, applicants, eligibility) |
| Online Marketplace | mediates a transaction between the sides with payment flowing through the platform; a board mediates interest, not commerce — nothing is bought, no checkout exists |
| Applicant Tracking System / Recruiting Management Platform | the employer-side pipeline system of record: requisitions, approvals, interview stages; a board's applicant surface is a lightweight front door, and boards integrate with ATSs rather than replace them |
| Candidate Search Platform | opposite direction and object: employer searching for people, usually over an external corpus; a board's resume search is the employer-side layer over the board's own seeker base |
| Professional Social Network | professional identity, network, and feed are the primary objects; jobs are one surface; network-embedded job surfaces deliver the board's machinery inside a larger product |
| Association Job Board | identical machinery under a membership-organization operator, presented as a member service with member identity/pricing; an operator/audience variant of this Type |
| Public Employment Service Platform | the state as employment-services operator; same posting/apply machinery, often with added casework/referral obligations — the boundary with that Type is recorded for its own research pass |
| Vertical Search Engine | a pure search surface over harvested postings with no postings of its own and no response machinery; aggregation with a hosted response path stays a board |

## Representative Products

- **LinkedIn (Jobs surfaces)** — the board delivered inside a professional network; richest seeker-side machinery and labeled promoted postings
- **Monster** — the classic general commercial board: self-serve employer platform, pay-for-performance promotion, resume search product
- **USAJOBS** — the government-operated pole: many federal agencies, structured announcements, tracked applications, free public service
- **RemoteOK** — the thin niche pole: remote-work only, attribute-rich postings, paid posting, minimal machinery

The defining core was checked against pre-digital realizations (newspaper job-classified sections, public employment posting offices) to avoid over-fitting the definition to the modern account-based stack.

## Sources

Research date: **2026-09-07**

- LinkedIn — Help Center, "Search and Apply for Jobs" topic and articles (apply modes, alerts, saved jobs, recommendations, promoted jobs, resume sharing, job tracker): https://www.linkedin.com/help/linkedin
- Monster — hiring site Help Center and product pages (posting creation and lifecycle states, promotion budgets, applicant management, resume search): https://hiring.monster.com/help-center/ , https://hiring.monster.com/products/post-a-job/ , https://hiring.monster.com/products/resume-search/ , https://www.monster.com/
- USAJOBS (U.S. Office of Personnel Management) — Help Center (job announcement structure, closing types, application lifecycle, search facets, About): https://help.usajobs.gov/how-to , https://help.usajobs.gov/about
- RemoteOK — site surface (attribute filters, sorting, paid posting, premium, feeds): https://remoteok.com/

> Sourcing limitation: several major boards (Indeed, ZipRecruiter, SEEK, Glassdoor) and the classifieds pole (Craigslist) were not fetchable from the research environment on 2026-09-07. They are treated as market context only; no operational claims, market shares, prices, or limits are asserted for them in this document. Precise product-specific figures observed in accessible sources (plan prices, credit costs, activity counts, stored-resume counts) were deliberately kept out of this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary reasoning are recorded in the paired Research Notes.
