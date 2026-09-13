# Worship Planning

## Overview

A **Worship Planning** application is the congregation's service-production planning system. Its purpose is to organize *what happens in a worship service* — the order of worship — as a structured plan, and to put that plan in the hands of the people who make the service happen: the worship team, AV and media volunteers, readers, and the preacher.

The defining core is small:

```text
Service Plan of Record
└── ordered, item-based plan for a dated worship-service occasion
    (songs, sermon slot, readings, announcements, media, liturgy)
        +
Team-facing Preparation Loop
└── the plan distributed to its contributors,
    each seeing their parts, notes, files, and timings
```

Everything else the category is known for — song libraries with chord charts and key transposition, volunteer scheduling, rehearsal audio, live-run displays, song-usage reporting to church-music licensing bodies, printed bulletins — is standard or optional structure layered on that core. The reason churches adopt these products is that "the plan" in a typical congregation is not one document for one person: it is the coordination point for a rotating team of volunteers who each need to know their part before Sunday.

When the center of gravity shifts to *who serves* rather than *what happens in the service*, the product is drifting toward Ministry Scheduling; when it shifts to the *message as a record* that outlives the service, toward Sermon Management; when it shifts to *displaying content live during* the service, toward Worship Presentation Software.

## Users & Context

**Primary users — the planners.** Usually a worship or music pastor, service coordinator, or administrative volunteer who owns the weekly rhythm: building the order of worship, adding the songs and their keys, attaching the files, noting what the AV team needs, and scheduling the people. In larger churches this is a staff role; in smaller churches it is one volunteer wearing several hats. Planner seats are commonly limited and priced differently from participant access.

**Primary users — the team members.** Musicians, vocalists, AV/media operators, readers, greeters, and others rostered for a given service. They are typically unpaid volunteers drawn from the congregation. They receive the plan, see the items they are responsible for, open the attached lyrics, chord charts, or media, listen to practice recordings, respond to scheduling requests, and — in products that carry a live-run surface — follow the plan in real time during the service.

**Secondary users.** The preacher or liturgy lead, whose sermon slot and notes live in the plan; technical volunteers who consume media cues and slide sources; and, in some products, a public or congregational audience viewing a read-only version of the order of service.

The usage cadence is strongly weekly and cyclical: services recur at known times, the same songs and structures return, and the plan for next Sunday is assembled, filled, rehearsed, run, and archived — then the cycle begins again. Multi-site churches repeat this per campus and per service time.

## Core Model

### The Defining Core

**The service plan of record.** The central object is the *plan* — a persistent, ordered sequence of items for one dated worship-service occasion. This is the order of worship made operational: not a printed program handed to the congregation, but a working plan the production team builds and executes from. Plans are organized under the church's service structure (a named service type or recurring occasion — traditional, contemporary, youth, a Sunday mass), and a typical plan line-by-line reads like the service itself: opening song, welcome, two songs, scripture reading, sermon slot, announcements, closing song.

Each **item** is a discrete element of the service:

- a **song** — normally the most numerous item type, carrying its key, arrangement, lyrics, and chord charts;
- **spoken or liturgical elements** — sermon slot, readings, prayers, communion, baptism moments;
- **announcements and transitions**;
- **media items** — videos, backing tracks, image cues.

Items can be added, rearranged by dragging, color-coded, and annotated. **Plan notes** carry the information contributors need — sermon notes, stage directions, special reminders. **Attachments** put the actual preparation content on the item or on the song: audio files, lyric sheets, chord charts, documents, media files. Many products also let planners see and work on several upcoming services side-by-side, which is how multi-service and multi-campus churches keep a month of Sundays straight.

**The team-facing preparation loop.** A plan that only the planner can see is just a document. The second defining structure is that the plan is *distributed*: every scheduled contributor sees the plan — commonly filtered or highlighted to what is theirs — together with the notes, files, and timings attached to their part. Musicians download charts and listen to practice audio; AV volunteers see media cues; readers see their reading. Products express this through team views of the plan, mobile apps, printable run sheets, and per-role file access. This is what turns an order of worship into a coordination system: the plan is the place where "what will happen" becomes "what each person prepares".

The two structures are jointly load-bearing:

- a plan with no team distribution is a word-processor template;
- a distribution layer with no plan of record is team messaging;
- a song library with neither is musician tooling.

### The Content Layer: Songs and Files

Mature products in this category almost always carry a **song library**: the church's accumulated repertoire as reusable records, each holding titles, keys, tempo and other musical attributes, lyrics, chord charts, arrangements in multiple keys, transposition, links to recordings, and usage history. Plan items reference library songs rather than re-typing them, so "add the set" is a lookup, and the library is where practice files live and where usage reports come from. Songs are commonly imported from church-music licensing services, and media files are stored in an account-wide library for reuse across services.

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Volunteer scheduling on the plan** — defined positions per service, scheduling of people into them (by hand, from templates, or auto-scheduled from availability and past rotations), notifications, accept-or-decline responses, availability block-outs, and substitution handling. Depth varies widely; some products carry the full loop, others a light notify-and-confirm layer.
- **Templates and recurring structure** — a recurring service saved as a template so next week's plan starts pre-filled; service types grouping plans and teams.
- **Rehearsal support** — practice audio with part-isolation and looping, chord-chart and sheet-music access on mobile devices, and in some products integration with dedicated rehearsal apps.
- **Communication** — reminders of upcoming commitments, follow-ups to non-responders, and team messaging scoped by team, role, or service.
- **Roles and permissions** — planner versus participant/viewer access; leaders over teams; controlled visibility of files and notes.
- **Print output** — printed run sheets for the stage and the booth, and in some products printed orders of worship or worship booklets for the congregation.
- **Usage reporting** — song-usage reporting to church-music licensing bodies, and reports on services, volunteers, and songs performed.

### One Structure, Many Implementations

```text
Concept:              Order of worship formalized
Realizations:         worship flow editor, service plan/run sheet, liturgical Ordo

Concept:              Preparation content on items
Realizations:         attached files, per-song charts and audio, plan notes, media libraries

Concept:              Team distribution
Realizations:         shared team views, mobile apps, printable run sheets, per-role file access
```

A reader who has only seen one shape of the product — say, a setlist-first app for a worship band — should still recognize a liturgy-first planning platform, or a print-first bulletin workflow, as the same Type from the two structures above.

## How It Works

### The weekly planning cycle

```text
Create or clone a plan for the upcoming service occasion
→ add items in order (songs from the library, sermon slot, readings, announcements, media)
→ attach notes, files, and media per item
→ schedule people into positions and notify them
→ team members respond and access their parts
→ rehearse from the attached material
→ run the service from the plan
→ archive; the plan becomes the record of what happened
```

### Build the plan

The planner opens a dated plan under a service type — often starting from a template of the regular order — and builds the service line by line: adding song items by picking from the song library (which brings their key, charts, and recordings along), inserting the sermon slot with notes, and attaching media. Items are reordered by dragging until the flow reads correctly.

### Fill the people

Positions are defined per service type or team; the planner schedules individuals or whole teams into them — manually, from saved rotations, or by auto-scheduling that respects availability and block-out dates. Scheduled people are notified and typically confirm or decline; planners chase non-responders and arrange substitutes. In planning-first products this loop is a light layer on the plan; in scheduling-oriented products the same loop is the whole product.

### Prepare

Each team member opens the plan, sees what they are responsible for, and prepares: downloading chord charts and lyric sheets, listening to their part of the practice audio (often with looping and part-isolation), reading plan notes. Rehearsal happens against the plan's material; the planner can often see who has accessed their files.

### Run and close the cycle

On the day, some products offer a live-run surface — the current item broadcast to the team, with progress and timing — while others serve printed run sheets for the same purpose. Afterwards the plan remains stored as a record of the service: which songs were used (feeding licensing reports), who served, and what the order actually was.

## Interfaces

The surfaces below are described conceptually; exact names and layouts vary by product.

### Plan editor (worship flow)

The planner's primary work surface.

- the ordered item list for one service occasion, with item types, keys, durations where tracked, and color coding
- primary actions: add/edit/reorder items, attach files and notes, add service times, clone from template, share or print

### Song library

The content backbone for musical items.

- searchable song records with keys, arrangements, lyrics, chords, attached media, usage history
- primary actions: add/import songs (commonly from church-music licensing services), transpose, add arrangements, attach files, tag and filter

### Scheduling view

Where people meet the plan.

- positions and teams per service, the assignment grid across upcoming services, availability and responses
- primary actions: schedule/notify, record responses, arrange substitutes, message team

### Team member view (often mobile)

The contributor's side of the loop.

- my schedule, my items in each plan, plan notes, attached charts/audio, respond to requests
- primary actions: confirm/decline, download or stream preparation material, message the team, request a substitute

### Live/run surface (where present)

A run-mode view of the plan used during the service.

- current item, upcoming items, timing and progress, plan notes
- primary actions: advance through items, keep the team in sync

### Reports and settings

- song-usage and volunteer-service reports; service-type, team, and permission configuration; media/file library management

## Important Rules / Behaviors

- **The plan is the coordination contract.** What is attached to an item is what the team prepares from; a missing chart or note is the classic failure the category exists to prevent. Distribution — not just authorship — is therefore a structural behavior, and file access is commonly permission-controlled by role.
- **Plans persist as records.** Completed plans are archived, not deleted; song usage history and service history accumulate in the library and reports.
- **Scheduling responses are reconciled, not assumed.** A scheduled volunteer who has not responded is a visible pending state that planners chase; substitutions are recorded on the plan rather than handled off-system.
- **Songs are reusable records, not text.** Because a song carries keys, arrangements, and licensing-relevant usage, adding "a song" to a plan is normally a reference into the library — this is what makes transposition, charts, and usage reporting coherent.
- **Recurring structure is configured, not re-created.** Regular services run on templates and service types; deviation from the template is the exception a planner makes deliberately.
- **The liturgical pole reorganizes the same core.** In liturgy-first products the "items" are liturgical elements (chants, hymns, texts of the rite) drawn from the tradition's calendar and books, the distribution loop delivers music by role, and the print output is a worship booklet — but the plan-of-record plus preparation-loop structure is unchanged.

## Variants

- **Setlist-first band workflow** — the dominant shape: song library, chord charts, transposition, rehearsal audio, and volunteer scheduling arranged around the weekly worship set.
- **Planning-first standalone specialists** — long-lived independent products centered on the worship flow editor with scheduling attached.
- **ChMS-bundled module** — the same loop realized as a feature area of a church management system, drawing people and teams from the congregation's records.
- **Companion-app families** — a free or low-cost planning app paired with sibling presentation, chord-chart, and rehearsal apps; the plan syncs to the companions so one build feeds display, charts, and practice.
- **Catholic liturgical preparation pole** — Ordo-shaped: assembling the order of worship from liturgical texts and music suggestions, managing a sacred-music library, producing printed worship booklets, and sharing music with musicians by role; characteristically without volunteer scheduling machinery.
- **Packaging and scale variants** — priced by planner seats with unlimited participant access, priced by team-member count, or free; church-plant to multi-campus scale.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Ministry Scheduling | closest sibling; frequently bundled | Ministry Scheduling centers *who serves* — positions filled at occasions across the whole ministry life, with the assignment loop as its core. Worship Planning centers *what happens in the service*. Products may carry both; removing position-filling and keeping the order/songs leaves Worship Planning, and pure schedulers exist with zero plan content. |
| Sermon Management | adjacent; different object | Sermon Management holds the *message as a record* — sermon library, publication, podcast feeds — that outlives the service. The plan holds a sermon *slot* (item + notes), not the message record. |
| Worship Presentation Software | adjacent; different moment | Presentation software displays lyrics, scripture, and slides *live during* the service to the congregation. Planning software organizes the service *before* it and equips the team. They meet at the hand-off: plans feed slides into presentation software. |
| Church Management System / ChMS | broader; frequent bundler | ChMS centers the congregation record core (people, households, giving, groups); worship planning is one capability slice that also exists as standalone products. |
| Religious Volunteer Management | adjacent; upstream | Volunteer-lifecycle machinery (recruiting, screening, training, tracking) centers the volunteer pool; worship planning consumes the pool it produces. |
| Event Agenda Management | distant analog | Builds a program/agenda for a one-off event with speakers, exhibitors, and attendees; worship planning serves a recurring weekly service with a volunteer production team and no attendee registration. |
| Calendar / Resource Calendar surfaces | adjacent | Service occasions are dated like events, but the managed unit is the plan and its content and people, not rooms, resources, or registrations. |
| Sheet Music / Rehearsal apps | complementary | Musician tools hold repertoire for the player; planning products hold the service plan. Products integrate with chart and rehearsal apps rather than replace them. |

## Representative Products

- Planning Center Services — standalone specialist; separately-priced product of a modular church-software suite
- Elvanto (a Tithe.ly company) — worship planning as a feature area of a full church management system
- WorshipTools Planning — free planning app paired with companion presentation, charts, and rehearsal apps
- WorshipPlanning.com (Planning) — long-lived standalone specialist
- Source & Summit — Catholic liturgical preparation pole

The core model was checked against the liturgical (Ordo-shaped, print-first, scheduling-free) pole as well as the dominant evangelical setlist shape, and against standalone, bundled, and free-companion packaging, to avoid defining the Type by one product philosophy or one denominational pattern.

## Sources

Research date: **2026-09-09**

- Planning Center — Services product page: https://www.planningcenter.com/services
- Elvanto — Worship features page: https://www.elvanto.com/features/worship/ (and https://www.elvanto.com/features/)
- WorshipTools — Planning product page: https://www.worshipextreme.com/en-us/planning (and https://www.worshipextreme.com/)
- WorshipPlanning.com — product page: https://www.worshipplanning.com/
- Source & Summit — digital platform page: https://www.sourceandsummit.com/

> Sourcing limitation: Faithlife Proclaim (a prep-to-display product often integrated from planning tools) was unreachable during research; the planning→presentation hand-off is therefore evidenced from the planning side of the integration, not from presentation software's own documentation. Planning Center's detailed help-center articles were not individually verified; operational claims for that product rest on its own product page, and no precise limits, time windows, or default settings are asserted anywhere in this document. Claims are calibrated to vendor-published documentation strength.
