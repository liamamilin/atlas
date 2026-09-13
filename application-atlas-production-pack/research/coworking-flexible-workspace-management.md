# Research Notes — Coworking / Flexible Workspace Management

Research date: 2026-09-07
Methodology: update-v1 WORKFLOW_v1.1 + WRITING_GUIDE_v1.1

## Research Goal

Understand the operator-side software that runs a coworking / flexible workspace business: what its world is made of (spaces, members, plans, bookings, money), how the operational loop works (signup → membership → usage → billing), which capabilities are defining vs merely common in today's market, and where its boundaries lie against workplace/desk-booking software, hotel PMS, property management, and membership systems.

## Initial Boundary (hypothesis before research)

- Core use hypothesis: manage a shared-workspace business — sell flexible access to desks/offices/rooms as memberships, take bookings, check people in, control access, invoice.
- Users hypothesis: space operators (community managers, space managers, multi-site operators) as admin users; members and non-member visitors as end users.
- Nearest neighbors: Workplace Management / Desk Booking (occupant-side), Hotel PMS (transient stays), Membership Management System (no space), Commercial Property Management (leases), Venue Management System (event space booking), Amenity Booking.
- Key discriminator hypothesis: the operator sells recurring, flexible-term access (memberships) over its own space inventory and bills for it. Remove members/billing → occupant-side booking tool; remove space → membership billing software.
- Unknowns: whether plan/contract/membership is one concept or two; whether community features are definitional; whether day-pass/non-member business is core; whether "flexible workspace" extends beyond offices (shared kitchens, warehouses).

## Research Questions

1. What is the core commercial object (plan? contract? membership?) and how do the template vs instance layers relate?
2. How is space structured (location → floor → units)? What is bookable vs assignable?
3. How do members consume space (bookings, credits, passes, assignments, check-ins, door access)?
4. How does billing work (recurring cycles, proration, one-off charges, deposits, taxes, gateways, compliance)?
5. Who are the record types (member, contact, team/company, visitor, lead) and how do they convert?
6. Which community/engagement capabilities are standard (directory, events, messaging)?
7. What are the boundaries vs workplace management, hotel PMS, property management, membership systems?
8. What variants exist (virtual office, day-pass-only, enterprise operators, non-office verticals)?

## Representative Products

Chosen for market representation, documentation quality, different product philosophy, different customer tier:

| Product | Position / philosophy | Customer tier | Evidence tier |
|---|---|---|---|
| Nexudus (est. 2012, 90+ countries) | established all-in-one, API-first, deep billing/CRM/community breadth | single spaces → large networks | A (glossary + full KB index) |
| Cobot (Berlin, Europe) | "most intuitive", lightweight, community-first, strong European compliance | small–mid independent spaces | A (Learn Cobot collection, 118 articles) |
| Optix (ex-ShareDesk) | automation-first, mobile-first member experience | growth-stage operators, niche flex verticals | A (feature pages) / A− (help center not deeply sampled) |
| OfficeRnD Flex | platform with Hub modules; also ships a separate occupant-side product (Workplace) — useful for boundary work | growing operators → enterprise/multi-brand | A (Flex help center navigation, 1000+ articles) |
| Coworks | community-first, SMB, non-office verticals (makerspaces, universities, childcare, shared labs) | small community operators | A (help-center collections + feature scope) / A− (individual articles not deeply sampled) |

## Sources

- https://www.nexudus.com/ (product scope, integrations, apps)
- https://help.nexudus.com/ + https://help.nexudus.com/llms.txt + https://help.nexudus.com/docs/glossary.md (KB index; glossary: plans/contracts/members/contacts/teams/resources/rates/benefits/passes/check-ins/visitors/floor plans)
- https://www.cobot.me/ + https://helpcenter.cobot.me/en/ + https://helpcenter.cobot.me/en/collections/2757948-learn-cobot (setup, plans, time passes, credits, resources, invoicing, payments, members/teams, analytics)
- https://www.optixapp.com/ + https://www.optixapp.com/features/membership-plans/ (plans model, feature scope)
- https://www.officernd.com/ + https://help.officernd.com/ + https://help-flex.officernd.com/en/ (Flex onboarding steps; locations/resources; billing plans vs memberships; bill runs; invoicing; operations)
- https://www.coworks.com/ + https://help.coworksapp.com/en/ (feature scope; collections incl. Occupancy, Members & Teams, Bookings & Events, CRM)

All fetches succeeded on 2026-09-07. No source-access limitation on the main claims; Optix and Coworks were sampled at feature/collection level rather than article level (noted in Uncertainties).

## Product Observations

### Nexudus (evidence layer A unless noted)

Key observations:

- **Location is the operating unit.** Each location has its own Admin Panel and its own Members Portal; multiple locations form a "network" with an extra network location for global settings. Location-level settings include taxes, payment processing, notifications.
- **Record taxonomy (from the official glossary):**
  - Customers = members + contacts. Individual customer (a person) vs company customer (business entity linked to a person as point of contact).
  - Contacts = customers with no active contract. "Contacts automatically become members when they sign up to a plan and get a contract."
  - Members = customers with at least one active contract.
  - Visitors = people registered to visit a customer at a date/time; tour bookings also create visitors; "Turning Visitors Into Customers" documented.
- **Plan vs Contract (glossary, directly stated):** "Plans are the template for the subscription while the contract is the individual agreement you have with each customer." Plans auto-renew on a predefined period; a contract is generated per signup from the plan's settings and can be edited (invoice date, invoice period), prorated, upgraded/downgraded, copied, cancelled, price-scheduled, frozen (paused) and resumed.
- **Inventory** = the things you sell: products (one-off and recurring), passes (day passes, time passes, pay-as-you-go passes), resources and floor plans.
- **Resources / Rates / Resource types:** resources are rooms, desks, or any area bookable at a price; rates are shared across resources of the same type; a resource type controls which resources can be booked with time or money credits. Rates can target all customers, contacts only, members only, or members on specific plans. Combined resources let several rooms be booked as one. Resource rules/limits, shifts/open hours, features, late-cancellation fees, dynamic pricing documented.
- **Benefits:** time credits, money credits, printing credits, and passes added to plans/products; benefits never add direct charges — their value is priced into the plan.
- **Bookings:** time slots on a resource; free or charged per rates; statuses incl. tentative with admin approval; booking products (extras); attendee check-in/out; invoicing bookings.
- **Floor plans:** visual floors with units (desks, offices) connectable to resources; "admins assign specific floor plan items such as desks and offices to customer contracts" — assignment is contract-anchored.
- **Check-ins:** manual, Wi-Fi (RADIUS/MikroTik), RFID cards, door access control; access tokens for Wi-Fi; failed check-in monitoring; passes connect to access systems ("let customers holding certain passes unlock doors").
- **Finance:** invoice periods; draft invoices; invoice-as (bill a customer's fees to another payer); transferring invoices; cancel vs refund vs void; credit balances; deposits (refundable, automatically credited on the cancellation date); discounts (codes, referral, team); tax rates incl. per-location and per-customer personal tax rates; chart of accounts/ledgers; card gateways vs direct-debit gateways (Stripe, GoCardless, PayPal, Klarna, Worldpay, Forte, MercadoPago…); SCA.
- **Teams:** groups of customers sharing discounts, credits, passes, Wi-Fi; exactly one "team paying customer"; multiple team administrators; team billing merge; charging members instead of the paying customer.
- **CRM/community:** opportunities with boards/stages, proposals with documents + e-sign, enquiries, reminders, tasks; events with tickets/waiting lists, articles/news, discussion boards, virtual rooms, perks, newsletters, surveys, courses; help desk; deliveries (mail) with collection reminders; ePOS kiosk (NexKIOSK), room display (NexBoard), check-in kiosk (NexIO), mobile member app (Passport), mail app (NexDelivery) — companion apps are vendor-specific (L3).
- **Visitor management** and identity checks documented.

### Cobot (evidence layer A)

Key observations:

- Setup model: register a space account; space settings (tax rates, T&C, invoice settings, privacy/DPA); multiple spaces manageable from one portal; "managing members across multiple locations" (members with access to all locations).
- **Membership Plans** collection (title-level, directly observed): "Plans describe the resources, amenities and extras your members receive – and for what fee – on a monthly basis." Monthly extras (lockers/keys), booking credits ("free resource hours or monetary credits as part of their membership plan, with discounted rates once credits run out"), deposits and signup charges, discounts/promo rates, annual/yearly plans, "Companies With Long-Term Leases and Employees" (plans longer than 1 month), pausing memberships, cancel vs delete vs reactivate, bulk plan changes, plan-level approval queues.
- **Time passes**: hourly/daily/weekly access passes sold or granted; time-pass vouchers.
- **Drop-in passes / Products**: day passes, half-day passes, trial days "for one-time visitors and everyone else seeking maximum flexibility without committing to a recurring membership"; discount codes; **allocatable resources**: "Rent out offices, fixed desks and other resources to members and teams – and get an overview of occupancy, availability" (offices-as-resources with allocation; migration of offices into Cobot as allocatable resources).
- **Booking calendar**: resources reservable hourly by members and externals; advanced pricing (fixed rates, discounts, price caps); open hours and calendar blockers; booking extras; inviting participants; members can edit bookings until they start, admins anytime; .ics feeds; Google/Outlook/Liquidspace sync.
- **Invoicing**: automated member invoicing ("Cobot effortlessly generates and dispatches member invoices"); multiple tax rates/currencies; accounting codes; free-form invoices for non-members; prorated invoices; one-time charges and credits; invoicing ahead of billing date; retention rates; payment reminders; correction invoices; "Pay Now" links (semi-automated); country e-invoicing: Germany (XRechnung-class e-invoices), Spain VERI*FACTU, Poland KSeF, France e-invoicing, Swiss QR-bill.
- **Payments**: automated payment methods (monthly auto-collection), manual payment methods (cash/check/bank transfer), making payment methods required at signup, charging at signup/in advance, refunds for members and visitors.
- **Members & contacts**: members dashboard; self-signup via homepage/plan-specific forms; check-ins ("Get a clear picture of who uses your space and when"); checking in members' guests; pausing/canceling/reactivating; **"Revoking Access When a Payment Fails: Cobot doesn't revoke member access for payment failures – it's up to spaces to do this manually"** (documented behavior); member portal (manage plan, bookings, payments); community directory; teams (team plans; converting "paid-for" members to teams); contacts management (drop-ins, external bookers, event attendees → convert to members).
- **Communication**: automated + manual emails, newsletters (recommends Mailchimp), Slack invites, help desk.
- **Analytics**: occupancy/usage/growth analytics; exports of members, invoices/revenue, attendance, bookings.
- **Access control**: "controlling who gets access to what, when. Manage permissions and integrate with the leading access control providers" (Kleverkey testimonial for doorlocks); meeting-room display add-on; tip-jar add-on (member purchases charged to invoice).
- Events: member and public registration, event booking and ticketing; external bookings feature (selling rooms to non-members) with its own help collection.

### Optix (evidence layer A for the plans page; A− for scope via feature index)

Key observations:

- **Plans** = "recurring subscriptions that you can create and assign to users or teams. They help organize memberships and facilitate recurring revenue." Plan customization: price; included resources, check-ins, products; billing date; free trial; custom invoicing cadence; custom currency; custom start date. Plan templates for recurring offers; plans purchasable in-app (mobile-first) or on the website; plan analytics to forecast recurring revenue.
- Feature surface (from the site's own feature index): Resource Booking, Desk Booking, Meeting Room Booking, **Assignments (dedicated)**, Billing & Payments, Invoicing, Plans, Check-ins, CRM (leads/tours), Community Feed, Directory and Messaging, Issue Reporting, Events, Visitor Management, Marketplace, Perks, Web Widgets, White-labeled mobile app, Multi-location, Analytics, Floor plan (introduced Oct 2025 per blog), Automations engine (workflow automation positioned as the differentiator).
- Automation framing: end-to-end member-journey automation (lead capture → nurturing → onboarding → booking → invoicing → upsell) — philosophy-level, not structural (L3).
- **Vertical generalization is explicit**: solutions for coworking, co-warehousing, flex spaces, medical coworking, shared kitchens, shared salons, golf simulators, micro-gyms, coworking+childcare, creative/therapist spaces. The product itself asserts the model holds for shared space of any kind — supports an office-agnostic L0.

### OfficeRnD Flex (evidence layer A)

Key observations:

- Onboarding checklist (official): set up account → configure organization billing settings → set up services → create floor plans and set up resources → import customer and membership data → set up integrations → customize member tools. The setup order itself reveals the model: space → billing → plans → resources → people.
- **Locations & Resources**: locations; floors; floor plans (sketch/design, add resources, split an office into two, change meeting room ↔ private office); resource types (default + custom); **assignable vs bookable resources** ("Make Hot Desks Bookable", "Assign Resources – Desks and Private Offices", "Make a resource type both bookable and assignable"); hierarchical meeting rooms; flexible capacity; amenities on resources; parking spaces; resource statuses; relocation and resource-history merge/review; "Manage Two Companies Using One Private Office".
- **Billing Plans vs Memberships (official distinction):** "The Difference Between a Billing Plan and a Membership" — plans are the offer; memberships are the instance assigned to a member or a company. Fixed vs month-to-month memberships; membership approval; price adjustments; cancel or pause; membership cancellation requests; locked memberships; **assign memberships to resources** (private-office membership bound to a specific office); add a membership for another location; adjust booking credits on an existing membership.
- **Resource rates**: hourly and daily rates; "billing plans vs resource rates" — recurring membership revenue vs per-use revenue as two distinct revenue lines.
- **Invoicing machinery (deepest of the sample)**: invoice statuses; financial document types (invoices, credit notes, statements, receipts); bill runs ("How bill runs create your monthly invoices"; manual execution; cancellation); billing options for recurring memberships and one-off fees; proration; invoice due dates; billing lock date protecting finalized invoices/payments; single vs separate invoice generation rules; invoice numbering by location; eInvoicing activation with country-specific requirements; processing fees for card payments (location-specific); late fees for overdue invoices; bad debt recording; markups; revenue accounts and targets; multi-currency with dynamic exchange rates; multi-location payment details; overpayment allocation; clearing-account reconciliation of bulk provider payments; deposits (record, allocate to invoice, refund with credit note); tax rate priority per location/customer.
- **Operations**: companies (with active-members seat allowance; contact person vs billing person permissions); members (status changes, privacy settings, merge profiles); opportunities; forms; guided tours scheduling; "Who's In" (who has checked in today).
- Payments: stored payment details charging; payment receipts; payment status management incl. marking failed; NACHA compliance for ACH.
- The vendor ships a **separate occupant-side product** (OfficeRnD Workplace: desk/room booking for employees of one company) — direct structural evidence for the operator-vs-occupant boundary.

### Coworks (evidence layer A− / scope-level)

Key observations:

- Feature scope (own site): Member App, Billing, Events, Leads Database (CRM), Booking Rooms & Equipment, Day Passes, Booking Credits, Visitor Check-Ins + Management, Member Check-Ins, Tour Requests, Discounts & Promo Codes, Multi-Location Management, Data & Analytics, Access Control integrations, tool integrations (Stripe, QuickBooks, Kisi, Brivo, Salto, Salesforce, HubSpot, calendars, Zapier).
- Help-center collections confirm structure: Billing (84 articles; "Invoices and their lifecycle"), Bookings & Events, CRM, **Members & Teams**, **Occupancy ("manage the dedicated Suites and Desks in the Occupancy tab")**, Member App, Reporting, Branding, Integrations, Getting Started.
- Audience generalization (own positioning): coworking, commercial real estate, makerspaces, universities & incubators, coworking+childcare, therapy/wellness, chambers of commerce, co-warehousing, flex office, shared labs — again office-agnostic.
- Philosophy: community-first, deliberately unbloated, mobile-first member app; SMB tier with human support.

## Cross-product Comparison

| Dimension | Nexudus | Cobot | Optix | OfficeRnD Flex | Coworks | Judgment |
|---|---|---|---|---|---|---|
| Location as operating unit | yes (per-location panels/portals; network layer) | yes (space = account; multi-space portal) | yes (multi-location feature) | yes (locations → floors → floor plans) | yes (multi-location management) | **Core (L0)** — all five |
| Space units: desks/offices/rooms as managed records | resources + floor-plan units connectable to resources | resources + allocatable offices/fixed desks | resources + floor plan + assignments | resource types; assignable vs bookable; flexible capacity | rooms/equipment + Occupancy (suites/desks) | **Core (L0)** — all five |
| Plan/subscription as recurring commercial offer | Plans (templates) → Contracts (instances) | Membership Plans (+ time passes) | Plans = recurring subscriptions for users or teams | Billing Plans → Memberships (assigned to member or company) | memberships/billing + day passes | **Core (L0)** — all five; template-vs-instance split varies (Nexudus & OfficeRnD make it explicit; Cobot/Optix fold it) |
| Plan instance anchored to person AND company/team | members + company customers + teams (paying customer) | members + teams (team plans) | users or teams | member or company; companies with seat allowance | members & teams | **Core (L0)** — the membership hangs off a person or an organization |
| Booking of space with pricing rules | bookings + rates + credits + rules | booking calendar + advanced pricing + credits | resource/desk/meeting booking | bookings + hourly/daily resource rates | bookings + booking credits | **Core (L0)** — all five |
| Standing allocation (assignment) of dedicated space | floor-plan items assigned to contracts | allocatable resources for offices/fixed desks | Assignments (dedicated) | assign memberships to resources | Occupancy tab (suites/desks) | **Core (L0)** — all five (booking and assignment are the two usage modes) |
| Check-in / presence | manual/Wi-Fi/RFID/door; failed check-ins | manual check-ins; guests; attendance exports | check-ins feature; kiosk check-in | "Who's In"; visitor hub | member + visitor check-ins | **Common (L1)** — universal in sample but a space can operate without it |
| Door access / Wi-Fi integration | passes → access systems, Wi-Fi | access-control integrations; Wi-Fi auth | Kisi integration | door access integrations collection | Kisi/Brivo/Salto | **Common (L1)** |
| Recurring automated invoicing + payment collection | yes (deepest gateway breadth) | yes (automation + Pay Now links) | yes (invoicing cadence per plan) | yes (bill runs; deepest document machinery) | yes (invoice lifecycle) | **Core (L0)** — operator billing is universal and definitional |
| Usage-based billing of bookings | yes | yes (price caps, extras) | yes | yes (resource rates vs plans distinction) | yes | Common (L1) — near-universal but day-pass/membership-only operators exist |
| Deposits | yes | yes | not confirmed | yes | not confirmed | Common (L1); single/dual-source → not core |
| Proration / mid-cycle changes | yes | yes | custom cadence/start date | yes (detailed) | implied by billing depth | Common (L1) |
| Tax handling & regional e-invoicing | per-location/personal tax rates | DE/ES/PL/FR/CH compliance articles | custom currency | tax-rate priority, eInvoicing, NACHA | not deeply sampled | Common (L1); specifics regional (L2) |
| Member self-service portal / app | Members Portal + Passport app | member portal + members mobile app | mobile-first branded app | member portal + mobile apps | member app | **Common (L1)** — market-defining expectation, not definitional |
| Self-serve signup + approval queue | yes | yes (signup forms; approval queue) | online purchase; free trials | purchase flows; membership approval | tour requests; signups | Common (L1) |
| Day passes / non-member revenue | day/time/PAYG passes | drop-in passes; external bookings | passes (feature list); public purchase | purchase flows incl. non-members | day passes | Common (L1) — flexibility pole, not required |
| Credits as included entitlements | time/money/printing credits | booking credits (hours or money) | included resources/check-ins in plans | booking credits on memberships | booking credits | **Common (L1)** — the entitlement mechanism is near-universal; exact credit kinds vary |
| Community: directory, events, messaging/feed | rich (boards, articles, events, perks…) | directory; events; Slack handoff | directory, feed, messaging, events | community engagement (Experience Hub) | events; member app community | **Common (L1)** — philosophically central to coworking, structurally secondary |
| CRM / leads / tours | opportunities, proposals, e-sign, enquiries | lightweight CRM; leads→members conversion | CRM feature; automations | opportunities; guided tours | leads database; tour requests | Common (L1) |
| Visitor management | yes | guest check-in | visitor management | Visitor Hub | visitor check-ins + management | Common (L1) |
| Deliveries/mail (virtual office supply chain) | deliveries + NexDelivery app | not in sampled scope | not in sampled scope | not in sampled scope | not in sampled scope | Optional (L2) — tied to virtual-office business |
| Virtual office productization | virtual offices (own marketing pillar) | legal guide only | no | no | no | Optional (L2); vendor-leaning at Nexudus |
| Multi-site network/global settings | network location layer | multi-space portal | multi-location | multi-location billing/payment details | multi-location | Common (L1) — scale-dependent, not definitional |
| Automation engine as differentiator | workflow automations; AI agents | add-ons | automations (flagship) | AI Hub, dynamic pricing | AI prompts for reporting (content only) | Optional (L2) / vendor philosophy (L3) |
| Occupancy/usage analytics | Trends BI dashboards | analytics + add-ons + exports | plan analytics | Data Hub, revenue targets | data & analytics | Common (L1) |

## Canonical Model (abstraction hierarchy)

### L0 — Defining Invariant (deliberately minimal)

The operator-side system of record for a flexible-workspace business. Four structures; remove any one and the product stops being this Type:

1. **The space inventory under management** — one or more locations decomposed into named, managed units of workspace (desks, offices, meeting rooms, or functionally equivalent bookable/allocatable units). Remove → generic membership/subscription billing or CRM.
2. **The member holding a recurring, flexible-term membership** — a person or an organization (team/company) signed up to a plan/subscription that recurs on a defined period and can be started, changed, paused and ended on short, flexible terms rather than lease terms. Remove → room/desk/venue booking tool (occupant-side or event-side).
3. **The usage record connecting member to space** — bookings of bookable units and/or standing assignment of allocatable units, priced and governed by the membership's terms (rates, included credits/passes). Remove → subscription billing platform; the space business has no operational layer.
4. **Operator-side billing of memberships and usage** — the system generates recurring invoices for memberships and charges for usage, and records payments. Remove → workspace scheduling tool (Workplace Management Type).

Historical/market-sample check (older, regional, platform-native): a space run on spreadsheets + a paper calendar + bank transfers already exhibits all four structures (inventory list, member list with monthly plans, bookings/assignments, invoices) — no specific technology (floor-plan editors, access control, mobile apps, payment rails, e-invoicing) is required by the definition. Regional payment differences (direct debit vs ACH vs cards) and compliance differences are implementation. Niche verticals (shared kitchens, co-warehousing, medical coworking, salons — explicitly marketed by sampled products) satisfy the core without any office-specific assumption. → L0 passes.

### L1 — Common Mature Structure (market-expected, not defining)

- member self-service portal and/or branded mobile app (booking, invoices, payments, profile)
- check-in machinery (manual, kiosk, Wi-Fi, RFID, door access) and presence views ("who's in")
- access-control and Wi-Fi integrations driven by membership/plan state
- day passes / drop-in / external (non-member) booking and payment as a second revenue mode
- entitlement mechanics: included credits (time/money), passes, member-vs-visitor rates, discounts
- teams/companies: shared billing, paying customer, admins, seat management
- CRM layer: leads/enquiries, tours, opportunities, conversion to membership
- visitor management and guest check-in
- community surfaces: directory, events/tickets, messaging/feed
- analytics: occupancy, utilization, revenue, exports
- deposits, proration, plan pausing/cancellation flows, approval queues
- tax configuration, multi-currency, regional e-invoicing compliance
- integrations spine: payments (card + direct debit), accounting (QuickBooks/Xero), calendars, access hardware, Zapier/API

### L2 — Variant / Optional Structure

- virtual office / mail-handling business line
- public-facing booking storefronts and marketplaces (external demand channels)
- dynamic/peak pricing, processing fees passed to payers, markups
- multi-brand enterprise operation (portfolio roll-up, per-entity billing entities, consolidated networks)
- vertical tuning (co-warehousing, shared kitchens, medical coworking, salons, makerspaces, campus/incubator)
- automation/AI layers (lead nurture, support agents, dynamic pricing)
- hybrid-work feature drift (desk booking for a single company's employees — occupant-side)
- local compliance postures (e-invoicing regimes, receipts, fiscal QR codes)

### L3 — Vendor-specific (research notes only)

- Nexudus companion apps named Passport/NexBoard/NexIO/NexKIOSK/NexDelivery; "Trends" BI; CRM boards/stages; contract freezing terminology; invoice-as.
- Cobot tip-jar add-on; meeting-room display add-on; VERI*FACTU/KSeF named compliance articles; explicit "we don't auto-revoke access on payment failure" stance.
- Optix automation engine marketing; "1,000+ automations"; niche-solutions taxonomy; white-label app as flagship.
- OfficeRnD "Hub" module names (Flex Operations Hub, Experience Hub, Growth Hub, AI Hub, Visitor Hub, Data Hub); FlexIndex; Randi support bot; billing lock date as named control.
- Coworks Occupancy tab naming; "quietly runs without needing my attention" positioning.

## Vendor-specific Findings

- Cobot documents a deliberate behavior: payment failure does not automatically revoke member access (operator's manual decision). Treating auto-revocation as universal would be wrong; it varies.
- Nexudus and OfficeRnD both formalize the template/instance split (Plan→Contract; Billing Plan→Membership); Cobot and Optix let plans carry most of that semantics directly. The canonical model should keep both layers conceptually (offer vs active subscription) without forcing two objects.
- OfficeRnD's dual product line (Flex vs Workplace) is the clearest market evidence that operator-side and occupant-side workspace software are separate Types sharing booking mechanics.
- OfficeRnD supports two companies sharing one private office; Nexudus supports combined resources (rooms booked as one) — capacity-sharing edge cases exist but are product-level.

## Boundary Findings

| Neighboring Type | Relationship | Distinction / "remove what → becomes that Type" |
|---|---|---|
| Workplace Management Platform / Desk Booking | adjacent (shared booking mechanics) | Occupant-side: one company manages its own space for employees; no members, no plans, no operator billing. Remove members+memberships+operator billing → Workplace Management. OfficeRnD ships both as separate products (direct evidence). |
| Hotel PMS | adjacent (hospitality operator system) | Transient nightly stays, guests, room status/housekeeping, night audit vs recurring flexible memberships, work use (hourly/day/month), no housekeeping cycle. Change the commercial relationship to per-night stays with room readiness cycles → Hotel PMS. |
| Commercial Property Management | adjacent (landlord side) | Lease-based tenancy: long fixed terms, rent rolls, CAM reconciliation vs month-to-month plans, day passes, community. Lengthen terms and switch to lease administration → Property Management. Cobot's "long-term leases" plan support shows the shared edge. |
| Membership Management System / AMS | adjacent (membership machinery) | AMS manages member records, renewals, benefits for an association with no space inventory and no space usage. Remove space inventory + usage → Membership Management. |
| Venue Management System | adjacent | Event-driven space booking (functions, rentals) vs membership-driven flexible access. Remove recurring memberships → venue booking. |
| Amenity Booking Platform | weaker adjacent | Single-amenity scheduling for an existing population; no commercial membership layer. |
| Resource Calendar / Enterprise Resource Scheduling | capability overlap | Pure scheduling without the commercial (plan/billing) layer; flex software contains it as a capability. |
| Building Access & Visitor Management | integration surface | Access control is consumed via integration; it is not the record system of the workspace business. |
| Subscription Billing Platform | capability overlap | Billing machinery without space inventory/usage; flex software embeds subscription billing as one of its four pillars. |
| Short-term Rental Management | adjacent (operator-side rental) | Nightly/short-stay dwellings vs workspace membership; different unit economics and lifecycles. |

Type integrity judgment: the leaf is a legitimate, independent Application Type — not a variant of property management or a capability of billing software. Its four L0 structures jointly distinguish it from every neighbor; no neighbor has all four.

## Uncertainties

- Optix and Coworks were researched at feature/collection scope rather than deep article scope; claims attributed to them are about scope and model, not fine mechanics. Their billing-rule details (e.g., proration behavior, deposit handling) were not directly verified → keep such mechanics generic in the final document.
- Whether any mature product truly lacks usage-based billing (booked-room charging) — all sampled products support it, but membership-only or all-inclusive spaces may not use it; kept as Common (L1), not Core.
- No legacy/regional small vendor directly examined (e.g., early-2010s tools, regional Asian products); the historical check relies on the structural argument (spreadsheets satisfy L0) plus Cobot/Nexudus longevity (both founded early 2010s), not on direct observation of a legacy product.
- Community feature depth varies widely; the final document treats community as standard capability, not definition — if future evidence shows membership-without-community products dominating some region, L0 remains unaffected (community was never in L0).
- Team/company billing rules (who pays, seat allowances) differ per product; details kept vendor-specific.

## Final Synthesis

A Coworking / Flexible Workspace Management application is the operator-side system of record for running a shared-workspace business. Its world is built from four permanent structures: (1) a space inventory — locations decomposed into bookable and/or allocatable workspace units; (2) members — people or organizations holding recurring, flexible-term plan subscriptions; (3) usage — bookings and standing assignments that connect members to space under plan-governed pricing and entitlements; and (4) operator billing — recurring invoicing and payment collection for memberships and usage. Around this core, mature products add member self-service (portals/apps), presence and access machinery (check-ins, door/Wi-Fi integration), a second revenue pole of day passes and external bookings, a light CRM for lead→member conversion, community surfaces (directory, events, messaging), and occupancy/revenue analytics. The deepest implementation differences are billing machinery depth (bill runs, credit notes, e-invoicing regimes) and product philosophy (automation-first vs community-first vs platform-suite), which are variant axes, not definitional ones. The Type is office-agnostic in the market itself (shared kitchens, co-warehousing, medical coworking, salons run on the same four structures) and is cleanly separated from occupant-side workplace software by the presence of members, memberships, and operator billing.
