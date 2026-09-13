# Classroom Management

## Overview

A **Classroom Management application** is the teacher-facing control surface for running a live class. It binds a roster of identified students to a taught class and lets the teacher observe and act on students' in-class state while the class meets: marking who is present, recording conduct as it happens, watching and steering the screens and devices students are working on, and arranging where students sit.

The defining core is deliberately small:

```text
Class roster (identified students bound to a taught class)
└── Teacher-facing control surface (the teacher operates; students are the managed subjects)
    └── In-the-moment operation on the class as it meets
```

Everything commonly associated with the category — screen thumbnails, web filtering, behavior points, seating charts, timers, noise meters, parent communication, cloud deployment — is standard capability that mature products add to make that core workable. No single one of them is required: real products exist that monitor devices but record no conduct, and products that record conduct but touch no devices. What makes the software classroom management is the frame: the teacher, the class roster, and direct action on what is happening in the room right now.

When the dominant surface shifts to hosting courses and content, to setting and grading work across days or weeks, to delivering the lesson itself online, or to school-wide records and discipline case management, the product is drifting toward a different Application Type (Learning Management System, Assignment Management, Virtual Classroom, Student Behavior Management).

## Users & Context

The primary user is a **classroom teacher** — most commonly in K-12 schools, but the same role exists in computer labs, higher education, and corporate training rooms. The teacher uses the application during lessons: at the start (register, seating, launching materials), throughout (watching screens, awarding points, locking or redirecting devices), and at the end (reviewing what happened).

**Students** are the managed subjects rather than operators. They experience the application's effects directly: their screen may be locked or redirected, websites blocked or opened for them, points awarded or deducted, their seat assigned. In some products students also have a small active role — requesting help, raising a hand, seeing their own points.

Secondary users shape how the application is configured and governed:

- **IT administrators / technicians** — deploy the software, connect it to school systems, set base policies, and in some products operate a separate technical console for device maintenance.
- **Co-teachers and paraprofessionals** — share access to the same class in several products.
- **School leaders and behavior managers** — view school-wide conduct data, configure behavior reasons and consequences, and manage staff permissions.
- **Parents and families** — in some products receive behavior points, messages, or reports; visibility is typically configurable by the school.

The work context is a scheduled class period. The application is opened when the class meets and its actions are anchored to that meeting — which is what separates it from software that manages coursework across time or student records across years.

## Core Model

### The Defining Core

Three structures. Remove any one and the product stops being recognizable as classroom management:

- **Class roster** — a defined set of identified students bound to a class the teacher teaches. The roster is the address book of every action: attendance is marked against it, points are awarded to it, commands are sent to its members, seats are assigned from it. Rosters typically come from school systems (student information systems, MIS, Google Classroom, Clever, ClassLink) or are entered manually.
- **Teacher-facing control surface** — a dedicated surface from which the teacher observes and acts. The teacher is the operator; students are the managed subjects. This is the structural opposite of a collaboration workspace (where everyone operates) or a broadcast (where the teacher only presents).
- **In-the-moment operation on in-class state** — the unit of work is the class meeting. The teacher observes what is happening now (who is present, how students are behaving, what is on their screens, where they sit) and acts on it now (marks, awards, commands, moves). This is what distinguishes the Type from software that manages work completed across time.

### The Four State Domains

Mature products fill the frame by letting the teacher observe and act on some combination of four domains of in-class state. Products specialize — most go deep on one or two — but the domains recur across the market:

- **Presence** — who is in the room. Implemented as a class register or attendance marking taken during the lesson, sometimes with custom prompts.
- **Conduct** — how students are behaving. Implemented as points (positive and often negative) with configurable reasons or skills, notes, badges or rewards, and reports; in some products extended with school-wide consequences such as sanctions and detentions.
- **Device and screen state** — what students are doing on their devices. Implemented as live screen thumbnails, activity timelines, screenshots, and control commands: lock or blank screens, open or close tabs and applications, push a website to everyone, restrict web and app use, mute audio.
- **Physical arrangement** — where students sit. Implemented as seating plans: a canvas of the room's desks, drag-and-drop placement of students, and student cards showing relevant data (support needs, assessment data) for use during the lesson.

### One Structure, Many Implementations

The core model is written in conceptual terms. Implementations vary widely:

```text
Concept:            Class roster
Implementations:    SIS/MIS sync, Google Classroom / Clever / ClassLink sync,
                    manual entry, enroll codes, fixed machine lists (lab era)

Concept:            The class meeting
Implementations:    explicit start/stop session bound to a schedule;
                    a live connection between teacher console and student devices;
                    a persistent class with a per-lesson register

Concept:            Conduct record
Implementations:    points with custom skills/reasons, badges, stickers,
                    behavior events with sanctions and detentions

Concept:            Device control
Implementations:    browser extension, installed agent, network client

Concept:            Observation
Implementations:    screen thumbnails, activity timelines, screenshots,
                    app/website/keyboard histories, register tallies
```

A reader who has only seen one implementation — say, a cloud service that shows Chromebook screens — should still be able to recognize an on-premise lab controller or a behavior-points app as the same Type from the core model.

### Capabilities Shared by Mature Products

These are not what makes the product classroom management, but they make it practical:

- roster integration with school systems
- a session or connection model binding the teacher's surface to student devices for the lesson
- screen monitoring (thumbnails, live view, screenshots, activity histories)
- device-control commands (lock/blank screen, open/push content, close tabs or apps, restrict web/apps)
- in-class web and application filtering, with teacher-level temporary override of school policy
- teacher↔student messaging (chat, help requests, raise hand)
- conduct recording (points, rewards, custom reasons, notes, reports)
- attendance/register
- seating charts with student data cards
- in-class engagement tools (timer, random student selector, group maker, noise meter, check-ins, quick surveys)
- records of what happened (session logs, command logs, behavior reports) for later review
- role separation between the classroom teacher and IT/administration, with co-teacher sharing and granular permissions

## How It Works

### Set up the class and roster

```text
Create or import the class
→ roster arrives from the school system (SIS/MIS/Google Classroom/Clever/ClassLink)
  or is entered manually
→ students are identified individuals, not anonymous devices
→ optional: co-teachers granted access; groups defined within the class
```

Roster setup is usually done once per term or year; some products re-sync automatically at each login.

### Open the class for a lesson

```text
Select the class
→ start a session (often scheduled to match the timetable)
   or connect to the students' devices
   or open the class and its register
→ students join: automatically through their managed school accounts,
  or by the teacher connecting to known devices
→ the teacher's surface now reflects the live class
```

In device-centric products the session is explicit — it has a start and end, and restrictions applied during it are released when it ends. In conduct-centric products there may be no explicit session at all: the class is persistent, and the register or points panel is simply opened during the lesson.

### Observe

The teacher watches the class through the surface the product provides:

- a grid of student tiles showing each student's current screen or active tab
- a register showing presence
- behavior tallies per student
- activity histories (websites, applications, sometimes keyboard activity)

### Act in the moment

The characteristic actions of the Type, all taken against the roster during the lesson:

- **direct devices** — lock or blank screens to get attention; open a website on every device; close a distracting tab; restrict the class to approved sites or apps; push a file or page
- **record conduct** — award or deduct points with a reason and optional note; give a badge or sticker; in some products escalate to a sanction or detention
- **mark presence** — take the register, noting absences
- **arrange the room** — move students on the seating plan; reshuffle groups
- **communicate** — send a private message to one student, an announcement to all; students may request help
- **run the room** — start a timer, pick a random student, generate groups, show a noise meter on the projector

### Close and review

```text
End the session (restrictions released; locks cleared)
→ the product keeps records: browsing timelines, screenshots, command logs,
  behavior events, attendance
→ teacher (and sometimes school leaders) review reports
→ in some products, summaries flow to families
```

### The conduct loop

Conduct deserves its own loop because it extends beyond the single lesson:

```text
Observe behavior
→ award positive or negative points with a reason (customizable per school)
→ event recorded centrally, attributed to the staff member, timestamped
→ visible on the student's profile and in class and school reports
→ visibility to the student and family is configurable per event and per school
→ in some products, negative events trigger consequences
  (sanctions, detentions) through school-defined rules
```

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Class dashboard

The teacher's entry surface.

- lists the teacher's classes as tiles or a menu
- shows sync status of rosters
- primary actions: open a class, start a session, schedule sessions

### Live session view / screens grid

The operational heart of device-centric products.

- a tile per student: name, current screen or active tab, connection state
- selection of one, some, or all students
- primary actions: lock/blank screens, open or close tabs, push a URL, restrict web/apps, screenshot, message, exclude an absent student

### Register / attendance view

- the class list with present/absent marking for the current lesson
- primary actions: mark students, add notes, submit to the school record where integrated

### Conduct / points panel

- the class list with per-student point tallies
- awarding controls: positive/negative points, reason picker, comment, badge
- primary actions: award to one/many/all, undo, view student history

### Seating plan canvas

- a top-down canvas of the room with desks
- student cards draggable onto seats, showing chosen data (support indicators, assessment data)
- primary actions: place desks, assign seats, autofill, save as template, project the plan for the class

### In-class toolkit

- single-purpose tools displayed full-screen or on the projector: timer, random student picker, group maker, noise meter, direction reminders
- primary actions: start/configure the tool, cast to the room display

### Reports / history

- past sessions and events: timelines, screenshots, command logs, behavior reports, attendance summaries
- primary actions: review, filter by student or date, export or share

### Administration console (secondary surface)

- IT/admin-facing: deploy and configure, manage staff accounts and permissions, set base filtering policy, review usage and logs
- deliberately separate from the teacher surface — a structural feature of the Type

## Important Rules / Behaviors

### Teacher actions are visible to students

The managed subjects see the effects of the teacher's actions: a locked screen displays a message, a blocked site shows a block page, awarded points appear on the student's view. The application is not covert surveillance tooling in its classroom form; visibility is part of how it steers behavior.

### Device restrictions are lesson-scoped

In products with explicit sessions, locks, blocks, and restrictions applied during a session are released when the session ends — a lock does not follow the student into the next class. Some products coordinate overlapping sessions between teachers so a lock is never orphaned; in products without explicit sessions, screen blanking and locking are manual toggles the teacher controls directly.

### Teacher overrides are temporary; school policy is the base layer

Where the product includes in-class web filtering, the teacher's rules apply during the lesson on top of — not instead of — the school's managed filtering policy. This division of labor (teacher = momentary, school = standing) is a structural rule of the Type and the reason IT administration exists as a separate role.

### Conduct records are durable and attributable

A behavior event is a record: it carries the student, the reason, the staff member, a timestamp, and an optional comment. Records persist on the student's profile across lessons and terms, feed reports, and — where families are connected — may be shared under configurable visibility rules (positive-only, staff-only, per-event comment sharing).

### Permissions gate conduct and visibility

Who may award points, who may see other staff members' events, who may manage reasons and consequences, who may view seating plans — these are permission-controlled. In whole-school products the permission model is granular enough to distinguish a classroom teacher from an attendance officer or behavior manager.

### The roster binding makes actions apply to the right student

Commands, points, attendance, and seats all resolve through the class roster to identified students. This is why roster integrity (sync with school systems, handling of adds/removes) is a first-class concern rather than a convenience feature.

### Records are kept

Sessions leave traces — timelines, screenshots, command logs, chat records — and behavior leaves records. Review of these records by teachers, school leaders, and (in some products) administrators is a normal part of the loop, not an exception path.

## Variants

The Type is implemented in several recognizable shapes. A variant remains a variant of this Type unless it changes the core users, objects, or workflow so much that the frame no longer applies:

- **Device-monitoring classroom management** — the teacher's surface is a live grid of student screens with control commands and in-class filtering; conduct and attendance are minimal or absent. Common in 1:1 device schools and computer labs.
- **Behavior/community classroom management** — the surface centers on conduct points, class culture, and family communication; no device control at all. Common in elementary grades.
- **Whole-school platform modules** — classroom management capabilities (register, seating, behavior) ship as modules of a broader learning platform alongside homework, assessment, timetables, and MIS integration; school-wide discipline machinery (sanctions, detentions, referrals) lives in the same system.
- **Lab-heritage on-premise controllers** — locally hosted teacher console controlling networked lab computers; the historical form of the Type, still in use, often extended with testing and device-maintenance tools.
- **Audience extensions** — the same structure serves corporate training rooms and higher-education teaching spaces.
- **Regional framings** — US products emphasize filtering, scenes, and PBIS-style positive behavior; UK products emphasize the MIS-connected register, behaviour points, detentions, and sanctions.
- **Business models** — freemium teacher-first adoption, district/site licensing, and hardware-bundle packaging all occur.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Learning Management System | adjacent, often integrated | an LMS hosts courses, content, and work over time; classroom management operates the live class and hosts no content |
| Assignment Management | adjacent, sharpest workflow seam | assignment management governs work completed across time (set → submit → grade → return); classroom management governs the class as it meets; whole-school products ship both as separate modules |
| Virtual Classroom | adjacent | a virtual classroom delivers the lesson itself online (video, whiteboard, lesson surface) for remote teaching; classroom management observes and controls the class rather than delivering instruction |
| Student Behavior Management | overlapping module | in-class conduct points are classroom management; school-wide discipline machinery (referrals, sanctions, detention administration, program management) is a distinct Type — some platforms contain both |
| Student Attendance System | overlapping module | the in-class register is classroom management; school-wide attendance records, statutory reporting, and absence management are a distinct Type |
| Endpoint Management / UEM | adjacent, frequently confused | UEM is IT-admin policy management of device fleets; classroom management is teacher-facing live control during class; vendors themselves ship them as separate products with separate consoles |
| Student Information System | upstream | the SIS holds enrollment and records; classroom management consumes rosters from it and writes some events back, but does not manage student records |
| Audience Response System | capability overlap | an ARS collects responses to items from many participants and shows aggregates; some classroom-management products embed survey/Q&A capabilities, but response collection is not the defining action of this Type |
| Assessment Platform | capability overlap | embedded quizzes and tests exist in some products; formal assessment (item banks, scoring pipelines, results systems) is a distinct Type |
| Childcare Management System | name collision only | "classroom management" in childcare software means rooms, capacity, and staff-to-child ratios — a different object world entirely |

## Representative Products

- **GoGuardian Teacher** — device-monitoring pole; cloud service with a browser extension; live sessions, screen views, commands, in-class filtering scenes; US K-12 district scale
- **LanSchool (Air / Classic)** — lab-heritage device control in both cloud and locally hosted forms; screen monitoring, device commands, messaging, testing
- **NetSupport School** — classic full-featured classroom management across platforms; monitoring, control, instruction, assessment, rewards, technician console; K-12 through corporate training
- **ClassDojo** — behavior/community pole; conduct points with custom skills, class story, family messaging, in-class toolkit; freemium, global
- **Satchel One** — whole-school platform carrying classroom-management modules (register, seating plans, behaviour with sanctions and detentions) alongside homework and MIS integration; UK framing

The defining core was checked against the lab-era on-premise lineage (LanSchool Classic, NetSupport School) and the behavior-only pole (ClassDojo) to avoid defining the Type by any single era, deployment model, or capability family.

## Sources

Research date: **2026-09-07**

- GoGuardian Teacher — official documentation: overview, starting a classroom session, commands overview — https://docs.goguardian.com/products/teacher
- LanSchool — official product pages (Air, Classic) — https://lanschool.com/solutions/lanschool-air , https://lanschool.com/solutions/classic
- NetSupport School — official product and features pages — https://www.netsupportschool.com/ , https://www.netsupportschool.com/features/
- ClassDojo — official product pages and help center (points, class setup, toolkit) — https://www.classdojo.com/points/ , https://help.classdojo.com/
- Satchel One — official help center (staff collection; behaviour; seating plans) — https://help.satchelone.com/

> Sourcing limitation: the LanSchool knowledge base was unreachable from the research environment (redirect and empty responses), so LanSchool claims rest on its official product pages only. The Satchel One marketing site is script-gated; its evidence comes from the official help center. Vendor adoption figures quoted on marketing pages were treated as claims, not facts. Precise product defaults and limits are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
