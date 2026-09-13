# Research Notes — Venue Management System

Research date: 2026-09-09

## Research Goal

Understand what a Venue Management System (VMS) really is as an Application Type: what objects exist inside it, who operates it, how bookings move through it, and where it sits against the heavily pre-flagged sibling Types in §26 (Event Management Platform, Event Registration, Event Ticketing, Convention/Exhibition, Banquet Management, Catering Management, Festival Management, Attraction Management) plus §17/§28 space/facility siblings.

This leaf arrives with more pre-hung boundary flags than almost any other §26 leaf:

- **banquet-management** (2026-09-09): "venue management = space inventory for any use, without the F&B/BEO layer; flagged for joint review when Catering Management and Venue Management System are processed"
- **catering-management** (2026-09-09): "flagged for the venue-management-system pass: remove the F&B/production layer from catering → VMS"
- **theater-production-management** (2026-09-09): "vs venue-management (spaces as schedulable resources bound to calls vs bookable sellable inventory)"
- **sports-facility-management** (2026-09-09): "event/venue-management §26 (parties as productized bookings vs event-centered)"
- **reserved-seating-platform** (2026-09-09): "venue-management (spaces vs selling asset)"
- **convention-exhibition-management** (2026-09-07): "vs Venue Management System (operator + object differ)"
- **event-management-platform** (2026-09-07): "vs Venue Management System (venue-side vs organizer-side)"
- **festival-management** (2026-09-07): "vs Attraction Management (venue-side vs organizer-side)"
- **hotel-property-management-system-pms** (2026-09-08): function-space/activity booking recorded as a property-type variant inside PMS

## Initial Boundary Hypothesis

Before research: a VMS is the **venue-side** system of record — the operator of physical function spaces (convention centers, arenas, stadiums, theatres, conference centres, function rooms, banquet halls) manages those spaces as **bookable inventory** and works **bookings** (occasions committed to spaces × times) through a sales/operations lifecycle. Nearest confusions: Event Management Platform (organizer side), Banquet/Sales & Catering (function-execution layer), resource scheduling systems (generic rooms, no event semantics), hotel PMS (accommodation center).

## Research Questions

1. What is the unit of record — the event, the booking, the space, or something else? How do products decompose an occasion into space-time usages?
2. What is the booking lifecycle (statuses) and who drives it?
3. Is money (quotes/contracts/invoicing) definitional or common? Is there a no-money pole?
4. What does the "diary"/calendar surface actually show, and what conflict machinery exists (spaces only, or resources/people too)?
5. Where is the exact seam vs Event Management Platform (organizer side) and vs Banquet/Catering (F&B layer)?
6. Where is the seam vs generic room/space scheduling (workplace/university booking tools)?
7. Does the hotel pole (function space + room blocks) belong inside this Type or is it Hotel PMS territory?
8. Historical check: does a paper-era function diary satisfy the definition?

## Representative Products

| Product | Pole | Customer tier | Reach |
|---|---|---|---|
| **iVvy** (Event & Venue Management Software) | sales & catering-led, multi-property, marketplace | hotels, hospitality groups, function centres, stadiums | knowledge.ivvy.com/kb (Tier 1) + product pages (Tier 2) |
| **Mazévo** | institutional room & event scheduling (requests/approvals/academic) | universities, churches, K-12, government, hospitals, libraries, athletic facilities | gomazevo.com/help KB (Tier 1) + product pages (Tier 2) |
| **EventPro** | modular all-in-one (venue booking + event management + catering as separate solution lines), cloud/on-prem | venues, convention centres, arenas, arts centres (testimonials), caterers | eventpro.net product pages (Tier 2) |
| **Artifax** | arts & culture venue operations (programming + scheduling + finance) | theatres (LW Theatres), galleries (National Portrait Gallery, SFMOMA), cathedrals, councils | artifax.com product/feature pages (Tier 2) + support.artifax.net help centre exists (not fetched) |

Boundary witnesses (not representative samples of this Type): **Skedda** (workplace desk/room booking; fetched — positioned as "Workplace Management Software"; its rentable-space offshoot "AllBooked" covers sports facilities/community spaces/music studios as self-serve booking), **Accruent EMS** (accruent.com/products/ems-software → 404 ×1, abandoned per network rule; EMS exists as market context — Mazévo ships an "EMS Data Migration" service and an "EMS vs Mazévo" comparison page, both visible in fetched navigation). **Momentus Technologies (ex-Ungerboeck)** — the convention-center/arena enterprise leader — unreachable: transport error ×2 (root and /products), abandoned per network rule; no claims made about it.

## Sources

- iVvy — knowledge.ivvy.com/kb (KB index + /kb/venues section, fetched 2026-09-09); www.ivvy.com (home + /venue-event-management-software/, fetched 2026-09-09)
- Mazévo — www.gomazevo.com (home), /product/features, gomazevo.com/help (KB index), /help/managing-events (all fetched 2026-09-09)
- EventPro — www.eventpro.net (home), /venue-management-software.html (both fetched 2026-09-09)
- Artifax — artifax.com (home), /features/scheduling/ (both fetched 2026-09-09)
- Skedda — www.skedda.com (fetched 2026-09-09, boundary witness only)
- Momentus (momentus.tech) — transport error ×2, abandoned
- Accruent EMS — 404 ×1, abandoned

No help-center articles were fetched at article depth for iVvy (only the KB section index), Mazévo (only KB indexes), or Artifax (help centre not attempted). All quotes below are from fetched pages verbatim or near-verbatim.

## Product Observations

### iVvy (Event & Venue Management Software)

Evidence layer: A (direct, KB index + product pages).

- Positioning: "Event & Venue Management Software … Sales & Catering Software that manages every enquiry, booking, proposal, and event from one place. CRM, function diary, branded proposals, e-signature contracts, version-controlled BEOs, automated invoicing, and reporting — built for venue sales teams that need to move fast." (product page)
- Venue model: multi-venue/multi-property — "Limiting a User to certain properties", "Setting up Venue Groups", "Copying an Opportunity to Another Venue", group reports across venues, "Venue Performance Comparison Report". User groups, user policies, booking roles, cost centres per venue.
- Space inventory: **Function Spaces** ("Create/Edit your Function Spaces"), with **Room Hire/Rental Plans** ("Setting the Room Hire/Room Rental Plans for Function Spaces"), categories for function spaces, **Floorplan Module** ("Creating a Floorplan using the Floorplan Module", "Adding a Floorplan to a Quote or Booking"), **Default Setup Requirements**.
- Resources: "Creating a Resource", **Resource Diary** (dedicated diary for resources), adding resources to quotes/bookings.
- Commercial catalog attachable to bookings: Products, **Food Menus / Menu Items / Menu Groups / Menu Types**, **Beverage Packages / Items / Types**, **Event Templates**, discount campaigns, surcharges, commissions for agents/PCOs, payment terms, minimum spend ("Set a Booking Minimum Spend").
- Sales pipeline: **Leads module**, **Opportunities** (create, allocate to team members, opportunity types/market segments, sources, quality, stages + reasons), **Activities + Activity Calendar** (Outlook integration), **Quotes** ("Adding a Quote to an Opportunity", "Converting a Quote (Prospect) to a Booking (Tentative)"), reservations at "**Prospective** and **Prospective Hold**" status, proposal documents with e-signature, PDF or e-contracts.
- Bookings: Simple vs **Detailed Booking**; bookings decompose into **Sessions/Functions** ("Adding a Session / Function to a Booking or Quote", "Bulk Session / Function Editors", "Session / Function Status"); status changes ("Changing the status of a booking", "Editing the Status of Multiple Quotes / Bookings"); **BEO** (Banquet Event Order) packet, finalising BEO + **BEO Changelog**; **Virtual Run Sheet** ("Using the Venue Virtual Run Sheet" — live view on tablet/phone, adjusts as details change); Setup Requirements; Booking Notes, Default Booking Notes; Booking Changelog; Copying/moving bookings; **Recurring Bookings**; Cancelling; **Case and Issue Management** ("When something goes wrong on event day … log it immediately"); surveys linked to bookings.
- Accommodation pole (hotel): "Turning on Accommodation for your Venue", Accommodation Rooms, Rate Plans, Room Categories, Release Schedules, Blackout Dates, **Group Room Reservations**, **Rooming Lists** import, Group Reservation Website — i.e., the hotel pole holds sleeping-room blocks alongside function spaces.
- Money: Invoices within bookings, **Billing Automation**, Pay-Now buttons, payment gateways, credit notes, refunds, payment methods, credit-card fees, tax report (GST/VAT/service fees), Profit and Loss on booking summary, cost centres, **Revenue Pace Report**, **Quote & Booking Forecast**, budgets vs actuals.
- Diary: **Function Diary** is a named first-class surface (nav topic "Diary"): "Navigating your Diary", "Calendar View", "**Blocking a Space in the Diary**", "Adding Important Dates to your Diary", "Coordinator Function Diary View", "Changing the Order of your Diary". Product page: "Keep everyone aligned with a single, shared function diary".
- Demand capture: **Booking Engines** (own-site availability display + enquiry/booking intake into CRM: "Booking Buttons and Widgets", "Meeting Booker", RFP forms simple/detailed, "Booking Availability Rules", "Space Allocation Rules", "Opportunity Allocation Rules"), **iVvy Marketplace** listing (add venue to marketplace, FAQs, catering options, event guidelines, COVID-safe options).
- Reporting: space utilisation ("Event Space Utilisation Report"), resource utilisation, covers, production report, sales pipeline/tracking/agent performance, dashboards (Sales and Operations Dashboard, Group Dashboard), report builder, venue-group comparisons.

### Mazévo

Evidence layer: A (direct, KB indexes + features page).

- Positioning: "Modern Room Scheduling & Event Management Platform" for organizations that "need more than simple room booking": "complex events, shared resources, approval workflows, billing, or academic scheduling". Explicitly contrasts itself with "a lightweight calendar with minimal coordination between people, spaces, and services".
- Core objects: **Events** (customer-facing occasion: organization + contacts + event type + description, public/private, VIP flag, event coordinators, attachments) containing **Bookings** (space×time commitments: "How to Change the Room on a Booking", "How to Change the Time of a Booking", "How to Change the Date of a Booking", "How to Move a Booking", "How to Copy a Booking", "How to Cancel a Booking", "How to Change the Status of a Booking", "How to Change the Pricing Plan for an Event", "Why are Bookings Displayed in Italics" — visual state encoding). "Addressing Conflicts When Adding Events on Multiple Dates".
- Conflict machinery is explicit and first-class: "Managing Conflicts — Overview of The Conflict Status"; features page: "Resolve potential conflicts in seconds … instantly see why a room is not available … never overbook".
- Calendar surfaces: **Event Book** (day view of bookings by room, sortable), **Event Calendar**, **Day At A Glance**, Find Events (saved views, email a view), **Activity Log**, data history ("How to View the History of Any Data in the System").
- Intake: **Facility Request Forms** (customer submits request against real-time availability; fully configurable; collects resources/service needs), **Requests processing** (find requests, approve/deny, request additional information, incomplete requests, resolve inventory issues), **Approval Workflows** (rules-based routing, secondary approvals, approval states) — the institutional intake pole instead of a sales pipeline.
- Resources: resource inventory management with **inventory checking** ("What Triggers Inventory Checking in the Event Editor", "Managing Inventory Issues as an Event Planner") — "Get alerted if you don't have enough required resources".
- Room setups: "How to Use Room Setups", "How to Attach a Room Diagram to a Booking".
- Documents: **Confirmations** (send, suppress pricing, limit service providers), **Banquet Event Order** ("How to Create a Banquet Event Order") — BEO present even at the institutional pole.
- Money: **Billing & Invoicing** (quotes → detailed invoices → payments/deposits tracking; automated room and resource pricing from the pricing schedule; corrected invoices; reconciliation with finance office; taxes).
- Operations: **Mobile Ops App** ("Give your operations team a clear, mobile view of what needs to be done, and track progress in real time as events are set up"; replace paper event reports; staff check off tasks), **Operations Daily Logs**, tasks and reminders, notifications/scheduled emails/messaging channels.
- Academic scheduling: separate module — SIS integration (Ellucian Banner/Colleague/PowerCampus, PeopleSoft, Anthology, Jenzabar, Workday), "Optimize thousands of course sections in minutes", bidirectional integration, back-to-back instructor rooms. This is the university room-scheduling extension of the same machinery.
- Public calendar: master calendar for the organization, single or multiple calendars per location/topic, images/registration links.
- Integrations: room signs/display boards, door access control, HVAC based on occupancy, payment systems, student engagement platforms, Google/Outlook calendar.
- Industries: colleges & universities, churches & temples, K-12, government agencies, hospitals, libraries, athletic facilities (community/nonprofit).

### EventPro

Evidence layer: A/B (direct product pages, Tier 2).

- Positioning: "comprehensive and versatile solution built from seamlessly integrated modules for **venue booking, event planning, catering management**, and so much more. Choose the event, venue, and catering components you need." — the vendor itself splits three solution lines: **Venue Management** ("manage rooms, resources, people, and places", "venue booking management system"), **Event Management** (end-to-end event lifecycle for event professionals), **Catering Management**.
- Venue model: "manage the booking process from the first enquiry (even online enquiries) to emailing the final thank you letter, and everything in between. A venue booking calendar, complete booking management including setup resources, catering, beverage, and staffing requirements, budgeting, invoicing".
- **Booking Wizard** ("Wizards guide you through the steps of entering a booking, account, contact & other key functionality"); **Shared Booking Calendar** ("manage all of your bookable spaces in a simple but advanced featured calendar"); "Easy-View Event Booking Calendar — graphic, color-coded … determine at a glance what your real and potential commitments are … **the conflict check prevents double bookings**".
- Spaces: "You customize the Booking Calendar to your event spaces, whether they include **physical rooms, or outdoor spaces, any type of bookable space** is easily managed."
- No double bookings named as a headline feature ("No double bookings" in the feature list).
- Modules: Catering Management, Beverage Management, **Resource Management** ("Track audio/visual, chairs, tables, decorations, signs, linens, tableware, and more"), **Staffing Management** (assign staffing requirements to bookings), Package Management (pre-defined resource bundles), Integrated CRM, Sales Management (leads & opportunities → convert into clients with bookings), Communications Logs, **Itinerary Scheduler** (drag-and-drop event organization for event locations, functions, resources and attendee assignments), Attendee Management, Booth/Exhibitor Management, Travel & Accommodations, **Floor Plans** ("Create elegant, precise floor plans no matter the event type"), Invoicing & Payments (auto-create invoices from booking info, batch invoicing), Integrated Budgets, Task Management, Reporting, User Security, Dashboards/KPIs.
- Online layer: EPConnect — **Online Booking Calendar** (view location booking calendar online, multiple definable views), **Online Space Booking** (users create/edit bookings online via New Booking Wizard), **Online Booking Enquiries** (web enquiries "automatically pulled for easy processing"), online invoicing/payments, event webpages, online event registrations.
- Deployment: cloud or on-premise ("All EventPro applications will have the same functionality").
- Testimonials: Sunshine Convention Centre (Victoria University), Wells Fargo Centers, Riverway Arts Centre — venue-side operators.

### Artifax

Evidence layer: A/B (direct product/feature pages, Tier 2).

- Positioning: "Venue and event management software purpose-built for arts and culture. Plan, schedule, and coordinate events across your whole organization — all in one place." FAQ: "we help you manage bookings, people, spaces, and resources in one secure platform".
- Feature areas: **Scheduling**, **Artistic Programming** ("from rehearsals to guest scheduling"), **Event Management** ("plan, coordinate, and deliver performances"), **CRM** ("Convert leads into sales"), **Finances** ("From quotes to invoicing"), **Reporting**.
- Scheduling model: "One calendar with every event under control … keeps teams aligned, prevents costly clashes": **Graphical Calendar View** (drag-and-drop, spot "clashes, gaps, and pressure points"), List/Year/Availability views, **Real-Time Conflict Checking** ("automatic conflict checks flag issues early … teams avoid double-booking **spaces, equipment, or people**"), **Multiple Locations & Spaces** ("multiple venues, rooms, and resources in one view"), filtering/search by date/space/client/event type, **Templates & Patterns** for repeated events, integrated updates ("Every change is shared instantly across departments … the calendar as the single source of truth").
- Money: quotes → invoicing (Finances feature; testimonial: "the time that it takes me to generate **contracts and invoices** for clients has been cut in half").
- Integrations: finance systems (Sage, SAP, Xero, Advanced Exchequer), **ticketing platforms (Spektrix, Tessitura, VivaTicket)**, Outlook/Google calendars, Mailchimp, Stripe, DocuSign, StaffSavvy (staffing).
- Scale/lineage: "11m Events Managed", "13.2k Users", "756 Published Calendars"; blog: "In 1986, arts and cultural organizations managed events with paper diaries, manual updates and siloed records" (40-year company history) — direct vendor acknowledgment of the paper-diary baseline.
- Community intake: Contact Widget module — "Turn website enquiries into structured sales opportunities".
- Departments nav (unfetched detail): scheduling/operations/programming/finance/customer-service roles across the venue.

### Skedda (boundary witness, not a representative product)

Evidence layer: A (direct).

- "Workplace Management Software": "Give your team self-serve booking for desks, rooms, and resources. Automated rules keep it fair". Core = desks/meeting rooms/parking/labs for an internal population (workplace, universities, coworking).
- Structure: self-serve booking + automated rules (approvals, quotas, priority windows, check-in), interactive floor plans, neighborhoods, visitor management, occupancy insights, utilization analytics, SSO/SCIM, two-way calendar sync.
- Its rentable-space arm "AllBooked by Skedda" (separate product/domain) covers sports facilities, community spaces, music studios — self-serve booking with payments/memberships.
- No occasion-shaped booking records, no sales pipeline, no quotes/contracts/BEOs, no venue-operations documents anywhere in fetched material. This is the structural shape of "space booking" WITHOUT the venue-management operation — the cleanest observed lower bound for the Type.

## Cross-product Comparison

| Structure | iVvy | Mazévo | EventPro | Artifax | Evidence |
|---|---|---|---|---|---|
| Bookable spaces as persistent configured inventory (function spaces/rooms, capacity, categories) | Function Spaces + room hire plans + floorplans | Facilities/rooms + room setups + diagrams | Bookable spaces (rooms or outdoor), booking calendar per space | "multiple venues, rooms, and resources" | B (4/4) |
| Booking = occasion bound to space(s) × time, persistent, editable (move/copy/cancel) | Booking + Sessions/Functions | Event + Bookings | Booking (+ functions via Itinerary) | Events on calendar | B (4/4) |
| Central calendar/diary of the venue's commitments | Function Diary (+ Resource Diary) | Event Book / Event Calendar / Day At A Glance | Shared Booking Calendar (color-coded) | Graphical Calendar (single source of truth) | B (4/4) |
| Conflict / double-booking prevention | space blocking in diary; availability rules | Conflict status; "never double-book" | "conflict check prevents double bookings"; "No double bookings" | real-time conflict checks (spaces, equipment, people) | B (4/4) |
| Customer records (CRM / organizations & contacts) | CRM, accounts, contacts, companies | Organizations and Contacts | Integrated CRM | CRM | B (4/4) |
| Intake → commitment pipeline | Leads → Opportunities → Quotes → Bookings (Prospective/Prospective Hold/Tentative/Confirmed) | Requests → approvals → Events/Bookings | Enquiries (incl. online) → Bookings via wizard | Leads (contact widget) → bookings; contracts | B (4/4, two different intake postures) |
| Money on the booking: pricing, quotes, deposits, invoices | Room hire plans, minimum spend, payment terms, invoices, billing automation, credit notes | Pricing plans, quotes, invoices, payments/deposits | Auto-invoices from bookings, budgets, batch invoicing | Quotes → contracts → invoices | B (4/4) |
| Operational documents generated from bookings | Proposals, e-contracts, BEO + changelog, Virtual Run Sheet | Confirmations, BEO, setup reports, scheduled emails | Booking reports, task reminders, communications | Contracts, invoices, published calendars | B (4/4) |
| Resources/equipment with availability attention | Resources + Resource Diary | Resource inventory checking | Resource Management (AV, chairs, linens…) | conflicts include equipment & people | B (4/4) |
| Setup/room-layout machinery | Setup Requirements, Floorplan Module, default setups | Room Setups, Room Diagrams | Floor Plans, room setup | (not directly evidenced in fetched pages) | B (3/4) |
| Catering/menus attachable | Menus, beverage packages (S&C-shaped) | catering as service need; BEO | Catering Management module | (not evidenced) | B (3/4) — seam surface with Catering/Banquet |
| Utilization/production reporting | Space/resource utilisation, pace, production | events-per-room analytics | forecasting, utilization benefits ("Increase utilization") | reporting + published calendars | B (4/4) |
| Public/self-serve demand capture | Booking engine, widgets, Meeting Booker, Marketplace | Request forms, public calendar | EPConnect online booking/enquiries | Contact widget | B (4/4) |
| Multi-venue / multi-property | Venue groups, properties | campus/department scope | Locations | Multiple locations & spaces | B (4/4) |
| Accommodation rooms/room blocks | Yes (hotel pole) | No | Travel & Accommodations module | No | single-pole → variant |
| Academic/course scheduling | No | Yes (module) | No | No | single-pole → variant |
| Staffing assignment | No direct evidence | ops staff tasking | Staffing Management module | conflicts include people | partial → optional |
| AI agents | iVvyAI | No | Virtual Assistants (workflow automation) | No | era-current, optional |

**Naming variance:** the occasion container is called Booking (iVvy), Event (Mazévo), Booking/Event (EventPro), Event (Artifax); the space-time usage is Session/Function (iVvy), Booking (Mazévo), Function (EventPro itinerary). "Venue" itself is multi-property in iVvy (a venue group has properties) and single-property elsewhere. The recurring abstract pair is: **occasion** and **space-time commitment(s)**.

**Money question:** all four products carry quotes/invoices/deposits. But Mazévo's pole (universities, libraries, churches) bills community use and internal cost recovery, and its intake is requests+approvals, not a sales pipeline. Conclusion: money machinery = common mature structure; a sales/CRM pipeline = common in commercial venues, replaced by request/approval intake in institutional venues; neither is definitional. What IS constant: bookings are worked as a managed portfolio (status lifecycle, holds, confirmations, changes) — that is the operational center everywhere.

**Conflict machinery:** universal, and in two products explicitly broader than rooms (Artifax: spaces+equipment+people; Mazévo: resource inventory checks). The diary + conflict check is the operational heart of the Type.

## Canonical Model (L0 — defining invariant)

Three jointly-held structures:

1. **The venue's bookable spaces as inventory of record** — persistent, individually identified spaces (rooms, halls, arenas, function rooms, outdoor areas) configured with bookable time, grouped under one venue operator (multi-property in mature products); availability over time is the property the whole system guards. Remove → a CRM/pipeline or an event tool with no venue substrate.
2. **The booking as the space-committing unit of record** — a persistent record binding an occasion (customer/organization + event type + date/time) to one or more specific spaces over specific time, decomposable into per-space/per-time usages (sessions/functions/bookings), editable (move/copy/cancel/re-book) rather than one-shot. Remove → a diary entry list or generic event/calendar management.
3. **The venue-side managed booking operation on a shared calendar** — bookings held as a portfolio and worked through a status lifecycle (intake/inquiry → hold/tentative → confirmed → executed → closed/settled) on a central venue calendar/diary with conflict/double-booking prevention across spaces (commonly resources too), plus the coordination outputs the operation needs (confirmations, function sheets, run sheets, tasks). Remove → a static space list, or a pure self-serve booking widget.

Jointly-held load-bearing tests:

- 1 alone = room/floor-plan inventory list (Facility Management / Space Management territory)
- 2 alone = appointment book / calendar entry
- 3 without 1+2 = generic calendar/scheduling app
- 1+2 without 3 = spaces with bookings but no managed operation (self-serve booking tool — Skedda-class)
- 1+3 without 2 = availability calendar over rooms with no occasion records
- 2+3 without 1 = organizer-side event management / generic occasion tracking

## L1 — Common Mature Structure (not definitional)

- CRM/organization+contact records with booking history
- Sales pipeline (leads/opportunities → quotes → contracts with e-signature) at commercial poles; request forms + approval workflows at institutional poles (same slot, different posture)
- Money on the booking: pricing plans/room hire rates, deposits, payment terms, invoicing, credit notes, payment collection, budgets vs actuals
- Operational document generation: proposals/contracts/confirmations, BEOs/function sheets, run sheets, setup reports, staff notifications
- Resource/equipment inventory with availability checking (sometimes staffing)
- Room setup machinery: setup types/styles, capacity charts, floor plans/diagrams attachable to bookings
- Catering/menus/beverage attachable to bookings (strongest at the hotel/function-centre pole)
- Utilization/production/revenue reporting, dashboards, pace reports
- Public calendars, website booking engines/enquiry widgets, marketplace distribution
- Tasks, notes, activity logs, changelogs/audit trails
- Multi-venue/multi-property administration, role/permission systems

## L2 — Variant / Optional Structure

- Accommodation rooms & group room blocks (hotel pole; integrates toward PMS rather than replacing it)
- Academic/course scheduling with SIS integration (university pole)
- Intake posture: sales-led (CRM pipeline) vs request/approval-led (institutional) vs operations-led (arts programming)
- Marketplace listing/distribution of the venue's spaces
- Ticketing module (sold as a separate product line by the same vendor — organizer-side Type)
- Exhibitor/booth management (event-suite extension)
- On-premise vs cloud deployment; module/suite packaging; AI agents
- Industry seasoning: convention centres, arenas/stadiums, theatres/arts centres, function centres, universities, churches, government/community venues
- Visitor/occupancy integrations, door access, HVAC/signage integration (institutional)

## L3 — Vendor-specific (research notes only)

- iVvy: "Session/Function" decomposition, Prospective/Prospective Hold/Tentative/Confirmed status vocabulary, Opportunity Types/Market Segments/Quality, iVvyAI agents, iVvyPay, Venue Virtual Run Sheet, Banquet Check, cost centres, "3× faster RFP response" marketing claims.
- Mazévo: Event Book / Day At A Glance / Find Events surfaces, Conflict Status article, secondary approvals, Mobile Ops App, EMS Data Migration service (evidence of the Accruent EMS predecessor market), named SIS integrations.
- EventPro: EPConnect module family, Booking Wizard, Virtual Assistants, desktop+cloud parity, "since 1985" parent (PSI).
- Artifax: "Deal Types Configured 213", 11m-events scale stat, 1986 lineage narrative, Contact Widget, named integrations (Tessitura/Spektrix/Sage/SAP/DocuSign/StaffSavvy).
- Accruent EMS: exists as the institutional-EMS incumbent (evidence: Mazévo's migration service and comparison page); content not fetched, no claims.

## Boundary Findings

1. **vs Event Management Platform** (processed; pre-hung flag "venue-side vs organizer-side") — **RATIFIED from this side.** The EMP centers the event as a managed record with a registration surface and attendee lifecycle (that pass's L0: event record + registration surface + attendance lifecycle). The VMS centers the venue's spaces and the venue's booking portfolio; the occasion matters as a commitment against space and venue operations. Vendor-side corroboration: EventPro sells "Venue Management" and "Event Management" as two different solution lines with different centers (venue booking calendar/enquiries vs event lifecycle/attendees/exhibitors). Remove-test holds both directions: remove spaces → EMP; remove attendee/registration lifecycle → VMS survives (Mazévo/Artifax carry no registration machinery in their venue cores).
2. **vs Banquet Management** (processed; pending joint-review flag) — **DISCHARGED, keep-both ratified.** The banquet pass's discriminator ("banquet = booked function in the venue's own function spaces: diary + BEO + on-premise execution; venue management = space inventory for any use, without the F&B/BEO layer") holds under this pass's evidence, refined: the seam is the **scope of the bookable inventory and the center of the record** — banquet management centers the booked function's F&B/service execution; VMS centers the venue's whole space portfolio across all uses (concerts, exhibitions, meetings, weddings, classes, rentals) where F&B is one attachable line, not the spine. BEO presence is NOT a discriminator (iVvy and Mazévo both generate BEOs while remaining VMS products; the banquet pass itself predicted "venue management = space inventory … without the F&B/BEO layer" — refined to "not the center"). Product-market overlap zone acknowledged: hotel "sales & catering" departments buy VMS products (iVvy positions itself as both); the boundary is center-of-gravity, not exclusive capability.
3. **vs Catering Management** (processed; "remove the F&B/production layer from catering → VMS") — **CONFIRMED from this side.** In sampled VMS products catering appears only as attachable menus/services on bookings (iVvy menus/beverage packages; Mazévo catering service; EventPro catering module). None of the fetched VMS material centers food production/recipe/delivery machinery — that is the catering pass's spine. Remove-test holds.
4. **vs Convention/Exhibition Management** (processed, "operator + object differ") — **RATIFIED.** The exhibition Type's sellable floor is booth-level inventory inside ONE produced show; the venue's inventory is hall/room-level across MANY occasions (a show is one booking from the venue's side). Two different inventory grains and two different operators (show organizer vs venue operator); suites (Cvent-class) straddle by packaging.
5. **vs Ticketing / Reserved Seating** (processed, "spaces vs selling asset") — **RATIFIED.** The venue rents the hall and time; ticketing sells admission/seat entitlements to occasions in it. Direct market evidence: Artifax integrates with Tessitura/Spektrix/VivaTicket (ticketing platforms) rather than replacing them; iVvy sells "Event Ticketing Software" as a separate product line.
6. **vs Hotel PMS** (processed; function-space booking recorded as a PMS variant) — **HELD with refinement.** The hotel pole of VMS (iVvy: function spaces + accommodation room blocks + rooming lists) coexists with PMS: iVvy's headline integrations are Opera Cloud/Mews/StayNTouch (PMS) — the VMS holds the function-space and event side while the PMS holds the operated stay (check-in/folio/housekeeping). The overlap zone is group room blocks; boundary = center of gravity (function/event inventory vs accommodation stay machinery).
7. **vs Sports Facility Management** (§28 processed; "parties as productized bookings vs event-centered") — **RATIFIED with the same center-of-gravity rule.** Sports facility management centers recurring timeslot reservations/memberships/leagues on generic rentable spaces; VMS centers occasion-shaped bookings on the venue's function inventory. Mazévo lists athletic facilities among its markets (community use scheduling) — the families share the space-booking substrate; the occasion/slot orientation is the seam. Community/athletic booking products can sit either side by posture.
8. **vs generic room/space scheduling (no leaf: workplace desk/room booking)** — Skedda-class products carry self-serve space booking + rules + utilization but no occasion-shaped booking records, no sales/contract operation, no venue-operations documents; they self-label "Workplace Management". This material is the observed lower bound BELOW the VMS Type (L0 leg 3 missing). Institutional VMS products (Mazévo) occupy the layer just above it by adding the occasion record, the lifecycle, and the operation. No directory leaf exists for pure workplace space booking in the fetched sample's own terms (§17 Space Management/Workplace Management covers the built-facility side); recorded as observation, no directory change.
9. **vs Amenity Booking Platform** (§17 processed) — closed resident population vs open market bookings; consistent with the sports-facility pass's record. Held.
10. **vs Theater Production Management** (processed, "spaces as schedulable resources bound to calls vs bookable sellable inventory") — **RATIFIED.** The production office schedules its own show's calls; the venue books its spaces out (including to productions). Artifax sits on the venue side even inside theatres (its center is the venue calendar/booking/finance, not the production call schedule).
11. **vs Resource Calendar / Enterprise Resource Scheduling Platform** (§03.08/§10, unprocessed) — generic resource scheduling vs venue semantics (bookings as commercial occasions, revenue, customers). Forward note: those passes should test whether generic resource schedulers without venue/event semantics fall inside or outside; expected keep-separate.
12. **Naming observation:** the market uses "venue management software", "venue booking system", "event management system" (institutional), "sales & catering software" (hotel pole), "room scheduling" — label noise, one structural Type. "VMS" collides with Vendor Management System (§09) — pure name collision, different Types.

## Historical / Market-Sample Check (§24)

- Artifax's own company narrative: in 1986 "arts and cultural organizations managed events with paper diaries, manual updates and siloed records" — the paper function diary + hold/confirm practice + contracts + capacity charts satisfies all three L0 legs with zero modern machinery.
- EventPro's own framing of the pre-software baseline: "If you've already tried paper calendars or spreadsheets … Writing down the room, client, and time is not enough" — i.e., the baseline practice this Type digitizes is the paper venue diary; the product's claimed added value (conflict checks, operations coordination) is L1, not L0.
- University conference offices and community venues (paper booking ledgers) satisfy the institutional pole without sales pipelines or e-signatures.
- No era-, region-, or vendor-specific pattern enters L0: no cloud, no CRM pipeline, no marketplace, no AI, no e-signature, no English-market vocabulary.

## Uncertainties

1. **Momentus (Ungerboeck) unreachable** (transport error ×2) — the largest enterprise venue-management vendor (convention centers, arenas) is undocumented here. The enterprise/convention-center pole rests on Artifax/EventPro/iVvy adjacency. No claims made about Momentus products; assertion strength capped accordingly.
2. **Accruent EMS 404** — institutional-EMS incumbent not directly evidenced; only its market existence (via Mazévo's migration/comparison surfaces).
3. **Help-center article depth** — iVvy/Mazévo KB section indexes were fetched, not individual articles; Artifax help centre not fetched. Status vocabularies beyond what titles show (e.g., exact confirmed→closed state names) are held conceptual.
4. **Exact conflict-check semantics** (what conflicts with what, per product) not article-verified; held at "prevention across spaces, commonly resources/people" strength.
5. **Pricing/packaging** not researched (not needed for the Type's structure).
6. Whether a "booking engine/marketplace" surface (customer self-serve RFP into the pipeline) is definitional or common — held common (Mazévo's institutional pole runs on request forms instead; both are intake realizations of the same slot).

## Final Synthesis

A Venue Management System is the **venue operator's system of record for selling and operating its bookable spaces**: it holds the spaces as configured bookable inventory, records bookings as persistent occasion-to-space-time commitments, works those bookings as a portfolio through a status lifecycle on a shared venue calendar with conflict prevention, and produces the money and operations outputs (quotes/contracts/invoices, confirmations/BEOs/run sheets, tasks, utilization reports) that running a venue requires. It is venue-side (the space-holder's perspective), occasion-shaped (not slot- or membership-shaped), and space-portfolio-scoped (all uses of the venue, not one function family). Its neighbors are distinguished by perspective (EMP: organizer side), operational layer (Banquet: function F&B execution; Catering: food operation), inventory grain (Convention: booths in one show; Ticketing: seats/admissions), or domain center (Hotel PMS: stays; Sports Facility: timeslots/memberships).
