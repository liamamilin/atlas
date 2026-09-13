# Scholarly Conference Management

## Overview

A **Scholarly Conference Management** system is the conference organizer's system of record for producing and running a scholarly conference. It anchors the conference edition as a managed event, runs the pipeline that turns submitted works into the conference's content (call for papers → submissions → evaluation → acceptance decisions), assembles the accepted works into the event's published program of sessions, and manages the participation that forms around the event — registration and payments, communication with authors, reviewers and delegates, and commonly the proceedings and the virtual or hybrid delivery of the event itself.

It solves a coordination problem that email, spreadsheets and generic event tools cannot: a conference must simultaneously collect and select content from a community of external authors, build a coherent multi-session schedule out of whatever was accepted, and register the people who will attend — all on a fixed calendar that culminates in the event itself. Every part of the system exists to move the conference through that cycle.

The boundary of the Type: it is the conference as an organizing whole. The review exchange alone — submissions paired with reviewers, reviews collected, decisions recorded, with no event around them — is the whole product of a Peer Review Platform. Generic event logistics — registration, venue, a curated agenda of invited speakers — is the territory of Event Management. A scholarly conference management system holds both together: the content pipeline that produces the program, inside the event container that the program serves.

## Users & Context

**Operators (the organizing side):**

- **Conference chair / program chair** — owns the cycle: defines the call, appoints the committee, oversees evaluation, ratifies decisions, owns the program.
- **Organizing committee / administrators** — configure forms and deadlines, manage users and roles, run registration, handle payments and correspondence.
- **Track chairs, session moderators, discussants** — program-level roles responsible for a subject track or a single session's operation.
- **Registration / front-desk staff** — on-site check-in, badge lists, last-minute registrations, payment queries.

**Participants (mostly external, mostly part-time):**

- **Authors / presenters** — submit works against the call, revise or upload final versions when accepted, register, and present in the program.
- **Reviewers / program committee members** — evaluate assigned submissions by a deadline under the process's confidentiality rules.
- **Delegates / attendees** — register, pay, and navigate the program (increasingly through a personal agenda or event app).

The work context is a **per-edition cycle with a calendar**: the call opens, a deadline closes submissions, a review window follows, decisions are released, final files are collected, the program is assembled and published, registration runs toward capacity, and the event happens — after which proceedings or an abstract book may be produced. Each edition is typically run as its own instance (its own site, database or setup), with configuration commonly carried over from the previous year.

## Core Model

The system's world is organized around one durable container — the conference edition — and the pipeline that fills it.

```text
Conference edition (the managed event of record)
  ├── Call & submission forms (configured per edition)
  ├── Submissions (papers / abstracts / posters / panels — authors, files, topics)
  │     ↓ evaluated by
  │   Reviewers & program committee  →  recorded decisions
  │     ↓ accepted works become
  ├── Program: tracks → sessions → presentations (with presenters)
  │     ↓ laid out on
  │   Schedule (days, times, rooms/locations)  →  published program
  ├── Participants & registration (attendees, fees, payments)
  ├── The event itself (on-site check-in / virtual or hybrid venue)
  └── Proceedings / abstract book (the edition's publication output)
```

### The defining core

Three structures. Remove any one and the software is no longer recognizable as scholarly conference management:

- **The conference edition as the managed event of record.** A persistent, individually identified event instance — dated, per-edition — that anchors the call, the committee, the program, and the participants. Conferences are run as instances: a separate site, database or setup per edition, with configuration commonly reused for the next one. Without the edition container there is no "the conference" being managed — only disconnected review runs and tools.
- **The submission-to-acceptance content pipeline.** Works are submitted against the conference's call through configured forms, evaluated (peer review is the dominant mechanism; light screening and no-review acceptance are configured postures of the same machinery), and resolved into recorded acceptance decisions. This is what makes the conference *scholarly* in structure: its content is contributed from the research community and selected by evaluation, not curated by organizers from invited speakers.
- **The program assembled from accepted works.** Accepted submissions become presentations placed into the event's program structure — grouped into sessions along subject tracks, scheduled into time blocks with rooms or locations, attributed to their presenters — and the program is published as the conference agenda, publicly or to registered participants. Without this step the software is a review exchange with decisions but no event program.

### Standard capabilities layered on the core

Mature products across the researched sample carry most of the following. They make running the conference practical; they do not define the Type.

- **Registration and payments** — participant groups with differentiated prices (member/student/regular), time-discount periods such as early-bird rates, configurable registration forms with conditional options and availability limits, automatic invoices and receipts, online payment gateways alongside manual payment entry, refunds and late-payer tracking.
- **Presenter–registration coupling** — the registration side and the submission side are one world: presenters are notified to register from the same system that accepted them, authors and reviewers typically register in the environment they already have accounts in, and some systems let organizers restrict registration to authors and presenters or make registration a submission requirement.
- **Camera-ready / final upload** — accepted submissions re-enter the system to deposit final versions for the program and the proceedings.
- **Communication machinery** — templated automatic notifications at every stage transition (submission received, review assigned, decision released, registration confirmed), plus bulk personalized email to authors, reviewers or delegates, with reminder scheduling.
- **Roles over one account** — author, reviewer, chair and administrator roles, extended by program-level roles (track chairs, meta-reviewers, session moderators, discussants, front-desk staff); one person often holds several roles in the same edition without switching accounts.
- **Multi-track support** — per-track submission types, deadlines, review committees and chairs.
- **Personal agendas** — attendees build their own itinerary from the published program, in the web app or a mobile event app.
- **On-site operations** — check-in and attendance marking, front-desk roles with limited data access, badge and attendee lists, last-minute registration.
- **Exports and reporting** — submissions, reviews, registrations and payments exportable at every stage; author indexes; dashboards showing how each stage is progressing.
- **Proceedings / abstract book output** — generated in-product as a formatted book, prepared for hand-off to a publisher, or produced through integrated publishing services.
- **Virtual and hybrid delivery** — links to live streams per session or presentation, on-demand content, video-conferencing integration, slide hosting.
- **Session-level interaction** — discussion boards on sessions and presentations, attendee networking, poster galleries.

### One structure, many realizations

The core is written conceptually; products realize each part differently.

```text
Concept:      Conference edition container
Realizations: separate database per conference; per-year site requests;
              per-event setup and pricing; event instance in an event platform

Concept:      Submission (the work entering the pipeline)
Realizations: full paper, abstract, poster, speaker proposal,
              symposium/panel proposal, award or grant application

Concept:      Evaluation stage
Realizations: full committee review with bidding and conflicts; abstract
              rating with presentation-type decisions; light screening;
              no-review acceptance

Concept:      Program unit (the accepted work placed in the schedule)
Realizations: contribution / presentation / talk — the same record that was
              submitted and reviewed, now scheduled

Concept:      Program structure
Realizations: tracks → sessions → scheduled blocks → presentations;
              streams and parallel sessions; poster sessions

Concept:      Registration
Realizations: full registration module with invoicing; integrated ticketing;
              registration handled by a host event platform
```

A reader who has only seen one implementation — say, a submission-and-review site with no schedule — should still be able to recognize the full conference system from this model, and vice versa.

## How It Works

The conference cycle runs once per edition, through gated stages:

### 1. Create the edition and configure the call

The organizers create the edition (a new site, database or event instance), define the program's subject tracks, configure the submission forms (submission types, fields, file requirements, topics), set the deadlines, and appoint the committee. Tracks usually must exist before the call opens, because submitters choose their track when submitting.

### 2. Collect submissions

```text
Call opens → authors submit (files + metadata + authors + track/topic)
→ confirmations sent → submissions close at the deadline
→ operators screen for formal requirements
```

Authors can typically edit until the deadline; some editions run multiple submission stages (abstract first, full paper later).

### 3. Evaluate

```text
Reviewers recruited / imported → state expertise or bid on submissions
→ declare conflicts → chairs assign (manually or with matching support)
→ reviewers submit structured evaluations by the deadline
→ committee discussion, optional author rebuttal
```

This stage is the review exchange — the same machinery a dedicated Peer Review Platform specializes in — running as one stage of the conference pipeline.

### 4. Decide and notify

Chairs record per-submission acceptance decisions (accept, reject, revise; sometimes a waitlist), release them with templated notifications, and open the final-upload stage so accepted authors deposit camera-ready versions. Acceptance is the hinge of the whole model: it is what moves a work from the pipeline into the program.

### 5. Build the program

```text
Define sessions (grouped by track/subject)
→ assign accepted submissions to sessions as presentations
→ schedule sessions into time blocks with rooms/locations
→ check for conflicts (a presenter in two places at once, empty sessions,
  missing presenters)
→ publish the program (public link, or restricted to registered participants)
```

The program builder works on the accepted submissions themselves — organizers assign the existing records rather than re-typing content — and the published program typically exposes titles, abstracts, presenters and sometimes downloadable files. Attendees can usually build personal agendas from it.

### 6. Register participants

Registration forms open with participant categories and period-based pricing; attendees register, pay (online gateways, bank transfer, or on-site), and receive invoices and confirmations. Presenters are commonly expected to register for the event to keep their slot in the program, and organizers monitor the registration list against the program (who has registered, who has paid, who still owes).

### 7. Run the event

On the event days the system serves the published program to attendees (web, mobile app, printed export), supports on-site check-in at the registration desk, and — for virtual or hybrid editions — links each session and presentation to its live stream, meeting room or on-demand content.

### 8. Produce the record

After the event, the edition's output is produced: proceedings or an abstract book generated in the product or exported for a publisher, final statistics, and the archived record of the edition. Configuration is commonly stored to seed the next edition.

### Core vs standard vs optional

**Defining core** — without these, not scholarly conference management:

- the conference edition as a managed event instance
- the submission-to-acceptance pipeline (call → submissions → evaluation → decisions)
- the program assembled from accepted works and published as the event's agenda

**Standard capabilities** — present in most mature products:

- registration and payments (with presenter–registration coupling)
- camera-ready / final uploads
- communication machinery and reminders
- role system over one account; multi-track support
- personal agendas; exports and reporting
- proceedings / abstract-book output
- virtual/hybrid delivery surfaces; on-site check-in

**Optional / variant** — depends on segment, scale and posture:

- native mobile event apps; exhibitor and sponsor spaces; poster galleries
- integrated room/venue booking; event surveys; certificates and invitation letters
- awards and best-paper flows
- open-source self-hosting vs SaaS; free tiers for small events

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Organizer / chair console

The organizing side's cockpit for the whole edition.

- stage-by-stage overview (submissions, review progress, decisions, registrations, payments), task cards for upcoming work, statistics
- primary actions: configure forms/deadlines/tracks, manage users and roles, assign reviewers, record and release decisions, build and publish the program, message groups, export data

### Author / presenter portal

The submitter's window into the cycle.

- submission form, submission status timeline, decision notification, final-upload step, registration entry, presenter details (bio, photo) where collected
- primary actions: submit, revise, upload final version, register, view program placement

### Reviewer workspace

The evaluator's queue.

- assigned submissions with deadlines, submission files, the review form, committee discussion where enabled
- primary actions: bid or accept assignments, download files, enter or edit reviews, comment

### Program builder / scheduling grid

Where the event's content structure is assembled.

- sessions and their blocks on a day/time grid, accepted submissions awaiting assignment, presenter conflict indicators, draft/published state
- primary actions: create sessions and blocks, assign presentations, set times and rooms, run conflict checks, publish or unpublish

### Public program page

The conference's public face during the run-up and the event.

- agenda by day with sessions, presentations, presenters and abstracts; downloadable files where enabled; personal-agenda controls; virtual-session links where applicable
- primary actions: browse, search, bookmark sessions, open session/presentation details

### Registration and payment

The attendee's enrollment surface.

- registration form with categories and priced options, payment method selection, invoice/confirmation access
- primary actions: register, pay, edit registration (within rules), cancel

### On-site front desk

The check-in surface for the event days.

- attendee search, check-in/attendance marking, last-minute registration, payment status
- primary actions: check in, register walk-ins, print badges/receipts

### Virtual event surface

The event's online venue for virtual and hybrid editions.

- live session streams, on-demand content, presenter pages, session discussion
- primary actions: join session, watch on-demand, comment or ask questions

## Important Rules / Behaviors

- **The cycle is gated by deadlines.** Every stage — submission, review, final upload, registration — opens and closes on configured dates, and the system disables the corresponding actions when a deadline passes. Late reviews or late files require operator intervention.
- **Acceptance links the pipeline to the program.** Only accepted works enter the program; the acceptance decision is the state change that converts a submission into a presentation. Rejected or withdrawn works drop out of the program path (their records remain).
- **Presenting is commonly tied to registering.** The registration side and the program side are coupled: presenters are expected to register, some systems restrict registration to authors and presenters or make registration a submission requirement, and organizers track registered-and-paid status against the program.
- **The program has publication states.** While being built, the schedule, abstracts and author lists are typically hidden from regular users (draft mode); publishing exposes the program publicly or to registered participants only, at the organizers' choice.
- **Scheduling is conflict-checked.** Mature products detect direct and potential time conflicts — a presenter scheduled in two parallel sessions, empty sessions, talks without presenters — before the program is published.
- **One account, many roles, scoped access.** A person may be author, reviewer and chair in the same edition; what they see depends on the role they are acting in, and sensitive data (reviews, payments) is visible only to the roles that need it.
- **Registration has payment states.** A registration carries its fee calculation, payment status and invoice; edits after payment are restricted or re-invoiced, and unpaid registrations can be blocked from check-in.
- **Editions are separate but continuous.** Each edition runs in its own instance with its own data; configuration and user bases are commonly carried forward, but each edition's record — submissions, reviews, program, registrations — belongs to that edition.

## Variants

- **By format** — in-person (the classic shape: program, registration, on-site check-in), virtual (the program becomes an online venue with live and on-demand content), hybrid (both at once).
- **By scale** — small workshops (a submission form, a review round, a one-day program) through to large multi-track conferences and collocated events run as joint programs under one schedule.
- **By review intensity** — full paper peer review with committee discussion and rebuttals; abstract review deciding presentation types (talk/poster); light screening; acceptance without review. The pipeline machinery is the same; the evaluation depth is configured.
- **By audience** — academic and scientific conferences (the center of gravity), medical and technical society meetings, and association or professional events that run contributed-content programs with the same machinery.
- **By proceedings posture** — generate the abstract book or proceedings in-product; prepare exports for an external publisher; or publish through the vendor's integrated publishing services.
- **By deployment and pricing** — hosted SaaS with per-event or quoted pricing; free or low-cost per-edition licensing; open-source self-hosting for institutions.

A variant remains a variant unless it changes the core: if the software stops producing the program from evaluated submissions, or stops holding an event container at all, it has become a peer review platform or a generic event tool, not a conference management system.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Peer Review Platform | closest sibling; partial overlap | the review exchange is its *entire* product — submissions paired with reviewers, reviews, outcomes — with no event container, no program, no registration; here the review exchange is one stage inside the conference pipeline. Remove the event/program/registration machinery from a bundled product and a peer review platform remains; remove the review machinery and a generic event system remains |
| Event Management Platform | adjacent; different organizing whole | centers the event's logistics — registration, venue, curated agenda of invited speakers, check-in, apps; the content pipeline exists there only as an add-on module (abstract management). Remove the pipeline → generic event management remains; remove the event logistics → the pipeline remains |
| Event Registration Platform | capability slice | standalone registration/ticketing for events generally, with no content pipeline and no program; registration here is one module of the conference whole |
| Event Agenda Management | capability slice | schedule building exists on both sides; the discriminator is the agenda's source — assembled from evaluated submissions here, curated by organizers there |
| Convention / Exhibition Management | adjacent | centers trade-show semantics (exhibitors, booths, lead retrieval); exhibitor/sponsor modules appear inside conference products as packaging |
| Academic Journal Management | sibling in the research & knowledge domain; different container | the journal is an ongoing publication container (issues, production pipeline) with review as a stage; the conference is a dated edition whose pipeline produces the event's program, with proceedings as an output often handed to a publisher |
| Association Event Management | adjacent | centers the association's broader event program (multi-event calendars, membership context); when a single contributed-content conference is the center, this Type applies |
| Attendee Management / Event Mobile App | capability slices | event-side capabilities that also exist as standalone Types for the generic event market; here they are standard or optional layers |

The boundary with the Peer Review Platform is the most important one, because the two Types overlap on the evaluation stage and many products bundle both sides. The structural difference is the organizing whole: the review exchange alone versus the conference edition with its produced program.

## Representative Products

- **ConfTool** — long-established European system covering the full cycle: submission and review, program scheduling, participant registration and invoicing, on-site check-in; free edition for small events.
- **Ex Ordo** — all-in-one platform for scientific, medical and technical events: review, registration, visual program builder with conflict checking, virtual/hybrid venue, proceedings book and mobile app.
- **Oxford Abstracts** — academic conference platform tiered from abstract management (submission → review → decisions → ticketing) up to a full conference site with program builder, networking and poster galleries.
- **Indico** — CERN's open-source event platform whose conference shape spans program tracks, call for abstracts, review workflows, the session/block timetable, registration and room booking.
- **EasyChair** — long-established workhorse combining submission/review machinery with registration, program generation from submission data, and integrated proceedings publishing.

The defining core was additionally checked against boundary probes: a review-workflow-only conference toolkit (Microsoft CMT), a pure review exchange with no event machinery (OpenReview), and an abstract-management module inside a generic event platform (Cvent) — to separate the conference whole from the review exchange and from event logistics.

## Sources

Research date: **2026-09-09**

- ConfTool — official homepage and full feature list — https://www.conftool.net/en/ , https://www.conftool.net/en/features.html (reviewer documentation via the paired Peer Review Platform research, 2026-09-08)
- Ex Ordo — official product pages (conference management, programme) — https://www.exordo.com/ , https://www.exordo.com/product/conference-management , https://www.exordo.com/product/conference-programme
- Oxford Abstracts — official homepage and academic conference software page — https://www.oxfordabstracts.com/ , https://www.oxfordabstracts.com/product/academic-conference-software/
- Indico — official user guide (conference, programme, timetable, registration configuration) — https://learn.getindico.io/conferences/about/ , https://learn.getindico.io/conferences/timetable/ , https://learn.getindico.io/conferences/registration_config/
- EasyChair — official product pages (home, registration, Smart Program) — https://easychair.org/ , https://easychair.org/registration , https://easychair.org/smart_program
- Microsoft CMT — official documentation index (boundary probe) — https://cmt3.research.microsoft.com/docs/
- OpenReview — official documentation (boundary probe, via the paired Peer Review Platform research) — https://docs.openreview.net/
- Cvent — official abstract management product page (boundary probe) — https://www.cvent.com/en/abstract-management-software

> Sourcing limitations: EasyChair's help center was unreachable (per the paired Peer Review Platform research), so its claims are calibrated to official product-page level. Ex Ordo and Oxford Abstracts evidence is product-page level; their help centers were not fetched, so operational detail beyond the documented features is not asserted. Microsoft CMT's deeper documentation pages were only partially reachable; its program/registration machinery is reported as "not evidenced," not as "absent." Vendor scale figures are vendor-stated marketing claims. Precise operational details that depend on inaccessible documentation (exact scheduling constraints per product, refund rules, numeric limits) are intentionally not stated; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
