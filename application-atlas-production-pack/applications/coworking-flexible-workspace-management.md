# Coworking / Flexible Workspace Management

## Overview

A **Coworking / Flexible Workspace Management** application is the operator-side system of record for running a shared-workspace business. It manages the operator's space inventory (desks, offices, meeting rooms at one or more locations), the members who hold recurring memberships to use that space, the bookings and desk/office assignments that connect members to space, and the billing of memberships and usage.

It solves a specific operational problem: a flexible-workspace business sells access on short, changing terms — month-to-month plans, day passes, hourly meeting rooms, teams that grow and shrink — rather than fixed leases. The application keeps the commercial relationships (who has what plan), the physical reality (which desk, office, or room is used by whom and when), and the money (recurring invoices, usage charges, payments) in one continuously reconciled system.

The defining core is small:

```text
Space inventory (locations → bookable / allocatable units)
        ▲
        │ used via bookings and standing assignments
        │
Member ── holds ──▶ Recurring membership (plan-based, flexible terms)
        │
        └── billed for ──▶ Memberships + usage → Invoices → Payments
```

Remove the space inventory and it becomes membership-billing software. Remove the members and billing and it becomes an occupant-side desk/room booking tool. Remove the usage layer and it becomes a subscription-billing platform. All four structures together are what make the Type.

## Users & Context

**Primary users — the operator's staff:**

- **Community / space manager** — the daily operator: signs up members, assigns desks and offices, handles bookings and access problems, chases payments, runs events. This role lives in the admin console and often the front desk.
- **Operator owner / manager** — watches occupancy, revenue, and member growth; configures plans, pricing, and locations.
- **Multi-site operations staff** — in larger networks, manage settings, billing entities, and reporting across locations from a central level.

**End users — the operator's customers:**

- **Members** — individuals or companies (teams) holding plans; they book rooms and desks, check in, view and pay invoices, and use the community directory through a member portal or branded mobile app.
- **Team admins** — a member designated by a company to manage its team's seats and sometimes its bookings.
- **Non-members** — day-pass users, external meeting-room renters, event attendees, and visitors; they interact through public signup pages and check-in surfaces rather than full membership.

Typical context: independent coworking spaces, multi-location flexible-workspace brands, serviced-office and executive-suite operators, landlords converting floors to flexible use, and — per the market itself — adjacent shared-space businesses (co-warehousing, shared kitchens, medical coworking, shared studios) that run on the same model.

## Core Model

### The defining structures

**1. The space inventory.** The operator's space is modeled as one or more **locations**, each decomposing into floors or zones and then into named **workspace units**: desks, private offices, meeting rooms, and functionally equivalent bookable or allocatable units. Units come in two operating modes that coexist in every mature product:

- **Bookable units** — reserved for time slots (a meeting room for two hours, a hot desk for a day). Bookings carry pricing rules of their own.
- **Allocatable units** — assigned on a standing basis to a member or team for the life of a membership (a dedicated desk, a private office). Allocation is tied to the membership, not to a calendar slot.

Many products also render the space as a **floor plan**, placing units on a visual map; assignment and booking can then happen on the map itself.

**2. The member and the membership.** A **member** is a person (or an organization — company/team — represented as a customer record with people attached) holding an active **membership**: a recurring subscription created from a **plan**. The plan is the offer; the membership (some products call it a contract) is the live instance with its own dates, price adjustments, and included entitlements. What makes the terms "flexible" rather than lease-like is structural: memberships recur on short periods (typically monthly), can be paused, changed, or ended on short notice, and can be seated per person or per team. The person↔organization relationship matters commercially: a team usually has one paying entity and several covered members, with a designated team admin.

**3. The usage record.** Every use of the space is a record connecting a member (or an authorized non-member) to a unit:

- a **booking** — a time slot on a bookable unit, optionally priced, optionally requiring approval, optionally carrying extras (catering, equipment);
- an **assignment** — a standing allocation of an allocatable unit to a membership;
- a **check-in** — a record of physical presence, whether manual, kiosk-based, Wi-Fi-verified, or driven by door access.

The membership's terms govern usage: member-vs-non-member rates, included credits (hours or money) consumed by bookings, passes that grant entry, and access permissions that decide which doors or resources a plan unlocks.

**4. Operator billing.** The system generates **recurring invoices** for each membership on its billing cycle and charges for usage beyond entitlements, then records **payments** through integrated gateways (card and direct-debit rails) or manual methods. Because occupancy and billing must reconcile continuously, mature products carry a real accounts-receivable layer: proration for mid-cycle changes, credits and corrections, deposits, taxes per location, and payment-failure handling.

### Standard capabilities around the core

Mature products across the market reliably add:

- **Member self-service** — a portal and/or branded mobile app for booking, check-in, invoices, payments, profile, and directory.
- **Entitlement mechanics** — credits (time or money), passes, and plan-scoped rates that make "what your plan includes" executable rather than descriptive.
- **Day-pass and external revenue** — selling passes and meeting-room time to non-members, with public purchase flows.
- **Presence and access** — check-in surfaces (kiosk, app, front desk, Wi-Fi), "who's in today" views, and integrations that translate plan state into door and Wi-Fi access.
- **Light CRM** — leads, tour requests, opportunities, and conversion paths from contact to member.
- **Visitor management** — registering, notifying, and checking in guests of members.
- **Community surfaces** — member directory, events and ticketing, messaging or feeds.
- **Analytics** — occupancy, utilization, member growth, revenue, with exports.
- **Integration spine** — payments (cards, direct debit), accounting systems, calendars, access hardware, and public APIs.

These capabilities are near-universal in current products, but they are the practical machinery of the business, not the definition of the Type — older or leaner operations have run the defining core without them.

### One structure, several implementations

```text
Concept:  plan vs active membership
Realizations: two explicit objects (plan → contract / billing plan → membership)
              or one plan object carrying term settings per member

Concept:  usage pricing
Realizations: rate tables per unit type, member/non-member tiers,
              included credits consumed per booking, flat inclusions

Concept:  presence
Realizations: manual front-desk check-in, tablet kiosk, Wi-Fi authentication,
              RFID/card readers, door-access integration
```

## How It Works

### Set up the business

```text
Create location(s)
→ define workspace units (bookable and/or allocatable) and pricing
→ create plans (term, price, included entitlements, access rights)
→ configure taxes, payment methods, invoice settings
→ connect integrations (payments, accounting, access control)
```

This order mirrors how operator-side products structure their own onboarding.

### Run the member lifecycle

```text
Lead / tour request
→ contact record
→ plan selection (self-serve signup or staff-created)
→ approval if required
→ active membership (plan instance with dates and entitlements)
→ changes: upgrade/downgrade, price adjustment, pause/freeze
→ cancellation or end of term
→ (reactivation, or archive)
```

A person without an active membership is typically kept as a contact — the pool from which future members come. Companies get the same lifecycle at team level, with a paying entity and seat management.

### The daily loop

```text
Members book rooms/desks (or use assigned ones) and check in
→ the system prices bookings against rates, credits, and passes
→ staff see who is in, what is occupied, what needs attention
→ doors and Wi-Fi honor plan state via access integration
→ usage charges accrue to member accounts
```

### The billing cycle

```text
Billing run (typically monthly, per member's cycle)
→ recurring invoice: membership + allocated units + accrued usage − credits
→ automatic charge via stored payment method, or delivery for payment
→ failures and reminders handled; access consequences are policy, not automatic
→ corrections: credits, refunds, re-invoicing where rules allow
→ payments reconciled into accounting
```

## Interfaces

**Admin / operations console** (web) — the operator's home. Dashboards surface occupancy, who is checked in, membership changes, and outstanding invoices. Sections cover members and companies, bookings and the calendar, billing and invoices, plans and inventory, leads, visitors, and reporting.

**Booking calendar** — day/week view of bookable units with per-unit pricing and rules; members book through their own surfaces while staff manage, approve, and edit bookings here.

**Member portal / branded mobile app** — the member's surface: book and check in, view plan and entitlements, see and pay invoices, connect with the directory, register visitors.

**Front-desk and embedded surfaces** — check-in kiosks, visitor sign-in, room displays outside meeting rooms, and tablet or web widgets; in several products these are companion apps rather than core screens.

**Public web surfaces** — plan signup forms, day-pass purchase, public meeting-room booking, and tour-request forms embedded on the operator's website.

**Inventory / settings** — locations, floor plans, units, plans, rates, taxes, and integration configuration. This is where the space inventory and commercial offers are defined.

## Important Rules / Behaviors

- **Entitlements gate usage.** What a booking costs — or whether it costs anything — is determined by the membership's plan: member vs non-member rates, included credits consumed before paid rates apply, and passes required for entry. Changing a plan changes what the member can do.
- **Assignment and booking are distinct commitments.** An allocated desk or office is occupied for the membership's term and shows in occupancy counts; a booking is a transient claim on a unit with its own cancellation and no-show rules. Some units can support both modes.
- **Memberships are living agreements.** They can be paused, repriced, upgraded, or moved between units mid-cycle; billing prorates or schedules changes according to product rules. Cancellation typically respects the current paid period.
- **Billing correctness has its own controls.** Recurring invoices are generated by scheduled billing runs; corrections happen through credits, refunds, or re-invoicing rather than editing history; deposits are held against the membership and commonly credited at cancellation.
- **Payment failure does not automatically lock the door.** At least one established product documents that access is not revoked automatically on failed payment, leaving that decision to staff; access consequences of billing state are operator policy, and the software's role is to surface the state.
- **Approval is a lever, not a constant.** Self-serve signups and bookings can flow straight through or wait for staff approval, depending on how the operator configures the space.
- **The record taxonomy is deliberate.** Members, contacts (non-member people), teams/companies, visitors, and leads are different record types with different rights — only members hold memberships; visitors never get accounts by default; leads exist to convert.

## Variants

- **By business mix** — membership-dominant operators vs day-pass/external-booking-heavy operators; some add virtual-office and mail-handling as a distinct product line.
- **By scale** — single space vs multi-location network; networks add central settings, cross-location membership, and consolidated reporting.
- **By vertical** — the same four structures run co-warehousing, shared kitchens, medical coworking, shared studios/salons, makerspaces, and campus incubators; "workspace" in this Type means shared space generally, not only offices.
- **By philosophy** — automation-first products (lead-to-invoice workflow automation), community-first products (directory, events, feed as the point), and platform suites that wrap the core in sales, visitor, and analytics modules.
- **By edge case** — companies with long-term lease-like arrangements are supported by several products through long-period plans, shading toward property management without leaving the Type.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Workplace Management Platform / Desk Booking | adjacent | Occupant-side: a single company manages its own office for employees — booking mechanics are shared, but there are no members, memberships, or operator billing. Remove those → this Type. The same vendor offering both usually ships them as separate products. |
| Hotel Property Management System (PMS) | adjacent | Transient nightly stays with guest/room/housekeeping cycles vs recurring flexible memberships and work-pattern usage. Convert the relationship to per-night stays → Hotel PMS. |
| Commercial Property Management | adjacent | Lease-based tenancy, rent rolls, long fixed terms vs month-to-month plans and day passes. Lengthen the terms and switch to lease administration → Property Management. |
| Membership Management System | adjacent | Member records, renewals, and benefits with no space inventory or usage. Remove the space → Membership Management. |
| Venue Management System | adjacent | Event-driven space rental vs membership-driven flexible access. Remove recurring memberships → Venue Booking. |
| Amenity Booking Platform | weaker adjacent | Scheduling shared amenities for an existing resident population; no commercial membership layer. |
| Resource Calendar / Enterprise Resource Scheduling | capability overlap | Pure scheduling without the commercial layer; contained here as a capability. |
| Building Access & Visitor Management | integration surface | Consumed via integrations; not the system of record for the workspace business. |

The operator-vs-occupant line is the most important boundary: booking software can look identical on a screenshot, but this Type is distinguished by holding the commercial relationship (members, plans, billing) for space the operator sells.

## Representative Products

- Nexudus
- Cobot
- Optix
- OfficeRnD Flex
- Coworks

## Sources

Research date: **2026-09-07**

- Nexudus — product site https://www.nexudus.com/ ; Knowledge Base https://help.nexudus.com/ (incl. documentation index and Glossary: plans, contracts, members, contacts, teams, resources, rates, benefits, passes, check-ins, visitors, floor plans)
- Cobot — product site https://www.cobot.me/ ; Help Center https://helpcenter.cobot.me/en/ (Learn Cobot collection: plans, time passes, booking credits, resources, invoicing, payments, members & teams, analytics)
- Optix — product site and feature pages https://www.optixapp.com/ (membership plans, resource/desk/meeting booking, invoicing, check-ins)
- OfficeRnD Flex — product site https://www.officernd.com/ ; Flex Help Center https://help-flex.officernd.com/en/ (onboarding checklist; locations & resources; billing plans vs memberships; bill runs; invoicing)
- Coworks — product site https://www.coworks.com/ ; Help Center https://help.coworksapp.com/en/ (collections: Billing, Bookings & Events, Members & Teams, Occupancy, CRM)

> Sourcing note: Optix and Coworks were examined at product-site and help-center collection level rather than individual article level; mechanics claimed only from their marketing pages are stated generically in this document. Fine-grained billing rules (exact proration formulas, deposit behavior, compliance regimes) vary by product and region and are deliberately not asserted as universal.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
