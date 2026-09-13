# Shared Team Calendar

## Overview

A **Shared Team Calendar** is a calendar maintained as the **shared schedule of record for a defined group of people** — a team, department, organization, or household. Instead of one person planning private time, the calendar holds the events of common concern to the group: meetings, deadlines, releases, training days, holidays, vacations, shifts of note. Every member consults the same schedule, and members who are granted permission add to and change it; who can see it and who can edit it is governed by an owner or administrator.

The defining structure is small:

```text
Defined group of people (team / organization / household)
└── One shared schedule of record
    └── Persistent, time-anchored events of common concern
        └── Controlled multi-person access
            (who may view — who may add and change)
```

Remove the group as the calendar's audience and it is an ordinary personal calendar. Remove the shared schedule and nothing calendrical remains. Remove the access control and it collapses into either a personal calendar (one consumer) or an anonymous events feed (no group).

The shared team calendar is one member of the calendar family: the same calendar structure found in any calendar application, with its sharing and permission machinery pointed at a group of people rather than a private self. Its sibling variant, the resource calendar, points the same machinery at a bookable thing — a room, a desk, a vehicle — consumed as a free/busy record. Some vendors sell the shared calendar as a standalone product; in calendar suites it arrives as per-person sharing permissions or as the calendar that belongs to a group. Both forms keep the same underlying object: one schedule the whole group reads from and, within their rights, writes to.

## Users & Context

The population is layered, like most shared settings:

**Administrator / owner** — the person (or team) who holds the calendar:

- creates the calendar and its structure (one schedule, or several named calendars within it)
- decides who may see it and at what level: read-only, able to add, able to edit, able to manage
- adds and removes members, sometimes in groups, and revokes access when people leave
- keeps the calendar trustworthy: resolves conflicting entries, corrects mistakes, retires stale calendars

**Editors / contributors** — members who maintain the schedule:

- add events the group needs to know about, change them as plans move, delete or correct errors
- may be limited to editing only what they created, depending on how the calendar is governed

**Members / viewers** — everyone the schedule is for:

- read the shared calendar as their single source of truth for what the group is doing
- consume it where they work: in the product itself, in their own calendar app through a subscription, on a web page, on a phone
- some can add entries (a request, a signup) without being able to alter anyone else's

**Outsiders (optional)** — partners, customers, or the public, who may be given a read-only view of the schedule when the group wants to publish it.

The work context is any group whose plans are interdependent enough that private calendars stop being enough: operations teams running field schedules, staff coordinating shifts and cover, schools publishing term dates, marketing teams tracking campaign milestones, families keeping everyone's activities in one place. The problem being solved is shared visibility with controlled change: everyone sees the same truth, and not everyone can rewrite it.

## Core Model

### The Defining Core

Three structures, held together:

**The group as the calendar's audience.** The calendar exists for a bounded, identifiable set of people. Membership is explicit — people are added, invited, or granted access as members of a team or group — and the events on the calendar are the group's shared life rather than one person's plans. This is what separates a shared team calendar from a personal calendar that happens to have entries about work.

**One shared schedule of record.** All members read from the same event store. There are not several private calendars reconciled by invitations; there is one schedule, presented on the familiar day/week/month grid, that the group treats as authoritative for what is happening and when. Events are time-anchored records — a title, a start and end, commonly a location, notes, attachments, and a repeating rule — exactly as in any calendar, but their audience is the group.

**Controlled multi-person access.** More than one person consumes the calendar, and participation is tiered. At minimum the calendar distinguishes those who may view it from those who may change it. Whoever creates or owns the calendar governs these grants: they admit members, set each member's level, and can revoke. In deep implementations the tiers multiply — add-only, edit-own-events-only, view-without-details — but the load-bearing minimum is the view/change distinction under an administrator's control.

### Standard Capabilities of Mature Implementations

Around that core, mature shared calendars commonly add most of the following. They make the calendar practical for real groups but do not define it:

- **Member management** — adding and removing people individually or in groups, with the administrator's rights distinct from everyone else's.
- **Multiple named calendars within the shared space** — color-coded event containers (by project, team, location, category), each potentially with its own visibility or permission setting.
- **Read-only distribution** — the schedule pushed outward as subscription feeds into members' own calendar apps, published to a web address, or embedded on a site, always as a read-only copy of the record.
- **Change visibility** — notifications when the schedule changes, digest or agenda emails summarizing what is coming, so members do not have to re-read the grid to notice an update.
- **Richer event content for coordination** — comments on events, signups or RSVPs, file attachments, custom fields, and standalone shareable pages for single events.
- **Standard calendar machinery** — recurring events, reminders and alerts, time-zone handling, day/week/month (and larger) views, search — inherited intact from the calendar type.
- **Cross-device access** — web, mobile, and desktop surfaces all reading the same shared record.

### One Structure, Many Implementations

The model is written in conceptual terms; products realize each piece differently:

```text
Concept:   How members get in
Forms:     the administrator adds each user's account;
           members are invited and accept;
           access rides on a directory group they already belong to;
           a shareable link opens the calendar without any login

Concept:   Who may do what
Forms:     a simple view-only / edit choice;
           a ladder of levels (view, view-without-details, add-only,
           edit-own-events, full edit, administer);
           delegation, where a trusted person manages the
           calendar on the owner's behalf

Concept:   Where the calendar lives
Forms:     a standalone shared-calendar product;
           a calendar shared from one person's mailbox with
           per-person permissions;
           the calendar that belongs to a group itself;
           a platform-native calendar shared with family or coworkers
```

A reader who has only seen one form — say, a work calendar shared with colleagues by permission — should be able to recognize the others from the model: the no-login link a school publishes for term dates and the family calendar on everyone's phone are the same structure, wearing different surfaces.

## How It Works

### Stand the calendar up

```text
Owner creates the calendar
→ structures it (one calendar, or named sub-calendars with colors)
→ decides the access policy (who may view / add / edit / manage)
→ adds members — by account, invitation, group, or link
→ the calendar exists as a shared record from that moment
```

This is a one-time act per calendar, repeated as the organization grows; everything that follows inherits the access policy.

### Keep the schedule current

```text
A contributor notices a change in the group's plans
→ adds an event (title, time, location, details, repeat rule)
   or edits an existing one — as far as their permission allows
→ the change lands on the one shared record immediately
→ members who enabled notifications learn of the update
→ everyone reading the calendar — app, feed, embedded page —
   sees the same corrected schedule
```

The interaction loop of this Type is exactly this maintenance cycle: the group's plans change, a permitted member records the change on the shared record, and the record radiates to every consumer. Authorship matters in mature products — some limit a member to editing only what they created, so contributors can add without being able to rewrite colleagues' entries.

### Consume it where you work

```text
Member opens the calendar in the product, or
subscribes to a read-only feed from their own calendar app, or
visits the published/embedded page
→ reads the same shared record from any of these surfaces
→ optionally sets reminders, filters, or personal display choices
   that affect only their own view
```

Consumption is read-mostly for most members. The group-wide record changes only through the permission gate; personal overlays (colors, reminders, hidden calendars) stay private to each viewer.

### Bring someone in — or take access away

```text
Administrator grants access (adds account / sends invite / issues link)
→ member joins at the assigned level
…
Administrator revokes access when the person leaves
→ the member loses the calendar; everyone else is unaffected
```

Access is administered continuously, not just at setup: people join, leave, and change roles, and the calendar's owner adjusts grants accordingly. Link-based access is the deliberate exception — anyone holding the link gets in — and products that offer it frame it for public or low-sensitivity schedules, with the administrator choosing the permission the link carries.

## Interfaces

The surfaces below appear across the researched products in conceptual form; exact layouts and names vary.

### The shared calendar grid

The schedule itself — the primary surface.

- typical information: event blocks across day/week/month frames, color-coded by sub-calendar or category, with today marked and filters for which calendars are shown
- primary actions: read the group's plans, add an event, open an event's details, edit or delete as permitted

### Event detail

The record of a single occurrence.

- typical information: title, time (with recurrence), location, notes, attachments, the creating author where tracked, comments or signups where offered
- primary actions: edit or delete as permitted, comment or sign up, share the event as a standalone page

### Sharing / access management

Where the group and its rights live.

- typical information: members and their permission levels, groups of members, access links with their own levels, feeds the calendar publishes
- primary actions: add or remove members, set or change permission levels, create groups, issue or revoke links, reset feeds

### Subscription / publish surfaces

The read-only outbound faces of the same record.

- typical information: a feed URL to add to another calendar app, an embeddable web view, a published calendar page
- primary actions: copy the feed address, configure the embed, view the published schedule

### Personal calendar app (as consumer)

The member's own calendar, which ingests the shared record.

- typical information: the shared calendar appearing alongside personal calendars, read-only
- primary actions: show/hide it, set alerts, read the group's plans next to one's own

## Important Rules / Behaviors

- **One record, many readers.** Every member consumes the same schedule; what differs by member is only rights and personal display choices. A change made through any surface appears to all — there is no per-member copy of the group's schedule to fall out of sync.
- **Rights gate every write.** Viewing is the base level; every further act — adding, editing, deleting, managing members — exists only where the administrator granted it. In mature implementations the tiers can be fine-grained, including "add but never modify others' events" and "view the schedule but not the details".
- **The administrator stands outside the rules.** Whoever holds the calendar can always do what members cannot: change grants, restructure calendars, fix any entry. The tier system binds members, not the owner.
- **Outbound copies are read-only.** Subscription feeds, published pages, and embedded views are consumption surfaces. The authority stays with the shared record; the copies reflect it, typically refreshed periodically rather than instantly.
- **Access is revocable per person.** Membership changes do not require re-sharing the calendar with everyone; a departed member's access can be cut without touching other members'. Link-based access trades this precision for convenience — the link, once loose, reaches anyone who holds it, and the control it carries is coarser by design.
- **Group plans, not private plans.** What lands on the shared calendar is understood to be the group's concern. Private entries stay on personal calendars; where a shared calendar is shared *from* someone's mailbox, that person's other content remains theirs — sharing the calendar shares the schedule, not the person.

## Variants

- **Dedicated shared-calendar products** — standalone tools whose entire premise is the group's schedule, commonly web-based, with deep permission ladders, sub-calendars, feeds, and embedding; used by operations, schools, sports, nonprofits.
- **Suite-native shared calendars** — sharing realized inside a calendar/mail service: a calendar shared from a mailbox with per-person permissions, a shared mailbox's calendar managed by admins, or delegates managing a calendar on an owner's behalf.
- **Group-container calendars** — the calendar that belongs to a group object itself (a team or group with members), where adding someone to the group grants the calendar; common in collaboration suites.
- **Platform-native sharing** — the device platform's calendar shared with family or coworkers, with edit/view-only choices and read-only publishing to other subscribers.
- **Mobile-first consumer group calendars** — app-centered calendars for families, classes, and hobby groups, with invitation-based membership and communication around events as the headline.
- **Published/public team calendars** — the group's schedule opened to outsiders through links, embeds, and feeds; the audience widens but the record and its administrators stay the same.
- **Household pole** — the same structure pointed at a family or household rather than a work team; a family-shared calendar alone sits here, while a full household product (with lists, meals, chores around the calendar) is the separate Family Organizer type.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Calendar Application | the parent structure: a calendar whose audience is one person planning private time; the shared team calendar points the same structure at a defined group, making sharing and permissions load-bearing |
| Resource Calendar | sibling variant: the calendar owned by a bookable thing (room, desk, vehicle), holding reservations and consumed as a free/busy availability record; the shared team calendar serves a group's people and their events of common concern |
| Meeting Scheduling Application | negotiates a time across people (availability collection, polls, booking links); its outcome may land on the shared calendar, but the persistent group record, not the negotiation, is this Type's center |
| Team Messaging Application | teams often gather in a messaging product that embeds a calendar surface; there the conversation is the object and the schedule a feature — when the shared schedule of record becomes primary, it is this Type |
| Family Organizer | a family-shared calendar is the single-layer neighbor; the organizer adds the household circle and the items layer (lists, meals, chores) around it |
| Employee Scheduling Platform | schedules people as labor into shifts under coverage, qualification, and wage rules; a shift plan may be published to a team calendar, but the labor-record machinery is not here |
| Project Management Application | task-derived timelines and roadmaps with completion semantics; deadline events may appear on the shared calendar, but tasks and boards are a different object world |
| Event Management Platform | produces events for audiences (registration, ticketing, agendas); publishing a group's schedule is distribution of the record, not event production |
| Appointment Scheduling Application | customer-facing booking of a provider's time slots; the shared team calendar coordinates insiders, not client bookings |

The most consequential boundary is with the Calendar Application itself: same grid, same events, same machinery — the difference is who the calendar is *for*. The second boundary to hold is with the resource calendar: people's shared plans versus a thing's claimed availability, two directions the calendar family's sharing machinery can be pointed.

## Representative Products

- **Teamup Calendar** — a dedicated shared-calendar product: one shared calendar with named sub-calendars, administrator-managed members and links, fine-grained permission levels, read-only feeds and embedding; used across operations, education, sports, and nonprofits
- **TimeTree** — a mobile-first shared calendar organized around groups: create a calendar, invite the group, keep several shared calendars side by side with communication around events
- **Microsoft Outlook / Microsoft 365** — the suite-native form: calendars shared from a mailbox with per-person view/edit/delegate permissions, admin-managed shared mailboxes, and the group calendar that belongs to a Microsoft 365 group
- **Apple Calendar** — the platform-native form: iCloud calendars shared with edit or view-only access, plus read-only publishing that others subscribe to (named as a market anchor from earlier research; details carried from the calendar research pass)
- **Google Calendar** — the second major suite ecosystem's shared-calendar layer (named here as a market anchor; its official documentation was not reachable during research, and no product-specific claims are made about it)

Together these span the dedicated and suite-native realizations, the work-team and consumer-group audiences, and the account-based and link-based access models.

## Sources

Research date: **2026-09-08**

- Teamup — product site ("Customizable shared calendar for business") — https://www.teamup.com/
- Teamup — Access Permission Levels (Knowledge Base) — https://calendar.teamup.com/kb/what-are-access-permissions/
- Teamup — User Account Access vs Calendar Links (Knowledge Base) — https://calendar.teamup.com/kb/how-to-choose-between-account-access-or-calendar-links/
- Teamup — Sync with iCalendar Feeds (Knowledge Base) — https://calendar.teamup.com/kb/what-are-icalendar-feeds
- Microsoft — About shared mailboxes, shared folders, and shared calendars in Outlook — https://support.microsoft.com/en-us/outlook/sharing/about-shared-mailboxes-shared-folders-and-shared-calendars-in-outlook
- Microsoft — Microsoft 365 Groups and Microsoft Teams (Microsoft Learn) — https://learn.microsoft.com/en-us/microsoftteams/office-365-groups
- Microsoft — Outlook help & learning hub (Sharing & delegate topic structure) — https://support.microsoft.com/en-us/outlook/
- TimeTree — product site ("An app for easy calendar sharing and communication") — https://timetreeapp.com/

> Sourcing limitations: Google Calendar's official documentation was not reachable from the research environment during this pass (the same limitation was recorded by the two earlier calendar-family research passes); Google is named as a market anchor only, with no product-specific claims. TimeTree's help center was likewise unreachable; its evidence is limited to official product pages, and claims about it are kept at capability level. Evidence for Apple Calendar's sharing behavior is carried from the earlier calendar research pass rather than re-fetched. Precise vendor details (permission-level counts and names, time windows, plan restrictions, pricing) are intentionally not stated in this document; they are recorded in the paired Research Notes.

Detailed product-by-product observations, the cross-product comparison, and the boundary analysis against the calendar, resource-calendar, and scheduling types are recorded in the paired Research Notes.
