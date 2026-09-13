# Theater Production Management

## Overview

A **Theater Production Management** application is the production office's system of record for making and running a live performance: it holds the production (a specific show) as a managed unit, the company of people making it, the schedule of rehearsals, performances and technical work that carries the show from first rehearsal to closing, and the communication that keeps the whole company informed and on schedule.

Its defining core is four things held together:

```text
Production (the show as a managed unit)
└── Company (cast, crew, designers, stage management — with production roles)
    └── Schedule of production calls (rehearsals, performances, load-ins, fittings)
        └── Company-facing communication (the callboard: what's happening, what changed, what you owe)
```

Everything else commonly associated with the category — performance reports, conflict detection, attendance, contact sheets, season planning, budgets, inventory — is built on this core but does not define it.

The boundary is equally clear: this software manages the **making and running** of shows, not the selling of tickets (the audience/business side), and it plans a **live performance run**, not a film or television shoot.

## Users & Context

The system is two-sided by nature.

**Planning side** — the people who run the production:

- **Production managers and production coordinators** plan the season, build schedules, book spaces and people, and keep budgets and resources in view.
- **Stage managers** run the day-to-day: they publish calls, track attendance and conflicts, file rehearsal and performance reports, and keep the company moving.
- **Company and technical managers** maintain the roster, contact details, emergency and medical information, and access rights.

**Company side** — everyone the production depends on, consuming far more than they edit:

- **Cast** need their rehearsal and performance calls, fittings, and schedule changes.
- **Crew and designers** need load-ins, technical rehearsals, department notes, and shared documents.
- In education settings, students run the system under supervision and **parents/guardians** see schedules and receive notifications.

The work environment spans a desk (building schedules, maintaining records) and the building itself (posting notices, taking attendance, calling a show). Updates are frequent and time-sensitive: a rehearsal moves, an actor is released early, a space frees up — and the change must reach everyone affected before they leave home.

The context is any organization that mounts productions: producing theaters, opera and dance companies, festivals, venues with in-house shows, universities and schools, and live-event producers. The same structures serve all of them.

## Core Model

### The Defining Core

**1. The production.** The central container is the production — one identified show with a title, dates, and its own body of work. Everything in the system hangs on it: the schedule, the people, the documents, the reports. A producing organization holds many productions at once — a season of shows, each siloed so that members see only what concerns them — and a closed production remains retrievable as an archive rather than being deleted.

**2. The company.** A production is carried by people: cast, crew, designers, stage management, production staff. Each is a record with contact details and one or more production roles, grouped into departments and working groups (cast, lighting, wardrobe, stage management, and so on). Roles matter as much as people: a schedule can be built against a role before anyone is cast in it, and the person drops in later. Contact information carries privacy — each member decides what is shared on company contact sheets, while managers can reach emergency and medical details.

**3. The schedule of production calls.** The schedule is the production's operating rhythm: dated, time-bound **calls** — rehearsals, performances, load-ins, technical work, fittings, meetings — each binding specific people to specific spaces at specific times. A performance is a schedulable, repeatable event: the run of a show is many scheduled performances of one production. The schedule lives under constant change, and mature systems keep it consistent: they detect conflicts (a person or space called twice), guard against double-booking, and propagate every change to every view derived from it.

**4. Company-facing communication (the callboard function).** Production management is not a private planning tool — its audience is the whole company. The traditional callboard at the stage door is the model: a single place where schedules, notices, and paperwork are posted for everyone. In software this becomes announcements and notes targeted at the whole organization or one production (often with expiration dates), shared files and discussions, and published schedules that reach the company with minimal friction — push notifications, text and email fan-out, printable calendars, or auto-updating web pages that require no account to view. Receipt matters: systems confirm that a note was read by each person it was meant for. And the flow runs both ways — the company reports back availability and conflicts, signs up for open calls, and answers production reports with follow-ups.

Remove any one of the four and the Type collapses into something else: without the production, a generic project workspace; without the company, a calendar with nobody in it; without the schedule of calls, a contact list with files; without the callboard function, a planner the company never sees.

### Standard Capabilities

Mature products commonly add, on top of the core:

- **The report cycle.** Stage management runs on reports: after each rehearsal or performance, a structured report is filed — what happened, what each department owes — with follow-up notes tracked to completion. Products typically offer report templates per production type, drafting, and revision propagation: an edited report re-reaches everyone who received the original.
- **Availability and conflict handling.** Members' availability and conflicts are captured against the schedule; conflicts are detected automatically; crew can self-sign-up for open calls; managers see who is over-committed across productions.
- **Attendance and hours.** Sign-in per day or per call, with weekly hours computable for managers and visible to members.
- **Contact sheets** generated from the roster, respecting each member's privacy choices.
- **Season and portfolio planning.** A company calendar across all productions, reusable schedule templates, and cloning of a past production's structure onto a new one (anchored, for instance, to its first performance).
- **Calendar interop and print.** Subscribe-able calendar feeds, printable call views, and mobile-friendly shared pages — because the company consumes the schedule in many ways.

### One Structure, Many Implementations

The core is conceptual; products implement it differently:

```text
Concept:                  Company-facing distribution
Implementations:          auto-updating shared web pages (no login), in-app callboard
                          with read confirmations, email/SMS/push fan-out, printed
                          calendars posted to a physical wall

Concept:                  Roles before people
Implementations:          role placeholders schedulable in the timeline and castable
                          later; character/role groups built into preliminary
                          rehearsal schedules

Concept:                  Resources for the production
Implementations:          simple shared file areas; structured item inventories with
                          departments and QR labels; equipment requirements attached
                          to events feeding budgets
```

A reader who has only seen a modern cloud product should still recognize the older shape: the paper schedule taped to the callboard, the typed report duplicated to department heads, the ring binder of contact sheets.

## How It Works

**Set up the production and company.** A production is created with its identity and dates; the company is assembled from the organization's people (or added on the fly), each with roles and department assignments. Access is tiered: managers edit, the company views — and distribution to the company often needs no accounts at all.

**Build and maintain the schedule.** The production's timeline is built from calls: a rehearsal for the cast, a load-in for the crew, a fitting for two actors, a performance for everyone. Each call carries time, duration, space, people (or roles), and department tags. Building against roles lets a rehearsal schedule exist before casting is final. As reality shifts — dates move, spaces change — the schedule is edited in place and the change ripples to every view, feed, and page derived from it.

**Publish the callboard.** The schedule and notices are pushed out to the company: an announcement for the whole building or one show, a rehearsal calendar for the cast, a load-in page for the crew. Notifications fan out the moment something is posted; shared pages always show the latest version; a note confirms who has read it. Nobody should learn about a moved rehearsal from standing in the wrong room.

**Run the day and the report cycle.** Attendance is taken at calls; conflicts surface as they arise. After rehearsal or performance, stage management files a report — department by department, with follow-up items — and tracked notes chase what was promised. Report revisions re-deliver automatically to their recipients.

**Plan beyond one show.** At the organization level, productions compose into a season calendar; templates and cloning turn last season's structure into next season's starting point. Where the organization runs shops or stock, resources attach to productions as requirements with costs; where it hires crews, calls carry labor needs and rates.

**Close and archive.** When a production closes it is deactivated, not destroyed: its schedules, reports, and files remain retrievable as the organization's institutional memory.

## Interfaces

Exact layouts vary by product; these are the surfaces the work happens on.

**Production home / dashboard**
Purpose: orient within one production (or across the season).
Typical information: productions and their states, upcoming calls, recent notices, pending follow-ups.
Primary actions: open a production, post an announcement, jump to today's schedule.

**Schedule / calendar**
Purpose: build and read the production's rhythm of calls.
Typical information: dated calls with time, space, people, department; month/week/day/list views; filters by person, department, show, location.
Primary actions: create and edit calls, resolve conflicts, shift dates, filter to "my calls."

**Call / event detail**
Purpose: one scheduled unit of work.
Typical information: time and duration, space, attendees or roles, department, attachments, related report.
Primary actions: add or change attendees, book crew for the call, sign up for an open call, attach a report.

**Callboard / announcements**
Purpose: broadcast and targeted production communication.
Typical information: announcements with expiration, notes with per-person read state, discussions with attachments.
Primary actions: post to a production or the whole organization, confirm receipt, reply or discuss.

**Company roster / contact sheets**
Purpose: the people of the production.
Typical information: names, roles, departments, contact details (privacy-scoped), emergency and medical information for authorized managers.
Primary actions: add or edit members, assign roles and groups, generate contact sheets.

**Reports**
Purpose: the stage-management record of what happened and what is owed.
Typical information: rehearsal/performance report bodies by department, follow-up notes with due dates, templates.
Primary actions: file from an event, edit and re-deliver, track follow-ups to completion.

**Shared pages (for the company)**
Purpose: consumption surfaces that require no account.
Typical information: schedule filtered to the viewer, notes and to-dos, locations, team lists, attachments.
Primary actions: view, filter, subscribe from a personal calendar, bookmark on a phone.

**Settings / user management**
Purpose: access and organization configuration.
Typical information: user levels, module access, department and role vocabularies.
Primary actions: grant or restrict access, configure who sees which productions.

## Important Rules / Behaviors

**Conflict guards are structural.** The system actively prevents the classic scheduling failure: a person or a space called twice at the same time. Conflicts are detected when calls are made, not discovered when people collide in the hallway.

**Information silos per production.** A member of one production does not see the calls, files, or reports of another — the production container is also the privacy boundary. Organization-wide notices are the deliberate exception.

**Two-sided access.** Editing is for managers; the company consumes. Consumption is deliberately low-friction (no-login pages, read confirmations, fan-out notifications) because the audience includes everyone from leads to volunteers — and, in education, parents.

**The schedule is the source of truth.** Printed calendars, personal-calendar feeds, and shared pages are all derivatives. Change the schedule once; every derivative updates. The failure mode the category exists to kill is the stale PDF.

**Reports drive follow-through.** A report is not a diary: its follow-up notes are tracked items with owners and due dates, and revised reports re-reach their original recipients.

**Closed productions persist.** Deactivation archives rather than deletes; the organization's production history remains inspectable.

## Variants

- **Producing house / repertory** — a season of shows in one system; season calendars, template cloning, cross-show resource and crew management are the emphasis.
- **Education and school theater** — students run real productions under supervision; parents/guardians become a formal audience; sign-in sheets and notifications are tuned to a school day.
- **Commercial and union production** — crew labor deepens: positions with rates, booked calls, per-person call times, overtime visibility, exports toward payroll.
- **Resource-heavy organizations** — shops and stock bring item inventories, requirements attached to calls, and cost rollups onto the production.
- **Adjacent live audiences** — opera, dance, festivals, corporate and live events run on the same structures with different vocabulary; some products serve all of them.
- **Documentation-focused edge** — tools centered on stage-management paperwork (blocking and cue documentation) sit at this Type's boundary; research for this document could not verify that product family through official documentation, so its placement is left open.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Film Production Management | sibling, same family | plans capture of recorded media: script breakdown → scenes on shoot days → call sheets per shooting day; no performance run, no rehearsal-report cycle |
| TV Production Management | sibling, same family | as film; adds multi-camera rundowns and broadcast execution machinery |
| Production Scheduling / Call Sheet Application | instrument inside the family | the scheduling/call-sheet tool itself; theater production management is the whole production office around its schedule |
| Performing Arts Organization Management | adjacent, different side | the organization's audience and business system (ticketing, subscriptions, fundraising, marketing); the production here is a unit of work, there a unit of sale |
| Venue Management System | adjacent | bookable spaces as sellable inventory; here spaces are schedulable resources bound to calls |
| Project Management Application | genus neighbor | generic projects/tasks/teams; lacks production-native objects — calls, the company, performances, event-tied reports — and the whole-company audience |
| Event Management Platform | adjacent | attendee-facing logistics (registration, ticketing); here the managed population is the company, not an audience |
| Workforce Scheduling / Employee Scheduling | genus neighbor | shift scheduling over employees; the production context, the call semantics, and the performance run are what this Type adds |

The most consequential boundary is with **Film/TV Production Management**: both are "production management," both have casts, crews, schedules, and paperwork. The test is the delivery unit. If the system's heart is the live run — rehearsals leading to repeated scheduled performances of a fixed show, with rehearsal and performance reports feeding the company — it is this Type. If the heart is the shoot — scenes captured on days, call sheets per shooting day — it is film/TV territory.

## Representative Products

- **VirtualCallboard** — callboard, scheduling, and communication for stage and production managers; theater, opera, education.
- **Propared** — production planning for arts and events organizations; schedules, people, spaces, resources, budgets across a season.
- **Dramatify** — studied as the film/TV/broadcast comparator that clarifies this Type's boundary; its shoot-centric structures are what a theater production system does *not* center on.

## Sources

- VirtualCallboard — homepage, Features, For Education: https://www.virtualcallboard.com/ , https://www.virtualcallboard.com/features/ , https://www.virtualcallboard.com/for-education/ (researched 2026-09-09)
- Propared — homepage, Explore Scheduling, and official training materials: https://www.propared.com/ , https://www.propared.com/explore-scheduling/ (researched 2026-09-09)
- Dramatify — homepage and feature inventory: https://dramatify.com/ (researched 2026-09-09)
- CallBoard (boundary examination only): https://callboard.app/ (researched 2026-09-09)

> Sourcing limitation: the stage-management-documentation pole (blocking/cue-sheet tools) could not be verified through official documentation during research — the leading product's site is not readable without JavaScript and its help center is closed. No claims about that product family are made in this document beyond acknowledging the edge in Variants. Precise operational details (specific limits, default rates, overtime rules) observed in vendor materials are intentionally kept out of this document.
