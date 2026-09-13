# Nail Salon Management

## Overview

A **Nail Salon Management** application is the operating system for a nail salon: it manages the full life of a client visit — the catalog of bookable nail services with their durations and prices, the clients who receive them, the appointment that binds a client to a service and a nail technician at a time, and the checkout that turns the completed service into recorded revenue — together with the salon layer around the visit: client preferences such as nail shapes and colors, technician-level pricing and pay, walk-in handling, retail sales, and retention loops.

The defining structure is the same visit economy that underlies appointment-based service businesses in general — this Type is its nail-industry expression. What gives the nail variant its shape is the service vocabulary and the visit culture: catalogs built from manicure, pedicure, gel, acrylic, and color-change services; client records that remember preferences such as nail shapes and colors; booking that can carry design references and match the right technician; visits that may run two technicians in parallel; and a strong walk-in and group-visit tradition that the software serves with waiting rooms and express booking.

When the catalog reverts to hair services with color formulas and processing records, the product is salon management; when clinical intake, consent, and treatment documentation take over, it drifts toward med-spa or massage territory; when the software is built around the individual technician's own book and income rather than a managed salon, it becomes the beauty-professional packaging of the same family.

## Users & Context

The primary users are the **nail technicians** (often called nail techs or, in some products, providers or artists) and the **salon owner or manager**:

- **Nail technicians** — see their day's schedule, review the client's history and preferences (shape, colors, past services), perform the service, and hand off to checkout; in commission- and tip-based salons their pay is calculated from what they perform.
- **Salon owner / manager** — owns the service catalog and pricing (including per-technician price levels), staff schedules, policies, inventory, and the reports that run the business.
- **Front desk** (in busier salons) — books and moves appointments, greets walk-ins, runs the waiting list, checks clients out.

Secondary participants are the **clients**: they book through a booking page (usually without logging in), pay and tip — increasingly from their own phones — and return driven by automated rebooking prompts and reminders.

The work environment is the salon floor: technicians move between manicure tables and pedicure chairs, the calendar is the center of gravity, and walk-ins arrive without appointments. A distinctive rhythm of the nail business is the **parallel visit** — one technician working on a client's manicure while another handles the pedicure — and the **group visit** — friends or parties booked side by side.

## Core Model

The world of the application is the visit economy of an appointment-based service business, filled with nail-industry content:

```text
Client (person, persistent record with preferences and history)
   ↓ books
Service (catalog entry: duration + price, nail vocabulary)
   ↓ bound by
Appointment (client × service × technician × time)
   ↓ delivered under
Visit lifecycle (arrive → service → complete; cancel / no-show as named outcomes)
   ↓ resolves into
Checkout (payment, tips, retail; per-technician attribution)
```

### The defining core

- **Bookable service catalog** — the salon's menu of nail services, each with its own duration and price, organized in categories with add-ons (paraffin, callus treatment, designs) and bundles. The nail vocabulary (manicure, pedicure, gel, acrylic, shellac, color change) fills the catalog; it does not change its structure. Durations matter structurally: appointment slots are built from them.
- **Identified client records** — one persistent record per person: contact details, visit and purchase history, and the salon's notes on the client. In nail salons these notes carry the client's preferences — products name nail shapes, color combinations, and personal dates as the content worth keeping — so the salon can repeat last month's set.
- **The appointment** — the binding of a specific client to a specific service at a time with a specific technician. Technician availability is what makes a slot bookable; stations and pedicure chairs participate as shared resources. Cancellation and no-show are first-class outcomes, backed by deposits, cancellation policies, and cards on file.
- **Visit lifecycle** — the appointment is worked from booking through confirmation and arrival to completion; the record of what happened accumulates on the client.
- **Checkout** — the completed service is resolved into recorded payment in the same system: card payments, tips, package or gift-card redemption, retail products, and — because nail economics are per-technician — attribution of what was earned to the right technician.

Remove the appointment and catalog and only a client CRM remains; remove the checkout and the client ledger and only a scheduler remains. The five structures together make this a management system rather than a collection of tools.

### The nail layer

Around the visit, the researched products carry a consistent nail-industry configuration:

- **Nail service vocabulary** — the catalog and marketplace categorization are keyed on nail terms (manicure, pedicure, acrylic, gel, shellac, color change). Products recognize a nail salon by its service names.
- **Preference-type client content** — the client record holds what the salon must remember to reproduce a result: nail shapes, color combos, brands, birthdays. Unlike the massage and med-spa siblings, no treatment-note or consent-form culture was observed in this sample — the record carries preferences, not clinical documents.
- **Design-informed booking** — for salons offering custom nail art, clients can attach inspiration photos when booking, and the salon prices by service complexity and matches the design to a technician with the right specialization. Pricing is commonly tiered by technician experience, seniority, or specialized skills, so the same service can carry different prices per technician.
- **Two-technician services** — a single visit can involve two technicians working in parallel (the classic manicure-plus-pedicure pairing). The booking model supports a service performed by more than one provider, and group bookings put several clients side by side.
- **Walk-in and group culture** — waiting-room and express-booking machinery turns unscheduled arrivals into tracked visits (text a link, collect a card on file, notify when the technician is ready), and the checkout handles several clients from one group together.

### Standard capabilities

Capabilities carried by most mature products, though not what makes the product a nail salon manager:

- **Login-free online booking** on the salon's own booking page, with deposit, cancellation, and card-on-file policies built into the flow
- **Automated confirmations and reminders** by text and email; two-way messaging
- **No-show protection** — required deposits, cards on file, cancellation fees, blocking repeat offenders
- **Per-technician economics** — commissions, tips, hourly pay, payroll calculation; clients paying and tipping from their phones with earnings directed to the right technician
- **Packages, memberships, and gift cards** — sold up front, tracked per client, redeemed at checkout
- **Retail and inventory** — polishes, tools, and aftercare products sold in the same checkout, with stock tracking
- **Retention loops** — rebooking prompts at checkout, review requests linked to the salon's public profile, marketing campaigns
- **Reporting** — revenue, technician performance, utilization, no-shows, client retention
- **Multi-location support** for small chains and franchises

### One structure, many implementations

The core is written conceptually; products realize the same concepts under different names.

```text
Concept:          Technician
Implementations:  nail tech, technician, provider, artist, staff member, employee

Concept:          Client preference record
Implementations:  client notes and history (shapes, colors, formulas), profile tags, custom fields

Concept:          Per-technician pricing
Implementations:  per-provider price lists, tiered pricing by experience/seniority, complexity-based customizations

Concept:          Walk-in handling
Implementations:  virtual waiting room, express booking links with card-on-file, walk-in checkout, waitlist

Concept:          Parallel visit
Implementations:  multi-provider services, two-technician appointments, service bundles across providers
```

A reader who has only seen a large franchise chain on an enterprise platform should still recognize a solo booth-renting technician's setup from the core alone.

## How It Works

### Configure the salon

```text
Define the service catalog (manicure/pedicure/enhancement services with durations and prices,
categories, add-ons, per-technician price levels)
→ add technicians and working hours; set stations and pedicure chairs as resources
→ configure deposits, cancellation and no-show policies, packages, gift cards
→ set permissions (front desk / technician / manager)
```

### Fill the book

```text
Clients self-book online (no login) or book by phone / walk in
→ reminders and confirmations sent; deposits or cards on file captured where configured
→ walk-ins enter a waiting list or express-booking flow; the desk texts a link,
   collects a card on file, and notifies the client when their technician is ready
→ waitlist fills slots freed by cancellations
```

### Run the visit

```text
Client arrives; appointment checked in
→ technician opens the client record: history, preferences (shape, colors), photos
→ service delivered (one technician — or two in parallel for mani + pedi)
→ checkout: service price at the client's technician level, tips, retail,
   package/gift-card redemption; earnings attributed to the right technician
→ rebooking prompt before the client leaves
```

The defining loop is this one: the appointment drives the day, the client's preferences ride on the record, and the checkout closes the visit into per-technician revenue — all without leaving the system.

### Grow the book

A large share of the machinery exists to turn visits into regulars: automated rebooking prompts at checkout, reminder and win-back messages, review requests, referral and gift-card sales, and packages that prepay a series of visits. For walk-in-led salons, the waiting room and express booking are the growth surface; for appointment-led salons, it is the booking page and its policies.

### Core vs Common vs Optional

**Defining core** — without these, not this Type:

- bookable nail service catalog with duration and price
- identified client records
- appointment binding client × service × technician × time
- lifecycle through service delivery, with cancellation/no-show as named outcomes
- checkout resolving the visit into recorded money

**Common mature structure** — present in most modern products:

- login-free online booking with deposits and cancellation policies
- reminders, two-way texting, waiting list
- no-show protection
- client preference records (shapes, colors, history)
- add-ons, bundles, per-technician pricing, tips and commissions, payroll
- two-technician services and group bookings
- retail/inventory; packages, memberships, gift cards
- reviews, rebooking automation, reporting, multi-location

**Variant / optional** — depends on packaging, segment, and market:

- nail-art studio configuration (design photo intake, artist matching, complexity pricing)
- bundled consumer marketplace (present in some products, deliberately absent in others)
- booth-renter economics and instant payouts
- franchise/multi-location scale with centralized catalogs
- regional nail-only studios (evidence limited in this research)

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Calendar / appointment book

The operational center of the salon.

- typical information: technicians' days at a glance, appointment statuses, color coding, walk-ins and gaps
- primary actions: create/move/cancel appointments, check in, open the client record, run two-technician or group bookings, block time

### Client record

The person-centric surface everything attaches to.

- typical information: contact details, visit history, preferred nail shapes and color combos, photos, notes, packages and balances, saved payment methods
- primary actions: book, record preferences, take payment, message, view history

### Booking page

The client-facing surface.

- typical information: services with durations and prices (per technician), real availability, the salon's policies
- primary actions: book or reschedule, choose a technician, add-ons, upload design inspiration photos (where supported), pay a deposit

### Waiting room / express booking

The walk-in surface.

- typical information: waiting clients, technicians' readiness, quoted waits
- primary actions: add a walk-in, text a booking/payment link, collect a card on file, notify when ready

### Checkout / point of sale

The money surface for the visit.

- typical information: services at the client's technician level, retail items, tips, package balances
- primary actions: take payment, split payment, redeem prepaid value, sell retail and gift cards, refund, direct earnings to the right technician

### Reporting and settings

Management surface: revenue and technician performance, utilization, no-shows, retention; plus configuration of services, price levels, staff, policies, and permissions.

## Important Rules / Behaviors

- **A slot exists only where a technician is free.** Booking machinery checks technician availability, and stations or pedicure chairs constrain it further; blockouts on either can make a slot unavailable. Parallel visits consume two technicians' time in one appointment.
- **Cancellation and no-show are named outcomes, not deletions.** Policies attach deposits, cards on file, or fees; freed slots feed a waiting list; repeat no-showers can be blocked from online booking.
- **The same service can carry different prices per technician.** Price levels by experience, seniority, or specialization are a normal configuration, and booking surfaces show the client which technician's price they are booking.
- **Checkout attributes money to the technician.** Tips, commissions, and service revenue are recorded per technician for payroll — in commission salons and booth-rent salons alike.
- **The client record carries the reproduction data.** The salon's ability to repeat a client's last set depends on preference notes (shape, colors) being kept on the record; the researched products frame this as client notes and history rather than clinical documentation.
- **Walk-ins enter the same economy.** An unscheduled arrival is registered as a visit bound to a technician and a service, and it ends in the same checkout — the appointment book and the waiting room are two doors into one record system.
- **Appointment states are conceptual.** Booked → confirmed → arrived/in service → completed is the canonical flow; exact state names and colors vary by product.

## Variants

- **Multi-vertical platform packaging** — the dominant shape: nail salons served by salon/spa platforms where "nail salon" is a business type or industry configuration (catalog vocabulary, default services, industry marketing), with the full appointment-business machinery shared across verticals
- **Solo technician / booth renter** — one professional's book, payments, and client records; booth-rent payouts and instant payouts as the distinguishing economics
- **Walk-in-led high-volume salon** — waiting room, express booking, and group checkout in the foreground; appointment booking as a complement
- **Appointment-led design studio** — online booking with deposits, design-photo intake, complexity-based pricing, seniority price ladders
- **Multi-location nail franchise** — centralized catalog and policies, cross-location reporting, franchise roles
- **Marketplace posture** — the salon listed in the vendor's consumer app with automatic industry categorization; deliberately absent in products that position against marketplace leakage
- **Regional nail-only studios** — nail-exclusive businesses in other markets; the researched evidence for standalone nail-only software is limited (see Sources)

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Appointment-based Service Business Management | the generic Type whose defining core this leaf shares | nail salon management is its nail-industry variant; the difference is service vocabulary, preference content, and visit culture, not object structure |
| Salon Management System | closest sibling | same core; hair-side overlay (color formulas, processing records) instead of nail vocabulary and shapes |
| Barbershop Management | sibling | same core; barber overlay (individual barber as brand, booth rent, queue culture) shares walk-in and booth-rent aspects with nails |
| Spa Management System | sibling | same core with room-and-therapy itinerary emphasis |
| Med Spa Management | sibling with a compliance layer | adds regulated-treatment documentation and consent machinery absent from the nail variant |
| Massage Practice Management | sibling with documentation layer | clinical-intake and treatment-note culture absent from the nail variant |
| Beauty Professional Business App | packaging sibling | the individual professional is the account, not the salon; solo nail technicians converge with it |
| Beauty Service Marketplace | consumer-side counterpart | cross-salon discovery and booking vs operator-side management; bundled marketplace apps are an optional posture here |
| Retail POS | partial overlap | shares the payment spine; remove the appointment and technician context and only a POS remains |
| Appointment Scheduling Application | machinery overlap | slot and availability machinery without the client ledger, checkout, and technician economics |

The most important boundary is the one against the generic appointment-business Type: the defining core is shared and kept as a separate industry leaf by family precedent. Inside the beauty family, the discriminator is the overlay — nail vocabulary, preference records, and walk-in/group culture — not the structure.

## Representative Products

- **Vagaro** — multi-vertical salon/spa/fitness suite with a consumer marketplace; documents Nail Salon as a first-class business type and carries the full appointment-business machinery
- **Mangomint** — design-forward salon/spa platform with a dedicated nail-salon solution (nail art photo intake, two-technician services, walk-in waiting room, per-artist payments)
- **GlossGenius** — solo-first, mobile-first platform widely used by nail technicians and booth renters; positions walk-in-to-regular conversion and nail-specific client notes
- **Boulevard** — client-experience platform for appointment-based self-care businesses, serving premium nail salons and multi-location nail franchises

The defining core was checked across four platforms with different philosophies (marketplace suite, design-forward suite, solo-first, client-experience platform) to avoid over-fitting to any one packaging.

## Sources

Research date: **2026-09-08**

- Vagaro Support (help center, Tier-1): "Set Your Business Type" (Nail Salon keyword list) — https://support.vagaro.com/hc/en-us/articles/360048745274-Set-Your-Business-Type ; help-center search (nail; two providers; multi-provider services and bundles articles) — https://support.vagaro.com/hc/en-us/search
- Mangomint: Nail salon software page — https://www.mangomint.com/solutions/nail-salon-software/
- GlossGenius: Nail salon software page — https://glossgenius.com/customers/nail-salon-software ; platform homepage — https://glossgenius.com/
- Boulevard: Nail salon software page — https://www.joinblvd.com/nail-salon-software ; Support Center (Tier-1): "Enabling and Disabling Online Booking" (per-provider pricing on the booking overlay), "Professional App" — https://support.boulevard.io/en/ ; customer story (Freecoat Nails) — https://www.joinblvd.com/customer-stories/freecoat-nails

> Sourcing limitations: no standalone nail-only product could be researched — NailsMedia is an unreleased site and Nailbook (Japan) returned HTTP 403; search engines were unusable from the research environment. Nail-specific claims from Mangomint and GlossGenius rest on their official product pages (structure-level, not help-center depth); Vagaro and Boulevard nail-related claims rest on Tier-1 operational documentation. Claims about the shared appointment-business core reuse Tier-1 evidence recorded in the same research program on 2026-09-06. Vendor-published outcome figures are excluded from this document. Detailed observations, evidence-layer notes, and the removal tests behind the boundaries above are recorded in the paired Research Notes.
