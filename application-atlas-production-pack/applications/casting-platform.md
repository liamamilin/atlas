# Casting Platform

## Overview

A **Casting Platform** is a two-sided market application that connects productions seeking performers with performers seeking roles. The production side — casting directors, filmmakers, advertisers — publishes casting opportunities (role notices and breakdowns) into a shared talent market under publisher-controlled visibility. The performer side maintains persistent talent profiles carrying appearance attributes and performance media. The platform's core transaction is the **submission**: a profile put forward for a specific role, by the performer or their representative. Discovery runs in both directions — talent searches for roles, and casting searches for talent.

The defining work of the platform ends at the matched exchange: published opportunities, discoverable profiles, and submissions moving between them. The selection process that follows — audition rounds, evaluations, callbacks, the recorded casting decision — is the territory of Audition Management, which casting platforms commonly bundle but which does not define them.

## Users & Context

Four user populations interact with a casting platform, with the submission as the point where their work meets:

**Production side:**
- **Casting directors** — run casting for film, TV, commercial, and theatre productions; publish role opportunities, review incoming submissions, and advance candidates toward auditions.
- **Filmmakers and content creators** — independent producers and advertisers who cast their own projects, often through a lighter, sometimes approval-gated, posting flow.

**Supply side:**
- **Performers (talent)** — actors, models, voice artists, and other performers; build and maintain their profiles, discover roles, and submit themselves.
- **Talent representatives (agents and managers)** — maintain rosters of performers and submit on their behalf; in parts of the industry (notably US film/TV) this is the traditional submitting party, with direct self-submission as the performer-empowered alternative.

The work context is a continuous market: many unrelated productions publish into the same platform at any time, and many performers and agencies search and submit across all of them. Activity is deadline-driven (roles open and close quickly) and media-heavy (headshots, reels, self-tapes are the currency of consideration).

## Core Model

### The Defining Core

```text
Production / Casting Office
└── Casting Opportunity (project + role + breakdown/casting notice)
    └── published with visibility controls → talent market
         ↑ discovered via                    ↓ submission
Talent Profile (performer or representative acts)
         └── Submission (profile bound to a specific role)
              └── casting-side review space
```

Four structures. If any one is removed, the product is no longer recognizable as a casting platform:

- **Published casting opportunities** — a project holding one or more roles, each described in a casting notice or breakdown (character description, age range, union status, rate and usage, work dates, location, required skills). Publication is always visibility-controlled: the publisher decides who may see and submit — representatives only or performers too, which regions, which union status, which talent types. Without published opportunities, the product is just a talent directory.
- **Talent profiles** — persistent, per-person records carrying appearance and eligibility attributes (age range, gender appearance, location, union status, sizes, special skills) and performance media (headshots, résumé, demo reels, clips). One profile serves many submissions across many productions and, in mature products, is shared across all of a performer's representatives. Without profiles, the product is a listings board with no candidate identity.
- **Submissions** — the transaction that binds a profile to a published role, initiated by the performer or their representative, and delivered into a casting-side review space. Submissions can typically be customized per role (which media casting sees, an attached note, requested media) and retracted until reviewed. Without submissions, listings and profiles remain disconnected — a classifieds shape, not casting.
- **Two-sided market discovery** — searchable, filterable surfaces on both sides: talent browse role listings with saved searches and receive match alerts derived from their profile; casting reviews submissions and, in most products, can proactively search the talent database by criteria. The platform serves many unrelated productions and performers simultaneously — it is a shared market intermediary, not one organization's private intake funnel.

### Standard Capabilities

Mature products commonly add the following. They make the platform practical but do not define it:

- **Role match alerts and saved searches** — the profile's attributes drive automatic matching; performers save filter sets and receive notifications when fitting roles appear.
- **Submission status tracking** — performers see coarse statuses on their submissions (submitted / selected / under consideration, with labels varying by product) and a submission history; representatives track submissions across their whole roster.
- **Requests inbox** — callback requests, audition requests, media requests, and question requests from casting arrive in a unified alert inbox on the talent or representative side.
- **Self-tape machinery** — casting requests a taped audition with custom sides, instructions, and a due date; the performer records and uploads; the tape lands in the project's review space.
- **Representative tooling** — roster management, submit-on-behalf with criteria-based autofill (union status, playable age range, working location, appearance), per-submission customization, packages (curated roster presentations shareable outside the platform).
- **Audition scheduling and virtual-audition entry points** — the handoff into the selection funnel.
- **Privacy and trust machinery** — visibility controls over profiles and media (submitted media visible only to the casting office it was sent to; protected or watermarked audition sides in some products), and anti-fraud guidance for performers in some products.
- **Mobile apps** — role alerts, submissions, and audition-request responses on the go.

### One Structure, Many Implementations

```text
Concept:            Published casting opportunity
Implementations:    film/TV breakdown, commercial casting notice, open casting call, open-call link

Concept:            Submission initiator
Implementations:    the performer directly (often membership-gated) or their representative; both modes coexist in every mature product

Concept:            Visibility control
Implementations:    agents-only release, performer-visible listings, region targeting, union/talent-type filters, approval-gated posting

Concept:            Monetization
Implementations:    talent subscriptions, per-submission fees, representative subscriptions, free production-side posting
```

## How It Works

### Production side: publish and receive

```text
Create project (title, type, production details)
→ define roles (character, description, age range, specs)
→ publish the breakdown/casting notice with visibility controls
→ submissions arrive in the project's review space
→ review, sort, filter, rate
→ advance candidates (requests, self-tapes, auditions)
```

The publisher decides who sees the opportunity. The same production may be visible to representatives only, or to performers directly, or targeted by region and union status.

### Performer side: profile, discover, submit

```text
Build the profile (attributes + headshots + résumé + reels)
→ set match criteria / save searches
→ receive match alerts or browse the role listings
→ open a role, check eligibility and requirements
→ submit: choose which media casting sees, add requested media and a note
→ track the submission's status; respond to requests
```

Self-submission may be gated by a paid membership in some products; where it is, the representative track is the alternative. A submission can usually be retracted until casting has reviewed it.

### Representative side: roster and submit-on-behalf

```text
Build the roster (invite performers)
→ review new roles against the roster
→ autofill candidates by the role's criteria (union, age range, location, appearance)
→ customize each submission (media selection, notes)
→ submit; manage incoming audition/callback requests per client
```

### After the match: handoff to selection

Once submissions are in, the work moves toward auditions — self-tape requests with sides and deadlines, audition scheduling, live or virtual audition sessions, and eventually the casting decision. Some platforms run this entire funnel inside the product; others stop at the submission exchange and feed a separate studio-side system. Either way, this is the seam with Audition Management: the platform's own defining loop is complete when the match is made and the candidate pool is in casting's hands.

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Role listings / casting billboard (talent side)

The discovery surface.

- lists published roles and projects, filterable by the performer's attributes (age range, gender appearance, location by default) plus project type, role type, union status
- supports saved searches and match notifications
- primary actions: browse, filter, open a role, submit

### Role / breakdown detail

- character description, eligibility requirements (age, location, union), rate and usage where applicable, work dates, requested media, sides if posted
- primary actions: submit, check requirements

### Profile editor and media library

- attributes (measurements, sizes, special skills, union status), headshots, résumé, reels and clips, representation links
- primary actions: update media, control visibility, manage representation

### Submission flow and tracker

- per-submission media selection and notes; submission history; status indicators
- primary actions: submit, customize, unsubmit (until reviewed), track status

### Alerts / requests inbox

- callback, audition, media, and question requests in one place
- primary actions: respond, confirm or reschedule an audition, upload requested media

### Casting-side project workspace

- the project's roles, published breakdown, incoming submissions with sort/filter/rating, self-tape reviews, and (where bundled) scheduling and session tools
- primary actions: publish, review submissions, rate or shortlist, request self-tapes, schedule auditions

### Representative workspace

- roster, role matching across clients, submission assembly, per-client request handling, packages
- primary actions: add clients, submit talent, handle requests, share packages

## Important Rules / Behaviors

### Visibility is the publisher's decision

The single most consequential control on the platform: the same role may be released to representatives only, or opened to performers directly, and scoped by region, union status, and talent type. This control — not openness — is the structural constant; products differ in how much they default to open.

### Eligibility is enforced by criteria, and strictly

Roles carry hard requirements (age range, working location, union status). At least one major product states outright that strict age or location requirements admit no exceptions — performers are told to submit only to roles they fit. Matching filters on both sides (autofill by role criteria on the rep side; profile-derived default filters on the talent side) encode the same rule.

### Submissions are retractable until reviewed

Both talent and representatives can withdraw a submission, but only until the casting side has viewed it. After review, the submission is part of the casting record.

### The profile belongs to the performer

Even where representatives do the submitting, the underlying profile is the performer's: performers control their own profile and who has access to it (one vendor explicitly grounds this in state privacy law), can add or remove representation, and one profile is shared across all of their representatives rather than duplicated per agency.

### Feedback to talent is deliberately coarse

Performers see submission statuses and receive requests, but detailed evaluation of rep-submitted work typically stays with the representative; platforms direct talent to contact their representative about submissions made on their behalf. The platform records the exchange, not the deliberation.

### Trust is an explicit concern

Because casting notices promise work, platforms carry trust machinery: submitted media is kept private to the casting office it was sent to, audition sides and documents are protected (for example with watermarks), some products publish explicit anti-fraud guidance for performers, and some gate project publication behind platform approval.

## Variants

- **Industry segment** — film/TV scripted casting (breakdown-driven, union-heavy, rep-mediated), commercials (rate/usage detail, fast cycles), modeling and print, voice-over, background/extras, theatre, and student/independent film. The same core model spans all of these; the artifacts and eligibility rules vary.
- **Openness posture** — representative-mediated markets (breakdowns released to agents only) at one pole; open self-submission marketplaces at the other; open-call links (a casting office soliciting direct submissions) as a hybrid.
- **Who pays** — talent-side subscriptions are the dominant model (self-submission and media hosting gated by membership), with per-submission fees, representative subscriptions, and free or paid production-side posting varying by product.
- **Regional and union regimes** — union-status attributes, eligibility filters, and union-member discounts are prominent in the US market; other markets run the same structure with different eligibility vocabularies.
- **Bundling depth** — platforms range from submission-exchange-only products that feed a separate studio-side system, to products running the full selection funnel (self-tapes, scheduling, sessions, decision tracking) inside the platform.
- **Tier of the poster** — studio/enterprise casting offices, working casting directors, and independent filmmakers/advertisers use progressively lighter posting flows (the lightest sometimes approval-gated by the platform).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Audition Management | closest sibling; commonly bundled | runs the selection funnel for roles an organization controls — rounds, evaluations, statuses, the recorded decision; the casting platform's defining work is the market exchange (published opportunities, profiles, submissions) that happens before and around that funnel. Remove the market/discovery layer and a management product remains; remove the funnel machinery and a platform remains. |
| Talent Agency Management | adjacent, same intermediary figures | agency-side business software (roster economics, commissions, contracts, bookings) run by the representative; rep accounts inside a casting platform exist only to submit into the market and handle resulting requests |
| Artist Booking Platform | adjacent | engages a performer for a dated live appearance via offer/hold/confirm; casting selects performers for production roles via published opportunities and submissions |
| Job Board / Listings Platform | structural analog | same posted-opportunity + application shape, but the candidate object is a résumé rather than a media-bearing performer profile, and the artifacts (breakdowns, sides, self-tapes), representative mediation, and union eligibility are casting-specific |
| Script Breakdown Application | name collision only | decomposes a screenplay into production elements in pre-production; a casting breakdown is a role notice published to talent — different objects, users, and workflows |
| Film Production Management | downstream | starts after casting, managing the production itself; the casting platform's terminal state is a candidate pool and cast, not a production |
| Recruiting / Applicant Tracking (hiring) | structural kin in another domain | same market shape (opportunities + candidate profiles + applications + funnel), but employment hiring with résumés and interviews rather than performance casting with media-first profiles, representatives, and union eligibility |

## Representative Products

- **Casting Networks** — hybrid platform serving casting directors, talent representatives, project creators, and talent; runs the full workflow from published breakdown to worksheet
- **Breakdown Services (Actors Access / Breakdown Express)** — long-established US industry infrastructure; publisher-controlled breakdown release with a representative-mediated default and a paid self-submission track
- **Cast It Talent** — talent-side feeder into a studio casting database; direct submission into studio inboxes
- **Casting Frontier** — open US marketplace with public casting-call listings and tiered talent subscriptions

The definition was checked against the paper-era breakdown model (breakdown releases to agents, headshot files, submission drops) to avoid over-fitting to the modern self-subscription marketplace.

## Sources

Research date: **2026-09-06**

- Casting Networks — official support center: https://support.castingnetworks.com/ (casting-director workflow guide, Casting Billboard® and submission-tracking articles, talent-representative guides, project-creator section)
- Breakdown Services, Ltd. — official FAQ: https://breakdownservices.com/index.cfm/main/faq ; Actors Access: https://www.actorsaccess.com/
- Cast It Talent — official site: https://www.castittalent.com/ ; official help center: https://support.castitsystems.com/ (talent FAQs)
- Casting Frontier — official site: https://castingfrontier.com/ (product pages; help center not fetched)

> Sourcing limitation: Backstage, Mandy Network, and StarNow (consumer-marketplace casting products) were unreachable (HTTP 403) on 2026-09-06 and are therefore not represented in the sample; no claims are made about them. Casting Frontier evidence is product-page level. Vendor market-share figures encountered during research are recorded as vendor claims and are not relied on here. Precise prices, quotas, and limits observed for individual products are intentionally omitted from this document; they are product-specific details, not characteristics of the Type.

Detailed evidence, product-by-product observations, the cross-product comparison, and the joint boundary review with Audition Management are recorded in the paired Research Notes.
