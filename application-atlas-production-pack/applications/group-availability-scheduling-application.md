# Group Availability Scheduling Application

## Overview

A **Group Availability Scheduling Application** finds a time that works for a group of people. One person creates a shared poll for a single occasion — a meeting, event, or gathering — proposes a set of candidate times, and everyone invited declares which options they can make. The application collects those declarations into one aggregated availability view and carries the group to a chosen time.

The defining structure is small:

```text
Occasion that needs a time
└── Time-finding poll (shared object: context + candidate time options)
    └── Participant-declared availability (each person answers for themselves)
        └── Aggregated availability comparison (who can make which option)
            └── One chosen time (announced to the group; poll ends)
```

What the poll produces is a **chosen time**, not a managed booking. There is no provider selling time, no service catalog, and no persistent appointment record with a lifecycle — the appointment-like machinery belongs to the sibling Appointment Scheduling type, and organizer-imposed times with accept/decline responses belong to Meeting Scheduling. Here, the time is *derived from* what participants say works for them.

## Users & Context

**The organizer (initiator)** — the person responsible for getting the occasion scheduled. They create the poll, propose the options, distribute it, chase stragglers, and make (or ratify) the final choice. Organizers are typically peers with no authority over the participants' calendars: a team lead polling a project group, a club officer polling members, a volunteer coordinator polling respondents across organizations, a friend group planning a reunion.

**The participants** — everyone whose availability matters. Their entire job is to answer one question per option: "can you make this?" They are frequently outside any shared organization — some have no account in any related system, some are external partners — which is why participation must work from a bare link.

Typical triggering situations:

- a meeting spanning multiple teams or organizations, where nobody can see everyone else's calendar
- groups too large or too heterogeneous for one person to reconcile schedules by email
- occasions with genuinely flexible timing (social events, community activities, recurring group sessions)
- cross-company collaboration where no shared scheduling infrastructure exists

The work environment is conversation-heavy: polls are most often distributed through chat, email, and messaging apps, and participation takes under a minute on a phone or any browser.

## Core Model

### The Defining Core

**The time-finding poll** is the center of the application's world. One poll exists for one occasion that needs a time. It carries the occasion's context — title, and usually a location, description, or video-conference link — plus the candidate time options. It is a shared object: the organizer authors it, participants answer it, and everyone sees the aggregate.

**Candidate time options** are the proposed date-times (or whole-day options) the group answers against. They are set by the organizer when creating the poll — picked on a calendar grid or drawn as slots — and some products let participants add options. Two interface styles realize the same concept:

- **option lists** — a handful of discrete proposed slots, each voted on
- **availability grids** — a range of dates × times the organizer brackets, where each participant marks the cells they can attend

**Participant-declared availability** is the poll's raw data. Each participant answers for themselves which options work. The classic realization is a three-state vote per option — yes, "if need be" (workable but not preferred), no — but plain yes/no voting and grid-cell marking satisfy the same concept. Crucially, the *participants* are the source of the availability information: no participant owns the time, and no pre-published bookable schedule defines it.

**The aggregated availability comparison** is the application's central computed artifact. As responses arrive, the poll shows, for each option, who can attend, who cannot, who is indifferent, and (in grid style) where everyone's availability overlaps. This shared view is what replaces the email thread — the whole point of the type is that the group's availability becomes visible in one place.

**The chosen time** is the outcome. Once responses are in, the group — usually steered by the organizer, sometimes by simple majority visibility — converges on one final option. Mature products make this explicit: the organizer marks one option as final, and the application announces it to everyone and commonly closes the poll. The chosen time is the end of the poll's story; what happens afterwards (calendar entries, the actual meeting) lives outside this type.

### Standard Capabilities Around the Core

Mature products commonly add, without these being part of the definition:

- **link-based distribution** — a shareable URL anyone can open; email invitations with per-invitee tracking (sent / opened / responded) as an alternative
- **accountless participation** — participants identify themselves with a typed name and optionally an email; accounts are never required to respond
- **editable responses** — participants can change their votes until the poll closes; email-confirmed respondents can edit from any device
- **response pressure** — deadlines that stop responses after a date, and automatic reminders to people who have not voted
- **timezone handling** — options displayed in each participant's own timezone, with a lock option when everyone should see the same clock times
- **per-option capacity limits** — capping how many participants may select the same slot, so a venue- or group-sized option cannot be overrun
- **visibility controls** — hidden participant lists, results withheld until the organizer reveals them, fully anonymous responses
- **outcome distribution** — a confirmation announcement to all participants; calendar invitations sent when a calendar is connected
- **organizer tooling** — a dashboard of the organizer's polls, duplication for recurring occasions, results export
- **video-conference link attachment** on the occasion context

### One Structure, Many Implementations

```text
Concept:  Candidate time options
Realized as:  discrete voted options, marked availability grids, whole-day options

Concept:  Participant-declared availability
Realized as:  yes / if-need-be / no ladders, plain votes, grid-cell marking, anonymous modes

Concept:  Participant identity
Realized as:  self-declared name, name + email with edit links, platform accounts (optional), anonymity

Concept:  The chosen time
Realized as:  announcement email, calendar invitations, a highlighted final option on the poll, or
              simply the group reading the overlap view
```

A reader who has only seen a modern SaaS poll should still recognize an account-less availability grid or a calendar-suite scheduling poll as the same type: the poll, the declarations, the aggregate, and the chosen time are all present.

## How It Works

### Create the poll

```text
Describe the occasion (title, location, description, optional video link)
→ propose candidate times (pick slots on a calendar, or bracket a date-time grid)
→ set response rules if wanted (deadline, capacity per slot, visibility)
→ create the poll
```

The organizer's own calendar may be consulted while proposing — some products overlay busy times or hint at conflicts — but the organizer's availability is input for *choosing what to propose*, not a constraint the application enforces.

### Distribute and collect

```text
Share the poll link (chat / email / embedded) — or invite by email
→ participants open the link: occasion context on top, options below
→ each participant marks availability per option (yes / if need be / no, or grid cells)
→ submit with a name (+ optional email); no account needed
→ responses appear immediately in the aggregate view
```

The organizer watches responses accumulate, sees who has not responded (especially with email invitations), and can nudge with automatic or manual reminders until the deadline.

### Converge and finalize

```text
Read the aggregate: counts and names per option (or the group's overlap)
→ choose one final option
→ mark it final / "book" it
→ the application announces the choice to every participant
   (announcement email always; calendar invitations when connected)
→ the poll closes to further responses
```

In the most minimal realizations there is no explicit finalize button: the group simply reads the intersection and the organizer communicates the result by ordinary means. In suite-embedded realizations, the confirmation step is tied into the surrounding calendar. Either way, the poll's own record ends at the chosen time — there is no appointment object to reschedule, track attendance against, or complete.

### Core vs Common vs Optional

**Defining core** — without these, it is not a group availability scheduler:

- a shared poll for one occasion that needs a time
- candidate time options
- participant-declared availability (self-answered, no owner of the time)
- aggregated availability comparison
- convergence on one chosen time as the outcome

**Standard capabilities** — present in most mature products:

- link distribution and accountless participation
- editable responses
- reminders and response deadlines
- per-participant timezone display
- outcome announcements and calendar-invite distribution
- organizer dashboard, duplication, export
- visibility controls and capacity limits

**Optional / variant** — depends on product, market, and deployment:

- availability-grid interfaces (vs option lists)
- embedding inside calendar/scheduling suites
- self-hosting, SSO, team spaces, white-labeling
- participant-added options, comments, per-poll notification subscriptions
- API access

## Interfaces

### Poll editor (organizer, creation)

- Purpose: define the occasion and its candidate options.
- Typical information: title, description, location, video-conference toggle, duration per option, calendar grid (week or month view) for picking slots, timezone indicator.
- Primary actions: add/edit/remove options, set duration, switch grid/list style, open settings (deadline, limits, visibility), create.

### Share dialog (organizer)

- Purpose: get the poll to the participants.
- Typical information: the poll's shareable link, email invitation fields, per-invitee response status.
- Primary actions: copy link, send email invitations, track who has responded.

### Poll page (participant)

The participant's entire experience.

- Purpose: answer the availability question.
- Typical information: occasion context (organizer, title, location, description), the option list or grid, per-option vote state, current aggregate counts, the poll's final option once chosen.
- Primary actions: toggle availability per option, submit with name/email, edit own response, optionally subscribe to updates.

### Results view (organizer, and participants where visibility allows)

- Purpose: make the group's availability comparable at a glance.
- Typical information: options as rows/columns, each participant's per-option answer, per-option totals, best-option highlighting.
- Primary actions: inspect per-person responses, mark the final option, export.

### Dashboard (organizer)

- Purpose: manage the organizer's polls over time.
- Typical information: list of polls with status (open / closed / chosen), response counts.
- Primary actions: open, edit, duplicate, delete, export.

## Important Rules / Behaviors

- **One final option.** Finalizing selects a single option; the poll does not become a multi-booking. After finalization, further responses are typically closed or frozen.
- **Editing options invalidates answers.** Changing the candidate options after votes have arrived breaks the correspondence between responses and options — responses become mismatched with the new option set. The poll's answer set is only as stable as its option set.
- **The organizer is also a participant.** The organizer's own availability is part of the aggregate (some products pre-mark the organizer as available on every option they proposed, changeable at any time).
- **Accountless by design.** Participation works from the link alone; identity is a self-declared name, optionally backed by an email that grants response-editing rights. This makes the poll's participant list conventionally identified rather than authenticated.
- **The outcome is announced, not enforced.** The application tells everyone the chosen time (and can send calendar invitations), but it does not manage attendance, rescheduling, or completion. If the time needs to move, the realizations either re-open communication or run a new poll; the original chosen time is not a managed booking object.
- **Visibility is a real control surface.** Because responses are attributed to named people in a group, products offer hiding of participant lists, deferred result reveal, and anonymity — a structural privacy control, not an afterthought.
- **Capacity can be bounded per option.** Where an option can only absorb a limited number of participants, the poll enforces a cap per slot.

## Variants

- **Option-list polls** — the classic form: a handful of proposed slots voted on individually.
- **Availability-grid polls** — a bracketed date-time range where participants mark cells; favored for large flexible windows (e.g. week-long events, conference scheduling among many people).
- **Platform-embedded scheduling polls** — the same loop inside a calendar/mail suite: candidate times proposed from attendees' free/busy, votes collected, confirmation creating the calendar event. Distributes through the suite rather than a standalone link.
- **Scheduling-suite bridge features** — booking/scheduling products that include a group-poll mode alongside their personal booking machinery; the poll inherits the suite's calendar connections.
- **Self-hosted / open-source deployments** — the same structure run inside an organization's own infrastructure, often with deeper anonymity modes, APIs, and platform-app integrations.
- **Team-wrapped polls** — shared workspaces, branding, and centralized billing for organizations that run many polls.
- **Adjacent sign-up sheets** — participants *claim* one of several slots rather than declaring availability across all of them; sold and used as a distinct tool, though superficially similar.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Meeting Scheduling Application | closest sibling | organizer authority: a time is proposed and invitees accept/decline; booking links publish the *organizer's own* availability. Here the time is derived *from* participants' declared availability. The discriminator: do participants answer "when should it be?" (this type) or "can you attend at…?" (meeting scheduling) |
| Appointment Scheduling Application | sibling, provider-side | provider-defined bookable offerings, availability machinery, client-initiated booking, persistent appointment record with lifecycle. No provider and no booking record exist here; the output is a chosen time |
| Calendar Application | underlying surface | calendars store and display personal time; this type *collects and compares* multiple people's declarations to create a new occasion. A calendar's free/busy is input to proposing options, not the poll itself |
| Polling Application / Survey Platform | structural cousin | a date poll is a poll, but generic polling answers arbitrary questions with no occasion context, no availability semantics, and no scheduling endpoint. The seam is thin — a generic poll tool can host a date poll — which is exactly why the occasion-focus and the aggregate-to-decision loop define this type |
| Interview Scheduling Platform | domain-anchored scheduling | maintains persistent, managed interview records anchored to a hiring context with interviewer-availability reconciliation; this type ends at a chosen time with no record-keeping |
| Event Registration Platform | downstream | handles attendance *after* a time (and often a venue) is fixed; registration is an allocation of attendance, not a discovery of the time |

The Meeting Scheduling boundary is the most important one, because both types answer "when do we meet?" The structural difference is where availability comes from: the organizer's published availability with invitee consent (Meeting Scheduling) versus participants declaring their own availability with the time derived from the aggregate (this type).

## Representative Products

- Doodle — the market-defining group poll product
- Rallly — open-source-rooted standalone scheduling poll
- Nextcloud Polls — self-hosted platform-app realization
- When2meet — minimalist account-less availability grid

Platform suites (calendar-embedded scheduling polls) and scheduling suites with group-poll modes realize the same structure in embedded form.

## Sources

Research date: **2026-09-07**

- Doodle — product pages https://doodle.com/en/ , https://doodle.com/en/product/polls/ ; Help Center https://help.doodle.com/en/ — collections "Group Poll" and "Participation", incl. "Introduction to Group Poll", "How do I create a group poll?", "How do I select the final option for my group poll?", "How do I participate in a group poll?"
- Rallly — official documentation https://support.rallly.co/ ("Create a poll", "Invite participants", "Schedule", "Participant Guide", "Introduction")
- Nextcloud Polls — official project README https://github.com/nextcloud/polls
- When2meet — live application surface https://www.when2meet.com/

> Sourcing limitation: the platform-native realization (a major calendar suite's scheduling poll) and one scheduling suite's group-poll mode could not be directly fetched from the research environment (vendor support search unreachable; help-center migration). They are described only structurally, without vendor-specific feature claims, and single-product operational details (numeric limits, plan gating, exact option mechanics) are intentionally not stated in this document. Such details remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the abstraction levels are recorded in the paired Research Notes.
