# Salon Management System

## Overview

A **Salon Management System** is the operating system for a salon — a business whose revenue is built on client appointments for personal-care services performed by stylists and other salon professionals. It manages the full life of a client visit: the bookable service menu (cuts, color, highlights, perms, treatments, and the rest of the hair and beauty catalog), the clients and their history, the appointment that binds a client to a stylist at a time, and the checkout that turns the finished service into recorded revenue — together with the salon layer around the visit: color formulas and before/after photos on the client record, processing time inside color services, stylist-level pricing and commissions, booth-rent and hybrid business models, and professional-product retail.

The defining structure is:

```text
Bookable service menu (each service with duration and price)
+ Identified client records
+ Stylist availability (schedules, stations/rooms)
  └── Appointment (client × service × stylist × time slot)
        └── Lifecycle: booked → confirmed → arrived → in service → completed
              (cancellation / no-show as named alternative outcomes)
              └── Checkout → recorded payment + tip against the client
```

This core is shared with appointment-driven service businesses in general (barbershops, nail salons, spas, wellness studios); what gives the salon category its shape is emphasis and elaboration rather than new machinery. In salons, the service menu is filled with hair-service vocabulary; a color service can contain **processing time** during which the client waits and the stylist is free to take another client; the client record carries **color formulas and before/after photos**; and the money layer is organized around **stylist-level economics** — tiered pricing by seniority, commissions on services and products, tips, and booth-rent arrangements. Everything else commonly associated with these products — self-booking pages, reminder texts, no-show fees, packages and memberships, marketing automation, multi-location management — is widespread but sits on top of the core rather than defining it.

When the appointment and its business context disappear — leaving only a calendar and reminders, or only a payment terminal — the product has drifted into a different Application Type (an appointment scheduler, or a point of sale).

## Users & Context

The primary users sit on the business side:

- **Salon owner / manager** — owns the service menu and pricing (including per-stylist price levels), staff schedules, policies, inventory, and the reports that run the business; in larger salons, oversees stations, rooms, and multiple locations.
- **Stylist (service provider)** — works from a personal calendar or column, sees arriving clients, performs services, and in most salons is paid partly by commission on what they deliver. In solo and booth-renter setups, the stylist is also the owner and the front desk.
- **Front desk / reception** — the daily operator of the calendar: books and reschedules appointments, checks clients in, handles cancellations and walk-ins, takes payment. In small salons this role collapses into the stylist or owner.

On the other side sits the **client**, who mostly interacts indirectly: booking through the salon's booking page or app, receiving confirmations and reminders, and paying at the end of the visit. Some products run a consumer marketplace where new clients discover the salon; others deliberately keep discovery off the software entirely.

The work environment is the front desk and the chair: a calendar screen the whole day is organized around, the stylist's chair-side view of their own book, and a checkout step at the end of each visit. The client relationship is the economic engine — salons live on rebooking and retention, which is why the client record, the rebooking prompt, and the lapsed-client campaign are first-class surfaces.

## Core Model

### The Defining Core

Five structures. If one is removed, the product is no longer this Type:

- **Bookable service menu** — the hair and beauty services the salon sells, each defined with a duration (how long the chair is occupied) and a price. Categories organize the menu; add-ons (extra treatments attachable at booking or checkout) and bundles (multiple services sold as one) are the standard elaborations. The salon's identity lives in the vocabulary: cuts, color, highlights, blowouts, perms, keratin and relaxer treatments, color correction — products recognize salon businesses by these service names.
- **Identified client records** — every visitor is a persistent, individually identified record: contact details, visit history, notes, preferences, and balances. The salon remembers the person, not just the transaction; the record is what makes rebooking, preference service, and no-show tracking possible.
- **The appointment as the central binding object** — an appointment binds a client, a service from the menu, and the stylist who will perform it, into a specific time slot on the salon calendar. Whoever does the hair is part of the booking: clients choose their stylist, and a solo stylist is modeled as the provider of their own calendar.
- **Appointment lifecycle to service delivery** — the appointment moves through named states from booking, through confirmation and the client's arrival, to the service being performed and completed. Cancellation and no-show are first-class alternative outcomes with their own policy handling, not merely deleted records.
- **Checkout that resolves the visit into recorded money** — the completed appointment becomes a chargeable visit recorded against the client. Tipping is a standard component of the ticket; retail products and walk-in customers share the same checkout surface, so the service business and the merchandise business settle in one place.

### Objects Around the Core

- **Stylist profiles and levels** — the professional's working configuration: services performed, prices (often tiered by experience — junior, senior, master stylist pricing for the same service), working hours, and earnings. Availability is what makes a slot bookable.
- **Stations and rooms** — chairs, styling stations, processing rooms, and equipment that services consume. Booking the appointment can also book the resource.
- **Client formula and photo content** — the salon-characteristic layer of the client record: color formulas and recipes (mixed color, developer, timing) recorded so the same result is repeatable at the next visit, before/after photos, and preference notes. In current products this content lives in the client's notes and profile rather than as a separate formula module; dedicated formula machinery (weighing, waste tracking) arrives through third-party integrations.
- **Processing time** — the salon's distinctive time-model elaboration. A color service is modeled in blocks: the working time when the stylist is with the client, the **processing time** when the client waits (under a dryer, with color developing) and the stylist is bookable by other clients, and the finishing time when the stylist returns to complete the service. The client sees one appointment; the calendar sees bookable capacity inside it.
- **Stylist economics** — commissions (service-based and product-based), tips, hourly pay, payroll, and — in booth-rent and hybrid salons — rent arrangements with renters paid out to their own accounts.
- **Prepaid value** — packages, memberships, and gift cards sold to clients, carried on the client record, and redeemed at checkout.
- **Retail products and backbar inventory** — professional products sold to clients in the same transaction as services; stock deducted not only by sales but by **product usage in services** (the backbar), keeping inventory honest about what the salon consumed.

### One Structure, Many Implementations

The core model is conceptual. Products implement it with different vocabularies and postures:

```text
Concept:              Service time model
Implementations:      single duration per service,
                      working + processing + finishing blocks with bookable processing time,
                      per-stylist duration and price overrides

Concept:              Formula keeping
Implementations:      typed note categories on the client profile,
                      free-text client notes with photo attachments,
                      third-party color-system integrations writing formulas back to the profile

Concept:              Business model
Implementations:      commission-based employment,
                      booth rental with renters as tenants,
                      hybrid of both in one salon

Concept:              New-client acquisition
Implementations:      bundled consumer marketplace,
                      booking page plus Google/social booking overlays,
                      no discovery at all (the salon brings its own clients)
```

A reader who has only seen a marketplace-era salon app should still be able to recognize a back-office chain system, or a solo stylist's phone-only setup, from the core model alone.

## How It Works

### Set up the salon

```text
Define services (name, duration, price, category — color services with processing blocks)
→ add stylists and their working hours
→ assign which services each stylist performs, at which price level
→ optionally attach stations/rooms to services
→ set booking rules (how far ahead, approval required, deposits)
→ publish the booking page
```

After setup, the menu, stylist availability, and booking rules jointly determine what clients can book and when.

### Book an appointment

Booking happens from two directions:

- **Client self-booking** — the client opens the salon's booking page (or a marketplace listing, where the vendor runs one), picks a service, sees available times generated from stylist availability, chooses a stylist (or accepts assignment, often at a tier-based price), and books. Depending on the salon's rules the booking confirms instantly or becomes a request; deposits or saved cards may be required.
- **Desk-side booking** — the front desk books on the calendar directly: pick the client (or create them), pick the services and stylist, pick the slot. Multi-service visits — a cut and a color in one sitting, composed as a bundle or a sequence — are built here, and the calendar blocks the combined time including processing and cleanup.

### Run the visit

```text
Appointment sits on the stylist's calendar
→ automated confirmation and reminders go out
→ client arrives; appointment is checked in
→ the stylist performs the work
   (in a color service: work → client processes while the stylist may take another client → finish)
→ service completed; the appointment becomes ready for checkout
```

Alternative outcomes are handled by policy: **cancelled** (possibly with a fee from a saved card), **no-show** (fee or future-booking restriction; the event stays on the client's record), **rescheduled** (the appointment moves, keeping its history).

### Check out

```text
Open the completed appointment (or a walk-in)
→ review the service ticket (add retail items or add-ons)
→ apply discounts, prepaid redemptions, tips
→ take payment (card, cash, wallet, gift card, split across methods)
→ record the transaction against the client's history
→ receipt; rebook the next visit before the client leaves
```

Checkout is where the visit becomes revenue and where per-stylist earnings are attributed — the commission report is fed by the same ticket. In booth-rent salons, the money may be routed onward to the renter's own account.

### Run the salon around the loop

Beyond single visits, the operator works recurring loops: keeping chairs full (waitlists, rebooking prompts, win-back campaigns to lapsed clients), managing the team (schedules, performance, commissions, payroll), tracking retention and no-show rates, keeping retail and backbar inventory stocked, and — where the vendor offers one — appearing in a consumer marketplace to acquire new clients. A recurring salon-specific concern is **stylist turnover**: when a stylist leaves, their clients' history and formulas stay on the salon's records so the guests can be rebooked and served by someone else.

### Defining core vs standard capabilities vs optional

**Defining core** — without these, not this Type:

- bookable service menu with duration and price
- identified client records
- appointment binding client × service × stylist × time
- lifecycle through service delivery, with cancellation/no-show outcomes
- checkout resolving the visit into recorded payment, tips included

**Standard capabilities** — present in nearly all mature products:

- online client self-booking page
- automated confirmations and reminders
- cancellation/no-show policies with fees, deposits, saved cards
- client visit history, notes, and preferences — with color formulas/recipes and before/after photos as the salon-characteristic content
- processing-time blocks inside services, bookable by other clients (common in salon-serving products; a salon that does little color work may not use them)
- multi-service visits and bundles (cut + color in one sitting)
- tiered pricing by stylist level; per-stylist prices and durations
- stations/rooms as bookable resources
- packages, memberships, gift cards with redemption at checkout
- retail sales with inventory, including product usage deducted by services
- commissions (service- and product-based), tips, payroll
- walk-in handling beside the appointment book
- reporting (revenue, utilization, retention, no-shows, per-stylist performance)
- multi-location management

**Optional / variant** — depends on posture and business model:

- consumer marketplace listing and discovery app (bundled by some vendors, explicitly absent in others)
- booth-rent machinery (rent tracking, renter payouts to separate accounts, direct booking links for renters)
- hotel-salon room charges (resort/hotel spas charging to the guest's room)
- salon-industry environmental service fees
- mobile/outcall services; tanning-bed and room scheduling; classes
- clinical-grade documentation overlays (intake forms, charting) for medspa-adjacent salons
- AI assistants (automated reception, rebooking, marketing)

## Interfaces

### Calendar / appointment book

The operator's home surface.

- Purpose: see and manage the day (or week) across stylist columns and stations.
- Typical information: appointments as colored blocks per status, stylist columns, station occupancy, empty slots, processing-time openings inside longer services, walk-in entry points.
- Primary actions: book, reschedule, change status (confirm, check in, start, complete, no-show, cancel), block out time.

### Online booking page (client-facing)

- Purpose: let clients book without staff involvement.
- Typical information: service menu with prices and durations (tiered by stylist level where offered), stylist choices, available times, booking and cancellation policies.
- Primary actions: choose service/stylist/time, provide contact details, sometimes pay a deposit.

### Client profile

- Purpose: the single record of the salon's relationship with a person.
- Typical information: contact details, visit history, formula and preference notes, before/after photos, upcoming appointments, package/membership/gift-card balances, saved payment methods, no-show history.
- Primary actions: book, edit details, note-taking (formulas, preferences), view history, manage balances.

### Checkout screen

- Purpose: settle the visit.
- Typical information: the service ticket, retail items, price adjustments, discounts, tips, taxes, applied prepaid value, per-stylist attribution.
- Primary actions: add/remove items, apply discounts, redeem package/membership/gift card, take payment (split methods), refund, print/send receipt, prompt rebooking.

### Stylist views and money surfaces

- The stylist's personal calendar and earnings view (today's clients, commissions earned, tips).
- Payroll and commission reporting for the owner; renter payout surfaces in booth-rent salons.

### Reporting / dashboard

- Purpose: answer "how is the salon doing?"
- Typical information: revenue by service/stylist/day, chair utilization, rebooking and retention rates, cancellation/no-show reports, retail attachment, prepaid liability.
- Primary actions: filter, compare periods, drill into stylist performance.

## Important Rules / Behaviors

- **Availability is the booking law.** A slot is bookable only when the assigned stylist (and any required station) is free for the service's full duration. Schedules, time off, and blockouts remove capacity; booking rules further constrain online booking.
- **Processing time is bookable — by design and by toggle.** In color services, the block when the client waits is, by default, capacity the salon can sell to another client; products let the salon disable this "double booking" per service. The client always sees one continuous appointment; only the salon's calendar shows the openings inside it.
- **An appointment is a reservation, not a sale.** Booking commits time, not money; money changes state only at checkout. No-shows and cancellations are the gap between the two, which is why policy enforcement — fees, deposits, saved cards — is structural rather than an add-on, and why no-show history is tracked per client.
- **The formula is the salon's memory of the result.** Color work is repeatable only if the formula survives the visit; that is why formula content sits on the client record (as notes, categories, or photos) and why staff-only visibility and edit permissions on those notes are normal. Notes are internal — clients do not see them.
- **Checkout is separate from service delivery.** The stylist finishes the service; the front desk (or the stylist, in a solo setup) then settles the ticket. A visit can be completed but not yet paid — products keep these states distinct and allow reversal before final settlement.
- **Money follows the stylist.** Every ticket attributes its earnings — service revenue, product revenue, tips — to the stylist who performed the work; commissions and payroll are computed from that attribution. In booth-rent salons, the salon↔renter relationship (rent owed, payouts to separate accounts) is modeled alongside the salon↔client one.
- **The client record outlives the stylist.** When a stylist leaves, their clients' history and formulas remain on the salon's records so the guests can be rebooked and served by someone else — the software's answer to the industry's turnover problem.
- **Prepaid value changes the checkout, not the catalog.** A package visit or membership entitlement is redeemed against the ticket; the client is not re-charged, but the redemption is still recorded against the stylist's performance.
- **Permissions scale with role and size.** Solo stylists see everything; in teams, stylists typically see their own calendars and earnings, while price overrides, discounts, refunds, formula-note access, and policy changes may require manager permission.

## Variants

- **Multi-vertical salon platforms** — one product serving salons, barbershops, nail salons, spas, and medspas; the salon is one configured vertical. The most common realization of the Type.
- **Salon-native suites** — products built salon-first (booking, color-service timing, stylist economics as the center), often positioned up-market into spas and medspas.
- **Solo-first, payments-native products** — one stylist, one calendar, payments built in; the software substitutes for a receptionist (self-booking, reminders, no-show protection). Booth renters are a major audience.
- **Booth-rental and hybrid salons** — rental economics foregrounded: rent tracking, renters paid out to their own accounts, direct booking links per renter, mixed commission/rent arrangements under one roof.
- **Enterprise chains and franchises** — multi-location operations with cross-location client records, standardized service menus, consolidated reporting, and franchise oversight.
- **Hotel/resort salons** — services charged to the hotel guest's room through property-management integration.
- **Marketplace-era vs anti-marketplace posture** — the same core sold with a bundled consumer discovery app, or explicitly without one ("your clients shouldn't see your competitors").

A variant remains a variant as long as the appointment-to-checkout core describes it; when clinical care becomes the primary unit of work (medspa) or the served subject stops being a person in the chair (pet grooming), the product belongs to a neighboring Type.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Appointment-based Service Business Management | generic core | the shared defining core (service catalog + clients + appointment + lifecycle + checkout) is identical; salon management is its hair-salon industry variant — differences are overlay (hair vocabulary, processing time, formulas, stylist economics), not structure |
| Barbershop Management | sibling variant | same core; barber overlay emphasizes the individual barber's identity, booth rent, tips, and client-side checkout; salon overlay emphasizes color formulas, processing time, and multi-service color visits; platforms cross-serve both |
| Nail Salon Management | sibling variant | same core; nail overlay carries nail-service vocabulary, shape/color preferences, and art-informed booking instead of hair vocabulary and formulas |
| Spa Management System | sibling variant | same core; the spa pole centers rooms and therapy itineraries rather than the stylist's chair and the color service |
| Med Spa Management | sibling variant with a regulated layer | same visit economy plus a clinical-documentation/compliance layer (intake, consent, charts); remove that layer and the med-spa business runs on this Type's core |
| Beauty Professional Business App | same core, opposite packaging | there the individual professional's own book/brand/income is the account; here the salon is the account (roster, stations, commissions, shop identity); the two converge when a solo stylist uses salon software |
| Beauty Service Marketplace | consumer-side counterpart | the marketplace's primary surface is discovery across many businesses; this Type manages one business; some vendors bundle both sides |
| Appointment Scheduling Application | shares booking machinery | schedules appointments but carries no client ledger, no service-delivery lifecycle, and no checkout; a salon management system *runs on* the appointment |
| Retail Point of Sale | shares checkout spine | sells items over the counter; no appointments, durations, or stylists; here the sale originates from a scheduled service, and retail shares only the checkout |
| Pet Grooming Management | structurally rhyming | same appointment-book skeleton, but the served subject is an animal under an owner account with a drop-off → groom → pick-up loop; here a person sits in the chair through the visit |

The two sharpest tests: remove the client ledger and checkout → an appointment scheduler remains; remove the booking and calendar → a point of sale remains. Against the generic appointment-business Type, no removal test separates them — they differ in industry overlay, which is why this leaf is documented as a variant of that core rather than a structurally independent one.

## Representative Products

- **Vagaro** — multi-vertical salon/spa/fitness suite with a consumer marketplace; documents hair-salon business typing, formula notes, and gap-processing time in its help center.
- **Boulevard** — salon-native client-experience platform (salon is its lead industry); documents the four-block service timing model, color-formula client notes, and salon-industry integrations.
- **Zenoti** — enterprise salon/spa/medspa platform for single-location to chain operations; illustrates the high end of the same core with stylist economics and backbar inventory.
- **Mangomint** — design-forward salon/spa suite with hair salons as the lead vertical; documents booth-rental/hybrid/commission support, tiered stylist pricing, and walk-in machinery.
- **GlossGenius** — solo-first, payments-native platform for salon owners and booth renters; no marketplace; documents color recipes and before/after photos on client profiles.

The core model was checked against products from different postures (multi-vertical platforms, salon-native suites, solo-first products) and different business models (commission, booth-rent, hybrid), and against the paper-era salon (appointment book + formula cards + retail shelf) so the definition does not depend on any one generation or packaging of the software.

## Sources

Research date: **2026-09-10**

- Vagaro Support (help center, Tier-1): "Set Your Business Type" (Hair Salon keyword list) — https://support.vagaro.com/hc/en-us/articles/360048745274-Set-Your-Business-Type ; "Manage Customer Notes" (Formula Notes category) — https://support.vagaro.com/hc/en-us/articles/360007906613-Manage-Customer-Notes ; "Manage Gap Processing Time During a Service" — https://support.vagaro.com/hc/en-us/articles/360010299394-Manage-Gap-Processing-Time-During-a-Service ; help-center search (booking time incl. gap processing/cleanup; per-employee prices; renters and contractors) — https://support.vagaro.com/hc/en-us/search
- Boulevard Support Center (Tier-1): "Client Notes" (color formulas) — https://support.boulevard.io/en/articles/5941455-client-notes ; "Service Timing Options" (Duration/Processing/Finishing/Transition) — https://support.boulevard.io/en/articles/5941395-service-timing-options ; "Boulevard Integrations" (Vish color formulas, Green Circle Salons, OPERA) — https://support.boulevard.io/en/articles/7880786-boulevard-integrations ; support-center search (advanced service customization, service records report, permission groups) — https://support.boulevard.io/en/search
- Zenoti salon management page (Tier-2): https://www.zenoti.com/salon-management-software ; Zenoti API documentation (object model, Tier-1, reused from the 2026-09-06 family pass): https://docs.zenoti.com/
- Mangomint hair-salon page (Tier-2): https://www.mangomint.com/solutions/hair-salon-software/
- GlossGenius salon page (Tier-2): https://glossgenius.com/customers/salon-software

> Sourcing limitation: Zenoti's help center was not reachable (403) and its claims here rest on official product pages plus API-doc evidence reused from the family pass; Mangomint and GlossGenius help centers were not reachable in this research program (carried limitation), so their evidence is product-page level and operational details are stated at reduced strength. Fresha and Booksy remained unreachable (carried from the 2026-09-06 pass). Precise vendor figures, plan gates, and pricing are deliberately omitted from this document and remain in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison matrix, and boundary analysis are recorded in the paired Research Notes.
