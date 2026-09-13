# Congregation Membership Management

## Overview

A **Congregation Membership Management** application is the church-side system that maintains the congregation's roll of people: identified individuals, organized into households, each carrying a recorded membership status, administered by the church's own staff and leaders. It answers the most basic administrative question a congregation has — who belongs to us, who is connected but not yet enrolled, who has moved away, who has drifted — and produces the directories, lists, labels, and reports that the rest of church administration runs on.

The defining core is deliberately small:

```text
Congregation people roll (identified individuals)
└── Recorded membership status per person
    └── Church-side administration of the roll
```

Everything else commonly associated with church software — attendance kiosks, giving tools, group modules, texting, member apps — is standard capability layered around the roll, or belongs to neighboring application types. A parish register, a paper membership roll with letters of transfer, or a 1990s single-desktop office database satisfies the core without any modern machinery.

In the market this type appears in two shapes: as **standalone products and modules** (a free membership database usable entirely on its own; a membership module purchasable separately from a desktop suite; a parish census and family-directory module), and as the **record core inside full church management systems**. What makes it a type of its own is the roll itself — people, households, membership status, and the outputs derived from them — without the operational machinery (check-in stations, giving collection, groups, events) whose presence would make the product a full Church Management System.

## Users & Context

The organization, not the individual, is the operator. Primary users:

- **Church office administrators and membership secretaries** — maintain the roll: add people and families, update contact details, merge duplicates, process transfers, record removals
- **Pastors and pastoral staff** — read status and history, record visits and pastoral notes, act on lifecycle events (a new family, a death, a drifting household)
- **Lay leaders and class/group leaders** — delegated, scoped access to their own slice of the roll: a class roster, a committee list

Secondary users are the **members themselves**, through a member portal or app: they update their own contact information, opt into the directory, and view their own record. Members are the subjects of the roll, not its operators — a structural distinction from community platforms where members are the primary actors.

The work context is the church office during the week (records, updates, lists, reports) plus recurring annual rhythms: directory publication, year-end reporting, membership classes and intake, and transfer processing when families move between congregations.

## Core Model

### The Defining Core

**Person record (roll entry).** The central object: an identified individual with name and contact details, demographic fields, and an extensible set of custom fields (typed fields and tabs — text, date, dropdown, checkbox — are common). The person record is the anchor to which status, history, and outputs attach.

**Membership status.** The defining field: the roll distinguishes who belongs (member) from who is connected but not enrolled (visitor, regular attender) and who has left (inactive, transferred, removed). Status is recorded by the church, not claimed by the member — in many congregations, becoming a member is a governed act (a class, a rite, a transfer approved by the church), and the system records that act. Exact status vocabularies vary by product and by tradition.

**Church-side administration.** Staff and lay leaders hold permissioned access and maintain the roll; members may self-edit scoped fields of their own record, but governance of the data — and of everyone else's — stays with the church.

### Standard Capabilities Around the Core

Mature products carry most of the following. They make the roll operational but do not define the type:

- **Households / families** — people grouped into family units as first-class records. Address and contact information are often held at household level, children belong to a household under their guardians, and non-traditional family structures are accommodated. In Catholic variants the family is the unit of registration, with individuals as family members.
- **Custom fields** — the congregation extends the person record for its own data needs (school grade, skills, interests, communication preferences, baptism dates).
- **Directories** — the roll rendered for people to use: printable directories in multiple formats, and/or a member-facing directory where members appear and connect, with privacy controls over who appears.
- **Lists, labels, and reports** — the roll queried and rendered for administration: mailing labels, email lists, class and committee rosters, birthday and anniversary reports, attendance summaries, custom reports by criteria, and exports to spreadsheets or word-processor merges.
- **Attendance as a signal** — light recording of personal attendance at events and worship, kept on the person. This is a membership-health signal (who is active, who has drifted), distinct from the check-in machinery of a full church management system.
- **Lifecycle and milestone records** — the dated events of belonging: joining (membership class, baptism, profession of faith, transfer in), leaving (transfer out, death, removal). Catholic variants keep sacramental milestones as lifelong records with certificate and notification-letter templates.
- **Member self-service portal** — profile self-update, directory visibility, giving-history view, class and volunteer signups, in the products that offer one.
- **Duplicate merge and data hygiene** — duplicate profiles are a normal hazard of congregation data; merge tooling is standard in mature products.
- **Sensitive notes** — visitation logs, pastoral care, counseling, and health notes stored on the record under restricted visibility.
- **Communication from the roll** — emailing individuals, groups, or committees; printing labels. (Managed messaging loops — compose, schedule, track, opt-out — belong to the communication-platform type.)
- **Import, export, and migration** — CSV import/export and vendor-assisted migration; switching systems is a known market dynamic.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:   Congregation people roll
Realized as:  person profiles with custom fields (modular suites),
              family + individual records in one view (desktop heritage),
              family census / directory records (parish heritage)

Concept:   Membership status
Realized as:  status fields updated by automations,
              membership-progress workflows,
              parishioner registration and sacramental records

Concept:   Roll outputs
Realized as:  printed directories and labels,
              member-facing directories and portals,
              lists, reports, and exports
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

## How It Works

### Enroll a person or family

```text
A family visits, registers online, or fills a connection card
→ the record is created (household linked, members attached)
→ staff complete and verify the profile
→ membership status is recorded (visitor, attender — or member,
   once the class / rite / transfer is completed)
```

People enter the roll through capture surfaces (forms, registration, portal self-registration) or through migration from a previous system. Duplicate profiles are a normal hazard of congregation data; merge tooling is common in mature products.

### Maintain the roll

```text
Life happens: moves, new children, deaths, families changing congregations
→ staff update contact details, merge duplicates, record lifecycle events
→ status changes are recorded explicitly (joined, transferred in/out, removed, inactive)
→ removed people are typically retained as history, not deleted
```

The roll is a living census. Membership is managed, not assumed: moving from visitor to member to inactive is an explicit, tracked progression, because directory visibility, communication eligibility, and reporting often depend on it.

### Use the roll

```text
Build or open a list (a query over the roll, often saved and auto-refreshing)
→ render it: mailing labels, email list, class roster, directory, report
→ act: contact the list, publish the directory, file the report
```

This loop — query the roll, render, act — is the administrative heartbeat of the type. The same roll feeds the printed directory, the member-facing directory, the newsletter labels, and the annual report.

### Member self-service

```text
Member signs in to the portal / app
→ updates their own contact information (scoped fields)
→ opts into (or out of) the visible directory
→ views their giving history, signs up for classes or volunteering
→ changes flow back into the same records staff work from
```

### Feed neighboring systems

```text
The roll is the substrate:
→ giving systems attribute gifts to people on the roll
→ check-in and attendance systems write participation back to profiles
→ communication systems draw audiences from lists built on the roll
```

Standalone realizations of this type exist precisely because the roll can stand alone; the surrounding systems integrate with it rather than replace it.

### Core vs standard vs optional

- **Defining core** — the people roll; recorded membership status per person; church-side administration.
- **Standard capabilities** — households, custom fields, directories, lists/labels/reports, attendance-as-signal, lifecycle records, member portal, duplicate merge, sensitive notes, communication from the roll, import/export.
- **Optional / variant** — background checks, workflow automation, forms feeding the roll, giving-history views, multi-campus support, diocesan-level hierarchies, desktop vs hosted deployment.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### People list & profile

The primary staff surface. The list searches and filters the roll; the profile shows the person's details, household, custom fields, status, attendance signal, and notes. Primary actions: create/edit/merge profiles, change status, add notes, add to a list or group.

### Household view

The family-unit surface: household contact details, all family members (often with ages), alternate addresses. Primary actions: edit household, add or move members, record household-level changes.

### Directory

The roll rendered for people: printable formats for the office, and/or a member-facing directory with privacy controls. Primary actions: generate/print, control visibility, publish.

### Lists, labels & reports

The query-and-render surface: saved criteria, auto-refreshing lists, label printing, custom reports, exports. Primary actions: build/save a list, print labels, generate a report, export.

### Member portal / app

The congregation-facing surface: profile self-service, directory, giving history, signups. Primary actions: self-edit scoped fields, opt into the directory, register.

### Administration & permissions

Configuration of users, roles, and visibility — which staff see which records, which fields are restricted, what members may self-edit. In some products this reaches field level: sensitive fields can be hidden from staff without explicit access.

## Important Rules / Behaviors

### Status is governed, not self-declared

Membership status changes are recorded by the church — through a class, a rite, a transfer, or an administrative action — not by the member clicking a button. The member may self-edit contact fields; the status belongs to the congregation's governance.

### Status drives visibility and eligibility

Directory inclusion, communication eligibility, and reporting categories typically depend on status. A visitor, an active member, and an inactive member appear differently (or not at all) in the directory and the lists built from the roll.

### The roll is the substrate

Other systems — giving, check-in, communication, scheduling — attribute their records to people on the roll and often sync from it. This single-record invariant is why standalone tools in the same market advertise their integration with the membership database, and why the roll can be sold as a product of its own.

### Removal is a status, not an erasure

Leaving the roll is recorded as a terminal status (transferred out, inactive, deceased) rather than as a deletion — the status model itself keeps the person on the roll, because pastoral records, letters of transfer, and historical reporting depend on the continuity of the record.

### Congregant data is sensitive by default

Visitation and counseling notes, health information, and directory visibility are privacy-controlled structures. Members commonly control whether they appear in the directory; children's information is handled with particular care.

### Attendance is a signal, not machinery

Recording that a person attended is a membership-health observation. The full machinery of check-in stations, security labels, and custody protocols belongs to the church-management-system type; here attendance stays light — a dated mark on the person.

## Variants

- **Catholic parish census pole.** The family is the unit of registration; sacramental milestones are kept as lifelong records with certificate and letter templates; a diocesan-level census aggregates families, sacraments, staff, and volunteers across parishes.
- **Mainline membership-roll pole.** The roll, transfers between congregations, and long-lived family records are the center; directories and annual reporting are the main outputs.
- **Evangelical engagement-led pole.** Membership is one step in a tracked progression (guest → attender → member → serving); this emphasis blurs into the church-management-system type, where follow-up workflows and participation machinery dominate.
- **Packaging.** A standalone free product usable on its own; a purchasable module of a desktop suite; a module of a web suite; a lightweight all-in-one where the roll is bundled with check-in and giving; the record core of a full church management system (the dominant market pattern).
- **Deployment.** Locally installed desktop software (still current in the heritage pole), remotely hosted web access, and SaaS.
- **Scale.** A single congregation's roll; multi-campus churches; denominational or diocesan hierarchies aggregating many congregations' rolls.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Church Management System / ChMS | closest neighbor | ChMS is the roll **plus** participation machinery (attendance/check-in, giving records, groups, events, follow-up workflows) operated as one ministry system; this type is the roll without that machinery — and standalone roll-only products and modules exist |
| Membership Management System | generic sibling | same roll grammar, but generic members with dues, renewals, and benefits; congregation membership centers status, households, and pastoral records, with no dues machinery |
| Member Directory | output slice | the directory is one rendering of the roll (print and/or member-facing, privacy-controlled), not the maintained record itself |
| Church Giving Platform | meets at the giver record | the roll holds the person; the giving platform holds collection channels and gift records; suites commonly split them into separate modules |
| Church Communication Platform | meets at the audience substrate | the roll supplies lists and audiences; the comms type owns the sending loop (compose, schedule, replies, opt-outs) |
| Nonprofit CRM / Donor Management System | structurally similar | same record grammar but donor-centric (gifts, campaigns, appeals); this type is membership-centric (status, households, pastoral records) |
| Association Management System | adjacent market | AMS organizes self-governing member bodies and chapters with their own officers and finances; a congregation's roll has no subordinate self-governing units |

The most important boundary is with the Church Management System: the two share the record core, and most market products bundle the roll inside a ChMS. The seam is the participation machinery — strip it away and a standalone membership product remains; make it the product's center and the product is a ChMS.

## Representative Products

- **Planning Center People** — a free membership database explicitly usable on its own, with paid sibling products (Check-Ins, Giving, Groups, Registrations) integrating around it
- **Church Windows (Membership module)** — desktop-heritage suite whose Membership module is purchasable standalone, with Donations, Accounting, and Payroll as separate modules
- **ParishSOFT Families** — Catholic parish census and family-directory module with sacramental records and a parishioner portal; a diocesan Census module aggregates across parishes
- **Breeze ChMS (Tithe.ly)** — the lightweight all-in-one pole, where the people database is the center but check-in and giving are bundled

The defining core was checked against the heritage poles (parish registers, desktop membership modules) and against the pre-digital forms (paper rolls, transfer letters) to avoid over-fitting to the modern SaaS implementation.

## Sources

Research date: **2026-09-07**

- Planning Center People: https://planning.center/people · Help article (custom fields): https://pcopeople.zendesk.com/hc/en-us/articles/204263134
- Church Windows: https://www.churchwindows.com/ · Membership module: https://www.churchwindows.com/membership/
- ParishSOFT Families: https://www.parishsoft.com/families/
- Breeze ChMS: https://www.breezechms.com/
- Servant Keeper (boundary anchor): https://www.servantpc.com/ · Churchteams (boundary anchor): https://www.churchteams.com/

> Sourcing limitation: evidence for Church Windows, ParishSOFT, Breeze, Servant Keeper, and Churchteams is product-page tier; only Planning Center contributed a Tier-1 help article (fetched during the paired ChMS research pass). Planning Center's help-center search and member-app help sections are script-rendered and returned no article content, and one vendor help URL returned 404. Precise operational details (exact status vocabularies, permission ladders, numeric limits, pricing) are intentionally not asserted in this document; such details remain in the Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample check are recorded in the paired Research Notes.
