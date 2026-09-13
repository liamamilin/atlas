# Religious Education Management

## Overview

A **Religious Education Management** application is the congregation's education-program administration system: it runs the religious education program a congregation offers its own families — Sunday school, parish catechesis or faith formation, synagogue religious school, and comparable programs — by holding each enrolled student as a record, organizing students into classes led by teachers or catechists, and recording attendance session by session across a program year.

The defining core is small:

```text
The congregation's families (its own people records)
└── Enrolled student of record (a person enrolled in the program for a term)
    └── Class (students grouped with an assigned catechist/teacher and a meeting schedule)
        └── Session attendance (per-meeting participation marks, accumulating as history)
```

Everything else commonly associated with running such a program — online registration, fees, grade levels, rooms, sacrament or milestone tracking, rosters and labels, parent communication — is standard machinery that mature products add around this core. The system is deliberately **not** a school: it holds no academic transcripts, no state reporting, and no academic gradebook. It is also not a check-in system and not a content platform, though it interoperate with both.

## Users & Context

The operator is a congregation — a parish, church, synagogue, or mosque — running a supplementary religious education program for children and often adults. The system is staff-facing, with a family-facing self-service layer:

- **Program director / coordinator** (in Catholic parishes often the Director of Religious Education): configures the program year, builds classes, assigns catechists, oversees enrollment and fees, runs reports.
- **Catechists / teachers**: commonly volunteers drawn from the congregation; they receive rosters, take attendance, and communicate with parents.
- **Parents / families**: register children into classes, provide medical and learning-needs information, pay program fees, receive communications — typically through a family portal.
- **Congregation administrators**: maintain the underlying family and member records the program draws from; handle safety compliance for volunteers.

The work rhythm is the **program year**: enrollment opens before the term, classes meet on a recurring weekly or similar schedule through the term, attendance is taken at each meeting, milestones are recorded as students complete preparation, and the year closes with reports and rollover into the next term.

## Core Model

### The Defining Core

Three structures, held together, over the congregation's own people records:

**1. The enrolled student of record.** A person — typically a child of a family in the congregation — is held as a persistent enrollment in the program for a defined term. The enrollment is the unit everything else hangs on: it is created at registration, placed into a class, carried through the term, and accumulates the student's participation history. Students are not anonymous attendees; they come from the congregation's own family and member records, and registration runs through the family.

**2. The class as the taught unit.** Students are organized into classes within the program. Each class carries an assigned teacher or catechist — in practice usually a volunteer from the congregation, with a designated leader — a meeting schedule (day, time, recurring dates within the term), commonly a grade level, a room or location, and often a capacity. The class is the roster: the list of students someone is responsible for teaching.

**3. The session-attendance record.** Attendance is recorded per meeting date against the class roster. Each mark accumulates into the student's participation history in the program — the digital continuation of the traditional class register. Attendance is what makes the enrollment a living record rather than a list entry.

**The domain binding.** The program is the congregation's own religious education — catechesis, faith formation, religious school — administered by the congregation over its own families. Both the students and the teachers come from the congregation's people records. Remove this binding and the same machinery becomes generic children's-activity or class management.

### Standard Capabilities of Mature Products

Mature products carry most of the following. They make the program practical; they are not what makes the product a religious education management system.

- **Program term with rollover** — the term (program year) as the container for classes and sessions; classes and sessions copied forward to the next term; students promoted or transferred between classes and grades.
- **Online registration** — an enrollment window with start and end dates, per-session activation, ranked class choices, and capture of special learning needs and health or medical needs.
- **Fee machinery** — per-student fees, multi-child discounts, family-level caps, and discounts, with payment routed into the congregation's giving funds or an external payment page; many programs run free and skip this entirely.
- **Grade levels** as the placement vocabulary, and **rooms/locations** (building → room, capacity) for classes.
- **Program lines in one place** — children's religious education, adult faith formation, and vacation Bible school administered side by side.
- **Milestone / sacrament tracking** — preparation year, completion date, place and celebrant, group completion for a whole class; in Catholic implementations the sacrament records are permanent.
- **Reporting and output** — class rosters, catechist lists, attendance reports by date/grade/class, parent lists, mailing labels, name tags, attendance sign-in sheets.
- **Communication** — email or message students and parents, email volunteers, individually or by class.
- **Volunteer roles** for catechists and helpers.
- **Family portal** — self-service registration, fee payment, and family-record review.

### One Structure, Many Implementations

The core is written conceptually; products realize it differently:

```text
Concept:            Program term
Implementations:    term/program-year objects, school-year labels, single ongoing program

Concept:            Teacher / catechist
Implementations:    volunteer records with roles, staff records, leader flags on class rosters

Concept:            Milestone
Implementations:    sacrament records (Catholic), b'nei mitzvah preparation (synagogue),
                    confirmation class completion (Protestant)

Concept:            Enrollment
Implementations:    office-entered rosters, family-portal online registration, paper intake
```

A reader who encounters only one implementation should still recognize the others from the core.

## How It Works

### Set up the program year

```text
Define the term (date range spanning the program year)
→ define grades, rooms/buildings, departments, volunteer roles
→ define sessions (meeting day/time patterns that generate class meeting dates)
```

The term is the broadest timespan classes are held in; sessions within it generate the recurring meeting dates that attendance will hang on.

### Build classes

```text
Create classes within the term
→ each class bound to a session (meeting times), a grade, a room
→ assign a leader and volunteer catechists
→ set capacity
```

Classes may serve children's religious education, sacramental preparation, adult formation, or vacation Bible school — the same class structure carries all program lines.

### Enroll students

```text
Registration window opens (per term, per session)
→ families register through the portal (or the office enters enrollments)
→ family record reviewed/updated; student added with needs and medical notes
→ ranked class choices submitted
→ fees calculated (per-student, multi-child discount, family cap) and paid
→ placement confirmed — or rejected if the class is full
```

Enrollment binds the student into a class roster for the term. Only people who exist in the congregation's family/member records can be enrolled or serve as volunteers.

### Run sessions and record attendance

```text
Class meets on its scheduled date
→ catechist or office records attendance against the roster
→ marks: present / absent, commonly tardy and excused
→ bulk "mark all present" then correct exceptions
→ attendance accumulates per student across the term
```

Attendance requires a scheduled meeting: a class with no meeting dates cannot take attendance. A student appears on the attendance list only when enrolled within the session's date parameters.

### Track milestones

```text
Students in a preparation class complete the program's milestone requirements
→ milestone records updated (individually or as a group for the whole class)
→ preparation year, completion date, place, celebrant recorded
→ records retained permanently on the person's record
```

### Close the year and roll over

```text
Term-end reports (attendance, rosters, catechist lists, parent lists)
→ classes and sessions copied to the next term
→ students promoted or transferred to their next classes
→ new registration window opens
```

### Capability tiers

**Defining core** — without these, not this Type:

- enrolled student of record (term-bound enrollment from the congregation's families)
- class with assigned catechist/teacher and meeting schedule
- per-session attendance recorded against the class roster

**Standard capabilities** — present in most modern products:

- program term with rollover and student promotion
- online registration with windows, class choices, needs capture
- fee machinery with family-level logic
- grade levels, rooms/locations, program lines
- milestone/sacrament tracking
- rosters, attendance reports, labels, name tags
- communication with parents and volunteers
- family portal

**Variant / optional** — depends on tradition, market, and deployment:

- sacramental machinery specific to a tradition
- check-in integration and background screening / safe-environment compliance
- curriculum and content delivery (the content-platform shape)
- paid vs free programs
- desktop vs cloud; module vs standalone product

## Interfaces

The following surfaces are described conceptually; names and layouts vary by product.

### Students & volunteers list

The program's people view.

- lists enrolled students and assigned volunteers for the selected term, filterable by session, class, grade, department, role
- primary actions: add a student to a class, add a volunteer, filter, export

### Classes & sessions

The program's structure view.

- classes tab: each class with its session, leader, volunteers, grade, capacity, and enrollment count; open a class to see and edit its roster
- sessions tab: meeting day/time, date ranges, volunteers, classes offered
- primary actions: add/copy classes and sessions (including copying to the next term), enroll or transfer students, export

### Attendance

The term's operating rhythm.

- filterable by session/class/grade/date; per-student present/absent marks with tardy and excused options; bulk marking
- printable sign-in sheets and blank attendance sheets; attendance reports by date, grade, class

### Registration setup & family portal

The enrollment front door.

- staff side: enable registration per term and session, set start/end dates, configure fees (flat, multi-child tiers, family cap, discounts) and payment routing
- family side: review family details, select term, add students with needs information and ranked class choices, pay, receive confirmation

### Milestone / sacrament records

The program's permanent memory.

- milestone types with preparation year, completion date, place, celebrant
- search by prep year, term, class, grade, age; group entry for a whole class; printable certificates

### Reports & labels

The output layer.

- class rosters, catechist lists, attendance reports, parent information, mailing labels, name tags

### Settings

The configuration layer.

- terms, grades, rooms/buildings, departments, volunteer roles; registration and payment switches

## Important Rules / Behaviors

- **People come from the congregation's records.** Students and volunteers must exist in the congregation's family/member records before they can be enrolled or assigned — the program administers the congregation's own people, not a walk-in population.
- **Attendance requires a scheduled meeting.** A class with no meeting dates, or not tied to a session, cannot take attendance.
- **Enrollment gates attendance visibility.** In the deepest-documented implementation, a student appears on an attendance list only when the enrollment date falls within the session's date parameters.
- **Capacity gates acceptance.** Registration into a full class can be rejected; in products with an online registration flow, families are notified of acceptance or rejection.
- **Attendance records persist.** Once recorded, an attendance record stays; statuses can be changed (present ↔ absent, tardy, excused) but the record is not removed.
- **Milestone records are permanent.** In the deepest-documented implementation, sacrament records can be viewed, added, edited, and printed but not deleted.
- **Structure in use is retired, not deleted.** A term that has been used in classes or sessions is deactivated rather than deleted.
- **Fees are family-shaped.** Fee logic commonly operates at the family level: per-child amounts, multi-child discounts, and caps on what a family pays in total.
- **Rollover copies structure, not students.** Copying classes and sessions to the next term typically carries the class setup; students move by promotion or transfer.

## Variants

- **Catholic parish faith formation** — the deepest realization: program-year classes plus sacramental-preparation machinery (preparation years, completion records, celebrants), safe-environment screening for volunteers, and tuition handling for programs that charge.
- **Protestant Sunday school** — frequently realized without a dedicated module: classes live as groups in a church management system, with attendance through groups or children's check-in; the education-program loop is the same even where the packaging differs.
- **Synagogue religious school** — enrollment, classes, teachers, attendance, and b'nei mitzvah preparation within synagogue management systems.
- **Content-platform shape** — curriculum providers that pair a large library of lessons, videos, and assessments with a class-management layer (rosters, attendance, homework, progress) for parishes and schools.
- **Paid vs free programs** — fee machinery present or absent.
- **Deployment** — desktop-installed classics, cloud suites, module vs standalone packaging.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Church Management System (ChMS) | the whole-congregation record core (members, giving, events); religious education is one program slice — often shipped as a module of a ChMS, which is the dominant packaging of this Type |
| School Management System / SIS | a school's academic operations: transcripts, state reporting, academic gradebooks; congregational catechesis has none of these — full-time parochial schools belong there, not here |
| Learning Management System / Educational Content Platform | centers the curriculum being delivered (lessons, videos, assessments); this Type centers the program being administered — content platforms with class layers straddle the seam |
| Ministry Scheduling | schedules volunteer serving positions against occasions; this Type runs the class/enrollment/attendance loop — suites ship both as separate modules |
| Childcare Management | custody-and-care operations with capacity-limited care inventory and per-stay billing; catechesis programs teach, they do not provide care custody |
| Event Management | centers an event's registration, logistics, and money economy; vacation Bible school is administered here as a program line, not as an event product |
| Children's check-in systems | center secure per-event check-in/out with security labels; no enrollment, classes, or terms — they interoperate with class rosters but neither subsumes the other |
| Course Registration System | centers the registration transaction itself; here registration is the entry act of an ongoing program relationship |
| Nonprofit Program Management | generic program-delivery machinery (programs → planned elements → delivery records); this Type carries the congregational education grammar — enrollment, classes, grades, attendance, milestones |
| Classroom Management | K-12 classroom instruction and behavior tools for schools; not congregational program administration |

The most important boundary is with the **Church Management System**: this Type is best understood as the education-program loop that congregations run — realized most often as a dedicated module inside a ChMS, occasionally as a standalone product, and in the Protestant market frequently through generic groups plus check-in.

## Representative Products

- **ParishSOFT (Faith Formation / Religious Education module)** — Catholic parish suite with a dedicated religious-education module: terms, sessions, classes, catechists, attendance, online registration with family fee logic, sacrament tracking.
- **CatholicBrain** — Catholic faith-formation content platform with a class-management layer (rosters, attendance, homework, progress, DRE admin portal).

Market-structure note: the dedicated-module realization is Catholic-market-led; Protestant church management systems (Churchteams, Servant Keeper, Church Windows, PowerChurch, Breeze/Tithely) realize Sunday school through groups and check-in without a dedicated module, and children's check-in specialists (KidCheck, Planning Center Check-Ins) serve the adjacent security/attendance need. Synagogue religious-school modules exist in the market but could not be verified from official documentation in this research pass (see Sources).

## Sources

Research date: **2026-09-09**

- ParishSOFT — Faith Formation product page: https://www.parishsoft.com/faith-formation/ ; support center articles (Religious Education module navigation, settings/lookups, add a class, taking attendance, online registration and fee payment, adding volunteers, classes & sessions page, group sacraments, My Own Church registration): https://support.parishsoft.com/hc/en-us
- CatholicBrain — https://www.catholicbrain.com/
- KidCheck — https://www.kidcheck.com/
- Planning Center Check-Ins — https://www.planningcenter.com/check-ins
- Churchteams — https://www.churchteams.com/
- Servant Keeper — https://www.servantpc.com/
- Church Windows — https://churchwindows.com/
- PowerChurch — https://www.powerchurch.com/
- Breeze ChMS / Tithely — https://www.breezechms.com/

> Sourcing limitations: the synagogue-management vendors that market religious-school modules (ShulCloud, ChaverWeb) blocked automated access (HTTP 403 / transport errors, including via web archive), so the Jewish pole rests on market context only and no operational claims are drawn from it. Madrasa / Islamic supplementary-school software could not be verified (search engines degraded). The ParishSOFT fact-sheet PDF was reachable only as binary and was not text-extractable in this environment. Precise numeric limits, prices, and plan details are deliberately omitted from this document; product-specific mechanics remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical / market-sample checks are recorded in the paired Research Notes.
