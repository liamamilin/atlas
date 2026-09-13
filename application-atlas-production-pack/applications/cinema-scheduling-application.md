# Cinema Scheduling Application

## Overview

A **Cinema Scheduling Application** is the film exhibitor's programme-planning application: the surface on which a cinema operator composes its schedule of sessions — which films play in which auditoriums at which times — and publishes that schedule as the operational programme the cinema runs on.

The defining core is small:

```text
Film estate (schedulable content records)
        +
Auditorium/screen estate (placement capacity)
        ↓
Session placements (film × screen × date/time, each carrying its selling configuration)
        ↓
The published schedule — the programme of record
        ↓
Selling channels · signage & listings · projection
```

Two boundary facts matter. First, this function does not sell tickets, run concessions, or settle with distributors — those are the Cinema Management System's jobs; scheduling is that system's **programming spine**, and in the current market it ships as the scheduling module of such systems rather than as standalone products. Second, it does not drive projectors — the projection-control system (TMS) consumes the published schedule. What this application owns is the act of turning films and screens into a buyable, operable programme.

## Users & Context

**Film programmer / booker** — the primary user. In chains, a head-office role that owns the programme across many sites: decides which films play where, negotiates holdovers within distributor agreements, and balances audience demand against each cinema's operational dynamics. In independents, the owner or manager does the same job for one site. Practitioners describe the work as a craft that combines audience understanding, cinema operations, and distributor/studio agreements; a single seven-screen site can juggle dozens of distinct films in one week.

**Site manager** — the second user. Adapts the centrally planned programme to local reality: adds an extra session when a show is selling out, adjusts times, swaps screens. In chain deployments the manager works within limits set by the programmer; in single-site products the two roles collapse into one person.

The working rhythm is a **continuously recomposed programme**: new films enter as they are released, performance data flows back from advance sales, and the schedule for coming days and weeks is revised on a rolling cycle — with pre-planning done months ahead for major releases.

## Core Model

### The session placement

The unit of scheduling is the **session** (showtime): one film placed in one auditorium at one date and time. Sessions are composed ahead of time — commonly by dragging a film from a palette onto a schedule canvas — and each carries its selling configuration: pricing (price cards or per-performance rules), which sales channels may sell it, seating mode (allocated/reserved or unallocated/general admission), allowance for trailers and cleanup time, and whether it is a public, limited-access, or private showing. The session is where scheduling meets money: it is configured so that the selling system can price and sell it the moment it becomes visible.

### The two reference estates

Sessions draw from two managed estates:

- **The film estate** — films held as content records (title, runtime, rating, synopsis, poster media), created once and reused across many sessions, sites, and channels. Runtime shapes the time math of the schedule; rating gates age-checked selling downstream. Film data commonly arrives from a central or studio-official film database rather than being re-entered per site.
- **The auditorium/screen estate** — the operator's own screens with their capacities and layouts, into which sessions are placed. The canvas of the scheduling surface is literally organized as one row per screen against a time axis.

Remove the film estate and the tool becomes generic resource scheduling; remove the auditorium estate and it becomes broadcast-style content scheduling. The two estates together are what make the schedule *cinema* scheduling.

### The schedule as the programme of record

The population of session placements forms the schedule — and the schedule is not a private sketch. Once published it becomes the programme of record: visible to site staff, buyable through every selling channel, displayed on signage and public listings, and consumed by the projection system. The scheduling application is therefore the **origin point of the cinema's entire downstream operation**; everything else in the exhibitor's software estate hangs off what it publishes.

### Standard capabilities around the core

Mature products commonly add:

- **Drag-and-drop schedule canvas** — screen rows against a time axis; drag, paint, and move sessions directly on the grid.
- **Bulk composition** — copy schedules by day or week; carry holdover bookings from head office; repeat patterns across the circuit.
- **Session-level configuration** — price cards, channel availability, seating mode, trailer/cleanup time, private showings, per-performance ticket rules.
- **Film database integration** — preloaded or centrally managed film records feeding the schedule and the public channels.
- **Programmer–manager division of labor** (chain deployments) — central programmers own the programme; site managers adapt within permission limits; changes made locally are visible to (and approvable by) the programmer.
- **Outward distribution** — the schedule pushed to digital signage, websites, listing/ticketing services, and exported to the projection system.
- **Performance feedback** — advance-sales and attendance data informing the next scheduling cycle ("switching out scheduled films", demand forecasting for strategic scheduling decisions).
- **Assisted/AI scheduling** (advanced tier) — forecast-informed generation of an initial schedule that the programmer refines and overrides; what-if analysis for booking decisions.

## How It Works

The scheduling loop runs as a repeating cycle:

```text
Pre-plan (months ahead: which films, which sites)
→ Compose sessions (drag films onto the screen × time canvas)
→ Configure each session (pricing, channels, seating mode, trailer/cleanup time)
→ Publish (the schedule becomes visible and buyable)
→ Distribute (signage, websites, listings, projection export)
→ Sell & measure (advance sales, attendance)
→ Refine (adjust, extend, hold over, switch out — and compose next week)
```

**Composition.** The programmer works on a canvas divided into rows (one per auditorium) and time segments. Films are dragged from a searchable palette onto the canvas; a film placed on the canvas is thereby assigned to a screen and a session time. Bulk tools copy a day's or week's schedule forward; chains import holdover bookings from head office. Some products enforce centrally deployed planning policies — rules specifying how many sessions of a film play per day and at which times.

**Configuration.** Double-clicking a session opens its properties: timing, sales settings, attributes. This is where the session's selling configuration is set — the price card it uses, which channels can sell it, whether seats are allocated, how much trailer and cleanup time it needs, whether it is private.

**Publication.** Composition typically happens in a draft state that is invisible to the operation; converting the schedule to its published state makes the sessions visible to site managers and buyable across channels. Products warn explicitly against publishing incomplete schedules — the publish act is the moment the programme becomes real.

**Distribution.** The published schedule flows outward automatically: to digital signage and marquees, to the cinema's website and apps, to third-party listing and ticketing services, and — by export or integration — to the projection-control system, where the film schedule drives the operation of the auditoriums.

**Refinement.** Sales data flows back: advance-ticket reports break down demand by showtime, auditorium, and date; dashboards show which films are performing. The programmer responds by adding sessions, moving showtimes, extending a film's run (holdover), or switching films out — and the cycle repeats. In the most advanced products, a forecast-informed assistant rapidly generates a starting schedule from historical and ongoing performance data, and the programmer's job shifts from manual placement to refinement and override — with the human retaining final say.

## Interfaces

### Schedule canvas

The primary surface. One row per auditorium against a time axis; sessions appear as placed blocks with status indicators. Primary actions: add a film to the schedule (drag/paint from the palette), move or resize a session, open session properties, open sessions for sale.

### Session properties panel

The per-session configuration surface: timing, sales settings (pricing, channels), attributes (seating mode, trailer/cleanup allowance, private access). Primary actions: edit values, save, (where permitted) publish.

### Film palette / film database

The searchable list of schedulable films with their records (runtime, rating, synopsis, media). Primary actions: search, place onto the canvas, create or edit film records (including custom records for special events).

### Publication & status controls

Draft/published state indicators and the controls that convert composed sessions into the visible, buyable programme. Primary actions: toggle draft mode, convert to planned/published, save.

### Distribution & export outputs

The surfaces where the schedule leaves the application: signage feeds, website/listing updates, and the export or integration that hands the schedule to the projection system.

## Important Rules / Behaviors

**The schedule is invisible until published.** Sessions composed in draft do not exist for the operation — site managers cannot see them and channels cannot sell them. Publication is an explicit, confirmable act; products warn against publishing incomplete schedules. This makes publish the structural gate between planning and operation.

**The programmer's authority can be enforced.** In chain deployments, the programme is the programmer's object: the software can restrict which session properties site managers may change — for example the film, the start time, the film format, the screen — so that local changes require programmer approval. The programmer's own surface is unrestricted; the site surface is bounded. Single-site products collapse this into one role.

**Time math is structural.** A session occupies its auditorium for runtime plus trailers plus cleanup; the canvas enforces that sessions on one screen do not overlap. Trailer/cleanup allowances are configured per session.

**Distributor agreements and planning policies constrain composition.** The schedule is composed under commercial constraints — agreements with distributors and studios govern what plays where and how often, and centrally deployed planning policies can specify the number and times of sessions per film per day. Scheduling is a commercial act, not just a timetable.

**The published schedule drives everything downstream.** Selling channels price and sell against sessions; signage and listings display them; the projection system executes them. A change to the schedule propagates outward automatically — which is why publish semantics and permissions matter.

**The schedule is continuously recomposed.** Programmes are revised on rolling cycles as films enter and leave release; holdovers extend runs; performance data feeds the next iteration. The schedule is never "done" — it is the operator's living programme.

## Variants

- **Chain central programming** — a head-office programmer owns the programme for many sites; site managers adapt within permissions; holdover bookings and planning policies coordinate the circuit. The enterprise shape.
- **Single-site self-scheduling** — the independent cinema's manager composes the schedule directly in the same surface that runs everything else. The small-site shape; same core, collapsed roles.
- **Assisted/AI scheduling** — forecast-informed generation of initial schedules with human refinement; what-if analysis for booking decisions. Present at the enterprise pole; some large exhibitors have built bespoke tools of this kind.
- **Content breadth variants** — festivals and repertory programming, marathons and double features (multiple films ticketed as one session), alternative content and private screenings scheduled in the same surface.
- **Market-shape variants** — reserved-seating-first markets carry seat-level configuration in the session; general-admission-first markets do not. The scheduling act is identical; what a session carries differs.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Cinema Management System | parent system | the whole exhibitor business system (selling, concessions, settlement); scheduling is its programming spine module — this leaf documents that slice |
| Theatre Management System (projection) | downstream consumer | controls digital cinema servers and playlists; it *consumes* the published schedule ("the film schedule drives the operation of the cinema"); no selling or programming of its own |
| Broadcast Management System | adjacent scheduler | schedules content for transmission to an undifferentiated audience; cinema scheduling places ticketed sessions in seated auditoriums |
| Event Ticketing Platform | adjacent seller | sells organizer-defined one-off events; it does not own or compose the operator's rolling programme of sessions |
| Employee Scheduling Platform | naming neighbor | schedules staff shifts, not film sessions; "cinema scheduling" here means the film programme, not rosters |
| Production Scheduling / Call Sheet Application | naming neighbor | schedules the *making* of films (script breakdown, shooting days); this leaf schedules the *exhibition* of finished films |
| Distributor-side release planning | opposite side of the relationship | the distributor decides release dates and which cinemas book a film; the exhibitor's programmer decides sessions within its own estate |
| Meeting/Resource Scheduling | generic neighbor | books resources against availability for internal use; cinema scheduling composes a public commercial programme under distributor agreements |

The most important boundary is with the **Cinema Management System**: research found no standalone end-to-end scheduling products — the function is realized as the scheduling module of cinema management systems (with AI scheduling as add-on depth at the enterprise pole). This page documents the scheduling function itself; the management-system page documents the whole business system around it.

## Representative Products

The scheduling surfaces of the researched cinema management systems:

- **Vista — Film Manager / Showtime Manager** (enterprise chains; central circuit programming, draft→publish workflow, permission machinery, planning policies, Assisted Scheduling and Cinema Intelligence AI)
- **Veezi — Film Programming** (SaaS for independents; drag-and-drop programming, bulk copy, per-session configuration)
- **RTS — Film & Schedule Management** (all-in-one US vendor; drag-and-drop scheduler, film database, export to TMS/LMS)
- **Omniterm — Ticketing Control** (North America; central film-data store with scheduling, pricing, and seating; automation feeds to projection and signage)

No standalone cinema scheduling product family was identified in the researched market; the products above are the market realization of this Type.

## Sources

Research date: **2026-09-10**

- Vista Help Centre — "Showtime Manager": https://help.vista.co/hc/en-nz/articles/4416511988633-Showtime-Manager
- Vista Help Centre — "Creating and publishing draft sessions in film manager": https://help.vista.co/hc/en-nz/articles/59102702457369
- Vista Help Centre — "Restricting session properties in Showtime Manager": https://help.vista.co/hc/en-nz/articles/13960191819929
- Vista Classic product page (Film Manager, Cinema Manager, Cinema Intelligence): https://vista.co/vista-classic
- Vista Cinema Manager product sheet (PDF): https://cdn.prod.website-files.com/60a5ad9159a5687b2c694d70/6449a6151b308932ff0fe594_Cinema%20Manager%20Product%20Sheet%202020.pdf
- Vista insights — Pathé × Vista Assisted Scheduling case study: https://vista.co/insights/joint-innovation-by-pathe-and-vista-halves-film-programming-time
- Veezi — Film Programming: https://www.veezi.com/features/film-programming
- RTS — Operations (Film & Schedule Management): https://www.rts-solutions.com/operations-1
- Omniterm — Theatre Management: https://omniterm.com/theatre-management/
- OneCinema TMS (boundary reference): https://onecinema.de/en/produkte/onecinema-tms
- City A.M. — Vue AI scheduling (2024): https://www.cityam.com/vue-cinemas-ai-software-drives-admissions
- Screen Daily — AI tools in cinema chains (2026): https://www.screendaily.com/features/how-major-and-indie-cinema-chains-are-using-ai-tools-they-are-saving-me-at-least-one-day-a-week/5215694.article

> Sourcing notes: evidence for the scheduling workflow is strongest for Vista (help-centre articles documenting the canvas, draft→publish lifecycle, and permission restrictions) and direct for Veezi and RTS at product-page level; Omniterm evidence is product-page level from the sibling research pass. Publish semantics beyond Vista's explicit draft/planned states are asserted at moderate strength. AI scheduling is documented for one vendor's products plus press reports of exhibitor-built tools; it is presented as an advanced capability, not a standard one. Detailed evidence and the standalone-vs-module disposition analysis are recorded in the paired Research Notes.
