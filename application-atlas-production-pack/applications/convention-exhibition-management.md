# Convention / Exhibition Management

## Overview

A **Convention / Exhibition Management** application is the show organizer's operating system for producing an exhibition, trade show, or convention. It centers on a structure that generic event software does not have: the exhibition floor, laid out as a plan of individually identified and individually sellable booth or space units, and the exhibitor population whose paid participation fills that floor. Around this core the system sells and assigns space under contract, coordinates exhibitors through a self-service portal, delivers the audience through registration and attendee-facing discovery surfaces, and closes the loop by reporting leads and outcomes back to exhibitors so they rebook for the next edition.

The defining core is therefore:

```text
Show (produced, dated, venue-bound occasion, typically recurring in editions)
└── Exhibitor population (companies and organizations paying to participate)
    └── Exhibition floor as sellable space inventory
        (floor plan decomposed into identified booths/spaces with availability states)
        └── Space allocation binding an exhibitor to specific space
            (application or selection → assignment → contract/payment)
```

Remove the sellable floor and its exhibitor commerce, and what remains is a general event management platform. Remove the exhibitor population, and what remains is a venue booking or diagramming tool. The coupling of show, exhibitors, floor inventory, and space allocation is what makes this a distinct Application Type.

Exhibitions and conventions are treated here as one Type because real products serve both under one roof: the floor-shaped trade show and the session-shaped convention share the same exhibitor commerce spine, and session/program machinery appears as a standard layer when the event format includes an education program.

## Users & Context

The system is operated by the **show organizer** — an independent show organizer, a trade association running its annual meeting and exhibit hall, a for-profit exhibition company, or a corporate events team. Typical roles:

- **Exhibition / sales leadership** — owns the floor: how much space exists, how it is priced, how sales are pacing against the edition timeline.
- **Booth and sponsorship sales staff** — work applications, space requests, assignments, contracts, invoices, and payment collection; they are the primary operators of the space-allocation machinery.
- **Show operations staff** — maintain the floor plan itself (layout, booth numbering, statuses, changes), coordinate deadlines, and handle on-site logistics.
- **Marketing / content staff** — run attendee registration campaigns, the program (sessions, speakers, call-for-proposals where applicable), and communications.
- **Registration and on-site staff** — check attendees in, print badges, and manage access on show days.

Three external populations interact with the system directly:

- **Exhibitors** — companies that purchase space and services. Their staff use the exhibitor portal to manage listings, meet deadlines, submit content, and — during the show — capture leads and manage meetings. Exhibitors are paying business customers of the show, which shapes the system: it carries commerce (contracts, payments, invoicing) toward them, not just coordination.
- **Attendees / visitors** — register, browse the exhibitor directory and floor plan, build a personal show plan, and meet exhibitors. For trade shows they are typically the industry audience whose presence is the exhibitor's reason to buy space.
- **General service contractors and venue partners** — not users of the system proper, but recipients of its outputs: the floor plan is a coordination artifact that must be shared with the contractors who physically build the show.

## Core Model

### The show as the produced unit

Everything lives inside a **show** — a named, dated, venue-bound occasion. Shows recur, and the recurring edition is an economic fact of the Type: a show's value is its exhibitor base, and the sales cycle for the next edition typically begins before or during the current one. Some products therefore treat the show portfolio — many editions, many shows — as a first-class management layer.

### The exhibition floor and its inventory

The **floor plan** is not just a drawing; it is an inventory. The hall is decomposed into individually identified **booths or space units**, each with properties (number, size, type, price basis) and an availability state. The organizer builds and edits this layout with dedicated floor-plan tooling — drawing, combining, splitting, and renumbering booths — and the same plan then powers everything downstream: the sales console that tracks what is available, the exhibitor-facing selection experience, the attendee-facing interactive map, and the printed or exported plan used by contractors. Because the plan is an inventory, changes to it are controlled: spaces can be held or locked, and statuses are visible and manageable at scale.

### Exhibitors as the managed commercial population

An **exhibitor** is a company or organization record — profile, categories, products, contacts — bound to the show by what it has purchased. Exhibitors buy more than floor space: sponsorships, advertising placements, directory upgrades, and package add-ons are sold alongside space, and the exhibitor's purchased items determine what appears in the directory, on the floor plan, and in the app. The exhibitor record is the anchor for the whole service relationship: applications, contracts, payments, deadlines, listings, leads, and outcomes all hang off it.

### The space allocation binding

The pivot of the model is the **allocation**: the record that binds a specific exhibitor to specific space for a specific edition. Allocation is reached through different selling models — an application in which the exhibitor states space requirements and preferences and the organizer assigns; direct self-selection of a numbered booth from the live plan; or renewal of an exhibitor's previous position — but in all of them the same structure results: space reserved or assigned, terms recorded, payment collected, and the plan updated. The allocation is what converts the floor from a map into a booked, monetized show.

### The attendee population and the program

**Attendees** register into the show — in some products natively, in others through an integrated registration system — and become the audience layer: badge-holding visitors who browse, plan, and meet. Where the show is a convention, a **program** layer carries sessions, speakers, and (commonly) a call-for-proposals process; the program and the floor are two faces of the same edition, and attendee planning tools mix both (save exhibitors, schedule sessions).

### The exhibitor value loop

A distinctive supporting structure is the machinery that makes the exhibitor's purchase pay off: lead capture (scanning attendee badges at the booth), meeting scheduling between buyers and sellers (including hosted-buyer programs in some segments), and performance reporting (leads, meetings, booth traffic) that feeds the exhibitor's decision to rebook. The organizer runs this machinery as part of the show product — exhibitor retention is a managed outcome, not a side effect.

## How It Works

The canonical operating loop runs once per edition:

```text
Lay out the floor
→ Sell the floor
→ Onboard exhibitors
→ Build the audience and program
→ Drive the match
→ Run the show on-site
→ Settle, report, and rebook
```

**1. Lay out the floor.** Operations staff build the edition's floor plan: the hall layout, booth geometry and numbering, booth types and statuses. Where venue standards exist, tools can check the layout against a reference plan and flag sizing, placement, or numbering errors. The plan is iterated continuously — inventory is added, held, released, and re-numbered — and shared in controlled views.

**2. Sell the floor.** Sales staff open the space inventory to exhibitors. Depending on the show's selling model, exhibitors either submit applications describing their space needs (with competitor-adjacency and partner preferences, which the organizer resolves by assignment) or select specific booths themselves from the live plan and compare pricing. Sponsorships and advertising are sold in the same motion, often in the same transaction flow. Contracts are issued, payments collected, and the plan reflects the result in real time; sales reporting tracks pacing, revenue, and at-risk exhibitors across the cycle.

**3. Onboard exhibitors.** Confirmed exhibitors work in a self-service portal: complete their directory listing, submit content and media, meet deadlines, order upgrades, and prepare booth staff. The organizer segments exhibitors (by category, size, status) and drives preparation with targeted communications.

**4. Build the audience and program.** Registration opens (in this system or an integrated one); the program is assembled — submissions reviewed, sessions scheduled, speakers coordinated; the attendee-facing surfaces go live: searchable exhibitor directory, interactive floor plan, personal show planner, and the event app.

**5. Drive the match.** Before and during the show, the system's job becomes connecting the two populations: attendees find relevant exhibitors (search, categories, recommendations), exhibitors see who is coming, and meetings are requested, approved, and scheduled — in hosted-buyer segments, the platform itself allocates meetings between qualified buyers and exhibitors.

**6. Run the show on-site.** Attendees check in and receive badges; the floor runs; exhibitor staff capture leads by scanning badges and log meetings; the floor plan may be edited live (relocations, on-site sales); session access may be scanned. The show days are the only period when all three populations act inside the system simultaneously.

**7. Settle, report, and rebook.** After (and during) the show, leads are exported to exhibitor CRMs, exhibitor performance reports are delivered, and the financial picture closes (outstanding space balances collected). The retention loop turns outcomes into next-edition sales: on-site rebooking — where a show offers it — lets exhibitors commit to their next position while the current show is still fresh, and analytics flag exhibitors at risk of not returning.

## Interfaces

The system is a multi-console application with distinct surfaces per population:

- **Floor-plan editor (organizer)** — the inventory workbench. Shows the hall as a manipulable plan with booth numbers, types, statuses, and color highlighting; supports drag-and-drop editing, bulk status/type changes, holds and locks, and multi-user concurrent editing. Depending on the product it may also check the layout against a reference plan for sizing/numbering errors and produce output (print-ready plans, exportable drawings) for contractors. Primary actions: create/modify booths, assign and release space, lock or hold, change statuses, export.
- **Space & sponsorship sales console (organizer)** — the commercial view over the same inventory. Lists exhibitors with their space requests and sales status, drives application handling, assignment, contracts, invoicing, and payment tracking, and reports sales pacing. Primary actions: process application, assign booth, issue contract/invoice, record payment, upsell sponsorship or advertising.
- **Exhibitor portal (exhibitor)** — the exhibitor's self-service home: listing/profile management, deadlines and tasks, content submission, purchased-item management, and during the show a lead dashboard (captured leads, qualification notes, exports) and meeting management. Primary actions: edit listing, submit content, complete tasks, review and export leads, request meetings.
- **Public show site: directory + interactive floor plan (attendee)** — search and browse exhibitors by category or product; view the floor plan with booth-level exhibitor locations and points of interest; save exhibitors and sessions to a personal plan. Primary actions: search, filter, save, navigate.
- **Registration & check-in (attendee + on-site staff)** — registration flows with audience types and pricing rules; on-site check-in, badge printing, and access scanning.
- **Program planner (attendee + organizer)** — session catalog, schedule building, and (organizer-side) submission review, session scheduling, and speaker coordination for convention formats.
- **Event app / planner (attendee, exhibitor, organizer)** — the mobile companion carrying the agenda, the directory, the floor map, personal plans, notifications, and meeting schedules.
- **Analytics & reporting (organizer)** — registration and attendance, booth sales and revenue, sponsorship performance, exhibitor engagement and retention risk; increasingly with AI-assisted recommendations for both organizer and exhibitor users.

## Important Rules / Behaviors

- **One space, one exhibitor at a time.** The floor inventory cannot be double-sold: an allocation holds or consumes the space, and the same availability state drives both the organizer's sales console and the public-facing plan. Products add hold and lock mechanics to protect spaces during negotiation and to prevent accidental modification of confirmed layouts.
- **Confirmed space follows recorded commitment.** Assignment and the exhibitor's purchase are connected: applications or selections lead to contracts and payment, and the exhibitor's standing (balance, signed terms) gates what is confirmed and what is merely requested. Exact mechanics vary by product and show policy.
- **The floor plan is audience-scoped.** Different populations see different versions of the same plan: attendees get navigation-oriented maps (exhibitor locations, amenities); exhibitors get detail useful for selecting space (venue entrances, utility locations, columns); contractors get production-ready drawings. Maturity of this separation varies by product; the underlying pattern — one plan, many views — is the structural point.
- **Exhibitor content flows under organizer control.** Exhibitors author their own listings and content, but deadlines, approval, and visibility are organizer-managed: the public directory and floor plan present what the organizer has released.
- **Lead data is generated by exhibitors, governed by the organizer.** Badge scanning happens at the booth, but the data model, consent posture, and export plumbing are provided by the show's system, and lead volume/quality is a headline outcome the organizer reports on.
- **Registration may be native or an integration seam.** The exhibition-specific system can own registration, but in the researched market it equally often integrates a dedicated registration platform; the exhibition machinery does not depend on owning the attendee funnel.
- **The edition is a cycle, not a one-off.** Rebooking, renewal, and retention are structural: sales activity for a future edition can begin on-site during the current one, and exhibitor records persist across editions as the show's core asset.

## Variants

- **B2B trade show (vertical exhibition)** — the classic center of the Type: industry buyers, booth-heavy, lead-driven.
- **Association annual meeting with exhibit hall** — session-heavy convention with a co-located floor; association-management-system and membership integration are common; the program layer carries more weight.
- **Consumer / public expo** — ticketed general-public audiences; admission and on-site experience weigh more than B2B lead machinery.
- **Hosted-buyer market** — curated buyer populations; the platform allocates meetings between qualified buyers and exhibitors as a core activity.
- **Conference-with-expo and corporate events** — registration-led events that add an exhibit component; here the Type's machinery appears inside broader event platforms.
- **Selling-model variants** — sell-by-space (application and organizer assignment) vs exhibitor self-selection vs renewal/priority-based allocation; many shows blend them across the sales cycle.
- **Registration-ownership variants** — full suites owning the attendee funnel vs exhibition specialists integrating external registration.
- **Scale variants** — single flagship editions vs multi-show portfolios with shared exhibitor bases, cloning, and portfolio analytics.
- **Virtual / hybrid layers** — digital exhibitor profiles and booths, virtual sessions, and online meeting programs extending the physical show.
- **On-site depth variants** — from self-service check-in to full-service badge production, access control, and session scanning operated with vendor hardware and staff.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Event Management Platform | adjacent; sharpest seam | manages the event lifecycle (registration → engagement → measurement) for any event; lacks the sellable-booth inventory and space commerce as defining structure — remove the floor machinery from this Type and you get an EMP |
| Exhibitor Management | contained slice | the exhibitor-population layer (records, portal, logistics, communications) sold standalone; this Type contains it plus the floor inventory and space sales |
| Venue Management System | different operator, different object | the venue manages its own bookable spaces and calendar; this Type manages the organizer's show and its booth inventory placed inside a venue |
| Event Registration Platform | contained slice / integration seam | attendee registration and ticketing machinery; may be native here or integrated from outside |
| Event Ticketing Platform | adjacent revenue object | monetizes admission (attendee pays); this Type monetizes participation (exhibitor pays for space and services); both can coexist for one show |
| Festival Management | sibling large-event Type | organizes stages, lineups, and audience ticketing; this Type organizes exhibitors, booths, and the buyer-seller marketplace |
| Attendee Management | contained slice | the audience layer (registration data, badges, attendance) generalized across event types |
| Event Lead Retrieval | contained slice | the exhibitor-side scanning and lead tooling used on the show floor |
| Event Agenda Management | contained slice | the program/session machinery used by convention formats |
| Sponsor Management | overlapping slice | sponsorship sales and fulfillment; in this Type sponsorships are one purchased item alongside floor space |
| Event Diagramming (capability) | confusable tooling | draws venue layouts and seating as a design artifact; this Type manages the floor as sellable, state-bearing inventory with commerce semantics |

The most important boundary is with the Event Management Platform: broad event suites legitimately serve trade shows, but their center of gravity is the event lifecycle shared across all events, and the space-sale spine is not their center of gravity; exhibition-first products own that spine and integrate the rest. Products straddle the seam, which is why both Types stand.

## Representative Products

- **Map Your Show** — exhibition-first specialist; floor-plan builder, booth & sponsorship sales, exhibitor resource center, and attendee planner as the product spine (registration via integration).
- **Swapcard** — attendee-experience and data-first platform carrying a strong exhibitor center (leads, meetings, hosted buyers, ROI) on a full event platform.
- **Cvent** — market-leading broad event suite; dedicated exhibitor management, trade-show lead capture, and meeting scheduling, with venue diagramming on the design side.
- **Stova** — broad suite with an exhibitor resource center and trade-show deployments across association and enterprise organizers.
- **RainFocus** — enterprise conference platform (large conventions, sponsor activation, portfolio orchestration) — included as the boundary anchor toward general event management.

Together the sample spans the exhibition-first specialist, the broad suites, and the enterprise conference pole, and supports the structural split the document describes.

## Sources

Research date: **2026-09-07**

Official vendor surfaces (product and solution pages):

- Map Your Show — https://www.mapyourshow.com/ , https://www.mapyourshow.com/trade-show-exposition-floor-builder , https://www.mapyourshow.com/trade-show-booth-sales
- Swapcard — https://www.swapcard.com/ , https://www.swapcard.com/features/exhibitor-sponsor-tools
- Cvent — https://www.cvent.com/en/event-marketing-management , https://www.cvent.com/en/event-marketing-management/trade-show-solutions , https://www.cvent.com/en/products
- Stova — https://stova.io/
- RainFocus — https://www.rainfocus.com/

> Sourcing limitation: evidence comes from official product/solution pages and FAQs; vendor help centers and user guides were not reachable in this pass, and a legacy exhibition tooling site (expocad.com) was unreachable (404). Accordingly, no precise numeric limits, defaults, or operational timings are asserted in this document, and the historical breadth of the Type is argued structurally rather than from directly observed legacy products. Vendor scale claims found on marketing pages were recorded in research notes only and are not used as evidence here.

Detailed evidence, per-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes (research/convention-exhibition-management.md).
