# Research Notes — Massage Practice Management

Research date: 2026-09-08

## Research Goal

Understand the software category used by massage therapists and massage/bodywork practices to run their business — booking, clients, treatment documentation, packages, checkout, and the wellness-practice-specific machinery around them — and determine whether "Massage Practice Management" is a structurally independent Application Type or the massage-industry variant of the generic appointment-based service business category. This pass owes a joint-review resolution to the flag recorded when `appointment-based-service-business-management` was processed (2026-09-06), which listed this leaf among probable industry Variants; the `barbershop-management` pass (2026-09-06) set the precedent for resolving such flags.

## Initial Boundary

Initial hypothesis (before research):

- The leaf sits in Directory §29 between "Med Spa Management" and "Nail Salon Management", surrounded by industry-specific siblings (salon, barbershop, spa, med spa, nail, tattoo) and near the generic "Appointment-based Service Business Management" leaf.
- Expected massage-specific overlays to test (not assumed defining):
  - **Clinical documentation layer** — massage intake is famously health-history-based (contraindications, medications, conditions); treatment/session notes (SOAP-class) are a professional norm for licensed massage therapists.
  - **Packages/series economics** — prepaid series of sessions are a classic massage-practice revenue structure.
  - **Insurance claiming** — in some regions (Canada, Australia/NZ, parts of the US), massage therapy is claimable against health funds; products may carry claiming machinery.
  - **Compliance posture** — health-adjacent client data (HIPAA-class) may be a first-class concern.
  - **Mobile/outcall service** — house-call massage is a known practice mode.
- Closest neighbors to test against: Appointment-based Service Business Management (generic core), Spa Management System / Med Spa Management (siblings), Practice Management System & Patient Scheduling (§22 — the clinical-pole seam), Appointment Scheduling Application (03.09), Retail POS (05.10), Beauty Service Marketplace / Service Marketplace (§05.02/§29).

## Research Questions

1. What objects make up a massage practice management system's world, and do they differ structurally from the generic appointment-business core?
2. How is the clinical-documentation layer structured — client-facing intake vs practitioner-facing treatment notes; what binds them to the client record and to services?
3. How do prepaid packages/series work (sale, redemption, expiry)?
4. Is insurance claiming a defining or regional/optional capability?
5. How do packaging philosophies differ (massage-native product vs allied-health practice management vs generic appointment suite vs enterprise spa platform)?
6. Which capabilities are common vs optional (self-booking, reminders, waitlist, no-show protection, marketing, multi-location, mobile service, marketplace)?
7. Boundary tests: what would have to be removed for this to become a scheduling app, a POS, an allied-health EHR, or a marketplace?
8. Historical check: would a paper-era massage practice (appointment book + client cards + SOAP notes + punch-card packages) still fit the definition?

## Representative Products

| Product | Segment / philosophy | Customer tier | Why selected |
|---|---|---|---|
| ClinicSense | Massage-native clinic management: SOAP notes + intake forms at the center, "originally built for solo massage therapists" | Solo → small clinic | The massage-native philosophy pole |
| Zanda (formerly Power Diary) | Allied-health practice management with a dedicated Massage Therapy vertical; EHR-flavored (clinical notes, body charting, claiming) | Solo → group practices | Clinical-practice-management pole, global/AU-US |
| Vagaro | Generic salon/spa/fitness appointment-business suite serving massage as a wellness vertical; Tier-1 help center documents Forms + SOAP Notes | SMB → chains → multi-location | Generic-suite pole with first-hand clinical-add-on evidence |
| Zenoti | Enterprise spa/salon/wellness platform (massage/spa services in scope); full object model via Tier-1 API docs | Enterprise / chains | Enterprise tier; spa-pole structure (rooms, therapist schedules, series packages) |

Sampling notes:

- MassageBook (the best-known massage-native suite) was a primary target but `massagebook.com` returned HTTP 403 and `help.massagebook.com` failed with a transport error — abandoned after 2 attempts per network rules; no MassageBook evidence used. (ClinicSense's own comparison page confirms MassageBook is a same-category competitor.)
- Mindbody: `mindbodyonline.com/business-types/massage` returned 404; root site evidence for the wellness-marketplace pole was already recorded in the `beauty-service-marketplace` sibling pass (2026-09-06) and is used only as cross-product context, not as a sampled product here.
- Fresha/Booksy: recorded as unreachable (403) in multiple prior sibling passes; not retried.
- ClinicSense help center (`support.clinicsense.com`) timed out on first fetch — not retried; ClinicSense assertions rest on its product pages (Tier 2), which are unusually specific.

## Sources

Tier 1 (official operational documentation), fetched 2026-09-08:

- Vagaro Support — Help Center home: https://support.vagaro.com/hc/en-us
  - Category list includes: Checkout; Calendar and Scheduling; Things You Sell; Customer Management; **Forms and SOAP Notes**; Employee Management; Payroll; Reports and Dashboard; Check-in App; E-Prescribe; Marketing Your Business. Footer badges: HIPAA Compliant, PCI DSS Compliance.
  - Forms and SOAP Notes category: https://support.vagaro.com/hc/en-us/categories/24397607931675-Forms-and-SOAP-Notes
    (articles: Activate the Vagaro Forms Feature; Create a Form Template; Create a New SOAP Note Template; Make Forms Mandatory for Your Customers; Require Customers to Log In When Completing a Form; Send a Notification When a Form is Completed; Set an Expiration Date for a Form; **Using Forms vs. SOAP Notes**; Require a SOAP Note for Services; Import Forms and SOAP Notes; Convert Forms and SOAP Notes; Allow or Block Employee Access to Forms & SOAP Notes; fill from profile/calendar/checkout/link/embed; edit/delete/print/download responses; view summary; see who filled out)
  - "Create a New SOAP Note Template": https://support.vagaro.com/hc/en-us/articles/15732373708315-Create-a-New-SOAP-Note-Template
- Zenoti API documentation (llms.txt index): https://docs.zenoti.com/llms.txt
  (centers, rooms, employees/therapists, schedules/blockouts, services/variants/add-ons/price-scaling, guests/notes/forms/relationships, service-booking flow create→slots→reserve→confirm→collect payment, group/couple bookings, series packages, memberships freeze/unfreeze, gift cards, coupons, opportunities)

Tier 2 (official product pages), fetched 2026-09-08:

- ClinicSense home: https://clinicsense.com/
- ClinicSense Massage Therapy page: https://clinicsense.com/professions/massage-therapy-software
  (feature groups: Charting — SOAP notes / Intake forms / Consent forms; Scheduling — Online booking / Appointment reminders / No-Show Guard; Financial — Invoicing & payments / TELUS Health eClaims / Treatment packages / Gift certificates / Square integration / Reports; Communication — newsletters / availability summary / wellness check-ins / feedback & Google reviews / referrals / birthday emails; FAQs incl. HIPAA, solo-therapist origin, booking-page-without-website, switching from pen & paper)
- Zanda home: https://www.powerdiary.com/us/ (redirect target; Zanda Health)
- Zanda Massage Therapy page: https://www.powerdiary.com/profession/massage-therapy-software
  (positioning "Massage Therapy Practice Management Software"; CRM for massage therapists; HIPAA-compliant charting; AI SOAP notes; client portal; rooms/resources on calendar; invoices at session end; Medicare/DVA/NDIS + US insurance billing; testimonials from home-based/mobile massage businesses)

Reused cross-product context (recorded in sibling research passes of 2026-09-06, sources reachable that day):

- Vagaro calendar/status/checkout/customer structure — Tier-1 (research/appointment-based-service-business-management.md, research/barbershop-management.md)
- Zenoti booking/invoice/member-guest structure — Tier-1 API docs (same passes)
- Mindbody wellness-marketplace positioning — Tier-2 (research/beauty-service-marketplace.md)

Access limitations (recorded per evidence rules):

- MassageBook: 403 + transport error, abandoned. Consequence: the massage-native pole is evidenced by ClinicSense product pages only (Tier 2); no claims about MassageBook anywhere.
- ClinicSense help center: timeout ×1; Tier-2 evidence only for that product.
- Zanda knowledge base (support.zandahealth.com) not fetched; assertions from product pages (Tier 2).
- Consequence: precise operational details (template limits, redemption rules, fee mechanics, plan gates) are deliberately not asserted; structure-level claims only where evidence supports them.

## Product Observations

### ClinicSense (evidence layer: A/B — Tier-2 product pages, unusually specific; help center unreachable)

Positioning: "Clinic management software" for health & wellness practices; massage therapy listed first among professions (massage, physical therapy, osteopathy, clinics, holistic medicine, chiropractic, acupuncture, medical spa); "8,500+ health & wellness businesses" (marketing stat — recorded here only). FAQ: "ClinicSense was originally built for solo massage therapists, and we continue to focus on meeting their needs today." HIPAA-compliant per FAQ. Massage association partners displayed (AMTA, ABMP, RMT Ontario/BC/Saskatchewan/Manitoba/PEI/NL, Canadian massage & osteopathic associations) — deep massage-profession embedding.

- **Charting is the headline**: "Switch from paper client files to online SOAP notes; you'll never feel more organized." Customizable SOAP notes for massage therapists — build templates from scratch or use pre-loaded templates; "no limit to how many templates you can save"; duplicate + update forms for fast note-taking; "Notes, forms, + files automatically stored within the EMR"; one-click SOAP note charting.
- **Intake & consent**: intake forms "automatically emailed to clients"; customizable intake and consent forms with online signatures.
- **Scheduling**: online booking via website or social media, or a free built-in booking page (no website needed); eligibility rules — "Determine which services, practitioners, and even patients are eligible for online booking"; request payment in advance; "block problematic clients from booking online"; SMS/email appointment reminders; waitlist; cancellation policies; No-Show Guard® (branded no-show protection).
- **Financial**: invoicing & payments; clients pay online before booking; automated payment reminders; **treatment packages** (prepaid series); gift certificates ("massage gift certificates"); TELUS Health eClaims (Canadian insurer claiming integration); Square integration; financial reports ("track your monthly revenue").
- **Communication/retention**: post-appointment feedback requests; weekly availability summaries; wellness check-ins; Google reviews; client referrals; birthday emails; newsletters.
- Data model language: client files / EMR / notes+forms+files stored together; "everything you need as a licensed massage therapist" (testimonial).
- Mobile/outcall: "Manage your practice on the move… making house calls or traveling between contracts" (FAQ section); testimonials from home-based practices.
- Switching: "Whether you're currently using pen & paper or another software platform…" (names the analog pre-history).

### Zanda / Power Diary (evidence layer: B — Tier-2 product pages)

Positioning: "Practice management software for health practices"; dedicated profession pages include **Massage Therapy** ("Practice management for massage therapists and bodywork practitioners. Zanda makes it easy to organize appointments, track treatment progress, and handle billing"). Practice types: new / solo / group practices. Compliance badges: ISO 27001, HIPAA, GDPR.

- **Scheduling**: drag-and-drop calendar; hover pop-ups; "up to three automated reminders per appointment"; SMS confirmations auto-update the calendar; waitlists with instant fill suggestions; availability rules (clients only see open times); **rooms or resources booked alongside every appointment**; conflict alerts; multi-practitioner views; multi-location; QR codes & embeds; recurring appointments; group appointments; client profile "at a glance" before each session.
- **Client portal**: clients register on a custom-branded portal, book online 24/7, pay at booking; complete forms and e-sign online; "everything saves automatically to their Zanda client profile".
- **Clinical documentation**: "HIPAA-compliant charting — track progress, manage records, and document treatment with custom templates"; clinical notes with **body charting**; customizable note templates; scored forms track progress and generate reports; **"create AI SOAP notes for massage therapy, turning your conversations and observations into structured documentation"** (BizzyAI).
- **Billing**: Stripe integration (deposit or full payment for online bookings); "invoices are auto-created and sent with a payment link the moment a session ends"; automated unpaid-invoice reminders; **claiming: Medicare, DVA, NDIS (AU) and US insurance billing**.
- **CRM for massage therapists**: two-way email and SMS messaging; secure client portal; client records including referrers and multiple contacts.
- **Reporting**: practitioner utilization, revenue, appointments, invoices; Excel export; public API (beta).
- Telehealth (Zoom) exists as platform capability (less central for massage).
- Testimonials name the massage practice shapes: "home-based Remedial Massage therapy business… SOAP notes for my clients… templates easy to tweak"; "making house calls"; running "massage and personal training businesses".

### Vagaro (evidence layer: A — Tier-1 help center fetched this pass; calendar/checkout/customer structure Tier-1 from same-family sibling passes 2026-09-06)

Positioning: appointment-business suite for salon/spa/fitness (massage inside the Wellness vertical per sibling-pass evidence); consumer marketplace app; HIPAA Compliant badge on the support site.

- **Help-center category map (Tier 1)**: Checkout; Calendar and Scheduling; Things You Sell; Customer Management; **Forms and SOAP Notes**; Employee Management; Payroll; Reports; Check-in App; Marketing. This shows the suite carries the full appointment-business machinery plus a clinical-documentation feature area.
- **Forms vs SOAP Notes (Tier 1, category + articles)**:
  - Forms: templates with elements (short/long answer, choose one, multiple choice, dropdown, custom field, scale, contact, image, photo, date/time, text, separator, signature, file upload, payment); can be made mandatory for customers; login can be required; expiration dates; notifications on completion; sent from the calendar, at checkout, from the customer profile, via link, or embedded on a website; responses editable/printable/downloadable, with summaries and completion tracking.
  - **SOAP notes**: "Subjective, Objective, Assessment, and Plan notes—commonly called SOAP notes—are used by healthcare and wellness professionals to document a client's condition and treatment plan." Five prebuilt templates; blank-template designer; import of existing (paper-era) notes; all submitted notes saved to the customer's profile; fillable from the customer's profile or **required during checkout**.
  - **Service binding**: "Require SOAP Note for Services" — attach a SOAP template to selected services; "Always Require SOAP Note" re-prompts every appointment; required-service bookings show a "Form Required" icon on the calendar.
  - **Structural rule (Tier 1, verbatim)**: "SOAP notes are completed by your business only. Unlike forms, they can't be required during online bookings." → client-facing intake forms vs practitioner-facing treatment notes are two distinct document classes with different enforcement points.
  - **Access control**: "Allow or Block Employee Access to Forms & SOAP Notes" — per-employee permission over clinical content.
- **Generic-suite structure (Tier-1, sibling passes 2026-09-06, reused)**: services with categories/add-ons/bundles/packages/memberships/gift cards/retail inventory; resources (rooms/equipment) with resource calendars; customer profiles with appointment history/notes/tags/no-show counters; full documented appointment status set (Requested → Accepted → … → Complete; No-Show/Cancel with fees); checkout with split payment, discounts-with-approval, tips, taxes, package/membership/gift-card redemption, cards on file, refunds; employee schedules and payroll; consumer marketplace; mobile (at-client-location) services; multi-location.

### Zenoti (evidence layer: A — Tier-1 API docs fetched this pass)

Positioning: enterprise spa/salon/wellness platform; massage/spa services in scope; API surface exposes the full object model.

- **Organization → centers** (multi-location native); **rooms of a center** (listable, retrievable, blockout-able) — the room is a first-class schedulable resource; **employees/therapists** with schedules, attendance, blockout times (one-off and recurring; room blockouts symmetric).
- **Services**: categories; variants; add-ons; **therapist price scaling** (per-therapist pricing for the same service); **therapist-gender preference** at booking (a spa/bodywork-specific option: clients may request a therapist by gender).
- **Guests** (= clients): create/merge (with merge history)/search across centers; **relationships** (spouse, friend, family — group bookings); guest notes (typed; private notes distinguished); **guest forms** (create/retrieve/update; uploaded files, signatures, annotations); saved cards; appointment history; purchase history; gift cards/prepaid cards/coupons; loyalty points.
- **Service booking flow (Tier 1, stepwise)**: create booking → retrieve available slots → reserve slot → confirm → invoice generated on confirmation → collect payment; reschedule = re-run the flow; **group bookings** (host books for family via relationships), **couple bookings**, service bundles, day packages.
- **Commercials**: packages (series) with buy/redeem per guest; memberships with freeze/unfreeze/auto-renewal and pending-collection amounts; gift card templates and sales; coupons; product sale flow; opportunities (upsell pipeline with sales stages) — retention/upsell machinery typical of the enterprise spa pole.
- Not observed in the API surface: SOAP-note/charting endpoints (documentation may exist in the product UI but is not evidenced here — recorded as an uncertainty).

## Cross-product Comparison

| Structure | ClinicSense | Zanda | Vagaro | Zenoti | Evidence |
|---|---|---|---|---|---|
| Bookable service catalog with duration + price | ✔ | ✔ | ✔ | ✔ (variants/add-ons/price scaling) | B |
| Identified client records (client/patient/guest) with history | ✔ (client files/EMR) | ✔ (client records, referrers) | ✔ (Tier-1 sibling) | ✔ (guests, merge, relationships) | B |
| Appointment binds client × service × practitioner × time | ✔ | ✔ | ✔ | ✔ (create→slots→reserve→confirm) | B |
| Practitioner schedules + availability; rooms/resources as booking constraints | ◐ (practitioner eligibility; rooms not observed) | ✔ (rooms/resources on calendar) | ✔ (resource calendars, sibling Tier-1) | ✔ (therapist schedules, room blockouts) | B |
| Appointment lifecycle through delivery; cancel/no-show as named outcomes | ✔ (reminders, No-Show Guard, waitlist, policies) | ✔ (SMS confirm, waitlist, conflict alerts) | ✔ (full status set, sibling Tier-1) | ✔ (reserve→confirm→invoice; reschedule) | B |
| Checkout resolving the visit into recorded payment | ✔ (invoicing & payments) | ✔ (invoice at session end, payment link) | ✔ (Tier-1 sibling) | ✔ (invoice → collect payment) | B |
| Client-facing intake forms (health history/consent) | ✔ (auto-emailed; e-signatures) | ✔ (portal forms, e-sign, auto-save to record) | ✔ (mandatory; login; expiration) | ✔ (guest forms w/ signatures/files) | B |
| Practitioner-facing treatment documentation (SOAP-class) | ✔ (headline: SOAP notes, EMR, templates) | ✔ (clinical notes, body charting, AI SOAP) | ✔ (Tier-1: templates, service binding, staff-only rule) | ◐ (not observed in API docs) | B — 3/4 sampled |
| Documentation saved to the client record | ✔ | ✔ | ✔ (Tier-1: saved to customer profile) | ✔ (guest notes/forms on guest) | B |
| Prepaid packages/series redeemable as visits | ✔ (treatment packages) | ◐ (not observed on massage page) | ✔ (packages/memberships, sibling Tier-1) | ✔ (series packages buy/redeem) | B |
| Insurance/health-fund claiming | ✔ (TELUS Health eClaims — Canada) | ✔ (Medicare/DVA/NDIS, US insurance) | — (not observed) | — (not observed) | B — regional, 2/4 |
| Self-booking page/portal | ✔ (website/social/embed; eligibility rules) | ✔ (branded portal, pay at booking) | ✔ (booking site, sibling Tier-1) | ◐ (online guest creation) | B |
| Reminders/confirmations | ✔ (SMS/email) | ✔ (up to 3; SMS confirm) | ✔ (sibling Tier-1) | ◐ (notifications) | B |
| Waitlist | ✔ | ✔ | ◐ (sibling) | — (not observed) | B |
| No-show protection (card on file / fees / blocklist) | ✔ (No-Show Guard; block problematic clients; pay-in-advance) | ◐ (pay at booking) | ✔ (fees, card on file, sibling Tier-1) | ◐ (saved cards) | B |
| Marketing/retention loops | ✔ (feedback, reviews, referrals, wellness check-ins, newsletters, birthday) | ◐ (recall automation, Mailchimp) | ✔ (marketing suite, sibling Tier-1) | ✔ (opportunities, loyalty) | B |
| Health-data privacy posture | ✔ (HIPAA per FAQ) | ✔ (HIPAA, ISO 27001, GDPR) | ✔ (HIPAA badge; HIPAA-tagged form elements; per-employee access blocks) | ◐ (not observed) | B |
| Multi-location | ◐ (clinic page) | ✔ (multi-location, group practices) | ✔ (sibling Tier-1) | ✔ (org→centers) | B |
| Mobile/outcall (at-client-location) service | ◐ (house-calls testimonial; on-the-move section) | ◐ (home-based testimonials) | ✔ (mobile services, sibling Tier-1) | — (not observed) | B — thin |
| Retail product sales | — (not observed) | — (not observed) | ✔ (retail inventory, sibling Tier-1) | ✔ (product sale flow) | B — suite pole |
| Payroll / commissions | — | — | ✔ (payroll, sibling Tier-1) | ✔ (employee payroll info) | B — suite pole |
| AI documentation | — (not observed) | ✔ (AI SOAP notes / BizzyAI) | — (not observed) | — (not observed) | product-specific |
| Telehealth | — | ✔ (Zoom) | ◐ (Live Stream category) | — | product-specific |
| Therapist-gender preference at booking | — | — | — | ✔ (Tier-1) | product-specific |

Legend: ✔ directly observed for that product; ◐ observed indirectly/partially; — not observed in fetched sources.

## Canonical Model

### Level 0 — Defining Invariant

Smallest structure without which the product stops being recognizable as massage practice management:

1. **Bookable bodywork service catalog** — the practice's service menu (massage modalities/treatments), each with its own duration and price.
2. **Identified client records** — persistent, individually identified clientele (the practice remembers the person, their history, and their documentation, not just transactions).
3. **The appointment as central binding object** — an appointment binds a client, a service, and the practitioner who performs it, into a time slot; practitioner availability (and commonly a room/table) makes the slot bookable.
4. **Lifecycle to service delivery** — the appointment moves from booked (optionally confirmed) through arrival and service performance to completion, with cancellation and no-show as named alternative outcomes.
5. **Checkout resolving the visit into recorded money** — the completed service becomes a chargeable visit recorded against the client (direct payment, redeemed package visit, or claimed/insured service).

Justification tests:

- Remove catalog + appointment binding → generic scheduling application.
- Remove checkout + client ledger → an appointment scheduler remains.
- Remove the appointment/calendar → a POS or invoicing tool remains.
- Remove treatment documentation → still massage practice management (the generic-suite pole — Vagaro, Zenoti — carries the full appointment economy with documentation as an activatable/optional area; Zenoti's documentation surface is not even visible in its Tier-1 API). Documentation is therefore characteristic but NOT definitional.
- Historical check: paper-era massage practice — appointment book with per-therapist columns + client cards carrying health-history intake and per-visit treatment notes + punch-card series + cash at the desk — satisfies all five legs at analog level. A solo therapist running phone-only booking satisfies all five. The definition does not overfit the current cloud/AI generation.

Joint-review resolution (owed to the appointment-based pass): every Level-0 element is identical to the generic appointment-business core. Massage differences concentrate in emphasis and overlay, not in new object types. Verdict: **massage-industry Variant of Appointment-based Service Business Management, keep-both** (barbershop-management precedent); recorded in STATUS.md.

### Level 1 — Common Mature Structure

Present across the researched sample (evidence layer B), expected of mature products but not defining:

- Client self-booking (public page/portal/embed; sometimes with eligibility rules and prepayment).
- Automated confirmations and reminders (SMS/email; some products let confirmations write back to the calendar).
- Waitlist machinery to fill cancellations.
- No-show protection: card on file, deposits/prepayment at booking, cancellation/no-show fees, blocking problematic clients from online booking.
- Client communication (two-way messaging, follow-ups) and retention loops (feedback/review requests, rebooking, newsletters, birthday/referral nudges).
- Prepaid packages/gift certificates as revenue machinery.
- Reporting: revenue, appointments, practitioner utilization.
- Multi-location support; group/multi-practitioner practices with role separation.
- Health-data privacy posture: HIPAA-style compliance claims, per-employee access control over forms/notes.

### Level 2 — Variant / Optional Structure

Depends on packaging philosophy, region, and business model:

- **Packaging poles** — (a) massage-native clinic product (charting-first: ClinicSense); (b) allied-health practice management with a massage vertical (EHR-flavored: Zanda — clinical notes, body charting, claiming, telehealth); (c) generic appointment-business suite serving massage (Vagaro — documentation as an activatable feature area); (d) enterprise spa platform (Zenoti — rooms, series packages, memberships, upsell opportunities).
- **Clinical-documentation depth** — from simple per-visit notes to template libraries, body charts, scored outcome forms, progress reports, AI-assisted note drafting.
- **Insurance/health-fund claiming** — regional: Canadian eClaims integration, Australian Medicare/DVA/NDIS, US insurance billing; absent (unobserved) in the suite pole.
- **Mobile/outcall massage** — the same visit structure performed at the client's location.
- **Marketplace posture** — some suites bundle a consumer discovery app (Vagaro); clinical-pole products are booking-page-only.
- **AI documentation** — AI-drafted SOAP notes (observed in one product; emerging pattern).
- **Telehealth** — present in the clinical pole as platform capability (marginal for hands-on bodywork).
- **Retail/payroll depth** — suite-pole capabilities (product sales, commissions/payroll) often absent in the clinical pole.

### Level 3 — Vendor-specific (research notes only)

- ClinicSense: No-Show Guard® (branded); TELUS Health eClaims; wellness check-ins; weekly availability summaries; "originally built for solo massage therapists"; association partnerships (AMTA/ABMP/RMT bodies); one-click SOAP charting; free booking page without a website; 14-day trial framing.
- Zanda: BizzyAI (AI assistant; AI SOAP notes "turning conversations and observations into structured documentation"); Practice Operations Manual; Physitrack integration; scored forms generating progress reports; body charting; ISO 27001 certification; "up to three reminders per appointment"; invoices auto-created "the moment a session ends"; ex-Power Diary identity.
- Vagaro: five prebuilt SOAP templates; SOAP import (paper-era migration path); "Always Require" re-prompt semantics; "Form Required" calendar icon; SOAP notes staff-only / cannot be required at online booking (Tier-1 verbatim rule); Take Photo (HIPAA) form element; per-employee allow/block access to Forms & SOAP Notes; PayPro front-desk hardware; E-Prescribe category (suite breadth beyond this Type); status color scheme; IOUs at checkout.
- Zenoti: therapist-gender preference; price scaling per therapist; couple bookings; day packages vs series packages distinction; membership freeze/unfreeze with pending-collection accrual; host-guest group bookings via relationships; merge history across centers; opportunities with sales-stage rules; Aveda birthday-gift integration endpoints.

## Rejected Findings

- **"The clinical-documentation layer is part of the defining core"** — rejected: the generic-suite and enterprise poles carry the full appointment economy with documentation optional/not-observed (Vagaro activates it as a feature; Zenoti's API surface shows none), and a massage practice on such a system is still fully served. Documentation is the Type's most characteristic overlay, not its invariant. (Cf. the medspa/clinical overlays classified as L2 in the appointment-based pass.)
- **"Massage practice management requires insurance claiming"** — rejected: claiming is regional (Canada/AU/NZ/US-adjacent) and absent in 2/4 sampled products; the analog practice ran on cash.
- **"Packages are definitional"** — rejected: packages/series are strong in 3/4 products but the visit economy stands without them (pay-per-visit pole exists; analog punch-cards are the paper form of a Common structure, not a precondition).
- **"Massage practice management is a distinct object model from generic appointment-business software"** — rejected after comparison: all defining elements are shared; differences are overlay/emphasis (documentation depth, packages, claiming, privacy posture) — mirrors the barbershop joint-review outcome.
- **"Marketplace discovery is part of the Type"** — rejected: consumer-side discovery belongs to marketplace Types; only one sampled product bundles it, as optional posture.

## Boundary Findings

1. **vs Appointment-based Service Business Management (generic Type)** — defining core identical (catalog + clients + appointment binding + lifecycle + checkout). Massage Practice Management is the massage/bodywork-industry variant: same core with characteristic emphases (health-intake + treatment documentation, packages/series economics, regional claiming, wellness privacy posture, mobile/outcall mode). Joint-review conclusion: **probable industry Variant, not an independent Type; keep-both** per the barbershop precedent. This document still describes the Type as it manifests in massage, with the variant relationship stated in Related Application Types.
2. **vs Spa Management System / Med Spa Management (§29 siblings, unprocessed)** — same generic core; the spa overlay (per the appointment-based pass's spa evidence) emphasizes multi-service itineraries, rooms/equipment, retail; the med-spa overlay adds clinical/medical-supervision machinery; the massage overlay emphasizes health intake + treatment notes + packages. Removal tests change only overlays. Flagged for their own passes.
3. **vs Salon Management System / Nail Salon Management (§29 siblings)** — same core; different service semantics (color formulas/processing vs nail services vs bodywork); massage overlay is the clinical-documentation emphasis. Removal tests change only overlays.
4. **vs Practice Management System (§22) / allied-health EHR territory** — the clinical-pole products (Zanda explicitly "practice management software"; ClinicSense "EMR" vocabulary) sit ON the seam. Test: remove the appointment-to-checkout visit economy → §22-style clinical record system remains; remove the documentation layer → this Type remains intact. The visit economy (bookable catalog + payment per visit) stays central in all four sampled products, so the leaf does not merge with §22. This ratifies the appointment-based pass's note that "health-adjacent booking stays a variant and does not merge this Type with Patient Scheduling / Practice Management (§22)". Residual seam recorded for the §22 pass's side.
5. **vs Patient Scheduling (§22)** — shares booking machinery; Patient Scheduling lacks the service-catalog commerce and checkout-as-revenue structure (no evidence needed beyond the appointment-based pass's structural argument; consistent).
6. **vs Appointment Scheduling Application (03.09)** — remove the client ledger and checkout → scheduling application. Holds for all four sampled products.
7. **vs Retail POS (05.10)** — payment spine shared; remove the booking/calendar and service-delivery context → POS. Retail sales appear only in the suite pole.
8. **vs Beauty Service Marketplace / Service Marketplace (05.02/§29)** — marketplace is consumer-side discovery across providers; this Type manages one practice (or one therapist's book). Marketplace posture is an optional variant here (Vagaro consumer app). On-demand massage marketplaces (Blys/Soothe-class) belong to the marketplace side.
9. **vs Beauty Professional Business App (§29)** — the individual-professional packaging (own book/brand/income) is adjacent packaging over the same core; the massage-native solo products (ClinicSense "built for solo massage therapists") blur toward it, but the sampled massage-native product remains practice/account-oriented rather than personal-brand-economics-oriented. Boundary held at packaging level; left to that leaf's own pass.

## Uncertainties

- MassageBook unreachable (403 ×2): the strongest-known massage-native brand is unevidenced; the massage-native pole rests on one product (ClinicSense, Tier 2). Claims about massage-native patterns are written at structure level with reduced strength.
- ClinicSense help center unreachable (timeout): operational details (template mechanics, package redemption rules, claiming flow) unverified; no precise limits asserted.
- Zenoti documentation/charting surface not visible in the Tier-1 API docs — whether the enterprise pole ships SOAP-class charting is unknown; written as an uncertainty, not a negative claim.
- Tips at checkout: observed only in the suite pole's Tier-1 sibling evidence (Vagaro); whether tipping is a standard massage-checkout component could not be verified from this sample; not asserted in the final document.
- Group/family booking (Zenoti relationships) and couple bookings are spa-pole features; their prevalence in massage-specific products is unverified.
- Claiming mechanics (which services qualify, per-region rules) documented only as named integrations; no workflow claims made.

## Final Synthesis

Massage Practice Management is best understood as **the massage/bodywork-industry expression of appointment-based service business management**: a practice operating system organized around the treatment visit. Its world contains a bookable bodywork service catalog (modalities with durations and prices), an identified client population, and the appointment as the central binding object — client × service × practitioner × time, commonly double-constrained by a room/table. The appointment carries a lifecycle from booking through confirmation and arrival to service completion (or cancellation/no-show under policy), and terminates in checkout — a payment recorded against the client, whether paid directly, redeemed from a prepaid package, or routed through health-fund claiming. What gives the massage variant its shape is the clinical-documentation overlay and the wellness-practice economics around the visit: client-facing health-intake and consent forms collected before treatment; practitioner-facing treatment documentation (SOAP-class notes, in the clinical pole with body charting and outcome tracking) saved to the client record and optionally enforced per service; prepaid series/packages as the dominant retention structure; a health-data privacy posture (HIPAA-class claims, per-employee access control); and, regionally, insurance claiming. The market realizes one Type in four packaging poles — massage-native clinic product, allied-health practice management with a massage vertical, generic appointment suite, enterprise spa platform — and the defining core itself is shared with the generic appointment-business Type: this leaf is its massage variant, as the prior joint-review flag predicted and the barbershop precedent resolved.
