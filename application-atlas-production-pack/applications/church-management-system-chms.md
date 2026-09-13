# Church Management System / ChMS

## Overview

A **Church Management System (ChMS)** is a congregation's central record system: it holds identified people — organized into households or families — as its core records, attaches their participation over time (attendance, group involvement, giving history, serving) to those records, and is operated by the church's own staff and lay leaders as an administrative system of record for ministry.

The defining core is deliberately small:

```text
Congregation people records (individuals + households)
└── Participation records over time, attached to the person
    └── Church-side administration (staff/leaders govern the records;
        members are the subjects — and partial self-servers — of the records)
```

Everything else commonly associated with church software — children's check-in kiosks, giving tools, texting, church apps, volunteer scheduling, websites — is standard capability layered around that record core, not what makes the product a ChMS. A parish census register or a 1990s office membership database satisfies the core without any of the modern machinery; conversely, a product without people records is not a ChMS no matter how many church features it has.

The record core is also why the surrounding church-software market is organized the way it is: giving platforms, communication platforms, scheduling specialists, and worship planners all exist beside the ChMS, integrate with it, or ship as its modules. A ChMS can lack any one of those modules and remain a ChMS; it cannot lack the record core.

## Users & Context

The organization, not the individual, is the operator. Primary users:

- **Church staff and administrators** — maintain the people database, households, and membership records; configure groups, events, and security; run reports for leadership
- **Pastors and ministry directors** — read engagement history, assign and work follow-up, coordinate pastoral care
- **Lay leaders and group leaders** — delegated, scoped access: take their group's attendance, message their members, manage their team's roster
- **Volunteers** — narrow operational roles: run a check-in station, manage a classroom roster
- **Volunteer coordinators** — build serving rotations, track availability and confirmations

Secondary users are the **congregation members themselves**, through a member-facing portal or app: they update their own profile, view directories, sign up for events, give, view their serving schedule, and interact with their group. Members appear in the records and may edit parts of their own record, but they do not operate the system — a structural distinction from community platforms where members are the primary actors.

The work context is the church office during the week (records, follow-up, planning, reporting) and the church building on a service day (check-in stations, attendance, headcounts), with the member app running continuously in between.

## Core Model

### The Defining Core

**Person record.** The central object: an identified individual with contact details, demographic fields (name, birth date, gender, contact information are typical defaults), and an extensible set of custom fields (custom tabs and typed fields — text, date, dropdown, checkbox, file — are common). The person record is the anchor to which everything else attaches.

**Household / family.** People are grouped into households or families as first-class units. The household matters because church life is largely familial: address and contact info are often held at household level, giving and attendance can be recorded per family, and children belong to a household under their guardians.

**Participation records.** The person's history of engagement, accumulated over time and visible on the profile: attendance at services, events, and groups; membership in groups and teams; contribution history; serving history; notes. This is what distinguishes a ChMS from a static member directory — the record is a *life of involvement*, not just a listing.

**Church-side administration.** The system is governed by the organization: staff and leaders hold permissioned access, sensitive data is visibility-controlled, and members' self-service is scoped by the church. The church owns the data; members are its subjects.

### Standard Capabilities Around the Core

Mature products carry most of the following. They make the record core operational but do not define the Type:

- **Groups** — the organizing units of congregational life: small groups, Bible studies, classes, serving teams, governance bodies (elders, boards), care and recovery groups. A group has a type, a leader (or leaders), members drawn from the people records, its own attendance, and often its own communication surface. Privacy postures vary: private groups hidden from public listing and, in some products, confidential groups whose member lists are anonymous to everyone but leaders and administrators — a structure aimed at recovery, grief, and counseling contexts.
- **Contribution records** — gifts attributed to a giver and designated to a fund, recorded against the person's profile, with statements and pledge tracking. This is the *record-keeping* half of giving; the collection channels (online forms, text giving, kiosks) belong to the giving-platform Type that integrates with — or is bundled in — the ChMS.
- **Attendance machinery** — event attendance, group and class attendance, and simple headcounts, filterable by date, location, event type, and demographic.
- **Children's check-in with security machinery** — check-in stations or kiosks that print child name tags and parent security labels with matching codes; pickup verification (label match, barcode scan, or a verified list of authorized adults); room rosters with live check-in/out state; parent notification by text; room capacity limits; and, in some products, medical or allergy notes surfaced on the labels. Volunteer-run stations, parent self-check-in from a phone, and classroom clipboard views are common station modes.
- **Member lifecycle and follow-up workflows** — capture of first-time guests (connection cards, forms, check-in), welcome and follow-up sequences, multi-step workflows that track a person's progress toward goals such as membership or serving, and re-engagement of people whose attendance has lapsed. Multi-step workflow and queue structures — assignable, with steps and completions — are the common implementation.
- **Communication from the records** — email, SMS, and push notifications sent to lists or segments built from people data (a list is typically a saved, often auto-refreshing query over the records).
- **Volunteer and serving scheduling** — positions, teams, rotations, schedule requests with accept/decline, availability and blockout dates, reminders, and sometimes household-level scheduling.
- **Events, registration, and facilities** — event creation with signups and payments, plus room and resource booking with approval routing.
- **Reporting and dashboards** — engagement dashboards and reports over attendance, giving, and involvement; saved and shareable people searches.
- **Member-facing portal / app** — profile self-service, church-wide directory, event signups, giving, serving schedules, and group interaction.
- **Forms** — public-facing forms (connection cards, registrations, prayer requests) whose submissions create or update records automatically.
- **Safety machinery** — background checks for staff and volunteers, often with an integrated screening provider, completion tracking, and renewal dates; volunteer eligibility sometimes enforced as a group requirement.
- **Sensitive notes** — prayer requests, pastoral-care and counseling notes, health conditions — stored on the profile under restricted visibility.
- **Multi-campus** — campuses or locations as an organizational layer across people, events, attendance, and giving.
- **Data migration** — CSV import/export and vendor-assisted migration from competing systems; switching costs are a known market dynamic and migration assistance is a standard offer.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Congregation people records
Realized as:  person + household profiles with custom fields (modular suites),
              member database with tags (simple all-in-one),
              family census records (parish heritage systems)

Concept:   Participation records
Realized as:  activity feeds and engagement history,
              attendance analytics, giving history on the profile,
              sacramental milestones

Concept:   Follow-up workflows
Realized as:  multi-step workflows, process queues, connection requests,
              discipleship "steps" or pathways
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

## How It Works

### Record a person

```text
A guest fills a connection card / form / checks in a child
→ the submission creates or updates a person record (household linked)
→ staff review, merge duplicates, complete the profile
→ the person enters follow-up (welcome sequence, next-step workflow)
```

People enter the system through capture surfaces (forms, check-in, guest follow-up) or through migration from a previous system. Duplicate profiles are a normal hazard of congregation data; merge tooling is common.

### Record participation

```text
Sunday / event / group meeting
→ check-in at a station (child + parent labels printed; security code issued)
   or attendance taken (individually or as a headcount)
→ the attendance record lands on each person's profile
→ contributions received are entered or synced as attributed, fund-designated records
```

Participation accrues automatically as a by-product of church operations — this is the mechanism that keeps the engagement history current without staff data entry.

### Act on the records

```text
Build or open a list (saved query over people data, often auto-refreshing)
→ see who matches (first-time guests, drifting regulars, eligible volunteers)
→ assign people to a workflow / queue (steps, owners, due follow-up)
→ communicate with the list (email / SMS / push)
→ record outcomes back on the profile (notes, workflow completion)
```

This loop — query the records, act, record the outcome — is the ChMS's administrative heartbeat, and it is the same loop whether the goal is guest follow-up, pastoral care, or volunteer pipeline management.

### Run check-in safely

```text
Family arrives (or pre-checks from the parent's phone)
→ station prints child name tag + parent security label with matching code
→ child joins a room; room roster updates live
→ at pickup: match labels / scan the code / verify an authorized adult
→ child checked out; times recorded
```

The security machinery (codes, pickup authorization, restricted label content, parent texting) exists because the system is handing custody of other people's children — the check-in is a safety protocol, not just an attendance counter.

### Member self-service

```text
Member signs in to the portal / app
→ updates their own profile (scoped fields)
→ gives, signs up for events, views their serving schedule
→ interacts with their group (chat, RSVP, resources)
→ changes flow back into the same records staff work from
```

### Core vs standard vs optional

- **Defining core** — people records with households; participation history on the person; church-side permissioned administration.
- **Standard capabilities** — groups, contribution records, attendance, children's check-in security, follow-up workflows, communication from records, volunteer scheduling, events/facilities, reporting, member portal, forms, background checks, sensitive notes, custom fields, multi-campus, migration.
- **Optional / variant** — fund accounting depth, full worship/service planning, website and app builders, streaming and media libraries, learning-management modules, AI assistance, denominational compliance machinery.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### People list & profile

The primary staff surface. The list searches and filters the database; the profile shows the person's details, household, custom fields, participation history (attendance, giving, groups, serving), and notes. Primary actions: create/edit/merge profiles, edit household, add notes, start a workflow, add to a group or list.

### Groups

The organizing-unit surface: group types, group finder (public or internal), a group's roster, leaders, attendance, events, and communication. Primary actions: create groups, add members, take attendance, message members, delegate leader access.

### Check-in station

A kiosk-style surface used on service days: household lookup or self-scan, select children and locations, print labels, live room rosters, checkout verification. Primary actions: check in/out, print labels, text a parent, view room roster.

### Attendance & reports / dashboards

Engagement surfaces over the accumulated records: attendance trends, giving summaries, group health, saved lists. Primary actions: filter, build/save lists and reports, export.

### Workflows / queues

The follow-up surface: workflow definitions with steps, assigned people, statuses, and completion tracking. Primary actions: create workflows, assign, advance steps, record outcomes.

### Member portal / app

The congregation-facing surface: profile, directory, giving, event signups, serving schedule, group interaction. Primary actions: self-edit scoped fields, sign up, give, RSVP.

### Forms builder

Surface for creating public capture forms whose submissions write back into records. Primary actions: build form, publish, map submissions to profiles.

### Administration & permissions

Configuration of users, roles, and visibility — which staff see which products, which leaders see which groups, which fields are restricted. In some products this granularity reaches the field level: sensitive custom fields can be hidden from staff who lack explicit access, and masked even in lists and notifications.

## Important Rules / Behaviors

### The record core is shared

Every module — giving, check-in, groups, events, communication — writes back to the same person record. This single-profile invariant is the ChMS's central promise: attendance, giving, and group involvement are read together on one profile, and it is why standalone tools in the same market advertise their integration with the ChMS database.

### Members are subjects, not operators

Self-service is real but scoped: members may edit designated fields of their own profile and interact with their own groups, while governance of the data — and of everyone else's — stays with the church. Some products keep children out of member accounts entirely, tracking minors through check-in rather than login.

### Congregant data is sensitive by default

Notes about counseling, health, or prayer requests; membership in recovery or care groups; and children's locations are visibility-controlled structures, not settings afterthoughts. Confidential group membership can be anonymous even to other members; sensitive profile fields can be masked from staff without explicit access; and, in some products, security labels deliberately omit information (such as a child's location) that must not leak to whoever holds the printed label.

### Check-in is a custody protocol

A child's checkout depends on matching security labels or codes, or on verifying that the arriving adult is authorized — even when labels don't match. Room capacity limits and live rosters support the same duty of care.

### Attendance is a pastoral signal

Because participation history accumulates on the person, absence becomes visible: lists of first-time guests, of regulars who stopped attending, of households without contact information. Much of the workflow machinery exists to act on exactly these signals — the records are kept not only for administration but to keep people "from falling through the cracks."

### Contribution records are distinct from collection channels

The ChMS records and attributes gifts; the channels that move money (online forms, text giving, kiosks) may be bundled, but conceptually belong to the giving platform that feeds the record. Statements and pledge tracking flow from the record, not the channel.

### Lifecycle is managed, not assumed

Moving from guest to regular to member to inactive is typically an explicit, tracked progression — via status fields, workflow steps, or milestone records — because follow-up, communication eligibility, and directory visibility often depend on it. Exact status vocabularies vary by product and by denomination.

## Variants

- **Denominational / heritage poles.** Catholic parish and diocese systems center the family census, sacramental milestones (baptism, confirmation, first communion), faith-formation classes, and diocesan-level compliance and reporting, sometimes with parish school tuition. Evangelical engagement-led systems emphasize guest pathways, discipleship steps, and serving. Mainline membership-led systems emphasize rolls, pastoral record-keeping, and giving history.
- **Packaging.** Modular suites priced per product (database free, modules paid); flat-price all-in-one bundles; enterprise engagement suites where the ChMS is one pillar beside giving and apps; open-source, self-hosted platforms with community ecosystems.
- **Scale posture.** Church plants and small churches (one office administrator doing everything), single-campus mid-size, multi-site large churches, and diocesan hierarchies managing many parishes as subordinate organizations.
- **Module depth.** Finance depth (fund accounting, check scanning, benevolence), worship/service planning depth (service plans, song libraries, chord charts, rehearsal), digital-platform breadth (websites, custom apps, streaming, sermon libraries), and learning/discipleship modules vary widely and are common bundling levers.
- **AI assistance.** Natural-language people search, giving-data question answering, list building, and prayer-request triage are appearing across the sample; treat as an era-common capability, not a defining one.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Church Giving Platform | adjacent sibling | owns collection channels and money movement; ChMS owns the people record and the contribution record; the two meet at the giver record |
| Church Communication Platform | adjacent sibling | owns the sending loop (compose, schedule, replies, opt-outs) over audiences drawn from the records; ChMS is the record substrate; ships both as standalone tools and as ChMS modules |
| Nonprofit CRM / Donor Management System | structurally similar | same record grammar (people, giving, groups, workflows) but generic-nonprofit objects; ChMS adds congregation-specific objects: households, attendance/check-in, child security, worship-life milestones |
| Membership Management System / Congregation Membership Management | slice | membership records and directories are one module of the record core; ChMS adds the participation machinery and operational modules around it |
| Ministry Scheduling / Worship Planning / Religious Small-group Management / Pastoral Care Management / Religious Volunteer Management | capability slices | each owns one loop in depth and exists both as a ChMS module and as a standalone specialist; the ChMS is the system of record that unifies them |
| Childcare Management System | check-in overlap | both run custody-style check-in, but childcare is a business (enrollment, tuition, ratios, licensing) while ChMS check-in is ministry safety inside a record system |
| CRM (generic) | same grammar, different domain | ChMS "pipelines" are guest and discipleship pathways, not commercial deals; objects are congregation-life objects |
| Association Management System | adjacent | AMS organizes self-governing subordinate units (chapters) with their own officers and finances; ChMS campuses are internal locations of one congregation |

## Representative Products

- **Planning Center** — modular suite; free people database with paid per-product modules (Groups, Check-Ins, Giving, Registrations, Services, Calendar); strong public documentation
- **Tithe.ly Church Management** (formerly Breeze ChMS) — flat-price all-in-one pole for small and mid-size churches
- **Pushpay ChMS** (formerly Church Community Builder) — enterprise engagement suite; process-queue heritage
- **Rock RMS** — open-source, self-hosted platform with the widest feature surface (websites, apps, TV apps, learning)
- **ParishSOFT** — Catholic parish and diocese heritage pole; census, sacramental, and faith-formation model

The defining core was checked against the heritage pole (parish census/offering recording) and against the pre-digital office-database pattern to avoid over-fitting to the modern engagement-suite implementation.

## Sources

Research date: **2026-09-07**

- Planning Center — People: https://planning.center/people · ChMS use case: https://planning.center/use-cases/chms · Check-Ins: https://planning.center/check-ins · Groups: https://planning.center/groups · Help article (custom fields): https://pcopeople.zendesk.com/hc/en-us/articles/204263134
- Tithe.ly Church Management: https://tithe.ly/chms
- Pushpay ChMS: https://pushpay.com/product/chms-software/ · Pushpay: https://www.churchcommunitybuilder.com/
- Rock RMS features: https://rockrms.com/rock-features
- ParishSOFT: https://www.parishsoft.com/

> Sourcing limitation: evidence for Tithe.ly, Pushpay, Rock RMS, and ParishSOFT is product-page tier; only Planning Center contributed a Tier-1 help-center article this pass, and Rock's book documentation was not reachable (404). Precise operational details (exact permission ladders, status vocabularies, numeric limits, pricing) are intentionally not asserted in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
