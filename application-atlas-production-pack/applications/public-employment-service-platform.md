# Public Employment Service Platform

## Overview

A **Public Employment Service Platform** is the digital system of a government's public employment service: the online venue where employers across the economy submit vacancies to the service, people register with the service as jobseekers, and the two sides find each other — under a public mandate, free of charge to both sides.

The defining core is small:

```text
Public employment service as operator (public mandate, free to both sides)
└── Employer-submitted vacancy pool from the general labor market
    └── Registered jobseeker population
        └── Discovery + response path between the two sides
```

Everything else commonly associated with these platforms — verified employer files, occupational classification vocabularies, resume builders, job alerts, algorithmic matching, application-status tracking, counseling networks, labour-market information, benefit linkage, employment programs — is widespread in mature services but is not what makes the platform what it is. The paper-era employment office (employers notifying vacancies, jobseeker rolls, counselor referral, all free) satisfies the same core with no software at all, and today's platforms document that lineage explicitly.

When the operator is a commercial company monetizing placement, the product is a Job Board. When the vacancies are the government's own (the state hiring its own workforce), the product is government-as-employer recruitment. The Public Employment Service Platform is the government acting as the labor market's intermediary.

## Users & Context

Primary users:

- **jobseekers** — people looking for work, who register with the service, maintain a profile/resume, search or get matched to vacancies, and apply. A substantial share are benefit claimants for whom registering and demonstrating work-search is part of the benefit process.
- **employers** — businesses and organizations across the economy (private and public sector), which register with the service, submit vacancies, review candidates, and receive applications. Hiring stays in the employer's hands.

Secondary users:

- **employment counselors / advisers** — the service's human staff, who guide jobseekers, support employers' recruitment, and connect both sides to programs; the platform typically surfaces this network (locators, directories, contact channels).
- **service administrators** — the government operators who verify employers, review postings, run governance (fraud control, misuse reporting), and publish labour-market information.

The context is a public service with statutory standing: the platform is one surface of an institution that also runs physical offices, benefit processes, and labor-market programs. Services are free to both sides as a matter of mandate, not business model.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as a public employment service platform:

- **Public employment service as operator.** The platform is operated by (or on behalf of) the government's public employment service — an institution holding a labor-market mandate for the jurisdiction — and its core services are free to both sides. This is the property that separates the Type from commercial job boards.
- **Employer-submitted vacancy pool from the general labor market.** Employers across the economy — not only the government itself — register with the service and submit vacancies that form the service's vacancy stock. This is the property that separates the Type from government-as-employer recruitment sites.
- **Registered jobseeker population.** People register with the service as jobseekers; the platform holds them as accounts and profiles that the service serves — and, in mature forms, actively mobilizes through matching, invitations, and work-search records.
- **Discovery + response path.** Registered jobseekers search and browse the vacancy pool and respond to employers — applying on the platform or through channels the posting prescribes (email, phone, in person, mail). The hiring decision and process remain the employer's.

The four are jointly load-bearing:

```text
Operator alone                          → a government website
Vacancy pool alone                      → a vacancy database
Registered jobseekers alone             → a registration system
Discovery + response alone              → a search engine
Operator + pool, no registration        → a vacancy bulletin (the pre-registration-era board)
Operator + registration, no pool        → a jobseeker registry with nothing to offer
Pool + registration, no operator        → a commercial job board with accounts
All records, no connection              → an archive nobody connects through
```

### Standard Capabilities

Mature platforms commonly add the following. They make the service practical; they do not define it.

- **Employer registration and verification** — a business file with the service, checked against government business/identity records; approved employers' postings may carry a verified marking.
- **Structured vacancy records** — title, location, vacancies count, employment type, wages, benefits, skills and qualifications; in some services, titles must be drawn from the jurisdiction's official occupational classification.
- **Seeker profiles and resumes** — profile with work experience, skills, education; resume upload and/or a resume builder; document storage.
- **Search, filters, saved jobs, and job alerts** — the discovery layer over the pool, with email/push notifications of new matching postings.
- **On-platform application** — applying directly through the service (commonly with a stored resume), alongside the prescribed offline channels; application-status visibility to the seeker in some services.
- **Two-sided matching** — in some services the service matches registered jobseeker profiles to postings and lets employers review ranked candidates and invite them to apply; in others, human advisers perform the matching assistance.
- **Employer-side candidate visibility** — search over the registered population or CV database; dashboards showing applications and, in some services, the local labor supply for an occupation.
- **Human service network in-product** — locators and directories for employment centres, advisers, and counselors; contact and chat channels.
- **Labour-market information and career planning** — employment prospects by occupation and region, wage comparisons, trends, career quizzes and planning tools.
- **Government program integration** — job fairs and recruitment events, funded mobility schemes, summer-jobs and apprenticeship programs, work trials, wage-subsidy and work-sharing programs, foreign-worker program information.
- **Governance machinery** — misuse reporting on postings, fraud warnings and blacklists, role-specific terms of use.

### One Structure, Many Implementations

The core model is conceptual. Implementations vary:

```text
Concept:  Public operator with a mandate
Forms:    single national service, federation of national services behind a
          supranational portal, regional/state services

Concept:  Employer-submitted vacancy pool
Forms:    employer self-service posting after verified registration,
          submission through local offices or call centres,
          aggregation from partner/commercial boards into the pool

Concept:  Registered jobseeker
Forms:    simple account sign-in, formal registration flows,
          statutory identity numbers, immigration-program credentials

Concept:  Intermediation
Forms:    self-service search and alerts, algorithmic matching with
          invitations, human advisers and counselors, or a combination
```

A reader who has only seen one national service should still be able to recognize a thin listing service or a supranational federation portal as the same Type.

## How It Works

### Employer path: register, submit, receive

```text
Create a user account with the service
→ register the business/employer file (identity verified against
  government records; review by the service)
→ submit a vacancy (structured fields; classification vocabulary
  where the service imposes one)
→ service reviews and publishes the posting
→ candidates apply through the channels the posting offers
→ employer reviews applications / matched profiles,
  invites candidates, and runs its own hiring process
```

Registration depth varies: some services verify the employer against statutory business registries before postings go live; others require little more than an account. Posting is free everywhere in the sampled services — charging for placement would be drifting toward commercial-board behavior.

### Jobseeker path: register, be found, respond

```text
Register with the service (account; formal registration flow where used)
→ build a profile / resume
→ search and filter the vacancy pool, save jobs, subscribe to alerts
→ optionally: activate matching so the service proposes postings
  and employers can find and invite the profile
→ respond to a vacancy (on-platform application, or the channel
  the posting prescribes)
→ track applications where the service offers status visibility
```

Registration is what makes the seeker a *client of the service* rather than a visitor: the profile feeds matching and employer-side search, and in some services the same records serve benefit processes — for example, job-alert subscriptions created automatically from a benefit claim, or job-search activity kept as proof of search efforts.

### The service layer around the platform

The platform sits on top of a service institution. Around the core loop, the service operates:

- **counseling and offices** — employment centres, advisers, and counselors reachable through or beside the platform, offering guidance, CV support, and recruitment advice;
- **programs** — job fairs, funded mobility schemes, sector academies, work trials, subsidies — attached to postings and profiles through flags, tags, and dedicated sections;
- **labour-market information** — prospects, wages, and trends published from the service's market monitoring, often computed from the platform's own vacancy and registration data;
- **benefit linkage** — connections to unemployment-insurance and benefit processes, ranging from advisory content to automatic subscriptions and work-search records.

### Core vs Common vs Optional

**Defining core** — without these, not a public employment service platform:

- public employment service as operator (public mandate, free to both sides)
- employer-submitted vacancy pool from the general labor market
- registered jobseeker population
- discovery + response path between the two sides

**Common mature structure** — present in most modern services:

- employer verification and structured vacancy records
- seeker profiles/resumes, search, alerts, saved jobs
- on-platform application; status visibility in mature forms
- matching and invitations; employer-side candidate visibility
- human service network surfaced in-product
- labour-market information and career planning
- program integration and governance machinery

**Variant / optional** — depends on jurisdiction, service architecture, and era:

- benefit-linkage depth (advisory → automatic subscriptions and work-search records)
- statutory identity depth (business-registry verification, national identity numbers, immigration credentials)
- controlled occupational vocabularies
- immigration/foreign-worker machinery and eligibility gating
- population-targeted services (youth, newcomers, persons with disabilities, veterans…)
- distribution deals sharing postings with commercial boards
- mobile apps, AI resume/interview aids

## Interfaces

The following surfaces are described conceptually. Names and layouts vary by service.

### Job search

The seeker's primary entry surface.

- lists the vacancy pool with filters (occupation, location, employment type, wages, program flags)
- primary actions: search, filter, save a job, create an alert, open a posting

### Vacancy posting detail

The unit of supply, seen by the seeker.

- structured vacancy content (title, employer, location, terms, duties, qualifications), employer identity, application methods
- primary actions: apply (on-platform or prescribed channel), save, report a problem

### Jobseeker dashboard

The registered seeker's workspace.

- profile and resume management, saved jobs, alerts, matches and invitations, applications and their status, job-search activity records
- primary actions: update profile, respond to invitations, apply, track activity

### Employer dashboard

The registered employer's workspace.

- employer file(s), posting management, applicant inflow, matched candidate profiles, activity reports
- primary actions: create/edit posting, review and invite candidates, manage applications

### Employer registration

The gateway to posting.

- business identity, relationship of the registrant to the business, statutory identifiers where used
- primary actions: register, await review, manage employer files

### Service network surfaces

- employment centre / adviser locators and directories; contact and chat channels; program and event listings (job fairs, schemes)

### Labour-market information section

- occupational prospects, wages by region, trends and reports; career planning tools

## Important Rules / Behaviors

### Free of charge is a mandate, not a promotion

Core services are free to both sides, and the sampled services state this explicitly — one as a governance-grade notice warning jobseekers against anyone charging fees in the service's name. Paid placement is not part of the Type.

### The service verifies; the employer hires

The service stands between the sides: it verifies employers, reviews postings, and operates governance — but the hiring decision and process remain the employer's. The platform mediates interest; it does not employ.

### Registration creates the client relationship

Seeker features (matching, invitations, applications, status, work-search records) are bound to the registered profile. Anonymous browsing may be possible, but the service's obligations and machinery attach to registration.

### Eligibility can gate response

Some services gate application by legal eligibility to work in the jurisdiction — postings may be restricted to candidates with work authorization, and immigration-program credentials may be required fields. This is jurisdictional machinery, not universal.

### Vacancy content may be standardized

Some services require titles and attributes to come from the jurisdiction's official occupational classification, trading employer freedom of expression for comparability across the pool and the labour-market statistics built on it.

### Governance is visible

Misuse reporting on postings, fraud warnings, blacklisted-entity lists, and role-specific terms are part of the operating model — the public operator polices its venue in ways commercial venues rarely document.

## Variants

- **Single national platform** — one service operating the whole jurisdiction's venue end-to-end (posting, matching, counseling surfaces, LMI).
- **Supranational federation portal** — a portal aggregating the vacancy databases of many national public employment services, with cross-border advisers and funded mobility schemes; employers post through their national service.
- **Thin listing service** — a minimal national service limited to posting and applying, with the human service layer operating beside it rather than inside it.
- **Counseling-centric platform** — a service where career counseling, career centres, and skill-provider networks are as prominent as the vacancy pool, often alongside legacy employment-exchange machinery.
- **Government-as-employer recruitment** — a structurally different neighbor (see Related Types) where the operator's own agencies are the only employers.
- **Regional/state services** — sub-national platforms, sometimes delivering the national service's in-person layer.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Job Board | closest neighbor — same posting/search/apply machinery | operator is a commercial (or niche) venue monetizing or curating placement; postings are advertisements on the venue; seeker accounts are conveniences, not service clients. The public employment service platform is operated under a public mandate, free to both sides, holds the vacancy pool as the service's own stock, and serves registered jobseekers as clients (counseling, matching, benefit linkage) |
| Government-as-employer recruitment sites (e.g. multi-agency federal hiring portals) | adjacent — often mistaken for this Type | the vacancies are the operator's own (the state hiring its workforce); the pool is not the general labor market flowing through a public employment service |
| Government Service Portal | adjacent | general authenticated gateway to all government services; the employment platform is one domain-specific service it may link to |
| Public Benefits Management | adjacent, institutionally linked | administers benefit claims and payments; the employment platform links into benefit processes (auto-subscriptions, work-search records) but does not adjudicate or pay benefits |
| Social Services Case Management | adjacent | counselor casework systems; the employment platform's center is the labor-market venue, not case files |
| Career Site Platform | adjacent | one employer's own public careers presence; the employment platform pools many employers' vacancies as a public service |
| Recruiting Management Platform / ATS | adjacent | the employer's own pipeline system of record; the employment platform's employer side ends at posting, candidate visibility, and application inflow |
| Candidate Search Platform | adjacent | standalone employer→people sourcing product; the employment platform's candidate search is a layer over its own registered population |
| Professional Social Network | adjacent | profile/feed network with a jobs surface; identity here is a service registration, not a social graph |

The boundary with the Job Board is the most important one, because the machinery overlaps almost completely. The structural tests: **who operates** (public mandate vs commercial venue), **whose vacancies** (the service's own pool from registered employers vs advertisements placed on a venue), and **who the seeker is** (the service's registered client vs the venue's account holder). The two Types also interlock in the market — public services share their postings with commercial boards, and commercial boards feed postings into public pools — cooperation across the seam, not confusion of the Types.

## Representative Products

- **Job Bank** (Canada) — the national employment service as a full platform: verified employer files, classification-controlled postings, two-sided matching, application status, employment-centre network, labour-market information, benefit-claim linkage
- **EURES** (European Union) — the supranational federation portal over national public employment services' vacancy databases, with advisers, mobility schemes, and cross-border candidate search
- **Find a Job** (UK) — the thin listing-service pole: free posting and applying, with the human recruitment services operating beside it
- **National Career Service** (India) — the counseling-centric pole: registered jobseekers/employers/counsellors/career centres, employment-exchange lineage, free-of-cost governance

The definition was also checked against a government-as-employer recruitment venue (USAJOBS, evidence from the Job Board research pass) to keep the government-as-intermediary and government-as-employer cases separate.

## Sources

Research date: **2026-09-09**

- Job Bank (Canada) — https://www.jobbank.gc.ca/home , https://www.jobbank.gc.ca/aboutus , https://www.jobbank.gc.ca/employers , https://www.jobbank.gc.ca/helpsupport (incl. find-a-job support topic)
- EURES (European Union) — https://eures.europa.eu/index_en , https://eures.europa.eu/jobseekers_en , https://eures.europa.eu/employers/advertise-job_en
- Find a Job (UK) — https://www.gov.uk/find-a-job , https://www.gov.uk/advertise-job , https://www.gov.uk/jobcentre-plus-help-for-recruiters
- National Career Service (India) — https://www.ncs.gov.in/
- USAJOBS (boundary anchor) — evidence carried from the Job Board research pass (fetched 2026-09-07): https://help.usajobs.gov/

> Sourcing limitation: several major public employment platforms (France Travail, Bundesagentur für Arbeit, Arbetsförmedlingen, MyCareersFuture Singapore) could not be fetched from the research environment (timeouts / script-rendered pages). Claims about benefit-registration depth inside platforms are limited to what the accessible services document; deeper casework and referral workflows were not directly observable and are described only at the strength of the available evidence.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis (including the joint review with the Job Board Type) are recorded in the paired Research Notes.
