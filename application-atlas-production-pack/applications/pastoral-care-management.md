# Pastoral Care Management

## Overview

A **Pastoral Care Management** application is the church-side system for organizing how a congregation cares for its people: it records who needs care, assigns that care to specific caregivers, records the care actually given — visits, calls, cards, conversations, prayers — and keeps the care moving through follow-up until the need resolves. Its records are treated as sensitive pastoral information, held under visibility restricted to those entrusted with the care.

The defining core is small. Three structures must be present together:

```text
Care need, anchored to an identified person
└── Assigned caregiving loop (named caregiver → contact → follow-up → resolution)
    └── Person-bound, visibility-restricted care record
```

- **Care need anchored to an identified person** — an illness, hospitalization, bereavement, absence, crisis, counseling need, or prayer request, recorded against a specific person from the congregation's people records. Guests and non-members can be care subjects too.
- **Assigned caregiving loop** — responsibility for the need is given to a named caregiver (a pastor, a staff member, or a lay caregiver). The work appears on that person's list, contact is made, and follow-up continues until the need is resolved. Responsibility can be transferred or delegated.
- **Person-bound, visibility-restricted care record** — every care contact becomes a durable note attached to the person's record, visible only to people with the appropriate care role, accumulating over time as the person's care history.

Remove the person anchor and it becomes generic task management. Remove the assignment and loop and it becomes a prayer list. Remove the record and the loop becomes ephemeral to-do tracking. Remove the visibility restriction and the pastoral-confidentiality dimension collapses into ordinary contact notes.

The dominant packaging today is inside a Church Management System — either as a named care module or as care workflows configured over the church's people records. The packaging varies by product; the care loop itself does not.

## Users & Context

Primary users:

- **pastor / care pastor** — carries or supervises the care load; reads the care history before and after contact
- **ministry assistant or care coordinator** — receives care needs, creates care items, routes assignments to the right caregiver
- **lay caregivers** — deacons, elders, visitation teams, care-team volunteers; typically hold limited system access scoped to the people they serve

Secondary users:

- **small group leaders** — often the closest point of care; care may be routed to them
- **church members** — as subjects of care and, in many products, as submitters of prayer requests

Typical situations that generate care work: a member hospitalized, a death in a family, a family that has stopped attending, a first-time guest to follow up, a homebound member needing regular visitation, a counseling conversation, a prayer request submitted by a member. The work happens at bedsides, homes, and coffee shops — which is why mobile access to care lists and records is a common companion capability.

## Core Model

### The care need

The unit of work is a care need bound to one person: "check on this family," "visit this hospitalized member," "follow up with this guest." One need involves one care subject; when many people need the same contact (for example, Sunday's guests), the system holds one care item per person rather than one shared item. A need reaches the system by referral (staff or leader enters it), by detection (an attendance lapse or a form), or by self-submission (most commonly a prayer request). Categories — hospitalization, bereavement, new guest, prayer request, and similar — are commonly attached to make care searchable and reportable.

### The caregiver and the assignment

Care work is assigned to people, and the assignment has structure: someone records the need, someone is responsible for seeing it done, and someone actually makes the contact. These can be the same person or three different people. Responsibility is transferable — a coordinator may pass a need to a group leader, who may keep it or hand it to a lay caregiver. In documented implementations the assignee may accept or decline, and the responsible people are notified as the work changes state. The care item stays visible on the caregiver's work list until it is done, and stays visible on the care subject's record while it is open.

### The care record

The contact itself — a personal visit, a phone call, a card or letter, a counseling conversation — is recorded as a note attached to the care subject's record, with the date of contact, who recorded it, and usually a category. In documented implementations, completing a care assignment requires recording the contact: the note is the deliverable, not an afterthought. Notes accumulate on the person's record as the person's care history — what happened, when, and by whom — which is what allows the next caregiver to catch up on the person's situation before making contact.

### Visibility and confidentiality

Pastoral records are sensitive by nature, and the visibility model reflects that. Records can be restricted so that only holders of a specific care role can see that a contact even happened; unrestricted records remain visible to ordinary staff access. Person-level confidential fields (for example, confidential notes held directly on the person record) follow the same pattern. Some products additionally mask sensitive note content from users without clearance. The design intent is consistent across the sample: sensitive information stays with the people entrusted with the care.

### Prayer requests

Prayer requests form a parallel capture surface alongside the care loop. Members commonly submit requests (often anonymously) through the church's app or website; staff review them before anything is shared more broadly; approved requests flow into prayer lists or prayer streams. Prayer requests frequently become care needs when they reveal a situation requiring contact.

### One structure, many implementations

The core model is conceptual. Products realize each piece differently:

```text
Concept:              Care need
Implementations:      a named care task; a workflow card in a configurable workflow;
                      a flagged/annotated person record

Concept:              Caregiver assignment
Implementations:      task assignee with owner/creator roles; workflow step assignee;
                      a care group with leaders

Concept:              Care record
Implementations:      a care note tied to the contact; a general person note with
                      categories; a workflow record

Concept:              Visibility restriction
Implementations:      role-restricted tasks and notes; permission-scoped person
                      fields; masked note content
```

A reader who has only seen one implementation — say, a care-tasks module — should be able to recognize a church running its pastoral care through configured workflows and masked notes as the same Type.

## How It Works

The typical care loop runs as follows:

```text
A need surfaces (referral / attendance signal / form / prayer request)
→ a coordinator records the care need about a specific person
→ assigns it to a caregiver (or transfers it to someone who will)
→ the caregiver is notified and accepts the care item
→ contact is made (visit / call / card / conversation)
→ the caregiver records the contact as a note on the person's record
  (restricting visibility if the content is sensitive)
→ a follow-up is scheduled or created
→ the loop repeats until the need resolves
```

Around this loop sit several recurring activities:

- **Guest and absence care** — guests from a service become one care item each; members whose attendance lapses can trigger care items automatically in products with workflow automation.
- **Oversight** — a care pastor or coordinator reviews open and overdue items, filters the care record by person, category, caregiver, or date, and reports on care activity (who has been visited, what is incomplete, which ministry areas need attention).
- **Prayer handling** — submitted prayer requests are reviewed, approved for sharing where appropriate, and prayed over; the prayer stream runs alongside visitation care.

The loop is intentionally continuous: open care items do not quietly disappear. They remain visible on the caregiver's list and on the person's record until they are completed and recorded.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Care worklist

The caregiver's home surface: the care items assigned to them, with what requires action surfaced first. Typical information: person, need, due date, status, who assigned it. Primary actions: accept, decline (with reason), complete by recording the contact.

### Person record care view

The care history lives on the person's record, not in a separate silo. Typical information: open care items about this person, past care notes with dates and authors, sometimes family context and engagement signals alongside. Primary actions: create a care need, add a care note, create a follow-up. This is also where a caregiver catches up on the person's situation before visiting.

### Care search and management

The coordinator's surface for the whole care record: filter by category, caregiver, person, date range, and completion state; manage items in bulk; export. It answers questions like "who has incomplete visits this month?" and "what care touched this family last quarter?"

### Prayer request review

Where member-submitted prayer requests arrive: read, approve or hold before broader sharing, route to prayer lists, and (where offered) let members mark prayers as prayed.

### Mobile care surface

A companion view for care done away from a desk: see assigned care items, record the visit or call afterwards, and add notes on the spot.

## Important Rules / Behaviors

- **Confidentiality is structural, not incidental.** Care records can be restricted to specific care roles; guidance in the most deeply documented implementations warns explicitly against recording confidential content outside that restriction. In at least those implementations, once a record is restricted, users without the role cannot even see that a contact occurred. Staff-level access does not automatically equal access to restricted pastoral records.
- **The record is the deliverable.** In documented implementations, a care assignment is completed by recording the contact that was made — the note lands on the care subject's record, and the assignment cannot be closed without it. This keeps the care history complete by construction.
- **Open care stays visible.** Incomplete care items persist on both the caregiver's work list and the care subject's record until completed; they are findable by coordinators. Care that is assigned but never recorded is detectable.
- **One need, one person.** Care items are about a single person; bulk needs (guest follow-up after a service) are realized as per-person items so each person's care history is complete.
- **Care attaches to people, wherever they are in the church's records.** Guests and non-members can be care subjects; membership is not a prerequisite for care.
- **Responsibility is delegable.** Ownership of a care item can transfer without losing the record; delegation chains (coordinator → group leader → lay caregiver) are a common pattern in larger churches.

## Variants

- **Named care module** — a productized care feature inside a ChMS, with its own tasks, notes, categories, and visibility controls (the deepest-documented realization in the sample).
- **Configured care workflows** — the same loop built from a general workflow engine over people records: cards move through steps, assignees change, follow-up steps repeat. Common in workflow-centric platforms; a major modular ChMS ships no named care product at all and realizes care this way.
- **Record-level care** — care recorded as sensitive notes and confidential fields on person records under permission controls, with lighter or no dedicated care-item machinery; observed in a non-US market product.
- **Small church vs multi-staff** — a single pastor's notes and prayer list at one pole; at the other, care pastors, coordinators routing assignments, engagement dashboards that flag drifting members, and case-like management of complex ongoing situations.
- **Tradition shapes** — evangelical follow-up culture (guest care, attendance-triggered care, prayer streams) vs parish visitation traditions (homebound and elder/parish-district visitation) vs institutional chaplaincy in hospitals and militaries, which shares the personal-care grammar but belongs to a different institutional owner and is documented in healthcare-system territory rather than here.
- **Benevolence extension** — assistance funds and material aid tracked alongside relational care in some products.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Church Management System / ChMS | host environment; broader | ChMS operates the whole ministry system — membership, giving, groups, events, check-in, communication. This Type centers only the care loop, which a ChMS may or may not productize; a modular ChMS can exist without it, and the care loop can exist as a standalone slice of one. |
| Congregation Membership Management | substrate | The roll holds who the people are and their membership status; this Type holds what the church does for people in need. Membership status is not required for care — guests receive care too. |
| Ministry Scheduling | shares assignment grammar | Scheduling centers rosters of volunteers for services and roles; this Type centers the care need and its loop. Care-team rotations borrow the scheduling grammar without changing centers. |
| Religious Small-group Management | delivery context | Groups are often where care happens (care is frequently routed through group leaders), but groups center community life and membership, not individual care needs. |
| Care Plan Management (healthcare) | name-adjacent, structurally distinct | Clinical care plans hold assessments, goals, interventions, terminology, orders, and clinical outcomes under healthcare governance. Congregational care holds visits, calls, prayer, and counseling under church governance, with no clinical machinery. |
| Social Services / Nonprofit Case Management | workflow-shape sibling | Case management centers a case record with assessment, service plan, eligibility, and program/benefits context, reported to agencies or funders. Pastoral care centers person-level care relationships delivered relationally, with no eligibility or benefits machinery. Large churches' care ministries can take case-like shapes, but the absence of program/eligibility machinery is the practical test. |
| CRM | object overlap | Tasks and notes exist in CRMs too. What distinguishes this Type is the congregation context, the care-need semantics, and the structural confidentiality expectation. |

## Representative Products

- **TouchPoint** — enterprise ChMS whose "Tasks & Notes" is sold as named pastoral care software, with the care machinery documented at operational depth
- **Rock RMS** — open-source ChMS realizing pastoral care through configurable workflows, connection follow-up, and a dedicated prayer subsystem
- **Planning Center** — modular ChMS with no dedicated care product; care realized through People workflows, masked notes, and member-side prayer requests
- **ChurchTools** — German-market ChMS where care-adjacent work runs through people follow-ups, groups, and permission-scoped records
- **Churchteams** — mid-market suite representing the automation-based realization without a named care module

## Sources

Research date: 2026-09-08

- TouchPoint — Pastoral Care Software (feature page): https://www.touchpointsoftware.com/features/pastoral-care-software/
- TouchPoint — Tasks & Notes documentation (section index; Tasks; Add a Note; Tracking Tasks and Notes; Confidential Comments as Extra Values): https://docs.touchpointsoftware.com/
- Rock RMS — homepage and features: https://www.rockrms.com/ , https://www.rockrms.com/rock-features
- Planning Center — homepage and product list: https://planning.center/
- ChurchTools — Help Knowledge Base, Modules: https://churchtools.academy/en/help/churchtools-modules/
- Churchteams — homepage: https://www.churchteams.com/

> Sourcing limitations: a standalone care-ministry specialist (CareNote) could not be reached (repeated transport errors), and general search engines were unavailable or regionally redirected during this pass — the market scan is therefore incomplete, and no standalone-product claims are made. Evidence for the care machinery is deepest for TouchPoint (operational documentation tier); for the other products it rests on official product pages and help-structure indexes, so their operational specifics are described only at the strength those sources support. Detailed evidence and per-product observations are recorded in the paired Research Notes.
