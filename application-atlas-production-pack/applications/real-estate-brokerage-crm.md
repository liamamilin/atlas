# Real Estate Brokerage CRM

## Overview

A **Real Estate Brokerage CRM** is a brokerage's shared system of record for its client relationships. It holds the brokerage's clients and prospects as identified records carrying the role each person plays in the business — new lead, buyer, seller, past client — binds every working relationship to the property context it is transacting (a seller's own home being listed, a buyer's requirements and the properties matched to them), and carries each client through the brokerage's own pipeline from first inquiry to closed transaction, under the ownership of an individual agent with brokerage-level routing and oversight.

It solves a problem specific to agency-style real estate: the people a brokerage does business with arrive continuously from many directions (property portals, websites, ads, referrals, past clients), each relationship is anchored to specific properties rather than to an abstract product, deals take weeks or months of paced follow-up, and the relationships — not the agents — are the brokerage's asset. The CRM is where leads become clients, where the record of every call, text, message, showing, and offer accumulates, and where the office can see, direct, and measure the whole motion.

Its boundary: it is the agency-side system for relationships and pipeline. It is not the public venue where property listings are pooled for consumers, not the showing schedule's system of record, and not the transaction file that governs a contract's paperwork — though it feeds the first, touches the second, and commonly embeds a light version of the third.

## Users & Context

**Primary users:**

- **Agents** — the revenue workers. Each agent owns a slice of the brokerage's client population, works new leads assigned to them, advances their buyers and sellers through the pipeline, and keeps stage and follow-up state current. Daily work happens in contact profiles, pipelines, call/text/email surfaces, and calendars.
- **Inside sales agents (ISAs)** — in team-shaped brokerages, specialists whose job is the early pipeline: rapid response to new internet leads, qualification, and appointment setting before handing the client to a field agent.
- **Team leaders / brokers / owners** — supervise the motion: configure lead routing across agents, monitor response behavior, review pipelines and forecasts, and measure per-agent performance.
- **Administrators / operations staff** — manage lead sources, integrations, templates, users, and permissions; in larger brokerages, transaction or listing coordinators who pick up work after a contract is signed.

**Secondary users:** lenders and settlement partners who are attached to the same client records in some setups; marketing staff who build campaigns out of the same database.

The work context is a continuously running acquisition-and-conversion loop: new inquiries arrive daily, each must be answered quickly, most are not ready to transact yet and must be nurtured for months, and the ones who do transact become past clients to be cultivated for repeat and referral business. The software is used constantly throughout the day by agents, mostly on desktop with mobile apps for field work, and at start-of-day and weekly reviews by managers.

## Core Model

### The Defining Core

```text
Brokerage client population of record
│   persons/households · roles: lead / buyer / seller / past client
│   agent-owned, office-shared · accumulating interaction history
│
├── Property context (the relationship's subject matter)
│   seller → the property to be listed (their own)
│   buyer/applicant → requirements + matched, saved, tracked properties
│   both → offers on specific properties
│
└── The brokerage pipeline (the commercial motion)
    new lead → contacted → appointment → shown/matched
    → listing agreement / offers → under contract → closed
    (nurture, rejected, and past-client states alongside)
```

Three structures, all required. If any one is removed, the software stops being this Type:

**The brokerage's client population of record.** Persistent records for the people the brokerage does or seeks business with. These are shared working records — owned by an agent, visible to the office — not personal address books. Each record carries the person's role or roles (a person can be both a past buyer and a future seller), and accumulates the relationship's history: logged calls, texts, emails, notes, meetings, and showings. This is what survives an agent leaving and what makes the database a brokerage asset rather than a private one.

**The property-anchored relationship.** Real estate is transacted over specific properties, and the CRM reflects that: a seller's record is bound to the property they want sold; a buyer's record carries what they are looking for and the properties matched, saved, or toured against it; offers and contracts name specific properties. Property data is a first-class part of the system — supplied by the market's listing databases where those exist, or held natively and published outward where they do not (see Variants). Remove this leg and the record no longer says what the business is transacting: it becomes a generic CRM.

**The brokerage pipeline over client relationships.** Each working client stands in a stage of the brokerage's own vocabulary — from new lead through contact, appointment, showing or listing, offer and contract, to closed — and the stage describes the person's current standing in the relationship, not a document's state. Stages are typically configurable per brokerage, and the pipeline is what managers route, watch, and report on. Remove this leg and the system is a contact file with no commercial motion.

### Standard Capabilities

What mature products in this category commonly add on top of the core. These make the Type practical; they are not what defines it.

- **Multi-channel lead intake** — inquiries arriving from property portals and marketplaces, the brokerage's own IDX-style property-search websites, landing pages, digital advertising, website-visitor identification, referrals, open-house sign-ins, and past-client outreach; commonly including processing of the brokerage's email inboxes so that inquiries sent to a normal email address become contacts automatically.
- **Lead routing and distribution** — per-source rules that assign each new lead to an agent or team (round-robin and duty rotations, first-to-claim, team "ponds", direct-to-ISA routing, attribute rules such as price band or area), with automated immediate response because speed of first contact is a competitive obsession in this trade.
- **Automated follow-up** — action plans / drip campaigns (scheduled email, text, and task sequences) attached by lead source or stage; smart lists and saved segments that surface who to follow up with and when; activity-based prioritization of the most promising opportunities.
- **Native communication** — calling, texting, and email from inside the record, automatically logged to it; templates and, increasingly, AI drafting assistance.
- **Property-data integration** — live listing data from the market's listing database (where one exists), status-change alerts, hot-sheet views of new and changed listings, buyer-to-listing matching, and branded market reports sent to clients.
- **Appointment and showing coordination** — appointments set and confirmed, showings logged against the client's record and commonly against the property.
- **Transaction checklists** — buyer/seller checklist templates, task assignment, deadline tracking, and sometimes client-facing progress portals, covering the contract-to-close stretch (depth varies; see Related Types).
- **Team and brokerage machinery** — agents, ISAs, team leads, and admin roles; shared calendars and records; permissions; per-agent reporting, leaderboards, and dashboards; commission reporting on the agent side.
- **Mobile apps, duplicate management, import/migration, and an integration ecosystem.**

### One Structure, Many Implementations

The core is written conceptually; realizations differ by market and product:

```text
Concept:   buyer/seller roles
Implementations:  role tags on the person record (US-style) ·
                  dedicated applicant and vendor record types (UK-style)

Concept:   property context
Implementations:  listing data consumed from a market listing database (MLS-class,
                  US pattern) · property records authored in the CRM and pushed
                  out to portals (UK/AU pattern) · both at once

Concept:   the pipeline
Implementations:  stage carried on the person record · separate deal/transaction
                  objects · applicant-status progression
```

Stage names, module names, and packaging differ per product; the structures above are the stable part. The core was also checked against market veterans and non-US realizations — a UK agency platform that keeps property records natively with no market-wide listing database, a decades-old all-in-one CRM, and the pre-software brokerage practice of shared client card files and an office deal ledger — so the definition does not depend on the current North-American listing-data pattern or on any modern automation layer.

## How It Works

### Leads enter and are routed

```text
Inquiry arrives (portal / website / ad / email inbox / referral / sign-in)
→ system creates a contact, attributed to its lead source
→ routing rules assign it to an agent (or an ISA team first)
→ an automated action plan fires: immediate text/email, scheduled tasks
→ agent works the response loop: call, text, email
```

The intake-and-routing layer is configured once by the brokerage — which sources are connected, who gets what, what fires automatically — and then runs continuously.

### The buyer motion

```text
New buyer lead → attempt contact → qualify (budget, area, timing)
→ appointment set → record buyer's requirements
→ properties matched / saved-search portal activity tracked
→ showings conducted and logged → offers submitted on specific properties
→ offer accepted → under contract → closing work → closed
```

The buyer's record accumulates the requirements, the properties seen and saved, feedback from showings, and each offer. Market-data integration keeps the matched properties and their statuses current.

### The seller motion

```text
Seller lead (valuation request, farming, referral)
→ attempt contact → appointment / valuation visit
→ listing agreement signed → the property goes active on the market
→ the property is published (directly or via the market's channels)
→ inquiries and showings on the listing are managed
→ offer accepted → under contract → closing work → closed
```

The seller's property moves through its own public-facing life (listed, under offer, sold) while the seller's relationship stage moves in parallel in the CRM. In markets where the CRM authors property records, preparing and publishing the listing to portals is part of this motion.

### The nurture loop

Most leads are not ready to transact. They are moved to a nurture state, enrolled in long-interval campaigns (market updates, seasonal touches), and surfaced periodically by smart lists — until they re-engage, transact, or are marked rejected. Closed clients rotate into a past-client state aimed at repeat and referral business.

### The brokerage loop

Managers watch the same objects from above: response times to new leads, stage distribution across the team, upcoming appointments, at-risk pipelines, per-agent conversion and volume. Routing rules and action plans are tuned; performance is reported. In team-shaped brokerages this oversight layer is a primary reason the CRM is a brokerage system rather than a pile of agent personal tools.

### Contract to close

When a deal goes under contract, work continues: checklists of tasks and deadlines, document collection, client updates, coordination with transaction coordinators, and confirmation of the closing — after which the client record flips to closed/past-client and the commission is recorded against it in products that carry that layer. The depth of this machinery inside the CRM varies widely by product and packaging.

## Interfaces

Described conceptually; exact names and layouts vary by product.

### Pipeline / stage board

The commercial motion at a glance.

- Typical information: contacts grouped by stage, counts and value per stage, aging and stuck items
- Primary actions: move a contact's stage, open a record, filter by source/agent/role, review what needs attention today

### Contact / lead profile

The center of daily work — one screen per relationship.

- Typical information: identity and contact details, role(s), current stage, owner, full interaction timeline (calls, texts, emails, notes), property context (requirements, saved/matched properties, their own listing if a seller), source attribution, tasks
- Primary actions: log or make a call/text/email, change stage, add a note or task, assign or reassign, attach property interest, start or stop an action plan

### Smart lists / segments

Saved searches over the client population that answer "who do I work right now".

- Typical information: leads not yet contacted, due follow-ups, new inquiries, long-silent relationships, past clients due a touch
- Primary actions: bulk actions (text, email, stage change, action-plan assignment), open records

### Communication surfaces

Calling, texting, and email executed from the record with automatic logging; template libraries and scheduled sequences.

### Property context surfaces

Matched and saved properties per buyer, listing details and status per seller, market reports and alerts generated from listing data.

### Calendar / appointments

Scheduled appointments and showings against clients (and commonly properties), with reminders and confirmation flows.

### Transaction / checklist view

Where embedded: per-deal checklist templates with task owners, deadlines, completion state, and sometimes a client-facing progress portal.

### Dashboards and reports

Agent-level (my pipeline, my commissions, my day) and brokerage-level (team leaderboard, source performance, conversion and volume), used for the management loop.

### Administration

Lead-source connections, routing rules, action-plan builders, stage customization, team/user management, permissions, integrations.

## Important Rules / Behaviors

**Records are shared brokerage assets with individual ownership.** A contact has an owner (usually the assigning agent), but the office holds the database: records are visible to management, transferable when agents leave or leads are reassigned, and duplicated-person discipline (the same consumer arriving from several sources) is an ongoing operational concern that products support with matching and merge tooling.

**The stage describes the person, not a document.** In the dominant realization the stage answers "who is this contact to us right now" — one stage at a time, updated as the relationship moves — while role (buyer/seller/renter) is usually carried separately as a tag or record type. A single pipeline typically serves both sides of the business, with seller-specific stages (listing agreement, active listing) sitting alongside buyer-specific ones (showing, offers).

**Speed of first response is engineered, not hoped for.** Routing with automated immediate outreach — driven by lead source, not by an agent remembering — is the standard posture; many products make the automated first touch a first-class configuration object.

**Follow-up runs on automation attached to source and stage.** Action plans fire on arrival and on stage changes; smart lists define the daily work list. The practical rule of the trade — most leads need months of paced contact — is baked into how these products sequence communication.

**Property data authority varies by market.** Where a market-wide listing database (MLS-class) exists, the CRM is a consumer of listing data and statuses; where it does not, the CRM authors the property records and publishes them outward to portals, with the required fields and checks completed before publication. Either way, the CRM binds clients to property context and reflects the property's market state.

**Communication and marketing are rule-bound.** Consumer contact is subject to consent and messaging-compliance requirements that vary by jurisdiction (marketing-consent tracking, texting-registration machinery, and — in some markets — identity and anti-money-laundering checks recorded on client and property records). Products encode these as fields, checks, and workflows rather than leaving them to memory.

**Terminal states persist.** Closed deals remain in the database as past clients — the population from which referrals and repeat business come; rejected and trashed leads are retained (and often re-activatable) rather than destroyed, because today's rejected lead is a future seller.

## Variants

- **Packaging poles.** Pure-CRM products ("open systems") that integrate out to websites, dialers, and transaction tools; all-in-one front-office platforms that bundle property-search websites, lead generation, marketing automation, and the CRM; and whole-agency platforms that add lettings/property-management, client-account, back-office, or agent-recruitment modules. The core is the same; the perimeter differs.
- **Regional realizations.** US-style: the market listing database is the listing authority and the CRM consumes it (buyer-side search, property insights, market reports); routing- and ISA-heavy team motions are common. UK/AU-style: applicant–vendor–property vocabulary, native property records pushed to portals, valuation ("appraisal") to instruction ("listing") as the winning motion, compliance checks built in, lettings often run in the same platform.
- **Carrier of progression.** Stage-on-contact (the person record carries the stage), separate deal/transaction objects, or applicant-status models — three realizations of the same pipeline.
- **Customer tier.** Solo-agent products (routing trivial, everything personal-plus), team products (ISA roles, ponds, first-claim rotations, leaderboards), brokerage/enterprise platforms (multi-branch hierarchies, brand/franchise deployments, agent recruitment and back office alongside).
- **Service-wrapped vs self-serve.** Some vendors attach human services (lead-response concierges, managed advertising) on top of the same database; these are business-model variants, not structures.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Property Listing Platform | adjacent, upstream venue | the pooled public venue where property offers are discovered by consumers; the brokerage CRM is the agency-side system where clients, relationships, and often the listing records themselves originate. Remove the public venue and the CRM stands; remove the client/pipeline record and only inventory remains |
| Property Showing Platform | adjacent machinery | owns the showing schedule's system of record (per-listing rulebook, approval gate, access, feedback); in the CRM a showing is one activity on a client's timeline and one pipeline stage — the buyer there is a showing participant, not a managed relationship |
| Real Estate Transaction Management | adjacent, downstream | the post-contract transaction file (documents, deadlines, compliance); CRMs embed checklist/timeline layers of varying depth, and pipeline stages reference the deal, but the transaction's own system of record is the sibling |
| Customer Relationship Management / CRM | family ancestor | the generic Type holds relationship records, history, progression, and shared working over any commercial "product"; this Type adds the property-anchored invariant and the brokerage organization shape (agent ownership, ISA routing, branch hierarchy) |
| Lead Generation / Lead Management Platform | upstream feed | creates and supplies leads (ads, portals, data); the CRM receives, routes, and converts them; bundled lead engines in all-in-one platforms are packaging, not the CRM's identity |
| Account Management CRM | neighbor in the family | ongoing stewardship of standing customer organizations vs this Type's acquisition-to-close motion over property-anchored person relationships; past-client nurture lives here as a state of the same record |
| Real Estate Development / Investment Management | different operators | developers and investors manage projects, assets, and funds; a brokerage CRM serves fee-earning agents transacting on other people's properties |
| Marketing Automation Platform | embedded capability | drip campaigns and market reports are standard features here, not the defining center |

## Representative Products

- **Follow Up Boss** — team/agent-focused real estate CRM in the "open system" mold; deep lead-routing and follow-up machinery.
- **BoldTrail (Inside Real Estate)** — brokerage all-in-one platform pole: CRM plus property-search websites, lead engine, marketing automation, and transaction/back-office integration.
- **Wise Agent** — independent, agent-tier CRM with embedded transaction checklists and property lists.
- **BoomTown (Inside Real Estate)** — lead-generation-driven team platform pairing predictive CRM with managed lead services.
- **Reapit** — UK estate-agency platform pole: sales and lettings CRM with native applicant/vendor/property records and portal publishing.
- **Top Producer** — long-established all-in-one CRM (agents to teams/brokers), useful as a market-veteran reference point.

The Core Model was checked against older, regional, and pre-software realizations (see the note at the end of Core Model) to keep the definition from over-fitting to one market's current implementation.

## Sources

Research date: **2026-09-09**

- Follow Up Boss Help Center — "Getting Started: Owners & Admins", "Changing a Lead Stage", "Lead Flow Overview" — https://help.followupboss.com/hc/en-us
- Wise Agent — product home and Transaction Management feature page — https://wiseagent.com/ , https://wiseagent.com/features/transaction-management.asp
- BoomTown — product home and Predictive CRM feature page — https://boomtownroi.com/ , https://boomtownroi.com/features/predictive-crm
- Reapit — platform home and Sales CRM page (incl. FAQ) — https://www.reapit.com/ , https://www.reapit.com/platform/sales-crm
- BoldTrail / Inside Real Estate — corporate and product pages — https://boldtrail.com/ , https://insiderealestate.com/solution/
- Top Producer — product home and feature pages — https://topproducer.com/

> Sourcing limitation: operational help-center depth was reached only for Follow Up Boss; the other products were researched at official product-page depth (support portals not accessed). The document therefore states stage names and defaults only as configurable per-brokerage vocabulary, avoids numeric limits and product-specific operational details, and calibrates claims about embedded transaction depth and compliance machinery as varying by product and market.

Detailed evidence, product-by-product observations, and boundary analysis are recorded in the paired Research Notes.
