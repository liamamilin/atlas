# Festival Management

## Overview

A **Festival Management** application is organizer-side software for producing a festival: it holds the festival as a single managed occasion — a dated, public, multi-part event that recurs across editions — maintains records for the people who make up the festival's ecosystem (performers or filmmakers and their parties, staff and volunteers, contractors, press, guests, and the audience), and issues and tracks the access entitlements (passes, accreditations, tickets, wristbands) that govern who may enter which spaces and program parts.

It solves a problem generic event tools do not: a festival is not one happening with a guest list, but a composite production — many program parts across many venues and days, several distinct populations beyond the audience, each with its own intake, entitlements, and logistics, coordinated by a production team and repeated year after year. Spreadsheets and email chains break under that combinatorics; festival software makes the occasion, its people, and their entitlements into managed records.

The defining structure is small:

```text
Festival occasion of record (composite, dated, recurring editions)
└── Participant ecosystem (identified records with roles:
    performers/filmmakers, crew, volunteers, contractors,
    press, guests, audience)
    └── Access entitlements (passes / accreditation / tickets /
        wristbands issued against records, with issuance and
        check-in tracked)
```

Everything else the market associates with festivals — lineup and screening schedules, submissions and juries, catalogues and film guides, guest travel and hotels, catering, audience box offices, streaming — is common capability layered on that spine, and different products own different parts of it. Neither audience ticketing nor program scheduling is required: products exist that manage only the crew-and-site side with no audience sales at all, and products exist that manage only submissions. When the managed population collapses to a simple attendee list for a single happening, the product has become generic event management instead.

## Users & Context

**Primary operators** — the festival's production office:

- **Festival director / producer** — owns the occasion: defines the edition, watches the whole picture (program, participants, entitlements, money), makes the consequential calls.
- **Programmer / curator** — selects what appears: reviews submissions, assigns selection statuses and program sections, builds the schedule of screenings, performances, and events across venues and times.
- **Artist liaison / production coordinator** — works the participant side before the event: collects what each artist, filmmaker, or contractor must supply in advance (technical riders, documents, catering requests) and routes it to the right colleagues.
- **Accreditation manager** — runs the entitlement machinery: defines pass types, approves requests, issues badges and wristbands, and controls who is entitled to what on site.
- **Volunteer / staff coordinator** — recruits, selects, schedules, and accredits the workforce.
- **Guest services / hospitality** — manages invitations, RSVPs, travel, transfers, accommodation, and personal itineraries for filmmakers, guests, press, and delegations.
- **Box office / admissions staff** (where the product sells admission) — sell tickets and passes, scan entries, handle door sales.

**Participants** — the populations the operators work on:

- **Performers / filmmakers and their parties** — submit work or are booked, supply advance information, receive accreditation, travel and itineraries.
- **Crew, contractors, and vendors** — supply documents and insurance, complete inductions, hold site passes.
- **Volunteers and staff** — apply through forms, are scheduled, catered, and badged.
- **Press and industry guests** — request accreditation, receive invitations and hospitality.
- **Audience** — buy tickets or passes where the product faces the public.

Typical context: a recurring festival — music, film, theatre, book, food, or cultural — run by a small permanent team that scales up with seasonal staff and volunteers. Work intensifies in windows: intake and selection months ahead, entitlement issuance and publication in the weeks before, a dense on-site window during the festival, and a closeout that feeds the next edition. The relationship is annual: the same organization, the same populations, the same machinery, edition after edition.

## Core Model

### The Defining Core

**1. The festival occasion of record.** A named, dated, organizer-run public event that spans multiple days and consists of many program parts across multiple venues or stages. It is the container to which every record attaches — participants, entitlements, program items, hospitality, publications. It recurs: the festival is run as a series of editions, and the occasion's records, templates, and relationships carry from one edition to the next. Remove the occasion and the remaining records are a generic contact database; remove the composite, multi-part shape and it is a single-event tool.

**2. The participant ecosystem.** The festival's people, held as identified records with roles and festival-specific attributes — far beyond a simple attendee list. A festival must know, per person: what they submitted or perform, what documents and insurance they have filed, what induction they have completed, what passes they hold, where they stay, when they arrive, what they eat, and what they may access. The populations differ in kind — a filmmaker with a submitted film, a crew contractor with an expiring insurance certificate, a volunteer with a shift, a journalist with an interview request, a passholder with benefits — but all are participant records worked by the same office. Remove the ecosystem and what remains is a schedule or a ticket inventory without people.

**3. Access entitlements.** The festival controls and records who is entitled to be where. Entitlements — passes, accreditations, tickets, wristbands — are issued against participant records, carry access scope (which sites, venues, program parts, days), and are tracked through issuance and check-in: requested, approved, produced, collected, scanned. This is the operational heart of the Type: every sampled product family, whatever else it owns, issues and checks entitlements. Remove it and the product is a planning or database tool without gates.

```text
Festival occasion (edition of a recurring, composite event)
   ↓ anchors
Participant ecosystem (records with roles, intake, documents, logistics)
   ↓ carries
Access entitlements (passes / accreditation / tickets / wristbands)
   ↓ enforced at
Entry & check-in (issuance, scanning, attendance)
```

### Standard Capabilities

Mature festival products commonly add these around the core. They make the Type practical; they do not define it.

- **Program and schedule management** — program parts (screenings, performances, talks, events) placed across venues, days, and times, with the master schedule exported or published to websites, apps, and ticketing systems; some products add warnings for scheduling conflicts. Common in the film-festival pole; a dedicated site-operations product may leave the lineup to other tools.
- **Structured participant intake** — forms that collect what the festival needs from each person or company before the event: artistic submissions with entry fees (film genre), advance production information routed to the right team member (music genre), volunteer applications, document uploads — with automatic chasing of missing or expired items in some products.
- **Selection workflows** — review and rating of submitted work by programmers or juries, selection statuses, and mass notification of results.
- **Publications** — catalogue and program-guide data prepared, proofed, translated, and exported to print, websites, mobile apps, and ticketing platforms.
- **Hospitality and logistics** — participant-facing logistics such as invitations with RSVPs, travel and transfer details, hotel rooming lists, personalized itineraries, or catering requests and meal passes; which forms appear varies by genre and product.
- **Communications** — mass mail with personalized content and attachments (confirmations, itineraries, invoices), newsletters, press releases.
- **Edition continuity** — copying configurations, saved queries, and templates from previous editions; year-round databases and memberships that persist between festivals.
- **Team coordination** — admin roles, task assignment, notes on records, routing of incoming information to responsible colleagues.
- **Reporting and analytics** — submission volumes, selection rates, attendance scans, sales, catering uptake.

### One Structure, Many Implementations

The core model is conceptual; products realize each piece differently:

```text
Concept:      Festival occasion of record
Realizations: edition objects in a year-round database; per-event annual
              licensing; year-round programming around a flagship festival

Concept:      Participant ecosystem
Realizations: person/company/film database modules; contact records with
              documents and inductions; audience accounts with memberships

Concept:      Access entitlements
Realizations: accreditation badges with access levels; wristbands and
              passouts; tickets and rule-based passes with QR codes

Concept:      Structured intake
Realizations: submission forms with entry fees; advancing forms routed to
              artist liaison; volunteer calls; document collection
```

A reader who has only seen one implementation — say, a film-festival platform with submissions and guest hospitality — should still recognize a crew-accreditation product or an audience box-office product as the same Type from the core model.

## How It Works

The working loop runs across the festival year:

### 1. Set up the edition

```text
Create (or copy) the festival edition
→ configure dates, venues, pass/accreditation types, ticket types
→ set intake forms and deadlines
→ open intake
```

Most organizers start an edition from the previous one: the occasion's configuration, saved queries, and templates carry forward. The festival's year-round database — people, companies, works, history — persists between editions.

### 2. Intake participants

```text
Participants submit or are added
→ artistic submissions with fees (film genre) / advance production
  information (music genre) / volunteer applications / document uploads
→ information lands on the right participant record
→ routed automatically to the responsible team member
→ missing items chased (and expiring documents flagged, in some products)
```

The intake step is genre-shaped but structurally the same: the festival declares what it needs from each participant category, collects it through forms, and binds it to records. A filmmaker supplies a film and press kit; a crew contractor supplies insurance certificates; a volunteer supplies availability; an artist supplies technical and catering requirements.

### 3. Select and program

```text
Reviewers rate and comment on submissions
→ programmers assign selection statuses and program sections
→ results communicated by mass mail
→ selected parts scheduled across venues, days, and times
  (with conflict warnings where the product offers them)
→ program data exported to catalogue, website, app, ticketing
```

Where the product owns the program, scheduling is done on a board of venues and time slots — the digital descendant of the printed-stickers-on-a-wall practice — with the system warning about double bookings and format conflicts. Where the product does not own the program, this step happens in a sibling tool and the festival management product continues to work the people side.

### 4. Issue entitlements

```text
Participants request (or are granted) passes / accreditation / tickets
→ organizers approve and modify requests
→ badges and wristbands produced with names, access levels, QR codes
→ issuance tracked (assigned / paid / printed / collected)
→ pre-sorted for distribution (envelopes, tour buses, will-call)
```

Entitlement rules can be elaborate: a pass may bundle venue access, catering, and program benefits automatically, without discount codes. Paid entitlements integrate payment; guest entitlements integrate invitations and RSVPs.

### 5. Run the site

```text
Arrival: scan QR code → check-in screen shows what to issue and verify
→ inductions completed on phones before site admission where required
→ catering collected with meal passes; usage logged
→ guests follow personal itineraries (screenings, meetings, transfers)
→ attendance recorded by scan for statistics
```

On-site work is entitlement-driven: the scan at the gate determines what a person may collect and where they may go. Hospitality machinery — transfers, rooming lists, itineraries — runs in parallel for guests and delegations.

### 6. Publish and communicate

```text
Catalogue / program guide data proofed, translated, locked
→ exported to print, website, mobile app, ticketing platforms
→ newsletters, press releases, and reminders sent by mass mail
→ program changes propagate to already-published surfaces
```

### 7. Close out and carry forward

```text
Attendance, sales, and usage reconciled
→ results reported; participant histories updated
→ the edition's records remain as the record of what happened
→ next edition created by copying this one
```

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Participant database / records

The system's heart: the festival's people and their works.

- Typical information: per person — role and category, contact details, submitted works or booked performances, documents and their expiry states, induction status, entitlements, travel and accommodation, history across editions.
- Primary actions: add or import records, link records to each other (person ↔ company ↔ work), filter and search, edit, export, clone across editions.

### Intake and selection workspace

Where submissions, applications, and advance information arrive and are worked.

- Typical information: incoming entries with their statuses, reviewer ratings and comments, missing documents, fee payments.
- Primary actions: assign to reviewers, set selection statuses, notify submitters, import from external submission platforms, chase missing items.

### Schedule board

The program laid out across venues and times.

- Typical information: program parts by venue, day, and time; sections and categories color-coded; conflict warnings.
- Primary actions: drag to schedule, assign venues and slots, attach people (moderators, guests), export or publish.

### Accreditation console

The entitlement machinery.

- Typical information: pass types and their access scope, requests with approval states, badge designs, issuance tracking.
- Primary actions: approve or modify requests, produce badges and wristbands, define pass rules and benefits, pre-sort for distribution.

### Check-in / scanning surface

The on-site gate.

- Typical information: scan results showing what a person must collect and where they may go; attendance counts.
- Primary actions: scan QR codes, verify identity, issue passes, record attendance.

### Hospitality views

Travel, accommodation, and itineraries for guests and delegations.

- Typical information: arrival and departure details, transfer schedules, rooming lists, personalized itineraries.
- Primary actions: enter travel details, assign drivers and rooms, generate vouchers and schedules, send itineraries.

### Publication export

The bridge to the festival's public faces.

- Typical information: catalogue and program data with proofing and translation states.
- Primary actions: prepare, lock, and export data to print, web, app, and ticketing surfaces.

### Box office (where present)

The audience-facing sales surface.

- Typical information: ticket and pass types, sales, orders, scanning.
- Primary actions: sell, refund, scan, report.

## Important Rules / Behaviors

- **Entitlements gate entry.** A person's access on site is determined by what they hold: no valid pass, no venue entry; no ticket, no screening; and where the festival requires completed inductions or verified identity, an unmet requirement blocks site admission. The check-in scan is the enforcement point, and what it shows (issue, verify, refuse) is driven by the participant's record.
- **Participant records persist across editions.** The festival's database is year-round: a filmmaker who submitted three years ago, a contractor's expiring insurance, a volunteer's history — all remain. New editions are built on top of this continuity, not from scratch.
- **Intake is deadline-shaped and routed.** The festival declares what each participant category must supply and by when; the system routes incoming information to the responsible colleague (for example, advance production requirements flowing to the artist liaison), and some products automatically chase missing items or flag expiring documents.
- **Selection statuses drive communication.** Submitted work moves through review states; the transition to selected or rejected triggers mass notification. Submitters may be given access to update their own information once selected.
- **The occasion is composite.** One person commonly holds many roles and entitlements across many program parts and days — an artist who is also a guest with hotel and transfer arrangements; a volunteer who is also an audience member. The model must carry these combinations without treating the person as several unrelated records.
- **Audience ticketing is optional.** Festival management exists in crew-facing forms that never sell to the public, and in audience-facing forms that delegate production to other tools. What is not optional is the entitlement structure itself — someone must always be defined as entitled to what.
- **Program changes propagate.** Where the product owns the program, changes to the schedule flow to already-published surfaces (website, app, ticketing) rather than requiring re-entry.

## Variants

- **Genre poles.** Film festivals (submissions, juries, screenings, guest hospitality, catalogues), music festivals and tours (advancing, site accreditation, catering, crew compliance), theatre festivals, book fairs and literary festivals, food and cultural festivals. The genre shapes the intake machinery and the program form, not the core.
- **Office poles.** The market realizes the Type as products that each own one "office" of the festival around the shared spine: the central production database (program + people + hospitality + publications), the site operations and accreditation office (crew passes, advancing, compliance), the box office and audience platform (tickets, passes, film guide, streaming), and the submissions office (intake and selection). These interlock — a production database syncing selected films to a box office, a submissions platform syncing to a production database — rather than each trying to do everything.
- **Audience-facing vs crew-facing.** Some products sell admission and face the public; others never touch audience sales and face only the production ecosystem.
- **Virtual and hybrid layers.** Streaming, video-on-demand, and online film guides extending the festival beyond the physical site.
- **Year-round operation.** Memberships, year-round programming, and donor relations that persist between editions.
- **Pricing shapes.** Per-event annual licensing, per-transaction SaaS fees, and free-to-festivals models funded otherwise.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Event Management Platform | the sharpest boundary. Generic event management centers on one occasion's registration flow and its attendee population; festival management centers on a composite, recurring occasion and a multi-category participant ecosystem with entitlements and hospitality. A generic platform can run festival ticketing; it does not carry the production ecosystem (advancing, inductions, accreditation scopes, guest logistics) as its spine |
| Event Ticketing Platform | ticketing is one capability here, often delegated to a sibling product; festival management exists without any audience sales, while a ticketing platform has no participant ecosystem, intake, or hospitality |
| Event Agenda Management | the program record and its published renderings are that Type's center; here the program is one common structure (absent from some products) serving the occasion and its ecosystem |
| Event Credential / Badge Management | credential issuance and check-in are one slice of the entitlement structure here; festival accreditation is embedded in the participant lifecycle (requests tied to advancing, documents, inductions, hospitality), not centered on the credential artifact |
| Artist Booking Platform | transacts the engagement between artist and buyer; festival management coordinates the already-booked artist inside the production (advancing, accreditation, catering, hospitality). Sequential, not the same Type |
| Volunteer Management System | volunteers are one participant category here; a dedicated VMS is workforce-generic across industries with no festival occasion, program, or admission |
| Convention / Exhibition Management | exhibitions organize exhibitors and booths for a marketplace; festivals organize a program and audience plus a production ecosystem. Both large produced events, different core objects |
| Cashless Venue Platform | owns stored-value wallets and on-site transactions; festival management owns the occasion, participants, and entitlements. Festivals commonly bundle both, which is why they are easy to confuse |
| Attraction Management System | venue-side operations where the venue is the standing asset; festival management is organizer-side production where the occasion is the asset and the site is temporary |
| Registration Platform / Form Builder | a form collects responses; festival intake binds submissions to participant records with selection workflows, entitlements, and edition continuity |

## Representative Products

- **Eventival** — full festival production suite born in film festivals: a central database (people, companies, films, events, projects) with submissions, selection, programming, accreditation, guest hospitality, publications, and communications; used by film festivals worldwide and expanding into theatre festivals and book fairs.
- **Eventree** — UK festival and tour operations standard: accreditation, advancing, catering, document management, health-and-safety inductions, and pass/wristband issuance for the festival's working population; no audience ticketing.
- **Eventive** — film-festival box office and audience platform: ticketing, rule-based passes, film guide, scanning, balloting, memberships, and streaming; integrates with production databases.
- **Festhome** — film-festival submissions and selection platform: entry intake, screening room, juror accounts, selection notifications; syncs with production suites.

Together these cover the production-database, site-operations, box-office, and submissions poles across film and music festival genres. The Core Model was checked against the crew-facing pole (a product with no audience sales and no program module) and the submissions slice to avoid defining the Type by the audience-ticketing or program-management pattern.

## Sources

Research date: **2026-09-07**

- Eventival — platform overview, film-festivals page, and features page: https://eventival.com , https://eventival.com/film-festivals/ , https://eventival.com/features/
- Eventree — product homepage with module descriptions and pricing: https://www.eventree.co.uk
- Eventive — product home, film-festivals page, and help-center structure: https://eventive.org , https://eventive.org/film-festivals , https://help.eventive.org
- Festhome — filmmaker and festival-organizer pages: https://festhome.com , https://festivals.festhome.com
- Rosterfy (boundary check only) — https://www.rosterfy.com

> Sourcing limitation: dedicated music/arts festival suites (Festival Pro, FestKit) and a festival ticketing platform (The Ticket Fairy) were not reachable from the research environment this pass (timeouts, transport errors, and access denial respectively). The music-festival pole is therefore represented by a site-operations product rather than a full lineup-and-vendor suite; vendor management and camping machinery are deliberately not described as standard capabilities. Precise vendor numbers, tier limits, and state names are recorded in the paired Research Notes, not asserted here.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against the sibling event Types are recorded in the paired Research Notes.
