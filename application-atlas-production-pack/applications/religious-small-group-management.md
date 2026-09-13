# Religious Small-group Management

## Overview

A **Religious Small-group Management** application is a congregation's small-group ministry system: it holds each ongoing group — a life group, home group, Bible study, youth group, or care/affinity group — as a persistent record with a designated leader and a membership roster drawn from the congregation's own people records, connects people to groups through a find-and-join front door, runs each group's ongoing life (joining, meetings, attendance, communication) largely through self-serving lay leaders, and reports the group picture back to staff so the congregation can see who is connected and who is drifting.

The defining core is small:

```text
The congregation's people records  (the registry substrate)
└── Group  (the persistent community of record)
    ├── Leader(s) + membership roster  → roles, join dates
    ├── Join rules  → open / request-to-join / closed, with limits
    ├── Group life  → meetings & attendance, communication,
    │                 group events, shared resources
    └── The group picture  → attendance trends, drop-off follow-up,
                              health reporting → written back to people
```

Everything commonly associated with modern small-group software — the public group finder, leader self-service portals, group chat, health metrics, coaching structures — is standard machinery that mature products add around this core. The system is deliberately **not** a conversation app (messaging is one capability of the group, not the center), not an event tool (a group persists across meetings and seasons; an event is a dated occurrence), and not the congregation's whole record system (it organizes known people into communities; it does not own the congregation's roster, giving, or check-in).

## Users & Context

The distinctive feature of this Type's user picture is that **the primary operators are lay volunteers**, not staff:

- **Group leaders** (members of the congregation): run their own groups — update the roster, take attendance, message members, schedule group events — usually without any administrative access to the church database. The software's job is to make this self-service easy enough that leaders actually do it.
- **Groups / discipleship / connections pastor** (church staff): owns the small-group program — shapes the group catalog, recruits and supports leaders, monitors group health, and follows up with people who are drifting or unconnected.
- **Coaches or community directors** (where the church uses a coaching structure): oversee a span of leaders and their groups, receiving the same feedback and reports the staff see for their span of care.
- **Church administrators**: configure group types, permissions, and the public finder; manage integrations with the church database.
- **Members and seekers** (they use the system without belonging to staff): browse the group directory, request to join, participate in group life, and receive group communications through the church's app or website.

The work rhythm is the **ongoing group life**: groups meet weekly or biweekly in homes, on campus, or online; attendance is captured after each meeting; leaders and staff exchange feedback continuously; and the program often runs in seasonal cycles (semester launches, group relaunches) or continuously year-round.

## Core Model

### The defining core

Three structures, held together, over the congregation's own people records. Remove any one and the product stops being this type of software.

**1. The group as a persistent community of record.** A group is a named, ongoing sub-community of the congregation — carrying a designated leader, a bounded membership roster, and how and when it typically meets — held as a durable record that is created, maintained across meetings and seasons, and eventually archived or ended rather than expiring with any single date. This is what separates a group from an event: an event happens on a date and closes; a group persists and its life is recorded over time.

**2. The congregation-people binding.** Group members and leaders resolve to identified people in the congregation's own records — held natively by the product or synchronized with an integrated church database. The group is a sub-community of a known population, not an open public graph, and the group's membership and participation attach to each person's record. A seeker who joins a group becomes a known person; a member's group involvement sits beside their giving, attendance, and event history.

**3. The administered group-life loop.** The group's ongoing life is operated and recorded over time: people join and leave under the group's join rules, its meetings happen and participation is recorded against the roster (per-meeting attendance is the dominant realization), the group communicates as a body, and the organization can see and act on all of it. Without this loop the product is just a directory of groups.

### Standard capabilities

These are the furniture of mature products — expected in the market, but not what makes the software what it is:

- **Public group finder / directory** — a searchable, filterable listing of joinable groups (by group type, life stage, day of week, location; often with a map view and pre-filtered links for the church website), with a public page per group: description, photo, meeting schedule, location, leaders, and a join or contact action. Groups can also be unlisted or private.
- **Join mechanics** — per-group join rules: open signup (join directly), request-to-join (the request routes to the leader for approval), or closed; join requests tracked as objects with pending/approved/rejected states and optional applicant messages; enrollment limits (member caps, closing dates) that automatically close a group when reached.
- **Leader self-service** — leaders operate their groups from their own accounts or even from no-login links: roster updates, attendance, messaging — without admin access to the church database.
- **Low-friction attendance capture** — after each meeting, the leader receives a reminder (email or text) whose link opens an attendance form with names pre-checked; guests can be added on the form; some products escalate reminders when a leader doesn't respond.
- **Group messaging** — group-wide announcements, a per-group chat channel, direct messages between members, and push notifications through the church app.
- **Group events** — a calendar per group with events and RSVPs, visibility-controlled (public or members-only).
- **Shared resources** — files, links, and study materials shared with the group, sometimes visible to leaders only.
- **Attendance-based follow-up** — reports of who stopped attending, visitor counts, and drop-off trends that feed staff follow-up.
- **Group health reporting** — dashboards and periodic health reports for staff and leadership: how many groups are meeting, how many people are in groups, who is new, who has left, which groups need attention.
- **Scoped permissions** — administrators see everything; leaders see only their own groups; access to the whole people database from the group workspace is gated and often discouraged.
- **Confidentiality postures** — member lists can be hidden or made anonymous to everyone but the leader and administrators (recovery, grief, and counseling groups).
- **Group types and tags** — the classification vocabulary: small groups, Bible studies, youth, women's/men's, recovery, serving teams, classes.
- **Multi-campus support** — groups and access organized by campus or location.
- **Prospect / connection tracking** — seekers tracked from signup through follow-up to connected member, with reminders so interest does not quietly lapse.

### One structure, many implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Congregation-people binding
Realized as:  groups inside the church database's own people records,
              a standalone group tool kept in sync with an external
              church database, memberships written back to person profiles

Concept:   Join rules
Realized as:  open signup, request-to-join with leader approval,
              private/hidden groups, member caps and closing dates
              that auto-close enrollment

Concept:   Group life
Realized as:  per-meeting attendance forms opened from reminder
              emails/texts, group chat channels, group event calendars
              with RSVP, shared file/link resources

Concept:   The group picture
Realized as:  attendance trend reports, "who stopped attending" lists,
              monthly health reports to leadership, engagement dashboards
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

## How It Works

The lifecycle all researched products share runs **Set up the program → Create groups → Connect people → Run group life → Oversee the picture**.

### Set up the program

```text
Define group types (small groups, Bible studies, youth, recovery…)
→ set permissions (who sees all groups, who sees only their own)
→ configure the public finder and its filters
→ connect the people database (native or integrated)
```

### Create and configure a group

```text
Create the group record
→ name, description, photo, group type, tags
→ set the meeting rhythm ("Sundays at 9:30am") and location (physical or virtual)
→ assign a leader (and, where used, a coach)
→ choose the join rule (open / request-to-join / closed) and any member or date limits
→ choose visibility (listed in the finder, unlisted, private)
```

Configuration is often reusable: mature products let staff duplicate a group — carrying its members, leaders, calendar, and settings — into a new season or cycle.

### Connect people

```text
A member or seeker opens the group finder (app or website)
→ browses/filters groups, opens a group page
→ joins directly (open) or requests to join (routed to the leader)
→ leader (or staff) approves or rejects the request
→ the person becomes a member; the membership lands on their person record
→ the leader is notified and follows up before the person's first meeting
```

Seekers who sign up but have not yet joined are tracked as prospects, with follow-up reminders to staff or leaders so interest does not quietly lapse.

### Run group life

```text
The group meets (in a home, on campus, or online)
→ the leader receives an attendance reminder
→ opens the attendance form (names pre-checked, no login needed)
→ marks who came, adds guests, often answers a short feedback question
→ the record lands on the group and on each person's profile
→ between meetings the leader messages the group, shares resources,
  and posts group events with RSVPs
```

### Oversee the picture

```text
Staff and leadership review the group picture
→ attendance trends, new joiners, people who stopped attending
→ groups that are not meeting consistently are flagged for support
→ follow-up is assigned (contact the drifting member, check on the leader)
→ periodic health reports go to leadership
→ the congregation answers its engagement question:
   "who attends on Sunday but isn't in a group?"
```

### Capability tiers

**Defining core** — without these, not this Type:

- the group as a persistent community of record (leader + roster + meeting rhythm)
- the congregation-people binding (members resolve to people records; participation attaches to persons)
- the administered group-life loop (join/leave under rules, recorded ongoing life, organizational visibility)

**Standard capabilities** — present in most modern products:

- public group finder / directory
- join mechanics (open / request-to-join / closed, with limits and approvals)
- leader self-service
- per-meeting attendance with low-friction capture
- group messaging
- group events with RSVP
- shared resources
- attendance-based follow-up and group health reporting
- scoped permissions and confidentiality postures
- group types and tags, multi-campus support
- write-back to person records
- prospect/connection tracking

**Variant / optional** — depends on church size, philosophy, and packaging:

- coaching structures (coaches over leaders, senior coaches over coaches)
- member health surveys and leader feedback questions
- leader recruiting pipelines
- attendance accountability escalation
- semester/cycle-based group programs vs continuous groups
- virtual/hybrid groups
- non-small-group uses of the same machinery (serving teams, mission trips, governance bodies, assimilation tracking)
- non-church organizations (parishes, non-profits, peer groups, coaching organizations)

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Group finder (public)

The front door for members and seekers.

- lists joinable groups with photos, meeting schedules, locations, and group types; filterable by day, life stage, category; often with a map view
- primary actions: search and filter, open a group page, request to join or contact the leader

### Group page

A group's public face.

- description, meeting schedule, location (or online link), leaders, member count where visible
- primary actions: join (directly or by request), ask a question before joining

### Leader workspace

The lay leader's operating surface — the heart of the Type.

- the leader's own groups with rosters, roles, and join dates
- primary actions: update the roster, take attendance, message the group, post group events, share resources, approve join requests

### Attendance capture

A deliberately low-friction surface, often reached from a reminder link rather than a login.

- pre-checked member names, guest additions, an optional feedback question
- primary actions: mark attendance, add a guest, submit

### Staff group administration

The staff view over the whole group population.

- group list with membership counts, join-rule and visibility settings, group types and tags
- primary actions: create/duplicate groups, configure types and permissions, manage leaders, assign coaches

### Health & reporting dashboards

The organization's oversight surface.

- attendance trends, active and lapsed groups, new joiners, people who stopped attending, prospect pipeline states
- primary actions: filter, drill into a group or person, assign follow-up, export

### Member app surface

Where members live with their groups between meetings.

- "my groups" section, group chat and announcements, group events with RSVP, shared resources
- primary actions: read and reply, RSVP, view group details

## Important Rules / Behaviors

- **Join rules gate membership.** Each group carries its own rule — open signup, request-to-join with leader approval, or closed — and enrollment limits (member caps, closing dates) that automatically close a group when reached. The same church typically runs all postures at once.
- **Membership is a person-to-group state.** Memberships carry a join date and a role (member or leader); in the deepest-documented implementation a person holds at most one active membership in a given group at a time. Promoting someone to leader can be an administrator-level action, not a leader-level one.
- **Leaders are delegated, not sovereign.** Leaders manage their own groups without administrative access to the church database; access to the whole people database from the group workspace is gated — one vendor documents it as explicitly not recommended. Staff retain visibility over everything leaders do.
- **Confidentiality shapes community.** Member lists can be hidden or anonymous (recovery, grief, counseling groups); in one documented implementation, features that would expose member identities to each other are disabled while the list is confidential. Privacy and community are in deliberate tension, and the group's posture governs it.
- **Attendance is leader-captured and engineered for compliance.** Because leaders are volunteers, products minimize friction (reminder links, pre-checked names, no login) and some escalate — repeated reminders, then notification of staff or the coach — when attendance goes unrecorded.
- **Groups are records, not throwaways.** Groups are archived or ended rather than deleted, preserving the participation trail; mature products support duplicating a group into a new season instead of starting over.
- **Participation outlives the meeting.** Group membership and attendance persist on the person's record beside giving, check-in, and event history — the substrate for the congregation's engagement questions.
- **Children are a boundary case.** Some products restrict children from member-facing accounts and group messaging entirely, routing kids through children's check-in instead; student groups commonly require leader approval so parents and leaders stay in the loop.

## Variants

- **Standalone small-group specialist** — a dedicated product beside an external church database, kept in sync with it; the group-health and coaching philosophy is deepest here (attendance metrics, health surveys, leader support loops).
- **Modular-suite standalone product** — a groups product within a modular church-software suite, sharing the suite's people database; strongest member-facing finder and group chat.
- **All-in-one suite module** — groups inside a full church management system; the deepest write-back (group membership and attendance as attributes of the person record beside giving and check-in), lighter standalone machinery.
- **Open-source module** — groups as one capability of a self-hosted church management system, often with group requirements (training, background checks) and group scheduling attached.
- **Groups as universal organizer** — in some all-in-one systems the group object carries everything: small groups, serving teams, mission trips, governance bodies, assimilation tracking; the small-group program is the dominant use, not the only one.
- **Semester-cycle vs continuous groups** — seasonal launches with group duplication into each new cycle, or groups running year-round.
- **Virtual and hybrid groups** — online meeting links alongside physical locations.
- **Confidential groups** — recovery, grief, and counseling groups with hidden or anonymous member lists.
- **Non-church organizations** — the same machinery serving parishes, non-profits, peer groups, and coaching organizations; the small-group software market itself is Protestant-evangelical-led, with Catholic and other traditions more often realizing community through faith-formation programs and general group machinery.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Church Management System / ChMS | record-core sibling | the ChMS holds people, giving, attendance, and events as its core and treats groups as one organizing unit; this Type owns the group loop in depth (finder, joining, group life, health) and exists both as a ChMS module and a standalone product. Remove the group loop → ChMS; remove the whole-congregation record core → this Type |
| Congregation Membership Management | substrate sibling | maintains the congregation's whole roster and membership status; this Type organizes known people into sub-communities and runs those communities |
| Religious Event Management | sibling with a different time shape | an event is a dated occurrence with registration options and a close; a group is a standing community that persists across meetings and seasons. Groups carry events (calendars, RSVP), but the group outlives any event. One mid-market product realizes event registration as a group — a packaging blur, not an identity |
| Religious Education Management | sibling with a different loop | classes are groups, but education runs the enrollment→class→session-attendance→milestone loop over a program term, with grades and catechists; small groups run ongoing community life without terms, grades, or milestones |
| Pastoral Care Management | sibling with a different center | groups are often the care-delivery context (meal trains, prayer requests flowing from group reports), but this Type centers community membership and group life; care management centers individual care needs. Remove the care loop → this Type; remove the group container → care management |
| Ministry Scheduling / Religious Volunteer Management | sibling with a different loop | serving teams are frequently realized as groups, but positions, rotations, and serving schedules belong to ministry scheduling; the community loop belongs here. All-in-one systems realize both on the same group machinery |
| Church Communication Platform | capability sibling | the comms platform owns the sending loop over the records; here messaging is one capability of the group record, not the product's center |
| Group Messaging Application / Community Chat Platform | adjacent (generic) | conversation-centered products have no group-of-record lifecycle, no leader role, no congregation substrate, and no attendance |
| Member Community Platform (association side) | adjacent sibling | a similar abstract shape (community registry + groups), but for associations, with no congregation people-record substrate or ministry grammar |
| Generic group tools (social/Meetup-class) | adjacent (generic) | open public graphs with no people-record binding and no organizational oversight; remove the congregation binding from this Type and that is what remains |

The most important boundary is with the **Church Management System**: this Type is best understood as the group loop that congregations run — realized most often as a module inside a ChMS, and sometimes as a standalone product beside one. The ChMS answers "who is in our congregation and how are they involved?"; the small-group system answers "who is in community, and is each group alive?"

## Representative Products

- **Planning Center Groups** — standalone groups product of a modular church-software suite; member-facing finder and group chat, join-request machinery, confidential groups, attendance and engagement reporting.
- **GroupVitals** — independent standalone small-group specialist; group health metrics, coaching structures, prospect pipeline, no-login attendance capture; syncs with external church databases.
- **Tithe.ly Groups** — groups module of an all-in-one vendor; app-first joining, group types with privacy postures, attendance written to the person record.
- **Churchteams** — mid-market all-in-one with a group-centric data model; Groupfinder embeds, monthly health reports, groups carrying teams and mission trips as well as small groups.
- **Pushpay ChMS (formerly Church Community Builder)** — enterprise engagement-suite module; groups with events, messages, needs, attendance, and RSVP inside the whole-congregation system.

These represent different philosophies and tiers: a modular-suite standalone product, an independent health-focused specialist, an all-in-one module, a group-centric mid-market system, and an enterprise suite module.

## Sources

Research date: **2026-09-09**

Official operational documentation:

- Planning Center — Groups API reference (Group, Membership, GroupApplication, Enrollment, Attendance objects), version 2023-07-10 — https://api.planningcenteronline.com/docs/apps/groups
- GroupVitals — Getting Started: Overview (knowledge base) — http://support.groupvitals.com/article/113-getting-started-overview-read-this-first

Official product pages:

- Planning Center Groups — https://planning.center/groups
- GroupVitals — https://www.groupvitals.com/ (with the group sign-ups, health, attendance, and dashboard pages)
- Tithe.ly Groups — https://get.tithe.ly/product/groups
- Churchteams Groups — https://go.churchteams.com/groups-churchteams/
- Pushpay ChMS — https://www.pushpay.com/product/chms-software/

> Sourcing limitations: the Tithe.ly help center returned HTTP 403 during this research pass (it was reachable for a sibling pass earlier the same day), so Tithe.ly evidence rests on its official product page and its operational FAQ. Pushpay's support site was unreachable (as in the sibling pass), so its group observations rest on the official product page. Rock RMS's public documentation returned 404 again and it was not sampled as a primary. Precise vendor-specific numbers, formulas, and defaults (pricing tiers, metric formulas, reminder schedules) are intentionally not asserted in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
