# Research Notes — Property Showing Platform

## Research Goal

Understand what a Property Showing Platform really is by studying real products: what the system of record is, who the parties are, how a viewing request becomes a completed (or missed) visit, what rules govern it, and where the Type's boundaries lie against the Property Listing Platform (its upstream venue sibling), generic appointment scheduling, and the other §17 real-estate machinery Types.

## Initial Boundary

Working hypothesis at start:

- A Property Showing Platform coordinates **in-person viewings of properties on the market** (for sale or for rent) between a requesting side (prospective buyer/tenant, often via their agent) and a controlling side (listing agent / owner / landlord / property manager).
- Most likely confused with:
  - **Property Listing Platform** (§17, processed) — the public venue of offers; prior pass left a forward note: "portals embed light application/screening/viewing depth as venue features; the standalone Types own the machinery's system of record."
  - **Appointment Scheduling Application** (§03.09, processed) — generic booking machinery (availability, self-booking, confirmations).
  - **Amenity Booking Platform** (§17, processed) — building-owned shared assets, occupancy-derived bookers.
  - **Real Estate Brokerage CRM** (§17, unprocessed) — clients/deals system of record.
  - **Property Inspection Application** (§17, processed) — professional condition inspections.
  - **Rental Application Platform / Tenant Screening Platform** (§17, unprocessed) — downstream application/screening machinery.
- Unknowns at start: exact product landscape; whether self-showings are definitional or variant; the role of MLS integration; whether feedback is definitional; open-house handling.

## Research Questions

1. What is a "showing" as a record? What states does it carry?
2. Who are the parties, and how does the two-sided confirmation loop work?
3. What property-level showing configuration exists (availability, lead times, restrictions, access instructions)?
4. How do requests arrive (MLS links, listing-site inquiries, phone, syndication)?
5. What access machinery exists (accompanied, lockbox, smart lock, self-guided)?
6. Is feedback collection definitional or common?
7. What does the listing side's operational surface look like (calendar, worksheet, reports)?
8. What differs between the sales side and the leasing side of the market?
9. Where are the boundaries vs the neighboring Types listed above?

## Representative Products

Selected for market representativeness, documentation quality, different product philosophies, and different customer tiers:

| Product | Side of market | Philosophy / tier |
|---|---|---|
| **ShowingTime (Zillow ShowingTime+)** | residential sales (agents, teams, offices, brokers, MLSs) | the incumbent showing-management service; MLS-integrated; human appointment center + online scheduling |
| **ShowMojo** | rental leasing (property managers, landlords) | automation-first leasing platform; showing management as one pillar; self-guided tours; proprietary access hardware |
| **TenantTurner** | rental leasing (property managers) | self-scheduling + self-showing; pre-qualification gate; 24/7 live answer tier |
| **ShowingHero** | rental + sale (property managers) | prospect-driven automation; no call center by design; per-active-listing pricing |

Rejected/abandoned: **Aligned Showings** (Lone Wolf) — the natural second sales-side sample; main site is a JS shell, support site transport-errored, support page rendered only a contact form (3 attempts). Recorded as a sourcing limitation; sales-side operational depth rests on ShowingTime's KB alone.

## Sources

Fetched 2026-09-09 (Tier 1 unless noted):

- ShowingTime — https://www.showingtime.com/ (home) · https://showingtime.com/solutions/showings-and-offers (solution page) · https://showingtime.com/resources/support and https://showingtimeplus.com/solutions/showings-and-offers/support (support + FAQ)
- ShowingTime Appointment Center Knowledge Base — https://apptcenter.uservoice.com/knowledgebase (topic index) · https://apptcenter.uservoice.com/knowledgebase/articles/444110-appointment-rules · https://apptcenter.uservoice.com/knowledgebase/articles/523949-scheduling-a-single-showing
- ShowMojo — https://hello.showmojo.com/ (home) · https://hello.showmojo.com/solutions/showing-management/ · https://hello.showmojo.com/property-manager-faqs/
- TenantTurner — https://www.tenantturner.com/ (home) · https://help.tenantturner.com/ (help center index) · https://help.tenantturner.com/exploring-tenant-turner · https://help.tenantturner.com/what-happens-when-a-lead-inquires-through-an-online-listing (Blueprint: lead cycle)
- ShowingHero — https://showinghero.com/ (home; Tier 2 marketing surface) · https://showinghero.com/faq (FAQ)

Unreachable: alignedshowings.com (JS shell), support.alignedshowings.com (transport error), alignedshowings.com/support (JS shell). ShowMojo's "Leasing Knowledge Base" footer link 404s; PM FAQ used instead.

## Product Observations

### ShowingTime (Zillow ShowingTime+) — evidence layer A unless noted

Positioning (Tier 2, vendor claim): "showing management and market data tools for agents, teams, brokers and MLSs"; "most widely used showing management scheduling technology in residential real estate"; FAQ claims 1.2M active listings subscribed and ~4M showings managed per month (vendor-scale claims, not independently verified).

- **Products/services**: Appointment Center (agents; 24/7/365 live call center of "appointment specialists" handling showing requests received online or by phone); Front Desk (office managers/team leads); ShowingTime for the MLS (members "schedule multiple appointments online and organize them by driving route"); LiveConnect (live call answering add-on); On-Demand and Part-Time service modes (office handles business hours; after-hours routed to the Appointment Center).
- **Scheduling flow (buyer's agent)** — two entry paths: through the MLS (find listing → "Schedule a Showing" link → ShowingTime scheduling screen) or through ShowingTime directly (search by street/MLS number). Then: review listing details and confirmation preferences → agree to terms → pick a date/time slot. The slot grid encodes the listing's rules: white = available; gray = "Suggested Lead Time"; black = unavailable (required lead time, showing restrictions, past times); shaded = minimum appointment length. Attach buyer(s); Agency Type and buyer name required in some markets. Multi-unit listings expose unit selection.
- **Appointment status model**: after submitting, the requester sees one of two states — the appointment "requires confirmation from any/all contacts" (pending) or requires no confirmation (confirmed). Related flows: Proposing a New Time; scheduling from a cancelled or declined appointment; Curb Showings (article exists; content not fetched — held lightly).
- **Listing worksheet / appointment rules** (the property's showing configuration): Showing Restriction (blocks appointments; the reason is shown to the agent trying to schedule) and Showing Exception (changes the confirmation process for a window: rule contacts, required/suggested lead times, access information). Rules are Timed or All-day, One-time or Repeating; managed in list and calendar views. "Allow Overlapping Showings = no" produces buffer time between showings.
- **Contacts**: Adding Buyers, Viewing Buyer Activity, Seller Management (seller notification preferences). Buyers are held as records attached to appointments.
- **Feedback**: dedicated KB section — Creating Feedback Templates, Feedback Management, Submitting Feedback; FAQ article "My seller says they are not getting feedback" — feedback flows to sellers.
- **Access**: access information held on the listing/rules; lockbox integrations (Master Lock, igloohome); calendar sync; two-way text messaging; message center.
- **Reports**: Activity on Comparables, Agent Activity, Agent Listings, admin reports; listing activity reports marketed on the home page.
- **Adjacent capabilities**: Offer Manager (side-by-side offer comparison, offer forms, auto-forward to clients); Offer Registration for Canada; Pricing Benchmark Report; Target Market Analysis; MarketView Broker (recruiting); MarketStats. Inspectors and appraisers can be enabled to schedule online in many MLSs. Agents call 800-SHOWING for appointments/confirmations; the number is placed in the MLS listing's showing instructions. Billable-listings toggle: showing management can be turned off for lots/land/commercial.

### ShowMojo — evidence layer A

Positioning: "automated leasing platform"; Showing Management is one pillar beside syndication, lead generation, screening, smart locks, analytics, live answering.

- **Setup ("Set It Up Once")**: define showing rules — showing types, hours, lead time, buffers, approvals, blackout dates; organize scheduling on one calendar or multiple, each with its own settings; select tour options — self-guided, agent-assisted, virtual, group, occupied-unit — by property, calendar, listing group, or account; import or sync listings (two-way PMS sync or bulk import).
- **Run ("Let ShowMojo Do the Rest")**: prospects self-schedule based on rules and availability; the system confirms, reminds, reschedules/cancels, and provides day-of details; coordination when needed — tenant/owner approval, backup routing, escalation to humans.
- **Inquiry flow (PM FAQ)**: prospect inquires by phone/email/text → automatic response with customized messaging → available showing times presented from configured availability → prospect self-screens via qualification questions → selects a time → automated confirmations and reminders → for self-guided tours, access coordinated through integrated smart locks/lockboxes with a time-limited code → after the showing, automatic follow-up collects feedback. "Your team is involved only when the situation calls for it."
- **The gate**: pre-screening questions (income, pets, move-in timing, etc.) as a hard gate or configured per listing/listing group; prospects who don't meet criteria are automatically blocked with a polite message. Tenant/owner approval can be required before showings (occupied units, owner-managed properties). Accompanied showings are "routed to the appropriate agent's calendar."
- **No-show machinery**: automated confirmations and reminders; a pre-confirmation step (the showing agent doesn't leave for the property until the prospect confirms they're on their way); cancelled prospects are prompted to reschedule rather than dropping out.
- **Access hardware**: MojoBox (proprietary digital lockbox) and MojoLock (smart deadbolt); grant/revoke access remotely; identity verification, phone validation, geolocation controls before access.
- **Operational surfaces**: multiple calendars; listing groups (tag by community/region/owner/team); brand customization; location-aware cluster scheduling; "running late" pings that notify prospects and shift the schedule.
- **Integrations**: two-way PMS sync (AppFolio, Buildium, Rent Manager, Entrata), one-way imports (Yardi, RentCafe, Rentvine, Rentec Direct, others), XML feed, public API + webhooks, Zapier. Syndication to 50+ rental sites. Canada supported since 2013. Plans priced by average on-market listings or units under management. Live Answer human service; AI Virtual Agent (era-current). Vendor-scale claims: 1.7M+ units leased, 24M+ showings scheduled, 78M+ leads (not independently verified).

### TenantTurner — evidence layer A

Positioning: leasing automation (listings, leads, showings, data & reporting).

- **Lead cycle (Blueprint article, 8 steps)**: lead inquires through an online listing (own site, Zillow, Zumper, etc.) → TenantTurner emails the lead an invitation to start scheduling → lead answers pre-qualification questions (team-set requirements) → if qualified, chooses appointment options based on the availability the team sets; if disqualified, sees a message stating they cannot move forward → appointment set → email calendar invite with date/time/location → roughly 24 hours prior (adjustable in account settings) a confirmation request is sent → once confirmed, showing instructions are released (customizable: how to access the property, who to contact).
- **Showings**: in-person or secure self-showings via electronic lockboxes; instant alerts, reminders, follow-up; "We'll cancel any unconfirmed appointments to save you time and reduce no-shows."
- **After the viewing**: collect feedback on the rental; send applications; compile owner reports.
- **Leads**: customizable pre-qualification; lead waitlists if a unit isn't ready; alerts on high-interest leads; Live Answer — 24/7 human support for leasing calls, scheduling, troubleshooting self-access (Ultra plan).
- **Access**: Seros smart locks and lockboxes (own hardware line); self-access hardware options; also vendor access.
- **Integrations**: PMS (Rent Manager, AppFolio, Buildium, Rentvine; a "Buildium Showings Coordinator" integration), Zapier (8,000+ apps). Syndication to 20+ sites. Reporting: real-time performance, owner reports, lockbox-use reporting.

### ShowingHero — evidence layer A for FAQ content; page is a Tier-2 marketing surface

Positioning: "leasing and showing automation platform"; serves "your sale or rental listing" and "pre-screen tenants or buyers" (both sides of the market claimed).

- **Showing types (FAQ)**: prospect-proposed showings "the traditional way"; agent showings scheduled on agent mini-calendars (created "based on preference and priorities"); self-showings via a "safe, verified and secure electronic smart box system."
- **Self-showing security**: multiple verification levels; verify/screen/validate each prospect; entry/exit notification to the manager; geo-fencing features to reduce scams/fraud.
- **Pre-screening**: customizable questions; only prospects who pass the manager-approved screening can schedule; qualified prospects nurtured with customized touch points.
- **Communications**: alerts plus email/SMS; acknowledges and responds to all leads 24/7 with a scheduling link; communicates with "your agents, occupants and prospects to schedule, confirm, remind, follow-up"; 50+ customizable message templates.
- **Reports**: dashboard with top-line analytics; reports by tenant, showings, property, date, showing type.
- **Integrations**: PMS imports (Propertyware, AppFolio, Buildium). No call center "by design" — each client gets a dedicated phone number; calls route to the office or client success team. US + Canada. Charged per active listing.

## Cross-product Comparison

| Structure | ShowingTime | ShowMojo | TenantTurner | ShowingHero |
|---|---|---|---|---|
| Showing appointment as tracked record | ✔ single showing + ShowingCart; pending/confirmed states; reschedule/decline flows | ✔ (24M+ showings scheduled; confirm/remind/reschedule) | ✔ 8-step cycle ending in calendar invite + confirmation | ✔ schedule/confirm/remind/follow-up |
| Property-bound showing rulebook | ✔ listing worksheet: restrictions/exceptions, required/suggested lead times, buffers, overlapping control, access info | ✔ rules: types/hours/lead time/buffers/approvals/blackouts, per property/calendar/group | ✔ team-set availability + customizable showing instructions | ✔ times/days open + agent mini-calendars |
| Listing-side gate over each request | ✔ confirmation from any/all contacts, or rule-driven auto-confirm; propose-new-time | ✔ approvals (tenant/owner) + rule-driven auto-confirm; escalation to humans | ✔ pre-qual gate + confirmation request; auto-cancel unconfirmed | ✔ screening approval + confirm |
| Requester side | buyer's agents (via MLS or platform) | prospects direct | prospects direct | prospects direct (+ prospect-proposed) |
| Feedback after showing | ✔ templates/management; flows to sellers | ✔ automatic follow-up collects feedback | ✔ collect feedback post-viewing | ✔ follow-up after each showing |
| Access machinery | ✔ access info on rules; Master Lock / igloohome lockbox integrations | ✔ MojoLock/MojoBox + identity/phone/geolocation verification | ✔ Seros locks/lockboxes | ✔ smart box + verification/geo-fencing |
| Self-guided tours | not observed in fetched docs | ✔ | ✔ | ✔ |
| Human service layer | ✔ 24/7 Appointment Center call center | ✔ Live Answer add-on | ✔ Live Answer (top plan) | ✖ "no call center by design" |
| Listing supply channel | MLS listing data | PMS sync + syndication 50+ sites | PMS import + syndication 20+ sites | PMS import |
| Notifications | ✔ email/text/push, two-way text | ✔ text/email | ✔ alerts/reminders | ✔ email/SMS |
| Reports | ✔ activity/agent/listings | ✔ leasing analytics | ✔ owner reports | ✔ by tenant/showing/property/type |
| Route planning / multi-showing trips | ✔ ShowingCart driving route | ✔ location-aware clusters | not observed | not observed |
| Pre-screening gate before scheduling | ✖ (agents are the trusted requesters) | ✔ hard gate | ✔ pre-qual questions | ✔ screening gate |
| Occupied-unit / occupant approval | seller notification preferences observed | ✔ tenant/owner approval | occupant communication observed (ShowingHero FAQ wording) | ✔ (communicates with occupants) |
| Adjacent capabilities | Offer Manager, market stats/pricing reports, recruiting analytics | syndication, lead gen, screening, analytics | syndication, applications, screening-adjacent | applications, nurture |

Reading: the first three rows are present in **all four** products with matching semantics — that is the candidate defining core. Everything else varies by segment (sales vs leasing), requester (agent vs prospect), supply channel (MLS vs PMS/syndication), and automation posture.

## Abstraction Layers

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The showing appointment as the unit of record** — a persistent, individually tracked request by a prospective viewer (directly, or through their agent) to view an identified property at a proposed time, carrying participants, status (requested → confirmed → completed / cancelled / no-show), and the visit's arrangements. Remove → an enquiry form on a listing page, or a bare calendar entry.
2. **The property's showing rulebook** — listing-bound configuration governing when and how viewings may occur: availability windows, required/suggested lead times, restrictions/blackouts, confirmation requirements, access instructions, occupancy constraints. Remove → generic appointment booking with no property semantics, or a listing venue with no schedule.
3. **The listing-side gate over each request** — every request is resolved against the rulebook and/or explicit approval by the controlling side (confirm / decline / propose another time); automation may execute the gate, but the listing side owns acceptance. Remove → open self-booking with no property-side control (generic scheduling), or a one-sided request box.

Jointly-held load-bearing:

- 1 alone = a viewing log / calendar of entries
- 2 without 1 = a rulebook nobody books against
- 3 without 1+2 = a generic approval workflow
- 1+2 without 3 = a self-booking board with no property-side control → drifts to Appointment Scheduling territory
- 1+3 without 2 = ad-hoc appointment coordination with no property rulebook → drifts to generic scheduling/CRM activity
- 2+3 without 1 = an access policy with no appointment memory

### L1 — Common Mature Structure (standard capabilities, not definitional)

- multi-channel request intake (MLS listing links, listing-site inquiries, phone lines)
- confirmations, reminders, reschedule/cancel, no-show tracking; auto-cancel of unconfirmed appointments (documented at TenantTurner; implied elsewhere)
- feedback collection after the showing, reported to the listing side/seller (3/4 explicit; ShowingHero follow-up observed)
- access machinery: instructions released after confirmation; lockbox/smart-lock integrations (4/4 in some form)
- prospect/buyer records and activity history
- reports/analytics (listing activity, agent activity, owner reports)
- calendar sync, mobile apps
- route planning across multiple showings (2/4 explicit)

### L2 — Variant / Optional Structure

- requester side: agent-mediated (sales) vs prospect-direct (leasing; ShowingHero claims both)
- supply channel: MLS-integrated listing data (sales) vs PMS sync + listing-site syndication (leasing)
- self-guided tours with electronic access (leasing-dominant; not observed in ShowingTime's fetched docs)
- pre-screening/qualification gates before scheduling (leasing-dominant; absent on the sales side where agents are trusted requesters)
- human service layer: 24/7 appointment centers / live answer vs "no call center by design"
- segment: residential sales vs rental leasing (ShowingHero claims both)
- geography: US/Canada observed in-sample; regional practices (e.g., agent-arranged viewings in other markets) not directly sampled
- packaging: standalone showing service vs pillar inside a leasing-automation suite vs embedded in portals/PM suites
- pricing: per-agent/office/MLS services vs per-active-listing vs portfolio plans

### L3 — Vendor-specific (research notes only)

- ShowingTime: ShowingCart™ (multi-showing driving-route cart), Offer Manager, Offer Registration for Canada, Pricing Benchmark Report, Target Market Analysis, MarketView Broker, MarketStats, Home by ShowingTime (seller guide), On-Demand/Part-Time Appointment Center service modes, 800-SHOWING number convention, billable-listings toggle, inspector/appraiser scheduling enablement, curb showings.
- ShowMojo: MojoLock/MojoBox proprietary hardware, Live Answer, AI Virtual Agent, listing-group branding, pre-confirmation "on my way" step.
- TenantTurner: Seros hardware line, Buildium Showings Coordinator integration, lead waitlists, Ultra-plan Live Answer.
- ShowingHero: geo-fencing specifics, per-active-listing pricing, dedicated client phone numbers, entry/exit notifications.

## Vendor-specific Findings

- Offer management (side-by-side offer comparison) is ShowingTime-only in this sample — adjacent capability, not Type-defining.
- Market data products (pricing benchmarks, showing-based market stats) are ShowingTime-only — a data layer built on showing activity, not the showing machinery itself.
- Proprietary access hardware (MojoLock/MojoBox, Seros) is a leasing-side differentiator; ShowingTime integrates third-party lockboxes instead.
- The human appointment center (ShowingTime 24/7; Live Answer add-ons) vs ShowingHero's explicit "no call center by design" — the service layer is a business-model variant, not a structure.

## Boundary Findings

1. **vs Property Listing Platform (§17, processed)** — RATIFIED from this side on the venue-vs-machinery seam that pass proposed: the listing platform is the pooled public venue of expiring offers (discovery, market states, interest routing); the showing platform owns the **schedule of record** for viewing that inventory — the appointment, the rulebook, the confirmation loop, feedback, access. Portals surface viewing requests as venue depth (prior pass: OpenRent viewing booking, Zillow tours); the standalone Type owns the machinery. Removal tests: strip the pooled public venue → a showing platform remains (it can run off MLS feeds or PMS imports); strip the appointment machinery → a listing platform remains.
2. **vs Appointment Scheduling Application (§03.09, processed)** — the two share the entire booking machinery (published availability, self-booking, confirmations, reminders, calendar sync). The seam is the bookable unit and the parties: here the unit is **access to market inventory bound to a listing rulebook**, the parties are transaction participants (prospects and their agents on one side; listing agent/owner/occupant on the other), and the record carries transaction semantics (buyer identity/agency, feedback to the seller, property access control). Appointment Scheduling books a **priced service from a provider catalog** with client records and appointment policies. Generic scheduling tools can host "showings" as event types; they do not own listing-bound rules, access machinery, or the feedback-to-seller loop.
3. **vs Amenity Booking Platform (§17, processed)** — amenity booking centers building-owned shared assets booked by an occupancy-derived resident population under a building rulebook; the showing platform centers market inventory viewed by outsiders under a listing rulebook. Eligibility source (occupancy vs market interest) and the viewed object (shared amenity vs for-sale/for-rent unit) decide.
4. **vs Real Estate Brokerage CRM (§17, unprocessed)** — the CRM owns clients, properties and deals; the showing platform owns the showing schedule. Buyer identity appears here as a **showing participant** (ShowingTime Contacts: buyers attached to appointments, buyer activity), and feedback/activity may flow toward CRM tools — but the deal pipeline is not this Type's record. Forward note for that pass: the listing-origin seam (CRM as listing source) and the activity-vs-deal seam.
5. **vs Property Inspection Application (§17, processed)** — professional condition inspections (inspectors, reports, defect records) vs prospect viewings. ShowingTime's inspector/appraiser scheduling enablement shows the showing platform can carry *other* property visits as appointments; the inspection's own record and report belong to the other Type.
6. **vs Rental Application Platform / Tenant Screening Platform (§17, unprocessed)** — downstream machinery. Showing platforms embed **light pre-screening as a scheduling gate** (ShowMojo hard gate, TenantTurner pre-qual questions, ShowingHero screening); the application and screening **system of record** is the sibling Type. TenantTurner hands off post-viewing to applications. Forward note for those passes.
7. **vs open-house sign-in tools** — the open house is a drop-in flow without an appointment; dedicated open-house tools exist in the market but were not fetched in this pass. Held as an adjacent surface, unasserted (see Uncertainties).

## Historical / Market-Sample Check

Before showing software, viewing appointments were arranged by phone through the listing agent's office or a centralized showing desk; the paper listing worksheet (showing instructions, restrictions, access notes) is the ancestor of the digital listing rulebook, and the showing call center is the ancestor of the automated gate. All three L0 structures hold for a phone-based showing desk with a paper worksheet: appointments recorded, property rules consulted, listing side confirms. Regional practices where the estate agent arranges viewings from portal enquiries also satisfy the core — with the portal owning the venue, not the schedule. The definition does not depend on MLS integration, lockboxes, apps, or self-showings. Check passes.

## Uncertainties

- **Aligned Showings unreachable** (3 attempts: JS shell, transport error, JS shell). The sales side is evidenced deeply by ShowingTime alone; corroboration for the shared structures comes from the leasing-side products. Sales-side-specific claims are calibrated accordingly.
- **ShowingHero** evidence rests on its marketing pages + FAQ (no help center found); observations held at moderate strength.
- **Open-house handling** not directly evidenced in the sample; dedicated open-house tools not fetched. Held as adjacent, unasserted.
- **Regional (non-North-American) showing practice** not directly sampled; the historical/regional check is reasoning over the sampled structures, not fetched evidence.
- **Curb showings**: article title observed in ShowingTime's KB; content not fetched. Held as a product-specific exception, lightly.
- **Vendor scale claims** (ShowingTime 1.2M listings / 4M showings per month; ShowMojo 24M+ showings) are vendor-published, not independently verified — used only as positioning signals.
- Exact numeric defaults (lead times, confirmation windows) are documented only where a source states them (TenantTurner's ~24-hour confirmation request, adjustable); not generalized.

## Final Synthesis

The Property Showing Platform is the **showing schedule's system of record** for properties on the market. Its defining core is three jointly-held structures: the showing appointment as a persistent tracked record; the property-bound showing rulebook that governs when and how viewings may occur; and the listing-side gate that resolves every request (confirm / decline / propose another time), whether executed by a human or by automation. Around that core, mature products add request intake from multiple channels, confirmation/reminder/no-show machinery, post-showing feedback reported to the listing side, access machinery (instructions, lockboxes, smart locks, self-guided tours), prospect/buyer records, reports, and route planning. The Type splits into two market poles — MLS-integrated sales-side showing management (agent-mediated requests) and leasing-side automation (prospect-direct self-scheduling, commonly with pre-screening gates and self-guided access) — sharing the same core. The seam against the Property Listing Platform is venue-vs-machinery; against Appointment Scheduling it is market-inventory-access-with-transaction-semantics vs priced-service-catalog; against the application/screening siblings it is scheduling-gate vs system-of-record.
