# Building Access & Visitor Management

## Overview

A **Building Access & Visitor Management** application is the software layer that controls and accounts for the movement of people across a building's controlled boundary.

It does two connected jobs:

- **Building access** — it turns the places where people physically enter (doors, gates, turnstiles, elevators, lobbies) into managed decision surfaces: each crossing attempt is verified against configured rules, allowed or refused, and recorded.
- **Visitor management** — it gives temporary visitors their own path through that boundary: pre-arrival registration, check-in on arrival, notification of the person being visited, a badge or temporary credential, and a recorded departure.

The defining core is small:

```text
Managed entry points
└── Identified person at the boundary
    ├── Occupant (persistent authorization, carried by a credential)
    └── Visitor (bounded authorization, created by registration/check-in)
└── Grant / deny decision under configured rules
└── Recorded entry event (live monitoring + persistent audit record)
```

Everything else commonly associated with the category — mobile credentials, badge printing, kiosks, watchlist screening, video intercoms, elevator control — is standard market capability layered on this core, not what makes the product what it is. Older and simpler products (card-and-panel systems with a visitor logbook, intercom-and-fob residential systems, tablet-based digital sign-in sheets) fit the same core without any of the modern specifics.

When the product stops deciding and recording entry — for example, when it only books space, tracks work hours, or automates building plant — it has crossed into a different Application Type.

## Users & Context

Primary operating users:

- **Security and facility administrators** — configure entry points, access rules, schedules and credentials; monitor live activity; investigate incidents; run lockdown.
- **Front desk / reception staff** — greet and check in visitors, issue badges, manage unexpected arrivals, sign visitors out.
- **Office / property managers** — oversee the person population (employees, tenants, residents), delegate hosting rights, review reports for compliance and utilization.

Primary participating users:

- **Occupants** — employees, tenants, or residents who unlock doors with a credential day to day, and often invite their own guests.
- **Visitors** — interviewees, contractors, clients, delivery personnel, event guests — who register before arrival or check in on arrival, and interact with a check-in form, kiosk, or intercom rather than a full console.

Typical contexts: commercial offices, multi-tenant commercial real estate, multifamily residential buildings, coworking spaces, industrial and warehouse sites, schools, clinics and government buildings. The workflow is the same everywhere; the balance between the access pole and the visitor pole, and the depth of compliance tooling, varies by context.

## Core Model

### Entry point

An entry point is a managed software object standing in for a controlled physical crossing — a door, gate, turnstile, elevator bank, vehicle lane, or an attended lobby. Each entry point is bound to control hardware (an electric lock, magnetic lock, or wireless lock driven by a controller and a reader) or to an admission surface (a check-in kiosk or reception desk that admits visitors). The entry point is the anchor of the whole model: rules, schedules, credentials, and event records all attach to it.

### Person: occupants and visitors

Every person who crosses the boundary exists in the system as a person record, in one of two classes:

- **Occupant** — a persistently authorized person (employee, tenant, resident, staff member). Their authorization is standing: it lasts as long as their role or lease, and it is exercised by presenting a credential.
- **Visitor** — a temporarily authorized person. Their authorization is bounded: it is created by an invitation or registration, exists for a defined visit or time window, and is explicitly ended by sign-out, deactivation, or expiry. A visitor record links the person to a **host** (the occupant they are here to see), a purpose, and the visit's timestamps.

### Credential

A credential is the identity carrier an occupant (or sometimes a visitor) presents at the entry point. Products commonly support several form factors side by side: physical cards and fobs, PIN codes, mobile-app unlocks, QR codes and access links, wallet passes, biometric face recognition, and license-plate recognition for vehicle entries. Conceptually the form factor does not matter; what matters is that the credential binds a person to a verifiable token evaluated at the boundary.

### Access rule set

Access is decided by a rule set that combines:

- **Access groups / access levels** — the standard mechanism binding persons to sets of entry points. An admin assigns a person to a group; the group is granted particular entry points. Group membership, not one-off grants, is how buildings are administered.
- **Schedules** — time windows that gate when an entry point or a group can open: business-hours unlock schedules, restricted-hour access for certain groups, holiday calendars, and temporary overrides.
- **Visitor authorization state** — for the visitor pole, the rule set is the visit itself: who is invited, by which host, for what purpose, valid from when until when, and possibly gated by screening or approval.

### Decision

For each crossing attempt the system makes a grant/deny decision: automated credential verification for occupants; an admission decision at check-in for visitors — sometimes fully automated, sometimes mediated by reception staff or a formal approval workflow. The decision is the product's reason to exist; everything else records or administers it.

### Event and visit records

Every entry (and, where supported, exit) becomes a persistent record: who, where, when, granted or denied, by which credential — the audit trail and the live feed are the same data seen at different moments. The visitor's record additionally carries the visit's lifecycle: registration, check-in, agreements signed, badge issued, host notified, sign-out.

```text
Occupant path:
Person → assigned to Access Group → granted Entry Point(s) under Schedule
→ presents Credential → decision → Entry event

Visitor path:
Invite / Pre-registration (host + purpose + validity)
→ arrival → Check-in (fields, photo, ID, agreement, screening)
→ Host notified → Badge / temporary credential for the visit window
→ Sign-out / expiry → Visit record retained
```

## How It Works

Three loops cover the life of the system.

### 1. The occupant authorization loop

```text
Add person (directory invite, CSV import, or HR/identity sync)
→ assign to access group(s)
→ group holds entry points + schedules
→ issue credential(s)
→ person badges/unlocks; each attempt is decided and recorded
→ on role change or departure: adjust group or deactivate credential
```

Administering a building is mostly editing groups, schedules, and the person population — not touching doors. Deactivating a lost credential, and issuing a replacement, is a routine transaction; the old credential must stop working immediately.

### 2. The visitor visit loop

```text
Before arrival:
  host (or admin) invites the visitor — name, host, purpose, date/validity
  and/or the visitor completes pre-registration (details, documents, agreements)

On arrival:
  visitor checks in — at a kiosk/tablet, by scanning a QR code, or with reception
  → provides required details (name, contact, host, purpose)
  → may be photographed, have ID checked, or be screened against block/watch lists
  → may e-sign a legal agreement (NDA, waiver, safety briefing)
  → host is notified through email, SMS, or chat

During the visit:
  visitor wears a printed or digital badge
  and/or holds a temporary credential granting specific entry points for the visit window

On departure:
  visitor signs out (self-service, at the desk, or by reminder to the host)
  / the pass deactivates or expires
  → the complete visit record is retained
```

Two entry patterns coexist: **pre-registered** visitors (invited, fast-tracked, sometimes with a QR pass) and **walk-up** visitors (register on the spot, possibly requiring host approval before admission). Large or compliance-driven organizations add formal approval workflows between check-in and admission.

### 3. The operations loop

```text
Monitor live events (entries, denials, forced/held-open doors, device health)
→ respond: remote unlock, lockdown, dispatch, or investigation
  (often alongside camera footage of the same door event)
→ review history, exports and reports
→ adjust rules (groups, schedules, credentials, visitor policies)
```

Door hardware must keep deciding even when the network is down; products differ in how (local edge decisions, cached credentials, offline check-in modes), but a boundary that fails open or blind when connectivity fails is not acceptable for this Type.

### Capability tiers

**Defining core** — without these the product is not in this Type:

- managed entry points bound to hardware or admission surfaces
- identified persons (occupants and visitors) at the boundary
- grant/deny decisions under configured rules
- recorded entry/visit events for monitoring and audit
- visitor authorization that is bounded, host-linked, and explicitly ended

**Standard capabilities** — expected of mature products:

- access groups/levels and schedules
- multi-form credential management
- kiosk/tablet/QR check-in with configurable forms per visitor type
- host notifications, badge printing, visitor photos
- legal-agreement (NDA/waiver) e-signature at check-in
- visitor log with exports and long retention
- live event feed, remote unlock, lockdown, device health
- role model (admins, security, reception, delegated hosts, occupants)
- self-service (occupants unlock doors and invite their own guests)
- directory/identity integration (SSO, SCIM/HRIS sync)
- calendar-based visitor invites
- occupancy and entry-history reporting

**Optional / advanced** — depends on segment, region, and security posture:

- ID scanning and identity verification
- block lists, watch lists, and multi-step approval workflows
- video intercom with call routing at the entry
- elevator/floor control, turnstiles, parking and license-plate entry
- eviction/emergency mustering and mass notification
- deep compliance packs for regional regimes
- bundling with video surveillance, intrusion alarms, mailroom, or space booking

## Interfaces

The Type is unusual in having **four distinct audiences**, each with its own surface.

### Admin console (web)

The system of record for operators.

- purpose: configure and administer the boundary
- typical content: places/sites, entry points, access groups, schedules, persons, credentials, visitor policies, event history, reports
- primary actions: create/edit entry points and groups, assign persons, issue/revoke credentials, set schedules, review events, run lockdown, export audit data

### Live monitoring surface

The operational eye.

- purpose: see what is happening at the boundary now
- typical content: real-time entry/denial events, camera context where bundled, device status, active visitors
- primary actions: acknowledge alerts, remote unlock, lock down, tag incidents

### Check-in surface (kiosk / tablet / QR form / front desk)

The visitor's front door.

- purpose: register the visitor's arrival and trigger admission + hosting
- typical content: welcome screen, check-in form fields (name, contact, host, purpose), agreement e-sign, photo capture, badge printing status
- primary actions: check in, sign out, call for assistance; behind it, reception actions to admit, hold, or refuse a visitor

### Occupant mobile app / portal

The person-side surface.

- purpose: daily entry and self-service
- typical content: digital keys/credentials, places and entry points available to the person, their invited guests
- primary actions: unlock (in person or remotely), manage personal PIN, invite and track guests, receive notifications

## Important Rules / Behaviors

- **Group membership, not individuals, grants doors.** Person-level exceptions exist, but the administration model is group-based; deleting a person's group membership closes every door the group opened.
- **Schedules are part of the decision.** The same credential can open the same door at 10:00 and be denied at 22:00. Holiday calendars and overrides modify the base windows.
- **Visitor authorization is always bounded.** A visitor credential or pass has a validity window and/or a limited duration from check-in; it must end by sign-out, deactivation, or expiry. A visitor is never simply "added like an employee."
- **Ending access must be immediate.** Deactivating a lost credential or cancelling a visitor's pass takes effect at the boundary right away — this is the operational guarantee the product is bought for.
- **Denied and anomalous events are surfaced, not silent.** Denials, forced-door, held-open, and offline-device events reach the monitoring surface, because the record's value is in the exceptions.
- **Offline behavior is a design constraint.** Entry points continue to decide during network outages (locally cached rules/credentials or degraded modes); check-in may continue in offline mode and sync later.
- **The visitor record is a compliance artifact.** Log retention, agreement-version tracking ("which NDA version did this visitor accept"), and evacuation lists ("who is in the building") make the visit log a regulatory document, not just a convenience.
- **Screening can block admission.** Block/watch-list matches and approval workflows interpose a human or policy gate between check-in and admission; the visitor can complete check-in and still be refused.

## Variants

- **Access-first** — born as a door/security system, with visitor management added as a module or companion product. Common in enterprise security estates; often bundled with video surveillance and intrusion alarms.
- **Visitor-first** — born as a digital visitor logbook/reception platform, with the door layer reached through integrations with third-party access control systems. Common in enterprise workplace management; the boundary decision for visitors lives at the check-in surface.
- **Combined-native** — access, intercom, and visitors delivered as one product. Common in multifamily residential and small commercial buildings, where the entry intercom is both the access device and the visitor interface.
- **Residential / multifamily tilt** — tenant and resident populations, video intercom at building entry, standing delivery access for carriers, property-management-system integrations.
- **Commercial office tilt** — employee populations, calendar-driven meetings, reception desks, hybrid-work occupancy.
- **Compliance-heavy / regulated sites** — ID scanning, watchlists, formal approvals, regional legal regimes, audit-grade logs (government, schools, industrial, finance).
- **Deployment postures** — cloud-native, hybrid cloud with edge decision-making at the door, and modern software on top of legacy on-prem panels.
- **Scale extension** — same model applied to elevators, turnstiles, vehicle lanes and multi-site portfolios managed from one console.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Building Management System / BMS | adjacent in the building stack | BMS automates building plant (HVAC, lighting, energy); this Type decides and records *people* crossing the boundary. Remove people → BMS; remove plant → this Type |
| Space & Occupancy Management | adjacent | books *space and time*; this Type governs *crossing*. Occupancy reporting overlaps, the decision does not |
| Campus Card Management | adjacent (institutional) | person-centered credential across many campus services (dining, print, events, doors); door access is one downstream consumer. Boundary-centered vs person-services-centered |
| Time & Attendance | data handoff | owns work-time semantics (shifts, breaks, payroll); entry events may feed it, but entry *permission* is out of its scope |
| Hotel Front Desk / Hotel PMS | hospitality analog | guest registration is folio/stay-economics-centric with room-lock integration downstream; no stay or folio objects exist here |
| Workplace Management Platform | broader (partial overlap) | platforms spanning desks, rooms, deliveries, signage and communications may include visitor management as one module; the visitor module is the in-scope slice |
| Identity & Access Management / IAM (IT) | convergent neighbor | authenticates people for *digital* resources; this Type authorizes *physical* crossings. Shared directories and provisioning are convergence, not identity |
| Video Surveillance / unified security suites | companion | video supplies evidence context for entry events; many vendors bundle both — bundling does not merge the Types |
| Package & Mailroom Management | sibling (facilities) | tracks *objects* arriving; this Type admits *people*. Carrier standing-access is in scope; parcel logging is not |
| Amenity Booking / Meeting Scheduling | adjacent | reserves a time slot for a resource; this Type grants a boundary crossing. An amenity booking may be the *reason* for a visit, not the authorization itself |
| Event / Attendee Management | occasion analog | admits attendees against a ticket for an occasion; this Type admits people to a building under standing or visit rules. Events hosted in buildings create temporary overlap |

The most consequential boundary is with **IT IAM**: the two share person records, provisioning machinery, and increasingly credentials, and some vendors market their convergence. The test is the managed object — apps and sessions versus doors and visits.

## Representative Products

- **Kisi** — cloud access control with an integrated visitor registration flow (SMB/mid-market commercial office)
- **Swiftlane** — combined access control, video intercom, and visitor passes (multifamily residential and small commercial)
- **Envoy** — visitor-first enterprise workplace platform; door layer via third-party access control integrations
- **Verkada** — enterprise hybrid-cloud access control with a companion guest/visitor module
- **Brivo** — cloud access control suite spanning commercial real estate and multifamily, with visitor management in its unified platform

The defining core was checked against older and simpler patterns (card-and-panel systems with visitor logbooks, intercom-and-fob residential entries, tablet-era digital sign-in sheets) to avoid over-fitting the definition to the current cloud/mobile implementation.

## Sources

Research date: **2026-09-06**

- Kisi Product Documentation (access control, doors, visitor management, registration point, admin quick start) — https://docs.kisi.io/ , https://docs.kisi.io/access_control/ , https://docs.kisi.io/visitor_management/visitor_registration_point , https://docs.kisi.io/quick_start/admins/
- Swiftlane Help Center (admin collection, access groups, visitor passes) — https://support.swiftlane.com/en/collections/10329490-i-m-an-admin , https://support.swiftlane.com/en/articles/9810805-access-group-overview , https://support.swiftlane.com/en/articles/9810829-how-do-i-create-a-visitors-pass
- Envoy Help Center (Visitors collection; About Envoy Visitors) — https://envoy.help/en/ , https://envoy.help/en/collections/1930712-visitors , https://envoy.help/en/articles/3330129-about-envoy-visitors
- Verkada Access Control (official product page) — https://www.verkada.com/access-control/
- Brivo (official site; security suite, access control, visitor management) — https://www.brivo.com/
- Envoy platform overview (module architecture, access control integrations) — https://www.envoy.com/products

> Sourcing limitation: operational help-center documentation for Brivo (answers.brivo.com) and Verkada (docs.verkada.com) could not be fetched from the research environment on 2026-09-06 (repeated transport errors / access denial). Both products are therefore represented at positioning level only; no operational or numeric claims in this document rest on them. Precise figures observed during research that belong to individual products (plan quotas, single-use pass expiry windows, retention policies) were deliberately excluded from this document.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/market-sample breadth check are recorded in the paired Research Notes.
