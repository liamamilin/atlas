# Audition Management

## Overview

An **Audition Management** application runs the selection process by which a performing-arts organization fills defined roles with performers. It organizes the work around a production, show, or program that holds the roles to be filled; tracks individual performers as candidates for those roles; runs audition rounds — scheduled live sessions, submitted recordings, or live virtual auditions — that attach an evaluation to each candidacy; and moves candidates through stages toward a recorded casting decision that can be shared with the people who ratify it.

The defining core is small:

```text
Selection context (production / show / program)
└── Role or opportunity to fill
    └── Candidacy (a specific performer considered for a specific role)
        ├── Demonstration material (the audition: live, recorded, or virtual)
        ├── Evaluation record (ratings / notes / score)
        └── Selection status (progression toward cast or passed)
```

Everything else commonly associated with the category — published casting notices, self-tape workflows, audition scheduling machinery, scoring rubrics, secure sharing with producers — is standard capability in current products but is not what makes the product an audition manager. A paper-era theater running sign-up sheets, a headshot pile, penciled audition notes, and a callback list satisfies the same core structure.

When the center of gravity shifts to publicly listing opportunities for talent to discover, the product is drifting toward a different Application Type (Casting Platform). When it shifts to running the talent's own business, it is Talent Agency Management. When it shifts to logistics after the roles are filled, it is production management.

## Users & Context

**Primary operators** are the people responsible for filling the roles:

- **casting directors and casting teams** — run casting for film, television, and commercial productions; manage the candidate flow per role and stage the rounds
- **program or admissions staff and adjudication panels** — in performing-arts education, festivals, and youth ensembles, they collect applications, schedule audition days, and score candidates
- **artistic directors, show administrators, stage managers** — in community and regional theater, often the same small team defines roles, runs sign-ups, and issues role offers

**Decision-makers outside the casting team** — producers, directors, studio executives, admission committees — do not run the funnel but ratify its output. A large part of the software's job is packaging candidacies (shortlists, recordings, evaluations) for these people to review.

**Participating, non-operator users** act on candidacies rather than manage them:

- **performers / auditionees** — submit profiles and demonstration material, book audition slots, upload self-tapes, confirm appointments, receive offers
- **talent representatives** (agents, managers) — submit and manage candidacies on behalf of their clients in film/TV and commercial casting
- **parents of minors** — in community theater, commonly manage a child's audition form and participation from their own account

The context is any domain where selection is by performance demonstration: film, television, commercials, theater, dance, music, opera. The work is deadline-driven and round-based — an intake window, one or more audition rounds, callbacks, then offers.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as audition management:

- **A selection context with defined roles to fill** — casting always happens inside a container (a film or series project, a show, a program or ensemble) that holds named parts, positions, or seats. Without defined roles there is no casting semantics — only generic forms or events.
- **Individual performer candidacies** — a candidate is not anonymous traffic; the system tracks an identified person, with a profile and demonstration material, considered for one or more specific roles. Without this, the product is a media library or a directory, not a selection process.
- **Audition rounds that produce evaluative records** — the audition is the defining act: an organized opportunity for the candidate to demonstrate suitability — in a scheduled live session, in a submitted recording, or in a live virtual room — and each demonstration produces an evaluation (notes, ratings, or scores) attached to that candidacy. Without this, the product is intake and roster-keeping only.
- **Staged progression toward a recorded casting decision** — candidacies move through statuses (in consideration → auditioned → callback → offered/cast, or passed) until each role is filled or the candidacy ends. Without this, the product is signup logistics; the point of the work is the decision.

Exact status labels vary by product; the staged progression itself does not.

### Standard Capabilities

Mature products commonly add the following. They make the core practical but do not define the Type.

- **Role definitions with specs** — character description, age range, physical or skill requirements; in film/TV these are packaged as a "breakdown" that can be published or sent to representatives.
- **Intake forms and candidate profiles** — structured capture of headshot, experience, training, contact details, and (in theater) emergency contact; profiles are usually persistent and reusable across productions.
- **Recorded-audition handling** — requesting a self-tape with sides, instructions, and a deadline; receiving the upload; reviewing it in place against the role.
- **Scheduling machinery** — audition slots or time blocks with capacity limits, candidate self-scheduling or operator assignment, reminders, confirmations and change requests, check-in on the day.
- **Live virtual auditions** — a waiting lobby, virtual rooms, readiness status, and storage of what happens in the room (recordings, notes), so that remote and in-person rounds can run on one system.
- **Evaluation tooling** — free-text notes and triage ratings at minimum; scorecards or rubrics where the organization scores formally; multi-evaluator support so several people can assess and comment on the same candidacy.
- **Triage, callbacks, and offers** — shortlists per role, callback rounds, and offer/booking as the terminal positive state.
- **Curated packaging and controlled sharing** — lists of candidates per role and shareable views (links or exports) for producers, directors, or committees, with the selecting organization controlling what is visible.
- **Communications** — confirmations, reminders, schedule changes, and direct messaging to candidates, parents, or representatives.
- **Exports and reporting** — candidate lists and evaluation summaries for production meetings or program administration.

### One Structure, Many Implementations

The core model is conceptual; products realize the concepts differently:

```text
Concept:  Defined role to fill
Implementations:   character breakdown (film/TV), cast part (theater), seat/position in a program or ensemble (education)

Concept:  Candidacy intake
Implementations:   submission to a published breakdown, invited/private submission, signup form, formal application with media

Concept:  Audition round
Implementations:   scheduled live slot, submitted recording (self-tape), live virtual audition room, hybrid of these

Concept:  Evaluation
Implementations:   notes, triage ratings, scorecards, rubric-based adjudication

Concept:  Decision
Implementations:   offer/booking (film/TV), role offer (theater), admission/acceptance communication (education)
```

A reader who has only seen one implementation — for example, film/TV casting with agent submissions and self-tapes — should still be able to recognize a community-theater signup-and-callback workflow or a conservatory adjudication day as the same Type.

## How It Works

### Define the roles

The operators create the selection context and enumerate what must be filled: each role gets a name, a description, and the requirements candidates will be judged against. In film/TV this is the breakdown; in theater it is the cast list of the show; in education it is the program's openings and audition requirements.

### Collect candidates

Candidates enter through the intake mode the organization has chosen: they respond to a published breakdown, submit on invitation, fill in a signup form, or submit a formal application with recorded material. Each intake creates or updates a candidate profile and a candidacy per role. Where representatives are used, they submit on behalf of their clients; where minors are involved, a parent typically mediates the submission.

### Run the audition round

The audition itself takes one of three forms, and mature products usually support more than one:

```text
Scheduled live audition
→ operators publish slots or sessions (with capacity limits)
→ candidates book, or operators assign
→ reminders go out; candidates confirm or request changes
→ on the day: check-in, then the room

Submitted recording (self-tape)
→ operator requests a tape from specific candidates
→ sides, instructions, and a deadline accompany the request
→ candidate records and uploads
→ tape lands against the candidacy for review

Live virtual audition
→ candidate enters a lobby from a link
→ system shows readiness; operator moves them into a room
→ performance happens under the platform's video; recordings and notes are captured
```

### Evaluate

Evaluators — the casting team, adjudicators, or invited reviewers — attach their judgment to the candidacy: notes, ratings, flags, or scored criteria. Evaluation is typically cumulative: intake triage, then round-by-round assessment. Multiple evaluators can score the same candidate independently; in the education variant the scoring follows a rubric.

### Progress and decide

Candidates advance through statuses. The common shape:

```text
New candidacy
→ in consideration (triage: keep / hold / release)
→ auditioned (first round)
→ callback (subsequent round)
→ offered / cast
        or
→ passed (exits the funnel)
```

When a role is offered and accepted, the selection is complete: the role is filled, and in theater-oriented products the accepted performer may also gain access to the production's working materials (schedules, notes, communications). In every variant the funnel ends in a recorded decision per role.

### Package for the decision-makers

Throughout — and especially before final decisions — the casting team assembles what decision-makers need to see: shortlists per role, selected recordings, evaluation summaries. These go out as shareable views whose visibility the selecting organization controls, because audition material is sensitive (unreleased production information, footage of minors, pre-release casting choices).

### Capability tiers

**Defining core** — selection context with roles; individual candidacies; audition rounds producing evaluative records; staged progression to a recorded decision.

**Standard capabilities** — role specs/breakdowns, intake forms and profiles, self-tape handling, scheduling machinery, virtual audition support, evaluation tooling, triage/callbacks/offers, controlled sharing, communications, exports.

**Variant-dependent** — public marketplace intake, agent-mediated submissions, parent-mediated minors, rubric adjudication, application fees, union/eligibility filtering, repertory casting across multiple shows, production-cycle integration beyond casting.

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Production / selection dashboard

The operator's entry point: the container (project, show, program) with its roles and where each stands.

- typical information: roles, candidacy counts per role and stage, upcoming audition days, pending offers
- primary actions: open a role, start an intake, open the schedule

### Role detail / breakdown

One role to be filled.

- typical information: description, requirements, candidates attached to the role and their states
- primary actions: add/edit role specs, publish or send the breakdown, review candidacies

### Candidacy list

The working list of candidates, filtered per role or round.

- typical information: headshot, profile summary, demonstration material, current status, evaluation summary
- primary actions: triage (advance/hold/pass), request a tape, assign to a slot, message, export

### Audition schedule

The round's time structure.

- typical information: slots or sessions, capacity, who is booked, confirmations
- primary actions: create slots/sessions, assign or self-book candidates, send reminders, handle change requests

### Audition-day surface

What the room runs on.

- in person: check-in of arriving candidates, order of the room, per-candidate note capture
- virtual: lobby with readiness status, room-to-room movement, live capture of recordings and notes

### Candidate detail

One performer's file in this selection.

- typical information: profile (headshot, experience, training), submitted media, per-role candidacies, evaluations from all evaluators, status history
- primary actions: play recordings, add evaluation, change status, offer

### Review / share view for decision-makers

The packaging surface for producers, directors, or committees.

- typical information: curated candidate lists per role, selected recordings, notes the organization chose to expose
- primary actions: review, comment where enabled, approve choices

### Candidate-facing portal

What auditionees and their intermediaries use.

- typical information: available opportunities or assigned roles, profile, booked slots, requested tapes and deadlines, messages
- primary actions: submit materials, upload a self-tape, book or change a slot, confirm attendance, respond to an offer

## Important Rules / Behaviors

- **Candidacy is per role.** The same performer can hold several candidacies inside one selection context, each with its own material, evaluation, and status. Decisions attach to the candidacy, not merely to the person.
- **Demonstration material answers the role.** A requested tape or a live audition is bound to the role's brief (sides, requirements) and its deadline; material is therefore evidence within a candidacy, not just an asset in a profile.
- **Status transitions drive the funnel.** Triage gates who auditions; round results gate who is called back; only advanced candidates receive offers. Bulk status changes and role-level views are the operator's control surface.
- **Evaluation is multi-person and mostly private until shared.** Several evaluators score independently, and their notes are visible to the selecting team; what reaches producers, directors, or committees is a deliberate subset. Audition material is treated as sensitive — sharing is access-controlled in mature products, and some add expiring or password-protected links; the posture ranges from lightweight tools to studio-grade controls (watermarked sides, download and display restrictions, special handling of minors' data).
- **Time is binding.** Slots have capacities; tapes have deadlines; missed confirmations and late changes are normal exceptions that the operator reconciles through the schedule and messaging surfaces.
- **The decision is recorded and consequential.** A completed selection leaves a trail — who was seen, by whom, with what evaluation, and who was cast — which is the product's institutional memory across productions.
- **Minors get mediated handling.** Where children audition, a parent or guardian manages the candidacy, and display of minor-specific attributes is restricted in sharing surfaces.

## Variants

The Type is one funnel realized under different market conditions:

- **Film/TV studio casting** — agent- and manager-mediated intake, breakdown-driven submissions, self-tape-heavy early rounds, curated video review for producers and studios, strong security posture; casting offices collaborate with the studio inside the same workspace.
- **Commercial casting** — shorter cycles, high volume, frequently platform-based: the same product combines published notices, submission intake, and the selection workflow.
- **Community and regional theater** — signup-form-first intake, candidate-chosen slots, conflict calendars (in some products, candidates declare unavailability that later constrains rehearsal planning), collaborative scorecards, and role offers that in some products grant access to production resources; the selection funnel is the entry to a longer production cycle.
- **Performing-arts education and arts organizations** — application-first intake with recorded media, formal rubric-based adjudication by assigned evaluators, segmented audition days (prepared pieces, skills checks, interviews), virtual audition days at institutional scale, and communication of admission outcomes.
- **Repertory and ensemble casting** — in some products, one audition round feeds multiple shows or ensembles; the funnel fans out to several selection contexts.

A variant remains a variant while the core model holds. If the product's center becomes public discovery of opportunities rather than the selection funnel, it is functioning as a Casting Platform; if it becomes the talent's own business management, it is Talent Agency Management.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Casting Platform | the discovery/matching side: published breakdowns and notices, searchable talent profiles, market-scale submission intake; audition management is the organization-side funnel around the audition and the decision. Real products often bundle both, which is why the boundary is drawn at where the defining work happens |
| Talent Agency Management | run by the talent's representative to manage roster, submissions, and bookings as a business; in audition management the representative is a participating submitter, not the operator |
| Applicant Tracking System | same funnel shape (intake → screen → evaluate → decide) but for employment: resumes and interviews instead of performance demonstrations, jobs instead of roles; entertainment-specific artifacts (breakdowns, sides, self-tapes, callbacks) and minors/union rules do not exist there |
| Event Registration Platform | shares scheduling mechanics (slots, reminders, check-in) but its terminal state is attendance; audition management's terminal state is a casting decision that fills roles |
| Candidate Assessment Platform | shares evaluation mechanics (rubrics, scorecards, multiple assessors) but serves general skills assessment rather than selecting performers for parts in a production or program |
| Production Scheduling / Call Sheet Application; Film Production Management | downstream of casting: they take over after roles are filled, managing rehearsals, shoots, crews; casting tools may connect to them but the selection funnel is not their center |

## Representative Products

- **Cast It Systems** — studio-side casting workflow for film/TV: roles, candidate lists, audition-video review, controlled sharing with producers
- **Casting Networks** — commercial casting platform combining published breakdowns and submissions with the selection workflow (self-tapes, scheduling, sessions, status tracking)
- **Cast98** — community-theater production software centered on audition sign-ups, callbacks, and role offers
- **Acceptd** — application and audition management for performing-arts education and arts organizations: applications, video auditions, scheduling, rubric adjudication

The defining core was checked across all four segments (studio film/TV, commercial platform, community theater, education) to avoid defining the Type by any single market's implementation, and against the paper-era audition process as a historical sample.

## Sources

Research date: **2026-09-06**

- Cast It Systems — https://castitsystems.com/ (home, services, clients pages); Cast It support center: https://support.castitsystems.com/en/articles/11393409 (sharing audition videos)
- Casting Networks — official support center https://support.castingnetworks.com/ , including "Casting Directors: How Do I Manage My Film & TV Casting Workflow on Casting Networks?" https://support.castingnetworks.com/en/articles/11367617
- Cast98 — https://cast98.com/ , https://cast98.com/features/audition-scheduling , https://cast98.com/features/audition-management
- Acceptd — https://getacceptd.com/ , https://getacceptd.com/audition-scheduling-software , https://getacceptd.com/auditionroom

> Sourcing limitations: the Casting Networks marketing site (www.castingnetworks.com) was not reachable (HTTP 403); its official support center was used instead. Cast It Systems' deeper workflow documentation is not fully public; claims about its internal mechanics are kept general. Acceptd's help-center articles were not fetched; its observations rest on official product pages. Precise vendor-specific figures and branded mechanics are intentionally omitted from this document.
