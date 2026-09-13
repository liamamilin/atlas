# Exhibitor Management

## Overview

An **Exhibitor Management** application is the organizer-side system for managing the companies that exhibit at a show — from the moment they commit to participate, through preparation, the show itself, and the results they take home.

A show's exhibitors are a population unlike its attendees: organizations (not individuals) that have been allocated or sold space, that owe the organizer content, documents, and completed tasks on fixed deadlines, and that bring their own staff to work the booth. Exhibitor Management is the system of record for that relationship. Its defining core:

```text
Exhibitor record (the participating company)
└── Participation obligations (tasks, deadlines, documents, content)
    └── worked jointly to completion — organizer defines and verifies,
        exhibitor completes through a self-service portal
        bound to the exhibitor's own record
```

Everything else commonly bundled with it — booth selection, payments, lead dashboards, appointments, virtual booths, sponsor sales — is standard capability or optional extension, not what makes the product this Type.

The boundary matters: Exhibitor Management does **not** own the exhibition floor itself. Laying out the floor plan, selling space, and managing booth inventory belong to Convention / Exhibition Management. Scanning attendee badges at the booth belongs to Event Lead Retrieval. Producing and issuing badges belongs to Event Credential / Badge Management. Exhibitor Management is the relationship and logistics layer between organizer and exhibitor that those systems assume, feed, and consume.

## Users & Context

Primary operators — the show's side:

- **Show organizer / exhibitor operations team** — defines the exhibitor program, sets tasks and deadlines, collects documents and content, tracks the readiness of the whole population, and communicates with every exhibiting company.
- **Exhibitor sales / show management staff** — consume the population view: who has paid, who is behind on deliverables, who needs chasing.

Secondary operators — the exhibitor's side:

- **Exhibitor company admins** — log into the exhibitor portal to complete tasks, submit required documents, build and edit the company's listing, register booth staff, and manage orders. In mature products the exhibitor's own admins manage their team's calendars and staff information directly.
- **Booth staff** — the exhibitor's employees working the show; they appear in the system as people registered under the exhibitor's record.

Consumers of what the system produces: the public exhibitor directory, the event app and show planner, the floor plan, badge production, and lead/performance reporting.

Typical context: B2B trade shows and expositions, conference exhibit halls, consumer expos, and association annual shows. The exhibitor relationship spans months — intake, preparation, the show, and the aftermath — with the exhibitor portal as the exhibiting company's working surface throughout that cycle.

## Core Model

### The exhibitor record

The fundamental object is a **company-level record** — not a person. One exhibitor record carries:

- **Identity and listing content** — company name, brand, description, logo, media, product information, categories; the material published to audience-facing surfaces.
- **People** — company contacts, the exhibitor's own portal admins, and booth staff, each with their own access and (where supported) appointment calendars.
- **Space reference** — the booth the exhibitor occupies. The reference may be assigned by the organizer, selected by the exhibitor during registration, or recorded from another system; the floor plan itself as sellable inventory is not this Type's object.
- **Entitlements and orders** — packages, advertising, add-ons, badge quotas, balances.
- **Obligations** — the tasks, deadlines, required documents, and content the exhibitor owes the organizer.

```text
Show's exhibitor program
└── Exhibitor record
    ├── Listing content  ──→ published to directory / app / web surfaces
    ├── People (contacts · portal admins · booth staff)
    ├── Space reference (booth)
    ├── Entitlements & orders
    └── Obligations (tasks · deadlines · documents · content)
        └── define → complete → verify
```

### The participation obligation loop

This is the engine of the Type. The organizer defines what every exhibitor must do or provide — checklist items ("submit insurance certificate", "upload logo", "register booth staff by …"), each with a due date. The loop runs across organizational lines:

```text
Organizer defines obligations (task categories, checklists, required documents)
→ assigns them to exhibitors
→ exhibitor completes them in the portal (uploads, forms, staff lists)
→ organizer verifies and tracks completion across the population
→ reminders chase items approaching or past their deadlines
```

The exhibitor is an actor in this loop, not merely a subject of it. That is what separates an exhibitor-management system from an internal tracking spreadsheet: the defining work is jointly owned, and the exhibitor completes its side through its own self-service surface.

### The two-sided surface

Mature products realize the loop with two coupled workspaces:

- the **organizer console**, which manages the population (create tasks, assign, monitor completion, communicate);
- the **exhibitor portal**, bound to each exhibitor's own record, through which the exhibiting company self-serves everything about its own participation.

The portal is the named centerpiece of the category — Exhibitor Portal, Exhibitor Resource Center, Exhibitor Center — and is typically the exhibitor's single place to "manage everything they need for the event they're exhibiting at."

### Concept vs implementation

The core is written conceptually; products realize it differently:

```text
Concept:  Exhibitor record
Realized as:  company profile in the portal, booth record, directory listing —
              usually the same underlying record seen from several surfaces

Concept:  Self-service completion surface
Realized as:  web portal with per-exhibitor login and team members;
              historically, the paper exhibitor manual + return forms

Concept:  Obligation
Realized as:  checklist items, required documents, content submissions,
              staff rosters — with due dates and reminders
```

## How It Works

The exhibitor's participation moves through one lifecycle:

```text
Intake          apply / register (often with tiers, packages, booth selection)
→ Onboard       build the profile & listing; purchase add-ons
→ Prepare       complete tasks → submit documents & content → register booth staff
→ Run the show  occupy the booth; take meetings; receive organizer communications
→ After         see leads & results; retain for the next edition
```

### Intake

The exhibitor enters the population through an application or an exhibitor-registration flow. Common machinery: exhibitor tiers, packages, à-la-carte add-ons, booth selection at registration time, custom question forms per tier, and payment collection (cards, invoice, check, wire depending on product). Intake may be native to the product or handled by the event's registration platform — what this Type requires is that the result is a managed exhibitor record.

### Preparation — the obligation loop in practice

After intake, the portal becomes the exhibitor's to-do list for the show. The organizer builds checklists (often from templates reused across events), assigns items, links resource files, and sets reminders before due dates. The exhibitor completes items: uploading compliance documents, submitting company descriptions and media, confirming listing details, and registering booth staff. The organizer watches a completion dashboard across the whole population — who is ready, who is late, who needs a phone call.

### Listing publication

Exhibitors edit their own profile content; changes propagate to the audience-facing surfaces — the exhibitor directory, the show planner, the event app, and expo webpages — commonly immediately and without organizer re-entry. This keeps one record authoritative from the exhibitor's editing act to what attendees see.

### Booth staff

Exhibitors add and manage their own booth staff in the portal, typically with per-team logins and role-based access (for example, a booth manager versus booth reps). The staff roster feeds downstream machinery — badges, check-in, and appointment calendars that attendees can book against.

### Communications

The organizer runs the exhibitor communication program from the same system: branded pre- and post-event emails, deadline reminders, access codes, and announcement channels for critical information before, during, and after the show.

### Results and retention

After (and during) the show, the exhibitor's own surface shows results — leads captured, stats, meeting outcomes — commonly with export to the exhibitor's CRM. Organizers use the same performance data to prove exhibitor ROI and to drive rebooking for the next edition.

### Capability tiers

**Defining core** — without these, not Exhibitor Management:

- exhibitor company records
- organizer-defined participation obligations with deadlines
- exhibitor-side completion through a self-service surface bound to the exhibitor's record

**Standard capabilities** — present in most mature products:

- intake with tiers, packages, add-ons (and often booth selection)
- self-service listing/profile editing with propagation to audience surfaces
- task/checklist machinery with reminders
- document & content collection with tracking
- organizer↔exhibitor communications
- self-serve booth staff registration
- orders, balances, and payment collection
- lead & ROI visibility in the exhibitor's own surface
- buyer–seller appointments
- integration spine (registration, floor plan, directory/app, SSO for exhibitor teams)

**Optional / variant** — depends on segment and product:

- virtual/online booths and tiered visibility
- gamified booth traffic (passports, leaderboards)
- advertising and sponsorship sales to exhibitors
- hosted-buyer and matchmaking programs
- on-site rebooking machinery (belongs to the floor/sale side of the sibling Type)

## Interfaces

### Organizer console — exhibitor list

Purpose: manage the exhibitor population at a glance.

- typical information: exhibitor name, booth, tier/package, payment/balance state, task completion, outstanding deadlines
- primary actions: add/record an exhibitor, assign tasks, send communications, filter by readiness or compliance, open an exhibitor's detail

### Organizer console — exhibitor detail

Purpose: work one exhibitor relationship end to end.

- typical information: profile and listing content, contacts and booth staff, booth reference, orders/balance, tasks and documents with their states, communication history
- primary actions: assign/chase tasks, approve or review submissions, update booth association, record changes, communicate

### Task/checklist builder

Purpose: define the exhibitor program's obligations once, apply broadly.

- typical information: task categories, due dates, attachments/resource links, reminder schedules
- primary actions: create categories and items, assign, link vendors or resources, schedule reminders

### Exhibitor portal — dashboard

Purpose: the exhibitor's single place to manage its own participation.

- typical information: key dates, outstanding tasks, announcements, balance
- primary actions: complete tasks, jump to listing/staff/orders, read announcements

### Exhibitor portal — listing editor, documents, staff, orders

Purpose: self-service for the record's exhibitor-owned parts.

- listing editor: description, logo, media, categories — with the audience-facing effect visible
- documents: upload required items, see what is still missing
- staff: add/edit booth staff, manage team access and calendars
- orders/payments: packages, add-ons, balance, payment history

### Exhibitor directory (public surface)

Purpose: the audience-facing rendering of the records — searchable company listings (commonly with the interactive floor plan alongside). The directory is fed by this Type but its audience is the attendee's; in the directory the exhibitor record meets the attendee layer.

## Important Rules / Behaviors

- **The record is the company.** Attendee records are persons; the exhibitor record is an organization with people attached. Exhibitor staff usually enter the attendee/badge layer for admission purposes, but the company record and its obligations stay here.
- **Exhibitor edits propagate.** When an exhibitor updates its listing, the change reaches the directory, planner, app, or webpages directly — commonly immediately — rather than through organizer re-entry.
- **Deadlines drive the loop.** Obligations carry due dates; reminders are sent before them; completion state is visible to the organizer across the population. Late or missing items are the normal exception the system is built to surface.
- **Portal access is scoped to the exhibitor's own record.** An exhibiting company sees and edits its own participation — its staff, its documents, its orders — not other exhibitors'. Within the company, access is often tiered (booth manager vs booth rep).
- **An exhibitor belongs to a booth.** The exhibitor↔booth association is maintained here (assignment, selection, or recording from elsewhere), but the floor plan's integrity — booth inventory, availability, sale — is the Convention / Exhibition Management Type's object.
- **Payment behavior varies by packaging.** Balances, payment schedules, and add-on purchases may live natively here, in the registration platform, or in a separate commerce module; what stays constant is that the exhibitor's commercial state is visible on its record.

## Variants

- **Packaging pole.** A dedicated standalone product focused on exhibitor operations; an exhibition-specialist module (where the same vendor sells floor-plan and booth-sales products separately); or a module of an all-in-one event platform. The exhibitor-ops core is the same across poles.
- **Console-first vs hub-first.** Some products lead with the organizer's management machinery (tasks, booth coordination); others lead with the exhibitor-facing hub (the Resource Center as the exhibitor's central place). Both realize the same two-sided loop.
- **Space-machinery depth.** From a bare booth reference on the record, to exhibitor booth selection during registration, to an organized booth-assignment block — while full floor inventory and space commerce stay with the sibling Type.
- **Show-type scope.** B2B trade shows, consumer/public expos, conference exhibit halls, association annual show floors; the obligation sets differ (consumer expos emphasize listings and staff; B2B shows add appointments, hosted buyers, lead programs).
- **Virtual/hybrid surfaces.** Online booths with tiered visibility, livestream showcases, and virtual-lead interactions extend the same record into the digital venue.
- **Sponsor bundling.** Market products frequently bundle "exhibitor & sponsor" management in one module; the populations and their obligation sets are distinct, and the sponsor population is treated as its own Application Type.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Convention / Exhibition Management | containment parent | owns the produced show, the floor as sellable booth inventory, the exhibitor-to-space allocation, and space commerce; this Type is the exhibitor-relationship operations layer inside or beside it |
| Event Management Platform | umbrella | manages any event's lifecycle (registration, agenda, engagement); exhibitors appear there as an optional module, not the center |
| Event Lead Retrieval | different actor, different object | exhibitor *staff* capture *attendee* credentials on the show floor; this Type has the organizer managing the exhibitor *company* and consuming the results as ROI visibility |
| Sponsor Management | parallel sibling slice | a distinct managed population (packages, visibility, advertising) with its own obligation set; products bundle the two, the Types stand apart |
| Attendee Management | parallel population | person records and the attendance lifecycle vs company records and participation obligations |
| Event Credential / Badge Management | downstream consumer | designs/produces/issues badges; booth staff rosters maintained here feed it |
| Event Registration Platform | shared intake seam | registration machinery may process exhibitor sign-ups and payments; this Type owns the resulting exhibitor relationship |
| CRM (sales) | look-alike, different loop | exhibitor records resemble accounts, but the loop is event-participation-shaped (deadlines, documents, staff, listings) and show-cycle-bounded, not a sales pipeline |

The most important boundary is with Convention / Exhibition Management, because the two overlap on the exhibitor population. The structural test: remove the sellable floor (booth inventory, availability states, space sale) from a show system and a meaningful exhibitor-management product remains — exactly what the market sells standalone; remove the exhibitor-relationship machinery (records, obligations, portal) and only floor/sales tooling remains, with nobody onboarded or serviced. Both Types stand; one contains the other's slice.

## Representative Products

- Cvent — Exhibitor Management (dedicated product; enterprise tier)
- Map Your Show — Exhibitor Resource Center (exhibition-first specialist)
- Whova — Exhibitor & Sponsor Management (all-in-one, mid-market/conference tier)
- Swapcard — Exhibitor Center (AI-first platform)
- Stova — Exhibitor Resource Center (broad suite, association/enterprise tier)

The Core Model was checked across these poles — dedicated product, exhibition specialist, all-in-one platform, AI-first platform, and enterprise suite — and against the pre-portal paper-manual form of the same work, so the definition does not depend on any single packaging, era, or show type.

## Sources

Research date: **2026-09-07**

Primary vendor surfaces (official product pages):

- Cvent Exhibitor Management — https://www.cvent.com/en/event-marketing-management/exhibitor-management
- Map Your Show Exhibitor Resource Center — https://www.mapyourshow.com/exhibitor-resource-center
- Swapcard Exhibitor & Sponsor Tools — https://www.swapcard.com/features/exhibitor-sponsor-tools
- Whova Exhibitor & Trade Show Management — https://whova.com/trade-show-app-lead-retrieval/
- Stova — https://stova.io/ (Exhibitor Resource Center description)
- vFairs — exhibitor portal / lead capture setup pages (dedicated portal, booth manager/booth rep roles)

> Sourcing limitation: no Tier-1 help-center / user-guide articles were reachable for any product on this date; evidence is from official product pages and FAQs. Dedicated exhibitor-management product pages for Stova and vFairs were unreachable (404); their observations come from official pages fetched the same date during adjacent research passes. Precise operational details (state names, permission ladders, numeric limits, default deadlines, fee structures) are therefore intentionally not stated; rules are described at the conceptual level the evidence supports.

Detailed product-by-product observations, the cross-product comparison matrix, and boundary analyses are recorded in the paired Research Notes.
