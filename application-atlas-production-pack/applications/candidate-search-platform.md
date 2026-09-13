# Candidate Search Platform

## Overview

A **Candidate Search Platform** is an employer-side discovery application: it maintains a **searchable corpus of candidate-bearing profiles**, lets a recruiting user express what kind of person a role needs as a **query**, and returns a ranked set of **identified candidate people** who match — each result carrying enough background to judge fit and enough identifiability to be contacted or routed into the hiring workflow.

It solves the problem that job postings alone cannot: most qualified people are not applicants. The application's defining core is therefore small and specific:

```text
Searchable candidate corpus
└── Recruiter-expressed query (filters / keywords / Boolean / described persona)
    └── Ranked results, each identifying a specific candidate person
        └── Actions that move that person into the hiring workflow
            (save → contact → handoff to the pipeline)
```

The corpus may be operated by the product itself (a member network, an aggregated index of public profiles, a licensed database, a bank of resumes) or drawn from the hiring organization's own records (past applicants, current employees); what matters is that it is queryable over candidates. When the center of gravity shifts to maintaining person records rather than querying them, the product is drifting toward a different Application Type (Candidate Profile Platform); when it shifts to running engagement campaigns over identified people, toward another (Talent Sourcing Platform).

## Users & Context

Primary users:

- **Recruiters and talent sourcers** — express role needs as queries, refine results, save and route promising people.
- **Staffing-agency recruiters** — run the same loop on behalf of client employers.

Secondary users:

- **Hiring managers** — consume shared result sets and projects, give feedback that sharpens subsequent searches.
- **Admins** — manage seats and roles, outreach allowances, pipeline-stage defaults, integrations, and compliance settings.

The typical context is proactive recruiting: filling a role where inbound applications are insufficient in volume or quality, building a pipeline ahead of demand, covering hard-to-fill or high-volume niches, or re-examining people already known to the organization (past applicants, internal employees). The application operates upstream of the applicant tracking system: its output is identified people with context, not applications in process.

## Core Model

### The Defining Core

Four properties. Remove any one and the product is no longer recognizable as this Type:

- **Searchable candidate corpus.** A queryable body of candidate-bearing records. Implementations vary widely: a product-operated member network, an aggregated index built from public professional profiles, specialized licensed pools (subject-matter experts, healthcare registrants, code-forge activity, cleared personnel), a job board's bank of candidate-authored resumes, or the employer's own records surfaced for rediscovery. The corpus belongs to the product or the world — the customer queries it; maintaining a curated one-record-per-person layer is *not* required.
- **Query-driven discovery.** The recruiter states a need; the system matches it against the corpus. The query is the defining interaction: everything in the product is organized around expressing, running, saving, and refining queries.
- **Candidate-bearing results.** Each result identifies a specific person — name, current role, background signals — and typically carries a relevance indicator and keyword matches against the query. Results are people, not documents, companies, postings, or sales contacts.
- **Hiring-side operation.** The searching party is the hiring organization (or its agency), and results exist to feed a hiring workflow: evaluate, contact, save, hand off.

### Standard Capabilities

Mature products commonly add the following around that core. They make the loop practical but do not define the Type.

- **Multiple query forms over the same corpus**: structured filters (role, skills, location, employers, years of experience, education); keyword and Boolean strings, often with field-specific syntax; one-click signal filters; and — increasingly standard in current products — natural-language search in which the user describes the ideal candidate or pastes a job description and the system translates it into filters and rankings. Several products keep Boolean and AI modes side by side as an explicit switch, which is good evidence that the AI form is a layer over the query, not a replacement structure.
- **Signal and constraint filters** that only make sense in recruiting: open-to-work or active-candidate indicators, predictions of who is likely to change roles, company-alumni filters (who left a given employer and where they went), diversity filters and bias-reduction display modes, security-clearance levels, industry and region scopes.
- **Results as people cards**: ranked lists with match or fit indicators, keyword highlighting, and a bounded visible result window — search-engine-like behavior applied to people.
- **Actions on results**: open the full profile; save to a project, position, or shortlist; hide or dismiss; find similar candidates; contact through a metered channel; add to an outreach sequence; export.
- **Persistent working artifacts**: searches that can be saved, re-run, and shared; projects or positions where sourced people accumulate, sometimes with lightweight pipeline stages; team-shared filter presets; notes.
- **Rediscovery and internal slices**: past applicants and current employees surfaced as searchable segments of the corpus — usually as dedicated filters, dedicated pools, or dedicated product lines.
- **Contact and outreach attachment**: messaging or contact-retrieval that is commonly metered (allowances tied to the license or plan), plus integrated email sequences and response tracking. The outreach machinery is attached capability, not the discovery core.
- **Insights**: aggregate views over any result set — composition of a talent pool, market context such as salary benchmarks — and performance analytics for searches and outreach.
- **Capture extension**: a browser extension to identify, enrich, and save people found on other sites.
- **Handoff**: export (spreadsheets, documents) and integrations that push identified people into the ATS or CRM, where the application pipeline takes over.

### One Structure, Many Implementations

The core is conceptual; products realize it differently. Reading the concept layer first keeps the Type distinct from any single era or vendor pattern:

```text
Concept:  Searchable candidate corpus
Realizations:  product-operated member network · aggregated public-profile index ·
               specialized licensed pools · job-board resume bank ·
               employer's own records (past applicants, employees)

Concept:  Query expression
Realizations:  structured filters · Boolean strings · one-click signal filters ·
               natural-language persona / job-description paste · agent-run searches

Concept:  Result actions
Realizations:  metered contact · save to project/position · outreach sequence ·
               export / ATS push

Concept:  Delivery
Realizations:  recruiter runs each search · saved searches re-run on a schedule ·
               agent searches continuously · vendor team runs searches and
               delivers reviewed batches
```

A reader who has only seen one realization — say, natural-language search over an aggregated public index — should still be able to recognize a keyword-searched resume bank or a filter-driven member-graph search as the same Type.

## How It Works

### The discovery loop

```text
Express the need
→ run the query over the corpus
→ refine (filters, signal toggles, re-ranking)
→ evaluate results (profile previews, fit indicators)
→ act on people (save / contact / hide / find similar)
→ persist and share (project, saved search, team feedback)
→ hand off (export, ATS push — the person enters the application pipeline)
```

**Express the need.** The recruiter starts from a job description, an ideal-candidate description, a filter set, or a Boolean string. In current products the natural-language path compiles into the same underlying filters the manual path sets by hand.

**Run and refine.** The system matches the query against the corpus and returns ranked results. The recruiter narrows with filters and signal toggles (for example, only people signaling openness to new roles, or only alumni of specific employers). Visible result windows are bounded, like general search engines; precision in the query matters.

**Evaluate.** Results are scanned as people cards; the full profile opens for the serious ones. Fit indicators and keyword highlighting explain why a person matched. Aggregate insights may be projected over the whole result set ("what does this talent pool look like?").

**Act.** Saved people accumulate in a project or position. Contact, where offered, commonly consumes an allowance; the same message surface is reachable from results, project pages, and profiles. People can be moved between searches and shared with hiring managers for feedback.

**Persist and hand off.** Sourced people are exported or synced into the ATS, where the application pipeline begins. At least one product states the underlying rule explicitly: candidates the customer has sourced are theirs to keep, and the safe place to keep them is the ATS — the search platform's corpus is licensed, not owned.

### The managed-delivery variant

A significant variant restructures the loop: the recruiter submits a position's search criteria; the vendor's system (in some products a human team paired with AI) runs the search continuously and delivers results in reviewed batches on a set pace; the recruiter approves or rejects each delivered person, and that calibration feedback is what lets the system adjust subsequent results. The search itself has a status lifecycle — open, paused, closed — and wasted delivery is controlled by pausing when feedback stops. The defining loop is unchanged; only who runs it moved.

## Interfaces

Exact layouts vary by product; the surfaces below recur across the researched sample.

### Query builder / search bar

The entry surface: a global search bar plus a filter pane (and in current products a natural-language chat box).

- Typical content: filter categories, Boolean field syntax, saved and recent searches
- Primary actions: run a search, switch query modes, save a search

### Results list

- Typical information: people cards with current role and employer, match/relevance indicators, keyword highlights, signal badges
- Primary actions: open profile, save to project, contact, hide, find similar, bulk actions

### Profile view

- Typical information: background, experience, education, skills, source provenance, contact-availability indicators
- Primary actions: contact, save, add to sequence, note, export

### Project / position workspace

- Typical information: saved people, lightweight pipeline stages, team members, notes, per-search analytics
- Primary actions: add/remove people, move stages, share, set search status (in managed delivery: open/hold/close)

### Outreach surfaces

- Typical information: message composer with templates, sequence schedules, response inbox, delivery/reply tracking
- Primary actions: send, schedule, follow up, pause

### Insights and admin

- Insights: aggregate composition of a result set or talent pool, search and outreach performance, market context
- Admin: seats and roles, outreach allowances, pipeline-stage defaults, integrations, compliance settings (diversity tools, data-subject requests, AI-usage policies where offered)

## Important Rules / Behaviors

### The corpus is licensed, not owned

The searchable corpus belongs to the product or the world. Access is subscription-gated, and corpus composition can change without the customer's control. Sourced people, once exported or synced into the customer's own systems, are the customer's to keep — products explicitly encourage moving sourced candidates into the ATS for permanence.

### Contact is commonly metered

Messaging a candidate or retrieving contact details typically consumes allowances tied to the license or plan; some products meter contact retrieval while stating plainly that they are not the primary source of that contact information. Metering shapes behavior: recruiters batch and prioritize whom they contact.

### Result windows are bounded

Like general search engines, candidate search products commonly limit how much of a result set is visible, no matter how many people match. Query precision is therefore a skill the product expects.

### Freshness and provenance are imperfect

Where profiles are derived from public or third-party data, results can lag a person's actual situation; products document that discrepancies occur when someone recently changed, privatized, or removed public information. Prudent use treats results as leads, not verified records.

### Compliance surfaces are part of the product

Recruiting-specific constraints appear as product machinery, not fine print: diversity classifiers and bias-reduction display modes, data-subject opt-out paths under privacy law, published usage terms for AI in hiring, and (in vertical corpora) eligibility signals such as clearance level. What a query may express — and how results may be used to contact people — is partly a governed question.

### Calibration governs automated delivery

Where search runs as a managed or agent-driven service, feedback on delivered results is load-bearing: without approving or rejecting delivered people, the system cannot adjust. Searches left uncalibrated are paused or closed to avoid wasted delivery.

### Discovery and pipeline interlock, but remain distinct

Rediscovery — searching past applicants and employees — treats the organization's own records as corpus segments, and search results flow into ATS pipelines. The search application stays upstream: it produces identified people with context; the pipeline system of record owns the process that follows.

## Variants

Common market shapes of the same Type:

- **Network-native search suite** — the corpus is the product's own member graph; search, metered outreach, and project artifacts form a separately licensed tool over the network (e.g. a recruiter subscription sold alongside a professional social network).
- **Standalone people-search engines** — the corpus is aggregated from public professional profiles across the web; query forms range from Boolean to natural language; vertical data (healthcare registries, code-forge activity) extends reach.
- **Managed / automated sourcing services** — vendor team and AI run submitted searches and deliver calibrated batches on a weekly pace; the recruiter's loop is review and feedback.
- **Agentic platforms** — background agents run searches continuously, learn from reviewer feedback, and feed shortlists and outreach automatically.
- **Job-board resume search** — the corpus is a bank of candidate-authored resumes; economics are typically per-contact; the historically dominant form of the Type.
- **Vertical corpora** — specialized pools for healthcare, cleared personnel, subject-matter experts, developers.
- **Agency / staffing mode** — search run on behalf of client employers, with results routed to client submission workflows.
- **Embedded rediscovery modules** — the same machinery shipped as a capability inside an ATS or talent-CRM product rather than as a standalone search subscription.

A variant remains a variant while the defining core applies. Where the product's center of gravity moves to maintaining person records, it becomes a Candidate Profile Platform; where it moves to engagement campaigns over identified people, a Talent Sourcing Platform; where the searched object becomes postings and the searcher becomes the candidate, a Job Board.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Candidate Profile Platform | record layer vs corpus lens: the profile platform's value is a maintained one-record-per-person layer (dedup/merge, cross-process persistence); the search platform's value is answering "who matches?" over a corpus the customer need not curate. Search is a capability inside profile platforms; the standalone search Type exists where the engine is the product. |
| Talent Sourcing Platform | activity vs machinery: sourcing organizes end-to-end identification and engagement workflows (sequences, reply handling); candidate search organizes the query→corpus→results loop. Nearly every search product attaches outreach and every sourcing tool embeds search — the seam is the center of gravity, and joint review is recorded. |
| Applicant Tracking System | pipeline system of record for applications in process vs discovery of people upstream or adjacent to process. Interlocked in both directions (rediscovery indexes ATS candidates into search; search results export into pipelines). |
| Job Board | candidate-side discovery over employer postings, ending in applications; candidate search is employer-side discovery over people. A job board's resume-search product is the employer-side search layer sold separately. |
| Contact Discovery Platform / Sales Intelligence | same query-people-contact machinery over a sales corpus and deal-oriented downstream workflow; recruiting adds candidate-specific corpus slices, compliance surfaces, and hiring handoff. |
| Professional Social Network | the network is the person's self-presentation surface and often the corpus substrate; the search product is a separately licensed tool over that substrate with sourcing controls. The market ships both as distinct products. |
| Recruitment Marketing Platform | attraction layer that generates inbound applicants (campaigns, career site) vs outbound discovery layer that finds people who never applied; talent-community signups are the seam where marketing hands people to the record/discovery layers. |
| Resume Builder | candidate-side document authoring; the resume is one input artifact that may feed a search corpus, not the managed object of this Type. |
| Search Engine (general) | open-web document retrieval vs a recruiting-structured people corpus with recruiting-native filters, action rails, and compliance machinery; hand-built search-engine people queries ("X-Ray" strings) are the Type's primitive ancestor and a benchmark products explicitly compare against. |

## Representative Products

- LinkedIn Recruiter — network-native search suite (member-graph corpus, filter + AI-assisted search, projects, metered InMail)
- hireEZ — outbound AI sourcing suite (open-web search, ATS rediscovery, agentic agent)
- SeekOut — standalone people-search engine (specialized talent pools, AI/Boolean dual mode, diversity and clearance tooling)
- Fetcher — managed/automated sourcing (submitted searches, delivered batches, calibration)
- Juicebox (PeopleGPT) — AI-native natural-language people search with attached CRM and agents

The job-board resume-bank pole (e.g. Indeed's resume search) is documented as market context; its support documentation could not be retrieved during research, so no operational claims rest on it.

## Sources

Research date: **2026-09-07**

- LinkedIn Recruiter Help — Help center root; "AI features in LinkedIn Recruiter"; "Projects in Recruiter and Recruiter Lite"; "Run a standard search for candidates in Recruiter and Recruiter Lite" — https://www.linkedin.com/help/recruiter
- hireEZ — Help center root and Sourcing Suite category — https://help.hireez.com ; Open Web Sourcing product page — https://hireez.com/ai-sourcing/
- SeekOut Help Center — Help center root; Search collection (Search Databases, AI Search, Boolean Search, Search Filters, Search Insights, Power Filters, Chrome Extension, Search FAQ) — https://support.seekout.com/en/
- Fetcher — Product page — https://www.fetcher.ai ; Help center root and Search Management category — https://help.fetcher.ai/
- Juicebox — Product page incl. FAQ — https://www.juicebox.ai

> Sourcing limitations: Indeed's support domain rejected automated access (HTTP 403) and was abandoned after one attempt — the job-board resume-bank pole is treated as market context with no product-specific claims. Juicebox evidence is product-page level (its docs and help center were not fetched), and hireEZ help-center article internals beyond category structure were not directly observed. Numeric scale figures (profile counts, platform counts, integration counts) are vendor claims and are not stated as Type properties in this document. Detailed evidence, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
