# Family Care Coordination

## Overview

A **Family Care Coordination** application is a private, shared space that helps the circle of people around one person who needs care — an aging parent, a relative with a serious illness or disability, someone recovering from surgery, a child with special needs — organize that care together. It gives a family one place to describe the care situation, invite the people who help, list what help is needed and when, let helpers claim those needs, and keep everyone informed about how the person is doing.

The defining core is deliberately small. A product in this Type has all four of these:

```text
Care recipient / care situation
└── Care circle (invited, private membership of known helpers)
    └── Care needs & occasions, expressed and claimed
        └── Circle-wide updates & communication
```

Everything else commonly associated with these products — medication lists, document storage, care journals, photo galleries, AI assistants, human care-navigation services — is widespread in current products but is not what makes the product a care-coordination tool. A volunteer meal-train website from the early 2000s and a modern AI-assisted caregiving app satisfy the same defining core.

The closest boundary: when the shared space is centered on the *household* rather than on *one person who needs care* (chores, shopping, a family calendar for everyone), the product is a Family Organizer. When the space matches strangers to care jobs for payment, it is a care marketplace. When an organization operates clinical coordination over patient populations, it is healthcare care coordination, not this Type.

## Users & Context

**Primary user — the family coordinator.** One person, usually a close relative, sets up and steers the space: creates it around the person receiving care, describes the situation, invites the circle, posts needs, and assigns or moderates. In practice this is often the sibling or adult child doing the largest share of caregiving ("primary caregiver", "care coordinator" are the roles real users name for themselves).

**Helpers — the circle.** Extended family (frequently living in different towns or states), friends, neighbors, congregation or community volunteers, and sometimes co-workers. They typically log in occasionally: to see what is needed, claim a task that fits their schedule, read the latest updates, or leave a note of encouragement.

**The care recipient.** Present in two ways: directly (using the app, or being the subject everyone coordinates around), or represented by the coordinator. Some products give the recipient the ability to answer "how can I help?" by simply pointing people to the page.

**Professional carers.** In some families, paid or professional caregivers are invited into the circle as members and post their daily notes there. Separately, one product pole layers a funded human service — dedicated care navigators reached through employer or health-plan benefits — on top of the same family coordination space.

Typical context: care is needed over weeks or years (illness, surgery recovery, dementia, disability, a birth), the helpers are scattered across households and geographies, and the recurring failure the product replaces is coordination-by-phone-tag — duplicated effort, missed appointments, unevenly distributed burden, and relatives who want to help but don't know how to ask or what to do.

## Core Model

### The Defining Core

```text
Care recipient / care situation
└── Care circle (invited, private membership of known helpers)
    └── Care needs & occasions, expressed and claimed
        └── Circle-wide updates & communication
```

Four properties. Each one is load-bearing — remove it and the product becomes a different kind of software:

- **A container centered on the care recipient.** The space exists for one person's care situation, not for a household, a team, or a listing. Products describe this directly: a village "centers on one loved one"; a community is created for "someone in need." A family caring for two parents typically runs two separate spaces. This is what separates the Type from family/household organizers.
- **An invited, private circle of known helpers.** Members are hand-picked — family, friends, neighbors, congregation members, invited professionals — admitted by invitation, shared access code, or approval. There is no stranger matching and no public feed. This is what separates the Type from care marketplaces and social platforms, and it makes the circle both a communication surface and an access-control boundary.
- **Care needs that are expressed and claimed.** The coordinator or recipient lists concrete help — a meal on Tuesday, a ride to an appointment, a visit, errands, sitting with the person, household tasks — usually attached to dates. Helpers see the open needs, claim or sign up for the ones that fit them, and the resulting commitments are visible to the whole circle, so gaps and overlaps are obvious. This express-and-claim loop is the actual coordination work of the Type.
- **Circle-wide updates and communication.** News about the person and the situation — condition changes, daily check-ins, photos, announcements, messages of support — flows to all members on a shared, persistent surface. Everyone holds the same picture, which is what allows helpers far away to stay involved without interrupting the household with phone calls.

A **coordinator role** and a **shared care calendar** recur in every mature product, but they are realized *inside* these four properties: a circle needs someone who creates and steers it, and the express-and-claim loop is normally organized by date. They are standard structure, not additional defining pieces.

### Standard Capabilities

Capabilities that mature products commonly carry, without defining the Type:

- **Care calendar** — the primary "when" surface: appointments, visits, meal deliveries, rides, and personal occasions (birthdays, anniversaries) laid out over time; events can be assigned to specific members.
- **Coordinator and member roles** — the creator can add other organizers, group members (by branch of the family, by congregation, by shift), and manage who is in the circle.
- **Reminders and notifications** — email or push reminders for claimed needs and upcoming occasions, aimed at eliminating "phone-tag" and email overload.
- **Encouragement surfaces** — short notes of support to the family, photo sharing, milestone memories.
- **Care records** (at the richest pole) — medication lists with photos, dosage reasons and reminders; important document storage; written care plans; a wellness journal tracking daily condition and mood over time.

### One Structure, Many Implementations

The core is stated conceptually. Products realize each piece differently:

```text
Care recipient-centered container  →  app "village", web "community"/"care team",
                                      a standalone signup-sheet "page"
Membership gating                  →  email/text invitations, shared access code,
                                      searchable teams with approval
Expressing needs                   →  dated task list, care-calendar entries,
                                      a one-button "who can help?" broadcast
Claiming                           →  online sign-up, volunteering from the list,
                                      assignment by the coordinator
Updates                            →  journal timeline, announcements, well wishes,
                                      team messages, photo galleries
```

A reader who has only seen one shape — say, a modern mobile caregiving app — should still be able to recognize an older church-organized meal calendar as the same Type from the core alone.

## How It Works

### Set up the circle

```text
Create the space around the person needing care
→ describe the situation (an announcement of purpose)
→ invite family, friends, and (optionally) professional carers
→ organize members into groups if the circle is large
```

Setup is deliberately light — minutes, not configuration projects. The situation announcement is a standard early step: it tells late joiners what is happening and what kind of help makes sense.

### Run the coordination loop

```text
Coordinator or recipient posts what is needed (a meal, a ride,
   a visit, errands, sitting — usually on a date)
→ helpers see open needs and claim or sign up for what fits them
→ reminders go out before the occasion
→ the commitment is visible to everyone; unfilled gaps stay visible too
```

This loop is the heart of the product. Its purpose is to convert diffuse goodwill ("let us know if you need anything") into concrete, scheduled, visible commitments — and to spread the work instead of letting it concentrate on one person.

### Keep the circle informed

```text
Coordinator or a carer posts an update (condition, check-in, photo, news)
→ the whole circle sees the same information at the same time
→ members respond with support, questions, or new offers of help
→ history accumulates, so someone returning after weeks can catch up
```

### Maintain care records (where offered)

```text
Add medications (with photos, dosage, reasons) → reminders fire
→ store important documents in folders
→ write and update care plans
→ journal daily condition and mood
```

Record-keeping is a capability of richer products, not a phase every circle goes through. A lightweight circle may use only the calendar and the needs list for its entire life.

### Core vs Standard vs Optional

**Defining core** — without these, it is not family care coordination:

- care-recipient-centered container
- invited, private circle of known helpers
- express-and-claim loop for care needs
- circle-wide updates and communication

**Standard structure** — present in essentially all mature products:

- shared care calendar
- coordinator vs member roles, member groups
- reminders/notifications
- situation announcement and member management
- encouragement and photo sharing

**Optional / variant** — depends on product philosophy, era, and segment:

- medication lists, document storage, care plans, wellness journaling
- AI assistance (answering caregiving questions, turning updates into next steps)
- a funded human care-navigation service layered on the app
- account-free access by shared code; searchable public teams
- gift cards and greeting-card sending

## Interfaces

Described conceptually; exact names and layouts vary by product.

### Circle home / dashboard

The entry surface for the whole space.

- the person being cared for and the situation description
- upcoming occasions and open needs, latest updates
- primary actions: post a need, add an event, post an update, manage members

### Care calendar

The "when" surface.

- dated events and needs: appointments, meals, rides, visits, occasions
- who has claimed what; open slots
- primary actions: create event, assign members, claim/sign up, edit or delete

### Needs / task list

The "what is needed" surface.

- open and filled needs, often grouped by kind (meals, rides, visits, errands, household tasks)
- primary actions: list a need, sign up, withdraw, mark fulfilled

### Updates feed / journal

The "stay informed" surface.

- reverse-chronological updates, check-ins, photos, announcements, notes of support
- primary actions: post an update, comment or send well wishes, attach a photo

### Members & roles

- the circle's roster, grouped as the coordinator arranges (family branches, teams, congregations)
- primary actions: invite (email/text/link/code), approve, group, remove, set organizer rights

### Records (where offered)

- medications (today's list, reminders), documents (folders), care plans, wellness journal
- primary actions: add/edit entries, set reminders, view history

## Important Rules / Behaviors

### Membership is the privacy boundary

The space is private by construction: what is posted is visible to the invited circle, not to the public or to other circles on the platform. Invitation or a shared access code is how people get in. This matters because the content — health condition, family logistics, photos — is intimate. Mature products let the coordinator control who is admitted and, in some products, what role-based permissions each invitee has.

### Claims are visible commitments

When a helper signs up, the commitment becomes visible to the whole circle — as do unfilled needs. The product's value comes from this shared visibility: no duplicate casseroles, no forgotten rides, and no single relative quietly absorbing everything. Some products additionally show what *others* are planning (e.g., what meal someone else is bringing) so helpers can coordinate with each other.

### The coordinator acts on behalf of others

Coordinators routinely post needs the recipient did not ask for and manage the space while the recipient is unwell. Products therefore allow one member to create, edit, or delete entries for others, and to add fellow organizers as the circle grows.

### Participation must be low-effort

Helpers are occasional users, often older, sometimes joining rarely. Products lower the barrier accordingly: joining by invitation link or a simple page code, acting directly from email reminders, and (in some products) using the space without creating a full account. If participating requires real effort, the circle quietly dies — this constraint shapes much of the interaction design.

### The space outlives the crisis

Updates, messages, and history persist. Families return to read the record after recovery — or after a death — and the same space can wind down or pivot to a new phase of care. There is no formal "closed" state in most products; the circle simply goes quiet.

## Variants

Common shapes the Type takes:

- **Family-organized caregiving app** — the full "command center": circle + calendar + needs + medications + documents + journal; free core with paid plans.
- **Community-organized care team** — centered on meals, rides, and encouragement; used by siblings of an aging parent, by new parents, or by a church/community group organizing a meal train; free.
- **Volunteer signup-sheet style** — the oldest and lightest form: a coordinator lists needs, helpers sign up online, the recipient points people to the page; access by simple page code rather than accounts; often organized by congregations and neighbors around illness, recovery, deployment, or a birth.
- **Service-augmented platform** — the family app plus a funded human layer: dedicated care navigators, hotlines, curated content and support groups, paid for by employers, health plans, or public programs while remaining free to the family.
- **Professional-inclusive circle** — paid or professional caregivers invited as members who post daily notes alongside family.

A variant remains a variant of this Type as long as the four core properties hold. A product that drops the care-recipient-centered container (household-wide logistics) becomes a family organizer; one that replaces the known circle with stranger matching becomes a marketplace; one that drops the express-and-claim loop becomes a journal or communication tool.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Family Organizer | closest sibling in the same category | centered on the *household* (chores, shopping, everyone's calendar); no care situation, no helper circle crossing household boundaries |
| Babysitting / Home Services Marketplace | adjacent | two-sided matching of strangers with booking and payment; here members are already-known people mobilized for free |
| Care Coordination Platform (healthcare) | name neighbor, different operator | provider- or payer-operated clinical coordination over patient populations; this Type is family-operated informal care |
| Patient Portal / Telehealth | adjacent | clinical systems operated by providers; a care-coordination app may reference appointments and medications but keeps no clinical record of record |
| Childcare Management System / Daycare Management | adjacent | manages a care *business* (enrollment, staff, billing, classrooms) for many children; this Type coordinates circle care for one person |
| Parenting / Baby Tracking Application | adjacent | logs a child's feeding and sleep for the parents; no helper circle and no needs-claiming loop |
| Home Care Agency Management | adjacent | agency-side scheduling and administration of paid staff; here the family self-organizes its own helpers |
| Team Messaging / Community Chat | structural neighbor | both are private group communication; they lack the care-recipient-centered container and the express-and-claim care loop that define this Type |

## Representative Products

- **Caring Village** — family caregiving app built around a care-recipient-centered "village"; calendar, to-dos, medications, documents, messaging, wellness journal.
- **Lotsa Helping Hands** — long-running free service for organizing help around "someone in need"; care calendar with task sign-up, announcements, well wishes.
- **CareCalendar** — free signup-sheet-style coordination pages organized by a coordinator (since 2002); needs list, online sign-up, news updates; widely used by congregations and communities.
- **ianacare** — family care navigation app (team, "who can help?" needs, calendar coverage, updates) with an optional human care-navigator service funded through employer and health-plan benefits.

The core model was checked against the oldest available form (a 2002-era, account-light, volunteer-organized signup sheet) to avoid defining the Type by today's app-era feature set.

## Sources

Research date: **2026-09-07**

- Caring Village — homepage and feature page: https://www.caringvillage.com/ , https://caringvillage.com/app/
- Lotsa Helping Hands — homepage and official knowledge base (community setup, roles, calendar and tasks): https://lotsahelpinghands.com/ , https://lotsa.helpscoutdocs.com/
- CareCalendar — homepage (roles, needs types, access model): https://carecalendar.org/
- ianacare — homepage (solution, benefit-funded navigator service, user accounts of usage): https://www.ianacare.com/

> Sourcing note: all four products were studied from their official sites and, for one product, its official support knowledge base. In-app screens and fine-grained permission settings were not directly exercised; precise operational limits, plan details, and vendor-claimed usage counts are therefore intentionally omitted. One additional candidate product could not be reliably identified online (name collision with an unrelated company) and was excluded; the remaining four samples span the Type's main shapes and eras.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
