# Med Spa Management

## Overview

A **Med Spa Management** application is the operating system of record for a medical spa — a business that delivers regulated aesthetic treatments (injectables, laser and light procedures, medical-grade skin care, IV therapy, medically supervised weight management) in a retail-wellness setting. It runs the full life of a client visit: the catalog of bookable treatments, the client record that carries the person's history, the appointment that binds a client to a treatment at a time with a qualified provider, the delivery of the visit, and the checkout that turns the completed treatment into recorded revenue.

What separates this category from generic appointment-business software is not a different core — it is the same visit economy, configured for treatments that are medical in character. Because the services are regulated and their results are documented, the software carries a characteristic compliance and documentation layer: client-facing intake and consent forms, provider-facing treatment notes saved to the client record, before-and-after photography, careful handling of health-related data, and treatment products tracked by the unit. When the regulated-treatment layer disappears and the catalog reverts to relaxation therapies delivered in rooms by therapists, the product becomes spa management software; when clinical encounters, insurance claiming, and physician-led care programs dominate, it drifts toward healthcare practice management.

## Users & Context

The software serves a small staff team inside one business (or a multi-location group):

- **Front desk / reception** — books and reshuffles appointments, checks clients in, takes payment, sells retail, manages the day's flow.
- **Treatment providers** — injectors, aestheticians, nurses, nurse practitioners, physicians: see their schedule, review the client's history and forms, document the treatment, record what was used.
- **Practice or spa manager / owner** — owns the catalog and pricing, staff schedules and pay-related settings, compliance setup, and the reports that run the business.

Secondary participants are the **clients themselves** (called clients or patients depending on the product): they book and pay through self-service surfaces, complete intake and consent forms before arriving, and may receive pre- and post-care instructions. In many businesses a **medical director or supervising provider** exists as a role in the business; software reflects this through review/approval duties rather than a separate system.

The work environment is front desk plus treatment room: the desk works in a dashboard on a desktop, providers work from tablets or phones at the chair — checking in the client, completing forms, charting, photographing results, and taking payment where the visit ends.

## Core Model

The world of the application is the visit economy of an appointment-based service business, adapted to regulated treatments:

```text
Client (person, persistent record with history)
   ↓ books
Treatment (catalog entry: duration + price + provider requirements)
   ↓ bound by
Appointment (client × treatment × provider × time)
   ↓ delivered under
Visit lifecycle (arrive → treat → complete; cancel / no-show as named outcomes)
   ↓ resolves into
Checkout (payment recorded against the visit, memberships/packages redeemed)
```

### The defining core

- **Treatment catalog** — the bookable services, each with duration and price. Treatments are provider-typed and often screening-dependent; the same software also sells retail products beside them.
- **Client records** — one persistent record per person: contact details, visit and purchase history, and (commonly) health-adjacent content gathered through forms. The record is the anchor everything else hangs on.
- **Appointment** — the binding of a specific client to a specific treatment at a time with a specific provider; treatment rooms and equipment participate as shared resources. Cancellation and no-show are first-class outcomes, often backed by deposits or card-on-file policies.
- **Visit lifecycle** — the appointment is worked through arrival, service, and completion; the record of what happened accumulates on the client.
- **Checkout** — the completed visit is resolved into recorded payment in the same system: card payments, packages, memberships, gift cards, and retail purchases.

Remove the appointment and catalog and only a client CRM remains; remove the checkout and only a scheduler remains; remove the client ledger and only a point of sale remains. The five structures above are jointly what makes this a management system rather than a collection of tools.

### The compliance and documentation layer

This is what the med-spa configuration adds on top of the visit economy. It is characteristic of the Type — mature products in this space carry it in some form — but it varies in depth from a light forms module to a full clinical record, and in at least one researched product it is sold as an optional add-on and in another enabled as a setting:

- **Client-facing forms** — medical intake and consent documents sent to the client and tied to appointments, with completion status and expiry (an expired consent must be re-collected before the next treatment). Completed forms save against the client record.
- **Provider-facing treatment documentation** — notes and charts completed by the provider at the point of care (structured note templates are the common form, SOAP-style notes the clinical idiom), saved to the client record and attachable per treatment. These documents are internal: they are not sent to clients.
- **Review and sign-off** — completed forms and charts can be routed to a designated reviewer who comments, approves, or rejects; some products surface documentation-completion rates as a compliance view for managers.
- **Before-and-after photography** — standardized capture (guides, overlays, per-body-area organization), annotation of treatment points on images, and side-by-side comparison, stored on the client record. Results photography is both a clinical record and a sales asset.
- **Regulated-data handling** — health-adjacent information is treated as sensitive: signed data-protection agreements with the vendor, restricted visibility of treatment details in client-facing messages, audit trails, and role-based access to records.
- **Unit-based product economics** — treatment products (injectables, skin products) linked to services with quantity and price per unit used, so usage, cost, and charging are recorded per treatment; stock levels and reorder alerts follow.
- **e-Prescribing and telehealth** — optional capabilities in some products: sending prescriptions from the client profile, and video consultations typed as appointments.

### One spine, many depths

The core is written conceptually; products differ mainly in how deep the compliance layer goes and how it is packaged. One researched product sells the entire clinical layer (photo markup, sign-off, regulated-data coverage) as a purchasable add-on on a general-purpose platform; another enables regulated-data handling as a setting "once enabled"; a third builds it in as a first-class module; a fourth, clinic-first product carries a full electronic medical record while still leading with booking, deposits, and point of sale. A reader meeting any of these should recognize the same spine.

## How It Works

### Configure the business

```text
Define treatment catalog (duration, price, provider eligibility, resources)
→ add providers and working hours; set rooms/equipment
→ build client-facing intake/consent forms and provider-facing note templates
→ configure deposits, no-show policies, memberships, packages
→ set access permissions (front desk / provider / manager)
```

For a med spa, configuration includes the compliance surface: which form is required for which treatment, what expires and when, who reviews documentation, and which data is hidden from client-facing messages.

### Fill the book and screen the client

```text
Client self-books online (or books by phone / walk-in)
→ reminders sent; deposits or card-on-file captured where configured
→ required intake/consent forms sent automatically and completed before arrival
→ waitlist fills cancellations
```

A documented med-spa-specific posture: some businesses deliberately limit online booking to consultations and require clients to call for treatment bookings, so screening happens before a regulated treatment is scheduled. The software supports this by letting the business restrict which services are bookable online.

### Run the visit

```text
Check in → verify forms are complete (chase or re-collect if expired/missing)
→ provider opens the client record: history, photos, prior treatments
→ deliver the treatment; document notes at the point of care
→ photograph before/after where part of the protocol
→ record products used (units consumed)
→ checkout: payment, package/membership redemption, retail
→ post-care instructions sent; rebooking prompted
```

The defining loop is this one: the appointment drives the day, the documentation and photography attach to the client record as the visit happens, and checkout closes the visit into revenue — all without leaving the system.

### Manage and grow

Managers work the same records from above: utilization and revenue reports, membership and prepaid-unit tracking, product-usage and stock reports, staff performance and commissions, retention campaigns and review requests, and — where the compliance layer is in use — documentation-compliance views. Multi-location groups add cross-site reporting and centralized catalog control with site-level flexibility.

## Interfaces

Surfaces are described conceptually; exact layouts and names vary by product.

### Appointment book / calendar

The operational center for the front desk and providers.

- typical information: days/weeks of appointments by provider and room, statuses, form-completion flags
- primary actions: create/move/cancel appointments, check in, open the client record, start checkout

### Client record (client card)

The person-centric surface everything attaches to.

- typical information: contact details, visit and purchase history, forms and their statuses, treatment notes, before/after photos, memberships/packages, retail history
- primary actions: book, complete/view forms and charts, upload/mark up photos, take payment, message

### Forms and charts workspace

Where the documentation layer lives, reachable from the appointment and the client record.

- typical information: form/chart name, type, status (not started / in progress / completed / expired), who completed it and when
- primary actions: send/resent reminders to clients, complete charts (with templates, image annotation, photo upload), route for sign-off, export

### Checkout / point of sale

- typical information: the visit's charges, products used, package/membership balances, retail items
- primary actions: take payment, redeem prepaid value, split payments, sell retail/gift cards, receipt

### Provider (tablet/phone) workspace

The chair-side surface: today's schedule, the client in front of you, forms to complete, notes to write, photos to take, checkout to run.

### Management and reporting

- typical information: revenue and utilization, client retention, membership/prepaid-unit status, product usage and stock, staff performance, documentation compliance
- primary actions: configure catalog/policies, manage staff and permissions, run campaigns, review compliance gaps

### Client self-service

Online booking, form completion, deposits and payments, appointment management, and in some products a portal to view history, photos, and care instructions.

## Important Rules / Behaviors

- **Consent before treatment is enforced by the record, not memory.** Required forms attach to appointments; an expired or missing form surfaces at check-in and the client must complete (or re-complete) it before the next treatment. Some products let managers require review/sign-off of completed documentation before it counts.
- **Treatment documentation is internal.** Client-facing forms and provider-facing charts are distinct document classes; charts are never sent to clients. Compliance-minded products also hide treatment names from automated client-facing messages by default.
- **Health-adjacent data is access-controlled.** Role-based permissions decide who sees records, notes, and photos; vendor agreements and audit trails support the business's regulatory posture (the regime itself — e.g., HIPAA or GDPR — depends on where the business operates and is a configuration, not a product constant).
- **The visit resolves into money in the same system.** Deposits, no-show fees, package and membership redemption, and per-unit product charges all post against the visit at checkout; a visit that is not checked out remains an open thread in the day's reconciliation.
- **Treatments are screening-dependent.** Unlike haircut appointments, many treatments can only be booked or delivered after a consultation or completed intake; products reflect this through bookable consultations, online-booking restrictions, and gated service visibility.

## Variants

- **Packaging of the clinical layer** — the same Type spans: general appointment platforms with med-spa configuration (clinical layer optional/add-on), platforms with built-in medspa modules, and clinic-first products carrying a full electronic medical record while keeping the booking economy central.
- **Sub-industry emphasis** — injectable/filler clinics, laser and skin clinics, medical weight-loss practices, IV-therapy and wellness clinics: same machinery, different catalog taxonomy and charting templates.
- **Regulatory regime** — US-style privacy compliance versus UK/EU data protection; consent and record vocabulary follows the regime.
- **Scale** — single-location practices; multi-location chains and franchises with centralized catalogs, cross-site reporting, and role hierarchy.
- **Optional extensions** — e-prescribing, telehealth consultations, AI-assisted note-taking, insurance billing (rare in this sample), consumer financing, retail depth.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Appointment-based Service Business Management | generalist sibling | same visit economy without the regulated-treatment compliance layer; med spa is the medical-aesthetics industry configuration of it |
| Spa Management System | closest sibling in the same family | remove consents/clinical notes/regulated-data handling and unit-based treatment economics → relaxation/wellness therapies in rooms; the spa pole's center is the room-and-therapy itinerary |
| Salon / Barbershop / Nail / Massage Management | industry siblings | same core; their overlays (color formulas, tipping, treatment documentation) differ from the med-spa compliance layer |
| Beauty Professional Business App | packaging sibling | the individual professional's own book and income, rather than a managed business location |
| Patient Scheduling / Practice Management (healthcare) | regulated cousin | clinical encounters inside medical-record and insurance semantics; here the commercial visit economy stays central even when documentation is deep |
| Beauty Service Marketplace | consumer-side counterpart | cross-provider discovery and booking; this Type runs one business |
| E-commerce / Retail POS | partial overlap | sells owned inventory at a counter; no appointment spine, no client-visit record |

The sharpest boundary inside the family is with Spa Management System: the test is the regulated-treatment layer, not the presence of rooms or memberships. The sharpest boundary outside the family is with healthcare practice management: documentation depth alone does not cross it — where insurance claiming and physician-led care programs take over, the product has left this Type.

## Representative Products

- Zenoti — enterprise all-in-one platform serving medspas, salons, spas, and fitness businesses
- Boulevard — client-experience platform for appointment-based self-care businesses, with a medspa add-on
- Mangomint — salon and spa software with a dedicated med-spa solution
- Pabau — clinic practice management used by medspas and aesthetic clinics

## Sources

Research date: **2026-09-08**

- Zenoti — Medical spa software page: https://www.zenoti.com/medical-spa-software (site: https://www.zenoti.com/)
- Boulevard — Medical spa software page: https://www.joinblvd.com/medical-spa-software ; Support Center (Tier-1): "Forms and Charts in the Professional App" (https://support.boulevard.io/en/articles/8038055), "Product Tracking" (https://support.boulevard.io/en/articles/10723276), "Medspa Training Checklist" (https://support.boulevard.io/en/articles/9586002), "Medspa Add-On" (https://support.boulevard.io/en/articles/9084775)
- Mangomint — Med spa software page: https://www.mangomint.com/solutions/medical-spa-software/ (site: https://www.mangomint.com/)
- Pabau — Medical spa software page: https://pabau.com/industry/medical-spa-software/ (site: https://pabau.com/)

> Sourcing limitation: operational help-center documentation was reached for one of the four researched products (Boulevard); the other three products' claims rest on their official product and industry pages, so their contribution is asserted at structure level rather than operational detail. Vendor-published figures (pricing, ratings, benchmark percentages, integration reach) are deliberately excluded from this document. Detailed observations, packaging evidence, and the removal tests behind the boundaries above are recorded in the paired Research Notes.
