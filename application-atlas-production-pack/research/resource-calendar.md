# Research Notes — Resource Calendar

Research date: 2026-09-08
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what a "Resource Calendar" is as a directory leaf (§03.08 Calendar family): what the market actually ships under and around this concept, what the defining structure of a calendar owned by a bookable resource is, who creates/uses/consumes it, how a reservation flows through it, and — most importantly — where the Type's boundary sits against the two neighbors that pre-hung flags on this leaf:

1. **calendar-application pass (2026-09-06)** flagged Resource Calendar as a probable *object variant* of Calendar Application ("a calendar whose owner is a bookable resource such as a conference room, consumed through free/busy rather than personal planning") and called for joint review when this leaf is processed.
2. **enterprise-resource-scheduling-platform pass (2026-09-06)** recorded Resource Calendar as "a capability/interface *inside* that Type" (the availability surface), with the test: remove registry + governance + booking lifecycle → "you have a calendar feature, not the platform".

This pass is the resource-calendar side of that joint review. It must decide: independent Type, calendar-family variant, or capability — with evidence, not taxonomy convenience.

---

## Initial Boundary

Working hypothesis at step 1:

- **What it is:** a calendar whose subject/owner is a shared, schedulable *thing* (meeting room, desk, equipment, vehicle) rather than a person; entries on it are reservations; it is consumed as the availability record ("is it free? who has it?").
- **Who uses it:** employees booking shared resources (usually through their personal calendar or a booking portal), administrators/facilities staff who create and govern the resource calendars, delegates who manage bookings on a resource's behalf.
- **Nearest neighbors:** Calendar Application (parent structure), Shared Team Calendar (sibling §03.08 leaf, unprocessed), Enterprise Resource Scheduling Platform (§10, processed — the platform layer above), Meeting Scheduling Application, Appointment Scheduling Application, Space Management Platform, Amenity Booking Platform, Event Management Platform.
- **Likely confusion #1:** the corpus's own shorthand — office-operations/workplace-management passes used "Resource Calendar (pole)" loosely to mean *booking-only suites* (Skedda-class). If the invariant is the schedule record itself, that shorthand is label drift, not evidence of a booking-platform Type named "resource calendar".
- **Unknowns at start:** does any vendor sell a *standalone* resource-calendar product? Is conflict prevention definitional or policy? What does the request-processing layer look like across products? Is the resource's "identity" (mailbox/email) definitional or an implementation?

---

## Research Questions

1. What is the object of record — what exactly does a resource calendar contain, and what is it *for*?
2. What identity does the resource hold (mailbox? directory record? platform entry), and how do requesters address it?
3. How does a reservation get made, processed, and released? Where does automation end and human approval begin?
4. What policy machinery exists on the resource's calendar itself (windows, durations, conflicts, who-may-book)?
5. Which parts are invariant vs common vs variant across suite-native and dedicated-product realizations?
6. Where is the seam vs Calendar Application (parent), Enterprise Resource Scheduling Platform (platform layer), Meeting/Appointment Scheduling, Space Management?
7. Historical check: would older / regional / platform-native / paper-era practice still fit the definition?

---

## Representative Products

Selected for market representation + documentation quality + different product philosophies + different layers of the stack:

| Product | Form | Why sampled |
|---|---|---|
| **Microsoft 365 / Exchange room & equipment mailboxes (Outlook)** | suite-native resource calendars inside a calendar service | the term's definitional carrier; deepest Tier-1 operational docs (admin guide, FAQ, full booking-policy cmdlet reference) |
| **Google Workspace resource calendars (Google Calendar)** | suite-native, second ecosystem | market anchor; official docs unreachable (see Sources) — held anchor-only |
| **Skedda** | dedicated venue/space booking platform with rule engine | the booking-heavy pole nearest Enterprise Resource Scheduling; boundary data point |
| **Joan** | door-display overlay on existing calendar systems | the purest "resource calendar consumed at the door" realization; documents the calendar-backend dependence explicitly |
| **Robin** | workplace operations platform with resource booking | shows the platform-layer packaging around the same resource schedule |

Deliberately not sampled: open-source schedulers (Booked/phpScheduleIt — conceptual lineage only, not fetched), desk-experience vendors already sampled by the workplace passes, room-display competitors of Joan (same form), pure visitor-management vendors (different Type).

---

## Sources

**Fetched successfully this pass (Tier 1 unless noted):**

- Microsoft Learn — "Create Room and Equipment Mailboxes" (M365 admin docs): https://learn.microsoft.com/en-us/microsoft-365/admin/manage/room-and-equipment-mailboxes
- Microsoft Learn — "Room and Equipment Mailboxes FAQ": https://learn.microsoft.com/en-us/microsoft-365/admin/manage/room-equipment-mailboxes-faq
- Microsoft Learn — Set-CalendarProcessing cmdlet reference (Exchange PowerShell): https://learn.microsoft.com/en-us/powershell/module/exchange/set-calendarprocessing
- Skedda Support — "6 Quick Steps to get started with Skedda": https://support.skedda.com/en/articles/2689785-6-quick-steps-to-get-started-with-skedda
- Skedda Support — "Booking Conditions": https://support.skedda.com/en/articles/112700-booking-conditions
- Joan Help Center — "What is Joan and how does it work?": https://support.getjoan.com/knowledge/what-is-joan-and-how-does-it-work
- Joan Help Center — "Which calendar solutions does Joan support?": https://support.getjoan.com/knowledge/which-calendar-solutions-does-joan-support
- Joan Help Center — Getting started index / Room management section structure: https://support.getjoan.com/knowledge/getting-started
- Robin — product site (Tier 2, marketing): https://robinpowered.com/ (resource booking / room scheduling / Microsoft+Google integration pages)

**Unreachable (abandoned per network rules):**

- Google Workspace Admin Help (support.google.com/a/answer/1686462) — timeout ×2 this pass; the calendar-application pass recorded the same wall (timeouts ×2+/404 ×2). Google is held as a market anchor only.
- Robin Help Center (support.robinpowered.com) — transport error ×2. Robin evidence is product-page strength only.

**Carried corpus evidence (from sibling passes' documents/notes):**

- calendar-application.md — org calendars: "rooms or equipment appear as schedulable resources"; "calendars of groups or resources (rooms, equipment) can be opened alongside one's own"; Related-Types row "Resource Calendar — object variant".
- enterprise-resource-scheduling-platform.md — Related-Types row and boundary test vs Resource Calendar; standard capability "Calendar integrations — two-way synchronization with corporate calendars (Outlook/Google)" (Skedda among that pass's sources).
- space-management-platform.md — booking as "a surface over the space inventory"; temporal reservations consumed via free/busy.
- office-operations-platform.md / workplace-management-platform.md — "pure booking suite = Resource Calendar pole" shorthand (label drift, see Boundary Findings).

---

## Product Observations

### Microsoft 365 / Exchange room & equipment mailboxes (Outlook) — Tier 1

The definitional carrier of the concept. Evidence layer A (directly observed in official docs).

**Object and identity**
- Two resource kinds: **room mailboxes** (bound to a physical location: conference room, auditorium, training lab) and **equipment mailboxes** (bound to a non-location resource: "media equipment, or a moving truck"). [A]
- The resource holds a **mailbox identity**: an email alias is required "to send a meeting request to the room or equipment". Sign-in to the mailbox is recommended to be blocked; no product license is needed ("resource mailboxes" are not people). [A]
- Admin creation fields: type (room/equipment), friendly name, email, **capacity**, **location**, phone. [A]
- FAQ: "Do I need an owner in charge of booking the rooms or equipment? — No." [A]

**Booking flow**
- The user books by **adding the room or equipment to a meeting invitation "as if it were a person"** (Required field), sets title/purpose, times, recurrence, optionally Teams link. [A]
- **Scheduling Assistant** shows "a live calendar view of the room or equipment's availability" — "blue means the room or equipment is reserved, or busy. Select the white, or free, area." [A]
- Cancel = remove the room/equipment from the meeting "like you would an attendee. Removing the room or equipment frees up the room for others to reserve." [A]

**Request processing (the booking-policy layer — Set-CalendarProcessing, "effective only on resource mailboxes")**
- Automated processing modes: **AutoAccept** (Calendar Attendant + resource booking attendant; "free = accept; busy = decline", decisions sent directly to eligible organizers), **AutoUpdate** (requests held tentative until a delegate approves), **None** (processing disabled). FAQ frames the choice: "Does someone have to accept or decline every request? — No… You can decide whether to let someone automatically book or manage the room or equipment." [A]
- Approval duality: **AllBookInPolicy / BookInPolicy** (auto-approve in-policy requests from all users / listed users-groups) vs **AllRequestInPolicy / RequestOutOfPolicy / RequestInPolicy** (requests routed to **ResourceDelegates** for human approval). [A]
- Policy parameters: **BookingWindowInDays** (advance-booking window; documented default 180 days — vendor default, kept out of the final document), **MaximumDurationInMinutes** / **MinimumDurationInMinutes**, **AllowRecurringMeetings**, **AllowConflicts** (default false; **can be set true, permitting overlapping bookings by policy** — recurring-series conflict thresholds via ConflictPercentageAllowed / MaximumConflictInstances), **EnforceSchedulingHorizon** (recurring series extending past the window), **ScheduleOnlyDuringWorkHours**, **ProcessExternalMeetingMessages** (external senders rejected by default), **EnforceCapacity** (attendee count vs room capacity, Exchange Online), **BookingType** (Standard vs Reserved = cannot be reserved). [A]
- **Check-in and auto-release** (Exchange Online): EnableAutoRelease — "users need to check in to the reserved room, desk, or desk-pool"; if nobody checks in within the claim window (PostReservationMaxClaimTimeInMinutes), the space releases automatically for others. [A]
- Privacy hygiene on the resource's calendar: DeleteSubject / DeleteComments / DeleteAttachments defaults strip booking detail; the default folder permission (**AvailabilityOnly**) shows free/busy without subjects — **LimitedDetails** is required to see titles. Custom response text (AdditionalResponse) and decline reasons (OrganizerInfo) are configurable. [A]
- Non-calendar mail to the resource is deleted (DeleteNonCalendarItems); the mailbox exists for its calendar. [A]
- A newer **workspace mailbox** kind exists for desk pools (MinimumDurationInMinutes applies only to workspace mailboxes; check-in/auto-release covers "rooms, desks, and desk pools"). [A]

### Google Workspace resource calendars — NOT REACHED

- support.google.com answer pages timed out twice this pass; the calendar-application pass hit the same wall. **No Google-specific operational claims are made anywhere in this research.**
- Market-anchor status is corroborated indirectly by Tier-1/Tier-2 third-party documentation: Joan's official help lists **Google Workspace** as a supported calendar backend for room devices [A]; Robin's official site documents "Real-time Microsoft 365 and **Google Calendar** integrations" for rooms/desks [A-T2]. The existence of a room/resource-calendar layer inside Google Workspace is therefore third-party-attested; its internal mechanics are not.

### Skedda — Tier 1

A dedicated venue/space booking platform; the booking-heavy pole. Evidence layer A (help center), with the calendar-sync capability carried from the ERS pass's documented sources.

- **Venue model:** the organization sets up a "venue" containing **spaces** — named records with photos, descriptions, features, capacity, floor plans/maps. [A]
- **Access & visibility:** venue public or login-protected; *who can book* configured as anyone / only system users / only users carrying certain **user tags**; booking transparency (what details others see) configurable. [A]
- **Rule engine:** "Booking conditions… deny certain bookings. Skedda will *allow* all bookings by default unless a rule/setting denies it." Conditions customize by space, day of week, time of day, duration, holder tags: min/max durations, strict fixed blocks ("strict two-hour blocks starting only at 10 am, 12…"), day/time gating ("prevent users tagged *Members* from booking on Sundays before 2 pm"). Conditions stack with **hours of availability**, **booking windows**, and **quotas**. [A]
- **Admin override, verbatim parallel to Exchange delegates:** "Booking conditions do *not* apply to System users! They can *break your rules* and book at any time, for anyone, irrespective of your settings." [A]
- Operational layer: booking/cancellation policies, confirmation emails, color rules, invitation links, venue URL shareable publicly (demo venue exists). [A]
- Calendar synchronization with corporate calendar suites is documented by the ERS pass (Skedda among its sources) as that Type's standard capability — two-way sync with Outlook/Google so bookings appear in personal calendars and calendar events can create bookings. [carried; not re-fetched this pass]

### Joan — Tier 1

A door-display overlay whose entire product premise is the existing resource calendar. Evidence layer A (help center).

- Room booking = "**seamlessly integrating your company's existing calendar with your physical rooms**. Utilizing the Joan device, each room is equipped with an E-paper tablet **displaying its availability**. Employees can conveniently view and book rooms directly from their company's calendar." [A]
- Supported calendar backends, enumerated: **Google Workspace, Microsoft Exchange 2010/2013/2016, Microsoft Office 365, iCalendar (.ics)** — "only one calendar solution can be connected… at a time." [A]
- The help center's Room-management section is organized **by calendar backend** (Microsoft 365 / Exchange / Google / iCalendar), plus shared-environment use, buildings, interfaces. [A]
- Product family beyond rooms: desk booking (floor plans, app booking), parking & asset booking, visitor management, digital signage, analytics — the room-calendar core sits inside a widening workplace offer. [A]

### Robin — Tier 2 (product site only; help center unreachable)

- Platform modules: **Resource booking** ("Book desks, rooms, lockers, parking and more"), space management, meeting management ("Reduce conflicts, right-size meetings and handle requests"), workplace analytics, visitor management, employee experience. [A-T2]
- The calendar dependence, verbatim from the IT persona: "**Deploy once, stay perfectly in sync: Real-time Microsoft 365 and Google Calendar integrations keep schedules accurate** and enables employees to book in apps they already know" (Teams, Slack, Outlook, mobile); "Check calendar health and get proactive alerts." [A-T2]
- Room displays, wayfinding, desk booking listed as features/pages. [A-T2]
- Operational depth (booking policies, check-in semantics, sync directionality) is **not verified** — help center unreachable. Robin's claims here are kept at capability level.

---

## Cross-product Comparison

| Dimension | Exchange/Outlook (suite-native) | Skedda (booking platform) | Joan (display overlay) | Robin (workplace suite) |
|---|---|---|---|---|
| Where the record lives | the resource mailbox's calendar, inside the calendar service | the platform's venue schedule (syncs with suite calendars per ERS-pass sourcing) | the *existing* calendar backend (Google/Exchange/O365/iCal) — Joan keeps it as the record | synced with Microsoft 365 / Google calendars in real time |
| Resource identity | mailbox with email alias; capacity/location/phone attributes; sign-in blocked; unlicensed | space record with photos/capacity/features/floor plan | the room's calendar in the chosen backend | rooms/desks/lockers/parking as bookable records across synced calendars |
| How a reservation is made | invite the room "as if it were a person" in Outlook; Scheduling Assistant free/busy | book in the portal/venue URL under access rules | view availability at the door; book "directly from their company's calendar" | book "in the apps they already know" (Outlook/Teams/Slack/mobile) |
| Request processing | automated attendant (free=accept/busy=decline) or delegate approval; configurable per resource | rule engine: deny unless conditions met; conditions bypassed by system users | rides the backend's processing; device displays the outcome | "reduce conflicts… handle requests" (mechanism unverified) |
| Policy layer | booking window, min/max duration, recurrence, work hours, external senders, conflicts, capacity, check-in/auto-release | hours, booking windows, quotas, deny-conditions by space/day/time/duration/tag | backend-dependent | unverified this pass |
| Human roles | none required (attendant); delegates optional; admins configure | system users/admins exempt from rules; user tags govern booking rights | admins configure rooms/devices | workplace/IT/facilities teams run the platform |
| Consumption surfaces | personal calendar + scheduling assistant + room lists | web portal + (per ERS sourcing) calendar sync | door display + personal calendar + mobile app | portal, Outlook/Teams/Slack, room displays |
| Exclusivity | default no conflicts; **allow-conflicts exists as policy** | prevent-by-default via engine; policy-settable posture | backend's discipline | "reduce conflicts" |

**Stable commonalities across the sample (layer B):**
1. A persistent calendar/schedule **bound to a shared resource**, not a person.
2. Entries on it are **reservations** — time-bound claims made by requesters.
3. The schedule is consumed as the **availability record** (free/busy; "blue means reserved").
4. Booking happens **through or onto the resource's calendar** — by inviting it, or by surfaces that write to it.
5. A **processing layer** sits between the request and the record: automation (accept-if-free), human delegates, or rule engines — always with an admin override.
6. The resource carries **attributes** (capacity, location, features) used for discovery.
7. **Policy machinery** (windows, durations, hours, who-may-book) attaches to the resource, in every product that documents depth.

---

## Abstraction Levels

### L0 — Defining Invariant (minimal)

```text
Resource-owned schedule of record
└── Reservation entries (time-bound claims of use by requesters)
    └── Consumed as the shared availability record (free/busy)
```

1. **The calendar's subject/owner is a shared bookable resource** — a room, desk, equipment item, vehicle — not a person. Remove → Calendar Application (the subject becomes a person planning their own time) or Shared Team Calendar.
2. **Entries are reservations** — claims by requesters to use the resource over a time span, recorded on the resource's schedule. Remove → a happenings/publicity calendar (an events feed for the hall) with no claim semantics.
3. **The schedule is consumed as the availability record** — people consult it as the authority on when the resource is free or taken ("is it free? who has it?"); free/busy is the consumption mode; nobody plans a personal life on it. Remove → a personal diary or an org announcement feed; the coordination purpose collapses.

Joint-bearing tests:
- 1 alone = a spare calendar with a thing's name on it.
- 1+2 without 3 = a booking log nobody consults (the coordination function is gone).
- 1+3 without 2 = an opening-hours display; nothing is claimed.
- 2+3 without 1 = claims without a subject — that is meeting scheduling across people or appointment booking of provider time.

### L1 — Common Mature Structure (standard capabilities)

- **Booking through the personal calendar**: add the resource as an attendee; scheduling-assistant free/busy grids; room lists/finders for discovery. [A: Exchange; B: pattern visible across Robin/Joan consumption surfaces]
- **Automated request processing**: accept-if-free/decline-if-busy attendants, with response messages carrying reasons/custom text; or routing to human approvers (delegates). [A: Exchange; posture variants across sample]
- **Booking policy attached to the resource**: advance windows, min/max durations, recurrence rules, hours, who-may-book. [A: Exchange + Skedda; B]
- **Admin/delegate override**: humans who can book anything for anyone regardless of policy (Exchange ResourceDelegates + out-of-policy; Skedda System users). [B — two products, independently documented, same structure]
- **Resource attributes and organization**: capacity, location, features; buildings/floors/categories/room lists. [A: Exchange, Skedda, Joan, Robin]
- **Recurring reservations** with series semantics. [A: Exchange; B]
- **Multiple consumption surfaces**: personal calendar, web/mobile portals, door displays. [B]

### L2 — Variant / Optional Structure

- **Check-in + no-show auto-release** (Exchange Online rooms/desks/desk pools; common in booking platforms per sibling passes). [A in one product; carried B]
- **Capacity enforcement** (attendee count vs room capacity). [A: Exchange Online; variant]
- **Deny-rule engines** conditioned on tags/time/duration (Skedda). [A: one product]
- **Utilization analytics**. [A-T2: Robin; carried B from sibling passes]
- **Floor plans / kiosks / door displays / signage** as overlay surfaces. [A: Joan, Robin, Exchange Places-class]
- **Desk / parking / asset / locker extension** beyond rooms. [B: Skedda, Joan, Robin, Exchange desk pools]
- **Public/external venue booking** with shared URLs (and payments on some platforms per sibling passes). [A: Skedda]
- **Two-way sync overlays** — dedicated booking products writing reservations into suite resource calendars and reading suite meetings onto their own surfaces. [A: Joan (T1), Robin (T2); carried B via ERS pass]
- **Privacy gradations** of booking detail in free/busy views. [A: Exchange AvailabilityOnly/LimitedDetails; Skedda transparency settings]

### L3 — Vendor-specific (research notes only; excluded from the final document)

- Exchange terminology: Calendar Attendant, resource booking attendant, AutoAccept/AutoUpdate; documented defaults (BookingWindowInDays 180; MaximumDurationInMinutes 1440; ConflictPercentageAllowed 0; AutoAccept default in EAC-created mailboxes); workspace mailboxes/desk pools (Microsoft Places family); ProcessExternalMeetingMessages default; DeleteSubject/DeleteComments privacy defaults; BookingType Reserved.
- Joan: device lineup (Joan 6/6 Pro/13, e-ink), MyJoan portal, single-backend-at-a-time restriction, Visionect origin, visitor-management/signage modules.
- Skedda: plan-based condition limits, "Skedda Fred" test user, AllBooked sibling product, venue/color-rule specifics.
- Robin: module branding (Meeting Management, Space Management), AI positioning, Gartner MQ marketing claims, calendar-health alerts.

---

## Vendor-specific Findings

- The **mailbox/email form** of the resource's identity is Exchange's realization — a directory calendar resource (Google pattern, unverified) and platform records (Skedda/Joan/Robin) are other realizations. Not definitional.
- **Auto-accept** is one documented processing posture (Exchange, with delegate-approval as the documented alternative in the same product); not the Type's defining behavior.
- **Check-in/auto-release** is documented Tier-1 only in Exchange Online (rooms/desks/desk pools); elsewhere carried from sibling passes at capability level.
- **Rule-engine granularity** (per-tag deny conditions) is Skedda-specific in this sample's direct evidence; Exchange expresses equivalent intent via BookInPolicy lists and parameter policies.

---

## Rejected Findings (anti-overfit)

1. **"No double-booking" as definitional** — rejected. Exchange documents `AllowConflicts $true` as a supported policy mode where conflicting (even recurring) bookings are accepted. The invariant is the schedule-as-record; *exclusivity is a policy posture, not a law*. This also keeps the seam clean vs Enterprise Resource Scheduling Platform, whose defining behavior *is* enforcement (no silent double-booking as the platform's arbiter role).
2. **"Rooms only"** — rejected. Equipment mailboxes, "a moving truck", desks, desk pools, parking, assets, lockers appear across the sample. The invariant is "shared bookable resource".
3. **"Mailbox/email identity"** — rejected as implementation. Joan connects to iCalendar feeds and directory calendars; Skedda/Robin hold their own records. The conceptual layer is an *addressable calendar identity for the resource*.
4. **"Door displays"** — rejected as definitional. They are overlay consumption surfaces (Joan, Robin, Exchange Places-class); the record exists without them.
5. **"Auto-accept automation"** — rejected. Delegate-approval and rule-engine postures are equally documented in-sample.
6. **"Suite-native is the only form"** — rejected. Overlays and platforms keep the same record structure while adding portals, displays, and rules; some keep the suite calendar as the record (Joan, Robin), some hold their own and sync (Skedda per ERS sourcing).
7. **"Resource Calendar = booking suite"** (the corpus's own shorthand) — rejected as label drift. Booking suites are Enterprise Resource Scheduling / platform territory; the resource calendar is the schedule record they synchronize with and govern. Reconciled in Boundary Findings.

---

## Boundary Findings

1. **vs Calendar Application (§03.08 parent)** — the same calendar structure (time-anchored events on a persistent navigable schedule) with a different subject and consumption mode: the calendar's owner is a resource, entries are other people's claims, and the schedule is read as availability, not planned as personal time. The calendar-application pass's variant framing is **confirmed from this side**. Remove-test: strip the resource subject → Calendar Application; the calendar-application document itself already lists this Type as its "object variant".
2. **vs Shared Team Calendar (§03.08 sibling, unprocessed)** — both are calendar-structure variants pointed away from the private self: shared team calendar = the calendar's sharing/permission machinery aimed at an organization's *people's events of common concern*; resource calendar = the calendar aimed at a *thing being claimed*. That pass should confirm the triad framing (calendar / shared team / resource) proposed by the calendar-application pass.
3. **vs Enterprise Resource Scheduling Platform (§10, processed)** — **record vs system.** The resource calendar is the schedule/availability record and its consumption surfaces; the platform adds the resource registry at organizational scale, the booking workflow/lifecycle, governance (approvals, quotas, scoped permissions), and utilization measurement. The ERS pass's "capability inside this Type" framing is confirmed — with one refinement from Tier-1 evidence: the suite-native realization carries real policy machinery *on the resource itself* (Exchange booking windows, delegate approval, check-in/auto-release), so the seam is not "policy lives only in platforms"; it is registry-scale + lifecycle + cross-resource governance. Skedda-class rule-engine booking suites straddle: their center is the venue schedule with heavy policy automation — held as the **thin platform pole**, consistent with the ERS document's own variant list.
4. **vs Meeting Scheduling Application (§03.09)** — the resource calendar claims *the resource's* time; meeting scheduling negotiates *the people's* mutual time, with a room as an optional constraint attached to the outcome.
5. **vs Appointment Scheduling Application (§03.09)** — customer-facing booking of *provider service time* with client records; a resource calendar claims *organizational assets* on behalf of internal requesters (that pass recorded resources as optional constraints only).
6. **vs Space Management Platform (§17, processed)** — temporal claims vs the spatial inventory/allocation/moves discipline; that pass already holds booking as "a surface over the space inventory" in mature platforms.
7. **vs Amenity Booking Platform (§17, processed)** — building-amenity semantics (eligibility by lease/residency, deposits, guest limits) vs generic organizational claims; that pass flagged the seam, and this pass adds nothing contradicting it.
8. **vs Event Management Platform (§26)** — the claim on the venue/space vs the production of the event itself (registration, agenda, attendees).
9. **vs Employee Scheduling Platform (§09, processed)** — people as labor in shifts vs resources as things to be claimed.
10. **Label-drift note for the taxonomy pass** — office-operations-platform and workplace-management-platform used "Resource Calendar (pole)" to mean *booking-only suites* (Skedda/Engage-class). This pass determines those suites sit at the thin platform pole of Enterprise Resource Scheduling (or as this variant's booking-heavy realizations); the shorthand should be reconciled so no third Type is implied by the drift.

**Does the leaf stand as an independent Type?** No standalone "resource calendar" product category was found in the sample: the structure ships (a) as resource containers *inside* calendar suites and (b) as the schedule-of-record that booking products synchronize with and overlay. Per the workflow, this is recorded as a **variant of Calendar Application** — the document is still written in full (as the variant's own record, cross-referencing both neighbors), and the determination goes to STATUS.md rather than a silent directory edit.

---

## Historical / Market-Sample Check

- **Paper-era practice**: the conference-room booking book at a front desk or the equipment sign-out sheet — a schedule bound to the resource, entries as claims, consulted by whoever wants the slot. Satisfies all three L0 legs with zero software machinery. [C]
- **2007-era Exchange room mailboxes** and the long-standing suite pattern — invite-the-room, attendant/delegate processing, free/busy — fit the model without any modern additions (displays, analytics, AI). [A — the cmdlet reference documents versions back to Exchange Server 2010; the concept predates the sampled doc surface]
- **Platform-native calendars** (per the calendar-application pass's carried evidence): org calendars including rooms/equipment opened alongside personal ones — same structure. [carried]
- The definition names no email protocol, no mailbox, no cloud, no display hardware, no AI, no desk/parking extensions — all era/market machinery. Historical check **passed**.

---

## Uncertainties

1. **Google Workspace resource calendars** — official docs unreachable (timeouts ×2 this pass; same wall in the calendar-application pass). Third-party attestation exists (Joan T1 lists Google Workspace as a backend; Robin T2 documents Google Calendar integration), but no Google-internal operational detail is asserted anywhere. If a later pass fetches Google's admin help, the L1 list should be re-verified against it.
2. **Robin's operational depth** — help center unreachable (transport error ×2); booking-policy/check-in/sync-directionality semantics unverified. Robin is held at product-page (capability) strength.
3. **Skedda↔suite calendar sync specifics** — not re-fetched this pass; carried from the ERS pass's sourced capability list. Directionality (one-way vs two-way) not asserted here.
4. **Standalone-product question** — no standalone resource-calendar product was found, but absence in a 5-product sample is not proof of absence in the market; the variant determination rests on how the sampled market *ships* the structure, and is flagged for the taxonomy pass.
5. **Apple platform-native resource schedules** — carried from the calendar-application pass's corpus record ("Apple resource-schedule views"); not re-verified this pass.

---

## Final Synthesis

The Resource Calendar is the **shared bookable resource's own schedule**: a persistent calendar whose subject is a room, desk, equipment item, or vehicle rather than a person, whose entries are **reservations** — time-bound claims made by requesters through the calendar itself or through surfaces that write to it — and which is consumed as the **availability record** (free/busy) by everyone coordinating use of that resource.

The defining core is three jointly-held structures (resource-owned schedule + reservation entries + availability-as-record consumption). Everything else mature products carry — invite-as-attendee booking, scheduling assistants, automated attendants or delegate approval, booking policies, admin overrides, resource hierarchies, recurring reservations, portals, door displays, check-in/auto-release, rule engines, analytics — is standard capability or variant structure, not definition.

**Determination for the taxonomy record:** the leaf is an **object/subject variant of the Calendar Application Type** (as the calendar-application pass proposed), not an independent product category — no sampled vendor sells a standalone resource calendar; the structure ships inside calendar suites (Exchange room/equipment mailboxes Tier-1; Google resource calendars market-anchor-only) and as the schedule-of-record that booking products (Robin, Skedda, Joan) synchronize with and build surfaces upon. The **record-vs-enforcement** seam against Enterprise Resource Scheduling Platform is confirmed with Tier-1 support (Exchange documents allow-conflicts as policy; the platform Type's invariant is registry + governance + lifecycle + utilization). The corpus's "Resource Calendar pole" shorthand for booking suites is label drift to be reconciled at a taxonomy pass. No directory change made from this side.
