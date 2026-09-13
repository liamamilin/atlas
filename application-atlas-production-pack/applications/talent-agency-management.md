# Talent Agency Management

## Overview

A **Talent Agency Management** application is the business system of record that a talent agency runs on: the software that holds the agency's roster of represented clients, moves professional opportunities through a tracked pipeline to booked work, and settles the money between the agency and the people it represents.

An agency's whole business fits this description: it signs performers and creatives to representation agreements, presents them for work it finds or is offered, negotiates the engagements, and earns its income from the work its clients do. This Application Type is the software realization of that loop. Its defining core is three structures that only exist together:

```text
Roster of represented clients
    matched against
Opportunity pipeline (external opportunities → pursuit → booked work)
    resolved through
Representation money loop (client earnings → agency earnings → settlement)
```

Everything else that modern agency systems carry — application intake, media libraries, contact books, communication tooling, contract templates, reporting, client portals — makes the agency practical to run, but does not define it. An agency operating a client card file, a deals diary with pencilled holds, and a commission ledger satisfies the same core; the software digitizes and automates it.

The Type is not the shared market where roles are published and discovered (that is a Casting Platform), not the selection process a production runs to fill roles (Audition Management), not the live-engagement transaction between artist-side and buyer-side parties (Artist Booking Platform), and not the software that supplies workers to employer job orders (Staffing Agency Management System).

## Users & Context

**Primary operators** are the agency's own staff:

- **Talent agents** — the core operators. They build and maintain client rosters (or segments of a shared roster), field incoming opportunities, match them to suitable available clients, submit or offer, negotiate, and chase the resulting engagements.
- **Agents' assistants and coordinators** — run the daily mechanics: diary and availability upkeep, submission preparation, tape and material handling, confirmations and travel/logistics for booked work.
- **Agency manager / owner** — oversees the roster's health, which clients to take on and let go, agent workloads, and the agency's performance.
- **Commission / finance staff** — operate the money loop: track invoices and payments on booked work, compute what the agency has earned per client, and produce client statements and payouts.

**Participating, non-operator users**:

- **The represented clients themselves** — the subject of every record, but not the operators. In mature systems they hold their own limited accounts: viewing their diary and jobs, keeping materials current, confirming details. The pipeline is moved by agents on their behalf.

**External counterparties** — casting directors, producers, promoters, event buyers, brand and production contacts — appear as contacts and as the sources of opportunities. They are not a managed system population; the agency system is one organization's private record, unlike the two-sided surfaces it consumes.

The context is a relationship-and-deadline business: opportunities arrive continuously from many external channels, close quickly, and are matched against who is free and suitable. Agencies range from solo agents and boutique firms to large multi-agent offices, and segment specialization (acting, voice, live music, and so on) shapes the daily vocabulary without changing the structure.

## Core Model

### The Defining Core

**1. The roster of represented clients.** Persistent, individually identified records for the people the agency represents — the agency's asset of record. A client record carries their professional profile: identifying details, category and appearance attributes relevant to the segment, representation status, and their working media — photographs, show reels, voice demos, scripts, clips, and files. The client record accumulates history: what was submitted, what was booked, what was earned. Without a roster of represented careers, the system is just a contacts database.

**2. The opportunity pipeline matched against the roster.** Professional work reaches the agency from outside — casting breakdowns and role notices, inbound offers and enquiries, event and tour approaches, direct invitations from production contacts. The agency's daily work is matching those opportunities to suitable, *available* clients and pursuing them as tracked pipeline items. A pursuit moves through observable states — expressed in acting vocabulary as submitted → auditioning or taping → recalled → pencilled → offered → job, and in live-music vocabulary as enquiry → hold → offer → contract — until it resolves into booked work or falls away. Availability and diary state are the matching substrate: an opportunity can only be matched to clients who are free on the relevant dates. Without the pipeline, the roster is a list nobody works from.

**3. The representation money loop.** Booked work converts into the client's earnings, and the agency's income derives from that work — commission on client earnings in the dominant model, with rates held per client and configurable. The system tracks the money on each engagement (invoices issued, payments received), computes what the agency has earned, and settles between agency and client — periodic runs that produce client statements and payouts. Without the money loop, the product is a submission tool with no economics attached to representation.

These three are jointly held: a roster with no pipeline is a database; a pipeline with no roster is casting tooling for unanchored people; money with neither is a calculator. The combination is what makes the system an agency's system of record.

### Standard Capabilities

Mature products commonly add, and agency work practically requires:

- **Client profiles with media management** — organized headshots, reels, tapes, and documents per client, kept current and presentable.
- **Industry contact book** — the casting directors, producers, promoters, and buyers the agency works with, linked to the opportunities and clients they involve.
- **Communication tooling** — email and message sending toward clients and industry contacts, often in bulk with details merged from the pipeline.
- **Contracts and deal terms** — engagement contracts and offer documents generated from templates, carrying the negotiated terms of each booking.
- **Diary and holds management** — per-client and per-agent calendar views; non-binding holds placed on dates before confirmation; conflict awareness across the roster.
- **Materials handling** — the segment's working media at pipeline speed: tape processing and distribution for screen work, rider and itinerary documents for live work.
- **Reporting** — agency performance by agent, client, engagement type, and revenue.
- **Client-facing accounts** — limited client access to their own diary, jobs, and materials, in some products.
- **Intake of new clients** — processing applications for representation (common, though a stable-roster agency can run without dedicated intake machinery).

### One Spine, Segment Vocabularies

The core model is segment-neutral; each industry expresses the same spine in its own vocabulary:

```text
Concept:        pursuit states between opportunity and booked work
Acting:         submission → audition/tape → recall → pencil → offer → job
Live music:     enquiry/hold → offer → contract → settlement

Concept:        availability state on the client
Acting:         client availability and availability checks
Live music:     the touring calendar and date holds

Concept:        the agency's earnings on a client's work
Acting:         commission computed in pay runs against invoiced work
Live music:     commission percentages held per artist, payouts tracked to actuals
```

A reader who has only seen one segment's vocabulary should still recognize the other from the spine.

## How It Works

### Build and maintain the roster

```text
Opportunity to represent arises (application, referral, scouting)
→ evaluate the performer
→ if accepted: create the client record
→ complete the profile: attributes, media, representation terms
→ the client becomes matchable in the pipeline
```

Where intake machinery exists, applications flow in through a dedicated surface and every applicant is tracked to a response. Agencies also carry the reverse motion: clients lapse or are dropped, and the roster's composition is itself managed.

### Match opportunities to clients

```text
Opportunity arrives (breakdown, role notice, inbound offer, enquiry)
→ record it with its requirements and dates
→ filter the roster for suitable, available clients
→ discuss/select with the client
→ submit, offer, or respond — creating a tracked pursuit
```

This is the loop agents live in. The matching uses the client's profile attributes and their availability state; the pursuit is bound to the client record and accumulates its history there.

### Pursue to booked work

```text
Submission / offer made
→ pursue: auditions, tapes, meetings, recalls (acting) — or negotiation and holds (live music)
→ outcome: offered → agreed
→ contract / engagement terms recorded
→ the job is booked: diary updated, materials and logistics prepared
```

The pursuit's states are the agency's operational currency — knowing at any moment what is submitted, what is on hold, what is confirmed, and what fell through. Confirmed work enters the diary; conflicting holds are surfaced and resolved before commitment.

### Run the booked work

```text
Job approaches → confirm details, distribute materials/scripts/itineraries
→ the client works the engagement
→ changes and cancellations handled against the record
```

The agency is the coordination hub: the client's diary, the counterparties' information, and the documents each engagement needs are kept current from the system.

### Settle the money

```text
Booked work completes → invoice tracked (or payment received from the engagement)
→ agency earnings computed against the client's work (commission basis, per client)
→ money received and reconciled
→ periodic run: client statements and payouts produced
```

This closes the loop that defines the business: the agency's revenue is a function of its clients' booked work, and the system is where that relationship is computed, tracked, and settled.

### Core vs standard vs optional

**Defining core** — without these, not a talent agency management system:

- roster of represented clients as persistent career records
- opportunity pipeline matched against the roster, with availability as the matching substrate
- pursuit states carrying opportunities to booked work
- the representation money loop: agency earnings derived from client work and settled between agency and client

**Standard capabilities** — present in most mature products:

- media/profile management, contact book, communication tooling, contract templates, diary and holds, reporting, client accounts, intake processing

**Segment and scale variants** — depend on industry, region, and agency size:

- segment machinery (tape processing, extras booking, tour routing, ticket counts, settlements)
- casting-platform integration; venue/database discovery
- regulatory-shaped commission and contract configuration; business-management depth

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Roster / client list

The agency's primary entry surface.

- lists the represented clients with segment-relevant attributes and status
- filterable and searchable (by category, availability, agent, attributes)
- primary actions: open a client, find matchable clients for an opportunity, manage representation status

### Client detail

The career record of one represented client.

- profile and attributes, media library, representation terms
- their pipeline: current submissions and pursuits, past jobs
- their diary and availability; their money: earnings, agency earnings, statements
- primary actions: update profile and media, record availability, create submissions, log jobs and payments

### Pipeline / deal tracking

The pursuit workspace.

- incoming opportunities with requirements and dates
- current pursuits by state — what is submitted, on hold, offered, confirmed
- primary actions: record an opportunity, match and submit clients, move pursuit states, generate offers and contracts

### Diary / calendar

The roster's time dimension.

- per-client and per-agent views; bookings, holds, auditions, meetings
- conflict and availability checks before commitments
- primary actions: place or release a hold, confirm a booking, check availability

### Money surfaces

- invoices and payments tracked per engagement
- commission computation against client work
- runs producing client statements and payouts; agency receivables
- primary actions: record invoices/payments, run commissions, produce statements

### Communication

- outbound mail and messages toward clients and industry contacts, individually or in bulk, with pipeline details merged in
- typically the mechanism for submissions, offers, and chasing responses

### Reporting

- performance of the agency across agents, clients, engagement types, and time — bookings, revenue, and roster health

### Client portal

- the talent's limited view: their diary, their jobs, their materials, confirmations requested of them

## Important Rules / Behaviors

### Availability gates matching

An opportunity can only be matched to clients who are available for it. Availability is therefore a first-class state on the client record, maintained continuously, and checked before any submission or offer. Holds on dates are how interest is reserved before commitment.

### Holds are not commitments

The pipeline distinguishes non-binding interest (pencils, holds) from confirmed work (offers accepted, contracts issued). Multiple parties can hold the same date or role; the confirmation step is the binding event that resolves the conflict. Exact labels differ by segment and product; the progression from non-binding to binding is the shared behavior.

### The client is represented, not operated

The system's operators are agents; clients act on their own records only through limited surfaces (confirming availability, updating materials). The pipeline moves at the agent's hand. This is the structural expression of representation, and it separates the Type from self-serve marketplaces.

### Money derives from client work

The agency's earnings are computed against the client's booked engagements — commission-based in the dominant model, with rates held per client and configurable. Payments arriving on engagements are reconciled before client payouts are produced. The agency's receivables and the clients' statements are two views of the same engagements.

### External counterparties are contacts, not accounts

Producers, casting directors, promoters, and buyers appear in the system as contacts attached to opportunities and engagements. The agency system holds no buyer-side population and no shared marketplace surface — the flows that would require those live in the platforms the agency consumes.

## Variants

- **Acting and creative representation** — the reference shape: submissions into casting breakdowns, audition/tape/recall tracking, pencils and offers, per-job invoicing and commission runs; commonly integrates with casting platforms where a market's casting infrastructure is centralized.
- **Voiceover representation** — the same spine organized around demos and tape specs, with segment-specific material handling.
- **Supporting-artist / extras representation** — high-volume, date-driven booking of background talent; the roster and diary dominate.
- **Live music booking agencies** — the booking-heavy pole: roster of artists with commission percentages, date holds and offers, contracts, deposits, settlements, itineraries, tour routing; often connected to venue-side systems.
- **Model agencies** — expected to fit the same spine (roster, day- and usage-based bookings, options, commission), though segment-specific software for this pole was not directly verified in this research.
- **Creator / influencer talent management** — an emerging segment expected to instantiate the same core (roster, brand-deal pipeline, commission); not directly verified here.
- **Business-management flavor** — some representation firms extend into broader financial administration of clients' affairs beyond agency-sourced work; depth varies and the core spine is unchanged.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Artist Booking Platform | closest sibling — partial overlap on the booking-heavy pole | centers the booking transaction (artist × dated occasion × terms) between artist-side and buyer-side parties; buyers are a first-class system population; a booking platform needs no career-management objects. The agency system centers the represented client across many revenue types, with intake, availability, commission, and statements |
| Casting Platform | adjacent — the agency consumes it | a shared two-sided market where productions publish roles and many agencies/performers submit; the agency system is one organization's private roster-and-money spine that submits *into* such platforms |
| Audition Management | adjacent — production-side | runs the selection process (roles → candidacies → auditions → casting decision); the agency tracks its clients' auditions as pipeline states but never runs the selection |
| Staffing Agency Management System | naming parallel, different business | supplies interchangeable workforce capacity against employer-owned job orders, earning placement fees or pay/bill spread; the talent agency books *specific individuals* and earns on the client's own work |
| Record Label Management | sibling spine, different asset | the label's asset of record is the controlled recording catalog with deal terms and royalty settlement; the agency's asset of record is the person and their flow of engagements |
| Customer Relationship Management | generic baseline | a configured CRM can approximate roster plus pipeline, but lacks the representation money loop (commission against client earnings, statements/payouts), the availability-and-holds machinery, and the industry integrations |

The boundary with Artist Booking Platform is the important one, because booking agencies and booking platforms converge on roster + offers + contracts + money. The structural test: whose record is the system built around — the booking transaction with buyer-side parties as a system population, or the represented client with buyers as external contacts? Both Types are legitimately distinct; some music-industry products sit deliberately near the seam.

## Representative Products

- Tagmin — acting, voice, and supporting-artist agencies (UK; used internationally)
- Prism — booking and talent agencies in live music (US)
- Gigwell — artist booking agencies (US/EU)

Research context: Tagmin is part of the Talent Systems family (with the Spotlight casting platform), which also sells the representative workflow — roster management and submission into casting projects — as one leg of a casting ecosystem; this coupling informed the Casting Platform boundary above.

## Sources

Research date: **2026-09-09**

- Tagmin — https://www.tagmin.com/ (features, modules, about)
- Talent Systems — https://talentsystems.com/ (audience overview incl. talent representatives)
- Prism — https://prism.fm/ and https://prism.fm/why-prism-for-agencies/ (agency product pages)
- Gigwell — https://gigwell.com/ (product overview)

> Sourcing limitation: vendor help-center and FAQ articles were not reachable from the research environment on 2026-09-09 (timeouts and transport errors), and several additional agency-software vendors in the model-agency and entertainment-agency segments were unreachable. Product observations therefore rest on official product pages rather than operational documentation. Accordingly, this document avoids precise operational facts (commission defaults, payrun frequencies, exact state names, numeric limits); pipeline state vocabularies are described as segment conventions, not as product-verified rules.

Detailed evidence, product-by-product observations, the cross-product comparison, and the joint-review resolution with Artist Booking Platform are recorded in the paired Research Notes.
