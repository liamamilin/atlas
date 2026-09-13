# Research Funding Discovery Platform

## Overview

A **Research Funding Discovery Platform** is the funding seeker's discovery system over a corpus of funding opportunities offered by many sponsors. It maintains a structured, continuously updated collection of opportunity records — each describing a specific grant, fellowship, award, or similar offering: what it funds, who is eligible, by when, and for how much — and provides the search, filtering, and matching mechanisms through which researchers and research institutions find the opportunities worth pursuing.

The defining core is small:

```text
Funding-opportunity corpus (many sponsors, one seeker-facing collection)
└── Seeker-side discovery over that corpus
    (search / browse / filter / match → evaluate → retain → stay informed)
```

Everything else commonly associated with these products — researcher profiles, AI recommendations, email alerts, curated lists, funder intelligence, institutional dissemination tools — is standard capability layered on that core, not what makes the product a funding discovery platform. A printed directory of research grants with a good index, or an emailed list of new opportunities, satisfies the same defining structure without any of the modern layer.

The platform is held **for the seeker** and aggregates **many sponsors**. When the system is held by a funder to run its own programs, or by an institution to administer its own applications and awards, it has become a different Application Type (Grantmaking Platform, Research Grant Management).

## Users & Context

The primary user is a **researcher** (principal investigator, faculty member, postdoc, graduate student) looking for money to fund a research program — typically with a specific project in mind and a set of constraints (career stage, citizenship, discipline, institution).

The second primary user is the **research office** — research development and pre-award staff whose job is to make sure the institution's researchers see relevant opportunities. They configure and curate what colleagues see, run targeted dissemination, manage internal deadlines (such as limited-submission sifts), and report on usage.

Secondary users:

- **research administrators** who manage the institutional subscription, user provisioning, and default settings
- **institutional leadership** consuming aggregate views of funding activity for planning

A closely related market serves **nonprofit organizations and professional grant writers** doing the same kind of work for program funding rather than research funding (see Variants).

The work context is periodic and deadline-driven: researchers check in between project milestones, respond to alerts, and intensify their searching when preparing proposals. Research offices work the platform continuously as part of their service to faculty.

## Core Model

### The opportunity record

The unit of the collection is the **funding opportunity**: a persistent, identified record describing one funding offering from one sponsor. Across the researched products, opportunity records consistently carry:

- **identity** — a title and an opportunity number or identifier used to reference the record unambiguously
- **sponsor** — the government agency, foundation, corporation, or other entity offering the funding
- **description** — what the funding supports, often with structured keywords or category assignments
- **eligibility** — who may apply: applicant types (faculty, student, nonprofit…), citizenship/residency requirements, applicant and activity locations, institutional types
- **funding shape** — the instrument or type (grant, fellowship, prize, training program, cooperative agreement) and typically a maximum award amount
- **timing** — deadline(s) or closing date, sometimes forecast dates for opportunities not yet officially announced
- **status** — whether the opportunity is announced and open, closed, or retained as a historical record
- **application information** — how and where to apply, contacts, related documents

The record persists and is maintained: when a sponsor changes a deadline or revises the program, the record is updated, and users who follow it are notified. Opportunities related to each other (renewals, companion calls) are commonly linked and shown together.

### The sponsor/funder layer

Alongside opportunities, mature products hold records about **sponsors and funders** themselves: who they are, what they fund, and — in several products — what they have funded in the past. Past-award and giving-history data lets a seeker judge a funder's typical award size, priorities, and openness to new applicants before investing effort in an application.

### The seeker-side interest model

Discovery is driven by a model of what the seeker is looking for. Two realizations exist, and they are the same concept at different scales:

- **researcher profile** — an individual's research interests (keywords or phrases, often generated from publications or a CV), discipline, career stage; the basis for personalized recommendations
- **organizational project criteria** — a program area or funding goal described by mission, location, funding use, funder-type preferences, and target grant size; the basis for matching in organization-oriented products

### Saved searches and alerts

A **saved search** is a persistent query over the corpus; an **alert** is its notification channel. New or modified opportunities matching the query are pushed to the user — commonly as periodic email digests. This is the mechanism that turns a one-time search into continuous awareness, and it is the most universally implemented capability across the Type.

### Curated and institutional collections

Beyond the raw corpus, the collection is organized into **curated lists** (editorially selected, most-popular, profile-matched) and **institution-local collections** — internal funding programs, shared lists assembled by research offices, and channels through which the institution promotes specific opportunities to its members.

### Concept and implementation, separated

```text
Concept:                       Common implementations:
Opportunity corpus assembly    editorial curation · automated crawling with
                               human verification · direct posting by sponsors ·
                               aggregation from funder websites and public filings

Seeker interest model          researcher profile (publications-derived interests) ·
                               organizational project criteria

Matching                       keyword search · saved-search alerts ·
                               profile-based recommendation · AI/semantic search
```

A reader who has only seen one implementation — say, an AI-recommended feed — should still be able to recognize a purely search-and-alert product as the same Type.

## How It Works

### Assemble the corpus (continuous, mostly invisible to the user)

Opportunities enter the collection through one of the assembly models above — editors reviewing sponsor announcements, crawlers harvesting funder websites, sponsors posting directly, or aggregation from public filings. Records are verified, structured, indexed, and updated as sponsors revise them. The user sees the result: a current, searchable corpus.

### Establish the seeker's interest

```text
Join via an institution or organization
→ create a profile (research interests, career stage)
   or set up a project (program area, funding needs, constraints)
→ optionally: administrators pre-configure defaults or auto-create profiles
```

The interest model is what powers recommendations; a search works without it, but matching does not.

### Discover

Three routes into the corpus, which products combine:

```text
Search        keyword / advanced / faceted queries over the corpus
Browse        curated lists, categories, sponsor directories, popular picks
Receive       profile- or criteria-based matches, pushed as alerts
```

Search results are filtered by the eligibility and timing facets that matter to the seeker — applicant type, citizenship, location, sponsor type, funding type, amount, deadline window — and sorted by relevance, deadline, or recency.

### Evaluate an opportunity

The seeker opens the opportunity detail: what it funds, whether they are eligible, when it closes, how much it offers, how to apply. At this point the platform's job is to present the record faithfully; the judgment about whether to pursue is the user's.

### Retain and track

Opportunities worth acting on are saved — to a personal list, a shared institutional list, or a tracked pipeline with deadlines, owners, tasks, and status. Saved opportunities become the seeker's working set; deadline reminders and change notifications keep it current.

### Stay informed

The alert loop closes the workflow: saved searches, profile matches, and followed opportunities generate ongoing notifications as the corpus changes. Discovery is not a single session but a standing awareness maintained by the platform.

### Where the workflow ends

The platform's responsibility ends at an informed, tracked opportunity. Preparing and submitting the application, and administering any resulting award, belong to the application/pre-award process and to grant management systems. One government portal in the sample attaches application submission directly to discovery; that is an extension, not the defining shape.

## Interfaces

Described in conceptual terms; exact layouts and names vary by product.

### Search page

The primary work surface.

- basic keyword search plus an advanced mode with combined criteria
- eligibility and timing facets (applicant type, citizenship, location, sponsor type, funding type, amount, deadline window, status)
- results list with per-record summary (title, sponsor, deadline, amount) and sorting
- primary actions: run a search, refine with facets, save the search, export results

### Opportunity detail

The evaluation surface.

- full record: description, eligibility, deadlines, amount, sponsor information, application instructions, related opportunities
- primary actions: save/bookmark, share, subscribe to updates on this opportunity, follow links to the sponsor

### Profile / project setup

The interest-model surface.

- researcher profile: interests/keywords, career stage, publications; or project criteria: program description, locations, funding use, funder types, grant size
- primary actions: create/edit the profile or project, generate interests from a CV or publications, adjust recommendation filters

### Recommendations / matches view

The pushed-discovery surface.

- opportunities matched to the profile or project, sorted by fit
- primary actions: review, save to a list or tracker, hide (with a reason/note), refine the matching criteria

### Saved searches and alerts management

- list of saved searches with their criteria and notification settings
- primary actions: edit criteria, enable/disable alerts, view current results

### Institutional administration console

The research office's surface.

- shared and curated lists, internal opportunity entries, dissemination to members or groups, default settings per user type, usage reporting
- primary actions: curate and share lists, add internal opportunities, configure defaults, view usage

### Tracker / calendar (where offered)

The working-set surface.

- saved opportunities organized by deadline, status, owner, or project; deadline calendars and reminders
- primary actions: update status, assign owners, add notes and tasks, set reminders

## Important Rules / Behaviors

### Opportunity lifecycle states

Opportunities move through a lifecycle that the platform makes visible: announced/open, closed at the deadline, and retained as a historical record; some products also carry a **forecast** state for planned opportunities that are not yet officially announced — with the explicit caveat that a forecast may never become a real call. Deadline status is therefore both data and a filter: seekers search differently for opportunities closing this month versus those announced for next year.

### Eligibility is both filter and gate

Eligibility fields (applicant type, citizenship, location, institutional type) let seekers narrow searches — but they also mean a record can be irrelevant or inaccessible to a given seeker no matter how well it matches topically. Mature products treat eligibility as a first-class facet, and mismatched eligibility is a common reason to discard an otherwise attractive match.

### Deadlines are the operating rhythm

The deadline drives sorting, filtering, calendar views, reminders, and the urgency of the whole workflow. When a sponsor changes a deadline on a followed opportunity, the platform notifies followers — a documented behavior in several products, and one of the platform's core value claims over manual monitoring.

### Limited submission

Some opportunities allow only a bounded number of applications per institution. Products flag these records and institutions commonly run internal selection processes; the platform supports the flag and the internal channel, while the selection decision itself remains an institutional process.

### Data provenance varies and is a quality claim

Vendors differ on how records are produced — editorial teams, verified crawling, direct sponsor posting, aggregation from public filings — and market that provenance as their accuracy guarantee. The user-visible consequence is the same (a maintained record), but update speed and coverage differ by model; the platform's trustworthiness rests on this invisible layer.

### Access is typically mediated

Most products are licensed to institutions or organizations rather than sold to individuals: access is gated by institutional membership, and features like saving searches and receiving alerts usually require an individual account within that license. Free public portals exist as a distinct access model.

## Variants

- **editorially curated academic platforms** — in-house editors verify and index opportunities from thousands of sponsors; strongest in large research institutions (the classic research-administration subscription)
- **crawl-and-verify academic platforms** — automated harvesting of sponsor sources with specialist verification; often positioned as the accessible, modern alternative
- **sponsor-posted government portals** — the official discovery face of a national grant ecosystem; free, authoritative, limited to that government's agencies, and sometimes attached to application submission
- **news-integrated funding intelligence** — the opportunity database bundled with editorial research-policy news and funding guidance, common in the UK/European market
- **suite-embedded discovery** — the funding database consumed inside a broader research-administration platform rather than as a standalone product
- **nonprofit grant-seeking platforms** — the same core model serving nonprofits and grant consultants: project-based matching, funder intelligence from public tax filings, and pipeline tracking; funding domains are program areas rather than research disciplines
- **AI-forward variants** — semantic search, plain-language project setup, and profile-based recommendation engines layered over the same corpus

A variant remains a variant while the defining core holds. When the system starts administering the institution's own applications and awards, it has crossed into Research Grant Management; when it is held by a funder to run its own programs, it has crossed into Grantmaking Platform.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Research Grant Management | manages the institution's own applications and awarded grants through their lifecycle; this Type ends at a discovered, tracked opportunity |
| Grantmaking Platform | funder-side: designing programs, accepting and reviewing applications, making awards; this Type is seeker-side over many sponsors |
| Government Grants Management | the granting government's internal administration of its programs; this Type is the public discovery face, aggregating across sponsors |
| Academic Search Engine | retrieves literature and documents; this Type retrieves fundable opportunities with eligibility, deadline, and amount semantics |
| Vertical Search Engine | general vertical retrieval; this Type is domain-structured around the opportunity record and the alert/match loop, not document ranking |
| Lead Generation Platform | the commercial structural analog (database + matching + alerts + pipeline), but with sales-lead semantics instead of funding semantics |
| Research Administration Platform | the institution's wider research operations; this Type's discovery layer is often consumed inside it, but discovery alone is the narrower Type |

The most important boundary is with **Research Grant Management**: the unit of work decides the Type. If the system's working object is the opportunity (seeker-side, multi-sponsor corpus), it is a funding discovery platform; if it is the application or award (institution-side lifecycle), it is grant management. Products that bundle both exist, and the discovery layer inside them remains this Type.

## Representative Products

- **Pivot-RP** (Clarivate) — editorially curated global funding database with researcher-profile matching and institutional workflow tools
- **GrantForward** — crawl-and-verify funding database with profile-based recommendations and institutional dissemination tools
- **SPIN** (InfoEd Global / Digital Science) — long-established sponsor-sourced funding database with profile-based alerting, often embedded in research-administration suites
- **Research Professional** — UK/Europe-centered funding database integrated with research-policy news and weekly alerting
- **Grants.gov** — the free US federal discovery portal; opportunities posted directly by agencies, with saved-search subscriptions
- **Instrumentl** — nonprofit/university grant-seeking platform: project-based matching, funder intelligence from public filings, and pipeline tracking

The defining core was checked against all six, spanning editorial, crawl-verify, sponsor-posted, and filing-aggregation corpus models, and free, institutionally subscribed, and organizationally subscribed access models.

## Sources

Research date: **2026-09-10**

- Pivot-RP — Clarivate product page and factsheet; Pivot-RP help center (Searching for Funding Opportunities); Pivot-RP Profiles product documentation (Ex Libris Knowledge Center) — clarivate.com, pivot-rp.zendesk.com, knowledge.exlibrisgroup.com
- GrantForward — product index, about, subscription, and tutorials pages — grantforward.com
- SPIN — SPIN Global Suite product page and access portal — infoedglobal.com, spin.infoedglobal.com; university research-office guides (Toledo, Penn, UNC)
- Research Professional — Funding product documentation (Ex Libris Knowledge Center); university guides (Plymouth, King's College London, Reading, Sussex)
- Grants.gov — Search Grants page; Online Help (Search Grants Tab, Subscribe to Saved Searches, Manage Subscriptions, Subscribe to Opportunities); Grants Learning Center — grants.gov
- Instrumentl — Help Center (What are matches, What is a project, Funder Matches, Discover beta, Discover Plan); product FAQ — help.instrumentl.com, instrumentl.com
- Symplectic — products page (market-structure observation on SPIN's post-acquisition positioning) — symplectic.co.uk

> Sourcing limitation: direct fetches of several vendor sites were blocked (403/404) from the research environment on 2026-09-10. Evidence was taken from official vendor pages, official help centers, and official product documentation as surfaced through web search, supplemented by university research-office guides that document institutional usage. Numeric scale figures appearing in vendor materials (opportunity counts, sponsor counts, profile counts) are vendor-stated and are not treated as verified facts in this document. Precise operational parameters (update cadences, exact field schemas, plan-level feature gating) are recorded in the paired Research Notes only where documented.
