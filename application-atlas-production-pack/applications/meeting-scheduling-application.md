# Meeting Scheduling Application

## Overview

A **Meeting Scheduling Application** lets a host — a professional or a team — publish when they are available to meet, and lets invitees book a meeting themselves by picking a meeting kind and a specific open time from a shareable booking page. The booking becomes a meeting: a record binding host, invitee(s), and time, written to the participants' calendars and manageable afterwards.

It solves the coordination loop that otherwise happens over email — "are you free Tuesday? what about Thursday?" — by replacing it with a standing, self-service booking surface. The host configures their availability once; every subsequent booking happens without the host's involvement until the meeting is confirmed.

The boundary: this is scheduling machinery for **meetings between people** — intro calls, interviews, 1:1s, demos, office hours. It is not a service business's appointment book (no priced service catalog, no client ledger, no deposit or cancellation policies), not a group time-finding poll (the host's availability defines the options, not the participants'), and not a calendar (it publishes availability for others to book, rather than managing the host's own time).

## Users & Context

**Hosts** are the primary configuring users: professionals who give their time in meetings — founders and consultants taking intro calls, sales reps booking demos, recruiters and hiring managers running interviews, managers holding 1:1s and office hours, teachers and coaches offering sessions. A host sets up meeting kinds and availability once, then shares links that keep working.

**Invitees** are the bookers: prospects, candidates, colleagues, clients, students. They never configure anything; they arrive at a booking page, pick a meeting kind and a time, and leave their details. Most invitees use the product once per booking and need no account.

**Team administrators** (in team deployments) manage members, shared meeting kinds, routing rules, and organization-wide settings.

The context is professional meeting-making across sales, recruiting, customer success, education, and everyday workplace coordination. The surrounding infrastructure is the shared digital calendar: availability is checked against it, and booked meetings land on it.

## Core Model

### The Defining Core

```text
Host (person or team)
└── Published availability
    │   (schedules / working hours, checked against connected calendars)
    └── Meeting kinds (event types / links)
        │   (named, duration-carrying templates: location/video, description, questions)
        └── Shareable booking surface
            │   (personal page, per-kind page, embeds, one-off links)
            └── Invitee booking
                │   (invitee picks kind + open slot, leaves contact details)
                └── Meeting record
                    (host × invitee(s) × time; reschedulable/cancellable;
                     written to the participants' calendars)
```

Four properties. If any one is removed, the product is no longer recognizable as a meeting scheduler:

- **Host-published availability** — the host declares when they can meet, as reusable rules (working hours, schedules, date-specific overrides), and the system checks connected calendars so already-busy times are not offered. The host's availability — not the participants' declarations — defines the candidate times. Without it there is no booking loop, only coordination by message.
- **Meeting kinds as bookable templates** — named, duration-carrying meeting types (an "event type" or "link": a 30-minute intro call, a 60-minute interview) that shape the booking with a location or video link, a description, and optionally questions for the invitee. Duration is what makes slot computation possible. Without kinds, the product is a blank "share my calendar" page.
- **Invitee-initiated booking** — an external person selects a meeting kind and a specific open slot through a shareable surface and books it, providing their name and contact details, without the host mediating each booking. This self-service loop is the reason the Type exists.
- **The meeting as the outcome and record** — the booking persists as a meeting binding host, invitee(s), and time. It can be rescheduled or cancelled afterwards, and in mature products it is written to the participants' calendars, where the meeting actually lives.

### Standard Capabilities

Mature products commonly add the following. They make the core practical; they do not define the Type.

- **Availability controls** — buffers before/after meetings, minimum booking notice, how far in advance bookings are allowed, start-time increments, caps on meetings per day/week/month, timezone display and locking.
- **Calendar synchronization** — busy-checking across one or more connected calendars, a designated booking calendar, and write-back of booked meetings.
- **Video conferencing** — a video link (Zoom/Meet/Teams-class) attached as the default meeting location.
- **Notifications and workflows** — confirmation emails, reminders, follow-ups, and automated messages around bookings.
- **Reschedule and cancel** — by host and invitee, with the meeting record updated everywhere; no-show marking; reassignment of a booking to a different host on teams.
- **Team distribution** — round-robin links that distribute meetings across a pool of hosts by availability and fairness rules; collective links that require several hosts at once; group links where multiple invitees book the same slot; shared team meeting kinds.
- **Booking questions and prefill** — custom questions asked at booking; URL parameters that prefill answers; campaign tracking.
- **Approval mode** — bookings held as pending requests the host accepts or rejects (optional).
- **Payments** — charging for meetings or selling meeting packages (optional).
- **Routing forms** — qualifying an inbound visitor and routing them to the right host's booking (team/revenue deployments).
- **Analytics and administration** — booking statistics; organization-level member, kind, and policy management.

### One Structure, Many Implementations

The core model is conceptual. Products realize each concept differently:

```text
Concept:   Host identity            Implementations: personal link/username, calendar-suite account, team workspace member
Concept:   Availability             Implementations: weekly schedules + date overrides, calendar busy-checking, time blocks, out-of-office redirects
Concept:   Meeting kinds            Implementations: event types, scheduling links, meeting types
Concept:   Booking surface          Implementations: public booking page, embeds, browser extension, email slot insertion, in-suite booking page
Concept:   Meeting record           Implementations: bookings list inside the product + calendar events on participants' calendars
```

A reader who has only seen one implementation — say, a public booking link — should still be able to recognize a calendar suite's built-in booking page as the same Type.

## How It Works

### Host setup (once)

```text
Connect calendar(s)
→ set availability (working hours, schedules; busy times excluded automatically)
→ create meeting kinds (name, duration, location/video, questions)
→ share the booking link (email signature, website, social profile)
```

After setup the system runs without the host: availability is recomputed continuously from the schedules and the connected calendars' busy time.

### Invitee booking (every meeting)

```text
Open the host's link
→ pick a meeting kind
→ pick an open slot (shown in the invitee's timezone)
→ answer questions / leave name and contact
→ confirm
→ meeting created on the host's calendar (commonly the invitee's too)
→ confirmations and reminders sent
```

Booking is instant by default. In approval mode the request is held as pending until the host accepts it; only then is the meeting pushed to the calendar and confirmed to the invitee.

### After the booking

```text
Reschedule (host or invitee picks a new open slot; record updated everywhere)
→ or cancel (slot freed, notifications sent)
→ meeting happens
→ mark no-show (optional)
```

On teams, a booked meeting can be reassigned to another host without cancelling it.

### Team distribution

For pools of hosts, a single link serves the whole team: the system computes the union of available slots across hosts, the invitee picks a time, and the system assigns a host — by round-robin fairness rules, priority, or ownership logic. Collective links require several hosts simultaneously; routing forms qualify the invitee first and send them to the right host or kind.

## Interfaces

### Host dashboard

The host's working surface.

- meeting kinds list (create/edit kinds: duration, location, questions, limits)
- availability editor (schedules, date overrides, buffers, notice rules)
- bookings list (upcoming/past; reschedule, cancel, reassign, no-show)
- sharing controls (links, embeds, one-off links)

### Booking page (invitee-facing)

The surface invitees see.

- the host's meeting kinds (or a single kind, on a per-kind page)
- a time-slot picker showing open slots in the invitee's timezone
- the booking form (questions, name, contact)
- confirmation state (instant, or "requires confirmation")

### Embeds and extensions

The booking surface placed where invitees already are: inline or pop-up embeds on websites, browser extensions for sharing links from anywhere, slot suggestions inside emails.

### Admin console (team deployments)

Member management, shared meeting kinds, routing forms, organization policies, SSO.

## Important Rules / Behaviors

- **Availability is the access control.** An invitee can only book times the system has computed as open. Anything that removes time from the host's availability — a calendar event, a date override, an out-of-office entry, a frequency cap — removes it from every booking surface at once.
- **Busy-checking prevents double-booking.** Connected calendars are checked before slots are offered; a booked meeting is written back and immediately blocks its own slot.
- **Rules constrain the slot set, not the invitee.** Buffers, minimum notice, booking windows, and frequency limits all act by shrinking the set of offered times; the invitee never sees a rejected booking, only fewer options.
- **The calendar is the meeting's home.** The product keeps its own bookings list, but the meeting itself lives as a calendar event on the participants' calendars; rescheduling and cancellation must keep the two in sync.
- **Confirmation can be instant or gated.** Default is instant booking; approval mode introduces a pending state in which the slot may or may not be held, at the host's choice.
- **Timezones are the invitee's problem, solved by the product.** Slots display in the invitee's timezone; hosts can lock the timezone when precision matters.
- **The host's availability defines the options.** If participants must declare their own availability to find a time, the flow has left this Type (see Related Application Types).

## Variants

- **Individual link-first** — the canonical form: a professional's personal booking page and links (Calendly, SavvyCal).
- **Open-source infrastructure** — the scheduler as self-hostable infrastructure with API access, serving individuals through organizations (Cal.com).
- **Recipient-experience-first** — design centered on the invitee's booking experience: calendar overlays, preferred-time highlighting, availability expressed through time blocks (SavvyCal).
- **Revenue-team packaging** — the same scheduling core embedded in lead routing: forms and chatbots that qualify visitors and book them with the right rep; ownership-based distribution; CRM write-back (Chili Piper).
- **Platform-native** — booking pages built into a calendar/productivity suite, using suite identity and storage (Microsoft's personal booking pages with meeting types; Google Calendar's appointment schedules).
- **AI-assisted** — scheduling delegated to an assistant that negotiates times over email/chat or via API on the host's behalf.
- **Embedded meeting polls** — propose several candidate slots to a group and let members vote; a bridge feature toward group time-finding, present in some scheduling products.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Appointment Scheduling Application | closest sibling; shared booking-link machinery | appointment scheduling models a service business's bookable offerings — priced service catalog, persistent client records, appointment policies (deposits, cancellation windows), operator-side appointment management; meeting scheduling models meetings between people, with the meeting landing on calendars and no client ledger |
| Group Availability Scheduling Application | sibling | group availability derives the time *from* participants' declared availability; meeting scheduling offers the *host's* published availability for the invitee to pick from |
| Calendar Application | adjacent; shares the calendar infrastructure | a calendar manages the user's own time and events, including propose-and-accept invites; meeting scheduling publishes availability for external self-booking. Calendar sync is the bridge, not the boundary |
| Interview Scheduling Platform | use-case-specific relative | adds hiring-anchored persistent interview records, interviewer-pool reconciliation, and ATS integration; a generic meeting scheduler merely hosts "interview" as a meeting kind |
| Event Registration Platform | adjacent | event registration sells attendance at discrete dated happenings with attendee rosters; meeting scheduling books a host's time. Group meeting kinds sit in the overlap |
| AI Meeting Assistant / Meeting Productivity | downstream | scheduling ends where the meeting begins; notes, recaps, and action items belong to the meeting-productivity Types |
| Sales Engagement / Lead-routing platforms | packaging overlap | revenue-team schedulers embed meeting booking inside lead distribution; when routing, not booking, is the center of gravity, the product belongs to the sales-side Types |

The boundary with Appointment Scheduling is the most important one, because the two Types share the entire booking-link machinery and leading products deliberately straddle. The working test: remove the service-business semantics (priced catalog, client records, appointment policies) and what remains is meeting scheduling; add them and the same machinery becomes appointment scheduling. Vendors themselves mark the seam — one suite ships a personal booking page built on "meeting types" alongside a separate business booking product built on "services and staff".

## Representative Products

- **Calendly** — the market-defining link-first scheduler; individuals through enterprise; meeting kinds, availability controls, team distribution, routing forms, and an adjacent meeting-lifecycle product family.
- **Cal.com** — open-source scheduling infrastructure; deep event-type and team mechanics (round-robin with fairness rules, collective and group links), API/MCP access, self-hosting.
- **SavvyCal** — recipient-experience-first scheduler; calendar overlay, preferred slots, time blocks; collective/round-robin/group team modes.
- **Chili Piper (ChiliCal)** — revenue-team meeting scheduling embedded in lead routing and CRM machinery.
- **Microsoft Bookings (Personal Bookings)** — platform-native booking pages built on meeting types inside Microsoft 365; used to check that the core holds outside the link-vendor pattern.

## Sources

Research date: **2026-09-08**

- Calendly — Help Center (quick-answer articles on calendar connections, availability fine-tuning, buffers, meeting limits, embeds): https://help.calendly.com/hc/en-us ; product pages: https://calendly.com/features , https://calendly.com/scheduling
- Cal.com — Help Desk (What are Links; Create your first event type; Round Robin Scheduling; How to require confirmation; Edit Availability; full article index): https://cal.com/help/llms.txt and articles thereunder
- SavvyCal — product page: https://savvycal.com/ ; Knowledge Base (Configuring link availability; Scheduling group meetings with polls; Scheduling Links category): https://docs.savvycal.com/
- Chili Piper — Help Center (ChiliCal, Concierge, Web Experiences, Distro, Handoff sections): https://help.chilipiper.com/
- Microsoft Bookings overview (Personal Bookings / Shared Bookings) — https://learn.microsoft.com/en-us/microsoft-365/bookings/bookings-overview (fetched 2026-09-06 in the paired Appointment Scheduling research)

> Sourcing limitations: Google Calendar appointment schedules documentation was unreachable this pass (repeated timeouts), so the platform-native pole is evidenced by the Microsoft sample and described structurally otherwise. Calendly's help-center category listings and Chili Piper's operational details were only partially reachable; claims for those products are kept at structure level. Precise numeric limits, plan gating, and default values are intentionally not stated; they are recorded only where directly observed, in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the sibling-boundary analysis (including the appointment-vs-meeting joint review) are recorded in the paired Research Notes.
