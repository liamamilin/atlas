# Research Notes — Tattoo Studio Management

Research date: 2026-09-09

## Research Goal

Understand the software category used by tattoo studios (commonly together with piercing services) to run their business — booking, clients, deposits, consent/release forms, multi-session work, checkout, and the body-art-specific machinery around them — and determine whether "Tattoo Studio Management" is a structurally independent Application Type or the tattoo/piercing-industry variant of the generic appointment-based service business category.

This pass owes a joint-review resolution to the flag recorded when `appointment-based-service-business-management` was processed (2026-09-06), which listed this leaf among probable industry Variants, and to the removal test recorded by the `med-spa-management` and `nail-salon-management` passes (2026-09-08): "remove the regulated-treatment layer → that industry's business on the same visit economy." The `barbershop-management` (2026-09-06), `massage-practice-management` / `med-spa-management` / `nail-salon-management` (2026-09-08) passes set the precedent for resolving such flags.

## Initial Boundary

Initial hypothesis (before research):

- The leaf sits in Directory §29 between "Virtual Beauty Try-on Application" and "Personal Styling Platform", inside the industry-sibling block (salon, barbershop, spa, med spa, nail, tattoo) near the generic "Appointment-based Service Business Management" leaf.
- Expected tattoo-specific overlays to test (not assumed defining):
  - **Deposit-centric booking economics** — custom tattoo work is famously booked with a non-refundable deposit paid up front; deposit handling may be deeper than the generic policy layer.
  - **Consent / release forms + age verification** — tattooing is age-restricted and requires signed informed consent; waiver/consent machinery may be a first-class layer.
  - **Custom design / artwork handling** — consultations, design approval, reference images, placement/size details; possibly a design object.
  - **Multi-session work** — large pieces done over multiple sittings; recurring/repeat booking structures.
  - **Walk-in / flash demand** beside booked custom work.
  - **Piercing adjacency** — many studios offer both.
  - **Aftercare instructions** — post-session care messaging.
  - **Artist as the bookable unit** with portfolio (barbershop-like).
- Closest neighbors to test against: Appointment-based Service Business Management (generic core), Salon/Barbershop/Spa/Med Spa/Nail siblings, Appointment Scheduling Application (03.09), Retail POS (05.10), Beauty Service Marketplace / Service Marketplace (05.02/§29), Digital Waiver Management (§26 — consent/waiver machinery seam), Practice Management System (§22 — consent-forms-but-no-clinical seam), Beauty Professional Business App (§29 solo-artist packaging).

## Research Questions

1. What objects make up a tattoo studio management system's world, and do they differ structurally from the generic appointment-business core?
2. How do deposits work (collection at booking, calendar visibility, forfeiture on no-show, refund rules, application to the final ticket)? Is deposit machinery definitional or a configured emphasis?
3. Is there a design/artwork object or approval workflow, or does design content live inside booking forms and client records?
4. How is the consent/release-form layer structured — client-facing intake vs day-of consent; what binds forms to services, appointments, and client records?
5. How is multi-session work handled (recurring appointments, repeat bookings)?
6. How do consultations and walk-in slots appear in the service catalog?
7. Is the artist the bookable unit, and what artist-specific content exists (portfolio, licensing)?
8. How do packaging philosophies differ (tattoo-native product vs tattoo vertical of a small-business booking platform vs generic multi-vertical suite)?
9. Which capabilities are common vs optional (self-booking, reminders, aftercare messaging, retail, gift cards, payroll, marketplace, website builder)?
10. Boundary tests: what would have to be removed for this to become a scheduling app, a POS, a marketplace, or a standalone waiver system?
11. Historical check: would a paper-era tattoo shop (appointment book + deposit log + paper consent forms + design sketches) still fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| DaySmart Body Art (Powered by InkBook) | Tattoo/piercing-native studio management; the InkBook product line rebranded under DaySmart's body-art vertical | Solo artists → multi-artist shops | The tattoo-native philosophy pole; piercing named in scope |
| Bookedin | Small-business online booking platform with a dedicated, deeply-written Tattoo Shops vertical | Solo artists → busy shops | Tattoo-vertical pole; vendor publishes tattoo-specific guidance (booking form vs consent form) |
| Vagaro | Generic salon/spa/fitness/wellness appointment-business suite serving tattoo as a business type; consumer marketplace | SMB → chains → multi-location | Generic-suite pole with Tier-1 help-center evidence (deposits, forms, business types) |

Sampling notes:

- Tattoo Studio Pro (`tattoostudiopro.com`): domain parked on a default server vhost — product unreachable; no claims made.
- InkBook: no longer a separate site; DaySmart Body Art's login points to `online.inkbooktattoosoftware.com`, the app store listing is "InkBook Software", and the site footer carries "Powered by InkBook" — treated as one product (DaySmart Body Art / InkBook).
- PocketSuite: reachable, but its industry list has no tattoo vertical (beauty/health-wellness/home services only); usable only as generic context, not sampled.
- Timely (`gettimely.com/tattoo-software/`): 404. Mangomint (`mangomint.com/tattoo-studio-software`): 404. Not sampled.
- Fresha / Booksy / GlossGenius: recorded as unreachable (403 / JS shell) in multiple prior sibling passes; not retried.
- Bookedin help center (`support.bookedin.com`): transport error + timeout on two attempts — abandoned per network rules; Bookedin evidence rests on its marketing/vertical/blog pages (Tier 2).
- DaySmart Body Art root page timed out once and succeeded on retry; its support center was not fetched — DaySmart evidence is Tier 2 (product pages only).

## Sources

Tier 1 (official operational documentation), fetched 2026-09-09:

- Vagaro Support — Help Center home: https://support.vagaro.com/hc/en-us
  (category map: Checkout; Credit Card Processing; Calendar and Scheduling; Things You Sell; Customer Management; Forms and SOAP Notes; Employee Management; Payroll; Reports and Dashboard; Marketing; Check-in App; E-Prescribe; …; HIPAA Compliant + PCI DSS badges)
- Vagaro — "Require a Customer Deposit for Online Booking": https://support.vagaro.com/hc/en-us/articles/17733255383707-Require-a-Customer-Deposit-for-Online-Booking
  (deposit definition, deposit icons, membership/package deposit payment, card auto-storage, payout timing, payroll attribution, refund configuration, setup: Deposit Due fixed/%, minimum-price threshold, customer-type targeting, cancellation policy; support replies: default non-refundable, one universal deposit rule per business, remaining-balance settlement)
- Vagaro help-center search results (2026-09-09):
  - "Set Your Business Type" (article snippet lists tattoos / tattoo removal among business types)
  - "Portfolio Image Tips" ("Only images related to Barber, Beauty, Fitness, Wellness, Tattoo, and Pet Grooming services are eligible for approval")
  - "Manually Collect a Customer Deposit From the Calendar"; "See Your Deposit History from the Deposits Report"; "Refund a Prepaid Appointment or Deposit From a Customer's Profile"; "Automatically Charge a Cancellation or No-Show Fee"; "Require a Credit Card on File to Book"

Tier 2 (official product pages), fetched 2026-09-09:

- DaySmart Body Art — home: https://www.daysmart.com/bodyart/
  ("Piercing & Tattoo Studio Software"; schedule/inventory/payroll/clients/campaigns/payments; "Powered by InkBook"; independent-artist and multi-artist packages)
- DaySmart Body Art — Appointment Scheduling: https://www.daysmart.com/bodyart/features/booking-management/
  (digital tattoo appointment book; online requests must be accepted; no double-booking; reminders; color-coding/filters/dashboard; recurring appointments for multi-session work — "Lock down the time that works until that piece is done")
- DaySmart Body Art — Forms: https://www.daysmart.com/bodyart/features/forms/
  ("Tattoo & Piercing Release Form App"; drag-and-drop builder with signature capture; requirement modes: never / every booking / first booking only; per-service form requirement "before services can be rendered"; Forms tab roster; alert status on the appointment until forms returned; "in compliance or not" at appointment time; send via text/email; per-client completed/outstanding forms; COVID-19 screenings)
- DaySmart Body Art — Client Management: https://www.daysmart.com/bodyart/features/client-management/
  ("Tattoo CRM"; notes before/after appointments; photos attached to client records; release forms stored; loyalty/membership; deposits + cards on file; retail inventory; integrated EMV payments; gift cards)
- DaySmart Body Art — Online Booking: https://www.daysmart.com/bodyart/features/online-booking/
  (free booking website; 24/7 booking; Facebook booking; accept/reject requests with automatic email notification)
- Bookedin — Tattoo vertical: https://bookedin.com/tattoo-shop-online-appointment-booking-software/
  (vendor definition of the category; consultations/deposits/walk-in service types; deposit at booking before confirmation; multi-artist calendars; client profiles with reference images/placement/deposit history; aftercare messaging; tattoo + piercing customer evidence; US/CA/UK/AU)
- Bookedin — Features: https://bookedin.com/online-scheduling-payment-system-features/
  (online booking with flexible availability, recurring bookings, custom booking forms, add-ons; reminders incl. reply-to-confirm and follow-up sequences; deposits/upfront payments; Square/Stripe/PayPal; client list & history with custom fields/photos/documents/no-show history; staff security roles; 2-way calendar sync; mobile app)
- Bookedin — Blog "Tattoo Booking Form vs. Consent Form": https://bookedin.com/blog/tattoo-booking-form-vs-consent-form/
  (booking form = pre-appointment intake: contact, flash/custom, concept, placement+size, style, reference images, budget, availability, optional light health check, deposit-agreement line; consent form = signed in person day-of: ID/age verification, guardian consent where locally allowed, medical disclosure, sobriety statement, risk acknowledgment, aftercare agreement, optional photo release, client+artist signatures with date/time, artist license number where required, record retention; "some shops lump these into one form or skip one altogether"; digital standard + paper backup; store with appointment + client record; day-of "bring an ID" reminders)

Reused cross-product context (recorded in sibling research passes, sources reachable on those days):

- Vagaro calendar/status/checkout/customer structure; Zenoti API object model — Tier-1 (research/appointment-based-service-business-management.md, 2026-09-06)
- Vagaro Forms vs SOAP Notes structural rule (client-facing forms vs staff-only clinical notes) — Tier-1 (research/massage-practice-management.md, 2026-09-08)
- Variant resolutions for barbershop / massage / med-spa / nail-salon — sibling passes 2026-09-06/08

Access limitations (recorded per evidence rules):

- Bookedin help center unreachable (transport error + timeout) — deposit/form operational mechanics rest on official blog + vertical page (Tier 2); no precise limits asserted.
- DaySmart Body Art support center not fetched — Tier-2 evidence only for that product.
- Tattoo Studio Pro unreachable (parked domain); Timely/Mangomint tattoo pages 404; PocketSuite has no tattoo vertical — the tattoo-native pole rests on one product (DaySmart Body Art, Tier 2).
- Vagaro marketing site 403 (this pass and prior passes); help center reachable (Tier 1).
- Consequence: precise operational details (deposit minimums, form limits, plan gates) are deliberately not asserted; structure-level claims only where evidence supports them.

## Product Observations

### DaySmart Body Art / InkBook (evidence layer: A — Tier-2 product pages, unusually specific; support center not fetched)

Positioning: "Piercing & Tattoo Studio Software"; "Tattoo Studio Software That Works as Hard as You Do… keep your schedule straight, track inventory and manage payroll, clients, campaigns and payments"; "Crafted for Your Piercing & Tattoo Business… the all-in-one studio management solution." Footer: "Powered by InkBook"; business login at `online.inkbooktattoosoftware.com`; mobile app listed as "InkBook Software". Packages framed for "an independent tattoo artist or a multi-artist business" — "piercing and tattoo scheduling software packages."

- **Appointment book**: "A Digital Tattoo Appointment Book"; integrated calendars; "Appointments made online must be accepted by you before they go on your books" (approval mode); "previously booked times are not offered as available online. No risk of double-booked appointments"; automatic reminders ("Eliminate no-shows"); color-coding, smart filters, customizable dashboard.
- **Multi-session work**: recurring appointments — "Keep multi-session, repeat, and recurring clients on schedule with the recurring appointments feature… **Lock down the time that works until that piece is done.** Simply enter the information once and let DaySmart's tattoo booking software do the rest." Multi-session tattoo projects are realized as recurring/repeat appointments, not a separate project object.
- **Forms ("Tattoo & Piercing Release Form App")**: drag-and-drop builder — single/multiple choice, dropdowns, sliders/scales, date/time, short/long answer, **signature capture**, required/optional answers, headers/paragraphs/separators, preview mode. Requirement modes per form: not required / required each time an appointment is booked / required only the first time. "Designate which services require forms completion **before services can be rendered**." Forms tab roster (status, responses, date created). "**When new appointments are added that require a release form(s), DaySmart Body Art will show an alert status on that appointment until the required form(s) have been returned completed.** At appointment time, you'll know at a glance if your next customer is in compliance or not." Sent via text/email from the appointment book; per-client record shows completed/outstanding forms. Use cases named: COVID-19 screenings; "Ensure applicable services are compliant and clients understand the rules involved with the consent form app."
- **Client management ("Tattoo CRM & Client Management")**: digitized client records; personalize service "by reviewing notes, past work or purchase history". Detailed Notes: "Take notes **before appointments and after**, upload and attach **photos** to client records, **store release forms**, contact information and more." Loyalty/membership programs. "**DaySmart Body Art customers who are eligible for loyalty programs are also eligible to take deposits and securely hold client credit card information on file** for ease of payments." Retail inventory tracking. Integrated payment processing (EMV desktop devices). Customizable online gift cards.
- **Online booking**: free themed website (hosted or custom domain); 24/7 tattoo and piercing booking; gift cards; booking from the shop's Facebook page; studio is "notified automatically when a client books online. Once you **accept or reject the client request**, DaySmart Body Art will notify the client by email—automatically."
- Suite breadth: text marketing, email marketing, 2-way texting, reputation management (solicit reviews, head off complaints), payroll processing, QuickBooks sync, business reports, mobile apps, website builder.

### Bookedin (evidence layer: A/B — Tier-2 vertical + features pages and official blog; help center unreachable)

Positioning: "Tattoo Appointment Scheduling Software Built for Artists & Studios"; tattoo shops listed first among industries; named customers: Oriana Tattoo (Miami Beach), Daredevil Tattoo (NYC), Twistid Ink, private studio owners, a tattoo-and-piercing shop (The Lotus Pod), Ink Embassy (Australia); "used by thousands of studios across the U.S., Canada, the U.K., and Australia" (vendor claim — recorded, not asserted).

- **Vendor's own category definition**: "Tattoo appointment scheduling software lets tattoo artists and tattoo shops accept online bookings, manage calendars, collect deposits, and automate client reminders from one platform."
- **Booking**: clients book "consultations or appointments online and pay the deposit before they even sit down in your chair"; 24/7 booking page, no app/login required; booking link on Facebook/Instagram/website; multi-artist shops — "clients can choose the artist they want at the time they want. Booked time slots are automatically greyed out, so you'll never double book."
- **Service-type patterns (FAQ)**: "You can set up separate service types: **consultations (free or paid), deposits-required appointments, and walk-in slots.** Each can have its own booking rules and duration."
- **Deposits**: "Bookedin lets you require a deposit at the time of booking — **clients pay before they are confirmed on your calendar**. This dramatically reduces no-shows for long and expensive tattoo sessions." "Deposits, prepayments, and automated SMS/email reminders help reduce no-shows." Payment via credit/debit/Venmo/PayPal; connects to Square, Stripe, or PayPal processors; payment requests any time.
- **Client records**: "The platform can store **client notes, reference images, tattoo placement details**, past appointments, and **deposit history** in secure client profiles." Features page: custom profiles with tailor-made fields, photos and documents attached, full booking history "including cancellations and no-shows", import existing lists.
- **Messaging**: automatic confirmations, reminders, "preparation instructions, and **tattoo aftercare advice** via text and email"; "attach aftercare information to your confirmation and follow-up messages so every client receives it automatically"; follow-up emails (thank-you an hour after; rebooking sequences by service).
- **Booking form vs consent form (official blog, 2026-07)**:
  - Booking form (pre-appointment, on the booking page after date/time/artist): contact info; **tattoo type (flash or custom)** — "Flash is quicker to schedule; custom needs design time and possibly a consult"; concept (1–2 sentences); **placement and approximate size** (drive price, difficulty, session length, healing); style categories (fine line, traditional, blackwork, realism, neo-traditional); reference images (2–3); budget range; availability; optional simple health check (scheduling-relevant factors only); **deposit agreement line** (nonrefundable or transferable). "Avoid asking comprehensive medical questions… don't ask the client to sign any legal documents" at this stage.
  - Consent form (**signed in person, right before the session starts**): verify government-issued ID and local age requirement (guardian info where minors are locally allowed); medical disclosure (allergies, conditions, blood thinners, pregnancy, recent sunburn/illness); sobriety statement; risk acknowledgment; aftercare agreement; optional photo/video release; **client and performing-artist signatures with date and time**; artist license/registration number where locally required; record-retention statement. "Get fresh, informed consent right before the session." Digital as standard + paper backup; scan-and-upload paper forms to the client profile; "Store consent info with the exact appointment and client record"; day-of reminders ("bring an ID").
  - Notably: "You might've heard of instances where shops simply lump these into one form **or skip one altogether**" — shops operate without the digital form layer.
- **Features page**: online booking (appointments/classes/workshops; flexible availability by day/week/service; recurring bookings with conflict checks; custom booking forms; add-on services); reminders (text with reply-to-confirm; custom emails with attachments, per-service messages, cancellation policy; follow-up email sequences); marketing (Google listings, Facebook/Instagram, email-list export, ad-tracking pixels); payments (get paid upfront/deposits; payment requests; Square/Stripe/PayPal); client & business insights (client list & history; one-click call/text/email; activity & reports — bookings, no-shows, cancellations, Excel export); security (staff security roles — four access levels, per-calendar visibility; two-step verification; SSL); mobile app; 2-way calendar sync (Google/Outlook/Apple/Exchange); company branding.
- Plans: free plan (up to 20 bookings/month) and paid plans from $20/month (pricing-page claims — recorded here only).

### Vagaro (evidence layer: A — Tier-1 help center fetched this pass; suite structure Tier-1 from sibling passes 2026-09-06)

Positioning: appointment-business suite for salon/spa/fitness/wellness; tattoo present as a business type and professional category; consumer marketplace app; HIPAA Compliant + PCI DSS badges on the support site.

- **Tattoo as a served vertical (Tier 1)**: "Set Your Business Type" article lists tattoos / tattoo removal among selectable business types (search snippet). "Portfolio Image Tips": "Only images related to Barber, Beauty, Fitness, Wellness, **Tattoo**, and Pet Grooming services are eligible for approval" — professionals carry approval-gated portfolio images, tattoo included.
- **Deposit machinery (Tier 1, full article)**:
  - Definition: "Deposits, also called upfront payments, down payments, or advance amounts, help prevent no-shows, late cancellations, and profit loss by making sure timeslots are not wasted. **When a customer no-shows or cancels their appointment or class, you get to keep their deposit.**"
  - Configuration: on the public listing page as an upfront cost or percentage, or manually charged from the calendar ("enter the Deposit Due or select Deposit % … Select Charge Deposit"); requires Credit Card Processing + Online Shopping Cart.
  - Setup parameters: Deposit Due (fixed or percentage); "For Bookings Greater Than or Equal To" minimum-price threshold; which customer types require the deposit — new customers / existing customers / mobile-service appointments / **customers with prior no-shows or cancellations**; cancellation-policy text shown with the booking.
  - Calendar visibility: deposit-state icons — **100% Prepaid Appointment, Partial Deposit, Deposit Paid by Membership, Deposit Paid by Package**.
  - Money behavior: membership or package visits can fully pay a deposit; deposit recalculated when a membership partially discounts; cards used online are auto-stored on the customer profile; deposit funds arrive one business day after payment; with Vagaro Payroll, the deposit is attributed to the payroll cycle of the appointment date (Sold By editable on the Transaction List).
  - Refunds: configurable — automatic refund of prepaid appointments/deposits on cancellation is a toggle (Online Appointment Rules); by default deposits are non-refundable (support reply); manual refund from the customer profile; Deposits Report for deposit history.
  - Vendor limitation (support reply): one universal deposit rule per business — no per-service deposit tiers (feature-request threads confirm).
  - Related machinery: Automatically Charge a Cancellation or No-Show Fee; Require a Credit Card on File to Book.
- **Generic-suite structure (Tier-1, sibling passes 2026-09-06, reused)**: services with categories/add-ons/bundles/packages/memberships/gift cards/retail inventory; resources (rooms/equipment); customer profiles with appointment history/notes/tags/no-show counters; full documented appointment status set (Requested → Accepted → … → Complete; No-Show/Cancel with fees); checkout with split payment, discounts-with-approval, tips, taxes, package/membership/gift-card redemption, cards on file, refunds; employee schedules and payroll; consumer marketplace; multi-location.
- **Forms and SOAP Notes feature area (Tier-1 category; details from massage-pass Tier-1)**: client-facing forms (templates, mandatory, login-required, expiration, signature/file elements, sent from calendar/checkout/profile/link/embed) vs staff-only SOAP notes (cannot be required at online booking; service binding; per-employee access control). For tattoo studios the forms side is the relevant layer; the SOAP side is clinical-adjacent machinery the suite carries for other verticals.

## Cross-product Comparison

| Structure | DaySmart Body Art (InkBook) | Bookedin | Vagaro | Evidence |
|---|---|---|---|---|
| Bookable service catalog with duration + price | ✔ (tattoo & piercing services; packages for solo→multi-artist) | ✔ (consultations / deposit-required appointments / walk-in slots as service types with own rules & duration) | ✔ (Tier-1 sibling; tattoo a business type) | B |
| Identified client records with history | ✔ (Tattoo CRM; notes before/after; photos; release forms stored) | ✔ (notes, reference images, placement details, deposit history, cancellations/no-shows) | ✔ (Tier-1 sibling) | B |
| Appointment binds client × service × artist × time | ✔ (digital appointment book; per-artist) | ✔ (multi-artist calendars; clients choose artist; no double-booking) | ✔ (Tier-1 sibling; portfolio per professional) | B |
| Appointment lifecycle; cancel/no-show as named outcomes | ✔ (accept/reject online requests; reminders) | ✔ (booking history incl. cancellations & no-shows; reply-to-confirm) | ✔ (Tier-1 sibling status set) | B |
| Checkout resolving the visit into recorded money | ✔ (integrated EMV payments; tickets) | ✔ (upfront + payment requests; processors) | ✔ (Tier-1 sibling checkout) | B |
| Online self-booking page | ✔ (free website; 24/7; Facebook) | ✔ (24/7; social/website embeds) | ✔ (listing page; Tier-1 sibling) | B |
| Approval mode on online bookings | ✔ (accept/reject before going on the books) | ◐ (deposit-before-confirmation; notifications on book/confirm/cancel) | ◐ (appointment rules; Tier-1 sibling) | B |
| Deposits collected at booking | ✔ (deposits + cards on file) | ✔ (deposit before confirmation; "long and expensive sessions") | ✔ (Tier-1: fixed/%, thresholds, customer-type targeting, icons, forfeiture, refund config, report) | B |
| Deposit kept on no-show/cancellation | ◐ (not explicit on fetched pages) | ◐ (implied: deposits reduce no-shows; deposit-agreement line in booking form) | ✔ (Tier-1 verbatim: "you get to keep their deposit"; default non-refundable) | A (single product explicit) |
| Consent/release forms bound to services & appointments | ✔ (release-form app; per-service requirement; alert on appointment until returned; "in compliance at a glance"; stored on client record) | ✔ (consent-form guidance; store with appointment + client record; day-of signing) | ◐ (generic Forms area: mandatory, expiration, service binding; consent framing not tattoo-specific) | B |
| Booking-form intake of project content (concept/placement/size/style/reference images/budget) | ◐ (photos + notes on client records; custom fields not evidenced) | ✔ (booking-form field list; custom booking form fields) | ◐ (custom fields via forms; not tattoo-specific) | B (Bookedin explicit) |
| Multi-session / repeat work | ✔ (recurring appointments — "until that piece is done") | ✔ (recurring bookings with conflict checks) | ◐ (not verified this pass) | B — 2/3 |
| Consultations as bookable service type | — (not observed) | ✔ (free or paid consultations) | ◐ (consultation = ordinary service) | product-specific pattern |
| Walk-in slots as managed service type | — (not observed) | ✔ (walk-in slots with own rules) | — (not observed) | product-specific |
| Aftercare / prep messaging | — (not observed on fetched pages) | ✔ (aftercare advice attached to confirmations/follow-ups) | ◐ (custom emails/messages; not tattoo-specific) | B — thin |
| Artist portfolio | ◐ (website builder with photos; reputation mgmt) | ◐ (staff profile photos/branding) | ✔ (portfolio images incl. tattoo, approval-gated — Tier-1) | B |
| Retail product sales | ✔ (inventory; aftercare-adjacent retail) | ◐ (add-on services/products at booking) | ✔ (Tier-1 sibling) | B |
| Gift cards | ✔ (customizable online gift cards) | — (not observed) | ✔ (Tier-1 sibling) | B |
| Loyalty / memberships | ✔ (loyalty/membership programs) | — (not observed) | ✔ (Tier-1 sibling) | B |
| Payroll / commissions | ✔ (payroll processing) | — (not observed) | ✔ (Tier-1 sibling; deposit-payroll attribution) | B — suite pole |
| Multi-location | — (not observed) | — (not observed) | ✔ (Tier-1 sibling) | B — suite pole |
| Marketplace / directory posture | — (not observed) | ◐ (public business directory) | ✔ (consumer marketplace; Tier-1 sibling) | B — optional posture |
| Website builder | ✔ (free themed website) | ◐ (booking page as website substitute; embeds) | ◐ (MySite category) | B |
| Staff roles / permissions | ◐ (employee management) | ✔ (four access levels; per-calendar visibility) | ✔ (Tier-1 sibling) | B |
| 2-way texting | ✔ | ◐ (one-click text; reply-to-confirm) | ✔ (Tier-1 sibling) | B |
| Reputation / review management | ✔ (solicit reviews, head off complaints) | ◐ (Google listings; ad tracking) | ◐ (marketing suite; Tier-1 sibling) | B |
| Age verification / ID-check tooling | — (not observed) | ◐ (ID-check practice + "bring an ID" reminders in official guidance; no ID-scan tooling observed) | — (not observed) | guidance-level only |
| Piercing in scope | ✔ (named in product title/pages) | ◐ (tattoo-and-piercing customer evidence) | — (not observed) | B |

Legend: ✔ directly observed for that product; ◐ observed indirectly/partially; — not observed in fetched sources.

## Canonical Model

### Level 0 — Defining Invariant

Smallest structure without which the product stops being recognizable as tattoo studio management:

1. **Bookable body-art service catalog** — the studio's service menu (tattoo sessions of various kinds, piercings, consultations), each with its own duration and price.
2. **Identified client records** — persistent, individually identified clientele (the studio remembers the person, their history, and their project content, not just transactions).
3. **The appointment as central binding object** — an appointment binds a client, a service, and the artist who performs it, into a time slot; artist availability makes the slot bookable.
4. **Lifecycle to service delivery** — the appointment moves from booked (optionally confirmed/approved) through arrival to the session being performed and completed, with cancellation and no-show as named alternative outcomes.
5. **Checkout resolving the session into recorded money** — the completed session becomes a chargeable visit recorded against the client (direct payment, deposit-then-balance, or redeemed prepaid value).

Justification tests:

- Remove catalog + appointment binding → generic scheduling application.
- Remove checkout + client ledger → an appointment scheduler remains.
- Remove the appointment/calendar → a POS or invoicing tool remains.
- Remove deposit machinery → still tattoo studio management (deposits are a configuration on the generic core; Vagaro's Tier-1 article treats them as optional settings; analog shops ran on cash deposits or verbal commitments).
- Remove consent/release forms → still runs (Bookedin's own guidance documents shops that "lump these into one form or skip one altogether"; paper consent forms are the analog baseline; DaySmart ships forms as an activatable feature area).
- Remove multi-session/recurring structure → single-session shops still run.
- Remove design/reference content → the generic core still runs.
- Historical check: paper-era tattoo shop — appointment book with per-artist columns + deposit log/carbon slips + paper consent forms signed day-of + design sketches and reference pictures in client folders + cash at the desk — satisfies all five legs at analog level. InkBook's desktop-software generation satisfies with no cloud/AI/marketplace machinery. The definition does not overfit the current cloud generation.

Joint-review resolution (owed to the appointment-based pass): every Level-0 element is identical to the generic appointment-business core. Tattoo differences concentrate in emphasis and overlay, not in new object types. Verdict: **tattoo/piercing-industry Variant of Appointment-based Service Business Management, keep-both** (barbershop/massage/med-spa/nail precedent); recorded in STATUS.md. The med-spa passes' removal test is discharged: removing the regulated-treatment layer lands exactly here — the tattoo visit economy carries **no clinical-documentation class** (no provider-facing charting object was observed in any sampled product; consent forms are client-facing legal documents, not clinical notes).

### Level 1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected of mature products but not defining:

- Online client self-booking page (24/7; social/website embeds; commonly with studio approval of online requests).
- Automated confirmations and reminders (SMS/email), commonly carrying preparation instructions and aftercare information.
- **Deposit collection at booking** — fixed or percentage, charged before confirmation; card auto-stored on the client profile; deposit state visible on the calendar; deposit history/report; refund behavior configurable (default non-refundable in the one product with explicit evidence).
- Cancellation/no-show policy machinery (fees, cards on file, booking restrictions for clients with no-show history).
- Client records carrying **body-art project content**: notes before/after sessions, reference images, placement/size details, photos, documents, deposit history.
- Multi-artist calendars; clients choose the artist; per-artist schedules and (in the generic pole) portfolio images.
- Recurring/repeat bookings used for multi-session work.
- Consent/release forms: digital form builder with signature capture; per-service requirement; completion alerts on the appointment; forms stored on the client record.
- Retail product sales (aftercare-adjacent), gift cards, loyalty/memberships at the suite poles.
- Reporting (bookings, no-shows, cancellations, revenue); staff roles/permissions; 2-way texting; reputation/review management.

### Level 2 — Variant / Optional Structure

Depends on packaging philosophy, region, and business model:

- **Packaging poles** — (a) tattoo/piercing-native studio product (DaySmart Body Art/InkBook); (b) small-business booking platform with a dedicated tattoo vertical (Bookedin); (c) generic multi-vertical appointment suite serving tattoo as a business type (Vagaro).
- **Consultations as a distinct bookable service type** (free or paid) — explicit in one product; elsewhere consultations are ordinary services.
- **Walk-in slots as a managed service type** (flash-style demand beside booked custom work) — explicit in one product.
- **Flash vs custom work** as a scheduling/pricing distinction (custom needs design time and possibly a consult) — industry practice documented in vendor guidance, realized through service types and booking-form fields.
- **Marketplace/directory posture** — public business directory (Bookedin), consumer marketplace app (Vagaro); absent in the tattoo-native pole.
- **Website builder** bundled (free themed website in the tattoo-native pole; booking-page-as-website elsewhere).
- **Payroll/commissions depth, multi-location** — suite-pole capabilities.
- **Payment-processor posture** — integrated merchant services (Vagaro deposits require its own merchant services) vs bring-your-own processors (Square/Stripe/PayPal in Bookedin).
- **Regional consent law** — age-of-consent variation, guardian consent where minors are locally allowed, artist license/registration numbers where required; ID-check is practice guidance, not observed tooling.
- **Era-specific health screenings** (COVID-19 screening forms) — a form-template use case, not a structure.

### Level 3 — Vendor-specific (research notes only)

- DaySmart Body Art: "Powered by InkBook" lineage and `inkbooktattoosoftware` login host; recurring-appointments framing "lock down the time that works until that piece is done"; form requirement modes (every booking vs first booking only); Forms tab roster with response counts; alert-on-appointment compliance state; deposits/cards-on-file gated to loyalty-eligible customers (unusual gating — wording ambiguous, recorded as uncertainty); free themed website; Facebook booking; QuickBooks sync; reputation management; EMV desktop devices.
- Bookedin: "3 reminders per booking" claim; free plan (20 bookings/month) and $20/month entry price; consultations/deposit-required/walk-in service-type patterns; Venmo/PayPal plus bring-your-own Square/Stripe/PayPal; four staff access levels with per-calendar visibility; follow-up email sequences (thank-you + rebooking); consent-form template giveaway; "more than 80% reduction in no-shows" marketing claim; tattoo industry-statistics report.
- Vagaro: deposit-state icons (100% Prepaid / Partial Deposit / Deposit Paid by Membership / Deposit Paid by Package); one universal deposit rule per business; deposit funds next business day; payroll-cycle deposit attribution with Sold By editing; auto-refund toggle; deposit targeting by customer type (new/existing/no-show-history/mobile); minimum-price threshold; deposits require Vagaro Merchant Services; portfolio-image approval categories; E-Prescribe category (suite breadth beyond this Type); Forms vs SOAP Notes staff-only rule (Tier-1, from the massage pass).

## Rejected Findings

- **"Deposit machinery is part of the defining core"** — rejected: deposits are a no-show-protection configuration on the generic appointment core (Vagaro's Tier-1 article configures them as optional settings shared across verticals; the analog shop ran on cash deposits). Deposits are the Type's most characteristic *emphasis* — in tattoo they are commonly required before confirmation for long, expensive custom sessions — but a studio system without deposit machinery still serves the studio.
- **"Consent/release forms are definitional"** — rejected: Bookedin's own guidance documents shops that skip or lump forms; DaySmart ships forms as a feature area with per-service activation; paper consent forms are the analog baseline. The consent layer is the Type's most characteristic compliance overlay, not its invariant.
- **"Multi-session work requires a first-class 'project' object"** — rejected: sampled products realize multi-session work through recurring/repeat appointments ("lock down the time… until that piece is done"), not a separate project object. No evidence of a project object in any fetched source.
- **"A design/artwork approval workflow is part of the Type"** — rejected: no sampled product documents a design-approval object or workflow; design content lives in booking-form fields (concept, placement, size, style, reference images) and client-record notes/photos. (Uncertainty recorded — some products may offer it; not observed.)
- **"Tattoo studio management is a distinct object model from generic appointment-business software"** — rejected after comparison: all defining elements are shared; differences are overlay/emphasis (deposit-centric booking economics, consent/compliance forms, body-art project content, multi-session recurrence, artist-as-unit, aftercare messaging) — mirrors the barbershop/massage/med-spa/nail resolutions.
- **"Marketplace discovery is part of the Type"** — rejected: consumer-side discovery belongs to marketplace Types; observed only as optional posture (Bookedin directory, Vagaro marketplace).

## Boundary Findings

1. **vs Appointment-based Service Business Management (generic Type)** — defining core identical (catalog + clients + appointment binding + lifecycle + checkout). Tattoo Studio Management is the tattoo/piercing-industry variant: same core with characteristic emphases (deposit-at-booking economics for long custom sessions, consent/release-form compliance layer, body-art project content on client records, multi-session recurrence, artist-as-bookable-unit, aftercare messaging). Joint-review conclusion: **probable industry Variant, not an independent Type; keep-both** per the sibling precedent. This document still describes the Type as it manifests in tattoo studios, with the variant relationship stated in Related Application Types. DISCHARGES the appointment-based pass's sibling flag from this side.
2. **vs Salon / Barbershop / Spa / Med Spa / Nail Salon Management (§29 siblings)** — same generic core; different overlays. The med-spa passes' removal test is discharged from this side: remove the regulated-treatment layer and the med-spa business runs on the same visit economy — and the tattoo economy carries **no regulated-treatment/clinical-documentation layer at all** (consent forms are client-facing legal documents; no provider-facing charting class observed). Tattoo's distinguishing overlays vs the beauty siblings: deposit-before-confirmation as the norm for custom work, day-of informed-consent signing with ID/age verification, and project-content intake (concept/placement/reference images).
3. **vs Appointment Scheduling Application (03.09)** — remove the client ledger and checkout → a scheduling application remains. Holds for all three sampled products.
4. **vs Retail POS (05.10)** — payment spine shared; remove the booking/calendar and service-delivery context → POS. Retail sales appear in all poles (aftercare products, jewelry-adjacent retail at suite poles).
5. **vs Beauty Service Marketplace / Service Marketplace (05.02/§29)** — marketplace is consumer-side discovery across providers; this Type manages one studio. Marketplace posture is an optional variant here (Bookedin directory; Vagaro consumer app).
6. **vs Digital Waiver Management (§26, unprocessed)** — the consent/release-form layer here is a feature inside the studio system, bound to appointments, services, and client records (completion alerts, per-service requirements, storage on the record). A standalone waiver-collection Type would make the waiver the primary object; forward seam flagged for that leaf's pass.
7. **vs Practice Management System / Patient Scheduling (§22)** — no clinical charting class in the sampled tattoo products; the §22 seam holds (med-spa precedent ratified: documentation depth alone does not merge with §22, and here there is no documentation class to begin with).
8. **vs Beauty Professional Business App (§29)** — solo-artist packaging (Bookedin private-studio owners; DaySmart independent-artist packages) is adjacent packaging over the same core; the sampled tattoo-native product remains studio/account-oriented. Boundary held at packaging level; left to that leaf's own pass.

## Uncertainties

- Bookedin help center unreachable (2 failures): deposit/form operational mechanics rest on official blog + vertical page (Tier 2); no precise limits asserted.
- DaySmart Body Art support center not fetched: form/deposit mechanics from product pages (Tier 2); the "loyalty-eligible customers are also eligible to take deposits" wording is ambiguous (eligibility gating unclear) — recorded, not asserted.
- Whether any tattoo-native product carries a first-class design/artwork object or approval workflow: not observed in any fetched source; unverified either way.
- Touch-up policies (free/charged touch-ups): not observed in fetched sources; not claimed.
- ID-verification tooling (scanning): not observed; only ID-check practice guidance documented.
- Vagaro tattoo-specific depth (how tattoo studios use the suite in practice): only business-type + portfolio evidence; no tattoo-specific workflow claims made.
- Piercing-specific machinery (jewelry inventory, piercing records, sterilization tracking): DaySmart names piercing in scope but no piercing-specific structure observed beyond the service catalog; recorded as uncertainty.
- Multi-session handling in Vagaro (recurring appointments) not verified this pass; claimed only for 2/3 sampled products.

## Final Synthesis

Tattoo Studio Management is best understood as **the tattoo/piercing-industry expression of appointment-based service business management**: a studio operating system organized around the body-art session. Its world contains a bookable service catalog (tattoo sessions, piercings, consultations — each with duration and price), an identified client population, and the appointment as the central binding object — client × service × artist × time — carried through a lifecycle from booking (commonly with studio approval of online requests) through arrival to the completed session, terminating in checkout where the session becomes recorded money. What gives the tattoo variant its shape is the overlay around that core: **deposit-centric booking economics** (deposits commonly required before confirmation for long, expensive custom sessions, with forfeiture on no-show and configurable refunds); a **consent/compliance form layer** (client-facing intake at booking — concept, placement, size, style, reference images, budget — and day-of informed-consent forms signed in person with ID/age verification, health disclosure, and client+artist signatures, bound to the appointment and stored on the client record); **body-art project content** living on client records (notes, reference images, placement details, photos, deposit history); **multi-session work** realized as recurring/repeat appointments ("until that piece is done"); the **artist as the bookable unit** with per-artist calendars and portfolios; and **aftercare/prep messaging** attached to confirmations and follow-ups. The market realizes one Type in three packaging poles — tattoo/piercing-native studio product, small-business booking platform with a tattoo vertical, generic multi-vertical suite — and the defining core itself is shared with the generic appointment-business Type: this leaf is its tattoo variant, as the prior joint-review flag predicted and the sibling precedents resolved.
